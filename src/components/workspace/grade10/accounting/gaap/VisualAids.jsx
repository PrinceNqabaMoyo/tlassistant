import React from 'react';

export const Grade10AccountingGAAPVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    const tab = visualAidsTab || 'principles';

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
                    onClick={() => setVisualAidsTab('principles')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'principles' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Principles
                </button>
                <button
                    onClick={() => setVisualAidsTab('keywords')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'keywords' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Keywords
                </button>
                <button
                    onClick={() => setVisualAidsTab('exam')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'exam' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Exam tips
                </button>
            </div>

            {tab === 'principles' && (
                <div className="space-y-3">
                    <Card title="GAAP in one line">
                        GAAP is a framework of rules, procedures and guidelines that helps businesses record and report financial information consistently and reliably.
                    </Card>

                    <Card title="The 6 key Grade 10 principles">
                        <div className="space-y-2">
                            <div><span className="font-semibold">Historical cost:</span> record assets at purchase price.</div>
                            <div><span className="font-semibold">Prudence:</span> be conservative when uncertain; don’t overstate assets/income.</div>
                            <div><span className="font-semibold">Materiality:</span> show important items separately; group small items.</div>
                            <div><span className="font-semibold">Business entity:</span> business and owner finances are separate.</div>
                            <div><span className="font-semibold">Going concern:</span> assume the business will continue operating.</div>
                            <div><span className="font-semibold">Matching:</span> match income and related expenses in the same period.</div>
                        </div>
                    </Card>
                </div>
            )}

            {tab === 'keywords' && (
                <div className="space-y-3">
                    <Card title="Keywords">
                        <div className="space-y-2">
                            <div><span className="font-semibold">Accounting policy:</span> consistent decisions about how to record similar transactions.</div>
                            <div><span className="font-semibold">Cost price:</span> purchase price (historical cost).</div>
                            <div><span className="font-semibold">Foreseeable future:</span> time period assumed under going concern.</div>
                            <div><span className="font-semibold">Adjusting entry:</span> entry made to record income/expenses in the correct period (matching).</div>
                        </div>
                    </Card>
                </div>
            )}

            {tab === 'exam' && (
                <div className="space-y-3">
                    <Card title="Exam tips">
                        <div className="space-y-2">
                            <div><span className="font-semibold">Tip 1:</span> Link the example to the principle (e.g. “Vehicles recorded at cost” → historical cost).</div>
                            <div><span className="font-semibold">Tip 2:</span> Matching keywords: “separate owner” (entity), “continue operating” (going concern), “same period” (matching).</div>
                            <div><span className="font-semibold">Tip 3:</span> If it’s about being careful/uncertain values, it’s usually prudence.</div>
                        </div>
                    </Card>
                </div>
            )}
        </div>
    );
};
