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

const Grade12AccountingScaffold = ({
    onBack,
    subskills,

    g12AcctVisualAidsOpen,
    setG12AcctVisualAidsOpen,

    g12AcctScaffoldDifficulty,
    setG12AcctScaffoldDifficulty,
    g12AcctScaffoldSubskill,
    setG12AcctScaffoldSubskill,
    g12AcctScaffoldSeed,
    setG12AcctScaffoldSeed,

    fetchGrade12AccountingScaffoldQuestion,
    g12AcctScaffoldLoading,
    g12AcctScaffoldError,
    g12AcctScaffoldQuestion,

    g12AcctScaffoldAnswer,
    setG12AcctScaffoldAnswer,
    g12AcctScaffoldFeedback,
    setG12AcctScaffoldFeedback,
    g12AcctScaffoldShowHint,
    setG12AcctShowHint,

    renderGrade12AccountingVisualAids,
    hideConfig = false,
    isMarkingEnv = false,
}) => {
    const question = g12AcctScaffoldQuestion;
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

    const setAnswerValue = (value) => {
        setG12AcctScaffoldAnswer(value);
        setG12AcctScaffoldFeedback(null);
    };

    const checkAnswer = () => {
        if (!question) return;

        if (question.question_type === 'mcq') {
            const ok = String(g12AcctScaffoldAnswer) === String(question.correct_index);
            setG12AcctScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Correct answer: ${question.options?.[question.correct_index] || ''}` });
            return;
        }

        if (question.question_type === 'typed') {
            const user = normalizeText(g12AcctScaffoldAnswer);
            if (!user) {
                setG12AcctScaffoldFeedback({ kind: 'error', message: 'Write an answer first.' });
                return;
            }
            setG12AcctScaffoldFeedback({ kind: 'info', message: 'Compare your answer to the sample answer / visual aids.' });
            return;
        }

        if (question.question_type === 'calc') {
            const userN = toNumber(g12AcctScaffoldAnswer);
            if (userN === null) {
                setG12AcctScaffoldFeedback({ kind: 'error', message: 'Enter a number first.' });
                return;
            }
            const correct = Number(question.correct_value);
            const ok = Number.isFinite(correct) && Math.abs(userN - correct) <= 0.01;
            setG12AcctScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Expected: ${question.unit || ''}${correct.toFixed(2)}` });
            return;
        }

        if (question.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(question);
            const ans = (g12AcctScaffoldAnswer && typeof g12AcctScaffoldAnswer === 'object')
                ? g12AcctScaffoldAnswer
                : buildEmptyWordbankAnswer(question);

            const selections = ans?.selections && typeof ans.selections === 'object' ? ans.selections : {};

            let total = 0;
            let hit = 0;
            Object.keys(correctMap).forEach((rowKey) => {
                const expected = correctMap?.[rowKey]?.['2'];
                if (expected === null || expected === undefined) return;
                total += 1;
                const got = selections?.[rowKey]?.['2'];
                if (String(got) === String(expected)) hit += 1;
            });

            setG12AcctScaffoldFeedback(total > 0 && hit === total
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. You matched ${hit}/${total} correctly.` });
            return;
        }

        if (question.question_type === 'journal' || question.question_type === 'ledger') {
            const expectedMap = getExpectedByCellId(question);
            const ans = (g12AcctScaffoldAnswer && typeof g12AcctScaffoldAnswer === 'object')
                ? g12AcctScaffoldAnswer
                : buildEmptyJournalAnswer(question);
            const cells = ans?.cells && typeof ans.cells === 'object' ? ans.cells : {};

            const keys = Object.keys(expectedMap);
            if (!keys.length) {
                setG12AcctScaffoldFeedback({ kind: 'error', message: 'Nothing to mark for this table.' });
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

            setG12AcctScaffoldFeedback(hit === total
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. You got ${hit}/${total} correct.` });
            return;
        }

        setG12AcctScaffoldFeedback({ kind: 'error', message: `Unsupported question type: ${question.question_type}` });
    };

    return (
        <div className="w-full">
            {g12AcctScaffoldError && (
                <div className="mb-3 p-3 bg-red-50 border border-red-200 text-red-800 rounded-lg text-sm">
                    {g12AcctScaffoldError}
                </div>
            )}

            {g12AcctScaffoldLoading && (
                <div className="text-sm text-slate-500">Loading...</div>
            )}

            {!question && !g12AcctScaffoldLoading && (
                <div className="text-sm text-slate-500">
                    Click "Generate Question" to begin.
                </div>
            )}

            {question && (
                <div className="space-y-4">
                    {/* Note: Prompt is rendered by WorkspaceModeShell via questionSlot */}

                    <MCQRenderer
                        question={question}
                        answer={g12AcctScaffoldAnswer}
                        setAnswer={setAnswerValue}
                        feedback={g12AcctScaffoldFeedback}
                    />
                    <TypedRenderer
                        question={question}
                        answer={g12AcctScaffoldAnswer}
                        setAnswer={setAnswerValue}
                        feedback={g12AcctScaffoldFeedback}
                    />
                    <CalcRenderer
                        question={question}
                        answer={g12AcctScaffoldAnswer}
                        setAnswer={setAnswerValue}
                        feedback={g12AcctScaffoldFeedback}
                        isMarkingEnv={isMarkingEnv}
                    />
                    <WordbankTableRenderer
                        question={question}
                        answer={g12AcctScaffoldAnswer}
                        setAnswer={setAnswerValue}
                        feedback={g12AcctScaffoldFeedback}
                        isMarkingEnv={isMarkingEnv}
                    />
                    <JournalRenderer
                        question={question}
                        answer={g12AcctScaffoldAnswer}
                        setAnswer={setAnswerValue}
                        feedback={g12AcctScaffoldFeedback}
                        isMarkingEnv={isMarkingEnv}
                    />

                    {/* Action Buttons */}
                    {!isMarkingEnv && (
                        <div className="flex items-center gap-3 pt-4 border-t border-slate-100">
                            <button
                                onClick={checkAnswer}
                                disabled={!question}
                                className="bg-indigo-600 text-white px-6 py-2 rounded-xl hover:bg-indigo-700 transition-colors shadow-sm disabled:opacity-50 disabled:cursor-not-allowed font-medium text-sm"
                            >
                                Check Answer
                            </button>
                            <button
                                onClick={() => {
                                    setG12AcctShowHint(!g12AcctScaffoldShowHint);
                                    if (!g12AcctScaffoldShowHint) setG12AcctScaffoldFeedback(null);
                                }}
                                disabled={!question}
                                className="bg-white text-slate-700 border border-slate-200 px-4 py-2 rounded-xl hover:bg-slate-50 transition-colors shadow-sm disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium"
                            >
                                {g12AcctScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                            </button>
                            <button
                                type="button"
                                onClick={() => setShowHelpPanel(!showHelpPanel)}
                                className="text-indigo-600 hover:text-indigo-800 text-sm font-medium"
                            >
                                {showHelpPanel ? 'Hide Notes' : 'Show Notes'}
                            </button>
                        </div>
                    )}

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

                    {showHelpPanel && !currentNotes && (
                        <div className="mt-3 p-3 bg-gray-50 border border-gray-200 rounded-lg text-sm text-gray-600">
                            No curriculum notes available for this question type.
                        </div>
                    )}

                    {g12AcctScaffoldShowHint && question && (
                        <div className="mt-4 p-4 bg-amber-50 border border-amber-200 rounded-xl text-amber-800 text-sm">
                            <h4 className="font-semibold mb-1 flex items-center gap-2">
                                💡 Hint
                            </h4>
                            <p>{question.hint || 'No hint available.'}</p>
                            {question.guidelines && (
                                <ul className="list-disc pl-5 mt-2 space-y-1">
                                    {question.guidelines.map((g, i) => <li key={i}>{g}</li>)}
                                </ul>
                            )}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default Grade12AccountingScaffold;
