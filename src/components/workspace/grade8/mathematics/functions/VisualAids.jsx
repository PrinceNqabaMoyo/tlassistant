import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const FunctionsVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'basics', label: 'Basics' },
            { key: 'flow', label: 'Flow diagrams' },
            { key: 'formulas', label: 'Formulas' },
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
                            <div className="text-sm font-semibold text-gray-800">Constant vs variable</div>
                            <div className="text-sm text-gray-700">A constant stays the same. A variable can change.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Relationship</div>
                            <div className="text-sm text-gray-700">If one variable depends on the other, they have a relationship.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'flow' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Flow diagram idea</div>
                            <div className="text-sm text-gray-700 mt-1">Input → apply operator(s) → output. Each input lines up with its output.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Order matters</div>
                            <div className="text-sm text-gray-700 mt-1">If there are two boxes, do the first box first, then the second.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'formulas' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Symbols</div>
                            <div className="text-sm text-gray-700">Use x for input and y for output. Example: y = 3x + 8.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Reading a formula</div>
                            <div className="text-sm text-gray-700 mt-1">3x means “multiply x by 3”. +8 means “add 8”.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default FunctionsVisualAids;
