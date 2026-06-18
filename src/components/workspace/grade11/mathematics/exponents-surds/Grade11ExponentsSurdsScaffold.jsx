import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

const normalizeAnswer = (value) => {
    if (value === null || value === undefined) return '';
    return String(value)
        .trim()
        .replace(/\s+/g, '')
        .replace(/−/g, '-')
        .toLowerCase();
};

const Grade11ExponentsSurdsScaffold = ({
    onBack,
    scaffoldSteps,
    g11ExpSurdsVisualAidsOpen,
    setG11ExpSurdsVisualAidsOpen,
    g11ExpSurdsScaffoldDifficulty,
    setG11ExpSurdsScaffoldDifficulty,
    g11ExpSurdsScaffoldStepIndex,
    setG11ExpSurdsScaffoldStepIndex,
    fetchGrade11ExpSurdsScaffoldQuestion,
    g11ExpSurdsScaffoldLoading,
    g11ExpSurdsScaffoldError,
    g11ExpSurdsScaffoldQuestion,
    g11ExpSurdsScaffoldCheckpointIndex,
    setG11ExpSurdsScaffoldCheckpointIndex,
    g11ExpSurdsScaffoldCheckpointAnswers,
    setG11ExpSurdsScaffoldCheckpointAnswers,
    g11ExpSurdsScaffoldCheckpointFeedback,
    setG11ExpSurdsScaffoldCheckpointFeedback,
    g11ExpSurdsScaffoldAnswer,
    setG11ExpSurdsScaffoldAnswer,
    g11ExpSurdsScaffoldFeedback,
    setG11ExpSurdsScaffoldFeedback,
    g11ExpSurdsScaffoldShowHint,
    setG11ExpSurdsScaffoldShowHint,
    renderGrade11ExpSurdsVisualAids,
}) => {
    const question = g11ExpSurdsScaffoldQuestion;
    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g11ExpSurdsScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];
    const cpDone = checkpoints.length > 0 && (Number(g11ExpSurdsScaffoldCheckpointIndex) || 0) >= checkpoints.length;

    const step = scaffoldSteps?.[g11ExpSurdsScaffoldStepIndex] || scaffoldSteps?.[0];

    const newExample = () => {
        if (!step?.key) return;
        setG11ExpSurdsScaffoldFeedback(null);
        setG11ExpSurdsScaffoldShowHint(false);
        setG11ExpSurdsScaffoldCheckpointIndex(0);
        setG11ExpSurdsScaffoldCheckpointAnswers({});
        setG11ExpSurdsScaffoldCheckpointFeedback({});
        setG11ExpSurdsScaffoldAnswer('');
        fetchGrade11ExpSurdsScaffoldQuestion({ subskill: step.key, difficulty: g11ExpSurdsScaffoldDifficulty });
    };

    const setCheckpointAnswer = (cpId, value) => {
        setG11ExpSurdsScaffoldCheckpointAnswers((prev) => ({ ...(prev || {}), [cpId]: value }));
        setG11ExpSurdsScaffoldCheckpointFeedback((prev) => ({ ...(prev || {}), [cpId]: null }));
    };

    const checkCheckpoint = () => {
        if (!question || !currentCheckpoint) return;
        const cpId = currentCheckpoint.id;
        const userValue = g11ExpSurdsScaffoldCheckpointAnswers?.[cpId] ?? '';
        const expected = normalizeAnswer(currentCheckpoint.correct_answer);
        const got = normalizeAnswer(userValue);

        const ok = expected && got === expected;
        setG11ExpSurdsScaffoldCheckpointFeedback((prev) => ({
            ...(prev || {}),
            [cpId]: ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` },
        }));
    };

    const goNextCheckpoint = () => {
        if (!question || !currentCheckpoint) return;
        const cpId = currentCheckpoint.id;
        const fb = g11ExpSurdsScaffoldCheckpointFeedback?.[cpId];
        if (!fb || fb.kind !== 'success') return;
        if (cpIndex >= checkpoints.length - 1) {
            setG11ExpSurdsScaffoldCheckpointIndex(checkpoints.length);
        } else {
            setG11ExpSurdsScaffoldCheckpointIndex(cpIndex + 1);
        }
    };

    const checkFinalAnswer = () => {
        if (!question) return;
        const expected = normalizeAnswer(question.correct_answer);
        const got = normalizeAnswer(g11ExpSurdsScaffoldAnswer);

        if (expected && got === expected) {
            setG11ExpSurdsScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG11ExpSurdsScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 11 Mathematics • Exponents and surds • Scaffold</h2>
                            <p className="text-sm text-gray-600">Work through checkpoints, then give the final answer.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g11ExpSurdsVisualAidsOpen && (
                                <button
                                    onClick={() => setG11ExpSurdsVisualAidsOpen(true)}
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

                    <div className="grid grid-cols-1 md:grid-cols-3 gap-3 mb-6">
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Difficulty</label>
                            <select
                                value={g11ExpSurdsScaffoldDifficulty}
                                onChange={(e) => setG11ExpSurdsScaffoldDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>

                        <div>
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Subskill</label>
                            <select
                                value={g11ExpSurdsScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG11ExpSurdsScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG11ExpSurdsScaffoldFeedback(null);
                                    setG11ExpSurdsScaffoldShowHint(false);
                                    setG11ExpSurdsScaffoldCheckpointIndex(0);
                                    setG11ExpSurdsScaffoldCheckpointAnswers({});
                                    setG11ExpSurdsScaffoldCheckpointFeedback({});
                                    setG11ExpSurdsScaffoldAnswer('');
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {(scaffoldSteps || []).map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>

                        <div className="flex items-end">
                            <button
                                onClick={newExample}
                                disabled={g11ExpSurdsScaffoldLoading}
                                className="w-full px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g11ExpSurdsScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    {g11ExpSurdsScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">{g11ExpSurdsScaffoldError}</div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g11ExpSurdsScaffoldLoading && !question ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : question ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-2">Question</div>
                                <div className="text-gray-800 mb-4">{renderMathText(question.question)}</div>

                                {Array.isArray(question.steps) && question.steps.length > 0 && (
                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                        <div className="text-sm font-semibold text-gray-800 mb-2">Steps</div>
                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                            {question.steps.map((s, idx) => (
                                                <li key={`${idx}_${s}`}>{renderMathText(s)}</li>
                                            ))}
                                        </ol>
                                    </div>
                                )}

                                {checkpoints.length > 0 && !cpDone && currentCheckpoint && (
                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-4">
                                        <div className="text-sm font-semibold text-gray-800 mb-2">Checkpoint {cpIndex + 1} of {checkpoints.length}</div>
                                        <div className="text-sm text-gray-700 mb-2">{renderMathText(currentCheckpoint.prompt || '')}</div>
                                        <input
                                            value={g11ExpSurdsScaffoldCheckpointAnswers?.[currentCheckpoint.id] ?? ''}
                                            onChange={(e) => setCheckpointAnswer(currentCheckpoint.id, e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md mb-2"
                                            placeholder="Type your checkpoint answer"
                                        />

                                        <div className="flex gap-2">
                                            <button
                                                onClick={checkCheckpoint}
                                                className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg font-semibold"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={goNextCheckpoint}
                                                className="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg font-semibold"
                                            >
                                                Next
                                            </button>
                                        </div>

                                        {g11ExpSurdsScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                            <div
                                                className={`mt-3 p-3 rounded-lg text-sm border ${
                                                    g11ExpSurdsScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success'
                                                        ? 'bg-emerald-50 border-emerald-200 text-emerald-800'
                                                        : 'bg-red-50 border-red-200 text-red-800'
                                                }`}
                                            >
                                                {g11ExpSurdsScaffoldCheckpointFeedback[currentCheckpoint.id].message}
                                            </div>
                                        )}
                                    </div>
                                )}

                                {checkpoints.length > 0 && cpDone && (
                                    <div className="mb-4 p-3 rounded-lg border border-emerald-200 bg-emerald-50 text-emerald-800 text-sm">
                                        All checkpoints complete. Now give the final answer.
                                    </div>
                                )}

                                <div className="bg-white border border-gray-200 rounded-lg p-4">
                                    <div className="text-sm font-semibold text-gray-800 mb-2">Final answer</div>
                                    <input
                                        value={g11ExpSurdsScaffoldAnswer}
                                        onChange={(e) => {
                                            setG11ExpSurdsScaffoldAnswer(e.target.value);
                                            setG11ExpSurdsScaffoldFeedback(null);
                                        }}
                                        className="w-full px-3 py-2 border border-gray-300 rounded-md mb-2"
                                        placeholder="Type your final answer"
                                    />
                                    <div className="flex gap-2">
                                        <button
                                            onClick={checkFinalAnswer}
                                            className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-semibold"
                                        >
                                            Check answer
                                        </button>
                                        <button
                                            onClick={() => setG11ExpSurdsScaffoldShowHint((v) => !v)}
                                            className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                        >
                                            {g11ExpSurdsScaffoldShowHint ? 'Hide hint' : 'Show hint'}
                                        </button>
                                    </div>

                                    {g11ExpSurdsScaffoldFeedback && (
                                        <div
                                            className={`mt-3 p-3 rounded-lg text-sm border ${
                                                g11ExpSurdsScaffoldFeedback.kind === 'success'
                                                    ? 'bg-emerald-50 border-emerald-200 text-emerald-800'
                                                    : 'bg-red-50 border-red-200 text-red-800'
                                            }`}
                                        >
                                            {g11ExpSurdsScaffoldFeedback.message}
                                        </div>
                                    )}

                                    {g11ExpSurdsScaffoldShowHint && question.explanation && (
                                        <div className="mt-3 p-3 rounded-lg text-sm border border-indigo-200 bg-indigo-50 text-indigo-900">
                                            {renderMathText(question.explanation)}
                                        </div>
                                    )}
                                </div>
                            </>
                        ) : (
                            <div className="text-gray-600">Choose a subskill and click New Example.</div>
                        )}
                    </div>
                </div>

                {g11ExpSurdsVisualAidsOpen && (
                    <VisualAidsPanel
                        isOpen={g11ExpSurdsVisualAidsOpen}
                        setIsOpen={setG11ExpSurdsVisualAidsOpen}
                    >
                        {renderGrade11ExpSurdsVisualAids ? renderGrade11ExpSurdsVisualAids() : null}
                    </VisualAidsPanel>
                )}
            </div>
        </div>
    );
};

export default Grade11ExponentsSurdsScaffold;
