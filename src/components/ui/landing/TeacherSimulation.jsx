import React, { useState } from 'react';
import {
    Printer,
    FileText,
    CheckCircle2,
    Users,
    Zap,
    ArrowRight,
    Sparkles,
    Check,
    AlertCircle,
    Copy,
    ArrowLeft,
} from 'lucide-react';

const TeacherSimulation = ({ isLightPalette = true, onGetStarted, onSelectPerspective }) => {
    const [selectedSubject, setSelectedSubject] = useState('accounting'); // 'accounting' | 'maths' | 'business'
    const [marksTime, setMarksTime] = useState('30marks'); // '30marks' | '50marks'
    const [activeViewTab, setActiveViewTab] = useState('paper'); // 'paper' | 'memo' | 'heatmap'
    const [isGenerating, setIsGenerating] = useState(false);
    const [assignedDrill, setAssignedDrill] = useState(false);

    const testScenarios = {
        accounting: {
            title: 'General Journal & Subsidiary Ledgers Assessment',
            grade: 'Grade 10 Accounting',
            term: 'Term 1 / Term 2 Benchmark',
            totalMarks: marksTime === '30marks' ? 30 : 50,
            duration: marksTime === '30marks' ? '45 minutes' : '60 minutes',
            q1Title: 'QUESTION 1: GENERAL JOURNAL ENTRIES',
            q1Marks: 12,
            q1Text: 'Record the following transactions in the General Journal of Sunrise Traders for March 2024. Show all working clearly.',
            transactions: [
                '1. 14 March: J. Dlamini, a debtor owing R1,600, was declared insolvent. Receive 40c in the Rand and write off the balance as irrecoverable.',
                '2. 22 March: Owner took merchandise for personal use, cost price R850, selling price R1,150.',
            ],
            memoSteps: [
                { desc: 'Bank account debited with cash received (40% of R1,600 = R640)', marks: '✓ 2M' },
                { desc: 'Bad Debts debited with irrecoverable balance (60% of R1,600 = R960)', marks: '✓ 2M' },
                { desc: 'Debtors Control credited with total discharged balance (R1,600)', marks: '✓ 2A' },
                { desc: 'Drawings debited with cost price R850 (not selling price)', marks: '✓ 2M' },
                { desc: 'Trading Stock credited with cost price R850', marks: '✓ 2A' },
                { desc: 'Narrations correctly formulated and verified', marks: '✓ 2M' },
            ],
            misconception: 'Selling price vs cost price on Drawings (net vs gross confusion)',
            affectedCount: 16,
            totalStudents: 28,
        },
        maths: {
            title: 'Algebraic Expressions & Quadratic Factorisation',
            grade: 'Grade 10 Mathematics',
            term: 'Term 1 / Term 2 Benchmark',
            totalMarks: marksTime === '30marks' ? 30 : 50,
            duration: marksTime === '30marks' ? '45 minutes' : '60 minutes',
            q1Title: 'QUESTION 1: FACTORISATION & SIMPLIFICATION',
            q1Marks: 10,
            q1Text: 'Factorise the following expressions fully and state all restrictions where applicable.',
            transactions: [
                '1.1 Simplify: (3x² - 12) / (x² - 4x + 4)',
                '1.2 Solve for x: 2x² - 5x - 3 = 0',
            ],
            memoSteps: [
                { desc: 'Common factor extraction: 3(x² - 4) = 3(x - 2)(x + 2)', marks: '✓ 2M' },
                { desc: 'Trinomial denominator factorisation: (x - 2)²', marks: '✓ 2M' },
                { desc: 'Cancellation of identical binomial (x - 2) and final answer 3(x + 2)/(x - 2)', marks: '✓ 1A' },
                { desc: 'Quadratic factor pairs correctly resolved: (2x + 1)(x - 3) = 0', marks: '✓ 2M' },
                { desc: 'Both roots explicitly isolated: x = -1/2 or x = 3', marks: '✓ 2A' },
                { desc: 'Full consequential accuracy (CA) awarded if sign distributed uniformly', marks: '✓ 1CA' },
            ],
            misconception: 'Sign error when factorising trinomial outer/inner products',
            affectedCount: 12,
            totalStudents: 28,
        },
        business: {
            title: 'Business Environments & SWOT Classification',
            grade: 'Grade 11 Business Studies',
            term: 'Term 1 / Term 2 Benchmark',
            totalMarks: marksTime === '30marks' ? 30 : 50,
            duration: marksTime === '30marks' ? '45 minutes' : '60 minutes',
            q1Title: 'QUESTION 1: MACRO & MARKET ENVIRONMENT ANALYSIS',
            q1Marks: 14,
            q1Text: 'Read the case study of Zola Logistics and evaluate the environmental challenges. Classify each challenge into Micro, Market, or Macro environment.',
            transactions: [
                '1. High fuel price hikes decreed by the Department of Energy.',
                '2. Inadequate staff training leading to dispatch inventory shortages.',
                '3. New competitor offering 15% lower courier rates in Gauteng.',
            ],
            memoSteps: [
                { desc: 'Fuel price hike classified into Macro Environment (Economic / Legal factor)', marks: '✓ 2M' },
                { desc: 'Explain lack of control by management over macro environment', marks: '✓ 2A' },
                { desc: 'Staff training classified into Micro Environment (full management control)', marks: '✓ 2M' },
                { desc: 'Inventory shortage strategy correctly identified (internal skills audit)', marks: '✓ 2A' },
                { desc: 'Competitor pricing classified into Market Environment (limited control)', marks: '✓ 2M' },
                { desc: 'Appropriate strategic response formulated with rubric criteria', marks: '✓ 4M' },
            ],
            misconception: 'Macro vs Market environment control confusion',
            affectedCount: 14,
            totalStudents: 28,
        },
    };

    const current = testScenarios[selectedSubject];

    const handleSubjectSelect = (sub) => {
        setIsGenerating(true);
        setSelectedSubject(sub);
        setAssignedDrill(false);
        setTimeout(() => setIsGenerating(false), 200);
    };

    return (
        <div className="w-full">
            {/* Header & Subtitle */}
            <div className="text-center max-w-3xl mx-auto mb-8">
                <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-bold bg-indigo-500/10 border border-indigo-500/25 text-indigo-600 mb-3">
                    <span>👩‍🏫</span>
                    <span>Interactive Teacher LMS Cockpit Preview</span>
                </div>
                <h3
                    className="text-2xl sm:text-3xl lg:text-4xl font-bold tracking-tight text-slate-900"
                    style={{ fontFamily: 'Afacad, sans-serif' }}
                >
                    Fundile automates the setting of tests and exams with memos.
                </h3>
                <p className="mt-2 text-sm sm:text-base text-slate-600">
                    Built for teachers and schools to generate exam-standard printable A4 test papers, verified teacher memoranda with consequential marking rules, and instant class heatmaps in seconds.
                </p>
            </div>

            {/* Assessment Generator Controller Bar */}
            <div className="bg-slate-50 border border-slate-200 p-4 sm:p-5 rounded-2xl mb-6 max-w-4xl mx-auto shadow-xs text-left">
                <span className="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-3">
                    Interactive Generator Controls:
                </span>
                <div className="grid sm:grid-cols-3 gap-3">
                    {/* Click 1: Subject & Topic */}
                    <div>
                        <label className="text-[11px] font-bold text-slate-700 block mb-1">
                            1. Select Subject &amp; Topic:
                        </label>
                        <select
                            value={selectedSubject}
                            onChange={(e) => handleSubjectSelect(e.target.value)}
                            className="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-[#13519C]"
                        >
                            <option value="accounting">Gr 10 Accounting · General Journal</option>
                            <option value="maths">Gr 10 Mathematics · Quad Factorisation</option>
                            <option value="business">Gr 11 Business Studies · SWOT Analysis</option>
                        </select>
                    </div>

                    {/* Click 2: Marks & Time */}
                    <div>
                        <label className="text-[11px] font-bold text-slate-700 block mb-1">
                            2. Mark Weight &amp; Duration:
                        </label>
                        <select
                            value={marksTime}
                            onChange={(e) => setMarksTime(e.target.value)}
                            className="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-[#13519C]"
                        >
                            <option value="30marks">30 Marks · 45 Mins (Class Quiz)</option>
                            <option value="50marks">50 Marks · 60 Mins (Cycle Test)</option>
                        </select>
                    </div>

                    {/* Click 3: Action status */}
                    <div>
                        <label className="text-[11px] font-bold text-slate-700 block mb-1">
                            3. Generation Engine:
                        </label>
                        <div className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-bold">
                            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                            <span>100% Deterministic · Zero AI Hallucinations</span>
                        </div>
                    </div>
                </div>
            </div>

            {/* Document Preview Tabs */}
            <div className="flex flex-wrap items-center justify-center gap-2 mb-6">
                {[
                    { id: 'paper', label: '1. Printable A4 Exam Paper', icon: FileText, badge: 'Photocopy Ready' },
                    { id: 'memo', label: '2. Official Marking Memorandum', icon: CheckCircle2, badge: 'NSC Method Marks' },
                    { id: 'heatmap', label: '3. Flawed Procedure Analytics', icon: AlertCircle, badge: 'Cohort Diagnosis' },
                    { id: 'submissions', label: '4. Live Class Submissions', icon: Users, badge: '22/28 Submitted' },
                    { id: 'quiz_maker', label: '5. Online Quiz Production', icon: Zap, badge: 'Join Code: MAT-702' },
                ].map((tab) => {
                    const Icon = tab.icon;
                    const isActive = activeViewTab === tab.id;
                    return (
                        <button
                            key={tab.id}
                            type="button"
                            onClick={() => setActiveViewTab(tab.id)}
                            className={`inline-flex items-center gap-2 px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-full text-xs sm:text-sm font-bold transition-all duration-200 cursor-pointer ${
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
            <div className="bg-white border border-slate-200 rounded-[28px] p-4 sm:p-8 shadow-sm text-left">
                {/* ── TAB 1: PRINTABLE EXAM PAPER ── */}
                {activeViewTab === 'paper' && (
                    <div className="space-y-6 max-w-3xl mx-auto">
                        <div className="border-b-2 border-slate-900 pb-3 flex justify-between items-center">
                            <div>
                                <span className="text-[10px] uppercase font-bold tracking-wider text-slate-500">
                                    Official National Curriculum Assessment Paper
                                </span>
                                <h4 className="text-xl sm:text-2xl font-bold text-slate-900 mt-1">
                                    {current.title}
                                </h4>
                            </div>
                            <div className="text-right">
                                <span className="text-xs font-bold text-[#13519C] block">{current.grade}</span>
                                <span className="text-[11px] text-slate-500 font-medium">{current.totalMarks} Marks · {current.duration}</span>
                            </div>
                        </div>

                        {/* Question 1 Body */}
                        <div className="p-4 bg-slate-50 border border-slate-200 rounded-2xl space-y-3">
                            <div className="flex justify-between items-center text-xs font-bold text-slate-800">
                                <span>{current.q1Title}</span>
                                <span className="text-[#13519C] bg-blue-50 px-2 py-0.5 rounded-md border border-blue-200">[{current.q1Marks} Marks]</span>
                            </div>
                            <p className="text-xs text-slate-600 leading-relaxed font-serif">
                                {current.q1Text}
                            </p>
                            <div className="space-y-2 pt-2 border-t border-slate-200/80">
                                {current.transactions.map((tx, idx) => (
                                    <p key={idx} className="text-xs text-slate-700 font-mono bg-white p-2.5 rounded-xl border border-slate-200/60">
                                        {tx}
                                    </p>
                                ))}
                            </div>
                        </div>

                        {/* Action Buttons */}
                        <div className="flex flex-col sm:flex-row justify-between items-center gap-3 pt-2">
                            <span className="text-xs text-slate-500">
                                Output format: Clean A4 monochrome for sharp photocopy duplication
                            </span>
                            <div className="flex gap-2 w-full sm:w-auto">
                                <button
                                    type="button"
                                    onClick={() => alert('Simulated print: Printable A4 test paper sent to printer.')}
                                    className="flex-1 sm:flex-none inline-flex items-center justify-center gap-2 px-4 py-2 rounded-xl bg-[#13519C] text-white text-xs font-semibold shadow-xs hover:bg-[#0f3e77] transition cursor-pointer"
                                >
                                    <Printer className="h-4 w-4" />
                                    <span>Print A4 Paper</span>
                                </button>
                                <button
                                    type="button"
                                    onClick={() => setActiveViewTab('memo')}
                                    className="flex-1 sm:flex-none inline-flex items-center justify-center gap-2 px-4 py-2 rounded-xl bg-slate-100 text-slate-700 text-xs font-semibold hover:bg-slate-200 transition cursor-pointer"
                                >
                                    <span>View Marking Memo →</span>
                                </button>
                            </div>
                        </div>
                    </div>
                )}

                {/* ── TAB 2: OFFICIAL MARKING MEMORANDUM ── */}
                {activeViewTab === 'memo' && (
                    <div className="space-y-6 max-w-3xl mx-auto">
                        <div className="border-b-2 border-indigo-900 pb-3 flex justify-between items-center">
                            <div>
                                <span className="text-[10px] uppercase font-bold tracking-wider text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded-full">
                                    OFFICIAL TEACHER MEMORANDUM
                                </span>
                                <h4 className="text-xl sm:text-2xl font-bold text-slate-900 mt-1">
                                    {current.title} — Marking Guide
                                </h4>
                            </div>
                            <span className="text-xs font-bold text-slate-600 bg-slate-100 px-3 py-1.5 rounded-lg">
                                Consequential Accuracy (CA) Enabled
                            </span>
                        </div>

                        <div className="overflow-x-auto">
                            <table className="w-full text-xs text-left border-collapse">
                                <thead>
                                    <tr className="bg-slate-100 text-slate-800 font-bold border-b border-slate-300">
                                        <th className="p-3">Step Point &amp; Marking Schema Description</th>
                                        <th className="p-3 text-center w-28">CAPS Mark</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {current.memoSteps.map((step, idx) => (
                                        <tr key={idx} className="border-b border-slate-200 hover:bg-slate-50/80">
                                            <td className="p-3 font-medium text-slate-800">
                                                {step.desc}
                                            </td>
                                            <td className="p-3 text-center font-bold text-[#13519C] bg-blue-50/40">
                                                {step.marks}
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>

                        <div className="p-4 bg-emerald-50 border border-emerald-200 rounded-2xl text-xs text-emerald-900 space-y-1">
                            <span className="font-bold block">✨ Automated Stepwise Procedure Marking in Pro Tier:</span>
                            <p>
                                When learners submit this test online, Fundile awards method marks automatically using rigorous step evaluation and automated coordinate marking—saving teachers 100% of weekend grading time.
                            </p>
                        </div>
                    </div>
                )}

                {/* ── TAB 3: FLAWED PROCEDURE ANALYTICS (Requests 4 & 5) ── */}
                {activeViewTab === 'heatmap' && (
                    <div className="space-y-6 max-w-3xl mx-auto">
                        <div className="border-b border-slate-200 pb-3 flex flex-col sm:flex-row justify-between sm:items-center gap-2">
                            <div>
                                <span className="text-[10px] uppercase font-bold tracking-wider text-rose-700 bg-rose-50 px-2.5 py-0.5 rounded-full">
                                    COHORT FLAWED PROCEDURE DIAGNOSTIC
                                </span>
                                <h4 className="text-xl font-bold text-slate-900 mt-1">
                                    Grade 10A · 28 Learners Analyzed
                                </h4>
                            </div>
                            <span className="text-xs text-slate-500 font-medium">
                                Procedure breakdown across recent submissions
                            </span>
                        </div>

                        {/* Identified Procedure Flaw Banner */}
                        <div className="p-4 rounded-2xl border border-amber-300 bg-amber-50/80 space-y-3">
                            <div className="flex items-start justify-between gap-3">
                                <div>
                                    <div className="flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-amber-900">
                                        <AlertCircle className="h-4 w-4 text-amber-700" />
                                        <span>Systemic Procedural Flaw Localized:</span>
                                    </div>
                                    <h5 className="text-base font-bold text-slate-900 mt-1">
                                        {current.misconception}
                                    </h5>
                                    <p className="text-xs text-slate-700 mt-1">
                                        <strong>16 of 28 learners</strong> followed this exact flawed procedure (using Selling Price R1,150 instead of Cost Price R850 on Drawings), losing 4 to 6 marks each.
                                    </p>
                                </div>
                                <span className="text-xs font-extrabold bg-amber-200 text-amber-900 px-3 py-1 rounded-full shrink-0">
                                    {Math.round((current.affectedCount / current.totalStudents) * 100)}% of class
                                </span>
                            </div>

                            <div className="p-3 bg-white/90 rounded-xl border border-amber-200 text-xs space-y-1">
                                <span className="font-bold text-slate-800 block">Teacher Intervention Recommendation:</span>
                                <p className="text-slate-600">
                                    Do not reteach the entire General Journal unit. Dispatch a 5-minute atomic micro-drill isolating <em>strictly</em> the Drawings cost-price rule so automaticity is restored before the cycle test.
                                </p>
                            </div>

                            <div className="pt-1">
                                {!assignedDrill ? (
                                    <button
                                        type="button"
                                        onClick={() => setAssignedDrill(true)}
                                        className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-[#13519C] text-white text-xs font-bold shadow-md hover:bg-[#0f3e77] transition cursor-pointer"
                                    >
                                        <Zap className="h-4 w-4 text-[#FFD166]" />
                                        <span>1-Click Dispatch 5-Min Remedial Drill to 16 Affected Learners</span>
                                    </button>
                                ) : (
                                    <div className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-emerald-600 text-white text-xs font-bold shadow-sm">
                                        <CheckCircle2 className="h-4 w-4" />
                                        <span>Remedial drill dispatched to 16 student smartphones via Class Code! Gaps scheduled for review.</span>
                                    </div>
                                )}
                            </div>
                        </div>

                        {/* Aggregate Procedure Statistics */}
                        <div className="grid sm:grid-cols-3 gap-3">
                            <div className="bg-slate-50 p-3 rounded-xl border border-slate-200 text-center">
                                <span className="text-[10px] text-slate-500 font-bold uppercase block">Average Method Marks Lost</span>
                                <span className="text-xl font-bold text-rose-600">-5.4 Marks</span>
                            </div>
                            <div className="bg-slate-50 p-3 rounded-xl border border-slate-200 text-center">
                                <span className="text-[10px] text-slate-500 font-bold uppercase block">Remedial Recovery Target</span>
                                <span className="text-xl font-bold text-emerald-600">+100% In 5 Mins</span>
                            </div>
                            <div className="bg-slate-50 p-3 rounded-xl border border-slate-200 text-center">
                                <span className="text-[10px] text-slate-500 font-bold uppercase block">Grading Time Saved</span>
                                <span className="text-xl font-bold text-[#13519C]">2.5 Hours</span>
                            </div>
                        </div>
                    </div>
                )}

                {/* ── TAB 4: LIVE CLASS SUBMISSIONS MONITOR (Requests 4 & 5) ── */}
                {activeViewTab === 'submissions' && (
                    <div className="space-y-6 max-w-3xl mx-auto">
                        <div className="border-b border-slate-200 pb-3 flex flex-col sm:flex-row justify-between sm:items-center gap-2">
                            <div>
                                <span className="text-[10px] uppercase font-bold tracking-wider text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded-full">
                                    LIVE HOMEWORK &amp; ASSIGNMENT ROSTER
                                </span>
                                <h4 className="text-xl font-bold text-slate-900 mt-1">
                                    Grade 10A Accounting · Assignment #4 Submissions
                                </h4>
                            </div>
                            <div className="flex items-center gap-2">
                                <span className="text-xs font-bold bg-emerald-100 text-emerald-800 px-2.5 py-1 rounded-full">
                                    22 of 28 Submitted (78%)
                                </span>
                            </div>
                        </div>

                        {/* Submissions Table */}
                        <div className="overflow-x-auto border border-slate-200 rounded-xl">
                            <table className="w-full text-xs text-left border-collapse">
                                <thead>
                                    <tr className="bg-slate-100 text-slate-800 font-bold border-b border-slate-200">
                                        <th className="p-3">Learner Name</th>
                                        <th className="p-3">Status</th>
                                        <th className="p-3 text-center">Auto-Marked Score</th>
                                        <th className="p-3">Procedural Error Diagnosis</th>
                                        <th className="p-3 text-right">Submission Time</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {[
                                        { name: 'Sipho Zulu', status: 'Submitted', score: '92%', error: 'Sound Procedure (Level 7)', time: '14:20 Yesterday', color: 'text-emerald-700' },
                                        { name: 'Nqobile Moyo', status: 'Submitted', score: '84%', error: 'Drawings net vs gross error', time: '18:05 Yesterday', color: 'text-amber-700' },
                                        { name: 'Thabo Mokoena', status: 'Submitted', score: '58%', error: 'Drawings net vs gross error', time: '20:11 Yesterday', color: 'text-rose-700' },
                                        { name: 'Lerato Dlamini', status: 'Submitted', score: '78%', error: 'Sound Procedure (Level 6)', time: '07:45 Today', color: 'text-emerald-700' },
                                        { name: 'Bongani Sithole', status: 'In Progress', score: '—', error: 'Active on Question 3 of 4', time: 'Active now', color: 'text-blue-600' },
                                        { name: 'Zanele Khumalo', status: 'Pending', score: '—', error: 'Automated SMS reminder sent', time: 'Not started', color: 'text-slate-400' },
                                    ].map((student, idx) => (
                                        <tr key={idx} className="border-b border-slate-100 last:border-0 hover:bg-slate-50">
                                            <td className="p-3 font-semibold text-slate-900">{student.name}</td>
                                            <td className="p-3">
                                                <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                                                    student.status === 'Submitted' ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' :
                                                    student.status === 'In Progress' ? 'bg-blue-50 text-blue-700 border border-blue-200' : 'bg-slate-100 text-slate-600'
                                                }`}>
                                                    {student.status}
                                                </span>
                                            </td>
                                            <td className="p-3 text-center font-mono font-bold text-slate-800">{student.score}</td>
                                            <td className={`p-3 font-medium ${student.color}`}>{student.error}</td>
                                            <td className="p-3 text-right text-slate-500">{student.time}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>

                        <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl flex items-center justify-between text-xs">
                            <span className="text-slate-600">
                                Pro tier tracks step-level procedure timings and flags learners who spend &gt;8 mins on factor pairs.
                            </span>
                            <button
                                type="button"
                                onClick={() => alert('Simulated reminder: WhatsApp nudge sent to remaining 6 students.')}
                                className="px-3 py-1.5 rounded-lg bg-white border border-slate-200 text-[#13519C] font-semibold hover:bg-slate-50 cursor-pointer"
                            >
                                Send Nudge to Incomplete
                            </button>
                        </div>
                    </div>
                )}

                {/* ── TAB 5: ONLINE QUIZ PRODUCTION (Request 5) ── */}
                {activeViewTab === 'quiz_maker' && (
                    <div className="space-y-6 max-w-3xl mx-auto">
                        <div className="border-b border-slate-200 pb-3 flex justify-between items-center">
                            <div>
                                <span className="text-[10px] uppercase font-bold tracking-wider text-cyan-700 bg-cyan-50 px-2.5 py-0.5 rounded-full">
                                    INSTANT ONLINE QUIZ BUILDER
                                </span>
                                <h4 className="text-xl font-bold text-slate-900 mt-1">
                                    Configure &amp; Dispatch Online Quizzes in 60 Seconds
                                </h4>
                            </div>
                            <span className="text-xs font-mono font-bold bg-cyan-100 text-cyan-900 px-3 py-1 rounded-lg">
                                CLASS CODE: ACC-801
                            </span>
                        </div>

                        {/* Builder Form Card */}
                        <div className="bg-slate-50 p-5 rounded-2xl border border-slate-200 space-y-4">
                            <div className="grid sm:grid-cols-2 gap-4">
                                <div>
                                    <label className="text-xs font-bold text-slate-700 block mb-1">Target Subject &amp; Grade:</label>
                                    <input
                                        type="text"
                                        readOnly
                                        value="Grade 10 Accounting · Sole Trader General Journal"
                                        className="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800"
                                    />
                                </div>
                                <div>
                                    <label className="text-xs font-bold text-slate-700 block mb-1">Assessment Rigour Mode:</label>
                                    <select className="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800">
                                        <option>Practice Mode (3-Tier Hints Enabled)</option>
                                        <option>Strict Assessment Mode (Exam Timer &amp; Zero Hints)</option>
                                    </select>
                                </div>
                            </div>

                            <div className="grid sm:grid-cols-3 gap-3">
                                <div className="bg-white p-3 rounded-xl border border-slate-200">
                                    <span className="text-[10px] font-bold text-slate-500 uppercase block">Question Variations</span>
                                    <span className="text-sm font-bold text-slate-800">Seeded (Anti-Cheating)</span>
                                </div>
                                <div className="bg-white p-3 rounded-xl border border-slate-200">
                                    <span className="text-[10px] font-bold text-slate-500 uppercase block">Mark Allocation</span>
                                    <span className="text-sm font-bold text-[#13519C]">Automated NSC Rubric</span>
                                </div>
                                <div className="bg-white p-3 rounded-xl border border-slate-200">
                                    <span className="text-[10px] font-bold text-slate-500 uppercase block">Mobile Compatibility</span>
                                    <span className="text-sm font-bold text-emerald-600">Zero App Install</span>
                                </div>
                            </div>

                            <div className="pt-2 flex flex-col sm:flex-row justify-between items-center gap-3">
                                <span className="text-xs text-slate-500">
                                    Learners enter code <strong>ACC-801</strong> on their smartphone to start immediately.
                                </span>
                                <button
                                    type="button"
                                    onClick={() => alert('Online Quiz Dispatched! Link: https://fundile.com/quiz/ACC-801 copied to clipboard.')}
                                    className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold shadow-md transition cursor-pointer"
                                >
                                    <Zap className="h-4 w-4" />
                                    <span>Dispatch to Class WhatsApp / Classroom</span>
                                </button>
                            </div>
                        </div>
                    </div>
                )}
            </div>

            {/* Bottom CTA Bar */}
            <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-3">
                <button
                    type="button"
                    onClick={onGetStarted}
                    className="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-xl bg-[#13519C] px-8 py-3.5 text-sm sm:text-base font-semibold text-white shadow-md hover:bg-[#0f3e77] transition cursor-pointer"
                >
                    Open Teacher LMS Cockpit
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
                Instant 6-character class join codes · Zero student email setup required · Works on any smartphone
            </p>
        </div>
    );
};

export default TeacherSimulation;
