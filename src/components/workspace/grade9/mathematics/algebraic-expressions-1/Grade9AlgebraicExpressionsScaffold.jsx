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

const Grade9AlgebraicExpressionsScaffold = ({
    onBack,
    scaffoldSteps,
    g9AlgExpVisualAidsOpen,
    setG9AlgExpVisualAidsOpen,
    g9AlgExpScaffoldDifficulty,
    setG9AlgExpScaffoldDifficulty,
    g9AlgExpScaffoldStepIndex,
    setG9AlgExpScaffoldStepIndex,
    fetchGrade9AlgExpScaffoldQuestion,
    g9AlgExpScaffoldLoading,
    g9AlgExpScaffoldError,
    g9AlgExpScaffoldQuestion,
    g9AlgExpScaffoldShowHint,
    setG9AlgExpScaffoldShowHint,
    g9AlgExpScaffoldAnswer,
    setG9AlgExpScaffoldAnswer,
    g9AlgExpScaffoldFeedback,
    setG9AlgExpScaffoldFeedback,
    g9AlgExpScaffoldCheckpointIndex,
    setG9AlgExpScaffoldCheckpointIndex,
    g9AlgExpScaffoldCheckpointAnswers,
    setG9AlgExpScaffoldCheckpointAnswers,
    g9AlgExpScaffoldCheckpointFeedback,
    setG9AlgExpScaffoldCheckpointFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade9AlgExpVisualAids,
}) => {
    const currentStep = scaffoldSteps?.[g9AlgExpScaffoldStepIndex] || scaffoldSteps?.[0];

    const question = g9AlgExpScaffoldQuestion;
    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g9AlgExpScaffoldCheckpointIndex) || 0));
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
        const got = normalize(g9AlgExpScaffoldAnswer);

        if (expected && got === expected) {
            setG9AlgExpScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG9AlgExpScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!question || !currentCheckpoint) return;

        const cpId = currentCheckpoint.id;
        const userValue = g9AlgExpScaffoldCheckpointAnswers?.[cpId] ?? '';
        const normalize = getNormalizerFor(currentCheckpoint.correct_answer);
        const expected = normalize(currentCheckpoint.correct_answer);
        const got = normalize(userValue);

        const ok = expected && got === expected;

        setG9AlgExpScaffoldCheckpointFeedback((prev) => ({
            ...(prev || {}),
            [cpId]: ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` },
        }));
    };

    const goNextCheckpoint = () => {
        if (!question || !currentCheckpoint) return;
        const cpId = currentCheckpoint.id;
        const fb = g9AlgExpScaffoldCheckpointFeedback?.[cpId];
        if (!fb || fb.kind !== 'success') return;

        if (cpIndex >= checkpoints.length - 1) {
            setG9AlgExpScaffoldCheckpointIndex(checkpoints.length);
        } else {
            setG9AlgExpScaffoldCheckpointIndex(cpIndex + 1);
        }
    };

    const setCheckpointAnswer = (cpId, value) => {
        setG9AlgExpScaffoldCheckpointAnswers((prev) => ({ ...(prev || {}), [cpId]: value }));
        setG9AlgExpScaffoldCheckpointFeedback((prev) => ({ ...(prev || {}), [cpId]: null }));
    };

    const newExample = () => {
        const step = scaffoldSteps[g9AlgExpScaffoldStepIndex] || scaffoldSteps[0];
        fetchGrade9AlgExpScaffoldQuestion({ subskill: step.key, difficulty: g9AlgExpScaffoldDifficulty });
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Algebraic expressions 1 • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g9AlgExpVisualAidsOpen && (
                                <button
                                    onClick={() => setG9AlgExpVisualAidsOpen(true)}
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
                                value={g9AlgExpScaffoldDifficulty}
                                onChange={(e) => setG9AlgExpScaffoldDifficulty(e.target.value)}
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
                                value={g9AlgExpScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG9AlgExpScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG9AlgExpScaffoldFeedback(null);
                                    setG9AlgExpScaffoldShowHint(false);
                                    setG9AlgExpScaffoldCheckpointIndex(0);
                                    setG9AlgExpScaffoldCheckpointAnswers({});
                                    setG9AlgExpScaffoldCheckpointFeedback({});
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {scaffoldSteps.map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={newExample}
                                disabled={g9AlgExpScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g9AlgExpScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="mb-4">
                        <div className="text-sm font-semibold text-gray-800">Step {g9AlgExpScaffoldStepIndex + 1} / {scaffoldSteps.length}: {currentStep?.title}</div>
                        <div className="text-sm text-gray-600">{currentStep?.prompt}</div>
                    </div>

                    {g9AlgExpScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">{g9AlgExpScaffoldError}</div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g9AlgExpScaffoldLoading && !question ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : question ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{question.question}</div>

                                {question.question_type === 'scaffold' ? (
                                    <>
                                        {Array.isArray(question.steps) && (
                                            <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                    {question.steps.map((s, idx) => (
                                                        <li key={`${idx}_${s}`} className={idx === Math.min(cpIndex, question.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}>{s}</li>
                                                    ))}
                                                </ol>
                                            </div>
                                        )}

                                        {cpIndex < checkpoints.length && currentCheckpoint ? (
                                            <div className="bg-white border border-gray-200 rounded-lg p-4">
                                                <div className="text-sm font-semibold text-gray-800 mb-2">Checkpoint {cpIndex + 1} / {checkpoints.length}</div>
                                                <div className="text-gray-800 font-medium mb-3">{currentCheckpoint.prompt}</div>

                                                <input
                                                    type="text"
                                                    value={g9AlgExpScaffoldCheckpointAnswers?.[currentCheckpoint.id] ?? ''}
                                                    onChange={(e) => setCheckpointAnswer(currentCheckpoint.id, e.target.value)}
                                                    className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                    placeholder="Type your answer"
                                                />

                                                <div className="mt-4 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                    <button
                                                        onClick={checkCheckpoint}
                                                        disabled={String(g9AlgExpScaffoldCheckpointAnswers?.[currentCheckpoint.id] ?? '').trim() === ''}
                                                        className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                                    >
                                                        Check
                                                    </button>
                                                    <button
                                                        onClick={() => setG9AlgExpScaffoldShowHint((p) => !p)}
                                                        className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                                    >
                                                        {g9AlgExpScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                                    </button>
                                                    <button
                                                        onClick={goNextCheckpoint}
                                                        disabled={g9AlgExpScaffoldCheckpointFeedback?.[currentCheckpoint.id]?.kind !== 'success'}
                                                        className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400"
                                                    >
                                                        Next
                                                    </button>
                                                </div>

                                                {g9AlgExpScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                                    <div className={`mt-4 p-4 rounded-lg border text-sm ${g9AlgExpScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'border-green-200 bg-green-50 text-green-800' : 'border-red-200 bg-red-50 text-red-800'}`}>
                                                        <div className="font-semibold">{g9AlgExpScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'Correct' : 'Incorrect'}</div>
                                                        {g9AlgExpScaffoldShowHint && currentCheckpoint.explanation && (
                                                            <div className="mt-2">{currentCheckpoint.explanation}</div>
                                                        )}
                                                    </div>
                                                )}
                                            </div>
                                        ) : (
                                            <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                                                <div className="font-semibold text-green-900">Done!</div>
                                                <div className="text-sm text-green-800 mt-1">Final answer: <span className="font-semibold">{question.correct_answer}</span></div>
                                            </div>
                                        )}
                                    </>
                                ) : (
                                    <>
                                        <div className="mb-4">
                                            <label className="block text-sm font-semibold text-gray-700 mb-1">Your answer</label>
                                            <input
                                                type="text"
                                                value={g9AlgExpScaffoldAnswer}
                                                onChange={(e) => {
                                                    setG9AlgExpScaffoldAnswer(e.target.value);
                                                    setG9AlgExpScaffoldFeedback(null);
                                                }}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        </div>
                                        <div className="flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={checkAnswer}
                                                disabled={String(g9AlgExpScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG9AlgExpScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                            >
                                                {g9AlgExpScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                        </div>

                                        {g9AlgExpScaffoldFeedback && (
                                            <div className={`mt-4 p-4 rounded-lg border text-sm ${g9AlgExpScaffoldFeedback.kind === 'success' ? 'border-green-200 bg-green-50 text-green-800' : 'border-red-200 bg-red-50 text-red-800'}`}>
                                                <div className="font-semibold">{g9AlgExpScaffoldFeedback.kind === 'success' ? 'Correct' : 'Incorrect'}</div>
                                                {g9AlgExpScaffoldFeedback.kind !== 'success' && (
                                                    <div className="mt-1"><span className="font-semibold">Correct answer:</span> {question.correct_answer}</div>
                                                )}
                                            </div>
                                        )}
                                    </>
                                )}
                            </>
                        ) : (
                            <div className="text-gray-600">No question yet.</div>
                        )}
                    </div>
                </div>

                <VisualAidsPanel isOpen={g9AlgExpVisualAidsOpen} setIsOpen={setG9AlgExpVisualAidsOpen}>
                    {renderGrade9AlgExpVisualAids()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade9AlgebraicExpressionsScaffold;
