import React from 'react';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

const tabClass = (active) => (
    `px-3 py-2 rounded-lg text-sm font-semibold border ${active ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-800 border-indigo-200 hover:bg-indigo-50'}`
);

export const Grade12FunctionsVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    const tab = visualAidsTab || 'inverses';

    return (
        <div className="p-3">
            <div className="flex items-center justify-between mb-3">
                <div className="text-sm font-bold text-gray-900">Visual Aids</div>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="px-2 py-1 text-xs bg-gray-100 hover:bg-gray-200 rounded"
                >
                    Close
                </button>
            </div>

            <div className="flex flex-wrap gap-2 mb-4">
                <button className={tabClass(tab === 'inverses')} onClick={() => setVisualAidsTab('inverses')}>Inverses</button>
                <button className={tabClass(tab === 'exponentials')} onClick={() => setVisualAidsTab('exponentials')}>Exp/Log</button>
                <button className={tabClass(tab === 'laws')} onClick={() => setVisualAidsTab('laws')}>Log Laws</button>
            </div>

            {tab === 'inverses' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Linear inverse</div>
                        <div className="text-sm text-gray-700">{renderMathText('If f(x) = ax + q, then f^{-1}(x) = (x - q)/a')}</div>
                        <div className="text-sm text-gray-700 mt-1">{renderMathText('Graph of f and f^{-1} are reflected in y = x')}</div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Intercept swap</div>
                        <div className="text-sm text-gray-700">{renderMathText('If (x_0; y_0) lies on f, then (y_0; x_0) lies on f^{-1}')}</div>
                    </div>
                </div>
            )}

            {tab === 'exponentials' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Conversion</div>
                        <div className="text-sm text-gray-700">{renderMathText('x = b^y \u21d4 y = log_b x')}</div>
                        <div className="text-sm text-gray-700 mt-1">{renderMathText('log x means log_{10} x')}</div>
                        <div className="text-sm text-gray-700 mt-1">{renderMathText('ln x means log_e x')}</div>
                    </div>
                </div>
            )}

            {tab === 'laws' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Power rule</div>
                        <div className="text-sm text-gray-700">{renderMathText('log_a(x^b) = b\u00b7log_a(x)')}</div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Change of base</div>
                        <div className="text-sm text-gray-700">{renderMathText('log_a x = (log_b x)/(log_b a)')}</div>
                    </div>
                </div>
            )}
        </div>
    );
};
