import React, { useState, useEffect } from 'react';

const TrialBalanceInput = ({ initialData, onChange, isSubmitted }) => {
    const [data, setData] = useState(initialData || {
        businessName: '',
        date: '',
        accounts: [
            { account: '', debit: '', credit: '' }
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
        newData.accounts[rowIndex][field] = value;
        setData(newData);
    };

    const handleAddRow = () => {
        if (!isSubmitted) {
            setData(prev => ({
                ...prev,
                accounts: [...prev.accounts, { account: '', debit: '', credit: '' }]
            }));
        }
    };

    const handleRemoveRow = (rowIndex) => {
        if (!isSubmitted && data.accounts.length > 1) {
            setData(prev => ({
                ...prev,
                accounts: prev.accounts.filter((_, index) => index !== rowIndex)
            }));
        }
    };

    const calculateTotals = () => {
        const totalDebit = data.accounts.reduce((sum, row) => {
            const debit = parseFloat(row.debit) || 0;
            return sum + debit;
        }, 0);

        const totalCredit = data.accounts.reduce((sum, row) => {
            const credit = parseFloat(row.credit) || 0;
            return sum + credit;
        }, 0);

        return { totalDebit, totalCredit };
    };

    const { totalDebit, totalCredit } = calculateTotals();
    const isBalanced = Math.abs(totalDebit - totalCredit) < 0.01;

    return (
        <div className="bg-white rounded-lg shadow-md border border-gray-200 p-6">
            <div className="mb-6">
                <h3 className="text-xl font-bold text-gray-800 mb-4">Trial Balance</h3>
                
                {/* Header Fields */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
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
                            Date
                        </label>
                        <input
                            type="text"
                            value={data.date}
                            onChange={(e) => handleHeaderChange('date', e.target.value)}
                            disabled={isSubmitted}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                            placeholder="Enter date (e.g., 31 December 2024)"
                        />
                    </div>
                </div>

                {/* Title */}
                <div className="text-center mb-6">
                    <h2 className="text-2xl font-bold text-gray-800">
                        Trial Balance of {data.businessName || '______'} on {data.date || '______'}
                    </h2>
                </div>

                {/* Table */}
                <div className="overflow-x-auto">
                    <table className="w-full border-collapse border border-gray-300">
                        <thead>
                            <tr className="bg-gray-50">
                                <th className="border border-gray-300 px-4 py-3 text-left font-semibold text-gray-700">
                                    Account
                                </th>
                                <th className="border border-gray-300 px-4 py-3 text-right font-semibold text-gray-700">
                                    Debit (R)
                                </th>
                                <th className="border border-gray-300 px-4 py-3 text-right font-semibold text-gray-700">
                                    Credit (R)
                                </th>
                                {!isSubmitted && (
                                    <th className="border border-gray-300 px-4 py-3 text-center font-semibold text-gray-700">
                                        Actions
                                    </th>
                                )}
                            </tr>
                        </thead>
                        <tbody>
                            {data.accounts.map((row, index) => (
                                <tr key={index} className="hover:bg-gray-50">
                                    <td className="border border-gray-300 px-4 py-3">
                                        <input
                                            type="text"
                                            value={row.account}
                                            onChange={(e) => handleCellChange(index, 'account', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="Account name"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-4 py-3">
                                        <input
                                            type="number"
                                            step="0.01"
                                            value={row.debit}
                                            onChange={(e) => handleCellChange(index, 'debit', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 text-right focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="0.00"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-4 py-3">
                                        <input
                                            type="number"
                                            step="0.01"
                                            value={row.credit}
                                            onChange={(e) => handleCellChange(index, 'credit', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 text-right focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="0.00"
                                        />
                                    </td>
                                    {!isSubmitted && (
                                        <td className="border border-gray-300 px-4 py-3 text-center">
                                            <button
                                                onClick={() => handleRemoveRow(index)}
                                                disabled={data.accounts.length <= 1}
                                                className="text-red-600 hover:text-red-800 disabled:text-gray-400 disabled:cursor-not-allowed"
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
                                <td className="border border-gray-300 px-4 py-3 text-left">
                                    Total
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-right">
                                    R {totalDebit.toFixed(2)}
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-right">
                                    R {totalCredit.toFixed(2)}
                                </td>
                                {!isSubmitted && <td className="border border-gray-300 px-4 py-3"></td>}
                            </tr>
                        </tfoot>
                    </table>
                </div>

                {/* Balance Status */}
                <div className={`mt-4 p-3 rounded-md ${isBalanced ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                    <p className="font-semibold">
                        {isBalanced ? '✓ Trial Balance is Balanced' : '✗ Trial Balance is Not Balanced'}
                    </p>
                    <p className="text-sm mt-1">
                        Difference: R {Math.abs(totalDebit - totalCredit).toFixed(2)}
                    </p>
                </div>

                {/* Add Row Button */}
                {!isSubmitted && (
                    <div className="mt-4">
                        <button
                            onClick={handleAddRow}
                            className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors duration-200"
                        >
                            Add Account
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
};

export default TrialBalanceInput;
