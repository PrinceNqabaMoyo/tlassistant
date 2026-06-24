---
description: Step-by-step implementation plan for modernizing Grade 7-9 EMS with curriculum-driven scaffold progression, new question types, marking endpoints, and adaptive agentic tutoring.
---

# EMS Grades 7-9 Modernization Plan

## Context

EMS (Economic and Management Sciences) at Grades 7-9 is a lower-level combination of Accounting and Business Studies. The current implementation lags behind the Business Studies G10-12 modernization that introduced:

- Curriculum-driven scaffold steps parsed from `.md` files
- Section-based progression with dynamic question format selection
- New question types: `word_bank`, `matching_columns`, `crossword`, `essay`
- `/mark` and `/sections` API endpoints
- Agentic tutoring with adaptive progression

This plan brings EMS G7-9 to parity while respecting the subject's unique blend of financial literacy, economics, and entrepreneurship.

---

## Phase 1 — Foundation: Curriculum Parser & `/sections` Endpoints

### 1.1 Create `_ems_curriculum.py` (per grade)

**Files:**
- `caps-ai-backend/app/utils/grade7_ems/_ems_curriculum.py`
- `caps-ai-backend/app/utils/grade8_ems/_ems_curriculum.py`
- `caps-ai-backend/app/utils/grade9_ems/_ems_curriculum.py`

**Approach:** Re-export `parse_md_sections`, `get_topic_sections`, `_find_md_file` from `app.utils.grade10_business_studies._bs_curriculum`.

**Content per file:**
- `TOPIC_MD_MAP: Dict[str, str]` — map every generator topic key to its curriculum `.md` file path under `curriculum_docs/EMS_Gr{7,8,9}/`
- `get_g{7,8,9}_topic_sections(topic: str)` — wrapper that calls `parse_md_sections` on the mapped file

### 1.2 Map All Curriculum Files

**Grade 7** (11 topics across 3 terms):
```
Term 1: history_of_money, needs_and_wants, goods_and_services, businesses
Term 2: accounting_concepts, income_and_expenses, budgets
Term 3: the_entrepreneur, starting_a_business, entrepreneurs_day, inequality_and_poverty
```

**Grade 8** (12 topics across 3 terms):
```
Term 1: government, national_budget, standard_of_living, accounting_basics, source_documents
Term 2: accounting_cycle, crj_services, factors_of_production, markets
Term 3: crj_trading, cpj, forms_of_ownership
```

**Grade 9** (12 topics across 3 terms):
```
Term 1: crj_cpj_trading, economic_systems, general_ledger_trial_balance, circular_flow
Term 2: debtors_journal_1, price_theory, sectors_of_economy
Term 3: trade_unions, debtors_journal_2, creditors_journal, business_functions
```

### 1.3 Add `/sections` Endpoint to All 3 EMS APIs

**Files:**
- `caps-ai-backend/app/api/grade7_ems.py`
- `caps-ai-backend/app/api/grade8_ems.py`
- `caps-ai-backend/app/api/grade9_ems.py`

**Endpoint:** `GET /sections?topic=<topic_key>`
**Response:** `{ topic: str, steps: [{ key, title, formats }] }`

### 1.4 Add Format-Key Normalization

In each API's `generate_questions()` function, add:
```python
_FORMAT_TO_SUBSKILL = {
    'mcq': 'concepts',
    'word_bank': 'concepts',
    'matching_columns': 'concepts',
    'crossword': 'concepts',
    'typed': 'application',
    'essay': 'discussion',
}
subskill = _FORMAT_TO_SUBSKILL.get(subskill, subskill)
```

**Verification:**
- Run `python -c` to test that `get_g7_topic_sections('grade7_ems_history_of_money')` returns parsed sections.
- Run `python -c` to test that all 31 curriculum `.md` files are reachable via `_find_md_file`.

---

## Phase 2 — Marking & Question Type Enhancement

### 2.1 Add `/mark` Endpoint to All 3 EMS APIs

**Pattern:** Follow `grade10_business_studies.py` `/mark` implementation.

**Files to modify:**
- `caps-ai-backend/app/api/grade7_ems.py`
- `caps-ai-backend/app/api/grade8_ems.py`
- `caps-ai-backend/app/api/grade9_ems.py`

