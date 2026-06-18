import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const normalizePatternAnswer = (value) => {
    if (value === null || value === undefined) return '';
    return String(value)
        .trim()
        .replace(/;/g, ',')
        .replace(/\s+/g, '')
        .replace(/−/g, '-')
        .toLowerCase();
};

const normalizeCommaNumberList = (value) => {
    const s = normalizePatternAnswer(value);
    if (!s) return '';
    const parts = s
        .split(',')
        .map((p) => p.trim())
        .filter(Boolean);
    return parts.join(',');
};

const Grade8PatternsScaffold = ({
    onBack,
    scaffoldSteps,
    g8PatVisualAidsOpen,
    setG8PatVisualAidsOpen,
    g8PatScaffoldDifficulty,
    setG8PatScaffoldDifficulty,
    g8PatScaffoldStepIndex,
    setG8PatScaffoldStepIndex,
    fetchGrade8PatternsScaffoldQuestion,
    g8PatScaffoldLoading,
    g8PatScaffoldError,
    g8PatScaffoldQuestion,
    g8PatScaffoldShowHint,
    setG8PatScaffoldShowHint,
    g8PatScaffoldAnswer,
    setG8PatScaffoldAnswer,
    g8PatScaffoldFeedback,
    setG8PatScaffoldFeedback,
    g8PatScaffoldCheckpointIndex,
    setG8PatScaffoldCheckpointIndex,
    g8PatScaffoldCheckpointAnswers,
    setG8PatScaffoldCheckpointAnswers,
    g8PatScaffoldCheckpointFeedback,
    setG8PatScaffoldCheckpointFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade8PatternsVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 8 Mathematics • Numeric &amp; Geometric Patterns • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g8PatVisualAidsOpen && (
                                <button
                                    onClick={() => setG8PatVisualAidsOpen(true)}
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
                                value={g8PatScaffoldDifficulty}
                                onChange={(e) => setG8PatScaffoldDifficulty(e.target.value)}
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
                                value={g8PatScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG8PatScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG8PatScaffoldFeedback(null);
                                    setG8PatScaffoldShowHint(false);
                                    setG8PatScaffoldCheckpointIndex(0);
                                    setG8PatScaffoldCheckpointAnswers({});
                                    setG8PatScaffoldCheckpointFeedback({});
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
                                    const step = scaffoldSteps[g8PatScaffoldStepIndex] || scaffoldSteps[0];
                                    fetchGrade8PatternsScaffoldQuestion({ subskill: step.key, difficulty: g8PatScaffoldDifficulty });
                                }}
                                disabled={g8PatScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g8PatScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <div>
                                <div className="text-sm font-semibold text-gray-800">
                                    Step {g8PatScaffoldStepIndex + 1} / {scaffoldSteps.length}: {scaffoldSteps[g8PatScaffoldStepIndex]?.title}
                                </div>
                                <div className="text-sm text-gray-600">{scaffoldSteps[g8PatScaffoldStepIndex]?.prompt}</div>
                            </div>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                            <div
                                className="bg-indigo-600 h-2 rounded-full"
                                style={{ width: `${Math.round(((g8PatScaffoldStepIndex + 1) / scaffoldSteps.length) * 100)}%` }}
                            />
                        </div>
                    </div>

                    {g8PatScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g8PatScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g8PatScaffoldLoading && !g8PatScaffoldQuestion ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : g8PatScaffoldQuestion ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{g8PatScaffoldQuestion.question}</div>

                                {g8PatScaffoldQuestion.question_type === 'scaffold' && Array.isArray(g8PatScaffoldQuestion.checkpoints) ? (
                                    (() => {
                                        const cps = g8PatScaffoldQuestion.checkpoints;
                                        const cp = cps[g8PatScaffoldCheckpointIndex];
                                        const cpId = cp?.id || `cp_${g8PatScaffoldCheckpointIndex}`;
                                        const answerValue = g8PatScaffoldCheckpointAnswers[cpId] ?? '';
                                        const feedback = g8PatScaffoldCheckpointFeedback[cpId];
                                        const isDone = g8PatScaffoldCheckpointIndex >= cps.length;
                                        const isAllCorrect = cps.every((c, idx) => {
                                            const id = c?.id || `cp_${idx}`;
                                            return g8PatScaffoldCheckpointFeedback[id]?.isCorrect;
                                        });

                                        return (
                                            <div>
                                                {Array.isArray(g8PatScaffoldQuestion.steps) && (
                                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                            {g8PatScaffoldQuestion.steps.map((s, idx) => (
                                                                <li
                                                                    key={`${idx}_${s}`}
                                                                    className={idx === Math.min(g8PatScaffoldCheckpointIndex, g8PatScaffoldQuestion.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}
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
                                                            Checkpoint {g8PatScaffoldCheckpointIndex + 1} / {cps.length}
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
                                                                            onChange={(e) => setG8PatScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                        />
                                                                        <span className="text-gray-800">{opt}</span>
                                                                    </label>
                                                                ))}
                                                            </div>
                                                        ) : (
                                                            <input
                                                                type="text"
                                                                value={answerValue}
                                                                onChange={(e) => setG8PatScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                                placeholder="Type your answer"
                                                            />
                                                        )}

                                                        <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                            <button
                                                                onClick={() => {
                                                                    const user = String(answerValue);
                                                                    const correct = String(cp.correct_answer ?? '');

                                                                    const ok = cp.kind === 'mcq'
                                                                        ? user === correct
                                                                        : (
                                                                            normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                                            || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase()
                                                                            || normalizeCommaNumberList(user) === normalizeCommaNumberList(correct)
                                                                            || normalizePatternAnswer(user) === normalizePatternAnswer(correct)
                                                                        );

                                                                    setG8PatScaffoldCheckpointFeedback((prev) => ({
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
                                                                onClick={() => setG8PatScaffoldShowHint((p) => !p)}
                                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                                            >
                                                                {g8PatScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                                            </button>
                                                            <button
                                                                onClick={() => {
                                                                    const ok = !!g8PatScaffoldCheckpointFeedback[cpId]?.isCorrect;
                                                                    if (!ok) return;
                                                                    setG8PatScaffoldCheckpointIndex((prev) => prev + 1);
                                                                    setG8PatScaffoldShowHint(false);
                                                                }}
                                                                disabled={!g8PatScaffoldCheckpointFeedback[cpId]?.isCorrect}
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

                                                        {g8PatScaffoldShowHint && (feedback?.explanation || cp?.explanation) && (
                                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                                {feedback?.explanation || cp?.explanation}
                                                            </div>
                                                        )}
                                                    </div>
                                                )}

                                                <div className="mt-4">
                                                    <button
                                                        onClick={() => {
                                                            setG8PatScaffoldStepIndex((prev) => {
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
                                            value={g8PatScaffoldAnswer}
                                            onChange={(e) => setG8PatScaffoldAnswer(e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Type your answer"
                                        />

                                        <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={() => {
                                                    const user = String(g8PatScaffoldAnswer);
                                                    const correct = String(g8PatScaffoldQuestion.correct_answer ?? '');

                                                    const ok = normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                        || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase()
                                                        || normalizeCommaNumberList(user) === normalizeCommaNumberList(correct)
                                                        || normalizePatternAnswer(user) === normalizePatternAnswer(correct);

                                                    setG8PatScaffoldFeedback({
                                                        isCorrect: ok,
                                                        correctAnswer: g8PatScaffoldQuestion.correct_answer,
                                                        explanation: g8PatScaffoldQuestion.explanation
                                                    });
                                                }}
                                                disabled={String(g8PatScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG8PatScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                            >
                                                {g8PatScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                            <button
                                                onClick={() => {
                                                    setG8PatScaffoldStepIndex((prev) => {
                                                        const next = prev + 1;
                                                        return next >= scaffoldSteps.length ? 0 : next;
                                                    });
                                                }}
                                                disabled={!g8PatScaffoldFeedback?.isCorrect}
                                                className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                            >
                                                Next Step
                                            </button>
                                        </div>

                                        {g8PatScaffoldFeedback && (
                                            <div className={`mt-4 p-3 rounded-lg text-sm border ${g8PatScaffoldFeedback.isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
                                                <div className="font-semibold">{g8PatScaffoldFeedback.isCorrect ? 'Correct' : 'Not quite'}</div>
                                                <div className="mt-1"><span className="font-semibold">Correct answer:</span> {g8PatScaffoldFeedback.correctAnswer}</div>
                                            </div>
                                        )}

                                        {g8PatScaffoldShowHint && g8PatScaffoldQuestion.explanation && (
                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                {g8PatScaffoldQuestion.explanation}
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

                <VisualAidsPanel isOpen={g8PatVisualAidsOpen} setIsOpen={setG8PatVisualAidsOpen}>
                    {renderGrade8PatternsVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade8PatternsScaffold;
