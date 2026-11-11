import React, { useState } from 'react';

/**
 * 1. Geometry2DCircleExplorerAid (Maths #26)
 * Interactive Circle Parts (Radius, Diameter, Chord, Arc, Sector) & Straight Line Geometry Explorer
 */
export function Geometry2DCircleExplorerAid() {
  const [selectedPart, setSelectedPart] = useState('radius');

  const PARTS = {
    radius: {
      label: 'Radius (r)',
      formula: 'r = d ÷ 2',
      desc: 'Distance from the centre O to any point on the circumference. All radii of a circle are equal.',
      color: '#13519C',
    },
    diameter: {
      label: 'Diameter (d)',
      formula: 'd = 2 × r',
      desc: 'A straight line passing through the centre O joining two points on the circumference. Longest chord of a circle.',
      color: '#0D9488',
    },
    chord: {
      label: 'Chord',
      formula: 'Line segment joining 2 circumference points',
      desc: 'A straight line segment whose endpoints both lie on the circle (does not need to pass through the centre).',
      color: '#D97706',
    },
    arc: {
      label: 'Arc',
      formula: 'Curved portion of circumference',
      desc: 'A continuous portion of the curved boundary (circumference) of the circle.',
      color: '#E11D48',
    },
    sector: {
      label: 'Sector',
      formula: 'Bounded by 2 radii and an arc',
      desc: 'A "pie-slice" region enclosed by two radii and the arc between them.',
      color: '#7C3AED',
    },
  };

  const active = PARTS[selectedPart] || PARTS.radius;

  return (
    <div data-testid="geometry-2d-circle-aid" className="bg-white rounded-2xl border border-slate-200 p-4 space-y-4 text-slate-800">
      <div className="flex flex-wrap gap-1.5">
        {Object.entries(PARTS).map(([key, item]) => (
          <button
            key={key}
            type="button"
            onClick={() => setSelectedPart(key)}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
              selectedPart === key
                ? 'bg-[#13519C] text-white shadow-sm'
                : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
            }`}
          >
            {item.label}
          </button>
        ))}
      </div>

      <div className="flex justify-center bg-slate-50 rounded-xl border border-slate-200 p-4">
        <svg viewBox="0 0 320 240" className="w-full max-w-xs h-auto">
          {/* Sector fill */}
          <path
            d="M 160 120 L 245 120 A 85 85 0 0 0 202.5 46.4 Z"
            fill={selectedPart === 'sector' ? 'rgba(124, 58, 237, 0.28)' : 'rgba(124, 58, 237, 0.06)'}
            stroke={selectedPart === 'sector' ? '#7C3AED' : 'none'}
            strokeWidth="2.5"
          />
          {/* Main circle */}
          <circle cx="160" cy="120" r="85" fill="none" stroke="#334155" strokeWidth="2.5" />
          {/* Highlighted Arc */}
          <path
            d="M 245 120 A 85 85 0 0 0 202.5 46.4"
            fill="none"
            stroke="#E11D48"
            strokeWidth={selectedPart === 'arc' ? '6' : '2.5'}
          />
          {/* Diameter */}
          <line
            x1="75"
            y1="120"
            x2="245"
            y2="120"
            stroke="#0D9488"
            strokeWidth={selectedPart === 'diameter' ? '5' : '2'}
            strokeDasharray={selectedPart === 'diameter' ? 'none' : '4 3'}
          />
          {/* Radius */}
          <line
            x1="160"
            y1="120"
            x2="202.5"
            y2="46.4"
            stroke="#13519C"
            strokeWidth={selectedPart === 'radius' || selectedPart === 'sector' ? '5' : '2.5'}
          />
          {/* Chord */}
          <line
            x1="95"
            y1="175"
            x2="225"
            y2="175"
            stroke="#D97706"
            strokeWidth={selectedPart === 'chord' ? '5' : '2.5'}
          />
          {/* Centre O */}
          <circle cx="160" cy="120" r="4.5" fill="#0F172A" />
          <text x="148" y="112" fontSize="12" fontWeight="bold" fill="#0F172A">O</text>
          <text x="186" y="82" fontSize="11" fontWeight="bold" fill="#13519C">r</text>
          <text x="115" y="136" fontSize="11" fontWeight="bold" fill="#0D9488">d = 2r</text>
          <text x="142" y="192" fontSize="11" fontWeight="bold" fill="#D97706">Chord</text>
          <text x="235" y="75" fontSize="11" fontWeight="bold" fill="#E11D48">Arc</text>
        </svg>
      </div>

      <div className="p-3.5 rounded-xl bg-indigo-50/70 border border-indigo-200 space-y-1">
        <div className="flex items-center justify-between">
          <span className="text-xs font-extrabold text-slate-900">{active.label}</span>
          <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-white border border-slate-200 text-[#13519C]">
            {active.formula}
          </span>
        </div>
        <p className="text-xs text-slate-700 leading-relaxed">{active.desc}</p>
      </div>
    </div>
  );
}

/**
 * 2. IntegerNumberLineHopperAid (Maths #37)
 * Interactive Number Line for Adding & Subtracting Positive and Negative Integers
 */
export function IntegerNumberLineHopperAid() {
  const [startVal, setStartVal] = useState(-4);
  const [stepVal, setStepVal] = useState(7);
  const resultVal = startVal + stepVal;
  const ticks = Array.from({ length: 21 }, (_, i) => i - 10);

  const xFor = (n) => 30 + ((n + 10) / 20) * 440;
  const xStart = xFor(Math.max(-10, Math.min(10, startVal)));
  const xEnd = xFor(Math.max(-10, Math.min(10, resultVal)));
  const midX = (xStart + xEnd) / 2;

  return (
    <div data-testid="integer-number-line-aid" className="bg-white rounded-2xl border border-slate-200 p-4 space-y-4 text-slate-800">
      <div className="grid grid-cols-2 gap-3">
        <label className="bg-slate-50 p-2.5 rounded-xl border border-slate-200 flex flex-col gap-1">
          <div className="flex justify-between text-xs font-bold">
            <span>Start Integer:</span>
            <span className="font-mono text-[#13519C]">{startVal}</span>
          </div>
          <input
            type="range"
            min="-9"
            max="9"
            value={startVal}
            onChange={(e) => setStartVal(Number(e.target.value))}
            className="accent-[#13519C] cursor-pointer"
          />
        </label>
        <label className="bg-slate-50 p-2.5 rounded-xl border border-slate-200 flex flex-col gap-1">
          <div className="flex justify-between text-xs font-bold">
            <span>Jump (Add / Subtract):</span>
            <span className={`font-mono ${stepVal >= 0 ? 'text-emerald-700' : 'text-rose-700'}`}>
              {stepVal >= 0 ? `+${stepVal} (Right →)` : `${stepVal} (← Left)`}
            </span>
          </div>
          <input
            type="range"
            min="-9"
            max="9"
            value={stepVal}
            onChange={(e) => setStepVal(Number(e.target.value))}
            className="accent-emerald-600 cursor-pointer"
          />
        </label>
      </div>

      <div className="bg-slate-50 rounded-xl border border-slate-200 p-3 overflow-x-auto">
        <svg viewBox="0 0 500 130" className="w-full min-w-[380px] h-auto">
          <line x1="20" y1="85" x2="480" y2="85" stroke="#334155" strokeWidth="2.5" />
          {ticks.map((t) => {
            const x = xFor(t);
            return (
              <g key={t}>
                <line x1={x} y1={t === 0 ? 75 : 80} x2={x} y2={t === 0 ? 95 : 90} stroke={t === 0 ? '#0F172A' : '#64748B'} strokeWidth={t === 0 ? '2.5' : '1.5'} />
                <text x={x} y="108" textAnchor="middle" fontSize="10" fontWeight={t === 0 ? 'bold' : 'normal'} fill={t < 0 ? '#BE123C' : t > 0 ? '#047857' : '#0F172A'}>
                  {t}
                </text>
              </g>
            );
          })}
          {stepVal !== 0 && (
            <path
              d={`M ${xStart} 82 Q ${midX} 22 ${xEnd} 82`}
              fill="none"
              stroke={stepVal > 0 ? '#059669' : '#E11D48'}
              strokeWidth="3"
              strokeDasharray="5 3"
            />
          )}
          <circle cx={xStart} cy="85" r="6" fill="#13519C" />
          <circle cx={xEnd} cy="85" r="7" fill={stepVal >= 0 ? '#059669' : '#E11D48'} />
          <text x={midX} y="38" textAnchor="middle" fontSize="12" fontWeight="bold" fill={stepVal >= 0 ? '#059669' : '#E11D48'}>
            {stepVal >= 0 ? `+${stepVal} hops right` : `${stepVal} hops left`}
          </text>
        </svg>
      </div>

      <div className="p-3 rounded-xl bg-indigo-50 border border-indigo-200 text-center font-mono text-sm font-bold text-slate-900">
        ({startVal}) {stepVal >= 0 ? `+ ${stepVal}` : `- ${Math.abs(stepVal)}`} = <span className="text-[#13519C] text-base">{resultVal}</span>
      </div>
    </div>
  );
}

/**
 * 3. AcidBaseLitmusSimulatorAid (NS #1)
 * Interactive Litmus Paper & pH Scale Testing Lab
 */
export function AcidBaseLitmusSimulatorAid() {
  const SUBSTANCES = [
    { id: 'lemon', name: 'Lemon Juice / Vinegar', ph: 2.5, type: 'Acid', redLitmus: 'Stays Red', blueLitmus: 'Turns Red', feel: 'Sour taste, corrosive' },
    { id: 'hcl', name: 'Stomach Acid (HCl)', ph: 1.5, type: 'Strong Acid', redLitmus: 'Stays Red', blueLitmus: 'Turns Red', feel: 'Highly corrosive' },
    { id: 'water', name: 'Pure Distilled Water', ph: 7.0, type: 'Neutral', redLitmus: 'Stays Red', blueLitmus: 'Stays Blue', feel: 'Neither acidic nor basic' },
    { id: 'salt', name: 'Table Salt Solution', ph: 7.0, type: 'Neutral', redLitmus: 'Stays Red', blueLitmus: 'Stays Blue', feel: 'Formed by neutralisation' },
    { id: 'bicarb', name: 'Bicarbonate of Soda', ph: 9.0, type: 'Weak Base', redLitmus: 'Turns Blue', blueLitmus: 'Stays Blue', feel: 'Bitter, slippery feel' },
    { id: 'soap', name: 'Soap / Bleach Solution', ph: 12.0, type: 'Strong Base', redLitmus: 'Turns Blue', blueLitmus: 'Stays Blue', feel: 'Slippery/soapy, corrosive' },
  ];
  const [selected, setSelected] = useState(SUBSTANCES[0]);

  const isAcid = selected.ph < 7;
  const isBase = selected.ph > 7;

  return (
    <div data-testid="acid-base-litmus-aid" className="bg-white rounded-2xl border border-slate-200 p-4 space-y-4 text-slate-800">
      <div className="grid grid-cols-2 sm:grid-cols-3 gap-1.5">
        {SUBSTANCES.map((s) => (
          <button
            key={s.id}
            type="button"
            onClick={() => setSelected(s)}
            className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold text-left border transition-all cursor-pointer ${
              selected.id === s.id
                ? 'bg-[#13519C] text-white border-[#13519C]'
                : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
            }`}
          >
            {s.name}
          </button>
        ))}
      </div>

      <div className="bg-slate-50 rounded-xl border border-slate-200 p-4 flex flex-col items-center">
        <svg viewBox="0 0 320 180" className="w-full max-w-xs h-auto">
          {/* Beaker */}
          <path d="M 90 40 L 90 155 Q 90 165 100 165 L 220 165 Q 230 165 230 155 L 230 40" fill="none" stroke="#334155" strokeWidth="3" />
          {/* Solution liquid */}
          <path
            d="M 92 85 L 228 85 L 228 154 Q 228 163 219 163 L 101 163 Q 92 163 92 154 Z"
            fill={isAcid ? 'rgba(244, 63, 94, 0.18)' : isBase ? 'rgba(59, 130, 246, 0.18)' : 'rgba(16, 185, 129, 0.15)'}
          />
          {/* Red Litmus Strip */}
          <rect x="125" y="20" width="22" height="65" fill="#FCA5A5" stroke="#991B1B" strokeWidth="1.5" />
          <rect x="125" y="85" width="22" height="50" fill={isBase ? '#3B82F6' : '#EF4444'} stroke="#991B1B" strokeWidth="1.5" />
          <text x="136" y="15" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#991B1B">Red Litmus</text>

          {/* Blue Litmus Strip */}
          <rect x="175" y="20" width="22" height="65" fill="#93C5FD" stroke="#1E3A8A" strokeWidth="1.5" />
          <rect x="175" y="85" width="22" height="50" fill={isAcid ? '#EF4444' : '#3B82F6'} stroke="#1E3A8A" strokeWidth="1.5" />
          <text x="186" y="15" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#1E3A8A">Blue Litmus</text>
        </svg>
      </div>

      <div className="grid grid-cols-3 gap-2 text-center text-xs">
        <div className="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
          <div className="text-[10px] uppercase text-slate-500 font-bold">Classification</div>
          <div className="font-extrabold text-slate-900 mt-0.5">{selected.type} (pH {selected.ph})</div>
        </div>
        <div className="p-2.5 rounded-xl bg-rose-50 border border-rose-200">
          <div className="text-[10px] uppercase text-rose-700 font-bold">Red Litmus</div>
          <div className="font-extrabold text-rose-900 mt-0.5">{selected.redLitmus}</div>
        </div>
        <div className="p-2.5 rounded-xl bg-blue-50 border border-blue-200">
          <div className="text-[10px] uppercase text-blue-700 font-bold">Blue Litmus</div>
          <div className="font-extrabold text-blue-900 mt-0.5">{selected.blueLitmus}</div>
        </div>
      </div>
    </div>
  );
}

