import React, { useState, useMemo } from 'react';
import { Compass, RotateCw, Activity, CheckCircle2, Sparkles } from 'lucide-react';

const SPECIAL_ANGLES = [
  { deg: 0, rad: '0', sin: '0', cos: '1', tan: '0' },
  { deg: 30, rad: 'π/6', sin: '1/2', cos: '√3/2', tan: '1/√3' },
  { deg: 45, rad: 'π/4', sin: '√2/2', cos: '√2/2', tan: '1' },
  { deg: 60, rad: 'π/3', sin: '√3/2', cos: '1/2', tan: '√3' },
  { deg: 90, rad: 'π/2', sin: '1', cos: '0', tan: 'Undefined' },
  { deg: 120, rad: '2π/3', sin: '√3/2', cos: '-1/2', tan: '-√3' },
  { deg: 135, rad: '3π/4', sin: '√2/2', cos: '-√2/2', tan: '-1' },
  { deg: 150, rad: '5π/6', sin: '1/2', cos: '-√3/2', tan: '-1/√3' },
  { deg: 180, rad: 'π', sin: '0', cos: '-1', tan: '0' },
  { deg: 210, rad: '7π/6', sin: '-1/2', cos: '-√3/2', tan: '1/√3' },
  { deg: 225, rad: '5π/4', sin: '-√2/2', cos: '-√2/2', tan: '1' },
  { deg: 240, rad: '4π/3', sin: '-√3/2', cos: '-1/2', tan: '√3' },
  { deg: 270, rad: '3π/2', sin: '-1', cos: '0', tan: 'Undefined' },
  { deg: 300, rad: '5π/3', sin: '-√3/2', cos: '1/2', tan: '-√3' },
  { deg: 315, rad: '7π/4', sin: '-√2/2', cos: '√2/2', tan: '-1' },
  { deg: 330, rad: '11π/6', sin: '-1/2', cos: '√3/2', tan: '-1/√3' },
  { deg: 360, rad: '2π', sin: '0', cos: '1', tan: '0' },
];

