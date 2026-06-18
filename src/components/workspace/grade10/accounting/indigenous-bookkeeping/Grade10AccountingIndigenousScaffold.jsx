import React, { useMemo, useEffect, useState } from 'react';

import { TableInput } from '../../../../forms/TableComponents';
import { useGrade10AccountingMarking } from '../useGrade10AccountingMarking';

const normalizeText = (value) => {
    if (value === null || value === undefined) return '';
    return String(value).trim().replace(/\s+/g, ' ').toLowerCase();
};

const toNumber = (value) => {
    if (value === null || value === undefined) return null;
    const n = Number(String(value).replace(/[^0-9.\-]/g, ''));
    return Number.isFinite(n) ? n : null;
};

const getWordBank = (question) => Array.isArray(question?.word_bank) ? question.word_bank : [];

const getCorrectMap = (question) => (question?.correct_map && typeof question.correct_map === 'object') ? question.correct_map : {};

const getAnswerPartHints = (question) => Array.isArray(question?.answer_part_hints) ? question.answer_part_hints : [];

const getDerivationMap = (question) => (question?.derivation_map && typeof question.derivation_map === 'object') ? question.derivation_map : {};

const getCellTeachingMap = (question) => (question?.cell_teaching_map && typeof question.cell_teaching_map === 'object') ? question.cell_teaching_map : {};

const getTokenLabel = (token) => String(token?.label || token?.text || '').trim();

const buildEmptyWordbankAnswer = (question) => {
    const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
    const selections = {};
    for (let i = 0; i < rows.length; i += 1) {
        selections[String(i)] = { '1': null, '2': null };
    }
    return { selections, activeTokenId: null };
};

const getUsedTokenIds = (ans) => {
    const selections = ans?.selections && typeof ans.selections === 'object' ? ans.selections : {};
    const used = new Set();
    Object.values(selections).forEach((row) => {
        if (!row) return;
        const a = row['1'];
        const b = row['2'];
        if (a) used.add(String(a));
        if (b) used.add(String(b));
    });
    return used;
};

const buildNonTabularMemoItems = (question) => {
    const answerPartHints = getAnswerPartHints(question);
    const derivationItems = Object.entries(getDerivationMap(question)).map(([label, value]) => ({
        label: String(label || '').trim(),
        value: String(value || '').trim(),
    })).filter((item) => item.value);

    if (answerPartHints.length > 0) {
        const baseItems = answerPartHints
            .map((item, idx) => ({
                label: String(item?.label || `Memo point ${idx + 1}`).trim(),
                value: String(item?.value || '').trim(),
            }))
            .filter((item) => item.value);
        const sampleAnswer = String(question?.sample_answer || '').trim();
        if (sampleAnswer) {
            baseItems.push({ label: 'Guideline answer', value: sampleAnswer });
        }
        return [...baseItems, ...derivationItems.filter((item) => item.label.toLowerCase() !== 'guideline answer')];
    }

    if (question?.question_type === 'calc') {
        const items = [];
        const formulaHint = String(question?.formula_hint || '').trim();
        const formula = String(question?.working_formula || '').trim();
        const correctValue = question?.correct_value;
        if (formulaHint) items.push({ label: 'Formula hint', value: formulaHint });
        if (formula) items.push({ label: 'Working', value: formula });
        if (correctValue !== null && correctValue !== undefined && String(correctValue).trim() !== '') {
            items.push({ label: 'Correct answer', value: `${question?.unit || ''}${correctValue}`.trim() });
        }
        return [...items, ...derivationItems];
    }

    return String(question?.sample_answer || '')
        .split('\n')
        .map((line) => line.trim())
        .filter(Boolean)
        .map((line, idx) => ({ label: `Memo point ${idx + 1}`, value: line }))
        .concat(derivationItems);
};

