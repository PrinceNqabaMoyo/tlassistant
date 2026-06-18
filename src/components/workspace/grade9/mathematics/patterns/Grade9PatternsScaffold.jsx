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

const Grade9PatternsScaffold = ({
    onBack,
    scaffoldSteps,
    g9PatVisualAidsOpen,
    setG9PatVisualAidsOpen,
    g9PatScaffoldDifficulty,
    setG9PatScaffoldDifficulty,
    g9PatScaffoldStepIndex,
    setG9PatScaffoldStepIndex,
    fetchGrade9PatternsScaffoldQuestion,
    g9PatScaffoldLoading,
    g9PatScaffoldError,
    g9PatScaffoldQuestion,
    g9PatScaffoldShowHint,
    setG9PatScaffoldShowHint,
    g9PatScaffoldAnswer,
    setG9PatScaffoldAnswer,
    g9PatScaffoldFeedback,
    setG9PatScaffoldFeedback,
    g9PatScaffoldCheckpointIndex,
    setG9PatScaffoldCheckpointIndex,
    g9PatScaffoldCheckpointAnswers,
    setG9PatScaffoldCheckpointAnswers,
    g9PatScaffoldCheckpointFeedback,
    setG9PatScaffoldCheckpointFeedback,
    renderGrade9PatternsVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Numeric &amp; Geometric Patterns • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g9PatVisualAidsOpen && (
                                <button
                                    onClick={() => setG9PatVisualAidsOpen(true)}
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
                                value={g9PatScaffoldDifficulty}
                                onChange={(e) => setG9PatScaffoldDifficulty(e.target.value)}
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
                                value={g9PatScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG9PatScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG9PatScaffoldFeedback(null);
                                    setG9PatScaffoldShowHint(false);
                                    setG9PatScaffoldCheckpointIndex(0);
                                    setG9PatScaffoldCheckpointAnswers({});
                                    setG9PatScaffoldCheckpointFeedback({});
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
                                    const step = scaffoldSteps[g9PatScaffoldStepIndex] || scaffoldSteps[0];
                                    fetchGrade9PatternsScaffoldQuestion({ subskill: step.key, difficulty: g9PatScaffoldDifficulty });
                                }}
                                disabled={g9PatScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g9PatScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <div>
                                <div className="text-sm font-semibold text-gray-800">
                                    Step {g9PatScaffoldStepIndex + 1} / {scaffoldSteps.length}: {scaffoldSteps[g9PatScaffoldStepIndex]?.title}
                                </div>
                                <div className="text-sm text-gray-600">{scaffoldSteps[g9PatScaffoldStepIndex]?.prompt}</div>
                            </div>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                            <div
                                className="bg-indigo-600 h-2 rounded-full"
                                style={{ width: `${Math.round(((g9PatScaffoldStepIndex + 1) / scaffoldSteps.length) * 100)}%` }}
                            />
                        </div>
                    </div>

                    {g9PatScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g9PatScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g9PatScaffoldLoading && !g9PatScaffoldQuestion ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : g9PatScaffoldQuestion ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{g9PatScaffoldQuestion.question}</div>

                                {g9PatScaffoldQuestion.question_type === 'scaffold' && Array.isArray(g9PatScaffoldQuestion.checkpoints) ? (
                                    (() => {
                                        const cps = g9PatScaffoldQuestion.checkpoints;
                                        const cp = cps[g9PatScaffoldCheckpointIndex];
                                        const cpId = cp?.id || `cp_${g9PatScaffoldCheckpointIndex}`;
                                        const answerValue = g9PatScaffoldCheckpointAnswers[cpId] ?? '';
                                        const feedback = g9PatScaffoldCheckpointFeedback[cpId];
                                        const isDone = g9PatScaffoldCheckpointIndex >= cps.length;
                                        const isAllCorrect = cps.every((c, idx) => {
                                            const id = c?.id || `cp_${idx}`;
                                            return g9PatScaffoldCheckpointFeedback[id]?.isCorrect;
                                        });

                                        return (
                                            <div>
                                                {Array.isArray(g9PatScaffoldQuestion.steps) && (
                                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                            {g9PatScaffoldQuestion.steps.map((s, idx) => (
                                                                <li
                                                                    key={`${idx}_${s}`}
                                                                    className={idx === Math.min(g9PatScaffoldCheckpointIndex, g9PatScaffoldQuestion.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}
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
                                                            Checkpoint {g9PatScaffoldCheckpointIndex + 1} / {cps.length}
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
                                                                            onChange={(e) => setG9PatScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                        />
                                                                        <span className="text-gray-800">{opt}</span>
                                                                    </label>
                                                                ))}
                                                            </div>
                                                        ) : (
                                                            <input
                                                                type="text"
                                                                value={answerValue}
                                                                onChange={(e) => setG9PatScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                                placeholder="Type your answer"
                                                            />
                                                        )}

                                                        <div className="mt-3 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                            <button
                                                                onClick={() => {
                                                                    const user = String(answerValue);
                                                                    const correct = String(cp.correct_answer ?? '');

                                                                    const ok = cp.kind === 'mcq'
                                                                        ? user === correct
                                                                        : (
                                                                            normalizeCommaNumberList(user) === normalizeCommaNumberList(correct)
                                                                            || normalizePatternAnswer(user) === normalizePatternAnswer(correct)
                                                                        );

                                                                    setG9PatScaffoldCheckpointFeedback((prev) => ({
                                                                        ...prev,
                                                                        [cpId]: {
                                                                            isCorrect: ok,
                                                                            correctAnswer: correct,
                                                                            explanation: cp.explanation
                                                                        }
                                                                    }));

                                                                    if (ok) {
                                                                        setG9PatScaffoldCheckpointIndex((prev) => prev + 1);
                                                                    }
                                                                }}
                                                                disabled={String(answerValue).trim() === ''}
                                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                                            >
                                                                Check
                                                            </button>
                                                            {feedback && (
                                                                <div className={`text-sm ${feedback.isCorrect ? 'text-green-700' : 'text-red-700'}`}>
                                                                    {feedback.isCorrect ? 'Correct.' : `Incorrect. Correct answer: ${feedback.correctAnswer}`}
                                                                </div>
                                                            )}
                                                        </div>

                                                        {feedback?.explanation && (
                                                            <div className="mt-3 text-sm text-gray-700 bg-gray-50 border border-gray-200 rounded-lg p-3">
                                                                {feedback.explanation}
                                                            </div>
                                                        )}
                                                    </div>
                                                )}

                                                {isDone && (
                                                    <div className="bg-white border border-gray-200 rounded-lg p-4">
                                                        <div className="text-gray-900 font-semibold mb-2">Finished</div>
                                                        <div className={`text-sm font-semibold ${isAllCorrect ? 'text-green-700' : 'text-red-700'}`}>
                                                            {isAllCorrect ? 'All checkpoints correct.' : 'Some checkpoints are incorrect.'}
                                                        </div>
                                                        {g9PatScaffoldQuestion.explanation && (
                                                            <div className="mt-3 text-sm text-gray-700 bg-gray-50 border border-gray-200 rounded-lg p-3">
                                                                {g9PatScaffoldQuestion.explanation}
                                                            </div>
                                                        )}
                                                    </div>
                                                )}
                                            </div>
                                        );
                                    })()
                                ) : (
                                    <>
                                        <div className="mb-3">
                                            <label className="block text-sm font-semibold text-gray-700 mb-1">Your answer</label>
                                            <input
                                                type="text"
                                                value={g9PatScaffoldAnswer}
                                                onChange={(e) => setG9PatScaffoldAnswer(e.target.value)}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        </div>

                                        <div className="flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={() => {
                                                    const user = String(g9PatScaffoldAnswer);
                                                    const correct = String(g9PatScaffoldQuestion.correct_answer ?? '');

                                                    const ok = g9PatScaffoldQuestion.question_type === 'mcq'
                                                        ? user === correct
                                                        : (
                                                            normalizeCommaNumberList(user) === normalizeCommaNumberList(correct)
                                                            || normalizePatternAnswer(user) === normalizePatternAnswer(correct)
                                                        );

                                                    setG9PatScaffoldFeedback({
                                                        isCorrect: ok,
                                                        correctAnswer: correct,
                                                        explanation: g9PatScaffoldQuestion.explanation,
                                                    });
                                                }}
                                                disabled={String(g9PatScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG9PatScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-indigo-50 text-indigo-800 rounded-lg font-semibold border border-indigo-200 hover:bg-indigo-100"
                                            >
                                                {g9PatScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                        </div>

                                        {g9PatScaffoldFeedback && (
                                            <div className={`mt-4 p-4 rounded-lg border ${g9PatScaffoldFeedback.isCorrect ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                                                <div className="font-semibold">{g9PatScaffoldFeedback.isCorrect ? 'Correct!' : 'Not quite.'}</div>
                                                {!g9PatScaffoldFeedback.isCorrect && (
                                                    <div className="mt-1 text-sm"><span className="font-semibold">Correct answer:</span> {g9PatScaffoldFeedback.correctAnswer}</div>
                                                )}
                                            </div>
                                        )}

                                        {g9PatScaffoldShowHint && g9PatScaffoldQuestion.explanation && (
                                            <div className="mt-3 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                {g9PatScaffoldQuestion.explanation}
                                            </div>
                                        )}
                                    </>
                                )}
                            </>
                        ) : (
                            <div className="text-gray-600">No question loaded yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g9PatVisualAidsOpen} setIsOpen={setG9PatVisualAidsOpen}>
                    {renderGrade9PatternsVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade9PatternsScaffold;
