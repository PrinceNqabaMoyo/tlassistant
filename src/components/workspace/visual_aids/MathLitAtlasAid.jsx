import React, { useState } from 'react';
import { Compass, TrendingUp, Box, Layers, Sliders, MapPin, Calculator, Ruler } from 'lucide-react';

/**
 * MathLitAtlasAid — Dedicated Cognitive Sidecar Visual Aid for Mathematical Literacy (Grades 10–12).
 *
 * Implements Rule 0d-14 & Diagram Doctrine:
 * - Dual-tab architecture:
 *   * Tab 1: Annotated Master Atlas (Curriculum Symbols, Tax/Tariff Schematics & Packaging Nets)
 *   * Tab 2: Interactive Dynamic Exploration Lab (Scale Converter, Stepped Tariff Calculator & Packing Scrubber)
 */
export default function MathLitAtlasAid() {
  const [activeTab, setActiveTab] = useState('atlas'); // 'atlas' | 'interactive'
  const [activeAtlasSection, setActiveAtlasSection] = useState('maps'); // 'maps' | 'tariffs' | 'packaging'

  // Interactive state
  const [scaleRatio, setScaleRatio] = useState(100); // 1 : 100
  const [measuredCm, setMeasuredCm] = useState(5.5);
  const [waterUsageKL, setWaterUsageKL] = useState(18);
  const [cartonL, setCartonL] = useState(60);
  const [cartonW, setCartonW] = useState(40);
  const [cartonH, setCartonH] = useState(30);
  const [boxL, setBoxL] = useState(15);
  const [boxW, setBoxW] = useState(10);
  const [boxH, setBoxH] = useState(10);

  // Calculations
  const realDistanceMeters = (measuredCm * scaleRatio) / 100;
  const realDistanceKm = realDistanceMeters / 1000;

  // Water tariff stepped calculation (Typical SA municipal tariff)
  // 0-6 kL @ R 15,50; >6-15 kL @ R 24,00; >15-30 kL @ R 35,00; >30 kL @ R 50,00
  const calculateWaterTariff = (kl) => {
    let cost = 0;
    let b1 = Math.min(kl, 6);
    cost += b1 * 15.5;
    let b2 = Math.min(Math.max(kl - 6, 0), 9);
    cost += b2 * 24.0;
    let b3 = Math.min(Math.max(kl - 15, 0), 15);
    cost += b3 * 35.0;
    let b4 = Math.max(kl - 30, 0);
    cost += b4 * 50.0;
    return { cost, b1, b2, b3, b4 };
  };
  const waterTariff = calculateWaterTariff(waterUsageKL);

  // Packing capacity
  const countL = Math.max(1, Math.floor(cartonL / boxL));
  const countW = Math.max(1, Math.floor(cartonW / boxW));
  const countH = Math.max(1, Math.floor(cartonH / boxH));
  const totalBoxes = countL * countW * countH;

  return (
    <div data-testid="mathlit-atlas-aid" className="flex flex-col h-full bg-slate-50 text-slate-800 font-sans">
      {/* Top Header */}
      <div className="p-4 bg-white border-b border-slate-200 shadow-2xs">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <div className="p-2 bg-blue-50 text-blue-700 rounded-xl border border-blue-200">
              <Compass className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-sm font-bold text-slate-900 leading-tight">
                Mathematical Literacy Master Atlas
              </h2>
              <p className="text-[11px] text-slate-500">
                Maps, Plans, Tariffs, Tax Thresholds & Packaging Arrays
              </p>
            </div>
          </div>
          {/* Dual Tab Switcher */}
          <div className="flex p-0.5 bg-slate-100 rounded-xl border border-slate-200 text-xs font-semibold">
            <button
              onClick={() => setActiveTab('atlas')}
              className={`px-3 py-1 rounded-lg transition-all ${
                activeTab === 'atlas' ? 'bg-white text-blue-700 shadow-2xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              <span className="flex items-center gap-1.5">
                <Layers className="w-3.5 h-3.5" /> Annotated Atlas
              </span>
            </button>
            <button
              onClick={() => setActiveTab('interactive')}
              className={`px-3 py-1 rounded-lg transition-all ${
                activeTab === 'interactive' ? 'bg-white text-blue-700 shadow-2xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              <span className="flex items-center gap-1.5">
                <Sliders className="w-3.5 h-3.5" /> Interactive Lab
              </span>
            </button>
          </div>
        </div>
      </div>

      {/* Tab 1: Annotated Atlas */}
      {activeTab === 'atlas' && (
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {/* Sub-navigation pills */}
          <div className="flex gap-2">
            {[
              { id: 'maps', label: '1. Maps, Scale & Floor Plans', icon: Compass },
              { id: 'tariffs', label: '2. Tariffs & SARS Tax', icon: TrendingUp },
              { id: 'packaging', label: '3. Packaging & 3D Nets', icon: Box },
            ].map((sec) => (
              <button
                key={sec.id}
                onClick={() => setActiveAtlasSection(sec.id)}
                className={`px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 border transition-all ${
                  activeAtlasSection === sec.id
                    ? 'bg-blue-600 text-white border-blue-600 shadow-2xs'
                    : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-100'
                }`}
              >
                <sec.icon className="w-3.5 h-3.5" />
                {sec.label}
              </button>
            ))}
          </div>

          {/* Section 1: Maps & Floor Plans */}
          {activeAtlasSection === 'maps' && (
            <div className="space-y-4">
              <div className="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs">
                <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                  <Compass className="w-4 h-4 text-blue-600" /> Architectural Architectural Symbols & Scale Conventions
                </h3>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
                  <div className="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                    <span className="font-bold text-slate-800 block mb-1">Door Swing</span>
                    <span className="text-slate-600">Quarter-circle arc showing direction of door opening.</span>
                  </div>
                  <div className="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                    <span className="font-bold text-slate-800 block mb-1">Window Opening</span>
                    <span className="text-slate-600">Parallel double lines placed inside wall cuts.</span>
                  </div>
                  <div className="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                    <span className="font-bold text-slate-800 block mb-1">Number Scale</span>
                    <span className="text-slate-600 font-mono">1 : 50 (1 cm on paper = 50 cm reality).</span>
                  </div>
                  <div className="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                    <span className="font-bold text-slate-800 block mb-1">Bar Scale</span>
                    <span className="text-slate-600">Alternating dark/light segments measuring ground km.</span>
                  </div>
                </div>
              </div>

              {/* Graphic Compass Bearing Reference */}
              <div className="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs">
                <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider mb-2">
                  Three-Figure Compass Bearings (Measured Clockwise from True North)
                </h3>
                <div className="flex flex-wrap gap-2 text-xs font-mono font-semibold">
                  <span className="px-2.5 py-1 bg-red-50 text-red-700 rounded-lg border border-red-200">North: 000° / 360°</span>
                  <span className="px-2.5 py-1 bg-blue-50 text-blue-700 rounded-lg border border-blue-200">North-East: 045°</span>
                  <span className="px-2.5 py-1 bg-slate-100 text-slate-700 rounded-lg border border-slate-300">East: 090°</span>
                  <span className="px-2.5 py-1 bg-blue-50 text-blue-700 rounded-lg border border-blue-200">South-East: 135°</span>
                  <span className="px-2.5 py-1 bg-slate-100 text-slate-700 rounded-lg border border-slate-300">South: 180°</span>
                  <span className="px-2.5 py-1 bg-blue-50 text-blue-700 rounded-lg border border-blue-200">South-West: 225°</span>
                  <span className="px-2.5 py-1 bg-slate-100 text-slate-700 rounded-lg border border-slate-300">West: 270°</span>
                  <span className="px-2.5 py-1 bg-blue-50 text-blue-700 rounded-lg border border-blue-200">North-West: 315°</span>
                </div>
              </div>
            </div>
          )}

          {/* Section 2: Tariffs & Tax */}
          {activeAtlasSection === 'tariffs' && (
            <div className="space-y-4">
              <div className="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs">
                <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                  <TrendingUp className="w-4 h-4 text-emerald-600" /> Stepped Block Tariffs vs. Linear Cost Formulas
                </h3>
                <div className="space-y-2 text-xs text-slate-700 leading-relaxed">
                  <p>
                    <strong>Stepped (Piecewise) Tariffs:</strong> Water and electricity tariffs charge progressively higher rates per unit consumed as consumption crosses into higher tier blocks. The first block is not re-priced when entering higher blocks.
                  </p>
                  <p>
                    <strong>Linear Flat Rates:</strong> Formula: <code className="font-mono bg-slate-100 px-1 py-0.5 rounded">Total Cost = Fixed Monthly Admin Fee + (Unit Rate × Units)</code>. Represented by a single straight line with y-intercept.
                  </p>
                  <p>
                    <strong>UIF Statutory Deduction:</strong> 1% employee contribution capped at a monthly salary ceiling (e.g. R 17 712 / R 14 872 / R 12 478). Any earnings above this ceiling pay a fixed maximum monthly cap.
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* Section 3: Packaging & Nets */}
          {activeAtlasSection === 'packaging' && (
            <div className="space-y-4">
              <div className="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs">
                <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                  <Box className="w-4 h-4 text-indigo-600" /> 3D Packaging Capacity & Floor Space Conservation
                </h3>
                <div className="space-y-2 text-xs text-slate-700 leading-relaxed">
                  <p>
                    <strong>Box Packing Capacity Formula:</strong>
                  </p>
                  <div className="p-3 bg-slate-50 font-mono rounded-xl border border-slate-200 text-xs">
                    Number along Length = ⌊Carton Length ÷ Box Length⌋<br />
                    Number along Width = ⌊Carton Width ÷ Box Width⌋<br />
                    Number of Layers = ⌊Carton Height ÷ Box Height⌋<br />
                    <strong>Total Boxes = Length Count × Width Count × Layer Count</strong>
                  </div>
                  <p className="text-slate-500 text-[11px]">
                    *Note: Never divide total carton volume by box volume, because rigid boxes cannot be melted to fill empty residual space.
                  </p>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Tab 2: Interactive Lab */}
      {activeTab === 'interactive' && (
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {/* 1. Scale Calculator */}
          <div className="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs space-y-3">
            <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider flex items-center gap-1.5">
              <Ruler className="w-4 h-4 text-blue-600" /> Interactive Scale Converter
            </h3>
            <div className="grid grid-cols-2 gap-3 text-xs">
              <div>
                <label className="font-semibold text-slate-700 block mb-1">Scale Ratio (1 : X)</label>
                <input
                  type="range"
                  min="20"
                  max="1000"
                  step="10"
                  value={scaleRatio}
                  onChange={(e) => setScaleRatio(Number(e.target.value))}
                  className="w-full"
                />
                <span className="font-mono text-blue-700 font-bold">1 : {scaleRatio}</span>
              </div>
              <div>
                <label className="font-semibold text-slate-700 block mb-1">Ruler Measurement (cm)</label>
                <input
                  type="range"
                  min="0.5"
                  max="25"
                  step="0.5"
                  value={measuredCm}
                  onChange={(e) => setMeasuredCm(Number(e.target.value))}
                  className="w-full"
                />
                <span className="font-mono text-blue-700 font-bold">{measuredCm} cm</span>
              </div>
            </div>
            <div className="p-3 bg-blue-50 border border-blue-200 rounded-xl text-xs flex justify-between items-center font-mono">
              <span>Real Distance:</span>
              <strong className="text-blue-900 text-sm">
                {realDistanceMeters.toLocaleString('en-ZA', { maximumFractionDigits: 2 })} m ({realDistanceKm.toLocaleString('en-ZA', { maximumFractionDigits: 3 })} km)
              </strong>
            </div>
          </div>

          {/* 2. Municipal Stepped Tariff Scrubber */}
          <div className="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs space-y-3">
            <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider flex items-center gap-1.5">
              <TrendingUp className="w-4 h-4 text-emerald-600" /> Municipal Stepped Water Tariff Scrubber
            </h3>
            <div className="text-xs space-y-1">
              <label className="font-semibold text-slate-700 block">Monthly Consumption: {waterUsageKL} kL</label>
              <input
                type="range"
                min="0"
                max="50"
                step="1"
                value={waterUsageKL}
                onChange={(e) => setWaterUsageKL(Number(e.target.value))}
                className="w-full"
              />
            </div>
            <div className="grid grid-cols-4 gap-2 text-[11px] font-mono text-center">
              <div className="p-2 bg-slate-50 border border-slate-200 rounded-lg">
                <span className="text-slate-500 block">0–6 kL</span>
                <strong>{waterTariff.b1} kL</strong>
              </div>
              <div className="p-2 bg-slate-50 border border-slate-200 rounded-lg">
                <span className="text-slate-500 block">&gt;6–15 kL</span>
                <strong>{waterTariff.b2} kL</strong>
              </div>
              <div className="p-2 bg-slate-50 border border-slate-200 rounded-lg">
                <span className="text-slate-500 block">&gt;15–30 kL</span>
                <strong>{waterTariff.b3} kL</strong>
              </div>
              <div className="p-2 bg-slate-50 border border-slate-200 rounded-lg">
                <span className="text-slate-500 block">&gt;30 kL</span>
                <strong>{waterTariff.b4} kL</strong>
              </div>
            </div>
            <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-xl text-xs flex justify-between items-center font-mono">
              <span>Total Stepped Water Bill:</span>
              <strong className="text-emerald-900 text-sm">
                R {waterTariff.cost.toLocaleString('en-ZA', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
              </strong>
            </div>
          </div>

          {/* 3. Carton Packing Capacity Scrubber */}
          <div className="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs space-y-3">
            <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider flex items-center gap-1.5">
              <Box className="w-4 h-4 text-indigo-600" /> 3D Packaging Capacity Calculator
            </h3>
            <div className="grid grid-cols-2 gap-3 text-xs">
              <div>
                <span className="font-semibold text-slate-700 block mb-1">Outer Carton Dimensions (cm)</span>
                <span className="font-mono text-slate-600">{cartonL} cm × {cartonW} cm × {cartonH} cm</span>
              </div>
              <div>
                <span className="font-semibold text-slate-700 block mb-1">Inner Box Dimensions (cm)</span>
                <span className="font-mono text-slate-600">{boxL} cm × {boxW} cm × {boxH} cm</span>
              </div>
            </div>
            <div className="p-3 bg-indigo-50 border border-indigo-200 rounded-xl text-xs flex justify-between items-center font-mono">
              <span>Packing Capacity: {countL} × {countW} × {countH} =</span>
              <strong className="text-indigo-900 text-sm">
                {totalBoxes} individual boxes
              </strong>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
