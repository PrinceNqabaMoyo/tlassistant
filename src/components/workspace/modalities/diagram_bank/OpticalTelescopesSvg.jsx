import React, { useState, useEffect, useRef, useMemo } from 'react';
import InteractiveCallouts from './InteractiveCallouts';
import {
  Globe,
  BookOpen,
  FileText,
  Sparkles,
  Play,
  Pause,
  Eye,
  Sliders,
  Maximize2,
  Info,
} from 'lucide-react';

function normalizeTelescopeView(rawView) {
  const v = String(rawView || 'textbook').toLowerCase().trim();
  if (v === 'exam' || v === 'exam_paper' || v === 'stipple') return 'exam';
  if (v === 'alive' || v === 'sim' || v === 'simulation') return 'alive';
  return 'textbook';
}

const VIEW_METADATA = {
  textbook: {
    label: 'Astronomical Optical Telescopes Master (Reflector vs Refractor)',
    Icon: BookOpen,
  },
  exam: {
    label: 'Examination Ink Stipple Line-Art',
    Icon: FileText,
  },
  alive: {
    label: 'Dynamic Optical Ray-Tracing & Dispersion Simulation',
    Icon: Sparkles,
  },
};

/**
 * Authentic Astronomical Optical Telescopes Ray-Tracing Schematic.
 * Aligned with South African Natural Sciences Grade 8 ("Looking into space", SALT)
 * and Physical Sciences Grade 10/11 (Geometric Optics).
 *
 * Implements Rule 0d-14 (The Heart Standard) & Dual Static/Alive Engine:
 * - Static Mode: Authentic Textbook Master + NSC Exam Stipple plates in public/diagrams/
 * - Alive Mode: 60 FPS dynamic ray-tracing simulation showing starlight photon paths,
 *   primary mirror reflection, focal convergence, eyepiece magnification, and chromatic aberration.
 */
