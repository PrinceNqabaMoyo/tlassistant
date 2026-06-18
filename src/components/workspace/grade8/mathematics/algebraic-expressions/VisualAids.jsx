import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const AlgebraicExpressionsVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'basics', label: 'Basics' },
            { key: 'like_terms', label: 'Like terms' },
            { key: 'substitution', label: 'Substitution' },
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
                {visualAidsTab === 'basics' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Normal algebraic language</div>
                            <div className="text-sm text-gray-700 mt-1">Write 2x instead of 2 × x. Write x × 2 as 2x.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Brackets</div>
                            <div className="text-sm text-gray-700 mt-1">If you add/subtract first and then multiply, use brackets: 3(x + 5).</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'like_terms' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Like terms</div>
                            <div className="text-sm text-gray-700 mt-1">Like terms have the same variable(s) raised to the same power. Example: 3x and −7x are like terms.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Unlike terms</div>
                            <div className="text-sm text-gray-700 mt-1">x and x² are unlike. x and y are unlike.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'substitution' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Substitution</div>
                            <div className="text-sm text-gray-700 mt-1">To evaluate 5x + 3 when x = 2: 5×2 + 3 = 13.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Order</div>
                            <div className="text-sm text-gray-700 mt-1">Multiply first, then add/subtract.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default AlgebraicExpressionsVisualAids;
