import React, { useState, useEffect } from 'react';
import { 
  RotateCcw, 
  Sparkles, 
  CheckCircle2, 
  AlertTriangle, 
  ShieldAlert, 
  Flame, 
  Zap, 
  X,
  BookOpen,
  Settings
} from 'lucide-react';
import studentStore from '../../services/studentStore';

/**
 * SuperAdminProgressResetModal
 * Allows the owner / super admin to reset student mastery and dues to 0%
 * or toggle between testing presets to thoroughly verify the adaptive onboarding journey.
 */
export default function SuperAdminProgressResetModal({ 
  isOpen, 
  onClose, 
  activeSubject = 'accounting' 
}) {
  const [storeState, setStoreState] = useState(() => studentStore.getState());
  const [toastMessage, setToastMessage] = useState(null);

  useEffect(() => {
    const unsubscribe = studentStore.subscribe((newState) => {
      setStoreState({ ...newState });
    });
    return unsubscribe;
  }, []);

  const showToast = (msg) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3500);
  };

  if (!isOpen) return null;

  const currentSub = studentStore.getSubject(activeSubject);

  const handleResetActive = () => {
    studentStore.resetSubjectToZero(activeSubject);
    showToast(`Reset ${activeSubject} to 0% (Diagnostic Required)`);
  };

  const handleResetAll = () => {
    studentStore.resetAllSubjectsToZero();
    showToast('All subjects reset to 0% mastery and 0 dues');
  };

  const handleApplyPreset = (presetName, label) => {
    studentStore.setPresetProfile(presetName);
    showToast(`Applied preset: ${label}`);
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4 animate-in fade-in duration-150">
      <div className="bg-white rounded-2xl max-w-lg w-full border border-slate-300 shadow-2xl overflow-hidden text-slate-800">
        
        {/* Header */}
        <div className="px-5 py-4 bg-[#13519C] text-white flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-white/10 flex items-center justify-center text-white">
              <ShieldAlert className="w-5 h-5 text-amber-300" />
            </div>
            <div>
              <h3 className="font-bold text-sm tracking-tight">Super Admin • Mastery &amp; Progress Testing Control</h3>
              <p className="text-[11px] text-blue-100">Live calibration tool for Onboarding, Diagnostics &amp; Mastery Dials</p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="w-8 h-8 rounded-lg flex items-center justify-center hover:bg-white/10 text-white/80 hover:text-white transition cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Toast Notification */}
        {toastMessage && (
          <div className="px-5 py-2.5 bg-emerald-50 border-b border-emerald-200 text-emerald-800 text-xs font-semibold flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
            <span>{toastMessage}</span>
          </div>
        )}

        <div className="p-5 space-y-4 max-h-[80vh] overflow-y-auto">
          {/* Active Subject Live Status */}
          <div className="p-3.5 bg-slate-50 border border-slate-200 rounded-xl space-y-2">
            <div className="flex items-center justify-between text-xs">
              <span className="font-bold text-slate-700 uppercase tracking-wider text-[10px]">
                Active Subject: <strong className="text-slate-900 uppercase font-extrabold">{activeSubject}</strong>
              </span>
              <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                currentSub.status === 'exam_ready' ? 'bg-emerald-100 text-emerald-800' :
                currentSub.status === 'practice' ? 'bg-blue-100 text-blue-800' :
                currentSub.status === 'scaffold' ? 'bg-amber-100 text-amber-800' :
                'bg-slate-200 text-slate-700'
              }`}>
                {currentSub.status === 'diagnostic_required' ? 'Diagnostic Required' : currentSub.status}
              </span>
            </div>

            <div className="grid grid-cols-2 gap-3 text-center">
              <div className="p-2 bg-white rounded-lg border border-slate-200 shadow-2xs">
                <div className="text-xl font-bold text-slate-900">{currentSub.formativeMastery}%</div>
                <div className="text-[10px] text-slate-500 uppercase font-bold tracking-wider">Formative BKT</div>
              </div>
              <div className="p-2 bg-white rounded-lg border border-slate-200 shadow-2xs">
                <div className="text-xl font-bold text-slate-900">{currentSub.evaluativeScore}%</div>
                <div className="text-[10px] text-slate-500 uppercase font-bold tracking-wider">Evaluative Exam</div>
              </div>
            </div>
          </div>

          {/* Primary 1-Click Reset Actions */}
          <div className="space-y-2.5">
            <span className="text-[11px] font-bold uppercase tracking-wider text-slate-500 block">
              1-Click Zero Reset (For Onboarding &amp; Diagnostic Testing)
            </span>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              <button
                type="button"
                onClick={handleResetActive}
                className="flex items-center justify-center gap-2 px-3 py-2.5 rounded-xl border border-rose-300 bg-rose-50 text-rose-800 hover:bg-rose-100 transition text-xs font-bold shadow-2xs cursor-pointer"
              >
                <RotateCcw className="w-3.5 h-3.5 text-rose-600" />
                <span>Reset {activeSubject} to 0%</span>
              </button>

              <button
                type="button"
                onClick={handleResetAll}
                className="flex items-center justify-center gap-2 px-3 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white transition text-xs font-bold shadow-xs cursor-pointer"
              >
                <RotateCcw className="w-3.5 h-3.5 text-white" />
                <span>Reset ALL to 0%</span>
              </button>
            </div>
          </div>

          {/* Simulation & Pacing Testing Presets */}
          <div className="space-y-2.5 pt-2 border-t border-slate-200">
            <span className="text-[11px] font-bold uppercase tracking-wider text-slate-500 block">
              Quick Calibration Presets (Test Progression Stages)
            </span>

            <div className="space-y-2">
              <button
                type="button"
                onClick={() => handleApplyPreset('new_0', 'New Learner (0% Baseline)')}
                className="w-full flex items-center justify-between p-2.5 rounded-xl bg-white border border-slate-200 hover:border-slate-300 transition text-xs font-semibold text-left cursor-pointer"
              >
                <div>
                  <div className="font-bold text-slate-900">0% New Learner Baseline</div>
                  <div className="text-[11px] text-slate-500">All subjects 0% • 0 dues • Triggers Diagnostic on next click</div>
                </div>
                <span className="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-bold text-[10px]">Apply</span>
              </button>

              <button
                type="button"
                onClick={() => handleApplyPreset('intermediate_50', 'Intermediate Learner (50% Mastery)')}
                className="w-full flex items-center justify-between p-2.5 rounded-xl bg-white border border-blue-200 hover:border-blue-300 transition text-xs font-semibold text-left cursor-pointer"
              >
                <div>
                  <div className="font-bold text-blue-900">50% Intermediate Learner</div>
                  <div className="text-[11px] text-slate-500">Unlocks Practice Mode • 3-Tier hints active • 3-day streak</div>
                </div>
                <span className="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold text-[10px]">Apply</span>
              </button>

              <button
                type="button"
                onClick={() => handleApplyPreset('exam_ready_85', 'Exam Ready (85% BKT Mastery)')}
                className="w-full flex items-center justify-between p-2.5 rounded-xl bg-white border border-emerald-200 hover:border-emerald-300 transition text-xs font-semibold text-left cursor-pointer"
              >
                <div>
                  <div className="font-bold text-emerald-900">85% Exam-Ready High Flyer</div>
                  <div className="text-[11px] text-slate-500">Unlocks Timed Exam Mode • Level 7 readiness • 7-day streak</div>
                </div>
                <span className="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold text-[10px]">Apply</span>
              </button>
            </div>
          </div>

          {/* Gamification Token Testing */}
          <div className="pt-2 border-t border-slate-200 flex items-center justify-between text-xs text-slate-600">
            <div className="flex items-center gap-3">
              <span className="flex items-center gap-1 font-bold text-amber-700">
                <Flame className="w-3.5 h-3.5 text-[#FF9100]" />
                {storeState.streakDays} Days
              </span>
              <span className="flex items-center gap-1 font-bold text-blue-700">
                <Zap className="w-3.5 h-3.5 text-blue-500" />
                {storeState.totalXp} XP
              </span>
            </div>
            <button
              type="button"
              onClick={() => {
                studentStore.saveState({
                  ...storeState,
                  streakDays: storeState.streakDays + 1,
                  totalXp: storeState.totalXp + 100
                });
                showToast('+1 Day Streak & +100 XP added');
              }}
              className="px-2.5 py-1 rounded-lg border border-slate-200 bg-slate-50 hover:bg-slate-100 text-slate-700 font-bold text-[11px] cursor-pointer"
            >
              +100 XP / +1 Day
            </button>
          </div>
        </div>

        {/* Footer */}
        <div className="px-5 py-3 bg-slate-50 border-t border-slate-200 flex items-center justify-end">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl bg-[#13519C] text-white text-xs font-bold hover:bg-blue-800 transition cursor-pointer"
          >
            Done
          </button>
        </div>

      </div>
    </div>
  );
}
