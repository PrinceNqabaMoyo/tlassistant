import React from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

const normalizeTrigAnswer = (value) => {
    if (value === null || value === undefined) return '';
    return String(value)
        .trim()
        .replace(/−/g, '-')
        .replace(/\s+/g, '')
        .toLowerCase();
};

const Grade10Trigonometry1Scaffold = ({
    onBack,
    scaffoldSteps,
    g10Trig1VisualAidsOpen,
    setG10Trig1VisualAidsOpen,
    g10Trig1ScaffoldDifficulty,
    setG10Trig1ScaffoldDifficulty,
    g10Trig1ScaffoldStepIndex,
    setG10Trig1ScaffoldStepIndex,
    fetchGrade10Trig1ScaffoldQuestion,
    g10Trig1ScaffoldLoading,
    g10Trig1ScaffoldError,
    g10Trig1ScaffoldQuestion,
    g10Trig1ScaffoldCheckpointIndex,
    setG10Trig1ScaffoldCheckpointIndex,
    g10Trig1ScaffoldCheckpointAnswers,
    setG10Trig1ScaffoldCheckpointAnswers,
    g10Trig1ScaffoldCheckpointFeedback,
    setG10Trig1ScaffoldCheckpointFeedback,
    g10Trig1ScaffoldAnswer,
    setG10Trig1ScaffoldAnswer,
    g10Trig1ScaffoldFeedback,
    setG10Trig1ScaffoldFeedback,
    g10Trig1ScaffoldShowHint,
    setG10Trig1ScaffoldShowHint,
    renderGrade10Trig1VisualAids,
}) => {
    const question = g10Trig1ScaffoldQuestion;
    const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
    const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g10Trig1ScaffoldCheckpointIndex) || 0));
    const currentCheckpoint = checkpoints[cpIndex];

    const checkAnswer = () => {
        if (!question) return;
        const expected = normalizeTrigAnswer(question.correct_answer);
        const got = normalizeTrigAnswer(g10Trig1ScaffoldAnswer);

        if (expected && got === expected) {
            setG10Trig1ScaffoldFeedback({ kind: 'success', message: 'Correct.' });
        } else {
            setG10Trig1ScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
        }
    };

    const checkCheckpoint = () => {
        if (!question || !currentCheckpoint) return;

        const cpId = currentCheckpoint.id;
        const userValue = g10Trig1ScaffoldCheckpointAnswers?.[cpId] ?? '';
        const expected = normalizeTrigAnswer(currentCheckpoint.correct_answer);
        const got = normalizeTrigAnswer(userValue);

        const ok = expected && got === expected;

        setG10Trig1ScaffoldCheckpointFeedback((prev) => ({
            ...(prev || {}),
            [cpId]: ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` },
        }));
    };

    const goNextCheckpoint = () => {
        if (!question || !currentCheckpoint) return;
        const cpId = currentCheckpoint.id;
        const fb = g10Trig1ScaffoldCheckpointFeedback?.[cpId];
        if (!fb || fb.kind !== 'success') return;

        if (cpIndex >= checkpoints.length - 1) {
            setG10Trig1ScaffoldCheckpointIndex(checkpoints.length);
        } else {
            setG10Trig1ScaffoldCheckpointIndex(cpIndex + 1);
        }
    };

    const setCheckpointAnswer = (cpId, value) => {
        setG10Trig1ScaffoldCheckpointAnswers((prev) => ({ ...(prev || {}), [cpId]: value }));
        setG10Trig1ScaffoldCheckpointFeedback((prev) => ({ ...(prev || {}), [cpId]: null }));
    };

    const newExample = () => {
        const step = scaffoldSteps[g10Trig1ScaffoldStepIndex] || scaffoldSteps[0];
        fetchGrade10Trig1ScaffoldQuestion({ subskill: step.key, difficulty: g10Trig1ScaffoldDifficulty });
    };

    const isDone = question?.question_type === 'scaffold' && checkpoints.length > 0
        ? (Number(g10Trig1ScaffoldCheckpointIndex) || 0) >= checkpoints.length
        : false;

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="flex gap-4">
                <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <div>
                            <h2 className="text-2xl font-bold text-gray-900">Grade 10 Mathematics • Trigonometry 1 • Scaffold</h2>
                            <p className="text-sm text-gray-600">Step-by-step practice with checkpoints (includes calculator procedure).</p>
                        </div>
                        <div className="flex items-center gap-2">
                            {!g10Trig1VisualAidsOpen && (
                                <button
                                    onClick={() => setG10Trig1VisualAidsOpen(true)}
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
                                value={g10Trig1ScaffoldDifficulty}
                                onChange={(e) => setG10Trig1ScaffoldDifficulty(e.target.value)}
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
                                value={g10Trig1ScaffoldStepIndex}
                                onChange={(e) => {
                                    const idx = Number(e.target.value);
                                    setG10Trig1ScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                    setG10Trig1ScaffoldFeedback(null);
                                    setG10Trig1ScaffoldShowHint(false);
                                    setG10Trig1ScaffoldCheckpointIndex(0);
                                    setG10Trig1ScaffoldCheckpointAnswers({});
                                    setG10Trig1ScaffoldCheckpointFeedback({});
                                    setG10Trig1ScaffoldAnswer('');
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
                                disabled={g10Trig1ScaffoldLoading}
                                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                            >
                                {g10Trig1ScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    {g10Trig1ScaffoldError && (
                        <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">{g10Trig1ScaffoldError}</div>
                    )}

                    <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                        {g10Trig1ScaffoldLoading && !question ? (
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
                                            <div className="text-gray-900 font-semibold">Finished</div>
                                            {question.explanation && (
                                                <div className="mt-3 text-sm text-gray-700 bg-gray-50 border border-gray-200 rounded-lg p-3">
                                                    {renderMathText(question.explanation)}
                                                </div>
                                            )}
                                        </div>
                                    ) : (
                                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                                            <div className="text-sm font-semibold text-gray-800 mb-2">Checkpoint {cpIndex + 1} / {checkpoints.length}</div>
                                            <div className="text-gray-800 font-medium mb-3">{renderMathText(currentCheckpoint?.prompt || '')}</div>

                                            <input
                                                type="text"
                                                value={g10Trig1ScaffoldCheckpointAnswers?.[currentCheckpoint?.id] ?? ''}
                                                onChange={(e) => setCheckpointAnswer(currentCheckpoint?.id, e.target.value)}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />

                                            <div className="mt-3 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                <button
                                                    onClick={checkCheckpoint}
                                                    disabled={String(g10Trig1ScaffoldCheckpointAnswers?.[currentCheckpoint?.id] ?? '').trim() === ''}
                                                    className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                                >
                                                    Check
                                                </button>
                                                <button
                                                    onClick={goNextCheckpoint}
                                                    className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700"
                                                >
                                                    Next
                                                </button>
                                            </div>

                                            {currentCheckpoint?.id && g10Trig1ScaffoldCheckpointFeedback?.[currentCheckpoint.id] && (
                                                <div className={`mt-3 p-3 rounded-lg text-sm ${g10Trig1ScaffoldCheckpointFeedback[currentCheckpoint.id].kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' : 'bg-red-50 text-red-800 border border-red-200'}`}>
                                                    {renderMathText(g10Trig1ScaffoldCheckpointFeedback[currentCheckpoint.id].message)}
                                                </div>
                                            )}

                                            {currentCheckpoint?.explanation && (
                                                <div className="mt-3 text-sm text-gray-700 bg-gray-50 border border-gray-200 rounded-lg p-3">
                                                    {renderMathText(currentCheckpoint.explanation)}
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
                                                value={g10Trig1ScaffoldAnswer}
                                                onChange={(e) => {
                                                    setG10Trig1ScaffoldAnswer(e.target.value);
                                                    setG10Trig1ScaffoldFeedback(null);
                                                }}
                                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                placeholder="Type your answer"
                                            />
                                        </div>

                                        <div className="flex flex-col sm:flex-row gap-2 sm:items-center">
                                            <button
                                                onClick={checkAnswer}
                                                disabled={String(g10Trig1ScaffoldAnswer).trim() === ''}
                                                className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                            >
                                                Check
                                            </button>
                                            <button
                                                onClick={() => setG10Trig1ScaffoldShowHint((p) => !p)}
                                                className="px-4 py-2 bg-indigo-50 text-indigo-800 rounded-lg font-semibold border border-indigo-200 hover:bg-indigo-100"
                                            >
                                                {g10Trig1ScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                            </button>
                                        </div>

                                        {g10Trig1ScaffoldFeedback && (
                                            <div className={`mt-4 p-4 rounded-lg border ${g10Trig1ScaffoldFeedback.kind === 'success' ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                                                {renderMathText(g10Trig1ScaffoldFeedback.message)}
                                            </div>
                                        )}

                                        {g10Trig1ScaffoldShowHint && question.explanation && (
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

                <VisualAidsPanel isOpen={g10Trig1VisualAidsOpen} setIsOpen={setG10Trig1VisualAidsOpen}>
                    {renderGrade10Trig1VisualAids?.()}
                </VisualAidsPanel>
            </div>
        </div>
    );
};

export default Grade10Trigonometry1Scaffold;
