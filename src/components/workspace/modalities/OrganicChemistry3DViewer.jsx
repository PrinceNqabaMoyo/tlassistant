import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Atom, Sparkles, Thermometer, CheckCircle2 } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import { createSphereAtom3D, createBondCylinder3D, createVectorArrow3D } from '../shared/atlas3d/atlasPartsKit';

const MOLECULES = {
  butane: {
    name: 'Butane (Unbranched Chain)',
    formula: 'C4H10',
    type: 'Chain Isomer',
    boilingPoint: '-0.5°C',
    boilingPointNum: -0.5,
    molarMass: 58.12,
    imf: 'London Dispersion (Higher surface area -> Stronger intermolecular forces)',
    description: 'Straight 4-carbon alkane chain. Greater contact area than branched isomer.',
    atoms: [
      { id: 'c1', type: 'C', pos: [-1.35, -0.2, 0] },
      { id: 'c2', type: 'C', pos: [-0.45, 0.35, 0.25] },
      { id: 'c3', type: 'C', pos: [0.45, -0.25, -0.25] },
      { id: 'c4', type: 'C', pos: [1.35, 0.3, 0.1] },
      { id: 'h1', type: 'H', pos: [-1.85, -0.55, -0.35] },
      { id: 'h2', type: 'H', pos: [-1.75, 0.45, -0.3] },
      { id: 'h3', type: 'H', pos: [-1.45, -0.5, 0.65] },
      { id: 'h4', type: 'H', pos: [1.85, 0.65, 0] },
      { id: 'h5', type: 'H', pos: [1.75, -0.3, 0.55] },
      { id: 'h6', type: 'H', pos: [1.45, 0.55, -0.6] },
    ],
    bonds: [
      ['c1', 'c2', 1], ['c2', 'c3', 1], ['c3', 'c4', 1],
      ['c1', 'h1', 1], ['c1', 'h2', 1], ['c1', 'h3', 1],
      ['c4', 'h4', 1], ['c4', 'h5', 1], ['c4', 'h6', 1],
    ],
  },
  methylpropane: {
    name: '2-Methylpropane (Isobutane)',
    formula: 'C4H10',
    type: 'Chain Isomer',
    boilingPoint: '-11.7°C',
    boilingPointNum: -11.7,
    molarMass: 58.12,
    imf: 'London Dispersion (Spherical shape -> Less surface area -> Weaker forces)',
    description: 'Branched alkane. Compact spherical geometry reduces intermolecular contact.',
    atoms: [
      { id: 'c1', type: 'C', pos: [0, 0, 0] },
      { id: 'c2', type: 'C', pos: [-1.05, -0.65, -0.25] },
      { id: 'c3', type: 'C', pos: [1.05, -0.65, -0.25] },
      { id: 'c4', type: 'C', pos: [0, 1.05, 0.35] },
      { id: 'h1', type: 'H', pos: [0, -0.3, 0.8] },
      { id: 'h2', type: 'H', pos: [-1.55, -1.0, 0] },
      { id: 'h3', type: 'H', pos: [1.55, -1.0, 0] },
      { id: 'h4', type: 'H', pos: [0, 1.65, 0] },
    ],
    bonds: [
      ['c1', 'c2', 1], ['c1', 'c3', 1], ['c1', 'c4', 1], ['c1', 'h1', 1],
      ['c2', 'h2', 1], ['c3', 'h3', 1], ['c4', 'h4', 1],
    ],
  },
  propan1ol: {
    name: 'Propan-1-ol (Primary Alcohol)',
    formula: 'C3H8O',
    type: 'Positional Isomer',
    boilingPoint: '97.2°C',
    boilingPointNum: 97.2,
    molarMass: 60.10,
    imf: 'Hydrogen Bonding (Terminal -OH group creates accessible polar site)',
    description: 'Hydroxyl group on carbon 1. Strong hydrogen bonding between molecules.',
    atoms: [
      { id: 'c1', type: 'C', pos: [-1.1, 0, 0] },
      { id: 'c2', type: 'C', pos: [0, 0.45, 0.2] },
      { id: 'c3', type: 'C', pos: [1.05, -0.2, -0.2] },
      { id: 'o1', type: 'O', pos: [1.85, 0.35, 0.1] },
      { id: 'h1', type: 'H', pos: [2.4, 0.6, 0.2] },
      { id: 'h2', type: 'H', pos: [-1.55, -0.45, -0.2] },
      { id: 'h3', type: 'H', pos: [-1.35, 0.45, 0.35] },
    ],
    bonds: [
      ['c1', 'c2', 1], ['c2', 'c3', 1], ['c3', 'o1', 1], ['o1', 'h1', 1],
      ['c1', 'h2', 1], ['c1', 'h3', 1],
    ],
  },
  propan2ol: {
    name: 'Propan-2-ol (Secondary Alcohol)',
    formula: 'C3H8O',
    type: 'Positional Isomer',
    boilingPoint: '82.6°C',
    boilingPointNum: 82.6,
    molarMass: 60.10,
    imf: 'Hydrogen Bonding (Internal -OH group sterically crowded -> Slightly lower BP)',
    description: 'Hydroxyl group on carbon 2. Steric hindrance lowers hydrogen bond strength.',
    atoms: [
      { id: 'c1', type: 'C', pos: [-1.05, -0.45, 0] },
      { id: 'c2', type: 'C', pos: [0, 0.2, 0] },
      { id: 'c3', type: 'C', pos: [1.05, -0.45, 0] },
      { id: 'o1', type: 'O', pos: [0, 1.15, 0.3] },
      { id: 'h1', type: 'H', pos: [-0.35, 1.65, 0.45] },
    ],
    bonds: [
      ['c1', 'c2', 1], ['c2', 'c3', 1], ['c2', 'o1', 1], ['o1', 'h1', 1],
    ],
  },
};

