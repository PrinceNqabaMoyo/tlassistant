import React, { useState, useEffect } from 'react';
import {
    ChevronLeft,
    ChevronDown,
    ChevronUp,
    Settings,
    Lock,
    CheckCircle2,
    ArrowLeftRight,
    ArrowRight,
    Loader2,
    GraduationCap,
    GitBranch,
} from 'lucide-react';
import { UserFriendlyError } from '../../ui/UserFriendlyError';

/**
 * WorkspaceModeShell — shared UI wrapper for scaffold/practice/marking views.
 *
 * Design language strictly follows "fundile-ui-alternative-design.html":
 *   • bg-brand-blue (#13519C) header ribbon with gold graduation cap & topic badge
 *   • Thin orange progress ribbon (bg-gradient-to-r from-brand-orange to-brand-amber)
 *   • bg-slate-50 canvas with white rounded-2xl cards and shadow-sm / shadow-lift
 *   • Primary action CTAs in bg-brand-orange (#FF9100) with shadow-ribbon
 *   • Cross-grade regression banner (rounded-2xl border-brand-orange/30 bg-amber-50/70)
 */

const modeColors = {
    scaffold: 'bg-brand-blue text-white border-brand-blue shadow-xs font-semibold',
    practice: 'bg-brand-blue text-white border-brand-blue shadow-xs font-semibold',
    marking: 'bg-brand-blue text-white border-brand-blue shadow-xs font-semibold',
};

const MODES = ['scaffold', 'practice', 'marking'];
const DIFFICULTIES = ['easy', 'medium', 'hard'];

/** Extract "scaffold" | "practice" | "marking" from a route string */
const getRouteMode = (mode) => {
    if (!mode) return null;
    for (const m of MODES) {
        if (mode.endsWith(`_${m}`)) return m;
    }
    return null;
};

/** Strip the mode suffix to get the route base, e.g. "grade10_exponents" */
const getRouteBase = (mode) => {
    const routeMode = getRouteMode(mode);
    if (!routeMode) return null;
    return mode.slice(0, mode.length - routeMode.length - 1); // -1 for the underscore
};

export const EmbeddedWorkspaceContext = React.createContext(false);

