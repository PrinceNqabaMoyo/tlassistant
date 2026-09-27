import React from 'react';
import { Award, CheckCircle2, XCircle, Sparkles, ArrowRight, Trophy } from 'lucide-react';

const MEDAL_STYLES = {
  gold: {
    icon: '🥇',
    title: 'Gold Topic Medal',
    border: 'border-amber-400 bg-amber-950/30 text-amber-300',
    glow: 'shadow-amber-500/30',
    badge: 'bg-amber-500/20 text-amber-300 border-amber-500/50'
  },
  silver: {
    icon: '🥈',
    title: 'Silver Topic Medal',
    border: 'border-slate-300 bg-slate-900/60 text-slate-200',
    glow: 'shadow-slate-400/20',
    badge: 'bg-slate-400/20 text-slate-200 border-slate-400/50'
  },
  bronze: {
    icon: '🥉',
    title: 'Bronze Topic Medal',
    border: 'border-orange-500/50 bg-orange-950/20 text-orange-300',
    glow: 'shadow-orange-500/20',
    badge: 'bg-orange-500/20 text-orange-300 border-orange-500/50'
  }
};

export default function ChallengeResultCard({
  isOpen = true,
  result = { passed: true, score_percentage: 86.7, medal_grade: 'silver', xp_awarded: 200 },
  challengeTitle = 'Algebraic Expressions Challenge',
  onClose,
  onViewTrophyRoom
}) {
  if (!isOpen || !result) return null;

  const medalStyle = result.medal_grade ? MEDAL_STYLES[result.medal_grade] : null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-950/85 backdrop-blur-md animate-fade-in text-slate-100">
      <div className="bg-slate-900 border border-slate-800 rounded-3xl shadow-2xl max-w-md w-full p-6 flex flex-col items-center text-center relative overflow-hidden">
        {/* Ambient Glow */}
        <div className="absolute -top-24 left-1/2 -translate-x-1/2 w-64 h-64 bg-indigo-500/15 rounded-full blur-3xl pointer-events-none" />

        {result.passed ? (
          <>
            <div className="w-16 h-16 rounded-2xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-3xl mb-4 shadow-lg shadow-amber-500/20 animate-bounce">
              {medalStyle?.icon || '🏆'}
            </div>
            <span className="text-xs px-2.5 py-0.5 rounded-full uppercase font-bold tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 mb-2">
              Challenge Passed!
            </span>
            <h3 className="text-xl font-bold text-slate-100">{challengeTitle}</h3>
            <div className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-300 via-amber-100 to-indigo-200 font-mono my-3">
              {result.score_percentage}%
            </div>

            {medalStyle && (
              <div className={`w-full p-4 rounded-2xl border ${medalStyle.border} shadow-lg ${medalStyle.glow} my-2 flex items-center justify-between`}>
                <div className="flex items-center gap-3 text-left">
                  <span className="text-2xl">{medalStyle.icon}</span>
                  <div>
                    <div className="text-sm font-bold text-slate-100">{medalStyle.title}</div>
                    <div className="text-xs text-slate-400">Authenticated Academic Credential</div>
                  </div>
                </div>
                <span className="text-sm font-mono font-bold text-indigo-300">+{result.xp_awarded} XP</span>
              </div>
            )}

            <p className="text-xs text-slate-300 mt-2 mb-6 leading-relaxed">
              Your mastery is verified. This credential has been added to your authenticated transcript.
            </p>

            <div className="w-full flex flex-col gap-2">
              {onViewTrophyRoom && (
                <button
                  onClick={onViewTrophyRoom}
                  className="w-full py-3 px-4 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-colors flex items-center justify-center gap-2 shadow-lg shadow-indigo-950/50"
                >
                  <Trophy className="w-4 h-4" />
                  <span>View in Trophy Room</span>
                </button>
              )}
              <button
                onClick={onClose}
                className="w-full py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-xs transition-colors"
              >
                Back to Curriculum Map
              </button>
            </div>
          </>
        ) : (
          <>
            <div className="w-16 h-16 rounded-2xl bg-rose-500/20 border border-rose-500/40 flex items-center justify-center text-3xl mb-4 text-rose-400">
              <XCircle className="w-8 h-8" />
            </div>
            <span className="text-xs px-2.5 py-0.5 rounded-full uppercase font-bold tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/30 mb-2">
              Threshold Not Reached
            </span>
            <h3 className="text-xl font-bold text-slate-100">{challengeTitle}</h3>
            <div className="text-3xl font-bold text-slate-300 font-mono my-3">
              {result.score_percentage}%
            </div>
            <p className="text-xs text-slate-400 my-2 leading-relaxed">
              Topic Medals require at least 60% mastery under exam conditions. Try the targeted prerequisite micro-drills to strengthen weak areas.
            </p>
            <button
              onClick={onClose}
              className="w-full mt-4 py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium text-xs transition-colors"
            >
              Continue Practice
            </button>
          </>
        )}
      </div>
    </div>
  );
}
