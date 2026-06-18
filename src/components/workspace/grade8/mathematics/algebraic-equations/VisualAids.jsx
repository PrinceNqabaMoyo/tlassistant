import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const AlgebraicEquationsVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'basics', label: 'Basics' },
            { key: 'inverse', label: 'Inverse ops' },
            { key: 'check', label: 'Check' },
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
                            <div className="text-sm font-semibold text-gray-800">Equation</div>
                            <div className="text-sm text-gray-700 mt-1">An equation is true when both sides are equal.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Balance idea</div>
                            <div className="text-sm text-gray-700 mt-1">Whatever you do to one side, do to the other side.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'inverse' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Undo +b</div>
                            <div className="text-sm text-gray-700 mt-1">If x + b = c, subtract b: x = c − b.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Undo ×a</div>
                            <div className="text-sm text-gray-700 mt-1">If ax = c, divide by a: x = c ÷ a.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'check' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Check a solution</div>
                            <div className="text-sm text-gray-700 mt-1">Substitute your x back into the original equation. Both sides must match.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default AlgebraicEquationsVisualAids;
