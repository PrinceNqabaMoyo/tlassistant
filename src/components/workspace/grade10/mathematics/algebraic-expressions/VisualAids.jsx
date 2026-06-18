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
            { key: 'expand', label: 'Expand' },
            { key: 'factor', label: 'Factorise' },
            { key: 'surds', label: 'Surds' },
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
                            <div className="text-sm font-semibold text-gray-800">Real numbers</div>
                            <div className="text-sm text-gray-700 mt-1">Rational numbers can be written as a/b. Irrational numbers cannot (e.g. π, √2).</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Rounding off</div>
                            <div className="text-sm text-gray-700 mt-1">To round to n decimal places, look at digit (n+1) to decide if you round up.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'surds' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Estimating surds</div>
                            <div className="text-sm text-gray-700 mt-1">Use consecutive perfect squares/cubes: if 25 &lt; 26 &lt; 36 then 5 &lt; √26 &lt; 6.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'expand' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Distributive property</div>
                            <div className="text-sm text-gray-700 mt-1">a(b + c) = ab + ac and a(b − c) = ab − ac.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'factor' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Common factor</div>
                            <div className="text-sm text-gray-700 mt-1">Take out the greatest common factor of all terms.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Difference of squares</div>
                            <div className="text-sm text-gray-700 mt-1">A² − B² = (A − B)(A + B).</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Grouping</div>
                            <div className="text-sm text-gray-700 mt-1">Group into pairs, factor each pair, then factor the common bracket.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default AlgebraicExpressionsVisualAids;
