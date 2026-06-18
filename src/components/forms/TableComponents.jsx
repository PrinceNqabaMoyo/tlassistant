import React, { useState, useEffect } from 'react';

// Table Renderer Component
export const TableRenderer = ({ table }) => {
    if (!table || !table.headers || !table.rows) {
        return <p className="text-sm text-gray-500">No table data to display.</p>;
    }

    return (
        <div className="my-4 overflow-x-auto">
            <table style={{ width: '100%', borderCollapse: 'collapse', tableLayout: 'fixed' }}>
                <thead>
                    <tr>
                        {table.headers.map((header, index) => (
                            <th key={index} style={{ border: '1px solid #000', padding: '6px', background: '#e5e7eb', fontWeight: 600, textAlign: 'center', fontSize: '0.875rem' }}>{header}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {table.rows.map((row, rowIndex) => (
                        <tr key={rowIndex}>
                            {row.map((cell, cellIndex) => (
                                <td key={cellIndex} style={{ border: '1px solid #000', padding: '6px', fontSize: '0.875rem', textAlign: 'center' }}>{cell}</td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

// Table Input Component
export const TableInput = ({ initialData, onChange, isSubmitted }) => {
    const [tableData, setTableData] = useState(initialData || { headers: [''], rows: [['']] });

    useEffect(() => {
        onChange(tableData);
    }, [tableData, onChange]);

    const handleCellChange = (rowIndex, cellIndex, value) => {
        if (isSubmitted) return;
        const newRows = [...tableData.rows];
        newRows[rowIndex][cellIndex] = value;
        setTableData({ ...tableData, rows: newRows });
    };

    const handleAddRow = () => {
        if (isSubmitted) return;
        const newRow = new Array(tableData.headers.length).fill('');
        setTableData({ ...tableData, rows: [...tableData.rows, newRow] });
    };

    const handleRemoveRow = (rowIndex) => {
        if (isSubmitted || tableData.rows.length <= 1) return;
        const newRows = tableData.rows.filter((_, index) => index !== rowIndex);
        setTableData({ ...tableData, rows: newRows });
    };

    return (
        <div className="mt-4">
            <p style={{ fontWeight: 600, marginBottom: '8px', color: '#374151' }}>Input your answer in the table:</p>
            <div className="overflow-x-auto">
                <table style={{ width: '100%', borderCollapse: 'collapse', tableLayout: 'fixed' }}>
                    <thead>
                        <tr>
                            {tableData.headers.map((header, index) => (
                                <th key={index} style={{ border: '1px solid #000', padding: '6px', background: '#e5e7eb', fontWeight: 600, textAlign: 'center', fontSize: '0.75rem', textTransform: 'uppercase', letterSpacing: '0.05em' }}>{header}</th>
                            ))}
                            {!isSubmitted && <th style={{ border: '1px solid #000', padding: '6px', background: '#e5e7eb', width: '40px' }}></th>}
                        </tr>
                    </thead>
                    <tbody>
                        {tableData.rows.map((row, rowIndex) => (
                            <tr key={rowIndex}>
                                {row.map((cell, cellIndex) => (
                                    <td key={cellIndex} style={{ border: '1px solid #000', padding: 0 }}>
                                        <input
                                            type="text"
                                            value={cell}
                                            onChange={(e) => handleCellChange(rowIndex, cellIndex, e.target.value)}
                                            disabled={isSubmitted}
                                            style={{ width: '100%', padding: '6px', border: 'none', outline: 'none', boxSizing: 'border-box', textAlign: 'center', fontSize: '0.875rem' }}
                                        />
                                    </td>
                                ))}
                                {!isSubmitted && (
                                    <td style={{ border: '1px solid #000', padding: 0 }}>
                                        <button onClick={() => handleRemoveRow(rowIndex)} disabled={tableData.rows.length <= 1} style={{ width: '100%', height: '100%', border: 'none', background: '#f3f4f6', cursor: 'pointer', fontWeight: 'bold', fontSize: '1rem', padding: '6px' }}>&times;</button>
                                    </td>
                                )}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            {!isSubmitted && (
                <div style={{ marginTop: '8px' }}>
                    <button onClick={handleAddRow} style={{ padding: '6px 12px', border: '1px solid #000', background: 'white', cursor: 'pointer', fontWeight: 600 }}>
                        + Add Row
                    </button>
                </div>
            )}
        </div>
    );
};

// Money Input Component
export const MoneyInput = ({ value = { main: '', cents: '' }, onChange, isSubmitted }) => {
    const handleMainChange = (e) => {
        if (/^\d*$/.test(e.target.value)) {
            onChange({ ...value, main: e.target.value });
        }
    };

    const handleCentsChange = (e) => {
        if (/^\d{0,2}$/.test(e.target.value)) {
            onChange({ ...value, cents: e.target.value });
        }
    };

    return (
        <div style={{ display: 'flex', alignItems: 'center', width: '100%' }}>
            <input
                type="text"
                value={value.main}
                onChange={handleMainChange}
                disabled={isSubmitted}
                style={{ flex: 1, padding: '6px', border: 'none', outline: 'none', boxSizing: 'border-box', fontFamily: 'ui-monospace, monospace', textAlign: 'right', fontSize: '0.875rem' }}
                placeholder="0"
            />
            <span style={{ padding: '0 2px', color: '#6b7280' }}>.</span>
            <input
                type="text"
                value={value.cents}
                onChange={handleCentsChange}
                disabled={isSubmitted}
                style={{ width: '3rem', padding: '6px', border: 'none', outline: 'none', boxSizing: 'border-box', fontFamily: 'ui-monospace, monospace', fontSize: '0.875rem' }}
                placeholder="00"
                maxLength="2"
            />
        </div>
    );
};
