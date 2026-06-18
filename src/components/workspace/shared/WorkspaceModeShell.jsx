import React, { useState, useEffect } from 'react';
import { ChevronLeft, ChevronDown, ChevronUp, Settings, Lock, CheckCircle2, ArrowLeftRight, Loader2 } from 'lucide-react';
import { UserFriendlyError } from '../../ui/UserFriendlyError';

/**
 * WorkspaceModeShell — shared UI wrapper for scaffold/marking views.
 *
 * Design language mirrors "Workspace UI.js":
 *   • bg-slate-50 page, max-w-5xl centered container
 *   • Configuration Panel for selecting mode, difficulty, subskill
 *   • Question Overlay with background blur
 *   • Soft mode pills (scaffold / marking)
 *   • Indigo / emerald / amber colour palette
 */

const modeColors = {
    scaffold: 'bg-indigo-50 text-indigo-700 border-indigo-200',
    practice: 'bg-emerald-50 text-emerald-700 border-emerald-200',
    marking: 'bg-amber-50 text-amber-700 border-amber-200',
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

const WorkspaceModeShell = ({
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
}) => {
    const currentMode = getRouteMode(workspaceMode) || 'scaffold';
    const routeBase = getRouteBase(workspaceMode);

    const [showQuestion, setShowQuestion] = useState(false);

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

    // Build subtitle from available info
    const subtitleParts = [
        selectedGrade ? `Grade ${selectedGrade}` : null,
        selectedSubject?.name || null,
        topic || null,
    ].filter(Boolean);

    const selectedSubskillLabel = subskills.find(s => s.key === localSubskill)?.title || localSubskill;
    const configurationGridClassName = showDifficultyControl
        ? 'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4'
        : 'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4';

    // Hide scrollbar on mount, restore on unmount
    useEffect(() => {
        document.body.classList.add('scrollbar-hide');
        document.documentElement.classList.add('scrollbar-hide');

        return () => {
            document.body.classList.remove('scrollbar-hide');
            document.documentElement.classList.remove('scrollbar-hide');
        };
    }, []);

    return (
        <div className="min-h-screen bg-slate-50 px-4 py-6 sm:px-6 relative overflow-x-hidden">
            <div className="max-w-5xl mx-auto space-y-6 relative">

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
                                    className="flex items-center gap-1 px-4 py-2 rounded-xl border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 transition-colors text-sm font-medium shadow-sm"
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
                                {/* Mode Selection */}
                                {availableModes.length > 1 && (
                                    <div className="space-y-2">
                                        <p className="text-xs font-semibold text-slate-500 uppercase tracking-wide">Mode</p>
                                        <div className="flex flex-wrap gap-2">
                                            {availableModes.map((m) => {
                                                const locked = m === 'marking' && isMarkingLocked;
                                                return (
                                                    <button
                                                        key={m}
                                                        onClick={() => handleModeSwitch(m)}
                                                        className={`text-xs px-3 py-2 rounded-full border transition-all duration-200 capitalize flex items-center gap-1 ${
                                                            locked
                                                                ? 'bg-slate-100 text-slate-400 border-slate-200 cursor-not-allowed opacity-60'
                                                                : localMode === m
                                                                    ? modeColors[m]
                                                                    : 'bg-white text-slate-500 border-slate-200 hover:bg-slate-50'
                                                        }`}
                                                        disabled={locked}
                                                        title={locked ? 'Upgrade to Pro for AI-powered marking' : ''}
                                                    >
                                                        {locked && <Lock className="h-3 w-3" />}
                                                        {m}
                                                        {locked && <span className="text-[10px] ml-0.5 font-semibold">PRO</span>}
                                                    </button>
                                                );
                                            })}
                                        </div>
                                    </div>
                                )}

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
                                                        className={`flex-1 px-3 py-2 rounded-xl text-sm capitalize border transition-all duration-200 ${localDifficulty === level ? 'bg-slate-800 text-white border-slate-800 shadow-md' : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-50'}`}
                                                    >
                                                        {level}
                                                    </button>
                                                ))}
                                            </div>
                                        </div>
                                    )}

                                    {/* Subskill */}
                                    <div className="space-y-2 sm:col-span-2">
                                        <p className="text-xs font-semibold text-slate-500 uppercase tracking-wide">Subskill</p>
                                        <select
                                            value={localSubskill}
                                            onChange={(e) => setLocalSubskill(e.target.value)}
                                            disabled={disableSubskillControl}
                                            className={`w-full px-3 py-3 rounded-xl border text-sm bg-white transition-all ${
                                                disableSubskillControl
                                                    ? 'border-slate-200 text-slate-400 bg-slate-50 cursor-not-allowed'
                                                    : 'border-slate-200 focus:outline-none focus:ring-2 focus:ring-slate-300 cursor-pointer'
                                            }`}
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

                                    {/* Generate Button */}
                                    <div className="flex items-end">
                                        <button
                                            onClick={handleGenerate}
                                            className="w-full rounded-xl h-12 text-sm font-semibold bg-slate-900 text-white hover:bg-slate-800 transition-all shadow-lg active:scale-95"
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
                    <div className="fixed inset-0 bg-slate-900/20 backdrop-blur-sm z-40 transition-opacity duration-300" />
                )}

                {/* ── Question Content Overlay ── */}
                {showQuestion && (
                    <div className="fixed inset-0 z-50 overflow-y-auto px-4 py-8 sm:px-6 scrollbar-hide">
                        <div className="max-w-5xl mx-auto space-y-6">

                            {/* Card 1: Header + Meta + Question Prompt */}
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
                                            className="flex items-center gap-1 px-4 py-2 rounded-xl border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 transition-colors text-sm font-medium shadow-sm"
                                        >
                                            <ChevronLeft className="h-4 w-4" />
                                            Back
                                        </button>
                                    </div>
                                </div>

                                {/* Meta Pills */}
                                <div className="flex flex-wrap items-center justify-between gap-3 text-xs">
                                    <div className="flex flex-wrap gap-2">
                                        <span className={`px-3 py-1 rounded-full border capitalize ${modeColors[localMode]}`}>
                                            {localMode}
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
                                    <div>{questionSlot}</div>
                                ) : isGenerating ? (
                                    <div className="rounded-xl border border-indigo-200 bg-indigo-50 px-6 py-8 flex flex-col items-center justify-center text-center space-y-3">
                                        <Loader2 className="w-8 h-8 text-indigo-600 animate-spin" />
                                        <p className="text-sm font-semibold text-indigo-900">
                                            Generating your question...
                                        </p>
                                        <p className="text-xs text-indigo-700 max-w-sm">
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

                            {/* Card 2: Answer / Interaction */}
                            <div className="rounded-2xl shadow-xl border border-slate-200 bg-white overflow-hidden">
                                <div className="p-4 sm:p-6">
                                    {children}
                                </div>

                                {/* Check / Compare Footer */}
                                {(onCheck || onCompare) && localMode !== 'marking' && (
                                    <div className="border-t border-slate-200 bg-slate-50 px-4 sm:px-6 py-3 flex flex-wrap gap-3">
                                        {onCheck && (
                                            <button
                                                onClick={onCheck}
                                                className={`flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold transition-all shadow-sm active:scale-95 ${
                                                    isChecked
                                                        ? 'bg-emerald-600 text-white hover:bg-emerald-700'
                                                        : 'bg-indigo-600 text-white hover:bg-indigo-700'
                                                }`}
                                            >
                                                <CheckCircle2 className="h-4 w-4" />
                                                {isChecked ? 'Checked ✓' : 'Check'}
                                            </button>
                                        )}
                                        {onCompare && isChecked && (
                                            <button
                                                onClick={onCompare}
                                                className={`flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold transition-all shadow-sm active:scale-95 ${
                                                    isComparing
                                                        ? 'bg-amber-600 text-white hover:bg-amber-700'
                                                        : 'bg-white text-slate-700 border border-slate-300 hover:bg-slate-100'
                                                }`}
                                            >
                                                <ArrowLeftRight className="h-4 w-4" />
                                                {isComparing ? 'Showing Answers' : 'Compare'}
                                            </button>
                                        )}
                                    </div>
                                )}
                            </div>

                            {/* Next Button */}
                            {onNext && (
                                <button
                                    onClick={onNext}
                                    className="w-full rounded-xl h-12 text-sm font-semibold bg-slate-900 text-white hover:bg-slate-800 transition-all shadow-lg active:scale-95"
                                >
                                    Next Question
                                </button>
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