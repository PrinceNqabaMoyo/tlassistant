import React, { useState, useRef, useEffect } from 'react';

/**
 * MobileWebApkView
 * Authentic Android WebAPK Mobile Experience.
 * Exactly mirrors the dedicated mobile design from fundile-learner-journey-prototype.html (lines 755 - 1145):
 * - Mobile Portrait Mode:
 *   - Android Status bar (14:30, LTE, 📶, 88% battery).
 *   - User Profile Ribbon with 1-tap [ ▲ Hide ] collapse toggle into 1-line indicator.
 *   - Today's Desk: Mobile-optimized assignment cards (Accounting due today 17:00, Maths due Friday 08:00, autonomous drill, offline cache).
 *   - Accounting Subject View in Portrait: Compact 2x2 card grid (Bank Gross 115%, Sales Excl 100%, Output VAT 15%, Cost of Sales) + Tier 3 hint.
 *   - Maths, Physics, Business Studies, Life Sciences, Tech Maths native cards.
 * - Mobile Landscape / Fullscreen Mode:
 *   - User Ribbon is AUTOMATICALLY HIDDEN to maximize vertical screen space.
 *   - Minimal landscape status bar.
 *   - Fullscreen 6-column 2D ledger table (Day, Details, Bank, Sales, Output VAT, Cost of Sales) with live inputs, Tier 3 hint, and marks award.
 * - Mobile Bottom Navigation Bar:
 *   - Pinned to the bottom.
 *   - Smooth horizontal scrolling carousel (scrollbar-none) with all 7 subjects.
 *   - Active subject highlighted with jewel-tone border and background.
 *   - Guaranteed 44px min touch targets.
 *   - Auto-scrolls active tab to center when selected.
 */

export const MOBILE_SUBJECTS = [
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
];

