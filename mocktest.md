# Fundile National Curriculum Full Stack Mock Testing Master Plan (Grades 7–12)

**Version:** 1.0.0  
**Protocol:** Step-by-Step Interactive Human-in-the-Loop Certification  
**Testing Principle:** The Super Admin (You) manually approves all payments and inspects live state transitions with your own eyes. No blackbox automation until manual verification of each set is complete.  
**Payment Ratio:** 95% submit Proof of Payment (EFT) requiring manual Super Admin approval; 5% sample the 2-week free trial.  
**Scope:** 100% of South African CAPS Subjects across Senior Phase (Grades 7–9) and FET Phase (Grades 10–12).

---

## Progress Dashboard

| Set | Grade & Focus | Concurrent Stakeholders | Cognitive Modality | Payment Mode | Status |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **Set 1** | **Gr 10 FET Core**<br>Mathematics & Accounting | Lesedi Khumalo (Learner)<br>Super Admin (You) | 2D Ledger Table + KaTeX/SymPy | R349 Term Pass (EFT) | 🟡 **Ready to Run** |
| **Set 2** | **Gr 7 Senior Phase Foundation**<br>Maths (Nets, Patterns & Div) & EMS | Ayanda Ndlovu (Learner)<br>Mrs. P. Khumalo (Teacher, `MTH701`)<br>Mr. S. Ndlovu (Parent)<br>Super Admin (You) | Columnar Long Division Grid + Geometric Net Unfolding SVG + Source Documents | R349 Term Pass (EFT) | ⚪ Queued |
| **Set 3** | **Gr 8 Senior Phase**<br>Maths & Natural Sciences | Bongani Sithole (Learner)<br>Mr. D. Naidoo (Teacher, `SCI802`)<br>Mrs. T. Sithole (Parent)<br>Super Admin (You) | Symbolic Algebra + Particle Matter Diagrams | R149 Monthly (EFT) | ⚪ Queued |
| **Set 4** | **Gr 9 Senior Phase Transition**<br>EMS & Natural Sciences | Zanele Mthembu (Learner)<br>Mrs. V. Pillay (Teacher, `EMS903`)<br>Super Admin (You) | Accounting Equation (A = O + L) + Ohm's Law Circuits | **2-Week Free Trial**<br>*(5% Sample)* | ⚪ Queued |
| **Set 5** | **Gr 10 Commercial & Applied**<br>Business Studies & Maths Lit | Siyabonga Cele (Learner)<br>Super Admin (You) | Environmental Rubric + Tariff Rate Schedules | R149 Monthly (EFT) | ⚪ Queued |
| **Set 6** | **Gr 11 Physical & Tech Maths**<br>Physical Sciences & Tech Maths | Ntsako Baloyi (Learner)<br>Dr. K. Mokoena (Teacher, `PHY110`)<br>Super Admin (You) | Vector Resolution & SI Units + Radians & Complex Numbers | R349 Term Pass (EFT) | ⚪ Queued |
| **Set 7** | **Gr 11 Life Sciences & Accounting**<br>Life Sciences & Asset Accounting | Kelebogile Dlamini (Learner)<br>Mrs. N. Dlamini (Parent)<br>Super Admin (You) | Biological Process Flowcharts + Depreciation Schedules | R349 Term Pass (EFT) | ⚪ Queued |
| **Set 8** | **Gr 12 Matric Distinction Peak**<br>Mathematics & Physical Sciences | Prince Mthembu (Learner)<br>Mr. V. Pillay (Principal / HOD)<br>Super Admin (You) | Differential Calculus [M][CA] + Chemical Equilibrium Kc | R999 Annual (EFT) | ⚪ Queued |
| **Set 9** | **Gr 12 Corporate & Governance**<br>Accounting & Business Studies | Thabo Molefe (Learner)<br>Mr. N. Sithole (Teacher, `ACC12B`)<br>Super Admin (You) | Published Corporate Balance Sheet + King IV / Companies Act Rubrics | R349 Term Pass (EFT) | ⚪ Queued |
| **Set 10** | **Gr 12 Applied & Technical**<br>Technical Maths & Maths Lit | Lerato Khanyile (Learner)<br>Mr. J. Khanyile (Parent)<br>Super Admin (You) | Integration Mechanics + SARS Tax Brackets (PAYE) | R149 Monthly (EFT) | ⚪ Queued |
| **Set 11** | **Cross-Grade Adaptive Descent**<br>Gr 12 -> Gr 10 -> Gr 8 Regression | Sibusiso Zulu (Struggling Learner)<br>HOD / Principal Pillay<br>Super Admin (You) | Automated Prerequisite Descent & Foundational Repair | Systemic License Sync | ⚪ Queued |

