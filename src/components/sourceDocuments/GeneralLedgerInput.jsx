import React, { useState, useEffect } from 'react';
import { MoneyInput } from '../forms/TableComponents';

const GeneralLedgerInput = ({ initialData, onChange, isSubmitted }) => {
    const [ledgerData, setLedgerData] = useState(initialData || {
        ledgerTitle: '',
        companyName: '',
        month: '',
        tables: [{
            title: '',
            rows: [{
                date: '',
                details: '',
                fol: '',
                debit: { main: '', cents: '' },
                credit: { main: '', cents: '' },
                balance: { main: '', cents: '' },
                balanceType: 'debit' // 'debit' or 'credit'
            }]
        }]
    });

    useEffect(() => {
        onChange(ledgerData);
    }, [ledgerData, onChange]);

    const handleHeaderChange = (field, value) => {
        if (isSubmitted) return;
        setLedgerData(prev => ({ ...prev, [field]: value }));
    };

    const handleCellChange = (tableIndex, rowIndex, field, value) => {
        if (isSubmitted) return;
        setLedgerData(prev => {
            const newData = { ...prev };
            newData.tables[tableIndex].rows[rowIndex][field] = value;
            
            // Recalculate balance for this row
            newData.tables[tableIndex].rows[rowIndex] = calculateRowBalance(
                newData.tables[tableIndex].rows[rowIndex],
                rowIndex > 0 ? newData.tables[tableIndex].rows[rowIndex - 1] : null
            );
            
            return newData;
        });
    };

    const calculateRowBalance = (currentRow, previousRow) => {
        const currentDebit = parseFloat(currentRow.debit.main || 0) + parseFloat(currentRow.debit.cents || 0) / 100;
        const currentCredit = parseFloat(currentRow.credit.main || 0) + parseFloat(currentRow.credit.cents || 0) / 100;
        
        let previousBalance = 0;
        if (previousRow) {
            previousBalance = parseFloat(previousRow.balance.main || 0) + parseFloat(previousRow.balance.cents || 0) / 100;
        }
        
        const newBalance = previousBalance + currentDebit - currentCredit;
        const balanceType = newBalance >= 0 ? 'debit' : 'credit';
        const absBalance = Math.abs(newBalance);
        
        return {
            ...currentRow,
            balance: {
                main: Math.floor(absBalance).toString(),
                cents: Math.round((absBalance % 1) * 100).toString().padStart(2, '0')
            },
            balanceType
        };
    };

    const handleAddRow = (tableIndex) => {
        if (isSubmitted) return;
        setLedgerData(prev => {
            const newData = { ...prev };
            const newRow = {
                date: '',
                details: '',
                fol: '',
                debit: { main: '', cents: '' },
                credit: { main: '', cents: '' },
                balance: { main: '', cents: '' },
                balanceType: 'debit'
            };
            
            // Calculate balance for new row
            const table = newData.tables[tableIndex];
            if (table.rows.length > 0) {
                const lastRow = table.rows[table.rows.length - 1];
                newRow.balance = { ...lastRow.balance };
                newRow.balanceType = lastRow.balanceType;
            }
            
            newData.tables[tableIndex].rows.push(newRow);
            return newData;
        });
    };

    const handleRemoveRow = (tableIndex, rowIndex) => {
        if (isSubmitted) return;
        setLedgerData(prev => {
            const newData = { ...prev };
            newData.tables[tableIndex].rows.splice(rowIndex, 1);
            
            // Recalculate balances for remaining rows
            for (let i = 0; i < newData.tables[tableIndex].rows.length; i++) {
                newData.tables[tableIndex].rows[i] = calculateRowBalance(
                    newData.tables[tableIndex].rows[i],
                    i > 0 ? newData.tables[tableIndex].rows[i - 1] : null
                );
            }
            
            return newData;
        });
    };

    const calculateTotals = (tableIndex) => {
        const table = ledgerData.tables[tableIndex];
        let totalDebit = 0;
        let totalCredit = 0;
        
        table.rows.forEach(row => {
            totalDebit += parseFloat(row.debit.main || 0) + parseFloat(row.debit.cents || 0) / 100;
            totalCredit += parseFloat(row.credit.main || 0) + parseFloat(row.credit.cents || 0) / 100;
        });
        
        return { totalDebit, totalCredit };
    };

    const removeTable = (tableIndex) => {
        if (isSubmitted || ledgerData.tables.length <= 1) return;
        setLedgerData(prev => ({
            ...prev,
            tables: prev.tables.filter((_, index) => index !== tableIndex)
        }));
    };

    return (
        <div className="p-4 my-4 bg-gray-50 border border-gray-300 rounded-lg">
            {/* Main Ledger Title */}
            <div className="mb-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
                <div className="mb-3">
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        General Ledger Title
                    </label>
                    <input
                        type="text"
                        value={ledgerData.ledgerTitle}
                        onChange={(e) => handleHeaderChange('ledgerTitle', e.target.value)}
                        disabled={isSubmitted}
                        className="w-full p-2 text-xl font-bold border border-gray-300 rounded-md"
                        placeholder="Enter general ledger title"
                    />
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Company Name
                        </label>
                        <input
                            type="text"
                            value={ledgerData.companyName}
                            onChange={(e) => handleHeaderChange('companyName', e.target.value)}
                            disabled={isSubmitted}
                            className="w-full p-2 border border-gray-300 rounded-md"
                            placeholder="Enter company name"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Month
                        </label>
                        <input
                            type="text"
                            value={ledgerData.month}
                            onChange={(e) => handleHeaderChange('month', e.target.value)}
                            disabled={isSubmitted}
                            className="w-full p-2 border border-gray-300 rounded-md"
                            placeholder="Enter month"
                        />
                    </div>
                </div>
            </div>

            {/* Tables Section */}
            {ledgerData.tables.map((table, tableIndex) => (
                <div key={tableIndex} className="mb-6 p-4 bg-white border border-gray-300 rounded-lg">
                    {/* Table Header with Title and Remove Button */}
                    <div className="mb-3 flex justify-between items-center">
                        <input
                            type="text"
                            value={table.title}
                            onChange={(e) => {
                                setLedgerData(prev => {
                                    const newData = { ...prev };
                                    newData.tables[tableIndex].title = e.target.value;
                                    return newData;
                                });
                            }}
                            disabled={isSubmitted}
                            className="flex-1 p-2 text-lg font-semibold border border-gray-300 rounded-md mr-3"
                            placeholder="Enter table title (e.g., Cash Account, Accounts Receivable)"
                        />
                        {ledgerData.tables.length > 1 && (
                            <button
                                onClick={() => removeTable(tableIndex)}
                                disabled={isSubmitted}
                                className="px-3 py-2 bg-red-500 text-white rounded hover:bg-red-600 disabled:bg-gray-300"
                                title="Remove this table"
                            >
                                Remove Table
                            </button>
                        )}
                    </div>

                    {/* Table */}
                    <div className="overflow-x-auto">
                        <table className="min-w-full border-2 border-gray-800">
                            <thead className="bg-gray-200">
                                <tr className="border-b-2 border-gray-800">
                                    <th className="p-2 border-r-2 border-gray-800">Date</th>
                                    <th className="p-2 border-r-2 border-gray-800">Details</th>
                                    <th className="p-2 border-r-2 border-gray-800">Fol.</th>
                                    <th className="p-2 border-r-2 border-gray-800">Debit</th>
                                    <th className="p-2 border-r-2 border-gray-800">Credit</th>
                                    <th className="p-2 border-r-2 border-gray-800">Balance</th>
                                </tr>
                            </thead>
                            <tbody>
                                {table.rows.map((row, rowIndex) => (
                                    <tr key={rowIndex} className="border-b border-gray-400">
                                        <td className="p-2 border-r border-gray-400">
                                            <input
                                                type="text"
                                                value={row.date}
                                                onChange={(e) => handleCellChange(tableIndex, rowIndex, 'date', e.target.value)}
                                                disabled={isSubmitted}
                                                className="w-full p-1 border border-gray-300 rounded"
                                                placeholder="Date"
                                            />
                                        </td>
                                        <td className="p-2 border-r border-gray-400">
                                            <input
                                                type="text"
                                                value={row.details}
                                                onChange={(e) => handleCellChange(tableIndex, rowIndex, 'details', e.target.value)}
                                                disabled={isSubmitted}
                                                className="w-full p-1 border border-gray-300 rounded"
                                                placeholder="Details"
                                            />
                                        </td>
                                        <td className="p-2 border-r border-gray-400">
                                            <input
                                                type="text"
                                                value={row.fol}
                                                onChange={(e) => handleCellChange(tableIndex, rowIndex, 'fol', e.target.value)}
                                                disabled={isSubmitted}
                                                className="w-full p-1 border border-gray-300 rounded"
                                                placeholder="Fol."
                                            />
                                        </td>
                                        <td className="p-2 border-r border-gray-400">
                                            <MoneyInput
                                                value={row.debit}
                                                onChange={(value) => handleCellChange(tableIndex, rowIndex, 'debit', value)}
                                                isSubmitted={isSubmitted}
                                            />
                                        </td>
                                        <td className="p-2 border-r border-gray-400">
                                            <MoneyInput
                                                value={row.credit}
                                                onChange={(value) => handleCellChange(tableIndex, rowIndex, 'credit', value)}
                                                isSubmitted={isSubmitted}
                                            />
                                        </td>
                                        <td className="p-2">
                                            <div className="flex items-center space-x-1">
                                                <span className="text-sm text-gray-600 mr-1">
                                                    {row.balanceType === 'debit' ? 'Dr' : 'Cr'}
                                                </span>
                                                <span className="font-mono">
                                                    {row.balance.main}.{row.balance.cents}
                                                </span>
                                            </div>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>

                    {/* Table Totals */}
                    <div className="mt-3 p-3 bg-gray-100 rounded-lg">
                        <div className="flex justify-between items-center">
                            <div className="text-sm text-gray-600">
                                <span className="font-semibold">Total Debit:</span> R{calculateTotals(tableIndex).totalDebit.toFixed(2)}
                                <span className="ml-4 font-semibold">Total Credit:</span> R{calculateTotals(tableIndex).totalCredit.toFixed(2)}
                            </div>
                            <button
                                onClick={() => handleRemoveRow(tableIndex, table.rows.length - 1)}
                                disabled={isSubmitted || table.rows.length <= 1}
                                className="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600 disabled:bg-gray-300"
                            >
                                Remove Row
                            </button>
                        </div>
                    </div>

                    {/* Add Row Button */}
                    <div className="mt-2">
                        <button
                            onClick={() => handleAddRow(tableIndex)}
                            disabled={isSubmitted}
                            className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 disabled:bg-gray-300"
                        >
                            Add Row
                        </button>
                    </div>
                </div>
            ))}

            {/* Add New Table Button */}
            <div className="mt-4">
                <button
                    onClick={() => {
                        setLedgerData(prev => ({
                            ...prev,
                            tables: [...prev.tables, {
                                title: '',
                                rows: [{
                                    date: '',
                                    details: '',
                                    fol: '',
                                    debit: { main: '', cents: '' },
                                    credit: { main: '', cents: '' },
                                    balance: { main: '', cents: '' },
                                    balanceType: 'debit'
                                }]
                            }]
                        }));
                    }}
                    disabled={isSubmitted}
                    className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 font-semibold disabled:bg-gray-300"
                >
                    Add New Table
                </button>
            </div>
        </div>
    );
};

export default GeneralLedgerInput;
