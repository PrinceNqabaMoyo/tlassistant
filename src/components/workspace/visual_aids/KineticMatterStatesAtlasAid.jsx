import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Thermometer, Gauge, Flame } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import AtlasSyncChartSvg from '../shared/atlas3d/AtlasSyncChartSvg';
import {
  createFloorGrid3D,
  createSphereAtom3D,
  createBondCylinder3D,
  createBlock3D,
  createVectorArrow3D,
} from '../shared/atlas3d/atlasPartsKit';
import { createPaperMaterial, tagInteractive3D } from '../shared/atlas3d/atlasRenderEngine';

/**
 * KineticMatterStatesAtlasAid
 *
 * Interactive 3D Paper & Ink Simulation for:
 *   - Natural Sciences Gr 7–8: Particle model of matter, states of matter, diffusion, density
 *   - Physical Sciences Gr 10: States of matter and the kinetic molecular theory, heating/cooling curves, latent heat
 *   - Physical Sciences Gr 11: Ideal gases and thermal properties (Boyle's Law p1V1 = p2V2, pV = nRT)
 *
 * Key Micro-Physics Demonstrated:
 *   1. Solid (< 0 °C): Particles vibrate about fixed 3D lattice nodes connected by intermolecular spring bonds.
 *   2. Melting Plateau (0 °C): Adding thermal energy Q breaks intermolecular bonds while temperature T remains constant (0 °C).
 *   3. Liquid (0–100 °C): Particles slide past one another; heating increases average kinetic energy (Ek ∝ T).
 *   4. Boiling Plateau (100 °C): Latent heat of vaporisation overcomes intermolecular attractions at constant T = 100 °C.
 *   5. Gas (> 100 °C): High-velocity elastic collisions against chamber walls & piston generate Pressure P = F/A = nRT/V.
 */

function computeHeatingState(heatKJ) {
  // Piecewise Heating Curve for 1 mol H2O from -20°C to 130°C as Q goes 0 -> 100 kJ
  if (heatKJ <= 15) {
    // Solid warming: -20°C to 0°C
    const frac = heatKJ / 15;
    return {
      phase: 'Solid (Crystal Lattice)',
      tempC: -20 + frac * 20,
      bondIntegrity: 1.0,
      agitation: 0.04 + frac * 0.04,
      isPlateau: false,
      latentType: null,
    };
  }
  if (heatKJ <= 35) {
    // Melting plateau at 0°C (Latent Heat of Fusion ΔH_fus)
    const frac = (heatKJ - 15) / 20;
    return {
      phase: 'Melting Plateau (Solid ⇌ Liquid)',
      tempC: 0,
      bondIntegrity: 1.0 - frac * 0.65,
      agitation: 0.08,
      isPlateau: true,
      latentType: 'Latent Heat of Fusion (Breaking Lattice Bonds at Constant 0 °C)',
    };
  }
  if (heatKJ <= 65) {
    // Liquid warming: 0°C to 100°C
    const frac = (heatKJ - 35) / 30;
    return {
      phase: 'Liquid State (Sliding Clusters)',
      tempC: frac * 100,
      bondIntegrity: 0.35,
      agitation: 0.1 + frac * 0.16,
      isPlateau: false,
      latentType: null,
    };
  }
  if (heatKJ <= 85) {
    // Boiling plateau at 100°C (Latent Heat of Vaporisation ΔH_vap)
    const frac = (heatKJ - 65) / 20;
    return {
      phase: 'Boiling Plateau (Liquid ⇌ Gas)',
      tempC: 100,
      bondIntegrity: Math.max(0, 0.35 * (1 - frac)),
      agitation: 0.26 + frac * 0.12,
      isPlateau: true,
      latentType: 'Latent Heat of Vaporisation (Overcoming Intermolecular Forces at Constant 100 °C)',
    };
  }
  // Superheated Gas: 100°C to 140°C
  const frac = (heatKJ - 85) / 15;
  return {
    phase: 'Gas State (Elastic Wall Collisions)',
    tempC: 100 + frac * 40,
    bondIntegrity: 0.0,
    agitation: 0.42 + frac * 0.18,
    isPlateau: false,
    latentType: null,
  };
}

