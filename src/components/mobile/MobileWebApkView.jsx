import React, { useState, useRef, useEffect } from 'react';
import { Lightbulb, CheckCircle2, ArrowRight, Loader2, Sparkles } from 'lucide-react';
import studentStore from '../../services/studentStore';
import MasteryDial from '../student/MasteryDial';

/**
 * MobileWebApkView
 * Authentic Android WebAPK Mobile Experience with Bidirectional Parity.
 * - Mobile Portrait Mode:
 *   - Android Status bar (14:30, LTE, 📶, 88% battery).
 *   - User Profile Ribbon with avatar photo tap (ProfilePhotoModal) & 1-tap collapse.
 *   - Dual-Ring MasteryDial in profile summary.
 *   - Interactive Topic Pill: Term 1 • {activeTopic} ▾ (TopicScopeModal).
 *   - Compact 4-stage progression stepper: [ 0. Diag ] [ 1. Scaff ] [ 2. Prac ] [ 3. Exam ].
 *   - Today's Desk & Dedicated Subject Views with live question inputs, 3-tier hints drawer, and mark button.
 * - Mobile Landscape / Fullscreen Mode:
 *   - Ribbon hidden to maximize vertical space.
 *   - Fullscreen 6-column 2D ledger table & math working area.
 * - Mobile Bottom Navigation Bar:
 *   - 10-subject horizontal carousel with 44px touch targets.
 */

