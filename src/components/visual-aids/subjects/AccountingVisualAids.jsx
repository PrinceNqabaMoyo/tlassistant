import React from 'react';

/**
 * Accounting Visual Aid Components
 * Handles balance sheets, income statements, T-accounts, etc.
 */

// Balance Sheet Component
export const BalanceSheet = ({ data, config, mode, onVisualAidChange }) => {
    const [visualData, setVisualData] = React.useState(data || {
        assets: {
            current: { cash: 50000, accounts_receivable: 25000, inventory: 30000 },
            non_current: { equipment: 100000, buildings: 200000 }
        },
        liabilities: {
            current: { accounts_payable: 20000, short_term_loans: 15000 },
            non_current: { long_term_loans: 150000 }
        },
        equity: { share_capital: 200000, retained_earnings: 50000 }
    });

    const handleDataChange = (section, subsection, item, value) => {
        const newData = { ...visualData };
        newData[section][subsection][item] = parseFloat(value) || 0;
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const calculateTotal = (items) => {
        return Object.values(items).reduce((sum, value) => sum + (parseFloat(value) || 0), 0);
    };

    const calculateAssetsTotal = () => {
        return calculateTotal(visualData.assets.current) + calculateTotal(visualData.assets.non_current);
    };

    const calculateLiabilitiesTotal = () => {
        return calculateTotal(visualData.liabilities.current) + calculateTotal(visualData.liabilities.non_current);
    };

    const calculateEquityTotal = () => {
        return calculateTotal(visualData.equity);
    };

    const isBalanced = () => {
        return Math.abs(calculateAssetsTotal() - (calculateLiabilitiesTotal() + calculateEquityTotal())) < 0.01;
    };

    return (
        <div className="balance-sheet bg-white border border-gray-200 rounded-lg p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4 text-center">
                Balance Sheet
            </h3>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Assets */}
                <div className="space-y-4">
                    <h4 className="text-lg font-semibold text-gray-700 border-b pb-2">Assets</h4>
                    
                    {/* Current Assets */}
                    <div>
                        <h5 className="font-medium text-gray-600 mb-2">Current Assets</h5>
                        <div className="space-y-2">
                            {Object.entries(visualData.assets.current).map(([item, value]) => (
                                <div key={item} className="flex justify-between items-center">
                                    <span className="text-sm text-gray-600 capitalize">
                                        {item.replace(/_/g, ' ')}
                                    </span>
                                    {mode === 'user-interactive' ? (
                                        <input
                                            type="number"
                                            value={value}
                                            onChange={(e) => handleDataChange('assets', 'current', item, e.target.value)}
                                            className="w-24 px-2 py-1 border border-gray-300 rounded text-right"
                                        />
                                    ) : (
                                        <span className="font-medium">R {value.toLocaleString()}</span>
                                    )}
                                </div>
                            ))}
                            <div className="border-t pt-2 font-medium">
                                Total Current Assets: R {calculateTotal(visualData.assets.current).toLocaleString()}
                            </div>
                        </div>
                    </div>

                    {/* Non-Current Assets */}
                    <div>
                        <h5 className="font-medium text-gray-600 mb-2">Non-Current Assets</h5>
                        <div className="space-y-2">
                            {Object.entries(visualData.assets.non_current).map(([item, value]) => (
                                <div key={item} className="flex justify-between items-center">
                                    <span className="text-sm text-gray-600 capitalize">
                                        {item.replace(/_/g, ' ')}
                                    </span>
                                    {mode === 'user-interactive' ? (
                                        <input
                                            type="number"
                                            value={value}
                                            onChange={(e) => handleDataChange('assets', 'non_current', item, e.target.value)}
                                            className="w-24 px-2 py-1 border border-gray-300 rounded text-right"
                                        />
                                    ) : (
                                        <span className="font-medium">R {value.toLocaleString()}</span>
                                    )}
                                </div>
                            ))}
                            <div className="border-t pt-2 font-medium">
                                Total Non-Current Assets: R {calculateTotal(visualData.assets.non_current).toLocaleString()}
                            </div>
                        </div>
                    </div>

                    <div className="border-t-2 pt-2 text-lg font-bold">
                        Total Assets: R {calculateAssetsTotal().toLocaleString()}
                    </div>
                </div>

                {/* Liabilities and Equity */}
                <div className="space-y-4">
                    <h4 className="text-lg font-semibold text-gray-700 border-b pb-2">Liabilities & Equity</h4>
                    
                    {/* Current Liabilities */}
                    <div>
                        <h5 className="font-medium text-gray-600 mb-2">Current Liabilities</h5>
                        <div className="space-y-2">
                            {Object.entries(visualData.liabilities.current).map(([item, value]) => (
                                <div key={item} className="flex justify-between items-center">
                                    <span className="text-sm text-gray-600 capitalize">
                                        {item.replace(/_/g, ' ')}
                                    </span>
                                    {mode === 'user-interactive' ? (
                                        <input
                                            type="number"
                                            value={value}
                                            onChange={(e) => handleDataChange('liabilities', 'current', item, e.target.value)}
                                            className="w-24 px-2 py-1 border border-gray-300 rounded text-right"
                                        />
                                    ) : (
                                        <span className="font-medium">R {value.toLocaleString()}</span>
                                    )}
                                </div>
                            ))}
                            <div className="border-t pt-2 font-medium">
                                Total Current Liabilities: R {calculateTotal(visualData.liabilities.current).toLocaleString()}
                            </div>
                        </div>
                    </div>

                    {/* Non-Current Liabilities */}
                    <div>
                        <h5 className="font-medium text-gray-600 mb-2">Non-Current Liabilities</h5>
                        <div className="space-y-2">
                            {Object.entries(visualData.liabilities.non_current).map(([item, value]) => (
                                <div key={item} className="flex justify-between items-center">
                                    <span className="text-sm text-gray-600 capitalize">
                                        {item.replace(/_/g, ' ')}
                                    </span>
                                    {mode === 'user-interactive' ? (
                                        <input
                                            type="number"
                                            value={value}
                                            onChange={(e) => handleDataChange('liabilities', 'non_current', item, e.target.value)}
                                            className="w-24 px-2 py-1 border border-gray-300 rounded text-right"
                                        />
                                    ) : (
                                        <span className="font-medium">R {value.toLocaleString()}</span>
                                    )}
                                </div>
                            ))}
                            <div className="border-t pt-2 font-medium">
                                Total Non-Current Liabilities: R {calculateTotal(visualData.liabilities.non_current).toLocaleString()}
                            </div>
                        </div>
                    </div>

                    {/* Equity */}
                    <div>
                        <h5 className="font-medium text-gray-600 mb-2">Equity</h5>
                        <div className="space-y-2">
                            {Object.entries(visualData.equity).map(([item, value]) => (
                                <div key={item} className="flex justify-between items-center">
                                    <span className="text-sm text-gray-600 capitalize">
                                        {item.replace(/_/g, ' ')}
                                    </span>
                                    {mode === 'user-interactive' ? (
                                        <input
                                            type="number"
                                            value={value}
                                            onChange={(e) => handleDataChange('equity', null, item, e.target.value)}
                                            className="w-24 px-2 py-1 border border-gray-300 rounded text-right"
                                        />
                                    ) : (
                                        <span className="font-medium">R {value.toLocaleString()}</span>
                                    )}
                                </div>
                            ))}
                            <div className="border-t pt-2 font-medium">
                                Total Equity: R {calculateEquityTotal().toLocaleString()}
                            </div>
                        </div>
                    </div>

                    <div className="border-t-2 pt-2 text-lg font-bold">
                        Total Liabilities & Equity: R {(calculateLiabilitiesTotal() + calculateEquityTotal()).toLocaleString()}
                    </div>
                </div>
            </div>

            {/* Balance Check */}
            <div className={`mt-6 p-4 rounded-lg text-center ${
                isBalanced() ? 'bg-green-50 border border-green-200' : 'bg-red-50 border border-red-200'
            }`}>
                <span className={`font-medium ${
                    isBalanced() ? 'text-green-800' : 'text-red-800'
                }`}>
                    {isBalanced() ? '✅ Balance Sheet is Balanced' : '❌ Balance Sheet is Not Balanced'}
                </span>
                {!isBalanced() && (
                    <p className="text-sm text-red-600 mt-1">
                        Difference: R {Math.abs(calculateAssetsTotal() - (calculateLiabilitiesTotal() + calculateEquityTotal())).toLocaleString()}
                    </p>
                )}
            </div>
        </div>
    );
};

