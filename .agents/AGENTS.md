# General Development Rules (100% Active Context — Zero-Truncation Standard)

> **MANDATORY SKILL & DOCTRINE ROUTING (Read Before Acting)**:
> - **Diagrams, 3D Sidecars & Blender**: Read `diagram_doctrine.md` and `.agents/skills/flash-remediation-protocol/SKILL.md`.
> - **Question Generators & Memorandums**: Read `.agents/skills/caps-generator-contract/SKILL.md` and `.agents/skills/flash-remediation-protocol/SKILL.md`.
> - **Architecture Updates**: Read `.agents/skills/manifest-sync/SKILL.md`.

---

## 00. THE REUSABLE 50-ARCHETYPE ITERATION & IMPLEMENTATION WORKFLOW

Every topic across Grades 7–12 MUST follow this 5-phase workflow (`reusable_50_archetype_workflow_plan.md`). Synthetic shims (`_subskill_1..52`), single-template loops, and self-authored weak exit tests are banned.
1. **Phase 1 — 3-Tier Curriculum & Figure Extraction**: Ground in `curriculum_docs/`, `curriculum_docs_auto/` (extracting all `>DIAGRAM[...]` and `Figure/Diagram/Graph` blocks as drawing specs per `0d-14.4`), and `curriculum_source_files/` PDFs.
2. **Phase 2 — >= 50 Semantic Archetypes**: Enumerate >=50 distinct subskills with descriptive snake_case IDs (`01_<name>`), parameter ranges, formulas, and SA contexts. Zero `subskill_N` shims.
3. **Phase 3 — Parameterized Generator & Two-Surface Visuals**: Builders in `app/utils/{subject}/{generator}.py` parameterized via `rng: random.Random(seed)` emitting static 2D `diagram_spec` (Surface 1) + Visual Aid & `SimuLearnPlayer.jsx` `diagram_and_steps` replay (Surface 2).
4. **Phase 4 — Super Admin Archetype Iteration**: `SuperAdminArchetypeWorkbench.jsx` linear `1..N` cycling toggle.
5. **Phase 5 — Locked 5D Referee Audit**: Run `python scripts/run_universal_comprehensive_diagram_audit.py --strict` across seeds `[101, 102, 103]`. Never modify referee scripts or weaken `scripts/verify_plan.py`.

---

## 0a–0c. Architecture Manifest — Read First, Update Always

- **0a. SESSION START**: Read `fundile-architecture.json` in full before writing code. It is the single source of truth for built/planned components and `_workflow` rules.
- **0b. DURING SESSION**: Whenever you build or change the status of any layer, service, API route, frontend component, Firestore collection, or generator, update `fundile-architecture.json` immediately (`planned` -> `built`/`partial`, update `lastUpdated`, maintain `openQuestions`).
- **0c. SESSION END**: Always run `python generate_architecture_html.py` from the project root last. Never edit `fundile-architecture.html` directly.

---

## 0d. ZERO-THEATER & ANTI-SHODDY ENGINEERING INVARIANT (MANDATORY LAW)

