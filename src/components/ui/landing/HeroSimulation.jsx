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
} from 'lucide-react';

// ═══════════════════════════════════════════════════════════════
// AUTHENTIC SUBJECT SHELF CONFIGURATION (Matches real app)
// ═══════════════════════════════════════════════════════════════
const SUBJECTS = [
    { id: 'accounting', name: 'Accounting', icon: BookOpen, grade: 'Grade 10', mastery: 84, color: 'text-emerald-700 bg-emerald-50 border-emerald-200' },
    { id: 'mathematics', name: 'Mathematics', icon: Calculator, grade: 'Grade 10', mastery: 82, color: 'text-blue-700 bg-blue-50 border-blue-200' },
    { id: 'physical_sciences', name: 'Physical Sciences', icon: FlaskConical, grade: 'Grade 10', mastery: 68, color: 'text-cyan-700 bg-cyan-50 border-cyan-200' },
    { id: 'business_studies', name: 'Business Studies', icon: Briefcase, grade: 'Grade 10', mastery: 75, color: 'text-purple-700 bg-purple-50 border-purple-200' },
    { id: 'ems', name: 'EMS', icon: Coins, grade: 'Grade 9', mastery: 80, color: 'text-amber-700 bg-amber-50 border-amber-200' },
];

export default function HeroSimulation({ isLightPalette = true }) {
    // ── SimuLearn Flow State ──
    // Step 0: In-Subject Practice with 3-Tier Pre-baked Hints
    // Step 1: Adaptive Progression & Circular Progress Dial update
    // Step 2: Subject Navigation (Switching from Accounting to Mathematics)
    // Step 3: Timed Exam Mode & Post-Exam Diagnostic Autopsy
    const [simuStep, setSimuStep] = useState(0);
    const [isAutoPlaying, setIsAutoPlaying] = useState(true);
    const [selectedSubject, setSelectedSubject] = useState(SUBJECTS[0]); // Accounting
    const [progressionMode, setProgressionMode] = useState('scaffold'); // 'scaffold' | 'practice' | 'assessment'

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

            // 1. Reveal hint after 2.5s
            timeoutId = setTimeout(() => {
                setShowHints(true);
                setActiveHintTier(1);

                // Tier 2 rule after another 2.5s
                setTimeout(() => {
                    setActiveHintTier(2);

                    // Tier 3 worked step after another 2.5s
                    setTimeout(() => {
                        setActiveHintTier(3);
                        // Populate correct answer
                        setAccountingFilled({ bank: '11 500', sales: '10 000', vat: '1 500' });

                        // Advance to Step 1 (Progress Dial) after 3s
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

            // Animate progress dial from 68% -> 84% (Exam Ready)
            let curr = 68;
            const interval = setInterval(() => {
                curr += 1;
                setFormativeMastery(curr);
                setEvaluativeScore(Math.min(curr + 4, 88));
                if (curr >= 84) {
                    clearInterval(interval);
                    // Move to Step 2 (Subject Switch) after 4s
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

            // Complete maths factorization step after 2.8s
            timeoutId = setTimeout(() => {
                setMathStepSubmitted(true);

                // Advance to Step 3 (Timed Exam Mode) after 3.5s
                setTimeout(() => {
                    setSimuStep(3);
                }, 3500);
            }, 2800);

        } else if (simuStep === 3) {
            // STEP 3: Timed Exam Mode & Post-Exam Autopsy
            setProgressionMode('assessment');
            setSelectedSubject(SUBJECTS[0]); // Accounting Exam
            setSelectedExamOption('A');

            // Submit exam after 3.5s to show Post-Exam Diagnostic Autopsy
            timeoutId = setTimeout(() => {
                setExamSubmitted(true);

                // Loop back to Step 0 after 9s of debrief viewing
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
    // CIRCULAR DUAL-RING MASTERY DIAL (Matches real MasteryDial)
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
            <div className="flex flex-col items-center justify-center p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
                <div className="relative" style={{ width: size, height: size }}>
                    <svg width={size} height={size} className="transform -rotate-90">
                        {/* Outer Track (Evaluative) */}
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
                        <span className="text-2xl font-bold text-slate-900 tracking-tight">
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
                }`}>
                    <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
                    <span>{isExamReady ? 'Exam Ready (Level 7)' : 'Proficient (Level 5)'}</span>
                </div>
            </div>
        );
    };

    return (
        <div className="relative w-full select-none" style={{ minHeight: '660px' }}>
            {/* The Actual Learner Workspace Window (Authentic Light Palette + Windows 11 Chrome) */}
            <div className="rounded-2xl bg-white border border-slate-300 shadow-xl overflow-hidden flex flex-col text-slate-800">
                
                {/* ── 0. WINDOWS 11 TITLE BAR (Strict Windows Controls: ─, □, ✕) ── */}
                <div className="px-3 sm:px-4 py-1.5 bg-slate-100 border-b border-slate-200 flex items-center justify-between gap-3 text-xs select-none">
                    {/* Left: App Icon & Title */}
                    <div className="flex items-center gap-2">
                        <div className="w-4 h-4 rounded bg-[#13519C] text-white flex items-center justify-center font-bold text-[9px]">
                            F
                        </div>
                        <span className="font-semibold text-slate-700 text-[11px] sm:text-xs tracking-tight">
                            Fundile — Learner Workspace (Grade 10 Accounting)
                        </span>
                        <div className="hidden md:flex items-center gap-1.5 px-2 py-0.5 rounded bg-white border border-slate-200 font-mono text-[10px] text-slate-500">
                            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                            <span>app.fundile.co.za/learner/workspace</span>
                        </div>
                    </div>

                    {/* Right: Windows 11 Window Controls */}
                    <div className="flex items-center -mr-2">
                        <button
                            type="button"
                            title="Minimize"
                            className="w-10 h-7 flex items-center justify-center hover:bg-slate-200 text-slate-600 transition"
                        >
                            <Minus className="w-3.5 h-3.5" />
                        </button>
                        <button
                            type="button"
                            title="Maximize"
                            className="w-10 h-7 flex items-center justify-center hover:bg-slate-200 text-slate-600 transition"
                        >
                            <Square className="w-3 h-3" />
                        </button>
                        <button
                            type="button"
                            title="Close"
                            className="w-10 h-7 flex items-center justify-center hover:bg-rose-500 hover:text-white text-slate-600 transition"
                        >
                            <X className="w-3.5 h-3.5" />
                        </button>
                    </div>
                </div>

                {/* ── 1. REAL TOP APP HEADER (Fundile Brand, Learner Profile, Streak & XP) ── */}
                <div className="px-4 py-2 bg-[#13519C] text-white flex items-center justify-between gap-3 text-xs">
                    {/* Left: Brand & Route */}
                    <div className="flex items-center gap-2.5">
                        <span className="font-bold text-sm tracking-tight text-white">FUNDILE</span>
                        <span className="hidden sm:inline text-blue-200 text-xs font-medium">| Term 1 Learner Engine</span>
                    </div>

                    {/* Center: Learner Profile & Grade */}
                    <div className="flex items-center gap-2">
                        <div className="w-6 h-6 rounded-full bg-white text-[#13519C] flex items-center justify-center font-bold text-[11px] shadow-xs">
                            N
                        </div>
                        <div className="text-left">
                            <span className="font-bold text-white block text-[11px] leading-tight">Nqobile Dlamini</span>
                            <span className="text-[10px] text-blue-100 block leading-tight">Grade 10 • CAPS</span>
                        </div>
                    </div>

                    {/* Right: Gamified Streak & XP */}
                    <div className="flex items-center gap-2">
                        <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-amber-500/20 border border-amber-300/40 text-amber-200 text-[11px] font-bold">
                            <Flame className="w-3.5 h-3.5 text-[#FF9100] fill-[#FF9100]" />
                            <span>5 Days</span>
                        </div>
                        <div className="hidden sm:flex items-center gap-1 px-2.5 py-1 rounded-full bg-blue-800/80 border border-blue-400/40 text-blue-100 text-[11px] font-bold">
                            <Zap className="w-3.5 h-3.5 text-blue-300" />
                            <span>1,420 XP</span>
                        </div>
                    </div>
                </div>

                {/* ── 2. REAL SUBJECT SHELF (Live Navigation Across Subjects) ── */}
                <div className="w-full bg-white border-b border-slate-200 px-3 sm:px-4 py-2 overflow-x-auto scrollbar-none flex items-center gap-2">
                    <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 pr-2 border-r border-slate-200 shrink-0">
                        Subjects
                    </span>
                    <div className="flex items-center gap-2 shrink-0">
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
                                    className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold transition-all duration-200 shrink-0 cursor-pointer ${
                                        isSelected
                                            ? 'bg-[#13519C] text-white shadow-xs scale-[1.02]'
                                            : 'bg-slate-50 hover:bg-slate-100 text-slate-700 border border-slate-200'
                                    }`}
                                >
                                    <Icon className="w-3.5 h-3.5 shrink-0" />
                                    <span>{sub.name}</span>
                                    <span className={`text-[10px] px-1.5 py-0.5 rounded font-bold ${
                                        isSelected ? 'bg-blue-800 text-white' : 'bg-slate-200 text-slate-700'
                                    }`}>
                                        {sub.mastery}%
                                    </span>
                                </button>
                            );
                        })}
                    </div>
                </div>

                {/* ── 3. ADAPTIVE PROGRESSION MODE RIBBON ── */}
                <div className="px-4 py-2 bg-slate-50 border-b border-slate-200 flex flex-wrap items-center justify-between gap-3 text-xs">
                    {/* Progression Stage Badges */}
                    <div className="flex items-center gap-1.5">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 mr-1 hidden sm:inline">
                            Progression:
                        </span>
                        <div className="flex items-center gap-1 p-0.5 bg-white rounded-lg border border-slate-200 text-[11px] font-bold shadow-xs">
                            <span className={`px-2.5 py-1 rounded-md transition ${
                                progressionMode === 'scaffold'
                                    ? 'bg-[#13519C] text-white shadow-xs'
                                    : 'text-slate-600'
                            }`}>
                                1. Scaffold
                            </span>
                            <span className={`px-2.5 py-1 rounded-md transition ${
                                progressionMode === 'practice'
                                    ? 'bg-[#13519C] text-white shadow-xs'
                                    : 'text-slate-600'
                            }`}>
                                2. Practice
                            </span>
                            <span className={`px-2.5 py-1 rounded-md transition ${
                                progressionMode === 'assessment'
                                    ? 'bg-rose-600 text-white shadow-xs animate-pulse'
                                    : 'text-slate-600'
                            }`}>
                                3. Exam Mode
                            </span>
                        </div>
                    </div>

                    {/* Mode Guidance or Exam Timer */}
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
                            >
                                <Lightbulb className="w-3.5 h-3.5 text-amber-600" />
                                <span>{showHints ? 'Hide 3-Tier Hints' : '💡 View 3-Tier Hints (Zero-LLM)'}</span>
                            </button>
                        </div>
                    )}
                </div>

                {/* ── 4. 3-TIER PRE-BAKED HINTS DRAWER (Scaffold Mode) ── */}
                {showHints && progressionMode !== 'assessment' && (
                    <div className="px-4 py-3 bg-amber-50/80 border-b border-amber-200 space-y-2 text-xs">
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-2">
                                <span className="text-[10px] font-bold uppercase tracking-wider text-amber-900 bg-amber-200/60 border border-amber-300 px-2 py-0.5 rounded">
                                    DETERMINISTIC 3-TIER HINT ENGINE
                                </span>
                                <span className="text-amber-800 text-[11px] hidden sm:inline">
                                    Pre-calculated ahead of time with zero token cost
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

                {/* ── 5. MAIN WORKSPACE CONTENT BODY (Native Modality per Subject & State) ── */}
                <div className="p-4 sm:p-6 flex-1 bg-slate-50 flex flex-col justify-center">

                    {/* ── SCENARIO A: ACCOUNTING SCAFFOLD (2D Ledger Table) ── */}
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
                                    <h4 className="text-sm sm:text-base font-bold text-slate-900 mt-1">
                                        Record Cash Sales of Merchandise: R11,500 (inclusive of 15% VAT)
                                    </h4>
                                </div>
                                <div className="text-right">
                                    <span className="text-[11px] text-slate-500 block">Total Marks:</span>
                                    <span className="text-sm font-bold text-amber-600">6 Marks</span>
                                </div>
                            </div>

                            {/* 2D Accounting Table */}
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
                                <div className="p-3 bg-emerald-50 border border-emerald-300 rounded-xl flex items-center justify-between text-xs text-emerald-900 shadow-xs animate-in fade-in">
                                    <div className="flex items-center gap-2">
                                        <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                                        <span>6 / 6 Marks Awarded • Schema Verified: Net VAT extracted accurately (15/115)</span>
                                    </div>
                                    <span className="font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded">+35 XP</span>
                                </div>
                            )}
                        </div>
                    )}

                    {/* ── SCENARIO B: ADAPTIVE MASTERY DIAL & PROGRESSION GATES ── */}
                    {simuStep === 1 && (
                        <div className="grid md:grid-cols-12 gap-6 items-center">
                            {/* Left: Real Circular Dual-Ring Progress Dial */}
                            <div className="md:col-span-5 flex flex-col items-center">
                                {renderMasteryDial(160, 10)}
                                <span className="text-[11px] text-slate-500 mt-2 text-center">
                                    Inner: BKT Formative Mastery ({formativeMastery}%) • Outer: Evaluative Score ({evaluativeScore}%)
                                </span>
                            </div>

                            {/* Right: Progression Milestones Unlocked */}
                            <div className="md:col-span-7 space-y-3">
                                <div>
                                    <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-bold">
                                        <Award className="w-3.5 h-3.5 text-emerald-600" />
                                        <span>Adaptive Gate Unlocked</span>
                                    </div>
                                    <h4 className="text-base sm:text-lg font-bold text-slate-900 mt-1">
                                        Mastery Threshold Exceeded: 84% BKT Index
                                    </h4>
                                    <p className="text-xs text-slate-600 mt-0.5">
                                        Because Nqobile scored &gt;80% in autonomous problem solving, the system unlocks official Examination conditions.
                                    </p>
                                </div>

                                {/* Step Breakdown */}
                                <div className="space-y-2">
                                    <div className="p-2.5 rounded-xl bg-white border border-emerald-200 flex items-center justify-between text-xs shadow-xs">
                                        <div className="flex items-center gap-2">
                                            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                                            <span className="font-bold text-slate-800">1. Scaffold Mode (Guided 3-Tier Hints)</span>
                                        </div>
                                        <span className="text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded">100% Passed</span>
                                    </div>
                                    <div className="p-2.5 rounded-xl bg-white border border-emerald-200 flex items-center justify-between text-xs shadow-xs">
                                        <div className="flex items-center gap-2">
                                            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                                            <span className="font-bold text-slate-800">2. Practice Mode (Mastery Verification)</span>
                                        </div>
                                        <span className="text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded">100% Passed</span>
                                    </div>
                                    <div className="p-2.5 rounded-xl bg-indigo-50 border border-indigo-200 flex items-center justify-between text-xs text-indigo-900 shadow-xs">
                                        <div className="flex items-center gap-2">
                                            <Sparkles className="w-4 h-4 text-amber-500" />
                                            <span className="font-bold">3. Official Timed Assessment Mode</span>
                                        </div>
                                        <span className="bg-[#13519C] text-white px-2 py-0.5 rounded font-bold text-[10px]">
                                            UNLOCKED NOW
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* ── SCENARIO C: SUBJECT SWITCH TO MATHEMATICS (KaTeX & Stepwise Derivations) ── */}
                    {simuStep === 2 && selectedSubject.id === 'mathematics' && (
                        <div className="space-y-4">
                            <div className="flex items-center justify-between border-b border-slate-200 pb-3">
                                <div>
                                    <div className="flex items-center gap-2">
                                        <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-50 text-blue-800 border border-blue-200">
                                            Term 1 • Algebraic Expressions &amp; Trinomials
                                        </span>
                                        <span className="text-xs text-slate-500">Stepwise KaTeX Symbolic Derivation</span>
                                    </div>
                                    <h4 className="text-sm sm:text-base font-bold text-slate-900 mt-1">
                                        Factorise the Quadratic Trinomial: x² − 7x + 12
                                    </h4>
                                </div>
                                <div className="text-right">
                                    <span className="text-[11px] text-slate-500 block">Marks:</span>
                                    <span className="text-sm font-bold text-blue-700">3 Marks</span>
                                </div>
                            </div>

                            {/* Working Pad */}
                            <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-xs space-y-3 font-mono text-xs">
                                <div className="flex items-center justify-between text-slate-500 text-[11px] border-b border-slate-100 pb-2">
                                    <span>SymPy Procedure Tracker:</span>
                                    <span className="font-sans font-semibold">Target Format: (x + a)(x + b)</span>
                                </div>

                                <div className="space-y-2">
                                    <div className="flex items-center gap-2">
                                        <span className="w-20 text-slate-500 text-[10px]">Factor Pairs:</span>
                                        <span className="text-slate-700 bg-slate-100 px-2 py-1 rounded border border-slate-200">
                                            Product = +12, Sum = −7 → Pair: (−3) and (−4)
                                        </span>
                                    </div>
                                    <div className="flex items-center gap-2">
                                        <span className="w-20 text-slate-500 text-[10px]">Solution:</span>
                                        <div className="flex items-center gap-1.5 text-slate-900 font-bold text-sm bg-slate-50 px-3 py-1.5 rounded-lg border border-slate-300">
                                            <span>(x − 3)(x − 4)</span>
                                            {mathStepSubmitted && (
                                                <CheckCircle2 className="w-4 h-4 text-emerald-600 ml-2" />
                                            )}
                                        </div>
                                    </div>
                                </div>
                            </div>

                            {mathStepSubmitted && (
                                <div className="p-3 bg-blue-50 border border-blue-200 rounded-xl flex items-center justify-between text-xs text-blue-900 shadow-xs animate-in fade-in">
                                    <div className="flex items-center gap-2">
                                        <CheckCircle2 className="w-4 h-4 text-blue-600" />
                                        <span>Symbolic Equivalence Confirmed • Method Marks: 3/3 awarded</span>
                                    </div>
                                    <span className="font-bold text-blue-700 bg-blue-100 px-2 py-0.5 rounded">+40 XP</span>
                                </div>
                            )}
                        </div>
                    )}

                    {/* ── SCENARIO D: TIMED EXAM MODE & POST-EXAM DIAGNOSTIC AUTOPSY ── */}
                    {simuStep === 3 && (
                        <div className="space-y-4">
                            {!examSubmitted ? (
                                <div className="space-y-3">
                                    <div className="flex items-center justify-between border-b border-slate-200 pb-3">
                                        <div>
                                            <div className="flex items-center gap-2">
                                                <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-rose-50 text-rose-800 border border-rose-200">
                                                    Grade 10 CAPS March Examination • Timed Conditions
                                                </span>
                                                <span className="text-xs text-slate-500">Strict Exam Invariants Active</span>
                                            </div>
                                            <h4 className="text-sm sm:text-base font-bold text-slate-900 mt-1">
                                                Question 2.1: VAT Extraction on Receipt of R2,300 (Inclusive)
                                            </h4>
                                        </div>
                                        <div className="text-right">
                                            <span className="text-xs font-bold font-mono text-rose-700 bg-rose-50 border border-rose-200 px-2.5 py-1 rounded">
                                                ⏱️ {formatTimer(examTimer)}
                                            </span>
                                        </div>
                                    </div>

                                    {/* MCQ Options in Exam */}
                                    <div className="space-y-2 text-xs">
                                        <div className={`p-3 rounded-xl border flex items-center justify-between transition ${
                                            selectedExamOption === 'A'
                                                ? 'bg-blue-50 border-[#13519C] text-[#13519C] font-semibold shadow-xs'
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
                                /* POST-EXAM DIAGNOSTIC AUTOPSY (What the student actually gets after an exam) */
                                <div className="p-4 sm:p-5 bg-amber-50/60 border border-amber-300 rounded-2xl space-y-3 text-xs shadow-xs animate-in zoom-in-95">
                                    <div className="flex items-center justify-between border-b border-amber-200 pb-2.5">
                                        <div className="flex items-center gap-2">
                                            <AlertTriangle className="w-4 h-4 text-amber-600" />
                                            <span className="font-bold text-sm text-slate-900">Post-Exam Diagnostic Autopsy</span>
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

                {/* ── 6. SIMULEARN INTERACTIVE STEP CONTROLS (Pure user journey navigation) ── */}
                <div className="px-4 py-2.5 bg-slate-100 border-t border-slate-200 flex flex-wrap items-center justify-between gap-2 text-xs">
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
        </div>
    );
}
