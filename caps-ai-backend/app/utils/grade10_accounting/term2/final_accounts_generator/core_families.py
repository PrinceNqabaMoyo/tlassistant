from __future__ import annotations

import random
from typing import Any, Dict, List

from ....sole_trader.names import pick_business_name as _pick_business_name
from .shared import (
    _cell,
    _make_calc,
    _make_fill_in_table_question,
    _make_mcq,
    _make_typed,
    _round_money,
    _teaching_hint,
    _with_validation,
)


def _gen_closing_transfers(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    biz = _pick_business_name(r=r)

    pool.append(_make_mcq(
        prompt="What is the first step in the closing transfer process?",
        options=[
            "Balance the Capital account.",
            "Transfer Debtors' Allowances to Sales to get net sales.",
            "Prepare the Balance Sheet.",
            "Close the Bank account.",
        ],
        correct_index=1,
        explanation="Step 1: Transfer Debtors' Allowances account to Sales account to determine net sales.",
    ))

    pool.append(_make_mcq(
        prompt="After closing the Trading account, the balance represents:",
        options=[
            "Net profit for the year.",
            "Gross profit, which is transferred to the Profit and Loss account.",
            "Total assets of the business.",
            "The owner's drawings for the year.",
        ],
        correct_index=1,
        explanation="The Trading account balance = Gross Profit (Net Sales – Cost of Sales), which is transferred to the Profit and Loss account.",
    ))

    pool.append(_make_mcq(
        prompt="Where is the net profit transferred to at the end of the financial year?",
        options=[
            "The Bank account.",
            "The Trading account.",
            "The Capital account.",
            "The Creditors control account.",
        ],
        correct_index=2,
        explanation="Net profit from the Profit and Loss account is transferred to the Capital account (increasing owner's equity).",
    ))

    pool.append(_make_mcq(
        prompt="Which account is closed directly to the Capital account during closing transfers?",
        options=[
            "Drawings",
            "Cost of Sales",
            "Sales",
            "Creditors control",
        ],
        correct_index=0,
        explanation="The Drawings account is closed directly to the Capital account at year-end.",
    ))

    pool.append(_make_mcq(
        prompt="After the Trading account is balanced, where is the gross profit transferred?",
        options=[
            "Bank",
            "Profit and Loss account",
            "Creditors control",
            "Post-closing Trial Balance",
        ],
        correct_index=1,
        explanation="Gross profit is transferred from the Trading account to the Profit and Loss account.",
    ))

    sales = r.choice([500000, 650000, 742000, 830000, 842000, 950000])
    debtors_allow = r.choice([8000, 10000, 12000, 15000])
    net_sales = sales - debtors_allow
    cos = r.choice([300000, 350000, 415000, 480000])
    gross_profit = net_sales - cos

    pool.append(_with_validation(_make_calc(
        prompt=f"{biz} has the following balances:\n• Sales: R{sales:,}\n• Debtors' Allowances: R{debtors_allow:,}\n• Cost of Sales: R{cos:,}\n\nCalculate the gross profit.",
        correct_answer=float(gross_profit),
        working_formula=f"Gross Profit = (Sales - Debtors' Allowances) - Cost of Sales = (R{sales:,} - R{debtors_allow:,}) - R{cos:,}",
        formula_hint="Gross Profit = (Sales - Debtors' Allowances) - Cost of Sales",
    ), "closing_gross_profit", sales=sales, debtors_allow=debtors_allow, cost_of_sales=cos))

    other_income = r.choice([50000, 72000, 94600])
    total_expenses = r.choice([350000, 400000, 425000])
    net_profit = gross_profit + other_income - total_expenses

    pool.append(_with_validation(_make_calc(
        prompt=f"{biz}'s Trading account shows a gross profit of R{gross_profit:,}. Other income totals R{other_income:,} and total expenses are R{total_expenses:,}.\n\nCalculate the net profit.",
        correct_answer=float(net_profit),
        working_formula=f"Net Profit = Gross Profit + Other Income - Total Expenses = R{gross_profit:,} + R{other_income:,} - R{total_expenses:,}",
        formula_hint="Net Profit = Gross Profit + Other Income - Total Expenses",
    ), "closing_net_profit", gross_profit=gross_profit, other_income=other_income, total_expenses=total_expenses))

    opening_capital = r.choice([180000, 234500, 295000, 350000])
    drawings = r.choice([18000, 23800, 30000])
    closing_capital = opening_capital + net_profit - drawings

    pool.append(_with_validation(_make_calc(
        prompt=f"{biz}'s Capital balance at beginning of year: R{opening_capital:,}. Net profit: R{net_profit:,}. Drawings: R{drawings:,}.\n\nCalculate the closing Capital balance.",
        correct_answer=float(closing_capital),
        working_formula="Closing Capital = Opening Capital + Net Profit - Drawings",
        formula_hint="Closing Capital = Opening Capital + Net Profit - Drawings",
    ), "closing_capital", opening_capital=opening_capital, net_profit=net_profit, drawings=drawings))

    capital_scenario = r.choice([
        {"bank": 84000, "debtors": 46000, "stock": 52000, "equipment_cost": 180000, "accumdep": 36000, "creditors": 42000, "loan": 50000, "additional_capital": 30000, "net_profit": 76000, "drawings": 24000},
        {"bank": 72000, "debtors": 38000, "stock": 41000, "equipment_cost": 165000, "accumdep": 27000, "creditors": 36000, "loan": 44000, "additional_capital": 25000, "net_profit": 69000, "drawings": 20000},
        {"bank": 93000, "debtors": 54000, "stock": 47000, "equipment_cost": 190000, "accumdep": 42000, "creditors": 48000, "loan": 55000, "additional_capital": 35000, "net_profit": 81000, "drawings": 26000},
    ])
    capital_asset_total = _round_money(
        float(capital_scenario["bank"]) + float(capital_scenario["debtors"]) + float(capital_scenario["stock"]) + float(capital_scenario["equipment_cost"]) - float(capital_scenario["accumdep"])
    )
    capital_liability_total = _round_money(float(capital_scenario["creditors"]) + float(capital_scenario["loan"]))
    integrated_closing_capital = _round_money(capital_asset_total - capital_liability_total)
    integrated_opening_capital = _round_money(
        integrated_closing_capital - float(capital_scenario["additional_capital"]) - float(capital_scenario["net_profit"]) + float(capital_scenario["drawings"])
    )
    capital_prompt_tables = [
        {
            "heading": "Adjusted Balance Sheet information",
            "headers": ["Item", "Amount"],
            "rows": [
                [_cell("Bank"), _cell(capital_scenario["bank"])],
                [_cell("Debtors control"), _cell(capital_scenario["debtors"])],
                [_cell("Trading stock"), _cell(capital_scenario["stock"])],
                [_cell("Equipment at cost"), _cell(capital_scenario["equipment_cost"])],
                [_cell("Accumulated depreciation on equipment"), _cell(capital_scenario["accumdep"])],
                [_cell("Creditors control"), _cell(capital_scenario["creditors"])],
                [_cell("Loan"), _cell(capital_scenario["loan"])],
            ],
        },
        {
            "heading": "Owner's equity movements during the year",
            "headers": ["Item", "Amount"],
            "rows": [
                [_cell("Additional capital introduced"), _cell(capital_scenario["additional_capital"])],
                [_cell("Net profit for the year"), _cell(capital_scenario["net_profit"])],
                [_cell("Drawings"), _cell(capital_scenario["drawings"])],
            ],
        },
    ]
    capital_tables = [
        {
            "heading": "Part A: Determine closing capital from the Balance Sheet equation",
            "headers": ["Item", "Amount"],
            "rows": [
                [_cell("Total assets"), _cell("", editable=True, cell_id="cap-total-assets")],
                [_cell("Total liabilities"), _cell("", editable=True, cell_id="cap-total-liabilities")],
                [_cell("Closing capital"), _cell("", editable=True, cell_id="cap-closing-capital-a")],
            ],
        },
        {
            "heading": "Part B: Capital calculation",
            "headers": ["Item", "Amount"],
            "rows": [
                [_cell("Opening capital"), _cell("", editable=True, cell_id="cap-opening-capital")],
                [_cell("Additional capital introduced"), _cell("", editable=True, cell_id="cap-additional-capital")],
                [_cell("Net profit"), _cell("", editable=True, cell_id="cap-net-profit")],
                [_cell("Drawings"), _cell("", editable=True, cell_id="cap-drawings")],
                [_cell("Closing capital"), _cell("", editable=True, cell_id="cap-closing-capital-b")],
            ],
        },
        {
            "heading": "Part C: Owner's equity extract",
            "headers": ["Description", "Amount"],
            "rows": [
                [_cell("Capital at beginning of year"), _cell("", editable=True, cell_id="cap-equity-opening")],
                [_cell("Add: Additional capital introduced"), _cell("", editable=True, cell_id="cap-equity-additional")],
                [_cell("Add: Net profit"), _cell("", editable=True, cell_id="cap-equity-profit")],
                [_cell("Less: Drawings"), _cell("", editable=True, cell_id="cap-equity-drawings")],
                [_cell("Capital at end of year"), _cell("", editable=True, cell_id="cap-equity-closing")],
            ],
        },
    ]
    capital_correct_map = {
        "cap-total-assets": capital_asset_total,
        "cap-total-liabilities": capital_liability_total,
        "cap-closing-capital-a": integrated_closing_capital,
        "cap-opening-capital": integrated_opening_capital,
        "cap-additional-capital": capital_scenario["additional_capital"],
        "cap-net-profit": capital_scenario["net_profit"],
        "cap-drawings": capital_scenario["drawings"],
        "cap-closing-capital-b": integrated_closing_capital,
        "cap-equity-opening": integrated_opening_capital,
        "cap-equity-additional": capital_scenario["additional_capital"],
        "cap-equity-profit": capital_scenario["net_profit"],
        "cap-equity-drawings": capital_scenario["drawings"],
        "cap-equity-closing": integrated_closing_capital,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="final_account_table",
        prompt=f"Use the adjusted information for {biz} to complete the capital-calculation workflow: (A) determine closing capital from the Balance Sheet equation, (B) complete the capital calculation, and (C) complete the owner's equity extract.",
        prompt_tables=capital_prompt_tables,
        tables=capital_tables,
        correct_map=capital_correct_map,
        derivation_map={
            "cap-total-assets": f"Total assets = Bank R{int(capital_scenario['bank']):,} + Debtors R{int(capital_scenario['debtors']):,} + Trading stock R{int(capital_scenario['stock']):,} + Equipment cost R{int(capital_scenario['equipment_cost']):,} - Accumulated depreciation R{int(capital_scenario['accumdep']):,} = R{int(capital_asset_total):,}",
            "cap-total-liabilities": f"Total liabilities = Creditors R{int(capital_scenario['creditors']):,} + Loan R{int(capital_scenario['loan']):,} = R{int(capital_liability_total):,}",
            "cap-closing-capital-a": f"Closing capital = Total assets R{int(capital_asset_total):,} - Total liabilities R{int(capital_liability_total):,} = R{int(integrated_closing_capital):,}",
            "cap-opening-capital": f"Opening capital = Closing capital R{int(integrated_closing_capital):,} - Additional capital R{int(capital_scenario['additional_capital']):,} - Net profit R{int(capital_scenario['net_profit']):,} + Drawings R{int(capital_scenario['drawings']):,} = R{int(integrated_opening_capital):,}",
            "cap-closing-capital-b": f"Closing capital = Opening capital R{int(integrated_opening_capital):,} + Additional capital R{int(capital_scenario['additional_capital']):,} + Net profit R{int(capital_scenario['net_profit']):,} - Drawings R{int(capital_scenario['drawings']):,} = R{int(integrated_closing_capital):,}",
        },
        cell_hints={
            "cap-total-assets": "Remember to deduct accumulated depreciation from equipment cost when working out the asset total.",
            "cap-total-liabilities": "Add the liability balances only; do not include capital in this total.",
            "cap-closing-capital-a": "Closing capital is the balancing figure after deducting liabilities from total assets.",
            "cap-opening-capital": "Rearrange the capital formula to solve for opening capital after using closing capital from Part A.",
            "cap-closing-capital-b": "Part B must finish with the same closing capital already determined in Part A.",
            "cap-equity-closing": "Carry the same closing capital amount into the owner's equity extract.",
        },
        cell_teaching_map={
            "cap-total-assets": _teaching_hint(
                role_in_requirement="This cell totals the assets that support the closing capital figure.",
                evidence_from_question="The Balance Sheet information includes Bank, Debtors control, Trading stock, Equipment at cost, and Accumulated depreciation on equipment.",
                rule_or_principle="Total assets include current assets plus the carrying value of non-current assets, not the asset cost before depreciation.",
                method_or_formula="Add the current assets and the carrying value of the equipment after deducting accumulated depreciation.",
                record_link="This total is then compared with total liabilities to determine closing capital by the accounting equation.",
                how_to_derive=f"Add R{int(capital_scenario['bank']):,} + R{int(capital_scenario['debtors']):,} + R{int(capital_scenario['stock']):,} + R{int(capital_scenario['equipment_cost']):,} - R{int(capital_scenario['accumdep']):,} to get R{int(capital_asset_total):,}.",
                transfer_tip="When a fixed asset and accumulated depreciation are both shown, convert them to carrying value before using them in capital or Balance Sheet totals.",
            ),
            "cap-total-liabilities": _teaching_hint(
                role_in_requirement="This cell totals the liabilities used in the closing-capital calculation.",
                evidence_from_question=f"The Balance Sheet information lists Creditors control of R{int(capital_scenario['creditors']):,} and a Loan of R{int(capital_scenario['loan']):,}.",
                rule_or_principle="Total liabilities are the sum of the liability balances only.",
                method_or_formula="Add the two liability amounts together before applying the accounting equation.",
                record_link="This liability total is deducted from total assets to determine closing capital in Part A.",
                how_to_derive=f"R{int(capital_scenario['creditors']):,} + R{int(capital_scenario['loan']):,} = R{int(capital_liability_total):,}.",
                transfer_tip="Keep liabilities separate from capital when using the accounting equation to solve for owner's equity.",
            ),
            "cap-opening-capital": _teaching_hint(
                role_in_requirement="This cell identifies the opening owner-equity balance for the capital calculation.",
                evidence_from_question="Part B must use the closing capital from Part A together with additional capital, net profit, and drawings given in the owner's equity movements table.",
                rule_or_principle="Opening capital = Closing capital - Additional capital - Net profit + Drawings.",
                method_or_formula="Reverse the usual capital-movement formula because the closing capital is already known.",
                record_link="This opening capital then becomes the first line in both the capital calculation and the owner's equity extract.",
                how_to_derive=f"R{int(integrated_closing_capital):,} - R{int(capital_scenario['additional_capital']):,} - R{int(capital_scenario['net_profit']):,} + R{int(capital_scenario['drawings']):,} = R{int(integrated_opening_capital):,}.",
                transfer_tip="If the question gives closing capital and the year's movements, reverse the normal capital formula carefully to solve for the missing opening figure.",
            ),
            "cap-closing-capital-b": _teaching_hint(
                role_in_requirement="This cell completes the capital-calculation section with the final closing balance.",
                evidence_from_question="Part B uses Opening capital, Additional capital, Net profit, and Drawings to rebuild the year-end capital figure.",
                rule_or_principle="Closing capital = Opening capital + Additional capital + Net profit - Drawings.",
                method_or_formula="Add the increases to capital and deduct drawings to arrive at the same closing balance found in Part A.",
                record_link="This closing balance must agree with both Part A and the owner's equity extract in Part C.",
                how_to_derive=f"R{int(integrated_opening_capital):,} + R{int(capital_scenario['additional_capital']):,} + R{int(capital_scenario['net_profit']):,} - R{int(capital_scenario['drawings']):,} = R{int(integrated_closing_capital):,}.",
                transfer_tip="Use repeated figures across parts as a self-check: the closing capital should stay consistent wherever it appears.",
            ),
            "cap-equity-closing": _teaching_hint(
                role_in_requirement="This cell carries the final capital balance into the owner's equity extract.",
                evidence_from_question="Part C is a presentation step based on the figures already worked out in Parts A and B.",
                rule_or_principle="The closing capital in a capital calculation must agree with the final capital shown in the owner's equity section.",
                method_or_formula="Transfer the already-established closing capital unchanged into the last line of the equity extract.",
                record_link="This line is the owner's-equity presentation equivalent of the closing-capital balance in Parts A and B.",
                how_to_derive=f"Copy the closing capital already established: R{int(integrated_closing_capital):,}.",
                transfer_tip="When the same figure appears in later tables, transfer it exactly rather than recalculating from scratch unless the question introduces a new adjustment.",
            ),
        },
        working_map={
            "cap-total-assets": "Part A uses the accounting equation first: find total assets, then total liabilities, then derive closing capital.",
            "cap-opening-capital": "Part B reverses the capital formula because the closing capital from Part A is already known.",
            "cap-closing-capital-b": "Use Part B as a reconstruction check that the closing capital agrees with Part A.",
            "cap-equity-closing": "Part C is a presentation carry-through of the same capital figures already worked out in Parts A and B.",
        },
        guidelines=[
            "Use carrying value for equipment when determining total assets.",
            "Find closing capital from assets minus liabilities before reversing the capital formula to determine opening capital.",
            "Carry the same capital figures consistently across the capital calculation and owner's equity extract.",
        ],
        marks=18,
    ), "capital_calculation_integrated_fill", expected_cells=13, cell_expectations=capital_correct_map))

    pool.append(_with_validation(_make_typed(
        prompt="List the 9 steps in the closing transfer process in order.",
        sample_answer=(
            "1. Transfer Debtors' Allowances to Sales (net sales)\n"
            "2. Transfer Sales and Cost of Sales to Trading account\n"
            "3. Balance Trading account (gross profit) → transfer to P&L\n"
            "4. Transfer all income accounts to P&L\n"
            "5. Transfer all expense accounts to P&L\n"
            "6. Balance P&L (net profit) → transfer to Capital\n"
            "7. Close Drawings to Capital\n"
            "8. Balance the Capital account\n"
            "9. Prepare Post-closing Trial Balance"
        ),
        grading_rubric=["debtors allowances to sales", "trading account", "profit and loss", "capital", "post-closing trial balance"],
    ), "closing_steps_typed", minimum_parts=9))

    closing_workflow_scenario = r.choice([
        {"bank": 62000, "stock": 28000, "equipment": 160000, "creditors": 24000, "loan": 36000, "net_profit": 68000, "drawings": 20000},
        {"bank": 74000, "stock": 36000, "equipment": 170000, "creditors": 30000, "loan": 40000, "net_profit": 82000, "drawings": 26000},
        {"bank": 58000, "stock": 30000, "equipment": 132000, "creditors": 20000, "loan": 26000, "net_profit": 54000, "drawings": 18000},
    ])
    workflow_debtors_allow = r.choice([8000, 10000, 12000, 15000])
    workflow_postclosing_total = _round_money(
        float(closing_workflow_scenario["bank"]) + float(closing_workflow_scenario["stock"]) + float(closing_workflow_scenario["equipment"])
    )
    workflow_closing_capital = _round_money(
        workflow_postclosing_total - float(closing_workflow_scenario["creditors"]) - float(closing_workflow_scenario["loan"])
    )
    workflow_opening_capital = _round_money(
        workflow_closing_capital - float(closing_workflow_scenario["net_profit"]) + float(closing_workflow_scenario["drawings"])
    )
    workflow_capital_total = _round_money(workflow_opening_capital + float(closing_workflow_scenario["net_profit"]))
    closing_workflow_prompt_tables = [
        {
            "heading": "Year-end closing information",
            "headers": ["Item", "Amount / detail"],
            "rows": [
                [_cell("Debtors' Allowances balance to be closed"), _cell(workflow_debtors_allow)],
                [_cell("Net profit already determined from the Profit and Loss account"), _cell(closing_workflow_scenario["net_profit"])],
                [_cell("Drawings balance to be closed"), _cell(closing_workflow_scenario["drawings"])],
                [_cell("Opening capital"), _cell(workflow_opening_capital)],
            ],
        },
        {
            "heading": "Balances remaining after nominal accounts are closed",
            "headers": ["Account", "Amount"],
            "rows": [
                [_cell("Bank"), _cell(closing_workflow_scenario["bank"])],
                [_cell("Trading stock"), _cell(closing_workflow_scenario["stock"])],
                [_cell("Equipment"), _cell(closing_workflow_scenario["equipment"])],
                [_cell("Creditors control"), _cell(closing_workflow_scenario["creditors"])],
                [_cell("Loan"), _cell(closing_workflow_scenario["loan"])],
            ],
        },
    ]
    closing_workflow_tables = [
        {
            "heading": "Part A: General Journal closing entries",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ct-gj-1-dr-details"), _cell("", editable=True, cell_id="ct-gj-1-dr-amount"), _cell("")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ct-gj-1-cr-details"), _cell(""), _cell("", editable=True, cell_id="ct-gj-1-cr-amount")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ct-gj-2-dr-details"), _cell("", editable=True, cell_id="ct-gj-2-dr-amount"), _cell("")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ct-gj-2-cr-details"), _cell(""), _cell("", editable=True, cell_id="ct-gj-2-cr-amount")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ct-gj-3-dr-details"), _cell("", editable=True, cell_id="ct-gj-3-dr-amount"), _cell("")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ct-gj-3-cr-details"), _cell(""), _cell("", editable=True, cell_id="ct-gj-3-cr-amount")],
            ],
        },
        {
            "heading": "Part B: Capital account extract after closing transfers",
            "headers": ["Debit", "Amount", "Credit", "Amount"],
            "rows": [
                [_cell("", editable=True, cell_id="ct-capital-dr1-details"), _cell("", editable=True, cell_id="ct-capital-dr1-amount"), _cell("", editable=True, cell_id="ct-capital-cr1-details"), _cell("", editable=True, cell_id="ct-capital-cr1-amount")],
                [_cell("", editable=True, cell_id="ct-capital-dr2-details"), _cell("", editable=True, cell_id="ct-capital-dr2-amount"), _cell("", editable=True, cell_id="ct-capital-cr2-details"), _cell("", editable=True, cell_id="ct-capital-cr2-amount")],
                [_cell("", editable=True, cell_id="ct-capital-dr3-details"), _cell("", editable=True, cell_id="ct-capital-dr3-amount"), _cell("", editable=True, cell_id="ct-capital-cr3-details"), _cell("", editable=True, cell_id="ct-capital-cr3-amount")],
                [_cell(""), _cell(""), _cell("", editable=True, cell_id="ct-capital-cr4-details"), _cell("", editable=True, cell_id="ct-capital-cr4-amount")],
            ],
        },
        {
            "heading": "Part C: Post-closing Trial Balance extract",
            "headers": ["Account", "Debit", "Credit"],
            "rows": [
                [_cell("Bank"), _cell("", editable=True, cell_id="ct-tb-bank-debit"), _cell("")],
                [_cell("Trading stock"), _cell("", editable=True, cell_id="ct-tb-stock-debit"), _cell("")],
                [_cell("Equipment"), _cell("", editable=True, cell_id="ct-tb-equipment-debit"), _cell("")],
                [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="ct-tb-capital-credit")],
                [_cell("Creditors control"), _cell(""), _cell("", editable=True, cell_id="ct-tb-creditors-credit")],
                [_cell("Loan"), _cell(""), _cell("", editable=True, cell_id="ct-tb-loan-credit")],
                [_cell("Total"), _cell("", editable=True, cell_id="ct-tb-total-debit"), _cell("", editable=True, cell_id="ct-tb-total-credit")],
            ],
        },
    ]
    closing_workflow_correct_map = {
        "ct-gj-1-dr-details": "Debtors' Allowances",
        "ct-gj-1-dr-amount": workflow_debtors_allow,
        "ct-gj-1-cr-details": "Sales",
        "ct-gj-1-cr-amount": workflow_debtors_allow,
        "ct-gj-2-dr-details": "Profit and Loss",
        "ct-gj-2-dr-amount": closing_workflow_scenario["net_profit"],
        "ct-gj-2-cr-details": "Capital",
        "ct-gj-2-cr-amount": closing_workflow_scenario["net_profit"],
        "ct-gj-3-dr-details": "Capital",
        "ct-gj-3-dr-amount": closing_workflow_scenario["drawings"],
        "ct-gj-3-cr-details": "Drawings",
        "ct-gj-3-cr-amount": closing_workflow_scenario["drawings"],
        "ct-capital-dr1-details": "Drawings",
        "ct-capital-dr1-amount": closing_workflow_scenario["drawings"],
        "ct-capital-cr1-details": "Balance b/d",
        "ct-capital-cr1-amount": workflow_opening_capital,
        "ct-capital-dr2-details": "Balance c/d",
        "ct-capital-dr2-amount": workflow_closing_capital,
        "ct-capital-cr2-details": "Profit and Loss",
        "ct-capital-cr2-amount": closing_workflow_scenario["net_profit"],
        "ct-capital-dr3-details": "Total",
        "ct-capital-dr3-amount": workflow_capital_total,
        "ct-capital-cr3-details": "Total",
        "ct-capital-cr3-amount": workflow_capital_total,
        "ct-capital-cr4-details": "Balance b/d",
        "ct-capital-cr4-amount": workflow_closing_capital,
        "ct-tb-bank-debit": closing_workflow_scenario["bank"],
        "ct-tb-stock-debit": closing_workflow_scenario["stock"],
        "ct-tb-equipment-debit": closing_workflow_scenario["equipment"],
        "ct-tb-capital-credit": workflow_closing_capital,
        "ct-tb-creditors-credit": closing_workflow_scenario["creditors"],
        "ct-tb-loan-credit": closing_workflow_scenario["loan"],
        "ct-tb-total-debit": workflow_postclosing_total,
        "ct-tb-total-credit": workflow_postclosing_total,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="final_account_table",
        prompt=f"Use the year-end information for {biz} to complete the closing-transfer workflow: (A) General Journal closing entries, (B) the Capital account extract after closing transfers, and (C) the Post-closing Trial Balance extract.",
        prompt_tables=closing_workflow_prompt_tables,
        tables=closing_workflow_tables,
        correct_map=closing_workflow_correct_map,
        derivation_map={
            "ct-capital-dr2-amount": f"Closing capital = Opening capital R{int(workflow_opening_capital):,} + Net profit R{int(closing_workflow_scenario['net_profit']):,} - Drawings R{int(closing_workflow_scenario['drawings']):,} = R{int(workflow_closing_capital):,}",
            "ct-tb-capital-credit": f"Carry the closing capital from Part B into the Post-closing Trial Balance: R{int(workflow_closing_capital):,}",
            "ct-tb-total-debit": f"Total debits = Bank R{int(closing_workflow_scenario['bank']):,} + Trading stock R{int(closing_workflow_scenario['stock']):,} + Equipment R{int(closing_workflow_scenario['equipment']):,} = R{int(workflow_postclosing_total):,}",
            "ct-tb-total-credit": f"Total credits = Capital R{int(workflow_closing_capital):,} + Creditors R{int(closing_workflow_scenario['creditors']):,} + Loan R{int(closing_workflow_scenario['loan']):,} = R{int(workflow_postclosing_total):,}",
        },
        cell_hints={
            "ct-gj-1-dr-details": "To close Debtors' Allowances, debit that account and credit Sales.",
            "ct-gj-2-dr-details": "Net profit is transferred out of Profit and Loss to Capital.",
            "ct-gj-3-dr-details": "Drawings are closed to Capital by debiting Capital and crediting Drawings.",
            "ct-capital-cr1-details": "The capital account starts with the opening balance brought down on the credit side.",
            "ct-capital-dr2-amount": "Balance c/d on the debit side of Capital is the closing capital after adding profit and deducting drawings.",
            "ct-tb-bank-debit": "Bank is an asset and therefore belongs on the debit side of the Post-closing Trial Balance.",
            "ct-tb-capital-credit": "Only real and personal accounts remain in the Post-closing Trial Balance, so carry the closing capital balance through here.",
            "ct-tb-creditors-credit": "Creditors control is a liability and belongs in the credit column.",
            "ct-tb-loan-credit": "Loan is a liability and belongs in the credit column.",
            "ct-tb-total-debit": "Add the asset balances on the debit side and check that the credit side agrees.",
            "ct-tb-total-credit": "The credit total must match the debit total once all permanent-account balances are placed correctly.",
        },
        cell_teaching_map={
            "ct-gj-1-dr-details": _teaching_hint(
                role_in_requirement="This cell records the debit side of the first closing-transfer journal entry.",
                evidence_from_question=f"The prompt says Debtors' Allowances of R{int(workflow_debtors_allow):,} must be closed as part of the year-end process.",
                rule_or_principle="To close Debtors' Allowances into Sales when determining net sales, debit Debtors' Allowances and credit Sales.",
                method_or_formula="Use Debtors' Allowances on the debit side and Sales on the credit side for the same amount.",
                record_link="This journal step reduces Sales to Net Sales before the final-account sections are prepared.",
                how_to_derive="Place Debtors' Allowances on the debit side of the journal entry and Sales on the credit side for the same amount.",
                transfer_tip="When a nominal account is being closed, think about which account must be cleared to zero and which summary account receives the transfer.",
            ),
            "ct-gj-2-dr-details": _teaching_hint(
                role_in_requirement="This cell identifies the account debited when net profit is transferred at year-end.",
                evidence_from_question=f"The closing information states that net profit has already been determined as R{int(closing_workflow_scenario['net_profit']):,}.",
                rule_or_principle="A net profit balance is transferred by debiting Profit and Loss and crediting Capital.",
                method_or_formula="Use Profit and Loss on the debit side because the profit is being transferred out of that nominal account.",
                record_link="This same net-profit figure then appears in the Capital account as an increase in owner's equity.",
                how_to_derive="Write Profit and Loss in the debit details cell for the closing-profit journal entry.",
                transfer_tip="When a completed nominal account is being closed, ask where its balance must be transferred next.",
            ),
            "ct-capital-dr2-amount": _teaching_hint(
                role_in_requirement="This cell gives the closing balance carried down in the Capital account.",
                evidence_from_question=f"Use Opening capital R{int(workflow_opening_capital):,}, Net profit R{int(closing_workflow_scenario['net_profit']):,}, and Drawings R{int(closing_workflow_scenario['drawings']):,} from the closing information table.",
                rule_or_principle="Closing capital = Opening capital + Net profit - Drawings.",
                method_or_formula="Add the credit-side increases to capital and deduct drawings to find the balance c/d.",
                record_link="This closing-capital balance then becomes both the Balance b/d in the next period and the Capital figure in the Post-closing Trial Balance.",
                how_to_derive=f"R{int(workflow_opening_capital):,} + R{int(closing_workflow_scenario['net_profit']):,} - R{int(closing_workflow_scenario['drawings']):,} = R{int(workflow_closing_capital):,}.",
                transfer_tip="In closing-transfer questions, finish the Capital account before attempting any later Balance Sheet or Trial Balance carry-through.",
            ),
            "ct-capital-cr1-details": _teaching_hint(
                role_in_requirement="This cell labels the opening balance in the Capital account.",
                evidence_from_question=f"The closing information table provides Opening capital of R{int(workflow_opening_capital):,}.",
                rule_or_principle="An opening balance carried into the new period is recorded as Balance b/d.",
                method_or_formula="Use the standard ledger wording for the opening balance line.",
                record_link="This opening-balance entry is the starting point before profit and drawings are posted.",
                how_to_derive="Write Balance b/d on the opening credit side of the Capital account.",
                transfer_tip="Ledger balance lines follow a standard pattern: opening balances appear as Balance b/d and closing balances as Balance c/d.",
            ),
            "ct-tb-capital-credit": _teaching_hint(
                role_in_requirement="This cell transfers the final capital balance into the Post-closing Trial Balance.",
                evidence_from_question="Part C depends on the closing balance you established in the Capital account in Part B.",
                rule_or_principle="After closing transfers, the Post-closing Trial Balance contains the final capital balance rather than the opening capital figure.",
                method_or_formula="Copy the finished closing-capital balance from the Capital account into the credit column.",
                record_link="This is the permanent-account figure that remains after drawings and profit transfers have updated owner's equity.",
                how_to_derive=f"Copy the closing capital from Part B: R{int(workflow_closing_capital):,}.",
                transfer_tip="Always check whether a later table should use an opening balance or an updated closing balance from an earlier part.",
            ),
            "ct-tb-total-debit": _teaching_hint(
                role_in_requirement="This cell totals the debit side of the Post-closing Trial Balance extract.",
                evidence_from_question=f"The remaining asset balances are Bank R{int(closing_workflow_scenario['bank']):,}, Trading stock R{int(closing_workflow_scenario['stock']):,}, and Equipment R{int(closing_workflow_scenario['equipment']):,}.",
                rule_or_principle="Only permanent asset balances appear on the debit side after closing transfers are complete.",
                method_or_formula="Add the three asset balances shown in Part C to produce the debit total.",
                record_link="The matching credit total checks that capital and liabilities were transferred correctly after the closing process.",
                how_to_derive=f"R{int(closing_workflow_scenario['bank']):,} + R{int(closing_workflow_scenario['stock']):,} + R{int(closing_workflow_scenario['equipment']):,} = R{int(workflow_postclosing_total):,}.",
                transfer_tip="Leave the total row until the end so it acts as a check on all earlier permanent-account placements.",
            ),
        },
        working_map={
            "ct-gj-1-dr-details": "Part A closes the nominal accounts first in the journal before anything is carried into the ledger-style sections.",
            "ct-capital-dr2-amount": "Part B updates Capital using opening capital, net profit, and drawings to find the final closing balance.",
            "ct-tb-capital-credit": "Part C must use the updated closing capital from Part B, not the opening capital from the prompt.",
            "ct-tb-total-credit": "The finished Post-closing Trial Balance is the final check that only permanent accounts remain after closing transfers.",
        },
        guidelines=[
            "Close nominal accounts in the journal before carrying balances into the Capital account and the Post-closing Trial Balance.",
            "Use the net profit and drawings figures to update Capital before preparing the Post-closing Trial Balance.",
            "Only permanent accounts should remain in the Post-closing Trial Balance extract.",
        ],
        marks=30,
    ), "closing_transfer_workflow_fill", expected_cells=33, cell_expectations=closing_workflow_correct_map))

    full_closing_scenarios = [
        {
            "sales": 420000,
            "debtors_allowances": 12000,
            "cost_of_sales": 250000,
            "other_income": 28000,
            "total_expenses": 124000,
            "drawings": 24000,
            "bank": 76000,
            "stock": 42000,
            "equipment": 180000,
            "creditors": 34000,
            "loan": 52000,
        },
        {
            "sales": 510000,
            "debtors_allowances": 15000,
            "cost_of_sales": 310000,
            "other_income": 36000,
            "total_expenses": 151000,
            "drawings": 28000,
            "bank": 88000,
            "stock": 50000,
            "equipment": 210000,
            "creditors": 42000,
            "loan": 64000,
        },
        {
            "sales": 360000,
            "debtors_allowances": 10000,
            "cost_of_sales": 214000,
            "other_income": 22000,
            "total_expenses": 98000,
            "drawings": 18000,
            "bank": 68000,
            "stock": 36000,
            "equipment": 156000,
            "creditors": 26000,
            "loan": 40000,
        },
    ]
    for scenario in full_closing_scenarios:
        net_sales = _round_money(float(scenario["sales"]) - float(scenario["debtors_allowances"]))
        gross_profit = _round_money(float(net_sales) - float(scenario["cost_of_sales"]))
        net_profit = _round_money(float(gross_profit) + float(scenario["other_income"]) - float(scenario["total_expenses"]))
        postclosing_total = _round_money(float(scenario["bank"]) + float(scenario["stock"]) + float(scenario["equipment"]))
        closing_capital = _round_money(float(postclosing_total) - float(scenario["creditors"]) - float(scenario["loan"]))
        opening_capital = _round_money(float(closing_capital) - float(net_profit) + float(scenario["drawings"]))
        capital_total = _round_money(float(opening_capital) + float(net_profit))

        full_prompt_tables = [
            {
                "heading": f"{biz} — Adjusted nominal balances before closing transfers",
                "headers": ["Account", "Amount"],
                "rows": [
                    [_cell("Sales"), _cell(scenario["sales"])],
                    [_cell("Debtors' Allowances"), _cell(scenario["debtors_allowances"])],
                    [_cell("Cost of Sales"), _cell(scenario["cost_of_sales"])],
                    [_cell("Other income total"), _cell(scenario["other_income"])],
                    [_cell("Total expenses"), _cell(scenario["total_expenses"])],
                    [_cell("Drawings"), _cell(scenario["drawings"])],
                ],
            },
            {
                "heading": "Balances remaining after nominal accounts are closed",
                "headers": ["Account", "Amount"],
                "rows": [
                    [_cell("Bank"), _cell(scenario["bank"])],
                    [_cell("Trading stock"), _cell(scenario["stock"])],
                    [_cell("Equipment"), _cell(scenario["equipment"])],
                    [_cell("Creditors control"), _cell(scenario["creditors"])],
                    [_cell("Loan"), _cell(scenario["loan"])],
                ],
            },
        ]
        full_tables = [
            {
                "heading": "Part A: General Journal closing entries",
                "headers": ["Date", "Details", "Debit", "Credit"],
                "rows": [
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-gj-1-dr-details"), _cell("", editable=True, cell_id="ctf-gj-1-dr-amount"), _cell("")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-gj-1-cr-details"), _cell(""), _cell("", editable=True, cell_id="ctf-gj-1-cr-amount")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-gj-2-dr-details"), _cell("", editable=True, cell_id="ctf-gj-2-dr-amount"), _cell("")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-gj-2-cr-details"), _cell(""), _cell("", editable=True, cell_id="ctf-gj-2-cr-amount")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-gj-3-dr-details"), _cell("", editable=True, cell_id="ctf-gj-3-dr-amount"), _cell("")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-gj-3-cr-details"), _cell(""), _cell("", editable=True, cell_id="ctf-gj-3-cr-amount")],
                ],
            },
            {
                "heading": "Part B: Trading Account extract after closing transfers",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Net Sales"), _cell("", editable=True, cell_id="ctf-tr-net-sales")],
                    [_cell("Cost of Sales"), _cell("", editable=True, cell_id="ctf-tr-cos")],
                    [_cell("Gross Profit"), _cell("", editable=True, cell_id="ctf-tr-gp")],
                ],
            },
            {
                "heading": "Part C: Profit and Loss Account extract after closing transfers",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Gross Profit"), _cell("", editable=True, cell_id="ctf-pl-gp")],
                    [_cell("Other income"), _cell("", editable=True, cell_id="ctf-pl-other-income")],
                    [_cell("Total expenses"), _cell("", editable=True, cell_id="ctf-pl-expenses")],
                    [_cell("Net Profit"), _cell("", editable=True, cell_id="ctf-pl-net-profit")],
                ],
            },
            {
                "heading": "Part D: Drawings account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell("1 Mar 2025"), _cell("Balance b/d"), _cell("Balance"), _cell(scenario["drawings"]), _cell("")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-dr-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="ctf-dr-cr-amount")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-dr-total-details"), _cell(""), _cell("", editable=True, cell_id="ctf-dr-total-debit"), _cell("", editable=True, cell_id="ctf-dr-total-credit")],
                ],
            },
            {
                "heading": "Part E: Capital account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell("1 Mar 2025"), _cell("", editable=True, cell_id="ctf-cap-open-details"), _cell("Balance"), _cell(""), _cell("", editable=True, cell_id="ctf-cap-open-credit")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-cap-profit-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="ctf-cap-profit-credit")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-cap-draw-details"), _cell("GJ"), _cell("", editable=True, cell_id="ctf-cap-draw-debit"), _cell("")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-cap-bal-details"), _cell(""), _cell("", editable=True, cell_id="ctf-cap-bal-debit"), _cell("")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="ctf-cap-total-details"), _cell(""), _cell("", editable=True, cell_id="ctf-cap-total-debit"), _cell("", editable=True, cell_id="ctf-cap-total-credit")],
                    [_cell("1 Mar 2026"), _cell("", editable=True, cell_id="ctf-cap-bd-details"), _cell("Balance"), _cell(""), _cell("", editable=True, cell_id="ctf-cap-bd-credit")],
                ],
            },
            {
                "heading": "Part F: Post-closing Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="ctf-tb-bank-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="ctf-tb-stock-debit"), _cell("")],
                    [_cell("Equipment"), _cell("", editable=True, cell_id="ctf-tb-equipment-debit"), _cell("")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="ctf-tb-capital-credit")],
                    [_cell("Creditors control"), _cell(""), _cell("", editable=True, cell_id="ctf-tb-creditors-credit")],
                    [_cell("Loan"), _cell(""), _cell("", editable=True, cell_id="ctf-tb-loan-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="ctf-tb-total-debit"), _cell("", editable=True, cell_id="ctf-tb-total-credit")],
                ],
            },
        ]

        full_correct_map = {
            "ctf-gj-1-dr-details": "Debtors' Allowances",
            "ctf-gj-1-dr-amount": scenario["debtors_allowances"],
            "ctf-gj-1-cr-details": "Sales",
            "ctf-gj-1-cr-amount": scenario["debtors_allowances"],
            "ctf-gj-2-dr-details": "Profit and Loss",
            "ctf-gj-2-dr-amount": net_profit,
            "ctf-gj-2-cr-details": "Capital",
            "ctf-gj-2-cr-amount": net_profit,
            "ctf-gj-3-dr-details": "Capital",
            "ctf-gj-3-dr-amount": scenario["drawings"],
            "ctf-gj-3-cr-details": "Drawings",
            "ctf-gj-3-cr-amount": scenario["drawings"],
            "ctf-tr-net-sales": net_sales,
            "ctf-tr-cos": scenario["cost_of_sales"],
            "ctf-tr-gp": gross_profit,
            "ctf-pl-gp": gross_profit,
            "ctf-pl-other-income": scenario["other_income"],
            "ctf-pl-expenses": scenario["total_expenses"],
            "ctf-pl-net-profit": net_profit,
            "ctf-dr-cr-details": "Capital",
            "ctf-dr-cr-amount": scenario["drawings"],
            "ctf-dr-total-details": "Total",
            "ctf-dr-total-debit": scenario["drawings"],
            "ctf-dr-total-credit": scenario["drawings"],
            "ctf-cap-open-details": "Balance b/d",
            "ctf-cap-open-credit": opening_capital,
            "ctf-cap-profit-details": "Profit and Loss",
            "ctf-cap-profit-credit": net_profit,
            "ctf-cap-draw-details": "Drawings",
            "ctf-cap-draw-debit": scenario["drawings"],
            "ctf-cap-bal-details": "Balance c/d",
            "ctf-cap-bal-debit": closing_capital,
            "ctf-cap-total-details": "Total",
            "ctf-cap-total-debit": capital_total,
            "ctf-cap-total-credit": capital_total,
            "ctf-cap-bd-details": "Balance b/d",
            "ctf-cap-bd-credit": closing_capital,
            "ctf-tb-bank-debit": scenario["bank"],
            "ctf-tb-stock-debit": scenario["stock"],
            "ctf-tb-equipment-debit": scenario["equipment"],
            "ctf-tb-capital-credit": closing_capital,
            "ctf-tb-creditors-credit": scenario["creditors"],
            "ctf-tb-loan-credit": scenario["loan"],
            "ctf-tb-total-debit": postclosing_total,
            "ctf-tb-total-credit": postclosing_total,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the year-end balances for {biz} to complete the full closing-transfer project: (A) prepare the key General Journal closing entries, (B) complete the Trading Account extract, (C) complete the Profit and Loss Account extract, (D) close the Drawings account, (E) update and balance the Capital account, and (F) complete the Post-closing Trial Balance extract.",
            prompt_tables=full_prompt_tables,
            tables=full_tables,
            correct_map=full_correct_map,
            derivation_map={
                "ctf-tr-net-sales": f"Net Sales = R{int(scenario['sales']):,} - R{int(scenario['debtors_allowances']):,} = R{int(net_sales):,}.",
                "ctf-tr-gp": f"Gross Profit = R{int(net_sales):,} - R{int(scenario['cost_of_sales']):,} = R{int(gross_profit):,}.",
                "ctf-pl-net-profit": f"Net Profit = Gross Profit R{int(gross_profit):,} + Other income R{int(scenario['other_income']):,} - Total expenses R{int(scenario['total_expenses']):,} = R{int(net_profit):,}.",
                "ctf-cap-open-credit": f"Opening capital = Closing capital R{int(closing_capital):,} - Net profit R{int(net_profit):,} + Drawings R{int(scenario['drawings']):,} = R{int(opening_capital):,}.",
                "ctf-cap-bal-debit": f"Closing capital = Opening capital R{int(opening_capital):,} + Net profit R{int(net_profit):,} - Drawings R{int(scenario['drawings']):,} = R{int(closing_capital):,}.",
                "ctf-tb-total-debit": f"Total debits = Bank R{int(scenario['bank']):,} + Trading stock R{int(scenario['stock']):,} + Equipment R{int(scenario['equipment']):,} = R{int(postclosing_total):,}.",
            },
            cell_hints={
                "ctf-gj-2-dr-details": "A net profit balance is transferred out of Profit and Loss to Capital at year-end.",
                "ctf-tr-gp": "Gross Profit comes from Net Sales minus Cost of Sales.",
                "ctf-pl-net-profit": "Net Profit = Gross Profit + Other income - Total expenses.",
                "ctf-dr-cr-details": "Drawings are closed by transferring the balance to Capital.",
                "ctf-cap-open-credit": "Use the closing capital and reverse the capital formula to solve for opening capital.",
                "ctf-tb-capital-credit": "Use the closing capital from the Capital account, not the opening balance.",
            },
            cell_teaching_map={
                "ctf-gj-2-dr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the account debited when the year's net profit is closed off.",
                    evidence_from_question=f"The completed Profit and Loss Account section shows a net profit of R{int(net_profit):,}.",
                    rule_or_principle="A net profit balance is transferred by debiting Profit and Loss and crediting Capital.",
                    method_or_formula="Use Profit and Loss on the debit side because the profit must be transferred out of that account into Capital.",
                    record_link="The same net-profit figure is then posted into the Capital account and affects the Post-closing Trial Balance.",
                    how_to_derive="Use Profit and Loss on the debit side because the profit must be transferred out of that account into Capital.",
                    transfer_tip="When a nominal account has been fully balanced and shows profit, the closing transfer moves that profit into owner's equity.",
                ),
                "ctf-tr-gp": _teaching_hint(
                    role_in_requirement="This cell shows the gross profit created in the Trading Account before any other income or expenses are considered.",
                    evidence_from_question=f"Net Sales are R{int(net_sales):,} after deducting Debtors' Allowances, and Cost of Sales is R{int(scenario['cost_of_sales']):,}.",
                    rule_or_principle="Gross Profit = Net Sales - Cost of Sales.",
                    method_or_formula="Subtract Cost of Sales from Net Sales after the Trading Account section has been completed.",
                    record_link="This Gross Profit is then carried directly into the Profit and Loss section.",
                    how_to_derive=f"R{int(net_sales):,} - R{int(scenario['cost_of_sales']):,} = R{int(gross_profit):,}.",
                    transfer_tip="The Trading Account is completed before the Profit and Loss Account because Gross Profit is carried forward into the next section.",
                ),
                "ctf-pl-net-profit": _teaching_hint(
                    role_in_requirement="This cell gives the final net profit that will be closed to Capital.",
                    evidence_from_question=f"Gross Profit is R{int(gross_profit):,}, Other income is R{int(scenario['other_income']):,}, and Total expenses are R{int(scenario['total_expenses']):,}.",
                    rule_or_principle="Net Profit = Gross Profit + Other income - Total expenses.",
                    method_or_formula="Add Gross Profit and Other income, then deduct Total expenses.",
                    record_link="This result is then used in the closing journal and the Capital account update.",
                    how_to_derive=f"R{int(gross_profit):,} + R{int(scenario['other_income']):,} - R{int(scenario['total_expenses']):,} = R{int(net_profit):,}.",
                    transfer_tip="Once net profit is known, that same figure drives the closing-transfer journal and the Capital account update.",
                ),
                "ctf-dr-cr-details": _teaching_hint(
                    role_in_requirement="This cell records where the Drawings account is closed at year-end.",
                    evidence_from_question=f"The Drawings account has a balance b/d of R{int(scenario['drawings']):,} that must be closed off.",
                    rule_or_principle="Drawings are closed to Capital, so Drawings is credited and Capital is debited for the same amount.",
                    how_to_derive="Write Capital in the details column for the credit side of the Drawings account.",
                    transfer_tip="Ask which owner's-equity account must absorb the drawings balance once the temporary drawings account is cleared.",
                ),
                "ctf-cap-open-credit": _teaching_hint(
                    role_in_requirement="This cell places the opening capital balance into the Capital account before year-end transfers are processed.",
                    evidence_from_question="The question gives the year-end permanent-account balances and the net profit/drawings figures, so the opening capital must be deduced as the missing starting balance.",
                    rule_or_principle="Opening capital = Closing capital - Net profit + Drawings when there is no additional capital introduced.",
                    how_to_derive=f"R{int(closing_capital):,} - R{int(net_profit):,} + R{int(scenario['drawings']):,} = R{int(opening_capital):,}.",
                    transfer_tip="When a final capital figure is implied by the Post-closing Trial Balance, you can reverse the capital formula to reconstruct the opening balance.",
                ),
                "ctf-tb-capital-credit": _teaching_hint(
                    role_in_requirement="This cell carries the finished closing capital into the Post-closing Trial Balance.",
                    evidence_from_question="The Capital account in Part E has already been updated for net profit and drawings.",
                    rule_or_principle="The Post-closing Trial Balance must show the closing capital balance, not the opening balance and not a nominal account figure.",
                    method_or_formula="Copy the closing balance from the updated Capital account into the credit column of the Post-closing Trial Balance.",
                    record_link="This is the permanent-equity figure that remains after all year-end transfers are complete.",
                    how_to_derive=f"Copy the closing capital from Part E: R{int(closing_capital):,}.",
                    transfer_tip="Later tables in a workflow usually depend on the updated balance from the previous step, so transfer figures forward carefully.",
                ),
            },
            working_map={
                "ctf-tr-gp": "Complete the workflow in order: Trading Account first, then Profit and Loss, then the closing journal and ledger-style sections.",
                "ctf-pl-net-profit": "The Net Profit figure is a carry-through value: it closes Profit and Loss and then updates Capital.",
                "ctf-cap-bal-debit": "Part E uses opening capital, profit, and drawings to produce the final closing capital balance.",
                "ctf-tb-capital-credit": "Part F must use the updated capital from Part E, not any earlier capital figure in the scenario.",
            },
            guidelines=[
                "Close Debtors' Allowances to Sales first so that Net Sales is available for the Trading Account.",
                "Complete Trading Account before Profit and Loss, and complete Profit and Loss before updating Capital.",
                "Close Drawings to Capital, then use the updated closing capital in the Post-closing Trial Balance.",
                "Only permanent accounts remain in the Post-closing Trial Balance.",
            ],
            marks=38,
        ), "closing_transfer_full_project_fill", expected_cells=43, cell_expectations=full_correct_map))

    return pool


