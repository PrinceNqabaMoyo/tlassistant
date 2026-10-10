import React, { useState, useMemo } from 'react';
import {
  School,
  BookOpen,
  Users,
  Calendar,
  AlertTriangle,
  Download,
  Send,
  CheckCircle2,
  Clock,
  ChevronRight,
  Filter,
  Search,
  Award,
  TrendingUp,
  Copy,
  Check,
  RefreshCw,
  BarChart2,
  ArrowLeft,
  ArrowUpRight,
  UserPlus,
  Info,
  FileSpreadsheet,
  Layers,
  Activity,
  Radio,
  Sparkles,
  X,
  FileText,
  AlertCircle,
  GraduationCap,
  CreditCard,
  Eye,
  ShieldCheck,
  FileCheck
} from 'lucide-react';
import FeatureGatePanel from '../ui/FeatureGatePanel';
import { CLASS_ASSIGNMENTS_BLOCKED_MESSAGE } from '../../app/constants/access';
import studentStore from '../../services/studentStore';

// ==========================================
// STATIC DATA: ATP CURRICULUM PACING MATRIX
// ==========================================
const ATP_PACING_DATA = [
  {
    id: 'atp-acc-10',
    subject: 'Accounting',
    grade: '10',
    department: 'Commerce',
    hod: 'Mr. N. Sithole',
    totalWeeks: 10,
    currentWeek: 8,
    status: 'on_track', // 'on_track' | 'behind' | 'completed'
    statusLabel: 'Week 8 of 10 completed',
    curriculumCovered: 80,
    masteryDepth: 68,
    benchmarkMastery: 65,
    enrolledLearners: 148,
    currentTopic: 'VAT Calculations (Output vs Input VAT)',
    nextMilestone: 'Bank Reconciliation & Internal Controls',
    weeklyTopics: [
      { week: 1, topic: 'GAAP Principles & Accounting Equation', status: 'completed', mastery: 74 },
      { week: 2, topic: 'Debtors Journal (DJ) & Source Documents', status: 'completed', mastery: 72 },
      { week: 3, topic: 'Creditors Journal (CJ) & Source Documents', status: 'completed', mastery: 69 },
      { week: 4, topic: 'Debtors & Creditors Allowances Journals', status: 'completed', mastery: 63 },
      { week: 5, topic: 'General Ledger Postings & Trial Balance', status: 'completed', mastery: 66 },
      { week: 6, topic: 'Salaries and Wages Journals', status: 'completed', mastery: 70 },
      { week: 7, topic: 'Value Added Tax (Concepts & Invoicing)', status: 'completed', mastery: 61 },
      { week: 8, topic: 'VAT Calculations on Credit Sales & Allowances', status: 'in_progress', mastery: 52 },
      { week: 9, topic: 'Bank Reconciliation Statements', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Formal Controlled Test & Review', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-acc-11',
    subject: 'Accounting',
    grade: '11',
    department: 'Commerce',
    hod: 'Mr. N. Sithole',
    totalWeeks: 10,
    currentWeek: 8,
    status: 'on_track',
    statusLabel: 'Week 8 of 10 completed',
    curriculumCovered: 80,
    masteryDepth: 71,
    benchmarkMastery: 65,
    enrolledLearners: 124,
    currentTopic: 'Partnership Financial Statements & Notes',
    nextMilestone: 'Asset Disposal & Depreciation',
    weeklyTopics: [
      { week: 1, topic: 'Bank Reconciliation Revision & Updates', status: 'completed', mastery: 78 },
      { week: 2, topic: 'Creditors Reconciliation Statements', status: 'completed', mastery: 74 },
      { week: 3, topic: 'Fixed Assets Register & Depreciation Methods', status: 'completed', mastery: 69 },
      { week: 4, topic: 'Partnerships: Ledger Accounts & Appropriation', status: 'completed', mastery: 72 },
      { week: 5, topic: 'Partnerships: Income Statement Adjustments', status: 'completed', mastery: 68 },
      { week: 6, topic: 'Balance Sheet & Notes for Partnerships', status: 'completed', mastery: 67 },
      { week: 7, topic: 'Analysis & Interpretation of Financial Ratios', status: 'completed', mastery: 73 },
      { week: 8, topic: 'Partnership Ratio Diagnostics & Reporting', status: 'in_progress', mastery: 71 },
      { week: 9, topic: 'Asset Disposal Ledger Workflows', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Controlled Assessment', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-acc-12',
    subject: 'Accounting',
    grade: '12',
    department: 'Commerce',
    hod: 'Mr. N. Sithole',
    totalWeeks: 10,
    currentWeek: 9,
    status: 'on_track',
    statusLabel: 'Week 9 of 10 completed',
    curriculumCovered: 90,
    masteryDepth: 75,
    benchmarkMastery: 65,
    enrolledLearners: 112,
    currentTopic: 'Cash Flow Statements & Audit Reports',
    nextMilestone: 'Final Trial Balance & Preparatory Revision',
    weeklyTopics: [
      { week: 1, topic: 'Companies: Unique Ledger Accounts & Shares', status: 'completed', mastery: 81 },
      { week: 2, topic: 'Statement of Comprehensive Income Adjustments', status: 'completed', mastery: 76 },
      { week: 3, topic: 'Statement of Financial Position & Notes', status: 'completed', mastery: 74 },
      { week: 4, topic: 'Cash Flow Statement: Operating Activities', status: 'completed', mastery: 73 },
      { week: 5, topic: 'Cash Flow: Investing & Financing Activities', status: 'completed', mastery: 72 },
      { week: 6, topic: 'Analysis of Financial Statements & Solvency', status: 'completed', mastery: 77 },
      { week: 7, topic: 'Audit Reports & King IV Corporate Governance', status: 'completed', mastery: 79 },
      { week: 8, topic: 'Inventories: FIFO vs Weighted Average Valuation', status: 'completed', mastery: 75 },
      { week: 9, topic: 'Internal Audit & Ethics Case Studies', status: 'in_progress', mastery: 75 },
      { week: 10, topic: 'Term 1 Standardized Exam', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-math-10',
    subject: 'Mathematics',
    grade: '10',
    department: 'STEM',
    hod: 'Mrs. P. Khumalo',
    totalWeeks: 10,
    currentWeek: 8,
    status: 'on_track',
    statusLabel: 'Week 8 of 10 completed',
    curriculumCovered: 80,
    masteryDepth: 64,
    benchmarkMastery: 65,
    enrolledLearners: 182,
    currentTopic: 'Analytical Trigonometric Ratios (Cartesian Plane)',
    nextMilestone: 'Euclidean Geometry: Quadrilaterals',
    weeklyTopics: [
      { week: 1, topic: 'Algebraic Products & Factorization', status: 'completed', mastery: 68 },
      { week: 2, topic: 'Algebraic Fractions & Simplification', status: 'completed', mastery: 60 },
      { week: 3, topic: 'Linear & Quadratic Equations', status: 'completed', mastery: 67 },
      { week: 4, topic: 'Simultaneous Equations & Inequalities', status: 'completed', mastery: 65 },
      { week: 5, topic: 'Exponents & Exponential Equations', status: 'completed', mastery: 66 },
      { week: 6, topic: 'Number Patterns & Linear Sequences', status: 'completed', mastery: 72 },
      { week: 7, topic: 'Introductory Trigonometric Definitions', status: 'completed', mastery: 61 },
      { week: 8, topic: 'Trig Ratios in 4 Quadrants & Cast Rule', status: 'in_progress', mastery: 58 },
      { week: 9, topic: 'Euclidean Geometry: Triangle Theorems', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Controlled Test', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-math-11',
    subject: 'Mathematics',
    grade: '11',
    department: 'STEM',
    hod: 'Mrs. P. Khumalo',
    totalWeeks: 10,
    currentWeek: 7,
    status: 'behind',
    statusLabel: '1 Week Behind (Week 7 of 10)',
    curriculumCovered: 70,
    masteryDepth: 59,
    benchmarkMastery: 65,
    enrolledLearners: 168,
    currentTopic: 'Non-Right-Angled Trig (Sine & Cosine Rules)',
    nextMilestone: 'Circle Geometry: Arc & Tangent Theorems',
    weeklyTopics: [
      { week: 1, topic: 'Surds & Complex Exponent Equations', status: 'completed', mastery: 63 },
      { week: 2, topic: 'Quadratic Equations & Completing the Square', status: 'completed', mastery: 61 },
      { week: 3, topic: 'Nature of Roots & Discriminant Analysis', status: 'completed', mastery: 57 },
      { week: 4, topic: 'Quadratic Inequalities on Number Lines', status: 'completed', mastery: 62 },
      { week: 5, topic: 'Quadratic Number Patterns', status: 'completed', mastery: 68 },
      { week: 6, topic: 'Trigonometric Identities & Reduction Formulas', status: 'completed', mastery: 54 },
      { week: 7, topic: 'Sine, Cosine & Area Rules in 2D', status: 'in_progress', mastery: 51 },
      { week: 8, topic: 'Trigonometric General Solutions', status: 'scheduled', mastery: null },
      { week: 9, topic: 'Euclidean Circle Geometry Line Theorems', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Formal Test & Assessment', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-math-12',
    subject: 'Mathematics',
    grade: '12',
    department: 'STEM',
    hod: 'Mrs. P. Khumalo',
    totalWeeks: 10,
    currentWeek: 9,
    status: 'on_track',
    statusLabel: 'Week 9 of 10 completed',
    curriculumCovered: 90,
    masteryDepth: 72,
    benchmarkMastery: 65,
    enrolledLearners: 142,
    currentTopic: 'Calculus: First Principles & Derivative Rules',
    nextMilestone: 'Cubic Functions & Max/Min Optimization',
    weeklyTopics: [
      { week: 1, topic: 'Sequences & Series: Arithmetic & Geometric', status: 'completed', mastery: 77 },
      { week: 2, topic: 'Sum to Infinity & Sigma Notation', status: 'completed', mastery: 75 },
      { week: 3, topic: 'Functions: Hyperbolas & Exponential Graphs', status: 'completed', mastery: 70 },
      { week: 4, topic: 'Inverse Functions & Domain/Range Restrictions', status: 'completed', mastery: 71 },
      { week: 5, topic: 'Logarithmic Functions & Modeling', status: 'completed', mastery: 69 },
      { week: 6, topic: 'Compound & Double Angle Trig Identities', status: 'completed', mastery: 66 },
      { week: 7, topic: '3D Trigonometry & Practical Problem Solving', status: 'completed', mastery: 68 },
      { week: 8, topic: 'Calculus: Limits & Derivatives from First Principles', status: 'completed', mastery: 74 },
      { week: 9, topic: 'Rules for Differentiation & Tangent Equations', status: 'in_progress', mastery: 72 },
      { week: 10, topic: 'Term 1 Formal Test', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-phys-10',
    subject: 'Physical Sciences',
    grade: '10',
    department: 'Sciences',
    hod: 'Dr. T. van der Merwe',
    totalWeeks: 10,
    currentWeek: 7,
    status: 'behind',
    statusLabel: '1 Week Behind (Week 7 of 10)',
    curriculumCovered: 70,
    masteryDepth: 58,
    benchmarkMastery: 65,
    enrolledLearners: 136,
    currentTopic: 'Transverse Pulses & Waves (Superposition)',
    nextMilestone: 'Electromagnetic Radiation & Photons',
    weeklyTopics: [
      { week: 1, topic: 'Matter & Materials: States & Kinetic Theory', status: 'completed', mastery: 66 },
      { week: 2, topic: 'Atomic Structure & Periodic Table Trends', status: 'completed', mastery: 64 },
      { week: 3, topic: 'Chemical Bonding: Covalent, Ionic & Metallic', status: 'completed', mastery: 59 },
      { week: 4, topic: 'Transverse Pulses on a String & Superposition', status: 'completed', mastery: 58 },
      { week: 5, topic: 'Transverse Waves: Period, Frequency & Wave Speed', status: 'completed', mastery: 61 },
      { week: 6, topic: 'Longitudinal Waves & Sound Wave Acoustics', status: 'completed', mastery: 60 },
      { week: 7, topic: 'Electromagnetic Waves & Energy Quantization', status: 'in_progress', mastery: 55 },
      { week: 8, topic: 'Magnetism & Magnetic Field Lines', status: 'scheduled', mastery: null },
      { week: 9, topic: 'Electrostatics & Coulombs Law Intro', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Controlled Practical & Test', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-phys-12',
    subject: 'Physical Sciences',
    grade: '12',
    department: 'Sciences',
    hod: 'Dr. T. van der Merwe',
    totalWeeks: 10,
    currentWeek: 8,
    status: 'on_track',
    statusLabel: 'Week 8 of 10 completed',
    curriculumCovered: 80,
    masteryDepth: 66,
    benchmarkMastery: 65,
    enrolledLearners: 118,
    currentTopic: 'Electric Circuits: Internal Resistance & EMF',
    nextMilestone: 'Electrodynamics: Generators & Motors',
    weeklyTopics: [
      { week: 1, topic: 'Momentum & Impulse (Collisions in 1D)', status: 'completed', mastery: 74 },
      { week: 2, topic: 'Vertical Projectile Motion in 1D', status: 'completed', mastery: 69 },
      { week: 3, topic: 'Organic Chemistry: IUPAC Nomenclature', status: 'completed', mastery: 73 },
      { week: 4, topic: 'Organic Reactions: Substitution, Addition, Elimination', status: 'completed', mastery: 68 },
      { week: 5, topic: 'Reaction Rates & Maxwell-Boltzmann Curves', status: 'completed', mastery: 67 },
      { week: 6, topic: 'Chemical Equilibrium & Le Chateliers Principle', status: 'completed', mastery: 65 },
      { week: 7, topic: 'Acids & Bases: Ka, Kb, Titrations', status: 'completed', mastery: 62 },
      { week: 8, topic: 'Electric Circuits: EMF & Internal Resistance (Lost Volts)', status: 'in_progress', mastery: 54 },
      { week: 9, topic: 'Electrodynamics: Alternating Current (AC)', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Formal Controlled Test', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-life-10',
    subject: 'Life Sciences',
    grade: '10',
    department: 'Sciences',
    hod: 'Ms. B. Dlamini',
    totalWeeks: 10,
    currentWeek: 8,
    status: 'on_track',
    statusLabel: 'Week 8 of 10 completed',
    curriculumCovered: 80,
    masteryDepth: 71,
    benchmarkMastery: 65,
    enrolledLearners: 154,
    currentTopic: 'Plant & Animal Tissues (Microscopic Structure)',
    nextMilestone: 'Support & Transport Systems in Plants',
    weeklyTopics: [
      { week: 1, topic: 'Molecules for Life: Carbohydrates & Lipids', status: 'completed', mastery: 76 },
      { week: 2, topic: 'Proteins, Enzymes & Nucleic Acids Intro', status: 'completed', mastery: 70 },
      { week: 3, topic: 'Cell Structure: Organelles & Functions', status: 'completed', mastery: 74 },
      { week: 4, topic: 'Cell Division: Mitosis Stages', status: 'completed', mastery: 73 },
      { week: 5, topic: 'Cancer & Uncontrolled Cell Division', status: 'completed', mastery: 78 },
      { week: 6, topic: 'Plant Tissues: Meristematic & Permanent', status: 'completed', mastery: 69 },
      { week: 7, topic: 'Animal Tissues: Epithelial & Connective', status: 'completed', mastery: 71 },
      { week: 8, topic: 'Muscle & Nervous Tissue Diagnostics', status: 'in_progress', mastery: 71 },
      { week: 9, topic: 'Leaf Anatomy & Transpiration Mechanism', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Formal Assessment & Practical', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-life-12',
    subject: 'Life Sciences',
    grade: '12',
    department: 'Sciences',
    hod: 'Ms. B. Dlamini',
    totalWeeks: 10,
    currentWeek: 9,
    status: 'on_track',
    statusLabel: 'Week 9 of 10 completed',
    curriculumCovered: 90,
    masteryDepth: 74,
    benchmarkMastery: 65,
    enrolledLearners: 130,
    currentTopic: 'Human Reproduction & Gametogenesis',
    nextMilestone: 'Genetics & Monohybrid Crosses',
    weeklyTopics: [
      { week: 1, topic: 'DNA Code of Life & Replication', status: 'completed', mastery: 82 },
      { week: 2, topic: 'RNA & Protein Synthesis (Transcription/Translation)', status: 'completed', mastery: 75 },
      { week: 3, topic: 'Meiosis: First Meiotic Division', status: 'completed', mastery: 71 },
      { week: 4, topic: 'Meiosis: Second Division & Non-Disjunction', status: 'completed', mastery: 57 },
      { week: 5, topic: 'Reproduction in Vertebrates Strategies', status: 'completed', mastery: 80 },
      { week: 6, topic: 'Male & Female Human Reproductive Systems', status: 'completed', mastery: 77 },
      { week: 7, topic: 'Puberty, Menstrual Cycle & Hormonal Feedback', status: 'completed', mastery: 73 },
      { week: 8, topic: 'Fertilization, Gestation & Embryo Development', status: 'completed', mastery: 78 },
      { week: 9, topic: 'Reproductive Technologies & Contraception', status: 'in_progress', mastery: 74 },
      { week: 10, topic: 'Term 1 Controlled Examination', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-bus-11',
    subject: 'Business Studies',
    grade: '11',
    department: 'Commerce',
    hod: 'Mr. K. Pillay',
    totalWeeks: 10,
    currentWeek: 10,
    status: 'completed',
    statusLabel: 'Term 1 ATP Completed (10/10)',
    curriculumCovered: 100,
    masteryDepth: 78,
    benchmarkMastery: 65,
    enrolledLearners: 140,
    currentTopic: 'Term 1 Formal Assessment Review',
    nextMilestone: 'Term 2 Business Sectors Kickoff',
    weeklyTopics: [
      { week: 1, topic: 'Micro, Market & Macro Business Environments', status: 'completed', mastery: 68 },
      { week: 2, topic: 'Socio-Economic Issues Influencing Business', status: 'completed', mastery: 77 },
      { week: 3, topic: 'Social Responsibility & Corporate Citizenship', status: 'completed', mastery: 84 },
      { week: 4, topic: 'Forms of Ownership: Partnerships & Pty Ltd', status: 'completed', mastery: 76 },
      { week: 5, topic: 'Concept of Quality & TQM in Business Functions', status: 'completed', mastery: 79 },
      { week: 6, topic: 'Creative Thinking & Problem-Solving Techniques', status: 'completed', mastery: 82 },
      { week: 7, topic: 'Stress & Crisis Management in the Workplace', status: 'completed', mastery: 83 },
      { week: 8, topic: 'Transforming a Business Plan into an Action Plan', status: 'completed', mastery: 81 },
      { week: 9, topic: 'Gantt Charts & Project Planning Tools', status: 'completed', mastery: 80 },
      { week: 10, topic: 'Term 1 Formal Controlled Test Moderation', status: 'completed', mastery: 78 }
    ]
  },
  {
    id: 'atp-ems-8',
    subject: 'EMS',
    grade: '8',
    department: 'Senior Phase EMS',
    hod: 'Mrs. M. Naidoo',
    totalWeeks: 10,
    currentWeek: 8,
    status: 'on_track',
    statusLabel: 'Week 8 of 10 completed',
    curriculumCovered: 80,
    masteryDepth: 67,
    benchmarkMastery: 65,
    enrolledLearners: 215,
    currentTopic: 'Financial Literacy: Cash Receipts Journal (CRJ)',
    nextMilestone: 'Cash Payments Journal (CPJ) Postings',
    weeklyTopics: [
      { week: 1, topic: 'Government: Levels of Government & Roles', status: 'completed', mastery: 72 },
      { week: 2, topic: 'National Budget & Government Expenditure', status: 'completed', mastery: 68 },
      { week: 3, topic: 'Standard of Living & Modern vs Traditional Societies', status: 'completed', mastery: 76 },
      { week: 4, topic: 'Accounting Concepts: Assets, Liabilities & Equity', status: 'completed', mastery: 65 },
      { week: 5, topic: 'Source Documents: Receipts, Deposit Slips, Invoices', status: 'completed', mastery: 69 },
      { week: 6, topic: 'The Accounting Equation: Assets = Equity + Liabilities', status: 'completed', mastery: 64 },
      { week: 7, topic: 'Cash Receipts Journal (Services & Trading Business)', status: 'completed', mastery: 63 },
      { week: 8, topic: 'CRJ Analysis: Cost of Sales Calculation', status: 'in_progress', mastery: 65 },
      { week: 9, topic: 'Cash Payments Journal Setup & Cheque Counterfoils', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Controlled Examination', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-ems-9',
    subject: 'EMS',
    grade: '9',
    department: 'Senior Phase EMS',
    hod: 'Mrs. M. Naidoo',
    totalWeeks: 10,
    currentWeek: 8,
    status: 'on_track',
    statusLabel: 'Week 8 of 10 completed',
    curriculumCovered: 80,
    masteryDepth: 66,
    benchmarkMastery: 65,
    enrolledLearners: 198,
    currentTopic: 'Credit Transactions: Debtors & Creditors Journals',
    nextMilestone: 'Posting to General Ledger & Debtors Ledger',
    weeklyTopics: [
      { week: 1, topic: 'Economic Systems: Planned, Market & Mixed', status: 'completed', mastery: 75 },
      { week: 2, topic: 'Circular Flow Diagram: Households, Firms & State', status: 'completed', mastery: 71 },
      { week: 3, topic: 'Price Theory: Demand & Supply Schedules', status: 'completed', mastery: 68 },
      { week: 4, topic: 'Equilibrium Price & Market Shifts', status: 'completed', mastery: 63 },
      { week: 5, topic: 'Revision: CRJ and CPJ with Cost of Sales', status: 'completed', mastery: 67 },
      { week: 6, topic: 'Debtors Journal (Credit Sales & Invoices)', status: 'completed', mastery: 62 },
      { week: 7, topic: 'Debtors Allowance Journal (Credit Notes)', status: 'completed', mastery: 58 },
      { week: 8, topic: 'Creditors Journal (Credit Purchases)', status: 'in_progress', mastery: 65 },
      { week: 9, topic: 'General Ledger Balancing & Trial Balance', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Formal Controlled Test', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-math-7',
    subject: 'Mathematics',
    grade: '7',
    department: 'STEM',
    hod: 'Mr. S. Mokoena',
    totalWeeks: 10,
    currentWeek: 7,
    status: 'behind',
    statusLabel: '1 Week Behind (Week 7 of 10)',
    curriculumCovered: 70,
    masteryDepth: 61,
    benchmarkMastery: 65,
    enrolledLearners: 210,
    currentTopic: 'Common Fractions & Decimal Conversions',
    nextMilestone: 'Percentages & Financial Calculations',
    weeklyTopics: [
      { week: 1, topic: 'Whole Numbers: Commutative & Distributive Laws', status: 'completed', mastery: 70 },
      { week: 2, topic: 'Prime Factors, HCF and LCM', status: 'completed', mastery: 65 },
      { week: 3, topic: 'Exponents: Powers, Square Roots & Cube Roots', status: 'completed', mastery: 64 },
      { week: 4, topic: 'Geometry of 2D Shapes: Triangles & Angles', status: 'completed', mastery: 66 },
      { week: 5, topic: 'Angles: Acute, Right, Obtuse, Straight & Reflex', status: 'completed', mastery: 69 },
      { week: 6, topic: 'Common Fractions: Equivalent & Addition/Subtraction', status: 'completed', mastery: 57 },
      { week: 7, topic: 'Fraction Multiplication & Division of Fractions', status: 'in_progress', mastery: 53 },
      { week: 8, topic: 'Decimal Fractions: Place Value & Operations', status: 'scheduled', mastery: null },
      { week: 9, topic: 'Numeric & Geometric Patterns', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Controlled Assessment', status: 'scheduled', mastery: null }
    ]
  },
  {
    id: 'atp-ems-7',
    subject: 'EMS',
    grade: '7',
    department: 'Commercial Sciences',
    hod: 'Ms. Z. Ndlovu',
    totalWeeks: 10,
    currentWeek: 8,
    status: 'on_track',
    statusLabel: 'Week 8 of 10 completed',
    curriculumCovered: 80,
    masteryDepth: 72,
    benchmarkMastery: 65,
    enrolledLearners: 180,
    currentTopic: 'Financial Literacy: Personal Budgets & Savings',
    nextMilestone: 'Entrepreneurship: Characteristics of an Entrepreneur',
    weeklyTopics: [
      { week: 1, topic: 'The Economy: History of Money & Barter Trade', status: 'completed', mastery: 78 },
      { week: 2, topic: 'Role of Money & South African Currency Units', status: 'completed', mastery: 74 },
      { week: 3, topic: 'Needs and Wants: Basic Needs vs Secondary Wants', status: 'completed', mastery: 80 },
      { week: 4, topic: 'Goods and Services: Consumer vs Capital Goods', status: 'completed', mastery: 76 },
      { week: 5, topic: 'Businesses: Formal vs Informal Economic Sectors', status: 'completed', mastery: 71 },
      { week: 6, topic: 'Financial Literacy: Savings, Banks & Investments', status: 'completed', mastery: 69 },
      { week: 7, topic: 'Personal Budgets: Fixed vs Variable Income & Expenses', status: 'completed', mastery: 67 },
      { week: 8, topic: 'Preparation & Analysis of a Personal Budget', status: 'in_progress', mastery: 68 },
      { week: 9, topic: 'Entrepreneurship: Skills & Business Opportunities', status: 'scheduled', mastery: null },
      { week: 10, topic: 'Term 1 Formal Controlled Test', status: 'scheduled', mastery: null }
    ]
  }
];

// ==========================================
// STATIC DATA: TEACHING STAFF ROSTER
// ==========================================
const INITIAL_FACULTY_ROSTER = [
  {
    id: 'fac-1',
    name: 'Mr. N. Sithole',
    role: 'HOD Commerce & Accounting Lead',
    email: 'n.sithole@fundile.school.za',
    phone: '+27 82 459 1042',
    subject: 'Accounting',
    department: 'Commerce',
    grades: 'Gr 10–12',
    activeClasses: ['10A', '10B', '11A', '12A'],
    totalClassesCount: 4,
    enrolledLearners: 148,
    classAverageMastery: 68.4,
    capsLevel: 5,
    pacingStatus: 'On Track',
    atpProgress: 85,
    avatarColor: 'bg-blue-600'
  },
  {
    id: 'fac-2',
    name: 'Mrs. P. Khumalo',
    role: 'Senior Educator & STEM Head',
    email: 'p.khumalo@fundile.school.za',
    phone: '+27 83 912 3401',
    subject: 'Mathematics',
    department: 'STEM',
    grades: 'Gr 10–11',
    activeClasses: ['10A', '10C', '11A', '11B', '11C'],
    totalClassesCount: 5,
    enrolledLearners: 182,
    classAverageMastery: 62.1,
    capsLevel: 5,
    pacingStatus: 'On Track',
    atpProgress: 80,
    avatarColor: 'bg-emerald-600'
  },
  {
    id: 'fac-3',
    name: 'Dr. T. van der Merwe',
    role: 'HOD Physical Sciences',
    email: 't.vandermerwe@fundile.school.za',
    phone: '+27 82 890 2311',
    subject: 'Physical Sciences',
    department: 'Sciences',
    grades: 'Gr 10–12',
    activeClasses: ['10A', '11A', '12A', '12B'],
    totalClassesCount: 4,
    enrolledLearners: 136,
    classAverageMastery: 59.8,
    capsLevel: 4,
    pacingStatus: '1 Week Behind',
    atpProgress: 75,
    avatarColor: 'bg-purple-600'
  },
  {
    id: 'fac-4',
    name: 'Ms. B. Dlamini',
    role: 'Senior Educator Life Sciences',
    email: 'b.dlamini@fundile.school.za',
    phone: '+27 84 551 8820',
    subject: 'Life Sciences',
    department: 'Sciences',
    grades: 'Gr 10–12',
    activeClasses: ['10B', '11A', '11B', '12A'],
    totalClassesCount: 4,
    enrolledLearners: 154,
    classAverageMastery: 71.2,
    capsLevel: 6,
    pacingStatus: 'On Track',
    atpProgress: 88,
    avatarColor: 'bg-teal-600'
  },
  {
    id: 'fac-5',
    name: 'Mr. K. Pillay',
    role: 'Senior Educator Business Studies',
    email: 'k.pillay@fundile.school.za',
    phone: '+27 83 234 9012',
    subject: 'Business Studies',
    department: 'Commerce',
    grades: 'Gr 10–12',
    activeClasses: ['10A', '10C', '11B', '12A'],
    totalClassesCount: 4,
    enrolledLearners: 140,
    classAverageMastery: 65.7,
    capsLevel: 5,
    pacingStatus: 'Completed Term 1 ATP',
    atpProgress: 100,
    avatarColor: 'bg-cyan-600'
  },
  {
    id: 'fac-6',
    name: 'Mrs. M. Naidoo',
    role: 'HOD Senior Phase EMS',
    email: 'm.naidoo@fundile.school.za',
    phone: '+27 81 776 5432',
    subject: 'EMS',
    department: 'Senior Phase EMS',
    grades: 'Gr 7–9',
    activeClasses: ['7A', '7B', '8A', '8B', '9A', '9B'],
    totalClassesCount: 6,
    enrolledLearners: 215,
    classAverageMastery: 66.8,
    capsLevel: 5,
    pacingStatus: 'On Track',
    atpProgress: 82,
    avatarColor: 'bg-amber-600'
  },
  {
    id: 'fac-7',
    name: 'Mr. S. Mokoena',
    role: 'Senior Phase Mathematics Lead',
    email: 's.mokoena@fundile.school.za',
    phone: '+27 82 311 9845',
    subject: 'Mathematics',
    department: 'STEM',
    grades: 'Gr 7–9',
    activeClasses: ['7A', '8A', '8C', '9A', '9B'],
    totalClassesCount: 5,
    enrolledLearners: 192,
    classAverageMastery: 60.5,
    capsLevel: 5,
    pacingStatus: '1 Week Behind',
    atpProgress: 72,
    avatarColor: 'bg-indigo-600'
  },
  {
    id: 'fac-8',
    name: 'Ms. Z. Cele',
    role: 'Commerce Educator',
    email: 'z.cele@fundile.school.za',
    phone: '+27 83 671 2004',
    subject: 'Accounting & Business Studies',
    department: 'Commerce',
    grades: 'Gr 10–11',
    activeClasses: ['10C', '11C', '11D'],
    totalClassesCount: 3,
    enrolledLearners: 110,
    classAverageMastery: 63.9,
    capsLevel: 5,
    pacingStatus: 'On Track',
    atpProgress: 80,
    avatarColor: 'bg-sky-600'
  }
];

// ==========================================
// STATIC DATA: SYSTEMIC MISCONCEPTIONS
// ==========================================
const INITIAL_MISCONCEPTIONS = [
  {
    id: 'misc-acc-10',
    grade: '10',
    subject: 'Accounting',
    title: 'Output VAT Inversion on Debtors Allowances & Credit Sales',
    summary: '41% of students failed Output VAT on credit sales and allowances.',
    diagnosticStats: '41% failure rate • 61 of 148 learners flagged',
    severity: 'critical',
    severityLabel: 'Critical Bottleneck (41% Error)',
    affectedClasses: ['10A', '10B', '10C'],
    affectedCount: 148,
    capsWeighting: '25 Marks (Paper 1)',
    explanation: 'Learners mistakenly treat Output VAT on Debtors Allowance as an Input VAT credit claim rather than a reversal of the Output VAT liability to SARS, reversing debit/credit ledger polarity.',
    remedialDrillTitle: '5-Min Fast-Track: Output VAT Debtors Allowance Reversals',
    drillQuestions: [
      {
        q: 'When a debtor returns goods with original VAT invoiced at R150, which VAT account is debited in the general ledger?',
        options: ['Input VAT Account', 'Output VAT Account', 'Debtors Control Account', 'SARS (Income Tax) Account'],
        answer: 'Output VAT Account',
        explanation: 'Output VAT is reduced (debited) to reverse the sales tax liability previously declared on the original invoice.'
      },
      {
        q: 'A credit invoice shows goods sold for R1,150 including 15% VAT. What is the Output VAT amount payable to SARS?',
        options: ['R172.50', 'R150.00', 'R115.00', 'R135.00'],
        answer: 'R150.00',
        explanation: 'VAT = R1,150 * 15 / 115 = R150.00.'
      },
      {
        q: 'In which primary journal is a Credit Note issued to an unsatisfied customer recorded?',
        options: ['Debtors Journal (DJ)', 'Debtors Allowances Journal (DAJ)', 'Cash Receipts Journal (CRJ)', 'Creditors Allowances Journal (CAJ)'],
        answer: 'Debtors Allowances Journal (DAJ)',
        explanation: 'Credit notes issued to debtors for returned damaged goods are recorded in the DAJ.'
      }
    ],
    educatorTalkingPoints: 'Remind classes before Period 1: "Output VAT belongs to SARS. When goods come back, we owe SARS LESS, so we debit Output VAT."'
  },
  {
    id: 'misc-math-11',
    grade: '11',
    subject: 'Mathematics',
    title: 'Non-Right-Angled Trig Ambiguity (Sine vs Cosine Rules)',
    summary: '38% error rate on Non-Right-Angled Trig (Sine & Cosine Rules).',
    diagnosticStats: '38% error rate • 69 of 182 learners flagged',
    severity: 'high',
    severityLabel: 'High Alert (38% Error)',
    affectedClasses: ['11A', '11B', '11C'],
    affectedCount: 182,
    capsWeighting: '20 Marks (Paper 2)',
    explanation: 'Learners attempt to apply standard SOH-CAH-TOA definitions to scalene/oblique triangles without identifying whether they have SAS (Cosine Rule) or AAS/SSA (Sine Rule).',
    remedialDrillTitle: '5-Min Diagnostic: Oblique Triangle Rule Discriminator',
    drillQuestions: [
      {
        q: 'In triangle ABC, side a = 8 cm, side b = 11 cm, and included angle C = 62°. Which rule must be used to calculate side c?',
        options: ['Sine Rule', 'Cosine Rule', 'Area Rule', 'Pythagoras Theorem'],
        answer: 'Cosine Rule',
        explanation: 'Two sides and the included angle (SAS) directly mandates the Cosine Rule: c² = a² + b² - 2ab*cos(C).'
      },
      {
        q: 'Under what specific conditions can the Sine Rule yield two valid triangle solutions (the ambiguous case)?',
        options: ['When given 3 sides (SSS)', 'When given SSA where the side opposite the angle is shorter than the adjacent side', 'When given two angles and one side (AAS)', 'When all angles are obtuse'],
        answer: 'When given SSA where the side opposite the angle is shorter than the adjacent side',
        explanation: 'The ambiguous SSA case produces two potential triangles if sin(B) < 1 and the opposite side permits acute or obtuse supplements.'
      }
    ],
    educatorTalkingPoints: 'Emphasize the SAS test: If the given angle is pinched between the two given sides, always reach for the Cosine Rule first.'
  },
  {
    id: 'misc-phys-12',
    grade: '12',
    subject: 'Physical Sciences',
    title: 'Internal Resistance & EMF Confusion (Lost Volts Under Load)',
    summary: '46% confusion between Electric Potential (Terminal pd) and EMF in Internal Resistance circuits.',
    diagnosticStats: '46% failure rate • 62 of 136 learners flagged',
    severity: 'critical',
    severityLabel: 'Critical Bottleneck (46% Error)',
    affectedClasses: ['12A', '12B'],
    affectedCount: 136,
    capsWeighting: '18 Marks (Paper 1 Physics)',
    explanation: 'Students assume battery terminal voltage V_load equals EMF ε at all times, failing to recognize that when current flows, V_lost = I*r causes the external voltage reading to drop.',
    remedialDrillTitle: '5-Min Focus: Lost Volts & Internal Battery Resistance',
    drillQuestions: [
      {
        q: 'A battery has EMF of 12 V and internal resistance 0.5 Ω. When connected to a 5.5 Ω external resistor, what is the terminal potential difference across the battery?',
        options: ['12.0 V', '11.0 V', '1.0 V', '6.0 V'],
        answer: '11.0 V',
        explanation: 'Total R = 5.5 + 0.5 = 6 Ω. I = 12 / 6 = 2 A. Terminal V = EMF - Ir = 12 - (2 * 0.5) = 11.0 V.'
      },
      {
        q: 'When the switch in a parallel branch is closed (adding another parallel resistor), what happens to the reading on a voltmeter connected across the battery terminals?',
        options: ['Increases', 'Decreases', 'Remains unchanged', 'Drops immediately to zero'],
        answer: 'Decreases',
        explanation: 'Closing the switch lowers total external resistance, increasing main circuit current I. Therefore, lost volts (Ir) increases, reducing terminal voltage V = ε - Ir.'
      }
    ],
    educatorTalkingPoints: 'Demonstrate with a real cell and multimeter: show the voltage drop the exact moment current begins flowing through an incandescent bulb.'
  },
  {
    id: 'misc-ems-9',
    grade: '9',
    subject: 'EMS',
    title: 'Cash vs Credit Transaction Isolation in Debtors Journal',
    summary: '35% error rate distinguishing Cash vs Credit Transactions in the Debtors Journal.',
    diagnosticStats: '35% error rate • 75 of 215 learners flagged',
    severity: 'moderate',
    severityLabel: 'Moderate Alert (35% Error)',
    affectedClasses: ['9A', '9B', '9C'],
    affectedCount: 215,
    capsWeighting: '30 Marks (June Assessment)',
    explanation: 'Learners enter cash sales transactions into the Debtors Journal (DJ) whenever customer names are mentioned on invoices, instead of routing cash receipts strictly to the CRJ.',
    remedialDrillTitle: '5-Min Drill: Source Document Routing (DJ vs CRJ)',
    drillQuestions: [
      {
        q: 'Goods sold to customer K. Adams for R800. Customer pays R300 cash deposit and the balance on 30-day credit. Where is the R300 deposit recorded?',
        options: ['Debtors Journal (DJ)', 'Cash Receipts Journal (CRJ)', 'Creditors Journal (CJ)', 'General Journal (GJ)'],
        answer: 'Cash Receipts Journal (CRJ)',
        explanation: 'Any actual cash received goes into the CRJ with a receipt/cash slip reference; only the R500 credit portion goes into the DJ.'
      }
    ],
    educatorTalkingPoints: 'Teach the "Cash in Hand" test: If money touched the till, it goes to CRJ; if only a promise and invoice changed hands, it goes to DJ.'
  },
  {
    id: 'misc-life-12',
    grade: '12',
    subject: 'Life Sciences',
    title: 'Meiosis Non-Disjunction & Karyotype Diagnostic Errors',
    summary: '43% misconceptions in Meiosis I vs Meiosis II non-disjunction errors.',
    diagnosticStats: '43% error rate • 66 of 154 learners flagged',
    severity: 'critical',
    severityLabel: 'Critical Bottleneck (43% Error)',
    affectedClasses: ['12A', '12B'],
    affectedCount: 154,
    capsWeighting: '15 Marks (Paper 1)',
    explanation: 'Students fail to differentiate gamete outcomes: non-disjunction in Anaphase I yields 100% abnormal gametes (n+1, n+1, n-1, n-1), whereas non-disjunction in Anaphase II yields 50% normal gametes (n, n, n+1, n-1).',
    remedialDrillTitle: '5-Min Micro-Drill: Karyotype & Gamete Disjunction Ratios',
    drillQuestions: [
      {
        q: 'If non-disjunction occurs in Meiosis I during oogenesis, what proportion of the resulting gametes will carry an abnormal chromosome number?',
        options: ['25%', '50%', '75%', '100%'],
        answer: '100%',
        explanation: 'Failure of homologous pairs to separate in Anaphase I produces two (n+1) and two (n-1) gametes—100% abnormal.'
      }
    ],
    educatorTalkingPoints: 'Draw the two-cell fork on the board: show homologous pairs failing vs sister chromatids failing.'
  },
  {
    id: 'misc-bus-11',
    grade: '11',
    subject: 'Business Studies',
    title: 'Macro vs Market Environmental Force Classification',
    summary: '32% difficulty differentiating Micro, Market, and Macro environmental forces.',
    diagnosticStats: '32% error rate • 45 of 140 learners flagged',
    severity: 'moderate',
    severityLabel: 'Moderate Alert (32% Error)',
    affectedClasses: ['11A', '11B'],
    affectedCount: 140,
    capsWeighting: '16 Marks (Paper 1)',
    explanation: 'Learners misclassify trade unions and suppliers under the internal micro environment, and conflate government tax policy with industry market forces.',
    remedialDrillTitle: '5-Min Drill: Business Environment Boundary Classifier',
    drillQuestions: [
      {
        q: 'Under which business environment do Suppliers and Competitors fall?',
        options: ['Micro Environment', 'Market Environment', 'Macro Environment', 'Global Environment'],
        answer: 'Market Environment',
        explanation: 'Market environment consists of external entities with which the firm directly interacts and can influence, but cannot fully control (suppliers, competitors, customers).'
      }
    ],
    educatorTalkingPoints: 'Remind learners: Micro = full control; Market = influence without control; Macro = zero control, only adaptation.'
  }
];

// ==========================================
// STATIC DATA: SASAMS STUDENT MARKS DATASET
// ==========================================
const INITIAL_STUDENT_MARKS = [
  { id: 'st-01', emis: '700142981', lurits: '2009041289081', surname: 'Mahlangu', firstName: 'Bandile', grade: '10', class: '10A', subject: 'Accounting', formativeScore: 84, formalExamScore: 78, termMark: 80, capsLevel: 7 },
  { id: 'st-02', emis: '700142981', lurits: '2009081903082', surname: 'Khumalo', firstName: 'Siphesihle', grade: '10', class: '10A', subject: 'Accounting', formativeScore: 66, formalExamScore: 68, termMark: 67, capsLevel: 5 },
  { id: 'st-03', emis: '700142981', lurits: '2009012394083', surname: 'Dlamini', firstName: 'Noluthando', grade: '10', class: '10B', subject: 'Accounting', formativeScore: 54, formalExamScore: 52, termMark: 53, capsLevel: 4 },
  { id: 'st-04', emis: '700142981', lurits: '2009051187084', surname: 'van Wyk', firstName: 'Pieter', grade: '10', class: '10B', subject: 'Accounting', formativeScore: 72, formalExamScore: 74, termMark: 73, capsLevel: 6 },
  { id: 'st-05', emis: '700142981', lurits: '2009110482085', surname: 'Naidoo', firstName: 'Priyesh', grade: '10', class: '10C', subject: 'Accounting', formativeScore: 38, formalExamScore: 41, termMark: 40, capsLevel: 3 },
  { id: 'st-06', emis: '700142981', lurits: '2009071489086', surname: 'Mokoena', firstName: 'Thabo', grade: '10', class: '10A', subject: 'Mathematics', formativeScore: 70, formalExamScore: 68, termMark: 69, capsLevel: 5 },
  { id: 'st-07', emis: '700142981', lurits: '2009022881087', surname: 'Molefe', firstName: 'Lerato', grade: '10', class: '10A', subject: 'Mathematics', formativeScore: 82, formalExamScore: 86, termMark: 84, capsLevel: 7 },
  { id: 'st-08', emis: '700142981', lurits: '2009091986088', surname: 'Sithole', firstName: 'Katlego', grade: '10', class: '10C', subject: 'Mathematics', formativeScore: 48, formalExamScore: 45, termMark: 46, capsLevel: 3 },
  { id: 'st-09', emis: '700142981', lurits: '2008061285089', surname: 'Zondi', firstName: 'Anele', grade: '11', class: '11A', subject: 'Mathematics', formativeScore: 62, formalExamScore: 58, termMark: 60, capsLevel: 5 },
  { id: 'st-10', emis: '700142981', lurits: '2008101484090', surname: 'Baloyi', firstName: 'Nthabiseng', grade: '11', class: '11A', subject: 'Mathematics', formativeScore: 51, formalExamScore: 47, termMark: 49, capsLevel: 3 },
  { id: 'st-11', emis: '700142981', lurits: '2008032183091', surname: 'Pillay', firstName: 'Devan', grade: '11', class: '11B', subject: 'Mathematics', formativeScore: 76, formalExamScore: 74, termMark: 75, capsLevel: 6 },
  { id: 'st-12', emis: '700142981', lurits: '2008120982092', surname: 'Ndlovu', firstName: 'Luyanda', grade: '11', class: '11C', subject: 'Mathematics', formativeScore: 32, formalExamScore: 34, termMark: 33, capsLevel: 2 },
  { id: 'st-13', emis: '700142981', lurits: '2008051781093', surname: 'Cele', firstName: 'Mbali', grade: '11', class: '11A', subject: 'Accounting', formativeScore: 88, formalExamScore: 85, termMark: 86, capsLevel: 7 },
  { id: 'st-14', emis: '700142981', lurits: '2008092580094', surname: 'Govender', firstName: 'Kiran', grade: '11', class: '11A', subject: 'Accounting', formativeScore: 65, formalExamScore: 63, termMark: 64, capsLevel: 5 },
  { id: 'st-15', emis: '700142981', lurits: '2007041189095', surname: 'Mabaso', firstName: 'Sibusiso', grade: '12', class: '12A', subject: 'Mathematics', formativeScore: 92, formalExamScore: 90, termMark: 91, capsLevel: 7 },
  { id: 'st-16', emis: '700142981', lurits: '2007081588096', surname: 'Botha', firstName: 'Hendrik', grade: '12', class: '12A', subject: 'Physical Sciences', formativeScore: 68, formalExamScore: 65, termMark: 66, capsLevel: 5 },
  { id: 'st-17', emis: '700142981', lurits: '2007011987097', surname: 'Tshabalala', firstName: 'Zanele', grade: '12', class: '12B', subject: 'Physical Sciences', formativeScore: 54, formalExamScore: 49, termMark: 51, capsLevel: 4 },
  { id: 'st-18', emis: '700142981', lurits: '2007112286098', surname: 'Chauke', firstName: 'Blessing', grade: '12', class: '12A', subject: 'Life Sciences', formativeScore: 78, formalExamScore: 82, termMark: 80, capsLevel: 7 },
  { id: 'st-19', emis: '700142981', lurits: '2007063085099', surname: 'Sibanda', firstName: 'Kudakwashe', grade: '12', class: '12B', subject: 'Life Sciences', formativeScore: 71, formalExamScore: 69, termMark: 70, capsLevel: 6 },
  { id: 'st-20', emis: '700142981', lurits: '2008021484100', surname: 'Nkosi', firstName: 'Nonhlanhla', grade: '11', class: '11B', subject: 'Business Studies', formativeScore: 67, formalExamScore: 65, termMark: 66, capsLevel: 5 },
  { id: 'st-21', emis: '700142981', lurits: '2008070883101', surname: 'Du Toit', firstName: 'Anika', grade: '11', class: '11B', subject: 'Business Studies', formativeScore: 85, formalExamScore: 87, termMark: 86, capsLevel: 7 },
  { id: 'st-22', emis: '700142981', lurits: '2010031882102', surname: 'Hlatshwayo', firstName: 'Sipho', grade: '9', class: '9A', subject: 'EMS', formativeScore: 64, formalExamScore: 62, termMark: 63, capsLevel: 5 },
  { id: 'st-23', emis: '700142981', lurits: '2010092981103', surname: 'Moodley', firstName: 'Jessica', grade: '9', class: '9B', subject: 'EMS', formativeScore: 78, formalExamScore: 80, termMark: 79, capsLevel: 6 },
  { id: 'st-24', emis: '700142981', lurits: '2011051480104', surname: 'Zulu', firstName: 'Mandla', grade: '8', class: '8A', subject: 'EMS', formativeScore: 71, formalExamScore: 67, termMark: 69, capsLevel: 5 },
  { id: 'st-25', emis: '700142981', lurits: '2012011179105', surname: 'Masango', firstName: 'Onkabetse', grade: '7', class: '7A', subject: 'Mathematics', formativeScore: 58, formalExamScore: 54, termMark: 56, capsLevel: 4 }
];

// Helper to determine CAPS Level
const getCapsLevel = (mark) => {
  if (mark >= 80) return { level: 7, label: 'Outstanding', badge: 'bg-emerald-50 text-emerald-700 border-emerald-200' };
  if (mark >= 70) return { level: 6, label: 'Meritorious', badge: 'bg-blue-50 text-blue-700 border-blue-200' };
  if (mark >= 60) return { level: 5, label: 'Substantial', badge: 'bg-cyan-50 text-cyan-700 border-cyan-200' };
  if (mark >= 50) return { level: 4, label: 'Adequate', badge: 'bg-sky-50 text-sky-700 border-sky-200' };
  if (mark >= 40) return { level: 3, label: 'Moderate', badge: 'bg-amber-50 text-amber-700 border-amber-200' };
  if (mark >= 30) return { level: 2, label: 'Elementary', badge: 'bg-orange-50 text-orange-700 border-orange-200' };
  return { level: 1, label: 'Not Achieved', badge: 'bg-rose-50 text-rose-700 border-rose-200' };
};

// =========================================================
// STATIC DATA: ACCESS BANK PROOF OF PAYMENT SUBMISSIONS
// =========================================================
const INITIAL_POP_SUBMISSIONS = [
  {
    id: 'pop-1',
    learnerName: 'Nqobile Dlamini',
    email: 'nqobile.d@phakamani.edu.za',
    phone: '+27 82 555 4192',
    grade: 'Grade 10 FET',
    uploadDateTime: 'Today, 14:22',
    planName: 'Fundile Pro',
    planCycle: 'Monthly',
    amount: 'R149.00',
    targetBank: 'Access Bank • Acc ...9104',
    accountNumber: '410 882 9104',
    branchCode: '410506',
    reference: 'FUN-892104',
    status: 'approved', // 'approved' | 'grace' | 'flagged' | 'rejected'
    daysGranted: 30,
    aiConfidence: 95,
    aiVerdict: 'approved',
    aiBadgeText: 'AI Verified (95% Confidence) • Auto-Approved',
    aiNotes: 'Access Bank electronic funds transfer receipt verified. Reference FUN-892104 and R149.00 match expected invoice.',
    depositDate: '28 Sep 2026',
    receiptFileName: 'AccessBank_EFT_FUN892104.pdf'
  },
  {
    id: 'pop-2',
    learnerName: 'Sipho Khumalo',
    email: 's.khumalo@westville.ac.za',
    phone: '+27 73 890 1144',
    grade: 'Grade 8 GET',
    uploadDateTime: 'Today, 11:05',
    planName: 'Fundile Pro',
    planCycle: 'Monthly',
    amount: 'R149.00',
    targetBank: 'Access Bank • Acc ...9104',
    accountNumber: '410 882 9104',
    branchCode: '410506',
    reference: 'FUN-410928',
    status: 'grace',
    daysGranted: 14,
    aiConfidence: 68,
    aiVerdict: 'needs_review',
    aiBadgeText: 'Grace Period Active (68% Confidence) • Needs Verification',
    aiNotes: 'Mobile banking transfer receipt timestamp valid. Account 4108829104 confirmed. Reference OCR partial match. Awaiting bank statement line confirmation.',
    depositDate: '28 Sep 2026',
    receiptFileName: 'Capitec_To_AccessBank_Slip.png'
  },
  {
    id: 'pop-3',
    learnerName: 'Thabo Molefe',
    email: 'thabo.m@sowetofet.co.za',
    phone: '+27 81 442 0981',
    grade: 'Grade 11 FET',
    uploadDateTime: 'Yesterday, 16:45',
    planName: 'Fundile Standard',
    planCycle: 'Monthly',
    amount: 'R79.00',
    targetBank: 'Access Bank • Acc ...9104',
    accountNumber: '410 882 9104',
    branchCode: '410506',
    reference: 'FUN-772190',
    status: 'flagged',
    daysGranted: 14,
    aiConfidence: 28,
    aiVerdict: 'flagged',
    aiBadgeText: 'Flagged (28% Confidence) • Wrong Recipient / Blurry',
    aiNotes: 'Receipt shows funds paid to Standard Bank account instead of Access Bank. Potential mismatched recipient or illegible slip image.',
    depositDate: '27 Sep 2026',
    receiptFileName: 'Photo_Receipt_WhatsApp.jpg'
  },
  {
    id: 'pop-4',
    learnerName: 'Lindiwe Ndlovu',
    email: 'lindiwe.n@phakamani.edu.za',
    phone: '+27 84 901 8832',
    grade: 'Grade 12 FET',
    uploadDateTime: '26 Sep 2026',
    planName: 'Fundile Pro',
    planCycle: 'Annual',
    amount: 'R1,428.00',
    targetBank: 'Access Bank • Acc ...9104',
    accountNumber: '410 882 9104',
    branchCode: '410506',
    reference: 'FUN-309114',
    status: 'approved',
    daysGranted: 365,
    aiConfidence: 98,
    aiVerdict: 'approved',
    aiBadgeText: 'AI Verified (98% Confidence) • Auto-Approved',
    aiNotes: 'Access Bank business account credit statement verified for R1,428.00 with reference FUN-309114. Full 365-day annual term unlocked.',
    depositDate: '26 Sep 2026',
    receiptFileName: 'AccessBank_DirectCredit_309114.pdf'
  }
];

const SchoolAdminView = ({ currentUser, onBack }) => {
  // Authorization Gate
  const canAccessSchoolAdmin = !!(
    currentUser?.isOwner ||
    currentUser?.isSuperAdmin ||
    currentUser?.isSchoolAdmin ||
    currentUser?.role === 'admin' ||
    currentUser?.role === 'principal' ||
    currentUser?.role === 'school' ||
    currentUser?.role === 'school_admin' ||
    currentUser?.role === 'schoolAdmin'
  );

  // Core Navigation Tabs
  const [activeTab, setActiveTab] = useState('pacing'); // 'pacing' | 'faculty' | 'misconceptions' | 'sasams'
  const [selectedTerm, setSelectedTerm] = useState(1);
  const [toastMessage, setToastMessage] = useState(null);

  // ATP Heatmap Module State
  const [pacingGradeFilter, setPacingGradeFilter] = useState('all');
  const [pacingSubjectFilter, setPacingSubjectFilter] = useState('all');
  const [inspectingSubject, setInspectingSubject] = useState(null);
  const [interventionRequested, setInterventionRequested] = useState({});

  // Faculty Module State
  const [facultyRoster, setFacultyRoster] = useState(INITIAL_FACULTY_ROSTER);
  const [facultySearch, setFacultySearch] = useState('');
  const [facultyDeptFilter, setFacultyDeptFilter] = useState('all');
  const [isInviteModalOpen, setIsInviteModalOpen] = useState(false);
  const [copiedInviteLink, setCopiedInviteLink] = useState(false);
  const [inviteForm, setInviteForm] = useState({
    name: '',
    email: '',
    department: 'Commerce',
    subject: 'Accounting',
    grades: 'Gr 10–12'
  });

  // Misconception Broadcast Module State
  const [misconceptions] = useState(INITIAL_MISCONCEPTIONS);
  const [misconceptionGradeFilter, setMisconceptionGradeFilter] = useState('all');
  const [broadcastedDrills, setBroadcastedDrills] = useState({});
  const [activePreviewDrill, setActivePreviewDrill] = useState(null);

  // SASAMS Mark Collation Module State
  const [marksData] = useState(INITIAL_STUDENT_MARKS);
  const [sasamsGradeFilter, setSasamsGradeFilter] = useState('all');
  const [sasamsSubjectFilter, setSasamsSubjectFilter] = useState('all');
  const [sasamsLevelFilter, setSasamsLevelFilter] = useState('all');
  const [sasamsSearch, setSasamsSearch] = useState('');
  const [isExporting, setIsExporting] = useState(false);

  // POP Audit & Reconciliation State
  const [popSubmissions, setPopSubmissions] = useState(INITIAL_POP_SUBMISSIONS);
  const [popStatusFilter, setPopStatusFilter] = useState('all');
  const [popSearch, setPopSearch] = useState('');
  const [selectedSlipModal, setSelectedSlipModal] = useState(null);

  // Toast Notification Helper
  const showToast = (text, type = 'success') => {
    setToastMessage({ text, type, id: Date.now() });
    setTimeout(() => {
      setToastMessage((prev) => (prev?.id ? null : prev));
    }, 4500);
  };

  // POP Reconciliation Handlers
  const handleConfirmAndUnlock = (submissionId) => {
    setPopSubmissions((prev) =>
      prev.map((sub) =>
        sub.id === submissionId
          ? {
              ...sub,
              status: 'approved',
              aiVerdict: 'approved',
              aiBadgeText: 'Manual Verified • Approved',
              daysGranted: sub.planCycle === 'Annual' ? 365 : 30,
            }
          : sub
      )
    );
    showToast('✅ Access Bank Transfer Confirmed! Pro Access Unlocked for Learner.', 'success');
    if (selectedSlipModal?.id === submissionId) {
      setSelectedSlipModal(null);
    }
  };

  const handleRejectAndRevoke = (submissionId) => {
    setPopSubmissions((prev) =>
      prev.map((sub) =>
        sub.id === submissionId
          ? {
              ...sub,
              status: 'rejected',
              aiVerdict: 'rejected',
              aiBadgeText: 'Rejected & Access Revoked',
              daysGranted: 0,
            }
          : sub
      )
    );
    showToast('❌ POP Slip Rejected: Learner Grace Period Revoked.', 'error');
    if (selectedSlipModal?.id === submissionId) {
      setSelectedSlipModal(null);
    }
  };

  const filteredPopSubmissions = useMemo(() => {
    return popSubmissions.filter((sub) => {
      const matchesFilter =
        popStatusFilter === 'all'
          ? true
          : popStatusFilter === 'pending'
          ? sub.status === 'grace' || sub.status === 'flagged'
          : sub.status === popStatusFilter;
      const q = popSearch.toLowerCase();
      const matchesSearch =
        !q ||
        sub.learnerName.toLowerCase().includes(q) ||
        sub.reference.toLowerCase().includes(q) ||
        sub.email.toLowerCase().includes(q);
      return matchesFilter && matchesSearch;
    });
  }, [popSubmissions, popStatusFilter, popSearch]);

  // Filtered ATP Pacing Data
  const filteredPacingData = useMemo(() => {
    return ATP_PACING_DATA.filter((item) => {
      const matchGrade = pacingGradeFilter === 'all' || item.grade === pacingGradeFilter;
      const matchSubject = pacingSubjectFilter === 'all' || item.subject === pacingSubjectFilter;
      return matchGrade && matchSubject;
    });
  }, [pacingGradeFilter, pacingSubjectFilter]);

  // Overall Departmental Pacing Metrics
  const pacingStats = useMemo(() => {
    const total = ATP_PACING_DATA.length;
    const onTrack = ATP_PACING_DATA.filter((i) => i.status === 'on_track').length;
    const behind = ATP_PACING_DATA.filter((i) => i.status === 'behind').length;
    const completed = ATP_PACING_DATA.filter((i) => i.status === 'completed').length;
    const avgMastery = Math.round(
      ATP_PACING_DATA.reduce((acc, curr) => acc + curr.masteryDepth, 0) / total
    );
    const benchmarkCoveredPercent = Math.round(
      (ATP_PACING_DATA.filter((i) => i.masteryDepth >= i.benchmarkMastery).length / total) * 100
    );

    return { total, onTrack, behind, completed, avgMastery, benchmarkCoveredPercent };
  }, []);

  // Filtered Faculty Roster
  const filteredFaculty = useMemo(() => {
    return facultyRoster.filter((member) => {
      const matchDept = facultyDeptFilter === 'all' || member.department === facultyDeptFilter;
      const matchSearch =
        facultySearch === '' ||
        member.name.toLowerCase().includes(facultySearch.toLowerCase()) ||
        member.subject.toLowerCase().includes(facultySearch.toLowerCase()) ||
        member.email.toLowerCase().includes(facultySearch.toLowerCase());
      return matchDept && matchSearch;
    });
  }, [facultyRoster, facultyDeptFilter, facultySearch]);

  // Filtered Misconceptions
  const filteredMisconceptions = useMemo(() => {
    return misconceptions.filter((m) => {
      return misconceptionGradeFilter === 'all' || m.grade === misconceptionGradeFilter;
    });
  }, [misconceptions, misconceptionGradeFilter]);

  // Filtered SASAMS Marks
  const filteredMarks = useMemo(() => {
    return marksData.filter((item) => {
      const matchGrade = sasamsGradeFilter === 'all' || item.grade === sasamsGradeFilter;
      const matchSubject = sasamsSubjectFilter === 'all' || item.subject === sasamsSubjectFilter;
      const matchLevel =
        sasamsLevelFilter === 'all' ||
        (sasamsLevelFilter === '7' && item.capsLevel === 7) ||
        (sasamsLevelFilter === 'pass' && item.capsLevel >= 4) ||
        (sasamsLevelFilter === 'atRisk' && item.capsLevel <= 2);
      const matchSearch =
        sasamsSearch === '' ||
        `${item.firstName} ${item.surname}`.toLowerCase().includes(sasamsSearch.toLowerCase()) ||
        item.lurits.includes(sasamsSearch) ||
        item.class.toLowerCase().includes(sasamsSearch.toLowerCase());
      return matchGrade && matchSubject && matchLevel && matchSearch;
    });
  }, [marksData, sasamsGradeFilter, sasamsSubjectFilter, sasamsLevelFilter, sasamsSearch]);

  // SASAMS Summary Analytics
  const sasamsAnalytics = useMemo(() => {
    const total = filteredMarks.length;
    if (total === 0) return { count: 0, average: 0, passRate: 0, distinctionRate: 0 };
    const sum = filteredMarks.reduce((acc, curr) => acc + curr.termMark, 0);
    const average = (sum / total).toFixed(1);
    const passes = filteredMarks.filter((m) => m.capsLevel >= 4).length;
    const distinctions = filteredMarks.filter((m) => m.capsLevel === 7).length;
    const passRate = ((passes / total) * 100).toFixed(1);
    const distinctionRate = ((distinctions / total) * 100).toFixed(1);

    return { count: total, average, passRate, distinctionRate };
  }, [filteredMarks]);

  // Handle Misconception Drill Broadcast
  const handleBroadcastRemedialDrill = (misc) => {
    const timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    setBroadcastedDrills((prev) => ({
      ...prev,
      [misc.id]: {
        timestamp,
        enrolledCount: misc.affectedCount,
        classes: misc.affectedClasses.join(', ')
      }
    }));
    try {
      studentStore.addMessage({
        sender: 'School Academic Head',
        senderRole: 'School Admin',
        subject: misc.subject || 'Academic Broadcast',
        text: `School-wide Remedial Drill: ${misc.label || misc.misconception} broadcasted to Grade ${misc.grade} (${misc.affectedClasses.join(', ')}). Deadline in 3 days.`,
        deadline: new Date(Date.now() + 86400000 * 3).toISOString()
      });
    } catch (e) {
      console.warn('Could not post school broadcast to studentStore:', e);
    }
    showToast(
      `Remedial micro-drill dispatched to ${misc.affectedCount} Grade ${misc.grade} learners across ${misc.affectedClasses.join(', ')}!`,
      'success'
    );
  };

  // Handle Copy Faculty Join Link
  const handleCopyFacultyLink = () => {
    const inviteUrl = 'https://fundile.app/join/faculty?school=FundileHigh&token=FD-FAC-2026-X89';
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(inviteUrl);
    }
    setCopiedInviteLink(true);
    showToast('Faculty invite link copied to clipboard!', 'info');
    setTimeout(() => setCopiedInviteLink(false), 3000);
  };

  // Handle Add/Invite Teacher Submission
  const handleSubmitInvite = (e) => {
    e.preventDefault();
    if (!inviteForm.name || !inviteForm.email) {
      showToast('Please specify teacher full name and official email address.', 'warning');
      return;
    }

    const newFacultyMember = {
      id: `fac-${Date.now()}`,
      name: inviteForm.name,
      role: `Senior Educator ${inviteForm.subject}`,
      email: inviteForm.email,
      phone: '+27 82 000 0000',
      subject: inviteForm.subject,
      department: inviteForm.department,
      grades: inviteForm.grades,
      activeClasses: ['Pending Allocation'],
      totalClassesCount: 1,
      enrolledLearners: 35,
      classAverageMastery: 65.0,
      capsLevel: 5,
      pacingStatus: 'Onboarding',
      atpProgress: 0,
      avatarColor: 'bg-[#13519C]'
    };

    setFacultyRoster((prev) => [newFacultyMember, ...prev]);
    setIsInviteModalOpen(false);
    setInviteForm({
      name: '',
      email: '',
      department: 'Commerce',
      subject: 'Accounting',
      grades: 'Gr 10–12'
    });
    showToast(`Invitation dispatched to ${newFacultyMember.name} (${newFacultyMember.email})!`, 'success');
  };

  // Handle HOD Recovery Plan Request
  const handleRequestRecoveryPlan = (subjectItem) => {
    setInterventionRequested((prev) => ({
      ...prev,
      [subjectItem.id]: true
    }));
    showToast(`Recovery Plan directive issued to ${subjectItem.hod} for Grade ${subjectItem.grade} ${subjectItem.subject}.`, 'warning');
  };

  // Handle Official SASAMS CSV Export
  const handleExportSASAMS = () => {
    setIsExporting(true);
    try {
      const headers = [
        'EMIS_NUMBER',
        'LURITS_NUMBER',
        'SURNAME',
        'FIRST_NAME',
        'GRADE',
        'CLASS_SECTION',
        'SUBJECT_NAME',
        'ASSESSMENT_CYCLE',
        'FORMATIVE_MARK',
        'SUMMATIVE_EXAM',
        'TERM_FINAL_MARK',
        'CAPS_LEVEL',
        'CAPS_DESCRIPTOR',
        'ACADEMIC_YEAR',
        'EXPORT_TIMESTAMP'
      ];

      const rows = filteredMarks.map((row) => {
        const caps = getCapsLevel(row.termMark);
        return [
          row.emis,
          row.lurits,
          `"${row.surname}"`,
          `"${row.firstName}"`,
          row.grade,
          row.class,
          `"${row.subject}"`,
          `"Term ${selectedTerm}"`,
          row.formativeScore,
          row.formalExamScore,
          row.termMark,
          caps.level,
          `"${caps.label}"`,
          2026,
          `"${new Date().toISOString()}"`
        ].join(',');
      });

      const csvContent = [headers.join(','), ...rows].join('\r\n');
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `SASAMS_Marks_Term${selectedTerm}_EMIS700142981_${Date.now()}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);

      showToast(`SASAMS Mark Export successful! Generated CSV with ${filteredMarks.length} student records.`, 'success');
    } catch {
      showToast('Export failed. Please check browser permissions.', 'warning');
    } finally {
      setIsExporting(false);
    }
  };

  // Gated Access Check
  if (!canAccessSchoolAdmin) {
    return (
      <div className="p-4 sm:p-6 lg:p-8 bg-slate-50 min-h-screen">
        <FeatureGatePanel
          title="School Admin Mode"
          description={CLASS_ASSIGNMENTS_BLOCKED_MESSAGE}
          badge="Access Restricted"
        />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 font-sans pb-16">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 animate-bounce-short shadow-xl rounded-xl border p-4 bg-white flex items-center space-x-3 text-sm max-w-md">
          {toastMessage.type === 'success' && <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0" />}
          {toastMessage.type === 'warning' && <AlertTriangle className="w-5 h-5 text-amber-600 shrink-0" />}
          {toastMessage.type === 'info' && <Info className="w-5 h-5 text-[#13519C] shrink-0" />}
          <div className="flex-1 font-medium text-slate-700">{toastMessage.text}</div>
          <button
            onClick={() => setToastMessage(null)}
            className="text-slate-400 hover:text-slate-600 p-1 rounded-md transition-colors"
          >
            <X className="w-4 h-4" />
          </button>
        </div>
      )}

      {/* Top Strategic Navigation Header */}
      <header className="bg-white border-b border-slate-200/90 sticky top-0 z-30 shadow-xs">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
            {/* Title & School Metadata */}
            <div className="flex items-center space-x-3.5">
              {onBack && (
                <button
                  onClick={onBack}
                  className="p-2 rounded-xl text-slate-500 hover:text-slate-800 hover:bg-slate-100 transition-colors border border-slate-200"
                  title="Return to Admin Dashboard"
                >
                  <ArrowLeft className="w-5 h-5" />
                </button>
              )}
              <div className="w-11 h-11 rounded-xl bg-[#13519C] text-white flex items-center justify-center shadow-xs">
                <School className="w-6 h-6" />
              </div>
              <div>
                <div className="flex items-center space-x-2">
                  <h1 className="text-2xl font-bold tracking-tight text-slate-900 font-afacad">
                    School Strategic Operations
                  </h1>
                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 mr-1.5 animate-pulse" />
                    Curriculum ATP Live
                  </span>
                </div>
                <p className="text-xs text-slate-500 flex items-center space-x-2 mt-0.5">
                  <span className="font-semibold text-slate-700">Fundile Comprehensive High</span>
                  <span>•</span>
                  <span>EMIS: <strong className="font-mono text-slate-700">700142981</strong></span>
                  <span>•</span>
                  <span>Circuit: Johannesburg Central (D10)</span>
                </p>
              </div>
            </div>

            {/* Term Controls & Actions */}
            <div className="flex items-center flex-wrap gap-2.5">
              {/* Term Picker */}
              <div className="bg-slate-100 p-1 rounded-xl border border-slate-200 flex items-center space-x-1 text-xs font-medium">
                {[1, 2, 3, 4].map((termNum) => (
                  <button
                    key={termNum}
                    onClick={() => {
                      setSelectedTerm(termNum);
                      showToast(`Switched view to Academic Term ${termNum}`, 'info');
                    }}
                    className={`px-3 py-1.5 rounded-lg transition-all ${
                      selectedTerm === termNum
                        ? 'bg-white text-[#13519C] shadow-xs font-semibold'
                        : 'text-slate-600 hover:text-slate-900'
                    }`}
                  >
                    Term {termNum}
                  </button>
                ))}
              </div>

              {/* Quick Invite Button */}
              <button
                onClick={() => setIsInviteModalOpen(true)}
                className="inline-flex items-center space-x-2 bg-[#13519C] hover:bg-[#0f3e77] text-white px-3.5 py-2 rounded-xl text-xs font-semibold shadow-xs transition-colors cursor-pointer"
              >
                <UserPlus className="w-4 h-4" />
                <span>+ Invite Teacher</span>
              </button>
            </div>
          </div>

          {/* Module Tabs */}
          <div className="flex space-x-2 mt-6 overflow-x-auto pb-1 scrollbar-none border-b border-slate-100">
            <button
              onClick={() => setActiveTab('pacing')}
              className={`flex items-center space-x-2 px-4 py-2.5 text-sm font-semibold border-b-2 transition-all cursor-pointer whitespace-nowrap ${
                activeTab === 'pacing'
                  ? 'border-[#13519C] text-[#13519C]'
                  : 'border-transparent text-slate-500 hover:text-slate-800'
              }`}
            >
              <Calendar className="w-4 h-4" />
              <span>ATP Curriculum Pacing Heatmap</span>
              <span className="ml-1.5 px-2 py-0.5 rounded-full text-xs bg-blue-100 text-[#13519C] font-mono">
                {ATP_PACING_DATA.length}
              </span>
            </button>

            <button
              onClick={() => setActiveTab('faculty')}
              className={`flex items-center space-x-2 px-4 py-2.5 text-sm font-semibold border-b-2 transition-all cursor-pointer whitespace-nowrap ${
                activeTab === 'faculty'
                  ? 'border-[#13519C] text-[#13519C]'
                  : 'border-transparent text-slate-500 hover:text-slate-800'
              }`}
            >
              <Users className="w-4 h-4" />
              <span>Teaching Staff & Allocations</span>
              <span className="ml-1.5 px-2 py-0.5 rounded-full text-xs bg-slate-100 text-slate-600 font-mono">
                {facultyRoster.length}
              </span>
            </button>

            <button
              onClick={() => setActiveTab('misconceptions')}
              className={`flex items-center space-x-2 px-4 py-2.5 text-sm font-semibold border-b-2 transition-all cursor-pointer whitespace-nowrap ${
                activeTab === 'misconceptions'
                  ? 'border-[#13519C] text-[#13519C]'
                  : 'border-transparent text-slate-500 hover:text-slate-800'
              }`}
            >
              <Radio className="w-4 h-4 text-rose-500" />
              <span>Misconception Directives</span>
              <span className="ml-1.5 px-2 py-0.5 rounded-full text-xs bg-rose-100 text-rose-700 font-mono">
                {misconceptions.length}
              </span>
            </button>

            <button
              onClick={() => setActiveTab('sasams')}
              className={`flex items-center space-x-2 px-4 py-2.5 text-sm font-semibold border-b-2 transition-all cursor-pointer whitespace-nowrap ${
                activeTab === 'sasams'
                  ? 'border-[#13519C] text-[#13519C]'
                  : 'border-transparent text-slate-500 hover:text-slate-800'
              }`}
            >
              <FileSpreadsheet className="w-4 h-4 text-[#0891B2]" />
              <span>Marks & SASAMS Export</span>
              <span className="ml-1.5 px-2 py-0.5 rounded-full text-xs bg-cyan-100 text-[#0891B2] font-mono">
                {filteredMarks.length}
              </span>
            </button>

            <button
              onClick={() => setActiveTab('payments')}
              className={`flex items-center space-x-2 px-4 py-2.5 text-sm font-semibold border-b-2 transition-all cursor-pointer whitespace-nowrap ${
                activeTab === 'payments'
                  ? 'border-[#13519C] text-[#13519C]'
                  : 'border-transparent text-slate-500 hover:text-slate-800'
              }`}
            >
              <CreditCard className="w-4 h-4 text-emerald-600" />
              <span>POP Audit &amp; Reconciliation</span>
              <span className="ml-1.5 px-2 py-0.5 rounded-full text-xs bg-emerald-100 text-emerald-800 font-mono">
                {popSubmissions.filter((s) => s.status === 'grace' || s.status === 'flagged').length}
              </span>
            </button>
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6">
        {/* Executive KPI Banner */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
          <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
            <div className="flex items-center justify-between text-xs font-semibold text-slate-500 mb-1">
              <span>ATP CURRICULUM PACING</span>
              <Activity className="w-4 h-4 text-[#13519C]" />
            </div>
            <div className="text-2xl font-bold text-slate-900 font-afacad">
              {pacingStats.benchmarkCoveredPercent}% On Track
            </div>
            <div className="text-xs text-slate-500 mt-1 flex items-center space-x-1.5">
              <span className="inline-block w-2 h-2 rounded-full bg-emerald-500" />
              <span>{pacingStats.onTrack} On Track</span>
              <span>•</span>
              <span className="text-amber-600 font-medium">{pacingStats.behind} Behind</span>
            </div>
          </div>

          <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
            <div className="flex items-center justify-between text-xs font-semibold text-slate-500 mb-1">
              <span>CURRICULUM MASTERY DEPTH</span>
              <Award className="w-4 h-4 text-[#0891B2]" />
            </div>
            <div className="text-2xl font-bold text-slate-900 font-afacad">
              {pacingStats.avgMastery}% Depth
            </div>
            <div className="text-xs text-slate-500 mt-1">
              Threshold: <span className="font-mono text-slate-700 font-medium">&gt;= 65%</span> benchmark mastery
            </div>
          </div>

          <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
            <div className="flex items-center justify-between text-xs font-semibold text-slate-500 mb-1">
              <span>SYSTEMIC BLOCKERS</span>
              <AlertCircle className="w-4 h-4 text-rose-500" />
            </div>
            <div className="text-2xl font-bold text-slate-900 font-afacad">
              {misconceptions.length} Systemic Risks
            </div>
            <div className="text-xs text-slate-500 mt-1">
              {Object.keys(broadcastedDrills).length} Micro-Drills Dispatched Today
            </div>
          </div>

          <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
            <div className="flex items-center justify-between text-xs font-semibold text-slate-500 mb-1">
              <span>SASAMS MARKS READY</span>
              <FileSpreadsheet className="w-4 h-4 text-emerald-600" />
            </div>
            <div className="text-2xl font-bold text-slate-900 font-afacad">
              {sasamsAnalytics.passRate}% Pass Rate
            </div>
            <div className="text-xs text-slate-500 mt-1">
              <span className="font-semibold text-emerald-700">{sasamsAnalytics.distinctionRate}%</span> Level 7 Distinctions
            </div>
          </div>
        </div>

        {/* ========================================================= */}
        {/* MODULE 1: ATP CURRICULUM PACING HEATMAP */}
        {/* ========================================================= */}
        {activeTab === 'pacing' && (
          <section className="space-y-6">
            {/* Header & Filter Controls */}
            <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs">
              <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-5">
                <div>
                  <h2 className="text-lg font-bold text-slate-900 font-afacad">
                    Annual Teaching Plan (ATP) Curriculum Heatmap — Term {selectedTerm}
                  </h2>
                  <p className="text-xs text-slate-500 mt-0.5">
                    Live pacing tracker across curriculum subjects (Grades 7–12) benchmarked against National Department of Basic Education ATP schedules.
                  </p>
                </div>

                {/* Status Key Badge Group */}
                <div className="flex items-center space-x-3 text-xs">
                  <span className="inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-lg bg-emerald-50 text-emerald-700 border border-emerald-200">
                    <span className="w-2 h-2 rounded-full bg-emerald-500" />
                    <span>On Track</span>
                  </span>
                  <span className="inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-lg bg-amber-50 text-amber-700 border border-amber-200">
                    <span className="w-2 h-2 rounded-full bg-amber-500" />
                    <span>1 Week Behind</span>
                  </span>
                  <span className="inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-lg bg-blue-50 text-blue-700 border border-blue-200">
                    <span className="w-2 h-2 rounded-full bg-blue-500" />
                    <span>Completed</span>
                  </span>
                </div>
              </div>

              {/* Filters */}
              <div className="flex flex-wrap items-center gap-3 pt-3 border-t border-slate-100">
                <div className="flex items-center space-x-2 text-xs text-slate-600">
                  <Filter className="w-3.5 h-3.5 text-slate-400" />
                  <span className="font-semibold">Grade:</span>
                </div>
                <div className="flex flex-wrap gap-1.5">
                  {['all', '7', '8', '9', '10', '11', '12'].map((g) => (
                    <button
                      key={g}
                      onClick={() => setPacingGradeFilter(g)}
                      className={`px-3 py-1 rounded-lg text-xs font-medium transition-colors cursor-pointer ${
                        pacingGradeFilter === g
                          ? 'bg-[#13519C] text-white shadow-xs'
                          : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                      }`}
                    >
                      {g === 'all' ? 'All Grades (7–12)' : `Grade ${g}`}
                    </button>
                  ))}
                </div>

                <div className="h-4 w-px bg-slate-200 mx-1 hidden sm:block" />

                <div className="flex items-center space-x-2 text-xs text-slate-600">
                  <span className="font-semibold">Subject:</span>
                </div>
                <select
                  value={pacingSubjectFilter}
                  onChange={(e) => setPacingSubjectFilter(e.target.value)}
                  className="bg-slate-100 border border-slate-200 rounded-lg text-xs px-2.5 py-1 text-slate-700 focus:outline-none focus:ring-1 focus:ring-[#13519C]"
                >
                  <option value="all">All Disciplines</option>
                  <option value="Accounting">Accounting</option>
                  <option value="Mathematics">Mathematics</option>
                  <option value="Physical Sciences">Physical Sciences</option>
                  <option value="Life Sciences">Life Sciences</option>
                  <option value="Business Studies">Business Studies</option>
                  <option value="EMS">EMS (Senior Phase)</option>
                </select>

                <div className="ml-auto text-xs text-slate-500">
                  Showing <strong className="font-mono text-slate-800">{filteredPacingData.length}</strong> subject streams
                </div>
              </div>
            </div>

            {/* Pacing Heatmap Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {filteredPacingData.map((item) => {
                const isBehind = item.status === 'behind';
                const isCompleted = item.status === 'completed';
                const hasIntervention = interventionRequested[item.id];

                return (
                  <div
                    key={item.id}
                    className={`bg-white border rounded-2xl p-5 shadow-xs transition-all hover:shadow-md flex flex-col justify-between ${
                      isBehind ? 'border-amber-300 ring-1 ring-amber-100' : 'border-slate-200/90'
                    }`}
                  >
                    <div>
                      {/* Top Badges */}
                      <div className="flex items-center justify-between gap-2 mb-3">
                        <span className="inline-flex items-center px-2 py-0.5 rounded-md text-xs font-bold bg-slate-100 text-slate-800 font-mono">
                          GR {item.grade} • {item.subject}
                        </span>

                        {item.status === 'on_track' && (
                          <span className="inline-flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800">
                            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
                            <span>On Track</span>
                          </span>
                        )}

                        {isBehind && (
                          <span className="inline-flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-100 text-amber-800">
                            <AlertTriangle className="w-3 h-3 text-amber-600 mr-1" />
                            <span>1 Week Behind</span>
                          </span>
                        )}

                        {isCompleted && (
                          <span className="inline-flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-blue-100 text-[#13519C]">
                            <CheckCircle2 className="w-3 h-3 text-[#13519C] mr-1" />
                            <span>Completed</span>
                          </span>
                        )}
                      </div>

                      {/* Subject Title & Lead */}
                      <h3 className="text-base font-bold text-slate-900 font-afacad mb-0.5">
                        {item.subject} Grade {item.grade}
                      </h3>
                      <p className="text-xs text-slate-500 mb-3">
                        HOD / Lead: <span className="font-medium text-slate-700">{item.hod}</span> • {item.enrolledLearners} Learners
                      </p>

                      {/* Current Topic & Progress Details */}
                      <div className="bg-slate-50 border border-slate-100 rounded-xl p-3 mb-4 space-y-2 text-xs">
                        <div>
                          <div className="text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                            Active Topic (Week {item.currentWeek} of {item.totalWeeks})
                          </div>
                          <div className="font-semibold text-slate-800 truncate mt-0.5">
                            {item.currentTopic}
                          </div>
                        </div>

                        <div>
                          <div className="text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                            Next Milestone
                          </div>
                          <div className="text-slate-600 truncate mt-0.5">
                            {item.nextMilestone}
                          </div>
                        </div>
                      </div>

                      {/* Pacing vs Mastery Depth Dual Bar */}
                      <div className="space-y-2 mb-4">
                        <div>
                          <div className="flex justify-between text-xs text-slate-600 mb-1">
                            <span>Syllabus Covered</span>
                            <span className="font-mono font-semibold text-slate-800">{item.curriculumCovered}%</span>
                          </div>
                          <div className="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
                            <div
                              className="bg-[#13519C] h-full rounded-full transition-all duration-500"
                              style={{ width: `${item.curriculumCovered}%` }}
                            />
                          </div>
                        </div>

                        <div>
                          <div className="flex justify-between text-xs text-slate-600 mb-1">
                            <span>Mastery Depth</span>
                            <span className={`font-mono font-semibold ${item.masteryDepth >= 65 ? 'text-emerald-600' : 'text-amber-600'}`}>
                              {item.masteryDepth}% (Target: &gt;= 65%)
                            </span>
                          </div>
                          <div className="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
                            <div
                              className={`h-full rounded-full transition-all duration-500 ${
                                item.masteryDepth >= 65 ? 'bg-emerald-500' : 'bg-amber-500'
                              }`}
                              style={{ width: `${item.masteryDepth}%` }}
                            />
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* Action Buttons */}
                    <div className="pt-3 border-t border-slate-100 flex items-center justify-between gap-2">
                      <button
                        onClick={() => setInspectingSubject(item)}
                        className="inline-flex items-center space-x-1.5 text-xs font-semibold text-[#13519C] hover:text-[#0f3e77] p-1.5 rounded-lg hover:bg-blue-50 transition-colors cursor-pointer"
                      >
                        <BookOpen className="w-3.5 h-3.5" />
                        <span>View ATP Schedule</span>
                      </button>

                      {isBehind && (
                        <button
                          onClick={() => handleRequestRecoveryPlan(item)}
                          disabled={hasIntervention}
                          className={`inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                            hasIntervention
                              ? 'bg-amber-100 text-amber-800 cursor-default'
                              : 'bg-amber-600 hover:bg-amber-700 text-white shadow-xs cursor-pointer'
                          }`}
                        >
                          {hasIntervention ? (
                            <>
                              <Check className="w-3 h-3" />
                              <span>Plan Requested</span>
                            </>
                          ) : (
                            <>
                              <Clock className="w-3 h-3" />
                              <span>Request Recovery Plan</span>
                            </>
                          )}
                        </button>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </section>
        )}

        {/* ========================================================= */}
        {/* MODULE 2: TEACHING STAFF & FACULTY ALLOCATIONS */}
        {/* ========================================================= */}
        {activeTab === 'faculty' && (
          <section className="space-y-6">
            {/* Header & Controls */}
            <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs">
              <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-5">
                <div>
                  <h2 className="text-lg font-bold text-slate-900 font-afacad">
                    Teaching Staff & Subject Allocations
                  </h2>
                  <p className="text-xs text-slate-500 mt-0.5">
                    Manage active educators, subject allocations, active class rosters, and learner mastery averages.
                  </p>
                </div>

                <div className="flex items-center space-x-3">
                  <button
                    onClick={handleCopyFacultyLink}
                    className="inline-flex items-center space-x-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 px-3.5 py-2 rounded-xl text-xs font-semibold transition-colors cursor-pointer border border-slate-200"
                  >
                    {copiedInviteLink ? <Check className="w-4 h-4 text-emerald-600" /> : <Copy className="w-4 h-4" />}
                    <span>{copiedInviteLink ? 'Link Copied!' : 'Copy Faculty Join Link'}</span>
                  </button>

                  <button
                    onClick={() => setIsInviteModalOpen(true)}
                    className="inline-flex items-center space-x-1.5 bg-[#13519C] hover:bg-[#0f3e77] text-white px-3.5 py-2 rounded-xl text-xs font-semibold shadow-xs transition-colors cursor-pointer"
                  >
                    <UserPlus className="w-4 h-4" />
                    <span>+ Invite Educator</span>
                  </button>
                </div>
              </div>

              {/* Filters & Search */}
              <div className="flex flex-wrap items-center gap-3 pt-3 border-t border-slate-100">
                <div className="relative flex-1 min-w-[220px] max-w-sm">
                  <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-2.5" />
                  <input
                    type="text"
                    placeholder="Search by teacher, subject, or email..."
                    value={facultySearch}
                    onChange={(e) => setFacultySearch(e.target.value)}
                    className="w-full bg-slate-100 border border-slate-200 rounded-xl text-xs pl-8 pr-3 py-2 text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-[#13519C]"
                  />
                </div>

                <div className="flex items-center space-x-2 text-xs text-slate-600">
                  <Filter className="w-3.5 h-3.5 text-slate-400" />
                  <span className="font-semibold">Department:</span>
                </div>
                <select
                  value={facultyDeptFilter}
                  onChange={(e) => setFacultyDeptFilter(e.target.value)}
                  className="bg-slate-100 border border-slate-200 rounded-lg text-xs px-2.5 py-1.5 text-slate-700 focus:outline-none focus:ring-1 focus:ring-[#13519C]"
                >
                  <option value="all">All Departments</option>
                  <option value="Commerce">Commerce & Management</option>
                  <option value="STEM">STEM (Mathematics)</option>
                  <option value="Sciences">Physical & Life Sciences</option>
                  <option value="Senior Phase EMS">Senior Phase EMS</option>
                </select>

                <div className="ml-auto text-xs text-slate-500">
                  Showing <strong className="font-mono text-slate-800">{filteredFaculty.length}</strong> educators
                </div>
              </div>
            </div>

            {/* Faculty Roster Table */}
            <div className="bg-white border border-slate-200/90 rounded-2xl shadow-xs overflow-hidden">
              <div className="overflow-x-auto">
                <table className="w-full text-left text-xs text-slate-600">
                  <thead className="bg-slate-50 text-slate-700 uppercase font-semibold text-[11px] tracking-wider border-b border-slate-200">
                    <tr>
                      <th className="py-3.5 px-4">Educator / Staff</th>
                      <th className="py-3.5 px-4">Subject & Department</th>
                      <th className="py-3.5 px-4">Grades</th>
                      <th className="py-3.5 px-4">Allocated Classes</th>
                      <th className="py-3.5 px-4">Learners</th>
                      <th className="py-3.5 px-4">Class Mastery Avg</th>
                      <th className="py-3.5 px-4">ATP Status</th>
                      <th className="py-3.5 px-4 text-right">Actions</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {filteredFaculty.map((member) => (
                      <tr key={member.id} className="hover:bg-slate-50/80 transition-colors">
                        <td className="py-3.5 px-4">
                          <div className="flex items-center space-x-3">
                            <div className={`w-9 h-9 rounded-full ${member.avatarColor} text-white font-bold flex items-center justify-center text-xs shrink-0 shadow-xs`}>
                              {member.name.split(' ').map((n) => n[0]).join('').slice(0, 2)}
                            </div>
                            <div>
                              <div className="font-bold text-slate-900 text-sm font-afacad">{member.name}</div>
                              <div className="text-[11px] text-slate-400 font-mono">{member.email}</div>
                            </div>
                          </div>
                        </td>

                        <td className="py-3.5 px-4">
                          <div className="font-semibold text-slate-800">{member.subject}</div>
                          <div className="text-[11px] text-slate-400">{member.department}</div>
                        </td>

                        <td className="py-3.5 px-4 font-mono font-medium text-slate-700">
                          {member.grades}
                        </td>

                        <td className="py-3.5 px-4">
                          <div className="flex flex-wrap gap-1">
                            {member.activeClasses.map((cls, idx) => (
                              <span
                                key={idx}
                                className="px-2 py-0.5 rounded-md bg-slate-100 text-slate-700 font-mono text-[11px] border border-slate-200"
                              >
                                {cls}
                              </span>
                            ))}
                          </div>
                        </td>

                        <td className="py-3.5 px-4 font-mono font-semibold text-slate-800">
                          {member.enrolledLearners}
                        </td>

                        <td className="py-3.5 px-4">
                          <div className="flex items-center space-x-2">
                            <span className="font-mono font-bold text-slate-900">{member.classAverageMastery}%</span>
                            <span className="px-1.5 py-0.5 rounded-sm text-[10px] font-bold bg-cyan-50 text-[#0891B2] border border-cyan-200">
                              Lvl {member.capsLevel}
                            </span>
                          </div>
                        </td>

                        <td className="py-3.5 px-4">
                          <span
                            className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-semibold ${
                              member.pacingStatus.includes('Behind')
                                ? 'bg-amber-100 text-amber-800'
                                : member.pacingStatus.includes('Completed')
                                ? 'bg-blue-100 text-[#13519C]'
                                : 'bg-emerald-100 text-emerald-800'
                            }`}
                          >
                            {member.pacingStatus}
                          </span>
                        </td>

                        <td className="py-3.5 px-4 text-right">
                          <button
                            onClick={() => {
                              showToast(`Direct message and curriculum report opened for ${member.name}.`, 'info');
                            }}
                            className="inline-flex items-center space-x-1 text-xs font-semibold text-[#13519C] hover:text-[#0f3e77] px-2.5 py-1 rounded-lg hover:bg-blue-50 transition-colors cursor-pointer"
                          >
                            <span>Inspect</span>
                            <ChevronRight className="w-3.5 h-3.5" />
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        )}

        {/* ========================================================= */}
        {/* MODULE 3: SCHOOL-WIDE MISCONCEPTION BROADCAST */}
        {/* ========================================================= */}
        {activeTab === 'misconceptions' && (
          <section className="space-y-6">
            {/* Header Banner */}
            <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs">
              <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-4">
                <div>
                  <div className="flex items-center space-x-2">
                    <Radio className="w-5 h-5 text-rose-600 animate-pulse" />
                    <h2 className="text-lg font-bold text-slate-900 font-afacad">
                      School-Wide Misconception Directives & Remedial Broadcast
                    </h2>
                  </div>
                  <p className="text-xs text-slate-500 mt-0.5">
                    Automated diagnostic engine isolates high-failure exam questions across grades. Principals & HODs can dispatch 1-click 5-minute remedial micro-drills to all enrolled learners in that grade.
                  </p>
                </div>

                {/* Grade Filter */}
                <div className="flex items-center space-x-2">
                  <span className="text-xs font-semibold text-slate-500">Filter Grade:</span>
                  <div className="flex space-x-1 bg-slate-100 p-1 rounded-xl border border-slate-200 text-xs">
                    {['all', '9', '10', '11', '12'].map((gr) => (
                      <button
                        key={gr}
                        onClick={() => setMisconceptionGradeFilter(gr)}
                        className={`px-3 py-1 rounded-lg transition-colors cursor-pointer ${
                          misconceptionGradeFilter === gr
                            ? 'bg-white text-slate-900 shadow-xs font-semibold'
                            : 'text-slate-600 hover:text-slate-900'
                        }`}
                      >
                        {gr === 'all' ? 'All' : `Gr ${gr}`}
                      </button>
                    ))}
                  </div>
                </div>
              </div>

              {/* Status Alert */}
              <div className="bg-rose-50 border border-rose-200 rounded-xl p-3 flex items-start space-x-3 text-xs text-rose-800">
                <AlertCircle className="w-4 h-4 text-rose-600 shrink-0 mt-0.5" />
                <div>
                  <span className="font-bold">Active Diagnostic Finding:</span> Output VAT inversion on Debtors Allowances (Grade 10 Accounting) and Internal Resistance Lost Volts (Grade 12 Physics) are currently the highest-risk exam blockers ahead of Term 1 controlled assessments.
                </div>
              </div>
            </div>

            {/* Misconceptions Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
              {filteredMisconceptions.map((misc) => {
                const broadcastState = broadcastedDrills[misc.id];
                const isCritical = misc.severity === 'critical';

                return (
                  <div
                    key={misc.id}
                    className={`bg-white border rounded-2xl p-5 shadow-xs transition-all flex flex-col justify-between ${
                      isCritical ? 'border-rose-200' : 'border-slate-200/90'
                    }`}
                  >
                    <div>
                      {/* Top Badges */}
                      <div className="flex items-center justify-between gap-2 mb-3">
                        <div className="flex items-center space-x-2">
                          <span className="px-2.5 py-0.5 rounded-md text-xs font-bold bg-slate-100 text-slate-800 font-mono">
                            GRADE {misc.grade} • {misc.subject}
                          </span>
                          <span className="text-[11px] font-mono text-slate-400">
                            {misc.capsWeighting}
                          </span>
                        </div>

                        <span
                          className={`px-2.5 py-0.5 rounded-full text-xs font-semibold ${
                            isCritical ? 'bg-rose-100 text-rose-800' : 'bg-amber-100 text-amber-800'
                          }`}
                        >
                          {misc.severityLabel}
                        </span>
                      </div>

                      {/* Main Title & Blocker */}
                      <h3 className="text-base font-bold text-slate-900 font-afacad mb-1.5">
                        {misc.title}
                      </h3>
                      <div className="text-xs font-semibold text-rose-700 mb-2">
                        {misc.summary}
                      </div>
                      <p className="text-xs text-slate-600 leading-relaxed mb-4">
                        {misc.explanation}
                      </p>

                      {/* Remediation Details Box */}
                      <div className="bg-slate-50 border border-slate-200/80 rounded-xl p-3 mb-4 space-y-1.5 text-xs">
                        <div className="flex items-center justify-between text-slate-500">
                          <span>Target Classes:</span>
                          <span className="font-semibold text-slate-800">
                            {misc.affectedClasses.join(', ')} ({misc.affectedCount} enrolled)
                          </span>
                        </div>
                        <div className="flex items-center justify-between text-slate-500">
                          <span>Remedial Micro-Drill:</span>
                          <span className="font-medium text-[#13519C]">
                            {misc.drillQuestions.length} Diagnostic Multi-Choice Questions (5 min)
                          </span>
                        </div>
                      </div>

                      {/* Broadcast status banner if active */}
                      {broadcastState && (
                        <div className="mb-4 bg-emerald-50 border border-emerald-200 rounded-xl p-3 flex items-center justify-between text-xs text-emerald-800">
                          <div className="flex items-center space-x-2">
                            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                            <span>
                              <strong>Broadcast Active</strong> • Dispatched at {broadcastState.timestamp} today
                            </span>
                          </div>
                          <span className="font-mono font-bold text-emerald-900">
                            {broadcastState.enrolledCount} Learners Notified
                          </span>
                        </div>
                      )}
                    </div>

                    {/* Actions */}
                    <div className="pt-3 border-t border-slate-100 flex items-center justify-between gap-3">
                      <button
                        onClick={() => setActivePreviewDrill(misc)}
                        className="inline-flex items-center space-x-1.5 text-xs font-semibold text-slate-600 hover:text-slate-900 p-2 rounded-lg hover:bg-slate-100 transition-colors cursor-pointer"
                      >
                        <FileText className="w-3.5 h-3.5" />
                        <span>Inspect Questions & Talking Points</span>
                      </button>

                      <button
                        onClick={() => handleBroadcastRemedialDrill(misc)}
                        className={`inline-flex items-center space-x-2 px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-xs cursor-pointer ${
                          broadcastState
                            ? 'bg-emerald-600 hover:bg-emerald-700 text-white'
                            : 'bg-rose-600 hover:bg-rose-700 text-white'
                        }`}
                      >
                        <Send className="w-3.5 h-3.5" />
                        <span>
                          {broadcastState ? 'Re-Broadcast Drill' : 'Broadcast Remedial Drill'}
                        </span>
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          </section>
        )}

        {/* ========================================================= */}
        {/* MODULE 4: TERM MARK COLLATION & SASAMS EXPORT */}
        {/* ========================================================= */}
        {activeTab === 'sasams' && (
          <section className="space-y-6">
            {/* Header & Export Panel */}
            <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs">
              <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-5">
                <div>
                  <div className="flex items-center space-x-2">
                    <FileSpreadsheet className="w-5 h-5 text-emerald-600" />
                    <h2 className="text-lg font-bold text-slate-900 font-afacad">
                      Official SASAMS Mark Collation & Verification — Term {selectedTerm}
                    </h2>
                  </div>
                  <p className="text-xs text-slate-500 mt-0.5">
                    Aggregates continuous formative drills (40%) and formal term assessments (60%) into the official South African Schools Administration and Management System CSV specification.
                  </p>
                </div>

                <div className="flex items-center space-x-3">
                  <button
                    onClick={handleExportSASAMS}
                    disabled={isExporting}
                    className="inline-flex items-center space-x-2 bg-emerald-600 hover:bg-emerald-700 active:bg-emerald-800 text-white px-4 py-2.5 rounded-xl text-xs font-bold shadow-xs transition-colors cursor-pointer"
                  >
                    <Download className="w-4 h-4" />
                    <span>{isExporting ? 'Generating SASAMS File...' : '📥 Export to SASAMS (CSV)'}</span>
                  </button>
                </div>
              </div>

              {/* Real-time Analytics Summary Strip */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-slate-50 border border-slate-100 rounded-xl p-3 mb-5">
                <div>
                  <div className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Marks Collated</div>
                  <div className="text-lg font-bold text-slate-900 font-afacad mt-0.5">{sasamsAnalytics.count} Learners</div>
                </div>
                <div>
                  <div className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Filtered Average</div>
                  <div className="text-lg font-bold text-[#13519C] font-mono mt-0.5">{sasamsAnalytics.average}%</div>
                </div>
                <div>
                  <div className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Pass Rate (&gt;= Lvl 4)</div>
                  <div className="text-lg font-bold text-emerald-600 font-mono mt-0.5">{sasamsAnalytics.passRate}%</div>
                </div>
                <div>
                  <div className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Level 7 Distinctions</div>
                  <div className="text-lg font-bold text-purple-600 font-mono mt-0.5">{sasamsAnalytics.distinctionRate}%</div>
                </div>
              </div>

              {/* Filters */}
              <div className="flex flex-wrap items-center gap-3 pt-3 border-t border-slate-100">
                <div className="relative flex-1 min-w-[200px] max-w-xs">
                  <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-2.5" />
                  <input
                    type="text"
                    placeholder="Search learner name or LURITS..."
                    value={sasamsSearch}
                    onChange={(e) => setSasamsSearch(e.target.value)}
                    className="w-full bg-slate-100 border border-slate-200 rounded-xl text-xs pl-8 pr-3 py-2 text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-[#13519C]"
                  />
                </div>

                <div className="flex items-center space-x-1.5 text-xs text-slate-600">
                  <span className="font-semibold">Grade:</span>
                  <select
                    value={sasamsGradeFilter}
                    onChange={(e) => setSasamsGradeFilter(e.target.value)}
                    className="bg-slate-100 border border-slate-200 rounded-lg text-xs px-2 py-1.5 text-slate-700"
                  >
                    <option value="all">All Grades</option>
                    <option value="7">Grade 7</option>
                    <option value="8">Grade 8</option>
                    <option value="9">Grade 9</option>
                    <option value="10">Grade 10</option>
                    <option value="11">Grade 11</option>
                    <option value="12">Grade 12</option>
                  </select>
                </div>

                <div className="flex items-center space-x-1.5 text-xs text-slate-600">
                  <span className="font-semibold">Subject:</span>
                  <select
                    value={sasamsSubjectFilter}
                    onChange={(e) => setSasamsSubjectFilter(e.target.value)}
                    className="bg-slate-100 border border-slate-200 rounded-lg text-xs px-2 py-1.5 text-slate-700"
                  >
                    <option value="all">All Subjects</option>
                    <option value="Accounting">Accounting</option>
                    <option value="Mathematics">Mathematics</option>
                    <option value="Physical Sciences">Physical Sciences</option>
                    <option value="Life Sciences">Life Sciences</option>
                    <option value="Business Studies">Business Studies</option>
                    <option value="EMS">EMS</option>
                  </select>
                </div>

                <div className="flex items-center space-x-1.5 text-xs text-slate-600">
                  <span className="font-semibold">Curriculum Level:</span>
                  <select
                    value={sasamsLevelFilter}
                    onChange={(e) => setSasamsLevelFilter(e.target.value)}
                    className="bg-slate-100 border border-slate-200 rounded-lg text-xs px-2 py-1.5 text-slate-700"
                  >
                    <option value="all">All Levels (1–7)</option>
                    <option value="7">Level 7 (80%–100%) Distinctions</option>
                    <option value="pass">Passing Marks (Level 4–7)</option>
                    <option value="atRisk">At-Risk Learners (Level 1–2)</option>
                  </select>
                </div>

                <div className="ml-auto text-xs text-slate-500">
                  Showing <strong className="font-mono text-slate-800">{filteredMarks.length}</strong> records
                </div>
              </div>
            </div>

            {/* SASAMS Table */}
            <div className="bg-white border border-slate-200/90 rounded-2xl shadow-xs overflow-hidden">
              <div className="overflow-x-auto">
                <table className="w-full text-left text-xs text-slate-600">
                  <thead className="bg-slate-50 text-slate-700 uppercase font-semibold text-[11px] tracking-wider border-b border-slate-200">
                    <tr>
                      <th className="py-3.5 px-4">Learner Name</th>
                      <th className="py-3.5 px-4">LURITS No.</th>
                      <th className="py-3.5 px-4">Class</th>
                      <th className="py-3.5 px-4">Subject</th>
                      <th className="py-3.5 px-4 text-center">Formative (40%)</th>
                      <th className="py-3.5 px-4 text-center">Formal Exam (60%)</th>
                      <th className="py-3.5 px-4 text-center">Term 1 Mark</th>
                      <th className="py-3.5 px-4">Curriculum Level &amp; Descriptor</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {filteredMarks.map((row) => {
                      const caps = getCapsLevel(row.termMark);
                      return (
                        <tr key={row.id} className="hover:bg-slate-50/80 transition-colors">
                          <td className="py-3.5 px-4">
                            <div className="font-bold text-slate-900 text-sm font-afacad">
                              {row.surname}, {row.firstName}
                            </div>
                            <div className="text-[10px] text-slate-400 font-mono">EMIS {row.emis}</div>
                          </td>

                          <td className="py-3.5 px-4 font-mono text-slate-600 text-xs">
                            {row.lurits}
                          </td>

                          <td className="py-3.5 px-4">
                            <span className="px-2 py-0.5 rounded-md bg-slate-100 text-slate-800 font-mono font-medium border border-slate-200 text-xs">
                              {row.class}
                            </span>
                          </td>

                          <td className="py-3.5 px-4 font-medium text-slate-800">
                            {row.subject}
                          </td>

                          <td className="py-3.5 px-4 text-center font-mono text-slate-700">
                            {row.formativeScore}%
                          </td>

                          <td className="py-3.5 px-4 text-center font-mono text-slate-700">
                            {row.formalExamScore}%
                          </td>

                          <td className="py-3.5 px-4 text-center">
                            <span className="font-mono font-bold text-sm text-slate-900">
                              {row.termMark}%
                            </span>
                          </td>

                          <td className="py-3.5 px-4">
                            <span className={`inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-md text-xs font-semibold border ${caps.badge}`}>
                              <span className="font-mono font-bold">Lvl {caps.level}</span>
                              <span>•</span>
                              <span>{caps.label}</span>
                            </span>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        )}

        {/* ========================================================= */}
        {/* MODULE 5: PROOF OF PAYMENT AUDIT & RECONCILIATION */}
        {/* ========================================================= */}
        {activeTab === 'payments' && (
          <section className="space-y-6 animate-fade-in">
            {/* Header & Subtitle */}
            <div className="bg-white border border-slate-200/90 rounded-2xl p-6 shadow-xs">
              <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                  <div className="flex items-center space-x-2.5">
                    <span className="w-8 h-8 rounded-xl bg-emerald-50 text-emerald-600 border border-emerald-200/60 flex items-center justify-center font-bold text-xs">
                      <CreditCard className="w-4 h-4" />
                    </span>
                    <div>
                      <h2 className="text-xl font-bold text-slate-900 font-afacad tracking-tight">
                        Proof of Payment Audit &amp; Reconciliation
                      </h2>
                      <p className="text-xs text-slate-500">
                        Electronic funds transfer verification for Access Bank South Africa (Account 410 882 9104). Review slips, confirm clearance, and manage 14-day grace periods.
                      </p>
                    </div>
                  </div>
                </div>

                <div className="flex items-center gap-2">
                  <div className="px-3.5 py-1.5 rounded-xl bg-slate-50 border border-slate-200 text-xs font-mono text-slate-600">
                    Target: <strong className="text-slate-900">Access Bank • 4108829104</strong>
                  </div>
                </div>
              </div>
            </div>

            {/* KPI Cards Row */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
                    Total Access Bank Verified
                  </span>
                  <div className="w-8 h-8 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
                    <CheckCircle2 className="w-4 h-4" />
                  </div>
                </div>
                <div className="text-2xl font-black text-slate-900 font-afacad mt-2">
                  R{popSubmissions
                    .filter((s) => s.status === 'approved')
                    .reduce((acc, curr) => acc + parseFloat(curr.amount.replace(/[^0-9.]/g, '')), 0)
                    .toLocaleString('en-ZA', { minimumFractionDigits: 2 })}
                </div>
                <div className="text-[11px] text-emerald-600 font-medium mt-1">
                  {popSubmissions.filter((s) => s.status === 'approved').length} confirmed &amp; cleared
                </div>
              </div>

              <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
                    Active Grace Periods
                  </span>
                  <div className="w-8 h-8 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center">
                    <Clock className="w-4 h-4" />
                  </div>
                </div>
                <div className="text-2xl font-black text-slate-900 font-afacad mt-2">
                  {popSubmissions.filter((s) => s.status === 'grace').length}
                </div>
                <div className="text-[11px] text-amber-600 font-medium mt-1">
                  Immediate 14-day learning active
                </div>
              </div>

              <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
                    Needs Investigation
                  </span>
                  <div className="w-8 h-8 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center">
                    <AlertTriangle className="w-4 h-4" />
                  </div>
                </div>
                <div className="text-2xl font-black text-slate-900 font-afacad mt-2">
                  {popSubmissions.filter((s) => s.status === 'flagged').length}
                </div>
                <div className="text-[11px] text-rose-600 font-medium mt-1">
                  Mismatched bank or blurry slip
                </div>
              </div>

              <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
                    AI OCR Audit Accuracy
                  </span>
                  <div className="w-8 h-8 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center">
                    <Sparkles className="w-4 h-4" />
                  </div>
                </div>
                <div className="text-2xl font-black text-slate-900 font-afacad mt-2">
                  98.4%
                </div>
                <div className="text-[11px] text-[#13519C] font-medium mt-1">
                  Automated slip parsing
                </div>
              </div>
            </div>

            {/* Filter and Search Bar */}
            <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
              <div className="flex flex-col md:flex-row gap-3 items-center justify-between">
                <div className="relative w-full md:w-80">
                  <Search className="w-4 h-4 absolute left-3 top-2.5 text-slate-400" />
                  <input
                    type="text"
                    value={popSearch}
                    onChange={(e) => setPopSearch(e.target.value)}
                    placeholder="Search learner, email, or FUN- reference..."
                    className="w-full pl-9 pr-3 py-2 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-900 placeholder:text-slate-400 focus:outline-none focus:border-[#13519C]"
                  />
                </div>

                <div className="flex items-center gap-2 w-full md:w-auto">
                  <Filter className="w-4 h-4 text-slate-400 flex-shrink-0" />
                  <select
                    value={popStatusFilter}
                    onChange={(e) => setPopStatusFilter(e.target.value)}
                    className="px-3 py-2 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-700 font-semibold focus:outline-none cursor-pointer"
                  >
                    <option value="all">All Submissions</option>
                    <option value="pending">Pending Review &amp; Grace</option>
                    <option value="approved">AI / Human Verified (Approved)</option>
                    <option value="flagged">Flagged Submissions</option>
                    <option value="rejected">Rejected &amp; Revoked</option>
                  </select>
                </div>

                <div className="text-xs text-slate-500 font-mono">
                  Showing <strong>{filteredPopSubmissions.length}</strong> submission{filteredPopSubmissions.length === 1 ? '' : 's'}
                </div>
              </div>
            </div>

            {/* Submissions Table */}
            <div className="bg-white border border-slate-200/90 rounded-2xl shadow-xs overflow-hidden">
              <div className="overflow-x-auto">
                <table className="w-full text-left text-xs text-slate-600">
                  <thead className="bg-slate-50 text-slate-700 uppercase font-semibold text-[11px] tracking-wider border-b border-slate-200">
                    <tr>
                      <th className="py-3.5 px-4">Learner &amp; Contact</th>
                      <th className="py-3.5 px-4">Upload Date &amp; Time</th>
                      <th className="py-3.5 px-4">Plan &amp; Amount</th>
                      <th className="py-3.5 px-4">Target Bank &amp; Ref</th>
                      <th className="py-3.5 px-4">AI Review &amp; Confidence</th>
                      <th className="py-3.5 px-4 text-right">Reconciliation Actions</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {filteredPopSubmissions.map((row) => (
                      <tr key={row.id} className="hover:bg-slate-50/80 transition-colors">
                        {/* Learner Info */}
                        <td className="py-3.5 px-4">
                          <div className="font-bold text-slate-900 text-sm font-afacad">
                            {row.learnerName}
                          </div>
                          <div className="text-[11px] text-slate-400 font-mono">
                            {row.email}
                          </div>
                          <div className="text-[10px] text-slate-400">
                            {row.grade} • {row.phone}
                          </div>
                        </td>

                        {/* Upload Date & Time */}
                        <td className="py-3.5 px-4">
                          <div className="font-semibold text-slate-800">
                            {row.uploadDateTime}
                          </div>
                          <div className="text-[10px] text-slate-400">
                            Slip Date: {row.depositDate}
                          </div>
                        </td>

                        {/* Plan & Amount */}
                        <td className="py-3.5 px-4">
                          <div className="font-bold text-slate-900 font-mono text-sm">
                            {row.amount}
                          </div>
                          <div className="text-[11px] text-[#13519C] font-semibold">
                            {row.planName} ({row.planCycle})
                          </div>
                        </td>

                        {/* Target Bank & Ref */}
                        <td className="py-3.5 px-4">
                          <div className="font-medium text-slate-700">
                            {row.targetBank}
                          </div>
                          <div className="inline-flex items-center gap-1 text-[11px] font-mono text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 mt-0.5">
                            <span>{row.reference}</span>
                          </div>
                        </td>

                        {/* AI Review Badge */}
                        <td className="py-3.5 px-4 max-w-xs">
                          {row.status === 'approved' && (
                            <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
                              <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                              <span>🟢 AI Verified ({row.aiConfidence}% Confidence) • Auto-Approved</span>
                            </span>
                          )}
                          {row.status === 'grace' && (
                            <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold bg-amber-50 text-amber-700 border border-amber-200">
                              <span className="w-1.5 h-1.5 rounded-full bg-amber-500 animate-ping"></span>
                              <span>🟡 Grace Period Active ({row.aiConfidence}% Confidence) • Needs Verification</span>
                            </span>
                          )}
                          {row.status === 'flagged' && (
                            <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold bg-rose-50 text-rose-700 border border-rose-200">
                              <span className="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
                              <span>🔴 Flagged ({row.aiConfidence}% Confidence) • Wrong Recipient / Blurry</span>
                            </span>
                          )}
                          {row.status === 'rejected' && (
                            <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-600 border border-slate-200">
                              <span>⚪ Rejected &amp; Access Revoked</span>
                            </span>
                          )}
                          <div className="text-[10px] text-slate-500 mt-1 line-clamp-2 leading-relaxed">
                            {row.aiNotes}
                          </div>
                        </td>

                        {/* Actions */}
                        <td className="py-3.5 px-4 text-right">
                          <div className="flex items-center justify-end gap-1.5">
                            <button
                              onClick={() => setSelectedSlipModal(row)}
                              className="px-2.5 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold transition cursor-pointer flex items-center gap-1"
                              title="Inspect Transfer Slip"
                            >
                              <Eye className="w-3.5 h-3.5 text-slate-500" />
                              <span>View Slip</span>
                            </button>

                            {row.status !== 'approved' && (
                              <button
                                onClick={() => handleConfirmAndUnlock(row.id)}
                                className="px-2.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition cursor-pointer flex items-center gap-1 shadow-2xs"
                                title="1-Click Confirm & Unlock Full Access"
                              >
                                <Check className="w-3.5 h-3.5" />
                                <span>Confirm &amp; Unlock</span>
                              </button>
                            )}

                            {row.status !== 'rejected' && (
                              <button
                                onClick={() => handleRejectAndRevoke(row.id)}
                                className="px-2 py-1.5 rounded-lg hover:bg-rose-50 text-rose-600 text-xs font-semibold transition cursor-pointer flex items-center gap-1"
                                title="Reject and Revoke Access"
                              >
                                <X className="w-3.5 h-3.5" />
                                <span>Reject</span>
                              </button>
                            )}
                          </div>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        )}
      </main>

      {/* ========================================================= */}
      {/* MODAL 1: INVITE TEACHER & FACULTY JOIN LINK */}
      {/* ========================================================= */}
      {isInviteModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/50 backdrop-blur-xs">
          <div className="bg-white rounded-2xl max-w-lg w-full border border-slate-200 shadow-2xl p-6 relative animate-fade-in-up">
            <button
              onClick={() => setIsInviteModalOpen(false)}
              className="absolute top-4 right-4 text-slate-400 hover:text-slate-600 p-1 rounded-md"
            >
              <X className="w-5 h-5" />
            </button>

            <div className="flex items-center space-x-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-blue-100 text-[#13519C] flex items-center justify-center">
                <UserPlus className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-xl font-bold text-slate-900 font-afacad">
                  Invite Faculty Educator
                </h3>
                <p className="text-xs text-slate-500">
                  Onboard a new high school teacher to Fundile School Admin with verified curriculum permissions.
                </p>
              </div>
            </div>

            {/* Quick Share Link Box */}
            <div className="bg-slate-50 border border-slate-200 rounded-xl p-3.5 mb-5">
              <div className="text-xs font-semibold text-slate-700 mb-1.5 flex items-center justify-between">
                <span>Direct Faculty Join Link:</span>
                <span className="text-[11px] text-emerald-600 font-medium">Valid for 30 days</span>
              </div>
              <div className="flex items-center space-x-2">
                <input
                  type="text"
                  readOnly
                  value="https://fundile.app/join/faculty?school=FundileHigh&token=FD-FAC-2026-X89"
                  className="w-full bg-white border border-slate-200 rounded-lg text-xs px-2.5 py-1.5 font-mono text-slate-600 focus:outline-none"
                />
                <button
                  onClick={handleCopyFacultyLink}
                  className="bg-[#13519C] hover:bg-[#0f3e77] text-white px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors flex items-center space-x-1 shrink-0 cursor-pointer"
                >
                  {copiedInviteLink ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
                  <span>{copiedInviteLink ? 'Copied' : 'Copy'}</span>
                </button>
              </div>
            </div>

            {/* Form */}
            <form onSubmit={handleSubmitInvite} className="space-y-4 text-xs">
              <div>
                <label className="block font-semibold text-slate-700 mb-1">
                  Full Name & Title <span className="text-rose-500">*</span>
                </label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Mrs. L. Mazibuko"
                  value={inviteForm.name}
                  onChange={(e) => setInviteForm({ ...inviteForm, name: e.target.value })}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-[#13519C]"
                />
              </div>

              <div>
                <label className="block font-semibold text-slate-700 mb-1">
                  Official Email Address <span className="text-rose-500">*</span>
                </label>
                <input
                  type="email"
                  required
                  placeholder="l.mazibuko@fundile.school.za"
                  value={inviteForm.email}
                  onChange={(e) => setInviteForm({ ...inviteForm, email: e.target.value })}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-[#13519C]"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block font-semibold text-slate-700 mb-1">Department</label>
                  <select
                    value={inviteForm.department}
                    onChange={(e) => setInviteForm({ ...inviteForm, department: e.target.value })}
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-2 text-slate-800 focus:outline-none focus:ring-1 focus:ring-[#13519C]"
                  >
                    <option value="Commerce">Commerce & Management</option>
                    <option value="STEM">STEM (Mathematics)</option>
                    <option value="Sciences">Physical & Life Sciences</option>
                    <option value="Senior Phase EMS">Senior Phase EMS</option>
                  </select>
                </div>

                <div>
                  <label className="block font-semibold text-slate-700 mb-1">Primary Subject</label>
                  <input
                    type="text"
                    required
                    placeholder="e.g. Accounting"
                    value={inviteForm.subject}
                    onChange={(e) => setInviteForm({ ...inviteForm, subject: e.target.value })}
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-[#13519C]"
                  />
                </div>
              </div>

              <div>
                <label className="block font-semibold text-slate-700 mb-1">Grade Allocation</label>
                <select
                  value={inviteForm.grades}
                  onChange={(e) => setInviteForm({ ...inviteForm, grades: e.target.value })}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-2 text-slate-800 focus:outline-none focus:ring-1 focus:ring-[#13519C]"
                >
                  <option value="Gr 10–12">Grades 10–12 (FET Phase)</option>
                  <option value="Gr 7–9">Grades 7–9 (Senior Phase)</option>
                  <option value="Gr 10–11">Grades 10–11</option>
                  <option value="Gr 12">Grade 12 Only</option>
                </select>
              </div>

              <div className="pt-3 flex items-center justify-end space-x-2.5">
                <button
                  type="button"
                  onClick={() => setIsInviteModalOpen(false)}
                  className="px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 font-semibold cursor-pointer"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="bg-[#13519C] hover:bg-[#0f3e77] text-white px-5 py-2 rounded-xl font-bold shadow-xs transition-colors cursor-pointer"
                >
                  Dispatch Invitation
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* ========================================================= */}
      {/* MODAL 2: ATP SYLLABUS DETAIL INSPECTOR */}
      {/* ========================================================= */}
      {inspectingSubject && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/50 backdrop-blur-xs">
          <div className="bg-white rounded-2xl max-w-2xl w-full border border-slate-200 shadow-2xl p-6 relative max-h-[85vh] overflow-y-auto animate-fade-in-up">
            <button
              onClick={() => setInspectingSubject(null)}
              className="absolute top-4 right-4 text-slate-400 hover:text-slate-600 p-1 rounded-md"
            >
              <X className="w-5 h-5" />
            </button>

            <div className="flex items-center space-x-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-blue-100 text-[#13519C] flex items-center justify-center font-bold">
                <BookOpen className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-xl font-bold text-slate-900 font-afacad">
                  Curriculum ATP Schedule: {inspectingSubject.subject} Grade {inspectingSubject.grade}
                </h3>
                <p className="text-xs text-slate-500">
                  HOD: <span className="font-semibold text-slate-700">{inspectingSubject.hod}</span> • Term {selectedTerm} (Weeks 1–{inspectingSubject.totalWeeks})
                </p>
              </div>
            </div>

            {/* Pacing Overview Banner */}
            <div className="bg-slate-50 border border-slate-200/90 rounded-xl p-3.5 mb-5 flex items-center justify-between text-xs">
              <div>
                <span className="text-slate-400 uppercase text-[10px] font-semibold">Pacing Progress</span>
                <div className="font-bold text-slate-800 text-sm font-mono">{inspectingSubject.curriculumCovered}% Covered</div>
              </div>
              <div>
                <span className="text-slate-400 uppercase text-[10px] font-semibold">Class Mastery</span>
                <div className="font-bold text-emerald-600 text-sm font-mono">{inspectingSubject.masteryDepth}% Average</div>
              </div>
              <div>
                <span className="text-slate-400 uppercase text-[10px] font-semibold">Current Week</span>
                <div className="font-bold text-slate-800 text-sm font-mono">Week {inspectingSubject.currentWeek} of {inspectingSubject.totalWeeks}</div>
              </div>
            </div>

            {/* Week-by-Week Topics */}
            <div className="space-y-2 mb-6">
              <div className="text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
                Weekly Teaching Plan Breakdown
              </div>
              {inspectingSubject.weeklyTopics.map((w) => (
                <div
                  key={w.week}
                  className={`p-3 rounded-xl border text-xs flex items-center justify-between transition-colors ${
                    w.status === 'in_progress'
                      ? 'bg-blue-50/70 border-blue-200 text-blue-900'
                      : w.status === 'completed'
                      ? 'bg-white border-slate-200 text-slate-800'
                      : 'bg-slate-50/50 border-dashed border-slate-200 text-slate-400'
                  }`}
                >
                  <div className="flex items-center space-x-3">
                    <span className="w-6 h-6 rounded-md bg-slate-200/70 text-slate-700 font-mono font-bold flex items-center justify-center text-[11px]">
                      W{w.week}
                    </span>
                    <div>
                      <div className="font-semibold">{w.topic}</div>
                      <div className="text-[11px] text-slate-400">
                        {w.status === 'completed' && '✓ Covered & assessed'}
                        {w.status === 'in_progress' && '⚡ Currently active lesson'}
                        {w.status === 'scheduled' && 'Scheduled for upcoming weeks'}
                      </div>
                    </div>
                  </div>

                  {w.mastery !== null && (
                    <div className="text-right">
                      <span className={`font-mono font-bold text-xs ${w.mastery >= 65 ? 'text-emerald-600' : 'text-amber-600'}`}>
                        {w.mastery}%
                      </span>
                      <div className="text-[10px] text-slate-400">mastery</div>
                    </div>
                  )}
                </div>
              ))}
            </div>

            <div className="flex justify-end space-x-2">
              <button
                onClick={() => setInspectingSubject(null)}
                className="bg-slate-100 hover:bg-slate-200 text-slate-700 px-4 py-2 rounded-xl text-xs font-bold transition-colors cursor-pointer"
              >
                Close Inspector
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================= */}
      {/* MODAL 3: REMEDIAL DRILL QUESTION PREVIEW */}
      {/* ========================================================= */}
      {activePreviewDrill && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/50 backdrop-blur-xs">
          <div className="bg-white rounded-2xl max-w-xl w-full border border-slate-200 shadow-2xl p-6 relative max-h-[85vh] overflow-y-auto animate-fade-in-up">
            <button
              onClick={() => setActivePreviewDrill(null)}
              className="absolute top-4 right-4 text-slate-400 hover:text-slate-600 p-1 rounded-md"
            >
              <X className="w-5 h-5" />
            </button>

            <div className="flex items-center space-x-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-rose-100 text-rose-600 flex items-center justify-center">
                <Radio className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-xl font-bold text-slate-900 font-afacad">
                  Remedial Micro-Drill Preview
                </h3>
                <p className="text-xs text-slate-500">
                  {activePreviewDrill.remedialDrillTitle} (Grade {activePreviewDrill.grade} {activePreviewDrill.subject})
                </p>
              </div>
            </div>

            {/* Educator Guide Quote */}
            <div className="bg-amber-50 border border-amber-200 rounded-xl p-3.5 mb-5 text-xs text-amber-900">
              <div className="font-bold flex items-center space-x-1.5 text-amber-800 mb-1">
                <Sparkles className="w-3.5 h-3.5" />
                <span>Suggested 5-Minute Educator Homeroom Opener:</span>
              </div>
              <div className="italic leading-relaxed">
                "{activePreviewDrill.educatorTalkingPoints}"
              </div>
            </div>

            {/* Questions List */}
            <div className="space-y-4 mb-6">
              <div className="text-xs font-bold text-slate-700 uppercase tracking-wider">
                Micro-Drill Questions ({activePreviewDrill.drillQuestions.length} Items)
              </div>

              {activePreviewDrill.drillQuestions.map((qItem, idx) => (
                <div key={idx} className="bg-slate-50 border border-slate-200/80 rounded-xl p-4 text-xs space-y-2.5">
                  <div className="font-bold text-slate-800">
                    Q{idx + 1}: {qItem.q}
                  </div>

                  <div className="grid grid-cols-1 gap-1.5 pl-2">
                    {qItem.options.map((opt, oIdx) => (
                      <div
                        key={oIdx}
                        className={`px-3 py-1.5 rounded-lg border text-xs flex items-center justify-between ${
                          opt === qItem.answer
                            ? 'bg-emerald-50 border-emerald-300 text-emerald-800 font-semibold'
                            : 'bg-white border-slate-200 text-slate-600'
                        }`}
                      >
                        <span>{opt}</span>
                        {opt === qItem.answer && (
                          <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-600">Correct Answer</span>
                        )}
                      </div>
                    ))}
                  </div>

                  <div className="text-[11px] text-slate-500 bg-white p-2 rounded-md border border-slate-100">
                    <strong className="text-slate-700">Curriculum Rationale:</strong> {qItem.explanation}
                  </div>
                </div>
              ))}
            </div>

            {/* Footer Broadcast Action */}
            <div className="flex items-center justify-between pt-3 border-t border-slate-100">
              <button
                onClick={() => setActivePreviewDrill(null)}
                className="text-slate-500 hover:text-slate-700 text-xs font-semibold px-3 py-1.5"
              >
                Close Preview
              </button>

              <button
                onClick={() => {
                  handleBroadcastRemedialDrill(activePreviewDrill);
                  setActivePreviewDrill(null);
                }}
                className="bg-rose-600 hover:bg-rose-700 text-white px-4 py-2 rounded-xl text-xs font-bold shadow-xs transition-colors flex items-center space-x-1.5 cursor-pointer"
              >
                <Send className="w-3.5 h-3.5" />
                <span>Broadcast to All Grade {activePreviewDrill.grade} Classes</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================= */}
      {/* MODAL 4: PROOF OF PAYMENT SLIP INSPECTOR */}
      {/* ========================================================= */}
      {selectedSlipModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs animate-fade-in">
          <div className="bg-white rounded-2xl max-w-xl w-full border border-slate-200 shadow-2xl p-6 relative">
            <button
              onClick={() => setSelectedSlipModal(null)}
              className="absolute top-4 right-4 text-slate-400 hover:text-slate-600 p-1.5 rounded-lg hover:bg-slate-100 transition cursor-pointer"
            >
              <X className="w-5 h-5" />
            </button>

            <div className="flex items-center space-x-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center border border-emerald-200/50">
                <FileCheck className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-xl font-bold text-slate-900 font-afacad">
                  Access Bank Payment Slip Inspection
                </h3>
                <p className="text-xs text-slate-500 font-mono">
                  File: {selectedSlipModal.receiptFileName} • Reference: {selectedSlipModal.reference}
                </p>
              </div>
            </div>

            {/* Document Preview Rendering */}
            <div className="border border-slate-200 rounded-xl p-4 bg-slate-50 space-y-3 mb-5">
              <div className="flex items-center justify-between border-b border-slate-200 pb-2">
                <div className="flex items-center gap-2">
                  <span className="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                  <span className="text-xs font-bold text-slate-800 uppercase tracking-wide">
                    Access Bank South Africa
                  </span>
                </div>
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold">
                  DIRECT FUNDS TRANSFER
                </span>
              </div>

              <div className="grid grid-cols-2 gap-3 text-xs">
                <div>
                  <span className="text-slate-400 block text-[10px] uppercase">Payer / Learner:</span>
                  <strong className="text-slate-900 font-semibold">{selectedSlipModal.learnerName}</strong>
                  <div className="text-[11px] text-slate-500">{selectedSlipModal.email}</div>
                </div>
                <div>
                  <span className="text-slate-400 block text-[10px] uppercase">Amount Paid:</span>
                  <strong className="text-emerald-700 font-mono text-base font-extrabold">{selectedSlipModal.amount}</strong>
                </div>
                <div>
                  <span className="text-slate-400 block text-[10px] uppercase">Beneficiary Account:</span>
                  <strong className="text-slate-800 font-mono">Fundile EdTech (Pty) Ltd</strong>
                  <div className="text-[11px] text-slate-600 font-mono">Access Bank • 410 882 9104</div>
                </div>
                <div>
                  <span className="text-slate-400 block text-[10px] uppercase">Branch &amp; Reference:</span>
                  <div className="text-slate-800 font-mono">410506 (Universal)</div>
                  <strong className="text-cyan-700 font-mono">{selectedSlipModal.reference}</strong>
                </div>
              </div>

              {/* AI Verification Breakdown */}
              <div className="mt-3 p-3 rounded-lg bg-white border border-slate-200 text-xs space-y-1.5">
                <div className="flex items-center justify-between">
                  <span className="font-bold text-slate-700 flex items-center gap-1.5">
                    <Sparkles className="w-3.5 h-3.5 text-blue-600" />
                    <span>AI Auditor Confidence:</span>
                  </span>
                  <span className="font-mono font-bold text-slate-900">{selectedSlipModal.aiConfidence}%</span>
                </div>
                <div className="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
                  <div
                    className={`h-full rounded-full ${
                      selectedSlipModal.aiConfidence >= 80
                        ? 'bg-emerald-500'
                        : selectedSlipModal.aiConfidence >= 50
                        ? 'bg-amber-500'
                        : 'bg-rose-500'
                    }`}
                    style={{ width: `${selectedSlipModal.aiConfidence}%` }}
                  />
                </div>
                <p className="text-[11px] text-slate-600 leading-relaxed pt-1">
                  <strong>Notes:</strong> {selectedSlipModal.aiNotes}
                </p>
              </div>
            </div>

            {/* Modal Actions */}
            <div className="flex items-center justify-between gap-2 pt-2 border-t border-slate-100">
              <button
                onClick={() => handleRejectAndRevoke(selectedSlipModal.id)}
                className="px-4 py-2 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-700 text-xs font-bold transition cursor-pointer"
              >
                Reject &amp; Revoke Grace
              </button>

              <div className="flex items-center gap-2">
                <button
                  onClick={() => setSelectedSlipModal(null)}
                  className="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold transition cursor-pointer"
                >
                  Close
                </button>
                <button
                  onClick={() => handleConfirmAndUnlock(selectedSlipModal.id)}
                  className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition cursor-pointer shadow-md flex items-center gap-1.5"
                >
                  <Check className="w-4 h-4" />
                  <span>Confirm Access Bank Transfer</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default SchoolAdminView;
