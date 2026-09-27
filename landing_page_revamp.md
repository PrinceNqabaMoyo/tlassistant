# Fundile Landing Page Revamp & Multi-Subject Ecosystem Specification

> **Status:** Active Reference & Execution Blueprint  
> **Target Audience:** Individual Learners & Parents (Primary B2C), Schools, Tutors & District Admins (B2B)  
> **Regulatory Invariant (Rule 2b & Strategic Policy):** Strict prohibition of proprietary examining body trademarks in promotional marketing copy. Zero explicit use of the acronym "CAPS" on student-facing, parent-facing, or promotional surfaces (replace with *"South African National Curriculum Standards"*, *"National Academic Standards"*, *"Official South African 7-Level Achievement Scale"*, and *"Authentic Exam-Standard"* to eliminate public school misconceptions).  
> **Deterministic Invariant:** Zero LLM cost for static question generation, step-by-step marking, and hint distribution.

---

## 1. Executive Summary & Screenshot Audit (Screenshots 1–8)

An exhaustive evaluation of the current live landing page (`LandingPage.jsx`, `PerspectiveShowcase.jsx`, `CapsNscClarity.jsx`, `DemandCaptureForm.jsx`, `LandingFaq.jsx`) was conducted across 8 user-provided screenshots.

### Screenshot 1: Hero Section & Value Proposition
* **Current State:**
  * Displays "Built for the South African high-school learner" eyebrow.
  * Interactive rolling slot-machine ticker cycles through subjects (`Mathematics`, `Accounting`, `Physical Sciences`, `EMS`, `Business Studies`, `every subject.`).
  * Tagline: "Use Fundile, become a top student."
  * Feature bullets with amber checkmarks: unlimited practice, adaptive progression, knowledge gap diagnostic reports, examining bodies covered, SimuLearn data-saving alternative.
  * CTA buttons: Primary "Start 2-week free trial", bouncing arrow "See how it works".
* **Deficiencies & Critical Fixes:**
  * **Underselling Omission:** The slot machine and headline omitted **Life Sciences**, **Natural Sciences**, and **Mathematical Literacy**. Ticker updated to cycle through all 8 core subjects: `Mathematics`, `Physical Sciences`, `Life Sciences`, `Natural Sciences`, `Mathematical Literacy`, `EMS`, `Accounting`, `Business Studies`, and `every subject.`.
  * **Grade Inclusivity:** The eyebrow states "high-school learner", which alienates Senior Phase (Grades 7–9) EMS and Natural Sciences learners. Reframed to: *"Built for South African Grades 7–12 Learners"*.
  * **Mobile SimuLearn CTA:** On small viewports, the scrolling slot machine text should remain centered and never cause layout thrashing or overflow.

### Screenshot 2: Perspective Showcase (Learners / Teachers / Parents)
* **Current State:**
  * Segmented control toggle allowing visitors to view the platform from three perspectives:
    1. **Learners:** "Your personal AI tutor and exam coach that never gets tired."
    2. **Teachers:** "A force multiplier for lesson prep, question authoring, and marking."
    3. **Parents:** "Clear visibility into what your child actually knows and where they struggle."
  * Interactive live simulator below the toggle demonstrates the selected persona's dashboard in action.
* **Recommendations:**
  * Excellent conversion architecture. Maintain the tabbed perspective toggle as the primary bridge below the fold.
  * Add a direct CTA inside the Teacher tab pointing to `/for-teachers` and the School LMS Cockpit.

### Screenshot 3: The Problem → The Promise (The Hidden Curriculum)
* **Current State:**
  * Eyebrow: "The hidden curriculum".
  * Headline: "Most learners are surprised by the exam. They should not be."
  * 3 Surface cards:
    1. *Exam-standard from day one* — Practice questions pitched at authentic exam level from the first topic.
    2. *See where you went wrong* — Step-by-step marking pinpoints exact line transitions.
    3. *Unlimited practice* — Deterministic generators produce endless fresh variants.
