import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const WholeNumbersVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
    multiplesBase,
    setMultiplesBase,
    multiplesMax,
    setMultiplesMax,
    placeValueInput,
    setPlaceValueInput,
    roundingNumber,
    setRoundingNumber,
    roundingBase,
    setRoundingBase,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'place_value', label: 'Place Value' },
            { key: 'rounding', label: 'Rounding' },
            { key: 'multiples', label: 'Multiples' },
        ],
        []
    );

    const placeValueColumns = useMemo(
        () => [
            { key: 'm', label: 'M' },
            { key: 'hth', label: 'HTh' },
            { key: 'tth', label: 'TTh' },
            { key: 'th', label: 'Th' },
            { key: 'h', label: 'H' },
            { key: 't', label: 'T' },
            { key: 'u', label: 'U' },
        ],
        []
    );

    const safeMax = Math.min(200, Math.max(20, Number(multiplesMax) || 100));
    const grid = [];
    for (let i = 1; i <= safeMax; i++) grid.push(i);

    const pvDigits = (String(placeValueInput || '').replace(/\D/g, '')).split('');
    const pvCells = {};
    placeValueColumns.forEach((c) => {
        pvCells[c.key] = '';
    });

    const reversedDigits = [...pvDigits].reverse();
    const columnKeysRightToLeft = ['u', 't', 'h', 'th', 'tth', 'hth', 'm'];
    columnKeysRightToLeft.forEach((k, idx) => {
        pvCells[k] = reversedDigits[idx] || '';
    });

    const roundingN = Number(String(roundingNumber || '').replace(/[^0-9]/g, ''));
    const safeRoundingBase = Math.max(1, Number(roundingBase) || 10);
    const roundingValid = Number.isFinite(roundingN) && roundingN >= 0;
    const lower = roundingValid ? Math.floor(roundingN / safeRoundingBase) * safeRoundingBase : 0;
    const upper = roundingValid ? lower + safeRoundingBase : safeRoundingBase;
    const mid = roundingValid ? lower + safeRoundingBase / 2 : safeRoundingBase / 2;
    const rounded = roundingValid ? (roundingN < mid ? lower : upper) : 0;
    const positionPct = roundingValid && safeRoundingBase > 0
        ? Math.max(0, Math.min(100, ((roundingN - lower) / safeRoundingBase) * 100))
        : 0;

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
                {visualAidsTab === 'place_value' && (
                    <div>
                        <div className="text-sm text-gray-700 mb-3">Type a number and see how it splits into place values.</div>
                        <div className="mb-4">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Number</label>
                            <input
                                type="text"
                                value={placeValueInput}
                                onChange={(e) => setPlaceValueInput(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                placeholder="e.g. 507 032"
                            />
                            <div className="mt-1 text-xs text-gray-500">Digits only are used (spaces/commas ignored).</div>
                        </div>
                        <div className="overflow-x-auto">
                            <table className="min-w-full border border-gray-200 rounded-lg overflow-hidden">
                                <thead className="bg-gray-50">
                                    <tr>
                                        {placeValueColumns.map((c) => (
                                            <th key={c.key} className="px-3 py-2 text-xs font-bold text-gray-700 border-b border-gray-200 text-center">
                                                {c.label}
                                            </th>
                                        ))}
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        {placeValueColumns.map((c) => (
                                            <td key={c.key} className="px-3 py-4 text-center border-b border-gray-200">
                                                <div className="w-10 h-10 mx-auto rounded-md border border-gray-200 bg-white flex items-center justify-center font-semibold text-gray-800">
                                                    {pvCells[c.key]}
                                                </div>
                                            </td>
                                        ))}
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div className="mt-4 text-xs text-gray-600">Tip: Start from the right (Units) and move left.</div>
                    </div>
                )}

                {visualAidsTab === 'rounding' && (
                    <div>
                        <div className="text-sm text-gray-700 mb-3">Use the number line idea to see what it rounds to.</div>
                        <div className="grid grid-cols-1 gap-3 mb-4">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 mb-1">Number</label>
                                <input
                                    type="text"
                                    value={roundingNumber}
                                    onChange={(e) => setRoundingNumber(e.target.value)}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                    placeholder="e.g. 6 742"
                                />
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 mb-1">Round to nearest</label>
                                <select
                                    value={safeRoundingBase}
                                    onChange={(e) => setRoundingBase(Number(e.target.value))}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                >
                                    <option value={10}>10</option>
                                    <option value={100}>100</option>
                                    <option value={1000}>1 000</option>
                                    <option value={10000}>10 000</option>
                                </select>
                            </div>
                        </div>

                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-xs text-gray-600 mb-2">Nearest multiples:</div>
                            <div className="flex items-center justify-between text-sm font-semibold text-gray-800 mb-3">
                                <div>{lower}</div>
                                <div>{upper}</div>
                            </div>
                            <div className="relative h-3 bg-gray-200 rounded-full">
                                <div className="absolute top-0 h-3 bg-indigo-200 rounded-full" style={{ left: '0%', width: '50%' }} />
                                <div className="absolute top-0 h-3 bg-green-200 rounded-full" style={{ left: '50%', width: '50%' }} />
                                <div className="absolute -top-1 w-1 h-5 bg-gray-700" style={{ left: '50%' }} title="Midpoint" />
                                {roundingValid && (
                                    <div className="absolute -top-1 w-1 h-5 bg-red-600" style={{ left: `${positionPct}%` }} title="Your number" />
                                )}
                            </div>
                            <div className="mt-3 text-sm text-gray-700">
                                {roundingValid ? (
                                    <>
                                        <span className="font-semibold">Rounded result:</span> {rounded}
                                        <div className="text-xs text-gray-500 mt-1">Midpoint is {mid}. If the number is below midpoint, round down; if it is at/above midpoint, round up.</div>
                                    </>
                                ) : (
                                    <span className="text-gray-500">Enter a whole number to see the rounding number line.</span>
                                )}
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'multiples' && (
                    <div>
                        <div className="flex items-end justify-between gap-3 mb-3">
                            <div className="w-full">
                                <label className="block text-sm font-semibold text-gray-700 mb-1">Highlight multiples of</label>
                                <input
                                    type="number"
                                    min="2"
                                    max="20"
                                    value={multiplesBase}
                                    onChange={(e) => setMultiplesBase(Number(e.target.value))}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                />
                            </div>
                        </div>

                        <div className="mb-3">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Grid max</label>
                            <select
                                value={multiplesMax}
                                onChange={(e) => setMultiplesMax(Number(e.target.value))}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md"
                            >
                                <option value={50}>50</option>
                                <option value={100}>100</option>
                                <option value={150}>150</option>
                                <option value={200}>200</option>
                            </select>
                        </div>

                        <div className="grid grid-cols-10 gap-1">
                            {grid.map((n) => {
                                const isMult = multiplesBase > 0 && n % multiplesBase === 0;
                                return (
                                    <div
                                        key={n}
                                        className={`text-xs text-center py-2 rounded ${isMult ? 'bg-green-600 text-white font-bold' : 'bg-white border border-gray-200 text-gray-700'}`}
                                    >
                                        {n}
                                    </div>
                                );
                            })}
                        </div>
                        <div className="mt-3 text-xs text-gray-600">Multiples are numbers you get when you multiply by a whole number.</div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default WholeNumbersVisualAids;
