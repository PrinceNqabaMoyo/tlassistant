import React, { useState, useEffect, useRef } from 'react';
import FundileLogo from './FundileLogo';
import {
    ArrowRight,
    Sparkles,
    MessageCircleWarning,
    ChevronDown,
    CheckCircle2,
    GraduationCap,
    Users,
    BookOpen,
    Building2,
    Mail,
    Activity,
    Wrench,
    CheckSquare,
    Radar,
    ShieldCheck,
    Landmark,
    Home,
    Star,
    Check,
    Cpu,
    WifiOff,
    FileCheck2,
} from 'lucide-react';
import DemandCaptureForm from './DemandCaptureForm';
import ScrollReveal from './landing/ScrollReveal';
import PerspectiveShowcase from './landing/PerspectiveShowcase';
import InstallAppModal from './InstallAppModal';

import { LIVE_AVAILABILITY_DETAIL, LIVE_AVAILABILITY_HEADLINE, LIVE_AVAILABILITY_NOTE } from '../../app/constants/availability';
import { HERO_COPY, HIDDEN_CURRICULUM, PRICING_COPY, HOW_IT_WORKS, INTERNAL_CONSISTENCY, TEACHERS_LINK } from '../../app/constants/landingCopy';

const AUDIENCE_KEYS = ['learners', 'parents', 'teachers', 'schools'];

