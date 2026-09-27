# Unified Cognitive Workspace & Progression Streamlining Implementation Plan

## Problem Statement & Context
Currently, the Fundile frontend suffers from two major structural issues that cause user confusion and massive technical debt:
1. **Obsolete 3-Mode Progression Selector**: The legacy `Scaffold` $\rightarrow$ `Practice` $\rightarrow$ `Marking/Exam` selector tabs (originating before the adaptive progression and Bayesian Knowledge Tracing engines were built) compete with and contradict the modern adaptive progression model. Scaffolding is a cognitive assistance level that should fade in and out dynamically, not a rigid gate learners must grind through before being permitted to practice.
2. **Combinatorial File Explosion**: Each grade and subject maintains separate scaffold and practice components (e.g. `Grade7ExponentsScaffold.jsx`, `Grade7ExponentsPractice.jsx`, `Grade10AccountingSoleTraderScaffold.jsx`, etc.). Each re-implements its own headers, buttons, mode pills, and layouts. Changes to branding, responsiveness, or interaction semantics require touching dozens of files.

## Architectural Objectives
1. **Eliminate the 3-Mode Selector Everywhere**: Remove `scaffold`, `practice`, and `marking` switcher tabs across all UI layers. Replace with two distinct, intuitive states:
   - **Active Learning & Practice Workspace**: Clean, unhindered problem solving with dynamic, in-situ scaffolding that unfolds only when the learner struggles or requests step-by-step deconstruction.
   - **Assessment Mode**: Timed, full-screen exam conditions unlocking when the Dual-Ring Mastery Dial reaches $\ge 80\%$ (or triggered on demand), concluding with the Post-Exam Diagnostic Autopsy.
2. **Implement `UniversalWorkspace.jsx`**: A single, streamlined workspace shell driven by the backend generator's cognitive modality:
   - `math`: KaTeX math rendering, stepwise working pad, specialized topic `MathKeypad`, and South African comma decimal support.
   - `ledger`: 2D Accounting & EMS tabular grid with cell-level coordinate marking and status constraints.
   - `rubric`: Business Studies concept matcher and keyword taxonomy chips.
   - `diagram`: JSXGraph interactive geometric/circuit/vector visualizations.
3. **Harmonize Navigation & State Machine**: Topic selection cleanly mounts the `UniversalWorkspace` with the active topic, eliminating grade/mode routing mismatches.
4. **Enforce Brand Aesthetics & Mobile-First Invariants**: Strict compliance with `fundile-ui-alternative-design.html` (brand royal blue `#13519C` header ribbon with gold graduation cap, vibrant orange `#FF9100` progress bar and primary CTA, clean white `rounded-2xl` elevation cards, $\ge 44\text{px}$ touch targets, and full-viewport mobile layouts).

---

## Proposed Changes

### 1. Core Shell & Component Architecture

#### [NEW] `src/components/workspace/UniversalWorkspace.jsx`
- **Role**: Single universal workspace component for all grades (7–12) and all subjects.
- **Features**:
  - Sticky top brand ribbon with gold graduation cap, grade/subject pills, and vivid orange topic badge.
  - Thin gradient progress ribbon (`from-brand-orange to-brand-amber`).
  - Problem statement and metadata card.
  - Dynamic modality renderer selector (`MathModalityRenderer`, `LedgerModalityRenderer`, `RubricModalityRenderer`, `DiagramModalityRenderer`).
  - **In-Situ Dynamic Scaffold Drawer**: Expandable step-by-step breakdown that learners can unfold when needed or that automatically suggests deconstruction after consecutive errors, without forcing mode switches.
  - On-brand interactive footer: `Check` (royal blue), `Compare Memo` (blue outline), `Next Question` (vivid orange).
  - Prerequisite Gap Banner: Appears automatically when cross-grade regression is detected by `prerequisite_tree`.
  - Pro Tier Socratic suggestion chips drawer.

#### [MODIFY] `src/components/workspace/shared/WorkspaceModeShell.jsx`
- Deprecate and remove the obsolete 3-mode selector tabs (`scaffold`, `practice`, `marking`).
- Remove `availableModes` and mode routing buttons.
- Align with the simplified `UniversalWorkspace` layout.

#### [MODIFY] `src/views/StudentWorkspaceView.jsx`
- Remove `activeTab` mode switching (`Dashboard` vs `Practice Mode` vs `Curriculum Map`) that conflicts with direct topic engagement.
- Integrate directly with `UniversalWorkspace`.

---

### 2. Workspace Registry Streamlining

#### [MODIFY] `src/components/workspace/workspaceRegistry.js`
- Refactor the registry so curriculum topics map directly to `UniversalWorkspace` with the designated backend generator key, removing the need for duplicate scaffold vs practice component mappings.
- Preserve backward-compatible fallback for existing custom visual aids.

---

### 3. Modality Renderers Consolidation

#### [NEW] `src/components/workspace/modalities/MathModalityRenderer.jsx`
- Renders KaTeX problem statements, dynamic working pad, live KaTeX preview, and integrated `MathKeypad`.

#### [NEW] `src/components/workspace/modalities/LedgerModalityRenderer.jsx`
- Renders 2D accounting journals and ledgers with cell coordinate inputs, debits/credits, and balance calculation.

#### [NEW] `src/components/workspace/modalities/RubricModalityRenderer.jsx`
- Renders Business Studies scenarios, concept keywords, and rubric-matching evaluation.

#### [NEW] `src/components/workspace/modalities/DiagramModalityRenderer.jsx`
- Embeds interactive JSXGraph geometry and science diagrams.

---

### 4. Governance & Build Verification
- Update `fundile-architecture.json` to record the Universal Workspace architecture.
- Run `python generate_architecture_html.py` to regenerate the HTML architecture manifest.
- Run `npm run build` to confirm clean compilation and zero circular chunk errors.

---

## Verification Plan

### Automated Tests & Checks
1. **JSX AST Syntax Validation**:
   - Run `@babel/parser` on all new and modified components to ensure zero syntax or JSX parsing errors.
2. **Vite Production Build**:
   - Execute `npm run build` and ensure exit code 0 with clean asset generation.
3. **Backend Service Health**:
   - Verify that generator payloads pass expected modality parameters (`math`, `ledger`, `rubric`, `diagram`) to `UniversalWorkspace`.

### Manual & Visual Verification
1. **Mode Elimination**: Confirm that the 3-mode selector tabs (`Scaffold`, `Practice`, `Marking`) are completely absent across desktop and mobile views.
2. **Dynamic Scaffolding**: Verify that step-by-step deconstruction can be unfolded in-place during practice without page reloads or mode changes.
3. **Responsive Aesthetics**: Validate that headers, buttons, cards, and keypads conform to `fundile-ui-alternative-design.html` on both mobile (390px) and desktop (1280px+).
