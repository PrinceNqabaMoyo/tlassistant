// Marketing copy for the landing page, kept in one place so wording — especially
// the legally sensitive CAPS / NSC / examining-body section — can be reviewed and
// edited without touching layout. Treat the CAPS/NSC copy as sign-off material.

export const HERO_COPY = {
    eyebrow: 'Built for the South African high-school learner',
    title: 'Helping you master high school.',
    subtitle:
        'Every subject, unlimited exam-standard practice, and feedback that shows you exactly where you went wrong — for less than the cost of a single private-tutoring hour a month. Fundile prepares you for the exam from your very first session, so you are never caught by surprise.',
    imageAlt: 'South African high-school learners studying together with Fundile',
    imageCaption: 'For every South African learner — whatever school, whatever exam.',
    primaryCta: 'Start free',
    secondaryCta: 'See how it works',
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
            body: 'Practice questions are pitched at NSC exam level from the first topic, not only at revision time.',
        },
        {
            title: 'See where you went wrong',
            body: 'Step-by-step marking shows the exact line your method broke down — and still credits the work that was correct.',
        },
        {
            title: 'Unlimited practice',
            body: 'Generators produce endless fresh variants of any question, so you practise until it is automatic.',
        },
    ],
};

// How it works — 3 steps.
export const HOW_IT_WORKS = {
    eyebrow: 'How it works',
    title: 'A single, focused learning flow.',
    steps: [
        {
            step: '01',
            title: 'Pick a topic',
            body: 'Choose the exact subject and topic you need — no aimless searching.',
        },
        {
            step: '02',
            title: 'Scaffold → Practice → Assessment',
            body: 'Move through guided scaffolding, then practice, then an exam-style assessment, unlocking as you master each stage.',
        },
        {
            step: '03',
            title: 'Learn from feedback',
            body: 'A tutor that shows you where your working went wrong and how to fix it — so the next attempt is stronger.',
        },
    ],
};

// CAPS / NSC clarity — the trust centrepiece. Wording follows what each body
// itself publishes; it never implies endorsement by any body.
export const CAPS_NSC = {
    eyebrow: 'CAPS, the NSC & the examining bodies',
    title: 'The difference is not the curriculum — it is the preparation.',
    didYouKnow:
        'Did you know? CAPS is the South African national curriculum on which the IEB, SACAI and DBE high-school exams are all based.',
    intro:
        'Many families believe the IEB or SACAI teach a different, "superior" curriculum to the DBE. In reality there is one national curriculum, and Fundile prepares you for the same National Senior Certificate whichever body sets your exam.',
    // Plain-language "curriculum aligned" promise, in the user's words.
    aligned: {
        heading: 'Curriculum aligned',
        body: 'Fundile is built on the CAPS curriculum. With Fundile you can master your subjects to excel whether you sit for:',
        bodies: ['the IEB', 'SACAI', "the government's DBE examination"],
    },
    // CAPS -> three bodies -> one NSC.
    flow: {
        foundation: {
            label: 'CAPS',
            caption: 'The South African national curriculum (what must be learned), Grades R–12.',
        },
        bodies: [
            { label: 'DBE', caption: 'Public-school examinations' },
            { label: 'IEB', caption: 'Independent examinations' },
            { label: 'SACAI', caption: 'Private/home-education examinations' },
        ],
        outcome: {
            label: 'One NSC',
            caption: 'The same National Senior Certificate qualification, quality-assured by Umalusi.',
        },
    },
    // Comparison table — first rows identical across bodies (that is the point);
    // only the last row differs.
    table: {
        columns: ['DBE', 'IEB', 'SACAI'],
        rows: [
            {
                label: 'Curriculum',
                values: ['South African National Curriculum', 'South African National Curriculum', 'South African National Curriculum'],
            },
            {
                label: 'Qualification',
                values: ['National Senior Certificate', 'National Senior Certificate', 'National Senior Certificate'],
            },
            {
                label: 'Quality assured by',
                values: ['Umalusi', 'Umalusi', 'Umalusi'],
            },
            {
                label: 'What differs',
                values: [
                    'Assessment style & school-based assessment',
                    'Assessment style & emphasis (internationally benchmarked)',
                    'Assessment style for private & home education',
                ],
            },
        ],
    },
    // Safe framing line, per locked wording.
    framing:
        'Built on the CAPS curriculum — the South African National Curriculum behind the NSC — Fundile prepares you for your NSC exams whether they are set by the DBE, IEB or SACAI.',
    disclaimer:
        'Fundile aligns to CAPS and prepares learners for the NSC. Fundile is not affiliated with, or endorsed by, the DBE, IEB, SACAI or Umalusi.',
};

