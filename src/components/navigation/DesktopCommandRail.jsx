import React, { useState } from 'react';
import { 
  ChevronDown, 
  ChevronRight, 
  PanelLeftClose, 
  PanelLeftOpen, 
  Settings, 
  CheckCircle2, 
  Target, 
  Briefcase 
} from 'lucide-react';
import { getSubjectTheme } from '../../theme/subjectPalette';
import { ALL_FET_PHASE_SUBJECTS, ALL_SENIOR_PHASE_SUBJECTS } from '../curriculum/SubjectManagerModal';

/**
 * DesktopCommandRail (Option A Navigation Rail)
 * Smoothly collapsible full-height left navigation column.
 * 
 * Invariants:
 * - Collapses completely to w-0 (smooth transition, zero residual width or borders).
 * - Fixed inner width (w-64) prevents layout jank and wrapping during width animation.
 * - Floating trigger button allows instant re-opening when collapsed.
 * - Independently expandable accordions:
 *   * Self-Paced Learning: expands enrolled subjects list; maintains its state independently.
 *   * School Classwork: displays homework or independent account statement; maintains its state independently.
 */

export default function DesktopCommandRail({
  activeTab = 'desk',
  activeReelSubjectId = 'accounting',
  onSelectSubject = () => {},
  activeDeskMode = 'self_paced', // 'self_paced' | 'classwork'
  onSelectDeskMode = () => {},
  currentGrade = 10,
  schoolName = 'Westville High School',
  studentName = 'Prince Moyo',
  streakDays = 5,
  xp = 1420,
  enabledSubjects = ['accounting', 'mathematics', 'physical_sciences', 'life_sciences'],
  isIndependent = false,
  onOpenManageSubjects = () => {},
  onOpenOfflinePacks = () => {},
  isCollapsed = false,
  onToggleCollapse = () => {},
  assignedTasks = [],
}) {
  const isSeniorPhase = currentGrade <= 9;
  const fullPhaseList = isSeniorPhase ? ALL_SENIOR_PHASE_SUBJECTS : ALL_FET_PHASE_SUBJECTS;
  
  // Filter by enabled subjects
  const enrolledSubjects = fullPhaseList.filter(s => enabledSubjects.includes(s.id));
  const activeCount = enrolledSubjects.length;
  const totalCount = fullPhaseList.length;

  const [isSelfPacedOpen, setIsSelfPacedOpen] = useState(true);
  const [isClassworkOpen, setIsClassworkOpen] = useState(activeDeskMode === 'classwork');

  const isSelfPacedActive = activeDeskMode === 'self_paced' || activeTab !== 'desk';
  const isClassworkActive = activeDeskMode === 'classwork' && activeTab === 'desk';

  return (
    <>
      {/* 1. FLOATING EXPAND TRIGGER BUTTON (Visible when rail is collapsed) */}
      {isCollapsed && (
        <button
          type="button"
          onClick={onToggleCollapse}
          className="fixed top-3 left-3 z-40 px-3 py-2 bg-[#081326] text-white rounded-xl shadow-xl border border-slate-700/80 hover:bg-[#13519C] hover:scale-105 active:scale-95 transition-all flex items-center gap-2 cursor-pointer group text-xs font-bold font-sans"
          title="Expand Command Rail (Sidebar)"
        >
          <PanelLeftOpen className="w-4 h-4 text-[#FF9100] group-hover:rotate-12 transition-transform" />
          <span className="hidden sm:inline">Sidebar</span>
        </button>
      )}

      {/* 2. THE MAIN COMMAND RAIL ASIDE */}
      <aside
        className={`bg-gradient-to-b from-[#081326] to-[#0A1933] text-white shrink-0 flex flex-col justify-between transition-all duration-300 ease-in-out select-none font-sans ${
          isCollapsed 
            ? 'w-0 opacity-0 pointer-events-none border-r-0' 
            : 'w-64 opacity-100 border-r border-slate-800 shadow-xl'
        } overflow-hidden relative z-30`}
      >
        {/* Fixed-width inner container guarantees smooth curtain slide without text re-wrap */}
        <div className="w-64 flex flex-col h-full justify-between">
          
          <div className="overflow-y-auto overflow-x-hidden flex-1">
            {/* Top Line: Learner Name & Grade + Collapse Trigger */}
            <div className="p-3.5 border-b border-slate-800/80 flex items-center justify-between">
              <div className="flex items-center gap-2 min-w-0">
                <span className="font-bold text-white text-xs truncate max-w-[130px]" title={studentName}>
                  {studentName}
                </span>
                <span className="text-[10px] text-emerald-400 font-semibold bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20 shrink-0 font-mono">
                  Gr {currentGrade} {isSeniorPhase ? 'Senior' : 'FET'}
                </span>
              </div>
              <button 
                type="button"
                data-testid="btn-collapse-sidebar"
                onClick={onToggleCollapse} 
                className="text-slate-400 hover:text-white p-1 rounded-md hover:bg-slate-800 transition cursor-pointer text-xs shrink-0" 
                title="Collapse Sidebar"
              >
                <PanelLeftClose className="w-4 h-4" />
              </button>
            </div>

            {/* ACCORDION NAVIGATION */}
            <div className="px-2 py-2 space-y-2">
              
              {/* ───────────────────────────────────────────────────────── */}
              {/* ACCORDION 1: SELF-PACED LEARNING (Priority Default View)  */}
              {/* ───────────────────────────────────────────────────────── */}
              <div className="space-y-1">
                <div
                  className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-bold transition ${
                    isSelfPacedActive
                      ? 'bg-[#13519C] text-white shadow-sm'
                      : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
                  }`}
                >
                  <button
                    type="button"
                    data-testid="tab-desk"
                    onClick={() => {
                      onSelectDeskMode('self_paced');
                      if (activeTab !== 'desk') {
                        onSelectSubject('desk');
                      }
                      setIsSelfPacedOpen(true);
                    }}
                    className="flex items-center gap-2 flex-1 text-left cursor-pointer truncate"
                  >
                    <Target className="w-3.5 h-3.5 text-emerald-400 shrink-0" />
                    <span className="truncate">Self-Paced Learning</span>
                  </button>
                  <div className="flex items-center gap-1.5 shrink-0">
                    <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-white/20 text-white">
                      Core
                    </span>
                    <button
                      type="button"
                      data-testid="btn-toggle-self-paced"
                      onClick={() => setIsSelfPacedOpen((prev) => !prev)}
                      className="p-1 rounded hover:bg-white/20 transition cursor-pointer text-white/80 hover:text-white"
                      title={isSelfPacedOpen ? 'Collapse self-paced subjects' : 'Expand self-paced subjects'}
                      aria-label="Toggle Self-Paced subjects"
                    >
                      {isSelfPacedOpen ? (
                        <ChevronDown className="w-3.5 h-3.5" />
                      ) : (
                        <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
                      )}
                    </button>
                  </div>
                </div>

                {/* Nested Enrolled Subjects (Independent dropdown) */}
                {isSelfPacedOpen && (
                  <div className="pl-3 pr-1 py-1 space-y-0.5 border-l-2 border-blue-500/40 ml-4 animate-fadeIn">
                    {enrolledSubjects.map((s) => {
                      const theme = getSubjectTheme(s.id);
                      const isSelected = (activeTab === s.id) || (activeTab === 'desk' && activeReelSubjectId === s.id);
                      
                      return (
                        <button
                          key={s.id}
                          type="button"
                          data-testid={`tab-${s.id}`}
                          onClick={() => onSelectSubject(s.id)}
                          className={`w-full min-h-[34px] flex items-center justify-between px-3 py-1.5 rounded-lg text-xs font-medium transition cursor-pointer ${
                            isSelected 
                              ? 'bg-blue-600/30 text-white font-bold border border-blue-400/40 shadow-xs' 
                              : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
                          }`}
                        >
                          <div className="flex items-center gap-2 truncate">
                            <span 
                              className="w-2.5 h-2.5 rounded-full shrink-0 transition-transform"
                              style={{ 
                                backgroundColor: theme.base,
                                boxShadow: isSelected ? theme.glowSm : 'none'
                              }} 
                            />
                            <span className="truncate">{s.short}</span>
                          </div>
                          <span 
                            className="text-[10px] font-bold px-1.5 py-0.5 rounded shrink-0"
                            style={{
                              backgroundColor: theme.soft,
                              color: theme.text
                            }}
                          >
                            Active
                          </span>
                        </button>
                      );
                    })}

                    {/* Ergonomic Placement: Manage Enrolled Subjects directly under the subject list */}
                    <div className="pt-1">
                      <button
                        type="button"
                        data-testid="btn-manage-enrolled-subjects"
                        onClick={onOpenManageSubjects}
                        className="w-full py-1.5 px-2.5 rounded-lg text-[11px] font-semibold text-slate-300 hover:text-white hover:bg-white/10 border border-slate-700/70 transition flex items-center justify-between cursor-pointer group shadow-2xs"
                        title="Add or remove self-paced curriculum subjects"
                      >
                        <div className="flex items-center gap-1.5 truncate">
                          <Settings className="w-3.5 h-3.5 text-amber-400 group-hover:rotate-45 transition-transform shrink-0" />
                          <span className="truncate">Manage Subjects</span>
                        </div>
                        <span className="text-[10px] bg-slate-800 text-slate-300 px-1.5 py-0.2 rounded font-mono shrink-0">
                          {activeCount}/{totalCount}
                        </span>
                      </button>
                    </div>
                  </div>
                )}
              </div>

              {/* ───────────────────────────────────────────────────────── */}
              {/* ACCORDION 2: SCHOOL CLASSWORK (Focused Homework Diary)    */}
              {/* ───────────────────────────────────────────────────────── */}
              <div className="space-y-1 pt-1">
                <div
                  className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-medium transition ${
                    isClassworkActive
                      ? 'bg-[#13519C] text-white font-bold shadow-sm'
                      : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
                  }`}
                >
                  <button
                    type="button"
                    data-testid="tab-classwork"
                    onClick={() => {
                      onSelectDeskMode('classwork');
                      if (activeTab !== 'desk') {
                        onSelectSubject('desk');
                      }
                      setIsClassworkOpen(true);
                    }}
                    className="flex items-center gap-2 flex-1 text-left cursor-pointer truncate"
                  >
                    <Briefcase className="w-3.5 h-3.5 text-amber-400 shrink-0" />
                    <span className="truncate">School Classwork</span>
                  </button>
                  <div className="flex items-center gap-1.5 shrink-0">
                    {!isIndependent && assignedTasks.length > 0 && (
                      <span className="text-[10px] font-extrabold px-1.5 py-0.5 rounded-full bg-rose-500 text-white shadow-xs">
                        {assignedTasks.length} Due
                      </span>
                    )}
                    {isIndependent && (
                      <span className="text-[9px] font-bold px-1.5 py-0.5 rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">
                        Independent
                      </span>
                    )}
                    <button
                      type="button"
                      data-testid="btn-toggle-classwork"
                      onClick={() => setIsClassworkOpen((prev) => !prev)}
                      className="p-1 rounded hover:bg-white/20 transition cursor-pointer text-white/80 hover:text-white"
                      title={isClassworkOpen ? 'Collapse classwork list' : 'Expand classwork list'}
                      aria-label="Toggle School Classwork list"
                    >
                      {isClassworkOpen ? (
                        <ChevronDown className="w-3.5 h-3.5" />
                      ) : (
                        <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
                      )}
                    </button>
                  </div>
                </div>

                {/* Nested Homework Subjects or Independent Status (Independent dropdown) */}
                {isClassworkOpen && (
                  <div className="pl-3 pr-1 py-1 space-y-0.5 border-l-2 border-amber-500/40 ml-4 animate-fadeIn">
                    {isIndependent ? (
                      <div className="p-2.5 rounded-xl bg-purple-950/40 border border-purple-500/30 text-[11px] text-purple-200 space-y-1">
                        <div className="font-bold flex items-center gap-1.5 text-purple-300">
                          <span>🏡</span>
                          <span>Independent Account</span>
                        </div>
                        <p className="text-[10px] text-slate-300 leading-relaxed">
                          Not linked to any school or institution. Your learning is 100% self-paced with zero homework deadlines.
                        </p>
                      </div>
                    ) : assignedTasks.length === 0 ? (
                      <p className="text-[11px] text-slate-400 italic px-2 py-1">
                        No pending school assignments.
                      </p>
                    ) : (
                      assignedTasks.map((task) => {
                        const theme = getSubjectTheme(task.subject);
                        return (
                          <button
                            key={task.id}
                            type="button"
                            onClick={() => {
                              onSelectDeskMode('classwork');
                              onSelectSubject('desk');
                            }}
                            className="w-full min-h-[34px] flex items-center justify-between px-3 py-1.5 rounded-lg text-xs font-medium text-slate-300 hover:text-white hover:bg-slate-800/60 transition cursor-pointer"
                          >
                            <div className="flex items-center gap-2 truncate">
                              <span 
                                className="w-2.5 h-2.5 rounded-full shrink-0" 
                                style={{ 
                                  backgroundColor: theme.base,
                                  boxShadow: theme.glowSm
                                }} 
                              />
                              <span className="truncate">{task.subjectName || task.subject}</span>
                            </div>
                            <span className="text-[9px] font-extrabold px-1.5 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30 shrink-0">
                              {task.dueTime}
                            </span>
                          </button>
                        );
                      })
                    )}
                  </div>
                )}
              </div>

            </div>

          </div>

          {/* Sidebar Footer */}
          <div className="p-3 border-t border-slate-800 text-[11px] text-slate-400">
            <button
              type="button"
              data-testid="btn-rail-offline-packs"
              onClick={onOpenOfflinePacks}
              className="w-full text-left space-y-1 hover:bg-white/5 p-1.5 rounded-lg transition cursor-pointer group"
              title="Manage 30-Day Offline Study Packs"
            >
              <div className="flex items-center justify-between">
                <span className="flex items-center gap-1.5 text-slate-300 group-hover:text-white">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                  <span>Offline Packs</span>
                </span>
                <span className="text-emerald-400 font-bold group-hover:underline">Ready ✓</span>
              </div>
              <div className="text-[10px] text-slate-500">&lt; 2 MB Data • Instant Loading</div>
            </button>
          </div>

        </div>
      </aside>
    </>
  );
}
