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
    Lightbulb,
    Clock,
    ShieldCheck,
    AlertTriangle,
    Sparkles,
    Settings,
    Lock,
    CheckSquare,
    ChevronDown,
    ChevronUp
} from 'lucide-react';
import MathText from './shared/mathx/MathText';
import MathModalityRenderer from './modalities/MathModalityRenderer';
import LedgerModalityRenderer from './modalities/LedgerModalityRenderer';
import RubricModalityRenderer from './modalities/RubricModalityRenderer';
import DiagramModalityRenderer from './modalities/DiagramModalityRenderer';
import ArithmeticGridModalityRenderer from './modalities/ArithmeticGridModalityRenderer';
import GeometricNets3DViewer from './modalities/GeometricNets3DViewer';
import ElectrodynamicsMotorViewer from './modalities/ElectrodynamicsMotorViewer';
import OrganicChemistry3DViewer from './modalities/OrganicChemistry3DViewer';
import MasteryDial from '../student/MasteryDial';
import SuperAdminProgressResetModal from '../admin/SuperAdminProgressResetModal';
import TopicScopeModal from '../curriculum/TopicScopeModal';
import studentStore from '../../services/studentStore';

/**
 * UniversalWorkspace — Single unified cognitive question workspace for all Grades 7–12.
 * 
 * Option 1 Dual-Font System & Exact Simulation Box Palette:
 * - Display titles/headings: Afacad (`fontFamily: 'Afacad, sans-serif'`)
 * - Workspace cards, progression ribbon, hints, buttons, inputs: Crisp System Sans-Serif (`font-sans`)
 * - Tabular numbers, ledger coordinates, math procedures, timers: Strict `font-mono`
 * 
 * Color Palette:
 * - 60% `bg-slate-50` backdrop with pure `bg-white` cards and `border-slate-200`
 * - 30% `#13519C` Brand Blue for active progression pills, selected states, and primary brand indicators
 * - 10% purposeful cognitive feedback:
 *   * `#FF9100` / `bg-amber-50` / `border-amber-300` / `text-amber-900` for hints and diagnostic callouts
 *   * `#10B981` / `bg-emerald-50` / `border-emerald-300` / `text-emerald-800` for verified answers, marks credit
 *   * `#E11D48` / `bg-rose-50` / `border-rose-200` / `text-rose-700` for exam timer and error flags
 * 
 * Progression Hierarchy:
 * - [ 0. Diagnostic ] [ 1. Scaffold ] [ 2. Practice ] [ 3. Exam Mode ]
 * - When isDiagnosticRequired is true, active stage MUST BE '0. Diagnostic (Required)'.
 *   Stages 1, 2, 3 are clearly gated/locked with subtle 🔒 icon.
 */
/**
 * Renders multi-line prompt text cleanly:
 * - Splits into paragraphs / lines
 * - Highlights numbered transactions (e.g. "1. ", "Day 4: ") with font-mono badges & indentation
 * - Highlights bullet points ("- ", "• ") with clear indentation
 * - Formats sub-headings (e.g. "Required:", "Information:") with uppercase tracking
 * - Uses KaTeX via MathText for math expressions (\(... \) or $...$)
 * - Option 1 typography (crisp sans-serif, font-mono for monetary amounts)
 */
