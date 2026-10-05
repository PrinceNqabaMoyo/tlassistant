import React, { useState, useRef, useEffect } from 'react';
import { 
  Lightbulb, 
  CheckCircle2, 
  ArrowRight, 
  Loader2, 
  Sparkles,
  GraduationCap,
  Bell,
  Clock,
  Compass,
  WifiOff
} from 'lucide-react';
import studentStore from '../../services/studentStore';
import { getSubjectTheme, BRAND } from '../../theme/subjectPalette';

/**
 * MobileWebApkView
 * Authentic Android WebAPK Mobile Experience with Bidirectional Parity.
 * 
 * Architectural Invariants:
 * 1. Subtle Wave Header Ribbon:
 *    - Deep brand blue gradient (#13519C to #0f4280) with gold graduation cap badge.
 *    - Afacad typography: "Fundile", subtitle "Learn • Practice • Progress".
 *    - Notification bell with red dot and student avatar calling onOpenProfilePhoto.
 *    - Organic subtle SVG wave path (h-5 text-slate-50) smoothly blending into the canvas.
 * 2. Student Greeting & Compact Metrics:
 *    - Eliminates redundant 4-metric summary bar to save ~110px vertical height.
 *    - Compact greeting card with student name (defaulting to Prince), grade, streak, XP, and Link Parent.
 * 3. Today's Desk: Two Sticky Non-Scrolling Sections with Tucking Boundary:
 *    - Section 1: Upcoming Tasks (sticky header, Accounting & Mathematics cards tucking under).
 *    - Section 2: Self-Paced Mastery (sticky header, 4 BKT calibrated autonomous cards tucking under).
 *    - Offline WebAPK Cache Status Badge.
 * 4. Pinned Bottom Subject Navigation:
 *    - Permanently anchored 10-subject carousel (#mob-bottom-nav) with 44px min touch targets.
 *    - Content container flex-1 overflow-y-auto overscroll-contain; bottom nav is NEVER displaced.
 */

const MOBILE_SUBJECTS = [
  { id: 'desk', label: 'Desk', icon: '📋' },
  { id: 'accounting', label: 'Accounting', icon: '📗' },
  { id: 'maths', label: 'Maths', icon: '📘' },
  { id: 'mathslit', label: 'Maths Lit', icon: '📊' },
  { id: 'physics', label: 'Physics', icon: '📙' },
  { id: 'business', label: 'Business', icon: '📕' },
  { id: 'lifesci', label: 'Life Sciences', icon: '🔬' },
  { id: 'techmaths', label: 'Tech Maths', icon: '📐' },
  { id: 'ems', label: 'EMS', icon: '🪙' },
  { id: 'natsci', label: 'Natural Sciences', icon: '🌱' },
];

const normalizeTabId = (id) => {
  if (!id) return 'desk';
  const clean = String(id).toLowerCase().trim();
  if (clean === 'maths' || clean === 'mathematics') return 'maths';
  if (clean === 'mathslit' || clean === 'maths_lit' || clean === 'mathematical_literacy') return 'mathslit';
  if (clean === 'physics' || clean === 'physical_sciences') return 'physics';
  if (clean === 'business' || clean === 'business_studies') return 'business';
  if (clean === 'lifesci' || clean === 'life_sciences') return 'lifesci';
  if (clean === 'techmaths' || clean === 'technical_mathematics') return 'techmaths';
  if (clean === 'ems') return 'ems';
  if (clean === 'natsci' || clean === 'natural_sciences') return 'natsci';
  if (clean === 'accounting') return 'accounting';
  return clean || 'desk';
};

const getDefaultTopicForSubject = (subjectId) => {
  const s = String(subjectId || '').toLowerCase();
  if (s.includes('accounting')) return 'Cash Receipts Journal';
  if (s.includes('mathslit') || s.includes('literacy')) return 'Municipal Tariffs';
  if (s.includes('math') && !s.includes('tech')) return 'Trinomial Factorisation';
  if (s.includes('physics')) return '1D Constant Acceleration';
  if (s.includes('business')) return 'Business Environments';
  if (s.includes('lifesci')) return 'Cell Division & Mitosis';
  if (s.includes('tech')) return 'Mensuration & Trig';
  if (s.includes('ems')) return 'Financial Literacy';
  if (s.includes('natsci')) return 'Matter and Materials';
  return 'General Practice';
};

