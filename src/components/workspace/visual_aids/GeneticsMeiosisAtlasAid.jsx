import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Dna, AlertTriangle } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import { createBlock3D, createSphereAtom3D } from '../shared/atlas3d/atlasPartsKit';

/**
 * GeneticsMeiosisAtlasAid
 * -----------------------
 * Grade 12 Life Sciences (Meiosis & Genetics):
 * 3D Homologous Bivalent Crossing-Over at Chiasmata (Prophase I),
 * Random Arrangement at the Equator (Metaphase I: 2^n combinations),
 * and Anaphase I / II Disjunction vs. Non-Disjunction (Trisomy 21 / Down Syndrome).
 */

const STAGES = [
  { id: 'prophase1', label: 'Prophase I (Chiasmata)' },
  { id: 'metaphase1', label: 'Metaphase I (Random Assortment)' },
  { id: 'anaphase1', label: 'Anaphase I (Disjunction)' },
];

export default function GeneticsMeiosisAtlasAid() {
  const [stage, setStage] = useState('prophase1');
  const [nonDisjunction, setNonDisjunction] = useState(false);
  const [selectedId, setSelectedId] = useState('crossing_over');

  const calculationsMap = useMemo(() => {
    return {
      crossing_over: {
        id: 'crossing_over',
        symbol: '\\text{Prophase I Chiasma}',
        label: 'Synapsis & Crossing-Over at Chiasmata (Genetic Variation #1)',
        color: '#2B5B84',
        badgeText: 'Recombinant Chromatids',
        formula: '\\text{Non-Sister Chromatids of Homologous Pair Exchange Allele Segments at Chiasma}',
        substitution: '\\text{Paternal (Blue) + Maternal (Red) Bivalent} \\longrightarrow 4\\text{ genetically distinct chromatids}',
        result: '\\text{Introduces new allele combinations on the same chromosome}',
        meaning: 'During Prophase I, homologous chromosomes pair up (synapsis) to form a bivalent. Non-sister chromatids overlap at chiasmata and swap corresponding DNA segments.',
      },
      random_assortment: {
        id: 'random_assortment',
        symbol: '2^n = 2^{23}',
        label: 'Metaphase I Independent Assortment (Genetic Variation #2)',
        color: '#2D6A4F',
        badgeText: '2²³ = 8,388,608 Combos',
        formula: '\\text{Possible Gamete Combinations} = 2^n \\quad (n = 23 \\text{ haploid chromosome pairs in humans})',
        substitution: '2^{23} = 8\\,388\\,608 \\text{ combinations (before crossing-over!)}',
        result: '2n = 46 \\xrightarrow{\\text{Meiosis I}} n = 23 \\text{ per daughter cell}',
        meaning: 'Homologous pairs line up randomly in two rows along the equator during Metaphase I, so maternal and paternal chromosomes assort independently into gametes.',
      },
      non_disjunction_calc: {
        id: 'non_disjunction_calc',
        symbol: nonDisjunction ? '2n + 1 = 47' : 'n = 23',
        label: nonDisjunction
          ? 'Anaphase Non-Disjunction → Aneuploidy (Trisomy 21 / Down Syndrome)'
          : 'Normal Anaphase I Disjunction (Reduction Division 2n → n)',
        color: nonDisjunction ? '#B8432E' : '#D97706',
        badgeText: nonDisjunction ? 'Trisomy 21 (47 Chromosomes)' : 'Normal Disjunction (n=23)',
        formula: nonDisjunction
          ? '\\text{Gamete } (n + 1 = 24) + \\text{Normal Gamete } (n = 23) \\longrightarrow \\text{Zygote } (2n + 1 = 47)'
          : '\\text{Spindle fibres pull whole homologous chromosomes to opposite poles } (2n = 46 \\to n = 23)',
        substitution: nonDisjunction
          ? '\\text{Failure of Chromosome pair 21 to separate} \\implies 3\\text{ copies of Chromosome 21}'
          : '\\text{Centromeres do NOT split in Anaphase I; whole homologues separate}',
        result: nonDisjunction ? '\\text{Down Syndrome (47 chromosomes)}' : '\\text{Haploid cells } (n = 23)',
        meaning: nonDisjunction
          ? 'Non-disjunction is the failure of homologous chromosomes (Anaphase I) or sister chromatids (Anaphase II) to separate, producing abnormal gametes with n+1 (24) or n−1 (22) chromosomes.'
          : 'Anaphase I is the reduction division: whole bivalent partners separate to opposite poles, halving the chromosome number from diploid (2n) to haploid (n).',
      },
    };
  }, [nonDisjunction]);

  const activeCalculation = calculationsMap[selectedId] || calculationsMap.crossing_over;

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    const makeChromatidPair = (colorHex, swappedTipColor, interactiveId) => {
      const grp = new THREE.Group();
      grp.userData = { interactiveId, labelPoint: [0, 0.75, 0] };

      const leftArm = createBlock3D({ width: 0.16, height: 1.35, depth: 0.16, color: colorHex, interactiveId });
      leftArm.rotation.z = 0.22;
      const rightArm = createBlock3D({ width: 0.16, height: 1.35, depth: 0.16, color: colorHex, interactiveId });
      rightArm.rotation.z = -0.22;
      grp.add(leftArm, rightArm);

      // Swapped recombinant tip segment at bottom of inner chromatid
      if (swappedTipColor) {
        const tip = createBlock3D({ width: 0.18, height: 0.36, depth: 0.18, color: swappedTipColor, interactiveId: 'crossing_over' });
        tip.position.set(0.15, -0.52, 0.02);
        grp.add(tip);
      }

      const centromere = createSphereAtom3D({ radius: 0.14, color: 0xD97706, interactiveId });
      grp.add(centromere);
      return grp;
    };

    const sep = stage === 'prophase1' ? 0.28 : stage === 'metaphase1' ? 0.55 : 1.45;
    const patChr = makeChromatidPair(0x2B5B84, 0xB8432E, 'crossing_over');
    const matChr = makeChromatidPair(0xB8432E, 0x2B5B84, 'non_disjunction_calc');

    if (stage === 'anaphase1' && nonDisjunction) {
      // Both homologues pulled to the RIGHT pole (+x) together!
      patChr.position.set(1.15, 0.95, 0);
      matChr.position.set(1.55, 0.95, 0);
    } else {
      patChr.position.set(-sep, 0.95, 0);
      matChr.position.set(sep, 0.95, 0);
    }

    root.add(patChr, matChr);

    // Spindle equator line
    const eqLine = new THREE.Line(
      new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(0, 0.05, -1.3),
        new THREE.Vector3(0, 0.05, 1.3),
      ]),
      new THREE.LineBasicMaterial({ color: 0x64748B })
    );
    root.add(eqLine);

    return { interactiveObjects: [root] };
  }, [nonDisjunction, stage]);

  return (
    <div data-testid="genetics-meiosis-atlas-aid" className="space-y-4 text-slate-800">
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-purple-100 text-purple-900 uppercase tracking-wider">
              Grade 12 Life Sciences • Meiosis & Genetic Variation
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              3D Homologous Bivalent Crossing-Over & Anaphase Non-Disjunction Explorer
            </h4>
          </div>

          <button
            type="button"
            data-testid="btn-toggle-nondisjunction"
            onClick={() => {
              setStage('anaphase1');
              setNonDisjunction((v) => !v);
              setSelectedId('non_disjunction_calc');
            }}
            className={`px-2.5 py-1 rounded-lg text-xs font-semibold border flex items-center gap-1 ${
              nonDisjunction
                ? 'bg-rose-600 border-rose-600 text-white'
                : 'bg-slate-100 border-slate-200 text-slate-700'
            }`}
          >
            <AlertTriangle className="w-3.5 h-3.5" />
            {nonDisjunction ? 'Non-Disjunction Active (Trisomy 21)' : 'Simulate Non-Disjunction'}
          </button>
        </div>

        <div className="flex flex-wrap gap-1.5">
          {STAGES.map((s) => (
            <button
              key={s.id}
              type="button"
              data-testid={`btn-meiosis-${s.id}`}
              onClick={() => {
                setStage(s.id);
                if (s.id === 'prophase1') setSelectedId('crossing_over');
                if (s.id === 'metaphase1') setSelectedId('random_assortment');
                if (s.id === 'anaphase1') setSelectedId('non_disjunction_calc');
              }}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                stage === s.id
                  ? 'bg-[#2B5B84] text-white shadow-xs'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
              }`}
            >
              {s.label}
            </button>
          ))}
        </div>
      </div>

      <AtlasCanvas3D
        testId="genetics-meiosis-3d-canvas"
        height={280}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle="Inspect recombinant swapped chromatid tips from Prophase I chiasmata or toggle Anaphase I non-disjunction"
      />

      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />
    </div>
  );
}
