import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import InteractiveCallouts from './InteractiveCallouts';
import {
  Wind,
  BookOpen,
  FileText,
  Play,
  Pause,
  RotateCcw,
  Sparkles,
  Activity,
  Layers,
  ZoomIn,
  ZoomOut,
  Eye,
} from 'lucide-react';

function circlePath(cx, cy, r) {
  return `M ${cx - r},${cy} a ${r},${r} 0 1,0 ${r * 2},0 a ${r},${r} 0 1,0 ${-r * 2},0 Z`;
}

function ellipsePath(cx, cy, rx, ry) {
  return `M ${cx - rx},${cy} a ${rx},${ry} 0 1,0 ${rx * 2},0 a ${rx},${ry} 0 1,0 ${-rx * 2},0 Z`;
}

function normalizeAlveolusView(rawView) {
  const v = String(rawView || 'textbook').toLowerCase().trim();
  if (v === 'exam' || v === 'exam_paper' || v === 'stipple') return 'exam';
  return 'textbook';
}

const VIEW_METADATA = {
  textbook: {
    label: 'Pulmonary Alveolus & Capillary Diffusion Cross-Section',
    Icon: BookOpen,
  },
  exam: {
    label: 'Examination Ink Stipple Line-Art',
    Icon: FileText,
  },
};

const PHASES = [
  {
    id: 'ventilation',
    title: '1. Inhalation (Ventilation)',
    desc: 'Fresh atmospheric air fills alveolar lumen (pO2 = 104 mmHg, pCO2 = 40 mmHg).',
    color: '#0284c7',
  },
  {
    id: 'perfusion',
    title: '2. Capillary Inflow (Perfusion)',
    desc: 'Deoxygenated blood arrives from pulmonary artery (pO2 = 40 mmHg, pCO2 = 45 mmHg).',
    color: '#3b82f6',
  },
  {
    id: 'diffusion',
    title: '3. Passive Gas Diffusion',
    desc: 'O2 diffuses into RBCs; CO2 diffuses into alveolar space across 0.5 µm membrane.',
    color: '#8b5cf6',
  },
  {
    id: 'oxygenation',
    title: '4. Oxygenated Outflow',
    desc: 'Oxygenated blood (pO2 = 100 mmHg, 98% Hb-O2) flows to left atrium via pulmonary vein.',
    color: '#ef4444',
  },
];

/**
 * Authentic Human Gaseous Exchange Alveolus & Pulmonary Capillary Diffusion.
 * Merges Static Exam Mode (Heart Architecture standard) and Alive Understanding Mode (60 FPS Simulation).
 *
 * Implements Rule 0d-14 (The Heart Architecture Standard) & Phase 4 Dual-Mode Merge:
 * - Static Mode: Authentic unlabeled Textbook Master + NSC Exam Stipple plates in public/diagrams/ with InteractiveCallouts.
 * - Alive Mode: 60 FPS animated RBC capillary transit, O2 & CO2 concentration gradient particle diffusion,
 *   step scrubber, speed controls, single-RBC tracking mode, and macroscopic cardiopulmonary loop zoom.
 */
