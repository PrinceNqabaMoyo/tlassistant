# Fundile: Curriculum Provision & Adaptive Learning Design Master Plan
**Document Version:** 2.1.0  
**Status:** Approved Architectural Specification & Pedagogical Master Document  
**Target Curriculum:** South African National Curriculum Statement (CAPS) — Grades 7–12  
**Subjects Covered:** Mathematics, Mathematical Literacy, Technical Mathematics, Economic & Management Sciences (EMS), Accounting, Business Studies, Natural Sciences, Physical Sciences (Physics & Chemistry), Life Sciences (Biology)  
**Examining Bodies Covered:** Authentic standard for public, private, and independent school examinations nationwide  

---

## Executive Summary: The Architectural & Curricular Vision

Traditional educational software and generative AI chatbots fail high school learners due to two opposing design flaws:
1. **The Static LMS Flaw (The Rigid Conveyor Belt):** Legacy systems force learners through a fixed, linear progression (`Scaffold → Practice → Assessment`). Every learner is fed the same monolithic questions regardless of prior schema, treating subskills equally and offering zero targeted diagnosis or deconstruction.
2. **The Generic AI Chatbot Flaw (The Passive Hallucinator):** Chatbots wait passively for the student to prompt them. However, a struggling student does not know what they do not know. When prompted, LLMs regularly miss South African curriculum boundaries, hallucinate incorrect calculation steps, and provide answers directly—inducing the *illusion of competence* while destroying cognitive retention.

**Fundile's Core Operating Thesis:**
> *"AI chatbots wait for your question. But a learner doesn't know what they don't know. Fundile already knows what the exam demands, has the question waiting first, deterministically diagnoses procedural gaps, remediates weaknesses through horizontal topic slicing and adaptive regression, and certifies true exam readiness through multi-tier post-readiness practice."*

---

## 1. The End-to-End Learner Assessment & Readiness Pipeline

Fundile structures the complete student journey as a continuous, 4-stage pedagogical loop:

```
                      THE COMPLETE FUNDILE LEARNER LIFECYCLE
                      
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Stage 1: Diagnostic Entry Battery ("The Question is Waiting")          │
   │ • 3-Question Micro-Benchmark (β = 0.3, 0.6, 0.85) on first topic entry.│
   │ • Homework Escape Hatch with implicit background diagnostic probing.   │
   └───────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Stage 2: Adaptive Progression & Deterministic Remediation              │
   │ • Real-time line-by-line / cell-by-cell procedure tracking.            │
   │ • Standardized snake_case misconception tagging.                       │
   │ • Targeted isomorphic practice variants on struggled parameters.       │
   │ • Adaptive Regression to elementary sub-drills on repeat failure.      │
   └───────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Stage 3: Real-Time Readiness Analysis & Memory-Decayed BKT             │
   │ • Bayesian Knowledge Tracing with Ebbinghaus memory decay (P(L, Δt)).  │
   │ • Visual Topic Mastery Dial & Readiness Index (0% to 100%).            │
   │ • "Refresh Recommended" alert when inactive topic decay drops < 70%.   │
   │ • Unlock gate for post-readiness evaluative testing.                   │
   └───────────────────────────────────┬────────────────────────────────────┘
                                       │
                                       ▼
   ┌────────────────────────────────────────────────────────────────────────┐
   │ Stage 4: Post-Readiness Evaluative & Exam Practice Suite               │
   │                                                                        │
   │ 4A. Topic-Based Tests:                                                 │
   │     • 20–30 min formative assessments certifying subskill integration. │
   │                                                                        │
   │ 4B. Term-Based Exams (Control Tests & Mid-Years):                      │
   │     • Bounded by school calendar (term <= selected_term).              │
   │     • 50–100 marks covering full term curriculum weighting.            │
   │                                                                        │
   │ 4C. End-of-Year Exams (Final Mock Examinations):                       │
   │     • Authentic Paper 1 & Paper 2 terminal exam simulations.           │
   │     • 100–150 marks, 2–3 hours, official formula sheets & rubrics.     │
   │                                                                        │
   │ 4D. Post-Exam Triage & 3-Step Remedial Sequence:                       │
   │     • Cognitive Conflict Probe ──► SimuLearn Replay ──► Isomorphic Pair│
   └────────────────────────────────────────────────────────────────────────┘
```

---

### 1.1 Stage 1: Diagnostic Entry Battery
* **Zero Decision Fatigue:** Learners are never dropped onto an empty screen with a blank "Generate" button.
* When entering a topic for the first time, a question is **already primed and waiting**:
  * **Item 1 (Low Difficulty - $\beta = 0.30$, High Discrimination $\alpha = 1.2$):** Single-step definition and baseline arithmetic.
  * **Item 2 (Core Exam Standard - $\beta = 0.60$, High Discrimination $\alpha = 1.6$):** Standard multi-step transaction or derivation.
  * **Item 3 (High Discriminant - $\beta = 0.85$, High Discrimination $\alpha = 1.8$):** Reverse parameter, non-routine context, or multi-ledger adjustment.
* **Homework Assist Escape Hatch:** Learners with immediate homework needs tap `[ I have a specific homework question tonight ──► ]`. Question 1 of their homework session acts as an implicit diagnostic probe, initializing their Bayesian Knowledge Tracing prior ($P_{init}$) invisibly without stalling urgent school assignments.

---

### 1.2 Stage 2: Adaptive Progression & Procedure Tracking
* **Zero-LLM Calculation:** Every math line is verified symbolically by SymPy; every accounting entry is verified by coordinate cell evaluation; every science formula is verified by dimension and value checks.
* **Consequential Accuracy:** If Line 1 has an arithmetic slip but Lines 2–4 are mathematically consistent with that intermediate error, the student receives full method marks and a carry-over note.
* **Standardized Misconception Taxonomy:** Errors are tagged with clean snake_case identifiers (`net_vs_gross_confusion`, `sign_error_distribution`, `omitted_balance_b_d`, etc.).
* **Adaptive Regression (Deconstruction):** Failing a compound archetype twice automatically deconstructs the problem into atomic constituent sub-drills (`mode="elementary_<subskill>"`), rebuilding prerequisite schemas before re-attempting compound questions.

---

### 1.3 Stage 3: Real-Time Readiness Analysis & Memory-Decayed BKT
As the student works, the student model (`student_model.py`) updates the probability of mastery $P(L_k)$ for each subskill parameter $k$.

#### 1.3.1 Ebbinghaus Memory Decay Function
To prevent false-positive readiness where a student mastered a topic months prior but has since suffered natural cognitive decay, Fundile implements a continuous time-decay penalty:

$$P(L_{k, t}) = P(L_{k, t-1}) \cdot e^{-\lambda_k \cdot \Delta t}$$

* **$\Delta t$:** Calendar days elapsed since the learner's last verified engagement with subskill $k$.
* **$\lambda_k$:** Topic-specific memory half-life decay parameter (e.g. $\lambda_{\text{mechanics}} = 0.015\,\text{day}^{-1}$, $\lambda_{\text{definitions}} = 0.025\,\text{day}^{-1}$).
* **Dynamic Dial States:**
  * **Novice (0–39%):** Red / Uncalibrated.
  * **Developing (40–59%):** Amber / Scaffolding active.
  * **Proficient (60–79%):** Yellow / Scaffolding fading.
  * **Exam Ready (80–100%):** Green / Evaluative suite unlocked.
  * **Refresh Recommended ($< 70\%$ post-decay):** Amber Pulse / Unlocks a 2-question micro-refresher sprint to restore peak calibration.

---

### 1.4 Stage 4: Post-Readiness Evaluative & Exam Practice Suite

#### 4A. Topic-Based Tests (Formative Topic Certification)
* **Duration:** 20 to 30 minutes.
* **Marks:** 25 to 35 marks.
* **Objective:** Certify that the student can integrate all subskills of a single topic under unassisted, timed conditions. Zero hints allowed.
* **Pass Threshold:** 75% unlocks the "Topic Certified" badge on the student's mastery dashboard.

#### 4B. Term-Based Exams (Calendar-Bounded Control Tests)
* **Duration:** 60 to 90 minutes.
* **Marks:** 50 to 100 marks.
* **Calendar Guardrail:** Strictly governed by `term <= selected_term`. A Term 2 student is never served Term 3 or 4 content.
* **Structure:** Aggregates all topics scheduled in the CAPS Annual Teaching Plan (ATP) up to that term.

