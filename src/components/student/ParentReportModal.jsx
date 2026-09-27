import React, { useState } from 'react';
import { Printer, Share2, Award, TrendingUp, AlertTriangle, CheckCircle2, X } from 'lucide-react';

const CAPS_LEVELS = [
  { min: 80, level: 7, rating: 'Outstanding Achievement', color: 'text-emerald-400 bg-emerald-950/60 border-emerald-500/40' },
  { min: 70, level: 6, rating: 'Meritorious Achievement', color: 'text-emerald-400 bg-emerald-950/40 border-emerald-500/30' },
  { min: 60, level: 5, rating: 'Substantial Achievement', color: 'text-blue-400 bg-blue-950/40 border-blue-500/30' },
  { min: 50, level: 4, rating: 'Adequate Achievement', color: 'text-amber-400 bg-amber-950/40 border-amber-500/30' },
  { min: 40, level: 3, rating: 'Moderate Achievement', color: 'text-orange-400 bg-orange-950/40 border-orange-500/30' },
  { min: 30, level: 2, rating: 'Elementary Achievement', color: 'text-rose-400 bg-rose-950/40 border-rose-500/30' },
  { min: 0, level: 1, rating: 'Not Achieved', color: 'text-rose-500 bg-rose-950/60 border-rose-600/40' },
];

