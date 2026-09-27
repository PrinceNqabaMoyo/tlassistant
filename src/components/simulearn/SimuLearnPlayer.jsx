import React, { useState, useEffect, useRef } from 'react';
import KaTeXRenderer from '../shared/KaTeXRenderer';

// Pre-packaged canonical scripts for instantaneous zero-latency offline playback
const DEFAULT_SCRIPTS = {
  accounting_crj_vat: {
    archetype: 'crj_vat_split',
    title: 'Recording Cash Sales with 15% VAT in the CRJ',
    subject: 'Accounting',
    grid_type: 'journal_table',
    headers: ['Day', 'Details', 'Bank (Gross)', 'Sales (Excl)', 'Output VAT (15%)', 'Cost of Sales'],
    frames: [
      {
        time_ms: 0,
        action: 'highlight_prompt',
        narrative: 'Transaction: Sold merchandise for R1,150 cash. Cost of sales is R800. (VAT rate is 15%).'
      },
      {
        time_ms: 2000,
        action: 'type_cell',
        cell_id: 'r0_c0',
        value: '12',
        label: 'Day',
        narrative: 'Record the day (12) in the Day column.'
      },
      {
        time_ms: 4000,
        action: 'type_cell',
        cell_id: 'r0_c1',
        value: 'Cash',
        label: 'Details',
        narrative: "Details is 'Cash' (or CRT for cash register tape)."
      },
      {
        time_ms: 6000,
        action: 'type_cell',
        cell_id: 'r0_c2',
        value: '1150.00',
        label: 'Bank Gross',
        narrative: 'Bank always receives the full gross cash amount: R1,150.00.'
      },
      {
        time_ms: 8500,
        action: 'formula_callout',
        latex: '\\text{Sales (Excl)} = 1150 \\times \\frac{100}{115} = 1000.00',
        narrative: 'Extract VAT: Divide gross by 1.15 to find net Sales of R1,000.00.'
      },
      {
        time_ms: 10500,
        action: 'type_cell',
        cell_id: 'r0_c3',
        value: '1000.00',
        label: 'Sales Excl',
        narrative: 'Record R1,000.00 in Sales and R150.00 in Output VAT.'
      }
    ]
  },
  math_quadratic_trinomial: {
    archetype: 'quadratic_factorisation',
    title: 'Factorising a Quadratic Trinomial: x² + 5x + 6',
    subject: 'Mathematics',
    grid_type: 'stepwise_math',
    frames: [
      {
        time_ms: 0,
        action: 'show_expression',
        latex: 'x^2 + 5x + 6',
        narrative: 'Goal: Factorise the trinomial into two binomial brackets (x + a)(x + b).'
      },
      {
        time_ms: 2500,
        action: 'formula_callout',
        latex: '\\text{Find } a, b \\text{ where } a \\cdot b = 6 \\text{ and } a + b = 5',
        narrative: 'Step 1: Look for factors of the constant term (+6) that sum to the middle coefficient (+5).'
      },
      {
        time_ms: 5500,
        action: 'show_step',
        latex: '2 \\times 3 = 6 \\quad \\text{and} \\quad 2 + 3 = 5',
        narrative: 'Step 2: The factor pair is +2 and +3.'
      },
      {
        time_ms: 8500,
        action: 'final_solution',
        latex: '(x + 2)(x + 3)',
        narrative: 'Step 3: Write the factorised form: (x + 2)(x + 3).'
      }
    ]
  },
  physics_kinematics_dx: {
    archetype: 'kinematics_1d',
    title: 'Kinematics: Displacement Equation Δx = v_i Δt + ½ a Δt²',
    subject: 'Physical Sciences',
    grid_type: 'stepwise_math',
    frames: [
      {
        time_ms: 0,
        action: 'list_knowns',
        latex: 'v_i = 10\\text{ m/s}, \\quad a = 2\\text{ m/s}^2, \\quad \\Delta t = 4\\text{ s}',
        narrative: 'Step 1: Write down all given variables.'
      },
      {
        time_ms: 3000,
        action: 'show_formula',
        latex: '\\Delta x = v_i \\Delta t + \\frac{1}{2} a \\Delta t^2',
        narrative: 'Step 2: Choose the equation of motion containing vi, a, and Δt.'
      },
      {
        time_ms: 6500,
        action: 'substitute_values',
        latex: '\\Delta x = (10)(4) + \\frac{1}{2}(2)(4)^2 = 40 + 16',
        narrative: 'Step 3: Substitute knowns. Remember to square the time first (4² = 16).'
      },
      {
        time_ms: 9500,
        action: 'final_solution',
        latex: '\\Delta x = 56\\text{ m}',
        narrative: 'Step 4: Compute final displacement: 56 metres.'
      }
    ]
  },
  lifesciences_punnett_square: {
    archetype: 'monohybrid_cross',
    title: 'Monohybrid Cross: Heterozygous Parents (Bb × Bb)',
    subject: 'Life Sciences',
    grid_type: 'punnett_grid',
    headers: ['Gametes', 'B', 'b'],
    frames: [
      {
        time_ms: 0,
        action: 'highlight_prompt',
        latex: '\\text{Parents: } Bb \\times Bb \\quad (\\text{Brown dominant to blue})',
        narrative: 'Parental genotypes: Both parents are heterozygous (Bb).'
      },
      {
        time_ms: 2500,
        action: 'type_cell',
        cell_id: 'r0_c0',
        value: 'BB',
        label: 'Square 1: B from Mother, B from Father',
        narrative: 'Square 1: Homozygous Dominant (BB) - Brown phenotype.'
      },
      {
        time_ms: 5000,
        action: 'type_cell',
        cell_id: 'r0_c1',
        value: 'Bb',
        label: 'Square 2: B from Mother, b from Father',
        narrative: 'Square 2: Heterozygous (Bb) - Brown phenotype.'
      },
      {
        time_ms: 7500,
        action: 'type_cell',
        cell_id: 'r1_c0',
        value: 'Bb',
        label: 'Square 3: b from Mother, B from Father',
        narrative: 'Square 3: Heterozygous (Bb) - Brown phenotype.'
      },
      {
        time_ms: 9500,
        action: 'type_cell',
        cell_id: 'r1_c1',
        value: 'bb',
        label: 'Square 4: b from Mother, b from Father',
        narrative: 'Square 4: Homozygous Recessive (bb) - Blue phenotype.'
      },
      {
        time_ms: 11000,
        action: 'final_solution',
        latex: '\\text{Ratio: } 3\\text{ Brown} : 1\\text{ Blue} \\quad (75\\% : 25\\%)',
        narrative: 'Summary: 3 : 1 phenotypic ratio (75% probability of dominant trait).'
      }
    ]
  }
};

