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

---

1. **Always Build Full-Stack**: When tasked with building a new module or feature (like EMS), you MUST implement both the backend logic (generators, endpoints) AND the frontend React UI (Scaffold, Practice, and Assessment modes). Do not stop at the backend.
2. **Engine Contract as the Gold Standard (Not Tabular UI)**: Accounting Grade 10/11 is the architectural gold standard for the *Backend Contract* (deterministic seed generation, solution graphs, error taxonomy with misconception tags, and 3-tier pre-baked hints). However, do NOT force its 2D tabular UI onto non-tabular subjects. Render each subject in its native cognitive modality:
   - Accounting/EMS: 2D ledger & journal tables with cell-level coordinate marking.
   - Mathematics: Stepwise symbolic derivations (SymPy line transitions + KaTeX working pad).
   - Business Studies: Rubric-based semantic points with keyword & concept matching.
   - Geometry: Spatial declarative visualisations (JSXGraph/Mafs).
2b. **Examining Body Branding & Legal Policy**: Never use proprietary examining body trademarks (IEB, SACAI, DBE, NSC) in student/parent marketing, UI copy, or landing pages. Use universal, public-domain curriculum alignment statements instead:
   - "100% Aligned with South African Curriculum Standards (CAPS)"
   - "Authentic Grade 8–12 Exam-Standard Questions & Marking Rubrics"
   - "Trusted preparation for public, private, and independent school examinations nationwide"
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

11b. **Curriculum Source Documents for Generator Creation (Priority & Pacing)**
    - When creating or refining question generators, always consult the curriculum source documents:
      - `curriculum_docs_auto/` takes **primary priority** for pacing, authentic exam mark allocations, term weighting, and diagram vision annotations.
      - It must be used **in conjunction with** the manually typed `curriculum_docs/` files to ensure comprehensive conceptual depth, teacher notes, and syllabus completeness.
      - Together, these documents serve as the authoritative curricular ground truth from which all deterministic generators are created and calibrated.

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

26. **Curriculum Source Precedence (Authoring Generators)**
    - When authoring question archetypes, learning objectives, marking schemas, and worked solutions, refer to both curriculum document trees:
      - `curriculum_docs_auto/` takes priority for authentic exam marks, time pacing, term scheduling, and diagram annotations.
      - Use in conjunction with manually typed `curriculum_docs/` for syllabus completeness, conceptual depth, and teacher notes.

26b. **Zero-Meta-Curriculum Invariant & Exam Paper Authenticity Standard**
    - **Absolute Negative Constraint**: Students in tests and exams are tested on **subject concepts, procedures, calculations, and analytical problem-solving**—NEVER on administrative policy or curriculum bureaucracy.
    - Questions, prompts, options, and worked solutions must NEVER contain phrases such as:
      - `"According to the CAPS curriculum / document / guidelines..."`
      - `"As required by CAPS / ATP / DBE..."`
      - `"Review the foundational rules according to official requirements..."`
      - Questions asking which term a topic is taught in or what percentage weighting is allocated to a topic.
    - Every question must directly mimic an authentic high school test or national examination paper (DBE/IEB standard) with realistic scenarios, concrete numbers, formulas, or accounting ledgers.
    - When extracting from curriculum documents, adversarially strip all teacher notes, pacing comments, and administrative policy text.

