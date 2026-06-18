import React, { useState, useEffect, useRef } from 'react';
import MCQOption from '../../../shared/MCQOption';
import { useGrade10AccountingMarking } from '../useGrade10AccountingMarking';

const normalizeText = (v) => v == null ? '' : String(v).trim().replace(/\s+/g, ' ').toLowerCase();

const FILL_IN_TABLE_TYPES = new Set(['journal', 'ledger', 'final_account_table', 'trial_balance_table', 'asset_register_table', 'adjustment_analysis_table']);

const isFillInTableQuestionType = (questionTypeRaw) => FILL_IN_TABLE_TYPES.has(String(questionTypeRaw || '').trim().toLowerCase());

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

const clampHintPosition = (x, y, width = 320, height = 240) => {
    if (typeof window === 'undefined') return { x, y };
    const margin = 12;
    const maxX = Math.max(margin, window.innerWidth - width - margin);
    const maxY = Math.max(margin, window.innerHeight - height - margin);
    return {
        x: Math.min(Math.max(margin, Number(x) || margin), maxX),
        y: Math.min(Math.max(margin, Number(y) || margin), maxY),
    };
};

const buildHintSections = (teachingHint, fallbackText) => {
    const sections = [];
    if (teachingHint && typeof teachingHint === 'object') {
        const labels = [
            ['role_in_requirement', 'What this cell is asking'],
            ['evidence_from_question', 'Where to look in the question'],
            ['rule_or_principle', 'Rule / principle'],
            ['method_or_formula', 'Method / formula'],
            ['record_link', 'Connection to other records'],
            ['how_to_derive', 'How to derive it'],
            ['transfer_tip', 'Use this in similar questions'],
        ];
        labels.forEach(([key, title]) => {
            const text = String(teachingHint[key] || '').trim();
            if (text) sections.push({ title, text });
        });
    }
    if (!sections.length) {
        const text = String(fallbackText || '').trim();
        if (text) sections.push({ title: 'Hint', text });
    }
    return sections;
};

const getWordBank = (question) => Array.isArray(question?.word_bank) ? question.word_bank : [];
const getCorrectMap = (question) => (question?.correct_map && typeof question?.correct_map === 'object') ? question.correct_map : {};

const getStructuredTables = (question) => {
    if (!question || question?.question_type === 'table_wordbank') return [];
    if (Array.isArray(question?.tables)) return question.tables.filter(Boolean);
    if (question?.table && typeof question.table === 'object') return [question.table];
    return [];
};

const getPromptTables = (question) => {
    if (Array.isArray(question?.prompt_tables)) return question.prompt_tables.filter(Boolean);
    if (Array.isArray(question?.prompt_journals)) return question.prompt_journals.filter(Boolean);
    if (question?.prompt_table && typeof question.prompt_table === 'object') return [question.prompt_table];
    if (question?.prompt_journal && typeof question.prompt_journal === 'object') return [question.prompt_journal];
    return [];
};

const buildEmptyTableAnswer = (question) => {
    const cells = {};
    getStructuredTables(question).forEach((table) => {
        const rows = Array.isArray(table?.rows) ? table.rows : [];
        rows.forEach((row) => {
            (Array.isArray(row) ? row : []).forEach((cell) => {
                if (!cell?.cell_id) return;
                cells[String(cell.cell_id)] = cell?.value || '';
            });
        });
    });
    return { cells, extra_rows_by_table: {} };
};

const buildFillInMemoTables = (question) => {
    const correctMap = getCorrectMap(question);
    return getStructuredTables(question).map((table) => ({
        ...table,
        rows: (Array.isArray(table?.rows) ? table.rows : []).map((row) =>
            (Array.isArray(row) ? row : []).map((cell) => {
                if (!cell || typeof cell !== 'object') return { value: String(cell ?? '') };
                const nextCell = { ...cell, editable: false };
                if (nextCell.cell_id && Object.prototype.hasOwnProperty.call(correctMap, String(nextCell.cell_id))) {
                    nextCell.value = correctMap[String(nextCell.cell_id)];
                }
                return nextCell;
            })
        ),
    }));
};

