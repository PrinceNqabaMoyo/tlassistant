import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const Grade7Geo2DPractice = ({
    onBack,
    g7Geo2DVisualAidsOpen,
    setG7Geo2DVisualAidsOpen,
    g7Geo2DPracticeDifficulty,
    setG7Geo2DPracticeDifficulty,
    fetchGrade7Geo2DPractice,
    g7Geo2DPracticeLoading,
    g7Geo2DPracticeError,
    g7Geo2DPracticeQuestions,
    g7Geo2DPracticeAnswers,
    setG7Geo2DPracticeAnswers,
    g7Geo2DPracticeFeedback,
    setG7Geo2DPracticeFeedback,
    formatExponentCarets,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGeo2DVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 7 Mathematics • Geometry of 2D shapes • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types. No calculator.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g7Geo2DVisualAidsOpen && (
                                <button
                                    onClick={() => setG7Geo2DVisualAidsOpen(true)}
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
                                value={g7Geo2DPracticeDifficulty}
                                onChange={(e) => setG7Geo2DPracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>

                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchGrade7Geo2DPractice({ difficulty: g7Geo2DPracticeDifficulty })}
                                disabled={g7Geo2DPracticeLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g7Geo2DPracticeLoading ? 'Generating…' : 'Generate New Set'}
                            </button>
                        </div>
                    </div>

                    {g7Geo2DPracticeError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g7Geo2DPracticeError}
                        </div>
                    )}

                    {g7Geo2DPracticeLoading && g7Geo2DPracticeQuestions.length === 0 && (
                        <div className="p-6 text-gray-600">Loading questions…</div>
                    )}

                    <div className="space-y-6">
                        {g7Geo2DPracticeQuestions.map((q, idx) => {
                            const qid = q.id || q.question_id || `q_${idx}`;
                            const answerValue = g7Geo2DPracticeAnswers[qid] ?? '';
                            const feedback = g7Geo2DPracticeFeedback[qid];
                            const promptText = q.question || q.prompt;

                            return (
                                <div key={qid} className="bg-gray-50 border border-gray-200 rounded-xl p-5">
                                    <div className="flex items-start justify-between gap-3">
                                        <div>
                                            <div className="text-sm text-gray-500">Question {idx + 1}</div>
                                            <div className="text-gray-900 font-semibold">{formatExponentCarets(promptText)}</div>
                                        </div>
                                        <div className="text-xs font-semibold px-2 py-1 rounded-full bg-white border border-gray-200 text-gray-700">
                                            {q.question_type?.toUpperCase?.() || 'Q'}
                                        </div>
                                    </div>

                                    <div className="mt-4">
                                        {q.question_type === 'mcq' && Array.isArray(q.options) ? (
                                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                                {q.options.map((opt) => (
                                                    <label key={opt} className="flex items-center gap-2 p-3 bg-white border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100">
                                                        <input
                                                            type="radio"
                                                            name={qid}
                                                            value={opt}
                                                            checked={answerValue === opt}
                                                            onChange={(e) => setG7Geo2DPracticeAnswers((prev) => ({ ...prev, [qid]: e.target.value }))}
                                                        />
                                                        <span className="text-gray-800">{formatExponentCarets(opt)}</span>
                                                    </label>
                                                ))}
                                            </div>
                                        ) : (
                                            <input
                                                type="text"
                                                value={answerValue}
                                                onChange={(e) => setG7Geo2DPracticeAnswers((prev) => ({ ...prev, [qid]: e.target.value }))}
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
                                                const ok = normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct)
                                                    || normalizeTextAnswer(user).toLowerCase() === normalizeTextAnswer(correct).toLowerCase();
                                                setG7Geo2DPracticeFeedback((prev) => ({
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
                                    </div>

                                    {feedback && (
                                        <div className={`mt-4 p-3 rounded-lg text-sm border ${feedback.isCorrect ? 'bg-green-50 border-green-200 text-green-900' : 'bg-red-50 border-red-200 text-red-900'}`}>
                                            <div className="font-semibold">{feedback.isCorrect ? 'Correct' : 'Not quite'}</div>
                                            <div className="mt-1"><span className="font-semibold">Correct answer:</span> {formatExponentCarets(feedback.correctAnswer)}</div>
                                            {feedback.explanation && (
                                                <div className="mt-2 text-gray-800">{formatExponentCarets(feedback.explanation)}</div>
                                            )}
                                        </div>
                                    )}
                                </div>
                            );
                        })}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g7Geo2DVisualAidsOpen} setIsOpen={setG7Geo2DVisualAidsOpen}>
                    {renderGeo2DVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade7Geo2DPractice;
