/**
 * sampleClassesData.js
 * Comprehensive CAPS curriculum data for South African High Schools (Grades 7–12).
 * Provides the 5-class scoped test suite for the owner/tester account,
 * while maintaining clean empty state for general teacher signups.
 */

export const STORAGE_KEY = 'fundile_teacher_classes_v3';

export const FIVE_TEST_CLASSES = [
  {
    classId: 'cls_gr10_acc',
    name: 'Grade 10 Accounting (Period 2)',
    subject: 'Accounting',
    grade: '10',
    term: 1,
    joinCode: 'ACC10B',
    studentCount: 28,
    avgMastery: 78,
    homeworkDue: 8,
    topMisconception: 'net_vs_gross_confusion',
    misconceptionLabel: 'Confusing 15% Exclusive vs 115% Inclusive VAT Formula',
    recentSubmissionCount: 24,
    students: [
      {
        id: 's1',
        name: 'Thabo Ndlovu',
        email: 'thabo.n@school.co.za',
        score: 88,
        status: 'Mastered',
        photoURL: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&q=80',
        topic: 'Cash Receipts & Payments Journals',
        olympiadBadge: '🥇 SAICA Gold (94%)',
        misconception: null,
        lastActive: '10 mins ago',
      },
      {
        id: 's2',
        name: 'Lerato Dlamini',
        email: 'lerato.d@school.co.za',
        score: 58,
        status: 'Remedial',
        photoURL: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=120&q=80',
        topic: 'Debtors Ledger & Allowances',
        olympiadBadge: null,
        misconception: 'net_vs_gross_confusion',
        misconceptionDesc: 'Inverting debtor control debits and credits',
        lastActive: '45 mins ago',
      },
      {
        id: 's3',
        name: 'Sipho Zulu',
        email: 'sipho.z@school.co.za',
        score: 92,
        status: 'Mastered',
        photoURL: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80',
        topic: 'Trial Balance & Financial Statements',
        olympiadBadge: '🥈 SAICA Top 5%',
        misconception: null,
        lastActive: '2 hours ago',
      },
      {
        id: 's4',
        name: 'Zanele Khumalo',
        email: 'zanele.k@school.co.za',
        score: 74,
        status: 'On Track',
        photoURL: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=120&q=80',
        topic: 'VAT Output vs VAT Input',
        olympiadBadge: null,
        misconception: 'net_vs_gross_confusion',
        misconceptionDesc: '15% Exclusive vs 115% Inclusive calculation',
        lastActive: 'Yesterday',
      },
      {
        id: 's5',
        name: 'Nkosana Sithole',
        email: 'nkosana.s@school.co.za',
        score: 64,
        status: 'In Progress',
        photoURL: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80',
        topic: 'Posting from Cash Receipts Journal',
        olympiadBadge: null,
        misconception: 'cost_of_sales_omission',
        misconceptionDesc: 'Omitting Cost of Sales double entry in CRJ',
        lastActive: '3 hours ago',
      },
    ]
  },
  {
    classId: 'cls_gr10_math',
    name: 'Grade 10 Mathematics — Alpha',
    subject: 'Mathematics',
    grade: '10',
    term: 1,
    joinCode: 'MAT10A',
    studentCount: 32,
    avgMastery: 71,
    homeworkDue: 14,
    topMisconception: 'sign_error_distribution',
    misconceptionLabel: 'Sign Error when Distributing Negative Outer Factors',
    recentSubmissionCount: 29,
    students: [
      {
        id: 's6',
        name: 'Kagiso Molefe',
        email: 'kagiso.m@school.co.za',
        score: 68,
        status: 'On Track',
        photoURL: 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=120&q=80',
        topic: 'Algebraic Expressions & Factoring',
        olympiadBadge: '🥈 SAMO Silver (88%)',
        misconception: 'sign_error_distribution',
        misconceptionDesc: 'Distributing negative sign across brackets',
        lastActive: '1 hour ago',
      },
      {
        id: 's7',
        name: 'Naledi Sithole',
        email: 'naledi.s@school.co.za',
        score: 52,
        status: 'Remedial',
        photoURL: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=120&q=80',
        topic: 'Exponential Equations & Laws',
        olympiadBadge: null,
        misconception: 'sign_error_distribution',
        misconceptionDesc: 'Adding exponents when multiplying unlike bases',
        lastActive: 'Just now',
      },
      {
        id: 's8',
        name: 'Bongani Nkosi',
        email: 'bongani.n@school.co.za',
        score: 91,
        status: 'Mastered',
        photoURL: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80',
        topic: 'Analytical Geometry & Linear Functions',
        olympiadBadge: '🥇 SAMO Top 100 Provincial',
        misconception: null,
        lastActive: '5 hours ago',
      },
      {
        id: 's9',
        name: 'Buhle Mabena',
        email: 'buhle.m@school.co.za',
        score: 72,
        status: 'On Track',
        photoURL: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&q=80',
        topic: 'Trigonometric Ratios (SOH CAH TOA)',
        olympiadBadge: null,
        misconception: null,
        lastActive: 'Yesterday',
      },
      {
        id: 's10',
        name: 'Ayanda Mokoena',
        email: 'ayanda.m@school.co.za',
        score: 61,
        status: 'In Progress',
        photoURL: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=120&q=80',
        topic: 'Number Patterns & Linear Sequences',
        olympiadBadge: null,
        misconception: 'sequence_difference_multiplier',
        misconceptionDesc: 'Confusing common difference with multiplier',
        lastActive: '4 hours ago',
      },
    ]
  },
  {
    classId: 'cls_gr11_math',
    name: 'Grade 11 Mathematics — Extended',
    subject: 'Mathematics',
    grade: '11',
    term: 1,
    joinCode: 'MAT11X',
    studentCount: 26,
    avgMastery: 74,
    homeworkDue: 6,
    topMisconception: 'quadratic_formula_sign',
    misconceptionLabel: 'Inverting -b in Quadratic Formula ±√Discriminant',
    recentSubmissionCount: 22,
    students: [
      {
        id: 's15',
        name: 'Tumelo Khanyile',
        email: 'tumelo.k@school.co.za',
        score: 89,
        status: 'Mastered',
        photoURL: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80',
        topic: 'Quadratic Equations & Nature of Roots',
        olympiadBadge: '🥇 SAMO Round 2 Qualifier',
        misconception: null,
        lastActive: '15 mins ago',
      },
      {
        id: 's16',
        name: 'Nomsa Gwala',
        email: 'nomsa.g@school.co.za',
        score: 54,
        status: 'Remedial',
        photoURL: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&q=80',
        topic: 'Trigonometric Reduction Formulae',
        olympiadBadge: null,
        misconception: 'quadratic_formula_sign',
        misconceptionDesc: 'Forgetting -b sign change when b is negative',
        lastActive: '1 hour ago',
      },
      {
        id: 's17',
        name: 'Jabulani Mazibuko',
        email: 'jabu.m@school.co.za',
        score: 76,
        status: 'On Track',
        photoURL: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80',
        topic: 'Analytical Geometry (Inclination angles)',
        olympiadBadge: null,
        misconception: null,
        lastActive: '4 hours ago',
      },
    ]
  },
  {
    classId: 'cls_gr9_ems',
    name: 'Grade 9 EMS (Commerce)',
    subject: 'EMS',
    grade: '9',
    term: 1,
    joinCode: 'EMS9Q1',
    studentCount: 35,
    avgMastery: 84,
    homeworkDue: 9,
    topMisconception: 'debit_credit_inversion',
    misconceptionLabel: 'Inverting Bank Statement vs Bank Account Entries',
    recentSubmissionCount: 33,
    students: [
      {
        id: 's11',
        name: 'Andile Mthembu',
        email: 'andile.m@school.co.za',
        score: 94,
        status: 'Mastered',
        photoURL: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80',
        topic: 'Cash Receipts Journal (CRJ)',
        olympiadBadge: '🥇 EMS Provincial Quiz Winner',
        misconception: null,
        lastActive: '20 mins ago',
      },
      {
        id: 's12',
        name: 'Precious Moyo',
        email: 'precious.m@school.co.za',
        score: 79,
        status: 'On Track',
        photoURL: 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=120&q=80',
        topic: 'The Circular Flow Model of Economy',
        olympiadBadge: null,
        misconception: null,
        lastActive: '3 hours ago',
      },
      {
        id: 's13',
        name: 'Kgotso Baloyi',
        email: 'kgotso.b@school.co.za',
        score: 56,
        status: 'Remedial',
        photoURL: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=120&q=80',
        topic: 'Accounting Equation: Assets = OE + Liab',
        olympiadBadge: null,
        misconception: 'debit_credit_inversion',
        misconceptionDesc: 'Swapping asset debit and expense debit roles',
        lastActive: '6 hours ago',
      },
      {
        id: 's14',
        name: 'Minenhle Radebe',
        email: 'minenhle.r@school.co.za',
        score: 82,
        status: 'Mastered',
        photoURL: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&q=80',
        topic: 'Entrepreneurship & SWOT Analysis',
        olympiadBadge: null,
        misconception: null,
        lastActive: 'Yesterday',
      },
    ]
  },
  {
    classId: 'cls_gr10_physics',
    name: 'Grade 10 Physical Sciences (Physics & Chem)',
    subject: 'Physical Sciences',
    grade: '10',
    term: 1,
    joinCode: 'PHY10P',
    studentCount: 30,
    avgMastery: 70,
    homeworkDue: 11,
    topMisconception: 'vector_direction_omission',
    misconceptionLabel: 'Omitting Direction on Vector Resultants [e.g. East or Right]',
    recentSubmissionCount: 25,
    students: [
      {
        id: 's18',
        name: 'Khaya Cele',
        email: 'khaya.c@school.co.za',
        score: 85,
        status: 'Mastered',
        photoURL: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80',
        topic: 'Transverse Waves & Pulses (v = fλ)',
        olympiadBadge: '🥈 SAASTA Science Top 10%',
        misconception: null,
        lastActive: '30 mins ago',
      },
      {
        id: 's19',
        name: 'Gugu Mkhize',
        email: 'gugu.m@school.co.za',
        score: 55,
        status: 'Remedial',
        photoURL: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=120&q=80',
        topic: 'Vectors & Scalar Quantities in 1D',
        olympiadBadge: null,
        misconception: 'vector_direction_omission',
        misconceptionDesc: 'Reporting displacement with magnitude only without direction',
        lastActive: '2 hours ago',
      },
      {
        id: 's20',
        name: 'Sandile Vilakazi',
        email: 'sandile.v@school.co.za',
        score: 72,
        status: 'On Track',
        photoURL: 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=120&q=80',
        topic: 'Atomic Structure & Electron Configuration',
        olympiadBadge: null,
        misconception: null,
        lastActive: 'Yesterday',
      },
    ]
  },
  {
    classId: 'cls_gr7_ems',
    name: 'Grade 7 EMS (Senior Phase)',
    subject: 'EMS',
    grade: '7',
    term: 1,
    joinCode: 'EMS7P1',
    studentCount: 30,
    avgMastery: 81,
    homeworkDue: 6,
    topMisconception: 'budget_deficit_surplus_confusion',
    misconceptionLabel: 'Confusing Personal Budget Deficits vs Surplus Calculation',
    recentSubmissionCount: 28,
    students: [
      {
        id: 's21',
        name: 'Mpho Sithole',
        email: 'mpho.s@school.co.za',
        score: 90,
        status: 'Mastered',
        photoURL: null,
        topic: 'Personal Budgets & Savings',
        olympiadBadge: '🥇 Top Junior Saver',
        misconception: null,
        lastActive: '15 mins ago',
      },
      {
        id: 's22',
        name: 'Nandi Khumalo',
        email: 'nandi.k@school.co.za',
        score: 62,
        status: 'Remedial',
        photoURL: null,
        topic: 'Needs vs Wants Classification',
        olympiadBadge: null,
        misconception: 'budget_deficit_surplus_confusion',
        misconceptionDesc: 'Calculating fixed vs variable expenses',
        lastActive: '1 hour ago',
      }
    ]
  }
];