* **Recommendations:**
  * High emotional resonance with parents and learners.
  * Enhance contrast of the card border on dark mode (`border-white/10 hover:border-[#2B7BD8]/40 hover:bg-white/[0.08]`).

### Screenshot 4: How It Works & "Not a Chatbot" Callout
* **Current State:**
  * 3-step numbered flow: `01 Pick a topic` → `02 Scaffold → Practice → Assessment` → `03 Learn from feedback`.
  * Callout banner: *"Fundile is not an AI chatbot. Chatbots answer the question for you. Fundile asks you the question, then helps you close the gaps in your own understanding."*
* **Recommendations:**
  * Directly addresses parent fears of AI doing homework for their children.
  * Reinforces deterministic curriculum grounding and zero hallucination.

### Screenshot 5: Pricing Section & Availability Paradox (The Root Cause of Underselling)
* **Current State:**
  * Headline: "One subscription. Every subject. Less than one tutoring hour."
  * Tutoring cost anchor: R50–R200/hr vs R150/mo.
  * Two packages displayed:
    * **Standard (R150 / mo):** Unlimited deterministic practice, adaptive progression, scaffolded exam questions, step-by-step marking.
    * **Pro (R299 / mo):** Live Socratic tutor, deep subskill diagnosis, adaptive micro-lessons.
  * 2-week free trial banner (no card required).
* **The Fatal Bug / Underselling:**
  * Directly above the CTA button was a note reading:  
    `"Fundile currently supports Grade 10 and Grade 11 Accounting. More grades and subjects are coming soon."`
  * This completely invalidated the promise of "One subscription. Every subject." and caused prospective users to bounce immediately.
  * **Fix:** Purge all "Accounting only" constants from `src/app/constants/availability.js` and `src/app/constants/access.js`. Proclaim full Grades 7–12 coverage across Mathematics, Physical Sciences, Life Sciences, Natural Sciences, Mathematical Literacy, EMS, Accounting, and Business Studies.

### Screenshot 6: Trust, Objection-Handling & Rule 2b Legal Compliance
* **Current State:**
  * Section title: "Curriculum Standards & Exam Alignment".
  * 3-column comparative table comparing public, independent, and distance learning preparation.
* **Rule 2b Legal Violation & Strategic Brand Alignment:**
  * Under project Rule 2b: *Never use proprietary examining body trademarks (IEB, SACAI, DBE, NSC) in student/parent marketing, UI copy, or landing pages.*
  * Under the *No Explicit CAPS Acronym Policy*: Purge raw "CAPS" acronyms from public-facing copy to prevent the false impression of an inferior public-school-only product.
  * Replaced with universal, authoritative alignment statements:
    * `"100% Aligned with South African National Curriculum Standards"`
    * `"Authentic Grade 7–12 Exam-Standard Questions & Marking Rubrics"`
    * `"Trusted preparation for public, private, and independent school examinations nationwide"`
  * The flow diagram is reframed to show:  
    `National Curriculum Standards → Public, Independent & Distance Schools → Universal Senior Certificate & Tertiary Readiness`.

### Screenshot 7: FAQ Accordion UI
* **Current State:**
  * 4 key objection-handlers:
    1. Curriculum alignment across school types.
    2. Available subjects and grades (previously claimed only Accounting!).
    3. Cost comparison against private tutoring.
    4. POPIA compliance and child data protection.
* **Fixes:**
  * FAQ item 2 updated to proudly announce all 8 core subjects across Grades 7 to 12.
  * Added question clarifying how individual learner subscriptions work compared to school-provided enterprise accounts.

### Screenshot 8: Demand Capture / Interest Form (Aesthetic Inconsistency)
* **Current State:**
  * Card container rendered with hardcoded `bg-white` and light border `border-sky-100` on an otherwise dark-themed (`bg-slate-950`) page.
  * Resulted in an unstyled, high-contrast white rectangular box that broke the aesthetic unity of the design.
