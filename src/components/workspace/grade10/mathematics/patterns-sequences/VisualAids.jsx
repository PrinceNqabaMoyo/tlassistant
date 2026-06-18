import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const PatternsSequencesVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'notation', label: 'Notation' },
            { key: 'arithmetic', label: 'Arithmetic' },
            { key: 'geometric', label: 'Geometric' },
            { key: 'linear', label: 'Linear' },
        ],
        []
    );

    return (
        <div className="h-full flex flex-col">
            <div className="flex items-center justify-between p-3 border-b border-gray-200 bg-white">
                <div className="text-sm font-semibold text-gray-800">Patterns &amp; Sequences</div>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 rounded-md hover:bg-gray-100 text-gray-600"
                    title="Close visual aids"
                >
                    <X className="w-4 h-4" />
                </button>
            </div>

            <div className="p-3 border-b border-gray-200 bg-white">
                <div className="flex flex-wrap gap-2">
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
                {visualAidsTab === 'notation' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Term notation</div>
                            <div className="text-sm text-gray-700">Use T1, T2, … for term values, and T_n for the general term (nth term).</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Common difference</div>
                            <div className="text-sm text-gray-700">For an arithmetic sequence, d = T_n − T_(n−1).</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'arithmetic' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Arithmetic sequences</div>
                            <div className="text-sm text-gray-700">Add a constant difference each time.</div>
                            <div className="mt-2 text-sm text-gray-700">General term: T_n = a + (n − 1)d</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'geometric' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Geometric sequences</div>
                            <div className="text-sm text-gray-700">Multiply by a constant ratio each time.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'linear' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Linear patterns from situations</div>
                            <div className="text-sm text-gray-700">Many patterns grow by a constant amount, so they can be modeled with T_n = an + b.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default PatternsSequencesVisualAids;
