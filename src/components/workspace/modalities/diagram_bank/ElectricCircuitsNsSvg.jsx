import React from 'react';
import InteractiveCallouts from './InteractiveCallouts';
import { Zap } from 'lucide-react';

/**
 * Authentic Electric Circuits Schematic (Series & Parallel with Meters).
 * Aligned with South African Natural Sciences Grade 8 & 9 (Energy & Change Term 3: Circuits).
 *
 * Implements 3-Layer Architecture:
 * - High-definition visual plate without answer-leaking baked labels
 * - Server-side anchor coordinates mapped in electric_circuits_ns.json
 * - InteractiveCallouts with collision-free horizontal elbow leader lines
 * - Single locked view presentation badge
 */
export default function ElectricCircuitsNsSvg({
  pins = [],
  labels = [],
  activePin,
  onSelectPin,
  viewBox = '0 0 600 480',
  gradeMask = 'g8',
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
        data-testid="electric-circuits-ns-locked-view-badge"
        className="flex items-center justify-between w-full px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs"
      >
        <span className="text-[11px] font-bold text-slate-700 flex items-center gap-1.5 font-mono">
          <Zap className="w-3.5 h-3.5 text-amber-500" />
          <span>Electric Circuit Schematic (Series & Parallel)</span>
        </span>
        <span className="text-[10px] font-mono text-slate-500 uppercase tracking-wider">
          {gradeMask === 'g9' ? 'Natural Sciences Grade 9' : 'Natural Sciences Grade 8'}
        </span>
      </div>

      <svg
        viewBox={viewBox}
        data-testid="electric-circuits-ns-canvas"
        className="w-full h-auto select-none rounded-xl border border-slate-200 bg-white shadow-sm"
        style={{ minWidth: '320px' }}
      >
        {/* ── MAIN CIRCUIT PATHS ── */}
        {/* Top rail: Left corner (120,75) -> switch -> battery -> Right corner (480,75) */}
        <line x1="120" y1="75" x2="160" y2="75" stroke="#334155" strokeWidth="3" />
        {/* Switch gaps */}
        <line x1="200" y1="75" x2="280" y2="75" stroke="#334155" strokeWidth="3" />
        <line x1="320" y1="75" x2="480" y2="75" stroke="#334155" strokeWidth="3" />

        {/* Left vertical rail: (120,75) -> Ammeter -> (120,255) -> (200,255) */}
        <line x1="120" y1="75" x2="120" y2="215" stroke="#334155" strokeWidth="3" />
        <line x1="120" y1="265" x2="120" y2="255" stroke="#334155" strokeWidth="3" />
        <line x1="120" y1="255" x2="200" y2="255" stroke="#334155" strokeWidth="3" />

        {/* Right vertical rail: (480,75) -> (480,255) -> (400,255) */}
        <line x1="480" y1="75" x2="480" y2="255" stroke="#334155" strokeWidth="3" />
        <line x1="480" y1="255" x2="400" y2="255" stroke="#334155" strokeWidth="3" />

        {/* Parallel Branch 1 (Upper: y=200): (200,255) -> (200,200) -> Resistor 1 -> (400,200) -> (400,255) */}
        <path d="M 200,255 L 200,200 L 270,200" fill="none" stroke="#334155" strokeWidth="3" />
        <path d="M 330,200 L 400,200 L 400,255" fill="none" stroke="#334155" strokeWidth="3" />

        {/* Parallel Branch 2 (Lower: y=310): (200,255) -> (200,310) -> Resistor 2 -> (400,310) -> (400,255) */}
        <path d="M 200,255 L 200,310 L 270,310" fill="none" stroke="#334155" strokeWidth="3" />
        <path d="M 330,310 L 400,310 L 400,255" fill="none" stroke="#334155" strokeWidth="3" />

        {/* Voltmeter Parallel Loop across Branch 2: (220,310) -> (220,395) -> Voltmeter -> (380,395) -> (380,310) */}
        <path d="M 230,310 L 230,395 L 275,395" fill="none" stroke="#2563eb" strokeWidth="2" strokeDasharray="4 2" />
        <path d="M 325,395 L 370,395 L 370,310" fill="none" stroke="#2563eb" strokeWidth="2" strokeDasharray="4 2" />

        {/* ── 1. CHEMICAL BATTERY (TWO CELLS IN SERIES) ── */}
        <g id="battery-cells" transform="translate(300, 75)">
          {/* Cell 1: Long positive plate (left), short thick negative (right) */}
          <line x1="-20" y1="-18" x2="-20" y2="18" stroke="#0f172a" strokeWidth="2.5" />
          <line x1="-12" y1="-10" x2="-12" y2="10" stroke="#0f172a" strokeWidth="5.5" />
          {/* Cell 2 */}
          <line x1="8" y1="-18" x2="8" y2="18" stroke="#0f172a" strokeWidth="2.5" />
          <line x1="16" y1="-10" x2="16" y2="10" stroke="#0f172a" strokeWidth="5.5" />
          {/* Internal connection between cells */}
          <line x1="-12" y1="0" x2="8" y2="0" stroke="#334155" strokeWidth="2.5" />
          {/* Polarity signs */}
          <text x="-27" y="-12" fontSize="12" fill="#ef4444" fontWeight="bold" fontFamily="sans-serif">+</text>
          <text x="21" y="-10" fontSize="14" fill="#3b82f6" fontWeight="bold" fontFamily="sans-serif">−</text>
        </g>

        {/* ── 2. KNIFE SWITCH COMPONENT ── */}
        <g id="switch" transform="translate(180, 75)">
          <circle cx="-16" cy="0" r="3.5" fill="#334155" />
          <circle cx="16" cy="0" r="3.5" fill="#334155" />
          {/* Closed contact blade */}
          <line x1="-16" y1="0" x2="14" y2="-4" stroke="#d97706" strokeWidth="3" strokeLinecap="round" />
        </g>

        {/* ── 3. AMMETER (SERIES IN MAIN TRUNK) ── */}
        <g id="ammeter" transform="translate(120, 240)">
          <circle cx="0" cy="0" r="22" fill="#f8fafc" stroke="#0284c7" strokeWidth="2.5" />
          <text x="0" y="7" fontSize="18" fill="#0369a1" fontWeight="bold" textAnchor="middle" fontFamily="sans-serif">
            A
          </text>
        </g>

        {/* ── 4. BRANCHING JUNCTION NODES ── */}
        <circle cx="200" cy="255" r="5" fill="#0f172a" />
        <circle cx="400" cy="255" r="5" fill="#0f172a" />
        <circle cx="230" cy="310" r="4" fill="#2563eb" />
        <circle cx="370" cy="310" r="4" fill="#2563eb" />

        {/* ── 5. RESISTOR 1 (BRANCH 1) — Authentic IEC/SABS clean rectangular symbol ── */}
        <g id="resistor-1" transform="translate(300, 200)">
          <rect x="-28" y="-12" width="56" height="24" rx="2" fill="#f8fafc" stroke="#0f172a" strokeWidth="2.5" />
          <text x="0" y="4" fontSize="11" fill="#475569" fontWeight="bold" textAnchor="middle" fontFamily="sans-serif">
            R₁
          </text>
        </g>

        {/* ── 6. RESISTOR 2 (BRANCH 2) — Authentic IEC/SABS clean rectangular symbol ── */}
        <g id="resistor-2" transform="translate(300, 310)">
          <rect x="-28" y="-12" width="56" height="24" rx="2" fill="#f8fafc" stroke="#0f172a" strokeWidth="2.5" />
          <text x="0" y="4" fontSize="11" fill="#475569" fontWeight="bold" textAnchor="middle" fontFamily="sans-serif">
            R₂
          </text>
        </g>

        {/* ── 7. VOLTMETER (PARALLEL) ── */}
        <g id="voltmeter" transform="translate(300, 395)">
          <circle cx="0" cy="0" r="22" fill="#eff6ff" stroke="#2563eb" strokeWidth="2.5" />
          <text x="0" y="7" fontSize="18" fill="#1d4ed8" fontWeight="bold" textAnchor="middle" fontFamily="sans-serif">
            V
          </text>
        </g>

        {/* ── 3-LAYER COLLISION-FREE INTERACTIVE CALLOUTS ── */}
        <InteractiveCallouts
          pins={effectivePins}
          activePin={activePin}
          onSelectPin={onSelectPin}
          canvasWidth={600}
          canvasHeight={480}
        />
      </svg>
    </div>
  );
}
