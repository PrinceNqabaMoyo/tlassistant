import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const StraightLinesVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'basics', label: 'Basics' },
            { key: 'parallel', label: 'Parallel' },
            { key: 'perpendicular', label: 'Perpendicular' },
            { key: 'symbols', label: 'Symbols' },
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
                            <div className="text-sm font-semibold text-gray-800 mb-2">Line segment vs line vs ray</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">Line segment</span>: has 2 endpoints (measurable)</div>
                                <div><span className="font-semibold">Line</span>: no endpoints (cannot be measured)</div>
                                <div><span className="font-semibold">Ray</span>: 1 endpoint, extends forever in 1 direction</div>
                            </div>
                        </div>
                        <div className="text-xs text-gray-500">Tip: A line and a ray extend indefinitely, so we only draw a part of them.</div>
                    </div>
                )}

                {visualAidsTab === 'parallel' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Parallel lines</div>
                            <div className="text-sm text-gray-700">Parallel lines stay the same distance apart and do not meet.</div>
                            <div className="mt-2 text-sm text-gray-700"><span className="font-semibold">Example:</span> AB // CD</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'perpendicular' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Perpendicular lines</div>
                            <div className="text-sm text-gray-700">Perpendicular lines meet to form a right angle (90°).</div>
                            <div className="mt-2 text-sm text-gray-700"><span className="font-semibold">Example:</span> AB ⊥ CD</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'symbols' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Symbols</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">//</span> means parallel</div>
                                <div><span className="font-semibold">⊥</span> means perpendicular</div>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default StraightLinesVisualAids;
