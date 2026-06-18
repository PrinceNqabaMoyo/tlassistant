import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const AnalyticalGeometryVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'basics', label: 'Basics' },
            { key: 'distance', label: 'Distance' },
            { key: 'midpoint', label: 'Midpoint' },
            { key: 'gradient', label: 'Gradient' },
            { key: 'lines', label: 'Lines' },
        ],
        []
    );

    return (
        <div className="h-full flex flex-col">
            <div className="flex items-center justify-between p-3 border-b border-gray-200 bg-white">
                <div className="text-sm font-semibold text-gray-800">Analytical Geometry</div>
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
                {visualAidsTab === 'basics' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Coordinate basics</div>
                            <div className="text-sm text-gray-700">Points are written as (x; y). Be consistent with order and signs.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Parallel / perpendicular</div>
                            <div className="text-sm text-gray-700">Parallel: m₁ = m₂. Perpendicular: m₁·m₂ = −1 (when both gradients exist).</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'distance' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Distance formula</div>
                            <div className="text-sm text-gray-700">AB = √((x₂−x₁)² + (y₂−y₁)²)</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'midpoint' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Midpoint formula</div>
                            <div className="text-sm text-gray-700">M = ((x₁+x₂)/2; (y₁+y₂)/2)</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'gradient' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Gradient</div>
                            <div className="text-sm text-gray-700">m = (y₂−y₁)/(x₂−x₁). Horizontal: m=0. Vertical: undefined.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'lines' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Line forms</div>
                            <div className="text-sm text-gray-700">Point-slope: y − y₁ = m(x − x₁). Standard: Ax + By + C = 0. Slope-intercept: y = mx + c.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default AnalyticalGeometryVisualAids;
