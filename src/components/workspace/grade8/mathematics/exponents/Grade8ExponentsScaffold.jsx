import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const normalizeExponentAnswer = (value) => {
    if (value === null || value === undefined) return '';
    return String(value)
        .trim()
        .replace(/\s+/g, '')
        .replace(/,/g, '')
        .replace(/×/g, 'x')
        .replace(/−/g, '-')
        .toLowerCase();
};

const Grade8ExponentsScaffold = ({
    onBack,
    scaffoldSteps,
    g8ExpVisualAidsOpen,
    setG8ExpVisualAidsOpen,
    g8ExpScaffoldDifficulty,
    setG8ExpScaffoldDifficulty,
    g8ExpScaffoldStepIndex,
    setG8ExpScaffoldStepIndex,
    fetchGrade8ExponentsScaffoldQuestion,
    g8ExpScaffoldLoading,
    g8ExpScaffoldError,
    g8ExpScaffoldQuestion,
    g8ExpScaffoldShowHint,
    setG8ExpScaffoldShowHint,
    g8ExpScaffoldAnswer,
    setG8ExpScaffoldAnswer,
    g8ExpScaffoldFeedback,
    setG8ExpScaffoldFeedback,
    g8ExpScaffoldCheckpointIndex,
    setG8ExpScaffoldCheckpointIndex,
    g8ExpScaffoldCheckpointAnswers,
    setG8ExpScaffoldCheckpointAnswers,
    g8ExpScaffoldCheckpointFeedback,
    setG8ExpScaffoldCheckpointFeedback,
    formatExponentCarets,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade8ExponentsVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 8 Mathematics • Exponents • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step method practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g8ExpVisualAidsOpen && (
                                <button
                                    onClick={() => setG8ExpVisualAidsOpen(true)}
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
                                value={g8ExpScaffoldDifficulty}
                                onChange={(e) => setG8ExpScaffoldDifficulty(e.target.value)}
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
                                value={g8ExpScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG8ExpScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG8ExpScaffoldFeedback(null);
                                    setG8ExpScaffoldShowHint(false);
                                    setG8ExpScaffoldCheckpointIndex(0);
                                    setG8ExpScaffoldCheckpointAnswers({});
                                    setG8ExpScaffoldCheckpointFeedback({});
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
                                    const step = scaffoldSteps[g8ExpScaffoldStepIndex] || scaffoldSteps[0];
                                    fetchGrade8ExponentsScaffoldQuestion({ subskill: step.key, difficulty: g8ExpScaffoldDifficulty });
                                }}
                                disabled={g8ExpScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g8ExpScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="mb-4">
                        <div className="text-sm font-semibold text-gray-800">Step {g8ExpScaffoldStepIndex + 1} / {scaffoldSteps.length}: {scaffoldSteps[g8ExpScaffoldStepIndex]?.title}</div>
                        <div className="text-sm text-gray-600">{scaffoldSteps[g8ExpScaffoldStepIndex]?.prompt}</div>
                        <div className="w-full bg-gray-200 rounded-full h-2 mt-2">
                            <div
                                className="bg-indigo-600 h-2 rounded-full"
                                style={{ width: `${Math.round(((g8ExpScaffoldStepIndex + 1) / scaffoldSteps.length) * 100)}%` }}
                            />
                        </div>
                    </div>

                    {g8ExpScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g8ExpScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g8ExpScaffoldLoading && !g8ExpScaffoldQuestion ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : g8ExpScaffoldQuestion ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{formatExponentCarets(g8ExpScaffoldQuestion.question)}</div>

                                {g8ExpScaffoldQuestion.question_type === 'scaffold' && Array.isArray(g8ExpScaffoldQuestion.checkpoints) ? (
                                    (() => {
                                        const cps = g8ExpScaffoldQuestion.checkpoints;
                                        const cp = cps[g8ExpScaffoldCheckpointIndex];
                                        const cpId = cp?.id || `cp_${g8ExpScaffoldCheckpointIndex}`;
                                        const answerValue = g8ExpScaffoldCheckpointAnswers[cpId] ?? '';
                                        const feedback = g8ExpScaffoldCheckpointFeedback[cpId];
                                        const isDone = g8ExpScaffoldCheckpointIndex >= cps.length;

                                        return (
                                            <div>
                                                {Array.isArray(g8ExpScaffoldQuestion.steps) && (
                                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                            {g8ExpScaffoldQuestion.steps.map((s, idx) => (
                                                                <li
                                                                    key={`${idx}_${s}`}
                                                                    className={idx === Math.min(g8ExpScaffoldCheckpointIndex, g8ExpScaffoldQuestion.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}
                                                                >
                                                                    {formatExponentCarets(s)}
                                                                </li>
                                                            ))}
                                                        </ol>
                                                    </div>
                                                )}

                                                {!isDone && cp && (
                                                    <div className="bg-white border border-gray-200 rounded-lg p-4">
                                                        <div className="text-sm font-semibold text-gray-800 mb-2">Checkpoint {g8ExpScaffoldCheckpointIndex + 1} / {cps.length}</div>
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
                                                                            onChange={(e) => setG8ExpScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
                                                                        />
                                                                        <span className="text-gray-800">{formatExponentCarets(opt)}</span>
                                                                    </label>
                                                                ))}
                                                            </div>
                                                        ) : (
                                                            <input
                                                                type="text"
                                                                value={answerValue}
                                                                onChange={(e) => setG8ExpScaffoldCheckpointAnswers((prev) => ({ ...prev, [cpId]: e.target.value }))}
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
                                                                            || normalizeExponentAnswer(user) === normalizeExponentAnswer(correct)
                                                                        );

                                                                    setG8ExpScaffoldCheckpointFeedback((prev) => ({
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
                                                                onClick={() => setG8ExpScaffoldShowHint((p) => !p)}
                                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                                            >
                                                                {g8ExpScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                                            </button>
                                                            <button
                                                                onClick={() => {
                                                                    const ok = !!g8ExpScaffoldCheckpointFeedback[cpId]?.isCorrect;
                                                                    if (!ok) return;
                                                                    setG8ExpScaffoldCheckpointIndex((prev) => prev + 1);
                                                                    setG8ExpScaffoldShowHint(false);
                                                                }}
                                                                disabled={!g8ExpScaffoldCheckpointFeedback[cpId]?.isCorrect}
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

                                                        {g8ExpScaffoldShowHint && (feedback?.explanation || cp?.explanation) && (
                                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                                {feedback?.explanation || cp?.explanation}
                                                            </div>
                                                        )}
                                                    </div>
                                                )}

                                                {g8ExpScaffoldCheckpointIndex >= cps.length && (
                                                    <div className="mt-4 p-4 bg-green-50 border border-green-200 rounded-lg text-green-900">
                                                        <div className="font-semibold">All checkpoints completed.</div>
                                                        <div className="mt-1 text-sm">Final answer: <span className="font-semibold">{formatExponentCarets(g8ExpScaffoldQuestion.correct_answer)}</span></div>
                                                    </div>
                                                )}
                                            </div>
                                        );
                                    })()
                                ) : (
                                    <>
                                        <input
                                            type="text"
                                            value={g8ExpScaffoldAnswer}
                                            onChange={(e) => setG8ExpScaffoldAnswer(e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Type your answer"
                                        />

                                        <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={() => {
                                                    const user = String(g8ExpScaffoldAnswer);
                                                    const correct = String(g8ExpScaffoldQuestion.correct_answer ?? '');
                                                    const ok = (
                                                        normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                        || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase()
                                                        || normalizeExponentAnswer(user) === normalizeExponentAnswer(correct)
                                                    );
                                                    setG8ExpScaffoldFeedback({
                                                        isCorrect: ok,
                                                        correctAnswer: g8ExpScaffoldQuestion.correct_answer,
                                                        explanation: g8ExpScaffoldQuestion.explanation
                                                    });
                                                }}
                                                disabled={String(g8ExpScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check Answer
                                            </button>
                                            <button
                                                onClick={() => setG8ExpScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                            >
                                                {g8ExpScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                        </div>

                                        {g8ExpScaffoldFeedback && (
                                            <div className={`mt-4 p-3 rounded-lg text-sm border ${g8ExpScaffoldFeedback.isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
                                                <div className="font-semibold">{g8ExpScaffoldFeedback.isCorrect ? 'Correct' : 'Not quite'}</div>
                                                <div className="mt-1"><span className="font-semibold">Correct answer:</span> {formatExponentCarets(g8ExpScaffoldFeedback.correctAnswer)}</div>
                                            </div>
                                        )}

                                        {g8ExpScaffoldShowHint && g8ExpScaffoldFeedback?.explanation && (
                                            <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                {g8ExpScaffoldFeedback.explanation}
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

                <VisualAidsPanel isOpen={g8ExpVisualAidsOpen} setIsOpen={setG8ExpVisualAidsOpen}>
                    {renderGrade8ExponentsVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade8ExponentsScaffold;
