import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { ExternalLink, Dna, Sparkles, BookOpen } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import { createSphereAtom3D, createBondCylinder3D, createHelixCoil3D } from '../shared/atlas3d/atlasPartsKit';

const MOLECULES = [
  {
    id: 'dna',
    name: 'B-DNA Double Helix',
    subTitle: 'Watson-Crick Antiparallel B-Form',
    pdbId: '1BNA',
    category: 'Nucleic Acid',
    length: '12 Base Pairs',
    keyFeatures: [
      'Right-handed antiparallel double helix (5′→3′ paired with 3′→5′)',
      'Complementary base pairing: A=T (2 H-bonds), G≡C (3 H-bonds)',
      'Deoxyribose sugar-phosphate backbone on exterior',
      'Major and minor grooves for regulatory protein recognition',
    ],
    curriculumRelevance: 'Life Sciences Gr 12: Code of Life, DNA replication, and Transcription.',
    calc: {
      id: 'dna_calc',
      symbol: '\\%A = \\%T,\\; \\%G = \\%C',
      label: "Chargaff's Base-Pairing Ratio & Hydrogen Bond Count",
      color: '#2B5B84',
      badgeText: 'A=T (2 H-bonds) | G≡C (3 H-bonds)',
      formula: '\\%A + \\%T + \\%G + \\%C = 100\\% \\quad (\\text{where } A=T \\text{ and } G=C)',
      substitution: '\\text{If Cytosine } (C) = 28\\% \\implies G = 28\\% \\implies A + T = 44\\% \\implies A = 22\\%',
      result: 'N_{\\text{H-bonds}} = 2(N_{AT}) + 3(N_{GC})',
      meaning: 'Purines (Adenine, Guanine) always pair with complementary Pyrimidines (Thymine, Cytosine) to keep the double-helix diameter uniform at 2.0 nm.',
    },
  },
  {
    id: 'trna',
    name: 'Transfer RNA (tRNA-Phe)',
    subTitle: 'L-Shaped Tertiary Conformation',
    pdbId: '1TRM',
    category: 'Nucleic Acid',
    length: '76 Nucleotides',
    keyFeatures: [
      'Cloverleaf secondary structure folding into an L-shaped 3D tertiary structure',
      'Anticodon triplet loop complementary to mRNA codon during translation',
      'Amino acid attachment stem ending in 3′-CCA sequence',
      'D-loop and TΨC-loop providing structural stabilization',
    ],
    curriculumRelevance: 'Life Sciences Gr 12: Translation & Protein Synthesis at the Ribosome.',
    calc: {
      id: 'trna_calc',
      symbol: '\\text{Codon} \\leftrightarrow \\text{Anticodon}',
      label: 'Triplet Base Code: DNA Template → mRNA Codon → tRNA Anticodon',
      color: '#7C3AED',
      badgeText: '1 Amino Acid = 3 Bases',
      formula: 'N_{\\text{nucleotides}} = 3 \\times N_{\\text{amino acids}} \\quad (\\text{e.g., } 75\\text{ amino acids} = 225\\text{ bases})',
      substitution: '\\text{DNA } 3^\\prime\\text{-TAC-5}^\\prime \\xrightarrow{\\text{Transcription}} \\text{mRNA } 5^\\prime\\text{-AUG-3}^\\prime \\xrightarrow{\\text{tRNA}} 3^\\prime\\text{-UAC-5}^\\prime',
      result: '\\text{Delivers specific amino acid to ribosome A-site}',
      meaning: 'Each tRNA folds into a 3D L-shape with an exposed triplet anticodon at one end and a specific amino acid covalently attached to its 3′-CCA stem.',
    },
  },
  {
    id: 'hemoglobin',
    name: 'Deoxyhemoglobin Tetramer',
    subTitle: 'Quaternary Oxygen Transport Complex',
    pdbId: '1HHO',
    category: 'Globular Protein',
    length: '4 Subunits (2α, 2β)',
    keyFeatures: [
      'Quaternary structure composed of two α-globin and two β-globin chains',
      'Four prosthetic heme groups each containing a central Fe²⁺ iron ion',
      'Cooperative binding of up to 4 O₂ molecules (allosteric transition)',
      'Tense (T) state in tissues vs. Relaxed (R) state in alveolar capillaries',
    ],
    curriculumRelevance: 'Natural Sciences Gr 9 & Life Sciences Gr 10: Circulatory Transport & Gas Exchange.',
    calc: {
      id: 'hb_calc',
      symbol: '\\text{Hb} + 4\\text{O}_2 \\rightleftharpoons \\text{Hb(O}_2)_4',
      label: 'Quaternary Heme-Iron Cooperative Oxygen Binding & Bohr Shift',
      color: '#B8432E',
      badgeText: '4 Fe²⁺ Heme Prosthetic Groups',
      formula: '\\text{Hb} + 4\\,\\text{O}_2 \\rightleftharpoons \\text{Oxyhaemoglobin } (\\text{High } p\\text{O}_2 \\text{ in Alveoli})',
      substitution: '\\uparrow p\\text{CO}_2 \\text{ in respiring muscle lowers blood pH} \\implies \\text{O}_2 \\text{ dissociates to tissues}',
      result: '1\\text{ Hb tetramer carries up to } 4\\,\\text{O}_2\\text{ molecules}',
      meaning: 'Iron (Fe²⁺) is an essential mineral in the diet because each of the four polypeptide subunits of haemoglobin requires a central Fe²⁺ heme group to bind oxygen reversibly.',
    },
  },
  {
    id: 'lysozyme',
    name: 'Lysozyme Hydrolase',
    subTitle: 'Enzyme Active Site & Induced Fit',
    pdbId: '1LYZ',
    category: 'Enzyme / Catalyst',
    length: '129 Amino Acids',
    keyFeatures: [
      'Single polypeptide chain with 4 disulfide bonds for structural rigidity',
      'Prominent substrate binding cleft between two structural domains',
      'Catalytic residues Glu35 and Asp52 break bacterial cell wall peptidoglycans',
      'Demonstrates the induced fit model of enzyme catalysis',
    ],
    curriculumRelevance: 'Life Sciences Gr 10: Enzymes, activation energy, and denaturation.',
    calc: {
      id: 'lysozyme_calc',
      symbol: 'E + S \\rightleftharpoons ES \\to E + P',
      label: 'Enzyme Lock-and-Key / Induced-Fit Catalysis & Denaturation',
      color: '#2D6A4F',
      badgeText: 'Lowers Activation Energy E_a',
      formula: 'E + S \\rightleftharpoons \\text{Enzyme-Substrate Complex } (ES) \\longrightarrow E + P',
      substitution: 'T > T_{\\text{optimum}} \\text{ or extreme pH breaks H-bonds/ionic bonds} \\implies \\text{Active Site Denatures}',
      result: '\\Delta G_{\\text{activation}} \\text{ lowered without consuming enzyme } E',
      meaning: 'Biological catalysts are 3D globular proteins whose active-site cleft is complementary in shape and charge to a specific substrate.',
    },
  },
];

