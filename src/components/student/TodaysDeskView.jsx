import React, { useState, useEffect, useRef } from 'react';
import studentStore from '../../services/studentStore';
import { 
  ArrowRight, 
  ChevronLeft, 
  ChevronRight, 
  Lightbulb, 
  CheckCircle2, 
  Clock, 
  BookOpen, 
  Calculator,
  Briefcase
} from 'lucide-react';
import { getSubjectTheme } from '../../theme/subjectPalette';
import { ALL_FET_PHASE_SUBJECTS, ALL_SENIOR_PHASE_SUBJECTS } from '../curriculum/SubjectManagerModal';

/**
 * TodaysDeskView
 * Option A Dashboard: Self-Paced First Priority Studio + Decoupled School Classwork.
 * 
 * Invariants:
 * - Central Rotation Reel with springy "Genie out of the bottle" bloom effect.
 * - Saturated, vibrant jewel tones with explicit luminous box-shadow halos (no flat matte).
 * - Single-row solid color subject pills without inner containers or scrollbars.
 * - Authentic button copy: "Start Session" (if fresh / 0%) vs "Continue Session" (if prior progress).
 * - Decoupled School Classwork diary with contextual notification chip on the self-paced studio.
 */

const SUBJECT_DETAILS = {
  accounting: {
    topic: 'Cash Receipts Journal (VAT 15%)',
    stage: 'Stage 2: Practice',
    desc: 'Cash sales, 40% mark-up on cost, and debtor ledger posting.',
  },
  mathematics: {
    topic: 'Algebraic Trinomial Factorisation',
    stage: 'Stage 2: Practice',
    desc: 'Stepwise symbolic factoring & KaTeX procedure verification.',
  },
  technical_mathematics: {
    topic: 'Complex Numbers & Technical Trigonometry',
    stage: 'Stage 0: Diagnostic Required',
    desc: 'Applied engineering calculations & radian angular velocities.',
  },
  mathematical_literacy: {
    topic: 'Tariffs, Municipal Budgets & Break-Even Analysis',
    stage: 'Stage 2: Practice',
    desc: 'Real-world South African municipal sliding scale tariffs.',
  },
  physical_sciences: {
    topic: 'Motion in 1D & Constant Acceleration',
    stage: 'Stage 1: Scaffold',
    desc: 'Equations of motion, displacement vectors, acceleration.',
  },
  life_sciences: {
    topic: 'Cell Division: Mitosis & Microscope Slides',
    stage: 'Stage 0: Diagnostic Required',
    desc: 'Chromosome identification, prophase to telophase biological diagrams.',
  },
  business_studies: {
    topic: 'Micro, Market & Macro Environments',
    stage: 'Stage 2: Practice',
    desc: 'Legislation impact rubrics & PESTLE business analysis.',
  },
  ems: {
    topic: 'Financial Literacy & Cash Receipts',
    stage: 'Stage 2: Practice',
    desc: 'Accounting equation analysis and service enterprise ledgers.',
  },
  natural_sciences: {
    topic: 'Matter & Materials: Periodic Table',
    stage: 'Stage 1: Scaffold',
    desc: 'Atomic structure, chemical equations and particle model.',
  },
};

