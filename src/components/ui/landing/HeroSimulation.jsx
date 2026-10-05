import React, { useState, useEffect, useRef } from 'react';
import {
    Calculator,
    BookOpen,
    FlaskConical,
    Briefcase,
    Coins,
    Lightbulb,
    Clock,
    ShieldCheck,
    Award,
    CheckCircle2,
    AlertTriangle,
    Sparkles,
    Flame,
    ArrowRight,
    RotateCcw,
    Play,
    Pause,
    Zap,
    Minus,
    Square,
    X,
    GraduationCap,
} from 'lucide-react';
import { getSubjectTheme } from '../../../theme/subjectPalette';

// ═══════════════════════════════════════════════════════════════
// AUTHENTIC SUBJECT SHELF CONFIGURATION
// ═══════════════════════════════════════════════════════════════
const SUBJECTS = [
    { id: 'accounting', name: 'Accounting', icon: BookOpen, grade: 'Grade 10', mastery: 84, theme: getSubjectTheme('accounting'), accentHex: getSubjectTheme('accounting').base },
    { id: 'mathematics', name: 'Mathematics', icon: Calculator, grade: 'Grade 10', mastery: 82, theme: getSubjectTheme('mathematics'), accentHex: getSubjectTheme('mathematics').base },
    { id: 'physical_sciences', name: 'Physical Sciences', icon: FlaskConical, grade: 'Grade 10', mastery: 68, theme: getSubjectTheme('physical_sciences'), accentHex: getSubjectTheme('physical_sciences').base },
    { id: 'business_studies', name: 'Business Studies', icon: Briefcase, grade: 'Grade 10', mastery: 75, theme: getSubjectTheme('business_studies'), accentHex: getSubjectTheme('business_studies').base },
    { id: 'ems', name: 'EMS', icon: Coins, grade: 'Grade 9', mastery: 80, theme: getSubjectTheme('ems'), accentHex: getSubjectTheme('ems').base },
];

