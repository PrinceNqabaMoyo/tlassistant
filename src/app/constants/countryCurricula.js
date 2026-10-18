/**
 * Declarative Pan-African Curriculum & Country Registry
 * 
 * Supports regional differentiation across:
 * - South Africa (/za) [Active Production Engine]
 * - Zimbabwe (/zw)     [Skeleton / Waitlist]
 * - Tanzania (/tz)     [Skeleton / Waitlist]
 * - Kenya (/ke)        [Skeleton / Waitlist]
 * - Ghana (/gh)        [Skeleton / Waitlist]
 * - Nigeria (/ng)      [Skeleton / Waitlist]
 * 
 * INVARIANT: South African user-facing UI must NEVER reference or display the acronym 'CAPS'.
 * Use universal 'National Curriculum Standards' or 'South African National Curriculum'.
 */

export const COUNTRY_CURRICULA = {
  za: {
    code: 'za',
    name: 'South Africa',
    flag: '🇿🇦',
    status: 'active',
    path: '/za',
    curriculumTitle: 'South African National Curriculum Standards',
    shortCurriculum: 'National Curriculum',
    stages: 'Grades 7–12 (Senior & FET Phase)',
    currency: 'ZAR',
    currencySymbol: 'R',
    paymentMethods: 'EFT, Instant EFT, Debit/Credit Card',
    examAlignment: 'Statutory National Senior Certificate standards for public, private & independent examinations',
    plannedSubjects: [
      'Mathematics',
      'Physical Sciences',
      'Life Sciences',
      'Natural Sciences',
      'Mathematical Literacy',
      'Accounting',
      'Business Studies',
      'Economic and Management Sciences (EMS)',
      'Technical Mathematics',
    ],
  },
  zw: {
    code: 'zw',
    name: 'Zimbabwe',
    flag: '🇿🇼',
    status: 'coming_soon',
    path: '/zw',
    curriculumTitle: 'ZIMSEC & Cambridge International Curriculum',
    shortCurriculum: 'ZIMSEC / Cambridge',
    stages: 'Forms 1–4 (O-Level) & Forms 5–6 (A-Level)',
    currency: 'USD / ZiG',
    currencySymbol: '$',
    paymentMethods: 'EcoCash, InnBucks, Local Banking & Card',
    examAlignment: 'Aligned with Zimbabwe School Examinations Council (ZIMSEC) & Cambridge International syllabi',
    heroTitle: 'Master ZIMSEC & Cambridge Secondary Examinations',
    heroEyebrow: 'Zimbabwe Secondary Learning Assistant • Launching Soon',
    tagline: 'Stepwise math derivations, procedural science problems, and commercial ledger practice for Forms 1 to 6.',
    plannedSubjects: [
      'Mathematics (O-Level & A-Level)',
      'Integrated Science / Physical Science',
      'Biology / Life Sciences',
      'Principles of Accounts',
      'Business Studies & Commerce',
      'Pure Mathematics (A-Level)',
      'Physics & Chemistry (A-Level)',
    ],
  },
  tz: {
    code: 'tz',
    name: 'Tanzania',
    flag: '🇹🇿',
    status: 'coming_soon',
    path: '/tz',
    curriculumTitle: 'NECTA National Secondary Curriculum',
    shortCurriculum: 'NECTA',
    stages: 'Forms 1–4 (CSEE / O-Level) & Forms 5–6 (ACSEE / A-Level)',
    currency: 'TZS',
    currencySymbol: 'TSh',
    paymentMethods: 'M-Pesa, Tigo Pesa, Airtel Money & Card',
    examAlignment: 'Aligned with National Examinations Council of Tanzania (NECTA) Form 4 & Form 6 guidelines',
    heroTitle: 'Excel in NECTA Certificate & Advanced Examinations',
    heroEyebrow: 'Tanzania Secondary Learning Assistant • Launching Soon',
    tagline: 'Interactive problem-solving, structured science calculations, and bookkeeping tailored for Tanzanian secondary students.',
    plannedSubjects: [
      'Basic Mathematics (Form 1–4)',
      'Advanced Mathematics (Form 5–6)',
      'Physics & Chemistry',
      'Biology',
      'Bookkeeping & Commerce',
      'Civics & General Studies',
    ],
  },
  ke: {
    code: 'ke',
    name: 'Kenya',
    flag: '🇰🇪',
    status: 'coming_soon',
    path: '/ke',
    curriculumTitle: 'Competency-Based Curriculum (CBC) & KCSE',
    shortCurriculum: 'CBC & KCSE',
    stages: 'Junior Secondary (Grades 7–9) & Senior Secondary (Grades 10–12 / Form 1–4)',
    currency: 'KES',
    currencySymbol: 'KSh',
    paymentMethods: 'M-Pesa (Safaricom), Airtel Money & Card',
    examAlignment: 'Aligned with Kenya Institute of Curriculum Development (KICD) CBC & KNEC examination frameworks',
    heroTitle: 'Master Kenya CBC & KCSE Secondary Learning',
    heroEyebrow: 'Kenya Secondary Learning Assistant • Launching Soon',
    tagline: 'Competency-driven STEM mastery, step-by-step mathematical reasoning, and comprehensive commercial studies.',
    plannedSubjects: [
      'Mathematics (Junior & Senior Secondary)',
      'Integrated Science (Junior Secondary)',
      'Physics, Chemistry & Biology (Senior)',
      'Business Studies',
      'Pre-Technical Studies',
      'Computer Science',
    ],
  },
  gh: {
    code: 'gh',
    name: 'Ghana',
    flag: '🇬🇭',
    status: 'coming_soon',
    path: '/gh',
    curriculumTitle: 'NaCCA & WAEC (BECE & WASSCE)',
    shortCurriculum: 'NaCCA / WASSCE',
    stages: 'Basic 7–9 (JHS 1–3) & Senior High (SHS 1–3)',
    currency: 'GHS',
    currencySymbol: 'GH₵',
    paymentMethods: 'MTN Mobile Money, Telecel Cash & Card',
    examAlignment: 'Aligned with National Council for Curriculum and Assessment (NaCCA) & WAEC examination syllabi',
    heroTitle: 'Empower Ghanaian Students for BECE & WASSCE Distinction',
    heroEyebrow: 'Ghana Secondary Learning Assistant • Launching Soon',
    tagline: 'Stepwise working pads, automated procedure verification, and past-exam standard questions for JHS and SHS scholars.',
    plannedSubjects: [
      'Core Mathematics & Elective Mathematics',
      'Integrated Science',
      'Physics & Chemistry',
      'Biology',
      'Financial Accounting & Cost Accounting',
      'Business Management & Economics',
    ],
  },
  ng: {
    code: 'ng',
    name: 'Nigeria',
    flag: '🇳🇬',
    status: 'coming_soon',
    path: '/ng',
    curriculumTitle: 'WAEC (WASSCE), NECO & UTME / JAMB',
    shortCurriculum: 'WAEC / JAMB',
    stages: 'Junior Secondary (JSS 1–3) & Senior Secondary (SSS 1–3)',
    currency: 'NGN',
    currencySymbol: '₦',
    paymentMethods: 'Paystack, Flutterwave, Bank Transfer & Card',
    examAlignment: 'Aligned with NERDC National Curriculum, WAEC, NECO, and JAMB UTME examination requirements',
    heroTitle: 'Top Scores in WAEC, NECO & UTME / JAMB',
    heroEyebrow: 'Nigeria Secondary Learning Assistant • Launching Soon',
    tagline: 'Unlimited practice, procedural marking, and diagnostic gap closing for JSS and SSS students nationwide.',
    plannedSubjects: [
      'General Mathematics & Further Mathematics',
      'Physics & Chemistry',
      'Biology',
      'Financial Accounting',
      'Commerce & Economics',
      'Basic Science & Technology (JSS 1–3)',
    ],
  },
};

export const SKELETON_COUNTRY_CODES = ['zw', 'tz', 'ke', 'gh', 'ng'];

export const ALL_COUNTRY_CODES = ['za', ...SKELETON_COUNTRY_CODES];

export const getCountryConfig = (code = 'za') => {
  const normalized = String(code).toLowerCase().replace(/[^a-z]/g, '');
  return COUNTRY_CURRICULA[normalized] || COUNTRY_CURRICULA.za;
};