export default function TodaysDeskView({
  grade = 10,
  schoolName = 'Westville High School',
  currentUser = null,
  isIndependent: propIsIndependent = null,
  activeMode = 'self_paced', // 'self_paced' | 'classwork'
  onChangeActiveMode = () => {},
  activeReelSubjectId = 'accounting',
  onSelectReelSubject = () => {},
  enabledSubjects = ['accounting', 'mathematics', 'technical_mathematics', 'mathematical_literacy', 'physical_sciences', 'life_sciences', 'business_studies'],
  onOpenSubject = () => {},
  onOpenJoinClassModal = () => {},
  onOpenLinkGuardian = () => {},
  onOpenOfflinePacks = () => {},
}) {
  const [storeState, setStoreState] = useState(() => studentStore.getState());
  const [animatingCard, setAnimatingCard] = useState(false);
  const cardRef = useRef(null);

  useEffect(() => {
    const unsub = studentStore.subscribe((newState) => {
      setStoreState({ ...newState });
    });
    return unsub;
  }, []);

  const isSeniorPhase = grade <= 9;
  const fullPhaseList = isSeniorPhase ? ALL_SENIOR_PHASE_SUBJECTS : ALL_FET_PHASE_SUBJECTS;
  const enrolledList = fullPhaseList.filter(s => enabledSubjects.includes(s.id));

  // Determine current active subject for the reel
  const currentSubjItem = enrolledList.find(s => s.id === activeReelSubjectId) || enrolledList[0] || fullPhaseList[0];
  const currentTheme = getSubjectTheme(currentSubjItem.id);
  const sessionTopic = (storeState?.activeSession?.subjectId === currentSubjItem.id && storeState?.activeSession?.topic) 
    ? storeState.activeSession.topic 
    : null;
  const currentDetails = {
    ...(SUBJECT_DETAILS[currentSubjItem.id] || {
      topic: 'Foundational Drill',
      stage: 'Stage 2: Practice',
      desc: 'Core procedural calculations and conceptual practice.'
    }),
    ...(sessionTopic ? { topic: sessionTopic } : {})
  };

  const currentSubData = studentStore.getSubject(currentSubjItem.id);
  const masteryScore = currentSubData?.formativeMastery || 0;
  const hasHistory = (currentSubData?.questionsAttempted || 0) > 0 || Boolean(sessionTopic);
  const isDiagnostic = (currentSubData?.status === 'diagnostic_required' || masteryScore === 0) && !hasHistory;

  // Authentic human button copy
  const ctaButtonText = isDiagnostic ? 'Start Session' : 'Continue Session';

  // Trigger springy genie bloom animation on subject change
  const triggerGenieAnimation = (newSubjId) => {
    onSelectReelSubject(newSubjId);
    setAnimatingCard(true);
    setTimeout(() => {
      setAnimatingCard(false);
    }, 360);
  };

  const stepReel = (direction) => {
    if (enrolledList.length === 0) return;
    const currentIndex = enrolledList.findIndex(s => s.id === currentSubjItem.id);
    const nextIndex = (currentIndex + direction + enrolledList.length) % enrolledList.length;
    triggerGenieAnimation(enrolledList[nextIndex].id);
  };

  const effectiveUser = currentUser || storeState.currentUser;
  const isIndependent = Boolean(propIsIndependent ?? effectiveUser?.isIndependent ?? storeState?.isIndependent);
  const assignedTasks = isIndependent
    ? []
    : (effectiveUser?.assignedTasks || storeState?.assignedTasks || []);

  // ═══════════════════════════════════════════════════════════════════════════
  // VIEW 1: SELF-PACED MASTERY STUDIO (PRIORITY DEFAULT VIEW)
  // ═══════════════════════════════════════════════════════════════════════════
  if (activeMode === 'self_paced') {
    return (
      <div className="p-4 sm:p-6 max-w-5xl mx-auto space-y-4 animate-fadeIn font-sans select-none">
        
        {/* Top Pacing & Notification Banner */}
        <div className="bg-white p-4 rounded-xl border border-slate-200/90 shadow-xs flex flex-wrap items-center justify-between gap-3">
          <div>
            <h3 className="text-base font-bold text-slate-900 tracking-tight font-display">
              Self-Paced Mastery Studio • Grade {grade} {isSeniorPhase ? 'Senior Phase' : 'FET'}
            </h3>
            <p className="text-xs text-slate-500">
              Autonomous concept drills calibrated for curriculum mastery.
            </p>
          </div>

          <div className="flex items-center gap-2.5">
            <button
              type="button"
              data-testid="btn-open-join-class-modal"
              onClick={onOpenJoinClassModal}
              className="inline-flex items-center gap-1.5 min-h-[36px] px-3.5 py-2 rounded-xl border border-emerald-300 bg-emerald-50 hover:bg-emerald-100 text-xs font-semibold text-emerald-800 transition cursor-pointer shadow-2xs"
              title="Join a Teacher's Class Code"
            >
              <span>🏫</span>
              <span>Join Class</span>
            </button>
            <button
              type="button"
              data-testid="btn-open-link-guardian-modal"
              onClick={onOpenLinkGuardian}
              className="inline-flex items-center gap-1.5 min-h-[36px] px-3.5 py-2 rounded-xl border border-blue-300 bg-blue-50 hover:bg-blue-100 text-xs font-semibold text-[#13519C] transition cursor-pointer shadow-2xs"
              title="Family & Guardian Link"
            >
              <span>🔗</span>
              <span>Link Parent</span>
            </button>
            <button
              type="button"
              data-testid="btn-open-offline-pack-modal"
              onClick={onOpenOfflinePacks}
              className="inline-flex items-center gap-1.5 min-h-[36px] px-3.5 py-2 rounded-xl border border-violet-300 bg-violet-50 hover:bg-violet-100 text-xs font-semibold text-violet-800 transition cursor-pointer shadow-2xs"
              title="Download 30-Day Offline Study Packs"
            >
              <span>📦</span>
              <span>Offline Packs</span>
            </button>
            {!isIndependent && assignedTasks.length > 0 && (
              <div className="flex items-center gap-2 bg-amber-50 border border-amber-200 px-3 py-1.5 rounded-xl text-xs text-amber-900 font-semibold shadow-2xs">
                <span className="w-2 h-2 rounded-full bg-rose-500 animate-pulse" />
                <span>{assignedTasks.length} School Assignments Due</span>
                <button
                  type="button"
                  onClick={() => onChangeActiveMode('classwork')}
                  className="ml-1 text-[11px] font-bold text-[#13519C] hover:text-blue-800 underline cursor-pointer"
                >
                  Switch to Classwork &rarr;
                </button>
              </div>
            )}
          </div>
        </div>

        {/* Pick Up Where You Left Off (Session Resumption Banner) */}
        {storeState?.activeSession?.topic && (
          <div className="bg-gradient-to-r from-blue-50/90 via-slate-50 to-emerald-50/70 p-3.5 rounded-xl border border-blue-200/80 shadow-2xs flex flex-wrap items-center justify-between gap-3 animate-fadeIn">
            <div className="flex items-center gap-3">
              <span 
                className="w-3 h-3 rounded-full shrink-0 shadow-xs" 
                style={{ 
                  backgroundColor: getSubjectTheme(storeState.activeSession.subjectId || 'accounting').base,
                  boxShadow: getSubjectTheme(storeState.activeSession.subjectId || 'accounting').glowSm
                }} 
              />
              <div>
                <span className="text-[10px] font-bold text-slate-500 uppercase tracking-wider block">
                  Pick Up Where You Left Off
                </span>
                <span className="text-xs sm:text-sm font-bold text-slate-900">
                  {fullPhaseList.find(s => s.id === storeState.activeSession.subjectId)?.name || 'Accounting'}: {storeState.activeSession.topic}
                </span>
              </div>
            </div>

            <button
              type="button"
              onClick={() => onOpenSubject(storeState.activeSession.subjectId, storeState.activeSession.topic)}
              className="px-3.5 py-1.5 rounded-xl text-white text-xs font-bold shadow-xs hover:opacity-95 active:scale-95 transition cursor-pointer flex items-center gap-1.5 shrink-0"
              style={{ 
                background: getSubjectTheme(storeState.activeSession.subjectId || 'accounting').gradient,
                boxShadow: getSubjectTheme(storeState.activeSession.subjectId || 'accounting').glow 
              }}
            >
              <span>Resume Session</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>
        )}

        {/* ═══════════════════════════════════════════════════════════════════════ */}
        {/* THE ROTATION REEL CAROUSEL STAGE (SEAMLESS CLEAN STAGE — NO INNER BOXES) */}
        {/* ═══════════════════════════════════════════════════════════════════════ */}
        <div className="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200/90 shadow-xs flex flex-col items-center justify-center relative min-h-[340px]">
          
          {/* Left Rotation Arrow */}
          <button
            type="button"
            onClick={() => stepReel(-1)}
            className="absolute left-3 sm:left-6 top-[44%] -translate-y-1/2 w-10 h-10 rounded-full bg-slate-50 shadow-md border border-slate-200 flex items-center justify-center text-slate-700 hover:text-slate-950 hover:bg-white hover:scale-105 active:scale-95 transition cursor-pointer z-30 font-bold text-sm"
            title="Previous Subject"
            aria-label="Previous Subject"
          >
            <ChevronLeft className="w-5 h-5" />
          </button>

          {/* Right Rotation Arrow */}
          <button
            type="button"
            onClick={() => stepReel(1)}
            className="absolute right-3 sm:right-6 top-[44%] -translate-y-1/2 w-10 h-10 rounded-full bg-slate-50 shadow-md border border-slate-200 flex items-center justify-center text-slate-700 hover:text-slate-950 hover:bg-white hover:scale-105 active:scale-95 transition cursor-pointer z-30 font-bold text-sm"
            title="Next Subject"
            aria-label="Next Subject"
          >
            <ChevronRight className="w-5 h-5" />
          </button>

          {/* ───────────────────────────────────────────────────────────────── */}
          {/* CENTERED HERO SUBJECT CARD (WITH RADIANT NEON HALO & GENIE EFFECT) */}
          {/* ───────────────────────────────────────────────────────────────── */}
          <div 
            ref={cardRef}
            key={currentSubjItem.id}
            className={`w-full max-w-md bg-white rounded-2xl border border-slate-200/90 p-6 space-y-4 z-20 transition-all ${
              animatingCard ? 'genie-card-animate' : 'animate-fadeIn'
            }`}
            style={{ 
              borderTopWidth: '6px',
              borderTopColor: currentTheme.base,
              boxShadow: currentTheme.glowLg,
            }}
          >
            {/* Header: Dot, Subject Name & BKT Index */}
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <span 
                  className="w-3.5 h-3.5 rounded-full shrink-0"
                  style={{ 
                    backgroundColor: currentTheme.base,
                    boxShadow: currentTheme.glowSm 
                  }}
                />
                <div>
                  <h3 className="text-lg font-bold text-slate-900 font-display tracking-tight">
                    {currentSubjItem.name}
                  </h3>
                  <span className="text-xs text-slate-500">
                    {currentSubjItem.domain}
                  </span>
                </div>
              </div>

              <div className="text-right">
                <span 
                  className="text-2xl font-black font-display"
                  style={{ color: currentTheme.base }}
                >
                  {isDiagnostic ? 'New' : `${masteryScore}%`}
                </span>
                <span className="block text-[9px] text-slate-400 font-mono tracking-wider">
                  MASTERY INDEX
                </span>
              </div>
            </div>

            {/* Topic Details Block */}
            <div className="bg-slate-50/90 p-3.5 rounded-xl border border-slate-100 text-xs space-y-1.5">
              <div className="flex items-center justify-between">
                <span className="font-bold text-slate-800 text-xs">
                  {currentDetails.topic}
                </span>
                <span className="text-[10px] bg-white border border-slate-200 px-2 py-0.5 rounded font-bold text-slate-700">
                  {isDiagnostic ? 'Stage 0: Diagnostic' : currentDetails.stage}
                </span>
              </div>
              <p className="text-xs text-slate-600 leading-relaxed">
                {currentDetails.desc}
              </p>
            </div>

            {/* Radiant CTA Button with Authentic Human Copy */}
            <div className="pt-1">
              <button
                type="button"
                data-testid="btn-open-subject-session"
                onClick={() => onOpenSubject(currentSubjItem.id, currentDetails.topic)}
                className="w-full min-h-[44px] py-3 text-white text-sm font-bold rounded-xl transition hover:opacity-95 active:scale-98 cursor-pointer flex items-center justify-center gap-2"
                style={{ 
                  background: currentTheme.gradient,
                  boxShadow: currentTheme.glow 
                }}
              >
                <span>{ctaButtonText} in {currentSubjItem.short}</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>

          </div>

          {/* ───────────────────────────────────────────────────────────────── */}
          {/* SINGLE-ROW SOLID COLOR SUBJECT PILLS (NO INNER BOX, NO SCROLLBAR) */}
          {/* ───────────────────────────────────────────────────────────────── */}
          <div className="w-full flex items-center justify-center gap-2.5 sm:gap-3 mt-6 select-none flex-nowrap">
            {enrolledList.map((s) => {
              const theme = getSubjectTheme(s.id);
              const isSelected = (s.id === currentSubjItem.id);

              return (
                <button
                  key={s.id}
                  type="button"
                  onClick={() => triggerGenieAnimation(s.id)}
                  className={`min-h-[36px] px-3 sm:px-3.5 py-2 rounded-xl text-xs font-bold text-white transition-all duration-200 shrink-0 cursor-pointer ${
                    isSelected
                      ? 'ring-2 ring-slate-900 ring-offset-2 scale-105 opacity-100'
                      : 'opacity-80 hover:opacity-100 hover:scale-102 shadow-2xs'
                  }`}
                  style={{
                    background: isSelected ? theme.gradient : theme.base,
                    boxShadow: isSelected ? theme.glow : 'none'
                  }}
                  title={`Select ${s.name}`}
                >
                  <span>{s.short}</span>
                </button>
              );
            })}
          </div>

        </div>

        {/* Targeted 5-Minute Pitstop Banner (Shown strictly when an authentic diagnostic/exam gap exists) */}
        {Boolean(storeState?.hasFailedExam || storeState?.triageRecord || (storeState?.strugglingTopics && storeState.strugglingTopics.length > 0)) && (
          <div className="bg-amber-50/80 p-3.5 rounded-xl border border-amber-300 text-xs flex items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded-lg bg-amber-200/60 text-amber-900 flex items-center justify-center shrink-0">
                <Lightbulb className="w-4 h-4 text-amber-800" />
              </div>
              <div>
                <span className="font-bold text-amber-900 text-sm block">
                  Post-Exam Triage Pitstop Available
                </span>
                <p className="text-[11px] text-amber-800">
                  {storeState?.triageRecord?.diagnosticSummary || 'Targeted atomic micro-drill available to close prerequisite concept gaps.'}
                </p>
              </div>
            </div>
            <button
              type="button"
              onClick={() => {
                const triageSubject = storeState?.triageRecord?.subject || currentSubjItem.id;
                const triageTopic = storeState?.triageRecord?.topic || currentDetails.topic;
                onOpenSubject(triageSubject, triageTopic);
              }}
              className="min-h-[36px] px-4 py-2 bg-[#FF9100] text-[#0B2545] font-bold rounded-lg shadow-sm hover:opacity-90 shrink-0 cursor-pointer text-xs"
            >
              Start 5-Min Fix &rarr;
            </button>
          </div>
        )}

        {/* Offline Cache Indicator */}
        <div className="bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs flex items-center justify-between text-xs">
          <div className="flex items-center gap-2.5">
            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
            <span className="text-slate-700 font-medium">Offline Storage Ready • &lt; 2 MB Data • Instant Loading</span>
          </div>
          <span className="text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 text-[11px]">
            Ready ✓
          </span>
        </div>

      </div>
    );
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // VIEW 2: SCHOOL CLASSWORK (FOCUSED & DECOUPLED HOMEWORK DIARY)
  // ═══════════════════════════════════════════════════════════════════════════
  return (
    <div className="p-4 sm:p-6 max-w-4xl mx-auto space-y-4 animate-fadeIn font-sans select-none">
      
      {/* Header with Return to Self-Paced Studio */}
      <div className="bg-white p-4 rounded-xl border border-slate-200/90 shadow-xs flex items-center justify-between">
        <div>
          <div className="flex items-center gap-2">
            <h3 className="text-base font-bold text-slate-900 tracking-tight font-display">
              {isIndependent ? 'Institutional Classwork' : 'School Classwork & Teacher Assignments'}
            </h3>
            {!isIndependent && assignedTasks.length > 0 && (
              <span className="text-[10px] font-extrabold px-2 py-0.5 rounded-full bg-rose-500 text-white">
                {assignedTasks.length} Due
              </span>
            )}
          </div>
          <p className="text-xs text-slate-500">
            {isIndependent 
              ? 'Independent Account • Not linked to any school or institution.'
              : `Tasks assigned by your educators at ${schoolName}.`}
          </p>
        </div>

        <button
          type="button"
          onClick={() => onChangeActiveMode('self_paced')}
          className="text-xs font-bold text-[#13519C] hover:underline cursor-pointer flex items-center gap-1"
        >
          <span>&larr; Return to Self-Paced Studio</span>
        </button>
      </div>

      {/* Homework Tasks List */}
      {isIndependent ? (
        <div className="bg-purple-50/90 border border-purple-200 p-8 rounded-2xl shadow-xs space-y-3 text-center">
          <div className="w-12 h-12 rounded-2xl bg-purple-100 text-purple-700 flex items-center justify-center text-2xl mx-auto shadow-2xs">
            🏡
          </div>
          <h4 className="text-base font-bold text-purple-900 font-display">
            Independent Account — No Institutional Affiliation
          </h4>
          <p className="text-xs text-purple-800 max-w-lg mx-auto leading-relaxed">
            You are registered as an Independent Learner and are not linked to any school or institution. You have no teacher-assigned homework or class deadlines. All curriculum topics, drills, and exam simulations are available directly through your <strong>Self-Paced Learning Studio</strong>.
          </p>
          <div className="pt-2 flex flex-wrap items-center justify-center gap-3">
            <button
              type="button"
              onClick={() => onChangeActiveMode('self_paced')}
              className="px-4 py-2 bg-[#13519C] hover:bg-blue-800 text-white text-xs font-bold rounded-xl shadow-xs cursor-pointer transition"
            >
              Open Self-Paced Studio &rarr;
            </button>
            {onOpenJoinClassModal && (
              <button
                type="button"
                data-testid="btn-link-class-code"
                onClick={onOpenJoinClassModal}
                className="px-4 py-2 bg-white hover:bg-slate-50 text-slate-700 border border-slate-300 text-xs font-semibold rounded-xl shadow-xs cursor-pointer transition"
              >
                🏫 Join a School Class
              </button>
            )}
          </div>
        </div>
      ) : assignedTasks.length === 0 ? (
        <div className="bg-emerald-50/80 border border-emerald-200 p-8 rounded-2xl shadow-xs text-center space-y-2">
          <div className="w-10 h-10 rounded-full bg-emerald-100 text-emerald-700 mx-auto flex items-center justify-center text-lg font-bold">
            ✓
          </div>
          <h4 className="text-base font-bold text-emerald-900 font-display">
            All Caught Up!
          </h4>
          <p className="text-xs text-emerald-700 max-w-md mx-auto">
            No pending school assignments right now. Return to Self-Paced Studio to keep your streak alive.
          </p>
        </div>
      ) : (
        <div className="space-y-3">
          {assignedTasks.map((task) => {
            const theme = getSubjectTheme(task.subject);
            const isAccounting = (task.subject || '').includes('accounting');

            return (
              <div
                key={task.id}
                data-testid="card-task-upcoming"
                className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs hover:shadow-md transition-all space-y-3"
                style={{ 
                  borderLeftWidth: '5px', 
                  borderLeftColor: theme.base,
                  boxShadow: `0 4px 16px -4px ${theme.shadowColor}`
                }}
              >
                <div className="flex items-center justify-between text-xs">
                  <span 
                    className="px-2.5 py-0.5 rounded-full text-[11px] font-extrabold text-white flex items-center gap-1.5 shadow-2xs"
                    style={{ backgroundColor: theme.base }}
                  >
                    {isAccounting ? <BookOpen className="w-3 h-3" /> : <Calculator className="w-3 h-3" />}
                    <span>{(task.subjectName || task.subject).toUpperCase()}</span>
                    <span>•</span>
                    <span>{task.dueText || 'DUE TODAY'}</span>
                  </span>

                  <div className="flex items-center gap-2">
                    <span className="text-[10px] font-bold text-rose-700 bg-rose-50 px-2 py-0.5 rounded border border-rose-200">
                      Pending
                    </span>
                    <span className="bg-rose-500 text-white font-extrabold px-2.5 py-0.5 rounded-full text-[11px] flex items-center gap-1">
                      <Clock className="w-3 h-3" />
                      <span>{task.dueTime || '17:00'}</span>
                    </span>
                  </div>
                </div>

                <div>
                  <h4 className="text-base font-bold text-slate-900 font-display">
                    {task.title}
                  </h4>
                  <p className="text-xs text-slate-600 mt-1">
                    Assigned by <strong>{task.assignedBy || 'Faculty'}</strong> • {task.marks || 10} Marks • {task.notes || 'Targeted practice.'}
                  </p>
                </div>

                <div className="pt-3 border-t border-slate-100 flex items-center justify-between">
                  <span 
                    className="text-xs font-semibold px-2.5 py-1 rounded"
                    style={{ backgroundColor: theme.soft, color: theme.text }}
                  >
                    Estimated: {task.estimatedMins || 15} mins
                  </span>

                  <button
                    type="button"
                    data-testid="btn-open-task-subject"
                    onClick={() => onOpenSubject(task.subject, task.title)}
                    className="px-5 py-2 text-white text-xs font-bold rounded-xl shadow-xs transition hover:opacity-95 active:scale-98 cursor-pointer flex items-center gap-1.5"
                    style={{ 
                      background: theme.gradient,
                      boxShadow: theme.glowSm
                    }}
                  >
                    <span>Start Assignment</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}

    </div>
  );
}