---

## Detailed Set Specifications

### Set 1: Grade 10 FET Core — Mathematics & Accounting
- **Concurrent Users:**
  1. `Learner`: **Lesedi Khumalo** (Grade 10 FET, Westville High School)
  2. `Super Admin`: **You**
- **Syllabus Content:**
  - **Mathematics:** Term 1 Euclidean Geometry (Circle theorems & line transitions) + Algebraic Expressions.
  - **Accounting:** Term 1 Cash Receipts Journal (CRJ) & General Ledger with 15% VAT split.
- **Cognitive Modalities Tested:**
  - 2D Ledger Table with cell-level coordinate marking (`r0_c0` to `r5_c5`).
  - KaTeX Symbolic Derivations with South African comma decimal separator (`{,}`).
- **Misconceptions Targeted:**
  - `net_vs_gross_vat_confusion`: Student puts 115% gross amount into 100% sales column.
  - `exterior_angle_inversion`: Misidentifying cyclic quad exterior angle relation.
- **Payment & Approval Workflow:**
  - Fresh signup → Skips 2-week trial → Selects **School Term Pass (R349 / 3 Months)** → Attaches Access Bank POP (`e2e/fixtures/sample_pop.pdf`).
  - **You open Super Admin**: Inspect pending slip → Click **`3 Mo (Term)`** button.
  - **Live Verification**: Student paywall drops immediately; problem surface loads deterministically with pre-baked 3-tier hints.

---

### Set 2: Grade 7 Senior Phase Foundation — Mathematics & EMS
- **Concurrent Users:**
  1. `Learner`: **Ayanda Ndlovu** (Grade 7 Senior Phase)
  2. `Teacher`: **Mrs. Patience Khumalo** (Class Join Code: `MTH701`)
  3. `Parent`: **Mr. Sipho Ndlovu** (Guardian Phone: `+27 82 555 7892`)
  4. `Super Admin`: **You**
