import React, { useEffect } from 'react';
import MCQOption from '../../../shared/MCQOption';
import { useGrade10AccountingMarking } from '../useGrade10AccountingMarking';

const normalizeText = (v) => v == null ? '' : String(v).trim().replace(/\s+/g, ' ').toLowerCase();

const getWordBank = (question) => Array.isArray(question?.word_bank) ? question.word_bank : [];
const getCorrectMap = (question) => (question?.correct_map && typeof question.correct_map === 'object') ? question.correct_map : {};
const getAnswerPartHints = (question) => Array.isArray(question?.answer_part_hints) ? question.answer_part_hints : [];
const getDerivationMap = (question) => (question?.derivation_map && typeof question.derivation_map === 'object') ? question.derivation_map : {};
const getCellTeachingMap = (question) => (question?.cell_teaching_map && typeof question.cell_teaching_map === 'object') ? question.cell_teaching_map : {};

const buildEmptyWordbankAnswer = (question) => {
    const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
    const selections = {};
    for (let i = 0; i < rows.length; i += 1) {
        selections[String(i)] = { '2': null };
    }
    return { selections, activeTokenId: null };
};

const getUsedTokenIds = (ans) => {
    const selections = ans?.selections && typeof ans.selections === 'object' ? ans.selections : {};
    const used = new Set();
    Object.values(selections).forEach((row) => {
        if (!row) return;
        const v = row['2'];
        if (v) used.add(String(v));
    });
    return used;
};

