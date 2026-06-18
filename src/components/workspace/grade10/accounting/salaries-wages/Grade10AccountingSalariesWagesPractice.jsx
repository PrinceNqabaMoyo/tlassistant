import React, { useState, useEffect } from 'react';
import MCQOption from '../../../shared/MCQOption';
import { useGrade10AccountingMarking } from '../useGrade10AccountingMarking';

const normalizeText = (value) => {
    if (value === null || value === undefined) return '';
    return String(value).trim().replace(/\s+/g, ' ').toLowerCase();
};

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

const numbersMatch = (actual, expected) => {
    const actualN = typeof actual === 'number' ? actual : toNumber(actual);
    const expectedN = typeof expected === 'number' ? expected : toNumber(expected);
    if (actualN === null || expectedN === null) return false;
    return Math.abs(actualN - expectedN) <= 0.01;
};

const getWordBank = (question) => Array.isArray(question?.word_bank) ? question.word_bank : [];
const getCorrectMap = (question) => (question?.correct_map && typeof question.correct_map === 'object') ? question.correct_map : {};

const buildEmptyJournalAnswer = (question) => {
    const journals = Array.isArray(question?.journals)
        ? question.journals
        : (question?.journal ? [question.journal] : []);
    const cells = {};
    journals.forEach((journal) => {
        const rows = Array.isArray(journal?.rows) ? journal.rows : [];
        rows.forEach((row) => {
            (Array.isArray(row) ? row : []).forEach((cell) => {
                if (!cell?.cell_id) return;
                cells[String(cell.cell_id)] = cell?.value || '';
            });
        });
    });
    return { cells, extra_rows_by_table: {} };
};

const buildNonTabularHintItems = (question) => {
    const explicitItems = Array.isArray(question?.answer_part_hints) ? question.answer_part_hints : [];
    const normalizedExplicit = explicitItems
        .map((item, idx) => ({
            label: String(item?.label || `Answer part ${idx + 1}`).trim(),
            value: String(item?.value || '').trim(),
        }))
        .filter((item) => item.value);
    if (normalizedExplicit.length > 0) return normalizedExplicit;

    if (question?.question_type === 'calc') {
        const items = [];
        const formula = String(question?.working_formula || '').trim();
        if (formula) items.push({ label: 'Working', value: formula });
        if (question?.correct_answer !== null && question?.correct_answer !== undefined && String(question.correct_answer).trim() !== '') {
            const unit = String(question?.unit || '').trim();
            items.push({ label: 'Correct answer', value: `${unit}${question.correct_answer}`.trim() });
        }
        return items;
    }

    return String(question?.sample_answer || '')
        .split('\n')
        .map((line) => line.trim())
        .filter(Boolean)
        .map((line, idx) => ({ label: `Memo point ${idx + 1}`, value: line }));
};

const buildWordbankMemoRows = (question) => {
    const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
    const wordBank = getWordBank(question);
    const correctMap = getCorrectMap(question);
    const labelById = {};
    wordBank.forEach((token) => {
        labelById[String(token.id)] = String(token.label || '').trim();
    });
    return Object.keys(correctMap)
        .sort((a, b) => Number(a) - Number(b))
        .map((rowKey) => {
            const row = rows[Number(rowKey)] || [];
            const tokenId = correctMap?.[rowKey]?.['2'];
            return {
                rowLabel: String(row?.[0] || Number(rowKey) + 1),
                definition: String(row?.[1] || '').trim(),
                answer: labelById[String(tokenId)] || '',
            };
        })
        .filter((item) => item.answer);
};

const buildTypedHintSections = (question) => {
    const sections = [];
    const guidelines = Array.isArray(question?.guidelines) ? question.guidelines.map((item) => String(item || '').trim()).filter(Boolean) : [];
    const memoLabels = Array.isArray(question?.answer_part_hints)
        ? question.answer_part_hints.map((item) => String(item?.label || '').trim()).filter(Boolean)
        : [];

    if (guidelines.length > 0) {
        sections.push({ title: 'What to include', text: guidelines.join('\n') });
    }
    if (memoLabels.length > 0) {
        sections.push({ title: 'Memo structure', text: memoLabels.join('\n') });
    }
    return sections;
};

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

const shouldHandleEnterCheck = (event) => {
    if (event.key !== 'Enter' || event.nativeEvent?.isComposing) return false;
    const tagName = String(event.target?.tagName || '').toLowerCase();
    if (tagName === 'textarea') return !event.shiftKey;
    return tagName === 'input';
};

