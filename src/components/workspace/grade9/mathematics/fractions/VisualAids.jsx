import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const FractionsVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'equivalent', label: 'Equivalent' },
            { key: 'simplify', label: 'Simplify' },
            { key: 'mixed', label: 'Mixed/Improper' },
            { key: 'add_sub', label: 'Add/Subtract' },
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
                {visualAidsTab === 'equivalent' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Equivalent fractions</div>
                            <div className="text-sm text-gray-700">Multiply or divide numerator and denominator by the same number: a/b = (a×k)/(b×k).</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'simplify' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Simplest form</div>
                            <div className="text-sm text-gray-700">Divide numerator and denominator by their greatest common factor (GCF).</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'mixed' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Mixed ↔ improper</div>
                            <div className="text-sm text-gray-700">Mixed to improper: w a/b = (w×b + a)/b. Improper to mixed: divide numerator by denominator.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'add_sub' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Add & subtract</div>
                            <div className="text-sm text-gray-700">Find a common denominator first. Then add/subtract numerators and simplify.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default FractionsVisualAids;
