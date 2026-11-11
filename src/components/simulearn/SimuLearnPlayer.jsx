import React, { useState, useEffect, useRef } from 'react';
import KaTeXRenderer from '../shared/KaTeXRenderer';
import DiagramRenderer from '../workspace/shared/mathx/DiagramRenderer';
import HumanHeartSvg from '../workspace/modalities/diagram_bank/HumanHeartSvg';
import AlveolusGasExchangeSvg from '../workspace/modalities/diagram_bank/AlveolusGasExchangeSvg';
import ParticleModelSvg from '../workspace/modalities/diagram_bank/ParticleModelSvg';
import GeyserHeatingElementSvg from '../workspace/modalities/diagram_bank/GeyserHeatingElementSvg';
import OpticalTelescopesSvg from '../workspace/modalities/diagram_bank/OpticalTelescopesSvg';

// Pre-packaged canonical scripts for instantaneous zero-latency offline playback
const DEFAULT_SCRIPTS = {
  alveolus_gas_exchange: {
    archetype: 'gas_exchange_alveolus_sync',
    title: 'Alveolar Gaseous Exchange: Ventilation, Perfusion & Diffusion Across 0,5 µm Membrane',
    subject: 'Life Sciences',
    grade: 11,
    grid_type: 'diagram_process',
    diagram_type: 'alveolus_gas_exchange',
    frames: [
      {
        time_ms: 0,
        action: 'set_state',
        state: 'ventilation',
        phase: 'ventilation',
        sound: null,
        ecg_segment: 'Inspiratory Phase',
        latex: 'P_{\\text{alveolar}} = 104\\text{ mmHg } (\\text{O}_2) \\quad P_{\\text{alveolar}} = 40\\text{ mmHg } (\\text{CO}_2)',
        narrative: 'Phase 1: Inhalation (Ventilation). Contraction of the diaphragm and external intercostals expands thoracic volume, pulling fresh air into the alveolar lumen. Alveolar pO2 is 104 mmHg and pCO2 is 40 mmHg.',
      },
      {
        time_ms: 3500,
        action: 'set_state',
        state: 'perfusion',
        phase: 'perfusion',
        sound: null,
        ecg_segment: 'Pulmonary Arteriole Inflow',
        latex: 'P_{\\text{venous}} = 40\\text{ mmHg } (\\text{O}_2) \\quad P_{\\text{venous}} = 45\\text{ mmHg } (\\text{CO}_2)',
        narrative: 'Phase 2: Perfusion. Deoxygenated blood pumped from the right ventricle arrives via the pulmonary artery. Inflow capillary blood has low pO2 (40 mmHg) and high pCO2 (45 mmHg). Erythrocytes flow in single file.',
      },
      {
        time_ms: 7500,
        action: 'set_state',
        state: 'diffusion',
        phase: 'diffusion',
        sound: null,
        ecg_segment: 'Trans-Membrane Gas Exchange',
        latex: '\\Delta P_{\\text{O}_2} = 104 - 40 = 64\\text{ mmHg} \\quad \\Delta P_{\\text{CO}_2} = 45 - 40 = 5\\text{ mmHg}',
        narrative: 'Phase 3: Passive Diffusion. A steep partial pressure gradient of 64 mmHg drives oxygen across the ultra-thin 0,5 µm respiratory membrane into the RBCs, binding to hemoglobin to form oxyhemoglobin. Carbon dioxide diffuses down its gradient (5 mmHg) into the alveolar lumen.',
      },
      {
        time_ms: 12000,
        action: 'set_state',
        state: 'oxygenation',
        phase: 'oxygenation',
        sound: null,
        ecg_segment: 'Pulmonary Venule Outflow',
        latex: '\\text{Hb-O}_2 \\text{ Saturation} = 98\\% \\quad P_{\\text{arterial}} = 100\\text{ mmHg}',
        narrative: 'Phase 4: Oxygenated Outflow & Exhalation. Blood leaving the pulmonary capillary is fully oxygenated (98% Hb-O2, pO2 100 mmHg), returning via the four pulmonary veins to the left atrium of the heart for systemic distribution. CO2 is exhaled.',
      },
    ],
  },
  particle_model_matter: {
    archetype: 'particle_model_states_and_phase_changes',
    title: 'Kinetic Particle Model: Solid Lattice, Latent Heat & Phase Transitions',
    subject: 'Natural Sciences',
    grade: 8,
    grid_type: 'diagram_process',
    diagram_type: 'particle_model',
    frames: [
      {
        time_ms: 0,
        action: 'set_state',
        state: 'solid',
        phase: 'solid',
        sound: null,
        ecg_segment: 'Crystalline Solid (< 0 °C)',
        latex: 'T < 0^\\circ\\text{C} \\quad \\bar{E}_k \\propto T \\quad \\text{Strong Intermolecular Lattice Forces}',
        narrative: 'Phase 1: Solid State. Particles are closely packed in a regular geometric crystal lattice. Particles cannot change positions; they vibrate continuously about fixed equilibrium points. Strong intermolecular forces maintain fixed shape and fixed volume.',
      },
      {
        time_ms: 3500,
        action: 'set_state',
        state: 'melting',
        phase: 'melting',
        sound: null,
        ecg_segment: 'Melting Plateau (0 °C Latent Heat)',
        latex: 'T = 0^\\circ\\text{C} \\quad Q = m L_f \\quad \\Delta T = 0',
        narrative: 'Phase 2: Melting (Latent Heat of Fusion). At 0 °C, thermal energy added does NOT increase temperature. Instead, latent heat breaks the rigid intermolecular lattice bonds, allowing particles to slip out of their fixed positions into a fluid liquid.',
      },
      {
        time_ms: 7500,
        action: 'set_state',
        state: 'liquid',
        phase: 'liquid',
        sound: null,
        ecg_segment: 'Liquid State (0 °C to 100 °C)',
        latex: '0^\\circ\\text{C} < T < 100^\\circ\\text{C} \\quad \\text{Fluid Close Packing (Rolling Motion)}',
        narrative: 'Phase 3: Liquid State. Particles remain in close contact but possess sufficient kinetic energy to roll and slide past each other randomly. Liquids have a fixed volume but take the shape of their container.',
      },
      {
        time_ms: 12000,
        action: 'set_state',
        state: 'boiling',
        phase: 'boiling',
        sound: null,
        ecg_segment: 'Boiling Plateau (100 °C Latent Heat)',
        latex: 'T = 100^\\circ\\text{C} \\quad Q = m L_v \\quad \\Delta T = 0',
        narrative: 'Phase 4: Boiling (Latent Heat of Vaporisation). At 100 °C, added heat is absorbed to completely overcome all remaining intermolecular attractive forces. Particles break free from the liquid surface into rapid vapor particles.',
      },
      {
        time_ms: 16500,
        action: 'set_state',
        state: 'gas',
        phase: 'gas',
        sound: null,
        ecg_segment: 'Gas State (> 100 °C)',
        latex: 'T > 100^\\circ\\text{C} \\quad p V = n R T \\quad \\text{Elastic High-Velocity Collisions}',
        narrative: 'Phase 5: Gas State. Particles are widely separated with negligible intermolecular forces. They move rapidly in straight lines, colliding elastically with each other and container walls to exert gas pressure.',
      },
    ],
  },
  geyser_heating_element: {
    archetype: 'geyser_heating_element_heat_transfer',
    title: 'Domestic Geyser: Electrical Resistance Heating, Convection & Thermostat Cut-Off',
    subject: 'Natural Sciences',
    grade: 8,
    grid_type: 'diagram_process',
    diagram_type: 'geyser_heating_element',
    frames: [
      {
        time_ms: 0,
        action: 'set_state',
        state: 'heating',
        phase: 'heating',
        sound: null,
        ecg_segment: 'Joule Heating (P = I²R)',
        latex: 'P = I^2 R = (13,0\\text{ A})^2 \\times 17,6\\,\\Omega = 3000\\text{ W } (3,0\\text{ kW})',
        narrative: 'Phase 1: Electrical Resistance Heating. 230 V mains electricity flows through the submerged coiled nichrome/copper element at the base of the tank. Electrical energy is converted directly into thermal energy via Joule heating.',
      },
      {
        time_ms: 4000,
        action: 'set_state',
        state: 'convection',
        phase: 'convection',
        sound: null,
        ecg_segment: 'Thermal Convection Currents',
        latex: '\\rho_{\\text{hot}} < \\rho_{\\text{cold}} \\quad \\text{Buoyancy Force Drives Circulation}',
        narrative: 'Phase 2: Thermal Convection Circulation. Heated water expands and becomes less dense than cold water. The warm water rises along the central axis of the cylinder, while denser cooler water sinks along the insulated outer walls to be heated at the bottom.',
      },
      {
        time_ms: 8500,
        action: 'set_state',
        state: 'stratification',
        phase: 'stratification',
        sound: null,
        ecg_segment: 'Thermal Stratification',
        latex: 'T_{\\text{top}} = 65^\\circ\\text{C} \\quad T_{\\text{bottom}} = 25^\\circ\\text{C}',
        narrative: 'Phase 3: Thermal Stratification. The long vertical cold water dip tube delivers replacement municipal water directly to the bottom. Less dense hot water accumulates at the top, where the outlet pipe draws it for household use without mixing with incoming cold water.',
      },
      {
        time_ms: 13000,
        action: 'set_state',
        state: 'cut_off',
        phase: 'cut_off',
        sound: null,
        ecg_segment: 'Thermostat Safety Cut-Off',
        latex: 'T \\ge T_{\\text{setpoint}} (65^\\circ\\text{C}) \\implies \\text{Bimetallic Strip Bends } \\implies I = 0\\text{ A}',
        narrative: 'Phase 4: Thermostat Safety Cut-Off. As water reaches 65 °C, differential thermal expansion causes the bimetallic strip in the thermostat probe to bend away from the contact points, breaking the circuit and cutting power to the heating element.',
      },
    ],
  },
  optical_telescopes: {
    archetype: 'optical_telescopes_salt_vs_refractor',
    title: 'Astronomical Optical Telescopes: Newtonian/SALT Reflection vs Keplerian Refraction',
    subject: 'Natural Sciences',
    grade: 8,
    grid_type: 'diagram_process',
    diagram_type: 'optical_telescopes',
    frames: [
      {
        time_ms: 0,
        action: 'set_state',
        state: 'starlight_inflow',
        phase: 'starlight_inflow',
        sound: null,
        ecg_segment: 'Incident Parallel Starlight',
        latex: '\\text{Aperture } D = 11\\text{ m (SALT)} \\quad \\text{Light Gathering Power } \\propto D^2',
        narrative: 'Phase 1: Light Gathering Power. Distant astronomical objects emit parallel light waves. The light gathering power of a telescope depends on the surface area of its objective aperture (proportional to diameter squared).',
      },
      {
        time_ms: 4000,
        action: 'set_state',
        state: 'reflection',
        phase: 'reflection',
        sound: null,
        ecg_segment: 'Primary Mirror Reflection (Zero Chromatic Defect)',
        latex: '\\theta_r = \\theta_i \\quad \\text{Zero Chromatic Aberration in Curved Mirrors}',
        narrative: 'Phase 2: Newtonian Reflection (SALT Standard). In a reflecting telescope, parallel starlight reflects off the concave primary mirror. Because the law of reflection (angle of incidence equals angle of reflection) is independent of wavelength, mirrors reflect all colors to the exact same focus with zero chromatic aberration.',
      },
      {
        time_ms: 8500,
        action: 'set_state',
        state: 'refraction',
        phase: 'refraction',
        sound: null,
        ecg_segment: 'Convex Objective Lens Refraction',
        latex: 'M = \\frac{f_o}{f_e} = \\frac{800\\text{ mm}}{20\\text{ mm}} = 40\\times',
        narrative: 'Phase 3: Keplerian Refraction. In a refracting telescope, light passes through a glass convex objective lens. The light rays bend (refract) and converge to form a real inverted intermediate image at the principal focus F.',
      },
      {
        time_ms: 13000,
        action: 'set_state',
        state: 'dispersion',
        phase: 'dispersion',
        sound: null,
        ecg_segment: 'Chromatic Aberration in Lenses',
        latex: 'n_{\\text{blue}} > n_{\\text{red}} \\implies f_{\\text{blue}} < f_{\\text{red}} \\quad (\\text{Color Fringing Defect})',
        narrative: 'Phase 4: Chromatic Aberration Limitation. Glass has a higher refractive index for short wavelengths (blue light) than long wavelengths (red light). Consequently, blue light refracts more steeply and focuses closer to the lens than red light, creating blurred color fringes around celestial objects. This is why the world’s largest astronomical observatories (like SALT in Sutherland) are reflecting telescopes!',
      },
    ],
  },
  cardiac_cycle: {
    archetype: 'cardiac_cycle_sync',
    title: 'The Human Cardiac Cycle: Atrial Systole, Ventricular Systole & Diastole',
    subject: 'Life Sciences',
    grade: 10,
    grid_type: 'diagram_process',
    diagram_type: 'human_heart',
    frames: [
      {
        time_ms: 0,
        action: 'set_state',
        state: 'atrial_systole',
        sound: null,
        ecg_segment: 'P wave to PR interval',
        narrative: 'Phase 1: Atrial Systole (0,1 s). The SA node fires; both atria contract simultaneously, forcing blood through the open tricuspid and bicuspid (mitral) valves into the relaxed ventricles.',
      },
      {
        time_ms: 3500,
        action: 'set_state',
        state: 'ventricular_systole',
        sound: 'lubb',
        ecg_segment: 'QRS complex to ST segment',
        narrative: 'Phase 2: Ventricular Systole (0,3 s). Ventricles contract forcefully. High pressure snaps the atrioventricular valves shut (first heart sound: "lubb"). The aortic and pulmonary semi-lunar valves open, pumping blood into the aorta and pulmonary artery.',
      },
      {
        time_ms: 7500,
        action: 'set_state',
        state: 'general_diastole',
        sound: 'dubb',
        ecg_segment: 'T wave to TP segment',
        narrative: 'Phase 3: General Diastole (0,4 s). Both atria and ventricles relax. Falling ventricular pressure causes blood to recoil against the semi-lunar valves, snapping them shut (second heart sound: "dubb"). Blood flows passively into atria.',
      },
    ],
  },
  accounting_crj_vat: {
    archetype: 'crj_vat_split',
    title: 'Recording Cash Sales with 15% VAT in the CRJ',
    subject: 'Accounting',
    grid_type: 'journal_table',
    headers: ['Day', 'Details', 'Bank (Gross)', 'Sales (Excl)', 'Output VAT (15%)', 'Cost of Sales'],
    frames: [
      {
        time_ms: 0,
        action: 'highlight_prompt',
        narrative: 'Transaction: Sold merchandise for R1,150 cash. Cost of sales is R800. (VAT rate is 15%).'
      },
      {
        time_ms: 2000,
        action: 'type_cell',
        cell_id: 'r0_c0',
        value: '12',
        label: 'Day',
        narrative: 'Record the day (12) in the Day column.'
      },
      {
        time_ms: 4000,
        action: 'type_cell',
        cell_id: 'r0_c1',
        value: 'Cash',
        label: 'Details',
        narrative: "Details is 'Cash' (or CRT for cash register tape)."
      },
      {
        time_ms: 6000,
        action: 'type_cell',
        cell_id: 'r0_c2',
        value: '1150.00',
        label: 'Bank Gross',
        narrative: 'Bank always receives the full gross cash amount: R1,150.00.'
      },
      {
        time_ms: 8500,
        action: 'formula_callout',
        latex: '\\text{Sales (Excl)} = 1150 \\times \\frac{100}{115} = 1000.00',
        narrative: 'Extract VAT: Divide gross by 1.15 to find net Sales of R1,000.00.'
      },
      {
        time_ms: 10500,
        action: 'type_cell',
        cell_id: 'r0_c3',
        value: '1000.00',
        label: 'Sales Excl',
        narrative: 'Record R1,000.00 in Sales and R150.00 in Output VAT.'
      }
    ]
  },
  math_quadratic_trinomial: {
    archetype: 'quadratic_factorisation',
    title: 'Factorising a Quadratic Trinomial: x² + 5x + 6',
    subject: 'Mathematics',
    grid_type: 'stepwise_math',
    frames: [
      {
        time_ms: 0,
        action: 'show_expression',
        latex: 'x^2 + 5x + 6',
        narrative: 'Goal: Factorise the trinomial into two binomial brackets (x + a)(x + b).'
      },
      {
        time_ms: 2500,
        action: 'formula_callout',
        latex: '\\text{Find } a, b \\text{ where } a \\cdot b = 6 \\text{ and } a + b = 5',
        narrative: 'Step 1: Look for factors of the constant term (+6) that sum to the middle coefficient (+5).'
      },
      {
        time_ms: 5500,
        action: 'show_step',
        latex: '2 \\times 3 = 6 \\quad \\text{and} \\quad 2 + 3 = 5',
        narrative: 'Step 2: The factor pair is +2 and +3.'
      },
      {
        time_ms: 8500,
        action: 'final_solution',
        latex: '(x + 2)(x + 3)',
        narrative: 'Step 3: Write the factorised form: (x + 2)(x + 3).'
      }
    ]
  },
  physics_kinematics_dx: {
    archetype: 'kinematics_1d',
    title: 'Kinematics: Displacement Equation Δx = v_i Δt + ½ a Δt²',
    subject: 'Physical Sciences',
    grid_type: 'stepwise_math',
    frames: [
      {
        time_ms: 0,
        action: 'list_knowns',
        latex: 'v_i = 10\\text{ m/s}, \\quad a = 2\\text{ m/s}^2, \\quad \\Delta t = 4\\text{ s}',
        narrative: 'Step 1: Write down all given variables.'
      },
      {
        time_ms: 3000,
        action: 'show_formula',
        latex: '\\Delta x = v_i \\Delta t + \\frac{1}{2} a \\Delta t^2',
        narrative: 'Step 2: Choose the equation of motion containing vi, a, and Δt.'
      },
      {
        time_ms: 6500,
        action: 'substitute_values',
        latex: '\\Delta x = (10)(4) + \\frac{1}{2}(2)(4)^2 = 40 + 16',
        narrative: 'Step 3: Substitute knowns. Remember to square the time first (4² = 16).'
      },
      {
        time_ms: 9500,
        action: 'final_solution',
        latex: '\\Delta x = 56\\text{ m}',
        narrative: 'Step 4: Compute final displacement: 56 metres.'
      }
    ]
  },
  lifesciences_punnett_square: {
    archetype: 'monohybrid_cross',
    title: 'Monohybrid Cross: Heterozygous Parents (Bb × Bb)',
    subject: 'Life Sciences',
    grid_type: 'punnett_grid',
    headers: ['Gametes', 'B', 'b'],
    frames: [
      {
        time_ms: 0,
        action: 'highlight_prompt',
        latex: '\\text{Parents: } Bb \\times Bb \\quad (\\text{Brown dominant to blue})',
        narrative: 'Parental genotypes: Both parents are heterozygous (Bb).'
      },
      {
        time_ms: 2500,
        action: 'type_cell',
        cell_id: 'r0_c0',
        value: 'BB',
        label: 'Square 1: B from Mother, B from Father',
        narrative: 'Square 1: Homozygous Dominant (BB) - Brown phenotype.'
      },
      {
        time_ms: 5000,
        action: 'type_cell',
        cell_id: 'r0_c1',
        value: 'Bb',
        label: 'Square 2: B from Mother, b from Father',
        narrative: 'Square 2: Heterozygous (Bb) - Brown phenotype.'
      },
      {
        time_ms: 7500,
        action: 'type_cell',
        cell_id: 'r1_c0',
        value: 'Bb',
        label: 'Square 3: b from Mother, B from Father',
        narrative: 'Square 3: Heterozygous (Bb) - Brown phenotype.'
      },
      {
        time_ms: 9500,
        action: 'type_cell',
        cell_id: 'r1_c1',
        value: 'bb',
        label: 'Square 4: b from Mother, b from Father',
        narrative: 'Square 4: Homozygous Recessive (bb) - Blue phenotype.'
      },
      {
        time_ms: 11000,
        action: 'final_solution',
        latex: '\\text{Ratio: } 3\\text{ Brown} : 1\\text{ Blue} \\quad (75\\% : 25\\%)',
        narrative: 'Summary: 3 : 1 phenotypic ratio (75% probability of dominant trait).'
      }
    ]
  }
};

