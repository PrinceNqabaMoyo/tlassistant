---
description: Modularize the Grade 10 Final Accounts generator safely while preserving current behavior and keeping every resulting file under 1800 lines.
---

# Grade 10 Final Accounts Modularization Workflow

## Goal

Modularize `caps-ai-backend/app/utils/grade10_accounting/term2/final_accounts_generator.py` without losing any of the current Final Accounts and Year-end Adjustments coverage, especially the recently expanded reversal-linked and integrated mini-project families.

The modularized end state must place all generator-related files inside a dedicated package folder at `caps-ai-backend/app/utils/grade10_accounting/term2/final_accounts_generator/` so the `term2` directory does not become cluttered with many sibling files.

## Hard constraints

1. Keep every resulting Python file under `1800` lines.
2. Preserve the current runtime behavior and payload shapes.
3. Keep the stable public import surface under `final_accounts_generator`, with the final public entrypoint provided by `final_accounts_generator/__init__.py`.
4. Do not delete or weaken any reversal family, validation rule, routing rule, or integrated mini-project that already exists.
5. Do not do the refactor as one giant patch.
6. Run verification after each meaningful extraction step.

## Refactor target structure

Use responsibility-based modules inside `caps-ai-backend/app/utils/grade10_accounting/term2/final_accounts_generator/`.

### Target files

- `final_accounts_generator/__init__.py`
  - thin facade and stable import surface
  - high-level orchestration only

- `final_accounts_generator/shared.py`
  - shared helpers
  - cell builders
  - table builders
  - common formatting, money, rounding, ID, and prompt helpers

- `final_accounts_generator/validation.py`
  - scenario validation logic
  - helper validators
  - family-specific validation branches

- `final_accounts_generator/reversal_families.py`
  - accrued income reversal families
  - accrued expenses reversal families
  - prepaid expenses reversal families
  - income received in advance reversal families
  - linked practicals, PATB carry-through, and integrated mini-projects

- `final_accounts_generator/core_families.py`
  - non-reversal practical builders
  - depreciation
  - adjustments
  - asset register
  - final-account fill families
  - trial balance related practical families that are not part of the reversal-specific module

- `final_accounts_generator/integrated_families.py`
  - integrated non-reversal multipart project builders
  - any larger multipart practical families that should stay together

- `final_accounts_generator/dispatch.py` if needed
  - extract routing and pool assembly only if dispatch remains too large after the other moves

### Packaging note

- During the transition, the existing `final_accounts_generator.py` file may temporarily remain in place while code is being moved.
- The final intended state is a dedicated `final_accounts_generator/` package directory with `__init__.py` as the public entrypoint.
- Preserve the import path expected by callers when completing the cutover.

## Required protection baseline

Before each major extraction phase, preserve a regression baseline.

### Minimum checks

- `python -m py_compile caps-ai-backend/app/utils/grade10_accounting/term2/final_accounts_generator.py`
- focused smoke checks for dedicated reversal subskills
- mixed-pool checks for `reversals`
- confirmation that `final_account_table` still includes both simple carry-through items and integrated mini-projects
- confirmation that scenario validation metadata still matches the extracted families

### Behavior that must not regress

- question payload structure
- question type distribution for dedicated reversal subskills
- scenario validation family names
- integrated reversal mini-project availability
- post-adjustment Trial Balance carry-through availability
- existing frontend-compatible fill-in table fields

## Execution order

Follow these phases in order.

### Phase 1: Freeze the current baseline

1. Confirm runtime tests are complete or at least gather the latest runtime observations.
2. Re-run compile and focused smoke checks.
3. Record any existing fragile areas before moving code.

### Phase 2: Create the package shell and extract shared primitives

Create the `final_accounts_generator/` package folder first so every later extraction lands inside the dedicated directory.

Move the safest shared helpers first into `final_accounts_generator/shared.py`.

#### First extraction candidates

- `_cell`
- `_make_fill_in_table_question`
- money helpers
- rounding helpers
- ID helpers
- repeated generic table and prompt helpers