def _gen_depreciation(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    biz = _pick_business_name(r=r)

    pool.append(_make_mcq(
        prompt="What is the difference between 'depreciation' and 'accumulated depreciation'?",
        options=[
            "They are the same thing.",
            "Depreciation is the current year's amount; accumulated depreciation includes this year plus all prior years.",
            "Depreciation is for vehicles only; accumulated depreciation is for equipment only.",
            "Depreciation increases asset value; accumulated depreciation decreases it.",
        ],
        correct_index=1,
        explanation="Depreciation = current year write-off. Accumulated depreciation = total write-off from purchase date to now (current year + all previous years).",
    ))

    pool.append(_make_mcq(
        prompt="What is the double entry for writing off depreciation?",
        options=[
            "Dr. Bank, Cr. Equipment.",
            "Dr. Depreciation (expense), Cr. Accumulated depreciation on asset.",
            "Dr. Accumulated depreciation, Cr. Capital.",
            "Dr. Trading stock, Cr. Depreciation.",
        ],
        correct_index=1,
        explanation="Dr. Depreciation (expense) / Cr. Accumulated depreciation on vehicles/equipment. Depreciation is an expense; accumulated depreciation is a contra-asset.",
    ))

    pool.append(_make_mcq(
        prompt="Which GAAP concept requires that depreciation be written off each year?",
        options=[
            "The going concern concept.",
            "The matching concept (expenses matched to the period).",
            "The prudence concept.",
            "The business entity concept.",
        ],
        correct_index=1,
        explanation="The matching concept requires that the cost of using an asset is allocated to the accounting period in which it is used.",
    ))

    pool.append(_make_mcq(
        prompt="Which method calculates depreciation on the carrying value of the asset each year?",
        options=[
            "Straight-line method",
            "Diminishing-balance method",
            "FIFO method",
            "Current account method",
        ],
        correct_index=1,
        explanation="The diminishing-balance method calculates depreciation on the carrying value remaining at the start of each year.",
    ))

    pool.append(_make_mcq(
        prompt="If an asset is bought during the year, what must be considered when calculating annual depreciation?",
        options=[
            "Only the folio number",
            "The number of months the asset was owned",
            "The owner's drawings",
            "The stock count",
        ],
        correct_index=1,
        explanation="Part-year depreciation must be calculated for the months that the asset was owned during the financial year.",
    ))

    eq_cost = r.choice([10000, 15000, 20000, 24000, 30000, 50000])
    sl_pct = r.choice([10, 15, 20, 25])
    sl_depr = _round_money(eq_cost * sl_pct / 100)
    pool.append(_with_validation(_make_calc(
        prompt=f"{biz} purchased equipment for R{eq_cost:,}. Depreciation is written off at {sl_pct}% per annum on the straight-line method.\n\nCalculate the annual depreciation.",
        correct_answer=sl_depr,
        working_formula=f"{sl_pct}% × R{eq_cost:,} = R{sl_depr:,.2f}",
        formula_hint=f"Annual depreciation = {sl_pct}% × cost price",
    ), "depreciation_straight_line", cost=eq_cost, percentage=sl_pct))

    veh_cost = r.choice([80000, 100000, 120000, 150000, 200000])
    db_pct = r.choice([15, 20, 25])
    months_owned = r.choice([6, 9, 12])
    yr1_depr = _round_money(veh_cost * db_pct / 100 * months_owned / 12)
    carrying_after_yr1 = _round_money(veh_cost - yr1_depr)
    yr2_depr = _round_money(carrying_after_yr1 * db_pct / 100)
    carrying_after_yr2 = _round_money(carrying_after_yr1 - yr2_depr)

    pool.append(_with_validation(_make_calc(
        prompt=f"{biz} purchased a vehicle for R{veh_cost:,}. Depreciation at {db_pct}% on diminishing (book) balance. The vehicle was owned for {months_owned} months in Year 1.\n\nCalculate Year 1 depreciation.",
        correct_answer=yr1_depr,
        working_formula=f"{db_pct}% × R{veh_cost:,} × {months_owned}/12",
        formula_hint=f"Year 1 depreciation = {db_pct}% × cost × {months_owned}/12",
    ), "depreciation_diminishing_partial", cost=veh_cost, percentage=db_pct, months=months_owned))

    pool.append(_with_validation(_make_calc(
        prompt=f"Using the vehicle above (cost R{veh_cost:,}, {db_pct}% diminishing balance, Year 1 depreciation R{yr1_depr:,.2f}), calculate the carrying value at the end of Year 2.",
        correct_answer=carrying_after_yr2,
        working_formula=f"Carrying value = R{carrying_after_yr1:,.2f} - ({db_pct}% × R{carrying_after_yr1:,.2f}) = R{carrying_after_yr2:,.2f}",
        formula_hint="Year 2 carrying value = carrying value after Year 1 - Year 2 depreciation",
    ), "depreciation_carrying_year2", cost=veh_cost, percentage=db_pct, months=months_owned))

    comp_cost = r.choice([8000, 10000, 12000, 15000])
    comp_sl_pct = 20
    comp_yr1 = _round_money(comp_cost * comp_sl_pct / 100)
    comp_accum_yr3 = _round_money(comp_yr1 * 3)
    comp_cv_yr3 = _round_money(comp_cost - comp_accum_yr3)

    pool.append(_with_validation(_make_calc(
        prompt=f"{biz} purchased a computer for R{comp_cost:,} on 1 January. Depreciation at {comp_sl_pct}% on cost price (straight-line).\n\nWhat is the carrying value at the end of Year 3?",
        correct_answer=comp_cv_yr3,
        working_formula=f"CV = Cost - Accumulated = R{comp_cost:,} - (R{comp_yr1:,.2f} × 3) = R{comp_cv_yr3:,.2f}",
        formula_hint="Carrying value = Cost - Accumulated depreciation",
    ), "asset_register_carrying_year3", cost=comp_cost, percentage=comp_sl_pct, years=3))

    dep_core_asset_label = r.choice(["equipment", "vehicles", "machinery"])
    dep_core_cost = r.choice([48000, 60000, 72000, 90000])
    dep_core_rate = r.choice([10, 15, 20])
    dep_core_prior_years = r.choice([1, 2, 3])
    dep_core_current_year = _round_money(dep_core_cost * dep_core_rate / 100)
    dep_core_opening_accum = _round_money(dep_core_current_year * dep_core_prior_years)
    dep_core_closing_accum = _round_money(dep_core_opening_accum + dep_core_current_year)
    dep_core_carrying_value = _round_money(dep_core_cost - dep_core_closing_accum)
    dep_core_prompt_tables = [
        {
            "heading": "Asset information",
            "headers": ["Item", "Amount / Detail"],
            "rows": [
                [_cell(f"{str(dep_core_asset_label).capitalize()} at cost"), _cell(dep_core_cost)],
                [_cell("Depreciation method"), _cell("Straight-line on cost price")],
                [_cell("Annual depreciation rate"), _cell(f"{dep_core_rate}%")],
                [_cell("Accumulated depreciation on 1 March 2025"), _cell(dep_core_opening_accum)],
            ],
        },
    ]
    dep_core_tables = [
        {
            "heading": "Part A: Year-end depreciation summary",
            "headers": ["Description", "Amount"],
            "rows": [
                [_cell("Depreciation for the current year"), _cell("", editable=True, cell_id="dep-core-current")],
                [_cell("Accumulated depreciation at year-end"), _cell("", editable=True, cell_id="dep-core-closing-accum")],
                [_cell("Carrying value at year-end"), _cell("", editable=True, cell_id="dep-core-carrying")],
            ],
        },
        {
            "heading": "Part B: Distinguish the terms",
            "headers": ["Term", "Meaning"],
            "rows": [
                [_cell("Depreciation"), _cell("", editable=True, cell_id="dep-core-depreciation-meaning")],
                [_cell("Accumulated depreciation"), _cell("", editable=True, cell_id="dep-core-accum-meaning")],
            ],
        },
    ]
    dep_core_correct_map = {
        "dep-core-current": dep_core_current_year,
        "dep-core-closing-accum": dep_core_closing_accum,
        "dep-core-carrying": dep_core_carrying_value,
        "dep-core-depreciation-meaning": "Current-year write-off",
        "dep-core-accum-meaning": "Total write-off to date",
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="final_account_table",
        prompt=f"Use the information for {biz} to complete the depreciation-core summary: (A) calculate the current-year depreciation, closing accumulated depreciation, and carrying value for the {dep_core_asset_label}; and (B) distinguish between depreciation and accumulated depreciation.",
        prompt_tables=dep_core_prompt_tables,
        tables=dep_core_tables,
        correct_map=dep_core_correct_map,
        derivation_map={
            "dep-core-current": f"Current-year depreciation = R{int(dep_core_cost):,} × {dep_core_rate}% = R{int(dep_core_current_year):,}",
            "dep-core-closing-accum": f"Closing accumulated depreciation = Opening accumulated depreciation R{int(dep_core_opening_accum):,} + current-year depreciation R{int(dep_core_current_year):,} = R{int(dep_core_closing_accum):,}",
            "dep-core-carrying": f"Carrying value = Cost R{int(dep_core_cost):,} - closing accumulated depreciation R{int(dep_core_closing_accum):,} = R{int(dep_core_carrying_value):,}",
        },
        cell_hints={
            "dep-core-current": "Straight-line depreciation is calculated on cost price.",
            "dep-core-closing-accum": "Add the current year's depreciation to the opening accumulated depreciation balance.",
            "dep-core-carrying": "Carrying value equals cost minus accumulated depreciation.",
            "dep-core-depreciation-meaning": "This term refers to the amount written off for the current financial year.",
            "dep-core-accum-meaning": "This term refers to the total depreciation charged since the asset was bought.",
        },
        cell_teaching_map={
            "dep-core-current": _teaching_hint(
                role_in_requirement="This cell calculates the depreciation expense for the current year.",
                evidence_from_question=f"The asset cost is R{int(dep_core_cost):,} and the straight-line rate is {dep_core_rate}% per year.",
                rule_or_principle="Straight-line depreciation is calculated on original cost each year.",
                how_to_derive=f"R{int(dep_core_cost):,} × {dep_core_rate}% = R{int(dep_core_current_year):,}.",
                transfer_tip="For straight-line questions, the same annual depreciation amount repeats each full year unless the rate or cost changes.",
            ),
            "dep-core-closing-accum": _teaching_hint(
                role_in_requirement="This cell updates accumulated depreciation to the year-end balance.",
                evidence_from_question=f"The opening accumulated depreciation is R{int(dep_core_opening_accum):,} and the current-year depreciation is R{int(dep_core_current_year):,}.",
                rule_or_principle="Accumulated depreciation is the total depreciation charged from purchase date to the reporting date.",
                how_to_derive=f"R{int(dep_core_opening_accum):,} + R{int(dep_core_current_year):,} = R{int(dep_core_closing_accum):,}.",
                transfer_tip="Always separate the current year's depreciation from the running accumulated balance, then add them together for year-end.",
            ),
            "dep-core-carrying": _teaching_hint(
                role_in_requirement="This cell gives the carrying value of the asset at year-end.",
                evidence_from_question=f"The asset remains at cost R{int(dep_core_cost):,} and the updated accumulated depreciation is R{int(dep_core_closing_accum):,}.",
                rule_or_principle="Carrying value = cost price - accumulated depreciation.",
                how_to_derive=f"R{int(dep_core_cost):,} - R{int(dep_core_closing_accum):,} = R{int(dep_core_carrying_value):,}.",
                transfer_tip="Do not subtract only the current year's depreciation when the question asks for carrying value at year-end; use total accumulated depreciation to date.",
            ),
        },
        guidelines=[
            "Calculate straight-line depreciation on cost price.",
            "Update accumulated depreciation by adding the current year's charge to the opening accumulated balance.",
            "Carrying value is cost less accumulated depreciation, and accumulated depreciation is the total write-off to date.",
        ],
        marks=12,
    ), "depreciation_core_summary_fill", expected_cells=5, cell_expectations=dep_core_correct_map))

    dep_cost = r.choice([18000, 24000, 30000, 36000])
    dep_pct = r.choice([10, 15, 20])
    dep_amount = _round_money(dep_cost * dep_pct / 100)
    ledger_prompt_table = {
        "heading": "General Journal entry to be posted",
        "headers": ["Date", "Details", "Debit", "Credit"],
        "rows": [
            [_cell("28 Feb 2026"), _cell("Depreciation"), _cell(dep_amount), _cell("")],
            [_cell("28 Feb 2026"), _cell("Accumulated depreciation on equipment"), _cell(""), _cell(dep_amount)],
        ],
    }
    ledger_tables = [
        {
            "heading": "Depreciation account",
            "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
            "rows": [
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="dep-ledger-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="dep-ledger-dr-amount"), _cell("")],
            ],
        },
        {
            "heading": "Accumulated depreciation on equipment account",
            "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
            "rows": [
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="dep-ledger-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="dep-ledger-cr-amount")],
            ],
        },
    ]
    ledger_correct_map = {
        "dep-ledger-dr-details": "Accumulated depreciation on equipment",
        "dep-ledger-dr-amount": dep_amount,
        "dep-ledger-cr-details": "Depreciation",
        "dep-ledger-cr-amount": dep_amount,
    }
    ledger_derivation_map = {
        "dep-ledger-dr-amount": f"R{dep_cost:,} × {dep_pct}% = R{dep_amount:,}",
        "dep-ledger-cr-amount": f"The credit entry uses the same depreciation amount: R{dep_amount:,}",
    }
    ledger_cell_hints = {
        "dep-ledger-dr-details": "Use the opposite account name in the details column.",
        "dep-ledger-dr-amount": "Calculate the depreciation amount first from cost × rate.",
        "dep-ledger-cr-details": "This details entry is the account on the other side of the journal.",
        "dep-ledger-cr-amount": "The two amounts in this posting must be equal.",
    }
    ledger_cell_teaching_map = {
        "dep-ledger-dr-details": _teaching_hint(
            role_in_requirement="This cell identifies the source account for the debit posting.",
            evidence_from_question="Read the prepared General Journal entry shown above the ledger.",
            rule_or_principle="In ledger posting, the details column shows the opposite account.",
            how_to_derive="Look at the credit side of the journal entry and copy that account name as the details entry.",
            transfer_tip="When posting from a journal to the ledger, ask: which account is on the other side of this entry?",
        ),
        "dep-ledger-dr-amount": _teaching_hint(
            role_in_requirement="This cell records the depreciation expense amount for the year.",
            evidence_from_question="Use the cost and rate given in the prompt.",
            rule_or_principle="Straight-line depreciation = cost price × rate.",
            how_to_derive=f"R{dep_cost:,} × {dep_pct}% = R{dep_amount:,}",
            transfer_tip="Once you calculate the amount, it is used on both sides of the double entry.",
        ),
        "dep-ledger-cr-details": _teaching_hint(
            role_in_requirement="This cell identifies the opposite account in the accumulated-depreciation ledger posting.",
            evidence_from_question="The prepared journal entry shows Depreciation debited and Accumulated depreciation on equipment credited.",
            rule_or_principle="The details column in a ledger account records the account on the other side of the journal entry.",
            method_or_formula="Because accumulated depreciation is credited against Depreciation, use Depreciation in the details column.",
            record_link="This ledger posting must agree exactly with the prepared General Journal entry above it.",
            how_to_derive="Look at the debit side of the journal and copy Depreciation as the details entry in the credited ledger account.",
            transfer_tip="For ledger details, do not repeat the same account name as the heading; write the opposing account instead.",
        ),
        "dep-ledger-cr-amount": _teaching_hint(
            role_in_requirement="This cell records the credited accumulated-depreciation amount.",
            evidence_from_question=f"The annual depreciation calculated from the cost and rate is R{dep_amount:,}.",
            rule_or_principle="Both sides of the depreciation double entry use the same amount.",
            method_or_formula=f"Credit the accumulated-depreciation account with R{dep_amount:,}.",
            record_link="This same amount is the one debited to Depreciation and later affects carrying value / accumulated-depreciation totals.",
            how_to_derive=f"Use the same calculated depreciation amount R{dep_amount:,} on the credit side.",
            transfer_tip="Once the depreciation amount is calculated, transfer it unchanged to both accounts in the double entry.",
        ),
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="ledger",
        prompt=f"{biz} bought equipment for R{dep_cost:,}. Depreciation must be written off at {dep_pct}% per annum. The journal entry has already been prepared below. Post the entry to the relevant General Ledger accounts.",
        prompt_table=ledger_prompt_table,
        tables=ledger_tables,
        correct_map=ledger_correct_map,
        derivation_map=ledger_derivation_map,
        cell_hints=ledger_cell_hints,
        cell_teaching_map=ledger_cell_teaching_map,
        working_map={
            "dep-ledger-dr-details": "The Depreciation account uses the credited accumulated-depreciation account as its details entry.",
            "dep-ledger-cr-details": "The accumulated-depreciation account uses Depreciation as the opposite account in the details column.",
            "dep-ledger-cr-amount": "The same calculated depreciation amount is posted unchanged on the credit side of accumulated depreciation.",
        },
        guidelines=["Post the debit entry to the Depreciation account.", "Post the credit entry to the Accumulated depreciation on equipment account.", "Use the account name on the opposite side as the details entry."],
        marks=8,
    ), "depreciation_ledger_fill", expected_cells=4, amount=dep_amount))

    ledger_asset_label = r.choice(["equipment", "vehicles", "machinery"])
    ledger_accum_label = f"Accumulated depreciation on {ledger_asset_label}"
    ledger_opening_accum = r.choice([18000, 24000, 30000, 36000])
    ledger_workflow_amount = r.choice([12000, 15000, 18000, 21000])
    ledger_closing_accum = _round_money(ledger_opening_accum + ledger_workflow_amount)
    ledger_workflow_prompt_tables = [
        {
            "heading": "General Journal entries to post",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell("28 Feb 2026"), _cell("Depreciation"), _cell(ledger_workflow_amount), _cell("")],
                [_cell("28 Feb 2026"), _cell(ledger_accum_label), _cell(""), _cell(ledger_workflow_amount)],
                [_cell("28 Feb 2026"), _cell("Profit and Loss"), _cell(ledger_workflow_amount), _cell("")],
                [_cell("28 Feb 2026"), _cell("Depreciation"), _cell(""), _cell(ledger_workflow_amount)],
            ],
        },
        {
            "heading": "Opening balance information",
            "headers": ["Account", "Balance on 1 Mar 2025"],
            "rows": [
                [_cell(ledger_accum_label), _cell(ledger_opening_accum)],
            ],
        },
    ]
    ledger_workflow_tables = [
        {
            "heading": "Depreciation account",
            "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
            "rows": [
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="depwf-dep-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="depwf-dep-dr-amount"), _cell("")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="depwf-dep-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="depwf-dep-cr-amount")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="depwf-dep-total-details"), _cell(""), _cell("", editable=True, cell_id="depwf-dep-total-debit"), _cell("", editable=True, cell_id="depwf-dep-total-credit")],
            ],
        },
        {
            "heading": f"{ledger_accum_label.capitalize()} account",
            "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
            "rows": [
                [_cell("1 Mar 2025"), _cell("", editable=True, cell_id="depwf-acc-open-details"), _cell("Balance"), _cell(""), _cell("", editable=True, cell_id="depwf-acc-open-amount")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="depwf-acc-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="depwf-acc-cr-amount")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="depwf-acc-bal-details"), _cell(""), _cell("", editable=True, cell_id="depwf-acc-bal-amount"), _cell("")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="depwf-acc-total-details"), _cell(""), _cell("", editable=True, cell_id="depwf-acc-total-debit"), _cell("", editable=True, cell_id="depwf-acc-total-credit")],
                [_cell("1 Mar 2026"), _cell("", editable=True, cell_id="depwf-acc-bd-details"), _cell("Balance"), _cell(""), _cell("", editable=True, cell_id="depwf-acc-bd-amount")],
            ],
        },
    ]
    ledger_workflow_correct_map = {
        "depwf-dep-dr-details": ledger_accum_label,
        "depwf-dep-dr-amount": ledger_workflow_amount,
        "depwf-dep-cr-details": "Profit and Loss",
        "depwf-dep-cr-amount": ledger_workflow_amount,
        "depwf-dep-total-details": "Total",
        "depwf-dep-total-debit": ledger_workflow_amount,
        "depwf-dep-total-credit": ledger_workflow_amount,
        "depwf-acc-open-details": "Balance b/d",
        "depwf-acc-open-amount": ledger_opening_accum,
        "depwf-acc-cr-details": "Depreciation",
        "depwf-acc-cr-amount": ledger_workflow_amount,
        "depwf-acc-bal-details": "Balance c/d",
        "depwf-acc-bal-amount": ledger_closing_accum,
        "depwf-acc-total-details": "Total",
        "depwf-acc-total-debit": ledger_closing_accum,
        "depwf-acc-total-credit": ledger_closing_accum,
        "depwf-acc-bd-details": "Balance b/d",
        "depwf-acc-bd-amount": ledger_closing_accum,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="ledger",
        prompt=f"Use the journal entries and opening balance for {biz} to post the depreciation workflow to the General Ledger: (A) post and close the Depreciation account, and (B) update and balance the {ledger_accum_label} account.",
        prompt_tables=ledger_workflow_prompt_tables,
        tables=ledger_workflow_tables,
        correct_map=ledger_workflow_correct_map,
        derivation_map={
            "depwf-acc-bal-amount": f"Closing accumulated depreciation = Opening balance R{int(ledger_opening_accum):,} + current-year depreciation R{int(ledger_workflow_amount):,} = R{int(ledger_closing_accum):,}",
            "depwf-acc-total-debit": f"The debit side needs Balance c/d of R{int(ledger_closing_accum):,} to balance the credit entries.",
            "depwf-acc-bd-amount": f"The next period's Balance b/d equals the previous period's Balance c/d: R{int(ledger_closing_accum):,}",
        },
        cell_hints={
            "depwf-dep-dr-details": "For each ledger entry, the details column shows the account on the opposite side of the journal entry.",
            "depwf-dep-cr-details": "The depreciation expense is closed to Profit and Loss at year-end.",
            "depwf-acc-bal-amount": "Add the opening accumulated depreciation balance and the current-year depreciation to get the balance c/d.",
            "depwf-acc-bd-amount": "Balance b/d on 1 March is the same amount as the previous day's balance c/d.",
        },
        cell_teaching_map={
            "depwf-dep-dr-details": _teaching_hint(
                role_in_requirement="This cell names the opposite account for the debit posting in the Depreciation account.",
                evidence_from_question="The first journal entry debits Depreciation and credits the accumulated depreciation account.",
                rule_or_principle="In ledger posting, the details column contains the account on the other side of the journal entry.",
                how_to_derive=f"Because Depreciation is debited against {ledger_accum_label}, write {ledger_accum_label} in the details column.",
                transfer_tip="When you are unsure about a ledger details entry, look back to the opposite side of the source journal line.",
            ),
            "depwf-dep-cr-details": _teaching_hint(
                role_in_requirement="This cell records where the Depreciation account is closed at year-end.",
                evidence_from_question="The second journal entry debits Profit and Loss and credits Depreciation for the same amount.",
                rule_or_principle="Expense accounts are transferred to Profit and Loss during closing entries.",
                how_to_derive="Copy Profit and Loss into the details column for the credit side of the Depreciation account.",
                transfer_tip="If a nominal expense account is being closed, expect Profit and Loss to appear as the transfer destination.",
            ),
            "depwf-acc-bal-amount": _teaching_hint(
                role_in_requirement="This cell gives the balance carried down on the accumulated depreciation account.",
                evidence_from_question=f"The account starts with Balance b/d of R{int(ledger_opening_accum):,} and receives a further credit posting of R{int(ledger_workflow_amount):,}.",
                rule_or_principle="A credit-balance account is balanced by placing Balance c/d on the debit side for the total credit balance.",
                how_to_derive=f"R{int(ledger_opening_accum):,} + R{int(ledger_workflow_amount):,} = R{int(ledger_closing_accum):,}.",
                transfer_tip="For accumulated depreciation, opening credit balance plus new depreciation usually produces the closing credit balance unless disposal information is given.",
            ),
        },
        guidelines=[
            "Use the opposite account name in each ledger details column.",
            "Close the Depreciation expense account to Profit and Loss before totalling it.",
            "Balance the accumulated depreciation account and carry the closing balance down to the next period.",
        ],
        marks=18,
    ), "depreciation_ledger_workflow_fill", expected_cells=18, cell_expectations=ledger_workflow_correct_map))

    computer_cost = 10000
    computer_rate = 20
    computer_dep_year = _round_money(computer_cost * computer_rate / 100)
    vehicle_cost = 120000
    vehicle_rate = 10
    vehicle_dep_year1 = _round_money(vehicle_cost * vehicle_rate / 100 * 6 / 12)
    vehicle_carry_year1 = _round_money(vehicle_cost - vehicle_dep_year1)
    vehicle_dep_year2 = _round_money(vehicle_carry_year1 * vehicle_rate / 100)
    vehicle_carry_year2 = _round_money(vehicle_carry_year1 - vehicle_dep_year2)
    vehicle_dep_year3 = _round_money(vehicle_carry_year2 * vehicle_rate / 100)
    vehicle_carry_year3 = _round_money(vehicle_carry_year2 - vehicle_dep_year3)
    asset_register_tables = [
        {
            "heading": "Asset register: computer (straight-line)",
            "headers": ["Date", "Annual depreciation", "Accumulated depreciation", "Carrying value"],
            "rows": [
                [_cell("31 Dec 2024"), _cell("", editable=True, cell_id="ar-comp-y1-dep"), _cell("", editable=True, cell_id="ar-comp-y1-accum"), _cell("", editable=True, cell_id="ar-comp-y1-carry")],
                [_cell("31 Dec 2025"), _cell("", editable=True, cell_id="ar-comp-y2-dep"), _cell("", editable=True, cell_id="ar-comp-y2-accum"), _cell("", editable=True, cell_id="ar-comp-y2-carry")],
                [_cell("31 Dec 2026"), _cell("", editable=True, cell_id="ar-comp-y3-dep"), _cell("", editable=True, cell_id="ar-comp-y3-accum"), _cell("", editable=True, cell_id="ar-comp-y3-carry")],
            ],
        },
        {
            "heading": "Asset register: vehicle (diminishing-balance)",
            "headers": ["Date", "Annual depreciation", "Accumulated depreciation", "Carrying value"],
            "rows": [
                [_cell("31 Dec 2024"), _cell("", editable=True, cell_id="ar-veh-y1-dep"), _cell("", editable=True, cell_id="ar-veh-y1-accum"), _cell("", editable=True, cell_id="ar-veh-y1-carry")],
                [_cell("31 Dec 2025"), _cell("", editable=True, cell_id="ar-veh-y2-dep"), _cell("", editable=True, cell_id="ar-veh-y2-accum"), _cell("", editable=True, cell_id="ar-veh-y2-carry")],
                [_cell("31 Dec 2026"), _cell("", editable=True, cell_id="ar-veh-y3-dep"), _cell("", editable=True, cell_id="ar-veh-y3-accum"), _cell("", editable=True, cell_id="ar-veh-y3-carry")],
            ],
        },
    ]
    asset_register_correct_map = {
        "ar-comp-y1-dep": computer_dep_year,
        "ar-comp-y1-accum": computer_dep_year,
        "ar-comp-y1-carry": _round_money(computer_cost - computer_dep_year),
        "ar-comp-y2-dep": computer_dep_year,
        "ar-comp-y2-accum": _round_money(computer_dep_year * 2),
        "ar-comp-y2-carry": _round_money(computer_cost - (computer_dep_year * 2)),
        "ar-comp-y3-dep": computer_dep_year,
        "ar-comp-y3-accum": _round_money(computer_dep_year * 3),
        "ar-comp-y3-carry": _round_money(computer_cost - (computer_dep_year * 3)),
        "ar-veh-y1-dep": vehicle_dep_year1,
        "ar-veh-y1-accum": vehicle_dep_year1,
        "ar-veh-y1-carry": vehicle_carry_year1,
        "ar-veh-y2-dep": vehicle_dep_year2,
        "ar-veh-y2-accum": _round_money(vehicle_dep_year1 + vehicle_dep_year2),
        "ar-veh-y2-carry": vehicle_carry_year2,
        "ar-veh-y3-dep": vehicle_dep_year3,
        "ar-veh-y3-accum": _round_money(vehicle_dep_year1 + vehicle_dep_year2 + vehicle_dep_year3),
        "ar-veh-y3-carry": vehicle_carry_year3,
    }
    asset_register_derivation_map = {
        "ar-comp-y1-dep": f"R{computer_cost:,} × {computer_rate}% = R{computer_dep_year:,}",
        "ar-comp-y1-accum": f"Year 1 accumulated depreciation for the computer equals the first year's depreciation: R{computer_dep_year:,}",
        "ar-comp-y2-carry": f"R{computer_cost:,} - R{_round_money(computer_dep_year * 2):,} = R{_round_money(computer_cost - (computer_dep_year * 2)):,}",
        "ar-veh-y1-dep": f"R{vehicle_cost:,} × {vehicle_rate}% × 6/12 = R{vehicle_dep_year1:,}",
        "ar-veh-y2-dep": f"R{vehicle_carry_year1:,} × {vehicle_rate}% = R{vehicle_dep_year2:,}",
        "ar-veh-y3-dep": f"R{vehicle_carry_year2:,} × {vehicle_rate}% = R{vehicle_dep_year3:,}",
    }
    asset_register_cell_hints = {
        "ar-comp-y1-dep": "The computer uses straight-line depreciation on cost price, so the annual amount repeats each year.",
        "ar-comp-y1-accum": "In the first year, accumulated depreciation is the same as the first year's depreciation.",
        "ar-comp-y1-carry": "Carrying value = cost price - accumulated depreciation.",
        "ar-veh-y1-dep": "The vehicle was only owned for 6 months in the first year.",
        "ar-veh-y2-dep": "Use the carrying value at the start of Year 2, not the original cost, for diminishing-balance depreciation.",
        "ar-veh-y2-accum": "Add Year 1 and Year 2 depreciation to get accumulated depreciation at the end of Year 2.",
    }
    asset_register_cell_teaching_map = {
        "ar-comp-y1-dep": _teaching_hint(
            role_in_requirement="This cell records the first year's annual depreciation for the computer.",
            evidence_from_question="The prompt states R10 000 at 20% on cost price.",
            rule_or_principle="Straight-line depreciation is calculated on original cost every year.",
            method_or_formula="Multiply the original cost by the straight-line rate.",
            record_link="This annual depreciation amount is then used to update accumulated depreciation and carrying value in the same register.",
            how_to_derive="R10 000 × 20% = R2 000.",
            transfer_tip="If the method is cost price / straight-line, expect the same annual amount each full year.",
        ),
        "ar-comp-y1-carry": _teaching_hint(
            role_in_requirement="This cell gives the carrying value of the computer at the end of the first year.",
            evidence_from_question=f"The computer cost is R{int(computer_cost):,} and Year 1 accumulated depreciation is R{int(computer_dep_year):,}.",
            rule_or_principle="Carrying value = cost price - accumulated depreciation.",
            method_or_formula="Subtract the accumulated depreciation from the original cost.",
            record_link="This carrying value becomes a presentation figure in the register even though straight-line depreciation next year still uses cost price.",
            how_to_derive=f"R{int(computer_cost):,} - R{int(computer_dep_year):,} = R{int(_round_money(computer_cost - computer_dep_year)):,}.",
            transfer_tip="Do not confuse the carrying value display with the base used for straight-line depreciation; straight-line still uses cost price.",
        ),
        "ar-veh-y1-dep": _teaching_hint(
            role_in_requirement="This cell records the first year's annual depreciation for the vehicle.",
            evidence_from_question="The vehicle cost is R120 000 and it was owned for 6 months in the first year.",
            rule_or_principle="Diminishing-balance uses the carrying value, and part-year ownership must be pro-rated.",
            method_or_formula="Multiply the cost by the diminishing-balance rate and then pro-rate for the 6 months owned.",
            record_link="This Year 1 depreciation is then used to find both accumulated depreciation and the Year 1 carrying value that becomes the Year 2 base.",
            how_to_derive="R120 000 × 10% × 6/12 = R6 000.",
            transfer_tip="When an asset is bought during the year, include only the months owned in the first year's calculation.",
        ),
        "ar-veh-y2-dep": _teaching_hint(
            role_in_requirement="This cell calculates the vehicle's Year 2 depreciation using the diminishing-balance method.",
            evidence_from_question=f"The Year 1 carrying value is R{int(vehicle_carry_year1):,}, and the vehicle continues at {vehicle_rate}% on diminishing balance.",
            rule_or_principle="Under diminishing balance, each year's depreciation is calculated on the carrying value at the start of that year.",
            method_or_formula="Multiply the Year 1 carrying value by the depreciation rate.",
            record_link="This depreciation amount then updates the accumulated depreciation and reduces the carrying value again for Year 2.",
            how_to_derive=f"R{int(vehicle_carry_year1):,} × {vehicle_rate}% = R{int(vehicle_dep_year2):,}.",
            transfer_tip="With diminishing balance, the base changes every year, so check the previous carrying value before calculating the next year's depreciation.",
        ),
    }
    pool.append(_make_fill_in_table_question(
        question_type="asset_register_table",
        prompt=f"{biz} bought a computer for R{computer_cost:,} on 1 January 2024 and a vehicle for R{vehicle_cost:,} on 1 July 2024. Complete the asset registers to 31 December 2026. The computer is depreciated at {computer_rate}% on cost price and the vehicle at {vehicle_rate}% on diminishing balance.",
        tables=asset_register_tables,
        correct_map=asset_register_correct_map,
        derivation_map=asset_register_derivation_map,
        cell_hints=asset_register_cell_hints,
        cell_teaching_map=asset_register_cell_teaching_map,
        working_map={
            "ar-comp-y1-dep": "Finish each computer row in order: annual depreciation, then accumulated depreciation, then carrying value.",
            "ar-veh-y2-dep": "For the vehicle, always use the previous year's carrying value as the new base before completing the rest of the row.",
            "ar-veh-y2-accum": "In both registers, accumulated depreciation is a running total, not a new separate formula each year.",
        },
        guidelines=[
            "Straight-line depreciation repeats on original cost each full year.",
            "Diminishing-balance depreciation uses the carrying value at the start of each year.",
            "Accumulated depreciation grows year by year, and carrying value is cost less accumulated depreciation.",
        ],
        marks=18,
    ))

    equipment_purchase = r.choice([28000, 36000, 42000, 50000])
    installation_cost = r.choice([2000, 3500, 5000])
    equipment_total_cost = _round_money(equipment_purchase + installation_cost)
    equipment_rate = r.choice([10, 15])
    equipment_dep_year1 = _round_money(equipment_total_cost * equipment_rate / 100 * 4 / 12)
    equipment_dep_year2 = _round_money(equipment_total_cost * equipment_rate / 100)
    equipment_dep_year3 = _round_money(equipment_total_cost * equipment_rate / 100)
    equipment_accum_year1 = equipment_dep_year1
    equipment_accum_year2 = _round_money(equipment_dep_year1 + equipment_dep_year2)
    equipment_accum_year3 = _round_money(equipment_dep_year1 + equipment_dep_year2 + equipment_dep_year3)
    equipment_carry_year1 = _round_money(equipment_total_cost - equipment_accum_year1)
    equipment_carry_year2 = _round_money(equipment_total_cost - equipment_accum_year2)
    equipment_carry_year3 = _round_money(equipment_total_cost - equipment_accum_year3)
    asset_register_note_tables = [
        {
            "heading": "Asset register: equipment (straight-line)",
            "headers": ["Date", "Annual depreciation", "Accumulated depreciation", "Carrying value"],
            "rows": [
                [_cell("31 Dec 2025"), _cell("", editable=True, cell_id="ar-equip-y1-dep"), _cell("", editable=True, cell_id="ar-equip-y1-accum"), _cell("", editable=True, cell_id="ar-equip-y1-carry")],
                [_cell("31 Dec 2026"), _cell("", editable=True, cell_id="ar-equip-y2-dep"), _cell("", editable=True, cell_id="ar-equip-y2-accum"), _cell("", editable=True, cell_id="ar-equip-y2-carry")],
                [_cell("31 Dec 2027"), _cell("", editable=True, cell_id="ar-equip-y3-dep"), _cell("", editable=True, cell_id="ar-equip-y3-accum"), _cell("", editable=True, cell_id="ar-equip-y3-carry")],
            ],
        },
        {
            "heading": "Tangible assets note extract (31 Dec 2027)",
            "headers": ["Asset", "Cost price", "Accumulated depreciation", "Carrying value"],
            "rows": [
                [_cell("Equipment"), _cell("", editable=True, cell_id="ar-note-cost"), _cell("", editable=True, cell_id="ar-note-accum"), _cell("", editable=True, cell_id="ar-note-carry")],
            ],
        },
    ]
    asset_register_note_correct_map = {
        "ar-equip-y1-dep": equipment_dep_year1,
        "ar-equip-y1-accum": equipment_accum_year1,
        "ar-equip-y1-carry": equipment_carry_year1,
        "ar-equip-y2-dep": equipment_dep_year2,
        "ar-equip-y2-accum": equipment_accum_year2,
        "ar-equip-y2-carry": equipment_carry_year2,
        "ar-equip-y3-dep": equipment_dep_year3,
        "ar-equip-y3-accum": equipment_accum_year3,
        "ar-equip-y3-carry": equipment_carry_year3,
        "ar-note-cost": equipment_total_cost,
        "ar-note-accum": equipment_accum_year3,
        "ar-note-carry": equipment_carry_year3,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="asset_register_table",
        prompt=f"{biz} bought equipment on 1 September 2025 for R{int(equipment_purchase):,} and paid installation costs of R{int(installation_cost):,}. Depreciation is written off at {equipment_rate}% per annum on cost price. Complete the asset register to 31 December 2027 and then complete the tangible assets note extract.",
        prompt_table={
            "heading": "Purchase and policy details",
            "headers": ["Item", "Amount / detail"],
            "rows": [
                [_cell("Equipment invoice price"), _cell(equipment_purchase)],
                [_cell("Installation cost"), _cell(installation_cost)],
                [_cell("Date bought"), _cell("1 Sep 2025")],
                [_cell("Depreciation method"), _cell("Straight-line on total cost")],
                [_cell("Rate"), _cell(f"{equipment_rate}% p.a.")],
            ],
        },
        tables=asset_register_note_tables,
        correct_map=asset_register_note_correct_map,
        derivation_map={
            "ar-equip-y1-dep": f"Total cost = R{int(equipment_purchase):,} + R{int(installation_cost):,} = R{int(equipment_total_cost):,}; Year 1 depreciation = R{int(equipment_total_cost):,} × {equipment_rate}% × 4/12 = R{int(equipment_dep_year1):,}",
            "ar-equip-y2-dep": f"Full-year straight-line depreciation = R{int(equipment_total_cost):,} × {equipment_rate}% = R{int(equipment_dep_year2):,}",
            "ar-note-cost": f"Cost price in the note = Purchase price R{int(equipment_purchase):,} + Installation cost R{int(installation_cost):,} = R{int(equipment_total_cost):,}",
            "ar-note-accum": f"Accumulated depreciation at 31 Dec 2027 = R{int(equipment_dep_year1):,} + R{int(equipment_dep_year2):,} + R{int(equipment_dep_year3):,} = R{int(equipment_accum_year3):,}",
            "ar-note-carry": f"Carrying value at 31 Dec 2027 = Cost price R{int(equipment_total_cost):,} - Accumulated depreciation R{int(equipment_accum_year3):,} = R{int(equipment_carry_year3):,}",
        },
        cell_hints={
            "ar-equip-y1-dep": "Include installation cost in the cost price, then pro-rate for the 4 months owned in 2025.",
            "ar-equip-y2-dep": "Straight-line depreciation on cost price uses the same full-year amount each full year.",
            "ar-note-cost": "The tangible assets note uses the total cost including installation.",
            "ar-note-accum": "The note's accumulated depreciation must agree with the final accumulated-depreciation balance in the register.",
            "ar-note-carry": "Carrying value in the note must match the final carrying value in the asset register.",
        },
        cell_teaching_map={
            "ar-equip-y1-dep": _teaching_hint(
                role_in_requirement="This cell records the first depreciation charge in the asset register.",
                evidence_from_question=f"The asset cost includes both the purchase price R{int(equipment_purchase):,} and installation cost R{int(installation_cost):,}, and it was owned for only 4 months in 2025.",
                rule_or_principle="Installation costs form part of the asset's cost price, and straight-line depreciation is pro-rated for part-year ownership.",
                method_or_formula="First combine purchase price and installation to get total cost, then apply the annual rate for 4/12 of a year.",
                record_link="This first-year depreciation feeds the register's accumulated-depreciation and carrying-value lines and later the note extract.",
                how_to_derive=f"First find total cost R{int(equipment_total_cost):,}, then calculate R{int(equipment_total_cost):,} × {equipment_rate}% × 4/12 = R{int(equipment_dep_year1):,}.",
                transfer_tip="Whenever an asset is bought during the year, decide whether any extra costs belong to cost price and then adjust the first year's depreciation for the months owned.",
            ),
            "ar-note-cost": _teaching_hint(
                role_in_requirement="This cell records the cost-price figure for the tangible assets note.",
                evidence_from_question=f"The prompt gives an equipment purchase price of R{int(equipment_purchase):,} and installation cost of R{int(installation_cost):,}.",
                rule_or_principle="Installation cost forms part of the asset's cost price and must be included in note disclosure.",
                method_or_formula="Add the invoice price and installation cost to determine the disclosed cost price.",
                record_link="This cost figure is the same total cost used as the base for the asset-register depreciation calculations.",
                how_to_derive=f"R{int(equipment_purchase):,} + R{int(installation_cost):,} = R{int(equipment_total_cost):,}.",
                transfer_tip="When a note asks for cost price, use the full capitalized cost, not only the supplier invoice amount.",
            ),
            "ar-note-carry": _teaching_hint(
                role_in_requirement="This cell carries the final register balance into the tangible assets note extract.",
                evidence_from_question="The note is dated 31 Dec 2027, so it must use the same closing balances as the last line of the register.",
                rule_or_principle="A disclosure note should agree to the closing balances in the detailed asset register.",
                method_or_formula="Use the final carrying value already produced in the register rather than recalculating it from scratch in the note.",
                record_link="This note disclosure must reconcile with the closing line of the register for the same date.",
                how_to_derive=f"Use the 31 Dec 2027 carrying value from the register: R{int(equipment_carry_year3):,}.",
                transfer_tip="When a question combines a detailed schedule and a disclosure note, finish the schedule first and then transfer the closing balances into the note.",
            ),
        },
        working_map={
            "ar-equip-y1-dep": "Build the register first: total cost, then Year 1 part-year depreciation, then later full-year straight-line charges.",
            "ar-note-cost": "Only after the register is complete should you transfer the final cost, accumulated depreciation, and carrying value into the note.",
            "ar-note-carry": "The note is a carry-through disclosure, so its closing figures must match the last row of the register exactly.",
        },
        guidelines=[
            "Include installation cost in the cost price before calculating depreciation.",
            "Pro-rate the first year's depreciation because the asset was bought during the year.",
            "The tangible assets note must agree with the closing balances in the asset register.",
        ],
        marks=12,
    ), "asset_register_installation_note_fill", expected_cells=12, cell_expectations=asset_register_note_correct_map))

    pool.append(_make_mcq(
        prompt="Can the value of an asset be reflected as R0 (zero) in the financial statements?",
        options=[
            "Yes, once fully depreciated it shows R0.",
            "No — the final value must be shown as R1 in the Balance Sheet.",
            "Yes, but only for vehicles.",
            "No — it must be written off to the Capital account.",
        ],
        correct_index=1,
        explanation="The value of an asset can never be R0 in financial statements. The final carrying value is shown as R1.",
    ))

    return pool


__all__ = ["_gen_closing_transfers", "_gen_depreciation"]
