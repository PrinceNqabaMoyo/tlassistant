import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const extractDivisionOperands = (q) => {
    if (!q) return null;
    const dividend = q?.dividend ?? q?.parameters?.dividend ?? q?.meta?.dividend ?? q?.data?.dividend;
    const divisor = q?.divisor ?? q?.parameters?.divisor ?? q?.meta?.divisor ?? q?.data?.divisor;
    if (dividend !== undefined && divisor !== undefined && dividend !== null && divisor !== null) {
        const a = String(dividend).trim();
        const b = String(divisor).trim();
        if (a !== '' && b !== '') return { dividend: a, divisor: b };
    }

    const s = String(q?.question ?? '').trim();
    const bySymbol = s.match(/(\d[\d,\s]*)\s*(?:÷|\/|\\)\s*(\d[\d,\s]*)/);
    if (bySymbol) {
        return {
            dividend: String(bySymbol[1]).replace(/\s+/g, '').replace(/,/g, ''),
            divisor: String(bySymbol[2]).replace(/\s+/g, '').replace(/,/g, ''),
        };
    }
    const byWords = s.match(/(\d[\d,\s]*)\s*(?:divided by|divide by)\s*(\d[\d,\s]*)/i);
    if (byWords) {
        return {
            dividend: String(byWords[1]).replace(/\s+/g, '').replace(/,/g, ''),
            divisor: String(byWords[2]).replace(/\s+/g, '').replace(/,/g, ''),
        };
    }
    return null;
};

const LongDivisionBracket = ({ divisor, dividend }) => {
    return (
        <div className="inline-flex items-stretch font-mono text-lg">
            <div className="pr-2 text-gray-900 flex items-center justify-end">{divisor}</div>
            <div className="pl-2 pr-2 pt-1 border-l-2 border-t-2 border-gray-900 text-gray-900">{dividend}</div>
        </div>
    );
};

