import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';

const _gcd = (a, b) => {
    let x = Math.abs(Number(a) || 0);
    let y = Math.abs(Number(b) || 0);
    while (y) {
        const t = x % y;
        x = y;
        y = t;
    }
    return x || 1;
};

const normalizeFractionAnswer = (value) => {
    const s0 = String(value ?? '').trim();
    if (!s0) return '';

    const s = s0.replace(/\s+/g, ' ');

    // integer
    if (/^[-+]?\d+$/.test(s)) return String(Number(s));

    // mixed number: "a b/c" (a can be negative)
    const mixedMatch = s.match(/^([-+]?\d+)\s+(\d+)\/(\d+)$/);
    if (mixedMatch) {
        const whole = Number(mixedMatch[1]);
        const n = Number(mixedMatch[2]);
        const d = Number(mixedMatch[3]);
        if (!Number.isFinite(whole) || !Number.isFinite(n) || !Number.isFinite(d) || d === 0) return s0;
        const sign = whole < 0 ? -1 : 1;
        const absWhole = Math.abs(whole);
        const num = sign * (absWhole * d + n);
        const g = _gcd(num, d);
        const nn = num / g;
        const dd = d / g;
        return dd === 1 ? String(nn) : `${nn}/${dd}`;
    }

    // fraction: "a/b" (a can be negative)
    const fracMatch = s.match(/^([-+]?\d+)\/(\d+)$/);
    if (fracMatch) {
        const n = Number(fracMatch[1]);
        const d = Number(fracMatch[2]);
        if (!Number.isFinite(n) || !Number.isFinite(d) || d === 0) return s0;
        const g = _gcd(n, d);
        const nn = n / g;
        const dd = d / g;
        return dd === 1 ? String(nn) : `${nn}/${dd}`;
    }

    return s0;
};