export default function BiomolecularStructureAid() {
  const [selectedMolId, setSelectedMolId] = useState('dna');
  const mol = MOLECULES.find((m) => m.id === selectedMolId) || MOLECULES[0];

  const calculationsMap = useMemo(() => {
    return { [mol.calc.id]: mol.calc };
  }, [mol]);

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    if (mol.id === 'dna') {
      // 3D Antiparallel Double Helix with base-pair rungs
      const turns = 2.2;
      const height = 2.2;
      const radius = 0.65;
      const steps = 12;

      for (let i = 0; i <= steps; i++) {
        const u = i / steps;
        const angle = u * Math.PI * 2 * turns;
        const y = 0.15 + u * height;
        const p1 = [Math.cos(angle) * radius, y, Math.sin(angle) * radius];
        const p2 = [Math.cos(angle + Math.PI) * radius, y, Math.sin(angle + Math.PI) * radius];

        const s1 = createSphereAtom3D({ radius: 0.11, color: 0x2B5B84, interactiveId: mol.calc.id });
        s1.position.set(...p1);
        const s2 = createSphereAtom3D({ radius: 0.11, color: 0xB8432E, interactiveId: mol.calc.id });
        s2.position.set(...p2);
        root.add(s1, s2);

        const rung = createBondCylinder3D({
          start: p1,
          end: p2,
          radius: 0.04,
          color: i % 2 === 0 ? 0xD97706 : 0x2D6A4F,
          order: 1,
          interactiveId: mol.calc.id,
        });
        root.add(rung);
      }
    } else if (mol.id === 'trna') {
      // L-shaped 3D tertiary fold with Anticodon loop at bottom and 3'-CCA amino acid stem at right
      const stemVert = createHelixCoil3D({ radius: 0.32, height: 1.4, turns: 3, tubeRadius: 0.06, color: 0x7C3AED, interactiveId: mol.calc.id });
      stemVert.position.set(-0.35, 0.25, 0);
      const stemHoriz = createHelixCoil3D({ radius: 0.28, height: 1.25, turns: 3, tubeRadius: 0.06, color: 0x2B5B84, interactiveId: mol.calc.id });
      stemHoriz.rotation.z = -Math.PI / 2;
      stemHoriz.position.set(-0.35, 1.55, 0);
      const anticodon = createSphereAtom3D({ radius: 0.2, color: 0xD97706, interactiveId: mol.calc.id });
      anticodon.position.set(-0.35, 0.2, 0);
      const aminoAcid = createSphereAtom3D({ radius: 0.22, color: 0x2D6A4F, interactiveId: mol.calc.id });
      aminoAcid.position.set(1.05, 1.55, 0);
      root.add(stemVert, stemHoriz, anticodon, aminoAcid);
    } else if (mol.id === 'hemoglobin') {
      // 4 Quaternary Subunits (2 alpha, 2 beta) with golden Fe2+ heme cores
      const offsets = [
        { pos: [-0.55, 1.35, 0.3], color: 0xB8432E },
        { pos: [0.55, 1.35, -0.3], color: 0xE11D48 },
        { pos: [-0.55, 0.55, -0.3], color: 0xE11D48 },
        { pos: [0.55, 0.55, 0.3], color: 0xB8432E },
      ];
      offsets.forEach((sub) => {
        const globin = createSphereAtom3D({ radius: 0.46, color: sub.color, opacity: 0.72, interactiveId: mol.calc.id });
        globin.position.set(...sub.pos);
        const hemeFe = createSphereAtom3D({ radius: 0.14, color: 0xF59E0B, interactiveId: mol.calc.id });
        hemeFe.position.set(sub.pos[0], sub.pos[1], sub.pos[2] + 0.32);
        root.add(globin, hemeFe);
      });
    } else {
      // Lysozyme globular enzyme domains with substrate bound in the active-site cleft
      const domTop = createSphereAtom3D({ radius: 0.65, color: 0x2B5B84, interactiveId: mol.calc.id });
      domTop.position.set(-0.2, 1.45, 0);
      const domBot = createSphereAtom3D({ radius: 0.72, color: 0x2B5B84, interactiveId: mol.calc.id });
      domBot.position.set(-0.2, 0.6, 0);
      const substrate = createSphereAtom3D({ radius: 0.28, color: 0xD97706, interactiveId: mol.calc.id });
      substrate.position.set(0.45, 1.05, 0);
      root.add(domTop, domBot, substrate);
    }

    return { interactiveObjects: [root] };
  }, [mol]);

  return (
    <div data-testid="biomolecular-structure-aid" className="space-y-4 text-slate-800">
      {/* Molecule Selection Pills */}
      <div className="flex flex-wrap gap-1.5 p-2 bg-slate-50 rounded-xl border border-slate-200">
        {MOLECULES.map((item) => (
          <button
            key={item.id}
            data-testid={`btn-select-mol-${item.id}`}
            onClick={() => setSelectedMolId(item.id)}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
              selectedMolId === item.id
                ? 'bg-[#13519C] text-white shadow-sm'
                : 'bg-white text-slate-700 hover:bg-slate-100 border border-slate-200'
            }`}
          >
            {item.name}
          </button>
        ))}
      </div>

      {/* Molecule Hero Card & 3D Paper & Ink Representation */}
      <div className="bg-white p-3.5 rounded-xl border border-slate-200 shadow-sm space-y-3">
        <div className="flex items-start justify-between">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-indigo-100 text-indigo-800 uppercase tracking-wider">
              {mol.category} · PDB: {mol.pdbId}
            </span>
            <h4 className="text-base font-bold text-slate-900 mt-1">{mol.name}</h4>
            <p className="text-xs text-slate-500">{mol.subTitle}</p>
          </div>

          <div className="text-right">
            <span className="text-[10px] text-slate-400 font-bold uppercase tracking-wider">Scale / Size</span>
            <div className="text-xs font-mono font-bold text-[#13519C]">{mol.length}</div>
          </div>
        </div>

        {/* True Three.js 3D Conformation Viewport */}
        <AtlasCanvas3D
          testId="biomolecular-3d-canvas"
          height={260}
          buildScene={buildScene}
          selectedId={mol.calc.id}
          onSelect={() => {}}
          badgeItems={[mol.calc]}
          subtitle="Drag to orbit 3D macromolecule • Click badge to inspect Chargaff ratios, triplet codons, or enzyme catalysis"
        />

        {/* Interactive Launch Button (Mol* Sidecar Pill) */}
        <div className="w-full flex items-center justify-between px-3 py-2 rounded-lg bg-slate-900 text-white">
          <span className="text-[11px] font-mono text-slate-300 flex items-center gap-1.5">
            <Dna className="w-3.5 h-3.5 text-indigo-400" />
            RCSB PDB Accession: {mol.pdbId}
          </span>
          <a
            href="sidecar://biomolecular-structure-viewer"
            data-testid="btn-launch-molstar-sidecar"
            className="inline-flex items-center gap-1.5 px-3 py-1 rounded-md text-xs font-semibold bg-indigo-600 text-white hover:bg-indigo-500 shadow-sm transition-colors"
            title="Launch Mol* 3D Viewer Sidecar Panel"
          >
            <ExternalLink className="w-3.5 h-3.5" />
            Open Mol* 3D Sidecar
          </a>
        </div>

        {/* Interactive Calculation Popover */}
        <CalculationPopoverCard
          calculation={mol.calc}
          allCalculations={ Object.values(calculationsMap) }
          onSelectCalculation={() => {}}
        />

        {/* Structural Hallmarks */}
        <div className="space-y-1.5">
          <span className="text-xs font-bold text-slate-800 flex items-center gap-1">
            <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
            Key Structural Features
          </span>
          <ul className="space-y-1">
            {mol.keyFeatures.map((feat, idx) => (
              <li key={idx} className="text-xs text-slate-600 flex items-start gap-1.5">
                <span className="w-1.5 h-1.5 rounded-full bg-indigo-500 mt-1.5 shrink-0" />
                <span>{feat}</span>
              </li>
            ))}
          </ul>
        </div>

        {/* National Curriculum Standards Context */}
        <div className="p-2.5 rounded-lg bg-emerald-50 border border-emerald-200 text-xs text-emerald-900">
          <span className="font-bold flex items-center gap-1">
            <BookOpen className="w-3.5 h-3.5 text-emerald-700" />
            National Curriculum Standards Syllabus Link:
          </span>
          <p className="mt-0.5 text-emerald-800">{mol.curriculumRelevance}</p>
        </div>
      </div>
    </div>
  );
}
