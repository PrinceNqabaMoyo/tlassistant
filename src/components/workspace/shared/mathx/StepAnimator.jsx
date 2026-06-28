import React from 'react';
import MathText from './MathText';

/**
 * StepAnimator — displays two adjacent canonical steps with a visual transition
 * indicator (e.g. an arrow showing a term moving across the equals sign).
 *
 * Props:
 *   fromStep   canonical step object { from_latex, op, rule }
 *   toStep     canonical step object { to_latex, op, rule }
 *   active     boolean — whether to animate / highlight the transition
 */
const StepAnimator = ({ fromStep, toStep, active = false }) => {
    if (!fromStep && !toStep) return null;

    const fromLatex = fromStep?.from_latex || fromStep?.to_latex || '';
    const toLatex = toStep?.to_latex || '';
    const operation = toStep?.op || fromStep?.op || '';
    const rule = toStep?.rule || fromStep?.rule || '';

    return (
        <div className={`rounded-lg border p-3 transition-colors ${active ? 'border-indigo-300 bg-indigo-50' : 'border-slate-200 bg-white'}`}>
            <div className="flex items-center justify-between gap-3">
                <div className="flex-1 min-w-0">
                    {fromLatex ? (
                        <MathText latex={fromLatex} display />
                    ) : (
                        <span className="text-xs text-slate-400 italic">Start</span>
                    )}
                </div>
                <div className="flex flex-col items-center px-2">
                    <svg
                        className={`w-6 h-6 transition-transform ${active ? 'text-indigo-500 translate-x-1' : 'text-slate-300'}`}
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        strokeWidth={2}
                    >
                        <path strokeLinecap="round" strokeLinejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                    </svg>
                    {operation ? (
                        <span className="mt-1 text-[10px] font-medium uppercase tracking-wide text-slate-500">
                            {operation}
                        </span>
                    ) : null}
                </div>
                <div className="flex-1 min-w-0">
                    {toLatex ? (
                        <MathText latex={toLatex} display />
                    ) : (
                        <span className="text-xs text-slate-400 italic">End</span>
                    )}
                </div>
            </div>
            {rule ? (
                <p className="mt-2 text-xs text-slate-500 text-center">
                    Rule: {rule}
                </p>
            ) : null}
        </div>
    );
};

export default StepAnimator;
