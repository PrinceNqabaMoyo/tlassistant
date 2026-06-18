import React from 'react';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

const tabClass = (active) => (
    `px-3 py-2 rounded-lg text-sm font-semibold border ${active ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-800 border-indigo-200 hover:bg-indigo-50'}`
);

export const Grade12PatternsSequencesSeriesVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    const tab = visualAidsTab || 'sequences';

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
                <button className={tabClass(tab === 'sequences')} onClick={() => setVisualAidsTab('sequences')}>Sequences</button>
                <button className={tabClass(tab === 'series')} onClick={() => setVisualAidsTab('series')}>Series</button>
                <button className={tabClass(tab === 'sigma')} onClick={() => setVisualAidsTab('sigma')}>Sigma</button>
            </div>

            {tab === 'sequences' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Arithmetic sequence</div>
                        <div className="text-sm text-gray-700">{renderMathText('Common difference: d = T_2 - T_1')}</div>
                        <div className="text-sm text-gray-700 mt-1">{renderMathText('General term: T_n = a + (n - 1)d')}</div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Geometric sequence</div>
                        <div className="text-sm text-gray-700">{renderMathText('Constant ratio: r = T_2 / T_1')}</div>
                        <div className="text-sm text-gray-700 mt-1">{renderMathText('General term: T_n = a r^(n - 1)')}</div>
                    </div>
                </div>
            )}

            {tab === 'series' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Arithmetic series (finite)</div>
                        <div className="text-sm text-gray-700">{renderMathText('S_n = n/2 [2a + (n - 1)d]')}</div>
                        <div className="text-sm text-gray-700 mt-1">{renderMathText('Also: S_n = n/2 (a + l) where l = T_n')}</div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Geometric series (finite)</div>
                        <div className="text-sm text-gray-700">{renderMathText('S_n = a(1 - r^n)/(1 - r) (r ≠ 1)')}</div>
                        <div className="text-sm text-gray-700 mt-1">{renderMathText('Equivalent: S_n = a(r^n - 1)/(r - 1)')}</div>
                    </div>
                </div>
            )}

            {tab === 'sigma' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Sigma notation</div>
                        <div className="text-sm text-gray-700">{renderMathText('Σ(k=m to n) [T_k] means T_m + T_(m+1) + ... + T_n')}</div>
                        <div className="text-sm text-gray-700 mt-1">{renderMathText('Example: Σ(k=1 to 4) [k] = 1 + 2 + 3 + 4')}</div>
                    </div>
                </div>
            )}
        </div>
    );
};
