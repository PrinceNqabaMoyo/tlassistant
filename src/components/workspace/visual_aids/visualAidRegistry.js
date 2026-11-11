/**
 * visualAidRegistry.js
 * Central Registry of Cognitive Visual Aids for UniversalWorkspace.
 *
 * Architectural Invariant:
 * Visual Aids are exploratory pedagogical scaffolds that open on-demand in the
 * non-intrusive Cognitive Sidecar Drawer. Unlike Question Diagrams (which live
 * in the question card and are actively graded), Visual Aids are NEVER graded
 * and do not alter student answer submissions.
 */

import React from 'react';
import {
  Atom,
  Compass,
  Layers,
  Sparkles,
  Activity,
  Box,
  Zap,
  Flame,
  FlaskConical,
  TrendingUp,
  CircleDot,
  Eye,
  Wind,
  Dna,
  Landmark,
} from 'lucide-react';

export const VISUAL_AIDS = {
  aid_periodic_table: {
    id: 'aid_periodic_table',
    title: '118-Element Periodic Table',
    shortTitle: 'Periodic Table',
    category: 'Chemistry & Matter',
    description: 'Interactive atomic numbers, Bohr/spdf electron configurations, and periodic trend heatmaps.',
    icon: Atom,
    testId: 'periodic-table-aid',
    component: React.lazy(() => import('./PeriodicTableAid')),
    matchKeywords: [
      'periodic', 'element', 'atom', 'matter', 'subatomic',
      'chemical reaction', 'chemical change', 'bonding', 'stoichiometry',
      'acid', 'base', 'neutral', 'electrochemistry', 'galvanic', 'redox',
      'solution', 'titration', 'concentration', 'mole', 'valency',
    ],
  },
  aid_atomic_bonding_lattice: {
    id: 'aid_atomic_bonding_lattice',
    title: '3D Atomic Structure, Bonding & Crystal Lattices',
    shortTitle: '3D Lattices & VSEPR',
    category: 'Chemistry & Matter',
    description: '3D Bohr vs. s/p orbitals, NaCl ionic lattice hydration, Diamond sp³ vs. Graphite sp² delocalised electrons, Metallic Cu²⁺ electron sea, and VSEPR shapes.',
    icon: Atom,
    testId: 'atomic-bonding-lattice-aid',
    component: React.lazy(() => import('./AtomicBondingLatticeAtlasAid')),
    matchKeywords: [
      'atomic structure', 'bohr', 'orbital', 'isotope', 'chemical bonding',
      'ionic', 'covalent', 'metallic', 'lattice', 'crystal', 'nacl',
      'diamond', 'graphite', 'vsepr', 'molecular shape', 'electronegativity',
      'intermolecular', 'compound', 'atoms',
    ],
  },
  aid_kinetic_matter_states: {
    id: 'aid_kinetic_matter_states',
    title: '3D Kinetic Theory of Matter, States & Gas Laws',
    shortTitle: '3D States of Matter',
    category: 'Chemistry & Matter',
    description: '3D Solid lattice vibration, melting/boiling latent-heat plateaus where intermolecular bonds break at constant T, and ideal gas piston P-V collisions.',
    icon: Flame,
    testId: 'kinetic-matter-states-aid',
    component: React.lazy(() => import('./KineticMatterStatesAtlasAid')),
    matchKeywords: [
      'states of matter', 'kinetic molecular', 'particle model', 'heating curve',
      'cooling curve', 'latent heat', 'melting', 'boiling', 'evaporation',
      'ideal gas', 'boyle', 'charles', 'pressure', 'phase change', 'matter and materials',
    ],
  },
  aid_circuit_potential_atlas: {
    id: 'aid_circuit_potential_atlas',
    title: '3D Electric Circuit Potential & Resistor Collisions',
    shortTitle: '3D Circuit Voltage',
    category: 'Physical & Natural Sciences',
    description: '3D Paper & Ink circuit elevating electric potential y ∝ V(x), showing electron deceleration & lattice collisions inside resistors (P = I²R) and lost volts (Ir).',
    icon: Zap,
    testId: 'circuit-potential-atlas-aid',
    component: React.lazy(() => import('./CircuitPotentialAtlasAid')),
    matchKeywords: [
      'electric circuit', 'circuit', 'ohm', 'resistor', 'resistance',
      'internal resistance', 'series', 'parallel', 'current', 'potential difference',
      'voltage', 'emf', 'power', 'energy and change', 'electricity',
    ],
  },
  aid_newton_mechanics_atlas: {
    id: 'aid_newton_mechanics_atlas',
    title: '3D Inclined Plane & Free-Body Vector Resolution',
    shortTitle: '3D Forces & Incline',
    category: 'Physical Sciences',
    description: 'Interactive 3D inclined plane decomposing weight Fg into Fg∥ = mg sin θ and Fg⊥ = mg cos θ alongside normal force FN and kinetic friction fk.',
    icon: Compass,
    testId: 'newton-mechanics-atlas-aid',
    component: React.lazy(() => import('./NewtonMechanicsAtlasAid')),
    matchKeywords: [
      'newton', 'force', 'incline', 'slope', 'friction', 'normal force',
      'free-body', 'free body', 'vector', 'work', 'energy and power',
      'momentum', 'impulse', 'equilibrium', 'mechanics',
    ],
  },
  aid_kinematics_projectile_atlas: {
    id: 'aid_kinematics_projectile_atlas',
    title: '3D Projectile Strobe & Doppler Wavefronts',
    shortTitle: '3D Motion & Doppler',
    category: 'Physical Sciences',
    description: '3D stroboscopic vertical projectile motion showing why vy = 0 at the apex while g = 9.8 m/s² downwards, plus 3D Doppler wavefront compression.',
    icon: Activity,
    testId: 'kinematics-projectile-atlas-aid',
    component: React.lazy(() => import('./KinematicsProjectileAtlasAid')),
    matchKeywords: [
      'projectile', 'vertical projectile', 'equations of motion', 'kinematics',
      'free fall', 'velocity', 'acceleration', 'doppler', 'wavefront',
      'frequency', 'pitch', 'redshift', 'motion in one dimension',
    ],
  },
  aid_electrochemistry_titration_atlas: {
    id: 'aid_electrochemistry_titration_atlas',
    title: '3D Galvanic Cell & Acid-Base Titration Lab',
    shortTitle: '3D Redox & Titration',
    category: 'Physical Sciences',
    description: '3D Zn-Cu galvanic cell with anode oxidation, cathode plating, and salt bridge migration, plus 3D burette acid-base titration pH equivalence curve.',
    icon: FlaskConical,
    testId: 'electrochemistry-titration-atlas-aid',
    component: React.lazy(() => import('./ElectrochemistryAndTitrationAtlasAid')),
    matchKeywords: [
      'electrochemistry', 'galvanic', 'electrolytic', 'redox', 'anode',
      'cathode', 'salt bridge', 'cell potential', 'acid', 'base',
      'titration', 'ph', 'neutralisation', 'equivalence', 'stoichiometry',
    ],
  },
  aid_unit_circle_trig: {
    id: 'aid_unit_circle_trig',
    title: 'Dynamic Unit Circle & Wave Trigonometry',
    shortTitle: 'Unit Circle',
    category: 'Mathematics & Waves',
    description: 'Cartesian unit circle, ASTC quadrant signs, exact surd ratios, and simultaneous waveform generation.',
    icon: Compass,
    testId: 'unit-circle-aid',
    component: React.lazy(() => import('./UnitCircleTrigAid')),
    matchKeywords: [
      'trigonomet', 'trig', 'sine', 'cosine', 'tangent', 'reduction',
      'special angle', 'identit', 'wave', 'amplitude', 'periodicity',
      'cartesian', 'quadrant', 'cast', 'astc',
    ],
  },
  aid_trig_3d_elevation: {
    id: 'aid_trig_3d_elevation',
    title: '3D Trigonometry Height & Bearing Unfolder',
    shortTitle: '3D Trig Planes',
    category: 'Mathematics',
    description: '3D vertical tower elevation triangle (ΔQPA) hinged to the oblique horizontal bearing triangle (ΔPAB) with Sine, Cosine, and Area Rule popovers.',
    icon: Compass,
    testId: 'trig-3d-elevation-atlas-aid',
    component: React.lazy(() => import('./Trig3DElevationAtlasAid')),
    matchKeywords: [
      'trigonomet', '2d and 3d', '3d trig', 'angle of elevation',
      'depression', 'sine rule', 'cosine rule', 'area rule', 'bearing',
    ],
  },
  aid_calculus_first_principles: {
    id: 'aid_calculus_first_principles',
    title: '3D Calculus Optimization & Secant-to-Tangent Limit',
    shortTitle: '3D Calculus Lab',
    category: 'Mathematics',
    description: '3D open-top box volume optimization V(x) peaking where V′(x) = 0, plus First Principles secant chord gradient converging as h → 0.',
    icon: TrendingUp,
    testId: 'calculus-first-principles-atlas-aid',
    component: React.lazy(() => import('./CalculusFirstPrinciplesAtlasAid')),
    matchKeywords: [
      'calculus', 'first principles', 'derivative', 'gradient', 'tangent',
      'stationary point', 'optimization', 'maxima', 'minima', 'cubic',
      'differential', 'rate of change',
    ],
  },
  aid_euclidean_circle_theorem: {
    id: 'aid_euclidean_circle_theorem',
    title: '3D-Layered Euclidean Circle Theorem Unfolder',
    shortTitle: '3D Circle Proofs',
    category: 'Mathematics',
    description: 'Explodes overlapping Euclidean circle theorem triangles (isosceles radii OA = OP = OB and tan-chord) into distinct 3D elevation layers.',
    icon: CircleDot,
    testId: 'euclidean-circle-theorem-atlas-aid',
    component: React.lazy(() => import('./EuclideanCircleTheoremAtlasAid')),
    matchKeywords: [
      'euclidean', 'circle geometry', 'tangent', 'chord', 'cyclic quad',
      'angle at centre', 'circumference', 'subtended', 'theorem', 'similarity',
    ],
  },
  aid_polynomial_functions_atlas: {
    id: 'aid_polynomial_functions_atlas',
    title: 'Cartesian Functions & Polynomial Coefficient Lab',
    shortTitle: 'Functions & Coefficients',
    category: 'Mathematics',
    description: 'Dual-capacity Annotated Master Atlas + Live Coefficient Sliders (a, b, c, d / p, q) with real-time drifting roots, turning points, asymptotes, and derivative tangent scrubber.',
    icon: TrendingUp,
    testId: 'polynomial-functions-atlas-aid',
    component: React.lazy(() => import('./PolynomialFunctionsAtlasAid')),
    matchKeywords: [
      'function', 'functions and relationships', 'polynomial', 'parabola',
      'quadratic', 'hyperbola', 'exponential', 'cubic', 'graph', 'intercept',
      'asymptote', 'turning point', 'concavity', 'inflection', 'inverse',
      'algebraic expressions', 'equations and inequalities',
    ],
  },
  aid_number_patterns_growth: {
    id: 'aid_number_patterns_growth',
    title: 'Number Patterns & Quadratic Sequence Growth Explorer',
    shortTitle: 'Patterns & Sequences',
    category: 'Mathematics',
    description: 'Dual-capacity Finite Difference Atlas (Δ₁ & Δ₂ = 2a) + Live Stage Scrubber (n = 1..10) decomposing core vs. growing perimeter and plotting (n; Tₙ).',
    icon: Layers,
    testId: 'number-patterns-growth-atlas-aid',
    component: React.lazy(() => import('./NumberPatternsGrowthAtlasAid')),
    matchKeywords: [
      'pattern', 'number patterns', 'geometric patterns', 'sequence', 'series',
      'quadratic pattern', 'linear pattern', 'constant difference', 'second difference',
      'general term', 'nth term', 'arithmetic', 'sigma',
    ],
  },
  aid_digestive_peristalsis: {
    id: 'aid_digestive_peristalsis',
    title: '3D Digestive Tract Peristalsis, Enzymes & Villus',
    shortTitle: '3D Peristalsis & Villus',
    category: 'Life & Natural Sciences',
    description: '3D cutaway muscular peristalsis wave (with anti-gravity swallow toggle), regional alimentary pH enzyme curves, and 3D intestinal villus lacteal/capillary absorption.',
    icon: Activity,
    testId: 'digestive-peristalsis-atlas-aid',
    component: React.lazy(() => import('./DigestivePeristalsisAtlasAid')),
    matchKeywords: [
      'digestive', 'nutrition', 'alimentary', 'peristalsis', 'oesophagus',
      'stomach', 'small intestine', 'villus', 'villi', 'lacteal',
      'hepatic portal', 'enzyme', 'amylase', 'pepsin', 'lipase', 'bile',
    ],
  },
  aid_human_eye_accommodation: {
    id: 'aid_human_eye_accommodation',
    title: '3D Human Eye Accommodation & Pupillary Reflex',
    shortTitle: '3D Eye Optics',
    category: 'Life Sciences',
    description: '3D ciliary muscle ring contraction, suspensory ligament slackening, and crystalline lens convexity bulging from 6 m to 20 cm, plus iris pupillary reflex.',
    icon: Eye,
    testId: 'human-eye-accommodation-atlas-aid',
    component: React.lazy(() => import('./HumanEyeAccommodationAtlasAid')),
    matchKeywords: [
      'eye', 'accommodation', 'pupillary', 'ciliary', 'suspensory',
      'lens', 'retina', 'cornea', 'iris', 'pupil', 'nervous system',
      'responding to the environment', 'receptor', 'vision',
    ],
  },
  aid_physiology_exchange: {
    id: 'aid_physiology_exchange',
    title: '3D Breathing, Nephron Osmoregulation & Carrying Capacity',
    shortTitle: '3D Breathing & Nephron',
    category: 'Life & Natural Sciences',
    description: '3D thoracic diaphragm Boyle’s Law ventilation, Nephron Loop of Henle counter-current & ADH collecting duct permeability, and logistic carrying capacity K.',
    icon: Wind,
    testId: 'physiology-exchange-atlas-aid',
    component: React.lazy(() => import('./PhysiologyExchangeAtlasAid')),
    matchKeywords: [
      'gaseous exchange', 'breathing', 'ventilation', 'diaphragm', 'alveol',
      'excretion', 'kidney', 'nephron', 'loop of henle', 'osmoregulation',
      'adh', 'homeostasis', 'population ecology', 'carrying capacity', 'logistic',
    ],
  },
  aid_genetics_meiosis: {
    id: 'aid_genetics_meiosis',
    title: '3D Meiosis Chiasmata Crossing-Over & Non-Disjunction',
    shortTitle: '3D Meiosis & Chiasma',
    category: 'Life Sciences',
    description: '3D homologous bivalent crossing-over at chiasmata in Prophase I, Metaphase I random assortment (2²³), and Anaphase I non-disjunction (Trisomy 21).',
    icon: Dna,
    testId: 'genetics-meiosis-atlas-aid',
    component: React.lazy(() => import('./GeneticsMeiosisAtlasAid')),
    matchKeywords: [
      'meiosis', 'chiasma', 'crossing over', 'crossing-over', 'bivalent',
      'homologous', 'non-disjunction', 'trisomy', 'down syndrome',
      'karyotype', 'genetics', 'inheritance', 'gamete', 'cell division',
    ],
  },
  aid_biomolecular_structure: {
    id: 'aid_biomolecular_structure',
    title: 'Biomolecular 3D Structure Viewer',
    shortTitle: 'Biomolecules 3D',
    category: 'Life Sciences & Genetics',
    description: 'Interactive 3D molecular conformations for DNA, RNA, hemoglobin, and enzymes with Mol* sidecar link.',
    icon: Layers,
    testId: 'biomolecular-structure-aid',
    component: React.lazy(() => import('./BiomolecularStructureAid')),
    matchKeywords: [
      'dna', 'rna', 'protein', 'enzyme', 'nucleic', 'meiosis',
      'genetics', 'inheritance', 'code of life', 'cell', 'translation',
      'transcription', 'hemoglobin',
    ],
  },
  aid_organic_chemistry_3d: {
    id: 'aid_organic_chemistry_3d',
    title: '3D Organic Chemistry CPK Explorer',
    shortTitle: 'Organic 3D',
    category: 'Physical Sciences',
    description: 'Interactive 3D molecular models, conformational rotation, chain isomerism, and intermolecular forces.',
    icon: Sparkles,
    testId: 'organic-chem-canvas',
    component: React.lazy(() => import('../modalities/OrganicChemistry3DViewer')),
    matchKeywords: [
      'organic', 'alkane', 'alkene', 'alkyne', 'alcohol', 'aldehyde',
      'ketone', 'carboxylic', 'ester', 'isomer', 'iupac', 'intermolecular',
      'homologous',
    ],
  },
  aid_electrodynamics_motor: {
    id: 'aid_electrodynamics_motor',
    title: 'Electrodynamics Armature & Oscilloscope',
    shortTitle: '3D Motor & AC/DC',
    category: 'Physical Sciences',
    description: '3D rotating armature simulation, magnetic flux linkage, and AC/DC induced EMF oscilloscope trace.',
    icon: Activity,
    testId: 'electrodynamics-canvas',
    component: React.lazy(() => import('../modalities/ElectrodynamicsMotorViewer')),
    matchKeywords: [
      'electrodynamics', 'generator', 'motor', 'armature', 'faraday',
      'induction', 'alternating current', 'slip ring', 'split ring',
      'dynamo', 'electromagnetic',
    ],
  },
  aid_geometric_nets_3d: {
    id: 'aid_geometric_nets_3d',
    title: '3D Geometric Nets Polyhedron Folding',
    shortTitle: '3D Nets',
    category: 'Mathematics',
    description: 'Interactive polyhedral net folding simulations, face/vertex/edge counts, and Euler’s polyhedron formula.',
    icon: Box,
    testId: 'geometric-nets-canvas',
    component: React.lazy(() => import('../modalities/GeometricNets3DViewer')),
    matchKeywords: [
      'geometric_nets', 'net', 'polyhed', 'cube', 'prism', 'pyramid',
      'euler', '3d objects', 'surface area', 'faces vertices edges', 'measurement',
    ],
  },
  aid_cardiovascular_atlas: {
    id: 'aid_cardiovascular_atlas',
    title: 'Human Heart & Cardiac Cycle Reference Atlas',
    shortTitle: 'Heart Atlas',
    category: 'Life & Natural Sciences',
    description: 'Interactive reference comparing 3D coronal cross-section, directional blood flow schematic, 2D examination line-art, and 3-phase cardiac cycle states.',
    icon: Activity,
    testId: 'cardiovascular-atlas-aid',
    component: React.lazy(() => import('./CardiovascularAtlasAid')),
    matchKeywords: [
      'circulatory', 'respiratory', 'transport systems in animals',
      'transport systems in mammals', 'heart', 'cardiac cycle', 'blood vessel',
    ],
  },
  aid_geometry_2d_circle: {
    id: 'aid_geometry_2d_circle',
    title: '2D Geometry & Circle Parts Explorer',
    shortTitle: 'Circle & 2D Parts',
    category: 'Mathematics',
    description: 'Interactive radius, diameter, chord, arc, and sector explorer for Geometry of 2D Shapes.',
    icon: CircleDot,
    testId: 'geometry-2d-circle-aid',
    component: React.lazy(() => import('./Grade7InteractiveAids').then((m) => ({ default: m.Geometry2DCircleExplorerAid }))),
    matchKeywords: [
      'geometry of 2d', '2d shapes', 'circle', 'radius', 'diameter', 'chord', 'arc', 'sector', 'straight lines',
    ],
  },
  aid_integer_number_line: {
    id: 'aid_integer_number_line',
    title: 'Integer Number Line Hopper',
    shortTitle: 'Integer Number Line',
    category: 'Mathematics',
    description: 'Interactive number line showing directional hops for adding and subtracting positive and negative integers.',
    icon: TrendingUp,
    testId: 'integer-number-line-aid',
    component: React.lazy(() => import('./Grade7InteractiveAids').then((m) => ({ default: m.IntegerNumberLineHopperAid }))),
    matchKeywords: [
      'integers', 'integer', 'negative', 'number line', 'additive inverse',
    ],
  },
  aid_acid_base_litmus: {
    id: 'aid_acid_base_litmus',
    title: 'Litmus Paper & Acid-Base Indicator Lab',
    shortTitle: 'Litmus & pH Lab',
    category: 'Chemistry & Matter',
    description: 'Interactive red and blue litmus paper dip test across household acids, bases, and neutrals.',
    icon: FlaskConical,
    testId: 'acid-base-litmus-aid',
    component: React.lazy(() => import('./Grade7InteractiveAids').then((m) => ({ default: m.AcidBaseLitmusSimulatorAid }))),
    matchKeywords: [
      'acids, bases and neutrals', 'acid', 'base', 'litmus', 'indicator', 'neutral',
    ],
  },
  aid_heat_transfer_thermos: {
    id: 'aid_heat_transfer_thermos',
    title: 'Heat Transfer & Vacuum Flask Simulator',
    shortTitle: 'Heat & Thermos Lab',
    category: 'Physical & Natural Sciences',
    description: 'Interactive conduction, convection, radiation, and vacuum flask (Thermos) insulation cutaway.',
    icon: Flame,
    testId: 'heat-transfer-thermos-aid',
    component: React.lazy(() => import('./Grade7InteractiveAids').then((m) => ({ default: m.HeatTransferThermosSimulatorAid }))),
    matchKeywords: [
      'heat transfer', 'insulation', 'conduction', 'convection', 'radiation', 'thermos', 'vacuum flask', 'energy saving',
    ],
  },
  aid_earth_seasons_tides: {
    id: 'aid_earth_seasons_tides',
    title: 'Earth 23,5° Axial Tilt, Seasons & Tides Simulator',
    shortTitle: 'Seasons & Tides',
    category: 'Planet Earth & Beyond',
    description: 'Interactive Southern vs Northern Hemisphere solstice tilt, equinoxes, and Spring/Neap tides.',
    icon: Compass,
    testId: 'earth-seasons-tides-aid',
    component: React.lazy(() => import('./Grade7InteractiveAids').then((m) => ({ default: m.EarthMoonSunSeasonsTidesAid }))),
    matchKeywords: [
      'relationship of the sun', 'relationship of the moon', 'seasons', 'tides', 'axial tilt', 'solstice', 'equinox', 'gravity',
    ],
  },
  aid_mathlit_maps_and_plans: {
    id: 'aid_mathlit_maps_and_plans',
    title: 'Mathematical Literacy: Maps, Scale & Floor Plans Atlas',
    shortTitle: 'Maps & Floor Plans',
    category: 'Mathematical Literacy',
    description: 'Exploratory visual companion for bar scales, compass bearings, strip maps, elevation views, and architectural floor plans.',
    icon: Compass,
    testId: 'mathlit-maps-plans-aid',
    component: React.lazy(() => import('./MathLitAtlasAid')),
    matchKeywords: [
      'map', 'scale', 'plan', 'floor', 'elevation', 'bearing', 'compass',
      'distance', 'direction', 'route', 'strip', 'grid', 'seating', 'assembly',
      'scale maps and plans', 'maps and plans', 'plans and scale',
    ],
  },
  aid_mathlit_tariffs_and_taxation: {
    id: 'aid_mathlit_tariffs_and_taxation',
    title: 'Mathematical Literacy: Tariffs, Finance & Taxation Companion',
    shortTitle: 'Tariffs & Tax Curves',
    category: 'Mathematical Literacy',
    description: 'Interactive stepped municipal water/electricity blocks, SARS personal income tax brackets, UIF salary ceiling cap, and break-even cost analysis.',
    icon: TrendingUp,
    testId: 'mathlit-tariffs-taxation-aid',
    component: React.lazy(() => import('./MathLitAtlasAid')),
    matchKeywords: [
      'tariff', 'tax', 'taxation', 'income tax', 'uif', 'finance', 'budget',
      'banking', 'interest', 'inflation', 'break-even', 'cost', 'income',
      'step tariff', 'water', 'electricity', 'rates', 'fees',
    ],
  },
  aid_mathlit_measurement_and_packaging: {
    id: 'aid_mathlit_measurement_and_packaging',
    title: 'Mathematical Literacy: Measurement, Nets & Packaging Atlas',
    shortTitle: 'Measurement & Packaging',
    category: 'Mathematical Literacy',
    description: 'Visual 3D carton packing arrays, perimeter and area tile formulas, volume/capacity liquid conversions, and folding 2D packaging nets.',
    icon: Box,
    testId: 'mathlit-measurement-packaging-aid',
    component: React.lazy(() => import('./MathLitAtlasAid')),
    matchKeywords: [
      'packaging', 'carton', 'box', 'packing', 'measurement', 'perimeter',
      'area', 'volume', 'capacity', 'net', 'cylinder', 'prism', 'conversion',
      'weight', 'temperature', 'bmi', 'medicine', 'dosage', 'lengths',
    ],
  },
  aid_commerce_and_accounting: {
    id: 'aid_commerce_and_accounting',
    title: 'Commerce & Financial Accounting Atlas',
    shortTitle: 'Accounting & Business Atlas',
    category: 'Commerce & Accounting',
    description: 'Interactive Accounting Equation (A = OE + L), Ledger T-Accounts Architecture (DEAD CLIC), South African VAT 15% calculator, Break-Even & Cost-Volume-Profit live model, and 8-step Accounting Cycle.',
    icon: Landmark,
    testId: 'commerce-accounting-atlas-aid',
    component: React.lazy(() => import('./CommerceAndAccountingAtlasAid')),
    matchKeywords: [
      'accounting', 'ledger', 'journal', 'trial balance', 'balance sheet',
      'income statement', 'financial statement', 'asset', 'liability', "owner's equity",
      'vat', 'cost of sales', 'debtor', 'creditor', 'cash receipts', 'cash payments',
      'petty cash', 'depreciation', 'bank reconciliation', 'manufacturing', 'budget',
      'break-even', 'business environment', 'pestle', 'circular flow', 'factors of production',
      'ems', 'business studies',
    ],
  },
};

