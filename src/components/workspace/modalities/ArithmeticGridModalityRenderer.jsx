import React, { useState, useEffect } from 'react';
import { CheckCircle2, AlertTriangle, Lightbulb, ChevronDown, ChevronUp, Loader2 } from 'lucide-react';
import MathText from '../shared/mathx/MathText';

/**
 * ArithmeticGridModalityRenderer
 * Native cognitive modality for CAPS Grades 7–9 arithmetic procedures:
 * - South African Long Division Algorithm
 * - Columnar Subtraction & Borrowing Verification
 * - Stepwise Multi-digit Arithmetic
 */
export default function ArithmeticGridModalityRenderer({
    question,
    topic,
    onCheck,
    result,
    isChecking,
    showDynamicScaffold,
    onToggleScaffold,
}) {
    if (!question) return null;

    const grid = question.arithmetic_grid || {
        operation: 'long_division',
        divisor: 5,
        dividend: 845,
        quotient: 169,
        remainder: 0,
        sub_steps: [
            { current: 8, digit_quotient: 1, product: 5, remainder: 3 },
            { current: 34, digit_quotient: 6, product: 30, remainder: 4 },
            { current: 45, digit_quotient: 9, product: 45, remainder: 0 }
        ]
    };

    const divisor = grid.divisor || 5;
    const dividend = grid.dividend || 845;
    const expectedQuotient = grid.quotient || question.correct_quotient || 169;
    const expectedRemainder = grid.remainder || question.correct_remainder || 0;

    const [quotientInput, setQuotientInput] = useState('');
    const [remainderInput, setRemainderInput] = useState('0');
    const [showSteps, setShowSteps] = useState(false);

    // Reset when question changes
    useEffect(() => {
        setQuotientInput('');
        setRemainderInput('0');
        setShowSteps(false);
    }, [question.id]);

    const handleSubmit = (e) => {
        if (e) e.preventDefault();
        if (onCheck) {
            onCheck({
                quotient: quotientInput.trim(),
                remainder: remainderInput.trim() || '0',
            });
        }
    };

    const isCorrect = result?.is_correct;
    const hasError = result && !result.is_correct;
    const isBorrowingError = result?.misconception_tag === 'subtraction_borrowing_inversion' ||
        result?.error_type === 'subtraction_borrowing_inversion';

    return (
        <div className="space-y-5 font-sans" data-testid="arithmetic-grid-workspace">
            {/* Top Algorithmic Layout */}
            <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs">
                <div className="flex flex-wrap items-center justify-between gap-3 mb-4 pb-3 border-b border-slate-100">
                    <div>
                        <span className="text-[10px] font-extrabold px-2 py-0.5 rounded bg-blue-50 text-[#13519C] border border-blue-200 uppercase tracking-wider font-mono">
                            Long Division Algorithm • Grade 7 Standard
                        </span>
                        <h4 className="text-sm font-bold text-slate-800 mt-1" style={{ fontFamily: 'Afacad, sans-serif' }}>
                            Columnar Division Bracket &amp; Place-Value Grid
                        </h4>
                    </div>

                    <button
                        type="button"
                        onClick={() => setShowSteps(!showSteps)}
                        className="text-xs font-bold text-[#13519C] hover:text-blue-800 flex items-center gap-1 cursor-pointer"
                    >
                        <span>{showSteps ? 'Hide Division Steps' : 'Show Step Breakdown'}</span>
                        {showSteps ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
                    </button>
                </div>

                {/* Division Bracket Visualization */}
                <div className="bg-slate-50/80 rounded-xl p-4 border border-slate-200/70 flex flex-col items-center justify-center space-y-4">
                    {/* Quotient Display / Bracket Container */}
                    <div className="font-mono text-lg select-text inline-block">
                        {/* Quotient Line */}
                        <div className="flex justify-end pr-2 text-[#13519C] font-bold text-xl tracking-widest min-h-[28px]">
                            {quotientInput ? quotientInput : <span className="text-slate-300">? ? ?</span>}
                        </div>

                        {/* Radical Line */}
                        <div className="flex items-center">
                            <span className="text-slate-700 font-bold pr-2">{divisor}</span>
                            <div className="border-t-2 border-l-2 border-slate-800 pl-3 pr-4 py-1 text-slate-900 font-black tracking-widest bg-white shadow-2xs rounded-tr-lg">
                                {dividend}
                            </div>
                        </div>

                        {/* Step Breakdown (if expanded) */}
                        {showSteps && grid.sub_steps && (
                            <div className="mt-3 pl-8 space-y-2 text-xs border-l-2 border-dashed border-slate-300">
                                {grid.sub_steps.map((step, idx) => (
                                    <div key={idx} className="space-y-1">
                                        <div className="flex items-center gap-2 text-slate-600">
                                            <span className="text-slate-400">Step {idx + 1}:</span>
                                            <span>{divisor} &times; {step.digit_quotient} = <strong>{step.product}</strong></span>
                                        </div>
                                        <div className="text-slate-700 pl-2">
                                            &minus; {step.product} = <strong className="text-emerald-700">{step.remainder}</strong>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                </div>

                {/* Interactive Learner Input Form */}
                <form onSubmit={handleSubmit} className="mt-5 space-y-4">
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        {/* Quotient Input */}
                        <div>
                            <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                                Quotient (Whole Number)
                            </label>
                            <input
                                type="text"
                                data-testid="input-quotient"
                                value={quotientInput}
                                onChange={(e) => setQuotientInput(e.target.value)}
                                placeholder="e.g. 169"
                                className={`w-full px-4 py-2.5 rounded-xl border-2 font-mono text-base font-bold text-slate-900 focus:outline-none transition ${
                                    hasError
                                        ? 'border-rose-400 bg-rose-50/50 focus:border-rose-500'
                                        : isCorrect
                                        ? 'border-emerald-500 bg-emerald-50/40 focus:border-emerald-600'
                                        : 'border-slate-300 focus:border-[#13519C] bg-white'
                                }`}
                                autoFocus
                            />
                        </div>

                        {/* Remainder Input */}
                        <div>
                            <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">
                                Remainder (If Any, or 0)
                            </label>
                            <input
                                type="text"
                                data-testid="input-remainder"
                                value={remainderInput}
                                onChange={(e) => setRemainderInput(e.target.value)}
                                placeholder="0"
                                className="w-full px-4 py-2.5 rounded-xl border-2 border-slate-300 focus:border-[#13519C] font-mono text-base font-bold text-slate-900 focus:outline-none bg-white transition"
                            />
                        </div>
                    </div>

                    {/* Feedback Callout */}
                    {hasError && (
                        <div className="p-3.5 rounded-xl bg-rose-50 border border-rose-300 text-rose-900 text-xs flex items-start gap-2.5 animate-fadeIn">
                            <AlertTriangle className="w-4 h-4 text-rose-600 shrink-0 mt-0.5" />
                            <div className="space-y-1">
                                <span className="font-bold block">
                                    {isBorrowingError ? 'Place-Value Subtraction Slip Detected' : 'Division Slip Detected'}
                                </span>
                                <p className="text-slate-700 leading-relaxed">
                                    {result.feedback || 'Check your intermediate subtraction steps. Make sure to borrow correctly across place values.'}
                                </p>
                                {isBorrowingError && (
                                    <span className="inline-block mt-1 font-mono text-[10px] font-bold bg-rose-100 text-rose-800 px-2 py-0.5 rounded border border-rose-200">
                                        Misconception: subtraction_borrowing_inversion
                                    </span>
                                )}
                            </div>
                        </div>
                    )}

                    {isCorrect && (
                        <div className="p-3.5 rounded-xl bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs flex items-center justify-between gap-3 animate-fadeIn">
                            <div className="flex items-center gap-2">
                                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                                <div>
                                    <span className="font-bold block">Accurate Quotient &amp; Algorithm Completed!</span>
                                    <span className="text-slate-600">{result.feedback || `Quotient is ${expectedQuotient} with remainder ${expectedRemainder}.`}</span>
                                </div>
                            </div>
                            <span className="font-mono text-xs font-extrabold bg-emerald-100 text-emerald-800 px-2.5 py-1 rounded-lg">
                                +35 XP
                            </span>
                        </div>
                    )}

                    {/* Action Bar */}
                    <div className="pt-2 flex items-center justify-between">
                        <button
                            type="button"
                            onClick={() => {
                                setQuotientInput(String(expectedQuotient));
                                setRemainderInput(String(expectedRemainder));
                            }}
                            className="text-xs font-semibold text-slate-500 hover:text-slate-800 underline cursor-pointer"
                        >
                            Fill Correct ({expectedQuotient})
                        </button>

                        <button
                            type="submit"
                            data-testid="btn-check-answer"
                            disabled={isChecking || !quotientInput.trim()}
                            className="px-6 py-2.5 rounded-xl bg-[#13519C] hover:bg-[#0f4280] disabled:opacity-50 text-white font-bold text-xs shadow-sm transition active:scale-98 cursor-pointer flex items-center gap-2"
                        >
                            {isChecking ? (
                                <>
                                    <Loader2 className="w-4 h-4 animate-spin" />
                                    <span>Verifying Algorithm...</span>
                                </>
                            ) : (
                                <>
                                    <CheckCircle2 className="w-4 h-4" />
                                    <span>Check Division</span>
                                </>
                            )}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}
