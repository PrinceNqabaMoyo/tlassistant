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

const Grade10AlgebraicExpressionsScaffold = ({
    onBack,
    scaffoldSteps,
    g10AlgExpVisualAidsOpen,
    setG10AlgExpVisualAidsOpen,
    g10AlgExpScaffoldDifficulty,
    setG10AlgExpScaffoldDifficulty,
    g10AlgExpScaffoldStepIndex,
    setG10AlgExpScaffoldStepIndex,
    fetchGrade10AlgExpScaffoldQuestion,
    g10AlgExpScaffoldLoading,
    g10AlgExpScaffoldError,
    g10AlgExpScaffoldQuestion,
    g10AlgExpScaffoldShowHint,
    setG10AlgExpScaffoldShowHint,
    g10AlgExpScaffoldAnswer,
    setG10AlgExpScaffoldAnswer,
    g10AlgExpScaffoldFeedback,
    setG10AlgExpScaffoldFeedback,
    g10AlgExpScaffoldCheckpointIndex,
    setG10AlgExpScaffoldCheckpointIndex,
    g10AlgExpScaffoldCheckpointAnswers,
    setG10AlgExpScaffoldCheckpointAnswers,
    g10AlgExpScaffoldCheckpointFeedback,
    setG10AlgExpScaffoldCheckpointFeedback,
    normalizeWholeNumberAnswer,
    normalizeTextAnswer,
    renderGrade10AlgExpVisualAids,
}) => {
    const currentStep = scaffoldSteps?.[g10AlgExpScaffoldStepIndex] || scaffoldSteps?.[0];

    const question = g10AlgExpScaffoldQuestion;
    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g10AlgExpScaffoldCheckpointIndex) || 0));
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
        const got = normalize(g10AlgExpScaffoldAnswer);

        if (expected && got === expected) {
            setG10AlgExpScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG10AlgExpScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!question || !currentCheckpoint) return;

        const cpId = currentCheckpoint.id;
        const userValue = g10AlgExpScaffoldCheckpointAnswers?.[cpId] ?? '';
        const normalize = getNormalizerFor(currentCheckpoint.correct_answer);
        const expected = normalize(currentCheckpoint.correct_answer);
        const got = normalize(userValue);

        const ok = expected && got === expected;

        setG10AlgExpScaffoldCheckpointFeedback((prev) => ({
            ...(prev || {}),
            [cpId]: ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` },
        }));
    };

    const goNextCheckpoint = () => {
        if (!question || !currentCheckpoint) return;
        const cpId = currentCheckpoint.id;
        const fb = g10AlgExpScaffoldCheckpointFeedback?.[cpId];
        if (!fb || fb.kind !== 'success') return;

        if (cpIndex >= checkpoints.length - 1) {
            setG10AlgExpScaffoldCheckpointIndex(checkpoints.length);
        } else {
            setG10AlgExpScaffoldCheckpointIndex(cpIndex + 1);
        }
    };

    const setCheckpointAnswer = (cpId, value) => {
        setG10AlgExpScaffoldCheckpointAnswers((prev) => ({ ...(prev || {}), [cpId]: value }));
        setG10AlgExpScaffoldCheckpointFeedback((prev) => ({ ...(prev || {}), [cpId]: null }));
    };

    const newExample = () => {
        const step = scaffoldSteps[g10AlgExpScaffoldStepIndex] || scaffoldSteps[0];
        fetchGrade10AlgExpScaffoldQuestion({ subskill: step.key, difficulty: g10AlgExpScaffoldDifficulty });
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 10 Mathematics • Algebraic expressions • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
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
                                value={g10AlgExpScaffoldDifficulty}
                                onChange={(e) => setG10AlgExpScaffoldDifficulty(e.target.value)}
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
                                value={g10AlgExpScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG10AlgExpScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG10AlgExpScaffoldFeedback(null);
                                    setG10AlgExpScaffoldShowHint(false);
                                    setG10AlgExpScaffoldCheckpointIndex(0);
                                    setG10AlgExpScaffoldCheckpointAnswers({});
                                    setG10AlgExpScaffoldCheckpointFeedback({});
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
                                disabled={g10AlgExpScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g10AlgExpScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="mb-4">
                        <div className="text-sm font-semibold text-gray-800">Step {g10AlgExpScaffoldStepIndex + 1} / {scaffoldSteps.length}: {currentStep?.title}</div>
                        <div className="text-sm text-gray-600">{currentStep?.prompt}</div>
                    </div>

                    {g10AlgExpScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">{g10AlgExpScaffoldError}</div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g10AlgExpScaffoldLoading && !question ? (
                            <div className="text-gray-600">Loading question…</div>
                        ) : question ? (
                            <>
                                <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                <div className="text-gray-800 font-medium mb-4">{renderMathText(question.question)}</div>

                                {question.question_type === 'scaffold' ? (
                                    <>
                                        {Array.isArray(question.steps) && (
                                            <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                                <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                                <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                                    {question.steps.map((s, idx) => (
                                                        <li key={`${idx}_${s}`} className={idx === Math.min(cpIndex, question.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}>{renderMathText(s)}</li>
                                                    ))}
                                                </ol>
                                            </div>
                                        )}

                                        {currentCheckpoint && cpIndex < checkpoints.length ? (
                                            <div className="bg-white border border-gray-200 rounded-lg p-4">
                                                <div className="font-semibold text-gray-900 mb-2">{renderMathText(currentCheckpoint.prompt)}</div>
                                                <div className="flex flex-col sm:flex-row gap-2">
                                                    <input
                                                        type="text"
                                                        value={g10AlgExpScaffoldCheckpointAnswers?.[currentCheckpoint.id] ?? ''}
                                                        onChange={(e) => setCheckpointAnswer(currentCheckpoint.id, e.target.value)}
                                                        className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                                        placeholder="Your answer"
                                                    />
                                                    <button
                                                        onClick={checkCheckpoint}
                                                        className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700"
                                                    >
                                                        Check
                                                    </button>
                                                    <button
                                                        onClick={goNextCheckpoint}
                                                        className="px-4 py-2 bg-gray-100 text-gray-800 rounded-lg font-semibold hover:bg-gray-200"
                                                    >
                                                        Next
                                                    </button>
                                                </div>
                                                {g10AlgExpScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                                    <div className={`mt-3 p-3 rounded-lg text-sm ${g10AlgExpScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                                        {renderMathText(g10AlgExpScaffoldCheckpointFeedback[currentCheckpoint.id].message)}
                                                    </div>
                                                )}
                                            </div>
                                        ) : null}
                                    </>
                                ) : null}

                                {g10AlgExpScaffoldShowHint && question?.explanation && (
                                    <div className="mt-4 p-3 bg-indigo-50 border border-indigo-200 rounded-lg text-indigo-900 text-sm whitespace-pre-wrap">{question.explanation}</div>
                                )}

                                <div className="mt-6">
                                    <label className="block text-sm font-semibold text-gray-700 mb-1">Your Answer</label>
                                    <div className="flex flex-col sm:flex-row gap-2">
                                        <input
                                            type="text"
                                            value={g10AlgExpScaffoldAnswer}
                                            onChange={(e) => setG10AlgExpScaffoldAnswer(e.target.value)}
                                            className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                            placeholder="Type your answer"
                                        />
                                        <button
                                            onClick={checkAnswer}
                                            className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700"
                                        >
                                            Check
                                        </button>
                                        <button
                                            onClick={() => setG10AlgExpScaffoldShowHint((p) => !p)}
                                            className="px-4 py-2 bg-gray-100 text-gray-800 rounded-lg font-semibold hover:bg-gray-200"
                                        >
                                            {g10AlgExpScaffoldShowHint ? 'Hide hint' : 'Show hint'}
                                        </button>
                                    </div>
                                </div>
                            </>
                        ) : (
                            <div className="text-gray-600">Click “New Example” to start.</div>
                        )}
                    </div>

                    {g10AlgExpScaffoldFeedback && (
                        <div className={`mt-4 p-3 rounded-lg text-sm ${g10AlgExpScaffoldFeedback.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                            {renderMathText(g10AlgExpScaffoldFeedback.message)}
                        </div>
                    )}
                </div>

                {g10AlgExpVisualAidsOpen && (
                    <VisualAidsPanel onClose={() => setG10AlgExpVisualAidsOpen(false)}>
                        {renderGrade10AlgExpVisualAids?.()}
                    </VisualAidsPanel>
                )}
            </div>
        </div>
    );
};

export default Grade10AlgebraicExpressionsScaffold;
