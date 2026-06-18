import React, { useState, useEffect } from 'react';

const AccountingEquationTableInput = ({ initialData, onChange, isSubmitted }) => {
    const [data, setData] = useState(initialData || {
        businessName: '',
        date: '',
        assets: [{ effect: '', reason: '' }],
        ownersEquity: [{ effect: '', reason: '' }],
        liabilities: [{ effect: '', reason: '' }]
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

    const handleCellChange = (section, rowIndex, field, value) => {
        const newData = { ...data };
        newData[section][rowIndex][field] = value;
        setData(newData);
    };

    const handleAddRow = (section) => {
        if (!isSubmitted) {
            setData(prev => ({
                ...prev,
                [section]: [...prev[section], { effect: '', reason: '' }]
            }));
        }
    };



    const calculateTotals = () => {
        const assetsTotal = data.assets.reduce((sum, row) => {
            const effect = parseFloat(row.effect) || 0;
            return sum + effect;
        }, 0);

        const ownersEquityTotal = data.ownersEquity.reduce((sum, row) => {
            const effect = parseFloat(row.effect) || 0;
            return sum + effect;
        }, 0);

        const liabilitiesTotal = data.liabilities.reduce((sum, row) => {
            const effect = parseFloat(row.effect) || 0;
            return sum + effect;
        }, 0);

        return { assetsTotal, ownersEquityTotal, liabilitiesTotal };
    };

    const { assetsTotal, ownersEquityTotal, liabilitiesTotal } = calculateTotals();
    const isBalanced = Math.abs(assetsTotal - (ownersEquityTotal + liabilitiesTotal)) < 0.01;

    return (
        <div className="bg-white rounded-lg shadow-md border border-gray-200 p-6">
            <div className="mb-6">
                <h3 className="text-xl font-bold text-gray-800 mb-4">Accounting Equation Table</h3>
                
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
                        Accounting Equation of {data.businessName || '______'} on {data.date || '______'}
                    </h2>
                </div>

                {/* Table */}
                <div className="overflow-x-auto">
                    <table className="w-full border-collapse border border-gray-300">
                        <thead>
                            <tr className="bg-gray-50">
                                <th className="border border-gray-300 px-4 py-3 text-center font-semibold text-gray-700 bg-blue-100">
                                    Assets
                                </th>
                                <th className="border border-gray-300 px-4 py-3 text-center font-semibold text-gray-700 bg-green-100">
                                    Owner's Equity
                                </th>
                                <th className="border border-gray-300 px-4 py-3 text-center font-semibold text-gray-700 bg-purple-100">
                                    Liabilities
                                </th>
                            </tr>
                            <tr className="bg-gray-50">
                                <th className="border border-gray-300 px-4 py-2 text-center text-sm font-medium text-gray-700 bg-blue-50">
                                    Effect (R)
                                </th>
                                <th className="border border-gray-300 px-4 py-2 text-center text-sm font-medium text-gray-700 bg-blue-50">
                                    Reason
                                </th>
                                <th className="border border-gray-300 px-4 py-2 text-center text-sm font-medium text-gray-700 bg-green-50">
                                    Effect (R)
                                </th>
                                <th className="border border-gray-300 px-4 py-2 text-center text-sm font-medium text-gray-700 bg-green-50">
                                    Reason
                                </th>
                                <th className="border border-gray-300 px-4 py-2 text-center text-sm font-medium text-gray-700 bg-purple-50">
                                    Effect (R)
                                </th>
                                <th className="border border-gray-300 px-4 py-2 text-center text-sm font-medium text-gray-700 bg-purple-50">
                                    Reason
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            {Array.from({ length: Math.max(data.assets.length, data.ownersEquity.length, data.liabilities.length) }).map((_, rowIndex) => (
                                <tr key={rowIndex} className="hover:bg-gray-50">
                                    {/* Assets Column */}
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="number"
                                            step="0.01"
                                            value={data.assets[rowIndex]?.effect || ''}
                                            onChange={(e) => handleCellChange('assets', rowIndex, 'effect', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 text-right focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="0.00"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="text"
                                            value={data.assets[rowIndex]?.reason || ''}
                                            onChange={(e) => handleCellChange('assets', rowIndex, 'reason', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="Reason for change"
                                        />
                                    </td>
                                    
                                    {/* Owner's Equity Column */}
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="number"
                                            step="0.01"
                                            value={data.ownersEquity[rowIndex]?.effect || ''}
                                            onChange={(e) => handleCellChange('ownersEquity', rowIndex, 'effect', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 text-right focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="0.00"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="text"
                                            value={data.ownersEquity[rowIndex]?.reason || ''}
                                            onChange={(e) => handleCellChange('ownersEquity', rowIndex, 'reason', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="Reason for change"
                                        />
                                    </td>
                                    
                                    {/* Liabilities Column */}
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="number"
                                            step="0.01"
                                            value={data.liabilities[rowIndex]?.effect || ''}
                                            onChange={(e) => handleCellChange('liabilities', rowIndex, 'effect', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 text-right focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="0.00"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-2 py-2">
                                        <input
                                            type="text"
                                            value={data.liabilities[rowIndex]?.reason || ''}
                                            onChange={(e) => handleCellChange('liabilities', rowIndex, 'reason', e.target.value)}
                                            disabled={isSubmitted}
                                            className="w-full px-2 py-1 border-0 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                                            placeholder="Reason for change"
                                        />
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                        <tfoot>
                            <tr className="bg-gray-100 font-semibold">
                                <td className="border border-gray-300 px-4 py-3 text-center bg-blue-50">
                                    Total Assets
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-center bg-blue-50">
                                    R {assetsTotal.toFixed(2)}
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-center bg-green-50">
                                    Total Owner's Equity
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-center bg-green-50">
                                    R {ownersEquityTotal.toFixed(2)}
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-center bg-purple-50">
                                    Total Liabilities
                                </td>
                                <td className="border border-gray-300 px-4 py-3 text-center bg-purple-50">
                                    R {liabilitiesTotal.toFixed(2)}
                                </td>
                            </tr>
                        </tfoot>
                    </table>
                </div>

                {/* Balance Status */}
                <div className={`mt-4 p-3 rounded-md ${isBalanced ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
                    <p className="font-semibold">
                        {isBalanced ? '✓ Accounting Equation is Balanced' : '✗ Accounting Equation is Not Balanced'}
                    </p>
                    <p className="text-sm mt-1">
                        Assets = Owner's Equity + Liabilities
                    </p>
                    <p className="text-sm mt-1">
                        R {assetsTotal.toFixed(2)} = R {ownersEquityTotal.toFixed(2)} + R {liabilitiesTotal.toFixed(2)}
                    </p>
                    <p className="text-sm mt-1">
                        Difference: R {Math.abs(assetsTotal - (ownersEquityTotal + liabilitiesTotal)).toFixed(2)}
                    </p>
                </div>

                {/* Add Row Buttons */}
                {!isSubmitted && (
                    <div className="mt-4 flex flex-wrap gap-2">
                        <button
                            onClick={() => handleAddRow('assets')}
                            className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors duration-200"
                        >
                            Add Assets Row
                        </button>
                        <button
                            onClick={() => handleAddRow('ownersEquity')}
                            className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 transition-colors duration-200"
                        >
                            Add Owner's Equity Row
                        </button>
                        <button
                            onClick={() => handleAddRow('liabilities')}
                            className="bg-purple-600 text-white px-4 py-2 rounded-md hover:bg-purple-700 transition-colors duration-200"
                        >
                            Add Liabilities Row
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
};

export default AccountingEquationTableInput;
