import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const extractDivisionOperands = (q) => {
    if (!q) return null;
    const dividend = q?.dividend ?? q?.parameters?.dividend ?? q?.meta?.dividend ?? q?.data?.dividend;
    const divisor = q?.divisor ?? q?.parameters?.divisor ?? q?.meta?.divisor ?? q?.data?.divisor;
    if (dividend !== undefined && divisor !== undefined && dividend !== null && divisor !== null) {
        const a = String(dividend).trim();
        const b = String(divisor).trim();
        if (a !== '' && b !== '') return { dividend: a, divisor: b };
    }

    const s = String(q?.question ?? '').trim();
    const bySymbol = s.match(/(\d[\d,\s]*)\s*(?:÷|\/|\\)\s*(\d[\d,\s]*)/);
    if (bySymbol) {
        return {
            dividend: String(bySymbol[1]).replace(/\s+/g, '').replace(/,/g, ''),
            divisor: String(bySymbol[2]).replace(/\s+/g, '').replace(/,/g, ''),
        };
    }
    const byWords = s.match(/(\d[\d,\s]*)\s*(?:divided by|divide by)\s*(\d[\d,\s]*)/i);
    if (byWords) {
        return {
            dividend: String(byWords[1]).replace(/\s+/g, '').replace(/,/g, ''),
            divisor: String(byWords[2]).replace(/\s+/g, '').replace(/,/g, ''),
        };
    }
    return null;
};

const LongDivisionBracket = ({ divisor, dividend }) => {
    return (
        <div className="inline-flex items-stretch font-mono text-lg">
            <div className="pr-2 text-gray-900 flex items-center justify-end">{divisor}</div>
            <div className="pl-2 pr-2 pt-1 border-l-2 border-t-2 border-gray-900 text-gray-900">{dividend}</div>
        </div>
    );
};

const Grade8WholeNumbersPractice = ({
    onBack,
    g8WholeVisualAidsOpen,
    setG8WholeVisualAidsOpen,
    g8WholePracticeDifficulty,
    setG8WholePracticeDifficulty,
    fetchGrade8WholeNumbersPractice,
    g8WholePracticeLoading,
    g8WholePracticeError,
    g8WholePracticeQuestions,
    g8WholePracticeAnswers,
    setG8WholePracticeAnswers,
    g8WholePracticeFeedback,
    setG8WholePracticeFeedback,
    normalizeWholeNumberAnswer,
    renderGrade8WholeNumbersVisualAids,
}) => {
    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 8 Mathematics • Whole Numbers • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types. No calculator.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g8WholeVisualAidsOpen && (
                                <button
                                    onClick={() => setG8WholeVisualAidsOpen(true)}
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
                                value={g8WholePracticeDifficulty}
                                onChange={(e) => setG8WholePracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchGrade8WholeNumbersPractice({ difficulty: g8WholePracticeDifficulty })}
                                disabled={g8WholePracticeLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g8WholePracticeLoading ? 'Generating…' : 'Generate New Set'}
                            </button>
                        </div>
                    </div>

                    {g8WholePracticeError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g8WholePracticeError}
                        </div>
                    )}

                    {g8WholePracticeLoading && g8WholePracticeQuestions.length === 0 && (
                        <div className="p-6 text-gray-600">Loading questions…</div>
                    )}

                    <div className="space-y-6">
                        {g8WholePracticeQuestions.map((q, idx) => {
                            const qid = q.id || q.question_id || `q_${idx}`;
                            const answerValue = g8WholePracticeAnswers[qid] ?? '';
                            const feedback = g8WholePracticeFeedback[qid];
                            const isCorrect = feedback?.isCorrect;
                            const divisionOperands =
                                String(q?.subskill || '') === 'long_division'
                                    ? extractDivisionOperands(q)
                                    : null;

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

                                    {divisionOperands ? (
                                        <div className="mt-4 text-gray-800 font-medium">
                                            <LongDivisionBracket
                                                divisor={divisionOperands.divisor}
                                                dividend={divisionOperands.dividend}
                                            />
                                        </div>
                                    ) : (
                                        <div className="mt-4 text-gray-800 font-medium">{q.question}</div>
                                    )}

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
                                                                setG8WholePracticeAnswers((prev) => ({ ...prev, [qid]: e.target.value }));
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
                                                    setG8WholePracticeAnswers((prev) => ({ ...prev, [qid]: e.target.value }));
                                                }}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        )}
                                    </div>

                                    <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                        <button
                                            onClick={() => {
                                                const user = answerValue;
                                                const correct = q.correct_answer;
                                                const ok = normalizeWholeNumberAnswer(user) === normalizeWholeNumberAnswer(correct);
                                                setG8WholePracticeFeedback((prev) => ({
                                                    ...prev,
                                                    [qid]: {
                                                        isCorrect: ok,
                                                        correctAnswer: q.correct_answer,
                                                        explanation: q.explanation
                                                    }
                                                }));
                                            }}
                                            disabled={String(answerValue).trim() === ''}
                                            className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
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
                                        <div className="mt-3 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                            {feedback.explanation}
                                        </div>
                                    )}
                                </div>
                            );
                        })}

                        {!g8WholePracticeLoading && g8WholePracticeQuestions.length === 0 && !g8WholePracticeError && (
                            <div className="p-6 text-gray-600">No questions yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g8WholeVisualAidsOpen} setIsOpen={setG8WholeVisualAidsOpen}>
                    {renderGrade8WholeNumbersVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade8WholeNumbersPractice;