#### Phase 2 exit criteria

- package folder exists and imports cleanly
- main generator still imports and runs cleanly during transition
- helper signatures remain stable
- no payload shape changes

### Phase 3: Extract validation

Move validation into `final_accounts_generator/validation.py`.

#### Include

- `_validate_final_accounts_question`
- helper functions used only by validation
- family-specific recomputation checks
- reversal mini-project validation branches

#### Phase 3 exit criteria

- all existing validation paths still run
- reversal mini-project validation remains intact
- compile and smoke checks pass

### Phase 4: Extract reversal families as one coherent module

Move all reversal-specific builders into `final_accounts_generator/reversal_families.py`.

#### Keep together

- accrued income reversal builders
- accrued expense reversal builders
- prepaid expense reversal builders
- income received in advance reversal builders
- journal, analysis, ledger, carry-through, PATB, and mini-project families
- reversal-specific pool assembly helpers if they exist

#### Phase 4 exit criteria

- dedicated reversal subskills still generate the same family mix
- `reversals` mixed pool still reaches the new mini-project families
- no reversal family is silently dropped from routing

### Phase 5: Extract non-reversal practical families

Move the remaining practical builders into `final_accounts_generator/core_families.py`.

#### Likely scope

- depreciation practicals
- adjustment journal and analysis families
- asset register families
- simpler final-account fill families
- non-reversal trial balance practical families

#### Phase 5 exit criteria

- non-reversal subskills still generate successfully
- no import-cycle issues appear
- file sizes remain under the limit

### Phase 6: Extract integrated non-reversal multipart builders

Move the broader multipart project builders into `final_accounts_generator/integrated_families.py`.

#### Phase 6 exit criteria

- integrated non-reversal projects still generate
- their validation metadata still matches
- main generator shrinks further without losing the public API

### Phase 7: Cut over to the package entrypoint

Refactor the package entrypoint so `final_accounts_generator/__init__.py` mainly provides:

- stable public imports
- top-level orchestration
- high-level dispatch
- minimal glue logic

If routing is still too large, extract it into `final_accounts_generator/dispatch.py` and re-export as needed from the facade.

#### Phase 7 exit criteria

- `final_accounts_generator/__init__.py` is comfortably below the size limit
- all modularized files live inside the dedicated `final_accounts_generator/` folder
- external callers do not need to change their imports
- the public interface remains stable

### Phase 8: Final cleanup and verification

1. Remove dead helpers and duplicate constants.
2. Standardize imports.
3. Confirm no resulting file exceeds `1800` lines.
4. Run final compile checks.
5. Run final smoke checks across reversal and non-reversal families.
6. Confirm the audit assumptions still match the live generator state.

## Testing cadence during modularization

After each phase above:

1. run compile checks
2. run targeted smoke checks for affected families
3. inspect for circular imports
4. inspect for missing helper imports
5. stop and fix regressions before moving to the next phase

Do not stack multiple extraction phases without verification.

## Non-negotiable safety rules

- Do not rename public entrypoints casually.
- Do not change question JSON shape during the refactor.
- Do not split reversal logic across several files unless one reversal module itself later approaches the line cap.
- Do not mix validation logic back into family-builder files after extracting it.
- Do not let file organization be driven only by line count; organize primarily by responsibility.
- Do not scatter the modularized files across `term2`; keep them inside the dedicated `final_accounts_generator/` package folder.
- Do not overwrite working behavior with speculative cleanup.

## Definition of done

The modularization is complete only when all of the following are true:

- every resulting Python file is under `1800` lines
- the modularized code lives inside the dedicated `final_accounts_generator/` folder
- `final_accounts_generator/__init__.py` remains the stable public entrypoint
- compile checks pass
- reversal mini-projects still generate correctly
- linked reversal families still route correctly
- validation remains intact
- integrated non-reversal projects still work
- no expected family disappears from the generator

## Follow-up after completion

Once modularization is complete and verified, pivot to the next subskill workstream using the modularized structure as the new baseline.
