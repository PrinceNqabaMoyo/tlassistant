# General Development Rules

## Architecture Manifest — Read First, Update Always

0a. **SESSION START — Read the architecture manifest:** Before writing any code, read
    `fundile-architecture.json` in full. It is the single source of truth for what is built,
    what is planned, and what the system constraints are. Do not ask the owner to explain
    the architecture — it is in that file. The `_workflow` block inside it contains your
    exact maintenance instructions.

0b. **DURING SESSION — Keep the manifest current:** Whenever you build, partially build,
    or change the status of any layer, service, API route, frontend component, Firestore
    collection, or generator — update `fundile-architecture.json` immediately:
    - Move items from `planned` arrays to `built` arrays when complete.
    - Change `"status": "planned"` to `"status": "partial"` or `"status": "built"`.
    - Update `"lastUpdated"` to today's date.
    - Add new open questions to `openQuestions` if they arise.
    - Remove resolved open questions from `openQuestions`.

0c. **SESSION END — Regenerate the HTML:** After all code changes and before ending the
    session, run from the project root:
    ```
    python generate_architecture_html.py
    ```
    This regenerates `fundile-architecture.html` from the updated JSON. Always run this last.
    Never edit `fundile-architecture.html` directly — it is a generated file.

0d. **ZERO-THEATER & ANTI-SHODDY ENGINEERING INVARIANT (MANDATORY LAW)**:
    - **0d-1. No Theatrical Testing ("Hollywood Pattern")**: Never write fake test actions, cosmetic HUD banners, simulated progress countdowns, or screenplay scripts that do not interact with live, real application components. Every test step must execute the genuine end-to-end user movement (real authentication, real form submissions, real database state changes, real navigation). Console logs must only report verified post-assertion states, never theatrical pre-action narration.
    - **0d-2. Strict Identity & Privilege Isolation (The Super Admin Law)**: The Super Admin / Owner is strictly the authentic platform owner (restricted to verified owner emails in `firestore.rules`: `princenqaba@gmail.com`, `princenqabamoyo@outlook.com`). The Super Admin is NEVER a mock persona (`MOCK_SUPER_ADMIN`), NEVER simulated with URL query parameters (`?persona=admin`), and NEVER seeded from mock classroom rosters. School Admin and classroom stakeholders may use mock environments for class roster simulation; Super Admin governance, clearance, and security must use authentic authentication and valid Firebase ID tokens.
    - **0d-3. Role-State Decoupling Invariant**: Administrative and educator components must NEVER read or display state from `studentStore` unless explicitly querying a student's record for academic oversight. Header avatars, profile modals, and settings for administrators must derive identity strictly from the authenticated admin user profile, never defaulting to mock learner state (e.g. "Nqobile Dlamini").
    - **0d-4. Source-Code Grounding Invariant (Zero Phantom Selectors)**: An agent is strictly forbidden from writing or modifying a locator, test ID, or action in an E2E spec without first viewing the exact target component source file in `src/`. Every selector must have its exact presence in the live JSX confirmed before appearing in a test spec. Hallucinating, guessing, or writing from memory is strictly considered a defect.
    - **0d-5. Genuine End-to-End Actions (No Backdoor Scripting Substitution)**: In an E2E test, database helper scripts are ONLY permitted for pre-test clean-slate setup (e.g. purging test accounts before the test begins). Database scripts must NEVER substitute for the actual user actions being tested. If a test narrative states "Super Admin reviews and approves the payment", the Super Admin window MUST navigate the UI, open the uploaded POP file via the authentic signed URL endpoint, verify the reference, and click the on-screen approval button. No backdoors.
    - **0d-6. Zero Silent Skips in E2E**: NEVER wrap critical test steps in `if (await isVisible())`, `if (count > 0)`, or empty `catch` blocks. Test steps must use explicit assertions (`await expect(locator).toBeVisible({ timeout: ... })` or `await expect(locator).toBeEnabled()`) so that if a selector, button, modal, or backend fails, the test halts and fails loudly. Silent skipping is strictly considered a defect.
    - **0d-7. Runtime Execution Verification & Viewport Non-Interference**: Never claim code, features, or tests work solely based on `npm run build` or static lint checks. Building is not executing. You must run the actual scripts/tests, inspect the live runtime output, and confirm all steps succeeded before reporting completion. Test instrumentation (cursors, pause buttons, test helpers) must NEVER occupy header, top-bar, or primary action zones (must stay in non-interactive canvas margins like `bottom: 16px; left: 16px`) and must never intercept pointer events directed at application components. Local development (`http://localhost:5173` / `http://localhost:5001`) is the default test environment to protect production data from pollution.
    - **0d-8. Holistic Cross-Spec & Pre-Flight Audit Invariant (Anti-Whack-A-Mole Law)**: Never conclude a debugging turn or code modification by fixing only a single isolated failure line. In a Vite SPA, syntax errors in downstream components or omissions in shared utilities (`autopilotHud.js`, `studentStore.js`, `schoolEnrollmentService.js`, `playwright.config.js`) will invisibly break upstream pages or sibling test specs. Before declaring any fix complete, you MUST execute the holistic pre-flight gate (`npm run test:audit`), asserting:
      1. Mechanical E2E purity: 0 selector or privilege violations across all 13 specs (`python scripts/audit_e2e_specs.py`).
      2. Zero cross-spec syntax/export breakage: 0 errors across all 12 test specs (`npx playwright test --list`).
      3. Live browser connectivity: Clean, unblocked DOM mount in < 2 seconds on `127.0.0.1:5173` with 0 console errors (`node scripts/smoke_check.js`).
    - **0d-9. Responsive Visibility & CSS Union Invariant (The Anti-Hidden Selector Law)**: When targeting interactive components that exist in both mobile and desktop viewports, locators MUST strictly filter by `:visible` across all union clauses (e.g. `[data-testid="btn"]:visible, button:has-text("..."):visible`), and never append a trailing non-`:visible` fallback (e.g. `..., [data-testid="btn"]`) with `.first()`. In document-order evaluation, this causes Playwright to select the hidden desktop DOM node when running in a mobile viewport, resulting in `Received: hidden` failure.
    - **0d-10. Multi-Card Clearance Desk Scoping Invariant**: On administrative management desks containing repeating card lists (such as EFT Payment Approvals), action triggers and post-action verification assertions MUST strictly scope to the specific card container:
      `locator('div[data-testid^="payment-card-"]:has([data-testid="payment-email-${email}"])')`.
      Never use global `.first()` action locators or global text matchers (`text=approved`), which falsely match filter tabs or neighboring records.
    - **0d-11. Resilient Profile Upsert & Authentic Banking Receipt Law**: Institutional workflows and approval handlers in `AdminForms.jsx` and `SchoolAdminView.jsx` must use `setDoc(ref, data, { merge: true })` instead of throwing or assuming client documents are pre-materialized. All E2E verification must utilize authentic, vector-compliant South African banking receipts (Access Bank letterhead, double-ring audit stamps, PASA disclosures) rather than plain-text stubs.
    - **0d-12. Systematic Cross-Grade & Cross-Subject Generalization Invariant (The Anti-Silo / Anti-Whack-A-Mole Law)**: Whenever a defect, UX inconsistency, or engine limitation is identified in one grade or subject (e.g. Grade 10 Mathematics), the agent is strictly forbidden from applying a localized fix solely to that specific instance. The agent MUST systematically audit all grades (Senior Phase Grades 7–9 and FET Phase Grades 10–12) and all subjects (Mathematics, Accounting, Physical Sciences, Life Sciences, Business Studies, Technical Mathematics, Mathematical Literacy, EMS, Natural Sciences) to eradicate the architectural root cause across the entire platform. Zero localized patching; zero whack-a-mole engineering.

