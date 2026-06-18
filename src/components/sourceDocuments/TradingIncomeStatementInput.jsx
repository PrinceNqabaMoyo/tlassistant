import React, { useState, useEffect } from 'react';
import { MoneyInput } from '../forms/TableComponents';

const TradingIncomeStatementInput = ({ initialData, onChange, isSubmitted }) => {
    const [incomeStatementData, setIncomeStatementData] = useState(initialData || {
        ownerName: '',
        businessName: '',
        yearEnded: '',
        sales: { main: '', cents: '' },
        costOfSales: { main: '', cents: '' },
        otherOperatingIncome: [
            { description: '', amount: { main: '', cents: '' } },
            { description: '', amount: { main: '', cents: '' } },
            { description: '', amount: { main: '', cents: '' } }
        ],
        operatingExpenses: [
            { description: '', amount: { main: '', cents: '' } },
            { description: '', amount: { main: '', cents: '' } },
            { description: '', amount: { main: '', cents: '' } }
        ],
        interestIncome: { main: '', cents: '' },
        interestExpense: { main: '', cents: '' }
    });

    useEffect(() => {
        onChange(incomeStatementData);
    }, [incomeStatementData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setIncomeStatementData(prev => ({ ...prev, [field]: value }));
    };

    const handleMoneyChange = (field, value) => {
        if (isSubmitted) return;
        setIncomeStatementData(prev => ({ ...prev, [field]: value }));
    };

    const handleOtherIncomeChange = (index, field, value) => {
        if (isSubmitted) return;
        const updatedOtherIncome = [...incomeStatementData.otherOperatingIncome];
        updatedOtherIncome[index] = { ...updatedOtherIncome[index], [field]: value };
        setIncomeStatementData(prev => ({ ...prev, otherOperatingIncome: updatedOtherIncome }));
    };

    const handleExpenseChange = (index, field, value) => {
        if (isSubmitted) return;
        const updatedExpenses = [...incomeStatementData.operatingExpenses];
        updatedExpenses[index] = { ...updatedExpenses[index], [field]: value };
        setIncomeStatementData(prev => ({ ...prev, operatingExpenses: updatedExpenses }));
    };

    const addOtherIncome = () => {
        if (isSubmitted) return;
        const newIncome = { description: '', amount: { main: '', cents: '' } };
        setIncomeStatementData(prev => ({
            ...prev,
            otherOperatingIncome: [...prev.otherOperatingIncome, newIncome]
        }));
    };

    const removeOtherIncome = (index) => {
        if (isSubmitted) return;
        const updatedOtherIncome = incomeStatementData.otherOperatingIncome.filter((_, i) => i !== index);
        setIncomeStatementData(prev => ({ ...prev, otherOperatingIncome: updatedOtherIncome }));
    };

    const addExpense = () => {
        if (isSubmitted) return;
        const newExpense = { description: '', amount: { main: '', cents: '' } };
        setIncomeStatementData(prev => ({
            ...prev,
            operatingExpenses: [...prev.operatingExpenses, newExpense]
        }));
    };

    const removeExpense = (index) => {
        if (isSubmitted) return;
        const updatedExpenses = incomeStatementData.operatingExpenses.filter((_, i) => i !== index);
        setIncomeStatementData(prev => ({ ...prev, operatingExpenses: updatedExpenses }));
    };

    // Calculate totals
    const calculateGrossProfit = () => {
        const sales = parseFloat(incomeStatementData.sales?.main || 0) + 
                     parseFloat(incomeStatementData.sales?.cents || 0) / 100;
        const costOfSales = parseFloat(incomeStatementData.costOfSales?.main || 0) + 
                           parseFloat(incomeStatementData.costOfSales?.cents || 0) / 100;
        return sales - costOfSales;
    };

    const calculateTotalOtherIncome = () => {
        return incomeStatementData.otherOperatingIncome.reduce((sum, item) => {
            const amount = parseFloat(item.amount?.main || 0) + parseFloat(item.amount?.cents || 0) / 100;
            return sum + amount;
        }, 0);
    };

    const calculateGrossOperatingIncome = () => {
        const grossProfit = calculateGrossProfit();
        const otherIncome = calculateTotalOtherIncome();
        return grossProfit + otherIncome;
    };

    const calculateTotalExpenses = () => {
        return incomeStatementData.operatingExpenses.reduce((sum, item) => {
            const amount = parseFloat(item.amount?.main || 0) + parseFloat(item.amount?.cents || 0) / 100;
            return sum + amount;
        }, 0);
    };

    const calculateOperatingProfit = () => {
        return calculateGrossOperatingIncome() - calculateTotalExpenses();
    };

    const calculateProfitBeforeInterest = () => {
        const operatingProfit = calculateOperatingProfit();
        const interestIncome = parseFloat(incomeStatementData.interestIncome?.main || 0) + 
                              parseFloat(incomeStatementData.interestIncome?.cents || 0) / 100;
        return operatingProfit + interestIncome;
    };

    const calculateNetProfit = () => {
        const profitBeforeInterest = calculateProfitBeforeInterest();
        const interestExpense = parseFloat(incomeStatementData.interestExpense?.main || 0) + 
                               parseFloat(incomeStatementData.interestExpense?.cents || 0) / 100;
        return profitBeforeInterest - interestExpense;
    };

    const formatMoney = (amount) => {
        const main = Math.floor(amount);
        const cents = Math.round((amount - main) * 100);
        return { main: main.toString(), cents: cents.toString().padStart(2, '0') };
    };

    return (
        <div className="p-4 my-4 bg-gray-50 border border-gray-300 rounded-lg">
            <div className="text-center mb-4">
                <h3 className="text-lg font-bold text-gray-800">Income Statement (Trading Business)</h3>
            </div>
            
            <div className="border-2 border-gray-400 rounded-lg p-6 bg-white">
                {/* Header Section */}
                <div className="mb-6">
                    <div className="mb-4">
                        <label className="block font-semibold text-sm text-gray-700 mb-2">Owner Name (Optional):</label>
                        <input 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                            value={incomeStatementData.ownerName} 
                            onChange={e => handleFieldChange("ownerName", e.target.value)}
                            disabled={isSubmitted}
                            placeholder="Name of business owner"
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block font-semibold text-sm text-gray-700 mb-2">Business Name:</label>
                        <input 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                            value={incomeStatementData.businessName} 
                            onChange={e => handleFieldChange("businessName", e.target.value)}
                            disabled={isSubmitted}
                            placeholder="Name of business"
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block font-semibold text-sm text-gray-700 mb-2">INCOME STATEMENT FOR THE YEAR ENDED:</label>
                        <input 
                            type="date" 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                            value={incomeStatementData.yearEnded} 
                            onChange={e => handleFieldChange("yearEnded", e.target.value)}
                            disabled={isSubmitted}
                        />
                    </div>
                </div>

                {/* Income Statement Table */}
                <div className="mb-6">
                    <table className="min-w-full border border-gray-300">
                        <thead className="bg-gray-100">
                            <tr>
                                <th className="border border-gray-300 px-3 py-2 text-left text-sm font-semibold text-gray-700"></th>
                                <th className="border border-gray-300 px-3 py-2 text-left text-sm font-semibold text-gray-700">Note</th>
                                <th className="border border-gray-300 px-3 py-2 text-left text-sm font-semibold text-gray-700">R</th>
                            </tr>
                        </thead>
                        <tbody>
                            {/* Sales */}
                            <tr>
                                <td className="border border-gray-300 px-3 py-2 text-sm text-gray-700">Sales</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2">
                                    <MoneyInput
                                        value={incomeStatementData.sales}
                                        onChange={(value) => handleMoneyChange("sales", value)}
                                        disabled={isSubmitted}
                                        placeholder="0.00"
                                    />
                                </td>
                            </tr>
                            
                            {/* Cost of Sales */}
                            <tr>
                                <td className="border border-gray-300 px-3 py-2 text-sm text-gray-700">Cost of Sales</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2">
                                    <MoneyInput
                                        value={incomeStatementData.costOfSales}
                                        onChange={(value) => handleMoneyChange("costOfSales", value)}
                                        disabled={isSubmitted}
                                        placeholder="0.00"
                                    />
                                </td>
                            </tr>
                            
                            {/* Gross Profit */}
                            <tr className="bg-gray-50">
                                <td className="border border-gray-300 px-3 py-2 text-sm font-bold text-gray-700">Gross profit</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2">
                                    <MoneyInput
                                        value={formatMoney(calculateGrossProfit())}
                                        onChange={() => {}} // Read-only, calculated automatically
                                        disabled={true}
                                        placeholder="0.00"
                                    />
                                </td>
                            </tr>
                            
                            {/* Other Operating Income */}
                            <tr>
                                <td className="border border-gray-300 px-3 py-2 text-sm text-gray-700">Other operating income</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                            </tr>
                            
                            {/* Other Operating Income Items */}
                            {incomeStatementData.otherOperatingIncome.map((item, index) => (
                                <tr key={`other-income-${index}`}>
                                    <td className="border border-gray-300 px-3 py-2">
                                        <input 
                                            className="w-full p-1 border border-gray-200 rounded focus:outline-none focus:ring-1 focus:ring-blue-500 text-sm"
                                            value={item.description} 
                                            onChange={e => handleOtherIncomeChange(index, 'description', e.target.value)}
                                            disabled={isSubmitted}
                                            placeholder="Other income description"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-3 py-2"></td>
                                    <td className="border border-gray-300 px-3 py-2">
                                        <MoneyInput
                                            value={item.amount}
                                            onChange={(value) => handleOtherIncomeChange(index, 'amount', value)}
                                            disabled={isSubmitted}
                                            placeholder="0.00"
                                        />
                                    </td>
                                    {!isSubmitted && (
                                        <td className="border border-gray-300 px-3 py-2">
                                            <button 
                                                onClick={() => removeOtherIncome(index)}
                                                className="text-red-600 hover:text-red-800 text-lg font-bold"
                                            >
                                                ×
                                            </button>
                                        </td>
                                    )}
                                </tr>
                            ))}
                            
                            {/* Separator */}
                            <tr>
                                <td colSpan="3" className="border border-gray-300 px-3 py-1 bg-gray-200"></td>
                            </tr>
                            
                            {/* Gross Operating Income */}
                            <tr className="bg-gray-50">
                                <td className="border border-gray-300 px-3 py-2 text-sm font-bold text-gray-700">Gross Operating Income</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2">
                                    <MoneyInput
                                        value={formatMoney(calculateGrossOperatingIncome())}
                                        onChange={() => {}} // Read-only, calculated automatically
                                        disabled={true}
                                        placeholder="0.00"
                                    />
                                </td>
                            </tr>
                            
                            {/* Operating Expenses */}
                            <tr>
                                <td className="border border-gray-300 px-3 py-2 text-sm text-gray-700">Operating expenses</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                            </tr>
                            
                            {/* Operating Expenses Items */}
                            {incomeStatementData.operatingExpenses.map((item, index) => (
                                <tr key={`expense-${index}`}>
                                    <td className="border border-gray-300 px-3 py-2">
                                        <input 
                                            className="w-full p-1 border border-gray-200 rounded focus:outline-none focus:ring-1 focus:ring-blue-500 text-sm"
                                            value={item.description} 
                                            onChange={e => handleExpenseChange(index, 'description', e.target.value)}
                                            disabled={isSubmitted}
                                            placeholder="Expense description"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-3 py-2"></td>
                                    <td className="border border-gray-300 px-3 py-2">
                                        <MoneyInput
                                            value={item.amount}
                                            onChange={(value) => handleExpenseChange(index, 'amount', value)}
                                            disabled={isSubmitted}
                                            placeholder="0.00"
                                        />
                                    </td>
                                    {!isSubmitted && (
                                        <td className="border border-gray-300 px-3 py-2">
                                            <button 
                                                onClick={() => removeExpense(index)}
                                                className="text-red-600 hover:text-red-800 text-lg font-bold"
                                            >
                                                ×
                                            </button>
                                        </td>
                                    )}
                                </tr>
                            ))}
                            
                            {/* Separator */}
                            <tr>
                                <td colSpan="3" className="border border-gray-300 px-3 py-1 bg-gray-200"></td>
                            </tr>
                            
                            {/* Operating Profit */}
                            <tr>
                                <td className="border border-gray-300 px-3 py-2 text-sm text-gray-700">Operating profit (loss)</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2">
                                    <MoneyInput
                                        value={formatMoney(calculateOperatingProfit())}
                                        onChange={() => {}} // Read-only, calculated automatically
                                        disabled={true}
                                        placeholder="0.00"
                                    />
                                </td>
                            </tr>
                            
                            {/* Interest Income */}
                            <tr>
                                <td className="border border-gray-300 px-3 py-2 text-sm text-gray-700">Interest Income</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2">
                                    <MoneyInput
                                        value={incomeStatementData.interestIncome}
                                        onChange={(value) => handleMoneyChange("interestIncome", value)}
                                        disabled={isSubmitted}
                                        placeholder="0.00"
                                    />
                                </td>
                            </tr>
                            
                            {/* Profit Before Interest */}
                            <tr>
                                <td className="border border-gray-300 px-3 py-2 text-sm text-gray-700">Profit (loss) before interest expense</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2">
                                    <MoneyInput
                                        value={formatMoney(calculateProfitBeforeInterest())}
                                        onChange={() => {}} // Read-only, calculated automatically
                                        disabled={true}
                                        placeholder="0.00"
                                    />
                                </td>
                            </tr>
                            
                            {/* Interest Expense */}
                            <tr>
                                <td className="border border-gray-300 px-3 py-2 text-sm text-gray-700">Interest Expense</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2">
                                    <MoneyInput
                                        value={incomeStatementData.interestExpense}
                                        onChange={(value) => handleMoneyChange("interestExpense", value)}
                                        disabled={isSubmitted}
                                        placeholder="0.00"
                                    />
                                </td>
                            </tr>
                            
                            {/* Net Profit */}
                            <tr className="bg-gray-50">
                                <td className="border border-gray-300 px-3 py-2 text-sm font-bold text-gray-700">Net profit (loss) for the year</td>
                                <td className="border border-gray-300 px-3 py-2"></td>
                                <td className="border border-gray-300 px-3 py-2">
                                    <MoneyInput
                                        value={formatMoney(calculateNetProfit())}
                                        onChange={() => {}} // Read-only, calculated automatically
                                        disabled={true}
                                        placeholder="0.00"
                                    />
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    
                    {/* Add Buttons */}
                    {!isSubmitted && (
                        <div className="mt-4 flex space-x-4">
                            <button 
                                onClick={addOtherIncome}
                                className="px-4 py-2 bg-blue-500 text-white rounded-md text-sm font-semibold hover:bg-blue-600"
                            >
                                Add Other Income
                            </button>
                            <button 
                                onClick={addExpense}
                                className="px-4 py-2 bg-green-500 text-white rounded-md text-sm font-semibold hover:bg-green-600"
                            >
                                Add Expense
                            </button>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default TradingIncomeStatementInput;