- **0d-1. No Theatrical Testing ("Hollywood Pattern")**: Never write fake test actions, cosmetic HUD banners, simulated countdowns, or screenplay scripts. Every test step must execute real authentication, real form submissions, real DB state changes, and real UI navigation. Console logs only report verified post-assertion states.
- **0d-2. Strict Identity & Privilege Isolation (The Super Admin Law)**: Super Admin is strictly the authentic platform owner (`firestore.rules`: `princenqaba@gmail.com`, `princenqabamoyo@outlook.com`) using valid Firebase ID tokens. NEVER use `MOCK_SUPER_ADMIN`, URL query spoofing (`?persona=admin`), or classroom mocks for Super Admin clearance.
- **0d-3. Role-State Decoupling**: Admin and educator components must NEVER read or display state from `studentStore` (e.g. "Nqobile Dlamini") unless explicitly querying a learner record for oversight.
- **0d-4. Source-Code Grounding (Zero Phantom Selectors)**: Never write or modify a locator/testId in an E2E spec without first reading the target JSX file in `src/` to confirm its exact presence.
- **0d-5. Genuine End-to-End Actions (No Backdoor DB Substitution)**: DB helper scripts are ONLY permitted for pre-test clean-slate purge (`scripts/purge_test_user_admin.py`). Never substitute DB scripts for tested UI actions (e.g., Super Admin must open the signed URL POP and click the on-screen approval button).
- **0d-6. Zero Silent Skips in E2E**: NEVER wrap test steps in `if (await isVisible())`, `if (count > 0)`, or empty `catch` blocks. Use explicit `await expect(locator).toBeVisible()` / `.toBeEnabled()` so failures halt loudly.
- **0d-7. Runtime Execution Verification & Viewport Non-Interference**: Building (`npm run build`) is not executing. Always run the live script/test and inspect runtime output. Test HUDs must stay in `bottom: 16px; left: 16px` and never intercept app pointer events. Default to local dev (`http://localhost:5173` / `http://localhost:5001`).
- **0d-8. Holistic Cross-Spec Pre-Flight Gate (Anti-Whack-A-Mole Law)**: Before declaring any fix complete, run `npm run test:audit`, asserting:
  1. `python scripts/audit_generators_preservation.py` (0 deleted generators).
  2. `python scripts/audit_e2e_specs.py` (0 selector/privilege violations).
  3. `python scripts/audit_diagram_registry.py` & `audit_diagrams_md_coverage.py`.
  4. `npx playwright test --list` (0 cross-spec syntax/export errors).
  5. `node scripts/smoke_check.js` (clean DOM mount on `localhost:5173` with 0 console errors).
- **0d-9. Responsive Visibility & CSS Union Law**: Filter all union clauses by `:visible` (e.g. `[data-testid="btn"]:visible, button:has-text("..."):visible`); never append a trailing non-`:visible` fallback with `.first()`.
- **0d-10. Multi-Card Clearance Desk Scoping**: Scope repeating card actions strictly to the target card: `locator('div[data-testid^="payment-card-"]:has([data-testid="payment-email-${email}"])')`. Never use global `.first()` or global `text=approved`.
- **0d-11. Resilient Profile Upsert & Authentic Banking Receipts**: Use `setDoc(ref, data, { merge: true })` in `AdminForms.jsx` and `SchoolAdminView.jsx`. E2E POP uploads must use authentic vector South African banking receipts (`scripts/generate_authentic_pop_pdf.py`).
- **0d-12. Systematic Cross-Grade & Cross-Subject Generalization**: Never patch a defect only in the single reported grade/subject; audit and fix the root cause across all Grades 7–12 and all 9 subjects.
- **0d-13. Zero-Bundling & Authoritative Curriculum Manifest**: Every topic across all 30 tracks must have a dedicated generator grounded in `curriculum_docs_auto/*.md` and mapped 1:1 in `caps_term_registry_data.json`. No multi-topic grab bags, no dual registries, and must pass `python scripts/audit_semantic_relevance.py`.
- **0d-14 & Rule 29. Scientific, Anatomical & Geographic Diagram Authenticity Law (The Heart Standard & Unified Diagram Doctrine — see `diagram_doctrine.md`)**:
  1. **Separation of Concerns**: Question Cards use **100% static 2D exam figures** (never 3D simulations in graded cards). Interactive 3D (Three.js Paper & Ink) and dynamic parameter sliders ($a, b, c, d$) belong strictly in the **Enhancement Companion** (`CognitiveSidecarDrawer.jsx` + `SimuLearnPlayer.jsx`: Tab 1 Annotated Master Atlas, Tab 2 Live Process Simulation).
  2. **Zero Hand-Coded SVG Clipart (Approach A)**: Organic anatomy, cytology, histology, landforms, and lab apparatus MUST use publication-grade unlabeled plates (`<master>_textbook.jpg` + `<master>_exam_stipple.jpg` on pure `#FFFFFF` with 0 baked text/letters/arrows) in `public/diagrams/` generated via `image-generator` or Blender 5.2.3 MCP (`localhost:9876`). Raw SVG `<polygon>`/`<ellipse>`/`<circle>` clipart is banned (`python scripts/audit_heart_standard_plates.py --all`).
  3. **Question-Dedicated Pin Isolation & Visual Calibration**: `InteractiveCallouts.jsx` (`viewBox="0 0 600 480"`, horizontal elbow lines to `x=60`/`x=540`) must render ONLY the specific pins tested by the active question seed, filtered by `grades` mask in `caps-ai-backend/app/data/diagram_anchors/<master>.json`, using opaque tokens (`ref_1`, zero answer leaks). Always screenshot in a live browser and inspect via `read_file` to calibrate `[x, y]` coordinates dead-center.
  4. **Diagram Description → Design Law** <!-- RULE-ANCHOR: diagram_description_design_law -->: Figure descriptions in `curriculum_docs_auto/` (`>DIAGRAM[...]`, `Figure N.N`, `Diagram N`, `Graph N`, narrated measurements) are stand-ins for images lost in PDF → Markdown conversion. They are specs to **draw** as a seeded `diagram_spec`, never text to copy into `question_text`; the question must refer to the figure. Decorative photos are exempt. See `diagram_doctrine.md` §9; detector `python scripts/audit_diagram_description_leak.py`.
