from __future__ import annotations

import random
from typing import Any, Dict, List

from .....sole_trader.names import pick_business_name as _pick_business_name
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
def _gen_interest_adjustments(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    biz = _pick_business_name(r=r)

    loan_scenarios = [
        {
            "loan_balance": 120000,
            "rate": 12,
            "months": 3,
            "base_expense": 9000,
            "year_end_date": "28 Feb 2026",
            "next_date": "1 Mar 2026",
        },
        {
            "loan_balance": 150000,
            "rate": 10,
            "months": 4,
            "base_expense": 12500,
            "year_end_date": "31 Dec 2026",
            "next_date": "1 Jan 2027",
        },
    ]
    for scenario in loan_scenarios:
        accrued_amount = _round_money(float(scenario["loan_balance"]) * float(scenario["rate"]) / 100 * float(scenario["months"]) / 12)
        adjusted_interest = _round_money(float(scenario["base_expense"]) + float(accrued_amount))
        pool.append(_with_validation(_make_calc(
            prompt=f"{biz} has a loan balance of R{int(scenario['loan_balance']):,} at {int(scenario['rate']):,}% per annum. Interest for the last {int(scenario['months'])} month(s) of the year has not yet been paid.\n\nCalculate the accrued interest on the loan.",
            correct_answer=accrued_amount,
            working_formula=f"Accrued interest = R{int(scenario['loan_balance']):,} × {int(scenario['rate'])}% × {int(scenario['months'])}/12",
            formula_hint="Accrued interest = loan balance × rate × months/12",
        ), "interest_on_loan_calc", loan_balance=scenario["loan_balance"], rate=scenario["rate"], months=scenario["months"]))

        loan_prompt_table = {
            "heading": "Interest on loan source note",
            "headers": ["Item", "Amount / detail"],
            "rows": [
                [_cell("Loan balance"), _cell(scenario["loan_balance"])],
                [_cell("Interest rate"), _cell(f"{int(scenario['rate'])}% p.a.")],
                [_cell("Months outstanding"), _cell(int(scenario["months"]))],
                [_cell("Interest on loan already in the Trial Balance"), _cell(scenario["base_expense"])],
            ],
        }
        loan_journal_table = {
            "heading": "General Journal: interest on loan adjustment",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="int-loan-j-dr-details"), _cell("", editable=True, cell_id="int-loan-j-dr-amount"), _cell("")],
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="int-loan-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="int-loan-j-cr-amount")],
            ],
        }
        loan_journal_correct_map = {
            "int-loan-j-dr-details": "Interest on loan",
            "int-loan-j-dr-amount": accrued_amount,
            "int-loan-j-cr-details": "Accrued expenses",
            "int-loan-j-cr-amount": accrued_amount,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=f"{biz} still owes interest on loan for the last {int(scenario['months'])} month(s) of the year. Prepare the General Journal entry dated {scenario['year_end_date']} to record the year-end interest adjustment.",
            prompt_table=loan_prompt_table,
            table=loan_journal_table,
            correct_map=loan_journal_correct_map,
            derivation_map={
                "int-loan-j-dr-amount": f"Accrued interest = R{int(scenario['loan_balance']):,} × {int(scenario['rate'])}% × {int(scenario['months'])}/12 = R{int(accrued_amount):,}.",
                "int-loan-j-cr-amount": f"Use the same accrued-interest amount on the credit side: R{int(accrued_amount):,}.",
            },
            cell_hints={
                "int-loan-j-dr-details": "Outstanding loan interest is an expense for this year, so debit the interest expense account.",
                "int-loan-j-cr-details": "The unpaid interest is a liability at year-end.",
                "int-loan-j-dr-amount": "Calculate the accrued interest using loan balance × rate × months/12.",
                "int-loan-j-cr-amount": "Use the same accrued-interest amount on the credit side.",
            },
            cell_teaching_map={
                "int-loan-j-dr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the debit account for the accrued interest adjustment.",
                    evidence_from_question="The prompt says interest for the final months of the year is still owing.",
                    rule_or_principle="An expense incurred but not yet paid is debited to the expense account and credited to a liability account.",
                    method_or_formula="Debit Interest on loan and credit Accrued expenses with the same accrued-interest amount.",
                    record_link="This same adjustment will later increase the Interest on loan figure in Profit and Loss and create an accrued-expense liability.",
                    how_to_derive="Because the expense belongs to the current year, debit Interest on loan.",
                    transfer_tip="When the business still owes an expense at year-end, think expense up and current liability up.",
                ),
                "int-loan-j-cr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the liability account credited for unpaid interest.",
                    evidence_from_question="The interest has been incurred but not yet paid by year-end.",
                    rule_or_principle="Outstanding expenses are current liabilities until they are paid.",
                    method_or_formula="Credit Accrued expenses with the same amount used to debit Interest on loan.",
                    record_link="The credited liability will appear in the Balance Sheet / statement extracts as Accrued expenses.",
                    how_to_derive="Because the amount is still payable, credit Accrued expenses.",
                    transfer_tip="If cash has not left the business yet, the credit side is often a payable / accrued-expense account.",
                ),
                "int-loan-j-dr-amount": _teaching_hint(
                    role_in_requirement="This cell calculates the debit amount for the accrued loan-interest adjustment.",
                    evidence_from_question=f"The source note gives a loan balance of R{int(scenario['loan_balance']):,} at {int(scenario['rate'])}% p.a. for {int(scenario['months'])} month(s) still outstanding.",
                    rule_or_principle="An expense accrual is measured for the part of the year already incurred, using the annual rate and time outstanding.",
                    method_or_formula=f"R{int(scenario['loan_balance']):,} × {int(scenario['rate'])}% × {int(scenario['months'])}/12 = R{int(accrued_amount):,}.",
                    record_link="This amount must match the credit to Accrued expenses and later increase the Interest on loan balance in the adjusted records.",
                    how_to_derive="Apply the accrual formula to the loan balance, annual rate, and months owing.",
                    transfer_tip="When a loan-interest accrual gives capital, rate, and months, calculate the amount first and then mirror it on the other side of the journal.",
                ),
                "int-loan-j-cr-amount": _teaching_hint(
                    role_in_requirement="This cell records the matching credit amount for the loan-interest accrual.",
                    evidence_from_question=f"The same accrued-interest amount of R{int(accrued_amount):,} must be used on both sides of this journal entry.",
                    rule_or_principle="A journal entry balances by repeating the same amount on the opposite side for the same adjustment.",
                    method_or_formula=f"Credit amount = debit amount = R{int(accrued_amount):,}.",
                    record_link="This amount must equal the debit to Interest on loan and becomes the Accrued expenses liability carried through later.",
                    how_to_derive="Copy the calculated accrued-interest amount from the debit side to the credit side.",
                    transfer_tip="Complete the calculation once, then mirror the same figure on the opposite side instead of recalculating it.",
                ),
            },
            working_map={
                "int-loan-j-dr-details": "This entry increases the current-year loan-interest expense to its full adjusted amount.",
                "int-loan-j-cr-details": "The same amount becomes a year-end liability until it is paid in the next period.",
                "int-loan-j-dr-amount": "Calculate the accrued-interest amount first, then use that single figure for the whole journal row.",
                "int-loan-j-cr-amount": "Mirror the debit amount on the credit side so the expense-accrual journal balances.",
            },
            guidelines=[
                "Calculate the accrued interest first.",
                "Use the same amount on both sides of the journal entry.",
                "Treat the unpaid amount as a current liability at year-end.",
            ],
            marks=8,
        ), "interest_on_loan_journal_fill", expected_cells=4, cell_expectations=loan_journal_correct_map))

        loan_ledger_prompt_tables = [
            {
                "heading": "General Journal entries to post",
                "headers": ["Date", "Details", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("Interest on loan"), _cell(accrued_amount), _cell("")],
                    [_cell(scenario["year_end_date"]), _cell("Accrued expenses"), _cell(""), _cell(accrued_amount)],
                    [_cell(scenario["year_end_date"]), _cell("Profit and Loss"), _cell(adjusted_interest), _cell("")],
                    [_cell(scenario["year_end_date"]), _cell("Interest on loan"), _cell(""), _cell(adjusted_interest)],
                ],
            },
            {
                "heading": "Opening balance information",
                "headers": ["Account", "Balance on first day of the year"],
                "rows": [
                    [_cell("Interest on loan"), _cell(scenario["base_expense"])],
                ],
            },
        ]
        loan_ledger_tables = [
            {
                "heading": "Interest on loan account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["next_date"]), _cell("", editable=True, cell_id="int-loan-l-open-details"), _cell("Balance"), _cell("", editable=True, cell_id="int-loan-l-open-amount"), _cell("")],
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="int-loan-l-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="int-loan-l-dr-amount"), _cell("")],
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="int-loan-l-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="int-loan-l-cr-amount")],
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="int-loan-l-total-details"), _cell(""), _cell("", editable=True, cell_id="int-loan-l-total-debit"), _cell("", editable=True, cell_id="int-loan-l-total-credit")],
                ],
            },
            {
                "heading": "Accrued expenses account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="int-liab-l-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="int-liab-l-cr-amount")],
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="int-liab-l-bal-details"), _cell(""), _cell("", editable=True, cell_id="int-liab-l-bal-amount"), _cell("")],
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="int-liab-l-total-details"), _cell(""), _cell("", editable=True, cell_id="int-liab-l-total-debit"), _cell("", editable=True, cell_id="int-liab-l-total-credit")],
                    [_cell(scenario["next_date"]), _cell("", editable=True, cell_id="int-liab-l-bd-details"), _cell("Balance"), _cell(""), _cell("", editable=True, cell_id="int-liab-l-bd-amount")],
                ],
            },
        ]
        loan_ledger_correct_map = {
            "int-loan-l-open-details": "Balance b/d",
            "int-loan-l-open-amount": scenario["base_expense"],
            "int-loan-l-dr-details": "Accrued expenses",
            "int-loan-l-dr-amount": accrued_amount,
            "int-loan-l-cr-details": "Profit and Loss",
            "int-loan-l-cr-amount": adjusted_interest,
            "int-loan-l-total-details": "Total",
            "int-loan-l-total-debit": adjusted_interest,
            "int-loan-l-total-credit": adjusted_interest,
            "int-liab-l-cr-details": "Interest on loan",
            "int-liab-l-cr-amount": accrued_amount,
            "int-liab-l-bal-details": "Balance c/d",
            "int-liab-l-bal-amount": accrued_amount,
            "int-liab-l-total-details": "Total",
            "int-liab-l-total-debit": accrued_amount,
            "int-liab-l-total-credit": accrued_amount,
            "int-liab-l-bd-details": "Balance b/d",
            "int-liab-l-bd-amount": accrued_amount,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="ledger",
            prompt=f"Use the journal entries and opening balance to post the interest-on-loan adjustment workflow for {biz}: (A) update and close the Interest on loan account, and (B) record and carry forward the Accrued expenses liability.",
            prompt_tables=loan_ledger_prompt_tables,
            tables=loan_ledger_tables,
            correct_map=loan_ledger_correct_map,
            derivation_map={
                "int-loan-l-dr-amount": f"Accrued interest = R{int(scenario['loan_balance']):,} × {int(scenario['rate'])}% × {int(scenario['months'])}/12 = R{int(accrued_amount):,}.",
                "int-loan-l-cr-amount": f"Adjusted Interest on loan transferred to Profit and Loss = opening balance R{int(scenario['base_expense']):,} + accrued interest R{int(accrued_amount):,} = R{int(adjusted_interest):,}.",
                "int-liab-l-bal-amount": f"The unpaid interest becomes the closing Accrued expenses balance: R{int(accrued_amount):,}.",
                "int-liab-l-bd-amount": f"Balance b/d on the next day equals the previous day's Balance c/d: R{int(accrued_amount):,}.",
                "int-loan-l-total-debit": f"Total debit in Interest on loan = opening balance R{int(scenario['base_expense']):,} + accrued interest R{int(accrued_amount):,} = R{int(adjusted_interest):,}.",
                "int-liab-l-total-credit": f"Total credit in Accrued expenses equals the accrued-interest posting from Interest on loan: R{int(accrued_amount):,}.",
            },
            cell_hints={
                "int-loan-l-open-details": "An opening balance on an expense account is shown as Balance b/d on the debit side.",
                "int-loan-l-dr-details": "The details column shows the opposite account from the journal entry.",
                "int-loan-l-cr-details": "The expense account is closed to Profit and Loss at year-end.",
                "int-liab-l-bal-amount": "The liability balance carried down equals the accrued amount still owing.",
                "int-loan-l-total-debit": "Add the opening balance and the accrued-interest posting before writing the total for the Interest on loan account.",
                "int-liab-l-total-credit": "The credit total in Accrued expenses comes from the accrued-interest posting and must equal the balanced debit total.",
            },
            cell_teaching_map={
                "int-loan-l-cr-details": _teaching_hint(
                    role_in_requirement="This cell names the account used to close the Interest on loan expense account.",
                    evidence_from_question="The workflow requires the expense account to be closed after the accrual is posted.",
                    rule_or_principle="Expense accounts are transferred to Profit and Loss during year-end closing.",
                    method_or_formula="Total adjusted Interest on loan = opening balance + accrued amount, then transfer that total to Profit and Loss.",
                    record_link="The same adjusted amount must appear later in the Profit and Loss extract as the final Interest on loan expense.",
                    how_to_derive="Use Profit and Loss in the details column because the expense account is being closed.",
                    transfer_tip="When an expense account is being closed, look for Profit and Loss as the destination account.",
                ),
                "int-liab-l-bal-amount": _teaching_hint(
                    role_in_requirement="This cell gives the liability balance carried down on Accrued expenses.",
                    evidence_from_question="The interest has been recorded but not yet paid by year-end.",
                    rule_or_principle="A liability account with a credit entry is balanced by placing Balance c/d on the debit side for the same amount.",
                    method_or_formula="Balance c/d on Accrued expenses = accrued-interest amount still payable at year-end.",
                    record_link="This same amount is the Balance Sheet carry-through amount under current liabilities.",
                    how_to_derive=f"Because only the accrued-interest liability remains in the account, Balance c/d is R{int(accrued_amount):,}.",
                    transfer_tip="For a simple payable opened by one credit entry, the carried-down balance usually equals that outstanding amount.",
                ),
                "int-loan-l-total-debit": _teaching_hint(
                    role_in_requirement="This cell totals the debit side of the Interest on loan account after the accrual has been posted.",
                    evidence_from_question=f"The debit side of Interest on loan contains the opening balance of R{int(scenario['base_expense']):,} and the accrued-interest posting of R{int(accrued_amount):,}.",
                    rule_or_principle="An expense ledger account is totalled after all period postings have been entered and before the closing transfer is checked against that total.",
                    method_or_formula=f"R{int(scenario['base_expense']):,} + R{int(accrued_amount):,} = R{int(adjusted_interest):,}.",
                    record_link="This total must agree with the credit-side closing transfer to Profit and Loss in the same account.",
                    how_to_derive="Add the opening expense balance and the accrual entry on the debit side, then write that sum as the account total.",
                    transfer_tip="Leave ledger totals until the postings are complete so you do not total an incomplete account.",
                ),
                "int-liab-l-total-credit": _teaching_hint(
                    role_in_requirement="This cell totals the credit side of the Accrued expenses account in the workflow.",
                    evidence_from_question=f"Accrued expenses has one credit posting from Interest on loan for R{int(accrued_amount):,}, followed by balancing and carry-down entries.",
                    rule_or_principle="A liability account total reflects the original credit posting and must match the completed debit total once the balance c/d has been inserted.",
                    method_or_formula=f"Credit total in Accrued expenses = R{int(accrued_amount):,}.",
                    record_link="This total matches the year-end accrued-interest liability being carried into the next period.",
                    how_to_derive="Use the original credit posting amount as the credit total, then confirm the debit side balances to the same figure.",
                    transfer_tip="In a simple liability T-account opened by one credit entry, the credit total is often the same as that single original posting.",
                ),
            },
            working_map={
                "int-loan-l-cr-details": f"First add the opening expense of R{int(scenario['base_expense']):,} and the accrued amount of R{int(accrued_amount):,}, then close the total to Profit and Loss.",
                "int-liab-l-bd-amount": "The liability remains owing into the next period, so the closing balance c/d becomes the next period's balance b/d.",
                "int-loan-l-total-debit": "Finish the Interest on loan account by totalling the debit entries before checking that Profit and Loss closes the same amount on the credit side.",
                "int-liab-l-total-credit": "Total the original liability credit after inserting Balance c/d so both sides of Accrued expenses agree.",
            },
            guidelines=[
                "Post the accrual to Interest on loan and Accrued expenses first.",
                "Then close the full adjusted Interest on loan balance to Profit and Loss.",
                "Carry the unpaid liability down to the next period in Accrued expenses.",
            ],
            marks=18,
        ), "interest_on_loan_ledger_fill", expected_cells=17, cell_expectations=loan_ledger_correct_map))

        loan_carry_tables = [
            {
                "heading": "Profit and Loss Account (extract)",
                "headers": ["Expense", "Amount"],
                "rows": [[_cell("Interest on loan"), _cell("", editable=True, cell_id="int-loan-fa-expense")]],
            },
            {
                "heading": "Balance Sheet (extract)",
                "headers": ["Current liabilities", "Amount"],
                "rows": [[_cell("Accrued expenses"), _cell("", editable=True, cell_id="int-loan-fa-liability")]],
            },
        ]
        loan_carry_correct_map = {
            "int-loan-fa-expense": adjusted_interest,
            "int-loan-fa-liability": accrued_amount,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the Interest on loan source information for {biz} to carry the year-end adjustment into the Profit and Loss Account and Balance Sheet extracts.",
            prompt_table=loan_prompt_table,
            tables=loan_carry_tables,
            correct_map=loan_carry_correct_map,
            derivation_map={
                "int-loan-fa-expense": f"Adjusted Interest on loan = R{int(scenario['base_expense']):,} + R{int(accrued_amount):,} = R{int(adjusted_interest):,}.",
                "int-loan-fa-liability": f"Carry the unpaid accrued-interest amount to Current liabilities: R{int(accrued_amount):,}.",
            },
            cell_hints={
                "int-loan-fa-expense": "Add the accrued interest to the interest already shown in the Trial Balance.",
                "int-loan-fa-liability": "The unpaid amount becomes Accrued expenses under current liabilities.",
            },
            cell_teaching_map={
                "int-loan-fa-expense": _teaching_hint(
                    role_in_requirement="This cell shows the final Interest on loan expense in Profit and Loss.",
                    evidence_from_question=f"The source table gives Interest on loan already recorded of R{int(scenario['base_expense']):,} and an accrued amount of R{int(accrued_amount):,}.",
                    rule_or_principle="Expenses must be matched to the period in which they are incurred, even if unpaid at year-end.",
                    method_or_formula=f"Adjusted Interest on loan = R{int(scenario['base_expense']):,} + R{int(accrued_amount):,}.",
                    record_link="This adjusted amount must agree with the amount closed from the Interest on loan ledger account to Profit and Loss.",
                    how_to_derive=f"Add the accrual to the Trial Balance figure to show the full year expense: R{int(adjusted_interest):,}.",
                    transfer_tip="If an expense is still owing at year-end, increase the expense in Profit and Loss and create a liability for the same amount.",
                ),
                "int-loan-fa-liability": _teaching_hint(
                    role_in_requirement="This cell carries the unpaid loan-interest amount to the Balance Sheet.",
                    evidence_from_question="The prompt states that part of the year's loan interest is still unpaid at year-end.",
                    rule_or_principle="Amounts still payable at year-end are shown as current liabilities.",
                    method_or_formula=f"Carry the accrued-interest amount R{int(accrued_amount):,} to Accrued expenses.",
                    record_link="This liability amount must match the balance carried down in the Accrued expenses ledger account.",
                    how_to_derive="Use the accrued-interest amount, because that is the portion not yet paid.",
                    transfer_tip="Whenever an expense is owing, expect a matching current-liability carry-through on the Balance Sheet.",
                ),
            },
            working_map={
                "int-loan-fa-expense": "The Profit and Loss extract must show the full adjusted expense for the year, not only the amount already paid.",
                "int-loan-fa-liability": "The Balance Sheet extract carries only the unpaid portion still owed at year-end.",
            },
            guidelines=[
                "Add the accrued interest to the existing Interest on loan figure in Profit and Loss.",
                "Carry the same accrued amount to Accrued expenses under current liabilities.",
            ],
            marks=4,
        ), "interest_on_loan_carrythrough_fill", expected_cells=2, cell_expectations=loan_carry_correct_map))

    income_scenarios = [
        {
            "base_income": 12000,
            "amount": 1800,
            "year_end_date": "28 Feb 2026",
            "source_label": "Interest income on a fixed deposit is still owing at year-end",
        },
        {
            "base_income": 15000,
            "amount": 2400,
            "year_end_date": "31 Dec 2026",
            "source_label": "Interest income earned but not yet received from a savings investment",
        },
    ]
    for scenario in income_scenarios:
        adjusted_income = _round_money(float(scenario["base_income"]) + float(scenario["amount"]))
        income_prompt_table = {
            "heading": "Interest income source note",
            "headers": ["Item", "Amount / detail"],
            "rows": [
                [_cell("Interest income already in the Trial Balance"), _cell(scenario["base_income"])],
                [_cell(scenario["source_label"]), _cell(scenario["amount"])],
            ],
        }
        income_journal_table = {
            "heading": "General Journal: interest income adjustment",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="int-inc-j-dr-details"), _cell("", editable=True, cell_id="int-inc-j-dr-amount"), _cell("")],
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="int-inc-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="int-inc-j-cr-amount")],
            ],
        }
        income_journal_correct_map = {
            "int-inc-j-dr-details": "Accrued income",
            "int-inc-j-dr-amount": scenario["amount"],
            "int-inc-j-cr-details": "Interest income",
            "int-inc-j-cr-amount": scenario["amount"],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=f"{biz} has interest income still owing at year-end. Prepare the General Journal entry dated {scenario['year_end_date']} to record the year-end interest-income adjustment.",
            prompt_table=income_prompt_table,
            table=income_journal_table,
            correct_map=income_journal_correct_map,
            derivation_map={
                "int-inc-j-dr-amount": f"Use the interest-income amount still receivable: R{int(scenario['amount']):,}.",
                "int-inc-j-cr-amount": f"Credit Interest income with the same amount: R{int(scenario['amount']):,}.",
            },
            cell_hints={
                "int-inc-j-dr-details": "Income still receivable is recorded in an asset account.",
                "int-inc-j-cr-details": "The income account is credited because the income has been earned this period.",
                "int-inc-j-dr-amount": "Use the amount of interest income still owing at year-end.",
                "int-inc-j-cr-amount": "Repeat the same receivable amount on the credit side.",
            },
            cell_teaching_map={
                "int-inc-j-dr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the debit account for interest income still owing.",
                    evidence_from_question="The prompt says the interest income has been earned but not yet received.",
                    rule_or_principle="Amounts receivable at year-end are current assets.",
                    method_or_formula="Debit Accrued income and credit Interest income with the same amount.",
                    record_link="The same amount will later appear in the Balance Sheet as an accrued-income asset.",
                    how_to_derive="Because the business is owed the money, debit Accrued income.",
                    transfer_tip="When income is earned but unpaid, think asset up and income up.",
                ),
                "int-inc-j-cr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the income account credited for the adjustment.",
                    evidence_from_question="The amount belongs to the current year even though cash has not yet been received.",
                    rule_or_principle="Income earned in the current period must be credited to the correct income account under the matching / accrual principle.",
                    method_or_formula="Credit Interest income with the accrued amount.",
                    record_link="This credited amount increases the Interest income figure carried to the Income Statement extract.",
                    how_to_derive="Use Interest income because that is the nominal account affected by the accrual.",
                    transfer_tip="For accrued income, the nominal income account is credited and the receivable account is debited.",
                ),
                "int-inc-j-dr-amount": _teaching_hint(
                    role_in_requirement="This cell records the debit amount for the accrued-interest-income journal entry.",
                    evidence_from_question=f"The source note states that interest income of R{int(scenario['amount']):,} is still owing at year-end.",
                    rule_or_principle="An accrued-income adjustment uses the exact amount earned but not yet received on both sides of the journal.",
                    method_or_formula=f"Debit Accrued income with R{int(scenario['amount']):,}.",
                    record_link="This amount must match the credit to Interest income and later appear as the Accrued income asset in the Balance Sheet extract.",
                    how_to_derive="Read the receivable amount directly from the source note and enter it on the debit side.",
                    transfer_tip="If the note gives the accrued-income amount directly, use it as given and then mirror it on the matching credit side.",
                ),
                "int-inc-j-cr-amount": _teaching_hint(
                    role_in_requirement="This cell records the matching credit amount for the interest-income accrual.",
                    evidence_from_question=f"The accrued-interest-income journal uses the same receivable amount of R{int(scenario['amount']):,} on both sides.",
                    rule_or_principle="A journal entry balances by repeating the same adjustment amount on the opposite side.",
                    method_or_formula=f"Credit Interest income with R{int(scenario['amount']):,}.",
                    record_link="This amount must equal the debit to Accrued income and later increase the adjusted Interest income figure in the statements.",
                    how_to_derive="Copy the same receivable amount used on the debit side.",
                    transfer_tip="Once you identify the adjustment amount, check that the credit side mirrors it exactly.",
                ),
            },
            working_map={
                "int-inc-j-dr-details": "Start by recognising that money owed to the business is a receivable asset before you choose the income account.",
                "int-inc-j-dr-amount": "Use the stated interest income still owing as the fixed amount for the whole journal entry.",
                "int-inc-j-cr-details": "This adjustment increases current-year interest income and creates a matching receivable asset.",
                "int-inc-j-cr-amount": "Mirror the same receivable amount on the credit side so the accrued-income journal balances.",
            },
            guidelines=[
                "Record the amount still receivable at year-end.",
                "Use Accrued income on the debit side and Interest income on the credit side.",
            ],
            marks=8,
        ), "interest_income_journal_fill", expected_cells=4, cell_expectations=income_journal_correct_map))

        income_analysis_table = {
            "heading": "Adjustment analysis: interest income",
            "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
            "rows": [
                [_cell(scenario["source_label"]), _cell("", editable=True, cell_id="int-inc-a-amount"), _cell("", editable=True, cell_id="int-inc-a-dr"), _cell("", editable=True, cell_id="int-inc-a-cr"), _cell("", editable=True, cell_id="int-inc-a-is"), _cell("", editable=True, cell_id="int-inc-a-bs")],
            ],
        }
        income_analysis_correct_map = {
            "int-inc-a-amount": scenario["amount"],
            "int-inc-a-dr": "Accrued income",
            "int-inc-a-cr": "Interest income",
            "int-inc-a-is": "Income increases by R" + f"{int(scenario['amount']):,}",
            "int-inc-a-bs": "Current asset increases by R" + f"{int(scenario['amount']):,}",
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="adjustment_analysis_table",
            prompt=f"{biz} must adjust for interest income still owing at year-end. Complete the adjustment analysis table.",
            prompt_table=income_prompt_table,
            table=income_analysis_table,
            correct_map=income_analysis_correct_map,
            derivation_map={
                "int-inc-a-amount": f"Use the interest-income adjustment amount: R{int(scenario['amount']):,}.",
            },
            cell_hints={
                "int-inc-a-amount": "Use the same interest-income adjustment amount throughout the analysis row.",
                "int-inc-a-dr": "Amounts receivable are debited to an asset account.",
                "int-inc-a-cr": "The related income account is credited because income has been earned.",
                "int-inc-a-is": "This adjustment increases income for the current period.",
                "int-inc-a-bs": "An amount still receivable is shown as a current asset.",
            },
            cell_teaching_map={
                "int-inc-a-amount": _teaching_hint(
                    role_in_requirement="This cell records the amount column of the accrued-interest-income analysis row.",
                    evidence_from_question=f"The adjustment note gives the interest income still owing as R{int(scenario['amount']):,}.",
                    rule_or_principle="The analysis table uses the same amount as the journal entry because it is analysing that exact accrual adjustment.",
                    method_or_formula=f"Enter R{int(scenario['amount']):,} in the amount column.",
                    record_link="This amount must agree with both the debit to Accrued income and the credit to Interest income in the journal entry.",
                    how_to_derive="Copy the adjustment amount directly from the source note before completing the effect columns.",
                    transfer_tip="Lock in the source amount first, then use that same figure to reason through the account and statement effects.",
                ),
                "int-inc-a-dr": _teaching_hint(
                    role_in_requirement="This cell identifies the account debited in the interest-income analysis table.",
                    evidence_from_question="The interest income has been earned but is still receivable at year-end.",
                    rule_or_principle="Amounts owed to the business are shown in an accrued-income asset account until cash is received.",
                    method_or_formula="Debit Accrued income and credit Interest income with the same amount.",
                    record_link="This account must match the debit side of the corresponding journal entry and the asset carry-through in the Balance Sheet.",
                    how_to_derive="Choose Accrued income because the business is still owed this money.",
                    transfer_tip="In analysis tables, ask first whether the business owes money or is owed money to decide between accrued expenses and accrued income.",
                ),
                "int-inc-a-cr": _teaching_hint(
                    role_in_requirement="This cell identifies the account credited in the interest-income analysis table.",
                    evidence_from_question="The adjustment relates to interest income earned in the current period.",
                    rule_or_principle="Income earned in the current period is credited to the relevant nominal income account even if it has not yet been received.",
                    method_or_formula="Credit Interest income with the accrued amount.",
                    record_link="This account must match the credit side of the journal entry and the increased income shown in the Income Statement carry-through.",
                    how_to_derive="Use Interest income because that is the revenue account increased by this accrual.",
                    transfer_tip="Once you identify an accrued-income adjustment, pair the receivable asset with the matching income account.",
                ),
                "int-inc-a-is": _teaching_hint(
                    role_in_requirement="This cell explains the Income Statement effect of the accrued interest-income adjustment.",
                    evidence_from_question="The interest belongs to the current year but has not yet been received in cash.",
                    rule_or_principle="Accrued income increases current-period income because it has already been earned.",
                    method_or_formula="Increase Interest income by the accrued amount.",
                    record_link="This effect must match the credit posted to Interest income in the journal entry and the adjusted statement carry-through amount.",
                    how_to_derive=f"Show that income increases by R{int(scenario['amount']):,}.",
                    transfer_tip="If income is owing to the business, the Income Statement effect is usually an increase in income.",
                ),
                "int-inc-a-bs": _teaching_hint(
                    role_in_requirement="This cell explains the Balance Sheet effect of the interest-income accrual.",
                    evidence_from_question="The business is still owed the interest amount at year-end.",
                    rule_or_principle="Amounts receivable are shown as current assets until collected.",
                    method_or_formula="Carry the accrued amount to Accrued income under current assets.",
                    record_link="This Balance Sheet effect must match the debit entry to Accrued income and the carry-through extract.",
                    how_to_derive=f"Show a current-asset increase of R{int(scenario['amount']):,}.",
                    transfer_tip="Whenever the business is still owed money, expect a current-asset effect.",
                ),
            },
            working_map={
                "int-inc-a-amount": "Use the journal adjustment amount first, then keep that same figure fixed across the rest of the analysis row.",
                "int-inc-a-dr": "The debit column shows the receivable asset created because the business is still owed this income.",
                "int-inc-a-cr": "The credit column names the income account increased by the accrual.",
                "int-inc-a-is": "The analysis table follows directly from the journal entry: income rises and a matching receivable asset is created.",
                "int-inc-a-bs": "Because the amount is still receivable, the Balance Sheet effect is a current-asset increase rather than a liability change.",
            },
            guidelines=[
                "Use the same amount across the adjustment, the double entry, and the statement effects.",
                "Show that accrued interest income increases both income and current assets.",
            ],
            marks=6,
        ), "interest_income_analysis_fill", expected_cells=5, cell_expectations=income_analysis_correct_map))

        income_carry_tables = [
            {
                "heading": "Income Statement extract",
                "headers": ["Other income", "Amount"],
                "rows": [[_cell("Interest income"), _cell("", editable=True, cell_id="int-inc-fa-income")]],
            },
            {
                "heading": "Balance Sheet extract",
                "headers": ["Current assets", "Amount"],
                "rows": [[_cell("Accrued income"), _cell("", editable=True, cell_id="int-inc-fa-asset")]],
            },
        ]
        income_carry_correct_map = {
            "int-inc-fa-income": adjusted_income,
            "int-inc-fa-asset": scenario["amount"],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the interest-income information below to carry the year-end adjustment into the Income Statement and Balance Sheet extracts for {biz}.",
            prompt_table=income_prompt_table,
            tables=income_carry_tables,
            correct_map=income_carry_correct_map,
            derivation_map={
                "int-inc-fa-income": f"Adjusted Interest income = R{int(scenario['base_income']):,} + R{int(scenario['amount']):,} = R{int(adjusted_income):,}.",
                "int-inc-fa-asset": f"Carry the interest still receivable to Accrued income: R{int(scenario['amount']):,}.",
            },
            cell_hints={
                "int-inc-fa-income": "Add the interest still owing to the Interest income figure already shown.",
                "int-inc-fa-asset": "The amount still receivable becomes a current asset.",
            },
            cell_teaching_map={
                "int-inc-fa-income": _teaching_hint(
                    role_in_requirement="This cell shows the adjusted Interest income figure in the Income Statement.",
                    evidence_from_question=f"The source note gives Interest income already recorded of R{int(scenario['base_income']):,} and a further amount of R{int(scenario['amount']):,} still owing.",
                    rule_or_principle="Income earned in the current period must be fully included even if not yet received.",
                    method_or_formula=f"Adjusted Interest income = R{int(scenario['base_income']):,} + R{int(scenario['amount']):,}.",
                    record_link="This adjusted figure must agree with the journal credit to Interest income plus the original Trial Balance figure.",
                    how_to_derive=f"Add the accrued amount to the existing figure to get R{int(adjusted_income):,}.",
                    transfer_tip="For accrued income, increase the statement income figure and carry the unpaid amount to current assets.",
                ),
                "int-inc-fa-asset": _teaching_hint(
                    role_in_requirement="This cell carries the unpaid interest-income amount to the Balance Sheet.",
                    evidence_from_question="The interest has been earned but not yet received in cash.",
                    rule_or_principle="Amounts still receivable are shown as current assets.",
                    method_or_formula=f"Carry R{int(scenario['amount']):,} to Accrued income.",
                    record_link="This asset amount must match the journal debit to Accrued income and the adjustment-analysis Balance Sheet effect.",
                    how_to_derive="Use only the unpaid amount, because that is what remains receivable at year-end.",
                    transfer_tip="Do not carry the full adjusted income figure to the Balance Sheet; carry only the amount still owing.",
                ),
            },
            working_map={
                "int-inc-fa-income": "The Income Statement receives the full adjusted nominal income amount.",
                "int-inc-fa-asset": "The Balance Sheet receives only the receivable portion still outstanding at year-end.",
            },
            guidelines=[
                "Add the accrued amount to Interest income in the Income Statement.",
                "Carry the same accrued amount to Accrued income under current assets.",
            ],
            marks=4,
        ), "interest_income_carrythrough_fill", expected_cells=2, cell_expectations=income_carry_correct_map))

    workflow_loan_balance = 100000
    workflow_loan_rate = 12
    workflow_loan_months = 3
    workflow_loan_amount = _round_money(float(workflow_loan_balance) * float(workflow_loan_rate) / 100 * float(workflow_loan_months) / 12)
    workflow_income_amount = 2400
    workflow_prompt_table = {
        "heading": "Interest adjustment source list",
        "headers": ["No.", "Adjustment"],
        "rows": [
            [_cell("1"), _cell(f"Interest on loan on R{int(workflow_loan_balance):,} at {int(workflow_loan_rate)}% p.a. for the last {int(workflow_loan_months)} month(s) is still owing.")],
            [_cell("2"), _cell(f"Interest income of R{int(workflow_income_amount):,} on an investment is still receivable at year-end.")],
        ],
    }
    workflow_journal_table = {
        "heading": "General Journal: grouped interest adjustments",
        "headers": ["Date", "Details", "Debit", "Credit"],
        "rows": [
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="intwf-1-dr-details"), _cell("", editable=True, cell_id="intwf-1-dr-amount"), _cell("")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="intwf-1-cr-details"), _cell(""), _cell("", editable=True, cell_id="intwf-1-cr-amount")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="intwf-2-dr-details"), _cell("", editable=True, cell_id="intwf-2-dr-amount"), _cell("")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="intwf-2-cr-details"), _cell(""), _cell("", editable=True, cell_id="intwf-2-cr-amount")],
        ],
    }
    workflow_correct_map = {
        "intwf-1-dr-details": "Interest on loan",
        "intwf-1-dr-amount": workflow_loan_amount,
        "intwf-1-cr-details": "Accrued expenses",
        "intwf-1-cr-amount": workflow_loan_amount,
        "intwf-2-dr-details": "Accrued income",
        "intwf-2-dr-amount": workflow_income_amount,
        "intwf-2-cr-details": "Interest income",
        "intwf-2-cr-amount": workflow_income_amount,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="journal",
        prompt=f"Use the interest-adjustment source list for {biz} to prepare all the General Journal entries required at year-end.",
        prompt_table=workflow_prompt_table,
        table=workflow_journal_table,
        correct_map=workflow_correct_map,
        derivation_map={
            "intwf-1-dr-amount": f"Accrued interest on loan = R{int(workflow_loan_balance):,} × {int(workflow_loan_rate)}% × {int(workflow_loan_months)}/12 = R{int(workflow_loan_amount):,}.",
            "intwf-2-dr-amount": f"Use the interest income still receivable amount from the source note: R{int(workflow_income_amount):,}.",
            "intwf-1-cr-amount": f"Credit Accrued expenses with the same accrued-interest amount: R{int(workflow_loan_amount):,}.",
            "intwf-2-cr-amount": f"Credit Interest income with the same receivable amount: R{int(workflow_income_amount):,}.",
        },
        cell_hints={
            "intwf-1-dr-details": "Outstanding loan interest belongs to this year, so start with the expense account on the debit side.",
            "intwf-1-cr-details": "Unpaid loan interest is credited to a liability account.",
            "intwf-2-dr-details": "Interest income still receivable is debited to an asset account.",
            "intwf-2-cr-details": "The related income account is credited because the income has already been earned.",
            "intwf-1-dr-amount": "Calculate the accrued loan interest using loan balance × rate × months/12.",
            "intwf-1-cr-amount": "Use the same accrued-interest amount on the credit side of row 1.",
            "intwf-2-dr-amount": "Use the interest income still receivable amount given in adjustment 2.",
            "intwf-2-cr-amount": "Use the same receivable amount on the credit side of row 2.",
        },
        cell_teaching_map={
            "intwf-1-dr-details": _teaching_hint(
                role_in_requirement="This cell records the debit account for the loan-interest accrual in a grouped workflow.",
                evidence_from_question="The source list states that loan interest for the last part of the year is still owing.",
                rule_or_principle="Outstanding expenses are debited to the expense account and credited to a liability account.",
                method_or_formula=f"Accrued interest = R{int(workflow_loan_balance):,} × {int(workflow_loan_rate)}% × {int(workflow_loan_months)}/12.",
                record_link="This amount later increases the Interest on loan figure in Profit and Loss and creates Accrued expenses in the Balance Sheet.",
                how_to_derive="Debit Interest on loan because the expense belongs to the current accounting period.",
                transfer_tip="In grouped interest-adjustment questions, separate expense accruals from income accruals before choosing the debit account.",
            ),
            "intwf-1-cr-details": _teaching_hint(
                role_in_requirement="This cell records the liability account credited for the loan-interest accrual in the grouped workflow.",
                evidence_from_question="The source list says the final months of interest are still owing and have not yet been paid.",
                rule_or_principle="Outstanding expenses are credited to a current-liability account until settlement.",
                method_or_formula="Credit Accrued expenses with the same accrued-interest amount used on the debit side.",
                record_link="This creates the liability that later appears in the Balance Sheet and adjusted trial balance.",
                how_to_derive="Use Accrued expenses because the amount is still payable at year-end.",
                transfer_tip="For an expense accrual, the credit side usually creates or increases a payable account.",
            ),
            "intwf-2-dr-details": _teaching_hint(
                role_in_requirement="This cell records the debit account for interest income still receivable in the grouped workflow.",
                evidence_from_question="The source list states that the business is still owed the interest income at year-end.",
                rule_or_principle="Accrued income is debited to a current asset account and credited to the relevant income account.",
                method_or_formula="Debit Accrued income and credit Interest income with the same receivable amount.",
                record_link="This amount later appears as Accrued income in the Balance Sheet and increases Interest income in the Income Statement.",
                how_to_derive="Debit Accrued income because the business has earned the money and is still owed it.",
                transfer_tip="If the business is owed money at year-end, the debit side is usually a current-asset accrual account.",
            ),
            "intwf-2-cr-details": _teaching_hint(
                role_in_requirement="This cell records the income account credited for the accrued-interest-income entry in the grouped workflow.",
                evidence_from_question="The interest income belongs to the current period even though it has not yet been received in cash.",
                rule_or_principle="Income earned in the current period must be credited to the relevant nominal income account.",
                method_or_formula="Credit Interest income with the receivable amount from the source note.",
                record_link="This increases the current-period interest-income figure that later appears in the Income Statement and adjusted trial balance.",
                how_to_derive="Use Interest income because that is the revenue account affected by the accrual.",
                transfer_tip="For an income accrual, pair the receivable asset on the debit side with the matching income account on the credit side.",
            ),
            "intwf-1-dr-amount": _teaching_hint(
                role_in_requirement="This cell calculates the amount for the loan-interest accrual in row 1 of the grouped journal workflow.",
                evidence_from_question=f"Adjustment 1 states that interest on loan on R{int(workflow_loan_balance):,} at {int(workflow_loan_rate)}% p.a. for the last {int(workflow_loan_months)} month(s) is still owing.",
                rule_or_principle="An outstanding expense is measured for the part of the year already incurred, using the accrual formula before it is journalised.",
                method_or_formula=f"R{int(workflow_loan_balance):,} × {int(workflow_loan_rate)}% × {int(workflow_loan_months)}/12 = R{int(workflow_loan_amount):,}.",
                record_link="This amount must match the credit to Accrued expenses in row 1 and later increase Interest on loan in the adjusted records.",
                how_to_derive="Apply the loan-interest accrual formula to the balance, annual rate, and months outstanding.",
                transfer_tip="When an accrual question gives capital, annual rate, and months, calculate the expense first and then repeat that amount on the paired credit side.",
            ),
            "intwf-1-cr-amount": _teaching_hint(
                role_in_requirement="This cell enters the matching credit amount for the loan-interest accrual in row 1.",
                evidence_from_question=f"Row 1 records one accrued-expense adjustment, so the credit must use the same accrued-interest amount of R{int(workflow_loan_amount):,}.",
                rule_or_principle="Every journal entry must balance, so the credit amount equals the debit amount for the same adjustment row.",
                method_or_formula=f"Credit amount = debit amount for row 1 = R{int(workflow_loan_amount):,}.",
                record_link="This amount must match the debit to Interest on loan and becomes the Accrued expenses liability carried forward.",
                how_to_derive="Copy the calculated accrued-interest amount from the debit side of row 1.",
                transfer_tip="Complete one row at a time: calculate the row's debit amount, then mirror exactly the same figure on the credit side.",
            ),
            "intwf-2-dr-amount": _teaching_hint(
                role_in_requirement="This cell enters the receivable amount for the accrued-interest-income adjustment in row 2.",
                evidence_from_question=f"Adjustment 2 says interest income of R{int(workflow_income_amount):,} on an investment is still receivable at year-end.",
                rule_or_principle="Accrued income is recognised at the amount earned but not yet received, and that same amount is debited to the receivable account.",
                method_or_formula=f"Use the stated receivable amount: R{int(workflow_income_amount):,}.",
                record_link="This amount must match the credit to Interest income in row 2 and later appear as Accrued income in the Balance Sheet / adjusted trial balance.",
                how_to_derive="Read the amount directly from adjustment 2 and enter it as the Accrued income debit.",
                transfer_tip="If the source note gives a receivable amount directly, do not recalculate it; use it and repeat it on the matching credit side.",
            ),
            "intwf-2-cr-amount": _teaching_hint(
                role_in_requirement="This cell enters the matching credit amount for the accrued-interest-income entry in row 2.",
                evidence_from_question=f"The accrued-interest-income adjustment in row 2 uses the receivable amount of R{int(workflow_income_amount):,} on both sides of the journal.",
                rule_or_principle="Journal rows must balance, so the credited income amount equals the debited receivable amount for the same adjustment.",
                method_or_formula=f"Credit amount = debit amount for row 2 = R{int(workflow_income_amount):,}.",
                record_link="This amount must match the debit to Accrued income and increases the Interest income figure used in later records.",
                how_to_derive="Copy the stated receivable amount from the debit side of row 2.",
                transfer_tip="After identifying the correct accounts, check that each journal row uses the same amount on both sides before moving to the next adjustment.",
            ),
        },
        working_map={
            "intwf-1-dr-details": "Row 1 is an outstanding-expense adjustment, so it increases the expense and creates a matching payable.",
            "intwf-2-dr-details": "Row 2 is an accrued-income adjustment, so it creates a receivable and increases income.",
            "intwf-1-cr-details": "Complete the expense-accrual row as one balanced pair before moving to the income-accrual row.",
            "intwf-1-dr-amount": "Calculate row 1 first, then copy that same accrued-interest amount to the row 1 credit side.",
            "intwf-1-cr-amount": "Row 1 balances by repeating the calculated accrued-interest amount on the liability credit side.",
            "intwf-2-dr-amount": "Use the stated receivable amount for row 2 and mirror it on the income credit side.",
            "intwf-2-cr-amount": "Finish row 2 by copying the receivable amount to the Interest income credit side.",
        },
        guidelines=[
            "Treat the loan-interest item as an accrued expense and the investment-interest item as accrued income.",
            "Use the same amount on both sides of each journal entry.",
            "Do not combine the two adjustments into one total; journal each one separately.",
        ],
        marks=10,
    ), "interest_adjustment_journal_workflow_fill", expected_cells=8, cell_expectations=workflow_correct_map))

    patb_bank = 58000
    patb_fixed_deposit = 40000
    patb_stock = 62000
    patb_interest_expense = 8400
    patb_interest_income = 16000
    patb_loan = 100000
    patb_income_adjustment = workflow_income_amount
    patb_expense_adjustment = workflow_loan_amount
    patb_adjusted_income = _round_money(float(patb_interest_income) + float(patb_income_adjustment))
    patb_adjusted_expense = _round_money(float(patb_interest_expense) + float(patb_expense_adjustment))
    patb_capital = _round_money(float(patb_bank) + float(patb_fixed_deposit) + float(patb_stock) + float(patb_interest_expense) - float(patb_interest_income) - float(patb_loan))
    patb_total = _round_money(float(patb_bank) + float(patb_fixed_deposit) + float(patb_stock) + float(patb_income_adjustment) + float(patb_adjusted_expense))
    patb_prompt_tables = [
        {
            "heading": "Pre-adjustment Trial Balance extract",
            "headers": ["Account", "Debit", "Credit"],
            "rows": [
                [_cell("Bank"), _cell(patb_bank), _cell("")],
                [_cell("Fixed deposit"), _cell(patb_fixed_deposit), _cell("")],
                [_cell("Trading stock"), _cell(patb_stock), _cell("")],
                [_cell("Interest on loan"), _cell(patb_interest_expense), _cell("")],
                [_cell("Interest income"), _cell(""), _cell(patb_interest_income)],
                [_cell("Loan"), _cell(""), _cell(patb_loan)],
                [_cell("Capital"), _cell(""), _cell(patb_capital)],
            ],
        },
        {
            "heading": "Year-end interest adjustments",
            "headers": ["No.", "Adjustment"],
            "rows": [
                [_cell("1"), _cell(f"Interest on loan owing at year-end: R{int(patb_expense_adjustment):,}")],
                [_cell("2"), _cell(f"Interest income owing at year-end: R{int(patb_income_adjustment):,}")],
            ],
        },
    ]
    patb_table = {
        "heading": "Post-adjustment Trial Balance extract",
        "headers": ["Account", "Debit", "Credit"],
        "rows": [
            [_cell("Bank"), _cell("", editable=True, cell_id="intpatb-bank-debit"), _cell("")],
            [_cell("Fixed deposit"), _cell("", editable=True, cell_id="intpatb-fixed-deposit-debit"), _cell("")],
            [_cell("Trading stock"), _cell("", editable=True, cell_id="intpatb-stock-debit"), _cell("")],
            [_cell("Accrued income"), _cell("", editable=True, cell_id="intpatb-accrued-income-debit"), _cell("")],
            [_cell("Interest on loan"), _cell("", editable=True, cell_id="intpatb-interest-expense-debit"), _cell("")],
            [_cell("Interest income"), _cell(""), _cell("", editable=True, cell_id="intpatb-interest-income-credit")],
            [_cell("Accrued expenses"), _cell(""), _cell("", editable=True, cell_id="intpatb-accrued-expenses-credit")],
            [_cell("Loan"), _cell(""), _cell("", editable=True, cell_id="intpatb-loan-credit")],
            [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="intpatb-capital-credit")],
            [_cell("Total"), _cell("", editable=True, cell_id="intpatb-total-debit"), _cell("", editable=True, cell_id="intpatb-total-credit")],
        ],
    }
    patb_correct_map = {
        "intpatb-bank-debit": patb_bank,
        "intpatb-fixed-deposit-debit": patb_fixed_deposit,
        "intpatb-stock-debit": patb_stock,
        "intpatb-accrued-income-debit": patb_income_adjustment,
        "intpatb-interest-expense-debit": patb_adjusted_expense,
        "intpatb-interest-income-credit": patb_adjusted_income,
        "intpatb-accrued-expenses-credit": patb_expense_adjustment,
        "intpatb-loan-credit": patb_loan,
        "intpatb-capital-credit": patb_capital,
        "intpatb-total-debit": patb_total,
        "intpatb-total-credit": patb_total,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="trial_balance_table",
        prompt=f"Use the Pre-adjustment Trial Balance extract and the year-end interest adjustments for {biz} to complete the Post-adjustment Trial Balance extract.",
        prompt_tables=patb_prompt_tables,
        table=patb_table,
        correct_map=patb_correct_map,
        derivation_map={
            "intpatb-interest-expense-debit": f"Adjusted Interest on loan = R{int(patb_interest_expense):,} + R{int(patb_expense_adjustment):,} = R{int(patb_adjusted_expense):,}.",
            "intpatb-interest-income-credit": f"Adjusted Interest income = R{int(patb_interest_income):,} + R{int(patb_income_adjustment):,} = R{int(patb_adjusted_income):,}.",
            "intpatb-total-debit": f"Total debits = R{int(patb_bank):,} + R{int(patb_fixed_deposit):,} + R{int(patb_stock):,} + R{int(patb_income_adjustment):,} + R{int(patb_adjusted_expense):,} = R{int(patb_total):,}.",
            "intpatb-accrued-expenses-credit": f"Carry the unpaid loan-interest amount to Accrued expenses: R{int(patb_expense_adjustment):,}.",
            "intpatb-accrued-income-debit": f"Carry the interest income still owing to Accrued income: R{int(patb_income_adjustment):,}.",
        },
        cell_hints={
            "intpatb-accrued-income-debit": "The amount still receivable from interest income becomes a new accrued-income asset in the debit column.",
            "intpatb-interest-expense-debit": "Add the accrued loan interest to the existing Interest on loan balance.",
            "intpatb-interest-income-credit": "Add the accrued interest income to the existing Interest income balance.",
            "intpatb-accrued-expenses-credit": "Outstanding loan interest creates a new accrued-expense liability in the credit column.",
        },
        cell_teaching_map={
            "intpatb-accrued-income-debit": _teaching_hint(
                role_in_requirement="This cell inserts the new Accrued income asset in the Post-adjustment Trial Balance.",
                evidence_from_question=f"The year-end note says interest income of R{int(patb_income_adjustment):,} is still owing at year-end.",
                rule_or_principle="An accrued-income adjustment creates a current-asset balance that must appear in the debit column of the adjusted trial balance.",
                method_or_formula="Enter the interest income still receivable as Accrued income.",
                record_link="This asset must agree with the journal debit to Accrued income and the Balance Sheet carry-through amount.",
                how_to_derive=f"Use R{int(patb_income_adjustment):,} as the new Accrued income debit balance.",
                transfer_tip="When an adjustment creates a new asset, check whether it must be inserted as an extra line in the adjusted trial balance.",
            ),
            "intpatb-interest-expense-debit": _teaching_hint(
                role_in_requirement="This cell shows the adjusted Interest on loan balance in the Post-adjustment Trial Balance.",
                evidence_from_question=f"The Pre-adjustment Trial Balance shows Interest on loan of R{int(patb_interest_expense):,}, and the year-end note adds unpaid interest of R{int(patb_expense_adjustment):,}.",
                rule_or_principle="Outstanding expenses increase the related expense account in the Post-adjustment Trial Balance.",
                method_or_formula=f"Adjusted Interest on loan = R{int(patb_interest_expense):,} + R{int(patb_expense_adjustment):,}.",
                record_link="This adjusted amount must match the amount that would be closed from the Interest on loan ledger account to Profit and Loss.",
                how_to_derive=f"Add the accrued expense to the pre-adjustment balance to get R{int(patb_adjusted_expense):,}.",
                transfer_tip="When completing a Post-adjustment Trial Balance, update the original nominal balance before you think about the totals.",
            ),
            "intpatb-interest-income-credit": _teaching_hint(
                role_in_requirement="This cell shows the adjusted Interest income balance in the Post-adjustment Trial Balance.",
                evidence_from_question=f"The Pre-adjustment Trial Balance shows Interest income of R{int(patb_interest_income):,}, and the year-end note adds interest still owing of R{int(patb_income_adjustment):,}.",
                rule_or_principle="Accrued income increases the related income account in the Post-adjustment Trial Balance.",
                method_or_formula=f"Adjusted Interest income = R{int(patb_interest_income):,} + R{int(patb_income_adjustment):,}.",
                record_link="This amount must agree with the journal credit to Interest income and the Income Statement carry-through amount.",
                how_to_derive=f"Add the accrued income to the pre-adjustment balance to get R{int(patb_adjusted_income):,}.",
                transfer_tip="When income is owing at year-end, update the credit-side income account and add a matching asset on the debit side.",
            ),
            "intpatb-accrued-expenses-credit": _teaching_hint(
                role_in_requirement="This cell inserts the new Accrued expenses liability in the Post-adjustment Trial Balance.",
                evidence_from_question=f"The year-end note shows unpaid interest on loan of R{int(patb_expense_adjustment):,}.",
                rule_or_principle="An accrued-expense adjustment creates a current-liability balance that must appear in the credit column of the adjusted trial balance.",
                method_or_formula="Enter the unpaid interest amount as Accrued expenses.",
                record_link="This liability must agree with the journal credit to Accrued expenses and the Balance Sheet carry-through amount.",
                how_to_derive=f"Use R{int(patb_expense_adjustment):,} as the new Accrued expenses credit balance.",
                transfer_tip="When an adjustment creates a new liability, insert it as a separate credit line before totaling the adjusted trial balance.",
            ),
            "intpatb-total-debit": _teaching_hint(
                role_in_requirement="This cell shows the final total of the debit column in the Post-adjustment Trial Balance.",
                evidence_from_question="Every adjusted account balance in the debit column has already been completed above this total line.",
                rule_or_principle="A Trial Balance total is the sum of all balances in that column after every adjustment has been applied.",
                method_or_formula="Add all debit balances after adjustment, including the new Accrued income asset and the adjusted Interest on loan expense.",
                record_link="The debit total must equal the credit total once all adjustments have been posted correctly.",
                how_to_derive=f"The finished debit column adds to R{int(patb_total):,}.",
                transfer_tip="Always calculate totals last, after every adjusted account balance and new accrual account has been inserted.",
            ),
        },
        working_map={
            "intpatb-accrued-income-debit": "Interest income owing creates a new asset line in the debit column.",
            "intpatb-accrued-expenses-credit": "Unpaid loan interest creates a new liability line in the credit column.",
            "intpatb-total-debit": "Once the adjusted balances are complete, the debit and credit totals must match exactly.",
        },
        guidelines=[
            "Adjust the existing Interest on loan and Interest income balances before working out the totals.",
            "Add Accrued income to the debit column and Accrued expenses to the credit column.",
            "Total the finished columns only after every adjustment has been carried through.",
        ],
        marks=10,
    ), "interest_adjustment_post_adjustment_tb_fill", expected_cells=11, cell_expectations=patb_correct_map))

    return pool



