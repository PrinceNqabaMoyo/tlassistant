import React from 'react';
import { 
  ChevronDown, 
  ChevronRight, 
  PanelLeftClose, 
  PanelLeftOpen, 
  Settings, 
  Flame, 
  Zap, 
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
 * - Mutually exclusive accordions:
 *   * Self-Paced Learning: expands enrolled subjects list with glowing jewel dots; collapses when inactive.
 *   * School Classwork: expands homework list (2 Due); collapses when inactive.
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
  enabledSubjects = ['accounting', 'mathematics', 'technical_mathematics', 'mathematical_literacy', 'physical_sciences', 'life_sciences', 'business_studies'],
  onOpenManageSubjects = () => {},
  isCollapsed = false,
  onToggleCollapse = () => {},
  assignedTasks = [
    { id: 'task_acc_1', subject: 'accounting', subjectName: 'Accounting', dueTime: '17:00' },
    { id: 'task_math_1', subject: 'mathematics', subjectName: 'Mathematics', dueTime: '08:00' }
  ],
}) {
  const isSeniorPhase = currentGrade <= 9;
  const fullPhaseList = isSeniorPhase ? ALL_SENIOR_PHASE_SUBJECTS : ALL_FET_PHASE_SUBJECTS;
  
  // Filter by enabled subjects
  const enrolledSubjects = fullPhaseList.filter(s => enabledSubjects.includes(s.id));
  const activeCount = enrolledSubjects.length;
  const totalCount = fullPhaseList.length;

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
            {/* Brand Header */}
            <div className="p-3.5 border-b border-slate-800/80 flex items-center justify-between">
              <div className="flex items-center gap-2.5">
                <div className="w-7 h-7 rounded-lg bg-[#FF9100] text-[#0B2545] font-black flex items-center justify-center text-sm shadow-md">
                  🎓
                </div>
                <div>
                  <h2 className="text-xs font-bold text-white tracking-tight font-display">FUNDILE</h2>
                  <p className="text-[10px] text-slate-400 truncate max-w-[140px]">{schoolName}</p>
                </div>
              </div>
              <button 
                type="button"
                onClick={onToggleCollapse} 
                className="text-slate-400 hover:text-white p-1 rounded-md hover:bg-slate-800 transition cursor-pointer text-xs" 
                title="Collapse Sidebar"
              >
                <PanelLeftClose className="w-4 h-4" />
              </button>
            </div>

            {/* Student Mini-Profile & Stats Card */}
            <div className="p-3 bg-white/5 border border-slate-800/60 m-2 rounded-xl">
              <div className="flex items-center justify-between text-xs">
                <span className="font-bold text-white text-[11px] truncate max-w-[130px]">{studentName}</span>
                <span className="text-[10px] text-emerald-400 font-semibold bg-emerald-500/10 px-1.5 py-0.5 rounded border border-emerald-500/20 shrink-0">
                  Gr {currentGrade} {isSeniorPhase ? 'Senior' : 'FET'}
                </span>
              </div>
              <div className="grid grid-cols-2 gap-2 mt-2 pt-2 border-t border-slate-700/40 text-[11px]">
                <div className="flex items-center gap-1.5 text-amber-300 font-bold">
                  <Flame className="w-3.5 h-3.5 text-[#FF9100] fill-[#FF9100]" />
                  <span>{streakDays}d Streak</span>
                </div>
                <div className="flex items-center gap-1.5 text-blue-300 font-bold">
                  <Zap className="w-3.5 h-3.5 text-blue-400" />
                  <span>{xp > 999 ? `${(xp / 1000).toFixed(1)}k` : xp} XP</span>
                </div>
              </div>
            </div>

            {/* ACCORDION NAVIGATION */}
            <div className="px-2 py-2 space-y-2">
              
              {/* ───────────────────────────────────────────────────────── */}
              {/* ACCORDION 1: SELF-PACED LEARNING (Priority Default View)  */}
              {/* ───────────────────────────────────────────────────────── */}
              <div className="space-y-1">
                <button
                  type="button"
                  onClick={() => {
                    onSelectDeskMode('self_paced');
                    if (activeTab !== 'desk') {
                      onSelectSubject('desk');
                    }
                  }}
                  className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-bold transition cursor-pointer ${
                    isSelfPacedActive
                      ? 'bg-[#13519C] text-white shadow-sm'
                      : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
                  }`}
                >
                  <div className="flex items-center gap-2">
                    <Target className="w-3.5 h-3.5 text-emerald-400" />
                    <span>Self-Paced Learning</span>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-white/20 text-white">
                      Core
                    </span>
                    {isSelfPacedActive ? (
                      <ChevronDown className="w-3 h-3 text-white/80" />
                    ) : (
                      <ChevronRight className="w-3 h-3 text-slate-400" />
                    )}
                  </div>
                </button>

                {/* Nested Enrolled Subjects (Shown only when Self-Paced is Active) */}
                {isSelfPacedActive && (
                  <div className="pl-3 pr-1 py-1 space-y-0.5 border-l-2 border-blue-500/40 ml-4 animate-fadeIn">
                    {enrolledSubjects.map((s) => {
                      const theme = getSubjectTheme(s.id);
                      const isSelected = (activeTab === s.id) || (activeTab === 'desk' && activeReelSubjectId === s.id);
                      
                      return (
                        <button
                          key={s.id}
                          type="button"
                          onClick={() => onSelectSubject(s.id)}
                          className={`w-full flex items-center justify-between px-2.5 py-1.5 rounded-lg text-xs font-medium transition cursor-pointer ${
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
                            BKT
                          </span>
                        </button>
                      );
                    })}
                  </div>
                )}
              </div>

              {/* ───────────────────────────────────────────────────────── */}
              {/* ACCORDION 2: SCHOOL CLASSWORK (Focused Homework Diary)    */}
              {/* ───────────────────────────────────────────────────────── */}
              <div className="space-y-1 pt-1">
                <button
                  type="button"
                  onClick={() => {
                    onSelectDeskMode('classwork');
                    if (activeTab !== 'desk') {
                      onSelectSubject('desk');
                    }
                  }}
                  className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-medium transition cursor-pointer ${
                    isClassworkActive
                      ? 'bg-[#13519C] text-white font-bold shadow-sm'
                      : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
                  }`}
                >
                  <div className="flex items-center gap-2">
                    <Briefcase className="w-3.5 h-3.5 text-amber-400" />
                    <span>School Classwork</span>
                  </div>
                  <div className="flex items-center gap-1.5">
                    {assignedTasks.length > 0 && (
                      <span className="text-[10px] font-extrabold px-1.5 py-0.5 rounded-full bg-rose-500 text-white shadow-xs">
                        {assignedTasks.length} Due
                      </span>
                    )}
                    {isClassworkActive ? (
                      <ChevronDown className="w-3 h-3 text-white/80" />
                    ) : (
                      <ChevronRight className="w-3 h-3 text-slate-400" />
                    )}
                  </div>
                </button>

                {/* Nested Homework Subjects (Shown only when Classwork is Active) */}
                {isClassworkActive && (
                  <div className="pl-3 pr-1 py-1 space-y-0.5 border-l-2 border-rose-500/40 ml-4 animate-fadeIn">
                    {assignedTasks.map((task) => {
                      const theme = getSubjectTheme(task.subject);
                      return (
                        <button
                          key={task.id}
                          type="button"
                          onClick={() => {
                            onSelectDeskMode('classwork');
                            onSelectSubject('desk');
                          }}
                          className="w-full flex items-center justify-between px-2.5 py-1.5 rounded-lg text-xs font-medium text-slate-300 hover:text-white hover:bg-slate-800/60 transition cursor-pointer"
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
                    })}
                  </div>
                )}
              </div>

            </div>

            {/* Manage Phase Subjects Button */}
            <div className="px-3 pt-3">
              <button
                type="button"
                onClick={onOpenManageSubjects}
                className="w-full py-2 px-3 rounded-xl text-xs font-bold bg-white/5 hover:bg-white/10 text-slate-300 hover:text-white border border-slate-700/60 transition flex items-center justify-between cursor-pointer shadow-2xs group"
                title="Manage active phase subjects"
              >
                <div className="flex items-center gap-2">
                  <Settings className="w-3.5 h-3.5 text-amber-400 group-hover:rotate-45 transition-transform" />
                  <span>Manage Subjects</span>
                </div>
                <span className="text-[10px] bg-slate-800 text-slate-400 px-1.5 py-0.5 rounded font-mono">
                  {activeCount}/{totalCount}
                </span>
              </button>
            </div>

          </div>

          {/* Sidebar Footer */}
          <div className="p-3 border-t border-slate-800 text-[11px] text-slate-400 space-y-1">
            <div className="flex items-center justify-between">
              <span className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                <span>Offline Cache</span>
              </span>
              <span className="text-emerald-400 font-bold">Ready ✓</span>
            </div>
            <div className="text-[10px] text-slate-500">&lt; 2 MB Data • Instant Loading</div>
          </div>

        </div>
      </aside>
    </>
  );
}