**Required marking logic:**
- `mcq`: exact match on `correct_index`
- `typed`: keyword coverage scoring (same as BS)
- `journal` (tabular): cell-by-cell comparison of `correct_map` against `student_answer`
- `word_bank`: slot-to-word mapping validation
- `matching_columns`: pair validation
- `crossword`: grid cell validation
- `essay`: rubric keyword coverage + concept validation

**Response shape:**
```json
{
  "success": true,
  "score": 8,
  "max_score": 10,
  "percentage": 80,
  "is_correct": false,
  "feedback": "...",
  "progression": { "level_up": false, "next_recommended": "..." },
  "recommendations": [...]
}
```

### 2.2 Extend Generators for New Question Types

For **each** EMS generator, add builder functions using `app.utils.grade10_business_studies._bs_common`:

- `_word_bank_question(rng, item)` — vocabulary matching
- `_matching_columns_question(rng, item)` — concept ↔ definition
- `_crossword_question(rng, item)` — term-based grid
- `_essay_question(rng, item)` — rubric-based written response

**Accounting-based topics** (Gr7 accounting_concepts, Gr8 crj/cpj, Gr9 journals/ledger) should prioritize:
- `matching_columns` for terminology (e.g., debit ↔ credit rules)
- `word_bank` for account names
- `journal` (already exists) for procedural practice

**Economics topics** (Gr7 history_of_money, Gr8 markets, Gr9 economic_systems) should prioritize:
- `mcq` for concept checking
- `essay` for discussion questions
- `crossword` for vocabulary reinforcement

**Verification:**
- Generate 1 question of each new type per grade and inspect JSON structure.
- Ensure `question_type` is correctly set in the output.

---

## Phase 3 — Frontend Modernization

### 3.1 Create/Reuse `useDynamicScaffoldSteps` for EMS

**Option A (Recommended):** Reuse existing hook.

In `src/components/workspace/grade{7,8,9}/ems/shared/`:
```js
export { useDynamicScaffoldSteps } from '../../grade10/business-studies/shared/useDynamicScaffoldSteps';
```

**Update each EMS controller/registry** to:
- Import `useDynamicScaffoldSteps`
- Pass `sectionsEndpoint: '/api/grade{7,8,9}_ems/sections'`
- Replace hardcoded `scaffoldSteps` with dynamically fetched steps

### 3.2 Update Registry Files

**Files:**
- `src/components/workspace/registry/grade7EmsRegistry.js`
- `src/components/workspace/registry/grade8EmsRegistry.js`
- `src/components/workspace/registry/grade9EmsRegistry.js`

**Changes:**
1. Remove hardcoded `steps` arrays from `TOPIC_CONFIGS`
2. Fetch steps dynamically via `useDynamicScaffoldSteps`
3. Add `disableSubskillControl: true` for scaffold-like modes
4. Ensure `workspaceRegistry.js` renders EMS routes correctly

### 3.3 Wire Question Type Renderers

EMS already has `journal` rendering (tabular). Need to add:
- `WordBankQuestionUI` — reuse from `src/components/workspace/shared/`
- `MatchingColumnsUI` — reuse or create
- `BSCrosswordGrid` — reuse from `src/components/workspace/grade10/business-studies/shared/`
- `BSEssayRenderer` — reuse from `src/components/workspace/grade10/business-studies/shared/`

**Marking hooks:**
- Create `useGrade7EmsMarking.js`
- Create `useGrade8EmsMarking.js`
- Create `useGrade9EmsMarking.js`

Each should point to the respective `/mark` endpoint and handle the marking response shape.

**Verification:**
- Load one EMS topic in scaffold mode — verify steps load from backend.
- Load one EMS topic in practice mode — verify question generates and renders.
- Submit an answer — verify `/mark` returns correct score and feedback.

---

## Phase 4 — Missing Topic Generators

### 4.1 Grade 7 Missing Generators (5 new)

