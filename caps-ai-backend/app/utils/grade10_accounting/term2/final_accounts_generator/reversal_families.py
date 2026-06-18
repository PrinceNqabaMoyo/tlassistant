from __future__ import annotations

import random
from typing import Any, Dict, List

from .shared import _cell, _make_fill_in_table_question, _round_money, _teaching_hint, _with_validation


def _gen_reversal_adjustments(*, r: random.Random, biz: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []

    accrued_income = _round_money(float(context.get("accrued_income", 0.0)))
    accrued_expense_amount = _round_money(float(context.get("accrued_expense_amount", 0.0)))
    prepaid_total = _round_money(float(context.get("prepaid_total", 0.0)))
    prepaid_amount = _round_money(float(context.get("prepaid_amount", 0.0)))
    income_advance_amount = _round_money(float(context.get("income_advance_amount", 0.0)))

    accrued_income_ledger_scenarios = [
        {
            "income_label": "Rent income",
            "amount": accrued_income,
            "base_balance": 18000,
            "year_end_date": "28 Feb 2026",
            "reversal_date": "1 Mar 2026",
            "prompt_intro": f"{biz} is still owed rent income of R{accrued_income:,} at year-end.",
        },
        {
            "income_label": "Commission income",
            "amount": _round_money(r.choice([1800, 2400, 3000, 4200])),
            "base_balance": 24000,
            "year_end_date": "30 Jun 2026",
            "reversal_date": "1 Jul 2026",
            "prompt_intro": "",
        },
        {
            "income_label": "Interest income",
            "amount": _round_money(r.choice([900, 1200, 1500, 2100])),
            "base_balance": 12000,
            "year_end_date": "31 Dec 2026",
            "reversal_date": "1 Jan 2027",
            "prompt_intro": "",
        },
    ]
    accrued_income_ledger_scenarios[1]["prompt_intro"] = f"{biz} earned commission income that has not yet been received by 30 June 2026. The amount still receivable is R{int(accrued_income_ledger_scenarios[1]['amount']):,}."
    accrued_income_ledger_scenarios[2]["prompt_intro"] = f"{biz} has interest income owing at year-end of R{int(accrued_income_ledger_scenarios[2]['amount']):,}."
    for scenario in accrued_income_ledger_scenarios:
        income_label = str(scenario["income_label"])
        adjusted_income_balance = _round_money(float(scenario["base_balance"]) + float(scenario["amount"]))
        accrued_income_ledger_tables = [
            {
                "heading": "Accrued income account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-inc-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="acc-inc-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-inc-rev-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="acc-inc-rev-amount")],
                ],
            },
            {
                "heading": f"{income_label} account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="rent-inc-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="rent-inc-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="rent-inc-rev-details"), _cell("GJ"), _cell("", editable=True, cell_id="rent-inc-rev-amount"), _cell("")],
                ],
            },
        ]
        accrued_income_journal_table = {
            "heading": "General Journal",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-inc-j-dr-details"), _cell("", editable=True, cell_id="acc-inc-j-dr-amount"), _cell("")],
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-inc-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="acc-inc-j-cr-amount")],
                [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-inc-j-rev-dr-details"), _cell("", editable=True, cell_id="acc-inc-j-rev-dr-amount"), _cell("")],
                [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-inc-j-rev-cr-details"), _cell(""), _cell("", editable=True, cell_id="acc-inc-j-rev-cr-amount")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=f"{scenario['prompt_intro']} Prepare the General Journal entry for the year-end adjustment dated {scenario['year_end_date']} and the reversal on {scenario['reversal_date']}.",
            table=accrued_income_journal_table,
            correct_map={
                "acc-inc-j-dr-details": "Accrued income",
                "acc-inc-j-dr-amount": scenario["amount"],
                "acc-inc-j-cr-details": income_label,
                "acc-inc-j-cr-amount": scenario["amount"],
                "acc-inc-j-rev-dr-details": income_label,
                "acc-inc-j-rev-dr-amount": scenario["amount"],
                "acc-inc-j-rev-cr-details": "Accrued income",
                "acc-inc-j-rev-cr-amount": scenario["amount"],
            },
            derivation_map={
                "acc-inc-j-dr-amount": f"Use the accrued income amount given: R{int(scenario['amount']):,}",
                "acc-inc-j-rev-dr-amount": f"The reversal uses the same amount as the year-end adjustment: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "acc-inc-j-dr-details": "At year-end, debit the Accrued income asset account.",
                "acc-inc-j-cr-details": f"Credit the related income account: {income_label}.",
                "acc-inc-j-rev-dr-details": "The reversal swaps the original credit entry to the debit side.",
                "acc-inc-j-rev-cr-details": "The reversal recreates the opposite entry in Accrued income.",
            },
            guidelines=[
                f"Year-end: Dr Accrued income / Cr {income_label}.",
                f"Reversal next period: Dr {income_label} / Cr Accrued income.",
            ],
            marks=8,
        ), "accrued_income_reversal_journal_fill", expected_cells=8, amount=scenario["amount"], amount_cell_ids=["acc-inc-j-dr-amount", "acc-inc-j-cr-amount", "acc-inc-j-rev-dr-amount", "acc-inc-j-rev-cr-amount"]))
        accrued_income_analysis_table = {
            "heading": f"Adjustment analysis: {str(income_label).lower()}",
            "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
            "rows": [
                [_cell(f"{income_label} earned but not yet received"), _cell("", editable=True, cell_id="acc-inc-a-amount"), _cell("", editable=True, cell_id="acc-inc-a-dr"), _cell("", editable=True, cell_id="acc-inc-a-cr"), _cell("", editable=True, cell_id="acc-inc-a-is"), _cell("", editable=True, cell_id="acc-inc-a-bs")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="adjustment_analysis_table",
            prompt=f"{scenario['prompt_intro']} Complete the adjustment analysis table for the year-end adjustment.",
            table=accrued_income_analysis_table,
            correct_map={
                "acc-inc-a-amount": scenario["amount"],
                "acc-inc-a-dr": "Accrued income",
                "acc-inc-a-cr": income_label,
                "acc-inc-a-is": "Income increases by R" + f"{int(scenario['amount']):,}",
                "acc-inc-a-bs": "Current asset increases by R" + f"{int(scenario['amount']):,}",
            },
            derivation_map={
                "acc-inc-a-amount": f"Use the amount still receivable at year-end: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "acc-inc-a-dr": "Amounts receivable are assets, so the asset account is debited.",
                "acc-inc-a-cr": "The income account is credited because the income has been earned.",
                "acc-inc-a-bs": "The adjustment creates a current asset on the Balance Sheet.",
            },
            guidelines=[
                "Accrued income increases income and creates a current asset.",
                "Use the same amount in the double entry and in the statement effects.",
            ],
            marks=6,
        ), "accrued_income_analysis_fill", expected_cells=5, amount=scenario["amount"], amount_cell_id="acc-inc-a-amount"))
        accrued_income_carry_tables = [
            {
                "heading": "Income Statement extract",
                "headers": ["Other income", "Amount"],
                "rows": [[_cell(income_label), _cell("", editable=True, cell_id="acc-inc-fa-income")]],
            },
            {
                "heading": "Balance Sheet extract",
                "headers": ["Current assets", "Amount"],
                "rows": [[_cell("Accrued income"), _cell("", editable=True, cell_id="acc-inc-fa-asset")]],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the source extract and year-end adjustment to carry the effect of the accrual into the Income Statement and Balance Sheet extracts for {str(income_label).lower()}.",
            prompt_table={
                "heading": "Source extract",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell(f"{income_label} before adjustment"), _cell(scenario["base_balance"])],
                    [_cell("Accrued income adjustment"), _cell(scenario["amount"])],
                ],
            },
            tables=accrued_income_carry_tables,
            correct_map={
                "acc-inc-fa-income": adjusted_income_balance,
                "acc-inc-fa-asset": scenario["amount"],
            },
            derivation_map={
                "acc-inc-fa-income": f"Adjusted {income_label} = R{int(scenario['base_balance']):,} + R{int(scenario['amount']):,} = R{int(adjusted_income_balance):,}",
                "acc-inc-fa-asset": f"Carry the accrued income amount to Current assets: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "acc-inc-fa-income": f"Increase {str(income_label).lower()} by the amount still receivable.",
                "acc-inc-fa-asset": "Amounts still receivable appear as a current asset on the Balance Sheet.",
            },
            guidelines=[
                f"Add the accrual to the {income_label} figure in the Income Statement.",
                "Carry the same amount to Accrued income under Current assets.",
            ],
            marks=4,
        ), "accrued_income_carrythrough_fill", expected_cells=2, adjusted_amount=adjusted_income_balance, carry_amount=scenario["amount"], adjusted_cell_id="acc-inc-fa-income", carry_cell_id="acc-inc-fa-asset"))
        accrued_income_tb_bank = _round_money(float(scenario["base_balance"]) + 42000.0)
        accrued_income_tb_stock = _round_money(float(scenario["amount"]) + 18000.0)
        accrued_income_tb_capital = _round_money(float(accrued_income_tb_bank) + float(accrued_income_tb_stock) - float(scenario["base_balance"]))
        accrued_income_tb_total = _round_money(float(accrued_income_tb_bank) + float(accrued_income_tb_stock) + float(scenario["amount"]))
        accrued_income_tb_prompt_tables = [
            {
                "heading": "Pre-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell(accrued_income_tb_bank), _cell("")],
                    [_cell("Trading stock"), _cell(accrued_income_tb_stock), _cell("")],
                    [_cell(income_label), _cell(""), _cell(scenario["base_balance"])],
                    [_cell("Capital"), _cell(""), _cell(accrued_income_tb_capital)],
                ],
            },
            {
                "heading": "Year-end adjustment",
                "headers": ["Adjustment", "Amount"],
                "rows": [[_cell(f"{income_label} owing at year-end"), _cell(scenario["amount"])]]
            },
        ]
        accrued_income_tb_table = {
            "heading": "Post-adjustment Trial Balance extract",
            "headers": ["Account", "Debit", "Credit"],
            "rows": [
                [_cell("Bank"), _cell("", editable=True, cell_id="acc-inc-patb-bank-debit"), _cell("")],
                [_cell("Trading stock"), _cell("", editable=True, cell_id="acc-inc-patb-stock-debit"), _cell("")],
                [_cell("Accrued income"), _cell("", editable=True, cell_id="acc-inc-patb-asset-debit"), _cell("")],
                [_cell(income_label), _cell(""), _cell("", editable=True, cell_id="acc-inc-patb-income-credit")],
                [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="acc-inc-patb-capital-credit")],
                [_cell("Total"), _cell("", editable=True, cell_id="acc-inc-patb-total-debit"), _cell("", editable=True, cell_id="acc-inc-patb-total-credit")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="trial_balance_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the year-end adjustment to complete the Post-adjustment Trial Balance extract for the accrued {str(income_label).lower()}.",
            prompt_tables=accrued_income_tb_prompt_tables,
            table=accrued_income_tb_table,
            correct_map={
                "acc-inc-patb-bank-debit": accrued_income_tb_bank,
                "acc-inc-patb-stock-debit": accrued_income_tb_stock,
                "acc-inc-patb-asset-debit": scenario["amount"],
                "acc-inc-patb-income-credit": adjusted_income_balance,
                "acc-inc-patb-capital-credit": accrued_income_tb_capital,
                "acc-inc-patb-total-debit": accrued_income_tb_total,
                "acc-inc-patb-total-credit": accrued_income_tb_total,
            },
            derivation_map={
                "acc-inc-patb-income-credit": f"Adjusted {income_label} = R{int(scenario['base_balance']):,} + R{int(scenario['amount']):,} = R{int(adjusted_income_balance):,}",
                "acc-inc-patb-total-debit": f"Total debit = Bank + Trading stock + Accrued income = R{int(accrued_income_tb_bank):,} + R{int(accrued_income_tb_stock):,} + R{int(scenario['amount']):,} = R{int(accrued_income_tb_total):,}",
            },
            cell_hints={
                "acc-inc-patb-asset-debit": "The accrued amount becomes a current asset in the debit column.",
                "acc-inc-patb-income-credit": f"Increase {str(income_label).lower()} by the amount still receivable.",
                "acc-inc-patb-total-debit": "Total all debit balances after adding the new accrued income asset.",
            },
            guidelines=[
                "Copy unchanged balances from the Pre-adjustment Trial Balance.",
                f"Add the accrual to {income_label} and show the same amount as Accrued income on the debit side.",
            ],
            marks=7,
        ), "accrued_income_post_adjustment_tb_fill", expected_cells=7, total=accrued_income_tb_total, adjusted_amount=adjusted_income_balance, carry_amount=scenario["amount"], adjusted_cell_id="acc-inc-patb-income-credit", carry_cell_id="acc-inc-patb-asset-debit", total_debit_cell_id="acc-inc-patb-total-debit", total_credit_cell_id="acc-inc-patb-total-credit"))
        accrued_income_mini_tables = [
            {
                "heading": "Part A: General Journal",
                "headers": ["Date", "Details", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-inc-mini-j-dr-details"), _cell("", editable=True, cell_id="acc-inc-mini-j-dr-amount"), _cell("")],
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-inc-mini-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="acc-inc-mini-j-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-inc-mini-j-rev-dr-details"), _cell("", editable=True, cell_id="acc-inc-mini-j-rev-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-inc-mini-j-rev-cr-details"), _cell(""), _cell("", editable=True, cell_id="acc-inc-mini-j-rev-cr-amount")],
                ],
            },
            {
                "heading": "Part B: Adjustment analysis",
                "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
                "rows": [
                    [_cell(f"{income_label} earned but not yet received"), _cell("", editable=True, cell_id="acc-inc-mini-a-amount"), _cell("", editable=True, cell_id="acc-inc-mini-a-dr"), _cell("", editable=True, cell_id="acc-inc-mini-a-cr"), _cell("", editable=True, cell_id="acc-inc-mini-a-is"), _cell("", editable=True, cell_id="acc-inc-mini-a-bs")],
                ],
            },
            {
                "heading": "Part C1: Income Statement extract",
                "headers": ["Other income", "Amount"],
                "rows": [[_cell(income_label), _cell("", editable=True, cell_id="acc-inc-mini-fa-income")]],
            },
            {
                "heading": "Part C2: Balance Sheet extract",
                "headers": ["Current assets", "Amount"],
                "rows": [[_cell("Accrued income"), _cell("", editable=True, cell_id="acc-inc-mini-fa-asset")]],
            },
            {
                "heading": "Part D: Post-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="acc-inc-mini-patb-bank-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="acc-inc-mini-patb-stock-debit"), _cell("")],
                    [_cell("Accrued income"), _cell("", editable=True, cell_id="acc-inc-mini-patb-asset-debit"), _cell("")],
                    [_cell(income_label), _cell(""), _cell("", editable=True, cell_id="acc-inc-mini-patb-income-credit")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="acc-inc-mini-patb-capital-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="acc-inc-mini-patb-total-debit"), _cell("", editable=True, cell_id="acc-inc-mini-patb-total-credit")],
                ],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the year-end adjustment to complete the integrated reversal mini-project for accrued {str(income_label).lower()}: (A) General Journal adjustment and reversal, (B) adjustment analysis, (C) Income Statement and Balance Sheet extracts, and (D) Post-adjustment Trial Balance extract.",
            prompt_tables=accrued_income_tb_prompt_tables,
            tables=accrued_income_mini_tables,
            correct_map={
                "acc-inc-mini-j-dr-details": "Accrued income",
                "acc-inc-mini-j-dr-amount": scenario["amount"],
                "acc-inc-mini-j-cr-details": income_label,
                "acc-inc-mini-j-cr-amount": scenario["amount"],
                "acc-inc-mini-j-rev-dr-details": income_label,
                "acc-inc-mini-j-rev-dr-amount": scenario["amount"],
                "acc-inc-mini-j-rev-cr-details": "Accrued income",
                "acc-inc-mini-j-rev-cr-amount": scenario["amount"],
                "acc-inc-mini-a-amount": scenario["amount"],
                "acc-inc-mini-a-dr": "Accrued income",
                "acc-inc-mini-a-cr": income_label,
                "acc-inc-mini-a-is": "Income increases by R" + f"{int(scenario['amount']):,}",
                "acc-inc-mini-a-bs": "Current asset increases by R" + f"{int(scenario['amount']):,}",
                "acc-inc-mini-fa-income": adjusted_income_balance,
                "acc-inc-mini-fa-asset": scenario["amount"],
                "acc-inc-mini-patb-bank-debit": accrued_income_tb_bank,
                "acc-inc-mini-patb-stock-debit": accrued_income_tb_stock,
                "acc-inc-mini-patb-asset-debit": scenario["amount"],
                "acc-inc-mini-patb-income-credit": adjusted_income_balance,
                "acc-inc-mini-patb-capital-credit": accrued_income_tb_capital,
                "acc-inc-mini-patb-total-debit": accrued_income_tb_total,
                "acc-inc-mini-patb-total-credit": accrued_income_tb_total,
            },
            derivation_map={
                "acc-inc-mini-fa-income": f"Adjusted {income_label} = R{int(scenario['base_balance']):,} + R{int(scenario['amount']):,} = R{int(adjusted_income_balance):,}",
                "acc-inc-mini-patb-income-credit": f"Carry the adjusted {income_label} figure from Part C1 into Part D: R{int(adjusted_income_balance):,}",
                "acc-inc-mini-patb-total-debit": f"Total debit = Bank + Trading stock + Accrued income = R{int(accrued_income_tb_bank):,} + R{int(accrued_income_tb_stock):,} + R{int(scenario['amount']):,} = R{int(accrued_income_tb_total):,}",
            },
            cell_hints={
                "acc-inc-mini-j-dr-details": "The year-end journal starts with the accrued income asset account on the debit side.",
                "acc-inc-mini-a-cr": "The related income account is credited because the income was earned in this period.",
                "acc-inc-mini-fa-income": "Add the accrual to the income balance before carrying it to the statements.",
                "acc-inc-mini-patb-asset-debit": "The same accrued amount appears as an asset in the Post-adjustment Trial Balance.",
                "acc-inc-mini-patb-total-debit": "Use the completed balances in Part D to total the debit column.",
            },
            cell_teaching_map={
                "acc-inc-mini-fa-income": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {str(income_label).lower()} amount into the Income Statement extract.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance shows {income_label} at R{int(scenario['base_balance']):,} and the year-end adjustment adds R{int(scenario['amount']):,}.",
                    rule_or_principle="Accrued income belongs to the current period and increases the income account.",
                    how_to_derive=f"R{int(scenario['base_balance']):,} + R{int(scenario['amount']):,} = R{int(adjusted_income_balance):,}.",
                    transfer_tip="In integrated adjustment questions, update the nominal account first, then carry the adjusted figure into later statement sections.",
                ),
                "acc-inc-mini-patb-asset-debit": _teaching_hint(
                    role_in_requirement="This cell shows the new asset created by the accrual in the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The adjustment table and journal both use Accrued income for the amount R{int(scenario['amount']):,}.",
                    rule_or_principle="Income owing at year-end is a current asset and must appear in the debit column of the adjusted trial balance.",
                    how_to_derive=f"Enter Accrued income at R{int(scenario['amount']):,} in the debit column.",
                    transfer_tip="When an adjustment creates a new asset or liability, check whether that new account must also appear in the trial balance.",
                ),
            },
            guidelines=[
                "Carry the same accrued amount consistently through the journal, analysis, statements, and trial balance.",
                "Use the adjusted income figure in both the Income Statement extract and the Post-adjustment Trial Balance.",
            ],
            marks=22,
        ), "accrued_income_reversal_mini_project", expected_cells=22, amount=scenario["amount"], amount_cell_ids=["acc-inc-mini-j-dr-amount", "acc-inc-mini-j-cr-amount", "acc-inc-mini-j-rev-dr-amount", "acc-inc-mini-j-rev-cr-amount", "acc-inc-mini-a-amount", "acc-inc-mini-fa-asset", "acc-inc-mini-patb-asset-debit"], adjusted_amount=adjusted_income_balance, adjusted_cell_ids=["acc-inc-mini-fa-income", "acc-inc-mini-patb-income-credit"], total=accrued_income_tb_total, total_debit_cell_id="acc-inc-mini-patb-total-debit", total_credit_cell_id="acc-inc-mini-patb-total-credit"))
        accrued_income_exam_tables = [
            {
                "heading": "Part A1: Accrued income account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-inc-ex-asset-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="acc-inc-ex-asset-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-inc-ex-asset-rev-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="acc-inc-ex-asset-rev-amount")],
                ],
            },
            {
                "heading": f"Part A2: {income_label} account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-inc-ex-income-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="acc-inc-ex-income-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-inc-ex-income-rev-details"), _cell("GJ"), _cell("", editable=True, cell_id="acc-inc-ex-income-rev-amount"), _cell("")],
                ],
            },
            {
                "heading": "Part B1: Income Statement extract",
                "headers": ["Other income", "Amount"],
                "rows": [[_cell(income_label), _cell("", editable=True, cell_id="acc-inc-ex-fa-income")]],
            },
            {
                "heading": "Part B2: Balance Sheet extract",
                "headers": ["Current assets", "Amount"],
                "rows": [[_cell("Accrued income"), _cell("", editable=True, cell_id="acc-inc-ex-fa-asset")]],
            },
            {
                "heading": "Part C: Post-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="acc-inc-ex-patb-bank-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="acc-inc-ex-patb-stock-debit"), _cell("")],
                    [_cell("Accrued income"), _cell("", editable=True, cell_id="acc-inc-ex-patb-asset-debit"), _cell("")],
                    [_cell(income_label), _cell(""), _cell("", editable=True, cell_id="acc-inc-ex-patb-income-credit")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="acc-inc-ex-patb-capital-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="acc-inc-ex-patb-total-debit"), _cell("", editable=True, cell_id="acc-inc-ex-patb-total-credit")],
                ],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the accrued income adjustment to complete the integrated accrued income workflow for accrued {str(income_label).lower()}: (A) post the year-end adjustment and the reversal to the ledger accounts, (B) carry the effect to the Income Statement and Balance Sheet extracts, and (C) complete the Post-adjustment Trial Balance extract.",
            prompt_tables=accrued_income_tb_prompt_tables,
            tables=accrued_income_exam_tables,
            correct_map={
                "acc-inc-ex-asset-dr-details": income_label,
                "acc-inc-ex-asset-dr-amount": scenario["amount"],
                "acc-inc-ex-asset-rev-details": income_label,
                "acc-inc-ex-asset-rev-amount": scenario["amount"],
                "acc-inc-ex-income-cr-details": "Accrued income",
                "acc-inc-ex-income-cr-amount": scenario["amount"],
                "acc-inc-ex-income-rev-details": "Accrued income",
                "acc-inc-ex-income-rev-amount": scenario["amount"],
                "acc-inc-ex-fa-income": adjusted_income_balance,
                "acc-inc-ex-fa-asset": scenario["amount"],
                "acc-inc-ex-patb-bank-debit": accrued_income_tb_bank,
                "acc-inc-ex-patb-stock-debit": accrued_income_tb_stock,
                "acc-inc-ex-patb-asset-debit": scenario["amount"],
                "acc-inc-ex-patb-income-credit": adjusted_income_balance,
                "acc-inc-ex-patb-capital-credit": accrued_income_tb_capital,
                "acc-inc-ex-patb-total-debit": accrued_income_tb_total,
                "acc-inc-ex-patb-total-credit": accrued_income_tb_total,
            },
            derivation_map={
                "acc-inc-ex-asset-rev-amount": f"The reversal uses the same amount as the year-end accrual: R{int(scenario['amount']):,}",
                "acc-inc-ex-fa-income": f"Adjusted {income_label} = R{int(scenario['base_balance']):,} + R{int(scenario['amount']):,} = R{int(adjusted_income_balance):,}",
                "acc-inc-ex-patb-income-credit": f"Carry the adjusted {income_label} amount into the credit column of the Post-adjustment Trial Balance: R{int(adjusted_income_balance):,}",
                "acc-inc-ex-patb-total-debit": f"Total debit = Bank + Trading stock + Accrued income = R{int(accrued_income_tb_bank):,} + R{int(accrued_income_tb_stock):,} + R{int(scenario['amount']):,} = R{int(accrued_income_tb_total):,}",
            },
            cell_hints={
                "acc-inc-ex-asset-dr-details": "In the Accrued income account, the details column shows the opposite account from the journal entry.",
                "acc-inc-ex-income-cr-details": "In the income account, use the opposite account from the accrual entry in the details column.",
                "acc-inc-ex-fa-income": "Add the accrual to the existing income balance before carrying it into the statement extract.",
                "acc-inc-ex-patb-asset-debit": "The accrued amount becomes a current asset in the adjusted trial balance.",
                "acc-inc-ex-patb-total-debit": "Use all completed debit balances in Part C to total the column.",
            },
            cell_teaching_map={
                "acc-inc-ex-fa-income": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {str(income_label).lower()} figure into the Income Statement extract.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance gives {income_label} at R{int(scenario['base_balance']):,} and the year-end adjustment adds R{int(scenario['amount']):,}.",
                    rule_or_principle="Accrued income belongs to the current accounting period, so it increases the related income account.",
                    how_to_derive=f"Add R{int(scenario['amount']):,} to R{int(scenario['base_balance']):,} to get R{int(adjusted_income_balance):,}.",
                    transfer_tip="In integrated adjustment workflows, update the nominal account first and then carry the adjusted figure into later statement sections.",
                ),
                "acc-inc-ex-patb-asset-debit": _teaching_hint(
                    role_in_requirement="This cell shows the asset created by the accrual in the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The year-end adjustment creates Accrued income for R{int(scenario['amount']):,}.",
                    rule_or_principle="Income owing at year-end is a current asset and appears in the debit column of the adjusted trial balance.",
                    how_to_derive=f"Enter Accrued income at R{int(scenario['amount']):,} on the debit side.",
                    transfer_tip="When an adjustment creates a new asset, check whether that account must be added to the adjusted trial balance.",
                ),
            },
            guidelines=[
                "Post the accrual and the reversal using the same amount in both ledger accounts.",
                "Carry the adjusted income figure consistently into the Income Statement and the Post-adjustment Trial Balance.",
                "Show the accrued amount as a current asset in both the Balance Sheet extract and the Post-adjustment Trial Balance.",
            ],
            marks=17,
        ), "accrued_income_reversal_mini_project", expected_cells=17, amount=scenario["amount"], amount_cell_ids=["acc-inc-ex-asset-dr-amount", "acc-inc-ex-asset-rev-amount", "acc-inc-ex-income-cr-amount", "acc-inc-ex-income-rev-amount", "acc-inc-ex-fa-asset", "acc-inc-ex-patb-asset-debit"], adjusted_amount=adjusted_income_balance, adjusted_cell_ids=["acc-inc-ex-fa-income", "acc-inc-ex-patb-income-credit"], total=accrued_income_tb_total, total_debit_cell_id="acc-inc-ex-patb-total-debit", total_credit_cell_id="acc-inc-ex-patb-total-credit"))
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="ledger",
            prompt=f"{scenario['prompt_intro']} Post the year-end adjustment dated {scenario['year_end_date']} and the reversal on {scenario['reversal_date']}.",
            tables=accrued_income_ledger_tables,
            correct_map={
                "acc-inc-dr-details": income_label,
                "acc-inc-dr-amount": scenario["amount"],
                "acc-inc-rev-details": income_label,
                "acc-inc-rev-amount": scenario["amount"],
                "rent-inc-cr-details": "Accrued income",
                "rent-inc-cr-amount": scenario["amount"],
                "rent-inc-rev-details": "Accrued income",
                "rent-inc-rev-amount": scenario["amount"],
            },
            derivation_map={
                "acc-inc-dr-amount": f"Use the outstanding amount at year-end: R{int(scenario['amount']):,}",
                "acc-inc-rev-amount": f"Reverse the exact same amount at the start of the next period: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "acc-inc-dr-details": f"At year-end, the Accrued income asset is paired with the {str(income_label).lower()} account.",
                "acc-inc-rev-details": "The reversal uses the opposite account name in the details column.",
                "rent-inc-cr-details": "The income account shows the opposite account in the details column.",
                "rent-inc-rev-details": "On reversal day, the income account uses Accrued income as the details entry.",
            },
            cell_teaching_map={
                "acc-inc-dr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the opposite account for the year-end debit in the Accrued income account.",
                    evidence_from_question=f"The year-end adjustment is Dr Accrued income / Cr {income_label}.",
                    rule_or_principle="In ledger posting, the details column shows the opposite account in the journal entry.",
                    how_to_derive=f"Because Accrued income is debited, the details entry is {income_label}.",
                    transfer_tip="When posting any adjustment, first identify the double entry and then write the opposite account in the details column.",
                ),
                "acc-inc-rev-amount": _teaching_hint(
                    role_in_requirement="This cell records the reversal amount at the start of the new period.",
                    evidence_from_question=f"The question tells you to reverse the year-end adjustment on {scenario['reversal_date']}.",
                    rule_or_principle="A reversal uses the exact same amount as the original year-end adjustment.",
                    how_to_derive=f"Copy the original accrued income amount R{int(scenario['amount']):,} into the reversal entry.",
                    transfer_tip="For reversal entries, change the side of the entry but do not change the amount.",
                ),
                "rent-inc-rev-details": _teaching_hint(
                    role_in_requirement=f"This cell identifies the opposite account for the reversal entry in the {income_label} account.",
                    evidence_from_question="The reversal removes the original accrual from the income account at the start of the next period.",
                    rule_or_principle="The reversing entry swaps the debit and credit accounts used at year-end.",
                    how_to_derive="The original opposite account was Accrued income, so that remains the details entry on reversal.",
                    transfer_tip="Write the opposite account name consistently in both ledgers when reversing an adjustment.",
                ),
            },
            guidelines=[
                f"Year-end: Dr Accrued income / Cr {income_label}.",
                f"Reversal next year: Dr {income_label} / Cr Accrued income.",
            ],
            marks=8,
        ), "accrued_income_reversal_ledger_fill", expected_cells=8, amount=scenario["amount"], amount_cell_ids=["acc-inc-dr-amount", "acc-inc-rev-amount", "rent-inc-cr-amount", "rent-inc-rev-amount"]))

    accrued_expense_ledger_scenarios = [
        {
            "expense_label": "Telephone",
            "amount": accrued_expense_amount,
            "base_balance": 7200,
            "year_end_date": "28 Feb 2026",
            "reversal_date": "1 Mar 2026",
            "prompt_intro": f"{biz} still owes telephone expenses of R{accrued_expense_amount:,} at year-end.",
        },
        {
            "expense_label": "Wages",
            "amount": _round_money(r.choice([1400, 2200, 2800, 3600])),
            "base_balance": 15600,
            "year_end_date": "30 Jun 2026",
            "reversal_date": "1 Jul 2026",
            "prompt_intro": "",
        },
        {
            "expense_label": "Water and electricity",
            "amount": _round_money(r.choice([800, 1100, 1600, 2400])),
            "base_balance": 9600,
            "year_end_date": "31 Dec 2026",
            "reversal_date": "1 Jan 2027",
            "prompt_intro": "",
        },
    ]
    accrued_expense_ledger_scenarios[1]["prompt_intro"] = f"{biz} still owes wages of R{int(accrued_expense_ledger_scenarios[1]['amount']):,} at 30 June 2026."
    accrued_expense_ledger_scenarios[2]["prompt_intro"] = f"{biz} still owes water and electricity of R{int(accrued_expense_ledger_scenarios[2]['amount']):,} at year-end."
    for scenario in accrued_expense_ledger_scenarios:
        expense_label = str(scenario["expense_label"])
        adjusted_expense_balance = _round_money(float(scenario["base_balance"]) + float(scenario["amount"]))
        accrued_expense_ledger_tables = [
            {
                "heading": "Accrued expenses account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-exp-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="acc-exp-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-exp-rev-details"), _cell("GJ"), _cell("", editable=True, cell_id="acc-exp-rev-amount"), _cell("")],
                ],
            },
            {
                "heading": f"{expense_label} account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="tel-exp-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="tel-exp-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="tel-exp-rev-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="tel-exp-rev-amount")],
                ],
            },
        ]
        accrued_expense_journal_table = {
            "heading": "General Journal",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-exp-j-dr-details"), _cell("", editable=True, cell_id="acc-exp-j-dr-amount"), _cell("")],
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-exp-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="acc-exp-j-cr-amount")],
                [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-exp-j-rev-dr-details"), _cell("", editable=True, cell_id="acc-exp-j-rev-dr-amount"), _cell("")],
                [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-exp-j-rev-cr-details"), _cell(""), _cell("", editable=True, cell_id="acc-exp-j-rev-cr-amount")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=f"{scenario['prompt_intro']} Prepare the General Journal entry for the year-end adjustment dated {scenario['year_end_date']} and the reversal on {scenario['reversal_date']}.",
            table=accrued_expense_journal_table,
            correct_map={
                "acc-exp-j-dr-details": expense_label,
                "acc-exp-j-dr-amount": scenario["amount"],
                "acc-exp-j-cr-details": "Accrued expenses",
                "acc-exp-j-cr-amount": scenario["amount"],
                "acc-exp-j-rev-dr-details": "Accrued expenses",
                "acc-exp-j-rev-dr-amount": scenario["amount"],
                "acc-exp-j-rev-cr-details": expense_label,
                "acc-exp-j-rev-cr-amount": scenario["amount"],
            },
            derivation_map={
                "acc-exp-j-dr-amount": f"Use the accrued expense amount given: R{int(scenario['amount']):,}",
                "acc-exp-j-rev-dr-amount": f"The reversal uses the same amount as the year-end adjustment: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "acc-exp-j-dr-details": f"At year-end, debit the expense account: {expense_label}.",
                "acc-exp-j-cr-details": "The unpaid amount is credited to Accrued expenses.",
                "acc-exp-j-rev-dr-details": "The reversal debits the liability account first.",
                "acc-exp-j-rev-cr-details": "The reversal credits the original expense account.",
            },
            guidelines=[
                f"Year-end: Dr {expense_label} / Cr Accrued expenses.",
                f"Reversal next period: Dr Accrued expenses / Cr {expense_label}.",
            ],
            marks=8,
        ), "accrued_expense_reversal_journal_fill", expected_cells=8, amount=scenario["amount"], amount_cell_ids=["acc-exp-j-dr-amount", "acc-exp-j-cr-amount", "acc-exp-j-rev-dr-amount", "acc-exp-j-rev-cr-amount"]))
        accrued_expense_analysis_table = {
            "heading": f"Adjustment analysis: {str(expense_label).lower()}",
            "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
            "rows": [
                [_cell(f"{expense_label} incurred but not yet paid"), _cell("", editable=True, cell_id="acc-exp-a-amount"), _cell("", editable=True, cell_id="acc-exp-a-dr"), _cell("", editable=True, cell_id="acc-exp-a-cr"), _cell("", editable=True, cell_id="acc-exp-a-is"), _cell("", editable=True, cell_id="acc-exp-a-bs")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="adjustment_analysis_table",
            prompt=f"{scenario['prompt_intro']} Complete the adjustment analysis table for the year-end adjustment.",
            table=accrued_expense_analysis_table,
            correct_map={
                "acc-exp-a-amount": scenario["amount"],
                "acc-exp-a-dr": expense_label,
                "acc-exp-a-cr": "Accrued expenses",
                "acc-exp-a-is": "Expense increases by R" + f"{int(scenario['amount']):,}",
                "acc-exp-a-bs": "Current liability increases by R" + f"{int(scenario['amount']):,}",
            },
            derivation_map={
                "acc-exp-a-amount": f"Use the amount still owing at year-end: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "acc-exp-a-dr": "Outstanding expenses increase the relevant expense account.",
                "acc-exp-a-cr": "The unpaid amount creates a current liability.",
                "acc-exp-a-bs": "The Balance Sheet effect is a current liability increase.",
            },
            guidelines=[
                "Accrued expenses increase expenses and create current liabilities.",
                "Use the same amount in the double entry and in the statement effects.",
            ],
            marks=6,
        ), "accrued_expense_analysis_fill", expected_cells=5, amount=scenario["amount"], amount_cell_id="acc-exp-a-amount"))
        accrued_expense_carry_tables = [
            {
                "heading": "Income Statement extract",
                "headers": ["Expenses", "Amount"],
                "rows": [[_cell(expense_label), _cell("", editable=True, cell_id="acc-exp-fa-expense")]],
            },
            {
                "heading": "Balance Sheet extract",
                "headers": ["Current liabilities", "Amount"],
                "rows": [[_cell("Accrued expenses"), _cell("", editable=True, cell_id="acc-exp-fa-liability")]],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the source extract and year-end adjustment to carry the effect of the outstanding {str(expense_label).lower()} into the Income Statement and Balance Sheet extracts.",
            prompt_table={
                "heading": "Source extract",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell(f"{expense_label} before adjustment"), _cell(scenario["base_balance"])],
                    [_cell("Accrued expense adjustment"), _cell(scenario["amount"])],
                ],
            },
            tables=accrued_expense_carry_tables,
            correct_map={
                "acc-exp-fa-expense": adjusted_expense_balance,
                "acc-exp-fa-liability": scenario["amount"],
            },
            derivation_map={
                "acc-exp-fa-expense": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} + R{int(scenario['amount']):,} = R{int(adjusted_expense_balance):,}",
                "acc-exp-fa-liability": f"Carry the outstanding amount to Current liabilities: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "acc-exp-fa-expense": f"Add the unpaid amount to the {str(expense_label).lower()} line in the Income Statement.",
                "acc-exp-fa-liability": "Carry the same amount to Accrued expenses under Current liabilities.",
            },
            guidelines=[
                f"Add the accrual to the {expense_label} figure in the Income Statement.",
                "Carry the same amount to Accrued expenses under Current liabilities.",
            ],
            marks=4,
        ), "accrued_expense_carrythrough_fill", expected_cells=2, adjusted_amount=adjusted_expense_balance, carry_amount=scenario["amount"], adjusted_cell_id="acc-exp-fa-expense", carry_cell_id="acc-exp-fa-liability"))
        accrued_expense_tb_bank = _round_money(float(scenario["base_balance"]) + 36000.0)
        accrued_expense_tb_stock = _round_money(float(scenario["amount"]) + 20000.0)
        accrued_expense_tb_capital = _round_money(float(accrued_expense_tb_bank) + float(accrued_expense_tb_stock) + float(scenario["base_balance"]))
        accrued_expense_tb_total = _round_money(float(accrued_expense_tb_bank) + float(accrued_expense_tb_stock) + float(adjusted_expense_balance))
        accrued_expense_tb_prompt_tables = [
            {
                "heading": "Pre-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell(accrued_expense_tb_bank), _cell("")],
                    [_cell("Trading stock"), _cell(accrued_expense_tb_stock), _cell("")],
                    [_cell(expense_label), _cell(scenario["base_balance"]), _cell("")],
                    [_cell("Capital"), _cell(""), _cell(accrued_expense_tb_capital)],
                ],
            },
            {
                "heading": "Year-end adjustment",
                "headers": ["Adjustment", "Amount"],
                "rows": [[_cell(f"{expense_label} owing at year-end"), _cell(scenario["amount"])]]
            },
        ]
        accrued_expense_tb_table = {
            "heading": "Post-adjustment Trial Balance extract",
            "headers": ["Account", "Debit", "Credit"],
            "rows": [
                [_cell("Bank"), _cell("", editable=True, cell_id="acc-exp-patb-bank-debit"), _cell("")],
                [_cell("Trading stock"), _cell("", editable=True, cell_id="acc-exp-patb-stock-debit"), _cell("")],
                [_cell(expense_label), _cell("", editable=True, cell_id="acc-exp-patb-expense-debit"), _cell("")],
                [_cell("Accrued expenses"), _cell(""), _cell("", editable=True, cell_id="acc-exp-patb-liability-credit")],
                [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="acc-exp-patb-capital-credit")],
                [_cell("Total"), _cell("", editable=True, cell_id="acc-exp-patb-total-debit"), _cell("", editable=True, cell_id="acc-exp-patb-total-credit")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="trial_balance_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the year-end adjustment to complete the Post-adjustment Trial Balance extract for the outstanding {str(expense_label).lower()}.",
            prompt_tables=accrued_expense_tb_prompt_tables,
            table=accrued_expense_tb_table,
            correct_map={
                "acc-exp-patb-bank-debit": accrued_expense_tb_bank,
                "acc-exp-patb-stock-debit": accrued_expense_tb_stock,
                "acc-exp-patb-expense-debit": adjusted_expense_balance,
                "acc-exp-patb-liability-credit": scenario["amount"],
                "acc-exp-patb-capital-credit": accrued_expense_tb_capital,
                "acc-exp-patb-total-debit": accrued_expense_tb_total,
                "acc-exp-patb-total-credit": accrued_expense_tb_total,
            },
            derivation_map={
                "acc-exp-patb-expense-debit": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} + R{int(scenario['amount']):,} = R{int(adjusted_expense_balance):,}",
                "acc-exp-patb-total-debit": f"Total debit = Bank + Trading stock + adjusted {expense_label} = R{int(accrued_expense_tb_bank):,} + R{int(accrued_expense_tb_stock):,} + R{int(adjusted_expense_balance):,} = R{int(accrued_expense_tb_total):,}",
            },
            cell_hints={
                "acc-exp-patb-expense-debit": f"Add the outstanding amount to the {str(expense_label).lower()} expense balance.",
                "acc-exp-patb-liability-credit": "Show the same unpaid amount as a current liability.",
                "acc-exp-patb-total-debit": "Total all debit balances after adjusting the expense account.",
            },
            guidelines=[
                "Copy unchanged balances from the Pre-adjustment Trial Balance.",
                f"Add the accrual to {expense_label} and show the same amount as Accrued expenses on the credit side.",
            ],
            marks=7,
        ), "accrued_expense_post_adjustment_tb_fill", expected_cells=7, total=accrued_expense_tb_total, adjusted_amount=adjusted_expense_balance, carry_amount=scenario["amount"], adjusted_cell_id="acc-exp-patb-expense-debit", carry_cell_id="acc-exp-patb-liability-credit", total_debit_cell_id="acc-exp-patb-total-debit", total_credit_cell_id="acc-exp-patb-total-credit"))
        accrued_expense_mini_tables = [
            {
                "heading": "Part A: General Journal",
                "headers": ["Date", "Details", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-exp-mini-j-dr-details"), _cell("", editable=True, cell_id="acc-exp-mini-j-dr-amount"), _cell("")],
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-exp-mini-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="acc-exp-mini-j-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-exp-mini-j-rev-dr-details"), _cell("", editable=True, cell_id="acc-exp-mini-j-rev-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-exp-mini-j-rev-cr-details"), _cell(""), _cell("", editable=True, cell_id="acc-exp-mini-j-rev-cr-amount")],
                ],
            },
            {
                "heading": "Part B: Adjustment analysis",
                "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
                "rows": [
                    [_cell(f"{expense_label} incurred but not yet paid"), _cell("", editable=True, cell_id="acc-exp-mini-a-amount"), _cell("", editable=True, cell_id="acc-exp-mini-a-dr"), _cell("", editable=True, cell_id="acc-exp-mini-a-cr"), _cell("", editable=True, cell_id="acc-exp-mini-a-is"), _cell("", editable=True, cell_id="acc-exp-mini-a-bs")],
                ],
            },
            {
                "heading": "Part C1: Income Statement extract",
                "headers": ["Expenses", "Amount"],
                "rows": [[_cell(expense_label), _cell("", editable=True, cell_id="acc-exp-mini-fa-expense")]],
            },
            {
                "heading": "Part C2: Balance Sheet extract",
                "headers": ["Current liabilities", "Amount"],
                "rows": [[_cell("Accrued expenses"), _cell("", editable=True, cell_id="acc-exp-mini-fa-liability")]],
            },
            {
                "heading": "Part D: Post-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="acc-exp-mini-patb-bank-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="acc-exp-mini-patb-stock-debit"), _cell("")],
                    [_cell(expense_label), _cell("", editable=True, cell_id="acc-exp-mini-patb-expense-debit"), _cell("")],
                    [_cell("Accrued expenses"), _cell(""), _cell("", editable=True, cell_id="acc-exp-mini-patb-liability-credit")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="acc-exp-mini-patb-capital-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="acc-exp-mini-patb-total-debit"), _cell("", editable=True, cell_id="acc-exp-mini-patb-total-credit")],
                ],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the year-end adjustment to complete the integrated reversal mini-project for outstanding {str(expense_label).lower()}: (A) General Journal adjustment and reversal, (B) adjustment analysis, (C) Income Statement and Balance Sheet extracts, and (D) Post-adjustment Trial Balance extract.",
            prompt_tables=accrued_expense_tb_prompt_tables,
            tables=accrued_expense_mini_tables,
            correct_map={
                "acc-exp-mini-j-dr-details": expense_label,
                "acc-exp-mini-j-dr-amount": scenario["amount"],
                "acc-exp-mini-j-cr-details": "Accrued expenses",
                "acc-exp-mini-j-cr-amount": scenario["amount"],
                "acc-exp-mini-j-rev-dr-details": "Accrued expenses",
                "acc-exp-mini-j-rev-dr-amount": scenario["amount"],
                "acc-exp-mini-j-rev-cr-details": expense_label,
                "acc-exp-mini-j-rev-cr-amount": scenario["amount"],
                "acc-exp-mini-a-amount": scenario["amount"],
                "acc-exp-mini-a-dr": expense_label,
                "acc-exp-mini-a-cr": "Accrued expenses",
                "acc-exp-mini-a-is": "Expense increases by R" + f"{int(scenario['amount']):,}",
                "acc-exp-mini-a-bs": "Current liability increases by R" + f"{int(scenario['amount']):,}",
                "acc-exp-mini-fa-expense": adjusted_expense_balance,
                "acc-exp-mini-fa-liability": scenario["amount"],
                "acc-exp-mini-patb-bank-debit": accrued_expense_tb_bank,
                "acc-exp-mini-patb-stock-debit": accrued_expense_tb_stock,
                "acc-exp-mini-patb-expense-debit": adjusted_expense_balance,
                "acc-exp-mini-patb-liability-credit": scenario["amount"],
                "acc-exp-mini-patb-capital-credit": accrued_expense_tb_capital,
                "acc-exp-mini-patb-total-debit": accrued_expense_tb_total,
                "acc-exp-mini-patb-total-credit": accrued_expense_tb_total,
            },
            derivation_map={
                "acc-exp-mini-fa-expense": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} + R{int(scenario['amount']):,} = R{int(adjusted_expense_balance):,}",
                "acc-exp-mini-patb-expense-debit": f"Carry the adjusted {expense_label} figure from Part C1 into Part D: R{int(adjusted_expense_balance):,}",
                "acc-exp-mini-patb-total-debit": f"Total debit = Bank + Trading stock + adjusted {expense_label} = R{int(accrued_expense_tb_bank):,} + R{int(accrued_expense_tb_stock):,} + R{int(adjusted_expense_balance):,} = R{int(accrued_expense_tb_total):,}",
            },
            cell_hints={
                "acc-exp-mini-j-cr-details": "The year-end journal creates the Accrued expenses liability.",
                "acc-exp-mini-a-dr": f"Debit {expense_label} because the expense belongs to the current period.",
                "acc-exp-mini-fa-expense": "Add the outstanding amount to the expense before carrying it to later parts.",
                "acc-exp-mini-patb-liability-credit": "The same amount appears as a current liability in the trial balance.",
                "acc-exp-mini-patb-total-debit": "Use the completed Part D balances to total the debit column.",
            },
            cell_teaching_map={
                "acc-exp-mini-fa-expense": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {str(expense_label).lower()} amount into the Income Statement extract.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance shows {expense_label} at R{int(scenario['base_balance']):,} and the year-end adjustment adds R{int(scenario['amount']):,}.",
                    rule_or_principle="Outstanding expenses belong to the current period and increase the expense account.",
                    how_to_derive=f"R{int(scenario['base_balance']):,} + R{int(scenario['amount']):,} = R{int(adjusted_expense_balance):,}.",
                    transfer_tip="For integrated accrual questions, adjust the nominal expense first, then carry the updated figure forward into the statements and trial balance.",
                ),
                "acc-exp-mini-patb-liability-credit": _teaching_hint(
                    role_in_requirement="This cell places the new liability created by the accrual into the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The journal and analysis both use Accrued expenses for the unpaid amount R{int(scenario['amount']):,}.",
                    rule_or_principle="An outstanding expense creates a current liability that must appear on the credit side of the adjusted trial balance.",
                    how_to_derive=f"Enter Accrued expenses at R{int(scenario['amount']):,} in the credit column.",
                    transfer_tip="Whenever an adjustment creates a new liability, check whether it must be shown in both the Balance Sheet effect and the trial balance.",
                ),
            },
            guidelines=[
                "Carry the same outstanding amount consistently through the journal, analysis, statements, and trial balance.",
                "Use the adjusted expense figure in both the Income Statement extract and the Post-adjustment Trial Balance.",
            ],
            marks=22,
        ), "accrued_expense_reversal_mini_project", expected_cells=22, amount=scenario["amount"], amount_cell_ids=["acc-exp-mini-j-dr-amount", "acc-exp-mini-j-cr-amount", "acc-exp-mini-j-rev-dr-amount", "acc-exp-mini-j-rev-cr-amount", "acc-exp-mini-a-amount", "acc-exp-mini-fa-liability", "acc-exp-mini-patb-liability-credit"], adjusted_amount=adjusted_expense_balance, adjusted_cell_ids=["acc-exp-mini-fa-expense", "acc-exp-mini-patb-expense-debit"], total=accrued_expense_tb_total, total_debit_cell_id="acc-exp-mini-patb-total-debit", total_credit_cell_id="acc-exp-mini-patb-total-credit"))
        accrued_expense_exam_tables = [
            {
                "heading": "Part A1: Accrued expenses account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-exp-ex-liability-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="acc-exp-ex-liability-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-exp-ex-liability-rev-details"), _cell("GJ"), _cell("", editable=True, cell_id="acc-exp-ex-liability-rev-amount"), _cell("")],
                ],
            },
            {
                "heading": f"Part A2: {expense_label} account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="acc-exp-ex-expense-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="acc-exp-ex-expense-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="acc-exp-ex-expense-rev-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="acc-exp-ex-expense-rev-amount")],
                ],
            },
            {
                "heading": "Part B1: Income Statement extract",
                "headers": ["Expenses", "Amount"],
                "rows": [[_cell(expense_label), _cell("", editable=True, cell_id="acc-exp-ex-fa-expense")]],
            },
            {
                "heading": "Part B2: Balance Sheet extract",
                "headers": ["Current liabilities", "Amount"],
                "rows": [[_cell("Accrued expenses"), _cell("", editable=True, cell_id="acc-exp-ex-fa-liability")]],
            },
            {
                "heading": "Part C: Post-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="acc-exp-ex-patb-bank-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="acc-exp-ex-patb-stock-debit"), _cell("")],
                    [_cell(expense_label), _cell("", editable=True, cell_id="acc-exp-ex-patb-expense-debit"), _cell("")],
                    [_cell("Accrued expenses"), _cell(""), _cell("", editable=True, cell_id="acc-exp-ex-patb-liability-credit")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="acc-exp-ex-patb-capital-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="acc-exp-ex-patb-total-debit"), _cell("", editable=True, cell_id="acc-exp-ex-patb-total-credit")],
                ],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the accrued expense adjustment to complete the integrated accrued expense workflow for outstanding {str(expense_label).lower()}: (A) post the year-end adjustment and the reversal to the ledger accounts, (B) carry the effect to the Income Statement and Balance Sheet extracts, and (C) complete the Post-adjustment Trial Balance extract.",
            prompt_tables=accrued_expense_tb_prompt_tables,
            tables=accrued_expense_exam_tables,
            correct_map={
                "acc-exp-ex-liability-cr-details": expense_label,
                "acc-exp-ex-liability-cr-amount": scenario["amount"],
                "acc-exp-ex-liability-rev-details": expense_label,
                "acc-exp-ex-liability-rev-amount": scenario["amount"],
                "acc-exp-ex-expense-dr-details": "Accrued expenses",
                "acc-exp-ex-expense-dr-amount": scenario["amount"],
                "acc-exp-ex-expense-rev-details": "Accrued expenses",
                "acc-exp-ex-expense-rev-amount": scenario["amount"],
                "acc-exp-ex-fa-expense": adjusted_expense_balance,
                "acc-exp-ex-fa-liability": scenario["amount"],
                "acc-exp-ex-patb-bank-debit": accrued_expense_tb_bank,
                "acc-exp-ex-patb-stock-debit": accrued_expense_tb_stock,
                "acc-exp-ex-patb-expense-debit": adjusted_expense_balance,
                "acc-exp-ex-patb-liability-credit": scenario["amount"],
                "acc-exp-ex-patb-capital-credit": accrued_expense_tb_capital,
                "acc-exp-ex-patb-total-debit": accrued_expense_tb_total,
                "acc-exp-ex-patb-total-credit": accrued_expense_tb_total,
            },
            derivation_map={
                "acc-exp-ex-liability-rev-amount": f"The reversal uses the same amount as the year-end accrual: R{int(scenario['amount']):,}",
                "acc-exp-ex-fa-expense": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} + R{int(scenario['amount']):,} = R{int(adjusted_expense_balance):,}",
                "acc-exp-ex-patb-expense-debit": f"Carry the adjusted {expense_label} amount into the debit column of the Post-adjustment Trial Balance: R{int(adjusted_expense_balance):,}",
                "acc-exp-ex-patb-total-debit": f"Total debit = Bank + Trading stock + adjusted {expense_label} = R{int(accrued_expense_tb_bank):,} + R{int(accrued_expense_tb_stock):,} + R{int(adjusted_expense_balance):,} = R{int(accrued_expense_tb_total):,}",
            },
            cell_hints={
                "acc-exp-ex-liability-cr-details": "In the Accrued expenses account, the details column shows the opposite account from the journal entry.",
                "acc-exp-ex-expense-dr-details": "In the expense account, use the opposite account from the accrual entry in the details column.",
                "acc-exp-ex-fa-expense": "Add the unpaid amount to the existing expense balance before carrying it into the statement extract.",
                "acc-exp-ex-patb-liability-credit": "The same accrued amount appears as a current liability in the adjusted trial balance.",
                "acc-exp-ex-patb-total-debit": "Use all completed debit balances in Part C to total the column.",
            },
            cell_teaching_map={
                "acc-exp-ex-fa-expense": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {str(expense_label).lower()} figure into the Income Statement extract.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance gives {expense_label} at R{int(scenario['base_balance']):,} and the year-end adjustment adds R{int(scenario['amount']):,}.",
                    rule_or_principle="Outstanding expenses belong to the current accounting period, so they increase the related expense account.",
                    how_to_derive=f"Add R{int(scenario['amount']):,} to R{int(scenario['base_balance']):,} to get R{int(adjusted_expense_balance):,}.",
                    transfer_tip="In integrated adjustment workflows, update the nominal expense first and then carry the adjusted figure into later statement sections.",
                ),
                "acc-exp-ex-patb-liability-credit": _teaching_hint(
                    role_in_requirement="This cell shows the liability created by the accrual in the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The year-end adjustment creates Accrued expenses for R{int(scenario['amount']):,}.",
                    rule_or_principle="An outstanding expense creates a current liability and appears in the credit column of the adjusted trial balance.",
                    how_to_derive=f"Enter Accrued expenses at R{int(scenario['amount']):,} on the credit side.",
                    transfer_tip="When an adjustment creates a new liability, check whether that account must be added to the adjusted trial balance.",
                ),
            },
            guidelines=[
                "Post the accrual and the reversal using the same amount in both ledger accounts.",
                "Carry the adjusted expense figure consistently into the Income Statement and the Post-adjustment Trial Balance.",
                "Show the accrued amount as a current liability in both the Balance Sheet extract and the Post-adjustment Trial Balance.",
            ],
            marks=17,
        ), "accrued_expense_reversal_mini_project", expected_cells=17, amount=scenario["amount"], amount_cell_ids=["acc-exp-ex-liability-cr-amount", "acc-exp-ex-liability-rev-amount", "acc-exp-ex-expense-dr-amount", "acc-exp-ex-expense-rev-amount", "acc-exp-ex-fa-liability", "acc-exp-ex-patb-liability-credit"], adjusted_amount=adjusted_expense_balance, adjusted_cell_ids=["acc-exp-ex-fa-expense", "acc-exp-ex-patb-expense-debit"], total=accrued_expense_tb_total, total_debit_cell_id="acc-exp-ex-patb-total-debit", total_credit_cell_id="acc-exp-ex-patb-total-credit"))
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="ledger",
            prompt=f"{scenario['prompt_intro']} Post the year-end adjustment dated {scenario['year_end_date']} and the reversal on {scenario['reversal_date']}.",
            tables=accrued_expense_ledger_tables,
            correct_map={
                "acc-exp-cr-details": expense_label,
                "acc-exp-cr-amount": scenario["amount"],
                "acc-exp-rev-details": expense_label,
                "acc-exp-rev-amount": scenario["amount"],
                "tel-exp-dr-details": "Accrued expenses",
                "tel-exp-dr-amount": scenario["amount"],
                "tel-exp-rev-details": "Accrued expenses",
                "tel-exp-rev-amount": scenario["amount"],
            },
            derivation_map={
                "acc-exp-cr-amount": f"Use the outstanding expense amount at year-end: R{int(scenario['amount']):,}",
                "acc-exp-rev-amount": f"Reverse the exact same amount at the start of the next period: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "acc-exp-cr-details": f"The liability account uses the {str(expense_label).lower()} account as the details entry at year-end.",
                "acc-exp-rev-details": "The reversing entry uses the same opposite account in the details column.",
                "tel-exp-dr-details": "The expense account uses Accrued expenses as the details entry.",
                "tel-exp-rev-details": "On reversal day, the expense account again shows the opposite account as details.",
            },
            cell_teaching_map={
                "acc-exp-cr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the opposite account for the year-end credit in Accrued expenses.",
                    evidence_from_question=f"The year-end adjustment is Dr {expense_label} / Cr Accrued expenses.",
                    rule_or_principle="In a ledger, the details column records the opposite account from the journal entry.",
                    how_to_derive=f"Because Accrued expenses is credited, the details entry is {expense_label}.",
                    transfer_tip="For liabilities created by year-end adjustments, write the related expense or income account in the details column.",
                ),
                "tel-exp-dr-amount": _teaching_hint(
                    role_in_requirement="This cell records the expense increase for the current period.",
                    evidence_from_question=f"The business still owes {str(expense_label).lower()} of the stated amount at year-end.",
                    rule_or_principle="Outstanding expenses increase the expense account in the current period.",
                    how_to_derive=f"Use the full accrued amount R{int(scenario['amount']):,} for the year-end debit.",
                    transfer_tip="If an expense is owing, the expense account gets the debit and the liability gets the credit.",
                ),
                "tel-exp-rev-details": _teaching_hint(
                    role_in_requirement=f"This cell identifies the opposite account for the reversal in the {expense_label} account.",
                    evidence_from_question=f"The question requires a reversal on {scenario['reversal_date']}.",
                    rule_or_principle="The reversal entry swaps the original debit and credit accounts but keeps the same pair of accounts.",
                    how_to_derive="The opposite account remains Accrued expenses, so that is the details entry.",
                    transfer_tip="When reversing, keep the same account pair and amount; only the sides change.",
                ),
            },
            guidelines=[
                f"Year-end: Dr {expense_label} / Cr Accrued expenses.",
                f"Reversal next year: Dr Accrued expenses / Cr {expense_label}.",
            ],
            marks=8,
        ), "accrued_expense_reversal_ledger_fill", expected_cells=8, amount=scenario["amount"], amount_cell_ids=["acc-exp-cr-amount", "acc-exp-rev-amount", "tel-exp-dr-amount", "tel-exp-rev-amount"]))

    prepaid_ledger_scenarios = [
        {
            "expense_label": "Insurance",
            "amount": prepaid_amount,
            "base_balance": 12000,
            "year_end_date": "28 Feb 2026",
            "reversal_date": "1 Mar 2026",
            "prompt_intro": f"{biz} paid insurance of R{prepaid_total:,} for 12 months starting 1 October. The year ends on 28 February and the prepaid portion is R{prepaid_amount:,}.",
        },
        {
            "expense_label": "Advertising",
            "amount": 13500,
            "base_balance": 18000,
            "year_end_date": "30 Jun 2026",
            "reversal_date": "1 Jul 2026",
            "prompt_intro": f"{biz} paid advertising for 12 months starting 1 April 2026. At 30 June 2026 the prepaid portion is R13 500.",
        },
        {
            "expense_label": "Rates",
            "amount": 6000,
            "base_balance": 15000,
            "year_end_date": "31 Dec 2026",
            "reversal_date": "1 Jan 2027",
            "prompt_intro": f"{biz} paid rates in advance and the unused portion at 31 December 2026 amounts to R6 000.",
        },
    ]
    for scenario in prepaid_ledger_scenarios:
        expense_label = str(scenario["expense_label"])
        adjusted_prepaid_expense_balance = _round_money(float(scenario["base_balance"]) - float(scenario["amount"]))
        prepaid_ledger_tables = [
            {
                "heading": "Prepaid expenses account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="prepaid-exp-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="prepaid-exp-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="prepaid-exp-rev-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="prepaid-exp-rev-amount")],
                ],
            },
            {
                "heading": f"{expense_label} account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="insurance-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="insurance-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="insurance-rev-details"), _cell("GJ"), _cell("", editable=True, cell_id="insurance-rev-amount"), _cell("")],
                ],
            },
        ]
        prepaid_journal_table = {
            "heading": "General Journal",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="prepaid-j-dr-details"), _cell("", editable=True, cell_id="prepaid-j-dr-amount"), _cell("")],
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="prepaid-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="prepaid-j-cr-amount")],
                [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="prepaid-j-rev-dr-details"), _cell("", editable=True, cell_id="prepaid-j-rev-dr-amount"), _cell("")],
                [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="prepaid-j-rev-cr-details"), _cell(""), _cell("", editable=True, cell_id="prepaid-j-rev-cr-amount")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=f"{scenario['prompt_intro']} Prepare the General Journal entry for the year-end adjustment dated {scenario['year_end_date']} and the reversal on {scenario['reversal_date']}.",
            table=prepaid_journal_table,
            correct_map={
                "prepaid-j-dr-details": "Prepaid expenses",
                "prepaid-j-dr-amount": scenario["amount"],
                "prepaid-j-cr-details": expense_label,
                "prepaid-j-cr-amount": scenario["amount"],
                "prepaid-j-rev-dr-details": expense_label,
                "prepaid-j-rev-dr-amount": scenario["amount"],
                "prepaid-j-rev-cr-details": "Prepaid expenses",
                "prepaid-j-rev-cr-amount": scenario["amount"],
            },
            derivation_map={
                "prepaid-j-dr-amount": f"Use the prepaid amount given: R{int(scenario['amount']):,}",
                "prepaid-j-rev-dr-amount": f"The reversal uses the same prepaid amount: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "prepaid-j-dr-details": "At year-end, debit the Prepaid expenses asset account.",
                "prepaid-j-cr-details": f"Credit the expense account: {expense_label}.",
                "prepaid-j-rev-dr-details": "The reversal restores the expense account on the debit side.",
                "prepaid-j-rev-cr-details": "The reversal credits Prepaid expenses to cancel the asset entry.",
            },
            guidelines=[
                f"Year-end: Dr Prepaid expenses / Cr {expense_label}.",
                f"Reversal next period: Dr {expense_label} / Cr Prepaid expenses.",
            ],
            marks=8,
        ), "prepaid_expense_reversal_journal_fill", expected_cells=8, amount=scenario["amount"], amount_cell_ids=["prepaid-j-dr-amount", "prepaid-j-cr-amount", "prepaid-j-rev-dr-amount", "prepaid-j-rev-cr-amount"]))
        prepaid_analysis_table = {
            "heading": f"Adjustment analysis: {str(expense_label).lower()}",
            "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
            "rows": [
                [_cell(f"{expense_label} paid in advance"), _cell("", editable=True, cell_id="prepaid-a-amount"), _cell("", editable=True, cell_id="prepaid-a-dr"), _cell("", editable=True, cell_id="prepaid-a-cr"), _cell("", editable=True, cell_id="prepaid-a-is"), _cell("", editable=True, cell_id="prepaid-a-bs")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="adjustment_analysis_table",
            prompt=f"{scenario['prompt_intro']} Complete the adjustment analysis table for the year-end adjustment.",
            table=prepaid_analysis_table,
            correct_map={
                "prepaid-a-amount": scenario["amount"],
                "prepaid-a-dr": "Prepaid expenses",
                "prepaid-a-cr": expense_label,
                "prepaid-a-is": "Expense decreases by R" + f"{int(scenario['amount']):,}",
                "prepaid-a-bs": "Current asset increases by R" + f"{int(scenario['amount']):,}",
            },
            derivation_map={
                "prepaid-a-amount": f"Use the unused portion given in the question: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "prepaid-a-dr": "A prepaid expense creates a current asset.",
                "prepaid-a-cr": f"Credit {expense_label} to remove the future-period portion from this year's expense.",
                "prepaid-a-bs": "The Balance Sheet effect is a current asset increase.",
            },
            guidelines=[
                "A prepaid expense reduces the current-period expense and creates a current asset.",
                "Use the same amount in the double entry and in the statement effects.",
            ],
            marks=6,
        ), "prepaid_expense_analysis_fill", expected_cells=5, amount=scenario["amount"], amount_cell_id="prepaid-a-amount"))
        prepaid_carry_tables = [
            {
                "heading": "Income Statement extract",
                "headers": ["Expenses", "Amount"],
                "rows": [[_cell(expense_label), _cell("", editable=True, cell_id="prepaid-fa-expense")]],
            },
            {
                "heading": "Balance Sheet extract",
                "headers": ["Current assets", "Amount"],
                "rows": [[_cell("Prepaid expenses"), _cell("", editable=True, cell_id="prepaid-fa-asset")]],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the source extract and year-end adjustment to carry the effect of the prepaid {str(expense_label).lower()} into the Income Statement and Balance Sheet extracts.",
            prompt_table={
                "heading": "Source extract",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell(f"{expense_label} before adjustment"), _cell(scenario["base_balance"])],
                    [_cell("Prepaid portion"), _cell(scenario["amount"])],
                ],
            },
            tables=prepaid_carry_tables,
            correct_map={
                "prepaid-fa-expense": adjusted_prepaid_expense_balance,
                "prepaid-fa-asset": scenario["amount"],
            },
            derivation_map={
                "prepaid-fa-expense": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} - R{int(scenario['amount']):,} = R{int(adjusted_prepaid_expense_balance):,}",
                "prepaid-fa-asset": f"Carry the prepaid amount to Current assets: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "prepaid-fa-expense": f"Subtract the prepaid amount from the {str(expense_label).lower()} line in the Income Statement.",
                "prepaid-fa-asset": "Carry the same amount to Prepaid expenses under Current assets.",
            },
            guidelines=[
                f"Subtract the prepaid amount from the {expense_label} figure in the Income Statement.",
                "Carry the same amount to Prepaid expenses under Current assets.",
            ],
            marks=4,
        ), "prepaid_expense_carrythrough_fill", expected_cells=2, adjusted_amount=adjusted_prepaid_expense_balance, carry_amount=scenario["amount"], adjusted_cell_id="prepaid-fa-expense", carry_cell_id="prepaid-fa-asset"))
        prepaid_tb_bank = _round_money(float(scenario["base_balance"]) + 34000.0)
        prepaid_tb_stock = _round_money(float(scenario["amount"]) + 15000.0)
        prepaid_tb_capital = _round_money(float(prepaid_tb_bank) + float(prepaid_tb_stock) + float(scenario["base_balance"]))
        prepaid_tb_total = _round_money(float(prepaid_tb_bank) + float(prepaid_tb_stock) + float(adjusted_prepaid_expense_balance) + float(scenario["amount"]))
        prepaid_tb_prompt_tables = [
            {
                "heading": "Pre-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell(prepaid_tb_bank), _cell("")],
                    [_cell("Trading stock"), _cell(prepaid_tb_stock), _cell("")],
                    [_cell(expense_label), _cell(scenario["base_balance"]), _cell("")],
                    [_cell("Capital"), _cell(""), _cell(prepaid_tb_capital)],
                ],
            },
            {
                "heading": "Year-end adjustment",
                "headers": ["Adjustment", "Amount"],
                "rows": [[_cell(f"Prepaid portion of {str(expense_label).lower()}"), _cell(scenario["amount"])]]
            },
        ]
        prepaid_tb_table = {
            "heading": "Post-adjustment Trial Balance extract",
            "headers": ["Account", "Debit", "Credit"],
            "rows": [
                [_cell("Bank"), _cell("", editable=True, cell_id="prepaid-patb-bank-debit"), _cell("")],
                [_cell("Trading stock"), _cell("", editable=True, cell_id="prepaid-patb-stock-debit"), _cell("")],
                [_cell(expense_label), _cell("", editable=True, cell_id="prepaid-patb-expense-debit"), _cell("")],
                [_cell("Prepaid expenses"), _cell("", editable=True, cell_id="prepaid-patb-asset-debit"), _cell("")],
                [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="prepaid-patb-capital-credit")],
                [_cell("Total"), _cell("", editable=True, cell_id="prepaid-patb-total-debit"), _cell("", editable=True, cell_id="prepaid-patb-total-credit")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="trial_balance_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the year-end adjustment to complete the Post-adjustment Trial Balance extract for the prepaid {str(expense_label).lower()}.",
            prompt_tables=prepaid_tb_prompt_tables,
            table=prepaid_tb_table,
            correct_map={
                "prepaid-patb-bank-debit": prepaid_tb_bank,
                "prepaid-patb-stock-debit": prepaid_tb_stock,
                "prepaid-patb-expense-debit": adjusted_prepaid_expense_balance,
                "prepaid-patb-asset-debit": scenario["amount"],
                "prepaid-patb-capital-credit": prepaid_tb_capital,
                "prepaid-patb-total-debit": prepaid_tb_total,
                "prepaid-patb-total-credit": prepaid_tb_total,
            },
            derivation_map={
                "prepaid-patb-expense-debit": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} - R{int(scenario['amount']):,} = R{int(adjusted_prepaid_expense_balance):,}",
                "prepaid-patb-total-debit": f"Total debit = Bank + Trading stock + adjusted {expense_label} + Prepaid expenses = R{int(prepaid_tb_bank):,} + R{int(prepaid_tb_stock):,} + R{int(adjusted_prepaid_expense_balance):,} + R{int(scenario['amount']):,} = R{int(prepaid_tb_total):,}",
            },
            cell_hints={
                "prepaid-patb-expense-debit": f"Remove the prepaid portion from the {str(expense_label).lower()} expense balance.",
                "prepaid-patb-asset-debit": "Show the prepaid portion as a current asset.",
                "prepaid-patb-total-debit": "Total all debit balances after splitting the expense and prepaid asset.",
            },
            guidelines=[
                "Copy unchanged balances from the Pre-adjustment Trial Balance.",
                f"Reduce {expense_label} by the prepaid amount and show the same amount as Prepaid expenses on the debit side.",
            ],
            marks=7,
        ), "prepaid_expense_post_adjustment_tb_fill", expected_cells=7, total=prepaid_tb_total, adjusted_amount=adjusted_prepaid_expense_balance, carry_amount=scenario["amount"], adjusted_cell_id="prepaid-patb-expense-debit", carry_cell_id="prepaid-patb-asset-debit", total_debit_cell_id="prepaid-patb-total-debit", total_credit_cell_id="prepaid-patb-total-credit"))
        prepaid_mini_tables = [
            {
                "heading": "Part A: General Journal",
                "headers": ["Date", "Details", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="prepaid-mini-j-dr-details"), _cell("", editable=True, cell_id="prepaid-mini-j-dr-amount"), _cell("")],
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="prepaid-mini-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="prepaid-mini-j-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="prepaid-mini-j-rev-dr-details"), _cell("", editable=True, cell_id="prepaid-mini-j-rev-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="prepaid-mini-j-rev-cr-details"), _cell(""), _cell("", editable=True, cell_id="prepaid-mini-j-rev-cr-amount")],
                ],
            },
            {
                "heading": "Part B: Adjustment analysis",
                "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
                "rows": [
                    [_cell(f"{expense_label} paid in advance"), _cell("", editable=True, cell_id="prepaid-mini-a-amount"), _cell("", editable=True, cell_id="prepaid-mini-a-dr"), _cell("", editable=True, cell_id="prepaid-mini-a-cr"), _cell("", editable=True, cell_id="prepaid-mini-a-is"), _cell("", editable=True, cell_id="prepaid-mini-a-bs")],
                ],
            },
            {
                "heading": "Part C1: Income Statement extract",
                "headers": ["Expenses", "Amount"],
                "rows": [[_cell(expense_label), _cell("", editable=True, cell_id="prepaid-mini-fa-expense")]],
            },
            {
                "heading": "Part C2: Balance Sheet extract",
                "headers": ["Current assets", "Amount"],
                "rows": [[_cell("Prepaid expenses"), _cell("", editable=True, cell_id="prepaid-mini-fa-asset")]],
            },
            {
                "heading": "Part D: Post-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="prepaid-mini-patb-bank-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="prepaid-mini-patb-stock-debit"), _cell("")],
                    [_cell(expense_label), _cell("", editable=True, cell_id="prepaid-mini-patb-expense-debit"), _cell("")],
                    [_cell("Prepaid expenses"), _cell("", editable=True, cell_id="prepaid-mini-patb-asset-debit"), _cell("")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="prepaid-mini-patb-capital-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="prepaid-mini-patb-total-debit"), _cell("", editable=True, cell_id="prepaid-mini-patb-total-credit")],
                ],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the year-end adjustment to complete the integrated reversal mini-project for prepaid {str(expense_label).lower()}: (A) General Journal adjustment and reversal, (B) adjustment analysis, (C) Income Statement and Balance Sheet extracts, and (D) Post-adjustment Trial Balance extract.",
            prompt_tables=prepaid_tb_prompt_tables,
            tables=prepaid_mini_tables,
            correct_map={
                "prepaid-mini-j-dr-details": "Prepaid expenses",
                "prepaid-mini-j-dr-amount": scenario["amount"],
                "prepaid-mini-j-cr-details": expense_label,
                "prepaid-mini-j-cr-amount": scenario["amount"],
                "prepaid-mini-j-rev-dr-details": expense_label,
                "prepaid-mini-j-rev-dr-amount": scenario["amount"],
                "prepaid-mini-j-rev-cr-details": "Prepaid expenses",
                "prepaid-mini-j-rev-cr-amount": scenario["amount"],
                "prepaid-mini-a-amount": scenario["amount"],
                "prepaid-mini-a-dr": "Prepaid expenses",
                "prepaid-mini-a-cr": expense_label,
                "prepaid-mini-a-is": "Expense decreases by R" + f"{int(scenario['amount']):,}",
                "prepaid-mini-a-bs": "Current asset increases by R" + f"{int(scenario['amount']):,}",
                "prepaid-mini-fa-expense": adjusted_prepaid_expense_balance,
                "prepaid-mini-fa-asset": scenario["amount"],
                "prepaid-mini-patb-bank-debit": prepaid_tb_bank,
                "prepaid-mini-patb-stock-debit": prepaid_tb_stock,
                "prepaid-mini-patb-expense-debit": adjusted_prepaid_expense_balance,
                "prepaid-mini-patb-asset-debit": scenario["amount"],
                "prepaid-mini-patb-capital-credit": prepaid_tb_capital,
                "prepaid-mini-patb-total-debit": prepaid_tb_total,
                "prepaid-mini-patb-total-credit": prepaid_tb_total,
            },
            derivation_map={
                "prepaid-mini-fa-expense": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} - R{int(scenario['amount']):,} = R{int(adjusted_prepaid_expense_balance):,}",
                "prepaid-mini-patb-expense-debit": f"Carry the adjusted {expense_label} figure from Part C1 into Part D: R{int(adjusted_prepaid_expense_balance):,}",
                "prepaid-mini-patb-total-debit": f"Total debit = Bank + Trading stock + adjusted {expense_label} + Prepaid expenses = R{int(prepaid_tb_bank):,} + R{int(prepaid_tb_stock):,} + R{int(adjusted_prepaid_expense_balance):,} + R{int(scenario['amount']):,} = R{int(prepaid_tb_total):,}",
            },
            cell_hints={
                "prepaid-mini-j-dr-details": "The year-end journal debits Prepaid expenses because the amount belongs to the next period.",
                "prepaid-mini-a-cr": f"Credit {expense_label} to remove the future-period portion from this year’s expense.",
                "prepaid-mini-fa-expense": "Subtract the prepaid portion before carrying the expense into later parts.",
                "prepaid-mini-patb-asset-debit": "The prepaid amount also appears as a current asset in the trial balance.",
                "prepaid-mini-patb-total-debit": "Use the completed Part D balances to total the debit column.",
            },
            cell_teaching_map={
                "prepaid-mini-fa-expense": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {str(expense_label).lower()} amount into the Income Statement extract.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance shows {expense_label} at R{int(scenario['base_balance']):,} and the year-end adjustment removes the prepaid portion of R{int(scenario['amount']):,}.",
                    rule_or_principle="A prepaid expense belongs to the next period, so it must be removed from the current expense.",
                    how_to_derive=f"R{int(scenario['base_balance']):,} - R{int(scenario['amount']):,} = R{int(adjusted_prepaid_expense_balance):,}.",
                    transfer_tip="In integrated prepayment questions, split the original expense into the current-period expense and the prepaid asset before completing later sections.",
                ),
                "prepaid-mini-patb-asset-debit": _teaching_hint(
                    role_in_requirement="This cell places the new prepaid asset into the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The journal and analysis both identify Prepaid expenses for the amount R{int(scenario['amount']):,}.",
                    rule_or_principle="A prepaid expense is a current asset and appears in the debit column of the adjusted trial balance.",
                    how_to_derive=f"Enter Prepaid expenses at R{int(scenario['amount']):,} in the debit column.",
                    transfer_tip="When an adjustment creates a prepaid asset, it should usually appear in both the Balance Sheet effect and the adjusted trial balance.",
                ),
            },
            guidelines=[
                "Carry the same prepaid amount consistently through the journal, analysis, statements, and trial balance.",
                "Use the adjusted expense figure in both the Income Statement extract and the Post-adjustment Trial Balance.",
            ],
            marks=22,
        ), "prepaid_expense_reversal_mini_project", expected_cells=22, amount=scenario["amount"], amount_cell_ids=["prepaid-mini-j-dr-amount", "prepaid-mini-j-cr-amount", "prepaid-mini-j-rev-dr-amount", "prepaid-mini-j-rev-cr-amount", "prepaid-mini-a-amount", "prepaid-mini-fa-asset", "prepaid-mini-patb-asset-debit"], adjusted_amount=adjusted_prepaid_expense_balance, adjusted_cell_ids=["prepaid-mini-fa-expense", "prepaid-mini-patb-expense-debit"], total=prepaid_tb_total, total_debit_cell_id="prepaid-mini-patb-total-debit", total_credit_cell_id="prepaid-mini-patb-total-credit"))
        prepaid_exam_tables = [
            {
                "heading": "Part A1: Prepaid expenses account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="prepaid-ex-asset-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="prepaid-ex-asset-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="prepaid-ex-asset-rev-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="prepaid-ex-asset-rev-amount")],
                ],
            },
            {
                "heading": f"Part A2: {expense_label} account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="prepaid-ex-expense-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="prepaid-ex-expense-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="prepaid-ex-expense-rev-details"), _cell("GJ"), _cell("", editable=True, cell_id="prepaid-ex-expense-rev-amount"), _cell("")],
                ],
            },
            {
                "heading": "Part B1: Income Statement extract",
                "headers": ["Expenses", "Amount"],
                "rows": [[_cell(expense_label), _cell("", editable=True, cell_id="prepaid-ex-fa-expense")]],
            },
            {
                "heading": "Part B2: Balance Sheet extract",
                "headers": ["Current assets", "Amount"],
                "rows": [[_cell("Prepaid expenses"), _cell("", editable=True, cell_id="prepaid-ex-fa-asset")]],
            },
            {
                "heading": "Part C: Post-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="prepaid-ex-patb-bank-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="prepaid-ex-patb-stock-debit"), _cell("")],
                    [_cell(expense_label), _cell("", editable=True, cell_id="prepaid-ex-patb-expense-debit"), _cell("")],
                    [_cell("Prepaid expenses"), _cell("", editable=True, cell_id="prepaid-ex-patb-asset-debit"), _cell("")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="prepaid-ex-patb-capital-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="prepaid-ex-patb-total-debit"), _cell("", editable=True, cell_id="prepaid-ex-patb-total-credit")],
                ],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the prepaid expense adjustment to complete the integrated prepaid expense workflow for prepaid {str(expense_label).lower()}: (A) post the year-end adjustment and the reversal to the ledger accounts, (B) carry the effect to the Income Statement and Balance Sheet extracts, and (C) complete the Post-adjustment Trial Balance extract.",
            prompt_tables=prepaid_tb_prompt_tables,
            tables=prepaid_exam_tables,
            correct_map={
                "prepaid-ex-asset-dr-details": expense_label,
                "prepaid-ex-asset-dr-amount": scenario["amount"],
                "prepaid-ex-asset-rev-details": expense_label,
                "prepaid-ex-asset-rev-amount": scenario["amount"],
                "prepaid-ex-expense-cr-details": "Prepaid expenses",
                "prepaid-ex-expense-cr-amount": scenario["amount"],
                "prepaid-ex-expense-rev-details": "Prepaid expenses",
                "prepaid-ex-expense-rev-amount": scenario["amount"],
                "prepaid-ex-fa-expense": adjusted_prepaid_expense_balance,
                "prepaid-ex-fa-asset": scenario["amount"],
                "prepaid-ex-patb-bank-debit": prepaid_tb_bank,
                "prepaid-ex-patb-stock-debit": prepaid_tb_stock,
                "prepaid-ex-patb-expense-debit": adjusted_prepaid_expense_balance,
                "prepaid-ex-patb-asset-debit": scenario["amount"],
                "prepaid-ex-patb-capital-credit": prepaid_tb_capital,
                "prepaid-ex-patb-total-debit": prepaid_tb_total,
                "prepaid-ex-patb-total-credit": prepaid_tb_total,
            },
            derivation_map={
                "prepaid-ex-asset-rev-amount": f"The reversal uses the same amount as the year-end prepayment: R{int(scenario['amount']):,}",
                "prepaid-ex-fa-expense": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} - R{int(scenario['amount']):,} = R{int(adjusted_prepaid_expense_balance):,}",
                "prepaid-ex-patb-expense-debit": f"Carry the adjusted {expense_label} amount into the debit column of the Post-adjustment Trial Balance: R{int(adjusted_prepaid_expense_balance):,}",
                "prepaid-ex-patb-total-debit": f"Total debit = Bank + Trading stock + adjusted {expense_label} + Prepaid expenses = R{int(prepaid_tb_bank):,} + R{int(prepaid_tb_stock):,} + R{int(adjusted_prepaid_expense_balance):,} + R{int(scenario['amount']):,} = R{int(prepaid_tb_total):,}",
            },
            cell_hints={
                "prepaid-ex-asset-dr-details": "In the Prepaid expenses account, the details column shows the opposite account from the journal entry.",
                "prepaid-ex-expense-cr-details": "In the expense account, use the opposite account from the prepayment entry in the details column.",
                "prepaid-ex-fa-expense": "Subtract the prepaid portion from the existing expense balance before carrying it into the statement extract.",
                "prepaid-ex-patb-asset-debit": "The same prepaid amount appears as a current asset in the adjusted trial balance.",
                "prepaid-ex-patb-total-debit": "Use all completed debit balances in Part C to total the column.",
            },
            cell_teaching_map={
                "prepaid-ex-fa-expense": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {str(expense_label).lower()} figure into the Income Statement extract.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance gives {expense_label} at R{int(scenario['base_balance']):,} and the year-end adjustment removes the prepaid portion of R{int(scenario['amount']):,}.",
                    rule_or_principle="A prepaid expense belongs to the next accounting period, so it must be removed from the current expense account.",
                    how_to_derive=f"Subtract R{int(scenario['amount']):,} from R{int(scenario['base_balance']):,} to get R{int(adjusted_prepaid_expense_balance):,}.",
                    transfer_tip="In integrated prepayment workflows, adjust the expense first and then carry the updated figure into later statement sections.",
                ),
                "prepaid-ex-patb-asset-debit": _teaching_hint(
                    role_in_requirement="This cell shows the asset created by the prepayment in the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The year-end adjustment creates Prepaid expenses for R{int(scenario['amount']):,}.",
                    rule_or_principle="A prepaid expense is a current asset and appears in the debit column of the adjusted trial balance.",
                    how_to_derive=f"Enter Prepaid expenses at R{int(scenario['amount']):,} on the debit side.",
                    transfer_tip="When an adjustment creates a prepaid asset, check whether that account must be added to the adjusted trial balance.",
                ),
            },
            guidelines=[
                "Post the prepayment and the reversal using the same amount in both ledger accounts.",
                "Carry the adjusted expense figure consistently into the Income Statement and the Post-adjustment Trial Balance.",
                "Show the prepaid amount as a current asset in both the Balance Sheet extract and the Post-adjustment Trial Balance.",
            ],
            marks=17,
        ), "prepaid_expense_reversal_mini_project", expected_cells=17, amount=scenario["amount"], amount_cell_ids=["prepaid-ex-asset-dr-amount", "prepaid-ex-asset-rev-amount", "prepaid-ex-expense-cr-amount", "prepaid-ex-expense-rev-amount", "prepaid-ex-fa-asset", "prepaid-ex-patb-asset-debit"], adjusted_amount=adjusted_prepaid_expense_balance, adjusted_cell_ids=["prepaid-ex-fa-expense", "prepaid-ex-patb-expense-debit"], total=prepaid_tb_total, total_debit_cell_id="prepaid-ex-patb-total-debit", total_credit_cell_id="prepaid-ex-patb-total-credit"))
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="ledger",
            prompt=f"{scenario['prompt_intro']} Post the year-end adjustment dated {scenario['year_end_date']} and the reversal on {scenario['reversal_date']}.",
            tables=prepaid_ledger_tables,
            correct_map={
                "prepaid-exp-dr-details": expense_label,
                "prepaid-exp-dr-amount": scenario["amount"],
                "prepaid-exp-rev-details": expense_label,
                "prepaid-exp-rev-amount": scenario["amount"],
                "insurance-cr-details": "Prepaid expenses",
                "insurance-cr-amount": scenario["amount"],
                "insurance-rev-details": "Prepaid expenses",
                "insurance-rev-amount": scenario["amount"],
            },
            derivation_map={
                "prepaid-exp-dr-amount": f"Use the prepaid portion already given: R{int(scenario['amount']):,}",
                "prepaid-exp-rev-amount": f"Reverse the same prepaid amount at the start of the next period: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "prepaid-exp-dr-details": f"At year-end, the prepaid asset is paired with the {str(expense_label).lower()} expense account.",
                "insurance-cr-details": "The expense account uses Prepaid expenses as the opposite account.",
                "insurance-rev-details": "The reversal uses the same opposite account in the details column.",
            },
            cell_teaching_map={
                "prepaid-exp-dr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the opposite account for the year-end debit in Prepaid expenses.",
                    evidence_from_question=f"The year-end adjustment for a prepaid expense is Dr Prepaid expenses / Cr {expense_label}.",
                    rule_or_principle="The details column always shows the opposite account used in the double entry.",
                    how_to_derive=f"Because Prepaid expenses is debited, the details entry is {expense_label}.",
                    transfer_tip="When an amount is paid in advance, move the future-period portion into a prepaid asset.",
                ),
                "insurance-cr-amount": _teaching_hint(
                    role_in_requirement="This cell reduces the expense account for the portion that belongs to the next period.",
                    evidence_from_question=f"The question states the prepaid portion is R{int(scenario['amount']):,}.",
                    rule_or_principle="A prepaid expense is removed from the current-period expense and carried forward as an asset.",
                    how_to_derive=f"Credit {expense_label} with the prepaid amount R{int(scenario['amount']):,}.",
                    transfer_tip="If part of an expense belongs to next year, credit the expense account and debit a prepaid asset.",
                ),
                "insurance-rev-details": _teaching_hint(
                    role_in_requirement=f"This cell identifies the opposite account for the reversal in the {expense_label} account.",
                    evidence_from_question=f"The question requires the reversal on {scenario['reversal_date']}.",
                    rule_or_principle="A reversal keeps the same account pair but posts them on the opposite sides.",
                    how_to_derive="The opposite account remains Prepaid expenses, so that is the details entry.",
                    transfer_tip="Reversals help the next period record the actual expense normally without double counting.",
                ),
            },
            guidelines=[
                f"Year-end: Dr Prepaid expenses / Cr {expense_label}.",
                f"Reversal next year: Dr {expense_label} / Cr Prepaid expenses.",
            ],
            marks=8,
        ), "prepaid_expense_reversal_ledger_fill", expected_cells=8, amount=scenario["amount"], amount_cell_ids=["prepaid-exp-dr-amount", "prepaid-exp-rev-amount", "insurance-cr-amount", "insurance-rev-amount"]))

    advance_income_ledger_scenarios = [
        {
            "income_label": "Rent income",
            "amount": income_advance_amount,
            "base_balance": 18000,
            "year_end_date": "28 Feb 2026",
            "reversal_date": "1 Mar 2026",
            "prompt_intro": f"A tenant paid {biz} rent in advance of R{income_advance_amount:,} before year-end.",
        },
        {
            "income_label": "Commission income",
            "amount": _round_money(r.choice([2500, 3500, 4800, 6000])),
            "base_balance": 24000,
            "year_end_date": "30 Jun 2026",
            "reversal_date": "1 Jul 2026",
            "prompt_intro": "",
        },
        {
            "income_label": "Service fees",
            "amount": _round_money(r.choice([1800, 2400, 3000, 4200])),
            "base_balance": 15000,
            "year_end_date": "31 Dec 2026",
            "reversal_date": "1 Jan 2027",
            "prompt_intro": "",
        },
    ]
    advance_income_ledger_scenarios[1]["prompt_intro"] = f"A client paid commission income in advance to {biz}. At 30 June 2026 the amount not yet earned is R{int(advance_income_ledger_scenarios[1]['amount']):,}."
    advance_income_ledger_scenarios[2]["prompt_intro"] = f"{biz} received service fees in advance and the unearned portion at year-end is R{int(advance_income_ledger_scenarios[2]['amount']):,}."
    for scenario in advance_income_ledger_scenarios:
        income_label = str(scenario["income_label"])
        adjusted_income_advance_balance = _round_money(float(scenario["base_balance"]) - float(scenario["amount"]))
        advance_income_ledger_tables = [
            {
                "heading": "Income received in advance account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="adv-inc-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="adv-inc-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="adv-inc-rev-details"), _cell("GJ"), _cell("", editable=True, cell_id="adv-inc-rev-amount"), _cell("")],
                ],
            },
            {
                "heading": f"{income_label} account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="rent-adv-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="rent-adv-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="rent-adv-rev-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="rent-adv-rev-amount")],
                ],
            },
        ]
        advance_income_journal_table = {
            "heading": "General Journal",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="adv-inc-j-dr-details"), _cell("", editable=True, cell_id="adv-inc-j-dr-amount"), _cell("")],
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="adv-inc-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="adv-inc-j-cr-amount")],
                [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="adv-inc-j-rev-dr-details"), _cell("", editable=True, cell_id="adv-inc-j-rev-dr-amount"), _cell("")],
                [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="adv-inc-j-rev-cr-details"), _cell(""), _cell("", editable=True, cell_id="adv-inc-j-rev-cr-amount")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=f"{scenario['prompt_intro']} Prepare the General Journal entry for the year-end adjustment dated {scenario['year_end_date']} and the reversal on {scenario['reversal_date']}.",
            table=advance_income_journal_table,
            correct_map={
                "adv-inc-j-dr-details": income_label,
                "adv-inc-j-dr-amount": scenario["amount"],
                "adv-inc-j-cr-details": "Income received in advance",
                "adv-inc-j-cr-amount": scenario["amount"],
                "adv-inc-j-rev-dr-details": "Income received in advance",
                "adv-inc-j-rev-dr-amount": scenario["amount"],
                "adv-inc-j-rev-cr-details": income_label,
                "adv-inc-j-rev-cr-amount": scenario["amount"],
            },
            derivation_map={
                "adv-inc-j-dr-amount": f"Use the unearned income amount given: R{int(scenario['amount']):,}",
                "adv-inc-j-rev-dr-amount": f"The reversal uses the same amount as the year-end adjustment: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "adv-inc-j-dr-details": f"At year-end, debit the income account: {income_label}.",
                "adv-inc-j-cr-details": "Credit Income received in advance to create the liability.",
                "adv-inc-j-rev-dr-details": "The reversal debits the liability account first.",
                "adv-inc-j-rev-cr-details": "The reversal credits the original income account.",
            },
            guidelines=[
                f"Year-end: Dr {income_label} / Cr Income received in advance.",
                f"Reversal next period: Dr Income received in advance / Cr {income_label}.",
            ],
            marks=8,
        ), "income_received_in_advance_reversal_journal_fill", expected_cells=8, amount=scenario["amount"], amount_cell_ids=["adv-inc-j-dr-amount", "adv-inc-j-cr-amount", "adv-inc-j-rev-dr-amount", "adv-inc-j-rev-cr-amount"]))
        advance_income_analysis_table = {
            "heading": f"Adjustment analysis: {str(income_label).lower()}",
            "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
            "rows": [
                [_cell(f"{income_label} received before it is earned"), _cell("", editable=True, cell_id="adv-inc-a-amount"), _cell("", editable=True, cell_id="adv-inc-a-dr"), _cell("", editable=True, cell_id="adv-inc-a-cr"), _cell("", editable=True, cell_id="adv-inc-a-is"), _cell("", editable=True, cell_id="adv-inc-a-bs")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="adjustment_analysis_table",
            prompt=f"{scenario['prompt_intro']} Complete the adjustment analysis table for the year-end adjustment.",
            table=advance_income_analysis_table,
            correct_map={
                "adv-inc-a-amount": scenario["amount"],
                "adv-inc-a-dr": income_label,
                "adv-inc-a-cr": "Income received in advance",
                "adv-inc-a-is": "Income decreases by R" + f"{int(scenario['amount']):,}",
                "adv-inc-a-bs": "Current liability increases by R" + f"{int(scenario['amount']):,}",
            },
            derivation_map={
                "adv-inc-a-amount": f"Use the amount not yet earned at year-end: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "adv-inc-a-dr": f"Debit {income_label} to remove the amount not yet earned from current-period income.",
                "adv-inc-a-cr": "Credit Income received in advance to show the liability.",
                "adv-inc-a-bs": "The Balance Sheet effect is a current liability increase.",
            },
            guidelines=[
                "Income received in advance reduces current-period income and creates a current liability.",
                "Use the same amount in the double entry and in the statement effects.",
            ],
            marks=6,
        ), "income_received_in_advance_analysis_fill", expected_cells=5, amount=scenario["amount"], amount_cell_id="adv-inc-a-amount"))
        advance_income_carry_tables = [
            {
                "heading": "Income Statement extract",
                "headers": ["Other income", "Amount"],
                "rows": [[_cell(income_label), _cell("", editable=True, cell_id="adv-inc-fa-income")]],
            },
            {
                "heading": "Balance Sheet extract",
                "headers": ["Current liabilities", "Amount"],
                "rows": [[_cell("Income received in advance"), _cell("", editable=True, cell_id="adv-inc-fa-liability")]],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the source extract and year-end adjustment to carry the effect of the deferred {str(income_label).lower()} into the Income Statement and Balance Sheet extracts.",
            prompt_table={
                "heading": "Source extract",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell(f"{income_label} before adjustment"), _cell(scenario["base_balance"])],
                    [_cell("Income received in advance adjustment"), _cell(scenario["amount"])],
                ],
            },
            tables=advance_income_carry_tables,
            correct_map={
                "adv-inc-fa-income": adjusted_income_advance_balance,
                "adv-inc-fa-liability": scenario["amount"],
            },
            derivation_map={
                "adv-inc-fa-income": f"Adjusted {income_label} = R{int(scenario['base_balance']):,} - R{int(scenario['amount']):,} = R{int(adjusted_income_advance_balance):,}",
                "adv-inc-fa-liability": f"Carry the deferred amount to Current liabilities: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "adv-inc-fa-income": f"Subtract the unearned amount from the {str(income_label).lower()} line in the Income Statement.",
                "adv-inc-fa-liability": "Carry the same amount to Income received in advance under Current liabilities.",
            },
            guidelines=[
                f"Subtract the deferred amount from the {income_label} figure in the Income Statement.",
                "Carry the same amount to Income received in advance under Current liabilities.",
            ],
            marks=4,
        ), "income_received_in_advance_carrythrough_fill", expected_cells=2, adjusted_amount=adjusted_income_advance_balance, carry_amount=scenario["amount"], adjusted_cell_id="adv-inc-fa-income", carry_cell_id="adv-inc-fa-liability"))
        advance_income_tb_bank = _round_money(float(scenario["base_balance"]) + 41000.0)
        advance_income_tb_stock = _round_money(float(scenario["amount"]) + 16000.0)
        advance_income_tb_capital = _round_money(float(advance_income_tb_bank) + float(advance_income_tb_stock) - float(scenario["base_balance"]))
        advance_income_tb_total = _round_money(float(advance_income_tb_bank) + float(advance_income_tb_stock))
        advance_income_tb_prompt_tables = [
            {
                "heading": "Pre-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell(advance_income_tb_bank), _cell("")],
                    [_cell("Trading stock"), _cell(advance_income_tb_stock), _cell("")],
                    [_cell(income_label), _cell(""), _cell(scenario["base_balance"])],
                    [_cell("Capital"), _cell(""), _cell(advance_income_tb_capital)],
                ],
            },
            {
                "heading": "Year-end adjustment",
                "headers": ["Adjustment", "Amount"],
                "rows": [[_cell(f"Income received in advance for {str(income_label).lower()}"), _cell(scenario["amount"])]]
            },
        ]
        advance_income_tb_table = {
            "heading": "Post-adjustment Trial Balance extract",
            "headers": ["Account", "Debit", "Credit"],
            "rows": [
                [_cell("Bank"), _cell("", editable=True, cell_id="adv-inc-patb-bank-debit"), _cell("")],
                [_cell("Trading stock"), _cell("", editable=True, cell_id="adv-inc-patb-stock-debit"), _cell("")],
                [_cell(income_label), _cell(""), _cell("", editable=True, cell_id="adv-inc-patb-income-credit")],
                [_cell("Income received in advance"), _cell(""), _cell("", editable=True, cell_id="adv-inc-patb-liability-credit")],
                [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="adv-inc-patb-capital-credit")],
                [_cell("Total"), _cell("", editable=True, cell_id="adv-inc-patb-total-debit"), _cell("", editable=True, cell_id="adv-inc-patb-total-credit")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="trial_balance_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the year-end adjustment to complete the Post-adjustment Trial Balance extract for income received in advance from {str(income_label).lower()}.",
            prompt_tables=advance_income_tb_prompt_tables,
            table=advance_income_tb_table,
            correct_map={
                "adv-inc-patb-bank-debit": advance_income_tb_bank,
                "adv-inc-patb-stock-debit": advance_income_tb_stock,
                "adv-inc-patb-income-credit": adjusted_income_advance_balance,
                "adv-inc-patb-liability-credit": scenario["amount"],
                "adv-inc-patb-capital-credit": advance_income_tb_capital,
                "adv-inc-patb-total-debit": advance_income_tb_total,
                "adv-inc-patb-total-credit": advance_income_tb_total,
            },
            derivation_map={
                "adv-inc-patb-income-credit": f"Adjusted {income_label} = R{int(scenario['base_balance']):,} - R{int(scenario['amount']):,} = R{int(adjusted_income_advance_balance):,}",
                "adv-inc-patb-total-credit": f"Total credit = adjusted {income_label} + Income received in advance + Capital = R{int(adjusted_income_advance_balance):,} + R{int(scenario['amount']):,} + R{int(advance_income_tb_capital):,} = R{int(advance_income_tb_total):,}",
            },
            cell_hints={
                "adv-inc-patb-income-credit": f"Remove the unearned amount from the {str(income_label).lower()} balance.",
                "adv-inc-patb-liability-credit": "Show the unearned amount as Income received in advance.",
                "adv-inc-patb-total-credit": "Total all credit balances after separating the deferred income liability.",
            },
            guidelines=[
                "Copy unchanged balances from the Pre-adjustment Trial Balance.",
                f"Reduce {income_label} by the unearned amount and show the same amount as Income received in advance on the credit side.",
            ],
            marks=7,
        ), "income_received_in_advance_post_adjustment_tb_fill", expected_cells=7, total=advance_income_tb_total, adjusted_amount=adjusted_income_advance_balance, carry_amount=scenario["amount"], adjusted_cell_id="adv-inc-patb-income-credit", carry_cell_id="adv-inc-patb-liability-credit", total_debit_cell_id="adv-inc-patb-total-debit", total_credit_cell_id="adv-inc-patb-total-credit"))
        advance_income_mini_tables = [
            {
                "heading": "Part A: General Journal",
                "headers": ["Date", "Details", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="adv-inc-mini-j-dr-details"), _cell("", editable=True, cell_id="adv-inc-mini-j-dr-amount"), _cell("")],
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="adv-inc-mini-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="adv-inc-mini-j-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="adv-inc-mini-j-rev-dr-details"), _cell("", editable=True, cell_id="adv-inc-mini-j-rev-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="adv-inc-mini-j-rev-cr-details"), _cell(""), _cell("", editable=True, cell_id="adv-inc-mini-j-rev-cr-amount")],
                ],
            },
            {
                "heading": "Part B: Adjustment analysis",
                "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
                "rows": [
                    [_cell(f"{income_label} received before it is earned"), _cell("", editable=True, cell_id="adv-inc-mini-a-amount"), _cell("", editable=True, cell_id="adv-inc-mini-a-dr"), _cell("", editable=True, cell_id="adv-inc-mini-a-cr"), _cell("", editable=True, cell_id="adv-inc-mini-a-is"), _cell("", editable=True, cell_id="adv-inc-mini-a-bs")],
                ],
            },
            {
                "heading": "Part C1: Income Statement extract",
                "headers": ["Other income", "Amount"],
                "rows": [[_cell(income_label), _cell("", editable=True, cell_id="adv-inc-mini-fa-income")]],
            },
            {
                "heading": "Part C2: Balance Sheet extract",
                "headers": ["Current liabilities", "Amount"],
                "rows": [[_cell("Income received in advance"), _cell("", editable=True, cell_id="adv-inc-mini-fa-liability")]],
            },
            {
                "heading": "Part D: Post-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="adv-inc-mini-patb-bank-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="adv-inc-mini-patb-stock-debit"), _cell("")],
                    [_cell(income_label), _cell(""), _cell("", editable=True, cell_id="adv-inc-mini-patb-income-credit")],
                    [_cell("Income received in advance"), _cell(""), _cell("", editable=True, cell_id="adv-inc-mini-patb-liability-credit")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="adv-inc-mini-patb-capital-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="adv-inc-mini-patb-total-debit"), _cell("", editable=True, cell_id="adv-inc-mini-patb-total-credit")],
                ],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the year-end adjustment to complete the integrated reversal mini-project for income received in advance from {str(income_label).lower()}: (A) General Journal adjustment and reversal, (B) adjustment analysis, (C) Income Statement and Balance Sheet extracts, and (D) Post-adjustment Trial Balance extract.",
            prompt_tables=advance_income_tb_prompt_tables,
            tables=advance_income_mini_tables,
            correct_map={
                "adv-inc-mini-j-dr-details": income_label,
                "adv-inc-mini-j-dr-amount": scenario["amount"],
                "adv-inc-mini-j-cr-details": "Income received in advance",
                "adv-inc-mini-j-cr-amount": scenario["amount"],
                "adv-inc-mini-j-rev-dr-details": "Income received in advance",
                "adv-inc-mini-j-rev-dr-amount": scenario["amount"],
                "adv-inc-mini-j-rev-cr-details": income_label,
                "adv-inc-mini-j-rev-cr-amount": scenario["amount"],
                "adv-inc-mini-a-amount": scenario["amount"],
                "adv-inc-mini-a-dr": income_label,
                "adv-inc-mini-a-cr": "Income received in advance",
                "adv-inc-mini-a-is": "Income decreases by R" + f"{int(scenario['amount']):,}",
                "adv-inc-mini-a-bs": "Current liability increases by R" + f"{int(scenario['amount']):,}",
                "adv-inc-mini-fa-income": adjusted_income_advance_balance,
                "adv-inc-mini-fa-liability": scenario["amount"],
                "adv-inc-mini-patb-bank-debit": advance_income_tb_bank,
                "adv-inc-mini-patb-stock-debit": advance_income_tb_stock,
                "adv-inc-mini-patb-income-credit": adjusted_income_advance_balance,
                "adv-inc-mini-patb-liability-credit": scenario["amount"],
                "adv-inc-mini-patb-capital-credit": advance_income_tb_capital,
                "adv-inc-mini-patb-total-debit": advance_income_tb_total,
                "adv-inc-mini-patb-total-credit": advance_income_tb_total,
            },
            derivation_map={
                "adv-inc-mini-fa-income": f"Adjusted {income_label} = R{int(scenario['base_balance']):,} - R{int(scenario['amount']):,} = R{int(adjusted_income_advance_balance):,}",
                "adv-inc-mini-patb-income-credit": f"Carry the adjusted {income_label} figure from Part C1 into Part D: R{int(adjusted_income_advance_balance):,}",
                "adv-inc-mini-patb-total-credit": f"Total credit = adjusted {income_label} + Income received in advance + Capital = R{int(adjusted_income_advance_balance):,} + R{int(scenario['amount']):,} + R{int(advance_income_tb_capital):,} = R{int(advance_income_tb_total):,}",
            },
            cell_hints={
                "adv-inc-mini-j-cr-details": "The year-end journal credits Income received in advance to create the liability.",
                "adv-inc-mini-a-dr": f"Debit {income_label} because part of the recorded income belongs to the next period.",
                "adv-inc-mini-fa-income": "Subtract the unearned portion before carrying the income balance to later parts.",
                "adv-inc-mini-patb-liability-credit": "The same amount also appears as a liability in the trial balance.",
                "adv-inc-mini-patb-total-credit": "Use the completed Part D balances to total the credit column.",
            },
            cell_teaching_map={
                "adv-inc-mini-fa-income": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {str(income_label).lower()} amount into the Income Statement extract.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance shows {income_label} at R{int(scenario['base_balance']):,} and the year-end adjustment removes the unearned amount of R{int(scenario['amount']):,}.",
                    rule_or_principle="Income received in advance must be removed from current-period income because it belongs to the next period.",
                    how_to_derive=f"R{int(scenario['base_balance']):,} - R{int(scenario['amount']):,} = R{int(adjusted_income_advance_balance):,}.",
                    transfer_tip="In integrated deferred-income questions, split the original income into the earned portion for this period and the liability to carry forward.",
                ),
                "adv-inc-mini-patb-liability-credit": _teaching_hint(
                    role_in_requirement="This cell places the deferred-income liability into the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The journal and analysis both use Income received in advance for R{int(scenario['amount']):,}.",
                    rule_or_principle="Income received in advance is a current liability and appears in the credit column of the adjusted trial balance.",
                    how_to_derive=f"Enter Income received in advance at R{int(scenario['amount']):,} in the credit column.",
                    transfer_tip="When an adjustment creates deferred income, it should appear in both the Balance Sheet effect and the adjusted trial balance.",
                ),
            },
            guidelines=[
                "Carry the same deferred-income amount consistently through the journal, analysis, statements, and trial balance.",
                "Use the adjusted income figure in both the Income Statement extract and the Post-adjustment Trial Balance.",
            ],
            marks=22,
        ), "income_received_in_advance_reversal_mini_project", expected_cells=22, amount=scenario["amount"], amount_cell_ids=["adv-inc-mini-j-dr-amount", "adv-inc-mini-j-cr-amount", "adv-inc-mini-j-rev-dr-amount", "adv-inc-mini-j-rev-cr-amount", "adv-inc-mini-a-amount", "adv-inc-mini-fa-liability", "adv-inc-mini-patb-liability-credit"], adjusted_amount=adjusted_income_advance_balance, adjusted_cell_ids=["adv-inc-mini-fa-income", "adv-inc-mini-patb-income-credit"], total=advance_income_tb_total, total_debit_cell_id="adv-inc-mini-patb-total-debit", total_credit_cell_id="adv-inc-mini-patb-total-credit"))
        advance_income_exam_tables = [
            {
                "heading": "Part A1: Income received in advance account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="adv-inc-ex-liability-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="adv-inc-ex-liability-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="adv-inc-ex-liability-rev-details"), _cell("GJ"), _cell("", editable=True, cell_id="adv-inc-ex-liability-rev-amount"), _cell("")],
                ],
            },
            {
                "heading": f"Part A2: {income_label} account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="adv-inc-ex-income-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="adv-inc-ex-income-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="adv-inc-ex-income-rev-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="adv-inc-ex-income-rev-amount")],
                ],
            },
            {
                "heading": "Part B1: Income Statement extract",
                "headers": ["Other income", "Amount"],
                "rows": [[_cell(income_label), _cell("", editable=True, cell_id="adv-inc-ex-fa-income")]],
            },
            {
                "heading": "Part B2: Balance Sheet extract",
                "headers": ["Current liabilities", "Amount"],
                "rows": [[_cell("Income received in advance"), _cell("", editable=True, cell_id="adv-inc-ex-fa-liability")]],
            },
            {
                "heading": "Part C: Post-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="adv-inc-ex-patb-bank-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="adv-inc-ex-patb-stock-debit"), _cell("")],
                    [_cell(income_label), _cell(""), _cell("", editable=True, cell_id="adv-inc-ex-patb-income-credit")],
                    [_cell("Income received in advance"), _cell(""), _cell("", editable=True, cell_id="adv-inc-ex-patb-liability-credit")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="adv-inc-ex-patb-capital-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="adv-inc-ex-patb-total-debit"), _cell("", editable=True, cell_id="adv-inc-ex-patb-total-credit")],
                ],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the deferred-income adjustment to complete the integrated income received in advance workflow for {str(income_label).lower()}: (A) post the year-end adjustment and the reversal to the ledger accounts, (B) carry the effect to the Income Statement and Balance Sheet extracts, and (C) complete the Post-adjustment Trial Balance extract.",
            prompt_tables=advance_income_tb_prompt_tables,
            tables=advance_income_exam_tables,
            correct_map={
                "adv-inc-ex-liability-cr-details": income_label,
                "adv-inc-ex-liability-cr-amount": scenario["amount"],
                "adv-inc-ex-liability-rev-details": income_label,
                "adv-inc-ex-liability-rev-amount": scenario["amount"],
                "adv-inc-ex-income-dr-details": "Income received in advance",
                "adv-inc-ex-income-dr-amount": scenario["amount"],
                "adv-inc-ex-income-rev-details": "Income received in advance",
                "adv-inc-ex-income-rev-amount": scenario["amount"],
                "adv-inc-ex-fa-income": adjusted_income_advance_balance,
                "adv-inc-ex-fa-liability": scenario["amount"],
                "adv-inc-ex-patb-bank-debit": advance_income_tb_bank,
                "adv-inc-ex-patb-stock-debit": advance_income_tb_stock,
                "adv-inc-ex-patb-income-credit": adjusted_income_advance_balance,
                "adv-inc-ex-patb-liability-credit": scenario["amount"],
                "adv-inc-ex-patb-capital-credit": advance_income_tb_capital,
                "adv-inc-ex-patb-total-debit": advance_income_tb_total,
                "adv-inc-ex-patb-total-credit": advance_income_tb_total,
            },
            derivation_map={
                "adv-inc-ex-liability-rev-amount": f"The reversal uses the same amount as the year-end deferred-income adjustment: R{int(scenario['amount']):,}",
                "adv-inc-ex-fa-income": f"Adjusted {income_label} = R{int(scenario['base_balance']):,} - R{int(scenario['amount']):,} = R{int(adjusted_income_advance_balance):,}",
                "adv-inc-ex-patb-income-credit": f"Carry the adjusted {income_label} amount into the credit column of the Post-adjustment Trial Balance: R{int(adjusted_income_advance_balance):,}",
                "adv-inc-ex-patb-total-credit": f"Total credit = adjusted {income_label} + Income received in advance + Capital = R{int(adjusted_income_advance_balance):,} + R{int(scenario['amount']):,} + R{int(advance_income_tb_capital):,} = R{int(advance_income_tb_total):,}",
            },
            cell_hints={
                "adv-inc-ex-liability-cr-details": "In the Income received in advance account, the details column shows the opposite account from the journal entry.",
                "adv-inc-ex-income-dr-details": "In the income account, use the opposite account from the deferred-income entry in the details column.",
                "adv-inc-ex-fa-income": "Subtract the unearned portion from the existing income balance before carrying it into the statement extract.",
                "adv-inc-ex-patb-liability-credit": "The same deferred amount appears as a current liability in the adjusted trial balance.",
                "adv-inc-ex-patb-total-credit": "Use all completed credit balances in Part C to total the column.",
            },
            cell_teaching_map={
                "adv-inc-ex-fa-income": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {str(income_label).lower()} figure into the Income Statement extract.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance gives {income_label} at R{int(scenario['base_balance']):,} and the year-end adjustment removes the unearned amount of R{int(scenario['amount']):,}.",
                    rule_or_principle="Income received in advance belongs to the next accounting period, so it must be removed from the current income account.",
                    how_to_derive=f"Subtract R{int(scenario['amount']):,} from R{int(scenario['base_balance']):,} to get R{int(adjusted_income_advance_balance):,}.",
                    transfer_tip="In integrated deferred-income workflows, adjust the income first and then carry the updated figure into later statement sections.",
                ),
                "adv-inc-ex-patb-liability-credit": _teaching_hint(
                    role_in_requirement="This cell shows the liability created by the deferred income in the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The year-end adjustment creates Income received in advance for R{int(scenario['amount']):,}.",
                    rule_or_principle="Income received in advance is a current liability and appears in the credit column of the adjusted trial balance.",
                    how_to_derive=f"Enter Income received in advance at R{int(scenario['amount']):,} on the credit side.",
                    transfer_tip="When an adjustment creates deferred income, check whether that account must be added to the adjusted trial balance.",
                ),
            },
            guidelines=[
                "Post the deferred-income adjustment and the reversal using the same amount in both ledger accounts.",
                "Carry the adjusted income figure consistently into the Income Statement and the Post-adjustment Trial Balance.",
                "Show the deferred amount as a current liability in both the Balance Sheet extract and the Post-adjustment Trial Balance.",
            ],
            marks=17,
        ), "income_received_in_advance_reversal_mini_project", expected_cells=17, amount=scenario["amount"], amount_cell_ids=["adv-inc-ex-liability-cr-amount", "adv-inc-ex-liability-rev-amount", "adv-inc-ex-income-dr-amount", "adv-inc-ex-income-rev-amount", "adv-inc-ex-fa-liability", "adv-inc-ex-patb-liability-credit"], adjusted_amount=adjusted_income_advance_balance, adjusted_cell_ids=["adv-inc-ex-fa-income", "adv-inc-ex-patb-income-credit"], total=advance_income_tb_total, total_debit_cell_id="adv-inc-ex-patb-total-debit", total_credit_cell_id="adv-inc-ex-patb-total-credit"))
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="ledger",
            prompt=f"{scenario['prompt_intro']} Post the year-end adjustment dated {scenario['year_end_date']} and the reversal on {scenario['reversal_date']}.",
            tables=advance_income_ledger_tables,
            correct_map={
                "adv-inc-cr-details": income_label,
                "adv-inc-cr-amount": scenario["amount"],
                "adv-inc-rev-details": income_label,
                "adv-inc-rev-amount": scenario["amount"],
                "rent-adv-dr-details": "Income received in advance",
                "rent-adv-dr-amount": scenario["amount"],
                "rent-adv-rev-details": "Income received in advance",
                "rent-adv-rev-amount": scenario["amount"],
            },
            derivation_map={
                "adv-inc-cr-amount": f"Use the unearned income amount at year-end: R{int(scenario['amount']):,}",
                "adv-inc-rev-amount": f"Reverse the same amount at the start of the next period: R{int(scenario['amount']):,}",
            },
            cell_hints={
                "adv-inc-cr-details": f"The liability account uses {str(income_label).lower()} as the opposite account at year-end.",
                "rent-adv-dr-details": "The income account uses Income received in advance as the opposite account.",
                "rent-adv-rev-details": "The reversal keeps the same opposite account in the details column.",
            },
            cell_teaching_map={
                "adv-inc-cr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the opposite account for the year-end credit in the liability account.",
                    evidence_from_question=f"Income received in advance is recorded by debiting {income_label} and crediting Income received in advance.",
                    rule_or_principle="The details column shows the opposite account used in the journal entry.",
                    how_to_derive=f"Because Income received in advance is credited, the details entry is {income_label}.",
                    transfer_tip="For unearned income, reduce the income account and create a liability for the same amount.",
                ),
                "rent-adv-dr-amount": _teaching_hint(
                    role_in_requirement=f"This cell reduces the {str(income_label).lower()} account for the portion not yet earned.",
                    evidence_from_question="The amount was received before it was earned, so it belongs to the next period.",
                    rule_or_principle="Income received in advance decreases current-period income and creates a liability.",
                    how_to_derive=f"Debit {income_label} with the full deferred amount R{int(scenario['amount']):,}.",
                    transfer_tip="If income is received early, take it out of this year's income and carry it as a liability.",
                ),
                "rent-adv-rev-details": _teaching_hint(
                    role_in_requirement=f"This cell identifies the opposite account for the reversal in the {income_label} account.",
                    evidence_from_question=f"The question requires the reversal on {scenario['reversal_date']}.",
                    rule_or_principle="The reversal uses the same account pair as the year-end adjustment.",
                    how_to_derive="The opposite account remains Income received in advance, so that is the details entry.",
                    transfer_tip="Use reversals so that the next period's actual receipt or earning can be recorded normally.",
                ),
            },
            guidelines=[
                f"Year-end: Dr {income_label} / Cr Income received in advance.",
                f"Reversal next year: Dr Income received in advance / Cr {income_label}.",
            ],
            marks=8,
        ), "income_received_in_advance_reversal_ledger_fill", expected_cells=8, amount=scenario["amount"], amount_cell_ids=["adv-inc-cr-amount", "adv-inc-rev-amount", "rent-adv-dr-amount", "rent-adv-rev-amount"]))

    return pool


__all__ = ["_gen_reversal_adjustments"]