- **0d-15. Zero-Phantom-Implementation & Truthful Completion Law**:
  1. **5-Link Chain Required for "Complete"**: (1) File exists on disk, (2) Generator runs across >=3 seeds, (3) Backend API route returns payload with auth, (4) Frontend mounts in live browser with 0 console errors, (5) Interactive grading/evaluation passes. If any link is missing, report `PARTIAL: [Exact missing link]`.
  2. **Zero Fictional Tokens**: Verify every filename, function, route, and metric via shell command in the current turn before writing it.
  3. **Machine-Generated Reports Only**: Generate all tables/reports in `reports/` via Python scripts inspecting disk reality; never hand-type markdown status tables.
  4. **Banned Adjectival Fluff**: Words like *"Flawless"*, *"Gold Standard"*, *"Pristine"*, *"World-Class"* are banned. Use binary status: `PASS (Exit Code 0)`, `FAIL (Exit Code 1)`, or `PARTIAL: [Detail]`.

---

## Rules 30 & 31. Mechanical Enforcement & Plan Compliance Laws (Mandatory for All Models Including Gemini 3.8)

- **30. Full-Archetype Audit & Anti-Hollywood Mechanical Enforcement Law**:
  1. **Zero Sampling**: Execute, mount in live `UniversalWorkspace.jsx` (`1440x900`), and screenshot 100% of subskill archetypes across all requested topics (all 2,383 archetypes across Gr 7–12). Zero synthetic HTML stubs.
  2. **Mandatory Multi-Scroll Capture**: Whenever `scrollHeight > clientHeight + 60`, scroll in viewport increments capturing `pre_scroll_1..N.png` and `memo_scroll_1..N.png` to the bottom.
  3. **Zero Detector Weakening**: Never mute, comment out, or add bypass exceptions to deterministic audit checks. Fix the actual generator or React component grounded in `curriculum_docs_auto/`.
  4. **Gatekeeper**: No grade audit is complete until `python scripts/verify_no_hollywood_audit.py --grade <G>` returns `PASS (Exit Code 0)`.
- **31. Plan Compliance & Evidence-Based Completion Law**:
  1. **Every Plan Item Has an ID & Exit Test**: Every deliverable (`GP-1`, `GP-2`, ...) must have an executable command exiting `0` on pass. If no exit test exists, write the test first.
  2. **Done = Command Exits 0 in Current Turn**: Mark `PASS` only when the item's exit command was run in the current turn with real output shown.
  3. **Final Report = `python scripts/verify_plan.py` Output**: Reproduce all plan items in order (`PASS`, `FAIL`, `PARTIAL: <missing link>`, or `NOT DONE`). End every completion report with `"Items not done or only partly done"` (or `"None (all items PASS per verify_plan.py)"`).
  4. **Small Batches with Mandatory Stop**: Execute at most 1 phase or 8 items per turn, run `scripts/verify_plan.py`, report the table, and stop for owner review.
  5. **No Self-Grading & Real Chain Only**: Never weaken an exit test. Question/memo/diagram exit tests must run through `generator -> API route -> mounted UniversalWorkspace.jsx`.

