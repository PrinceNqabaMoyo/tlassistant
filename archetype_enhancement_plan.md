# Archetype Enhancement Plan: Grade 11 & 12 Accounting

## Overview
This document outlines the complete plan for updating and enhancing the Grade 11 and 12 accounting question generators to match the curriculum archetype documents. The current generators have a fundamental flaw: they output pre-filled answers instead of actual questions with REQUIRED sections, INFORMATION sections, and empty tables for students to complete.

## Current State Assessment

### Critical Issues Identified
1. **Wrong Output Format**: Generators produce pre-filled "answers" as questions
2. **Missing REQUIRED Section**: No clear statement of what students must prepare
3. **Missing INFORMATION Section**: No pre-adjustment balances or adjustments provided
4. **No Empty Templates**: Students need empty tables to fill, not completed ones
5. **Incomplete Archetype Coverage**: Not all archetypes from curriculum docs are implemented

---

## Grade 11 Curriculum Documents & Archetype Mapping

### 1. Partnerships Balance Sheet (Statement of Financial Position)
**File**: `Partnerships balance sheet(stat.financial position)questionarchetypes.md`

#### Archetypes Identified (6 Questions):
| Q# | Type | Current Status | Generator | Action Required |
|----|------|----------------|-----------|-----------------|
| Q1 | Full Balance Sheet + Notes | ⚠️ Partial | `partnership_balance_sheet_generator.py` | **REBUILD**: Add net profit calculation, Trade & Other Payables note, proper adjustment scenarios |
| Q2 | Capital Note + Current Account Note + Calculations | ❌ Missing | None | **NEW**: Create capital note generator with interest on capital calculations, drawings calculations |
| Q3 | Trade Receivables + Payables + Balance Sheet | ⚠️ Partial | `partnership_balance_sheet_generator.py` | **ENHANCE**: Add Trade & Other Payables note, include salaries journal adjustments, loan calculations |
| Q4 | Current Account + Equity Section | ❌ Missing | None | **NEW**: Add equity section only generator with capital/current account split |
| Q5 | Full Balance Sheet with Back-calculations | ❌ Missing | None | **NEW**: Add loan statement interpretation, fixed deposit maturity split |
| Q6 | Equity & Liabilities Section Only | ❌ Missing | None | **NEW**: Create partial balance sheet generator |

#### Specific Enhancements Needed:
- **Q1 Structure**: Net profit calculation → Current Accounts note → Trade & Other Receivables note → Trade & Other Payables note → Balance Sheet
- **Adjustments to Include**: Salaries omitted, bank charges, dishonoured cheques, provision for bad debts, inventory adjustments, loan repayments
- **Missing Notes**: Trade and Other Payables (creditors + accrued expenses + income in advance + SARS PAYE + pension + medical aid + UIF)

---

### 2. Partnerships Ledger Accounts
**File**: `Partnerships ledger account questionarchetypes.md`

#### Archetypes Identified (4 Questions):
| Q# | Type | Current Status | Generator | Action Required |
|----|------|----------------|-----------|-----------------|
| Q1 | Capital Accounts + Current Accounts T-accounts | ⚠️ Partial | `partnership_ledger_generator.py` | **ENHANCE**: Add capital account T-account, proper adjustment scenarios |
| Q2 | Appropriation Account only | ⚠️ Partial | `partnership_ledger_generator.py` | **REVIEW**: Ensure proper context/requirements format |
| Q3 | Current Account with Monthly Drawings | ❌ Missing | None | **NEW**: Add detailed monthly drawings breakdown |
| Q4 | Full Ledger (Capital, Current, Appropriation, Drawings) | ⚠️ Partial | `partnership_ledger_generator.py` | **ENHANCE**: Add drawings account T-account |

#### Specific Enhancements Needed:
- Add Capital Account T-account with capital contribution changes
- Add Drawings Account T-account
- Include detailed transaction descriptions in INFORMATION section
- Add interest on capital calculation breakdowns

---

### 3. Income Statement (Statement of Comprehensive Income)
**File**: `STATEMENT OF COMPREHENSIVE INCOME(INCOME STATEMENT) QArchetypes.md`

#### Archetypes Identified (5 Questions):
| Q# | Type | Current Status | Generator | Action Required |
|----|------|----------------|-----------|-----------------|
| Q1 | Full Income Statement | ⚠️ Partial | `income_statement_generator.py` | **ENHANCE**: Add proper adjustment scenarios (depreciation, consumable stores, bad debts) |
| Q2 | Income Statement + Retained Income Note | ⚠️ Partial | `income_statement_generator.py` | **ENHANCE**: Add retained income note requirement |
| Q3 | Income Statement with Production Cost | ❌ Missing | None | **NEW**: Add manufacturing/production cost statement |
| Q4 | Income Statement with Extraordinary Items | ❌ Missing | None | **NEW**: Add discontinued operations/extraordinary items |
| Q5 | Full Income Statement + Notes | ❌ Missing | None | **NEW**: Complete question with all notes |

