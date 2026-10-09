# Curriculum Verification & Completion Master Execution Plan (Grades 7–12)

> **Document Version:** 1.0.0  
> **Audited Date:** 2026-10-09  
> **Source Documents:** `caps-ai-backend/curriculum_docs_auto/*/Syllabus.md` & `curriculum_docs/`  
> **Guiding Principle:** "Just because there are `.md`s and generators does not mean the topic is complete." Every topic must be verified against its official South African CAPS Annual Teaching Plan (ATP) weekly breakdown, cognitive weighting, and assessment requirements.

---

## 1. Executive Ground-Truth Audit: Syllabus.md vs. Active Generators

A rigorous automated parse of all **30 official CAPS `Syllabus.md` files** across Grades 7–12 identified **3,591 instructional sub-units and weekly ATP requirements**. 

| Subject & Grade | Total Syllabus ATP Units | Genuine Dedicated | Cross-Grade Proxy | Granular Gaps | Real Coverage % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **EMS Grade 7** | 78 | 76 | 2 | 0 | 97.4% |
| **EMS Grade 8** | 79 | 77 | 2 | 0 | 97.5% |
| **EMS Grade 9** | 66 | 65 | 1 | 0 | 98.5% |
| **Business Studies Grade 10** | 182 | 182 | 0 | 0 | 100.0% |
| **Business Studies Grade 11** | 165 | 165 | 0 | 0 | 100.0% |
| **Business Studies Grade 12** | 172 | 172 | 0 | 0 | 100.0% |
| **Life Sciences Grade 10** | 94 | 94 | 0 | 0 | 100.0% |
| **Life Sciences Grade 11** | 90 | 90 | 0 | 0 | 100.0% |
| **Life Sciences Grade 12** | 71 | 71 | 0 | 0 | 100.0% |
| **Mathematical Literacy Gr 10** | 38 | 38 | 0 | 0 | 100.0% |
| **Mathematical Literacy Gr 11** | 38 | 38 | 0 | 0 | 100.0% |
| **Mathematical Literacy Gr 12** | 21 | 21 | 0 | 0 | 100.0% |
| **Technical Mathematics Gr 10** | 45 | 45 | 0 | 0 | 100.0% |
| **Technical Mathematics Gr 11** | 43 | 43 | 0 | 0 | 100.0% |
| **Technical Mathematics Gr 12** | 46 | 46 | 0 | 0 | 100.0% |
| **Physical Sciences Grade 10** | 237 | 237 | 0 | 0 | 100.0% |
| **Physical Sciences Grade 11** | 203 | 203 | 0 | 0 | 100.0% |
| **Physical Sciences Grade 12** | 276 | 276 | 0 | 0 | 100.0% |
| **Natural Sciences Grade 7** | 139 | 139* | 0 | 0 | *Clustered |
| **Natural Sciences Grade 8** | 161 | 161* | 0 | 0 | *Clustered |
| **Natural Sciences Grade 9** | 203 | 203* | 0 | 0 | *Clustered |
| **Mathematics Grade 7** | 122 | 55 | 1 | 66 | 45.1% |
| **Mathematics Grade 8** | 199 | 58 | 2 | 139 | 29.1% |
| **Mathematics Grade 9** | 166 | 54 | 0 | 112 | 32.5% |
| **Mathematics Grade 10** | 62 | 15 | 0 | 47 | 24.2% |
| **Mathematics Grade 11** | 53 | 14 | 2 | 37 | 26.4% |
| **Mathematics Grade 12** | 88 | 16 | 1 | 71 | 18.2% |
| **Accounting Grade 10** | 143 | 9 | 8 | 126 | 6.3% |
| **Accounting Grade 11** | 148 | 3 | 4 | 141 | 2.0% |
| **Accounting Grade 12** | 163 | 5 | 8 | 150 | 3.1% |
| **TOTAL** | **3,591** | **2,671** | **31** | **889** | **74.4%** |

### Key Takeaways from the Audit
1. **The "Monolithic Archetype" Fallacy**: In Accounting and Mathematics, while there were generators that passed high-level topic titles (e.g., `sole_trader`, `algebraic_expressions`), they only tested 1 or 2 static question archetypes, failing to provide practice on the 10–20 sub-skills outlined in the CAPS syllabus (such as specific year-end adjustments, salaries journals, decimal fractions, angle relationships, or probability trees).
2. **The "Cross-Grade Shortcut" Trap**: 31 topics relied on cross-grade shortcuts (e.g. Grade 10 Budgeting borrowing Grade 12 Matric Cash Budgets; Grade 7 Graphs borrowing Grade 8 Functions).
3. **EMS Completeness**: EMS Grades 7–9 are over 97% complete, needing only 2 specific sub-skill generators (`The production process` in Grade 7 Term 3, and `Levels and functions of management` in Grade 8 Term 3).

---

## 2. The 6-Pillar Generator Standard (Mandatory Contract)

Every new or upgraded generator MUST adhere to the non-negotiable contract:
1. **Term & ATP Pacing Metadata**: Emits `term` (1–4), `caps_weight_percent`, and `suggested_duration_mins`.
2. **Deconstructibility (Atomic Micro-Drills)**: Supports `mode="compound" | "elementary_<subskill>"`.
3. **Standardized Misconception Taxonomy**: Snake_case tags (e.g., `net_vs_gross_confusion`, `fraction_denominator_addition_error`).
4. **Teacher-Editable Marking Schema**: Explicit `marking_points` with point descriptions and marks.
5. **Deterministic 3-Tier Hints**: Pre-computed Tier 1 (Nudge), Tier 2 (Rule), Tier 3 (Worked calculation).
6. **Modality & Zero-Meta Invariant**: Native modality (2D ledger, SymPy/KaTeX, Rubric). **Zero** mentions of "According to CAPS" or curriculum policy bureaucracy.

