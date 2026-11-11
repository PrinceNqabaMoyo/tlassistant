import React, { useState } from 'react';
import MathText from '../shared/mathx/MathText';
import MathAnswerArea from '../shared/mathx/MathAnswerArea';
import { Dna, Sparkles } from 'lucide-react';

export default function PunnettSquareModalityRenderer({
    question,
    topic,
    onCheck,
    result,
    isChecking,
    showDynamicScaffold,
    onToggleScaffold,
}) {
    if (!question) return null;

    const spec = question.punnett_spec || {};
    const p1Label = spec.p1_label || 'Parent 1 (Bb)';
    const p2Label = spec.p2_label || 'Parent 2 (Bb)';
    const p1Gametes = spec.p1_gametes || ['B', 'b'];
    const p2Gametes = spec.p2_gametes || ['B', 'b'];
    const expectedCells = spec.expected_cells || ['BB', 'Bb', 'Bb', 'bb'];
    const phenoRatio = spec.phenotype_ratio || '3:1';

    const [userCells, setUserCells] = useState({
        cell_0_0: '',
        cell_0_1: '',
        cell_1_0: '',
        cell_1_1: '',
    });

    const handleCellChange = (key, val) => {
        setUserCells(prev => ({ ...prev, [key]: val }));
    };

    return (
        <div className="space-y-6">
            {/* Punnett Square Visual Card */}
            <div 
                data-testid="punnett-square-canvas" 
                className="p-4 sm:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs space-y-4 font-sans"
            >
                <div className="flex items-center justify-between border-b border-slate-100 pb-2">
                    <div className="flex items-center gap-2">
                        <span className="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs font-bold shadow-2xs">
                            <Dna className="w-3.5 h-3.5" />
                        </span>
                        <span className="text-xs font-bold text-slate-800 uppercase tracking-wide">
                            Genetic Cross Diagram (Punnett Square)
                        </span>
                    </div>
                    <span className="text-[11px] font-mono text-emerald-700 font-semibold bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded">
                        Ratio: {phenoRatio}
                    </span>
                </div>

                {/* Parental Cross Summary */}
                <div className="grid grid-cols-2 gap-3 text-xs bg-slate-50 p-3 rounded-xl border border-slate-200/80">
                    <div>
                        <span className="text-slate-500 font-semibold">Female Gametes (P1):</span>
                        <p className="font-bold text-slate-800 font-mono mt-0.5">{p1Label}</p>
                    </div>
                    <div>
                        <span className="text-slate-500 font-semibold">Male Gametes (P2):</span>
                        <p className="font-bold text-slate-800 font-mono mt-0.5">{p2Label}</p>
                    </div>
                </div>

                {/* 2x2 Interactive Punnett Table */}
                <div className="flex justify-center my-2">
                    <div className="inline-block bg-white p-3 rounded-xl border border-slate-200 shadow-2xs">
                        <table className="border-collapse text-center font-mono">
                            <thead>
                                <tr>
                                    <th className="p-2 border border-slate-200 bg-slate-100/80 text-[11px] text-slate-500 font-semibold">
                                        ♀ \ ♂
                                    </th>
                                    <th className="p-2 w-16 border border-slate-200 bg-blue-50 text-blue-800 font-bold text-sm">
                                        {p2Gametes[0] || 'B'}
                                    </th>
                                    <th className="p-2 w-16 border border-slate-200 bg-blue-50 text-blue-800 font-bold text-sm">
                                        {p2Gametes[1] || 'b'}
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th className="p-2 h-14 border border-slate-200 bg-purple-50 text-purple-800 font-bold text-sm">
                                        {p1Gametes[0] || 'B'}
                                    </th>
                                    <td className="p-2 border border-slate-200 bg-emerald-50/50 hover:bg-emerald-50 transition">
                                        <div className="font-bold text-base text-slate-800">
                                            {expectedCells[0] || 'BB'}
                                        </div>
                                    </td>
                                    <td className="p-2 border border-slate-200 bg-emerald-50/50 hover:bg-emerald-50 transition">
                                        <div className="font-bold text-base text-slate-800">
                                            {expectedCells[1] || 'Bb'}
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <th className="p-2 h-14 border border-slate-200 bg-purple-50 text-purple-800 font-bold text-sm">
                                        {p1Gametes[1] || 'b'}
                                    </th>
                                    <td className="p-2 border border-slate-200 bg-emerald-50/50 hover:bg-emerald-50 transition">
                                        <div className="font-bold text-base text-slate-800">
                                            {expectedCells[2] || 'Bb'}
                                        </div>
                                    </td>
                                    <td className="p-2 border border-slate-200 bg-emerald-50/50 hover:bg-emerald-50 transition">
                                        <div className="font-bold text-base text-slate-800">
                                            {expectedCells[3] || 'bb'}
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div className="text-[11px] text-slate-500 text-center font-sans">
                    Offspring genotypes formed through random fertilisation during sexual reproduction.
                </div>
            </div>

            {/* Answer Area (Phenotypic Ratio & Probability calculation) */}
            <MathAnswerArea
                question={question}
                topic={topic}
                onCheck={onCheck}
                result={result}
                busy={isChecking}
            />
        </div>
    );
}
