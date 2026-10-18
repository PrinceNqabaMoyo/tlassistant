import React, { useState } from 'react';
import { Sparkles, X, Check, BarChart3, RefreshCw, ShieldCheck, BookOpen, AlertCircle } from 'lucide-react';
import { buildApiUrl } from '../../utils/apiBaseUrl';

export default function TeacherAiCopilotPanel({
  isOpen = false,
  onClose = () => {},
  question = null,
  qIndex = 0,
  onApplyReskin = () => {},
  onApplyRubric = () => {},
  allQuestions = []
}) {
  const [activeTab, setActiveTab] = useState('reskin'); // 'reskin' | 'audit' | 'rubric'
  const [selectedTheme, setSelectedTheme] = useState('township_retail');
  const [customTheme, setCustomTheme] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [reskinnedResult, setReskinnedResult] = useState('');
  const [auditResult, setAuditResult] = useState(null);
  const [polishedScheme, setPolishedScheme] = useState(null);

  if (!isOpen) return null;

  const handleReskin = async () => {
    if (!question) return;
    setLoading(true);
    setError(null);
    setReskinnedResult('');

    try {
      const themeToSend = customTheme.trim() || selectedTheme;
      const res = await fetch(buildApiUrl('/api/teacher/copilot-assist'), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          action: 'reskin_context',
          question,
          context_theme: themeToSend
        })
      });

      if (!res.ok) {
        throw new Error('Copilot could not process reskin request.');
      }
      const data = await res.json();
      setReskinnedResult(data.reskinned_text || '');
    } catch (err) {
      setError(err.message || 'Reskin failed.');
    } finally {
      setLoading(false);
    }
  };

  const handleAudit = async () => {
    setLoading(true);
    setError(null);
    setAuditResult(null);

    try {
      const res = await fetch(buildApiUrl('/api/teacher/copilot-assist'), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          action: 'audit_balance',
          questions: allQuestions
        })
      });

      if (!res.ok) throw new Error('Audit failed.');
      const data = await res.json();
      setAuditResult(data.result);
    } catch (err) {
      setError(err.message || 'Audit failed.');
    } finally {
      setLoading(false);
    }
  };

  const handlePolishRubric = async () => {
    if (!question) return;
    setLoading(true);
    setError(null);
    setPolishedScheme(null);

    try {
      const res = await fetch(buildApiUrl('/api/teacher/copilot-assist'), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          action: 'polish_rubric',
          question
        })
      });

      if (!res.ok) throw new Error('Rubric polish failed.');
      const data = await res.json();
      setPolishedScheme(data.marking_scheme);
    } catch (err) {
      setError(err.message || 'Polish failed.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-[140] flex items-center justify-center bg-black/60 backdrop-blur-xs p-3 sm:p-4 animate-in fade-in select-none">
      <div 
        className="w-full max-w-lg bg-white rounded-3xl border border-slate-200 shadow-2xl overflow-hidden flex flex-col max-h-[88vh]"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-gradient-to-r from-[#13519C] to-indigo-700 text-white px-6 py-4 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-white/10 flex items-center justify-center border border-white/20">
              <Sparkles className="w-5 h-5 text-amber-300" />
            </div>
            <div>
              <h3 className="text-lg font-bold text-white leading-tight font-display">
                Teacher AI Copilot
              </h3>
              <p className="text-xs text-blue-100">
                Grounded on authoritative national curriculum benchmarks
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="p-1.5 rounded-full text-white/80 hover:text-white hover:bg-white/10 transition cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Tab Switcher */}
        <div className="grid grid-cols-3 p-1.5 bg-slate-100 border-b border-slate-200 text-xs font-bold shrink-0">
          <button
            type="button"
            onClick={() => setActiveTab('reskin')}
            className={`py-2 rounded-xl transition cursor-pointer text-center ${
              activeTab === 'reskin' ? 'bg-white text-[#13519C] shadow-xs' : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            🇿🇦 Reskin Context
          </button>
          <button
            type="button"
            onClick={() => { setActiveTab('audit'); handleAudit(); }}
            className={`py-2 rounded-xl transition cursor-pointer text-center ${
              activeTab === 'audit' ? 'bg-white text-[#13519C] shadow-xs' : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            📊 Cognitive Audit
          </button>
          <button
            type="button"
            onClick={() => setActiveTab('rubric')}
            className={`py-2 rounded-xl transition cursor-pointer text-center ${
              activeTab === 'rubric' ? 'bg-white text-[#13519C] shadow-xs' : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            ✍️ Polish Rubric
          </button>
        </div>

        {/* Body */}
        <div className="p-5 overflow-y-auto flex-1 font-sans space-y-4">
          {error && (
            <div className="p-3 bg-red-50 border border-red-200 text-red-700 text-xs rounded-xl flex items-center gap-2">
              <AlertCircle className="w-4 h-4 shrink-0" />
              <span>{error}</span>
            </div>
          )}

          {/* TAB 1: RESKIN CONTEXT */}
          {activeTab === 'reskin' && (
            <div className="space-y-4">
              <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-2xl text-xs text-emerald-900 flex items-start gap-2.5">
                <ShieldCheck className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                <div>
                  <strong className="block font-bold">Numerical Invariance Active</strong>
                  The Copilot adapts the narrative story while locking every mathematical number, equation, and unit so the marking memo remains 100% accurate.
                </div>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-2">
                  Target Question: <span className="text-[#13519C]">Question {qIndex + 1}</span>
                </label>
                <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-600 italic max-h-24 overflow-y-auto">
                  "{question?.question_text}"
                </div>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-2">
                  Select South African Context Theme
                </label>
                <div className="grid grid-cols-2 gap-2 text-xs">
                  {[
                    { id: 'township_retail', label: '🛒 Township Spaza / Bakery' },
                    { id: 'renewable_energy', label: '☀️ Karoo Solar & Wind Farm' },
                    { id: 'agriculture', label: '🌾 Citrus & Macadamia Farm' },
                    { id: 'sports', label: '⚽ Provincial Schools Tournament' },
                    { id: 'tech_startup', label: '💻 Cape Town Tech & Logistics' }
                  ].map(theme => (
                    <button
                      key={theme.id}
                      type="button"
                      onClick={() => { setSelectedTheme(theme.id); setCustomTheme(''); }}
                      className={`p-2.5 rounded-xl border text-left font-medium transition cursor-pointer ${
                        selectedTheme === theme.id && !customTheme
                          ? 'border-[#13519C] bg-blue-50/80 text-[#13519C] font-bold shadow-2xs'
                          : 'border-slate-200 hover:bg-slate-50 text-slate-700'
                      }`}
                    >
                      {theme.label}
                    </button>
                  ))}
                </div>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">
                  Or Custom South African Setting:
                </label>
                <input
                  type="text"
                  placeholder="e.g. Durban harbor shipping logistics"
                  value={customTheme}
                  onChange={(e) => setCustomTheme(e.target.value)}
                  className="w-full px-3 py-2 text-xs rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#13519C]"
                />
              </div>

              <button
                type="button"
                onClick={handleReskin}
                disabled={loading}
                className="w-full py-2.5 rounded-xl bg-[#13519C] hover:bg-blue-800 text-white font-bold text-xs flex items-center justify-center gap-2 shadow-xs transition cursor-pointer disabled:opacity-50"
              >
                {loading ? <RefreshCw className="w-3.5 h-3.5 animate-spin" /> : <Sparkles className="w-3.5 h-3.5" />}
                <span>Reskin Scenario (Preserve Numbers)</span>
              </button>

              {reskinnedResult && (
                <div className="space-y-2 pt-2 border-t border-slate-200">
                  <label className="block text-xs font-bold text-emerald-800">
                    Generated Reskinned Scenario:
                  </label>
                  <div className="p-3 bg-emerald-50/70 border border-emerald-200 rounded-xl text-xs text-slate-800 leading-relaxed font-sans">
                    {reskinnedResult}
                  </div>
                  <button
                    type="button"
                    onClick={() => {
                      onApplyReskin(reskinnedResult);
                      onClose();
                    }}
                    className="w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold rounded-xl shadow-xs transition cursor-pointer flex items-center justify-center gap-1.5"
                  >
                    <Check className="w-4 h-4" />
                    <span>Apply to Question {qIndex + 1}</span>
                  </button>
                </div>
              )}
            </div>
          )}

          {/* TAB 2: COGNITIVE BALANCE AUDIT */}
          {activeTab === 'audit' && (
            <div className="space-y-4">
              <div className="p-3 bg-blue-50 border border-blue-200 rounded-2xl text-xs text-[#13519C]">
                💡 Audits the current test paper against official national examination cognitive level targets (Levels 1 to 4).
              </div>

              {loading ? (
                <div className="py-8 text-center text-slate-500 text-xs">
                  <RefreshCw className="w-5 h-5 animate-spin mx-auto mb-2 text-[#13519C]" />
                  Auditing paper cognitive levels...
                </div>
              ) : auditResult ? (
                <div className="space-y-3">
                  <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs flex items-center justify-between">
                    <span className="font-bold text-slate-700">Total Paper Marks:</span>
                    <span className="font-bold font-mono text-[#13519C] text-sm">{auditResult.total_marks} Marks</span>
                  </div>

                  <div className="space-y-2">
                    {Object.entries(auditResult.distribution || {}).map(([key, val]) => (
                      <div key={key} className="p-2.5 bg-white rounded-xl border border-slate-200 flex items-center justify-between text-xs">
                        <span className="font-medium text-slate-700">{key}</span>
                        <span className="font-bold font-mono text-slate-900 bg-slate-100 px-2 py-0.5 rounded">{val}</span>
                      </div>
                    ))}
                  </div>

                  <div className="p-3 bg-amber-50 border border-amber-200 rounded-xl text-xs text-amber-900 font-medium">
                    🎯 <strong>Curriculum Recommendation:</strong> {auditResult.recommendation}
                  </div>
                </div>
              ) : null}
            </div>
          )}

          {/* TAB 3: POLISH RUBRIC */}
          {activeTab === 'rubric' && (
            <div className="space-y-4">
              <div className="p-3 bg-blue-50 border border-blue-200 rounded-2xl text-xs text-[#13519C]">
                💡 Standardizes marking criteria with official National Senior Certificate (NSC) marking notation: <strong>[M]</strong> Method mark, <strong>[A]</strong> Accuracy mark, <strong>[CA]</strong> Consistent Accuracy.
              </div>

              <button
                type="button"
                onClick={handlePolishRubric}
                disabled={loading}
                className="w-full py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs flex items-center justify-center gap-2 shadow-xs transition cursor-pointer disabled:opacity-50"
              >
                {loading ? <RefreshCw className="w-3.5 h-3.5 animate-spin" /> : <BookOpen className="w-3.5 h-3.5" />}
                <span>Format with Official Exam Marking Symbols</span>
              </button>

              {polishedScheme && (
                <div className="space-y-2 pt-2 border-t border-slate-200">
                  <label className="block text-xs font-bold text-slate-700">
                    Polished Marking Scheme:
                  </label>
                  <div className="space-y-1.5 max-h-48 overflow-y-auto">
                    {polishedScheme.map((item, idx) => (
                      <div key={idx} className="p-2 bg-slate-50 border border-slate-200 rounded-lg text-xs flex items-center justify-between">
                        <span className="font-medium text-slate-800">{item.point}</span>
                        <span className="font-bold text-[#13519C] font-mono">[{item.marks} M]</span>
                      </div>
                    ))}
                  </div>
                  <button
                    type="button"
                    onClick={() => {
                      onApplyRubric(polishedScheme);
                      onClose();
                    }}
                    className="w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold rounded-xl shadow-xs transition cursor-pointer flex items-center justify-center gap-1.5"
                  >
                    <Check className="w-4 h-4" />
                    <span>Apply Polished Notation</span>
                  </button>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="p-3.5 bg-slate-50 border-t border-slate-200 flex items-center justify-between text-xs text-slate-500 shrink-0">
          <span>Grounded in DBE National Curriculum Standards</span>
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl bg-slate-200 hover:bg-slate-300 text-slate-800 font-bold transition cursor-pointer"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
