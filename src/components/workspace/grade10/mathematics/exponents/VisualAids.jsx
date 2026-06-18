import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const ExponentsVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'laws', label: 'Laws' },
            { key: 'negative', label: 'Negative' },
            { key: 'rational', label: 'Rational' },
            { key: 'equations', label: 'Equations' },
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
                {visualAidsTab === 'laws' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Same base</div>
                            <div className="text-sm text-gray-700 mt-1">a^m × a^n = a^(m+n) and a^m ÷ a^n = a^(m−n).</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Power of a power</div>
                            <div className="text-sm text-gray-700 mt-1">(a^m)^n = a^(m·n).</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'negative' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Negative exponent</div>
                            <div className="text-sm text-gray-700">a^(-n) = 1/a^n.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'rational' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Rational exponents</div>
                            <div className="text-sm text-gray-700">a^(m/n) means an nth root: a^(m/n) = (n√a)^m.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Examples</div>
                            <div className="text-sm text-gray-700">x^(1/2) = √x and x^(3/2) = (√x)^3.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'equations' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800">Equating exponents</div>
                            <div className="text-sm text-gray-700">If a^x = a^k (a &gt; 0, a ≠ 1), then x = k.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default ExponentsVisualAids;
