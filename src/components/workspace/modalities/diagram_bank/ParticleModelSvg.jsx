import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import InteractiveCallouts from './InteractiveCallouts';
import {
  Atom,
  BookOpen,
  FileText,
  Sparkles,
  Play,
  Pause,
  RotateCcw,
  Gauge,
  Flame,
  Thermometer,
  Activity,
  Eye,
  TrendingUp,
  Maximize2,
  ChevronRight,
  Info,
} from 'lucide-react';

function circlePath(cx, cy, r) {
  return `M ${cx - r},${cy} a ${r},${r} 0 1,0 ${r * 2},0 a ${r},${r} 0 1,0 ${-r * 2},0 Z`;
}

function normalizeParticleModelView(rawView) {
  const v = String(rawView || 'textbook').toLowerCase().trim();
  if (v === 'exam' || v === 'exam_paper' || v === 'stipple') return 'exam';
  if (v === 'alive' || v === 'sim' || v === 'simulation') return 'alive';
  return 'textbook';
}

const VIEW_METADATA = {
  textbook: {
    label: 'Particle Model of Matter Master',
    Icon: BookOpen,
  },
  exam: {
    label: 'Examination Ink Stipple Line-Art',
    Icon: FileText,
  },
  alive: {
    label: 'Dynamic Kinetic Particle Simulation',
    Icon: Sparkles,
  },
};

// Phase states along the heating curve
const PHASES = [
  { id: 'solid', name: 'Solid (Ice)', temp: -15, desc: 'Tightly packed regular lattice vibrating in fixed positions' },
  { id: 'melting', name: 'Melting Plateau (0 °C)', temp: 0, desc: 'Latent heat breaks intermolecular lattice forces; temperature constant' },
  { id: 'liquid', name: 'Liquid (Water)', temp: 45, desc: 'Closely packed particles rolling and sliding past each other' },
  { id: 'boiling', name: 'Boiling Plateau (100 °C)', temp: 100, desc: 'Latent heat overcomes remaining attractive forces; vaporisation' },
  { id: 'gas', name: 'Gas (Steam)', temp: 130, desc: 'Widely separated particles moving rapidly at high speeds in all directions' },
];

/**
 * Authentic Particle Model of Matter (Solid, Liquid, Gas & Phase Transitions) Schematic.
 * Aligned with South African Natural Sciences Grade 8 and Physical Sciences Grade 10.
 *
 * Implements Rule 0d-14 (The Heart Architecture Standard) & Dual Static/Alive Engine:
 * - Static Mode: Authentic unlabeled Textbook Master + NSC Exam Stipple plates in public/diagrams/
 * - Alive Mode: 60 FPS requestAnimationFrame dynamic kinetic simulation on the same 600x480 coordinate geometry
 * - Simulates Brownian motion, temperature-dependent vibrational amplitude, phase transitions, and gas collisions
 * - Telemetry HUD with temperature, average kinetic energy, pressure gauge, and intermolecular force meter
 * - Single locked view in question mode; multi-view toggle in Reference Atlas & SimuLearn
 */
