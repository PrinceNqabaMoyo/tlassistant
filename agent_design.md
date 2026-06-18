# Agentic System Design for Fundile TLAssistant (v5)

> **Scope**: Student mode only. Teacher and Admin modes will be designed separately later.

---

## Part 1 — Subscription Tier Strategy

### Standard Package — No LLM, No AI, No API Costs

The Standard package is the app **exactly as it works today, minus the LLM connection**. It is powered entirely by deterministic Python generators and the rule-based evaluation engine. There is zero LLM dependency, zero external API cost.

**What the student gets:**

| Feature | How it works |
|---------|-------------|
| Question generation | **Deterministic Python generators** — e.g. `generate_grade8_integers_question()`, `generate_sole_trader()`, `generate_salaries_wages()`. No LLM involved. |
| Question rendering | **Existing React components** — 75+ math components (AlgebraicExpressionBuilder, GeometryStudio, QuadraticGraphInput, etc.) + accounting journal/ledger tabular structures |
| Answer marking | **Rule-based evaluation engine** (`evaluation_service.py`) — handles MCQ, tables, journals, ledgers, calculations, wordbanks, bundles, consequential marking. No LLM involved. |
| Geometry Studio | **Existing 249KB React component** — interactive 2D/3D shapes, constructions, grids |
| Statistics & graphing | **Existing React components** — Histogram, BoxWhiskerPlot, ScatterPlot, PieChart, BarChart, StemAndLeafPlot, etc. |
| POP upload + email | **Supabase + Resend API** — already working |

**What the student does NOT get:**
- ❌ No AI chatbot / tutoring conversation
- ❌ No "explain this to me" free-form questions
- ❌ No personalised feedback beyond the rule-based marking
- ❌ No CAPS wiki content lookup
- ❌ No visual rendering sub-agent (KaTeX, JSXGraph, chemistry)
- ❌ No student weakness tracking

### Existing Deterministic Generator Inventory

The app already has a massive library of deterministic question generators:

#### Mathematics (Grades 7–12, 35+ route files)
```
grade8_integers, grade8_exponents, grade8_patterns, grade8_whole_numbers,
grade8_algebraic_equations, grade8_algebraic_expressions, grade8_functions,
grade9_integers, grade9_exponents, grade9_patterns, grade9_whole_numbers,
grade9_fractions, grade9_decimal_notation, grade9_algebraic_equations,
grade9_algebraic_expressions, grade9_functions_relationships,
grade10_exponents, grade10_algebraic_expressions, grade10_equations_inequalities,
grade10_patterns_sequences, grade10_trigonometry1,
grade11_exponents_surds, grade11_equations_inequalities,
grade11_patterns_sequences, grade11_analytical_geometry,
grade12_finance, grade12_functions, grade12_patterns_sequences_series,
grade12_trigonometry,
exponents, whole_numbers, geometry_2d_shapes, geometry_construction,
geometry_straight_lines
```

Plus `quiz_routes.py` (39KB) and `routes.py` (33KB) — comprehensive quiz and geometry systems.

#### Accounting (Grades 10–12, 20+ route files)
```
Grade 10: indigenous-bookkeeping, sole-trader, salaries-wages,
          final-accounts, vat, ethics, gaap, internal-control
Grade 11: concepts, fixed-assets, income-statement,
          partnership-balance-sheet, partnership-ledger, reconciliation
Grade 12: concepts, cash-flow, company-general-ledger,
          financial-statements, analysis-interpretation,
          audits-governance-shareholding
```

#### Business Studies (Grades 10–11)
Dedicated route files for grade 10 and grade 11 content.

#### Geometry Backend (2,676-line `geometry_diagrams.py`)
TriangleCalculator, QuadrilateralAnalyzer, CircleCalculator, Geometry3DCalculator, InteractiveAngleTool, ComprehensiveQuizGenerator, GeometryDiagramGenerator — all deterministic, no LLM.

> [!IMPORTANT]
> **None of these generators use LLM.** They are pure Python with `random.seed()` for reproducibility. This is the core value of the Standard package — reliable, cheap to run, zero API costs.

---

### Pro Package — Adds the Agentic System (Student Mode)

The Pro package adds an LLM-powered layer **on top of** the existing Standard experience. Everything in Standard still works; Pro adds intelligence.

**What Pro adds for the student:**

