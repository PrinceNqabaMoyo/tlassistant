import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const ExponentsVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
    vizBase,
    setVizBase,
    vizExponent,
    setVizExponent,
    vizRoot,
    setVizRoot,
    formatExponentCarets,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'powers', label: 'Powers' },
            { key: 'roots', label: 'Roots' },
            { key: 'tables', label: 'Tables' },
            { key: 'bodmas', label: 'BODMAS' },
        ],
        []
    );

    const safeBase = Math.max(1, Math.min(20, Number(vizBase) || 1));
    const safeExp = Math.max(1, Math.min(10, Number(vizExponent) || 1));
    const expanded = safeExp <= 8 ? Array.from({ length: safeExp }, () => String(safeBase)).join(' × ') : `${safeBase} × … × ${safeBase} (${safeExp} factors)`;
    const powValue = safeExp <= 8 ? safeBase ** safeExp : null;

    const rootN = Math.max(0, Number(vizRoot) || 0);
    const sqrtVal = Number.isFinite(rootN) ? Math.floor(Math.sqrt(rootN)) : 0;
    const isPerfectSquare = Number.isFinite(rootN) && sqrtVal * sqrtVal === rootN;
    const cbrtVal = Number.isFinite(rootN) ? Math.round(Math.cbrt(rootN)) : 0;
    const isPerfectCube = Number.isFinite(rootN) && cbrtVal * cbrtVal * cbrtVal === rootN;

    const squares = Array.from({ length: 15 }, (_, i) => {
        const n = i + 1;
        return { n, v: n * n };
    });
    const cubes = Array.from({ length: 12 }, (_, i) => {
        const n = i + 1;
        return { n, v: n * n * n };
    });

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
                {visualAidsTab === 'powers' && (
                    <div>
                        <div className="text-sm text-gray-700 mb-3">A power means repeated multiplication with the same base.</div>
                        <div className="grid grid-cols-1 gap-3 mb-4">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 mb-1">Base</label>
                                <input
                                    type="number"
                                    min="1"
                                    max="20"
                                    value={vizBase}
                                    onChange={(e) => setVizBase(Number(e.target.value))}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                />
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 mb-1">Exponent</label>
                                <input
                                    type="number"
                                    min="1"
                                    max="10"
                                    value={vizExponent}
                                    onChange={(e) => setVizExponent(Number(e.target.value))}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                />
                                <div className="mt-1 text-xs text-gray-500">2 = squared, 3 = cubed, &gt;3 = "to the power …".</div>
                            </div>
                        </div>

                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">Meaning</div>
                            <div className="text-sm text-gray-700 mb-2">
                                <span className="font-semibold">{formatExponentCarets(`${safeBase}^${safeExp}`)}</span> means:
                            </div>
                            <div className="text-sm text-gray-800 font-medium">{expanded}</div>
                            {powValue !== null && (
                                <div className="mt-3 text-sm text-gray-700"><span className="font-semibold">Value:</span> {powValue}</div>
                            )}
                            {powValue === null && (
                                <div className="mt-3 text-xs text-gray-500">(Value hidden for large exponents.)</div>
                            )}
                        </div>
                    </div>
                )}

                {visualAidsTab === 'roots' && (
                    <div>
                        <div className="text-sm text-gray-700 mb-3">Roots undo powers: √ undoes squaring, ∛ undoes cubing.</div>
                        <div className="mb-4">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Number</label>
                            <input
                                type="number"
                                min="0"
                                value={vizRoot}
                                onChange={(e) => setVizRoot(Number(e.target.value))}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            />
                        </div>

                        <div className="space-y-3">
                            <div className="bg-white border border-gray-200 rounded-lg p-4">
                                <div className="text-sm font-semibold text-gray-800">Square root</div>
                                <div className="text-sm text-gray-700 mt-1">√{rootN} = {sqrtVal}{isPerfectSquare ? '' : ' (not a perfect square)'}</div>
                            </div>
                            <div className="bg-white border border-gray-200 rounded-lg p-4">
                                <div className="text-sm font-semibold text-gray-800">Cube root</div>
                                <div className="text-sm text-gray-700 mt-1">∛{rootN} = {cbrtVal}{isPerfectCube ? '' : ' (not a perfect cube)'}</div>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'tables' && (
                    <div>
                        <div className="text-sm text-gray-700 mb-3">Reference table (use to build fluency).</div>
                        <div className="grid grid-cols-1 gap-4">
                            <div className="bg-white border border-gray-200 rounded-lg p-4">
                                <div className="text-sm font-semibold text-gray-800 mb-2">Squares (1² to 15²)</div>
                                <div className="grid grid-cols-3 gap-2">
                                    {squares.map(({ n, v }) => (
                                        <div key={`sq_${n}`} className="text-xs border border-gray-200 rounded-md px-2 py-2 bg-gray-50">
                                            <div className="font-semibold text-gray-800">{n}²</div>
                                            <div className="text-gray-700">{v}</div>
                                        </div>
                                    ))}
                                </div>
                            </div>

                            <div className="bg-white border border-gray-200 rounded-lg p-4">
                                <div className="text-sm font-semibold text-gray-800 mb-2">Cubes (1³ to 12³)</div>
                                <div className="grid grid-cols-3 gap-2">
                                    {cubes.map(({ n, v }) => (
                                        <div key={`cb_${n}`} className="text-xs border border-gray-200 rounded-md px-2 py-2 bg-gray-50">
                                            <div className="font-semibold text-gray-800">{n}³</div>
                                            <div className="text-gray-700">{v}</div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'bodmas' && (
                    <div>
                        <div className="text-sm text-gray-700 mb-3">When there are multiple operations, the order matters.</div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-2">BODMAS</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">B</span>rackets first</div>
                                <div><span className="font-semibold">O</span>rders (powers and roots) next</div>
                                <div><span className="font-semibold">D</span>ivision and <span className="font-semibold">M</span>ultiplication (left to right)</div>
                                <div><span className="font-semibold">A</span>ddition and <span className="font-semibold">S</span>ubtraction (left to right)</div>
                            </div>
                            <div className="mt-3 text-xs text-gray-500">Tip: Orders includes exponents like 3² and roots like √49.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default ExponentsVisualAids;
