import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const normalizeAlgebraExpr = (value) => {
    if (value === null || value === undefined) return '';
    return String(value)
        .trim()
        .replace(/−/g, '-')
        .replace(/×/g, 'x')
        .replace(/\s+/g, '')
        .toLowerCase();
};

const normalizeYesNo = (value) => {
    const s = String(value ?? '').trim().toLowerCase();
    if (s === 'y') return 'yes';
    if (s === 'n') return 'no';
    return s;
};

const Grade8AlgebraicExpressionsPractice = ({
    onBack,
    g8AlgExpVisualAidsOpen,
    setG8AlgExpVisualAidsOpen,
    g8AlgExpPracticeDifficulty,
    setG8AlgExpPracticeDifficulty,
    fetchGrade8AlgExpPractice,
    g8AlgExpPracticeLoading,
    g8AlgExpPracticeError,
    g8AlgExpPracticeQuestions,
    g8AlgExpPracticeAnswers,
    setG8AlgExpPracticeAnswers,
    g8AlgExpPracticeFeedback,
    setG8AlgExpPracticeFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade8AlgExpVisualAids,
}) => {
    const questions = Array.isArray(g8AlgExpPracticeQuestions) ? g8AlgExpPracticeQuestions : [];

    const getNormalizerFor = (rawAnswer) => {
        const s = String(rawAnswer ?? '').trim();
        if (!s) return normalizeTextAnswer;

        if (/^[-+]?\d+$/.test(s)) return normalizeWholeNumberAnswer;
        if (/^(yes|no)$/i.test(s)) return (v) => normalizeYesNo(normalizeTextAnswer(v));
        if (/[a-z]/i.test(s) || /\^|\(|\)|\+|\-/.test(s)) return normalizeAlgebraExpr;

        return normalizeTextAnswer;
    };

    const checkOne = (idx) => {
        const q = questions[idx];
        if (!q) return;

        const answers = Array.isArray(g8AlgExpPracticeAnswers) ? [...g8AlgExpPracticeAnswers] : [];
        const feedback = Array.isArray(g8AlgExpPracticeFeedback) ? [...g8AlgExpPracticeFeedback] : [];

        const userValue = answers[idx] ?? '';
        const normalize = getNormalizerFor(q.correct_answer);
        const expected = normalize(q.correct_answer);
        const got = normalize(userValue);

        if (expected && got === expected) {
            feedback[idx] = { kind: 'success', message: 'Correct.' };
        } else {
            feedback[idx] = { kind: 'error', message: `Not quite. Expected: ${q.correct_answer}` };
        }

        setG8AlgExpPracticeFeedback(feedback);
    };

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g8AlgExpPracticeAnswers) ? [...g8AlgExpPracticeAnswers] : [];
        answers[idx] = value;
        setG8AlgExpPracticeAnswers(answers);

        const feedback = Array.isArray(g8AlgExpPracticeFeedback) ? [...g8AlgExpPracticeFeedback] : [];
        feedback[idx] = null;
        setG8AlgExpPracticeFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 8 Mathematics • Algebraic expressions 1 • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g8AlgExpVisualAidsOpen && (
                                <button
                                    onClick={() => setG8AlgExpVisualAidsOpen(true)}
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
                                value={g8AlgExpPracticeDifficulty}
                                onChange={(e) => setG8AlgExpPracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>

                        <button
                            onClick={() => fetchGrade8AlgExpPractice({ difficulty: g8AlgExpPracticeDifficulty })}
                            className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-semibold"
                            disabled={g8AlgExpPracticeLoading}
                        >
                            New Set
                        </button>

                        {g8AlgExpPracticeLoading && (
                            <div className="text-sm text-gray-600">Loading…</div>
                        )}
                    </div>

                    {g8AlgExpPracticeError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g8AlgExpPracticeError}</div>
                    )}

                    <div className="space-y-4">
                        {questions.map((q, idx) => (
                            <div key={q.id || idx} className="border border-gray-200 rounded-lg p-4 bg-white">
                                <div className="font-semibold text-gray-900 mb-2">Q{idx + 1}. {q.question}</div>

                                {q.question_type === 'mcq' ? (
                                    <div>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                            {(q.options || []).map((opt) => (
                                                <button
                                                    key={opt}
                                                    onClick={() => setAnswer(idx, String(opt))}
                                                    className={`px-3 py-2 rounded-lg border text-left ${String(g8AlgExpPracticeAnswers?.[idx] ?? '') === String(opt) ? 'border-indigo-500 bg-indigo-50' : 'border-gray-200 bg-white hover:bg-gray-50'}`}
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
                                    <div>
                                        <div className="flex flex-col sm:flex-row gap-2">
                                            <input
                                                type="text"
                                                value={g8AlgExpPracticeAnswers?.[idx] ?? ''}
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
                                    </div>
                                )}

                                {g8AlgExpPracticeFeedback?.[idx] && (
                                    <div className={`mt-3 p-3 rounded-lg text-sm ${g8AlgExpPracticeFeedback[idx].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                        {g8AlgExpPracticeFeedback[idx].message}
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

                        {!g8AlgExpPracticeLoading && questions.length === 0 && (
                            <div className="text-sm text-gray-600">Click “New Set” to begin.</div>
                        )}
                    </div>
                </div>

                {g8AlgExpVisualAidsOpen && (
                    <VisualAidsPanel onClose={() => setG8AlgExpVisualAidsOpen(false)}>
                        {renderGrade8AlgExpVisualAids?.()}
                    </VisualAidsPanel>
                )}
            </div>
        </div>
    );
};

export default Grade8AlgebraicExpressionsPractice;
