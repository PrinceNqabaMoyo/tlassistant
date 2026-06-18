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

const Grade12FinancePractice = ({
    onBack,
    g12FinanceVisualAidsOpen,
    setG12FinanceVisualAidsOpen,
    g12FinancePracticeDifficulty,
    setG12FinancePracticeDifficulty,
    fetchGrade12FinancePractice,
    g12FinancePracticeLoading,
    g12FinancePracticeError,
    g12FinancePracticeQuestions,
    g12FinancePracticeAnswers,
    setG12FinancePracticeAnswers,
    g12FinancePracticeFeedback,
    setG12FinancePracticeFeedback,
    renderGrade12FinanceVisualAids,
}) => {
    const questions = Array.isArray(g12FinancePracticeQuestions) ? g12FinancePracticeQuestions : [];

    const checkOne = (idx) => {
        const q = questions[idx];
        if (!q) return;

        const answers = Array.isArray(g12FinancePracticeAnswers) ? [...g12FinancePracticeAnswers] : [];
        const feedback = Array.isArray(g12FinancePracticeFeedback) ? [...g12FinancePracticeFeedback] : [];

        const userValue = answers[idx] ?? '';
        const correct = String(q.correct_answer ?? q.answer ?? '');

        const ok = q.question_type === 'mcq'
            ? String(userValue) === correct
            : normalizeAnswer(userValue) === normalizeAnswer(correct);

        feedback[idx] = ok
            ? { kind: 'success', message: 'Correct.' }
            : { kind: 'error', message: `Not quite. Expected: ${correct}` };

        setG12FinancePracticeFeedback(feedback);
    };

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g12FinancePracticeAnswers) ? [...g12FinancePracticeAnswers] : [];
        answers[idx] = value;
        setG12FinancePracticeAnswers(answers);

        const feedback = Array.isArray(g12FinancePracticeFeedback) ? [...g12FinancePracticeFeedback] : [];
        feedback[idx] = null;
        setG12FinancePracticeFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 12 Mathematics • Finance • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types. Check each answer as you go.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g12FinanceVisualAidsOpen && (
                                <button
                                    onClick={() => setG12FinanceVisualAidsOpen(true)}
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
                                value={g12FinancePracticeDifficulty}
                                onChange={(e) => setG12FinancePracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchGrade12FinancePractice({ difficulty: g12FinancePracticeDifficulty })}
                                disabled={g12FinancePracticeLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g12FinancePracticeLoading ? 'Generating…' : 'Generate New Set'}
                            </button>
                        </div>
                    </div>

                    {g12FinancePracticeError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g12FinancePracticeError}
                        </div>
                    )}

                    {g12FinancePracticeLoading && questions.length === 0 && (
                        <div className="p-6 text-gray-600">Loading questions…</div>
                    )}

                    <div className="space-y-6">
                        {questions.map((q, idx) => {
                            const answerValue = (Array.isArray(g12FinancePracticeAnswers) ? g12FinancePracticeAnswers[idx] : '') ?? '';
                            const feedback = Array.isArray(g12FinancePracticeFeedback) ? g12FinancePracticeFeedback[idx] : null;
                            const isCorrect = feedback?.kind === 'success';

                            return (
                                <div key={q.id || `q_${idx}`} className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                                    <div className="flex items-start justify-between gap-4">
                                        <div>
                                            <h3 className="text-lg font-semibold text-gray-900">Question {idx + 1}</h3>
                                            <p className="text-sm text-gray-600">{q.subskill?.replaceAll?.('_', ' ') || ''}</p>
                                        </div>
                                        {feedback && (
                                            <div className={`px-3 py-1 rounded-full text-sm font-semibold ${isCorrect ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                                                {isCorrect ? 'Correct' : 'Incorrect'}
                                            </div>
                                        )}
                                    </div>

                                    <div className="mt-4 text-gray-800 font-medium">{renderMathText(q.question)}</div>

                                    <div className="mt-4">
                                        {q.question_type === 'mcq' && Array.isArray(q.options) ? (
                                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                                {q.options.map((opt) => (
                                                    <label key={opt} className="flex items-center gap-2 p-3 bg-white border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50">
                                                        <input
                                                            type="radio"
                                                            name={q.id || `q_${idx}`}
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
                                                placeholder="Type your answer"
                                            />
                                        )}
                                    </div>

                                    <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                        <button
                                            onClick={() => checkOne(idx)}
                                            disabled={String(answerValue).trim() === ''}
                                            className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                        >
                                            Check
                                        </button>
                                        {feedback && (
                                            <div className="text-sm text-gray-700">
                                                <span className="font-semibold">Correct answer:</span> {renderMathText(String(q.correct_answer ?? q.answer ?? ''))}
                                            </div>
                                        )}
                                    </div>

                                    {q.explanation && (
                                        <div className="mt-3 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                            {renderMathText(q.explanation)}
                                        </div>
                                    )}
                                </div>
                            );
                        })}

                        {!g12FinancePracticeLoading && questions.length === 0 && !g12FinancePracticeError && (
                            <div className="p-6 text-gray-600">No questions yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g12FinanceVisualAidsOpen} setIsOpen={setG12FinanceVisualAidsOpen}>
                    {renderGrade12FinanceVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade12FinancePractice;
