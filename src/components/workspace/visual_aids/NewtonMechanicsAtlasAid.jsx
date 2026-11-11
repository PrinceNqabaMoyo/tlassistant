import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Compass, Layers, Sliders } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import AtlasSyncChartSvg from '../shared/atlas3d/AtlasSyncChartSvg';
import { createBlock3D, createInclinedRamp3D, createVectorArrow3D } from '../shared/atlas3d/atlasPartsKit';

/**
 * NewtonMechanicsAtlasAid
 * -----------------------
 * Grade 11–12 Physical Sciences & Technical Sciences:
 * 3D Inclined Plane & Two-Body Free-Body Vector Resolution Explorer.
 *
 * Every 3D force vector (Fg, Fg||, Fg⊥, FN, fk, Fapp, Fnet) is clickable/hoverable
 * and reveals its exact trigonometric substitution and numerical calculation in
 * CalculationPopoverCard.
 */

export default function NewtonMechanicsAtlasAid() {
  const [massKg, setMassKg] = useState(4.0);
  const [angleDeg, setAngleDeg] = useState(30);
  const [muK, setMuK] = useState(0.20);
  const [appliedForceN, setAppliedForceN] = useState(12.0);
  const [decomposeGravity, setDecomposeGravity] = useState(true);
  const [selectedId, setSelectedId] = useState('fg_parallel');

  const g = 9.8;

  const mechanicsMath = useMemo(() => {
    const rad = (angleDeg * Math.PI) / 180;
    const fg = massKg * g;
    const fgParallel = fg * Math.sin(rad);
    const fgPerp = fg * Math.cos(rad);
    const fNormal = fgPerp;
    const fkMax = muK * fNormal;

    // Net driving force along incline before friction (positive = up slope)
    const driveUp = appliedForceN - fgParallel;
    const fk = Math.min(Math.abs(driveUp), fkMax) * (driveUp >= 0 ? -1 : 1);
    const fNet = driveUp + fk;
    const accel = fNet / massKg;

    return {
      rad,
      fg,
      fgParallel,
      fgPerp,
      fNormal,
      fkMax,
      fkMagnitude: Math.abs(fk),
      fNet,
      accel,
    };
  }, [massKg, angleDeg, muK, appliedForceN]);

  const calculationsMap = useMemo(() => {
    const { fg, fgParallel, fgPerp, fNormal, fkMagnitude, fNet, accel } = mechanicsMath;
    return {
      fg_total: {
        id: 'fg_total',
        symbol: '\\vec{F}_g',
        label: 'Gravitational Force (Weight Straight Down)',
        color: '#475569',
        badgeText: `Fg = ${fg.toFixed(1)} N`,
        formula: 'F_g = m \\cdot g',
        substitution: `F_g = (${massKg.toFixed(1)}\\text{ kg})(9.8\\text{ m\\cdot s}^{-2})`,
        result: `F_g = ${fg.toFixed(2)}\\text{ N (downwards)}`,
        meaning: `Earth attracts the ${massKg.toFixed(1)} kg block vertically downwards toward the centre of the Earth. On an incline of θ = ${angleDeg}°, we resolve F_g into components parallel and perpendicular to the slope.`,
      },
      fg_parallel: {
        id: 'fg_parallel',
        symbol: 'F_{g\\parallel}',
        label: 'Parallel Weight Component (Down the Slope)',
        color: '#B8432E',
        badgeText: `Fg∥ = ${fgParallel.toFixed(1)} N`,
        formula: 'F_{g\\parallel} = m g \\sin\\theta',
        substitution: `F_{g\\parallel} = (${massKg.toFixed(1)})(9.8)\\sin(${angleDeg}^\\circ) = (${fg.toFixed(1)})(${Math.sin((angleDeg * Math.PI) / 180).toFixed(3)})`,
        result: `F_{g\\parallel} = ${fgParallel.toFixed(2)}\\text{ N down incline}`,
        meaning: `As incline angle θ increases, sin(${angleDeg}°) grows, pulling the block more strongly down the ramp.`,
      },
      fg_perp: {
        id: 'fg_perp',
        symbol: 'F_{g\\perp}',
        label: 'Perpendicular Weight Component (Into Ramp)',
        color: '#2B5B84',
        badgeText: `Fg⊥ = ${fgPerp.toFixed(1)} N`,
        formula: 'F_{g\\perp} = m g \\cos\\theta',
        substitution: `F_{g\\perp} = (${massKg.toFixed(1)})(9.8)\\cos(${angleDeg}^\\circ) = (${fg.toFixed(1)})(${Math.cos((angleDeg * Math.PI) / 180).toFixed(3)})`,
        result: `F_{g\\perp} = ${fgPerp.toFixed(2)}\\text{ N into surface}`,
        meaning: `Presses the block perpendicularly into the inclined plane surface and determines the normal force F_N.`,
      },
      f_normal: {
        id: 'f_normal',
        symbol: '\\vec{F}_N',
        label: 'Normal Reaction Force (Perpendicular to Surface)',
        color: '#2D6A4F',
        badgeText: `FN = ${fNormal.toFixed(1)} N`,
        formula: 'F_N = F_{g\\perp} = m g \\cos\\theta',
        substitution: `F_N = (${massKg.toFixed(1)})(9.8)\\cos(${angleDeg}^\\circ)`,
        result: `F_N = ${fNormal.toFixed(2)}\\text{ N}`,
        meaning: `Because there is zero acceleration perpendicular to the ramp surface, the normal force balances F_{g⊥} exactly.`,
      },
      f_friction: {
        id: 'f_friction',
        symbol: 'f_k',
        label: 'Kinetic Frictional Force (Opposing Motion)',
        color: '#D97706',
        badgeText: `fk = ${fkMagnitude.toFixed(1)} N`,
        formula: 'f_k = \\mu_k F_N = \\mu_k m g \\cos\\theta',
        substitution: `f_k = (${muK.toFixed(2)})(${fNormal.toFixed(2)}\\text{ N})`,
        result: `f_k = ${fkMagnitude.toFixed(2)}\\text{ N}`,
        meaning: `Microscopic surface interlocking opposes sliding motion along the plane and is directly proportional to the normal force F_N.`,
      },
      f_net: {
        id: 'f_net',
        symbol: '\\vec{F}_{\\text{net}}, \\vec{a}',
        label: "Newton's Second Law Along the Incline",
        color: '#7C3AED',
        badgeText: `a = ${accel.toFixed(2)} m/s²`,
        formula: 'F_{\\text{net}} = F_{\\text{app}} - F_{g\\parallel} \\pm f_k = m a',
        substitution: `${fNet.toFixed(2)}\\text{ N} = (${massKg.toFixed(1)}\\text{ kg}) \\cdot a`,
        result: `F_{\\text{net}} = ${fNet.toFixed(2)}\\text{ N},\\quad a = ${accel.toFixed(2)}\\text{ m\\cdot s}^{-2}`,
        meaning: accel >= 0
          ? `Net force acts UP the incline, accelerating the block upward at ${accel.toFixed(2)} m·s⁻².`
          : `Gravity overcomes the applied pull, accelerating the block DOWN the incline at ${Math.abs(accel).toFixed(2)} m·s⁻².`,
      },
    };
  }, [mechanicsMath, massKg, angleDeg, muK]);

  const activeCalculation = calculationsMap[selectedId] || calculationsMap.fg_parallel;

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    const { rad, fg, fgParallel, fgPerp, fNormal, fkMagnitude } = mechanicsMath;
    const rampRun = 3.8;
    const rampHeight = Math.max(0.35, Math.min(2.6, Math.tan(rad) * rampRun));
    const effAngle = Math.atan2(rampHeight, rampRun);

    // 1. Inclined wedge
    const rampMesh = createInclinedRamp3D({
      run: rampRun,
      height: rampHeight,
      depth: 1.5,
      color: 0xECE5D8,
    });
    rampMesh.position.set(-rampRun * 0.48, 0, -0.75);
    root.add(rampMesh);

    // 2. Block positioned mid-slope
    const sFrac = 0.52;
    const bx = -rampRun * 0.48 + rampRun * sFrac;
    const by = rampHeight * (1 - sFrac);

    const slopeGroup = new THREE.Group();
    slopeGroup.position.set(bx, by, 0);
    slopeGroup.rotation.z = -effAngle;
    root.add(slopeGroup);

    const blockH = 0.56;
    const blockMesh = createBlock3D({
      width: 0.85,
      height: blockH,
      depth: 0.68,
      color: 0xD97706,
      interactiveId: 'f_net',
    });
    blockMesh.position.set(0, blockH / 2, 0);
    slopeGroup.add(blockMesh);

    const vScale = 0.032; // N -> 3D world units
    const cmOrigin = [0, blockH / 2, 0];

    // Normal Force FN (along +y of slopeGroup)
    const fnLen = Math.max(0.55, fNormal * vScale);
    const fnArrow = createVectorArrow3D({
      origin: cmOrigin,
      direction: [0, 1, 0],
      length: fnLen,
      color: 0x2D6A4F,
      interactiveId: 'f_normal',
    });
    slopeGroup.add(fnArrow);

    // Parallel component Fg|| (down the slope: +x in slopeGroup since ramp slopes down toward +x)
    if (decomposeGravity) {
      const fgpLen = Math.max(0.45, fgParallel * vScale);
      const fgpArrow = createVectorArrow3D({
        origin: cmOrigin,
        direction: [1, 0, 0],
        length: fgpLen,
        color: 0xB8432E,
        interactiveId: 'fg_parallel',
      });
      slopeGroup.add(fgpArrow);

      // Perpendicular component Fg⊥ (into the slope: -y in slopeGroup)
      const fgPerpLen = Math.max(0.5, fgPerp * vScale);
      const fgPerpArrow = createVectorArrow3D({
        origin: cmOrigin,
        direction: [0, -1, 0],
        length: fgPerpLen,
        color: 0x2B5B84,
        interactiveId: 'fg_perp',
      });
      slopeGroup.add(fgPerpArrow);
    }

    // Total gravity Fg straight down in world coordinates
    const worldBlockCenter = new THREE.Vector3(0, blockH / 2, 0.22);
    slopeGroup.localToWorld(worldBlockCenter);
    const fgLen = Math.max(0.65, fg * vScale);
    const fgArrow = createVectorArrow3D({
      origin: [worldBlockCenter.x, worldBlockCenter.y, worldBlockCenter.z],
      direction: [0, -1, 0],
      length: fgLen,
      color: 0x475569,
      interactiveId: 'fg_total',
    });
    root.add(fgArrow);

    // Kinetic Friction fk along surface
    if (fkMagnitude > 0.2) {
      const fkDir = appliedForceN >= fgParallel ? 1 : -1;
      const fkArrow = createVectorArrow3D({
        origin: [0, 0.08, 0.28],
        direction: [fkDir, 0, 0],
        length: Math.max(0.4, fkMagnitude * vScale),
        color: 0xD97706,
        interactiveId: 'f_friction',
      });
      slopeGroup.add(fkArrow);
    }

    // Applied pull F_app up the slope (-x in slopeGroup)
    if (appliedForceN > 0.5) {
      const fAppArrow = createVectorArrow3D({
        origin: [-0.25, blockH / 2, 0],
        direction: [-1, 0, 0],
        length: Math.max(0.45, appliedForceN * vScale),
        color: 0x7C3AED,
        interactiveId: 'f_net',
      });
      slopeGroup.add(fAppArrow);
    }

    return {
      interactiveObjects: [root],
    };
  }, [mechanicsMath, decomposeGravity, appliedForceN]);

  // Synchronized chart showing how Fg|| (sin θ) and Fg⊥ (cos θ) vary from 0° to 60°
  const angleSeries = useMemo(() => {
    const ptsParallel = [];
    const ptsPerp = [];
    const fg = massKg * g;
    for (let deg = 0; deg <= 60; deg += 3) {
      const r = (deg * Math.PI) / 180;
      ptsParallel.push({ x: deg, y: fg * Math.sin(r) });
      ptsPerp.push({ x: deg, y: fg * Math.cos(r) });
    }
    return [
      { id: 'fg_par', label: 'Fg∥ = mg sin θ', color: '#B8432E', points: ptsParallel },
      { id: 'fg_perp', label: 'FN = mg cos θ', color: '#2D6A4F', points: ptsPerp },
    ];
  }, [massKg]);

  return (
    <div data-testid="newton-mechanics-atlas-aid" className="space-y-4 text-slate-800">
      {/* Header & Controls */}
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-rose-100 text-rose-900 uppercase tracking-wider">
              3D Free-Body Vector Resolution
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              Inclined Plane Forces & Trigonometric Component Breakdown
            </h4>
          </div>

          <button
            type="button"
            data-testid="btn-toggle-gravity-components"
            onClick={() => setDecomposeGravity((v) => !v)}
            className={`px-3 py-1 rounded-lg text-xs font-semibold border transition-all flex items-center gap-1.5 ${
              decomposeGravity
                ? 'bg-rose-50 border-rose-300 text-rose-900'
                : 'bg-slate-100 border-slate-200 text-slate-700'
            }`}
          >
            <Layers className="w-3.5 h-3.5" />
            {decomposeGravity ? 'Resolved: Fg∥ & Fg⊥ Visible' : 'Resolve Fg into Components'}
          </button>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Mass (m)</span>
              <span className="font-mono font-bold text-slate-900">{massKg.toFixed(1)} kg</span>
            </div>
            <input
              type="range"
              min="1"
              max="10"
              step="0.5"
              value={massKg}
              onChange={(e) => setMassKg(parseFloat(e.target.value))}
              className="w-full accent-slate-800 cursor-pointer h-1.5"
            />
          </label>

          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Angle (θ)</span>
              <span className="font-mono font-bold text-rose-700">{angleDeg}°</span>
            </div>
            <input
              type="range"
              min="10"
              max="55"
              step="1"
              value={angleDeg}
              onChange={(e) => setAngleDeg(parseInt(e.target.value, 10))}
              className="w-full accent-rose-600 cursor-pointer h-1.5"
            />
          </label>

          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Friction (μk)</span>
              <span className="font-mono font-bold text-amber-700">{muK.toFixed(2)}</span>
            </div>
            <input
              type="range"
              min="0"
              max="0.6"
              step="0.05"
              value={muK}
              onChange={(e) => setMuK(parseFloat(e.target.value))}
              className="w-full accent-amber-600 cursor-pointer h-1.5"
            />
          </label>

          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Pull F_app</span>
              <span className="font-mono font-bold text-purple-700">{appliedForceN.toFixed(0)} N</span>
            </div>
            <input
              type="range"
              min="0"
              max="50"
              step="2"
              value={appliedForceN}
              onChange={(e) => setAppliedForceN(parseFloat(e.target.value))}
              className="w-full accent-purple-600 cursor-pointer h-1.5"
            />
          </label>
        </div>
      </div>

      {/* 3D Canvas */}
      <AtlasCanvas3D
        testId="newton-mechanics-3d-canvas"
        height={320}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle="Click any 3D force arrow (Fg∥, Fg⊥, FN, fk, or block) to inspect its live trigonometric derivation"
      />

      {/* Calculation Popover */}
      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />

      {/* Synchronized Component Curve */}
      <AtlasSyncChartSvg
        title="Component Magnitude vs. Incline Angle θ"
        xLabel="Incline Angle θ (degrees)"
        yLabel="Force (N)"
        xDomain={[0, 60]}
        yDomain={[0, Math.max(50, massKg * g + 5)]}
        series={angleSeries}
        activePoint={{
          x: angleDeg,
          y: selectedId === 'fg_perp' || selectedId === 'f_normal' ? mechanicsMath.fgPerp : mechanicsMath.fgParallel,
          label: `θ=${angleDeg}°`,
          color: activeCalculation.color,
        }}
      />
    </div>
  );
}
