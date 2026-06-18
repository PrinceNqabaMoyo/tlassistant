# Grade 10 Transaction Analysis Validation Plan

## Objective
Resolve the current validation findings for the Grade 10 Sole Trader `equation` subskill by correcting transaction-effect logic, tightening archetype fidelity, improving hint quality, and preserving the existing accounting table UX.

## Validation Inputs Incorporated
Source: `Validation logs.md`

### Confirmed Validation Findings
1. Some generated transaction effects appear to treat Assets and Equity as automatically `±`, which is not always correct.
2. Every transaction/question in `caps-ai-backend/curriculum_docs/Accounting _Gr10/Term 1/gr10Accounting Equation and Transaction analysis archetypes.md` must be reviewed for correctness.
3. The archetype review must produce a report covering transaction nature, payment methods, source documents, and related accounting treatment.
4. That report must then be used to improve the Grade 10 accounting-equation generator.
5. Hints must explain the accounting effect clearly and show calculations where percentages/derived values are involved.

## Current State Snapshot
### First-pass work already completed
- Added multiline transaction-list prompt assembly in `caps-ai-backend/app/utils/grade10_accounting/sole_trader_generator.py`.
- Stopped pre-filling editable accounting-equation cells by default.
- Added first-pass per-cell hint surfacing in `src/components/workspace/grade10/accounting/sole-trader/Grade10AccountingSoleTraderScaffold.jsx`.
- Audited Grade 10-12 accounting Scaffold hint behavior and confirmed Grade 11 and Grade 12 currently rely on question-level hints rather than cell-level table hints.

### Gaps still to close
- Archetype-by-archetype correctness review has not yet been completed.
- The `±` transaction-effect concern needs targeted validation against each archetype and generator mapping.
- Hint content is surfaced in the UI, but the underlying hint language still needs to become more explanatory and calculation-aware.
- Verification/build pass is still pending.

## Authoritative References
- `Validation logs.md`
- `caps-ai-backend/curriculum_docs/Accounting _Gr10/Term 1/gr10Accounting Equation and Transaction analysis archetypes.md`
- `caps-ai-backend/app/utils/grade10_accounting/sole_trader_generator.py`
- `src/components/workspace/grade10/accounting/sole-trader/Grade10AccountingSoleTraderScaffold.jsx`
- `src/components/workspace/grade10/accounting/sole-trader/Grade10AccountingSoleTraderPractice.jsx`
- `sole_trader_refactor_plan.md`

## Primary Files In Scope
### Backend
- `caps-ai-backend/app/utils/grade10_accounting/sole_trader_generator.py`
- `caps-ai-backend/app/api/accounting/grade10_sole_trader_routes.py`

### Frontend
- `src/components/workspace/grade10/accounting/sole-trader/Grade10AccountingSoleTraderScaffold.jsx`
- `src/components/workspace/grade10/accounting/sole-trader/Grade10AccountingSoleTraderPractice.jsx`
- `src/components/workspace/shared/WorkspaceModeShell.jsx`
- `src/components/workspace/registry/grade10Registry.js`
- `src/components/workspace/grade10/accounting/sole-trader/controller.js`

### Validation / Analysis Outputs
- `Gr10Transaction-analysis-validation.md`
- a new archetype audit report file in the project root or another agreed workspace location

## Implementation Strategy

### Phase 1 - Archetype correctness audit
Goal: validate the Grade 10 transaction-analysis source material against accounting rules before widening generator changes.

Actions:
1. Read every transaction/question pattern in `gr10Accounting Equation and Transaction analysis archetypes.md`.
2. Classify each archetype by:
   - transaction nature
   - cash / credit / mixed treatment
   - affected element(s): assets, owner's equity, liabilities
   - whether the effect is increase, decrease, or no effect per element
   - payment method
   - source document(s)
   - whether calculations are required
3. Identify mistakes, ambiguities, or inconsistent accounting treatment in the archetypes.
4. Produce an audit report that records both correct patterns and defects.

Success criteria:
- Every archetype has been reviewed.
- The review clearly distinguishes correct vs incorrect accounting effects.
- We have a usable source-of-truth report for generator correction work.

### Phase 2 - Generator transaction-effect correction
Goal: ensure the generator does not assume invalid `±` behavior for Assets, Equity, or Liabilities.

Actions:
1. Trace how each accounting-equation archetype currently maps to row effects in `sole_trader_generator.py`.
2. Check whether any templates or helper logic incorrectly default to simultaneous add/deduct behavior.
3. Correct each affected template so the generated answer table reflects the true accounting effect for that transaction type.
4. Re-check multi-row transactions to ensure continuation rows do not distort the actual equation impact.

