import React from 'react';
import { X } from 'lucide-react';

const WholeNumbersVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = [
        { key: 'methods', label: 'Methods' },
        { key: 'factors', label: 'Factors' },
    ];

    return (
        <div className="h-full flex flex-col">
            <div className="flex items-center justify-between p-3 border-b border-gray-200">
                <div className="font-semibold text-gray-900">Visual Aids</div>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 rounded-md hover:bg-gray-100 text-gray-600"
                    title="Close visual aids"
                >
                    <X className="w-4 h-4" />
                </button>
            </div>

            <div className="p-3 border-b border-gray-200">
                <div className="flex gap-2 flex-wrap">
                    {tabs.map((t) => (
                        <button
                            key={t.key}
                            onClick={() => setVisualAidsTab(t.key)}
                            className={`px-3 py-1 rounded-full text-sm font-semibold border ${visualAidsTab === t.key ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'}`}
                        >
                            {t.label}
                        </button>
                    ))}
                </div>
            </div>

            <div className="flex-1 overflow-y-auto p-4">
                {visualAidsTab === 'methods' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="font-semibold text-gray-900 mb-1">Column methods</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">Addition:</span> add right-to-left; carry tens.</div>
                                <div><span className="font-semibold">Subtraction:</span> subtract right-to-left; borrow 10 when needed.</div>
                                <div><span className="font-semibold">Long division:</span> subtract big chunks of the divisor; remainder must be less than divisor.</div>
                            </div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="font-semibold text-gray-900 mb-1">Rounding & compensating</div>
                            <div className="text-sm text-gray-700">Round to an easy base, calculate, then adjust by the total rounding error.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'factors' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="font-semibold text-gray-900 mb-1">Prime numbers</div>
                            <div className="text-sm text-gray-700">2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31…</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="font-semibold text-gray-900 mb-1">Prime factorisation reminder</div>
                            <div className="text-sm text-gray-700">Divide by 2, then 3, then 5, 7… Use powers like 2^3.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default WholeNumbersVisualAids;