export default function AlveolusGasExchangeSvg({
  pins = [],
  landmarks = [],
  labels = [],
  activePin,
  onSelectPin,
  viewBox = '0 0 600 480',
  gradeMask = 'g11',
  view,
  defaultView = 'textbook',
  allowViewSwitch = false,
  state = 'static',
  mode: propMode,
  phase: propPhase,
  isPlaying: propIsPlaying,
  playbackSpeed: propPlaybackSpeed = 1,
}) {
  const initialView = normalizeAlveolusView(view || defaultView);
  const [activeView, setActiveView] = useState(initialView);

  // Dual-mode state: 'static' (exam plate with pins) or 'alive' (simulation)
  const isExternalAlive = propMode === 'alive' || (state && state !== 'static');
  const [internalAlive, setInternalAlive] = useState(false);
  const isAlive = propMode !== undefined ? propMode === 'alive' : (isExternalAlive || internalAlive);

  // Simulation controls
  const [isPlaying, setIsPlaying] = useState(propIsPlaying !== undefined ? propIsPlaying : true);
  const [playbackSpeed, setPlaybackSpeed] = useState(propPlaybackSpeed || 1);
  const [activePhaseIndex, setActivePhaseIndex] = useState(0);
  const [followRbc, setFollowRbc] = useState(false);
  const [isMacroscopic, setIsMacroscopic] = useState(false);

  // Sync prop changes
  useEffect(() => {
    setActiveView(normalizeAlveolusView(view || defaultView));
  }, [view, defaultView]);

  useEffect(() => {
    if (propPhase) {
      const idx = PHASES.findIndex((p) => p.id === propPhase);
      if (idx !== -1) setActivePhaseIndex(idx);
    }
  }, [propPhase]);

  useEffect(() => {
    if (propIsPlaying !== undefined) setIsPlaying(propIsPlaying);
  }, [propIsPlaying]);

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

  const currentMeta = VIEW_METADATA[activeView] || VIEW_METADATA.textbook;
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

  // Capillary Parametric Trajectory Spline (x, y as a function of t: 0 -> 1)
  // Curves around the alveolus from pulmonary arteriole (bottom) to pulmonary venule (top)
  const getCapillaryPoint = useCallback((t) => {
    // Clamp t to [0, 1]
    const u = Math.max(0, Math.min(1, t));
    // Bézier curve control points: P0(475, 430) -> P1(430, 310) -> P2(415, 210) -> P3(455, 60)
    const p0 = { x: 475, y: 430 };
    const p1 = { x: 428, y: 310 };
    const p2 = { x: 418, y: 210 };
    const p3 = { x: 455, y: 60 };

    const inv = 1 - u;
    const x =
      inv * inv * inv * p0.x +
      3 * inv * inv * u * p1.x +
      3 * inv * u * u * p2.x +
      u * u * u * p3.x;
    const y =
      inv * inv * inv * p0.y +
      3 * inv * inv * u * p1.y +
      3 * inv * u * u * p2.y +
      u * u * u * p3.y;

    // Tangent angle for orienting the biconcave erythrocyte disc
    const dx =
      3 * inv * inv * (p1.x - p0.x) +
      6 * inv * u * (p2.x - p1.x) +
      3 * u * u * (p3.x - p2.x);
    const dy =
      3 * inv * inv * (p1.y - p0.y) +
      6 * inv * u * (p2.y - p1.y) +
      3 * u * u * (p3.y - p2.y);
    const angleDeg = (Math.atan2(dy, dx) * 180) / Math.PI;

    return { x, y, angleDeg, progress: u };
  }, []);

  // Compute 7 Red Blood Cells flowing along the capillary
  const RBC_COUNT = 7;
  const rbcs = useMemo(() => {
    const cells = [];
    const cycleDuration = 7.0; // seconds for one cell to traverse the capillary
    for (let i = 0; i < RBC_COUNT; i++) {
      const phaseOffset = i / RBC_COUNT;
      const progress = ((simTime / cycleDuration + phaseOffset) % 1 + 1) % 1;
      const pt = getCapillaryPoint(progress);

      // Oxygen saturation curve along the capillary:
      // Inflow: 75% Hb-O2 (pO2 = 40)
      // Rapid diffusion across mid-capillary (progress 0.25 -> 0.75)
      // Outflow: 98% Hb-O2 (pO2 = 100)
      const sigmoid = 1 / (1 + Math.exp(-10 * (progress - 0.45)));
      const saturation = 0.75 + 0.23 * sigmoid;
      const pO2 = 40 + 60 * sigmoid;

      // Color interpolation: deoxygenated blue-purple -> oxygenated bright crimson
      // Blue: rgb(43, 91, 132), Red: rgb(220, 38, 38)
      const r = Math.round(43 + (220 - 43) * sigmoid);
      const g = Math.round(91 + (38 - 91) * sigmoid);
      const b = Math.round(132 + (38 - 132) * sigmoid);
      const color = `rgb(${r}, ${g}, ${b})`;
      const glowColor = `rgba(${r}, ${g}, ${b}, 0.55)`;

      cells.push({
        id: `rbc-${i}`,
        index: i,
        x: pt.x,
        y: pt.y,
        angleDeg: pt.angleDeg,
        progress,
        saturation,
        pO2,
        color,
        glowColor,
        isFollowed: i === 2, // RBC #2 is the designated telemetry tracking cell
      });
    }
    return cells;
  }, [simTime, getCapillaryPoint]);

  // Compute 16 Oxygen (O2) diffusing particles from Alveolar Lumen into Capillary
  const O2_PARTICLE_COUNT = 16;
  const o2Particles = useMemo(() => {
    const list = [];
    for (let i = 0; i < O2_PARTICLE_COUNT; i++) {
      const seed = i * 137.5;
      const localTime = (simTime * 0.7 + i * 0.4) % 3.0; // 3-second diffusion lifetime
      const progress = localTime / 3.0;

      // Start in Alveolar space (x: 270-320, y: 190-270)
      const startX = 280 + Math.sin(seed) * 35;
      const startY = 230 + Math.cos(seed) * 50;

      // Target capillary wall (x: 410-430, y: 170-300)
      const targetX = 422;
      const targetY = 170 + ((seed * 11) % 140);

      const curX = startX + (targetX - startX) * progress;
      const curY = startY + (targetY - startY) * progress + Math.sin(simTime * 4 + i) * 3;
      const opacity = progress < 0.1 ? progress * 10 : progress > 0.85 ? (1 - progress) / 0.15 : 1;

      list.push({
        id: `o2-${i}`,
        x: curX,
        y: curY,
        opacity,
      });
    }
    return list;
  }, [simTime]);

  // Compute 12 Carbon Dioxide (CO2) diffusing particles from Capillary into Alveolar Lumen
  const CO2_PARTICLE_COUNT = 12;
  const co2Particles = useMemo(() => {
    const list = [];
    for (let i = 0; i < CO2_PARTICLE_COUNT; i++) {
      const seed = i * 223.7;
      const localTime = (simTime * 0.6 + i * 0.5) % 3.2;
      const progress = localTime / 3.2;

      // Start near capillary wall
      const startX = 426;
      const startY = 160 + ((seed * 7) % 150);

      // Diffuse inward to Alveolar space (x: 280-310, y: 180-260)
      const targetX = 295 + Math.sin(seed * 2) * 30;
      const targetY = 220 + Math.cos(seed * 3) * 45;

      const curX = startX + (targetX - startX) * progress;
      const curY = startY + (targetY - startY) * progress + Math.cos(simTime * 3.5 + i) * 3;
      const opacity = progress < 0.1 ? progress * 10 : progress > 0.85 ? (1 - progress) / 0.15 : 0.95;

      list.push({
        id: `co2-${i}`,
        x: curX,
        y: curY,
        opacity,
      });
    }
    return list;
  }, [simTime]);

  // Tracked RBC metrics
  const trackedRbc = rbcs.find((c) => c.isFollowed) || rbcs[0];

  return (
    <div
      data-testid="alveolus-root"
      className="flex flex-col items-center w-full max-w-2xl select-none space-y-2 font-sans"
    >
      {/* --------------------------------------------------------------------- */}
      {/* HEADER CONTROL BAR: Static / Alive Mode Toggle & Controls             */}
      {/* --------------------------------------------------------------------- */}
      <div className="flex flex-col w-full gap-1.5">
        <div className="flex items-center justify-between w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs shadow-2xs">
          <div className="flex items-center gap-2">
            <span className="w-5 h-5 rounded-md bg-[#13519C] text-white flex items-center justify-center text-xs font-bold shadow-2xs">
              <Wind className="w-3.5 h-3.5" />
            </span>
            <span className="font-bold text-slate-800 tracking-tight text-[12px] sm:text-xs">
              {isAlive
                ? 'Dynamic Gaseous Exchange Simulation (Alive Mode)'
                : currentMeta.label}
            </span>
          </div>

          <div className="flex items-center gap-1.5">
            {/* Mode Switcher: Static vs. Alive */}
            {!isAlive ? (
              <button
                type="button"
                data-testid="btn-bring-to-life"
                onClick={() => setInternalAlive(true)}
                className="px-3 py-1 rounded-lg font-bold text-xs bg-emerald-600 hover:bg-emerald-700 text-white shadow-xs transition-all cursor-pointer flex items-center gap-1.5 animate-pulse"
                title="Bring this anatomical diagram to life with active capillary flow and gas diffusion"
              >
                <Sparkles className="w-3.5 h-3.5 text-amber-300" />
                <span>Bring It To Life</span>
              </button>
            ) : (
              <button
                type="button"
                data-testid="btn-back-to-exam"
                onClick={() => setInternalAlive(false)}
                className="px-2.5 py-1 rounded-lg font-bold text-[11px] bg-slate-200 hover:bg-slate-300 text-slate-800 transition-colors cursor-pointer flex items-center gap-1"
                title="Return to static examination diagram with callout pins"
              >
                <BookOpen className="w-3 h-3" />
                <span>Exam Plate</span>
              </button>
            )}

            {/* Static View Switcher (when in static mode and atlas allows) */}
            {!isAlive && allowViewSwitch && (
              <div className="flex gap-1 ml-1 border-l border-slate-200 pl-1.5">
                <button
                  type="button"
                  data-testid="btn-view-textbook"
                  onClick={() => setActiveView('textbook')}
                  className={`px-2 py-0.5 rounded font-bold text-[10px] transition cursor-pointer flex items-center gap-1 ${
                    activeView === 'textbook'
                      ? 'bg-[#13519C] text-white'
                      : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200'
                  }`}
                >
                  <BookOpen className="w-2.5 h-2.5" />
                  <span>Textbook</span>
                </button>
                <button
                  type="button"
                  data-testid="btn-view-exam"
                  onClick={() => setActiveView('exam')}
                  className={`px-2 py-0.5 rounded font-bold text-[10px] transition cursor-pointer flex items-center gap-1 ${
                    activeView === 'exam'
                      ? 'bg-[#13519C] text-white'
                      : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200'
                  }`}
                >
                  <FileText className="w-2.5 h-2.5" />
                  <span>Exam</span>
                </button>
              </div>
            )}
          </div>
        </div>

        {/* Alive Simulation Control Toolbar (Active in Alive Mode) */}
        {isAlive && (
          <div
            data-testid="alveolus-alive-controls"
            className="flex flex-wrap items-center justify-between w-full px-3 py-1.5 bg-slate-900 border border-slate-800 rounded-xl text-slate-200 text-xs gap-2 shadow-inner"
          >
            {/* Play/Pause & Speed */}
            <div className="flex items-center gap-2">
              <button
                type="button"
                data-testid="btn-play-pause-sim"
                onClick={() => setIsPlaying((p) => !p)}
                className="w-7 h-7 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white flex items-center justify-center font-bold transition cursor-pointer shadow-xs"
                title={isPlaying ? 'Pause simulation' : 'Play simulation'}
              >
                {isPlaying ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5 ml-0.5" />}
              </button>

              <button
                type="button"
                data-testid="btn-speed-toggle"
                onClick={() =>
                  setPlaybackSpeed((s) => (s === 1 ? 2 : s === 2 ? 0.5 : 1))
                }
                className="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 font-mono text-[11px] font-bold text-indigo-300 border border-slate-700 transition cursor-pointer"
                title="Toggle playback speed"
              >
                {playbackSpeed}x Speed
              </button>

              {/* Follow Single RBC Toggle */}
              <button
                type="button"
                data-testid="btn-follow-rbc"
                onClick={() => setFollowRbc((f) => !f)}
                className={`px-2 py-1 rounded text-[11px] font-bold transition cursor-pointer flex items-center gap-1 border ${
                  followRbc
                    ? 'bg-amber-500/20 text-amber-300 border-amber-400/50'
                    : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border-slate-700'
                }`}
                title="Lock tracking camera on an individual erythrocyte (RBC)"
              >
                <Eye className="w-3 h-3" />
                <span>Follow RBC</span>
              </button>

              {/* Macroscopic Cardiopulmonary Loop Toggle */}
              <button
                type="button"
                data-testid="btn-zoom-macro"
                onClick={() => setIsMacroscopic((m) => !m)}
                className={`px-2 py-1 rounded text-[11px] font-bold transition cursor-pointer flex items-center gap-1 border ${
                  isMacroscopic
                    ? 'bg-sky-500/20 text-sky-300 border-sky-400/50'
                    : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border-slate-700'
                }`}
                title="Toggle macroscopic cardiopulmonary loop hierarchy"
              >
                <Layers className="w-3 h-3" />
                <span>{isMacroscopic ? 'Micro Alveolus' : 'Macro Lungs'}</span>
              </button>
            </div>

            {/* Scientific Phase Stepper */}
            <div className="flex items-center gap-1 overflow-x-auto">
              {PHASES.map((ph, idx) => (
                <button
                  key={ph.id}
                  type="button"
                  data-testid={`btn-phase-${ph.id}`}
                  onClick={() => setActivePhaseIndex(idx)}
                  className={`px-2 py-0.5 rounded text-[10px] font-bold transition cursor-pointer whitespace-nowrap ${
                    activePhaseIndex === idx
                      ? 'bg-indigo-500 text-white shadow-2xs'
                      : 'bg-slate-800 hover:bg-slate-700 text-slate-400'
                  }`}
                >
                  Step {idx + 1}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* --------------------------------------------------------------------- */}
      {/* PRIMARY SVG CANVAS (600 x 480 Coordinates)                            */}
      {/* --------------------------------------------------------------------- */}
      <div
        data-testid="alveolus-alive-stage"
        className="relative w-full rounded-2xl overflow-hidden border border-slate-200 shadow-sm bg-white"
      >
        <svg
          viewBox={viewBox}
          data-testid="alveolus-gas-exchange-canvas"
          className="w-full h-auto drop-shadow-sm select-none transition-all duration-300"
          style={{ minWidth: '320px', maxHeight: '520px' }}
        >
          {/* ================================================================= */}
          {/* STATIC EXAM / TEXTBOOK PLATES                                     */}
          {/* ================================================================= */}
          {!isMacroscopic && (
            <>
              {activeView === 'textbook' && (
                <g id="view_textbook_master" opacity={isAlive ? 0.92 : 1}>
                  <image
                    href="/diagrams/alveolus_textbook.jpg"
                    x="50"
                    y="0"
                    width="500"
                    height="480"
                    preserveAspectRatio="xMidYMid meet"
                    className="select-none pointer-events-none"
                  />
                </g>
              )}

              {activeView === 'exam' && (
                <g id="view_exam_paper" opacity={isAlive ? 0.92 : 1}>
                  <image
                    href="/diagrams/alveolus_exam_stipple.jpg"
                    x="50"
                    y="0"
                    width="500"
                    height="480"
                    preserveAspectRatio="xMidYMid meet"
                    className="select-none pointer-events-none"
                  />
                </g>
              )}
            </>
          )}

          {/* ================================================================= */}
          {/* ALIVE SIMULATION OVERLAY: 60 FPS Capillary Flow & Diffusion       */}
          {/* ================================================================= */}
          {isAlive && !isMacroscopic && (
            <g id="alive_simulation_overlay">
              {/* Capillary Flow Track Guide (Subtle glowing flow pathway) */}
              <path
                d="M 475,430 C 428,310 418,210 455,60"
                fill="none"
                stroke="#60a5fa"
                strokeWidth="24"
                strokeOpacity="0.18"
                strokeLinecap="round"
              />

              {/* Animated O2 Diffusion Particles (Lumen -> Capillary RBCs) */}
              <g id="o2_diffusion_swarm">
                {o2Particles.map((p) => (
                  <g key={p.id} opacity={p.opacity}>
                    <path d={circlePath(p.x, p.y, 4.5)} fill="#f59e0b" filter="drop-shadow(0 0 3px #ef4444)" />
                    <path d={circlePath(p.x, p.y, 2)} fill="#ffffff" />
                  </g>
                ))}
              </g>

              {/* Animated CO2 Diffusion Particles (Capillary Plasma -> Lumen) */}
              <g id="co2_diffusion_swarm">
                {co2Particles.map((p) => (
                  <g key={p.id} opacity={p.opacity}>
                    <path d={circlePath(p.x, p.y, 4)} fill="#06b6d4" filter="drop-shadow(0 0 3px #2563eb)" />
                    <path d={circlePath(p.x, p.y, 1.8)} fill="#ffffff" />
                  </g>
                ))}
              </g>

              {/* Circulating Erythrocytes (Red Blood Cells) */}
              <g id="erythrocytes_capillary_stream">
                {rbcs.map((cell) => {
                  const isTracked = followRbc && cell.isFollowed;
                  return (
                    <g
                      key={cell.id}
                      transform={`translate(${cell.x}, ${cell.y}) rotate(${cell.angleDeg})`}
                    >
                      {/* Pulse halo if single-RBC tracking mode is active */}
                      {isTracked && (
                        <path
                          d={circlePath(0, 0, 18)}
                          fill="none"
                          stroke="#fbbf24"
                          strokeWidth="2.5"
                          strokeDasharray="4 2"
                          className="animate-spin"
                        />
                      )}

                      {/* Erythrocyte Biconcave Disc Shape */}
                      <path
                        d={ellipsePath(0, 0, 12, 7.5)}
                        fill={cell.color}
                        stroke="#ffffff"
                        strokeWidth="1.2"
                        filter="drop-shadow(0 1px 3px rgba(0,0,0,0.35))"
                      />
                      {/* Biconcave Central Dimple / Depression */}
                      <path
                        d={ellipsePath(0, 0, 5.5, 3.2)}
                        fill="#ffffff"
                        opacity={0.35}
                      />
                    </g>
                  );
                })}
              </g>

              {/* Follow-RBC Floating Telemetry Tag */}
              {followRbc && trackedRbc && (
                <g
                  transform={`translate(${trackedRbc.x + 18}, ${trackedRbc.y - 18})`}
                  className="pointer-events-none"
                >
                  <rect
                    x="0"
                    y="0"
                    width="130"
                    height="38"
                    rx="6"
                    fill="#0f172a"
                    fillOpacity="0.92"
                    stroke="#fbbf24"
                    strokeWidth="1.2"
                  />
                  <text x="8" y="15" fill="#fbbf24" fontSize="10" fontWeight="bold">
                    Target: RBC #2
                  </text>
                  <text x="8" y="28" fill="#f8fafc" fontSize="9.5" fontFamily="monospace">
                    Hb-O2: {(trackedRbc.saturation * 100).toFixed(0)}% • {trackedRbc.pO2.toFixed(0)} mmHg
                  </text>
                </g>
              )}

              {/* Diffusion Vector Labels */}
              <g id="diffusion_legend_markers" className="pointer-events-none">
                <rect x="230" y="220" width="46" height="20" rx="5" fill="#fef2f2" stroke="#dc2626" strokeWidth="1.2" />
                <text x="253" y="234" textAnchor="middle" fontSize="11" fontWeight="800" fill="#dc2626">
                  O2 ➔
                </text>

                <rect x="330" y="270" width="50" height="20" rx="5" fill="#eff6ff" stroke="#2563eb" strokeWidth="1.2" />
                <text x="355" y="284" textAnchor="middle" fontSize="11" fontWeight="800" fill="#1d4ed8">
                  ⬅ CO2
                </text>
              </g>
            </g>
          )}

          {/* ================================================================= */}
          {/* MACROSCOPIC SYSTEM CARDIOPULMONARY VIEW                          */}
          {/* ================================================================= */}
          {isAlive && isMacroscopic && (
            <g id="macroscopic_cardiopulmonary_loop">
              {/* Background Plate for Macroscopic View */}
              <rect x="0" y="0" width="600" height="480" fill="#0f172a" />

              {/* Title & Hierarchy Breadcrumbs */}
              <text x="300" y="35" textAnchor="middle" fill="#94a3b8" fontSize="11" fontWeight="bold" letterSpacing="1">
                RESPIRATORY &amp; CIRCULATORY SYSTEM INTEGRATION
              </text>
              <text x="300" y="55" textAnchor="middle" fill="#38bdf8" fontSize="14" fontWeight="bold">
                Pulmonary Circulatory Loop &amp; Bilateral Gas Exchange
              </text>

              {/* Trachea & Bronchi */}
              <path d="M 300,70 L 300,120" stroke="#cbd5e1" strokeWidth="12" strokeLinecap="round" />
              <path d="M 300,120 C 300,140 230,150 200,180" fill="none" stroke="#cbd5e1" strokeWidth="8" />
              <path d="M 300,120 C 300,140 370,150 400,180" fill="none" stroke="#cbd5e1" strokeWidth="8" />

              {/* Left & Right Lung Lobes */}
              <path
                d="M 140,170 C 110,210 110,290 150,330 C 190,370 230,340 230,280 C 230,220 200,170 140,170 Z"
                fill="#1e293b"
                stroke="#38bdf8"
                strokeWidth="2.5"
                strokeDasharray="6 3"
              />
              <path
                d="M 460,170 C 490,210 490,290 450,330 C 410,370 370,340 370,280 C 370,220 400,170 460,170 Z"
                fill="#1e293b"
                stroke="#38bdf8"
                strokeWidth="2.5"
                strokeDasharray="6 3"
              />

              <text x="170" y="250" textAnchor="middle" fill="#94a3b8" fontSize="12" fontWeight="bold">
                Right Lung
              </text>
              <text x="170" y="270" textAnchor="middle" fill="#38bdf8" fontSize="10">
                Alveolar Sacs (300M)
              </text>

              <text x="430" y="250" textAnchor="middle" fill="#94a3b8" fontSize="12" fontWeight="bold">
                Left Lung
              </text>
              <text x="430" y="270" textAnchor="middle" fill="#38bdf8" fontSize="10">
                Alveolar Sacs (300M)
              </text>

              {/* Central Heart Schematic */}
              <rect x="255" y="240" width="90" height="110" rx="16" fill="#1e1e38" stroke="#f43f5e" strokeWidth="3" />
              <text x="300" y="280" textAnchor="middle" fill="#f43f5e" fontSize="13" fontWeight="bold">
                HEART
              </text>
              <text x="300" y="300" textAnchor="middle" fill="#94a3b8" fontSize="9">
                RV (Deox) ➔ LV (Ox)
              </text>

              {/* Pulmonary Artery (Blue: Deoxygenated blood Heart -> Lungs) */}
              <path
                d="M 275,240 C 250,200 200,200 180,220"
                fill="none"
                stroke="#3b82f6"
                strokeWidth="4"
                strokeDasharray="5 3"
              />
              <path
                d="M 325,240 C 350,200 400,200 420,220"
                fill="none"
                stroke="#3b82f6"
                strokeWidth="4"
                strokeDasharray="5 3"
              />

              {/* Pulmonary Veins (Red: Oxygenated blood Lungs -> Heart) */}
              <path
                d="M 210,310 C 240,320 260,310 270,300"
                fill="none"
                stroke="#ef4444"
                strokeWidth="4"
              />
              <path
                d="M 390,310 C 360,320 340,310 330,300"
                fill="none"
                stroke="#ef4444"
                strokeWidth="4"
              />

              {/* Interactive Zoom In Hotspot back to Alveolus */}
              <g
                className="cursor-pointer"
                onClick={() => setIsMacroscopic(false)}
              >
                <path d={circlePath(170, 300, 22)} fill="#0284c7" fillOpacity="0.3" stroke="#38bdf8" strokeWidth="2" />
                <path d={circlePath(170, 300, 16)} fill="#0284c7" />
                <text x="170" y="304" textAnchor="middle" fill="#ffffff" fontSize="9" fontWeight="bold">
                  ZOOM
                </text>
              </g>

              {/* Macro Legend */}
              <rect x="50" y="420" width="500" height="42" rx="10" fill="#1e293b" stroke="#334155" />
              <path d={circlePath(90, 441, 5)} fill="#3b82f6" />
              <text x="105" y="445" fill="#94a3b8" fontSize="10">
                Pulmonary Artery (Deox: pO2 40)
              </text>
              <path d={circlePath(280, 441, 5)} fill="#ef4444" />
              <text x="295" y="445" fill="#94a3b8" fontSize="10">
                Pulmonary Vein (Ox: pO2 100)
              </text>
              <text x="470" y="445" fill="#38bdf8" fontSize="10" fontWeight="bold">
                Click ZOOM to inspect
              </text>
            </g>
          )}

          {/* ================================================================= */}
          {/* STATIC MODE: Dynamic Interactive Callouts & Pins Layer           */}
          {/* ================================================================= */}
          {!isAlive && (
            <>
              {/* Static Diffusion Vectors */}
              <defs>
                <marker id="arrow-o2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                  <path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626" />
                </marker>
                <marker id="arrow-co2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                  <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />
                </marker>
              </defs>
              <g id="gas_diffusion_vectors" className="pointer-events-none">
                <path d="M 315,245 C 355,255 390,265 422,272" fill="none" stroke="#ffffff" strokeWidth="5.5" strokeLinecap="round" />
                <path d="M 315,245 C 355,255 390,265 422,272" fill="none" stroke="#dc2626" strokeWidth="3" strokeLinecap="round" markerEnd="url(#arrow-o2)" />
                <rect x="272" y="230" width="38" height="20" rx="5" fill="#fef2f2" stroke="#dc2626" strokeWidth="1.5" />
                <text x="291" y="244" textAnchor="middle" fontSize="11" fontWeight="800" fill="#dc2626">
                  O<tspan baselineShift="sub" fontSize="8.5">2</tspan>
                </text>

                <path d="M 432,215 C 395,205 360,198 320,195" fill="none" stroke="#ffffff" strokeWidth="5.5" strokeLinecap="round" />
                <path d="M 432,215 C 395,205 360,198 320,195" fill="none" stroke="#2563eb" strokeWidth="3" strokeLinecap="round" markerEnd="url(#arrow-co2)" />
                <rect x="268" y="182" width="44" height="20" rx="5" fill="#eff6ff" stroke="#2563eb" strokeWidth="1.5" />
                <text x="290" y="196" textAnchor="middle" fontSize="11" fontWeight="800" fill="#1d4ed8">
                  CO<tspan baselineShift="sub" fontSize="8.5">2</tspan>
                </text>
              </g>

              {/* Pin Callouts Layer */}
              <InteractiveCallouts
                pins={effectivePins}
                landmarks={landmarks}
                activePin={activePin}
                onSelectPin={onSelectPin}
                viewBox={viewBox}
              />
            </>
          )}
        </svg>

        {/* ------------------------------------------------------------------- */}
        {/* SCIENTIFIC HUD FOOTER (ALIVE MODE)                                  */}
        {/* ------------------------------------------------------------------- */}
        {isAlive && !isMacroscopic && (
          <div className="p-3 bg-slate-900 border-t border-slate-800 text-slate-200 flex flex-col gap-2">
            <div className="flex items-center justify-between">
              <span className="text-[11px] font-bold text-amber-300 uppercase tracking-wide flex items-center gap-1.5 font-mono">
                <Activity className="w-3.5 h-3.5 text-amber-400" />
                {PHASES[activePhaseIndex].title}
              </span>
              <span className="text-[10px] font-mono text-slate-400">
                Membrane Thickness: 0.5 µm (Short Diffusion Path)
              </span>
            </div>
            <p className="text-xs text-slate-300 leading-relaxed">
              {PHASES[activePhaseIndex].desc}
            </p>

            {/* Partial Pressure Bar Meters */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 font-mono text-[11px]">
              <div className="p-1.5 bg-slate-800/80 rounded-lg border border-slate-700">
                <div className="text-slate-400 text-[10px]">Alveolus pO2</div>
                <div className="text-amber-300 font-bold">104 mmHg</div>
              </div>
              <div className="p-1.5 bg-slate-800/80 rounded-lg border border-slate-700">
                <div className="text-slate-400 text-[10px]">Inflow Blood pO2</div>
                <div className="text-sky-300 font-bold">40 mmHg</div>
              </div>
              <div className="p-1.5 bg-slate-800/80 rounded-lg border border-slate-700">
                <div className="text-slate-400 text-[10px]">Outflow Blood pO2</div>
                <div className="text-rose-400 font-bold">100 mmHg</div>
              </div>
              <div className="p-1.5 bg-slate-800/80 rounded-lg border border-slate-700">
                <div className="text-slate-400 text-[10px]">Erythrocyte Sat.</div>
                <div className="text-emerald-400 font-bold">98% Hb-O2</div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Attribution & Alignment */}
      <div className="flex items-center justify-between w-full text-[10px] text-slate-400 font-mono px-1">
        <span>Curriculum Standard: Grade 9 NS &amp; Grade 11 Life Sciences (Gaseous Exchange)</span>
        <span>Dual Static/Alive Engine • Heart Architecture Standard</span>
      </div>
    </div>
  );
}
