import React, { useMemo } from 'react';
import {
  ArrowRight,
  Sparkles,
  CheckCircle2,
  GraduationCap,
  Building2,
  BookOpen,
  ShieldCheck,
  Globe,
  Layers,
  ChevronRight,
  ExternalLink,
} from 'lucide-react';
import FundileLogo from './FundileLogo';
import DemandCaptureForm from './DemandCaptureForm';
import { getCountryConfig, COUNTRY_CURRICULA, ALL_COUNTRY_CODES } from '../../app/constants/countryCurricula';

/**
 * CountrySkeletonLanding
 * 
 * Localized curriculum preview and early access waitlist landing page for:
 * - Zimbabwe (/zw)
 * - Tanzania (/tz)
 * - Kenya (/ke)
 * - Ghana (/gh)
 * - Nigeria (/ng)
 * 
 * Provides authentic regional curriculum details, planned subject roadmap,
 * and early access registration while directing users to the live South African
 * platform (/za) whenever desired.
 */
export default function CountrySkeletonLanding({
  countryCode = 'zw',
  db,
  onSwitchToSouthAfrica,
  onSwitchCountry,
  onSignIn,
  onNavigatePrivacy,
}) {
  const country = useMemo(() => getCountryConfig(countryCode), [countryCode]);

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 font-sans antialiased selection:bg-[#FF9100]/20 selection:text-[#13519C]">
      
      {/* ── TOP NOTIFICATION RIBBON ── */}
      <aside
        aria-label="Regional Availability"
        className="bg-gradient-to-r from-[#13519C] via-[#1a63bc] to-[#13519C] text-white px-4 py-2.5 text-xs text-center font-medium shadow-xs"
      >
        <div className="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2">
          <div className="flex items-center gap-2">
            <span className="px-2 py-0.5 rounded-full bg-amber-400 text-slate-950 font-black text-[10px] uppercase tracking-wider">
              Preview Mode
            </span>
            <span>
              Fundile {country.name} is scheduled for rollout. Looking for the fully live platform?
            </span>
          </div>
          <button
            type="button"
            onClick={onSwitchToSouthAfrica}
            className="inline-flex items-center gap-1.5 font-bold text-amber-300 hover:text-white underline decoration-amber-300 underline-offset-2 transition cursor-pointer"
          >
            <span>Explore South Africa (Active Now)</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </aside>

      {/* ── STICKY NAVIGATION BAR ── */}
      <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={onSwitchToSouthAfrica}
              className="flex items-center gap-2 cursor-pointer focus:outline-none"
              title="Fundile Home"
            >
              <FundileLogo className="h-7 w-auto" />
            </button>
            <span className="text-slate-300 font-light hidden sm:inline">|</span>
            <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-slate-100 border border-slate-200 text-xs font-bold text-slate-700">
              <span className="text-sm">{country.flag}</span>
              <span>{country.name}</span>
              <span className="text-[10px] font-semibold text-slate-400 uppercase tracking-wider ml-1">
                Upcoming
              </span>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={onSwitchToSouthAfrica}
              className="hidden md:inline-flex items-center gap-2 px-3.5 py-1.5 rounded-xl border border-blue-200 bg-blue-50/70 hover:bg-blue-100/80 text-[#13519C] text-xs font-bold transition cursor-pointer"
            >
              <span>🇿🇦 Live in South Africa</span>
            </button>
            {onSignIn && (
              <button
                type="button"
                onClick={onSignIn}
                className="px-4 py-1.5 rounded-xl border border-slate-300 hover:border-slate-400 text-slate-700 text-xs font-bold transition cursor-pointer"
              >
                Sign In
              </button>
            )}
          </div>
        </div>
      </header>

      {/* ── HERO SECTION ── */}
      <main className="max-w-6xl mx-auto px-4 sm:px-6 pt-12 pb-20 space-y-16">
        <section className="text-center max-w-3xl mx-auto space-y-6">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-[#13519C] text-xs font-bold shadow-2xs">
            <Sparkles className="w-3.5 h-3.5 text-[#FF9100]" />
            <span>{country.heroEyebrow || `${country.name} Curriculum Assistant • Coming Soon`}</span>
          </div>

          <h1 className="text-3xl sm:text-5xl font-extrabold tracking-tight text-slate-900 leading-tight">
            {country.heroTitle || `Master Secondary Exams in ${country.name}`}
          </h1>

          <p className="text-base sm:text-lg text-slate-600 leading-relaxed max-w-2xl mx-auto">
            {country.tagline || `We are bringing Fundile's deterministic learning engine, step-by-step procedure tracking, and adaptive practice to ${country.name}.`}
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
            <a
              href="#waitlist"
              className="w-full sm:w-auto px-6 py-3.5 rounded-2xl bg-[#FF9100] hover:bg-[#e07f00] text-slate-950 font-black text-sm shadow-md hover:shadow-lg transition flex items-center justify-center gap-2 cursor-pointer"
            >
              <span>Join {country.name} Early Access</span>
              <ArrowRight className="w-4 h-4" />
            </a>
            <button
              type="button"
              onClick={onSwitchToSouthAfrica}
              className="w-full sm:w-auto px-6 py-3.5 rounded-2xl border border-slate-300 hover:border-slate-400 bg-white text-slate-800 font-bold text-sm shadow-2xs transition flex items-center justify-center gap-2 cursor-pointer"
            >
              <span>View Live South African Platform</span>
              <ExternalLink className="w-3.5 h-3.5 text-slate-400" />
            </button>
          </div>
        </section>

        {/* ── REGIONAL CURRICULUM ARCHITECTURE CARDS ── */}
        <section className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="p-5 rounded-2xl bg-white border border-slate-200 shadow-2xs space-y-2">
            <div className="w-9 h-9 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center font-bold">
              <BookOpen className="w-5 h-5" />
            </div>
            <h3 className="font-bold text-slate-900 text-sm">Curriculum Standard</h3>
            <p className="text-xs text-slate-600 font-medium leading-relaxed">
              {country.curriculumTitle}
            </p>
            <p className="text-[11px] text-slate-400 leading-tight">
              {country.examAlignment}
            </p>
          </div>

          <div className="p-5 rounded-2xl bg-white border border-slate-200 shadow-2xs space-y-2">
            <div className="w-9 h-9 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold">
              <GraduationCap className="w-5 h-5" />
            </div>
            <h3 className="font-bold text-slate-900 text-sm">Academic Structure</h3>
            <p className="text-xs text-slate-600 font-medium leading-relaxed">
              {country.stages}
            </p>
            <p className="text-[11px] text-slate-400 leading-tight">
              Calibrated to authentic national examination grading brackets.
            </p>
          </div>

          <div className="p-5 rounded-2xl bg-white border border-slate-200 shadow-2xs space-y-2">
            <div className="w-9 h-9 rounded-xl bg-purple-50 text-purple-700 flex items-center justify-center font-bold">
              <Layers className="w-5 h-5" />
            </div>
            <h3 className="font-bold text-slate-900 text-sm">Local Payment Rails</h3>
            <p className="text-xs text-slate-600 font-medium leading-relaxed">
              {country.currency} ({country.currencySymbol})
            </p>
            <p className="text-[11px] text-slate-400 leading-tight">
              {country.paymentMethods}
            </p>
          </div>

          <div className="p-5 rounded-2xl bg-white border border-slate-200 shadow-2xs space-y-2">
            <div className="w-9 h-9 rounded-xl bg-amber-50 text-amber-700 flex items-center justify-center font-bold">
              <ShieldCheck className="w-5 h-5" />
            </div>
            <h3 className="font-bold text-slate-900 text-sm">Pedagogical Contract</h3>
            <p className="text-xs text-slate-600 font-medium leading-relaxed">
              100% Deterministic Engine
            </p>
            <p className="text-[11px] text-slate-400 leading-tight">
              SymPy procedural checking, 3-tier pre-computed hints &amp; zero hallucination.
            </p>
          </div>
        </section>

        {/* ── PLANNED SUBJECT ROADMAP ── */}
        <section className="p-6 sm:p-8 rounded-3xl bg-white border border-slate-200 shadow-xs space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-100 pb-4">
            <div>
              <span className="text-xs font-bold text-[#13519C] uppercase tracking-wider">
                Planned Roadmap
              </span>
              <h3 className="text-xl font-bold text-slate-900">
                Core Subjects Planned for {country.name}
              </h3>
            </div>
            <span className="text-xs text-slate-500 font-medium">
              Aligned with {country.shortCurriculum}
            </span>
          </div>

          <div className="grid sm:grid-cols-2 md:grid-cols-3 gap-3 pt-2">
            {country.plannedSubjects.map((subject, idx) => (
              <div
                key={idx}
                className="p-3.5 rounded-xl border border-slate-100 bg-slate-50/70 flex items-center gap-3 text-xs font-bold text-slate-800"
              >
                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                <span>{subject}</span>
              </div>
            ))}
          </div>
        </section>

        {/* ── EARLY ACCESS WAITLIST CAPTURE ── */}
        <section id="waitlist" className="max-w-2xl mx-auto pt-4">
          <DemandCaptureForm
            db={db}
            source={`waitlist_${country.code}`}
            title={`Be First in Line: Fundile ${country.name}`}
            description={`Tell us what subject, school, or stage you need in ${country.name}. School administrators, teachers, and parents receive early access invites as our pilot launches.`}
            submitLabel={`Register for ${country.name} Early Access`}
            isLightPalette={true}
          />
        </section>

        {/* ── REGIONAL DIRECTORY / COUNTRY SWITCHER ── */}
        <section className="border-t border-slate-200 pt-10 space-y-4 text-center">
          <div className="flex items-center justify-center gap-2 text-xs font-bold text-slate-500 uppercase tracking-wider">
            <Globe className="w-4 h-4 text-slate-400" />
            <span>Pan-African Curriculum Network</span>
          </div>

          <div className="flex flex-wrap items-center justify-center gap-2 max-w-4xl mx-auto">
            {ALL_COUNTRY_CODES.map((code) => {
              const c = COUNTRY_CURRICULA[code];
              const isActive = code === country.code;
              const isLive = c.status === 'active';

              return (
                <button
                  key={code}
                  type="button"
                  onClick={() => {
                    if (code === 'za') {
                      onSwitchToSouthAfrica?.();
                    } else if (onSwitchCountry) {
                      onSwitchCountry(code);
                    }
                  }}
                  className={`px-3.5 py-2 rounded-xl text-xs font-bold transition flex items-center gap-1.5 cursor-pointer ${
                    isActive
                      ? 'bg-[#13519C] text-white shadow-xs'
                      : isLive
                      ? 'bg-blue-50 border border-blue-200 text-[#13519C] hover:bg-blue-100'
                      : 'bg-white border border-slate-200 text-slate-700 hover:bg-slate-100'
                  }`}
                >
                  <span className="text-sm">{c.flag}</span>
                  <span>{c.name}</span>
                  {isLive && (
                    <span className="px-1.5 py-0.2 rounded text-[9px] bg-emerald-500 text-white font-extrabold uppercase ml-1">
                      Live
                    </span>
                  )}
                </button>
              );
            })}
          </div>
        </section>
      </main>

      {/* ── FOOTER ── */}
      <footer className="border-t border-slate-200 bg-white py-8 text-center text-xs text-slate-500 space-y-2">
        <p>© {new Date().getFullYear()} Fundile Education. All rights reserved.</p>
        <p className="max-w-2xl mx-auto px-4 text-[11px] text-slate-400 leading-relaxed">
          Fundile is an independent educational platform. All national curriculum frameworks, examination board names, and trademarks (including ZIMSEC, NECTA, KICD, KNEC, NaCCA, WAEC, NECO, and JAMB) belong to their respective statutory owners.
        </p>
        {onNavigatePrivacy && (
          <p>
            <button
              type="button"
              onClick={onNavigatePrivacy}
              className="text-slate-600 hover:text-slate-900 underline underline-offset-2 transition cursor-pointer"
            >
              Privacy Statement (POPIA Compliant)
            </button>
          </p>
        )}
      </footer>
    </div>
  );
}