export const normalizeTabId = (id) => {
  if (!id) return 'desk';
  const clean = String(id).toLowerCase().trim();
  if (clean === 'maths' || clean === 'mathematics') return 'maths';
  if (clean === 'physics' || clean === 'physical_sciences') return 'physics';
  if (clean === 'business' || clean === 'business_studies') return 'business';
  if (clean === 'lifesci' || clean === 'life_sciences') return 'lifesci';
  if (clean === 'techmaths' || clean === 'technical_mathematics') return 'techmaths';
  if (clean === 'accounting') return 'accounting';
  return 'desk';
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
}) {
  const [isRibbonCollapsed, setIsRibbonCollapsed] = useState(false);
  const bottomNavRef = useRef(null);
  const activeBtnRef = useRef(null);
  const contentScrollRef = useRef(null);
  const lastScrollTopRef = useRef(0);

  const currentTab = normalizeTabId(activeTab);
  const isLandscape = orientation === 'landscape';
  const firstName = studentName ? studentName.split(' ')[0] : 'Nqobile';
  const formattedSchool = schoolName ? schoolName.replace(/School/i, '').trim() : 'Westville High';

  // Accounting live cell inputs in landscape mode
  const [ledgerInputs, setLedgerInputs] = useState({
    bank: '11 500',
    sales: '10 000',
    vat: '1 500',
  });

  // Dynamic automatic hiding on scroll in content container
  const handleContentScroll = (e) => {
    const currentScrollTop = e.currentTarget.scrollTop;
    const diff = currentScrollTop - lastScrollTopRef.current;

    if (currentScrollTop <= 15) {
      // Near top: automatically show the ribbon again
      setIsRibbonCollapsed(false);
    } else if (diff > 6 && currentScrollTop > 30) {
      // Scrolling down: automatically collapse ribbon to maximize question/ledger screen real estate
      setIsRibbonCollapsed(true);
    } else if (diff < -8) {
      // Scrolling up: automatically restore ribbon
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

  return (
    <div className="flex flex-col h-full bg-white text-slate-800 font-sans select-none relative overflow-hidden">
      
      {/* ───────────────────────────────────────────────────────────── */}
      {/* 1. ANDROID SYSTEM STATUS BAR                                  */}
      {/* ───────────────────────────────────────────────────────────── */}
      <div className={`px-6 ${isLandscape ? 'pt-2 pb-1.5' : 'pt-3 pb-2'} bg-[#13519C] text-white flex items-center justify-between text-[11px] font-mono select-none shrink-0`}>
        <span id="mob-clock">14:30</span>
        <div className="flex items-center gap-2">
          {isLandscape && (
            <span className="text-[10px] text-emerald-300 font-sans font-bold hidden sm:inline">
              🔄 Fullscreen 6-Col Ledger Active
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
          className="px-4 py-2.5 bg-[#13519C] text-white flex items-center justify-between border-t border-blue-800/40 transition-all duration-300 ease-in-out shrink-0"
        >
          <div className="flex items-center gap-2.5">
            <div className="w-7 h-7 rounded-full bg-white text-[#13519C] flex items-center justify-center font-extrabold text-xs shadow-xs">
              {studentName ? studentName.charAt(0) : 'N'}
            </div>
            <div>
              <span className="font-bold text-xs block leading-tight">{studentName}</span>
              <span className="text-[10px] text-blue-100/90 leading-tight">Grade {grade} FET • {formattedSchool}</span>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-[10px] bg-amber-400 text-slate-950 font-extrabold px-2 py-0.5 rounded-full shadow-xs">
              🔥 {streakDays}d
            </span>
            <span className="text-[10px] bg-blue-900/80 text-blue-100 font-extrabold px-2 py-0.5 rounded-full border border-blue-400/40 shadow-xs">
              ⚡ 1.4k
            </span>
            {/* 1-Tap Ribbon Collapse Button in Portrait Mode */}
            <button
              type="button"
              id="btn-toggle-ribbon"
              onClick={() => setIsRibbonCollapsed(true)}
              className="ml-1 px-2 py-0.5 rounded-md bg-white/20 hover:bg-white/30 text-white font-bold text-[10px] flex items-center gap-1 transition cursor-pointer"
              title="Collapse Profile Ribbon to Maximize Workspace"
            >
              <span>▲</span>
              <span>Hide</span>
            </button>
          </div>
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
      {/* 3. MOBILE INTERACTIVE CONTENT VIEWS                            */}
      {/* ───────────────────────────────────────────────────────────── */}
      <div 
        ref={contentScrollRef}
        onScroll={handleContentScroll}
        className="flex-1 bg-slate-50 overflow-y-auto"
      >
        
        {/* ==================== MOBILE VIEW 1: TODAY'S DESK ==================== */}
        {currentTab === 'desk' && (
          <div id="mob-content-desk" className="p-4 space-y-3">
            {/* Assignment 1: Accounting */}
            <div className="bg-white border-2 border-emerald-400 p-3.5 rounded-2xl shadow-sm">
              <div className="flex justify-between items-center text-[10px] font-extrabold mb-1">
                <span className="bg-emerald-600 text-white px-2 py-0.5 rounded-full">ACCOUNTING • DUE TODAY</span>
                <span className="bg-rose-500 text-white px-2 py-0.5 rounded-full font-extrabold text-[9px] shadow-xs">17:00</span>
              </div>
              <h5 className="text-xs font-bold text-slate-900 mt-1">General Journal: Debtors &amp; Bad Debts</h5>
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
              <h5 className="text-xs font-bold text-slate-900 mt-1">Trinomial Factorisation Drill</h5>
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

        {/* ==================== MOBILE VIEW 2: ACCOUNTING (Dual-Mode) ==================== */}
        {currentTab === 'accounting' && (
          <div id="mob-content-accounting" className="p-4 space-y-3">
            {/* Subject Header */}
            <div className="bg-emerald-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-emerald-100 block">Grade 10 Accounting</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5">Topic 1.1: CRJ &amp; 15% VAT</h5>
              </div>
              <span className="bg-white text-emerald-800 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: 84%
              </span>
            </div>

            {/* (A) PORTRAIT VIEW: Compact 2x2 Card Grid */}
            {!isLandscape ? (
              <div id="mob-accounting-portrait-cards" className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                <div className="flex items-center justify-between text-xs pb-1 border-b border-slate-100">
                  <span className="text-[10px] font-bold uppercase text-slate-500">2D Ledger Inputs</span>
                  <span className="text-[10px] font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded border border-amber-200">6 Marks</span>
                </div>
                <div className="grid grid-cols-2 gap-2 text-xs">
                  <div className="p-2.5 bg-emerald-50 rounded-xl border border-emerald-200">
                    <span className="text-[10px] text-slate-600 block font-semibold">Bank (Gross 115%)</span>
                    <span className="font-mono font-bold text-emerald-800 text-sm">R 11 500</span>
                  </div>
                  <div className="p-2.5 bg-emerald-50 rounded-xl border border-emerald-200">
                    <span className="text-[10px] text-slate-600 block font-semibold">Sales (Excl 100%)</span>
                    <span className="font-mono font-bold text-emerald-800 text-sm">R 10 000</span>
                  </div>
                  <div className="p-2.5 bg-emerald-50 rounded-xl border border-emerald-200">
                    <span className="text-[10px] text-slate-600 block font-semibold">Output VAT (15%)</span>
                    <span className="font-mono font-bold text-emerald-800 text-sm">R 1 500</span>
                  </div>
                  <div className="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                    <span className="text-[10px] text-slate-600 block font-semibold">Cost of Sales</span>
                    <span className="font-mono font-bold text-slate-700 text-sm">R 8 000</span>
                  </div>
                </div>
                <div className="p-2.5 bg-amber-50 rounded-xl border border-amber-200 text-[11px] text-amber-900">
                  <span className="font-bold text-amber-800">Tier 3 Hint:</span> R11,500 × 15/115 = R1,500 VAT.
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
                  <span className="font-extrabold text-white bg-emerald-600 px-2.5 py-0.5 rounded text-[10px]">6/6 Marks Credited</span>
                </div>
              </div>
            )}
          </div>
        )}

        {/* ==================== MOBILE VIEW 3: MATHEMATICS ==================== */}
        {currentTab === 'maths' && (
          <div id="mob-content-maths" className="p-4 space-y-3">
            <div className="bg-blue-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-blue-100 block">Grade 10 Mathematics</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5">Trinomial Factorisation</h5>
              </div>
              <span className="bg-white text-blue-900 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: 82%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
              <span className="text-[10px] font-bold uppercase text-slate-400">Step-by-Step KaTeX Keypad</span>
              <p className="text-xs font-bold text-slate-800">Factorise: x² − 7x + 12</p>
              <div className="p-3 bg-blue-50 border border-blue-200 rounded-xl text-blue-950 font-bold text-xs font-mono">
                (x − 3)(x − 4) ✓ Equivalence Confirmed
              </div>
              <p className="text-[11px] text-slate-500">SymPy symbolic engine verified: (−3) + (−4) = −7 and (−3) × (−4) = +12.</p>
            </div>
          </div>
        )}

        {/* ==================== MOBILE VIEW 4: PHYSICAL SCIENCES ==================== */}
        {currentTab === 'physics' && (
          <div id="mob-content-physics" className="p-4 space-y-3">
            <div className="bg-cyan-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-cyan-100 block">Physical Sciences</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5">1D Constant Acceleration</h5>
              </div>
              <span className="bg-white text-cyan-900 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: 68%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
              <p className="text-xs text-slate-700">Trolley accelerates from rest at 2,5 m/s² for 4 s.</p>
              <div className="p-3 bg-cyan-50 border border-cyan-200 rounded-xl text-cyan-950 font-mono font-bold text-xs">
                vf = 0 + (2,5)(4) = 10,0 m/s
              </div>
            </div>
          </div>
        )}

        {/* ==================== MOBILE VIEW 5: BUSINESS STUDIES ==================== */}
        {currentTab === 'business' && (
          <div id="mob-content-business" className="p-4 space-y-3">
            <div className="bg-[#FF9100] text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-amber-100 block">Business Studies</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5">Business Environments</h5>
              </div>
              <span className="bg-white text-amber-950 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: 75%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
              <p className="text-xs text-slate-700">Fuel price increase decree by Minister of Mineral Resources.</p>
              <div className="p-3 bg-amber-50 border border-amber-200 rounded-xl text-amber-950 font-bold text-xs">
                Macro Environment (Economic &amp; Political) • Outside Management Control
              </div>
            </div>
          </div>
        )}

        {/* ==================== MOBILE VIEW 6: LIFE SCIENCES ==================== */}
        {currentTab === 'lifesci' && (
          <div id="mob-content-lifesci" className="p-4 space-y-3">
            <div className="bg-teal-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-teal-100 block">Life Sciences</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5">Cell Division &amp; Mitosis</h5>
              </div>
              <span className="bg-white text-teal-950 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: 78%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
              <p className="text-xs text-slate-700">Sister chromatids separating towards opposite poles.</p>
              <div className="p-3 bg-teal-50 border border-teal-200 rounded-xl text-teal-950 font-bold text-xs">
                Anaphase (Spindle Fiber Contraction) ✓
              </div>
            </div>
          </div>
        )}

        {/* ==================== MOBILE VIEW 7: TECH MATHS ==================== */}
        {currentTab === 'techmaths' && (
          <div id="mob-content-techmaths" className="p-4 space-y-3">
            <div className="bg-indigo-600 text-white p-3.5 rounded-2xl shadow-sm flex items-center justify-between">
              <div>
                <span className="text-[10px] font-extrabold uppercase tracking-wider text-indigo-100 block">Tech Maths</span>
                <h5 className="text-xs font-extrabold text-white mt-0.5">Mensuration &amp; Trig</h5>
              </div>
              <span className="bg-white text-indigo-950 font-extrabold px-2.5 py-1 rounded-lg text-[10px] shadow-xs">
                Mastery: 72%
              </span>
            </div>
            <div className="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2 font-mono text-xs">
              <p className="text-slate-700 font-sans">Sides 6 cm and 8 cm right-angled triangle.</p>
              <div className="p-3 bg-indigo-50 border border-indigo-200 rounded-xl text-indigo-950 font-bold">
                r = √(6² + 8²) = 10 cm &bull; sin(θ) = 0.6 ✓
              </div>
            </div>
          </div>
        )}

      </div>

      {/* ───────────────────────────────────────────────────────────── */}
      {/* 4. MOBILE BOTTOM SWIPEABLE CAROUSEL (7 Subjects, 44px touch)  */}
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
              {sub.badge && (
                <span className={`px-1.5 py-0.5 rounded-full ${sub.badgeBg} text-[9px] font-extrabold`}>
                  {sub.badge}
                </span>
              )}
            </button>
          );
        })}
      </nav>

    </div>
  );
}