function renderFormattedPrompt(promptText) {
    if (!promptText || !promptText.trim()) {
        return (
            <p className="text-sm sm:text-base text-slate-500 italic font-sans">
                No question prompt loaded.
            </p>
        );
    }

    const lines = promptText.split(/\r?\n/);
    return (
        <div className="space-y-2 text-sm sm:text-base text-slate-800 leading-relaxed font-sans">
            {lines.map((rawLine, idx) => {
                const line = rawLine.trim();

                // Blank line spacer
                if (!line) {
                    return <div key={idx} className="h-1.5" />;
                }

                // Section header (e.g. "Required:", "Information:", "Transactions:", "The following balances...")
                const isHeading = /^(required|information|transactions|balances|instructions|note|statement|details):?$/i.test(line)
                    || (/^[A-Z][A-Za-z\s]+:$/.test(line) && line.length < 40);

                if (isHeading) {
                    return (
                        <div key={idx} className="pt-2 pb-0.5 border-b border-slate-200">
                            <h5 className="font-bold text-slate-900 text-xs uppercase tracking-wider font-sans">
                                {line}
                            </h5>
                        </div>
                    );
                }

                // Numbered transaction or day item (e.g. "1. ", "2) ", "Day 4:", "14. ")
                const numberedMatch = line.match(/^(\d+[.)]|\bDay\s+\d+:?)\s+(.*)$/i);
                if (numberedMatch) {
                    const [, numPrefix, content] = numberedMatch;
                    return (
                        <div key={idx} className="flex items-start gap-2.5 my-1 pl-1">
                            <span className="shrink-0 px-2 py-0.5 rounded-md bg-slate-100 text-slate-700 text-xs font-mono font-bold border border-slate-200 mt-0.5 shadow-2xs">
                                {numPrefix}
                            </span>
                            <div className="text-slate-800 text-sm leading-relaxed flex-1">
                                <MathText text={content} />
                            </div>
                        </div>
                    );
                }

                // Bullet item (e.g. "- Bank: R22 400.00", "• Trading stock...")
                const bulletMatch = line.match(/^([-•*])\s+(.*)$/);
                if (bulletMatch) {
                    const [, , content] = bulletMatch;
                    return (
                        <div key={idx} className="flex items-start gap-2.5 my-1 pl-2">
                            <span className="shrink-0 text-[#13519C] font-bold text-base leading-none mt-0.5">•</span>
                            <div className="text-slate-800 text-sm leading-relaxed flex-1">
                                <MathText text={content} />
                            </div>
                        </div>
                    );
                }

                // Standard paragraph / line
                return (
                    <p key={idx} className="text-slate-800 text-sm sm:text-base leading-relaxed">
                        <MathText text={line} />
                    </p>
                );
            })}
        </div>
    );
}

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
    onSelectTopic,
    prerequisiteBanner,
    generationError,
    result,
    isEmbedded = false,
    formativeMastery = 0,
    evaluativeScore = 0,
    initialProgressionMode,
    onProgressionModeChange,
}) {
    const subjectTitle = typeof subject === 'string' ? subject : subject?.name || 'Subject';
    const normalizedSubId = String(subjectTitle).toLowerCase().replace(/\s+/g, '_');

    // Subscribe to studentStore to reflect active live mastery
    const [storeState, setStoreState] = useState(() => studentStore.getState());
    useEffect(() => {
        const unsub = studentStore.subscribe((newState) => {
            setStoreState({ ...newState });
        });
        return unsub;
    }, []);

    const subData = storeState?.subjects?.[normalizedSubId] || studentStore.getSubject(normalizedSubId);
    const currentFormative = subData.formativeMastery ?? formativeMastery;
    const currentEvaluative = subData.evaluativeScore ?? evaluativeScore;
    
    // Diagnostic requirement check: status is 'diagnostic_required' OR 0% mastery with 0 attempts
    const isDiagnosticRequired = subData.status === 'diagnostic_required' || (currentFormative === 0 && (subData.questionsAttempted || 0) === 0);

    // Initial progression mode resolution:
    // If diagnostic is required, active mode MUST be 'diagnostic', NOT 'practice'
    const getComputedProgressionMode = () => {
        if (isDiagnosticRequired) return 'diagnostic';
        if (initialProgressionMode && initialProgressionMode !== 'diagnostic') return initialProgressionMode;
        if (currentFormative >= 80) return 'assessment';
        if (currentFormative >= 60) return 'practice';
        return 'scaffold';
    };

    const [progressionMode, setProgressionMode] = useState(getComputedProgressionMode);
    const [gateNotice, setGateNotice] = useState(null);
    const [showAdminResetModal, setShowAdminResetModal] = useState(false);
    const [showTopicModal, setShowTopicModal] = useState(false);
    const [isChecked, setIsChecked] = useState(false);
    const [isComparing, setIsComparing] = useState(false);
    const [showHints, setShowHints] = useState(false);
    const [showGuidelines, setShowGuidelines] = useState(true);
    const [activeHintTier, setActiveHintTier] = useState(1);
    const [examTimer, setExamTimer] = useState(600); // 10 minutes in seconds

    // Synchronize mode whenever subject or diagnostic status updates
    useEffect(() => {
        if (isDiagnosticRequired) {
            setProgressionMode('diagnostic');
            setShowHints(false);
        } else {
            setProgressionMode((prev) => {
                if (prev === 'diagnostic') {
                    return currentFormative >= 80 ? 'assessment' : currentFormative >= 60 ? 'practice' : 'scaffold';
                }
                return prev;
            });
        }
    }, [normalizedSubId, isDiagnosticRequired, currentFormative]);

    useEffect(() => {
        setIsChecked(false);
        setIsComparing(false);
        setShowHints(progressionMode === 'scaffold');
        setShowGuidelines(true);
    }, [question?.id, progressionMode]);

    // Exam countdown timer
    useEffect(() => {
        if (progressionMode !== 'assessment') return;
        const interval = setInterval(() => {
            setExamTimer((prev) => (prev > 0 ? prev - 1 : 0));
        }, 1000);
        return () => clearInterval(interval);
    }, [progressionMode]);

    const formatTimer = (seconds) => {
        const m = Math.floor(seconds / 60);
        const s = seconds % 60;
        return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    };

    const handleCheckWrapper = async (userAnswer) => {
        if (onCheck) {
            await onCheck(userAnswer);
            setIsChecked(true);
        }
        // If in diagnostic mode, automatically calibrate baseline from first attempt
        if (isDiagnosticRequired) {
            const scorePct = (result?.score && result?.total) 
                ? Math.round((result.score / result.total) * 100) 
                : 55;
            studentStore.completeDiagnostic(normalizedSubId, scorePct);
            setGateNotice(null);
        }
    };

    const handleCompareToggle = () => {
        if (onCompare) {
            onCompare();
        }
        setIsComparing((prev) => !prev);
    };

    const handleModeSwitch = (modeId) => {
        // If diagnostic is required, gated stages 1, 2, 3 show gentle guidance
        if (isDiagnosticRequired && modeId !== 'diagnostic') {
            setGateNotice("Complete your diagnostic baseline first to calibrate your learning path.");
            setTimeout(() => setGateNotice(null), 4500);
            return;
        }

        // If exam mode is selected before reaching 80% BKT mastery
        if (modeId === 'assessment' && currentFormative < 80) {
            setGateNotice("Reach 80% BKT Mastery in Practice to unlock Timed Exam Mode.");
            setTimeout(() => setGateNotice(null), 4500);
            return;
        }

        setGateNotice(null);
        setProgressionMode(modeId);
        if (onProgressionModeChange) onProgressionModeChange(modeId);
        if (modeId === 'scaffold') {
            setShowHints(true);
        } else {
            setShowHints(false);
        }
    };

    const handleCalibrateBaseline = (startingScore = 55) => {
        studentStore.completeDiagnostic(normalizedSubId, startingScore);
        setGateNotice(null);
        setProgressionMode(startingScore >= 60 ? 'practice' : 'scaffold');
    };

    // Extract deterministic 3-tier hints
    const rawHints = question?.hints;
    const hints = {
        tier_1: (typeof rawHints === 'object' && rawHints?.tier_1) || rawHints?.[0] || 'Carefully inspect the parameters given in the question and identify the required formula or accounting columns.',
        tier_2: (typeof rawHints === 'object' && rawHints?.tier_2) || rawHints?.[1] || question?.explanation || 'Apply standard CAPS procedural steps: isolate the unknowns and check directional signs or contra accounts.',
        tier_3: (typeof rawHints === 'object' && rawHints?.tier_3) || rawHints?.[2] || question?.worked_solution || 'Refer to the memo calculation to verify your step.'
    };

    // Determine cognitive modality from question payload or subject domain
    const modality = (() => {
        const topLower = String(topic || '').toLowerCase();
        const subLower = String(subjectTitle || '').toLowerCase();

        // 1. SOTA Visual Modalities (AI Blackboard showcase)
        if (
            question?.modality === 'geometric_nets' ||
            topLower.includes('geometry of 3d') ||
            topLower.includes('geometric net') ||
            topLower.includes('3d object') ||
            topLower.includes('platonic solid')
        ) return 'geometric_nets';

        if (
            question?.modality === 'electrodynamics' ||
            topLower.includes('electrodynamics') ||
            topLower.includes('ac generator') ||
            topLower.includes('dc motor') ||
            topLower.includes('armature')
        ) return 'electrodynamics';

        if (
            question?.modality === 'organic_chemistry' ||
            topLower.includes('organic chemistry') ||
            topLower.includes('isomer') ||
            topLower.includes('homologous series')
        ) return 'organic_chemistry';

        // 2. Fundamental & Standard Modalities
        if (
            question?.modality === 'arithmetic_grid' || 
            question?.arithmetic_grid || 
            question?.subskill === 'long_division' ||
            topLower.includes('whole numbers') ||
            topLower.includes('long division')
        ) return 'arithmetic_grid';
        if (question?.journal || question?.table_schema) return 'ledger';
        if (question?.options || question?.options_latex || question?.question_type === 'mcq') return 'math';
        if (question?.diagram_spec || question?.diagram) return 'diagram';
        if (subLower.includes('business')) return 'rubric';
        if (question?.modality) return question.modality;
        return 'math';
    })();

    // Extract authentic prompt text across all backend generator schemas
    const promptText = question?.prompt || question?.question || question?.question_text || question?.instruction || question?.prompt_latex || '';

    const isExamReady = currentFormative >= 80;

    return (
        <div className={isEmbedded ? "w-full h-full relative font-sans" : "min-h-screen bg-slate-50 relative font-sans"}>
            
            {/* Top Workspace Header (Topic, Grade, Back & Super Admin Reset) */}
            <div className="flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-slate-200">
                <div>
                    <div className="flex items-center gap-2">
                        <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-[#13519C]/10 text-[#13519C] border border-[#13519C]/20 uppercase tracking-wider font-mono">
                            Grade {grade || '10'} • {subjectTitle}
                        </span>
                        {isDiagnosticRequired ? (
                            <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-50 text-amber-800 border border-amber-300 animate-pulse font-sans">
                                0. Diagnostic Required
                            </span>
                        ) : (
                            <span className={`text-[10px] font-bold px-2 py-0.5 rounded border font-sans ${
                                isExamReady 
                                    ? 'bg-emerald-50 text-emerald-800 border-emerald-300' 
                                    : 'bg-blue-50 text-blue-800 border-blue-300'
                            }`}>
                                {isExamReady ? 'Exam Ready (Level 7)' : 'Formative Mastery Active'}
                            </span>
                        )}
                    </div>
                    <div className="flex items-center gap-2 mt-1">
                        <h2 className="text-base sm:text-lg font-bold text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                            {topic || 'Authentic CAPS Problem Solving'}
                        </h2>
                        <button
                            type="button"
                            onClick={() => setShowTopicModal(true)}
                            className="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg border border-slate-300 hover:border-[#13519C] bg-white hover:bg-blue-50 text-slate-700 hover:text-[#13519C] text-xs font-semibold shadow-2xs transition cursor-pointer font-sans"
                            title="Change Topic or Exam Scope"
                        >
                            <span>Change Topic</span>
                            <ChevronDown className="w-3 h-3" />
                        </button>
                    </div>
                </div>

                <div className="flex items-center gap-2">
                    {/* Super Admin Reset Calibration Tool */}
                    <button
                        type="button"
                        onClick={() => setShowAdminResetModal(true)}
                        className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-300 bg-white hover:bg-slate-100 text-slate-700 transition text-xs font-semibold shadow-2xs cursor-pointer font-sans"
                        title="Super Admin: Reset mastery and test diagnostic onboarding"
                    >
                        <Settings className="w-3.5 h-3.5 text-slate-500" />
                        <span className="hidden sm:inline">Admin Reset</span>
                    </button>

                    {onBack && (
                        <button
                            type="button"
                            onClick={onBack}
                            className="inline-flex items-center gap-1 px-3 py-1.5 rounded-xl border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 transition text-xs font-semibold shadow-2xs cursor-pointer font-sans"
                        >
                            <ChevronLeft className="w-3.5 h-3.5" />
                            <span>Back</span>
                        </button>
                    )}
                </div>
            </div>

            {/* ── 1. ADAPTIVE PROGRESSION MODE RIBBON (Matching HeroSimulation.jsx) ── */}
            <div className="mt-3 px-3 sm:px-4 py-2 bg-slate-50 rounded-xl border border-slate-200 flex flex-wrap items-center justify-between gap-3 text-xs">
                {/* Progression Stage Badges */}
                <div className="flex items-center gap-1.5">
                    <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 mr-1 hidden sm:inline">
                        Progression:
                    </span>
                    <div className="flex items-center gap-1 p-0.5 bg-white rounded-lg border border-slate-200 text-[11px] font-bold shadow-2xs">
                        
                        {/* Stage 0: Diagnostic */}
                        <button
                            type="button"
                            onClick={() => handleModeSwitch('diagnostic')}
                            className={`px-2.5 py-1 rounded-md transition cursor-pointer flex items-center gap-1.5 ${
                                progressionMode === 'diagnostic'
                                    ? 'bg-[#13519C] text-white shadow-2xs'
                                    : isDiagnosticRequired
                                    ? 'bg-amber-100 text-amber-900 border border-amber-300'
                                    : 'text-slate-600 hover:text-slate-900'
                            }`}
                        >
                            <span>0. Diagnostic</span>
                            {isDiagnosticRequired ? (
                                <span className="text-[9px] bg-[#FF9100] text-white px-1.5 py-0.2 rounded font-extrabold">
                                    Required
                                </span>
                            ) : (
                                <span className="text-emerald-600 font-extrabold">✓</span>
                            )}
                        </button>

                        {/* Stage 1: Scaffold */}
                        <button
                            type="button"
                            onClick={() => handleModeSwitch('scaffold')}
                            className={`px-2.5 py-1 rounded-md transition flex items-center gap-1 cursor-pointer ${
                                progressionMode === 'scaffold'
                                    ? 'bg-[#13519C] text-white shadow-2xs'
                                    : isDiagnosticRequired
                                    ? 'text-slate-400 bg-slate-50/70 opacity-70 hover:bg-slate-100'
                                    : 'text-slate-600 hover:text-slate-900'
                            }`}
                            title={isDiagnosticRequired ? "Locked: Complete diagnostic baseline first" : "Scaffold Mode: Guided 3-tier hints"}
                        >
                            <span>1. Scaffold</span>
                            {isDiagnosticRequired && <Lock className="w-2.5 h-2.5 text-slate-400" />}
                        </button>

                        {/* Stage 2: Practice */}
                        <button
                            type="button"
                            onClick={() => handleModeSwitch('practice')}
                            className={`px-2.5 py-1 rounded-md transition flex items-center gap-1 cursor-pointer ${
                                progressionMode === 'practice'
                                    ? 'bg-[#13519C] text-white shadow-2xs'
                                    : isDiagnosticRequired
                                    ? 'text-slate-400 bg-slate-50/70 opacity-70 hover:bg-slate-100'
                                    : 'text-slate-600 hover:text-slate-900'
                            }`}
                            title={isDiagnosticRequired ? "Locked: Complete diagnostic baseline first" : "Practice Mode: Autonomous problem solving"}
                        >
                            <span>2. Practice</span>
                            {isDiagnosticRequired && <Lock className="w-2.5 h-2.5 text-slate-400" />}
                        </button>

                        {/* Stage 3: Exam Mode */}
                        <button
                            type="button"
                            onClick={() => handleModeSwitch('assessment')}
                            className={`px-2.5 py-1 rounded-md transition flex items-center gap-1 cursor-pointer ${
                                progressionMode === 'assessment'
                                    ? 'bg-rose-600 text-white shadow-2xs animate-pulse'
                                    : isDiagnosticRequired || currentFormative < 80
                                    ? 'text-slate-400 bg-slate-50/70 opacity-70 hover:bg-slate-100'
                                    : 'text-slate-600 hover:text-slate-900'
                            }`}
                            title={isDiagnosticRequired ? "Locked: Complete diagnostic baseline first" : currentFormative < 80 ? "Locked: Reach 80% BKT Mastery to unlock" : "Exam Mode: Timed CAPS assessment"}
                        >
                            <span>3. Exam Mode</span>
                            {(isDiagnosticRequired || currentFormative < 80) && <Lock className="w-2.5 h-2.5 text-slate-400" />}
                        </button>
                    </div>
                </div>

                {/* Mode Guidance, Exam Timer, or Hints Toggle */}
                {progressionMode === 'assessment' ? (
                    <div className="flex items-center gap-3">
                        <div className="flex items-center gap-1.5 px-3 py-1 rounded-lg bg-rose-50 border border-rose-200 text-rose-700 font-bold font-mono text-xs">
                            <Clock className="w-3.5 h-3.5 animate-pulse text-rose-600" />
                            <span>Exam Timer: {formatTimer(examTimer)}</span>
                        </div>
                        <span className="text-[11px] text-slate-500 font-semibold hidden md:inline">
                            🛡️ Pre-baked Hints Locked in Exam
                        </span>
                    </div>
                ) : progressionMode === 'diagnostic' ? (
                    <div className="flex items-center gap-2">
                        <div className="flex items-center gap-1.5 px-3 py-1 rounded-lg bg-slate-100 text-slate-600 border border-slate-200 text-xs font-semibold select-none">
                            <ShieldCheck className="w-3.5 h-3.5 text-slate-500" />
                            <span>🛡️ Hints Locked in Diagnostic</span>
                        </div>
                    </div>
                ) : (
                    <div className="flex items-center gap-2">
                        <button
                            type="button"
                            data-testid="btn-toggle-hints"
                            onClick={() => setShowHints(!showHints)}
                            className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-bold transition cursor-pointer ${
                                showHints
                                    ? 'bg-[#FF9100] text-white shadow-2xs'
                                    : 'bg-amber-50 text-amber-900 border border-amber-300 hover:bg-amber-100'
                            }`}
                        >
                            <Lightbulb className="w-3.5 h-3.5 text-amber-600" />
                            <span>{showHints ? 'Hide 3-Tier Hints' : '💡 View 3-Tier Hints (Zero-LLM)'}</span>
                        </button>
                    </div>
                )}
            </div>

            {/* ── Gated Stage Notification Banner ── */}
            {gateNotice && (
                <div className="mt-2 px-4 py-2.5 bg-amber-50 border border-amber-300 rounded-xl flex items-center justify-between text-xs text-amber-900 shadow-2xs animate-in fade-in">
                    <div className="flex items-center gap-2">
                        <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0" />
                        <span className="font-semibold">{gateNotice}</span>
                    </div>
                    <button
                        type="button"
                        onClick={() => setGateNotice(null)}
                        className="text-amber-700 hover:text-amber-900 font-bold cursor-pointer text-xs"
                    >
                        Dismiss
                    </button>
                </div>
            )}

            {/* ── 2. 3-TIER PRE-BAKED HINTS DRAWER (Scaffold & Practice Mode) ── */}
            {showHints && progressionMode !== 'assessment' && progressionMode !== 'diagnostic' && (
                <div className="mt-2 px-4 py-3 bg-amber-50/80 border border-amber-300 rounded-xl space-y-2 text-xs font-sans animate-in fade-in">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-bold uppercase tracking-wider text-amber-900 bg-amber-200/60 border border-amber-300 px-2 py-0.5 rounded font-mono">
                                DETERMINISTIC 3-TIER HINT ENGINE
                            </span>
                            <span className="text-amber-800 text-[11px] hidden sm:inline">
                                Pre-calculated ahead of time with zero token cost
                            </span>
                        </div>
                        <div className="flex gap-1 bg-white p-0.5 rounded-lg border border-amber-200 text-[10px] font-bold shadow-2xs">
                            {[1, 2, 3].map((tier) => (
                                <button
                                    key={tier}
                                    type="button"
                                    data-testid={`btn-hint-tier-${tier}`}
                                    onClick={() => setActiveHintTier(tier)}
                                    className={`px-2.5 py-0.5 rounded transition cursor-pointer ${
                                        activeHintTier === tier
                                            ? 'bg-[#13519C] text-white font-bold'
                                            : 'text-slate-600 hover:text-slate-900'
                                    }`}
                                >
                                    Tier {tier}: {tier === 1 ? 'Nudge' : tier === 2 ? 'Rule' : 'Worked Step'}
                                </button>
                            ))}
                        </div>
                    </div>

                    <div className="p-3 bg-white border border-amber-200 rounded-xl text-slate-800 text-xs leading-relaxed shadow-2xs">
                        {activeHintTier === 1 && (
                            <div>
                                <strong className="text-amber-800 font-bold">Tier 1 (Location / Nudge):</strong> {hints.tier_1}
                            </div>
                        )}
                        {activeHintTier === 2 && (
                            <div>
                                <strong className="text-amber-800 font-bold">Tier 2 (Directional Rule):</strong> {hints.tier_2}
                            </div>
                        )}
                        {activeHintTier === 3 && (
                            <div>
                                <strong className="text-amber-800 font-bold">Tier 3 (Worked Step Calculation):</strong> {hints.tier_3}
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* ── 3. BASELINE DIAGNOSTIC CALIBRATION BANNER ── */}
            {isDiagnosticRequired && (
                <div className="mt-3 p-4 bg-amber-50 border border-amber-300 rounded-xl flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs text-amber-900 shadow-2xs animate-in fade-in">
                    <div className="flex items-start sm:items-center gap-3">
                        <div className="w-8 h-8 rounded-xl bg-amber-200/80 border border-amber-300 text-amber-900 flex items-center justify-center shrink-0 font-bold">
                            <Sparkles className="w-4 h-4 text-amber-700" />
                        </div>
                        <div>
                            <h4 className="font-bold text-sm text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                Diagnostic Baseline Active • Answer this question without hints to calibrate your starting mastery index.
                            </h4>
                            <p className="text-amber-800 text-xs mt-0.5">
                                Your baseline performance calibrates your personalized BKT trajectory and unlocks Scaffold, Practice, and Exam modes.
                            </p>
                        </div>
                    </div>
                    <div className="flex items-center gap-2 shrink-0">
                        <button
                            type="button"
                            onClick={() => handleCalibrateBaseline(55)}
                            className="px-4 py-2 rounded-xl bg-[#13519C] hover:bg-blue-800 text-white font-bold text-xs shadow-xs transition cursor-pointer"
                        >
                            Calibrate Baseline (55%)
                        </button>
                    </div>
                </div>
            )}

            {/* ── 4. MAIN QUESTION WORKSPACE & MASTERY DIAL (Exact Simulation Box Layout) ── */}
            <div className="mt-4 grid lg:grid-cols-12 gap-5 items-start">
                
                {/* Left: Problem-Solving Surface (8 cols on lg) */}
                <div className="lg:col-span-8 space-y-4">
                    <div 
                        data-testid="question-surface"
                        data-source={question?.source || (question ? 'deterministic_generator' : 'none')}
                        className="rounded-2xl border border-slate-200 bg-white p-4 sm:p-6 space-y-5 shadow-xs font-sans"
                    >
                        
                        {/* Split Question Header matching HeroSimulation.jsx */}
                        <div className="flex items-center justify-between border-b border-slate-200 pb-3">
                            <div>
                                <div className="flex items-center gap-2">
                                    <button
                                        type="button"
                                        onClick={() => setShowTopicModal(true)}
                                        className="inline-flex items-center gap-1.5 text-[10px] font-bold px-2.5 py-1 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-800 border border-emerald-300 shadow-2xs transition-all cursor-pointer group"
                                        title="Click to Change Topic or Align with School Exam Scope"
                                    >
                                        <span>Term 1 • {topic || 'CAPS Problem Solving'}</span>
                                        <ChevronDown className="w-3 h-3 text-emerald-700 group-hover:translate-y-0.5 transition-transform" />
                                    </button>
                                    <span className="text-xs text-slate-500 font-sans">
                                        {modality === 'ledger' ? 'Authentic 2D Ledger Entry' :
                                         modality === 'math' ? 'Stepwise KaTeX Symbolic Derivation' :
                                         modality === 'diagram' ? 'Geometric & Diagrammatic Model' :
                                         'Analytical Concept Evaluation'}
                                    </span>
                                </div>
                                <h4 className="text-sm sm:text-base font-bold text-slate-900 mt-1" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    {question?.title || (topic ? `${topic} Practice Problem` : 'Authentic Problem Solving')}
                                </h4>
                            </div>
                            <div className="text-right shrink-0">
                                <span className="text-[11px] text-slate-500 block font-sans">Total Marks:</span>
                                <span className="text-sm font-bold text-amber-600 font-mono">
                                    {question?.marks || 6} Marks
                                </span>
                            </div>
                        </div>

                        {/* Question Prompt */}
                        {isGenerating ? (
                            <div className="rounded-xl border border-blue-200 bg-blue-50 px-6 py-8 flex flex-col items-center justify-center text-center space-y-3">
                                <Loader2 className="w-8 h-8 text-[#13519C] animate-spin" />
                                <p className="text-sm font-semibold text-slate-900">Generating authentic question...</p>
                                <p className="text-xs text-slate-600">Deterministic values calibrated to your mastery level.</p>
                            </div>
                        ) : generationError ? (
                            <div className="rounded-xl border border-rose-200 bg-rose-50 p-4 text-xs font-semibold text-rose-800">
                                {generationError}
                            </div>
                        ) : (
                            <div className="space-y-4">
                                {renderFormattedPrompt(promptText)}
                                {Array.isArray(question?.guidelines) && question.guidelines.length > 0 && (
                                    <div className="rounded-xl border border-slate-200 bg-slate-50/70 p-3.5 space-y-2 mt-3 font-sans">
                                        <div className="flex items-center justify-between">
                                            <div className="flex items-center gap-2">
                                                <span className="w-5 h-5 rounded-md bg-[#13519C]/10 text-[#13519C] flex items-center justify-center text-xs font-bold font-mono">
                                                    📋
                                                </span>
                                                <span className="text-xs font-bold text-slate-800 uppercase tracking-wide font-sans">
                                                    Required Guidelines &amp; CAPS Checklist
                                                </span>
                                                <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-blue-100 text-[#13519C] font-mono">
                                                    {question.guidelines.length} rules
                                                </span>
                                            </div>
                                            <button
                                                type="button"
                                                onClick={() => setShowGuidelines((prev) => !prev)}
                                                className="text-xs font-semibold text-[#13519C] hover:underline cursor-pointer flex items-center gap-1 font-sans"
                                            >
                                                {showGuidelines ? (
                                                    <>Hide Guidelines <ChevronUp className="w-3.5 h-3.5" /></>
                                                ) : (
                                                    <>Show Guidelines <ChevronDown className="w-3.5 h-3.5" /></>
                                                )}
                                            </button>
                                        </div>

                                        {showGuidelines && (
                                            <div className="pt-2 border-t border-slate-200/60 grid sm:grid-cols-2 gap-2 text-xs text-slate-700">
                                                {question.guidelines.map((guideline, gIdx) => (
                                                    <div key={gIdx} className="flex items-start gap-2 bg-white p-2.5 rounded-lg border border-slate-200/60 shadow-2xs">
                                                        <CheckSquare className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
                                                        <span className="leading-snug flex-1">
                                                            <MathText text={guideline} />
                                                        </span>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                )}
                            </div>
                        )}

                        {/* Modality Interaction Slot (Ledger, Math, Rubric, Diagram) */}
                        {!isGenerating && question && (
                            <div className="space-y-4 pt-2">
                                {modality === 'ledger' && (
                                    <LedgerModalityRenderer
                                        question={question}
                                        topic={topic}
                                        onCheck={handleCheckWrapper}
                                        result={result}
                                        isChecking={isChecking}
                                        showDynamicScaffold={showHints}
                                        onToggleScaffold={() => setShowHints((prev) => !prev)}
                                    />
                                )}
                                {modality === 'rubric' && (
                                    <RubricModalityRenderer
                                        question={question}
                                        topic={topic}
                                        onCheck={handleCheckWrapper}
                                        result={result}
                                        isChecking={isChecking}
                                        showDynamicScaffold={showHints}
                                        onToggleScaffold={() => setShowHints((prev) => !prev)}
                                    />
                                )}
                                {modality === 'diagram' && (
                                    <DiagramModalityRenderer
                                        question={question}
                                        topic={topic}
                                        onCheck={handleCheckWrapper}
                                        result={result}
                                        isChecking={isChecking}
                                        showDynamicScaffold={showHints}
                                        onToggleScaffold={() => setShowHints((prev) => !prev)}
                                    />
                                )}
                                {modality === 'arithmetic_grid' && (
                                    <ArithmeticGridModalityRenderer
                                        question={question}
                                        topic={topic}
                                        onCheck={handleCheckWrapper}
                                        result={result}
                                        isChecking={isChecking}
                                        showDynamicScaffold={showHints}
                                        onToggleScaffold={() => setShowHints((prev) => !prev)}
                                    />
                                )}
                                {modality === 'geometric_nets' && (
                                    <div className="space-y-4">
                                        <GeometricNets3DViewer />
                                        <MathModalityRenderer
                                            question={question}
                                            topic={topic}
                                            onCheck={handleCheckWrapper}
                                            result={result}
                                            isChecking={isChecking}
                                            showDynamicScaffold={showHints}
                                            onToggleScaffold={() => setShowHints((prev) => !prev)}
                                        />
                                    </div>
                                )}
                                {modality === 'electrodynamics' && (
                                    <div className="space-y-4">
                                        <ElectrodynamicsMotorViewer />
                                        <MathModalityRenderer
                                            question={question}
                                            topic={topic}
                                            onCheck={handleCheckWrapper}
                                            result={result}
                                            isChecking={isChecking}
                                            showDynamicScaffold={showHints}
                                            onToggleScaffold={() => setShowHints((prev) => !prev)}
                                        />
                                    </div>
                                )}
                                {modality === 'organic_chemistry' && (
                                    <div className="space-y-4">
                                        <OrganicChemistry3DViewer />
                                        <MathModalityRenderer
                                            question={question}
                                            topic={topic}
                                            onCheck={handleCheckWrapper}
                                            result={result}
                                            isChecking={isChecking}
                                            showDynamicScaffold={showHints}
                                            onToggleScaffold={() => setShowHints((prev) => !prev)}
                                        />
                                    </div>
                                )}
                                {modality === 'math' && (
                                    <MathModalityRenderer
                                        question={question}
                                        topic={topic}
                                        onCheck={handleCheckWrapper}
                                        result={result}
                                        isChecking={isChecking}
                                        showDynamicScaffold={showHints}
                                        onToggleScaffold={() => setShowHints((prev) => !prev)}
                                    />
                                )}

                                {/* Verified Consequential Marks Banner matching HeroSimulation.jsx */}
                                {isChecked && result && (
                                    <div className="p-3 bg-emerald-50 border border-emerald-300 rounded-xl flex items-center justify-between text-xs text-emerald-900 shadow-2xs animate-in fade-in">
                                        <div className="flex items-center gap-2">
                                            <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                                            <span>
                                                {result.score ?? question?.marks ?? 6} / {result.total ?? question?.marks ?? 6} Marks Awarded • Schema Verified: {result.feedback || 'Net calculation and entry extracted accurately.'}
                                            </span>
                                        </div>
                                        <span className="font-bold text-emerald-700 bg-emerald-100 px-2.5 py-0.5 rounded shrink-0 font-mono">
                                            +35 XP
                                        </span>
                                    </div>
                                )}

                                {/* Interactive Action Footer */}
                                <div className="border-t border-slate-100 pt-3 flex flex-wrap items-center justify-between gap-3">
                                    <div>
                                        {onCompare && isChecked && (
                                            <button
                                                type="button"
                                                onClick={handleCompareToggle}
                                                className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-semibold transition cursor-pointer ${
                                                    isComparing
                                                        ? 'bg-amber-600 text-white'
                                                        : 'bg-white text-[#13519C] border border-[#13519C]/30 hover:bg-blue-50'
                                                }`}
                                            >
                                                <ArrowLeftRight className="w-3.5 h-3.5" />
                                                <span>{isComparing ? 'Hide Memo' : 'Compare Memo'}</span>
                                            </button>
                                        )}
                                    </div>

                                    {onNext && (
                                        <button
                                            type="button"
                                            data-testid="btn-next-question"
                                            onClick={onNext}
                                            className="ml-auto flex items-center gap-2 px-5 py-2 rounded-xl text-xs font-bold bg-[#FF9100] text-white hover:bg-amber-600 transition shadow-xs cursor-pointer active:scale-98"
                                        >
                                            <span>Next Problem</span>
                                            <ArrowRight className="w-3.5 h-3.5" />
                                        </button>
                                    )}
                                </div>
                            </div>
                        )}
                    </div>
                </div>

                {/* Right: Circular Dual-Ring Mastery Dial Card (4 cols on lg) */}
                <div className="lg:col-span-4 space-y-4">
                    <div className="p-5 rounded-2xl bg-white border border-slate-200 shadow-xs flex flex-col items-center text-center space-y-3 font-sans">
                        <div className="text-left w-full pb-2 border-b border-slate-100">
                            <span className="text-[10px] font-extrabold uppercase tracking-wider text-[#FF9100] block font-sans">
                                Real-Time Progress
                            </span>
                            <h4 className="text-sm font-bold text-slate-900 mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                Cognitive Mastery Dial
                            </h4>
                        </div>

                        {/* Dual-Arc Circular Gauge matching HeroSimulation */}
                        <MasteryDial
                            formativeMastery={currentFormative}
                            evaluativeScore={currentEvaluative}
                            size={140}
                            variant="light"
                        />

                        <p className="text-[11px] text-slate-500 mt-1 leading-relaxed text-center font-sans">
                            Inner ring: BKT Formative Mastery ({currentFormative}%) • Outer ring: Evaluative Exam ({currentEvaluative}%)
                        </p>
                    </div>

                    {/* Prerequisite Regression Banner (If triggered) */}
                    {prerequisiteBanner && (
                        <div className="rounded-2xl border border-amber-300 bg-amber-50/80 p-4 space-y-2 text-xs shadow-xs font-sans">
                            <div className="flex items-center gap-2">
                                <GitBranch className="w-4 h-4 text-amber-600" />
                                <span className="font-bold text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    Prerequisite Gap Identified (Grade {prerequisiteBanner.target_grade})
                                </span>
                            </div>
                            <p className="text-slate-600 leading-relaxed">
                                {prerequisiteBanner.explanation || 'Step down recommended to master foundational rules.'}
                            </p>
                            <button
                                type="button"
                                onClick={() => onStartMicroDrill && onStartMicroDrill(prerequisiteBanner)}
                                className="mt-1 text-xs font-bold text-[#13519C] hover:underline flex items-center gap-1 cursor-pointer"
                            >
                                Start 5-Min Prerequisite Drill →
                            </button>
                        </div>
                    )}
                </div>

            </div>

            {/* Super Admin Reset Modal */}
            <SuperAdminProgressResetModal
                isOpen={showAdminResetModal}
                onClose={() => setShowAdminResetModal(false)}
                activeSubject={normalizedSubId}
            />

            {/* Interactive CAPS Topic & Exam Scope Modal */}
            <TopicScopeModal
                isOpen={showTopicModal}
                onClose={() => setShowTopicModal(false)}
                subject={subjectTitle}
                grade={grade}
                currentTopic={topic}
                onSelectTopic={(newTopic) => {
                    if (onSelectTopic) {
                        onSelectTopic(newTopic);
                    }
                }}
            />

        </div>
    );
}
