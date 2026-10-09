import React, { useState, useRef, useEffect, useMemo } from 'react';
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
  WifiOff,
  Flame,
  Zap
} from 'lucide-react';
import studentStore, { getTimeGreeting } from '../../services/studentStore';
import MessageBoardModal from '../notifications/MessageBoardModal';
import { getSubjectTheme, BRAND } from '../../theme/subjectPalette';
import UniversalWorkspace from '../workspace/UniversalWorkspace';

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
  result = null,
  onOpenProfilePhoto = () => {},
  onOpenLinkGuardian = () => {},
  onOpenJoinClassModal = () => {},
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
  const [showMessageBoard, setShowMessageBoard] = useState(false);
  const [activeMobileDeskSection, setActiveMobileDeskSection] = useState('school_work'); // 'school_work' | 'self_study'

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
  const isIndependent = Boolean(storeState?.isIndependent || storeState?.currentUser?.isIndependent);

  const assignedTasks = useMemo(() => {
    if (isIndependent) return [];
    return storeState?.currentUser?.assignedTasks || [
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
    ];
  }, [isIndependent, storeState?.currentUser?.assignedTasks]);
  const hasUnviewedTasks = assignedTasks.some(t => studentStore.isTaskUnviewed(t.id));

  // Item 4: Bottom rail filtering based on School Work vs Self-Study
  const displayedSubjects = useMemo(() => {
    if (currentTab === 'desk' && activeMobileDeskSection === 'school_work') {
      const taskSubjects = new Set(assignedTasks.map(t => normalizeTabId(t.subject)));
      return MOBILE_SUBJECTS.filter(s => s.id === 'desk' || taskSubjects.has(s.id));
    }
    return MOBILE_SUBJECTS;
  }, [currentTab, activeMobileDeskSection, assignedTasks]);

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
                <span className="text-[10px] text-blue-200/90 font-medium leading-none truncate max-w-[190px]">
                  {`Grade ${grade} • ${storeState?.phase || (grade >= 10 ? 'FET Phase' : 'Senior Phase')} • ${isIndependent ? 'Independent Account' : formattedSchool}`}
                </span>
              </div>
            </div>

            {/* Right: Actions (Notification Bell & Profile Avatar) */}
            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => setShowMessageBoard(true)}
                className="relative p-1.5 rounded-full hover:bg-white/10 active:bg-white/20 text-white transition cursor-pointer flex items-center justify-center min-w-[36px] min-h-[36px]"
                title="Message Board"
                aria-label="Message Board"
              >
                <Bell className="w-4 h-4 text-blue-100" />
                {(storeState?.messages?.some(m => !m.isRead) || hasUnviewedTasks) && (
                  <span className="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-rose-500 ring-2 ring-[#13519C] animate-pulse" />
                )}
              </button>

              <button
                type="button"
                data-testid="btn-open-user-profile"
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
                    {getTimeGreeting()},
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
                  <span 
                    className="text-[10px] bg-amber-100 text-amber-900 border border-amber-300 font-extrabold px-2 py-0.5 rounded-full shadow-2xs flex items-center gap-1 cursor-help"
                    title="Study Streak: Days in a row you have completed exercises on Fundile"
                  >
                    <span>🔥</span>
                    <span>{effectiveStreak}d</span>
                  </span>
                  <span 
                    className="text-[10px] bg-blue-50 text-[#13519C] border border-blue-200 font-extrabold px-2 py-0.5 rounded-full shadow-2xs flex items-center gap-1 cursor-help"
                    title="Mastery XP: Experience points earned for verified concept and step accuracy"
                  >
                    <span>⚡</span>
                    <span>{effectiveXp > 999 ? `${(effectiveXp / 1000).toFixed(1)}k` : effectiveXp} XP</span>
                  </span>
                </div>
                <div className="flex items-center gap-1.5">
                  <button
                    type="button"
                    data-testid="btn-open-join-class-modal"
                    onClick={() => onOpenJoinClassModal && onOpenJoinClassModal()}
                    className="px-2 py-1 rounded-lg bg-emerald-50 hover:bg-emerald-100 active:bg-emerald-200 text-emerald-800 text-[10px] font-extrabold border border-emerald-200 flex items-center gap-1 transition cursor-pointer shadow-2xs min-h-[30px]"
                    title="Join Teacher's Class"
                  >
                    <span>🏫</span>
                    <span>Join Class</span>
                  </button>
                  <button
                    type="button"
                    data-testid="btn-open-link-guardian-modal"
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

            {/* Section Switcher: School Work vs Self-Study */}
            <div className="flex items-center gap-2 p-1 bg-slate-200/80 rounded-2xl">
              <button
                type="button"
                onClick={() => setActiveMobileDeskSection('school_work')}
                className={`flex-1 py-1.5 px-3 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center justify-center gap-1.5 ${
                  activeMobileDeskSection === 'school_work'
                    ? 'bg-white text-[#13519C] shadow-sm'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                <span>🎒 School Classwork</span>
                {assignedTasks.length > 0 && (
                  <span className={`px-1.5 py-0.5 rounded-full text-[10px] font-extrabold ${
                    hasUnviewedTasks
                      ? 'bg-rose-500 text-white animate-pulse'
                      : 'bg-blue-100 text-[#13519C]'
                  }`}>
                    {assignedTasks.length}
                  </span>
                )}
              </button>

              <button
                type="button"
                onClick={() => setActiveMobileDeskSection('self_study')}
                className={`flex-1 py-1.5 px-3 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center justify-center gap-1.5 ${
                  activeMobileDeskSection === 'self_study'
                    ? 'bg-white text-emerald-800 shadow-sm'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                <span>📖 Self-Paced Learning</span>
                <span className="px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[10px] font-extrabold">
                  4 Active
                </span>
              </button>
            </div>

            {/* Section 1: School Classwork */}
            {activeMobileDeskSection === 'school_work' && (
              <section id="mob-upcoming-tasks-section" className="space-y-3 relative">
                {/* Sticky Header */}
                <div className="sticky top-0 z-20 bg-slate-50/95 backdrop-blur-md py-2.5 px-1 flex items-center justify-between border-b border-slate-200/60 shadow-xs">
                  <div className="flex items-center gap-2">
                    {hasUnviewedTasks ? (
                      <span className="relative flex h-2.5 w-2.5">
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-rose-400 opacity-75"></span>
                        <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-rose-500"></span>
                      </span>
                    ) : (
                      <span className="text-sm">📅</span>
                    )}
                    <h3 
                      className="text-xs font-extrabold uppercase tracking-wider text-slate-800" 
                      style={{ fontFamily: 'Afacad, sans-serif' }}
                    >
                      School Classwork
                    </h3>
                    <span className={`px-2 py-0.5 rounded-full text-[11px] font-extrabold border ${
                      hasUnviewedTasks 
                        ? 'bg-rose-50 text-rose-700 border-rose-300 animate-pulse'
                        : 'bg-blue-100 text-[#13519C] border-blue-200/80'
                    }`}>
                      {assignedTasks.length}
                    </span>
                  </div>
                  {(assignedTasks.length > 0 && !isIndependent) && (
                    <button
                      type="button"
                      onClick={() => {
                        const firstTask = assignedTasks[0];
                        if (firstTask) {
                          studentStore.markTaskViewed(firstTask.id);
                          onSelectTab(firstTask.subject);
                        }
                      }}
                      className="text-[11px] font-bold text-[#13519C] hover:text-blue-800 flex items-center gap-0.5 transition cursor-pointer"
                    >
                      <span>View all</span>
                      <span>→</span>
                    </button>
                  )}
                </div>

                {/* Dynamic Task Rendering */}
                {isIndependent ? (
                  <div className="bg-purple-50/80 border border-purple-200 p-4 rounded-2xl shadow-xs text-center space-y-1.5">
                    <span className="text-xl">🏡</span>
                    <h4 className="text-xs font-bold text-purple-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                      Independent Homeschool Path Active
                    </h4>
                    <p className="text-[11px] text-purple-700 leading-snug">
                      Zero school homework deadlines assigned. Switch to Self-Study to master topics autonomously.
                    </p>
                  </div>
                ) : (assignedTasks.length === 0) ? (
                  <div className="bg-emerald-50/80 border border-emerald-200 p-4 rounded-2xl shadow-xs text-center space-y-1">
                    <span className="text-xl">🎉</span>
                    <h4 className="text-xs font-bold text-emerald-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                      All Caught Up!
                    </h4>
                    <p className="text-[11px] text-emerald-700 leading-snug">
                      No school homework due right now. Switch to Self-Study to practice autonomously and boost your Mastery Dial.
                    </p>
                  </div>
                ) : (
                  assignedTasks.map((task) => {
                    const tTheme = getSubjectTheme(task.subject);
                    const isUnviewed = studentStore.isTaskUnviewed(task.id);

                    return (
                      <div 
                        key={task.id} 
                        data-testid="card-task-upcoming"
                        className={`p-3.5 rounded-2xl shadow-xs space-y-2 transition-all ${
                          isUnviewed
                            ? 'bg-rose-50/70 border-2 border-rose-300 ring-2 ring-rose-200/70'
                            : 'bg-white border border-slate-200/80'
                        }`}
                        style={{ borderLeftWidth: '4px', borderLeftColor: tTheme.base }}
                      >
                        <div className="flex justify-between items-center text-[10px] font-extrabold">
                          <span 
                            className="text-white px-2.5 py-0.5 rounded-full text-[10px] font-extrabold shadow-xs"
                            style={{ backgroundColor: tTheme.base }}
                          >
                            {(task.subjectName || task.subject).toUpperCase()} • {task.dueText}
                          </span>
                          <div className="flex items-center gap-1.5">
                            {isUnviewed && (
                              <span className="bg-rose-500 text-white px-1.5 py-0.5 rounded-full font-extrabold text-[9px] shadow-xs animate-pulse">
                                NEW
                              </span>
                            )}
                            <span className="bg-rose-500 text-white px-2 py-0.5 rounded-full font-extrabold text-[9px] shadow-xs flex items-center gap-1">
                              <Clock className="w-3 h-3 inline" />
                              <span>{task.dueTime}</span>
                            </span>
                          </div>
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
                          data-testid="btn-open-task-subject"
                          onClick={() => {
                            studentStore.markTaskViewed(task.id);
                            if (task.topic) {
                              studentStore.setActiveSession({
                                subjectId: normalizeTabId(task.subject),
                                topic: task.topic,
                                lastActiveTab: normalizeTabId(task.subject),
                              });
                            }
                            onSelectTab(task.subject, false, task.topic);
                          }}
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
            )}

            {/* Section 2: Self-Paced Learning */}
            {activeMobileDeskSection === 'self_study' && (
              <section id="mob-self-paced-mastery-section" className="space-y-3 relative pt-1">
                {/* Sticky Header */}
                <div className="sticky top-0 z-20 bg-slate-50/95 backdrop-blur-md py-2.5 px-1 flex items-center justify-between border-b border-slate-200/60 shadow-xs">
                  <div className="flex items-center gap-2">
                    <Compass className="w-4 h-4 text-emerald-700" />
                    <h3 
                      className="text-xs font-extrabold uppercase tracking-wider text-slate-800" 
                      style={{ fontFamily: 'Afacad, sans-serif' }}
                    >
                      Self-Paced Learning
                    </h3>
                    <span className="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-extrabold border border-emerald-200/80">
                      4
                    </span>
                  </div>
                  <span className="text-[10px] font-extrabold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
                    BKT Calibrated
                  </span>
                </div>

                {/* Mobile Pick Up Where You Left Off Card */}
                {storeState?.activeSession?.topic && (
                  <div className="bg-gradient-to-r from-blue-50/90 to-emerald-50/80 p-3.5 rounded-2xl border border-blue-200/90 shadow-2xs space-y-2 animate-fadeIn">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <span 
                          className="w-2.5 h-2.5 rounded-full" 
                          style={{ backgroundColor: getSubjectTheme(storeState.activeSession.subjectId || 'accounting').base }} 
                        />
                        <span className="text-[10px] font-extrabold text-[#13519C] uppercase tracking-wider">
                          Pick Up Where You Left Off
                        </span>
                      </div>
                      <span className="text-[10px] font-bold text-slate-500 font-mono">
                        Active Session
                      </span>
                    </div>
                    <p className="text-xs font-bold text-slate-900">
                      {storeState.activeSession.topic}
                    </p>
                    <button
                      type="button"
                      onClick={() => onSelectTab(storeState.activeSession.subjectId)}
                      className="w-full py-2.5 text-white text-xs font-bold rounded-xl shadow-xs transition flex items-center justify-center gap-1.5 hover:opacity-95 active:scale-98 cursor-pointer"
                      style={{ background: getSubjectTheme(storeState.activeSession.subjectId || 'accounting').gradient }}
                    >
                      <span>Resume Active Session →</span>
                    </button>
                  </div>
                )}

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
            )}

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

        {/* ==================== NON-DESK VIEWS: UNIVERSAL WORKSPACE ==================== */}
        {currentTab !== 'desk' && (
          <div className="p-3 sm:p-4 space-y-3 pb-24">
            <UniversalWorkspace
              grade={grade}
              subject={currentTab}
              topic={activeTopic}
              question={question}
              isGenerating={isLoadingQuestion}
              isChecking={isMarking}
              onCheck={onCheckAnswer}
              onNext={onNextQuestion}
              onSelectTopic={onSelectTopic}
              result={result}
              isEmbedded={true}
              formativeMastery={currentSubData?.formativeMastery || 0}
              evaluativeScore={currentSubData?.evaluativeScore || 0}
            />
          </div>
        )}
      </div>

      {/* ───────────────────────────────────────────────────────────── */}
      {/* 5. MOBILE BOTTOM SWIPEABLE CAROUSEL (Adaptive Subject Rail)   */}
      {/* ───────────────────────────────────────────────────────────── */}
      <nav 
        id="mob-bottom-nav"
        ref={bottomNavRef}
        className="fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 px-3 py-2 select-none pb-[calc(0.5rem+env(safe-area-inset-bottom))] shadow-lg flex items-center gap-2.5 overflow-x-auto scrollbar-none [&::-webkit-scrollbar]:hidden"
      >
        {displayedSubjects.map((sub) => {
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

      {/* Communications Message Board Modal */}
      <MessageBoardModal 
        isOpen={showMessageBoard} 
        onClose={() => setShowMessageBoard(false)} 
      />

    </div>
  );
}
