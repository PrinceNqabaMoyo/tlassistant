/**
 * Authentic Diagnostic Question Bank
 * Pure, authentic South African exam-standard questions across all 9 subjects.
 * Zero-Meta-Curriculum Invariant: 0% administrative policy, 100% subject problem-solving.
 */

export const AUTHENTIC_DIAGNOSTIC_BANK = {
  accounting: {
    id: 'diag_acct_crj_101',
    modality: 'ledger',
    title: 'Cash Receipts Journal (15% VAT)',
    prompt: 'Phambili Solutions Ltd\nRecord the transactions in the Cash Receipts Journal for March.\n1. Day 1: Owner deposited capital R50 000.\n2. Day 4: Cash sales of merchandise R11 500 (incl. 15% VAT). Cost of sales R8 000.',
    journal: {
      title_fields: [{ cell_id: 'title_business', label: 'Business Name', editable: false, value: 'Phambili Solutions Ltd' }],
      headers: ['Doc', 'Day', 'Details', 'Fol', 'Bank', 'Sales', 'Output VAT', 'Cost of Sales'],
      rows: [
        [
          { cell_id: 'r0_c0', value: 'Rec 01', editable: false },
          { cell_id: 'r0_c1', value: '1', editable: false },
          { cell_id: 'r0_c2', value: 'Capital: S. Phambili', editable: false },
          { cell_id: 'r0_c3', value: 'B1', editable: false },
          { cell_id: 'r0_c4', value: '50000.00', editable: false },
          { cell_id: 'r0_c5', value: '', editable: false },
          { cell_id: 'r0_c6', value: '', editable: false },
          { cell_id: 'r0_c7', value: '', editable: false }
        ],
        [
          { cell_id: 'r1_c0', value: 'CRT 01', editable: false },
          { cell_id: 'r1_c1', value: '4', editable: false },
          { cell_id: 'r1_c2', value: 'Cash Sales', editable: false },
          { cell_id: 'r1_c3', value: 'N1', editable: false },
          { cell_id: 'r1_c4', value: '', editable: true },
          { cell_id: 'r1_c5', value: '10000.00', editable: false },
          { cell_id: 'r1_c6', value: '1500.00', editable: false },
          { cell_id: 'r1_c7', value: '8000.00', editable: false }
        ]
      ]
    },
    correct_map: { 'r1_c4': '11500.00' },
    marks: 6,
    hints: {
      tier1: 'Bank receives the total gross amount collected from the customer including VAT.',
      tier2: 'Gross Bank Amount = Net Sales (100%) + Output VAT (15%).',
      tier3: 'Calculate: R10 000 (Sales) + R1 500 (VAT) = R11 500.00.'
    }
  },

  mathematics: {
    id: 'diag_math_trinomial_101',
    question_type: 'mcq',
    modality: 'math',
    title: 'Algebraic Expressions: Trinomial Factorisation',
    prompt: 'Factorise the quadratic expression completely:\nx^2 - 7x + 12',
    options: [
      '(x - 3)(x - 4)',
      '(x + 3)(x + 4)',
      '(x - 2)(x - 6)',
      '(x - 1)(x - 12)'
    ],
    correct_index: 0,
    ideal_answer: '(x - 3)(x - 4)',
    marks: 4,
    worked_solution: 'Find factor pairs of +12 that sum to -7: (-3) and (-4). Thus x^2 - 7x + 12 = (x - 3)(x - 4).',
    hints: {
      tier1: 'Look at the constant term (+12) and the linear term coefficient (-7).',
      tier2: 'Since the constant is positive and the middle term is negative, both factors must be negative.',
      tier3: 'Factor pairs of 12: (-1, -12), (-2, -6), (-3, -4). Notice that -3 + (-4) = -7. So the answer is (x - 3)(x - 4).'
    }
  },

  physical_sciences: {
    id: 'diag_physics_kinematics_101',
    question_type: 'mcq',
    modality: 'math',
    title: 'Mechanics: 1D Uniform Acceleration',
    prompt: 'A vehicle accelerates uniformly from rest to a velocity of 20 m/s over a time interval of 5 seconds.\n\nCalculate the magnitude of the acceleration of the vehicle.',
    options: [
      '4 m/s²',
      '100 m/s²',
      '2 m/s²',
      '0.25 m/s²'
    ],
    correct_index: 0,
    ideal_answer: '4 m/s²',
    marks: 4,
    worked_solution: 'v_f = v_i + a * Δt => 20 = 0 + a(5) => a = 20 / 5 = 4 m/s².',
    hints: {
      tier1: 'Identify the given quantities: v_i = 0 m/s, v_f = 20 m/s, and Δt = 5 s.',
      tier2: 'Use the kinematic equation v_f = v_i + a * Δt.',
      tier3: 'Substitute into the equation: 20 = 0 + 5a, which gives a = 20 / 5 = 4 m/s².'
    }
  },

  business_studies: {
    id: 'diag_bs_environments_101',
    question_type: 'mcq',
    modality: 'math',
    title: 'Business Environments: Market Environment Analysis',
    prompt: 'Read the scenario below and answer the question:\n\nKhaya operates a bakery in Umlazi called "Khaya Sweets". He employs three bakers and purchases flour from Golden Grain Mills. Recently, a rival bakery opened across the street offering discounted bread.\n\nWhich ONE of the following is an element of the MARKET ENVIRONMENT affecting Khaya Sweets?',
    options: [
      'The three employed bakers',
      'Competitors (the rival bakery)',
      'The baking ovens and equipment',
      'Khaya\'s business vision statement'
    ],
    correct_index: 1,
    ideal_answer: 'Competitors (the rival bakery)',
    expected_answer: 'Competitors (the rival bakery)',
    marks: 3,
    worked_solution: 'Competitors belong to the market environment because they operate outside the firm within the immediate industry, where the business has influence but not complete control.',
    hints: {
      tier1: 'Distinguish between internal factors (micro environment) and industry factors (market environment).',
      tier2: 'The micro environment comprises internal employees, vision, and assets. The market environment includes customers, suppliers, and competitors.',
      tier3: 'The rival bakery is a competitor, which is a core component of the market environment.'
    }
  },

  life_sciences: {
    id: 'diag_lifesci_genetics_101',
    question_type: 'mcq',
    modality: 'math',
    title: 'Genetics: Monohybrid Dominance & Phenotypes',
    prompt: 'In pea plants, the allele for purple flowers (P) is dominant over the allele for white flowers (p).\n\nA heterozygous purple flowering plant (Pp) is crossed with a homozygous recessive white flowering plant (pp).\n\nWhat is the expected percentage of offspring with purple flowers?',
    options: [
      '50%',
      '75%',
      '25%',
      '100%'
    ],
    correct_index: 0,
    ideal_answer: '50%',
    expected_answer: '50%',
    marks: 4,
    worked_solution: 'Cross Pp x pp. Gametes: P, p with p, p. Punnett square gives 2 Pp (purple) and 2 pp (white). Probability of purple = 2/4 = 50%.',
    hints: {
      tier1: 'Draw a 2x2 Punnett square crossing alleles P and p against p and p.',
      tier2: 'The offspring genotypes produced are: Pp, Pp, pp, pp.',
      tier3: 'Two out of the four offspring inherit the dominant P allele (Pp), which gives 50% purple flowers.'
    }
  },

  mathematical_literacy: {
    id: 'diag_mathslit_tariffs_101',
    question_type: 'mcq',
    modality: 'math',
    title: 'Finance: Residential Water Tariff Calculation',
    prompt: 'A household consumed 22 kL of water in a month. The municipality applies the following stepped tariff:\n- Block 1 (0 to 6 kL): Free (R0.00)\n- Block 2 (7 to 15 kL): R18.50 per kL\n- Block 3 (16 to 30 kL): R24.00 per kL\n(Exclude VAT)\n\nCalculate the total monthly cost for 22 kL of water.',
    options: [
      'R334.50',
      'R528.00',
      'R407.00',
      'R314.50'
    ],
    correct_index: 0,
    ideal_answer: 'R334.50',
    marks: 5,
    worked_solution: 'Block 1 (6 kL): R0. Block 2 (9 kL): 9 x R18.50 = R166.50. Block 3 (7 kL): 7 x R24.00 = R168.00. Total = 0 + 166.50 + 168.00 = R334.50.',
    hints: {
      tier1: 'Split the 22 kL into the three steps: 6 kL in Block 1, 9 kL in Block 2, and 7 kL in Block 3.',
      tier2: 'Multiply the volume in each tier by its rate and sum the results.',
      tier3: 'Block 1 = R0.00. Block 2 = 9 × R18.50 = R166.50. Block 3 = 7 × R24.00 = R168.00. Total = R334.50.'
    }
  },

  technical_mathematics: {
    id: 'diag_techmath_complex_101',
    question_type: 'mcq',
    modality: 'math',
    title: 'Complex Numbers: Modulus Calculation',
    prompt: 'Given the complex number z = 3 + 4i.\n\nCalculate the modulus |z| of the complex number.',
    options: [
      '5',
      '7',
      '25',
      '1'
    ],
    correct_index: 0,
    ideal_answer: '5',
    marks: 3,
    worked_solution: '|z| = √(a² + b²) = √(3² + 4²) = √(9 + 16) = √25 = 5.',
    hints: {
      tier1: 'Recall that for any complex number z = a + bi, the modulus is given by |z| = √(a² + b²).',
      tier2: 'Substitute a = 3 and b = 4 into the formula.',
      tier3: '|z| = √(3² + 4²) = √(9 + 16) = √25 = 5.'
    }
  },

  natural_sciences: {
    id: 'diag_natsci_circuits_101',
    question_type: 'mcq',
    modality: 'math',
    title: 'Energy & Change: Series Electric Circuits',
    prompt: 'Two resistors of 4 Ω and 6 Ω are connected in SERIES across a 20 V power supply.\n\nDetermine the total resistance and the current in the circuit.',
    options: [
      'Total R = 10 Ω, Current = 2 A',
      'Total R = 2.4 Ω, Current = 8.3 A',
      'Total R = 10 Ω, Current = 200 A',
      'Total R = 24 Ω, Current = 0.83 A'
    ],
    correct_index: 0,
    ideal_answer: 'Total R = 10 Ω, Current = 2 A',
    marks: 4,
    worked_solution: 'Series resistance: R_total = 4 + 6 = 10 Ω. Current: I = V / R = 20 / 10 = 2 A.',
    hints: {
      tier1: 'For resistors connected in series, the total resistance is the sum of the individual resistances.',
      tier2: 'Use Ohm\'s Law formula: I = V / R_total.',
      tier3: 'R_total = 4 + 6 = 10 Ω. Then I = 20 V / 10 Ω = 2 A.'
    }
  },

  ems: {
    id: 'diag_ems_circular_101',
    question_type: 'mcq',
    modality: 'math',
    title: 'The Economy: Closed Circular Flow Model',
    prompt: 'In the closed circular flow of goods and services between Households and Businesses:\n\nHouseholds provide the factors of production (land, labour, capital, entrepreneurship) to businesses via the factor market.\n\nWhat remuneration do households receive in exchange for providing LABOUR?',
    options: [
      'Salaries and wages',
      'Rent',
      'Interest',
      'Profit'
    ],
    correct_index: 0,
    ideal_answer: 'Salaries and wages',
    expected_answer: 'Salaries and wages',
    marks: 3,
    worked_solution: 'The remuneration for labour is salaries and wages. (Rent is for land, interest is for capital, and profit is for entrepreneurship).',
    hints: {
      tier1: 'Recall the four factors of production and their respective economic rewards.',
      tier2: 'Land earns rent; Capital earns interest; Entrepreneurship earns profit.',
      tier3: 'Labour earns salaries and wages.'
    }
  }
};

