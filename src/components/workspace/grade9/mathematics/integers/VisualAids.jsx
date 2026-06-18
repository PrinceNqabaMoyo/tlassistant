import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const IntegersVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'rules', label: 'Sign rules' },
            { key: 'properties', label: 'Properties' },
            { key: 'distributive', label: 'Distributive' },
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
                {visualAidsTab === 'rules' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Addition/Subtraction</div>
                            <div className="text-sm text-gray-700">Subtracting a number is adding its opposite: a − (−b) = a + b.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Multiply/Divide signs</div>
                            <div className="text-sm text-gray-700">Same signs → positive. Different signs → negative.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'properties' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Commutative</div>
                            <div className="text-sm text-gray-700">a + b = b + a and ab = ba.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Associative</div>
                            <div className="text-sm text-gray-700">(a + b) + c = a + (b + c) and (ab)c = a(bc).</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Inverses</div>
                            <div className="text-sm text-gray-700">Additive inverse: a + (−a) = 0. Multiplicative inverse exists for ±1 in integers.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'distributive' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Distributive property</div>
                            <div className="text-sm text-gray-700">a(b + c) = ab + ac and a(b − c) = ab − ac.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Tip</div>
                            <div className="text-sm text-gray-700">Keep brackets until you distribute. Then simplify carefully with signs.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default IntegersVisualAids;