#### Specific Enhancements Needed:
- Add pre-adjustment trial balance format
- Include adjustments: depreciation, bad debts, consumable stores, prepaid/accrued items
- Add trading stock deficit/surplus calculations
- Include retained income note requirement

---

### 4. Reconciliation
**File**: `Reconciliation Question Archetypes.md`

#### Archetypes Identified (Multiple sections):
| Section | Type | Current Status | Generator | Action Required |
|---------|------|----------------|-----------|-----------------|
| Bank Reconciliation | Bank Reconciliation Statement | ⚠️ Partial | `reconciliation_generator.py` | **ENHANCE**: Add CRJ/CPJ corrections, proper format |
| Debtors Reconciliation | Debtors List Reconciliation | ❌ Missing | None | **NEW**: Add debtors reconciliation generator |
| Creditors Reconciliation | Creditors List Reconciliation | ❌ Missing | None | **NEW**: Add creditors reconciliation generator |
| Age Analysis | Debtors Age Analysis | ❌ Missing | None | **NEW**: Add age analysis interpretation |

#### Specific Enhancements Needed:
- Bank reconciliation with CRJ/CPJ corrections before reconciliation
- Debtors reconciliation with errors in debtors control vs debtors list
- Creditors reconciliation with errors and omissions

---

### 5. Fixed/Tangible Assets
**File**: `Fixed-Tangible Assets QuestionArcheType.md`

#### Archetypes Identified (Multiple questions):
| Q# | Type | Current Status | Generator | Action Required |
|----|------|----------------|-----------|-----------------|
| Q1 | Asset Register Entry | ❌ Missing | None | **NEW**: Add asset register note generator |
| Q2 | Asset Disposal | ❌ Missing | None | **NEW**: Add asset disposal journal entries |
| Q3 | Fixed Assets Note Calculation | ❌ Missing | None | **NEW**: Add fixed assets note preparation |

---

### 6. Controlled Test Term 1
**File**: `Controlled test_term 1.md`

#### Archetypes Identified:
| Section | Type | Current Status | Generator | Action Required |
|---------|------|----------------|-----------|-----------------|
| Concepts | Concepts & Ethics | ⚠️ Partial | `controlled_test_generator.py` | **ENHANCE**: Add proper question format |
| GAAP | GAAP Principles | ⚠️ Partial | `controlled_test_generator.py` | **ENHANCE**: Add proper question format |
| CRJ/CPJ | Cash Journals with Adjustments | ✅ Added | `controlled_test_generator.py` | **VERIFY**: Check format matches archetype |
| Bank Reconciliation | Full Bank Reconciliation | ⚠️ Partial | `reconciliation_generator.py` | **ENHANCE**: Match CT format |

---

### 7. Concepts
**File**: `Concepts questionArchetypes.md`

#### Archetypes Identified:
| Type | Current Status | Generator | Action Required |
|------|----------------|-----------|-----------------|
| Concepts (Typed) | ⚠️ Partial | `controlled_test_generator.py` | **ENHANCE**: Add proper REQUIRED/INFORMATION format |
| Ethics (Typed) | ⚠️ Partial | `controlled_test_generator.py` | **ENHANCE**: Add proper REQUIRED/INFORMATION format |
| Internal Control (Typed) | ⚠️ Partial | `controlled_test_generator.py` | **ENHANCE**: Add proper REQUIRED/INFORMATION format |
| GAAP (Typed) | ⚠️ Partial | `controlled_test_generator.py` | **ENHANCE**: Add proper REQUIRED/INFORMATION format |

---

## Grade 12 Curriculum Documents & Archetype Mapping

### 1. Analysis & Interpretation
**File**: `Analysis and interpretation of financial statements.md`

#### Archetypes Identified:
| Type | Current Status | Generator | Action Required |
|------|----------------|-----------|-----------------|
| Ratio Calculations | ⚠️ Partial | `analysis_interpretation_generator.py` | **REVIEW**: Ensure proper context provided |
| Comment Questions | ⚠️ Partial | `analysis_interpretation_generator.py` | **ENHANCE**: Add scenario context before questions |
| Comparative Analysis | ❌ Missing | None | **NEW**: Add multi-year comparison |
| Cash Flow Integration | ❌ Missing | None | **NEW**: Link cash flow to analysis |

---

### 2. Company Financial Statements
**File**: `Financial statements and notes.md`

