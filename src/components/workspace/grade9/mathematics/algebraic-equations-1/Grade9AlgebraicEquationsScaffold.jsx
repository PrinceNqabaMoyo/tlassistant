import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const normalizeEqAnswer = (value) => {
    if (value === null || value === undefined) return '';
    return String(value)
        .trim()
        .replace(/−/g, '-')
        .replace(/\s+/g, '')
        .toLowerCase();
};

const normalizeYesNo = (value) => {
    const s = String(value ?? '').trim().toLowerCase();
    if (s === 'y') return 'yes';
    if (s === 'n') return 'no';
    return s;
};

const Grade9AlgebraicEquationsScaffold = ({
    onBack,
    scaffoldSteps,
    g9AlgEqVisualAidsOpen,
    setG9AlgEqVisualAidsOpen,
    g9AlgEqScaffoldDifficulty,
    setG9AlgEqScaffoldDifficulty,
    g9AlgEqScaffoldStepIndex,
    setG9AlgEqScaffoldStepIndex,
    fetchGrade9AlgEqScaffoldQuestion,
    g9AlgEqScaffoldLoading,
    g9AlgEqScaffoldError,
    g9AlgEqScaffoldQuestion,
    g9AlgEqScaffoldShowHint,
    setG9AlgEqScaffoldShowHint,
    g9AlgEqScaffoldAnswer,
    setG9AlgEqScaffoldAnswer,
    g9AlgEqScaffoldFeedback,
    setG9AlgEqScaffoldFeedback,
    g9AlgEqScaffoldCheckpointIndex,
    setG9AlgEqScaffoldCheckpointIndex,
    g9AlgEqScaffoldCheckpointAnswers,
    setG9AlgEqScaffoldCheckpointAnswers,
    g9AlgEqScaffoldCheckpointFeedback,
    setG9AlgEqScaffoldCheckpointFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade9AlgEqVisualAids,
}) => {
    const currentStep = scaffoldSteps?.[g9AlgEqScaffoldStepIndex] || scaffoldSteps?.[0];

    const question = g9AlgEqScaffoldQuestion;
    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g9AlgEqScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];

    const getNormalizerFor = (rawAnswer) => {
        const s = String(rawAnswer ?? '').trim();
        if (!s) return normalizeTextAnswer;

        if (/^[-+]?\d+$/.test(s)) return normalizeWholeNumberAnswer;
        if (/^(yes|no)$/i.test(s)) return (v) => normalizeYesNo(normalizeTextAnswer(v));

        return normalizeEqAnswer;
    };

    const checkAnswer = () => {
        if (!question) return;

        const normalize = getNormalizerFor(question.correct_answer);
        const expected = normalize(question.correct_answer);
        const got = normalize(g9AlgEqScaffoldAnswer);

        if (expected && got === expected) {
            setG9AlgEqScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG9AlgEqScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!question || !currentCheckpoint) return;

        const cpId = currentCheckpoint.id;
        const userValue = g9AlgEqScaffoldCheckpointAnswers?.[cpId] ?? '';
        const normalize = getNormalizerFor(currentCheckpoint.correct_answer);
        const expected = normalize(currentCheckpoint.correct_answer);
        const got = normalize(userValue);

        const ok = expected && got === expected;

        setG9AlgEqScaffoldCheckpointFeedback((prev) => ({
            ...(prev || {}),
            [cpId]: ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` },
        }));
    };

    const goNextCheckpoint = () => {
        if (!question || !currentCheckpoint) return;
        const cpId = currentCheckpoint.id;
        const fb = g9AlgEqScaffoldCheckpointFeedback?.[cpId];
        if (!fb || fb.kind !== 'success') return;

        if (cpIndex >= checkpoints.length - 1) {
            setG9AlgEqScaffoldCheckpointIndex(checkpoints.length);
        } else {
            setG9AlgEqScaffoldCheckpointIndex(cpIndex + 1);
        }
    };

    const setCheckpointAnswer = (cpId, value) => {
        setG9AlgEqScaffoldCheckpointAnswers((prev) => ({ ...(prev || {}), [cpId]: value }));
        setG9AlgEqScaffoldCheckpointFeedback((prev) => ({ ...(prev || {}), [cpId]: null }));
    };

    const newExample = () => {
        const step = scaffoldSteps[g9AlgEqScaffoldStepIndex] || scaffoldSteps[0];
        fetchGrade9AlgEqScaffoldQuestion({ subskill: step.key, difficulty: g9AlgEqScaffoldDifficulty });
    };

    const resetForNewStep = (nextIndex) => {
        setG9AlgEqScaffoldStepIndex(nextIndex);
        setG9AlgEqScaffoldShowHint(false);
        setG9AlgEqScaffoldAnswer('');
        setG9AlgEqScaffoldFeedback(null);
        setG9AlgEqScaffoldCheckpointIndex(0);
        setG9AlgEqScaffoldCheckpointAnswers({});
        setG9AlgEqScaffoldCheckpointFeedback({});
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Algebraic equations 1 • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g9AlgEqVisualAidsOpen && (
                                <button
                                    onClick={() => setG9AlgEqVisualAidsOpen(true)}
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
                                value={g9AlgEqScaffoldDifficulty}
                                onChange={(e) => {
                                    setG9AlgEqScaffoldDifficulty(e.target.value);
                                    setG9AlgEqScaffoldShowHint(false);
                                    setG9AlgEqScaffoldAnswer('');
                                    setG9AlgEqScaffoldFeedback(null);
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
                                value={g9AlgEqScaffoldStepIndex}
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

                    {g9AlgEqScaffoldError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g9AlgEqScaffoldError}</div>
                    )}

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <h3 className="text-lg font-bold text-gray-900">Question</h3>
                            <div className="flex gap-2">
                                <button
                                    onClick={newExample}
                                    className="px-3 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold"
                                    disabled={g9AlgEqScaffoldLoading}
                                >
                                    New Question
                                </button>
                                <button
                                    onClick={() => setG9AlgEqScaffoldShowHint((p) => !p)}
                                    className="px-3 py-2 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-800 text-sm font-semibold"
                                    disabled={!question}
                                >
                                    {g9AlgEqScaffoldShowHint ? 'Hide hint' : 'Show hint'}
                                </button>
                            </div>
                        </div>

                        <div className="p-4 border border-gray-200 rounded-lg bg-gray-50">
                            {g9AlgEqScaffoldLoading && (
                                <div className="text-sm text-gray-600">Loading…</div>
                            )}
                            {!g9AlgEqScaffoldLoading && question && (
                                <div className="text-gray-900 whitespace-pre-wrap">{question.question}</div>
                            )}
                            {!g9AlgEqScaffoldLoading && !question && (
                                <div className="text-sm text-gray-600">Select a step and click “New Question”.</div>
                            )}
                        </div>

                        {g9AlgEqScaffoldShowHint && question?.explanation && (
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
                                        value={g9AlgEqScaffoldCheckpointAnswers?.[currentCheckpoint?.id] ?? ''}
                                        onChange={(e) => setCheckpointAnswer(currentCheckpoint?.id, e.target.value)}
                                        className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                        placeholder="Your answer"
                                        disabled={!currentCheckpoint}
                                    />
                                    <button
                                        onClick={checkCheckpoint}
                                        className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                        disabled={!currentCheckpoint}
                                    >
                                        Check
                                    </button>
                                    <button
                                        onClick={goNextCheckpoint}
                                        className="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg font-semibold"
                                        disabled={!currentCheckpoint}
                                    >
                                        Next
                                    </button>
                                </div>

                                {currentCheckpoint?.id && g9AlgEqScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                    <div className={`mt-3 p-3 rounded-lg text-sm ${g9AlgEqScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                        {g9AlgEqScaffoldCheckpointFeedback[currentCheckpoint.id].message}
                                    </div>
                                )}
                            </div>
                        </div>
                    )}

                    <div className="border-t border-gray-200 pt-6">
                        <h3 className="text-lg font-bold text-gray-900 mb-2">Final Answer</h3>
                        <div className="flex flex-col sm:flex-row gap-2">
                            <input
                                type="text"
                                value={g9AlgEqScaffoldAnswer}
                                onChange={(e) => {
                                    setG9AlgEqScaffoldAnswer(e.target.value);
                                    setG9AlgEqScaffoldFeedback(null);
                                }}
                                className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                placeholder="Type your final answer"
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

                        {g9AlgEqScaffoldFeedback && (
                            <div className={`mt-3 p-3 rounded-lg text-sm ${g9AlgEqScaffoldFeedback.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                {g9AlgEqScaffoldFeedback.message}
                            </div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g9AlgEqVisualAidsOpen} setIsOpen={setG9AlgEqVisualAidsOpen}>
                    {renderGrade9AlgEqVisualAids?.()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade9AlgebraicEquationsScaffold;
