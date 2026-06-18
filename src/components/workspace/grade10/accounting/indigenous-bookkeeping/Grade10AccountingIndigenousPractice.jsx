import React, { useState, useEffect } from 'react';
import VisualAidsPanel from '../../../VisualAidsPanel';
import { TableInput, TableRenderer } from '../../../../forms/TableComponents';
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

const Grade10AccountingIndigenousPractice = ({
    onBack,
    g10AcctIndVisualAidsOpen,
    setG10AcctIndVisualAidsOpen,
    g10AcctIndPracticeDifficulty,
    setG10AcctIndPracticeDifficulty,
    fetchGrade10AcctIndPractice,
    g10AcctIndPracticeLoading,
    g10AcctIndPracticeError,
    g10AcctIndPracticeQuestions,
    g10AcctIndPracticeAnswers,
    setG10AcctIndPracticeAnswers,
    g10AcctIndPracticeFeedback,
    setG10AcctIndPracticeFeedback,
    renderGrade10AcctIndVisualAids,
    hideConfig,
}) => {
    const questions = Array.isArray(g10AcctIndPracticeQuestions) ? g10AcctIndPracticeQuestions : [];
    const [currentIndex, setCurrentIndex] = useState(0);
    const [showMemo, setShowMemo] = useState(false);
    const [showHint, setShowHint] = useState(false);
    const [reviewMode, setReviewMode] = useState(false);
    const [activeReviewMemoIndex, setActiveReviewMemoIndex] = useState(null);

    const marking = useGrade10AccountingMarking();

    // Reset marking state when new questions are fetched
    useEffect(() => {
        if (questions.length > 0) {
            marking.setMarkingMode('practice');
        }
    }, [questions]);

    useEffect(() => {
        setCurrentIndex(0);
        setShowMemo(false);
        setShowHint(false);
        setReviewMode(false);
        setActiveReviewMemoIndex(null);
    }, [questions]);

    useEffect(() => {
        if (!questions.length) return;
        if (!Array.isArray(g10AcctIndPracticeAnswers) || g10AcctIndPracticeAnswers.length !== questions.length) {
            setG10AcctIndPracticeAnswers(questions.map((question) => {
                if (question.question_type === 'table_wordbank') return buildEmptyWordbankAnswer(question);
                if (question.question_type === 'table') return question.table || { headers: [''], rows: [['']] };
                return '';
            }));
        }
        if (!Array.isArray(g10AcctIndPracticeFeedback) || g10AcctIndPracticeFeedback.length !== questions.length) {
            setG10AcctIndPracticeFeedback(questions.map(() => null));
        }
    }, [questions.length]);

    const handleNext = () => {
        if (reviewMode) return;
        if (currentIndex < questions.length - 1) {
            setCurrentIndex((prev) => prev + 1);
        }
    };

    const handlePrev = () => {
        if (reviewMode) return;
        if (currentIndex > 0) {
            setCurrentIndex((prev) => prev - 1);
        }
    };

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g10AcctIndPracticeAnswers) ? [...g10AcctIndPracticeAnswers] : [];
        answers[idx] = value;
        setG10AcctIndPracticeAnswers(answers);

        // Register with marking hook if in marking mode
        if (questions[idx]) {
            marking.registerAnswer(questions[idx].id, value);
        }

        const feedback = Array.isArray(g10AcctIndPracticeFeedback) ? [...g10AcctIndPracticeFeedback] : [];
        feedback[idx] = null;
        setG10AcctIndPracticeFeedback(feedback);
        if (idx === currentIndex) setShowMemo(false);
    };

    const setFeedbackAt = (targetIndex, value) => {
        const next = Array.isArray(g10AcctIndPracticeFeedback) ? g10AcctIndPracticeFeedback.slice() : [];
        next[targetIndex] = value;
        setG10AcctIndPracticeFeedback(next);
    };

    const evaluateQuestion = (question, userValue) => {
        if (!question) return { kind: 'error', message: 'Unable to review this answer.' };

        if (question.question_type === 'mcq') {
            const ok = String(userValue) === String(question.correct_index);
            return ok
                ? { kind: 'success', message: '0 of 1 responses incorrect.' }
                : { kind: 'error', message: `1 of 1 responses incorrect. Correct answer: ${question.options?.[question.correct_index] || ''}` };
        }

        if (question.question_type === 'typed') {
            const ok = normalizeText(userValue).length > 0;
            return ok
                ? { kind: 'info', message: '0 of 1 responses missing. Compare with the memo below.' }
                : { kind: 'error', message: '1 of 1 responses missing. Write an answer first.' };
        }

        if (question.question_type === 'table') {
            const hasAny = Array.isArray(userValue?.rows)
                ? userValue.rows.some((row) => (row || []).some((cell) => String(cell || '').trim().length > 0))
                : false;
            return hasAny
                ? { kind: 'info', message: 'Answer saved. Compare with the memo below.' }
                : { kind: 'error', message: 'Fill in at least one cell before checking.' };
        }

        if (question.question_type === 'calc') {
            const got = toNumber(userValue);
            const expected = Number(question.correct_value);
            if (got === null) return { kind: 'error', message: '1 of 1 responses incorrect. Enter a number first.' };
            const ok = Number.isFinite(expected) && Math.abs(expected - got) <= 0.01;
            return ok
                ? { kind: 'success', message: '0 of 1 responses incorrect.' }
                : { kind: 'error', message: `1 of 1 responses incorrect. Correct answer: ${(question.unit || '')}${expected.toFixed(2)}`.trim() };
        }

        if (question.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(question);
            const answerState = (userValue && typeof userValue === 'object') ? userValue : buildEmptyWordbankAnswer(question);
            const selections = answerState?.selections && typeof answerState.selections === 'object' ? answerState.selections : {};
            let total = 0;
            let hit = 0;

            Object.keys(correctMap).forEach((rowKey) => {
                const rowCorrect = correctMap?.[rowKey] || {};
                ['1', '2'].forEach((colKey) => {
                    const expected = rowCorrect?.[colKey];
                    if (expected === null || expected === undefined) return;
                    total += 1;
                    const got = selections?.[rowKey]?.[colKey];
                    if (String(got) === String(expected)) hit += 1;
                });
            });

            return hit === total && total > 0
                ? { kind: 'success', message: `0 of ${total} responses incorrect.` }
                : { kind: 'error', message: `${Math.max(total - hit, 0)} of ${total} responses incorrect.` };
        }

        return { kind: 'info', message: 'Saved.' };
    };

    const checkOne = (idx) => {
        const question = questions[idx];
        if (!question) return;
        const answers = Array.isArray(g10AcctIndPracticeAnswers) ? g10AcctIndPracticeAnswers : [];
        setFeedbackAt(idx, evaluateQuestion(question, answers[idx]));
    };

    const handleFinishAndReview = () => {
        const answers = Array.isArray(g10AcctIndPracticeAnswers) ? g10AcctIndPracticeAnswers : [];
        setG10AcctIndPracticeFeedback(questions.map((question, questionIndex) => evaluateQuestion(question, answers[questionIndex])));
        setShowMemo(false);
        setShowHint(false);
        setActiveReviewMemoIndex(null);
        setReviewMode(true);
    };

    // Get current question
    const idx = currentIndex;
    const q = questions[idx];

    // Determine which feedback to show based on mode
    let fb = null;
    if (marking.isMarkingSubmitted && q) {
        fb = marking.getFeedbackForQuestion(q.id);
    } else if (marking.isPracticeMode) {
        fb = g10AcctIndPracticeFeedback?.[idx];
    }

    const answer = g10AcctIndPracticeAnswers?.[idx];

    const renderWordbankTable = (question, targetIndex, { readOnly = false, useCorrectAnswers = false } = {}) => {
        if (!question) return null;
        const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
        const headers = Array.isArray(question?.table?.headers) ? question.table.headers : [];
        const wordBank = getWordBank(question);
        const ans = (g10AcctIndPracticeAnswers?.[targetIndex] && typeof g10AcctIndPracticeAnswers[targetIndex] === 'object')
            ? g10AcctIndPracticeAnswers[targetIndex]
            : buildEmptyWordbankAnswer(question);
        const used = getUsedTokenIds(ans);
        const tokenLabelById = {};
        wordBank.forEach((token) => {
            tokenLabelById[String(token.id)] = getTokenLabel(token);
        });
        const correctMap = getCorrectMap(question);
        const cellTeachingMap = getCellTeachingMap(question);
        const derivationMap = getDerivationMap(question);

        const setWordbankAnswer = (updater) => {
            const base = (g10AcctIndPracticeAnswers?.[targetIndex] && typeof g10AcctIndPracticeAnswers[targetIndex] === 'object')
                ? g10AcctIndPracticeAnswers[targetIndex]
                : buildEmptyWordbankAnswer(question);
            const next = typeof updater === 'function' ? updater(base) : updater;
            setAnswer(targetIndex, next);
        };

        const setActiveTokenId = (tokenId) => {
            if (tokenId && used.has(String(tokenId))) return;
            setWordbankAnswer({ ...(ans || {}), activeTokenId: tokenId });
        };

        const placeActive = (rowIdx, colIdx) => {
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
                {!readOnly && (
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
                                const informalId = useCorrectAnswers ? correctMap?.[String(rowIdx)]?.['1'] : (ans?.selections?.[String(rowIdx)]?.['1'] || null);
                                const formalId = useCorrectAnswers ? correctMap?.[String(rowIdx)]?.['2'] : (ans?.selections?.[String(rowIdx)]?.['2'] || null);
                                const informalTeaching = cellTeachingMap?.[`${rowIdx}:1`];
                                const formalTeaching = cellTeachingMap?.[`${rowIdx}:2`];
                                const informalDerivation = String(derivationMap?.[`${rowIdx}:1`] || '').trim();
                                const formalDerivation = String(derivationMap?.[`${rowIdx}:2`] || '').trim();

                                return (
                                    <tr key={`${heading}_${rowIdx}`} className="border-b border-slate-100 last:border-b-0">
                                        <td className="px-3 py-2 text-slate-700 font-semibold align-top min-w-[180px]">
                                            {heading}
                                        </td>
                                        <td className="px-3 py-2 align-top">
                                            <div className="flex flex-wrap items-center gap-2">
                                                {readOnly ? (
                                                    <div className={`min-w-[220px] text-left px-3 py-2 rounded-lg border min-h-[42px] ${useCorrectAnswers && informalId ? 'bg-emerald-50 border-emerald-400 text-emerald-800 font-semibold' : 'bg-white border-slate-200 text-slate-700'}`}>
                                                        {informalId ? tokenLabelById[String(informalId)] || '' : <span className="text-slate-400">{useCorrectAnswers ? '—' : 'No selection'}</span>}
                                                    </div>
                                                ) : (
                                                    <button
                                                        type="button"
                                                        onClick={() => placeActive(rowIdx, 1)}
                                                        className="min-w-[220px] text-left px-3 py-2 rounded-lg border border-dashed border-slate-300 bg-white text-slate-700 hover:bg-slate-50"
                                                    >
                                                        {informalId ? tokenLabelById[String(informalId)] || '' : 'Place selected phrase here'}
                                                    </button>
                                                )}
                                                {!readOnly && informalId && (
                                                    <button
                                                        type="button"
                                                        onClick={() => clearCell(rowIdx, 1)}
                                                        className="px-2 py-1 rounded-md border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                                                    >
                                                        Clear
                                                    </button>
                                                )}
                                            </div>
                                            {readOnly && (informalTeaching || informalDerivation) && (
                                                <div className="mt-2 text-xs text-slate-600 space-y-1">
                                                    {informalTeaching?.what_to_enter && <div><span className="font-semibold">What to enter:</span> {informalTeaching.what_to_enter}</div>}
                                                    {informalTeaching?.where_to_look && <div><span className="font-semibold">Where to look:</span> {informalTeaching.where_to_look}</div>}
                                                    {informalTeaching?.method_or_formula && <div><span className="font-semibold">Rule:</span> {informalTeaching.method_or_formula}</div>}
                                                    {informalTeaching?.record_link && <div><span className="font-semibold">Record link:</span> {informalTeaching.record_link}</div>}
                                                    {informalDerivation && <div><span className="font-semibold">Why:</span> {informalDerivation}</div>}
                                                </div>
                                            )}
                                        </td>
                                        <td className="px-3 py-2 align-top">
                                            <div className="flex flex-wrap items-center gap-2">
                                                {readOnly ? (
                                                    <div className={`min-w-[220px] text-left px-3 py-2 rounded-lg border min-h-[42px] ${useCorrectAnswers && formalId ? 'bg-emerald-50 border-emerald-400 text-emerald-800 font-semibold' : 'bg-white border-slate-200 text-slate-700'}`}>
                                                        {formalId ? tokenLabelById[String(formalId)] || '' : <span className="text-slate-400">{useCorrectAnswers ? '—' : 'No selection'}</span>}
                                                    </div>
                                                ) : (
                                                    <button
                                                        type="button"
                                                        onClick={() => placeActive(rowIdx, 2)}
                                                        className="min-w-[220px] text-left px-3 py-2 rounded-lg border border-dashed border-slate-300 bg-white text-slate-700 hover:bg-slate-50"
                                                    >
                                                        {formalId ? tokenLabelById[String(formalId)] || '' : 'Place selected phrase here'}
                                                    </button>
                                                )}
                                                {!readOnly && formalId && (
                                                    <button
                                                        type="button"
                                                        onClick={() => clearCell(rowIdx, 2)}
                                                        className="px-2 py-1 rounded-md border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                                                    >
                                                        Clear
                                                    </button>
                                                )}
                                            </div>
                                            {readOnly && (formalTeaching || formalDerivation) && (
                                                <div className="mt-2 text-xs text-slate-600 space-y-1">
                                                    {formalTeaching?.what_to_enter && <div><span className="font-semibold">What to enter:</span> {formalTeaching.what_to_enter}</div>}
                                                    {formalTeaching?.where_to_look && <div><span className="font-semibold">Where to look:</span> {formalTeaching.where_to_look}</div>}
                                                    {formalTeaching?.method_or_formula && <div><span className="font-semibold">Rule:</span> {formalTeaching.method_or_formula}</div>}
                                                    {formalTeaching?.record_link && <div><span className="font-semibold">Record link:</span> {formalTeaching.record_link}</div>}
                                                    {formalDerivation && <div><span className="font-semibold">Why:</span> {formalDerivation}</div>}
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

    const nonTabularMemoItems = q && q?.question_type !== 'mcq' && q?.question_type !== 'table_wordbank'
        ? buildNonTabularMemoItems(q)
        : [];
    const wordbankMemoRows = q?.question_type === 'table_wordbank' ? buildWordbankMemoRows(q) : [];
    const calcHintText = String(q?.working_formula || '').trim();
    const calcFormulaHint = String(q?.formula_hint || '').trim();
    const calcDerivationMap = getDerivationMap(q);

    const renderReviewQuestion = (reviewQuestion, reviewIndex) => {
        const reviewFeedback = Array.isArray(g10AcctIndPracticeFeedback) ? g10AcctIndPracticeFeedback[reviewIndex] : null;
        const memoOpen = activeReviewMemoIndex === reviewIndex;
        const reviewMemoItems = reviewQuestion && reviewQuestion?.question_type !== 'mcq' && reviewQuestion?.question_type !== 'table_wordbank'
            ? buildNonTabularMemoItems(reviewQuestion)
            : [];

        return (
            <div key={reviewQuestion?.id || reviewIndex} className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm space-y-4">
                <div className="flex flex-wrap items-start justify-between gap-3">
                    <div>
                        <div className="text-sm font-semibold text-slate-500">Question {reviewIndex + 1} of {questions.length}</div>
                        <div className="text-lg font-medium text-slate-900 whitespace-pre-wrap">{reviewQuestion?.prompt}</div>
                    </div>
                    {['mcq', 'typed', 'calc', 'table_wordbank', 'table'].includes(String(reviewQuestion?.question_type || '')) && (
                        <button
                            type="button"
                            onClick={() => setActiveReviewMemoIndex(memoOpen ? null : reviewIndex)}
                            className="px-4 py-2 bg-purple-600 text-white rounded-xl font-semibold hover:bg-purple-700 transition-colors"
                        >
                            {memoOpen ? 'Hide Memo' : 'Compare / Memo'}
                        </button>
                    )}
                </div>

                {reviewQuestion?.question_type === 'mcq' && (
                    <div className="grid grid-cols-1 gap-2">
                        {(reviewQuestion.options || []).map((option, optionIndex) => (
                            <div key={optionIndex} className={`px-4 py-3 rounded-xl border ${String(reviewQuestion.correct_index) === String(optionIndex) ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : 'bg-white border-slate-200 text-slate-700'}`}>
                                {option}
                            </div>
                        ))}
                    </div>
                )}

                {reviewQuestion?.question_type === 'calc' && (
                    <div className="p-3 rounded-xl border border-slate-200 bg-slate-50 text-slate-700 text-sm">
                        Your answer: {(() => { const a = g10AcctIndPracticeAnswers?.[reviewIndex]; return (typeof a === 'string' || typeof a === 'number') ? String(a).trim() || 'No answer entered' : 'No answer entered'; })()}
                    </div>
                )}

                {reviewQuestion?.question_type === 'typed' && (
                    <div className="p-3 rounded-xl border border-slate-200 bg-slate-50 text-slate-700 text-sm whitespace-pre-wrap">
                        {(() => { const a = g10AcctIndPracticeAnswers?.[reviewIndex]; return (typeof a === 'string' || typeof a === 'number') ? String(a).trim() || 'No answer entered' : 'No answer entered'; })()}
                    </div>
                )}

                {reviewQuestion?.question_type === 'table' && (
                    <TableRenderer table={g10AcctIndPracticeAnswers?.[reviewIndex] || reviewQuestion.table} />
                )}

                {reviewQuestion?.question_type === 'table_wordbank' && renderWordbankTable(reviewQuestion, reviewIndex, { readOnly: true })}

                {reviewFeedback && (
                    <div className={`mt-3 p-3 rounded-xl text-sm border ${reviewFeedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : reviewFeedback.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                        {reviewFeedback.message}
                    </div>
                )}

                {memoOpen && reviewQuestion?.question_type !== 'table_wordbank' && reviewQuestion?.question_type !== 'mcq' && reviewMemoItems.length > 0 && (
                    <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                        <div className="font-semibold text-slate-900">Compare / Memo</div>
                        <div className="mt-3 space-y-3">
                            {reviewMemoItems.map((item) => (
                                <div key={`${item.label}-${item.value}`}>
                                    <div className="font-semibold text-slate-900">{item.label}</div>
                                    <div className="whitespace-pre-wrap">{item.value}</div>
                                </div>
                            ))}
                        </div>
                    </div>
                )}

                {memoOpen && reviewQuestion?.question_type === 'mcq' && reviewQuestion.explanation && (
                    <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                        <div className="font-semibold text-slate-900">Explanation</div>
                        <div className="mt-2 whitespace-pre-wrap">{reviewQuestion.explanation}</div>
                    </div>
                )}

                {memoOpen && reviewQuestion?.question_type === 'table_wordbank' && (
                    <div className="space-y-3">
                        <div className="text-sm font-semibold text-slate-900">Compare / Memo</div>
                        {renderWordbankTable(reviewQuestion, reviewIndex, { readOnly: true, useCorrectAnswers: true })}
                    </div>
                )}
            </div>
        );
    };

    if (!q && questions.length > 0) {
        // Reset to first question if index is out of bounds
        setCurrentIndex(0);
        return null;
    }

    return (
        <>
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-slate-800">Practice Mode</h3>

                
            </div>

            {marking.markingError && (
                <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">
                    {marking.markingError}
                </div>
            )}

            {g10AcctIndPracticeLoading && (
                <div className="text-sm text-slate-500">Loading...</div>
            )}

            {g10AcctIndPracticeError && (
                <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">
                    {g10AcctIndPracticeError}
                </div>
            )}

            {!q && questions.length === 0 && !g10AcctIndPracticeLoading && (
                <div className="text-slate-600 py-8 text-center">
                    Click "Generate Question" to begin.
                </div>
            )}

            {q && !reviewMode && (
                <div className="space-y-4">
                    {/* Navigation and Submission Header */}
                    <div className="flex items-center justify-between bg-slate-50 p-3 rounded-xl border border-slate-200">
                        <div className="text-sm font-semibold text-slate-700">
                            Question {currentIndex + 1} of {questions.length}
                        </div>
                        <div className="flex items-center gap-2">
                            <button
                                onClick={handlePrev}
                                disabled={currentIndex === 0}
                                className="px-3 py-1.5 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-700 hover:bg-slate-50 disabled:opacity-50"
                            >
                                Previous
                            </button>
                            <button
                                onClick={handleNext}
                                disabled={currentIndex === questions.length - 1}
                                className="px-3 py-1.5 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-700 hover:bg-slate-50 disabled:opacity-50"
                            >
                                Next
                            </button>
                        </div>
                    </div>

                    <div className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm">
                        <div className="text-lg font-medium text-slate-800 whitespace-pre-wrap">{q.prompt}</div>

                        <div className="mt-6">
                            {q.question_type === 'mcq' && (
                                <div className="mt-3 space-y-2">
                                    {(q.options || []).map((opt, oi) => (
                                        <button
                                            key={oi}
                                            type="button"
                                            onClick={() => setAnswer(idx, oi)}
                                            className={`w-full text-left flex items-center gap-3 text-sm rounded-xl border px-4 py-3 transition-colors ${String(answer) === String(oi)
                                                ? 'bg-slate-50 border-slate-300 text-slate-900'
                                                : 'bg-white border-slate-200 text-slate-800 hover:bg-slate-50'
                                                }`}
                                        >
                                            <span
                                                className={`inline-flex h-4 w-4 flex-shrink-0 rounded-full border items-center justify-center ${String(answer) === String(oi)
                                                    ? 'border-slate-600'
                                                    : 'border-slate-400'
                                                    }`}
                                                style={{ aspectRatio: '1' }}
                                            >
                                                {String(answer) === String(oi) && (
                                                    <span className="h-2 w-2 rounded-full bg-slate-900" />
                                                )}
                                            </span>
                                            <span>{oi + 1}. {opt}</span>
                                        </button>
                                    ))}
                                </div>
                            )}

                            {q.question_type === 'typed' && (
                                <div className="mt-3">
                                    <textarea
                                        value={typeof answer === 'string' ? answer : ''}
                                        onChange={(e) => setAnswer(idx, e.target.value)}
                                        className="w-full p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-300"
                                        rows={4}
                                        placeholder="Write your answer here…"
                                    />
                                </div>
                            )}

                            {q.question_type === 'calc' && (
                                <div className="mt-3">
                                    <div className="text-sm text-slate-600 mb-2">Answer</div>
                                    <div className="flex items-center gap-2">
                                        {q.unit === 'R' && (
                                            <span className="px-3 py-2 bg-white border border-slate-200 rounded-xl text-slate-700">R</span>
                                        )}
                                        <input
                                            type="number"
                                            step="0.01"
                                            value={answer ?? ''}
                                            onChange={(e) => setAnswer(idx, e.target.value)}
                                            className="flex-1 p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-300"
                                            placeholder="0.00"
                                        />
                                    </div>
                                </div>
                            )}

                            {q.question_type === 'table_wordbank' && renderWordbankTable(q, idx)}

                            {q.question_type === 'table' && (
                                <div className="mt-3">
                                    <TableInput
                                        initialData={answer || q.table}
                                        onChange={(data) => setAnswer(idx, data)}
                                        isSubmitted={false}
                                    />
                                </div>
                            )}

                            {fb && (
                                <div className={`mt-3 p-3 rounded-xl text-sm border ${fb.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : fb.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                                    {fb.message}
                                </div>
                            )}

                            {showMemo && q.question_type === 'mcq' && q.explanation && (
                                <div className="mt-3 text-sm text-slate-700">
                                    <span className="font-semibold">Explanation: </span>{q.explanation}
                                </div>
                            )}

                            {/* Action Buttons */}
                            <div className="mt-8 flex justify-end gap-3 pt-4 border-t border-slate-100">
                                {marking.isPracticeMode ? (
                                    <>
                                        <button
                                            onClick={() => checkOne(idx)}
                                            className="px-6 py-2 bg-indigo-50 text-indigo-700 rounded-xl font-semibold hover:bg-indigo-100 transition-colors"
                                        >
                                            {fb ? 'Checked' : 'Check Answer'}
                                        </button>
                                        {fb && ['mcq', 'typed', 'calc', 'table_wordbank', 'table'].includes(String(q?.question_type || '')) && (
                                            <button onClick={() => setShowMemo(!showMemo)} className={`px-6 py-2 rounded-xl font-semibold transition-colors border ${showMemo ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'}`}>
                                                {showMemo ? 'Hide Memo' : 'Compare / Memo'}
                                            </button>
                                        )}
                                        <button onClick={() => setShowHint(!showHint)} className={`px-6 py-2 rounded-xl font-semibold transition-colors border ${showHint ? 'bg-amber-50 border-amber-200 text-amber-700' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'}`}>
                                            {showHint ? 'Hide Hint' : 'Hint'}
                                        </button>
                                        {(fb || showHint || showMemo) && (
                                            <button onClick={() => { setFeedbackAt(idx, null); setShowHint(false); setShowMemo(false); }} className="px-6 py-2 bg-white border border-slate-200 text-slate-700 rounded-xl font-semibold hover:bg-slate-50 transition-colors">
                                                Clear feedback
                                            </button>
                                        )}
                                        {currentIndex === questions.length - 1 && (
                                            <button onClick={handleFinishAndReview} className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors">
                                                Finish & Review
                                            </button>
                                        )}
                                    </>
                                ) : (
                                    !marking.isMarkingSubmitted && (
                                        <button
                                            onClick={() => marking.submitAssessment(questions)}
                                            disabled={marking.isSubmitting}
                                            className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors disabled:opacity-50"
                                        >
                                            {marking.isSubmitting ? 'Submitting...' : 'Submit Assessment'}
                                        </button>
                                    )
                                )}
                            </div>

                            {showHint && q?.question_type === 'calc' && (calcHintText || calcFormulaHint) && (
                                <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl text-sm text-yellow-900">
                                    <div className="font-semibold">Calculation hint</div>
                                    {calcFormulaHint && <div className="mt-2 font-medium whitespace-pre-wrap">{calcFormulaHint}</div>}
                                    {calcHintText && <div className="mt-2 whitespace-pre-wrap">{calcHintText}</div>}
                                    {getAnswerPartHints(q).length > 0 && (
                                        <div className="mt-3 space-y-2">
                                            {getAnswerPartHints(q).map((item, hintIndex) => (
                                                <div key={`${item?.label || hintIndex}-${item?.value || ''}`} className="bg-white/70 border border-yellow-200 rounded-lg p-3">
                                                    <div className="font-semibold">{item?.label || `Hint ${hintIndex + 1}`}</div>
                                                    <div className="mt-1 whitespace-pre-wrap">{item?.value}</div>
                                                </div>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            )}

                            {showHint && q?.question_type === 'typed' && Array.isArray(q?.guidelines) && q.guidelines.length > 0 && (
                                <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                                    <div className="font-semibold text-yellow-900">Typed-answer hint</div>
                                    <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                        {q.guidelines.map((item, hintIndex) => <li key={hintIndex}>{item}</li>)}
                                    </ul>
                                    {getAnswerPartHints(q).length > 0 && (
                                        <div className="mt-3 space-y-2">
                                            {getAnswerPartHints(q).map((item, hintIndex) => (
                                                <div key={`${item?.label || hintIndex}-${item?.value || ''}`} className="bg-white/70 border border-yellow-200 rounded-lg p-3 text-sm text-yellow-900">
                                                    <div className="font-semibold">{item?.label || `Hint ${hintIndex + 1}`}</div>
                                                    <div className="mt-1 whitespace-pre-wrap">{item?.value}</div>
                                                </div>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            )}

                            {showHint && q?.question_type === 'table_wordbank' && Array.isArray(q?.guidelines) && q.guidelines.length > 0 && (
                                <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                                    <div className="font-semibold text-yellow-900">Word-bank hint</div>
                                    <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                        {q.guidelines.map((item, hintIndex) => <li key={hintIndex}>{item}</li>)}
                                    </ul>
                                    {wordbankMemoRows.length > 0 && (
                                        <div className="mt-3 space-y-2">
                                            {wordbankMemoRows.map((row) => (
                                                <div key={`hint-${row.rowLabel}`} className="bg-white/70 border border-yellow-200 rounded-lg p-3 text-sm text-yellow-900">
                                                    <div className="font-semibold">{row.rowLabel}</div>
                                                    {row.informalTeaching?.what_to_enter && <div className="mt-1"><span className="font-semibold">Informal:</span> {row.informalTeaching.what_to_enter}</div>}
                                                    {row.formalTeaching?.what_to_enter && <div className="mt-1"><span className="font-semibold">Formal:</span> {row.formalTeaching.what_to_enter}</div>}
                                                </div>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            )}

                            {showHint && q?.question_type === 'table' && Array.isArray(q?.guidelines) && q.guidelines.length > 0 && (
                                <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                                    <div className="font-semibold text-yellow-900">Table hint</div>
                                    <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                        {q.guidelines.map((item, hintIndex) => <li key={hintIndex}>{item}</li>)}
                                    </ul>
                                </div>
                            )}

                            {showMemo && q?.question_type !== 'mcq' && q?.question_type !== 'table_wordbank' && nonTabularMemoItems.length > 0 && (
                                <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
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

                            {showMemo && q?.question_type === 'table_wordbank' && wordbankMemoRows.length > 0 && (
                                <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                                    <div className="font-semibold text-slate-900">Compare / Memo</div>
                                    <div className="mt-3 space-y-3">
                                        {wordbankMemoRows.map((row) => (
                                            <div key={`${row.rowLabel}-${row.informalAnswer}-${row.formalAnswer}`} className="border border-slate-200 rounded-lg p-3 bg-white">
                                                <div className="font-semibold text-slate-900">{row.rowLabel}</div>
                                                {row.informalAnswer && <div className="mt-2"><span className="font-semibold text-slate-900">Informal:</span> {row.informalAnswer}</div>}
                                                {row.formalAnswer && <div className="mt-1"><span className="font-semibold text-slate-900">Formal:</span> {row.formalAnswer}</div>}
                                                {row.informalDerivation && <div className="mt-1"><span className="font-semibold text-slate-900">Why informal:</span> {row.informalDerivation}</div>}
                                                {row.formalDerivation && <div className="mt-1"><span className="font-semibold text-slate-900">Why formal:</span> {row.formalDerivation}</div>}
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}

                            {showMemo && q?.question_type === 'calc' && Object.keys(calcDerivationMap || {}).length > 0 && (
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
                        </div>
                    </div>
                </div>
            )}

            {reviewMode && questions.length > 0 && (
                <div className="space-y-4">
                    <div className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm">
                        <div className="flex flex-wrap items-center justify-between gap-3">
                            <div>
                                <div className="text-lg font-semibold text-slate-900">Review your {questions.length}-question practice set</div>
                                <div className="text-sm text-slate-600">Scroll through every question below and open the memo for any item you want to revisit.</div>
                            </div>
                            <button
                                type="button"
                                onClick={() => {
                                    setReviewMode(false);
                                    setActiveReviewMemoIndex(null);
                                    setCurrentIndex(0);
                                }}
                                className="px-4 py-2 bg-white border border-slate-200 text-slate-700 rounded-xl font-semibold hover:bg-slate-50"
                            >
                                Back to questions
                            </button>
                        </div>
                    </div>
                    <div className="space-y-4">
                        {questions.map((reviewQuestion, reviewIndex) => renderReviewQuestion(reviewQuestion, reviewIndex))}
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
                        Review your answers above. The feedback is now displayed securely from the backend!
                    </p>
                </div>
            )}
        </>
    );
};

export default Grade10AccountingIndigenousPractice;

