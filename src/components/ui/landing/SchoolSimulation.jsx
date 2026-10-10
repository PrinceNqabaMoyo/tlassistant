import React, { useState } from 'react';
import {
    Building2,
    BarChart3,
    CheckCircle2,
    Clock,
    Mail,
    Receipt,
    Lock,
    ArrowRight,
    Users,
    AlertTriangle,
    Send,
    Download,
    FileCheck,
    ArrowLeft,
} from 'lucide-react';

const SchoolSimulation = ({ isLightPalette = true, onGetStarted, onSelectPerspective }) => {
    const [activeTab, setActiveTab] = useState('pacing'); // 'pacing' | 'intervention' | 'sgb'
    const [selectedCohort, setSelectedCohort] = useState('gr10'); // 'gr10' | 'gr11' | 'gr12'
    const [dispatchedAlert, setDispatchedAlert] = useState(false);

    const cohortData = {
        gr10: {
            title: 'Grade 10 Department Overview',
            subject: 'Accounting & Mathematics',
            totalLearners: 142,
            overallPacing: 88,
            classes: [
                { name: 'Grade 10A (Mrs. Khumalo)', enrolled: 34, pacing: 94, status: 'On Track', color: 'text-emerald-700 bg-emerald-50 border-emerald-200' },
                { name: 'Grade 10B (Mr. Dlamini)', enrolled: 36, pacing: 78, status: '2 Weeks Behind', color: 'text-amber-700 bg-amber-50 border-amber-200' },
                { name: 'Grade 10C (Ms. Ndlovu)', enrolled: 35, pacing: 91, status: 'On Track', color: 'text-emerald-700 bg-emerald-50 border-emerald-200' },
                { name: 'Grade 10D (Mr. Botha)', enrolled: 37, pacing: 89, status: 'On Track', color: 'text-emerald-700 bg-emerald-50 border-emerald-200' },
            ],
            laggingTopic: 'Bank Reconciliation (Internal Controls & Ledgers)',
            laggingClass: 'Grade 10B',
            recommendedAction: '15-minute targeted Bank Recon diagnostic worksheet',
        },
        gr11: {
            title: 'Grade 11 Department Overview',
            subject: 'Physical Sciences & Mathematics',
            totalLearners: 128,
            overallPacing: 91,
            classes: [
                { name: 'Grade 11A (Dr. Pillay)', enrolled: 32, pacing: 96, status: 'Ahead of Pacing', color: 'text-emerald-700 bg-emerald-50 border-emerald-200' },
                { name: 'Grade 11B (Mrs. Molefe)', enrolled: 31, pacing: 84, status: 'Attention Needed', color: 'text-amber-700 bg-amber-50 border-amber-200' },
                { name: 'Grade 11C (Mr. Venter)', enrolled: 33, pacing: 92, status: 'On Track', color: 'text-emerald-700 bg-emerald-50 border-emerald-200' },
                { name: 'Grade 11D (Ms. Sithole)', enrolled: 32, pacing: 90, status: 'On Track', color: 'text-emerald-700 bg-emerald-50 border-emerald-200' },
            ],
            laggingTopic: 'Intermolecular Forces & Chemical Bonding',
            laggingClass: 'Grade 11B',
            recommendedAction: '20-minute conceptual bonding remediation drill',
        },
    };

    const current = cohortData[selectedCohort] || cohortData.gr10;

    return (
        <div className="w-full">
            {/* Header & Subtitle */}
            <div className="text-center max-w-3xl mx-auto mb-8">
                <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-bold bg-cyan-500/10 border border-cyan-500/25 text-cyan-700 mb-3">
                    <span>🏛️</span>
                    <span>Interactive School Admins Cockpit Preview</span>
                </div>
                <h3
                    className="text-2xl sm:text-3xl lg:text-4xl font-bold tracking-tight text-slate-900"
                    style={{ fontFamily: 'Afacad, sans-serif' }}
                >
                    Departmental pacing &amp; academic oversight in real time
                </h3>
                <p className="mt-2 text-sm sm:text-base text-slate-600">
                    See how Principals, Academic Directors, and School Admins monitor curriculum coverage across all classes, dispatch interventions, and manage SGB-compliant procurement.
                </p>
            </div>

            {/* Mode Selector Tabs */}
            <div className="flex flex-wrap items-center justify-center gap-2 mb-6">
                {[
                    { id: 'pacing', label: '1. Departmental Pacing Tracker', icon: BarChart3, badge: 'Cross-Class Pacing' },
                    { id: 'intervention', label: '2. Cross-Grade Procedure Analytics', icon: AlertTriangle, badge: 'Cohort Bottlenecks' },
                    { id: 'school_admin', label: '3. School Admin Dashboard', icon: Building2, badge: '270 Enrolled · 91% Completion' },
                    { id: 'sgb', label: '4. SGB Procurement & Invoicing', icon: Receipt, badge: 'info@fundile.com' },
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

            {/* Main Stage */}
            <div className="bg-white border border-slate-200 rounded-[28px] p-5 sm:p-8 shadow-sm text-left">
                
                {/* ── TAB 1: DEPARTMENTAL PACING TRACKER ── */}
                {activeTab === 'pacing' && (
                    <div className="space-y-6 max-w-3xl mx-auto">
                        <div className="flex flex-col sm:flex-row justify-between sm:items-center gap-3 border-b border-slate-200 pb-4">
                            <div>
                                <span className="text-[10px] font-bold uppercase tracking-wider text-cyan-700 bg-cyan-50 px-2.5 py-0.5 rounded-full">
                                    ACADEMIC HEADQUARTERS VIEW
                                </span>
                                <h4 className="text-xl font-bold text-slate-900 mt-1">
                                    {current.title} · {current.totalLearners} Active Learners
                                </h4>
                            </div>

                            {/* Cohort Switcher */}
                            <div className="flex gap-1.5 p-1 bg-slate-100 rounded-xl">
                                <button
                                    type="button"
                                    onClick={() => { setSelectedCohort('gr10'); setDispatchedAlert(false); }}
                                    className={`px-3 py-1 rounded-lg text-xs font-bold transition ${
                                        selectedCohort === 'gr10' ? 'bg-white text-[#13519C] shadow-xs' : 'text-slate-600'
                                    }`}
                                >
                                    Grade 10
                                </button>
                                <button
                                    type="button"
                                    onClick={() => { setSelectedCohort('gr11'); setDispatchedAlert(false); }}
                                    className={`px-3 py-1 rounded-lg text-xs font-bold transition ${
                                        selectedCohort === 'gr11' ? 'bg-white text-[#13519C] shadow-xs' : 'text-slate-600'
                                    }`}
                                >
                                    Grade 11
                                </button>
                            </div>
                        </div>

                        {/* Overall Department Progress Gauge */}
                        <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-4">
                            <div>
                                <span className="text-xs font-bold text-slate-500 uppercase tracking-wider">
                                    Term 2 Syllabus Completion Status
                                </span>
                                <h5 className="text-lg font-bold text-slate-900 mt-0.5">
                                    {current.overallPacing}% of prescribed term syllabus completed
                                </h5>
                                <p className="text-xs text-slate-600">
                                    Based on continuous question attempts and homework submissions across all classes.
                                </p>
                            </div>
                            <div className="flex items-center gap-2">
                                <span className="text-2xl font-extrabold text-[#13519C]">{current.overallPacing}%</span>
                                <span className="text-[11px] font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full">
                                    14 Days to Exams
                                </span>
                            </div>
                        </div>

                        {/* Class Roster Cards */}
                        <div className="grid sm:grid-cols-2 gap-3">
                            {current.classes.map((cls, idx) => (
                                <div key={idx} className={`p-4 rounded-2xl border ${cls.color} space-y-1.5`}>
                                    <div className="flex justify-between items-center text-xs">
                                        <span className="font-bold text-slate-900">{cls.name}</span>
                                        <span className="font-bold text-[10px] px-2 py-0.5 rounded-full bg-white shadow-xs">
                                            {cls.status}
                                        </span>
                                    </div>
                                    <div className="w-full bg-white/70 h-2 rounded-full overflow-hidden">
                                        <div
                                            className="bg-[#13519C] h-full rounded-full"
                                            style={{ width: `${cls.pacing}%` }}
                                        />
                                    </div>
                                    <div className="flex justify-between text-[10px] text-slate-500">
                                        <span>{cls.enrolled} Learners</span>
                                        <span className="font-bold text-slate-700">{cls.pacing}% Covered</span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                )}

                {/* ── TAB 2: CROSS-GRADE PROCEDURE ANALYTICS ── */}
                {activeTab === 'intervention' && (
                    <div className="space-y-6 max-w-3xl mx-auto">
                        <div className="border-b border-slate-200 pb-3 flex flex-col sm:flex-row justify-between sm:items-center gap-2">
                            <div>
                                <span className="text-[10px] font-bold uppercase tracking-wider text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded-full">
                                    CROSS-GRADE COHORT AUTOPSY
                                </span>
                                <h4 className="text-xl font-bold text-slate-900 mt-1">
                                    Systemic Procedural Bottleneck Detection
                                </h4>
                            </div>
                            <span className="text-xs font-bold text-slate-600 bg-slate-100 px-3 py-1 rounded-full">
                                270 Enrolled Learners Audited
                            </span>
                        </div>

                        <p className="text-xs text-slate-600 leading-relaxed">
                            Fundile’s deterministic engine aggregates error taxonomy tags across homework, quizzes, and class assessments to identify where entire grades stumble on the same cognitive rule.
                        </p>

                        {/* Top Systemic Flaw Cards */}
                        <div className="space-y-3">
                            <div className="p-4 rounded-2xl border border-red-200 bg-red-50/60 space-y-3">
                                <div className="flex items-start justify-between gap-3">
                                    <div className="flex items-start gap-2.5">
                                        <AlertTriangle className="h-5 w-5 text-red-600 shrink-0 mt-0.5" />
                                        <div>
                                            <div className="flex items-center gap-2">
                                                <span className="text-xs font-bold text-red-900">Grade 10 Accounting</span>
                                                <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-red-100 text-red-800">52 Learners Affected (71% of cohort)</span>
                                            </div>
                                            <p className="text-sm font-bold text-slate-900 mt-0.5">
                                                Procedural Flaw: <code className="text-xs bg-white px-1.5 py-0.5 rounded border border-red-200 font-mono text-red-700">net_vs_gross_confusion</code>
                                            </p>
                                            <p className="text-xs text-slate-600 mt-1">
                                                Learners consistently multiply the gross Bank receipt by 15/100 instead of 15/115 when extracting VAT from inclusive cash slip totals. Total lost marks: <strong>312 marks across Grade 10</strong>.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                                <div className="pt-1 flex items-center justify-between">
                                    <span className="text-[11px] text-slate-500">Affects Grade 10A, 10B, and 10D</span>
                                    {!dispatchedAlert ? (
                                        <button
                                            type="button"
                                            onClick={() => setDispatchedAlert(true)}
                                            className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-[#13519C] text-white text-xs font-bold shadow-sm hover:bg-[#0f3e77] transition cursor-pointer"
                                        >
                                            <Send className="h-3.5 w-3.5" />
                                            <span>Dispatch 15-Min VAT Prerequisite Drill (52 Learners)</span>
                                        </button>
                                    ) : (
                                        <div className="px-3 py-1.5 bg-emerald-600 text-white rounded-xl text-xs font-bold flex items-center gap-2">
                                            <CheckCircle2 className="h-4 w-4 shrink-0" />
                                            <span>Dispatched to 52 learners across 3 classes!</span>
                                        </div>
                                    )}
                                </div>
                            </div>

                            <div className="p-4 rounded-2xl border border-amber-200 bg-amber-50/60 space-y-2">
                                <div className="flex items-start justify-between gap-3">
                                    <div className="flex items-start gap-2.5">
                                        <AlertTriangle className="h-5 w-5 text-amber-600 shrink-0 mt-0.5" />
                                        <div>
                                            <div className="flex items-center gap-2">
                                                <span className="text-xs font-bold text-amber-900">Grade 11 Mathematics</span>
                                                <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-800">41 Learners Affected (64% of cohort)</span>
                                            </div>
                                            <p className="text-sm font-bold text-slate-900 mt-0.5">
                                                Procedural Flaw: <code className="text-xs bg-white px-1.5 py-0.5 rounded border border-amber-200 font-mono text-amber-700">reciprocal_trig_confusion</code>
                                            </p>
                                            <p className="text-xs text-slate-600 mt-1">
                                                Confusing inverse functions (arcsin) with reciprocal functions (1/sin θ = cosec θ) when solving for reduction formulas in Quadrant II.
                                            </p>
                                        </div>
                                    </div>
                                    <span className="text-xs font-bold text-amber-800 bg-white px-2 py-1 rounded-lg border border-amber-200">
                                        164 Marks Lost
                                    </span>
                                </div>
                            </div>

                            <div className="p-4 rounded-2xl border border-slate-200 bg-slate-50 space-y-2">
                                <div className="flex items-start justify-between gap-3">
                                    <div className="flex items-start gap-2.5">
                                        <CheckCircle2 className="h-5 w-5 text-slate-500 shrink-0 mt-0.5" />
                                        <div>
                                            <div className="flex items-center gap-2">
                                                <span className="text-xs font-bold text-slate-900">Grade 8 EMS</span>
                                                <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-slate-200 text-slate-700">38 Learners Resolved</span>
                                            </div>
                                            <p className="text-sm font-bold text-slate-900 mt-0.5">
                                                Procedural Flaw: <code className="text-xs bg-white px-1.5 py-0.5 rounded border border-slate-200 font-mono text-slate-700">debit_credit_inversion</code>
                                            </p>
                                            <p className="text-xs text-slate-600 mt-1">
                                                Posting bank payments as debits rather than credits in the General Ledger. Remediated via atomic 10-question T-account drill.
                                            </p>
                                        </div>
                                    </div>
                                    <span className="text-xs font-bold text-emerald-700 bg-emerald-50 px-2 py-1 rounded-lg border border-emerald-200">
                                        Mastery: 92%
                                    </span>
                                </div>
                            </div>
                        </div>

                        <div className="p-4 bg-slate-50 border border-slate-200 rounded-2xl text-xs text-slate-600">
                            <strong>Why HODs &amp; Principals love this:</strong> Instead of vague remarks like <em>"the learners are struggling with Accounting"</em>, Fundile pinpoints the exact cognitive step where 52 students failed. You can prescribe remedial intervention in 1 click before term exams.
                        </div>
                    </div>
                )}

                {/* ── TAB 3: SCHOOL ADMIN DASHBOARD ── */}
                {activeTab === 'school_admin' && (
                    <div className="space-y-6 max-w-3xl mx-auto">
                        <div className="border-b border-slate-200 pb-3 flex flex-col sm:flex-row justify-between sm:items-center gap-2">
                            <div>
                                <span className="text-[10px] font-bold uppercase tracking-wider text-cyan-700 bg-cyan-50 px-2.5 py-0.5 rounded-full">
                                    INSTITUTIONAL MANAGEMENT
                                </span>
                                <h4 className="text-xl font-bold text-slate-900 mt-1">
                                    School Administration &amp; Curriculum Governance
                                </h4>
                            </div>
                            <span className="text-xs font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full">
                                Academic Year 2026 · Active
                            </span>
                        </div>

                        {/* Top KPI Grid */}
                        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl">
                                <span className="text-[10px] font-bold text-slate-500 uppercase">Enrolled Learners</span>
                                <p className="text-2xl font-extrabold text-[#13519C] mt-0.5">270</p>
                                <span className="text-[10px] text-emerald-600 font-semibold">Grades 7–12</span>
                            </div>
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl">
                                <span className="text-[10px] font-bold text-slate-500 uppercase">Syllabus Pacing</span>
                                <p className="text-2xl font-extrabold text-emerald-600 mt-0.5">91%</p>
                                <span className="text-[10px] text-slate-500 font-semibold">Term 2 Syllabus Target</span>
                            </div>
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl">
                                <span className="text-[10px] font-bold text-slate-500 uppercase">Educators</span>
                                <p className="text-2xl font-extrabold text-slate-900 mt-0.5">14</p>
                                <span className="text-[10px] text-slate-500 font-semibold">Across 4 Depts</span>
                            </div>
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl">
                                <span className="text-[10px] font-bold text-slate-500 uppercase">Weekly Attempts</span>
                                <p className="text-2xl font-extrabold text-amber-600 mt-0.5">1 840</p>
                                <span className="text-[10px] text-emerald-600 font-semibold">↑ 18% vs last week</span>
                            </div>
                        </div>

                        {/* Departmental Health */}
                        <div>
                            <span className="text-xs font-bold text-slate-700 uppercase tracking-wider block mb-2">
                                Department Syllabus Health
                            </span>
                            <div className="space-y-2 text-xs">
                                <div className="p-3 bg-white border border-slate-200 rounded-xl flex items-center justify-between gap-3">
                                    <div>
                                        <span className="font-bold text-slate-900">Commercial Dept (Accounting &amp; EMS)</span>
                                        <p className="text-[11px] text-slate-500">4 Educators · 142 Active Learners</p>
                                    </div>
                                    <div className="flex items-center gap-3">
                                        <span className="font-mono font-bold text-slate-700">92% Pacing</span>
                                        <span className="text-[10px] font-bold px-2 py-0.5 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-full">On Schedule</span>
                                    </div>
                                </div>
                                <div className="p-3 bg-white border border-slate-200 rounded-xl flex items-center justify-between gap-3">
                                    <div>
                                        <span className="font-bold text-slate-900">STEM Dept (Mathematics &amp; Sciences)</span>
                                        <p className="text-[11px] text-slate-500">6 Educators · 128 Active Learners</p>
                                    </div>
                                    <div className="flex items-center gap-3">
                                        <span className="font-mono font-bold text-slate-700">89% Pacing</span>
                                        <span className="text-[10px] font-bold px-2 py-0.5 bg-amber-50 text-amber-700 border border-amber-200 rounded-full">Trig Review Active</span>
                                    </div>
                                </div>
                                <div className="p-3 bg-white border border-slate-200 rounded-xl flex items-center justify-between gap-3">
                                    <div>
                                        <span className="font-bold text-slate-900">Humanities &amp; Business Studies</span>
                                        <p className="text-[11px] text-slate-500">4 Educators · 110 Active Learners</p>
                                    </div>
                                    <div className="flex items-center gap-3">
                                        <span className="font-mono font-bold text-slate-700">95% Pacing</span>
                                        <span className="text-[10px] font-bold px-2 py-0.5 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-full">Ahead of Schedule</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        {/* Active Class Roster & Join Codes */}
                        <div>
                            <div className="flex justify-between items-center mb-2">
                                <span className="text-xs font-bold text-slate-700 uppercase tracking-wider">
                                    Active Classes &amp; Student Join Codes
                                </span>
                                <span className="text-[11px] text-slate-500">Self-serve zero-admin enrollment</span>
                            </div>
                            <div className="border border-slate-200 rounded-xl overflow-hidden text-xs">
                                <table className="w-full text-left">
                                    <thead className="bg-slate-50 border-b border-slate-200 text-slate-600 font-bold">
                                        <tr>
                                            <th className="p-2.5">Class &amp; Educator</th>
                                            <th className="p-2.5">Join Code</th>
                                            <th className="p-2.5">Enrolled</th>
                                            <th className="p-2.5">Activity</th>
                                        </tr>
                                    </thead>
                                    <tbody className="divide-y divide-slate-100">
                                        <tr>
                                            <td className="p-2.5 font-semibold text-slate-900">Grade 10A Accounting (Mrs. Khumalo)</td>
                                            <td className="p-2.5"><code className="bg-slate-100 px-2 py-0.5 rounded font-mono font-bold text-[#13519C]">ACC-10A</code></td>
                                            <td className="p-2.5 text-slate-600">34 Learners</td>
                                            <td className="p-2.5"><span className="text-emerald-700 font-bold">94% Active</span></td>
                                        </tr>
                                        <tr>
                                            <td className="p-2.5 font-semibold text-slate-900">Grade 11A Mathematics (Dr. Pillay)</td>
                                            <td className="p-2.5"><code className="bg-slate-100 px-2 py-0.5 rounded font-mono font-bold text-[#13519C]">MTH-11A</code></td>
                                            <td className="p-2.5 text-slate-600">32 Learners</td>
                                            <td className="p-2.5"><span className="text-emerald-700 font-bold">96% Active</span></td>
                                        </tr>
                                        <tr>
                                            <td className="p-2.5 font-semibold text-slate-900">Grade 10B Accounting (Mr. Dlamini)</td>
                                            <td className="p-2.5"><code className="bg-slate-100 px-2 py-0.5 rounded font-mono font-bold text-[#13519C]">ACC-10B</code></td>
                                            <td className="p-2.5 text-slate-600">36 Learners</td>
                                            <td className="p-2.5"><span className="text-amber-700 font-bold">78% Active</span></td>
                                        </tr>
                                        <tr>
                                            <td className="p-2.5 font-semibold text-slate-900">Grade 8 EMS (Mrs. Molefe)</td>
                                            <td className="p-2.5"><code className="bg-slate-100 px-2 py-0.5 rounded font-mono font-bold text-[#13519C]">EMS-8C</code></td>
                                            <td className="p-2.5 text-slate-600">35 Learners</td>
                                            <td className="p-2.5"><span className="text-emerald-700 font-bold">91% Active</span></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        {/* Export bar */}
                        <div className="flex flex-wrap items-center justify-between gap-3 p-3.5 bg-slate-50 border border-slate-200 rounded-xl text-xs">
                            <span className="text-slate-600">Need official department reporting for District moderation?</span>
                            <div className="flex gap-2">
                                <button
                                    type="button"
                                    onClick={() => alert('Downloading official Department Curriculum Compliance Audit PDF...')}
                                    className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white border border-slate-300 font-bold text-slate-700 hover:bg-slate-100 transition cursor-pointer"
                                >
                                    <Download className="h-3.5 w-3.5" />
                                    <span>Download Curriculum Audit PDF</span>
                                </button>
                            </div>
                        </div>
                    </div>
                )}

                {/* ── TAB 3: SGB PROCUREMENT & QUOTATION ── */}
                {activeTab === 'sgb' && (
                    <div className="space-y-6 max-w-3xl mx-auto">
                        <div className="border-b border-cyan-200 pb-3 flex flex-col sm:flex-row justify-between sm:items-center gap-2">
                            <div>
                                <span className="text-[10px] font-bold uppercase tracking-wider text-cyan-700 bg-cyan-50 px-2.5 py-0.5 rounded-full">
                                    INSTITUTIONAL PROCUREMENT &amp; SGB INVOICING
                                </span>
                                <h4 className="text-xl font-bold text-slate-900 mt-1">
                                    For pricing, schools should contact info@fundile.com
                                </h4>
                            </div>
                            <span className="text-xs font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full">
                                SGB Tax Invoicing
                            </span>
                        </div>

                        {/* Quotation Sample Card */}
                        <div className="p-5 rounded-2xl border border-slate-200 bg-slate-50 space-y-4">
                            <div className="flex justify-between items-start text-xs border-b border-slate-200 pb-3">
                                <div>
                                    <span className="font-bold text-slate-900 block">INSTITUTIONAL VOLUME PACKAGE</span>
                                    <span className="text-slate-500">Tiered pricing calibrated to enrolled learner headcount</span>
                                </div>
                                <span className="font-mono text-cyan-700 font-bold">24-Hr Quotation Turnaround</span>
                            </div>

                            <div className="grid sm:grid-cols-3 gap-3 text-xs">
                                <div className="p-3 bg-white rounded-xl border border-slate-200">
                                    <span className="font-bold text-slate-900 block mb-1">Included for Teachers:</span>
                                    <p className="text-slate-600 text-[11px]">Multi-class Teacher LMS Cockpits, automated printable A4 test papers &amp; full memoranda.</p>
                                </div>
                                <div className="p-3 bg-white rounded-xl border border-slate-200">
                                    <span className="font-bold text-slate-900 block mb-1">Included for HODs:</span>
                                    <p className="text-slate-600 text-[11px]">Departmental syllabus pacing monitors, cohort diagnostic heatmaps, and remedial dispatch.</p>
                                </div>
                                <div className="p-3 bg-white rounded-xl border border-slate-200">
                                    <span className="font-bold text-slate-900 block mb-1">Included for SGBs:</span>
                                    <p className="text-slate-600 text-[11px]">Official SGB tax invoice, standard EFT procurement terms, and dedicated onboarding specialist.</p>
                                </div>
                            </div>

                            {/* Direct Email Callout */}
                            <div className="pt-2 flex flex-col sm:flex-row items-center justify-between gap-4 p-4 rounded-xl bg-cyan-900 text-white">
                                <div>
                                    <span className="text-xs font-bold uppercase tracking-wider text-cyan-300">
                                        Direct Institutional Contact
                                    </span>
                                    <p className="text-sm font-semibold mt-0.5">
                                        Request your school's volume quotation and demo today:
                                    </p>
                                </div>
                                <a
                                    href="mailto:info@fundile.com?subject=Institutional%20Quotation%20%26%20SGB%20Inquiry"
                                    className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-cyan-400 hover:bg-cyan-300 text-slate-950 text-xs font-bold shadow-md transition shrink-0 cursor-pointer"
                                >
                                    <Mail className="h-4 w-4" />
                                    <span>Email info@fundile.com</span>
                                </a>
                            </div>
                        </div>
                    </div>
                )}
            </div>

            {/* Bottom CTA Bar */}
            <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-3">
                <a
                    href="mailto:info@fundile.com?subject=School%20Pilot%20and%20Institutional%20Pricing%20Inquiry"
                    className="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-xl bg-cyan-700 hover:bg-cyan-600 px-8 py-3.5 text-sm sm:text-base font-semibold text-white shadow-md transition cursor-pointer"
                >
                    <Mail className="h-4.5 w-4.5" />
                    Request Institutional Pilot &amp; Quote
                </a>
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
                For pricing, schools should contact <a href="mailto:info@fundile.com" className="font-bold underline text-cyan-700">info@fundile.com</a> · SGB-approved invoicing · Flexible semester or annual billing
            </p>
        </div>
    );
};

export default SchoolSimulation;
