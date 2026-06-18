import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';
import FunctionGraph from '../../../FunctionGraph';

const normalizeFunctionAnswer = (value) => {
    if (value === null || value === undefined) return '';
    return String(value)
        .trim()
        .replace(/−/g, '-')
        .replace(/×/g, 'x')
        .replace(/\s+/g, '')
        .toLowerCase();
};

const normalizeCommaList = (value) => {
    const s = String(value ?? '')
        .trim()
        .replace(/−/g, '-')
        .replace(/\s+/g, '');
    if (!s) return '';
    return s
        .split(',')
        .map((p) => p.trim())
        .filter(Boolean)
        .join(',');
};

const Grade9FunctionsRelationshipsScaffold = ({
    onBack,
    scaffoldSteps,
    g9FuncVisualAidsOpen,
    setG9FuncVisualAidsOpen,
    g9FuncScaffoldDifficulty,
    setG9FuncScaffoldDifficulty,
    g9FuncScaffoldStepIndex,
    setG9FuncScaffoldStepIndex,
    fetchGrade9FunctionsScaffoldQuestion,
    g9FuncScaffoldLoading,
    g9FuncScaffoldError,
    g9FuncScaffoldQuestion,
    g9FuncScaffoldShowHint,
    setG9FuncScaffoldShowHint,
    g9FuncScaffoldAnswer,
    setG9FuncScaffoldAnswer,
    g9FuncScaffoldFeedback,
    setG9FuncScaffoldFeedback,
    g9FuncScaffoldCheckpointIndex,
    setG9FuncScaffoldCheckpointIndex,
    g9FuncScaffoldCheckpointAnswers,
    setG9FuncScaffoldCheckpointAnswers,
    g9FuncScaffoldCheckpointFeedback,
    setG9FuncScaffoldCheckpointFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade9FunctionsVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Functions &amp; Relationships • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g9FuncVisualAidsOpen && (
                                <button
                                    onClick={() => setG9FuncVisualAidsOpen(true)}
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
                                value={g9FuncScaffoldDifficulty}
                                onChange={(e) => setG9FuncScaffoldDifficulty(e.target.value)}
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
                                value={g9FuncScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG9FuncScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG9FuncScaffoldFeedback(null);
                                    setG9FuncScaffoldShowHint(false);
                                    setG9FuncScaffoldCheckpointIndex(0);
                                    setG9FuncScaffoldCheckpointAnswers({});
                                    setG9FuncScaffoldCheckpointFeedback({});
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
                                    const step = scaffoldSteps[g9FuncScaffoldStepIndex] || scaffoldSteps[0];
                                    fetchGrade9FunctionsScaffoldQuestion({ subskill: step.key, difficulty: g9FuncScaffoldDifficulty });
                                }}
                                disabled={g9FuncScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g9FuncScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    {g9FuncScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g9FuncScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g9FuncScaffoldLoading && !g9FuncScaffoldQuestion ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : g9FuncScaffoldQuestion ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{g9FuncScaffoldQuestion.question}</div>

                                {g9FuncScaffoldQuestion.graph && (
                                    <div className="mb-4">
                                        <FunctionGraph graph={g9FuncScaffoldQuestion.graph} />
                                    </div>
                                )}

                                {g9FuncScaffoldQuestion.question_type === 'scaffold' && Array.isArray(g9FuncScaffoldQuestion.checkpoints) ? (
                                    (() => {
                                        const cps = g9FuncScaffoldQuestion.checkpoints;
                                        const cp = cps[g9FuncScaffoldCheckpointIndex];
                                        const cpId = cp?.id || `cp_${g9FuncScaffoldCheckpointIndex}`;
                                        const answerValue = g9FuncScaffoldCheckpointAnswers[cpId] ?? '';
                                        const feedback = g9FuncScaffoldCheckpointFeedback[cpId];
                                        const isDone = g9FuncScaffoldCheckpointIndex >= cps.length;

                                        return (
                                            <div>
                                                {Array.isArray(g9FuncScaffoldQuestion.steps) && (
                                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                            {g9FuncScaffoldQuestion.steps.map((s, idx) => (
                                                                <li
                                                                    key={`${idx}_${s}`}
                                                                    className={idx === Math.min(g9FuncScaffoldCheckpointIndex, g9FuncScaffoldQuestion.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}
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
                                                            Checkpoint {g9FuncScaffoldCheckpointIndex + 1} / {cps.length}
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
                                                                            onChange={(e) => setG9FuncScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                        />
                                                                        <span className="text-gray-800">{opt}</span>
                                                                    </label>
                                                                ))}
                                                            </div>
                                                        ) : (
                                                            <input
                                                                type="text"
                                                                value={answerValue}
                                                                onChange={(e) => setG9FuncScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                                placeholder="Type your answer"
                                                            />
                                                        )}

                                                        <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                            <button
                                                                onClick={() => {
                                                                    const user = String(answerValue);
                                                                    const correct = String(cp.correct_answer ?? cp.answer ?? '');
                                                                    const ok = cp.kind === 'mcq'
                                                                        ? user === correct
                                                                        : (
                                                                            normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                                            || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase()
                                                                            || normalizeCommaList(user) === normalizeCommaList(correct)
                                                                            || normalizeFunctionAnswer(user) === normalizeFunctionAnswer(correct)
                                                                        );

                                                                    setG9FuncScaffoldCheckpointFeedback((prev) => ({
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
                                                                onClick={() => setG9FuncScaffoldShowHint((p) => !p)}
                                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                                            >
                                                                {g9FuncScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                                            </button>
                                                            <button
                                                                onClick={() => {
                                                                    const ok = !!g9FuncScaffoldCheckpointFeedback[cpId]?.isCorrect;
                                                                    if (!ok) return;
                                                                    setG9FuncScaffoldCheckpointIndex((prev) => prev + 1);
                                                                }}
                                                                disabled={!g9FuncScaffoldCheckpointFeedback[cpId]?.isCorrect}
                                                                className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                                            >
                                                                Next
                                                            </button>
                                                        </div>

                                                        {feedback?.explanation && g9FuncScaffoldShowHint && (
                                                            <div className="mt-3 text-sm text-gray-700 bg-indigo-50 border border-indigo-100 rounded-lg p-3">
                                                                {feedback.explanation}
                                                            </div>
                                                        )}
                                                    </div>
                                                )}

                                                {isDone && (
                                                    <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                                                        <div className="font-semibold text-green-900">Done!</div>
                                                        <div className="text-sm text-green-800 mt-1">
                                                            Final answer: <span className="font-semibold">{g9FuncScaffoldQuestion.correct_answer}</span>
                                                        </div>
                                                    </div>
                                                )}
                                            </div>
                                        );
                                    })()
                                ) : (
                                    <>
                                        <div className="mb-4">
                                            <label className="block text-sm font-semibold text-gray-700 mb-1">Your answer</label>
                                            <input
                                                type="text"
                                                value={g9FuncScaffoldAnswer}
                                                onChange={(e) => setG9FuncScaffoldAnswer(e.target.value)}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        </div>
                                        <div className="flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={() => {
                                                    const user = String(g9FuncScaffoldAnswer);
                                                    const correct = String(g9FuncScaffoldQuestion.correct_answer ?? g9FuncScaffoldQuestion.answer ?? '');

                                                    const ok = g9FuncScaffoldQuestion.question_type === 'mcq'
                                                        ? user === correct
                                                        : (
                                                            normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                            || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase()
                                                            || normalizeCommaList(user) === normalizeCommaList(correct)
                                                            || normalizeFunctionAnswer(user) === normalizeFunctionAnswer(correct)
                                                        );

                                                    setG9FuncScaffoldFeedback({
                                                        isCorrect: ok,
                                                        correctAnswer: g9FuncScaffoldQuestion.correct_answer ?? g9FuncScaffoldQuestion.answer,
                                                        explanation: g9FuncScaffoldQuestion.explanation,
                                                    });
                                                }}
                                                disabled={String(g9FuncScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG9FuncScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                            >
                                                {g9FuncScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                        </div>

                                        {g9FuncScaffoldFeedback && (
                                            <div className={`mt-4 p-4 rounded-lg border text-sm ${g9FuncScaffoldFeedback.isCorrect ? 'border-green-200 bg-green-50 text-green-800' : 'border-red-200 bg-red-50 text-red-800'}`}>
                                                <div className="font-semibold">{g9FuncScaffoldFeedback.isCorrect ? 'Correct' : 'Incorrect'}</div>
                                                {!g9FuncScaffoldFeedback.isCorrect && (
                                                    <div className="mt-1"><span className="font-semibold">Correct answer:</span> {g9FuncScaffoldFeedback.correctAnswer}</div>
                                                )}
                                                {g9FuncScaffoldShowHint && g9FuncScaffoldFeedback.explanation && (
                                                    <div className="mt-2">{g9FuncScaffoldFeedback.explanation}</div>
                                                )}
                                            </div>
                                        )}
                                    </>
                                )}
                            </>
                        ) : (
                            <div className="text-gray-600">No question yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g9FuncVisualAidsOpen} setIsOpen={setG9FuncVisualAidsOpen}>
                    {renderGrade9FunctionsVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade9FunctionsRelationshipsScaffold;