---

1. **Always Build Full-Stack**: When tasked with building a new module or feature (like EMS), you MUST implement both the backend logic (generators, endpoints) AND the frontend React UI (Scaffold, Practice, and Assessment modes). Do not stop at the backend.
2. **Engine Contract as the Gold Standard (Not Tabular UI)**: Accounting Grade 10/11 is the architectural gold standard for the *Backend Contract* (deterministic seed generation, solution graphs, error taxonomy with misconception tags, and 3-tier pre-baked hints). However, do NOT force its 2D tabular UI onto non-tabular subjects. Render each subject in its native cognitive modality:
   - Accounting/EMS: 2D ledger & journal tables with cell-level coordinate marking.
   - Mathematics: Stepwise symbolic derivations (SymPy line transitions + KaTeX working pad).
   - Business Studies: Rubric-based semantic points with keyword & concept matching.
   - Geometry: Spatial declarative visualisations (JSXGraph/Mafs).
2b. **Examining Body Branding, Legal Policy & Zero "CAPS" in South African UI Law (Permanent Memory Invariant)**:
   - **Zero "CAPS" Acronym in UI / Marketing**: The South African UI, marketing copy, landing pages, memoranda, student dashboards, and parent/teacher-facing interfaces must NEVER reference or display the acronym or term "CAPS". In South Africa, there is a widespread misconception that "CAPS" refers solely to the public/government school curriculum. Advertising or displaying "CAPS" creates resistance among private schools, independent examination candidates (IEB/SACAI), and homeschoolers.
   - **Universal Alignment Language Only**: Always use neutral, universal, public-domain curriculum alignment statements instead:
     - "100% Aligned with South African National Curriculum Standards"
     - "Authentic Grade 7–12 Exam-Standard Questions & Marking Rubrics"
     - "Trusted preparation for public, private, and independent school examinations nationwide"
     - "National Curriculum Statements / Standards"
   - **Examining Body Trademarks**: Never use proprietary examining body trademarks (IEB, SACAI, DBE, NSC) as brand endorsements or product claims in student/parent marketing, UI copy, or landing pages.
