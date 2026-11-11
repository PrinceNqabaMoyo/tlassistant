import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Atom, Layers, Sparkles, Droplets, Zap } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import {
  createFloorGrid3D,
  createSphereAtom3D,
  createBondCylinder3D,
  createVectorArrow3D,
} from '../shared/atlas3d/atlasPartsKit';
import { createPaperMaterial, tagInteractive3D } from '../shared/atlas3d/atlasRenderEngine';

const ATOM_PRESETS = {
  C: {
    symbol: 'C',
    name: 'Carbon-12',
    Z: 6,
    N: 6,
    shells: [2, 4],
    spdf: '1s² 2s² 2p²',
    valence: 4,
    ionCharge: 'Forms 4 covalent bonds',
    isotopes: '98.9% ¹²C (12 u) + 1.1% ¹³C (13 u) → Ar = 12.011',
  },
  O: {
    symbol: 'O',
    name: 'Oxygen-16',
    Z: 8,
    N: 8,
    shells: [2, 6],
    spdf: '1s² 2s² 2p⁴',
    valence: 6,
    ionCharge: 'O²⁻ (gains 2 e⁻ to complete octet)',
    isotopes: '99.76% ¹⁶O + 0.20% ¹⁸O → Ar = 15.999',
  },
  Na: {
    symbol: 'Na',
    name: 'Sodium-23',
    Z: 11,
    N: 12,
    shells: [2, 8, 1],
    spdf: '1s² 2s² 2p⁶ 3s¹',
    valence: 1,
    ionCharge: 'Na⁺ (loses 1 valence e⁻ from 3s¹)',
    isotopes: '100% ²³Na → Ar = 22.990',
  },
  Cl: {
    symbol: 'Cl',
    name: 'Chlorine-35/37',
    Z: 17,
    N: 18,
    shells: [2, 8, 7],
    spdf: '1s² 2s² 2p⁶ 3s² 3p⁵',
    valence: 7,
    ionCharge: 'Cl⁻ (gains 1 e⁻ into 3p orbital)',
    isotopes: '75% ³⁵Cl + 25% ³⁷Cl → Ar = (0.75×35)+(0.25×37) = 35.5',
  },
};

const LATTICE_MODES = {
  nacl: {
    id: 'nacl',
    label: 'NaCl Ionic Lattice',
    badge: '6:6 Cubic Coordination',
    desc: 'Alternating Na⁺ cations and Cl⁻ anions held by strong electrostatic attraction (F ∝ q₁q₂/r²). Brittle when sheared; dissolves in polar water via ion-dipole hydration.',
  },
  diamond: {
    id: 'diamond',
    label: 'Diamond (Covalent Network)',
    badge: 'sp³ Tetrahedral (109.5°)',
    desc: 'Every carbon atom is covalently bonded to 4 neighbours in a rigid 3D tetrahedral network. All 4 valence electrons are localised in σ-bonds → zero electrical conductivity.',
  },
  graphite: {
    id: 'graphite',
    label: 'Graphite (Layered Allotrope)',
    badge: 'sp² Hexagonal + Delocalised e⁻',
    desc: 'Each carbon bonds to 3 neighbours in flat 120° hexagonal layers. The 4th valence electron is delocalised between sheets → conducts electricity and slides as a lubricant.',
  },
  metallic: {
    id: 'metallic',
    label: 'Metallic Lattice (Cu²⁺ Sea)',
    badge: 'Positive Kernels + e⁻ Sea',
    desc: 'Positive metal kernels arranged in a regular 3D lattice surrounded by a mobile sea of delocalised valence electrons → malleable, ductile, and conducts heat/electricity.',
  },
};