export default function SimuLearnPlayer({
  archetypeKey = 'accounting_crj_vat',
  customScript = null,
  isOpen = true,
  onClose,
  onComplete
}) {
  const script = customScript || DEFAULT_SCRIPTS[archetypeKey] || DEFAULT_SCRIPTS.accounting_crj_vat;
  const frames = script.frames || [];

  const [currentFrameIndex, setCurrentFrameIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(true);
  const [playbackSpeed, setPlaybackSpeed] = useState(1);
  const [tableValues, setTableValues] = useState({});
  const timerRef = useRef(null);

  const currentFrame = frames[currentFrameIndex] || frames[0];
  const isFinished = currentFrameIndex >= frames.length - 1;

  // Sync table values up to current frame
  useEffect(() => {
    const newValues = {};
    for (let i = 0; i <= currentFrameIndex; i++) {
      const f = frames[i];
      if (f && f.action === 'type_cell' && f.cell_id) {
        newValues[f.cell_id] = f.value;
      }
    }
    setTableValues(newValues);
  }, [currentFrameIndex, frames]);

  // Autoplay step timer
  useEffect(() => {
    if (!isPlaying || isFinished) {
      if (timerRef.current) clearTimeout(timerRef.current);
      return;
    }

    const nextFrame = frames[currentFrameIndex + 1];
    const currentMs = currentFrame?.time_ms || 0;
    const nextMs = nextFrame?.time_ms || currentMs + 2500;
    const delta = Math.max(800, (nextMs - currentMs) / playbackSpeed);

    timerRef.current = setTimeout(() => {
      if (currentFrameIndex < frames.length - 1) {
        setCurrentFrameIndex(prev => prev + 1);
      } else {
        setIsPlaying(false);
      }
    }, delta);

    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, [isPlaying, currentFrameIndex, frames, playbackSpeed, isFinished]);

  if (!isOpen) return null;

  const handleRestart = () => {
    setCurrentFrameIndex(0);
    setTableValues({});
    setIsPlaying(true);
  };

  const handleNext = () => {
    if (currentFrameIndex < frames.length - 1) {
      setCurrentFrameIndex(prev => prev + 1);
    }
  };

  const handlePrev = () => {
    if (currentFrameIndex > 0) {
      setCurrentFrameIndex(prev => prev - 1);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-950/80 backdrop-blur-md animate-fade-in">
      <div className="bg-slate-900 border border-slate-700/80 rounded-2xl shadow-2xl max-w-3xl w-full flex flex-col overflow-hidden text-slate-100">
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-4 border-b border-slate-800 bg-slate-950/50">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-sm border border-indigo-500/30">
              ▶
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs px-2 py-0.5 rounded-full bg-indigo-900/60 text-indigo-300 font-semibold border border-indigo-700/50">
                  SimuLearn • {script.subject}
                </span>
                <span className="text-xs text-slate-400">Step {currentFrameIndex + 1} of {frames.length}</span>
              </div>
              <h3 className="text-sm sm:text-base font-semibold text-slate-100 mt-0.5">
                {script.title}
              </h3>
            </div>
          </div>
          {onClose && (
            <button
              onClick={onClose}
              className="p-1.5 rounded-lg text-slate-400 hover:text-slate-100 hover:bg-slate-800 transition-colors"
            >
              ✕
            </button>
          )}
        </div>

        {/* Dynamic Simulation Stage */}
        <div className="p-6 bg-slate-950/90 flex flex-col items-center justify-center min-h-[260px] relative">
          {/* Modal content based on grid_type */}
          {script.grid_type === 'journal_table' && (
            <div className="w-full overflow-x-auto">
              <table className="w-full text-xs text-left border-collapse border border-slate-700 rounded-lg overflow-hidden">
                <thead className="bg-slate-800/90 text-slate-300 text-[11px] uppercase tracking-wider">
                  <tr>
                    {script.headers?.map((h, i) => (
                      <th key={i} className="p-2.5 border-b border-r border-slate-700 font-semibold">
                        {h}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  <tr className="bg-slate-900/60">
                    <td className={`p-2.5 border-r border-slate-700 font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c0' ? 'bg-amber-500/20 text-amber-300 ring-2 ring-amber-400' : 'text-slate-200'}`}>
                      {tableValues['r0_c0'] || '—'}
                    </td>
                    <td className={`p-2.5 border-r border-slate-700 font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c1' ? 'bg-amber-500/20 text-amber-300 ring-2 ring-amber-400' : 'text-slate-200'}`}>
                      {tableValues['r0_c1'] || '—'}
                    </td>
                    <td className={`p-2.5 border-r border-slate-700 font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c2' ? 'bg-amber-500/20 text-amber-300 ring-2 ring-amber-400' : 'text-slate-200'}`}>
                      {tableValues['r0_c2'] || '—'}
                    </td>
                    <td className={`p-2.5 border-r border-slate-700 font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c3' ? 'bg-amber-500/20 text-amber-300 ring-2 ring-amber-400' : 'text-slate-200'}`}>
                      {tableValues['r0_c3'] || '—'}
                    </td>
                    <td className="p-2.5 border-r border-slate-700 font-mono text-slate-400">
                      {tableValues['r0_c3'] ? (parseFloat(tableValues['r0_c3']) * 0.15).toFixed(2) : '—'}
                    </td>
                    <td className="p-2.5 font-mono text-slate-400">
                      800.00
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          )}

          {script.grid_type === 'punnett_grid' && (
            <div className="flex flex-col items-center gap-3">
              <div className="grid grid-cols-3 gap-2 text-center text-sm font-semibold">
                <div className="p-2 text-slate-400">♀ \ ♂</div>
                <div className="p-2 bg-indigo-950/60 rounded text-indigo-300">B</div>
                <div className="p-2 bg-indigo-950/60 rounded text-indigo-300">b</div>

                <div className="p-2 bg-purple-950/60 rounded text-purple-300">B</div>
                <div className={`p-3 rounded border font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c0' ? 'bg-amber-500/20 border-amber-400 text-amber-300 ring-2 ring-amber-400' : 'bg-slate-800/80 border-slate-700 text-slate-200'}`}>
                  {tableValues['r0_c0'] || '—'}
                </div>
                <div className={`p-3 rounded border font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c1' ? 'bg-amber-500/20 border-amber-400 text-amber-300 ring-2 ring-amber-400' : 'bg-slate-800/80 border-slate-700 text-slate-200'}`}>
                  {tableValues['r0_c1'] || '—'}
                </div>

                <div className="p-2 bg-purple-950/60 rounded text-purple-300">b</div>
                <div className={`p-3 rounded border font-mono transition-all duration-300 ${currentFrame.cell_id === 'r1_c0' ? 'bg-amber-500/20 border-amber-400 text-amber-300 ring-2 ring-amber-400' : 'bg-slate-800/80 border-slate-700 text-slate-200'}`}>
                  {tableValues['r1_c0'] || '—'}
                </div>
                <div className={`p-3 rounded border font-mono transition-all duration-300 ${currentFrame.cell_id === 'r1_c1' ? 'bg-amber-500/20 border-amber-400 text-amber-300 ring-2 ring-amber-400' : 'bg-slate-800/80 border-slate-700 text-slate-200'}`}>
                  {tableValues['r1_c1'] || '—'}
                </div>
              </div>
            </div>
          )}

          {script.grid_type === 'stepwise_math' && (
            <div className="flex flex-col items-center gap-3 text-center">
              {currentFrame.latex && (
                <div className="p-3.5 bg-slate-900/90 rounded-xl border border-indigo-500/30 text-indigo-200 text-lg shadow-inner">
                  <KaTeXRenderer latex={currentFrame.latex} />
                </div>
              )}
            </div>
          )}

          {/* Formula overlay / Callout */}
          {currentFrame.latex && script.grid_type !== 'stepwise_math' && (
            <div className="mt-4 p-2.5 px-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 text-indigo-200 text-sm animate-fade-in shadow-lg">
              <KaTeXRenderer latex={currentFrame.latex} />
            </div>
          )}
        </div>

        {/* Narrative & Insight Bar */}
        <div className="px-6 py-3.5 bg-slate-900 border-t border-slate-800/80 flex items-start gap-3">
          <span className="text-amber-400 text-base mt-0.5">💡</span>
          <p className="text-xs sm:text-sm text-slate-200 leading-relaxed font-medium">
            {currentFrame.narrative}
          </p>
        </div>

        {/* Progress Scrub Bar */}
        <div className="w-full bg-slate-800 h-1.5 cursor-pointer">
          <div
            className="bg-indigo-500 h-full transition-all duration-300"
            style={{ width: `${((currentFrameIndex + 1) / frames.length) * 100}%` }}
          />
        </div>

        {/* Playback Controls & Actions */}
        <div className="p-4 bg-slate-950 flex flex-wrap items-center justify-between gap-3 border-t border-slate-800/80">
          <div className="flex items-center gap-2">
            <button
              onClick={handleRestart}
              className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors"
              title="Restart"
            >
              ↺
            </button>
            <button
              onClick={handlePrev}
              disabled={currentFrameIndex === 0}
              className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-300 transition-colors"
              title="Previous Step"
            >
              ⏮
            </button>
            <button
              onClick={() => setIsPlaying(!isPlaying)}
              className="px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-colors flex items-center gap-1.5 shadow-md shadow-indigo-900/40"
            >
              {isPlaying ? '⏸ Pause' : '▶ Play'}
            </button>
            <button
              onClick={handleNext}
              disabled={isFinished}
              className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-300 transition-colors"
              title="Next Step"
            >
              ⏭
            </button>
          </div>

          <div className="flex items-center gap-2">
            {/* Speed pills */}
            <div className="flex items-center bg-slate-900 rounded-lg p-0.5 border border-slate-800 text-[11px]">
              {[0.5, 1, 1.5, 2].map(speed => (
                <button
                  key={speed}
                  onClick={() => setPlaybackSpeed(speed)}
                  className={`px-2 py-1 rounded transition-colors ${
                    playbackSpeed === speed
                      ? 'bg-slate-700 text-indigo-300 font-semibold'
                      : 'text-slate-400 hover:text-slate-200'
                  }`}
                >
                  {speed}x
                </button>
              ))}
            </div>

            {/* Complete / Try Practice button */}
            <button
              onClick={() => {
                if (onComplete) onComplete();
                if (onClose) onClose();
              }}
              className="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs transition-colors shadow-md shadow-emerald-900/40"
            >
              Try Question Now →
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
