import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const ExponentsVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'laws', label: 'Laws' },
            { key: 'order', label: 'Order' },
            { key: 'negative', label: 'Negative exp' },
        ],
        []
    );

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
                {visualAidsTab === 'laws' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Key laws</div>
                            <div className="text-sm text-gray-700">Same base multiply → add exponents. Same base divide → subtract exponents. Power of power → multiply exponents. a^0 = 1.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'order' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Order of operations</div>
                            <div className="text-sm text-gray-700">Calculate powers before multiplication/division, then addition/subtraction.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'negative' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Negative exponents</div>
                            <div className="text-sm text-gray-700">a^-n = 1/a^n (reciprocal). Example: 5^-2 = 1/5^2 = 1/25.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default ExponentsVisualAids;
