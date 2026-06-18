import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const AlgebraicExpressions1VisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'basics', label: 'Basics' },
            { key: 'like_terms', label: 'Like terms' },
            { key: 'expand', label: 'Expand' },
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
                            <div className="text-sm font-semibold text-gray-800">Order of operations</div>
                            <div className="text-sm text-gray-700 mt-1">Brackets first. Then × and ÷. Then + and − (left to right).</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Algebraic language</div>
                            <div className="text-sm text-gray-700 mt-1">Write 4x instead of 4 × x, and 3(x + 2) when adding first.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'like_terms' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Like terms</div>
                            <div className="text-sm text-gray-700 mt-1">Same variable and same power (e.g., 3x and −5x, or 2y² and 7y²).</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Combine</div>
                            <div className="text-sm text-gray-700 mt-1">Add/subtract the coefficients: 3x + 2x = 5x; 7y − 10y = −3y.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'expand' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Distributive property</div>
                            <div className="text-sm text-gray-700 mt-1">a(b + c) = ab + ac and a(b − c) = ab − ac.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Example</div>
                            <div className="text-sm text-gray-700 mt-1">3(2x − 5) = 3·2x − 3·5 = 6x − 15.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default AlgebraicExpressions1VisualAids;
