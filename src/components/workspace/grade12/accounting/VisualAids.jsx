import React from 'react';

export const Grade12AccountingVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
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
                <h3 className="text-lg font-bold text-gray-900">Grade 12 Accounting • Visual aids</h3>
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
                    onClick={() => setVisualAidsTab('income_statement')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'income_statement' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Income statement
                </button>
                <button
                    onClick={() => setVisualAidsTab('cash_flow')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'cash_flow' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Cash flow
                </button>
                <button
                    onClick={() => setVisualAidsTab('ratios')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'ratios' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Ratios
                </button>
            </div>

            {tab === 'overview' && (
                <div className="space-y-3">
                    <Card title="What you practice here">
                        <div className="space-y-1">
                            <div>Companies: concepts, audits and governance.</div>
                            <div>Company general ledger (share capital, dividends, tax).</div>
                            <div>Financial statements, cash flow statements, and interpretation/ratios.</div>
                        </div>
                    </Card>
                    <Card title="Exam tip">
                        In calculations, always state the formula and show working. In comments, compare current vs previous year and conclude.
                    </Card>
                </div>
            )}

            {tab === 'income_statement' && (
                <div className="space-y-3">
                    <Card title="Income statement order (companies)">
                        <div className="space-y-1">
                            <div>Sales (less debtors’ allowances)</div>
                            <div>Less: Cost of sales</div>
                            <div>Gross profit</div>
                            <div>Other operating income</div>
                            <div>Gross operating income</div>
                            <div>Less: Operating expenses (directors’ fees, audit fees, etc.)</div>
                            <div>Operating profit</div>
                            <div>+ Interest income</div>
                            <div>Profit before finance cost</div>
                            <div>Less: Interest expense / finance cost</div>
                            <div>Profit before tax</div>
                            <div>Less: Income tax</div>
                            <div>Net profit after tax</div>
                        </div>
                    </Card>
                </div>
            )}

            {tab === 'cash_flow' && (
                <div className="space-y-3">
                    <Card title="Cash generated from operations">
                        Start with net profit before tax, add back non-cash items (e.g. depreciation) and adjust for changes in working capital.
                    </Card>
                    <Card title="Net change in cash">
                        Net change = Operating + Investing + Financing; Closing cash = Opening cash + Net change.
                    </Card>
                </div>
            )}

            {tab === 'ratios' && (
                <div className="space-y-3">
                    <Card title="Liquidity">
                        Current ratio = Current assets : Current liabilities. Acid test = (Receivables + Cash) : Current liabilities.
                    </Card>
                    <Card title="Gearing">
                        Debt/equity ratio = Non-current liabilities : Shareholders’ equity.
                    </Card>
                    <Card title="Shareholder return">
                        EPS (cents) = Net profit after tax / Issued shares × 100. DPS (cents) = (Interim + Final dividends) / Issued shares × 100.
                    </Card>
                </div>
            )}
        </div>
    );
};
