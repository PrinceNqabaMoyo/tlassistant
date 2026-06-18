import React, { useState, useEffect } from 'react';
import MCQOption from '../../../shared/MCQOption';
import { useGrade10AccountingMarking } from '../useGrade10AccountingMarking';

const normalizeText = (v) => v == null ? '' : String(v).trim().replace(/\s+/g, ' ').toLowerCase();

const toNumber = (value) => {
    if (value === null || value === undefined) return null;
    let s = String(value).trim();
    if (!s) return null;
    s = s.replace(/\s+/g, '');
    s = s.replace(/[Rr]/g, '');
    const lastDot = s.lastIndexOf('.');
    const lastComma = s.lastIndexOf(',');
    if (lastDot >= 0 && lastComma >= 0) {
        const decSep = lastDot > lastComma ? '.' : ',';
        const thouSep = decSep === '.' ? ',' : '.';
        s = s.split(thouSep).join('');
        if (decSep === ',') s = s.replace(',', '.');
    } else if (lastComma >= 0) {
        s = s.split('.').join('');
        s = s.replace(',', '.');
    } else {
        s = s.split(',').join('');
    }
    s = s.replace(/[^0-9.\-]/g, '');
    const n = Number(s);
    return Number.isFinite(n) ? n : null;
};

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
        if (question?.question_type === 'typed' && sampleAnswer) {
            baseItems.push({ label: 'Guideline answer', value: sampleAnswer });
        }
        return [...baseItems, ...derivationItems.filter((item) => item.label.toLowerCase() !== 'guideline answer')];
    }

    if (question?.question_type === 'calc') {
        const items = [];
        const formulaHint = String(question?.formula_hint || '').trim();
        const formula = String(question?.working_formula || '').trim();
        if (formulaHint) items.push({ label: 'Formula hint', value: formulaHint });
        if (formula) items.push({ label: 'Working', value: formula });
        if (question?.correct_answer !== null && question?.correct_answer !== undefined && String(question.correct_answer).trim() !== '') {
            const unit = String(question?.unit || '').trim() || 'R';
            items.push({ label: 'Correct answer', value: `${unit}${question.correct_answer}`.trim() });
        }
        return items;
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
        labelById[String(token.id)] = String(token.label || '').trim();
    });
    return Object.keys(correctMap)
        .sort((a, b) => Number(a) - Number(b))
        .map((rowKey) => {
            const row = rows[Number(rowKey)] || [];
            const tokenId = correctMap?.[rowKey]?.['2'];
            const cellKey = `${rowKey}:2`;
            return {
                rowLabel: String(row?.[0] || Number(rowKey) + 1),
                definition: String(row?.[1] || '').trim(),
                answer: labelById[String(tokenId)] || '',
                teaching: cellTeachingMap?.[cellKey] || null,
                derivation: String(derivationMap?.[cellKey] || '').trim(),
            };
        })
        .filter((item) => item.answer);
};

