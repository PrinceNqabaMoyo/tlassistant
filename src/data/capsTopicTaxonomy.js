/**
 * capsTopicTaxonomy.js
 * Comprehensive South African National Curriculum Statement (CAPS) topic & concept taxonomy
 * across all 9 subjects for Senior Phase (Grades 7–9) and FET Phase (Grades 10–12).
 * 
 * Powers Teacher Assessment Scope Customization & 1-Click Provincial ATP Presets:
 * Enables educators to select multiple topics and granularly toggle specific concepts/subskills,
 * with 1-click presets for Term 1 Control Test, Term 2 Mid-Year, Term 3 Trial, and Term 4 Final.
 */

export const CAPS_TOPIC_TAXONOMY = {
  'Mathematics': {
    '10': [
      {
        name: 'Algebraic Expressions',
        term: 1,
        subtopics: ['Linear factorisation', 'Trinomial factorisation', 'Difference of two squares', 'Sum and difference of two cubes', 'Algebraic fractions']
      },
      {
        name: 'Equations and Inequalities',
        term: 1,
        subtopics: ['Linear equations', 'Quadratic equations', 'Simultaneous equations', 'Linear inequalities', 'Literal equations']
      },
      {
        name: 'Trigonometry',
        term: 2,
        subtopics: ['Trigonometric ratios (sin, cos, tan)', 'Reciprocal ratios (cosec, sec, cot)', 'Special angles (30°, 45°, 60°)', 'Solving right-angled triangles', 'Trigonometric functions (sine and cosine graphs)']
      },
      {
        name: 'Euclidean Geometry',
        term: 2,
        subtopics: ['Triangles and angle sum', 'Properties of special quadrilaterals', 'Midpoint theorem', 'Pythagoras theorem applications']
      },
      {
        name: 'Analytical Geometry',
        term: 3,
        subtopics: ['Distance between two points', 'Gradient of a line segment', 'Midpoint of a line segment', 'Parallel and perpendicular lines']
      },
      {
        name: 'Functions and Graphs',
        term: 3,
        subtopics: ['Linear function y = mx + c', 'Hyperbola y = a/x + q', 'Parabola y = ax^2 + q', 'Exponential function y = ab^x + q']
      }
    ],
    '11': [
      {
        name: 'Exponents and Surds',
        term: 1,
        subtopics: ['Laws of rational exponents', 'Simplification of surds', 'Equations involving surds']
      },
      {
        name: 'Equations and Inequalities',
        term: 1,
        subtopics: ['Quadratic formula', 'Completing the square', 'Nature of roots (discriminant)', 'Quadratic inequalities']
      },
      {
        name: 'Trigonometry',
        term: 2,
        subtopics: ['Trigonometric identities (tan = sin/cos, sin^2+cos^2=1)', 'Reduction formulae (180±θ, 360±θ, 90±θ)', 'General solution of trigonometric equations', 'Sine, Cosine, and Area rules']
      },
      {
        name: 'Circle Geometry',
        term: 3,
        subtopics: ['Line from circle centre perpendicular to chord', 'Angle subtended at centre vs circumference', 'Angles in the same circle segment', 'Tangent perpendicular to radius', 'Tan-chord theorem']
      }
    ],
    '12': [
      {
        name: 'Differential Calculus',
        term: 1,
        subtopics: ['First principles derivative definition', 'Rules for differentiation', 'Cubic polynomials and turning points', 'Rates of change and calculus optimization']
      },
      {
        name: 'Polynomials and Remainder Theorem',
        term: 1,
        subtopics: ['Factor theorem', 'Remainder theorem', 'Cubic polynomial factorisation']
      },
      {
        name: 'Trigonometry',
        term: 2,
        subtopics: ['Compound angle identities', 'Double angle identities', '3D Trigonometric problems']
      },
      {
        name: 'Euclidean Geometry',
        term: 3,
        subtopics: ['Proportionality theorem in triangles', 'Similarity of triangles (AAA)', 'Theorem of Pythagoras via similarity']
      }
    ],
    '7': [
      {
        name: 'Numbers and Operations',
        term: 1,
        subtopics: ['Whole numbers and place value', 'Prime factors and HCF/LCM', 'Common fractions and mixed numbers', 'Decimal fractions and percentages']
      },
      {
        name: 'Patterns and Algebra',
        term: 2,
        subtopics: ['Numeric and geometric patterns', 'Algebraic expressions and input/output rules', 'Linear equations by inspection']
      }
    ],
    '8': [
      {
        name: 'Integers and Exponents',
        term: 1,
        subtopics: ['Calculations with negative integers', 'Laws of integer exponents', 'Scientific notation']
      },
      {
        name: 'Algebraic Expressions and Equations',
        term: 2,
        subtopics: ['Expanding binomial products', 'Common factor extraction', 'Solving linear equations with brackets']
      }
    ],
    '9': [
      {
        name: 'Algebra and Polynomials',
        term: 1,
        subtopics: ['Product of binomials', 'Factorising quadratic trinomials', 'Difference of two squares', 'Algebraic fractions with monomial denominators']
      },
      {
        name: 'Equations and Functions',
        term: 2,
        subtopics: ['Linear equations with fractions', 'Quadratic equations by factorisation', 'Straight-line graphs (gradient and intercepts)']
      }
    ]
  },

  'Accounting': {
    '10': [
      {
        name: 'Cash Receipts and Payments Journals',
        term: 1,
        subtopics: ['Cash Receipts Journal (15% VAT)', 'Cash Payments Journal', 'Bank Account reconciliation', 'Analysis of receipts']
      },
      {
        name: 'Value Added Tax (VAT)',
        term: 1,
        subtopics: ['15% VAT calculations (Zero-rated, Exempt, Standard)', 'Output VAT vs Input VAT', 'VAT payable or refundable to SARS']
      },
      {
        name: 'Debtors and Creditors',
        term: 2,
        subtopics: ['Debtors Journal and Debtors Allowances Journal', 'Creditors Journal and Creditors Allowances Journal', 'Debtors and Creditors Ledgers']
      },
      {
        name: 'General Ledger and Trial Balance',
        term: 3,
        subtopics: ['Posting from subsidiary journals', 'Balancing asset and liability accounts', 'Trial balance extraction']
      }
    ],
    '11': [
      {
        name: 'Partnerships',
        term: 1,
        subtopics: ['Partnership accounting concepts', 'Appropriation account', 'Current accounts and capital accounts', 'Financial statements for partnerships']
      },
      {
        name: 'Bank Reconciliation',
        term: 2,
        subtopics: ['Bank statement analysis', 'Bank reconciliation statement', 'Internal control over cash']
      },
      {
        name: 'Fixed Assets and Depreciation',
        term: 3,
        subtopics: ['Fixed asset register', 'Diminishing balance method', 'Straight line method', 'Asset disposal calculations']
      }
    ],
    '12': [
      {
        name: 'Companies and Financial Statements',
        term: 1,
        subtopics: ['Share capital and retained income', 'Income Statement and Balance Sheet', 'Notes to the financial statements']
      },
      {
        name: 'Cash Flow Statement',
        term: 2,
        subtopics: ['Cash generated from operations', 'Cash effects of investing activities', 'Cash effects of financing activities']
      },
      {
        name: 'Financial Analysis and Ratios',
        term: 3,
        subtopics: ['Solvency and liquidity ratios', 'Profitability and operating efficiency', 'Debt-equity and financial gearing']
      },
      {
        name: 'Corporate Governance and King IV',
        term: 4,
        subtopics: ['Role of directors and audit committee', 'Internal audit and ethics', 'Corporate social responsibility']
      }
    ]
  },

  'Physical Sciences': {
    '10': [
      {
        name: 'Mechanics: Kinematics',
        term: 1,
        subtopics: ['Position, displacement, and distance', 'Average speed and average velocity', 'Uniform acceleration equations of motion', 'Motion graphs (position-time, velocity-time)']
      },
      {
        name: 'Waves, Sound and Light',
        term: 2,
        subtopics: ['Transverse and longitudinal waves', 'Wave speed equation v = fλ', 'Electromagnetic spectrum and photon energy']
      },
      {
        name: 'Matter and Materials',
        term: 3,
        subtopics: ['Atomic structure and electron configurations', 'Chemical bonding (covalent, ionic, metallic)', 'Physical and chemical change']
      }
    ],
    '11': [
      {
        name: 'Newton\'s Laws of Motion',
        term: 1,
        subtopics: ['Newton\'s First Law and inertia', 'Newton\'s Second Law (F_net = ma)', 'Newton\'s Third Law (action-reaction)', 'Newton\'s Law of Universal Gravitation']
      },
      {
        name: 'Stoichiometry and Quantitative Chemistry',
        term: 2,
        subtopics: ['Mole concept and molar mass', 'Empirical and molecular formulae', 'Concentration and molar gas volume', 'Stoichiometric calculations with limiting reagents']
      }
    ],
    '12': [
      {
        name: 'Momentum, Impulse, Work and Energy',
        term: 1,
        subtopics: ['Linear momentum and conservation of momentum', 'Impulse-momentum theorem', 'Work-energy theorem', 'Conservative and non-conservative forces']
      },
      {
        name: 'Organic Chemistry',
        term: 2,
        subtopics: ['Homologous series and functional groups', 'IUPAC naming and structural isomers', 'Physical properties and intermolecular forces', 'Organic reaction types (addition, substitution, elimination)']
      },
      {
        name: 'Electrodynamics and Electricity',
        term: 3,
        subtopics: ['AC and DC generators', 'Electric motors and Fleming\'s left hand rule', 'Alternating current and rms voltage/current', 'Internal resistance and series-parallel networks']
      }
    ]
  },

  'Business Studies': {
    '10': [
      {
        name: 'Business Environments',
        term: 1,
        subtopics: ['Micro environment and eight business functions', 'Market environment (competitors, suppliers, consumers)', 'Macro environment (PESTLE analysis)']
      },
      {
        name: 'Forms of Ownership',
        term: 2,
        subtopics: ['Sole trader and partnership', 'Close Corporation', 'Private Company (Pty) Ltd', 'Public Company (Ltd)']
      }
    ],
    '11': [
      {
        name: 'Challenges in Business Environments',
        term: 1,
        subtopics: ['Adapting to challenges in business environments', 'Socio-economic issues (unemployment, piracy, strikes)', 'Creative thinking and problem-solving techniques']
      }
    ],
    '12': [
      {
        name: 'Impact of Recent Legislation',
        term: 1,
        subtopics: ['Broad-Based Black Economic Empowerment (BBBEE)', 'Labour Relations Act (LRA)', 'Basic Conditions of Employment Act (BCEA)', 'Employment Equity Act (EEA)']
      },
      {
        name: 'Human Resources and Ethics',
        term: 2,
        subtopics: ['Recruitment, selection and induction', 'Ethics and professionalism in business', 'King Code governance principles']
      }
    ]
  },

  'Life Sciences': {
    '10': [
      {
        name: 'Chemistry of Life and Cells',
        term: 1,
        subtopics: ['Inorganic and organic compounds', 'Cell structure and organelles', 'Mitosis and the cell cycle']
      }
    ],
    '11': [
      {
        name: 'Plant and Animal Physiology',
        term: 1,
        subtopics: ['Photosynthesis and leaf structure', 'Human nutrition and digestive system', 'Cellular respiration and ATP', 'Gaseous exchange']
      }
    ],
    '12': [
      {
        name: 'Genetics and Inheritance',
        term: 1,
        subtopics: ['DNA and RNA structure and replication', 'Protein synthesis (transcription and translation)', 'Meiosis and chromosomal mutations', 'Mendelian monohybrid and dihybrid crosses', 'Pedigree diagrams and genetic counseling']
      },
      {
        name: 'Evolution',
        term: 2,
        subtopics: ['Evidence for evolution', 'Darwinian natural selection', 'Speciation and geographic isolation', 'Hominid fossil records']
      }
    ]
  },

  'EMS': {
    '7': [
      {
        name: 'The Economy',
        term: 1,
        subtopics: ['History of money', 'Needs and wants', 'Goods and services', 'Businesses and consumers']
      },
      {
        name: 'Financial Literacy',
        term: 2,
        subtopics: ['Basic accounting concepts', 'Income and expenses', 'Personal and business budgets']
      }
    ],
    '8': [
      {
        name: 'The Economy',
        term: 1,
        subtopics: ['Government roles in the economy', 'National budget and taxes', 'Markets and prices']
      },
      {
        name: 'Financial Literacy',
        term: 2,
        subtopics: ['Accounting cycle', 'Source documents', 'Cash Receipts Journal (CRJ)', 'Cash Payments Journal (CPJ)']
      }
    ],
    '9': [
      {
        name: 'The Economy',
        term: 1,
        subtopics: ['Closed circular flow model', 'Price theory (demand and supply curves)', 'Sectors of the economy (primary, secondary, tertiary)']
      },
      {
        name: 'Financial Literacy',
        term: 2,
        subtopics: ['Cash Journals (CRJ and CPJ)', 'Debtors Journal (DJ)', 'General Ledger and trial balance']
      }
    ]
  },

  'Natural Sciences': {
    '7': [
      {
        name: 'Life and Living',
        term: 1,
        subtopics: ['Biosphere and biodiversity', 'Sexual reproduction in angiosperms', 'Human reproduction']
      },
      {
        name: 'Matter and Materials',
        term: 2,
        subtopics: ['Properties of materials', 'Separating mixtures', 'Acids, bases, and neutrals']
      }
    ],
    '8': [
      {
        name: 'Energy and Change',
        term: 3,
        subtopics: ['Static electricity', 'Electric circuits and components', 'Series and parallel circuits', 'Ohm\'s law basics']
      }
    ],
    '9': [
      {
        name: 'Matter and Materials',
        term: 2,
        subtopics: ['Atomic structure and subatomic particles', 'Periodic table of elements', 'Chemical reactions and equations', 'Reactions of metals and non-metals with oxygen']
      }
    ]
  },

  'Mathematical Literacy': {
    '10': [
      {
        name: 'Finance',
        term: 1,
        subtopics: ['Financial documents (receipts, bills, invoices)', 'Budgets, income and expenditure', 'Banking and interest rates']
      }
    ],
    '11': [
      {
        name: 'Finance and Tariffs',
        term: 2,
        subtopics: ['Stepped municipal water tariffs', 'Prepaid electricity tariffs', 'Hire purchase and loan repayments']
      }
    ],
    '12': [
      {
        name: 'Taxation and Finance',
        term: 1,
        subtopics: ['SARS personal income tax brackets', 'Tax rebates and medical aid credits', 'Inflation and exchange rates']
      }
    ]
  },

  'Technical Mathematics': {
    '10': [
      {
        name: 'Number Systems and Algebra',
        term: 1,
        subtopics: ['Real and non-real numbers', 'Binary and hexadecimal conversion', 'Algebraic factorisation']
      }
    ],
    '11': [
      {
        name: 'Complex Numbers',
        term: 1,
        subtopics: ['Imaginary unit i and complex form a + bi', 'Argand diagrams', 'Modulus and argument']
      }
    ],
    '12': [
      {
        name: 'Mensuration and Integration',
        term: 3,
        subtopics: ['Circular geometry and radians', 'Arc length and sector area', 'Definite and indefinite integrals', 'Area under curves']
      }
    ]
  }
};
