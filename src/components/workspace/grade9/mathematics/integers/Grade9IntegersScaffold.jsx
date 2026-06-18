import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const TableRenderer = ({ table }) => {
    if (!table || !Array.isArray(table.headers) || !Array.isArray(table.rows)) return null;
    return (
        <div className="overflow-x-auto">
            <table className="min-w-full border border-gray-200 rounded-lg overflow-hidden">
                <thead className="bg-gray-50">
                    <tr>
                        {table.headers.map((h, idx) => (
                            <th key={idx} className="px-3 py-2 text-left text-xs font-semibold text-gray-700 border-b border-gray-200">
                                {h}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {table.rows.map((row, rIdx) => (
                        <tr key={rIdx} className={rIdx % 2 === 0 ? 'bg-white' : 'bg-gray-50'}>
                            {row.map((cell, cIdx) => (
                                <td key={cIdx} className="px-3 py-2 text-sm text-gray-800 border-b border-gray-200 align-top">
                                    {String(cell ?? '')}
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

const Grade9IntegersScaffold = ({
    onBack,
    scaffoldSteps,
    g9IntVisualAidsOpen,
    setG9IntVisualAidsOpen,
    g9IntScaffoldDifficulty,
    setG9IntScaffoldDifficulty,
    g9IntScaffoldStepIndex,
    setG9IntScaffoldStepIndex,
    fetchGrade9IntegersScaffoldQuestion,
    g9IntScaffoldLoading,
    g9IntScaffoldError,
    g9IntScaffoldQuestion,
    g9IntScaffoldShowHint,
    setG9IntScaffoldShowHint,
    g9IntScaffoldAnswer,
    setG9IntScaffoldAnswer,
    g9IntScaffoldFeedback,
    setG9IntScaffoldFeedback,
    g9IntScaffoldCheckpointIndex,
    setG9IntScaffoldCheckpointIndex,
    g9IntScaffoldCheckpointAnswers,
    setG9IntScaffoldCheckpointAnswers,
    g9IntScaffoldCheckpointFeedback,
    setG9IntScaffoldCheckpointFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade9IntegersVisualAids,
}) => {
    const currentStep = scaffoldSteps?.[g9IntScaffoldStepIndex] || scaffoldSteps?.[0];
    const question = g9IntScaffoldQuestion;

    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g9IntScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];

    const getNormalizerFor = (rawAnswer) => {
        const s = String(rawAnswer ?? '').trim();
        if (!s) return normalizeTextAnswer;
        if (/^[-+]?\d+$/.test(s)) return normalizeWholeNumberAnswer;
        return normalizeTextAnswer;
    };

    const requestNew = () => {
        if (!currentStep) return;
        fetchGrade9IntegersScaffoldQuestion({ subskill: currentStep.key, difficulty: g9IntScaffoldDifficulty });
    };

    const checkAnswer = () => {
        if (!question) return;
        const normalize = getNormalizerFor(question.correct_answer);
        const expected = normalize(question.correct_answer);
        const got = normalize(g9IntScaffoldAnswer);
        if (expected && got === expected) {
            setG9IntScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG9IntScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!currentCheckpoint) return;

        const answers = { ...(g9IntScaffoldCheckpointAnswers || {}) };
        const feedback = { ...(g9IntScaffoldCheckpointFeedback || {}) };

        const userValue = answers[currentCheckpoint.id] ?? '';
        const normalize = getNormalizerFor(currentCheckpoint.correct_answer);
        const expected = normalize(currentCheckpoint.correct_answer);
        const got = normalize(userValue);

        if (expected && got === expected) {
            feedback[currentCheckpoint.id] = { kind: 'success', message: 'Correct.' };
        } else {
            feedback[currentCheckpoint.id] = { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` };
        }

        setG9IntScaffoldCheckpointFeedback(feedback);
    };

    const setCheckpointAnswer = (checkpointId, value) => {
        const answers = { ...(g9IntScaffoldCheckpointAnswers || {}) };
        answers[checkpointId] = value;
        setG9IntScaffoldCheckpointAnswers(answers);

        const feedback = { ...(g9IntScaffoldCheckpointFeedback || {}) };
        feedback[checkpointId] = null;
        setG9IntScaffoldCheckpointFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Integers • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g9IntVisualAidsOpen && (
                                <button
                                    onClick={() => setG9IntVisualAidsOpen(true)}
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
                                value={g9IntScaffoldDifficulty}
                                onChange={(e) => setG9IntScaffoldDifficulty(e.target.value)}
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
                                value={g9IntScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG9IntScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG9IntScaffoldFeedback(null);
                                    setG9IntScaffoldShowHint(false);
                                    setG9IntScaffoldCheckpointIndex(0);
                                    setG9IntScaffoldCheckpointAnswers({});
                                    setG9IntScaffoldCheckpointFeedback({});
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {(scaffoldSteps || []).map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>
                    </div>

                    <div className="flex items-center gap-2 mb-4">
                        <button
                            onClick={requestNew}
                            className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-semibold"
                            disabled={g9IntScaffoldLoading}
                        >
                            New Question
                        </button>
                        <button
                            onClick={() => setG9IntScaffoldShowHint(!g9IntScaffoldShowHint)}
                            className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                            disabled={!question}
                        >
                            {g9IntScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                        </button>
                        {g9IntScaffoldLoading && <div className="text-sm text-gray-600">Loading…</div>}
                    </div>

                    {g9IntScaffoldError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g9IntScaffoldError}</div>
                    )}

                    {!question && !g9IntScaffoldLoading && (
                        <div className="text-sm text-gray-600">Select a step and click “New Question”.</div>
                    )}

                    {question && (
                        <div className="border border-gray-200 rounded-lg p-4 bg-white">
                            <div className="font-semibold text-gray-900 mb-2">{question.question}</div>

                            {question.table && (
                                <div className="mb-3 p-3 border border-gray-200 rounded-lg bg-gray-50">
                                    <div className="text-sm font-semibold text-gray-800 mb-2">Reference table</div>
                                    <TableRenderer table={question.table} />
                                </div>
                            )}

                            {g9IntScaffoldShowHint && question.steps && (
                                <div className="mb-3 p-3 border border-indigo-200 rounded-lg bg-indigo-50">
                                    <div className="text-sm font-semibold text-indigo-800 mb-2">Steps</div>
                                    <ol className="list-decimal pl-5 text-sm text-indigo-900 space-y-1">
                                        {(question.steps || []).map((s, idx) => (
                                            <li key={idx}>{s}</li>
                                        ))}
                                    </ol>
                                </div>
                            )}

                            {checkpoints.length > 0 && (
                                <div className="mb-4 p-3 border border-gray-200 rounded-lg bg-gray-50">
                                    <div className="flex items-center justify-between gap-2 mb-3">
                                        <div className="text-sm font-semibold text-gray-800">Checkpoint {cpIndex + 1} of {checkpoints.length}</div>
                                        <div className="flex items-center gap-2">
                                            <button
                                                onClick={() => setG9IntScaffoldCheckpointIndex(Math.max(0, cpIndex - 1))}
                                                className="px-3 py-1 bg-white border border-gray-300 rounded-md text-sm font-semibold hover:bg-gray-50"
                                                disabled={cpIndex === 0}
                                            >
                                                Prev
                                            </button>
                                            <button
                                                onClick={() => setG9IntScaffoldCheckpointIndex(Math.min(checkpoints.length - 1, cpIndex + 1))}
                                                className="px-3 py-1 bg-white border border-gray-300 rounded-md text-sm font-semibold hover:bg-gray-50"
                                                disabled={cpIndex === checkpoints.length - 1}
                                            >
                                                Next
                                            </button>
                                        </div>
                                    </div>

                                    {currentCheckpoint && (
                                        <div>
                                            <div className="text-sm text-gray-800 mb-2">{currentCheckpoint.prompt}</div>
                                            <div className="flex flex-col sm:flex-row gap-2">
                                                <input
                                                    type="text"
                                                    value={g9IntScaffoldCheckpointAnswers?.[currentCheckpoint.id] ?? ''}
                                                    onChange={(e) => setCheckpointAnswer(currentCheckpoint.id, e.target.value)}
                                                    className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                                    placeholder="Your answer"
                                                />
                                                <button
                                                    onClick={checkCheckpoint}
                                                    className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                                >
                                                    Check
                                                </button>
                                            </div>

                                            {g9IntScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                                <div className={`mt-3 p-3 rounded-lg text-sm ${g9IntScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                                    {g9IntScaffoldCheckpointFeedback[currentCheckpoint.id].message}
                                                </div>
                                            )}
                                        </div>
                                    )}
                                </div>
                            )}

                            <div className="flex flex-col sm:flex-row gap-2">
                                <input
                                    type="text"
                                    value={g9IntScaffoldAnswer}
                                    onChange={(e) => {
                                        setG9IntScaffoldAnswer(e.target.value);
                                        setG9IntScaffoldFeedback(null);
                                    }}
                                    className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                    placeholder="Final answer"
                                />
                                <button
                                    onClick={checkAnswer}
                                    className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                >
                                    Check Final
                                </button>
                            </div>

                            {g9IntScaffoldFeedback && (
                                <div className={`mt-3 p-3 rounded-lg text-sm ${g9IntScaffoldFeedback.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                    {g9IntScaffoldFeedback.message}
                                </div>
                            )}

                            {question.explanation && (
                                <details className="mt-3">
                                    <summary className="cursor-pointer text-sm font-semibold text-indigo-700">Show explanation</summary>
                                    <div className="mt-2 text-sm text-gray-700 whitespace-pre-wrap">{question.explanation}</div>
                                </details>
                            )}
                        </div>
                    )}
                </div>

                {g9IntVisualAidsOpen && (
                    <VisualAidsPanel onClose={() => setG9IntVisualAidsOpen(false)}>
                        {renderGrade9IntegersVisualAids?.()}
                    </VisualAidsPanel>
                )}
            </div>
        </div>
    );
};

export default Grade9IntegersScaffold;
