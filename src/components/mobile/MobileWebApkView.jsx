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
  Zap,
  LogOut
} from 'lucide-react';
import studentStore, { getTimeGreeting } from '../../services/studentStore';
import MessageBoardModal from '../notifications/MessageBoardModal';
import { getSubjectTheme, BRAND } from '../../theme/subjectPalette';
import UniversalWorkspace from '../workspace/UniversalWorkspace';
import FundileLogo from '../ui/FundileLogo';
import { ALL_FET_PHASE_SUBJECTS, ALL_SENIOR_PHASE_SUBJECTS } from '../curriculum/SubjectManagerModal';

const SUBJECT_ICONS = {
  accounting: '📗',
  mathematics: '📘',
  physical_sciences: '📙',
  life_sciences: '🔬',
  business_studies: '📕',
  technical_mathematics: '📐',
  mathematical_literacy: '📊',
  ems: '🪙',
  natural_sciences: '🌱',
};

const normalizeTabId = (id) => {
  if (!id) return 'desk';
  const clean = String(id).toLowerCase().trim();
  if (clean === 'maths' || clean === 'mathematics') return 'mathematics';
  if (clean === 'mathslit' || clean === 'maths_lit' || clean === 'mathematical_literacy') return 'mathematical_literacy';
  if (clean === 'physics' || clean === 'physical_sciences') return 'physical_sciences';
  if (clean === 'business' || clean === 'business_studies') return 'business_studies';
  if (clean === 'lifesci' || clean === 'life_sciences') return 'life_sciences';
  if (clean === 'techmaths' || clean === 'technical_mathematics') return 'technical_mathematics';
  if (clean === 'ems') return 'ems';
  if (clean === 'natsci' || clean === 'natural_sciences') return 'natural_sciences';
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
  enabledSubjects = null,
  onOpenManageSubjects = null,
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
  onLogout = () => {},
}) {
  const [showHints, setShowHints] = useState(false);
  const [activeHintTier, setActiveHintTier] = useState(1);
  const [hasMarkedCurrent, setHasMarkedCurrent] = useState(false);
  const [showLogoutConfirm, setShowLogoutConfirm] = useState(false);

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
  const isIndependent = Boolean(storeState?.isIndependent || storeState?.currentUser?.isIndependent);
  const formattedSchool = isIndependent ? 'Independent Homeschool' : (schoolName ? schoolName.replace(/School/i, '').trim() : 'Westville High');

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

  // Horizontal swipeable bottom subject rail: Strictly present student's enrolled phase subjects
  const isSeniorPhase = Number(grade) <= 9;
  const fullPhaseList = isSeniorPhase ? ALL_SENIOR_PHASE_SUBJECTS : ALL_FET_PHASE_SUBJECTS;
  const enabledKeys = (enabledSubjects && enabledSubjects.length > 0)
    ? enabledSubjects
    : (storeState?.enabledSubjects || (isSeniorPhase ? ['mathematics', 'ems', 'natural_sciences'] : ['accounting', 'mathematics', 'physical_sciences', 'life_sciences']));

  const enrolledPhaseSubjects = useMemo(() => {
    return fullPhaseList
      .filter((s) => !enabledKeys || enabledKeys.length === 0 || enabledKeys.includes(s.id))
      .map((s) => ({
        ...s,
        label: s.short || s.name,
        icon: SUBJECT_ICONS[s.id] || '📚',
      }));
  }, [fullPhaseList, enabledKeys]);

  const displayedSubjects = enrolledPhaseSubjects;

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
      {/* MOBILE INTERACTIVE CONTENT SCROLL CONTAINER                   */}
      {/* ───────────────────────────────────────────────────────────── */}
      <div 
        ref={contentScrollRef}
        className="flex-1 bg-slate-50 overflow-y-auto overscroll-contain pb-28 scroll-smooth"
      >
        {/* 1. SUBTLE WAVE HEADER RIBBON (Glides off screen smoothly on downward scroll) */}
        {!isLandscape && (
          <header 
            id="mob-wave-header-ribbon"
            className="bg-gradient-to-b from-[#13519C] to-[#0f4280] text-white px-4 pt-[calc(0.75rem+env(safe-area-inset-top))] pb-5 shrink-0 overflow-hidden relative shadow-xs"
          >
            <div className="flex items-center justify-between gap-2 relative z-10">
              {/* Left: Fundile Brand Mark */}
              <div className="flex items-center gap-2 min-w-0">
                <FundileLogo className="h-6 sm:h-7 w-auto text-white shrink-0" wordmarkColor="white" />
              </div>

              {/* Right: Actions (Notification Bell, Sign Out & Profile Avatar) */}
              <div className="flex items-center gap-1.5">
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
                  data-testid="btn-open-logout-modal"
                  onClick={() => setShowLogoutConfirm(true)}
                  className="p-1.5 rounded-full hover:bg-white/10 active:bg-white/20 text-white transition cursor-pointer flex items-center justify-center min-w-[36px] min-h-[36px]"
                  title="Sign Out"
                  aria-label="Sign Out"
                >
                  <LogOut className="w-4 h-4 text-blue-100" />
                </button>

                {currentTab !== 'desk' && (
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
                )}
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

        {/* 2. MOBILE SUB-HEADER (Interactive Topic Pill & 4-Stage Stepper: Pins at top when working in subject) */}
        {currentTab !== 'desk' && (
          <div className={`sticky top-0 z-20 px-4 py-2 bg-slate-100/95 backdrop-blur-md border-b border-slate-200 flex flex-wrap items-center justify-between gap-2 shadow-xs transition-all duration-200 ${isLoadingQuestion ? 'opacity-70 pointer-events-none' : ''}`}>
            {/* Interactive Topic Pill (Calls onOpenTopicScope / onSelectTopic) */}
            <button
              type="button"
              disabled={isLoadingQuestion}
              onClick={() => {
                if (isLoadingQuestion) return;
                if (typeof onOpenTopicScope === 'function') {
                  onOpenTopicScope();
                } else if (typeof onSelectTopic === 'function') {
                  onSelectTopic(activeTopic || getDefaultTopicForSubject(currentTab));
                }
              }}
              className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#13519C] hover:bg-[#0e3c73] text-white text-[11px] font-bold transition shadow-xs cursor-pointer min-h-[36px] ${isLoadingQuestion ? 'opacity-60 pointer-events-none' : ''}`}
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

        {/* ==================== VIEW 1: TODAY'S DESK ==================== */}
        {currentTab === 'desk' && (
          <div id="mob-content-desk" className="p-4 space-y-4">
            
            {/* Student Profile Card (Decluttered & Clean) */}
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200/80 shadow-xs flex items-center justify-between gap-3">
              <div className="flex items-center gap-3 min-w-0">
                <button
                  type="button"
                  data-testid="btn-open-user-profile"
                  onClick={() => onOpenProfilePhoto && onOpenProfilePhoto()}
                  className="w-11 h-11 rounded-full bg-[#13519C] text-white font-extrabold text-sm flex items-center justify-center shrink-0 shadow-2xs ring-2 ring-slate-100 hover:ring-[#FF9100] transition cursor-pointer"
                  title="Profile & Settings"
                >
                  {userPhoto ? (
                    <img src={userPhoto} alt={studentName} className="h-full w-full object-cover rounded-full" />
                  ) : (
                    <span>{firstName ? firstName.charAt(0).toUpperCase() : 'P'}</span>
                  )}
                </button>
                <div className="min-w-0">
                  <h2 
                    className="text-base font-extrabold text-slate-900 leading-tight truncate" 
                    style={{ fontFamily: 'Afacad, sans-serif' }}
                  >
                    {resolvedStudentName}
                  </h2>
                  <span className="text-[11px] text-slate-500 font-medium block leading-tight truncate mt-0.5">
                    Grade {grade} • {formattedSchool}
                  </span>
                </div>
              </div>

              {/* Action Buttons: Join Class & Link Parent (+ Personas if dev/admin) */}
              <div className="flex items-center gap-1.5 shrink-0">
                <button
                  type="button"
                  data-testid="btn-open-join-class-modal"
                  onClick={() => onOpenJoinClassModal && onOpenJoinClassModal()}
                  className="px-2.5 py-1.5 rounded-xl bg-emerald-50 hover:bg-emerald-100 active:bg-emerald-200 text-emerald-800 text-xs font-extrabold border border-emerald-200 flex items-center gap-1 transition cursor-pointer shadow-2xs min-h-[34px]"
                  title="Join Teacher's Class"
                >
                  <span>🏫</span>
                  <span>Join Class</span>
                </button>
                <button
                  type="button"
                  data-testid="btn-open-link-guardian-modal"
                  onClick={() => onOpenLinkGuardian && onOpenLinkGuardian()}
                  className="px-2.5 py-1.5 rounded-xl bg-blue-50 hover:bg-blue-100 active:bg-blue-200 text-[#13519C] text-xs font-extrabold border border-blue-200 flex items-center gap-1 transition cursor-pointer shadow-2xs min-h-[34px]"
                  title="Family & Guardian Link"
                >
                  <span>🔗</span>
                  <span>Link Parent</span>
                </button>
                {onOpenPersonaSwitcher && (
                  <button
                    type="button"
                    onClick={() => onOpenPersonaSwitcher()}
                    className="p-1.5 rounded-xl bg-amber-50 hover:bg-amber-100 active:bg-amber-200 text-amber-900 text-xs font-extrabold border border-amber-200 flex items-center justify-center transition cursor-pointer shadow-2xs min-h-[34px] min-w-[34px]"
                    title="Switch Persona (Test Students, Teachers, Parents)"
                  >
                    <span>👥</span>
                  </button>
                )}
              </div>
            </div>

            {/* Section Switcher: School Work vs Self-Study */}
            <div className="flex items-center gap-2 p-1 bg-slate-200/80 rounded-2xl">
              <button
                type="button"
                data-testid="mob-mode-classwork"
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
                data-testid="mob-mode-self-paced"
                onClick={() => setActiveMobileDeskSection('self_study')}
                className={`flex-1 py-1.5 px-3 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center justify-center gap-1.5 ${
                  activeMobileDeskSection === 'self_study'
                    ? 'bg-white text-emerald-800 shadow-sm'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                <span>📖 Self-Paced Learning</span>
                <span className="px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[10px] font-extrabold">
                  {enrolledPhaseSubjects.length} Active
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
                      {enrolledPhaseSubjects.length}
                    </span>
                  </div>
                  {onOpenManageSubjects && (
                    <button
                      type="button"
                      data-testid="btn-mobile-manage-subjects"
                      onClick={onOpenManageSubjects}
                      className="text-[11px] font-extrabold text-emerald-800 bg-emerald-50 hover:bg-emerald-100 active:bg-emerald-200 px-2.5 py-1 rounded-full border border-emerald-300 transition cursor-pointer flex items-center gap-1 shadow-2xs"
                      title="Add or remove self-paced curriculum subjects"
                    >
                      <span>⚙️</span>
                      <span>Manage Subjects</span>
                    </button>
                  )}
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
                    <div className="text-xs">
                      <span className="font-extrabold text-[#13519C] block text-sm" style={{ fontFamily: 'Afacad, sans-serif' }}>
                        {enrolledPhaseSubjects.find(s => s.id === storeState.activeSession.subjectId)?.name || 'Subject'} • Grade {grade}
                      </span>
                      <p className="text-xs text-slate-700 font-medium mt-0.5">
                        Current Topic: <strong className="text-slate-900 font-bold">{storeState.activeSession.topic}</strong>
                      </p>
                    </div>
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

              {/* Dynamic Enrolled Autonomous Practice Cards */}
              <div className="space-y-2.5">
                {enrolledPhaseSubjects.map((sub) => {
                  const theme = getSubjectTheme(sub.id);
                  const subData = studentStore.getSubject(sub.id) || { formativeMastery: 0, status: 'diagnostic_required' };
                  const isDiagnostic = subData.status === 'diagnostic_required';
                  const mastery = subData.formativeMastery || 0;
                  const defaultTopic = getDefaultTopicForSubject(sub.id);

                  return (
                    <div 
                      key={sub.id}
                      data-testid={`card-subject-${sub.id}`}
                      className="bg-white p-3.5 rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-sm transition"
                      style={{ borderLeftWidth: '4px', borderLeftColor: theme.base }}
                    >
                      <div className="flex items-center justify-between gap-2 mb-2">
                        <div className="flex items-center gap-2.5 min-w-0">
                          <span className="text-xl shrink-0 p-1.5 rounded-xl bg-slate-50 border border-slate-200/70 shadow-2xs">
                            {sub.icon}
                          </span>
                          <div className="min-w-0">
                            <h3 
                              className="text-base font-extrabold text-slate-900 leading-tight truncate" 
                              style={{ fontFamily: 'Afacad, sans-serif' }}
                            >
                              {sub.name}
                            </h3>
                            <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider block mt-0.5">
                              Grade {grade}
                            </span>
                          </div>
                        </div>
                        <span 
                          className="px-2.5 py-1 rounded-full font-extrabold text-[10px] shadow-2xs shrink-0"
                          style={{
                            backgroundColor: isDiagnostic ? theme.soft : theme.base,
                            color: isDiagnostic ? theme.text : '#ffffff'
                          }}
                        >
                          {isDiagnostic ? 'Diagnostic' : `${mastery}% Mastery`}
                        </span>
                      </div>
                      <div className="pt-2 border-t border-slate-100 flex items-center justify-between text-xs">
                        <span className="text-[11px] text-slate-500 font-medium truncate">
                          Current Topic: <strong className="text-slate-800 font-semibold">{defaultTopic}</strong>
                        </span>
                      </div>
                      <button
                        type="button"
                        data-testid={`btn-launch-${sub.id}`}
                        onClick={() => onSelectTab(sub.id)}
                        className="mt-2.5 w-full py-2.5 text-white text-xs font-bold rounded-xl transition cursor-pointer shadow-xs min-h-[44px] flex items-center justify-center gap-1.5 hover:opacity-95 active:scale-98"
                        style={{ backgroundColor: theme.base }}
                      >
                        <span>Launch Practice →</span>
                      </button>
                    </div>
                  );
                })}
              </div>

              {/* Ergonomic Manage Subjects Action Card */}
              {onOpenManageSubjects && (
                <button
                  type="button"
                  data-testid="btn-manage-enrolled-subjects-mobile"
                  onClick={onOpenManageSubjects}
                  className="w-full py-3 px-4 rounded-2xl bg-white border border-dashed border-emerald-300 hover:border-emerald-500 text-emerald-800 hover:bg-emerald-50/50 text-xs font-bold transition flex items-center justify-between shadow-2xs cursor-pointer group mt-2"
                >
                  <div className="flex items-center gap-2.5">
                    <span className="text-base group-hover:rotate-45 transition-transform">⚙️</span>
                    <span>Customize Enrolled Phase Subjects</span>
                  </div>
                  <span className="text-[11px] font-mono bg-emerald-100 text-emerald-800 px-2.5 py-0.5 rounded-lg font-extrabold">
                    {enrolledPhaseSubjects.length} Active
                  </span>
                </button>
              )}
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
                    Offline Storage Cache
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
              data-testid={`tab-${sub.id}`}
              ref={isActive ? activeBtnRef : null}
              type="button"
              onClick={() => {
                if (isActive && sub.id === 'desk') {
                  contentScrollRef.current?.scrollTo({ top: 0, behavior: 'smooth' });
                } else {
                  onSelectTab(sub.id);
                }
              }}
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

      {/* Logout Confirmation Modal for Mobile */}
      {showLogoutConfirm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs">
          <div className="bg-white rounded-2xl p-5 max-w-xs w-full shadow-2xl border border-slate-200 text-center space-y-4">
            <div className="w-12 h-12 rounded-full bg-rose-100 text-rose-600 mx-auto flex items-center justify-center">
              <LogOut className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-base font-bold text-slate-900">Sign Out of Fundile?</h3>
              <p className="text-xs text-slate-500 mt-1">Your learning progress and streak are saved safely.</p>
            </div>
            <div className="flex items-center gap-2 pt-2">
              <button
                type="button"
                onClick={() => setShowLogoutConfirm(false)}
                className="flex-1 py-2 px-3 rounded-xl border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-50 transition cursor-pointer"
              >
                Cancel
              </button>
              <button
                type="button"
                data-testid="btn-confirm-logout"
                onClick={() => {
                  setShowLogoutConfirm(false);
                  if (typeof onLogout === 'function') onLogout();
                }}
                className="flex-1 py-2 px-3 rounded-xl bg-rose-600 hover:bg-rose-700 text-xs font-bold text-white shadow-xs cursor-pointer transition"
              >
                Sign Out
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}