export const AUDIENCES = {
    eyebrow: 'Who it is for',
    title: 'Built for learners first — with teachers, tutors and families alongside.',
    cards: [
        {
            key: 'students',
            title: 'For students',
            body: 'Structure, unlimited exam-standard practice, and feedback that tells you exactly what to fix.',
            cta: 'Start free',
            badge: 'Live now',
        },
        {
            key: 'teachers',
            title: 'For teachers & tutors',
            body: 'Assign work, review learners’ working, and set tasks that learners complete flexibly, any time.',
            cta: 'Coming soon',
            badge: 'Coming soon',
        },
        {
            key: 'families',
            title: 'For parents',
            body: 'One affordable subscription covering every subject — purposeful, supportive, and curriculum-aware.',
            cta: 'See pricing',
            badge: 'Live now',
        },
    ],
};

// Pricing anchor — real alternative is private tutoring.
export const PRICING_COPY = {
    eyebrow: 'Pricing',
    title: 'One subscription. Every subject. Less than one tutoring hour.',
    anchor:
        'Private tutoring in South Africa runs roughly R50–R200 an hour. Even three sessions a week at the low end is about R150 × 4 weeks = R600+ a month — for one subject. Fundile covers every subject and is available any time.',
    tiers: [
        {
            key: 'free',
            name: 'Free',
            price: 'R0',
            cadence: 'forever',
            description: 'A safe place to start: topic tracking, curriculum outlines, and selected practice generators.',
            badge: 'Always free',
            cta: 'Start free',
        },
        {
            key: 'standard',
            name: 'Standard',
            price: 'R150',
            cadence: '/ month',
            description: 'Unlimited deterministic practice across subjects, adaptive progression, and scaffolded, exam-standard questions with step-by-step marking.',
            badge: 'Live now',
            cta: 'Start Standard',
        },
        {
            key: 'pro',
            name: 'Pro',
            price: 'R299',
            cadence: '/ month',
            description: 'Everything in Standard, plus a live Socratic AI tutor that diagnoses your working in real time and adapts to your weak subskills.',
            badge: 'Coming soon',
            cta: 'Explore Pro',
        },
    ],
};

export const FAQ = {
    eyebrow: 'Questions',
    title: 'Straight answers.',
    items: [
        {
            q: 'Does Fundile teach the DBE, IEB or SACAI "curriculum"?',
            a: 'There is one national curriculum — CAPS. The DBE, IEB and SACAI are all examining bodies that assess the same National Senior Certificate against CAPS, and all are quality-assured by Umalusi. They differ in assessment style and emphasis, not in the underlying curriculum. Fundile is built on CAPS and prepares you for the NSC whichever body sets your exam.',
        },
        {
            q: 'Is the IEB or SACAI exam "harder" than the DBE?',
            a: 'They are different in style, not in curriculum. Each body sets its own papers and school-based assessment to the same NSC standard under Umalusi. What actually moves results is exam-level preparation — which Fundile gives every learner from day one.',
        },
        {
            q: 'Which subjects and grades are available?',
            a: 'Accounting (Grade 10 & 11) is live now, with Mathematics and more subjects rolling out. Tell us what you need next and we prioritise rollout from real demand.',
        },
        {
            q: 'How is this cheaper than a tutor?',
            a: 'One Fundile subscription covers every subject and is available any time, for less than a single private-tutoring hour a month. A tutor charges per hour, per subject.',
        },
        {
            q: 'Can teachers and tutors use it with their students?',
            a: 'Teacher and tutor collaboration — assigning work, reviewing learners’ working, and setting tasks — is coming soon. Register your interest and we will let you know when it lands.',
        },
        {
            q: 'Is my information safe?',
            a: 'Yes. Fundile approaches personal information with POPIA-aligned privacy responsibilities. You can read our privacy statement any time.',
        },
    ],
};

