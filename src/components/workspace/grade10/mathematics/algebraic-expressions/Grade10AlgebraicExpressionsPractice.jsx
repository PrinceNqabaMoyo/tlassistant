import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

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

const Grade10AlgebraicExpressionsPractice = ({
    onBack,
    g10AlgExpVisualAidsOpen,
    setG10AlgExpVisualAidsOpen,
    g10AlgExpPracticeDifficulty,
    setG10AlgExpPracticeDifficulty,
    fetchGrade10AlgExpPractice,
    g10AlgExpPracticeLoading,
    g10AlgExpPracticeError,
    g10AlgExpPracticeQuestions,
    g10AlgExpPracticeAnswers,
    setG10AlgExpPracticeAnswers,
    g10AlgExpPracticeFeedback,
    setG10AlgExpPracticeFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade10AlgExpVisualAids,
}) => {
    const questions = Array.isArray(g10AlgExpPracticeQuestions) ? g10AlgExpPracticeQuestions : [];

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

        const answers = Array.isArray(g10AlgExpPracticeAnswers) ? [...g10AlgExpPracticeAnswers] : [];
        const feedback = Array.isArray(g10AlgExpPracticeFeedback) ? [...g10AlgExpPracticeFeedback] : [];

        const userValue = answers[idx] ?? '';
        const normalize = getNormalizerFor(q.correct_answer);
        const expected = normalize(q.correct_answer);
        const got = normalize(userValue);

        if (expected && got === expected) {
            feedback[idx] = { kind: 'success', message: 'Correct.' };
        } else {
            feedback[idx] = { kind: 'error', message: `Not quite. Expected: ${q.correct_answer}` };
        }

        setG10AlgExpPracticeFeedback(feedback);
    };

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g10AlgExpPracticeAnswers) ? [...g10AlgExpPracticeAnswers] : [];
        answers[idx] = value;
        setG10AlgExpPracticeAnswers(answers);

        const feedback = Array.isArray(g10AlgExpPracticeFeedback) ? [...g10AlgExpPracticeFeedback] : [];
        feedback[idx] = null;
        setG10AlgExpPracticeFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 10 Mathematics • Algebraic expressions • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question types. Check each answer as you go.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g10AlgExpVisualAidsOpen && (
                                <button
                                    onClick={() => setG10AlgExpVisualAidsOpen(true)}
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
                                value={g10AlgExpPracticeDifficulty}
                                onChange={(e) => setG10AlgExpPracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchGrade10AlgExpPractice({ difficulty: g10AlgExpPracticeDifficulty })}
                                disabled={g10AlgExpPracticeLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g10AlgExpPracticeLoading ? 'Generating…' : 'Generate New Set'}
                            </button>
                        </div>
                    </div>

                    {g10AlgExpPracticeError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">{g10AlgExpPracticeError}</div>
                    )}

                    {g10AlgExpPracticeLoading && questions.length === 0 && (
                        <div className="p-6 text-gray-600">Loading questions…</div>
                    )}

                    <div className="space-y-6">
                        {questions.map((q, idx) => {
                            const userValue = (Array.isArray(g10AlgExpPracticeAnswers) ? g10AlgExpPracticeAnswers[idx] : '') ?? '';
                            const fb = Array.isArray(g10AlgExpPracticeFeedback) ? g10AlgExpPracticeFeedback[idx] : null;

                            return (
                                <div key={q.id || idx} className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                                    <div className="flex items-start justify-between gap-4">
                                        <div>
                                            <h3 className="text-lg font-semibold text-gray-900">Question {idx + 1}</h3>
                                            <p className="text-sm text-gray-600">{q.subskill?.replaceAll?.('_', ' ') || ''}</p>
                                        </div>
                                        {fb && (
                                            <div className={`px-3 py-1 rounded-full text-sm font-semibold ${fb.kind === 'success' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                                                {fb.kind === 'success' ? 'Correct' : 'Incorrect'}
                                            </div>
                                        )}
                                    </div>

                                    <div className="mt-4 text-gray-800 font-medium">{renderMathText(q.question)}</div>

                                    {q.question_type === 'mcq' && Array.isArray(q.options) ? (
                                        <div className="mt-4 grid grid-cols-1 sm:grid-cols-2 gap-2">
                                            {q.options.map((opt) => (
                                                <label key={opt} className="flex items-center gap-2 p-3 bg-white border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50">
                                                    <input
                                                        type="radio"
                                                        name={`q_${idx}`}
                                                        value={opt}
                                                        checked={String(userValue) === String(opt)}
                                                        onChange={(e) => setAnswer(idx, e.target.value)}
                                                    />
                                                    <span className="text-gray-800">{renderMathText(opt)}</span>
                                                </label>
                                            ))}
                                        </div>
                                    ) : (
                                        <div className="mt-4">
                                            <input
                                                type="text"
                                                value={userValue}
                                                onChange={(e) => setAnswer(idx, e.target.value)}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        </div>
                                    )}

                                    <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                        <button
                                            onClick={() => checkOne(idx)}
                                            disabled={String(userValue).trim() === ''}
                                            className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                        >
                                            Check
                                        </button>
                                        {fb?.kind !== 'success' && fb && (
                                            <div className="text-sm text-gray-700"><span className="font-semibold">Correct:</span> {renderMathText(q.correct_answer)}</div>
                                        )}
                                    </div>

                                    {fb && (
                                        <div className={`mt-3 p-3 rounded-lg text-sm ${fb.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                            {renderMathText(fb.message)}
                                        </div>
                                    )}
                                </div>
                            );
                        })}

                        {!g10AlgExpPracticeLoading && questions.length === 0 && !g10AlgExpPracticeError && (
                            <div className="p-6 text-gray-600">No questions yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g10AlgExpVisualAidsOpen} setIsOpen={setG10AlgExpVisualAidsOpen}>
                    {renderGrade10AlgExpVisualAids?.()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade10AlgebraicExpressionsPractice;
