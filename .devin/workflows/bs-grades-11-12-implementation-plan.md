---
description: Step-by-step implementation plan for rolling out question format enhancements, adaptive progression, and agentic tutoring to Grade 11 & 12 Business Studies.
---

# BS Grades 11 & 12 — Implementation Plan

## Recommendation: Infrastructure First, Then Grade Rollout

Build the shared question-format infrastructure **first** (Phases 0–2). Once the backend and frontend support all six question types, roll out **Grades 11 & 12** (Phases 3–4) with adaptive progression and the agent enabled from day one. This prevents wiring a shallow MCQ-only system into G11/G12 and then retrofitting new formats later.

---

## Phase 0 — Reusable Infrastructure (All Grades)

**Goal:** Add the missing question formats to the shared Business Studies layer so every grade can use them.

### 0.1 Backend: `_bs_common.py`

- Add `make_wordbank(pool, blanks, correct_map)`
- Add `make_matching(column_a, column_b, correct_pairs)`
- Add `make_crossword(words, clues, grid_size)`
- Add `make_essay(prompt, rubric, min_words, max_words)`
- Ensure each builder returns a deterministic, serializable JSON payload.

### 0.2 Backend: `grade10_business_studies.py` (mark endpoint)

- Extend the `/mark` handler to recognise:
  - `word_bank` → exact string match per blank
  - `matching_columns` → exact pair match
  - `crossword` → exact cell character match
  - `essay` → rubric keyword matching + structural checks
- Keep deterministic marking (no LLM required).

### 0.3 Frontend: Shared BS Renderers

- Reuse `WordBankQuestionUI` for `word_bank` (minor CSS tweaks for BS colour theme).
- Create `BSMatchingColumns` component (drag or click-to-pair).
- Create `BSCrosswordGrid` component (click-to-type, auto-check on word complete).
- Extend `BSGenericPractice` and `BSGenericScaffold` to route `question_type` to the correct renderer.

### 0.4 Frontend: Essay Renderer

- Long textarea with word-count display.
- Planning panel (intro / body / conclusion hints) toggled by a button.
- Rubric display shown after marking.

---

## Phase 1 — Question Format Taxonomy & Section-Based Progression (Grade 10 First)

**Goal:** Replace the current `subskill = question_format` pattern with a real curriculum progression.

### 1.1 Backend: Section Parser

- Create `parse_md_sections(md_path)` that reads a Grade 10 BS `.md` file and returns a list of sections (e.g., `Understanding business functions`, `The eight business functions`, `Management tasks`).
- Each section maps to a recommended set of formats:
  - **Concept-heavy sections** → MCQ + Word Bank
  - **Definition-heavy sections** → Matching Columns + Crossword
  - **Application sections** → Semantic short answers
  - **Synthesis sections** → Essay

### 1.2 Backend: Dynamic Scaffold Steps

- Replace `DEFAULT_SCAFFOLD_STEPS` in `createGrade10BSController.js` with a backend endpoint `/api/business-studies/grade10/sections`.
- The frontend fetches steps dynamically per topic.
- Each step no longer says `concepts` or `discussion`; it says the section name and carries a `formats` array.

### 1.3 Frontend: Drop the Subskill Dropdown

- In `WorkspaceModeShell`, hide or remove the subskill `<select>` for BS topics.
- Progression is driven by the scaffold step index, not by a user-selected format.

---

## Phase 2 — Memo Animation & UX Polish

**Goal:** Make the memo reveal feel responsive and satisfying.

### 2.1 Word Bank / Matching Memo Animation

- In `WordBankQuestionUI`, add CSS transitions (`transition-all duration-500`) on the pill positions.
- When `readOnly=true` (memo shown), animate each word pill to its `correctMap` blank position.

### 2.2 Crossword Memo Animation

- Fade incorrect letters to red, fade correct letters to green over 300ms.
- Auto-scroll to the first incorrect cell.

### 2.3 Essay Memo Display

- Show the rubric with ticks/crosses per criterion.
- Highlight missing keywords in the student’s text.

---

## Phase 3 — Grade 11 & 12 Backend (Adaptive + Agent)

**Goal:** Bring G11 and G12 BS online with the same backend patterns used for Grade 10.

### 3.1 Create G11 & G12 Backend Modules

- `app/utils/grade11_business_studies/`
- `app/utils/grade12_business_studies/`
- Each folder contains:
  - `_bs_common.py` (can be a symlink or shared import from G10)
  - `term_1/`, `term_2/`, `term_3/` topic generators
  - One `.md` file per topic in `caps-wiki/business-studies/grade-11/` and `grade-12/`

