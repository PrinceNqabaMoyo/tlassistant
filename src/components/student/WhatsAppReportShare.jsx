import React from 'react';
import { Share2, MessageCircle, CheckCircle, Sparkles } from 'lucide-react';

export default function WhatsAppReportShare({
  studentName = 'Learner',
  subject = 'Mathematics',
  topic = 'Algebraic Expressions',
  masteryScore = 85,
  streakDays = 3,
}) {
  const generateWhatsAppMessage = () => {
    const text = `🌟 *Fundile Weekly Mastery Digest for ${studentName}*\n\n` +
      `📚 *Subject:* ${subject}\n` +
      `🎯 *Topic:* ${topic}\n` +
      `🔥 *Mastery Level:* ${Math.round(masteryScore)}% (Exam-Ready)\n` +
      `⚡ *Streak:* ${streakDays} days of active problem solving!\n\n` +
      `_Fundile: 100% Aligned with South African National Curriculum Standards_`;

    return `https://wa.me/?text=${encodeURIComponent(text)}`;
  };

  return (
    <div className="bg-gradient-to-r from-emerald-950/60 to-slate-900 border border-emerald-500/30 rounded-2xl p-4 flex flex-col sm:flex-row items-center justify-between gap-3 shadow-lg">
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0">
          <MessageCircle className="w-5 h-5" />
        </div>
        <div>
          <h4 className="text-sm font-semibold text-white flex items-center gap-1.5">
            Share Progress with Mom / Dad
            <Sparkles className="w-3.5 h-3.5 text-amber-400" />
          </h4>
          <p className="text-xs text-slate-400">
            Send a 1-tap weekly mastery snapshot via WhatsApp.
          </p>
        </div>
      </div>

      <a
        href={generateWhatsAppMessage()}
        target="_blank"
        rel="noopener noreferrer"
        className="flex items-center gap-2 px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold shadow-lg shadow-emerald-600/30 transition-all shrink-0"
      >
        <Share2 className="w-3.5 h-3.5" />
        <span>Send on WhatsApp</span>
      </a>
    </div>
  );
}
