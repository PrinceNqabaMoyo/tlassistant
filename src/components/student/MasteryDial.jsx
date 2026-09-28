import React from 'react';
import { Award, ShieldCheck, Sparkles, TrendingUp, AlertTriangle, RotateCcw } from 'lucide-react';

export default function MasteryDial({
  formativeMastery = 0, // BKT P(L_n), 0 - 100
  evaluativeScore = 0,   // Evaluative homework/test avg, 0 - 100
  size = 140,
  strokeWidth = 9,
  isRefreshRecommended = false,
  onTriggerRefresher = () => {},
  variant = 'light', // 'light' (Simulation Box aesthetic) | 'dark'
}) {
  const center = size / 2;
  const outerRadius = center - strokeWidth;
  const innerRadius = outerRadius - strokeWidth - 4;

  const outerCircumference = 2 * Math.PI * outerRadius;
  const innerCircumference = 2 * Math.PI * innerRadius;

  const clampedFormative = Math.min(100, Math.max(0, formativeMastery));
  const clampedEvaluative = Math.min(100, Math.max(0, evaluativeScore));

  const outerStrokeDashoffset = outerCircumference - (clampedEvaluative / 100) * outerCircumference;
  const innerStrokeDashoffset = innerCircumference - (clampedFormative / 100) * innerCircumference;

  const isExamReady = clampedFormative >= 80;
  const isDiagnostic = clampedFormative === 0;

  // Level classification
  const getLevel = (score, needsRefresh) => {
    if (needsRefresh) {
      return {
        title: 'Refresh Needed',
        color: variant === 'light' ? 'text-amber-900' : 'text-amber-300',
        bg: variant === 'light' ? 'bg-amber-50 border-amber-300 animate-pulse' : 'bg-amber-500/20 border-amber-500/50 animate-pulse',
      };
    }
    if (isExamReady) {
      return { 
        title: 'Exam Ready (Level 7)', 
        color: variant === 'light' ? 'text-emerald-800' : 'text-emerald-400', 
        bg: variant === 'light' ? 'bg-emerald-50 border-emerald-300 ring-1 ring-emerald-400/20' : 'bg-emerald-500/10 border-emerald-500/30' 
      };
    }
    if (score >= 60) {
      return { 
        title: 'Proficient (Level 5)', 
        color: variant === 'light' ? 'text-blue-800' : 'text-blue-400', 
        bg: variant === 'light' ? 'bg-blue-50 border-blue-300' : 'bg-blue-500/10 border-blue-500/30' 
      };
    }
    if (isDiagnostic) {
      return {
        title: 'Diagnostic Baseline',
        color: variant === 'light' ? 'text-amber-800' : 'text-amber-300',
        bg: variant === 'light' ? 'bg-amber-50 border-amber-300' : 'bg-amber-500/20 border-amber-500/40',
      };
    }
    return { 
      title: 'Foundation (Level 3)', 
      color: variant === 'light' ? 'text-amber-800' : 'text-amber-400', 
      bg: variant === 'light' ? 'bg-amber-50 border-amber-300' : 'bg-amber-500/10 border-amber-500/30' 
    };
  };

  const level = getLevel(clampedFormative, isRefreshRecommended);

  if (variant === 'light') {
    return (
      <div className="flex flex-col items-center justify-center p-5 bg-white rounded-2xl border border-slate-200 shadow-xs font-sans w-full">
        <div className="relative" style={{ width: size, height: size }}>
          <svg width={size} height={size} className="transform -rotate-90">
            {/* Outer Track (Evaluative Exam) */}
            <circle 
              cx={center} 
              cy={center} 
              r={outerRadius} 
              fill="transparent" 
              stroke="rgba(203, 213, 225, 0.4)" 
              strokeWidth={strokeWidth} 
            />
            <circle
              cx={center}
              cy={center}
              r={outerRadius}
              fill="transparent"
              stroke="#F59E0B"
              strokeWidth={strokeWidth}
              strokeDasharray={outerCircumference}
              strokeDashoffset={outerStrokeDashoffset}
              strokeLinecap="round"
              className="transition-all duration-700 ease-out"
            />

            {/* Inner Track (Formative BKT Mastery) */}
            <circle 
              cx={center} 
              cy={center} 
              r={innerRadius} 
              fill="transparent" 
              stroke="rgba(203, 213, 225, 0.3)" 
              strokeWidth={strokeWidth} 
            />
            <circle
              cx={center}
              cy={center}
              r={innerRadius}
              fill="transparent"
              stroke="#10B981"
              strokeWidth={strokeWidth}
              strokeDasharray={innerCircumference}
              strokeDashoffset={innerStrokeDashoffset}
              strokeLinecap="round"
              className="transition-all duration-700 ease-out"
            />
          </svg>

          {/* Center Percentage Display */}
          <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
            <span className="text-2xl font-bold text-slate-900 tracking-tight font-mono">
              {Math.round(clampedFormative)}%
            </span>
            <span className="text-[9px] uppercase font-bold text-slate-500 tracking-wider font-sans">
              BKT Mastery
            </span>
          </div>
        </div>

        {/* Level Badge */}
        <div className={`mt-3 px-3 py-1 rounded-full border text-xs font-bold flex items-center gap-1.5 ${level.bg} ${level.color}`}>
          {isRefreshRecommended ? (
            <AlertTriangle className="w-3.5 h-3.5" />
          ) : (
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
          )}
          <span>{level.title}</span>
        </div>

        {/* Refresher Sprint Action */}
        {isRefreshRecommended && (
          <button
            onClick={onTriggerRefresher}
            className="mt-2.5 w-full py-1.5 px-3 rounded-xl bg-amber-50 hover:bg-amber-100 border border-amber-300 text-amber-900 text-xs font-semibold flex items-center justify-center gap-1.5 transition-colors shadow-2xs cursor-pointer"
          >
            <RotateCcw className="w-3.5 h-3.5 text-amber-600" />
            <span>2-Question Refresher Sprint</span>
          </button>
        )}

        {/* Track Legend */}
        <div className="mt-3 grid grid-cols-2 gap-2 w-full text-[11px] text-slate-500 pt-2.5 border-t border-slate-100 font-mono">
          <div className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-full bg-[#10B981] shrink-0" />
            <span className="truncate">BKT: {Math.round(clampedFormative)}%</span>
          </div>
          <div className="flex items-center gap-1.5 justify-end">
            <span className="w-2.5 h-2.5 rounded-full bg-[#F59E0B] shrink-0" />
            <span className="truncate">Exam: {Math.round(clampedEvaluative)}%</span>
          </div>
        </div>
      </div>
    );
  }

  // Dark variant fallback
  return (
    <div className="flex flex-col items-center justify-center p-4 bg-slate-900/90 rounded-2xl border border-slate-800 shadow-xl backdrop-blur">
      <div className="relative" style={{ width: size, height: size }}>
        <svg width={size} height={size} className="transform -rotate-90">
          <circle
            cx={center}
            cy={center}
            r={outerRadius}
            fill="transparent"
            stroke="rgb(51, 65, 85, 0.4)"
            strokeWidth={strokeWidth}
          />
          <circle
            cx={center}
            cy={center}
            r={outerRadius}
            fill="transparent"
            stroke="url(#evaluativeGradient)"
            strokeWidth={strokeWidth}
            strokeDasharray={outerCircumference}
            strokeDashoffset={outerStrokeDashoffset}
            strokeLinecap="round"
            className="transition-all duration-700 ease-out"
          />

          <circle
            cx={center}
            cy={center}
            r={innerRadius}
            fill="transparent"
            stroke="rgb(51, 65, 85, 0.3)"
            strokeWidth={strokeWidth}
          />
          <circle
            cx={center}
            cy={center}
            r={innerRadius}
            fill="transparent"
            stroke="url(#formativeGradient)"
            strokeWidth={strokeWidth}
            strokeDasharray={innerCircumference}
            strokeDashoffset={innerStrokeDashoffset}
            strokeLinecap="round"
            className="transition-all duration-700 ease-out"
          />

          <defs>
            <linearGradient id="formativeGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#10B981" />
              <stop offset="100%" stopColor="#06B6D4" />
            </linearGradient>
            <linearGradient id="evaluativeGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#F59E0B" />
              <stop offset="100%" stopColor="#EC4899" />
            </linearGradient>
          </defs>
        </svg>

        <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
          <span className="text-2xl font-bold text-white tracking-tight font-mono">
            {Math.round(clampedFormative)}%
          </span>
          <span className="text-[10px] uppercase font-semibold text-slate-400 tracking-wider">
            Mastery
          </span>
        </div>
      </div>

      <div className={`mt-3 px-2.5 py-0.5 rounded-full border text-xs font-medium flex items-center gap-1.5 ${level.bg} ${level.color}`}>
        {isRefreshRecommended ? (
          <AlertTriangle className="w-3.5 h-3.5" />
        ) : (
          <ShieldCheck className="w-3.5 h-3.5" />
        )}
        <span>{level.title}</span>
      </div>

      {isRefreshRecommended && (
        <button
          onClick={onTriggerRefresher}
          className="mt-2.5 w-full py-1.5 px-3 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 border border-amber-500/40 text-amber-200 text-xs font-semibold flex items-center justify-center gap-1.5 transition-colors shadow-sm"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>2-Question Refresher Sprint</span>
        </button>
      )}

      <div className="mt-3 grid grid-cols-2 gap-2 w-full text-[11px] text-slate-400 pt-2 border-t border-slate-800 font-mono">
        <div className="flex items-center gap-1.5">
          <span className="w-2 h-2 rounded-full bg-emerald-400 shrink-0" />
          <span className="truncate">Formative: {Math.round(clampedFormative)}%</span>
        </div>
        <div className="flex items-center gap-1.5">
          <span className="w-2 h-2 rounded-full bg-amber-400 shrink-0" />
          <span className="truncate">Evaluative: {Math.round(clampedEvaluative)}%</span>
        </div>
      </div>
    </div>
  );
}