export default function OpticalTelescopesSvg({
  pins = [],
  landmarks = [],
  labels = [],
  activePin,
  onSelectPin,
  viewBox = '0 0 600 480',
  gradeMask = 'g8',
  view,
  defaultView = 'textbook',
  allowViewSwitch = false,
  showSimControls = true,
  playbackSpeed: propPlaybackSpeed,
  initialMode = 'comparative',
}) {
  const initialView = normalizeTelescopeView(view || defaultView);
  const [activeView, setActiveView] = useState(initialView);
  const [isAlive, setIsAlive] = useState(initialView === 'alive');

  // Simulation controls
  const [isPlaying, setIsPlaying] = useState(true);
  const [playbackSpeed, setPlaybackSpeed] = useState(propPlaybackSpeed || 1.0);
  const [telescopeFilter, setTelescopeFilter] = useState(initialMode); // 'comparative', 'reflector', 'refractor'
  const [wavelengthNm, setWavelengthNm] = useState(550); // green 550nm
  const [demonstrateDispersion, setDemonstrateDispersion] = useState(false);
  const [trackedPhoton, setTrackedPhoton] = useState(false);

  useEffect(() => {
    const v = normalizeTelescopeView(view || defaultView);
    setActiveView(v);
    setIsAlive(v === 'alive');
  }, [view, defaultView]);

  useEffect(() => {
    if (propPlaybackSpeed !== undefined) setPlaybackSpeed(propPlaybackSpeed);
  }, [propPlaybackSpeed]);

  // Normalize pins
  const effectivePins =
    pins && pins.length > 0
      ? pins
      : labels && labels.length > 0
      ? labels.map((l) => ({
          pin: l.id || l.pin,
          anchor: [
            l.x !== undefined ? (l.x / 100) * 600 : 300,
            l.y !== undefined ? (l.y / 100) * 480 : 240,
          ],
          default_box: [
            l.x < 50 ? 60 : 540,
            l.y !== undefined ? (l.y / 100) * 480 : 240,
          ],
          side: l.x < 50 ? 'left' : 'right',
          role: 'target',
        }))
      : [];

  const currentMeta = VIEW_METADATA[isAlive ? 'alive' : activeView] || VIEW_METADATA.textbook;
  const CurrentViewIcon = currentMeta.Icon;

  // ---------------------------------------------------------------------------
  // 60 FPS Simulation Loop
  // ---------------------------------------------------------------------------
  const [simTime, setSimTime] = useState(0);
  const animFrameRef = useRef(null);
  const lastTimeRef = useRef(performance.now());

  useEffect(() => {
    if (!isAlive || !isPlaying) {
      if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
      return;
    }

    const animate = (now) => {
      const dt = (now - lastTimeRef.current) / 1000;
      lastTimeRef.current = now;
      setSimTime((prev) => prev + dt * playbackSpeed);
      animFrameRef.current = requestAnimationFrame(animate);
    };

    lastTimeRef.current = performance.now();
    animFrameRef.current = requestAnimationFrame(animate);

    return () => {
      if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
    };
  }, [isAlive, isPlaying, playbackSpeed]);

  // Optical calculations
  // Refractor focal lengths: f_objective = 800 mm, f_eyepiece = 20 mm -> M = 40x
  // Reflector focal lengths: f_primary = 1200 mm, f_eyepiece = 20 mm -> M = 60x
  const magnificationReflector = 60;
  const magnificationRefractor = 40;

  // Starlight Ray Pulse Trajectories
  // 1. Reflector Ray Path:
  // Leg 1: (x: 40 -> 510, y: 75 or 185) incoming parallel
  // Leg 2: (x: 510 -> 210, y: 75/185 -> 125/135) converging to 45 deg secondary mirror
  // Leg 3: (x: 210, y: 130 -> 230) reflecting 90 deg down through eyepiece
  const reflectorPulses = useMemo(() => {
    const pulses = [];
    const count = 6;
    for (let i = 0; i < count; i++) {
      const offset = i / count;
      const progress = ((simTime * 0.4 + offset) % 1 + 1) % 1;

      let px, py;
      const isTopRay = i % 2 === 0;
      const startY = isTopRay ? 75 : 185;

      if (progress < 0.45) {
        // Leg 1: Incoming from space to primary mirror
        const u = progress / 0.45;
        px = 40 + u * 470;
        py = startY;
      } else if (progress < 0.8) {
        // Leg 2: Primary mirror reflection toward secondary diagonal mirror
        const u = (progress - 0.45) / 0.35;
        px = 510 - u * 300;
        py = startY + u * (130 - startY);
      } else {
        // Leg 3: Secondary mirror downward reflection through eyepiece
        const u = (progress - 0.8) / 0.2;
        px = 210;
        py = 130 + u * 100;
      }

      pulses.push({
        id: `refl_pulse_${i}`,
        index: i,
        x: px,
        y: py,
        color: '#facc15', // gold starlight
      });
    }
    return pulses;
  }, [simTime]);

  // 2. Refractor Ray Path:
  // Leg 1: (x: 40 -> 170, y: 310 or 380) incoming parallel
  // Leg 2: (x: 170 -> 390, y: 310/380 -> 345) converging to focal point F
  // Leg 3: (x: 390 -> 500, y: 345 -> 380/310) expanding past focus to eyepiece lens
  // Leg 4: (x: 500 -> 560, y: 380/310) parallel exit beam
  const refractorPulses = useMemo(() => {
    const pulses = [];
    const count = 6;
    for (let i = 0; i < count; i++) {
      const offset = i / count;
      const progress = ((simTime * 0.4 + offset) % 1 + 1) % 1;

      let px, py;
      const isTopRay = i % 2 === 0;
      const startY = isTopRay ? 310 : 380;
      const exitY = isTopRay ? 380 : 310;

      if (progress < 0.25) {
        // Leg 1: Incoming to objective lens
        const u = progress / 0.25;
        px = 40 + u * 130;
        py = startY;
      } else if (progress < 0.65) {
        // Leg 2: Refraction to focal point (390, 345)
        const u = (progress - 0.25) / 0.4;
        px = 170 + u * 220;
        py = startY + u * (345 - startY);
      } else if (progress < 0.85) {
        // Leg 3: Passing through focal point toward eyepiece lens (500)
        const u = (progress - 0.65) / 0.2;
        px = 390 + u * 110;
        py = 345 + u * (exitY - 345);
      } else {
        // Leg 4: Collimated exit from eyepiece into eye
        const u = (progress - 0.85) / 0.15;
        px = 500 + u * 60;
        py = exitY;
      }

      pulses.push({
        id: `refr_pulse_${i}`,
        index: i,
        x: px,
        y: py,
        color: demonstrateDispersion ? (isTopRay ? '#38bdf8' : '#f87171') : '#38bdf8',
      });
    }
    return pulses;
  }, [simTime, demonstrateDispersion]);

  return (
    <div
      data-testid="optical-telescopes-root"
      className="flex flex-col items-center w-full max-w-2xl select-none space-y-2 font-sans"
    >
      {/* Header Bar */}
      {allowViewSwitch ? (
        <div className="flex items-center justify-between w-full px-2 py-1 bg-slate-50 border border-slate-200 rounded-xl text-xs">
          <span className="text-[11px] font-bold text-slate-600 uppercase tracking-wide flex items-center gap-1.5 font-mono">
            <Globe className="w-3.5 h-3.5 text-blue-600" />
            Telescope Optical Engine:
          </span>
          <div className="flex gap-1">
            <button
              type="button"
              data-testid="btn-view-textbook"
              onClick={() => {
                setActiveView('textbook');
                setIsAlive(false);
              }}
              className={`px-2.5 py-1 rounded-lg font-bold text-[11px] transition cursor-pointer flex items-center gap-1 ${
                !isAlive && activeView === 'textbook'
                  ? 'bg-[#13519C] text-white shadow-2xs'
                  : 'bg-white text-slate-700 hover:bg-slate-100 border border-slate-200'
              }`}
            >
              <BookOpen className="w-3 h-3" />
              <span>Textbook Master</span>
            </button>
            <button
              type="button"
              data-testid="btn-view-exam"
              onClick={() => {
                setActiveView('exam');
                setIsAlive(false);
              }}
              className={`px-2.5 py-1 rounded-lg font-bold text-[11px] transition cursor-pointer flex items-center gap-1 ${
                !isAlive && activeView === 'exam'
                  ? 'bg-[#13519C] text-white shadow-2xs'
                  : 'bg-white text-slate-700 hover:bg-slate-100 border border-slate-200'
              }`}
            >
              <FileText className="w-3 h-3" />
              <span>Exam Paper</span>
            </button>
            <button
              type="button"
              data-testid="btn-bring-to-life"
              onClick={() => setIsAlive(true)}
              className={`px-2.5 py-1 rounded-lg font-bold text-[11px] transition cursor-pointer flex items-center gap-1 ${
                isAlive
                  ? 'bg-amber-600 text-white shadow-2xs'
                  : 'bg-amber-50 text-amber-800 hover:bg-amber-100 border border-amber-300'
              }`}
            >
              <Sparkles className="w-3 h-3" />
              <span>Alive Simulation</span>
            </button>
          </div>
        </div>
      ) : (
        <div
          data-testid="telescopes-locked-view-badge"
          className="flex items-center justify-between w-full px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs"
        >
          <span className="text-[11px] font-bold text-slate-700 flex items-center gap-1.5 font-mono">
            <CurrentViewIcon className="w-3.5 h-3.5 text-blue-600" />
            <span>{currentMeta.label}</span>
          </span>
          <div className="flex items-center gap-2">
            {!isAlive ? (
              <button
                type="button"
                data-testid="btn-bring-to-life"
                onClick={() => setIsAlive(true)}
                className="px-2.5 py-1 rounded-lg font-bold text-[11px] transition cursor-pointer flex items-center gap-1 bg-amber-500 hover:bg-amber-600 text-white shadow-2xs"
              >
                <Sparkles className="w-3 h-3" />
                <span>Bring It To Life</span>
              </button>
            ) : (
              <button
                type="button"
                data-testid="btn-back-to-exam"
                onClick={() => setIsAlive(false)}
                className="px-2.5 py-1 rounded-lg font-bold text-[11px] transition cursor-pointer flex items-center gap-1 bg-slate-200 hover:bg-slate-300 text-slate-800"
              >
                <FileText className="w-3 h-3" />
                <span>Back to Exam Plate</span>
              </button>
            )}
            <span className="text-[10px] font-mono text-slate-500 uppercase tracking-wider">
              Natural Sciences Gr8 (SALT)
            </span>
          </div>
        </div>
      )}

      {/* Backward-compatibility badge */}
      <span data-testid="optical_telescopes-locked-view-badge" className="sr-only">Locked View</span>

      {/* Simulation Interactive Control Bar (Alive mode only) */}
      {isAlive && showSimControls && (
        <div
          data-testid="telescope-sim-controls"
          className="flex flex-wrap items-center justify-between w-full p-2.5 bg-slate-900 text-white rounded-xl text-xs gap-2 shadow-md border border-slate-800 font-sans"
        >
          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-play-pause-sim"
              onClick={() => setIsPlaying((p) => !p)}
              className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-400 cursor-pointer transition"
              title={isPlaying ? 'Pause' : 'Play'}
            >
              {isPlaying ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
            </button>
            <button
              type="button"
              data-testid="btn-speed-toggle"
              onClick={() => {
                const nextSpeed = playbackSpeed === 1.0 ? 2.0 : playbackSpeed === 2.0 ? 0.5 : 1.0;
                setPlaybackSpeed(nextSpeed);
              }}
              className="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 font-mono font-bold text-[11px] text-slate-300 cursor-pointer transition"
            >
              {playbackSpeed}x
            </button>
          </div>

          {/* Design Filter Tabs */}
          <div className="flex items-center gap-1">
            <button
              type="button"
              data-testid="btn-filter-all"
              onClick={() => setTelescopeFilter('comparative')}
              className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono ${telescopeFilter === 'comparative' ? 'bg-blue-600 text-white' : 'bg-slate-800 text-slate-400'}`}
            >
              Both (SALT vs Refractor)
            </button>
            <button
              type="button"
              data-testid="btn-filter-reflector"
              onClick={() => setTelescopeFilter('reflector')}
              className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono ${telescopeFilter === 'reflector' ? 'bg-blue-600 text-white' : 'bg-slate-800 text-slate-400'}`}
            >
              Reflecting Only
            </button>
            <button
              type="button"
              data-testid="btn-filter-refractor"
              onClick={() => setTelescopeFilter('refractor')}
              className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono ${telescopeFilter === 'refractor' ? 'bg-blue-600 text-white' : 'bg-slate-800 text-slate-400'}`}
            >
              Refracting Only
            </button>
          </div>

          {/* Chromatic Aberration Toggle */}
          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-toggle-aberration"
              onClick={() => setDemonstrateDispersion((d) => !d)}
              className={`px-2 py-1 rounded-md text-[10px] font-bold font-mono transition cursor-pointer flex items-center gap-1 ${
                demonstrateDispersion ? 'bg-red-600 text-white' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              <Sliders className="w-3 h-3 text-cyan-400" />
              <span>{demonstrateDispersion ? 'Dispersion ON' : 'Show Chromatic Aberration'}</span>
            </button>
            <button
              type="button"
              data-testid="btn-follow-photon"
              onClick={() => setTrackedPhoton((p) => !p)}
              className={`px-2 py-1 rounded-md text-[10px] font-bold font-mono transition cursor-pointer flex items-center gap-1 ${
                trackedPhoton ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              <Eye className="w-3 h-3" />
              <span>{trackedPhoton ? 'Tracking Photon' : 'Track Photon'}</span>
            </button>
          </div>
        </div>
      )}

      {/* Primary SVG Canvas */}
      <svg
        viewBox={viewBox}
        data-testid="telescopes-canvas"
        className="w-full h-auto drop-shadow-sm bg-white rounded-xl border border-slate-100 transition-all duration-300"
        style={{ minWidth: '320px', maxHeight: '520px' }}
      >
        <defs>
          <filter id="photonGlow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="3" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
          </filter>
        </defs>

        {/* MODE 1: STATIC EXAM PLATES */}
        {!isAlive && activeView === 'textbook' && (
          <g id="view_textbook_master">
            <image
              href="/diagrams/optical_telescopes_textbook.jpg"
              x="20"
              y="0"
              width="560"
              height="480"
              preserveAspectRatio="xMidYMid meet"
              className="select-none pointer-events-none"
            />
          </g>
        )}

        {!isAlive && activeView === 'exam' && (
          <g id="view_exam_paper">
            <image
              href="/diagrams/optical_telescopes_exam_stipple.jpg"
              x="20"
              y="0"
              width="560"
              height="480"
              preserveAspectRatio="xMidYMid meet"
              className="select-none pointer-events-none"
            />
          </g>
        )}

        {/* MODE 2: ALIVE DYNAMIC RAY-TRACING SIMULATION */}
        {isAlive && (
          <g id="alive_optical_simulation" data-testid="alive-optical-simulation">
            {/* 1. TOP TUBE: NEWTONIAN REFLECTING TELESCOPE (SALT DESIGN) */}
            {(telescopeFilter === 'comparative' || telescopeFilter === 'reflector') && (
              <g id="sim_reflecting_telescope" transform="translate(0, 0)">
                {/* Telescope Tube Outline */}
                <rect x="150" y="55" width="380" height="150" rx="8" fill="#1e293b" stroke="#475569" strokeWidth="3" />
                {/* Open Aperture at Left */}
                <line x1="150" y1="55" x2="150" y2="205" stroke="#0ea5e9" strokeWidth="3" strokeDasharray="4 4" />
                <text x="140" y="130" textAnchor="end" fill="#0284c7" fontSize="10" fontWeight="bold">
                  Open Aperture
                </text>

                {/* Primary Concave Curved Mirror at Right */}
                <path d="M 520,65 Q 500,130 520,195 L 532,195 L 532,65 Z" fill="#94a3b8" stroke="#f1f5f9" strokeWidth="2" />
                <text x="545" y="135" fill="#f8fafc" fontSize="10" fontWeight="bold">
                  Primary Mirror
                </text>

                {/* 45-Degree Flat Secondary Diagonal Mirror near aperture */}
                <line x1="195" y1="110" x2="225" y2="150" stroke="#f8fafc" strokeWidth="4" />
                <line x1="195" y1="110" x2="225" y2="150" stroke="#94a3b8" strokeWidth="1" />

                {/* Eyepiece Holder & Lens on Bottom Side */}
                <rect x="195" y="205" width="30" height="35" rx="3" fill="#334155" stroke="#64748b" strokeWidth="2" />
                <ellipse cx="210" cy="225" rx="12" ry="4" fill="#bae6fd" stroke="#0284c7" strokeWidth="1.5" />
                <text x="235" y="235" fill="#0284c7" fontSize="9" fontWeight="bold">
                  Eyepiece (Observer Eye)
                </text>

                {/* Static Ray Path Reference Lines */}
                <g stroke="#facc15" strokeWidth="1.5" opacity="0.45">
                  <line x1="40" y1="75" x2="515" y2="75" />
                  <line x1="40" y1="185" x2="515" y2="185" />
                  <line x1="515" y1="75" x2="210" y2="125" />
                  <line x1="515" y1="185" x2="210" y2="135" />
                  <line x1="210" y1="130" x2="210" y2="235" />
                </g>

                {/* Animated Photon Pulses flowing along reflector rays */}
                {reflectorPulses.map((pulse) => {
                  const isTracked = trackedPhoton && pulse.index === 0;
                  return (
                    <g key={pulse.id}>
                      {isTracked && (
                        <circle cx={pulse.x} cy={pulse.y} r="8" fill="none" stroke="#f59e0b" strokeWidth="2" />
                      )}
                      <circle
                        cx={pulse.x}
                        cy={pulse.y}
                        r="3.5"
                        fill={pulse.color}
                        filter="url(#photonGlow)"
                      />
                    </g>
                  );
                })}

                {/* Section Badge */}
                <text x="165" y="80" fill="#facc15" fontSize="11" fontWeight="bold">
                  REFLECTING TELESCOPE (SALT Standard — Zero Chromatic Aberration)
                </text>
              </g>
            )}

            {/* 2. BOTTOM TUBE: KEPLERIAN REFRACTING TELESCOPE */}
            {(telescopeFilter === 'comparative' || telescopeFilter === 'refractor') && (
              <g id="sim_refracting_telescope" transform="translate(0, 0)">
                {/* Telescope Tube Outline */}
                <rect x="150" y="275" width="375" height="140" rx="8" fill="#1e293b" stroke="#475569" strokeWidth="3" />

                {/* Large Convex Objective Lens at Left Entrance */}
                <path d="M 170,285 Q 185,345 170,405 Q 155,345 170,285 Z" fill="#bae6fd" stroke="#38bdf8" strokeWidth="2" opacity="0.85" />
                <text x="160" y="270" textAnchor="end" fill="#0284c7" fontSize="10" fontWeight="bold">
                  Convex Objective Lens
                </text>

                {/* Principal Optical Axis */}
                <line x1="130" y1="345" x2="550" y2="345" stroke="#64748b" strokeWidth="1" strokeDasharray="6 4" opacity="0.5" />

                {/* Principal Focus Point F */}
                <circle cx="390" cy="345" r="4" fill="#38bdf8" />
                <text x="390" y="365" textAnchor="middle" fill="#38bdf8" fontSize="10" fontWeight="bold">
                  Focus (F)
                </text>

                {/* Convex Eyepiece Lens at Right */}
                <path d="M 500,310 Q 510,345 500,380 Q 490,345 500,310 Z" fill="#bae6fd" stroke="#38bdf8" strokeWidth="2" opacity="0.85" />
                <text x="515" y="335" fill="#38bdf8" fontSize="10" fontWeight="bold">
                  Eyepiece Lens
                </text>

                {/* Static Refractor Ray Lines */}
                <g stroke="#38bdf8" strokeWidth="1.5" opacity="0.45">
                  <line x1="40" y1="310" x2="170" y2="310" />
                  <line x1="40" y1="380" x2="170" y2="380" />
                  <line x1="170" y1="310" x2="390" y2="345" />
                  <line x1="170" y1="380" x2="390" y2="345" />
                  <line x1="390" y1="345" x2="500" y2="380" />
                  <line x1="390" y1="345" x2="500" y2="310" />
                  <line x1="500" y1="310" x2="560" y2="310" />
                  <line x1="500" y1="380" x2="560" y2="380" />
                </g>

                {/* Chromatic Dispersion Rays (Demonstrating why blue bends more than red: n_blue > n_red) */}
                {demonstrateDispersion && (
                  <g opacity="0.8">
                    {/* Blue rays focus closer */}
                    <line x1="170" y1="310" x2="375" y2="345" stroke="#3b82f6" strokeWidth="1.5" strokeDasharray="3 2" />
                    <line x1="170" y1="380" x2="375" y2="345" stroke="#3b82f6" strokeWidth="1.5" strokeDasharray="3 2" />
                    <text x="365" y="330" fill="#3b82f6" fontSize="9" fontWeight="bold">F_blue</text>

                    {/* Red rays focus farther */}
                    <line x1="170" y1="310" x2="410" y2="345" stroke="#ef4444" strokeWidth="1.5" strokeDasharray="3 2" />
                    <line x1="170" y1="380" x2="410" y2="345" stroke="#ef4444" strokeWidth="1.5" strokeDasharray="3 2" />
                    <text x="420" y="330" fill="#ef4444" fontSize="9" fontWeight="bold">F_red</text>
                  </g>
                )}

                {/* Animated Photon Pulses flowing along refractor rays */}
                {refractorPulses.map((pulse) => {
                  return (
                    <circle
                      key={pulse.id}
                      cx={pulse.x}
                      cy={pulse.y}
                      r="3.5"
                      fill={pulse.color}
                      filter="url(#photonGlow)"
                    />
                  );
                })}

                {/* Section Badge */}
                <text x="165" y="300" fill="#38bdf8" fontSize="11" fontWeight="bold">
                  REFRACTING TELESCOPE (Galilean/Keplerian — Subject to Chromatic Aberration)
                </text>
              </g>
            )}

            {/* ================================================================ */}
            {/* SCIENTIFIC HUD METERS PANEL (bottom of viewBox)                  */}
            {/* ================================================================ */}
            <g id="hud_telemetry_panel" transform="translate(45, 422)">
              <rect
                x="0"
                y="0"
                width="510"
                height="50"
                rx="10"
                fill="#0f172a"
                stroke="#334155"
                strokeWidth="1.5"
              />

              {/* Meter 1: Reflector Magnification */}
              <g transform="translate(15, 10)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  REFLECTOR MAGNIFICATION (M)
                </text>
                <text x="0" y="26" fill="#facc15" fontSize="12" fontWeight="bold" fontFamily="monospace">
                  {magnificationReflector}x (f_o / f_e = 1200 / 20)
                </text>
              </g>

              {/* Meter 2: Refractor Magnification */}
              <g transform="translate(190, 10)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  REFRACTOR MAGNIFICATION (M)
                </text>
                <text x="0" y="26" fill="#38bdf8" fontSize="12" fontWeight="bold" fontFamily="monospace">
                  {magnificationRefractor}x (f_o / f_e = 800 / 20)
                </text>
              </g>

              {/* Meter 3: Chromatic Aberration Status */}
              <g transform="translate(365, 10)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  CHROMATIC ABERRATION
                </text>
                <text
                  x="0"
                  y="26"
                  fill={demonstrateDispersion ? '#f87171' : '#4ade80'}
                  fontSize="11"
                  fontWeight="bold"
                  fontFamily="monospace"
                >
                  {demonstrateDispersion ? 'DISPERSION DEFECT' : 'MIRROR: ZERO DEFECT'}
                </text>
              </g>
            </g>
          </g>
        )}

        {/* Dynamic Interactive Callouts Layer (Static exam mode only) */}
        {!isAlive && (
          <InteractiveCallouts
            pins={effectivePins}
            landmarks={landmarks}
            activePin={activePin}
            onSelectPin={onSelectPin}
          />
        )}
      </svg>
    </div>
  );
}