/**
 * 4. HeatTransferThermosSimulatorAid (NS #8)
 * Interactive Conduction, Convection, Radiation & Vacuum Flask Cutaway Simulator
 */
export function HeatTransferThermosSimulatorAid() {
  const [mode, setMode] = useState('conduction');

  const MODES = {
    conduction: {
      title: 'Conduction (Solids)',
      desc: 'Heat transfers through direct particle-to-particle vibrations in solids. Metals are good thermal conductors; plastic/wood/air are thermal insulators.',
    },
    convection: {
      title: 'Convection (Liquids & Gases)',
      desc: 'Heated fluid expands, becomes less dense, and rises while cooler, denser fluid sinks — forming a continuous convection current.',
    },
    radiation: {
      title: 'Radiation (Electromagnetic Waves)',
      desc: 'Heat travels as infrared waves through empty space (vacuum) without needing particles. Shiny silver surfaces reflect radiation; matt black absorbs it.',
    },
    thermos: {
      title: 'Vacuum Flask (Thermos) Insulation',
      desc: 'Combines 3 barriers: (1) Vacuum stops conduction & convection, (2) Silvered walls reflect infrared radiation, (3) Plastic stopper reduces convection.',
    },
  };

  return (
    <div data-testid="heat-transfer-thermos-aid" className="bg-white rounded-2xl border border-slate-200 p-4 space-y-4 text-slate-800">
      <div className="flex flex-wrap gap-1.5">
        {Object.entries(MODES).map(([k, v]) => (
          <button
            key={k}
            type="button"
            onClick={() => setMode(k)}
            className={`px-2.5 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
              mode === k ? 'bg-[#13519C] text-white' : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
            }`}
          >
            {v.title.split(' ')[0]}
          </button>
        ))}
      </div>

      <div className="bg-slate-50 rounded-xl border border-slate-200 p-4 flex justify-center">
        <svg viewBox="0 0 340 180" className="w-full max-w-sm h-auto">
          {mode === 'conduction' && (
            <g>
              <rect x="40" y="75" width="200" height="22" rx="4" fill="url(#condGrad)" stroke="#334155" strokeWidth="2" />
              <defs>
                <linearGradient id="condGrad" x1="0" y1="0" x2="1" y2="0">
                  <stop offset="0%" stopColor="#EF4444" />
                  <stop offset="50%" stopColor="#F59E0B" />
                  <stop offset="100%" stopColor="#60A5FA" />
                </linearGradient>
              </defs>
              <rect x="240" y="70" width="60" height="32" rx="6" fill="#78350F" />
              <text x="270" y="90" textAnchor="middle" fontSize="10" fill="#FFF" fontWeight="bold">Wood Handle</text>
              <path d="M 55 135 Q 45 110 55 98 Q 65 110 55 135" fill="#F97316" />
              <text x="140" y="60" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#B91C1C">Particle vibration → → →</text>
            </g>
          )}
          {mode === 'convection' && (
            <g>
              <rect x="95" y="30" width="150" height="115" rx="6" fill="#EFF6FF" stroke="#334155" strokeWidth="2.5" />
              <path d="M 140 125 L 140 55 L 115 55 L 115 125" fill="none" stroke="#EF4444" strokeWidth="3" strokeDasharray="4 2" />
              <path d="M 200 125 L 200 55 L 225 55 L 225 125" fill="none" stroke="#3B82F6" strokeWidth="3" strokeDasharray="4 2" />
              <text x="170" y="85" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#EF4444">↑ Warm rises</text>
              <text x="170" y="105" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#1D4ED8">↓ Cool sinks</text>
              <path d="M 170 170 Q 158 150 170 145 Q 182 150 170 170" fill="#F97316" />
            </g>
          )}
          {mode === 'radiation' && (
            <g>
              <circle cx="65" cy="90" r="28" fill="#F59E0B" />
              <text x="65" y="94" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#FFF">Heat Source</text>
              <path d="M 105 75 Q 130 65 155 75 T 205 75" fill="none" stroke="#EF4444" strokeWidth="2.5" />
              <path d="M 105 105 Q 130 95 155 105 T 205 105" fill="none" stroke="#EF4444" strokeWidth="2.5" />
              <rect x="215" y="40" width="35" height="45" fill="#0F172A" />
              <text x="275" y="65" fontSize="10" fontWeight="bold" fill="#0F172A">Black: Absorbs</text>
              <rect x="215" y="95" width="35" height="45" fill="#E2E8F0" stroke="#64748B" strokeWidth="2" />
              <text x="275" y="120" fontSize="10" fontWeight="bold" fill="#475569">Silver: Reflects</text>
            </g>
          )}
          {mode === 'thermos' && (
            <g>
              <rect x="115" y="18" width="70" height="18" rx="3" fill="#475569" />
              <rect x="100" y="36" width="100" height="130" rx="10" fill="#E2E8F0" stroke="#334155" strokeWidth="2.5" />
              <rect x="112" y="46" width="76" height="110" rx="6" fill="#FEE2E2" stroke="#94A3B8" strokeWidth="3" />
              <text x="150" y="100" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#991B1B">Hot Liquid</text>
              <text x="255" y="30" fontSize="10" fontWeight="bold" fill="#334155">1. Plastic Stopper</text>
              <text x="255" y="80" fontSize="10" fontWeight="bold" fill="#13519C">2. Vacuum Gap</text>
              <text x="255" y="130" fontSize="10" fontWeight="bold" fill="#0D9488">3. Silvered Walls</text>
            </g>
          )}
        </svg>
      </div>

      <div className="p-3 rounded-xl bg-amber-50 border border-amber-200 text-xs text-slate-800 leading-relaxed">
        <strong className="block text-amber-900 mb-0.5">{MODES[mode].title}</strong>
        {MODES[mode].desc}
      </div>
    </div>
  );
}

