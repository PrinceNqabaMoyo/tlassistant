import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Wind, Droplets, TrendingUp } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import AtlasSyncChartSvg from '../shared/atlas3d/AtlasSyncChartSvg';
import { createBlock3D, createSphereAtom3D, createVectorArrow3D } from '../shared/atlas3d/atlasPartsKit';
import { createPaperMaterial, addInkEdges } from '../shared/atlas3d/atlasRenderEngine';

/**
 * PhysiologyExchangeAtlasAid
 * --------------------------
 * Grade 11–12 Life Sciences:
 * - Mode 1: Thoracic Ventilation (Boyle's Law Inhalation vs. Exhalation)
 *   Shows dome-shaped diaphragm flattening downwards + ribcage lifting -> ΔV > 0 -> P_thoracic < P_atm.
 * - Mode 2: Nephron Loop of Henle Counter-Current Multiplier & ADH Osmoregulation
 *   Shows medullary osmolarity gradient (300 -> 1200 mOsm/L) and ADH aquaporin water reabsorption.
 * - Mode 3: Population Ecology Logistic Growth & Carrying Capacity (K)
 *   Shows dN/dt = rN(1 - N/K) and environmental resistance.
 */

export default function PhysiologyExchangeAtlasAid() {
  const [mode, setMode] = useState('ventilation'); // 'ventilation' | 'nephron' | 'ecology'
  const [diaphragmPull, setDiaphragmPull] = useState(0.75); // 0 = Exhaled (Dome up), 1 = Inhaled (Flattened down)
  const [adhLevel, setAdhLevel] = useState(80); // % ADH secretion (High on hot/dehydrated day)
  const [carryingCapK, setCarryingCapK] = useState(500);
  const [selectedId, setSelectedId] = useState('boyle_inhalation');

  const physMath = useMemo(() => {
    // Thoracic volume in Litres (2.5 L FRC up to 3.2 L with tidal inspiration)
    const vLung = 2.4 + diaphragmPull * 0.8;
    // Intra-alveolar pressure relative to 760 mmHg atmospheric
    const pAlveolar = 762 - diaphragmPull * 5.0; // drops to ~757 mmHg during inhalation
    const urineOsm = 150 + (adhLevel / 100) * 1050; // mOsm/L

    return { vLung, pAlveolar, urineOsm };
  }, [diaphragmPull, adhLevel]);

  const calculationsMap = useMemo(() => {
    if (mode === 'nephron') {
      return {
        loop_of_henle: {
          id: 'loop_of_henle',
          symbol: '\\text{Na}^+/\\text{Cl}^- \\text{ Pump}',
          label: 'Ascending Limb Active Na⁺/Cl⁻ Pump (Hypertonic Medulla)',
          color: '#D97706',
          badgeText: 'Medulla: 1200 mOsm/L',
          formula: '\\text{Ascending Limb (Impermeable to H}_2\\text{O)} \\xrightarrow{\\text{Active Na}^+\\text{ Pump}} \\text{Low } \\Psi_{\\text{medulla}}',
          substitution: '\\text{Descending limb permeable to H}_2\\text{O}; \\text{ Ascending limb actively pumps out Na}^+/\\text{Cl}^-',
          result: '\\text{Establishes steep osmotic gradient in renal medulla}',
          meaning: 'The Loop of Henle acts as a counter-current multiplier: pumping Na⁺ and Cl⁻ out of the water-impermeable ascending limb makes the renal medulla strongly hypertonic (low water potential).',
        },
        adh_collecting: {
          id: 'adh_collecting',
          symbol: `\\text{ADH} = ${adhLevel}\\%`,
          label: 'Collecting Duct ADH Aquaporin Permeability',
          color: '#2B5B84',
          badgeText: `Urine: ${physMath.urineOsm.toFixed(0)} mOsm/L`,
          formula: '\\uparrow \\text{ADH (Hypothalamus/Pituitary)} \\implies \\uparrow \\text{Aquaporins} \\implies \\uparrow \\text{H}_2\\text{O Reabsorption}',
          substitution: `\\text{ADH Level} = ${adhLevel}\\% \\implies \\text{Filtrate Osmolarity} \\approx ${physMath.urineOsm.toFixed(0)}\\text{ mOsm\\cdot L}^{-1}`,
          result: adhLevel >= 50
            ? '\\text{Small volume of concentrated urine excreted (Water conserved)}'
            : '\\text{Large volume of dilute urine excreted (Hydrated state)}',
          meaning: 'Osmoreceptors in the hypothalamus detect blood water potential and adjust ADH release from the pituitary gland to regulate collecting duct wall permeability.',
        },
      };
    }

    if (mode === 'ecology') {
      return {
        logistic_k: {
          id: 'logistic_k',
          symbol: 'K',
          label: `Logistic Growth & Carrying Capacity (K = ${carryingCapK})`,
          color: '#2D6A4F',
          badgeText: `K = ${carryingCapK} individuals`,
          formula: '\\frac{dN}{dt} = r N \\left(1 - \\frac{N}{K}\\right)',
          substitution: `\\text{Max growth rate at } N = \\frac{K}{2} = ${Math.round(carryingCapK / 2)}; \\text{ Equilibrium at } N = ${carryingCapK}`,
          result: `\\text{Carrying Capacity } K = ${carryingCapK}`,
          meaning: 'As population size N approaches carrying capacity K, environmental resistance (limited food, space, predation, disease) slows net growth toward zero.',
        },
      };
    }

    return {
      boyle_inhalation: {
        id: 'boyle_inhalation',
        symbol: 'P_{\\text{thoracic}} \\propto \\frac{1}{V_{\\text{thoracic}}}',
        label: diaphragmPull >= 0.5 ? 'Active Inhalation (Diaphragm Contracts & Flattens)' : 'Passive Exhalation (Diaphragm Relaxes into Dome)',
        color: '#2B5B84',
        badgeText: `V = ${physMath.vLung.toFixed(2)} L | P = ${physMath.pAlveolar.toFixed(1)} mmHg`,
        formula: 'P_1 V_1 = P_2 V_2 \\implies \\uparrow V_{\\text{thoracic}} \\text{ causes } P_{\\text{alveolar}} < P_{\\text{atm}}',
        substitution: `V_{\\text{lung}} = ${physMath.vLung.toFixed(2)}\\text{ L} \\implies P_{\\text{alv}} = ${physMath.pAlveolar.toFixed(1)}\\text{ mmHg vs } P_{\\text{atm}} = 760\\text{ mmHg}`,
        result: diaphragmPull >= 0.5
          ? '\\Delta P < 0 \\implies \\text{Air rushes IN down pressure gradient}'
          : '\\Delta P > 0 \\implies \\text{Air forced OUT of lungs}',
        meaning: 'Muscles do not inflate the lungs directly—contracting the diaphragm (flattening downward) and external intercostals (lifting the ribcage) expands thoracic volume, dropping internal pressure below atmospheric pressure.',
      },
    };
  }, [adhLevel, carryingCapK, diaphragmPull, mode, physMath]);

  const activeCalculation = calculationsMap[selectedId] || Object.values(calculationsMap)[0];

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    if (mode === 'ventilation') {
      // Thoracic bell jar / ribcage + 2 inflatable lung lobes + moving diaphragm floor
      const lungScale = 0.82 + diaphragmPull * 0.28;
      const lobeGeo = new THREE.SphereGeometry(0.55, 24, 20);
      lobeGeo.scale(0.85, lungScale * 1.35, 0.85);

      const leftLung = new THREE.Mesh(lobeGeo, createPaperMaterial(0xF43F5E, { opacity: 0.78, transparent: true }));
      addInkEdges(leftLung, 0x1E1B18, 0.7);
      leftLung.position.set(-0.65, 1.25, 0);
      leftLung.userData = { interactiveId: 'boyle_inhalation' };

      const rightLung = new THREE.Mesh(lobeGeo, createPaperMaterial(0xF43F5E, { opacity: 0.78, transparent: true }));
      addInkEdges(rightLung, 0x1E1B18, 0.7);
      rightLung.position.set(0.65, 1.25, 0);
      rightLung.userData = { interactiveId: 'boyle_inhalation' };
      root.add(leftLung, rightLung);

      // Trachea tube
      const trachea = createBlock3D({ width: 0.22, height: 0.9, depth: 0.22, color: 0x38BDF8, interactiveId: 'boyle_inhalation' });
      trachea.position.set(0, 2.1, 0);
      root.add(trachea);

      // Diaphragm sheet at bottom (flattens downward as diaphragmPull -> 1)
      const diaY = 0.55 - diaphragmPull * 0.38;
      const diaGeo = new THREE.CylinderGeometry(1.45, 1.55, 0.12, 28);
      const diaMesh = new THREE.Mesh(diaGeo, createPaperMaterial(0xB8432E));
      addInkEdges(diaMesh, 0x1E1B18, 0.8);
      diaMesh.position.set(0, diaY, 0);
      diaMesh.userData = { interactiveId: 'boyle_inhalation', labelPoint: [0, diaY + 0.25, 0] };
      root.add(diaMesh);
    } else if (mode === 'nephron') {
      // 3D U-shaped Loop of Henle + Collecting Duct
      const descLimb = createBlock3D({ width: 0.22, height: 1.8, depth: 0.22, color: 0x38BDF8, interactiveId: 'loop_of_henle' });
      descLimb.position.set(-0.85, 1.05, 0);
      const ascLimb = createBlock3D({ width: 0.28, height: 1.8, depth: 0.28, color: 0xD97706, interactiveId: 'loop_of_henle' });
      ascLimb.position.set(-0.15, 1.05, 0);
      const hairPin = createBlock3D({ width: 0.95, height: 0.22, depth: 0.22, color: 0xD97706, interactiveId: 'loop_of_henle' });
      hairPin.position.set(-0.5, 0.2, 0);

      // Collecting duct at x = +0.85 with H2O arrows proportional to adhLevel
      const collectDuct = createBlock3D({ width: 0.32, height: 2.0, depth: 0.32, color: 0x2B5B84, interactiveId: 'adh_collecting' });
      collectDuct.position.set(0.85, 1.1, 0);
      root.add(descLimb, ascLimb, hairPin, collectDuct);

      const arrowCount = Math.max(1, Math.round((adhLevel / 100) * 4));
      for (let i = 0; i < arrowCount; i++) {
        const h2oArrow = createVectorArrow3D({
          origin: [1.05, 0.45 + i * 0.42, 0],
          direction: [1, 0, 0],
          length: 0.55,
          color: 0x0EA5E9,
          interactiveId: 'adh_collecting',
        });
        root.add(h2oArrow);
      }
    } else {
      // 3D Ecological Carrying Capacity K habitat platform with population spheres
      const platform = createBlock3D({ width: 3.4, height: 0.14, depth: 2.2, color: 0x2D6A4F, interactiveId: 'logistic_k' });
      platform.position.set(0, 0.07, 0);
      root.add(platform);

      const count = Math.min(28, Math.max(6, Math.round(carryingCapK / 25)));
      for (let i = 0; i < count; i++) {
        const row = Math.floor(i / 7);
        const col = i % 7;
        const s = createSphereAtom3D({ radius: 0.12, color: 0xD97706, interactiveId: 'logistic_k' });
        s.position.set((col - 3) * 0.42, 0.26, (row - 1.5) * 0.45);
        root.add(s);
      }
    }

    return { interactiveObjects: [root] };
  }, [adhLevel, carryingCapK, diaphragmPull, mode]);

  const logisticSeries = useMemo(() => {
    const pts = [];
    const n0 = 15;
    const r = 0.45;
    for (let t = 0; t <= 20; t += 1) {
      const n = carryingCapK / (1 + ((carryingCapK - n0) / n0) * Math.exp(-r * t));
      pts.push({ x: t, y: n });
    }
    return [{ id: 'log', label: `Logistic S-Curve (K = ${carryingCapK})`, color: '#2D6A4F', fillArea: true, points: pts }];
  }, [carryingCapK]);

  return (
    <div data-testid="physiology-exchange-atlas-aid" className="space-y-4 text-slate-800">
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-teal-100 text-teal-900 uppercase tracking-wider">
              Grade 11–12 Life Sciences • Physiological Systems
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              {mode === 'ventilation'
                ? "Thoracic Breathing Mechanics (Boyle's Law Pressure-Volume)"
                : mode === 'nephron'
                ? 'Nephron Loop of Henle Counter-Current & ADH Osmoregulation'
                : 'Population Ecology S-Curve & Carrying Capacity (K)'}
            </h4>
          </div>

          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-phys-ventilation"
              onClick={() => {
                setMode('ventilation');
                setSelectedId('boyle_inhalation');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 ${
                mode === 'ventilation' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              <Wind className="w-3.5 h-3.5" />
              Breathing
            </button>
            <button
              type="button"
              data-testid="btn-phys-nephron"
              onClick={() => {
                setMode('nephron');
                setSelectedId('adh_collecting');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 ${
                mode === 'nephron' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              <Droplets className="w-3.5 h-3.5" />
              Nephron ADH
            </button>
            <button
              type="button"
              data-testid="btn-phys-ecology"
              onClick={() => {
                setMode('ecology');
                setSelectedId('logistic_k');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 ${
                mode === 'ecology' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              <TrendingUp className="w-3.5 h-3.5" />
              Carrying Cap K
            </button>
          </div>
        </div>

        {mode === 'ventilation' && (
          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-xs font-semibold text-slate-700">
              <span>Diaphragm Contraction (0% = Exhaled Dome, 100% = Inhaled Flat)</span>
              <span className="font-mono font-bold text-[#2B5B84]">
                {Math.round(diaphragmPull * 100)}% → V = {physMath.vLung.toFixed(2)} L
              </span>
            </div>
            <input
              type="range"
              min="0"
              max="1"
              step="0.05"
              value={diaphragmPull}
              onChange={(e) => setDiaphragmPull(parseFloat(e.target.value))}
              className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
            />
          </label>
        )}

        {mode === 'nephron' && (
          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-xs font-semibold text-slate-700">
              <span>ADH Hormone Concentration (Collecting Duct Permeability)</span>
              <span className="font-mono font-bold text-[#2B5B84]">
                {adhLevel}% ({physMath.urineOsm.toFixed(0)} mOsm/L)
              </span>
            </div>
            <input
              type="range"
              min="10"
              max="100"
              step="5"
              value={adhLevel}
              onChange={(e) => setAdhLevel(parseInt(e.target.value, 10))}
              className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
            />
          </label>
        )}

        {mode === 'ecology' && (
          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-xs font-semibold text-slate-700">
              <span>Habitat Carrying Capacity (K)</span>
              <span className="font-mono font-bold text-emerald-700">K = {carryingCapK}</span>
            </div>
            <input
              type="range"
              min="200"
              max="800"
              step="50"
              value={carryingCapK}
              onChange={(e) => setCarryingCapK(parseInt(e.target.value, 10))}
              className="w-full accent-emerald-600 cursor-pointer h-1.5"
            />
          </label>
        )}
      </div>

      <AtlasCanvas3D
        testId="physiology-exchange-3d-canvas"
        height={290}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle="Click 3D structures or floating badges to inspect the underlying physiological equations"
      />

      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />

      {mode === 'ecology' && (
        <AtlasSyncChartSvg
          title="Logistic Population Growth Curve N(t) Approaching Carrying Capacity K"
          xLabel="Time Generations (t)"
          yLabel="Population Size N"
          xDomain={[0, 20]}
          yDomain={[0, 850]}
          series={logisticSeries}
          activePoint={{
            x: 15,
            y: carryingCapK * 0.96,
            label: `K = ${carryingCapK}`,
            color: '#2D6A4F',
          }}
        />
      )}
    </div>
  );
}
