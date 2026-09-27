import React, { useState } from 'react';
import {
  AlertTriangle,
  Sparkles,
  CheckCircle2,
  ArrowRight,
  ShieldAlert,
  PlayCircle,
  HelpCircle,
  RotateCcw,
  Zap,
  X,
  TrendingUp,
} from 'lucide-react';

export default function PostExamTriageModal({
  isOpen = false,
  examTitle = 'Term Assessment Simulation',
  earnedMarks = 31,
  totalMarks = 50,
  missedQuestions = [
    {
      id: 'q2',
      text: 'Cash sales of R2,300 (incl. 15% VAT). Calculate the VAT amount and Net Sales.',
      lostMarks: 8,
      misconceptionTag: 'net_vs_gross_confusion',
      topic: 'Value Added Tax (VAT)',
    },
    {
      id: 'q4',
      text: 'Debtor returned goods originally invoiced at R575 (incl. 15% VAT). Determine credit note entry.',
      lostMarks: 6,
      misconceptionTag: 'net_vs_gross_confusion',
      topic: 'Debtors Allowances',
    },
  ],
  onClose = () => {},
  onRemedialComplete = () => {},
}) {
  const [activeMode, setActiveMode] = useState('autopsy'); // 'autopsy' | 'remedial_step1' | 'remedial_step2' | 'remedial_step3' | 'resolved'
  const [selectedConflictOption, setSelectedConflictOption] = useState(null);
  const [conflictSubmitted, setConflictSubmitted] = useState(false);
  const [verificationAnswers, setVerificationAnswers] = useState({ q1: '', q2: '' });
  const [verificationFeedback, setVerificationFeedback] = useState(null);

  if (!isOpen) return null;

  // Aggregate lost marks by misconception tag
  const misconceptionSummary = missedQuestions.reduce((acc, q) => {
    const tag = q.misconceptionTag || 'general_procedural_error';
    if (!acc[tag]) acc[tag] = { tag, lostMarks: 0, count: 0, topic: q.topic };
    acc[tag].lostMarks += q.lostMarks || 1;
    acc[tag].count += 1;
    return acc;
  }, {});

  const primaryMisconception = Object.values(misconceptionSummary)[0] || {
    tag: 'net_vs_gross_confusion',
    lostMarks: 14,
    topic: 'Value Added Tax',
  };

  const percentage = Math.round((earnedMarks / Math.max(1, totalMarks)) * 100);

  const handleConflictSubmit = () => {
    setConflictSubmitted(true);
  };

  const handleVerifySubmit = () => {
    // Both answers provided
    if (verificationAnswers.q1.trim() && verificationAnswers.q2.trim()) {
      setActiveMode('resolved');
      onRemedialComplete({
        tag: primaryMisconception.tag,
        resolved: true,
        xpAwarded: 50,
      });
    } else {
      setVerificationFeedback('Please attempt both verification calculations.');
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-md p-4 animate-in fade-in duration-200">
      <div className="bg-slate-900 border border-slate-700/80 rounded-3xl max-w-2xl w-full p-6 md:p-8 shadow-2xl text-white relative flex flex-col gap-6 max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-start justify-between border-b border-slate-800 pb-4">
          <div>
            <div className="flex items-center gap-2 text-sky-400 text-xs font-semibold uppercase tracking-wider">
              <Sparkles className="w-4 h-4" />
              <span>Post-Exam Triage Report &amp; Remedial Pipeline</span>
            </div>
            <h2 className="text-xl font-bold text-white mt-1">{examTitle}</h2>
          </div>
          <button onClick={onClose} className="text-slate-400 hover:text-white transition-colors">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* ─── SCREEN 1: AUTOPSY OVERVIEW ─── */}
        {activeMode === 'autopsy' && (
          <div className="space-y-6">
            {/* Score & Standing Banner */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div className="bg-slate-800/60 border border-slate-700/60 rounded-2xl p-4 text-center">
                <div className="text-xs text-slate-400 font-medium">Exam Score</div>
                <div className="text-3xl font-black text-white mt-1">{percentage}%</div>
                <div className="text-[11px] text-slate-400">
                  {earnedMarks} / {totalMarks} marks
                </div>
              </div>

              <div className="bg-rose-950/30 border border-rose-500/40 rounded-2xl p-4 sm:col-span-2 flex items-center gap-4">
                <div className="w-12 h-12 rounded-xl bg-rose-500/20 text-rose-400 flex items-center justify-center shrink-0">
                  <ShieldAlert className="w-6 h-6" />
                </div>
                <div>
                  <div className="text-xs font-bold text-rose-400 uppercase tracking-wide">
                    Root-Cause Diagnostic Bottleneck
                  </div>
                  <div className="text-sm font-semibold text-rose-200 mt-0.5">
                    You lost {primaryMisconception.lostMarks} marks purely due to{' '}
                    <code className="bg-rose-900/60 text-rose-200 px-1.5 py-0.5 rounded text-xs font-mono">
                      {primaryMisconception.tag}
                    </code>
                  </div>
                </div>
              </div>
            </div>

            {/* Diagnostic Breakdown List */}
            <div className="space-y-3">
              <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400">
                Identified Procedural Slips
              </h4>
              {missedQuestions.map((q, idx) => (
                <div
                  key={q.id || idx}
                  className="bg-slate-800/40 border border-slate-700/50 rounded-xl p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3"
                >
                  <div>
                    <div className="text-xs text-amber-400 font-semibold">{q.topic}</div>
                    <div className="text-sm text-slate-200 mt-0.5">{q.text}</div>
                  </div>
                  <div className="text-right shrink-0">
                    <span className="text-rose-400 font-bold text-sm">-{q.lostMarks} marks</span>
                    <div className="text-[10px] text-slate-400 font-mono mt-0.5">
                      {q.misconceptionTag}
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Call to Action */}
            <div className="bg-gradient-to-r from-sky-950/40 to-indigo-950/40 border border-sky-500/30 rounded-2xl p-5 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div>
                <div className="text-sm font-bold text-white flex items-center gap-1.5">
                  <Zap className="w-4 h-4 text-amber-400" />
                  <span>5-Minute Targeted Fix Ready</span>
                </div>
                <div className="text-xs text-slate-300 mt-1">
                  1 Conflict Probe ──► 1 SimuLearn Micro-Replay ──► 2 Verification Drills
                </div>
              </div>

              <button
                onClick={() => setActiveMode('remedial_step1')}
                className="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white font-bold text-sm flex items-center justify-center gap-2 shadow-lg shadow-indigo-500/20 transition-all shrink-0"
              >
                <span>Launch 5-Min Fix Drill</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        )}

        {/* ─── SCREEN 2: STEP 1 - COGNITIVE CONFLICT PROBE ─── */}
        {activeMode === 'remedial_step1' && (
          <div className="space-y-5 animate-in fade-in">
            <div className="flex items-center justify-between text-xs text-sky-400 font-semibold uppercase tracking-wider">
              <span>Step 1 of 3: Cognitive Conflict Probe</span>
              <span>1 Minute</span>
            </div>

            <div className="bg-slate-800/60 border border-slate-700 rounded-2xl p-5 space-y-3">
              <h3 className="text-base font-bold text-white">
                Examine This Mathematical Contradiction:
              </h3>
              <p className="text-sm text-slate-300 leading-relaxed">
                An item is priced at <strong className="text-amber-300">R1,150</strong> including 15%
                VAT.
                <br />
                If you compute VAT as <code className="bg-slate-900 px-1 py-0.5 rounded text-sky-300">15% × R1,150 = R172.50</code>,
                then subtract it to find the Net Price (<code className="bg-slate-900 px-1 py-0.5 rounded text-sky-300">R1,150 - R172.50 = R977.50</code>):
                <br />
                <span className="text-rose-300 font-medium mt-2 block">
                  What happens when you add 15% VAT back onto R977.50?
                </span>
              </p>

              <div className="space-y-2 pt-2">
                {[
                  {
                    id: 'A',
                    text: 'R977.50 + 15% = R1,124.12 (It does NOT equal R1,150! The VAT was overstated because 15% was applied to a base that already contained VAT).',
                    isCorrect: true,
                  },
                  {
                    id: 'B',
                    text: 'It equals R1,150 exactly.',
                    isCorrect: false,
                  },
                ].map((option) => (
                  <button
                    key={option.id}
                    onClick={() => {
                      setSelectedConflictOption(option.id);
                      setConflictSubmitted(false);
                    }}
                    className={`w-full text-left p-3.5 rounded-xl border text-sm transition-all flex items-start gap-3 ${
                      selectedConflictOption === option.id
                        ? 'border-sky-500 bg-sky-500/10 text-white'
                        : 'border-slate-700 bg-slate-900/60 text-slate-300 hover:border-slate-600'
                    }`}
                  >
                    <span className="w-5 h-5 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-xs font-bold shrink-0 mt-0.5">
                      {option.id}
                    </span>
                    <span className="leading-snug">{option.text}</span>
                  </button>
                ))}
              </div>

              {!conflictSubmitted && (
                <button
                  disabled={!selectedConflictOption}
                  onClick={handleConflictSubmit}
                  className="w-full mt-2 py-2.5 rounded-xl bg-sky-600 hover:bg-sky-500 disabled:opacity-50 text-white font-semibold text-sm transition-colors"
                >
                  Verify Realization
                </button>
              )}

              {conflictSubmitted && (
                <div className="bg-emerald-950/40 border border-emerald-500/40 rounded-xl p-4 mt-3">
                  <div className="text-emerald-400 font-bold text-sm flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4" />
                    <span>Schema Conflict Discovered!</span>
                  </div>
                  <p className="text-xs text-slate-300 mt-1 leading-relaxed">
                    Correct! The Gross Price represents <strong>115%</strong>, not 100%. To extract VAT from a gross amount, you must divide by 1.15 or multiply by <code className="bg-slate-900 px-1 text-emerald-300 font-mono">15/115</code>.
                  </p>
                  <button
                    onClick={() => setActiveMode('remedial_step2')}
                    className="mt-3 px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold flex items-center gap-1.5 transition-colors"
                  >
                    <span>Proceed to SimuLearn Micro-Replay</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              )}
            </div>
          </div>
        )}

        {/* ─── SCREEN 3: STEP 2 - SIMULEARN MICRO-REPLAY ─── */}
        {activeMode === 'remedial_step2' && (
          <div className="space-y-5 animate-in fade-in">
            <div className="flex items-center justify-between text-xs text-sky-400 font-semibold uppercase tracking-wider">
              <span>Step 2 of 3: SimuLearn Canonical Rule Replay</span>
              <span>1.5 Minutes (0.1% Data Cost)</span>
            </div>

            <div className="bg-slate-800/60 border border-slate-700 rounded-2xl p-6 text-center space-y-4">
              <div className="w-14 h-14 rounded-2xl bg-indigo-500/20 text-indigo-400 mx-auto flex items-center justify-center border border-indigo-500/30">
                <PlayCircle className="w-7 h-7" />
              </div>

              <h3 className="text-base font-bold text-white">
                The Canonical 100 : 15 : 115 Proportion Triangle
              </h3>

              {/* Visual Proportion Graphic */}
              <div className="grid grid-cols-3 gap-2 max-w-sm mx-auto my-4 text-xs font-mono font-bold">
                <div className="bg-slate-900 p-3 rounded-xl border border-slate-700">
                  <div className="text-slate-400 text-[10px] uppercase">Net Price</div>
                  <div className="text-sky-300 text-lg mt-1">100%</div>
                  <div className="text-[10px] text-slate-500">Base Cost</div>
                </div>
                <div className="bg-slate-900 p-3 rounded-xl border border-slate-700">
                  <div className="text-slate-400 text-[10px] uppercase">VAT (15%)</div>
                  <div className="text-amber-300 text-lg mt-1">15%</div>
                  <div className="text-[10px] text-slate-500">Tax Element</div>
                </div>
                <div className="bg-slate-900 p-3 rounded-xl border border-slate-700">
                  <div className="text-slate-400 text-[10px] uppercase">Gross Price</div>
                  <div className="text-emerald-300 text-lg mt-1">115%</div>
                  <div className="text-[10px] text-slate-500">Customer Pays</div>
                </div>
              </div>

              <div className="bg-slate-900/80 p-4 rounded-xl text-left border border-slate-800 text-xs text-slate-300 space-y-2">
                <div className="flex items-center gap-2 text-white font-semibold">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                  <span>Gold Standard Calculation Rules:</span>
                </div>
                <div>
                  • From Net to VAT: <code className="text-amber-300">Net × 15%</code> (or × 0.15)
                </div>
                <div>
                  • From Gross to Net: <code className="text-sky-300">Gross ÷ 1.15</code> (or × 100/115)
                </div>
                <div>
                  • From Gross to VAT: <code className="text-emerald-300">Gross × 15/115</code>
                </div>
              </div>

              <button
                onClick={() => setActiveMode('remedial_step3')}
                className="w-full sm:w-auto px-6 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm flex items-center justify-center gap-2 mx-auto transition-colors shadow-lg shadow-indigo-600/20"
              >
                <span>Ready for Verification Pair</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        )}

        {/* ─── SCREEN 4: STEP 3 - ISOMORPHIC VERIFICATION PAIR ─── */}
        {activeMode === 'remedial_step3' && (
          <div className="space-y-5 animate-in fade-in">
            <div className="flex items-center justify-between text-xs text-sky-400 font-semibold uppercase tracking-wider">
              <span>Step 3 of 3: Isomorphic Verification Drills</span>
              <span>2.5 Minutes</span>
            </div>

            <div className="space-y-4">
              {/* Question 1 */}
              <div className="bg-slate-800/60 border border-slate-700 rounded-2xl p-4 space-y-2">
                <div className="text-xs font-semibold text-slate-400">Drill 1: Extract VAT from Gross</div>
                <p className="text-sm font-medium text-slate-200">
                  A business purchases equipment for <strong className="text-sky-300">R4,600</strong> (VAT inclusive at 15%). Calculate the exact VAT amount.
                </p>
                <div className="flex items-center gap-2 pt-1">
                  <span className="text-xs text-slate-400 font-bold">R</span>
                  <input
                    type="text"
                    value={verificationAnswers.q1}
                    onChange={(e) =>
                      setVerificationAnswers({ ...verificationAnswers, q1: e.target.value })
                    }
                    placeholder="e.g. 600"
                    className="w-full sm:w-48 bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-sm text-white focus:outline-none focus:border-sky-500 font-mono"
                  />
                  <span className="text-xs text-slate-500 font-mono">(Hint: 4600 × 15/115)</span>
                </div>
              </div>

              {/* Question 2 */}
              <div className="bg-slate-800/60 border border-slate-700 rounded-2xl p-4 space-y-2">
                <div className="text-xs font-semibold text-slate-400">Drill 2: Calculate Net Sales</div>
                <p className="text-sm font-medium text-slate-200">
                  Cash Register Tape shows total sales of <strong className="text-emerald-300">R6,900</strong> (VAT inclusive at 15%). State the Net Sales revenue.
                </p>
                <div className="flex items-center gap-2 pt-1">
                  <span className="text-xs text-slate-400 font-bold">R</span>
                  <input
                    type="text"
                    value={verificationAnswers.q2}
                    onChange={(e) =>
                      setVerificationAnswers({ ...verificationAnswers, q2: e.target.value })
                    }
                    placeholder="e.g. 6000"
                    className="w-full sm:w-48 bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-sm text-white focus:outline-none focus:border-sky-500 font-mono"
                  />
                  <span className="text-xs text-slate-500 font-mono">(Hint: 6900 ÷ 1.15)</span>
                </div>
              </div>

              {verificationFeedback && (
                <div className="text-xs text-rose-400 bg-rose-950/40 p-2 rounded-lg border border-rose-500/30">
                  {verificationFeedback}
                </div>
              )}

              <button
                onClick={handleVerifySubmit}
                className="w-full py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 hover:to-teal-500 text-white font-bold text-sm flex items-center justify-center gap-2 shadow-lg shadow-emerald-500/20 transition-all"
              >
                <CheckCircle2 className="w-4 h-4" />
                <span>Verify &amp; Certify Remediation</span>
              </button>
            </div>
          </div>
        )}

        {/* ─── SCREEN 5: RESOLVED CELEBRATION ─── */}
        {activeMode === 'resolved' && (
          <div className="text-center py-6 space-y-4 animate-in zoom-in-95 duration-200">
            <div className="w-20 h-20 rounded-3xl bg-emerald-500/20 text-emerald-400 mx-auto flex items-center justify-center border border-emerald-500/40 shadow-inner">
              <Sparkles className="w-10 h-10" />
            </div>

            <h3 className="text-2xl font-black text-white tracking-tight">
              Misconception Cleared!
            </h3>
            <p className="text-sm text-slate-300 max-w-md mx-auto leading-relaxed">
              You successfully repaired your understanding of{' '}
              <span className="text-sky-300 font-semibold">{primaryMisconception.tag}</span>. Your
              BKT mastery dial has been re-calibrated.
            </p>

            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-bold">
              <Zap className="w-4 h-4" />
              <span>+50 Ungameable Mastery XP Awarded</span>
            </div>

            <div className="pt-4">
              <button
                onClick={onClose}
                className="px-6 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-semibold text-sm border border-slate-700 transition-colors"
              >
                Return to Dashboard
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