/**
 * Scoped Seeding Helper:
 * Ensures the 5 test classes are strictly provided for testing/owner accounts,
 * while other teacher accounts default to an empty roster [].
 */
export function getInitialTeacherClasses(currentUser) {
  // Check if testing/owner account
  const isTester = Boolean(
    currentUser?.isSuperAdmin ||
    currentUser?.isOwner ||
    currentUser?.email === 'sithole@school.co.za' ||
    (currentUser?.email && (
      currentUser.email.includes('owner') ||
      currentUser.email.includes('admin') ||
      currentUser.email.includes('fundile')
    ))
  );

  // If saved in localStorage, respect user's saved state
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
      const parsed = JSON.parse(saved);
      if (Array.isArray(parsed)) {
        return parsed;
      }
    }
  } catch (e) {
    console.warn('Error reading saved classes:', e);
  }

  // If tester/owner and no saved state, load the 5 rich test classes
  if (isTester) {
    return FIVE_TEST_CLASSES;
  }

  // For any other user, return empty classes array
  return [];
}

/**
 * Generates CAPS-aligned questions & step-by-step marking rubrics
 */
export function generateCapsTestQuestions(subject, grade, term, marksTarget) {
  const isAccounting = subject === 'Accounting';
  const isEMS = subject === 'EMS';
  const isPhysics = subject === 'Physical Sciences' || subject === 'Life Sciences';

  let bank = [];

  if (isAccounting || isEMS) {
    bank = [
      {
        id: 'q1',
        type: 'stepwise',
        question_text: `Value Added Tax (VAT) Calculation:
A sole trader, Apex Traders (registered VAT vendor at standard rate 15%), sold merchandise for cash.
1.1 The cash register tape shows gross sales of R34 500 (inclusive of 15% VAT). Calculate the Output VAT amount and the exclusive Sales amount.
1.2 The trader purchased inventory for R18 400 (inclusive of VAT). Calculate the Input VAT claimable.
1.3 Determine whether Apex Traders owes SARS or is entitled to a refund, and state the exact amount.`,
        marks: 10,
        solution: `1.1 Output VAT = R34 500 × 15 / 115 = R4 500. Sales (exclusive) = R34 500 - R4 500 = R30 000.
1.2 Input VAT = R18 400 × 15 / 115 = R2 400.
1.3 Output VAT (R4 500) > Input VAT (R2 400). Apex owes SARS = R4 500 - R2 400 = R2 100 payable.`,
        marking_scheme: [
          { point: '1.1 Output VAT formula 15/115 calculation (R4 500)', marks: 3, editable: true },
          { point: '1.1 Sales exclusive subtraction (R30 000)', marks: 2, editable: true },
          { point: '1.2 Input VAT formula 15/115 calculation (R2 400)', marks: 2, editable: true },
          { point: '1.3 Net VAT payable status to SARS (R2 100)', marks: 3, editable: true },
        ]
      },
      {
        id: 'q2',
        type: 'stepwise',
        question_text: `Cash Receipts Journal (CRJ) & Cash Payments Journal (CPJ):
Record the following transactions for KZN Outfitters for May 2026:
2.1 May 04: Cash sales of merchandise, R13 800 (cost of sales R9 200, mark-up 50% on cost).
2.2 May 11: Paid the landlord R7 500 by EFT for store rent.
2.3 May 18: Owner C. Dube deposited R25 000 directly into the business bank account as capital contribution.`,
        marks: 15,
        solution: `2.1 CRJ: Bank R13 800; Sales R12 000 (excl VAT R1 800); Cost of Sales R9 200.
2.2 CPJ: Bank R7 500; Rent Expense R7 500.
2.3 CRJ: Bank R25 000; Sundry Accounts Capital R25 000.`,
        marking_scheme: [
          { point: '2.1 CRJ Bank gross amount entry R13 800', marks: 3, editable: true },
          { point: '2.1 Cost of sales double entry R9 200', marks: 3, editable: true },
          { point: '2.2 CPJ Bank and Rent expense entries R7 500', marks: 4, editable: true },
          { point: '2.3 Capital deposit sundry entry R25 000', marks: 5, editable: true },
        ]
      },
      {
        id: 'q3',
        type: 'diagram',
        question_text: `Accounting Equation & Ledger Systems Flow:
Analyze the relationship between source documents, subsidiary journals, general ledger accounts, and trial balance balances. Complete the ledger accounts coordinate mapping.`,
        marks: 25,
        solution: `Asset accounts increase on Debit (+), decrease on Credit (-). Equity accounts increase on Credit (+), decrease on Debit (-). Liabilities increase on Credit (+), decrease on Debit (-).`,
        marking_scheme: [
          { point: 'Bank account double entry debit asset', marks: 8, editable: true },
          { point: 'Sales credit revenue equity', marks: 8, editable: true },
          { point: 'Cost of sales debit expense and trading stock credit', marks: 9, editable: true },
        ]
      },
    ];
  } else if (isPhysics) {
    bank = [
      {
        id: 'q1',
        type: 'stepwise',
        question_text: `Transverse Waves: A transverse wave travels along a stretched rope at a speed of 12 m/s. The distance between two consecutive wave crests is 0,8 m.
1.1 Define a transverse wave.
1.2 Calculate the frequency of the wave.
1.3 Calculate the period of the wave.`,
        marks: 10,
        solution: `1.1 A wave where particles of the medium vibrate perpendicular to the direction of wave motion.
1.2 v = f λ => 12 = f(0,8) => f = 15 Hz.
1.3 T = 1 / f = 1 / 15 ≈ 0,067 s.`,
        marking_scheme: [
          { point: '1.1 Correct CAPS standard definition [M]', marks: 3, editable: true },
          { point: '1.2 Formula v = f λ and substitution [M]', marks: 2, editable: true },
          { point: '1.2 Correct frequency 15 Hz with unit [A]', marks: 2, editable: true },
          { point: '1.3 Period formula T = 1/f and answer [A]', marks: 3, editable: true },
        ]
      },
      {
        id: 'q2',
        type: 'diagram',
        question_text: `Digestive System / Alimentary Canal Diagram Labeling:
Identify and label the key anatomical structures of the human digestive system and their associated physiological enzyme secretion roles.`,
        marks: 15,
        solution: `A: Mouth, B: Oesophagus, C: Stomach, D: Liver, E: Pancreas, F: Small Intestine, G: Large Intestine.`,
        marking_scheme: [
          { point: 'Anatomical labeling accuracy', marks: 10, editable: true },
          { point: 'Digestive enzyme secretion role description', marks: 5, editable: true },
        ]
      }
    ];
  } else {
    // Mathematics
    bank = [
      {
        id: 'q1',
        type: 'stepwise',
        question_text: `Algebraic Expressions & Factoring:
1.1 Factorise completely: 3x² - 12
1.2 Factorise the quadratic trinomial: 2x² + 5x - 3
1.3 Simplify the algebraic fraction: (x² - 9) / (x² + 2x - 15)`,
        marks: 10,
        solution: `1.1 3x² - 12 = 3(x² - 4) = 3(x - 2)(x + 2).
1.2 2x² + 5x - 3 = (2x - 1)(x + 3).
1.3 (x - 3)(x + 3) / ((x + 5)(x - 3)) = (x + 3) / (x + 5), for x ≠ 3, -5.`,
        marking_scheme: [
          { point: '1.1 Common factor 3 extraction', marks: 2, editable: true },
          { point: '1.1 Difference of two squares (x-2)(x+2)', marks: 2, editable: true },
          { point: '1.2 Factors (2x - 1)(x + 3)', marks: 3, editable: true },
          { point: '1.3 Factoring numerator and denominator with cancelation', marks: 3, editable: true },
        ]
      },
      {
        id: 'q2',
        type: 'stepwise',
        question_text: `Equations & Inequalities:
2.1 Solve for x: (2x - 3)(x + 4) = 0
2.2 Solve for x: 3^(x+1) - 3^x = 54
2.3 Solve simultaneously: y = 2x - 1 and x² + y² = 13`,
        marks: 15,
        solution: `2.1 x = 3/2 or x = -4.
2.2 3^x(3 - 1) = 54 => 3^x(2) = 54 => 3^x = 27 => x = 3.
2.3 x² + (2x - 1)² = 13 => 5x² - 4x - 12 = 0 => (5x + 6)(x - 2) = 0.
x = 2 => y = 3; or x = -1,2 => y = -3,4.`,
        marking_scheme: [
          { point: '2.1 Two linear factors solution', marks: 3, editable: true },
          { point: '2.2 Factoring 3^x and exponential equality', marks: 4, editable: true },
          { point: '2.3 Quadratic substitution and standard form', marks: 4, editable: true },
          { point: '2.3 Dual solution coordinates pairing', marks: 4, editable: true },
        ]
      },
      {
        id: 'q3',
        type: 'diagram',
        question_text: `Analytical Geometry & Straight Lines:
Given points A(-2, 3), B(4, 7), and C(1, -2) in the Cartesian plane.
3.1 Calculate the distance AB correct to two decimal places.
3.2 Determine the coordinates of M, the midpoint of AB.
3.3 Find the equation of the line perpendicular to AB passing through M.`,
        marks: 25,
        solution: `3.1 AB = √((4 - (-2))² + (7 - 3)²) = √(36 + 16) = √52 ≈ 7,21 units.
3.2 Midpoint M = ((-2 + 4)/2, (3 + 7)/2) = (1, 5).
3.3 Gradient m_AB = (7 - 3)/(4 - (-2)) = 4/6 = 2/3.
Perpendicular gradient m_perp = -3/2.
y - 5 = -3/2(x - 1) => y = -3/2 x + 13/2.`,
        marking_scheme: [
          { point: '3.1 Distance formula calculation (7,21 units)', marks: 8, editable: true },
          { point: '3.2 Midpoint formula application (1, 5)', marks: 8, editable: true },
          { point: '3.3 Negative reciprocal gradient & perpendicular equation', marks: 9, editable: true },
        ]
      }
    ];
  }

  if (marksTarget === 25) {
    return [bank[0], bank[1] || bank[0]];
  } else if (marksTarget === 50) {
    return bank;
  }
  return bank;
}