| Topic | Curriculum File | Key Concepts |
|---|---|---|
| needs_and_wants | `2-Needs and wants.md` | needs vs wants, scarcity, choices |
| goods_and_services | `3-Goods and services.md` | tangible vs intangible, consumer/producer |
| the_entrepreneur | `8-The entrepreneur.md` | traits, risk-taking, innovation |
| starting_a_business | `9-Starting a business.md` | business plan, resources, steps |
| entrepreneurs_day | `10-Entrepreneur's Day.md` | practical application, marketing |
| inequality_and_poverty | `11-Inequality and poverty.md` | causes, effects, solutions |

### 4.2 Grade 8 Missing Generators (6 new)

| Topic | Curriculum File | Key Concepts |
|---|---|---|
| government | `1-Government.md` | levels of government, roles |
| national_budget | `2-National Budget.md` | revenue, expenditure, deficit/surplus |
| standard_of_living | `3-Standard of living.md` | HDI, quality of life indicators |
| source_documents | `5-Source Documents.md` | types, purpose, information extracted |
| accounting_cycle | `6-The accounting cycle.md` | full cycle from transaction to financial statements |
| factors_of_production | `8-Factors of production.md` | land, labour, capital, entrepreneurship |
| markets | `9-The markets.md` | goods market, financial market, labour market |
| forms_of_ownership | `12-Forms of ownership.md` | sole trader, partnership, company, co-op |

### 4.3 Grade 9 Missing Generators (3 new)

| Topic | Curriculum File | Key Concepts |
|---|---|---|
| circular_flow | `4-The Circular flow.md` | households, firms, government, foreign sector |
| price_theory | `6-Price theory.md` | supply, demand, equilibrium |
| sectors_of_economy | `7-Sectors of the economy.md` | primary, secondary, tertiary |
| trade_unions | `8-Trade unions.md` | roles, collective bargaining, strikes |
| business_functions | `11-Functions of a Business.md` | HR, marketing, operations, finance |

**Pattern for each new generator:**
```python
import random
from app.utils.grade10_business_studies._bs_common import (
    build_mcq, build_typed, build_word_bank, build_matching_columns, build_generate
)

def _concept_pool(rng):
    return [...]

def _application_pool(rng):
    return [...]

def generate(subskill='concepts', difficulty='medium', count=1, seed=None, **kwargs):
    # Use build_generate or custom logic
    ...
```

**Verification:**
- Each generator must produce at least 10 MCQ variants, 5 typed variants.
- Accounting topics must include at least 3 journal-style tabular variants.
- All generators must set correct `curriculum_reference` metadata.

---

## Phase 5 — Adaptive Progression & Agentic Tutoring

### 5.1 Firestore Integration

**On successful marking (> 80%):**
- Write to `solved_freeform_problems` collection with `topic_id`, `subskill`, `timestamp`

**On struggle (< 50% or 3 consecutive incorrect):**
- Write to `struggling_problems` collection
- Trigger adaptive progression: recommend easier subskill or hint level

### 5.2 Agentic Tutoring for Accounting Topics

**Accounting-based topics needing special treatment:**
- Gr7: `accounting_concepts`, `income_and_expenses`, `budgets`
- Gr8: `accounting_basics`, `crj`, `cpj_and_crj`
- Gr9: `crj_cpj`, `general_ledger`, `debtors_journal`, `creditors_journal`, `debtors_ledger`

**Features:**
- Step-by-step hint degradation (3 levels: nudge → concept → breakdown)
- Cell-level hints for journal questions
- Concept reinforcement when accounting equation is violated
- Retry with similar but numerically different transactions

### 5.3 Progress Tracking

**Per student, per topic:**
- Track mastery per section key (from `/sections`)
- Level up when 3 consecutive questions correct at current section
- Recommend next section based on curriculum order

**Verification:**
- Simulate 5 attempts on one topic, verify progression logic.
- Check Firestore writes in Firebase console.
- Verify adaptive hint degradation on journal questions.

---

## File Inventory

### New Files

