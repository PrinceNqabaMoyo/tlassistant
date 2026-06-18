import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const normalizePatternAnswer = (value) => {
    if (value === null || value === undefined) return '';
    return String(value)
        .trim()
        .replace(/;/g, ',')
        .replace(/\s+/g, '')
        .replace(/−/g, '-')
        .toLowerCase();
};

const normalizeCommaNumberList = (value) => {
    const s = normalizePatternAnswer(value);
    if (!s) return '';
    const parts = s
        .split(',')
        .map((p) => p.trim())
        .filter(Boolean);
    return parts.join(',');
};

const Grade9PatternsPractice = ({
    onBack,
    g9PatVisualAidsOpen,
    setG9PatVisualAidsOpen,
    g9PatPracticeDifficulty,
    setG9PatPracticeDifficulty,
    fetchGrade9PatternsPractice,
    g9PatPracticeLoading,
    g9PatPracticeError,
    g9PatPracticeQuestions,
    g9PatPracticeAnswers,
    setG9PatPracticeAnswers,
    g9PatPracticeFeedback,
    setG9PatPracticeFeedback,
    renderGrade9PatternsVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Numeric &amp; Geometric Patterns • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types. No calculator.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g9PatVisualAidsOpen && (
                                <button
                                    onClick={() => setG9PatVisualAidsOpen(true)}
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
                                value={g9PatPracticeDifficulty}
                                onChange={(e) => setG9PatPracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchGrade9PatternsPractice({ difficulty: g9PatPracticeDifficulty })}
                                disabled={g9PatPracticeLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g9PatPracticeLoading ? 'Generating…' : 'Generate New Set'}
                            </button>
                        </div>
                    </div>

                    {g9PatPracticeError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g9PatPracticeError}
                        </div>
                    )}

                    {g9PatPracticeLoading && g9PatPracticeQuestions.length === 0 && (
                        <div className="p-6 text-gray-600">Loading questions…</div>
                    )}

                    <div className="space-y-6">
                        {g9PatPracticeQuestions.map((q, idx) => {
                            const qid = q.id || q.question_id || `q_${idx}`;
                            const answerValue = g9PatPracticeAnswers[qid] ?? '';
                            const feedback = g9PatPracticeFeedback[qid];
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
                                                                setG9PatPracticeAnswers((prev) => ({ ...prev, [qid]: e.target.value }));
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
                                                    setG9PatPracticeAnswers((prev) => ({ ...prev, [qid]: e.target.value }));
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
                                                        normalizeCommaNumberList(user) === normalizeCommaNumberList(correct)
                                                        || normalizePatternAnswer(user) === normalizePatternAnswer(correct)
                                                    );

                                                setG9PatPracticeFeedback((prev) => ({
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

                        {!g9PatPracticeLoading && g9PatPracticeQuestions.length === 0 && !g9PatPracticeError && (
                            <div className="p-6 text-gray-600">No questions yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g9PatVisualAidsOpen} setIsOpen={setG9PatVisualAidsOpen}>
                    {renderGrade9PatternsVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade9PatternsPractice;
