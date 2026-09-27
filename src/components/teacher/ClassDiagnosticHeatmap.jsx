import React, { useState } from 'react';
import { AlertCircle, TrendingDown, Users, Sparkles, ArrowUpRight, CheckCircle2, Printer } from 'lucide-react';
import PrintableTestModal from './PrintableTestModal';

const MOCK_CLASS_DIAGNOSTICS = [
  {
    id: 'd1',
    topic: 'Value Added Tax (VAT)',
    misconception: 'net_vs_gross_confusion',
    label: 'Confusing 15% Exclusive vs 115% Inclusive Formula',
    affectedStudents: 18,
    totalStudents: 28,
    severity: 'high',
    marksLostAvg: 7.5,
  },
  {
    id: 'd2',
    topic: 'Bank Reconciliation',
    misconception: 'debit_credit_inversion',
    label: 'Inverting Bank Statement vs Bank Account Entries',
    affectedStudents: 14,
    totalStudents: 28,
    severity: 'medium',
    marksLostAvg: 6.0,
  },
  {
    id: 'd3',
    topic: 'Quadratic Factorisation',
    misconception: 'sign_error_distribution',
    label: 'Sign Error when Distributing Negative Outer Factors',
    affectedStudents: 11,
    totalStudents: 28,
    severity: 'medium',
    marksLostAvg: 4.2,
  },
];

export default function ClassDiagnosticHeatmap({
  diagnostics = MOCK_CLASS_DIAGNOSTICS,
  onAssignRemedialDrill,
}) {
  const [assignedDrills, setAssignedDrills] = useState({});
  const [isPrintModalOpen, setIsPrintModalOpen] = useState(false);

  const handleAssign = (item) => {
    setAssignedDrills((prev) => ({ ...prev, [item.id]: true }));
    if (onAssignRemedialDrill) {
      onAssignRemedialDrill(item);
    }
  };

  const remedialQuestions = diagnostics.map((d, i) => ({
    question_text: `Targeted Diagnostic Item: Solve the key conceptual barrier in ${d.topic}. Specifically address: ${d.label}.`,
    marks: Math.round(d.marksLostAvg) || 5,
    marking_scheme: [
      { point: `Correct conceptual rule application for ${d.topic}`, marks: 2 },
      { point: `Accurate calculation without ${d.misconception}`, marks: Math.round(d.marksLostAvg) - 2 || 3 }
    ],
    solution: `Standard step-by-step resolution addressing ${d.label} with full consequential method marks.`
  }));

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-xl text-white flex flex-col gap-4">
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

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-4">
        <div>
          <div className="flex items-center gap-2 text-rose-400 text-xs font-semibold uppercase tracking-wider">
            <AlertCircle className="w-4 h-4" />
            <span>Class Diagnostic Weakness Heatmap</span>
          </div>
          <h3 className="text-lg font-bold text-slate-100 mt-1">Top Conceptual Bottlenecks</h3>
          <p className="text-xs text-slate-400">Aggregated across recent student submissions & test diagnostics</p>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={() => setIsPrintModalOpen(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 rounded-xl text-xs font-semibold text-white transition-colors shadow-md shadow-indigo-950/40"
          >
            <Printer className="w-3.5 h-3.5" />
            <span>Print Remedial Test & Memo</span>
          </button>
          <div className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-800 rounded-xl text-xs text-slate-300">
            <Users className="w-3.5 h-3.5 text-indigo-400" />
            <span>28 Active Students</span>
          </div>
        </div>
      </div>

      {/* Heatmap Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-3.5">
        {diagnostics.map((diag) => {
          const percentage = Math.round((diag.affectedStudents / diag.totalStudents) * 100);
          const isAssigned = assignedDrills[diag.id];

          return (
            <div
              key={diag.id}
              className={`p-4 rounded-xl border flex flex-col justify-between transition-all ${
                diag.severity === 'high'
                  ? 'bg-rose-950/20 border-rose-500/30'
                  : 'bg-amber-950/20 border-amber-500/30'
              }`}
            >
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-semibold text-slate-300">{diag.topic}</span>
                  <span
                    className={`text-[10px] px-2 py-0.5 rounded-full font-bold uppercase ${
                      diag.severity === 'high'
                        ? 'bg-rose-500/20 text-rose-300 border border-rose-500/40'
                        : 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                    }`}
                  >
                    {percentage}% Affected
                  </span>
                </div>

                <p className="text-sm font-medium text-slate-100">{diag.label}</p>

                <div className="text-xs text-slate-400 flex items-center gap-2 pt-1">
                  <span>Lost ~{diag.marksLostAvg} marks/test</span>
                </div>
              </div>

              <div className="pt-4 mt-2 border-t border-slate-800/80">
                <button
                  onClick={() => handleAssign(diag)}
                  disabled={isAssigned}
                  className={`w-full py-2 px-3 rounded-lg text-xs font-semibold flex items-center justify-center gap-1.5 transition-all ${
                    isAssigned
                      ? 'bg-emerald-950/40 text-emerald-300 border border-emerald-500/30 cursor-default'
                      : 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-600/30'
                  }`}
                >
                  {isAssigned ? (
                    <>
                      <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                      <span>Remedial Drill Dispatched</span>
                    </>
                  ) : (
                    <>
                      <Sparkles className="w-3.5 h-3.5" />
                      <span>Dispatch 5-Min Remedial Drill</span>
                    </>
                  )}
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
