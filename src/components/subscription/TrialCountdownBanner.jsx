import React from 'react';
import { Clock, ShieldAlert, Sparkles, Zap } from 'lucide-react';

/**
 * TrialCountdownBanner Component (Phase D2)
 * Renders an ambient status banner/pill indicating trial countdown,
 * paywall warning, or subscribed tier badge.
 */
export default function TrialCountdownBanner({
  trialStatus = { tier: 'trial', days_remaining: 12, trial_expired: false },
  onOpenSubscriptionModal = () => {},
  compact = false,
}) {
  const { tier = 'trial', days_remaining = 14, trial_expired = false } = trialStatus;

  if (tier === 'pro') {
    return (
      <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-purple-900/40 to-indigo-900/40 border border-purple-500/40 text-purple-300 shadow-sm">
        <Sparkles className="w-3.5 h-3.5 text-purple-400 animate-pulse" />
        <span>Fundile Pro</span>
      </div>
    );
  }

  if (tier === 'standard') {
    return (
      <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-950/40 border border-emerald-500/40 text-emerald-300 shadow-sm">
        <Zap className="w-3.5 h-3.5 text-emerald-400" />
        <span>Standard Subscriber</span>
      </div>
    );
  }

  if (trial_expired) {
    return (
      <button
        onClick={onOpenSubscriptionModal}
        className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-bold bg-rose-950/60 border border-rose-500/70 text-rose-300 hover:bg-rose-900/80 transition shadow-md animate-bounce"
        title="Your 14-day free trial has expired. Click to subscribe."
      >
        <ShieldAlert className="w-3.5 h-3.5 text-rose-400" />
        <span>Trial Expired — Unlock Access</span>
      </button>
    );
  }

  // Active Trial
  const isUrgent = days_remaining <= 3;
  return (
    <button
      onClick={onOpenSubscriptionModal}
      className={`inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium transition cursor-pointer ${
        isUrgent
          ? 'bg-amber-950/50 border border-amber-500/60 text-amber-300 hover:bg-amber-900/60'
          : 'bg-slate-800/80 border border-slate-700 text-slate-300 hover:bg-slate-700/80 hover:border-slate-500'
      }`}
      title="Click to view subscription options"
    >
      <Clock className={`w-3.5 h-3.5 ${isUrgent ? 'text-amber-400 animate-spin' : 'text-cyan-400'}`} />
      <span>
        {days_remaining === 1 ? (
          <strong className="text-amber-300">1 day left of trial</strong>
        ) : (
          <>
            <strong>{days_remaining} days</strong> left of trial
          </>
        )}
      </span>
      <span className="text-[10px] text-cyan-400 underline font-semibold ml-0.5">Upgrade</span>
    </button>
  );
}
