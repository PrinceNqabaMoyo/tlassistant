import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

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

const Grade8FunctionsScaffold = ({
    onBack,
    scaffoldSteps,
    g8FuncVisualAidsOpen,
    setG8FuncVisualAidsOpen,
    g8FuncScaffoldDifficulty,
    setG8FuncScaffoldDifficulty,
    g8FuncScaffoldStepIndex,
    setG8FuncScaffoldStepIndex,
    fetchGrade8FunctionsScaffoldQuestion,
    g8FuncScaffoldLoading,
    g8FuncScaffoldError,
    g8FuncScaffoldQuestion,
    g8FuncScaffoldShowHint,
    setG8FuncScaffoldShowHint,
    g8FuncScaffoldAnswer,
    setG8FuncScaffoldAnswer,
    g8FuncScaffoldFeedback,
    setG8FuncScaffoldFeedback,
    g8FuncScaffoldCheckpointIndex,
    setG8FuncScaffoldCheckpointIndex,
    g8FuncScaffoldCheckpointAnswers,
    setG8FuncScaffoldCheckpointAnswers,
    g8FuncScaffoldCheckpointFeedback,
    setG8FuncScaffoldCheckpointFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade8FunctionsVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 8 Mathematics • Functions &amp; Relationships • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g8FuncVisualAidsOpen && (
                                <button
                                    onClick={() => setG8FuncVisualAidsOpen(true)}
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
                                value={g8FuncScaffoldDifficulty}
                                onChange={(e) => setG8FuncScaffoldDifficulty(e.target.value)}
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
                                value={g8FuncScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG8FuncScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG8FuncScaffoldFeedback(null);
                                    setG8FuncScaffoldShowHint(false);
                                    setG8FuncScaffoldCheckpointIndex(0);
                                    setG8FuncScaffoldCheckpointAnswers({});
                                    setG8FuncScaffoldCheckpointFeedback({});
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
                                    const step = scaffoldSteps[g8FuncScaffoldStepIndex] || scaffoldSteps[0];
                                    fetchGrade8FunctionsScaffoldQuestion({ subskill: step.key, difficulty: g8FuncScaffoldDifficulty });
                                }}
                                disabled={g8FuncScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g8FuncScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <div>
                                <div className="text-sm font-semibold text-gray-800">
                                    Step {g8FuncScaffoldStepIndex + 1} / {scaffoldSteps.length}: {scaffoldSteps[g8FuncScaffoldStepIndex]?.title}
                                </div>
                                <div className="text-sm text-gray-600">{scaffoldSteps[g8FuncScaffoldStepIndex]?.prompt}</div>
                            </div>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                            <div
                                className="bg-indigo-600 h-2 rounded-full"
                                style={{ width: `${Math.round(((g8FuncScaffoldStepIndex + 1) / scaffoldSteps.length) * 100)}%` }}
                            />
                        </div>
                    </div>

                    {g8FuncScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g8FuncScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g8FuncScaffoldLoading && !g8FuncScaffoldQuestion ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : g8FuncScaffoldQuestion ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{g8FuncScaffoldQuestion.question}</div>

                                {g8FuncScaffoldQuestion.question_type === 'scaffold' && Array.isArray(g8FuncScaffoldQuestion.checkpoints) ? (
                                    (() => {
                                        const cps = g8FuncScaffoldQuestion.checkpoints;
                                        const cp = cps[g8FuncScaffoldCheckpointIndex];
                                        const cpId = cp?.id || `cp_${g8FuncScaffoldCheckpointIndex}`;
                                        const answerValue = g8FuncScaffoldCheckpointAnswers[cpId] ?? '';
                                        const feedback = g8FuncScaffoldCheckpointFeedback[cpId];
                                        const isDone = g8FuncScaffoldCheckpointIndex >= cps.length;

                                        return (
                                            <div>
                                                {Array.isArray(g8FuncScaffoldQuestion.steps) && (
                                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                            {g8FuncScaffoldQuestion.steps.map((s, idx) => (
                                                                <li
                                                                    key={`${idx}_${s}`}
                                                                    className={idx === Math.min(g8FuncScaffoldCheckpointIndex, g8FuncScaffoldQuestion.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}
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
                                                            Checkpoint {g8FuncScaffoldCheckpointIndex + 1} / {cps.length}
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
                                                                            onChange={(e) => setG8FuncScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                        />
                                                                        <span className="text-gray-800">{opt}</span>
                                                                    </label>
                                                                ))}
                                                            </div>
                                                        ) : (
                                                            <input
                                                                type="text"
                                                                value={answerValue}
                                                                onChange={(e) => setG8FuncScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
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

                                                                    setG8FuncScaffoldCheckpointFeedback((prev) => ({
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
                                                                onClick={() => setG8FuncScaffoldShowHint((p) => !p)}
                                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                                            >
                                                                {g8FuncScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                                            </button>
                                                            <button
                                                                onClick={() => {
                                                                    const ok = !!g8FuncScaffoldCheckpointFeedback[cpId]?.isCorrect;
                                                                    if (!ok) return;
                                                                    setG8FuncScaffoldCheckpointIndex((prev) => prev + 1);
                                                                }}
                                                                disabled={!g8FuncScaffoldCheckpointFeedback[cpId]?.isCorrect}
                                                                className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                                            >
                                                                Next
                                                            </button>
                                                        </div>

                                                        {feedback?.explanation && g8FuncScaffoldShowHint && (
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
                                                            Final answer: <span className="font-semibold">{g8FuncScaffoldQuestion.correct_answer}</span>
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
                                                value={g8FuncScaffoldAnswer}
                                                onChange={(e) => setG8FuncScaffoldAnswer(e.target.value)}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        </div>
                                        <div className="flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={() => {
                                                    const user = String(g8FuncScaffoldAnswer);
                                                    const correct = String(g8FuncScaffoldQuestion.correct_answer ?? g8FuncScaffoldQuestion.answer ?? '');

                                                    const ok = g8FuncScaffoldQuestion.question_type === 'mcq'
                                                        ? user === correct
                                                        : (
                                                            normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                            || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase()
                                                            || normalizeCommaList(user) === normalizeCommaList(correct)
                                                            || normalizeFunctionAnswer(user) === normalizeFunctionAnswer(correct)
                                                        );

                                                    setG8FuncScaffoldFeedback({
                                                        isCorrect: ok,
                                                        correctAnswer: g8FuncScaffoldQuestion.correct_answer ?? g8FuncScaffoldQuestion.answer,
                                                        explanation: g8FuncScaffoldQuestion.explanation,
                                                    });
                                                }}
                                                disabled={String(g8FuncScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG8FuncScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                            >
                                                {g8FuncScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                        </div>

                                        {g8FuncScaffoldFeedback && (
                                            <div className={`mt-4 p-4 rounded-lg border text-sm ${g8FuncScaffoldFeedback.isCorrect ? 'border-green-200 bg-green-50 text-green-800' : 'border-red-200 bg-red-50 text-red-800'}`}>
                                                <div className="font-semibold">{g8FuncScaffoldFeedback.isCorrect ? 'Correct' : 'Incorrect'}</div>
                                                {!g8FuncScaffoldFeedback.isCorrect && (
                                                    <div className="mt-1"><span className="font-semibold">Correct answer:</span> {g8FuncScaffoldFeedback.correctAnswer}</div>
                                                )}
                                                {g8FuncScaffoldShowHint && g8FuncScaffoldFeedback.explanation && (
                                                    <div className="mt-2">{g8FuncScaffoldFeedback.explanation}</div>
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

                <VisualAidsPanel isOpen={g8FuncVisualAidsOpen} setIsOpen={setG8FuncVisualAidsOpen}>
                    {renderGrade8FunctionsVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade8FunctionsScaffold;
