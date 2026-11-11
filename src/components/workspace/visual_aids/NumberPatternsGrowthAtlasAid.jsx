import React, { useState, useMemo } from 'react';
import { Grid, Sliders, BookOpen, Layers, TrendingUp } from 'lucide-react';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import MathText from '../shared/mathx/MathText';

/**
 * NumberPatternsGrowthAtlasAid
 * ----------------------------
 * Implements the Mathematics Dual-Capacity Standard (diagram_doctrine.md §2.3):
 * - Mode 1 (Annotated Master Atlas): Decomposition table showing Stage n, Term Value T_n,
 *   Constant Core vs. Growing Perimeter, First Difference Δ₁, and Constant Second Difference Δ₂ = 2a.
 * - Mode 2 (Live Interactive Growth Scrubber): Interactive stage slider (n = 1..10) for
 *   Linear (T_n = dn + c) and Quadratic (T_n = an² + bn + c) geometric patterns (tiles & matchsticks),
 *   highlighting newly added elements in contrasting ink and plotting (n, T_n) on a synchronized
 *   Cartesian sequence plot.
 */

const PATTERN_PRESETS = [
  {
    id: 'quadratic_tiles',
    kind: 'quadratic',
    label: 'Quadratic Tile Array (Tₙ = n² + 2n + 1)',
    grades: 'Grades 10–12 Quadratic Patterns',
    a: 1,
    b: 2,
    c: 1,
    desc: 'An (n + 1) × (n + 1) square array decomposed into an n × n inner core, two 1 × n border arms, and 1 corner tile.',
  },
  {
    id: 'linear_matchsticks',
    kind: 'linear',
    label: 'Linear Matchstick Houses (Tₙ = 3n + 1)',
    grades: 'Grades 7–10 Linear Patterns',
    a: 0,
    b: 3,
    c: 1,
    desc: '1 fixed starter matchstick on the left plus 3 new matchsticks added for every stage n.',
  },
  {
    id: 'quadratic_dots',
    kind: 'quadratic',
    label: 'Triangular-Plus-Border Dots (Tₙ = 2n² + n)',
    grades: 'Grades 11–12 Quadratic Sequences',
    a: 2,
    b: 1,
    c: 0,
    desc: 'Constant second difference Δ₂ = 2a = 4, demonstrating quadratic sequence acceleration.',
  },
];