export function buildDynamicSimuLearnScript(question, fallbackSubject = 'Mathematics', fallbackGrade = 7, fallbackTopic = '') {
  if (!question || typeof question !== 'object') return null;

  const subject = question.subject || fallbackSubject || 'Mathematics';
  const grade = question.grade || fallbackGrade || 7;
  const topic = question.topic || fallbackTopic || question.archetype || 'Worked Example';
  const arch = String(question.archetype || question.subskill || topic || '').toLowerCase();
  const promptText = String(question.question_text || question.prompt || question.question || '').replace(/\$\$?/g, '');

  // Special interactive visual replay 1: Stem-and-Leaf Plot (Maths #23)
  if (arch.includes('stem') && arch.includes('leaf')) {
    return {
      archetype: 'stem_and_leaf_dynamic',
      title: `SimuLearn Walkthrough • Constructing & Reading a Stem-and-Leaf Plot`,
      subject,
      grade,
      grid_type: 'stem_and_leaf_visual',
      frames: [
        {
          time_ms: 0,
          action: 'show_data',
          raw_numbers: [12, 15, 18, 21, 24, 24, 29, 32, 37],
          active_num: null,
          stems: { '1': [], '2': [], '3': [] },
          narrative: 'Step 1: Order the raw data from smallest to largest: 12, 15, 18, 21, 24, 24, 29, 32, 37. Each 2-digit number splits into a Stem (tens digit) and a Leaf (units digit).'
        },
        {
          time_ms: 2800,
          action: 'slot_stem',
          raw_numbers: [12, 15, 18, 21, 24, 24, 29, 32, 37],
          active_num: '12, 15, 18 → Stem 1 | Leaves 2  5  8',
          stems: { '1': [2, 5, 8], '2': [], '3': [] },
          narrative: 'Step 2: Group the 10s (12, 15, 18). Write "1" in the Stem column and slot the unit digits (2, 5, 8) in ascending order in the Leaf column.'
        },
        {
          time_ms: 5600,
          action: 'slot_stem',
          raw_numbers: [12, 15, 18, 21, 24, 24, 29, 32, 37],
          active_num: '21, 24, 24, 29 → Stem 2 | Leaves 1  4  4  9',
          stems: { '1': [2, 5, 8], '2': [1, 4, 4, 9], '3': [] },
          narrative: 'Step 3: Group the 20s (21, 24, 24, 29). Repeated values like 24 appear twice in the leaf row (1, 4, 4, 9) — this shows the mode!'
        },
        {
          time_ms: 8400,
          action: 'slot_stem',
          raw_numbers: [12, 15, 18, 21, 24, 24, 29, 32, 37],
          active_num: '32, 37 → Stem 3 | Leaves 2  7   (Key: 2 | 4 = 24)',
          stems: { '1': [2, 5, 8], '2': [1, 4, 4, 9], '3': [2, 7] },
          narrative: 'Step 4: Group the 30s (32, 37) under Stem 3. Always include the Key (e.g. 2 | 4 means 24) and count the leaves to verify all 9 values are recorded.'
        }
      ]
    };
  }

  // Special interactive visual replay 2: Equation Transposition & Balance (Maths #16, #17, #18)
  if (arch.includes('equation') || arch.includes('inspection') || arch.includes('solve_for')) {
    const solSteps = question.canonical_solution?.steps || [];
    if (solSteps.length > 0) {
      const frames = solSteps.map((st, idx) => ({
        time_ms: idx * 2800,
        action: idx === solSteps.length - 1 ? 'final_solution' : 'show_step',
        latex: st.to_latex || st.from_latex || String(st),
        from_latex: st.from_latex || null,
        operation_badge: st.justification || st.rule || (idx === 0 ? 'Apply inverse operation to both sides (keep equation balanced)' : 'Isolate the variable'),
        narrative: `Step ${idx + 1}: ${st.justification || st.explanation || `Transform ${st.from_latex || ''} into ${st.to_latex || ''}`}`
      }));
      return {
        archetype: arch || 'equation_balance',
        title: `SimuLearn Walkthrough • Balancing & Solving ${topic}`,
        subject,
        grade,
        grid_type: 'stepwise_math',
        frames
      };
    }
  }

  // Dynamic synthesis from canonical_solution.steps or worked_solution lines
  const dSpec = question.diagram_spec || question.diagram || question.graph || question.function_graph || null;
  const canonicalSteps = question.canonical_solution?.steps;
  if (Array.isArray(canonicalSteps) && canonicalSteps.length > 0) {
    const frames = canonicalSteps.map((st, idx) => {
      const fromLtx = st.from_latex ? `${st.from_latex} \\;\\longrightarrow\\; ` : '';
      const toLtx = st.to_latex || st.latex || st.step || '';
      return {
        time_ms: idx * 2800,
        action: idx === canonicalSteps.length - 1 ? 'final_solution' : 'show_step',
        latex: `${fromLtx}${toLtx}`,
        operation_badge: st.justification || `Step ${idx + 1}`,
        narrative: st.justification
          ? `Step ${idx + 1}: ${st.justification}`
          : `Step ${idx + 1}: Evaluate and simplify to obtain ${String(toLtx).replace(/\\/g, '')}.`
      };
    });
    return {
      archetype: arch || 'dynamic_canonical',
      title: `SimuLearn Walkthrough • ${topic}`,
      subject,
      grade,
      grid_type: dSpec ? 'diagram_and_steps' : 'stepwise_math',
      diagram_spec: dSpec,
      frames
    };
  }

  const rawWorked = String(question.worked_solution || question.explanation || question.sample_answer || '').trim();
  if (rawWorked) {
    const rawLines = rawWorked
      .split(/\n+/)
      .map((l) => l.replace(/^\*\*.*?\*\*:?\s*/, '').trim())
      .filter((l) => l.length > 2);

    if (rawLines.length > 0) {
      const frames = rawLines.slice(0, 6).map((line, idx) => {
        const cleanMath = line.replace(/\$/g, '');
        return {
          time_ms: idx * 2800,
          action: idx === rawLines.length - 1 ? 'final_solution' : 'show_step',
          latex: `\\text{${cleanMath.slice(0, 95).replace(/[{}]/g, '')}}`,
          operation_badge: `Step ${idx + 1} of ${Math.min(6, rawLines.length)}`,
          narrative: line.replace(/\$/g, '')
        };
      });
      if (question.expected_answer || question.correct_answer) {
        const finalAns = String(question.expected_answer || question.correct_answer).replace(/\$/g, '');
        frames.push({
          time_ms: frames.length * 2800,
          action: 'final_solution',
          latex: `\\mathbf{\\text{Final Answer: } ${finalAns.slice(0, 75).replace(/[{}]/g, '')}}`,
          operation_badge: 'Verified Final Result',
          narrative: `Final Answer: ${finalAns}`
        });
      }
      return {
        archetype: arch || 'dynamic_worked_solution',
        title: `SimuLearn Walkthrough • ${topic}`,
        subject,
        grade,
        grid_type: dSpec ? 'diagram_and_steps' : 'stepwise_math',
        diagram_spec: dSpec,
        frames
      };
    }
  }

  return null;
}

