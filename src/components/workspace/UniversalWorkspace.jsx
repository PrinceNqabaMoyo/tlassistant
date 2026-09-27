import React, { useState, useEffect } from 'react';
import {
    ChevronLeft,
    CheckCircle2,
    ArrowLeftRight,
    ArrowRight,
    Loader2,
    GraduationCap,
    GitBranch,
    X,
} from 'lucide-react';
import MathText from './shared/mathx/MathText';
import MathModalityRenderer from './modalities/MathModalityRenderer';
import LedgerModalityRenderer from './modalities/LedgerModalityRenderer';
import RubricModalityRenderer from './modalities/RubricModalityRenderer';
import DiagramModalityRenderer from './modalities/DiagramModalityRenderer';
import MasteryDial from '../student/MasteryDial';

/**
 * UniversalWorkspace — single unified question workspace for all Grades 7–12 and all subjects.
 * Eliminates the obsolete 3-mode selector (scaffold, practice, marking).
 * Scaffolding is dynamically unfoldable in-situ rather than locked behind mode gates.
 */
export default function UniversalWorkspace({
    grade,
    subject,
    topic,
    question,
    isGenerating = false,
    isChecking = false,
    onBack,
    onCheck,
    onCompare,
    onNext,
    onStartMicroDrill,
    prerequisiteBanner,
    generationError,
    result,
    isEmbedded = false,
    formativeMastery = 78,
    evaluativeScore = 82,
    initialProgressionMode = 'practice',
    onProgressionModeChange,
}) {
    const [progressionMode, setProgressionMode] = useState(initialProgressionMode); // 'scaffold' | 'practice' | 'exam'
    const [showMasteryModal, setShowMasteryModal] = useState(false);
    const [isChecked, setIsChecked] = useState(false);
    const [isComparing, setIsComparing] = useState(false);
    const [showDynamicScaffold, setShowDynamicScaffold] = useState(initialProgressionMode === 'scaffold');

    useEffect(() => {
        setIsChecked(false);
        setIsComparing(false);
        setShowDynamicScaffold(progressionMode === 'scaffold');
    }, [question?.id, progressionMode]);

    const handleCheckWrapper = async (userAnswer) => {
        if (onCheck) {
            await onCheck(userAnswer);
            setIsChecked(true);
        }
    };

    const handleCompareToggle = () => {
        if (onCompare) {
            onCompare();
        }
        setIsComparing(prev => !prev);
    };

    // Determine cognitive modality from question payload or subject domain
    const modality = (() => {
        if (question?.modality) return question.modality;
        const subjName = (typeof subject === 'string' ? subject : subject?.name || '').toLowerCase();
        if (subjName.includes('accounting') || subjName.includes('ems')) return 'ledger';
        if (subjName.includes('business')) return 'rubric';
        if (question?.diagram || question?.diagram_spec) return 'diagram';
        return 'math'; // Default: Mathematics, Physical Sciences, Tech Maths, Math Lit
    })();

    const subjectTitle = typeof subject === 'string' ? subject : subject?.name || 'Mathematics';

    return (
        <div className={isEmbedded ? "w-full h-full relative overflow-y-auto" : "min-h-screen bg-slate-50 relative overflow-x-hidden font-sans"}>
            {/* Sticky Brand Ribbon (Matching fundile-ui-alternative-design.html) */}
            {!isEmbedded && (
                <>
                    <header className="sticky top-0 z-30 bg-brand-blue border-b border-white/10 h-14 sm:h-16 shadow-lg shadow-brand-blue/20 px-4 sm:px-8">
                        <div className="max-w-6xl mx-auto h-full flex items-center justify-between">
                            <div className="flex items-center gap-2.5 text-white">
                                <span className="grid place-items-center h-8 w-8 sm:h-9 sm:w-9 rounded-xl bg-white/10 ring-1 ring-white/20">
                                    <GraduationCap className="h-4 w-4 sm:h-5 sm:w-5 text-brand-amber" />
                                </span>
                                <span className="font-display font-bold text-lg sm:text-xl tracking-tight">Fundile</span>
                            </div>
                            <div className="flex items-center gap-2 text-xs font-medium text-white/80">
                                {grade && (
                                    <span className="hidden sm:inline px-3 py-1 rounded-full bg-white/10 border border-white/15">
                                        Grade {grade}
                                    </span>
                                )}
                                <span className="hidden sm:inline px-3 py-1 rounded-full bg-white/10 border border-white/15">
                                    {subjectTitle}
                                </span>
                                <span className="px-3 py-1 rounded-full bg-brand-orange/90 font-semibold text-white shadow-xs">
                                    {topic || 'Learning Workspace'}
                                </span>
                            </div>
                        </div>
                    </header>
                    {/* Gradient progress ribbon */}
                    <div className="h-1.5 w-full bg-slate-100 mb-6">
                        <div className="h-full bg-gradient-to-r from-brand-orange to-brand-amber" style={{ width: '72%' }} />
                    </div>
                </>
            )}

            <div className={`max-w-5xl mx-auto space-y-6 relative ${isEmbedded ? '' : 'px-4 sm:px-6 pb-12'}`}>
                {/* Internal Navigation Header */}
                <div className="flex items-center justify-between gap-4">
                    <div>
                        <h1 className="text-xl sm:text-2xl font-bold text-slate-900">
                            {topic || 'Practice Problem'}
                        </h1>
                        <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
                            Grade {grade || '10'} • {subjectTitle} • Direct Problem Solving
                        </p>
                    </div>
                    {onBack && (
                        <button
                            type="button"
                            onClick={onBack}
                            className="flex items-center gap-1 px-4 py-2 rounded-xl border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 transition text-sm font-semibold shadow-xs cursor-pointer"
                        >
                            <ChevronLeft className="h-4 w-4" />
                            Back
                        </button>
                    )}
                </div>

                {/* ── 3-Tier Progression Mode Switcher & Adaptive Progress Dial ── */}
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 p-2.5 sm:p-3 rounded-2xl bg-white border border-slate-200/90 shadow-xs">
                    {/* 3-Tier Progression Mode Switcher */}
                    <div className="flex items-center gap-1 bg-slate-100 p-1 rounded-xl w-full sm:w-auto">
                        {[
                            { id: 'scaffold', label: '1. Scaffold', icon: '🧱', desc: 'Step-by-step guided problem solving' },
                            { id: 'practice', label: '2. Practice', icon: '🎯', desc: 'Autonomous formative mastery drill' },
                            { id: 'exam', label: '3. Exam Mode', icon: '📝', desc: 'Timed test condition with mark allocations' },
                        ].map((m) => {
                            const isActive = progressionMode === m.id;
                            return (
                                <button
                                    key={m.id}
                                    type="button"
                                    onClick={() => {
                                        setProgressionMode(m.id);
                                        if (onProgressionModeChange) onProgressionModeChange(m.id);
                                        if (m.id === 'scaffold') setShowDynamicScaffold(true);
                                    }}
                                    className={`flex-1 sm:flex-initial flex items-center justify-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                                        isActive
                                            ? 'bg-white text-[#13519C] shadow-xs'
                                            : 'text-slate-600 hover:text-slate-900'
                                    }`}
                                    title={m.desc}
                                >
                                    <span>{m.icon}</span>
                                    <span>{m.label}</span>
                                </button>
                            );
                        })}
                    </div>

                    {/* Adaptive Progress Dial / Mastery Pill */}
                    <button
                        type="button"
                        onClick={() => setShowMasteryModal(true)}
                        className="inline-flex items-center gap-2.5 px-3 py-1.5 rounded-xl bg-slate-50 hover:bg-slate-100 border border-slate-200/90 transition cursor-pointer text-left shrink-0 self-end sm:self-auto"
                        title="Click to view full BKT Formative Mastery Dial"
                    >
                        {/* Mini Circular Gauge */}
                        <div className="relative w-7 h-7 flex items-center justify-center shrink-0">
                            <svg className="w-7 h-7 transform -rotate-90">
                                <circle cx="14" cy="14" r="11" stroke="#e2e8f0" strokeWidth="2.5" fill="transparent" />
                                <circle
                                    cx="14" cy="14" r="11"
                                    stroke={formativeMastery >= 80 ? '#10b981' : formativeMastery >= 60 ? '#13519C' : '#f59e0b'}
                                    strokeWidth="2.5"
                                    fill="transparent"
                                    strokeDasharray={2 * Math.PI * 11}
                                    strokeDashoffset={(2 * Math.PI * 11) * (1 - (formativeMastery / 100))}
                                    strokeLinecap="round"
                                />
                            </svg>
                            <span className="absolute text-[8px] font-extrabold text-slate-800">
                                {formativeMastery}%
                            </span>
                        </div>
                        <div className="leading-tight">
                            <div className="flex items-center gap-1">
                                <span className="text-xs font-bold text-slate-900">
                                    {formativeMastery >= 80 ? 'Exam Ready' : formativeMastery >= 60 ? 'Proficient' : 'Foundation'}
                                </span>
                                <span className="text-[10px] text-emerald-600 font-extrabold">BKT</span>
                            </div>
                            <span className="text-[10px] text-slate-500">
                                Formative Mastery
                            </span>
                        </div>
                    </button>
                </div>

                {/* Question Card */}
                <div className="rounded-2xl shadow-sm border border-slate-200 bg-white overflow-hidden p-4 sm:p-6 space-y-5">
                    {/* Metadata Badges */}
                    <div className="flex flex-wrap items-center justify-between gap-3 text-xs">
                        <div className="flex flex-wrap items-center gap-2">
                            <span className="px-3 py-1 rounded-full bg-brand-blue/10 text-brand-blue border border-brand-blue/20 font-bold uppercase tracking-wider text-[11px]">
                                Practice &amp; Mastery
                            </span>
                            {question?.difficulty && (
                                <span className="px-3 py-1 rounded-full bg-slate-100 text-slate-700 font-semibold capitalize border border-slate-200">
                                    {question.difficulty}
                                </span>
                            )}
                            {question?.marks && (
                                <span className="px-3 py-1 rounded-full bg-amber-50 text-amber-800 font-bold border border-amber-200">
                                    {question.marks} Marks
                                </span>
                            )}
                        </div>
                    </div>

                    {/* Question Prompt */}
                    {isGenerating ? (
                        <div className="rounded-xl border border-blue-200 bg-blue-50 px-6 py-8 flex flex-col items-center justify-center text-center space-y-3">
                            <Loader2 className="w-8 h-8 text-brand-blue animate-spin" />
                            <p className="text-sm font-semibold text-slate-900">Generating problem...</p>
                            <p className="text-xs text-slate-600 max-w-sm">Calibrating values deterministically for your mastery level.</p>
                        </div>
                    ) : generationError ? (
                        <div className="rounded-xl border border-rose-200 bg-rose-50 p-4 text-xs font-semibold text-rose-800">
                            {generationError}
                        </div>
                    ) : (
                        <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 sm:p-5 text-sm sm:text-base text-slate-800 leading-relaxed font-medium">
                            <MathText text={question?.question || question?.prompt || 'No question prompt loaded.'} />
                        </div>
                    )}
                </div>

                {/* Modality Interaction Slot (Math, Ledger, Rubric, Diagram) */}
                {!isGenerating && question && (
                    <div className="rounded-2xl shadow-sm border border-slate-200 bg-white overflow-hidden p-4 sm:p-6 space-y-6">
                        {modality === 'ledger' && (
                            <LedgerModalityRenderer
                                question={question}
                                topic={topic}
                                onCheck={handleCheckWrapper}
                                result={result}
                                isChecking={isChecking}
                                showDynamicScaffold={showDynamicScaffold}
                                onToggleScaffold={() => setShowDynamicScaffold(prev => !prev)}
                            />
                        )}
                        {modality === 'rubric' && (
                            <RubricModalityRenderer
                                question={question}
                                topic={topic}
                                onCheck={handleCheckWrapper}
                                result={result}
                                isChecking={isChecking}
                                showDynamicScaffold={showDynamicScaffold}
                                onToggleScaffold={() => setShowDynamicScaffold(prev => !prev)}
                            />
                        )}
                        {modality === 'diagram' && (
                            <DiagramModalityRenderer
                                question={question}
                                topic={topic}
                                onCheck={handleCheckWrapper}
                                result={result}
                                isChecking={isChecking}
                                showDynamicScaffold={showDynamicScaffold}
                                onToggleScaffold={() => setShowDynamicScaffold(prev => !prev)}
                            />
                        )}
                        {modality === 'math' && (
                            <MathModalityRenderer
                                question={question}
                                topic={topic}
                                onCheck={handleCheckWrapper}
                                result={result}
                                isChecking={isChecking}
                                showDynamicScaffold={showDynamicScaffold}
                                onToggleScaffold={() => setShowDynamicScaffold(prev => !prev)}
                            />
                        )}

                        {/* Interactive Action Footer */}
                        <div className="border-t border-slate-100 pt-4 flex flex-wrap items-center justify-between gap-3">
                            <div className="flex items-center gap-3">
                                {onCompare && isChecked && (
                                    <button
                                        type="button"
                                        onClick={handleCompareToggle}
                                        className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-semibold transition cursor-pointer ${
                                            isComparing
                                                ? 'bg-amber-600 text-white'
                                                : 'bg-white text-brand-blue border border-brand-blue/30 hover:bg-blue-50'
                                        }`}
                                    >
                                        <ArrowLeftRight className="h-4 w-4" />
                                        {isComparing ? 'Showing Memo' : 'Compare Memo'}
                                    </button>
                                )}
                            </div>

                            {onNext && (
                                <button
                                    type="button"
                                    onClick={onNext}
                                    className="ml-auto flex items-center gap-2 px-6 py-2.5 rounded-xl text-sm font-bold bg-brand-orange text-white hover:bg-brand-orangeDark transition shadow-ribbon active:scale-95 cursor-pointer"
                                >
                                    <span>Next Problem</span>
                                    <ArrowRight className="h-4 w-4" />
                                </button>
                            )}
                        </div>
                    </div>
                )}

                {/* Prerequisite Gap Banner (When Cross-Grade Regression Occurs) */}
                {prerequisiteBanner && (
                    <div className="rounded-2xl border border-brand-orange/30 bg-amber-50/80 p-4 sm:p-5 flex items-start gap-3 shadow-xs">
                        <span className="h-9 w-9 shrink-0 grid place-items-center rounded-xl bg-brand-orange/15 text-brand-orange">
                            <GitBranch className="h-5 w-5" />
                        </span>
                        <div className="flex-1">
                            <p className="font-bold text-slate-900 text-sm">
                                Prerequisite gap identified — Step down to Grade {prerequisiteBanner.target_grade}
                            </p>
                            <p className="text-xs text-slate-600 mt-0.5 leading-relaxed">
                                {prerequisiteBanner.explanation || `Mastery in ${prerequisiteBanner.target_subskill || 'foundational concepts'} is recommended to unlock compound problems.`}
                            </p>
                            <button
                                type="button"
                                onClick={() => onStartMicroDrill && onStartMicroDrill(prerequisiteBanner)}
                                className="mt-2 text-xs font-bold text-brand-blue hover:underline flex items-center gap-1 cursor-pointer"
                            >
                                Start 5-Min Prerequisite Drill ({prerequisiteBanner.target_topic} • Grade {prerequisiteBanner.target_grade}) →
                            </button>
                        </div>
                    </div>
                )}
            </div>

            {/* Full BKT Mastery Dial Modal */}
            {showMasteryModal && (
                <div 
                    className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/60 backdrop-blur-sm animate-in fade-in duration-200"
                    onClick={() => setShowMasteryModal(false)}
                >
                    <div 
                        className="relative max-w-sm w-full bg-slate-900 text-white rounded-3xl p-6 shadow-2xl border border-slate-800"
                        onClick={(e) => e.stopPropagation()}
                    >
                        <button
                            type="button"
                            onClick={() => setShowMasteryModal(false)}
                            className="absolute top-4 right-4 p-2 rounded-full text-slate-400 hover:text-white hover:bg-white/10 transition cursor-pointer"
                        >
                            <X className="w-5 h-5" />
                        </button>
                        <div className="text-left mb-4">
                            <span className="text-[10px] font-extrabold uppercase tracking-widest text-[#FF9100]">
                                Cognitive Engine
                            </span>
                            <h3 className="text-lg font-bold text-white mt-0.5">
                                Adaptive Mastery Dial
                            </h3>
                            <p className="text-xs text-slate-400 mt-1 leading-relaxed">
                                Formative mastery modeled via Bayesian Knowledge Tracing with Ebbinghaus memory decay calibration.
                            </p>
                        </div>
                        <MasteryDial
                            formativeMastery={formativeMastery}
                            evaluativeScore={evaluativeScore}
                            size={160}
                        />
                        <div className="mt-4 pt-3 border-t border-slate-800 text-center">
                            <button
                                type="button"
                                onClick={() => setShowMasteryModal(false)}
                                className="w-full py-2.5 px-4 rounded-xl bg-white/10 hover:bg-white/20 text-white font-semibold text-xs transition cursor-pointer"
                            >
                                Close
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}
