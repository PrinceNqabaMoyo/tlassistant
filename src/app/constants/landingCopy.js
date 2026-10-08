// Marketing copy for the landing page, kept in one place so wording — especially
// the legally sensitive CAPS / NSC / examining-body section — can be reviewed and
// edited without touching layout. Treat the CAPS/NSC copy as sign-off material.

export const HERO_COPY = {
    eyebrow: 'Teaching & Learning Assistant + LMS • Grades 7–12',
    // title is now handled as a typing animation in LandingPage.jsx
    // 'typingSubjects' drives the animated part
    titlePrefix: 'Excel in',
    typingSubjects: [
        'Mathematics.',
        'Physical Sciences.',
        'Life Sciences.',
        'Natural Sciences.',
        'Mathematical Literacy.',
        'EMS.',
        'Accounting.',
        'Business Studies.',
    ],
    tagline: 'Use Fundile, become a top student.',
    bullets: [
        'Unlimited practice, multiple subjects, one fee.',
        'Adaptive learning: diagnostic test, personalized progression, and unlimited, newly-created, unique exam sets for each subject.',
        'Fundile tells you where you went wrong and focuses on closing your knowledge gaps.',
    ],
    imageAlt: 'South African learners studying with Fundile',
    imageCaption: 'For every South African learner — whatever school, whatever exam.',
    primaryCta: 'Start 2-week free trial',
    mobileSimCta: 'See what you get ↓',
    trialNote: '2-week free trial. No card required. Cancel anytime.',
};

export const EXPLORE_COPY = {
    title: 'Try Fundile now — no signup required',
    buttonText: 'Explore',
    gradeOptions: ['Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12'],
    subjectOptions: {
        'Grade 7': ['Economic and Management Sciences', 'Mathematics', 'Natural Sciences'],
        'Grade 8': ['Economic and Management Sciences', 'Mathematics', 'Natural Sciences'],
        'Grade 9': ['Economic and Management Sciences', 'Mathematics', 'Natural Sciences'],
        'Grade 10': ['Mathematics', 'Accounting', 'Business Studies', 'Physical Sciences', 'Life Sciences', 'Mathematical Literacy', 'Technical Mathematics'],
        'Grade 11': ['Mathematics', 'Accounting', 'Business Studies', 'Physical Sciences', 'Life Sciences', 'Mathematical Literacy', 'Technical Mathematics'],
        'Grade 12': ['Mathematics', 'Accounting', 'Business Studies', 'Physical Sciences', 'Life Sciences', 'Mathematical Literacy', 'Technical Mathematics'],
    },
    // Topic options are loaded dynamically from curriculum data based on grade + subject
    selectGradePrompt: 'Select your grade',
    selectSubjectPrompt: 'Select a subject',
    selectTopicPrompt: 'Select a topic',
    questionLabel: 'Question {n} of 3',
    answerPlaceholder: 'Type your answer here...',
    submitAnswer: 'Submit answer',
    nextQuestion: 'Next question',
    feedbackTitle: 'Feedback',
    subscribePopup: {
        title: "You've used your 3 free Explore questions",
        body: 'Start your 2-week free trial for unlimited practice + a personal improvement plan based on your work.',
        cta: 'Start 2-week free trial',
        dismiss: 'Maybe later',
    },
};

// "The hidden curriculum" — the problem we remove.
export const HIDDEN_CURRICULUM = {
    eyebrow: 'The hidden curriculum',
    title: 'Most learners are surprised by the exam. They should not be.',
    body:
        'Day-to-day classwork rarely looks like the final exam, so the real "rules of the game" stay hidden until it is too late. Fundile closes that gap: every topic is practised at exam standard, with transparent feedback on exactly where you went wrong — no surprises in November.',
    points: [
        {
            title: 'Exam-standard from day one',
            body: 'Practice questions are pitched at authentic exam level from the first topic, not only at revision time.',
        },
        {
            title: 'See where you went wrong',
            body: 'Step-by-step marking shows the exact line your method broke down — and still credits the work that was correct.',
        },
        {
            title: 'Unlimited practice',
            body: 'Deterministic generators produce endless fresh variants of any question, so you practise until it is automatic.',
        },
    ],
};

// How it works — 3 steps.
export const HOW_IT_WORKS = {
    eyebrow: 'How it works',
    title: 'A structured, adaptive learning system.',
    steps: [
        {
            step: '01',
            title: 'Pick a Topic or Take a Diagnostic',
            body: 'Choose the exact subject, grade, and topic you need, or begin with a diagnostic autopsy that pinpoints your baseline against the national curriculum.',
        },
        {
            step: '02',
            title: 'Scaffold → Practice → Assessment',
            body: 'Progress through guided scaffolding, move to independent practice, and unlock exam-standard assessments with pre-baked 3-tier hints.',
        },
        {
            step: '03',
            title: 'Precision Gap Autopsy & Micro-Drills',
            body: 'If your working stumbles, Fundile isolates the exact flawed step, awards consequential method marks, and deploys targeted 5-minute drills and SimuLearn visual animations.',
        },
    ],
};

