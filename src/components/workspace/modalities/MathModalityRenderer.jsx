import React, { useState, useEffect } from 'react';
import MathText from '../shared/mathx/MathText';
import MathAnswerArea from '../shared/mathx/MathAnswerArea';

export default function MathModalityRenderer({
    question,
    topic,
    onCheck,
    result,
    isChecking,
    showDynamicScaffold,
    onToggleScaffold,
}) {
    if (!question) return null;

    const rawSteps = question.scaffold_steps || question.solution_graph?.nodes || question.worked_solution || [];
    const hasScaffoldSteps = Array.isArray(rawSteps) && rawSteps.length > 0;

    return (
        <div className="space-y-6">
            {/* 1. Dynamic In-Situ Scaffold Drawer (Unfolds on demand / struggle) */}
            {hasScaffoldSteps && (
                <div className="rounded-2xl border border-blue-200 bg-blue-50/60 p-4 transition-all duration-300">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-2">
                            <span className="grid place-items-center h-6 w-6 rounded-lg bg-brand-blue text-white text-xs font-bold">
                                🪜
                            </span>
                            <span className="text-sm font-bold text-brand-blue">
                                Step-by-Step Breakdown (Scaffold)
                            </span>
                        </div>
                        <button
                            type="button"
                            onClick={onToggleScaffold}
                            className="text-xs font-bold text-brand-blue hover:underline cursor-pointer"
                        >
                            {showDynamicScaffold ? 'Hide Steps ▲' : 'Show Guided Steps ▼'}
                        </button>
                    </div>

                    {showDynamicScaffold && (
                        <div className="mt-4 pt-3 border-t border-blue-100 space-y-3">
                            <p className="text-xs text-slate-600">
                                Follow these structured milestones to solve the problem:
                            </p>
                            <ol className="space-y-2">
                                {rawSteps.map((step, idx) => (
                                    <li key={idx} className="flex items-start gap-2.5 text-xs text-slate-700 bg-white p-2.5 rounded-xl border border-blue-100 shadow-2xs">
                                        <span className="font-bold text-brand-blue shrink-0">Step {idx + 1}:</span>
                                        <div className="flex-1">
                                            {typeof step === 'string' ? (
                                                <MathText text={step} />
                                            ) : (
                                                <div>
                                                    <p className="font-semibold text-slate-800">{step.title || step.label || step.rule || `Milestone ${idx + 1}`}</p>
                                                    {step.description && <p className="text-slate-600 mt-0.5"><MathText text={step.description} /></p>}
                                                    {step.latex && <div className="mt-1"><MathText text={step.latex} /></div>}
                                                </div>
                                            )}
                                        </div>
                                    </li>
                                ))}
                            </ol>
                        </div>
                    )}
                </div>
            )}

            {/* 2. Math Answer & Keypad Interaction Area */}
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