---

## Rules 1–28. Core Platform, Curriculum, Modality & Operations Laws

1. **Always Build Full-Stack**: Implement both backend (generators, routes) and frontend React UI (Diagnostic, Scaffold, Practice, Exam modes).
2. **Native Cognitive Modalities & Branding (`Rules 2, 2b, 25`)**:
   - Render each subject in its native modality: Accounting/EMS (2D ledgers with `required`/`given`/`must_be_empty` cells & full Markdown table memos), Mathematics (SymPy step graphs + KaTeX working pad + comma decimals `{,}` via `_decomma`), Business Studies (rubric keyword/concept matching), Geometry/Graphs (GeoGebra+/JSXGraph).
   - **Zero "CAPS" Acronym or Examining Body Trademarks in UI (`Rule 2b`)**: Never display `"CAPS"`, `"IEB"`, `"SACAI"`, `"DBE"`, or `"NSC"` in student/parent/teacher UI or marketing. Use universal statements: *"100% Aligned with South African National Curriculum Standards"*.
3. **Hint System & File Size Limit (`Rules 3–4`)**: Adhere strictly to `hint_system_specification.md` (cell-level hints for tables; deterministic 3-tier pre-baked hints for non-tables). Keep all files `< 2000` lines; always backup `src/App.jsx` before editing.
4. **Application Tiers & Agentic System (`Rules 5–14`)**:
   - **Standard Package**: 100% deterministic Python/SymPy generation, hints, marking, and progression (`60%` Scaffold -> Practice, `80%` -> Assessment). Zero LLM calls, zero token cost.
   - **Pro Package**: Non-linear per-subskill BKT mastery (`app/services/student_model.py`) + single on-rails Socratic orchestrator via `app/services/llm_provider.py` (model-agnostic) using declarative 1-tap chips (`No freeform prompt engineering`). Grounded verbatim in `caps-wiki/` Markdown (not RAG) and gated by deterministic `topic_guardrail.py`. The agent must call deterministic generators for question variants—never author questions itself.
5. **Mathematics Modules (`Rules 16–19`)**:
   - SymPy-backed deterministic generators (`random.Random(seed)`) emitting canonical solution graphs (`from`/`to` in LaTeX + `srepr`, `op`, `rule`, `common_errors`).
   - KaTeX rendering (`MathText.jsx`) with South African comma decimal separator `{,}`.
   - Bidirectional JSON `diagram_spec` -> `DiagramRenderer.jsx` / `GeoGebraGeometryRenderer.jsx` and `ProcedureTracker` (`app/services/procedure_tracker.py`) awarding method marks `[M]` and consequential accuracy `[CA]`.
6. **6-Pillar Generator Contract & Zero-Meta-Curriculum Law (`Rules 20–26b` — see `caps-generator-contract/SKILL.md`)**:
   - Every generator must emit: (1) `term` (`1..4`), `caps_weight_percent`, `suggested_duration_mins`, (2) `mode="compound" | "elementary_<subskill>"`, (3) snake_case `misconception_tags`, (4) teacher-editable `marking_schema`, (5) deterministic 3-tier `hints`, and (6) native modality schema.
   - **Zero-Meta-Curriculum Invariant (`Rule 26b`)**: Never ask administrative policy questions or include phrases like *"According to CAPS/ATP..."*. Test pure subject matter problems only. Verify AST purity via `python caps-ai-backend/scripts/lint_purity.py`.
7. **Direct Engineering Standard (`Rule 27`)**: Work directly on source files and verify via terminal commands. Do not delegate code writing to artificial subagent personas (except invoking `image-generator` for Approach A visual plates).
8. **Hourly Check, GitHub Sync & Dual Redeployment (`Rule 28`)**: Automated hourly pipeline (`python scripts/hourly_sync_deploy.py` / `.github/workflows/hourly_sync_deploy.yml`) checks git status, runs `generate_architecture_html.py`, `lint_purity.py`, and `npm run build`, commits/pushes to `origin/main`, deploys frontend (`npx firebase deploy --only hosting`), and deploys backend (`python caps-ai-backend/deploy_hf.py`).
