import React from 'react';
import { X, AlertCircle, ChevronRight } from 'lucide-react';

/**
 * EvaluationOverlay — displays the rubric step-by-step breakdown
 * when a user clicks on an incorrect cell after Check.
 *
 * Props:
 *   cellId       — the cell that was clicked
 *   result       — { correct, expected, userValue, rubric }
 *   onClose      — dismiss callback
 *   position     — optional { top, left } for positioning
 */
const EvaluationOverlay = ({ cellId, result, onClose }) => {
    if (!result) return null;

    const { expected, userValue, rubric } = result;

    // rubric can be a string, array of steps, or object with { formula, steps }
    const renderRubric = () => {
        if (!rubric) {
            return (
                <p className="text-sm text-slate-500 italic">
                    The correct answer is <span className="font-semibold text-slate-800">{String(expected)}</span>
                </p>
            );
        }

        // If rubric is a string
        if (typeof rubric === 'string') {
            return <p className="text-sm text-slate-700">{rubric}</p>;
        }

        // If rubric is an object with formula and/or steps
        if (typeof rubric === 'object' && !Array.isArray(rubric)) {
            return (
                <div className="space-y-3">
                    {rubric.formula && (
                        <div className="bg-indigo-50 border border-indigo-200 rounded-lg px-3 py-2">
                            <p className="text-xs font-semibold text-indigo-600 uppercase tracking-wide mb-1">Formula</p>
                            <p className="font-mono text-sm text-indigo-900">{rubric.formula}</p>
                        </div>
                    )}
                    {rubric.steps && Array.isArray(rubric.steps) && (
                        <div className="space-y-2">
                            <p className="text-xs font-semibold text-slate-500 uppercase tracking-wide">Steps</p>
                            {rubric.steps.map((step, i) => (
                                <div key={i} className="flex gap-2 items-start">
                                    <span className="flex-shrink-0 w-5 h-5 rounded-full bg-slate-200 text-slate-600 text-xs flex items-center justify-center font-semibold mt-0.5">
                                        {i + 1}
                                    </span>
                                    <p className="text-sm text-slate-700">{typeof step === 'string' ? step : step.description || JSON.stringify(step)}</p>
                                </div>
                            ))}
                        </div>
                    )}
                    {rubric.hint && (
                        <p className="text-sm text-amber-700 bg-amber-50 border border-amber-200 rounded-lg px-3 py-2">
                            💡 {rubric.hint}
                        </p>
                    )}
                </div>
            );
        }

        // If rubric is an array of steps
        if (Array.isArray(rubric)) {
            return (
                <div className="space-y-2">
                    {rubric.map((step, i) => (
                        <div key={i} className="flex gap-2 items-start">
                            <span className="flex-shrink-0 w-5 h-5 rounded-full bg-slate-200 text-slate-600 text-xs flex items-center justify-center font-semibold mt-0.5">
                                {i + 1}
                            </span>
                            <p className="text-sm text-slate-700">{typeof step === 'string' ? step : JSON.stringify(step)}</p>
                        </div>
                    ))}
                </div>
            );
        }

        return null;
    };

    return (
        <div className="fixed inset-0 z-[100] flex items-center justify-center p-4" onClick={onClose}>
            {/* Backdrop */}
            <div className="absolute inset-0 bg-black/30 backdrop-blur-sm" />

            {/* Card */}
            <div
                className="relative bg-white rounded-2xl shadow-2xl border border-slate-200 w-full max-w-md overflow-hidden animate-in fade-in slide-in-from-bottom-4 duration-200"
                onClick={(e) => e.stopPropagation()}
            >
                {/* Header */}
                <div className="flex items-center justify-between px-4 py-3 bg-red-50 border-b border-red-100">
                    <div className="flex items-center gap-2">
                        <AlertCircle className="h-4 w-4 text-red-500" />
                        <span className="text-sm font-semibold text-red-700">Incorrect Answer</span>
                    </div>
                    <button
                        onClick={onClose}
                        className="p-1 rounded-lg hover:bg-red-100 transition-colors"
                    >
                        <X className="h-4 w-4 text-red-400" />
                    </button>
                </div>

                {/* Content */}
                <div className="p-4 space-y-4">
                    {/* Your answer vs Correct */}
                    <div className="grid grid-cols-2 gap-3">
                        <div className="bg-red-50 border border-red-200 rounded-xl px-3 py-2">
                            <p className="text-[10px] font-semibold text-red-500 uppercase tracking-wide mb-0.5">Your Answer</p>
                            <p className="text-sm font-medium text-red-800 break-words">{String(userValue || '—')}</p>
                        </div>
                        <div className="bg-emerald-50 border border-emerald-200 rounded-xl px-3 py-2">
                            <p className="text-[10px] font-semibold text-emerald-500 uppercase tracking-wide mb-0.5">Correct</p>
                            <p className="text-sm font-medium text-emerald-800 break-words">{String(expected || '—')}</p>
                        </div>
                    </div>

                    {/* Rubric breakdown */}
                    <div className="border-t border-slate-100 pt-3">
                        <p className="text-xs font-semibold text-slate-500 uppercase tracking-wide mb-2">How to solve it</p>
                        {renderRubric()}
                    </div>
                </div>

                {/* Footer */}
                <div className="px-4 py-3 bg-slate-50 border-t border-slate-200">
                    <button
                        onClick={onClose}
                        className="w-full flex items-center justify-center gap-1 px-4 py-2 rounded-xl text-sm font-semibold bg-slate-800 text-white hover:bg-slate-700 transition-all active:scale-95"
                    >
                        Got it
                        <ChevronRight className="h-4 w-4" />
                    </button>
                </div>
            </div>
        </div>
    );
};

/**
 * EvaluationScoreBanner — shows after Check with score summary
 */
export const EvaluationScoreBanner = ({ summary }) => {
    if (!summary) return null;

    const { total, correct, incorrect, percentage } = summary;
    const isAllCorrect = incorrect === 0;

    return (
        <div className={`rounded-xl border px-4 py-3 flex items-center justify-between ${
            isAllCorrect
                ? 'bg-emerald-50 border-emerald-200'
                : 'bg-amber-50 border-amber-200'
        }`}>
            <div className="flex items-center gap-3">
                <div className={`w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold ${
                    isAllCorrect ? 'bg-emerald-600 text-white' : 'bg-amber-600 text-white'
                }`}>
                    {percentage}%
                </div>
                <div>
                    <p className={`text-sm font-semibold ${isAllCorrect ? 'text-emerald-800' : 'text-amber-800'}`}>
                        {isAllCorrect ? 'Perfect Score! 🎉' : `${correct} of ${total} correct`}
                    </p>
                    {!isAllCorrect && (
                        <p className="text-xs text-amber-600">
                            Click red cells to see step-by-step solutions
                        </p>
                    )}
                </div>
            </div>
        </div>
    );
};

export default EvaluationOverlay;
