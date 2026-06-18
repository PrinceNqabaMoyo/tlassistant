import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const FunctionsRelationshipsVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'basics', label: 'Basics' },
            { key: 'representations', label: 'Representations' },
            { key: 'graphs', label: 'Graphs' },
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
                            <div className="text-sm font-semibold text-gray-800">Variables</div>
                            <div className="text-sm text-gray-700">Input (x) changes. Output (y) depends on x.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Function</div>
                            <div className="text-sm text-gray-700">A function gives exactly one output for each input.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'representations' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Same relationship, different forms</div>
                            <div className="text-sm text-gray-700">Flow diagram, table, formula, and graph can describe the same rule.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Substitute</div>
                            <div className="text-sm text-gray-700">To find outputs, substitute x into the formula (e.g. y = 5x + 20).</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'graphs' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Reading a line</div>
                            <div className="text-sm text-gray-700">Pick an x, go up/down to the line, then read the y value.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Intercepts</div>
                            <div className="text-sm text-gray-700">y-intercept is where the line crosses the y-axis (x=0). x-intercept is where y=0.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default FunctionsRelationshipsVisualAids;