/**
 * 5. EarthMoonSunSeasonsTidesAid (NS #12)
 * Interactive Earth 23.5° Tilt Seasons & Spring/Neap Tides Simulator
 */
export function EarthMoonSunSeasonsTidesAid() {
  const [month, setMonth] = useState('december');

  const SEASONS = {
    december: {
      title: 'December Solstice (Southern Hemisphere Summer)',
      sh: 'Summer (Tilted TOWARDS the Sun — direct rays, longer days)',
      nh: 'Winter (Tilted AWAY from the Sun — oblique rays, shorter days)',
      tide: 'Spring Tide occurs at New Moon & Full Moon (Sun, Earth, Moon aligned in a straight line).',
    },
    june: {
      title: 'June Solstice (Southern Hemisphere Winter)',
      sh: 'Winter (Tilted AWAY from the Sun — oblique rays, shorter days)',
      nh: 'Summer (Tilted TOWARDS the Sun — direct rays, longer days)',
      tide: 'Neap Tide occurs at First & Third Quarter Moon (Sun and Moon pull at 90° right angles).',
    },
    equinox: {
      title: 'March / September Equinox (Autumn & Spring)',
      sh: 'Equal 12-hour day and 12-hour night across both hemispheres (Sun directly over Equator).',
      nh: 'Equal 12-hour day and 12-hour night across both hemispheres.',
      tide: 'Gravitational pull of the Moon (and Sun) creates two tidal bulges on opposite sides of Earth.',
    },
  };

  const active = SEASONS[month] || SEASONS.december;

  return (
    <div data-testid="earth-seasons-tides-aid" className="bg-white rounded-2xl border border-slate-200 p-4 space-y-4 text-slate-800">
      <div className="flex flex-wrap gap-1.5">
        <button
          type="button"
          onClick={() => setMonth('december')}
          className={`px-3 py-1.5 rounded-lg text-xs font-bold cursor-pointer ${month === 'december' ? 'bg-[#13519C] text-white' : 'bg-slate-100 text-slate-700'}`}
        >
          December (SA Summer)
        </button>
        <button
          type="button"
          onClick={() => setMonth('june')}
          className={`px-3 py-1.5 rounded-lg text-xs font-bold cursor-pointer ${month === 'june' ? 'bg-[#13519C] text-white' : 'bg-slate-100 text-slate-700'}`}
        >
          June (SA Winter)
        </button>
        <button
          type="button"
          onClick={() => setMonth('equinox')}
          className={`px-3 py-1.5 rounded-lg text-xs font-bold cursor-pointer ${month === 'equinox' ? 'bg-[#13519C] text-white' : 'bg-slate-100 text-slate-700'}`}
        >
          Equinox & Tides
        </button>
      </div>

      <div className="bg-slate-900 rounded-xl p-4 flex justify-center">
        <svg viewBox="0 0 340 170" className="w-full max-w-sm h-auto">
          {/* Sun */}
          <circle cx="55" cy="85" r="32" fill="#FACC15" />
          <text x="55" y="89" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#713F12">SUN</text>
          {/* Solar rays */}
          <line x1="95" y1="65" x2="195" y2="65" stroke="#FDE047" strokeWidth="2" strokeDasharray="5 3" />
          <line x1="95" y1="85" x2="195" y2="85" stroke="#FDE047" strokeWidth="2.5" />
          <line x1="95" y1="105" x2="195" y2="105" stroke="#FDE047" strokeWidth="2" strokeDasharray="5 3" />

          {/* Tilted Earth (23.5 deg) */}
          <g transform={`translate(235, 85) rotate(${month === 'december' ? 23.5 : month === 'june' ? -23.5 : 0})`}>
            <line x1="0" y1="-52" x2="0" y2="52" stroke="#94A3B8" strokeWidth="2" strokeDasharray="3 2" />
            <circle cx="0" cy="0" r="36" fill="#2563EB" stroke="#93C5FD" strokeWidth="2" />
            <line x1="-36" y1="0" x2="36" y2="0" stroke="#F8FAFC" strokeWidth="1.5" strokeDasharray="3 2" />
            <text x="0" y="-14" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#FFF">NH</text>
            <text x="0" y="20" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#FDE047">SH (SA)</text>
          </g>
          <text x="235" y="155" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#E2E8F0">
            23,5° Axial Tilt
          </text>
        </svg>
      </div>

      <div className="p-3 rounded-xl bg-indigo-50 border border-indigo-200 text-xs space-y-1">
        <div className="font-bold text-slate-900">{active.title}</div>
        <div><strong>Southern Hemisphere (SA):</strong> {active.sh}</div>
        <div><strong>Northern Hemisphere:</strong> {active.nh}</div>
        <div className="text-indigo-800 pt-1"><strong>Tides Note:</strong> {active.tide}</div>
      </div>
    </div>
  );
}
