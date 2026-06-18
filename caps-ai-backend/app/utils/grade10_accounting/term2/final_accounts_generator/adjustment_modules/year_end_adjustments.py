from __future__ import annotations

import random
from typing import Any, Dict, List

from .....sole_trader.names import pick_business_name as _pick_business_name
from ..reversal_families import _gen_reversal_adjustments
from ..shared import (
    _cell,
    _make_calc,
    _make_fill_in_table_question,
    _make_mcq,
    _make_typed,
    _round_money,
    _teaching_hint,
    _with_validation,
)
def _gen_year_end_adjustments(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    biz = _pick_business_name(r=r)

    pool.append(_make_mcq(
        prompt="What is the double entry to write off a debtor (D. Davids) as irrecoverable (bad debt)?",
        options=[
            "Dr. Debtors control, Cr. Bad debts.",
            "Dr. Bad debts (expense), Cr. Debtors control.",
            "Dr. Bank, Cr. Bad debts recovered.",
            "Dr. Capital, Cr. Debtors control.",
        ],
        correct_index=1,
        explanation="Dr. Bad debts (expense) / Cr. Debtors control AND Cr. the debtor's individual account in the Debtors Ledger.",
    ))

    pool.append(_make_mcq(
        prompt="An amount is received from a debtor whose account was previously written off as bad debt. Which account is credited if the Bad debts account is debited to correct the earlier treatment?",
        options=[
            "Bad debts recovered",
            "Debtors control",
            "Trading stock surplus",
            "Accumulated depreciation",
        ],
        correct_index=0,
        explanation="Amounts recovered after a write-off are credited to Bad debts recovered when the Bad debts account is debited to correct the earlier treatment.",
    ))

    pool.append(_make_mcq(
        prompt="Rent for December has not yet been paid at year-end. What type of adjustment is this?",
        options=[
            "Prepaid expense.",
            "Income received in advance.",
            "Accrued expense (expense payable).",
            "Bad debt.",
        ],
        correct_index=2,
        explanation="An accrued expense is an expense that has been incurred but not yet paid at year-end. Dr. Expense / Cr. Accrued expense.",
    ))

    pool.append(_make_mcq(
        prompt="Insurance of R12,000 was paid for a 12-month period starting 1 October. The financial year ends 31 December. What is the prepaid amount?",
        options=[
            "R12,000",
            "R3,000",
            "R9,000",
            "R6,000",
        ],
        correct_index=2,
        explanation="3 months used (Oct-Dec), 9 months prepaid (Jan-Sep next year). Prepaid = 9/12 × R12,000 = R9,000.",
    ))

    consumables_bought = r.choice([2400, 3600, 5000, 8000])
    consumables_on_hand = r.choice([400, 600, 800, 1200])
    consumables_used = _round_money(consumables_bought - consumables_on_hand)

    pool.append(_with_validation(_make_calc(
        prompt=f"{biz} purchased stationery (consumable stores) worth R{consumables_bought:,} during the year. At year-end, stationery on hand is R{consumables_on_hand:,}.\n\nCalculate the stationery expense for the year.",
        correct_answer=consumables_used,
        working_formula=f"Stationery expense = Purchased - On hand = R{consumables_bought:,} - R{consumables_on_hand:,}",
        formula_hint="Stationery expense = Purchased - On hand",
    ), "adjustment_consumables_used", purchased=consumables_bought, on_hand=consumables_on_hand))

    rent_monthly = r.choice([3000, 4000, 5000, 6000])
    months_owed = r.choice([1, 2])
    accrued_income = _round_money(rent_monthly * months_owed)

    pool.append(_with_validation(_make_calc(
        prompt=f"{biz} receives rent income of R{rent_monthly:,} per month. At year-end, {months_owed} month(s) of rent has not yet been received.\n\nCalculate the accrued income.",
        correct_answer=accrued_income,
        working_formula=f"Accrued income = R{rent_monthly:,} × {months_owed}",
        formula_hint="Accrued income = monthly amount × months owing",
    ), "adjustment_accrued_income", monthly_amount=rent_monthly, months=months_owed))

    loan_balance = r.choice([80000, 100000, 120000, 150000])
    loan_rate = r.choice([10, 12, 15])
    months_outstanding = r.choice([3, 6])
    accrued_interest = _round_money(loan_balance * loan_rate / 100 * months_outstanding / 12)
    pool.append(_with_validation(_make_calc(
        prompt=f"{biz} has a loan balance of R{loan_balance:,} at {loan_rate}% per annum. Interest for the last {months_outstanding} month(s) of the year has not yet been paid and must be provided for.\n\nCalculate the accrued interest on the loan.",
        correct_answer=accrued_interest,
        working_formula=f"Accrued interest = R{loan_balance:,} × {loan_rate}% × {months_outstanding}/12",
        formula_hint="Accrued interest = loan balance × rate × months/12",
    ), "adjustment_accrued_interest", loan_balance=loan_balance, rate=loan_rate, months=months_outstanding))

    pool.append(_make_mcq(
        prompt="Interest on overdraft was incorrectly classified as bank charges. Which correction entry is needed?",
        options=[
            "Debit Interest on overdraft, credit Bank charges.",
            "Debit Bank charges, credit Interest on overdraft.",
            "Debit Accrued expenses, credit Interest on overdraft.",
            "Debit Interest on overdraft, credit Bank.",
        ],
        correct_index=0,
        explanation="The expense was classified to the wrong nominal account. The correction is Dr Interest on overdraft / Cr Bank charges.",
    ))

    pool.append(_make_mcq(
        prompt="A tenant pays 3 months' rent in advance on 1 December. The financial year ends 31 December. How should the 2 months' advance rent be treated?",
        options=[
            "Debit: Rent income, Credit: Income received in advance (liability).",
            "Debit: Bank, Credit: Rent income.",
            "Debit: Accrued income, Credit: Bank.",
            "Debit: Rent income, Credit: Capital.",
        ],
        correct_index=0,
        explanation="2 months' rent received in advance is a liability (income received in advance). Dr. Rent income / Cr. Income received in advance.",
    ))

    ts_per_records = r.choice([45000, 60000, 80000, 100000])
    actual_count = r.choice([ts_per_records - r.choice([500, 1000, 2000, 3000]), ts_per_records + r.choice([200, 500])])
    diff = _round_money(actual_count - ts_per_records)
    is_deficit = diff < 0

    pool.append(_with_validation(_make_calc(
        prompt=f"{biz}'s trading stock per records: R{ts_per_records:,}. Physical stock count: R{actual_count:,}.\n\nCalculate the stock {'deficit' if is_deficit else 'surplus'} (enter as a positive number).",
        correct_answer=abs(diff),
        working_formula=f"{'Deficit' if is_deficit else 'Surplus'} = |R{actual_count:,} - R{ts_per_records:,}| = R{abs(diff):,.2f}",
        formula_hint="Stock difference = |physical stock - stock per records|",
    ), "adjustment_stock_difference", per_records=ts_per_records, actual_count=actual_count))

    journal_amount = _round_money(consumables_on_hand)
    journal_table = {
        "heading": "General Journal",
        "headers": ["Date", "Details", "Debit", "Credit"],
        "rows": [
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="adj-consumables-dr-details"), _cell("", editable=True, cell_id="adj-consumables-dr-amount"), _cell("")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="adj-consumables-cr-details"), _cell(""), _cell("", editable=True, cell_id="adj-consumables-cr-amount")],
        ],
    }
    journal_correct_map = {
        "adj-consumables-dr-details": "Consumable stores on hand",
        "adj-consumables-dr-amount": journal_amount,
        "adj-consumables-cr-details": "Consumable stores",
        "adj-consumables-cr-amount": journal_amount,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="journal",
        prompt=f"{biz} purchased consumable stores costing R{consumables_bought:,} during the year. At year-end, consumable stores on hand amount to R{consumables_on_hand:,}. Prepare the General Journal entry to record the year-end adjustment.",
        table=journal_table,
        correct_map=journal_correct_map,
        derivation_map={
            "adj-consumables-dr-amount": f"Use the stores-on-hand figure given: R{int(journal_amount):,}.",
            "adj-consumables-cr-amount": f"Credit the same stores-on-hand figure to the expense account: R{int(journal_amount):,}.",
        },
        cell_hints={
            "adj-consumables-dr-details": "The unused stores become an asset at year-end, so the debit account is the stores-on-hand asset account.",
            "adj-consumables-cr-details": "Credit the consumable-stores expense account to remove the unused portion from this year's expense.",
            "adj-consumables-dr-amount": "Use the amount still on hand at year-end, not the total purchased during the year.",
            "adj-consumables-cr-amount": "Journal amounts must agree on both sides of the entry.",
        },
        cell_teaching_map={
            "adj-consumables-dr-details": _teaching_hint(
                role_in_requirement="This cell names the asset account debited for the unused stores still on hand.",
                evidence_from_question=f"The prompt states that consumable stores on hand at year-end amount to R{int(consumables_on_hand):,}.",
                rule_or_principle="Unused consumable stores are carried forward as an asset rather than remaining part of the current-year expense.",
                method_or_formula="Year-end entry: Dr Consumable stores on hand / Cr Consumable stores.",
                record_link="This same amount later appears as an asset carry-forward in ledger, trial-balance, or statement extracts where applicable.",
                how_to_derive="Debit Consumable stores on hand because the unused portion still benefits the next period.",
                transfer_tip="When part of a consumable purchase remains unused, move that part out of expense and into an asset account.",
            ),
            "adj-consumables-cr-details": _teaching_hint(
                role_in_requirement="This cell names the expense account credited to reduce the current-year consumables expense.",
                evidence_from_question=f"The amount on hand of R{int(consumables_on_hand):,} is part of the purchases that was not consumed this year.",
                rule_or_principle="Only the used portion should remain in the expense account for the current year.",
                method_or_formula="Credit Consumable stores with the stores-on-hand amount.",
                record_link="The reduced expense balance is the adjusted amount that belongs in the Income Statement for the year.",
                how_to_derive="Credit Consumable stores because the unused amount must be removed from this year's expense total.",
                transfer_tip="The asset created at year-end is matched by reducing the related expense by the same amount.",
            ),
        },
        working_map={
            "adj-consumables-dr-details": "Treat the stores-on-hand figure as the unused portion that must be carried forward to the next period.",
            "adj-consumables-cr-details": "The same amount is removed from the expense account so only the used portion remains in this year's records.",
        },
        guidelines=["The asset on hand is debited.", "The expense account is credited to reduce the amount consumed during the year.", "Enter the same amount on both sides."],
        marks=8,
    ), "adjustment_consumables_journal_fill", expected_cells=4, amount=journal_amount))

    accrued_income_table = {
        "heading": "Adjustment analysis: accrued income",
        "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
        "rows": [
            [_cell("Rent income earned but not yet received"), _cell("", editable=True, cell_id="adj-acc-inc-amount"), _cell("", editable=True, cell_id="adj-acc-inc-dr"), _cell("", editable=True, cell_id="adj-acc-inc-cr"), _cell("", editable=True, cell_id="adj-acc-inc-is"), _cell("", editable=True, cell_id="adj-acc-inc-bs")],
        ],
    }
    pool.append(_make_fill_in_table_question(
        question_type="adjustment_analysis_table",
        prompt=f"{biz} is still owed rent income of R{accrued_income:,} at year-end. Complete the adjustment analysis table.",
        table=accrued_income_table,
        correct_map={
            "adj-acc-inc-amount": accrued_income,
            "adj-acc-inc-dr": "Accrued income",
            "adj-acc-inc-cr": "Rent income",
            "adj-acc-inc-is": "Income increases by R" + f"{accrued_income:,}",
            "adj-acc-inc-bs": "Current asset increases by R" + f"{accrued_income:,}",
        },
        derivation_map={
            "adj-acc-inc-amount": f"Use the accrued income amount already calculated: R{accrued_income:,}",
        },
        cell_hints={
            "adj-acc-inc-amount": "Use the amount still owing at year-end; the same amount runs through the whole adjustment.",
            "adj-acc-inc-dr": "For accrued income, the asset account is debited.",
            "adj-acc-inc-cr": "The related income account is credited because the income has been earned.",
            "adj-acc-inc-is": "Think about what happens to income in the Income Statement.",
            "adj-acc-inc-bs": "Think about which Balance Sheet category is affected by an amount still receivable.",
        },
        cell_teaching_map={
            "adj-acc-inc-amount": _teaching_hint(
                role_in_requirement="This cell records the amount column of the accrued-income analysis row.",
                evidence_from_question=f"The question states that rent income of R{int(accrued_income):,} is still owing at year-end.",
                rule_or_principle="The analysis row uses the same amount as the adjustment being analysed because every part of the row refers to one accrual amount.",
                method_or_formula=f"Enter R{int(accrued_income):,} in the amount column.",
                record_link="This amount must match the debit to Accrued income, the credit to Rent income, and the statement effects shown in the same row.",
                how_to_derive="Copy the accrued-income amount directly from the prompt before completing the account and effect columns.",
                transfer_tip="Lock in the source amount first, then carry that same figure through the rest of the analysis row.",
            ),
            "adj-acc-inc-dr": _teaching_hint(
                role_in_requirement="This cell identifies the debit account for the accrual.",
                evidence_from_question="The income has been earned but not yet received.",
                rule_or_principle="Amounts receivable at year-end are assets.",
                method_or_formula="Debit Accrued income and credit Rent income with the same accrued amount.",
                record_link="This receivable will later appear as a current asset in the Balance Sheet / statement extracts.",
                how_to_derive="Debit Accrued income because the business now has a claim to receive the money.",
                transfer_tip="When income is owing to the business, debit the accrued income asset and credit the income account.",
            ),
            "adj-acc-inc-cr": _teaching_hint(
                role_in_requirement="This cell identifies the income account credited for the accrual.",
                evidence_from_question="The rent income belongs to the current period even though the cash has not yet been received.",
                rule_or_principle="Income earned in the current period must be recognised in that same period.",
                method_or_formula="Credit Rent income with the accrued amount still owing.",
                record_link="This credit increases the Income Statement income figure for the year.",
                how_to_derive="Use Rent income because that is the nominal income account affected by the adjustment.",
                transfer_tip="For accrued income, the debit creates the receivable and the credit increases the earned income.",
            ),
            "adj-acc-inc-is": _teaching_hint(
                role_in_requirement="This cell explains the Income Statement effect of accrued rent income.",
                evidence_from_question=f"The business is still owed R{int(accrued_income):,} rent income at year-end.",
                rule_or_principle="Accrued income increases current-period income because it has already been earned.",
                method_or_formula="Show an increase in income equal to the accrued amount.",
                record_link="This effect must agree with the credit to Rent income in the double entry.",
                how_to_derive=f"State that income increases by R{int(accrued_income):,}.",
                transfer_tip="If income is owing to the business, the Income Statement effect is usually an increase in income.",
            ),
            "adj-acc-inc-bs": _teaching_hint(
                role_in_requirement="This cell explains the Balance Sheet effect of the accrued-income adjustment.",
                evidence_from_question="The amount is still receivable from the customer / tenant at year-end.",
                rule_or_principle="Amounts receivable are shown as current assets until they are collected.",
                method_or_formula="Carry the accrued amount to a current-asset category.",
                record_link="This effect must agree with the debit entry to Accrued income.",
                how_to_derive=f"State that current assets increase by R{int(accrued_income):,}.",
                transfer_tip="Link the debit account in the journal directly to its Balance Sheet category.",
            ),
        },
        working_map={
            "adj-acc-inc-amount": "Use the stated accrued-income amount first, then carry that same figure across the account and statement-effect columns.",
            "adj-acc-inc-dr": "This accrual creates a receivable asset and increases current-period income with the same amount.",
            "adj-acc-inc-is": "Because the amount is earned this period, the same figure that creates the receivable also increases income.",
            "adj-acc-inc-bs": "The same amount that increases rent income is shown as a current asset because it is still owing.",
        },
        guidelines=[
            "An accrued income increases both income and current assets.",
            "Use the same amount through the double entry and the statement effects.",
        ],
        marks=6,
    ))

    accrued_expense_amount = _round_money(r.choice([580, 750, 1200, 1800]))
    accrued_expense_table = {
        "heading": "Adjustment analysis: accrued expense",
        "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
        "rows": [
            [_cell("Expense incurred but not yet paid"), _cell("", editable=True, cell_id="adj-acc-exp-amount"), _cell("", editable=True, cell_id="adj-acc-exp-dr"), _cell("", editable=True, cell_id="adj-acc-exp-cr"), _cell("", editable=True, cell_id="adj-acc-exp-is"), _cell("", editable=True, cell_id="adj-acc-exp-bs")],
        ],
    }
    pool.append(_make_fill_in_table_question(
        question_type="adjustment_analysis_table",
        prompt=f"{biz} still owes telephone expenses of R{accrued_expense_amount:,} at year-end. Complete the adjustment analysis table.",
        table=accrued_expense_table,
        correct_map={
            "adj-acc-exp-amount": accrued_expense_amount,
            "adj-acc-exp-dr": "Telephone",
            "adj-acc-exp-cr": "Accrued expenses",
            "adj-acc-exp-is": "Expense increases by R" + f"{accrued_expense_amount:,}",
            "adj-acc-exp-bs": "Current liability increases by R" + f"{accrued_expense_amount:,}",
        },
        derivation_map={
            "adj-acc-exp-amount": f"Use the outstanding telephone expense amount given: R{accrued_expense_amount:,}.",
        },
        cell_hints={
            "adj-acc-exp-amount": "Use the unpaid year-end amount throughout the whole analysis row.",
            "adj-acc-exp-dr": "Outstanding expense: debit the expense account.",
            "adj-acc-exp-cr": "The unpaid amount is a liability at year-end.",
            "adj-acc-exp-is": "An unpaid expense still belongs to this period, so think about the effect on expenses.",
            "adj-acc-exp-bs": "The unpaid amount is owed to someone else, so think liability rather than asset.",
        },
        cell_teaching_map={
            "adj-acc-exp-amount": _teaching_hint(
                role_in_requirement="This cell records the amount column of the accrued-expense analysis row.",
                evidence_from_question=f"The question states that telephone expenses of R{int(accrued_expense_amount):,} are still owing at year-end.",
                rule_or_principle="The same outstanding amount is used across the whole analysis row because the row analyses one unpaid expense adjustment.",
                method_or_formula=f"Enter R{int(accrued_expense_amount):,} in the amount column.",
                record_link="This amount must match the debit to Telephone, the credit to Accrued expenses, and both statement effects in the row.",
                how_to_derive="Copy the outstanding expense amount directly from the prompt before filling in the rest of the row.",
                transfer_tip="In analysis tables, the amount column anchors every other answer in that row, so set it first.",
            ),
            "adj-acc-exp-dr": _teaching_hint(
                role_in_requirement="This cell identifies the expense account debited for the accrual.",
                evidence_from_question=f"Telephone expenses of R{int(accrued_expense_amount):,} are still owing at year-end.",
                rule_or_principle="An expense incurred but not yet paid is recognised in the current period by debiting the expense account.",
                method_or_formula="Debit Telephone and credit Accrued expenses with the outstanding amount.",
                record_link="This debit increases the expense figure that will later appear in the Income Statement.",
                how_to_derive="Use Telephone because that is the expense account affected by the unpaid amount.",
                transfer_tip="When the business still owes an expense, think expense up and payable up.",
            ),
            "adj-acc-exp-cr": _teaching_hint(
                role_in_requirement="This cell identifies the liability account credited for the unpaid expense.",
                evidence_from_question="The telephone expense has been incurred but has not yet been paid by year-end.",
                rule_or_principle="Outstanding expenses are current liabilities until settlement takes place.",
                method_or_formula="Credit Accrued expenses with the same amount used to debit Telephone.",
                record_link="This credit creates the year-end liability that is carried to the Balance Sheet.",
                how_to_derive="Because the amount is still payable, credit Accrued expenses.",
                transfer_tip="If cash has not yet been paid, the credit side is often an accrued-expense liability.",
            ),
            "adj-acc-exp-is": _teaching_hint(
                role_in_requirement="This cell explains the Income Statement effect of the accrued-expense adjustment.",
                evidence_from_question=f"The business still owes R{int(accrued_expense_amount):,} for telephone at year-end.",
                rule_or_principle="Outstanding expenses increase the expense for the current period because the cost has already been incurred.",
                method_or_formula="Show an increase in expense equal to the accrued amount.",
                record_link="This statement effect must agree with the debit to Telephone in the journal logic.",
                how_to_derive=f"State that expenses increase by R{int(accrued_expense_amount):,}.",
                transfer_tip="A debit to an expense account usually means the Income Statement effect is an increase in expenses.",
            ),
            "adj-acc-exp-bs": _teaching_hint(
                role_in_requirement="This cell explains the Balance Sheet effect of the accrued-expense adjustment.",
                evidence_from_question="The amount is still owed to an outside party at year-end.",
                rule_or_principle="Amounts still payable are shown as current liabilities.",
                method_or_formula="Carry the accrued amount to current liabilities.",
                record_link="This effect must match the credit entry to Accrued expenses.",
                how_to_derive=f"State that current liabilities increase by R{int(accrued_expense_amount):,}.",
                transfer_tip="Connect the credited payable account directly to the Balance Sheet liability category.",
            ),
        },
        working_map={
            "adj-acc-exp-amount": "Use the unpaid year-end amount as the fixed figure for the whole analysis row before deciding the account and statement effects.",
            "adj-acc-exp-dr": "This adjustment recognises the expense in the current year and creates a matching liability for the unpaid amount.",
            "adj-acc-exp-is": "Because the unpaid cost still belongs to this year, the same amount increases the expense in the Income Statement.",
            "adj-acc-exp-bs": "The same amount that increases Telephone also becomes a current liability because it is still owing.",
        },
        guidelines=[
            "An accrued expense increases expenses and increases current liabilities.",
        ],
        marks=6,
    ))

    prepaid_total = 12000
    prepaid_months = 9
    prepaid_amount = _round_money(prepaid_total * prepaid_months / 12)
    prepaid_table = {
        "heading": "Adjustment analysis: prepaid expense",
        "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
        "rows": [
            [_cell("Insurance paid in advance"), _cell("", editable=True, cell_id="adj-prepaid-amount"), _cell("", editable=True, cell_id="adj-prepaid-dr"), _cell("", editable=True, cell_id="adj-prepaid-cr"), _cell("", editable=True, cell_id="adj-prepaid-is"), _cell("", editable=True, cell_id="adj-prepaid-bs")],
        ],
    }
    pool.append(_make_fill_in_table_question(
        question_type="adjustment_analysis_table",
        prompt=f"{biz} paid insurance of R{prepaid_total:,} for 12 months starting 1 October. The year ends on 31 December. Complete the adjustment analysis table for the prepaid portion.",
        table=prepaid_table,
        correct_map={
            "adj-prepaid-amount": prepaid_amount,
            "adj-prepaid-dr": "Prepaid expenses",
            "adj-prepaid-cr": "Insurance",
            "adj-prepaid-is": "Expense decreases by R" + f"{prepaid_amount:,}",
            "adj-prepaid-bs": "Current asset increases by R" + f"{prepaid_amount:,}",
        },
        derivation_map={
            "adj-prepaid-amount": f"9/12 × R{prepaid_total:,} = R{prepaid_amount:,}",
        },
        cell_hints={
            "adj-prepaid-amount": "Only the unused months are carried forward.",
            "adj-prepaid-dr": "The unused portion becomes a current asset for the next period.",
            "adj-prepaid-cr": "Credit the expense account to remove the prepaid part from this year's expense.",
            "adj-prepaid-is": "If part of an expense belongs to next year, this year's expense becomes smaller.",
            "adj-prepaid-bs": "The unused benefit is carried as an asset, not left inside the expense account.",
        },
        cell_teaching_map={
            "adj-prepaid-amount": _teaching_hint(
                role_in_requirement="This cell records the amount column of the prepaid-expense analysis row.",
                evidence_from_question=f"The unused insurance portion is calculated as R{int(prepaid_amount):,}.",
                rule_or_principle="The analysis row uses the prepaid portion only, because that is the part removed from this year's expense and carried forward.",
                method_or_formula=f"Enter the prepaid amount R{int(prepaid_amount):,}.",
                record_link="This amount must match the debit to Prepaid expenses, the credit to Insurance, and the statement effects shown in the row.",
                how_to_derive="Use the prepaid portion already calculated from the time-apportionment working.",
                transfer_tip="For prepayments, calculate the unused portion once and then reuse that same amount across the whole row.",
            ),
            "adj-prepaid-dr": _teaching_hint(
                role_in_requirement="This cell identifies the asset account debited for the prepaid portion.",
                evidence_from_question="The insurance payment covers months beyond the financial year-end.",
                rule_or_principle="A prepaid expense is a current asset because it represents future economic benefit.",
                method_or_formula="Debit Prepaid expenses and credit Insurance with the unused portion.",
                record_link="This debit creates the current-asset figure that will later appear in the Balance Sheet.",
                how_to_derive="Use Prepaid expenses because the unused insurance belongs to the next accounting period.",
                transfer_tip="If part of a payment still benefits the next period, move that part into an asset account.",
            ),
            "adj-prepaid-cr": _teaching_hint(
                role_in_requirement="This cell identifies the expense account credited for the prepaid adjustment.",
                evidence_from_question=f"The question shows a total insurance payment of R{int(prepaid_total):,}, but only 3 months belong to the current year.",
                rule_or_principle="The expense account must be reduced by the portion that does not belong to the current period.",
                method_or_formula="Credit Insurance with the prepaid amount.",
                record_link="This credit leaves only the used insurance amount in the Income Statement.",
                how_to_derive="Use Insurance because that is the expense account being reduced by the unused portion.",
                transfer_tip="The asset created at year-end is matched by reducing the related expense by the same amount.",
            ),
            "adj-prepaid-is": _teaching_hint(
                role_in_requirement="This cell explains the Income Statement effect of the prepaid-expense adjustment.",
                evidence_from_question=f"R{int(prepaid_amount):,} of the insurance payment relates to the next period rather than the current one.",
                rule_or_principle="Removing a prepaid portion from an expense decreases the current-period expense.",
                method_or_formula="Show a decrease in expense equal to the prepaid amount.",
                record_link="This must agree with the credit posted to Insurance.",
                how_to_derive=f"State that expense decreases by R{int(prepaid_amount):,}.",
                transfer_tip="When part of an expense becomes an asset, the Income Statement effect is usually a decrease in expense.",
            ),
            "adj-prepaid-bs": _teaching_hint(
                role_in_requirement="This cell explains the Balance Sheet effect of the prepaid-expense adjustment.",
                evidence_from_question="The business has paid for cover it will use in the next accounting period.",
                rule_or_principle="Future benefit still controlled by the business is shown as a current asset.",
                method_or_formula="Carry the prepaid amount to current assets.",
                record_link="This effect must match the debit to Prepaid expenses.",
                how_to_derive=f"State that current assets increase by R{int(prepaid_amount):,}.",
                transfer_tip="Prepayments reduce current-period expense and create an asset for the unused benefit.",
            ),
        },
        working_map={
            "adj-prepaid-amount": "Use the prepaid portion first, then carry that same figure through the asset, expense, and statement-effect columns.",
            "adj-prepaid-dr": "The prepaid portion leaves the expense account and is carried forward as an asset for next period.",
            "adj-prepaid-is": "The same amount that becomes an asset reduces this year's insurance expense.",
            "adj-prepaid-bs": "Because the unused portion benefits the next period, it appears as a current asset rather than remaining inside expense.",
        },
        guidelines=[
            "A prepaid expense reduces the expense for the period and creates a current asset.",
        ],
        marks=6,
    ))

    income_advance_amount = _round_money(r.choice([3000, 4500, 6000, 9000]))
    advance_income_table = {
        "heading": "Adjustment analysis: income received in advance",
        "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
        "rows": [
            [_cell("Income received before it is earned"), _cell("", editable=True, cell_id="adj-adv-inc-amount"), _cell("", editable=True, cell_id="adj-adv-inc-dr"), _cell("", editable=True, cell_id="adj-adv-inc-cr"), _cell("", editable=True, cell_id="adj-adv-inc-is"), _cell("", editable=True, cell_id="adj-adv-inc-bs")],
        ],
    }
    pool.append(_make_fill_in_table_question(
        question_type="adjustment_analysis_table",
        prompt=f"A tenant paid R{income_advance_amount:,} rent in advance before year-end. Complete the adjustment analysis table for income received in advance.",
        table=advance_income_table,
        correct_map={
            "adj-adv-inc-amount": income_advance_amount,
            "adj-adv-inc-dr": "Rent income",
            "adj-adv-inc-cr": "Income received in advance",
            "adj-adv-inc-is": "Income decreases by R" + f"{income_advance_amount:,}",
            "adj-adv-inc-bs": "Current liability increases by R" + f"{income_advance_amount:,}",
        },
        derivation_map={
            "adj-adv-inc-amount": f"Use the rent received in advance amount given: R{income_advance_amount:,}.",
        },
        cell_hints={
            "adj-adv-inc-amount": "Use the unearned amount consistently through the whole row.",
            "adj-adv-inc-dr": "Debit the income account to remove the part not yet earned this period.",
            "adj-adv-inc-cr": "The unearned amount becomes a liability until the next period arrives.",
            "adj-adv-inc-is": "Income received too early must reduce this year's earned income.",
            "adj-adv-inc-bs": "Because the business still owes service / occupation time, think liability rather than asset.",
        },
        cell_teaching_map={
            "adj-adv-inc-amount": _teaching_hint(
                role_in_requirement="This cell records the amount column of the income-received-in-advance analysis row.",
                evidence_from_question=f"The question states that rent of R{int(income_advance_amount):,} was received before it was earned.",
                rule_or_principle="The analysis row uses the same unearned amount across the whole row because one advance-income adjustment is being analysed.",
                method_or_formula=f"Enter R{int(income_advance_amount):,} in the amount column.",
                record_link="This amount must match the debit to Rent income, the credit to Income received in advance, and both statement effects in the row.",
                how_to_derive="Copy the unearned amount directly from the prompt before completing the account and effect columns.",
                transfer_tip="For advance-income rows, set the unearned amount first and then use it consistently across the whole row.",
            ),
            "adj-adv-inc-dr": _teaching_hint(
                role_in_requirement="This cell identifies the income account debited for the advance-income adjustment.",
                evidence_from_question=f"R{int(income_advance_amount):,} of rent was received before it was earned.",
                rule_or_principle="Income received before it is earned must be removed from current-period income.",
                method_or_formula="Debit Rent income and credit Income received in advance with the unearned amount.",
                record_link="This debit reduces the current-year income figure in the Income Statement.",
                how_to_derive="Use Rent income because that is the income account that must be reduced by the unearned portion.",
                transfer_tip="If cash was received too early, reduce income now and carry the unearned portion as a liability.",
            ),
            "adj-adv-inc-cr": _teaching_hint(
                role_in_requirement="This cell identifies the liability account credited for the unearned income.",
                evidence_from_question="The rent has been received, but part of it still relates to a future period.",
                rule_or_principle="Income received before it is earned is a current liability until the business delivers the related service / period benefit.",
                method_or_formula="Credit Income received in advance with the unearned amount.",
                record_link="This creates the Balance Sheet liability tied to the reduced rent income.",
                how_to_derive="Because the amount is not yet earned, credit Income received in advance.",
                transfer_tip="Advance income means cash is already in, but the earning process is not yet complete.",
            ),
            "adj-adv-inc-is": _teaching_hint(
                role_in_requirement="This cell explains the Income Statement effect of the advance-income adjustment.",
                evidence_from_question=f"The business received R{int(income_advance_amount):,} before that rent was earned.",
                rule_or_principle="Unearned income must be excluded from current-period income.",
                method_or_formula="Show a decrease in income equal to the amount received in advance.",
                record_link="This effect must agree with the debit posted to Rent income.",
                how_to_derive=f"State that income decreases by R{int(income_advance_amount):,}.",
                transfer_tip="When an income account is debited in an adjustment, current-period income is usually reduced.",
            ),
            "adj-adv-inc-bs": _teaching_hint(
                role_in_requirement="This cell explains the Balance Sheet effect of income received in advance.",
                evidence_from_question="The business still owes the future rental period to the tenant.",
                rule_or_principle="Unearned income is shown as a current liability until it is earned.",
                method_or_formula="Carry the amount received in advance to current liabilities.",
                record_link="This effect must match the credit to Income received in advance.",
                how_to_derive=f"State that current liabilities increase by R{int(income_advance_amount):,}.",
                transfer_tip="Advance receipts create liabilities because the business still owes the future benefit.",
            ),
        },
        working_map={
            "adj-adv-inc-amount": "Use the unearned amount as the fixed figure for the whole row before deciding the income and liability effects.",
            "adj-adv-inc-dr": "This adjustment removes unearned rent from current-year income and creates a matching liability.",
            "adj-adv-inc-is": "Because the amount was received too early, the same figure reduces this year's earned income.",
            "adj-adv-inc-bs": "The same amount that reduces Rent income is carried as Income received in advance in the Balance Sheet.",
        },
        guidelines=[
            "Income received in advance reduces income for the current period and creates a liability.",
        ],
        marks=6,
    ))

    adjustment_journal_prompt_table = {
        "heading": "Year-end adjustment source list",
        "headers": ["Adjustment", "Amount"],
        "rows": [
            [_cell("Rent income earned but not yet received"), _cell(accrued_income)],
            [_cell("Telephone expense owing at year-end"), _cell(accrued_expense_amount)],
            [_cell("Insurance prepaid portion"), _cell(prepaid_amount)],
            [_cell("Rent income received in advance"), _cell(income_advance_amount)],
        ],
    }
    adjustment_journal_table = {
        "heading": "General Journal for year-end adjustments",
        "headers": ["Date", "Details", "Debit", "Credit"],
        "rows": [
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="adj-wf-inc-dr-details"), _cell("", editable=True, cell_id="adj-wf-inc-dr-amount"), _cell("")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="adj-wf-inc-cr-details"), _cell(""), _cell("", editable=True, cell_id="adj-wf-inc-cr-amount")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="adj-wf-exp-dr-details"), _cell("", editable=True, cell_id="adj-wf-exp-dr-amount"), _cell("")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="adj-wf-exp-cr-details"), _cell(""), _cell("", editable=True, cell_id="adj-wf-exp-cr-amount")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="adj-wf-pre-dr-details"), _cell("", editable=True, cell_id="adj-wf-pre-dr-amount"), _cell("")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="adj-wf-pre-cr-details"), _cell(""), _cell("", editable=True, cell_id="adj-wf-pre-cr-amount")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="adj-wf-adv-dr-details"), _cell("", editable=True, cell_id="adj-wf-adv-dr-amount"), _cell("")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="adj-wf-adv-cr-details"), _cell(""), _cell("", editable=True, cell_id="adj-wf-adv-cr-amount")],
        ],
    }
    adjustment_journal_correct_map = {
        "adj-wf-inc-dr-details": "Accrued income",
        "adj-wf-inc-dr-amount": accrued_income,
        "adj-wf-inc-cr-details": "Rent income",
        "adj-wf-inc-cr-amount": accrued_income,
        "adj-wf-exp-dr-details": "Telephone",
        "adj-wf-exp-dr-amount": accrued_expense_amount,
        "adj-wf-exp-cr-details": "Accrued expenses",
        "adj-wf-exp-cr-amount": accrued_expense_amount,
        "adj-wf-pre-dr-details": "Prepaid expenses",
        "adj-wf-pre-dr-amount": prepaid_amount,
        "adj-wf-pre-cr-details": "Insurance",
        "adj-wf-pre-cr-amount": prepaid_amount,
        "adj-wf-adv-dr-details": "Rent income",
        "adj-wf-adv-dr-amount": income_advance_amount,
        "adj-wf-adv-cr-details": "Income received in advance",
        "adj-wf-adv-cr-amount": income_advance_amount,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="journal",
        prompt="Use the year-end adjustment source list to prepare all the General Journal entries for the adjustments shown. Record the entries for accrued income, accrued expense, prepaid expense, and income received in advance.",
        prompt_table=adjustment_journal_prompt_table,
        table=adjustment_journal_table,
        correct_map=adjustment_journal_correct_map,
        derivation_map={
            "adj-wf-inc-dr-amount": f"Use the accrued income amount from the source list: R{int(accrued_income):,}.",
            "adj-wf-exp-dr-amount": f"Use the accrued expense amount from the source list: R{int(accrued_expense_amount):,}.",
            "adj-wf-pre-dr-amount": f"Use the prepaid expense amount already determined: R{int(prepaid_amount):,}.",
            "adj-wf-adv-dr-amount": f"Use the income received in advance amount from the source list: R{int(income_advance_amount):,}.",
            "adj-wf-inc-cr-amount": f"Credit Rent income with the same accrued amount: R{int(accrued_income):,}.",
            "adj-wf-exp-cr-amount": f"Credit Accrued expenses with the same unpaid amount: R{int(accrued_expense_amount):,}.",
            "adj-wf-pre-cr-amount": f"Credit Insurance with the prepaid amount removed from this year: R{int(prepaid_amount):,}.",
            "adj-wf-adv-cr-amount": f"Credit Income received in advance with the unearned amount: R{int(income_advance_amount):,}.",
        },
        cell_hints={
            "adj-wf-inc-dr-details": "Amounts still receivable are debited to an asset account.",
            "adj-wf-inc-cr-details": "The related income account is credited because the income has already been earned.",
            "adj-wf-exp-dr-details": "The unpaid expense still belongs to this year, so debit the expense account.",
            "adj-wf-exp-cr-details": "Outstanding expenses create a liability at year-end.",
            "adj-wf-pre-dr-details": "A prepaid portion becomes an asset carried forward to the next period.",
            "adj-wf-pre-cr-details": "Credit the expense account to remove the part that belongs to the next period.",
            "adj-wf-adv-dr-details": "Income received too early must be removed from this year's earned income.",
            "adj-wf-adv-cr-details": "Income received before it is earned becomes a liability.",
            "adj-wf-inc-dr-amount": "Use the accrued income amount from the source list.",
            "adj-wf-inc-cr-amount": "Repeat the same accrued income amount on the credit side.",
            "adj-wf-exp-dr-amount": "Use the unpaid expense amount from the source list.",
            "adj-wf-exp-cr-amount": "Repeat the same unpaid expense amount on the credit side.",
            "adj-wf-pre-dr-amount": "Use the prepaid amount already determined.",
            "adj-wf-pre-cr-amount": "Repeat the same prepaid amount on the credit side.",
            "adj-wf-adv-dr-amount": "Use the income received in advance amount from the source list.",
            "adj-wf-adv-cr-amount": "Repeat the same unearned amount on the credit side.",
        },
        cell_teaching_map={
            "adj-wf-inc-dr-details": _teaching_hint(
                role_in_requirement="This cell gives the debit account for the accrued income journal entry.",
                evidence_from_question=f"The source list says rent income of R{int(accrued_income):,} has been earned but not yet received.",
                rule_or_principle="Income that is still receivable at year-end is recorded as an accrued income asset.",
                method_or_formula="Debit Accrued income and credit Rent income with the same accrued amount.",
                record_link="This debit creates the current-asset figure that will later appear in the Balance Sheet.",
                how_to_derive="Use Accrued income because the business now has a right to receive the amount.",
                transfer_tip="When the business has earned income but not yet received cash, think asset up and income up.",
            ),
            "adj-wf-inc-cr-details": _teaching_hint(
                role_in_requirement="This cell gives the credit account for the accrued income journal entry.",
                evidence_from_question="The rent income belongs to the current period even though the cash has not yet been collected.",
                rule_or_principle="Income earned in the current period must be credited to the relevant income account.",
                method_or_formula="Credit Rent income with the accrued amount still owing.",
                record_link="This credit increases the current-period income figure that later appears in the Income Statement.",
                how_to_derive="Use Rent income because that is the nominal income account affected by the accrual.",
                transfer_tip="For accrued income, pair the receivable asset on the debit side with the earned income account on the credit side.",
            ),
            "adj-wf-exp-dr-details": _teaching_hint(
                role_in_requirement="This cell gives the debit account for the accrued expense journal entry.",
                evidence_from_question=f"Telephone expense of R{int(accrued_expense_amount):,} is still owing at year-end.",
                rule_or_principle="An expense incurred but not yet paid must still be recognised in the current period.",
                method_or_formula="Debit Telephone and credit Accrued expenses with the unpaid amount.",
                record_link="This debit increases the current-period expense figure that later appears in the Income Statement.",
                how_to_derive="Use Telephone because that is the expense account being increased by the accrual.",
                transfer_tip="If the cost belongs to this year, debit the expense first, then find the matching payable account.",
            ),
            "adj-wf-exp-cr-details": _teaching_hint(
                role_in_requirement="This cell gives the credit account for the accrued expense journal entry.",
                evidence_from_question=f"Telephone expense of R{int(accrued_expense_amount):,} is still owing at year-end.",
                rule_or_principle="An expense that has been incurred but not yet paid creates a current liability.",
                method_or_formula="Credit Accrued expenses with the same amount used to debit Telephone.",
                record_link="This liability is later carried to current liabilities in the Balance Sheet.",
                how_to_derive="Credit Accrued expenses because the business owes this amount at year-end.",
                transfer_tip="If cash has not yet been paid for an expense already incurred, expect a liability account on the credit side.",
            ),
            "adj-wf-pre-dr-details": _teaching_hint(
                role_in_requirement="This cell gives the debit account for the prepaid expense journal entry.",
                evidence_from_question=f"The prepaid insurance amount is R{int(prepaid_amount):,}, meaning part of the payment relates to the next period.",
                rule_or_principle="A prepaid expense is a current asset because it represents future economic benefit.",
                method_or_formula="Debit Prepaid expenses and credit Insurance with the unused portion.",
                record_link="This debit creates the current-asset figure that will later appear in the Balance Sheet.",
                how_to_derive="Use Prepaid expenses because the unused insurance belongs to the next accounting period.",
                transfer_tip="If part of a payment still benefits the next period, move that part into an asset account.",
            ),
            "adj-wf-pre-cr-details": _teaching_hint(
                role_in_requirement="This cell gives the credit account for the prepaid expense journal entry.",
                evidence_from_question=f"The prepaid insurance amount is R{int(prepaid_amount):,}, meaning part of the payment relates to the next period.",
                rule_or_principle="The expense account must be reduced by the portion that does not belong to the current period.",
                method_or_formula="Credit Insurance with the prepaid amount.",
                record_link="This credit reduces the current-period expense figure that later appears in the Income Statement.",
                how_to_derive="Use Insurance because that is the expense account being reduced by the unused portion.",
                transfer_tip="The asset created at year-end is matched by reducing the related expense by the same amount.",
            ),
            "adj-wf-adv-dr-details": _teaching_hint(
                role_in_requirement="This cell gives the debit account for the income received in advance journal entry.",
                evidence_from_question=f"The source list shows rent income received in advance of R{int(income_advance_amount):,}.",
                rule_or_principle="Income received before it is earned must be removed from current-period income.",
                method_or_formula="Debit Rent income and credit Income received in advance with the unearned amount.",
                record_link="This debit reduces the current-period income figure that later appears in the Income Statement.",
                how_to_derive="Use Rent income because that is the income account that must be reduced by the unearned portion.",
                transfer_tip="If cash was received too early, reduce income now and carry the unearned portion as a liability.",
            ),
            "adj-wf-adv-cr-details": _teaching_hint(
                role_in_requirement="This cell gives the credit account for the income received in advance journal entry.",
                evidence_from_question=f"The source list shows rent income received in advance of R{int(income_advance_amount):,}.",
                rule_or_principle="Income received before it is earned is a liability until the service period arrives.",
                method_or_formula="Credit Income received in advance with the same unearned amount used to debit Rent income.",
                record_link="This liability is later carried to current liabilities in the Balance Sheet.",
                how_to_derive="Credit Income received in advance with the unearned portion.",
                transfer_tip="When cash is received too early, reduce the income for this period and create a liability.",
            ),
            "adj-wf-inc-dr-amount": _teaching_hint(
                role_in_requirement="This cell records the debit amount for the accrued-income journal entry in the grouped workflow.",
                evidence_from_question=f"The source list gives rent income earned but not yet received as R{int(accrued_income):,}.",
                rule_or_principle="The exact accrued-income amount is used on both sides of the journal entry because one receivable adjustment is being recorded.",
                method_or_formula=f"Debit Accrued income with R{int(accrued_income):,}.",
                record_link="This amount must match the credit to Rent income and later appear in the accrued-income asset carry-through.",
                how_to_derive="Read the accrued-income amount directly from the source list and enter it on the debit side.",
                transfer_tip="When the source list gives the adjustment amount directly, use it as the fixed figure for both sides of that journal entry.",
            ),
            "adj-wf-inc-cr-amount": _teaching_hint(
                role_in_requirement="This cell records the matching credit amount for the accrued-income journal entry in the grouped workflow.",
                evidence_from_question=f"The same accrued-income amount of R{int(accrued_income):,} must be used on both sides of the first entry.",
                rule_or_principle="A journal entry balances by repeating the same amount on the opposite side for the same adjustment.",
                method_or_formula=f"Credit Rent income with R{int(accrued_income):,}.",
                record_link="This amount must equal the debit to Accrued income and increases the current-period Rent income figure.",
                how_to_derive="Copy the same accrued-income amount from the debit side of the first entry.",
                transfer_tip="Complete one journal row-pair at a time: set the source amount first, then mirror it on the opposite side.",
            ),
            "adj-wf-exp-dr-amount": _teaching_hint(
                role_in_requirement="This cell records the debit amount for the accrued-expense journal entry in the grouped workflow.",
                evidence_from_question=f"The source list gives telephone expense owing at year-end as R{int(accrued_expense_amount):,}.",
                rule_or_principle="The full outstanding expense amount is recognised in the current period and used on both sides of the accrual entry.",
                method_or_formula=f"Debit Telephone with R{int(accrued_expense_amount):,}.",
                record_link="This amount must match the credit to Accrued expenses and later increase the Telephone expense carried to the Income Statement.",
                how_to_derive="Read the outstanding expense amount directly from the source list and enter it on the debit side.",
                transfer_tip="For grouped accrual workflows, use each source-list amount exactly as given before moving to the next entry.",
            ),
            "adj-wf-exp-cr-amount": _teaching_hint(
                role_in_requirement="This cell records the matching credit amount for the accrued-expense journal entry in the grouped workflow.",
                evidence_from_question=f"The accrued-expense row uses the same unpaid amount of R{int(accrued_expense_amount):,} on both sides.",
                rule_or_principle="Accrual journal entries balance by repeating the same adjustment amount on the opposite side.",
                method_or_formula=f"Credit Accrued expenses with R{int(accrued_expense_amount):,}.",
                record_link="This amount must equal the Telephone debit and later appear as the accrued-expense liability in the Balance Sheet.",
                how_to_derive="Copy the same unpaid expense amount from the debit side of the second entry.",
                transfer_tip="Once you know the correct accounts, check that the same source amount appears on both sides of the accrual row.",
            ),
            "adj-wf-pre-dr-amount": _teaching_hint(
                role_in_requirement="This cell records the debit amount for the prepaid-expense journal entry in the grouped workflow.",
                evidence_from_question=f"The prepaid insurance portion has already been determined as R{int(prepaid_amount):,}.",
                rule_or_principle="Only the prepaid portion is transferred out of the expense account and used on both sides of the journal entry.",
                method_or_formula=f"Debit Prepaid expenses with R{int(prepaid_amount):,}.",
                record_link="This amount must match the credit to Insurance and later appear as the prepaid asset in the Balance Sheet.",
                how_to_derive="Use the prepaid portion already calculated from the working and enter it on the debit side.",
                transfer_tip="For prepayments, carry the already-worked prepaid portion straight into the journal rather than recalculating it again.",
            ),
            "adj-wf-pre-cr-amount": _teaching_hint(
                role_in_requirement="This cell records the matching credit amount for the prepaid-expense journal entry in the grouped workflow.",
                evidence_from_question=f"The same prepaid amount of R{int(prepaid_amount):,} is removed from Insurance on the credit side.",
                rule_or_principle="The prepaid-entry credit amount mirrors the debit amount because one unused portion is being transferred out of expense.",
                method_or_formula=f"Credit Insurance with R{int(prepaid_amount):,}.",
                record_link="This amount must equal the debit to Prepaid expenses and reduce the current-period Insurance expense by the same amount.",
                how_to_derive="Copy the prepaid amount from the debit side of the third entry to the credit side.",
                transfer_tip="When part of an expense is carried forward, mirror the prepaid amount exactly on the credit side of the related expense account.",
            ),
            "adj-wf-adv-dr-amount": _teaching_hint(
                role_in_requirement="This cell records the debit amount for the income-received-in-advance journal entry in the grouped workflow.",
                evidence_from_question=f"The source list gives rent income received in advance as R{int(income_advance_amount):,}.",
                rule_or_principle="The full unearned amount is removed from current-period income and used on both sides of the advance-income entry.",
                method_or_formula=f"Debit Rent income with R{int(income_advance_amount):,}.",
                record_link="This amount must match the credit to Income received in advance and reduce current-period Rent income by the same amount.",
                how_to_derive="Read the unearned rent amount from the source list and enter it on the debit side.",
                transfer_tip="For income received in advance, use the unearned amount exactly as given before deciding the liability side.",
            ),
            "adj-wf-adv-cr-amount": _teaching_hint(
                role_in_requirement="This cell records the matching credit amount for the income-received-in-advance journal entry in the grouped workflow.",
                evidence_from_question=f"The same unearned amount of R{int(income_advance_amount):,} is carried to the liability side of the fourth entry.",
                rule_or_principle="The advance-income journal entry balances by repeating the same unearned amount on the credit side.",
                method_or_formula=f"Credit Income received in advance with R{int(income_advance_amount):,}.",
                record_link="This amount must equal the debit to Rent income and later appear as the liability carried to the Balance Sheet.",
                how_to_derive="Copy the same unearned amount from the debit side of the fourth entry.",
                transfer_tip="After identifying an advance-income amount, mirror it on the liability side to complete the balanced journal entry.",
            ),
        },
        working_map={
            "adj-wf-inc-dr-details": "The accrued-income row increases this year's Rent income and creates a matching receivable.",
            "adj-wf-exp-dr-details": "The accrued-expense row increases this year's Telephone expense and creates a matching payable.",
            "adj-wf-pre-dr-details": "The prepaid-expense row moves the unused insurance portion out of expense and into an asset.",
            "adj-wf-adv-dr-details": "The advance-income row removes unearned rent from current-year income and creates a matching liability.",
            "adj-wf-inc-dr-amount": "Use the accrued income amount from the source list as the fixed figure for the whole first entry.",
            "adj-wf-inc-cr-amount": "Mirror the same accrued income amount on the credit side of the first entry.",
            "adj-wf-exp-dr-amount": "Use the outstanding expense amount as the fixed figure for the second entry.",
            "adj-wf-exp-cr-amount": "Mirror the same unpaid expense amount on the credit side of the second entry.",
            "adj-wf-pre-dr-amount": "Use the prepaid portion already worked out, then carry it to both sides of the third entry.",
            "adj-wf-pre-cr-amount": "Mirror the prepaid amount on the expense-account credit side of the third entry.",
            "adj-wf-adv-dr-amount": "Use the unearned rent amount as the fixed figure for the fourth entry.",
            "adj-wf-adv-cr-amount": "Mirror the same unearned amount on the liability credit side of the fourth entry.",
        },
        guidelines=[
            "Use the source-list amount consistently on both sides of each journal entry.",
            "Record accruals and prepayments with the correct asset, liability, income, and expense accounts.",
            "Prepare a separate two-line journal entry for each adjustment shown.",
        ],
        marks=16,
    ), "adjustment_journal_workflow_fill", expected_cells=16, cell_expectations=adjustment_journal_correct_map))

    adjustment_matrix_prompt_table = {
        "heading": "Year-end adjustment source list",
        "headers": ["Adjustment", "Amount"],
        "rows": [
            [_cell("Rent income earned but not yet received"), _cell(accrued_income)],
            [_cell("Telephone expense owing at year-end"), _cell(accrued_expense_amount)],
            [_cell("Insurance prepaid portion"), _cell(prepaid_amount)],
            [_cell("Rent income received in advance"), _cell(income_advance_amount)],
        ],
    }
    adjustment_matrix_table = {
        "heading": "Adjustment analysis matrix",
        "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Accounting equation effect", "Reverse next period?"],
        "rows": [
            [_cell("Accrued income"), _cell("", editable=True, cell_id="adj-mx-inc-amount"), _cell("", editable=True, cell_id="adj-mx-inc-dr"), _cell("", editable=True, cell_id="adj-mx-inc-cr"), _cell("", editable=True, cell_id="adj-mx-inc-eq"), _cell("", editable=True, cell_id="adj-mx-inc-rev")],
            [_cell("Accrued expense"), _cell("", editable=True, cell_id="adj-mx-exp-amount"), _cell("", editable=True, cell_id="adj-mx-exp-dr"), _cell("", editable=True, cell_id="adj-mx-exp-cr"), _cell("", editable=True, cell_id="adj-mx-exp-eq"), _cell("", editable=True, cell_id="adj-mx-exp-rev")],
            [_cell("Prepaid expense"), _cell("", editable=True, cell_id="adj-mx-pre-amount"), _cell("", editable=True, cell_id="adj-mx-pre-dr"), _cell("", editable=True, cell_id="adj-mx-pre-cr"), _cell("", editable=True, cell_id="adj-mx-pre-eq"), _cell("", editable=True, cell_id="adj-mx-pre-rev")],
            [_cell("Income received in advance"), _cell("", editable=True, cell_id="adj-mx-adv-amount"), _cell("", editable=True, cell_id="adj-mx-adv-dr"), _cell("", editable=True, cell_id="adj-mx-adv-cr"), _cell("", editable=True, cell_id="adj-mx-adv-eq"), _cell("", editable=True, cell_id="adj-mx-adv-rev")],
        ],
    }
    adjustment_matrix_correct_map = {
        "adj-mx-inc-amount": accrued_income,
        "adj-mx-inc-dr": "Accrued income",
        "adj-mx-inc-cr": "Rent income",
        "adj-mx-inc-eq": "Assets increase; owner's equity increases",
        "adj-mx-inc-rev": "Yes",
        "adj-mx-exp-amount": accrued_expense_amount,
        "adj-mx-exp-dr": "Telephone",
        "adj-mx-exp-cr": "Accrued expenses",
        "adj-mx-exp-eq": "Liabilities increase; owner's equity decreases",
        "adj-mx-exp-rev": "Yes",
        "adj-mx-pre-amount": prepaid_amount,
        "adj-mx-pre-dr": "Prepaid expenses",
        "adj-mx-pre-cr": "Insurance",
        "adj-mx-pre-eq": "Assets increase; owner's equity increases",
        "adj-mx-pre-rev": "Yes",
        "adj-mx-adv-amount": income_advance_amount,
        "adj-mx-adv-dr": "Rent income",
        "adj-mx-adv-cr": "Income received in advance",
        "adj-mx-adv-eq": "Liabilities increase; owner's equity decreases",
        "adj-mx-adv-rev": "Yes",
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="adjustment_analysis_table",
        prompt="Use the year-end adjustment source list to complete the adjustment analysis matrix. For each adjustment, show the amount, the debit account, the credit account, the accounting equation effect, and whether it is normally reversed on the first day of the next period.",
        prompt_table=adjustment_matrix_prompt_table,
        table=adjustment_matrix_table,
        correct_map=adjustment_matrix_correct_map,
        derivation_map={
            "adj-mx-inc-amount": f"Use the accrued income amount from the source list: R{int(accrued_income):,}.",
            "adj-mx-exp-amount": f"Use the accrued expense amount from the source list: R{int(accrued_expense_amount):,}.",
            "adj-mx-pre-amount": f"Use the prepaid amount already determined: R{int(prepaid_amount):,}.",
            "adj-mx-adv-amount": f"Use the income received in advance amount from the source list: R{int(income_advance_amount):,}.",
        },
        cell_hints={
            "adj-mx-inc-eq": "If income increases, owner's equity also increases through profit.",
            "adj-mx-exp-eq": "If an expense increases, owner's equity decreases through profit.",
            "adj-mx-pre-eq": "A prepaid expense creates an asset and removes part of the expense from this year.",
            "adj-mx-adv-eq": "Income received in advance creates a liability and reduces this year's income.",
            "adj-mx-inc-rev": "These accrual and prepayment adjustments are usually reversed at the start of the next period in this workflow.",
            "adj-mx-exp-rev": "In this workflow, the year-end accrual is normally reversed on the first day of the next period.",
            "adj-mx-pre-rev": "This workflow expects the standard first-day reversal treatment for these adjustments.",
            "adj-mx-adv-rev": "This workflow treats the unearned-income adjustment as one that is normally reversed next period.",
        },
        cell_teaching_map={
            "adj-mx-inc-eq": _teaching_hint(
                role_in_requirement="This cell explains the accounting-equation effect of accrued income.",
                evidence_from_question=f"The business is owed R{int(accrued_income):,} rent income at year-end, so both the income account and an asset are affected.",
                rule_or_principle="When income increases, owner's equity increases through profit; when an amount is receivable, assets also increase.",
                method_or_formula="Accrued income means Assets increase and owner's equity increases.",
                record_link="This equation effect must match the double entry Dr Accrued income / Cr Rent income.",
                how_to_derive="Identify the asset created and then link the increased income to owner's equity.",
                transfer_tip="For equation effects, ask which asset, liability, or owner's equity category changes after the double entry.",
            ),
            "adj-mx-exp-eq": _teaching_hint(
                role_in_requirement="This cell explains the accounting-equation effect of an accrued expense.",
                evidence_from_question=f"Telephone expense of R{int(accrued_expense_amount):,} is still owing, so both an expense and a payable are created.",
                rule_or_principle="When expenses increase, owner's equity decreases through profit; when an amount is still payable, liabilities increase.",
                method_or_formula="Accrued expense means Liabilities increase and owner's equity decreases.",
                record_link="This equation effect must match the double entry Dr Telephone / Cr Accrued expenses.",
                how_to_derive="Identify the liability created and then link the increased expense to the decrease in owner's equity.",
                transfer_tip="Expense up plus liability up is the usual pattern for outstanding-expense adjustments.",
            ),
            "adj-mx-pre-eq": _teaching_hint(
                role_in_requirement="This cell explains the accounting-equation effect of a prepaid expense.",
                evidence_from_question=f"The prepaid insurance amount is R{int(prepaid_amount):,}, which is removed from this year's expense and carried forward as an asset.",
                rule_or_principle="Removing part of an expense increases owner's equity through profit, and the prepaid portion becomes an asset.",
                method_or_formula="Prepaid expense means Assets increase and owner's equity increases.",
                record_link="This equation effect must match the double entry Dr Prepaid expenses / Cr Insurance.",
                how_to_derive="Show that assets increase while owner's equity increases because the expense for this period becomes smaller.",
                transfer_tip="If an adjustment turns part of an expense into an asset, the asset side increases and profit improves.",
            ),
            "adj-mx-adv-eq": _teaching_hint(
                role_in_requirement="This cell explains the accounting-equation effect of income received in advance.",
                evidence_from_question=f"Rent income of R{int(income_advance_amount):,} was received before it was earned, so a liability replaces part of the income.",
                rule_or_principle="Removing unearned income decreases owner's equity through profit, while the amount received in advance is shown as a liability.",
                method_or_formula="Income received in advance means Liabilities increase and owner's equity decreases.",
                record_link="This equation effect must match the double entry Dr Rent income / Cr Income received in advance.",
                how_to_derive="Identify the liability created and then link the reduced income to the decrease in owner's equity.",
                transfer_tip="When income is received too early, the Balance Sheet side rises as a liability while current-period profit falls.",
            ),
            "adj-mx-inc-rev": _teaching_hint(
                role_in_requirement="This cell states whether the accrued-income adjustment is normally reversed in the next period in this workflow.",
                evidence_from_question="The matrix specifically asks for the normal reversal treatment used in this adjustment workflow.",
                rule_or_principle="Accrual and prepayment adjustments in this authored workflow are normally reversed on the first day of the next period.",
                method_or_formula="Enter Yes for the normal reversal treatment in this matrix.",
                record_link="This matches the reversal-oriented workflow pattern used elsewhere in the adjustment generator.",
                how_to_derive="Follow the workflow rule given by the exercise set: these adjustments are normally reversed next period.",
                transfer_tip="Answer the reversal column according to the workflow convention being taught in the question set, not from a different classroom method.",
            ),
        },
        working_map={
            "adj-mx-inc-eq": "Work row by row: identify the double entry first, then translate it into asset/liability and owner's-equity language.",
            "adj-mx-exp-eq": "For each adjustment, connect the Balance Sheet side to the profit effect before writing the accounting-equation wording.",
            "adj-mx-inc-rev": "Complete the reversal column last, after you have identified what kind of adjustment each row represents.",
        },
        guidelines=[
            "Use the amount given for each adjustment consistently across the amount and double-entry columns.",
            "For the accounting equation effect, connect the Balance Sheet side and the effect on owner's equity through profit.",
            "State whether each adjustment is normally reversed at the start of the next period.",
        ],
        marks=20,
    ), "adjustment_analysis_matrix_fill", expected_cells=20, cell_expectations=adjustment_matrix_correct_map))

    reversal_pool = _gen_reversal_adjustments(
        r=r,
        biz=biz,
        context={
            "accrued_income": accrued_income,
            "accrued_expense_amount": accrued_expense_amount,
            "prepaid_total": prepaid_total,
            "prepaid_months": prepaid_months,
            "prepaid_amount": prepaid_amount,
            "income_advance_amount": income_advance_amount,
        },
    )

    pool.extend(reversal_pool)
    pool.append(_with_validation(_make_typed(
        prompt="Explain why a business makes year-end adjustments. Refer to GAAP.",
        sample_answer="Year-end adjustments ensure that only income earned during the period and expenses incurred during the same period are included in the financial statements. This complies with the matching principle (GAAP) — expenses and income must be matched to the period in which they occur, giving a true and fair view of the business's performance.",
        grading_rubric=["matching principle / GAAP", "income earned in period", "expenses incurred in period", "true and fair view"],
    ), "adjustments_why_typed", minimum_parts=1))

    return pool

