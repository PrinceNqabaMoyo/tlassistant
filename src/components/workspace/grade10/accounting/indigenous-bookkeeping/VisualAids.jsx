import React from 'react';

export const Grade10IndigenousBookkeepingVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    const tab = visualAidsTab || 'concepts';

    const Card = ({ title, children }) => (
        <div className="bg-white border border-gray-200 rounded-lg p-3">
            <div className="text-sm font-bold text-gray-900 mb-1">{title}</div>
            <div className="text-sm text-gray-800">{children}</div>
        </div>
    );

    return (
        <div className="p-4">
            <div className="flex items-center justify-between mb-3">
                <h3 className="text-lg font-bold text-gray-900">Accounting Visual Aids</h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="px-3 py-1 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-md text-sm font-semibold"
                >
                    Close
                </button>
            </div>

            <div className="flex gap-2 mb-4">
                <button
                    onClick={() => setVisualAidsTab('concepts')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'concepts' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Concepts
                </button>
                <button
                    onClick={() => setVisualAidsTab('guidelines')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'guidelines' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Guidelines
                </button>
            </div>

            {tab === 'concepts' && (
                <div className="space-y-3">
                    <Card title="Quick contrast">
                        <div className="space-y-2">
                            <div><span className="font-semibold">Informal:</span> simple, survival-focused, mostly cash, minimal records, low inventory.</div>
                            <div><span className="font-semibold">Formal:</span> structured system, consistent policies, standards (e.g. GAAP), cash + credit, records for reporting/tax.</div>
                        </div>
                    </Card>

                    <Card title="Key terms (memory cards)">
                        <div className="space-y-1">
                            <div><span className="font-semibold">Cost price (CP):</span> what the trader pays for goods bought for resale.</div>
                            <div><span className="font-semibold">Cost of sales:</span> what the goods sold cost the trader (often CP of goods sold).</div>
                            <div><span className="font-semibold">Mark-up (MU):</span> profit added to cost price.</div>
                            <div><span className="font-semibold">Selling price (SP):</span> price charged to customers.</div>
                        </div>
                    </Card>

                    <Card title="Price rules">
                        <div className="space-y-1">
                            <div><span className="font-semibold">Formula:</span> CP + MU = SP</div>
                            <div><span className="font-semibold">If MU% is on CP:</span> SP = CP × (1 + MU%/100)</div>
                            <div><span className="font-semibold">Find CP:</span> CP = SP ÷ (1 + MU%/100)</div>
                        </div>
                    </Card>

                    <Card title="Recall checks">
                        <div className="space-y-1">
                            <div>Ask: “Is the business mostly cash or cash + credit?”</div>
                            <div>Ask: “Are records minimal or structured?”</div>
                            <div>Ask: “Does selling price change quickly (informal) or follow cost + margin (formal)?”</div>
                        </div>
                    </Card>
                </div>
            )}

            {tab === 'guidelines' && (
                <div className="space-y-2 text-sm text-gray-800">
                    <p className="font-semibold">Activity 1 planning table tips:</p>
                    <ul className="list-disc pl-5 space-y-1">
                        <li>Capital: start-up cash + assets contributed (tools/equipment).</li>
                        <li>Income/expenses per day: estimates based on realistic trading.</li>
                        <li>Cost of sales: what you pay suppliers.</li>
                        <li>Selling price: costs + expenses + profit margin (can be negotiable).</li>
                        <li>Stock kept: usually low stock in informal businesses.</li>
                    </ul>
                </div>
            )}
        </div>
    );
};
