import React from 'react';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

const tabClass = (active) => (
    `px-3 py-2 rounded-lg text-sm font-semibold border ${active ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-800 border-indigo-200 hover:bg-indigo-50'}`
);

export const Grade12FinanceVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    const tab = visualAidsTab || 'growth';

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
                <button className={tabClass(tab === 'growth')} onClick={() => setVisualAidsTab('growth')}>Growth/Decay</button>
                <button className={tabClass(tab === 'rates')} onClick={() => setVisualAidsTab('rates')}>Nominal/Effective</button>
                <button className={tabClass(tab === 'annuities')} onClick={() => setVisualAidsTab('annuities')}>Annuities</button>
            </div>

            {tab === 'growth' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Compound growth</div>
                        <div className="text-sm text-gray-700">{renderMathText('A = P(1+i)^n')}</div>
                        <div className="text-sm text-gray-700 mt-1">{renderMathText('n = log(A/P) / log(1+i)')}</div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Compound decay</div>
                        <div className="text-sm text-gray-700">{renderMathText('A = P(1-i)^n')}</div>
                    </div>
                </div>
            )}

            {tab === 'rates' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Nominal to effective</div>
                        <div className="text-sm text-gray-700">{renderMathText('1+i = (1 + i^{(m)}/m)^m')}</div>
                        <div className="text-sm text-gray-700 mt-1">{renderMathText('i = (1 + i^{(m)}/m)^m - 1')}</div>
                    </div>
                </div>
            )}

            {tab === 'annuities' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Future value (annuity-immediate)</div>
                        <div className="text-sm text-gray-700">{renderMathText('F = x((1+i)^n - 1)/i')}</div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Solve for payment</div>
                        <div className="text-sm text-gray-700">{renderMathText('x = Fi/((1+i)^n - 1)')}</div>
                    </div>
                </div>
            )}
        </div>
    );
};
