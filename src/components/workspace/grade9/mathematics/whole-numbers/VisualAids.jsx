import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const WholeNumbersVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'number_systems', label: 'Number systems' },
            { key: 'rounding', label: 'Rounding' },
            { key: 'division', label: 'Division' },
            { key: 'factors', label: 'Factors' },
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
                {visualAidsTab === 'number_systems' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Sets</div>
                            <div className="text-sm text-gray-700 space-y-1">
                                <div><span className="font-semibold">Natural</span>: 1, 2, 3, …</div>
                                <div><span className="font-semibold">Whole</span>: 0, 1, 2, 3, …</div>
                                <div><span className="font-semibold">Integers</span>: …, −2, −1, 0, 1, 2, …</div>
                                <div><span className="font-semibold">Rational</span>: can be written as a fraction a/b</div>
                            </div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Closure</div>
                            <div className="text-sm text-gray-700">A set is closed under an operation if doing the operation stays in the set.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'rounding' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Rounding rule</div>
                            <div className="text-sm text-gray-700">Look at the next digit: 0–4 round down, 5–9 round up.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Estimating products</div>
                            <div className="text-sm text-gray-700">Round both numbers to a friendly base, then multiply.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'division' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Check with multiplication</div>
                            <div className="text-sm text-gray-700">If a ÷ b = q remainder r, then a = bq + r and 0 ≤ r &lt; b.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Long division idea</div>
                            <div className="text-sm text-gray-700">Work left to right: estimate → multiply → subtract → bring down.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'factors' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Prime factorisation</div>
                            <div className="text-sm text-gray-700">Write a number as a product of primes (use exponents for repeats).</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Helpful primes</div>
                            <div className="text-sm text-gray-700">2, 3, 5, 7, 11, 13, …</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default WholeNumbersVisualAids;
