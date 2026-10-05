import React, { useState, useEffect } from 'react';
import { 
  Monitor, 
  Smartphone, 
  RotateCw, 
  Maximize2,
  ShieldAlert,
  RotateCcw
} from 'lucide-react';
import MobileWebApkView from '../mobile/MobileWebApkView';
import SuperAdminProgressResetModal from '../admin/SuperAdminProgressResetModal';
import studentStore from '../../services/studentStore';

/**
 * DevSandboxWrapper
 * Provides an in-browser live testing sandbox for Desktop PWA and Android WebAPK.
 * Faithfully mirrors fundile-learner-journey-prototype.html (lines 712 - 1150):
 * - Windows 11 Desktop PWA with system chrome, address bar pill, user ribbon, folder tabs.
 * - Android WebAPK Mobile with:
 *   - Mobile Ergonomics Bar (#mobile-control-bar): Real-time toggle between Portrait and Landscape/Fullscreen.
 *   - Adaptive Phone Chassis (#mobile-chassis): Smoothly expands between 384px (Portrait) and 768px (Landscape).
 *   - Camera Punch Hole (#mobile-punch-hole) repositioning adaptively.
 *   - Screen Canvas (#mobile-canvas) hosting MobileWebApkView.
 *   - Offline WebAPK capability footer.
 * - Native Responsive Viewport: Adaptive layout separating desktop and mobile cleanly.
 */