const WorkspaceModeShell = (props) => {
    const {
        workspaceMode,
        setWorkspaceMode,
        onBack,
        selectedSubject,
        selectedGrade,
        topic,
        subskills = [],
        difficulty,
        setDifficulty,
        subskill,
        setSubskill,
        onGenerate,
        children,
        questionSlot,
        onNext,
        renderVisualAids,
        availableModes = ['scaffold', 'practice', 'marking'],
        subscriptionTier = 'standard', // 'standard' | 'pro' | 'owner'
        showDifficultyControl = true,
        disableSubskillControl = false,
        showConfigBackButton = true,
        onCheck,
        onCompare,
        isChecked = false,
        isComparing = false,
        isGenerating = false,
        generationError = null,
        isSuperAdmin = false,
        autoStart = false,
    } = props;

    const isEmbeddedFromContext = React.useContext(EmbeddedWorkspaceContext);
    const isEmbedded = props.isEmbedded || isEmbeddedFromContext;

    const currentMode = getRouteMode(workspaceMode) || 'scaffold';
    const routeBase = getRouteBase(workspaceMode);

    const [showQuestion, setShowQuestion] = useState(autoStart);

    // Sync internal state with props when they change
    const [localDifficulty, setLocalDifficulty] = useState(difficulty || 'easy');
    const [localSubskill, setLocalSubskill] = useState(subskill || 'mixed');
    const [localMode, setLocalMode] = useState(currentMode);

    useEffect(() => {
        if (difficulty) setLocalDifficulty(difficulty);
    }, [difficulty]);

    useEffect(() => {
        if (subskill) setLocalSubskill(subskill);
    }, [subskill]);

    useEffect(() => {
        setLocalMode(currentMode);
    }, [currentMode]);

    const isMarkingLocked = subscriptionTier === 'standard';

    const handleModeSwitch = (nextMode) => {
        if (nextMode === localMode) return;
        // Block switching to marking if locked
        if (nextMode === 'marking' && isMarkingLocked) return;
        setLocalMode(nextMode);
        if (routeBase && setWorkspaceMode) {
            setWorkspaceMode(`${routeBase}_${nextMode}`);
        }
    };

    const handleGenerate = () => {
        if (setDifficulty) setDifficulty(localDifficulty);
        if (setSubskill) setSubskill(localSubskill);

        if (onGenerate) {
            onGenerate({
                mode: localMode,
                difficulty: localDifficulty,
                subskill: localSubskill
            });
        }
        setShowQuestion(true);
    };

    useEffect(() => {
        if (autoStart) {
            handleGenerate();
        }
    }, [autoStart]);

    // Build subtitle from available info
    const subtitleParts = [
        selectedGrade ? `Grade ${selectedGrade}` : null,
        selectedSubject?.name || null,
        topic || null,
    ].filter(Boolean);

    const selectedSubskillLabel = subskills.find(s => s.key === localSubskill)?.title || localSubskill;
    const showSubskillControl = !disableSubskillControl;
    const configurationGridClassName = (() => {
        const cols = [];
        if (showDifficultyControl) cols.push('difficulty');
        if (showSubskillControl) cols.push('subskill');
        cols.push('generate');
        const count = cols.length;
        if (count <= 2) return 'grid grid-cols-1 sm:grid-cols-2 gap-4';
        if (count === 3) return 'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4';
        return 'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4';
    })();

    // Hide scrollbar on mount, restore on unmount
    useEffect(() => {
        if (isEmbedded) return;
        document.body.classList.add('scrollbar-hide');
        document.documentElement.classList.add('scrollbar-hide');

        return () => {
            document.body.classList.remove('scrollbar-hide');
            document.documentElement.classList.remove('scrollbar-hide');
        };
    }, [isEmbedded]);

    return (
        <div className={isEmbedded ? "w-full h-full relative overflow-y-auto" : "min-h-screen bg-slate-50 relative overflow-x-hidden"}>
            {/* ── Fixed Top Brand Ribbon (fundile-ui-alternative-design.html) ── */}
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
                                {selectedGrade && (
                                    <span className="hidden sm:inline px-3 py-1 rounded-full bg-white/10 border border-white/15">
                                        Grade {selectedGrade}
                                    </span>
                                )}
                                {selectedSubject?.name && (
                                    <span className="hidden sm:inline px-3 py-1 rounded-full bg-white/10 border border-white/15">
                                        {selectedSubject.name}
                                    </span>
                                )}
                                <span className="px-3 py-1 rounded-full bg-brand-orange/90 font-semibold text-white shadow-xs">
                                    {topic || 'Question Workspace'}
                                </span>
                            </div>
                        </div>
                    </header>
                    {/* Gradient progress ribbon */}
                    <div className="h-1.5 w-full bg-slate-100 mb-6">
                        <div className="h-full bg-gradient-to-r from-brand-orange to-brand-amber" style={{ width: '68%' }} />
                    </div>
                </>
            )}

            <div className={`max-w-5xl mx-auto space-y-6 relative ${isEmbedded ? '' : 'px-4 sm:px-6 pb-12'}`}>

                {/* ── Header (Visible in Config View) ── */}
                {!showQuestion && (
                    <div className="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-4">
                        <div>
                            <h1 className="text-xl sm:text-2xl font-bold text-slate-800">
                                Question Workspace
                            </h1>
                            {subtitleParts.length > 0 && (
                                <p className="text-slate-500 text-xs sm:text-sm mt-1">
                                    {subtitleParts.join(' • ')}
                                </p>
                            )}
                        </div>
                        <div className="flex gap-2">
                            {showConfigBackButton && onBack && (
                                <button
                                    onClick={onBack}
                                    className="flex items-center gap-1 px-4 py-2 rounded-xl border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 transition-colors text-sm font-medium shadow-sm cursor-pointer"
                                >
                                    <ChevronLeft className="h-4 w-4" />
                                    Back
                                </button>
                            )}
                        </div>
                    </div>
                )}

                {/* ── Configuration Panel ── */}
                {!showQuestion && (
                    <div className="transition-all duration-300 transform translate-y-0 opacity-100">
                        <div className="rounded-2xl shadow-sm border border-slate-200 bg-white overflow-hidden">
                            <div className="p-4 sm:p-6 space-y-6">

                                {/* Controls Grid */}
                                <div className={configurationGridClassName}>
                                    {/* Difficulty */}
                                    {showDifficultyControl && (
                                        <div className="space-y-2">
                                            <p className="text-xs font-semibold text-slate-500 uppercase tracking-wide">Difficulty</p>
                                            <div className="flex gap-2">
                                                {DIFFICULTIES.map((level) => (
                                                    <button
                                                        key={level}
                                                        onClick={() => setLocalDifficulty(level)}
                                                        className={`flex-1 px-3 py-2 rounded-xl text-sm capitalize border transition-all duration-200 cursor-pointer ${
                                                            localDifficulty === level
                                                                ? 'bg-brand-blue text-white border-brand-blue shadow-md font-semibold'
                                                                : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-50 font-medium'
                                                        }`}
                                                    >
                                                        {level}
                                                    </button>
                                                ))}
                                            </div>
                                        </div>
                                    )}

                                    {/* Subskill */}
                                    {showSubskillControl && (
                                        <div className="space-y-2 sm:col-span-2">
                                            <p className="text-xs font-semibold text-slate-500 uppercase tracking-wide">Subskill</p>
                                            <select
                                                value={localSubskill}
                                                onChange={(e) => setLocalSubskill(e.target.value)}
                                                className="w-full px-3 py-3 rounded-xl border text-sm bg-white transition-all border-slate-200 focus:outline-none focus:ring-2 focus:ring-brand-blue/30 focus:border-brand-blue cursor-pointer"
                                            >
                                                {subskills.length > 0 ? (
                                                    subskills.map((s) => (
                                                        <option key={s.key} value={s.key}>{s.title}</option>
                                                    ))
                                                ) : (
                                                    <option value="mixed">Mixed (all)</option>
                                                )}
                                            </select>
                                        </div>
                                    )}

                                    {/* Generate Button */}
                                    <div className="flex items-end">
                                        <button
                                            onClick={handleGenerate}
                                            className="w-full rounded-xl h-12 text-sm font-semibold bg-brand-orange text-white hover:bg-brand-orangeDark transition-all shadow-ribbon active:scale-95 cursor-pointer"
                                        >
                                            Generate Question
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                )}

                {/* ── Overlay Background Blur ── */}
                {showQuestion && (
                    <div className={`${isEmbedded ? 'absolute' : 'fixed'} inset-0 bg-slate-900/20 backdrop-blur-sm z-40 transition-opacity duration-300`} />
                )}

                {/* ── Question Content Overlay ── */}
                {showQuestion && (
                    <div className={`${isEmbedded ? 'absolute px-2 py-3' : 'fixed px-4 py-8 sm:px-6'} inset-0 z-50 overflow-y-auto scrollbar-hide`}>
                        <div className={isEmbedded ? "space-y-3" : "max-w-5xl mx-auto space-y-6"}>

                            {/* Card 1: Header + Meta + Question Prompt (Only when NOT embedded) */}
                            {!isEmbedded && (
                                <div className="rounded-2xl shadow-xl border border-slate-200 bg-white overflow-hidden p-4 sm:p-6 space-y-6">
                                    {/* Internal Header (Title + Breadcrumbs + Back to Config) */}
                                    <div className="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-4 pb-4 border-b border-slate-100">
                                        <div>
                                            <h1 className="text-xl sm:text-2xl font-bold text-slate-800">
                                                Question Workspace
                                            </h1>
                                            {subtitleParts.length > 0 && (
                                                <p className="text-slate-500 text-xs sm:text-sm mt-1">
                                                    {subtitleParts.join(' • ')}
                                                </p>
                                            )}
                                        </div>
                                        <div>
                                            <button
                                                onClick={() => setShowQuestion(false)}
                                                className="flex items-center gap-1 px-4 py-2 rounded-xl border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 transition-colors text-sm font-medium shadow-sm cursor-pointer"
                                            >
                                                <ChevronLeft className="h-4 w-4" />
                                                Back
                                            </button>
                                        </div>
                                    </div>

                                    {/* Meta Pills */}
                                    <div className="flex flex-wrap items-center justify-between gap-3 text-xs">
                                        <div className="flex flex-wrap gap-2">
                                            <span className="px-3 py-1 rounded-full border bg-brand-blue/10 text-brand-blue border-brand-blue/20 font-bold uppercase tracking-wider text-[11px]">
                                                Practice &amp; Mastery
                                            </span>
                                            {showDifficultyControl && (
                                                <span className="px-3 py-1 rounded-full border bg-slate-100 text-slate-700 capitalize">
                                                    {localDifficulty}
                                                </span>
                                            )}
                                            <span className="px-3 py-1 rounded-full border bg-slate-100 text-slate-700">
                                                {selectedSubskillLabel}
                                            </span>
                                        </div>
                                    </div>

                                    {questionSlot ? (
                                        <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 sm:p-5">{questionSlot}</div>
                                    ) : isGenerating ? (
                                        <div className="rounded-xl border border-blue-200 bg-blue-50 px-6 py-8 flex flex-col items-center justify-center text-center space-y-3">
                                            <Loader2 className="w-8 h-8 text-brand-blue animate-spin" />
                                            <p className="text-sm font-semibold text-slate-900">
                                                Generating your question...
                                            </p>
                                            <p className="text-xs text-slate-600 max-w-sm">
                                                This usually takes a few seconds. We're putting together the perfect problem for you.
                                            </p>
                                        </div>
                                    ) : (
                                        <div className="rounded-xl border border-amber-200 bg-amber-50 px-4 py-4 space-y-2">
                                            <div className="text-sm font-semibold text-amber-900">
                                                <UserFriendlyError error={generationError || "Question generation did not complete."} isSuperAdmin={isSuperAdmin} />
                                            </div>
                                        </div>
                                    )}
                                </div>
                            )}

                            {/* Compact Loader for Embedded Mode */}
                            {isGenerating && isEmbedded && (
                                <div className="rounded-xl border border-blue-200 bg-blue-50 px-4 py-6 flex flex-col items-center justify-center text-center space-y-2">
                                    <Loader2 className="w-6 h-6 text-brand-blue animate-spin" />
                                    <p className="text-xs font-semibold text-slate-900">
                                        Generating your question...
                                    </p>
                                </div>
                            )}

                            {/* Card 2: Answer / Interaction */}
                            {!isGenerating && (
                                <div className="rounded-2xl shadow-xl border border-slate-200 bg-white overflow-hidden">
                                    {isEmbedded && questionSlot && (
                                        <div className="p-3 border-b border-slate-100 bg-slate-50 text-xs font-semibold text-slate-700 leading-relaxed max-h-24 overflow-y-auto whitespace-pre-wrap">
                                            {questionSlot}
                                        </div>
                                    )}
                                    <div className={isEmbedded ? "p-3" : "p-4 sm:p-6"}>
                                        {children}
                                    </div>

                                {/* Check / Compare / Next Footer */}
                                {(onCheck || onCompare || onNext) && localMode !== 'marking' && (
                                    <div className="border-t border-slate-200 bg-slate-50 px-4 sm:px-6 py-3 flex flex-wrap gap-3 items-center">
                                        {onCheck && (
                                            <button
                                                onClick={onCheck}
                                                className={`flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold transition-all shadow-sm active:scale-95 cursor-pointer ${
                                                    isChecked
                                                        ? 'bg-emerald-600 text-white hover:bg-emerald-700'
                                                        : 'bg-brand-blue text-white hover:bg-brand-cobalt'
                                                }`}
                                            >
                                                <CheckCircle2 className="h-4 w-4" />
                                                {isChecked ? 'Checked ✓' : 'Check'}
                                            </button>
                                        )}
                                        {onCompare && isChecked && (
                                            <button
                                                onClick={onCompare}
                                                className={`flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold transition-all shadow-sm active:scale-95 cursor-pointer ${
                                                    isComparing
                                                        ? 'bg-amber-600 text-white hover:bg-amber-700'
                                                        : 'bg-white text-brand-blue border border-brand-blue/30 hover:bg-blue-50'
                                                }`}
                                            >
                                                <ArrowLeftRight className="h-4 w-4" />
                                                {isComparing ? 'Showing Answers' : 'Compare memo'}
                                            </button>
                                        )}
                                        {onNext && (
                                            <button
                                                onClick={onNext}
                                                className="ml-auto flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold bg-brand-orange text-white hover:bg-brand-orangeDark transition shadow-ribbon active:scale-95 cursor-pointer"
                                            >
                                                Next <ArrowRight className="h-4 w-4" />
                                            </button>
                                        )}
                                    </div>
                                )}
                            </div>
                            )}

                            {/* Standalone Next Button when not in footer */}
                            {onNext && (!onCheck && !onCompare) && (
                                <button
                                    onClick={onNext}
                                    className="w-full rounded-xl h-12 text-sm font-semibold bg-brand-orange text-white hover:bg-brand-orangeDark transition-all shadow-ribbon active:scale-95 cursor-pointer flex items-center justify-center gap-2"
                                >
                                    Next Question <ArrowRight className="h-4 w-4" />
                                </button>
                            )}

                            {/* ── Prerequisite Gap Banner (Cross-grade regression made visible) ── */}
                            {props.prerequisiteBanner && (
                                <div className="rounded-2xl border border-brand-orange/30 bg-amber-50/70 p-4 sm:p-5 flex items-start gap-3 shadow-sm">
                                    <span className="h-9 w-9 shrink-0 grid place-items-center rounded-xl bg-brand-orange/15 text-brand-orange">
                                        <GitBranch className="h-5 w-5" />
                                    </span>
                                    <div className="flex-1">
                                        <p className="font-semibold text-slate-900 text-sm">
                                            Prerequisite gap detected — step down to Grade {props.prerequisiteBanner.target_grade}
                                        </p>
                                        <p className="text-xs text-slate-600 mt-0.5 leading-relaxed">
                                            {props.prerequisiteBanner.explanation || `You're missing ${props.prerequisiteBanner.target_subskill || 'foundational subskill'}. A 5-minute foundational micro-drill is recommended before continuing.`}
                                        </p>
                                        <button
                                            type="button"
                                            onClick={() => props.onStartMicroDrill && props.onStartMicroDrill(props.prerequisiteBanner)}
                                            className="mt-2 text-xs font-bold text-brand-blue hover:underline flex items-center gap-1 cursor-pointer"
                                        >
                                            Start micro-drill ({props.prerequisiteBanner.target_topic} · Grade {props.prerequisiteBanner.target_grade}) →
                                        </button>
                                    </div>
                                </div>
                            )}

                            {/* Visual Aids Panel (Collapsible) */}
                            {renderVisualAids && (
                                <VisualAidsPanel>
                                    {renderVisualAids()}
                                </VisualAidsPanel>
                            )}

                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

// Internal VisualAidsPanel component
const VisualAidsPanel = ({ children }) => {
    const [isOpen, setIsOpen] = useState(false);
    return (
        <div className="rounded-2xl shadow-lg border border-slate-200 bg-white overflow-hidden">
            <button
                onClick={() => setIsOpen(!isOpen)}
                className="w-full flex items-center justify-between p-4 bg-slate-50 hover:bg-slate-100 transition-colors"
            >
                <span className="font-semibold text-slate-800">Visual Aids</span>
                {isOpen ? <ChevronUp className="h-5 w-5 text-slate-500" /> : <ChevronDown className="h-5 w-5 text-slate-500" />}
            </button>
            {isOpen && <div className="p-4 border-t border-slate-200">{children}</div>}
        </div>
    );
};

export default WorkspaceModeShell;