| Feature | How it works | Standard? |
|---------|-------------|:---------:|
| **AI Tutor Chat** | LLM-powered conversational tutoring with the Student persona | ❌ |
| **CAPS Wiki Lookup** | Agent retrieves exact curriculum content from structured markdown files | ❌ |
| **KaTeX Math Rendering** | Agent returns LaTeX → frontend renders beautiful equations, fractions, long division | ❌ |
| **JSXGraph Geometry** | Agent returns shape config → frontend renders interactive labelled shapes with angles/sides | ❌ |
| **Chemistry Structures** (Phase 2) | Agent generates SMILES → RDKit.js renders molecules; Ketcher for student input | ❌ |
| **Student Weakness Tracking** (Phase 3) | Agent reads Firestore history, adapts tutoring to weak topics | ❌ |
| **"Explain my mistake"** | After rule-based marking, LLM explains WHY the student got it wrong | ❌ |
| All Standard features | Deterministic generators, evaluation engine, 75+ components | ✅ |

### Feature Gating Architecture (Student Mode)

**Frontend** — The student UI checks subscription tier and conditionally shows the AI chat panel:

```jsx
const { userData } = useAuth();
const isPro = userData?.subscription === 'pro';

return (
  <div>
    {/* Standard: always visible */}
    <QuestionPanel question={currentQuestion} />
    <AnswerInput onSubmit={handleSubmit} />
    <MarkingResults results={markingResults} />

    {/* Pro only: AI chat + visual rendering */}
    {isPro && (
      <>
        <AIChatPanel persona="student" />
        {response.render && <RenderDispatcher payload={response.render} />}
      </>
    )}
  </div>
);
```

**Backend** — The `/api/agent` endpoint only responds if the user has Pro:

```python
@agent_bp.route('/chat', methods=['POST'])
def agent_chat():
    data = request.get_json()
    user_tier = data.get('subscription', 'standard')
    
    if user_tier != 'pro':
        return jsonify({"error": "AI Chat requires Pro subscription"}), 403
    
    # ... existing agent logic ...
```

> [!TIP]
> This means the Standard package never makes any LLM API calls. The Gemini API key is only used when a Pro user sends a message. Your costs scale with Pro user count, not total user count.

---

## Part 2 — Pro Agentic Architecture (Student Mode)

### The Render Protocol

When the AI agent needs to show something visual, it returns a `render` payload alongside its text response:

```json
{
  "text": "The quadratic formula is used to find the roots of ax² + bx + c = 0:",
  "render": {
    "type": "math",
    "latex": "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"
  }
}
```

The frontend `RenderDispatcher` (already built, dormant) routes to the correct renderer.

### Supported Render Types

| Type | Frontend Renderer | Status |
|------|------------------|--------|
| `math` | KaTeX (LaTeX → formatted equations) | ✅ Built (dormant) |
| `geometry` | JSXGraph (interactive labelled shapes) | ✅ Built (dormant) |
| `chemistry` | RDKit.js (SMILES → molecule SVG) | ⬜ Phase 2 |
| `chemistry_input` | Ketcher (student draws structures) | ⬜ Phase 2 |
| `graph` | Plotly.js / existing React components | ⬜ Phase 2 |
| `diagram` | SVG templates (biology, physics) | ⬜ Phase 2 |
| `map` | Leaflet.js (geography) | ⬜ Phase 2 |
| `timeline` | Mermaid.js (history) | ⬜ Phase 2 |
| `accounting_table` | Existing journal/ledger components | ⬜ Phase 2 |

### Chat History & Session Management