Success criteria:
- Assets, Equity, and Liabilities only change where the archetype truly requires it.
- No generated transaction implies a false paired increase/decrease pattern.
- Multi-row table structure remains valid without introducing wrong signs.

### Phase 3 - Prompt and table fidelity fixes
Goal: keep the question display aligned with the archetypes and exam-style presentation.

Actions:
1. Preserve the multiline `Transactions:` narrative section in prompts.
2. Keep editable accounting-equation cells blank unless deliberate scaffold starters are explicitly designed.
3. Ensure headers remain visible.
4. Keep multiline prompt rendering readable in active and review states.

Success criteria:
- The prompt shows a readable vertical transaction list.
- The answer table starts blank where appropriate.
- Headers remain visible and table UX is unchanged.

### Phase 4 - Hint-content upgrade
Goal: make Scaffold hints explanatory rather than generic.

Actions:
1. Upgrade hint content so it explains the accounting consequence of each transaction.
2. Where relevant, hints should explicitly describe account movement, for example:
   - wages paid decrease assets
   - credit sales increase Debtors' Control and increase Sales / owner's equity effect through income
3. Where percentages or derived values are involved, include the actual calculation logic in the hint.
4. Ensure derivation text and cell hints support compare/memo behavior cleanly.
5. Keep Practice mode free of hints.

Success criteria:
- Hints explain why a value changes, not just what to type.
- Percentage-based transactions show the calculation method.
- Scaffold remains helpful without weakening Practice mode.

### Phase 5 - Archetype audit report to generator improvement loop
Goal: turn the audit into concrete generator improvements rather than leaving it as documentation only.

Actions:
1. Convert the archetype audit findings into a correction checklist for generator templates/helpers.
2. Patch generator wording, transaction metadata, payment-method handling, source-document logic, and account-effect logic as required.
3. Keep the report updated with resolved vs unresolved findings.

Success criteria:
- The audit report directly informs generator edits.
- Generator behavior matches the validated archetype set more closely after each patch.

### Phase 6 - Refactor threshold assessment
Goal: avoid turning `sole_trader_generator.py` into an unmaintainable hotspot.

Actions:
1. Continue patching in place while changes remain tightly scoped to accounting-equation validation.
2. If the audit produces broad repeated logic changes across many template families, pause and apply `sole_trader_refactor_plan.md` before expanding further.

Decision rule:
- If the remaining fixes stay local to equation templates, continue in place.
- If archetype correction requires many new shared abstractions, split the generator per the refactor plan.

## Required Audit Report Structure
The archetype review report should capture, at minimum:
- archetype/template identifier
- raw transaction wording
- corrected/validated transaction wording if needed
- transaction category
- cash / credit / other settlement method
- source document(s)
- affected accounts / equation elements
- correct effect direction per element
- calculation rule, if any
- issue found
- recommended generator fix
- status: open / resolved

## Execution Order
1. Perform the full archetype audit and create the report.
2. Correct any invalid transaction-effect logic in the generator.
3. Preserve and refine prompt/table fidelity behavior.
4. Upgrade hint content to explain accounting logic and calculations.
5. Run verification across Scaffold and Practice.
6. Reassess whether generator refactoring is warranted.

## Risks
- Some archetypes may contain wording that does not map cleanly to current generator abstractions.
- A single visible transaction may still require multiple table rows.
- Over-correcting the generator without a full audit report could introduce new accounting inaccuracies.
- Hint improvements may require better derivation metadata from the backend.

## Recommended Verification
1. Generate multiple `equation` questions in Scaffold and Practice.
2. Confirm the prompt includes a vertical transaction list.
3. Confirm editable cells are blank on initial render.
4. Confirm headers are visible.
5. Validate that generated equation effects are correct per archetype and do not force invalid `±` behavior.
6. In Scaffold, test that hints explain the accounting effect.
7. For percentage-based transactions, test that hints show the calculation logic.
8. In Practice, confirm no hints appear and end-of-set review still works.

## Expected Deliverables
### Deliverable 1
An amended plan file: `Gr10Transaction-analysis-validation.md`

### Deliverable 2
An archetype audit report covering correctness, transaction nature, payment methods, source documents, and generator implications.

### Deliverable 3
A corrected first-pass/second-pass generator implementation aligned to the audit findings.

## Status Summary
- Prompt transaction-list work: completed first pass
- Blank editable-cell behavior: completed first pass
- Scaffold per-cell hint surface: completed first pass
- Cross-grade accounting hint audit: completed
- Archetype correctness report: pending
- Generator transaction-effect correction against archetypes: pending
- Hint-content enrichment: pending
- Build/manual verification: pending
