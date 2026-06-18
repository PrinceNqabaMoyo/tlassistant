import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const Grade7WholeNumbersScaffold = ({
    onBack,
    scaffoldSteps,
    g7WholeVisualAidsOpen,
    setG7WholeVisualAidsOpen,
    g7WholeScaffoldDifficulty,
    setG7WholeScaffoldDifficulty,
    g7WholeScaffoldStepIndex,
    setG7WholeScaffoldStepIndex,
    setG7WholeScaffoldFeedback,
    setG7WholeScaffoldShowHint,
    setG7WholeScaffoldCheckpointIndex,
    setG7WholeScaffoldCheckpointAnswers,
    setG7WholeScaffoldCheckpointFeedback,
    fetchGrade7WholeNumbersScaffoldQuestion,
    g7WholeScaffoldLoading,
    g7WholeScaffoldError,
    g7WholeScaffoldQuestion,
    g7WholeScaffoldCheckpointIndex,
    g7WholeScaffoldCheckpointAnswers,
    g7WholeScaffoldCheckpointFeedback,
    g7WholeScaffoldShowHint,
    g7WholeScaffoldAnswer,
    setG7WholeScaffoldAnswer,
    normalizeWholeNumberAnswer,
    g7WholeScaffoldFeedback,
    renderWholeNumbersVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 7 Mathematics • Whole Numbers • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step learning. No calculator.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g7WholeVisualAidsOpen && (
                                <button
                                    onClick={() => setG7WholeVisualAidsOpen(true)}
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
                                value={g7WholeScaffoldDifficulty}
                                onChange={(e) => setG7WholeScaffoldDifficulty(e.target.value)}
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
                                value={g7WholeScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG7WholeScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG7WholeScaffoldFeedback(null);
                                    setG7WholeScaffoldShowHint(false);
                                    setG7WholeScaffoldCheckpointIndex(0);
                                    setG7WholeScaffoldCheckpointAnswers({});
                                    setG7WholeScaffoldCheckpointFeedback({});
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
                                    const step = scaffoldSteps[g7WholeScaffoldStepIndex] || scaffoldSteps[0];
                                    fetchGrade7WholeNumbersScaffoldQuestion({ subskill: step.key, difficulty: g7WholeScaffoldDifficulty });
                                }}
                                disabled={g7WholeScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g7WholeScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <div>
                                <div className="text-sm font-semibold text-gray-800">
                                    Step {g7WholeScaffoldStepIndex + 1} / {scaffoldSteps.length}: {scaffoldSteps[g7WholeScaffoldStepIndex]?.title}
                                </div>
                                <div className="text-sm text-gray-600">{scaffoldSteps[g7WholeScaffoldStepIndex]?.prompt}</div>
                            </div>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                            <div
                                className="bg-indigo-600 h-2 rounded-full"
                                style={{ width: `${Math.round(((g7WholeScaffoldStepIndex + 1) / scaffoldSteps.length) * 100)}%` }}
                            />
                        </div>
                    </div>

                    {g7WholeScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g7WholeScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g7WholeScaffoldLoading && !g7WholeScaffoldQuestion ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : g7WholeScaffoldQuestion ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{g7WholeScaffoldQuestion.question}</div>

                                {g7WholeScaffoldQuestion.question_type === 'scaffold' && Array.isArray(g7WholeScaffoldQuestion.checkpoints) ? (
                                    (() => {
                                        const cps = g7WholeScaffoldQuestion.checkpoints;
                                        const cp = cps[g7WholeScaffoldCheckpointIndex];
                                        const cpId = cp?.id || `cp_${g7WholeScaffoldCheckpointIndex}`;
                                        const answerValue = g7WholeScaffoldCheckpointAnswers[cpId] ?? '';
                                        const feedback = g7WholeScaffoldCheckpointFeedback[cpId];
                                        const isDone = g7WholeScaffoldCheckpointIndex >= cps.length;
                                        const isAllCorrect = cps.every((c, idx) => {
                                            const id = c?.id || `cp_${idx}`;
                                            return g7WholeScaffoldCheckpointFeedback[id]?.isCorrect;
                                        });

                                        return (
                                            <div>
                                                {Array.isArray(g7WholeScaffoldQuestion.steps) && (
                                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                            {g7WholeScaffoldQuestion.steps.map((s, idx) => (
                                                                <li
                                                                    key={`${idx}_${s}`}
                                                                    className={idx === Math.min(g7WholeScaffoldCheckpointIndex, g7WholeScaffoldQuestion.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}
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
                                                            Checkpoint {g7WholeScaffoldCheckpointIndex + 1} / {cps.length}
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
                                                                            onChange={(e) => setG7WholeScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                        />
                                                                        <span className="text-gray-800">{opt}</span>
                                                                    </label>
                                                                ))}
                                                            </div>
                                                        ) : (
                                                            <input
                                                                type="text"
                                                                value={answerValue}
                                                                onChange={(e) => setG7WholeScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
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

                                                                    setG7WholeScaffoldCheckpointFeedback((prev) => ({
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
                                                                onClick={() => setG7WholeScaffoldShowHint((p) => !p)}
                                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                                            >
                                                                {g7WholeScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                                            </button>
                                                            <button
                                                                onClick={() => {
                                                                    const ok = !!g7WholeScaffoldCheckpointFeedback[cpId]?.isCorrect;
                                                                    if (!ok) return;
                                                                    setG7WholeScaffoldCheckpointIndex((prev) => prev + 1);
                                                                    setG7WholeScaffoldShowHint(false);
                                                                }}
                                                                disabled={!g7WholeScaffoldCheckpointFeedback[cpId]?.isCorrect}
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

                                                        {g7WholeScaffoldShowHint && (feedback?.explanation || cp?.explanation) && (
                                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                                {feedback?.explanation || cp?.explanation}
                                                            </div>
                                                        )}
                                                    </div>
                                                )}

                                                <div className="mt-4">
                                                    <button
                                                        onClick={() => {
                                                            setG7WholeScaffoldStepIndex((prev) => {
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
                                            value={g7WholeScaffoldAnswer}
                                            onChange={(e) => setG7WholeScaffoldAnswer(e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Type your answer"
                                        />

                                        <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={() => {
                                                    const user = g7WholeScaffoldAnswer;
                                                    const correct = g7WholeScaffoldQuestion.correct_answer;
                                                    const ok = normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct);
                                                    setG7WholeScaffoldFeedback({
                                                        isCorrect: ok,
                                                        correctAnswer: g7WholeScaffoldQuestion.correct_answer,
                                                        explanation: g7WholeScaffoldQuestion.explanation
                                                    });
                                                }}
                                                disabled={String(g7WholeScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG7WholeScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                            >
                                                {g7WholeScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                            <button
                                                onClick={() => {
                                                    setG7WholeScaffoldStepIndex((prev) => {
                                                        const next = prev + 1;
                                                        return next >= scaffoldSteps.length ? 0 : next;
                                                    });
                                                }}
                                                disabled={!g7WholeScaffoldFeedback?.isCorrect}
                                                className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                            >
                                                Next Step
                                            </button>
                                        </div>

                                        {g7WholeScaffoldFeedback && (
                                            <div className={`mt-4 p-3 rounded-lg text-sm border ${g7WholeScaffoldFeedback.isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
                                                <div className="font-semibold">{g7WholeScaffoldFeedback.isCorrect ? 'Correct' : 'Not quite'}</div>
                                                <div className="mt-1"><span className="font-semibold">Correct answer:</span> {g7WholeScaffoldFeedback.correctAnswer}</div>
                                            </div>
                                        )}

                                        {g7WholeScaffoldShowHint && g7WholeScaffoldQuestion.explanation && (
                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                {g7WholeScaffoldQuestion.explanation}
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

                <VisualAidsPanel isOpen={g7WholeVisualAidsOpen} setIsOpen={setG7WholeVisualAidsOpen}>
                    {renderWholeNumbersVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade7WholeNumbersScaffold;