/**
 * Determines which visual aids are relevant for the current workspace context.
 *
 * @param {string} subject - Subject identifier or display name
 * @param {string} topic - Topic name
 * @param {string} modality - Question modality string
 * @param {object} question - Full question payload
 * @returns {Array<object>} Array of matching visual aid descriptor objects
 */
export function getAvailableVisualAids(subject = '', topic = '', modality = '', question = null) {
  const normTopic = String(topic || '').toLowerCase();
  const normSubject = String(subject || '').toLowerCase();
  const normModality = String(modality || question?.modality || '').toLowerCase();
  const results = [];

  // 1. Direct Question Modality Mappings
  if (normModality === 'geometric_nets') {
    results.push(VISUAL_AIDS.aid_geometric_nets_3d);
  }
  if (normModality === 'electrodynamics') {
    results.push(VISUAL_AIDS.aid_electrodynamics_motor);
  }
  if (normModality === 'organic_chemistry') {
    results.push(VISUAL_AIDS.aid_organic_chemistry_3d);
    results.push(VISUAL_AIDS.aid_periodic_table);
  }

  // 1b. Mathematical Literacy Dedicated Priority Grounding
  if (normSubject.includes('mathematical_literacy')) {
    if (
      normTopic.includes('map') ||
      normTopic.includes('plan') ||
      normTopic.includes('scale') ||
      normTopic.includes('assembly') ||
      normTopic.includes('model')
    ) {
      results.push(VISUAL_AIDS.aid_mathlit_maps_and_plans);
    }
    if (
      normTopic.includes('tariff') ||
      normTopic.includes('tax') ||
      normTopic.includes('finance') ||
      normTopic.includes('budget') ||
      normTopic.includes('bank') ||
      normTopic.includes('income') ||
      normTopic.includes('interest') ||
      normTopic.includes('exchange') ||
      normTopic.includes('pattern')
    ) {
      results.push(VISUAL_AIDS.aid_mathlit_tariffs_and_taxation);
    }
    if (
      normTopic.includes('pack') ||
      normTopic.includes('measur') ||
      normTopic.includes('perim') ||
      normTopic.includes('area') ||
      normTopic.includes('volum') ||
      normTopic.includes('weight') ||
      normTopic.includes('convers') ||
      normTopic.includes('length')
    ) {
      results.push(VISUAL_AIDS.aid_mathlit_measurement_and_packaging);
    }
    // Default dedicated fallback for Data handling / Probability / General
    if (results.length === 0) {
      results.push(VISUAL_AIDS.aid_mathlit_tariffs_and_taxation);
      results.push(VISUAL_AIDS.aid_mathlit_maps_and_plans);
    }
  }

  // 2. Keyword Topic Grounding
  Object.values(VISUAL_AIDS).forEach((aid) => {
    if (results.some((r) => r.id === aid.id)) return;

    const matchesKeyword = aid.matchKeywords.some((kw) =>
      normTopic.includes(kw) || normModality.includes(kw)
    );

    if (matchesKeyword) {
      results.push(aid);
    }
  });

  // 3. Subject-Level Contextual Fallbacks (Ensure rich 3D sidecars are always accessible)
  if (normSubject.includes('mathematical_literacy')) {
    [
      VISUAL_AIDS.aid_mathlit_maps_and_plans,
      VISUAL_AIDS.aid_mathlit_tariffs_and_taxation,
      VISUAL_AIDS.aid_mathlit_measurement_and_packaging,
    ].forEach((aid) => {
      if (aid && !results.some((r) => r.id === aid.id)) results.push(aid);
    });
  } else if (normSubject.includes('physical_sciences') || normSubject.includes('natural_sciences')) {
    [
      VISUAL_AIDS.aid_circuit_potential_atlas,
      VISUAL_AIDS.aid_newton_mechanics_atlas,
      VISUAL_AIDS.aid_atomic_bonding_lattice,
      VISUAL_AIDS.aid_kinetic_matter_states,
      VISUAL_AIDS.aid_periodic_table,
    ].forEach((aid) => {
      if (!results.some((r) => r.id === aid.id)) results.push(aid);
    });
  } else if (normSubject.includes('mathematics') || normSubject.includes('technical_mathematics')) {
    [
      VISUAL_AIDS.aid_polynomial_functions_atlas,
      VISUAL_AIDS.aid_number_patterns_growth,
      VISUAL_AIDS.aid_geometric_nets_3d,
      VISUAL_AIDS.aid_trig_3d_elevation,
      VISUAL_AIDS.aid_calculus_first_principles,
      VISUAL_AIDS.aid_euclidean_circle_theorem,
      VISUAL_AIDS.aid_unit_circle_trig,
    ].forEach((aid) => {
      if (!results.some((r) => r.id === aid.id)) results.push(aid);
    });
  } else if (normSubject.includes('life_sciences')) {
    [
      VISUAL_AIDS.aid_digestive_peristalsis,
      VISUAL_AIDS.aid_human_eye_accommodation,
      VISUAL_AIDS.aid_physiology_exchange,
      VISUAL_AIDS.aid_genetics_meiosis,
      VISUAL_AIDS.aid_biomolecular_structure,
      VISUAL_AIDS.aid_cardiovascular_atlas,
    ].forEach((aid) => {
      if (!results.some((r) => r.id === aid.id)) results.push(aid);
    });
  } else if (
    normSubject.includes('accounting') ||
    normSubject.includes('economic') ||
    normSubject.includes('ems') ||
    normSubject.includes('business')
  ) {
    [VISUAL_AIDS.aid_commerce_and_accounting].forEach((aid) => {
      if (aid && !results.some((r) => r.id === aid.id)) results.push(aid);
    });
  }

  return results;
}
