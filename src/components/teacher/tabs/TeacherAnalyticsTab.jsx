import React, { useState } from 'react';
import {
  AlertCircle, Users, Sparkles, Printer, CheckCircle2,
  TrendingUp, Calendar, ArrowRight, BarChart2, ShieldCheck, Flame
} from 'lucide-react';
import PrintableTestModal from '../PrintableTestModal';

const MOCK_DIAGNOSTICS = [
  {
    id: 'd1',
    topic: 'Value Added Tax (VAT)',
    misconception: 'net_vs_gross_confusion',
    label: 'Confusing 15% Exclusive vs 115% Inclusive Formula',
    affectedStudents: 18,
    totalStudents: 28,
    severity: 'high',
    marksLostAvg: 7.5,
    subject: 'Accounting Gr 10'
  },
  {
    id: 'd2',
    topic: 'Algebraic Expressions & Factoring',
    misconception: 'sign_error_distribution',
    label: 'Sign Error when Distributing Negative Outer Factors',
    affectedStudents: 14,
    totalStudents: 32,
    severity: 'high',
    marksLostAvg: 6.0,
    subject: 'Mathematics Gr 10'
  },
  {
    id: 'd3',
    topic: 'Bank Reconciliation & Double Entry',
    misconception: 'debit_credit_inversion',
    label: 'Inverting Bank Statement vs Bank Account Entries',
    affectedStudents: 12,
    totalStudents: 35,
    severity: 'medium',
    marksLostAvg: 5.5,
    subject: 'EMS Gr 9'
  },
  {
    id: 'd4',
    topic: 'Quadratic Equations & Nature of Roots',
    misconception: 'quadratic_formula_sign',
    label: 'Inverting -b in Quadratic Formula ±√Discriminant',
    affectedStudents: 9,
    totalStudents: 26,
    severity: 'medium',
    marksLostAvg: 4.8,
    subject: 'Mathematics Gr 11'
  },
  {
    id: 'd5',
    topic: 'Vectors & Scalar Quantities',
    misconception: 'vector_direction_omission',
    label: 'Omitting Direction on Vector Resultants [e.g. East or Right]',
    affectedStudents: 11,
    totalStudents: 30,
    severity: 'medium',
    marksLostAvg: 4.0,
    subject: 'Physical Sciences Gr 10'
  }
];

const ATP_PACING_DATA = [
  {
    subject: 'Accounting',
    grade: '10',
    term: 1,
    currentWeek: 8,
    targetWeek: 8,
    status: 'on_track',
    statusLabel: 'On Track (Week 8 of 10)',
    activeTopic: 'Cash Receipts & Payments Journals',
    nextTopic: 'Debtors Ledger & General Ledger Posting',
    completionRate: 80,
  },
  {
    subject: 'Mathematics',
    grade: '10',
    term: 1,
    currentWeek: 8,
    targetWeek: 8,
    status: 'on_track',
    statusLabel: 'On Track (Week 8 of 10)',
    activeTopic: 'Algebraic Expressions & Factoring',
    nextTopic: 'Equations & Inequalities',
    completionRate: 82,
  },
  {
    subject: 'Mathematics',
    grade: '11',
    term: 1,
    currentWeek: 7,
    targetWeek: 8,
    status: 'delayed',
    statusLabel: '1 Week Behind (Week 7 of 10)',
    activeTopic: 'Quadratic Equations & Roots',
    nextTopic: 'Trigonometric Reduction Formulae',
    completionRate: 70,
  },
  {
    subject: 'EMS',
    grade: '9',
    term: 1,
    currentWeek: 9,
    targetWeek: 8,
    status: 'ahead',
    statusLabel: 'Ahead of Schedule (Week 9 of 10)',
    activeTopic: 'Cash Receipts Journal (CRJ)',
    nextTopic: 'The Circular Flow Model of Economy',
    completionRate: 90,
  },
  {
    subject: 'Physical Sciences',
    grade: '10',
    term: 1,
    currentWeek: 8,
    targetWeek: 8,
    status: 'on_track',
    statusLabel: 'On Track (Week 8 of 10)',
    activeTopic: 'Transverse Waves & Pulses',
    nextTopic: 'Electromagnetic Radiation',
    completionRate: 78,
  }
];

