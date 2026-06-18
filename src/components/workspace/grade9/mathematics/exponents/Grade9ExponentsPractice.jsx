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

const Grade9ExponentsPractice = ({
    onBack,
    g9ExpVisualAidsOpen,
    setG9ExpVisualAidsOpen,
    g9ExpPracticeDifficulty,
    setG9ExpPracticeDifficulty,
    fetchGrade9ExponentsPractice,
    g9ExpPracticeLoading,
    g9ExpPracticeError,
    g9ExpPracticeQuestions,
    g9ExpPracticeAnswers,
    setG9ExpPracticeAnswers,
    g9ExpPracticeFeedback,
    setG9ExpPracticeFeedback,
    renderGrade9ExponentsVisualAids,
}) => {
    const questions = Array.isArray(g9ExpPracticeQuestions) ? g9ExpPracticeQuestions : [];

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g9ExpPracticeAnswers) ? [...g9ExpPracticeAnswers] : [];
        answers[idx] = value;
        setG9ExpPracticeAnswers(answers);

        const feedback = Array.isArray(g9ExpPracticeFeedback) ? [...g9ExpPracticeFeedback] : [];
        feedback[idx] = null;
        setG9ExpPracticeFeedback(feedback);
    };

    const checkOne = (idx) => {
        const q = questions[idx];
        if (!q) return;

        const answers = Array.isArray(g9ExpPracticeAnswers) ? [...g9ExpPracticeAnswers] : [];
        const feedback = Array.isArray(g9ExpPracticeFeedback) ? [...g9ExpPracticeFeedback] : [];

        const userValue = answers[idx] ?? '';
        const expected = normalizeExpAnswer(q.correct_answer);
        const got = normalizeExpAnswer(userValue);

        feedback[idx] = {
            isCorrect: expected && got === expected,
            correctAnswer: q.correct_answer,
            explanation: q.explanation,
        };

        setG9ExpPracticeFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Exponents • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types. No calculator.</p>
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
                                value={g9ExpPracticeDifficulty}
                                onChange={(e) => setG9ExpPracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchGrade9ExponentsPractice({ difficulty: g9ExpPracticeDifficulty })}
                                disabled={g9ExpPracticeLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g9ExpPracticeLoading ? 'Generating…' : 'Generate New Set'}
                            </button>
                        </div>
                    </div>

                    {g9ExpPracticeError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g9ExpPracticeError}</div>
                    )}

                    <div className="space-y-4">
                        {questions.map((q, idx) => {
                            const answerValue = (Array.isArray(g9ExpPracticeAnswers) ? g9ExpPracticeAnswers[idx] : '') ?? '';
                            const feedback = Array.isArray(g9ExpPracticeFeedback) ? g9ExpPracticeFeedback[idx] : null;

                            return (
                                <div key={q.id || idx} className="border border-gray-200 rounded-lg p-4 bg-white">
                                    <div className="flex items-start justify-between gap-4 mb-2">
                                        <div>
                                            <div className="font-semibold text-gray-900">Q{idx + 1}. {renderMathText(q.question)}</div>
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
                                            <div className="text-sm font-semibold text-gray-800 mb-2">Exponent laws (reference)</div>
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
                                                    <span className="text-gray-800">{renderMathText(opt)}</span>
                                                </label>
                                            ))}
                                        </div>
                                    ) : (
                                        <input
                                            type="text"
                                            value={answerValue}
                                            onChange={(e) => setAnswer(idx, e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Answer"
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
                                                <span className="font-semibold">Correct answer:</span> {renderMathText(feedback.correctAnswer)}
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

                        {!g9ExpPracticeLoading && questions.length === 0 && !g9ExpPracticeError && (
                            <div className="p-6 text-gray-600">No questions yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g9ExpVisualAidsOpen} setIsOpen={setG9ExpVisualAidsOpen}>
                    {renderGrade9ExponentsVisualAids?.()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade9ExponentsPractice;