#### Archetypes Identified (Multiple sections):
| Section | Type | Current Status | Generator | Action Required |
|---------|------|----------------|-----------|-----------------|
| Income Statement | Company Income Statement | ❌ Missing | None | **NEW**: Add company IS generator |
| Balance Sheet | Company Balance Sheet | ❌ Missing | None | **NEW**: Add company SFP generator |
| Cash Flow | Company Cash Flow Statement | ⚠️ Partial | `cash_flow_generator.py` | **ENHANCE**: Add proper notes integration |
| Notes | Fixed Assets, Trade Receivables, etc. | ⚠️ Partial | `cash_flow_generator.py` | **ENHANCE**: Add all company-specific notes |
| Retained Income | Retained Income Note | ❌ Missing | None | **NEW**: Add retained income note |
| Share Capital | Share Capital Note | ❌ Missing | None | **NEW**: Add share capital note |

---

### 3. Company General Ledger
**File**: `Bookkeeping of companies- General Legder of companies.md`

#### Archetypes Identified:
| Type | Current Status | Generator | Action Required |
|------|----------------|-----------|-----------------|
| Share Capital Ledger | ❌ Missing | None | **NEW**: Add share capital account |
| Retained Income Ledger | ❌ Missing | None | **NEW**: Add retained income account |
| Dividends Account | ❌ Missing | None | **NEW**: Add dividends account |
| SARS (Income Tax) | ❌ Missing | None | **NEW**: Add SARS income tax account |

---

### 4. Audits & Corporate Governance
**File**: `Audits, Corporate Governance and Shareholding.md`

#### Archetypes Identified:
| Type | Current Status | Generator | Action Required |
|------|----------------|-----------|-----------------|
| Audit Questions | ❌ Missing | None | **NEW**: Add audit opinion scenarios |
| Corporate Governance | ❌ Missing | None | **NEW**: Add King IV/King III questions |
| Shareholder Questions | ❌ Missing | None | **NEW**: Add AGM/shareholder meeting questions |

---

### 5. Concepts
**File**: `Concepts.md`

#### Archetypes Identified:
| Type | Current Status | Generator | Action Required |
|------|----------------|-----------|-----------------|
| Company Concepts | ❌ Missing | None | **NEW**: Add company-specific concepts |
| Ethical Behaviour | ❌ Missing | None | **NEW**: Add ethics scenarios |
| Legislation | ❌ Missing | None | **NEW**: Add Companies Act questions |

---

### 6. Controlled Test Term 1
**File**: `ControlledTest_Term1.md`

#### Archetypes Identified:
| Type | Current Status | Generator | Action Required |
|------|----------------|-----------|-----------------|
| Fixed Assets Back-calc | ✅ Added | `cash_flow_generator.py` | **VERIFY**: Check format |
| Cash Flow Preparation | ⚠️ Partial | `cash_flow_generator.py` | **ENHANCE**: Add full question format |

---

## Implementation Priority Matrix

### Phase 1: Critical Fixes (Must Have)
1. **partnership_balance_sheet_generator.py** - Complete rebuild with proper format
2. **income_statement_generator.py** - Complete rebuild with proper format
3. **partnership_ledger_generator.py** - Add missing capital/drawings accounts
4. **reconciliation_generator.py** - Add debtors/creditors reconciliation

### Phase 2: Missing Generators (High Priority)
1. Create `company_income_statement_generator.py`
2. Create `company_balance_sheet_generator.py`
3. Create `company_ledger_generator.py`
4. Create `audit_corporate_governance_generator.py`

### Phase 3: Enhancement (Medium Priority)
1. Add all missing note types to existing generators
2. Add concept/ethics/GAAP proper format
3. Add fixed assets register/disposal generators
4. Add age analysis generators

### Phase 4: Advanced Features (Low Priority)
1. Multi-year comparative questions
2. Complex integration questions (IS → SFP → Cash Flow → Analysis)
3. Manufacturing cost statements

---

## Question Format Standards

### Required Structure for All Questions:

```
[BUSINESS NAME]

#### REQUIRED:
[Numbered list of what student must prepare]
- e.g., "1.1 Calculate the correct net profit"
- e.g., "1.2 Prepare the Current Accounts note"
- e.g., "1.3 Prepare the Balance Sheet"

#### INFORMATION:

A. Balances on [DATE]:
[List of pre-adjustment balances in trial balance format]

B. Additional information and adjustments:
[Numbered list of adjustments]
1. [Adjustment 1]
2. [Adjustment 2]
...

C. Partnership agreement / Company policy:
[Terms for interest, salaries, profit sharing, etc.]
```

### Practice Mode Output:
- Empty tables with only row labels (some may be missing for student to fill)
- No values pre-filled
- All calculation cells blank

### Scaffold Mode Output:
- Tables with correct values filled in
- Cell hints showing calculation steps
- Sample answers for typed questions

---

