import React from 'react';
import { renderMathText } from '../../../../../utils/renderMathText.jsx';

const tabClass = (active) => (
    `px-3 py-2 rounded-lg text-sm font-semibold border ${active ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-800 border-indigo-200 hover:bg-indigo-50'}`
);

export const Grade12TrigonometryVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    const tab = visualAidsTab || 'reduction';

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
                <button className={tabClass(tab === 'reduction')} onClick={() => setVisualAidsTab('reduction')}>Reduction</button>
                <button className={tabClass(tab === 'special')} onClick={() => setVisualAidsTab('special')}>Special angles</button>
                <button className={tabClass(tab === 'identities')} onClick={() => setVisualAidsTab('identities')}>Identities</button>
                <button className={tabClass(tab === 'compound')} onClick={() => setVisualAidsTab('compound')}>Compound angles</button>
            </div>

            {tab === 'reduction' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">CAST signs</div>
                        <div className="text-sm text-gray-700">Q1: all positive</div>
                        <div className="text-sm text-gray-700">Q2: sin positive</div>
                        <div className="text-sm text-gray-700">Q3: tan positive</div>
                        <div className="text-sm text-gray-700">Q4: cos positive</div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Negative angles</div>
                        <div className="text-sm text-gray-700">{renderMathText('sin(-\\theta)=-sin\\theta')}</div>
                        <div className="text-sm text-gray-700">{renderMathText('cos(-\\theta)=cos\\theta')}</div>
                        <div className="text-sm text-gray-700">{renderMathText('tan(-\\theta)=-tan\\theta')}</div>
                    </div>
                </div>
            )}

            {tab === 'special' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Special angles (exact)</div>
                        <div className="text-sm text-gray-700">{renderMathText('sin30^\\circ=1/2,\\; cos30^\\circ=\\sqrt{3}/2')}</div>
                        <div className="text-sm text-gray-700">{renderMathText('sin45^\\circ=1/\\sqrt{2},\\; cos45^\\circ=1/\\sqrt{2},\\; tan45^\\circ=1')}</div>
                        <div className="text-sm text-gray-700">{renderMathText('sin60^\\circ=\\sqrt{3}/2,\\; cos60^\\circ=1/2')}</div>
                    </div>
                </div>
            )}

            {tab === 'identities' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Core identities</div>
                        <div className="text-sm text-gray-700">{renderMathText('tan\\theta=\\dfrac{sin\\theta}{cos\\theta}\\; (cos\\theta\\neq 0)')}</div>
                        <div className="text-sm text-gray-700">{renderMathText('sin^2\\theta+cos^2\\theta=1')}</div>
                        <div className="text-sm text-gray-700">{renderMathText('1-sin^2\\theta=cos^2\\theta')}</div>
                    </div>
                </div>
            )}

            {tab === 'compound' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-lg p-3">
                        <div className="text-sm font-semibold text-gray-800 mb-2">Compound angle formulae</div>
                        <div className="text-sm text-gray-700">{renderMathText('cos(\\alpha-\\beta)=cos\\alpha cos\\beta+sin\\alpha sin\\beta')}</div>
                        <div className="text-sm text-gray-700">{renderMathText('cos(\\alpha+\\beta)=cos\\alpha cos\\beta-sin\\alpha sin\\beta')}</div>
                        <div className="text-sm text-gray-700">{renderMathText('sin(\\alpha-\\beta)=sin\\alpha cos\\beta-cos\\alpha sin\\beta')}</div>
                        <div className="text-sm text-gray-700">{renderMathText('sin(\\alpha+\\beta)=sin\\alpha cos\\beta+cos\\alpha sin\\beta')}</div>
                    </div>
                </div>
            )}
        </div>
    );
};