const ATOM_CONFIG = {
  C: { color: 0x334155, radius: 0.25 },
  H: { color: 0xF8FAFC, radius: 0.14 },
  O: { color: 0xE11D48, radius: 0.22 },
  N: { color: 0x2563EB, radius: 0.22 },
};

export default function OrganicChemistry3DViewer() {
  const [activeKey, setActiveKey] = useState('butane');
  const [selectedCalcId, setSelectedCalcId] = useState('imf_boiling');

  const activeMolecule = MOLECULES[activeKey] || MOLECULES.butane;

  const calculationsMap = useMemo(() => {
    const isAlcohol = activeMolecule.formula === 'C3H8O';
    return {
      imf_boiling: {
        id: 'imf_boiling',
        symbol: 'T_b,\\text{ IMF}',
        label: `${activeMolecule.name} — Intermolecular Forces & Boiling Point`,
        color: isAlcohol ? '#E11D48' : '#2B5B84',
        badgeText: `BP: ${activeMolecule.boilingPoint}`,
        formula: isAlcohol
          ? '\\text{Hydrogen Bonding } (\\text{O}^{\\delta-}-\\text{H}^{\\delta+}) \\gg \\text{London Dispersion}'
          : '\\text{Unbranched Surface Area} > \\text{Branched Spherical Area} \\implies E_{\\text{London}} \\uparrow',
        substitution: `M(${activeMolecule.formula}) = ${activeMolecule.molarMass.toFixed(2)}\\text{ g\\cdot mol}^{-1} \\implies T_b = ${activeMolecule.boilingPoint}`,
        result: `T_b = ${activeMolecule.boilingPoint} \\text{ (${activeMolecule.type})}`,
        meaning: activeMolecule.imf,
      },
      tetrahedral_geom: {
        id: 'tetrahedral_geom',
        symbol: 'sp^3 (109.5^\\circ)',
        label: 'Tetrahedral Carbon Bond Angle & Hybridisation',
        color: '#2D6A4F',
        badgeText: '109.5° sp³',
        formula: '\\theta_{\\text{tetrahedral}} = \\arccos\\!\\left(-\\tfrac{1}{3}\\right) \\approx 109.5^\\circ',
        substitution: `\\text{Saturated } C_n H_{2n+2} \\text{ carbons form 4 } \\sigma\\text{-bonds in 3D tetrahedral geometry}`,
        result: `\\text{Molecular Formula: } ${activeMolecule.formula}`,
        meaning: activeMolecule.description,
      },
    };
  }, [activeMolecule]);

  const activeCalculation = calculationsMap[selectedCalcId] || calculationsMap.imf_boiling;

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    const atomPosMap = {};
    activeMolecule.atoms.forEach((a) => {
      atomPosMap[a.id] = a.pos;
      const cfg = ATOM_CONFIG[a.type] || ATOM_CONFIG.C;
      const sphere = createSphereAtom3D({
        radius: cfg.radius,
        color: cfg.color,
        interactiveId: a.type === 'O' ? 'imf_boiling' : 'tetrahedral_geom',
      });
      sphere.position.set(a.pos[0], a.pos[1] + 0.65, a.pos[2]);
      root.add(sphere);
    });

    activeMolecule.bonds.forEach(([id1, id2, order]) => {
      const p1 = atomPosMap[id1];
      const p2 = atomPosMap[id2];
      if (!p1 || !p2) return;
      const bond = createBondCylinder3D({
        start: [p1[0], p1[1] + 0.65, p1[2]],
        end: [p2[0], p2[1] + 0.65, p2[2]],
        order: order || 1,
        interactiveId: 'tetrahedral_geom',
      });
      root.add(bond);
    });

    // If alcohol, show polar O-H dipole arrow
    if (activeMolecule.atoms.some((a) => a.type === 'O')) {
      const oAtom = activeMolecule.atoms.find((a) => a.type === 'O');
      if (oAtom) {
        const dipole = createVectorArrow3D({
          origin: [oAtom.pos[0], oAtom.pos[1] + 0.95, oAtom.pos[2]],
          direction: [0, 1, 0],
          length: 0.6,
          color: 0xE11D48,
          interactiveId: 'imf_boiling',
        });
        root.add(dipole);
      }
    }

    return { interactiveObjects: [root] };
  }, [activeMolecule]);

  return (
    <div data-testid="organic-chem-canvas" className="w-full bg-white text-slate-800 rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col select-none space-y-3 p-3.5">
      {/* Top Header */}
      <div className="flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-teal-50 text-teal-700 border border-teal-200 flex items-center justify-center">
            <Atom className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold tracking-tight text-slate-900 flex items-center gap-1.5">
              3D Ball-and-Stick Molecular Isomer Explorer
              <span className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-teal-100 text-teal-800">
                Paper & Ink 3D
              </span>
            </h3>
            <p className="text-[11px] text-slate-500">
              {activeMolecule.name} ({activeMolecule.formula}) • BP: {activeMolecule.boilingPoint}
            </p>
          </div>
        </div>

        {/* Molecule selection pills */}
        <div className="flex items-center gap-1 overflow-x-auto scrollbar-none py-1">
          {Object.entries(MOLECULES).map(([key, item]) => (
            <button
              key={key}
              data-testid={`btn-mol-${key}`}
              onClick={() => setActiveKey(key)}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition-all ${
                activeKey === key
                  ? 'bg-[#2B5B84] text-white shadow-xs'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
              }`}
            >
              {item.name.split(' ')[0]}
            </button>
          ))}
        </div>
      </div>

      {/* True Three.js 3D Paper & Ink Viewport */}
      <AtlasCanvas3D
        testId="organic-chem-3d-stage"
        height={280}
        buildScene={buildScene}
        selectedId={selectedCalcId}
        onSelect={(id) => {
          if (id) setSelectedCalcId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle="Drag to orbit in 3D • Click any carbon, hydroxyl group, or badge to inspect IMF & boiling point mechanics"
      />

      {/* Interactive Calculation Popover */}
      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedCalcId}
      />

      {/* Intermolecular Forces Summary Footer */}
      <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 flex flex-col gap-1.5 text-xs">
        <div className="flex items-center justify-between">
          <span className="font-semibold text-slate-700 flex items-center gap-1">
            <Sparkles className="w-3.5 h-3.5 text-amber-600" />
            Intermolecular Forces ({activeMolecule.type}):
          </span>
          <span className="font-mono text-teal-800 font-bold flex items-center gap-1">
            <Thermometer className="w-3.5 h-3.5 text-rose-600" />
            {activeMolecule.formula} • BP {activeMolecule.boilingPoint}
          </span>
        </div>
        <p className="text-[11px] text-slate-600 leading-relaxed">{activeMolecule.imf}</p>
        <div className="flex items-center justify-between text-[11px] text-slate-500 pt-1 border-t border-slate-200/70">
          <span>CPK Colors: Slate = C, White = H, Crimson = O</span>
          <span className="text-emerald-700 font-semibold flex items-center gap-1">
            <CheckCircle2 className="w-3 h-3 text-emerald-600" /> Tetrahedral Bond Geometry (109.5°)
          </span>
        </div>
      </div>
    </div>
  );
}
