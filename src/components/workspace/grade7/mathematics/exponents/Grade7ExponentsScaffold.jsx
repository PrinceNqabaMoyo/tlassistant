import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const Grade7ExponentsScaffold = ({
    onBack,
    exponentsSteps,
    g7ExpVisualAidsOpen,
    setG7ExpVisualAidsOpen,
    g7ExpScaffoldDifficulty,
    setG7ExpScaffoldDifficulty,
    g7ExpScaffoldStepIndex,
    setG7ExpScaffoldStepIndex,
    setG7ExpScaffoldShowHint,
    setG7ExpScaffoldCheckpointIndex,
    setG7ExpScaffoldCheckpointAnswers,
    setG7ExpScaffoldCheckpointFeedback,
    fetchGrade7ExponentsScaffoldQuestion,
    g7ExpScaffoldLoading,
    g7ExpScaffoldError,
    g7ExpScaffoldQuestion,
    formatExponentCarets,
    g7ExpScaffoldCheckpointIndex,
    g7ExpScaffoldCheckpointAnswers,
    g7ExpScaffoldCheckpointFeedback,
    g7ExpScaffoldShowHint,
    g7ExpScaffoldAnswer,
    setG7ExpScaffoldAnswer,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    g7ExpScaffoldFeedback,
    setG7ExpScaffoldFeedback,
    renderExponentsVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 7 Mathematics • Exponents • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step learning. No calculator.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g7ExpVisualAidsOpen && (
                                <button
                                    onClick={() => setG7ExpVisualAidsOpen(true)}
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
                                value={g7ExpScaffoldDifficulty}
                                onChange={(e) => setG7ExpScaffoldDifficulty(e.target.value)}
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
                                value={g7ExpScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG7ExpScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG7ExpScaffoldFeedback(null);
                                    setG7ExpScaffoldShowHint(false);
                                    setG7ExpScaffoldCheckpointIndex(0);
                                    setG7ExpScaffoldCheckpointAnswers({});
                                    setG7ExpScaffoldCheckpointFeedback({});
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {exponentsSteps.map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => {
                                    const step = exponentsSteps[g7ExpScaffoldStepIndex] || exponentsSteps[0];
                                    fetchGrade7ExponentsScaffoldQuestion({ subskill: step.key, difficulty: g7ExpScaffoldDifficulty });
                                }}
                                disabled={g7ExpScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g7ExpScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="mb-4">
                        <div className="text-sm font-semibold text-gray-800">
                            Step {g7ExpScaffoldStepIndex + 1} / {exponentsSteps.length}: {exponentsSteps[g7ExpScaffoldStepIndex]?.title}
                        </div>
                        <div className="text-sm text-gray-600">{exponentsSteps[g7ExpScaffoldStepIndex]?.prompt}</div>
                        <div className="w-full bg-gray-200 rounded-full h-2 mt-2">
                            <div
                                className="bg-indigo-600 h-2 rounded-full"
                                style={{ width: `${Math.round(((g7ExpScaffoldStepIndex + 1) / exponentsSteps.length) * 100)}%` }}
                            />
                        </div>
                    </div>

                    {g7ExpScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g7ExpScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g7ExpScaffoldLoading && !g7ExpScaffoldQuestion ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : g7ExpScaffoldQuestion ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{formatExponentCarets(g7ExpScaffoldQuestion.question || g7ExpScaffoldQuestion.prompt)}</div>

                                {g7ExpScaffoldQuestion.question_type === 'scaffold' && Array.isArray(g7ExpScaffoldQuestion.checkpoints) ? (
                                    (() => {
                                        const cps = g7ExpScaffoldQuestion.checkpoints;
                                        const cp = cps[g7ExpScaffoldCheckpointIndex];
                                        const cpId = cp?.id || `cp_${g7ExpScaffoldCheckpointIndex}`;
                                        const answerValue = g7ExpScaffoldCheckpointAnswers[cpId] ?? '';
                                        const feedback = g7ExpScaffoldCheckpointFeedback[cpId];
                                        const isAllCorrect = cps.every((c, idx) => {
                                            const id = c?.id || `cp_${idx}`;
                                            return g7ExpScaffoldCheckpointFeedback[id]?.isCorrect;
                                        });

                                        return (
                                            <div>
                                                {Array.isArray(g7ExpScaffoldQuestion.steps) && (
                                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                            {g7ExpScaffoldQuestion.steps.map((s, idx) => {
                                                                const title = typeof s === 'string' ? s : s?.title;
                                                                const content = typeof s === 'string' ? '' : s?.content;
                                                                return (
                                                                    <li key={`${idx}_${title || 'step'}`}>
                                                                        <div className="font-semibold text-gray-800">{formatExponentCarets(title)}</div>
                                                                        {content ? <div className="text-gray-700">{formatExponentCarets(content)}</div> : null}
                                                                    </li>
                                                                );
                                                            })}
                                                        </ol>
                                                    </div>
                                                )}

                                                {cp && (
                                                    <div className="bg-white border border-gray-200 rounded-lg p-4">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">
                                                            Checkpoint {g7ExpScaffoldCheckpointIndex + 1} / {cps.length}
                                                        </div>
                                                        <div className="text-gray-800 font-medium mb-3">{formatExponentCarets(cp.prompt)}</div>

                                                        {cp.kind === 'mcq' && Array.isArray(cp.options) ? (
                                                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                                                {cp.options.map((opt) => (
                                                                    <label key={opt} className="flex items-center gap-2 p-3 bg-gray-50 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100">
                                                                        <input
                                                                            type="radio"
                                                                            name={cpId}
                                                                            value={opt}
                                                                            checked={answerValue === opt}
                                                                            onChange={(e) => setG7ExpScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                        />
                                                                        <span className="text-gray-800">{formatExponentCarets(opt)}</span>
                                                                    </label>
                                                                ))}
                                                            </div>
                                                        ) : (
                                                            <input
                                                                type="text"
                                                                value={answerValue}
                                                                onChange={(e) => setG7ExpScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                                placeholder="Type your answer"
                                                            />
                                                        )}

                                                        <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                            <button
                                                                onClick={() => {
                                                                    const user = String(answerValue);
                                                                    const correct = String(cp.correct_answer ?? cp.answer ?? '');
                                                                    const ok = normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                                        || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase();

                                                                    setG7ExpScaffoldCheckpointFeedback((prev) => ({
                                                                        ...prev,
                                                                        [cpId]: {
                                                                            isCorrect: ok,
                                                                            correctAnswer: cp.correct_answer ?? cp.answer,
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
                                                                onClick={() => setG7ExpScaffoldShowHint((p) => !p)}
                                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                                            >
                                                                {g7ExpScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                                            </button>
                                                            <button
                                                                onClick={() => {
                                                                    const ok = !!g7ExpScaffoldCheckpointFeedback[cpId]?.isCorrect;
                                                                    if (!ok) return;
                                                                    setG7ExpScaffoldCheckpointIndex((prev) => prev + 1);
                                                                    setG7ExpScaffoldShowHint(false);
                                                                }}
                                                                disabled={!g7ExpScaffoldCheckpointFeedback[cpId]?.isCorrect}
                                                                className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                                            >
                                                                Next Checkpoint
                                                            </button>
                                                        </div>

                                                        {feedback && (
                                                            <div className={`mt-4 p-3 rounded-lg text-sm border ${feedback.isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
                                                                <div className="font-semibold">{feedback.isCorrect ? 'Correct' : 'Not quite'}</div>
                                                                <div className="mt-1"><span className="font-semibold">Correct answer:</span> {formatExponentCarets(feedback.correctAnswer)}</div>
                                                            </div>
                                                        )}

                                                        {g7ExpScaffoldShowHint && (feedback?.explanation || cp?.explanation) && (
                                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                                {feedback?.explanation || cp?.explanation}
                                                            </div>
                                                        )}
                                                    </div>
                                                )}

                                                <div className="mt-4">
                                                    <button
                                                        onClick={() => {
                                                            setG7ExpScaffoldStepIndex((prev) => {
                                                                const next = prev + 1;
                                                                return next >= exponentsSteps.length ? 0 : next;
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
                                            value={g7ExpScaffoldAnswer}
                                            onChange={(e) => setG7ExpScaffoldAnswer(e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Type your answer"
                                        />

                                        <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={() => {
                                                    const user = String(g7ExpScaffoldAnswer);
                                                    const correct = String(g7ExpScaffoldQuestion.correct_answer ?? g7ExpScaffoldQuestion.answer ?? '');
                                                    const ok = normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                        || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase();
                                                    setG7ExpScaffoldFeedback({
                                                        isCorrect: ok,
                                                        correctAnswer: g7ExpScaffoldQuestion.correct_answer ?? g7ExpScaffoldQuestion.answer,
                                                        explanation: g7ExpScaffoldQuestion.explanation
                                                    });
                                                }}
                                                disabled={String(g7ExpScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG7ExpScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                            >
                                                {g7ExpScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                            <button
                                                onClick={() => {
                                                    setG7ExpScaffoldStepIndex((prev) => {
                                                        const next = prev + 1;
                                                        return next >= exponentsSteps.length ? 0 : next;
                                                    });
                                                }}
                                                disabled={!g7ExpScaffoldFeedback?.isCorrect}
                                                className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                            >
                                                Next Step
                                            </button>
                                        </div>

                                        {g7ExpScaffoldFeedback && (
                                            <div className={`mt-4 p-3 rounded-lg text-sm border ${g7ExpScaffoldFeedback.isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
                                                <div className="font-semibold">{g7ExpScaffoldFeedback.isCorrect ? 'Correct' : 'Not quite'}</div>
                                                <div className="mt-1"><span className="font-semibold">Correct answer:</span> {formatExponentCarets(g7ExpScaffoldFeedback.correctAnswer)}</div>
                                            </div>
                                        )}

                                        {g7ExpScaffoldShowHint && g7ExpScaffoldQuestion.explanation && (
                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                {g7ExpScaffoldQuestion.explanation}
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

                <VisualAidsPanel isOpen={g7ExpVisualAidsOpen} setIsOpen={setG7ExpVisualAidsOpen}>
                    {renderExponentsVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade7ExponentsScaffold;
