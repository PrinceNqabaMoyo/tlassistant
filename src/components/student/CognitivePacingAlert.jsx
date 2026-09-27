import React, { useState, useEffect } from 'react';
import { Clock, Coffee, PlayCircle, X, Sparkles, AlertTriangle } from 'lucide-react';

export default function CognitivePacingAlert({
  thresholdMinutes = 45,
  onOpenSimuLearn = () => {},
  isPracticing = true,
}) {
  const [secondsElapsed, setSecondsElapsed] = useState(0);
  const [showAlert, setShowAlert] = useState(false);
  const [breakTimer, setBreakTimer] = useState(null); // seconds remaining in 10-min break
  const [isDismissedForNow, setIsDismissedForNow] = useState(false);

  // Active deliberate practice timer
  useEffect(() => {
    if (!isPracticing || breakTimer !== null) return;

    const interval = setInterval(() => {
      setSecondsElapsed((prev) => {
        const next = prev + 1;
        if (next >= thresholdMinutes * 60 && !isDismissedForNow && !showAlert) {
          setShowAlert(true);
        }
        return next;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [isPracticing, thresholdMinutes, isDismissedForNow, showAlert, breakTimer]);

  // Break countdown timer
  useEffect(() => {
    if (breakTimer === null) return;
    if (breakTimer <= 0) {
      setBreakTimer(null);
      setSecondsElapsed(0); // Reset session timer after break
      setIsDismissedForNow(false);
      return;
    }

    const interval = setInterval(() => {
      setBreakTimer((prev) => (prev > 0 ? prev - 1 : 0));
    }, 1000);

    return () => clearInterval(interval);
  }, [breakTimer]);

  const elapsedMinutes = Math.floor(secondsElapsed / 60);
  const isNearLimit = elapsedMinutes >= thresholdMinutes - 5;
  const isOverLimit = elapsedMinutes >= thresholdMinutes;

  const handleStartBreak = () => {
    setShowAlert(false);
    setBreakTimer(10 * 60); // 10 minutes
  };

  const handleDismiss = () => {
    setShowAlert(false);
    setIsDismissedForNow(true);
    // Re-prompt in 15 minutes
    setTimeout(() => {
      setIsDismissedForNow(false);
    }, 15 * 60 * 1000);
  };

  // Break overlay
  if (breakTimer !== null) {
    const mins = Math.floor(breakTimer / 60);
    const secs = breakTimer % 60;
    return (
      <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/90 backdrop-blur-md p-4 animate-in fade-in">
        <div className="bg-slate-900 border border-emerald-500/40 rounded-3xl p-8 max-w-md w-full text-center shadow-2xl relative">
          <div className="w-16 h-16 rounded-2xl bg-emerald-500/20 text-emerald-400 mx-auto flex items-center justify-center mb-4 border border-emerald-500/30">
            <Coffee className="w-8 h-8" />
          </div>
          <h3 className="text-xl font-bold text-white mb-1">Rest & Consolidation Break</h3>
          <p className="text-sm text-slate-400 mb-6">
            Step away from the screen, stretch, and hydrate. Your cognitive schemas consolidate during rest!
          </p>

          <div className="text-4xl font-mono font-black text-emerald-300 tracking-wider mb-6 bg-slate-950/60 py-4 rounded-2xl border border-slate-800">
            {String(mins).padStart(2, '0')}:{String(secs).padStart(2, '0')}
          </div>

          <button
            onClick={() => {
              setBreakTimer(null);
              setSecondsElapsed(0);
            }}
            className="text-xs text-slate-400 hover:text-white underline transition-colors"
          >
            End break early and resume practice
          </button>
        </div>
      </div>
    );
  }

  return (
    <>
      {/* Ambient status indicator in bottom-right corner when near/over limit */}
      {isNearLimit && !showAlert && (
        <button
          onClick={() => setShowAlert(true)}
          className={`fixed bottom-4 right-4 z-40 flex items-center gap-2 px-3 py-1.5 rounded-full text-xs font-medium border shadow-lg backdrop-blur transition-all ${
            isOverLimit
              ? 'bg-amber-950/80 border-amber-500/50 text-amber-300 animate-pulse'
              : 'bg-slate-900/90 border-slate-700 text-slate-300'
          }`}
        >
          <Clock className="w-3.5 h-3.5" />
          <span>{elapsedMinutes}m deliberate practice</span>
        </button>
      )}

      {/* 45-Minute Circuit Breaker Modal */}
      {showAlert && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4 animate-in fade-in duration-200">
          <div className="bg-slate-900 border border-amber-500/40 rounded-2xl max-w-lg w-full p-6 shadow-2xl relative text-white flex flex-col gap-4">
            <div className="flex items-start justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2 text-amber-400 text-xs font-semibold uppercase tracking-wider">
                <AlertTriangle className="w-4 h-4" />
                <span>Cognitive Pacing Guardrail</span>
              </div>
              <button
                onClick={handleDismiss}
                className="text-slate-400 hover:text-white transition-colors"
                title="Dismiss"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div>
              <h3 className="text-lg font-bold text-slate-100">
                45 Minutes of Continuous Deliberate Practice Reached
              </h3>
              <p className="text-sm text-slate-300 mt-2 leading-relaxed">
                Cognitive science indicates that procedural accuracy declines significantly past 45 minutes of intense problem-solving. Pausing now prevents fatigue-induced error patterns.
              </p>
            </div>

            {/* Action options */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
              <button
                onClick={handleStartBreak}
                className="flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-sm transition-all shadow-lg shadow-emerald-600/20"
              >
                <Coffee className="w-4 h-4" />
                <span>Take 10-Min Break</span>
              </button>

              <button
                onClick={() => {
                  setShowAlert(false);
                  onOpenSimuLearn();
                }}
                className="flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm transition-all shadow-lg shadow-indigo-600/20"
              >
                <PlayCircle className="w-4 h-4" />
                <span>Watch SimuLearn</span>
              </button>
            </div>

            <button
              onClick={handleDismiss}
              className="w-full text-center text-xs text-slate-400 hover:text-slate-200 py-1 transition-colors"
            >
              Dismiss and continue practicing for 15 more minutes
            </button>
          </div>
        </div>
      )}
    </>
  );
}