const VSEPR_SHAPES = {
  linear: {
    id: 'linear',
    name: 'Carbon Dioxide (CO₂)',
    shapeName: 'Linear',
    angle: '180°',
    bp: 2,
    lp: 0,
    deltaChi: '|3.44 - 2.55| = 0.89 (Polar C=O bonds)',
    polarity: 'Non-polar overall (symmetrical 180° bond dipoles cancel: Σμ = 0)',
    atoms: [
      { pos: [0, 0, 0], r: 0.44, col: 0x334155 },
      { pos: [-1.75, 0, 0], r: 0.38, col: 0xe11d48 },
      { pos: [1.75, 0, 0], r: 0.38, col: 0xe11d48 },
    ],
    bonds: [
      { a: 0, b: 1, order: 2 },
      { a: 0, b: 2, order: 2 },
    ],
    lonePairs: [],
  },
  bent: {
    id: 'bent',
    name: 'Water (H₂O)',
    shapeName: 'Angular / Bent',
    angle: '104.5°',
    bp: 2,
    lp: 2,
    deltaChi: '|3.44 - 2.20| = 1.24 (Strongly Polar O–H)',
    polarity: 'Polar molecule (2 lone pairs compress bond angle from 109.5° to 104.5°; net dipole toward O)',
    atoms: [
      { pos: [0, 0.25, 0], r: 0.44, col: 0xe11d48 },
      { pos: [-1.25, -0.75, 0], r: 0.28, col: 0xf8fafc },
      { pos: [1.25, -0.75, 0], r: 0.28, col: 0xf8fafc },
    ],
    bonds: [
      { a: 0, b: 1, order: 1 },
      { a: 0, b: 2, order: 1 },
    ],
    lonePairs: [
      [0, 1.05, 0.72],
      [0, 1.05, -0.72],
    ],
  },
  pyramidal: {
    id: 'pyramidal',
    name: 'Ammonia (NH₃)',
    shapeName: 'Trigonal Pyramidal',
    angle: '107°',
    bp: 3,
    lp: 1,
    deltaChi: '|3.04 - 2.20| = 0.84 (Polar N–H)',
    polarity: 'Polar molecule (1 lone pair at apex compresses H–N–H angle to 107°; forms Hydrogen bonds)',
    atoms: [
      { pos: [0, 0.35, 0], r: 0.44, col: 0x2563eb },
      { pos: [-1.25, -0.65, 0.72], r: 0.28, col: 0xf8fafc },
      { pos: [1.25, -0.65, 0.72], r: 0.28, col: 0xf8fafc },
      { pos: [0, -0.65, -1.42], r: 0.28, col: 0xf8fafc },
    ],
    bonds: [
      { a: 0, b: 1, order: 1 },
      { a: 0, b: 2, order: 1 },
      { a: 0, b: 3, order: 1 },
    ],
    lonePairs: [[0, 1.32, 0]],
  },
  tetrahedral: {
    id: 'tetrahedral',
    name: 'Methane (CH₄)',
    shapeName: 'Tetrahedral',
    angle: '109.5°',
    bp: 4,
    lp: 0,
    deltaChi: '|2.55 - 2.20| = 0.35 (Weakly polar C–H)',
    polarity: 'Non-polar overall (4 symmetrical tetrahedral bonds at 109.5° cancel out: Σμ = 0)',
    atoms: [
      { pos: [0, 0, 0], r: 0.44, col: 0x334155 },
      { pos: [0, 1.55, 0], r: 0.28, col: 0xf8fafc },
      { pos: [-1.42, -0.52, 0.82], r: 0.28, col: 0xf8fafc },
      { pos: [1.42, -0.52, 0.82], r: 0.28, col: 0xf8fafc },
      { pos: [0, -0.52, -1.55], r: 0.28, col: 0xf8fafc },
    ],
    bonds: [
      { a: 0, b: 1, order: 1 },
      { a: 0, b: 2, order: 1 },
      { a: 0, b: 3, order: 1 },
      { a: 0, b: 4, order: 1 },
    ],
    lonePairs: [],
  },
};