// Curriculum & Examination alignment — Rule 2b compliant.
export const CAPS_NSC = {
    eyebrow: 'Curriculum Standards & Exam Alignment',
    title: 'The difference is not the curriculum — it is the preparation.',
    didYouKnow:
        'Did you know? There is only one official national curriculum standard in South Africa, which underpins public, private, and independent school examinations nationwide.',
    intro:
        'Many families believe private or independent schools follow a completely different curriculum. In reality, the South African National Curriculum forms the statutory foundation for all schools—the difference lies in preparation and assessment depth. Fundile prepares learners to excel at the highest level of examination standards.',
    aligned: {
        heading: '100% Aligned with National Curriculum Standards',
        body: 'Fundile is built directly on South African National Curriculum statements, preparing learners for:',
        bodies: ['Public school examinations', 'Independent & private school examinations', 'Distance & home-education assessments'],
    },
    flow: {
        foundation: {
            label: 'National Curriculum Standards',
            caption: 'The official South African national curriculum statements (what must be learned), Grades 7–12.',
        },
        bodies: [
            { label: 'Public Schools', caption: 'National state curriculum examinations' },
            { label: 'Independent Schools', caption: 'Private & independent school examinations' },
            { label: 'Distance & Homeschool', caption: 'Independent assessment bodies' },
        ],
        outcome: {
            label: 'Universal NSC',
            caption: 'Authentic National Senior Certificate preparation, quality-assured and benchmarked for university entry.',
        },
    },
    table: {
        columns: ['Public Schools', 'Independent Schools', 'Distance & Home Education'],
        rows: [
            {
                label: 'Curriculum Standard',
                values: ['South African National Curriculum', 'South African National Curriculum', 'South African National Curriculum'],
            },
            {
                label: 'Qualification',
                values: ['National Senior Certificate', 'National Senior Certificate', 'National Senior Certificate'],
            },
            {
                label: 'Quality Assurance',
                values: ['National Quality Standard', 'National Quality Standard', 'National Quality Standard'],
            },
            {
                label: 'Assessment Style',
                values: [
                    'Standardized national examination format',
                    'Higher-order cognitive & application emphasis',
                    'Flexible, continuous & independent assessment',
                ],
            },
        ],
    },
    framing:
        'Built on the South African National Curriculum statements behind the Senior Certificate — Fundile prepares you for your exams whether you study in public, private, or independent schools nationwide.',
    disclaimer:
        'Fundile is an independent educational platform aligned with the official South African National Curriculum Statements. All examination board names and trademarks belong to their respective owners.',
};

export const INTERNAL_CONSISTENCY = {
    title: 'Internally consistent, always.',
    body: 'Every question and its answer are generated from the same underlying logic, so they are always internally consistent. If you ever spot a discrepancy, tell us — we will fix it.',
    cta: 'Report a discrepancy',
    ctaHref: 'mailto:info@fundile.com?subject=Question%20discrepancy%20report',
};

export const TEACHERS_LINK = {
    text: 'Fundile for teachers, tutors, and schools is live.',
    cta: 'Explore School & Teacher Cockpit',
    href: '#teachers-simulation',
};

// Pricing anchor — real alternative is private tutoring.
export const PRICING_COPY = {
    eyebrow: 'Pricing',
    title: 'One subscription. Every subject. Less than one tutoring hour.',
    anchor:
        'Private tutoring in South Africa runs roughly R50–R200 an hour. Even three sessions a week at the low end is about R150 × 4 weeks = R600+ a month — for one subject. Fundile covers every subject and is available any time.',
    trial: {
        duration: '2 weeks',
        cardRequired: false,
        cancelAnytime: true,
        includes: 'Full Standard access — every feature, every subject across Grades 7–12',
    },
    trialValueProp:
        'At the end of your trial, Fundile tells you exactly what you need to improve and how — based on your actual work, not a guess.',
    tiers: [
        {
            key: 'standard',
            name: 'Standard',
            price: 'R150',
            cadence: '/ month',
            description: 'Unlimited deterministic practice across subjects, adaptive progression, and scaffolded, exam-standard questions with step-by-step marking.',
            badge: 'Live now',
            cta: 'Start free trial',
        },
        {
            key: 'pro',
            name: 'Pro',
            price: 'R299',
            cadence: '/ month',
            description: 'Everything in Standard, plus an on-rails Socratic AI tutor with dynamic suggestion chips, SimuLearn animated worked solutions, and targeted prerequisite micro-lessons.',
            badge: 'Live • 2-Week Free Trial',
            cta: 'Start 2-week free trial',
        },
    ],
};

export const FAQ = {
    eyebrow: 'Questions',
    title: 'Straight answers.',
    items: [
        {
            q: 'How is Fundile aligned to my child’s school curriculum?',
            a: 'In South Africa, all public, private, and independent schools follow the same underlying national curriculum statements for the National Senior Certificate. Fundile is 100% aligned with these national academic standards, ensuring your child develops the exact core competencies, problem-solving methods, and exam techniques required regardless of which examination board sets their final paper.',
        },
        {
            q: 'Which subjects and grades are available?',
            a: 'Fundile covers Grades 7 to 12 across all core subjects: Mathematics, Physical Sciences, Life Sciences, Natural Sciences, Mathematical Literacy, Economic & Management Sciences (EMS), Accounting, and Business Studies. Additional electives and language modules are expanded based on learner demand.',
        },
        {
            q: 'Can an individual learner subscribe independently of their school?',
            a: 'Yes! Individual learners and parents can subscribe directly and access the full suite of subjects and diagnostic reports. If their school later adopts Fundile, their account can seamlessly link to their teacher’s classroom using a school code without losing any history or progress.',
        },
        {
            q: 'How is this cheaper than a private tutor?',
            a: 'One Fundile subscription covers every subject 24/7 for less than the cost of a single private tutoring session a month. Tutors charge per hour, per subject; Fundile gives you unlimited practice across all subjects.',
        },
        {
            q: 'Is my child’s personal information safe?',
            a: 'Yes. Fundile is strictly compliant with the Protection of Personal Information Act (POPIA), including Section 35 protections for children’s personal data. We never sell student data or use learner responses for commercial advertising.',
        },
    ],
};
