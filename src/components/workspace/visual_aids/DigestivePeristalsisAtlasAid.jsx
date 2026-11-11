import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Activity, Play, Pause, RotateCcw } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import AtlasSyncChartSvg from '../shared/atlas3d/AtlasSyncChartSvg';
import {
  createPeristalsisTube3D,
  createSphereAtom3D,
  createVectorArrow3D,
} from '../shared/atlas3d/atlasPartsKit';
import { createPaperMaterial, addInkEdges } from '../shared/atlas3d/atlasRenderEngine';

/**
 * DigestivePeristalsisAtlasAid
 * ----------------------------
 * Grade 9 Natural Sciences & Grade 11 Life Sciences (Animal Nutrition):
 * 1. 3D Antagonistic Peristalsis Wave Simulator:
 *    Shows circular smooth muscle contracting BEHIND the food bolus (constraining lumen)
 *    while longitudinal smooth muscle contracts AHEAD (shortening & widening the lumen).
 *    Includes an "Invert Gravity (Upside-Down Swallow)" toggle proving peristalsis is an
 *    active muscular wave independent of gravity.
 * 2. Regional Alimentary Canal pH & Enzyme Hydrolysis:
 *    Mouth (Salivary Amylase, pH 7.0) -> Stomach (Pepsin + HCl, pH 2.0) -> Duodenum/Ileum
 *    (Bile emulsification + Pancreatic Lipase/Trypsin, pH 8.0).
 * 3. 3D Intestinal Villus Absorption Pathway:
 *    Glucose & Amino Acids -> Blood Capillaries -> Hepatic Portal Vein -> Liver;
 *    Fatty Acids & Glycerol -> Central Lacteal -> Thoracic Lymph Duct.
 */

