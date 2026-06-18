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

const Grade9DecimalNotationPractice = ({
    onBack,
    g9DecVisualAidsOpen,
    setG9DecVisualAidsOpen,
    g9DecPracticeDifficulty,
    setG9DecPracticeDifficulty,
    fetchGrade9DecimalNotationPractice,
    g9DecPracticeLoading,
    g9DecPracticeError,
    g9DecPracticeQuestions,
    g9DecPracticeAnswers,
    setG9DecPracticeAnswers,
    g9DecPracticeFeedback,
    setG9DecPracticeFeedback,
    renderGrade9DecimalNotationVisualAids,
}) => {
    const questions = Array.isArray(g9DecPracticeQuestions) ? g9DecPracticeQuestions : [];

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g9DecPracticeAnswers) ? [...g9DecPracticeAnswers] : [];
        answers[idx] = value;
        setG9DecPracticeAnswers(answers);

        const feedback = Array.isArray(g9DecPracticeFeedback) ? [...g9DecPracticeFeedback] : [];
        feedback[idx] = null;
        setG9DecPracticeFeedback(feedback);
    };

    const checkOne = (idx) => {
        const q = questions[idx];
        if (!q) return;

        const answers = Array.isArray(g9DecPracticeAnswers) ? [...g9DecPracticeAnswers] : [];
        const feedback = Array.isArray(g9DecPracticeFeedback) ? [...g9DecPracticeFeedback] : [];

        const userValue = answers[idx] ?? '';
        const expected = normalizeDecimalNotationAnswer(q.correct_answer);
        const got = normalizeDecimalNotationAnswer(userValue);

        feedback[idx] = {
            isCorrect: expected && got === expected,
            correctAnswer: q.correct_answer,
            explanation: q.explanation,
        };

        setG9DecPracticeFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Decimal Notation • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types. No calculator.</p>
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
                                value={g9DecPracticeDifficulty}
                                onChange={(e) => setG9DecPracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchGrade9DecimalNotationPractice({ difficulty: g9DecPracticeDifficulty })}
                                disabled={g9DecPracticeLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g9DecPracticeLoading ? 'Generating…' : 'Generate New Set'}
                            </button>
                        </div>
                    </div>

                    {g9DecPracticeError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g9DecPracticeError}</div>
                    )}

                    <div className="space-y-4">
                        {questions.map((q, idx) => {
                            const answerValue = (Array.isArray(g9DecPracticeAnswers) ? g9DecPracticeAnswers[idx] : '') ?? '';
                            const feedback = Array.isArray(g9DecPracticeFeedback) ? g9DecPracticeFeedback[idx] : null;

                            return (
                                <div key={q.id || idx} className="border border-gray-200 rounded-lg p-4 bg-white">
                                    <div className="flex items-start justify-between gap-4 mb-2">
                                        <div>
                                            <div className="font-semibold text-gray-900">Q{idx + 1}. {q.question}</div>
                                            <div className="text-xs text-gray-500">{q.subskill?.replaceAll?.('_', ' ') || ''}</div>
                                        </div>
                                        {feedback && (
                                            <div className={`px-3 py-1 rounded-full text-sm font-semibold ${feedback.isCorrect ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                                                {feedback.isCorrect ? 'Correct' : 'Incorrect'}
                                            </div>
                                        )}
                                    </div>

                                    {q.table && (
                                        <div className="mb-3 p-3 border border-gray-200 rounded-lg bg-gray-50">
                                            <div className="text-sm font-semibold text-gray-800 mb-2">Common fractions, decimal fractions and percentages (reference)</div>
                                            <TableRenderer table={q.table} />
                                        </div>
                                    )}

                                    {q.question_type === 'mcq' && Array.isArray(q.options) ? (
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                            {q.options.map((opt) => (
                                                <label key={opt} className="flex items-center gap-2 p-3 bg-gray-50 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100">
                                                    <input
                                                        type="radio"
                                                        name={`q_${idx}`}
                                                        value={opt}
                                                        checked={answerValue === opt}
                                                        onChange={(e) => setAnswer(idx, e.target.value)}
                                                    />
                                                    <span className="text-gray-800">{opt}</span>
                                                </label>
                                            ))}
                                        </div>
                                    ) : (
                                        <input
                                            type="text"
                                            value={answerValue}
                                            onChange={(e) => setAnswer(idx, e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Answer (accepts comma or dot decimals; include % if needed)"
                                        />
                                    )}

                                    <div className="mt-3 flex flex-col sm:flex-row gap-2 sm:items-center">
                                        <button
                                            onClick={() => checkOne(idx)}
                                            className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700"
                                            disabled={String(answerValue).trim() === ''}
                                        >
                                            Check Answer
                                        </button>
                                        {feedback && (
                                            <div className="text-sm text-gray-700">
                                                <span className="font-semibold">Correct answer:</span> {feedback.correctAnswer}
                                            </div>
                                        )}
                                    </div>

                                    {feedback?.explanation && (
                                        <div className="mt-3 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3 whitespace-pre-wrap">
                                            {feedback.explanation}
                                        </div>
                                    )}
                                </div>
                            );
                        })}

                        {!g9DecPracticeLoading && questions.length === 0 && !g9DecPracticeError && (
                            <div className="p-6 text-gray-600">No questions yet.</div>
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

export default Grade9DecimalNotationPractice;
