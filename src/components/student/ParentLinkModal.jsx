import React, { useState } from 'react';
import { 
  Users, Copy, Check, Share2, ShieldCheck, Heart, Sparkles, 
  CheckCircle2, X, ArrowRight, MessageCircle, FileText
} from 'lucide-react';

/**
 * ParentLinkModal Component (Layer D — Phase D10 / OQ1 Resolution)
 * Resolves Open Question OQ1: 6-Character Parent Linking Code.
 * Zero-friction connection between student academic progress and parent WhatsApp reports.
 */
export default function ParentLinkModal({
  isOpen = false,
  onClose = () => {},
  studentName = 'Thabo Ndlovu',
  parentCode = 'PAR8M4',
  grade = '10',
  onOpenReport = () => {},
}) {
  const [copied, setCopied] = useState(false);
  const [parentPhone, setParentPhone] = useState('');
  const [isSubscribed, setIsSubscribed] = useState(false);
  const [inputCode, setInputCode] = useState('');
  const [linkedSuccess, setLinkedSuccess] = useState(false);

  if (!isOpen) return null;

  const handleCopy = () => {
    navigator.clipboard.writeText(parentCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  };

  const handleShareWhatsApp = () => {
    const text = encodeURIComponent(
      `👋 Hi Mom/Dad! Link to my Fundile academic progress to receive my weekly academic progress report.\n\n` +
      `My Parent Link Code is: *${parentCode}*\n\n` +
      `Open Fundile to view my diagnostic mastery and progress across Mathematics, Sciences & Commercials!`
    );
    window.open(`https://wa.me/?text=${text}`, '_blank');
  };

  const handleSubscribePhone = (e) => {
    e.preventDefault();
    if (parentPhone.trim().length >= 10) {
      setIsSubscribed(true);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md animate-in fade-in duration-200">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl max-w-lg w-full overflow-hidden text-slate-100 relative">
        
        {/* Modal Header */}
        <div className="p-5 border-b border-slate-800 bg-slate-950/60 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-indigo-500/20 text-indigo-400 border border-indigo-500/30 flex items-center justify-center">
              <Users className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white">Parent Progress Linking</h3>
              <p className="text-xs text-slate-400">Zero-Friction 6-Character Parent Code</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Content */}
        <div className="p-6 space-y-6">
          
          {/* 1. The 6-Character Code Box */}
          <div className="bg-slate-950 border border-indigo-500/30 rounded-2xl p-5 text-center relative overflow-hidden shadow-inner">
            <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-500/10 rounded-full blur-2xl pointer-events-none" />
            
            <span className="text-[11px] font-bold text-indigo-400 uppercase tracking-wider block mb-1">
              {studentName}'s Parent Link Code
            </span>
            <div className="text-3xl font-mono font-black text-white tracking-widest my-2">
              {parentCode}
            </div>
            <p className="text-xs text-slate-400 max-w-xs mx-auto">
              Share this code with your parents so they can receive your weekly diagnostic progress reports.
            </p>

            <div className="flex items-center justify-center gap-2.5 mt-4">
              <button
                onClick={handleCopy}
                className="flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 px-4 py-2 rounded-xl text-xs font-semibold transition-all border border-slate-700"
              >
                {copied ? <Check className="w-4 h-4 text-emerald-400" /> : <Copy className="w-4 h-4" />}
                <span>{copied ? 'Code Copied' : 'Copy Code'}</span>
              </button>

              <button
                onClick={handleShareWhatsApp}
                className="flex items-center gap-2 bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-md shadow-emerald-600/20"
              >
                <Share2 className="w-4 h-4" />
                <span>Share via WhatsApp</span>
              </button>
            </div>
          </div>

          {/* 2. Automated Weekly WhatsApp Digest Enrollment */}
          <div className="bg-slate-800/40 border border-slate-800 rounded-xl p-4 space-y-3">
            <div className="flex items-center gap-2 text-xs font-bold text-slate-200">
              <MessageCircle className="w-4 h-4 text-emerald-400" />
              <span>Automated Weekly WhatsApp Progress Reports</span>
            </div>
            <p className="text-xs text-slate-400 leading-relaxed">
              Every Sunday at 18:00, Fundile dispatches an executive 30-second progress card and PDF progress memo directly to parent WhatsApp.
            </p>

            {!isSubscribed ? (
              <form onSubmit={handleSubscribePhone} className="flex gap-2">
                <input
                  type="tel"
                  placeholder="Parent WhatsApp (e.g. 082 123 4567)"
                  value={parentPhone}
                  onChange={(e) => setParentPhone(e.target.value)}
                  className="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-emerald-500"
                />
                <button
                  type="submit"
                  disabled={parentPhone.trim().length < 10}
                  className="bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 text-white px-4 py-2 rounded-xl text-xs font-bold transition-colors shrink-0"
                >
                  Enroll
                </button>
              </form>
            ) : (
              <div className="p-3 bg-emerald-950/60 border border-emerald-500/40 rounded-xl flex items-center justify-between text-xs text-emerald-300">
                <div className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                  <span>Enrolled: Weekly Sunday 18:00 digest active for {parentPhone}</span>
                </div>
                <button onClick={() => setIsSubscribed(false)} className="text-[11px] underline text-emerald-400 hover:text-white">Edit</button>
              </div>
            )}
          </div>

          {/* 3. Direct Progress Report Action */}
          <div className="pt-2 flex items-center justify-between text-xs">
            <span className="text-slate-400">Want to inspect the report first?</span>
            <button
              onClick={() => {
                onClose();
                onOpenReport();
              }}
              className="text-indigo-400 hover:text-indigo-300 font-semibold flex items-center gap-1"
            >
              <FileText className="w-3.5 h-3.5" />
              <span>Preview Parent Diagnostic Report</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