export const COLLAB_COMING_SOON = {
    title: 'Teacher & tutor collaboration is coming soon',
    body: 'A shared space for teachers, tutors and students to assign work, review working, and complete tasks flexibly — any time. Register your interest and we will tell you the moment it is ready.',
};

// How Fundile teaches — the four principles in the user's words.
export const PRINCIPLES = {
    eyebrow: 'How Fundile teaches',
    title: 'A learning method, not a search box.',
    items: [
        {
            title: 'Topically sequenced',
            body: 'Work through each subject in the order the curriculum builds it, so every topic stands on the one before it.',
        },
        {
            title: 'Personalised adaptive progression',
            body: 'Fundile tracks the subskills you have mastered and the ones you have not, then sends you exactly where you need to practise next.',
        },
        {
            title: 'Understanding over answers',
            body: 'We prioritise developing real understanding instead of handing out the answer — you do the thinking, Fundile fills the gaps.',
        },
        {
            title: 'Procedure over final product',
            body: 'We mark your method like an exam, not just your final answer — because in the NSC your working earns the marks.',
        },
    ],
};

// "Fundile is NOT an AI chatbot" — the core differentiation, in the user's words.
export const NOT_A_CHATBOT = {
    eyebrow: 'What makes Fundile different',
    title: 'Fundile is not an AI chatbot.',
    intro:
        'Chatbots like ChatGPT answer the question for you. Fundile turns that around: it asks you the question, then helps you close the gaps in your own understanding.',
    rows: [
        {
            aspect: 'Who answers',
            chatbot: 'You ask, the AI gives you the answer.',
            fundile: 'Fundile gives you the question; you answer, and it helps you fill the gaps in your understanding.',
        },
        {
            aspect: 'Curriculum guard-rails',
            chatbot: 'No syllabus guard-rails — it answers about anything.',
            fundile: 'Built on your grade-level syllabus, tests and exams, so it stays on topic.',
        },
        {
            aspect: 'Reliability',
            chatbot: 'Can hallucinate and drift off course.',
            fundile: 'Operates deterministically to always stay in context.',
        },
        {
            aspect: 'Curriculum objectives',
            chatbot: 'Answers are not calibrated to curriculum objectives.',
            fundile: 'Guides you against the South African curriculum objectives.',
        },
    ],
};

// "What the app does" claims, each with its own demo-media slot so a specific
// clip can be dropped under every claim. `demo.type` is 'youtube' for an embed
// or 'placeholder' for a labelled "coming soon" slot.
export const FEATURE_CLAIMS = {
    eyebrow: 'See it in action',
    title: 'Watch what Fundile actually does.',
    intro:
        'Every claim below comes with a short demo. We are recording one per feature — drop in to watch how each part works.',
    claims: [
        {
            key: 'topic-flow',
            title: 'Guided Scaffold → Practice → Assessment',
            body: 'Pick a topic and move through guided scaffolding, unlimited practice, and an exam-style assessment that unlocks as you master each stage.',
            demo: { type: 'youtube', src: 'https://www.youtube.com/embed/c4SMEpSFO0w?rel=0', label: 'Full product demo' },
        },
        {
            key: 'step-marking',
            title: 'Step-by-step marking that finds your mistake',
            body: 'Show your working line by line. Fundile pinpoints the exact line your method broke down — and still credits everything that was correct.',
            demo: { type: 'placeholder', label: 'Demo coming soon' },
        },
        {
            key: 'unlimited-practice',
            title: 'Unlimited, fresh exam-standard questions',
            body: 'Deterministic generators produce endless new variants of any question, so you can practise a tricky type until it is automatic.',
            demo: { type: 'placeholder', label: 'Demo coming soon' },
        },
        {
            key: 'adaptive',
            title: 'Adaptive progression on your weak subskills',
            body: 'When you struggle, Fundile drops you to the foundation you are missing and rebuilds it before moving you on.',
            demo: { type: 'placeholder', label: 'Demo coming soon' },
        },
    ],
};
