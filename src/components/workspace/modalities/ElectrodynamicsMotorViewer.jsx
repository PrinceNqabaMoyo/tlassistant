import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Zap, Play, Pause, Gauge, Activity } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import AtlasSyncChartSvg from '../shared/atlas3d/AtlasSyncChartSvg';
import { createBlock3D, createVectorArrow3D } from '../shared/atlas3d/atlasPartsKit';
import { createPaperMaterial, addInkEdges } from '../shared/atlas3d/atlasRenderEngine';

export default function ElectrodynamicsMotorViewer({
  defaultMode = 'ac_generator', // 'ac_generator' | 'dc_motor'
}) {
  const [mode, setMode] = useState(defaultMode);
  const [isRunning, setIsRunning] = useState(true);
  const [frequency, setFrequency] = useState(0.8); // Hz
  const [coilAngleDeg, setCoilAngleDeg] = useState(45);
  const [selectedId, setSelectedId] = useState('faraday_emf');

  const vMax = 12.0; // V
  const rad = (coilAngleDeg * Math.PI) / 180;
  const rawSin = Math.sin(rad);
  const currentEmf = (mode === 'dc_motor' ? Math.abs(rawSin) : rawSin) * vMax;
  const fluxRatio = Math.cos(rad);

  const calculationsMap = useMemo(() => {
    return {
      faraday_emf: {
        id: 'faraday_emf',
        symbol: '\\varepsilon(t)',
        label: mode === 'ac_generator'
          ? 'AC Generator Induced EMF (Slip Rings)'
          : 'DC Output / Split-Ring Commutator Rectification',
        color: mode === 'ac_generator' ? '#2B5B84' : '#D97706',
        badgeText: `ε = ${currentEmf.toFixed(1)} V`,
        formula: mode === 'ac_generator'
          ? '\\varepsilon = -N\\frac{\\Delta \\Phi}{\\Delta t} = \\varepsilon_{\\max} \\sin(\\theta)'
          : '\\varepsilon_{\\text{DC}} = |\\varepsilon_{\\max} \\sin(\\theta)| \\quad \\text{and} \\quad F = B I L \\sin\\theta',
        substitution: `\\varepsilon = (${vMax.toFixed(1)}\\text{ V}) \\cdot ${
          mode === 'dc_motor' ? `|\\sin(${coilAngleDeg}^\\circ)|` : `\\sin(${coilAngleDeg}^\\circ)`
        }`,
        result: `\\varepsilon = ${currentEmf.toFixed(2)}\\text{ V at } \\theta = ${coilAngleDeg}^\\circ`,
        meaning: mode === 'ac_generator'
          ? 'Two continuous slip rings maintain unbroken contact with each coil side, producing a sinusoidal alternating EMF that reverses polarity every 180°.'
          : 'A split-ring commutator swaps brush contact every half-turn when the coil passes the vertical neutral plane, keeping current/torque unidirectional.',
      },
      magnetic_flux: {
        id: 'magnetic_flux',
        symbol: '\\Phi = B A \\cos\\theta',
        label: 'Magnetic Flux Linkage vs. Rate of Change',
        color: '#2D6A4F',
        badgeText: `Φ = ${(fluxRatio * 100).toFixed(0)}% Φmax`,
        formula: '\\Phi = B A \\cos\\theta \\quad \\text{(Maximum EMF when } \\Phi = 0\\text{!)}',
        substitution: `\\Phi(\\theta=${coilAngleDeg}^\\circ) = \\Phi_{\\max}\\cos(${coilAngleDeg}^\\circ) = ${(fluxRatio).toFixed(2)}\\,\\Phi_{\\max}`,
        result: `\\frac{\\Delta \\Phi}{\\Delta t} \\propto \\sin(${coilAngleDeg}^\\circ) = ${Math.abs(rawSin).toFixed(2)}`,
        meaning: 'When the coil is horizontal (θ = 90°), flux linkage Φ is zero, but the coil sides cut perpendicular to the magnetic field lines B at maximum rate—producing maximum induced EMF!',
      },
    };
  }, [coilAngleDeg, currentEmf, fluxRatio, mode, rawSin]);

  const activeCalculation = calculationsMap[selectedId] || calculationsMap.faraday_emf;

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    // North Pole (Left) & South Pole (Right)
    const nPole = createBlock3D({
      width: 0.75,
      height: 1.4,
      depth: 1.2,
      color: 0xB8432E,
      interactiveId: 'magnetic_flux',
    });
    nPole.position.set(-1.95, 0.85, 0);
    root.add(nPole);

    const sPole = createBlock3D({
      width: 0.75,
      height: 1.4,
      depth: 1.2,
      color: 0x2B5B84,
      interactiveId: 'magnetic_flux',
    });
    sPole.position.set(1.95, 0.85, 0);
    root.add(sPole);

    // Magnetic Field Lines B from N to S
    for (let z = -0.35; z <= 0.35; z += 0.35) {
      const bArrow = createVectorArrow3D({
        origin: [-1.45, 0.85, z],
        direction: [1, 0, 0],
        length: 2.8,
        color: 0x2D6A4F,
        interactiveId: 'magnetic_flux',
      });
      root.add(bArrow);
    }

    // Rotating Armature Coil Group
    const coilGroup = new THREE.Group();
    coilGroup.position.set(0, 0.85, 0);
    coilGroup.rotation.z = (coilAngleDeg * Math.PI) / 180;
    coilGroup.userData = { interactiveId: 'faraday_emf', labelPoint: [0, 0.9, 0] };

    const armL = createBlock3D({ width: 0.12, height: 0.12, depth: 1.35, color: 0xD97706, interactiveId: 'faraday_emf' });
    armL.position.set(-0.65, 0, 0);
    const armR = createBlock3D({ width: 0.12, height: 0.12, depth: 1.35, color: 0xD97706, interactiveId: 'faraday_emf' });
    armR.position.set(0.65, 0, 0);
    const armBack = createBlock3D({ width: 1.4, height: 0.12, depth: 0.12, color: 0xD97706, interactiveId: 'faraday_emf' });
    armBack.position.set(0, 0, -0.65);
    coilGroup.add(armL, armR, armBack);

    // Slip rings vs Split-ring commutator at front (+z)
    const ringGeo = new THREE.TorusGeometry(0.24, 0.045, 12, 32);
    const ringMat = createPaperMaterial(mode === 'ac_generator' ? 0x0EA5E9 : 0xF97316);
    const ring1 = new THREE.Mesh(ringGeo, ringMat);
    addInkEdges(ring1, 0x1E1B18, 0.6);
    ring1.position.set(0, 0, 0.78);
    coilGroup.add(ring1);

    root.add(coilGroup);

    return {
      interactiveObjects: [root],
      update: (dt) => {
        if (isRunning) {
          coilGroup.rotation.z += dt * frequency * Math.PI * 1.5;
        }
      },
    };
  }, [coilAngleDeg, frequency, isRunning, mode]);

  // Synchronized EMF waveform ε(θ) and Flux Φ(θ)
  const waveSeries = useMemo(() => {
    const emfPts = [];
    const fluxPts = [];
    for (let deg = 0; deg <= 360; deg += 10) {
      const r = (deg * Math.PI) / 180;
      const eVal = (mode === 'dc_motor' ? Math.abs(Math.sin(r)) : Math.sin(r)) * vMax;
      emfPts.push({ x: deg, y: eVal });
      fluxPts.push({ x: deg, y: Math.cos(r) * vMax * 0.75 });
    }
    return [
      { id: 'emf', label: 'Induced EMF ε(θ)', color: mode === 'ac_generator' ? '#2B5B84' : '#D97706', points: emfPts },
      { id: 'flux', label: 'Magnetic Flux Φ(θ)', color: '#2D6A4F', dashed: true, points: fluxPts },
    ];
  }, [mode]);

  return (
    <div data-testid="electrodynamics-canvas" className="w-full bg-white text-slate-800 rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col select-none space-y-3 p-3.5">
      {/* Top Header */}
      <div className="flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-sky-50 text-sky-700 border border-sky-200 flex items-center justify-center">
            <Zap className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold tracking-tight text-slate-900 flex items-center gap-1.5">
              3D Electrodynamics Armature & Faraday Flux Explorer
            </h3>
            <p className="text-[11px] text-slate-500">
              Fleming&apos;s Hand Rules • Slip Rings vs Split-Ring Commutator • Live ε(θ) & Φ(θ)
            </p>
          </div>
        </div>

        {/* Generator / Motor Mode Toggle */}
        <div className="flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200">
          <button
            data-testid="btn-mode-ac-generator"
            onClick={() => setMode('ac_generator')}
            className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
              mode === 'ac_generator'
                ? 'bg-[#2B5B84] text-white shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            AC Generator (Slip Rings)
          </button>
          <button
            data-testid="btn-mode-dc-motor"
            onClick={() => setMode('dc_motor')}
            className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
              mode === 'dc_motor'
                ? 'bg-amber-600 text-white shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            DC Motor / Split Ring
          </button>
        </div>
      </div>

      {/* Angle & Frequency Controls */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
        <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
          <div className="flex justify-between text-[11px] font-semibold text-slate-600">
            <span>Inspect Coil Angle (θ)</span>
            <span className="font-mono font-bold text-[#2B5B84]">{coilAngleDeg}° (ε = {currentEmf.toFixed(1)} V)</span>
          </div>
          <input
            type="range"
            min="0"
            max="360"
            step="15"
            value={coilAngleDeg}
            onChange={(e) => {
              setIsRunning(false);
              setCoilAngleDeg(parseInt(e.target.value, 10));
            }}
            className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
          />
        </label>

        <div className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex items-center justify-between gap-2">
          <div className="flex items-center gap-1.5 text-[11px] font-mono text-slate-600">
            <Gauge className="w-3.5 h-3.5 text-slate-500" />
            <span>Freq:</span>
            <input
              type="range"
              min="0.2"
              max="2.0"
              step="0.1"
              value={frequency}
              onChange={(e) => setFrequency(parseFloat(e.target.value))}
              className="w-20 accent-[#2B5B84] cursor-pointer h-1.5"
            />
            <span className="text-slate-900 font-bold">{frequency.toFixed(1)} Hz</span>
          </div>
          <button
            type="button"
            onClick={() => setIsRunning(!isRunning)}
            className="px-2.5 py-1 rounded-lg bg-slate-200 hover:bg-slate-300 text-slate-800 text-xs font-semibold flex items-center gap-1"
          >
            {isRunning ? <Pause className="w-3 h-3" /> : <Play className="w-3 h-3" />}
            {isRunning ? 'Pause' : 'Rotate'}
          </button>
        </div>
      </div>

      {/* 3D Paper & Ink Viewport */}
      <AtlasCanvas3D
        testId="electrodynamics-3d-stage"
        height={270}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle="Click the rotating armature coil or magnetic field lines B to inspect Faraday's Law & flux linkage"
      />

      {/* Interactive Calculation Popover */}
      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />

      {/* Synchronized Oscilloscope Waveform */}
      <AtlasSyncChartSvg
        title="Synchronized Oscilloscope: Induced EMF ε(θ) vs. Magnetic Flux Φ(θ)"
        xLabel="Coil Rotation Angle θ (degrees)"
        yLabel="Voltage (V)"
        xDomain={[0, 360]}
        yDomain={[-14, 14]}
        series={waveSeries}
        activePoint={{
          x: coilAngleDeg,
          y: currentEmf,
          label: `ε = ${currentEmf.toFixed(1)} V`,
          color: mode === 'ac_generator' ? '#2B5B84' : '#D97706',
        }}
      />
    </div>
  );
}