### 3.2 Register API Endpoints

- Add `grade11_business_studies.py` blueprint:
  - `POST /api/business-studies/grade11/generate`
  - `POST /api/business-studies/grade11/mark`
  - `GET /api/business-studies/grade11/sections`
- Add `grade12_business_studies.py` blueprint with identical routes (`/grade12/...`).
- Register both in `app/__init__.py`.

### 3.3 Wire Adaptive Progression

- Reuse the existing `StudentModel` and `adaptive_progression.py` helpers.
- Add `PROGRESSION_MAP` entries for G11 and G12 BS topics.
- Ensure the `mark` endpoints for G11/G12 return:
  - `total_score`, `max_score`
  - `recommendations` (next section, harder format, revision)
  - `progression` (`continue`, `step_back`, `repeat`)

### 3.4 Wire the Agent

- Register G11 and G12 BS topics in `TopicGuardrail._load_allowed_links`.
- Add `get_student_history` support for `grade11_business_studies` and `grade12_business_studies`.
- Ensure the agent can answer free-form questions on G11/G12 content by indexing the `.md` files.

---

## Phase 4 — Grade 11 & 12 Frontend

**Goal:** Mirror the Grade 10 frontend structure for G11 and G12.

### 4.1 Folder Structure

```
src/components/workspace/grade11/business-studies/
├── shared/
│   ├── createGrade11BSController.js
│   ├── createGrade11BSRoute.jsx
│   ├── BSGenericPractice.jsx   (reuse G10 shared, or import)
│   ├── BSGenericScaffold.jsx   (reuse G10 shared)
│   └── ...
├── term-1/
│   ├── topic-a/
│   │   ├── controller.js
│   │   ├── Grade11BSTopicAScaffold.jsx
│   │   └── Grade11BSTopicAPractice.jsx
│   └── ...
```

### 4.2 Route Registration in `App.jsx`

- Add G11 BS routes:
  - `grade11_bs_topic_a_scaffold`
  - `grade11_bs_topic_a_practice`
- Add G12 BS routes (identical pattern).
- Use the same `WorkspaceModeShell` wrapper so the UI is consistent.

### 4.3 Marking Hook

- Create `useGrade11BusinessStudiesMarking.js` and `useGrade12BusinessStudiesMarking.js`.
- Each calls the correct `/grade11/` or `/grade12/` endpoint but otherwise shares logic with G10.

---

## Phase 5 — Data Seeding & QA

### 5.1 Curriculum `.md` Files

- Ensure every G11 and G12 BS topic has a corresponding `.md` in `caps-wiki/business-studies/grade-11/` and `grade-12/`.
- Follow the same heading structure (`## Section Name`) so the section parser works.

### 5.2 Generator Content

- Populate deterministic question pools for each topic.
- Aim for at least 20 MCQ variants, 10 word banks, 5 matching sets, and 3 essay prompts per topic for launch.

### 5.3 Smoke Tests

- Run each question type end-to-end (generate → render → answer → mark → memo) for one topic per grade.
- Verify Firestore writes to `solved_freeform_problems` and `struggling_problems`.

---

## Order of Execution

| Step | What | Why |
|------|------|-----|
| 1 | **Phase 0** — New question formats (backend + frontend shared) | Infrastructure every grade needs |
| 2 | **Phase 1** — Section-based progression (Grade 10) | Proves the progression model before scaling |
| 3 | **Phase 2** — Memo animations & UX polish | Student-facing polish before launch |
| 4 | **Phase 3** — G11 & G12 backend (endpoints, adaptive, agent) | Backend is grade-agnostic once formats exist |
| 5 | **Phase 4** — G11 & G12 frontend (routes, components, hooks) | Frontend mirrors G10 with new endpoints |
| 6 | **Phase 5** — Content seeding & QA | Final data population and testing |

---

## Key Decisions

- **One shared `_bs_common.py`** across G10/G11/G12. Do not duplicate.
- **One shared set of BS frontend components** (`BSGenericPractice`, `BSGenericScaffold`). Grade-specific wrappers only change the API endpoint.
- **Adaptive progression runs on Firestore**, not on the LLM. It works even when the LLM is offline.
- **Agent support is optional at runtime** because all marking is deterministic. Agent is a Pro-tier add-on, not a hard dependency.