const buildWordbankMemoRows = (question) => {
    const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
    const wordBank = getWordBank(question);
    const correctMap = getCorrectMap(question);
    const cellTeachingMap = getCellTeachingMap(question);
    const derivationMap = getDerivationMap(question);
    const labelById = {};
    wordBank.forEach((token) => {
        labelById[String(token.id)] = getTokenLabel(token);
    });
    return Object.keys(correctMap)
        .sort((a, b) => Number(a) - Number(b))
        .map((rowKey) => {
            const row = rows[Number(rowKey)] || [];
            const informalId = correctMap?.[rowKey]?.['1'];
            const formalId = correctMap?.[rowKey]?.['2'];
            return {
                rowLabel: String(row?.[0] || Number(rowKey) + 1),
                informalAnswer: labelById[String(informalId)] || '',
                formalAnswer: labelById[String(formalId)] || '',
                informalTeaching: cellTeachingMap?.[`${rowKey}:1`] || null,
                formalTeaching: cellTeachingMap?.[`${rowKey}:2`] || null,
                informalDerivation: String(derivationMap?.[`${rowKey}:1`] || '').trim(),
                formalDerivation: String(derivationMap?.[`${rowKey}:2`] || '').trim(),
            };
        })
        .filter((item) => item.informalAnswer || item.formalAnswer);
};

