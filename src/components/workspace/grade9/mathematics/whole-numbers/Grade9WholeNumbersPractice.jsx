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

const Grade9WholeNumbersPractice = ({
    onBack,
    g9WholeVisualAidsOpen,
    setG9WholeVisualAidsOpen,
    g9WholePracticeDifficulty,
    setG9WholePracticeDifficulty,
    fetchGrade9WholeNumbersPractice,
    g9WholePracticeLoading,
    g9WholePracticeError,
    g9WholePracticeQuestions,
    g9WholePracticeAnswers,
    setG9WholePracticeAnswers,
    g9WholePracticeFeedback,
    setG9WholePracticeFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade9WholeNumbersVisualAids,
}) => {
    const questions = Array.isArray(g9WholePracticeQuestions) ? g9WholePracticeQuestions : [];

    const getNormalizerFor = (rawAnswer) => {
        const s = String(rawAnswer ?? '').trim();
        if (!s) return normalizeTextAnswer;
        if (/^[-+]?\d+$/.test(s)) return normalizeWholeNumberAnswer;
        if (/^(yes|no)$/i.test(s)) return (v) => normalizeYesNo(normalizeTextAnswer(v));
        return normalizeTextAnswer;
    };

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g9WholePracticeAnswers) ? [...g9WholePracticeAnswers] : [];
        answers[idx] = value;
        setG9WholePracticeAnswers(answers);

        const feedback = Array.isArray(g9WholePracticeFeedback) ? [...g9WholePracticeFeedback] : [];
        feedback[idx] = null;
        setG9WholePracticeFeedback(feedback);
    };

    const checkOne = (idx) => {
        const q = questions[idx];
        if (!q) return;

        const answers = Array.isArray(g9WholePracticeAnswers) ? [...g9WholePracticeAnswers] : [];
        const feedback = Array.isArray(g9WholePracticeFeedback) ? [...g9WholePracticeFeedback] : [];

        const userValue = answers[idx] ?? '';
        const normalize = getNormalizerFor(q.correct_answer);
        const expected = normalize(q.correct_answer);
        const got = normalize(userValue);

        if (expected && got === expected) {
            feedback[idx] = { kind: 'success', message: 'Correct.' };
        } else {
            feedback[idx] = { kind: 'error', message: `Not quite. Expected: ${q.correct_answer}` };
        }

        setG9WholePracticeFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Whole Numbers • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types. CSV content renders as tables; long division renders in ASCII layout.</p>
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

                    <div className="flex flex-col sm:flex-row sm:items-end gap-3 mb-6">
                        <div className="w-full sm:w-56">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Difficulty</label>
                            <select
                                value={g9WholePracticeDifficulty}
                                onChange={(e) => setG9WholePracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>

                        <button
                            onClick={() => fetchGrade9WholeNumbersPractice({ difficulty: g9WholePracticeDifficulty })}
                            className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-semibold"
                            disabled={g9WholePracticeLoading}
                        >
                            New Set
                        </button>

                        {g9WholePracticeLoading && <div className="text-sm text-gray-600">Loading…</div>}
                    </div>

                    {g9WholePracticeError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g9WholePracticeError}</div>
                    )}

                    <div className="space-y-4">
                        {questions.map((q, idx) => (
                            <div key={q.id || idx} className="border border-gray-200 rounded-lg p-4 bg-white">
                                <div className="flex items-start justify-between gap-4 mb-2">
                                    <div>
                                        <div className="font-semibold text-gray-900">Q{idx + 1}. {q.question}</div>
                                        <div className="text-xs text-gray-500">{q.subskill?.replaceAll?.('_', ' ') || ''}</div>
                                    </div>
                                </div>

                                {q.table && (
                                    <div className="mb-3 p-3 border border-gray-200 rounded-lg bg-gray-50">
                                        <div className="text-sm font-semibold text-gray-800 mb-2">Reference table</div>
                                        <TableRenderer table={q.table} />
                                    </div>
                                )}

                                {q.long_division && (
                                    <div className="mb-3 p-3 border border-gray-200 rounded-lg bg-gray-50">
                                        <div className="text-sm font-semibold text-gray-800 mb-2">Long division layout</div>
                                        <pre className="font-mono text-sm whitespace-pre overflow-x-auto">{q.long_division}</pre>
                                    </div>
                                )}

                                {q.question_type === 'mcq' ? (
                                    <div>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                            {(q.options || []).map((opt) => (
                                                <button
                                                    key={opt}
                                                    onClick={() => setAnswer(idx, String(opt))}
                                                    className={`px-3 py-2 rounded-lg border text-left ${String(g9WholePracticeAnswers?.[idx] ?? '') === String(opt) ? 'border-indigo-500 bg-indigo-50' : 'border-gray-200 bg-white hover:bg-gray-50'}`}
                                                >
                                                    {opt}
                                                </button>
                                            ))}
                                        </div>
                                        <div className="mt-3">
                                            <button
                                                onClick={() => checkOne(idx)}
                                                className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                            >
                                                Check
                                            </button>
                                        </div>
                                    </div>
                                ) : (
                                    <div className="flex flex-col sm:flex-row gap-2">
                                        <input
                                            type="text"
                                            value={g9WholePracticeAnswers?.[idx] ?? ''}
                                            onChange={(e) => setAnswer(idx, e.target.value)}
                                            className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Your answer"
                                        />
                                        <button
                                            onClick={() => checkOne(idx)}
                                            className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                        >
                                            Check
                                        </button>
                                    </div>
                                )}

                                {g9WholePracticeFeedback?.[idx] && (
                                    <div className={`mt-3 p-3 rounded-lg text-sm ${g9WholePracticeFeedback[idx].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                        {g9WholePracticeFeedback[idx].message}
                                    </div>
                                )}

                                {q.explanation && (
                                    <details className="mt-3">
                                        <summary className="cursor-pointer text-sm font-semibold text-indigo-700">Show explanation</summary>
                                        <div className="mt-2 text-sm text-gray-700 whitespace-pre-wrap">{q.explanation}</div>
                                    </details>
                                )}
                            </div>
                        ))}

                        {!g9WholePracticeLoading && questions.length === 0 && (
                            <div className="text-sm text-gray-600">Click “New Set” to begin.</div>
                        )}
                    </div>
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

export default Grade9WholeNumbersPractice;