export default function NumberPatternsGrowthAtlasAid({ initialPreset = 'quadratic_tiles' }) {
  const [presetId, setPresetId] = useState(
    PATTERN_PRESETS.some((p) => p.id === initialPreset) ? initialPreset : 'quadratic_tiles'
  );
  const [viewMode, setViewMode] = useState('simulation'); // 'atlas' | 'simulation'
  const [stageN, setStageN] = useState(4);
  const [selectedCalcId, setSelectedCalcId] = useState('nth_term');

  const preset = PATTERN_PRESETS.find((p) => p.id === presetId) || PATTERN_PRESETS[0];
  const { a, b, c, kind } = preset;

  const evalTerm = (n) => a * n * n + b * n + c;

  // Sequence terms for n = 1..10
  const sequenceTerms = useMemo(() => {
    const list = [];
    for (let n = 1; n <= 10; n++) {
      const tn = evalTerm(n);
      const prev = n > 1 ? evalTerm(n - 1) : null;
      const d1 = prev !== null ? tn - prev : null;
      const prevD1 = n > 2 ? evalTerm(n - 1) - evalTerm(n - 2) : null;
      const d2 = d1 !== null && prevD1 !== null ? d1 - prevD1 : null;
      list.push({ n, tn, d1, d2 });
    }
    return list;
  }, [a, b, c]);

  const currentTerm = evalTerm(stageN);
  const prevTerm = stageN > 1 ? evalTerm(stageN - 1) : 0;
  const addedThisStage = stageN > 1 ? currentTerm - prevTerm : currentTerm;
  const firstDiffAtN = evalTerm(stageN + 1) - currentTerm;
  const secondDiff = 2 * a;

  const calculationsMap = useMemo(() => {
    if (kind === 'linear') {
      return {
        nth_term: {
          id: 'nth_term',
          shortLabel: `General Term Tₙ (n=${stageN})`,
          label: `Linear Sequence General Term at Stage n = ${stageN}`,
          color: '#2B5B84',
          badgeText: `T_${stageN} = ${currentTerm}`,
          formula: 'T_n = dn + c \\quad (d = T_2 - T_1)',
          substitution: `T_{${stageN}} = ${b}(${stageN}) + ${c}`,
          result: `T_{${stageN}} = ${currentTerm} \\quad (\\text{Constant } \\Delta_1 = ${b})`,
          meaning: `Every step n adds a constant perimeter increment of d = ${b} elements around the fixed starter core of c = ${c}.`,
        },
        first_diff: {
          id: 'first_diff',
          shortLabel: `Constant 1st Diff (d=${b})`,
          label: 'Constant First Difference & Linear Gradient',
          color: '#D97706',
          badgeText: `Δ₁ = ${b}`,
          formula: '\\Delta_1 = T_{n+1} - T_n = d',
          substitution: `T_{${stageN + 1}} - T_{${stageN}} = ${evalTerm(stageN + 1)} - ${currentTerm}`,
          result: `\\Delta_1 = ${b}`,
          meaning: 'Because the first difference Δ₁ is constant, plotting (n; Tₙ) produces collinear points along a straight line of gradient d.',
        },
      };
    }

    return {
      nth_term: {
        id: 'nth_term',
        shortLabel: `General Term Tₙ (n=${stageN})`,
        label: `Quadratic General Term Decomposition at Stage n = ${stageN}`,
        color: '#2B5B84',
        badgeText: `T_${stageN} = ${currentTerm}`,
        formula: 'T_n = an^2 + bn + c',
        substitution: `T_{${stageN}} = ${a}(${stageN})^2 + ${b}(${stageN}) + ${c}`,
        result: `T_{${stageN}} = ${a * stageN * stageN} \\text{ (core)} + ${b * stageN} \\text{ (arms)} + ${c} \\text{ (unit)} = ${currentTerm}`,
        meaning:
          'Decomposing the pattern into an n² quadratic core (blue), bn linear arms (amber), and c constant corner units (emerald) reveals why the algebraic formula is Tₙ = an² + bn + c.',
      },
      second_diff: {
        id: 'second_diff',
        shortLabel: `2nd Difference (2a=${secondDiff})`,
        label: 'Constant Second Difference & Parameter Identification',
        color: '#D97706',
        badgeText: `Δ₂ = 2a = ${secondDiff}`,
        formula: '2a = \\Delta_2, \\quad 3a + b = T_2 - T_1, \\quad a + b + c = T_1',
        substitution: `2a = ${secondDiff} \\implies a = ${a}, \\quad 3(${a}) + b = ${evalTerm(2) - evalTerm(1)} \\implies b = ${b}`,
        result: `a = ${a}, \\; b = ${b}, \\; c = ${c}`,
        meaning: `Between Stage ${stageN - 1 || 1} and Stage ${stageN}, ${addedThisStage} new elements were added. The first difference grows by Δ₂ = ${secondDiff} at every consecutive stage.`,
      },
    };
  }, [kind, stageN, currentTerm, b, c, a, secondDiff, addedThisStage]);

  const activeCalc = calculationsMap[selectedCalcId] || Object.values(calculationsMap)[0];

  // SVG Synchronized Plot coordinates
  const W = 580;
  const H = 250;
  const maxT = evalTerm(10);
  const toPlotX = (n) => 45 + ((n - 1) / 9) * (W - 75);
  const toPlotY = (t) => H - 30 - (t / Math.max(10, maxT)) * (H - 55);

  return (
    <div
      data-testid="number-patterns-growth-atlas-aid"
      className="space-y-3.5 text-slate-800 font-sans"
    >
      {/* Top Header & Controls */}
      <div className="bg-[#FAF8F3] rounded-xl border border-[#EAE5DC] p-3.5 shadow-2xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-amber-100 text-amber-900 uppercase tracking-wider">
              {preset.grades} • Visual Pattern Decomposition
            </span>
            <h4 className="text-sm font-bold text-[#1E2022] mt-1">
              {preset.label}
            </h4>
          </div>

          <div className="flex items-center gap-1.5 bg-white p-1 rounded-lg border border-[#EAE5DC]">
            <button
              type="button"
              data-testid="btn-pattern-mode-atlas"
              onClick={() => setViewMode('atlas')}
              className={`px-2.5 py-1 rounded-md text-xs font-bold flex items-center gap-1 transition cursor-pointer ${
                viewMode === 'atlas'
                  ? 'bg-[#13519C] text-white shadow-2xs'
                  : 'text-slate-600 hover:bg-slate-100'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Difference Table Atlas</span>
            </button>
            <button
              type="button"
              data-testid="btn-pattern-mode-simulation"
              onClick={() => setViewMode('simulation')}
              className={`px-2.5 py-1 rounded-md text-xs font-bold flex items-center gap-1 transition cursor-pointer ${
                viewMode === 'simulation'
                  ? 'bg-[#13519C] text-white shadow-2xs'
                  : 'text-slate-600 hover:bg-slate-100'
              }`}
            >
              <Sliders className="w-3.5 h-3.5" />
              <span>Interactive Stage Scrubber</span>
            </button>
          </div>
        </div>

        {/* Pattern Preset Buttons */}
        <div className="flex flex-wrap items-center gap-1.5 pt-1 border-t border-[#EAE5DC]">
          {PATTERN_PRESETS.map((pItem) => (
            <button
              key={pItem.id}
              type="button"
              data-testid={`btn-preset-${pItem.id}`}
              onClick={() => {
                setPresetId(pItem.id);
                setSelectedCalcId('nth_term');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition cursor-pointer border ${
                presetId === pItem.id
                  ? 'bg-[#2B5B84] text-white border-[#2B5B84]'
                  : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'
              }`}
            >
              {pItem.label}
            </button>
          ))}
        </div>

        {/* Stage Scrubber Slider (n = 1..10) */}
        <label className="bg-white p-3 rounded-xl border border-[#EAE5DC] flex flex-col gap-1.5">
          <div className="flex items-center justify-between text-xs font-semibold text-slate-700">
            <span className="flex items-center gap-1.5">
              <Grid className="w-3.5 h-3.5 text-[#13519C]" />
              <span>Scrub Pattern Stage Index (n = 1 … 10)</span>
            </span>
            <span className="font-mono font-bold text-[#13519C]">
              Stage n = {stageN} → T_{stageN} = {currentTerm} (+{addedThisStage} new elements)
            </span>
          </div>
          <input
            type="range"
            data-testid="slider-pattern-stage-n"
            min="1"
            max="10"
            step="1"
            value={stageN}
            onChange={(e) => setStageN(parseInt(e.target.value, 10))}
            className="w-full accent-[#13519C] cursor-pointer h-1.5"
          />
        </label>
      </div>

      {/* Visual Decomposition Canvas + Synchronized Sequence Graph */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-3">
        {/* Left Card: Structural Geometric Decomposition (Core vs Perimeter) */}
        <div className="bg-white rounded-xl border border-[#EAE5DC] p-3.5 shadow-xs space-y-2">
          <div className="flex items-center justify-between text-xs border-b border-slate-100 pb-2">
            <span className="font-bold text-[#1E2022] flex items-center gap-1.5">
              <Layers className="w-3.5 h-3.5 text-[#13519C]" />
              <span>Stage n = {stageN} Structural Decomposition</span>
            </span>
            <span className="font-mono text-[11px] font-bold text-slate-600">
              Total = {currentTerm}
            </span>
          </div>

          <svg
            viewBox="0 0 280 220"
            data-testid="pattern-geometric-svg"
            className="w-full h-auto bg-[#FAF8F3] rounded-lg border border-[#EAE5DC]"
          >
            {kind === 'quadratic' ? (
              (() => {
                // Draw (n+1) x (n+1) or n x n decomposition grid capped visually at n <= 7
                const visN = Math.min(stageN, 7);
                const cellSize = Math.min(24, Math.floor(170 / (visN + 1)));
                const startX = 24;
                const startY = 22;
                const items = [];
                for (let r = 0; r < visN; r++) {
                  for (let col = 0; col < visN; col++) {
                    const isNewOuterLayer = r === visN - 1 || col === visN - 1;
                    items.push(
                      <rect
                        key={`core-${r}-${col}`}
                        x={startX + col * (cellSize + 3)}
                        y={startY + r * (cellSize + 3)}
                        width={cellSize}
                        height={cellSize}
                        rx="3"
                        fill={isNewOuterLayer ? '#D97706' : '#2B5B84'}
                        opacity={isNewOuterLayer ? 0.95 : 0.85}
                      />
                    );
                  }
                }
                // Linear bn arms
                for (let arm = 0; arm < visN; arm++) {
                  items.push(
                    <rect
                      key={`arm-r-${arm}`}
                      x={startX + visN * (cellSize + 3) + 4}
                      y={startY + arm * (cellSize + 3)}
                      width={cellSize * 0.75}
                      height={cellSize}
                      rx="3"
                      fill="#059669"
                    />
                  );
                }
                return (
                  <g>
                    {items}
                    <text x="16" y="208" fontSize="9.5" fontWeight="bold" fill="#2B5B84">
                      ■ Inner Core ({a}n² = {a * stageN * stageN})
                    </text>
                    <text x="148" y="208" fontSize="9.5" fontWeight="bold" fill="#D97706">
                      ■ New Stage Increment (+{addedThisStage})
                    </text>
                  </g>
                );
              })()
            ) : (
              (() => {
                // Linear Matchstick pattern
                const visN = Math.min(stageN, 7);
                const stepW = Math.min(32, Math.floor(230 / visN));
                const sticks = [];
                for (let k = 0; k < visN; k++) {
                  const xLeft = 24 + k * stepW;
                  const isNewest = k === visN - 1;
                  const strokeCol = isNewest ? '#D97706' : '#2B5B84';
                  sticks.push(
                    <g key={`house-${k}`}>
                      <line x1={xLeft} y1={75} x2={xLeft + stepW} y2={75} stroke={strokeCol} strokeWidth="3.5" strokeLinecap="round" />
                      <line x1={xLeft} y1={135} x2={xLeft + stepW} y2={135} stroke={strokeCol} strokeWidth="3.5" strokeLinecap="round" />
                      <line x1={xLeft + stepW} y1={75} x2={xLeft + stepW} y2={135} stroke={strokeCol} strokeWidth="3.5" strokeLinecap="round" />
                    </g>
                  );
                }
                return (
                  <g>
                    {/* Fixed starter matchstick c = 1 */}
                    <line x1={24} y1={75} x2={24} y2={135} stroke="#059669" strokeWidth="4.5" strokeLinecap="round" />
                    {sticks}
                    <text x="16" y="195" fontSize="9.5" fontWeight="bold" fill="#059669">
                      ■ Starter Core (c = {c})
                    </text>
                    <text x="135" y="195" fontSize="9.5" fontWeight="bold" fill="#D97706">
                      ■ Stage {stageN} Increment (+{b})
                    </text>
                  </g>
                );
              })()
            )}
          </svg>
        </div>

        {/* Right Card: Synchronized (n, T_n) Sequence Plot OR Difference Table Atlas */}
        <div className="bg-white rounded-xl border border-[#EAE5DC] p-3.5 shadow-xs space-y-2">
          <div className="flex items-center justify-between text-xs border-b border-slate-100 pb-2">
            <span className="font-bold text-[#1E2022] flex items-center gap-1.5">
              <TrendingUp className="w-3.5 h-3.5 text-[#13519C]" />
              <span>
                {viewMode === 'atlas'
                  ? 'First & Second Finite Differences Table (Δ₁ & Δ₂)'
                  : 'Synchronized Sequence Plot (n; Tₙ)'}
              </span>
            </span>
            <span className="font-mono text-[11px] text-emerald-700 font-bold">
              Δ₁ = {firstDiffAtN} {kind === 'quadratic' ? `• Δ₂ = ${secondDiff}` : ''}
            </span>
          </div>

          {viewMode === 'atlas' ? (
            <div data-testid="pattern-difference-table" className="overflow-x-auto">
              <table className="w-full text-xs font-mono border-collapse">
                <thead>
                  <tr className="bg-slate-100 text-slate-700 border-b border-slate-200">
                    <th className="py-1.5 px-2 text-left">Stage (n)</th>
                    {sequenceTerms.slice(0, 6).map((item) => (
                      <th
                        key={item.n}
                        className={`py-1.5 px-2 text-center ${
                          item.n === stageN ? 'bg-indigo-100 text-[#13519C] font-bold' : ''
                        }`}
                      >
                        n={item.n}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  <tr>
                    <td className="py-1.5 px-2 font-bold text-slate-800">Term (Tₙ)</td>
                    {sequenceTerms.slice(0, 6).map((item) => (
                      <td
                        key={item.n}
                        className={`py-1.5 px-2 text-center font-bold ${
                          item.n === stageN ? 'bg-indigo-50 text-[#13519C]' : 'text-slate-800'
                        }`}
                      >
                        {item.tn}
                      </td>
                    ))}
                  </tr>
                  <tr>
                    <td className="py-1.5 px-2 font-semibold text-amber-800">1st Diff (Δ₁)</td>
                    {sequenceTerms.slice(0, 6).map((item) => (
                      <td key={item.n} className="py-1.5 px-2 text-center text-amber-700 font-semibold">
                        {item.d1 !== null ? `+${item.d1}` : '—'}
                      </td>
                    ))}
                  </tr>
                  {kind === 'quadratic' && (
                    <tr>
                      <td className="py-1.5 px-2 font-semibold text-emerald-800">2nd Diff (Δ₂=2a)</td>
                      {sequenceTerms.slice(0, 6).map((item) => (
                        <td key={item.n} className="py-1.5 px-2 text-center text-emerald-700 font-bold">
                          {item.d2 !== null ? `+${item.d2}` : '—'}
                        </td>
                      ))}
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          ) : (
            <svg
              viewBox={`0 0 ${W} ${H}`}
              data-testid="pattern-sequence-plot-svg"
              className="w-full h-auto bg-[#FAF8F3] rounded-lg border border-[#EAE5DC]"
            >
              {/* Axes */}
              <line x1={40} y1={15} x2={40} y2={H - 28} stroke="#1E2022" strokeWidth="1.5" />
              <line x1={40} y1={H - 28} x2={W - 20} y2={H - 28} stroke="#1E2022" strokeWidth="1.5" />
              <text x={W - 45} y={H - 8} fontSize="10" fontWeight="bold" fill="#1E2022">
                Stage n
              </text>
              <text x={12} y={24} fontSize="10" fontWeight="bold" fill="#1E2022">
                Tₙ
              </text>

              {/* Dashed interpolation curve */}
              <path
                d={sequenceTerms
                  .map((pt, i) => `${i === 0 ? 'M' : 'L'} ${toPlotX(pt.n).toFixed(1)} ${toPlotY(pt.tn).toFixed(1)}`)
                  .join(' ')}
                fill="none"
                stroke="#94A3B8"
                strokeWidth="1.8"
                strokeDasharray="4 4"
              />

              {/* Discrete Sequence Points (n, T_n) */}
              {sequenceTerms.map((pt) => {
                const isActive = pt.n === stageN;
                return (
                  <g key={`pt-${pt.n}`}>
                    <circle
                      cx={toPlotX(pt.n)}
                      cy={toPlotY(pt.tn)}
                      r={isActive ? 6.5 : 4.2}
                      fill={isActive ? '#D97706' : '#13519C'}
                      stroke="#FFFFFF"
                      strokeWidth="1.5"
                    />
                    <text
                      x={toPlotX(pt.n)}
                      y={H - 14}
                      textAnchor="middle"
                      fontSize="9.5"
                      fontFamily="monospace"
                      fill="#475569"
                    >
                      {pt.n}
                    </text>
                    {isActive && (
                      <text
                        x={toPlotX(pt.n)}
                        y={toPlotY(pt.tn) - 10}
                        textAnchor="middle"
                        fontSize="10.5"
                        fontWeight="bold"
                        fontFamily="monospace"
                        fill="#B45309"
                      >
                        ({pt.n}; {pt.tn})
                      </text>
                    )}
                  </g>
                );
              })}
            </svg>
          )}
        </div>
      </div>

      {/* Live Formula & Substitution Breakdown Card */}
      <CalculationPopoverCard
        calculation={activeCalc}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedCalcId}
      />
    </div>
  );
}