// Income Statement Component
export const IncomeStatement = ({ data, config, mode, onVisualAidChange }) => {
    const [visualData, setVisualData] = React.useState(data || {
        revenue: { sales: 500000, interest_income: 5000, other_income: 2000 },
        expenses: { 
            cost_of_goods_sold: 300000, 
            operating_expenses: { salaries: 80000, rent: 24000, utilities: 12000, marketing: 15000 },
            interest_expense: 8000, 
            tax_expense: 25000 
        }
    });

    const handleDataChange = (section, subsection, item, value) => {
        const newData = { ...visualData };
        if (subsection) {
            newData[section][subsection][item] = parseFloat(value) || 0;
        } else {
            newData[section][item] = parseFloat(value) || 0;
        }
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const calculateTotalRevenue = () => {
        return Object.values(visualData.revenue).reduce((sum, value) => sum + (parseFloat(value) || 0), 0);
    };

    const calculateTotalExpenses = () => {
        const operatingExpenses = Object.values(visualData.expenses.operating_expenses).reduce((sum, value) => sum + (parseFloat(value) || 0), 0);
        return visualData.expenses.cost_of_goods_sold + operatingExpenses + visualData.expenses.interest_expense + visualData.expenses.tax_expense;
    };

    const calculateNetIncome = () => {
        return calculateTotalRevenue() - calculateTotalExpenses();
    };

    return (
        <div className="income-statement bg-white border border-gray-200 rounded-lg p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4 text-center">
                Income Statement
            </h3>
            
            <div className="space-y-6">
                {/* Revenue */}
                <div>
                    <h4 className="text-lg font-semibold text-gray-700 border-b pb-2">Revenue</h4>
                    <div className="space-y-2">
                        {Object.entries(visualData.revenue).map(([item, value]) => (
                            <div key={item} className="flex justify-between items-center">
                                <span className="text-sm text-gray-600 capitalize">
                                    {item.replace(/_/g, ' ')}
                                </span>
                                {mode === 'user-interactive' ? (
                                    <input
                                        type="number"
                                        value={value}
                                        onChange={(e) => handleDataChange('revenue', null, item, e.target.value)}
                                        className="w-32 px-2 py-1 border border-gray-300 rounded text-right"
                                    />
                                ) : (
                                    <span className="font-medium">R {value.toLocaleString()}</span>
                                )}
                            </div>
                        ))}
                        <div className="border-t pt-2 font-bold text-lg">
                            Total Revenue: R {calculateTotalRevenue().toLocaleString()}
                        </div>
                    </div>
                </div>

                {/* Expenses */}
                <div>
                    <h4 className="text-lg font-semibold text-gray-700 border-b pb-2">Expenses</h4>
                    
                    {/* Cost of Goods Sold */}
                    <div className="mb-4">
                        <div className="flex justify-between items-center">
                            <span className="text-sm text-gray-600">Cost of Goods Sold</span>
                            {mode === 'user-interactive' ? (
                                <input
                                    type="number"
                                    value={visualData.expenses.cost_of_goods_sold}
                                    onChange={(e) => handleDataChange('expenses', null, 'cost_of_goods_sold', e.target.value)}
                                    className="w-32 px-2 py-1 border border-gray-300 rounded text-right"
                                />
                            ) : (
                                <span className="font-medium">R {visualData.expenses.cost_of_goods_sold.toLocaleString()}</span>
                            )}
                        </div>
                    </div>

                    {/* Operating Expenses */}
                    <div className="mb-4">
                        <h5 className="font-medium text-gray-600 mb-2">Operating Expenses</h5>
                        <div className="space-y-2 ml-4">
                            {Object.entries(visualData.expenses.operating_expenses).map(([item, value]) => (
                                <div key={item} className="flex justify-between items-center">
                                    <span className="text-sm text-gray-600 capitalize">
                                        {item.replace(/_/g, ' ')}
                                    </span>
                                    {mode === 'user-interactive' ? (
                                        <input
                                            type="number"
                                            value={value}
                                            onChange={(e) => handleDataChange('expenses', 'operating_expenses', item, e.target.value)}
                                            className="w-32 px-2 py-1 border border-gray-300 rounded text-right"
                                        />
                                    ) : (
                                        <span className="font-medium">R {value.toLocaleString()}</span>
                                    )}
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* Other Expenses */}
                    <div className="space-y-2">
                        {Object.entries(visualData.expenses).filter(([key]) => !['cost_of_goods_sold', 'operating_expenses'].includes(key)).map(([item, value]) => (
                            <div key={item} className="flex justify-between items-center">
                                <span className="text-sm text-gray-600 capitalize">
                                    {item.replace(/_/g, ' ')}
                                </span>
                                {mode === 'user-interactive' ? (
                                    <input
                                        type="number"
                                        value={value}
                                        onChange={(e) => handleDataChange('expenses', null, item, e.target.value)}
                                        className="w-32 px-2 py-1 border border-gray-300 rounded text-right"
                                    />
                                ) : (
                                    <span className="font-medium">R {value.toLocaleString()}</span>
                                )}
                            </div>
                        ))}
                    </div>

                    <div className="border-t pt-2 font-bold text-lg">
                        Total Expenses: R {calculateTotalExpenses().toLocaleString()}
                    </div>
                </div>

                {/* Net Income */}
                <div className="border-t-2 pt-4">
                    <div className="flex justify-between items-center text-xl font-bold">
                        <span>Net Income</span>
                        <span className={calculateNetIncome() >= 0 ? 'text-green-600' : 'text-red-600'}>
                            R {calculateNetIncome().toLocaleString()}
                        </span>
                    </div>
                </div>
            </div>
        </div>
    );
};

// T-Account Component
export const TAccount = ({ data, config, mode, onVisualAidChange }) => {
    const [visualData, setVisualData] = React.useState(data || {
        account_name: 'Cash',
        account_type: 'asset',
        debit_entries: [
            { date: '2024-01-01', description: 'Initial investment', amount: 50000 },
            { date: '2024-01-15', description: 'Sales revenue', amount: 25000 }
        ],
        credit_entries: [
            { date: '2024-01-10', description: 'Equipment purchase', amount: 15000 },
            { date: '2024-01-20', description: 'Rent payment', amount: 5000 }
        ]
    });

    const handleEntryChange = (side, index, field, value) => {
        const newData = { ...visualData };
        newData[`${side}_entries`][index][field] = value;
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const addEntry = (side) => {
        const newData = { ...visualData };
        newData[`${side}_entries`].push({
            date: new Date().toISOString().split('T')[0],
            description: '',
            amount: 0
        });
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const removeEntry = (side, index) => {
        const newData = { ...visualData };
        newData[`${side}_entries`].splice(index, 1);
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const calculateTotal = (entries) => {
        return entries.reduce((sum, entry) => sum + (parseFloat(entry.amount) || 0), 0);
    };

    const calculateBalance = () => {
        const debitTotal = calculateTotal(visualData.debit_entries);
        const creditTotal = calculateTotal(visualData.credit_entries);
        
        if (visualData.account_type === 'asset' || visualData.account_type === 'expense') {
            return debitTotal - creditTotal;
        } else {
            return creditTotal - debitTotal;
        }
    };

    return (
        <div className="t-account bg-white border border-gray-200 rounded-lg p-6">
            <div className="text-center mb-6">
                <h3 className="text-xl font-bold text-gray-800 mb-2">
                    {visualData.account_name}
                </h3>
                <span className="text-sm text-gray-500 capitalize">
                    {visualData.account_type} Account
                </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Debit Side */}
                <div>
                    <h4 className="text-lg font-semibold text-gray-700 border-b pb-2 text-center">
                        Debit (Dr)
                    </h4>
                    <div className="space-y-3">
                        {visualData.debit_entries.map((entry, index) => (
                            <div key={index} className="border border-gray-200 rounded p-3">
                                {mode === 'user-interactive' ? (
                                    <>
                                        <input
                                            type="date"
                                            value={entry.date}
                                            onChange={(e) => handleEntryChange('debit', index, 'date', e.target.value)}
                                            className="w-full mb-2 px-2 py-1 border border-gray-300 rounded text-sm"
                                        />
                                        <input
                                            type="text"
                                            value={entry.description}
                                            onChange={(e) => handleEntryChange('debit', index, 'description', e.target.value)}
                                            placeholder="Description"
                                            className="w-full mb-2 px-2 py-1 border border-gray-300 rounded text-sm"
                                        />
                                        <input
                                            type="number"
                                            value={entry.amount}
                                            onChange={(e) => handleEntryChange('debit', index, 'amount', e.target.value)}
                                            placeholder="Amount"
                                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                                        />
                                        <button
                                            onClick={() => removeEntry('debit', index)}
                                            className="mt-2 w-full px-2 py-1 bg-red-100 text-red-700 rounded text-sm hover:bg-red-200"
                                        >
                                            Remove
                                        </button>
                                    </>
                                ) : (
                                    <>
                                        <div className="text-xs text-gray-500">{entry.date}</div>
                                        <div className="font-medium">{entry.description}</div>
                                        <div className="text-right font-bold">R {entry.amount.toLocaleString()}</div>
                                    </>
                                )}
                            </div>
                        ))}
                        {mode === 'user-interactive' && (
                            <button
                                onClick={() => addEntry('debit')}
                                className="w-full px-4 py-2 bg-blue-100 text-blue-700 rounded hover:bg-blue-200"
                            >
                                + Add Debit Entry
                            </button>
                        )}
                        <div className="border-t pt-2 font-bold text-lg text-center">
                            Total: R {calculateTotal(visualData.debit_entries).toLocaleString()}
                        </div>
                    </div>
                </div>

                {/* Credit Side */}
                <div>
                    <h4 className="text-lg font-semibold text-gray-700 border-b pb-2 text-center">
                        Credit (Cr)
                    </h4>
                    <div className="space-y-3">
                        {visualData.credit_entries.map((entry, index) => (
                            <div key={index} className="border border-gray-200 rounded p-3">
                                {mode === 'user-interactive' ? (
                                    <>
                                        <input
                                            type="date"
                                            value={entry.date}
                                            onChange={(e) => handleEntryChange('credit', index, 'date', e.target.value)}
                                            className="w-full mb-2 px-2 py-1 border border-gray-300 rounded text-sm"
                                        />
                                        <input
                                            type="text"
                                            value={entry.description}
                                            onChange={(e) => handleEntryChange('credit', index, 'description', e.target.value)}
                                            placeholder="Description"
                                            className="w-full mb-2 px-2 py-1 border border-gray-300 rounded text-sm"
                                        />
                                        <input
                                            type="number"
                                            value={entry.amount}
                                            onChange={(e) => handleEntryChange('credit', index, 'amount', e.target.value)}
                                            placeholder="Amount"
                                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                                        />
                                        <button
                                            onClick={() => removeEntry('credit', index)}
                                            className="mt-2 w-full px-2 py-1 bg-red-100 text-red-700 rounded text-sm hover:bg-red-200"
                                        >
                                            Remove
                                        </button>
                                    </>
                                ) : (
                                    <>
                                        <div className="text-xs text-gray-500">{entry.date}</div>
                                        <div className="font-medium">{entry.description}</div>
                                        <div className="text-right font-bold">R {entry.amount.toLocaleString()}</div>
                                    </>
                                )}
                            </div>
                        ))}
                        {mode === 'user-interactive' && (
                            <button
                                onClick={() => addEntry('credit')}
                                className="w-full px-4 py-2 bg-green-100 text-green-700 rounded hover:bg-green-200"
                            >
                                + Add Credit Entry
                            </button>
                        )}
                        <div className="border-t pt-2 font-bold text-lg text-center">
                            Total: R {calculateTotal(visualData.credit_entries).toLocaleString()}
                        </div>
                    </div>
                </div>
            </div>

            {/* Account Balance */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg text-center">
                <div className="text-lg font-semibold text-gray-800">
                    Account Balance
                </div>
                <div className={`text-2xl font-bold ${
                    calculateBalance() >= 0 ? 'text-green-600' : 'text-red-600'
                }`}>
                    R {calculateBalance().toLocaleString()}
                </div>
                <div className="text-sm text-gray-600 mt-1">
                    {calculateBalance() >= 0 ? 'Debit Balance' : 'Credit Balance'}
                </div>
            </div>
        </div>
    );
};

export default {
    BalanceSheet,
    IncomeStatement,
    TAccount
};