export default function ParentReportModal({
  isOpen = false,
  onClose,
  studentName = 'Learner',
  grade = '10',
  streakDays = 5,
  totalXP = 1450,
  subjectMastery = {
    'Mathematics': 78,
    'Accounting': 84,
    'Physical Sciences': 65,
    'Life Sciences': 72
  },
  diagnosedMisconceptions = [
    {
      topic: 'Accounting: VAT Calculation',
      label: 'Confusing 15% Exclusive vs 115% Inclusive formula',
      marksLost: 6,
      remedial: '5-minute micro-drill on dividing gross Bank amount by 1.15.'
    },
    {
      topic: 'Mathematics: Quadratic Equations',
      label: 'Distributing negative factors in brackets',
      marksLost: 4,
      remedial: 'Isolate factor pair signs before bracket multiplication.'
    }
  ]
}) {
  if (!isOpen) return null;

  const scores = Object.values(subjectMastery);
  const avgScore = scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 75;
  const capsBand = CAPS_LEVELS.find(l => avgScore >= l.min) || CAPS_LEVELS[3];

  const handlePrint = () => {
    const printWindow = window.open('', '_blank');
    if (!printWindow) {
      alert('Please allow popups to print the academic progress report.');
      return;
    }

    const subjectRowsHtml = Object.entries(subjectMastery).map(([s, score]) => {
      const band = CAPS_LEVELS.find(l => score >= l.min) || CAPS_LEVELS[3];
      return `
        <tr>
          <td style="padding: 8px 10px; border-bottom: 1px solid #e2e8f0; font-weight: 600;">${s}</td>
          <td style="padding: 8px 10px; border-bottom: 1px solid #e2e8f0; text-align: center; font-family: monospace; font-weight: bold;">${score}%</td>
          <td style="padding: 8px 10px; border-bottom: 1px solid #e2e8f0; text-align: center;">Level ${band.level} (${band.rating})</td>
        </tr>
      `;
    }).join('');

    const misconceptionsHtml = diagnosedMisconceptions.map(m => `
      <div style="background: #fff5f5; border-left: 4px solid #f87171; padding: 10px; margin-bottom: 8px;">
        <div style="font-weight: bold; color: #991b1b; font-size: 9.5pt;">${m.topic}: ${m.label} (~${m.marksLost} marks lost)</div>
        <div style="font-size: 8.5pt; color: #4b5563; margin-top: 2px;">Fix: ${m.remedial}</div>
      </div>
    `).join('');

    const docHtml = `
      <!DOCTYPE html>
      <html>
      <head>
        <title>Academic Progress Report - ${studentName}</title>
        <style>
          @page { size: A4; margin: 18mm; }
          body { font-family: -apple-system, sans-serif; color: #1e293b; line-height: 1.5; margin: 0; padding: 0; }
        </style>
      </head>
      <body>
        <div style="border-bottom: 2px solid #0f172a; padding-bottom: 10px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <div style="font-size: 18pt; font-weight: 900; color: #4338ca;">FUNDILE</div>
            <div style="font-size: 8.5pt; color: #64748b;">Adaptive Learning & Cognitive Diagnostic Engine</div>
          </div>
          <div style="text-align: right;">
            <div style="font-weight: bold; font-size: 11pt;">Academic Progress Report</div>
            <div style="font-size: 8.5pt; color: #64748b;">Learner: ${studentName} • Grade ${grade}</div>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; margin-bottom: 20px; text-align: center;">
          <div><div style="font-size: 8pt; color: #64748b;">Average Score</div><div style="font-size: 14pt; font-weight: bold;">${avgScore}%</div></div>
          <div><div style="font-size: 8pt; color: #64748b;">National Standing</div><div style="font-size: 14pt; font-weight: bold; color: #16a34a;">Level ${capsBand.level}</div></div>
          <div><div style="font-size: 8pt; color: #64748b;">Ungameable XP</div><div style="font-size: 14pt; font-weight: bold; color: #4338ca;">${totalXP.toLocaleString()}</div></div>
          <div><div style="font-size: 8pt; color: #64748b;">Consistency</div><div style="font-size: 14pt; font-weight: bold; color: #d97706;">🔥 ${streakDays}d Streak</div></div>
        </div>

        <div style="font-weight: bold; font-size: 11pt; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; margin-bottom: 10px;">1. Subject Mastery Ratings</div>
        <table style="width: 100%; border-collapse: collapse; font-size: 9pt; margin-bottom: 20px;">
          <thead>
            <tr style="background: #f1f5f9;">
              <th style="padding: 6px 10px; text-align: left;">Subject</th>
              <th style="padding: 6px 10px; text-align: center; width: 80px;">Score</th>
              <th style="padding: 6px 10px; text-align: center; width: 180px;">Official Scale</th>
            </tr>
          </thead>
          <tbody>${subjectRowsHtml}</tbody>
        </table>

        <div style="font-weight: bold; font-size: 11pt; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; margin-bottom: 10px;">2. Conceptual Bottlenecks & Fixes</div>
        ${misconceptionsHtml}

        <div style="margin-top: 24px; border-top: 1px solid #e2e8f0; padding-top: 10px; font-size: 8pt; color: #94a3b8; display: flex; justify-content: space-between;">
          <span>Verified by Fundile Diagnostic Engine • Strictly Aligned with National Curriculum Standards</span>
          <span>Confidential Parent Report</span>
        </div>
      </body>
      </html>
    `;

    printWindow.document.open();
    printWindow.document.write(docHtml);
    printWindow.document.close();
    printWindow.onload = () => printWindow.print();
  };

  const handleWhatsAppShare = () => {
    const text = `🎓 *Fundile Academic Progress Report*\n*Learner:* ${studentName} (Grade ${grade})\n*Standing:* National Level ${capsBand.level} (${avgScore}% overall)\n*Study Streak:* 🔥 ${streakDays} Days\n*Academic XP:* ${totalXP.toLocaleString()} XP\n\n_Aligned with South African National Curriculum Standards_`;
    window.open(`https://wa.me/?text=${encodeURIComponent(text)}`, '_blank');
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-950/85 backdrop-blur-md animate-fade-in text-slate-100">
      <div className="bg-slate-900 border border-slate-800 rounded-3xl shadow-2xl max-w-2xl w-full flex flex-col max-h-[90vh] overflow-hidden">
        {/* Header */}
        <div className="p-5 border-b border-slate-800 bg-slate-950/60 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-indigo-500/20 text-indigo-300 flex items-center justify-center text-xl border border-indigo-500/30">
              📊
            </div>
            <div>
              <h3 className="text-base font-bold text-slate-100">Academic Diagnostic Progress Report</h3>
              <p className="text-xs text-slate-400">
                Learner: {studentName} • Grade {grade} • Parent & Guardian Digest
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={handlePrint}
              className="px-3.5 py-1.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-semibold text-xs flex items-center gap-1.5 transition-colors shadow-md shadow-blue-950/40"
            >
              <Printer className="w-3.5 h-3.5" />
              <span>Print PDF</span>
            </button>
            <button
              onClick={handleWhatsAppShare}
              className="px-3.5 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs flex items-center gap-1.5 transition-colors shadow-md shadow-emerald-950/40"
            >
              <Share2 className="w-3.5 h-3.5" />
              <span>WhatsApp</span>
            </button>
            <button
              onClick={onClose}
              className="p-1.5 rounded-lg text-slate-400 hover:text-slate-100 hover:bg-slate-800 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Report Content */}
        <div className="p-6 overflow-y-auto space-y-5 flex-1">
          {/* Hero Metrics */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div className="p-3.5 rounded-2xl bg-slate-950/70 border border-slate-800 text-center">
              <div className="text-[11px] text-slate-400 uppercase font-semibold">Overall Mastery</div>
              <div className="text-xl font-bold font-mono text-indigo-300 mt-1">{avgScore}%</div>
            </div>
            <div className="p-3.5 rounded-2xl bg-slate-950/70 border border-slate-800 text-center">
              <div className="text-[11px] text-slate-400 uppercase font-semibold">National Standing</div>
              <div className="text-xl font-bold font-mono text-emerald-400 mt-1">Level {capsBand.level}</div>
            </div>
            <div className="p-3.5 rounded-2xl bg-slate-950/70 border border-slate-800 text-center">
              <div className="text-[11px] text-slate-400 uppercase font-semibold">Ungameable XP</div>
              <div className="text-xl font-bold font-mono text-purple-300 mt-1">{totalXP.toLocaleString()}</div>
            </div>
            <div className="p-3.5 rounded-2xl bg-slate-950/70 border border-slate-800 text-center">
              <div className="text-[11px] text-slate-400 uppercase font-semibold">Study Streak</div>
              <div className="text-xl font-bold font-mono text-amber-400 mt-1">🔥 {streakDays}d</div>
            </div>
          </div>

          {/* Subject Mastery Table */}
          <div className="space-y-2">
            <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
              1. Subject Performance Breakdown
            </h4>
            <div className="rounded-2xl border border-slate-800 overflow-hidden bg-slate-950/50">
              <table className="w-full text-xs text-left">
                <thead className="bg-slate-900 text-slate-400 border-b border-slate-800 text-[11px]">
                  <tr>
                    <th className="p-3 font-semibold">Subject</th>
                    <th className="p-3 font-semibold text-center w-24">Mastery</th>
                    <th className="p-3 font-semibold text-center">Official Achievement Scale</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60">
                  {Object.entries(subjectMastery).map(([subj, score]) => {
                    const band = CAPS_LEVELS.find(l => score >= l.min) || CAPS_LEVELS[3];
                    return (
                      <tr key={subj}>
                        <td className="p-3 font-medium text-slate-200">{subj}</td>
                        <td className="p-3 font-mono font-bold text-center text-slate-100">{score}%</td>
                        <td className="p-3 text-center">
                          <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-bold border ${band.color}`}>
                            Level {band.level} • {band.rating}
                          </span>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>

          {/* Diagnosed Bottlenecks */}
          <div className="space-y-2">
            <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
              2. Diagnosed Conceptual Bottlenecks & Remedials
            </h4>
            <div className="space-y-2">
              {diagnosedMisconceptions.map((m, i) => (
                <div key={i} className="p-3.5 rounded-2xl bg-rose-950/20 border border-rose-500/30 text-xs space-y-1">
                  <div className="flex items-center justify-between text-rose-300 font-semibold">
                    <span>{m.topic}</span>
                    <span>~{m.marksLost} Marks Lost</span>
                  </div>
                  <div className="text-slate-300">{m.label}</div>
                  <div className="text-emerald-400 font-medium pt-1">
                    <strong>Recommended Fix:</strong> {m.remedial}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-slate-800 bg-slate-950/70 flex items-center justify-between text-xs text-slate-400">
          <span>Official South African 7-Level Achievement Scale. Verified by Fundile.</span>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium transition-colors"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
}
