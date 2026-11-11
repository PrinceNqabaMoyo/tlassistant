import React, { useState, useEffect, useRef, useMemo } from 'react';
import InteractiveCallouts from './InteractiveCallouts';
import {
  Zap,
  BookOpen,
  FileText,
  Sparkles,
  Play,
  Pause,
  Thermometer,
  Gauge,
  Activity,
  Eye,
  ShieldAlert,
  Flame,
} from 'lucide-react';

function normalizeGeyserView(rawView) {
  const v = String(rawView || 'textbook').toLowerCase().trim();
  if (v === 'exam' || v === 'exam_paper' || v === 'stipple') return 'exam';
  if (v === 'alive' || v === 'sim' || v === 'simulation') return 'alive';
  return 'textbook';
}

const VIEW_METADATA = {
  textbook: {
    label: 'Domestic Water Heater Tank & Heating Element Master',
    Icon: BookOpen,
  },
  exam: {
    label: 'Examination Ink Stipple Line-Art',
    Icon: FileText,
  },
  alive: {
    label: 'Dynamic Electrical Heating & Convection Simulation',
    Icon: Sparkles,
  },
};

/**
 * Authentic Domestic Geyser Water Heater & Heating Element Schematic.
 * Aligned with South African Natural Sciences Grade 8/9 and Physical Sciences Grade 10/11.
 *
 * Implements Rule 0d-14 (The Heart Standard) & Dual Static/Alive Engine:
 * - Static Mode: Authentic Textbook Master + NSC Exam Stipple plates in public/diagrams/
 * - Alive Mode: 60 FPS requestAnimationFrame simulation showing electric current flow,
 *   Joule heating (P = I^2 * R), convective water thermal circulation, and thermostat bimetallic trip.
 */
