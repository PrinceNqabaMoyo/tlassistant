import React, { useState, useEffect } from 'react';
import {
    MessageCircle,
    Zap,
    ShieldCheck,
    Award,
    CheckCircle2,
    Sparkles,
    Smartphone,
    ArrowRight,
    TrendingUp,
    Info,
    ExternalLink,
    ArrowLeft,
    FileText,
    Download,
    Printer,
    X,
    Eye,
    Check,
    AlertTriangle,
    RotateCcw,
    ChevronRight,
} from 'lucide-react';

const ParentSimulation = ({ isLightPalette = true, onGetStarted, onSelectPerspective }) => {
    const [activeTab, setActiveTab] = useState('whatsapp'); // 'whatsapp' | 'data' | 'readiness'
    const [selectedLearner, setSelectedLearner] = useState('nqobile'); // 'nqobile' | 'sipho'
    const [showPdfModal, setShowPdfModal] = useState(false);

    // ── SimuLearn State: 0 = Notification, 1 = Open Message, 2 = Open PDF Report ──
    const [simuStage, setSimuStage] = useState(0);
    const [isAutoPlaying, setIsAutoPlaying] = useState(true);

    useEffect(() => {
        if (!isAutoPlaying || activeTab !== 'whatsapp') return;

        let timer;
        if (simuStage === 0) {
            timer = setTimeout(() => setSimuStage(1), 2800);
        } else if (simuStage === 1) {
            timer = setTimeout(() => setSimuStage(2), 3400);
        } else if (simuStage === 2) {
            timer = setTimeout(() => setSimuStage(0), 8500);
        }
        return () => clearTimeout(timer);
    }, [simuStage, isAutoPlaying, activeTab]);

    const learners = {
        nqobile: {
            name: 'Nqobile Moyo',
            grade: 'Grade 10',
            subjects: 'Accounting & Mathematics',
            dataUsed: '1.6 MB',
            videoDataEquivalent: '450 MB',
            costSaved: 'R95',
            mastery: 84,
            level: 'Level 7 (Outstanding)',
            pdfFilename: 'Fundile_Diagnostic_Report_Nqobile_Gr10.pdf',
            fileSize: '142 KB',
            gapTopic: 'Accounting: Value Added Tax (VAT) Calculation',
            misconception: 'Confusing 15% exclusive with 115% inclusive formula',
            flawedProcedure: 'Multiplied gross inclusive Bank receipt (R2,300) by 15/100 instead of 15/115',
            cohortFlawStat: '18 of 28 learners in cohort followed this exact flawed procedure',
            methodMarksAwarded: '2 of 4 Method Marks credited for identifying Bank debit (consequential accuracy)',
            fixedStatus: 'Resolved in 5-min targeted prerequisite drill',
            prompt: 'Ask Nqobile how she determines whether to multiply by 15/115 or 15/100 when VAT is inclusive.',
            subjectScores: [
                { subject: 'Accounting', score: 84, level: 'Level 7', rating: 'Outstanding' },
                { subject: 'Mathematics', score: 78, level: 'Level 6', rating: 'Meritorious' },
                { subject: 'Physical Sciences', score: 65, level: 'Level 5', rating: 'Substantial' },
                { subject: 'Life Sciences', score: 72, level: 'Level 6', rating: 'Meritorious' },
            ]
        },
        sipho: {
            name: 'Sipho Zulu',
            grade: 'Grade 11',
            subjects: 'Physical Sciences & Maths',
            dataUsed: '1.9 MB',
            videoDataEquivalent: '520 MB',
            costSaved: 'R110',
            mastery: 88,
            level: 'Level 7 (Outstanding)',
            pdfFilename: 'Fundile_Diagnostic_Report_Sipho_Gr11.pdf',
            fileSize: '158 KB',
            gapTopic: 'Physics: Newtonian Vectors & Inclined Planes',
            misconception: 'Resolving perpendicular gravity components with inverted trig ratio',
            flawedProcedure: 'Used sin(θ) instead of cos(θ) for normal force parallel component calculation',
            cohortFlawStat: '14 of 28 learners in cohort made this identical trigonometry inversion',
            methodMarksAwarded: '3 of 5 Method Marks credited for free-body diagram vector labels',
            fixedStatus: 'Resolved in 6-min step-by-step vector resolution review',
            prompt: 'Ask Sipho how to determine whether adjacent or opposite side represents the parallel force component.',
            subjectScores: [
                { subject: 'Physical Sciences', score: 88, level: 'Level 7', rating: 'Outstanding' },
                { subject: 'Mathematics', score: 82, level: 'Level 7', rating: 'Outstanding' },
                { subject: 'Life Sciences', score: 76, level: 'Level 6', rating: 'Meritorious' },
                { subject: 'English FAL', score: 74, level: 'Level 6', rating: 'Meritorious' },
            ]
        },
    };

    const current = learners[selectedLearner];

    return (
        <div className="w-full relative">
            {/* ── A4 DIAGNOSTIC REPORT MODAL (Simulates opening the PDF document) ── */}
            {showPdfModal && (
                <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80 backdrop-blur-sm animate-fadeIn">
                    <div className="relative w-full max-w-2xl bg-white rounded-2xl shadow-2xl border border-slate-200 overflow-hidden flex flex-col max-h-[90vh]">
                        {/* Modal Header */}
                        <div className="bg-[#13519C] text-white px-5 py-3.5 flex items-center justify-between">
                            <div className="flex items-center gap-2.5">
                                <div className="p-1.5 rounded-lg bg-white/10">
                                    <FileText className="h-5 w-5 text-[#FFD166]" />
                                </div>
                                <div>
                                    <h4 className="font-bold text-sm sm:text-base leading-tight">
                                        {current.pdfFilename}
                                    </h4>
                                    <span className="text-[11px] text-blue-100">
                                        Authentic South African CAPS Diagnostic Report • {current.fileSize}
                                    </span>
                                </div>
                            </div>
                            <button
                                type="button"
                                onClick={() => setShowPdfModal(false)}
                                className="p-1.5 rounded-lg hover:bg-white/20 text-white/80 hover:text-white transition cursor-pointer"
                                title="Close"
                            >
                                <X className="h-5 w-5" />
                            </button>
                        </div>

                        {/* Modal Body (A4 Paper Surface) */}
                        <div className="p-5 sm:p-6 overflow-y-auto space-y-5 text-left text-slate-900 bg-slate-50/50">
                            {/* Document Letterhead */}
                            <div className="border-b-2 border-slate-900 pb-3 flex justify-between items-end">
                                <div>
                                    <span className="text-xl font-black tracking-tight text-[#13519C] block">FUNDILE</span>
                                    <span className="text-[10px] text-slate-500 font-semibold uppercase tracking-wider">
                                        Cognitive Diagnostic Engine • Official Parent Report
                                    </span>
                                </div>
                                <div className="text-right text-xs">
                                    <span className="font-bold text-slate-800 block">{current.name}</span>
                                    <span className="text-slate-500">{current.grade} • Term 1/2 Benchmark</span>
                                </div>
                            </div>

                            {/* Summary KPI Badges */}
                            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-center">
                                <div className="bg-white p-3 rounded-xl border border-slate-200 shadow-xs">
                                    <span className="text-[10px] text-slate-500 font-bold uppercase block">Overall Mastery</span>
                                    <span className="text-xl font-bold text-[#13519C]">{current.mastery}%</span>
                                </div>
                                <div className="bg-white p-3 rounded-xl border border-slate-200 shadow-xs">
                                    <span className="text-[10px] text-slate-500 font-bold uppercase block">CAPS Standing</span>
                                    <span className="text-xs font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded inline-block mt-1">
                                        {current.level}
                                    </span>
                                </div>
                                <div className="bg-white p-3 rounded-xl border border-slate-200 shadow-xs">
                                    <span className="text-[10px] text-slate-500 font-bold uppercase block">Mobile Data Used</span>
                                    <span className="text-xl font-bold text-emerald-600">{current.dataUsed}</span>
                                </div>
                                <div className="bg-white p-3 rounded-xl border border-slate-200 shadow-xs">
                                    <span className="text-[10px] text-slate-500 font-bold uppercase block">Data Saved</span>
                                    <span className="text-xs font-bold text-slate-700 block mt-1">{current.videoDataEquivalent} ({current.costSaved})</span>
                                </div>
                            </div>

                            {/* DEEP COGNITIVE PROCEDURE AUTOPSY (Requested in User Request 4) */}
                            <div className="bg-amber-50/90 border border-amber-300/80 rounded-xl p-4 space-y-2.5">
                                <div className="flex items-center gap-2">
                                    <AlertTriangle className="h-4 w-4 text-amber-700 shrink-0" />
                                    <span className="text-xs font-bold uppercase tracking-wider text-amber-900">
                                        Procedural Performance Breakdown &amp; Flaw Analysis
                                    </span>
                                </div>
                                <div>
                                    <p className="text-xs font-bold text-slate-900">{current.gapTopic}</p>
                                    <p className="text-xs text-amber-950 mt-0.5">
                                        <strong>Identified Flaw:</strong> {current.flawedProcedure}
                                    </p>
                                </div>
                                <div className="grid sm:grid-cols-2 gap-2 text-[11px] pt-1 border-t border-amber-200/80">
                                    <div>
                                        <span className="font-bold text-slate-700">Cohort Benchmark:</span>
                                        <p className="text-slate-600">{current.cohortFlawStat}</p>
                                    </div>
                                    <div>
                                        <span className="font-bold text-slate-700">Consequential Marking:</span>
                                        <p className="text-slate-600">{current.methodMarksAwarded}</p>
                                    </div>
                                </div>
                                <div className="bg-white/90 p-2.5 rounded-lg border border-amber-200/70 text-xs">
                                    <span className="font-bold text-emerald-800 block text-[11px]">✓ Targeted Remedial Action Plan:</span>
                                    <p className="text-slate-700 text-[11px] mt-0.5">{current.fixedStatus}</p>
                                </div>
                                <div className="bg-amber-100/70 p-2.5 rounded-lg text-xs">
                                    <span className="font-bold text-slate-800 block text-[11px]">💬 Recommended Dinner Conversation Starter:</span>
                                    <p className="text-slate-700 italic text-[11px] mt-0.5">"{current.prompt}"</p>
                                </div>
                            </div>

                            {/* Subject-by-Subject CAPS Breakdown */}
                            <div className="bg-white border border-slate-200 rounded-xl p-3.5 space-y-2">
                                <span className="text-xs font-bold text-slate-800 uppercase tracking-wider block">
                                    Curriculum Subject Breakdown
                                </span>
                                <div className="space-y-1.5">
                                    {current.subjectScores.map((s) => (
                                        <div key={s.subject} className="flex items-center justify-between text-xs py-1 border-b border-slate-100 last:border-0">
                                            <span className="font-medium text-slate-800">{s.subject}</span>
                                            <div className="flex items-center gap-2">
                                                <span className="font-mono font-bold text-[#13519C]">{s.score}%</span>
                                                <span className="text-[10px] px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 font-semibold">
                                                    {s.level} ({s.rating})
                                                </span>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>

                            {/* Verification & POPIA Notice */}
                            <div className="text-[10px] text-slate-500 border-t border-slate-200 pt-2 flex flex-col sm:flex-row justify-between items-center gap-2">
                                <span>100% POPIA Section 35 Minor Privacy Compliant</span>
                                <span>Verified NSC/CAPS Syllabus Alignment</span>
                            </div>
                        </div>

                        {/* Modal Footer */}
                        <div className="bg-slate-100 px-5 py-3 border-t border-slate-200 flex justify-end gap-2">
                            <button
                                type="button"
                                onClick={() => setShowPdfModal(false)}
                                className="px-4 py-2 rounded-xl text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer"
                            >
                                Close
                            </button>
                            <button
                                type="button"
                                onClick={() => {
                                    alert(`Simulated PDF Download: ${current.pdfFilename} (142 KB). In production, this streams the ReportLab vector A4 PDF.`);
                                }}
                                className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-semibold bg-[#13519C] text-white hover:bg-[#0f3e77] transition shadow-xs cursor-pointer"
                            >
                                <Download className="h-3.5 w-3.5" />
                                <span>Download PDF</span>
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* Header & Subtitle */}
            <div className="text-center max-w-3xl mx-auto mb-8">
                <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-bold bg-amber-500/10 border border-amber-500/25 text-amber-600 mb-3">
                    <span>👨‍👩‍👧</span>
                    <span>Interactive Parent Portal Preview</span>
                </div>
                <h3
                    className="text-2xl sm:text-3xl lg:text-4xl font-bold tracking-tight text-slate-900"
                    style={{ fontFamily: 'Afacad, sans-serif' }}
                >
                    Real-time oversight without nagging or costly tutor bills
                </h3>
                <p className="mt-2 text-sm sm:text-base text-slate-600">
                    See exactly how Fundile keeps parents informed with weekly official PDF diagnostic reports delivered via WhatsApp, 98% mobile data savings, and verified curriculum mastery.
                </p>
            </div>

            {/* Interactive Mode Selector Tabs */}
            <div className="flex flex-wrap items-center justify-center gap-2 mb-6">
                {[
                    { id: 'whatsapp', label: '1. WhatsApp Weekly PDF Report', icon: MessageCircle, badge: 'Official A4 Report' },
                    { id: 'data', label: '2. 98% Mobile Data Savings', icon: Zap, badge: '1.6MB vs 450MB' },
                    { id: 'readiness', label: '3. CAPS Exam Readiness', icon: Award, badge: 'Verified Mastery' },
                ].map((tab) => {
                    const Icon = tab.icon;
                    const isActive = activeTab === tab.id;
                    return (
                        <button
                            key={tab.id}
                            type="button"
                            onClick={() => setActiveTab(tab.id)}
                            className={`inline-flex items-center gap-2 px-4 py-2 rounded-full text-xs sm:text-sm font-bold transition-all duration-200 cursor-pointer ${
                                isActive
                                    ? 'bg-[#13519C] text-white shadow-md shadow-blue-900/20 scale-[1.02]'
                                    : 'bg-white text-slate-700 border border-slate-200 hover:bg-slate-50'
                            }`}
                        >
                            <Icon className="h-4 w-4 shrink-0" />
                            <span>{tab.label}</span>
                            <span
                                className={`text-[10px] px-2 py-0.5 rounded-full ${
                                    isActive ? 'bg-white/20 text-white' : 'bg-slate-100 text-slate-600'
                                }`}
                            >
                                {tab.badge}
                            </span>
                        </button>
                    );
                })}
            </div>

            {/* Main Interactive Stage */}
            <div className="bg-white border border-slate-200 rounded-[28px] p-4 sm:p-8 shadow-sm">
                
                {/* ── TAB 1: WHATSAPP PDF ATTACHMENT REPORT PREVIEW (Requests 3 & 4) ── */}
                {activeTab === 'whatsapp' && (
                    <div className="grid lg:grid-cols-12 gap-8 items-center">
                        {/* Left Info & Learner Switcher */}
                        <div className="lg:col-span-5 space-y-5 text-left">
                            <div className="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-emerald-600">
                                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                                Automated Sunday Morning PDF Delivery
                            </div>
                            <h4 className="text-xl sm:text-2xl font-bold text-slate-900 leading-snug">
                                Know where your child stands with an official PDF report
                            </h4>
                            <p className="text-sm text-slate-600 leading-relaxed">
                                No complex dashboards to navigate. Every Sunday, Fundile delivers an official A4 Diagnostic PDF progress report to your phone. It pinpoints the exact procedure errors your child made and arms you with conversation starters for dinner.
                            </p>

                            {/* Learner Switcher Pills */}
                            <div className="p-3 bg-slate-50 rounded-2xl border border-slate-200/80">
                                <span className="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-2">
                                    Simulate Learner Profile:
                                </span>
                                <div className="flex gap-2">
                                    <button
                                        type="button"
                                        onClick={() => setSelectedLearner('nqobile')}
                                        className={`flex-1 py-1.5 px-3 rounded-xl text-xs font-bold transition ${
                                            selectedLearner === 'nqobile'
                                                ? 'bg-[#13519C] text-white shadow-sm'
                                                : 'bg-white text-slate-700 border border-slate-200 hover:bg-slate-100'
                                        }`}
                                    >
                                        Nqobile (Gr 10)
                                    </button>
                                    <button
                                        type="button"
                                        onClick={() => setSelectedLearner('sipho')}
                                        className={`flex-1 py-1.5 px-3 rounded-xl text-xs font-bold transition ${
                                            selectedLearner === 'sipho'
                                                ? 'bg-[#13519C] text-white shadow-sm'
                                                : 'bg-white text-slate-700 border border-slate-200 hover:bg-slate-100'
                                        }`}
                                    >
                                        Sipho (Gr 11)
                                    </button>
                                </div>
                            </div>

                            <div className="space-y-2 text-xs text-slate-600">
                                <div className="flex items-center gap-2">
                                    <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
                                    <span>Official A4 PDF progress report attached directly in WhatsApp</span>
                                </div>
                                <div className="flex items-center gap-2">
                                    <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
                                    <span>Cognitive procedure error taxonomy &amp; remedial action included</span>
                                </div>
                                <div className="flex items-center gap-2">
                                    <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
                                    <span>100% POPIA child privacy compliant — zero commercial ads</span>
                                </div>
                            </div>
                        </div>

                        {/* Right: SimuLearn Smartphone Experience (Notification → Message → PDF Report) */}
                        <div className="lg:col-span-7 flex flex-col items-center">
                            
                            {/* SimuLearn Step Navigation Pills */}
                            <div className="w-full max-w-sm flex items-center justify-between gap-1 mb-3 text-xs">
                                <div className="flex items-center gap-1">
                                    <button
                                        type="button"
                                        onClick={() => setIsAutoPlaying(!isAutoPlaying)}
                                        className="px-2 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold transition cursor-pointer text-[10px]"
                                    >
                                        {isAutoPlaying ? 'Pause' : 'Play'}
                                    </button>
                                    <button
                                        type="button"
                                        onClick={() => {
                                            setSimuStage(0);
                                            setIsAutoPlaying(true);
                                        }}
                                        className="p-1 rounded-lg text-slate-400 hover:text-slate-700 transition cursor-pointer"
                                        title="Replay from start"
                                    >
                                        <RotateCcw className="w-3.5 h-3.5" />
                                    </button>
                                </div>

                                <div className="flex items-center gap-1">
                                    {[
                                        { s: 0, label: '1. Push Alert' },
                                        { s: 1, label: '2. WhatsApp' },
                                        { s: 2, label: '3. PDF Report' },
                                    ].map((step) => (
                                        <button
                                            key={step.s}
                                            type="button"
                                            onClick={() => {
                                                setIsAutoPlaying(false);
                                                setSimuStage(step.s);
                                            }}
                                            className={`px-2 py-0.5 rounded-full text-[10px] font-bold transition cursor-pointer ${
                                                simuStage === step.s
                                                    ? 'bg-[#13519C] text-white shadow-xs'
                                                    : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                                            }`}
                                        >
                                            {step.label}
                                        </button>
                                    ))}
                                </div>
                            </div>

                            {/* The Realistic Smartphone Frame */}
                            <div className="w-full max-w-sm rounded-[36px] border-[6px] border-slate-900 bg-slate-950 shadow-2xl overflow-hidden text-slate-900 relative aspect-[9/17] max-h-[580px] flex flex-col">
                                
                                {/* Phone Status Bar & Notch */}
                                <div className="bg-black text-white px-5 pt-2 pb-1.5 flex items-center justify-between text-[11px] font-semibold shrink-0 z-30">
                                    <span>08:30</span>
                                    <div className="w-16 h-4 rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center">
                                        <div className="w-2.5 h-2.5 rounded-full bg-slate-950" />
                                    </div>
                                    <div className="flex items-center gap-1 text-[10px]">
                                        <span>5G</span>
                                        <span>100%</span>
                                    </div>
                                </div>

                                {/* ── STAGE 0: LOCK SCREEN & INCOMING WHATSAPP NOTIFICATION ── */}
                                {simuStage === 0 && (
                                    <div 
                                        onClick={() => {
                                            setIsAutoPlaying(false);
                                            setSimuStage(1);
                                        }}
                                        className="relative flex-1 bg-gradient-to-b from-slate-800 via-indigo-950 to-slate-900 text-white p-4 flex flex-col justify-between cursor-pointer"
                                    >
                                        {/* Lock screen clock */}
                                        <div className="text-center pt-8 space-y-1">
                                            <span className="text-5xl font-bold tracking-tight block" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                                08:30
                                            </span>
                                            <span className="text-xs text-slate-300 font-medium block">
                                                Sunday, 23 March
                                            </span>
                                        </div>

                                        {/* Dropdown WhatsApp Notification Banner */}
                                        <div className="w-full bg-white/95 backdrop-blur-md rounded-2xl p-3 shadow-2xl border border-white/20 text-slate-900 animate-in slide-in-from-top-6 duration-500 space-y-1.5 relative group">
                                            <div className="flex items-center justify-between">
                                                <div className="flex items-center gap-1.5">
                                                    <div className="w-4 h-4 rounded-full bg-emerald-500 flex items-center justify-center text-white text-[9px] font-bold">
                                                        W
                                                    </div>
                                                    <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500">
                                                        WhatsApp • now
                                                    </span>
                                                </div>
                                                <span className="text-[10px] text-slate-400">Sunday</span>
                                            </div>

                                            <div>
                                                <div className="flex items-center gap-1">
                                                    <span className="font-bold text-xs text-slate-950">Fundile Learning Assistant</span>
                                                    <span className="text-[9px] bg-emerald-500 text-white font-bold px-1 rounded">✓</span>
                                                </div>
                                                <p className="text-[11px] text-slate-700 leading-snug mt-0.5">
                                                    📄 <strong>{current.name}</strong> achieved <strong>{current.mastery}% ({current.level})</strong> in Grade 10 Accounting! Tap to view the weekly diagnostic PDF report.
                                                </p>
                                            </div>

                                            {/* Translucent Animated Tap Ripple */}
                                            <div className="pt-1 flex items-center justify-between text-[10px] text-[#13519C] font-semibold">
                                                <span className="flex items-center gap-1">
                                                    <span className="w-2 h-2 rounded-full bg-[#FF9100] animate-ping" />
                                                    Tap to open WhatsApp message
                                                </span>
                                                <ChevronRight className="w-3.5 h-3.5 text-[#13519C]" />
                                            </div>
                                        </div>

                                        {/* Bottom lock screen helper */}
                                        <div className="text-center pb-3">
                                            <span className="text-[10px] text-slate-400 uppercase tracking-widest font-semibold">
                                                Swipe up or tap alert to open
                                            </span>
                                        </div>
                                    </div>
                                )}

                                {/* ── STAGE 1: OPEN WHATSAPP CHAT & PDF CARD ── */}
                                {simuStage === 1 && (
                                    <div className="flex-1 bg-[#E5DDD5] flex flex-col overflow-hidden text-slate-900">
                                        {/* WhatsApp Chat Header */}
                                        <div className="bg-[#075E54] text-white px-3.5 py-2.5 flex items-center gap-2.5 shadow-sm shrink-0">
                                            <div className="w-7 h-7 rounded-full bg-white/20 flex items-center justify-center text-xs font-bold border border-white/30">
                                                F
                                            </div>
                                            <div className="flex-1 min-w-0">
                                                <div className="flex items-center gap-1">
                                                    <span className="font-bold text-xs truncate">Fundile Learning Assistant</span>
                                                    <span className="text-[9px] bg-emerald-400 text-slate-950 font-bold px-1 rounded">✓</span>
                                                </div>
                                                <span className="text-[9px] text-emerald-100 block">Online • Automated Dispatch</span>
                                            </div>
                                        </div>

                                        {/* Chat Canvas with WhatsApp bubble pattern */}
                                        <div 
                                            className="p-3 flex-1 flex flex-col justify-end space-y-2.5 text-xs overflow-y-auto"
                                            style={{ backgroundImage: 'radial-gradient(#d1c7b8 1px, transparent 1px)', backgroundSize: '16px 16px' }}
                                        >
                                            <div className="text-center">
                                                <span className="bg-white/80 backdrop-blur-sm text-slate-600 text-[9px] font-bold px-2 py-0.5 rounded-full shadow-xs">
                                                    Sunday, 08:30 AM
                                                </span>
                                            </div>

                                            {/* WhatsApp Message Bubble */}
                                            <div className="bg-white rounded-2xl rounded-tl-sm p-3 shadow-sm border border-slate-200/60 space-y-2">
                                                <p className="text-[11px] text-slate-800 leading-relaxed">
                                                    Good morning. Here is the official weekly academic progress and diagnostic report for <strong>{current.name}</strong> ({current.grade}).
                                                </p>

                                                {/* TAP TO OPEN PDF DOCUMENT CARD */}
                                                <button
                                                    type="button"
                                                    onClick={() => {
                                                        setIsAutoPlaying(false);
                                                        setSimuStage(2);
                                                    }}
                                                    className="w-full text-left bg-slate-50 hover:bg-slate-100 border border-slate-200 rounded-xl p-2.5 flex items-center gap-2.5 transition-all hover:shadow-sm cursor-pointer group"
                                                >
                                                    <div className="h-9 w-9 rounded-lg bg-rose-500 text-white flex flex-col items-center justify-center font-bold text-[9px] shadow-xs shrink-0 group-hover:scale-105 transition-transform">
                                                        <span>PDF</span>
                                                        <FileText className="h-3.5 w-3.5 text-white" />
                                                    </div>
                                                    <div className="flex-1 min-w-0">
                                                        <span className="font-bold text-[11px] text-slate-900 truncate block group-hover:text-[#13519C]">
                                                            {current.pdfFilename}
                                                        </span>
                                                        <div className="flex items-center gap-1.5 text-[9px] text-slate-500 mt-0.5">
                                                            <span>1 page</span>
                                                            <span>•</span>
                                                            <span>{current.fileSize}</span>
                                                            <span>•</span>
                                                            <span className="text-[#13519C] font-bold inline-flex items-center gap-0.5">
                                                                <Eye className="h-3 w-3 text-[#FF9100]" /> Tap to view report
                                                            </span>
                                                        </div>
                                                    </div>
                                                </button>

                                                {/* Digest Micro-Stats */}
                                                <div className="bg-blue-50/80 border border-blue-100 p-2 rounded-lg text-[10px] flex justify-between items-center">
                                                    <span className="text-slate-600 font-medium">CAPS Readiness:</span>
                                                    <span className="font-bold text-[#13519C]">{current.mastery}% ({current.level})</span>
                                                </div>

                                                <div className="pt-0.5 flex items-center justify-between text-[9px] text-slate-400">
                                                    <span>Fundile Verified Diagnostic</span>
                                                    <span>08:30 AM ✓✓</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                )}

                                {/* ── STAGE 2: OPENING PDF REPORT INSIDE SMARTPHONE ── */}
                                {simuStage === 2 && (
                                    <div className="flex-1 bg-white flex flex-col overflow-hidden text-slate-900">
                                        {/* Mobile PDF Reader Header */}
                                        <div className="bg-slate-900 text-white px-3.5 py-2 flex items-center justify-between text-xs shrink-0">
                                            <div className="flex items-center gap-2 min-w-0">
                                                <FileText className="w-3.5 h-3.5 text-[#FFD166] shrink-0" />
                                                <span className="text-[11px] font-bold truncate">{current.pdfFilename}</span>
                                            </div>
                                            <button
                                                type="button"
                                                onClick={() => setShowPdfModal(true)}
                                                className="px-2 py-0.5 rounded bg-white/10 hover:bg-white/20 text-[10px] font-bold text-white shrink-0 cursor-pointer"
                                            >
                                                Full A4
                                            </button>
                                        </div>

                                        {/* Inner Document Canvas */}
                                        <div className="p-3.5 flex-1 overflow-y-auto space-y-2.5 text-left bg-slate-50 text-xs">
                                            {/* Report Title & Profile */}
                                            <div className="border-b border-slate-200 pb-2">
                                                <div className="flex items-center justify-between">
                                                    <span className="text-[9px] font-bold uppercase tracking-wider text-blue-800">
                                                        Official Diagnostic Report
                                                    </span>
                                                    <span className="text-[9px] text-emerald-600 font-bold bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200">
                                                        {current.level}
                                                    </span>
                                                </div>
                                                <h4 className="font-bold text-sm text-slate-900 mt-0.5 leading-tight">
                                                    {current.name} • {current.grade}
                                                </h4>
                                                <span className="text-[10px] text-slate-500">CAPS Term Evaluation • Overall Mastery: {current.mastery}%</span>
                                            </div>

                                            {/* Procedural Flaw Autopsy */}
                                            <div className="p-2.5 rounded-xl bg-amber-50 border border-amber-200 text-[11px] space-y-1">
                                                <span className="text-[9px] font-bold uppercase tracking-wider text-amber-900 block">
                                                    Procedural Flaw Autopsy:
                                                </span>
                                                <p className="text-slate-800 leading-snug">
                                                    {current.flawedProcedure}
                                                </p>
                                                <span className="text-[10px] text-amber-800 font-semibold block">
                                                    📊 {current.cohortFlawStat}
                                                </span>
                                            </div>

                                            {/* Consequential Method Marks */}
                                            <div className="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-[11px] space-y-0.5">
                                                <span className="text-[9px] font-bold uppercase tracking-wider text-emerald-900 block">
                                                    Consequential Marking Credit:
                                                </span>
                                                <p className="text-slate-800 leading-snug">
                                                    {current.methodMarksAwarded}
                                                </p>
                                            </div>

                                            {/* Dinner Conversation Starter */}
                                            <div className="p-2.5 rounded-xl bg-blue-50 border border-blue-200 text-[11px] space-y-0.5">
                                                <span className="text-[9px] font-bold uppercase tracking-wider text-blue-900 block">
                                                    Parent Conversation Starter:
                                                </span>
                                                <p className="text-slate-700 italic leading-snug">
                                                    "{current.prompt}"
                                                </p>
                                            </div>
                                        </div>

                                        {/* PDF Bottom Footer */}
                                        <div className="bg-slate-100 p-2 border-t border-slate-200 text-center shrink-0">
                                            <button
                                                type="button"
                                                onClick={() => setShowPdfModal(true)}
                                                className="w-full py-1.5 rounded-lg bg-[#13519C] text-white text-[10px] font-bold hover:bg-[#0f3e77] transition shadow-xs cursor-pointer flex items-center justify-center gap-1"
                                            >
                                                <ExternalLink className="w-3 h-3" />
                                                <span>Expand to Official Printable A4 View</span>
                                            </button>
                                        </div>
                                    </div>
                                )}
                            </div>

                            {/* Click to open full modal hint */}
                            <button
                                type="button"
                                onClick={() => setShowPdfModal(true)}
                                className="mt-3 inline-flex items-center gap-1.5 px-4 py-1.5 rounded-full text-xs font-bold text-[#13519C] bg-blue-50 border border-blue-200 hover:bg-blue-100 transition shadow-xs cursor-pointer"
                            >
                                <Eye className="h-3.5 w-3.5 text-[#FF9100]" />
                                <span>Preview Full High-Resolution A4 Document</span>
                            </button>
                        </div>
                    </div>
                )}

                {/* ── TAB 2: MOBILE DATA SAVINGS METER ── */}
                {activeTab === 'data' && (
                    <div className="max-w-3xl mx-auto space-y-6 text-left py-4">
                        <div className="text-center mb-6">
                            <span className="text-xs font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-3 py-1 rounded-full border border-amber-200/70">
                                Zero Video Streaming Data Waste
                            </span>
                            <h4 className="text-2xl font-bold text-slate-900 mt-2">
                                Why Fundile uses 98% less mobile data than video platforms
                            </h4>
                            <p className="text-sm text-slate-600 mt-1">
                                Traditional online learning forces children to stream heavy YouTube videos. Fundile renders lightweight, deterministic code directly on the learner's phone.
                            </p>
                        </div>

                        {/* Comparative Meter Bars */}
                        <div className="space-y-4">
                            {/* Fundile Bar */}
                            <div className="p-4 rounded-2xl border border-emerald-200 bg-emerald-50/60 space-y-2">
                                <div className="flex justify-between items-center text-sm">
                                    <span className="font-bold text-slate-900 flex items-center gap-2">
                                        <Zap className="h-4 w-4 text-emerald-600" />
                                        Fundile SimuLearn Interactive Session (1 Hour)
                                    </span>
                                    <span className="font-extrabold text-emerald-700 text-base">~1.8 MB</span>
                                </div>
                                <div className="w-full bg-emerald-200/70 h-3 rounded-full overflow-hidden">
                                    <div className="bg-emerald-500 h-full rounded-full" style={{ width: '3%' }} />
                                </div>
                                <p className="text-xs text-emerald-800">
                                    Lightweight vector drawings and Python calculation engines. Works smoothly even on 2G or poor rural cell reception.
                                </p>
                            </div>

                            {/* Traditional Video Bar */}
                            <div className="p-4 rounded-2xl border border-red-200 bg-red-50/50 space-y-2">
                                <div className="flex justify-between items-center text-sm">
                                    <span className="font-bold text-slate-900 flex items-center gap-2">
                                        <span>📹</span>
                                        Video Tutoring / YouTube Educational Streams (1 Hour)
                                    </span>
                                    <span className="font-extrabold text-red-700 text-base">~450 – 800 MB</span>
                                </div>
                                <div className="w-full bg-red-200/70 h-3 rounded-full overflow-hidden">
                                    <div className="bg-red-500 h-full rounded-full" style={{ width: '100%' }} />
                                </div>
                                <p className="text-xs text-red-800">
                                    Drains household mobile data bundles, buffers constantly in load-shedding, and costs families hundreds of Rands every month.
                                </p>
                            </div>
                        </div>

                        {/* Monthly Family Savings Box */}
                        <div className="p-5 rounded-2xl border border-blue-200 bg-blue-50/50 flex flex-col sm:flex-row items-center justify-between gap-4">
                            <div>
                                <span className="text-xs font-bold uppercase tracking-wider text-[#13519C]">
                                    Estimated Family Monthly Savings
                                </span>
                                <h5 className="text-xl font-bold text-slate-900 mt-0.5">
                                    Saves ~R180 to R350 every month in data per learner
                                </h5>
                                <p className="text-xs text-slate-600 mt-1">
                                    Calculated on standard South African prepay data rates (15GB/mo typical video load vs 100MB/mo with Fundile).
                                </p>
                            </div>
                            <div className="text-center sm:text-right shrink-0">
                                <span className="text-3xl font-extrabold text-[#13519C]">98%</span>
                                <span className="block text-xs font-bold text-slate-500 uppercase">Data Reduction</span>
                            </div>
                        </div>
                    </div>
                )}

                {/* ── TAB 3: CAPS EXAM READINESS ── */}
                {activeTab === 'readiness' && (
                    <div className="max-w-3xl mx-auto space-y-6 text-left py-4">
                        <div className="text-center mb-6">
                            <span className="text-xs font-bold uppercase tracking-wider text-indigo-600 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-200/70">
                                Continuous Diagnostic Tracking
                            </span>
                            <h4 className="text-2xl font-bold text-slate-900 mt-2">
                                Term Pacing &amp; Exam Readiness without Exam-Eve Panic
                            </h4>
                            <p className="text-sm text-slate-600 mt-1">
                                Fundile tracks syllabus mastery continuously. When term exams arrive, learners don't cram—they have already calibrated every question archetype.
                            </p>
                        </div>

                        {/* Subject Gauges */}
                        <div className="grid sm:grid-cols-3 gap-4">
                            {[
                                { subject: 'Accounting Gr 10', score: 86, term: 'Term 1 & 2', status: 'Exam-Ready', color: 'text-indigo-600', bg: 'bg-indigo-50 border-indigo-200' },
                                { subject: 'Mathematics Gr 10', score: 82, term: 'Term 1 & 2', status: 'Exam-Ready', color: 'text-blue-600', bg: 'bg-blue-50 border-blue-200' },
                                { subject: 'Business Studies Gr 10', score: 91, term: 'Term 1 & 2', status: 'Mastered', color: 'text-emerald-600', bg: 'bg-emerald-50 border-emerald-200' },
                            ].map((item, i) => (
                                <div key={i} className={`p-4 rounded-2xl border ${item.bg} text-center space-y-2`}>
                                    <span className="text-xs font-bold text-slate-600 block">{item.subject}</span>
                                    <div className="text-3xl font-extrabold text-slate-900">
                                        {item.score}%
                                    </div>
                                    <span className={`text-[11px] font-bold px-2 py-0.5 rounded-full ${item.color} bg-white shadow-xs`}>
                                        {item.status}
                                    </span>
                                    <span className="block text-[10px] text-slate-500">{item.term}</span>
                                </div>
                            ))}
                        </div>

                        {/* Guarantee note */}
                        <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center text-xs text-slate-600">
                            <strong>Authentic Curriculum Alignment:</strong> Questions, mark allocations, and worked solutions strictly follow national curriculum criteria and examination standards.
                        </div>
                    </div>
                )}
            </div>

            {/* Bottom CTA bar */}
            <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-3">
                <button
                    type="button"
                    onClick={onGetStarted}
                    className="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-xl bg-[#FF9100] px-8 py-3.5 text-sm sm:text-base font-semibold text-white shadow-md hover:bg-[#f58200] transition cursor-pointer"
                >
                    Start 2-Week Free Family Trial
                    <ArrowRight className="h-4.5 w-4.5" />
                </button>
                {onSelectPerspective && (
                    <button
                        type="button"
                        onClick={() => onSelectPerspective('learners')}
                        className="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-xl px-5 py-3.5 text-sm sm:text-base font-semibold border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 transition cursor-pointer"
                    >
                        <ArrowLeft className="h-4 w-4" />
                        Return to Learner View
                    </button>
                )}
            </div>
            <p className="mt-3 text-xs text-slate-500 text-center">
                R150 / month after trial · Cancel anytime · Zero credit card required to start
            </p>
        </div>
    );
};

export default ParentSimulation;