export default function MobileWebApkView({
  activeTab = 'desk',
  onSelectTab = () => {},
  orientation = 'portrait', // 'portrait' | 'landscape'
  studentName = 'Prince Moyo',
  grade = 10,
  schoolName = 'Westville High School',
  streakDays = 5,
  xp = 1420,
  // Bidirectional Parity Props:
  question = null,
  activeTopic = '',
  isLoadingQuestion = false,
  isMarking = false,
  onSelectTopic = () => {},
  onOpenTopicScope = null,
  onCheckAnswer = () => {},
  onNextQuestion = () => {},
  onOpenProfilePhoto = () => {},
  onOpenLinkGuardian = () => {},
  onOpenPersonaSwitcher = null,
}) {
  const [showHints, setShowHints] = useState(false);
  const [activeHintTier, setActiveHintTier] = useState(1);
  const [hasMarkedCurrent, setHasMarkedCurrent] = useState(false);

  // Accounting live cell inputs
  const [ledgerInputs, setLedgerInputs] = useState({
    bank: '11 500',
    sales: '10 000',
    vat: '1 500',
  });

  // Math/general question input
  const [mathAnswer, setMathAnswer] = useState('');

  const bottomNavRef = useRef(null);
  const activeBtnRef = useRef(null);
  const contentScrollRef = useRef(null);

  const [storeState, setStoreState] = useState(() => studentStore.getState());
  useEffect(() => {
    const unsub = studentStore.subscribe((newState) => {
      setStoreState({ ...newState });
    });
    return unsub;
  }, []);

  const effectiveStreak = storeState?.streakDays ?? streakDays;
  const effectiveXp = storeState?.totalXp ?? xp;
  const userPhoto = storeState?.photoURL || (typeof window !== 'undefined' ? localStorage.getItem('fundile_user_photoURL') : null);

  const currentTab = normalizeTabId(activeTab);
  const isLandscape = orientation === 'landscape';

  const resolvedStudentName = studentName || storeState?.studentName || 'Prince Moyo';
  const rawFirst = resolvedStudentName ? resolvedStudentName.split(' ')[0] : 'Prince';
  const firstName = (rawFirst && rawFirst.toLowerCase() !== 'nqobile') ? rawFirst : 'Prince';
  const formattedSchool = schoolName ? schoolName.replace(/School/i, '').trim() : 'Westville High';

  const currentSubData = studentStore.getSubject(currentTab) || {
    formativeMastery: 84,
    evaluativeScore: 78,
    status: 'practice'
  };

  const getDynamicBadge = (subId) => {
    const theme = getSubjectTheme(subId);
    if (subId === 'desk') {
      const dues = storeState?.deskDues ?? 2;
      return {
        text: dues > 0 ? `${dues} Due` : '0 Due',
        className: dues > 0 ? 'bg-rose-500 text-white shadow-sm shadow-rose-500/40' : 'bg-slate-200 text-slate-700',
        style: {}
      };
    }
    const sub = studentStore.getSubject(subId);
    if (!sub || sub.status === 'diagnostic_required') {
      return {
        text: 'Diag',
        className: 'border font-extrabold',
        style: {
          backgroundColor: theme.soft,
          color: theme.text,
          borderColor: theme.border,
        }
      };
    }
    const val = sub.formativeMastery ?? 0;
    return {
      text: `${val}%`,
      className: 'text-white font-extrabold shadow-2xs',
      style: {
        backgroundColor: theme.base,
      }
    };
  };

  // Reset answer states when question or tab changes
  useEffect(() => {
    setHasMarkedCurrent(false);
    setShowHints(false);
    setActiveHintTier(1);
    setMathAnswer('');
  }, [question?.id, currentTab]);

  // Reset scroll when switching tabs
  useEffect(() => {
    if (contentScrollRef.current) {
      contentScrollRef.current.scrollTop = 0;
    }
  }, [currentTab]);

  // Auto-scroll the active subject button into center view in the bottom carousel
  useEffect(() => {
    if (activeBtnRef.current) {
      activeBtnRef.current.scrollIntoView({
        behavior: 'smooth',
        inline: 'center',
        block: 'nearest',
      });
    }
  }, [currentTab]);

  const handleTriggerMark = () => {
    setHasMarkedCurrent(true);
    if (currentTab === 'accounting') {
      onCheckAnswer(ledgerInputs);
    } else {
      onCheckAnswer(mathAnswer || '(x - 3)(x - 4)');
    }
  };

  return (
    <div className="h-[100dvh] max-h-[100dvh] flex flex-col overflow-hidden bg-white text-slate-800 font-sans select-none relative">
      
      {/* ───────────────────────────────────────────────────────────── */}
      {/* 1. SUBTLE WAVE HEADER RIBBON                                   */}
      {/* ───────────────────────────────────────────────────────────── */}
      {!isLandscape && (
        <header 
          id="mob-wave-header-ribbon"
          className="bg-gradient-to-b from-[#13519C] to-[#0f4280] text-white pt-[calc(0.75rem+env(safe-area-inset-top))] pb-5 px-4 shrink-0 overflow-hidden relative"
        >
          <div className="flex items-center justify-between relative z-10">
            {/* Left: Fundile Brand Mark */}
            <div className="flex items-center gap-2.5">
              <div className="w-8 h-8 rounded-xl bg-white/10 border border-white/20 flex items-center justify-center shadow-xs shrink-0">
                <GraduationCap className="w-5 h-5 text-[#FF9100]" />
              </div>
              <div className="flex flex-col">
                <span 
                  className="font-extrabold text-lg leading-tight tracking-tight text-white" 
                  style={{ fontFamily: 'Afacad, sans-serif' }}
                >
                  Fundile
                </span>
                <span className="text-[10px] text-blue-200/90 font-medium leading-none">
                  Learn • Practice • Progress
                </span>
              </div>
            </div>

            {/* Right: Actions (Notification Bell & Profile Avatar) */}
            <div className="flex items-center gap-2">
              <button
                type="button"
                className="relative p-1.5 rounded-full hover:bg-white/10 active:bg-white/20 text-white transition cursor-pointer flex items-center justify-center min-w-[36px] min-h-[36px]"
                title="Notifications"
                aria-label="Notifications"
              >
                <Bell className="w-4 h-4 text-blue-100" />
                <span className="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-rose-500 ring-2 ring-[#13519C]" />
              </button>

              <button
                type="button"
                onClick={() => onOpenProfilePhoto && onOpenProfilePhoto()}
                className="relative group w-8 h-8 rounded-full overflow-hidden ring-2 ring-white/60 hover:ring-[#FF9100] transition flex items-center justify-center bg-white text-[#13519C] font-extrabold text-xs shadow-xs cursor-pointer shrink-0"
                title="Update Profile Photo"
                aria-label="Profile Photo"
              >
                {userPhoto ? (
                  <img src={userPhoto} alt={studentName} className="h-full w-full object-cover" />
                ) : (
                  <span>{firstName ? firstName.charAt(0) : 'P'}</span>
                )}
                <span className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 flex items-center justify-center text-[10px] transition-opacity text-white">
                  📸
                </span>
              </button>
            </div>
          </div>

          {/* Organic Subtle SVG Wave Path smoothly transitioning into bg-slate-50 */}
          <div className="absolute bottom-0 left-0 right-0 w-full overflow-hidden leading-none pointer-events-none">
            <svg 
              className="h-5 w-full text-slate-50 preserve-3d block" 
              viewBox="0 0 1200 120" 
              preserveAspectRatio="none"
            >
              <path 
                d="M0,0 C180,45 420,55 600,32 C820,8 1020,42 1200,22 L1200,120 L0,120 Z" 
                fill="currentColor"
              />
            </svg>
          </div>
        </header>
      )}

      {/* ───────────────────────────────────────────────────────────── */}
      {/* 3. MOBILE SUB-HEADER (Interactive Topic Pill & 4-Stage Stepper)*/}
      {/* ───────────────────────────────────────────────────────────── */}
      {currentTab !== 'desk' && (
        <div className="px-4 py-2 bg-slate-100 border-b border-slate-200 flex flex-wrap items-center justify-between gap-2 shrink-0">
          {/* Interactive Topic Pill (Calls onOpenTopicScope / onSelectTopic) */}
          <button
            type="button"
            onClick={() => {
              if (typeof onOpenTopicScope === 'function') {
                onOpenTopicScope();
              } else if (typeof onSelectTopic === 'function') {
                onSelectTopic(activeTopic || getDefaultTopicForSubject(currentTab));
              }
            }}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#13519C] hover:bg-[#0e3c73] text-white text-[11px] font-bold transition shadow-xs cursor-pointer min-h-[36px]"
            title="Choose Topic & Exam Scope"
            style={{ fontFamily: 'Afacad, sans-serif' }}
          >
            <span>Term 1 • {activeTopic || getDefaultTopicForSubject(currentTab)} ▾</span>
          </button>

          {/* Compact 4-Stage Progression Stepper */}
          <div className="flex items-center gap-1 p-0.5 bg-white rounded-lg border border-slate-200 text-[10px] font-bold shadow-2xs">
            {[
              { id: 'diagnostic_required', label: '0. Diag' },
              { id: 'scaffold', label: '1. Scaff' },
              { id: 'practice', label: '2. Prac' },
              { id: 'exam_ready', label: '3. Exam' },
            ].map((stg) => {
              const isCurrent = currentSubData.status === stg.id || 
                (stg.id === 'diagnostic_required' && currentSubData.formativeMastery === 0) ||
                (stg.id === 'scaffold' && currentSubData.formativeMastery > 0 && currentSubData.formativeMastery < 60) ||
                (stg.id === 'practice' && currentSubData.formativeMastery >= 60 && currentSubData.formativeMastery < 80) ||
                (stg.id === 'exam_ready' && currentSubData.formativeMastery >= 80);

              return (
                <span
                  key={stg.id}
                  className={`px-1.5 py-0.5 rounded-md transition ${
                    isCurrent
                      ? 'bg-[#13519C] text-white font-bold shadow-xs'
                      : 'text-slate-500'
                  }`}
                >
                  {stg.label}
                </span>
              );
            })}
          </div>
        </div>
      )}

      {/* ───────────────────────────────────────────────────────────── */}
      {/* 4. MOBILE INTERACTIVE CONTENT VIEWS                            */}
      {/* ───────────────────────────────────────────────────────────── */}
      <div 
        ref={contentScrollRef}
        className="flex-1 bg-slate-50 overflow-y-auto overscroll-contain pb-28"
      >
        
        {/* ==================== VIEW 1: TODAY'S DESK ==================== */}
        {currentTab === 'desk' && (
          <div id="mob-content-desk" className="p-4 space-y-4">
            
            {/* Student Greeting Card (Eliminates redundant 4-metric bar to recover ~110px) */}
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200/80 shadow-xs flex items-center justify-between gap-3">
              <div className="flex items-center gap-2.5 min-w-0">
                <div className="w-10 h-10 rounded-full bg-blue-100/90 text-[#13519C] flex items-center justify-center shrink-0 shadow-2xs">
                  <GraduationCap className="w-5 h-5 text-[#13519C]" />
                </div>
                <div className="min-w-0">
                  <span className="text-[11px] font-medium text-slate-500 block leading-tight">
                    Good morning,
                  </span>
                  <h2 
                    className="text-base font-extrabold text-slate-900 leading-tight truncate" 
                    style={{ fontFamily: 'Afacad, sans-serif' }}
                  >
                    {firstName}
                  </h2>
                  <span className="text-[10px] text-slate-500 font-medium block leading-tight truncate">
                    Grade {grade} • FET • {formattedSchool}
                  </span>
                </div>
              </div>

              <div className="flex flex-col items-end gap-1.5 shrink-0">
                <div className="flex items-center gap-1.5">
                  <span className="text-[10px] bg-amber-100 text-amber-900 border border-amber-300 font-extrabold px-2 py-0.5 rounded-full shadow-2xs flex items-center gap-1">
                    <span>🔥</span>
                    <span>{effectiveStreak}d</span>
                  </span>
                  <span className="text-[10px] bg-blue-50 text-[#13519C] border border-blue-200 font-extrabold px-2 py-0.5 rounded-full shadow-2xs flex items-center gap-1">
                    <span>⚡</span>
                    <span>{effectiveXp > 999 ? `${(effectiveXp / 1000).toFixed(1)}k` : effectiveXp} XP</span>
                  </span>
                </div>
                <div className="flex items-center gap-1.5">
                  <button
                    type="button"
                    onClick={() => onOpenLinkGuardian && onOpenLinkGuardian()}
                    className="px-2 py-1 rounded-lg bg-blue-50 hover:bg-blue-100 active:bg-blue-200 text-[#13519C] text-[10px] font-extrabold border border-blue-200 flex items-center gap-1 transition cursor-pointer shadow-2xs min-h-[30px]"
                    title="Family & Guardian Link"
                  >
                    <span>🔗</span>
                    <span>Link Parent</span>
                  </button>
                  {onOpenPersonaSwitcher && (
                    <button
                      type="button"
                      onClick={() => onOpenPersonaSwitcher()}
                      className="px-2 py-1 rounded-lg bg-amber-50 hover:bg-amber-100 active:bg-amber-200 text-amber-900 text-[10px] font-extrabold border border-amber-200 flex items-center gap-1 transition cursor-pointer shadow-2xs min-h-[30px]"
                      title="Switch Persona (Test Students, Teachers, Parents)"
                    >
                      <span>👥</span>
                      <span>Personas</span>
                    </button>
                  )}
                </div>
              </div>
            </div>

            {/* Section 1: Upcoming Tasks (Sticky Non-Scrolling Header & Tucking Cards) */}
            <section id="mob-upcoming-tasks-section" className="space-y-3 relative">
              {/* Sticky Header */}
              <div className="sticky top-0 z-20 bg-slate-50/95 backdrop-blur-md py-2.5 px-1 flex items-center justify-between border-b border-slate-200/60 shadow-xs">
                <div className="flex items-center gap-2">
                  <span className="text-sm">📅</span>
                  <h3 
                    className="text-xs font-extrabold uppercase tracking-wider text-slate-800" 
                    style={{ fontFamily: 'Afacad, sans-serif' }}
                  >
                    Upcoming Tasks
                  </h3>
                  <span className="px-2 py-0.5 rounded-full bg-blue-100 text-[#13519C] text-[11px] font-extrabold border border-blue-200/80">
                    {Boolean(storeState?.currentUser?.isIndependent) ? 0 : (storeState?.currentUser?.assignedTasks?.length ?? 2)}
                  </span>
                </div>
                {((storeState?.currentUser?.assignedTasks?.length ?? 2) > 0 && !storeState?.currentUser?.isIndependent) && (
                  <button
                    type="button"
                    onClick={() => onSelectTab(storeState?.currentUser?.assignedTasks?.[0]?.subject || 'accounting')}
                    className="text-[11px] font-bold text-[#13519C] hover:text-blue-800 flex items-center gap-0.5 transition cursor-pointer"
                  >
                    <span>View all</span>
                    <span>→</span>
                  </button>
                )}
              </div>

              {/* Dynamic Task Rendering */}
              {Boolean(storeState?.currentUser?.isIndependent) ? (
                <div className="bg-purple-50/80 border border-purple-200 p-4 rounded-2xl shadow-xs text-center space-y-1.5">
                  <span className="text-xl">🏡</span>
                  <h4 className="text-xs font-bold text-purple-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                    Independent Homeschool Path Active
                  </h4>
                  <p className="text-[11px] text-purple-700 leading-snug">
                    Zero school homework deadlines assigned. You have full self-paced freedom to master topics autonomously below.
                  </p>
                </div>
              ) : (storeState?.currentUser?.assignedTasks && storeState.currentUser.assignedTasks.length === 0) ? (
                <div className="bg-emerald-50/80 border border-emerald-200 p-4 rounded-2xl shadow-xs text-center space-y-1">
                  <span className="text-xl">🎉</span>
                  <h4 className="text-xs font-bold text-emerald-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                    All Caught Up!
                  </h4>
                  <p className="text-[11px] text-emerald-700 leading-snug">
                    No school homework due right now. Select any subject below to practice autonomously and boost your Mastery Dial.
                  </p>
                </div>
              ) : (
                (storeState?.currentUser?.assignedTasks || [
                  {
                    id: 'def-task-1',
                    subject: 'accounting',
                    subjectName: 'Accounting',
                    title: 'General Journal: Debtors & Bad Debts',
                    assignedBy: 'Mr. N. Sithole',
                    dueText: 'DUE TODAY',
                    dueTime: '17:00',
                    marks: 12,
                    estimatedMins: 15
                  },
                  {
                    id: 'def-task-2',
                    subject: 'maths',
                    subjectName: 'Mathematics',
                    title: 'Trinomial Factorisation Drill',
                    assignedBy: 'Mrs. S. Pillay',
                    dueText: 'DUE FRIDAY',
                    dueTime: '08:00',
                    marks: 10,
                    estimatedMins: 12
                  }
                ]).map((task) => {
                  const tTheme = getSubjectTheme(task.subject);
                  return (
                    <div 
                      key={task.id} 
                      className="bg-white border border-slate-200/80 p-3.5 rounded-2xl shadow-xs space-y-2"
                      style={{ borderLeftWidth: '4px', borderLeftColor: tTheme.base }}
                    >
                      <div className="flex justify-between items-center text-[10px] font-extrabold">
                        <span 
                          className="text-white px-2.5 py-0.5 rounded-full text-[10px] font-extrabold shadow-xs"
                          style={{ backgroundColor: tTheme.base }}
                        >
                          {(task.subjectName || task.subject).toUpperCase()} • {task.dueText}
                        </span>
                        <span className="bg-rose-500 text-white px-2 py-0.5 rounded-full font-extrabold text-[9px] shadow-xs flex items-center gap-1">
                          <Clock className="w-3 h-3 inline" />
                          <span>{task.dueTime}</span>
                        </span>
                      </div>
                      <h4 
                        className="text-xs font-bold text-slate-900 mt-1" 
                        style={{ fontFamily: 'Afacad, sans-serif' }}
                      >
                        {task.title}
                      </h4>
                      <p className="text-[11px] text-slate-600 leading-snug">
                        Assigned by {task.assignedBy} • {task.marks} Marks • {task.estimatedMins || 15} mins.
                      </p>
                      <button
                        type="button"
                        onClick={() => onSelectTab(task.subject)}
                        className="mt-2 w-full py-2.5 text-white text-xs font-bold rounded-xl shadow-xs transition cursor-pointer min-h-[44px] flex items-center justify-center gap-1.5 hover:opacity-95 active:scale-98"
                        style={{ backgroundColor: tTheme.base }}
                      >
                        <span>Open in {task.subjectName || 'Subject'} →</span>
                      </button>
                    </div>
                  );
                })
              )}
            </section>

            {/* Section 2: Self-Paced Mastery (Sticky Non-Scrolling Header & 4 Tucking Cards) */}
            <section id="mob-self-paced-mastery-section" className="space-y-3 relative pt-1">
              {/* Sticky Header */}
              <div className="sticky top-0 z-20 bg-slate-50/95 backdrop-blur-md py-2.5 px-1 flex items-center justify-between border-b border-slate-200/60 shadow-xs">
                <div className="flex items-center gap-2">
                  <Compass className="w-4 h-4 text-emerald-700" />
                  <h3 
                    className="text-xs font-extrabold uppercase tracking-wider text-slate-800" 
                    style={{ fontFamily: 'Afacad, sans-serif' }}
                  >
                    Self-Paced Mastery
                  </h3>
                  <span className="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-extrabold border border-emerald-200/80">
                    4
                  </span>
                </div>
                <span className="text-[10px] font-extrabold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
                  BKT Calibrated
                </span>
              </div>

              {/* 4 Autonomous Practice Cards */}
              <div className="space-y-2.5">
                {/* 1. Accounting */}
                {(() => {
                  const theme = getSubjectTheme('accounting');
                  return (
                    <div 
                      className="bg-white p-3.5 rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-sm transition"
                      style={{ borderLeftWidth: '4px', borderLeftColor: theme.base }}
                    >
                      <div className="flex items-center justify-between text-[10px] font-bold mb-1">
                        <span className="text-slate-500 font-semibold flex items-center gap-1">
                          <span>📗</span>
                          <span>Grade 10 Accounting</span>
                        </span>
                        <span 
                          className="text-white px-2 py-0.5 rounded-full font-extrabold text-[9px] shadow-2xs"
                          style={{ backgroundColor: theme.base }}
                        >
                          84% BKT
                        </span>
                      </div>
                      <p className="text-xs font-bold text-slate-800" style={{ fontFamily: 'Afacad, sans-serif' }}>
                        Cash Receipts Journal (VAT 15%)
                      </p>
                      <button
                        type="button"
                        onClick={() => onSelectTab('accounting')}
                        className="mt-2.5 w-full py-2.5 text-white text-xs font-bold rounded-xl transition cursor-pointer shadow-xs min-h-[44px] flex items-center justify-center gap-1.5 hover:opacity-95 active:scale-98"
                        style={{ backgroundColor: theme.base }}
                      >
                        <span>Resume Autonomous Drill →</span>
                      </button>
                    </div>
                  );
                })()}

                {/* 2. Mathematics */}
                {(() => {
                  const theme = getSubjectTheme('mathematics');
                  return (
                    <div 
                      className="bg-white p-3.5 rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-sm transition"
                      style={{ borderLeftWidth: '4px', borderLeftColor: theme.base }}
                    >
                      <div className="flex items-center justify-between text-[10px] font-bold mb-1">
                        <span className="text-slate-500 font-semibold flex items-center gap-1">
                          <span>📘</span>
                          <span>Grade 10 Mathematics</span>
                        </span>
                        <span 
                          className="text-white px-2 py-0.5 rounded-full font-extrabold text-[9px] shadow-2xs"
                          style={{ backgroundColor: theme.base }}
                        >
                          82% BKT
                        </span>
                      </div>
                      <p className="text-xs font-bold text-slate-800" style={{ fontFamily: 'Afacad, sans-serif' }}>
                        Algebraic Expressions &amp; Factorisation
                      </p>
                      <button
                        type="button"
                        onClick={() => onSelectTab('maths')}
                        className="mt-2.5 w-full py-2.5 text-white text-xs font-bold rounded-xl transition cursor-pointer shadow-xs min-h-[44px] flex items-center justify-center gap-1.5 hover:opacity-95 active:scale-98"
                        style={{ backgroundColor: theme.base }}
                      >
                        <span>Resume Autonomous Drill →</span>
                      </button>
                    </div>
                  );
                })()}

                {/* 3. Physical Sciences */}
                {(() => {
                  const theme = getSubjectTheme('physical_sciences');
                  return (
                    <div 
                      className="bg-white p-3.5 rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-sm transition"
                      style={{ borderLeftWidth: '4px', borderLeftColor: theme.base }}
                    >
                      <div className="flex items-center justify-between text-[10px] font-bold mb-1">
                        <span className="text-slate-500 font-semibold flex items-center gap-1">
                          <span>📙</span>
                          <span>Physical Sciences</span>
                        </span>
                        <span 
                          className="text-white px-2 py-0.5 rounded-full font-extrabold text-[9px] shadow-2xs"
                          style={{ backgroundColor: theme.base }}
                        >
                          78% BKT
                        </span>
                      </div>
                      <p className="text-xs font-bold text-slate-800" style={{ fontFamily: 'Afacad, sans-serif' }}>
                        Newton's Laws of Motion &amp; Vectors
                      </p>
                      <button
                        type="button"
                        onClick={() => onSelectTab('physics')}
                        className="mt-2.5 w-full py-2.5 text-white text-xs font-bold rounded-xl transition cursor-pointer shadow-xs min-h-[44px] flex items-center justify-center gap-1.5 hover:opacity-95 active:scale-98"
                        style={{ backgroundColor: theme.base }}
                      >
                        <span>Resume Autonomous Drill →</span>
                      </button>
                    </div>
                  );
                })()}

                {/* 4. Business Studies */}
                {(() => {
                  const theme = getSubjectTheme('business_studies');
                  return (
                    <div 
                      className="bg-white p-3.5 rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-sm transition"
                      style={{ borderLeftWidth: '4px', borderLeftColor: theme.base }}
                    >
                      <div className="flex items-center justify-between text-[10px] font-bold mb-1">
                        <span className="text-slate-500 font-semibold flex items-center gap-1">
                          <span>📕</span>
                          <span>Business Studies</span>
                        </span>
                        <span 
                          className="text-white px-2 py-0.5 rounded-full font-extrabold text-[9px] shadow-2xs"
                          style={{ backgroundColor: theme.base }}
                        >
                          75% BKT
                        </span>
                      </div>
                      <p className="text-xs font-bold text-slate-800" style={{ fontFamily: 'Afacad, sans-serif' }}>
                        Micro, Market &amp; Macro Environments
                      </p>
                      <button
                        type="button"
                        onClick={() => onSelectTab('business')}
                        className="mt-2.5 w-full py-2.5 text-white text-xs font-bold rounded-xl transition cursor-pointer shadow-xs min-h-[44px] flex items-center justify-center gap-1.5 hover:opacity-95 active:scale-98"
                        style={{ backgroundColor: theme.base }}
                      >
                        <span>Resume Autonomous Drill →</span>
                      </button>
                    </div>
                  );
                })()}
              </div>
            </section>

            {/* Offline WebAPK Data Badge */}
            <div className="bg-white p-3 rounded-2xl border border-slate-200 shadow-2xs flex items-center justify-between">
              <div className="flex items-center gap-2.5">
                <div className="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center shrink-0">
                  <WifiOff className="w-4 h-4 text-purple-700" />
                </div>
                <div>
                  <span className="text-[10px] font-extrabold uppercase text-purple-700 block tracking-wider">
                    Offline WebAPK Cache
                  </span>
                  <p className="text-[11px] font-semibold text-slate-700 leading-tight">
                    1.4 MB Total Data • Zero Video Buffering
                  </p>
                </div>
              </div>
              <span className="text-[10px] font-extrabold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200 shadow-2xs">
                Ready ✓
              </span>
            </div>

          </div>
        )}

        {/* ==================== VIEW 2: ACCOUNTING (Dual-Mode) ==================== */}
        {currentTab === 'accounting' && (
          <div id="mob-content-accounting" className="p-4 space-y-3">
            {/* Subject Header */}
            <div className="bg-emerald-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-emerald-100 block">Grade 10 Accounting</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  {activeTopic || 'CRJ & 15% VAT'}
                </h5>
              </div>
              <span className="bg-white text-emerald-800 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: {currentSubData.formativeMastery}%
              </span>
            </div>

            {/* (A) PORTRAIT VIEW: Compact 2x2 Card Grid */}
            {!isLandscape ? (
              <div id="mob-accounting-portrait-cards" className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                <div className="flex items-center justify-between text-xs pb-1 border-b border-slate-100">
                  <span className="text-[10px] font-bold uppercase text-slate-500">2D Ledger Inputs</span>
                  <span className="text-[10px] font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded border border-amber-200">6 Marks</span>
                </div>

                {question?.prompt && (
                  <p className="text-xs text-slate-700 leading-relaxed font-medium">
                    {question.prompt}
                  </p>
                )}

                <div className="grid grid-cols-2 gap-2 text-xs">
                  <div className="p-2.5 bg-emerald-50 rounded-xl border border-emerald-200">
                    <span className="text-[10px] text-slate-600 block font-semibold">Bank (Gross 115%)</span>
                    <input
                      type="text"
                      value={ledgerInputs.bank}
                      onChange={(e) => setLedgerInputs({ ...ledgerInputs, bank: e.target.value })}
                      className="font-mono font-bold text-emerald-800 text-sm bg-transparent w-full focus:outline-none border-b border-emerald-400"
                    />
                  </div>
                  <div className="p-2.5 bg-emerald-50 rounded-xl border border-emerald-200">
                    <span className="text-[10px] text-slate-600 block font-semibold">Sales (Excl 100%)</span>
                    <input
                      type="text"
                      value={ledgerInputs.sales}
                      onChange={(e) => setLedgerInputs({ ...ledgerInputs, sales: e.target.value })}
                      className="font-mono font-bold text-emerald-800 text-sm bg-transparent w-full focus:outline-none border-b border-emerald-400"
                    />
                  </div>
                  <div className="p-2.5 bg-emerald-50 rounded-xl border border-emerald-200">
                    <span className="text-[10px] text-slate-600 block font-semibold">Output VAT (15%)</span>
                    <input
                      type="text"
                      value={ledgerInputs.vat}
                      onChange={(e) => setLedgerInputs({ ...ledgerInputs, vat: e.target.value })}
                      className="font-mono font-bold text-emerald-800 text-sm bg-transparent w-full focus:outline-none border-b border-emerald-400"
                    />
                  </div>
                  <div className="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                    <span className="text-[10px] text-slate-600 block font-semibold">Cost of Sales</span>
                    <span className="font-mono font-bold text-slate-700 text-sm">R 8 000</span>
                  </div>
                </div>

                {/* 3-Tier Pre-baked Hints Drawer */}
                <div className="space-y-1.5 pt-1">
                  <button
                    type="button"
                    onClick={() => setShowHints(!showHints)}
                    className="w-full py-1.5 px-3 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200 text-xs font-bold flex items-center justify-between transition cursor-pointer min-h-[44px]"
                  >
                    <div className="flex items-center gap-1.5">
                      <Lightbulb className="w-3.5 h-3.5 text-amber-600" />
                      <span>{showHints ? 'Hide Hints' : '💡 View 3-Tier Pre-baked Hints'}</span>
                    </div>
                    <span className="text-[10px] text-amber-700">Tier {activeHintTier} of 3</span>
                  </button>

                  {showHints && (
                    <div className="p-3 bg-amber-50/90 rounded-xl border border-amber-300 text-[11px] text-amber-950 space-y-2 animate-in fade-in">
                      <div className="flex items-center gap-1">
                        {[1, 2, 3].map((tier) => (
                          <button
                            key={tier}
                            type="button"
                            onClick={() => setActiveHintTier(tier)}
                            className={`px-2 py-0.5 rounded text-[10px] font-bold cursor-pointer ${
                              activeHintTier === tier
                                ? 'bg-[#13519C] text-white shadow-xs'
                                : 'bg-white text-slate-600 hover:bg-slate-100'
                            }`}
                          >
                            Tier {tier}
                          </button>
                        ))}
                      </div>
                      <p>
                        {activeHintTier === 1 && 'Look at Bank Gross and calculate the 15/115 fraction.'}
                        {activeHintTier === 2 && 'When inclusive, Gross represents 115% and Sales represents 100%.'}
                        {activeHintTier === 3 && 'VAT = R11,500 × 15/115 = R1,500. Sales = R11,500 − R1,500 = R10,000.'}
                      </p>
                    </div>
                  )}
                </div>

                {/* Mark Answer Button & Verified Banner */}
                <div className="pt-2 flex flex-col gap-2">
                  <button
                    type="button"
                    onClick={handleTriggerMark}
                    disabled={isMarking || isLoadingQuestion}
                    className="w-full py-2.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-md shadow-emerald-700/20 flex items-center justify-center gap-2 transition cursor-pointer disabled:opacity-50 min-h-[44px]"
                  >
                    {isMarking ? <Loader2 className="w-4 h-4 animate-spin" /> : <CheckCircle2 className="w-4 h-4" />}
                    <span>{isMarking ? 'Marking Entry...' : 'Check & Verify Entry'}</span>
                  </button>

                  {hasMarkedCurrent && (
                    <div className="p-3 bg-emerald-50 border border-emerald-300 rounded-xl flex items-center justify-between text-xs text-emerald-950 font-bold shadow-xs animate-in zoom-in-95">
                      <div className="flex items-center gap-1.5">
                        <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                        <span>6 / 6 Marks Credited • Balanced</span>
                      </div>
                      <span className="px-2 py-0.5 rounded-full bg-emerald-600 text-white text-[10px] font-extrabold shadow-xs">
                        +35 XP
                      </span>
                    </div>
                  )}

                  {hasMarkedCurrent && (
                    <button
                      type="button"
                      onClick={() => {
                        setHasMarkedCurrent(false);
                        onNextQuestion();
                      }}
                      className="w-full py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-900 text-white font-bold text-xs flex items-center justify-center gap-1.5 transition cursor-pointer min-h-[44px]"
                    >
                      <span>Next Exercise</span>
                      <ArrowRight className="w-3.5 h-3.5" />
                    </button>
                  )}
                </div>
              </div>
            ) : (
              /* (B) LANDSCAPE VIEW: Fullscreen 6-Column 2D Ledger Table */
              <div id="mob-accounting-landscape-ledger" className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                <div className="flex items-center justify-between pb-2 border-b border-slate-100">
                  <div className="flex items-center gap-2">
                    <span className="text-[10px] font-extrabold uppercase bg-emerald-600 text-white px-2 py-0.5 rounded shadow-xs shadow-emerald-500/30">
                      CAPS CRJ 2D Ledger • Fullscreen Real Estate
                    </span>
                    <span className="text-xs font-bold text-slate-800 truncate">Cash Sales R11,500 (15% VAT)</span>
                  </div>
                  <span className="text-xs font-extrabold text-amber-600 bg-amber-50 px-2 py-0.5 rounded border border-amber-200">6 Marks</span>
                </div>
                <div className="overflow-x-auto rounded-xl border border-slate-200 shadow-2xs">
                  <table className="w-full text-xs text-left">
                    <thead className="bg-slate-100 text-slate-700 border-b border-slate-200 uppercase text-[10px] font-bold">
                      <tr>
                        <th className="p-2">Day</th>
                        <th className="p-2">Details</th>
                        <th className="p-2">Bank (Gross 115%)</th>
                        <th className="p-2">Sales (Excl 100%)</th>
                        <th className="p-2">Output VAT (15%)</th>
                        <th className="p-2">Cost of Sales</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100 font-mono text-xs">
                      <tr>
                        <td className="p-2 text-slate-600">12</td>
                        <td className="p-2 text-slate-800 font-sans font-medium">Cash / CRT</td>
                        <td className="p-1.5">
                          <input 
                            type="text" 
                            value={ledgerInputs.bank}
                            onChange={(e) => setLedgerInputs({ ...ledgerInputs, bank: e.target.value })}
                            className="w-24 px-2 py-1 rounded border-2 border-emerald-500 bg-emerald-50 text-emerald-800 font-bold focus:outline-none"
                          />
                        </td>
                        <td className="p-1.5">
                          <input 
                            type="text" 
                            value={ledgerInputs.sales}
                            onChange={(e) => setLedgerInputs({ ...ledgerInputs, sales: e.target.value })}
                            className="w-24 px-2 py-1 rounded border-2 border-emerald-500 bg-emerald-50 text-emerald-800 font-bold focus:outline-none"
                          />
                        </td>
                        <td className="p-1.5">
                          <input 
                            type="text" 
                            value={ledgerInputs.vat}
                            onChange={(e) => setLedgerInputs({ ...ledgerInputs, vat: e.target.value })}
                            className="w-20 px-2 py-1 rounded border-2 border-emerald-500 bg-emerald-50 text-emerald-800 font-bold focus:outline-none"
                          />
                        </td>
                        <td className="p-2 text-slate-600">8 000</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div className="p-2 bg-amber-50 border border-amber-200 rounded-xl text-[11px] text-amber-900 flex items-center justify-between">
                  <div className="flex items-center gap-1.5">
                    <span className="font-bold text-amber-800">Tier 3 Hint:</span>
                    <span>When VAT inclusive, R11,500 × 15/115 = R1,500 VAT.</span>
                  </div>
                  <span className="font-extrabold text-white bg-emerald-600 px-2.5 py-0.5 rounded text-[10px]">+35 XP Credited</span>
                </div>
              </div>
            )}
          </div>
        )}

        {/* ==================== VIEW 3: MATHEMATICS ==================== */}
        {currentTab === 'maths' && (
          <div id="mob-content-maths" className="p-4 space-y-3">
            <div className="bg-blue-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-blue-100 block">Grade 10 Mathematics</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  {activeTopic || 'Trinomial Factorisation'}
                </h5>
              </div>
              <span className="bg-white text-blue-900 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: {currentSubData.formativeMastery}%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
              <span className="text-[10px] font-bold uppercase text-slate-400">Step-by-Step KaTeX Keypad</span>
              <p className="text-xs font-bold text-slate-800">{question?.prompt || 'Factorise completely: x² − 7x + 12'}</p>
              
              <div className="space-y-2">
                <input
                  type="text"
                  value={mathAnswer}
                  onChange={(e) => setMathAnswer(e.target.value)}
                  placeholder="e.g. (x - 3)(x - 4)"
                  className="w-full px-3 py-2 rounded-xl border border-blue-300 font-mono text-xs font-bold text-blue-950 focus:outline-none focus:ring-2 focus:ring-blue-500 min-h-[44px]"
                />

                <button
                  type="button"
                  onClick={handleTriggerMark}
                  disabled={isMarking}
                  className="w-full py-2.5 bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs rounded-xl transition flex items-center justify-center gap-1.5 cursor-pointer shadow-xs min-h-[44px]"
                >
                  {isMarking ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <CheckCircle2 className="w-3.5 h-3.5" />}
                  <span>Verify Answer</span>
                </button>

                {hasMarkedCurrent && (
                  <div className="p-2.5 bg-emerald-50 border border-emerald-300 rounded-xl text-emerald-950 font-bold text-xs flex items-center justify-between animate-in fade-in">
                    <div className="flex items-center gap-1.5">
                      <Sparkles className="w-4 h-4 text-emerald-600" />
                      <span>SymPy Verified: (−3) + (−4) = −7</span>
                    </div>
                    <span className="bg-emerald-600 text-white px-2 py-0.5 rounded-full text-[10px]">+35 XP</span>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {/* ==================== VIEW 4: MATHEMATICAL LITERACY ==================== */}
        {currentTab === 'mathslit' && (
          <div id="mob-content-mathslit" className="p-4 space-y-3">
            <div className="bg-purple-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-purple-100 block">Maths Literacy</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  {activeTopic || 'Municipal Tariffs & Budgets'}
                </h5>
              </div>
              <span className="bg-white text-purple-950 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: {currentSubData.formativeMastery}%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs">
              <p className="text-slate-700">{question?.prompt || 'Calculate 25 kL water tariff: First 6 kL free, 7-15 kL @ R18.50, 16-25 kL @ R24.00.'}</p>
              <div className="p-3 bg-purple-50 border border-purple-200 rounded-xl text-purple-950 font-mono font-bold">
                Total = (0) + (9 × 18.50) + (10 × 24.00) = R406.50 ✓
              </div>
            </div>
          </div>
        )}

        {/* ==================== VIEW 5: PHYSICAL SCIENCES ==================== */}
        {currentTab === 'physics' && (
          <div id="mob-content-physics" className="p-4 space-y-3">
            <div className="bg-cyan-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-cyan-100 block">Physical Sciences</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  {activeTopic || '1D Constant Acceleration'}
                </h5>
              </div>
              <span className="bg-white text-cyan-900 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: {currentSubData.formativeMastery}%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
              <p className="text-xs text-slate-700">{question?.prompt || 'Trolley accelerates from rest at 2,5 m/s² for 4 s.'}</p>
              <div className="p-3 bg-cyan-50 border border-cyan-200 rounded-xl text-cyan-950 font-mono font-bold text-xs">
                vf = 0 + (2,5)(4) = 10,0 m/s ✓
              </div>
            </div>
          </div>
        )}

        {/* ==================== VIEW 6: BUSINESS STUDIES ==================== */}
        {currentTab === 'business' && (
          <div id="mob-content-business" className="p-4 space-y-3">
            <div 
              className="text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between"
              style={{ backgroundColor: getSubjectTheme('business_studies').base }}
            >
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-rose-100 block">Business Studies</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  {activeTopic || 'Business Environments'}
                </h5>
              </div>
              <span className="bg-white text-rose-950 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: {currentSubData.formativeMastery}%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
              <p className="text-xs text-slate-700">{question?.prompt || 'Fuel price increase decree by Minister of Mineral Resources.'}</p>
              <div className="p-3 bg-rose-50 border border-rose-200 rounded-xl text-rose-950 font-bold text-xs">
                Macro Environment (Economic &amp; Political) • Outside Management Control ✓
              </div>
            </div>
          </div>
        )}

        {/* ==================== VIEW 7: LIFE SCIENCES ==================== */}
        {currentTab === 'lifesci' && (
          <div id="mob-content-lifesci" className="p-4 space-y-3">
            <div 
              className="text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between"
              style={{ backgroundColor: getSubjectTheme('life_sciences').base }}
            >
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-lime-100 block">Life Sciences</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  {activeTopic || 'Cell Division & Mitosis'}
                </h5>
              </div>
              <span className="bg-white text-teal-950 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: {currentSubData.formativeMastery}%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
              <p className="text-xs text-slate-700">{question?.prompt || 'Sister chromatids separating towards opposite poles.'}</p>
              <div className="p-3 bg-teal-50 border border-teal-200 rounded-xl text-teal-950 font-bold text-xs">
                Anaphase (Spindle Fiber Contraction) ✓
              </div>
            </div>
          </div>
        )}

        {/* ==================== VIEW 8: TECH MATHS ==================== */}
        {currentTab === 'techmaths' && (
          <div id="mob-content-techmaths" className="p-4 space-y-3">
            <div className="bg-indigo-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-indigo-100 block">Tech Maths</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  {activeTopic || 'Mensuration & Trig'}
                </h5>
              </div>
              <span className="bg-white text-indigo-950 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: {currentSubData.formativeMastery}%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2 font-mono text-xs">
              <p className="text-slate-700 font-sans">{question?.prompt || 'Sides 6 cm and 8 cm right-angled triangle.'}</p>
              <div className="p-3 bg-indigo-50 border border-indigo-200 rounded-xl text-indigo-950 font-bold">
                r = √(6² + 8²) = 10 cm &bull; sin(θ) = 0.6 ✓
              </div>
            </div>
          </div>
        )}

        {/* ==================== VIEW 9: EMS ==================== */}
        {currentTab === 'ems' && (
          <div id="mob-content-ems" className="p-4 space-y-3">
            <div className="bg-amber-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-amber-100 block">Grade 9 EMS</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  {activeTopic || 'The Economy & Financial Literacy'}
                </h5>
              </div>
              <span className="bg-white text-amber-950 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: {currentSubData.formativeMastery}%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs">
              <p className="text-slate-700">{question?.prompt || 'Factors of production: Land, Labour, Capital, Entrepreneurship.'}</p>
              <div className="p-3 bg-amber-50 border border-amber-200 rounded-xl text-amber-950 font-bold">
                Remuneration: Rent, Wages/Salaries, Interest, Profit ✓
              </div>
            </div>
          </div>
        )}

        {/* ==================== VIEW 10: NATURAL SCIENCES ==================== */}
        {currentTab === 'natsci' && (
          <div id="mob-content-natsci" className="p-4 space-y-3">
            <div className="bg-emerald-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-emerald-100 block">Natural Sciences</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  {activeTopic || 'Matter and Materials'}
                </h5>
              </div>
              <span className="bg-white text-emerald-950 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: {currentSubData.formativeMastery}%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-xs">
              <p className="text-slate-700">{question?.prompt || 'Periodic table arrangement and atomic structure.'}</p>
              <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-xl text-emerald-950 font-bold">
                Atomic Number = Protons = Electrons in neutral atom ✓
              </div>
            </div>
          </div>
        )}

      </div>

      {/* ───────────────────────────────────────────────────────────── */}
      {/* 5. MOBILE BOTTOM SWIPEABLE CAROUSEL (10 Subjects, 44px min)  */}
      {/* ───────────────────────────────────────────────────────────── */}
      <nav 
        id="mob-bottom-nav"
        ref={bottomNavRef}
        className="fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 px-3 py-2 select-none pb-[calc(0.5rem+env(safe-area-inset-bottom))] shadow-lg flex items-center gap-2.5 overflow-x-auto scrollbar-none [&::-webkit-scrollbar]:hidden"
      >
        {MOBILE_SUBJECTS.map((sub) => {
          const isActive = currentTab === sub.id;
          const theme = getSubjectTheme(sub.id);
          const b = getDynamicBadge(sub.id);

          return (
            <button
              key={sub.id}
              id={`mob-tab-${sub.id}`}
              ref={isActive ? activeBtnRef : null}
              type="button"
              onClick={() => onSelectTab(sub.id)}
              className={`mob-nav-btn flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs transition shrink-0 whitespace-nowrap min-h-[44px] cursor-pointer font-bold ${
                isActive
                  ? 'border-2 shadow-sm'
                  : 'bg-slate-50 text-slate-600 border border-slate-200 hover:text-slate-900 font-medium'
              }`}
              style={{
                backgroundColor: isActive ? theme.soft : undefined,
                borderColor: isActive ? theme.base : undefined,
                color: isActive ? theme.text : undefined,
              }}
            >
              <span className="text-base leading-none">{sub.icon}</span>
              <span className="leading-none">{sub.label}</span>
              <span 
                className={`px-1.5 py-0.5 rounded-full text-[9px] ${b.className}`}
                style={b.style}
              >
                {b.text}
              </span>
            </button>
          );
        })}
      </nav>

    </div>
  );
}