3. **Follow the Hint System**: You must strictly adhere to the hint architecture defined in `hint_system_specification.md` (rich cell-level hints for tabular data, 3-tier hints for non-tabular data). Always read that file before implementing new generators or UI components.
4. **File Size Limit**: No file should exceed 2000 lines of code. Modularization must be implemented to keep files focused and maintainable. This is especially important for backend generators which can become huge.

## Application Tiers: Standard vs. Pro

### Adaptive Progression (How the Student Advances)

5. **Standard Package (Rule-Based / Linear — 100% Deterministic & Zero-LLM)**
   - Students move through Scaffold → Practice → Assessment in a fixed order.
   - Progression is unlocked by hardcoded score thresholds (e.g., 60% to leave Scaffold, 80% to unlock Assessment).
   - All subskills are treated equally. On failure, the student reattempts more deterministic questions from the same pool.
   - **Zero LLM calls are made**: question generation, answer calculation, procedure tracking, marking, and progression decisions are 100% deterministic Python code. Zero token cost.

6. **Pro Package (AI-Driven / Non-Linear)**
   - The system continuously tracks per-subskill mastery using metadata already emitted by generators (`learning_objective_id`, `misconception_tags`, `diagnostic_tags`, `minimum_mastery_score`, `keywords`).
   - If a student struggles with a specific subskill (e.g., "Calculating depreciation"), the system dynamically generates targeted micro-lessons and isomorphic practice questions for that subskill before allowing advancement.
   - The agent can request the generator to produce variants by changing context, numbers, or wording while keeping the same archetype and learning objective.
   - All progression decisions are reproducible and auditable: they are based on the shared student model, not an opaque LLM.

### Agentic System (How the AI Assists the Student)