| File | Phase | Description |
|---|---|---|
| `app/utils/grade7_ems/_ems_curriculum.py` | 1 | Curriculum parser + TOPIC_MD_MAP |
| `app/utils/grade8_ems/_ems_curriculum.py` | 1 | Curriculum parser + TOPIC_MD_MAP |
| `app/utils/grade9_ems/_ems_curriculum.py` | 1 | Curriculum parser + TOPIC_MD_MAP |
| `app/utils/grade7_ems/__init__.py` | 4 | Package init + generator exports |
| `src/components/workspace/grade7/ems/shared/useDynamicScaffoldSteps.js` | 3 | Re-export hook |
| `src/components/workspace/grade7/ems/shared/useGrade7EmsMarking.js` | 3 | Marking hook |
| `src/components/workspace/grade8/ems/shared/useDynamicScaffoldSteps.js` | 3 | Re-export hook |
| `src/components/workspace/grade8/ems/shared/useGrade8EmsMarking.js` | 3 | Marking hook |
| `src/components/workspace/grade9/ems/shared/useDynamicScaffoldSteps.js` | 3 | Re-export hook |
| `src/components/workspace/grade9/ems/shared/useGrade9EmsMarking.js` | 3 | Marking hook |

### Modified Files

| File | Phase | Changes |
|---|---|---|
| `app/api/grade7_ems.py` | 1, 2 | Add `/sections`, `/mark`, format normalization |
| `app/api/grade8_ems.py` | 1, 2 | Add `/sections`, `/mark`, format normalization |
| `app/api/grade9_ems.py` | 1, 2 | Add `/sections`, `/mark`, format normalization |
| `src/components/workspace/registry/grade7EmsRegistry.js` | 3 | Dynamic scaffold steps, disable subskill control |
| `src/components/workspace/registry/grade8EmsRegistry.js` | 3 | Dynamic scaffold steps, disable subskill control |
| `src/components/workspace/registry/grade9EmsRegistry.js` | 3 | Dynamic scaffold steps, disable subskill control |
| `app/__init__.py` | 1 | Ensure all EMS blueprints registered (already done) |

---

## Testing & Verification

### Smoke Tests (per grade)

1. **Sections endpoint:** `GET /api/grade7_ems/sections?topic=grade7_ems_history_of_money`
   - Expect: 200 OK with `steps` array containing parsed headings

2. **Generate endpoint:** `POST /api/grade7_ems/generate`
   - Body: `{ topic: 'grade7_ems_history_of_money', subskills: ['concepts'], difficulty: 'medium', count: 1 }`
   - Expect: 200 OK with question JSON

3. **Mark endpoint:** `POST /api/grade7_ems/mark`
   - Body: `{ question, student_answer }`
   - Expect: 200 OK with score, feedback, progression

4. **Frontend:** Load topic in scaffold mode → steps populate → question renders → submit → feedback shows → memo reveals

### Curriculum Fidelity Checklist

- [ ] Every `.md` file in `EMS_Gr7/` has a corresponding generator
- [ ] Every `.md` file in `EMS_Gr8/` has a corresponding generator
- [ ] Every `.md` file in `EMS_Gr9/` has a corresponding generator
- [ ] `_find_md_file` resolves all paths successfully
- [ ] Section parser extracts meaningful headings (not just "Activity 1")
- [ ] Format inference assigns appropriate question types per section

---

## Launch Criteria

- [ ] All 31 curriculum `.md` files mapped (G7: 11, G8: 12, G9: 12)
- [ ] All 3 grades have `/generate`, `/mark`, `/sections` endpoints
- [ ] At least 20 MCQ variants per topic
- [ ] At least 5 typed/journal variants per accounting topic
- [ ] New question types (word_bank, matching, crossword, essay) present in at least 3 topics per grade
- [ ] Frontend dynamically fetches scaffold steps
- [ ] End-to-end smoke test passes for 1 topic per grade
- [ ] Firestore writes verified for progression tracking

---

## Notes

- **EMS journal questions** (CRJ, CPJ, General Ledger) are unique — they use tabular `question_type: 'journal'` with `correct_map` for cell-by-cell marking. Do NOT convert these to standard MCQ/typed. Instead, enhance the existing journal marking logic.
- **Lower grade sensitivity:** G7-9 students need more scaffolding. Ensure hint sections are verbose and teaching notes are age-appropriate.
- **Accounting equation** is introduced in G7 and builds through G8-G9. Track prerequisite mastery across grades if possible.
