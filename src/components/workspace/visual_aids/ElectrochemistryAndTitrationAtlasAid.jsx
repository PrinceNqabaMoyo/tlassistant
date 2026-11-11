import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { FlaskConical, BatteryCharging } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import AtlasSyncChartSvg from '../shared/atlas3d/AtlasSyncChartSvg';
import { createBlock3D, createSphereAtom3D, createVectorArrow3D } from '../shared/atlas3d/atlasPartsKit';
import { createPaperMaterial, addInkEdges } from '../shared/atlas3d/atlasRenderEngine';

/**
 * ElectrochemistryAndTitrationAtlasAid
 * ------------------------------------
 * Grade 11–12 Physical Sciences (Chemistry):
 * - Mode 1: 3D Galvanic (Zn-Cu) Cell & Salt Bridge Ion Migration
 *   Shows Zn -> Zn2+ + 2e- oxidation at anode, Cu2+ + 2e- -> Cu plating at cathode,
 *   NO3- / K+ salt bridge electrical neutrality, and standard cell potential E°cell.
 * - Mode 2: 3D Burette Acid-Base Titration & Sigmoidal pH Equivalence Explorer
 *   Shows drop-by-drop NaOH addition into acid, equivalence point jump, and indicator transition.
 */

export default function ElectrochemistryAndTitrationAtlasAid() {
  const [mode, setMode] = useState('galvanic'); // 'galvanic' | 'titration'
  const [volAddedMl, setVolAddedMl] = useState(24.0); // mL of 0.10 M NaOH added to 25.0 mL of 0.10 M HCl
  const [selectedId, setSelectedId] = useState('cell_emf');

  const eAnodeZn = -0.76;
  const eCathodeCu = +0.34;
  const eCell = eCathodeCu - eAnodeZn; // +1.10 V

  // Compute titration pH for 25.0 mL of 0.10 M strong acid + V mL of 0.10 M NaOH
  const titrationMath = useMemo(() => {
    const vAcid = 25.0;
    const cAcid = 0.10;
    const cBase = 0.10;
    const nAcid = (vAcid / 1000) * cAcid;
    const nBase = (volAddedMl / 1000) * cBase;
    const vTotalL = (vAcid + volAddedMl) / 1000;

    let pH = 7.0;
    if (Math.abs(volAddedMl - vAcid) < 0.08) {
      pH = 7.0;
    } else if (volAddedMl < vAcid) {
      const hConc = Math.max(1e-7, (nAcid - nBase) / vTotalL);
      pH = -Math.log10(hConc);
    } else {
      const ohConc = Math.max(1e-7, (nBase - nAcid) / vTotalL);
      const pOH = -Math.log10(ohConc);
      pH = 14.0 - pOH;
    }

    return { vAcid, cAcid, cBase, nAcid, nBase, pH };
  }, [volAddedMl]);

  const calculationsMap = useMemo(() => {
    if (mode === 'titration') {
      const { nAcid, nBase, pH } = titrationMath;
      return {
        equivalence_calc: {
          id: 'equivalence_calc',
          symbol: '\\frac{c_a V_a}{c_b V_b} = \\frac{n_a}{n_b}',
          label: `Acid-Base Titration Stoichiometry & pH (${pH.toFixed(2)})`,
          color: pH >= 7 ? '#EC4899' : '#2B5B84',
          badgeText: `pH = ${pH.toFixed(2)}`,
          formula: 'n(\\text{HCl}) = c_a V_a,\\quad n(\\text{NaOH}) = c_b V_b',
          substitution: `n_a = (0.10)(0.0250) = ${nAcid.toFixed(4)}\\text{ mol},\\quad n_b = (0.10)(${(volAddedMl / 1000).toFixed(4)}) = ${nBase.toFixed(4)}\\text{ mol}`,
          result: `V_{\\text{added}} = ${volAddedMl.toFixed(1)}\\text{ cm}^3 \\implies \\text{pH} = ${pH.toFixed(2)}`,
          meaning: Math.abs(volAddedMl - 25) < 0.5
            ? 'At the equivalence point (25.0 cm³), moles of H₃O⁺ equal moles of OH⁻, causing a vertical pH jump through pH 7.00 (Bromothymol Blue turns green).'
            : volAddedMl < 25
            ? 'Excess H₃O⁺ ions remain in the conical flask before the equivalence point.'
            : 'Excess OH⁻ ions turn Phenolphthalein pink above pH 8.2.',
        },
      };
    }

    return {
      cell_emf: {
        id: 'cell_emf',
        symbol: 'E^\\circ_{\\text{cell}}',
        label: 'Standard Cell Potential (Voltmeter Reading)',
        color: '#2B5B84',
        badgeText: `E°cell = +${eCell.toFixed(2)} V`,
        formula: 'E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}}',
        substitution: `E^\\circ_{\\text{cell}} = (+0.34\\text{ V}) - (-0.76\\text{ V})`,
        result: `E^\\circ_{\\text{cell}} = +1.10\\text{ V (Spontaneous)}`,
        meaning: 'Because E°cell > 0 V, the redox reaction is spontaneous, converting chemical energy into electrical energy as electrons flow from the Zn anode to the Cu cathode.',
      },
      anode_zn: {
        id: 'anode_zn',
        symbol: '\\text{Zn(s)} \\to \\text{Zn}^{2+} + 2e^-',
        label: 'Zinc Anode (Oxidation — Mass Decreases)',
        color: '#64748B',
        badgeText: 'Anode (−): Zn Oxidation',
        formula: '\\text{Zn(s)} \\longrightarrow \\text{Zn}^{2+}\\text{(aq)} + 2e^- \\quad (E^\\circ = -0.76\\text{ V})',
        substitution: '\\text{Solid Zn atoms lose } 2e^- \\text{ and dissolve into solution as } \\text{Zn}^{2+}',
        result: '\\text{Anode mass decreases; } [\\text{Zn}^{2+}] \\text{ increases}',
        meaning: 'In a galvanic cell, oxidation always occurs at the negative anode. Released electrons travel up the external wire toward the voltmeter.',
      },
      cathode_cu: {
        id: 'cathode_cu',
        symbol: '\\text{Cu}^{2+} + 2e^- \\to \\text{Cu(s)}',
        label: 'Copper Cathode (Reduction — Mass Increases)',
        color: '#D97706',
        badgeText: 'Cathode (+): Cu Plating',
        formula: '\\text{Cu}^{2+}\\text{(aq)} + 2e^- \\longrightarrow \\text{Cu(s)} \\quad (E^\\circ = +0.34\\text{ V})',
        substitution: '\\text{Blue } \\text{Cu}^{2+} \\text{ ions accept } 2e^- \\text{ and plate onto the Cu electrode}',
        result: '\\text{Cathode mass increases; blue colour fades}',
        meaning: 'Reduction occurs at the positive cathode as arriving electrons reduce aqueous Cu²⁺ ions into solid copper metal.',
      },
      salt_bridge: {
        id: 'salt_bridge',
        symbol: '\\text{KNO}_3 \\text{ Salt Bridge}',
        label: 'Salt Bridge Ion Migration (Electrical Neutrality)',
        color: '#2D6A4F',
        badgeText: 'Anions → Anode | Cations → Cathode',
        formula: '\\text{NO}_3^- \\to \\text{Anode beaker},\\quad \\text{K}^+ \\to \\text{Cathode beaker}',
        substitution: '\\text{Balances excess } \\text{Zn}^{2+} \\text{ at anode and depleted } \\text{Cu}^{2+} \\text{ at cathode}',
        result: '\\text{Completes internal circuit & maintains neutrality}',
        meaning: 'Without the salt bridge, positive charge buildup in the Zn²⁺ half-cell would immediately halt electron flow.',
      },
    };
  }, [eCell, mode, titrationMath, volAddedMl]);

  const activeCalculation = calculationsMap[selectedId] || Object.values(calculationsMap)[0];

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    if (mode === 'galvanic') {
      // Left Beaker (ZnSO4) & Right Beaker (CuSO4)
      const beakerGeo = new THREE.CylinderGeometry(0.85, 0.85, 1.35, 24);
      const leftBeaker = new THREE.Mesh(beakerGeo, createPaperMaterial(0xE2E8F0, { opacity: 0.48, transparent: true }));
      addInkEdges(leftBeaker, 0x1E1B18, 0.5);
      leftBeaker.position.set(-1.35, 0.68, 0);
      root.add(leftBeaker);

      const rightBeaker = new THREE.Mesh(beakerGeo, createPaperMaterial(0x38BDF8, { opacity: 0.45, transparent: true }));
      addInkEdges(rightBeaker, 0x1E1B18, 0.5);
      rightBeaker.position.set(1.35, 0.68, 0);
      root.add(rightBeaker);

      // Zn Anode Electrode
      const znElectrode = createBlock3D({
        width: 0.28,
        height: 1.55,
        depth: 0.12,
        color: 0x64748B,
        interactiveId: 'anode_zn',
      });
      znElectrode.position.set(-1.55, 1.0, 0);
      root.add(znElectrode);

      // Cu Cathode Electrode
      const cuElectrode = createBlock3D({
        width: 0.28,
        height: 1.55,
        depth: 0.12,
        color: 0xD97706,
        interactiveId: 'cathode_cu',
      });
      cuElectrode.position.set(1.55, 1.0, 0);
      root.add(cuElectrode);

      // U-shaped Salt Bridge connecting both beakers
      const bridgeGroup = new THREE.Group();
      bridgeGroup.userData = { interactiveId: 'salt_bridge', labelPoint: [0, 1.65, 0] };
      const bridgeTop = createBlock3D({ width: 2.1, height: 0.2, depth: 0.2, color: 0x2D6A4F, interactiveId: 'salt_bridge' });
      bridgeTop.position.set(0, 1.55, 0);
      const bridgeL = createBlock3D({ width: 0.2, height: 0.85, depth: 0.2, color: 0x2D6A4F, interactiveId: 'salt_bridge' });
      bridgeL.position.set(-0.95, 1.15, 0);
      const bridgeR = createBlock3D({ width: 0.2, height: 0.85, depth: 0.2, color: 0x2D6A4F, interactiveId: 'salt_bridge' });
      bridgeR.position.set(0.95, 1.15, 0);
      bridgeGroup.add(bridgeTop, bridgeL, bridgeR);
      root.add(bridgeGroup);

      // External wire & Voltmeter box at top
      const vmBox = createBlock3D({
        width: 0.75,
        height: 0.42,
        depth: 0.25,
        color: 0x2B5B84,
        interactiveId: 'cell_emf',
      });
      vmBox.position.set(0, 2.25, 0);
      root.add(vmBox);

      const eArrow = createVectorArrow3D({
        origin: [-1.2, 2.25, 0],
        direction: [1, 0, 0],
        length: 2.4,
        color: 0x2B5B84,
        interactiveId: 'cell_emf',
      });
      root.add(eArrow);
    } else {
      // 3D Burette & Conical Flask Titration Setup
      const flaskColor = titrationMath.pH > 8.2 ? 0xEC4899 : titrationMath.pH >= 6.8 ? 0x10B981 : 0x38BDF8;
      const flaskGeo = new THREE.ConeGeometry(0.95, 1.35, 24);
      const flaskMesh = new THREE.Mesh(
        flaskGeo,
        createPaperMaterial(flaskColor, { opacity: 0.65, transparent: true })
      );
      addInkEdges(flaskMesh, 0x1E1B18, 0.6);
      flaskMesh.position.set(0, 0.68, 0);
      flaskMesh.userData = { interactiveId: 'equivalence_calc' };
      root.add(flaskMesh);

      // Burette cylinder above flask
      const buretteGeo = new THREE.CylinderGeometry(0.12, 0.12, 1.6, 16);
      const buretteMesh = new THREE.Mesh(buretteGeo, createPaperMaterial(0xF8FAFC, { opacity: 0.8, transparent: true }));
      addInkEdges(buretteMesh, 0x1E1B18, 0.7);
      buretteMesh.position.set(0, 2.25, 0);
      buretteMesh.userData = { interactiveId: 'equivalence_calc' };
      root.add(buretteMesh);

      const dropSphere = createSphereAtom3D({
        radius: 0.08,
        color: 0x2B5B84,
        interactiveId: 'equivalence_calc',
      });
      dropSphere.position.set(0, 1.35, 0);
      root.add(dropSphere);
    }

    return { interactiveObjects: [root] };
  }, [mode, titrationMath.pH]);

  // Titration pH curve
  const phSeries = useMemo(() => {
    const pts = [];
    for (let v = 0; v <= 40; v += 1) {
      let ph = 7;
      if (Math.abs(v - 25) < 0.2) ph = 7;
      else if (v < 25) {
        const h = ((25 - v) * 0.1) / (25 + v);
        ph = -Math.log10(Math.max(1e-7, h));
      } else {
        const oh = ((v - 25) * 0.1) / (25 + v);
        ph = 14 + Math.log10(Math.max(1e-7, oh));
      }
      pts.push({ x: v, y: ph });
    }
    return [{ id: 'ph', label: 'pH vs Volume NaOH', color: '#2B5B84', points: pts }];
  }, []);

  return (
    <div data-testid="electrochemistry-titration-atlas-aid" className="space-y-4 text-slate-800">
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-emerald-100 text-emerald-900 uppercase tracking-wider">
              Electrochemistry & Quantitative Chemical Change
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              {mode === 'galvanic'
                ? '3D Galvanic (Zn-Cu) Cell, Salt Bridge & Standard Potentials'
                : '3D Burette Acid-Base Titration & Sigmoidal Equivalence Curve'}
            </h4>
          </div>

          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-mode-galvanic"
              onClick={() => {
                setMode('galvanic');
                setSelectedId('cell_emf');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 ${
                mode === 'galvanic' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              <BatteryCharging className="w-3.5 h-3.5" />
              Galvanic Cell
            </button>
            <button
              type="button"
              data-testid="btn-mode-titration"
              onClick={() => {
                setMode('titration');
                setSelectedId('equivalence_calc');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 ${
                mode === 'titration' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              <FlaskConical className="w-3.5 h-3.5" />
              Acid-Base Titration
            </button>
          </div>
        </div>

        {mode === 'titration' && (
          <label className="bg-slate-50 p-2.5 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-xs font-semibold text-slate-700">
              <span>Volume of 0.10 M NaOH Added from Burette</span>
              <span className="font-mono font-bold text-[#2B5B84]">
                {volAddedMl.toFixed(1)} cm³ (pH = {titrationMath.pH.toFixed(2)})
              </span>
            </div>
            <input
              type="range"
              min="0"
              max="40"
              step="0.5"
              value={volAddedMl}
              onChange={(e) => setVolAddedMl(parseFloat(e.target.value))}
              className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
            />
          </label>
        )}
      </div>

      <AtlasCanvas3D
        testId="electrochemistry-titration-3d-canvas"
        height={300}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle={
          mode === 'galvanic'
            ? 'Click the Zn Anode, Cu Cathode, Salt Bridge, or Voltmeter to inspect half-reactions & E°cell'
            : 'Scrub NaOH volume through 25.0 cm³ to observe the equivalence point pH jump and indicator colour shift'
        }
      />

      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />

      {mode === 'titration' && (
        <AtlasSyncChartSvg
          title="Strong Acid + Strong Base Titration Curve (pH vs Volume NaOH)"
          xLabel="Volume NaOH Added (cm³)"
          yLabel="Solution pH"
          xDomain={[0, 40]}
          yDomain={[0, 14]}
          series={phSeries}
          activePoint={{
            x: volAddedMl,
            y: titrationMath.pH,
            label: `pH ${titrationMath.pH.toFixed(2)}`,
            color: '#2B5B84',
          }}
        />
      )}
    </div>
  );
}