7. **No Freeform Chat / No Prompt-Driven Interfaces**: Legacy freeform chat is deprecated and forbidden. The interface is strictly declarative, visual, and clickable:
   - For Teachers & Students: Select subject, select topic(s), enter marks/question count, click "Generate".
   - Never force users to 'prompt engineer' questions, assessments, or feedback.
   - The LLM has zero authority over calculation, answer truth, or question authoring.

8. **Standard Package (Zero-LLM Static Generation System)**
   - The backend deterministic generator produces the question, sample answer, marking schema, and all 3 tiers of hints *ahead of time* using pure Python / SymPy. Zero LLM cost.
   - The frontend reveals pre-computed hints when the student clicks a hint button.
   - There is no live chat conversation. All assistance is deterministic and pre-baked.

9. **Pro Package (Live Socratic Tutor — Small / Local LLM Layer)**
   - A single orchestrator agent with a tool belt handles all tutoring interactions.
   - The agent receives the current question context, the student's partial answer, and the shared student model.
   - It responds with a short text answer and, when needed, a `render` payload for visual components (KaTeX, JSXGraph, accounting tables, etc.).
   - The agent is strictly on-rails. The frontend should expose clickable suggestion chips for allowed prompts (e.g., "Explain the hint", "Show me another example", "Why is this wrong?"), but the student can also type a topic-bound question.
   - The agent must not write its own questions; it must call the deterministic generator when it needs a variant.

## LLM Provider Abstraction

10. **Model-Agnostic Layer**
    - The backend must not depend on a single provider. All LLM calls go through a thin provider abstraction (`app/services/llm_provider.py`).
    - The default implementation targets the **Hugging Face Inference API** so that open-source models (e.g., Gemma) can be used on the free tier.
    - Swapping to Gemini, self-hosted Gemma, or another endpoint is a configuration change only.
    - Keep prompts and tool definitions provider-agnostic; do not hardcode provider-specific response formats.

## Grounding: CAPS Wiki & Curriculum Source Documents

11. **Deterministic Context, Not RAG**
    - The agent is grounded by reading the relevant `caps-wiki/` Markdown file directly.
    - The agent prompt includes the current topic's wiki content verbatim; there is no vector retrieval or embedding search.
    - Wiki files are structured as Markdown with optional YAML frontmatter. They are compatible with the Open Knowledge Format (OKF) idea: a portable, human-readable knowledge bundle for the agent.
    - Syllabi and per-topic guidance live in `caps-wiki/{subject}/{grade}/{topic}.md`.

