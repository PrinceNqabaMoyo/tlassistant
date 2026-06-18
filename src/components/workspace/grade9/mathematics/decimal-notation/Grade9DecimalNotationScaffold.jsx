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

const _gcd = (a, b) => {
    let x = Math.abs(Number(a) || 0);
    let y = Math.abs(Number(b) || 0);
    while (y) {
        const t = x % y;
        x = y;
        y = t;
    }
    return x || 1;
};

const normalizeFractionAnswer = (value) => {
    const s0 = String(value ?? '').trim();
    if (!s0) return '';

    const s = s0.replace(/\s+/g, ' ');

    if (/^[-+]?\d+$/.test(s)) return String(Number(s));

    const mixedMatch = s.match(/^([-+]?\d+)\s+(\d+)\/(\d+)$/);
    if (mixedMatch) {
        const whole = Number(mixedMatch[1]);
        const n = Number(mixedMatch[2]);
        const d = Number(mixedMatch[3]);
        if (!Number.isFinite(whole) || !Number.isFinite(n) || !Number.isFinite(d) || d === 0) return s0;
        const sign = whole < 0 ? -1 : 1;
        const absWhole = Math.abs(whole);
        const num = sign * (absWhole * d + n);
        const g = _gcd(num, d);
        const nn = num / g;
        const dd = d / g;
        return dd === 1 ? String(nn) : `${nn}/${dd}`;
    }

    const fracMatch = s.match(/^([-+]?\d+)\/(\d+)$/);
    if (fracMatch) {
        const n = Number(fracMatch[1]);
        const d = Number(fracMatch[2]);
        if (!Number.isFinite(n) || !Number.isFinite(d) || d === 0) return s0;
        const g = _gcd(n, d);
        const nn = n / g;
        const dd = d / g;
        return dd === 1 ? String(nn) : `${nn}/${dd}`;
    }

    return s0;
};

const normalizeDecimalString = (value) => {
    const raw = String(value ?? '').trim();
    if (!raw) return '';

    const hasPercent = raw.includes('%');
    const s0 = raw.replace('%', '').replace(/\s+/g, '').replace(',', '.');

    if (!/^[+-]?(\d+)(\.\d+)?$/.test(s0)) {
        return hasPercent ? `${s0}%` : s0;
    }

    let s = s0;
    if (s.includes('.')) {
        s = s.replace(/0+$/, '').replace(/\.$/, '');
    }

    if (s === '' || s === '-' || s === '+') s = '0';
    return hasPercent ? `${s}%` : s;
};

const normalizeDecimalNotationAnswer = (value) => {
    const s = String(value ?? '').trim();
    if (!s) return '';
    if (s.includes('/')) return normalizeFractionAnswer(s);
    return normalizeDecimalString(s);
};

