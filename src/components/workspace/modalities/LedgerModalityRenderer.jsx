import React, { useState, useEffect } from 'react';
import { Lightbulb, BookOpen, ChevronDown, ChevronUp, Loader2 } from 'lucide-react';

export default function LedgerModalityRenderer({
    question,
    topic,
    onCheck,
    result,
    isChecking,
    showDynamicScaffold,
    onToggleScaffold,
}) {
    if (!question) return null;

    const questionStorageKey = question?.id ? `fundile_draft_cells_${question.id}` : null;
    const offlineStorageKey = question?.id ? `fundile_offline_draft_cells_${question.id}` : null;

    const [isOnline, setIsOnline] = useState(() => (typeof navigator !== 'undefined' ? navigator.onLine : true));
    const [draftSaved, setDraftSaved] = useState(false);

    // Track online/offline status
    useEffect(() => {
        const handleOnline = () => setIsOnline(true);
        const handleOffline = () => setIsOnline(false);
        window.addEventListener('online', handleOnline);
        window.addEventListener('offline', handleOffline);
        return () => {
            window.removeEventListener('online', handleOnline);
            window.removeEventListener('offline', handleOffline);
        };
    }, []);

    const [cellValues, setCellValues] = useState(() => {
        if (typeof window !== 'undefined') {
            try {
                if (questionStorageKey) {
                    const savedSession = sessionStorage.getItem(questionStorageKey);
                    if (savedSession) return JSON.parse(savedSession);
                }
                if (offlineStorageKey) {
                    const savedLocal = localStorage.getItem(offlineStorageKey);
                    if (savedLocal) {
                        const parsed = JSON.parse(savedLocal);
                        return parsed.values || parsed;
                    }
                }
            } catch (e) {}
        }
        return {};
    });
    const [activeCellId, setActiveCellId] = useState(null);
    const [revealedMemo, setRevealedMemo] = useState(false);
    const [savedLearnerValues, setSavedLearnerValues] = useState(null);

    // Reset entered values or rehydrate draft whenever question changes
    useEffect(() => {
        if (questionStorageKey) {
            try {
                const savedSession = sessionStorage.getItem(questionStorageKey);
                if (savedSession) {
                    setCellValues(JSON.parse(savedSession));
                    setDraftSaved(true);
                    return;
                }
                if (offlineStorageKey) {
                    const savedLocal = localStorage.getItem(offlineStorageKey);
                    if (savedLocal) {
                        const parsed = JSON.parse(savedLocal);
                        const vals = parsed.values || parsed;
                        setCellValues(vals);
                        setDraftSaved(true);
                        try { sessionStorage.setItem(questionStorageKey, JSON.stringify(vals)); } catch (e) {}
                        return;
                    }
                }
            } catch (e) {}
        }
        setCellValues({});
        setActiveCellId(null);
        setDraftSaved(false);
        setRevealedMemo(false);
        setSavedLearnerValues(null);
    }, [question?.id, question?.question_id, question?.prompt, questionStorageKey, offlineStorageKey]);

    const journal = question.journal || {};
    const titleFields = journal.title_fields || question.title_fields || [];

    // Calculate authentic South African paper stationery column proportions
    const getColumnWidthInfo = (label) => {
        const l = String(label || '').toLowerCase().trim();
        if (/^(day|date)$/i.test(l)) {
            return {
                widthClass: 'w-[48px] min-w-[44px] max-w-[55px]',
                colWidth: '48px',
            };
        }
        if (/^(doc|no|doc\s*no|voucher|inv|invoice)$/i.test(l)) {
            return {
                widthClass: 'w-[56px] min-w-[50px] max-w-[65px]',
                colWidth: '56px',
            };
        }
        if (/^(fol|folio|sundry\s*fol)$/i.test(l)) {
            return {
                widthClass: 'w-[50px] min-w-[46px] max-w-[60px]',
                colWidth: '50px',
            };
        }
        if (/creditor|debtor|details|account|particulars|description/i.test(l)) {
            return {
                widthClass: 'w-[250px] min-w-[210px]',
                colWidth: '250px',
            };
        }
        if (/sundry\s*details/i.test(l)) {
            return {
                widthClass: 'w-[180px] min-w-[150px]',
                colWidth: '180px',
            };
        }
        if (/amount|control|stock|stationery|bank|sales|cost|vat|total|price/i.test(l)) {
            return {
                widthClass: 'w-[110px] min-w-[95px] max-w-[130px]',
                colWidth: '110px',
            };
        }
        return {
            widthClass: 'w-[96px] min-w-[85px]',
            colWidth: '96px',
        };
    };

    // Normalize column headers
    const rawHeaders = journal.headers || question.columns || question.table_schema?.columns || ['Date', 'Details', 'Fol', 'Debit', 'Credit'];
    const headers = rawHeaders.map((col, idx) => {
        const label = typeof col === 'string' ? col : col.title || col.label || `Col ${idx + 1}`;
        const lNorm = label.toLowerCase();
        const isNumeric = /debit|credit|bank|sales|cost|amount|total|vat|receipts|r|price|disc/i.test(lNorm);
        const isCenter = /^(doc|day|fol|no|date)$/i.test(lNorm);
        const widthInfo = getColumnWidthInfo(label);
        return {
            label,
            isNumeric,
            isCenter,
            widthClass: widthInfo.widthClass,
            colWidth: widthInfo.colWidth,
        };
    });

    // Normalize table rows
    const rawRows = journal.rows || question.rows || question.table_schema?.rows || 5;
    const normalizedRows = (() => {
        if (Array.isArray(rawRows)) {
            return rawRows.map((rowItem, rIdx) => {
                const cellList = Array.isArray(rowItem)
                    ? rowItem
                    : Array.isArray(rowItem?.cells)
                        ? rowItem.cells
                        : headers.map((_, cIdx) => ({
                            cell_id: `r${rIdx}_c${cIdx}`,
                            value: '',
                            editable: true,
                        }));

                return cellList.map((cell, cIdx) => {
                    if (cell && typeof cell === 'object') {
                        return {
                            cell_id: cell.cell_id || `r${rIdx}_c${cIdx}`,
                            value: cell.value ?? '',
                            editable: Boolean(cell.editable),
                        };
                    }
                    return {
                        cell_id: `r${rIdx}_c${cIdx}`,
                        value: String(cell ?? ''),
                        editable: false,
                    };
                });
            });
        }

        // Numeric rows fallback
        const count = typeof rawRows === 'number' ? rawRows : 5;
        return Array.from({ length: count }, (_, rIdx) =>
            headers.map((_, cIdx) => ({
                cell_id: `r${rIdx}_c${cIdx}`,
                value: '',
                editable: true,
            }))
        );
    })();

    // Extract hints and pedagogical derivation maps
    const cellHints = journal.cell_hints || question.cell_hints || {};
    const cellTeachingMap = journal.cell_teaching_map || question.cell_teaching_map || {};
    const derivationMap = journal.derivation_map || question.derivation_map || {};

    const getCellHint = (cellId) => {
        if (!cellId) return null;
        const directHint = cellHints[cellId];
        const teaching = cellTeachingMap[cellId];
        const derivation = derivationMap[cellId];

        if (!directHint && !teaching && !derivation) return null;

        let title = '';
        let text = '';

        if (typeof directHint === 'string') {
            text = directHint;
        } else if (typeof directHint === 'object' && directHint !== null) {
            title = directHint.title || '';
            text = Array.isArray(directHint.steps)
                ? directHint.steps.join(' ')
                : (directHint.message || '');
        }

        if (!text && teaching) {
            text = teaching.how_to_derive || teaching.rule_or_principle || teaching.role_in_requirement || '';
        }

        if (!text && derivation) {
            text = derivation;
        }

        return {
            title,
            text,
            teaching,
            derivation,
        };
    };

    const handleCellChange = (cellId, val) => {
        setCellValues((prev) => {
            const next = {
                ...prev,
                [cellId]: val,
            };
            if (typeof window !== 'undefined') {
                if (questionStorageKey) {
                    try {
                        sessionStorage.setItem(questionStorageKey, JSON.stringify(next));
                    } catch (e) {}
                }
                if (offlineStorageKey) {
                    try {
                        localStorage.setItem(offlineStorageKey, JSON.stringify({
                            values: next,
                            updatedAt: Date.now(),
                            questionId: question?.id
                        }));
                    } catch (e) {}
                }
            }
            setDraftSaved(true);
            return next;
        });
    };

    // Clean up draft once checking result is verified
    useEffect(() => {
        if (result) {
            if (questionStorageKey) {
                try {
                    sessionStorage.removeItem(questionStorageKey);
                } catch (e) {}
            }
            if (offlineStorageKey) {
                try {
                    localStorage.removeItem(offlineStorageKey);
                } catch (e) {}
            }
            setDraftSaved(false);
        }
    }, [result, questionStorageKey, offlineStorageKey]);

    const handleCheckSubmission = () => {
        if (onCheck) {
            onCheck({
                cells: cellValues,
                ...cellValues,
            });
        }
    };

    const handleToggleRevealExpectedAnswers = () => {
        if (!revealedMemo) {
            setSavedLearnerValues({ ...cellValues });
            const expected = {};

            // 1. Primary ground-truth: question.correct_map (used across accounting & EMS generators)
            if (question?.correct_map && typeof question.correct_map === 'object') {
                Object.entries(question.correct_map).forEach(([k, v]) => {
                    if (v !== undefined && v !== null && String(v).trim() !== '') {
                        expected[k] = String(v);
                    }
                });
            }

            // 2. Expected cells / values aliases
            const altSources = [question?.expected_cells, question?.expected_values, question?.model_table];
            altSources.forEach((src) => {
                if (src && typeof src === 'object') {
                    Object.entries(src).forEach(([k, v]) => {
                        if (v !== undefined && v !== null && String(v).trim() !== '' && !expected[k]) {
                            expected[k] = String(v);
                        }
                    });
                }
            });

            // 3. Evaluation result cell_results expected values (if verified by backend evaluator)
            if (result?.cell_results) {
                Object.entries(result.cell_results).forEach(([k, v]) => {
                    if (v && v.expected !== undefined && v.expected !== null && String(v.expected).trim() !== '') {
                        expected[k] = String(v.expected);
                    }
                });
            }

            // 4. Pre-baked row cell values ONLY if they specify an explicit expected or solution property
            if (question?.journal?.rows && Array.isArray(question.journal.rows)) {
                question.journal.rows.forEach((r) => {
                    if (Array.isArray(r)) {
                        r.forEach((c) => {
                            if (c && c.cell_id) {
                                const explicitExpected = c.expected ?? c.solution;
                                if (explicitExpected !== undefined && explicitExpected !== null && String(explicitExpected).trim() !== '') {
                                    expected[c.cell_id] = String(explicitExpected);
                                }
                            }
                        });
                    }
                });
            }

            // 5. Title fields if any
            if (question?.journal?.title_fields && Array.isArray(question.journal.title_fields)) {
                question.journal.title_fields.forEach((f) => {
                    if (f && f.cell_id && f.value && !expected[f.cell_id]) {
                        expected[f.cell_id] = String(f.value);
                    }
                });
            }

            setCellValues((prev) => ({
                ...prev,
                ...expected,
            }));
            setRevealedMemo(true);
        } else {
            if (savedLearnerValues) {
                setCellValues({ ...savedLearnerValues });
            }
            setRevealedMemo(false);
        }
    };

    const activeHint = activeCellId ? getCellHint(activeCellId) : null;

    return (
        <div className="space-y-4 font-sans">
            {/* Model Solution Populated Banner */}
            {revealedMemo && (
                <div data-testid="banner-ledger-memo-active" className="p-2.5 rounded-xl bg-amber-50 border border-amber-300 text-xs text-amber-900 flex items-center justify-between shadow-2xs font-sans">
                    <div className="flex items-center gap-2">
                        <span className="font-bold">📖 Model Solution Populated in Table:</span>
                        <span>Studying expected journal values. Click &quot;Restore My Entries&quot; to continue your attempt.</span>
                    </div>
                    <button
                        type="button"
                        onClick={handleToggleRevealExpectedAnswers}
                        className="text-amber-800 font-bold underline cursor-pointer text-xs shrink-0 ml-2"
                    >
                        Restore My Entries
                    </button>
                </div>
            )}

            {/* Dynamic Ledger Scaffold Guidance */}
            <div className="rounded-xl border border-blue-200 bg-blue-50/60 p-3.5 transition-all">
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                        <span className="grid place-items-center h-6 w-6 rounded-lg bg-[#13519C] text-white text-xs font-bold">
                            <BookOpen className="w-3.5 h-3.5" />
                        </span>
                        <span className="text-xs font-bold text-[#13519C] uppercase tracking-wide">
                            Accounting Rules &amp; Double-Entry Equation
                        </span>
                    </div>
                    <button
                        type="button"
                        onClick={onToggleScaffold}
                        className="text-xs font-bold text-[#13519C] hover:underline cursor-pointer flex items-center gap-1 font-sans"
                    >
                        {showDynamicScaffold ? (
                            <>Hide Rules <ChevronUp className="w-3.5 h-3.5" /></>
                        ) : (
                            <>Show Transaction Rules <ChevronDown className="w-3.5 h-3.5" /></>
                        )}
                    </button>
                </div>

                {showDynamicScaffold && (
                    <div className="mt-3 pt-3 border-t border-blue-100 text-xs text-slate-700 space-y-1.5 animate-in fade-in">
                        <p className="font-semibold text-slate-800">Double Entry Reminder &amp; Ledger Direction:</p>
                        <div className="grid sm:grid-cols-2 gap-2 pt-1">
                            <div className="bg-white p-2 rounded-lg border border-blue-100 shadow-2xs">
                                <strong className="text-blue-900 block font-semibold">Debit (+) / Credit (-)</strong>
                                <span>Assets &amp; Expenses increase on the <strong>Debit</strong> side.</span>
                            </div>
                            <div className="bg-white p-2 rounded-lg border border-blue-100 shadow-2xs">
                                <strong className="text-blue-900 block font-semibold">Credit (+) / Debit (-)</strong>
                                <span>Liabilities, Equity, and Income increase on the <strong>Credit</strong> side.</span>
                            </div>
                        </div>
                    </div>
                )}
            </div>

            {/* Statement Header Bar (Business Name, Period, Statement Title) */}
            {titleFields && titleFields.length > 0 && (
                <div className="rounded-xl border border-slate-200 bg-slate-50/90 p-3 flex flex-wrap items-center gap-3 sm:gap-4 shadow-2xs">
                    <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-slate-200 text-slate-700 uppercase tracking-wider font-mono">
                        Statement Heading
                    </span>
                    {titleFields.map((field) => {
                        const cellId = field.cell_id;
                        const isEditable = field.editable !== false;
                        const fieldVal = cellValues[cellId] ?? (isEditable ? '' : (field.value || ''));
                        const cellResult = result?.cell_results?.[cellId];
                        const hasHint = Boolean(getCellHint(cellId));

                        if (!isEditable) {
                            return (
                                <div key={cellId} className="flex items-center gap-1.5 text-xs">
                                    <span className="font-semibold text-slate-500">{field.label}:</span>
                                    <span className="font-bold text-slate-900">{field.value || fieldVal || field.label}</span>
                                </div>
                            );
                        }

                        const fl = String(field.label || '').toLowerCase();
                        const fieldWidthClass = /journal|statement/i.test(fl)
                            ? 'w-64 min-w-[220px]'
                            : /business|name|trader/i.test(fl)
                                ? 'w-52 min-w-[180px]'
                                : /month|year|date/i.test(fl)
                                    ? 'w-32 min-w-[110px]'
                                    : 'w-40 min-w-[140px]';

                        return (
                            <div key={cellId} className="flex items-center gap-2 text-xs">
                                <span className="font-semibold text-slate-700">{field.label}:</span>
                                <div className="relative">
                                    <input
                                        type="text"
                                        value={fieldVal}
                                        onChange={(e) => handleCellChange(cellId, e.target.value)}
                                        placeholder={`Enter ${field.label}...`}
                                        className={`${fieldWidthClass} px-2.5 py-1 ${hasHint ? 'pr-6' : ''} rounded-lg border text-xs font-semibold font-sans outline-none transition ${
                                            cellResult
                                                ? (cellResult.score > 0 || cellResult.is_correct)
                                                    ? 'bg-emerald-50 border-emerald-500 text-emerald-900 ring-1 ring-emerald-400'
                                                    : 'bg-rose-50 border-rose-400 text-rose-900 ring-1 ring-rose-300'
                                                : fieldVal
                                                    ? 'bg-blue-50/70 border-[#13519C] text-slate-900'
                                                    : 'bg-white border-slate-300 text-slate-700 hover:border-slate-400 focus:border-[#13519C] focus:ring-1 focus:ring-[#13519C]'
                                        }`}
                                    />
                                    {hasHint && (
                                        <button
                                            type="button"
                                            onClick={() => setActiveCellId((prev) => prev === cellId ? null : cellId)}
                                            title="View hint for heading"
                                            className="absolute right-1.5 top-1/2 -translate-y-1/2 text-amber-500 hover:text-amber-600 text-[11px] cursor-pointer"
                                        >
                                            💡
                                        </button>
                                    )}
                                </div>
                                {cellResult && (
                                    <span className={`text-[10px] font-bold px-1.5 py-0.5 rounded font-mono ${
                                        cellResult.score > 0 ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800'
                                    }`}>
                                        {cellResult.score > 0 ? `+${cellResult.score}` : '0'}
                                    </span>
                                )}
                            </div>
                        );
                    })}
                </div>
            )}

            {/* 2D Tabular Grid - Styled like authentic South African Accounting Ledger Stationery */}
            <div className="overflow-x-auto rounded-xl border border-slate-300 bg-[#FAFBFD] shadow-2xs">
                <table className="w-full min-w-max border-collapse text-xs select-text">
                    <colgroup>
                        {headers.map((col, idx) => (
                            <col key={idx} style={{ width: col.colWidth, minWidth: col.colWidth }} />
                        ))}
                    </colgroup>
                    <thead>
                        <tr className="bg-slate-100 border-b-2 border-slate-300 text-slate-700 uppercase text-[10px] font-bold font-sans tracking-wide">
                            {headers.map((col, idx) => (
                                <th
                                    key={idx}
                                    style={{ width: col.colWidth, minWidth: col.colWidth }}
                                    className={`p-2 border-r border-slate-300 last:border-r-0 ${col.widthClass} ${
                                        col.isNumeric ? 'text-right' : col.isCenter ? 'text-center' : 'text-left'
                                    }`}
                                >
                                    {col.label}
                                </th>
                            ))}
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-200/80 font-mono text-xs">
                        {normalizedRows.map((row, rIdx) => {
                            // Check if category/section row or totals row
                            const isTotalRow = row.some((c) =>
                                String(c.value || '').trim().toLowerCase().includes('total')
                            );
                            const isSectionRow =
                                row[0]?.editable === false &&
                                row.slice(1).every((c) => !c.editable && !c.value) &&
                                /section|account/i.test(String(row[0]?.value || ''));

                            const rowClasses = isTotalRow
                                ? 'bg-slate-100/90 font-bold border-t-2 border-slate-400 border-b-4 border-double border-slate-700'
                                : isSectionRow
                                    ? 'bg-slate-50 font-bold text-slate-800'
                                    : 'hover:bg-slate-50/60';

                            return (
                                <tr key={rIdx} className={rowClasses}>
                                    {row.map((cell, cIdx) => {
                                        const cellId = cell.cell_id;
                                        const isEditable = cell.editable;
                                        const cellVal = cellValues[cellId] ?? (isEditable ? '' : (cell.value ?? ''));
                                        const cellResult = result?.cell_results?.[cellId];
                                        const cellHint = getCellHint(cellId);
                                        const colMeta = headers[cIdx] || {};

                                        if (!isEditable) {
                                            return (
                                                <td
                                                    key={cIdx}
                                                    style={{ width: colMeta.colWidth, minWidth: colMeta.colWidth }}
                                                    className={`px-2.5 py-1.5 border-r border-slate-200 last:border-r-0 ${colMeta.widthClass || ''} ${
                                                        colMeta.isNumeric
                                                            ? 'text-right font-mono font-semibold'
                                                            : colMeta.isCenter
                                                                ? 'text-center font-mono'
                                                                : 'text-left font-sans'
                                                    } ${isTotalRow ? 'font-bold text-slate-900 bg-slate-100/90' : 'text-slate-800'}`}
                                                >
                                                    {cellVal ? (
                                                        <span>{String(cellVal)}</span>
                                                    ) : (
                                                        <span className="text-slate-300 select-none">—</span>
                                                    )}
                                                </td>
                                            );
                                        }

                                        return (
                                            <td
                                                key={cIdx}
                                                style={{ width: colMeta.colWidth, minWidth: colMeta.colWidth }}
                                                className={`p-1 border-r border-slate-200 last:border-r-0 relative ${colMeta.widthClass || ''}`}
                                            >
                                                <div className="relative flex items-center w-full">
                                                    <input
                                                        type="text"
                                                        value={cellVal}
                                                        onChange={(e) => handleCellChange(cellId, e.target.value)}
                                                        className={`w-full px-2 py-1.5 ${cellHint ? 'pr-6' : 'pr-1.5'} rounded-md border text-xs transition outline-none ${
                                                            colMeta.isNumeric
                                                                ? 'text-right font-mono font-bold'
                                                                : colMeta.isCenter
                                                                    ? 'text-center font-mono font-semibold'
                                                                    : 'text-left font-sans font-semibold'
                                                        } ${
                                                            revealedMemo
                                                                ? 'bg-amber-50/90 border-amber-400 text-amber-950 font-bold ring-1 ring-amber-300'
                                                                : cellResult
                                                                    ? (cellResult.score > 0 || cellResult.is_correct)
                                                                        ? 'bg-emerald-50 border-emerald-500 text-emerald-900 ring-1 ring-emerald-400'
                                                                        : 'bg-rose-50 border-rose-400 text-rose-900 ring-1 ring-rose-300'
                                                                    : cellVal
                                                                        ? 'bg-blue-50/70 border-[#13519C] text-slate-900'
                                                                        : 'bg-white border-slate-300 text-slate-700 hover:border-slate-400 focus:bg-white focus:border-[#13519C] focus:ring-1 focus:ring-[#13519C]'
                                                        }`}
                                                        placeholder="..."
                                                    />
                                                    {cellHint && (
                                                        <button
                                                            type="button"
                                                            onClick={() => setActiveCellId((prev) => prev === cellId ? null : cellId)}
                                                            title="Hint available"
                                                            className="absolute right-1 text-[11px] opacity-75 hover:opacity-100 cursor-pointer"
                                                        >
                                                            💡
                                                        </button>
                                                    )}
                                                </div>
                                                {cellResult && (
                                                    <div className="absolute top-0 right-1 -translate-y-1/2 pointer-events-none z-10">
                                                        <span
                                                            className={`text-[9px] font-bold px-1 rounded shadow-2xs font-mono ${
                                                                cellResult.score > 0
                                                                    ? 'bg-emerald-600 text-white'
                                                                    : 'bg-rose-600 text-white'
                                                            }`}
                                                        >
                                                            {cellResult.score > 0 ? `+${cellResult.score}` : '0'}
                                                        </span>
                                                    </div>
                                                )}
                                            </td>
                                        );
                                    })}
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            </div>

            {/* Active Cell Hint & Derivation Drawer */}
            {activeHint && (
                <div className="rounded-xl border border-amber-300 bg-amber-50 p-3.5 text-xs text-amber-950 space-y-1.5 shadow-2xs animate-in fade-in">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-1.5 font-bold text-amber-900">
                            <Lightbulb className="w-4 h-4 text-amber-600 shrink-0" />
                            <span>Guidance for Cell [{activeCellId}]: {activeHint.title || 'Entry Hint & Rule'}</span>
                        </div>
                        <button
                            type="button"
                            onClick={() => setActiveCellId(null)}
                            className="text-amber-700 hover:text-amber-900 text-xs font-bold cursor-pointer px-1"
                        >
                            ✕
                        </button>
                    </div>
                    {activeHint.text && <p className="leading-relaxed">{activeHint.text}</p>}
                    {activeHint.teaching && (
                        <div className="pt-1.5 border-t border-amber-200/80 grid sm:grid-cols-2 gap-2 text-[11px] text-amber-900">
                            {activeHint.teaching.rule_or_principle && (
                                <div className="bg-white/80 p-2 rounded-lg border border-amber-200">
                                    <strong className="font-semibold block text-amber-950">Accounting Principle / Rule:</strong>
                                    <span>{activeHint.teaching.rule_or_principle}</span>
                                </div>
                            )}
                            {activeHint.teaching.how_to_derive && (
                                <div className="bg-white/80 p-2 rounded-lg border border-amber-200">
                                    <strong className="font-semibold block text-amber-950">How to Derive:</strong>
                                    <span>{activeHint.teaching.how_to_derive}</span>
                                </div>
                            )}
                            {activeHint.teaching.transfer_tip && (
                                <div className="sm:col-span-2 bg-white/80 p-2 rounded-lg border border-amber-200">
                                    <strong className="font-semibold block text-amber-950">Exam Tip:</strong>
                                    <span>{activeHint.teaching.transfer_tip}</span>
                                </div>
                            )}
                        </div>
                    )}
                </div>
            )}

            {/* Submission Action Footer */}
            <div className="flex flex-wrap items-center justify-between gap-2 pt-1">
                <div className="text-xs text-slate-500 font-sans flex items-center gap-2 flex-wrap">
                    {Object.keys(cellValues).filter((k) => cellValues[k] !== '').length > 0 ? (
                        <span>
                            <strong className="font-mono text-slate-800 font-bold">
                                {Object.keys(cellValues).filter((k) => cellValues[k] !== '').length}
                            </strong>{' '}
                            cell(s) entered
                        </span>
                    ) : (
                        <span>Enter balances or details into editable cells</span>
                    )}
                    {draftSaved && (
                        <span data-testid="draft-offline-sync-badge" className="inline-flex items-center gap-1 text-[11px] font-semibold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">
                            💾 Draft saved locally
                        </span>
                    )}
                    {!isOnline && (
                        <span data-testid="draft-offline-mode-badge" className="inline-flex items-center gap-1 text-[11px] font-semibold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">
                            ⚡ Offline Mode
                        </span>
                    )}
                </div>
                <div className="flex items-center gap-2">
                    {Boolean(result) && (
                        <button
                            type="button"
                            data-testid="btn-reveal-ledger-memo"
                            onClick={handleToggleRevealExpectedAnswers}
                            className={`px-3.5 py-2 rounded-xl text-xs font-bold transition shadow-xs cursor-pointer flex items-center gap-1.5 font-sans ${
                                revealedMemo
                                    ? 'bg-amber-600 hover:bg-amber-700 text-white'
                                    : 'bg-white text-[#13519C] border border-[#13519C]/40 hover:bg-blue-50'
                            }`}
                        >
                            <span>{revealedMemo ? '↩ Restore My Entries' : '👁️ Show Model Answer'}</span>
                        </button>
                    )}
                    <button
                        type="button"
                        data-testid="btn-check-answer"
                        onClick={handleCheckSubmission}
                        disabled={isChecking}
                        className="px-5 py-2 rounded-xl text-xs font-bold bg-[#13519C] hover:bg-blue-800 text-white transition shadow-xs cursor-pointer disabled:opacity-50 active:scale-98 font-sans flex items-center gap-1.5"
                    >
                        {isChecking ? (
                            <>
                                <Loader2 className="w-3.5 h-3.5 animate-spin" />
                                <span>Verifying Ledger...</span>
                            </>
                        ) : (
                            <span>Check Table</span>
                        )}
                    </button>
                </div>
            </div>
        </div>
    );
}
