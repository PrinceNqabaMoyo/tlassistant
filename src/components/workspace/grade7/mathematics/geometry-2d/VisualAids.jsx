import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const Geo2DVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'triangles', label: 'Triangles' },
            { key: 'quadrilaterals', label: 'Quadrilaterals' },
            { key: 'circles', label: 'Circles' },
            { key: 'similarity', label: 'Similarity' },
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
                {visualAidsTab === 'triangles' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Triangle types</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">Equilateral</span>: 3 equal sides</div>
                                <div><span className="font-semibold">Isosceles</span>: 2 equal sides</div>
                                <div><span className="font-semibold">Scalene</span>: no equal sides</div>
                                <div><span className="font-semibold">Right-angled</span>: one angle is 90°</div>
                            </div>
                        </div>
                        <div className="text-xs text-gray-500">Tip: "right-angled" is about an angle, not side lengths.</div>
                    </div>
                )}

                {visualAidsTab === 'quadrilaterals' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Adjacent vs opposite</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">Adjacent</span>: share a vertex</div>
                                <div><span className="font-semibold">Opposite</span>: do not touch</div>
                            </div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Common quadrilaterals</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">Parallelogram</span>: opposite sides parallel</div>
                                <div><span className="font-semibold">Rectangle</span>: 4 right angles</div>
                                <div><span className="font-semibold">Square</span>: 4 equal sides + 4 right angles</div>
                                <div><span className="font-semibold">Rhombus</span>: 4 equal sides</div>
                                <div><span className="font-semibold">Kite</span>: two pairs of adjacent equal sides</div>
                                <div><span className="font-semibold">Trapezium</span>: at least one pair of opposite sides parallel</div>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'circles' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Circle vocabulary</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">Centre</span>: middle point</div>
                                <div><span className="font-semibold">Radius</span>: centre to circle</div>
                                <div><span className="font-semibold">Diameter</span>: across the circle through centre (2 radii)</div>
                                <div><span className="font-semibold">Chord</span>: joins two points on the circle</div>
                                <div><span className="font-semibold">Sector</span>: region between two radii and an arc</div>
                                <div><span className="font-semibold">Segment</span>: region between a chord and an arc</div>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'similarity' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Similar vs congruent</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">Congruent</span>: same shape and same size</div>
                                <div><span className="font-semibold">Similar</span>: same shape, different size allowed</div>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Geo2DVisualAids;