#### 4C. End-of-Year Exams (Final Mock Paper Simulations)
* **Structure:** Replicates the exact national examination format:
  * **Mathematics:** Paper 1 (Algebra, Equations, Functions, Finance, Calculus, Probability - 100/150 marks) and Paper 2 (Euclidean Geometry, Analytical Geometry, Trigonometry, Statistics - 100/150 marks).
  * **Mathematical Literacy:** Paper 1 (Basic skills: Finance, Measurement, Data - 150 marks) and Paper 2 (Contextual applications: Maps & Plans, Integrated Measurement, Probability - 150 marks).
  * **Accounting:** Paper 1 (Financial Reporting: Balance Sheet, Income Statement, Cash Flow, Fixed Assets - 150 marks) and Paper 2 (Cost Accounting, Budgets, Bank/Creditors Reconciliations, Internal Controls & Ethics - 150 marks).
  * **Physical Sciences:** Paper 1 (Physics - Mechanics, Waves, Electricity, Electrodynamics - 150 marks) and Paper 2 (Chemistry - Chemical Change, Stoichiometry, Equilibrium, Acids/Bases, Organic - 150 marks).
  * **Life Sciences:** Paper 1 (Reproduction, Endocrine, Homeostasis, Response to Environment, Ecology - 150 marks) and Paper 2 (DNA, Meiosis, Genetics, Evolution - 150 marks).
* **Timing & Experience:** Authentic 2-hour or 3-hour countdown timers, downloadable formula sheets, standard comma decimal notation (`{,}`), and official layout answer books.

#### 4D. Post-Exam Triage Report & 3-Step Remedial Sequence
Rather than simply returning a percentage (e.g. "62%"), the engine produces an actionable diagnostic autopsy:
* *"You lost 16 marks across Questions 2 and 4 purely due to net_vs_gross_confusion."*
* One-tap remedial button: `[ Launch 5-Minute Targeted Fix Drill ──► ]` triggers an explicit **3-step cognitive repair sequence**:
  1. **Step 1: Cognitive Conflict Probe (1 min):** A specially calibrated question designed to confront the learner with a logical contradiction resulting from their misconception (e.g. proving that taking 15% off an inclusive price yields less VAT than was added to the exclusive price).
  2. **Step 2: SimuLearn Micro-Replay (1.5 mins):** A 90-second data-light animated step trace of the canonical decision rule (0.1% video data cost).
  3. **Step 3: Isomorphic Verification Pair (2.5 mins):** Two unassisted, freshly-seeded variations verifying that the misconception has been eliminated.

---

## 2. Curriculum Documents as Authoritative Calibration & Questioning Levels

All question generators, marking schemas, and exam blueprints are calibrated against the project's authoritative curriculum source repositories:

```
                             CURRICULUM SOURCE DIRECTORY TREE
                             
   caps-ai-backend/
   ├── curriculum_docs_auto/                 ◄── [PRIMARY CALIBRATION SOURCE]
   │   ├── Accounting_Gr10 ... Gr12              • Official Annual Teaching Plans (ATPs)
   │   ├── BusinessStudies_Gr10 ... Gr12         • Exact term weightings and mark allocations
   │   ├── EMS_Gr7 ... Gr9                       • Vision annotations of geometric & anatomical diagrams
   │   ├── LifeSciences_Gr10 ... Gr12            • Biological drawing rubrics and specimen keys
   │   ├── MathematicalLiteracy_Gr10 ... Gr12    • Stepped municipal tariffs and tax tables
   │   ├── Mathematics_Gr7 ... Gr12              • Authenticated cognitive level distributions
   │   ├── NaturalSciences_Gr7 ... Gr9           • Scientific inquiry & investigation pacing
   │   ├── PhysicalSciences_Gr10 ... Gr12        • Standard formula tables & constants
   │   └── TechnicalMathematics_Gr10 ... Gr12    • TVET/Technical school applied mechanics
   │
   └── curriculum_docs/                      ◄── [EXEMPLAR & DEPTH REFERENCE]
       ├── Gr10_Accounting_Exam1..51.pdf         • Authentic past national exam papers
       ├── Gr11_Accounting_Exam1..76.pdf         • Teacher memoranda and marking rubrics
       ├── Gr10_Mathematics_Exam_1..38.pdf       • Complete textbook chapter repositories
       ├── Gr10_PhysicalSciences_Exam1..8.pdf    • Exemplar Level 3 & Level 4 problem archetypes
       └── Textbook_Mathematics_Gr7..12_*.pdf    • Prerequisite conceptual depth and notes
```

### The 4 CAPS Cognitive Demand Levels
Every generated test and exam strictly reflects official CAPS cognitive weightings:

| Cognitive Level | Description & Characteristics | CAPS Weighting | Generator Implementation |
| :--- | :--- | :---: | :--- |
| **Level 1: Knowledge / Recall** | Straightforward recall of formulas, definitions, algorithms, biological terms, and single-step arithmetic without complex context. | **~20%** | Single-parameter drills; recall of journal rules, math definitions, basic unit conversions, cell organelle identification. |
| **Level 2: Routine Procedures** | Standard multi-step procedures performed in familiar contexts. Immediate application of standard algorithms. | **~35%** | Standard trinomial factorisation, basic ledger entries, routine Ohm's law substitutions, basic monohybrid genetic crosses. |
| **Level 3: Complex Procedures** | Multi-step problem solving requiring connection of two or more concepts, algebraic manipulation, or geometric proofs. | **~30%** | Simultaneous equations, kinematics with acceleration changes, Bank Reconciliation with timing + book errors, dihybrid crosses with pedigree analysis. |
| **Level 4: Problem Solving** | Non-routine, unfamiliar contexts, reverse parameter calculations, qualitative evaluations, experimental critiques, and optimization. | **~15%** | Reverse function parameters from graphs, financial ratio policy critique, non-routine geometry proofs, experimental validity critiques in science. |

---

## 3. Topic Slices: Vertical Progression Trajectories (Lower Grade to Upper Grade)

To ensure seamless horizontal slicing and prerequisite deconstruction, every topic strand in Fundile is mapped along its developmental trajectory across the grades.

---

### Domain 1: Mathematics (Grades 7–12)

```
                            MATHEMATICS STRAND PROGRESSION MAP
                            
   Gr 7–9 (Senior Phase: General Mathematics)  ──►  Gr 10–12 (FET Phase: Core Mathematics)
   ──────────────────────────────────────────       ──────────────────────────────────────
   Slice M1: Numbers, Exponents & Surds             Surds, Exponential Equations, Logarithms
   Slice M2: Algebraic Expressions & Equations      Quadratics, Polynomials, Inequalities
   Slice M3: Numeric & Geometric Patterns           Quadratic Sequences, Series, Sigma Notation
   Slice M4: Functions & Relationships              Hyperbola, Parabola, Exponential, Inverses
   Slice M5: 2D Geometry & Constructions            Euclidean Circle Geometry & Proportionality
   Slice M6: Coordinate Graphs & Lines              Analytical Geometry, Lines & Circles
   Slice M7: Measurement & Pythagoras               Trigonometry: Ratios, CAST, Graphs, 3D Rules
   Slice M8: Financial Math (Simple Interest)       Compound Decay, Annuities, Sinking Funds
   Slice M9: Data Handling & Statistics             Ogive Curves, Variance, Linear Regression
   Slice M10: Probability & Events                  Venn Diagrams, Tree Diagrams, Counting Principle
   Slice M11: [Not Available in Gr 7–11]            Differential Calculus (Grade 12 Exclusive)
```

