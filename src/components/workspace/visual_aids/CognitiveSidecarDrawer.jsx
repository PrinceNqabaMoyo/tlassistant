import React, { useEffect, useState } from 'react';
import { X, Compass, Sparkles, Loader2, BookOpen, Play, Layers } from 'lucide-react';
import { VISUAL_AIDS } from './visualAidRegistry';

const SimuLearnPlayer = React.lazy(() => import('../../simulearn/SimuLearnPlayer'));

/**
 * CognitiveSidecarDrawer — Unified 2-Tab Archetype Enhancement Companion
 * 
 * Implements Pillar 3 of the Unified Visual Architecture & Workspace Direction (v2.0):
 * - Tab 1: Annotated Master Atlas & Multi-Scale System Context (Full labeled anatomical/physical
 *   atlas, Micro <-> Macro zoom context, and interactive 2D/3D reference tools).
 * - Tab 2: Live Process & SimuLearn Step-by-Step Replay (Interactive parameter sliders,
 *   vector simulation, and step-by-step SimuLearn worked solution replay).
 */
export default function CognitiveSidecarDrawer({
  isOpen = false,
  onClose,
  availableAids = [],
  activeAidId,
  onSelectAid,
  activeQuestion = null,
  grade = null,
  subject = null,
  topic = null,
  simuLearnKey = 'accounting_crj_vat',
  initialCompanionTab = 'atlas',
  progressionMode = 'scaffold',
}) {
  const isExamLocked = progressionMode === 'assessment' || progressionMode === 'diagnostic';
  const [internalActiveId, setInternalActiveId] = useState(
    activeAidId || availableAids[0]?.id || 'aid_periodic_table'
  );
  const [companionTab, setCompanionTab] = useState(isExamLocked ? 'atlas' : (initialCompanionTab || 'atlas'));

  useEffect(() => {
    if (isExamLocked) {
      setCompanionTab('atlas');
    } else if (initialCompanionTab) {
      setCompanionTab(initialCompanionTab);
    }
  }, [initialCompanionTab, isOpen, isExamLocked]);

  useEffect(() => {
    if (activeAidId && availableAids.some((a) => a.id === activeAidId)) {
      setInternalActiveId(activeAidId);
    } else if (availableAids.length > 0) {
      setInternalActiveId(availableAids[0].id);
    }
  }, [activeAidId, availableAids]);

  // Handle Escape key to dismiss
  useEffect(() => {
    if (!isOpen) return;
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') {
        onClose?.();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const currentAid = VISUAL_AIDS[internalActiveId] || availableAids[0] || VISUAL_AIDS.aid_periodic_table;
  const ActiveComponent = currentAid.component;
  const CurrentIcon = currentAid.icon || Compass;

  const handleTabClick = (aidId) => {
    setInternalActiveId(aidId);
    onSelectAid?.(aidId);
  };

  return (
    <>
      {/* Semi-transparent Backdrop on Mobile only (Non-blocking companion on desktop) */}
      <div
        className="block sm:hidden fixed inset-0 bg-slate-900/40 backdrop-blur-xs z-40 transition-opacity"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Slide-out Drawer Container */}
      <aside
        data-testid="cognitive-sidecar-drawer"
        role="dialog"
        aria-label="Archetype Enhancement Companion Drawer"
        className="fixed top-0 right-0 bottom-0 z-50 w-full sm:w-[540px] md:w-[620px] bg-[#FAF8F3] shadow-2xl border-l border-[#EAE5DC] flex flex-col animate-in slide-in-from-right duration-200"
      >
        {/* Header */}
        <div className="p-3.5 bg-white border-b border-[#EAE5DC] flex items-center justify-between shrink-0">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-indigo-50 border border-indigo-200 flex items-center justify-center text-[#13519C]">
              <CurrentIcon className="w-4 h-4" />
            </div>
            <div>
              <div className="flex items-center gap-1.5">
                <span className="text-[10px] font-bold uppercase tracking-wider text-indigo-700 bg-indigo-50 px-1.5 py-0.2 rounded border border-indigo-200">
                  Archetype Enhancement Companion
                </span>
                <span className="text-[10px] text-slate-400 font-mono">
                  Never Graded
                </span>
              </div>
              <h3 className="text-sm font-bold text-[#1E2022] leading-tight">
                {companionTab === 'atlas' ? currentAid.title : `SimuLearn & Live Process • ${topic || currentAid.shortTitle || currentAid.title}`}
              </h3>
            </div>
          </div>

          <button
            data-testid="btn-close-sidecar"
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-slate-100 transition-colors cursor-pointer"
            title="Close companion (Esc)"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Primary 2-Tab Companion Switcher (Tab 1: Annotated Master Atlas | Tab 2: Live Process & SimuLearn) */}
        <div className="grid grid-cols-2 gap-1.5 px-3.5 py-2 bg-slate-100/90 border-b border-[#EAE5DC] shrink-0">
          <button
            type="button"
            data-testid="companion-tab-atlas"
            onClick={() => setCompanionTab('atlas')}
            className={`flex items-center justify-center gap-1.5 py-1.5 px-3 rounded-lg text-xs font-bold transition cursor-pointer ${
              companionTab === 'atlas'
                ? 'bg-[#13519C] text-white shadow-xs'
                : 'bg-white text-slate-700 border border-slate-200 hover:bg-slate-50'
            }`}
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>Tab 1: Annotated Master Atlas</span>
          </button>
          <button
            type="button"
            data-testid="companion-tab-simulation"
            disabled={isExamLocked}
            onClick={() => {
              if (!isExamLocked) setCompanionTab('simulation');
            }}
            className={`flex items-center justify-center gap-1.5 py-1.5 px-3 rounded-lg text-xs font-bold transition ${
              isExamLocked
                ? 'bg-slate-200/70 text-slate-400 cursor-not-allowed'
                : companionTab === 'simulation'
                ? 'bg-indigo-700 text-white shadow-xs cursor-pointer'
                : 'bg-white text-slate-700 border border-slate-200 hover:bg-slate-50 cursor-pointer'
            }`}
            title={
              isExamLocked
                ? 'Step-by-step process replays are locked during formal Exam & Diagnostic modes'
                : 'Open Live Process & SimuLearn Replay'
            }
          >
            <Play className="w-3.5 h-3.5" />
            <span>Tab 2: Live Process &amp; SimuLearn {isExamLocked ? '🔒' : ''}</span>
          </button>
        </div>

        {/* Sub-Aid Switcher if multiple aids available for this topic */}
        {companionTab === 'atlas' && availableAids.length > 1 && (
          <div className="flex items-center gap-1 px-3 py-1.5 bg-white border-b border-[#EAE5DC] overflow-x-auto shrink-0">
            {availableAids.map((aid) => {
              const Icon = aid.icon || Compass;
              const isActive = aid.id === internalActiveId;
              return (
                <button
                  key={aid.id}
                  data-testid={`tab-aid-${aid.id}`}
                  onClick={() => handleTabClick(aid.id)}
                  className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-semibold whitespace-nowrap transition-colors cursor-pointer ${
                    isActive
                      ? 'bg-indigo-50 text-[#13519C] shadow-2xs border border-indigo-200'
                      : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                  }`}
                >
                  <Icon className="w-3.5 h-3.5" />
                  <span>{aid.shortTitle || aid.title}</span>
                </button>
              );
            })}
          </div>
        )}

        {/* Scrollable Companion Body */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {companionTab === 'atlas' ? (
            <React.Suspense
              fallback={
                <div className="h-64 flex flex-col items-center justify-center gap-2 text-slate-500">
                  <Loader2 className="w-6 h-6 animate-spin text-[#13519C]" />
                  <span className="text-xs font-mono">Loading Master Atlas...</span>
                </div>
              }
            >
              <ActiveComponent activeQuestion={activeQuestion} grade={grade} />
            </React.Suspense>
          ) : (
            <div className="space-y-4">
              <React.Suspense
                fallback={
                  <div className="h-64 flex flex-col items-center justify-center gap-2 text-slate-500">
                    <Loader2 className="w-6 h-6 animate-spin text-indigo-600" />
                    <span className="text-xs font-mono">Loading SimuLearn Step-by-Step Replay...</span>
                  </div>
                }
              >
                <SimuLearnPlayer
                  isOpen={true}
                  embedded={true}
                  archetypeKey={simuLearnKey}
                  activeQuestion={activeQuestion}
                  subject={subject}
                  grade={grade}
                  topic={topic}
                  onComplete={() => setCompanionTab('atlas')}
                />
              </React.Suspense>
            </div>
          )}
        </div>

        {/* Drawer Footer Notice */}
        <div className="p-2.5 bg-white border-t border-[#EAE5DC] text-[11px] text-slate-600 flex items-center justify-between shrink-0">
          <span className="italic">
            Tip: Keep this companion open alongside your Paper Folio question while working.
          </span>
          <button
            onClick={onClose}
            className="text-xs font-bold text-[#13519C] hover:underline cursor-pointer"
          >
            Done
          </button>
        </div>
      </aside>
    </>
  );
}