export default function DigestivePeristalsisAtlasAid() {
  const [stageMode, setStageMode] = useState('peristalsis'); // 'peristalsis' | 'villus'
  const [bolusPos, setBolusPos] = useState(0.32); // 0.0 (oesophagus) -> 1.0 (ileum)
  const [invertedGravity, setInvertedGravity] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);
  const [selectedId, setSelectedId] = useState('circular_muscle');

  // Determine alimentary region from bolusPos (0..1)
  const regionInfo = useMemo(() => {
    if (bolusPos < 0.33) {
      return {
        region: 'Mouth & Oesophagus',
        pH: 7.0,
        enzyme: 'Salivary Amylase (Carbohydrase)',
        substrate: 'Starch (Polysaccharide) + H₂O → Maltose (Disaccharide)',
        color: '#2B5B84',
      };
    }
    if (bolusPos < 0.66) {
      return {
        region: 'Stomach (Gastric Lumen)',
        pH: 2.0,
        enzyme: 'Pepsin (Endopeptidase) + HCl',
        substrate: 'Proteins (Polypeptides) + H₂O → Shorter Polypeptides / Peptones',
        color: '#B8432E',
      };
    }
    return {
      region: 'Duodenum & Small Intestine (Ileum)',
      pH: 8.0,
      enzyme: 'Bile Salts + Pancreatic Lipase, Trypsin & Maltase',
      substrate: 'Emulsified Lipids → Glycerol + Fatty Acids; Maltose → Glucose',
      color: '#2D6A4F',
    };
  }, [bolusPos]);

  const calculationsMap = useMemo(() => {
    if (stageMode === 'villus') {
      return {
        hepatic_portal: {
          id: 'hepatic_portal',
          symbol: '\\text{Capillaries} \\to \\text{Hepatic Portal Vein}',
          label: 'Blood Capillary Network (Glucose & Amino Acids)',
          color: '#B8432E',
          badgeText: 'Glucose & Amino Acids → Liver',
          formula: '\\text{Active Transport + Facilitated Diffusion} \\longrightarrow \\text{Hepatic Portal Vein}',
          substitution: '\\text{One-cell-thick columnar epithelium with microvilli maximizes surface area } A',
          result: '\\text{Monosaccharides \\& Amino Acids transported to Liver}',
          meaning: 'Water-soluble monomers (glucose and amino acids) cross the single-layered columnar epithelium into the dense capillary network and travel via the Hepatic Portal Vein to the liver for homeostatic regulation.',
        },
        lacteal_lymph: {
          id: 'lacteal_lymph',
          symbol: '\\text{Central Lacteal (Lipids)}',
          label: 'Central Lacteal Lymphatic Vessel (Fatty Acids & Glycerol)',
          color: '#D97706',
          badgeText: 'Chylomicrons → Lymph Duct',
          formula: '\\text{Bile Emulsification} \\to \\text{Micelles} \\to \\text{Chylomicrons in Lacteal}',
          substitution: '\\text{Fatty acids \\& glycerol re-esterify inside epithelial cells before entering the lacteal}',
          result: '\\text{Absorbed into Lymphatic System (Left Subclavian Vein)}',
          meaning: 'Lipid digestion products are absorbed into the central blind-ending lymphatic vessel (lacteal) rather than directly into blood capillaries.',
        },
      };
    }

    return {
      circular_muscle: {
        id: 'circular_muscle',
        symbol: 'P_{\\text{behind}} > P_{\\text{ahead}}',
        label: 'Antagonistic Peristalsis Wave (Circular vs. Longitudinal Muscle)',
        color: '#B8432E',
        badgeText: 'Circular Contracts Behind',
        formula: '\\text{Behind Bolus: Circular Contracts (Lumen Constricts)} \\implies F_{\\text{propulsion}} \\to +x',
        substitution: `\\text{Bolus at } ${Math.round(bolusPos * 100)}\\% \\text{ of tract (${regionInfo.region})}`,
        result: invertedGravity
          ? '\\text{Bolus moves UPWARD against gravity } (-\\vec{g}) \\text{ via muscular wave!}'
          : '\\text{Bolus propelled forward along alimentary canal}',
        meaning: 'Peristalsis is an involuntary wave of antagonistic smooth muscle contraction: circular muscles contract BEHIND the food bolus (squeezing it forward) while longitudinal muscles contract AHEAD of the bolus (widening the lumen to receive it).',
      },
      enzyme_ph: {
        id: 'enzyme_ph',
        symbol: `\\text{pH} = ${regionInfo.pH.toFixed(1)}`,
        label: `${regionInfo.region} — Optimal Enzyme pH & Hydrolysis`,
        color: regionInfo.color,
        badgeText: `pH ${regionInfo.pH.toFixed(1)}: ${regionInfo.enzyme.split(' ')[0]}`,
        formula: `\\text{Substrate} + \\text{H}_2\\text{O} \\xrightarrow{\\text{${regionInfo.enzyme.split('(')[0].trim()}}} \\text{Absorbable Monomers}`,
        substitution: `\\text{Active at } \\text{pH} = ${regionInfo.pH.toFixed(1)}: \\text{ ${regionInfo.substrate}}`,
        result: `\\text{Optimal Rate at pH } ${regionInfo.pH.toFixed(1)}`,
        meaning: 'Each region of the human alimentary canal maintains a specific pH so its digestive enzymes maintain their 3D active-site conformation without denaturation.',
      },
    };
  }, [bolusPos, invertedGravity, regionInfo, stageMode]);

  const activeCalculation = calculationsMap[selectedId] || Object.values(calculationsMap)[0];

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    if (stageMode === 'peristalsis') {
      const tractGroup = new THREE.Group();
      if (invertedGravity) {
        // Tilt tract upward at 35° to show upward swallowing against gravity
        tractGroup.rotation.z = 0.55;
      }

      const tubeObj = createPeristalsisTube3D({
        length: 4.2,
        baseRadius: 0.42,
        bolusT: bolusPos,
        interactiveId: 'circular_muscle',
      });
      tubeObj.group.position.set(0, 0.85, 0);
      tractGroup.add(tubeObj.group);

      // Add contraction arrows behind bolus (-x from bolus)
      const bx = (bolusPos - 0.5) * 4.2;
      const squeezeX = Math.max(-1.95, bx - 0.48);

      const topSqueeze = createVectorArrow3D({
        origin: [squeezeX, 1.55, 0],
        direction: [0, -1, 0],
        length: 0.42,
        color: 0xB8432E,
        interactiveId: 'circular_muscle',
      });
      const botSqueeze = createVectorArrow3D({
        origin: [squeezeX, 0.15, 0],
        direction: [0, 1, 0],
        length: 0.42,
        color: 0xB8432E,
        interactiveId: 'circular_muscle',
      });
      const forwardPush = createVectorArrow3D({
        origin: [bx, 0.85, 0],
        direction: [1, 0, 0],
        length: 0.72,
        color: 0x2D6A4F,
        interactiveId: 'enzyme_ph',
      });
      tractGroup.add(topSqueeze, botSqueeze, forwardPush);
      root.add(tractGroup);
    } else {
      // 3D Cutaway Finger-Like Intestinal Villus
      // Outer Epithelial Dome (translucent)
      const villusGeo = new THREE.CapsuleGeometry(0.75, 1.45, 16, 28);
      const villusMesh = new THREE.Mesh(
        villusGeo,
        createPaperMaterial(0xFDE68A, { opacity: 0.35, transparent: true })
      );
      addInkEdges(villusMesh, 0xD97706, 0.65);
      villusMesh.position.set(0, 1.25, 0);
      villusMesh.userData = { interactiveId: 'hepatic_portal', labelPoint: [0.65, 1.7, 0] };
      root.add(villusMesh);

      // Central Yellow/Cream Lacteal (for Fatty Acids & Glycerol)
      const lactealGeo = new THREE.CylinderGeometry(0.18, 0.22, 1.65, 18);
      const lactealMesh = new THREE.Mesh(
        lactealGeo,
        createPaperMaterial(0xF59E0B, { opacity: 0.92, transparent: true })
      );
      addInkEdges(lactealMesh, 0x1E1B18, 0.8);
      lactealMesh.position.set(0, 1.05, 0);
      lactealMesh.userData = { interactiveId: 'lacteal_lymph', labelPoint: [0, 1.45, 0] };
      root.add(lactealMesh);

      // Wrapping Red/Blue Capillary Loop around the Lacteal (for Glucose & Amino Acids)
      const capPts = [];
      for (let i = 0; i <= 40; i++) {
        const u = i / 40;
        const angle = u * Math.PI * 4;
        const y = 0.35 + Math.sin(u * Math.PI) * 1.45;
        capPts.push(new THREE.Vector3(Math.cos(angle) * 0.42, y, Math.sin(angle) * 0.42));
      }
      const capGeo = new THREE.TubeGeometry(new THREE.CatmullRomCurve3(capPts), 64, 0.055, 12, false);
      const capMesh = new THREE.Mesh(capGeo, createPaperMaterial(0xB8432E));
      capMesh.userData = { interactiveId: 'hepatic_portal' };
      root.add(capMesh);

      // Nutrient monomer spheres entering villus
      for (let k = 0; k < 6; k++) {
        const isLipid = k % 2 === 0;
        const mon = createSphereAtom3D({
          radius: 0.08,
          color: isLipid ? 0xD97706 : 0x2B5B84,
          interactiveId: isLipid ? 'lacteal_lymph' : 'hepatic_portal',
        });
        mon.position.set((k - 2.5) * 0.35, 2.25 - (k % 3) * 0.25, 0.35);
        root.add(mon);
      }
    }

    return {
      interactiveObjects: [root],
      update: (dt) => {
        if (isPlaying && stageMode === 'peristalsis') {
          setBolusPos((prev) => {
            const next = prev + dt * 0.16;
            return next > 0.92 ? 0.12 : next;
          });
        }
      },
    };
  }, [bolusPos, invertedGravity, isPlaying, stageMode]);

  // Synchronized Enzyme Activity vs pH chart (Amylase pH 7, Pepsin pH 2, Lipase/Trypsin pH 8)
  const enzymeSeries = useMemo(() => {
    const pepsinPts = [];
    const amylasePts = [];
    const trypsinPts = [];
    for (let ph = 0.5; ph <= 11.5; ph += 0.5) {
      pepsinPts.push({ x: ph, y: 100 * Math.exp(-((ph - 2.0) ** 2) / 1.4) });
      amylasePts.push({ x: ph, y: 100 * Math.exp(-((ph - 7.0) ** 2) / 1.8) });
      trypsinPts.push({ x: ph, y: 100 * Math.exp(-((ph - 8.2) ** 2) / 1.8) });
    }
    return [
      { id: 'pepsin', label: 'Pepsin (Stomach pH 2)', color: '#B8432E', points: pepsinPts },
      { id: 'amylase', label: 'Amylase (Mouth pH 7)', color: '#2B5B84', points: amylasePts },
      { id: 'trypsin', label: 'Trypsin/Lipase (Duodenum pH 8)', color: '#2D6A4F', points: trypsinPts },
    ];
  }, []);

  return (
    <div data-testid="digestive-peristalsis-atlas-aid" className="space-y-4 text-slate-800">
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-rose-100 text-rose-900 uppercase tracking-wider">
              Human Nutrition: Peristalsis, Enzymes & Villus Absorption
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              {stageMode === 'peristalsis'
                ? '3D Cutaway Peristaltic Wave & Regional pH Hydrolysis'
                : '3D Small Intestine Villus: Lacteal vs. Hepatic Portal Capillary Absorption'}
            </h4>
          </div>

          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-digestive-peristalsis"
              onClick={() => {
                setStageMode('peristalsis');
                setSelectedId('circular_muscle');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold ${
                stageMode === 'peristalsis' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              3D Peristalsis Wave
            </button>
            <button
              type="button"
              data-testid="btn-digestive-villus"
              onClick={() => {
                setStageMode('villus');
                setSelectedId('hepatic_portal');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold ${
                stageMode === 'villus' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              3D Villus Absorption
            </button>
          </div>
        </div>

        {stageMode === 'peristalsis' && (
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5 items-center">
            <label className="sm:col-span-2 bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
              <div className="flex justify-between text-xs font-semibold text-slate-700">
                <span>Bolus Position Along Alimentary Canal ({regionInfo.region})</span>
                <span className="font-mono font-bold text-[#2B5B84]">
                  {Math.round(bolusPos * 100)}% (pH {regionInfo.pH.toFixed(1)})
                </span>
              </div>
              <input
                type="range"
                data-testid="slider-bolus-peristalsis"
                min="0.1"
                max="0.9"
                step="0.02"
                value={bolusPos}
                onChange={(e) => {
                  setIsPlaying(false);
                  setBolusPos(parseFloat(e.target.value));
                }}
                className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
              />
            </label>

            <div className="flex items-center gap-1.5 justify-end">
              <button
                type="button"
                data-testid="btn-invert-gravity"
                onClick={() => setInvertedGravity((v) => !v)}
                className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold border transition-all ${
                  invertedGravity
                    ? 'bg-amber-50 border-amber-300 text-amber-900'
                    : 'bg-slate-100 border-slate-200 text-slate-700'
                }`}
              >
                {invertedGravity ? 'Anti-Gravity Tilt: ON' : 'Upright Swallow'}
              </button>
              <button
                type="button"
                onClick={() => setIsPlaying((p) => !p)}
                className="px-2.5 py-1.5 rounded-lg bg-[#2B5B84] text-white text-xs font-semibold flex items-center gap-1"
              >
                {isPlaying ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
                {isPlaying ? 'Pause' : 'Wave'}
              </button>
            </div>
          </div>
        )}
      </div>

      <AtlasCanvas3D
        testId="digestive-peristalsis-3d-canvas"
        height={300}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle={
          stageMode === 'peristalsis'
            ? 'Observe circular muscle constriction BEHIND the bolus & longitudinal relaxation AHEAD • Click badges for enzyme pH mechanics'
            : 'Click the central yellow Lacteal (Lipids) or red Capillary loop (Glucose & Amino Acids → Hepatic Portal Vein)'
        }
      />

      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />

      <AtlasSyncChartSvg
        title="Digestive Enzyme Relative Activity vs. Regional Alimentary Canal pH"
        xLabel="Alimentary Canal pH"
        yLabel="Enzyme Activity (%)"
        xDomain={[0, 12]}
        yDomain={[0, 110]}
        series={enzymeSeries}
        activePoint={{
          x: regionInfo.pH,
          y: 100,
          label: `${regionInfo.region} (pH ${regionInfo.pH.toFixed(1)})`,
          color: regionInfo.color,
        }}
      />
    </div>
  );
}