---

## 3. Systematic Execution Roadmap

### Phase 1: Senior Phase Mathematics (Grades 7–9)
- [ ] **Task 1.1: Grade 7 Mathematics Decimals Generator**
  - Path: `caps-ai-backend/app/utils/grade7_mathematics/decimals_generator.py`
  - Sub-skills: Place value up to 3 decimals, converting fractions to decimals, operations (+, -, ×, ÷ by 10, 100, 1000), rounding to 1 and 2 decimal places.
- [ ] **Task 1.2: Grade 7 Mathematics 2D Geometry & Angles Generator**
  - Path: `caps-ai-backend/app/utils/grade7_mathematics/geometry_2d_generator.py`
  - Sub-skills: Angles classification (acute, right, obtuse, straight, reflex, revolution), triangle classification by sides and angles, sum of interior angles ($180^\circ$), quadrilateral properties (square, rectangle, parallelogram, rhombus, trapezium, kite).
- [ ] **Task 1.3: Grade 7 Mathematics Probability & Data Handling Generator**
  - Path: `caps-ai-backend/app/utils/grade7_mathematics/data_probability_generator.py`
  - Sub-skills: Single-event theoretical probability ($0 \le P \le 1$), relative frequency vs theoretical, mean, median, mode, range from raw data sets.
- [ ] **Task 1.4: Grade 7 Mathematics Graphs & Relationships**
  - Path: `caps-ai-backend/app/utils/grade7_mathematics/graphs_relationships_generator.py`
  - Sub-skills: Input/output flow diagrams, tables of ordered pairs, drawing and interpreting bar graphs and linear relationship graphs (replacing the Grade 8 proxy).

### Phase 2: Senior Phase EMS (Grades 7–9)
- [ ] **Task 2.1: Grade 7 EMS Production Process Generator**
  - Path: `caps-ai-backend/app/utils/grade7_ems/term3_production_process.py`
  - Sub-skills: Meaning of production, inputs (raw materials), processes, outputs, primary vs secondary vs tertiary production.
- [ ] **Task 2.2: Grade 8 EMS Levels & Functions of Management Generator**
  - Path: `caps-ai-backend/app/utils/grade8_ems/term3_management.py`
  - Sub-skills: Top, middle, lower management levels; 4 core management tasks: Planning, Organising, Leading, Controlling (POLC).
- [ ] **Task 2.3: Wire & Replace EMS Proxies in Registry**
  - Connect `term3_production_process` and `term3_management` into `generator_registry.py`.

### Phase 3: Senior Phase Natural Sciences (Grades 7–9)
- [ ] **Task 3.1: Grade 7 Natural Sciences Life & Living & Energy**
  - Dedicated generators for Biosphere, Biodiversity, Sexual reproduction in plants, Heat energy transfer.
- [ ] **Task 3.2: Grade 8 Natural Sciences Atoms & Reactions**
  - Dedicated generators for Particle model of matter, Chemical reactions, Static electricity, Visible light.
- [ ] **Task 3.3: Grade 9 Natural Sciences Earth & Beyond & Forces**
  - Dedicated generators for Human systems, Cost of electrical energy, Forces and balanced systems, Earth as a system.

### Phase 4: FET Accounting (Grades 10–12)
- [ ] **Task 4.1: Eliminate Grade 10 Accounting Proxies**
  - Build Grade 10-specific elementary Cash Budgeting and Manufacturing cost concepts (removing the Grade 12 Matric proxy).
- [ ] **Task 4.2: Grade 11 Accounting Adjustments & Statements**
  - Bank Reconciliation adapted to Grade 11 depth; Partnership adjustments and financial statements.
- [ ] **Task 4.3: Grade 12 Accounting Statements & Indicators**
  - Cash flow statements with notes; Financial indicator interpretation with recommendations.

### Phase 5: Verification, Testing & Architecture Manifest Sync
- [ ] **Task 5.1: Monte Carlo Audit (100 Seeds per Generator)**
  - Verify deterministic mathematical correctness, 0 exceptions, < 2.5s runtime.
- [ ] **Task 5.2: Zero-Meta-Curriculum Invariant Audit**
  - Ensure zero mentions of "According to CAPS" across all prompts, options, and memos.
- [ ] **Task 5.3: Architecture Manifest & HTML Sync**
  - Update `fundile-architecture.json` and run `python generate_architecture_html.py`.

---

## 4. Execution Sequence & Status Log

| Step | Action | Status | Notes |
| :---: | :--- | :---: | :--- |
| **0** | Author Master Execution Plan | **DONE** | Created `curriculum_syllabus_verification_and_execution_plan.md` |
| **1** | Build Grade 7 EMS Production Process Generator | **IN PROGRESS** | Resolving Grade 7 Term 3 proxy fallback |
| **2** | Build Grade 8 EMS Management Generator | **PENDING** | Resolving Grade 8 Term 3 gap generator |
| **3** | Build Grade 7 Math Decimals Generator | **PENDING** | Completing Grade 7 Term 2 decimals |
| **4** | Build Grade 7 Math 2D Geometry Generator | **PENDING** | Completing Grade 7 Term 2 geometry |
| **5** | Build Grade 7 Math Data & Probability Generator | **PENDING** | Completing Grade 7 Term 4 data & probability |
| **6** | Build Grade 7 Math Graphs & Relationships | **PENDING** | Removing Grade 8 functions proxy |