export default function SimuLearnPlayer({
  archetypeKey = 'accounting_crj_vat',
  customScript = null,
  activeQuestion = null,
  subject = null,
  grade = null,
  topic = null,
  isOpen = true,
  embedded = false,
  onClose,
  onComplete
}) {
  const dynamicQuestionScript = React.useMemo(
    () => buildDynamicSimuLearnScript(activeQuestion, subject, grade, topic),
    [activeQuestion, subject, grade, topic]
  );
  const script = customScript || dynamicQuestionScript || DEFAULT_SCRIPTS[archetypeKey] || DEFAULT_SCRIPTS.accounting_crj_vat;
  const frames = script.frames || [];

  const [currentFrameIndex, setCurrentFrameIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [playbackSpeed, setPlaybackSpeed] = useState(1);
  const [tableValues, setTableValues] = useState({});
  const timerRef = useRef(null);

  // Reset playback and frames whenever modal opens or script changes
  useEffect(() => {
    if (isOpen) {
      setCurrentFrameIndex(0);
      setIsPlaying(false);
      setTableValues({});
    } else {
      setIsPlaying(false);
      if (timerRef.current) clearTimeout(timerRef.current);
    }
  }, [isOpen, archetypeKey]);

  const currentFrame = frames[currentFrameIndex] || frames[0];
  const isFinished = currentFrameIndex >= frames.length - 1;

  // Sync table values up to current frame
  useEffect(() => {
    const newValues = {};
    for (let i = 0; i <= currentFrameIndex; i++) {
      const f = frames[i];
      if (f && f.action === 'type_cell' && f.cell_id) {
        newValues[f.cell_id] = f.value;
      }
    }
    setTableValues(newValues);
  }, [currentFrameIndex, frames]);

  // Autoplay step timer (only active when modal is open and isPlaying is true)
  useEffect(() => {
    if (!isOpen || !isPlaying || isFinished) {
      if (timerRef.current) clearTimeout(timerRef.current);
      return;
    }

    const nextFrame = frames[currentFrameIndex + 1];
    const currentMs = currentFrame?.time_ms || 0;
    const nextMs = nextFrame?.time_ms || currentMs + 2500;
    const delta = Math.max(800, (nextMs - currentMs) / playbackSpeed);

    timerRef.current = setTimeout(() => {
      if (currentFrameIndex < frames.length - 1) {
        setCurrentFrameIndex(prev => prev + 1);
      } else {
        setIsPlaying(false);
      }
    }, delta);

    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, [isOpen, isPlaying, currentFrameIndex, frames, playbackSpeed, isFinished]);

  if (!isOpen) return null;

  const handleRestart = () => {
    setCurrentFrameIndex(0);
    setTableValues({});
    setIsPlaying(true);
  };

  const handleNext = () => {
    if (currentFrameIndex < frames.length - 1) {
      setCurrentFrameIndex(prev => prev + 1);
    }
  };

  const handlePrev = () => {
    if (currentFrameIndex > 0) {
      setCurrentFrameIndex(prev => prev - 1);
    }
  };

  return (
    <div
      data-testid={embedded ? "embedded-simulearn-player" : "modal-simulearn-player"}
      className={
        embedded
          ? "w-full flex flex-col animate-fade-in"
          : "fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-950/80 backdrop-blur-md animate-fade-in"
      }
    >
      <div className="bg-slate-900 border border-slate-700/80 rounded-2xl shadow-2xl max-w-3xl w-full flex flex-col overflow-hidden text-slate-100">
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-4 border-b border-slate-800 bg-slate-950/50">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-sm border border-indigo-500/30">
              ▶
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs px-2 py-0.5 rounded-full bg-indigo-900/60 text-indigo-300 font-semibold border border-indigo-700/50">
                  SimuLearn • {script.subject}
                </span>
                <span className="text-xs text-slate-400">Step {currentFrameIndex + 1} of {frames.length}</span>
              </div>
              <h3 className="text-sm sm:text-base font-semibold text-slate-100 mt-0.5">
                {script.title}
              </h3>
            </div>
          </div>
          {onClose && !embedded && (
            <button
              type="button"
              data-testid="btn-simulearn-close"
              onClick={onClose}
              className="p-1.5 rounded-lg text-slate-400 hover:text-slate-100 hover:bg-slate-800 transition-colors cursor-pointer"
            >
              ✕
            </button>
          )}
        </div>

        {/* Dynamic Simulation Stage */}
        <div className="p-6 bg-slate-950/90 flex flex-col items-center justify-center min-h-[260px] relative">
          {/* Modal content based on grid_type */}
          {script.grid_type === 'journal_table' && (
            <div className="w-full overflow-x-auto">
              <table className="w-full text-xs text-left border-collapse border border-slate-700 rounded-lg overflow-hidden">
                <thead className="bg-slate-800/90 text-slate-300 text-[11px] uppercase tracking-wider">
                  <tr>
                    {script.headers?.map((h, i) => (
                      <th key={i} className="p-2.5 border-b border-r border-slate-700 font-semibold">
                        {h}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  <tr className="bg-slate-900/60">
                    <td className={`p-2.5 border-r border-slate-700 font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c0' ? 'bg-amber-500/20 text-amber-300 ring-2 ring-amber-400' : 'text-slate-200'}`}>
                      {tableValues['r0_c0'] || '—'}
                    </td>
                    <td className={`p-2.5 border-r border-slate-700 font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c1' ? 'bg-amber-500/20 text-amber-300 ring-2 ring-amber-400' : 'text-slate-200'}`}>
                      {tableValues['r0_c1'] || '—'}
                    </td>
                    <td className={`p-2.5 border-r border-slate-700 font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c2' ? 'bg-amber-500/20 text-amber-300 ring-2 ring-amber-400' : 'text-slate-200'}`}>
                      {tableValues['r0_c2'] || '—'}
                    </td>
                    <td className={`p-2.5 border-r border-slate-700 font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c3' ? 'bg-amber-500/20 text-amber-300 ring-2 ring-amber-400' : 'text-slate-200'}`}>
                      {tableValues['r0_c3'] || '—'}
                    </td>
                    <td className="p-2.5 border-r border-slate-700 font-mono text-slate-400">
                      {tableValues['r0_c3'] ? (parseFloat(tableValues['r0_c3']) * 0.15).toFixed(2) : '—'}
                    </td>
                    <td className="p-2.5 font-mono text-slate-400">
                      800.00
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          )}

          {script.grid_type === 'punnett_grid' && (
            <div className="flex flex-col items-center gap-3">
              <div className="grid grid-cols-3 gap-2 text-center text-sm font-semibold">
                <div className="p-2 text-slate-400">♀ \ ♂</div>
                <div className="p-2 bg-indigo-950/60 rounded text-indigo-300">B</div>
                <div className="p-2 bg-indigo-950/60 rounded text-indigo-300">b</div>

                <div className="p-2 bg-purple-950/60 rounded text-purple-300">B</div>
                <div className={`p-3 rounded border font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c0' ? 'bg-amber-500/20 border-amber-400 text-amber-300 ring-2 ring-amber-400' : 'bg-slate-800/80 border-slate-700 text-slate-200'}`}>
                  {tableValues['r0_c0'] || '—'}
                </div>
                <div className={`p-3 rounded border font-mono transition-all duration-300 ${currentFrame.cell_id === 'r0_c1' ? 'bg-amber-500/20 border-amber-400 text-amber-300 ring-2 ring-amber-400' : 'bg-slate-800/80 border-slate-700 text-slate-200'}`}>
                  {tableValues['r0_c1'] || '—'}
                </div>

                <div className="p-2 bg-purple-950/60 rounded text-purple-300">b</div>
                <div className={`p-3 rounded border font-mono transition-all duration-300 ${currentFrame.cell_id === 'r1_c0' ? 'bg-amber-500/20 border-amber-400 text-amber-300 ring-2 ring-amber-400' : 'bg-slate-800/80 border-slate-700 text-slate-200'}`}>
                  {tableValues['r1_c0'] || '—'}
                </div>
                <div className={`p-3 rounded border font-mono transition-all duration-300 ${currentFrame.cell_id === 'r1_c1' ? 'bg-amber-500/20 border-amber-400 text-amber-300 ring-2 ring-amber-400' : 'bg-slate-800/80 border-slate-700 text-slate-200'}`}>
                  {tableValues['r1_c1'] || '—'}
                </div>
              </div>
            </div>
          )}

          {script.grid_type === 'stem_and_leaf_visual' && (
            <div className="flex flex-col items-center gap-4 w-full max-w-lg" data-testid="simulearn-stem-leaf">
              <div className="flex flex-wrap gap-1.5 justify-center">
                {(currentFrame.raw_numbers || []).map((num, idx) => (
                  <span
                    key={idx}
                    className="px-2.5 py-1 rounded-md bg-slate-800 border border-slate-700 font-mono text-xs text-slate-200"
                  >
                    <span className="text-amber-400 font-bold">{Math.floor(num / 10)}</span>
                    <span className="text-sky-300 font-bold">{num % 10}</span>
                  </span>
                ))}
              </div>
              {currentFrame.active_num && (
                <div className="px-3 py-1 rounded-full bg-amber-500/20 border border-amber-400/50 text-amber-200 text-xs font-mono font-bold">
                  {currentFrame.active_num}
                </div>
              )}
              <table className="w-full max-w-xs border-collapse border border-slate-700 rounded-lg overflow-hidden text-sm font-mono">
                <thead className="bg-slate-800 text-slate-200">
                  <tr>
                    <th className="p-2 border-r border-slate-700 text-center w-24 text-amber-300">Stem (10s)</th>
                    <th className="p-2 text-left pl-4 text-sky-300">Leaf (Units)</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(currentFrame.stems || {}).map(([stemKey, leaves]) => (
                    <tr key={stemKey} className="border-t border-slate-800 bg-slate-900/70">
                      <td className="p-2.5 border-r border-slate-700 text-center font-bold text-amber-300">{stemKey}</td>
                      <td className="p-2.5 pl-4 tracking-widest text-sky-200 font-bold">
                        {Array.isArray(leaves) && leaves.length > 0 ? leaves.join('   ') : '—'}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {(script.grid_type === 'stepwise_math' || script.grid_type === 'diagram_and_steps') && (
            <div className="flex flex-col lg:flex-row items-center justify-center gap-4 w-full max-w-4xl" data-testid="simulearn-stepwise-stage">
              {script.diagram_spec && (
                <div className="w-full lg:w-1/2 p-3 bg-white rounded-xl border border-slate-300 shadow-sm text-slate-900" data-testid="simulearn-embedded-diagram">
                  <DiagramRenderer diagram={script.diagram_spec} />
                </div>
              )}
              <div className="flex flex-col items-center gap-3 text-center w-full max-w-xl">
                {currentFrame.from_latex && (
                  <div className="p-2.5 bg-slate-900/60 rounded-lg border border-slate-800 text-slate-400 text-sm">
                    <KaTeXRenderer latex={currentFrame.from_latex} />
                  </div>
                )}
                {currentFrame.operation_badge && (
                  <div className="px-3 py-1 rounded-full bg-amber-500/20 border border-amber-400/40 text-amber-300 text-xs font-semibold flex items-center gap-1.5">
                    <span>⇣</span>
                    <span>{currentFrame.operation_badge}</span>
                  </div>
                )}
                {currentFrame.latex && (
                  <div className="p-3.5 bg-slate-900/90 rounded-xl border border-indigo-500/30 text-indigo-200 text-lg shadow-inner w-full overflow-x-auto">
                    <KaTeXRenderer latex={currentFrame.latex} />
                  </div>
                )}
              </div>
            </div>
          )}

          {script.grid_type === 'diagram_process' && (
            <div className="flex flex-col items-center gap-4 w-full" data-testid="simulearn-diagram-process">
              {/* Dynamic Phase HUD */}
              <div className="flex flex-wrap items-center justify-center gap-2">
                <span className="px-3 py-1 rounded-full text-xs font-bold font-mono uppercase bg-indigo-500/20 text-indigo-300 border border-indigo-500/30" data-testid="sim-phase-badge">
                  Phase: {currentFrame.state ? currentFrame.state.replace(/_/g, ' ') : 'Static'}
                </span>
                {currentFrame.sound && (
                  <span className="px-3 py-1 rounded-full text-xs font-bold font-mono uppercase bg-rose-500/20 text-rose-300 border border-rose-500/30 animate-pulse" data-testid="sim-sound-badge">
                    Heart Sound: {currentFrame.sound}
                  </span>
                )}
                {currentFrame.ecg_segment && (
                  <span className="px-3 py-1 rounded-full text-xs font-mono text-cyan-300 bg-cyan-950/60 border border-cyan-800" data-testid="sim-ecg-badge">
                    ECG Trace: {currentFrame.ecg_segment}
                  </span>
                )}
              </div>

              {/* Master Diagram Vector Canvas */}
              <div className="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 w-full flex justify-center max-w-xl shadow-inner">
                {script.diagram_type === 'alveolus_gas_exchange' ? (
                  <AlveolusGasExchangeSvg
                    state={currentFrame.state || 'alive'}
                    mode="alive"
                    phase={currentFrame.phase || currentFrame.state}
                    pins={[]}
                    gradeMask={script.grade === 9 ? 'g9' : 'g11'}
                  />
                ) : script.diagram_type === 'particle_model' ? (
                  <ParticleModelSvg
                    view="alive"
                    initialTemperature={currentFrame.state === 'solid' ? -15 : currentFrame.state === 'melting' ? 0 : currentFrame.state === 'liquid' ? 45 : currentFrame.state === 'boiling' ? 100 : 130}
                    pins={[]}
                    gradeMask="g8"
                    allowViewSwitch={false}
                  />
                ) : script.diagram_type === 'geyser_heating_element' ? (
                  <GeyserHeatingElementSvg
                    view="alive"
                    initialWaterTemp={currentFrame.state === 'heating' ? 30 : currentFrame.state === 'convection' ? 45 : currentFrame.state === 'stratification' ? 60 : 70}
                    thermostatSetpoint={65}
                    pins={[]}
                    gradeMask="g8"
                    allowViewSwitch={false}
                  />
                ) : script.diagram_type === 'optical_telescopes' ? (
                  <OpticalTelescopesSvg
                    view="alive"
                    initialMode={currentFrame.state === 'reflection' ? 'reflector' : currentFrame.state === 'refraction' ? 'refractor' : 'comparative'}
                    pins={[]}
                    gradeMask="g8"
                    allowViewSwitch={false}
                  />
                ) : (
                  <HumanHeartSvg
                    state={currentFrame.state || 'static'}
                    pins={[]}
                    landmarks={[
                      { text: 'Aorta', anchor: [320, 65], side: 'right' },
                      { text: 'Pulmonary Artery', anchor: [270, 110], side: 'left' },
                      { text: 'Superior Vena Cava', anchor: [140, 90], side: 'left' }
                    ]}
                    gradeMask="g10"
                  />
                )}
              </div>
            </div>
          )}

          {/* Formula overlay / Callout */}
          {currentFrame.latex && script.grid_type !== 'stepwise_math' && (
            <div className="mt-4 p-2.5 px-4 bg-slate-900/90 rounded-xl border border-indigo-500/30 text-indigo-200 text-sm animate-fade-in shadow-lg">
              <KaTeXRenderer latex={currentFrame.latex} />
            </div>
          )}
        </div>

        {/* Narrative & Insight Bar */}
        <div className="px-6 py-3.5 bg-slate-900 border-t border-slate-800/80 flex items-start gap-3">
          <span className="text-amber-400 text-base mt-0.5">💡</span>
          <p className="text-xs sm:text-sm text-slate-200 leading-relaxed font-medium">
            {currentFrame.narrative}
          </p>
        </div>

        {/* Progress Scrub Bar */}
        <div className="w-full bg-slate-800 h-1.5 cursor-pointer">
          <div
            className="bg-indigo-500 h-full transition-all duration-300"
            style={{ width: `${((currentFrameIndex + 1) / frames.length) * 100}%` }}
          />
        </div>

        {/* Playback Controls & Actions */}
        <div className="p-4 bg-slate-950 flex flex-wrap items-center justify-between gap-3 border-t border-slate-800/80">
          <div className="flex items-center gap-2">
            <button
              type="button"
              data-testid="btn-simulearn-restart"
              onClick={handleRestart}
              className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors cursor-pointer"
              title="Restart"
            >
              ↺
            </button>
            <button
              type="button"
              data-testid="btn-simulearn-prev"
              onClick={handlePrev}
              disabled={currentFrameIndex === 0}
              className="px-2.5 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-xs font-semibold transition-colors cursor-pointer flex items-center gap-1"
              title="Previous Step"
            >
              ⏮ Prev Step
            </button>
            <button
              type="button"
              data-testid="btn-simulearn-play-pause"
              onClick={() => setIsPlaying(!isPlaying)}
              className="px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-colors flex items-center gap-1.5 shadow-md shadow-indigo-900/40 cursor-pointer"
            >
              {isPlaying ? '⏸ Pause' : '▶ Auto-Play'}
            </button>
            <button
              type="button"
              data-testid="btn-simulearn-next"
              onClick={handleNext}
              disabled={isFinished}
              className="px-2.5 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 text-xs font-semibold transition-colors cursor-pointer flex items-center gap-1"
              title="Next Step"
            >
              Next Step ⏭
            </button>
          </div>

          <div className="flex items-center gap-2">
            {/* Speed pills */}
            <div className="flex items-center bg-slate-900 rounded-lg p-0.5 border border-slate-800 text-[11px]">
              {[0.5, 1, 1.5, 2].map(speed => (
                <button
                  key={speed}
                  type="button"
                  onClick={() => setPlaybackSpeed(speed)}
                  className={`px-2 py-1 rounded transition-colors cursor-pointer ${
                    playbackSpeed === speed
                      ? 'bg-slate-700 text-indigo-300 font-semibold'
                      : 'text-slate-400 hover:text-slate-200'
                  }`}
                >
                  {speed}x
                </button>
              ))}
            </div>

            {/* Complete / Try Practice button */}
            <button
              type="button"
              data-testid="btn-simulearn-complete"
              onClick={() => {
                if (onComplete) onComplete();
                if (onClose) onClose();
              }}
              className="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs transition-colors shadow-md shadow-emerald-900/40 cursor-pointer font-bold"
            >
              Try Question Now →
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