export default function KineticMatterStatesAtlasAid() {
  const [heatKJ, setHeatKJ] = useState(25); // default in Melting Plateau so student immediately sees latent heat!
  const [volumeL, setVolumeL] = useState(2.5); // Piston volume 1.2 L to 4.0 L
  const [chartMode, setChartMode] = useState('heating'); // 'heating' | 'boyle'
  const [selectedCalcId, setSelectedCalcId] = useState(null);

  const thermal = useMemo(() => computeHeatingState(heatKJ), [heatKJ]);
  const tempK = Math.round(thermal.tempC + 273.15);
  const nMoles = 1.0;
  const R = 8.314;
  // Ideal gas pressure in kPa: P = nRT / V
  const pressureKPa = Number(((nMoles * R * tempK) / volumeL).toFixed(1));

  const calcItems = useMemo(
    () => [
      {
        id: 'kinetic_temp',
        label: `Kinetic Molecular Energy & Phase (${thermal.phase})`,
        shortLabel: `Temp (${Math.round(thermal.tempC)} °C / ${tempK} K)`,
        badge: thermal.isPlateau ? 'Constant T Plateau!' : 'Ek ∝ T',
        color: thermal.isPlateau ? '#D97706' : '#E11D48',
        result: `${Math.round(thermal.tempC)} °C (${tempK} K)`,
        formula: thermal.isPlateau
          ? '$$Q_{\\text{latent}} = m \\cdot L \\quad (\\Delta T = 0\\text{ K})$$'
          : '$$E_{k,\\text{avg}} = \\frac{3}{2} k_B T \\quad (T\\text{ in Kelvin})$$',
        substitution: thermal.isPlateau
          ? `$$Q = ${heatKJ}\\text{ kJ added} \\implies \\text{Temperature stays fixed at } ${Math.round(
              thermal.tempC
            )}\\text{ ^\\circ C}$$`
          : `$$T(K) = ${Math.round(thermal.tempC)} + 273.15 = ${tempK}\\text{ K}$$`,
        mechanism: thermal.isPlateau
          ? `${thermal.latentType}: Notice that even though you are adding heat (Q = ${heatKJ} kJ), the thermometer does NOT rise! All added thermal energy goes into potential energy (Ep) to break the intermolecular spring bonds between particles rather than speeding them up.`
          : `Temperature is a direct measure of the average translational kinetic energy of the particles. Heating increases particle speed and collision frequency.`,
      },
      {
        id: 'piston_pressure',
        label: "Gas Pressure & Boyle's / Ideal Gas Law",
        shortLabel: `Pressure (${pressureKPa} kPa)`,
        badge: `V = ${volumeL.toFixed(1)} L`,
        color: '#13519C',
        result: `P = ${pressureKPa} kPa`,
        formula: '$$pV = nRT \\implies P = \\frac{nRT}{V} \\quad (p_1V_1 = p_2V_2)$$',
        substitution: `$$P = \\frac{(1.0\\text{ mol})(8.314\\text{ J\\cdot mol}^{-1}\\text{K}^{-1})(${tempK}\\text{ K})}{${volumeL.toFixed(
          1
        )}\\text{ dm}^3} = ${pressureKPa}\\text{ kPa}$$`,
        mechanism:
          'Macroscopic gas pressure is caused by millions of elastic particle collisions against the container walls and movable piston (P = F/A). Decreasing chamber volume V crowds the particles, increasing collision frequency per unit area.',
      },
      {
        id: 'intermolecular_bonds',
        label: 'Intermolecular Forces vs. Thermal Agitation',
        shortLabel: `Bond Integrity (${Math.round(thermal.bondIntegrity * 100)}%)`,
        badge: `${Math.round(thermal.bondIntegrity * 100)}% Bound`,
        color: '#059669',
        result:
          thermal.bondIntegrity > 0.7
            ? 'Rigid Lattice'
            : thermal.bondIntegrity > 0.05
            ? 'Sliding Clusters'
            : 'Free Gas',
        formula: '$$E_{\\text{internal}} = E_k(\\text{motion}) + E_p(\\text{intermolecular bonds})$$',
        substitution: `$$\\text{Bond integrity} = ${Math.round(
          thermal.bondIntegrity * 100
        )}\\%, \\quad \\text{Agitation} = ${(thermal.agitation * 100).toFixed(0)}\\text{ units}$$`,
        mechanism:
          'In solids, strong intermolecular forces lock particles into a 3D lattice. In liquids, particles have enough kinetic energy to slide past neighbours. In gases, kinetic energy completely overcomes intermolecular attractions.',
      },
    ],
    [thermal, tempK, heatKJ, volumeL, pressureKPa]
  );

  const activeCalcItem =
    calcItems.find((c) => c.id === selectedCalcId) || calcItems[0] || null;

  // Build 3D Chamber, Movable Piston, and 27 Kinetic Particles + Intermolecular Bonds
  const buildScene = useCallback(
    ({ scene }) => {
      scene.add(createFloorGrid3D({ size: 9, divisions: 9, y: -2.0 }));

      // Chamber height scales with volumeL (1.2 L -> 4.0 L maps to topY -0.1 -> +2.1)
      const floorY = -1.6;
      const topY = floorY + 0.9 + ((volumeL - 1.0) / 3.0) * 2.1;
      const halfW = 1.65;

      // Translucent Glass Containment Chamber Walls
      const chamberHeight = topY - floorY + 0.3;
      const chamberBox = createBlock3D({
        width: halfW * 2,
        height: chamberHeight,
        depth: halfW * 2,
        color: 0xe2e8f0,
        opacity: 0.22,
        position: [0, (floorY + topY) / 2, 0],
        interactiveId: 'piston_pressure',
      });
      scene.add(chamberBox);

      // Movable Top Piston Plate + Downward Pressure Vector Arrow
      const pistonPlate = createBlock3D({
        width: halfW * 1.96,
        height: 0.22,
        depth: halfW * 1.96,
        color: 0x13519c,
        position: [0, topY + 0.11, 0],
        interactiveId: 'piston_pressure',
      });
      scene.add(pistonPlate);

      const pressureArrow = createVectorArrow3D({
        origin: [0, topY + 1.25, 0],
        dir: [0, -1, 0],
        length: 0.95,
        color: 0x13519c,
        interactiveId: 'piston_pressure',
      });
      scene.add(pressureArrow);

      // Thermal Burner Base below chamber
      const burnerGlow = Math.min(1, heatKJ / 100);
      const burnerPlate = createBlock3D({
        width: halfW * 1.8,
        height: 0.16,
        depth: halfW * 1.8,
        color: heatKJ > 15 ? 0xe11d48 : 0x38bdf8,
        glow: burnerGlow * 0.5,
        position: [0, floorY - 0.12, 0],
        interactiveId: 'kinetic_temp',
      });
      scene.add(burnerPlate);

      // 3x3x3 = 27 Particles
      const particles = [];
      let idx = 0;
      for (let ix = -1; ix <= 1; ix++) {
        for (let iy = 0; iy <= 2; iy++) {
          for (let iz = -1; iz <= 1; iz++) {
            const latticePos = new THREE.Vector3(
              ix * 0.72,
              floorY + 0.36 + iy * 0.65,
              iz * 0.72
            );
            const pColor = thermal.isPlateau
              ? 0xf59e0b
              : thermal.bondIntegrity > 0.7
              ? 0x2563eb
              : thermal.bondIntegrity > 0.05
              ? 0x0ea5e9
              : 0xe11d48;

            const sphere = createSphereAtom3D({
              radius: 0.2,
              color: pColor,
              position: [latticePos.x, latticePos.y, latticePos.z],
              glow: thermal.isPlateau ? 0.35 : 0.1,
              interactiveId: 'kinetic_temp',
            });
            scene.add(sphere);

            // Deterministic pseudo-random velocity vector per particle
            const vx = Math.sin(idx * 1.7 + 0.5);
            const vy = Math.cos(idx * 2.3 + 1.1);
            const vz = Math.sin(idx * 3.1 + 2.0);
            particles.push({
              mesh: sphere,
              latticePos,
              pos: latticePos.clone(),
              vel: new THREE.Vector3(vx, vy, vz).normalize(),
              phaseOffset: idx * 0.85,
            });
            idx++;
          }
        }
      }

      // Intermolecular Bond Lines (visible in Solid and Melting/Liquid states)
      const bondPairs = [];
      if (thermal.bondIntegrity > 0.05) {
        const bondMat = createPaperMaterial(
          thermal.isPlateau ? 0xf59e0b : 0x059669,
          { opacity: thermal.bondIntegrity }
        );
        for (let i = 0; i < particles.length; i++) {
          for (let j = i + 1; j < particles.length; j++) {
            if (particles[i].latticePos.distanceTo(particles[j].latticePos) < 0.78) {
              const cylGeo = new THREE.CylinderGeometry(0.032, 0.032, 0.7, 6);
              const cylMesh = new THREE.Mesh(cylGeo, bondMat);
              tagInteractive3D(cylMesh, 'intermolecular_bonds');
              scene.add(cylMesh);
              bondPairs.push({ mesh: cylMesh, a: particles[i], b: particles[j] });
            }
          }
        }
      }

      return {
        onTick: (elapsed) => {
          particles.forEach((p) => {
            if (thermal.bondIntegrity > 0.65) {
              // Solid / Melting: vibrate around fixed 3D lattice coordinates
              const amp = thermal.agitation * 1.4;
              p.mesh.position.set(
                p.latticePos.x + Math.sin(elapsed * 16 + p.phaseOffset) * amp,
                p.latticePos.y + Math.cos(elapsed * 18 + p.phaseOffset * 1.3) * amp,
                p.latticePos.z + Math.sin(elapsed * 15 + p.phaseOffset * 0.7) * amp
              );
            } else if (thermal.bondIntegrity > 0.05) {
              // Liquid / Boiling: circulate in lower half of chamber
              const liqTop = floorY + (topY - floorY) * 0.58;
              const x =
                p.latticePos.x * 1.25 +
                Math.sin(elapsed * 3.2 + p.phaseOffset) * 0.45;
              const y =
                floorY +
                0.3 +
                ((Math.sin(elapsed * 2.5 + p.phaseOffset) * 0.5 + 0.5) *
                  (liqTop - floorY - 0.45));
              const z =
                p.latticePos.z * 1.25 +
                Math.cos(elapsed * 2.9 + p.phaseOffset) * 0.45;
              p.mesh.position.set(
                Math.max(-halfW + 0.25, Math.min(halfW - 0.25, x)),
                y,
                Math.max(-halfW + 0.25, Math.min(halfW - 0.25, z))
              );
            } else {
              // Gas: high-speed elastic bouncing across entire chamber volume up to topY
              const speed = 1.6 + (heatKJ - 80) * 0.06;
              const bounce = (val, minV, maxV) => {
                const span = Math.max(0.2, maxV - minV);
                const cycle = ((val % (2 * span)) + 2 * span) % (2 * span);
                return minV + (cycle <= span ? cycle : 2 * span - cycle);
              };
              const x = bounce(
                p.latticePos.x + elapsed * p.vel.x * speed * 2.2,
                -halfW + 0.25,
                halfW - 0.25
              );
              const y = bounce(
                p.latticePos.y + elapsed * p.vel.y * speed * 2.2,
                floorY + 0.25,
                topY - 0.22
              );
              const z = bounce(
                p.latticePos.z + elapsed * p.vel.z * speed * 2.2,
                -halfW + 0.25,
                halfW - 0.25
              );
              p.mesh.position.set(x, y, z);
            }
          });

          // Update intermolecular bond cylinders
          const up = new THREE.Vector3(0, 1, 0);
          bondPairs.forEach(({ mesh, a, b }) => {
            const pa = a.mesh.position;
            const pb = b.mesh.position;
            const diff = new THREE.Vector3().subVectors(pb, pa);
            const dist = diff.length();
            if (dist > 1.25) {
              mesh.visible = false;
            } else {
              mesh.visible = true;
              mesh.position.addVectors(pa, pb).multiplyScalar(0.5);
              mesh.scale.set(1, dist / 0.7, 1);
              mesh.quaternion.setFromUnitVectors(up, diff.normalize());
            }
          });
        },
      };
    },
    [heatKJ, volumeL, thermal]
  );

  // Heating curve & Boyle's curve points for synchronized bottom SVG graph
  const heatingPoints = useMemo(() => {
    const pts = [];
    for (let q = 0; q <= 100; q += 2) {
      pts.push({ x: q, y: computeHeatingState(q).tempC });
    }
    return pts;
  }, []);

  const boylePoints = useMemo(() => {
    const pts = [];
    for (let v = 1.2; v <= 4.0; v += 0.1) {
      pts.push({ x: v, y: (nMoles * R * tempK) / v });
    }
    return pts;
  }, [tempK, nMoles, R]);

  return (
    <div data-testid="kinetic-matter-states-aid" className="space-y-3 text-slate-800">
      {/* Parameter Controls */}
      <div className="p-3 bg-white rounded-xl border border-slate-200 shadow-xs space-y-3">
        {/* Quick Phase Preset Buttons */}
        <div className="flex flex-wrap items-center justify-between gap-1.5">
          <div className="flex flex-wrap gap-1">
            {[
              { label: 'Solid (-10 °C)', q: 7 },
              { label: 'Melting Plateau (0 °C)', q: 25 },
              { label: 'Liquid (50 °C)', q: 50 },
              { label: 'Boiling Plateau (100 °C)', q: 75 },
              { label: 'Gas (125 °C)', q: 94 },
            ].map((preset) => (
              <button
                key={preset.label}
                type="button"
                data-testid={`btn-phase-q-${preset.q}`}
                onClick={() => setHeatKJ(preset.q)}
                className={`px-2 py-1 rounded-lg text-[11px] font-bold border transition-all ${
                  Math.abs(heatKJ - preset.q) <= 6
                    ? 'bg-[#13519C] text-white border-[#13519C]'
                    : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                }`}
              >
                {preset.label}
              </button>
            ))}
          </div>

          <div className="flex items-center gap-1">
            <button
              type="button"
              data-testid="btn-chart-heating"
              onClick={() => setChartMode('heating')}
              className={`px-2 py-0.5 rounded text-[11px] font-semibold border ${
                chartMode === 'heating'
                  ? 'bg-slate-900 text-white border-slate-900'
                  : 'bg-white text-slate-600 border-slate-200'
              }`}
            >
              Heating Curve T(Q)
            </button>
            <button
              type="button"
              data-testid="btn-chart-boyle"
              onClick={() => setChartMode('boyle')}
              className={`px-2 py-0.5 rounded text-[11px] font-semibold border ${
                chartMode === 'boyle'
                  ? 'bg-slate-900 text-white border-slate-900'
                  : 'bg-white text-slate-600 border-slate-200'
              }`}
            >
              Boyle’s Law P(V)
            </button>
          </div>
        </div>

        {/* Sliders for Heat Added Q and Chamber Volume V */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-100">
          <div>
            <div className="flex items-center justify-between text-xs font-bold text-slate-700 mb-1">
              <span className="flex items-center gap-1">
                <Flame className="w-3.5 h-3.5 text-rose-600" />
                Heat Added (Q):
              </span>
              <span className="font-mono text-rose-700">
                {heatKJ} kJ → {Math.round(thermal.tempC)} °C ({tempK} K)
              </span>
            </div>
            <input
              type="range"
              min="0"
              max="100"
              step="1"
              value={heatKJ}
              data-testid="slider-heat-kj"
              onChange={(e) => setHeatKJ(Number(e.target.value))}
              className="w-full accent-rose-600 cursor-pointer"
            />
          </div>

          <div>
            <div className="flex items-center justify-between text-xs font-bold text-slate-700 mb-1">
              <span className="flex items-center gap-1">
                <Gauge className="w-3.5 h-3.5 text-[#13519C]" />
                Piston Volume (V):
              </span>
              <span className="font-mono text-[#13519C]">
                {volumeL.toFixed(1)} dm³ → P = {pressureKPa} kPa
              </span>
            </div>
            <input
              type="range"
              min="1.2"
              max="4.0"
              step="0.1"
              value={volumeL}
              data-testid="slider-volume-l"
              onChange={(e) => setVolumeL(Number(e.target.value))}
              className="w-full accent-[#13519C] cursor-pointer"
            />
          </div>
        </div>
      </div>

      {/* 3D Paper & Ink Particle Chamber */}
      <AtlasCanvas3D
        buildScene={buildScene}
        sceneDeps={[heatKJ, volumeL]}
        activeInteractiveId={activeCalcItem?.id}
        onSelectInteractive={(id) => setSelectedCalcId(id)}
        badgeText={thermal.phase}
        subBadgeText={
          thermal.isPlateau
            ? 'LATENT HEAT PLATEAU: Breaking intermolecular bonds at constant temperature!'
            : `T = ${Math.round(thermal.tempC)} °C (${tempK} K) • P = ${pressureKPa} kPa`
        }
      />

      {/* Interactive Calculation & Mechanism Popover */}
      <CalculationPopoverCard
        item={activeCalcItem}
        allItems={calcItems}
        onSelectItem={(it) => setSelectedCalcId(it.id)}
      />

      {/* Synchronized Heating Curve or Boyle's Law Graph */}
      {chartMode === 'heating' ? (
        <AtlasSyncChartSvg
          title="Synchronized Heating Curve of Matter T(Q)"
          subtitle={`T = ${Math.round(thermal.tempC)} °C`}
          xLabel="Heat Energy Added Q (kJ)"
          yLabel="Temperature (°C)"
          xDomain={[0, 100]}
          yDomain={[-25, 145]}
          series={[{ id: 'heating', points: heatingPoints, color: '#E11D48', strokeWidth: 2.5 }]}
          zones={[
            { xStart: 15, xEnd: 35, label: 'Melting (ΔT=0)', color: '#FEF3C7', textColor: '#B45309' },
            { xStart: 65, xEnd: 85, label: 'Boiling (ΔT=0)', color: '#FEF3C7', textColor: '#B45309' },
          ]}
          currentPoint={{
            x: heatKJ,
            y: thermal.tempC,
            color: '#13519C',
            label: `${heatKJ}kJ, ${Math.round(thermal.tempC)}°C`,
          }}
        />
      ) : (
        <AtlasSyncChartSvg
          title="Synchronized Boyle’s Law Isotherm P vs. V (p₁V₁ = p₂V₂)"
          subtitle={`pV = ${(pressureKPa * volumeL).toFixed(0)} J`}
          xLabel="Chamber Volume V (dm³)"
          yLabel="Gas Pressure P (kPa)"
          xDomain={[1.0, 4.2]}
          yDomain={[400, 3200]}
          series={[{ id: 'boyle', points: boylePoints, color: '#13519C', strokeWidth: 2.5 }]}
          currentPoint={{
            x: volumeL,
            y: pressureKPa,
            color: '#E11D48',
            label: `V=${volumeL.toFixed(1)}L, P=${pressureKPa}kPa`,
          }}
        />
      )}
    </div>
  );
}