/**
 * Multi-Topic Calibrated Diagnostic Batteries
 * Policy: 5–6 minutes per topic/concept within the subject.
 * Each topic battery features a 3-probe diagnostic sequence:
 * - Probe 1: Prerequisite Foundation (Grade N-1 Gateway)
 * - Probe 2: Standard Grade-Level Procedure
 * - Probe 3: Non-Routine Problem Solving & Misconception Trap
 */
export const AUTHENTIC_TOPIC_DIAGNOSTIC_BATTERIES = {
  mathematics: [
    {
      topicId: 'math_algebra_trinomials',
      topicName: 'Algebraic Expressions & Trinomial Factorisation',
      allocatedMins: 6,
      probes: [
        {
          id: 'diag_math_p1_foundation',
          probeType: 'prerequisite_foundation',
          prompt: 'Find two integers whose product is +24 and whose sum is -11.',
          options: ['-3 and -8', '-4 and -6', '-2 and -12', '-1 and -24'],
          correct_index: 0,
          ideal_answer: '-3 and -8',
          marks: 2,
          worked_solution: 'Factor pairs of 24: (-1, -24), (-2, -12), (-3, -8). Notice -3 + (-8) = -11.',
          hints: { tier1: 'Look for factors of +24 that add up to -11.', tier2: 'Both factors must be negative.', tier3: '-3 * -8 = 24 and -3 + -8 = -11.' }
        },
        AUTHENTIC_DIAGNOSTIC_BANK.mathematics, // Probe 2: Standard Gateway (x^2 - 7x + 12)
        {
          id: 'diag_math_p3_application',
          probeType: 'application_misconception',
          prompt: 'Factorise completely by removing the common factor first:\n2x^3 - 10x^2 - 48x',
          options: ['2x(x - 8)(x + 3)', '2x(x + 8)(x - 3)', 'x(2x - 16)(x + 3)', '(2x^2 - 16x)(x + 3)'],
          correct_index: 0,
          ideal_answer: '2x(x - 8)(x + 3)',
          marks: 4,
          worked_solution: 'Step 1: Extract 2x -> 2x(x^2 - 5x - 24). Step 2: Factorise trinomial -> 2x(x - 8)(x + 3).',
          hints: { tier1: 'Always extract the Highest Common Factor (2x) first.', tier2: 'Now factorise the remaining trinomial x^2 - 5x - 24.', tier3: 'Factor pairs of -24 summing to -5 are -8 and +3.' }
        }
      ]
    },
    {
      topicId: 'math_equations_inequalities',
      topicName: 'Linear & Quadratic Equations',
      allocatedMins: 6,
      probes: [
        {
          id: 'diag_math_eq_p1',
          probeType: 'prerequisite_foundation',
          prompt: 'Solve for x: 3x - 7 = 14',
          options: ['x = 7', 'x = 21', 'x = 2.33', 'x = 5'],
          correct_index: 0,
          ideal_answer: 'x = 7',
          marks: 2,
          worked_solution: '3x = 14 + 7 = 21 => x = 21 / 3 = 7.',
          hints: { tier1: 'Add 7 to both sides.', tier2: '3x = 21.', tier3: 'Divide by 3: x = 7.' }
        },
        {
          id: 'diag_math_eq_p2',
          probeType: 'standard_method',
          prompt: 'Solve for x: (2x - 1)(x + 4) = 0',
          options: ['x = 1/2 or x = -4', 'x = -1/2 or x = 4', 'x = 1 or x = -4', 'x = 2 or x = -4'],
          correct_index: 0,
          ideal_answer: 'x = 1/2 or x = -4',
          marks: 3,
          worked_solution: '2x - 1 = 0 => x = 1/2; x + 4 = 0 => x = -4.',
          hints: { tier1: 'Zero-product principle: either bracket equals zero.', tier2: '2x - 1 = 0 or x + 4 = 0.', tier3: 'x = 1/2 or x = -4.' }
        },
        {
          id: 'diag_math_eq_p3',
          probeType: 'application_misconception',
          prompt: 'Solve for x: x^2 = 5x (Do not divide by x without considering x = 0)',
          options: ['x = 0 or x = 5', 'x = 5 only', 'x = ±√5', 'x = 0 only'],
          correct_index: 0,
          ideal_answer: 'x = 0 or x = 5',
          marks: 3,
          worked_solution: 'x^2 - 5x = 0 => x(x - 5) = 0 => x = 0 or x = 5.',
          hints: { tier1: 'Move all terms to one side: x^2 - 5x = 0.', tier2: 'Factorise out the common factor x.', tier3: 'x = 0 or x = 5.' }
        }
      ]
    },
    {
      topicId: 'math_trigonometry',
      topicName: 'Trigonometry: Ratios & Right-Angled Triangles',
      allocatedMins: 5,
      probes: [
        {
          id: 'diag_math_trig_p1',
          probeType: 'prerequisite_foundation',
          prompt: 'In a right-angled triangle, which ratio defines sin(θ)?',
          options: ['Opposite / Hypotenuse', 'Adjacent / Hypotenuse', 'Opposite / Adjacent', 'Hypotenuse / Opposite'],
          correct_index: 0,
          ideal_answer: 'Opposite / Hypotenuse',
          marks: 2,
          worked_solution: 'SOH CAH TOA: Sin = Opposite / Hypotenuse.',
          hints: { tier1: 'Remember SOH CAH TOA.', tier2: 'S = O / H.', tier3: 'Opposite / Hypotenuse.' }
        },
        {
          id: 'diag_math_trig_p2',
          probeType: 'standard_method',
          prompt: 'Given a right triangle with Opposite = 3 and Adjacent = 4. What is the length of the Hypotenuse?',
          options: ['5', '7', '1', '25'],
          correct_index: 0,
          ideal_answer: '5',
          marks: 2,
          worked_solution: 'Pythagoras: r = √(3^2 + 4^2) = √(9 + 16) = √25 = 5.',
          hints: { tier1: 'Use Theorem of Pythagoras: c^2 = a^2 + b^2.', tier2: 'c^2 = 9 + 16 = 25.', tier3: 'c = 5.' }
        },
        {
          id: 'diag_math_trig_p3',
          probeType: 'application_misconception',
          prompt: 'If tan(θ) = 3/4 and θ is an acute angle, determine the value of cos(θ).',
          options: ['4/5', '3/5', '5/4', '3/4'],
          correct_index: 0,
          ideal_answer: '4/5',
          marks: 3,
          worked_solution: 'Opp = 3, Adj = 4 => Hyp = 5. Therefore cos(θ) = Adj / Hyp = 4/5.',
          hints: { tier1: 'Identify Opp = 3, Adj = 4.', tier2: 'Hypotenuse is 5.', tier3: 'cos(θ) = Adj / Hyp = 4/5.' }
        }
      ]
    }
  ],

  accounting: [
    {
      topicId: 'acct_crj_vat',
      topicName: 'Cash Receipts Journal & 15% VAT',
      allocatedMins: 6,
      probes: [
        {
          id: 'diag_acct_p1_equation',
          probeType: 'prerequisite_foundation',
          prompt: 'Which accounting equation relationship is fundamentally correct?',
          options: ['Assets = Owner\'s Equity + Liabilities', 'Owner\'s Equity = Assets + Liabilities', 'Liabilities = Assets + Owner\'s Equity', 'Assets + Owner\'s Equity = Liabilities'],
          correct_index: 0,
          ideal_answer: 'Assets = Owner\'s Equity + Liabilities',
          marks: 2,
          worked_solution: 'The basic accounting equation is Assets = Owner\'s Equity + Liabilities (A = OE + L).',
          hints: { tier1: 'Recall the dual-entry accounting equation.', tier2: 'Resources owned (Assets) equal capital plus borrowings.', tier3: 'A = OE + L.' }
        },
        AUTHENTIC_DIAGNOSTIC_BANK.accounting, // Probe 2: Standard Gateway (CRJ Bank Gross)
        {
          id: 'diag_acct_p3_costofsales',
          probeType: 'application_misconception',
          prompt: 'Goods with a cost price of R4 000 were sold at a mark-up of 50% on cost. Determine the selling price EXCLUDING VAT.',
          options: ['R6 000.00', 'R8 000.00', 'R4 600.00', 'R5 000.00'],
          correct_index: 0,
          ideal_answer: 'R6 000.00',
          marks: 3,
          worked_solution: 'Selling Price = Cost Price x (100 + 50) / 100 = 4000 x 1.50 = R6 000.00.',
          hints: { tier1: 'Mark-up on cost formula: Cost × 150 / 100.', tier2: '4 000 × 1.5 = 6 000.', tier3: 'Selling price = R6 000.00.' }
        }
      ]
    }
  ],

  business_studies: [
    {
      topicId: 'bs_environments',
      topicName: 'Business Environments: Micro, Market & Macro',
      allocatedMins: 5,
      probes: [
        AUTHENTIC_DIAGNOSTIC_BANK.business_studies,
        {
          id: 'diag_bs_p2_macro',
          probeType: 'standard_method',
          prompt: 'An increase in the South African VAT rate from 14% to 15% is an element of which business environment?',
          options: ['Macro environment', 'Micro environment', 'Market environment', 'Internal environment'],
          correct_index: 0,
          ideal_answer: 'Macro environment',
          marks: 2,
          worked_solution: 'Taxation and legislation are external factors in the macro environment over which businesses have no direct control.',
          hints: { tier1: 'Government taxation legislation applies nationwide.', tier2: 'Businesses have no direct control over national tax rates.', tier3: 'Macro environment.' }
        },
        {
          id: 'diag_bs_p3_ownership',
          probeType: 'application_misconception',
          prompt: 'Which form of ownership offers limited liability to shareholders and ends with "(Pty) Ltd"?',
          options: ['Private Company', 'Sole Proprietorship', 'Partnership', 'Public Company'],
          correct_index: 0,
          ideal_answer: 'Private Company',
          marks: 3,
          worked_solution: 'A Private Company is designated as (Proprietary) Limited or (Pty) Ltd and provides limited liability to its shareholders.',
          hints: { tier1: '(Pty) Ltd stands for Proprietary Limited.', tier2: 'Sole traders and partnerships have unlimited liability.', tier3: 'Private Company.' }
        }
      ]
    }
  ],

  physical_sciences: [
    {
      topicId: 'phys_kinematics',
      topicName: 'Mechanics: 1D Kinematics & Acceleration',
      allocatedMins: 5,
      probes: [
        AUTHENTIC_DIAGNOSTIC_BANK.physical_sciences,
        {
          id: 'diag_phys_p2_displacement',
          probeType: 'standard_method',
          prompt: 'A runner travels 100 m East, then turns and runs 40 m West. What is the runner\'s resultant DISPLACEMENT?',
          options: ['60 m East', '140 m', '60 m West', '100 m East'],
          correct_index: 0,
          ideal_answer: '60 m East',
          marks: 3,
          worked_solution: 'Displacement is a vector quantity: Δx = +100 m + (-40 m) = +60 m East.',
          hints: { tier1: 'Displacement is the change in position from start to end with direction.', tier2: 'East is positive (+100), West is negative (-40).', tier3: '100 - 40 = 60 m East.' }
        },
        {
          id: 'diag_phys_p3_newton',
          probeType: 'application_misconception',
          prompt: 'A 5 kg block rests on a horizontal frictionless surface. A force of 20 N is applied. Calculate its acceleration.',
          options: ['4 m/s²', '100 m/s²', '0.25 m/s²', '15 m/s²'],
          correct_index: 0,
          ideal_answer: '4 m/s²',
          marks: 3,
          worked_solution: 'Newton\'s Second Law: F_net = m * a => a = F_net / m = 20 / 5 = 4 m/s².',
          hints: { tier1: 'Use Newton\'s Second Law: F = ma.', tier2: 'a = F / m.', tier3: '20 / 5 = 4 m/s².' }
        }
      ]
    }
  ]
};

