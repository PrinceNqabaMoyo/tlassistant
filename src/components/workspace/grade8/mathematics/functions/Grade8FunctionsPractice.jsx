import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const normalizeFunctionAnswer = (value) => {
    if (value === null || value === undefined) return '';
    return String(value)
        .trim()
        .replace(/−/g, '-')
        .replace(/×/g, 'x')
        .replace(/\s+/g, '')
        .toLowerCase();
};

const normalizeCommaList = (value) => {
    const s = String(value ?? '')
        .trim()
        .replace(/−/g, '-')
        .replace(/\s+/g, '');
    if (!s) return '';
    return s
        .split(',')
        .map((p) => p.trim())
        .filter(Boolean)
        .join(',');
};

const Grade8FunctionsPractice = ({
    onBack,
    g8FuncVisualAidsOpen,
    setG8FuncVisualAidsOpen,
    g8FuncPracticeDifficulty,
    setG8FuncPracticeDifficulty,
    fetchGrade8FunctionsPractice,
    g8FuncPracticeLoading,
    g8FuncPracticeError,
    g8FuncPracticeQuestions,
    g8FuncPracticeAnswers,
    setG8FuncPracticeAnswers,
    g8FuncPracticeFeedback,
    setG8FuncPracticeFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade8FunctionsVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 8 Mathematics • Functions &amp; Relationships • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g8FuncVisualAidsOpen && (
                                <button
                                    onClick={() => setG8FuncVisualAidsOpen(true)}
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
                                value={g8FuncPracticeDifficulty}
                                onChange={(e) => setG8FuncPracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchGrade8FunctionsPractice({ difficulty: g8FuncPracticeDifficulty })}
                                disabled={g8FuncPracticeLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g8FuncPracticeLoading ? 'Generating…' : 'Generate New Set'}
                            </button>
                        </div>
                    </div>

                    {g8FuncPracticeError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g8FuncPracticeError}
                        </div>
                    )}

                    {g8FuncPracticeLoading && g8FuncPracticeQuestions.length === 0 && (
                        <div className="p-6 text-gray-600">Loading questions…</div>
                    )}

                    <div className="space-y-6">
                        {g8FuncPracticeQuestions.map((q, idx) => {
                            const qid = q.id || q.question_id || `q_${idx}`;
                            const answerValue = g8FuncPracticeAnswers[qid] ?? '';
                            const feedback = g8FuncPracticeFeedback[qid];
                            const isCorrect = feedback?.isCorrect;

                            return (
                                <div key={qid} className="bg-gray-50 p-6 rounded-xl border border-gray-200">
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

                                    <div className="mt-4 text-gray-800 font-medium">{q.question}</div>

                                    <div className="mt-4">
                                        {q.question_type === 'mcq' && Array.isArray(q.options) ? (
                                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                                {q.options.map((opt) => (
                                                    <label key={opt} className="flex items-center gap-2 p-3 bg-white border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50">
                                                        <input
                                                            type="radio"
                                                            name={qid}
                                                            value={opt}
                                                            checked={answerValue === opt}
                                                            onChange={(e) => {
                                                                setG8FuncPracticeAnswers((prev) => ({ ...prev, [qid]: e.target.value }));
                                                            }}
                                                        />
                                                        <span className="text-gray-800">{opt}</span>
                                                    </label>
                                                ))}
                                            </div>
                                        ) : (
                                            <input
                                                type="text"
                                                value={answerValue}
                                                onChange={(e) => {
                                                    setG8FuncPracticeAnswers((prev) => ({ ...prev, [qid]: e.target.value }));
                                                }}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        )}
                                    </div>

                                    <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                        <button
                                            onClick={() => {
                                                const user = String(answerValue);
                                                const correct = String(q.correct_answer ?? q.answer ?? '');

                                                const ok = q.question_type === 'mcq'
                                                    ? user === correct
                                                    : (
                                                        normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                        || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase()
                                                        || normalizeCommaList(user) === normalizeCommaList(correct)
                                                        || normalizeFunctionAnswer(user) === normalizeFunctionAnswer(correct)
                                                    );

                                                setG8FuncPracticeFeedback((prev) => ({
                                                    ...prev,
                                                    [qid]: {
                                                        isCorrect: ok,
                                                        correctAnswer: q.correct_answer ?? q.answer,
                                                        explanation: q.explanation
                                                    }
                                                }));
                                            }}
                                            disabled={String(answerValue).trim() === ''}
                                            className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                        >
                                            Check
                                        </button>
                                        {feedback && (
                                            <div className="text-sm text-gray-700">
                                                <span className="font-semibold">Correct answer:</span> {feedback.correctAnswer}
                                            </div>
                                        )}
                                    </div>

                                    {feedback?.explanation && (
                                        <div className="mt-3 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                            {feedback.explanation}
                                        </div>
                                    )}
                                </div>
                            );
                        })}

                        {!g8FuncPracticeLoading && g8FuncPracticeQuestions.length === 0 && !g8FuncPracticeError && (
                            <div className="p-6 text-gray-600">No questions yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g8FuncVisualAidsOpen} setIsOpen={setG8FuncVisualAidsOpen}>
                    {renderGrade8FunctionsVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade8FunctionsPractice;