export default function DevSandboxWrapper({
  children,
  activeTab = 'desk',
  onSelectTab = () => {},
  currentGrade = 10,
  studentName = 'Prince Moyo',
  schoolName = 'Westville High School',
  streakDays = 5,
  xp = 1420,
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
}) {
  const [sandboxMode, setSandboxMode] = useState('desktop'); // 'desktop' | 'mobile' | 'native'
  const [mobileOrientation, setMobileOrientation] = useState('portrait'); // 'portrait' | 'landscape'
  const [showAdminResetModal, setShowAdminResetModal] = useState(false);

  const [storeState, setStoreState] = useState(() => studentStore.getState());
  useEffect(() => {
    const unsub = studentStore.subscribe((newState) => {
      setStoreState({ ...newState });
    });
    return unsub;
  }, []);

  const effectiveStreak = storeState?.streakDays ?? streakDays;
  const effectiveXp = storeState?.totalXp ?? xp;

  const isLandscape = mobileOrientation === 'landscape';

  const handleSetMobileOrientation = (mode) => {
    setMobileOrientation(mode);
  };

  return (
    <div className="min-h-screen bg-[#050B14] text-slate-100 flex flex-col font-sans selection:bg-[#FF9100]/30 selection:text-white">
      
      {/* ═══════════════════════════════════════════════════════════════ */}
      {/* 1. TOP SANDBOX CONTROLLER TOOLBAR (Real-Time Dev Switcher)       */}
      {/* ═══════════════════════════════════════════════════════════════ */}
      <header className="border-b border-slate-800 bg-[#081326]/95 backdrop-blur-md sticky top-0 z-50 px-4 sm:px-8 py-2.5 flex flex-wrap items-center justify-between gap-3 shadow-lg">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-[#13519C] to-blue-600 flex items-center justify-center font-extrabold text-white text-base shadow-md shadow-blue-900/40">
            F
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-sm font-bold text-white tracking-tight">Fundile Learner Dev Sandbox</span>
              <span className="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 flex items-center gap-1">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>Vite HMR Active</span>
              </span>
            </div>
            <p className="text-[11px] text-slate-400">
              Skeuo-Modern Folder Tabs • Dual-Device Viewport (Windows 11 vs Android WebAPK)
            </p>
          </div>
        </div>

        {/* Viewport Switcher Buttons */}
        <div className="flex items-center gap-1.5 bg-slate-900/90 p-1 rounded-xl border border-slate-700/80 shadow-inner">
          <span className="text-[11px] font-bold text-slate-400 px-2 uppercase tracking-wider hidden md:inline">
            Viewport:
          </span>

          <button
            type="button"
            id="btn-desktop"
            onClick={() => setSandboxMode('desktop')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
              sandboxMode === 'desktop'
                ? 'bg-[#13519C] text-white shadow-xs'
                : 'text-slate-400 hover:text-white hover:bg-slate-800'
            }`}
          >
            <Monitor className="w-3.5 h-3.5" />
            <span>Windows 11 Desktop PWA</span>
          </button>

          <button
            type="button"
            id="btn-mobile"
            onClick={() => setSandboxMode('mobile')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
              sandboxMode === 'mobile'
                ? 'bg-[#13519C] text-white shadow-xs'
                : 'text-slate-400 hover:text-white hover:bg-slate-800'
            }`}
          >
            <Smartphone className="w-3.5 h-3.5" />
            <span>Android WebAPK Mobile</span>
          </button>

          <button
            type="button"
            onClick={() => setSandboxMode('native')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
              sandboxMode === 'native'
                ? 'bg-[#13519C] text-white shadow-xs'
                : 'text-slate-400 hover:text-white hover:bg-slate-800'
            }`}
            title="100% Native Browser Viewport (best for testing on real phone or DevTools)"
          >
            <Maximize2 className="w-3.5 h-3.5" />
            <span className="hidden md:inline">Native Responsive</span>
          </button>

          <button
            type="button"
            onClick={() => setShowAdminResetModal(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer bg-amber-500/20 text-amber-300 border border-amber-500/40 hover:bg-amber-500/30 shadow-xs"
            title="Super Admin: Reset Student Mastery and Dues to 0%"
          >
            <RotateCcw className="w-3.5 h-3.5 text-amber-400" />
            <span>Reset Mastery (0%)</span>
          </button>
        </div>
      </header>

      {/* ═══════════════════════════════════════════════════════════════ */}
      {/* 2. LIVE SANDBOX THEATER STAGE                                   */}
      {/* ═══════════════════════════════════════════════════════════════ */}
      <main className="flex-1 flex flex-col justify-center items-center p-3 sm:p-8 relative overflow-hidden">
        
        {/* Subtle Ambient Radial Glows */}
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-600/10 rounded-full blur-3xl pointer-events-none"></div>
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-[#FF9100]/10 rounded-full blur-3xl pointer-events-none"></div>

        {/* ───────────────────────────────────────────────────────────── */}
        {/* MODE A: WINDOWS 11 DESKTOP PWA CONTAINER                      */}
        {/* ───────────────────────────────────────────────────────────── */}
        {sandboxMode === 'desktop' && (
          <div id="desktop-viewport" className="w-full max-w-6xl rounded-2xl overflow-hidden shadow-2xl border border-slate-700/60 bg-white text-slate-800 transition-all duration-300">
            
            {/* Windows 11 Title Bar & Address Bar */}
            <div className="bg-[#081326] px-4 py-2 border-b border-slate-700/80 flex items-center justify-between select-none">
              <div className="flex items-center gap-3">
                <div className="flex items-center gap-2 px-3 py-1 rounded-lg bg-slate-900/90 border border-slate-700/60 text-xs text-slate-300 font-mono">
                  <span className="text-emerald-400 font-bold">🔒 https://</span>
                  <span>app.fundile.co.za/learner</span>
                </div>
              </div>

              {/* Windows 11 Window Controls */}
              <div className="flex items-center gap-4 text-slate-400 text-xs font-mono select-none">
                <span className="hover:text-white cursor-pointer">─</span>
                <span className="hover:text-white cursor-pointer">□</span>
                <span className="hover:text-rose-400 cursor-pointer">✕</span>
              </div>
            </div>

            {/* Level 2: User Profile Ribbon */}
            <div className="px-6 py-3 bg-[#13519C] text-white flex flex-wrap items-center justify-between gap-3 shadow-inner">
              <div className="flex items-center gap-3">
                <div className="w-8 h-8 rounded-full bg-white text-[#13519C] flex items-center justify-center font-extrabold text-sm shadow-xs">
                  {studentName ? studentName.charAt(0) : 'N'}
                </div>
                <div>
                  <span className="font-bold text-white text-sm block leading-tight">{studentName}</span>
                  <span className="text-xs text-blue-100/90 leading-tight">Grade {currentGrade} FET • {schoolName}</span>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <div className="flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-500/25 border border-amber-300/40 text-amber-200 font-bold text-xs shadow-xs">
                  <span>🔥 {effectiveStreak}-Day Streak</span>
                </div>
                <div className="flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-900/60 border border-blue-300/40 text-blue-100 font-bold text-xs shadow-xs">
                  <span>⚡ {effectiveXp.toLocaleString()} XP</span>
                </div>
              </div>
            </div>

            {/* Level 3 & 4: Content Injection (PhysicalFolderTabs & Workspace) */}
            <div className="bg-white min-h-[580px]">
              {children}
            </div>

          </div>
        )}

        {/* ───────────────────────────────────────────────────────────── */}
        {/* MODE B: ANDROID MOBILE WEBAPK (Exact Prototype lines 712-1150) */}
        {/* ───────────────────────────────────────────────────────────── */}
        {sandboxMode === 'mobile' && (
          <div 
            id="mobile-viewport" 
            className={`transition-all duration-500 mx-auto w-full ${isLandscape ? 'max-w-3xl' : 'max-w-sm'}`}
          >
            
            {/* Mobile Ergonomics Bar: Orientation & Workspace Real Estate Toggle */}
            <div 
              id="mobile-control-bar" 
              className="flex flex-wrap items-center justify-between gap-3 mb-5 bg-[#081326]/90 backdrop-blur-md px-4 py-3 rounded-2xl border border-slate-700/80 shadow-2xl transition-all duration-300"
            >
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
                <div>
                  <span className="text-xs font-bold text-white block leading-tight">Mobile Ergonomics Mode</span>
                  <span id="current-orientation-label" className="text-[11px] text-slate-300">
                    {isLandscape 
                      ? '🔄 Landscape Mode • Ribbon Auto-Hidden • 6-Col Ledger Active' 
                      : '📱 Portrait Mode • 1-Tap Collapse Enabled'}
                  </span>
                </div>
              </div>
              <div className="flex items-center gap-2 bg-slate-900 p-1 rounded-xl border border-slate-700 shadow-inner">
                <button
                  type="button"
                  id="btn-mob-portrait"
                  onClick={() => handleSetMobileOrientation('portrait')}
                  className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                    !isLandscape 
                      ? 'bg-[#13519C] text-white shadow-xs' 
                      : 'text-slate-400 hover:text-white hover:bg-slate-800'
                  }`}
                >
                  <span>📱</span>
                  <span>Portrait</span>
                </button>
                <button
                  type="button"
                  id="btn-mob-landscape"
                  onClick={() => handleSetMobileOrientation('landscape')}
                  className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                    isLandscape 
                      ? 'bg-[#13519C] text-white shadow-xs' 
                      : 'text-slate-400 hover:text-white hover:bg-slate-800'
                  }`}
                >
                  <span>🔄</span>
                  <span>Landscape / Fullscreen</span>
                </button>
              </div>
            </div>

            {/* Phone Chassis Bezel (Adaptive Android Device) */}
            <div 
              id="mobile-chassis" 
              className={`bg-slate-900 shadow-2xl border-4 border-slate-800 relative transition-all duration-500 ${
                isLandscape 
                  ? 'p-3 rounded-[28px]' 
                  : 'p-3.5 rounded-[44px]'
              }`}
            >
              
              {/* Camera Punch Hole */}
              <div 
                id="mobile-punch-hole" 
                className={`absolute w-4 h-4 bg-black rounded-full z-40 border border-slate-800 pointer-events-none transition-all duration-500 ${
                  isLandscape 
                    ? 'top-1/2 left-3.5 -translate-y-1/2' 
                    : 'top-6 left-1/2 -translate-x-1/2'
                }`}
              ></div>

              {/* Phone Screen Canvas */}
              <div 
                id="mobile-canvas" 
                className={`bg-white overflow-hidden text-slate-800 flex flex-col justify-between relative shadow-inner transition-all duration-500 ${
                  isLandscape 
                    ? 'min-h-[390px] max-h-[460px] rounded-[20px]' 
                    : 'min-h-[640px] rounded-[34px]'
                }`}
              >
                <MobileWebApkView
                  activeTab={activeTab}
                  onSelectTab={onSelectTab}
                  orientation={mobileOrientation}
                  studentName={studentName}
                  grade={currentGrade}
                  schoolName={schoolName}
                  streakDays={streakDays}
                  xp={xp}
                  question={question}
                  activeTopic={activeTopic}
                  isLoadingQuestion={isLoadingQuestion}
                  isMarking={isMarking}
                  onSelectTopic={onSelectTopic}
                  onOpenTopicScope={onOpenTopicScope}
                  onCheckAnswer={onCheckAnswer}
                  onNextQuestion={onNextQuestion}
                  onOpenProfilePhoto={onOpenProfilePhoto}
                  onOpenLinkGuardian={onOpenLinkGuardian}
                />
              </div>

            </div>

            <p className="text-center text-xs text-slate-400 mt-3 select-none">
              📱 Android WebAPK View: 1-Tap Home Screen Launch • &lt; 1.4 MB Data • Works 100% Offline
            </p>

          </div>
        )}

        {/* ───────────────────────────────────────────────────────────── */}
        {/* MODE C: NATIVE RESPONSIVE (100% Faithful Responsive View)      */}
        {/* ───────────────────────────────────────────────────────────── */}
        {sandboxMode === 'native' && (
          <div className="w-full bg-white text-slate-800 min-h-screen rounded-xl shadow-xl overflow-hidden">
            {/* Desktop Layout on >= md */}
            <div className="hidden md:block">
              {children}
            </div>

            {/* Mobile Layout on < md */}
            <div className="block md:hidden min-h-screen">
              <MobileWebApkView
                activeTab={activeTab}
                onSelectTab={onSelectTab}
                orientation="portrait"
                studentName={studentName}
                grade={currentGrade}
                schoolName={schoolName}
                streakDays={streakDays}
                xp={xp}
                question={question}
                activeTopic={activeTopic}
                isLoadingQuestion={isLoadingQuestion}
                isMarking={isMarking}
                onSelectTopic={onSelectTopic}
                onOpenTopicScope={onOpenTopicScope}
                onCheckAnswer={onCheckAnswer}
                onNextQuestion={onNextQuestion}
                onOpenProfilePhoto={onOpenProfilePhoto}
              />
            </div>
          </div>
        )}

      </main>

      <SuperAdminProgressResetModal
        isOpen={showAdminResetModal}
        onClose={() => setShowAdminResetModal(false)}
        activeSubject={activeTab}
      />

    </div>
  );
}
