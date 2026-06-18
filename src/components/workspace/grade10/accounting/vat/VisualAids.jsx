import React from 'react';

export const Grade10VATVisualAids = ({
    visualAidsTab = 'overview',
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = [
        { key: 'overview', label: 'Overview' },
        { key: 'formulas', label: 'Formulas' },
        { key: 'classification', label: 'Classification' },
        { key: 'ethics', label: 'Ethics' },
    ];

    return (
        <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
            <div className="flex items-center justify-between px-4 py-3 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-slate-200">
                <h3 className="text-sm font-semibold text-violet-900">🧾 VAT Reference</h3>
                {setVisualAidsOpen && (
                    <button onClick={() => setVisualAidsOpen(false)} className="text-slate-400 hover:text-slate-600 text-lg leading-none">&times;</button>
                )}
            </div>

            <div className="flex border-b border-slate-100 px-2 pt-1 gap-1 overflow-x-auto">
                {tabs.map(t => (
                    <button key={t.key}
                        className={`px-3 py-1.5 text-xs font-medium rounded-t transition-colors whitespace-nowrap ${visualAidsTab === t.key ? 'bg-violet-100 text-violet-800 border-b-2 border-violet-500' : 'text-slate-500 hover:text-slate-700 hover:bg-slate-50'}`}
                        onClick={() => setVisualAidsTab?.(t.key)}>
                        {t.label}
                    </button>
                ))}
            </div>

            <div className="p-4 text-sm text-slate-700 space-y-3 max-h-[400px] overflow-y-auto">
                {visualAidsTab === 'overview' && (
                    <div className="space-y-2">
                        <p className="font-medium text-violet-800">Value Added Tax (VAT)</p>
                        <ul className="list-disc pl-5 space-y-1 text-xs">
                            <li><strong>VAT rate:</strong> 15% in South Africa</li>
                            <li><strong>VAT vendor:</strong> Business registered with SARS for VAT (turnover &gt; R1 million)</li>
                            <li><strong>Input VAT:</strong> VAT paid on purchases (claimable from SARS)</li>
                            <li><strong>Output VAT:</strong> VAT charged on sales (payable to SARS)</li>
                            <li><strong>VAT payable = Output VAT − Input VAT</strong></li>
                            <li>If Input &gt; Output → refund from SARS</li>
                        </ul>
                    </div>
                )}

                {visualAidsTab === 'formulas' && (
                    <div className="space-y-3">
                        <div className="bg-violet-50 border border-violet-200 rounded-lg p-3">
                            <p className="font-semibold text-violet-800 text-xs mb-1">VAT Inclusive → Exclusive</p>
                            <p className="text-xs font-medium">Price excl. VAT = Price incl. VAT ÷ 1.15</p>
                            <p className="text-xs">VAT amount = Price incl. − Price excl.</p>
                        </div>
                        <div className="bg-blue-50 border border-blue-200 rounded-lg p-3">
                            <p className="font-semibold text-blue-800 text-xs mb-1">VAT Exclusive → Inclusive</p>
                            <p className="text-xs font-medium">Price incl. VAT = Price excl. VAT × 1.15</p>
                            <p className="text-xs">VAT amount = Price excl. × 0.15</p>
                        </div>
                        <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                            <p className="font-semibold text-green-800 text-xs mb-1">Quick VAT Extract</p>
                            <p className="text-xs font-medium">VAT = Price incl. × 15/115</p>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'classification' && (
                    <div className="space-y-2">
                        <table className="w-full text-xs">
                            <thead><tr className="bg-slate-50"><th className="text-left p-1.5 font-semibold">Type</th><th className="text-left p-1.5 font-semibold">Rate</th><th className="text-left p-1.5 font-semibold">Examples</th></tr></thead>
                            <tbody>
                                <tr className="border-t"><td className="p-1.5 font-medium">Standard-rated</td><td className="p-1.5">15%</td><td className="p-1.5">Most goods and services</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Zero-rated</td><td className="p-1.5">0%</td><td className="p-1.5">Basic foodstuffs (brown bread, maize, rice, milk, eggs), exports, petrol/diesel</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Exempt</td><td className="p-1.5">N/A</td><td className="p-1.5">Financial services, public transport, rental of dwellings, education</td></tr>
                            </tbody>
                        </table>
                        <p className="text-xs text-slate-500 mt-1">Zero-rated: vendor can still claim input VAT. Exempt: vendor cannot claim input VAT.</p>
                    </div>
                )}

                {visualAidsTab === 'ethics' && (
                    <div className="space-y-2">
                        <div className="bg-red-50 border border-red-200 rounded-lg p-3">
                            <p className="font-semibold text-red-800 text-xs mb-1">Tax Evasion (ILLEGAL)</p>
                            <ul className="list-disc pl-4 text-xs text-red-700 space-y-1">
                                <li>Not registering when required</li>
                                <li>Hiding income / under-reporting sales</li>
                                <li>Claiming false input VAT</li>
                                <li>Not submitting VAT returns</li>
                            </ul>
                        </div>
                        <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                            <p className="font-semibold text-green-800 text-xs mb-1">Tax Avoidance (LEGAL)</p>
                            <ul className="list-disc pl-4 text-xs text-green-700 space-y-1">
                                <li>Claiming all legitimate input VAT</li>
                                <li>Using tax incentives and rebates</li>
                                <li>Proper record-keeping for deductions</li>
                            </ul>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Grade10VATVisualAids;
