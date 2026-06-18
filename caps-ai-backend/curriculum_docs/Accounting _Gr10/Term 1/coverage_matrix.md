# Accounting Equation Transaction Analysis - Coverage Matrix

**Generated:** 2026-02-03
**Generator Version:** preCoverageMatrix_20260203_073522

## Legend
- ✅ **Covered** - Fully implemented with templates and scaffold hints
- 🟡 **Partial** - Some patterns implemented, gaps remain
- ❌ **Missing** - No implementation yet

---

## Schema Definitions

| Schema ID | Columns | Special Features |
|-----------|---------|------------------|
| activity23 | No., Source doc, A/c Dr, A/c Cr, A, O, L | Activity 23 format (amounts as signed A/O/L) |
| activity24 | No., Source doc, A/c Dr, A/c Cr, Amount, A, O, L | Activity 24 format (signs in A/O/L) |
| gl_amount_aol | No., A/c Dr, A/c Cr, Amount, A, O, L | Basic GL + amount + A/O/L |
| gl_aol | No., A/c Dr, A/c Cr, A, O, L | Basic GL + A/O/L only |
| source_gl_amount_aol | No., Source doc, A/c Dr, A/c Cr, Amount, A, O, L | With source document column |
| journal_gl_amount_aol | No., Subsidiary Journal, A/c Dr, A/c Cr, Amount, A, O, L | With journal column |
| internal_gl_amount_aol | No., Internal Doc, A/c Dr, A/c Cr, Amount, Assets, Equity, Liabilities | Internal document style |
| gl_subledger_amount_aol | No., GL Dr, GL Cr, Subsidiary Dr, Subsidiary Cr, Amount, A, O, L | Nested headers (Section 11) |
| reason_effect | No., Assets(Reason+Effect), OE(Reason+Effect), L(Reason+Effect) | Reason + effect format |

---

## Archetype Section Coverage

### Section 1: Introduction (Bank + Capital)
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Loan received | ✅ | All | `loan_received` helper |
| Capital contribution | ✅ | All | `capital_contribution` helper |

### Section 2: Basic Transactions (Wages, Rent, Insurance)
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Wages paid | ✅ | All with internal/source | `wages_eft_internal` template |
| Rent paid | ✅ | All with internal/source | `rent_debit_order_internal` template |
| Insurance paid | ✅ | All with internal/source | `insurance_stop_order_internal` template |
| Petty cash transfer | ✅ | All | `petty_cash_transfer` template |

### Section 3: Cash Sales + Cost of Sales
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Cash sales + COS | ✅ | All | `cash_sales_cost` helper, 2 rows |

### Section 4: Fixed Deposits + Equipment
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Equipment purchase (cash) | ✅ | All | `equipment_cash_cpj` template |
| Fixed deposit maturity + interest | ✅ | All | `fixed_deposit_maturity` helper, 2 rows |

### Section 5: R/D Cheque + Stationery
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| R/D cheque + discount reversal | ✅ | All | `rd_cheque_gj` template, 2 rows |

### Section 6: Insolvent Debtor + Interest
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Insolvent debtor dividend + write-off | ✅ | All | `insolvent_debtor_dividend_writeoff` helper, 2 rows |
| Interest received | ✅ | All | `interest_income` helper |

### Section 7: Creditor Payment + Returns
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Creditor payment + discount | ✅ | All | `creditor_payment_discount_received` helper, 2 rows |
| Creditor allowance return | ✅ | All | `creditor_allowance_return` helper |

### Section 8: Credit Purchases + Sales
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Credit purchase with trade discount | ✅ | All | `purchase_credit_trade_discount` helper |
| Credit sales + COS | ✅ | All | `credit_sales_cost` helper, 2 rows |
| Debtor settlement with discount | ✅ | All | `debtor_settlement_discount` helper, 2 rows |