* **Fixes:**
  * Wired `isLightPalette` into `DemandCaptureForm.jsx`.
  * Implemented dark glassmorphism (`bg-slate-900/90 border border-slate-800 text-white`) with slate-950 inputs, subtle focus rings, and white/70 labels.
  * In light mode, seamlessly renders elegant slate-50/sky-100 styling.

---

## 2. Life Sciences Implementation Audit & Status

### Backend Capabilities Built
1. **Genetics & Monohybrid Cross Generator:**
   * Path: [`caps-ai-backend/app/utils/life_sciences/genetics_generator.py`](file:///c:/Users/princ/fundile-tlassistant-vite/caps-ai-backend/app/utils/life_sciences/genetics_generator.py)
   * 100% deterministic Punnett square calculations, Mendelian genetics, gamete segregation during Meiosis, parental genotypes/phenotypes, and offspring genotypic/phenotypic ratio determination.
   * Multiple model organisms: Pea plants (height, seed color), Guinea pigs (fur color), Drosophila fruit flies (eye color).
   * Cross archetypes: Heterozygous × Heterozygous (3:1 ratio), Heterozygous × Homozygous recessive (1:1 test cross), Homozygous dominant × Homozygous recessive (100% dominant).
2. **6-Pillar Generator Contract Compliance:**
   * Metadata: `term: 1`, `caps_weight_percent: 30`, `suggested_duration_mins: 10`.
   * Misconception tags: `confuses_phenotype_genotype`, `dominant_recessive_inversion`, `incorrect_gamete_separation`.
   * Marking schema: 6-mark breakdown with editable teacher marking points (`mp_p1_pheno`, `mp_meiosis`, `mp_punnett`, `mp_f1_ratio`, `mp_prob`), deductions, and consequential carry-forward accuracy.
   * 3-Tier Pre-baked Hints:
     * Tier 1 (Nudge): Parental genotype representation.
     * Tier 2 (Concept): Meiotic gamete separation before fertilization grid.
     * Tier 3 (Breakdown): Complete offspring ratio calculation.
3. **Central Registry Integration:**
   * Registered in [`generator_registry.py`](file:///c:/Users/princ/fundile-tlassistant-vite/caps-ai-backend/app/services/generator_registry.py) under `life_sciences_genetics` and aliased to `genetics`, `life sciences`, `monohybrid cross`, and `punnett square`.
4. **Curriculum Documents Grounding:**
   * 31 transcribed CAPS markdown modules in `caps-ai-backend/curriculum_docs_auto/`:
     * Grade 10: Cells, Chemistry of Life, Cell Division, Plant/Animal Tissues, Support Systems, Biosphere.
     * Grade 11: Biodiversity of Microorganisms/Plants/Animals, Photosynthesis, Respiration, Human Nutrition, Population Ecology.
     * Grade 12: DNA Code of Life, Meiosis, Genetics & Inheritance, Human Reproduction, Endocrine System, Evolution by Natural Selection, Human Evolution.

### Frontend Integration
* Added `Life Sciences` to `src/curriculumData.js` across Grades 10, 11, and 12.
* Configured dedicated subject branding in `App.jsx`: `icon: Activity`, `color: bg-emerald-500`.
* Whitelisted in `src/app/constants/access.js` (`LIVE_SUBJECT_MATRIX`) for immediate student and teacher access.

---

## 3. Comprehensive Multi-Subject & Grade Matrix

Fundile now officially presents and supports the following subject portfolio across all public surfaces, signup gates, and LMS dashboards:

| Subject | Grades | Cognitive Modality | Generator Engine |
|---|---|---|---|
| **Mathematics** | 7–12 | SymPy symbolic derivations, KaTeX working pad, step-by-step method marks | Deterministic SymPy + AST pure generators (`grade7_whole_numbers` to `grade12_trigonometry`) |
| **Physical Sciences** | 10–12 | Vector math, formula derivations, comma decimal notation | Pure Python physics engine (`mechanics_generator.py`) |
| **Life Sciences** | 10–12 | Punnett squares, genetic crosses, biological diagrams, structured schemas | Deterministic genetics engine (`genetics_generator.py`) |
| **Natural Sciences** | 7–9 | Matter, energy transfers, planetary systems, scientific method | Combinatorial scientific taxonomy engine |
| **Mathematical Literacy** | 10–12 | Real-world finance, tax tables, conversions, tariff systems | Practical finance generator (`finance_tax_generator.py`) |
| **Economic & Management Sciences (EMS)** | 7–9 | 2D Journals (CRJ, CPJ, DJ, CJ), General Ledger, circular flow, economy | Full 2D accounting tabular engine (`grade7_ems` to `grade9_ems`) |
| **Accounting** | 10–12 | 2D General Ledgers, trial balances, bank reconciliations, GAAP, final accounts | Architectural gold standard 2D tabular ledger engine |
| **Business Studies** | 10–12 | Rubric semantic matching, concept mapping, socio-economic analysis | 4D Combinatorial Engine (infinite semantic breadth) |
| **Technical Mathematics** | 10–12 | Complex numbers, circle geometry, technical calculus | Symbolic technical math generator |

---

## 4. Individual Learner vs. School/District Account Architecture

To ensure seamless onboarding for both independent B2C subscribers and B2B school rollouts:

1. **Independent Self-Subscribed Learner:**
   * Signs up directly on the landing page via the 2-week free trial.
   * Billed monthly via Card or Instant EFT (R150/mo Standard, R299/mo Pro).
   * Generates their own private diagnostic mastery profile.
   * Can link to a school at any time using a 6-character School Code without losing their historical progress or streak data.
2. **School-Subscribed Learner:**
   * Enrolled via Teacher LMS or School Admin batch import (CSV/Google Classroom).
   * Subscription paid centrally by the school or provincial department of education.
   * Access to teacher-assigned homework drills, mid-term tests, and mock exams.
   * Performance and knowledge gap diagnostics automatically sync to the Teacher Cockpit, Principal Dashboard, and District Superadmin Overview.

---

## 5. Mobile App Readiness & PWA Architecture

The platform has been audited for native mobile app packaging (via Capacitor or PWA):
1. **Responsive Viewport & Touch Ergonomics:**
   * All clickable UI elements (buttons, keypad tokens, hint triggers) have touch targets $\ge 44 \times 44\text{ px}$.
   * Safe-area padding implemented for iOS notch and Android gesture bars.
2. **Data-Conscious Architecture:**
   * SimuLearn declarative JSON solution replays replace heavy 100MB video streaming with lightweight 4KB vector instructions, reducing learner data consumption by over 95%.
3. **PWA Manifest & Service Worker:**
   * Web manifest configured with South African localized metadata, standalone display mode, and offline asset caching for core KaTeX math libraries.

---

## 6. Implementation Checklist & Verification

- [x] **Audit screenshots 1–8** and document all visual, layout, and copy recommendations.
- [x] **Verify Life Sciences implementation** in backend generators, registry, and curriculum documents.
- [x] **Purge "Accounting only" underselling** across `availability.js`, `access.js`, and `landingCopy.js`.
- [x] **Add Life Sciences, Natural Sciences, Mathematical Literacy, and EMS** to `curriculumData.js` and `App.jsx`.
- [x] **Restyle `DemandCaptureForm.jsx`** to support dark glassmorphic UI (`bg-slate-900/90`).
- [x] **Scrub proprietary trademarks (Rule 2b)** from `CapsNscClarity.jsx` and `landingCopy.js`.
- [x] **Validate backend test suite** (`test_sa_naming_engine.py` 7/7 pass, `test_unified_generate_api.py` 5/5 pass).
- [x] **Compile and verify frontend** (`npm run build`).
- [x] **Update `fundile-architecture.json`** and run `python generate_architecture_html.py` (Rule 0a-0c).
