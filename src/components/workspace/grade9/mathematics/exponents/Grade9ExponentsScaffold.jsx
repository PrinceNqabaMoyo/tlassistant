import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

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

const normalizeExpAnswer = (value) => {
    return String(value ?? '').trim().replace(/\s+/g, '');
};

const Grade9ExponentsScaffold = ({
    onBack,
    scaffoldSteps,
    g9ExpVisualAidsOpen,
    setG9ExpVisualAidsOpen,
    g9ExpScaffoldDifficulty,
    setG9ExpScaffoldDifficulty,
    g9ExpScaffoldStepIndex,
    setG9ExpScaffoldStepIndex,
    fetchGrade9ExponentsScaffoldQuestion,
    g9ExpScaffoldLoading,
    g9ExpScaffoldError,
    g9ExpScaffoldQuestion,
    g9ExpScaffoldShowHint,
    setG9ExpScaffoldShowHint,
    g9ExpScaffoldAnswer,
    setG9ExpScaffoldAnswer,
    g9ExpScaffoldFeedback,
    setG9ExpScaffoldFeedback,
    g9ExpScaffoldCheckpointIndex,
    setG9ExpScaffoldCheckpointIndex,
    g9ExpScaffoldCheckpointAnswers,
    setG9ExpScaffoldCheckpointAnswers,
    g9ExpScaffoldCheckpointFeedback,
    setG9ExpScaffoldCheckpointFeedback,
    renderGrade9ExponentsVisualAids,
}) => {
    const currentStep = scaffoldSteps?.[g9ExpScaffoldStepIndex] || scaffoldSteps?.[0];
    const question = g9ExpScaffoldQuestion;

    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g9ExpScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];

    const requestNew = () => {
        if (!currentStep) return;
        fetchGrade9ExponentsScaffoldQuestion({ subskill: currentStep.key, difficulty: g9ExpScaffoldDifficulty });
    };

    const checkAnswer = () => {
        if (!question) return;
        const expected = normalizeExpAnswer(question.correct_answer);
        const got = normalizeExpAnswer(g9ExpScaffoldAnswer);
        if (expected && got === expected) {
            setG9ExpScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG9ExpScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!currentCheckpoint) return;

        const answers = { ...(g9ExpScaffoldCheckpointAnswers || {}) };
        const feedback = { ...(g9ExpScaffoldCheckpointFeedback || {}) };

        const userValue = answers[currentCheckpoint.id] ?? '';
        const expected = normalizeExpAnswer(currentCheckpoint.correct_answer);
        const got = normalizeExpAnswer(userValue);

        if (expected && got === expected) {
            feedback[currentCheckpoint.id] = { kind: 'success', message: 'Correct.' };
        } else {
            feedback[currentCheckpoint.id] = { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` };
        }

        setG9ExpScaffoldCheckpointFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Exponents • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step method practice with checkpoints. No calculator.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g9ExpVisualAidsOpen && (
                                <button
                                    onClick={() => setG9ExpVisualAidsOpen(true)}
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
                                value={g9ExpScaffoldDifficulty}
                                onChange={(e) => setG9ExpScaffoldDifficulty(e.target.value)}
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
                                value={g9ExpScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG9ExpScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG9ExpScaffoldFeedback(null);
                                    setG9ExpScaffoldShowHint(false);
                                    setG9ExpScaffoldCheckpointIndex(0);
                                    setG9ExpScaffoldCheckpointAnswers({});
                                    setG9ExpScaffoldCheckpointFeedback({});
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {(scaffoldSteps || []).map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>
                    </div>

                    {g9ExpScaffoldError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g9ExpScaffoldError}</div>
                    )}

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <h3 className="text-lg font-bold text-gray-900">Question</h3>
                            <div className="flex gap-2">
                                <button
                                    onClick={requestNew}
                                    className="px-3 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold"
                                    disabled={g9ExpScaffoldLoading}
                                >
                                    New Question
                                </button>
                                <button
                                    onClick={() => setG9ExpScaffoldShowHint((p) => !p)}
                                    className="px-3 py-2 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-800 text-sm font-semibold"
                                    disabled={!question}
                                >
                                    {g9ExpScaffoldShowHint ? 'Hide hint' : 'Show hint'}
                                </button>
                            </div>
                        </div>

                        <div className="p-4 border border-gray-200 rounded-lg bg-gray-50">
                            {g9ExpScaffoldLoading && <div className="text-sm text-gray-600">Loading…</div>}
                            {!g9ExpScaffoldLoading && question && (
                                <div className="text-gray-900 whitespace-pre-wrap">{renderMathText(question.question)}</div>
                            )}
                            {!g9ExpScaffoldLoading && !question && (
                                <div className="text-sm text-gray-600">Select a subskill and click “New Question”.</div>
                            )}
                        </div>

                        {question?.table && (
                            <div className="mt-3 p-4 border border-gray-200 rounded-lg bg-white">
                                <div className="text-sm font-semibold text-gray-800 mb-2">Exponent laws (reference)</div>
                                <TableRenderer table={question.table} />
                            </div>
                        )}

                        {g9ExpScaffoldShowHint && question?.explanation && (
                            <div className="mt-3 p-3 bg-indigo-50 border border-indigo-200 rounded-lg text-indigo-900 text-sm whitespace-pre-wrap">{question.explanation}</div>
                        )}
                    </div>

                    {question?.question_type === 'scaffold' && checkpoints.length > 0 && (
                        <div className="mb-6">
                            <div className="flex items-center justify-between mb-2">
                                <h3 className="text-lg font-bold text-gray-900">Checkpoints</h3>
                                <div className="text-sm text-gray-600">{cpIndex + 1} / {checkpoints.length}</div>
                            </div>

                            {Array.isArray(question?.steps) && (
                                <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                    <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                    <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                        {question.steps.map((s, idx) => (
                                            <li
                                                key={`${idx}_${s}`}
                                                className={idx === Math.min(cpIndex, question.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}
                                            >
                                                {renderMathText(s)}
                                            </li>
                                        ))}
                                    </ol>
                                </div>
                            )}

                            <div className="p-4 border border-gray-200 rounded-lg bg-white">
                                <div className="font-semibold text-gray-900 mb-2">{renderMathText(currentCheckpoint?.prompt)}</div>

                                <div className="flex flex-col sm:flex-row gap-2">
                                    <input
                                        type="text"
                                        value={(g9ExpScaffoldCheckpointAnswers || {})[currentCheckpoint?.id] || ''}
                                        onChange={(e) => {
                                            const next = { ...(g9ExpScaffoldCheckpointAnswers || {}) };
                                            next[currentCheckpoint.id] = e.target.value;
                                            setG9ExpScaffoldCheckpointAnswers(next);
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

                                {g9ExpScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                    <div className={`mt-3 p-3 rounded-lg text-sm ${g9ExpScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                        {renderMathText(g9ExpScaffoldCheckpointFeedback[currentCheckpoint.id].message)}
                                    </div>
                                )}

                                <div className="mt-4 flex items-center justify-between">
                                    <button
                                        onClick={() => setG9ExpScaffoldCheckpointIndex(Math.max(0, cpIndex - 1))}
                                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                        disabled={cpIndex === 0}
                                    >
                                        Previous
                                    </button>
                                    <button
                                        onClick={() => setG9ExpScaffoldCheckpointIndex(Math.min(cpIndex + 1, checkpoints.length - 1))}
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
                                    value={g9ExpScaffoldAnswer}
                                    onChange={(e) => setG9ExpScaffoldAnswer(e.target.value)}
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

                    {g9ExpScaffoldFeedback && (
                        <div className={`mb-6 p-3 rounded-lg text-sm ${g9ExpScaffoldFeedback.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                            {renderMathText(g9ExpScaffoldFeedback.message)}
                        </div>
                    )}
                </div>

                {g9ExpVisualAidsOpen && (
                    <VisualAidsPanel onClose={() => setG9ExpVisualAidsOpen(false)}>
                        {renderGrade9ExponentsVisualAids?.()}
                    </VisualAidsPanel>
                )}
            </div>
        </div>
    );
};

export default Grade9ExponentsScaffold;
