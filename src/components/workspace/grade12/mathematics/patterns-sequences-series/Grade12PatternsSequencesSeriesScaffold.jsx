import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

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
    return s
        .split(',')
        .map((p) => p.trim())
        .filter(Boolean)
        .join(',');
};

const Grade12PatternsSequencesSeriesScaffold = ({
    onBack,
    scaffoldSteps,
    g12PssVisualAidsOpen,
    setG12PssVisualAidsOpen,
    g12PssScaffoldDifficulty,
    setG12PssScaffoldDifficulty,
    g12PssScaffoldStepIndex,
    setG12PssScaffoldStepIndex,
    fetchGrade12PatternsSequencesSeriesScaffoldQuestion,
    g12PssScaffoldLoading,
    g12PssScaffoldError,
    g12PssScaffoldQuestion,
    g12PssScaffoldCheckpointIndex,
    setG12PssScaffoldCheckpointIndex,
    g12PssScaffoldCheckpointAnswers,
    setG12PssScaffoldCheckpointAnswers,
    g12PssScaffoldCheckpointFeedback,
    setG12PssScaffoldCheckpointFeedback,
    g12PssScaffoldAnswer,
    setG12PssScaffoldAnswer,
    g12PssScaffoldFeedback,
    setG12PssScaffoldFeedback,
    g12PssScaffoldShowHint,
    setG12PssScaffoldShowHint,
    renderGrade12PatternsSequencesSeriesVisualAids,
}) => {
    const question = g12PssScaffoldQuestion;
    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIdx = Math.max(0, Math.min(checkpoints.length - 1, Number(g12PssScaffoldCheckpointIndex) || 0));
    const cp = checkpoints[cpIdx];
    const cpId = cp?.id || `cp_${cpIdx}`;
    const cpAnswer = g12PssScaffoldCheckpointAnswers?.[cpId] ?? '';
    const cpFeedback = g12PssScaffoldCheckpointFeedback?.[cpId];

    const checkTyped = (user, expected) => {
        const u = normalizeCommaNumberList(user);
        const e = normalizeCommaNumberList(expected);
        return (e && u === e) || normalizePatternAnswer(user) === normalizePatternAnswer(expected);
    };

    const checkCheckpoint = () => {
        if (!cp) return;
        const ok = cp.kind === 'mcq' ? String(cpAnswer) === String(cp.correct_answer ?? '') : checkTyped(cpAnswer, cp.correct_answer ?? '');
        setG12PssScaffoldCheckpointFeedback((prev) => ({
            ...(prev || {}),
            [cpId]: {
                isCorrect: ok,
                correctAnswer: String(cp.correct_answer ?? ''),
                explanation: cp.explanation,
            },
        }));
        if (ok) {
            setG12PssScaffoldCheckpointIndex((prev) => (Number(prev) || 0) + 1);
        }
    };

    const checkAnswer = () => {
        if (!question) return;
        const ok = question.question_type === 'mcq'
            ? String(g12PssScaffoldAnswer) === String(question.correct_answer ?? '')
            : checkTyped(g12PssScaffoldAnswer, question.correct_answer ?? '');
        setG12PssScaffoldFeedback({
            isCorrect: ok,
            correctAnswer: String(question.correct_answer ?? ''),
            explanation: question.explanation,
        });
    };

    const isDone = question?.question_type === 'scaffold' && checkpoints.length > 0
        ? (Number(g12PssScaffoldCheckpointIndex) || 0) >= checkpoints.length
        : false;

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 12 Mathematics • Patterns, Sequences &amp; Series • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g12PssVisualAidsOpen && (
                                <button
                                    onClick={() => setG12PssVisualAidsOpen(true)}
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
                                value={g12PssScaffoldDifficulty}
                                onChange={(e) => setG12PssScaffoldDifficulty(e.target.value)}
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
                                value={g12PssScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG12PssScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG12PssScaffoldCheckpointIndex(0);
                                    setG12PssScaffoldCheckpointAnswers({});
                                    setG12PssScaffoldCheckpointFeedback({});
                                    setG12PssScaffoldAnswer('');
                                    setG12PssScaffoldFeedback(null);
                                    setG12PssScaffoldShowHint(false);
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
                                    const step = (scaffoldSteps || [])[g12PssScaffoldStepIndex] || (scaffoldSteps || [])[0];
                                    if (!step) return;
                                    fetchGrade12PatternsSequencesSeriesScaffoldQuestion({ subskill: step.key, difficulty: g12PssScaffoldDifficulty });
                                }}
                                disabled={g12PssScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g12PssScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    {g12PssScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">
                            {g12PssScaffoldError}
                        </div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g12PssScaffoldLoading && !question ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : question ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{renderMathText(question.question)}</div>

                                {Array.isArray(question.steps) && question.steps.length > 0 && (
                                    <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                        <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                        <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                            {question.steps.map((s, idx) => (
                                                <li key={`${idx}_${s}`}>{renderMathText(s)}</li>
                                            ))}
                                        </ol>
                                    </div>
                                )}

                                {question.question_type === 'scaffold' && checkpoints.length > 0 ? (
                                    isDone ? (
                                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                                            <div className="text-gray-900 font-semibold mb-2">Finished</div>
                                            {question.explanation && (
                                                <div className="mt-3 text-sm text-gray-700 bg-gray-50 border border-gray-200 rounded-lg p-3">
                                                    {renderMathText(question.explanation)}
                                                </div>
                                            )}
                                        </div>
                                    ) : (
                                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                                            <div className="text-sm font-semibold text-gray-800 mb-2">Checkpoint {cpIdx + 1} / {checkpoints.length}</div>
                                            <div className="text-gray-800 font-medium mb-3">{renderMathText(cp?.prompt || '')}</div>

                                            {cp?.kind === 'mcq' && Array.isArray(cp.options) ? (
                                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                                    {cp.options.map((opt) => (
                                                        <label key={opt} className="flex items-center gap-2 p-3 bg-gray-50 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100">
                                                            <input
                                                                type="radio"
                                                                name={cpId}
                                                                value={opt}
                                                                checked={cpAnswer === opt}
                                                                onChange={(e) => {
                                                                    setG12PssScaffoldCheckpointAnswers((prev) => ({ ...(prev || {}), [cpId]: e.target.value }));
                                                                    setG12PssScaffoldCheckpointFeedback((prev) => ({ ...(prev || {}), [cpId]: null }));
                                                                }}
                                                            />
                                                            <span className="text-gray-800">{renderMathText(opt)}</span>
                                                        </label>
                                                    ))}
                                                </div>
                                            ) : (
                                                <input
                                                    type="text"
                                                    value={cpAnswer}
                                                    onChange={(e) => {
                                                        setG12PssScaffoldCheckpointAnswers((prev) => ({ ...(prev || {}), [cpId]: e.target.value }));
                                                        setG12PssScaffoldCheckpointFeedback((prev) => ({ ...(prev || {}), [cpId]: null }));
                                                    }}
                                                    className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                    placeholder="Type your answer"
                                                />
                                            )}

                                            <div className="mt-3 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                <button
                                                    onClick={checkCheckpoint}
                                                    disabled={String(cpAnswer).trim() === ''}
                                                    className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                                >
                                                    Check
                                                </button>
                                                {cpFeedback && (
                                                    <div className={`text-sm ${cpFeedback.isCorrect ? 'text-green-700' : 'text-red-700'}`}>
                                                        {cpFeedback.isCorrect ? 'Correct.' : `Incorrect. Correct answer: ${cpFeedback.correctAnswer}`}
                                                    </div>
                                                )}
                                            </div>

                                            {cpFeedback?.explanation && (
                                                <div className="mt-3 text-sm text-gray-700 bg-gray-50 border border-gray-200 rounded-lg p-3">
                                                    {renderMathText(cpFeedback.explanation)}
                                                </div>
                                            )}
                                        </div>
                                    )
                                ) : (
                                    <>
                                        <div className="mb-3">
                                            <label className="block text-sm font-semibold text-gray-700 mb-1">Your answer</label>
                                            <input
                                                type="text"
                                                value={g12PssScaffoldAnswer}
                                                onChange={(e) => {
                                                    setG12PssScaffoldAnswer(e.target.value);
                                                    setG12PssScaffoldFeedback(null);
                                                }}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        </div>

                                        <div className="flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={checkAnswer}
                                                disabled={String(g12PssScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG12PssScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-indigo-50 text-indigo-800 rounded-lg font-semibold border border-indigo-200 hover:bg-indigo-100"
                                            >
                                                {g12PssScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                        </div>

                                        {g12PssScaffoldFeedback && (
                                            <div className={`mt-4 p-4 rounded-lg border ${g12PssScaffoldFeedback.isCorrect ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                                                <div className="font-semibold">{g12PssScaffoldFeedback.isCorrect ? 'Correct!' : 'Not quite.'}</div>
                                                {!g12PssScaffoldFeedback.isCorrect && (
                                                    <div className="mt-1 text-sm"><span className="font-semibold">Correct answer:</span> {renderMathText(g12PssScaffoldFeedback.correctAnswer)}</div>
                                                )}
                                            </div>
                                        )}

                                        {g12PssScaffoldShowHint && question.explanation && (
                                            <div className="mt-3 text-sm text-gray-700 bg-white border border-gray-200 rounded-lg p-3">
                                                {renderMathText(question.explanation)}
                                            </div>
                                        )}
                                    </>
                                )}
                            </>
                        ) : (
                            <div className="text-gray-600">No question loaded yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g12PssVisualAidsOpen} setIsOpen={setG12PssVisualAidsOpen}>
                    {renderGrade12PatternsSequencesSeriesVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade12PatternsSequencesSeriesScaffold;
