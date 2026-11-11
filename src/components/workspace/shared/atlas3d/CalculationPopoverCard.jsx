import React from 'react';
import { Calculator, Sparkles, X, Info, ArrowRight } from 'lucide-react';
import MathText from '../mathx/MathText';

function ensureMathWrap(str) {
  if (!str) return '';
  const s = String(str).trim();
  if (s.includes('$')) return s;
  if (s.includes('\\') || s.includes('^') || s.includes('_') || s.includes('=')) {
    return `$${s}$`;
  }
  return s;
}

/**
 * CalculationPopoverCard
 *
 * Interactive calculation & physical-mechanism breakdown card for 3D Paper & Ink
 * Sidecar Visualization Tools.
 *
 * Whenever a learner clicks or hovers over a 3D vector, resistor, lattice bond,
 * particle chamber piston, or physiological structure, this card displays:
 *   1. Component / Vector Title & Symbol
 *   2. Authoritative Curriculum Formula (KaTeX)
 *   3. Live Numerical Substitution from current slider values
 *   4. Final Calculated Value with SI Units
 *   5. Micro-physical or physiological explanation ("Why this happens")
 */
export default function CalculationPopoverCard({
  item = null,
  calculation = null,
  allItems = [],
  allCalculations = [],
  onSelectItem,
  onSelectCalculation,
  onClear,
}) {
  const list = allCalculations.length > 0 ? allCalculations : allItems;
  const active = calculation || item || list[0] || null;
  const handleSelect = (entry) => {
    if (onSelectCalculation) onSelectCalculation(entry.id);
    if (onSelectItem) onSelectItem(entry);
  };

  if (!active) {
    return (
      <div
        data-testid="atlas-calc-popover-empty"
        className="p-3 rounded-xl bg-slate-50 border border-dashed border-slate-300 text-xs text-slate-500 flex items-center gap-2"
      >
        <Calculator className="w-4 h-4 text-[#13519C] shrink-0" />
        <span>
          Click any <strong>3D vector, component, or structure</strong> in the simulation (or select a pill below) to inspect its live curriculum formula and calculation.
        </span>
      </div>
    );
  }

  const mechanismText = active.mechanism || active.meaning || '';
  const badgeText = active.badge || active.badgeText || '';

  return (
    <div
      data-testid="atlas-calculation-popover"
      className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden transition-all"
    >
      {/* Quick-Select Pills for all inspectable parts/vectors in the scene */}
      {list.length > 0 && (
        <div className="px-3 py-2 bg-slate-50 border-b border-slate-200 flex items-center gap-1.5 overflow-x-auto">
          <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 shrink-0 mr-1 flex items-center gap-1">
            <Calculator className="w-3 h-3 text-[#13519C]" />
            Inspect:
          </span>
          {list.map((entry) => {
            const isSelected = active?.id === entry.id;
            return (
              <button
                key={entry.id}
                type="button"
                data-testid={`btn-calc-inspect-${entry.id}`}
                onClick={() => handleSelect(entry)}
                className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-[11px] font-semibold whitespace-nowrap transition-all border ${
                  isSelected
                    ? 'bg-[#13519C] text-white border-[#13519C] shadow-2xs'
                    : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-100'
                }`}
              >
                {entry.color && (
                  <span
                    className="w-2.5 h-2.5 rounded-full shrink-0 border border-white/50"
                    style={{ backgroundColor: entry.color }}
                  />
                )}
                <span>{entry.shortLabel || entry.badgeText || entry.label}</span>
              </button>
            );
          })}
        </div>
      )}

      {/* Active Calculation Breakdown Body */}
      <div className="p-3.5 space-y-2.5">
        <div className="flex items-start justify-between gap-2">
          <div className="flex items-center gap-2">
            {active.color && (
              <span
                className="w-3.5 h-3.5 rounded-md shrink-0 shadow-2xs"
                style={{ backgroundColor: active.color }}
              />
            )}
            <div>
              <div className="flex flex-wrap items-center gap-1.5">
                <h4
                  data-testid="calc-popover-label"
                  className="text-xs font-bold text-slate-900"
                >
                  {active.label}
                </h4>
                {badgeText && (
                  <span className="px-1.5 py-0.2 text-[10px] font-mono font-semibold rounded bg-indigo-50 text-indigo-700 border border-indigo-200">
                    {badgeText}
                  </span>
                )}
              </div>
              {active.subLabel && (
                <p className="text-[11px] text-slate-500">{active.subLabel}</p>
              )}
            </div>
          </div>

          <div className="flex items-center gap-2">
            {active.result && (
              <div
                data-testid="calc-popover-result"
                className="px-2.5 py-1 rounded-lg bg-emerald-50 border border-emerald-200 text-emerald-900 font-mono text-xs font-bold"
              >
                <MathText text={ensureMathWrap(active.result)} />
              </div>
            )}
            {onClear && (item || calculation) && (
              <button
                type="button"
                onClick={onClear}
                className="p-1 rounded-md text-slate-400 hover:text-slate-600 hover:bg-slate-100"
                title="Close inspection"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
          </div>
        </div>

        {/* Step-by-Step Formula -> Substitution -> Result Strip */}
        {(active.formula || active.substitution) && (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 bg-slate-900 text-white p-2.5 rounded-xl font-mono text-xs">
            {active.formula && (
              <div className="bg-slate-800/90 p-2 rounded-lg border border-slate-700">
                <div className="text-[9px] uppercase tracking-wider text-slate-400 font-sans font-bold mb-0.5">
                  1. Curriculum Formula
                </div>
                <div data-testid="calc-popover-formula" className="text-sky-300 font-semibold">
                  <MathText text={ensureMathWrap(active.formula)} />
                </div>
              </div>
            )}
            {active.substitution && (
              <div className="bg-slate-800/90 p-2 rounded-lg border border-slate-700">
                <div className="text-[9px] uppercase tracking-wider text-slate-400 font-sans font-bold mb-0.5 flex items-center gap-1">
                  <span>2. Live Substitution</span>
                  <ArrowRight className="w-2.5 h-2.5 text-emerald-400" />
                </div>
                <div data-testid="calc-popover-substitution" className="text-emerald-300 font-semibold">
                  <MathText text={ensureMathWrap(active.substitution)} />
                </div>
              </div>
            )}
          </div>
        )}

        {/* Micro-Physical or Physiological Mechanism Explanation */}
        {mechanismText && (
          <div
            data-testid="calc-popover-mechanism"
            className="p-2.5 rounded-lg bg-amber-50/80 border border-amber-200/80 text-xs text-slate-800 flex items-start gap-2"
          >
            <Sparkles className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
            <div className="leading-relaxed">
              <span className="font-bold text-amber-900 mr-1">Physical Mechanism:</span>
              <MathText text={mechanismText} />
            </div>
          </div>
        )}

        {active.note && (
          <div className="text-[11px] text-slate-600 flex items-start gap-1.5 pt-0.5">
            <Info className="w-3.5 h-3.5 text-[#13519C] shrink-0 mt-0.5" />
            <MathText text={active.note} />
          </div>
        )}
      </div>
    </div>
  );
}
