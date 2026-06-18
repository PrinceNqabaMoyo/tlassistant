import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

const normalizeEqIneq = (value) => {
    if (value === null || value === undefined) return '';
    return String(value)
        .trim()
        .replace(/−/g, '-')
        .replace(/≤/g, '<=')
        .replace(/≥/g, '>=')
        .replace(/\s+/g, '')
        .toLowerCase();
};

const Grade10EquationsInequalitiesScaffold = ({
    onBack,
    scaffoldSteps,
    g10EqIneqVisualAidsOpen,
    setG10EqIneqVisualAidsOpen,
    g10EqIneqScaffoldDifficulty,
    setG10EqIneqScaffoldDifficulty,
    g10EqIneqScaffoldStepIndex,
    setG10EqIneqScaffoldStepIndex,
    fetchGrade10EqIneqScaffoldQuestion,
    g10EqIneqScaffoldLoading,
    g10EqIneqScaffoldError,
    g10EqIneqScaffoldQuestion,
    g10EqIneqScaffoldCheckpointIndex,
    setG10EqIneqScaffoldCheckpointIndex,
    g10EqIneqScaffoldCheckpointAnswers,
    setG10EqIneqScaffoldCheckpointAnswers,
    g10EqIneqScaffoldCheckpointFeedback,
    setG10EqIneqScaffoldCheckpointFeedback,
    g10EqIneqScaffoldAnswer,
    setG10EqIneqScaffoldAnswer,
    g10EqIneqScaffoldFeedback,
    setG10EqIneqScaffoldFeedback,
    g10EqIneqScaffoldShowHint,
    setG10EqIneqScaffoldShowHint,
    renderGrade10EqIneqVisualAids,
}) => {
    const question = g10EqIneqScaffoldQuestion;
    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g10EqIneqScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];

    const checkAnswer = () => {
        if (!question) return;
        const expected = normalizeEqIneq(question.correct_answer);
        const got = normalizeEqIneq(g10EqIneqScaffoldAnswer);

        if (expected && got === expected) {
            setG10EqIneqScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG10EqIneqScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!question || !currentCheckpoint) return;

        const cpId = currentCheckpoint.id;
        const userValue = g10EqIneqScaffoldCheckpointAnswers?.[cpId] ?? '';
        const expected = normalizeEqIneq(currentCheckpoint.correct_answer);
        const got = normalizeEqIneq(userValue);

        const ok = expected && got === expected;

        setG10EqIneqScaffoldCheckpointFeedback((prev) => ({
            ...(prev || {}),
            [cpId]: ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` },
        }));
    };

    const goNextCheckpoint = () => {
        if (!question || !currentCheckpoint) return;
        const cpId = currentCheckpoint.id;
        const fb = g10EqIneqScaffoldCheckpointFeedback?.[cpId];
        if (!fb || fb.kind !== 'success') return;

        if (cpIndex >= checkpoints.length - 1) {
            setG10EqIneqScaffoldCheckpointIndex(checkpoints.length);
        } else {
            setG10EqIneqScaffoldCheckpointIndex(cpIndex + 1);
        }
    };

    const setCheckpointAnswer = (cpId, value) => {
        setG10EqIneqScaffoldCheckpointAnswers((prev) => ({ ...(prev || {}), [cpId]: value }));
        setG10EqIneqScaffoldCheckpointFeedback((prev) => ({ ...(prev || {}), [cpId]: null }));
    };

    const newExample = () => {
        const step = scaffoldSteps[g10EqIneqScaffoldStepIndex] || scaffoldSteps[0];
        fetchGrade10EqIneqScaffoldQuestion({ subskill: step.key, difficulty: g10EqIneqScaffoldDifficulty });
    };

    const isDone = question?.question_type === 'scaffold' && checkpoints.length > 0
        ? (Number(g10EqIneqScaffoldCheckpointIndex) || 0) >= checkpoints.length
        : false;

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 10 Mathematics • Equations &amp; inequalities • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g10EqIneqVisualAidsOpen && (
                                <button
                                    onClick={() => setG10EqIneqVisualAidsOpen(true)}
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
                                value={g10EqIneqScaffoldDifficulty}
                                onChange={(e) => setG10EqIneqScaffoldDifficulty(e.target.value)}
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
                                value={g10EqIneqScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG10EqIneqScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG10EqIneqScaffoldFeedback(null);
                                    setG10EqIneqScaffoldShowHint(false);
                                    setG10EqIneqScaffoldCheckpointIndex(0);
                                    setG10EqIneqScaffoldCheckpointAnswers({});
                                    setG10EqIneqScaffoldCheckpointFeedback({});
                                    setG10EqIneqScaffoldAnswer('');
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
                                onClick={newExample}
                                disabled={g10EqIneqScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g10EqIneqScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    {g10EqIneqScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">{g10EqIneqScaffoldError}</div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g10EqIneqScaffoldLoading && !question ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : question ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{renderMathText(question.question)}</div>

                                {question.question_type === 'scaffold' && checkpoints.length > 0 ? (
                                    isDone ? (
                                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                                            <div className="text-gray-900 font-semibold">Finished</div>
                                            {question.explanation && (
                                                <div className="mt-3 text-sm text-gray-700 bg-gray-50 border border-gray-200 rounded-lg p-3">
                                                    {renderMathText(question.explanation)}
                                                </div>
                                            )}
                                        </div>
                                    ) : (
                                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                                            <div className="text-sm font-semibold text-gray-800 mb-2">Checkpoint {cpIndex + 1} / {checkpoints.length}</div>
                                            <div className="text-gray-800 font-medium mb-3">{renderMathText(currentCheckpoint?.prompt || '')}</div>

                                            <input
                                                type="text"
                                                value={g10EqIneqScaffoldCheckpointAnswers?.[currentCheckpoint?.id] ?? ''}
                                                onChange={(e) => setCheckpointAnswer(currentCheckpoint?.id, e.target.value)}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />

                                            <div className="mt-3 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                <button
                                                    onClick={checkCheckpoint}
                                                    disabled={String(g10EqIneqScaffoldCheckpointAnswers?.[currentCheckpoint?.id] ?? '').trim() === ''}
                                                    className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                                >
                                                    Check
                                                </button>
                                                <button
                                                    onClick={goNextCheckpoint}
                                                    className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700"
                                                >
                                                    Next
                                                </button>
                                            </div>

                                            {currentCheckpoint?.id && g10EqIneqScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                                <div className={`mt-3 p-3 rounded-lg text-sm ${g10EqIneqScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                                    {renderMathText(g10EqIneqScaffoldCheckpointFeedback[currentCheckpoint.id].message)}
                                                </div>
                                            )}
                                        </div>
                                    )
                                ) : (
                                    <>
                                        <div className="mb-3">
                                            <label className="block text-sm font-semibold text-gray-700 mb-1">Your answer</label>
                                            <input
                                                type="text"
                                                value={g10EqIneqScaffoldAnswer}
                                                onChange={(e) => {
                                                    setG10EqIneqScaffoldAnswer(e.target.value);
                                                    setG10EqIneqScaffoldFeedback(null);
                                                }}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        </div>

                                        <div className="flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={checkAnswer}
                                                disabled={String(g10EqIneqScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG10EqIneqScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-indigo-50 text-indigo-800 rounded-lg font-semibold border border-indigo-200 hover:bg-indigo-100"
                                            >
                                                {g10EqIneqScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                        </div>

                                        {g10EqIneqScaffoldFeedback && (
                                            <div className={`mt-4 p-4 rounded-lg border ${g10EqIneqScaffoldFeedback.kind === 'success' ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                                                {renderMathText(g10EqIneqScaffoldFeedback.message)}
                                            </div>
                                        )}

                                        {g10EqIneqScaffoldShowHint && question.explanation && (
                                            <div className="mt-3 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                {renderMathText(question.explanation)}
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

                <VisualAidsPanel isOpen={g10EqIneqVisualAidsOpen} setIsOpen={setG10EqIneqVisualAidsOpen}>
                    {renderGrade10EqIneqVisualAids?.()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade10EquationsInequalitiesScaffold;
