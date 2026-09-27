import React from 'react';

export default function XPProgressBar({
  level = 4,
  currentXP = 1350,
  progressPercent = 68,
  streakDays = 5,
  onClick
}) {
  return (
    <div
      onClick={onClick}
      className="p-3 bg-slate-900/90 rounded-2xl border border-slate-800 shadow-md flex items-center justify-between gap-3 cursor-pointer hover:border-indigo-500/50 transition-all duration-300 group"
    >
      {/* Level Ring */}
      <div className="flex items-center gap-3">
        <div className="relative w-11 h-11 flex items-center justify-center">
          <svg className="w-full h-full -rotate-90" viewBox="0 0 36 36">
            <circle
              cx="18"
              cy="18"
              r="15"
              fill="none"
              className="stroke-slate-800"
              strokeWidth="3.5"
            />
            <circle
              cx="18"
              cy="18"
              r="15"
              fill="none"
              className="stroke-indigo-500 transition-all duration-500 ease-out"
              strokeWidth="3.5"
              strokeDasharray="94.2"
              strokeDashoffset={94.2 - (94.2 * progressPercent) / 100}
              strokeLinecap="round"
            />
          </svg>
          <span className="absolute font-bold text-xs text-indigo-200">
            L{level}
          </span>
        </div>

        <div>
          <div className="flex items-center gap-2">
            <span className="text-xs font-semibold text-slate-100 group-hover:text-indigo-300 transition-colors">
              Level {level} Scholar
            </span>
          </div>
          <div className="text-[11px] text-slate-400 font-mono">
            {currentXP.toLocaleString()} Ungameable XP
          </div>
        </div>
      </div>

      {/* Streak Badge */}
      <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-semibold">
        <span className="animate-pulse">🔥</span>
        <span>{streakDays}d Streak</span>
      </div>
    </div>
  );
}
