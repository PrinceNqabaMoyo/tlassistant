import React from 'react';
import InteractiveCallouts from './InteractiveCallouts';
import { Volume2 } from 'lucide-react';

/**
 * Authentic Doppler Effect Wavefront Schematic.
 * Aligned with South African Physical Sciences Grade 12 (Waves, Sound & Light: Doppler Effect).
 *
 * Implements 3-Layer Architecture:
 * - High-definition visual plate without answer-leaking baked labels
 * - Standardized viewBox="0 0 600 480"
 * - Server-side anchor coordinates mapped in doppler_effect.json
 * - InteractiveCallouts with collision-free horizontal elbow leader lines
 * - Single locked view presentation badge
 */
export default function DopplerEffectSvg({
  pins = [],
  labels = [],
  activePin,
  onSelectPin,
  viewBox = '0 0 600 480',
  gradeMask = 'g12',
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
        data-testid="doppler-effect-locked-view-badge"
        className="flex items-center justify-between w-full px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs"
      >
        <span className="text-[11px] font-bold text-slate-700 flex items-center gap-1.5 font-mono">
          <Volume2 className="w-3.5 h-3.5 text-blue-600" />
          <span>Doppler Effect Wavefront Propagation & Frequency Shift</span>
        </span>
        <span className="text-[10px] font-mono text-slate-500 uppercase tracking-wider">
          Physical Sciences Grade 12
        </span>
      </div>

      <svg
        viewBox={viewBox}
        data-testid="doppler-effect-canvas"
        className="w-full h-auto select-none rounded-xl border border-slate-200 bg-white shadow-sm"
        style={{ minWidth: '320px' }}
      >
        <defs>
          {/* Wavefront concentric stroke gradient */}
          <linearGradient id="wavefrontGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#38bdf8" />
            <stop offset="50%" stopColor="#2563eb" />
            <stop offset="100%" stopColor="#1d4ed8" />
          </linearGradient>

          {/* Velocity arrow marker */}
          <marker id="dopplerVelocityArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M 0,0 L 6,3 L 0,6 Z" fill="#dc2626" />
          </marker>
        </defs>

        {/* ── BACKGROUND ── */}
        <rect x="0" y="0" width="600" height="480" fill="#fafafa" rx="12" />

        {/* ── CENTRAL MOTION AXIS (Y = 240) ── */}
        <line
          x1="50"
          y1="240"
          x2="550"
          y2="240"
          stroke="#e2e8f0"
          strokeWidth="1.5"
          strokeDasharray="4,4"
        />

        {/* ── NON-CONCENTRIC SPHERICAL SOUND WAVEFRONTS ── */}
        {/* Oldest wavefront 1 (emitted at x=210, radius 160) */}
        <circle
          cx="210"
          cy="240"
          r="160"
          fill="none"
          stroke="#93c5fd"
          strokeWidth="2"
          strokeDasharray="6,3"
          opacity="0.6"
        />

        {/* Wavefront 2 (emitted at x=250, radius 120) */}
        <circle
          cx="250"
          cy="240"
          r="120"
          fill="none"
          stroke="#60a5fa"
          strokeWidth="2.5"
          opacity="0.75"
        />

        {/* Wavefront 3 (emitted at x=290, radius 80) */}
        <circle
          cx="290"
          cy="240"
          r="80"
          fill="none"
          stroke="#3b82f6"
          strokeWidth="3"
          opacity="0.9"
        />

        {/* Youngest wavefront 4 (emitted at x=330, radius 40) */}
        <circle
          cx="330"
          cy="240"
          r="40"
          fill="none"
          stroke="#1d4ed8"
          strokeWidth="3.5"
        />

        {/* ── MOVING SOUND SOURCE (AMBULANCE / EMITTER) ── */}
        <g id="sound-source" transform="translate(315, 226)">
          {/* Vehicle body */}
          <rect x="0" y="0" width="32" height="18" rx="4" fill="#ffffff" stroke="#1e293b" strokeWidth="2" />
          {/* Windshield */}
          <rect x="18" y="2" width="10" height="14" rx="2" fill="#38bdf8" />
          {/* Wheels */}
          <circle cx="8" cy="18" r="4" fill="#334155" />
          <circle cx="24" cy="18" r="4" fill="#334155" />
          {/* Flashing roof beacon */}
          <ellipse cx="14" cy="-2" rx="3.5" ry="3" fill="#ef4444" stroke="#b91c1c" strokeWidth="1" />
        </g>

        {/* ── SOURCE VELOCITY VECTOR (VS) ── */}
        <g id="source-velocity-indicator">
          <line
            x1="355"
            y1="215"
            x2="400"
            y2="215"
            stroke="#dc2626"
            strokeWidth="3"
            markerEnd="url(#dopplerVelocityArrow)"
          />
        </g>

        {/* ── STATIONARY OBSERVER AHEAD (X = 520, Y = 240) ── */}
        <g id="observer-ahead">
          {/* Observer icon */}
          <circle cx="520" cy="225" r="10" fill="#f1f5f9" stroke="#475569" strokeWidth="2" />
          <path d="M 508,255 C 508,242 532,242 532,255 Z" fill="#64748b" />
          {/* Ear / listener indicator */}
          <path d="M 510,225 C 507,222 507,228 510,227" fill="none" stroke="#2563eb" strokeWidth="2" />
        </g>

        {/* ── STATIONARY OBSERVER BEHIND (X = 80, Y = 240) ── */}
        <g id="observer-behind">
          {/* Observer icon */}
          <circle cx="80" cy="225" r="10" fill="#f1f5f9" stroke="#475569" strokeWidth="2" />
          <path d="M 68,255 C 68,242 92,242 92,255 Z" fill="#64748b" />
          {/* Ear / listener indicator */}
          <path d="M 90,225 C 93,222 93,228 90,227" fill="none" stroke="#2563eb" strokeWidth="2" />
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
