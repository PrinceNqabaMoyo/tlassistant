import React from 'react';
import { X } from 'lucide-react';

const IntegersVisualAids = ({
    visualAidsTab,
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = [
        { key: 'number_line', label: 'Number Line' },
        { key: 'rules', label: 'Rules' },
    ];

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
                {visualAidsTab === 'number_line' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="font-semibold text-gray-900 mb-1">Number line idea</div>
                            <div className="text-sm text-gray-700">Moving right increases the number. Moving left decreases the number. Negative numbers are left of 0.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="font-semibold text-gray-900 mb-1">Compare</div>
                            <div className="text-sm text-gray-700">Example: −3 &gt; −7 because −3 is closer to 0 (further right).</div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'rules' && (
                    <div className="space-y-3">
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="font-semibold text-gray-900 mb-1">Add/Subtract</div>
                            <div className="text-sm text-gray-700">Subtracting a number = adding its opposite. Example: 5 − (−2) = 5 + 2.</div>
                        </div>
                        <div className="bg-white border border-gray-200 rounded-lg p-4">
                            <div className="font-semibold text-gray-900 mb-1">Multiply/Divide signs</div>
                            <div className="text-sm text-gray-700">Same signs → positive. Different signs → negative.</div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default IntegersVisualAids;
