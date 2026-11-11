import React from 'react';
import InteractiveCallouts from './InteractiveCallouts';
import { Activity } from 'lucide-react';

/**
 * Authentic Periodic Transverse Wave Schematic.
 * Aligned with South African Physical Sciences (Grade 10 Term 1 Waves, Sound & Light).
 *
 * Implements 3-Layer Architecture:
 * - High-definition visual plate without answer-leaking baked labels
 * - Standardized viewBox="0 0 600 480"
 * - Server-side anchor coordinates mapped in transverse_wave.json
 * - InteractiveCallouts with collision-free horizontal elbow leader lines
 * - Single locked view presentation badge
 */
export default function TransverseWaveSvg({
  pins = [],
  labels = [],
  activePin,
  onSelectPin,
  viewBox = '0 0 600 480',
  gradeMask = 'g10',
}) {
  const effectivePins = (pins && pins.length > 0)
    ? pins
    : (labels && labels.length > 0
        ? labels.map((l) => ({
            pin: l.id || l.pin,
            anchor: [l.x !== undefined ? (l.x / 100) * 600 : 300, l.y !== undefined ? (l.y / 100) * 480 : 240],
            default_box: [l.x < 50 ? 60 : 540, l.y !== undefined ? (l.y / 100) * 480 : 240],
            side: l.x < 50 ? 'left' : 'right',
            role: 'target',
          }))
        : []);

  return (
    <div className="flex flex-col items-center w-full max-w-2xl select-none space-y-2">
      {/* Single Locked View Header Badge */}
      <div
        data-testid="transverse-wave-locked-view-badge"
        className="flex items-center justify-between w-full px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs"
      >
        <span className="text-[11px] font-bold text-slate-700 flex items-center gap-1.5 font-mono">
          <Activity className="w-3.5 h-3.5 text-blue-600" />
          <span>Periodic Transverse Wave Profile & Displacement</span>
        </span>
        <span className="text-[10px] font-mono text-slate-500 uppercase tracking-wider">
          Physical Sciences Grade 10
        </span>
      </div>

      <svg
        viewBox={viewBox}
        data-testid="transverse-wave-canvas"
        className="w-full h-auto select-none rounded-xl border border-slate-200 bg-white shadow-sm"
        style={{ minWidth: '320px' }}
      >
        <defs>
          {/* Subtle grid pattern */}
          <pattern id="waveGridPattern" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" strokeWidth="1" />
          </pattern>

          {/* Wave line stroke gradient */}
          <linearGradient id="waveStrokeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#0284c7" />
            <stop offset="50%" stopColor="#2563eb" />
            <stop offset="100%" stopColor="#4f46e5" />
          </linearGradient>

          {/* Arrow markers */}
          <marker id="waveArrowBlue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M 0,0 L 6,3 L 0,6 Z" fill="#2563eb" />
          </marker>
          <marker id="waveArrowGreen" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M 0,0 L 6,3 L 0,6 Z" fill="#059669" />
          </marker>
        </defs>

        {/* ── BACKGROUND GRID ── */}
        <rect x="0" y="0" width="600" height="480" fill="url(#waveGridPattern)" rx="12" />

        {/* ── EQUILIBRIUM REST LINE (Y = 240) ── */}
        <line
          x1="70"
          y1="240"
          x2="530"
          y2="240"
          stroke="#94a3b8"
          strokeWidth="2"
          strokeDasharray="6,5"
        />

        {/* ── 2-CYCLE SINUSOIDAL WAVE PROFILE ── */}
        {/* Node 0: (80, 240) -> Crest 1: (200, 150) -> Node 1: (260, 240) -> Trough 1: (320, 330) -> Node 2: (380, 240) -> Crest 2: (440, 150) -> Node 3: (500, 240) */}
        <path
          d="M 80,240
             C 120,150 160,150 200,150
             C 230,150 245,240 260,240
             C 275,240 290,330 320,330
             C 350,330 365,240 380,240
             C 395,240 410,150 440,150
             C 470,150 485,240 500,240"
          fill="none"
          stroke="url(#waveStrokeGrad)"
          strokeWidth="4"
          strokeLinecap="round"
        />

        {/* Crest 1 peak landmark point (x=200, y=150) */}
        <circle cx="200" cy="150" r="5" fill="#fef08a" stroke="#ca8a04" strokeWidth="2.5" />

        {/* Trough 1 peak landmark point (x=320, y=330) */}
        <circle cx="320" cy="330" r="5" fill="#fef08a" stroke="#ca8a04" strokeWidth="2.5" />

        {/* Crest 2 peak landmark point (x=440, y=150) */}
        <circle cx="440" cy="150" r="5" fill="#fef08a" stroke="#ca8a04" strokeWidth="2.5" />

        {/* ── AMPLITUDE INTERVAL (VERTICAL) ── */}
        <g id="amplitude-indicator">
          <line x1="200" y1="240" x2="200" y2="155" stroke="#059669" strokeWidth="2" strokeDasharray="3,3" />
          <line x1="192" y1="240" x2="208" y2="240" stroke="#059669" strokeWidth="2" />
          <line x1="192" y1="150" x2="208" y2="150" stroke="#059669" strokeWidth="2" />
        </g>

        {/* ── WAVELENGTH INTERVAL (HORIZONTAL) ── */}
        <g id="wavelength-indicator">
          {/* Extension lines from crests */}
          <line x1="200" y1="145" x2="200" y2="110" stroke="#cbd5e1" strokeWidth="1.5" strokeDasharray="2,2" />
          <line x1="440" y1="145" x2="440" y2="110" stroke="#cbd5e1" strokeWidth="1.5" strokeDasharray="2,2" />
          {/* Double-ended horizontal dimension bar */}
          <line x1="200" y1="110" x2="440" y2="110" stroke="#2563eb" strokeWidth="2" />
          <line x1="200" y1="102" x2="200" y2="118" stroke="#2563eb" strokeWidth="2" />
          <line x1="440" y1="102" x2="440" y2="118" stroke="#2563eb" strokeWidth="2" />
        </g>

        {/* ── PARTICLE OSCILLATION AXIS (VERTICAL) ── */}
        <g id="particle-motion-indicator">
          <circle cx="120" cy="240" r="6" fill="#3b82f6" stroke="#1d4ed8" strokeWidth="2" />
          <line x1="120" y1="225" x2="120" y2="205" stroke="#2563eb" strokeWidth="2" markerEnd="url(#waveArrowBlue)" />
          <line x1="120" y1="255" x2="120" y2="275" stroke="#2563eb" strokeWidth="2" markerEnd="url(#waveArrowBlue)" />
        </g>

        {/* ── WAVE PROPAGATION VECTOR (HORIZONTAL) ── */}
        <g id="wave-propagation-indicator">
          <line x1="470" y1="220" x2="520" y2="220" stroke="#059669" strokeWidth="3" markerEnd="url(#waveArrowGreen)" />
        </g>

        {/* ── 3-LAYER INTERACTIVE CALLOUTS ── */}
        <InteractiveCallouts
          pins={effectivePins}
          activePin={activePin}
          onSelectPin={onSelectPin}
        />
      </svg>
    </div>
  );
}