### Section 9: Interest + Drawings + Wages
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Interest on overdue debtor | ✅ | All | `interest_on_overdue` helper (kind="debtor") |
| Interest on overdue creditor | ✅ | All | `interest_on_overdue` helper (kind="creditor") |
| Drawings of stationery | 🟡 | All | Generic expense pattern only |
| Wages paid cash | ✅ | All | `wages_eft_internal` template |
| Vehicle purchase on credit | ❌ | All | Not yet implemented |

### Section 10: Credit Purchases + Cash Sales + Fee Income
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Credit purchase with trade discount | ✅ | All | Same as Section 8 |
| Cash sales | ✅ | All | `cash_sales_cost` helper |
| Fee income on credit | ✅ | All | `fee_income_credit` helper |

### Section 11: Nested Columns (Subsidiary Ledger)
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Credit purchase with delivery | ✅ | gl_subledger_amount_aol | `stock_credit_with_delivery_subledger` template |
| Credit sale with debtor subledger | ✅ | gl_subledger_amount_aol | `credit_sale_subledger` template |
| Owner withdrawal | ❌ | All | Not yet implemented |
| Fixed deposit investment | ❌ | All | Not yet implemented |
| Petty cash imprest restoration | ❌ | All | Not yet implemented |
| Debtor allowance | ✅ | All | `debtor_allowance_return` helper |
| Owner taking stock | ❌ | All | Not yet implemented |
| Bank charges | ✅ | All | `bank_charges` helper |
| Interest on current account | ❌ | All | Not yet implemented |

### Section 12: Bank Unfavourable
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Debtor settlement (unfavourable bank) | ✅ | All | `debtor_settlement_discount_unfavourable_bank` helper, 2 rows |
| Cash handling fee | ❌ | All | Not yet implemented |
| Cash withdrawal for wages | ❌ | All | Not yet implemented |
| Interest on overdraft | ✅ | All | `overdraft_interest` helper |
| Packing materials (unfavourable) | ❌ | All | Not yet implemented |
| Petty cash paid on behalf of debtor | ✅ | All | `petty_cash_on_behalf_of_debtor` helper, multi-value cell |

### Section 13: Error Correction + Equipment Return
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Stationery error correction | ✅ | All | `stationery_error_correction` template |
| Equipment return damaged | ✅ | All | `equipment_return_damaged` template |

### Section 14: Loan Repayment + Interest
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Loan repayment with interest | ✅ | All | `loan_repayment_with_interest` helper, 2 rows |
| Creditor payment | ✅ | All | Generic payment pattern |
| Postage paid | ❌ | All | Not yet implemented |

### Section 15: Credit Purchases + Trade Discounts
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Credit purchase with trade discount | ✅ | All | Same as Section 8 |
| Purchase by cheque with trade discount | ✅ | All | `purchase_by_cheque_trade_discount` helper |

### Section 16: Cash Sales + Cost of Sales
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Cash sales + COS | ✅ | All | Same as Section 3 |

### Section 17: Insurance Accrued + Debtor Settlement
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Insurance accrued | ✅ | All | `insurance_accrued` helper |
| Debtor settlement with discount | ✅ | All | Same as Section 8 |

### Section 18: Debtor Allowance + Returns
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Debtor allowance (returned goods) | ✅ | All | `debtor_allowance_return` helper, 2 rows |

### Section 19: Rent Received + Consumable Stores
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Rent received via EFT | ✅ | All | `rent_received_eft` template |
| Consumable stores (petty cash) | ✅ | All | `consumable_petty_cash` template |

### Section 20: Bank Statement Fees + Fixed Deposit
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Bank service fee | ✅ | All | Part of `bank_fee_breakdown` |
| Cash handling fee | ✅ | All | Part of `bank_fee_breakdown` |
| Overdraft interest | ✅ | All | Part of `bank_fee_breakdown` |
| Fixed deposit maturity + interest | ✅ | All | `fixed_deposit_maturity` helper |

### Section 21: Creditor Allowance
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Creditor allowance (returned goods) | ✅ | All | `creditor_allowance_return` helper |

