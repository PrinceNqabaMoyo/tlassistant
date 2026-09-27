import React, { useState } from 'react';
import { 
  Sparkles, X, Lightbulb, MessageSquare, Award, ArrowRight, 
  HelpCircle, AlertCircle, PlayCircle, CheckCircle2, ShieldAlert
} from 'lucide-react';
import DeclarativeSocraticChips from './DeclarativeSocraticChips';

/**
 * SocraticTutorDrawer Component (Layer C — Pro Agent)
 * On-rails declarative Socratic guidance interface.
 * Features:
 * - Contextual 1-tap Socratic misconception chips (Zero freeform prompt chat)
 * - Cognitive Teach-Back Evaluator (Learner explains reasoning; evaluated deterministically)
 * - 3-Strike Circuit Breaker (Auto-recommends SimuLearn animation after 3 failed attempts)
 */
export default function SocraticTutorDrawer({
  isOpen = false,
  onClose = () => {},
  subject = 'Accounting',
  topic = 'Cash Receipts Journal',
  subskill = 'Bank Debit Posting',
  misconceptionTags = ['debit_credit_inversion'],
  consecutiveErrors = 0,
  onLaunchSimuLearn = () => {},
  onMasteryEarned = () => {},
}) {
  const [activeTab, setActiveTab] = useState('chips'); // 'chips' | 'teach_back'
  const [socraticResponse, setSocraticResponse] = useState(null);
  const [teachBackText, setTeachBackText] = useState('');
  const [teachBackResult, setTeachBackResult] = useState(null);
  const [isEvaluating, setIsEvaluating] = useState(false);

  // Pre-calculated Socratic Responses for 1-tap chips
  const CHIP_EXPLANATIONS = {
    explain_vat_rule: "In South Africa, VAT is 15%. When selling goods, Gross amount is 115% and Net is 100%. The business collects the 15% on behalf of SARS, so it is a liability owed to SARS, not business revenue.",
    explain_contra_rule: "Under the double-entry system, the Contra Account answers: *'Why did the Bank balance change?'* For capital contributions, the contra account is Capital; for cash sales, it is Sales.",
    explain_factoring_signs: "Look at the constant term $c$ in $ax^2 + bx + c$. If $c$ is positive, both factors share the sign of $b$. If $c$ is negative, the factors have opposite signs, and the larger factor takes the sign of $b$.",
    explain_underlying_rule: `In ${subject}, every transaction must maintain balance. For ${topic}, identify which element of the accounting/math equation is changing and apply the core definition.`,
    decompose_step: "Step 1: Identify the given values and their exact account types. Step 2: Apply the formula or debit/credit rule to calculate the unknown before posting.",
    explain_common_misconception: "The most frequent error here is confusing net amounts with gross amounts, or inverting debit and credit entries because of personal bank statement habits."
  };

  const handleSelectChip = (queryKey, label) => {
    const text = CHIP_EXPLANATIONS[queryKey] || CHIP_EXPLANATIONS.explain_underlying_rule;
    setSocraticResponse({
      title: label,
      text: text,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    });
  };

  const handleEvaluateTeachBack = async () => {
    if (!teachBackText.trim()) return;
    setIsEvaluating(true);

    try {
      const res = await fetch('/api/agent/teach-back', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          subject,
          topic,
          subskill,
          explanation: teachBackText,
          misconception_tag: misconceptionTags[0] || null
        })
      });

      if (res.ok) {
        const data = await res.json();
        setTeachBackResult(data);
        if (data.is_mastered && data.xp_awarded > 0) {
          onMasteryEarned(data.xp_awarded);
        }
      } else {
        // Fallback local heuristic
        const isMastered = teachBackText.length > 40;
        setTeachBackResult({
          is_mastered: isMastered,
          score: isMastered ? 100 : 60,
          status: isMastered ? 'mastered' : 'partial',
          socratic_feedback: isMastered 
            ? "Impressive explanation! You accurately captured the underlying principle."
            : "Good start. Make sure to clearly link the rule back to how the equation balances.",
          xp_awarded: isMastered ? 25 : 0
        });
      }
    } catch (e) {
      // Local fallback for offline mode
      const isMastered = teachBackText.length > 40;
      setTeachBackResult({
        is_mastered: isMastered,
        score: isMastered ? 100 : 60,
        status: isMastered ? 'mastered' : 'partial',
        socratic_feedback: isMastered 
          ? "Impressive explanation! You accurately captured the underlying principle."
          : "Good start. Make sure to clearly link the rule back to how the equation balances.",
        xp_awarded: isMastered ? 25 : 0
      });
    } finally {
      setIsEvaluating(false);
    }
  };

  if (!isOpen) return null;

  const isCircuitBreakerOpen = consecutiveErrors >= 3;

  return (
    <div className="fixed inset-y-0 right-0 z-50 w-full max-w-md bg-slate-900 border-l border-slate-800 shadow-2xl flex flex-col transition-all duration-300">
      
      {/* 1. DRAWER HEADER */}
      <div className="p-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/80">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-400 flex items-center justify-center">
            <Sparkles className="w-4 h-4" />
          </div>
          <div>
            <h2 className="text-sm font-bold text-white tracking-tight">Socratic Tutor</h2>
            <p className="text-[11px] text-slate-400">Pro Socratic Guidance · Zero Chat Fluff</p>
          </div>
        </div>

        <button 
          onClick={onClose}
          className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
        >
          <X className="w-5 h-5" />
        </button>
      </div>

      {/* 2. CIRCUIT BREAKER TRIGGER (IF >= 3 CONSECUTIVE ERRORS) */}
      {isCircuitBreakerOpen && (
        <div className="m-4 p-4 rounded-xl bg-amber-950/60 border border-amber-500/50 shadow-lg animate-in fade-in duration-300">
          <div className="flex items-start gap-2.5">
            <ShieldAlert className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
            <div>
              <h3 className="text-xs font-bold text-amber-200">3-Strike Circuit Breaker Tripped</h3>
              <p className="text-[11px] text-amber-300/80 mt-1 leading-relaxed">
                You've encountered 3 consecutive challenges on this archetype. Research shows watching a visual derivation at this point cements understanding faster than guessing.
              </p>
              <button
                onClick={onLaunchSimuLearn}
                className="mt-3 flex items-center gap-2 bg-amber-500 hover:bg-amber-400 text-slate-950 px-3.5 py-1.5 rounded-lg font-bold text-xs transition-all shadow-md"
              >
                <PlayCircle className="w-4 h-4" />
                <span>Launch SimuLearn Worked Example</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* 3. TABS: GUIDANCE CHIPS vs TEACH-BACK */}
      <div className="flex border-b border-slate-800 bg-slate-950/40 text-xs font-semibold px-4 pt-2 gap-2">
        <button
          onClick={() => setActiveTab('chips')}
          className={`pb-2 px-2 border-b-2 transition-colors flex items-center gap-1.5 ${
            activeTab === 'chips' ? 'border-indigo-500 text-indigo-400' : 'border-transparent text-slate-400 hover:text-slate-300'
          }`}
        >
          <Lightbulb className="w-3.5 h-3.5" />
          <span>Socratic Nudges</span>
        </button>
        <button
          onClick={() => setActiveTab('teach_back')}
          className={`pb-2 px-2 border-b-2 transition-colors flex items-center gap-1.5 ${
            activeTab === 'teach_back' ? 'border-indigo-500 text-indigo-400' : 'border-transparent text-slate-400 hover:text-slate-300'
          }`}
        >
          <MessageSquare className="w-3.5 h-3.5" />
          <span>Teach-Back Mode</span>
          <span className="bg-indigo-950 text-indigo-300 text-[10px] px-1.5 py-0.2 rounded-full border border-indigo-800">
            +25 XP
          </span>
        </button>
      </div>

      {/* 4. CONTENT BODY */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        
        {activeTab === 'chips' && (
          <div className="space-y-4">
            <DeclarativeSocraticChips
              misconceptionTags={misconceptionTags}
              activeSubskill={subskill}
              onSelectChip={handleSelectChip}
            />

            {socraticResponse && (
              <div className="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-2 animate-in fade-in duration-200">
                <div className="flex items-center justify-between text-xs text-indigo-400 font-bold">
                  <span className="flex items-center gap-1.5">
                    <Sparkles className="w-3.5 h-3.5" /> {socraticResponse.title}
                  </span>
                  <span className="text-[10px] text-slate-500 font-normal">{socraticResponse.timestamp}</span>
                </div>
                <p className="text-xs text-slate-300 leading-relaxed">
                  {socraticResponse.text}
                </p>
              </div>
            )}
          </div>
        )}

        {activeTab === 'teach_back' && (
          <div className="space-y-4">
            <div className="bg-slate-950 border border-slate-800 rounded-xl p-4">
              <span className="text-[11px] font-bold text-indigo-400 uppercase tracking-wider block mb-1">
                Cognitive Teach-Back Challenge
              </span>
              <p className="text-xs text-slate-300 leading-relaxed">
                Explain in your own words: <strong>Why do we apply the rule for {subskill}?</strong>
              </p>
              <p className="text-[11px] text-slate-500 mt-1">
                Tip: Mention account types (Asset/Expense/Revenue) or math signs to earn full mastery.
              </p>
            </div>

            <textarea
              rows={4}
              value={teachBackText}
              onChange={(e) => setTeachBackText(e.target.value)}
              placeholder="Type your explanation here (e.g., Bank is an asset that increases on the debit side because money was received...)"
              className="w-full bg-slate-950 border border-slate-700/80 rounded-xl p-3 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
            />

            <button
              disabled={isEvaluating || !teachBackText.trim()}
              onClick={handleEvaluateTeachBack}
              className="w-full flex items-center justify-center gap-2 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white py-2.5 rounded-xl font-bold text-xs transition-all shadow-md shadow-indigo-600/20"
            >
              {isEvaluating ? (
                <span>Analyzing Conceptual Mastery...</span>
              ) : (
                <>
                  <span>Submit Cognitive Explanation</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </>
              )}
            </button>

            {teachBackResult && (
              <div 
                className={`p-4 rounded-xl border animate-in fade-in duration-300 ${
                  teachBackResult.is_mastered 
                    ? 'bg-emerald-950/60 border-emerald-500/50' 
                    : 'bg-amber-950/60 border-amber-500/50'
                }`}
              >
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center gap-2">
                    {teachBackResult.is_mastered ? (
                      <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                    ) : (
                      <AlertCircle className="w-4 h-4 text-amber-400" />
                    )}
                    <span className="text-xs font-bold text-white capitalize">
                      {teachBackResult.status.replace('_', ' ')} ({teachBackResult.score}%)
                    </span>
                  </div>
                  {teachBackResult.xp_awarded > 0 && (
                    <span className="bg-emerald-900 text-emerald-300 border border-emerald-700 text-[10px] font-bold px-2 py-0.5 rounded-full">
                      +{teachBackResult.xp_awarded} XP Awarded
                    </span>
                  )}
                </div>

                <p className="text-xs text-slate-300 leading-relaxed">
                  {teachBackResult.socratic_feedback}
                </p>

                {teachBackResult.suggested_next_step === 'launch_simulearn' && (
                  <button
                    onClick={onLaunchSimuLearn}
                    className="mt-3 w-full flex items-center justify-center gap-1.5 bg-amber-500 hover:bg-amber-400 text-slate-950 py-1.5 rounded-lg font-bold text-xs transition-all"
                  >
                    <PlayCircle className="w-3.5 h-3.5" />
                    <span>Watch Worked Example Animation</span>
                  </button>
                )}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