#### Slice M1: Number Systems, Exponents & Surds
* **Grade 7:** Whole numbers, prime factors, fractions, basic integer addition/subtraction.
* **Grade 8:** Exponential laws for natural exponents ($a^m \cdot a^n = a^{m+n}$), negative integer arithmetic.
* **Grade 9:** Rational vs irrational numbers, scientific notation, fractional calculations.
* **Grade 10:** Number systems ($\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{Q}'$, non-real), surd simplification, rationalising denominators.
* **Grade 11:** Fractional exponents ($a^{m/n} = \sqrt[n]{a^m}$), exponential equations with factorisation ($2^{x+1} - 2^x = 8$), surd equations with extraneous root verification.
* **Grade 12:** Logarithms (definitions, laws, change of base), solving complex exponential equations using logs.

#### Slice M2: Algebraic Expressions & Equations
* **Grade 7:** Formulating simple algebraic expressions from words, single-variable linear equations.
* **Grade 8:** Distributive law across brackets, multiplying binomials, solving $ax + b = c$.
* **Grade 9:** Factorisation: Common factor, Difference of Two Squares (DOTS), simple trinomials ($x^2 + bx + c$). Solving linear equations with fractions.
* **Grade 10:** Trinomial factorisation ($ax^2 + bx + c$ where $a \neq 1$), grouping, sum/difference of cubes. Quadratic equations ($ax^2 + bx + c = 0$), simultaneous linear equations (2 variables), linear inequalities.
* **Grade 11:** Quadratic formula ($x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$), completing the square, nature of roots (discriminant $\Delta = b^2 - 4ac$), quadratic inequalities with number lines, simultaneous equations (one linear, one quadratic).
* **Grade 12:** Remainder and Factor Theorems, factorising cubic polynomials, solving cubic equations ($ax^3 + bx^2 + cx + d = 0$).

#### Slice M3: Patterns, Sequences & Series
* **Grade 7:** Numeric and geometric patterns with constant difference.
* **Grade 8:** Finding the $n^{\text{th}}$ term of linear patterns ($T_n = dn + c$).
* **Grade 9:** Non-linear patterns, geometric sequences qualitative intro.
* **Grade 10:** Linear number patterns ($T_n = an + b$).
* **Grade 11:** Quadratic sequences (constant second difference $2a$, $3a + b$, $a + b + c$).
* **Grade 12:** Arithmetic sequences & series ($S_n = \frac{n}{2}[2a + (n-1)d]$), Geometric sequences & series ($S_n = \frac{a(r^n - 1)}{r - 1}$), Sum to infinity ($S_\infty = \frac{a}{1 - r}$ for $|r| < 1$), Sigma notation ($\sum$).

#### Slice M4: Functions & Graphs
* **Grade 7:** Input/output flow diagrams, tables of ordered pairs.
* **Grade 8:** Plotting points on the Cartesian plane, linear graphs $y = mx + c$.
* **Grade 9:** Gradient concept ($m = \frac{\Delta y}{\Delta x}$), $x$- and $y$-intercepts, sketching straight lines.
* **Grade 10:** Linear function ($y = mx + c$), Parabola ($y = ax^2 + q$), Hyperbola ($y = \frac{a}{x} + q$), Exponential function ($y = ab^x + q$). Domain and range.
* **Grade 11:** Horizontal and vertical shifts: Parabola ($y = a(x - p)^2 + q$), Hyperbola ($y = \frac{a}{x - p} + q$), Exponential ($y = ab^{x - p} + q$). Determining equations from given points and graphs.
* **Grade 12:** Inverse functions ($f^{-1}$): line inverse, parabola inverse and domain restriction ($x \geq 0$ for one-to-one function), exponential and logarithmic inverses ($y = b^x \iff y = \log_b x$). Cubic function graphs and calculus tangents.

#### Slice M5: Euclidean Geometry
* **Grade 7:** Angles on a straight line, vertically opposite angles, adjacent angles.
* **Grade 8:** Parallel lines (alternate, corresponding, co-interior angles), triangle interior angle sum, exterior angle theorem, isosceles and equilateral triangles.
* **Grade 9:** Congruency of triangles (SSS, SAS, AAS, RHS), Similarity of triangles (AAA, sides in proportion), Theorem of Pythagoras.
* **Grade 10:** Properties of special quadrilaterals (Parallelogram, Rectangle, Rhombus, Square, Trapezium, Kite), The Midpoint Theorem.
* **Grade 11:** Circle Geometry Theorems 1 to 7: Line from centre perpendicular to chord, Angle subtended at centre is twice angle at circumference, Angles in same segment, Cyclic quad opposite angles supplementary, Tangent perpendicular to radius, Tangent-chord theorem.
* **Grade 12:** Proportionality Theorem (line parallel to one side of a triangle), Similar Triangles Ratio Theorem (equiangular triangles have sides in proportion).

#### Slice M6: Analytical Geometry
* **Grade 10:** Distance formula ($d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$), Midpoint formula, Gradient formula, Parallel lines ($m_1 = m_2$), Perpendicular lines ($m_1 \cdot m_2 = -1$), Colinearity.
* **Grade 11:** Equation of a straight line ($y - y_1 = m(x - x_1)$), Angle of inclination ($\tan \theta = m$, acute and obtuse angles).
* **Grade 12:** Equation of a circle with centre at origin ($x^2 + y^2 = r^2$), Equation of a circle with centre $(a, b)$: $(x - a)^2 + (y - b)^2 = r^2$, Equation of a tangent to a circle at a given point.

#### Slice M7: Trigonometry
* **Grade 10:** Definitions of trig ratios in right-angled triangles ($\sin \theta = \frac{O}{H}$, $\cos \theta = \frac{A}{H}$, $\tan \theta = \frac{O}{A}$), Reciprocal ratios ($\mathrm{cosec}, \sec, \cot$), Special angles ($0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ$), Cartesian plane definitions ($x, y, r$).
* **Grade 11:** CAST diagram, Reduction formulae ($180^\circ \pm \theta$, $360^\circ - \theta$, $-\theta$), Co-functions ($90^\circ \pm \theta$), Fundamental identities ($\tan \theta = \frac{\sin \theta}{\cos \theta}$, $\sin^2 \theta + \cos^2 \theta = 1$), General solutions of trig equations, Trigonometric graphs (amplitude, period, phase shift).
* **Grade 12:** Compound angle identities ($\cos(\alpha \pm \beta)$, $\sin(\alpha \pm \beta)$), Double angle identities ($\sin 2\theta = 2\sin\theta\cos\theta$, $\cos 2\theta = \cos^2\theta - \sin^2\theta$), 2D and 3D Trigonometric problem solving: Sine rule, Cosine rule, Area rule.

#### Slice M8: Financial Mathematics
* **Grade 7:** Budgets, income, expenditure, simple profit and loss.
* **Grade 8:** Simple interest calculation ($A = P(1 + in)$), calculating interest rates and time periods.
* **Grade 9:** Hire purchase agreements, loan transactions, simple currency conversions.
* **Grade 10:** Simple and compound interest ($A = P(1 + i)^n$), hire purchase agreements, inflation calculations.
* **Grade 11:** Depreciation on reducing balance ($A = P(1 - i)^n$) vs straight-line ($A = P(1 - in)$), Nominal vs effective interest rates ($1 + i_{\text{eff}} = (1 + \frac{i_{\text{nom}}}{m})^m$).
* **Grade 12:** Future Value Annuities ($F_v = \frac{x[(1 + i)^n - 1]}{i}$), Present Value Annuities ($P_v = \frac{x[1 - (1 + i)^{-n}]}{i}$), Sinking funds, Deferred annuities, Outstanding loan balance calculations.

#### Slice M9: Statistics & Data Handling
* **Grade 7:** Data collection, tallies, calculating mean, median, mode, and range for ungrouped data.
* **Grade 8:** Frequency tables, stem-and-leaf displays, bar charts, histograms.
* **Grade 9:** Grouped data frequency tables, measures of central tendency for grouped data, scatter plots.
* **Grade 10:** Five-number summary (Min, $Q_1$, Median, $Q_3$, Max), Box-and-whisker plots, Semi-interquartile range, Grouped frequency intervals.
* **Grade 11:** Histograms with frequency polygons, Cumulative frequency tables and ogive curves, Variance and standard deviation ($\sigma$).
* **Grade 12:** Bivariate data analysis, Scatter plots, Least-squares regression line ($y = A + Bx$), Correlation coefficient ($r$), Identification of outliers.

#### Slice M10: Probability
* **Grade 7:** Relative frequency vs theoretical probability, outcomes of single events.
* **Grade 8:** Two-way tables, probability of compound events.
* **Grade 9:** Tree diagrams, independent events, complementary events.
* **Grade 10:** Venn diagrams (two events), Mutually exclusive events ($P(A \text{ or } B) = P(A) + P(B)$), Complementary events ($P(\text{not } A) = 1 - P(A)$), Addition rule ($P(A \cup B) = P(A) + P(B) - P(A \cap B)$).
* **Grade 11:** Dependent vs independent events ($P(A \cap B) = P(A) \cdot P(B)$), Venn diagrams with 3 events, Contingency tables.
* **Grade 12:** Fundamental Counting Principle, Factorial notation ($n!$), Permutations and arrangements with repetition and without repetition, Complex probability calculations using counting principles.

#### Slice M11: Differential Calculus *(Grade 12 Exclusive)*
* **Grade 12:** Limits and continuity ($\lim_{x \to a} f(x)$), First principles derivative ($f'(x) = \lim_{h \to 0}\frac{f(x+h) - f(x)}{h}$), Differentiation rules ($\frac{d}{dx}[x^n] = nx^{n-1}$), Equations of tangents to curves, Curve sketching for cubic functions (stationary points, inflection points), Practical rate of change, Optimization problems (maxima/minima in geometry and finance).

---

### Domain 2: EMS (Grades 7–9) $\implies$ Accounting (Grades 10–12)

```
                            ACCOUNTING STRAND PROGRESSION MAP
                            
   Gr 7–9 (Senior Phase: EMS Accounting)       ──►  Gr 10–12 (FET Phase: Core Accounting)
   ─────────────────────────────────────            ─────────────────────────────────────
   Slice A1: The Accounting Equation (A = O + L)    Sole Trader ──► Partnerships ──► Companies
   Slice A2: Cash Journals (CRJ, CPJ, DJ, CJ)       General Journal, VAT, Capital Transactions
   Slice A3: Ledgers & Basic Trial Balance          Subsidiary Ledgers, Control Accounts, Year-End
   Slice A4: Basic Debtors/Creditors Lists          Bank Recon, Creditors Recon, Internal Audit
   Slice A5: Statement of Net Worth                 Income Statement, Balance Sheet, Cash Flow
   Slice A6: Basic Mark-Up Calculations             Financial Ratios & Managerial Decisions
   Slice A7: Cost Price & Selling Price             Production Cost Statement & Break-Even Point
   Slice A8: Personal & Business Budgets            Cash Budgets & Projected Income Statements
   Slice A9: [Not Available in Gr 7–9]              Perpetual vs Periodic, FIFO, Weighted Average
```

#### Slice A1: The Accounting Equation & Transaction Analysis
* **Grade 7:** Personal income and expenditure, assets and liabilities concept, simple net worth.
* **Grade 8:** Cash transactions: The fundamental equation $A = O + L$, DEADCLIC rule (Debit: Expenses, Assets, Drawings; Credit: Liabilities, Income, Capital).
* **Grade 9:** Credit transactions: Debtors ($A+$), Creditors ($L+$), discounts allowed ($O-$) and received ($O+$).
* **Grade 10:** Sole Trader: Comprehensive transactions with VAT, bad debts, trading inventory adjustments.
* **Grade 11:** Partnership: Capital and Current accounts impact on Owner's Equity ($A = O + L$).
* **Grade 12:** Companies: Share capital, retained income, repurchase of shares, dividends declared and paid.

#### Slice A2: Subsidiary Journals & Source Documents
* **Grade 8:** Cash Receipts Journal (CRJ) and Cash Payments Journal (CPJ), source documents (receipts, cheques, deposit slips).
* **Grade 9:** Debtors Journal (DJ), Debtors Allowances Journal (DAJ), Creditors Journal (CJ), Creditors Allowances Journal (CAJ), Petty Cash Journal (PCJ).
* **Grade 10:** Value Added Tax (VAT 15%) in journals, trade discounts vs cash discounts, dishonoured cheques, General Journal (GJ) entries.
* **Grade 11:** General Journal: Error corrections, bad debts, withdrawals of stock, year-end adjustment entries.
* **Grade 12:** General Journal: Share issue, buy-back of shares above issue price, provisional tax, dividend allocations.

#### Slice A3: General Ledger, Subsidiary Ledgers & Trial Balance
* **Grade 8:** Posting from CRJ and CPJ to General Ledger T-accounts, balancing accounts ($c/d$ and $b/d$), Trial Balance.
* **Grade 9:** Debtors Ledger and Creditors Ledger, Debtors Control and Creditors Control accounts in the General Ledger.
* **Grade 10:** Complete Sole Trader General Ledger balancing, Pre-Adjustment Trial Balance and Post-Closing Trial Balance.
* **Grade 11:** Partnership Ledgers: Partner Capital, Partner Current, Appropriation Account.
* **Grade 12:** Company Ledgers: Ordinary Share Capital, Retained Income, SARS: Income Tax, Shareholders for Dividends.

#### Slice A4: Reconciliations & Internal Auditing
* **Grade 9:** Reconciling Debtors and Creditors lists with Control accounts.
* **Grade 10:** Bank Reconciliation Statement: Timing differences (outstanding cheques, deposits) vs internal book corrections (charges, interest, debit orders).
* **Grade 11:** Creditors Reconciliation: Comparing business records with monthly statements received from creditors.
* **Grade 12:** Advanced internal audit: Internal controls over cash, inventory, and debtors; King IV corporate governance principles and code of ethics.

#### Slice A5: Financial Statements & Year-End Reporting
* **Grade 9:** Statement of Net Worth for a sole trader.
* **Grade 10:** Sole Trader Financial Statements: Statement of Comprehensive Income (Income Statement) and Statement of Financial Position (Balance Sheet) with basic notes.
* **Grade 11:** Partnership Financial Statements: Income Statement, Balance Sheet with Partner Capital and Current Account notes.
* **Grade 12:** Company Financial Statements: Statement of Comprehensive Income, Statement of Financial Position, Statement of Changes in Equity, Cash Flow Statement (Indirect method), Audit reports (Qualified, Unqualified, Disclaimer).

#### Slice A6: Financial Statement Analysis & Ratio Interpretation
* **Grade 10:** Gross profit margin, Net profit margin, Solvency ratio, Current ratio, Acid-test ratio.
* **Grade 11:** Operating profit on sales, Return on Partners' Equity, Debtors collection period, Creditors payment period, Debt-equity ratio.
* **Grade 12:** Earnings Per Share (EPS), Dividends Per Share (DPS), Dividend Payout Rate, Net Asset Value (NAV), Return on Capital Employed (ROCE), Financial gearing and risk analysis, Qualitative justification of corporate decisions.

#### Slice A7: Cost Accounting & Manufacturing
* **Grade 8/9:** Cost of sales calculation, mark-up percentage on cost price.
* **Grade 10:** Direct costs vs Indirect costs, Factory overheads concept.
* **Grade 11:** Production Cost Statement: Direct Material Cost, Direct Labour Cost, Factory Overheads, Work-in-Process.
* **Grade 12:** Complete Manufacturing Financial Statements, Unit cost calculations, Break-even point analysis ($BEP = \frac{\text{Fixed Costs}}{\text{Selling Price} - \text{Variable Cost per Unit}}$), Internal controls over factory materials and wastage.

#### Slice A8: Budgeting & Cash Flow Forecasting
* **Grade 7:** Personal household budget preparation.
* **Grade 8/9:** Simple enterprise cash flow projections.
* **Grade 10:** Debtors collection schedule, Creditors payment schedule.
* **Grade 11:** Projected Income Statement for a sole trader or partnership.
* **Grade 12:** Cash Budget (3-month rolling projection), Cash Flow Statement (operating, investing, financing activities), Variance analysis (budgeted vs actual).

#### Slice A9: Inventory Systems & Stock Valuation *(Grades 10–12 Exclusive)*
* **Grade 10:** Perpetual inventory system: recording cost of sales at point of sale.
* **Grade 11:** Periodic inventory system vs Perpetual inventory system: purchases account, carriage on purchases, closing stock calculation.
* **Grade 12:** Inventory valuation methods: First-In-First-Out (FIFO), Weighted Average Method, Specific Identification. Stockholding period and stock turnover rate.

---

### Domain 3: Natural Sciences (Grades 7–9) $\implies$ Physical Sciences (Grades 10–12)

```
                        PHYSICAL SCIENCES STRAND PROGRESSION MAP
                        
   Gr 7–9 (Senior Phase: Natural Sciences)     ──►  Gr 10–12 (FET Phase: Physical Sciences)
   ───────────────────────────────────────          ───────────────────────────────────────
   Slice P1: Forces, Energy & Motion                Vectors, Newton's Laws, Momentum, Work-Energy
   Slice P2: Sound, Light & Spectrum                Waves, Snell's Law, Doppler Effect
   Slice P3: Electric Circuits & Static Charge      Coulomb's Law, Electric Fields, Electrodynamics
   Slice P4: Matter, Atoms & Reactions              Bonding, Intermolecular Forces, Gas Laws
   Slice P5: Acids, Bases & Stoichiometry           The Mole, Reaction Rates, Chemical Equilibrium
   Slice P6: Electric Cells & Electrolytes          Redox Reactions, Galvanic & Electrolytic Cells
   Slice P7: [Not Available in Gr 7–11]             Organic Chemistry & IUPAC (Grade 12 Exclusive)
```

#### Slice P1: Mechanics & Kinematics (Physics)
* **Grade 7:** Potential and kinetic energy, energy transfer.
* **Grade 8:** Contact forces (friction, tension) and non-contact forces (gravitational, magnetic, electrostatic).
* **Grade 9:** Forces and Newton's Third Law qualitative, gravitational acceleration.
* **Grade 10:** Vectors and scalars, 1D motion: position, displacement, speed, velocity, acceleration. Equations of motion ($v_f = v_i + a\Delta t$, $\Delta x = v_i \Delta t + \frac{1}{2}a\Delta t^2$). Motion graphs.
* **Grade 11:** 2D Vectors, resolving into components ($F_x = F\cos\theta, F_y = F\sin\theta$), Free-body diagrams, Newton's 1st, 2nd ($F_{\text{net}} = ma$), and 3rd Laws, Newton's Law of Universal Gravitation ($F = G\frac{m_1 m_2}{r^2}$).
* **Grade 12:** Momentum ($p = mv$) and Impulse ($J = F_{\text{net}}\Delta t = \Delta p$), Conservation of Linear Momentum ($m_1 v_{i1} + m_2 v_{i2} = m_1 v_{f1} + m_2 v_{f2}$), Vertical Projectile Motion in 1D ($a = -9{,}8\,\text{m}\cdot\text{s}^{-2}$), Work, Energy, and Power ($W = F\Delta x \cos\theta$, Work-Energy Theorem $W_{\text{net}} = \Delta E_k$, $P = \frac{W}{\Delta t} = Fv$).

#### Slice P2: Waves, Sound & Light (Physics)
* **Grade 7:** Sound energy, pitch, loudness, ear structure basics.
* **Grade 8:** Reflection of light, refraction intro, visible spectrum.
* **Grade 9:** Transverse waves, frequency, wavelength, amplitude.
* **Grade 10:** Transverse pulses, superposition, transverse waves, longitudinal waves, sound waves (speed of sound, ultrasound), electromagnetic radiation ($c = f\lambda$, $E = hf$).
* **Grade 11:** Geometrical optics: refraction, Snell's law ($n_1 \sin\theta_1 = n_2 \sin\theta_2$), critical angle and total internal reflection, 2D wavefronts, Huygens' principle, diffraction.
* **Grade 12:** The Doppler Effect: sound moving source/observer ($f_L = \frac{v \pm v_L}{v \mp v_s} f_s$), red shifts and blue shifts in astronomy.

#### Slice P3: Electricity & Magnetism (Physics)
* **Grade 7:** Electricity supply grid, energy sources.
* **Grade 8:** Simple series and parallel circuits, current, voltage.
* **Grade 9:** Resistance ($R = V/I$), safety with electricity.
* **Grade 10:** Electrostatics: conservation of charge, quantization of charge ($q = n e$), potential difference, current, resistance in series and parallel.
* **Grade 11:** Coulomb's Law ($F = k\frac{q_1 q_2}{r^2}$), Electric field strength ($E = \frac{F}{q} = k\frac{Q}{r^2}$), Ohm's Law quantitative, series and parallel resistor networks, internal resistance ($\mathcal{E} = I(R + r)$), electrical power and energy.
* **Grade 12:** Electrodynamics: electromagnetic induction, Faraday's Law ($\mathcal{E} = -N\frac{\Delta \Phi}{\Delta t}$), AC and DC generators, electric motors, alternating current ($V_{\text{rms}}, I_{\text{rms}}, P_{\text{ave}}$), Photoelectric Effect ($E = W_0 + E_{k\text{max}}$).

#### Slice P4: Matter, Atomic Structure & Bonding (Chemistry)
* **Grade 7:** Particle model of matter, properties of materials, periodic table intro.
* **Grade 8:** Atoms, elements, compounds, subatomic particles (protons, neutrons, electrons).
* **Grade 9:** Writing chemical formulas, balanced chemical equations intro.
* **Grade 10:** Atomic models (Bohr, electron configuration via Aufbau, Hund, Pauli), Periodic table trends (electronegativity, first ionization energy, atomic radius), Chemical bonding (covalent, ionic, metallic).
* **Grade 11:** Intermolecular forces (London dispersion, dipole-dipole, hydrogen bonding), Molecular geometry and VSEPR theory, Ideal gases and gas laws ($PV = nRT$, Boyle, Charles, Gay-Lussac).
* **Grade 12:** Optical phenomena and properties of matter: emission and absorption spectra.

#### Slice P5: Chemical Change, Stoichiometry & Equilibrium (Chemistry)
* **Grade 8:** Chemical reactions: reactants and products.
* **Grade 9:** Reactions of metals with oxygen, reactions of acids with bases.
* **Grade 10:** Physical vs chemical change, Law of conservation of mass, The mole concept ($n = \frac{m}{M}$, $n = \frac{V}{V_m}$, $n = \frac{N}{N_A}$), percentage composition, empirical and molecular formulas, molar concentration ($c = \frac{n}{V}$).
* **Grade 11:** Stoichiometric calculations with limiting reactants, percentage yield, Energy changes in chemical reactions ($\Delta H$, exothermic vs endothermic, bond energy).
* **Grade 12:** Rates of reaction (collision theory, Maxwell-Boltzmann curves, catalysts), Chemical equilibrium (dynamic equilibrium, Le Chatelier's principle, Equilibrium constant $K_c$ expressions and ICE tables), Acids and bases (Brønsted-Lowry, conjugate pairs, $K_a, K_b, K_w$, pH calculations, standard titrations).

#### Slice P6: Electrochemistry (Chemistry)
* **Grade 9:** Simple electric cells.
* **Grade 10:** Reactions in aqueous solutions, electrolytes, precipitation reactions.
* **Grade 11:** Redox reactions, oxidation numbers, identifying oxidizing and reducing agents.
* **Grade 12:** Galvanic cells (half-reactions, cell notation, standard electrode potentials table, $E^\circ_{\text{cell}} = E^\circ_{\text{reduction}} - E^\circ_{\text{oxidation}}$), Electrolytic cells (electrolysis of molten NaCl, chlor-alkali process, extraction of aluminium, electroplating, electro-refining).

#### Slice P7: Organic Chemistry *(Grade 12 Exclusive)*
* **Grade 12:** Functional groups and homologous series (alkanes, alkenes, alkynes, haloalkanes, alcohols, aldehydes, ketones, carboxylic acids, esters). IUPAC naming conventions. Structural, chain, and positional isomers. Intermolecular forces and boiling point / vapor pressure trends. Organic reactions: Addition (hydrogenation, halogenation, hydrohalogenation, hydration), Substitution (hydrolysis, halogenation), Elimination (dehydrohalogenation, dehydration), Esterification. Plastics and polymers.

---

### Domain 4: EMS (Grades 7–9) $\implies$ Business Studies (Grades 10–12)

```
                        BUSINESS STUDIES STRAND PROGRESSION MAP
                        
   Gr 7–9 (Senior Phase: EMS Business & Economy) ──► Gr 10–12 (FET Phase: Business Studies)
   ─────────────────────────────────────────────     ───────────────────────────────────────
   Slice B1: Economic Systems & Sectors              Micro, Market & Macro Environments, PESTLE
   Slice B2: Entrepreneurship & Business Plans       Forms of Ownership, Investments, JSE
   Slice B3: Workers' Rights & Sustainable Living    Ethics, Professionalism, CSR, CSI, King IV
   Slice B4: Business Functions & Contracts          Eight Functions, Labour Legislation, TQM
```

#### Slice B1: Business Environments & Environmental Strategies
* **Grade 7:** Needs and wants, goods and services, businesses in the community.
* **Grade 8:** Economic cycle, factors of production, primary, secondary, and tertiary sectors.
* **Grade 9:** Economic systems (planned, market, mixed), circular flow model.
* **Grade 10:** The Micro Environment (mission, vision, management, resources), The Market Environment (consumers, suppliers, competitors, intermediaries), The Macro Environment (PESTLE).
* **Grade 11:** Environmental challenges (inflation, strikes, socio-economic issues), adapting to challenges, lobbying, networking.
* **Grade 12:** Advanced Macro analysis, Porter's Five Forces model, Industrial analysis, Developing and evaluating strategic management processes.

#### Slice B2: Business Ventures, Entrepreneurship & Forms of Ownership
* **Grade 7:** Entrepreneurial characteristics and skills.
* **Grade 8:** Identifying business opportunities, SWOT analysis.
* **Grade 9:** Components of a viable business plan.
* **Grade 10:** Forms of ownership: Sole Trader, Partnership, Close Corporation, Private Company (Pty Ltd), Public Company (Ltd), State-Owned Company (SOC). Criteria for success.
* **Grade 11:** Benefits and challenges of ownership forms, Acquiring an existing business, Franchising, Outsourcing, Leasing.
* **Grade 12:** Business investments: Securities, JSE equities, RSA Retail Savings Bonds, Mutual funds, Compound interest business calculations, Insurance and assurance (insurable vs non-insurable risks, average clause).

#### Slice B3: Business Roles, Ethics, Inclusivity & CSR
* **Grade 7:** Environmental sustainability in commerce.
* **Grade 8:** Social responsibility of local businesses.
* **Grade 9:** Productivity, trade unions and employer organizations.
* **Grade 10:** Creative thinking and problem-solving techniques (Delphi, force-field analysis, brainstorming), relationship management.
* **Grade 11:** Professionalism and business ethics, King Code principles, stress and crisis management, workplace diversity.
* **Grade 12:** Corporate Social Responsibility (CSR) and Corporate Social Investment (CSI), Human rights, inclusivity, and environmental workplace policies, Team performance assessment and conflict management strategies.

#### Slice B4: Business Operations, Quality Management & Labour Legislation
* **Grade 8:** Employment contracts and workplace expectations.
* **Grade 9:** Role and function of trade unions.
* **Grade 10:** The eight business functions (General Management, Administration, Financial, Purchasing, Production, Marketing, Public Relations, Human Resources), concept of quality.
* **Grade 11:** Marketing mix (4Ps: Product, Price, Place, Promotion), Production costs and factory safety, Human Resources function (recruitment, selection, induction).
* **Grade 12:** South African Labour Legislation: BCEA, LRA, EEA, BBBEE, COIDA, SDA, CPA; Total Quality Management (TQM) elements and their impact on reducing costs of quality.

---

### Domain 5: Natural Sciences (Grades 7–9) $\implies$ Life Sciences (Grades 10–12)

```
                          LIFE SCIENCES STRAND PROGRESSION MAP
                          
   Gr 7–9 (Senior Phase: NS Life & Living)     ──►  Gr 10–12 (FET Phase: Life Sciences)
   ───────────────────────────────────────          ───────────────────────────────────
   Slice L1: Cell Biology & Microscopy              Molecules of Life, Cell Cycle, Mitosis, Cancer
   Slice L2: Plant & Animal Structure               Tissues, Organs, Plant/Human Support Systems
   Slice L3: Human Physiology & Homeostasis         Nutrition, Gas Exchange, Excretion, Nervous
   Slice L4: Genetics & Molecular Inheritance       DNA, RNA, Protein Synthesis, Meiosis, Crosses
   Slice L5: Ecology, Evolution & Continuity        Population Dynamics, Natural Selection, Hominids
```

#### Slice L1: Molecular and Cellular Basis of Life
* **Grade 7:** Basic cell structure, microscopes, unicellular vs multicellular organisms.
* **Grade 8:** Cell organelles (nucleus, cytoplasm, cell membrane, cell wall, mitochondria, chloroplasts, vacuoles).
* **Grade 9:** Cell division intro, growth and repair.
* **Grade 10:** Chemistry of life: organic compounds (carbohydrates, lipids, proteins, nucleic acids, vitamins) and inorganic compounds (water, mineral ions: $Na, K, Ca, Fe, I, P$), deficiency diseases. Cell structure under transmission electron microscopy. Mitosis phases: Interphase, Prophase, Metaphase, Anaphase, Telophase. Cytokinesis. Cancer etiology (carcinogens, benign vs malignant tumors, treatments).
* **Grade 12:** DNA and RNA structure, discovery of DNA (Watson, Crick, Franklin), DNA replication mechanism, transcription and translation in protein synthesis.

#### Slice L2: Plant and Animal Tissues, Anatomy & Support Systems
* **Grade 7:** Plant organs (roots, stems, leaves, flowers) and animal organs.
* **Grade 8:** Tissue types introduction.
* **Grade 9:** Musculoskeletal system introduction.
* **Grade 10:** Plant tissues: Meristematic and permanent tissues (xylem, phloem, parenchyma, collenchyma, sclerenchyma, epidermis). Animal tissues: Epithelial, connective, muscle, and nerve tissues. Human skeleton: Axial skeleton (cranium, vertebral column, ribcage) and appendicular skeleton (girdles and limbs), long bone structure, joints (fibrous, cartilaginous, synovial), musculoskeletal disorders (rickets, osteoporosis, arthritis). Plant support: turgor pressure, secondary thickening.

#### Slice L3: Human Life Processes & Dynamic Homeostasis
* **Grade 7:** Human reproduction and puberty basics.
* **Grade 8:** Human digestive, respiratory, and circulatory systems.
* **Grade 9:** Excretion and nervous control intro.
* **Grade 11:** Animal nutrition: mechanical and chemical digestion, absorption, assimilation, egestion, liver functions, diabetes mellitus. Cellular respiration: glycolysis, Krebs cycle, oxidative phosphorylation, anaerobic respiration. Human gas exchange: alveoli, mechanism of ventilation, transport of gases ($O_2, CO_2$), respiratory diseases. Human excretion: structure of the urinary system, the nephron (ultrafiltration, tubular reabsorption, tubular excretion), dialysis.
* **Grade 12:** Human response to the environment: The nervous system (brain structures: cerebrum, cerebellum, medulla oblongata; spinal cord, reflex arc, peripheral nervous system), diseases of the nervous system (Alzheimer's, multiple sclerosis). The human eye (accommodation, pupillary mechanism, visual defects) and ear (hearing, balance, hearing defects). The human endocrine system: Endocrine glands (pituitary, thyroid, pancreas, adrenal, gonads), negative feedback loops (TSH and thyroxin, insulin and glucagon, ADH and osmoregulation, aldosterone and salt balance). Thermoregulation (sweating, vasodilation, vasoconstriction). Human reproduction: Male and female reproductive anatomy, pubertal hormones, spermatogenesis, oogenesis, menstrual cycle (FSH, LH, estrogen, progesterone), fertilisation, blastocyst implantation, placenta function, contraception, STIs.

#### Slice L4: Genetics, Inheritance & Molecular Evolution
* **Grade 9:** Heredity and variation concepts.
* **Grade 12:** Meiosis: First and second meiotic divisions, crossing over (chiasmata formation), random assortment of chromosomes, non-disjunction and Down syndrome (Trisomy 21). Genetics and inheritance: Mendel's laws (Law of Segregation, Law of Independent Assortment, Law of Dominance). Monohybrid crosses: complete dominance, incomplete dominance, co-dominance (ABO blood grouping). Sex determination (XX, XY). Sex-linked inheritance (haemophilia, red-green colour blindness). Dihybrid crosses. Pedigree diagrams and genetic genealogy. Genetic engineering, recombinant DNA technology, cloning, stem cell research, genetically modified organisms (GMOs): benefits and ethical controversies. Paternity testing via DNA profiling.

#### Slice L5: Diversity, Change, Ecology & Environmental Studies
* **Grade 7:** Biosphere, biomes of South Africa, biodiversity.
* **Grade 8:** Ecosystems, food chains and webs, trophic levels.
* **Grade 9:** Interactions and interdependence within the environment, pollution.
* **Grade 10:** Biosphere to biomes (Fynbos, Savanna, Grassland, Succulent Karoo, Nama Karoo, Forest, Thicket). Abiotic and biotic factors. History of life on Earth: Geological timescales, fossil formation, Cambrian explosion, mass extinctions (Cretaceous-Paleogene), fossil evidence in South Africa (Cradle of Humankind, Karoo fossils).
* **Grade 11:** Population ecology: Population size parameters (natality, mortality, immigration, emigration), exponential and logistic growth forms, carrying capacity, environmental resistance. Estimating population size: Mark-recapture method (Lincoln-Petersen index) and quadrat sampling. Predator-prey relationships, interspecific and intraspecific competition, competitive exclusion principle, resource partitioning. Social organization (herds, packs, dominant breeding pairs, division of labour). Human population curves.
* **Grade 12:** Evolution by Natural Selection: Origin of ideas on evolution (Erasmus Darwin, Lamarck's laws of use/disuse and inheritance of acquired traits, Charles Darwin and Wallace). Evidence for evolution: Fossil record, biogeography, homologous structures, genetics. Speciation: Allopatric vs sympatric speciation, geographic isolation mechanisms, reproductive isolating mechanisms. Evolution in present times (DDT resistance in mosquitoes, antibiotic resistance in bacteria). Human Evolution: Out of Africa hypothesis vs Multiregional hypothesis, anatomical comparisons between African apes and humans (bipedalism, foramen magnum position, brain volume, teeth, palate shape, brow ridges), Australopithecus species (Taung Child, Mrs Ples, Little Foot, *Australopithecus sediba*), *Homo* species (*Homo habilis*, *Homo erectus*, *Homo sapiens*).

---

### Domain 6: Senior Phase Mathematics (Grades 7–9) $\implies$ Mathematical Literacy (Grades 10–12)

```
                      MATHEMATICAL LITERACY STRAND PROGRESSION MAP
                      
   Gr 7–9 (Senior Phase: General Mathematics)  ──►  Gr 10–12 (FET Phase: Mathematical Literacy)
   ──────────────────────────────────────────       ───────────────────────────────────────────
   Slice ML1: Financial Contexts & Calculations     Budgets, Payslips, Tax Tables, Tariffs, Loans
   Slice ML2: Measurement & Packaging Conversions   Multi-tier Units, Perimeter, Area, Volume, Box Fit
   Slice ML3: Maps, Plans & Space Representation    Number/Bar Scales, Elevations, Floor Plans, Grids
   Slice ML4: Data Handling & Real-World Stats      Box-and-Whisker, Percentiles, Media Misrepresentation
   Slice ML5: Probability & Everyday Risk Analysis  Relative Frequency, Tree Diagrams, Insurance Risk
```

#### Slice ML1: Financial Contexts & Civic Calculations
* **Grade 7:** Personal income and expenditure, household budgeting, simple profit calculations.
* **Grade 8:** Simple interest, price comparisons, unit costs.
* **Grade 9:** Hire purchase, simple currency conversions, personal bank statements.
* **Grade 10:** Financial documents: Till slips, household bills (water, electricity), account statements. Household budgeting: fixed, variable, and occasional expenses; income vs expenditure. Cost comparisons and unit pricing. Basic banking accounts and fees.
* **Grade 11:** Stepped municipal tariff structures (sliding scale for water and electricity, domestic vs commercial). Taxation: Payslip analysis, Gross vs Net salary, UIF contributions, Medical aid credits, SARS Personal Income Tax brackets and tax rebates (primary, secondary, tertiary). Break-even analysis for small enterprises. Inflation: consumer price index (CPI) impact on real purchasing power. Simple vs compound interest loans.
* **Grade 12:** Complex loan amortization tables (residual payments, interest changes). Hire purchase agreements vs personal bank loans vs credit cards. Currency exchange rates with bank commissions. Real estate investment calculations: transfer duty, bond registration fees, municipal rates and taxes. Life assurance vs short-term insurance (insurable risk, excesses, the average clause calculation).

#### Slice ML2: Measurement, Conversion & Packaging
* **Grade 7:** Metric system conversions (mm, cm, m, km; ml, l; g, kg).
* **Grade 8:** Perimeter and area of rectangles, triangles, circles.
* **Grade 9:** Surface area and volume of rectangular prisms and cylinders.
* **Grade 10:** Reading analogue and digital instruments (clocks, thermometers, kitchen scales, vernier calipers). Multi-tier unit conversions (length, mass, volume, temperature in $^\circ\text{C}$ and $^\circ\text{F}$). Calculating perimeter and area of regular and composite 2D shapes. Estimating quantities of paint, tiles, or fencing needed.
* **Grade 11:** Volume and capacity of rectangular and cylindrical containers. Body Mass Index (BMI) calculations and growth chart interpretation. Cooking recipe scaling. Calibrating measuring devices.
* **Grade 12:** Packaging and tessellation: Calculating how many smaller rectangular or cylindrical items fit into a larger shipping carton or container (considering orientation constraints). Complex composite 3D volumes (e.g. swimming pool with sloping floor). Surface area optimization and wastage percentage calculations in manufacturing.

#### Slice ML3: Maps, Plans & Spatial Representations
* **Grade 7:** Grid references on simple maps, compass directions.
* **Grade 8:** Drawing views of 3D objects (top, front, side views).
* **Grade 9:** Scale drawings introduction.
* **Grade 10:** Number scales (e.g. $1:50\,000$) and bar scales. Finding locations using alphanumeric grid references and compass bearings. Calculating real-world distances along straight and curved routes using map scales. Layout plans for rooms and seating arrangements.
* **Grade 11:** Architectural floor plans: reading symbols (doors, windows, plumbing fixtures), dimensions, window schedules. Elevation plans (North, South, East, West exterior views). Determining wall areas excluding doors and windows for building material costing. Topographical maps: contour lines, steepness of terrain.
* **Grade 12:** Assembly instructions: interpreting 3D exploded view diagrams (furniture assembly, mechanical parts). Complex building site plans, parking bay layouts, and electrical connection plans. Global positioning and travel itineraries: time zones, travel schedules, distance-time graphs with speed limit enforcement.

#### Slice ML4: Data Handling & Statistical Interpretation
* **Grade 7:** Tallies, bar graphs, pictograms, mean, median, mode.
* **Grade 8:** Frequency tables, histograms, pie charts.
* **Grade 9:** Grouped data frequency tables, scatter plots.
* **Grade 10:** Formulating questions and collecting data. Organizing data: stem-and-leaf diagrams, frequency tables. Measures of central tendency (mean, median, mode) and spread (range). Displaying data: bar graphs, compound bar graphs, histograms, pie charts.
* **Grade 11:** Measures of spread: Quartiles ($Q_1, Q_2, Q_3$), interquartile range (IQR). Constructing and interpreting box-and-whisker plots. Interpreting percentiles in pediatric growth charts and national test scores. Identifying bias and misrepresentation in advertising graphs (broken axes, 3D distortions).
* **Grade 12:** Bivariate data analysis: Scatter plots, identifying positive, negative, and zero correlation trends. Constructing a line of best fit by eye. Two-way contingency tables and categorical analysis. Critical analysis of statistical claims in media and public policy reports.

#### Slice ML5: Everyday Probability & Risk Assessment
* **Grade 7:** Qualitative probability (impossible, unlikely, even chance, likely, certain).
* **Grade 8:** Relative frequency vs theoretical probability of single events.
* **Grade 9:** Compound events and tree diagrams.
* **Grade 10:** Expressing probability as fractions, percentages, and decimals. Probability scale ($0$ to $1$). Outcomes of simple random events (dice, coins, lottery balls).
* **Grade 11:** Tree diagrams for compound multi-stage real-world scenarios (weather forecasts, medical test reliability: false positives vs false negatives). Two-way tables for joint probability calculations.
* **Grade 12:** Evaluating risk in everyday contexts: Vehicle accident statistics, insurance risk premiums, gaming and casino odds, public health risk models. Making informed financial and personal decisions using calculated expected values.

---

### Domain 7: Senior Phase Mathematics (Grades 7–9) $\implies$ Technical Mathematics (Grades 10–12)

```
                      TECHNICAL MATHEMATICS STRAND PROGRESSION MAP
                      
   Gr 7–9 (Senior Phase: General Mathematics)  ──►  Gr 10–12 (FET Phase: Technical Mathematics)
   ──────────────────────────────────────────       ───────────────────────────────────────────
   Slice TM1: Number Systems & Complex Numbers      Binary, Hexadecimal, Argand Plane, De Moivre
   Slice TM2: Technical Functions & Trigonometry    Radian Measure, Angular Velocity, Gear Ratios
   Slice TM3: Technical Geometry & Circles          Circle Segments, Belts, Pulleys, Engineering Arcs
   Slice TM4: Differential & Integral Calculus      Rates of Change, Definite Integrals, Work Done
   Slice TM5: Applied Mechanics & Mensuration       Centre of Gravity, Fluid Pressure, Irregular Areas
```
* **Overview:** Technical Mathematics caters to technical high schools and TVET pipelines, replacing abstract algebraic proofs with applied engineering mechanics, radian circular measure, angular velocity calculations ($\omega = 2\pi f$), complex numbers in AC circuit analysis ($z = a + bi$), and definite integral calculations for work done and irregular cross-sectional engineering areas (Simpson's Rule).

---

## 4. Cognitive Pacing, Ergonomics & Learning Science Guardrails

### 4.1 Cognitive Fatigue & 45-Minute Deliberate Practice Circuit Breaker
High school learners experience steep error-rate spikes after 45–50 minutes of continuous, high-load problem solving. Continuing past this boundary generates false-negative misconception tags caused by cognitive exhaustion rather than conceptual deficiency.
* **Session Guardrail:** The system enforces an active deliberate practice limit of **45 minutes** per continuous session.
* **Ambient Circuit Breaker:** At minute 45, the workspace displays an ambient recovery prompt:
  > *"You've completed 45 minutes of intense deliberate practice! Problem-solving accuracy naturally declines past this point. Take a 10-minute rest, or switch to a data-light SimuLearn worked example to consolidate your schemas."*

### 4.2 Spaced Retrieval & Refresher Pin Mechanics
To counter the Ebbinghaus forgetting curve, subskills that have not been practiced for over 21 days undergo automated time decay ($P(L_k) < 0.70$), shifting from "Exam Ready" to **"Refresh Recommended"**.
* The student dashboard surfaces a 1-tap **"2-Question Refresher Sprint"**.
* Answering both refresher items correctly instantly restores the subskill to full 100% calibration without requiring the student to re-do the entire instructional queue.

### 4.3 Cognitive Modality Matching by Subject
Every subject is delivered in its authentic cognitive modality:
* **Accounting & EMS:** 2D ledger and journal tables with cell-level coordinate marking, given cells, required cells, and deduction penalties for filling empty cells.
* **Core Mathematics & Technical Mathematics:** KaTeX mathematical rendering with SymPy symbolic equivalence per step, procedure tracking, and South African comma decimal separator normalization (`{,}`).
* **Physical Sciences:** Stepwise physics derivation with vector sign convention checks, SI unit verification, and chemical equation balancing.
* **Life Sciences:** High-contrast biological diagram labeling, sequence reconstruction (mitosis/protein synthesis stages), and rubric-based cause-and-effect biological reasoning.
* **Mathematical Literacy:** Contextual documents (water/electricity utility bills, payslips, tariff tables, tax brackets, floor plans) with multi-step tabular calculations and realistic rounding rules.
* **Business Studies:** Declarative case studies with rubric-based concept and keyword matching derived from `caps-wiki/`.

---

## 5. Institutional Integration & Infrastructure Resilience

### 5.1 Teacher LMS Homework vs. Adaptive Progression (The "Teacher Express Lane")
In institutional deployments, teachers assign homework sets with fixed deadlines (e.g. Grade 10 Trigonometric Equations due tomorrow).
* **The Express Lane:** Teacher-assigned homework bypasses personal adaptive gates and appears in a prominent **Teacher Express Lane** on the student dashboard. A student who is currently regression-locked on Grade 9 prerequisite algebra is not prevented from attempting their teacher's assignment.
* **Dual-Ledger Telemetry:** Every response submitted in the Teacher Express Lane simultaneously updates the teacher's mark book and the student's personal BKT model. If the student struggles, targeted prerequisite regression drills are quietly queued into their self-study path without delaying their homework submission.

### 5.2 Offline-First Telemetry Sync Protocol (Load-Shedding & Taxi Commute Resilience)
South African learners face frequent load-shedding and high cellular data costs. Fundile implements an offline-first service worker architecture:
* **Pre-Caching:** When a student connects on Wi-Fi, the system pre-caches the diagnostic battery, formula sheets, SimuLearn scripts, and elementary drills for their active topics into browser IndexedDB via Vite PWA Workbox.
* **Offline Execution:** When cellular connectivity drops during a taxi commute or blackout, the student continues solving questions locally.
* **Atomic Batch Sync:** Telemetry records (step transitions, cell coordinates, timestamps, misconception tags) are queued in local IndexedDB (`offline_telemetry_queue`).
* **Auto-Reconnection:** As soon as network connectivity is restored, the client transparently dispatches the batch to `/api/session/end`, updating Firestore without data loss or user disruption.

---

## 6. Implementation Roadmap & Universal Engine Contracts

All new and refactored question generators must satisfy the **Universal 6-Pillar Generator Contract** to power the entire diagnostic, adaptive progression, and post-readiness exam pipeline:

```python
# Universal Generator Output Contract Example (Bank Reconciliation)
{
    "question_id": "gr10_acct_term2_bank_recon_compound_01",
    "term": 2,                                # Powers Exam-on-Demand filtering
    "caps_weight_percent": 18,                # Weight in official term test
    "suggested_duration_mins": 15,            # Pacing calculation (1.2 mins/mark)
    "mode": "compound",                       # Supports "elementary_<subskill>"
    "subskill_id": "gr10_acct_recon_timing",
    "learning_objective_id": "LO_RECON_02",
    "cognitive_level": 3,                     # CAPS Level 1..4 demand
    "marking_schema": {
        "total_marks": 12,
        "marking_points": [
            {"id": "mp_1", "desc": "CRJ interest entry", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Bank Recon outstanding deposit", "marks": 3, "editable": True}
        ],
        "deductions": [
            {"rule": "must_be_empty_filled", "penalty": -1}
        ],
        "carry_forward_rule": "consequential_accuracy"
    },
    "hints": {
        "tier_1": "Look at the bank statement credit column on the 28th.",
        "tier_2": "Amounts credited by the bank that do not appear in the CRJ are direct deposits.",
        "tier_3": "Enter R4,500 in the CRJ under Bank and Current Income."
    },
    "misconception_tags": [
        "net_vs_gross_confusion",
        "bank_recon_vs_journal_classification_error"
    ]
}
```

### Technical Deliverables & Phasing
1. **Phase 1: Generator Contract Standardization:** Ensure all active generators across all 7 subject domains declare horizontal subskills, cognitive levels (1..4), and `mode="elementary_<subskill>"`.
2. **Phase 2: Prerequisite Registry Integration:** Wire `caps-ai-backend/app/utils/prerequisite_registry.py` into the session progression engine so 2-consecutive failures trigger automatic adaptive regression.
3. **Phase 3: Diagnostic Entry Flow:** Implement the 3-question Micro-Benchmark on first topic touch with the homework escape hatch.
4. **Phase 4: Post-Readiness Evaluative Test Engine:** Deploy Topic-Based Tests, Term-Based Control Tests, and End-of-Year Mock Papers with Post-Exam Triage debriefs.
5. **Phase 5: Offline Sync & Pacing Engine:** Deploy IndexedDB telemetry buffering and the 45-minute deliberate practice circuit breaker.
