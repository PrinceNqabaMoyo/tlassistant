import React, { useState } from 'react';

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

    const [cellValues, setCellValues] = useState({});
    const columns = question.columns || question.table_schema?.columns || ['Date', 'Details', 'Fol', 'Debit', 'Credit'];
    const rows = question.rows || question.table_schema?.rows || 5;

    const handleCellChange = (rowIdx, colIdx, val) => {
        setCellValues(prev => ({
            ...prev,
            [`${rowIdx}_${colIdx}`]: val
        }));
    };

    const handleCheckSubmission = () => {
        if (onCheck) {
            onCheck({ cells: cellValues });
        }
    };

    return (
        <div className="space-y-6">
            {/* Dynamic Ledger Scaffold Guidance */}
            <div className="rounded-2xl border border-blue-200 bg-blue-50/60 p-4 transition-all">
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                        <span className="grid place-items-center h-6 w-6 rounded-lg bg-brand-blue text-white text-xs font-bold">
                            📖
                        </span>
                        <span className="text-sm font-bold text-brand-blue">
                            Accounting Equation &amp; Rules
                        </span>
                    </div>
                    <button
                        type="button"
                        onClick={onToggleScaffold}
                        className="text-xs font-bold text-brand-blue hover:underline cursor-pointer"
                    >
                        {showDynamicScaffold ? 'Hide Rules ▲' : 'Show Transaction Rules ▼'}
                    </button>
                </div>

                {showDynamicScaffold && (
                    <div className="mt-3 pt-3 border-t border-blue-100 text-xs text-slate-700 space-y-1">
                        <p className="font-semibold text-slate-800">Double Entry Reminder:</p>
                        <p>• Assets &amp; Expenses increase on the <strong>Debit</strong> side.</p>
                        <p>• Liabilities, Equity, and Income increase on the <strong>Credit</strong> side.</p>
                        <p>• Bank Gross includes 15% VAT: \(\text{VAT} = \text{Gross} \times \frac{15}{115}\).</p>
                    </div>
                )}
            </div>

            {/* 2D Tabular Grid */}
            <div className="overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-2xs">
                <table className="w-full text-left border-collapse text-xs">
                    <thead>
                        <tr className="bg-slate-100 border-b border-slate-200 text-slate-700 font-bold">
                            {columns.map((col, idx) => (
                                <th key={idx} className="p-3 border-r border-slate-200 last:border-r-0">
                                    {typeof col === 'string' ? col : col.title || col.label}
                                </th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {Array.from({ length: typeof rows === 'number' ? rows : rows.length }).map((_, rIdx) => (
                            <tr key={rIdx} className="border-b border-slate-100 hover:bg-slate-50/50">
                                {columns.map((_, cIdx) => {
                                    const key = `${rIdx}_${cIdx}`;
                                    const val = cellValues[key] || '';
                                    return (
                                        <td key={cIdx} className="p-1.5 border-r border-slate-100 last:border-r-0">
                                            <input
                                                type="text"
                                                value={val}
                                                onChange={(e) => handleCellChange(rIdx, cIdx, e.target.value)}
                                                className="w-full px-2 py-1.5 rounded-lg border border-slate-200 focus:border-brand-blue focus:ring-1 focus:ring-brand-blue outline-none text-xs"
                                                placeholder="..."
                                            />
                                        </td>
                                    );
                                })}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <div className="flex justify-end">
                <button
                    type="button"
                    onClick={handleCheckSubmission}
                    disabled={isChecking}
                    className="px-5 py-2.5 rounded-xl text-sm font-semibold bg-brand-blue text-white hover:bg-brand-cobalt transition shadow-xs cursor-pointer"
                >
                    {isChecking ? 'Verifying...' : 'Check Table'}
                </button>
            </div>
        </div>
    );
}