### Section 22: Drawings of Stock
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Drawings of trading stock | ✅ | All | `drawings_stock_cost` helper |

### Section 23: Source Document Heavy
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Bank charges | ✅ | source_gl_amount_aol | `bank_charges_source` template |
| Loan received | ✅ | source_gl_amount_aol | `loan_received_source` template |
| Debtor settlement + discount | ✅ | source_gl_amount_aol | `debtor_settlement_discount_source` template |

### Section 24: Equipment + Cash Sales
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Equipment on credit | ✅ | All | `equipment_credit` template |
| Cash sales + COS | ✅ | All | `cash_sales_cost` template |

### Section 25: Returns + Bad Debts
| Transaction Pattern | Status | Schemas Compatible | Notes |
|--------------------|--------|-------------------|-------|
| Returned equipment | ✅ | All | `equipment_return_damaged` template |
| Cash sales + COS | ✅ | All | Same as Section 3 |
| Bad debt write-off | ✅ | All | `bad_debt_writeoff` helper |

---

## Summary Statistics

| Status | Count | Percentage |
|--------|-------|------------|
| ✅ Covered | 47 | ~85% |
| 🟡 Partial | 1 | ~2% |
| ❌ Missing | 7 | ~13% |

### Missing Patterns (to implement):
1. Vehicle purchase on credit (Section 9)
2. Owner withdrawal (Section 11)
3. Fixed deposit investment (Section 11)
4. Petty cash imprest restoration (Section 11)
5. Owner taking stock (Section 11)
6. Interest on current account (Section 11)
7. Cash handling fee standalone (Section 12)
8. Cash withdrawal for wages (Section 12)
9. Packing materials - unfavourable (Section 12)
10. Postage paid (Section 14)

---

## Helper Functions Inventory

| Helper | Multi-Row | Calculation | Tags Used |
|--------|-----------|-------------|-----------|
| `_make_cash_sales_cost` | ✅ 2 rows | Markup% | - |
| `_make_credit_sales_cost` | ✅ 2 rows | Markup% | - |
| `_make_debtor_settlement_discount` | ✅ 2 rows | Discount% | - |
| `_make_creditor_payment_discount_received` | ✅ 2 rows | Discount% | - |
| `_make_purchase_on_credit_trade_discount` | ❌ | Trade discount% | - |
| `_make_loan_repayment_with_interest` | ✅ 2 rows | Interest calc | - |
| `_make_insolvent_debtor_dividend_writeoff` | ✅ 2 rows | Cents in rand | `insolvency_dividend`, `insolvency_writeoff` |
| `_make_petty_cash_on_behalf_of_debtor` | ❌ | - | `petty_cash_on_behalf_debtor` |
| `_make_fee_income_on_credit` | ❌ | - | `fee_income_credit` |
| `_make_fixed_deposit_maturity` | ✅ 2 rows | Interest calc | `fd_maturity_principal`, `fd_maturity_interest` |
| `_make_bank_fee_breakdown` | ✅ 3 rows | - | `bank_fee_service`, `bank_fee_cash`, `bank_fee_overdraft_int` |
| `_make_debtor_settlement_discount_unfavourable_bank` | ✅ 2 rows | Discount% | `bank_unfavourable_receipt`, `bank_unfavourable_discount` |
| `_make_overdraft_interest` | ❌ | - | `bank_unfavourable_interest` |
| `_make_interest_on_overdue` | ❌ | Interest calc | - |

---

## Schema Compatibility Matrix

| Pattern | activity23/24 | gl_amount_aol | gl_aol | source_gl | journal_gl | internal_gl | gl_subledger | reason_effect |
|---------|--------------|---------------|--------|-----------|------------|-------------|--------------|---------------|
| Basic transactions | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| With source doc | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| With journal | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| With internal doc | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| With subledger | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Multi-row (COS, etc) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

*End of Coverage Matrix*