const Grade10AccountingSalariesWagesPractice = ({
    onBack,
    g10AcctSWVisualAidsOpen,
    setG10AcctSWVisualAidsOpen,
    g10AcctSWPracticeDifficulty,
    setG10AcctSWPracticeDifficulty,
    fetchGrade10AcctSWPractice,
    g10AcctSWPracticeLoading,
    g10AcctSWPracticeError,
    g10AcctSWPracticeQuestions,
    g10AcctSWPracticeAnswers,
    setG10AcctSWPracticeAnswers,
    g10AcctSWPracticeFeedback,
    setG10AcctSWPracticeFeedback,
    renderGrade10AcctSWVisualAids,
    currentIndex: externalCurrentIndex,
    setCurrentIndex: externalSetCurrentIndex,
    hideConfig,
}) => {
    const questions = Array.isArray(g10AcctSWPracticeQuestions) ? g10AcctSWPracticeQuestions : [];
    const [internalCurrentIndex, setInternalCurrentIndex] = useState(0);
    const [showMemo, setShowMemo] = useState(false);
    const [showHint, setShowHint] = useState(false);
    const [reviewMode, setReviewMode] = useState(false);
    const [activeReviewMemoIndex, setActiveReviewMemoIndex] = useState(null);
    const marking = useGrade10AccountingMarking();
    const currentIndex = typeof externalCurrentIndex === 'number' ? externalCurrentIndex : internalCurrentIndex;
    const setCurrentIndex = typeof externalSetCurrentIndex === 'function' ? externalSetCurrentIndex : setInternalCurrentIndex;

    useEffect(() => {
        if (questions.length > 0) marking.setMarkingMode('practice');
    }, [questions, marking]);

    useEffect(() => {
        setReviewMode(false);
        setActiveReviewMemoIndex(null);
        if (typeof setCurrentIndex === 'function') setCurrentIndex(0);
    }, [questions, setCurrentIndex]);

    const handleNext = () => {
        if (reviewMode) return;
        if (typeof setCurrentIndex !== 'function') return;
        if (currentIndex < questions.length - 1) setCurrentIndex(currentIndex + 1);
    };
    const handlePrev = () => {
        if (reviewMode) return;
        if (typeof setCurrentIndex !== 'function') return;
        if (currentIndex > 0) setCurrentIndex(currentIndex - 1);
    };

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g10AcctSWPracticeAnswers) ? [...g10AcctSWPracticeAnswers] : [];
        answers[idx] = value;
        setG10AcctSWPracticeAnswers(answers);
        if (questions[idx]) marking.registerAnswer(questions[idx].id, value);
        const feedback = Array.isArray(g10AcctSWPracticeFeedback) ? [...g10AcctSWPracticeFeedback] : [];
        feedback[idx] = null;
        setG10AcctSWPracticeFeedback(feedback);
        if (idx === currentIndex) setShowMemo(false);
    };

    useEffect(() => {
        if (!questions.length) return;
        if (!Array.isArray(g10AcctSWPracticeAnswers) || g10AcctSWPracticeAnswers.length !== questions.length) {
            setG10AcctSWPracticeAnswers(questions.map((q) => {
                if (q.question_type === 'journal' || q.question_type === 'ledger') return buildEmptyJournalAnswer(q);
                if (q.question_type === 'table_wordbank') return buildEmptyWordbankAnswer(q);
                return '';
            }));
        }
        if (!Array.isArray(g10AcctSWPracticeFeedback) || g10AcctSWPracticeFeedback.length !== questions.length) {
            setG10AcctSWPracticeFeedback(questions.map(() => null));
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [questions.length]);

    const setFeedbackAt = (idx, value) => {
        const next = Array.isArray(g10AcctSWPracticeFeedback) ? g10AcctSWPracticeFeedback.slice() : [];
        next[idx] = value;
        setG10AcctSWPracticeFeedback(next);
    };

    const buildReviewResult = ({
        kind,
        message,
        isCorrect,
        correctCount,
        totalCount,
        cellResults = {},
    }) => ({
        kind,
        message,
        isCorrect,
        correctCount,
        totalCount,
        wrongCount: Math.max(0, (Number(totalCount) || 0) - (Number(correctCount) || 0)),
        cellResults,
    });

    const evaluateQuestion = (q, userValue) => {
        if (!q) {
            return buildReviewResult({
                kind: 'error',
                message: 'Unable to review this answer.',
                isCorrect: false,
                correctCount: 0,
                totalCount: 1,
            });
        }

        if (q.question_type === 'mcq') {
            const ok = String(userValue) === String(q.correct_index);
            return buildReviewResult({
                kind: ok ? 'success' : 'error',
                message: ok ? '0 of 1 responses incorrect.' : `1 of 1 responses incorrect. Correct answer: ${q.options?.[q.correct_index] || ''}`,
                isCorrect: ok,
                correctCount: ok ? 1 : 0,
                totalCount: 1,
            });
        }

        if (q.question_type === 'calc') {
            const expected = parseFloat(q.correct_answer);
            const got = toNumber(userValue);
            if (got === null) {
                return buildReviewResult({
                    kind: 'error',
                    message: '1 of 1 responses incorrect. Enter a number first.',
                    isCorrect: false,
                    correctCount: 0,
                    totalCount: 1,
                });
            }
            const ok = Number.isFinite(expected) && Math.abs(expected - got) < 0.01;
            return buildReviewResult({
                kind: ok ? 'success' : 'error',
                message: ok ? '0 of 1 responses incorrect.' : `1 of 1 responses incorrect. Correct answer: ${(q.unit || 'R')}${expected.toFixed(2)}`,
                isCorrect: ok,
                correctCount: ok ? 1 : 0,
                totalCount: 1,
            });
        }

        if (q.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(q);
            const answerState = (userValue && typeof userValue === 'object') ? userValue : buildEmptyWordbankAnswer(q);
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
            return buildReviewResult({
                kind: ok ? 'success' : 'error',
                message: ok ? `0 of ${total} responses incorrect.` : `${total - hit} of ${total} responses incorrect.`,
                isCorrect: ok,
                correctCount: hit,
                totalCount: total,
            });
        }

        if (q.question_type === 'typed') {
            const ok = normalizeText(userValue).length > 0;
            return buildReviewResult({
                kind: ok ? 'info' : 'error',
                message: ok ? '0 of 1 responses missing. Compare with the memo below.' : '1 of 1 responses missing. Write an answer first.',
                isCorrect: ok ? null : false,
                correctCount: ok ? 1 : 0,
                totalCount: 1,
            });
        }

        if (q.question_type === 'journal' || q.question_type === 'ledger') {
            const expectedMap = getCorrectMap(q);
            const answerState = (userValue && typeof userValue === 'object') ? userValue : buildEmptyJournalAnswer(q);
            const cells = answerState?.cells && typeof answerState.cells === 'object' ? answerState.cells : {};
            const keys = Object.keys(expectedMap);
            const cellResults = {};
            let hit = 0;
            keys.forEach((key) => {
                const expected = expectedMap[key];
                const got = cells[key];
                const ok = normalizeText(got) === normalizeText(expected) || numbersMatch(got, expected);
                if (ok) hit += 1;
                cellResults[key] = { isCorrect: ok, expected, actual: got };
            });
            const ok = keys.length > 0 && hit === keys.length;
            return buildReviewResult({
                kind: ok ? 'success' : 'error',
                message: ok ? `0 of ${keys.length} cells incorrect.` : `${keys.length - hit} of ${keys.length} cells incorrect.`,
                isCorrect: ok,
                correctCount: hit,
                totalCount: keys.length,
                cellResults,
            });
        }

        return buildReviewResult({
            kind: 'info',
            message: 'Saved.',
            isCorrect: null,
            correctCount: 1,
            totalCount: 1,
        });
    };

    const checkOne = (q, idx) => {
        if (!q) return;
        const ans = Array.isArray(g10AcctSWPracticeAnswers) ? g10AcctSWPracticeAnswers[idx] : null;
        setFeedbackAt(idx, evaluateQuestion(q, ans));
    };

    const handleFinishAndReview = () => {
        const answers = Array.isArray(g10AcctSWPracticeAnswers) ? g10AcctSWPracticeAnswers : [];
        const feedback = questions.map((question, idx) => evaluateQuestion(question, answers[idx]));
        setG10AcctSWPracticeFeedback(feedback);
        setActiveReviewMemoIndex(null);
        setShowMemo(false);
        setShowHint(false);
        setReviewMode(true);
    };

    const renderWordbankTable = (q, idx, { readOnly = false, useCorrectAnswers = false } = {}) => {
        const ans = (g10AcctSWPracticeAnswers?.[idx] && typeof g10AcctSWPracticeAnswers[idx] === 'object')
            ? g10AcctSWPracticeAnswers[idx]
            : buildEmptyWordbankAnswer(q);
        const wordBank = getWordBank(q);
        const used = getUsedTokenIds(ans);
        const tokenLabelById = {};
        wordBank.forEach((t) => { tokenLabelById[String(t.id)] = t.label; });
        const correctMap = getCorrectMap(q);

        const setActiveTokenId = (tokenId) => setAnswer(idx, { ...(ans || {}), activeTokenId: tokenId });
        const clearCell = (rowIndex) => {
            setAnswer(idx, { ...(ans || {}), selections: { ...(ans?.selections || {}), [String(rowIndex)]: { ...((ans?.selections || {})[String(rowIndex)] || {}), '2': null } } });
        };
        const placeActive = (rowIndex) => {
            const tokenId = ans?.activeTokenId;
            if (!tokenId || used.has(String(tokenId))) return;
            setAnswer(idx, { ...(ans || {}), selections: { ...(ans?.selections || {}), [String(rowIndex)]: { ...((ans?.selections || {})[String(rowIndex)] || {}), '2': String(tokenId) } }, activeTokenId: null });
        };

        const rows = Array.isArray(q?.table?.rows) ? q.table.rows : [];
        const headers = Array.isArray(q?.table?.headers) ? q.table.headers : [];

        return (
            <div className="mt-3">
                {!readOnly && (
                    <div className="mb-3">
                        <div className="text-sm font-semibold text-gray-900 mb-2">Word bank</div>
                        <div className="flex flex-wrap gap-2">
                            {wordBank.map((t) => {
                                const isUsed = used.has(String(t.id));
                                const isActive = String(ans?.activeTokenId) === String(t.id);
                                return (
                                    <button key={t.id} type="button" disabled={isUsed} onClick={() => setActiveTokenId(String(t.id))}
                                        className={`px-3 py-1 rounded-full text-sm font-semibold border ${isUsed ? 'bg-gray-100 text-gray-400 border-gray-200' : isActive ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}>
                                        {t.label}
                                    </button>
                                );
                            })}
                        </div>
                    </div>
                )}
                <div className="overflow-x-auto">
                    <table className="min-w-full border border-gray-200 text-sm">
                        <thead className="bg-gray-50"><tr>{headers.map((h, i) => (<th key={i} className="px-3 py-2 border-b border-gray-200 text-left font-semibold text-gray-900">{h}</th>))}</tr></thead>
                        <tbody>
                            {rows.map((row, rowIndex) => {
                                const selectedId = useCorrectAnswers ? correctMap?.[String(rowIndex)]?.['2'] : ans?.selections?.[String(rowIndex)]?.['2'];
                                const label = selectedId ? tokenLabelById[String(selectedId)] : '';
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
                                        </td>
                                        {row[3] !== undefined && <td className="px-3 py-2 border-b border-gray-200">{row[3] || ''}</td>}
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>
            </div>
        );
    };

    const renderOneJournalTable = (q, idx, journal, tableIndex, { readOnly = false, cellValues = null } = {}) => {
        if (!journal) return null;
        const headers = Array.isArray(journal?.headers) ? journal.headers : [];
        const headerRows = Array.isArray(journal?.header_rows) ? journal.header_rows : [];
        const rows = Array.isArray(journal?.rows) ? journal.rows : [];
        const ans = (g10AcctSWPracticeAnswers?.[idx] && typeof g10AcctSWPracticeAnswers[idx] === 'object')
            ? g10AcctSWPracticeAnswers[idx]
            : buildEmptyJournalAnswer(q);
        const cells = cellValues && typeof cellValues === 'object' ? cellValues : (ans?.cells && typeof ans.cells === 'object' ? ans.cells : {});

        const tableStyle = { width: '100%', minWidth: `${Math.max(headers.length * 112, 720)}px`, borderCollapse: 'collapse', tableLayout: 'fixed' };
        const headerStyle = { border: '1px solid #000', padding: '6px', background: '#e5e7eb', fontWeight: 600, textAlign: 'center', verticalAlign: 'middle' };
        const bodyStyle = { border: '1px solid #000', padding: 0, verticalAlign: 'top' };

        return (
            <div className="mt-3 overflow-x-auto">
                <table style={tableStyle}>
                    <thead>
                        {headerRows.length > 0 ? headerRows.map((row, rowIndex) => (
                            <tr key={rowIndex}>
                                {row.map((cell, cellIndex) => {
                                    const label = (cell && typeof cell === 'object') ? cell.label : String(cell ?? '');
                                    const colSpan = (cell && typeof cell === 'object' && Number.isFinite(Number(cell.colSpan))) ? Number(cell.colSpan) : 1;
                                    const rowSpan = (cell && typeof cell === 'object' && Number.isFinite(Number(cell.rowSpan))) ? Number(cell.rowSpan) : 1;
                                    return <th key={cellIndex} colSpan={colSpan} rowSpan={rowSpan} style={headerStyle}>{label}</th>;
                                })}
                            </tr>
                        )) : (
                            <tr>
                                {headers.map((header, headerIndex) => <th key={headerIndex} style={headerStyle}>{header}</th>)}
                            </tr>
                        )}
                    </thead>
                    <tbody>
                        {rows.map((row, rowIndex) => (
                            <tr key={rowIndex}>
                                {(Array.isArray(row) ? row : []).map((cell, cellIndex) => {
                                    const cellId = cell?.cell_id || `t${tableIndex}_r${rowIndex}_c${cellIndex}`;
                                    const editable = !readOnly && Boolean(cell?.editable);
                                    const headerLabel = String(headers[cellIndex] || '').toLowerCase();
                                    const textAlign = /(amount|salary|wage|gross|paye|pension|medical|uif|bonus|commission|overtime|bank)/.test(headerLabel) ? 'right' : 'center';
                                    const value = editable ? (cells[String(cellId)] ?? '') : ((Object.prototype.hasOwnProperty.call(cells, String(cellId)) ? cells[String(cellId)] : cell?.value) || '');
                                    return (
                                        <td key={cellIndex} style={bodyStyle}>
                                            {editable ? (
                                                <input
                                                    value={value}
                                                    onChange={(e) => setAnswer(idx, {
                                                        ...ans,
                                                        cells: {
                                                            ...cells,
                                                            [String(cellId)]: e.target.value,
                                                        },
                                                    })}
                                                    style={{ width: '100%', padding: '6px', border: 'none', outline: 'none', boxSizing: 'border-box', textAlign, fontFamily: textAlign === 'right' ? 'ui-monospace, monospace' : 'inherit' }}
                                                />
                                            ) : (
                                                <div style={{ width: '100%', padding: '6px', boxSizing: 'border-box', textAlign, fontFamily: textAlign === 'right' ? 'ui-monospace, monospace' : 'inherit', color: /month/.test(headerLabel) ? '#6b7280' : '#111827' }}>
                                                    {value}
                                                </div>
                                            )}
                                        </td>
                                    );
                                })}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    };

    const renderPromptTables = (q, idx) => {
        const promptTables = Array.isArray(q?.prompt_journals)
            ? q.prompt_journals
            : (q?.prompt_journal ? [q.prompt_journal] : []);
        if (!promptTables.length) return null;
        return (
            <div className="space-y-4">
                {promptTables.map((journal, promptIndex) => (
                    <div key={`prompt-${promptIndex}`}>
                        <div className="mt-4 mb-2 text-sm font-semibold text-slate-700">{journal?.heading || 'Source information'}</div>
                        {renderOneJournalTable(q, idx, journal, -100 - promptIndex, { readOnly: true })}
                    </div>
                ))}
            </div>
        );
    };

    const renderJournalTables = (q, idx, { readOnly = false, cellValues = null } = {}) => {
        const journals = Array.isArray(q?.journals)
            ? q.journals
            : (q?.journal ? [q.journal] : []);
        return (
            <div className="space-y-4">
                {journals.map((journal, journalIndex) => (
                    <div key={`journal-${journalIndex}`}>
                        <div className="mt-4 mb-2 text-sm font-semibold text-slate-800">{journal?.heading || 'Accounting table'}</div>
                        {renderOneJournalTable(q, idx, journal, journalIndex, { readOnly, cellValues })}
                    </div>
                ))}
            </div>
        );
    };

    const renderReviewQuestion = (reviewQuestion, idx) => {
        const reviewFeedback = Array.isArray(g10AcctSWPracticeFeedback) ? g10AcctSWPracticeFeedback[idx] : null;
        const reviewAnswer = Array.isArray(g10AcctSWPracticeAnswers) ? g10AcctSWPracticeAnswers[idx] : null;
        const memoOpen = activeReviewMemoIndex === idx;
        const reviewNonTabularHintItems = reviewQuestion && reviewQuestion?.question_type !== 'table_wordbank' && reviewQuestion?.question_type !== 'journal' && reviewQuestion?.question_type !== 'ledger' ? buildNonTabularHintItems(reviewQuestion) : [];

        return (
            <div key={reviewQuestion?.id || idx} className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm space-y-4">
                <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-3">
                    <div>
                        <div className="text-sm font-semibold text-slate-800">Question {idx + 1}</div>
                        {reviewFeedback && (
                            <div className={`mt-2 inline-flex px-3 py-1 rounded-full text-xs font-semibold ${reviewFeedback.kind === 'success' ? 'bg-emerald-50 text-emerald-700' : reviewFeedback.kind === 'error' ? 'bg-red-50 text-red-700' : 'bg-slate-100 text-slate-700'}`}>
                                {reviewFeedback.message}
                            </div>
                        )}
                    </div>
                    <button
                        type="button"
                        onClick={() => setActiveReviewMemoIndex((prev) => prev === idx ? null : idx)}
                        className={`px-4 py-2 rounded-xl font-semibold transition-colors border ${memoOpen ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'}`}
                    >
                        {memoOpen ? 'Hide Memo' : 'Show Memo'}
                    </button>
                </div>

                <div className="text-lg font-medium text-slate-800 whitespace-pre-wrap">{reviewQuestion?.prompt}</div>

                {reviewQuestion?.question_type === 'mcq' && (
                    <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-700">
                        <div><span className="font-semibold text-slate-900">Your answer:</span> {reviewAnswer === null || reviewAnswer === undefined || String(reviewAnswer).trim() === '' ? 'No option selected' : (reviewQuestion?.options?.[Number(reviewAnswer)] || String(reviewAnswer))}</div>
                    </div>
                )}

                {reviewQuestion?.question_type === 'calc' && (
                    <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-700">
                        <div><span className="font-semibold text-slate-900">Your answer:</span> {typeof reviewAnswer === 'string' && reviewAnswer.trim() ? `${reviewQuestion?.unit || 'R'}${reviewAnswer}` : 'No answer entered'}</div>
                    </div>
                )}

                {reviewQuestion?.question_type === 'typed' && (
                    <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-700 whitespace-pre-wrap min-h-[110px]">
                        {typeof reviewAnswer === 'string' && reviewAnswer.trim() ? reviewAnswer : 'No written answer entered.'}
                    </div>
                )}

                {reviewQuestion?.question_type === 'table_wordbank' && renderWordbankTable(reviewQuestion, idx, { readOnly: true })}
                {(reviewQuestion?.question_type === 'journal' || reviewQuestion?.question_type === 'ledger') && renderPromptTables(reviewQuestion, idx)}
                {(reviewQuestion?.question_type === 'journal' || reviewQuestion?.question_type === 'ledger') && renderJournalTables(reviewQuestion, idx, { readOnly: true, cellValues: (reviewAnswer && typeof reviewAnswer === 'object' ? reviewAnswer.cells : {}) })}

                {memoOpen && reviewQuestion?.question_type === 'mcq' && (
                    <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                        <div className="font-semibold text-slate-900">Compare / Memo</div>
                        <div className="mt-2">Correct answer: {reviewQuestion?.options?.[reviewQuestion?.correct_index] || ''}</div>
                    </div>
                )}

                {memoOpen && reviewQuestion?.question_type !== 'table_wordbank' && reviewQuestion?.question_type !== 'mcq' && reviewQuestion?.question_type !== 'journal' && reviewQuestion?.question_type !== 'ledger' && reviewNonTabularHintItems.length > 0 && (
                    <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                        <div className="font-semibold text-slate-900">Compare / Memo</div>
                        <div className="mt-3 space-y-3">
                            {reviewNonTabularHintItems.map((item) => (
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

                {memoOpen && (reviewQuestion?.question_type === 'journal' || reviewQuestion?.question_type === 'ledger') && (
                    <div className="space-y-3">
                        <div className="text-sm font-semibold text-slate-900">Compare / Memo</div>
                        {renderJournalTables(reviewQuestion, idx, { readOnly: true, cellValues: getCorrectMap(reviewQuestion) })}
                    </div>
                )}
            </div>
        );
    };

    const q = questions[currentIndex];
    const ans = g10AcctSWPracticeAnswers?.[currentIndex];
    const feedback = g10AcctSWPracticeFeedback?.[currentIndex];
    const nonTabularHintItems = q ? buildNonTabularHintItems(q) : [];
    const wordbankMemoRows = q?.question_type === 'table_wordbank' ? buildWordbankMemoRows(q) : [];
    const typedHintSections = q?.question_type === 'typed' ? buildTypedHintSections(q) : [];
    const calcHintText = String(q?.working_formula || '').trim();

    const handleAnswerKeyDown = (event) => {
        if (!marking.isPracticeMode || !q || !shouldHandleEnterCheck(event)) return;
        event.preventDefault();
        checkOne(q, currentIndex);
    };

    useEffect(() => {
        setShowMemo(false);
        setShowHint(false);
    }, [currentIndex, q?.id]);

    return (
        <>
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-slate-800">Practice Mode</h3>
            </div>

            {marking.markingError && <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">{marking.markingError}</div>}
            {g10AcctSWPracticeLoading && <div className="text-sm text-slate-500">Loading...</div>}
            {g10AcctSWPracticeError && <div className="text-sm text-red-700 break-words">{g10AcctSWPracticeError}</div>}
            {!g10AcctSWPracticeLoading && questions.length === 0 && <div className="text-sm text-slate-500">Click "Generate Question" to start.</div>}

            {q && !reviewMode && (
                <div className="space-y-4" onKeyDown={handleAnswerKeyDown}>
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
                                    {(q.options || []).map((opt, oIdx) => (
                                        <MCQOption key={oIdx} selected={String(ans) === String(oIdx)} onClick={() => setAnswer(currentIndex, String(oIdx))} label={opt} />
                                    ))}
                                </div>
                            )}

                            {q.question_type === 'calc' && (
                                <div className="flex items-center gap-2">
                                    {q.unit && <span className="text-slate-500 font-medium">{q.unit}</span>}
                                    <input type="number" step="0.01" className="w-full max-w-xs p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-400" placeholder="0.00" value={typeof ans === 'string' ? ans : ''} onChange={(e) => setAnswer(currentIndex, e.target.value)} />
                                </div>
                            )}

                            {q.question_type === 'typed' && (
                                <div>
                                    <textarea value={typeof ans === 'string' ? ans : ''} onChange={(e) => setAnswer(currentIndex, e.target.value)} placeholder="Write your answer..." className="w-full min-h-[110px] p-3 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-slate-300" title="Press Enter to check, or Shift+Enter for a new line." />
                                </div>
                            )}

                            {q.question_type === 'table_wordbank' && renderWordbankTable(q, currentIndex)}

                            {(q.question_type === 'journal' || q.question_type === 'ledger') && renderPromptTables(q, currentIndex)}

                            {(q.question_type === 'journal' || q.question_type === 'ledger') && renderJournalTables(q, currentIndex)}
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
                                    <button
                                        onClick={() => {
                                            setFeedbackAt(currentIndex, null);
                                            setShowMemo(false);
                                            setShowHint(false);
                                        }}
                                        className="px-6 py-2 bg-white border border-slate-200 text-slate-600 rounded-xl font-semibold hover:bg-slate-50 transition-colors"
                                    >
                                        Clear feedback
                                    </button>
                                    <button
                                        onClick={() => setShowHint(!showHint)}
                                        className="px-6 py-2 bg-white border border-slate-200 text-slate-700 rounded-xl font-semibold hover:bg-slate-50 transition-colors"
                                    >
                                        {showHint ? 'Hide Hint' : 'Hint'}
                                    </button>
                                    {currentIndex === questions.length - 1 && (
                                        <button onClick={handleFinishAndReview} className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors">
                                            Finish & Review
                                        </button>
                                    )}
                                </>
                            ) : (
                                !marking.isMarkingSubmitted && (
                                    <button onClick={() => marking.submitAssessment(questions)} disabled={marking.isSubmitting} className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors disabled:opacity-50">{marking.isSubmitting ? 'Submitting...' : 'Submit Assessment'}</button>
                                )
                            )}
                        </div>

                        {showHint && q?.question_type === 'typed' && typedHintSections.length > 0 && (
                            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                                <div className="font-semibold text-yellow-900">Typed-answer hint</div>
                                <div className="mt-3 space-y-3 text-sm text-yellow-900">
                                    {typedHintSections.map((section, idx) => (
                                        <div key={`${section.title}-${idx}`} className="space-y-1">
                                            <div className="font-semibold text-yellow-950">{section.title}</div>
                                            <div className="whitespace-pre-line">{section.text}</div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {showHint && q?.question_type === 'calc' && calcHintText && (
                            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                                <div className="font-semibold text-yellow-900">Calculation hint</div>
                                <div className="mt-2 text-sm text-yellow-900 whitespace-pre-line">{calcHintText}</div>
                            </div>
                        )}

                        {showHint && q?.question_type === 'table_wordbank' && Array.isArray(q?.guidelines) && q.guidelines.length > 0 && (
                            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                                <div className="font-semibold text-yellow-900">Word-bank hint</div>
                                <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                    {q.guidelines.map((item, idx) => (
                                        <li key={idx}>{item}</li>
                                    ))}
                                </ul>
                            </div>
                        )}

                        {showHint && (q?.question_type === 'journal' || q?.question_type === 'ledger') && Array.isArray(q?.guidelines) && q.guidelines.length > 0 && (
                            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                                <div className="font-semibold text-yellow-900">Table hint</div>
                                <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                    {q.guidelines.map((item, idx) => (
                                        <li key={idx}>{item}</li>
                                    ))}
                                </ul>
                            </div>
                        )}

                        {feedback && marking.isPracticeMode && (
                            <div className={`mt-3 p-3 rounded-xl text-sm border ${feedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : feedback.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                                {feedback.message}
                            </div>
                        )}

                        {q?.question_type === 'typed' && marking.isPracticeMode && (
                            <div className="mt-4 p-3 rounded-xl text-sm border bg-slate-50 border-slate-200 text-slate-600">
                                ⭐ AI-graded feedback available in Pro subscription
                            </div>
                        )}

                        {showMemo && q?.question_type === 'typed' && nonTabularHintItems.length > 0 && (
                            <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                                <div className="font-semibold text-slate-900">Sample answer</div>
                                <div className="mt-3 space-y-3">
                                    {nonTabularHintItems.map((item, itemIdx) => (
                                        <div key={`${item.label}-${itemIdx}`} className="space-y-1">
                                            <div className="font-semibold text-slate-900">{item.label}</div>
                                            <div className="whitespace-pre-line">{item.value}</div>
                                        </div>
                                    ))}
                                </div>
                                {Array.isArray(q?.guidelines) && q.guidelines.length > 0 && (
                                    <div className="mt-4">
                                        <div className="font-semibold text-slate-900 mb-1">Guidelines</div>
                                        <ul className="list-disc pl-5 space-y-1">
                                            {q.guidelines.map((g, gi) => <li key={gi}>{g}</li>)}
                                        </ul>
                                    </div>
                                )}
                            </div>
                        )}

                        {showMemo && q?.question_type === 'calc' && nonTabularHintItems.length > 0 && (
                            <div className="mt-4 p-4 bg-indigo-50 border border-indigo-200 rounded-xl text-sm text-indigo-900">
                                <div className="font-semibold text-indigo-950">Compare / Memo</div>
                                <div className="mt-3 space-y-3">
                                    {nonTabularHintItems.map((item, itemIdx) => (
                                        <div key={`${item.label}-${itemIdx}`} className="space-y-1">
                                            <div className="font-semibold text-indigo-950">{item.label}</div>
                                            <div className="whitespace-pre-line">{item.value}</div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {showMemo && q?.question_type === 'table_wordbank' && wordbankMemoRows.length > 0 && (
                            <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                                <div className="font-semibold text-slate-900">Compare / Memo</div>
                                <div className="mt-3 space-y-3">
                                    {wordbankMemoRows.map((item, itemIdx) => (
                                        <div key={`${item.rowLabel}-${itemIdx}`} className="space-y-1">
                                            <div className="font-semibold text-slate-900">Row {item.rowLabel}</div>
                                            <div className="text-slate-600 whitespace-pre-line">{item.definition}</div>
                                            <div className="whitespace-pre-line">{item.answer}</div>
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
                                    if (typeof setCurrentIndex === 'function') setCurrentIndex(0);
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

export default Grade10AccountingSalariesWagesPractice;

