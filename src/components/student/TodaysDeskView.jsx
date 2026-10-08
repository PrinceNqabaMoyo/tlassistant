import React, { useState, useEffect } from 'react';
import studentStore, { getTimeGreeting } from '../../services/studentStore';
import { 
  ClipboardCheck, 
  Calendar, 
  Clock, 
  ArrowRight, 
  BookOpen, 
  Calculator, 
  Flame, 
  Zap, 
  WifiOff, 
  CheckCircle2, 
  TrendingUp,
  AlertCircle
} from 'lucide-react';
import { getSubjectTheme } from '../../theme/subjectPalette';

/**
 * TodaysDeskView
 * Action Dashboard rendered when the learner is on Tab 0 ("Today's Desk").
 * Eliminates redundant card drilling: learners immediately see teacher tasks,
 * autonomous quick-resumes, and diagnostic benchmarks.
 */

export default function TodaysDeskView({
  studentName = 'Nqobile Dlamini',
  grade = 10,
  schoolName = 'Westville High School',
  currentUser = null,
  streakDays = 5,
  xp = 1420,
  onOpenSubject = () => {},
  _onStartBenchmark = () => {},
  onOpenLinkGuardian = () => {},
}) {
  const [storeState, setStoreState] = useState(() => studentStore.getState());
  const [activeDeskSection, setActiveDeskSection] = useState('school_work'); // 'school_work' | 'self_study'

  useEffect(() => {
    const unsub = studentStore.subscribe((newState) => {
      setStoreState({ ...newState });
    });
    return unsub;
  }, []);

  const effectiveUser = currentUser || storeState.currentUser;
  const isIndependent = Boolean(effectiveUser?.isIndependent);
  const assignedTasks = isIndependent
    ? []
    : (effectiveUser?.assignedTasks || storeState?.currentUser?.assignedTasks || [
        {
          id: 'task_acc_1',
          subject: 'accounting',
          subjectName: 'Accounting',
          title: 'General Journal: Debtors & Bad Debts',
          assignedBy: 'Mrs. P. Khumalo',
          dueText: 'DUE TODAY',
          dueTime: '17:00',
          marks: 12,
          notes: 'Mrs. Khumalo assigned 12 marks practice (J. Dlamini dividend).',
          estimatedMins: 15
        },
        {
          id: 'task_math_1',
          subject: 'mathematics',
          subjectName: 'Mathematics',
          title: 'Trinomial Factorisation Drill',
          assignedBy: 'Mr. J. Botha',
          dueText: 'DUE FRIDAY',
          dueTime: '08:00',
          marks: 10,
          notes: 'Mr. Botha • 10 Marks • Friday test prep.',
          estimatedMins: 12
        }
      ]);
  const deskDues = assignedTasks.length;
  const hasUnviewedTasks = assignedTasks.some(t => studentStore.isTaskUnviewed(t.id));
  const physSub = studentStore.getSubject('physical_sciences');
  const busSub = studentStore.getSubject('business_studies');
  const lifeSub = studentStore.getSubject('life_sciences');
  return (
    <div className="p-4 sm:p-8 bg-slate-50 min-h-[560px] space-y-6 animate-fadeIn font-sans">
      
      {/* 1. Welcome & Pacing Banner with Demystified Gamification */}
      <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight font-display">
            {getTimeGreeting()}, {studentName}. {deskDues > 0 ? `You have ${deskDues} school assignment${deskDues === 1 ? '' : 's'} scheduled.` : 'All school assignments are up to date!'}
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 mt-1">
            Complete your scheduled School Work or practice autonomously in Self-Study.
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-2">
          {/* Study Streak Demystified Pill */}
          <div 
            className="group relative text-xs font-bold text-amber-900 bg-amber-50 hover:bg-amber-100 px-3 py-1.5 rounded-xl border border-amber-300 flex items-center gap-1.5 transition-colors cursor-help shadow-2xs"
            title="Study Streak: Days in a row you have completed exercises on Fundile"
          >
            <Flame className="w-3.5 h-3.5 text-[#FF9100] fill-[#FF9100]" />
            <span>{streakDays}d Streak</span>
            <div className="absolute bottom-full right-0 mb-2 hidden group-hover:flex flex-col w-56 p-2.5 bg-slate-900 text-white text-[11px] font-normal rounded-xl shadow-xl pointer-events-none z-30">
              <span className="font-bold text-amber-400">🔥 Study Streak</span>
              <span>Consecutive active study days. Complete at least one learning exercise daily to keep your streak alive!</span>
            </div>
          </div>

          {/* Mastery XP Demystified Pill */}
          <div 
            className="group relative text-xs font-bold text-[#13519C] bg-blue-50 hover:bg-blue-100 px-3 py-1.5 rounded-xl border border-blue-200 flex items-center gap-1.5 transition-colors cursor-help shadow-2xs"
            title="Mastery XP: Experience points earned for verified concept and procedural accuracy"
          >
            <Zap className="w-3.5 h-3.5 text-[#13519C]" />
            <span>{xp > 999 ? `${(xp / 1000).toFixed(1)}k` : xp} XP</span>
            <div className="absolute bottom-full right-0 mb-2 hidden group-hover:flex flex-col w-56 p-2.5 bg-slate-900 text-white text-[11px] font-normal rounded-xl shadow-xl pointer-events-none z-30">
              <span className="font-bold text-blue-300">⚡ Mastery XP</span>
              <span>Points earned for step accuracy and verified concept mastery without rote guessing.</span>
            </div>
          </div>

          <button
            type="button"
            onClick={onOpenLinkGuardian}
            className="text-xs font-bold text-[#13519C] bg-blue-50 hover:bg-blue-100 px-3.5 py-1.5 rounded-xl border border-blue-200 flex items-center gap-1.5 transition-colors cursor-pointer shadow-xs"
            title="Generate a temporary 15-minute passcode to link with parent or guardian"
          >
            <span>🔗</span>
            <span>Link Parent</span>
          </button>
          <span className="text-xs font-bold text-slate-700 bg-slate-100 px-3 py-1.5 rounded-xl border border-slate-200 flex items-center gap-1.5">
            <Calendar className="w-3.5 h-3.5 text-[#13519C]" />
            <span>Grade {grade} • {schoolName}</span>
          </span>
        </div>
      </div>

      {/* 2. Section Toggle Switch: School Work vs Self-Study */}
      <div className="flex items-center gap-2 p-1 bg-slate-200/80 rounded-2xl max-w-sm">
        <button
          type="button"
          onClick={() => setActiveDeskSection('school_work')}
          className={`flex-1 py-2 px-4 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer flex items-center justify-center gap-2 ${
            activeDeskSection === 'school_work'
              ? 'bg-white text-[#13519C] shadow-sm'
              : 'text-slate-600 hover:text-slate-900'
          }`}
        >
          <span>🎒 School Work</span>
          {deskDues > 0 && (
            <span className={`px-2 py-0.5 rounded-full text-[10px] font-extrabold ${
              hasUnviewedTasks 
                ? 'bg-rose-500 text-white animate-pulse'
                : 'bg-blue-100 text-[#13519C]'
            }`}>
              {deskDues}
            </span>
          )}
        </button>

        <button
          type="button"
          onClick={() => setActiveDeskSection('self_study')}
          className={`flex-1 py-2 px-4 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer flex items-center justify-center gap-2 ${
            activeDeskSection === 'self_study'
              ? 'bg-white text-emerald-800 shadow-sm'
              : 'text-slate-600 hover:text-slate-900'
          }`}
        >
          <span>📖 Self-Study</span>
          <span className="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[10px] font-extrabold">
            4 Active
          </span>
        </button>
      </div>

      {/* 3. Section Content Display */}
      {activeDeskSection === 'school_work' && (
        <div className="space-y-4 animate-fadeIn">
          <div className="flex items-center justify-between">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 flex items-center gap-2">
              {hasUnviewedTasks && (
                <span className="relative flex h-2.5 w-2.5">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-rose-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-rose-500"></span>
                </span>
              )}
              <span>School Work &amp; Teacher Assignments</span>
            </h3>
            {deskDues > 0 ? (
              <span className={`text-xs font-bold px-2.5 py-0.5 rounded-md border ${
                hasUnviewedTasks
                  ? 'text-rose-700 bg-rose-50 border-rose-300 animate-pulse'
                  : 'text-blue-700 bg-blue-50 border-blue-200'
              }`}>
                {deskDues} Assignment{deskDues === 1 ? '' : 's'}
              </span>
            ) : (
              <span className="text-xs text-emerald-700 font-bold bg-emerald-50 px-2.5 py-0.5 rounded-md border border-emerald-200">
                All Caught Up
              </span>
            )}
          </div>

          {isIndependent ? (
            <div className="bg-purple-50/90 border border-purple-200 p-6 rounded-2xl shadow-xs space-y-2 text-center">
              <span className="text-2xl">🏡</span>
              <h4 className="text-sm font-bold text-purple-900 font-display">
                Independent Homeschool Path • Self-Paced CAPS Study Plan
              </h4>
              <p className="text-xs text-purple-700 max-w-lg mx-auto">
                Zero school homework deadlines assigned. Switch to Self-Study to practice and master topics autonomously.
              </p>
            </div>
          ) : assignedTasks.length === 0 ? (
            <div className="bg-emerald-50/80 border border-emerald-200 p-6 rounded-2xl shadow-xs text-center space-y-2">
              <div className="w-10 h-10 rounded-full bg-emerald-100 text-emerald-700 mx-auto flex items-center justify-center text-lg font-bold shadow-2xs">
                ✓
              </div>
              <h4 className="text-sm font-bold text-emerald-900 font-display">
                All Caught Up!
              </h4>
              <p className="text-xs text-emerald-700 max-w-md mx-auto">
                No pending school work right now. Switch to Self-Study to practice autonomously and boost your Mastery Dial.
              </p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {assignedTasks.map((task) => {
                const theme = getSubjectTheme(task.subject);
                const isAccounting = (task.subject || '').includes('accounting');
                const isUnviewed = studentStore.isTaskUnviewed(task.id);

                return (
                  <div 
                    key={task.id} 
                    className={`p-5 rounded-2xl shadow-xs hover:shadow-md transition-all space-y-3 ${
                      isUnviewed
                        ? 'bg-rose-50/70 border-2 border-rose-300 ring-2 ring-rose-200/70'
                        : 'bg-white border border-slate-200'
                    }`}
                    style={{ borderLeftWidth: '5px', borderLeftColor: theme.base }}
                  >
                    <div className="flex items-center justify-between text-xs font-bold">
                      <span 
                        className="px-2.5 py-1 rounded-full text-[11px] font-extrabold shadow-sm flex items-center gap-1.5 text-white"
                        style={{ backgroundColor: theme.base }}
                      >
                        {isAccounting ? <BookOpen className="w-3.5 h-3.5" /> : <Calculator className="w-3.5 h-3.5" />}
                        <span>{(task.subjectName || task.subject).toUpperCase()} • {task.dueText || 'DUE SOON'}</span>
                      </span>

                      <div className="flex items-center gap-1.5">
                        {isUnviewed && (
                          <span className="text-[10px] font-extrabold text-rose-700 bg-white px-2 py-0.5 rounded-full border border-rose-300 animate-pulse">
                            NEW
                          </span>
                        )}
                        <span className="bg-rose-500 text-white px-2.5 py-0.5 rounded-full text-[11px] font-extrabold shadow-sm shadow-rose-500/30">
                          {task.dueTime || '17:00'}
                        </span>
                      </div>
                    </div>

                    <div>
                      <h4 className="text-base font-bold text-slate-900 font-display">
                        {task.title}
                      </h4>
                      <p className="text-xs text-slate-600 mt-1">
                        Assigned by {task.assignedBy || task.teacherName || 'Faculty'} • {task.marks || 10} Marks • {task.notes || task.description || 'Targeted CAPS practice.'}
                      </p>
                    </div>

                    <div className="pt-2 flex items-center justify-between border-t border-slate-100">
                      <span 
                        className="text-xs font-semibold px-2 py-0.5 rounded-md"
                        style={{ backgroundColor: theme.soft, color: theme.text }}
                      >
                        Estimated: {task.estimatedMins || 15} mins
                      </span>
                      <button
                        type="button"
                        onClick={() => {
                          studentStore.markTaskViewed(task.id);
                          onOpenSubject(task.subject, task.topic || task.title);
                        }}
                        className="px-4 py-2 text-white text-xs font-bold rounded-xl shadow-sm flex items-center gap-1.5 transition cursor-pointer hover:opacity-95 active:scale-98"
                        style={{ backgroundColor: theme.base }}
                      >
                        <span>Open in {task.subjectName || 'Subject'}</span>
                        <ArrowRight className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}

      {/* Self-Study Section */}
      {activeDeskSection === 'self_study' && (
        <div className="space-y-4 animate-fadeIn">
          <div className="flex items-center justify-between">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 flex items-center gap-2">
              <TrendingUp className="w-3.5 h-3.5 text-emerald-600" />
              <span>Self-Study &amp; Autonomous Mastery</span>
            </h3>
            <span className="text-xs text-emerald-700 font-bold bg-emerald-50 px-2.5 py-0.5 rounded-md border border-emerald-200">
              BKT Calibrated
            </span>
          </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
          {(() => {
            const physTheme = getSubjectTheme('physical_sciences');
            const isPhysDiag = physSub.status === 'diagnostic_required';
            return (
              <div 
                className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs space-y-2 hover:shadow-xs transition"
                style={{ borderLeftWidth: '4px', borderLeftColor: physTheme.base }}
              >
                <div className="flex items-center justify-between text-xs">
                  <span className="font-bold text-slate-800">Physical Sciences</span>
                  <span 
                    className="font-bold px-2 py-0.5 rounded-full text-[11px]"
                    style={{
                      backgroundColor: isPhysDiag ? physTheme.soft : physTheme.base,
                      color: isPhysDiag ? physTheme.text : '#FFFFFF',
                      border: isPhysDiag ? `1px solid ${physTheme.border}` : 'none'
                    }}
                  >
                    {isPhysDiag ? 'Diagnostic Due' : `${physSub.formativeMastery}% BKT`}
                  </span>
                </div>
                <p className="text-xs text-slate-600">Motion in 1D: Constant acceleration calculations.</p>
                <button
                  type="button"
                  onClick={() => onOpenSubject('physical_sciences', 'Motion in 1D')}
                  className="w-full mt-2 py-2 text-white text-xs font-bold rounded-xl transition cursor-pointer hover:opacity-95 active:scale-98 shadow-2xs"
                  style={{ backgroundColor: physTheme.base }}
                >
                  Resume Drill &rarr;
                </button>
              </div>
            );
          })()}

          {(() => {
            const busTheme = getSubjectTheme('business_studies');
            const isBusDiag = busSub.status === 'diagnostic_required';
            return (
              <div 
                className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs space-y-2 hover:shadow-xs transition"
                style={{ borderLeftWidth: '4px', borderLeftColor: busTheme.base }}
              >
                <div className="flex items-center justify-between text-xs">
                  <span className="font-bold text-slate-800">Business Studies</span>
                  <span 
                    className="font-bold px-2 py-0.5 rounded-full text-[11px]"
                    style={{
                      backgroundColor: isBusDiag ? busTheme.soft : busTheme.base,
                      color: isBusDiag ? busTheme.text : '#FFFFFF',
                      border: isBusDiag ? `1px solid ${busTheme.border}` : 'none'
                    }}
                  >
                    {isBusDiag ? 'Diagnostic Due' : `${busSub.formativeMastery}% BKT`}
                  </span>
                </div>
                <p className="text-xs text-slate-600">Micro vs Market vs Macro Environments.</p>
                <button
                  type="button"
                  onClick={() => onOpenSubject('business_studies', 'Business Environments')}
                  className="w-full mt-2 py-2 text-white text-xs font-bold rounded-xl transition cursor-pointer hover:opacity-95 active:scale-98 shadow-2xs"
                  style={{ backgroundColor: busTheme.base }}
                >
                  Resume Drill &rarr;
                </button>
              </div>
            );
          })()}

          {(() => {
            const lifeTheme = getSubjectTheme('life_sciences');
            const isLifeDiag = lifeSub.status === 'diagnostic_required';
            return (
              <div 
                className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs space-y-2 hover:shadow-xs transition"
                style={{ borderLeftWidth: '4px', borderLeftColor: lifeTheme.base }}
              >
                <div className="flex items-center justify-between text-xs">
                  <span className="font-bold text-slate-800">Life Sciences</span>
                  <span 
                    className="font-bold px-2 py-0.5 rounded-full text-[11px]"
                    style={{
                      backgroundColor: isLifeDiag ? lifeTheme.soft : lifeTheme.base,
                      color: isLifeDiag ? lifeTheme.text : '#FFFFFF',
                      border: isLifeDiag ? `1px solid ${lifeTheme.border}` : 'none'
                    }}
                  >
                    {isLifeDiag ? 'Diagnostic Due' : `${lifeSub.formativeMastery}% BKT`}
                  </span>
                </div>
                <p className="text-xs text-slate-600">Mitosis: Identifying cell division stages from diagrams.</p>
                <button
                  type="button"
                  onClick={() => onOpenSubject('life_sciences', 'Cell Division & Mitosis')}
                  className="w-full mt-2 py-2 text-white text-xs font-bold rounded-xl transition cursor-pointer hover:opacity-95 active:scale-98 shadow-2xs"
                  style={{ backgroundColor: lifeTheme.base }}
                >
                  Resume Drill &rarr;
                </button>
              </div>
            );
          })()}

        </div>
      </div>
      )}

      {/* 4. Offline WebAPK / PWA Health & Data Saver Card */}
      <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-2xs flex flex-wrap items-center justify-between gap-3 text-xs">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center font-bold">
            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
          </div>
          <div>
            <span className="font-bold text-slate-800 block">Offline Cache Active (Service Worker Ready)</span>
            <span className="text-slate-500 text-[11px]">18 questions cached locally • Submissions sync automatically when reconnected</span>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-[11px] font-bold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded-lg border border-emerald-200">
            ⚡ Data Saver &lt; 2 MB
          </span>
        </div>
      </div>

    </div>
  );
}
