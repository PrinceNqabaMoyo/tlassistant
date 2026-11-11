import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { TrendingUp, Box } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import AtlasSyncChartSvg from '../shared/atlas3d/AtlasSyncChartSvg';
import { createBlock3D, createSphereAtom3D } from '../shared/atlas3d/atlasPartsKit';

/**
 * CalculusFirstPrinciplesAtlasAid
 * -------------------------------
 * Grade 12 Mathematics & Technical Mathematics:
 * - Mode 1: 3D Box Volume Optimization (Folding cut corners x from a 24 cm × 18 cm sheet)
 *   Shows why V(x) = x(24 - 2x)(18 - 2x) peaks where V'(x) = 0.
 * - Mode 2: First Principles Secant-to-Tangent Limit Explorer (h -> 0)
 *   Shows the secant chord across (x, f(x)) and (x+h, f(x+h)) converging to f'(x).
 */

export default function CalculusFirstPrinciplesAtlasAid() {
  const [mode, setMode] = useState('optimization'); // 'optimization' | 'first_principles'
  const [cutX, setCutX] = useState(3.4); // cm corner cut (optimal ~ 3.40 cm for 24x18 sheet)
  const [hStep, setHStep] = useState(1.2); // h step for first principles on f(x) = 0.25 x^2
  const [selectedId, setSelectedId] = useState('box_volume');

  const sheetL = 24;
  const sheetW = 18;

  const calcMath = useMemo(() => {
    const lInner = Math.max(0.5, sheetL - 2 * cutX);
    const wInner = Math.max(0.5, sheetW - 2 * cutX);
    const volume = cutX * lInner * wInner;
    // V(x) = 4x^3 - 84x^2 + 432x => V'(x) = 12x^2 - 168x + 432
    const dVdx = 12 * cutX * cutX - 168 * cutX + 432;

    // First principles at x0 = 2 on f(x) = x^2
    const x0 = 2.0;
    const fx0 = x0 * x0;
    const fxh = (x0 + hStep) * (x0 + hStep);
    const secantGrad = (fxh - fx0) / Math.max(0.001, hStep);
    const exactGrad = 2 * x0;

    return {
      lInner,
      wInner,
      volume,
      dVdx,
      x0,
      fx0,
      fxh,
      secantGrad,
      exactGrad,
    };
  }, [cutX, hStep]);

  const calculationsMap = useMemo(() => {
    const { lInner, wInner, volume, dVdx, x0, hStep: hVal, secantGrad, exactGrad } = { ...calcMath, hStep };
    if (mode === 'first_principles') {
      return {
        secant_limit: {
          id: 'secant_limit',
          symbol: "f'(x) = \\lim_{h \\to 0}",
          label: `First Principles Secant Gradient (h = ${hVal.toFixed(2)})`,
          color: '#2B5B84',
          badgeText: `m_sec = ${secantGrad.toFixed(2)}`,
          formula: "f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}",
          substitution: `m_{\\text{sec}} = \\frac{(${x0} + ${hVal.toFixed(2)})^2 - (${x0})^2}{${hVal.toFixed(2)}} = 2(${x0}) + ${hVal.toFixed(2)}`,
          result: `m_{\\text{sec}} = ${secantGrad.toFixed(2)} \\xrightarrow{h \\to 0} f'(2) = ${exactGrad.toFixed(2)}`,
          meaning: 'As the horizontal step h shrinks toward 0, the two secant points coalesce into a single point of tangency with instantaneous gradient 2x = 4.',
        },
      };
    }

    return {
      box_volume: {
        id: 'box_volume',
        symbol: 'V(x)',
        label: `Open-Top Box Volume V(x) at Corner Cut x = ${cutX.toFixed(2)} cm`,
        color: '#2B5B84',
        badgeText: `V = ${volume.toFixed(0)} cm³`,
        formula: 'V(x) = x(24 - 2x)(18 - 2x) = 4x^3 - 84x^2 + 432x',
        substitution: `V(${cutX.toFixed(2)}) = (${cutX.toFixed(2)})(${lInner.toFixed(1)})(${wInner.toFixed(1)})`,
        result: `V = ${volume.toFixed(1)}\\text{ cm}^3`,
        meaning: 'Cutting small squares (x × x) from each corner and folding up the 4 flaps creates a 3D tray of height x, length (24 − 2x), and width (18 − 2x).',
      },
      stationary_point: {
        id: 'stationary_point',
        symbol: "V'(x) = 0",
        label: 'Stationary Point & Maximum Volume Condition',
        color: Math.abs(dVdx) < 8 ? '#2D6A4F' : '#D97706',
        badgeText: `V'(x) = ${dVdx.toFixed(1)}`,
        formula: "V'(x) = 12x^2 - 168x + 432 = 0 \\implies x \\approx 3.40\\text{ cm}",
        substitution: `V'(${cutX.toFixed(2)}) = 12(${cutX.toFixed(2)})^2 - 168(${cutX.toFixed(2)}) + 432`,
        result: `V'(${cutX.toFixed(2)}) = ${dVdx.toFixed(1)}\\text{ cm}^2`,
        meaning: Math.abs(cutX - 3.4) < 0.15
          ? 'At x ≈ 3.40 cm, the derivative V′(x) = 0 and V″(x) < 0, yielding the maximum possible 3D box volume (~654.9 cm³)!'
          : 'Scrub x toward 3.40 cm to watch the tangent gradient V′(x) flatten to zero at the peak of the volume curve.',
      },
    };
  }, [calcMath, cutX, hStep, mode]);

  const activeCalculation = calculationsMap[selectedId] || Object.values(calculationsMap)[0];

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    if (mode === 'optimization') {
      const scale = 0.14;
      const bw = calcMath.lInner * scale;
      const bd = calcMath.wInner * scale;
      const bh = cutX * scale * 1.4;

      // Base plate
      const base = createBlock3D({
        width: bw,
        height: 0.05,
        depth: bd,
        color: 0x2B5B84,
        interactiveId: 'box_volume',
      });
      base.position.set(0, 0.03, 0);
      root.add(base);

      // 4 folded side walls of height bh
      const wallF = createBlock3D({ width: bw, height: bh, depth: 0.05, color: 0xD97706, interactiveId: 'stationary_point' });
      wallF.position.set(0, bh / 2 + 0.03, bd / 2);
      const wallB = createBlock3D({ width: bw, height: bh, depth: 0.05, color: 0xD97706, interactiveId: 'stationary_point' });
      wallB.position.set(0, bh / 2 + 0.03, -bd / 2);
      const wallL = createBlock3D({ width: 0.05, height: bh, depth: bd, color: 0x2D6A4F, interactiveId: 'stationary_point' });
      wallL.position.set(-bw / 2, bh / 2 + 0.03, 0);
      const wallR = createBlock3D({ width: 0.05, height: bh, depth: bd, color: 0x2D6A4F, interactiveId: 'stationary_point' });
      wallR.position.set(bw / 2, bh / 2 + 0.03, 0);
      root.add(wallF, wallB, wallL, wallR);
    } else {
      // 3D Parabolic Rib Curve y = 0.22 x^2 with secant line between x0 and x0 + h
      const curvePts = [];
      for (let x = -2.2; x <= 2.4; x += 0.15) {
        curvePts.push(new THREE.Vector3(x, 0.25 + 0.32 * (x + 1.2) * (x + 1.2), 0));
      }
      const tubeGeo = new THREE.TubeGeometry(new THREE.CatmullRomCurve3(curvePts), 40, 0.045, 12, false);
      const tubeMesh = new THREE.Mesh(tubeGeo, new THREE.MeshBasicMaterial({ color: 0x1E1B18 }));
      root.add(tubeMesh);

      const xA = -0.2;
      const yA = 0.25 + 0.32 * (xA + 1.2) * (xA + 1.2);
      const xB = xA + hStep * 0.85;
      const yB = 0.25 + 0.32 * (xB + 1.2) * (xB + 1.2);

      const ptA = createSphereAtom3D({ radius: 0.11, color: 0x2B5B84, interactiveId: 'secant_limit' });
      ptA.position.set(xA, yA, 0);
      const ptB = createSphereAtom3D({ radius: 0.11, color: 0xD97706, interactiveId: 'secant_limit' });
      ptB.position.set(xB, yB, 0);
      root.add(ptA, ptB);

      // Extended secant line
      const slope = (yB - yA) / Math.max(0.02, xB - xA);
      const secStart = new THREE.Vector3(xA - 1.0, yA - slope * 1.0, 0);
      const secEnd = new THREE.Vector3(xA + 1.8, yA + slope * 1.8, 0);
      const secLine = new THREE.Line(
        new THREE.BufferGeometry().setFromPoints([secStart, secEnd]),
        new THREE.LineBasicMaterial({ color: 0xB8432E, linewidth: 2 })
      );
      root.add(secLine);
    }

    return { interactiveObjects: [root] };
  }, [calcMath, cutX, hStep, mode]);

  const volumeSeries = useMemo(() => {
    const pts = [];
    for (let x = 0.2; x <= 8.5; x += 0.3) {
      pts.push({ x, y: x * (24 - 2 * x) * (18 - 2 * x) });
    }
    return [{ id: 'vol', label: 'Volume V(x) [cm³]', color: '#2B5B84', fillArea: true, points: pts }];
  }, []);

  return (
    <div data-testid="calculus-first-principles-atlas-aid" className="space-y-4 text-slate-800">
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-purple-100 text-purple-900 uppercase tracking-wider">
              Grade 12 Differential Calculus
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              {mode === 'optimization'
                ? '3D Box Volume Optimization & Stationary Point V′(x) = 0'
                : 'First Principles Secant-to-Tangent Limit (h → 0)'}
            </h4>
          </div>

          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-calc-optimization"
              onClick={() => {
                setMode('optimization');
                setSelectedId('box_volume');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 ${
                mode === 'optimization' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              <Box className="w-3.5 h-3.5" />
              3D Optimization
            </button>
            <button
              type="button"
              data-testid="btn-calc-limit"
              onClick={() => {
                setMode('first_principles');
                setSelectedId('secant_limit');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 ${
                mode === 'first_principles' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              <TrendingUp className="w-3.5 h-3.5" />
              First Principles (h → 0)
            </button>
          </div>
        </div>

        {mode === 'optimization' ? (
          <label className="bg-slate-50 p-2.5 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-xs font-semibold text-slate-700">
              <span>Corner Cut Size (x) from 24 cm × 18 cm Sheet</span>
              <span className="font-mono font-bold text-[#2B5B84]">
                x = {cutX.toFixed(2)} cm → V = {calcMath.volume.toFixed(1)} cm³
              </span>
            </div>
            <input
              type="range"
              min="0.5"
              max="8.0"
              step="0.1"
              value={cutX}
              onChange={(e) => setCutX(parseFloat(e.target.value))}
              className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
            />
          </label>
        ) : (
          <label className="bg-slate-50 p-2.5 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-xs font-semibold text-slate-700">
              <span>Secant Step Width (h → 0)</span>
              <span className="font-mono font-bold text-[#2B5B84]">
                h = {hStep.toFixed(2)} → m_sec = {calcMath.secantGrad.toFixed(2)}
              </span>
            </div>
            <input
              type="range"
              min="0.02"
              max="2.0"
              step="0.02"
              value={hStep}
              onChange={(e) => setHStep(parseFloat(e.target.value))}
              className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
            />
          </label>
        )}
      </div>

      <AtlasCanvas3D
        testId="calculus-first-principles-canvas"
        height={290}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle={
          mode === 'optimization'
            ? 'Adjust corner cut x to 3.40 cm to maximize the 3D folded tray volume where V′(x) = 0'
            : 'Slide h toward 0.02 to watch the red secant chord converge onto the tangent gradient'
        }
      />

      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />

      {mode === 'optimization' && (
        <AtlasSyncChartSvg
          title="Cubic Volume Function V(x) = 4x³ − 84x² + 432x"
          xLabel="Corner Cut x (cm)"
          yLabel="Volume V (cm³)"
          xDomain={[0, 9]}
          yDomain={[0, 700]}
          series={volumeSeries}
          activePoint={{
            x: cutX,
            y: calcMath.volume,
            label: `V(${cutX.toFixed(1)}) = ${calcMath.volume.toFixed(0)} cm³`,
            color: '#2B5B84',
          }}
        />
      )}
    </div>
  );
}