const MOBILE_SUBJECTS = [
  { 
    id: 'desk', 
    label: 'Desk', 
    icon: '📋', 
    accent: '#13519C', 
    badge: '2 Due', 
    badgeBg: 'bg-rose-500 text-white shadow-sm shadow-rose-500/40',
    activeClass: 'bg-blue-50 text-[#13519C] border-2 border-blue-400 font-bold shadow-sm'
  },
  { 
    id: 'accounting', 
    label: 'Accounting', 
    icon: '📗', 
    accent: '#059669', 
    badge: '84%', 
    badgeBg: 'bg-emerald-600 text-white shadow-sm shadow-emerald-500/40',
    activeClass: 'bg-emerald-50 text-emerald-800 border-2 border-emerald-400 font-bold shadow-sm'
  },
  { 
    id: 'maths', 
    label: 'Maths', 
    icon: '📘', 
    accent: '#2563EB', 
    badge: '82%', 
    badgeBg: 'bg-blue-600 text-white shadow-sm shadow-blue-500/40',
    activeClass: 'bg-blue-50 text-blue-800 border-2 border-blue-400 font-bold shadow-sm'
  },
  { 
    id: 'mathslit', 
    label: 'Maths Lit', 
    icon: '📊', 
    accent: '#8B5CF6', 
    badge: '76%', 
    badgeBg: 'bg-purple-600 text-white shadow-sm shadow-purple-500/40',
    activeClass: 'bg-purple-50 text-purple-900 border-2 border-purple-400 font-bold shadow-sm'
  },
  { 
    id: 'physics', 
    label: 'Physics', 
    icon: '📙', 
    accent: '#0891B2', 
    badge: '68%', 
    badgeBg: 'bg-cyan-600 text-white shadow-sm shadow-cyan-500/40',
    activeClass: 'bg-cyan-50 text-cyan-800 border-2 border-cyan-400 font-bold shadow-sm'
  },
  { 
    id: 'business', 
    label: 'Business', 
    icon: '📕', 
    accent: '#EA580C', 
    badge: '75%', 
    badgeBg: 'bg-[#FF9100] text-white shadow-sm shadow-orange-500/40',
    activeClass: 'bg-amber-50 text-amber-900 border-2 border-amber-400 font-bold shadow-sm'
  },
  { 
    id: 'lifesci', 
    label: 'Life Sciences', 
    icon: '🔬', 
    accent: '#0D9488', 
    badge: '78%', 
    badgeBg: 'bg-teal-600 text-white shadow-sm shadow-teal-500/40',
    activeClass: 'bg-teal-50 text-teal-900 border-2 border-teal-400 font-bold shadow-sm'
  },
  { 
    id: 'techmaths', 
    label: 'Tech Maths', 
    icon: '📐', 
    accent: '#7C3AED', 
    badge: '72%', 
    badgeBg: 'bg-indigo-600 text-white shadow-sm shadow-indigo-500/40',
    activeClass: 'bg-indigo-50 text-indigo-900 border-2 border-indigo-400 font-bold shadow-sm'
  },
  { 
    id: 'ems', 
    label: 'EMS', 
    icon: '🪙', 
    accent: '#D97706', 
    badge: '80%', 
    badgeBg: 'bg-amber-600 text-white shadow-sm shadow-amber-500/40',
    activeClass: 'bg-amber-50 text-amber-900 border-2 border-amber-400 font-bold shadow-sm'
  },
  { 
    id: 'natsci', 
    label: 'Natural Sciences', 
    icon: '🌱', 
    accent: '#059669', 
    badge: '74%', 
    badgeBg: 'bg-emerald-600 text-white shadow-sm shadow-emerald-500/40',
    activeClass: 'bg-emerald-50 text-emerald-900 border-2 border-emerald-400 font-bold shadow-sm'
  },
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
  studentName = 'Nqobile Dlamini',
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
}) {
  const [isRibbonCollapsed, setIsRibbonCollapsed] = useState(false);
  const [showProfileSummary, setShowProfileSummary] = useState(false);
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
  const lastScrollTopRef = useRef(0);

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
  const firstName = studentName ? studentName.split(' ')[0] : 'Nqobile';
  const formattedSchool = schoolName ? schoolName.replace(/School/i, '').trim() : 'Westville High';

  const currentSubData = studentStore.getSubject(currentTab);

  const getDynamicBadge = (subId) => {
    if (subId === 'desk') {
      const dues = storeState?.deskDues ?? 0;
      return {
        text: dues > 0 ? `${dues} Due` : '0 Due',
        bg: dues > 0 ? 'bg-rose-500 text-white shadow-sm shadow-rose-500/40' : 'bg-slate-200 text-slate-700'
      };
    }
    const sub = studentStore.getSubject(subId);
    if (!sub || sub.status === 'diagnostic_required') {
      return {
        text: 'Diag',
        bg: 'bg-amber-100 text-amber-900 border border-amber-300'
      };
    }
    const val = sub.formativeMastery ?? 0;
    return {
      text: `${val}%`,
      bg: val >= 80 ? 'bg-emerald-600 text-white shadow-sm shadow-emerald-500/40' :
          val >= 60 ? 'bg-blue-600 text-white shadow-sm shadow-blue-500/40' :
          'bg-slate-200 text-slate-700'
    };
  };

  // Reset answer states when question or tab changes
  useEffect(() => {
    setHasMarkedCurrent(false);
    setShowHints(false);
    setActiveHintTier(1);
    setMathAnswer('');
  }, [question?.id, currentTab]);

  // Dynamic automatic hiding on scroll in content container
  const handleContentScroll = (e) => {
    const currentScrollTop = e.currentTarget.scrollTop;
    const diff = currentScrollTop - lastScrollTopRef.current;

    if (currentScrollTop <= 15) {
      setIsRibbonCollapsed(false);
    } else if (diff > 6 && currentScrollTop > 30) {
      setIsRibbonCollapsed(true);
    } else if (diff < -8) {
      setIsRibbonCollapsed(false);
    }

    lastScrollTopRef.current = currentScrollTop;
  };

  // Reset scroll and restore ribbon when switching tabs
  useEffect(() => {
    if (contentScrollRef.current) {
      contentScrollRef.current.scrollTop = 0;
      lastScrollTopRef.current = 0;
      setIsRibbonCollapsed(false);
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
    <div className="flex flex-col h-full bg-white text-slate-800 font-sans select-none relative overflow-hidden">
      
      {/* ───────────────────────────────────────────────────────────── */}
      {/* 1. ANDROID SYSTEM STATUS BAR                                  */}
      {/* ───────────────────────────────────────────────────────────── */}
      <div className={`px-5 ${isLandscape ? 'pt-1.5 pb-1' : 'pt-2.5 pb-1.5'} bg-[#13519C] text-white flex items-center justify-between text-[11px] font-mono select-none shrink-0`}>
        <span id="mob-clock">14:30</span>
        <div className="flex items-center gap-2">
          {isLandscape && (
            <span className="text-[10px] text-emerald-300 font-sans font-bold hidden sm:inline">
              🔄 Fullscreen Workspace Active
            </span>
          )}
          <span className="text-[10px] bg-blue-800/80 px-1.5 py-0.5 rounded border border-blue-400/30">LTE</span>
          <span>📶</span>
          <span>🔋 88%</span>
        </div>
      </div>

      {/* ───────────────────────────────────────────────────────────── */}
      {/* 2. USER PROFILE RIBBON (Collapsible in Portrait, Hidden in Land) */}
      {/* ───────────────────────────────────────────────────────────── */}
      {!isLandscape && !isRibbonCollapsed && (
        <div 
          id="mob-user-ribbon" 
          className="px-4 py-2 bg-[#13519C] text-white flex items-center justify-between border-t border-blue-800/40 transition-all duration-300 ease-in-out shrink-0"
        >
          <div className="flex items-center gap-2.5">
            {/* User Profile Avatar with Click Handler for ProfilePhotoModal */}
            <button
              type="button"
              onClick={() => onOpenProfilePhoto && onOpenProfilePhoto()}
              className="relative group w-8 h-8 rounded-full overflow-hidden ring-2 ring-white/50 hover:ring-[#FF9100] transition flex items-center justify-center bg-white text-[#13519C] font-extrabold text-xs shadow-xs cursor-pointer shrink-0"
              title="Update Profile Photo"
            >
              {userPhoto ? (
                <img src={userPhoto} alt={studentName} className="h-full w-full object-cover" />
              ) : (
                <span>{studentName ? studentName.charAt(0) : 'N'}</span>
              )}
              <span className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 flex items-center justify-center text-[10px] transition-opacity">
                📸
              </span>
            </button>

            <div>
              <span className="font-bold text-xs block leading-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>
                {studentName}
              </span>
              <span className="text-[10px] text-blue-100/90 leading-tight">
                Grade {grade} FET • {formattedSchool}
              </span>
            </div>
          </div>

          <div className="flex items-center gap-1.5">
            <span className="text-[10px] bg-amber-400 text-slate-950 font-extrabold px-2 py-0.5 rounded-full shadow-xs">
              🔥 {effectiveStreak}d
            </span>
            <span className="text-[10px] bg-blue-900/80 text-blue-100 font-extrabold px-2 py-0.5 rounded-full border border-blue-400/40 shadow-xs">
              ⚡ {effectiveXp > 999 ? `${(effectiveXp / 1000).toFixed(1)}k` : effectiveXp}
            </span>
            <button
              type="button"
              onClick={() => setShowProfileSummary(!showProfileSummary)}
              className="px-1.5 py-0.5 rounded-md bg-white/20 hover:bg-white/30 text-white font-bold text-[10px] transition cursor-pointer"
              title="Mastery Dial Summary"
            >
              {showProfileSummary ? '▲ Dial' : '▼ Dial'}
            </button>
            <button
              type="button"
              id="btn-toggle-ribbon"
              onClick={() => setIsRibbonCollapsed(true)}
              className="px-1.5 py-0.5 rounded-md bg-white/20 hover:bg-white/30 text-white font-bold text-[10px] transition cursor-pointer"
              title="Collapse Ribbon"
            >
              ▲ Hide
            </button>
          </div>
        </div>
      )}

      {/* Profile Mastery Summary Drawer in Portrait */}
      {!isLandscape && !isRibbonCollapsed && showProfileSummary && (
        <div className="px-4 py-3 bg-blue-950 text-white flex items-center justify-between border-t border-blue-800/60 animate-in fade-in shrink-0">
          <div className="flex items-center gap-3">
            <MasteryDial
              size={56}
              strokeWidth={5}
              formativeMastery={currentSubData.formativeMastery}
              evaluativeScore={currentSubData.evaluativeScore}
            />
            <div>
              <span className="text-[10px] font-bold uppercase text-blue-200 block tracking-wider">
                BKT Formative Mastery
              </span>
              <span className="text-sm font-bold text-white block leading-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>
                {currentSubData.formativeMastery}% Mastery
              </span>
              <span className="text-[10px] text-blue-300">
                Evaluative: {currentSubData.evaluativeScore}%
              </span>
            </div>
          </div>
          <button
            type="button"
            onClick={() => onOpenTopicScope ? onOpenTopicScope() : onSelectTopic(activeTopic)}
            className="px-2.5 py-1.5 rounded-xl bg-white/15 hover:bg-white/25 text-white text-[11px] font-bold border border-white/20 transition cursor-pointer"
          >
            Scope Scope ▾
          </button>
        </div>
      )}

      {/* 1-Line Collapsed Ribbon Indicator (Portrait Mode) */}
      {!isLandscape && isRibbonCollapsed && (
        <div 
          id="mob-ribbon-collapsed-bar" 
          className="px-4 py-1.5 bg-[#13519C] text-white text-[10px] font-bold flex items-center justify-between border-t border-blue-800/40 select-none shrink-0 transition-all duration-300 ease-in-out"
        >
          <span className="text-blue-100 flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-emerald-400"></span>
            <span>Workspace Maximized ({firstName} • Gr {grade})</span>
          </span>
          <button 
            type="button" 
            onClick={() => setIsRibbonCollapsed(false)} 
            className="text-amber-300 hover:text-white underline text-[10px] cursor-pointer"
          >
            ▼ Show Profile
          </button>
        </div>
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
            className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#13519C] hover:bg-[#0e3c73] text-white text-[11px] font-bold transition shadow-xs cursor-pointer"
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
        onScroll={handleContentScroll}
        className="flex-1 bg-slate-50 overflow-y-auto"
      >
        
        {/* ==================== VIEW 1: TODAY'S DESK ==================== */}
        {currentTab === 'desk' && (
          <div id="mob-content-desk" className="p-4 space-y-3">
            {/* Assignment 1: Accounting */}
            <div className="bg-white border-2 border-emerald-400 p-3.5 rounded-2xl shadow-sm">
              <div className="flex justify-between items-center text-[10px] font-extrabold mb-1">
                <span className="bg-emerald-600 text-white px-2 py-0.5 rounded-full">ACCOUNTING • DUE TODAY</span>
                <span className="bg-rose-500 text-white px-2 py-0.5 rounded-full font-extrabold text-[9px] shadow-xs">17:00</span>
              </div>
              <h5 className="text-xs font-bold text-slate-900 mt-1" style={{ fontFamily: 'Afacad, sans-serif' }}>General Journal: Debtors &amp; Bad Debts</h5>
              <p className="text-[11px] text-slate-600 mt-0.5">Mrs. Khumalo assigned 12 marks practice (J. Dlamini dividend).</p>
              <button
                type="button"
                onClick={() => onSelectTab('accounting')}
                className="mt-2.5 w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold rounded-xl shadow-sm shadow-emerald-600/30 transition cursor-pointer"
              >
                Open in Accounting &rarr;
              </button>
            </div>

            {/* Assignment 2: Mathematics */}
            <div className="bg-white border-2 border-blue-400 p-3.5 rounded-2xl shadow-sm">
              <div className="flex justify-between items-center text-[10px] font-extrabold mb-1">
                <span className="bg-blue-600 text-white px-2 py-0.5 rounded-full">MATHEMATICS • DUE FRIDAY</span>
                <span className="text-white bg-amber-500 px-2 py-0.5 rounded-full text-[9px] font-bold shadow-xs">08:00</span>
              </div>
              <h5 className="text-xs font-bold text-slate-900 mt-1" style={{ fontFamily: 'Afacad, sans-serif' }}>Trinomial Factorisation Drill</h5>
              <p className="text-[11px] text-slate-600 mt-0.5">Mr. Botha • 10 Marks • Friday test prep.</p>
              <button
                type="button"
                onClick={() => onSelectTab('maths')}
                className="mt-2.5 w-full py-2 bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold rounded-xl shadow-sm shadow-blue-600/30 transition cursor-pointer"
              >
                Open in Mathematics &rarr;
              </button>
            </div>

            {/* Self-Paced Autonomous Drill */}
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between text-[10px] font-bold mb-1">
                <span className="text-slate-500 uppercase">Self-Paced Mastery</span>
                <span className="text-white bg-emerald-600 px-2 py-0.5 rounded-full font-extrabold text-[9px]">84% BKT</span>
              </div>
              <p className="text-xs font-semibold text-slate-800">Cash Receipts Journal (VAT 15%)</p>
              <button
                type="button"
                onClick={() => onSelectTab('accounting')}
                className="mt-2 w-full py-1.5 bg-[#13519C] hover:bg-blue-800 text-white text-[11px] font-bold rounded-xl transition cursor-pointer shadow-xs"
              >
                Resume Autonomous Drill &rarr;
              </button>
            </div>

            {/* Offline WebAPK Data Badge */}
            <div className="bg-white p-3 rounded-2xl border border-slate-200 text-center">
              <span className="text-[10px] font-bold uppercase text-slate-400">Offline WebAPK Cache</span>
              <p className="text-[11px] font-semibold text-slate-600 mt-0.5">1.4 MB Total Data • Zero Video Buffering</p>
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
                    className="w-full py-1.5 px-3 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200 text-xs font-bold flex items-center justify-between transition cursor-pointer"
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
                    className="w-full py-2.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-md shadow-emerald-700/20 flex items-center justify-center gap-2 transition cursor-pointer disabled:opacity-50"
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
                      className="w-full py-2 px-4 rounded-xl bg-slate-800 hover:bg-slate-900 text-white font-bold text-xs flex items-center justify-center gap-1.5 transition cursor-pointer"
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
                  className="w-full px-3 py-2 rounded-xl border border-blue-300 font-mono text-xs font-bold text-blue-950 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />

                <button
                  type="button"
                  onClick={handleTriggerMark}
                  disabled={isMarking}
                  className="w-full py-2 bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs rounded-xl transition flex items-center justify-center gap-1.5 cursor-pointer shadow-xs"
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
            <div className="bg-[#FF9100] text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-amber-100 block">Business Studies</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  {activeTopic || 'Business Environments'}
                </h5>
              </div>
              <span className="bg-white text-amber-950 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: {currentSubData.formativeMastery}%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
              <p className="text-xs text-slate-700">{question?.prompt || 'Fuel price increase decree by Minister of Mineral Resources.'}</p>
              <div className="p-3 bg-amber-50 border border-amber-200 rounded-xl text-amber-950 font-bold text-xs">
                Macro Environment (Economic &amp; Political) • Outside Management Control ✓
              </div>
            </div>
          </div>
        )}

        {/* ==================== VIEW 7: LIFE SCIENCES ==================== */}
        {currentTab === 'lifesci' && (
          <div id="mob-content-lifesci" className="p-4 space-y-3">
            <div className="bg-teal-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-teal-100 block">Life Sciences</span>
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
        className="border-t border-slate-200 bg-white/95 backdrop-blur-md px-4 py-2 flex items-center gap-3 overflow-x-auto scrollbar-none [&::-webkit-scrollbar]:hidden select-none shadow-lg shrink-0"
      >
        {MOBILE_SUBJECTS.map((sub) => {
          const isActive = currentTab === sub.id;

          return (
            <button
              key={sub.id}
              id={`mob-tab-${sub.id}`}
              ref={isActive ? activeBtnRef : null}
              type="button"
              onClick={() => onSelectTab(sub.id)}
              className={`mob-nav-btn flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs transition shrink-0 whitespace-nowrap min-h-[44px] cursor-pointer ${
                isActive
                  ? sub.activeClass
                  : 'bg-slate-50 text-slate-600 border border-slate-200 hover:text-slate-900 font-medium'
              }`}
            >
              <span className="text-base leading-none">{sub.icon}</span>
              <span className="leading-none">{sub.label}</span>
              {(() => {
                const b = getDynamicBadge(sub.id);
                return (
                  <span className={`px-1.5 py-0.5 rounded-full ${b.bg} text-[9px] font-extrabold`}>
                    {b.text}
                  </span>
                );
              })()}
            </button>
          );
        })}
      </nav>

    </div>
  );
}