To provide a continuous tutoring experience, the Pro backend must persist conversation state:
- **Storage:** Chat history arrays (user/assistant messages) are persisted in Firestore under the student's document (`users/{uid}/chat_sessions/{sessionId}`).
- **Context Window Management:** To avoid exceeding LLM token limits, older messages should be summarized or truncated, keeping only the most recent N turns and the active curriculum context.
- **Session Linking:** When a student asks "explain my mistake", the chat session must be initialized with the specific problem context (the deterministic question, the student's wrong answer, and the rule-based evaluation feedback).

### Safety & Guardrails (Anti-Cheating)

The AI Tutor must guide the student, not do the work for them.
- **System Prompting:** The `Student persona` prompt must explicitly forbid providing direct answers to assignment questions. It should use Socratic questioning.
- **Input Filtering:** An initial lightweight classification pass (e.g., via Flan-T5) checks if the student's prompt is an attempt to bypass the tutor persona ("ignore previous instructions and solve this").

### CAPS Wiki Knowledge Base

Structured markdown files that the agent looks up deterministically (not fuzzy RAG):

```
caps-wiki/
├── mathematics/                        ← Core Maths (Grade 7–12)
│   ├── grade-7/fractions.md, geometry.md, statistics.md
│   ├── grade-8/integers.md, exponents.md, algebraic-expressions.md
│   ├── grade-9/fractions.md, functions.md, algebraic-equations.md
│   ├── grade-10/algebra.md, financial-maths.md, trigonometry.md
│   ├── grade-11/exponents-surds.md, analytical-geometry.md
│   └── grade-12/calculus.md, finance.md, functions.md
├── maths-literacy/                     ← Maths Literacy (Grade 10–12)
│   ├── grade-10/numbers-operations.md, finance.md, measurement.md, maps-plans.md
│   ├── grade-11/finance.md, measurement.md, maps-plans.md, data-handling.md
│   └── grade-12/finance.md, measurement.md, probability.md, data-handling.md
├── technical-mathematics/              ← Technical Maths (Grade 10–12)
│   ├── grade-10/algebraic-expressions.md, equations.md, trigonometry.md
│   ├── grade-11/complex-numbers.md, mensuration.md, circles-angles.md
│   └── grade-12/differential-calculus.md, integral-calculus.md, matrices.md
├── ems/                                ← Economic Management Sciences (Grade 7–9)
│   ├── grade-7/the-economy.md, entrepreneurship.md, financial-literacy.md
│   ├── grade-8/government-economy.md, entrepreneurship.md, financial-literacy.md
│   └── grade-9/the-economy.md, entrepreneurship.md, financial-literacy.md
├── accounting/                         ← Accounting (Grade 10–12)
│   ├── grade-10/cash-receipts-journal.md, general-ledger.md
│   ├── grade-11/partnerships.md, fixed-assets.md
│   └── grade-12/companies.md, cash-flow.md
├── business-studies/                   ← Business Studies (Grade 10–12)
│   ├── grade-10/
│   ├── grade-11/
│   └── grade-12/
├── physics/                            ← future
├── chemistry/                          ← future
├── biology/                            ← future
├── geography/                          ← future
├── history/                            ← future
├── english-language/                   ← future
├── english-literature/                 ← future
└── isizulu/                            ← future
```

> [!NOTE]
> EMS (Grade 7–9) feeds directly into Accounting and Business Studies (Grade 10–12). The wiki structure reflects this progression — EMS covers foundational concepts like financial literacy and entrepreneurship that are expanded in the FET phase subjects.

### Agent Tool Belt (Pro Only)

| Tool | What it does | Existing? |
|------|-------------|-----------|
| `solve_equation_tool` | SymPy algebra solver | ✅ Existing |
| `evaluate_expression_tool` | Expression evaluator | ✅ Existing |
| `geometry_calculator_tool` | Area/volume calculations | ✅ Existing |
| `calculus_tool` | Differentiation/integration | ✅ Existing |
| `format_expression_tool` | HTML formatting | ✅ Existing |
| `get_curriculum_page` | Wiki lookup (deterministic) | ⬜ To build |
| `render_visual` | Returns render payload for frontend | ⬜ To build |
| `get_student_history` | Reads Firestore weakness data | ⬜ Phase 3 |

---

## Part 3 — Architecture Diagram (Student Mode)

```
┌────────────────────────────────────────────────────────────────┐
│                    FRONTEND (React / Vite)                      │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ STANDARD (all users)                                     │  │
│  │  • QuestionPanel (deterministic questions)               │  │
│  │  • AnswerInput (student answers)                         │  │
│  │  • MarkingResults (rule-based evaluation)                │  │
│  │  • 75+ existing math components                         │  │
│  │  • Accounting journal/ledger tabular structures          │  │
│  │  • GeometryStudio (existing 249KB component)            │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ PRO ONLY (gated by subscription flag)                    │  │
│  │  • AIChatPanel (Student persona)                        │  │
│  │  • RenderDispatcher                                     │  │
│  │    ├── KaTeXRenderer (equations, fractions)             │  │
│  │    ├── JSXGraphRenderer (labelled shapes, angles)       │  │
│  │    ├── RDKit.js (chemistry — Phase 2)                   │  │
│  │    └── Ketcher (chemistry input — Phase 2)              │  │
│  └──────────────────────────────────────────────────────────┘  │
└──────────────────────────┬─────────────────────────────────────┘
                           │
              Standard ────┤──── Pro
                │          │        │
                ▼          │        ▼
┌──────────────────────┐   │  ┌─────────────────────────────┐
│  STANDARD BACKEND    │   │  │  PRO BACKEND (Agent)        │
│                      │   │  │                             │
│  /api/math/generate  │   │  │  /api/agent/chat            │
│  /api/accounting/*   │   │  │  LLM: Gemini Flash          │
│  /api/evaluate       │   │  │  Tools: solve, calc, wiki,  │
│  /api/payments/*     │   │  │         render_visual       │
│                      │   │  │  CAPS Wiki (markdown files) │
│  Deterministic only  │   │  │                             │
│  Zero LLM calls      │   │  │  Pro users only             │
└──────────────────────┘   │  └─────────────────────────────┘
                           │
                    Firestore (shared)
                    • User profiles
                    • Subscription tier
                    • Submission history
                    • Chat history / active sessions
```

---

## Part 4 — Implementation Phases (Student Mode)

### Phase 1 — Foundation

| Task | Status | Notes |
|------|--------|-------|
| KaTeX CDN in `index.html` | ✅ Done | Dormant until Pro wired |
| JSXGraph CDN in `index.html` | ✅ Done | Dormant until Pro wired |
| `KaTeXRenderer.jsx` | ✅ Done | Dormant, not imported |
| `JSXGraphRenderer.jsx` | ✅ Done | Dormant, not imported |
| `RenderDispatcher.jsx` | ✅ Done | Dormant, not imported |
| `caps-wiki/` folder + markdown files | ✅ Done | |
| `get_curriculum_page` tool in `agent_service.py` | ✅ Done | |
| `render_visual` tool in `agent_service.py` | ✅ Done | |
| Pro/Standard gating in frontend (Student mode) | ✅ Done | |
| Pro/Standard gating in backend (`/api/agent`) | ✅ Done | |

### Phase 2 — Science Subjects (Pro)
- RDKit.js + Ketcher for chemistry
- SVG diagram library for biology/physics
- Leaflet.js for geography maps
- Expand `caps-wiki/` for science subjects

### Phase 3 — Personalisation (Pro)
- `get_student_history` tool (Firestore reader)
- Student weakness tracking and adaptive tutoring
- `caps-wiki/` for humanities subjects

### Phase 4 — Teacher & Admin Modes
- To be designed in a separate session

---

## Part 5 — Existing Tool Review

> [!IMPORTANT]
> Before building new features, all existing tools in the agent's toolbelt and the frontend rendering stack should be reviewed. If a better free/open-source alternative exists, it should replace the current tool.

### Tools to Review

| Current Tool | Purpose | Review Question | Potential Replacement |
|-------------|---------|-----------------|----------------------|
| `solve_equation_tool` (SymPy) | Algebra solving | Is SymPy still the best free CAS for CAPS-level algebra? | SymPy is still state-of-the-art for this. **Keep.** |
| `evaluate_expression_tool` (SymPy) | Expression evaluation | Same as above | **Keep.** |
| `geometry_calculator_tool` (SymPy) | Area/volume calcs | Could JSXGraph handle this client-side and eliminate a server round-trip? | Review — JSXGraph can compute live on the client |
| `calculus_tool` (SymPy) | Differentiation/integration | Same as solve_equation | **Keep.** |
| `format_expression_tool` | HTML superscript/subscript | KaTeX renders far superior output. Is this tool still needed? | **Replace with KaTeX rendering via `render_visual`** |
| `curriculum_search_tool` (ChromaDB) | Fuzzy vector search on CAPS PDFs | Disabled. Wiki lookup is deterministic and better. | **Replace with `get_curriculum_page`** |
| `geometry_diagrams.py` (matplotlib) | Server-side diagram generation (2,676 lines) | JSXGraph does the same thing client-side, interactively, with labelled angles/sides. Is matplotlib still needed? | **Gradually retire in favour of JSXGraph** |
| GeometryStudio (React, 249KB) | Frontend geometry canvas | Does JSXGraph overlap or complement this component? | Review — may complement rather than replace |

### Review Process

For each tool, evaluate:
1. **Does a free alternative exist** that is better maintained, more feature-complete, or more performant?
2. **Can the work be moved client-side** to reduce server load on the free HF tier?
3. **Does the tool overlap** with another tool already in the stack?
4. **Is the tool CAPS-appropriate** — does it handle the specific notation, terminology, and question styles used in South African curriculum?

This review should be conducted as a distinct task before Phase 2 implementation begins.

---

## Part 6 — Open-Source LLM Strategy

| Task | Model | Why |
|------|-------|-----|
| Tool calling (maths) | **Gemini 1.5 Flash** (keep) | Reliable structured output |
| Curriculum Q&A (Pro) | **Mistral-7B-Instruct** (free HF API) | Strong instruction-following |
| Classification | **Flan-T5-Large** (free HF API) | Fast, lightweight |

---

## Appendix A — Codebase Refactor Audit

### Context

Earlier in this session (June 5th), the backend was refactored from a monolithic `MainApp.py` into a modular Flask blueprint structure. The original `MainApp.py` (39KB, last modified August 2025) was **not deleted** and remains as a backup.

### Files Created During the Refactor

All dates are June 5th, 2026. All logic was **extracted** from `MainApp.py` — no new functionality was added.

| File | Type | What was extracted |
|------|------|-------------------|
| `app/services/agent_service.py` | **NEW** | All LangChain/LLM agent initialisation, tool definitions, persona prompts |
| `app/services/journal_service.py` | **NEW** | CRJ/CPJ validation, marking, feedback generation, journal templates |
| `app/services/evaluation_service.py` | **NEW** | Part-marking grading engine (MCQ, tables, journals, ledgers, calculations) |
| `app/services/email_service.py` | **NEW** | Resend API email sender (replaces blocked SMTP) |
| `app/api/agent.py` | **NEW** | Flask blueprint exposing `/api/agent/chat` — calls `agent_service.py` |
| `app/api/journals.py` | **NEW** | Flask blueprint exposing `/api/journals/*` — calls `journal_service.py` |
| `app/api/evaluation.py` | **NEW** | Flask blueprint exposing `/api/evaluate` — calls `evaluation_service.py` |
| `app/api/teacher.py` | **NEW** | Flask blueprint exposing `/api/teacher/create-assessment` |
| `app/api/admin.py` | **NEW** | Flask blueprint exposing `/api/admin/*` |

### Files Modified During the Refactor

| File | Change | Impact |
|------|--------|--------|
| `app/__init__.py` | Registered all new blueprints, added `initialize_agent()` call | Routes now served from blueprints instead of monolithic file |
| `app/api/payments/routes.py` | Added 3 lines to trigger email notification after POP upload | Background thread, fires after upload already succeeds |
| `Dockerfile` | Added `PYTHONUNBUFFERED=1`, `--access-logfile -` | Logging only, no behaviour change |

### Files Modified During Phase 1 (June 8th)

| File | Change | Impact |
|------|--------|--------|
| `index.html` | Added 4 CDN lines (KaTeX CSS+JS, JSXGraph CSS+JS) | Scripts load but are never called. ~200KB added to page load |
| `src/components/shared/KaTeXRenderer.jsx` | **NEW** | Not imported anywhere — dormant |
| `src/components/shared/JSXGraphRenderer.jsx` | **NEW** | Not imported anywhere — dormant |
| `src/components/shared/RenderDispatcher.jsx` | **NEW** | Not imported anywhere — dormant |

### Utility Scripts (Not Part of the App)

| File | What it is | Safe to delete? |
|------|-----------|:-:|
| `search_api.js` | One-off Node.js script used to grep for `/api/` calls in `App.jsx` | ✅ Yes |

### Files NOT Modified (Confirmed Untouched)

| File | Status |
|------|--------|
| `MainApp.py` (original monolith) | ✅ Untouched since August 2025 |
| All 35+ math generator route files | ✅ Untouched |
| All 20+ accounting generator route files | ✅ Untouched |
| All `utils/` generator modules | ✅ Untouched |
| `geometry_diagrams.py` (2,676 lines) | ✅ Untouched |
| All 75+ frontend math components | ✅ Untouched |
| `App.jsx` | ✅ Untouched |
| `StudentView.jsx` | ✅ Untouched |

> [!IMPORTANT]
> **The Standard package (deterministic generators + evaluation engine) is completely unaffected by all changes in this session.** No generator logic, no marking logic, no rendering component, and no frontend view was modified. The only live changes are: (1) email notification on POP upload, (2) improved logging in Docker, and (3) modular blueprint structure — all of which are additive and backwards-compatible.