- **Syllabus Content:**
  - **Mathematics:**
    - Term 1: Number Patterns ($T_n = 4n - 1$) + Columnar Long Division ($4394 \div 26 = 169$).
    - Term 3: **Geometry of 3D Objects: Geometric Nets for 3D Shapes** (2D nets for cubes, rectangular prisms, triangular prisms, square pyramids, and cylinders; Polyhedra properties $F, V, E$ and Euler's formula $F + V - E = 2$; Total surface area calculated by unfolding 2D net polygons).
  - **EMS:** Financial Literacy — Source Documents (Receipts, Cheque Counterfoils, Deposit Slips).
- **Cognitive Modalities Tested:**
  - South African Columnar Arithmetic Grid (`dividend`, `divisor`, `quotient`, `intermediate_steps`).
  - **Interactive 2D Geometric Net Unfolding Canvas** (Declarative SVG diagram spec with folding net layouts, face matching, and surface area summation).
  - Mobile Pixel 7 Viewport (44px touch targets, sticky bottom subject carousel).
- **Misconceptions Targeted:**
  - `net_overlapping_faces_misconception`: Failing to recognize overlapping flaps in invalid 2D net arrangements.
  - `eulers_formula_subtraction_slip`: Algebraic sign errors when evaluating $F + V - E = 2$.
  - `subtraction_borrowing_inversion`: Student subtracts smaller from larger in column borrowing slip (enters `128` instead of `169`).
  - `source_doc_receipt_vs_invoice`: Confusing cash received document with credit invoice.
- **Payment & Linking Workflow:**
  - Enrolls via Teacher Join Code `MTH701` → Error recovery on arithmetic grid → Generates 15-minute ephemeral linking passcode `PAR-7892`.
  - **Mr. Sipho Ndlovu (Parent)** redeems `PAR-7892` on mobile viewport → Inspects in-app Sunday Academic Pulse showing **1.4 MB cellular data consumption** (< 2 MB PWA vs 450 MB video tutoring) and the repaired cognitive card.

---

### Set 3: Grade 8 Senior Phase Core — Mathematics & Natural Sciences
- **Concurrent Users:**
  1. `Learner`: **Bongani Sithole** (Grade 8 Senior Phase)
  2. `Teacher`: **Mr. David Naidoo** (Class Join Code: `SCI802`)
  3. `Parent`: **Mrs. Thandiwe Sithole**
  4. `Super Admin`: **You**
- **Syllabus Content:**
  - **Mathematics:** Algebraic Equations (Linear single-variable: $3x - 7 = 20$) + Integers with negative signs.
  - **Natural Sciences:** Matter & Materials (Particle model of matter, atoms, elements, compounds, density calculations $\rho = \frac{m}{V}$).
- **Cognitive Modalities Tested:**
  - SymPy Canonical Solution Graph (Linear line balance).
  - Particle arrangement diagrams + SI unit input normalization ($g/cm^3$ to $kg/m^3$).
- **Misconceptions Targeted:**
  - `sign_change_transposition`: Forgetting to invert sign when transposing term across equals sign.
  - `mass_volume_density_inversion`: Calculating density by multiplying mass by volume.
- **Payment & Approval Workflow:**
  - Fresh signup → Selects **Monthly Pass (R149 / Month)** → Submits FNB EFT POP → **You manually approve 30-Day Access** → Solves science density calculation.

---

### Set 4: Grade 9 Senior Phase Transition — EMS & Natural Sciences (Trial Path)
- **Concurrent Users:**
  1. `Learner`: **Zanele Mthembu** (Grade 9 Transition Phase)
  2. `Teacher`: **Mrs. V. Pillay** (Class Join Code: `EMS903`)
  3. `Super Admin`: **You**
- **Syllabus Content:**
  - **EMS:** The Accounting Equation ($Assets = Owner's\ Equity + Liabilities$) with Cash Receipts (CRJ) and Cash Payments (CPJ).
  - **Natural Sciences:** Energy & Change (Series and Parallel Circuits, Ohm's Law $V = I \times R$, potential difference).
- **Cognitive Modalities Tested:**
  - 3-Column Accounting Equation table ($A = O + L$) with effect signs ($+ / - / 0$) and reasons.
  - Declarative SVG Circuit diagrams with ammeters and voltmeters.
- **Misconceptions Targeted:**
  - `owner_equity_expense_inversion`: Recording an expense as an increase in Owner's Equity.
  - `series_parallel_current_confusion`: Assuming current splits in a series circuit.
- **Payment Workflow (The 5% Trial Sample):**
  - Fresh signup → **Activates 14-Day Free Diagnostic Trial** → Banner displays countdown ("14 Days Remaining on Trial") → Workspace unlocks immediately with zero payment friction.

---

### Set 5: Grade 10 Commercial & Applied — Business Studies & Maths Lit
- **Concurrent Users:**
  1. `Learner`: **Siyabonga Cele** (Grade 10 FET Phase)
  2. `Super Admin`: **You**
- **Syllabus Content:**
  - **Business Studies:** Micro, Market, and Macro business environments (SWOT & PESTLE analysis).
  - **Mathematical Literacy:** Tariffs & Break-even analysis (Municipal water & electricity tiered brackets).
- **Cognitive Modalities Tested:**
  - Rubric-based semantic concept matching (Keyword & concept alignment from `caps-wiki/business_studies/grade10/`).
  - Tiered tariff calculation tables (Stepwise block rate pricing).
- **Misconceptions Targeted:**
  - `macro_vs_market_confusion`: Classifying competitors as Macro instead of Market environment.
  - `tariff_cumulative_bracket_slip`: Applying the highest tariff rate to the entire consumption rather than tiered blocks.
- **Payment & Approval Workflow:**
  - Fresh signup → Submits Nedbank EFT POP for **Monthly Pass (R149)** → **You approve in Super Admin** → Learner completes tariff step calculation.

---

### Set 6: Grade 11 Physical Sciences & Technical Mathematics
- **Concurrent Users:**
  1. `Learner`: **Ntsako Baloyi** (Grade 11 FET Phase)
  2. `Teacher`: **Dr. K. Mokoena** (Class Join Code: `PHY110`)
  3. `Super Admin`: **You**
- **Syllabus Content:**
  - **Physical Sciences:** Newton's Laws of Motion (Newton I, II, III) + Vector force resolution on inclined planes ($F_g = mg \sin\theta$).
  - **Technical Mathematics:** Complex Numbers ($z = a + bi$, Argand diagrams) + Radian measure and angular velocity ($\omega = \frac{\theta}{t}$).
- **Cognitive Modalities Tested:**
  - Vector resolution free-body diagrams with directional tags ($[N]$, $[S]$, $[E]$, $[W]$, $[\text{down the slope}]$).
  - Complex number rectangular to polar form transformations.
- **Misconceptions Targeted:**
  - `omitted_normal_force_component`: Forgetting that on an incline $F_N = mg \cos\theta$.
  - `i_squared_positive_slip`: Treating $i^2$ as $+1$ instead of $-1$.
- **Payment & Approval Workflow:**
  - Fresh signup → Submits Standard Bank EFT POP for **Term Pass (R349)** → **You approve in Super Admin** → Solves inclined plane vector calculation with mandatory SI units ($N$, $kg \cdot m \cdot s^{-2}$).

---

### Set 7: Grade 11 Life Sciences & Asset Accounting
- **Concurrent Users:**
  1. `Learner`: **Kelebogile Dlamini** (Grade 11 FET Phase)
  2. `Parent`: **Mrs. Nomsa Dlamini** (Linked Guardian)
  3. `Super Admin`: **You**
- **Syllabus Content:**
  - **Life Sciences:** Photosynthesis & Cellular Respiration (Light/dark phases, ATP synthesis, glycolysis, Krebs cycle).
  - **Accounting:** Fixed Assets & Depreciation (Straight-line vs. Reducing-balance methods, Asset Disposal account).
- **Cognitive Modalities Tested:**
  - Biological process flowchart matching and organelle structure identification.
  - 4-Column Asset Disposal Ledger with carrying value and profit/loss calculation.
- **Misconceptions Targeted:**
  - `depreciation_cost_vs_carrying_confusion`: Calculating reducing balance depreciation on historical cost instead of book value.
  - `atp_aerobic_anaerobic_yield_slip`: Confusing 2 ATP anaerobic yield with 36-38 ATP aerobic yield.
- **Payment & Linking Workflow:**
  - Fresh signup → Submits Capitec EFT POP for **Term Pass (R349)** → **You approve in Super Admin** → Completes asset disposal memo → Parent inspects weekly topic mastery card on in-app profile.

---

### Set 8: Grade 12 Matric Distinction Peak — Mathematics & Physical Sciences
- **Concurrent Users:**
  1. `Learner`: **Prince Mthembu** (Grade 12 Matric Candidate, Westville High School)
  2. `Principal / HOD`: **Mr. Vinay Pillay** (School Administrator)
  3. `Super Admin`: **You**
- **Syllabus Content:**
  - **Mathematics:** Differential Calculus (First principles derivative $f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$ + Cubic polynomials & optimization).
  - **Physical Sciences:** Chemical Equilibrium ($K_c$ expressions, Le Chatelier's principle, RICE tables) + Doppler Effect with moving observer/source.
- **Cognitive Modalities Tested:**
  - Method marks [M] and Consequential Accuracy [CA] SymPy derivation tracking.
  - RICE (Ratio, Initial, Change, Equilibrium) chemical concentration matrix.
- **Misconceptions Targeted:**
  - `limit_h_zero_dropped_early`: Omitting $\lim_{h \to 0}$ before dividing through by $h$.
  - `kc_solids_liquids_included`: Including pure solids or pure liquids in the $K_c$ equilibrium expression.
- **Payment & School Admin Workflow:**
  - Fresh signup → Selects **Annual Distinction Pass (R999 / 12 Months)** → Attaches Investec EFT POP → **You manually approve 365-Day Access**.
  - **Mr. Vinay Pillay (Principal)** logs into School Admin Cockpit → Reviews Grade 12 Calculus pacing heatmap → Exports trial mark roster for SASAMS CSV format.

---

### Set 9: Grade 12 Corporate & Governance — Accounting & Business Studies
- **Concurrent Users:**
  1. `Learner`: **Thabo Molefe** (Grade 12 Matric Candidate)
  2. `Teacher`: **Mr. N. Sithole** (Class Join Code: `ACC12B`)
  3. `Super Admin`: **You**
- **Syllabus Content:**
  - **Accounting:** Financial Statements of a Public Company (Statement of Comprehensive Income, Balance Sheet, Notes to Financial Statements, Cash Flow Statement).
  - **Business Studies:** Human Resources, Corporate Social Responsibility (CSR), and Business Strategies under King IV Code of Governance.
- **Cognitive Modalities Tested:**
  - Authentic 8-row Published Financial Statement ledger with Retained Income notes.
  - Semantic Rubric match for King IV transparency, accountability, and fairness principles.
- **Misconceptions Targeted:**
  - `retained_income_dividends_timing_error`: Confusing interim dividends paid with final dividends declared.
  - `csr_vs_csi_concept_slip`: Conflating internal operational CSR with external philanthropic CSI expenditure.
- **Payment & Approval Workflow:**
  - Fresh signup → Enrolls in `ACC12B` → Submits POP for **Term Pass (R349)** → **You approve in Super Admin** → Solves Cash Flow Statement operating activities section.

---

### Set 10: Grade 12 Applied & Technical Pathways — Tech Maths & Maths Lit
- **Concurrent Users:**
  1. `Learner`: **Lerato Khanyile** (Grade 12 Technical Candidate)
  2. `Parent`: **Mr. Joshua Khanyile**
  3. `Super Admin`: **You**
- **Syllabus Content:**
  - **Technical Mathematics:** Integral Calculus (Indefinite and definite integrals, area between curves $\int_{a}^{b} [f(x) - g(x)] dx$).
  - **Mathematical Literacy:** Taxation & Finance (South African Revenue Service SARS income tax brackets, medical tax credits, rebates).
- **Cognitive Modalities Tested:**
  - Stepwise symbolic integration with constant of integration $+ C$.
  - Multi-bracket SARS progressive income tax calculator table.
- **Misconceptions Targeted:**
  - `forgot_plus_c_integration`: Omitting constant $+ C$ in indefinite integration.
  - `sars_bracket_flat_tax_slip`: Calculating tax as total taxable income multiplied by top bracket marginal percentage.
- **Payment & Linking Workflow:**
  - Fresh signup → Submits POP for **Monthly Pass (R149)** → **You approve in Super Admin** → Completes SARS tax bracket derivation → Parent confirms linked student progress.

---

### Set 11: Cross-Grade Adaptive Descent & Prerequisite Lineage Stress Test
- **Concurrent Users:**
  1. `Learner`: **Sibusiso Zulu** (Simulated struggling Grade 12 student)
  2. `HOD / Principal`: **Mr. Vinay Pillay** (School Administrator)
  3. `Super Admin`: **You**
- **Syllabus & Lineage Content:**
  - **The Blocker:** Student attempts Grade 12 Calculus optimization: $V'(r) = 0 \implies 3\pi r^2 - 12r = 0$.
  - **The Root Cause:** Fails basic quadratic factorisation (common factor extraction $3r(r - 4) = 0$) twice in a row.
  - **The Adaptive Descent:** System executes `prerequisite_tree.py` lineage map:
    - Drops student from Grade 12 Calculus $\to$ Grade 10 Algebraic Expressions (Factorising trinomials) $\to$ Grade 8 Highest Common Factor (HCF).
  - **The Remediation:** Student completes 5-minute atomic micro-drill on HCF $\to$ Rebuilds factorisation schema $\to$ Automatically ascends back to Grade 12 Calculus optimization.
- **Cognitive Modalities Tested:**
  - Dynamic Adaptive Prerequisite Lineage Banner.
  - Circuit Breaker to 5-minute SimuLearn worked visual replay.
- **School Admin Systemic Broadcast:**
  - Principal Pillay sees the systemic factorisation blocker flagged across 38 learners $\to$ Clicks **[ Broadcast Remedial Drill ]** to dispatch the 5-minute micro-fix school-wide.

---

## Operating Protocol for Execution

1. **One Set at a Time:** We do not touch Set 2 until Set 1 is 100% verified and approved by you.
2. **Fresh Signup Every Set:** Each set begins with a brand new user registration to ensure zero cached state or stale session contamination.
3. **Manual Approval via Super Admin:** You open the Super Admin interface, view the pending submission, and click the approval button with your own mouse.
4. **Visual Invariant:** You watch the learner's workspace unlock and verify that real curriculum questions load with zero fallbacks.
5. **Manifest & HTML Synchronization:** At the conclusion of every certified set, `fundile-architecture.json` and `fundile-architecture.html` are updated and regenerated.
