# Phase D: Term 2 Topic Implementation Plan

## Scope — Grade 10 (3 topics, starting here)

### Topic 1: Salaries & Wages Journal
**Subskills (scaffold steps):**
1. `salary_scales` — Reading salary scales (notch/annual/monthly)
2. `wages_calc` — Gross wage calculation (ordinary + overtime)
3. `deductions` — PAYE, pension, medical aid, UIF deductions
4. `employer_contributions` — SDL, UIF, medical, pension contributions
5. `salary_journal` — Complete the Salary Journal
6. `wage_journal` — Complete the Wage Journal
7. `general_ledger` — Post journals to General Ledger

**Frontend files (NEW):**
- `src/components/workspace/grade10/accounting/salaries-wages/controller.js`
- `src/components/workspace/grade10/accounting/salaries-wages/index.js`
- `src/components/workspace/grade10/accounting/salaries-wages/Grade10AccountingSalariesWagesScaffold.jsx`
- `src/components/workspace/grade10/accounting/salaries-wages/Grade10AccountingSalariesWagesPractice.jsx`
- `src/components/workspace/grade10/accounting/salaries-wages/VisualAids.jsx`

---

### Topic 2: Sole Trader Final Accounts & Year-end
**Subskills:**
1. `closing_transfers` — Steps in closing transfer process
2. `depreciation` — Straight line & diminishing balance
3. `bad_debts` — Writing off irrecoverable debts
4. `year_end_adjustments` — Accruals, prepayments, consumable stores
5. `final_accounts` — Trading + Profit & Loss accounts
6. `post_closing_tb` — Post-closing Trial Balance

**Frontend files (NEW):**
- `src/components/workspace/grade10/accounting/final-accounts/controller.js`
- `src/components/workspace/grade10/accounting/final-accounts/index.js`
- `src/components/workspace/grade10/accounting/final-accounts/Grade10AccountingFinalAccountsScaffold.jsx`
- `src/components/workspace/grade10/accounting/final-accounts/Grade10AccountingFinalAccountsPractice.jsx`
- `src/components/workspace/grade10/accounting/final-accounts/VisualAids.jsx`

---

### Topic 3: Value Added Tax (VAT)
**Subskills:**
1. `vat_concepts` — VAT rate, zero-rated, exempt, taxable
2. `vat_calculations` — Calculate VAT inclusive/exclusive amounts
3. `vat_classification` — Classify supplies (taxable/exempt/zero-rated)
4. `vat_ethics` — Tax evasion vs avoidance, ethical scenarios

**Frontend files (NEW):**
- `src/components/workspace/grade10/accounting/vat/controller.js`
- `src/components/workspace/grade10/accounting/vat/index.js`
- `src/components/workspace/grade10/accounting/vat/Grade10AccountingVATScaffold.jsx`
- `src/components/workspace/grade10/accounting/vat/Grade10AccountingVATPractice.jsx`
- `src/components/workspace/grade10/accounting/vat/VisualAids.jsx`

---

## Files to MODIFY (already backed up)

| File | Change |
|------|--------|
| `grade10Registry.js` | Add 3 new Route components + imports |
| `CurriculumHelper.jsx` | Add 3 topic detectors + mode routing + ordering + subskill rendering |

## Implementation Order
1. Create all 15 new files for 3 topics
2. Wire into CurriculumHelper.jsx (topic detection + routing)
3. Wire into grade10Registry.js (route components)
4. Build & test