const Grade10AccountingVATPractice = ({
    onBack,
    g10AcctVATVisualAidsOpen, setG10AcctVATVisualAidsOpen,
    g10AcctVATPracticeDifficulty, setG10AcctVATPracticeDifficulty,
    fetchGrade10AcctVATPractice,
    g10AcctVATPracticeLoading, g10AcctVATPracticeError, g10AcctVATPracticeQuestions,
    g10AcctVATPracticeAnswers, setG10AcctVATPracticeAnswers,
    g10AcctVATPracticeFeedback, setG10AcctVATPracticeFeedback,
    renderGrade10AcctVATVisualAids, hideConfig,
}) => {
    const questions = Array.isArray(g10AcctVATPracticeQuestions) ? g10AcctVATPracticeQuestions : [];
    const [currentIndex, setCurrentIndex] = useState(0);
    const [showMemo, setShowMemo] = useState(false);
    const [showHint, setShowHint] = useState(false);
    const [reviewMode, setReviewMode] = useState(false);
    const [activeReviewMemoIndex, setActiveReviewMemoIndex] = useState(null);
    const marking = useGrade10AccountingMarking();

    useEffect(() => {
        if (questions.length > 0) marking.setMarkingMode('practice');
    }, [questions, marking]);

    useEffect(() => {
        setCurrentIndex(0);
        setShowMemo(false);
        setShowHint(false);
        setReviewMode(false);
        setActiveReviewMemoIndex(null);
    }, [questions]);

    const handleNext = () => {
        if (reviewMode) return;
        if (currentIndex < questions.length - 1) setCurrentIndex((prev) => prev + 1);
    };

    const handlePrev = () => {
        if (reviewMode) return;
        if (currentIndex > 0) setCurrentIndex((prev) => prev - 1);
    };

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g10AcctVATPracticeAnswers) ? [...g10AcctVATPracticeAnswers] : [];
        answers[idx] = value;
        setG10AcctVATPracticeAnswers(answers);
        if (questions[idx]) marking.registerAnswer(questions[idx].id, value);
        const feedback = Array.isArray(g10AcctVATPracticeFeedback) ? [...g10AcctVATPracticeFeedback] : [];
        feedback[idx] = null;
        setG10AcctVATPracticeFeedback(feedback);
        if (idx === currentIndex) setShowMemo(false);
    };

    useEffect(() => {
        if (!questions.length) return;
        if (!Array.isArray(g10AcctVATPracticeAnswers) || g10AcctVATPracticeAnswers.length !== questions.length) {
            setG10AcctVATPracticeAnswers(questions.map((question) => {
                if (question.question_type === 'table_wordbank') return buildEmptyWordbankAnswer(question);
                return '';
            }));
        }
        if (!Array.isArray(g10AcctVATPracticeFeedback) || g10AcctVATPracticeFeedback.length !== questions.length) {
            setG10AcctVATPracticeFeedback(questions.map(() => null));
        }
    }, [questions.length]);

    const setFeedbackAt = (idx, value) => {
        const next = Array.isArray(g10AcctVATPracticeFeedback) ? g10AcctVATPracticeFeedback.slice() : [];
        next[idx] = value;
        setG10AcctVATPracticeFeedback(next);
    };

    const evaluateQuestion = (question, userValue) => {
        if (!question) return { kind: 'error', message: 'Unable to review this answer.' };

        if (question.question_type === 'mcq') {
            const ok = String(userValue) === String(question.correct_index);
            return ok
                ? { kind: 'success', message: '0 of 1 responses incorrect.' }
                : { kind: 'error', message: `1 of 1 responses incorrect. Correct answer: ${question.options?.[question.correct_index] || ''}` };
        }

        if (question.question_type === 'calc') {
            const expected = parseFloat(question.correct_answer);
            const got = toNumber(userValue);
            if (got === null) return { kind: 'error', message: '1 of 1 responses incorrect. Enter a number first.' };
            const ok = Number.isFinite(expected) && Math.abs(expected - got) < 0.01;
            return ok
                ? { kind: 'success', message: '0 of 1 responses incorrect.' }
                : { kind: 'error', message: `1 of 1 responses incorrect. Correct answer: ${(question.unit || 'R')}${expected.toFixed(2)}` };
        }

        if (question.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(question);
            const answerState = (userValue && typeof userValue === 'object') ? userValue : buildEmptyWordbankAnswer(question);
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
            return ok
                ? { kind: 'success', message: `0 of ${total} responses incorrect.` }
                : { kind: 'error', message: `${total - hit} of ${total} responses incorrect.` };
        }

        if (question.question_type === 'typed') {
            const ok = normalizeText(userValue).length > 0;
            return ok
                ? { kind: 'info', message: '0 of 1 responses missing. Compare with the memo below.' }
                : { kind: 'error', message: '1 of 1 responses missing. Write an answer first.' };
        }

        return { kind: 'info', message: 'Saved.' };
    };

    const checkOne = (question, idx) => {
        if (!question) return;
        const answer = Array.isArray(g10AcctVATPracticeAnswers) ? g10AcctVATPracticeAnswers[idx] : null;
        setFeedbackAt(idx, evaluateQuestion(question, answer));
    };

    const handleFinishAndReview = () => {
        const answers = Array.isArray(g10AcctVATPracticeAnswers) ? g10AcctVATPracticeAnswers : [];
        setG10AcctVATPracticeFeedback(questions.map((question, idx) => evaluateQuestion(question, answers[idx])));
        setActiveReviewMemoIndex(null);
        setShowMemo(false);
        setShowHint(false);
        setReviewMode(true);
    };

    const renderWordbankTable = (question, idx, { readOnly = false, useCorrectAnswers = false } = {}) => {
        const ans = (g10AcctVATPracticeAnswers?.[idx] && typeof g10AcctVATPracticeAnswers[idx] === 'object')
            ? g10AcctVATPracticeAnswers[idx]
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

        const setActiveTokenId = (tokenId) => setAnswer(idx, { ...(ans || {}), activeTokenId: tokenId });
        const clearCell = (rowIndex) => {
            setAnswer(idx, { ...(ans || {}), selections: { ...(ans?.selections || {}), [String(rowIndex)]: { ...((ans?.selections || {})[String(rowIndex)] || {}), '2': null } } });
        };
        const placeActive = (rowIndex) => {
            const tokenId = ans?.activeTokenId;
            if (!tokenId || used.has(String(tokenId))) return;
            setAnswer(idx, {
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
                                                    {teaching?.record_link && <div><span className="font-semibold">Record link:</span> {teaching.record_link}</div>}
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

    const renderReviewQuestion = (reviewQuestion, idx) => {
        const reviewFeedback = Array.isArray(g10AcctVATPracticeFeedback) ? g10AcctVATPracticeFeedback[idx] : null;
        const memoOpen = activeReviewMemoIndex === idx;
        const reviewMemoItems = reviewQuestion && reviewQuestion?.question_type !== 'mcq' && reviewQuestion?.question_type !== 'table_wordbank'
            ? buildNonTabularMemoItems(reviewQuestion)
            : [];

        return (
            <div key={reviewQuestion?.id || idx} className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm space-y-4">
                <div className="flex flex-wrap items-start justify-between gap-3">
                    <div>
                        <div className="text-sm font-semibold text-slate-500">Question {idx + 1} of {questions.length}</div>
                        <div className="text-lg font-medium text-slate-900 whitespace-pre-wrap">{reviewQuestion?.prompt}</div>
                    </div>
                    {['typed', 'calc', 'table_wordbank'].includes(String(reviewQuestion?.question_type || '')) && (
                        <button
                            type="button"
                            onClick={() => setActiveReviewMemoIndex(memoOpen ? null : idx)}
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
                        Your answer: {String(g10AcctVATPracticeAnswers?.[idx] || '').trim() || 'No answer entered'}
                    </div>
                )}

                {reviewQuestion?.question_type === 'typed' && (
                    <div className="p-3 rounded-xl border border-slate-200 bg-slate-50 text-slate-700 text-sm whitespace-pre-wrap">
                        {String(g10AcctVATPracticeAnswers?.[idx] || '').trim() || 'No answer entered'}
                    </div>
                )}

                {reviewQuestion?.question_type === 'table_wordbank' && renderWordbankTable(reviewQuestion, idx, { readOnly: true })}

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

                {memoOpen && reviewQuestion?.question_type === 'table_wordbank' && (
                    <div className="space-y-3">
                        <div className="text-sm font-semibold text-slate-900">Compare / Memo</div>
                        {renderWordbankTable(reviewQuestion, idx, { readOnly: true, useCorrectAnswers: true })}
                    </div>
                )}
            </div>
        );
    };

    const q = questions[currentIndex];
    const ans = g10AcctVATPracticeAnswers?.[currentIndex];
    const feedback = g10AcctVATPracticeFeedback?.[currentIndex];
    const nonTabularMemoItems = q && q?.question_type !== 'mcq' && q?.question_type !== 'table_wordbank' ? buildNonTabularMemoItems(q) : [];
    const wordbankMemoRows = q?.question_type === 'table_wordbank' ? buildWordbankMemoRows(q) : [];
    const calcHintText = String(q?.working_formula || '').trim();
    const calcFormulaHint = String(q?.formula_hint || '').trim();
    const calcDerivationMap = getDerivationMap(q);

    return (
        <>
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-slate-800">Practice Mode</h3>
                {questions.length > 0 && (
                    <div className="flex items-center gap-3 bg-white px-4 py-2 rounded-xl border border-slate-200">
                        <span className="text-sm font-semibold text-slate-700">Mode:</span>
                        <button onClick={marking.toggleMarkingMode} disabled={marking.isSubmitting}
                            className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${!marking.isPracticeMode ? 'bg-indigo-600' : 'bg-slate-200'}`}>
                            <span className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${!marking.isPracticeMode ? 'translate-x-6' : 'translate-x-1'}`} />
                        </button>
                        <span className="text-sm text-slate-600">{marking.isPracticeMode ? 'Practice' : 'Marking'}</span>
                    </div>
                )}
            </div>

            {marking.markingError && <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">{marking.markingError}</div>}
            {g10AcctVATPracticeLoading && <div className="text-sm text-slate-500">Loading...</div>}
            {g10AcctVATPracticeError && <div className="text-sm text-red-700 break-words">{g10AcctVATPracticeError}</div>}
            {!g10AcctVATPracticeLoading && questions.length === 0 && <div className="text-sm text-slate-500">Click "Generate Question" to start.</div>}

            {q && !reviewMode && (
                <div className="space-y-4">
                    <div className="flex items-center justify-between bg-slate-50 p-3 rounded-xl border border-slate-200">
                        <div className="text-sm font-semibold text-slate-700">Question {currentIndex + 1} of {questions.length}</div>
                        <div className="flex items-center gap-2">
                            <button onClick={handlePrev} disabled={currentIndex === 0} className="px-3 py-1.5 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-700 hover:bg-slate-50 disabled:opacity-50">Previous</button>
                            <button onClick={handleNext} disabled={currentIndex === questions.length - 1} className="px-3 py-1.5 bg-white border border-slate-200 rounded-lg text-sm font-semibold text-slate-700 hover:bg-slate-50 disabled:opacity-50">Next</button>
                        </div>
                    </div>

                    <div className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm">
                        <div className="text-lg font-medium text-slate-800 whitespace-pre-wrap">{q.prompt}</div>
                        <div className="mt-6">
                            {q.question_type === 'mcq' && (
                                <div className="grid grid-cols-1 gap-2">
                                    {(q.options || []).map((opt, oIdx) => <MCQOption key={oIdx} selected={String(ans) === String(oIdx)} onClick={() => setAnswer(currentIndex, String(oIdx))} label={opt} />)}
                                </div>
                            )}
                            {q.question_type === 'calc' && (
                                <div className="flex items-center gap-2">
                                    <span className="text-slate-500 font-medium">R</span>
                                    <input type="number" step="0.01" className="w-full max-w-xs p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-400" placeholder="0.00" value={typeof ans === 'string' ? ans : ''} onChange={(e) => setAnswer(currentIndex, e.target.value)} />
                                </div>
                            )}
                            {q.question_type === 'typed' && (
                                <div>
                                    <textarea value={typeof ans === 'string' ? ans : ''} onChange={(e) => setAnswer(currentIndex, e.target.value)} placeholder="Write your answer..." className="w-full min-h-[110px] p-3 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-slate-300" />
                                </div>
                            )}
                            {q.question_type === 'table_wordbank' && renderWordbankTable(q, currentIndex)}
                        </div>
                        <div className="mt-8 flex justify-end gap-3 pt-4 border-t border-slate-100">
                            {marking.isPracticeMode ? (
                                <>
                                    <button onClick={() => checkOne(q, currentIndex)} className="px-6 py-2 bg-indigo-50 text-indigo-700 rounded-xl font-semibold hover:bg-indigo-100 transition-colors">{feedback ? 'Checked' : 'Check Answer'}</button>
                                    {feedback && ['typed', 'calc', 'table_wordbank'].includes(String(q?.question_type || '')) && (
                                        <button onClick={() => setShowMemo(!showMemo)} className={`px-6 py-2 rounded-xl font-semibold transition-colors border ${showMemo ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'}`}>
                                            {showMemo ? 'Hide Memo' : 'Compare / Memo'}
                                        </button>
                                    )}
                                    <button onClick={() => setShowHint(!showHint)} className={`px-6 py-2 rounded-xl font-semibold transition-colors border ${showHint ? 'bg-amber-50 border-amber-200 text-amber-700' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'}`}>
                                        {showHint ? 'Hide Hint' : 'Hint'}
                                    </button>
                                    {(feedback || showHint || showMemo) && (
                                        <button onClick={() => { setFeedbackAt(currentIndex, null); setShowHint(false); setShowMemo(false); }} className="px-6 py-2 bg-white border border-slate-200 text-slate-700 rounded-xl font-semibold hover:bg-slate-50 transition-colors">
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
                                !marking.isMarkingSubmitted && <button onClick={() => marking.submitAssessment(questions)} disabled={marking.isSubmitting} className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors disabled:opacity-50">{marking.isSubmitting ? 'Submitting...' : 'Submit Assessment'}</button>
                            )}
                        </div>
                        {feedback && marking.isPracticeMode && (
                            <div className={`mt-3 p-3 rounded-xl text-sm border ${feedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : feedback.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                                {feedback.message}
                            </div>
                        )}
                        {showHint && q?.question_type === 'calc' && calcHintText && (
                            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl text-sm text-yellow-900">
                                <div className="font-semibold">Calculation hint</div>
                                {calcFormulaHint && <div className="mt-2 font-medium whitespace-pre-wrap">{calcFormulaHint}</div>}
                                <div className="mt-2 whitespace-pre-wrap">{calcHintText}</div>
                                {getAnswerPartHints(q).length > 0 && (
                                    <div className="mt-3 space-y-2">
                                        {getAnswerPartHints(q).map((item, idx) => (
                                            <div key={`${item?.label || idx}-${item?.value || ''}`} className="bg-white/70 border border-yellow-200 rounded-lg p-3">
                                                <div className="font-semibold">{item?.label || `Hint ${idx + 1}`}</div>
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
                                    {q.guidelines.map((item, index) => <li key={index}>{item}</li>)}
                                </ul>
                                {getAnswerPartHints(q).length > 0 && (
                                    <div className="mt-3 space-y-2">
                                        {getAnswerPartHints(q).map((item, idx) => (
                                            <div key={`${item?.label || idx}-${item?.value || ''}`} className="bg-white/70 border border-yellow-200 rounded-lg p-3 text-sm text-yellow-900">
                                                <div className="font-semibold">{item?.label || `Hint ${idx + 1}`}</div>
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
                                    {q.guidelines.map((item, index) => <li key={index}>{item}</li>)}
                                </ul>
                                {wordbankMemoRows.length > 0 && (
                                    <div className="mt-3 space-y-2">
                                        {wordbankMemoRows.map((row) => (
                                            <div key={`hint-${row.rowLabel}-${row.answer}`} className="bg-white/70 border border-yellow-200 rounded-lg p-3 text-sm text-yellow-900">
                                                <div className="font-semibold">Row {row.rowLabel}</div>
                                                {row.teaching?.what_to_enter && <div className="mt-1"><span className="font-semibold">What to enter:</span> {row.teaching.what_to_enter}</div>}
                                                {row.teaching?.where_to_look && <div className="mt-1"><span className="font-semibold">Where to look:</span> {row.teaching.where_to_look}</div>}
                                                {row.teaching?.method_or_formula && <div className="mt-1"><span className="font-semibold">Rule:</span> {row.teaching.method_or_formula}</div>}
                                            </div>
                                        ))}
                                    </div>
                                )}
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
                                        <div key={`${row.rowLabel}-${row.answer}`} className="border border-slate-200 rounded-lg p-3 bg-white">
                                            <div className="font-semibold text-slate-900">Row {row.rowLabel}</div>
                                            <div className="mt-1 text-slate-600">{row.definition}</div>
                                            <div className="mt-2"><span className="font-semibold text-slate-900">Correct term:</span> {row.answer}</div>
                                            {row.teaching?.what_to_enter && <div className="mt-2"><span className="font-semibold text-slate-900">What to enter:</span> {row.teaching.what_to_enter}</div>}
                                            {row.teaching?.where_to_look && <div className="mt-1"><span className="font-semibold text-slate-900">Where to look:</span> {row.teaching.where_to_look}</div>}
                                            {row.teaching?.method_or_formula && <div className="mt-1"><span className="font-semibold text-slate-900">Rule:</span> {row.teaching.method_or_formula}</div>}
                                            {row.teaching?.record_link && <div className="mt-1"><span className="font-semibold text-slate-900">Record link:</span> {row.teaching.record_link}</div>}
                                            {row.derivation && <div className="mt-1"><span className="font-semibold text-slate-900">Why:</span> {row.derivation}</div>}
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
            )}

            {reviewMode && questions.length > 0 && (
                <div className="space-y-4">
                    <div className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm">
                        <div className="flex flex-wrap items-center justify-between gap-3">
                            <div>
                                <div className="text-lg font-semibold text-slate-900">Review your 8-question practice set</div>
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
                        {questions.map((reviewQuestion, idx) => renderReviewQuestion(reviewQuestion, idx))}
                    </div>
                </div>
            )}
        </>
    );
};

export default Grade10AccountingVATPractice;

