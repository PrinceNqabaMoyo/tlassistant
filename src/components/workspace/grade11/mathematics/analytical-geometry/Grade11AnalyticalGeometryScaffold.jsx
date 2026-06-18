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

const Grade11AnalyticalGeometryScaffold = ({
    onBack,
    scaffoldSteps,
    g11AnalGeoVisualAidsOpen,
    setG11AnalGeoVisualAidsOpen,
    g11AnalGeoScaffoldDifficulty,
    setG11AnalGeoScaffoldDifficulty,
    g11AnalGeoScaffoldStepIndex,
    setG11AnalGeoScaffoldStepIndex,
    fetchGrade11AnalGeoScaffoldQuestion,
    g11AnalGeoScaffoldLoading,
    g11AnalGeoScaffoldError,
    g11AnalGeoScaffoldQuestion,
    g11AnalGeoScaffoldCheckpointIndex,
    setG11AnalGeoScaffoldCheckpointIndex,
    g11AnalGeoScaffoldCheckpointAnswers,
    setG11AnalGeoScaffoldCheckpointAnswers,
    g11AnalGeoScaffoldCheckpointFeedback,
    setG11AnalGeoScaffoldCheckpointFeedback,
    g11AnalGeoScaffoldAnswer,
    setG11AnalGeoScaffoldAnswer,
    g11AnalGeoScaffoldFeedback,
    setG11AnalGeoScaffoldFeedback,
    g11AnalGeoScaffoldShowHint,
    setG11AnalGeoScaffoldShowHint,
    renderGrade11AnalGeoVisualAids,
}) => {
    const question = g11AnalGeoScaffoldQuestion;
    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g11AnalGeoScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];
    const cpDone = checkpoints.length > 0 && (Number(g11AnalGeoScaffoldCheckpointIndex) || 0) >= checkpoints.length;

    const step = scaffoldSteps?.[g11AnalGeoScaffoldStepIndex] || scaffoldSteps?.[0];

    const newExample = () => {
        if (!step?.key) return;
        setG11AnalGeoScaffoldFeedback(null);
        setG11AnalGeoScaffoldShowHint(false);
        setG11AnalGeoScaffoldCheckpointIndex(0);
        setG11AnalGeoScaffoldCheckpointAnswers({});
        setG11AnalGeoScaffoldCheckpointFeedback({});
        setG11AnalGeoScaffoldAnswer('');
        fetchGrade11AnalGeoScaffoldQuestion({ subskill: step.key, difficulty: g11AnalGeoScaffoldDifficulty });
    };

    const setCheckpointAnswer = (cpId, value) => {
        setG11AnalGeoScaffoldCheckpointAnswers((prev) => ({ ...(prev || {}), [cpId]: value }));
        setG11AnalGeoScaffoldCheckpointFeedback((prev) => ({ ...(prev || {}), [cpId]: null }));
    };

    const checkCheckpoint = () => {
        if (!question || !currentCheckpoint) return;
        const cpId = currentCheckpoint.id;
        const userValue = g11AnalGeoScaffoldCheckpointAnswers?.[cpId] ?? '';

        const expected = normalizeAnswer(currentCheckpoint.correct_answer);
        const got = normalizeAnswer(userValue);
        const ok = currentCheckpoint.kind === 'mcq'
            ? String(userValue) === String(currentCheckpoint.correct_answer ?? '')
            : (expected && got === expected);

        setG11AnalGeoScaffoldCheckpointFeedback((prev) => ({
            ...(prev || {}),
            [cpId]: ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` },
        }));

        if (ok) {
            setG11AnalGeoScaffoldCheckpointIndex((prev) => (Number(prev) || 0) + 1);
        }
    };

    const checkAnswer = () => {
        if (!question) return;
        const expected = normalizeAnswer(question.correct_answer);
        const got = normalizeAnswer(g11AnalGeoScaffoldAnswer);
        const ok = question.question_type === 'mcq'
            ? String(g11AnalGeoScaffoldAnswer) === String(question.correct_answer ?? '')
            : (expected && got === expected);
        setG11AnalGeoScaffoldFeedback(ok
            ? { kind: 'success', message: 'Correct.' }
            : { kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 11 Mathematics • Analytical Geometry • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g11AnalGeoVisualAidsOpen && (
                                <button
                                    onClick={() => setG11AnalGeoVisualAidsOpen(true)}
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
                                value={g11AnalGeoScaffoldDifficulty}
                                onChange={(e) => setG11AnalGeoScaffoldDifficulty(e.target.value)}
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
                                value={g11AnalGeoScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG11AnalGeoScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG11AnalGeoScaffoldCheckpointIndex(0);
                                    setG11AnalGeoScaffoldCheckpointAnswers({});
                                    setG11AnalGeoScaffoldCheckpointFeedback({});
                                    setG11AnalGeoScaffoldAnswer('');
                                    setG11AnalGeoScaffoldFeedback(null);
                                    setG11AnalGeoScaffoldShowHint(false);
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {(scaffoldSteps || []).map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={newExample}
                                disabled={g11AnalGeoScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g11AnalGeoScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    {g11AnalGeoScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">{g11AnalGeoScaffoldError}</div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g11AnalGeoScaffoldLoading && !question ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : question ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{renderMathText(question.question)}</div>

                                {question.question_type === 'scaffold' && checkpoints.length > 0 ? (
                                    cpDone ? (
                                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                                            <div className="text-gray-900 font-semibold mb-2">Finished</div>
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

                                            {currentCheckpoint?.kind === 'mcq' && Array.isArray(currentCheckpoint.options) ? (
                                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                                    {currentCheckpoint.options.map((opt) => (
                                                        <label key={opt} className="flex items-center gap-2 p-3 bg-gray-50 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100">
                                                            <input
                                                                type="radio"
                                                                name={currentCheckpoint.id}
                                                                value={opt}
                                                                checked={(g11AnalGeoScaffoldCheckpointAnswers?.[currentCheckpoint.id] ?? '') === opt}
                                                                onChange={(e) => setCheckpointAnswer(currentCheckpoint.id, e.target.value)}
                                                            />
                                                            <span className="text-gray-800">{renderMathText(opt)}</span>
                                                        </label>
                                                    ))}
                                                </div>
                                            ) : (
                                                <input
                                                    type="text"
                                                    value={g11AnalGeoScaffoldCheckpointAnswers?.[currentCheckpoint.id] ?? ''}
                                                    onChange={(e) => setCheckpointAnswer(currentCheckpoint.id, e.target.value)}
                                                    className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                    placeholder="Type your answer"
                                                />
                                            )}

                                            <div className="mt-3 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                <button
                                                    onClick={checkCheckpoint}
                                                    disabled={String(g11AnalGeoScaffoldCheckpointAnswers?.[currentCheckpoint?.id] ?? '').trim() === ''}
                                                    className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                                >
                                                    Check
                                                </button>
                                                {g11AnalGeoScaffoldCheckpointFeedback?.[currentCheckpoint?.id] && (
                                                    <div className={`text-sm ${g11AnalGeoScaffoldCheckpointFeedback[currentCheckpoint.id]?.kind === 'success' ? 'text-green-700' : 'text-red-700'}`}>
                                                        {g11AnalGeoScaffoldCheckpointFeedback[currentCheckpoint.id]?.message}
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    )
                                ) : (
                                    <div className="bg-white border border-gray-200 rounded-lg p-4">
                                        {question.question_type === 'mcq' && Array.isArray(question.options) ? (
                                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                                {question.options.map((opt) => (
                                                    <label key={opt} className="flex items-center gap-2 p-3 bg-gray-50 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100">
                                                        <input
                                                            type="radio"
                                                            name={question.id}
                                                            value={opt}
                                                            checked={String(g11AnalGeoScaffoldAnswer) === String(opt)}
                                                            onChange={(e) => {
                                                                setG11AnalGeoScaffoldAnswer(e.target.value);
                                                                setG11AnalGeoScaffoldFeedback(null);
                                                            }}
                                                        />
                                                        <span className="text-gray-800">{renderMathText(opt)}</span>
                                                    </label>
                                                ))}
                                            </div>
                                        ) : (
                                            <input
                                                type="text"
                                                value={g11AnalGeoScaffoldAnswer}
                                                onChange={(e) => {
                                                    setG11AnalGeoScaffoldAnswer(e.target.value);
                                                    setG11AnalGeoScaffoldFeedback(null);
                                                }}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        )}

                                        <div className="mt-3 flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={checkAnswer}
                                                disabled={String(g11AnalGeoScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            {g11AnalGeoScaffoldFeedback && (
                                                <div className={`text-sm ${g11AnalGeoScaffoldFeedback.kind === 'success' ? 'text-green-700' : 'text-red-700'}`}>
                                                    {g11AnalGeoScaffoldFeedback.message}
                                                </div>
                                            )}
                                        </div>

                                        {g11AnalGeoScaffoldFeedback && question.explanation && (
                                            <div className="mt-3 text-sm text-gray-700 bg-gray-50 border border-gray-200 rounded-lg p-3">
                                                {renderMathText(question.explanation)}
                                            </div>
                                        )}
                                    </div>
                                )}
                            </>
                        ) : (
                            <div className="text-gray-600">No question yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g11AnalGeoVisualAidsOpen} setIsOpen={setG11AnalGeoVisualAidsOpen}>
                    {renderGrade11AnalGeoVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade11AnalyticalGeometryScaffold;
