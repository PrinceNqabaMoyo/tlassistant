import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const Grade7ExponentsPractice = ({
    onBack,
    g7ExpVisualAidsOpen,
    setG7ExpVisualAidsOpen,
    g7ExpPracticeDifficulty,
    setG7ExpPracticeDifficulty,
    fetchGrade7ExponentsPractice,
    g7ExpPracticeLoading,
    g7ExpPracticeError,
    g7ExpPracticeQuestions,
    g7ExpPracticeAnswers,
    setG7ExpPracticeAnswers,
    g7ExpPracticeFeedback,
    setG7ExpPracticeFeedback,
    formatExponentCarets,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderExponentsVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 7 Mathematics • Exponents • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types. No calculator.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g7ExpVisualAidsOpen && (
                                <button
                                    onClick={() => setG7ExpVisualAidsOpen(true)}
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
                                value={g7ExpPracticeDifficulty}
                                onChange={(e) => setG7ExpPracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchGrade7ExponentsPractice({ difficulty: g7ExpPracticeDifficulty })}
                                disabled={g7ExpPracticeLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g7ExpPracticeLoading ? 'Generating…' : 'Generate New Set'}
                            </button>
                        </div>
                    </div>

                    {g7ExpPracticeError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g7ExpPracticeError}
                        </div>
                    )}

                    {g7ExpPracticeLoading && g7ExpPracticeQuestions.length === 0 && (
                        <div className="p-6 text-gray-600">Loading questions…</div>
                    )}

                    <div className="space-y-6">
                        {g7ExpPracticeQuestions.map((q, idx) => {
                            const qid = q.id || q.question_id || `q_${idx}`;
                            const answerValue = g7ExpPracticeAnswers[qid] ?? '';
                            const feedback = g7ExpPracticeFeedback[qid];
                            const promptText = q.question || q.prompt;

                            return (
                                <div key={qid} className="bg-gray-50 border border-gray-200 rounded-xl p-5">
                                    <div className="text-sm font-semibold text-gray-800 mb-2">Question {idx + 1}</div>
                                    <div className="text-gray-800 font-medium mb-4">{formatExponentCarets(promptText)}</div>

                                    {q.question_type === 'mcq' && Array.isArray(q.options) ? (
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                            {q.options.map((opt) => (
                                                <label key={opt} className="flex items-center gap-2 p-3 bg-white border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100">
                                                    <input
                                                        type="radio"
                                                        name={qid}
                                                        value={opt}
                                                        checked={answerValue === opt}
                                                        onChange={(e) => setG7ExpPracticeAnswers((prev) => ({ ...prev, [qid]: e.target.value }))}
                                                    />
                                                    <span className="text-gray-800">{formatExponentCarets(opt)}</span>
                                                </label>
                                            ))}
                                        </div>
                                    ) : (
                                        <input
                                            type="text"
                                            value={answerValue}
                                            onChange={(e) => setG7ExpPracticeAnswers((prev) => ({ ...prev, [qid]: e.target.value }))}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Type your answer"
                                        />
                                    )}

                                    <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                        <button
                                            onClick={() => {
                                                const user = String(answerValue);
                                                const correct = String(q.answer);
                                                const ok = q.question_type === 'mcq'
                                                    ? user === correct
                                                    : (normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                        || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase());

                                                setG7ExpPracticeFeedback((prev) => ({
                                                    ...prev,
                                                    [qid]: {
                                                        isCorrect: ok,
                                                        correctAnswer: q.answer,
                                                        explanation: q.explanation
                                                    }
                                                }));
                                            }}
                                            disabled={String(answerValue).trim() === ''}
                                            className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                        >
                                            Check
                                        </button>
                                    </div>

                                    {feedback && (
                                        <div className={`mt-4 p-3 rounded-lg text-sm border ${feedback.isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
                                            <div className="font-semibold">{feedback.isCorrect ? 'Correct' : 'Not quite'}</div>
                                            <div className="mt-1"><span className="font-semibold">Correct answer:</span> {formatExponentCarets(feedback.correctAnswer)}</div>
                                        </div>
                                    )}

                                    {feedback?.explanation && (
                                        <div className="mt-4 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                            {feedback.explanation}
                                        </div>
                                    )}
                                </div>
                            );
                        })}

                        {!g7ExpPracticeLoading && g7ExpPracticeQuestions.length === 0 && !g7ExpPracticeError && (
                            <div className="p-6 text-gray-600">No questions yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g7ExpVisualAidsOpen} setIsOpen={setG7ExpVisualAidsOpen}>
                    {renderExponentsVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade7ExponentsPractice;
