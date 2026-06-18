import React from 'react';
import { getCurriculumNotes, getNotesByQuestionType } from '../../../../utils/curriculumNotesMapping';
import {
    buildEmptyJournalAnswer,
    buildEmptyWordbankAnswer,
    getCorrectMap,
    getExpectedByCellId,
    isNumericExpected,
    normalizeText,
    toNumber
} from '../../grade11/accounting/utils/accountingHelpers';

import MCQRenderer from '../../grade11/accounting/renderers/MCQRenderer';
import TypedRenderer from '../../grade11/accounting/renderers/TypedRenderer';
import CalcRenderer from '../../grade11/accounting/renderers/CalcRenderer';
import WordbankTableRenderer from '../../grade11/accounting/renderers/WordbankTableRenderer';
import JournalRenderer from '../../grade11/accounting/renderers/JournalRenderer';

const Grade12AccountingPractice = ({
    onBack,
    subskills,

    g12AcctVisualAidsOpen,
    setG12AcctVisualAidsOpen,

    g12AcctPracticeDifficulty,
    setG12AcctPracticeDifficulty,
    g12AcctPracticeSubskill,
    setG12AcctPracticeSubskill,
    g12AcctPracticeSeed,
    setG12AcctPracticeSeed,

    fetchGrade12AccountingPractice,
    g12AcctPracticeLoading,
    g12AcctPracticeError,
    g12AcctPracticeQuestions,

    g12AcctPracticeAnswers,
    setG12AcctPracticeAnswers,
    g12AcctPracticeFeedback,
    setG12AcctPracticeFeedback,

    renderGrade12AccountingVisualAids,
    hideConfig = false,
    currentIndex = 0,
}) => {
    // Current question based on index from Registry/Shell
    const question = g12AcctPracticeQuestions?.[currentIndex];

    // We can use a local state for showing notes if needed, or just rely on the global visual aids
    const [showHelpPanel, setShowHelpPanel] = React.useState(false);

    // Get curriculum notes for current question
    const getCurrentNotes = () => {
        if (!question) return null;
        const archetypeKey = question?.meta?.archetype_key || question?.archetype_key;
        if (archetypeKey) {
            return getCurriculumNotes(archetypeKey);
        }
        // Fallback to journal type mapping
        const journalType = question?.journal?.journal_type || question?.journal_type;
        return getNotesByQuestionType(question.question_type, journalType);
    };

    const currentNotes = getCurrentNotes();

    const currentAnswer = g12AcctPracticeAnswers?.[currentIndex];
    const currentFeedback = g12AcctPracticeFeedback?.[currentIndex];

    const setAnswerValue = (value) => {
        const newAnswers = [...(g12AcctPracticeAnswers || [])];
        // Ensure array is long enough
        while (newAnswers.length <= currentIndex) newAnswers.push(null);
        newAnswers[currentIndex] = value;
        setG12AcctPracticeAnswers(newAnswers);

        // Clear feedback when answer changes
        const newFeedback = [...(g12AcctPracticeFeedback || [])];
        if (newFeedback[currentIndex]) {
            newFeedback[currentIndex] = null;
            setG12AcctPracticeFeedback(newFeedback);
        }
    };

    const setFeedbackValue = (value) => {
        const newFeedback = [...(g12AcctPracticeFeedback || [])];
        while (newFeedback.length <= currentIndex) newFeedback.push(null);
        newFeedback[currentIndex] = value;
        setG12AcctPracticeFeedback(newFeedback);
    };

    const checkAnswer = () => {
        if (!question) return;

        const ans = currentAnswer;

        if (question.question_type === 'mcq') {
            const ok = String(ans) === String(question.correct_index);
            setFeedbackValue(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Correct answer: ${question.options?.[question.correct_index] || ''}` });
            return;
        }

        if (question.question_type === 'typed') {
            const user = normalizeText(ans);
            if (!user) {
                setFeedbackValue({ kind: 'error', message: 'Write an answer first.' });
                return;
            }
            setFeedbackValue({ kind: 'info', message: 'Answer recorded. Compare with model answer.' });
            return;
        }

        if (question.question_type === 'calc') {
            const userN = toNumber(ans);
            if (userN === null) {
                setFeedbackValue({ kind: 'error', message: 'Enter a number first.' });
                return;
            }
            const correct = Number(question.correct_value);
            const ok = Number.isFinite(correct) && Math.abs(userN - correct) <= 0.01;
            setFeedbackValue(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Expected: ${question.unit || ''}${correct.toFixed(2)}` });
            return;
        }

        if (question.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(question);
            const a = (ans && typeof ans === 'object') ? ans : buildEmptyWordbankAnswer(question);
            const selections = a?.selections && typeof a.selections === 'object' ? a.selections : {};

            let total = 0;
            let hit = 0;
            Object.keys(correctMap).forEach((rowKey) => {
                const expected = correctMap?.[rowKey]?.['2'];
                if (expected === null || expected === undefined) return;
                total += 1;
                const got = selections?.[rowKey]?.['2'];
                if (String(got) === String(expected)) hit += 1;
            });

            setFeedbackValue(total > 0 && hit === total
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. You matched ${hit}/${total} correctly.` });
            return;
        }

        if (question.question_type === 'journal' || question.question_type === 'ledger') {
            const expectedMap = getExpectedByCellId(question);
            const a = (ans && typeof ans === 'object') ? ans : buildEmptyJournalAnswer(question);
            const cells = a?.cells && typeof a.cells === 'object' ? a.cells : {};

            const keys = Object.keys(expectedMap);
            if (!keys.length) {
                setFeedbackValue({ kind: 'error', message: 'Nothing to mark for this table.' });
                return;
            }

            let total = 0;
            let hit = 0;
            keys.forEach((cellId) => {
                const expected = expectedMap[cellId];
                if (expected === null || expected === undefined) return;
                total += 1;
                const got = cells[cellId];

                if (Array.isArray(expected)) {
                    const gotNorm = normalizeText(got);
                    const ok = expected.some((x) => normalizeText(x) === gotNorm);
                    if (ok) hit += 1;
                    return;
                }

                if (isNumericExpected(expected)) {
                    const gotN = toNumber(got);
                    const expN = typeof expected === 'number' ? expected : toNumber(expected);
                    if (gotN !== null && expN !== null && Math.abs(gotN - expN) <= 0.01) hit += 1;
                    return;
                }

                if (normalizeText(got) === normalizeText(expected)) hit += 1;
            });

            setFeedbackValue(hit === total
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. You got ${hit}/${total} correct.` });
            return;
        }

        setFeedbackValue({ kind: 'error', message: `Unsupported question type: ${question.question_type}` });
    };

    return (
        <div className="w-full">
            {g12AcctPracticeError && (
                <div className="mb-3 p-3 bg-red-50 border border-red-200 text-red-800 rounded-lg text-sm">
                    {g12AcctPracticeError}
                </div>
            )}

            {g12AcctPracticeLoading && (
                <div className="text-sm text-slate-500">Loading practice set...</div>
            )}

            {!question && !g12AcctPracticeLoading && (
                <div className="text-sm text-slate-500">
                    Click "Generate Practice Set" to begin.
                </div>
            )}

            {question && (
                <div className="space-y-4">
                    <MCQRenderer
                        question={question}
                        answer={currentAnswer}
                        setAnswer={setAnswerValue}
                        feedback={currentFeedback}
                    />
                    <TypedRenderer
                        question={question}
                        answer={currentAnswer}
                        setAnswer={setAnswerValue}
                        feedback={currentFeedback}
                    />
                    <CalcRenderer
                        question={question}
                        answer={currentAnswer}
                        setAnswer={setAnswerValue}
                        feedback={currentFeedback}
                    />
                    <WordbankTableRenderer
                        question={question}
                        answer={currentAnswer}
                        setAnswer={setAnswerValue}
                        feedback={currentFeedback}
                    />
                    <JournalRenderer
                        question={question}
                        answer={currentAnswer}
                        setAnswer={setAnswerValue}
                        feedback={currentFeedback}
                    />

                    {/* Action Buttons */}
                    <div className="flex items-center gap-3 pt-4 border-t border-slate-100">
                        <button
                            onClick={checkAnswer}
                            className="bg-indigo-600 text-white px-6 py-2 rounded-xl hover:bg-indigo-700 transition-colors shadow-sm disabled:opacity-50 disabled:cursor-not-allowed font-medium text-sm"
                        >
                            Check Answer
                        </button>
                        <button
                            type="button"
                            onClick={() => setShowHelpPanel(!showHelpPanel)}
                            className="text-indigo-600 hover:text-indigo-800 text-sm font-medium"
                        >
                            {showHelpPanel ? 'Hide Notes' : 'Show Notes'}
                        </button>
                    </div>

                    {showHelpPanel && currentNotes && (
                        <div className="mt-3 p-4 bg-blue-50 border border-blue-200 rounded-lg">
                            <div className="flex items-center justify-between mb-2">
                                <div className="text-sm font-bold text-blue-900">{currentNotes.title}</div>
                            </div>
                            <ul className="list-disc pl-5 space-y-1 text-sm text-blue-800">
                                {currentNotes.notes.map((note, idx) => (
                                    <li key={idx}>{note}</li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default Grade12AccountingPractice;
