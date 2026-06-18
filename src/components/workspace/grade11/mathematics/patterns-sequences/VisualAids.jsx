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
            { key: 'linear', label: 'Linear' },
            { key: 'nth', label: 'T_n' },
            { key: 'quadratic', label: 'Quadratic' },
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
                            <div className="text-sm font-semibold text-gray-800 mb-1">Differences</div>
                            <div className="text-sm text-gray-700">First differences: T2 − T1, T3 − T2, … Second differences: differences of first differences.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'linear' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Linear (arithmetic) sequences</div>
                            <div className="text-sm text-gray-700">Add a constant difference each time.</div>
                            <div className="mt-2 text-sm text-gray-700">General term: T_n = a + (n − 1)d</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'nth' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Arithmetic nth term</div>
                            <div className="text-sm text-gray-700">T_n = a + (n − 1)d</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Linear form</div>
                            <div className="text-sm text-gray-700">Many linear sequences can be written as T_n = pn + q.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'quadratic' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Quadratic sequences</div>
                            <div className="text-sm text-gray-700">A sequence is quadratic if the second differences are constant.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">General term</div>
                            <div className="text-sm text-gray-700">T_n = an^2 + bn + c</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default PatternsSequencesVisualAids;
