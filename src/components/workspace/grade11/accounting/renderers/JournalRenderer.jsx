import React, { useState } from 'react';
import { buildEmptyJournalAnswer, journalTypeLabel, getExpectedByCellId } from '../utils/accountingHelpers';

const JournalRenderer = ({ question, answer, setAnswer, feedback, isMarkingEnv = false, showMemo = false, showCheckHighlights = false, showHints = false }) => {
    const [activeHelp, setActiveHelp] = useState(null); // { label, text, x, y }

    if (!question || (question.question_type !== 'journal' && question.question_type !== 'ledger')) return null;

    const clampHintPosition = (x, y, width = 250, height = 150) => {
        if (typeof window === 'undefined') return { x, y };
        const margin = 12;
        const maxX = Math.max(margin, window.innerWidth - width - margin);
        const maxY = Math.max(margin, window.innerHeight - height - margin);
        return {
            x: Math.min(Math.max(margin, Number(x) || margin), maxX),
            y: Math.min(Math.max(margin, Number(y) || margin), maxY),
        };
    };

    const ans = (answer && typeof answer === 'object') ? answer : buildEmptyJournalAnswer(question);
    const cells = ans?.cells && typeof ans.cells === 'object' ? ans.cells : {};
    const extraRowsByTable = (ans?.extra_rows_by_table && typeof ans.extra_rows_by_table === 'object') ? ans.extra_rows_by_table : {};

    const journals = Array.isArray(question?.journals)
        ? question.journals
        : (question?.journal ? [question.journal] : []);

    const setCell = (cellId, value) => {
        setAnswer({
            ...ans,
            cells: {
                ...cells,
                [String(cellId)]: value,
            },
        });
    };

    const addRow = (tableIndex, headers, baseRows) => {
        const extraRows = Array.isArray(extraRowsByTable[String(tableIndex)]) ? extraRowsByTable[String(tableIndex)] : [];
        const totalCols = headers.length;
        if (!totalCols) return;
        const newRowIndex = baseRows.length + extraRows.length;
        const newRow = Array.from({ length: totalCols }).map((_, cIdx) => ({
            cell_id: `t${tableIndex}_r${newRowIndex}_c${cIdx}`,
            value: '',
            editable: true,
        }));

        setAnswer({
            ...ans,
            extra_rows_by_table: {
                ...extraRowsByTable,
                [String(tableIndex)]: [...extraRows, newRow],
            },
        });
    };

    const cellHints = question.cell_hints || {};
    const rubricMap = question.rubric_map || {};
    const expectedMap = getExpectedByCellId(question) || {};

    const renderHelpButton = ({ label, text }) => {
        if (isMarkingEnv || !text || text.trim().length === 0) return null;
        if (!showHints) return null; // Respect showHints prop
        const isActive = activeHelp?.label === label;
        return (
            <div className="relative inline-flex items-center ml-1 z-10" style={{ verticalAlign: 'middle' }}>
                <button
                    type="button"
                    onClick={(e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        if (isActive) {
                            setActiveHelp(null);
                        } else {
                            const rect = e.currentTarget.getBoundingClientRect();
                            const pos = clampHintPosition(rect.right + 10, rect.top, 250, 100);
                            setActiveHelp({ label, text, x: pos.x, y: pos.y });
                        }
                    }}
                    className="inline-flex items-center justify-center w-[18px] h-[18px] rounded-full text-[10px] font-bold border border-indigo-300 text-indigo-700 bg-indigo-50 hover:bg-indigo-100 ring-2 ring-transparent transition-all"
                    aria-label={`Info: ${label}`}
                >
                    i
                </button>
            </div>
        );
    };

    const renderFormulaButton = ({ cellId }) => {
        const rubric = rubricMap[cellId];
        if (!rubric || !rubric.formula_structure) return null;
        const isActive = activeHelp?.label === `formula_${cellId}`;
        return (
            <div className="relative inline-flex items-center ml-0.5 z-10" style={{ verticalAlign: 'middle' }}>
                <button
                    type="button"
                    onClick={(e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        if (isActive) {
                            setActiveHelp(null);
                        } else {
                            const rect = e.currentTarget.getBoundingClientRect();
                            const pos = clampHintPosition(rect.right + 10, rect.top, 250, 150);
                            setActiveHelp({ label: `formula_${cellId}`, text: rubric.formula_structure, x: pos.x, y: pos.y, isFormula: true, rubric });
                        }
                    }}
                    className="inline-flex items-center justify-center w-[18px] h-[18px] rounded-full text-[10px] font-bold border border-violet-300 text-violet-700 bg-violet-50 hover:bg-violet-100 ring-2 ring-transparent transition-all"
                    aria-label={`Formula: ${cellId}`}
                    title="View marking formula"
                >
                    ƒ
                </button>
            </div>
        );
    };

    return (
        <div className="space-y-6 pb-24">
            <div>
                {journals.map((j, tIdx) => {
                    const headers = Array.isArray(j?.headers) ? j.headers : [];
                    const titleFields = Array.isArray(j?.title_fields) ? j.title_fields : [];
                    const baseRows = Array.isArray(j?.rows) ? j.rows : [];
                    const allowExtraRows = j?.allow_extra_rows === true;
                    const extraRows = Array.isArray(extraRowsByTable[String(tIdx)]) ? extraRowsByTable[String(tIdx)] : [];
                    const rows = allowExtraRows ? [...baseRows, ...extraRows] : baseRows;
                    const columnHelp = j?.column_help || {};
                    const rowHelp = j?.row_help || {};

                    return (
                        <div key={tIdx} className="mt-3 overflow-visible">
                            <div className="mt-1 mb-2 text-sm font-semibold text-gray-800">{journalTypeLabel(j?.journal_type)}</div>

                            {titleFields.length > 0 && (
                                <div className="mb-3 grid grid-cols-1 md:grid-cols-2 gap-3">
                                    {titleFields.map((tf) => {
                                        const id = tf?.cell_id;
                                        if (!id) return null;
                                        const label = String(tf?.label || id);
                                        const value = cells[String(id)] ?? '';
                                        return (
                                            <label key={id} className="block relative">
                                                <div className="text-xs font-semibold text-gray-700 mb-1 flex items-center">
                                                    {label}
                                                    {renderHelpButton({ label: label, text: cellHints[String(id)] })}
                                                </div>
                                                <input
                                                    value={value}
                                                    onChange={(e) => setCell(id, e.target.value)}
                                                    className="w-full p-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400"
                                                    placeholder=""
                                                />
                                            </label>
                                        );
                                    })}
                                </div>
                            )}

                            {allowExtraRows && (
                                <div style={{ marginBottom: '8px' }}>
                                    <button
                                        type="button"
                                        onClick={() => addRow(tIdx, headers, baseRows)}
                                        style={{ padding: '6px 12px', border: '1px solid #000', background: 'white', cursor: 'pointer', fontWeight: 600 }}
                                    >
                                        + Add row
                                    </button>
                                </div>
                            )}

                            <div className="overflow-visible">
                                <table style={{ width: '100%', borderCollapse: 'collapse', tableLayout: 'fixed' }}>
                                    <thead>
                                        <tr>
                                            {headers.map((h, hIdx) => (
                                                <th key={hIdx} style={{ border: '1px solid #000', padding: '6px', background: '#e5e7eb', fontWeight: 600, textAlign: 'center', fontSize: '0.75rem' }}>
                                                    {h}
                                                    {renderHelpButton({ label: h, text: columnHelp[h] })}
                                                </th>
                                            ))}
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {rows.map((row, rIdx) => (
                                            <tr key={rIdx}>
                                                {(Array.isArray(row) ? row : []).map((cell, cIdx) => {
                                                    const cellId = cell?.cell_id || `t${tIdx}_r${rIdx}_c${cIdx}`;
                                                    const value = cells[String(cellId)] ?? (cell?.value || '');
                                                    const editable = Boolean(cell?.editable);
                                                    const displayValue = (!editable && String(value || '').trim() === '') ? 'N/A' : value;

                                                    // row help often applies to the first cell of a row
                                                    const rowHelpText = cIdx === 0 ? rowHelp[String(rIdx)] || rowHelp[displayValue] : null;
                                                    const hintText = cellHints[cellId] || rowHelpText;

                                                    return (
                                                        <td key={cIdx} style={{ border: '1px solid #000', padding: 0, verticalAlign: 'top', position: 'relative' }}>
                                                            {editable ? (
                                                                <div className="flex w-full items-center">
                                                                    <input
                                                                        value={showMemo ? (Array.isArray(expectedMap[cellId]) ? expectedMap[cellId].join(' / ') : (expectedMap[cellId] ?? '')) : value}
                                                                        onChange={(e) => { if (!showMemo) setCell(cellId, e.target.value); }}
                                                                        style={{ 
                                                                            flexGrow: 1, padding: '6px', border: 'none', outline: 'none', boxSizing: 'border-box', textAlign: 'center', fontSize: '0.875rem',
                                                                            backgroundColor: showMemo ? '#f0fdf4' : 'transparent', color: showMemo ? '#065f46' : 'inherit', fontWeight: showMemo ? '600' : 'normal'
                                                                        }}
                                                                        placeholder=""
                                                                        readOnly={showMemo}
                                                                    />
                                                                    {hintText && <div className="pr-1">{renderHelpButton({ label: `Cell Help`, text: hintText })}</div>}
                                                                    {rubricMap[cellId] && <div className="pr-1">{renderFormulaButton({ cellId })}</div>}
                                                                </div>
                                                            ) : (
                                                                <div style={{ padding: '6px', minHeight: '2.25rem', display: 'flex', alignItems: 'center', justifyContent: (hintText && cIdx !== 0) ? 'space-between' : 'flex-start', fontSize: '0.875rem', color: displayValue === 'N/A' ? '#9ca3af' : '#1f2937', fontStyle: displayValue === 'N/A' ? 'italic' : 'normal' }}>
                                                                    <span>{displayValue}</span>
                                                                    {hintText && renderHelpButton({ label: displayValue !== 'N/A' ? displayValue : 'Row Info', text: hintText })}
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
                        </div>
                    );
                })}
            </div>

            {feedback && (
                <div className={`mt-3 p-3 rounded-lg text-sm ${feedback.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' :
                    feedback.kind === 'error' ? 'bg-red-50 text-red-800 border border-red-200' :
                        'bg-blue-50 text-blue-800 border border-blue-200'
                    }`}>
                    {feedback.message}
                </div>
            )}

            {activeHelp && (
                <div 
                    className={`fixed z-[100] w-64 p-3 rounded-xl shadow-xl text-[12px] text-gray-800 text-left normal-case break-words font-normal ${activeHelp.isFormula ? 'border border-violet-200 bg-violet-50' : 'border border-indigo-200 bg-white'}`}
                    style={{ left: activeHelp.x, top: activeHelp.y }}
                >
                    <div className={`flex items-start justify-between gap-2 mb-2 border-b pb-2 ${activeHelp.isFormula ? 'border-violet-200' : 'border-gray-100'}`}>
                        <div className={`font-bold leading-tight ${activeHelp.isFormula ? 'text-violet-900' : 'text-indigo-900'}`}>
                            {activeHelp.isFormula ? 'Marking Formula' : activeHelp.label}
                        </div>
                        <button
                            type="button"
                            onClick={() => setActiveHelp(null)}
                            className="text-gray-400 hover:text-gray-700 p-0.5 leading-none bg-white rounded-full w-5 h-5 flex items-center justify-center hover:bg-gray-100"
                        >
                            ✕
                        </button>
                    </div>
                    {activeHelp.isFormula ? (
                        <div className="leading-relaxed space-y-1.5">
                            <div className="font-semibold text-violet-800">{activeHelp.text}</div>
                            {Array.isArray(activeHelp.rubric?.foundational_values) && activeHelp.rubric.foundational_values.length > 0 && (
                                <div className="text-gray-600">
                                    <span className="font-medium">Values:</span>{' '}
                                    {activeHelp.rubric.foundational_values.map((v) =>
                                        typeof v === 'number' ? v.toLocaleString('en-ZA') : String(v)
                                    ).join(', ')}
                                </div>
                            )}
                            {Array.isArray(activeHelp.rubric?.operations) && activeHelp.rubric.operations.length > 0 && (
                                <div className="text-gray-600">
                                    <span className="font-medium">Operations:</span> {activeHelp.rubric.operations.join(' ')}
                                </div>
                            )}
                            {activeHelp.rubric?.max_score != null && (
                                <div className="mt-1.5 text-violet-700 font-semibold bg-violet-100/50 p-1.5 rounded-lg inline-block">
                                    Max: {activeHelp.rubric.max_score} {activeHelp.rubric.max_score === 1 ? 'mark' : 'marks'}
                                </div>
                            )}
                        </div>
                    ) : (
                        <div className="leading-relaxed">{activeHelp.text}</div>
                    )}
                </div>
            )}
        </div>
    );
};

export default JournalRenderer;