const Grade10AccountingIndigenousScaffold = ({
    onBack,
    scaffoldSteps,
    g10AcctIndVisualAidsOpen,
    setG10AcctIndVisualAidsOpen,
    g10AcctIndScaffoldDifficulty,
    setG10AcctIndScaffoldDifficulty,
    g10AcctIndScaffoldStepIndex,
    setG10AcctIndScaffoldStepIndex,
    fetchGrade10AcctIndScaffoldQuestion,
    g10AcctIndScaffoldLoading,
    g10AcctIndScaffoldError,
    g10AcctIndScaffoldQuestion,
    g10AcctIndScaffoldAnswer,
    setG10AcctIndScaffoldAnswer,
    g10AcctIndScaffoldFeedback,
    setG10AcctIndScaffoldFeedback,
    g10AcctIndScaffoldShowHint,
    setG10AcctIndScaffoldShowHint,
    renderGrade10AcctIndVisualAids,
    hideConfig,
}) => {
    const question = g10AcctIndScaffoldQuestion;
    const [showMemo, setShowMemo] = useState(false);

    const selectedSubtopic = scaffoldSteps[g10AcctIndScaffoldStepIndex] || scaffoldSteps[0];

    const marking = useGrade10AccountingMarking();

    // Reset marking state when new subtopic selected
    useEffect(() => {
        marking.setMarkingMode('practice');
        setShowMemo(false);
    }, [g10AcctIndScaffoldStepIndex]);

    useEffect(() => {
        setShowMemo(false);
    }, [question]);
  
    const newExample = () => {
        setShowMemo(false);
        fetchGrade10AcctIndScaffoldQuestion({
            subskill: selectedSubtopic?.key || 'informal_vs_formal',
            difficulty: g10AcctIndScaffoldDifficulty,
        });
    };

    const checkAnswer = () => {
        if (!question) return;

        if (question.question_type === 'mcq') {
            const ok = String(g10AcctIndScaffoldAnswer) === String(question.correct_index);
            setG10AcctIndScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Correct option: ${Number(question.correct_index) + 1}` });
            return;
        }

        if (question.question_type === 'typed') {
            const ok = normalizeText(g10AcctIndScaffoldAnswer).length > 0;
            setG10AcctIndScaffoldFeedback(ok
                ? { kind: 'info', message: '0 of 1 responses missing. Compare with the memo below.' }
                : { kind: 'error', message: 'Write a short answer first.' });
            return;
        }

        if (question.question_type === 'table') {
            const hasAny = Array.isArray(g10AcctIndScaffoldAnswer?.rows)
                ? g10AcctIndScaffoldAnswer.rows.some((r) => (r || []).some((c) => String(c || '').trim().length > 0))
                : false;
            setG10AcctIndScaffoldFeedback(hasAny
                ? { kind: 'info', message: 'Answer saved. Compare with the memo below.' }
                : { kind: 'error', message: 'Fill in at least one cell before checking.' });
            return;
        }

        if (question.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(question);
            const ans = (g10AcctIndScaffoldAnswer && typeof g10AcctIndScaffoldAnswer === 'object')
                ? g10AcctIndScaffoldAnswer
                : buildEmptyWordbankAnswer(question);

            const selections = ans?.selections && typeof ans.selections === 'object' ? ans.selections : {};
            const rowKeys = Object.keys(correctMap);
            let total = 0;
            let correct = 0;

            rowKeys.forEach((rk) => {
                const rowCorrect = correctMap[rk] || {};
                ['1', '2'].forEach((ck) => {
                    total += 1;
                    const expected = rowCorrect?.[ck];
                    const actual = selections?.[rk]?.[ck];
                    if (expected && actual && String(expected) === String(actual)) correct += 1;
                });
            });

            if (total === 0) {
                setG10AcctIndScaffoldFeedback({ kind: 'error', message: 'Nothing to mark for this question.' });
                return;
            }

            const filled = rowKeys.some((rk) => selections?.[rk]?.['1'] || selections?.[rk]?.['2']);
            if (!filled) {
                setG10AcctIndScaffoldFeedback({ kind: 'error', message: 'Place at least one phrase into the table first.' });
                return;
            }

            setG10AcctIndScaffoldFeedback(correct === total
                ? { kind: 'success', message: `0 of ${total} responses incorrect.` }
                : { kind: 'error', message: `${Math.max(total - correct, 0)} of ${total} responses incorrect.` });
            return;
        }

        if (question.question_type === 'calc') {
            const userN = toNumber(g10AcctIndScaffoldAnswer);
            if (userN === null) {
                setG10AcctIndScaffoldFeedback({ kind: 'error', message: 'Enter a number first.' });
                return;
            }
            const correct = Number(question.correct_value);
            const ok = Number.isFinite(correct) && Math.abs(userN - correct) <= 0.01;
            setG10AcctIndScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Correct answer: ${question.unit || ''}${correct.toFixed(2)}` });
            return;
        }

        setG10AcctIndScaffoldFeedback({ kind: 'error', message: 'Unsupported question type.' });
    };

    const setAnswerValue = (value) => {
        setG10AcctIndScaffoldAnswer(value);
        if (question) {
            marking.registerAnswer(question.id, value);
        }
        setG10AcctIndScaffoldFeedback(null);
        setShowMemo(false);
    };

    const setWordbankAnswer = (updater) => {
        const base = (g10AcctIndScaffoldAnswer && typeof g10AcctIndScaffoldAnswer === 'object')
            ? g10AcctIndScaffoldAnswer
            : buildEmptyWordbankAnswer(question);
        const next = typeof updater === 'function' ? updater(base) : updater;
        setAnswerValue(next);
    };

    const renderWordbankTable = () => {
        const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
        const headers = Array.isArray(question?.table?.headers) ? question.table.headers : [];
        const wordBank = getWordBank(question);
        const correctMap = question?.correct_map || {};
        const ans = (g10AcctIndScaffoldAnswer && typeof g10AcctIndScaffoldAnswer === 'object')
            ? g10AcctIndScaffoldAnswer
            : buildEmptyWordbankAnswer(question);
        // In memo mode, use correctMap for display instead of user selections
        const effectiveSelections = showMemo ? correctMap : (ans?.selections || {});
        const used = showMemo ? new Set() : getUsedTokenIds(ans);
        const tokenLabelById = {};
        wordBank.forEach((token) => {
            tokenLabelById[String(token.id)] = getTokenLabel(token);
        });

        const setActiveTokenId = (tokenId) => {
            if (showMemo) return;
            if (tokenId && used.has(String(tokenId))) return;
            setWordbankAnswer({ ...(ans || {}), activeTokenId: tokenId });
        };

        const placeActive = (rowIdx, colIdx) => {
            if (showMemo) return;
            const tokenId = ans?.activeTokenId;
            if (!tokenId || used.has(String(tokenId))) return;
            setWordbankAnswer((prev) => ({
                ...(prev || {}),
                selections: {
                    ...(prev?.selections || {}),
                    [String(rowIdx)]: {
                        ...((prev?.selections || {})[String(rowIdx)] || {}),
                        [String(colIdx)]: String(tokenId),
                    },
                },
                activeTokenId: null,
            }));
        };

        const clearCell = (rowIdx, colIdx) => {
            if (showMemo) return;
            setWordbankAnswer((prev) => {
                const selections = prev?.selections && typeof prev.selections === 'object' ? { ...prev.selections } : {};
                const rk = String(rowIdx);
                const rowSel = selections[rk] ? { ...selections[rk] } : { '1': null, '2': null };
                rowSel[String(colIdx)] = null;
                selections[rk] = rowSel;
                return { ...prev, selections };
            });
        };

        return (
            <div className="mt-3">
                {!showMemo && (
                    <div className="mb-3">
                        <div className="text-sm font-semibold text-slate-800 mb-2">Word bank</div>
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
                                        className={`px-3 py-1 rounded-full text-sm font-semibold border ${isUsed ? 'bg-slate-100 text-slate-400 border-slate-200' : isActive ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                                    >
                                        {getTokenLabel(token)}
                                    </button>
                                );
                            })}
                        </div>
                    </div>
                )}

                <div className="overflow-x-auto">
                    <table className="min-w-full border border-slate-200 text-sm">
                        <thead className="bg-slate-50">
                            <tr>
                                {headers.map((h, i) => (
                                    <th key={`${h}_${i}`} className="px-3 py-2 border-b border-slate-200 text-left font-semibold text-slate-900">{h}</th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {rows.map((r, rowIdx) => {
                                const heading = r?.[0];
                                const informalId = effectiveSelections?.[String(rowIdx)]?.['1'] || null;
                                const formalId = effectiveSelections?.[String(rowIdx)]?.['2'] || null;
                                const expectedInformal = correctMap?.[String(rowIdx)]?.['1'];
                                const expectedFormal = correctMap?.[String(rowIdx)]?.['2'];
                                const informalCorrect = showMemo && informalId && String(informalId) === String(expectedInformal);
                                const formalCorrect = showMemo && formalId && String(formalId) === String(expectedFormal);

                                const informalStyle = informalCorrect ? 'bg-emerald-50 border-emerald-400 text-emerald-800 font-semibold' : 'border-dashed border-slate-300 bg-white text-slate-700 hover:bg-slate-50';
                                const formalStyle = formalCorrect ? 'bg-emerald-50 border-emerald-400 text-emerald-800 font-semibold' : 'border-dashed border-slate-300 bg-white text-slate-700 hover:bg-slate-50';

                                return (
                                    <tr key={`${heading}_${rowIdx}`} className="border-b border-slate-100 last:border-b-0">
                                        <td className="px-3 py-2 text-slate-700 font-semibold align-top min-w-[180px]">
                                            {heading}
                                        </td>
                                        <td className="px-3 py-2 align-top">
                                            <div className="flex flex-wrap items-center gap-2">
                                                <button
                                                    type="button"
                                                    onClick={() => placeActive(rowIdx, 1)}
                                                    disabled={showMemo}
                                                    className={`min-w-[220px] text-left px-3 py-2 rounded-lg border ${informalStyle} ${showMemo ? 'cursor-default' : ''}`}
                                                >
                                                {informalId ? (
                                                    tokenLabelById[String(informalId)] || ''
                                                ) : (
                                                    showMemo ? '—' : 'Place selected phrase here'
                                                )}
                                                </button>
                                                {informalId && !showMemo && (
                                                    <button
                                                        type="button"
                                                        onClick={() => clearCell(rowIdx, 1)}
                                                        className="px-2 py-1 rounded-md border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                                                    >
                                                        Clear
                                                    </button>
                                                )}
                                            </div>
                                        </td>
                                        <td className="px-3 py-2 align-top">
                                            <div className="flex flex-wrap items-center gap-2">
                                                <button
                                                    type="button"
                                                    onClick={() => placeActive(rowIdx, 2)}
                                                    disabled={showMemo}
                                                    className={`min-w-[220px] text-left px-3 py-2 rounded-lg border ${formalStyle} ${showMemo ? 'cursor-default' : ''}`}
                                                >
                                                {formalId ? (
                                                    tokenLabelById[String(formalId)] || ''
                                                ) : (
                                                    showMemo ? '—' : 'Place selected phrase here'
                                                )}
                                                </button>
                                                {formalId && !showMemo && (
                                                    <button
                                                        type="button"
                                                        onClick={() => clearCell(rowIdx, 2)}
                                                        className="px-2 py-1 rounded-md border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                                                    >
                                                        Clear
                                                    </button>
                                                )}
                                            </div>
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

    const nonTabularMemoItems = question && question?.question_type !== 'mcq' && question?.question_type !== 'table_wordbank'
        ? buildNonTabularMemoItems(question)
        : [];
    const wordbankMemoRows = question?.question_type === 'table_wordbank' ? buildWordbankMemoRows(question) : [];
    const calcHintText = String(question?.working_formula || '').trim();
    const calcFormulaHint = String(question?.formula_hint || '').trim();

    
    const hasInput = useMemo(() => {
        if (!question) return false;
        const ans = g10AcctIndScaffoldAnswer;
        if (question.question_type === 'mcq') return ans !== null && ans !== undefined && String(ans).trim() !== '';
        if (question.question_type === 'typed') return String(ans || '').trim().length > 0;
        if (question.question_type === 'table_wordbank') {
            return (ans && ans.selections) ? Object.values(ans.selections).some(row => row && Object.values(row).some(v => v !== null && v !== undefined)) : false;
        }
        if (question.question_type === 'table') {
            return (ans && ans.rows) ? ans.rows.some(r => (r || []).some(c => String(c || '').trim().length > 0)) : false;
        }
        if (question.question_type === 'calc') {
            if (ans === null || ans === undefined) return false;
            if (typeof ans === 'string') return ans.trim().length > 0;
            if (typeof ans === 'number') return true;
            return Object.values(ans).some(val => String(val || '').trim().length > 0);
        }
        return false;
    }, [question, g10AcctIndScaffoldAnswer]);

    return (
        <>
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-slate-800">Scaffold Mode</h3>


            </div>

            {marking.markingError && (
                <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">
                    {marking.markingError}
                </div>
            )}

            {!hideConfig && (
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-6">
                    <div className="lg:col-span-2">
                        <div className="flex flex-col sm:flex-row sm:items-end gap-3">
                            <div className="flex-1">
                                <label className="text-sm font-semibold text-slate-700">Subtopic</label>
                                <select
                                    value={g10AcctIndScaffoldStepIndex}
                                    onChange={(e) => {
                                        const idx = Number(e.target.value);
                                        setG10AcctIndScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                        setG10AcctIndScaffoldFeedback(null);
                                        setG10AcctIndScaffoldShowHint(false);
                                        setG10AcctIndScaffoldAnswer(null);
                                    }}
                                    className="mt-1 w-full p-2 border rounded-lg">
                                    {scaffoldSteps.map((s, i) => (
                                        <option key={s.key} value={i}>{s.title}</option>
                                    ))}
                                </select>
                            </div>
                            <div>
                                <label className="text-sm font-semibold text-slate-700">Difficulty</label>
                                <select
                                    value={g10AcctIndScaffoldDifficulty}
                                    onChange={(e) => setG10AcctIndScaffoldDifficulty(e.target.value)}
                                    className="mt-1 p-2 border rounded-lg"
                                >
                                    <option value="easy">Easy</option>
                                    <option value="medium">Medium</option>
                                    <option value="hard">Hard</option>
                                </select>
                            </div>
                            <button
                                onClick={newExample}
                                className="px-4 py-2 bg-slate-900 text-white rounded-lg font-semibold hover:bg-slate-800"
                                disabled={g10AcctIndScaffoldLoading}
                            >
                                {g10AcctIndScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                    </div>

                    <div className="bg-slate-50 border border-slate-200 rounded-xl p-4">
                        <div className="font-semibold text-slate-800 mb-2">Hint</div>
                        <button
                            onClick={() => setG10AcctIndScaffoldShowHint(!g10AcctIndScaffoldShowHint)}
                            className="px-3 py-2 bg-white border border-slate-200 rounded-lg font-semibold text-slate-800 hover:bg-slate-100"
                        >
                            {g10AcctIndScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                        </button>
                        {g10AcctIndScaffoldShowHint && (
                            <div className="mt-3 text-sm text-slate-700 space-y-3">
                                {question?.question_type === 'calc' && (calcHintText || calcFormulaHint) && (
                                    <div className="space-y-2">
                                        {calcFormulaHint && <div className="font-medium whitespace-pre-wrap">{calcFormulaHint}</div>}
                                        {calcHintText && <div className="whitespace-pre-wrap">{calcHintText}</div>}
                                    </div>
                                )}

                                {Array.isArray(question?.guidelines) && question.guidelines.length > 0 ? (
                                    <ul className="list-disc pl-5 space-y-1">
                                        {question.guidelines.map((g, gi) => <li key={gi}>{g}</li>)}
                                    </ul>
                                ) : (
                                    <div>Use the notes: informal is usually cash-based, low inventory, minimal records; formal uses consistent policies and standards.</div>
                                )}

                                {getAnswerPartHints(question).length > 0 && (
                                    <div className="space-y-2">
                                        {getAnswerPartHints(question).map((item, hintIndex) => (
                                            <div key={`${item?.label || hintIndex}-${item?.value || ''}`} className="bg-white border border-slate-200 rounded-lg p-3">
                                                <div className="font-semibold text-slate-900">{item?.label || `Hint ${hintIndex + 1}`}</div>
                                                <div className="mt-1 whitespace-pre-wrap">{item?.value}</div>
                                            </div>
                                        ))}
                                    </div>
                                )}

                                {question?.question_type === 'table_wordbank' && wordbankMemoRows.length > 0 && (
                                    <div className="space-y-2">
                                        {wordbankMemoRows.map((row) => (
                                            <div key={`hint-${row.rowLabel}`} className="bg-white border border-slate-200 rounded-lg p-3">
                                                <div className="font-semibold text-slate-900">{row.rowLabel}</div>
                                                {row.informalTeaching?.what_to_enter && <div className="mt-1"><span className="font-semibold">Informal:</span> {row.informalTeaching.what_to_enter}</div>}
                                                {row.formalTeaching?.what_to_enter && <div className="mt-1"><span className="font-semibold">Formal:</span> {row.formalTeaching.what_to_enter}</div>}
                                            </div>
                                        ))}
                                    </div>
                                )}
                            </div>
                        )}
                    </div>
                </div>
            )}

            {g10AcctIndScaffoldError && (
                <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">
                    {g10AcctIndScaffoldError}
                </div>
            )}

            {!question && !g10AcctIndScaffoldLoading && (
                <div className="text-slate-600 py-8 text-center">Click "New Example" to begin.</div>
            )}

            {question && (
                <div className="space-y-4">
                    <div className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm">

                        {question.question_type === 'mcq' && (
                            <div className="mt-3 space-y-2">
                                {(question.options || []).map((opt, oi) => (
                                    <button
                                        key={oi}
                                        type="button"
                                        onClick={() => setAnswerValue(oi)}
                                        className={`w-full text-left flex items-center gap-3 text-sm rounded-xl border px-4 py-3 transition-colors ${String(g10AcctIndScaffoldAnswer) === String(oi)
                                            ? 'bg-slate-50 border-slate-300 text-slate-900'
                                            : 'bg-white border-slate-200 text-slate-800 hover:bg-slate-50'
                                            }`}
                                    >
                                        <span
                                            className={`inline-flex h-4 w-4 flex-shrink-0 rounded-full border items-center justify-center ${String(g10AcctIndScaffoldAnswer) === String(oi)
                                                ? 'border-slate-600'
                                                : 'border-slate-400'
                                                }`}
                                            style={{ aspectRatio: '1' }}
                                        >
                                            {String(g10AcctIndScaffoldAnswer) === String(oi) && (
                                                <span className="h-2 w-2 rounded-full bg-slate-900" />
                                            )}
                                        </span>
                                        <span>{oi + 1}. {opt}</span>
                                    </button>
                                ))}
                            </div>
                        )}

                        {question.question_type === 'typed' && (
                            <div className="mt-3">
                                <textarea
                                    value={g10AcctIndScaffoldAnswer || ''}
                                    onChange={(e) => setAnswerValue(e.target.value)}
                                    className="w-full p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-300"
                                    rows={4}
                                    placeholder="Write your answer here…"
                                />
                            </div>
                        )}

                        {question.question_type === 'calc' && (
                            <div className="mt-3">
                                <div className="text-sm text-slate-600 mb-2">Answer</div>
                                <div className="flex items-center gap-2">
                                    {question.unit === 'R' && (
                                        <span className="px-3 py-2 bg-white border border-slate-200 rounded-xl text-slate-700">R</span>
                                    )}
                                    <input
                                        type="number"
                                        step="0.01"
                                        value={g10AcctIndScaffoldAnswer ?? ''}
                                        onChange={(e) => setAnswerValue(e.target.value)}
                                        className="flex-1 p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-300"
                                        placeholder="0.00"
                                    />
                                </div>
                            </div>
                        )}

                        {question.question_type === 'table_wordbank' && renderWordbankTable()}

                        {question.question_type === 'table' && (
                            <div className="mt-3">
                                <TableInput
                                    initialData={g10AcctIndScaffoldAnswer || question.table}
                                    onChange={(data) => setAnswerValue(data)}
                                    isSubmitted={false}
                                />
                            </div>
                        )}

                        <div className="mt-8 flex justify-end gap-3 pt-4 border-t border-slate-100">
                            {marking.isPracticeMode ? (
                                <>
                                    <button
                                        onClick={checkAnswer}
                                        className="px-6 py-2 bg-indigo-50 text-indigo-700 rounded-xl font-semibold hover:bg-indigo-100 transition-colors"
                                    >
                                        Check Answer
                                    </button>
                                    {g10AcctIndScaffoldFeedback && ['mcq', 'typed', 'calc', 'table_wordbank', 'table'].includes(String(question?.question_type || '')) && (
                                        <button
                                            disabled={!hasInput}
                                            onClick={() => setShowMemo(!showMemo)}
                                            className={`px-6 py-2 rounded-xl font-semibold transition-colors border ${showMemo ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'} ${!hasInput ? 'opacity-50 cursor-not-allowed' : ''}`}
                                        >
                                            {showMemo ? 'Hide Memo' : 'Compare / Memo'}
                                        </button>
                                    )}
                                </>
                            ) : (
                                !marking.isMarkingSubmitted && (
                                    <button
                                        onClick={() => marking.submitAssessment([question])}
                                        disabled={marking.isSubmitting}
                                        className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors disabled:opacity-50"
                                    >
                                        {marking.isSubmitting ? 'Submitting...' : 'Submit Assessment'}
                                    </button>
                                )
                            )}
                        </div>

                        {marking.isPracticeMode && g10AcctIndScaffoldFeedback && (
                            <div className={`mt-3 p-3 rounded-xl border ${g10AcctIndScaffoldFeedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : g10AcctIndScaffoldFeedback.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                                {g10AcctIndScaffoldFeedback.message}
                            </div>
                        )}

                        {marking.isPracticeMode && showMemo && question.question_type === 'mcq' && question.explanation && (
                            <div className="mt-3 text-sm text-slate-700">
                                <span className="font-semibold">Explanation: </span>{question.explanation}
                            </div>
                        )}

                        {showMemo && question.question_type !== 'mcq' && question.question_type !== 'table_wordbank' && question.question_type !== 'calc' && nonTabularMemoItems.length > 0 && (
                            <div className="mt-6 text-sm text-slate-700 bg-slate-50 p-4 rounded-xl border border-slate-200">
                                <div className="font-semibold text-slate-900">Compare / Memo</div>
                                <div className="mt-3 space-y-3">
                                    {nonTabularMemoItems.map((item) => (
                                        <div key={`${item.label}-${item.value}`}>
                                            <div className="font-semibold text-slate-900">{item.label}</div>
                                            <div className="whitespace-pre-wrap">{item.value}</div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {showMemo && question.question_type === 'calc' && (
                            <div className="mt-6 text-sm text-slate-700 bg-slate-50 p-4 rounded-xl border border-slate-200">
                                <div className="font-semibold text-slate-900">Memo / Working</div>
                                <div className="mt-3 space-y-3">
                                    {calcFormulaHint && (
                                        <div>
                                            <div className="font-semibold text-slate-900">Formula</div>
                                            <div className="whitespace-pre-wrap">{calcFormulaHint}</div>
                                        </div>
                                    )}
                                    {calcHintText && (
                                        <div>
                                            <div className="font-semibold text-slate-900">Working</div>
                                            <div className="whitespace-pre-wrap">{calcHintText}</div>
                                        </div>
                                    )}
                                    {question.correct_value !== null && question.correct_value !== undefined && (
                                        <div>
                                            <div className="font-semibold text-slate-900">Correct answer</div>
                                            <div>{question.unit || ''}{question.correct_value}</div>
                                        </div>
                                    )}
                                    {!calcFormulaHint && !calcHintText && question.correct_value == null && (
                                        <div className="text-slate-500">No memo details available for this question.</div>
                                    )}
                                </div>
                            </div>
                        )}

                        {showMemo && question.question_type === 'table_wordbank' && wordbankMemoRows.length > 0 && (
                            <div className="mt-6 text-sm text-slate-700 bg-slate-50 p-4 rounded-xl border border-slate-200">
                                <div className="font-semibold text-slate-900">Compare / Memo</div>
                                <div className="mt-3 space-y-3">
                                    {wordbankMemoRows.map((row) => (
                                        <div key={`${row.rowLabel}-${row.informalAnswer}-${row.formalAnswer}`} className="bg-white border border-slate-200 rounded-lg p-3">
                                            <div className="font-semibold text-slate-900">{row.rowLabel}</div>
                                            {row.informalAnswer && <div className="mt-2"><span className="font-semibold">Informal:</span> {row.informalAnswer}</div>}
                                            {row.formalAnswer && <div className="mt-1"><span className="font-semibold">Formal:</span> {row.formalAnswer}</div>}
                                            {row.informalDerivation && <div className="mt-1"><span className="font-semibold">Why informal:</span> {row.informalDerivation}</div>}
                                            {row.formalDerivation && <div className="mt-1"><span className="font-semibold">Why formal:</span> {row.formalDerivation}</div>}
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* Marking Results Overlay/Summary */}
            {marking.isMarkingSubmitted && marking.markingResults && (
                <div className="mt-6 p-6 bg-indigo-50 border border-indigo-200 rounded-2xl">
                    <h4 className="text-xl font-bold text-indigo-900 mb-2">Assessment Results</h4>
                    <div className="flex items-end gap-2 mb-4">
                        <span className="text-4xl font-black text-indigo-700">
                            {Math.round((marking.markingResults.total_score / marking.markingResults.max_score) * 100)}%
                        </span>
                        <span className="text-sm font-medium text-indigo-600 mb-1">
                            ({marking.markingResults.total_score} / {marking.markingResults.max_score} marks)
                        </span>
                    </div>
                    <p className="text-indigo-800 text-sm">
                        Review your specific section answer. The feedback is now displayed securely from the backend!
                    </p>

                    {/* Specific question feedback from backend */}
                    {marking.getFeedbackForQuestion(question.id) && (
                        <div className={`mt-4 p-4 rounded-xl border ${marking.getFeedbackForQuestion(question.id).kind === 'success' ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                            {marking.getFeedbackForQuestion(question.id).message}
                        </div>
                    )}
                </div>
            )}


        </>
    );
};

export default Grade10AccountingIndigenousScaffold;

