import React, { useState, useEffect } from 'react';

const DebtorsLedgerInput = ({ initialData, onChange, isSubmitted }) => {
    const [data, setData] = useState(initialData || {
        businessName: '',
        debtorName: '',
        accountNumber: '',
        date: '',
        rows: [
            { date: '', details: '', fol: '', debit: '', credit: '', balance: '' }
        ]
    });

    useEffect(() => {
        if (initialData) {
            setData(initialData);
        }
    }, [initialData]);

    useEffect(() => {
        onChange(data);
    }, [data, onChange]);

    const handleHeaderChange = (field, value) => {
        setData(prev => ({
            ...prev,
            [field]: value
        }));
    };

    const handleCellChange = (rowIndex, field, value) => {
        const newData = { ...data };
        newData.rows[rowIndex][field] = value;
        
        // Calculate balance for this row
        if (field === 'debit' || field === 'credit') {
            newData.rows[rowIndex].balance = calculateBalance(rowIndex);
        }
        
        setData(newData);
    };

    const calculateBalance = (currentRowIndex) => {
        let balance = 0;
        
        for (let i = 0; i <= currentRowIndex; i++) {
            const row = data.rows[i];
            const debit = parseFloat(row.debit) || 0;
            const credit = parseFloat(row.credit) || 0;
            balance += debit - credit;
        }
        
        return balance.toFixed(2);
    };

    const handleAddRow = () => {
        if (!isSubmitted) {
            const newRow = { date: '', details: '', fol: '', debit: '', credit: '', balance: '' };
            setData(prev => ({
                ...prev,
                rows: [...prev.rows, newRow]
            }));
        }
    };

    const handleRemoveRow = (rowIndex) => {
        if (!isSubmitted && data.rows.length > 1) {
            const newRows = data.rows.filter((_, index) => index !== rowIndex);
            setData(prev => ({ ...prev, rows: newRows }));
            
            // Recalculate balances for remaining rows
            newRows.forEach((_, index) => {
                newRows[index].balance = calculateBalance(index);
            });
        }
    };

    const calculateTotals = () => {
        const totalDebit = data.rows.reduce((sum, row) => {
            const debit = parseFloat(row.debit) || 0;
            return sum + debit;
        }, 0);

        const totalCredit = data.rows.reduce((sum, row) => {
            const credit = parseFloat(row.credit) || 0;
            return sum + credit;
        }, 0);

        const finalBalance = totalDebit - totalCredit;

        return { totalDebit, totalCredit, finalBalance };
    };

    const { totalDebit, totalCredit, finalBalance } = calculateTotals();

    return (
        <div className="bg-white rounded-lg shadow-md border border-gray-200 p-6">
            <div className="mb-6">
                <h3 className="text-xl font-bold text-gray-800 mb-4">Debtors Ledger</h3>
                
                {/* Header Fields */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Business Name
                        </label>
                        <input
                            type="text"
                            value={data.businessName}
                            onChange={(e) => handleHeaderChange('businessName', e.target.value)}
                            disabled={isSubmitted}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                            placeholder="Enter business name"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Debtor Name
                        </label>
                        <input
                            type="text"
                            value={data.debtorName}
                            onChange={(e) => handleHeaderChange('debtorName', e.target.value)}
                            disabled={isSubmitted}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                            placeholder="Enter debtor name"
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Account Number
                        </label>
                        <input
                            type="text"
                            value={data.accountNumber}
                            onChange={(e) => handleHeaderChange('accountNumber', e.target.value)}
                            disabled={isSubmitted}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                            placeholder="Enter account number"
                        />
                    </div>
                </div>

                {/* Title */}
                <div className="text-center mb-6">
                    <h2 className="text-2xl font-bold text-gray-800">
                        Debtors Ledger of {data.businessName || '______'}
                    </h2>
                    <p className="text-lg text-gray-600 mt-2">
                        {data.debtorName || '______'} - Account No: {data.accountNumber || '______'}
                    </p>
                </div>

                {/* Table */}
                <div className="overflow-x-auto">
                    <table className="w-full border-collapse border border-gray-300">
                        <thead>
                            <tr className="bg-gray-50">
                                <th className="border border-gray-300 px-3 py-3 text-center font-semibold text-gray-700">
                                    Date
                                </th>
                                <th className="border border-gray-300 px-3 py-3 text-center font-semibold text-gray-700">
                                    Details/Documents no
                                </th>
                                <th className="border border-gray-300 px-2 py-3 text-center font-semibold text-gray-700 w-16">
                                    Fol.
                                </th>
                                <th className="border border-gray-300 px-3 py-3 text-center font-semibold text-gray-700">
                                    Debit (+)
                                </th>
                                <th className="border border-gray-300 px-3 py-3 text-center font-semibold text-gray-700">
                                    Credit (-)
                                </th>
                                <th className="border border-gray-300 px-3 py-3 text-center font-semibold text-gray-700">
                                    Balance
                                </th>
                                {!isSubmitted && (
                                    <th className="border border-gray-300 px-3 py-3 text-center font-semibold text-gray-700">
                                        Actions
                                    </th>
                                )}
                            </tr>
                        </thead>
                        <tbody>
                            {data.rows.map((row, rowIndex) => (
                                <tr key={rowIndex} className="hover:bg-gray-50">
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="text"
                                            value={row.date}
                                            onChange={(e) => handleCellChange(rowIndex, 'date', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="DD/MM/YYYY"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="text"
                                            value={row.details}
                                            onChange={(e) => handleCellChange(rowIndex, 'details', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="Enter details or document number"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-1 py-2 w-16">
                                        <input
                                            type="text"
                                            value={row.fol}
                                            onChange={(e) => handleCellChange(rowIndex, 'fol', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-1 py-1 border-0 text-center focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="1-2"
                                            maxLength="2"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="number"
                                            step="0.01"
                                            value={row.debit}
                                            onChange={(e) => handleCellChange(rowIndex, 'debit', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 text-right focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="0.00"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="number"
                                            step="0.01"
                                            value={row.credit}
                                            onChange={(e) => handleCellChange(rowIndex, 'credit', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 text-right focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="0.00"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="text"
                                            value={row.balance}
                                            disabled={true}
                                            className="w-full px-2 py-1 border-0 text-right bg-gray-50 font-medium"
                                            readOnly
                                        />
                                    </td>
                                    {!isSubmitted && (
                                        <td className="border border-gray-300 px-2 py-2 text-center">
                                            <button
                                                onClick={() => handleRemoveRow(rowIndex)}
                                                disabled={data.rows.length <= 1}
                                                className="text-red-600 hover:text-red-800 disabled:text-gray-400 disabled:cursor-not-allowed text-sm"
                                            >
                                                Remove
                                            </button>
                                        </td>
                                    )}
                                </tr>
                            ))}
                        </tbody>
                        <tfoot>
                            <tr className="bg-gray-100 font-semibold">
                                <td className="border border-gray-300 px-4 py-3 text-center">
                                    Total
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-center">
                                    -
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-center">
                                    -
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-right">
                                    R {totalDebit.toFixed(2)}
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-right">
                                    R {totalCredit.toFixed(2)}
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-right">
                                    R {finalBalance.toFixed(2)}
                                </td>
                                {!isSubmitted && <td className="border border-gray-300 px-4 py-3"></td>}
                            </tr>
                        </tfoot>
                    </table>
                </div>

                {/* Summary */}
                <div className="mt-4 p-3 bg-blue-50 border border-blue-200 rounded-md">
                    <p className="text-sm text-blue-800">
                        <span className="font-semibold">Final Balance:</span> R {finalBalance.toFixed(2)} 
                        {finalBalance > 0 ? ' (Debit Balance - Amount owed by debtor)' : 
                         finalBalance < 0 ? ' (Credit Balance - Amount owed to debtor)' : ' (Balanced)'}
                    </p>
                </div>

                {/* Add Row Button */}
                {!isSubmitted && (
                    <div className="mt-4">
                        <button
                            onClick={handleAddRow}
                            className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors duration-200"
                        >
                            Add Row
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
};

export default DebtorsLedgerInput;
