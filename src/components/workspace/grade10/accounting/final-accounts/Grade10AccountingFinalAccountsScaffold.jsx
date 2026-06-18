import React, { useEffect, useRef, useState } from 'react';
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
    if (guidelines.length > 0) sections.push({ title: 'What to include', text: guidelines.join('\n') });
    if (memoLabels.length > 0) sections.push({ title: 'Memo structure', text: memoLabels.join('\n') });
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
        const value = row['2'];
        if (value) used.add(String(value));
    });
    return used;
};

const Grade10AccountingFinalAccountsScaffold = ({
    onBack, scaffoldSteps,
    g10AcctFAVisualAidsOpen, setG10AcctFAVisualAidsOpen,
    g10AcctFAScaffoldDifficulty, setG10AcctFAScaffoldDifficulty,
    g10AcctFAScaffoldStepIndex, setG10AcctFAScaffoldStepIndex,
    fetchGrade10AcctFAScaffoldQuestion,
    g10AcctFAScaffoldLoading, g10AcctFAScaffoldError, g10AcctFAScaffoldQuestion,
    g10AcctFAScaffoldAnswer, setG10AcctFAScaffoldAnswer,
    g10AcctFAScaffoldFeedback, setG10AcctFAScaffoldFeedback,
    g10AcctFAScaffoldShowHint, setG10AcctFAScaffoldShowHint,
    renderGrade10AcctFAVisualAids, hideConfig, evaluationState,
    isMarkingEnv,
}) => {
    const question = g10AcctFAScaffoldQuestion;
    const [activeCellHint, setActiveCellHint] = useState(null);
    const [showCheckHighlights, setShowCheckHighlights] = useState(false);
    const [showMemo, setShowMemo] = useState(false);
    const cellHintPopupRef = useRef(null);
    const selectedSubtopic = scaffoldSteps[g10AcctFAScaffoldStepIndex] || scaffoldSteps[0];
    const marking = useGrade10AccountingMarking();
    const nonTabularMemoItems = question && question?.question_type !== 'table_wordbank' && !isFillInTableQuestionType(question?.question_type) ? buildNonTabularMemoItems(question) : [];
    const wordbankMemoRows = question?.question_type === 'table_wordbank' ? buildWordbankMemoRows(question) : [];
    const typedHintSections = question?.question_type === 'typed' ? buildTypedHintSections(question) : [];
    const calcHintText = String(question?.formula_hint || question?.working_formula || '').trim();

    useEffect(() => {
        marking.setMarkingMode(isMarkingEnv ? 'marking_active' : 'practice');
    }, [g10AcctFAScaffoldStepIndex, isMarkingEnv]);

    useEffect(() => {
        setShowMemo(false);
        setShowCheckHighlights(false);
        setActiveCellHint(null);
    }, [question?.id]);

    useEffect(() => {
        if (!activeCellHint || !cellHintPopupRef.current) return;
        const width = cellHintPopupRef.current.offsetWidth || 320;
        const height = cellHintPopupRef.current.offsetHeight || 240;
        const next = clampHintPosition(activeCellHint.x, activeCellHint.y, width, height);
        if (next.x !== activeCellHint.x || next.y !== activeCellHint.y) {
            setActiveCellHint((prev) => (prev ? { ...prev, x: next.x, y: next.y } : prev));
        }
    }, [activeCellHint]);

    useEffect(() => {
        if (!question) return;
        if (isFillInTableQuestionType(question?.question_type) && (!g10AcctFAScaffoldAnswer || typeof g10AcctFAScaffoldAnswer !== 'object' || !g10AcctFAScaffoldAnswer.cells)) {
            setG10AcctFAScaffoldAnswer(buildEmptyTableAnswer(question));
        }
        if (question.question_type === 'table_wordbank' && (!g10AcctFAScaffoldAnswer || typeof g10AcctFAScaffoldAnswer !== 'object' || !g10AcctFAScaffoldAnswer.selections)) {
            setG10AcctFAScaffoldAnswer(buildEmptyWordbankAnswer(question));
        }
    }, [question?.id]);

    const newExample = () => {
        fetchGrade10AcctFAScaffoldQuestion({ subskill: selectedSubtopic?.key || 'closing_transfers', difficulty: g10AcctFAScaffoldDifficulty });
        setShowMemo(false);
    };

    const checkAnswer = () => {
        if (!question) return;
        if (question.question_type === 'mcq') {
            const ok = String(g10AcctFAScaffoldAnswer) === String(question.correct_index);
            setG10AcctFAScaffoldFeedback(ok ? { kind: 'success', message: 'Correct.' } : { kind: 'error', message: `Not quite. Correct: ${question.options?.[question.correct_index] || ''}` });
            return;
        }
        if (question.question_type === 'calc') {
            const expected = parseFloat(question.correct_answer);
            const got = parseFloat(g10AcctFAScaffoldAnswer);
            if (isNaN(got)) { setG10AcctFAScaffoldFeedback({ kind: 'error', message: 'Enter a number.' }); return; }
            const ok = Math.abs(expected - got) < 0.01;
            setG10AcctFAScaffoldFeedback(ok ? { kind: 'success', message: 'Correct!' } : { kind: 'error', message: `Not quite. Expected: R${expected.toFixed(2)}` });
            return;
        }
        if (question.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(question);
            const ans = (g10AcctFAScaffoldAnswer && typeof g10AcctFAScaffoldAnswer === 'object') ? g10AcctFAScaffoldAnswer : buildEmptyWordbankAnswer(question);
            const selections = ans?.selections && typeof ans.selections === 'object' ? ans.selections : {};
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
            setG10AcctFAScaffoldFeedback(ok ? { kind: 'success', message: 'Correct.' } : { kind: 'error', message: `Not quite. You matched ${hit}/${total} correctly.` });
            return;
        }
        if (question.question_type === 'typed') {
            if (!normalizeText(g10AcctFAScaffoldAnswer)) { setG10AcctFAScaffoldFeedback({ kind: 'error', message: 'Write an answer, then check.' }); return; }
            setG10AcctFAScaffoldFeedback({ kind: 'info', message: 'Answer submitted. Use Compare / Memo to review the memo and guidance.' });
            return;
        }
        if (isFillInTableQuestionType(question.question_type)) {
            const correctMap = getCorrectMap(question);
            const ans = (g10AcctFAScaffoldAnswer && typeof g10AcctFAScaffoldAnswer === 'object') ? g10AcctFAScaffoldAnswer : buildEmptyTableAnswer(question);
            const cells = ans?.cells && typeof ans.cells === 'object' ? ans.cells : {};
            const keys = Object.keys(correctMap);
            let hit = 0;
            keys.forEach((key) => {
                const expected = correctMap[key];
                const got = cells[key];
                if (normalizeText(got) === normalizeText(expected) || numbersMatch(got, expected)) hit += 1;
            });
            const ok = keys.length > 0 && hit === keys.length;
            setShowCheckHighlights(true);
            setG10AcctFAScaffoldFeedback(ok ? { kind: 'success', message: 'Correct.' } : { kind: 'error', message: `Not quite. You completed ${hit}/${keys.length} cells correctly.` });
            return;
        }
        setG10AcctFAScaffoldFeedback({ kind: 'info', message: 'Answer saved.' });
    };

    const setAnswerValue = (value) => {
        setG10AcctFAScaffoldAnswer(value);
        if (question) marking.registerAnswer(question.id, value);
        setG10AcctFAScaffoldFeedback(null);
        setShowMemo(false);
        setShowCheckHighlights(false);
        setActiveCellHint(null);
    };

    const renderWordbankTable = () => {
        if (!question) return null;
        const ans = (g10AcctFAScaffoldAnswer && typeof g10AcctFAScaffoldAnswer === 'object') ? g10AcctFAScaffoldAnswer : buildEmptyWordbankAnswer(question);
        const wordBank = getWordBank(question);
        const used = getUsedTokenIds(ans);
        const tokenLabelById = {};
        wordBank.forEach((token) => {
            tokenLabelById[String(token.id)] = String(token.label || '').trim();
        });

        const setActiveTokenId = (tokenId) => {
            setAnswerValue({ ...(ans || {}), activeTokenId: tokenId });
        };

        const clearCell = (rowIndex) => {
            setAnswerValue({
                ...(ans || {}),
                selections: {
                    ...(ans?.selections || {}),
                    [String(rowIndex)]: {
                        ...((ans?.selections || {})[String(rowIndex)] || {}),
                        '2': null,
                    },
                },
            });
        };

        const placeActive = (rowIndex) => {
            const tokenId = ans?.activeTokenId;
            if (!tokenId || used.has(String(tokenId))) return;
            setAnswerValue({
                ...(ans || {}),
                selections: {
                    ...(ans?.selections || {}),
                    [String(rowIndex)]: {
                        ...((ans?.selections || {})[String(rowIndex)] || {}),
                        '2': String(tokenId),
                    },
                },
                activeTokenId: null,
            });
        };

        const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
        const headers = Array.isArray(question?.table?.headers) ? question.table.headers : [];

        return (
            <div className="mt-3">
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
                                    {token.label}
                                </button>
                            );
                        })}
                    </div>
                </div>
                <div className="overflow-x-auto">
                    <table className="min-w-full border border-slate-200 text-sm">
                        <thead className="bg-slate-50">
                            <tr>
                                {headers.map((header, index) => (
                                    <th key={index} className="px-3 py-2 border-b border-slate-200 text-left font-semibold text-slate-900">{header}</th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {rows.map((row, rowIndex) => {
                                const tokenId = ans?.selections?.[String(rowIndex)]?.['2'];
                                const tokenLabel = tokenLabelById[String(tokenId)] || '';
                                return (
                                    <tr key={rowIndex} className="border-b border-slate-100 last:border-b-0">
                                        <td className="px-3 py-2 text-slate-700">{row?.[0]}</td>
                                        <td className="px-3 py-2 text-slate-700">{row?.[1]}</td>
                                        <td className="px-3 py-2">
                                            <div className="flex flex-wrap items-center gap-2">
                                                <button type="button" onClick={() => placeActive(rowIndex)} className="min-w-[180px] text-left px-3 py-2 rounded-lg border border-dashed border-slate-300 bg-white text-slate-700 hover:bg-slate-50">
                                                    {tokenLabel || 'Place selected term here'}
                                                </button>
                                                {tokenLabel && (
                                                    <button type="button" onClick={() => clearCell(rowIndex)} className="px-2 py-1 rounded-md border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50">
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

    const renderOneStructuredTable = (table, tableIndex, { readOnly = false, cellValues = null } = {}) => {
        if (!table) return null;
        const headers = Array.isArray(table?.headers) ? table.headers : [];
        const headerRows = Array.isArray(table?.header_rows) ? table.header_rows : [];
        const rows = Array.isArray(table?.rows) ? table.rows : [];
        const ans = (g10AcctFAScaffoldAnswer && typeof g10AcctFAScaffoldAnswer === 'object') ? g10AcctFAScaffoldAnswer : buildEmptyTableAnswer(question);
        const cells = cellValues && typeof cellValues === 'object'
            ? cellValues
            : (ans?.cells && typeof ans.cells === 'object' ? ans.cells : {});
        const correctMap = getCorrectMap(question);
        const cellHints = (question?.cell_hints && typeof question.cell_hints === 'object') ? question.cell_hints : {};
        const cellTeachingMap = (question?.cell_teaching_map && typeof question.cell_teaching_map === 'object') ? question.cell_teaching_map : {};
        const workingMap = (question?.working_map && typeof question.working_map === 'object') ? question.working_map : {};

        const tableStyle = { width: '100%', minWidth: `${Math.max(headers.length * 112, 720)}px`, borderCollapse: 'collapse', tableLayout: 'fixed' };
        const headerStyle = { border: '1px solid #000', padding: '6px', background: '#e5e7eb', fontWeight: 600, textAlign: 'center', verticalAlign: 'middle' };
        const bodyStyle = { border: '1px solid #000', padding: 0, verticalAlign: 'top' };

        const openCellHint = (cellId, label, text, sections, triggerEl) => {
            const rect = triggerEl?.getBoundingClientRect?.();
            const anchorX = rect ? rect.left : 24;
            const anchorY = rect ? rect.bottom + 10 : 24;
            const next = clampHintPosition(anchorX, anchorY, 320, 240);
            setActiveCellHint((prev) => {
                if (prev?.cellId === cellId) return null;
                return {
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
                                    const derivationHint = String((question?.derivation_map || {})?.[String(cellId)] || '').trim();
                                    const workingHint = String(workingMap[String(cellId)] || '').trim();
                                    const hintParts = [];
                                    if (exactCellHint) hintParts.push(exactCellHint);
                                    else if (rowHint) hintParts.push(rowHint);
                                    if (derivationHint) hintParts.push(derivationHint);
                                    if (workingHint) hintParts.push(workingHint);
                                    const cellHintText = hintParts.join('\n\n').trim();
                                    const cellHintSections = buildHintSections(cellTeachingMap[String(cellId)], cellHintText);
                                    const showCellHintButton = g10AcctFAScaffoldShowHint && marking.isPracticeMode && editable && cellHintSections.length > 0;
                                    const cellLabel = String(headers[cellIndex] || cellId);
                                    let displayValue = rawValue;
                                    let cellBorder = 'none';
                                    let cellBg = '';
                                    let memoTooltip = derivationHint || (expected !== undefined ? `Expected: ${expected}` : '');
                                    if (!readOnly && showCheckHighlights && editable && expected !== undefined) {
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
                                                        onChange={(e) => setAnswerValue({
                                                            ...ans,
                                                            cells: {
                                                                ...((ans?.cells && typeof ans.cells === 'object') ? ans.cells : {}),
                                                                [String(cellId)]: e.target.value,
                                                            },
                                                        })}
                                                        readOnly={showMemo}
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
                                                    {showMemo && memoTooltip && String(rawValue).trim() !== String(displayValue).trim() && (
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

    const renderPromptTables = () => {
        const promptTables = getPromptTables(question);
        if (!promptTables.length) return null;
        return (
            <div className="space-y-4">
                {promptTables.map((table, idx) => (
                    <div key={`prompt-${idx}`}>
                        <div className="mt-4 mb-2 text-sm font-semibold text-slate-700">{table?.heading || 'Source information'}</div>
                        {renderOneStructuredTable(table, -100 - idx, { readOnly: true })}
                    </div>
                ))}
            </div>
        );
    };

    const renderStructuredTables = () => {
        const tables = getStructuredTables(question);
        return (
            <div className="space-y-4">
                {tables.map((table, idx) => (
                    <div key={`table-${idx}`}>
                        <div className="mt-4 mb-2 text-sm font-semibold text-slate-800">{table?.heading || 'Accounting table'}</div>
                        {renderOneStructuredTable(table, idx)}
                    </div>
                ))}
            </div>
        );
    };

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
                                <select value={g10AcctFAScaffoldStepIndex} onChange={(e) => { setG10AcctFAScaffoldStepIndex(Number(e.target.value) || 0); setG10AcctFAScaffoldFeedback(null); setG10AcctFAScaffoldShowHint(false); setG10AcctFAScaffoldAnswer(null); }} className="mt-1 w-full p-2 border rounded-lg">
                                    {scaffoldSteps.map((s, i) => <option key={s.key} value={i}>{s.title}</option>)}
                                </select>
                            </div>
                            <div>
                                <label className="text-sm font-semibold text-slate-700">Difficulty</label>
                                <select value={g10AcctFAScaffoldDifficulty} onChange={(e) => setG10AcctFAScaffoldDifficulty(e.target.value)} className="mt-1 p-2 border rounded-lg">
                                    <option value="easy">Easy</option><option value="medium">Medium</option><option value="hard">Hard</option>
                                </select>
                            </div>
                            <button onClick={newExample} className="px-4 py-2 bg-slate-900 text-white rounded-lg font-semibold hover:bg-slate-800" disabled={g10AcctFAScaffoldLoading}>{g10AcctFAScaffoldLoading ? 'Loading…' : 'New Example'}</button>
                        </div>
                    </div>
                </div>
            )}

            {g10AcctFAScaffoldError && <div className="mb-3 p-3 bg-red-50 border border-red-200 text-red-800 rounded-lg text-sm break-words">{g10AcctFAScaffoldError}</div>}
            {g10AcctFAScaffoldLoading && <div className="text-sm text-slate-500">Loading...</div>}

            {question && (
                <div className="space-y-4">
                    {question.question_type === 'mcq' && (
                        <div className="mt-3 grid grid-cols-1 gap-2">
                            {(question.options || []).map((opt, idx) => (
                                <MCQOption key={idx} selected={String(g10AcctFAScaffoldAnswer) === String(idx)} onClick={() => setAnswerValue(String(idx))} label={opt} />
                            ))}
                        </div>
                    )}

                    {question.question_type === 'calc' && (
                        <div className="mt-3 flex items-center gap-2">
                            <span className="text-slate-500 font-medium">R</span>
                            <input type="number" step="0.01" className="w-full max-w-xs p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-400" placeholder="0.00" value={g10AcctFAScaffoldAnswer || ''} onChange={(e) => setAnswerValue(e.target.value)} />
                        </div>
                    )}

                    {question.question_type === 'typed' && (
                        <div className="mt-3">
                            <textarea value={g10AcctFAScaffoldAnswer || ''} onChange={(e) => setAnswerValue(e.target.value)} placeholder="Write your answer..." className="w-full min-h-[120px] p-3 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-slate-300" />
                        </div>
                    )}

                    {question.question_type === 'table_wordbank' && renderWordbankTable()}

                    {isFillInTableQuestionType(question.question_type) && renderPromptTables()}

                    {isFillInTableQuestionType(question.question_type) && renderStructuredTables()}

                    <div className="mt-4 flex flex-wrap gap-2">
                        {marking.isPracticeMode ? (
                            <>
                                <button type="button" onClick={checkAnswer} className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-sm font-semibold transition-all">Check</button>
                                <button type="button" onClick={() => setG10AcctFAScaffoldShowHint(!g10AcctFAScaffoldShowHint)} className="px-4 py-2 bg-white border border-slate-200 hover:bg-slate-50 text-slate-800 rounded-xl text-sm font-semibold transition-all">Hint</button>
                                {g10AcctFAScaffoldFeedback && (['typed', 'calc', 'table_wordbank'].includes(String(question?.question_type || '')) || isFillInTableQuestionType(question?.question_type)) && (
                                    <button type="button" onClick={() => setShowMemo(!showMemo)} className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all border ${showMemo ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 text-slate-800 hover:bg-slate-50'}`}>
                                        {showMemo ? 'Hide Memo' : 'Compare / Memo'}
                                    </button>
                                )}
                                {(g10AcctFAScaffoldFeedback || showMemo || g10AcctFAScaffoldShowHint) && (
                                    <button type="button" onClick={() => { setG10AcctFAScaffoldFeedback(null); setG10AcctFAScaffoldShowHint(false); setShowMemo(false); setShowCheckHighlights(false); setActiveCellHint(null); }} className="px-4 py-2 bg-white border border-slate-200 hover:bg-slate-50 text-slate-800 rounded-xl text-sm font-semibold transition-all">
                                        Clear feedback
                                    </button>
                                )}
                            </>
                        ) : (
                            !marking.isMarkingSubmitted && <button type="button" onClick={() => marking.submitAssessment([question])} disabled={marking.isSubmitting} className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors disabled:opacity-50">{marking.isSubmitting ? 'Submitting...' : 'Submit Assessment'}</button>
                        )}
                    </div>

                    {g10AcctFAScaffoldShowHint && question?.question_type === 'typed' && typedHintSections.length > 0 && marking.isPracticeMode && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
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

                    {g10AcctFAScaffoldShowHint && question?.question_type === 'calc' && calcHintText && marking.isPracticeMode && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 rounded-xl text-sm text-yellow-900">
                            <div className="font-semibold">Calculation hint</div>
                            <div className="mt-2 whitespace-pre-wrap">{calcHintText}</div>
                        </div>
                    )}

                    {g10AcctFAScaffoldShowHint && question?.question_type === 'table_wordbank' && Array.isArray(question?.guidelines) && question.guidelines.length > 0 && marking.isPracticeMode && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                            <div className="font-semibold text-yellow-900">Word-bank hint</div>
                            <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                {question.guidelines.map((item, index) => <li key={index}>{item}</li>)}
                            </ul>
                        </div>
                    )}

                    {g10AcctFAScaffoldShowHint && isFillInTableQuestionType(question?.question_type) && Array.isArray(question?.guidelines) && question.guidelines.length > 0 && marking.isPracticeMode && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                            <div className="font-semibold text-yellow-900">Bookkeeping-table hint</div>
                            <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                {question.guidelines.map((item, index) => <li key={index}>{item}</li>)}
                            </ul>
                        </div>
                    )}

                    {g10AcctFAScaffoldShowHint && question?.question_type !== 'typed' && question?.question_type !== 'calc' && question?.question_type !== 'table_wordbank' && !isFillInTableQuestionType(question?.question_type) && marking.isPracticeMode && <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 text-yellow-900 rounded-xl text-sm">Use the visual aids panel for formulas, closing-transfer flow, and adjustment logic.</div>}

                    {g10AcctFAScaffoldFeedback && marking.isPracticeMode && (
                        <div className={`mt-3 p-3 rounded-xl text-sm border ${g10AcctFAScaffoldFeedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : g10AcctFAScaffoldFeedback.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                            {g10AcctFAScaffoldFeedback.message}
                        </div>
                    )}

                    {showMemo && question?.question_type !== 'table_wordbank' && nonTabularMemoItems.length > 0 && (
                        <div className="mt-3 p-3 bg-slate-50 border border-slate-200 rounded-xl">
                            <div className="font-semibold text-slate-800">Compare / Memo</div>
                            <div className="mt-3 space-y-3 text-sm text-slate-700">
                                {nonTabularMemoItems.map((item) => (
                                    <div key={`${item.label}-${item.value}`}>
                                        <div className="font-semibold text-slate-900">{item.label}</div>
                                        <div className="whitespace-pre-wrap">{item.value}</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}

                    {showMemo && question?.question_type === 'table_wordbank' && wordbankMemoRows.length > 0 && (
                        <div className="mt-3 p-3 bg-slate-50 border border-slate-200 rounded-xl">
                            <div className="font-semibold text-slate-800">Compare / Memo</div>
                            <div className="mt-3 space-y-3 text-sm text-slate-700">
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

                    {showMemo && isFillInTableQuestionType(question?.question_type) && (
                        <div className="mt-3 p-3 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                            Compare / Memo is shown directly in the table above. Correct values are displayed in-place with green highlighting.
                        </div>
                    )}
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

export default Grade10AccountingFinalAccountsScaffold;