## File-by-File Action Plan

### Grade 11 Files to Modify:

1. `partnership_balance_sheet_generator.py`
   - [ ] Add `_make_trade_and_other_payables_note()` function
   - [ ] Rewrite `_make_current_accounts_note()` with full adjustments
   - [ ] Rewrite `_make_trade_and_other_receivables_note()` with full adjustments
   - [ ] Rewrite `_make_balance_sheet()` with net profit calculation requirement
   - [ ] Add scenario generator for complex adjustments

2. `income_statement_generator.py`
   - [ ] Add proper REQUIRED/INFORMATION format
   - [ ] Add adjustment scenarios (depreciation, bad debts, consumable stores)
   - [ ] Add retained income note requirement option

3. `partnership_ledger_generator.py`
   - [ ] Add `_make_capital_account_question()` function
   - [ ] Add `_make_drawings_account_question()` function
   - [ ] Enhance existing functions with proper format

4. `reconciliation_generator.py`
   - [ ] Add `_make_debtors_reconciliation_question()` function
   - [ ] Add `_make_creditors_reconciliation_question()` function
   - [ ] Add `_make_age_analysis_question()` function

5. `controlled_test_generator.py`
   - [ ] Verify CRJ/CPJ adjustments format
   - [ ] Add concept questions with proper format
   - [ ] Add GAAP questions with proper format

### Grade 12 Files to Create/Modify:

1. **NEW**: `company_income_statement_generator.py`
   - Company-specific income statement format
   - Appropriation account handling
   - Tax calculations

2. **NEW**: `company_balance_sheet_generator.py`
   - Share capital note
   - Retained income note
   - Company-specific balance sheet format

3. **NEW**: `company_ledger_generator.py`
   - Share capital account
   - Retained income account
   - Dividends account
   - SARS (income tax) account

4. `cash_flow_generator.py`
   - [ ] Enhance with proper REQUIRED/INFORMATION format
   - [ ] Add integration with notes
   - [ ] Add back-calculation scenarios

5. `analysis_interpretation_generator.py`
   - [ ] Add scenario context before questions
   - [ ] Add comparative year questions

6. **NEW**: `audit_governance_generator.py`
   - Audit opinion questions
   - Corporate governance (King IV)
   - Shareholder meeting scenarios

---

## Curriculum Notes Mapping

Each generator must set the correct `archetype_key` to link to curriculum notes:

| Generator | Archetype Key Pattern |
|-----------|----------------------|
| Current Accounts Note | `g11_partnership_balance_sheet_current_accounts_note` |
| Trade Receivables Note | `g11_partnership_balance_sheet_trade_receivables_note` |
| Trade Payables Note | `g11_partnership_balance_sheet_trade_payables_note` |
| Balance Sheet | `g11_partnership_balance_sheet_statement` |
| Income Statement | `g11_partnership_income_statement` |
| Capital Account | `g11_partnership_ledger_capital` |
| Current Account | `g11_partnership_ledger_current` |
| Appropriation Account | `g11_partnership_ledger_appropriation` |
| Drawings Account | `g11_partnership_ledger_drawings` |
| Bank Reconciliation | `g11_bank_reconciliation` |
| Debtors Reconciliation | `g11_debtors_reconciliation` |
| Creditors Reconciliation | `g11_creditors_reconciliation` |
| CRJ/CPJ Adjustments | `g11_ct1_crj_cpj_adjustments` |
| Fixed Assets Back-calc | `g12_ct1_fixed_assets_backcalc` |
| Company Cash Flow | `g12_company_cash_flow` |
| Analysis Ratios | `g12_analysis_ratios` |
| Analysis Comments | `g12_analysis_comments` |

---

## Success Criteria

1. All questions follow the REQUIRED/INFORMATION format from curriculum docs
2. Practice mode shows empty tables (not pre-filled answers)
3. Scaffold mode shows answers with calculation hints
4. All archetypes from curriculum docs have corresponding generators
5. Each question has correct `archetype_key` for curriculum notes integration
6. Questions support both "practice" and "scaffold" modes correctly

---

## Timeline Estimate

- **Phase 1 (Critical Fixes)**: 3-4 sessions
- **Phase 2 (Missing Generators)**: 4-5 sessions
- **Phase 3 (Enhancement)**: 2-3 sessions
- **Phase 4 (Advanced)**: 2-3 sessions

**Total**: ~12-15 sessions to complete full archetype coverage with proper format

---

## Notes

- Each generator rewrite should include comprehensive test cases
- Cell hints must include calculation breakdowns
- All monetary values must include "R" symbol and proper formatting
- Row labels in tables should sometimes be left blank (marked with ">" in archetypes) for students to fill
- Values marked with "*" in archetypes indicate given values that should be pre-filled
