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

const Grade12FinanceScaffold = ({
    onBack,
    scaffoldSteps,
    g12FinanceVisualAidsOpen,
    setG12FinanceVisualAidsOpen,
    g12FinanceScaffoldDifficulty,
    setG12FinanceScaffoldDifficulty,
    g12FinanceScaffoldStepIndex,
    setG12FinanceScaffoldStepIndex,
    fetchGrade12FinanceScaffoldQuestion,
    g12FinanceScaffoldLoading,
    g12FinanceScaffoldError,
    g12FinanceScaffoldQuestion,
    g12FinanceScaffoldAnswer,
    setG12FinanceScaffoldAnswer,
    g12FinanceScaffoldFeedback,
    setG12FinanceScaffoldFeedback,
    g12FinanceScaffoldShowHint,
    setG12FinanceScaffoldShowHint,
    renderGrade12FinanceVisualAids,
}) => {
    const question = g12FinanceScaffoldQuestion;

    const checkAnswer = () => {
        if (!question) return;
        const correct = String(question.correct_answer ?? question.answer ?? '');
        const ok = question.question_type === 'mcq'
            ? String(g12FinanceScaffoldAnswer) === correct
            : normalizeAnswer(g12FinanceScaffoldAnswer) === normalizeAnswer(correct);

        setG12FinanceScaffoldFeedback({
            isCorrect: ok,
            correctAnswer: correct,
            explanation: question.explanation,
        });
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 12 Mathematics • Finance • Scaffold</h2>
                            <p className="text-sm text-gray-600">One example at a time with a hint toggle.</p>
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
                                value={g12FinanceScaffoldDifficulty}
                                onChange={(e) => setG12FinanceScaffoldDifficulty(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>
                        <div className="w-full md:w-72">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Subskill</label>
                            <select
                                value={g12FinanceScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG12FinanceScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG12FinanceScaffoldAnswer('');
                                    setG12FinanceScaffoldFeedback(null);
                                    setG12FinanceScaffoldShowHint(false);
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {(scaffoldSteps || []).map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => {
                                    const step = (scaffoldSteps || [])[g12FinanceScaffoldStepIndex] || (scaffoldSteps || [])[0];
                                    if (!step) return;
                                    fetchGrade12FinanceScaffoldQuestion({ subskill: step.key, difficulty: g12FinanceScaffoldDifficulty });
                                }}
                                disabled={g12FinanceScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g12FinanceScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    {g12FinanceScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g12FinanceScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g12FinanceScaffoldLoading && !question ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : question ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{renderMathText(question.question)}</div>

                                <div className="mb-3">
                                    <label className="block text-sm font-semibold text-gray-700 mb-1">Your answer</label>
                                    <input
                                        type="text"
                                        value={g12FinanceScaffoldAnswer}
                                        onChange={(e) => {
                                            setG12FinanceScaffoldAnswer(e.target.value);
                                            setG12FinanceScaffoldFeedback(null);
                                        }}
                                        className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                        placeholder="Type your answer"
                                    />
                                </div>

                                <div className="flex flex-col sm:flex-row gap-2 sm:items-center">
                                    <button
                                        onClick={checkAnswer}
                                        disabled={String(g12FinanceScaffoldAnswer).trim() === ''}
                                        className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                    >
                                        Check
                                    </button>
                                    <button
                                        onClick={() => setG12FinanceScaffoldShowHint((p) => !p)}
                                        className="px-4 py-2 bg-indigo-50 text-indigo-800 rounded-lg font-semibold border border-indigo-200 hover:bg-indigo-100"
                                    >
                                        {g12FinanceScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                    </button>
                                </div>

                                {g12FinanceScaffoldFeedback && (
                                    <div className={`mt-4 p-4 rounded-lg border ${g12FinanceScaffoldFeedback.isCorrect ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                                        <div className="font-semibold">{g12FinanceScaffoldFeedback.isCorrect ? 'Correct!' : 'Not quite.'}</div>
                                        {!g12FinanceScaffoldFeedback.isCorrect && (
                                            <div className="mt-1 text-sm"><span className="font-semibold">Correct answer:</span> {renderMathText(g12FinanceScaffoldFeedback.correctAnswer)}</div>
                                        )}
                                    </div>
                                )}

                                {g12FinanceScaffoldShowHint && question.explanation && (
                                    <div className="mt-3 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                        {renderMathText(question.explanation)}
                                    </div>
                                )}
                            </>
                        ) : (
                            <div className="text-gray-600">No question loaded yet.</div>
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

export default Grade12FinanceScaffold;
