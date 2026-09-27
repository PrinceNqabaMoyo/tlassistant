import React from 'react';
import { BadgeVisualEmblem, TIER_METADATA, getSubjectMeta } from './badgeIconRegistry';

export default function BadgeCard({
  tier = 'subskill_pin',
  title = 'Mastery Pin',
  subject = 'Mathematics',
  xp = 50,
  isLocked = false,
  grade = null,
  earnedAt = null
}) {
  const style = TIER_METADATA[tier] || TIER_METADATA.subskill_pin;
  const subjectMeta = getSubjectMeta(subject);

  if (isLocked) {
    return (
      <div className="flex items-center gap-3 p-3 rounded-xl border border-slate-800/80 bg-slate-900/40 opacity-50 grayscale select-none">
        <div className="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center text-lg text-slate-500">
          🔒
        </div>
        <div className="flex-1 min-w-0">
          <div className="text-xs font-medium text-slate-400 truncate">{title}</div>
          <div className="text-[11px] text-slate-500">{subject} • Locked</div>
        </div>
      </div>
    );
  }

  return (
    <div className={`group flex items-center gap-3 p-3 rounded-xl border ${style.border} shadow-lg ${style.glow} transition-all duration-300 hover:scale-[1.02] cursor-default`}>
      <BadgeVisualEmblem subject={subject} tier={tier} grade={grade} size="md" />
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-1.5 flex-wrap">
          <span className="text-xs font-semibold text-slate-100 truncate">{title}</span>
          {grade && (
            <span className="text-[10px] px-1.5 py-0.2 rounded-full uppercase font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">
              {grade}
            </span>
          )}
        </div>
        <div className="flex items-center justify-between text-[11px] text-slate-400 mt-0.5">
          <span>{subject}</span>
          <div className="flex items-center gap-2">
            <span className="font-mono text-indigo-400 font-semibold">+{xp} XP</span>
            <button
              onClick={(e) => {
                e.stopPropagation();
                const text = encodeURIComponent(
                  `🏅 *Academic Achievement on Fundile*\n` +
                  `I just earned the *${title}* (${grade ? grade.toUpperCase() + ' ' : ''}${tier.replace('_', ' ')}) in *${subject}*!\n` +
                  `Verified National Curriculum Mastery · +${xp} Ungameable Academic XP.`
                );
                window.open(`https://wa.me/?text=${text}`, '_blank');
              }}
              title="Share Achievement on WhatsApp"
              className="p-1 rounded-md bg-emerald-950/60 hover:bg-emerald-900 border border-emerald-800/60 text-emerald-400 hover:text-emerald-200 transition-colors"
            >
              <span className="text-[10px] font-bold">Share 💬</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