27. **Specialized Custom Subagents & Autonomous Delegation**
    - The repository maintains 17 persistent specialist configurations in `.agents/agents/`:
      - Systems & Engine Specialists:
        - `generator_architect.json`: 6-pillar deterministic Python/SymPy generators, AST purity, CC <= 12, horizontal and vertical slicing, Zero-Meta-Curriculum Invariant.
        - `curriculum_specialist.json`: CAPS syllabus, pacing, diagnostic calibration (beta 0.3, 0.6, 0.85), coverage completeness audits, zero-trademark policy, cross-grade spiral maps, zero-meta policy.
        - `question_appropriateness_specialist.json`: Exam authenticity and question appropriateness auditor. Enforces the Zero-Meta-Curriculum Invariant across all generators, static fallback banks, and challenges.
        - `cognitive_ui_engineer.json`: React 18/Vite cognitive modalities (KaTeX, JSXGraph, 2D ledgers), mobile-first 44px touch targets, full-viewport mobile layouts, file size < 2000 lines, brand visual consistency (#13519C brand blue, #FF9100 brand orange, bg-slate-50 canvas).
        - `eval_triage_architect.json`: Memory-Decayed BKT (P(L, dt)), post-exam triage 3-step repair, PDF memos, cross-grade spiral adaptive regression.
        - `systems_security_architect.json`: Socket pooling, query projections, SymPy thread sandboxing (2.5s timeout), POPIA Sec 35, token budgets, and operational cost governance.
        - `architecture_governor.json`: Manifest synchronization (Rule 0a-0c), quarterly SOTA stack audits, and generate_architecture_html.py.
        - `learning_journey_architect.json`: End-to-end pedagogical progression harmony (Diagnostic -> Scaffold -> Practice -> Assessment -> Prerequisite Regression), ungameable gamification (XP, streaks, 4-tier badges), cognitive pacing circuit breakers, and mastery thresholds.
        - `agentic_orchestrator_architect.json`: Pro tier Socratic conversational tutor, orchestrator tool belt, declarative suggestion chips taxonomy, topic guardrail, regex solution-leak shields, frustration circuit breakers, and provider abstraction.
        - `qa_test_architect.json`: End-to-end testing strategy, large-scale Monte Carlo generator seed determinism, responsive viewport validation, procedure tracker precision, and offline telemetry buffer testing.
      - Stakeholder Persona Specialists (UX, Ergonomics & Market Strategy):
        - `learner_ux_specialist.json`: Student psychology, distraction-free light workspaces, 3-tier progression pacing (Scaffold -> Practice -> Assessment), procedure tracker visual feedback, and ungameable gamification.
        - `teacher_cockpit_designer.json`: Educator ergonomics, D2L Brightspace-style humanized student rosters with real photo upload support, 3-click friction-free exam and memo authoring, rubric customization without code, and 1-click targeted micro-fix assignments.
        - `parent_bridge_marketer.json`: Parental trust, anxiety reduction, zero-nagging weekly Sunday WhatsApp pulse summaries, actionable coaching recommendations, transparent data savings marketing (< 2MB vs 450MB), and accessible home communication.
        - `school_admin_strategist.json`: School leadership administration, class roster creation, custom term mark collation and weightings (SASAMS alignment), Annual Teaching Plan (ATP) curriculum pacing heatmaps, grade-wide misconception remediation broadcasts, and POPIA child privacy governance.
      - Subject Pedagogy Specialists (Lead Subject Examiners):
        - `math_sciences_specialist.json`: Mathematics, Technical Mathematics, Mathematical Literacy (Grades 7–12) — procedural calculation purity, SA comma decimals, method marks [M] and consequential accuracy [CA], MathKeypad completeness, and Grade 12->7 prerequisite lineage.
        - `commercial_sciences_specialist.json`: EMS (7–9), Accounting (10–12), Business Studies (10–12) — 2D ledger coordinate marking, Accounting Equation columns, 15% VAT, and business legislation rubrics.
        - `sciences_domain_specialist.json`: Natural Sciences (7–9), Physical Sciences (10–12), Life Sciences (10–12) — CAPS Data Sheet equations, mandatory SI units, vector directions, balanced chemical equations, and biological diagram accuracy.
    - **In any conversation:** When the user requests work in one of these domains, or references an agent by name, the main agent must either adopt that specialist's strict invariants directly or register and invoke the subagent via `define_subagent` / `invoke_subagent` using the corresponding `.agents/agents/*.json` configuration.

28. **Mandatory Specialist Agent Routing Protocol (Enforced Delegation Pipeline)**
    - The main agent must NEVER attempt ad-hoc shortcuts or bypass specialized subagents when implementing tasks across distinct architectural domains.
    - **Enforced Task-to-Agent Delegation Matrix:**
      1. **Frontend React UI, Mobile Viewports & Ergonomics:** MUST be delegated to `cognitive_ui_engineer` (React 18, Vite, mobile touch targets, landscape/portrait workspace maximization, skeuo-modern folder tabs, cognitive modalities).
      2. **Learner Journey & Psychology:** MUST be delegated to `learner_ux_specialist` (dashboard layouts, emotional safety of looping, distraction-free workspaces).
      3. **Backend Question Generators:** MUST be delegated to `generator_architect` + Domain Specialist (`math_sciences_specialist`, `commercial_sciences_specialist`, `sciences_domain_specialist`).
      4. **End-to-End QA, Testing & Viewport Verification:** MUST be delegated to `qa_test_architect` (Vite production builds, Monte Carlo determinism, DOM/chassis validation).
      5. **Curriculum Pacing, Term Calibration & Alignment:** MUST be delegated to `curriculum_specialist`.
      6. **Architecture Manifest & Rule 0 Governance:** MUST be delegated to `architecture_governor`.
    - **Execution Mandate:**
      - Whenever a user task involves mobile UI, React layout refactoring, or cognitive modalities, the main agent MUST invoke `cognitive_ui_engineer` to perform the changes and verify fidelity against prototypes before presenting to the user.
      - Any QA or verification check MUST be executed or validated by `qa_test_architect`.
      - This protocol is non-negotiable and guarantees absolute consistency across the development pipeline.
    - **Agent Creation & Modification Governance (Explicit Permission Required):**
      - For any task requiring the creation of a **new specialist agent** or the **modification of an existing agent** (its definition, system prompt, capabilities, or tooling in `.agents/agents/*.json`), the assistant MUST explicitly ask the user for permission first before executing the modification or creating the agent.
      - Never unilaterally alter an existing agent's architecture, tools, or configuration, nor define new agent types without prior explicit user consent.

29. **Continuous Hourly Check, GitHub Sync & Dual Redeployment Protocol**
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



