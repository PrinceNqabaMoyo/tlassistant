import React from 'react';

export const Grade11AccountingVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    const tab = visualAidsTab || 'overview';

    const Card = ({ title, children }) => (
        <div className="bg-white border border-gray-200 rounded-lg p-3">
            <div className="text-sm font-bold text-gray-900 mb-1">{title}</div>
            <div className="text-sm text-gray-800">{children}</div>
        </div>
    );

    return (
        <div className="p-4">
            <div className="flex items-center justify-between mb-3">
                <h3 className="text-lg font-bold text-gray-900">Grade 11 Accounting • Visual aids</h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="px-3 py-1 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-md text-sm font-semibold"
                >
                    Close
                </button>
            </div>

            <div className="flex gap-2 mb-4 flex-wrap">
                <button
                    onClick={() => setVisualAidsTab('overview')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'overview' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Overview
                </button>
                <button
                    onClick={() => setVisualAidsTab('statements')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'statements' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Statements
                </button>
                <button
                    onClick={() => setVisualAidsTab('partnerships')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'partnerships' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Partnerships
                </button>
                <button
                    onClick={() => setVisualAidsTab('recon')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'recon' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Reconciliation
                </button>
            </div>

            {tab === 'overview' && (
                <div className="space-y-3">
                    <Card title="What you practice here">
                        <div className="space-y-1">
                            <div>Partnership accounting concepts and adjustments.</div>
                            <div>Fixed/tangible assets (depreciation and carrying value).</div>
                            <div>Partnership ledger accounts, balance sheet, reconciliations, and income statements.</div>
                        </div>
                    </Card>
                    <Card title="Exam tip">
                        Keep formats consistent: headings, subtotals, and brackets for expenses.
                    </Card>
                </div>
            )}

            {tab === 'statements' && (
                <div className="space-y-3">
                    <Card title="Income Statement (Statement of comprehensive income)">
                        <div className="space-y-1">
                            <div>Sales</div>
                            <div>Less: Cost of sales</div>
                            <div>Gross profit</div>
                            <div>Other operating income</div>
                            <div>Gross operating income</div>
                            <div>Less: Operating expenses</div>
                            <div>Operating profit</div>
                            <div>± Interest</div>
                            <div>Net profit</div>
                        </div>
                    </Card>
                    <Card title="Brackets">
                        Expenses are usually shown in brackets, e.g. <span className="font-semibold">(2400.00)</span>
                    </Card>
                </div>
            )}

            {tab === 'partnerships' && (
                <div className="space-y-3">
                    <Card title="Appropriation vs Current account">
                        <div className="space-y-1">
                            <div><span className="font-semibold">Appropriation account:</span> shows distribution of profit (interest on capital, salaries, profit share).</div>
                            <div><span className="font-semibold">Current account:</span> records drawings, salaries, interest, and profit share affecting partners.</div>
                        </div>
                    </Card>
                </div>
            )}

            {tab === 'recon' && (
                <div className="space-y-3">
                    <Card title="Bank reconciliation">
                        Start from the given balance (bank statement or cash book) and adjust for timing differences.
                    </Card>
                </div>
            )}
        </div>
    );
};
