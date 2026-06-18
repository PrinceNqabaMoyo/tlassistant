import React, { useState, useEffect } from 'react';
import MCQOption from '../../../shared/MCQOption';
import VisualAidsPanel from '../../../VisualAidsPanel';
import { TableInput } from '../../../../forms/TableComponents';
import { useGrade10AccountingMarking } from '../useGrade10AccountingMarking';

const normalizeText = (value) => {
    if (value === null || value === undefined) return '';
    return String(value).trim().replace(/\s+/g, ' ').toLowerCase();
};

const getWordBank = (question) => Array.isArray(question?.word_bank) ? question.word_bank : [];

const getCorrectMap = (question) => (question?.correct_map && typeof question.correct_map === 'object') ? question.correct_map : {};

const buildEmptyWordbankAnswer = (question) => {
    const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
    const selections = {};
    for (let i = 0; i < rows.length; i += 1) {
        selections[String(i)] = { '2': null };
    }
    return { selections, activeTokenId: null };
};

const getUsedTokenIds = (ans) => {
    const selections = ans?.selections && typeof ans.selections === 'object' ? ans.selections : {};
    const used = new Set();
    Object.values(selections).forEach((row) => {
        if (!row) return;
        const v = row['2'];
        if (v) used.add(String(v));
    });
    return used;
};