export default function TeacherAnalyticsTab({
  classes = [],
  onDispatchDrill = () => {},
}) {
  const [diagnostics] = useState(MOCK_DIAGNOSTICS);
  const [assignedMap, setAssignedMap] = useState({});
  const [isPrintModalOpen, setIsPrintModalOpen] = useState(false);

  const handleAssign = (item) => {
    setAssignedMap(prev => ({ ...prev, [item.id]: true }));
    onDispatchDrill(item.misconception, item.subject, item.affectedStudents);
  };

  const remedialQuestions = diagnostics.map((d) => ({
    question_text: `Targeted Diagnostic Item: Solve the key conceptual barrier in ${d.topic}. Specifically address: ${d.label}.`,
    marks: Math.round(d.marksLostAvg) || 5,
    marking_scheme: [
      { point: `Correct conceptual rule application for ${d.topic}`, marks: 2, editable: true },
      { point: `Accurate calculation without ${d.misconception}`, marks: Math.max(Math.round(d.marksLostAvg) - 2, 2), editable: true }
    ],
    solution: `Standard step-by-step resolution addressing ${d.label} with full consequential method marks.`
  }));

  // Calculate cohort performance distribution
  const allStudents = classes.flatMap(c => c.students || []);
  const levelDistribution = [
    { level: 'Level 7', range: '80–100%', count: allStudents.filter(s => s.score >= 80).length, color: 'bg-emerald-500', label: 'Outstanding' },
    { level: 'Level 6', range: '70–79%', count: allStudents.filter(s => s.score >= 70 && s.score < 80).length, color: 'bg-[#13519C]', label: 'Meritorious' },
    { level: 'Level 5', range: '60–69%', count: allStudents.filter(s => s.score >= 60 && s.score < 70).length, color: 'bg-sky-500', label: 'Substantial' },
    { level: 'Level 4', range: '50–59%', count: allStudents.filter(s => s.score >= 50 && s.score < 60).length, color: 'bg-amber-500', label: 'Adequate' },
    { level: 'Level 1–3', range: '<50%', count: allStudents.filter(s => s.score < 50).length, color: 'bg-rose-500', label: 'Remedial' },
  ];
  const totalCount = allStudents.length || 1;

  return (
    <div className="space-y-8 animate-in fade-in duration-200">
      
      {/* 1. CLASS DIAGNOSTIC WEAKNESS HEATMAP */}
      <section className="bg-white border border-slate-200/90 rounded-2xl p-6 shadow-xs hover:shadow-md transition-all duration-200">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-100 pb-4 mb-5">
          <div>
            <div className="flex items-center gap-2 text-rose-600 text-xs font-bold uppercase tracking-wider">
              <AlertCircle className="w-4 h-4" />
              <span>Class Diagnostic Bottlenecks Heatmap</span>
            </div>
            <h3 
              style={{ fontFamily: "'Afacad', sans-serif" }}
              className="text-xl font-bold text-slate-900 mt-1 tracking-tight"
            >
              Top Conceptual Obstacles Across Classes
            </h3>
            <p className="text-xs text-slate-500">Aggregated across recent student submissions &amp; formative diagnostic baseline checkpoints</p>
          </div>
          <div className="flex items-center gap-2 shrink-0">
            <button
              onClick={() => setIsPrintModalOpen(true)}
              className="flex items-center gap-1.5 px-3.5 py-2 bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 rounded-xl text-xs font-semibold transition-all shadow-xs cursor-pointer"
            >
              <Printer className="w-3.5 h-3.5 text-[#13519C]" />
              <span>Print Remedial Test &amp; Memo</span>
            </button>
            <div className="flex items-center gap-1.5 px-3 py-2 bg-blue-50 border border-blue-200/80 rounded-xl text-xs font-semibold text-[#13519C] font-mono">
              <Users className="w-3.5 h-3.5" />
              <span>{allStudents.length || 151} Learners Tracked</span>
            </div>
          </div>
        </div>

        {/* Diagnostic Items Table */}
        <div className="overflow-x-auto rounded-xl border border-slate-200/90">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 text-slate-500 uppercase tracking-wider text-[10px] border-b border-slate-200 font-semibold font-sans">
              <tr>
                <th className="py-3 px-4">Subject &amp; CAPS Topic</th>
                <th className="py-3 px-4">Specific Misconception Obstacle</th>
                <th className="py-3 px-4">Affected Learners</th>
                <th className="py-3 px-4">Avg Marks Lost</th>
                <th className="py-3 px-4">Severity</th>
                <th className="py-3 px-4 text-right">Targeted Remediation</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 bg-white">
              {diagnostics.map((diag) => (
                <tr key={diag.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="py-3.5 px-4">
                    <span className="text-[10px] font-bold text-[#13519C] bg-blue-50 border border-blue-200/70 px-2 py-0.5 rounded-md inline-block mb-1">
                      {diag.subject}
                    </span>
                    <div className="font-semibold text-slate-900">{diag.topic}</div>
                  </td>
                  <td className="py-3.5 px-4">
                    <div className="text-slate-800 font-medium">{diag.label}</div>
                    <div className="text-[11px] text-slate-400 font-mono mt-0.5">{diag.misconception}</div>
                  </td>
                  <td className="py-3.5 px-4 font-mono">
                    <span className="font-bold text-slate-900">{diag.affectedStudents}</span>
                    <span className="text-slate-400"> / {diag.totalStudents} ({Math.round(diag.affectedStudents / diag.totalStudents * 100)}%)</span>
                  </td>
                  <td className="py-3.5 px-4 font-mono font-bold text-rose-600">
                    -{diag.marksLostAvg} Marks
                  </td>
                  <td className="py-3.5 px-4">
                    <span className={`inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider ${
                      diag.severity === 'high' 
                        ? 'bg-rose-50 text-rose-700 border border-rose-200' 
                        : 'bg-amber-50 text-amber-900 border border-amber-200'
                    }`}>
                      {diag.severity}
                    </span>
                  </td>
                  <td className="py-3.5 px-4 text-right">
                    <button
                      onClick={() => handleAssign(diag)}
                      disabled={assignedMap[diag.id]}
                      className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition cursor-pointer ${
                        assignedMap[diag.id]
                          ? 'bg-emerald-50 text-emerald-700 border border-emerald-200 cursor-default'
                          : 'bg-[#13519C] hover:bg-[#0f3e77] text-white shadow-2xs'
                      }`}
                    >
                      {assignedMap[diag.id] ? (
                        <>
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          <span>Drill Dispatched</span>
                        </>
                      ) : (
                        <>
                          <Sparkles className="w-3.5 h-3.5" />
                          <span>Assign 5-Min Fix</span>
                        </>
                      )}
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* 2. CAPS ANNUAL TEACHING PLAN (ATP) SUBJECT PACING & PERFORMANCE CURVE */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        {/* ATP Pacing Guide (2 cols) */}
        <section className="lg:col-span-2 bg-white border border-slate-200/90 rounded-2xl p-6 shadow-xs hover:shadow-md transition-all duration-200">
          <div className="flex items-center justify-between mb-4 border-b border-slate-100 pb-3">
            <div className="flex items-center gap-2">
              <Calendar className="w-5 h-5 text-[#13519C]" />
              <div>
                <h3 
                  style={{ fontFamily: "'Afacad', sans-serif" }}
                  className="text-lg font-bold text-slate-900 tracking-tight"
                >
                  Annual Teaching Plan (ATP) Curriculum Pacing
                </h3>
                <p className="text-xs text-slate-500">Term 1 syllabus milestones vs scheduled Department of Basic Education weeks</p>
              </div>
            </div>
            <span className="text-xs font-semibold text-emerald-700 bg-emerald-50 border border-emerald-200 px-2.5 py-1 rounded-full flex items-center gap-1">
              <ShieldCheck className="w-3.5 h-3.5" />
              <span>Term 1 Week 8</span>
            </span>
          </div>

          <div className="space-y-4">
            {ATP_PACING_DATA.map((atp, idx) => (
              <div key={idx} className="p-3.5 rounded-xl border border-slate-200/80 bg-slate-50/50 hover:bg-slate-50 transition-colors">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1 mb-2">
                  <div className="flex items-center gap-2">
                    <span className="font-bold text-slate-900 text-xs">{atp.subject} Grade {atp.grade}</span>
                    <span className="text-slate-300">•</span>
                    <span className="text-xs text-slate-600 font-medium">Term {atp.term}</span>
                  </div>
                  <span className={`inline-flex items-center gap-1 text-[11px] font-semibold px-2 py-0.5 rounded-full ${
                    atp.status === 'on_track' ? 'bg-emerald-50 text-emerald-800 border border-emerald-200' :
                    atp.status === 'ahead' ? 'bg-blue-50 text-[#13519C] border border-blue-200' :
                    'bg-amber-50 text-amber-900 border border-amber-200'
                  }`}>
                    {atp.statusLabel}
                  </span>
                </div>

                {/* Progress bar */}
                <div className="w-full bg-slate-200/80 rounded-full h-2 overflow-hidden mb-2">
                  <div 
                    className={`h-full rounded-full transition-all duration-500 ${
                      atp.status === 'delayed' ? 'bg-[#FF9100]' : 'bg-[#13519C]'
                    }`}
                    style={{ width: `${atp.completionRate}%` }}
                  />
                </div>

                <div className="flex flex-wrap items-center justify-between text-[11px] text-slate-500">
                  <div className="flex items-center gap-1">
                    <span className="text-slate-400">Current:</span>
                    <span className="font-semibold text-slate-700">{atp.activeTopic}</span>
                  </div>
                  <div className="flex items-center gap-1">
                    <ArrowRight className="w-3 h-3 text-slate-400" />
                    <span className="text-slate-400">Next:</span>
                    <span className="text-slate-600">{atp.nextTopic}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* CAPS Performance Level Distribution (1 col) */}
        <section className="bg-white border border-slate-200/90 rounded-2xl p-6 shadow-xs hover:shadow-md transition-all duration-200 flex flex-col justify-between">
          <div>
            <div className="flex items-center gap-2 mb-4 border-b border-slate-100 pb-3">
              <BarChart2 className="w-5 h-5 text-[#13519C]" />
              <div>
                <h3 
                  style={{ fontFamily: "'Afacad', sans-serif" }}
                  className="text-lg font-bold text-slate-900 tracking-tight"
                >
                  Grade Distribution
                </h3>
                <p className="text-xs text-slate-500">Official CAPS Achievement Levels (1–7)</p>
              </div>
            </div>

            <div className="space-y-3">
              {levelDistribution.map((lvl) => {
                const pct = Math.round((lvl.count / totalCount) * 100);
                return (
                  <div key={lvl.level} className="space-y-1">
                    <div className="flex justify-between text-xs">
                      <div className="flex items-center gap-1.5">
                        <span className="font-bold text-slate-800">{lvl.level}</span>
                        <span className="text-slate-400 text-[11px]">({lvl.range})</span>
                      </div>
                      <div className="flex items-center gap-2 font-mono">
                        <span className="font-bold text-slate-900">{lvl.count}</span>
                        <span className="text-slate-400 text-[11px]">({pct}%)</span>
                      </div>
                    </div>
                    <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
                      <div 
                        className={`h-full rounded-full transition-all duration-500 ${lvl.color}`}
                        style={{ width: `${Math.max(pct, 4)}%` }}
                      />
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          <div className="mt-6 p-3 bg-blue-50 border border-blue-200/80 rounded-xl text-xs text-[#13519C] flex items-center gap-2">
            <TrendingUp className="w-4 h-4 shrink-0 text-[#13519C]" />
            <span>
              <strong>68% of cohort</strong> currently achieving CAPS Grade 10+ Bachelor Pass benchmark (&gt;50%).
            </span>
          </div>
        </section>

      </div>

      <PrintableTestModal
        isOpen={isPrintModalOpen}
        onClose={() => setIsPrintModalOpen(false)}
        testTitle="Class Diagnostic Remedial Test & Marking Memo"
        subject="Multi-Topic Remedial"
        grade="10"
        term={1}
        durationMins={25}
        questions={remedialQuestions}
      />

    </div>
  );
}