export default function GeyserHeatingElementSvg({
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
  initialWaterTemp = 35,
  thermostatSetpoint = 65,
}) {
  const initialView = normalizeGeyserView(view || defaultView);
  const [activeView, setActiveView] = useState(initialView);
  const [isAlive, setIsAlive] = useState(initialView === 'alive');

  // Simulation controls
  const [isPlaying, setIsPlaying] = useState(true);
  const [playbackSpeed, setPlaybackSpeed] = useState(propPlaybackSpeed || 1.0);
  const [waterTemp, setWaterTemp] = useState(initialWaterTemp);
  const [setpoint, setSetpoint] = useState(thermostatSetpoint);
  const [manualTrip, setManualTrip] = useState(false);
  const [trackedPlume, setTrackedPlume] = useState(false);

  useEffect(() => {
    const v = normalizeGeyserView(view || defaultView);
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

      // Warm water slowly up towards setpoint if heating
      setWaterTemp((prev) => {
        const isHeating = !manualTrip && prev < setpoint;
        if (isHeating) {
          return Math.min(setpoint, prev + dt * 1.8 * playbackSpeed);
        } else if (prev > 22) {
          // Slow passive cooling if tripped
          return Math.max(22, prev - dt * 0.4 * playbackSpeed);
        }
        return prev;
      });

      animFrameRef.current = requestAnimationFrame(animate);
    };

    lastTimeRef.current = performance.now();
    animFrameRef.current = requestAnimationFrame(animate);

    return () => {
      if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
    };
  }, [isAlive, isPlaying, playbackSpeed, manualTrip, setpoint]);

  // Derived electrical parameters
  const isThermostatClosed = !manualTrip && waterTemp < setpoint;
  const voltageV = 230; // standard SA mains voltage
  const resistanceOhms = 17.6; // 3 kW / (230 V)^2
  const currentAmps = isThermostatClosed ? (voltageV / resistanceOhms).toFixed(1) : (0.0).toFixed(1);
  const powerKW = isThermostatClosed ? ((voltageV * (voltageV / resistanceOhms)) / 1000).toFixed(2) : (0.0).toFixed(2);
  const pressureKPa = (350 + (waterTemp / 100) * 80).toFixed(0);

  // Convection particles (12 rising warm fluid parcels)
  const convectionPlumes = useMemo(() => {
    const list = [];
    const count = 12;
    for (let i = 0; i < count; i++) {
      const offset = i / count;
      const progress = ((simTime * 0.25 + offset) % 1 + 1) % 1;

      let px, py;
      if (progress < 0.5) {
        // Rising warm buoyant water along the central vertical column
        const u = progress / 0.5;
        px = 290 + Math.sin(u * Math.PI * 2 + i) * 15;
        py = 370 - u * 270;
      } else {
        // Cooler denser water descending along the left/right walls
        const u = (progress - 0.5) / 0.5;
        const sideSign = i % 2 === 0 ? 1 : -1;
        px = 300 + sideSign * (100 - Math.sin(u * Math.PI) * 10);
        py = 100 + u * 270;
      }

      list.push({
        id: `plume_${i}`,
        index: i,
        x: px,
        y: py,
        progress,
        isRising: progress < 0.5,
      });
    }
    return list;
  }, [simTime]);

  return (
    <div
      data-testid="geyser-heating-element-root"
      className="flex flex-col items-center w-full max-w-2xl select-none space-y-2 font-sans"
    >
      {/* Header Bar */}
      {allowViewSwitch ? (
        <div className="flex items-center justify-between w-full px-2 py-1 bg-slate-50 border border-slate-200 rounded-xl text-xs">
          <span className="text-[11px] font-bold text-slate-600 uppercase tracking-wide flex items-center gap-1.5 font-mono">
            <Zap className="w-3.5 h-3.5 text-amber-600" />
            Geyser Schematic Engine:
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
          data-testid="geyser-locked-view-badge"
          className="flex items-center justify-between w-full px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs"
        >
          <span className="text-[11px] font-bold text-slate-700 flex items-center gap-1.5 font-mono">
            <CurrentViewIcon className="w-3.5 h-3.5 text-amber-600" />
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

      {/* Backward-compatibility badge */}
      <span data-testid="geyser_heating_element-locked-view-badge" className="sr-only">Locked View</span>

      {/* Simulation Interactive Control Bar (Alive mode only) */}
      {isAlive && showSimControls && (
        <div
          data-testid="geyser-sim-controls"
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

          {/* Temperature & Thermostat Setpoint */}
          <div className="flex items-center gap-2">
            <span className="text-[10px] font-mono text-slate-400">Thermostat Setpoint:</span>
            <button
              type="button"
              data-testid="btn-setpoint-55"
              onClick={() => setSetpoint(55)}
              className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono ${setpoint === 55 ? 'bg-amber-500 text-slate-950' : 'bg-slate-800 text-slate-400'}`}
            >
              55 °C
            </button>
            <button
              type="button"
              data-testid="btn-setpoint-65"
              onClick={() => setSetpoint(65)}
              className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono ${setpoint === 65 ? 'bg-amber-500 text-slate-950' : 'bg-slate-800 text-slate-400'}`}
            >
              65 °C (Standard)
            </button>
            <button
              type="button"
              data-testid="btn-setpoint-75"
              onClick={() => setSetpoint(75)}
              className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono ${setpoint === 75 ? 'bg-amber-500 text-slate-950' : 'bg-slate-800 text-slate-400'}`}
            >
              75 °C
            </button>
          </div>

          {/* Manual Trip / Fault Toggle */}
          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-trip-thermostat"
              onClick={() => setManualTrip((m) => !m)}
              className={`px-2 py-1 rounded-md text-[10px] font-bold font-mono transition cursor-pointer flex items-center gap-1 ${
                manualTrip ? 'bg-red-600 text-white' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              <ShieldAlert className="w-3 h-3 text-amber-400" />
              <span>{manualTrip ? 'Trip Active (Cut-Off)' : 'Simulate Cut-Off'}</span>
            </button>
            <button
              type="button"
              data-testid="btn-follow-plume"
              onClick={() => setTrackedPlume((p) => !p)}
              className={`px-2 py-1 rounded-md text-[10px] font-bold font-mono transition cursor-pointer flex items-center gap-1 ${
                trackedPlume ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              <Eye className="w-3 h-3" />
              <span>{trackedPlume ? 'Tracking Plume' : 'Track Plume'}</span>
            </button>
          </div>
        </div>
      )}

      {/* Primary SVG Canvas */}
      <svg
        viewBox={viewBox}
        data-testid="geyser-canvas"
        className="w-full h-auto drop-shadow-sm bg-white rounded-xl border border-slate-100 transition-all duration-300"
        style={{ minWidth: '320px', maxHeight: '520px' }}
      >
        <defs>
          <linearGradient id="tankWaterGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor={isThermostatClosed ? '#fca5a5' : '#93c5fd'} stopOpacity="0.4" />
            <stop offset="100%" stopColor="#3b82f6" stopOpacity="0.6" />
          </linearGradient>

          <linearGradient id="heatingElementGlow" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stopColor={isThermostatClosed ? '#ef4444' : '#b45309'} />
            <stop offset="50%" stopColor={isThermostatClosed ? '#fbbf24' : '#d97706'} />
            <stop offset="100%" stopColor={isThermostatClosed ? '#ef4444' : '#b45309'} />
          </linearGradient>

          <filter id="elementHeatGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
          </filter>
        </defs>

        {/* MODE 1: STATIC EXAM PLATES */}
        {!isAlive && activeView === 'textbook' && (
          <g id="view_textbook_master">
            <image
              href="/diagrams/geyser_heating_element_textbook.jpg"
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
              href="/diagrams/geyser_heating_element_exam_stipple.jpg"
              x="20"
              y="0"
              width="560"
              height="480"
              preserveAspectRatio="xMidYMid meet"
              className="select-none pointer-events-none"
            />
          </g>
        )}

        {/* MODE 2: ALIVE DYNAMIC CONVECTION & JOULE HEATING SIMULATION */}
        {isAlive && (
          <g id="alive_geyser_simulation" data-testid="alive-geyser-simulation">
            {/* Outer Tank Insulation Layer */}
            <rect
              x="160"
              y="50"
              width="280"
              height="340"
              rx="40"
              fill="#f1f5f9"
              stroke="#cbd5e1"
              strokeWidth="6"
            />

            {/* Inner Enameled Steel Pressure Tank */}
            <rect
              x="180"
              y="65"
              width="240"
              height="310"
              rx="25"
              fill="url(#tankWaterGrad)"
              stroke="#64748b"
              strokeWidth="3"
            />

            {/* Cold Water Inlet Pipe with Dip Tube (Delivers to bottom) */}
            <g id="cold_water_inlet_dip_tube">
              <rect x="205" y="40" width="16" height="320" rx="3" fill="#60a5fa" stroke="#2563eb" strokeWidth="1.5" />
              {/* Cold water downward arrows */}
              <path d="M 213,90 L 213,320" stroke="#1d4ed8" strokeWidth="2" strokeDasharray="6 6" />
              <text x="200" y="35" textAnchor="end" fill="#2563eb" fontSize="9" fontWeight="bold">
                Cold In (Dip Tube)
              </text>
            </g>

            {/* Hot Water Outlet Pipe (Draws from top) */}
            <g id="hot_water_outlet">
              <rect x="380" y="40" width="16" height="40" rx="3" fill="#f87171" stroke="#dc2626" strokeWidth="1.5" />
              <path d="M 388,75 L 388,45" stroke="#b91c1c" strokeWidth="2" strokeDasharray="4 4" />
              <text x="400" y="35" textAnchor="start" fill="#dc2626" fontSize="9" fontWeight="bold">
                Hot Water Out
              </text>
            </g>

            {/* Sacrificial Magnesium Anode Rod */}
            <g id="sacrificial_anode_rod">
              <rect x="250" y="65" width="10" height="240" rx="2" fill="#94a3b8" stroke="#475569" strokeWidth="1" />
              <text x="255" y="60" textAnchor="middle" fill="#64748b" fontSize="8" fontWeight="bold">
                Mg Anode
              </text>
            </g>

            {/* Heating Element Coil (Nichrome Resistor) at bottom */}
            <g id="coiled_heating_element">
              {/* Element bracket */}
              <rect x="270" y="375" width="60" height="12" rx="4" fill="#334155" />
              {/* Coiled resistor path */}
              <path
                d="M 280,375 C 280,345 300,345 300,360 C 300,345 320,345 320,375"
                fill="none"
                stroke="url(#heatingElementGlow)"
                strokeWidth={isThermostatClosed ? "6" : "4"}
                strokeLinecap="round"
                filter={isThermostatClosed ? "url(#elementHeatGlow)" : "none"}
              />
              {/* Animated electric current flow dashes */}
              {isThermostatClosed && (
                <path
                  d="M 280,375 C 280,345 300,345 300,360 C 300,345 320,345 320,375"
                  fill="none"
                  stroke="#ffffff"
                  strokeWidth="2"
                  strokeDasharray="4 6"
                  strokeDashoffset={-simTime * 40}
                />
              )}
            </g>

            {/* Thermostat Probe & Bimetallic Contact Strip */}
            <g id="thermostat_sensor">
              <rect x="330" y="325" width="8" height="45" rx="2" fill="#cbd5e1" stroke="#475569" strokeWidth="1" />
              {/* Bimetallic contacts */}
              <circle cx="334" cy="365" r="4" fill={isThermostatClosed ? '#22c55e' : '#ef4444'} />
              <text x="345" y="340" fill={isThermostatClosed ? '#15803d' : '#b91c1c'} fontSize="9" fontWeight="bold">
                {isThermostatClosed ? 'Closed (Heating)' : 'Open (Tripped)'}
              </text>
            </g>

            {/* Convection Circulation Plumes */}
            <g id="convection_circulation">
              {convectionPlumes.map((plume) => {
                const isTracked = trackedPlume && plume.index === 0;
                return (
                  <g key={plume.id}>
                    {isTracked && (
                      <circle
                        cx={plume.x}
                        cy={plume.y}
                        r="9"
                        fill="none"
                        stroke="#f59e0b"
                        strokeWidth="2"
                      />
                    )}
                    <circle
                      cx={plume.x}
                      cy={plume.y}
                      r={plume.isRising ? 5.5 : 4.5}
                      fill={plume.isRising ? '#ef4444' : '#3b82f6'}
                      opacity={isThermostatClosed ? 0.85 : 0.4}
                    />
                  </g>
                );
              })}
            </g>

            {/* Central Thermal Convection Circulation Flow Arrows */}
            <path
              d="M 295,330 L 295,140 Q 295,110 320,110 Q 360,110 360,150 L 360,300"
              fill="none"
              stroke={isThermostatClosed ? '#f87171' : '#94a3b8'}
              strokeWidth="2"
              strokeDasharray="5 5"
              strokeDashoffset={-simTime * 20}
              opacity="0.6"
            />

            {/* Temperature & Pressure (TP) Valve on Side */}
            <g id="tp_safety_valve" transform="translate(420, 110)">
              <rect x="0" y="0" width="25" height="15" rx="2" fill="#e2e8f0" stroke="#64748b" strokeWidth="1.5" />
              <text x="32" y="12" fill="#475569" fontSize="9" fontWeight="bold">
                TP Valve ({pressureKPa} kPa)
              </text>
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

              {/* Meter 1: Water Temperature */}
              <g transform="translate(15, 12)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  WATER TEMP (T)
                </text>
                <text x="0" y="28" fill="#f8fafc" fontSize="13" fontWeight="bold" fontFamily="monospace">
                  {waterTemp.toFixed(1)} °C / {setpoint} °C
                </text>
              </g>

              {/* Meter 2: Electrical Current & Voltage */}
              <g transform="translate(150, 12)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  ELECTRIC CURRENT (I)
                </text>
                <text x="0" y="28" fill="#facc15" fontSize="13" fontWeight="bold" fontFamily="monospace">
                  {currentAmps} A (230 V AC)
                </text>
              </g>

              {/* Meter 3: Joule Heating Power */}
              <g transform="translate(290, 12)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  JOULE POWER (P = I²R)
                </text>
                <text x="0" y="28" fill="#f87171" fontSize="13" fontWeight="bold" fontFamily="monospace">
                  {powerKW} kW ({resistanceOhms} Ω)
                </text>
              </g>

              {/* Meter 4: Thermostat Status */}
              <g transform="translate(415, 12)">
                <text x="0" y="10" fill="#94a3b8" fontSize="9" fontWeight="bold">
                  THERMOSTAT
                </text>
                <text
                  x="0"
                  y="28"
                  fill={isThermostatClosed ? '#4ade80' : '#f87171'}
                  fontSize="11"
                  fontWeight="bold"
                  fontFamily="monospace"
                >
                  {isThermostatClosed ? 'HEATING ON' : 'CUT-OFF TRIP'}
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