const Grade10AccountingEthicsPractice = ({
    onBack,
    g10AcctEthicsVisualAidsOpen,
    setG10AcctEthicsVisualAidsOpen,
    g10AcctEthicsPracticeDifficulty,
    setG10AcctEthicsPracticeDifficulty,
    fetchGrade10AcctEthicsPractice,
    g10AcctEthicsPracticeLoading,
    g10AcctEthicsPracticeError,
    g10AcctEthicsPracticeQuestions,
    g10AcctEthicsPracticeAnswers,
    setG10AcctEthicsPracticeAnswers,
    g10AcctEthicsPracticeFeedback,
    setG10AcctEthicsPracticeFeedback,
    renderGrade10AcctEthicsVisualAids,
    hideConfig,
}) => {
    const questions = Array.isArray(g10AcctEthicsPracticeQuestions) ? g10AcctEthicsPracticeQuestions : [];
    const [currentIndex, setCurrentIndex] = useState(0);
    const [reviewMode, setReviewMode] = useState(false);
    const [liveElapsedSeconds, setLiveElapsedSeconds] = useState(0);
    const [elapsedSecondsByIndex, setElapsedSecondsByIndex] = useState([]);
    const attemptStartTimeRef = React.useRef(Date.now());
    const timerIntervalRef = React.useRef(null);

    const marking = useGrade10AccountingMarking();

    // Reset marking state when new questions are fetched
    useEffect(() => {
        if (questions.length > 0) {
            marking.setMarkingMode('practice');
        }
    }, [questions, marking]);

    const handleNext = () => {
        if (currentIndex < questions.length - 1) {
            setCurrentIndex((prev) => prev + 1);
        }
    };

    const handlePrev = () => {
        if (currentIndex > 0) {
            setCurrentIndex((prev) => prev - 1);
        }
    };

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g10AcctEthicsPracticeAnswers) ? [...g10AcctEthicsPracticeAnswers] : [];
        answers[idx] = value;
        setG10AcctEthicsPracticeAnswers(answers);

        // Register with marking hook if in marking mode
        if (questions[idx]) {
            marking.registerAnswer(questions[idx].id, value);
        }

        const feedback = Array.isArray(g10AcctEthicsPracticeFeedback) ? [...g10AcctEthicsPracticeFeedback] : [];
        feedback[idx] = null;
        setG10AcctEthicsPracticeFeedback(feedback);
    };

    useEffect(() => {
        if (!questions.length) return;
        if (!Array.isArray(g10AcctEthicsPracticeAnswers) || g10AcctEthicsPracticeAnswers.length !== questions.length) {
            setG10AcctEthicsPracticeAnswers(questions.map((q) => {
                if (q.question_type === 'table_wordbank') return buildEmptyWordbankAnswer(q);
                return '';
            }));
        }
        if (!Array.isArray(g10AcctEthicsPracticeFeedback) || g10AcctEthicsPracticeFeedback.length !== questions.length) {
            setG10AcctEthicsPracticeFeedback(questions.map(() => null));
        }
        setElapsedSecondsByIndex(questions.map(() => 0));
        setReviewMode(false);
        setLiveElapsedSeconds(0);
        attemptStartTimeRef.current = Date.now();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [questions.length]);

    useEffect(() => {
        if (questions.length === 0 || reviewMode || !marking.isPracticeMode) {
            if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
            return;
        }

        timerIntervalRef.current = setInterval(() => {
            setLiveElapsedSeconds(Math.floor((Date.now() - attemptStartTimeRef.current) / 1000));
        }, 1000);

        return () => {
            if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
        };
    }, [questions.length, reviewMode, marking.isPracticeMode]);

    useEffect(() => {
        if (reviewMode || !marking.isPracticeMode || questions.length === 0) return;
        setElapsedSecondsByIndex((prev) => {
            const next = [...prev];
            next[currentIndex] = (next[currentIndex] || 0) + 1;
            return next;
        });
    }, [liveElapsedSeconds]);

    const setFeedbackAt = (idx, value) => {
        const next = Array.isArray(g10AcctEthicsPracticeFeedback) ? g10AcctEthicsPracticeFeedback.slice() : [];
        next[idx] = value;
        setG10AcctEthicsPracticeFeedback(next);
    };

    const evaluateQuestion = (q, idx) => {
        if (!q) return null;
        const ans = Array.isArray(g10AcctEthicsPracticeAnswers) ? g10AcctEthicsPracticeAnswers[idx] : null;

        if (q.question_type === 'mcq') {
            const ok = String(ans) === String(q.correct_index);
            return ok
                ? { kind: 'success', message: 'Correct.', isCorrect: true, score: 1, max: 1 }
                : { kind: 'error', message: `Not quite. Correct answer: ${q.options?.[q.correct_index] || ''}`, isCorrect: false, score: 0, max: 1 };
        }

        if (q.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(q);
            const a = (ans && typeof ans === 'object') ? ans : buildEmptyWordbankAnswer(q);
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

            const ok = total > 0 && hit === total;
            return ok
                ? { kind: 'success', message: 'Correct.', isCorrect: true, score: total, max: total }
                : { kind: 'error', message: `Not quite. You matched ${hit}/${total} correctly.`, isCorrect: false, score: hit, max: total };
        }

        if (q.question_type === 'typed') {
            const user = normalizeText(ans);
            if (!user) {
                return { kind: 'error', message: 'Write an answer first.', isCorrect: false, score: 0, max: 1 };
            }
            return { kind: 'info', message: 'Compare your answer to the sample answer / visual aids.', isCorrect: null, score: 1, max: 1 };
        }

        return { kind: 'info', message: 'Saved.' };
    };

    const handleFinishAndReview = () => {
        if (!questions.length) return;
        const feedbacks = [];
        for (let i = 0; i < questions.length; i += 1) {
            feedbacks.push(evaluateQuestion(questions[i], i));
        }
        setG10AcctEthicsPracticeFeedback(feedbacks);
        setReviewMode(true);
        setCurrentIndex(0);
        if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
    };

    const checkOne = (q, idx) => {
        if (!q) return;
        const ans = Array.isArray(g10AcctEthicsPracticeAnswers) ? g10AcctEthicsPracticeAnswers[idx] : null;

        if (q.question_type === 'mcq') {
            const ok = String(ans) === String(q.correct_index);
            setFeedbackAt(idx, ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite.Correct answer: ${q.options?.[q.correct_index] || ''} ` });
            return;
        }

        if (q.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(q);
            const a = (ans && typeof ans === 'object') ? ans : buildEmptyWordbankAnswer(q);
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

            const ok = total > 0 && hit === total;
            setFeedbackAt(idx, ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite.You matched ${hit}/${total} correctly.` });
            return;
        }

        if (q.question_type === 'typed') {
            const user = normalizeText(ans);
            if (!user) {
                setFeedbackAt(idx, { kind: 'error', message: 'Write an answer first.' });
                return;
            }
            setFeedbackAt(idx, { kind: 'info', message: 'Compare your answer to the sample answer / visual aids.' });
            return;
        }

        setFeedbackAt(idx, { kind: 'info', message: 'Saved.' });
    };

    const renderWordbankTable = (q, idx) => {
        const ans = (g10AcctEthicsPracticeAnswers?.[idx] && typeof g10AcctEthicsPracticeAnswers[idx] === 'object')
            ? g10AcctEthicsPracticeAnswers[idx]
            : buildEmptyWordbankAnswer(q);

        const wordBank = getWordBank(q);
        const correctMap = getCorrectMap(q);
        // In review mode, use correctMap for display instead of user selections
        const effectiveSelections = reviewMode ? correctMap : (ans?.selections || {});
        const used = reviewMode ? new Set() : getUsedTokenIds(ans);

        const tokenLabelById = {};
        wordBank.forEach((t) => { tokenLabelById[String(t.id)] = t.label; });

        const setActiveTokenId = (tokenId) => {
            if (reviewMode) return;
            setAnswer(idx, {
                ...(ans || {}),
                activeTokenId: tokenId,
            });
        };

        const clearCell = (rowIndex) => {
            if (reviewMode) return;
            const next = {
                ...(ans || {}),
                selections: {
                    ...(ans?.selections || {}),
                    [String(rowIndex)]: {
                        ...((ans?.selections || {})[String(rowIndex)] || {}),
                        '2': null,
                    },
                },
            };
            setAnswer(idx, next);
        };

        const placeActive = (rowIndex) => {
            if (reviewMode) return;
            const tokenId = ans?.activeTokenId;
            if (!tokenId) return;
            if (used.has(String(tokenId))) return;

            const next = {
                ...(ans || {}),
                selections: {
                    ...(ans?.selections || {}),
                    [String(rowIndex)]: {
                        ...((ans?.selections || {})[String(rowIndex)] || {}),
                        '2': String(tokenId),
                    },
                },
                activeTokenId: null,
            };
            setAnswer(idx, next);
        };

        const rows = Array.isArray(q?.table?.rows) ? q.table.rows : [];
        const headers = Array.isArray(q?.table?.headers) ? q.table.headers : [];

        return (
            <div className="mt-3">
                {!reviewMode && (
                    <div className="mb-3">
                        <div className="text-sm font-semibold text-gray-900 mb-2">Word bank</div>
                        <div className="flex flex-wrap gap-2">
                            {wordBank.map((t) => {
                                const isUsed = used.has(String(t.id));
                                const isActive = String(ans?.activeTokenId) === String(t.id);
                                return (
                                    <button
                                        key={t.id}
                                        type="button"
                                        disabled={isUsed || reviewMode}
                                        onClick={() => setActiveTokenId(String(t.id))}
                                        className={`px-3 py-1 rounded-full text-sm font-semibold border ${isUsed ? 'bg-gray-100 text-gray-400 border-gray-200' : isActive ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                                    >
                                        {t.label}
                                    </button>
                                );
                            })}
                        </div>
                    </div>
                )}

                <div className="overflow-x-auto">
                    <table className="min-w-full border border-gray-200 text-sm">
                        <thead className="bg-gray-50">
                            <tr>
                                {headers.map((h, i) => (
                                    <th key={i} className="px-3 py-2 border-b border-gray-200 text-left font-semibold text-gray-900">{h}</th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {rows.map((row, rowIndex) => {
                                const selectedId = effectiveSelections?.[String(rowIndex)]?.['2'];
                                const label = selectedId ? tokenLabelById[String(selectedId)] : '';
                                const expectedId = correctMap?.[String(rowIndex)]?.['2'];
                                const isCorrectCell = reviewMode && selectedId && String(selectedId) === String(expectedId);

                                let cellBg = 'bg-white';
                                let cellBorder = label ? 'border-indigo-200' : 'border-gray-200';
                                let textClass = 'text-gray-900';
                                if (isCorrectCell) { cellBg = 'bg-emerald-50'; cellBorder = 'border-emerald-400'; textClass = 'text-emerald-800 font-semibold'; }

                                return (
                                    <tr key={rowIndex} className={rowIndex % 2 === 0 ? 'bg-white' : 'bg-gray-50'}>
                                        <td className="px-3 py-2 border-b border-gray-200 whitespace-nowrap">{row[0]}</td>
                                        <td className="px-3 py-2 border-b border-gray-200 min-w-[420px]">{row[1]}</td>
                                        <td className="px-3 py-2 border-b border-gray-200">
                                            <button
                                                type="button"
                                                onClick={() => { if (!reviewMode) placeActive(rowIndex); }}
                                                disabled={reviewMode}
                                                className={`w-full text-left px-3 py-2 rounded-md border ${cellBg} ${cellBorder} ${reviewMode ? 'cursor-default' : 'hover:bg-gray-50'}`}
                                            >
                                                {label ? (
                                                    <span className={`font-semibold ${textClass}`}>{label}</span>
                                                ) : (
                                                    <span className="text-gray-400">{reviewMode ? '—' : 'Click to place...'}</span>
                                                )}
                                            </button>
                                            {!reviewMode && (
                                                <div className="mt-1">
                                                    <button
                                                        type="button"
                                                        onClick={() => { if (!reviewMode) clearCell(rowIndex); }}
                                                        disabled={reviewMode}
                                                        className="text-xs font-semibold text-gray-600 hover:text-gray-900 disabled:opacity-50"
                                                    >
                                                        Clear
                                                    </button>
                                                </div>
                                            )}
                                        </td>
                                        <td className="px-3 py-2 border-b border-gray-200">{row[3] || ''}</td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>

                {Array.isArray(q?.guidelines) && q.guidelines.length > 0 && (
                    <div className="mt-3 bg-gray-50 border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-900 mb-1">Guidelines</div>
                        <ul className="list-disc pl-5 space-y-1 text-sm text-gray-800">
                            {q.guidelines.map((g, gIdx) => (
                                <li key={gIdx}>{g}</li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
        );
    };

    const q = questions[currentIndex];
    const ans = g10AcctEthicsPracticeAnswers?.[currentIndex];
    const feedback = g10AcctEthicsPracticeFeedback?.[currentIndex];

    return (
        <>
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-slate-800">Practice Mode</h3>

                
            </div>

            {marking.markingError && (
                <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">
                    {marking.markingError}
                </div>
            )}

            {g10AcctEthicsPracticeLoading && (
                <div className="text-sm text-slate-500">Loading...</div>
            )}
            {g10AcctEthicsPracticeError && (
                <div className="text-sm text-red-700 break-words">{g10AcctEthicsPracticeError}</div>
            )}

            {!g10AcctEthicsPracticeLoading && questions.length === 0 && (
                <div className="text-sm text-slate-500">Click "Generate Question" to start.</div>
            )}

            {q && (
                <div className="space-y-4">
                    {/* Navigation and Submission Header */}
                    <div className="flex items-center justify-between bg-slate-50 p-3 rounded-xl border border-slate-200">
                        <div className="text-sm font-semibold text-slate-700">
                            Question {currentIndex + 1} of {questions.length}
                        </div>
                        <div className="flex items-center gap-2">
                            <button
                                onClick={handlePrev}
                                disabled={currentIndex === 0}
                                className="px-3 py-1.5 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-700 hover:bg-slate-50 disabled:opacity-50"
                            >
                                Previous
                            </button>
                            <button
                                onClick={handleNext}
                                disabled={currentIndex === questions.length - 1}
                                className="px-3 py-1.5 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-700 hover:bg-slate-50 disabled:opacity-50"
                            >
                                Next
                            </button>
                        </div>
                    </div>

                    <div className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm">
                        <div className="text-lg font-medium text-slate-800 whitespace-pre-wrap">{q.prompt}</div>

                        <div className="mt-6">
                            {q.question_type === 'mcq' && (
                                <div className="grid grid-cols-1 gap-2">
                                    {(q.options || []).map((opt, oIdx) => (
                                        <MCQOption
                                            key={oIdx}
                                            selected={String(ans) === String(oIdx)}
                                            onClick={() => { if (!reviewMode) setAnswer(currentIndex, String(oIdx)); }}
                                            label={opt}
                                        />
                                    ))}
                                </div>
                            )}

                            {q.question_type === 'typed' && (
                                <div>
                                    <textarea
                                        value={typeof ans === 'string' ? ans : ''}
                                        onChange={(e) => { if (!reviewMode) setAnswer(currentIndex, e.target.value); }}
                                        disabled={reviewMode}
                                        placeholder="Write your answer..."
                                        className="w-full min-h-[110px] p-3 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-slate-300 disabled:bg-slate-50 disabled:text-slate-600"
                                    />
                                    {(q.question_type === 'typed' || q.question_type === 'table') && marking.isPracticeMode && (
                                        <div className="mt-6 text-sm text-slate-700 bg-slate-50 p-4 rounded-xl border border-slate-200">
                                            {q.sample_answer && (
                                                <div className="mb-2"><span className="font-semibold text-slate-900">Guideline answer: </span>{q.sample_answer}</div>
                                            )}
                                            {Array.isArray(q.guidelines) && q.guidelines.length > 0 && (
                                                <div>
                                                    <div className="font-semibold text-slate-900 mb-1">Guidelines:</div>
                                                    <ul className="list-disc pl-5 space-y-1">
                                                        {q.guidelines.map((g, gi) => <li key={gi}>{g}</li>)}
                                                    </ul>
                                                </div>
                                            )}
                                        </div>
                                    )}
                                </div>
                            )}

                            {q.question_type === 'table_wordbank' && renderWordbankTable(q, currentIndex)}
                        </div>

                        {/* Action Buttons */}
                        <div className="mt-8 flex justify-end gap-3 pt-4 border-t border-slate-100">
                            {marking.isPracticeMode ? (
                                reviewMode ? (
                                    <button
                                        onClick={handleNext}
                                        disabled={currentIndex === questions.length - 1}
                                        className="px-6 py-2 bg-indigo-50 text-indigo-700 rounded-xl font-semibold hover:bg-indigo-100 transition-colors disabled:opacity-50"
                                    >
                                        Next Question
                                    </button>
                                ) : (
                                    currentIndex === questions.length - 1 ? (
                                        <button
                                            onClick={handleFinishAndReview}
                                            className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors"
                                        >
                                            Finish and Review
                                        </button>
                                    ) : (
                                        <button
                                            onClick={handleNext}
                                            className="px-6 py-2 bg-indigo-50 text-indigo-700 rounded-xl font-semibold hover:bg-indigo-100 transition-colors"
                                        >
                                            Next Question
                                        </button>
                                    )
                                )
                            ) : (
                                !marking.isMarkingSubmitted && (
                                    <button
                                        onClick={() => marking.submitAssessment(questions)}
                                        disabled={marking.isSubmitting}
                                        className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors disabled:opacity-50"
                                    >
                                        {marking.isSubmitting ? 'Submitting...' : 'Submit Assessment'}
                                    </button>
                                )
                            )}
                        </div>

                        {/* Review Feedback Block */}
                        {reviewMode && feedback && (
                            <div className={`mt-4 p-4 rounded-xl border ${feedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200' : feedback.kind === 'error' ? 'bg-red-50 border-red-200' : 'bg-slate-50 border-slate-200'}`}>
                                <h4 className={`text-sm font-bold mb-2 flex items-center gap-2 ${feedback.kind === 'success' ? 'text-emerald-900' : feedback.kind === 'error' ? 'text-red-900' : 'text-slate-900'}`}>
                                    {feedback.kind === 'success' ? (
                                        <svg className="w-5 h-5 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                                        </svg>
                                    ) : feedback.kind === 'error' ? (
                                        <svg className="w-5 h-5 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                                        </svg>
                                    ) : null}
                                    {feedback.kind === 'success' ? 'Correct' : feedback.kind === 'error' ? 'Needs Review' : 'Feedback'}
                                </h4>
                                <p className={`text-sm ${feedback.kind === 'success' ? 'text-emerald-800' : feedback.kind === 'error' ? 'text-red-800' : 'text-slate-800'}`}>
                                    {feedback.message}
                                </p>
                            </div>
                        )}
                    </div>
                </div>
            )}
        </>
    );
};

export default Grade10AccountingEthicsPractice;