11b. **Curriculum Source Documents for Generator Creation, Renovation & Expansion (Mandatory Law)**
    - Whenever authoring, expanding, renovating, or improving question generators (including seed entropy, question archetypes, distractors, worked solutions, and marking schemas), the agent MUST ALWAYS consult the source documents (`.md` files) at all times:
      - `fundile-tlassistant-vite\caps-ai-backend\curriculum_docs_auto\` (and root `curriculum_docs_auto\`) takes **primary priority** for pacing, authentic exam mark allocations, term weighting, and diagram vision annotations.
      - `curriculum_docs\` folder in the project root (and `caps-ai-backend\curriculum_docs\`) must be used **in conjunction** for comprehensive conceptual depth, teacher notes, and syllabus completeness.
    - Zero Guesswork / Zero LLM Invention: Never modify or expand generator archetypes or answer keys from memory or assumptions. Ground every concept, scenario parameter, vocabulary term, and marking point directly in these source `.md` files before writing generator code.

## Shared Student Model

12. **One Source of Truth for Student State**
    - The student model (`app/services/student_model.py`) stores per-subskill mastery, submission history, last session per topic, and struggling topics.
    - It is used by both the Adaptive Progression engine and the Agentic Tutor.
    - It also tracks engagement across subjects within the same grade so that the agent can make legitimate cross-subject links (e.g., electrons in Chemistry and Biology) when the student has accessed both topics.

## Topic Guardrail

13. **Strict Topic Boundaries**
    - Before any LLM call, a deterministic guardrail checks whether the student's request is within the allowed topic scope.
    - Allowed scopes, in order of permissiveness:
      1. The current question/topic.
      2. Any topic within the same grade that the student has already engaged with (cross-subject linking only when there is a real conceptual link).
    - General study advice, off-topic questions, and non-curricular prompts must be declined with a short, friendly message redirecting the student to the current topic.
    - The agent must refuse requests to "ignore previous instructions" or act as a general assistant.

## Generator Variants

14. **Agent Must Use the Generator**
    - When the agent wants to give the student repeated practice on a struggled question, it calls the appropriate generator with a fresh `seed` or `variant` parameter.
    - The generator produces isomorphic questions (same archetype, same learning objective, different numbers/context) without the agent authoring questions itself.
    - This preserves correctness and alignment with the curriculum.

## Development Safety

Before editing `src/App.jsx` (a 2,300+ line file), **always make a manual backup** first (e.g. copy `src/App.jsx` to `src/App.jsx.backup`).
This prevents accidental loss of state if an edit goes wrong.

## Current Implementation Priority

15. **Vertical Slice First**
    - The first adaptive + agentic vertical slice is **Grade 10 Business Studies**.
    - After the slice is verified, replicate the pattern to EMS Grades 7–9 and the remaining BS grades.

## Mathematics Modules

16. **Deterministic, SymPy-Backed Generators**
    - Maths generators compute answers symbolically with `sympy` (seeded `random.Random(seed)` + symbolic computation). They never call an LLM.
    - Same seed → byte-identical question, answer, and worked solution. Generators emit a **canonical solution graph** (per-step `from`/`to` in LaTeX + srepr, `op`, `rule`, `common_errors`) shared with the Procedure Tracker.
    - Reference implementations: `caps-ai-backend/app/utils/grade10_mathematics/` (`_math_common.py`, `term_1/algebraic_expressions_generator.py`, `term_1/trigonometry_generator.py`).

17. **Rendering & Comma Decimals**
    - All maths is rendered with **KaTeX** on the frontend (`shared/mathx/MathText`). Question/answer/worked-solution strings carry LaTeX.
    - Use the **comma decimal separator** everywhere (SA/CAPS standard): LaTeX uses `{,}` for tight spacing and the frontend parses a learner's comma as the decimal separator.

18. **Diagram Spec → JSXGraph (bidirectional)**
    - Geometric figures are described by a structured **Diagram Spec** (JSON: `kind`, `points`, `sides`, `angles`, `right_angle_at`, labels), built by `_diagram.py` and rendered by `shared/mathx/DiagramRenderer.jsx` via **JSXGraph** — never hand-drawn image assets.
    - The same edge-key vocabulary (e.g. `"AB"`, `"BC"`, `"AC"`) travels in two directions: render (spec → figure) and mark (learner's selected edge → string compare to `correct_edge`). The `diagram_select` question type marks clicks deterministically (no pixels). The serialized spec is also the descriptive parameter the Pro agent reads to reason about a figure.

19. **Procedure Tracker + Maths Keypad**
    - Step-by-step working is marked by the **Procedure Tracker** (`app/services/procedure_tracker.py`): it parses each line, checks SymPy equivalence per transition, localises the FIRST error and classifies it from `common_errors`, and awards NSC-style method marks + an accuracy mark with carry-over. It is a tool on the one orchestrator, not a separate agent.
    - The **Working Pad** (`shared/mathx/WorkingPad`) is integrated from the start; for diagram questions the answer area embeds the interactive canvas.
    - The maths keypad is registry-driven: it inherits Algebra keys and grows per topic (Trig adds `sin`/`cos`/`tan`, `θ`, degree `°`). Each key carries a LaTeX label + a SymPy-parseable insert token.

## Generator Architecture Contract (Universal Across All Subjects & Grades)

All new question generators and refactored existing generators MUST implement this 6-pillar contract to remain compatible with the Calendar Exam Engine, the Post-Exam Triage Report, the Teacher LMS Cockpit, and Adaptive Deconstruction:

20. **Term & Calendar Metadata (Powers Exam-on-Demand)**
    - Every generator and archetype payload must declare:
      - `term`: integer (`1`, `2`, `3`, or `4`) reflecting the South African curriculum term.
      - `caps_weight_percent`: integer (approximate weighting in CAPS exams).
      - `suggested_duration_mins`: integer.
    - The calendar engine uses this to strictly enforce `term <= selected_term` so students in Term 2 are never given Term 3/4 content.

21. **Deconstructibility & Atomic Micro-Drills (Powers Adaptive Regression)**
    - Generators must not only emit monolithic compound questions (e.g. an entire 12-mark CRJ or full Quadratic derivation).
    - Every compound generator must support decomposing into its atomic constituent sub-drills via a parameter like `mode="compound" | "elementary_<subskill>"`:
      - *Accounting:* Isolate *just* the VAT calculation or *just* the Contra Account selection.
      - *Mathematics:* Isolate *just* finding factor pairs or *just* common factor extraction.
    - When a student fails a compound question twice, the engine calls the generator in elementary mode to rebuild the prerequisite schema.

22. **Standardized Misconception Taxonomy (Powers Post-Exam Triage)**
    - Every generator must tag predictable failure modes with clean, snake_case `misconception_tags`:
      - *Accounting:* `net_vs_gross_confusion`, `debit_credit_inversion`, `omitted_balance_b_d`.
      - *Mathematics:* `sign_error_distribution`, `forgot_pm_square_root`, `reciprocal_confusion`.
      - *Business Studies:* `macro_vs_market_confusion`, `omitted_legislation_impact`.
    - The Post-Exam Triage Engine aggregates these tags across a mock exam to tell the student: *"You lost 16 marks purely due to net_vs_gross_confusion. Click here for a 5-minute fix."*

23. **Teacher-Editable Marking Schema (Powers the LMS Cockpit)**
    - Every question must emit a structured `marking_schema` block:
      ```python
      "marking_schema": {
          "total_marks": 12,
          "marking_points": [
              {"id": "mp_1", "desc": "Transaction date", "marks": 1, "editable": True},
              {"id": "mp_2", "desc": "Bank gross amount (incl. VAT)", "marks": 3, "editable": True}
          ],
          "deductions": [
              {"rule": "must_be_empty_filled", "penalty": -1}
          ],
          "carry_forward_rule": "consequential_accuracy"
      }
      ```
    - This allows teachers in the LMS cockpit to adjust mark distributions and rubric text without modifying Python code.

24. **Deterministic 3-Tier Pre-Baked Hints (Zero LLM Cost)**
    - All three tiers of hints must be pre-calculated deterministically ahead of time:
      - **Tier 1 (Location / Nudge):** Directs attention to the specific cell or line.
      - **Tier 2 (Directional Rule):** States the underlying conceptual rule to apply.
      - **Tier 3 (Worked Step Calculation):** Provides the exact calculated step with numbers.
    - No LLM calls are made when a student requests a hint in Standard mode.

25. **Modality-Appropriate Representation**
    - Generators must format output for their native cognitive modality:
      - *Accounting & EMS:* 2D tabular schemas with cell coordinates and strict cell types (`required`, `given`, `must_be_empty`).
      - *Mathematics:* LaTeX KaTeX strings, SymPy canonical solution graphs, and South African comma decimal separator normalization (`_decomma`).
      - *Business Studies:* Rubric bullet points + concept match definitions from `caps-wiki`.

26. **Curriculum Source Precedence (Authoring, Renovating & Expanding Generators)**
    - When authoring, renovating, or expanding question archetypes, learning objectives, marking schemas, and worked solutions, agents must consult both curriculum document trees at all times:
      - `fundile-tlassistant-vite\caps-ai-backend\curriculum_docs_auto\` (and root `curriculum_docs_auto\`) takes **primary priority** for authentic exam marks, time pacing, term scheduling, and diagram annotations.
      - `curriculum_docs\` folder in the project root (and `caps-ai-backend\curriculum_docs\`) must be used **in conjunction** for syllabus completeness, conceptual depth, and teacher notes.
    - No changes or entropy expansions may be made without first viewing the relevant topic markdown files in these folders.

26b. **Zero-Meta-Curriculum Invariant & Exam Paper Authenticity Standard**
    - **Absolute Negative Constraint**: Students in tests and exams are tested on **subject concepts, procedures, calculations, and analytical problem-solving**—NEVER on administrative policy or curriculum bureaucracy.
    - Questions, prompts, options, and worked solutions must NEVER contain phrases such as:
      - `"According to the CAPS curriculum / document / guidelines..."`
      - `"As required by CAPS / ATP / DBE..."`
      - `"Review the foundational rules according to official requirements..."`
      - Questions asking which term a topic is taught in or what percentage weighting is allocated to a topic.
    - Every question must directly mimic an authentic high school test or national examination paper (DBE/IEB standard) with realistic scenarios, concrete numbers, formulas, or accounting ledgers.
    - When extracting from curriculum documents, adversarially strip all teacher notes, pacing comments, and administrative policy text.

27. **Direct Engineering Standard (Zero Subagent Persona Bureaucracy)**
    - Work directly on the codebase: read the exact source files, make grounded edits, and verify immediately via terminal commands.
    - Do not delegate implementation tasks to artificial specialist subagent personas. Subagents are strictly reserved for isolated, read-only research exploration when necessary.

28. **Continuous Hourly Check, GitHub Sync & Dual Redeployment Protocol**
    - The repository maintains an automated hourly cycle to inspect for codebase updates, sync changes to GitHub, and trigger production redeployments across both frontend (Firebase Hosting) and backend (Hugging Face Spaces).
    - **Hourly Execution Pipeline:**
      1. **Change Detection (Every 60 Minutes):**
         - Inspect working tree for local changes (`git status --porcelain`).
         - Check remote tracking branch (`git fetch origin`, compare `HEAD` vs `origin/main`).
         - If zero changes are detected locally and remotely, log heartbeat and exit idle.
      2. **Pre-Deployment Safety & Manifest Synchronization:**
         - If architecture files changed, execute Rule 0c: `python generate_architecture_html.py`.
         - If backend question generators were updated, verify AST purity: `python caps-ai-backend/scripts/lint_purity.py`.
         - If frontend code was updated, verify production bundling: `npm run build`.
      3. **GitHub Repository Synchronization:**
         - Stage all verified updates: `git add .`
         - Commit with an automated timestamp message: `git commit -m "chore(sync): automated hourly code check, verified build & architecture sync [YYYY-MM-DD HH:MM]"`
         - Push updates: `git push origin main`.
      4. **Frontend Production Redeployment (Firebase Hosting):**
         - When changes touch `src/`, `public/`, `index.html`, `vite.config.js`, `package.json`, or `firestore.rules`:
         - Build bundle: `npm run build`.
         - Deploy to Firebase Hosting: `npx firebase deploy --only hosting`.
      5. **Backend Production Redeployment (Hugging Face Spaces):**
         - When changes touch `caps-ai-backend/`:
         - Upload Docker container updates to Hugging Face Spaces (`snombi/tlassistant`): `python caps-ai-backend/deploy_hf.py`.
      6. **Audit & Notification Heartbeat:**
         - Log execution status, commit hash, and deployment URLs in session logs.
    - **Automation Channels:**
      - **Agent / IDE Schedule:** Use Antigravity's `schedule` tool (`CronExpression="0 * * * *"`, `IsDaemon=true`) to run recurring checks in the background.
      - **CLI Runner / Daemon:** Run `python scripts/hourly_sync_deploy.py --daemon` (or `npm run sync:hourly` for a one-off run).
      - **GitHub Actions CI/CD:** Scheduled cron workflow `.github/workflows/hourly_sync_deploy.yml` runs every hour (`0 * * * *`).



