import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

const Grade11ExponentsSurdsPractice = ({
    onBack,
    g11ExpSurdsPracticeQuestions,
    g11ExpSurdsPracticeAnswers,
    setG11ExpSurdsPracticeAnswers,
    g11ExpSurdsPracticeFeedback,
    g11ExpSurdsPracticeLoading,
    g11ExpSurdsPracticeError,
    g11ExpSurdsPracticeDifficulty,
    setG11ExpSurdsPracticeDifficulty,
    fetchGrade11ExpSurdsPractice,
    g11ExpSurdsVisualAidsOpen,
    setG11ExpSurdsVisualAidsOpen,
    renderGrade11ExpSurdsVisualAids,
}) => {
    const setAnswerAt = (idx, value) => {
        setG11ExpSurdsPracticeAnswers((prev) => {
            const next = Array.isArray(prev) ? [...prev] : [];
            next[idx] = value;
            return next;
        });
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 11 Mathematics • Exponents and surds • Practice</h2>
                            <p className="text-sm text-gray-600">Mixed question set (typed + multiple choice).</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g11ExpSurdsVisualAidsOpen && (
                                <button
                                    onClick={() => setG11ExpSurdsVisualAidsOpen(true)}
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
                                value={g11ExpSurdsPracticeDifficulty}
                                onChange={(e) => setG11ExpSurdsPracticeDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchGrade11ExpSurdsPractice({ difficulty: g11ExpSurdsPracticeDifficulty })}
                                disabled={g11ExpSurdsPracticeLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g11ExpSurdsPracticeLoading ? 'Loading…' : 'New Set'}
                            </button>
                        </div>
                    </div>

                    {g11ExpSurdsPracticeError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">{g11ExpSurdsPracticeError}</div>
                    )}

                    <div className="space-y-4">
                        {(g11ExpSurdsPracticeQuestions || []).map((q, idx) => {
                            const fb = (g11ExpSurdsPracticeFeedback || [])[idx];
                            const answer = (g11ExpSurdsPracticeAnswers || [])[idx] ?? '';
                            const isMcq = q?.question_type === 'mcq' && Array.isArray(q?.options);

                            return (
                                <div key={q?.id || idx} className="bg-gray-50 border border-gray-200 rounded-xl p-4">
                                    <div className="text-sm text-gray-600 mb-1">Question {idx + 1}{q?.subskill ? ` • ${q.subskill}` : ''}</div>
                                    <div className="text-gray-900 font-medium mb-3">{renderMathText(q?.question || '')}</div>

                                    {isMcq ? (
                                        <div className="space-y-2">
                                            {q.options.map((opt) => (
                                                <label key={opt} className="flex items-center gap-2">
                                                    <input
                                                        type="radio"
                                                        name={`g11expSurds_q_${idx}`}
                                                        value={opt}
                                                        checked={answer === opt}
                                                        onChange={() => setAnswerAt(idx, opt)}
                                                    />
                                                    <span className="text-gray-800">{renderMathText(opt)}</span>
                                                </label>
                                            ))}
                                        </div>
                                    ) : (
                                        <input
                                            value={answer}
                                            onChange={(e) => setAnswerAt(idx, e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Type your answer"
                                        />
                                    )}

                                    {fb && (
                                        <div
                                            className={`mt-3 p-3 rounded-lg text-sm border ${
                                                fb.kind === 'success'
                                                    ? 'bg-emerald-50 border-emerald-200 text-emerald-800'
                                                    : 'bg-red-50 border-red-200 text-red-800'
                                            }`}
                                        >
                                            {fb.message}
                                        </div>
                                    )}
                                </div>
                            );
                        })}
                    </div>
                </div>

                {g11ExpSurdsVisualAidsOpen && (
                    <VisualAidsPanel
                        isOpen={g11ExpSurdsVisualAidsOpen}
                        setIsOpen={setG11ExpSurdsVisualAidsOpen}
                    >
                        {renderGrade11ExpSurdsVisualAids ? renderGrade11ExpSurdsVisualAids() : null}
                    </VisualAidsPanel>
                )}
            </div>
        </div>
    );
};

export default Grade11ExponentsSurdsPractice;