export default function ParticleModelSvg({
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
  initialTemperature = 25,
}) {
  const initialView = normalizeParticleModelView(view || defaultView);
  const [activeView, setActiveView] = useState(initialView);
  const [isAlive, setIsAlive] = useState(initialView === 'alive');

  // Simulation controls
  const [isPlaying, setIsPlaying] = useState(true);
  const [playbackSpeed, setPlaybackSpeed] = useState(propPlaybackSpeed || 1.0);
  const [temperature, setTemperature] = useState(initialTemperature);
  const [activePhaseIndex, setActivePhaseIndex] = useState(2); // default liquid
  const [trackedParticleIndex, setTrackedParticleIndex] = useState(null);
  const [showHeatingCurveModal, setShowHeatingCurveModal] = useState(false);

  useEffect(() => {
    const v = normalizeParticleModelView(view || defaultView);
    setActiveView(v);
    setIsAlive(v === 'alive');
  }, [view, defaultView]);

  useEffect(() => {
    if (propPlaybackSpeed !== undefined) setPlaybackSpeed(propPlaybackSpeed);
  }, [propPlaybackSpeed]);

  // Normalize pins from modern contract or legacy labels
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
  // 60 FPS Alive Simulation Loop
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

  // Derived state physics
  const isSolid = temperature < 0;
  const isMelting = temperature === 0;
  const isLiquid = temperature > 0 && temperature < 100;
  const isBoiling = temperature === 100;
  const isGas = temperature > 100;

  // Sync temperature from phase selection
  const handleSelectPhase = (phaseIdx) => {
    setActivePhaseIndex(phaseIdx);
    setTemperature(PHASES[phaseIdx].temp);
  };

  // Scientific HUD parameters
  const kelvin = Math.max(1, temperature + 273.15);
  // Average Kinetic Energy (proportional to Kelvin temperature: E_k = 3/2 k_B T)
  const avgKineticEnergy = (0.0129 * (kelvin / 298.15)).toFixed(3); // in eV
  // Pressure (proportional to T / V in Gas, low in liquid/solid)
  const pressureKPa = isGas ? (101.3 * (kelvin / 373.15)).toFixed(1) : (101.3).toFixed(1);
  const imfStrength = isSolid ? 'Strong (Rigid)' : isLiquid ? 'Moderate (Fluid)' : 'Negligible (Free)';

  // ---------------------------------------------------------------------------
  // 3-Chamber Particle Physics Coordinates
  // Solid (x: 50..210, y: 150..370)
  // Liquid (x: 220..380, y: 150..370)
  // Gas (x: 390..550, y: 150..370)
  // ---------------------------------------------------------------------------

  // 1. Solid Lattice (4x4 = 16 particles in fixed equilibrium positions vibrating)
  const solidParticles = useMemo(() => {
    const list = [];
    const originX = 75;
    const originY = 220;
    const spacing = 34;
    const vibAmp = isSolid ? Math.min(6, 1.5 + (temperature + 40) * 0.08) : 1.2;

    for (let r = 0; r < 4; r++) {
      for (let c = 0; c < 4; c++) {
        const idx = r * 4 + c;
        const eqX = originX + c * spacing;
        const eqY = originY + r * spacing;

        // Harmonic thermal jitter based on particle frequency and simTime
        const freqX = 12 + (idx % 5) * 2;
        const freqY = 14 + (idx % 3) * 3;
        const dx = Math.sin(simTime * freqX + idx) * vibAmp;
        const dy = Math.cos(simTime * freqY + idx) * vibAmp;

        list.push({
          id: `solid_${idx}`,
          index: idx,
          x: eqX + dx,
          y: eqY + dy,
          eqX,
          eqY,
          r: 10,
        });
      }
    }
    return list;
  }, [simTime, temperature, isSolid]);

  // 2. Liquid Particles (16 particles moving fluidly in the bottom half of center container)
  const liquidParticles = useMemo(() => {
    const list = [];
    const originX = 245;
    const originY = 250;
    const width = 110;
    const height = 95;
    const speedMultiplier = isLiquid ? 1.0 + (temperature / 100) * 1.5 : 0.8;

    for (let i = 0; i < 16; i++) {
      // Deterministic pseudo-random Lissajous trajectory for rolling fluid motion
      const p1 = 0.8 + (i % 7) * 0.3;
      const p2 = 1.1 + (i % 5) * 0.4;
      const baseX = originX + ((i % 4) * 28 + 14);
      const baseY = originY + (Math.floor(i / 4) * 24 + 12);

      const dx = Math.sin(simTime * p1 * speedMultiplier + i * 1.3) * 16;
      const dy = Math.cos(simTime * p2 * speedMultiplier + i * 1.7) * 12;

      const px = Math.max(originX + 12, Math.min(originX + width - 12, baseX + dx));
      const py = Math.max(originY + 12, Math.min(originY + height - 12, baseY + dy));

      list.push({
        id: `liq_${i}`,
        index: i,
        x: px,
        y: py,
        r: 10,
      });
    }
    return list;
  }, [simTime, temperature, isLiquid]);

  // 3. Gas Particles (10 particles moving rapidly in 390..550 x, 170..370 y bouncing elastically)
  const gasParticles = useMemo(() => {
    const list = [];
    const minX = 415;
    const maxX = 535;
    const minY = 185;
    const maxY = 345;
    const speed = isGas ? 60 + (temperature - 100) * 1.2 : 45;

    for (let i = 0; i < 10; i++) {
      // Linear bouncy path with angle based on index
      const angle = (i * 36 + 15) * (Math.PI / 180);
      const vx = Math.cos(angle) * speed;
      const vy = Math.sin(angle) * speed;

      // Triangle wave reflection
      const spanX = maxX - minX;
      const spanY = maxY - minY;
      const rawX = (minX + (simTime * vx + i * 50) % (spanX * 2) + spanX * 2) % (spanX * 2);
      const rawY = (minY + (simTime * vy + i * 40) % (spanY * 2) + spanY * 2) % (spanY * 2);

      const px = rawX > spanX ? maxX - (rawX - spanX) : minX + rawX;
      const py = rawY > spanY ? maxY - (rawY - spanY) : minY + rawY;

      list.push({
        id: `gas_${i}`,
        index: i,
        x: px,
        y: py,
        vx: rawX > spanX ? -vx : vx,
        vy: rawY > spanY ? -vy : vy,
        r: 9,
      });
    }
    return list;
  }, [simTime, temperature, isGas]);

  return (
    <div
      data-testid="particle-model-root"
      className="flex flex-col items-center w-full max-w-2xl select-none space-y-2 font-sans"
    >
      {/* Header Bar */}
      {allowViewSwitch ? (
        <div className="flex items-center justify-between w-full px-2 py-1 bg-slate-50 border border-slate-200 rounded-xl text-xs">
          <span className="text-[11px] font-bold text-slate-600 uppercase tracking-wide flex items-center gap-1.5 font-mono">
            <Atom className="w-3.5 h-3.5 text-indigo-600" />
            Particle Model Engine:
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
          data-testid="particle-model-locked-view-badge"
          className="flex items-center justify-between w-full px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs"
        >
          <span className="text-[11px] font-bold text-slate-700 flex items-center gap-1.5 font-mono">
            <CurrentViewIcon className="w-3.5 h-3.5 text-indigo-600" />
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
              {gradeMask === 'g10' ? 'Physical Sciences Gr10' : 'Natural Sciences Gr8'}
            </span>
          </div>
        </div>
      )}

      {/* Backward-compatibility badge testids */}
      <span data-testid="particle_model-locked-view-badge" className="sr-only">Locked View</span>

      {/* Simulation Interactive Control Bar (Alive mode only) */}
      {isAlive && showSimControls && (
        <div
          data-testid="particle-sim-controls"
          className="flex flex-wrap items-center justify-between w-full p-2.5 bg-slate-900 text-white rounded-xl text-xs gap-2 shadow-md border border-slate-800 font-sans"
        >
          {/* Play/Pause & Speed */}
          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-play-pause-sim"
              onClick={() => setIsPlaying((p) => !p)}
              className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-400 cursor-pointer transition"
              title={isPlaying ? 'Pause Simulation' : 'Play Simulation'}
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

          {/* Phase Stepper Buttons */}
          <div className="flex items-center gap-1 overflow-x-auto py-0.5">
            {PHASES.map((ph, idx) => (
              <button
                key={ph.id}
                type="button"
                data-testid={`btn-phase-${ph.id}`}
                onClick={() => handleSelectPhase(idx)}
                className={`px-2 py-1 rounded-md text-[10px] font-bold font-mono transition cursor-pointer ${
                  activePhaseIndex === idx
                    ? 'bg-amber-500 text-slate-950 shadow-xs'
                    : 'bg-slate-800 text-slate-400 hover:text-white'
                }`}
              >
                {ph.name.split(' ')[0]}
              </button>
            ))}
          </div>

          {/* Secondary Actions */}
          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-follow-particle"
              onClick={() => setTrackedParticleIndex((prev) => (prev === null ? 0 : null))}
              className={`px-2 py-1 rounded-md text-[10px] font-bold font-mono transition cursor-pointer flex items-center gap-1 ${
                trackedParticleIndex !== null
                  ? 'bg-indigo-600 text-white'
                  : 'bg-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              <Eye className="w-3 h-3" />
              <span>{trackedParticleIndex !== null ? 'Tracking P#1' : 'Track P#1'}</span>
            </button>
            <button
              type="button"
              data-testid="btn-zoom-heating-curve"
              onClick={() => setShowHeatingCurveModal((m) => !m)}
              className="px-2 py-1 rounded-md text-[10px] font-bold font-mono transition cursor-pointer flex items-center gap-1 bg-slate-800 text-emerald-400 hover:bg-slate-700 border border-emerald-900/50"
            >
              <TrendingUp className="w-3 h-3" />
              <span>Heating Curve</span>
            </button>
          </div>
        </div>
      )}

      {/* Primary SVG Canvas */}
      <svg
        viewBox={viewBox}
        data-testid="particle-model-canvas"
        className="w-full h-auto drop-shadow-sm bg-white rounded-xl border border-slate-100 transition-all duration-300"
        style={{ minWidth: '320px', maxHeight: '520px' }}
      >
        <defs>
          {/* Radial gradient for realistic spherical atoms */}
          <radialGradient id="sphereSolidGrad" cx="35%" cy="35%" r="65%">
            <stop offset="0%" stopColor="#93c5fd" />
            <stop offset="45%" stopColor="#3b82f6" />
            <stop offset="90%" stopColor="#1d4ed8" />
            <stop offset="100%" stopColor="#1e3a8a" />
          </radialGradient>

          <radialGradient id="sphereLiquidGrad" cx="35%" cy="35%" r="65%">
            <stop offset="0%" stopColor="#67e8f9" />
            <stop offset="45%" stopColor="#06b6d4" />
            <stop offset="90%" stopColor="#0e7490" />
            <stop offset="100%" stopColor="#164e63" />
          </radialGradient>

          <radialGradient id="sphereGasGrad" cx="35%" cy="35%" r="65%">
            <stop offset="0%" stopColor="#fca5a5" />
            <stop offset="45%" stopColor="#ef4444" />
            <stop offset="90%" stopColor="#b91c1c" />
            <stop offset="100%" stopColor="#7f1d1d" />
          </radialGradient>

          <filter id="particleGlow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="3" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
          </filter>
        </defs>

        {/* ==================================================================== */}
        {/* MODE 1: STATIC EXAM PLATES                                            */}
        {/* ==================================================================== */}
        {!isAlive && activeView === 'textbook' && (
          <g id="view_textbook_master">
            <image
              href="/diagrams/particle_model_textbook.jpg"
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
              href="/diagrams/particle_model_exam_stipple.jpg"
              x="20"
              y="0"
              width="560"
              height="480"
              preserveAspectRatio="xMidYMid meet"
              className="select-none pointer-events-none"
            />
          </g>
        )}

        {/* ==================================================================== */}
        {/* MODE 2: ALIVE DYNAMIC 60 FPS SIMULATION OVERLAY                      */}
        {/* ==================================================================== */}
        {isAlive && (
          <g id="alive_kinetic_simulation" data-testid="alive-kinetic-simulation">
            {/* Background container outlines representing 3 states */}
            {/* Chamber 1: SOLID Container */}
            <rect
              x="55"
              y="160"
              width="155"
              height="200"
              rx="12"
              fill="#eff6ff"
              stroke="#93c5fd"
              strokeWidth="2"
              strokeDasharray={isSolid ? 'none' : '4 4'}
              opacity={isSolid ? 1 : 0.6}
            />
            <text x="132" y="185" textAnchor="middle" fill="#1e40af" fontSize="12" fontWeight="bold">
              SOLID (Fixed Lattice)
            </text>

            {/* Chamber 2: LIQUID Container */}
            <rect
              x="225"
              y="160"
              width="155"
              height="200"
              rx="12"
              fill="#ecfeff"
              stroke="#67e8f9"
              strokeWidth="2"
              strokeDasharray={isLiquid ? 'none' : '4 4'}
              opacity={isLiquid ? 1 : 0.6}
            />
            {/* Liquid Meniscus Wave */}
            <path
              d={`M 226,245 Q 265,${243 + Math.sin(simTime * 3) * 3} 302,245 T 379,245 L 379,358 Q 379,360 377,360 L 228,360 Q 226,360 226,358 Z`}
              fill="#cffafe"
              opacity="0.5"
            />
            <text x="302" y="185" textAnchor="middle" fill="#0e7490" fontSize="12" fontWeight="bold">
              LIQUID (Fluid Close)
            </text>

            {/* Chamber 3: GAS Container */}
            <rect
              x="395"
              y="160"
              width="155"
              height="200"
              rx="12"
              fill="#fff1f2"
              stroke="#fca5a5"
              strokeWidth="2"
              strokeDasharray={isGas ? 'none' : '4 4'}
              opacity={isGas ? 1 : 0.6}
            />
            <text x="472" y="185" textAnchor="middle" fill="#991b1b" fontSize="12" fontWeight="bold">
              GAS (Free Random)
            </text>

            {/* Inter-Chamber Phase Transition Arrows */}
            {/* Solid -> Liquid (Melting) */}
            <path d="M 180,140 L 250,140" stroke="#f59e0b" strokeWidth="2.5" markerEnd="url(#arrowGold)" />
            <text x="215" y="132" textAnchor="middle" fill="#b45309" fontSize="10" fontWeight="bold">
              Melting (+Heat)
            </text>

            {/* Liquid -> Gas (Boiling) */}
            <path d="M 350,140 L 420,140" stroke="#ef4444" strokeWidth="2.5" markerEnd="url(#arrowRed)" />
            <text x="385" y="132" textAnchor="middle" fill="#b91c1c" fontSize="10" fontWeight="bold">
              Boiling (+Heat)
            </text>

            {/* Reverse Condensation / Freezing */}
            <path d="M 420,380 L 350,380" stroke="#3b82f6" strokeWidth="2" strokeDasharray="3 3" />
            <text x="385" y="394" textAnchor="middle" fill="#1d4ed8" fontSize="9" fontWeight="bold">
              Condensation (-Heat)
            </text>
            <path d="M 250,380 L 180,380" stroke="#3b82f6" strokeWidth="2" strokeDasharray="3 3" />
            <text x="215" y="394" textAnchor="middle" fill="#1d4ed8" fontSize="9" fontWeight="bold">
              Freezing (-Heat)
            </text>

            {/* Solid Lattice Intermolecular Springs */}
            <g id="lattice_springs">
              {solidParticles.map((p, idx) => {
                const rightP = (idx % 4 < 3) ? solidParticles[idx + 1] : null;
                const bottomP = (idx < 12) ? solidParticles[idx + 4] : null;
                return (
                  <g key={`spring_${idx}`}>
                    {rightP && (
                      <line
                        x1={p.x}
                        y1={p.y}
                        x2={rightP.x}
                        y2={rightP.y}
                        stroke="#93c5fd"
                        strokeWidth="1.5"
                        strokeDasharray="2 2"
                      />
                    )}
                    {bottomP && (
                      <line
                        x1={p.x}
                        y1={p.y}
                        x2={bottomP.x}
                        y2={bottomP.y}
                        stroke="#93c5fd"
                        strokeWidth="1.5"
                        strokeDasharray="2 2"
                      />
                    )}
                  </g>
                );
              })}
            </g>

            {/* 1. Solid Particles Render */}
            <g id="solid_particles">
              {solidParticles.map((p) => {
                const isTracked = trackedParticleIndex === p.index;
                return (
                  <g key={p.id}>
                    {isTracked && (
                      <path
                        d={circlePath(p.x, p.y, p.r + 5)}
                        fill="none"
                        stroke="#f59e0b"
                        strokeWidth="2.5"
                        filter="url(#particleGlow)"
                      />
                    )}
                    <path
                      d={circlePath(p.x, p.y, p.r)}
                      fill="url(#sphereSolidGrad)"
                      stroke="#1e3a8a"
                      strokeWidth="1"
                    />
                  </g>
                );
              })}
            </g>

            {/* 2. Liquid Particles Render */}
            <g id="liquid_particles">
              {liquidParticles.map((p) => {
                return (
                  <path
                    key={p.id}
                    d={circlePath(p.x, p.y, p.r)}
                    fill="url(#sphereLiquidGrad)"
                    stroke="#164e63"
                    strokeWidth="1"
                  />
                );
              })}
            </g>

            {/* 3. Gas Particles Render with Velocity Vectors */}
            <g id="gas_particles">
              {gasParticles.map((p) => {
                const vecLen = 14;
                const speedMag = Math.sqrt(p.vx * p.vx + p.vy * p.vy) || 1;
                const ux = (p.vx / speedMag) * vecLen;
                const uy = (p.vy / speedMag) * vecLen;

                return (
                  <g key={p.id}>
                    {/* Velocity vector line */}
                    <line
                      x1={p.x}
                      y1={p.y}
                      x2={p.x + ux}
                      y2={p.y + uy}
                      stroke="#ef4444"
                      strokeWidth="1.5"
                    />
                    <path
                      d={circlePath(p.x + ux, p.y + uy, 1.8)}
                      fill="#ef4444"
                    />
                    <path
                      d={circlePath(p.x, p.y, p.r)}
                      fill="url(#sphereGasGrad)"
                      stroke="#7f1d1d"
                      strokeWidth="1"
                    />
                  </g>
                );
              })}
            </g>

            {/* ================================================================ */}
            {/* SCIENTIFIC HUD METERS PANEL (bottom of viewBox)                  */}
            {/* ================================================================ */}
            <g id="hud_telemetry_panel" transform="translate(45, 410)">
              <rect
                x="0"
                y="0"
                width="510"
                height="58"
                rx="10"
                fill="#0f172a"
                stroke="#334155"
                strokeWidth="1.5"
              />

              {/* Meter 1: Temperature */}
              <g transform="translate(15, 12)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  TEMPERATURE (T)
                </text>
                <text x="0" y="28" fill="#f8fafc" fontSize="13" fontWeight="bold" fontFamily="monospace">
                  {temperature} °C ({kelvin.toFixed(1)} K)
                </text>
              </g>

              {/* Meter 2: Average Kinetic Energy */}
              <g transform="translate(155, 12)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  AVG KINETIC ENERGY (Ēₖ)
                </text>
                <text x="0" y="28" fill="#38bdf8" fontSize="13" fontWeight="bold" fontFamily="monospace">
                  {avgKineticEnergy} eV (∝ T)
                </text>
              </g>

              {/* Meter 3: Pressure */}
              <g transform="translate(295, 12)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  PRESSURE (P)
                </text>
                <text x="0" y="28" fill="#facc15" fontSize="13" fontWeight="bold" fontFamily="monospace">
                  {pressureKPa} kPa
                </text>
              </g>

              {/* Meter 4: Intermolecular Force */}
              <g transform="translate(405, 12)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  INTERMOLECULAR FORCES
                </text>
                <text x="0" y="28" fill="#4ade80" fontSize="11" fontWeight="bold" fontFamily="monospace">
                  {imfStrength}
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

      {/* Macroscopic Heating Curve Dialog Modal */}
      {showHeatingCurveModal && (
        <div
          data-testid="modal-heating-curve"
          className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/70 backdrop-blur-xs p-4"
        >
          <div className="bg-white rounded-2xl max-w-xl w-full p-5 shadow-2xl border border-slate-200 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <div className="flex items-center gap-2">
                <span className="w-7 h-7 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">
                  <TrendingUp className="w-4 h-4" />
                </span>
                <div>
                  <h4 className="text-sm font-bold text-slate-900">
                    Heating Curve of Water & Latent Heat Plateaus
                  </h4>
                  <p className="text-[11px] text-slate-500 font-mono">
                    Phase transitions at 0 °C (Melting) & 100 °C (Boiling)
                  </p>
                </div>
              </div>
              <button
                type="button"
                data-testid="btn-close-heating-curve"
                onClick={() => setShowHeatingCurveModal(false)}
                className="text-slate-400 hover:text-slate-700 text-sm font-bold p-1 cursor-pointer"
              >
                ✕
              </button>
            </div>

            {/* Heating Curve SVG Diagram */}
            <svg viewBox="0 0 500 240" className="w-full h-auto bg-slate-50 rounded-xl border border-slate-200">
              {/* Axes */}
              <line x1="60" y1="20" x2="60" y2="200" stroke="#64748b" strokeWidth="2" />
              <line x1="60" y1="200" x2="480" y2="200" stroke="#64748b" strokeWidth="2" />
              <text x="30" y="25" fill="#475569" fontSize="10" fontWeight="bold">T (°C)</text>
              <text x="440" y="218" fill="#475569" fontSize="10" fontWeight="bold">Time (t)</text>

              {/* Temperature mark lines */}
              <line x1="55" y1="160" x2="480" y2="160" stroke="#cbd5e1" strokeDasharray="3 3" />
              <text x="32" y="164" fill="#64748b" fontSize="10" fontWeight="bold">0 °C</text>

              <line x1="55" y1="80" x2="480" y2="80" stroke="#cbd5e1" strokeDasharray="3 3" />
              <text x="22" y="84" fill="#64748b" fontSize="10" fontWeight="bold">100 °C</text>

              {/* Heating Curve Polyline */}
              {/* Solid warming: (60, 190) -> (110, 160) */}
              <line x1="60" y1="190" x2="110" y2="160" stroke="#3b82f6" strokeWidth="3" />
              <text x="75" y="185" fill="#1e40af" fontSize="9" fontWeight="bold">Solid</text>

              {/* Melting Plateau: (110, 160) -> (190, 160) */}
              <line x1="110" y1="160" x2="190" y2="160" stroke="#f59e0b" strokeWidth="4" />
              <text x="125" y="152" fill="#b45309" fontSize="9" fontWeight="bold">Melting (0 °C)</text>

              {/* Liquid warming: (190, 160) -> (280, 80) */}
              <line x1="190" y1="160" x2="280" y2="80" stroke="#06b6d4" strokeWidth="3" />
              <text x="220" y="125" fill="#0e7490" fontSize="9" fontWeight="bold">Liquid</text>

              {/* Boiling Plateau: (280, 80) -> (390, 80) */}
              <line x1="280" y1="80" x2="390" y2="80" stroke="#ef4444" strokeWidth="4" />
              <text x="305" y="72" fill="#b91c1c" fontSize="9" fontWeight="bold">Boiling (100 °C)</text>

              {/* Gas warming: (390, 80) -> (460, 30) */}
              <line x1="390" y1="80" x2="460" y2="30" stroke="#dc2626" strokeWidth="3" />
              <text x="425" y="50" fill="#991b1b" fontSize="9" fontWeight="bold">Gas</text>

              {/* Current Temperature Indicator Indicator Dot */}
              {(() => {
                let curX = 150;
                let curY = 160;
                if (temperature < 0) {
                  curX = 60 + ((temperature + 20) / 20) * 50;
                  curY = 190 - ((temperature + 20) / 20) * 30;
                } else if (temperature === 0) {
                  curX = 150;
                  curY = 160;
                } else if (temperature < 100) {
                  curX = 190 + (temperature / 100) * 90;
                  curY = 160 - (temperature / 100) * 80;
                } else if (temperature === 100) {
                  curX = 335;
                  curY = 80;
                } else {
                  curX = 390 + ((temperature - 100) / 40) * 70;
                  curY = 80 - ((temperature - 100) / 40) * 50;
                }
                return (
                  <g>
                    <path d={circlePath(curX, curY, 7)} fill="#f59e0b" filter="url(#particleGlow)" />
                    <path d={circlePath(curX, curY, 4)} fill="#ffffff" />
                  </g>
                );
              })()}
            </svg>

            {/* Scientific Explanation */}
            <div className="p-3 bg-amber-50 rounded-xl border border-amber-200 text-xs text-amber-900 space-y-1">
              <span className="font-bold">Pedagogical Principle (Latent Heat):</span>
              <p>
                During phase changes (Melting at 0 °C and Boiling at 100 °C), the temperature remains constant even
                though heat energy is continuously added. The thermal energy is absorbed as latent heat to break
                intermolecular electrostatic bonds between particles, rather than increasing their average kinetic energy.
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