/**
 * Retrieves the authentic diagnostic question for any subject key
 */
export function getAuthenticDiagnosticQuestion(subjectKey, topicKey = null, probeIndex = 0) {
  const s = String(subjectKey || '').toLowerCase();
  
  // If specific topic battery requested
  if (topicKey && AUTHENTIC_TOPIC_DIAGNOSTIC_BATTERIES[s]) {
    const topicBat = AUTHENTIC_TOPIC_DIAGNOSTIC_BATTERIES[s].find(t => t.topicId === topicKey);
    if (topicBat && topicBat.probes[probeIndex]) {
      return topicBat.probes[probeIndex];
    }
  }

  // Canonical fallback per subject
  if (s.includes('acc')) return AUTHENTIC_DIAGNOSTIC_BANK.accounting;
  if (s.includes('tech')) return AUTHENTIC_DIAGNOSTIC_BANK.technical_mathematics;
  if (s.includes('lit') || s.includes('mathslit')) return AUTHENTIC_DIAGNOSTIC_BANK.mathematical_literacy;
  if (s.includes('math')) return AUTHENTIC_DIAGNOSTIC_BANK.mathematics;
  if (s.includes('phys')) return AUTHENTIC_DIAGNOSTIC_BANK.physical_sciences;
  if (s.includes('life') || s.includes('bio')) return AUTHENTIC_DIAGNOSTIC_BANK.life_sciences;
  if (s.includes('bus')) return AUTHENTIC_DIAGNOSTIC_BANK.business_studies;
  if (s.includes('ems') || s.includes('economic')) return AUTHENTIC_DIAGNOSTIC_BANK.ems;
  if (s.includes('nat') || s.includes('sci')) return AUTHENTIC_DIAGNOSTIC_BANK.natural_sciences;
  return AUTHENTIC_DIAGNOSTIC_BANK.mathematics;
}

/**
 * Returns the topic-level diagnostic battery for a given subject
 * Paced at 5–6 minutes per topic.
 */
export function getAuthenticTopicDiagnosticBattery(subjectKey) {
  const s = String(subjectKey || '').toLowerCase();
  const normalizedKey = s.includes('acc') ? 'accounting' :
                        s.includes('bus') ? 'business_studies' :
                        s.includes('phys') ? 'physical_sciences' : 'mathematics';
  return AUTHENTIC_TOPIC_DIAGNOSTIC_BATTERIES[normalizedKey] || AUTHENTIC_TOPIC_DIAGNOSTIC_BATTERIES.mathematics;
}