export default function AtomicBondingLatticeAtlasAid() {
  const [activeTab, setActiveTab] = useState('crystal_lattices'); // 'bohr_orbitals' | 'crystal_lattices' | 'vsepr_geometry'
  const [atomKey, setAtomKey] = useState('Cl');
  const [orbitalView, setOrbitalView] = useState('bohr'); // 'bohr' | 'spdf'
  const [latticeKey, setLatticeKey] = useState('nacl');
  const [hydrateWater, setHydrateWater] = useState(false);
  const [applyVoltage, setApplyVoltage] = useState(true);
  const [vseprKey, setVseprKey] = useState('bent');
  const [selectedCalcId, setSelectedCalcId] = useState(null);

  const atomData = ATOM_PRESETS[atomKey] || ATOM_PRESETS.Cl;
  const latticeData = LATTICE_MODES[latticeKey] || LATTICE_MODES.nacl;
  const vseprData = VSEPR_SHAPES[vseprKey] || VSEPR_SHAPES.bent;

  // Inspectable calculation items per mode
  const calcItems = useMemo(() => {
    if (activeTab === 'bohr_orbitals') {
      return [
        {
          id: 'nucleus_mass',
          label: `${atomData.name} Nucleus (Z=${atomData.Z}, N=${atomData.N})`,
          shortLabel: 'Mass Number (A)',
          badge: `Z = ${atomData.Z}`,
          color: '#E11D48',
          result: `A = ${atomData.Z + atomData.N}`,
          formula: '$$A = Z + N$$',
          substitution: `$$A = ${atomData.Z}\\text{ protons} + ${atomData.N}\\text{ neutrons} = ${
            atomData.Z + atomData.N
          }\\text{ nucleons}$$`,
          mechanism: `The dense central nucleus holds ${atomData.Z} positively charged protons and ${atomData.N} neutral neutrons bound by the strong nuclear force. Isotopes calculation: ${atomData.isotopes}.`,
        },
        {
          id: 'valence_shell',
          label: `Valence Shell & AufBau Configuration`,
          shortLabel: 'Valence & Charge',
          badge: atomData.spdf,
          color: '#2563EB',
          result: `${atomData.valence} valence e⁻`,
          formula: '$$q_{\\text{ion}} = Z - N_{e^-}$$',
          substitution: `$$\\text{Shells: } (${atomData.shells.join(', ')}) \\implies \\text{Valence } = ${
            atomData.valence
          }\\;e^-$$`,
          mechanism: `${atomData.ionCharge}. Electrons occupy the lowest available energy sublevels first (1s → 2s → 2p → 3s → 3p) following Pauli exclusion and Hund's rule.`,
        },
      ];
    }

    if (activeTab === 'crystal_lattices') {
      if (latticeKey === 'nacl') {
        return [
          {
            id: 'ionic_bond',
            label: 'Electrostatic Ionic Lattice Force (Na⁺Cl⁻)',
            shortLabel: 'Coulomb Lattice Bond',
            badge: '6:6 Cubic',
            color: '#7C3AED',
            result: 'Tm = 801 °C',
            formula: '$$F_e = \\frac{k \\cdot |q_{\\text{Na}^+} \\cdot q_{\\text{Cl}^-}|}{r^2}$$',
            substitution: '$$\\Delta\\chi = |3.16 - 0.93| = 2.23 > 1.9 \\implies \\text{Complete } e^- \\text{ transfer}$$',
            mechanism:
              'Each Na⁺ ion is surrounded by 6 Cl⁻ ions in 3D space. Because strong electrostatic attractions act in all directions, a large amount of thermal energy is needed to melt the crystal (801 °C). Solid NaCl cannot conduct electricity because ions are locked in fixed lattice positions.',
          },
          {
            id: 'hydration_shell',
            label: 'Ion-Dipole Hydration in Water (Dissolution)',
            shortLabel: 'Water Hydration',
            badge: hydrateWater ? 'Dissolving Active' : 'Toggle Hydration',
            color: '#0284C7',
            result: 'NaCl(s) → Na⁺(aq) + Cl⁻(aq)',
            formula: '$$\\text{NaCl}(s) \\xrightarrow{\\text{H}_2\\text{O}} \\text{Na}^+(aq) + \\text{Cl}^-(aq)$$',
            substitution:
              '$$\\text{O}^{\\delta-} \\to \\text{Na}^+ \\quad \\text{and} \\quad \\text{H}^{\\delta+} \\to \\text{Cl}^-$$',
            mechanism:
              'Polar H₂O molecules surround surface ions with their negative oxygen (δ⁻) facing Na⁺ and positive hydrogens (δ⁺) facing Cl⁻. This ion-dipole attraction overcomes the lattice energy and frees mobile ions that conduct electricity as an electrolyte!',
          },
        ];
      }
      if (latticeKey === 'graphite') {
        return [
          {
            id: 'graphite_delocalised',
            label: 'Graphite sp² Layers & Mobile Delocalised Electrons',
            shortLabel: 'sp² Delocalised e⁻',
            badge: '120° Hexagonal',
            color: '#F59E0B',
            result: '3 σ-bonds + 1 free e⁻',
            formula: '$$e^-_{\\text{free per C}} = 4_{\\text{valence}} - 3_{\\text{covalent bonds}} = 1\\;e^-$$',
            substitution: '$$d_{\\text{in-layer}} = 0.142\\text{ nm} \\ll d_{\\text{between-layers}} = 0.335\\text{ nm}$$',
            mechanism:
              'Each carbon bonds strongly to 3 neighbours in flat hexagonal sheets, leaving 1 unhybridised p-electron per atom free to drift along the plane. Weak London forces between layers allow sheets to slide over one another (lubricant).',
          },
        ];
      }
      if (latticeKey === 'diamond') {
        return [
          {
            id: 'diamond_network',
            label: 'Diamond sp³ Giant Covalent Network',
            shortLabel: 'sp³ Tetrahedral',
            badge: '109.5° Network',
            color: '#0EA5E9',
            result: '0 free electrons',
            formula: '$$e^-_{\\text{free per C}} = 4_{\\text{valence}} - 4_{\\text{covalent } \\sigma\\text{-bonds}} = 0$$',
            substitution: '$$\\text{Bond angle} = 109.5^\\circ, \\quad T_m \\approx 3550\\text{ ^\\circ C}$$',
            mechanism:
              'All 4 valence electrons of every carbon atom are locked in strong covalent bonds arranged tetrahedrally in 3D. With zero mobile electrons or ions, diamond cannot conduct electricity.',
          },
        ];
      }
      return [
        {
          id: 'metallic_sea',
          label: 'Metallic Bonding: Positive Kernels + Delocalised e⁻ Sea',
          shortLabel: 'Electron Sea Drift',
          badge: applyVoltage ? 'E-Field Drift Active' : 'Random Thermal Motion',
          color: '#D97706',
          result: 'I = ΔQ / Δt',
          formula: '$$I = n \\cdot A \\cdot v_d \\cdot e$$',
          substitution:
            '$$\\text{Cu}^{2+}\\text{ kernels in 3D lattice} + 2\\text{ mobile valence } e^-\\text{ per atom}$$',
          mechanism:
            'Delocalised valence electrons move freely throughout the metallic lattice. When a potential difference is applied, electrons drift uniformly toward the positive terminal (electrical conduction). If a layer of kernels is pushed, the mobile electron sea moves with them, preventing repulsive fracture (malleability & ductility).',
        },
      ];
    }

    // VSEPR tab
    return [
      {
        id: 'vsepr_angle',
        label: `${vseprData.name} — ${vseprData.shapeName} Geometry`,
        shortLabel: `Bond Angle (${vseprData.angle})`,
        badge: `${vseprData.bp} BP, ${vseprData.lp} LP`,
        color: '#13519C',
        result: vseprData.angle,
        formula: '$$\\text{Steric Number } SN = \\text{BP} + \\text{LP}$$',
        substitution: `$$SN = ${vseprData.bp}\\text{ bonding pairs} + ${vseprData.lp}\\text{ lone pairs} = ${
          vseprData.bp + vseprData.lp
        }$$`,
        mechanism:
          'Valence Shell Electron Pair Repulsion (VSEPR): Lone pairs occupy more space closer to the central nucleus than bonding pairs. Repulsion strength: LP–LP > LP–BP > BP–BP.',
      },
      {
        id: 'bond_dipole',
        label: 'Electronegativity Difference & Molecular Polarity',
        shortLabel: 'Dipole & Δχ',
        badge: vseprData.deltaChi,
        color: '#059669',
        result: vseprData.lp > 0 ? 'Polar (μ ≠ 0)' : 'Non-Polar (μ = 0)',
        formula: '$$\\Delta\\chi = |\\chi_A - \\chi_B|$$',
        substitution: `$$\\Delta\\chi = ${vseprData.deltaChi}$$`,
        mechanism: vseprData.polarity,
      },
    ];
  }, [activeTab, atomData, latticeKey, hydrateWater, applyVoltage, vseprData]);

  const activeCalcItem =
    calcItems.find((c) => c.id === selectedCalcId) || calcItems[0] || null;

  // Build Three.js Scene
  const buildScene = useCallback(
    ({ scene }) => {
      scene.add(createFloorGrid3D({ size: 9, divisions: 9, y: -2.0 }));
      const animatedElectrons = [];
      const animatedHydration = [];

      if (activeTab === 'bohr_orbitals') {
        // Central Nucleus cluster of protons (red) and neutrons (slate)
        const nucGroup = new THREE.Group();
        const totalNucleons = Math.min(20, atomData.Z + atomData.N);
        for (let i = 0; i < totalNucleons; i++) {
          const phi = Math.acos(1 - (2 * (i + 0.5)) / totalNucleons);
          const theta = Math.PI * (1 + Math.sqrt(5)) * i;
          const r = 0.28;
          const isProton = i % 2 === 0;
          const nucleon = createSphereAtom3D({
            radius: 0.16,
            color: isProton ? 0xe11d48 : 0x64748b,
            position: [
              r * Math.sin(phi) * Math.cos(theta),
              r * Math.cos(phi),
              r * Math.sin(phi) * Math.sin(theta),
            ],
          });
          nucGroup.add(nucleon);
        }
        tagInteractive3D(nucGroup, 'nucleus_mass');
        scene.add(nucGroup);

        if (orbitalView === 'bohr') {
          // Concentric 3D Bohr Rings + Orbiting Electrons
          atomData.shells.forEach((count, sIdx) => {
            const shellRadius = 1.15 + sIdx * 0.9;
            const ringGeo = new THREE.TorusGeometry(shellRadius, 0.02, 8, 48);
            const tiltX = sIdx === 0 ? 0.35 : sIdx === 1 ? -0.42 : 0.22;
            const tiltZ = sIdx === 1 ? 0.25 : -0.18;
            const ringMesh = new THREE.Mesh(
              ringGeo,
              createPaperMaterial(sIdx === atomData.shells.length - 1 ? 0x2563eb : 0x94a3b8)
            );
            ringMesh.rotation.set(Math.PI / 2 + tiltX, 0, tiltZ);
            tagInteractive3D(ringMesh, 'valence_shell');
            scene.add(ringMesh);

            for (let eIdx = 0; eIdx < count; eIdx++) {
              const baseAngle = (eIdx / count) * Math.PI * 2;
              const isValence = sIdx === atomData.shells.length - 1;
              const elSphere = createSphereAtom3D({
                radius: isValence ? 0.14 : 0.11,
                color: isValence ? 0x2563eb : 0x38bdf8,
                glow: isValence ? 0.3 : 0.1,
                interactiveId: 'valence_shell',
              });
              scene.add(elSphere);
              animatedElectrons.push({
                mesh: elSphere,
                radius: shellRadius,
                baseAngle,
                speed: 1.4 - sIdx * 0.32,
                tiltX,
                tiltZ,
              });
            }
          });
        } else {
          // 3D s and p Quantum Orbital Probability Lobes (1s, 2s spheres + 2px, 2py, 2pz dumbbells)
          const sOrbital = createSphereAtom3D({
            radius: 0.85,
            color: 0x38bdf8,
            opacity: 0.35,
            interactiveId: 'valence_shell',
          });
          scene.add(sOrbital);

          const axes = [
            { dir: [1, 0, 0], col: 0x2563eb },
            { dir: [0, 1, 0], col: 0x10b981 },
            { dir: [0, 0, 1], col: 0xf59e0b },
          ];
          axes.forEach((ax) => {
            [-1, 1].forEach((sign) => {
              const lobeGeo = new THREE.SphereGeometry(0.45, 18, 18);
              lobeGeo.scale(
                ax.dir[0] ? 1.85 : 0.85,
                ax.dir[1] ? 1.85 : 0.85,
                ax.dir[2] ? 1.85 : 0.85
              );
              const lobe = new THREE.Mesh(
                lobeGeo,
                createPaperMaterial(ax.col, { opacity: 0.55 })
              );
              lobe.position.set(
                ax.dir[0] * sign * 1.15,
                ax.dir[1] * sign * 1.15,
                ax.dir[2] * sign * 1.15
              );
              tagInteractive3D(lobe, 'valence_shell');
              scene.add(lobe);
            });
          });
        }
      } else if (activeTab === 'crystal_lattices') {
        if (latticeKey === 'nacl') {
          // 3x3x3 NaCl Cubic Crystal Lattice
          const spacing = 1.05;
          for (let ix = -1; ix <= 1; ix++) {
            for (let iy = -1; iy <= 1; iy++) {
              for (let iz = -1; iz <= 1; iz++) {
                const isCl = (Math.abs(ix + iy + iz) % 2) === 0;
                const pos = [ix * spacing, iy * spacing, iz * spacing];
                const ion = createSphereAtom3D({
                  radius: isCl ? 0.31 : 0.21,
                  color: isCl ? 0x10b981 : 0x7c3aed, // Green Cl- (larger), Purple Na+ (smaller)
                  position: pos,
                  interactiveId: 'ionic_bond',
                });
                scene.add(ion);

                if (ix < 1) {
                  scene.add(
                    createBondCylinder3D({
                      start: pos,
                      end: [(ix + 1) * spacing, iy * spacing, iz * spacing],
                      radius: 0.035,
                      color: 0x94a3b8,
                      interactiveId: 'ionic_bond',
                    })
                  );
                }
                if (iy < 1) {
                  scene.add(
                    createBondCylinder3D({
                      start: pos,
                      end: [ix * spacing, (iy + 1) * spacing, iz * spacing],
                      radius: 0.035,
                      color: 0x94a3b8,
                      interactiveId: 'ionic_bond',
                    })
                  );
                }
                if (iz < 1) {
                  scene.add(
                    createBondCylinder3D({
                      start: pos,
                      end: [ix * spacing, iy * spacing, (iz + 1) * spacing],
                      radius: 0.035,
                      color: 0x94a3b8,
                      interactiveId: 'ionic_bond',
                    })
                  );
                }
              }
            }
          }

          // If Hydration is active, show polar H2O molecules pulling a corner Na+ and Cl- ion out
          if (hydrateWater) {
            const hydratedGroup = new THREE.Group();
            const naExtracted = createSphereAtom3D({
              radius: 0.22,
              color: 0x7c3aed,
              position: [2.4, 0.6, 0],
              glow: 0.3,
              interactiveId: 'hydration_shell',
            });
            hydratedGroup.add(naExtracted);
            // 3 water molecules orienting red Oxygen (δ-) toward Na+
            for (let k = 0; k < 3; k++) {
              const ang = (k / 3) * Math.PI * 2;
              const oxPos = [
                2.4 + 0.72 * Math.cos(ang),
                0.6 + 0.72 * Math.sin(ang),
                0,
              ];
              hydratedGroup.add(
                createSphereAtom3D({
                  radius: 0.16,
                  color: 0xe11d48,
                  position: oxPos,
                  interactiveId: 'hydration_shell',
                })
              );
            }
            scene.add(hydratedGroup);
            animatedHydration.push(hydratedGroup);
          }
        } else if (latticeKey === 'graphite') {
          // 2 Hexagonal sp2 Carbon Sheets + Drifting Delocalised Electrons between layers
          [-0.85, 0.85].forEach((yLayer) => {
            const hexCenters = [
              [0, 0],
              [1.2, 0],
              [-1.2, 0],
              [0.6, 1.04],
              [-0.6, 1.04],
              [0.6, -1.04],
              [-0.6, -1.04],
            ];
            hexCenters.forEach(([cx, cz]) => {
              const ringPts = [];
              for (let i = 0; i < 6; i++) {
                const a = (i * Math.PI) / 3;
                const px = cx + 0.68 * Math.cos(a);
                const pz = cz + 0.68 * Math.sin(a);
                ringPts.push([px, yLayer, pz]);
                scene.add(
                  createSphereAtom3D({
                    radius: 0.15,
                    color: 0x334155,
                    position: [px, yLayer, pz],
                    interactiveId: 'graphite_delocalised',
                  })
                );
              }
              for (let i = 0; i < 6; i++) {
                scene.add(
                  createBondCylinder3D({
                    start: ringPts[i],
                    end: ringPts[(i + 1) % 6],
                    radius: 0.04,
                    color: 0x64748b,
                    interactiveId: 'graphite_delocalised',
                  })
                );
              }
            });
          });

          // Delocalised mobile electrons drifting between the layers (y = 0)
          for (let e = 0; e < 14; e++) {
            const el = createSphereAtom3D({
              radius: 0.09,
              color: 0xf59e0b,
              glow: 0.5,
              position: [-2 + (e % 7) * 0.65, (e % 2 === 0 ? -0.25 : 0.25), -1.2 + Math.floor(e / 7) * 2.4],
              interactiveId: 'graphite_delocalised',
            });
            scene.add(el);
            animatedElectrons.push({
              mesh: el,
              isLinearDrift: true,
              baseX: -2.2 + (e / 14) * 4.4,
              y: e % 2 === 0 ? -0.28 : 0.28,
              z: ((e * 1.3) % 2.4) - 1.2,
              speed: 1.6,
            });
          }
        } else if (latticeKey === 'diamond') {
          // Tetrahedral sp3 covalent network
          const nodes = [
            [0, 0, 0],
            [0.9, 0.9, 0.9],
            [-0.9, -0.9, 0.9],
            [-0.9, 0.9, -0.9],
            [0.9, -0.9, -0.9],
            [1.8, 0, 1.8],
            [-1.8, 0, -1.8],
            [0, 1.8, 1.8],
            [0, -1.8, -1.8],
          ];
          const edges = [
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
            [1, 5],
            [1, 7],
            [3, 6],
            [4, 8],
          ];
          nodes.forEach((p) => {
            scene.add(
              createSphereAtom3D({
                radius: 0.24,
                color: 0x0ea5e9,
                position: p,
                interactiveId: 'diamond_network',
              })
            );
          });
          edges.forEach(([i, j]) => {
            scene.add(
              createBondCylinder3D({
                start: nodes[i],
                end: nodes[j],
                radius: 0.06,
                color: 0x334155,
                interactiveId: 'diamond_network',
              })
            );
          });
        } else {
          // Metallic Lattice: Cu2+ positive kernels + sea of delocalised electrons
          for (let ix = -1.5; ix <= 1.5; ix += 1.0) {
            for (let iy = -0.8; iy <= 0.8; iy += 0.8) {
              for (let iz = -0.8; iz <= 0.8; iz += 0.8) {
                scene.add(
                  createSphereAtom3D({
                    radius: 0.26,
                    color: 0xd97706,
                    position: [ix, iy, iz],
                    interactiveId: 'metallic_sea',
                  })
                );
              }
            }
          }
          for (let e = 0; e < 22; e++) {
            const el = createSphereAtom3D({
              radius: 0.085,
              color: 0x38bdf8,
              glow: 0.5,
              interactiveId: 'metallic_sea',
            });
            scene.add(el);
            animatedElectrons.push({
              mesh: el,
              isLinearDrift: applyVoltage,
              baseX: -2.2 + (e / 22) * 4.4,
              y: ((e * 0.73) % 2.0) - 1.0,
              z: ((e * 1.17) % 2.0) - 1.0,
              speed: applyVoltage ? 2.1 : 0.4,
            });
          }
        }
      } else {
        // VSEPR Molecular Geometry
        vseprData.atoms.forEach((a) => {
          scene.add(
            createSphereAtom3D({
              radius: a.r,
              color: a.col,
              position: a.pos,
              interactiveId: 'vsepr_angle',
            })
          );
        });
        vseprData.bonds.forEach((b) => {
          scene.add(
            createBondCylinder3D({
              start: vseprData.atoms[b.a].pos,
              end: vseprData.atoms[b.b].pos,
              order: b.order,
              radius: 0.075,
              color: 0x64748b,
              interactiveId: 'bond_dipole',
            })
          );
        });
        // Lone pair translucent clouds
        vseprData.lonePairs.forEach((lpPos) => {
          const lpOrb = createSphereAtom3D({
            radius: 0.36,
            color: 0xf59e0b,
            opacity: 0.48,
            position: lpPos,
            interactiveId: 'vsepr_angle',
          });
          scene.add(lpOrb);
        });
        // Net dipole vector if polar
        if (vseprData.lp > 0) {
          scene.add(
            createVectorArrow3D({
              origin: [1.9, -0.7, 0],
              dir: [0, 1, 0],
              length: 1.45,
              color: 0x059669,
              interactiveId: 'bond_dipole',
            })
          );
        }
      }

      return {
        onTick: (elapsed) => {
          animatedElectrons.forEach((item, idx) => {
            if (item.isLinearDrift !== undefined) {
              if (item.isLinearDrift) {
                const x = ((item.baseX + elapsed * item.speed + 2.4) % 4.8) - 2.4;
                item.mesh.position.set(
                  x,
                  item.y + Math.sin(elapsed * 5 + idx) * 0.08,
                  item.z
                );
              } else {
                item.mesh.position.set(
                  item.baseX + Math.sin(elapsed * 3 + idx) * 0.25,
                  item.y + Math.cos(elapsed * 2.7 + idx) * 0.25,
                  item.z + Math.sin(elapsed * 2.2 + idx * 2) * 0.25
                );
              }
            } else {
              const ang = item.baseAngle + elapsed * item.speed;
              const localPos = new THREE.Vector3(
                item.radius * Math.cos(ang),
                0,
                item.radius * Math.sin(ang)
              );
              const euler = new THREE.Euler(item.tiltX, 0, item.tiltZ);
              localPos.applyEuler(euler);
              item.mesh.position.copy(localPos);
            }
          });
          animatedHydration.forEach((grp) => {
            grp.position.x = Math.sin(elapsed * 2.2) * 0.22;
          });
        },
      };
    },
    [activeTab, atomData, orbitalView, latticeKey, hydrateWater, applyVoltage, vseprData]
  );

  return (
    <div data-testid="atomic-bonding-lattice-aid" className="space-y-3 text-slate-800">
      {/* Top Mode Switcher */}
      <div className="grid grid-cols-3 gap-1.5 bg-slate-100 p-1.5 rounded-xl border border-slate-200">
        {[
          { id: 'crystal_lattices', label: '1. 3D Crystal Lattices', icon: Layers },
          { id: 'bohr_orbitals', label: '2. Atom & Orbitals', icon: Atom },
          { id: 'vsepr_geometry', label: '3. VSEPR & Polarity', icon: Sparkles },
        ].map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              type="button"
              data-testid={`tab-atomic-${tab.id}`}
              onClick={() => {
                setActiveTab(tab.id);
                setSelectedCalcId(null);
              }}
              className={`flex items-center justify-center gap-1.5 py-1.5 px-2 rounded-lg text-xs font-bold transition-all ${
                isActive
                  ? 'bg-[#13519C] text-white shadow-xs'
                  : 'bg-white text-slate-600 hover:bg-slate-50 border border-slate-200/80'
              }`}
            >
              <Icon className="w-3.5 h-3.5 shrink-0" />
              <span className="truncate">{tab.label}</span>
            </button>
          );
        })}
      </div>

      {/* Mode-Specific Controls */}
      <div className="p-3 bg-white rounded-xl border border-slate-200 shadow-xs space-y-2.5">
        {activeTab === 'crystal_lattices' && (
          <>
            <div className="flex flex-wrap gap-1.5">
              {Object.values(LATTICE_MODES).map((lat) => (
                <button
                  key={lat.id}
                  type="button"
                  data-testid={`btn-lattice-${lat.id}`}
                  onClick={() => setLatticeKey(lat.id)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-semibold border transition-all ${
                    latticeKey === lat.id
                      ? 'bg-slate-900 text-white border-slate-900'
                      : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                  }`}
                >
                  {lat.label}
                </button>
              ))}
            </div>

            <div className="flex items-center justify-between gap-2 pt-1 border-t border-slate-100">
              <p className="text-[11px] text-slate-600 leading-snug">{latticeData.desc}</p>
              {latticeKey === 'nacl' && (
                <button
                  type="button"
                  data-testid="btn-toggle-hydration"
                  onClick={() => {
                    setHydrateWater((v) => !v);
                    setSelectedCalcId('hydration_shell');
                  }}
                  className={`shrink-0 inline-flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs font-bold border transition-all ${
                    hydrateWater
                      ? 'bg-sky-600 text-white border-sky-600'
                      : 'bg-sky-50 text-sky-800 border-sky-200 hover:bg-sky-100'
                  }`}
                >
                  <Droplets className="w-3.5 h-3.5" />
                  <span>{hydrateWater ? 'Hydration Active' : '+ Add H₂O Hydration'}</span>
                </button>
              )}
              {latticeKey === 'metallic' && (
                <button
                  type="button"
                  data-testid="btn-toggle-metallic-voltage"
                  onClick={() => setApplyVoltage((v) => !v)}
                  className={`shrink-0 inline-flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs font-bold border transition-all ${
                    applyVoltage
                      ? 'bg-amber-600 text-white border-amber-600'
                      : 'bg-amber-50 text-amber-900 border-amber-200'
                  }`}
                >
                  <Zap className="w-3.5 h-3.5" />
                  <span>{applyVoltage ? 'Voltage Drift ON' : 'Thermal Random'}</span>
                </button>
              )}
            </div>
          </>
        )}

        {activeTab === 'bohr_orbitals' && (
          <div className="flex flex-wrap items-center justify-between gap-2">
            <div className="flex flex-wrap gap-1.5">
              {Object.values(ATOM_PRESETS).map((at) => (
                <button
                  key={at.symbol}
                  type="button"
                  data-testid={`btn-atom-${at.symbol}`}
                  onClick={() => setAtomKey(at.symbol)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-bold border ${
                    atomKey === at.symbol
                      ? 'bg-[#13519C] text-white border-[#13519C]'
                      : 'bg-slate-50 text-slate-700 border-slate-200'
                  }`}
                >
                  {at.name} (Z={at.Z})
                </button>
              ))}
            </div>
            <div className="flex items-center gap-1">
              <button
                type="button"
                data-testid="btn-orbital-bohr"
                onClick={() => setOrbitalView('bohr')}
                className={`px-2.5 py-1 rounded-md text-xs font-semibold border ${
                  orbitalView === 'bohr'
                    ? 'bg-slate-900 text-white border-slate-900'
                    : 'bg-white text-slate-600 border-slate-200'
                }`}
              >
                Bohr Shells
              </button>
              <button
                type="button"
                data-testid="btn-orbital-spdf"
                onClick={() => setOrbitalView('spdf')}
                className={`px-2.5 py-1 rounded-md text-xs font-semibold border ${
                  orbitalView === 'spdf'
                    ? 'bg-slate-900 text-white border-slate-900'
                    : 'bg-white text-slate-600 border-slate-200'
                }`}
              >
                3D s & p Orbitals
              </button>
            </div>
          </div>
        )}

        {activeTab === 'vsepr_geometry' && (
          <div className="flex flex-wrap gap-1.5">
            {Object.values(VSEPR_SHAPES).map((sh) => (
              <button
                key={sh.id}
                type="button"
                data-testid={`btn-vsepr-${sh.id}`}
                onClick={() => setVseprKey(sh.id)}
                className={`px-2.5 py-1 rounded-lg text-xs font-semibold border ${
                  vseprKey === sh.id
                    ? 'bg-[#13519C] text-white border-[#13519C]'
                    : 'bg-slate-50 text-slate-700 border-slate-200'
                }`}
              >
                {sh.shapeName}: {sh.name} ({sh.angle})
              </button>
            ))}
          </div>
        )}
      </div>

      {/* 3D Paper & Ink Viewport */}
      <AtlasCanvas3D
        buildScene={buildScene}
        sceneDeps={[activeTab, atomKey, orbitalView, latticeKey, hydrateWater, applyVoltage, vseprKey]}
        activeInteractiveId={activeCalcItem?.id}
        onSelectInteractive={(id) => setSelectedCalcId(id)}
        badgeText={
          activeTab === 'crystal_lattices'
            ? latticeData.badge
            : activeTab === 'bohr_orbitals'
            ? `${atomData.name} (${atomData.spdf})`
            : `${vseprData.shapeName} (${vseprData.angle})`
        }
      />

      {/* Interactive Calculation & Mechanism Popover */}
      <CalculationPopoverCard
        item={activeCalcItem}
        allItems={calcItems}
        onSelectItem={(it) => setSelectedCalcId(it.id)}
      />
    </div>
  );
}
