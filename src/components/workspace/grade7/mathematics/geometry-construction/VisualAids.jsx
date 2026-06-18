import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const GeoConstructVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'angles', label: 'Angles' },
            { key: 'degrees', label: 'Degrees' },
            { key: 'protractor', label: 'Protractor' },
            { key: 'lines', label: 'Lines' },
            { key: 'compass', label: 'Compass' },
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
                {visualAidsTab === 'angles' && (
                    <div className="space-y-3">
                        <div className="text-sm text-gray-700">An angle is made by two rays (arms) meeting at a point (vertex).</div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Angle types (by size)</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">Acute</span>: between 0° and 90°</div>
                                <div><span className="font-semibold">Right</span>: exactly 90°</div>
                                <div><span className="font-semibold">Obtuse</span>: between 90° and 180°</div>
                                <div><span className="font-semibold">Straight</span>: exactly 180°</div>
                                <div><span className="font-semibold">Reflex</span>: between 180° and 360°</div>
                            </div>
                            <div className="mt-3 text-xs text-gray-500">Tip: arm length does not change the angle size.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'degrees' && (
                    <div className="space-y-3">
                        <div className="text-sm text-gray-700">Degrees (°) measure turn. A full turn is 360°.</div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Common angle facts</div>
                            <div className="grid grid-cols-2 gap-2 text-sm text-gray-700">
                                <div className="border border-gray-200 rounded-md p-2"><span className="font-semibold">Right</span>: 90°</div>
                                <div className="border border-gray-200 rounded-md p-2"><span className="font-semibold">Straight</span>: 180°</div>
                                <div className="border border-gray-200 rounded-md p-2"><span className="font-semibold">Full turn</span>: 360°</div>
                                <div className="border border-gray-200 rounded-md p-2"><span className="font-semibold">Half-right</span>: 45°</div>
                                <div className="border border-gray-200 rounded-md p-2"><span className="font-semibold">Third-right</span>: 30°</div>
                                <div className="border border-gray-200 rounded-md p-2"><span className="font-semibold">Quarter-right</span>: 22.5°</div>
                            </div>
                            <div className="mt-3 text-xs text-gray-500">Clock tip: the hour hand moves 30° each hour (360 ÷ 12).</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'protractor' && (
                    <div className="space-y-3">
                        <div className="text-sm text-gray-700">A protractor has two scales. Choose the one that starts at 0° on your reference arm.</div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Measuring steps</div>
                            <ol className="list-decimal pl-5 text-sm text-gray-700 space-y-1">
                                <li>Put the origin exactly on the vertex.</li>
                                <li>Line up the baseline with one arm.</li>
                                <li>Read the scale that starts at 0° on the baseline arm.</li>
                            </ol>
                            <div className="mt-3 text-xs text-gray-500">Reflex angles: if the smaller angle is x°, the reflex is 360° − x°.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'lines' && (
                    <div className="space-y-3">
                        <div className="text-sm text-gray-700">Parallel lines never meet. Perpendicular lines meet at 90°.</div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Symbols</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">⊥</span> means perpendicular</div>
                                <div><span className="font-semibold">//</span> means parallel</div>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'compass' && (
                    <div className="space-y-3">
                        <div className="text-sm text-gray-700">A compass draws circles. The compass opening equals the radius.</div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Key ideas</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">Radius</span>: centre to edge (constant in every direction)</div>
                                <div><span className="font-semibold">Concentric circles</span>: circles with the same centre</div>
                                <div><span className="font-semibold">Intersections</span>: where circles/lines cross</div>
                            </div>
                            <div className="mt-3 text-xs text-gray-500">Construction tip: keep the compass opening fixed unless the step says to change it.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default GeoConstructVisualAids;
