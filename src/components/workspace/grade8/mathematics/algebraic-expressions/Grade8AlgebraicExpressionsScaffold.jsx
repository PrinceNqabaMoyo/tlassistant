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

const Grade8AlgebraicExpressionsScaffold = ({
    onBack,
    scaffoldSteps,
    g8AlgExpVisualAidsOpen,
    setG8AlgExpVisualAidsOpen,
    g8AlgExpScaffoldDifficulty,
    setG8AlgExpScaffoldDifficulty,
    g8AlgExpScaffoldStepIndex,
    setG8AlgExpScaffoldStepIndex,
    fetchGrade8AlgExpScaffoldQuestion,
    g8AlgExpScaffoldLoading,
    g8AlgExpScaffoldError,
    g8AlgExpScaffoldQuestion,
    g8AlgExpScaffoldShowHint,
    setG8AlgExpScaffoldShowHint,
    g8AlgExpScaffoldAnswer,
    setG8AlgExpScaffoldAnswer,
    g8AlgExpScaffoldFeedback,
    setG8AlgExpScaffoldFeedback,
    g8AlgExpScaffoldCheckpointIndex,
    setG8AlgExpScaffoldCheckpointIndex,
    g8AlgExpScaffoldCheckpointAnswers,
    setG8AlgExpScaffoldCheckpointAnswers,
    g8AlgExpScaffoldCheckpointFeedback,
    setG8AlgExpScaffoldCheckpointFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade8AlgExpVisualAids,
}) => {
    const currentStep = scaffoldSteps?.[g8AlgExpScaffoldStepIndex] || scaffoldSteps?.[0];

    const question = g8AlgExpScaffoldQuestion;
    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g8AlgExpScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];

    const getNormalizerFor = (rawAnswer) => {
        const s = String(rawAnswer ?? '').trim();
        if (!s) return normalizeTextAnswer;

        if (/^[-+]?\d+$/.test(s)) return normalizeWholeNumberAnswer;
        if (/^(yes|no)$/i.test(s)) return (v) => normalizeYesNo(normalizeTextAnswer(v));
        if (/[a-z]/i.test(s) || /\^|\(|\)|\+|\-/.test(s)) return normalizeAlgebraExpr;

        return normalizeTextAnswer;
    };

    const checkAnswer = () => {
        if (!question) return;

        const normalize = getNormalizerFor(question.correct_answer);
        const expected = normalize(question.correct_answer);
        const got = normalize(g8AlgExpScaffoldAnswer);

        if (expected && got === expected) {
            setG8AlgExpScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG8AlgExpScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!currentCheckpoint) return;

        const answers = { ...(g8AlgExpScaffoldCheckpointAnswers || {}) };
        const feedback = { ...(g8AlgExpScaffoldCheckpointFeedback || {}) };

        const userValue = answers[currentCheckpoint.id] ?? '';
        const normalize = getNormalizerFor(currentCheckpoint.correct_answer);
        const expected = normalize(currentCheckpoint.correct_answer);
        const got = normalize(userValue);

        if (expected && got === expected) {
            feedback[currentCheckpoint.id] = { kind: 'success', message: 'Correct.' };
        } else {
            feedback[currentCheckpoint.id] = { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` };
        }

        setG8AlgExpScaffoldCheckpointFeedback(feedback);
    };

    const goNextCheckpoint = () => {
        const next = Math.min(cpIndex + 1, checkpoints.length - 1);
        setG8AlgExpScaffoldCheckpointIndex(next);
    };

    const goPrevCheckpoint = () => {
        const prev = Math.max(0, cpIndex - 1);
        setG8AlgExpScaffoldCheckpointIndex(prev);
    };

    const requestNew = () => {
        if (!currentStep) return;
        fetchGrade8AlgExpScaffoldQuestion({ subskill: currentStep.key, difficulty: g8AlgExpScaffoldDifficulty });
    };

    const resetForNewStep = (nextIndex) => {
        setG8AlgExpScaffoldStepIndex(nextIndex);
        setG8AlgExpScaffoldShowHint(false);
        setG8AlgExpScaffoldAnswer('');
        setG8AlgExpScaffoldFeedback(null);
        setG8AlgExpScaffoldCheckpointIndex(0);
        setG8AlgExpScaffoldCheckpointAnswers({});
        setG8AlgExpScaffoldCheckpointFeedback({});
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 8 Mathematics • Algebraic expressions 1 • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
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

                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-6">
                        <div className="lg:col-span-1">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Difficulty</label>
                            <select
                                value={g8AlgExpScaffoldDifficulty}
                                onChange={(e) => {
                                    setG8AlgExpScaffoldDifficulty(e.target.value);
                                    setG8AlgExpScaffoldShowHint(false);
                                    setG8AlgExpScaffoldAnswer('');
                                    setG8AlgExpScaffoldFeedback(null);
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                        </div>

                        <div className="lg:col-span-2">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Scaffold Step</label>
                            <select
                                value={g8AlgExpScaffoldStepIndex}
                                onChange={(e) => resetForNewStep(Number(e.target.value))}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {(scaffoldSteps || []).map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                            {currentStep?.prompt && <div className="mt-1 text-xs text-gray-500">{currentStep.prompt}</div>}
                        </div>
                    </div>

                    {g8AlgExpScaffoldError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g8AlgExpScaffoldError}</div>
                    )}

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <h3 className="text-lg font-bold text-gray-900">Question</h3>
                            <div className="flex gap-2">
                                <button
                                    onClick={requestNew}
                                    className="px-3 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold"
                                    disabled={g8AlgExpScaffoldLoading}
                                >
                                    New Question
                                </button>
                                <button
                                    onClick={() => setG8AlgExpScaffoldShowHint((p) => !p)}
                                    className="px-3 py-2 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-800 text-sm font-semibold"
                                    disabled={!question}
                                >
                                    {g8AlgExpScaffoldShowHint ? 'Hide hint' : 'Show hint'}
                                </button>
                            </div>
                        </div>

                        <div className="p-4 border border-gray-200 rounded-lg bg-gray-50">
                            {g8AlgExpScaffoldLoading && (
                                <div className="text-sm text-gray-600">Loading…</div>
                            )}
                            {!g8AlgExpScaffoldLoading && question && (
                                <div className="text-gray-900 whitespace-pre-wrap">{question.question}</div>
                            )}
                            {!g8AlgExpScaffoldLoading && !question && (
                                <div className="text-sm text-gray-600">Select a step and click “New Question”.</div>
                            )}
                        </div>

                        {g8AlgExpScaffoldShowHint && question?.explanation && (
                            <div className="mt-3 p-3 bg-indigo-50 border border-indigo-200 rounded-lg text-indigo-900 text-sm whitespace-pre-wrap">{question.explanation}</div>
                        )}
                    </div>

                    {question?.question_type === 'scaffold' && checkpoints.length > 0 && (
                        <div className="mb-6">
                            <div className="flex items-center justify-between mb-2">
                                <h3 className="text-lg font-bold text-gray-900">Checkpoints</h3>
                                <div className="text-sm text-gray-600">{cpIndex + 1} / {checkpoints.length}</div>
                            </div>

                            <div className="p-4 border border-gray-200 rounded-lg bg-white">
                                <div className="font-semibold text-gray-900 mb-2">{currentCheckpoint?.prompt}</div>

                                <div className="flex flex-col sm:flex-row gap-2">
                                    <input
                                        type="text"
                                        value={(g8AlgExpScaffoldCheckpointAnswers || {})[currentCheckpoint.id] ?? ''}
                                        onChange={(e) => {
                                            const next = { ...(g8AlgExpScaffoldCheckpointAnswers || {}) };
                                            next[currentCheckpoint.id] = e.target.value;
                                            setG8AlgExpScaffoldCheckpointAnswers(next);
                                        }}
                                        className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                        placeholder="Your answer"
                                    />
                                    <button
                                        onClick={checkCheckpoint}
                                        className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                    >
                                        Check
                                    </button>
                                </div>

                                {g8AlgExpScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                    <div className={`mt-3 p-3 rounded-lg text-sm ${g8AlgExpScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                        {g8AlgExpScaffoldCheckpointFeedback[currentCheckpoint.id].message}
                                    </div>
                                )}

                                <div className="mt-4 flex items-center justify-between">
                                    <button
                                        onClick={goPrevCheckpoint}
                                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                        disabled={cpIndex === 0}
                                    >
                                        Previous
                                    </button>
                                    <button
                                        onClick={goNextCheckpoint}
                                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                        disabled={cpIndex >= checkpoints.length - 1}
                                    >
                                        Next
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    {question && question?.question_type !== 'mcq' && (
                        <div className="mb-6">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Your Answer</label>
                            <div className="flex flex-col sm:flex-row gap-2">
                                <input
                                    type="text"
                                    value={g8AlgExpScaffoldAnswer}
                                    onChange={(e) => setG8AlgExpScaffoldAnswer(e.target.value)}
                                    className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                    placeholder="Type your answer"
                                    disabled={!question}
                                />
                                <button
                                    onClick={checkAnswer}
                                    className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                    disabled={!question}
                                >
                                    Check
                                </button>
                            </div>
                        </div>
                    )}

                    {question && question?.question_type === 'mcq' && (
                        <div className="mb-6">
                            <div className="text-sm font-semibold text-gray-700 mb-2">Choose one:</div>
                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                {(question.options || []).map((opt) => (
                                    <button
                                        key={opt}
                                        onClick={() => {
                                            setG8AlgExpScaffoldAnswer(String(opt));
                                            setG8AlgExpScaffoldFeedback(null);
                                        }}
                                        className={`px-3 py-2 rounded-lg border text-left ${String(g8AlgExpScaffoldAnswer) === String(opt) ? 'border-indigo-500 bg-indigo-50' : 'border-gray-200 bg-white hover:bg-gray-50'}`}
                                    >
                                        {opt}
                                    </button>
                                ))}
                            </div>
                            <div className="mt-3">
                                <button
                                    onClick={checkAnswer}
                                    className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                    disabled={!question}
                                >
                                    Check
                                </button>
                            </div>
                        </div>
                    )}

                    {g8AlgExpScaffoldFeedback && (
                        <div className={`mb-6 p-3 rounded-lg text-sm ${g8AlgExpScaffoldFeedback.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                            {g8AlgExpScaffoldFeedback.message}
                        </div>
                    )}
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

export default Grade8AlgebraicExpressionsScaffold;
