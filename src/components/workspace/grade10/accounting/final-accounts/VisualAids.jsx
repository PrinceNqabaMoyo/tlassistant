import React from 'react';

export const Grade10FinalAccountsVisualAids = ({
    visualAidsTab = 'overview',
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = [
        { key: 'overview', label: 'Overview' },
        { key: 'closing', label: 'Closing Transfers' },
        { key: 'depreciation', label: 'Depreciation' },
        { key: 'adjustments', label: 'Adjustments' },
    ];

    return (
        <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
            <div className="flex items-center justify-between px-4 py-3 bg-gradient-to-r from-amber-50 to-orange-50 border-b border-slate-200">
                <h3 className="text-sm font-semibold text-amber-900">📊 Final Accounts Reference</h3>
                {setVisualAidsOpen && (
                    <button onClick={() => setVisualAidsOpen(false)} className="text-slate-400 hover:text-slate-600 text-lg leading-none">&times;</button>
                )}
            </div>

            <div className="flex border-b border-slate-100 px-2 pt-1 gap-1 overflow-x-auto">
                {tabs.map(t => (
                    <button key={t.key}
                        className={`px-3 py-1.5 text-xs font-medium rounded-t transition-colors whitespace-nowrap ${visualAidsTab === t.key ? 'bg-amber-100 text-amber-800 border-b-2 border-amber-500' : 'text-slate-500 hover:text-slate-700 hover:bg-slate-50'}`}
                        onClick={() => setVisualAidsTab?.(t.key)}>
                        {t.label}
                    </button>
                ))}
            </div>

            <div className="p-4 text-sm text-slate-700 space-y-3 max-h-[400px] overflow-y-auto">
                {visualAidsTab === 'overview' && (
                    <div className="space-y-2">
                        <p className="font-medium text-amber-800">Year-end & Final Accounts Process</p>
                        <ul className="list-disc pl-5 space-y-1 text-xs">
                            <li><strong>Step 1:</strong> Record year-end adjustments (depreciation, bad debts, accruals, prepayments)</li>
                            <li><strong>Step 2:</strong> Prepare the Trading Account (cost of sales, gross profit)</li>
                            <li><strong>Step 3:</strong> Prepare the Profit & Loss Account (net profit/loss)</li>
                            <li><strong>Step 4:</strong> Close nominal accounts to Owner's Equity</li>
                            <li><strong>Step 5:</strong> Prepare the Post-closing Trial Balance</li>
                        </ul>
                    </div>
                )}

                {visualAidsTab === 'closing' && (
                    <div className="space-y-2">
                        <p className="font-medium text-amber-800">Closing Transfer Entries</p>
                        <div className="bg-amber-50 border border-amber-200 rounded-lg p-3 text-xs space-y-1">
                            <p><strong>Revenue accounts</strong> → Dr Revenue, Cr Trading/P&L</p>
                            <p><strong>Expense accounts</strong> → Dr Trading/P&L, Cr Expense</p>
                            <p><strong>Net Profit</strong> → Dr P&L, Cr Capital (Owner's Equity)</p>
                            <p><strong>Drawings</strong> → Dr Capital, Cr Drawings</p>
                        </div>
                        <p className="text-xs text-slate-500">Only real accounts (assets, liabilities, owner's equity) remain after closing.</p>
                    </div>
                )}

                {visualAidsTab === 'depreciation' && (
                    <div className="space-y-3">
                        <div className="bg-blue-50 border border-blue-200 rounded-lg p-3">
                            <p className="font-semibold text-blue-800 text-xs mb-1">Straight-line Method</p>
                            <p className="text-xs">Annual Depreciation = (Cost − Residual Value) ÷ Useful Life</p>
                        </div>
                        <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                            <p className="font-semibold text-green-800 text-xs mb-1">Diminishing Balance Method</p>
                            <p className="text-xs">Annual Depreciation = Carrying Value × Rate %</p>
                            <p className="text-xs mt-1">Carrying Value = Cost − Accumulated Depreciation</p>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'adjustments' && (
                    <div className="space-y-2">
                        <table className="w-full text-xs">
                            <thead><tr className="bg-slate-50"><th className="text-left p-1.5 font-semibold">Adjustment</th><th className="text-left p-1.5 font-semibold">Journal Entry</th></tr></thead>
                            <tbody>
                                <tr className="border-t"><td className="p-1.5 font-medium">Accrued expense</td><td className="p-1.5">Dr Expense, Cr Accrued Expense</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Prepaid expense</td><td className="p-1.5">Dr Prepaid Expense, Cr Expense</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Accrued income</td><td className="p-1.5">Dr Accrued Income, Cr Income</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Income received in advance</td><td className="p-1.5">Dr Income, Cr Income Received in Advance</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Bad debts</td><td className="p-1.5">Dr Bad Debts, Cr Debtors Control</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Depreciation</td><td className="p-1.5">Dr Depreciation, Cr Accumulated Depreciation</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Consumable stores on hand</td><td className="p-1.5">Dr Consumable Stores on Hand (asset), Cr Consumable Stores (expense)</td></tr>
                            </tbody>
                        </table>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Grade10FinalAccountsVisualAids;
