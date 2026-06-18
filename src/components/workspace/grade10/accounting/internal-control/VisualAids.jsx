import React from 'react';

export const Grade10InternalControlVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
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
                <h3 className="text-lg font-bold text-gray-900">Accounting Visual Aids</h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="px-3 py-1 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-md text-sm font-semibold"
                >
                    Close
                </button>
            </div>

            <div className="flex flex-wrap gap-2 mb-4">
                <button
                    onClick={() => setVisualAidsTab('overview')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'overview' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Overview
                </button>
                <button
                    onClick={() => setVisualAidsTab('cash')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'cash' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Cash
                </button>
                <button
                    onClick={() => setVisualAidsTab('keywords')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'keywords' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Keywords
                </button>
            </div>

            {tab === 'overview' && (
                <div className="space-y-3">
                    <Card title="Internal control (definition)">
                        Internal control is what management and staff do within the business to control activities, reduce risks (fraud/theft/errors), and help the business achieve its objectives.
                    </Card>
                    <Card title="The control process">
                        <div className="space-y-1">
                            <div><span className="font-semibold">1.</span> Decide objectives (short-term and long-term)</div>
                            <div><span className="font-semibold">2.</span> Gather information (strengths and shortcomings)</div>
                            <div><span className="font-semibold">3.</span> Analyse the information</div>
                            <div><span className="font-semibold">4.</span> Act against shortcomings</div>
                        </div>
                    </Card>
                    <Card title="Common control areas">
                        <div className="space-y-1">
                            <div>Stock</div>
                            <div>Debtors</div>
                            <div>Creditors</div>
                            <div>Fixed assets</div>
                            <div>Consumables</div>
                            <div>Cash (CRJ/CPJ/PCJ)</div>
                        </div>
                    </Card>
                </div>
            )}

            {tab === 'cash' && (
                <div className="space-y-3">
                    <Card title="Cash receipts (CRJ)">
                        Issue a document for every cash receipt, record it as soon as possible, keep cash safe, and deposit cash promptly (preferably within 24 hours).
                    </Card>
                    <Card title="Cash payments (CPJ)">
                        Payments should be by cheque (except petty cash). Cheques must be stored safely, recorded in sequence, and blank cheques must never be signed.
                    </Card>
                    <Card title="Petty cash (PCJ)">
                        Keep petty cash in a locked box, record payments in the petty cash journal, and attach supporting documents to vouchers where possible.
                    </Card>
                </div>
            )}

            {tab === 'keywords' && (
                <div className="space-y-3">
                    <Card title="Keywords">
                        <div className="space-y-2">
                            <div><span className="font-semibold">Separation of duties:</span> split tasks so one person cannot commit and hide errors/fraud.</div>
                            <div><span className="font-semibold">Stocktaking:</span> counting stock regularly to confirm records match actual stock.</div>
                            <div><span className="font-semibold">Authorisation:</span> approval before buying assets or spending money.</div>
                            <div><span className="font-semibold">Pilfering:</span> petty theft (e.g. taking stationery).</div>
                        </div>
                    </Card>
                </div>
            )}
        </div>
    );
};