const Grade10AccountingVATScaffold = ({
    onBack, scaffoldSteps,
    g10AcctVATVisualAidsOpen, setG10AcctVATVisualAidsOpen,
    g10AcctVATScaffoldDifficulty, setG10AcctVATScaffoldDifficulty,
    g10AcctVATScaffoldStepIndex, setG10AcctVATScaffoldStepIndex,
    fetchGrade10AcctVATScaffoldQuestion,
    g10AcctVATScaffoldLoading, g10AcctVATScaffoldError, g10AcctVATScaffoldQuestion,
    g10AcctVATScaffoldAnswer, setG10AcctVATScaffoldAnswer,
    g10AcctVATScaffoldFeedback, setG10AcctVATScaffoldFeedback,
    g10AcctVATScaffoldShowHint, setG10AcctVATScaffoldShowHint,
    renderGrade10AcctVATVisualAids, hideConfig, evaluationState,
}) => {
    const question = g10AcctVATScaffoldQuestion;
    const selectedSubtopic = scaffoldSteps[g10AcctVATScaffoldStepIndex] || scaffoldSteps[0];
    const marking = useGrade10AccountingMarking();
    const [showMemo, setShowMemo] = React.useState(false);
    const calcFormulaHint = String(question?.formula_hint || '').trim();
    const calcDerivationMap = getDerivationMap(question);

    useEffect(() => { marking.setMarkingMode('practice'); }, [g10AcctVATScaffoldStepIndex]);

    useEffect(() => {
        setShowMemo(false);
        if (question?.question_type === 'table_wordbank' && (!g10AcctVATScaffoldAnswer || typeof g10AcctVATScaffoldAnswer !== 'object')) {
            setG10AcctVATScaffoldAnswer(buildEmptyWordbankAnswer(question));
        }
    }, [question]);

    const newExample = () => {
        fetchGrade10AcctVATScaffoldQuestion({ subskill: selectedSubtopic?.key || 'concepts', difficulty: g10AcctVATScaffoldDifficulty });
    };

    const checkAnswer = () => {
        if (!question) return;
        if (question.question_type === 'mcq') {
            const ok = String(g10AcctVATScaffoldAnswer) === String(question.correct_index);
            setG10AcctVATScaffoldFeedback(ok ? { kind: 'success', message: 'Correct.' } : { kind: 'error', message: `Not quite. Correct: ${question.options?.[question.correct_index] || ''}` });
            return;
        }
        if (question.question_type === 'calc') {
            const expected = parseFloat(question.correct_answer);
            const got = parseFloat(g10AcctVATScaffoldAnswer);
            if (isNaN(got)) { setG10AcctVATScaffoldFeedback({ kind: 'error', message: 'Enter a number.' }); return; }
            const ok = Math.abs(expected - got) < 0.01;
            setG10AcctVATScaffoldFeedback(ok ? { kind: 'success', message: 'Correct!' } : { kind: 'error', message: `Not quite. Expected: R${expected.toFixed(2)}` });
            return;
        }
        if (question.question_type === 'typed') {
            if (!normalizeText(g10AcctVATScaffoldAnswer)) { setG10AcctVATScaffoldFeedback({ kind: 'error', message: 'Write an answer, then check.' }); return; }
            setG10AcctVATScaffoldFeedback({ kind: 'info', message: 'Check your answer against the sample answer and visual aids.' });
            return;
        }
        if (question.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(question);
            const answerState = (g10AcctVATScaffoldAnswer && typeof g10AcctVATScaffoldAnswer === 'object') ? g10AcctVATScaffoldAnswer : buildEmptyWordbankAnswer(question);
            const selections = answerState?.selections && typeof answerState.selections === 'object' ? answerState.selections : {};
            let total = 0;
            let hit = 0;
            Object.keys(correctMap).forEach((rowKey) => {
                const expected = correctMap?.[rowKey]?.['2'];
                if (expected === null || expected === undefined) return;
                total += 1;
                const got = selections?.[rowKey]?.['2'];
                if (String(got) === String(expected)) hit += 1;
            });
            const ok = total > 0 && hit === total;
            setG10AcctVATScaffoldFeedback(ok ? { kind: 'success', message: `0 of ${total} responses incorrect.` } : { kind: 'error', message: `${total - hit} of ${total} responses incorrect.` });
            return;
        }
        setG10AcctVATScaffoldFeedback({ kind: 'info', message: 'Answer saved.' });
    };

    const setAnswerValue = (value) => {
        setG10AcctVATScaffoldAnswer(value);
        if (question) marking.registerAnswer(question.id, value);
        setG10AcctVATScaffoldFeedback(null);
        setShowMemo(false);
    };

    const renderWordbankTable = ({ readOnly = false, useCorrectAnswers = false } = {}) => {
        const ans = (g10AcctVATScaffoldAnswer && typeof g10AcctVATScaffoldAnswer === 'object')
            ? g10AcctVATScaffoldAnswer
            : buildEmptyWordbankAnswer(question);
        const wordBank = getWordBank(question);
        const used = getUsedTokenIds(ans);
        const tokenLabelById = {};
        wordBank.forEach((token) => { tokenLabelById[String(token.id)] = token.label; });
        const correctMap = getCorrectMap(question);
        const cellTeachingMap = getCellTeachingMap(question);
        const derivationMap = getDerivationMap(question);
        const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
        const headers = Array.isArray(question?.table?.headers) ? question.table.headers : [];

        const setActiveTokenId = (tokenId) => setAnswerValue({ ...(ans || {}), activeTokenId: tokenId });
        const clearCell = (rowIndex) => {
            setAnswerValue({ ...(ans || {}), selections: { ...(ans?.selections || {}), [String(rowIndex)]: { ...((ans?.selections || {})[String(rowIndex)] || {}), '2': null } } });
        };
        const placeActive = (rowIndex) => {
            const tokenId = ans?.activeTokenId;
            if (!tokenId || used.has(String(tokenId))) return;
            setAnswerValue({
                ...(ans || {}),
                selections: { ...(ans?.selections || {}), [String(rowIndex)]: { ...((ans?.selections || {})[String(rowIndex)] || {}), '2': String(tokenId) } },
                activeTokenId: null,
            });
        };

        return (
            <div className="mt-3">
                {!readOnly && (
                    <div className="mb-3">
                        <div className="text-sm font-semibold text-gray-900 mb-2">Word bank</div>
                        <div className="flex flex-wrap gap-2">
                            {wordBank.map((token) => {
                                const isUsed = used.has(String(token.id));
                                const isActive = String(ans?.activeTokenId) === String(token.id);
                                return (
                                    <button
                                        key={token.id}
                                        type="button"
                                        disabled={isUsed}
                                        onClick={() => setActiveTokenId(String(token.id))}
                                        className={`px-3 py-1 rounded-full text-sm font-semibold border ${isUsed ? 'bg-gray-100 text-gray-400 border-gray-200' : isActive ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                                    >
                                        {token.label}
                                    </button>
                                );
                            })}
                        </div>
                    </div>
                )}
                <div className="overflow-x-auto">
                    <table className="min-w-full border border-gray-200 text-sm">
                        <thead className="bg-gray-50">
                            <tr>
                                {headers.map((header, headerIndex) => (
                                    <th key={headerIndex} className="px-3 py-2 border-b border-gray-200 text-left font-semibold text-gray-900">{header}</th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {rows.map((row, rowIndex) => {
                                const selectedId = useCorrectAnswers ? correctMap?.[String(rowIndex)]?.['2'] : ans?.selections?.[String(rowIndex)]?.['2'];
                                const label = selectedId ? tokenLabelById[String(selectedId)] : '';
                                const cellKey = `${rowIndex}:2`;
                                const teaching = cellTeachingMap?.[cellKey];
                                const derivation = String(derivationMap?.[cellKey] || '').trim();
                                return (
                                    <tr key={rowIndex} className={rowIndex % 2 === 0 ? 'bg-white' : 'bg-gray-50'}>
                                        <td className="px-3 py-2 border-b border-gray-200 whitespace-nowrap">{row[0]}</td>
                                        <td className="px-3 py-2 border-b border-gray-200 min-w-[320px]">{row[1]}</td>
                                        <td className="px-3 py-2 border-b border-gray-200">
                                            {readOnly ? (
                                                <div className="w-full text-left px-3 py-2 rounded-md border bg-white border-gray-200 min-h-[42px]">
                                                    {label ? <span className="font-semibold text-gray-900">{label}</span> : <span className="text-gray-400">No selection</span>}
                                                </div>
                                            ) : (
                                                <>
                                                    <button type="button" onClick={() => placeActive(rowIndex)} className={`w-full text-left px-3 py-2 rounded-md border ${label ? 'bg-white border-indigo-200' : 'bg-white border-gray-200 hover:bg-gray-50'}`}>
                                                        {label ? <span className="font-semibold text-gray-900">{label}</span> : <span className="text-gray-400">Click to place...</span>}
                                                    </button>
                                                    <div className="mt-1"><button type="button" onClick={() => clearCell(rowIndex)} className="text-xs font-semibold text-gray-600 hover:text-gray-900">Clear</button></div>
                                                </>
                                            )}
                                            {readOnly && (teaching || derivation) && (
                                                <div className="mt-2 text-xs text-slate-600 space-y-1">
                                                    {teaching?.what_to_enter && <div><span className="font-semibold">What to enter:</span> {teaching.what_to_enter}</div>}
                                                    {teaching?.where_to_look && <div><span className="font-semibold">Where to look:</span> {teaching.where_to_look}</div>}
                                                    {teaching?.method_or_formula && <div><span className="font-semibold">Rule:</span> {teaching.method_or_formula}</div>}
                                                    {derivation && <div><span className="font-semibold">Why:</span> {derivation}</div>}
                                                </div>
                                            )}
                                        </td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>
            </div>
        );
    };

    const memoItems = question?.question_type === 'calc'
        ? [
            ...(String(question?.formula_hint || '').trim() ? [{ label: 'Formula hint', value: String(question.formula_hint).trim() }] : []),
            ...(String(question?.working_formula || '').trim() ? [{ label: 'Working', value: String(question.working_formula).trim() }] : []),
            ...(question?.correct_answer !== null && question?.correct_answer !== undefined ? [{ label: 'Correct answer', value: `${question?.unit || 'R'}${question.correct_answer}` }] : []),
            ...getAnswerPartHints(question),
        ]
        : (getAnswerPartHints(question).length > 0
            ? getAnswerPartHints(question)
            : String(question?.sample_answer || '')
                .split('\n')
                .map((line) => line.trim())
                .filter(Boolean)
                .map((line, idx) => ({ label: `Memo point ${idx + 1}`, value: line })));

    return (
        <div className="w-full">
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-slate-800">Scaffold Mode</h3>
            </div>

            {marking.markingError && <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">{marking.markingError}</div>}

            {!hideConfig && (
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-6">
                    <div className="lg:col-span-2">
                        <div className="flex flex-col sm:flex-row sm:items-end gap-3">
                            <div className="flex-1">
                                <label className="text-sm font-semibold text-slate-700">Subtopic</label>
                                <select value={g10AcctVATScaffoldStepIndex} onChange={(e) => { setG10AcctVATScaffoldStepIndex(Number(e.target.value) || 0); setG10AcctVATScaffoldFeedback(null); setG10AcctVATScaffoldShowHint(false); setG10AcctVATScaffoldAnswer(null); }} className="mt-1 w-full p-2 border rounded-lg">
                                    {scaffoldSteps.map((s, i) => <option key={s.key} value={i}>{s.title}</option>)}
                                </select>
                            </div>
                            <div>
                                <label className="text-sm font-semibold text-slate-700">Difficulty</label>
                                <select value={g10AcctVATScaffoldDifficulty} onChange={(e) => setG10AcctVATScaffoldDifficulty(e.target.value)} className="mt-1 p-2 border rounded-lg">
                                    <option value="easy">Easy</option><option value="medium">Medium</option><option value="hard">Hard</option>
                                </select>
                            </div>
                            <button onClick={newExample} className="px-4 py-2 bg-slate-900 text-white rounded-lg font-semibold hover:bg-slate-800" disabled={g10AcctVATScaffoldLoading}>{g10AcctVATScaffoldLoading ? 'Loading…' : 'New Example'}</button>
                        </div>
                    </div>
                </div>
            )}

            {g10AcctVATScaffoldError && <div className="mb-3 p-3 bg-red-50 border border-red-200 text-red-800 rounded-lg text-sm break-words">{g10AcctVATScaffoldError}</div>}
            {g10AcctVATScaffoldLoading && <div className="text-sm text-slate-500">Loading...</div>}

            {question && (
                <div className="space-y-4">
                    {question.question_type === 'mcq' && (
                        <div className="mt-3 grid grid-cols-1 gap-2">
                            {(question.options || []).map((opt, idx) => (
                                <MCQOption key={idx} selected={String(g10AcctVATScaffoldAnswer) === String(idx)} onClick={() => setAnswerValue(String(idx))} label={opt} />
                            ))}
                        </div>
                    )}

                    {question.question_type === 'calc' && (
                        <div className="mt-3 flex items-center gap-2">
                            <span className="text-slate-500 font-medium">R</span>
                            <input type="number" step="0.01" className="w-full max-w-xs p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-400" placeholder="0.00" value={g10AcctVATScaffoldAnswer || ''} onChange={(e) => setAnswerValue(e.target.value)} />
                        </div>
                    )}

                    {question.question_type === 'typed' && (
                        <div className="mt-3">
                            <textarea value={g10AcctVATScaffoldAnswer || ''} onChange={(e) => setAnswerValue(e.target.value)} placeholder="Write your answer..." className="w-full min-h-[120px] p-3 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-slate-300" />
                        </div>
                    )}

                    {question.question_type === 'table_wordbank' && renderWordbankTable()}

                    <div className="mt-4 flex flex-wrap gap-2">
                        {marking.isPracticeMode ? (
                            <>
                                <button type="button" onClick={checkAnswer} className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-sm font-semibold transition-all">Check</button>
                                <button type="button" onClick={() => setG10AcctVATScaffoldShowHint(!g10AcctVATScaffoldShowHint)} className="px-4 py-2 bg-white border border-slate-200 hover:bg-slate-50 text-slate-800 rounded-xl text-sm font-semibold transition-all">Hint</button>
                                {g10AcctVATScaffoldFeedback && ['typed', 'calc', 'table_wordbank'].includes(String(question?.question_type || '')) && (
                                    <button type="button" onClick={() => setShowMemo(!showMemo)} className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all border ${showMemo ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 hover:bg-slate-50 text-slate-800'}`}>
                                        {showMemo ? 'Hide Memo' : 'Compare / Memo'}
                                    </button>
                                )}
                            </>
                        ) : (
                            !marking.isMarkingSubmitted && <button type="button" onClick={() => marking.submitAssessment([question])} disabled={marking.isSubmitting} className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors disabled:opacity-50">{marking.isSubmitting ? 'Submitting...' : 'Submit Assessment'}</button>
                        )}
                    </div>

                    {g10AcctVATScaffoldShowHint && marking.isPracticeMode && question?.question_type === 'calc' && String(question?.working_formula || '').trim() && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 text-yellow-900 rounded-xl text-sm">
                            <div className="font-semibold">Calculation hint</div>
                            {calcFormulaHint && <div className="mt-2 font-medium whitespace-pre-wrap">{calcFormulaHint}</div>}
                            <div className="mt-2 whitespace-pre-wrap">{question.working_formula}</div>
                            {getAnswerPartHints(question).length > 0 && (
                                <div className="mt-3 space-y-2">
                                    {getAnswerPartHints(question).map((item, idx) => (
                                        <div key={`${item?.label || idx}-${item?.value || ''}`} className="bg-white/70 border border-yellow-200 rounded-lg p-3 text-sm text-yellow-900">
                                            <div className="font-semibold">{item?.label || `Hint ${idx + 1}`}</div>
                                            <div className="mt-1 whitespace-pre-wrap">{item?.value}</div>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                    )}

                    {g10AcctVATScaffoldShowHint && marking.isPracticeMode && question?.question_type === 'typed' && Array.isArray(question?.guidelines) && question.guidelines.length > 0 && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 text-yellow-900 rounded-xl text-sm">
                            <div className="font-semibold">Typed-answer hint</div>
                            <ul className="mt-2 list-disc pl-5 space-y-1">
                                {question.guidelines.map((item, idx) => <li key={idx}>{item}</li>)}
                            </ul>
                            {getAnswerPartHints(question).length > 0 && (
                                <div className="mt-3 space-y-2">
                                    {getAnswerPartHints(question).map((item, idx) => (
                                        <div key={`${item?.label || idx}-${item?.value || ''}`} className="bg-white/70 border border-yellow-200 rounded-lg p-3 text-sm text-yellow-900">
                                            <div className="font-semibold">{item?.label || `Hint ${idx + 1}`}</div>
                                            <div className="mt-1 whitespace-pre-wrap">{item?.value}</div>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                    )}

                    {g10AcctVATScaffoldShowHint && marking.isPracticeMode && question?.question_type === 'table_wordbank' && Array.isArray(question?.guidelines) && question.guidelines.length > 0 && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 text-yellow-900 rounded-xl text-sm">
                            <div className="font-semibold">Word-bank hint</div>
                            <ul className="mt-2 list-disc pl-5 space-y-1">
                                {question.guidelines.map((item, idx) => <li key={idx}>{item}</li>)}
                            </ul>
                        </div>
                    )}

                    {g10AcctVATScaffoldFeedback && marking.isPracticeMode && (
                        <div className={`mt-3 p-3 rounded-xl text-sm border ${g10AcctVATScaffoldFeedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : g10AcctVATScaffoldFeedback.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                            {g10AcctVATScaffoldFeedback.message}
                        </div>
                    )}

                    {showMemo && question?.question_type !== 'table_wordbank' && question?.question_type !== 'mcq' && memoItems.length > 0 && (
                        <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                            <div className="font-semibold text-slate-900">Compare / Memo</div>
                            <div className="mt-3 space-y-3">
                                {memoItems.map((item) => (
                                    <div key={`${item.label}-${item.value}`}>
                                        <div className="font-semibold text-slate-900">{item.label}</div>
                                        <div className="whitespace-pre-wrap">{item.value}</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}

                    {showMemo && question?.question_type === 'mcq' && (
                        <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                            <div className="font-semibold text-slate-900">Compare / Memo</div>
                            <div className="mt-3">
                                <p className="text-emerald-700 font-medium">
                                    Correct option: {question.options?.[question.correct_index]}
                                </p>
                            </div>
                        </div>
                    )}

                    {showMemo && question?.question_type === 'calc' && Object.keys(calcDerivationMap || {}).length > 0 && (
                        <div className="mt-4 p-4 bg-white border border-indigo-100 rounded-xl text-sm text-slate-700">
                            <div className="font-semibold text-slate-900">Worked steps</div>
                            <div className="mt-3 space-y-2">
                                {Object.entries(calcDerivationMap).map(([label, value]) => (
                                    <div key={`${label}-${value}`} className="border border-slate-200 rounded-lg p-3 bg-slate-50">
                                        <div className="font-semibold text-slate-900">{label}</div>
                                        <div className="mt-1 whitespace-pre-wrap">{value}</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}

                    {showMemo && question?.question_type === 'table_wordbank' && renderWordbankTable({ readOnly: true, useCorrectAnswers: true })}
                </div>
            )}

            {marking.isMarkingSubmitted && marking.markingResults && (
                <div className="mt-6 p-6 bg-indigo-50 border border-indigo-200 rounded-2xl">
                    <h4 className="text-xl font-bold text-indigo-900 mb-2">Assessment Results</h4>
                    <div className="flex items-end gap-2 mb-4">
                        <span className="text-4xl font-black text-indigo-700">{Math.round((marking.markingResults.total_score / marking.markingResults.max_score) * 100)}%</span>
                        <span className="text-sm font-medium text-indigo-600 mb-1">({marking.markingResults.total_score} / {marking.markingResults.max_score} marks)</span>
                    </div>
                    {question && marking.getFeedbackForQuestion(question.id) && (
                        <div className={`mt-4 p-4 rounded-xl border ${marking.getFeedbackForQuestion(question.id).kind === 'success' ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                            {marking.getFeedbackForQuestion(question.id).message}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default Grade10AccountingVATScaffold;

