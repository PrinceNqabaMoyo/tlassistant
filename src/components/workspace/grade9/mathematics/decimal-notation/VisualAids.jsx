import React, { useMemo } from 'react';
import { X } from 'lucide-react';

const DecimalNotationVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = useMemo(
        () => [
            { key: 'equivalents', label: 'Equivalents' },
            { key: 'operations', label: 'Operations' },
            { key: 'division', label: 'Division' },
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
                {visualAidsTab === 'equivalents' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Fractions, decimals, percentages</div>
                            <div className="text-sm text-gray-700">Decimals and common fractions can represent the same value. Percent means “per 100”.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'operations' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Add/Subtract</div>
                            <div className="text-sm text-gray-700">Line up decimal points. Add/subtract tenths with tenths, hundredths with hundredths, etc.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Multiply</div>
                            <div className="text-sm text-gray-700">Multiply as whole numbers, then place the decimal using the total number of decimal places.</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'division' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="text-sm font-semibold text-gray-800 mb-1">Divide decimals</div>
                            <div className="text-sm text-gray-700">Multiply numerator and denominator by the smallest power of 10 that makes the divisor a whole number.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default DecimalNotationVisualAids;
