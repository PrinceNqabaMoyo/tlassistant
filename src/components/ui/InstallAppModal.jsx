import React, { useState, useEffect } from 'react';
import { 
  X, 
  Monitor, 
  Smartphone, 
  Download, 
  QrCode, 
  CheckCircle2, 
  Copy, 
  Check, 
  Sparkles, 
  ArrowRight,
  ShieldCheck,
  Zap,
  WifiOff,
  Share,
  PlusSquare
} from 'lucide-react';
import { QRCodeSVG } from 'qrcode.react';

/**
 * InstallAppModal
 * Unified cross-device install portal for Desktop PWA and Mobile WebAPK.
 * 
 * Invariants:
 * - Desktop Tab: One-click native PWA installation on Windows/macOS with zero address bar.
 * - Mobile Tab (Desktop view): Renders high-resolution vector QR code for 1-scan mobile installation.
 * - Mobile Tab (Mobile view): Direct 1-tap "Add to Home Screen / Install" button.
 * - Automatically detects local IP (e.g. https://192.168.1.84:5173) or production domain.
 */
export default function InstallAppModal({ isOpen, onClose }) {
  const [activeTab, setActiveTab] = useState('mobile'); // 'mobile' | 'desktop'
  const [copied, setCopied] = useState(false);
  const [deferredPrompt, setDeferredPrompt] = useState(null);
  const [isInstalled, setIsInstalled] = useState(false);
  const [isMobileDevice, setIsMobileDevice] = useState(false);
  const [isIos, setIsIos] = useState(false);

  // Capture PWA install prompt
  useEffect(() => {
    const handleBeforeInstall = (e) => {
      e.preventDefault();
      setDeferredPrompt(e);
    };

    const handleAppInstalled = () => {
      setIsInstalled(true);
      setDeferredPrompt(null);
    };

    window.addEventListener('beforeinstallprompt', handleBeforeInstall);
    window.addEventListener('appinstalled', handleAppInstalled);

    if (window.matchMedia('(display-mode: standalone)').matches) {
      setIsInstalled(true);
    }

    if (typeof window !== 'undefined') {
      const ua = navigator.userAgent || '';
      const isIosDevice = /iPhone|iPad|iPod/i.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
      setIsIos(isIosDevice);
      setIsMobileDevice(isIosDevice || /Android/i.test(ua) || window.innerWidth < 768);
    }

    return () => {
      window.removeEventListener('beforeinstallprompt', handleBeforeInstall);
      window.removeEventListener('appinstalled', handleAppInstalled);
    };
  }, []);

  // Compute mobile install URL (defaults to current origin, ensuring HTTPS network URL is used)
  const installUrl = typeof window !== 'undefined' ? window.location.origin : 'https://app.fundile.co.za';

  const handleCopyLink = () => {
    if (typeof navigator !== 'undefined' && navigator.clipboard) {
      navigator.clipboard.writeText(installUrl);
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    }
  };

  const handleTriggerInstall = async () => {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      if (outcome === 'accepted') {
        setIsInstalled(true);
      }
      setDeferredPrompt(null);
    } else {
      // Browser fallback instructions
      alert('To install, click the Install (⊕) icon in your browser address bar, or open your browser menu (⋮) and select "Install Fundile".');
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/70 backdrop-blur-md animate-in fade-in duration-200">
      <div 
        className="relative w-full max-w-lg bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden text-slate-800"
        onClick={(e) => e.stopPropagation()}
      >
        
        {/* Header Bar */}
        <div className="bg-[#081326] text-white p-5 sm:p-6 relative">
          <button 
            type="button"
            onClick={onClose}
            className="absolute top-4 right-4 p-2 rounded-full text-slate-400 hover:text-white hover:bg-white/10 transition cursor-pointer"
            aria-label="Close modal"
          >
            <X className="w-5 h-5" />
          </button>

          <div className="flex items-center gap-2 mb-1.5">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span className="text-[11px] font-extrabold uppercase tracking-wider text-emerald-300">
              Direct Device Installation
            </span>
          </div>
          <h3 className="text-xl sm:text-2xl font-bold tracking-tight text-white flex items-center gap-2">
            <span>Get the Fundile App</span>
          </h3>
          <p className="text-xs sm:text-sm text-slate-300 mt-1">
            Install Fundile on your device for distraction-free full-screen learning with zero buffering.
          </p>

          {/* Mode Switcher Tabs */}
          <div className="flex items-center gap-2 mt-4 bg-slate-900/80 p-1 rounded-xl border border-slate-700/80">
            <button
              type="button"
              onClick={() => setActiveTab('mobile')}
              className={`flex-1 flex items-center justify-center gap-2 py-2 rounded-lg text-xs font-bold transition cursor-pointer ${
                activeTab === 'mobile'
                  ? 'bg-[#13519C] text-white shadow-sm'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <Smartphone className="w-4 h-4" />
              <span>Mobile Phone (Android / iOS)</span>
            </button>
            <button
              type="button"
              onClick={() => setActiveTab('desktop')}
              className={`flex-1 flex items-center justify-center gap-2 py-2 rounded-lg text-xs font-bold transition cursor-pointer ${
                activeTab === 'desktop'
                  ? 'bg-[#13519C] text-white shadow-sm'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <Monitor className="w-4 h-4" />
              <span>Computer (Windows / Mac)</span>
            </button>
          </div>
        </div>

        {/* Modal Body */}
        <div className="p-5 sm:p-6">
          
          {/* ───────────────────────────────────────────────────────────── */}
          {/* TAB 1: MOBILE APP (SCAN QR CODE ON PC / DIRECT INSTALL ON PHONE) */}
          {/* ───────────────────────────────────────────────────────────── */}
          {activeTab === 'mobile' && (
            <div className="flex flex-col items-center text-center">
              
              {!isMobileDevice ? (
                // Computer View: Scan QR Code with Phone
                <>
                  <div className="bg-slate-50 p-4 rounded-2xl border-2 border-dashed border-slate-300 shadow-inner flex flex-col items-center">
                    <QRCodeSVG 
                      value={installUrl} 
                      size={180}
                      bgColor="#F8FAFC"
                      fgColor="#081326"
                      level="Q"
                      includeMargin={false}
                      imageSettings={{
                        src: '/pwa-192x192.png',
                        x: undefined,
                        y: undefined,
                        height: 38,
                        width: 38,
                        excavate: true,
                      }}
                    />
                    <div className="mt-2.5 flex items-center gap-1.5 text-[11px] font-bold text-slate-500">
                      <QrCode className="w-3.5 h-3.5 text-[#13519C]" />
                      <span>Point your phone camera to scan</span>
                    </div>
                  </div>

                  <div className="mt-4 text-left w-full space-y-2">
                    <div className="flex items-start gap-2.5 text-xs text-slate-600">
                      <span className="w-5 h-5 rounded-full bg-blue-100 text-[#13519C] font-bold flex items-center justify-center shrink-0 text-[11px]">1</span>
                      <span>Scan the QR code with your smartphone camera.</span>
                    </div>
                    <div className="flex items-start gap-2.5 text-xs text-slate-600">
                      <span className="w-5 h-5 rounded-full bg-blue-100 text-[#13519C] font-bold flex items-center justify-center shrink-0 text-[11px]">2</span>
                      <span>Tap the link that appears on your phone screen.</span>
                    </div>
                    <div className="flex items-start gap-2.5 text-xs text-slate-600">
                      <span className="w-5 h-5 rounded-full bg-blue-100 text-[#13519C] font-bold flex items-center justify-center shrink-0 text-[11px]">3</span>
                      <span>Tap <strong>"Install app"</strong> in Chrome (or <strong>"Add to Home Screen"</strong> in Safari).</span>
                    </div>
                  </div>

                  <div className="mt-4 pt-3 border-t border-slate-200 w-full flex items-center justify-between gap-2">
                    <span className="text-[11px] text-slate-500 truncate text-left max-w-[240px]">
                      {installUrl}
                    </span>
                    <button
                      type="button"
                      onClick={handleCopyLink}
                      className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-slate-300 hover:border-slate-400 bg-white text-xs font-semibold text-slate-700 transition cursor-pointer"
                    >
                      {copied ? <Check className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5" />}
                      <span>{copied ? 'Copied Link!' : 'Copy Link'}</span>
                    </button>
                  </div>
                </>
              ) : (
                // Direct Mobile View: Tap to Install
                <div className="space-y-4 w-full text-center py-2">
                  <img 
                    src="/pwa-192x192.png" 
                    alt="Fundile Icon" 
                    className="w-16 h-16 rounded-2xl shadow-lg mx-auto object-cover" 
                  />
                  <div>
                    <h4 className="font-bold text-slate-900 text-base">Install Fundile on your Phone</h4>
                    <p className="text-xs text-slate-500 mt-1">
                      Runs 100% full screen with bottom thumb navigation and offline cache.
                    </p>
                  </div>

                  {isIos ? (
                    <div className="space-y-3">
                      <div className="p-3.5 bg-blue-50/90 border border-blue-200/80 rounded-2xl text-left text-xs text-slate-700 space-y-2.5">
                        <div className="flex items-center gap-1.5 font-bold text-[#13519C]">
                          <Smartphone className="w-4 h-4 text-[#13519C]" />
                          <span>iOS / Safari 1-Tap Setup:</span>
                        </div>
                        <div className="flex items-center gap-2.5">
                          <span className="w-5 h-5 rounded-full bg-[#13519C] text-white font-bold flex items-center justify-center shrink-0 text-[11px]">1</span>
                          <span>Tap the <strong>Share</strong> button (<Share className="w-3.5 h-3.5 inline mx-0.5 text-[#13519C]" />) in Safari's toolbar.</span>
                        </div>
                        <div className="flex items-center gap-2.5">
                          <span className="w-5 h-5 rounded-full bg-[#13519C] text-white font-bold flex items-center justify-center shrink-0 text-[11px]">2</span>
                          <span>Scroll down and select <strong>"Add to Home Screen"</strong> (<PlusSquare className="w-3.5 h-3.5 inline mx-0.5 text-[#13519C]" />).</span>
                        </div>
                      </div>
                      <p className="text-[11px] text-slate-500">
                        Launches like an authentic native iOS app with full-screen gestures.
                      </p>
                    </div>
                  ) : (
                    <div className="space-y-2">
                      <button
                        type="button"
                        onClick={handleTriggerInstall}
                        className="w-full py-3.5 px-6 rounded-xl bg-[#FF9100] hover:bg-[#f58200] text-white font-bold text-sm shadow-md shadow-orange-500/30 transition flex items-center justify-center gap-2 cursor-pointer"
                      >
                        <Download className="w-4 h-4" />
                        <span>{isInstalled ? 'App Already Installed' : 'Install Mobile WebAPK Now'}</span>
                      </button>
                      <p className="text-[11px] text-slate-500">
                        {deferredPrompt 
                          ? '1-tap install: Fundile will install directly to your home screen & app drawer.' 
                          : 'Tip: If prompt does not appear, tap Chrome menu (⋮) → "Install app".'}
                      </p>
                    </div>
                  )}
                </div>
              )}

              {/* Data & Privacy Badges */}
              <div className="grid grid-cols-3 gap-2 mt-4 pt-3 border-t border-slate-100 w-full text-[10px] text-slate-600 font-medium">
                <div className="flex flex-col items-center gap-1 p-2 rounded-xl bg-slate-50">
                  <Zap className="w-4 h-4 text-amber-500" />
                  <span>&lt; 1.4 MB Data</span>
                </div>
                <div className="flex flex-col items-center gap-1 p-2 rounded-xl bg-slate-50">
                  <WifiOff className="w-4 h-4 text-emerald-600" />
                  <span>Works Offline</span>
                </div>
                <div className="flex flex-col items-center gap-1 p-2 rounded-xl bg-slate-50">
                  <ShieldCheck className="w-4 h-4 text-blue-600" />
                  <span>No Store Login</span>
                </div>
              </div>

            </div>
          )}

          {/* ───────────────────────────────────────────────────────────── */}
          {/* TAB 2: DESKTOP / LAPTOP APP                                  */}
          {/* ───────────────────────────────────────────────────────────── */}
          {activeTab === 'desktop' && (
            <div className="space-y-4">
              <div className="flex items-start gap-3 p-3.5 rounded-2xl bg-blue-50/80 border border-blue-200">
                <div className="p-2.5 rounded-xl bg-[#13519C] text-white shrink-0">
                  <Monitor className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-blue-950">Standalone Desktop Application</h4>
                  <p className="text-xs text-blue-800/80 mt-0.5 leading-relaxed">
                    Installs directly to your Windows 11 Taskbar or macOS Dock with <strong>zero address bar and no browser tabs</strong>.
                  </p>
                </div>
              </div>

              <div className="space-y-2 text-xs text-slate-600">
                <div className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                  <span>Skeuo-modern 3D Physical Folder Tabs at top of screen</span>
                </div>
                <div className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                  <span>Widescreen 2D ledger tables &amp; KaTeX working pads</span>
                </div>
                <div className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                  <span>Zero installation friction — no admin permissions required</span>
                </div>
              </div>

              <button
                type="button"
                onClick={handleTriggerInstall}
                className="w-full py-3.5 px-6 rounded-xl bg-[#13519C] hover:bg-blue-800 text-white font-bold text-sm shadow-md shadow-blue-900/20 transition flex items-center justify-center gap-2 cursor-pointer"
              >
                <Download className="w-4 h-4" />
                <span>{isInstalled ? 'Desktop App Installed' : 'Install Desktop App'}</span>
              </button>

              <p className="text-[11px] text-slate-400 text-center">
                Supported on Chrome, Edge, and Brave on Windows 10/11, macOS, and Linux.
              </p>
            </div>
          )}

        </div>

      </div>
    </div>
  );
}