const Grade9DecimalNotationScaffold = ({
    onBack,
    scaffoldSteps,
    g9DecVisualAidsOpen,
    setG9DecVisualAidsOpen,
    g9DecScaffoldDifficulty,
    setG9DecScaffoldDifficulty,
    g9DecScaffoldStepIndex,
    setG9DecScaffoldStepIndex,
    fetchGrade9DecimalNotationScaffoldQuestion,
    g9DecScaffoldLoading,
    g9DecScaffoldError,
    g9DecScaffoldQuestion,
    g9DecScaffoldShowHint,
    setG9DecScaffoldShowHint,
    g9DecScaffoldAnswer,
    setG9DecScaffoldAnswer,
    g9DecScaffoldFeedback,
    setG9DecScaffoldFeedback,
    g9DecScaffoldCheckpointIndex,
    setG9DecScaffoldCheckpointIndex,
    g9DecScaffoldCheckpointAnswers,
    setG9DecScaffoldCheckpointAnswers,
    g9DecScaffoldCheckpointFeedback,
    setG9DecScaffoldCheckpointFeedback,
    renderGrade9DecimalNotationVisualAids,
}) => {
    const currentStep = scaffoldSteps?.[g9DecScaffoldStepIndex] || scaffoldSteps?.[0];
    const question = g9DecScaffoldQuestion;

    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g9DecScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];

    const requestNew = () => {
        if (!currentStep) return;
        fetchGrade9DecimalNotationScaffoldQuestion({ subskill: currentStep.key, difficulty: g9DecScaffoldDifficulty });
    };

    const checkAnswer = () => {
        if (!question) return;
        const expected = normalizeDecimalNotationAnswer(question.correct_answer);
        const got = normalizeDecimalNotationAnswer(g9DecScaffoldAnswer);
        if (expected && got === expected) {
            setG9DecScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG9DecScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!currentCheckpoint) return;

        const answers = { ...(g9DecScaffoldCheckpointAnswers || {}) };
        const feedback = { ...(g9DecScaffoldCheckpointFeedback || {}) };

        const userValue = answers[currentCheckpoint.id] ?? '';
        const expected = normalizeDecimalNotationAnswer(currentCheckpoint.correct_answer);
        const got = normalizeDecimalNotationAnswer(userValue);

        if (expected && got === expected) {
            feedback[currentCheckpoint.id] = { kind: 'success', message: 'Correct.' };
        } else {
            feedback[currentCheckpoint.id] = { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` };
        }

        setG9DecScaffoldCheckpointFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Decimal Notation • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step method practice with checkpoints. No calculator.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g9DecVisualAidsOpen && (
                                <button
                                    onClick={() => setG9DecVisualAidsOpen(true)}
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
                                value={g9DecScaffoldDifficulty}
                                onChange={(e) => setG9DecScaffoldDifficulty(e.target.value)}
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
                                value={g9DecScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG9DecScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG9DecScaffoldFeedback(null);
                                    setG9DecScaffoldShowHint(false);
                                    setG9DecScaffoldCheckpointIndex(0);
                                    setG9DecScaffoldCheckpointAnswers({});
                                    setG9DecScaffoldCheckpointFeedback({});
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {(scaffoldSteps || []).map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>
                    </div>

                    {g9DecScaffoldError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g9DecScaffoldError}</div>
                    )}

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <h3 className="text-lg font-bold text-gray-900">Question</h3>
                            <div className="flex gap-2">
                                <button
                                    onClick={requestNew}
                                    className="px-3 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold"
                                    disabled={g9DecScaffoldLoading}
                                >
                                    New Question
                                </button>
                                <button
                                    onClick={() => setG9DecScaffoldShowHint((p) => !p)}
                                    className="px-3 py-2 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-800 text-sm font-semibold"
                                    disabled={!question}
                                >
                                    {g9DecScaffoldShowHint ? 'Hide hint' : 'Show hint'}
                                </button>
                            </div>
                        </div>

                        <div className="p-4 border border-gray-200 rounded-lg bg-gray-50">
                            {g9DecScaffoldLoading && <div className="text-sm text-gray-600">Loading…</div>}
                            {!g9DecScaffoldLoading && question && (
                                <div className="text-gray-900 whitespace-pre-wrap">{question.question}</div>
                            )}
                            {!g9DecScaffoldLoading && !question && (
                                <div className="text-sm text-gray-600">Select a subskill and click “New Question”.</div>
                            )}
                        </div>

                        {question?.table && (
                            <div className="mt-3 p-4 border border-gray-200 rounded-lg bg-white">
                                <div className="text-sm font-semibold text-gray-800 mb-2">Common fractions, decimal fractions and percentages (reference)</div>
                                <TableRenderer table={question.table} />
                            </div>
                        )}

                        {g9DecScaffoldShowHint && question?.explanation && (
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
                                                {s}
                                            </li>
                                        ))}
                                    </ol>
                                </div>
                            )}

                            <div className="p-4 border border-gray-200 rounded-lg bg-white">
                                <div className="font-semibold text-gray-900 mb-2">{currentCheckpoint?.prompt}</div>

                                <div className="flex flex-col sm:flex-row gap-2">
                                    <input
                                        type="text"
                                        value={(g9DecScaffoldCheckpointAnswers || {})[currentCheckpoint.id] ?? ''}
                                        onChange={(e) => {
                                            const next = { ...(g9DecScaffoldCheckpointAnswers || {}) };
                                            next[currentCheckpoint.id] = e.target.value;
                                            setG9DecScaffoldCheckpointAnswers(next);
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

                                {g9DecScaffoldCheckpointFeedback?.[currentCheckpoint?.id] && (
                                    <div
                                        className={`mt-3 p-3 rounded-lg text-sm ${g9DecScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success'
                                            ? 'bg-green-50 border border-green-200 text-green-800'
                                            : 'bg-red-50 border border-red-200 text-red-800'
                                            }`}
                                    >
                                        {g9DecScaffoldCheckpointFeedback[currentCheckpoint.id].message}
                                    </div>
                                )}

                                <div className="mt-4 flex justify-between">
                                    <button
                                        onClick={() => setG9DecScaffoldCheckpointIndex((p) => Math.max(0, (Number(p) || 0) - 1))}
                                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg"
                                        disabled={cpIndex === 0}
                                    >
                                        Previous
                                    </button>
                                    <button
                                        onClick={() => setG9DecScaffoldCheckpointIndex((p) => Math.min(checkpoints.length - 1, (Number(p) || 0) + 1))}
                                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg"
                                        disabled={cpIndex >= checkpoints.length - 1}
                                    >
                                        Next
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    <div className="border-t border-gray-200 pt-4">
                        <h3 className="text-lg font-bold text-gray-900 mb-2">Final Answer</h3>
                        <div className="flex flex-col sm:flex-row gap-2">
                            <input
                                type="text"
                                value={g9DecScaffoldAnswer}
                                onChange={(e) => {
                                    setG9DecScaffoldAnswer(e.target.value);
                                    setG9DecScaffoldFeedback(null);
                                }}
                                className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                placeholder="Answer (accepts comma or dot decimals; include % if needed)"
                                disabled={!question}
                            />
                            <button
                                onClick={checkAnswer}
                                className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                disabled={!question || String(g9DecScaffoldAnswer).trim() === ''}
                            >
                                Check Answer
                            </button>
                        </div>

                        {g9DecScaffoldFeedback && (
                            <div
                                className={`mt-3 p-3 rounded-lg text-sm ${g9DecScaffoldFeedback.kind === 'success'
                                    ? 'bg-green-50 border border-green-200 text-green-800'
                                    : 'bg-red-50 border border-red-200 text-red-800'
                                    }`}
                            >
                                {g9DecScaffoldFeedback.message}
                            </div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g9DecVisualAidsOpen} setIsOpen={setG9DecVisualAidsOpen}>
                    {renderGrade9DecimalNotationVisualAids?.()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade9DecimalNotationScaffold;
