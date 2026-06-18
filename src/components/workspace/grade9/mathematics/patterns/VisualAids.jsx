import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const PatternsVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'rules', label: 'Rules' },
            { key: 'tables', label: 'Tables' },
        ],
        []
    );

    const squares = useMemo(
        () => Array.from({ length: 15 }, (_, i) => {
            const n = i + 1;
            return { n, v: n * n };
        }),
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
                {visualAidsTab === 'rules' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Arithmetic sequence</div>
                            <div className="text-sm text-gray-700">Add/subtract the same number each time (constant difference).</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Geometric sequence</div>
                            <div className="text-sm text-gray-700">Multiply/divide by the same number each time (constant ratio).</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Square numbers</div>
                            <div className="text-sm text-gray-700">Square numbers follow n²: 1, 4, 9, 16, ...</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Changing differences</div>
                            <div className="text-sm text-gray-700">Sometimes the difference is not constant (e.g. 1, 2, 4, 7, 11, ...). Look for a pattern in the differences.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'tables' && (
                    <div className="grid grid-cols-1 gap-4">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Squares (1² to 15²)</div>
                            <div className="grid grid-cols-3 gap-2">
                                {squares.map(({ n, v }) => (
                                    <div key={`g9_sq_${n}`} className="text-xs border border-gray-200 rounded-md px-2 py-2 bg-gray-50">
                                        <div className="font-semibold text-gray-800">{n}²</div>
                                        <div className="text-gray-700">{v}</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default PatternsVisualAids;