export default function HeroSimulation() {
    // ── SimuLearn Flow State ──
    const [simuStep, setSimuStep] = useState(0);
    const [isAutoPlaying, setIsAutoPlaying] = useState(true);
    const [selectedSubject, setSelectedSubject] = useState(SUBJECTS[0]); // Accounting
    const [progressionMode, setProgressionMode] = useState('scaffold'); // 'diagnostic' | 'scaffold' | 'practice' | 'assessment'

    // ── Interactive In-Subject State ──
    const [showHints, setShowHints] = useState(false);
    const [activeHintTier, setActiveHintTier] = useState(1);
    const [accountingFilled, setAccountingFilled] = useState({ bank: '', sales: '', vat: '' });
    const [mathStepSubmitted, setMathStepSubmitted] = useState(false);

    // ── Adaptive Progress Dial State ──
    const [formativeMastery, setFormativeMastery] = useState(68);
    const [evaluativeScore, setEvaluativeScore] = useState(72);

    // ── Exam Simulation State ──
    const [examTimer, setExamTimer] = useState(2698); // 44:58
    const [examSubmitted, setExamSubmitted] = useState(false);
    const [selectedExamOption, setSelectedExamOption] = useState(null);

    const timerRef = useRef(null);

    // ═══════════════════════════════════════════════════════════
    // SIMULEARN ORCHESTRATION LOOP
    // ═══════════════════════════════════════════════════════════
    useEffect(() => {
        if (!isAutoPlaying) return;

        let timeoutId;

        if (simuStep === 0) {
            // STEP 0: Accounting Practice & 3-Tier Hints
            setSelectedSubject(SUBJECTS[0]); // Accounting
            setProgressionMode('scaffold');
            setExamSubmitted(false);

            timeoutId = setTimeout(() => {
                setShowHints(true);
                setActiveHintTier(1);

                setTimeout(() => {
                    setActiveHintTier(2);

                    setTimeout(() => {
                        setActiveHintTier(3);
                        setAccountingFilled({ bank: '11 500', sales: '10 000', vat: '1 500' });

                        setTimeout(() => {
                            setSimuStep(1);
                        }, 3000);
                    }, 2600);
                }, 2400);
            }, 2500);

        } else if (simuStep === 1) {
            // STEP 1: Adaptive Progression & Progress Dial Update
            setProgressionMode('practice');
            setShowHints(false);

            let curr = 68;
            const interval = setInterval(() => {
                curr += 1;
                setFormativeMastery(curr);
                setEvaluativeScore(Math.min(curr + 4, 88));
                if (curr >= 84) {
                    clearInterval(interval);
                    timeoutId = setTimeout(() => {
                        setSimuStep(2);
                    }, 4000);
                }
            }, 55);

            return () => clearInterval(interval);

        } else if (simuStep === 2) {
            // STEP 2: Subject Navigation (Switch to Mathematics)
            setSelectedSubject(SUBJECTS[1]); // Mathematics
            setProgressionMode('practice');
            setMathStepSubmitted(false);

            timeoutId = setTimeout(() => {
                setMathStepSubmitted(true);

                setTimeout(() => {
                    setSimuStep(3);
                }, 3500);
            }, 2800);

        } else if (simuStep === 3) {
            // STEP 3: Timed Exam Mode & Post-Exam Autopsy
            setProgressionMode('assessment');
            setSelectedSubject(SUBJECTS[0]); // Accounting Exam
            setSelectedExamOption('A');

            timeoutId = setTimeout(() => {
                setExamSubmitted(true);

                setTimeout(() => {
                    setSimuStep(0);
                    setAccountingFilled({ bank: '', sales: '', vat: '' });
                    setFormativeMastery(68);
                    setEvaluativeScore(72);
                }, 9000);
            }, 3500);
        }

        return () => clearTimeout(timeoutId);
    }, [simuStep, isAutoPlaying]);

    // Live countdown timer for exam mode
    useEffect(() => {
        if (progressionMode === 'assessment' && !examSubmitted) {
            timerRef.current = setInterval(() => {
                setExamTimer((t) => (t > 0 ? t - 1 : 0));
            }, 1000);
        } else {
            clearInterval(timerRef.current);
        }
        return () => clearInterval(timerRef.current);
    }, [progressionMode, examSubmitted]);

    const formatTimer = (secs) => {
        const m = Math.floor(secs / 60);
        const s = secs % 60;
        return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    };

    // Manual navigation handler
    const handleStepJump = (stepIndex) => {
        setIsAutoPlaying(false);
        setSimuStep(stepIndex);
        if (stepIndex === 0) {
            setSelectedSubject(SUBJECTS[0]);
            setProgressionMode('scaffold');
            setShowHints(true);
            setActiveHintTier(3);
            setAccountingFilled({ bank: '11 500', sales: '10 000', vat: '1 500' });
            setExamSubmitted(false);
        } else if (stepIndex === 1) {
            setProgressionMode('practice');
            setFormativeMastery(84);
            setEvaluativeScore(88);
            setShowHints(false);
            setExamSubmitted(false);
        } else if (stepIndex === 2) {
            setSelectedSubject(SUBJECTS[1]);
            setProgressionMode('practice');
            setMathStepSubmitted(true);
            setShowHints(false);
            setExamSubmitted(false);
        } else if (stepIndex === 3) {
            setProgressionMode('assessment');
            setSelectedSubject(SUBJECTS[0]);
            setSelectedExamOption('A');
            setExamSubmitted(true);
        }
    };

    // ═══════════════════════════════════════════════════════════
    // CIRCULAR DUAL-RING MASTERY DIAL
    // ═══════════════════════════════════════════════════════════
    const renderMasteryDial = (size = 140, strokeWidth = 9) => {
        const center = size / 2;
        const outerRadius = center - strokeWidth;
        const innerRadius = outerRadius - strokeWidth - 4;

        const outerCircumference = 2 * Math.PI * outerRadius;
        const innerCircumference = 2 * Math.PI * innerRadius;

        const outerStrokeDashoffset = outerCircumference - (evaluativeScore / 100) * outerCircumference;
        const innerStrokeDashoffset = innerCircumference - (formativeMastery / 100) * innerCircumference;

        const isExamReady = formativeMastery >= 80;

        return (
            <div className="flex flex-col items-center justify-center p-4 sm:p-5 bg-white rounded-2xl border border-slate-200 shadow-xs font-sans">
                <div className="relative" style={{ width: size, height: size }}>
                    <svg width={size} height={size} className="transform -rotate-90">
                        {/* Outer Track (Evaluative Exam) */}
                        <circle cx={center} cy={center} r={outerRadius} fill="transparent" stroke="rgba(203, 213, 225, 0.4)" strokeWidth={strokeWidth} />
                        <circle
                            cx={center}
                            cy={center}
                            r={outerRadius}
                            fill="transparent"
                            stroke="#F59E0B"
                            strokeWidth={strokeWidth}
                            strokeDasharray={outerCircumference}
                            strokeDashoffset={outerStrokeDashoffset}
                            strokeLinecap="round"
                            className="transition-all duration-700 ease-out"
                        />

                        {/* Inner Track (Formative BKT Mastery) */}
                        <circle cx={center} cy={center} r={innerRadius} fill="transparent" stroke="rgba(203, 213, 225, 0.3)" strokeWidth={strokeWidth} />
                        <circle
                            cx={center}
                            cy={center}
                            r={innerRadius}
                            fill="transparent"
                            stroke="#10B981"
                            strokeWidth={strokeWidth}
                            strokeDasharray={innerCircumference}
                            strokeDashoffset={innerStrokeDashoffset}
                            strokeLinecap="round"
                            className="transition-all duration-700 ease-out"
                        />
                    </svg>

                    {/* Center Percentage Display */}
                    <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
                        <span className="text-2xl font-bold text-slate-900 tracking-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>
                            {formativeMastery}%
                        </span>
                        <span className="text-[9px] uppercase font-bold text-slate-500 tracking-wider">
                            BKT Mastery
                        </span>
                    </div>
                </div>

                {/* Level Badge */}
                <div className={`mt-3 px-3 py-1 rounded-full border text-xs font-bold flex items-center gap-1.5 ${
                    isExamReady
                        ? 'bg-emerald-50 text-emerald-800 border-emerald-300 ring-1 ring-emerald-400/20'
                        : 'bg-blue-50 text-blue-800 border-blue-300'
                }`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                    <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
                    <span>{isExamReady ? 'Exam Ready (Level 7)' : 'Proficient (Level 5)'}</span>
                </div>
            </div>
        );
    };

    return (
        <div className="relative w-full select-none" style={{ minHeight: '660px' }}>
            
            {/* ═══════════════════════════════════════════════════════════════ */}
            {/* 1. DESKTOP VIEWPORT (Windows 11 PWA + Universal Workspace)     */}
            {/* ═══════════════════════════════════════════════════════════════ */}
            <div className="hidden sm:flex flex-col rounded-2xl bg-white border border-slate-300 shadow-xl overflow-hidden text-slate-800">
                
                {/* ── Level 1: System Title Bar (Windows 11 Controls ─, □, ✕ + URL route pill) ── */}
                <div className="px-3 sm:px-4 py-1.5 bg-slate-100 border-b border-slate-200 flex items-center justify-between gap-3 text-xs select-none">
                    <div className="flex items-center gap-2">
                        <GraduationCap className="w-4 h-4 text-[#FF9100] shrink-0" title="Fundile Desktop App" />
                        <span className="font-semibold text-slate-700 text-[11px] sm:text-xs tracking-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>
                            Fundile — Learner Workspace ({selectedSubject.grade} {selectedSubject.name})
                        </span>
                        <div className="flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-white border border-slate-200 font-mono text-[10px] text-slate-500 shadow-2xs">
                            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                            <span>app.fundile.co.za/workspace</span>
                        </div>
                    </div>

                    <div className="flex items-center -mr-2">
                        <button type="button" title="Minimize" className="w-10 h-7 flex items-center justify-center hover:bg-slate-200 text-slate-600 transition">
                            <Minus className="w-3.5 h-3.5" />
                        </button>
                        <button type="button" title="Maximize" className="w-10 h-7 flex items-center justify-center hover:bg-slate-200 text-slate-600 transition">
                            <Square className="w-3 h-3" />
                        </button>
                        <button type="button" title="Close" className="w-10 h-7 flex items-center justify-center hover:bg-rose-500 hover:text-white text-slate-600 transition">
                            <X className="w-3.5 h-3.5" />
                        </button>
                    </div>
                </div>

                {/* ── Level 2: User Ribbon (bg-[#13519C] with learner avatar, grade, streak, and XP) ── */}
                <div className="px-4 py-2.5 bg-[#13519C] text-white flex items-center justify-between gap-3 text-xs">
                    <div className="flex items-center gap-2.5">
                        <div className="w-6 h-6 rounded-lg bg-white/15 border border-white/25 flex items-center justify-center shrink-0 shadow-xs">
                            <GraduationCap className="w-4 h-4 text-[#FF9100]" />
                        </div>
                        <div>
                            <span className="font-bold text-sm tracking-tight text-white block leading-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>FUNDILE</span>
                            <span className="hidden md:block text-blue-200 text-[10px] leading-tight font-medium">Learn • Practice • Progress</span>
                        </div>
                    </div>

                    <div className="flex items-center gap-2">
                        <div className="w-7 h-7 rounded-full bg-white text-[#13519C] flex items-center justify-center font-bold text-xs shadow-xs">
                            N
                        </div>
                        <div className="text-left">
                            <span className="font-bold text-white block text-xs leading-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>Nqobile Dlamini</span>
                            <span className="text-[10px] text-blue-100 block leading-tight">Grade 10 FET • Westville High School</span>
                        </div>
                    </div>

                    <div className="flex items-center gap-2">
                        <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-amber-500/20 border border-amber-300/40 text-amber-200 text-xs font-bold">
                            <Flame className="w-3.5 h-3.5 text-[#FF9100] fill-[#FF9100]" />
                            <span>5 Days</span>
                        </div>
                        <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-blue-800/80 border border-blue-400/40 text-blue-100 text-xs font-bold">
                            <Zap className="w-3.5 h-3.5 text-blue-300" />
                            <span>1,420 XP</span>
                        </div>
                    </div>
                </div>

                {/* ── Level 3: Folder Tabs (Authentic slanted corner clip-path, seamless tab-to-folder connection) ── */}
                <div className="w-full bg-[#E6EDF5] border-b border-slate-300 px-4 pt-3 overflow-x-auto scrollbar-none flex items-end gap-0 select-none">
                    {SUBJECTS.map((sub) => {
                        const Icon = sub.icon;
                        const isSelected = selectedSubject.id === sub.id;

                        return (
                            <button
                                key={sub.id}
                                type="button"
                                onClick={() => {
                                    setIsAutoPlaying(false);
                                    setSelectedSubject(sub);
                                }}
                                className={`folder-tab group shrink-0 min-w-[125px] max-w-[200px] px-3.5 py-2.5 flex items-center justify-center gap-2 text-xs font-bold transition-all cursor-pointer relative select-none ${
                                    isSelected ? 'active' : 'inactive'
                                }`}
                                style={{
                                    clipPath: 'polygon(14px 0, 100% 0, 100% 100%, 0 100%, 0 14px)',
                                    WebkitClipPath: 'polygon(14px 0, 100% 0, 100% 100%, 0 100%, 0 14px)',
                                    zIndex: isSelected ? 30 : 10,
                                    transform: isSelected ? 'translateY(-3px)' : 'translateY(2px)',
                                    backgroundColor: isSelected ? '#FFFFFF' : (sub.theme?.soft || '#F1F5F9'),
                                    color: isSelected ? (sub.theme?.text || '#0F172A') : '#334155',
                                    borderBottom: isSelected ? '2px solid #FFFFFF' : '1px solid #CBD5E1',
                                    boxShadow: isSelected ? '0 -6px 16px -2px rgba(0, 0, 0, 0.12)' : 'none',
                                    fontFamily: 'Afacad, sans-serif'
                                }}
                            >
                                <svg className="absolute inset-0 w-full h-full pointer-events-none overflow-visible" preserveAspectRatio="none">
                                    <path
                                        d="M 0 14 L 14 0 H 1000"
                                        stroke={sub.accentHex}
                                        strokeWidth={isSelected ? 4 : 2}
                                        fill="none"
                                        vectorEffect="non-scaling-stroke"
                                    />
                                </svg>
                                <span className="w-2 h-2 rounded-full shrink-0" style={{ backgroundColor: sub.accentHex }} />
                                <Icon className="w-3.5 h-3.5 shrink-0" style={{ color: sub.accentHex }} />
                                <span className="truncate">{sub.name}</span>
                                <span 
                                    className="text-[10px] px-1.5 py-0.2 rounded-full font-bold"
                                    style={{
                                        backgroundColor: isSelected ? sub.theme?.base : sub.theme?.soft,
                                        color: isSelected ? '#FFFFFF' : sub.theme?.text,
                                    }}
                                >
                                    {sub.mastery}%
                                </span>
                            </button>
                        );
                    })}
                </div>

                {/* Connecting Accent Line */}
                <div
                    className="h-[3px] w-full transition-colors duration-300"
                    style={{ backgroundColor: selectedSubject.accentHex }}
                />

                {/* ── Level 4: 4-Stage Progression Ribbon & Hints Controls ── */}
                <div className="px-4 py-2 bg-slate-50 border-b border-slate-200 flex flex-wrap items-center justify-between gap-3 text-xs">
                    <div className="flex items-center gap-1.5">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 mr-1" style={{ fontFamily: 'Afacad, sans-serif' }}>
                            Progression:
                        </span>
                        <div className="flex items-center gap-1 p-0.5 bg-white rounded-lg border border-slate-200 text-[11px] font-bold shadow-xs">
                            <span className={`px-2.5 py-1 rounded-md transition ${
                                progressionMode === 'diagnostic' ? 'bg-[#13519C] text-white shadow-xs' : 'text-slate-500'
                            }`}>
                                0. Diagnostic
                            </span>
                            <span className={`px-2.5 py-1 rounded-md transition ${
                                progressionMode === 'scaffold' ? 'bg-[#13519C] text-white shadow-xs' : 'text-slate-500'
                            }`}>
                                1. Scaffold
                            </span>
                            <span className={`px-2.5 py-1 rounded-md transition ${
                                progressionMode === 'practice' ? 'bg-[#13519C] text-white shadow-xs' : 'text-slate-500'
                            }`}>
                                2. Practice
                            </span>
                            <span className={`px-2.5 py-1 rounded-md transition ${
                                progressionMode === 'assessment' ? 'bg-rose-600 text-white shadow-xs animate-pulse' : 'text-slate-500'
                            }`}>
                                3. Exam Mode
                            </span>
                        </div>
                    </div>

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
                    ) : (
                        <div className="flex items-center gap-2">
                            <button
                                type="button"
                                onClick={() => setShowHints(!showHints)}
                                className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-bold transition cursor-pointer ${
                                    showHints
                                        ? 'bg-[#FF9100] text-white shadow-xs'
                                        : 'bg-amber-50 text-amber-900 border border-amber-300 hover:bg-amber-100'
                                }`}
                                style={{ fontFamily: 'Afacad, sans-serif' }}
                            >
                                <Lightbulb className="w-3.5 h-3.5 text-amber-600" />
                                <span>{showHints ? 'Hide 3-Tier Hints' : '💡 View 3-Tier Hints (Zero-LLM)'}</span>
                            </button>
                        </div>
                    )}
                </div>

                {/* ── 3-Tier Pre-baked Hints Drawer ── */}
                {showHints && progressionMode !== 'assessment' && (
                    <div className="px-4 py-3 bg-amber-50/80 border-b border-amber-200 space-y-2 text-xs">
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-2">
                                <span className="text-[10px] font-bold uppercase tracking-wider text-amber-900 bg-amber-200/60 border border-amber-300 px-2 py-0.5 rounded">
                                    DETERMINISTIC 3-TIER HINT ENGINE
                                </span>
                                <span className="text-amber-800 text-[11px] hidden sm:inline">
                                    Pre-calculated ahead of time with zero token latency
                                </span>
                            </div>
                            <div className="flex gap-1 bg-white p-0.5 rounded-lg border border-amber-200 text-[10px] font-bold shadow-xs">
                                {[1, 2, 3].map((tier) => (
                                    <button
                                        key={tier}
                                        type="button"
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

                        <div className="p-3 bg-white border border-amber-200 rounded-xl text-slate-800 text-xs leading-relaxed shadow-xs">
                            {activeHintTier === 1 && (
                                <div>
                                    <strong className="text-amber-800 font-bold">Tier 1 (Location / Nudge):</strong> Direct attention to the Bank Gross column and Output VAT breakdown for inclusive transactions.
                                </div>
                            )}
                            {activeHintTier === 2 && (
                                <div>
                                    <strong className="text-amber-800 font-bold">Tier 2 (Directional Rule):</strong> When the sale is inclusive of 15% VAT, the gross Bank receipt represents 115%. To extract VAT, multiply by 15/115.
                                </div>
                            )}
                            {activeHintTier === 3 && (
                                <div>
                                    <strong className="text-amber-800 font-bold">Tier 3 (Worked Step Calculation):</strong> VAT = R11,500 × 15/115 = R1,500. Sales (exclusive) = R11,500 − R1,500 = R10,000.
                                </div>
                            )}
                        </div>
                    </div>
                )}

                {/* ── Active Workspace Body (Desktop) ── */}
                <div className="p-5 sm:p-6 flex-1 bg-slate-50 flex flex-col justify-center min-h-[380px]">
                    {/* SCENARIO A: ACCOUNTING 2D LEDGER TABLE */}
                    {simuStep === 0 && selectedSubject.id === 'accounting' && (
                        <div className="space-y-4">
                            <div className="flex items-center justify-between border-b border-slate-200 pb-3">
                                <div>
                                    <div className="flex items-center gap-2">
                                        <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200">
                                            Term 1 • Cash Receipts Journal (CRJ)
                                        </span>
                                        <span className="text-xs text-slate-500">Authentic 2D Ledger Entry</span>
                                    </div>
                                    <h4 className="text-sm sm:text-base font-bold text-slate-900 mt-1" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                        Record Cash Sales of Merchandise: R11,500 (inclusive of 15% VAT)
                                    </h4>
                                </div>
                                <div className="text-right">
                                    <span className="text-[11px] text-slate-500 block">Total Marks:</span>
                                    <span className="text-sm font-bold text-amber-600">6 Marks</span>
                                </div>
                            </div>

                            <div className="overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-xs">
                                <table className="w-full text-xs text-left">
                                    <thead className="bg-slate-100 text-slate-700 border-b border-slate-200 uppercase text-[10px] font-bold">
                                        <tr>
                                            <th className="p-2.5">Day</th>
                                            <th className="p-2.5">Details</th>
                                            <th className="p-2.5">Bank (Gross 115%)</th>
                                            <th className="p-2.5">Sales (Excl 100%)</th>
                                            <th className="p-2.5">Output VAT (15%)</th>
                                            <th className="p-2.5">Cost of Sales</th>
                                        </tr>
                                    </thead>
                                    <tbody className="divide-y divide-slate-100 font-mono text-xs">
                                        <tr>
                                            <td className="p-2.5 text-slate-600">12</td>
                                            <td className="p-2.5 text-slate-800">Cash / CRT</td>
                                            <td className="p-2">
                                                <input
                                                    type="text"
                                                    readOnly
                                                    value={accountingFilled.bank}
                                                    placeholder="e.g. 11 500"
                                                    className={`w-28 px-2.5 py-1.5 rounded-lg border text-xs font-bold transition ${
                                                        accountingFilled.bank ? 'bg-emerald-50 border-emerald-500 text-emerald-800' : 'bg-slate-50 border-slate-300 text-slate-700'
                                                    }`}
                                                />
                                            </td>
                                            <td className="p-2">
                                                <input
                                                    type="text"
                                                    readOnly
                                                    value={accountingFilled.sales}
                                                    placeholder="e.g. 10 000"
                                                    className={`w-28 px-2.5 py-1.5 rounded-lg border text-xs font-bold transition ${
                                                        accountingFilled.sales ? 'bg-emerald-50 border-emerald-500 text-emerald-800' : 'bg-slate-50 border-slate-300 text-slate-700'
                                                    }`}
                                                />
                                            </td>
                                            <td className="p-2">
                                                <input
                                                    type="text"
                                                    readOnly
                                                    value={accountingFilled.vat}
                                                    placeholder="e.g. 1 500"
                                                    className={`w-24 px-2.5 py-1.5 rounded-lg border text-xs font-bold transition ${
                                                        accountingFilled.vat ? 'bg-emerald-50 border-emerald-500 text-emerald-800' : 'bg-slate-50 border-slate-300 text-slate-700'
                                                    }`}
                                                />
                                            </td>
                                            <td className="p-2.5 text-slate-600">8 000</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>

                            {accountingFilled.vat && (
                                <div className="p-3 bg-emerald-50 border border-emerald-300 rounded-xl flex items-center justify-between text-xs text-emerald-950 font-bold shadow-xs animate-in fade-in">
                                    <div className="flex items-center gap-2">
                                        <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                                        <span>6 / 6 Marks Credited • Net VAT extracted accurately (15/115) • Consequential accuracy validated</span>
                                    </div>
                                    <span className="px-2.5 py-1 rounded-full bg-emerald-600 text-white font-extrabold text-[11px] shadow-xs shrink-0">
                                        +35 XP
                                    </span>
                                </div>
                            )}
                        </div>
                    )}

                    {/* SCENARIO B: ADAPTIVE MASTERY DIAL */}
                    {simuStep === 1 && (
                        <div className="grid md:grid-cols-12 gap-6 items-center">
                            <div className="md:col-span-5 flex flex-col items-center">
                                {renderMasteryDial(160, 10)}
                                <span className="text-[11px] text-slate-500 mt-2 text-center">
                                    Inner: BKT Formative Mastery ({formativeMastery}%) • Outer: Evaluative Score ({evaluativeScore}%)
                                </span>
                            </div>

                            <div className="md:col-span-7 space-y-3">
                                <div>
                                    <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-bold">
                                        <Award className="w-3.5 h-3.5 text-emerald-600" />
                                        <span>Mastery Threshold Achieved</span>
                                    </div>
                                    <h4 className="text-lg font-bold text-slate-900 mt-1" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                        Adaptive Progression: Scaffold &rarr; Exam Ready Mode
                                    </h4>
                                    <p className="text-xs text-slate-600 mt-1">
                                        Fundile continuously estimates your latent knowledge state P(L_n). Crossing 80% automatically unlocks Timed Exam Mode and reduces scaffold hints.
                                    </p>
                                </div>

                                <div className="grid grid-cols-2 gap-2 text-xs">
                                    <div className="p-3 rounded-xl bg-white border border-slate-200 shadow-xs">
                                        <span className="text-[10px] uppercase font-bold text-slate-400 block">Formative Mastery</span>
                                        <span className="text-xl font-bold text-emerald-600 mt-0.5 block">{formativeMastery}%</span>
                                        <span className="text-[11px] text-slate-500">Autonomous BKT Trajectory</span>
                                    </div>
                                    <div className="p-3 rounded-xl bg-white border border-slate-200 shadow-xs">
                                        <span className="text-[10px] uppercase font-bold text-slate-400 block">Evaluative Homework</span>
                                        <span className="text-xl font-bold text-amber-600 mt-0.5 block">{evaluativeScore}%</span>
                                        <span className="text-[11px] text-slate-500">Weighted Summative Score</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* SCENARIO C: MATHEMATICS FACTORISATION STEP */}
                    {simuStep === 2 && selectedSubject.id === 'mathematics' && (
                        <div className="space-y-4">
                            <div className="flex items-center justify-between border-b border-slate-200 pb-3">
                                <div>
                                    <div className="flex items-center gap-2">
                                        <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-50 text-blue-800 border border-blue-200">
                                            Grade 10 Mathematics • Topic 2.3
                                        </span>
                                        <span className="text-xs text-slate-500">Trinomial Factorisation Drill</span>
                                    </div>
                                    <h4 className="text-base font-bold text-slate-900 mt-1" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                        Factorise completely: <span className="font-mono bg-slate-100 px-2 py-0.5 rounded text-blue-900 font-bold">x² − 7x + 12</span>
                                    </h4>
                                </div>
                                <div className="text-right">
                                    <span className="text-[11px] text-slate-500 block">Mark Allocation:</span>
                                    <span className="text-sm font-bold text-blue-600">3 Marks</span>
                                </div>
                            </div>

                            <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-xs space-y-3">
                                <div className="flex items-center gap-3">
                                    <span className="text-xs font-semibold text-slate-600">Your Working:</span>
                                    <div className={`px-4 py-2 rounded-lg border font-mono text-sm font-bold flex items-center gap-2 ${
                                        mathStepSubmitted ? 'bg-blue-50 border-blue-400 text-blue-900 shadow-xs' : 'bg-slate-50 border-slate-300 text-slate-400'
                                    }`}>
                                        <span>{mathStepSubmitted ? '(x − 3)(x − 4)' : '( x ... )( x ... )'}</span>
                                        {mathStepSubmitted && <CheckCircle2 className="w-4 h-4 text-emerald-600" />}
                                    </div>
                                </div>

                                {mathStepSubmitted && (
                                    <div className="p-3 bg-emerald-50 border border-emerald-300 rounded-xl flex items-center justify-between text-xs text-emerald-950 font-bold shadow-xs animate-in fade-in">
                                        <div className="flex items-center gap-2">
                                            <Sparkles className="w-4 h-4 text-emerald-600 shrink-0" />
                                            <span>SymPy Symbolic Equivalence Verified: (−3) + (−4) = −7 and (−3) × (−4) = +12.</span>
                                        </div>
                                        <span className="px-2.5 py-1 rounded-full bg-emerald-600 text-white font-extrabold text-[11px] shadow-xs shrink-0">
                                            +35 XP
                                        </span>
                                    </div>
                                )}
                            </div>
                        </div>
                    )}

                    {/* SCENARIO D: TIMED EXAM MODE & POST-EXAM DIAGNOSTIC AUTOPSY */}
                    {simuStep === 3 && (
                        <div className="space-y-4">
                            {!examSubmitted ? (
                                <div className="p-4 sm:p-5 bg-white border border-rose-200 rounded-2xl space-y-4 shadow-xs">
                                    <div className="flex items-center justify-between border-b border-slate-100 pb-2.5">
                                        <div className="flex items-center gap-2">
                                            <span className="px-2 py-0.5 rounded bg-rose-100 text-rose-800 text-[10px] font-bold">
                                                EXAM QUESTION 1 OF 15
                                            </span>
                                            <span className="text-xs font-bold text-slate-700">Accounting Paper 1 • June Exam</span>
                                        </div>
                                        <span className="text-xs font-bold text-slate-500">4 Marks</span>
                                    </div>

                                    <p className="text-xs text-slate-800 font-medium">
                                        A business purchased stock costing R2,300 (VAT inclusive at 15%). Calculate the Output VAT amount:
                                    </p>

                                    <div className="space-y-2 text-xs">
                                        <div className={`p-3 rounded-xl border flex items-center justify-between ${
                                            selectedExamOption === 'A'
                                                ? 'bg-blue-50/70 border-[#13519C] text-[#13519C] font-semibold'
                                                : 'bg-white border-slate-200 text-slate-700'
                                        }`}>
                                            <span>Option A: R300.00 (Calculated via 15/115 × R2,300)</span>
                                            <span className="font-bold text-[#13519C]">Selected ✓</span>
                                        </div>
                                        <div className="p-3 rounded-xl border bg-white border-slate-200 text-slate-600">
                                            <span>Option B: R345.00 (Calculated via 15/100 × R2,300)</span>
                                        </div>
                                    </div>

                                    <div className="flex justify-end pt-2">
                                        <button
                                            type="button"
                                            onClick={() => setExamSubmitted(true)}
                                            className="px-5 py-2 rounded-xl bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold shadow-md cursor-pointer flex items-center gap-2"
                                        >
                                            <span>Submit Exam Paper</span>
                                            <ArrowRight className="w-3.5 h-3.5" />
                                        </button>
                                    </div>
                                </div>
                            ) : (
                                <div className="p-4 sm:p-5 bg-amber-50/60 border border-amber-300 rounded-2xl space-y-3 text-xs shadow-xs animate-in zoom-in-95">
                                    <div className="flex items-center justify-between border-b border-amber-200 pb-2.5">
                                        <div className="flex items-center gap-2">
                                            <AlertTriangle className="w-4 h-4 text-amber-600" />
                                            <span className="font-bold text-sm text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                                Post-Exam Diagnostic Autopsy
                                            </span>
                                            <span className="text-[10px] bg-amber-200/70 text-amber-900 px-2 py-0.5 rounded font-bold">
                                                Exam Report
                                            </span>
                                        </div>
                                        <span className="text-slate-600 font-semibold text-[11px]">Score: 42 / 50 Marks (84%)</span>
                                    </div>

                                    <div className="grid sm:grid-cols-2 gap-3 text-left">
                                        <div className="p-3 rounded-xl bg-white border border-slate-200 shadow-xs">
                                            <span className="text-[10px] font-bold text-rose-700 uppercase tracking-wider block">
                                                Predictable Cognitive Flaw Isolated:
                                            </span>
                                            <p className="text-xs text-slate-800 mt-1 font-semibold">
                                                Net vs. Gross VAT Inversion (`net_vs_gross_confusion`)
                                            </p>
                                            <span className="text-[11px] text-slate-500 mt-0.5 block">
                                                18 of 28 learners in cohort followed this exact flawed procedure.
                                            </span>
                                        </div>

                                        <div className="p-3 rounded-xl bg-white border border-slate-200 shadow-xs">
                                            <span className="text-[10px] font-bold text-emerald-700 uppercase tracking-wider block">
                                                Consequential Marking Audit:
                                            </span>
                                            <p className="text-xs text-slate-800 mt-1 font-semibold">
                                                2 of 4 Method Marks Credited
                                            </p>
                                            <span className="text-[11px] text-slate-500 mt-0.5 block">
                                                Fundile credited correct ledger categorization despite the arithmetic slip.
                                            </span>
                                        </div>
                                    </div>

                                    <div className="p-2.5 rounded-xl bg-white border border-amber-200 text-[11px] text-amber-900 flex items-center justify-between shadow-xs">
                                        <span>Automated Remedial Drill: 5-minute targeted VAT exclusive/inclusive exercise dispatched.</span>
                                        <span className="font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded border border-amber-200">Ready</span>
                                    </div>
                                </div>
                            )}
                        </div>
                    )}
                </div>

            </div>

            {/* ═══════════════════════════════════════════════════════════════ */}
            {/* 2. MOBILE VIEWPORT (Phone Chassis Matching MobileWebApkView)   */}
            {/* ═══════════════════════════════════════════════════════════════ */}
            <div className="block sm:hidden w-full max-w-[340px] mx-auto bg-slate-900 p-2.5 rounded-[36px] shadow-2xl border-4 border-slate-700 select-none text-slate-800">
                {/* Phone Top Notch / Camera Pill */}
                <div className="w-16 h-3 bg-black rounded-full mx-auto mb-1.5" />

                {/* Inner Screen */}
                <div className="rounded-[24px] overflow-hidden bg-white flex flex-col shadow-inner">
                    {/* Android Status Bar */}
                    <div className="px-3.5 pt-1.5 pb-1 bg-[#13519C] text-white flex items-center justify-between text-[10px] font-mono select-none">
                        <span>14:30</span>
                        <div className="flex items-center gap-1.5 text-[9px]">
                            <span className="bg-blue-800/80 px-1 py-0.2 rounded border border-blue-400/30">LTE</span>
                            <span>📶</span>
                            <span>🔋 88%</span>
                        </div>
                    </div>

                    {/* Collapsible Profile Ribbon */}
                    <div className="px-3 py-2 bg-[#13519C] text-white flex items-center justify-between border-t border-blue-800/40 text-xs">
                        <div className="flex items-center gap-2">
                            <div className="w-6 h-6 rounded-full bg-white text-[#13519C] flex items-center justify-center font-bold text-[10px]">
                                N
                            </div>
                            <div>
                                <span className="font-bold text-[11px] block leading-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>Nqobile Dlamini</span>
                                <span className="text-[9px] text-blue-100 block leading-tight">Grade 10 • Westville High</span>
                            </div>
                        </div>
                        <div className="flex items-center gap-1.5 text-[10px] font-bold">
                            <span className="bg-amber-400 text-slate-950 px-1.5 py-0.5 rounded-full">🔥 5d</span>
                            <span className="bg-blue-900 text-blue-100 px-1.5 py-0.5 rounded-full border border-blue-400/40">⚡ 1.4k</span>
                        </div>
                    </div>

                    {/* Mobile 4-Stage Progression Stepper */}
                    <div className="px-2.5 py-1.5 bg-slate-100 border-b border-slate-200 flex items-center justify-between text-[10px] font-bold">
                        {[
                            { id: 'diag', label: '0. Diag' },
                            { id: 'scaff', label: '1. Scaff' },
                            { id: 'prac', label: '2. Prac' },
                            { id: 'exam', label: '3. Exam' },
                        ].map((stg, i) => {
                            const isCurrent = (simuStep === 0 && i === 1) || (simuStep === 1 && i === 2) || (simuStep === 2 && i === 2) || (simuStep === 3 && i === 3);
                            return (
                                <span
                                    key={stg.id}
                                    className={`px-1.5 py-0.5 rounded-md transition ${
                                        isCurrent ? 'bg-[#13519C] text-white shadow-xs font-bold' : 'text-slate-500'
                                    }`}
                                >
                                    {stg.label}
                                </span>
                            );
                        })}
                    </div>

                    {/* Mobile Problem Solving Surface */}
                    <div className="p-3 bg-slate-50 min-h-[300px] flex flex-col justify-between">
                        {simuStep === 0 && (
                            <div className="space-y-2">
                                <div className="bg-white p-2.5 rounded-xl border border-slate-200 shadow-xs space-y-2">
                                    <div className="flex items-center justify-between text-[10px] pb-1 border-b border-slate-100">
                                        <span className="font-bold text-emerald-800 uppercase">Cash Receipts Journal</span>
                                        <span className="font-bold text-amber-700 bg-amber-50 px-1.5 py-0.5 rounded border border-amber-200">6 Marks</span>
                                    </div>
                                    <p className="text-[11px] text-slate-700 font-medium">Cash sales R11,500 (incl. 15% VAT). Cost of sales R8,000.</p>

                                    {/* 2x2 Problem Solving Surface */}
                                    <div className="grid grid-cols-2 gap-1.5 text-[10px]">
                                        <div className="p-1.5 bg-emerald-50 rounded-lg border border-emerald-200">
                                            <span className="text-slate-500 block">Bank (Gross 115%)</span>
                                            <span className="font-mono font-bold text-emerald-900 text-xs">{accountingFilled.bank || '...'}</span>
                                        </div>
                                        <div className="p-1.5 bg-emerald-50 rounded-lg border border-emerald-200">
                                            <span className="text-slate-500 block">Sales (Excl 100%)</span>
                                            <span className="font-mono font-bold text-emerald-900 text-xs">{accountingFilled.sales || '...'}</span>
                                        </div>
                                        <div className="p-1.5 bg-emerald-50 rounded-lg border border-emerald-200">
                                            <span className="text-slate-500 block">Output VAT (15%)</span>
                                            <span className="font-mono font-bold text-emerald-900 text-xs">{accountingFilled.vat || '...'}</span>
                                        </div>
                                        <div className="p-1.5 bg-slate-50 rounded-lg border border-slate-200">
                                            <span className="text-slate-500 block">Cost of Sales</span>
                                            <span className="font-mono font-bold text-slate-800 text-xs">R 8 000</span>
                                        </div>
                                    </div>
                                </div>

                                {/* 3-Tier Hints Drawer */}
                                {showHints && (
                                    <div className="p-2 bg-amber-50 rounded-xl border border-amber-200 text-[10px] text-amber-900 space-y-1">
                                        <div className="flex items-center justify-between font-bold">
                                            <span>💡 Hint Tier {activeHintTier}</span>
                                            <div className="flex gap-1">
                                                {[1, 2, 3].map((t) => (
                                                    <span key={t} className={`px-1 rounded ${activeHintTier === t ? 'bg-[#13519C] text-white' : 'bg-white text-slate-600'}`}>T{t}</span>
                                                ))}
                                            </div>
                                        </div>
                                        <p className="text-[10px]">
                                            {activeHintTier === 1 && 'Look at Bank Gross and calculate 15/115.'}
                                            {activeHintTier === 2 && 'Gross = 115%, Sales = 100%, VAT = 15%.'}
                                            {activeHintTier === 3 && 'R11,500 × 15/115 = R1,500 VAT. Sales = R10,000.'}
                                        </p>
                                    </div>
                                )}

                                {accountingFilled.vat && (
                                    <div className="p-2 bg-emerald-50 border border-emerald-300 rounded-xl flex items-center justify-between text-[10px] text-emerald-900 font-bold shadow-xs">
                                        <span>✓ 6/6 Marks Credited</span>
                                        <span className="bg-emerald-600 text-white px-2 py-0.5 rounded-full text-[9px]">+35 XP</span>
                                    </div>
                                )}
                            </div>
                        )}

                        {simuStep === 1 && (
                            <div className="space-y-3 py-2 text-center">
                                <div className="flex justify-center">
                                    {renderMasteryDial(130, 8)}
                                </div>
                                <span className="text-[11px] font-bold text-slate-700 block" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    Formative Mastery: {formativeMastery}% • Exam Ready
                                </span>
                            </div>
                        )}

                        {simuStep === 2 && (
                            <div className="bg-white p-3 rounded-xl border border-slate-200 space-y-2 text-xs">
                                <span className="text-[10px] font-bold text-blue-800 uppercase block">Grade 10 Mathematics</span>
                                <p className="font-bold text-slate-900">Factorise: x² − 7x + 12</p>
                                <div className="p-2 bg-blue-50 border border-blue-300 rounded-lg font-mono font-bold text-blue-950 text-xs">
                                    {mathStepSubmitted ? '(x − 3)(x − 4) ✓' : 'Working...'}
                                </div>
                                {mathStepSubmitted && (
                                    <div className="p-1.5 bg-emerald-50 border border-emerald-300 rounded-lg flex items-center justify-between text-[10px] text-emerald-900 font-bold">
                                        <span>SymPy Confirmed</span>
                                        <span className="bg-emerald-600 text-white px-2 py-0.5 rounded-full text-[9px]">+35 XP</span>
                                    </div>
                                )}
                            </div>
                        )}

                        {simuStep === 3 && (
                            <div className="bg-white p-3 rounded-xl border border-slate-200 space-y-2 text-xs">
                                <div className="flex justify-between items-center text-[10px] font-bold text-rose-700">
                                    <span>EXAM MODE</span>
                                    <span>⏱️ {formatTimer(examTimer)}</span>
                                </div>
                                <p className="text-[11px] text-slate-800 font-semibold">R2,300 stock incl. 15% VAT. Output VAT?</p>
                                <div className="p-2 bg-blue-50 border border-blue-400 rounded-lg text-[10px] text-blue-900 font-bold">
                                    Option A: R300 (15/115 × R2,300) ✓
                                </div>
                                {examSubmitted && (
                                    <div className="p-2 bg-amber-50 border border-amber-300 rounded-lg text-[10px] text-amber-900 space-y-1">
                                        <span className="font-bold block">Autopsy Report: Score 84%</span>
                                        <span>Net vs. Gross VAT procedure verified.</span>
                                    </div>
                                )}
                            </div>
                        )}
                    </div>

                    {/* Pinned Bottom Horizontal Subject Carousel */}
                    <div className="border-t border-slate-200 bg-white/95 px-2 py-1.5 flex items-center gap-1.5 overflow-x-auto scrollbar-none rounded-b-2xl">
                        {SUBJECTS.map((sub) => {
                            const isSelected = selectedSubject.id === sub.id;
                            return (
                                <button
                                    key={sub.id}
                                    type="button"
                                    onClick={() => {
                                        setIsAutoPlaying(false);
                                        setSelectedSubject(sub);
                                    }}
                                    className={`flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-[10px] font-bold shrink-0 min-h-[44px] cursor-pointer ${
                                        isSelected
                                            ? 'bg-blue-50 text-[#13519C] border-2 border-blue-400 shadow-xs'
                                            : 'bg-slate-50 text-slate-600 border border-slate-200'
                                    }`}
                                >
                                    <span>{sub.name === 'Physical Sciences' ? 'Physics' : sub.name === 'Business Studies' ? 'Business' : sub.name}</span>
                                    <span className={`text-[9px] px-1 py-0.2 rounded-full ${isSelected ? 'bg-blue-600 text-white' : 'bg-slate-200 text-slate-700'}`}>
                                        {sub.mastery}%
                                    </span>
                                </button>
                            );
                        })}
                    </div>
                </div>
            </div>

            {/* ═══════════════════════════════════════════════════════════════ */}
            {/* 3. SIMULEARN INTERACTIVE STEP CONTROLS (User Journey Bar)      */}
            {/* ═══════════════════════════════════════════════════════════════ */}
            <div className="mt-3 px-4 py-2.5 bg-slate-100 border border-slate-200 rounded-xl flex flex-wrap items-center justify-between gap-2 text-xs">
                <div className="flex items-center gap-2">
                    <button
                        type="button"
                        onClick={() => setIsAutoPlaying(!isAutoPlaying)}
                        className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 text-xs font-bold transition shadow-xs cursor-pointer"
                    >
                        {isAutoPlaying ? <Pause className="w-3 h-3 text-amber-600" /> : <Play className="w-3 h-3 text-emerald-600" />}
                        <span>{isAutoPlaying ? 'Pause SimuLearn' : 'Auto Play'}</span>
                    </button>
                    <button
                        type="button"
                        onClick={() => handleStepJump(0)}
                        className="inline-flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-slate-600 hover:bg-slate-200 hover:text-slate-900 transition text-xs font-semibold cursor-pointer"
                    >
                        <RotateCcw className="w-3 h-3" />
                        <span>Restart</span>
                    </button>
                </div>

                {/* Step Journey Pills */}
                <div className="flex items-center gap-1.5 overflow-x-auto scrollbar-none py-0.5">
                    {[
                        { idx: 0, label: '1. In-Subject & 3-Tier Hints' },
                        { idx: 1, label: '2. Adaptive Progress Dial' },
                        { idx: 2, label: '3. Subject Switch' },
                        { idx: 3, label: '4. Timed Exam & Autopsy' },
                    ].map((s) => (
                        <button
                            key={s.idx}
                            type="button"
                            onClick={() => handleStepJump(s.idx)}
                            className={`px-2.5 py-1 rounded-full text-[11px] font-bold transition cursor-pointer shrink-0 ${
                                simuStep === s.idx
                                    ? 'bg-[#13519C] text-white shadow-xs'
                                    : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 hover:text-slate-900'
                            }`}
                        >
                            {s.label}
                        </button>
                    ))}
                </div>
            </div>

        </div>
    );
}