const Grade9FractionsScaffold = ({
    onBack,
    scaffoldSteps,
    g9FracVisualAidsOpen,
    setG9FracVisualAidsOpen,
    g9FracScaffoldDifficulty,
    setG9FracScaffoldDifficulty,
    g9FracScaffoldStepIndex,
    setG9FracScaffoldStepIndex,
    fetchGrade9FractionsScaffoldQuestion,
    g9FracScaffoldLoading,
    g9FracScaffoldError,
    g9FracScaffoldQuestion,
    g9FracScaffoldShowHint,
    setG9FracScaffoldShowHint,
    g9FracScaffoldAnswer,
    setG9FracScaffoldAnswer,
    g9FracScaffoldFeedback,
    setG9FracScaffoldFeedback,
    g9FracScaffoldCheckpointIndex,
    setG9FracScaffoldCheckpointIndex,
    g9FracScaffoldCheckpointAnswers,
    setG9FracScaffoldCheckpointAnswers,
    g9FracScaffoldCheckpointFeedback,
    setG9FracScaffoldCheckpointFeedback,
    renderGrade9FractionsVisualAids,
}) => {
    const currentStep = scaffoldSteps?.[g9FracScaffoldStepIndex] || scaffoldSteps?.[0];
    const question = g9FracScaffoldQuestion;

    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g9FracScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];

    const requestNew = () => {
        if (!currentStep) return;
        fetchGrade9FractionsScaffoldQuestion({ subskill: currentStep.key, difficulty: g9FracScaffoldDifficulty });
    };

    const checkAnswer = () => {
        if (!question) return;
        const expected = normalizeFractionAnswer(question.correct_answer);
        const got = normalizeFractionAnswer(g9FracScaffoldAnswer);
        if (expected && got === expected) {
            setG9FracScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG9FracScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!currentCheckpoint) return;

        const answers = { ...(g9FracScaffoldCheckpointAnswers || {}) };
        const feedback = { ...(g9FracScaffoldCheckpointFeedback || {}) };

        const userValue = answers[currentCheckpoint.id] ?? '';
        const expected = normalizeFractionAnswer(currentCheckpoint.correct_answer);
        const got = normalizeFractionAnswer(userValue);

        if (expected && got === expected) {
            feedback[currentCheckpoint.id] = { kind: 'success', message: 'Correct.' };
        } else {
            feedback[currentCheckpoint.id] = { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` };
        }

        setG9FracScaffoldCheckpointFeedback(feedback);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 9 Mathematics • Fractions • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step method practice with checkpoints. No calculator.</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g9FracVisualAidsOpen && (
                                <button
                                    onClick={() => setG9FracVisualAidsOpen(true)}
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
                                value={g9FracScaffoldDifficulty}
                                onChange={(e) => setG9FracScaffoldDifficulty(e.target.value)}
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
                                value={g9FracScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG9FracScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG9FracScaffoldFeedback(null);
                                    setG9FracScaffoldShowHint(false);
                                    setG9FracScaffoldCheckpointIndex(0);
                                    setG9FracScaffoldCheckpointAnswers({});
                                    setG9FracScaffoldCheckpointFeedback({});
                                }}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                {(scaffoldSteps || []).map((s, idx) => (
                                    <option key={s.key} value={idx}>{s.title}</option>
                                ))}
                            </select>
                        </div>
                    </div>

                    {g9FracScaffoldError && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{g9FracScaffoldError}</div>
                    )}

                    <div className="mb-4">
                        <div className="flex items-center justify-between mb-2">
                            <h3 className="text-lg font-bold text-gray-900">Question</h3>
                            <div className="flex gap-2">
                                <button
                                    onClick={requestNew}
                                    className="px-3 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold"
                                    disabled={g9FracScaffoldLoading}
                                >
                                    New Question
                                </button>
                                <button
                                    onClick={() => setG9FracScaffoldShowHint((p) => !p)}
                                    className="px-3 py-2 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-800 text-sm font-semibold"
                                    disabled={!question}
                                >
                                    {g9FracScaffoldShowHint ? 'Hide hint' : 'Show hint'}
                                </button>
                            </div>
                        </div>

                        <div className="p-4 border border-gray-200 rounded-lg bg-gray-50">
                            {g9FracScaffoldLoading && <div className="text-sm text-gray-600">Loading…</div>}
                            {!g9FracScaffoldLoading && question && (
                                <div className="text-gray-900 whitespace-pre-wrap">{question.question}</div>
                            )}
                            {!g9FracScaffoldLoading && !question && (
                                <div className="text-sm text-gray-600">Select a subskill and click “New Question”.</div>
                            )}
                        </div>

                        {g9FracScaffoldShowHint && question?.explanation && (
                            <div className="mt-3 p-3 bg-indigo-50 border border-indigo-200 rounded-lg text-indigo-900 text-sm whitespace-pre-wrap">{question.explanation}</div>
                        )}
                    </div>

                    {question?.question_type === 'scaffold' && checkpoints.length > 0 && (
                        <div className="mb-6">
                            <div className="flex items-center justify-between mb-2">
                                <h3 className="text-lg font-bold text-gray-900">Checkpoints</h3>
                                <div className="text-sm text-gray-600">{cpIndex + 1} / {checkpoints.length}</div>
                            </div>

                            {Array.isArray(question?.steps) && (
                                <div className="mb-4 bg-white border border-gray-200 rounded-lg p-3">
                                    <div className="text-sm font-semibold text-gray-800 mb-2">Method steps</div>
                                    <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                        {question.steps.map((s, idx) => (
                                            <li
                                                key={`${idx}_${s}`}
                                                className={idx === Math.min(cpIndex, question.steps.length - 1) ? 'font-semibold text-indigo-700' : ''}
                                            >
                                                {s}
                                            </li>
                                        ))}
                                    </ol>
                                </div>
                            )}

                            <div className="p-4 border border-gray-200 rounded-lg bg-white">
                                <div className="font-semibold text-gray-900 mb-2">{currentCheckpoint?.prompt}</div>

                                <div className="flex flex-col sm:flex-row gap-2">
                                    <input
                                        type="text"
                                        value={(g9FracScaffoldCheckpointAnswers || {})[currentCheckpoint.id] ?? ''}
                                        onChange={(e) => {
                                            const next = { ...(g9FracScaffoldCheckpointAnswers || {}) };
                                            next[currentCheckpoint.id] = e.target.value;
                                            setG9FracScaffoldCheckpointAnswers(next);
                                        }}
                                        className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
                                        placeholder="Your answer (e.g. 3/4 or 1 1/2)"
                                    />
                                    <button
                                        onClick={checkCheckpoint}
                                        className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-semibold"
                                    >
                                        Check
                                    </button>
                                </div>

                                {g9FracScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                    <div className={`mt-3 p-3 rounded-lg text-sm ${g9FracScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                        {g9FracScaffoldCheckpointFeedback[currentCheckpoint.id].message}
                                    </div>
                                )}

                                <div className="mt-4 flex items-center justify-between">
                                    <button
                                        onClick={() => setG9FracScaffoldCheckpointIndex(Math.max(0, cpIndex - 1))}
                                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                        disabled={cpIndex === 0}
                                    >
                                        Previous
                                    </button>
                                    <button
                                        onClick={() => setG9FracScaffoldCheckpointIndex(Math.min(cpIndex + 1, checkpoints.length - 1))}
                                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-semibold"
                                        disabled={cpIndex >= checkpoints.length - 1}
                                    >
                                        Next
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    {question && (
                        <div className="mb-6">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Your Answer</label>
                            <div className="flex flex-col sm:flex-row gap-2">
                                <input
                                    type="text"
                                    value={g9FracScaffoldAnswer}
                                    onChange={(e) => setG9FracScaffoldAnswer(e.target.value)}
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

                    {g9FracScaffoldFeedback && (
                        <div className={`mb-6 p-3 rounded-lg text-sm ${g9FracScaffoldFeedback.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                            {g9FracScaffoldFeedback.message}
                        </div>
                    )}
                </div>

                {g9FracVisualAidsOpen && (
                    <VisualAidsPanel onClose={() => setG9FracVisualAidsOpen(false)}>
                        {renderGrade9FractionsVisualAids?.()}
                    </VisualAidsPanel>
                )}
            </div>
        </div>
    );
};

export default Grade9FractionsScaffold;
