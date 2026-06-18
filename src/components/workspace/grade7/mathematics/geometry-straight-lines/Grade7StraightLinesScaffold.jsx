import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const Grade7StraightLinesScaffold = ({
    onBack,
    straightLinesSteps,
    g7StraightVisualAidsOpen,
    setG7StraightVisualAidsOpen,
    g7StraightScaffoldDifficulty,
    setG7StraightScaffoldDifficulty,
    g7StraightScaffoldStepIndex,
    setG7StraightScaffoldStepIndex,
    setG7StraightScaffoldFeedback,
    setG7StraightScaffoldShowHint,
    setG7StraightScaffoldCheckpointIndex,
    setG7StraightScaffoldCheckpointAnswers,
    setG7StraightScaffoldCheckpointFeedback,
    fetchGrade7StraightLinesScaffoldQuestion,
    g7StraightScaffoldLoading,
    g7StraightScaffoldError,
    g7StraightScaffoldQuestion,
    g7StraightScaffoldCheckpointIndex,
    g7StraightScaffoldCheckpointAnswers,
    g7StraightScaffoldCheckpointFeedback,
    g7StraightScaffoldShowHint,
    g7StraightScaffoldAnswer,
    setG7StraightScaffoldAnswer,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    g7StraightScaffoldFeedback,
    renderStraightLinesVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 7 Mathematics • Geometry of straight lines • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step learning. No calculator.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g7StraightVisualAidsOpen && (
                                <button
                                    onClick={() => setG7StraightVisualAidsOpen(true)}
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
                                value={g7StraightScaffoldDifficulty}
                                onChange={(e) => setG7StraightScaffoldDifficulty(e.target.value)}
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
                                value={g7StraightScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG7StraightScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG7StraightScaffoldFeedback(null);
                                    setG7StraightScaffoldShowHint(false);
                                    setG7StraightScaffoldCheckpointIndex(0);
                                    setG7StraightScaffoldCheckpointAnswers({});
                                    setG7StraightScaffoldCheckpointFeedback({});
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {straightLinesSteps.map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>

                        <div className="flex gap-2">
                            <button
                                onClick={() => {
                                    const step = straightLinesSteps[g7StraightScaffoldStepIndex] || straightLinesSteps[0];
                                    fetchGrade7StraightLinesScaffoldQuestion({ subskill: step.key, difficulty: g7StraightScaffoldDifficulty });
                                }}
                                disabled={g7StraightScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g7StraightScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="mb-4">
                        <div className="text-sm font-semibold text-gray-800">
                            Step {g7StraightScaffoldStepIndex + 1} / {straightLinesSteps.length}: {straightLinesSteps[g7StraightScaffoldStepIndex]?.title}
                        </div>
                        <div className="text-sm text-gray-600">{straightLinesSteps[g7StraightScaffoldStepIndex]?.prompt}</div>
                        <div className="w-full bg-gray-200 rounded-full h-2 mt-2">
                            <div
                                className="bg-indigo-600 h-2 rounded-full"
                                style={{ width: `${Math.round(((g7StraightScaffoldStepIndex + 1) / straightLinesSteps.length) * 100)}%` }}
                            />
                        </div>
                    </div>

                    {g7StraightScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g7StraightScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g7StraightScaffoldLoading && !g7StraightScaffoldQuestion ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : g7StraightScaffoldQuestion ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{g7StraightScaffoldQuestion.question || g7StraightScaffoldQuestion.prompt}</div>

                                {g7StraightScaffoldQuestion.question_type === 'scaffold' && Array.isArray(g7StraightScaffoldQuestion.checkpoints) ? (
                                    (() => {
                                        const cps = g7StraightScaffoldQuestion.checkpoints;
                                        const cp = cps[g7StraightScaffoldCheckpointIndex];
                                        const cpId = cp?.id || `cp_${g7StraightScaffoldCheckpointIndex}`;
                                        const answerValue = g7StraightScaffoldCheckpointAnswers[cpId] ?? '';
                                        const feedback = g7StraightScaffoldCheckpointFeedback[cpId];
                                        const isAllCorrect = cps.every((c, idx) => {
                                            const id = c?.id || `cp_${idx}`;
                                            return g7StraightScaffoldCheckpointFeedback[id]?.isCorrect;
                                        });

                                        return (
                                            <div>
                                                {Array.isArray(g7StraightScaffoldQuestion.steps) && (
                                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                            {g7StraightScaffoldQuestion.steps.map((s, idx) => {
                                                                const title = typeof s === 'string' ? s : s?.title;
                                                                const content = typeof s === 'string' ? '' : s?.content;
                                                                return (
                                                                    <li key={`${idx}_${title || 'step'}`}>
                                                                        <div className="font-semibold text-gray-800">{title}</div>
                                                                        {content ? <div className="text-gray-700">{content}</div> : null}
                                                                    </li>
                                                                );
                                                            })}
                                                        </ol>
                                                    </div>
                                                )}

                                                {cp && (
                                                    <div className="bg-white border border-gray-200 rounded-lg p-4">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">
                                                            Checkpoint {g7StraightScaffoldCheckpointIndex + 1} / {cps.length}
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
                                                                            onChange={(e) => setG7StraightScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                        />
                                                                        <span className="text-gray-800">{opt}</span>
                                                                    </label>
                                                                ))}
                                                            </div>
                                                        ) : (
                                                            <input
                                                                type="text"
                                                                value={answerValue}
                                                                onChange={(e) => setG7StraightScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
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

                                                                    setG7StraightScaffoldCheckpointFeedback((prev) => ({
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
                                                                onClick={() => setG7StraightScaffoldShowHint((p) => !p)}
                                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                                            >
                                                                {g7StraightScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                                            </button>
                                                            <button
                                                                onClick={() => {
                                                                    const ok = !!g7StraightScaffoldCheckpointFeedback[cpId]?.isCorrect;
                                                                    if (!ok) return;
                                                                    setG7StraightScaffoldCheckpointIndex((prev) => prev + 1);
                                                                    setG7StraightScaffoldShowHint(false);
                                                                }}
                                                                disabled={!g7StraightScaffoldCheckpointFeedback[cpId]?.isCorrect}
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

                                                        {g7StraightScaffoldShowHint && (feedback?.explanation || cp?.explanation) && (
                                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                                {feedback?.explanation || cp?.explanation}
                                                            </div>
                                                        )}
                                                    </div>
                                                )}

                                                <div className="mt-4">
                                                    <button
                                                        onClick={() => {
                                                            setG7StraightScaffoldStepIndex((prev) => {
                                                                const next = prev + 1;
                                                                return next >= straightLinesSteps.length ? 0 : next;
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
                                            value={g7StraightScaffoldAnswer}
                                            onChange={(e) => setG7StraightScaffoldAnswer(e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Type your answer"
                                        />

                                        <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={() => {
                                                    const user = String(g7StraightScaffoldAnswer);
                                                    const correct = String(g7StraightScaffoldQuestion.correct_answer ?? g7StraightScaffoldQuestion.answer ?? '');
                                                    const ok = normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                        || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase();
                                                    setG7StraightScaffoldFeedback({
                                                        isCorrect: ok,
                                                        correctAnswer: g7StraightScaffoldQuestion.correct_answer ?? g7StraightScaffoldQuestion.answer,
                                                        explanation: g7StraightScaffoldQuestion.explanation
                                                    });
                                                }}
                                                disabled={String(g7StraightScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG7StraightScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                            >
                                                {g7StraightScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                            <button
                                                onClick={() => {
                                                    setG7StraightScaffoldStepIndex((prev) => {
                                                        const next = prev + 1;
                                                        return next >= straightLinesSteps.length ? 0 : next;
                                                    });
                                                }}
                                                disabled={!g7StraightScaffoldFeedback?.isCorrect}
                                                className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                            >
                                                Next Step
                                            </button>
                                        </div>

                                        {g7StraightScaffoldFeedback && (
                                            <div className={`mt-4 p-3 rounded-lg text-sm border ${g7StraightScaffoldFeedback.isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
                                                <div className="font-semibold">{g7StraightScaffoldFeedback.isCorrect ? 'Correct' : 'Not quite'}</div>
                                                <div className="mt-1"><span className="font-semibold">Correct answer:</span> {g7StraightScaffoldFeedback.correctAnswer}</div>
                                            </div>
                                        )}

                                        {g7StraightScaffoldShowHint && g7StraightScaffoldQuestion.explanation && (
                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                {g7StraightScaffoldQuestion.explanation}
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

                <VisualAidsPanel isOpen={g7StraightVisualAidsOpen} setIsOpen={setG7StraightVisualAidsOpen}>
                    {renderStraightLinesVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade7StraightLinesScaffold;
