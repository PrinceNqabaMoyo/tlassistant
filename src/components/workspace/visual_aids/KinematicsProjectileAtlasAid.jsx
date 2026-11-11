import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Activity, Radio, Compass } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import AtlasSyncChartSvg from '../shared/atlas3d/AtlasSyncChartSvg';
import { createSphereAtom3D, createVectorArrow3D } from '../shared/atlas3d/atlasPartsKit';

/**
 * KinematicsProjectileAtlasAid
 * ----------------------------
 * Grade 10–12 Physical Sciences:
 * - Mode 1: Vertical Projectile Motion & Stroboscopic Free-Fall (y(t), v_y(t), a_y(t))
 *   Shows why v_y = 0 m/s at the apex while acceleration remains g = 9.8 m/s² downwards.
 * - Mode 2: 3D Doppler Wavefront Compression & Expansion Explorer
 *   Shows spherical/circular wavefront crowding ahead of a moving ambulance/star (λ_front < λ_0, f_L > f_S).
 */

export default function KinematicsProjectileAtlasAid() {
  const [mode, setMode] = useState('projectile'); // 'projectile' | 'doppler'
  const [uInitial, setUInitial] = useState(19.6); // m/s upward launch
  const [timeRatio, setTimeRatio] = useState(0.5); // 0 -> 1 of flight time (0.5 = apex)
  const [sourceSpeed, setSourceSpeed] = useState(85); // m/s for Doppler
  const [sourceFreq, setSourceFreq] = useState(440); // Hz
  const [selectedId, setSelectedId] = useState('apex_state');

  const g = 9.8;
  const vSound = 340;

  const kinematicsMath = useMemo(() => {
    const tApex = uInitial / g;
    const tTotal = 2 * tApex;
    const tNow = timeRatio * tTotal;
    const yNow = Math.max(0, uInitial * tNow - 0.5 * g * tNow * tNow);
    const vyNow = uInitial - g * tNow;
    const yMax = (uInitial * uInitial) / (2 * g);

    // Doppler calculations
    const fApproach = (vSound / Math.max(10, vSound - sourceSpeed)) * sourceFreq;
    const fRecede = (vSound / (vSound + sourceSpeed)) * sourceFreq;
    const lambda0 = vSound / sourceFreq;
    const lambdaFront = (vSound - sourceSpeed) / sourceFreq;
    const lambdaBack = (vSound + sourceSpeed) / sourceFreq;

    return {
      tApex,
      tTotal,
      tNow,
      yNow,
      vyNow,
      yMax,
      fApproach,
      fRecede,
      lambda0,
      lambdaFront,
      lambdaBack,
    };
  }, [uInitial, timeRatio, sourceSpeed, sourceFreq]);

  const calculationsMap = useMemo(() => {
    const { tApex, tNow, yNow, vyNow, yMax, fApproach, fRecede, lambdaFront, lambdaBack } = kinematicsMath;
    if (mode === 'doppler') {
      return {
        doppler_approach: {
          id: 'doppler_approach',
          symbol: 'f_L (\\text{approach})',
          label: 'Approaching Wavefront Compression (Higher Pitch)',
          color: '#2B5B84',
          badgeText: `f_L = ${fApproach.toFixed(0)} Hz`,
          formula: 'f_L = \\frac{v}{v - v_S} f_S',
          substitution: `f_L = \\frac{340}{340 - ${sourceSpeed}} (${sourceFreq})`,
          result: `f_L = ${fApproach.toFixed(1)}\\text{ Hz},\\quad \\lambda_{\\text{front}} = ${lambdaFront.toFixed(2)}\\text{ m}`,
          meaning: `As the source moves toward the listener at ${sourceSpeed} m/s, each new crest is emitted closer to the previous one, compressing wavelength to ${lambdaFront.toFixed(2)} m and raising observed frequency.`,
        },
        doppler_recede: {
          id: 'doppler_recede',
          symbol: 'f_L (\\text{recede})',
          label: 'Receding Wavefront Expansion (Lower Pitch / Redshift)',
          color: '#B8432E',
          badgeText: `f_L = ${fRecede.toFixed(0)} Hz`,
          formula: 'f_L = \\frac{v}{v + v_S} f_S',
          substitution: `f_L = \\frac{340}{340 + ${sourceSpeed}} (${sourceFreq})`,
          result: `f_L = ${fRecede.toFixed(1)}\\text{ Hz},\\quad \\lambda_{\\text{back}} = ${lambdaBack.toFixed(2)}\\text{ m}`,
          meaning: `Behind the moving source, wavefronts are stretched apart to λ = ${lambdaBack.toFixed(2)} m, lowering the frequency heard by a stationary observer behind the source.`,
        },
      };
    }

    return {
      apex_state: {
        id: 'apex_state',
        symbol: 'y_{\\max}, v_y = 0',
        label: 'Maximum Height (Apex Turning Point)',
        color: '#D97706',
        badgeText: `y_max = ${yMax.toFixed(1)} m`,
        formula: 'v_f^2 = v_i^2 + 2a\\Delta y \\implies 0 = u^2 - 2 g y_{\\max}',
        substitution: `y_{\\max} = \\frac{(${uInitial.toFixed(1)})^2}{2(9.8)} \\text{ at } t_{\\text{apex}} = \\frac{${uInitial.toFixed(1)}}{9.8}`,
        result: `y_{\\max} = ${yMax.toFixed(2)}\\text{ m at } t = ${tApex.toFixed(2)}\\text{ s}`,
        meaning: `At the highest point, vertical velocity is instantaneously zero (v_y = 0 m·s⁻¹), YET gravitational acceleration remains 9.8 m·s⁻² downwards!`,
      },
      instant_velocity: {
        id: 'instant_velocity',
        symbol: '\\vec{v}(t)',
        label: `Instantaneous Velocity at t = ${tNow.toFixed(2)} s`,
        color: '#2B5B84',
        badgeText: `v_y = ${vyNow.toFixed(1)} m/s`,
        formula: 'v_f = v_i + a\\Delta t \\quad \\text{and} \\quad \\Delta y = v_i \\Delta t + \\tfrac{1}{2}a\\Delta t^2',
        substitution: `v_y = ${uInitial.toFixed(1)} + (-9.8)(${tNow.toFixed(2)})`,
        result: `v_y = ${vyNow.toFixed(2)}\\text{ m\\cdot s}^{-1},\\quad y = ${yNow.toFixed(2)}\\text{ m}`,
        meaning: `Notice the velocity-time graph is a continuous straight line with constant gradient -9.8 m·s⁻² crossing zero at t = ${tApex.toFixed(2)} s.`,
      },
      gravity_accel: {
        id: 'gravity_accel',
        symbol: '\\vec{g}',
        label: 'Constant Gravitational Acceleration (Free Fall)',
        color: '#B8432E',
        badgeText: 'g = -9.8 m/s²',
        formula: '\\vec{a} = \\vec{g} = 9.8\\text{ m\\cdot s}^{-2}\\text{ downwards}',
        substitution: `\\frac{\\Delta v_y}{\\Delta t} = -9.8\\text{ m\\cdot s}^{-2} \\text{ throughout flight}`,
        result: 'a_y = -9.8\\text{ m\\cdot s}^{-2} \\text{ (even at apex!)}',
        meaning: `Whether rising, turning at the apex, or falling, the only force acting on the projectile in free fall is weight F_g = mg downwards.`,
      },
    };
  }, [kinematicsMath, mode, sourceSpeed, sourceFreq, uInitial]);

  const activeCalculation = calculationsMap[selectedId] || Object.values(calculationsMap)[0];

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    if (mode === 'projectile') {
      const { tTotal, tNow, yNow, vyNow, yMax } = kinematicsMath;
      const yScale = 2.0 / Math.max(10, yMax);

      // Draw stroboscopic ghosts along parabolic trajectory (x spread slightly for visual clarity)
      const steps = 10;
      for (let i = 0; i <= steps; i++) {
        const frac = i / steps;
        const t = frac * tTotal;
        const y = Math.max(0, uInitial * t - 0.5 * g * t * t);
        const x = (frac - 0.5) * 3.8;
        const isApex = i === 5;
        const ghost = createSphereAtom3D({
          radius: isApex ? 0.14 : 0.09,
          color: isApex ? 0xD97706 : 0x94A3B8,
          opacity: isApex ? 0.95 : 0.42,
          interactiveId: isApex ? 'apex_state' : 'instant_velocity',
        });
        ghost.position.set(x, 0.14 + y * yScale, 0);
        root.add(ghost);
      }

      // Active projectile sphere at current timeRatio
      const curX = (timeRatio - 0.5) * 3.8;
      const curY = 0.14 + yNow * yScale;
      const ball = createSphereAtom3D({
        radius: 0.19,
        color: 0x2B5B84,
        interactiveId: 'instant_velocity',
      });
      ball.position.set(curX, curY, 0);
      root.add(ball);

      // Velocity vector v_y(t)
      if (Math.abs(vyNow) > 0.4) {
        const vDir = vyNow >= 0 ? 1 : -1;
        const vArrow = createVectorArrow3D({
          origin: [curX, curY, 0],
          direction: [0, vDir, 0],
          length: Math.max(0.35, Math.abs(vyNow) * 0.045),
          color: 0x2B5B84,
          interactiveId: 'instant_velocity',
        });
        root.add(vArrow);
      }

      // Constant downward acceleration vector g (always visible, even at apex!)
      const gArrow = createVectorArrow3D({
        origin: [curX + 0.24, curY, 0],
        direction: [0, -1, 0],
        length: 0.62,
        color: 0xB8432E,
        interactiveId: 'gravity_accel',
      });
      root.add(gArrow);
    } else {
      // 3D Doppler Wavefront Rings
      const mach = sourceSpeed / vSound;
      const srcSphere = createSphereAtom3D({
        radius: 0.22,
        color: 0xD97706,
        interactiveId: 'doppler_approach',
      });
      srcSphere.position.set(0.45, 0.35, 0);
      root.add(srcSphere);

      // Velocity arrow of source
      const srcArrow = createVectorArrow3D({
        origin: [0.45, 0.65, 0],
        direction: [1, 0, 0],
        length: 0.75,
        color: 0x2B5B84,
        interactiveId: 'doppler_approach',
      });
      root.add(srcArrow);

      // Concentric wavefront rings shifted by source motion
      for (let k = 1; k <= 6; k++) {
        const radius = k * 0.38;
        const centerX = 0.45 - k * mach * 0.36;
        const ringGeo = new THREE.TorusGeometry(radius, 0.022, 12, 48);
        ringGeo.rotateX(Math.PI / 2);
        const ringMat = new THREE.MeshBasicMaterial({
          color: k <= 3 ? 0x2B5B84 : 0xB8432E,
        });
        const ringMesh = new THREE.Mesh(ringGeo, ringMat);
        ringMesh.position.set(centerX, 0.12, 0);
        ringMesh.userData = { interactiveId: k <= 3 ? 'doppler_approach' : 'doppler_recede' };
        root.add(ringMesh);
      }
    }

    return { interactiveObjects: [root] };
  }, [kinematicsMath, mode, sourceSpeed, timeRatio, uInitial]);

  // Synchronized Velocity-Time v_y(t) & Position y(t) curves
  const chartSeries = useMemo(() => {
    const { tTotal } = kinematicsMath;
    const vPts = [];
    const yPts = [];
    for (let i = 0; i <= 20; i++) {
      const t = (i / 20) * tTotal;
      vPts.push({ x: t, y: uInitial - g * t });
      yPts.push({ x: t, y: Math.max(0, uInitial * t - 0.5 * g * t * t) });
    }
    return [
      { id: 'vy', label: 'Velocity v_y(t) [m/s]', color: '#2B5B84', points: vPts },
      { id: 'y', label: 'Height y(t) [m]', color: '#D97706', dashed: true, points: yPts },
    ];
  }, [kinematicsMath, uInitial]);

  return (
    <div data-testid="kinematics-projectile-atlas-aid" className="space-y-4 text-slate-800">
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-sky-100 text-sky-900 uppercase tracking-wider">
              Stroboscopic Kinematics & Wavefronts
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              {mode === 'projectile'
                ? 'Vertical Projectile Free-Fall & Apex Vector Analysis'
                : '3D Doppler Wavefront Compression & Pitch Shift'}
            </h4>
          </div>

          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-mode-projectile"
              onClick={() => {
                setMode('projectile');
                setSelectedId('apex_state');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition-all ${
                mode === 'projectile' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              Projectile Strobe
            </button>
            <button
              type="button"
              data-testid="btn-mode-doppler"
              onClick={() => {
                setMode('doppler');
                setSelectedId('doppler_approach');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition-all flex items-center gap-1 ${
                mode === 'doppler' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              <Radio className="w-3.5 h-3.5" />
              3D Doppler Shift
            </button>
          </div>
        </div>

        {mode === 'projectile' ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
            <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
              <div className="flex justify-between text-[11px] font-semibold text-slate-600">
                <span>Launch Velocity (u)</span>
                <span className="font-mono font-bold text-[#2B5B84]">+{uInitial.toFixed(1)} m/s</span>
              </div>
              <input
                type="range"
                min="9.8"
                max="29.4"
                step="0.5"
                value={uInitial}
                onChange={(e) => setUInitial(parseFloat(e.target.value))}
                className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
              />
            </label>

            <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
              <div className="flex justify-between text-[11px] font-semibold text-slate-600">
                <span>Flight Time Scrub (t = {kinematicsMath.tNow.toFixed(2)} s)</span>
                <span className="font-mono font-bold text-amber-700">
                  {Math.abs(timeRatio - 0.5) < 0.04 ? 'APEX (vy = 0)' : `${Math.round(timeRatio * 100)}%`}
                </span>
              </div>
              <input
                type="range"
                min="0"
                max="1"
                step="0.02"
                value={timeRatio}
                onChange={(e) => setTimeRatio(parseFloat(e.target.value))}
                className="w-full accent-amber-600 cursor-pointer h-1.5"
              />
            </label>
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
            <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
              <div className="flex justify-between text-[11px] font-semibold text-slate-600">
                <span>Source Speed (v_S)</span>
                <span className="font-mono font-bold text-[#2B5B84]">{sourceSpeed} m/s</span>
              </div>
              <input
                type="range"
                min="20"
                max="160"
                step="5"
                value={sourceSpeed}
                onChange={(e) => setSourceSpeed(parseInt(e.target.value, 10))}
                className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
              />
            </label>

            <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
              <div className="flex justify-between text-[11px] font-semibold text-slate-600">
                <span>Emitted Frequency (f_S)</span>
                <span className="font-mono font-bold text-amber-700">{sourceFreq} Hz</span>
              </div>
              <input
                type="range"
                min="200"
                max="800"
                step="20"
                value={sourceFreq}
                onChange={(e) => setSourceFreq(parseInt(e.target.value, 10))}
                className="w-full accent-amber-600 cursor-pointer h-1.5"
              />
            </label>
          </div>
        )}
      </div>

      <AtlasCanvas3D
        testId="kinematics-projectile-3d-canvas"
        height={300}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle={
          mode === 'projectile'
            ? 'Scrub time t to the apex (50%) to see why v_y = 0 m/s while g = 9.8 m/s² downwards remains active'
            : 'Click the compressed front rings or stretched rear rings to inspect the Doppler shift equation'
        }
      />

      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />

      {mode === 'projectile' && (
        <AtlasSyncChartSvg
          title="Synchronized Velocity v_y(t) & Position y(t) Graphs"
          xLabel="Time t (s)"
          yLabel="vy (m/s) / y (m)"
          xDomain={[0, Math.max(2, kinematicsMath.tTotal)]}
          yDomain={[-30, Math.max(30, kinematicsMath.yMax + 4)]}
          series={chartSeries}
          activePoint={{
            x: kinematicsMath.tNow,
            y: kinematicsMath.vyNow,
            label: `vy = ${kinematicsMath.vyNow.toFixed(1)} m/s`,
            color: '#2B5B84',
          }}
        />
      )}
    </div>
  );
}
