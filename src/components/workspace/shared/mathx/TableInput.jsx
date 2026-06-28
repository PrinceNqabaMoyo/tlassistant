import React from 'react';

/**
 * TableInput — a small editable grid for pattern / sequence table answers.
 *
 * Props:
 *   rows     array of row labels (e.g. ['Position', 'Value'])
 *   columns  array of column count (e.g. 5 for positions 1-5)
 *   values   current cell values { "0,2": "8" }  (rowIndex,colIndex)
 *   onChange ({ row, col, value }) => void
 *   readOnly disable editing
 */
const TableInput = ({ rows = ['n', 'T_n'], columns = 5, values = {}, onChange, readOnly = false }) => {
    const headers = Array.from({ length: columns }, (_, i) => i + 1);

    const handleChange = (rowIdx, colIdx, raw) => {
        if (readOnly || !onChange) return;
        const val = raw.trim();
        onChange({ row: rowIdx, col: colIdx, value: val });
    };

    return (
        <div className="overflow-x-auto">
            <table className="min-w-full text-sm border border-slate-200 rounded-lg overflow-hidden">
                <thead className="bg-slate-50">
                    <tr>
                        <th className="px-3 py-2 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider" />
                        {headers.map((h) => (
                            <th key={h} className="px-3 py-2 text-center text-xs font-semibold text-slate-500 uppercase tracking-wider">
                                {h}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                    {rows.map((label, rIdx) => (
                        <tr key={rIdx} className={rIdx % 2 === 0 ? 'bg-white' : 'bg-slate-50/50'}>
                            <td className="px-3 py-2 font-medium text-slate-700 whitespace-nowrap">{label}</td>
                            {headers.map((_, cIdx) => {
                                const key = `${rIdx},${cIdx}`;
                                const cellValue = values[key] ?? '';
                                return (
                                    <td key={cIdx} className="px-3 py-2">
                                        <input
                                            type="text"
                                            value={cellValue}
                                            onChange={(e) => handleChange(rIdx, cIdx, e.target.value)}
                                            readOnly={readOnly}
                                            className="w-16 px-2 py-1 text-center border border-slate-200 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent disabled:bg-slate-100"
                                        />
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

export default TableInput;
