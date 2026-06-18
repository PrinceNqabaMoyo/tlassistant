import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const normalizeYesNo = (value) => {
    const s = String(value ?? '').trim().toLowerCase();
    if (s === 'y') return 'yes';
    if (s === 'n') return 'no';
    return s;
};

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

const Grade9WholeNumbersScaffold = ({
    onBack,
    scaffoldSteps,
    g9WholeVisualAidsOpen,
    setG9WholeVisualAidsOpen,
    g9WholeScaffoldDifficulty,
    setG9WholeScaffoldDifficulty,
    g9WholeScaffoldStepIndex,
    setG9WholeScaffoldStepIndex,
    fetchGrade9WholeNumbersScaffoldQuestion,
    g9WholeScaffoldLoading,
    g9WholeScaffoldError,
    g9WholeScaffoldQuestion,
    g9WholeScaffoldShowHint,
    setG9WholeScaffoldShowHint,
    g9WholeScaffoldAnswer,
    setG9WholeScaffoldAnswer,
    g9WholeScaffoldFeedback,
    setG9WholeScaffoldFeedback,
    g9WholeScaffoldCheckpointIndex,
    setG9WholeScaffoldCheckpointIndex,
    g9WholeScaffoldCheckpointAnswers,
    setG9WholeScaffoldCheckpointAnswers,
    g9WholeScaffoldCheckpointFeedback,
    setG9WholeScaffoldCheckpointFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade9WholeNumbersVisualAids,
}) => {
    const currentStep = scaffoldSteps?.[g9WholeScaffoldStepIndex] || scaffoldSteps?.[0];
    const question = g9WholeScaffoldQuestion;

    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g9WholeScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];

    const getNormalizerFor = (rawAnswer) => {
        const s = String(rawAnswer ?? '').trim();
        if (!s) return normalizeTextAnswer;
        if (/^[-+]?\d+$/.test(s)) return normalizeWholeNumberAnswer;
        if (/^(yes|no)$/i.test(s)) return (v) => normalizeYesNo(normalizeTextAnswer(v));
        return normalizeTextAnswer;
    };

    const requestNew = () => {
        if (!currentStep) return;
        fetchGrade9WholeNumbersScaffoldQuestion({ subskill: currentStep.key, difficulty: g9WholeScaffoldDifficulty });
    };

    const checkAnswer = () => {
        if (!question) return;
        const normalize = getNormalizerFor(question.correct_answer);
        const expected = normalize(question.correct_answer);
        const got = normalize(g9WholeScaffoldAnswer);
        if (expected && got === expected) {
            setG9WholeScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG9WholeScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!currentCheckpoint) return;

        const answers = { ...(g9WholeScaffoldCheckpointAnswers || {}) };
        const feedback = { ...(g9WholeScaffoldCheckpointFeedback || {}) };

        const userValue = answers[currentCheckpoint.id] ?? '';
        const normalize = getNormalizerFor(currentCheckpoint.correct_answer);
        const expected = normalize(currentCheckpoint.correct_answer);
        const got = normalize(userValue);

        if (expected && got === expected) {
            feedback[currentCheckpoint.id] = { kind: 'success', message: 'Correct.' };
        } else {
            feedback[currentCheckpoint.id] = { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` };
        }

        setG9WholeScaffoldCheckpointFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Whole Numbers • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step method practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g9WholeVisualAidsOpen && (
                                <button
                                    onClick={() => setG9WholeVisualAidsOpen(true)}
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
                                value={g9WholeScaffoldDifficulty}
                                onChange={(e) => setG9WholeScaffoldDifficulty(e.target.value)}
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
                                value={g9WholeScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG9WholeScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG9WholeScaffoldFeedback(null);
                                    setG9WholeScaffoldShowHint(false);
                                    setG9WholeScaffoldCheckpointIndex(0);
                                    setG9WholeScaffoldCheckpointAnswers({});
                                    setG9WholeScaffoldCheckpointFeedback({});
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {(scaffoldSteps || []).map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>
                    </div>

                    {g9WholeScaffoldError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g9WholeScaffoldError}</div>
                    )}

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <h3 className="text-lg font-bold text-gray-900">Question</h3>
                            <div className="flex gap-2">
                                <button
                                    onClick={requestNew}
                                    className="px-3 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold"
                                    disabled={g9WholeScaffoldLoading}
                                >
                                    New Question
                                </button>
                                <button
                                    onClick={() => setG9WholeScaffoldShowHint((p) => !p)}
                                    className="px-3 py-2 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-800 text-sm font-semibold"
                                    disabled={!question}
                                >
                                    {g9WholeScaffoldShowHint ? 'Hide hint' : 'Show hint'}
                                </button>
                            </div>
                        </div>

                        <div className="p-4 border border-gray-200 rounded-lg bg-gray-50">
                            {g9WholeScaffoldLoading && <div className="text-sm text-gray-600">Loading…</div>}
                            {!g9WholeScaffoldLoading && question && (
                                <div className="text-gray-900 whitespace-pre-wrap">{question.question}</div>
                            )}
                            {!g9WholeScaffoldLoading && !question && (
                                <div className="text-sm text-gray-600">Select a subskill and click “New Question”.</div>
                            )}
                        </div>

                        {question?.table && (
                            <div className="mt-3 p-4 border border-gray-200 rounded-lg bg-white">
                                <div className="text-sm font-semibold text-gray-800 mb-2">Reference table</div>
                                <TableRenderer table={question.table} />
                            </div>
                        )}

                        {question?.long_division && (
                            <div className="mt-3 p-4 border border-gray-200 rounded-lg bg-white">
                                <div className="text-sm font-semibold text-gray-800 mb-2">Long division layout</div>
                                <pre className="font-mono text-sm whitespace-pre overflow-x-auto">{question.long_division}</pre>
                            </div>
                        )}

                        {g9WholeScaffoldShowHint && question?.explanation && (
                            <div className="mt-3 p-3 bg-indigo-50 border border-indigo-200 rounded-lg text-indigo-900 text-sm whitespace-pre-wrap">{question.explanation}</div>
                        )}
                    </div>

                    {question?.question_type === 'scaffold' && checkpoints.length > 0 && (
                        <div className="mb-6">
                            <div className="flex items-center justify-between mb-2">
                                <h3 className="text-lg font-bold text-gray-900">Checkpoints</h3>
                                <div className="text-sm text-gray-600">{cpIndex + 1} / {checkpoints.length}</div>
                            </div>

                            <div className="p-4 border border-gray-200 rounded-lg bg-white">
                                <div className="font-semibold text-gray-900 mb-2">{currentCheckpoint?.prompt}</div>

                                <div className="flex flex-col sm:flex-row gap-2">
                                    <input
                                        type="text"
                                        value={(g9WholeScaffoldCheckpointAnswers || {})[currentCheckpoint.id] ?? ''}
                                        onChange={(e) => {
                                            const next = { ...(g9WholeScaffoldCheckpointAnswers || {}) };
                                            next[currentCheckpoint.id] = e.target.value;
                                            setG9WholeScaffoldCheckpointAnswers(next);
                                        }}
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

                                {g9WholeScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                    <div className={`mt-3 p-3 rounded-lg text-sm ${g9WholeScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                        {g9WholeScaffoldCheckpointFeedback[currentCheckpoint.id].message}
                                    </div>
                                )}

                                <div className="mt-4 flex items-center justify-between">
                                    <button
                                        onClick={() => setG9WholeScaffoldCheckpointIndex(Math.max(0, cpIndex - 1))}
                                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                        disabled={cpIndex === 0}
                                    >
                                        Previous
                                    </button>
                                    <button
                                        onClick={() => setG9WholeScaffoldCheckpointIndex(Math.min(cpIndex + 1, checkpoints.length - 1))}
                                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                        disabled={cpIndex >= checkpoints.length - 1}
                                    >
                                        Next
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    {question && (
                        <div className="mb-6">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Your Answer</label>
                            <div className="flex flex-col sm:flex-row gap-2">
                                <input
                                    type="text"
                                    value={g9WholeScaffoldAnswer}
                                    onChange={(e) => setG9WholeScaffoldAnswer(e.target.value)}
                                    className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                    placeholder="Type your answer"
                                    disabled={!question}
                                />
                                <button
                                    onClick={checkAnswer}
                                    className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                    disabled={!question}
                                >
                                    Check
                                </button>
                            </div>
                        </div>
                    )}

                    {g9WholeScaffoldFeedback && (
                        <div className={`mb-6 p-3 rounded-lg text-sm ${g9WholeScaffoldFeedback.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                            {g9WholeScaffoldFeedback.message}
                        </div>
                    )}
                </div>

                {g9WholeVisualAidsOpen && (
                    <VisualAidsPanel onClose={() => setG9WholeVisualAidsOpen(false)}>
                        {renderGrade9WholeNumbersVisualAids?.()}
                    </VisualAidsPanel>
                )}
            </div>
        </div>
    );
};

export default Grade9WholeNumbersScaffold;