const buildNonTabularMemoItems = (question) => {
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

const getUsedTokenIds = (ans) => {
    const selections = ans?.selections && typeof ans.selections === 'object' ? ans.selections : {};
    const used = new Set();
    Object.values(selections).forEach((row) => {
        if (!row) return;
        const value = row['2'];
        if (value) used.add(String(value));
    });
    return used;
};

const Grade10AccountingFinalAccountsPractice = ({
    onBack,
    g10AcctFAVisualAidsOpen, setG10AcctFAVisualAidsOpen,
    g10AcctFAPracticeDifficulty, setG10AcctFAPracticeDifficulty,
    fetchGrade10AcctFAPractice,
    g10AcctFAPracticeLoading, g10AcctFAPracticeError, g10AcctFAPracticeQuestions,
    g10AcctFAPracticeAnswers, setG10AcctFAPracticeAnswers,
    g10AcctFAPracticeFeedback, setG10AcctFAPracticeFeedback,
    renderGrade10AcctFAVisualAids, hideConfig,
    currentIndex: externalCurrentIndex,
    setCurrentIndex: externalSetCurrentIndex,
}) => {
    const questions = Array.isArray(g10AcctFAPracticeQuestions) ? g10AcctFAPracticeQuestions : [];
    const [internalCurrentIndex, setInternalCurrentIndex] = useState(0);
    const [activeCellHint, setActiveCellHint] = useState(null);
    const [showMemo, setShowMemo] = useState(false);
    const [showHint, setShowHint] = useState(false);
    const [showCheckHighlights, setShowCheckHighlights] = useState(false);
    const [reviewMode, setReviewMode] = useState(false);
    const [activeReviewMemoIndex, setActiveReviewMemoIndex] = useState(null);
    const cellHintPopupRef = useRef(null);
    const marking = useGrade10AccountingMarking();
    const currentIndex = typeof externalCurrentIndex === 'number' ? externalCurrentIndex : internalCurrentIndex;
    const setCurrentIndex = typeof externalSetCurrentIndex === 'function' ? externalSetCurrentIndex : setInternalCurrentIndex;

    useEffect(() => { if (questions.length > 0) marking.setMarkingMode('practice'); }, [questions, marking]);

    useEffect(() => {
        setShowMemo(false);
        setShowHint(false);
        setShowCheckHighlights(false);
        setActiveCellHint(null);
    }, [currentIndex, questions]);

    useEffect(() => {
        setReviewMode(false);
        setActiveReviewMemoIndex(null);
        if (typeof setCurrentIndex === 'function') setCurrentIndex(0);
    }, [questions, setCurrentIndex]);

    useEffect(() => {
        if (!activeCellHint || !cellHintPopupRef.current) return;
        const width = cellHintPopupRef.current.offsetWidth || 320;
        const height = cellHintPopupRef.current.offsetHeight || 240;
        const next = clampHintPosition(activeCellHint.x, activeCellHint.y, width, height);
        if (next.x !== activeCellHint.x || next.y !== activeCellHint.y) {
            setActiveCellHint((prev) => (prev ? { ...prev, x: next.x, y: next.y } : prev));
        }
    }, [activeCellHint]);

    const handleNext = () => { if (!reviewMode && typeof setCurrentIndex === 'function' && currentIndex < questions.length - 1) setCurrentIndex(currentIndex + 1); };
    const handlePrev = () => { if (!reviewMode && typeof setCurrentIndex === 'function' && currentIndex > 0) setCurrentIndex(currentIndex - 1); };

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g10AcctFAPracticeAnswers) ? [...g10AcctFAPracticeAnswers] : [];
        answers[idx] = value;
        setG10AcctFAPracticeAnswers(answers);
        if (questions[idx]) marking.registerAnswer(questions[idx].id, value);
        const fb = Array.isArray(g10AcctFAPracticeFeedback) ? [...g10AcctFAPracticeFeedback] : [];
        fb[idx] = null;
        setG10AcctFAPracticeFeedback(fb);
        if (idx === currentIndex) {
            setShowMemo(false);
            setShowCheckHighlights(false);
            setActiveCellHint(null);
        }
    };

    useEffect(() => {
        if (!questions.length) return;
        if (!Array.isArray(g10AcctFAPracticeAnswers) || g10AcctFAPracticeAnswers.length !== questions.length)
            setG10AcctFAPracticeAnswers(questions.map((question) => {
                if (isFillInTableQuestionType(question?.question_type)) return buildEmptyTableAnswer(question);
                if (question.question_type === 'table_wordbank') return buildEmptyWordbankAnswer(question);
                return '';
            }));
        if (!Array.isArray(g10AcctFAPracticeFeedback) || g10AcctFAPracticeFeedback.length !== questions.length)
            setG10AcctFAPracticeFeedback(questions.map(() => null));
    }, [questions.length]);

    const setFeedbackAt = (idx, value) => {
        const next = Array.isArray(g10AcctFAPracticeFeedback) ? g10AcctFAPracticeFeedback.slice() : [];
        next[idx] = value;
        setG10AcctFAPracticeFeedback(next);
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
                message: ok ? '0 of 1 responses incorrect.' : `1 of 1 responses incorrect. Correct answer: R${expected.toFixed(2)}`,
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
        if (isFillInTableQuestionType(q.question_type)) {
            const correctMap = getCorrectMap(q);
            const answerState = (userValue && typeof userValue === 'object') ? userValue : buildEmptyTableAnswer(q);
            const cells = answerState?.cells && typeof answerState.cells === 'object' ? answerState.cells : {};
            const keys = Object.keys(correctMap);
            const cellResults = {};
            let hit = 0;
            keys.forEach((key) => {
                const expected = correctMap[key];
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
        const ans = Array.isArray(g10AcctFAPracticeAnswers) ? g10AcctFAPracticeAnswers[idx] : null;
        const result = evaluateQuestion(q, ans);
        if (idx === currentIndex) setShowCheckHighlights(isFillInTableQuestionType(q.question_type));
        setFeedbackAt(idx, result);
    };

    const handleFinishAndReview = () => {
        const answers = Array.isArray(g10AcctFAPracticeAnswers) ? g10AcctFAPracticeAnswers : [];
        const feedback = questions.map((question, idx) => evaluateQuestion(question, answers[idx]));
        setG10AcctFAPracticeFeedback(feedback);
        setActiveReviewMemoIndex(null);
        setShowMemo(false);
        setShowHint(false);
        setShowCheckHighlights(false);
        setActiveCellHint(null);
        setReviewMode(true);
    };

    const renderCellHintPopupContent = (hint) => {
        const sections = Array.isArray(hint?.sections) ? hint.sections : [];
        return (
            <div className="p-3 max-h-[60vh] overflow-y-auto leading-snug space-y-3">
                {sections.map((section, idx) => (
                    <div key={`${section.title}-${idx}`} className="space-y-1">
                        <div className="font-semibold text-yellow-950">{section.title}</div>
                        <div className="text-yellow-900 whitespace-pre-line">{section.text}</div>
                    </div>
                ))}
            </div>
        );
    };

    const renderOneStructuredTable = (q, idx, table, tableIndex, { readOnly = false, cellValues = null } = {}) => {
        if (!table) return null;
        const headers = Array.isArray(table?.headers) ? table.headers : [];
        const headerRows = Array.isArray(table?.header_rows) ? table.header_rows : [];
        const rows = Array.isArray(table?.rows) ? table.rows : [];
        const ans = (g10AcctFAPracticeAnswers?.[idx] && typeof g10AcctFAPracticeAnswers[idx] === 'object') ? g10AcctFAPracticeAnswers[idx] : buildEmptyTableAnswer(q);
        const cells = cellValues && typeof cellValues === 'object'
            ? cellValues
            : (ans?.cells && typeof ans.cells === 'object' ? ans.cells : {});
        const correctMap = getCorrectMap(q);
        const cellHints = (q?.cell_hints && typeof q.cell_hints === 'object') ? q.cell_hints : {};
        const cellTeachingMap = (q?.cell_teaching_map && typeof q.cell_teaching_map === 'object') ? q.cell_teaching_map : {};
        const workingMap = (q?.working_map && typeof q.working_map === 'object') ? q.working_map : {};

        const tableStyle = { width: '100%', minWidth: `${Math.max(headers.length * 112, 720)}px`, borderCollapse: 'collapse', tableLayout: 'fixed' };
        const headerStyle = { border: '1px solid #000', padding: '6px', background: '#e5e7eb', fontWeight: 600, textAlign: 'center', verticalAlign: 'middle' };
        const bodyStyle = { border: '1px solid #000', padding: 0, verticalAlign: 'top' };

        const openCellHint = (cellId, label, text, sections, triggerEl) => {
            const rect = triggerEl?.getBoundingClientRect?.();
            const anchorX = rect ? rect.left : 24;
            const anchorY = rect ? rect.bottom + 10 : 24;
            const next = clampHintPosition(anchorX, anchorY, 320, 240);
            setActiveCellHint((prev) => {
                if (prev?.cellId === cellId && prev?.questionIndex === idx) return null;
                return {
                    questionIndex: idx,
                    cellId,
                    label,
                    text,
                    sections,
                    x: next.x,
                    y: next.y,
                };
            });
        };

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
                                    const isNumeric = /(amount|debit|credit|balance|profit|loss|capital|drawings|sales|stock|cost|income|expense)/.test(headerLabel);
                                    const rawValue = (() => {
                                        if (editable) return cells[String(cellId)] ?? '';
                                        if (Object.prototype.hasOwnProperty.call(cells, String(cellId))) return cells[String(cellId)] ?? '';
                                        return cell?.value || '';
                                    })();
                                    const expected = correctMap[String(cellId)];
                                    const exactCellHint = String(cellHints[String(cellId)] || '').trim();
                                    const rowHint = String(cellHints[`t${tableIndex}_r${rowIndex}_c0`] || '').trim();
                                    const derivationHint = String((q?.derivation_map || {})?.[String(cellId)] || '').trim();
                                    const workingHint = String(workingMap[String(cellId)] || '').trim();
                                    const hintParts = [];
                                    if (exactCellHint) hintParts.push(exactCellHint);
                                    else if (rowHint) hintParts.push(rowHint);
                                    if (derivationHint) hintParts.push(derivationHint);
                                    if (workingHint) hintParts.push(workingHint);
                                    const cellHintText = hintParts.join('\n\n').trim();
                                    const cellHintSections = buildHintSections(cellTeachingMap[String(cellId)], cellHintText);
                                    const showCellHintButton = showHint && editable && cellHintSections.length > 0;
                                    const cellLabel = String(headers[cellIndex] || cellId);
                                    let displayValue = rawValue;
                                    let cellBorder = 'none';
                                    let cellBg = '';
                                    const memoTooltip = derivationHint || (expected !== undefined ? `Expected: ${expected}` : '');
                                    if (!readOnly && idx === currentIndex && showCheckHighlights && editable && expected !== undefined) {
                                        const hit = normalizeText(rawValue) === normalizeText(expected) || numbersMatch(rawValue, expected);
                                        if (showMemo) {
                                            displayValue = hit ? rawValue : expected;
                                            cellBorder = '2px solid #10b981';
                                            cellBg = 'rgba(16, 185, 129, 0.14)';
                                        } else if (hit && String(rawValue).trim() !== '') {
                                            cellBorder = '2px solid #10b981';
                                            cellBg = '#ecfdf5';
                                        } else {
                                            cellBorder = '2px solid #ef4444';
                                            cellBg = '#fef2f2';
                                        }
                                    }
                                    return (
                                        <td key={cellIndex} style={bodyStyle}>
                                            {editable ? (
                                                <div className="relative h-full w-full flex items-stretch group">
                                                    <input
                                                        value={displayValue}
                                                        onChange={(e) => setAnswer(idx, {
                                                            ...ans,
                                                            cells: {
                                                                ...((ans?.cells && typeof ans.cells === 'object') ? ans.cells : {}),
                                                                [String(cellId)]: e.target.value,
                                                            },
                                                        })}
                                                        readOnly={showMemo && idx === currentIndex}
                                                        style={{ width: '100%', padding: '6px', border: cellBorder, outline: 'none', boxSizing: 'border-box', textAlign: isNumeric ? 'right' : 'center', fontFamily: isNumeric ? 'ui-monospace, monospace' : 'inherit', backgroundColor: cellBg }}
                                                    />
                                                    {showCellHintButton && (
                                                        <button
                                                            type="button"
                                                            onClick={(e) => {
                                                                e.preventDefault();
                                                                e.stopPropagation();
                                                                openCellHint(String(cellId), cellLabel, cellHintText, cellHintSections, e.currentTarget);
                                                            }}
                                                            className="absolute top-1 right-1 inline-flex items-center justify-center w-5 h-5 rounded-full text-[11px] font-bold border border-yellow-300 text-yellow-800 bg-yellow-50 hover:bg-yellow-100"
                                                            aria-label={`Hint: ${cellLabel}`}
                                                        >
                                                            i
                                                        </button>
                                                    )}
                                                    {showMemo && idx === currentIndex && memoTooltip && String(rawValue).trim() !== String(displayValue).trim() && (
                                                        <div className="absolute opacity-0 pointer-events-none group-hover:opacity-100 transition-opacity z-20 bottom-full mb-1 left-1/2 -translate-x-1/2 w-48 p-2 bg-indigo-900 text-white text-xs rounded-lg shadow-xl text-center">
                                                            {memoTooltip}
                                                            <div className="absolute top-full left-1/2 -translate-x-1/2 w-2 h-2 bg-indigo-900 rotate-45 -mt-1"></div>
                                                        </div>
                                                    )}
                                                </div>
                                            ) : (
                                                <div style={{ width: '100%', padding: '6px', boxSizing: 'border-box', textAlign: isNumeric ? 'right' : 'center', fontFamily: isNumeric ? 'ui-monospace, monospace' : 'inherit', color: /(period|month)/.test(headerLabel) ? '#6b7280' : '#111827' }}>
                                                    {displayValue}
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
        const promptTables = getPromptTables(q);
        if (!promptTables.length) return null;
        return (
            <div className="space-y-4">
                {promptTables.map((table, promptIndex) => (
                    <div key={`prompt-${promptIndex}`}>
                        <div className="mt-4 mb-2 text-sm font-semibold text-slate-700">{table?.heading || 'Source information'}</div>
                        {renderOneStructuredTable(q, idx, table, -100 - promptIndex, { readOnly: true })}
                    </div>
                ))}
            </div>
        );
    };

    const renderStructuredTables = (q, idx, { readOnly = false, cellValues = null, tablesOverride = null } = {}) => {
        const tables = Array.isArray(tablesOverride) ? tablesOverride : getStructuredTables(q);
        return (
            <div className="space-y-4">
                {tables.map((table, tableIndex) => (
                    <div key={`table-${tableIndex}`}>
                        <div className="mt-4 mb-2 text-sm font-semibold text-slate-800">{table?.heading || 'Accounting table'}</div>
                        {renderOneStructuredTable(q, idx, table, tableIndex, { readOnly, cellValues })}
                    </div>
                ))}
            </div>
        );
    };

    const renderWordbankTable = (q, idx, { readOnly = false, useCorrectAnswers = false } = {}) => {
        const answerState = (g10AcctFAPracticeAnswers?.[idx] && typeof g10AcctFAPracticeAnswers[idx] === 'object')
            ? g10AcctFAPracticeAnswers[idx]
            : buildEmptyWordbankAnswer(q);
        const wordBank = getWordBank(q);
        const used = getUsedTokenIds(answerState);
        const tokenLabelById = {};
        wordBank.forEach((token) => { tokenLabelById[String(token.id)] = token.label; });

        const setActiveTokenId = (tokenId) => setAnswer(idx, { ...(answerState || {}), activeTokenId: tokenId });
        const clearCell = (rowIndex) => {
            setAnswer(idx, {
                ...(answerState || {}),
                selections: {
                    ...(answerState?.selections || {}),
                    [String(rowIndex)]: {
                        ...((answerState?.selections || {})[String(rowIndex)] || {}),
                        '2': null,
                    },
                },
            });
        };
        const placeActive = (rowIndex) => {
            const tokenId = answerState?.activeTokenId;
            if (!tokenId || used.has(String(tokenId))) return;
            setAnswer(idx, {
                ...(answerState || {}),
                selections: {
                    ...(answerState?.selections || {}),
                    [String(rowIndex)]: {
                        ...((answerState?.selections || {})[String(rowIndex)] || {}),
                        '2': String(tokenId),
                    },
                },
                activeTokenId: null,
            });
        };

        const rows = Array.isArray(q?.table?.rows) ? q.table.rows : [];
        const headers = Array.isArray(q?.table?.headers) ? q.table.headers : [];
        const correctMap = getCorrectMap(q);

        return (
            <div className="mt-3">
                {!readOnly && (
                    <div className="mb-3">
                        <div className="text-sm font-semibold text-gray-900 mb-2">Word bank</div>
                        <div className="flex flex-wrap gap-2">
                            {wordBank.map((token) => {
                                const isUsed = used.has(String(token.id));
                                const isActive = String(answerState?.activeTokenId) === String(token.id);
                                return (
                                    <button key={token.id} type="button" disabled={isUsed} onClick={() => setActiveTokenId(String(token.id))}
                                        className={`px-3 py-1 rounded-full text-sm font-semibold border ${isUsed ? 'bg-gray-100 text-gray-400 border-gray-200' : isActive ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}>
                                        {token.label}
                                    </button>
                                );
                            })}
                        </div>
                    </div>
                )}
                <div className="overflow-x-auto">
                    <table className="min-w-full border border-gray-200 text-sm">
                        <thead className="bg-gray-50"><tr>{headers.map((header, headerIndex) => <th key={headerIndex} className="px-3 py-2 border-b border-gray-200 text-left font-semibold text-gray-900">{header}</th>)}</tr></thead>
                        <tbody>
                            {rows.map((row, rowIndex) => {
                                const selectedId = useCorrectAnswers
                                    ? correctMap?.[String(rowIndex)]?.['2']
                                    : answerState?.selections?.[String(rowIndex)]?.['2'];
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
        const reviewFeedback = Array.isArray(g10AcctFAPracticeFeedback) ? g10AcctFAPracticeFeedback[idx] : null;
        const reviewAnswer = Array.isArray(g10AcctFAPracticeAnswers) ? g10AcctFAPracticeAnswers[idx] : null;
        const memoOpen = activeReviewMemoIndex === idx;
        const reviewNonTabularMemoItems = reviewQuestion && reviewQuestion?.question_type !== 'table_wordbank' && !isFillInTableQuestionType(reviewQuestion?.question_type) ? buildNonTabularMemoItems(reviewQuestion) : [];
        const reviewWordbankMemoRows = reviewQuestion?.question_type === 'table_wordbank' ? buildWordbankMemoRows(reviewQuestion) : [];

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
                        <div><span className="font-semibold text-slate-900">Your answer:</span> {typeof reviewAnswer === 'string' && reviewAnswer.trim() ? `R${reviewAnswer}` : 'No answer entered'}</div>
                    </div>
                )}

                {reviewQuestion?.question_type === 'typed' && (
                    <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-700 whitespace-pre-wrap min-h-[110px]">
                        {typeof reviewAnswer === 'string' && reviewAnswer.trim() ? reviewAnswer : 'No written answer entered.'}
                    </div>
                )}

                {reviewQuestion?.question_type === 'table_wordbank' && renderWordbankTable(reviewQuestion, idx, { readOnly: true })}
                {isFillInTableQuestionType(reviewQuestion?.question_type) && renderPromptTables(reviewQuestion, idx)}
                {isFillInTableQuestionType(reviewQuestion?.question_type) && renderStructuredTables(reviewQuestion, idx, { readOnly: true, cellValues: (reviewAnswer && typeof reviewAnswer === 'object' ? reviewAnswer.cells : {}) })}

                {memoOpen && reviewQuestion?.question_type === 'mcq' && (
                    <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                        <div className="font-semibold text-slate-900">Compare / Memo</div>
                        <div className="mt-2">Correct answer: {reviewQuestion?.options?.[reviewQuestion?.correct_index] || ''}</div>
                    </div>
                )}

                {memoOpen && reviewQuestion?.question_type !== 'table_wordbank' && reviewQuestion?.question_type !== 'mcq' && reviewNonTabularMemoItems.length > 0 && (
                    <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                        <div className="font-semibold text-slate-900">Compare / Memo</div>
                        <div className="mt-3 space-y-3">
                            {reviewNonTabularMemoItems.map((item) => (
                                <div key={`${item.label}-${item.value}`}>
                                    <div className="font-semibold text-slate-900">{item.label}</div>
                                    <div className="whitespace-pre-wrap">{item.value}</div>
                                </div>
                            ))}
                        </div>
                    </div>
                )}

                {memoOpen && reviewQuestion?.question_type === 'table_wordbank' && reviewWordbankMemoRows.length > 0 && (
                    <div className="space-y-3">
                        <div className="text-sm font-semibold text-slate-900">Compare / Memo</div>
                        {renderWordbankTable(reviewQuestion, idx, { readOnly: true, useCorrectAnswers: true })}
                    </div>
                )}

                {memoOpen && isFillInTableQuestionType(reviewQuestion?.question_type) && (
                    <div className="space-y-3">
                        <div className="text-sm font-semibold text-slate-900">Compare / Memo</div>
                        {renderStructuredTables(reviewQuestion, idx, { readOnly: true, cellValues: getCorrectMap(reviewQuestion), tablesOverride: buildFillInMemoTables(reviewQuestion) })}
                    </div>
                )}
            </div>
        );
    };

    const q = questions[currentIndex];
    const ans = g10AcctFAPracticeAnswers?.[currentIndex];
    const feedback = g10AcctFAPracticeFeedback?.[currentIndex];
    const nonTabularMemoItems = q && q?.question_type !== 'table_wordbank' && !isFillInTableQuestionType(q?.question_type) ? buildNonTabularMemoItems(q) : [];
    const wordbankMemoRows = q?.question_type === 'table_wordbank' ? buildWordbankMemoRows(q) : [];
    const typedHintSections = q?.question_type === 'typed' ? buildTypedHintSections(q) : [];
    const calcHintText = String(q?.formula_hint || q?.working_formula || '').trim();

    return (
        <>
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-slate-800">Practice Mode</h3>
            </div>

            {marking.markingError && <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">{marking.markingError}</div>}
            {g10AcctFAPracticeLoading && <div className="text-sm text-slate-500">Loading...</div>}
            {g10AcctFAPracticeError && <div className="text-sm text-red-700 break-words">{g10AcctFAPracticeError}</div>}
            {!g10AcctFAPracticeLoading && questions.length === 0 && <div className="text-sm text-slate-500">Click "Generate Question" to start.</div>}

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
                            {isFillInTableQuestionType(q?.question_type) && renderPromptTables(q, currentIndex)}
                            {isFillInTableQuestionType(q?.question_type) && renderStructuredTables(q, currentIndex)}
                        </div>
                        <div className="mt-8 flex justify-end gap-3 pt-4 border-t border-slate-100">
                            <button onClick={() => checkOne(q, currentIndex)} className="px-6 py-2 bg-indigo-50 text-indigo-700 rounded-xl font-semibold hover:bg-indigo-100 transition-colors">{feedback ? 'Checked' : 'Check Answer'}</button>
                            <button onClick={() => setShowHint(!showHint)} className={`px-6 py-2 rounded-xl font-semibold transition-colors border ${showHint ? 'bg-amber-50 border-amber-200 text-amber-700' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'}`}>
                                {showHint ? 'Hide Hint' : 'Hint'}
                            </button>
                            {feedback && (['typed', 'calc', 'table_wordbank'].includes(String(q?.question_type || '')) || isFillInTableQuestionType(q?.question_type)) && (
                                <button onClick={() => setShowMemo(!showMemo)} className={`px-6 py-2 rounded-xl font-semibold transition-colors border ${showMemo ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'}`}>
                                    {showMemo ? 'Hide Memo' : 'Compare / Memo'}
                                </button>
                            )}
                            {(feedback || showHint || showMemo) && (
                                <button onClick={() => { setFeedbackAt(currentIndex, null); setShowHint(false); setShowMemo(false); setShowCheckHighlights(false); setActiveCellHint(null); }} className="px-6 py-2 bg-white border border-slate-200 text-slate-700 rounded-xl font-semibold hover:bg-slate-50 transition-colors">
                                    Clear feedback
                                </button>
                            )}
                            {currentIndex === questions.length - 1 && (
                                <button onClick={handleFinishAndReview} className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors">
                                    Finish & Review
                                </button>
                            )}
                        </div>
                        {feedback && marking.isPracticeMode && (
                            <div className={`mt-3 p-3 rounded-xl text-sm border ${feedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : feedback.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                                {feedback.message}
                            </div>
                        )}

                        {showHint && q?.question_type === 'typed' && typedHintSections.length > 0 && (
                            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                                <div className="font-semibold text-yellow-900">Typed-answer hint</div>
                                <div className="mt-2 space-y-3 text-sm text-yellow-900">
                                    {typedHintSections.map((section) => (
                                        <div key={section.title}>
                                            <div className="font-semibold">{section.title}</div>
                                            <div className="whitespace-pre-wrap">{section.text}</div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {showHint && q?.question_type === 'calc' && calcHintText && (
                            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl text-sm text-yellow-900">
                                <div className="font-semibold">Calculation hint</div>
                                <div className="mt-2 whitespace-pre-wrap">{calcHintText}</div>
                            </div>
                        )}

                        {showHint && q?.question_type === 'table_wordbank' && Array.isArray(q?.guidelines) && q.guidelines.length > 0 && (
                            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                                <div className="font-semibold text-yellow-900">Word-bank hint</div>
                                <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                    {q.guidelines.map((item, index) => <li key={index}>{item}</li>)}
                                </ul>
                            </div>
                        )}

                        {showHint && isFillInTableQuestionType(q?.question_type) && Array.isArray(q?.guidelines) && q.guidelines.length > 0 && (
                            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                                <div className="font-semibold text-yellow-900">Bookkeeping-table hint</div>
                                <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                    {q.guidelines.map((item, index) => <li key={index}>{item}</li>)}
                                </ul>
                            </div>
                        )}

                        {showHint && q?.question_type !== 'typed' && q?.question_type !== 'calc' && q?.question_type !== 'table_wordbank' && !isFillInTableQuestionType(q?.question_type) && (
                            <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 text-yellow-900 rounded-xl text-sm">
                                Use the visual aids panel for formulas, adjustment logic, and closing-transfer flow.
                            </div>
                        )}

                        {showMemo && q?.question_type !== 'table_wordbank' && nonTabularMemoItems.length > 0 && (
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
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {showMemo && isFillInTableQuestionType(q?.question_type) && (
                            <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                                Compare / Memo is shown directly in the table above. Correct values are displayed in-place with green highlighting.
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

            {activeCellHint && (
                <div
                    ref={cellHintPopupRef}
                    className="fixed z-[120] w-[320px] max-w-[calc(100vw-24px)] rounded-2xl border border-yellow-200 bg-yellow-50 shadow-2xl"
                    style={{ left: activeCellHint.x, top: activeCellHint.y }}
                >
                    <div className="flex items-center justify-between gap-2 px-3 py-2 border-b border-yellow-200 bg-yellow-100 rounded-t-2xl">
                        <div className="min-w-0">
                            <div className="text-xs font-semibold uppercase tracking-wide text-yellow-950">Cell hint</div>
                            <div className="text-sm font-semibold text-yellow-950 truncate">{activeCellHint.label}</div>
                        </div>
                        <button
                            type="button"
                            onClick={() => setActiveCellHint(null)}
                            className="px-2 py-1 rounded-lg border border-yellow-300 bg-white text-yellow-900 hover:bg-yellow-100"
                        >
                            Close
                        </button>
                    </div>
                    {renderCellHintPopupContent(activeCellHint)}
                </div>
            )}
        </>
    );
};

export default Grade10AccountingFinalAccountsPractice;