export default function UnitCircleTrigAid() {
  const [angleDeg, setAngleDeg] = useState(45);
  const [showWaves, setShowWaves] = useState(true);

  const rad = useMemo(() => (angleDeg * Math.PI) / 180, [angleDeg]);
  const cosVal = useMemo(() => Math.cos(rad), [rad]);
  const sinVal = useMemo(() => Math.sin(rad), [rad]);
  const tanVal = useMemo(() => {
    if (Math.abs(cosVal) < 1e-6) return null;
    return sinVal / cosVal;
  }, [cosVal, sinVal]);

  // Quadrant determination (1 to 4)
  const quadrant = useMemo(() => {
    const mod = ((angleDeg % 360) + 360) % 360;
    if (mod === 0 || mod === 360) return 1;
    if (mod > 0 && mod < 90) return 1;
    if (mod === 90) return 1;
    if (mod > 90 && mod < 180) return 2;
    if (mod === 180) return 2;
    if (mod > 180 && mod < 270) return 3;
    if (mod === 270) return 3;
    return 4;
  }, [angleDeg]);

  // Special angle exact string match if applicable
  const specialMatch = useMemo(() => {
    return SPECIAL_ANGLES.find((sa) => sa.deg === angleDeg);
  }, [angleDeg]);

  // ASTC rule explanations
  const astcInfo = useMemo(() => {
    switch (quadrant) {
      case 1:
        return { letter: 'A', name: 'ALL', desc: 'All trig functions positive', rule: 'θ in [0°, 90°]' };
      case 2:
        return { letter: 'S', name: 'SIN', desc: 'Only sin θ is positive', rule: 'sin(180° - θ) = sin θ' };
      case 3:
        return { letter: 'T', name: 'TAN', desc: 'Only tan θ is positive', rule: 'tan(180° + θ) = tan θ' };
      case 4:
      default:
        return { letter: 'C', name: 'COS', desc: 'Only cos θ is positive', rule: 'cos(360° - θ) = cos θ' };
    }
  }, [quadrant]);

  // SVG dimensions for Unit Circle
  const R = 90; // radius in SVG units
  const cx = 120;
  const cy = 120;
  const px = cx + R * cosVal;
  const py = cy - R * sinVal; // SVG y is inverted

  return (
    <div data-testid="unit-circle-aid" className="space-y-4 text-slate-800">
      {/* Top Controls: Angle Slider & Quick Angles */}
      <div className="bg-slate-50 p-3 rounded-xl border border-slate-200 space-y-2.5">
        <div className="flex items-center justify-between">
          <label className="text-xs font-bold text-slate-700 flex items-center gap-1.5">
            <RotateCw className="w-3.5 h-3.5 text-[#13519C]" />
            Angle θ: <span className="font-mono text-[#13519C] text-sm">{angleDeg}°</span>
            <span className="text-[11px] font-mono text-slate-500">
              ({specialMatch ? specialMatch.rad : `${(rad / Math.PI).toFixed(2)}π`} rad)
            </span>
          </label>
          <div
            data-testid="astc-badge"
            className="px-2.5 py-0.5 rounded-full text-xs font-bold font-mono bg-indigo-100 text-indigo-900 border border-indigo-200 flex items-center gap-1"
          >
            <span>Quadrant {quadrant}:</span>
            <span className="text-indigo-600">[{astcInfo.letter}] {astcInfo.name}</span>
          </div>
        </div>

        <input
          type="range"
          min="0"
          max="360"
          step="1"
          value={angleDeg}
          data-testid="slider-angle"
          onChange={(e) => setAngleDeg(Number(e.target.value))}
          className="w-full accent-[#13519C] cursor-pointer"
        />

        {/* Quick select buttons for special angles */}
        <div className="flex flex-wrap gap-1 pt-1 border-t border-slate-200">
          <span className="text-[10px] text-slate-400 font-semibold self-center mr-1">Special:</span>
          {[0, 30, 45, 60, 90, 180, 270, 360].map((deg) => (
            <button
              key={deg}
              data-testid={`btn-angle-${deg}`}
              onClick={() => setAngleDeg(deg)}
              className={`px-2 py-0.5 text-[11px] font-mono rounded transition-colors ${
                angleDeg === deg
                  ? 'bg-[#13519C] text-white font-bold shadow-sm'
                  : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200'
              }`}
            >
              {deg}°
            </button>
          ))}
        </div>
      </div>

      {/* Main Visual Display: SVG Unit Circle & Reference Triangle */}
      <div className="bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex flex-col items-center">
        <svg viewBox="0 0 240 240" className="w-56 h-56 select-none">
          {/* Grid Axes */}
          <line x1="20" y1={cy} x2="220" y2={cy} stroke="#CBD5E1" strokeWidth="1.5" />
          <line x1={cx} y1="20" x2={cx} y2="220" stroke="#CBD5E1" strokeWidth="1.5" />

          {/* Quadrant Watermarks */}
          <text x="175" y="65" fill="#E2E8F0" fontSize="18" fontWeight="bold">Q1 (A)</text>
          <text x="45" y="65" fill="#E2E8F0" fontSize="18" fontWeight="bold">Q2 (S)</text>
          <text x="45" y="195" fill="#E2E8F0" fontSize="18" fontWeight="bold">Q3 (T)</text>
          <text x="175" y="195" fill="#E2E8F0" fontSize="18" fontWeight="bold">Q4 (C)</text>

          {/* Unit Circle */}
          <circle cx={cx} cy={cy} r={R} fill="none" stroke="#64748B" strokeWidth="1.5" />

          {/* Reference Right-Angled Triangle */}
          {/* Base: x = cos(θ) */}
          <line x1={cx} y1={cy} x2={px} y2={cy} stroke="#2563EB" strokeWidth="2.5" />
          {/* Height: y = sin(θ) */}
          <line x1={px} y1={cy} x2={px} y2={py} stroke="#059669" strokeWidth="2.5" />
          {/* Hypotenuse: r = 1 */}
          <line x1={cx} y1={cy} x2={px} y2={py} stroke="#D97706" strokeWidth="2" strokeDasharray="3 2" />

          {/* Angle Arc */}
          <path
            d={`M ${cx + 25} ${cy} A 25 25 0 ${angleDeg > 180 ? 1 : 0} 0 ${cx + 25 * Math.cos(rad)} ${cy - 25 * Math.sin(rad)}`}
            fill="none"
            stroke="#13519C"
            strokeWidth="2"
          />

          {/* Point P(cos, sin) */}
          <circle cx={px} cy={py} r="5" fill="#13519C" stroke="#ffffff" strokeWidth="2" />

          {/* Labels */}
          <text x={px + (cosVal >= 0 ? 8 : -45)} y={py + (sinVal >= 0 ? -8 : 16)} fill="#0F172A" fontSize="9" fontWeight="bold" fontFamily="monospace">
            P({cosVal.toFixed(2)}, {sinVal.toFixed(2)})
          </text>
          <text x="215" y={cy - 5} fill="#64748B" fontSize="9">x</text>
          <text x={cx + 5} y="25" fill="#64748B" fontSize="9">y</text>
        </svg>

        {/* Legend */}
        <div className="flex items-center justify-center gap-4 text-[11px] font-mono mt-1">
          <span className="flex items-center gap-1 text-blue-700 font-bold">
            <span className="w-2.5 h-2.5 bg-blue-600 rounded-sm"></span> x = cos θ ({cosVal.toFixed(3)})
          </span>
          <span className="flex items-center gap-1 text-emerald-700 font-bold">
            <span className="w-2.5 h-2.5 bg-emerald-600 rounded-sm"></span> y = sin θ ({sinVal.toFixed(3)})
          </span>
          <span className="flex items-center gap-1 text-amber-700 font-bold">
            <span className="w-2.5 h-2.5 bg-amber-500 rounded-sm"></span> r = 1
          </span>
        </div>
      </div>

      {/* Exact Ratios & Pythagorean Identity Card */}
      <div className="grid grid-cols-3 gap-2 text-center">
        <div className="p-2.5 bg-emerald-50 rounded-xl border border-emerald-200">
          <div className="text-[10px] uppercase font-bold text-emerald-800">sin θ</div>
          <div data-testid="trig-sin-value" className="text-sm font-mono font-bold text-emerald-950 mt-0.5">
            {specialMatch ? specialMatch.sin : sinVal.toFixed(3)}
          </div>
          <div className="text-[9px] font-mono text-emerald-700">{sinVal.toFixed(4)}</div>
        </div>

        <div className="p-2.5 bg-blue-50 rounded-xl border border-blue-200">
          <div className="text-[10px] uppercase font-bold text-blue-800">cos θ</div>
          <div data-testid="trig-cos-value" className="text-sm font-mono font-bold text-blue-950 mt-0.5">
            {specialMatch ? specialMatch.cos : cosVal.toFixed(3)}
          </div>
          <div className="text-[9px] font-mono text-blue-700">{cosVal.toFixed(4)}</div>
        </div>

        <div className="p-2.5 bg-amber-50 rounded-xl border border-amber-200">
          <div className="text-[10px] uppercase font-bold text-amber-800">tan θ</div>
          <div data-testid="trig-tan-value" className="text-sm font-mono font-bold text-amber-950 mt-0.5">
            {specialMatch ? specialMatch.tan : tanVal !== null ? tanVal.toFixed(3) : 'Undefined'}
          </div>
          <div className="text-[9px] font-mono text-amber-700">
            {tanVal !== null ? tanVal.toFixed(4) : 'Asymptote'}
          </div>
        </div>
      </div>

      {/* Simultaneous Sine & Cosine Waveform Graph */}
      <div className="bg-slate-50 p-3 rounded-xl border border-slate-200 space-y-1.5">
        <div className="flex items-center justify-between text-xs">
          <span className="font-bold text-slate-700 flex items-center gap-1.5">
            <Activity className="w-3.5 h-3.5 text-indigo-600" />
            Simultaneous Waveform Trace (0° to 360°)
          </span>
          <span className="text-[10px] font-mono text-slate-500">
            sin²θ + cos²θ = {(sinVal * sinVal + cosVal * cosVal).toFixed(3)}
          </span>
        </div>

        <svg viewBox="0 0 360 80" className="w-full h-20 bg-white rounded-lg border border-slate-200">
          {/* Zero center axis */}
          <line x1="0" y1="40" x2="360" y2="40" stroke="#E2E8F0" strokeWidth="1" />
          {/* Key ticks: 90, 180, 270 */}
          <line x1="90" y1="0" x2="90" y2="80" stroke="#F1F5F9" strokeWidth="1" strokeDasharray="2 2" />
          <line x1="180" y1="0" x2="180" y2="80" stroke="#F1F5F9" strokeWidth="1" strokeDasharray="2 2" />
          <line x1="270" y1="0" x2="270" y2="80" stroke="#F1F5F9" strokeWidth="1" strokeDasharray="2 2" />

          {/* Sine Wave (emerald) */}
          <path
            d={Array.from({ length: 361 }, (_, deg) => {
              const r = (deg * Math.PI) / 180;
              const y = 40 - 30 * Math.sin(r);
              return `${deg === 0 ? 'M' : 'L'} ${deg} ${y.toFixed(1)}`;
            }).join(' ')}
            fill="none"
            stroke="#059669"
            strokeWidth="1.5"
          />

          {/* Cosine Wave (blue) */}
          <path
            d={Array.from({ length: 361 }, (_, deg) => {
              const r = (deg * Math.PI) / 180;
              const y = 40 - 30 * Math.cos(r);
              return `${deg === 0 ? 'M' : 'L'} ${deg} ${y.toFixed(1)}`;
            }).join(' ')}
            fill="none"
            stroke="#2563EB"
            strokeWidth="1.5"
            strokeDasharray="3 1"
          />

          {/* Current Angle Tracking Points */}
          <circle cx={angleDeg} cy={40 - 30 * sinVal} r="3.5" fill="#059669" stroke="#ffffff" strokeWidth="1.5" />
          <circle cx={angleDeg} cy={40 - 30 * cosVal} r="3.5" fill="#2563EB" stroke="#ffffff" strokeWidth="1.5" />
          <line x1={angleDeg} y1="0" x2={angleDeg} y2="80" stroke="#E11D48" strokeWidth="1" strokeDasharray="2 2" />
        </svg>

        <div className="flex justify-between items-center text-[10px] text-slate-500 font-mono px-1">
          <span>0° (0 rad)</span>
          <span>90° (π/2)</span>
          <span>180° (π)</span>
          <span>270° (3π/2)</span>
          <span>360° (2π)</span>
        </div>
      </div>

      {/* Curriculum Note */}
      <div className="text-[11px] text-slate-600 bg-indigo-50/70 p-2.5 rounded-lg border border-indigo-200">
        <span className="font-semibold text-indigo-950">National Curriculum Standards Guide:</span>{' '}
        In {astcInfo.name} (Quadrant {quadrant}), {astcInfo.desc}. Identity:{' '}
        <code className="font-mono text-indigo-900 bg-white px-1 py-0.5 rounded border border-indigo-200">
          {astcInfo.rule}
        </code>
      </div>
    </div>
  );
}