const LandingPage = ({ onGetStarted, onSignIn, onViewSubscription, onNavigatePrivacy }) => {
    // ── Install modal state ──
    const [showInstallModal, setShowInstallModal] = useState(false);

    // ── Perspective navigation state ──
    const [activePerspective, setActivePerspective] = useState('learners');
    const [mobileTickerPerspective, setMobileTickerPerspective] = useState('learners');

    // ── Super Admin Landing CTA Posture Sync ──
    const [landingCtaMode, setLandingCtaMode] = useState(() => {
        return typeof window !== 'undefined'
            ? (localStorage.getItem('fundile_landing_cta_mode') || 'free_trial')
            : 'free_trial';
    });

    useEffect(() => {
        const handleStorageChange = () => {
            const currentMode = localStorage.getItem('fundile_landing_cta_mode') || 'free_trial';
            setLandingCtaMode(currentMode);
        };
        window.addEventListener('storage', handleStorageChange);
        return () => window.removeEventListener('storage', handleStorageChange);
    }, []);

    const isDirectAuthMode = landingCtaMode === 'direct_auth';
    const primaryCtaLabel = isDirectAuthMode ? 'Create Account' : HERO_COPY.primaryCta;
    const trialNoteLabel = isDirectAuthMode
        ? '100% Aligned with South African Curriculum Standards • Grades 7–12'
        : HERO_COPY.trialNote;

    // Auto-cycling highlight ticker on mobile viewports every 3.5s
    // INVARIANT: Visual highlight auto-advances, but simulator view below ONLY swaps when a tab is clicked!
    useEffect(() => {
        const ticker = setInterval(() => {
            setMobileTickerPerspective((current) => {
                const idx = AUDIENCE_KEYS.indexOf(current);
                const nextIdx = (idx + 1) % AUDIENCE_KEYS.length;
                return AUDIENCE_KEYS[nextIdx];
            });
        }, 3500);
        return () => clearInterval(ticker);
    }, []);

    const audienceRibbonContainerRef = useRef(null);

    // Auto-scroll active audience button into center view when mobile ticker cycles
    useEffect(() => {
        if (!mobileTickerPerspective) return;
        const activeTabEl = document.getElementById(`audience-tab-${mobileTickerPerspective}`);
        if (activeTabEl) {
            activeTabEl.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
        }
    }, [mobileTickerPerspective]);

    // ── Slot-machine upward infinite reel state ──
    const SLOT_ITEMS_BASE = [
        'Mathematics',
        'Physical Sciences',
        'Life Sciences',
        'Natural Sciences',
        'Mathematical Literacy',
        'Technical Mathematics',
        'Accounting',
        'Business Studies',
        'EMS',
        'every subject.',
    ];
    // Append duplicate Mathematics at the end so it rolls UP seamlessly to Mathematics, quietly resets index to 0 without downward snapping, and continues upward in a continuous loop.
    const SLOT_ITEMS = [...SLOT_ITEMS_BASE, SLOT_ITEMS_BASE[0]];
    const [slotIdx, setSlotIdx] = useState(0);
    const [isReelResetting, setIsReelResetting] = useState(false);
    const [showDetails, setShowDetails] = useState(false);
    const [showArrow, setShowArrow] = useState(false);

    // Initial fade in for value bullets and CTAs
    useEffect(() => {
        const detailsTimer = setTimeout(() => setShowDetails(true), 600);
        const arrowTimer = setTimeout(() => setShowArrow(true), 1200);
        return () => {
            clearTimeout(detailsTimer);
            clearTimeout(arrowTimer);
        };
    }, []);

    // Upward infinite slot roll timer: 10,000ms pause on 'every subject.' (index === SLOT_ITEMS_BASE.length - 1), 1,400ms for all other subjects
    useEffect(() => {
        const isEverySubject = slotIdx === SLOT_ITEMS_BASE.length - 1;
        const delay = isEverySubject ? 10000 : 1400;
        const reelTimer = setTimeout(() => {
            setSlotIdx((currentIdx) => {
                if (currentIdx >= SLOT_ITEMS.length - 1) {
                    return 1;
                }
                return currentIdx + 1;
            });
        }, delay);
        return () => clearTimeout(reelTimer);
    }, [slotIdx, SLOT_ITEMS.length, SLOT_ITEMS_BASE.length]);

    // When reel reaches duplicate Mathematics at the end:
    // Wait for the upward transition to finish (350ms), then quietly reset index to 0 with transition: none
    useEffect(() => {
        if (slotIdx === SLOT_ITEMS.length - 1) {
            const resetTimer = setTimeout(() => {
                setIsReelResetting(true);
                setSlotIdx(0);
            }, 380);
            return () => clearTimeout(resetTimer);
        } else if (isReelResetting) {
            const raf = requestAnimationFrame(() => {
                setIsReelResetting(false);
            });
            return () => cancelAnimationFrame(raf);
        }
    }, [slotIdx, isReelResetting, SLOT_ITEMS.length]);

    const heroRef = useRef(null);
    const ctaRowRef = useRef(null);
    const [isRibbonVisible, setIsRibbonVisible] = useState(true);
    const [showFloatingInstall, setShowFloatingInstall] = useState(false);
    const lastScrollYRef = useRef(0);

    useEffect(() => {
        const handleScroll = () => {
            const currentScrollY = window.scrollY || window.pageYOffset || 0;
            const diff = currentScrollY - lastScrollYRef.current;

            // Show floating install button once user scrolls past the first section view (~380px)
            setShowFloatingInstall(currentScrollY > 380);

            if (currentScrollY < 60) {
                // Near top of page: smoothly slide back into view
                setIsRibbonVisible(true);
            } else if (diff > 8 && currentScrollY > 100) {
                // Scrolling down: dynamically hide ribbon to maximize browsing area
                setIsRibbonVisible(false);
            } else if (diff < -8) {
                // Scrolling up: smoothly slide back into view
                setIsRibbonVisible(true);
            }

            lastScrollYRef.current = currentScrollY;
        };

        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll();
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    const PERSPECTIVE_LABELS = {
        learners: 'Learner Experience • Step-by-Step Scaffolding',
        parents: 'Parent Overview • Transparent Weekly Progress',
        teachers: 'Teacher Workflow • Instant Exam Authoring',
        schools: 'School Administration • SASAMS & ATP Pacing',
    };

    const scrollToSimulator = () => {
        const el = document.getElementById('how-it-works') || document.getElementById('ai-engine') || document.getElementById('features');
        if (el) {
            const yOffset = -110;
            const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({ top: y, behavior: 'smooth' });
        }
    };

    const handlePerspectiveChange = (perspective) => {
        setActivePerspective(perspective);
        // Automatically scroll the clicked tab button into center view
        const tabEl = document.getElementById(`audience-tab-${perspective}`);
        if (tabEl) {
            tabEl.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
        }
        const el = document.getElementById('how-it-works');
        if (el) {
            const yOffset = -110;
            const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({ top: y, behavior: 'smooth' });
        }
    };

    const scrollToSection = (id) => {
        const section = document.getElementById(id);
        if (section) {
            const yOffset = -110;
            const y = section.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({ top: y, behavior: 'smooth' });
        }
    };

    return (
        <div className="relative min-h-screen bg-slate-50 text-slate-900 font-sans selection:bg-[#13519C]/20 selection:text-[#13519C]">
            
            {/* FIXED BLUE RIBBON */}
            <div className={`fixed top-0 left-0 right-0 z-50 bg-[#13519C] border-b border-[#13519C]/20 transition-transform duration-300 ease-in-out ${
                isRibbonVisible ? 'translate-y-0' : '-translate-y-full'
            }`}>
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between items-center h-16">
                        <div className="flex items-center shrink-0 pointer-events-none">
                            <FundileLogo className="h-28 w-28 sm:h-48 sm:w-48 text-white" />
                        </div>
                        <div className="flex items-center gap-2.5 sm:gap-3">
                            <button
                                type="button"
                                onClick={() => setShowInstallModal(true)}
                                className="hidden sm:inline-flex items-center gap-1.5 rounded-lg border border-emerald-300/40 bg-emerald-500/20 px-2.5 py-1.5 text-xs sm:text-sm font-bold text-emerald-200 transition-all duration-300 hover:bg-emerald-500/30 cursor-pointer shadow-xs"
                                title="Install Fundile App on Mobile Phone or Computer"
                            >
                                <span>📲</span>
                                <span className="hidden sm:inline">Install App</span>
                            </button>
                            <button
                                type="button"
                                data-testid="btn-landing-signin"
                                onClick={onSignIn}
                                className="hidden sm:inline-flex rounded-lg border border-white/20 bg-white/10 px-3 py-1.5 text-sm sm:px-5 sm:py-2 sm:text-base font-medium text-white transition-all duration-300 hover:bg-white/20 cursor-pointer"
                            >
                                Sign in
                            </button>
                            <button 
                                type="button"
                                data-testid="btn-landing-signup"
                                onClick={onGetStarted}
                                className="bg-[#FF9100] hover:bg-[#f58200] text-white px-3 py-1 sm:px-4 sm:py-1.5 rounded-xl shadow-[0_4px_14px_rgba(255,145,0,0.39)] transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer text-center leading-tight flex flex-col items-center justify-center shrink-0 border border-orange-400/30"
                                title={isDirectAuthMode ? "Create Account" : "Start 2-week Free Trial"}
                            >
                                {isDirectAuthMode ? (
                                    <span className="text-xs sm:text-sm font-extrabold tracking-tight">
                                        Create Account
                                    </span>
                                ) : (
                                    <>
                                        <span className="text-[11px] sm:text-xs font-semibold text-amber-100 tracking-tight leading-tight">
                                            Start 2-week
                                        </span>
                                        <span className="text-xs sm:text-sm font-extrabold tracking-tight leading-tight">
                                            free trial
                                        </span>
                                    </>
                                )}
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            {/* FIXED AUDIENCE SUB-RIBBON (Crisp white fill, dark blue pills, zero scrollbars) */}
            <div className={`fixed top-16 left-0 right-0 z-50 transition-all duration-300 ease-in-out border-b bg-white/95 border-slate-200/90 shadow-xs backdrop-blur-md ${
                isRibbonVisible ? 'translate-y-0' : '-translate-y-16'
            }`}>
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 sm:py-2.5">
                    <div className="flex items-center justify-between gap-3">
                        <div 
                            ref={audienceRibbonContainerRef}
                            className="flex items-center gap-2 sm:gap-2.5 overflow-x-auto no-scrollbar scrollbar-hide px-1 py-0.5 max-w-full [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden [&::-webkit-scrollbar]:w-0 [&::-webkit-scrollbar]:h-0 relative z-10"
                            style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
                        >

                            {[
                                { id: 'learners', label: 'Learners', icon: GraduationCap, iconColor: 'text-[#13519C]' },
                                { id: 'parents', label: 'Parents', icon: Users, iconColor: 'text-amber-600' },
                                { id: 'teachers', label: 'Teachers', icon: BookOpen, iconColor: 'text-indigo-600' },
                                { id: 'schools', label: 'School Admins', shortLabel: 'Schools', icon: Building2, iconColor: 'text-cyan-600' },
                            ].map((tab) => {
                                const Icon = tab.icon;
                                const isDesktopActive = activePerspective === tab.id;
                                const isMobileHighlighted = mobileTickerPerspective === tab.id;

                                return (
                                    <button
                                        key={tab.id}
                                        id={`audience-tab-${tab.id}`}
                                        type="button"
                                        onClick={() => handlePerspectiveChange(tab.id)}
                                        className={`relative z-10 inline-flex items-center gap-2 px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-full text-xs sm:text-sm font-bold transition-all duration-300 cursor-pointer shrink-0 bg-white text-[#13519C] ${
                                            isMobileHighlighted
                                                ? 'ring-2 ring-[#FF9100] shadow-md shadow-amber-500/20 scale-[1.02] sm:ring-0 sm:shadow-none sm:scale-100'
                                                : 'border border-slate-200/90'
                                        } ${
                                            isDesktopActive
                                                ? 'sm:ring-2 sm:ring-[#FF9100] sm:shadow-md sm:shadow-amber-500/20 sm:scale-[1.02] sm:border-transparent'
                                                : 'sm:border sm:border-slate-200/90 sm:hover:bg-slate-50 hover:shadow-xs'
                                        }`}
                                    >
                                        <Icon className={`h-4 w-4 ${tab.iconColor} shrink-0`} />
                                        <span className="sm:hidden">{tab.shortLabel || tab.label}</span>
                                        <span className="hidden sm:inline">{tab.label}</span>
                                        {/* Mobile orange dot indicator */}
                                        {isMobileHighlighted && (
                                            <span className="w-1.5 h-1.5 rounded-full bg-[#FF9100] shrink-0 sm:hidden" />
                                        )}
                                        {/* Desktop orange dot indicator */}
                                        {isDesktopActive && (
                                            <span className="w-1.5 h-1.5 rounded-full bg-[#FF9100] shrink-0 hidden sm:inline-block" />
                                        )}
                                    </button>
                                );
                            })}
                        </div>

                        {/* Right Helper Info */}
                        <div className="shrink-0 hidden lg:flex items-center gap-2">
                            <span className="text-[11px] font-semibold text-slate-500 bg-slate-100 px-3 py-1 rounded-full border border-slate-200 flex items-center gap-1.5">
                                <span className="w-2 h-2 rounded-full bg-[#FF9100]" />
                                <span>{PERSPECTIVE_LABELS[activePerspective] || 'Learner Experience'}</span>
                            </span>
                        </div>
                    </div>
                </div>
            </div>

            {/* 1. HERO STAGE (Above the Fold) — Signature Deep Royal Navy / Cobalt Atmosphere */}
            <div className="relative min-h-[92vh] sm:min-h-screen bg-[#081326] bg-[radial-gradient(ellipse_at_top,_rgba(19,81,156,0.45)_0%,_rgba(8,19,38,0.98)_55%,_#050c18_100%)] text-white pt-24 sm:pt-32 pb-12 sm:pb-28 px-4 sm:px-6 lg:px-8 overflow-hidden">
                {/* Ambient Atmospheric Glows */}
                <div className="absolute -left-24 top-40 z-0 h-72 w-72 rounded-full blur-3xl bg-[#13519C]/30 pointer-events-none" />
                <div className="absolute right-0 top-24 z-0 h-96 w-96 rounded-full blur-3xl bg-[#FF9100]/15 pointer-events-none" />
                {/* Horizon gradient softening into curtain */}
                <div className="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[#081326] via-[#081326]/80 to-transparent pointer-events-none z-0" />

                <div className="relative z-10 max-w-7xl mx-auto">
                    <ScrollReveal delay={0.1}>
                        <section ref={heroRef} id="learner-screen-top" className="flex flex-col items-center justify-between text-center pb-4 pt-2 min-h-[calc(100vh-10rem)] max-w-4xl mx-auto relative z-10 box-border scroll-mt-32 sm:scroll-mt-36">
                            {/* Top & Middle Group */}
                            <div className="flex flex-col items-center justify-center flex-1 w-full gap-4">
                                <div className="inline-flex items-center gap-2 rounded-full px-3.5 sm:px-4 py-1.5 sm:py-2 text-xs sm:text-sm font-medium border border-[#2B7BD8]/40 bg-[#13519C]/20 text-blue-100 shadow-xs whitespace-nowrap">
                                    <Sparkles className="h-4 w-4 text-[#FFD166] hidden sm:inline-block shrink-0" />
                                    <span>{HERO_COPY.eyebrow}</span>
                                </div>

                                {/* ── Slot-machine headline ── */}
                                <h1
                                    className="font-bold tracking-tight text-white"
                                    style={{ fontFamily: 'Afacad, sans-serif' }}
                                >
                                    {/* Line 1 — static lead-in */}
                                    <span className="block text-4xl sm:text-5xl xl:text-6xl">
                                        Excel in
                                    </span>

                                    {/* Line 2 — slot machine: fixed height = exactly 1 line */}
                                    <span
                                        className="block overflow-hidden text-4xl sm:text-5xl xl:text-6xl"
                                        style={{ height: '1.1em' }}
                                        aria-live="polite"
                                        aria-label={SLOT_ITEMS[slotIdx]}
                                    >
                                        <span
                                            className="block"
                                            style={{
                                                 transform: `translateY(calc(${-slotIdx} * 1.1em))`,
                                                 transition: isReelResetting ? 'none' : 'transform 0.35s cubic-bezier(0.4,0,0.2,1)',
                                                 lineHeight: '1.1',
                                                 willChange: 'transform',
                                            }}
                                        >
                                            {SLOT_ITEMS.map((item, i) => {
                                                const isEverySubject = item === 'every subject.';
                                                return (
                                                    <span
                                                        key={i}
                                                        className={`block ${isEverySubject ? 'text-white' : 'text-[#FF9100]'}`}
                                                        style={{ height: '1.1em', lineHeight: '1.1' }}
                                                    >
                                                        {item}
                                                    </span>
                                                );
                                            })}
                                        </span>
                                    </span>

                                    {/* Line 3 — static tagline, always visible */}
                                    <span className="block text-2xl sm:text-3xl xl:text-4xl font-semibold mt-1 text-white/70">
                                        {HERO_COPY.tagline || 'Use Fundile, become a top student.'}
                                    </span>
                                </h1>

                                {/* Bullet points */}
                                <div 
                                    className={`transition-all duration-1000 ease-out transform ${
                                        showDetails ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4 pointer-events-none'
                                    }`}
                                >
                                    <ul className="mt-4 space-y-2 inline-block text-left">
                                        {(HERO_COPY.bullets || []).map((bullet, i) => (
                                            <li key={i} className="flex items-start gap-2.5 text-sm sm:text-base leading-6 text-slate-200">
                                                <CheckCircle2 className="h-4.5 w-4.5 mt-0.5 shrink-0 text-[#FF9100]" />
                                                <span>{bullet}</span>
                                            </li>
                                        ))}
                                    </ul>
                                </div>

                                {/* CTA row */}
                                <div 
                                    ref={ctaRowRef}
                                    className={`mt-2.5 sm:mt-4 w-full flex flex-col items-center transition-all duration-1000 ease-out transform ${
                                        showDetails ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4 pointer-events-none'
                                    }`}
                                >
                                    <div className="flex flex-row items-center justify-center gap-2.5 w-full max-w-md px-1 sm:px-0">
                                        <button
                                            type="button"
                                            data-testid="btn-landing-signup"
                                            onClick={onGetStarted}
                                            className="flex-1 inline-flex items-center justify-center gap-1.5 sm:gap-2 rounded-xl bg-[#FF9100] px-3 py-2.5 sm:px-8 sm:py-3.5 text-xs sm:text-base font-semibold text-white shadow-[0_16px_50px_rgba(255,145,0,0.3)] transition hover:bg-[#f58200] cursor-pointer whitespace-nowrap"
                                        >
                                            <span>{primaryCtaLabel}</span>
                                            <ArrowRight className="h-4 w-4 sm:h-4.5 sm:w-4.5" />
                                        </button>
                                        <button
                                            type="button"
                                            onClick={() => setShowInstallModal(true)}
                                            className="inline-flex items-center justify-center gap-1.5 sm:gap-2 rounded-xl border border-white/20 bg-white/10 backdrop-blur-md px-3 py-2.5 sm:px-6 sm:py-3.5 text-xs sm:text-base font-semibold text-white transition hover:bg-white/20 cursor-pointer shadow-lg hover:border-white/30 whitespace-nowrap shrink-0"
                                        >
                                            <span>📲</span>
                                            <span>Install App</span>
                                        </button>
                                    </div>
                                    <p className="mt-2 sm:mt-3 text-xs font-medium text-white/60">
                                        {trialNoteLabel}
                                    </p>
                                </div>
                            </div>

                            {/* Bouncing scroll arrow */}
                            <div 
                                className={`shrink-0 transition-all duration-1000 ease-out transform ${
                                    showArrow ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4 pointer-events-none'
                                }`}
                            >
                                <button
                                    onClick={scrollToSimulator}
                                    className="flex flex-col items-center gap-1.5 text-[10px] sm:text-xs font-semibold uppercase tracking-[0.2em] transition-all hover:translate-y-1 text-white/50 hover:text-white/80 cursor-pointer"
                                >
                                    <span>See how it works</span>
                                    <ChevronDown className="h-4 sm:h-5 w-4 sm:w-5 animate-bounce text-[#FF9100]" />
                                </button>
                            </div>
                        </section>
                    </ScrollReveal>
                </div>
            </div>

            {/* 2. LOWER CONTENT SECTIONS CANVAS — Crisp Radiant White / Soft-Slate Canvas with Antigravity Curtain Transition */}
            <div className="relative z-20 -mt-10 sm:-mt-14 bg-slate-50 text-slate-900 rounded-t-[36px] sm:rounded-t-[48px] lg:rounded-t-[56px] border-t border-slate-200/90 shadow-[0_-25px_60px_-15px_rgba(0,0,0,0.5)] px-4 sm:px-6 lg:px-8 pt-10 sm:pt-12 pb-24 transition-all duration-700">
                <div className="mx-auto max-w-7xl">
                    
                    {/* 0. DUAL-ENGINE ARCHITECTURE & TARGETED PRACTICE (BRIDGE SECTION) */}
                    <ScrollReveal delay={0.1}>
                        <section id="ai-engine" className="pt-2 sm:pt-4 pb-16 sm:pb-20 border-b border-slate-200/80 scroll-mt-32">
                            <div className="text-center max-w-4xl mx-auto">
                                
                                {/* Eyebrow Pill */}
                                <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white border border-slate-200/90 shadow-xs mb-6">
                                    <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                                    <span className="text-xs font-bold text-slate-700 uppercase tracking-wide">
                                        Dual-Engine Architecture • Grounded Socratic Intelligence
                                    </span>
                                </div>

                                {/* Main Display Headline (Afacad / Plus Jakarta Sans) */}
                                <h2 
                                    className="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-slate-900 tracking-tight leading-[1.12] mb-6"
                                    style={{ fontFamily: 'Afacad, sans-serif' }}
                                >
                                    Targeted Practice. Zero Rote Guesswork.<br className="hidden sm:inline" />
                                    <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#13519C] via-blue-700 to-[#FF9100]">
                                        {' '}100% Exam Certainty.
                                    </span>
                                </h2>

                                {/* Lead Narrative Paragraph */}
                                <p className="text-base sm:text-lg lg:text-xl text-slate-600 font-normal leading-relaxed max-w-3xl mx-auto mb-10">
                                    Fundile uses sophisticated computing to guide learners towards personal mastery of concepts. Built specifically for the South African education system in all its variations, learners from public and independent schools will be better off for getting on this platform.
                                </p>

                                {/* Focused CTA Button */}
                                <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-12">
                                    <button
                                        type="button"
                                        onClick={onGetStarted}
                                        className="w-full sm:w-auto inline-flex items-center justify-center px-8 py-3.5 text-base font-bold text-white bg-[#FF9100] hover:bg-[#e68200] rounded-xl shadow-lg shadow-orange-500/25 transition-all duration-200 transform hover:-translate-y-0.5 cursor-pointer"
                                    >
                                        <span>{primaryCtaLabel}</span>
                                        <ArrowRight className="w-5 h-5 ml-2" />
                                    </button>
                                </div>

                                {/* 4 Quick Badges Strip */}
                                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-left max-w-4xl mx-auto">
                                    {/* Badge 1: Socratic Guidance */}
                                    <div className="bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs flex items-start gap-3 hover:shadow-md transition duration-200">
                                        <div className="w-8 h-8 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center shrink-0 border border-blue-100">
                                            <Sparkles className="w-4 h-4 text-[#FF9100]" />
                                        </div>
                                        <div>
                                            <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Socratic Guidance</h4>
                                            <p className="text-[12px] text-slate-500 leading-snug mt-0.5">Never gives the answer away. Nudges the learner to discover the solution step-by-step.</p>
                                        </div>
                                    </div>

                                    {/* Badge 2: Verified Calculation Accuracy */}
                                    <div className="bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs flex items-start gap-3 hover:shadow-md transition duration-200">
                                        <div className="w-8 h-8 rounded-xl bg-orange-50 text-[#FF9100] flex items-center justify-center shrink-0 border border-orange-100">
                                            <Cpu className="w-4 h-4 text-[#13519C]" />
                                        </div>
                                        <div>
                                            <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Verified Accuracy</h4>
                                            <p className="text-[12px] text-slate-500 leading-snug mt-0.5">Mathematical calculations and accounting ledgers verified with zero guessing.</p>
                                        </div>
                                    </div>

                                    {/* Badge 3: Lean Data Usage */}
                                    <div className="bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs flex items-start gap-3 hover:shadow-md transition duration-200">
                                        <div className="w-8 h-8 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0 border border-emerald-100">
                                            <WifiOff className="w-4 h-4" />
                                        </div>
                                        <div>
                                            <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Ultra-Lean Data</h4>
                                            <p className="text-[12px] text-slate-500 leading-snug mt-0.5">Our lean architecture ensures extremely small use of data (&lt; 2 MB). No video buffering.</p>
                                        </div>
                                    </div>

                                    {/* Badge 4: Automated Tests & Memos */}
                                    <div className="bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs flex items-start gap-3 hover:shadow-md transition duration-200">
                                        <div className="w-8 h-8 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center shrink-0 border border-purple-100">
                                            <FileCheck2 className="w-4 h-4" />
                                        </div>
                                        <div>
                                            <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Automated Tests &amp; Memos</h4>
                                            <p className="text-[12px] text-slate-500 leading-snug mt-0.5">Fundile automates the setting of tests and exams with memos for teachers and schools.</p>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 1. CORE COGNITIVE PILLARS */}
                    <section id="features" className="scroll-mt-32 pt-16 pb-16">
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                            {/* Pillar 1: Smart Diagnostic Autopsy */}
                            <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 shadow-xs hover:shadow-md transition duration-300">
                                <div className="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
                                    <div className="w-8 h-8 rounded-xl bg-orange-50 text-[#FF9100] flex items-center justify-center shrink-0 border border-orange-100">
                                        <Activity className="w-4 h-4" />
                                    </div>
                                    <span>Smart Diagnostic Autopsy</span>
                                </div>
                                <p className="text-xs leading-relaxed text-slate-600">
                                    Automatically pinpoints the exact calculation step where marks were lost, just like a master teacher spotting an error pattern on a graded test paper.
                                </p>
                            </div>

                            {/* Pillar 2: 5-Minute Focus Fixes */}
                            <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 shadow-xs hover:shadow-md transition duration-300">
                                <div className="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
                                    <div className="w-8 h-8 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0 border border-emerald-100">
                                        <Wrench className="w-4 h-4" />
                                    </div>
                                    <span>5-Minute Focus Fixes</span>
                                </div>
                                <p className="text-xs leading-relaxed text-slate-600">
                                    Quick 3-question targeted practice sessions isolated purely to the single prerequisite step you stumbled on (such as calculating 15% VAT) before resuming full problems.
                                </p>
                            </div>

                            {/* Pillar 3: Fair Step Marking */}
                            <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 shadow-xs hover:shadow-md transition duration-300">
                                <div className="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
                                    <div className="w-8 h-8 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center shrink-0 border border-purple-100">
                                        <CheckSquare className="w-4 h-4" />
                                    </div>
                                    <span>Fair Step Marking</span>
                                </div>
                                <p className="text-xs leading-relaxed text-slate-600">
                                    You receive full method marks [M] for applying correct formulas and logic on subsequent steps, even if an early arithmetic calculation had a minor slip.
                                </p>
                            </div>

                            {/* Pillar 4: Skill Radar Calibration */}
                            <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 shadow-xs hover:shadow-md transition duration-300">
                                <div className="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
                                    <div className="w-8 h-8 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center shrink-0 border border-blue-100">
                                        <Radar className="w-4 h-4" />
                                    </div>
                                    <span>Skill Radar Calibration</span>
                                </div>
                                <p className="text-xs leading-relaxed text-slate-600">
                                    A thought-paced 2 to 4 check radar that skips drills you've already mastered and jumps straight to your optimal challenge tier without anxiety-inducing timers.
                                </p>
                            </div>
                        </div>
                    </section>

                    {/* 1.5 HOW IT WORKS — INTERACTIVE DEMO SIMULATIONS */}
                    <ScrollReveal delay={0.1}>
                        <section id="how-it-works" className="scroll-mt-32 pt-8 pb-16 border-b border-slate-200/80">
                            <PerspectiveShowcase
                                activePerspective={activePerspective}
                                onSelectPerspective={handlePerspectiveChange}
                                onGetStarted={onGetStarted}
                                onSignIn={onSignIn}
                                isLightPalette={true}
                            />
                        </section>
                    </ScrollReveal>

                    {/* 2. THE PROBLEM → THE PROMISE */}
                    <ScrollReveal delay={0.1}>
                        <section id="problem-promise" className="mt-8 scroll-mt-32">
                            <div className="max-w-3xl mb-10">
                                <span className="text-xs font-bold uppercase tracking-[0.25em] text-[#13519C] bg-blue-50 border border-blue-200/60 px-3 py-1 rounded-full inline-block mb-3">
                                    The Hidden Curriculum
                                </span>
                                <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    Most learners are surprised by the exam. They should not be.
                                </h2>
                                <p className="mt-4 text-base sm:text-lg leading-relaxed text-slate-600">
                                    Day-to-day classwork rarely looks like the final exam, so the real "rules of the game" stay hidden until it is too late. Fundile closes that gap: every topic is practised at exam standard, with transparent feedback on exactly where you went wrong — no surprises in November.
                                </p>
                            </div>

                            <div className="grid gap-6 md:grid-cols-3">
                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Exam-standard from day one
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Practice questions are pitched at authentic exam level from the first topic, not only at revision time.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        See where you went wrong
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Step-by-step marking shows the exact line your method broke down — and still credits the work that was correct with fair method marks.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Unlimited practice
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Deterministic generators produce endless fresh variants of any question, so you practise until it is automatic.
                                    </p>
                                </div>
                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 3. A STRUCTURED, ADAPTIVE LEARNING SYSTEM */}
                    <ScrollReveal delay={0.1}>
                        <section id="structured-system" className="mt-24 scroll-mt-32">
                            <div className="max-w-3xl mb-10">
                                <span className="text-xs font-bold uppercase tracking-[0.25em] text-[#13519C] bg-blue-50 border border-blue-200/60 px-3 py-1 rounded-full inline-block mb-3">
                                    How It Works
                                </span>
                                <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    A structured, adaptive learning system.
                                </h2>
                                <p className="mt-4 text-base sm:text-lg leading-relaxed text-slate-600">
                                    From diagnosing prerequisites to mastering final exam papers, our deterministic progression guides learners without calculation errors or generic chatbot guessing.
                                </p>
                            </div>

                            <div className="grid gap-6 md:grid-cols-3">
                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="text-xs font-bold uppercase tracking-[0.2em] text-[#13519C] mb-2">
                                        Step 01
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Pick a Topic or Take a Diagnostic
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Choose the exact subject, grade, and topic you need, or begin with a diagnostic autopsy that pinpoints your baseline against the national curriculum standard.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="text-xs font-bold uppercase tracking-[0.2em] text-[#13519C] mb-2">
                                        Step 02
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Scaffold → Practice → Assessment
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Progress through guided scaffolding, move to independent practice, and unlock exam-standard assessments with pre-baked 3-tier hints.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="text-xs font-bold uppercase tracking-[0.2em] text-[#13519C] mb-2">
                                        Step 03
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Precision Gap Autopsy & 5-Minute Focus Fixes
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        If your working stumbles, Fundile isolates the exact flawed step, awards consequential method marks, and deploys targeted 5-minute focus fixes and SimuLearn visual animations.
                                    </p>
                                </div>
                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 4. ACTIVE COGNITIVE LEARNING VS. PASSIVE CHATBOTS */}
                    <ScrollReveal delay={0.1}>
                        <section id="not-a-chatbot" className="mt-24 scroll-mt-32">
                            <div className="max-w-3xl mb-10">
                                <span className="text-xs font-bold uppercase tracking-[0.25em] text-[#13519C] bg-blue-50 border border-blue-200/60 px-3 py-1 rounded-full inline-block mb-3">
                                    Active Cognitive Learning vs. Passive Chatbots
                                </span>
                                <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    Fundile is not an AI chatbot.
                                </h2>
                                <p className="mt-4 text-base sm:text-lg leading-relaxed text-slate-600">
                                    Generic chatbots answer questions for you, encouraging passive copy-pasting and hallucinating non-existent formulas. Fundile asks you the question, enforces authentic exam-standard method working, and intervenes with precision when the learner struggles.
                                </p>
                            </div>

                            <div className="grid gap-6 md:grid-cols-2">
                                {/* Chatbot Column */}
                                <div className="rounded-[28px] border border-rose-200/90 bg-rose-50/40 p-6 sm:p-8 shadow-xs">
                                    <div className="flex items-center gap-3 mb-4">
                                        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-rose-100 text-rose-700">
                                            <MessageCircleWarning className="h-5 w-5" />
                                        </div>
                                        <div>
                                            <h3 className="text-lg sm:text-xl font-bold text-rose-950">Generic AI Chatbots</h3>
                                            <span className="text-xs font-medium text-rose-700">Passive • Hallucination Risk • Zero Accountability</span>
                                        </div>
                                    </div>
                                    <ul className="space-y-3.5 text-sm text-rose-900/80">
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-rose-500 font-bold shrink-0">✕</span>
                                            <span><strong>Gives the answer away:</strong> Solves homework for the learner without building neural pathways or cognitive automaticity.</span>
                                        </li>
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-rose-500 font-bold shrink-0">✕</span>
                                            <span><strong>Prone to hallucinations:</strong> Invents numbers, mixes up financial accounting rules, and calculates false arithmetic answers with total confidence.</span>
                                        </li>
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-rose-500 font-bold shrink-0">✕</span>
                                            <span><strong>Zero curriculum discipline:</strong> Unaware of South African national curriculum term weightings, official formula sheets, or method marking rubrics.</span>
                                        </li>
                                    </ul>
                                </div>

                                {/* Fundile Column */}
                                <div className="rounded-[28px] border-2 border-[#13519C] bg-white p-6 sm:p-8 shadow-md shadow-blue-900/10">
                                    <div className="flex items-center gap-3 mb-4">
                                        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-50 text-[#13519C]">
                                            <Sparkles className="h-5 w-5 text-[#FF9100]" />
                                        </div>
                                        <div>
                                            <h3 className="text-lg sm:text-xl font-bold text-slate-900">Fundile Cognitive Engine</h3>
                                            <span className="text-xs font-bold text-[#13519C]">Active • 100% Deterministic • National Standard</span>
                                        </div>
                                    </div>
                                    <ul className="space-y-3.5 text-sm text-slate-700">
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-emerald-600 font-bold shrink-0">✓</span>
                                            <span><strong>Stepwise procedure tracking:</strong> Awards authentic method marks, carry-over accuracy, and isolates the single line an error occurred.</span>
                                        </li>
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-emerald-600 font-bold shrink-0">✓</span>
                                            <span><strong>Mathematical and financial ground truth:</strong> Rigorous deterministic computation and authentic double-entry systems guarantee 100% precision.</span>
                                        </li>
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-emerald-600 font-bold shrink-0">✓</span>
                                            <span><strong>Diagnostic error autopsies:</strong> Tags specific misconceptions (e.g. net vs gross VAT formula) and deploys 5-minute targeted focus fixes.</span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 5. UNIVERSAL NATIONAL CURRICULUM STANDARDS */}
                    <ScrollReveal delay={0.1}>
                        <section id="curriculum-alignment" className="mt-24 scroll-mt-32">
                            <div className="max-w-3xl mb-10">
                                <span className="text-xs font-bold uppercase tracking-[0.25em] text-[#13519C] bg-blue-50 border border-blue-200/60 px-3 py-1 rounded-full inline-block mb-3">
                                    Curriculum Standards & Exam Alignment
                                </span>
                                <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    The difference is not the curriculum — it is the preparation.
                                </h2>
                                <div className="mt-4 p-4 rounded-2xl bg-blue-50 border border-blue-200/80 text-sm sm:text-base text-slate-700 leading-relaxed">
                                    <strong className="text-[#13519C] block mb-1">Did you know?</strong>
                                    There is only one official national curriculum standard in South Africa, which underpins public, private, and independent school examinations nationwide.
                                </div>
                                <p className="mt-4 text-base sm:text-lg leading-relaxed text-slate-600">
                                    Many families believe private or independent schools follow a completely different curriculum. In reality, the South African National Curriculum forms the statutory foundation for all schools—the difference lies in preparation and assessment depth. Fundile prepares learners to excel at the highest level of examination standards across all examining bodies.
                                </p>
                            </div>

                            <div className="grid gap-6 md:grid-cols-3">
                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="w-10 h-10 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center font-bold mb-4">
                                        <Landmark className="w-5 h-5" />
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Public School Examinations
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Comprehensive coverage of official national curriculum statements with authentic past exam question archetypes and official time pacing.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="w-10 h-10 rounded-xl bg-indigo-50 text-indigo-700 flex items-center justify-center font-bold mb-4">
                                        <ShieldCheck className="w-5 h-5" />
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Independent & Private School Examinations
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Higher-order multi-step questions, unseen conceptual synthesis, and rigorous rubric definitions benchmarked for top academic standards.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold mb-4">
                                        <Home className="w-5 h-5" />
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Distance & Home-Education Assessments
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Clear structured pacing with diagnostic radar checkpoints, assuring independent homeschoolers complete the national syllabus with certainty.
                                    </p>
                                </div>
                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 6. SIMPLE & TRANSPARENT PRICING */}
                    <ScrollReveal delay={0.1}>
                        <section id="pricing" className="mt-24 scroll-mt-32">
                            <div className="text-center max-w-3xl mx-auto mb-14">
                                <span className="text-xs font-bold uppercase tracking-[0.25em] text-[#13519C] bg-blue-50 border border-blue-200/60 px-3 py-1 rounded-full inline-block mb-3">
                                    Simple &amp; Transparent Pricing
                                </span>
                                <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    Accessible for Independent Learners. Scalable for Schools.
                                </h2>
                                <p className="mt-4 text-base sm:text-lg leading-relaxed text-slate-600">
                                    Private tutoring costs R150 to R350 per hour. Fundile gives you 24/7 unlimited exam practice, diagnostic autopsies, and step-by-step guidance for less than one tutoring session.
                                </p>
                            </div>

                            {/* Pricing Islands Grid (Unified Full-Curriculum Access with Term & Annual Anchors) */}
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto items-stretch">
                                {/* Island 1: Monthly Pass */}
                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-7 shadow-xs flex flex-col justify-between hover:shadow-md transition duration-300">
                                    <div>
                                        <div className="flex justify-between items-center mb-2">
                                            <span className="text-xs font-bold uppercase tracking-wider text-[#13519C]">Monthly Pass</span>
                                            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-50 text-[#13519C] border border-blue-200">Flexible</span>
                                        </div>
                                        <h3 className="text-2xl font-bold text-slate-900 mt-2">Monthly</h3>
                                        <p className="text-xs text-slate-500 mt-1 mb-4">Complete self-paced revision. Cancel anytime.</p>
                                        
                                        <div className="mt-4">
                                            <span className="text-4xl font-extrabold text-slate-900">R149</span>
                                            <span className="text-xs font-medium text-slate-500"> / month</span>
                                        </div>

                                        <ul className="mt-6 space-y-3 text-xs text-slate-600 border-t border-slate-100 pt-6">
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Full access to all 259 topics across Grades 7–12</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Step-by-step procedure tracker with method marks [M]</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Pre-baked 3-Tier hints & worked solution memos</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Lean architecture ensures extremely small use of data (&lt; 2 MB)</span>
                                            </li>
                                        </ul>
                                    </div>

                                    <div className="mt-8 pt-4">
                                        <button 
                                            type="button"
                                            onClick={onGetStarted}
                                            className="w-full inline-flex items-center justify-center py-3.5 px-4 rounded-xl text-xs font-bold text-[#13519C] bg-blue-50 hover:bg-blue-100 border border-blue-200 transition cursor-pointer"
                                        >
                                            {isDirectAuthMode ? 'Choose Monthly Pass' : 'Start 2-Week Free Trial'}
                                        </button>
                                    </div>
                                </div>

                                {/* Island 2: Term Pass (Featured - Most Popular) */}
                                <div className="rounded-[28px] border-2 border-[#13519C] bg-white p-7 shadow-lg shadow-blue-900/10 flex flex-col justify-between relative">
                                    <div className="absolute -top-3.5 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full text-xs font-extrabold bg-[#13519C] text-white shadow-sm flex items-center gap-1 whitespace-nowrap">
                                        <Star className="w-3 h-3 text-[#FF9100] fill-[#FF9100]" />
                                        <span>MOST POPULAR • TERM EXAM PREP</span>
                                    </div>

                                    <div>
                                        <div className="flex justify-between items-center mb-2 mt-2">
                                            <span className="text-xs font-bold uppercase tracking-wider text-[#FF9100]">School Term Pass</span>
                                            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-50 text-[#FF9100] border border-amber-200">Save R98</span>
                                        </div>
                                        <h3 className="text-2xl font-bold text-slate-900 mt-2">Term Pass (3 Months)</h3>
                                        <p className="text-xs text-slate-500 mt-1 mb-4">Aligned with South African school term exam deadlines.</p>
                                        
                                        <div className="mt-4">
                                            <span className="text-4xl font-extrabold text-slate-900">R349</span>
                                            <span className="text-xs font-medium text-slate-500"> / term <span className="text-emerald-600 font-bold">(~R116/mo)</span></span>
                                        </div>

                                        <ul className="mt-6 space-y-3 text-xs text-slate-700 border-t border-slate-100 pt-6">
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-[#FF9100] shrink-0" />
                                                <span><strong>Everything in Monthly Pass</strong></span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-[#FF9100] shrink-0" />
                                                <span>Post-exam triage autopsies & 5-minute targeted repairs</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-[#FF9100] shrink-0" />
                                                <span>SimuLearn visual animations (&lt; 2 MB data)</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-[#FF9100] shrink-0" />
                                                <span>Weekly Sunday 18:00 Parent WhatsApp Academic Pulse</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-[#FF9100] shrink-0" />
                                                <span>Guaranteed coverage of all Term 1–4 exam scopes</span>
                                            </li>
                                        </ul>
                                    </div>

                                    <div className="mt-8 pt-4">
                                        <button 
                                            type="button"
                                            onClick={onViewSubscription || onGetStarted}
                                            className="w-full inline-flex items-center justify-center py-3.5 px-4 rounded-xl text-xs font-bold text-white bg-[#FF9100] hover:bg-[#e68200] shadow-md transition cursor-pointer"
                                        >
                                            {isDirectAuthMode ? 'Choose Term Pass' : 'Start 2-Week Free Trial'}
                                        </button>
                                    </div>
                                </div>

                                {/* Island 3: Annual / Matric Distinction Pass */}
                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-7 shadow-xs flex flex-col justify-between hover:shadow-md transition duration-300">
                                    <div>
                                        <div className="flex justify-between items-center mb-2">
                                            <span className="text-xs font-bold uppercase tracking-wider text-emerald-700">Full Academic Year</span>
                                            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">Save R789</span>
                                        </div>
                                        <h3 className="text-2xl font-bold text-slate-900 mt-2">Annual Distinction Pass</h3>
                                        <p className="text-xs text-slate-500 mt-1 mb-4">Complete 12-month academic insurance for Grades 7–12.</p>
                                        
                                        <div className="mt-4">
                                            <span className="text-4xl font-extrabold text-slate-900">R999</span>
                                            <span className="text-xs font-medium text-slate-500"> / year <span className="text-emerald-600 font-bold">(~R83/mo)</span></span>
                                        </div>

                                        <ul className="mt-6 space-y-3 text-xs text-slate-600 border-t border-slate-100 pt-6">
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span><strong>All features across all 4 school terms</strong></span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Matric & Grade 11 Final Examination Countdown Packs</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Printable PDF past-exam papers and worked marking memos</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Priority holiday booster clinics & revision drills</span>
                                            </li>
                                        </ul>
                                    </div>

                                    <div className="mt-8 pt-4">
                                        <button 
                                            type="button"
                                            onClick={onViewSubscription || onGetStarted}
                                            className="w-full inline-flex items-center justify-center py-3.5 px-4 rounded-xl text-xs font-bold text-[#13519C] bg-blue-50 hover:bg-blue-100 border border-blue-200 transition cursor-pointer"
                                        >
                                            {isDirectAuthMode ? 'Choose Annual Pass' : 'Start 2-Week Free Trial'}
                                        </button>
                                    </div>
                                </div>
                            </div>

                            {/* Schools and SGB Institutional Banner */}
                            <div className="mt-10 max-w-4xl mx-auto rounded-2xl border border-sky-100 bg-gradient-to-r from-blue-50/80 via-white to-sky-50/80 p-5 sm:p-6 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-xs">
                                <div>
                                    <div className="flex items-center gap-2 mb-1">
                                        <span className="px-2 py-0.5 rounded-full text-[10px] font-extrabold uppercase tracking-wider bg-[#13519C] text-white">Schools &amp; SGB</span>
                                        <span className="text-xs font-bold text-slate-900">Institutional Volume Licensing</span>
                                    </div>
                                    <p className="text-xs text-slate-600 leading-relaxed">
                                        Empower entire grades with Teacher Cockpits, class heatmaps, 1-click SASAMS CSV exports, and offline practice from <strong className="text-slate-900">R45 / learner / term</strong>.
                                    </p>
                                </div>
                                <a 
                                    href="mailto:info@fundile.com?subject=School%20Volume%20Pricing%20%26%20Institutional%20Inquiry" 
                                    className="shrink-0 inline-flex items-center justify-center py-2.5 px-5 rounded-xl text-xs font-bold text-white bg-[#13519C] hover:bg-[#0e3d77] transition cursor-pointer whitespace-nowrap shadow-sm"
                                >
                                    Inquire for Schools →
                                </a>
                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 7. DEMAND CAPTURE */}
                    <ScrollReveal delay={0.1}>
                        <section id="interest-form" className="mt-24">
                            <DemandCaptureForm isLightPalette={true} />
                        </section>
                    </ScrollReveal>

                    {/* 8. AUTHENTIC INSTITUTIONAL FOOTER & POPIA */}
                    <footer className="mt-24 border-t border-slate-200 pt-12 pb-8">
                        {/* Top Brand Bar: Logo with Brand Blue Wordmark */}
                        <div className="mb-8">
                            <FundileLogo className="h-10 w-auto sm:h-12 text-[#13519C]" wordmarkColor="#13519C" />
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-10 items-start">
                            {/* Brand & Mission Column */}
                            <div className="md:col-span-2 space-y-4">
                                <p className="text-xs text-slate-500 leading-relaxed max-w-md">
                                    Fundile is South Africa’s deterministic curriculum engine and school management system. Grounded in the official National Curriculum Standards across Grades 7–12, we eliminate calculation hallucinations and empower learners, teachers, parents, and school leadership with measurable academic certainty.
                                </p>
                                <div className="flex items-center gap-3 pt-2">
                                    <span className="inline-flex items-center px-2.5 py-1 rounded-md bg-emerald-50 text-emerald-800 text-[11px] font-semibold border border-emerald-200">
                                        <ShieldCheck className="w-3.5 h-3.5 mr-1 text-emerald-600" /> POPIA Compliant (Sec 35)
                                    </span>
                                    <span className="inline-flex items-center px-2.5 py-1 rounded-md bg-blue-50 text-[#13519C] text-[11px] font-semibold border border-blue-200">
                                        <Check className="w-3.5 h-3.5 mr-1 text-[#FF9100]" /> 100% National Standard
                                    </span>
                                </div>
                                <div className="pt-2">
                                    <button
                                        type="button"
                                        onClick={() => setShowInstallModal(true)}
                                        className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-[#13519C] hover:bg-blue-800 text-white text-xs font-bold transition shadow-xs cursor-pointer border border-[#13519C]/30"
                                    >
                                        <span>📲 Install App on Mobile &amp; Desktop</span>
                                    </button>
                                </div>
                            </div>

                            {/* Stakeholders & Quick Links */}
                            <div>
                                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-900 mb-3">Stakeholders</h4>
                                <ul className="space-y-2 text-xs text-slate-600">
                                    <li><button type="button" onClick={() => handlePerspectiveChange('learners')} className="hover:text-[#13519C] transition cursor-pointer">For High School Learners</button></li>
                                    <li><button type="button" onClick={() => handlePerspectiveChange('parents')} className="hover:text-[#13519C] transition cursor-pointer">For Supportive Parents</button></li>
                                    <li><button type="button" onClick={() => handlePerspectiveChange('teachers')} className="hover:text-[#13519C] transition cursor-pointer">For Classroom Teachers</button></li>
                                    <li><button type="button" onClick={() => handlePerspectiveChange('schools')} className="hover:text-[#13519C] transition cursor-pointer">For School Admins</button></li>
                                    <li><button type="button" onClick={() => scrollToSection('features')} className="hover:text-[#13519C] transition cursor-pointer">Core Features</button></li>
                                </ul>
                            </div>

                            {/* Contact & Legal Links */}
                            <div>
                                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-900 mb-3">Institutional & Legal</h4>
                                <ul className="space-y-2 text-xs text-slate-600">
                                    <li>
                                        <a href="mailto:info@fundile.com" className="hover:text-[#13519C] transition flex items-center gap-1.5">
                                            <Mail className="w-3.5 h-3.5 text-slate-400" /> info@fundile.com
                                        </a>
                                    </li>
                                    <li>
                                        <a href="mailto:info@fundile.com?subject=School%20Pricing%20%26%20Institutional%20Inquiry" className="hover:text-[#13519C] transition flex items-center gap-1.5 font-semibold text-[#13519C]">
                                            <Building2 className="w-3.5 h-3.5" /> Institutional Inquiries
                                        </a>
                                    </li>
                                    <li>
                                        <button 
                                            type="button" 
                                            onClick={() => {
                                                if (typeof onNavigatePrivacy === 'function') {
                                                    onNavigatePrivacy();
                                                } else {
                                                    window.location.href = '/privacy';
                                                }
                                            }} 
                                            className="hover:text-[#13519C] transition flex items-center gap-1.5 cursor-pointer text-left"
                                        >
                                            <ShieldCheck className="w-3.5 h-3.5 text-slate-400" /> Privacy Policy (POPIA)
                                        </button>
                                    </li>
                                    <li>
                                        <button type="button" onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })} className="hover:text-[#13519C] transition cursor-pointer">Back to Top</button>
                                    </li>
                                </ul>
                            </div>
                        </div>

                        {/* Bottom Bar */}
                        <div className="border-t border-slate-200 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-slate-500 text-xs">
                            <div>
                                © {new Date().getFullYear()} Fundile. All rights reserved. 100% Aligned with South African National Curriculum Standards.
                            </div>
                            <div className="text-slate-400 text-[11px]">
                                Trusted preparation for public, private, and independent school examinations nationwide.
                            </div>
                        </div>
                    </footer>

                </div>
            </div>

            {/* FLOATING ACTION BUTTON: INSTALL FREE APP (Appears once user scrolls past hero section) */}
            <div 
                className={`fixed bottom-5 right-4 sm:bottom-6 sm:right-6 z-40 transition-all duration-300 ease-out transform ${
                    showFloatingInstall 
                        ? 'translate-y-0 opacity-100 scale-100' 
                        : 'translate-y-12 opacity-0 scale-90 pointer-events-none'
                }`}
            >
                <button
                    type="button"
                    onClick={() => setShowInstallModal(true)}
                    className="group relative flex items-center gap-2.5 px-3.5 py-2.5 sm:px-4.5 sm:py-3 rounded-full bg-gradient-to-r from-emerald-600 via-teal-600 to-emerald-700 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs sm:text-sm shadow-[0_10px_25px_-5px_rgba(5,150,105,0.45)] border border-emerald-300/40 backdrop-blur-md transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer"
                    title="Install Free Fundile App on Phone, Tablet or Computer"
                >
                    <span className="relative flex h-2 w-2">
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-300 opacity-75"></span>
                        <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-200"></span>
                    </span>
                    <span className="text-base sm:text-lg -ml-0.5">📲</span>
                    <span className="flex flex-col text-left leading-tight">
                        <span className="font-extrabold tracking-tight">Install Free App</span>
                        <span className="text-[10px] text-emerald-200 font-medium hidden sm:inline">Offline &amp; Low Data</span>
                    </span>
                </button>
            </div>

            {/* Direct Device Install Modal (PWA & WebAPK) */}
            <InstallAppModal 
                isOpen={showInstallModal} 
                onClose={() => setShowInstallModal(false)} 
            />
        </div>
    );
};

export default LandingPage;