const Grade8WholeNumbersScaffold = ({
    onBack,
    scaffoldSteps,
    g8WholeVisualAidsOpen,
    setG8WholeVisualAidsOpen,
    g8WholeScaffoldDifficulty,
    setG8WholeScaffoldDifficulty,
    g8WholeScaffoldStepIndex,
    setG8WholeScaffoldStepIndex,
    fetchGrade8WholeNumbersScaffoldQuestion,
    g8WholeScaffoldLoading,
    g8WholeScaffoldError,
    g8WholeScaffoldQuestion,
    g8WholeScaffoldShowHint,
    setG8WholeScaffoldShowHint,
    g8WholeScaffoldAnswer,
    setG8WholeScaffoldAnswer,
    g8WholeScaffoldFeedback,
    setG8WholeScaffoldFeedback,
    g8WholeScaffoldCheckpointIndex,
    setG8WholeScaffoldCheckpointIndex,
    g8WholeScaffoldCheckpointAnswers,
    setG8WholeScaffoldCheckpointAnswers,
    g8WholeScaffoldCheckpointFeedback,
    setG8WholeScaffoldCheckpointFeedback,
    normalizeWholeNumberAnswer,
    renderGrade8WholeNumbersVisualAids,
}) => {
    const divisionOperands =
        String(g8WholeScaffoldQuestion?.subskill || '') === 'long_division'
            ? extractDivisionOperands(g8WholeScaffoldQuestion)
            : null;
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 8 Mathematics • Whole Numbers • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step method practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g8WholeVisualAidsOpen && (
                                <button
                                    onClick={() => setG8WholeVisualAidsOpen(true)}
                                    className="px-4 py-2 bg-indigo-50 hover:bg-indigo-100 text-indigo-800 rounded-lg font-semibold border border-indigo-200"
                                >
                                    Visual Aids
                                </button>
                            )}
                            <button
                                onClick={onBack}
                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-medium"
                            >
                                Back
                            </button>
                        </div>
                    </div>

                    <div className="flex flex-col md:flex-row gap-3 md:items-end md:justify-between mb-6">
                        <div className="w-full md:w-64">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Difficulty</label>
                            <select
                                value={g8WholeScaffoldDifficulty}
                                onChange={(e) => setG8WholeScaffoldDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="w-full md:w-72">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Subskill</label>
                            <select
                                value={g8WholeScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG8WholeScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG8WholeScaffoldFeedback(null);
                                    setG8WholeScaffoldShowHint(false);
                                    setG8WholeScaffoldCheckpointIndex(0);
                                    setG8WholeScaffoldCheckpointAnswers({});
                                    setG8WholeScaffoldCheckpointFeedback({});
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {scaffoldSteps.map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => {
                                    const step = scaffoldSteps[g8WholeScaffoldStepIndex] || scaffoldSteps[0];
                                    fetchGrade8WholeNumbersScaffoldQuestion({ subskill: step.key, difficulty: g8WholeScaffoldDifficulty });
                                }}
                                disabled={g8WholeScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g8WholeScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <div>
                                <div className="text-sm font-semibold text-gray-800">
                                    Step {g8WholeScaffoldStepIndex + 1} / {scaffoldSteps.length}: {scaffoldSteps[g8WholeScaffoldStepIndex]?.title}
                                </div>
                                <div className="text-sm text-gray-600">{scaffoldSteps[g8WholeScaffoldStepIndex]?.prompt}</div>
                            </div>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                            <div
                                className="bg-indigo-600 h-2 rounded-full"
                                style={{ width: `${Math.round(((g8WholeScaffoldStepIndex + 1) / scaffoldSteps.length) * 100)}%` }}
                            />
                        </div>
                    </div>

                    {g8WholeScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g8WholeScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g8WholeScaffoldLoading && !g8WholeScaffoldQuestion ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : g8WholeScaffoldQuestion ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                {divisionOperands ? (
                                    <div className="text-gray-800 font-medium mb-4">
                                        <LongDivisionBracket
                                            divisor={divisionOperands.divisor}
                                            dividend={divisionOperands.dividend}
                                        />
                                    </div>
                                ) : (
                                    <div className="text-gray-800 font-medium mb-4">{g8WholeScaffoldQuestion.question}</div>
                                )}

                                {g8WholeScaffoldQuestion.question_type === 'scaffold' && Array.isArray(g8WholeScaffoldQuestion.checkpoints) ? (
                                    (() => {
                                        const cps = g8WholeScaffoldQuestion.checkpoints;
                                        const cp = cps[g8WholeScaffoldCheckpointIndex];
                                        const cpId = cp?.id || `cp_${g8WholeScaffoldCheckpointIndex}`;
                                        const answerValue = g8WholeScaffoldCheckpointAnswers[cpId] ?? '';
                                        const feedback = g8WholeScaffoldCheckpointFeedback[cpId];
                                        const isDone = g8WholeScaffoldCheckpointIndex >= cps.length;
                                        const isAllCorrect = cps.every((c, idx) => {
                                            const id = c?.id || `cp_${idx}`;
                                            return g8WholeScaffoldCheckpointFeedback[id]?.isCorrect;
                                        });

                                        return (
                                            <div>
                                                {Array.isArray(g8WholeScaffoldQuestion.steps) && (
                                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                            {g8WholeScaffoldQuestion.steps.map((s, idx) => (
                                                                <li
                                                                    key={`${idx}_${s}`}
                                                                    className={idx === Math.min(g8WholeScaffoldCheckpointIndex, g8WholeScaffoldQuestion.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}
                                                                >
                                                                    {s}
                                                                </li>
                                                            ))}
                                                        </ol>
                                                    </div>
                                                )}

                                                {!isDone && cp && (
                                                    <div className="bg-white border border-gray-200 rounded-lg p-4">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">
                                                            Checkpoint {g8WholeScaffoldCheckpointIndex + 1} / {cps.length}
                                                        </div>
                                                        <div className="text-gray-800 font-medium mb-3">{cp.prompt}</div>

                                                        {cp.kind === 'mcq' && Array.isArray(cp.options) ? (
                                                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                                                {cp.options.map((opt) => (
                                                                    <label key={opt} className="flex items-center gap-2 p-3 bg-gray-50 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100">
                                                                        <input
                                                                            type="radio"
                                                                            name={cpId}
                                                                            value={opt}
                                                                            checked={answerValue === opt}
                                                                            onChange={(e) => setG8WholeScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                        />
                                                                        <span className="text-gray-800">{opt}</span>
                                                                    </label>
                                                                ))}
                                                            </div>
                                                        ) : (
                                                            <input
                                                                type="text"
                                                                value={answerValue}
                                                                onChange={(e) => setG8WholeScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                                placeholder="Type your answer"
                                                            />
                                                        )}

                                                        <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                            <button
                                                                onClick={() => {
                                                                    const user = answerValue;
                                                                    const correct = cp.correct_answer;
                                                                    const ok = normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct);

                                                                    setG8WholeScaffoldCheckpointFeedback((prev) => ({
                                                                        ...prev,
                                                                        [cpId]: {
                                                                            isCorrect: ok,
                                                                            correctAnswer: cp.correct_answer,
                                                                            explanation: cp.explanation
                                                                        }
                                                                    }));
                                                                }}
                                                                disabled={String(answerValue).trim() === ''}
                                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                                            >
                                                                Check
                                                            </button>
                                                            <button
                                                                onClick={() => setG8WholeScaffoldShowHint((p) => !p)}
                                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                                            >
                                                                {g8WholeScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                                            </button>
                                                            <button
                                                                onClick={() => {
                                                                    const ok = !!g8WholeScaffoldCheckpointFeedback[cpId]?.isCorrect;
                                                                    if (!ok) return;
                                                                    setG8WholeScaffoldCheckpointIndex((prev) => prev + 1);
                                                                    setG8WholeScaffoldShowHint(false);
                                                                }}
                                                                disabled={!g8WholeScaffoldCheckpointFeedback[cpId]?.isCorrect}
                                                                className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                                            >
                                                                Next Checkpoint
                                                            </button>
                                                        </div>

                                                        {feedback && (
                                                            <div className={`mt-4 p-3 rounded-lg text-sm border ${feedback.isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
                                                                <div className="font-semibold">{feedback.isCorrect ? 'Correct' : 'Not quite'}</div>
                                                                <div className="mt-1"><span className="font-semibold">Correct answer:</span> {feedback.correctAnswer}</div>
                                                            </div>
                                                        )}

                                                        {g8WholeScaffoldShowHint && (feedback?.explanation || cp?.explanation) && (
                                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                                {feedback?.explanation || cp?.explanation}
                                                            </div>
                                                        )}
                                                    </div>
                                                )}

                                                <div className="mt-4">
                                                    <button
                                                        onClick={() => {
                                                            setG8WholeScaffoldStepIndex((prev) => {
                                                                const next = prev + 1;
                                                                return next >= scaffoldSteps.length ? 0 : next;
                                                            });
                                                        }}
                                                        disabled={!isAllCorrect}
                                                        className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                                    >
                                                        Next Step
                                                    </button>
                                                </div>
                                            </div>
                                        );
                                    })()
                                ) : (
                                    <>
                                        <input
                                            type="text"
                                            value={g8WholeScaffoldAnswer}
                                            onChange={(e) => setG8WholeScaffoldAnswer(e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Type your answer"
                                        />

                                        <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={() => {
                                                    const user = g8WholeScaffoldAnswer;
                                                    const correct = g8WholeScaffoldQuestion.correct_answer;
                                                    const ok = normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct);
                                                    setG8WholeScaffoldFeedback({
                                                        isCorrect: ok,
                                                        correctAnswer: g8WholeScaffoldQuestion.correct_answer,
                                                        explanation: g8WholeScaffoldQuestion.explanation
                                                    });
                                                }}
                                                disabled={String(g8WholeScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG8WholeScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                            >
                                                {g8WholeScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                            <button
                                                onClick={() => {
                                                    setG8WholeScaffoldStepIndex((prev) => {
                                                        const next = prev + 1;
                                                        return next >= scaffoldSteps.length ? 0 : next;
                                                    });
                                                }}
                                                disabled={!g8WholeScaffoldFeedback?.isCorrect}
                                                className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                            >
                                                Next Step
                                            </button>
                                        </div>

                                        {g8WholeScaffoldFeedback && (
                                            <div className={`mt-4 p-3 rounded-lg text-sm border ${g8WholeScaffoldFeedback.isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
                                                <div className="font-semibold">{g8WholeScaffoldFeedback.isCorrect ? 'Correct' : 'Not quite'}</div>
                                                <div className="mt-1"><span className="font-semibold">Correct answer:</span> {g8WholeScaffoldFeedback.correctAnswer}</div>
                                            </div>
                                        )}

                                        {g8WholeScaffoldShowHint && g8WholeScaffoldQuestion.explanation && (
                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                {g8WholeScaffoldQuestion.explanation}
                                            </div>
                                        )}
                                    </>
                                )}
                            </>
                        ) : (
                            <div className="text-gray-600">No question loaded.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g8WholeVisualAidsOpen} setIsOpen={setG8WholeVisualAidsOpen}>
                    {renderGrade8WholeNumbersVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade8WholeNumbersScaffold;
