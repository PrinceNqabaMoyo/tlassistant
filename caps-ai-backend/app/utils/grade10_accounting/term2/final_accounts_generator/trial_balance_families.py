from __future__ import annotations

import random
from typing import Any, Dict, List

from ....sole_trader.names import pick_business_name as _pick_business_name
from .shared import (
    _cell,
    _make_fill_in_table_question,
    _make_mcq,
    _make_typed,
    _round_money,
    _teaching_hint,
    _with_validation,
)


def _gen_trial_balance(r: random.Random) -> List[Dict[str, Any]]:
    """Pre/post adjustment and post-closing trial balance concepts."""
    pool: List[Dict[str, Any]] = []
    biz = _pick_business_name(r=r)

    bank_balance = r.choice([42000, 56000, 68000])
    stock_balance = r.choice([18000, 22000, 26000])
    equipment_balance = r.choice([65000, 84000, 96000])
    capital_balance = r.choice([90000, 108000, 122000])
    creditors_balance = r.choice([14000, 18000, 22000])
    loan_balance = _round_money(bank_balance + stock_balance + equipment_balance - capital_balance - creditors_balance)
    post_closing_total = _round_money(bank_balance + stock_balance + equipment_balance)

    prompt_table = {
        "heading": "Extracted balances after closing transfers",
        "headers": ["Account", "Amount"],
        "rows": [
            [_cell("Bank"), _cell(bank_balance)],
            [_cell("Trading stock"), _cell(stock_balance)],
            [_cell("Equipment"), _cell(equipment_balance)],
            [_cell("Capital"), _cell(capital_balance)],
            [_cell("Creditors control"), _cell(creditors_balance)],
            [_cell("Loan"), _cell(loan_balance)],
        ],
    }
    trial_balance_table = {
        "heading": "Post-closing Trial Balance",
        "headers": ["Account", "Debit", "Credit"],
        "rows": [
            [_cell("Bank"), _cell("", editable=True, cell_id="tb-bank-debit"), _cell("")],
            [_cell("Trading stock"), _cell("", editable=True, cell_id="tb-stock-debit"), _cell("")],
            [_cell("Equipment"), _cell("", editable=True, cell_id="tb-equipment-debit"), _cell("")],
            [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="tb-capital-credit")],
            [_cell("Creditors control"), _cell(""), _cell("", editable=True, cell_id="tb-creditors-credit")],
            [_cell("Loan"), _cell(""), _cell("", editable=True, cell_id="tb-loan-credit")],
            [_cell("Total"), _cell("", editable=True, cell_id="tb-total-debit"), _cell("", editable=True, cell_id="tb-total-credit")],
        ],
    }
    trial_balance_correct_map = {
        "tb-bank-debit": bank_balance,
        "tb-stock-debit": stock_balance,
        "tb-equipment-debit": equipment_balance,
        "tb-capital-credit": capital_balance,
        "tb-creditors-credit": creditors_balance,
        "tb-loan-credit": loan_balance,
        "tb-total-debit": post_closing_total,
        "tb-total-credit": post_closing_total,
    }
    trial_balance_derivation_map = {
        "tb-total-debit": f"Add the asset debits: R{bank_balance:,} + R{stock_balance:,} + R{equipment_balance:,} = R{post_closing_total:,}",
        "tb-total-credit": f"Credit total must equal the debit total = R{post_closing_total:,}",
    }
    trial_balance_cell_hints = {
        "tb-bank-debit": "Bank is an asset, so place it on the debit side.",
        "tb-stock-debit": "Trading stock is an asset and appears in the debit column.",
        "tb-equipment-debit": "Equipment is a non-current asset and appears in the debit column.",
        "tb-capital-credit": "Capital is owner's equity, so it appears in the credit column.",
        "tb-creditors-credit": "Creditors control is a liability, so it belongs in the credit column.",
        "tb-loan-credit": "A loan is a liability and therefore appears on the credit side.",
        "tb-total-debit": "Total the debit column after placing all balances on the correct side.",
        "tb-total-credit": "Once the trial balance is complete, the credit total must match the debit total.",
    }
    trial_balance_cell_teaching_map = {
        "tb-bank-debit": _teaching_hint(
            role_in_requirement="This cell places the Bank balance in the correct side of the Post-closing Trial Balance.",
            evidence_from_question=f"The extracted balances list Bank at R{int(bank_balance):,}.",
            rule_or_principle="Assets appear in the debit column of the Post-closing Trial Balance.",
            method_or_formula="Copy the Bank balance unchanged into the debit column.",
            record_link="Bank remains a Balance Sheet asset after all nominal accounts have been closed.",
            how_to_derive=f"Copy Bank = R{int(bank_balance):,} to the debit side.",
            transfer_tip="In a Post-closing Trial Balance, classify each remaining account first as asset, capital, liability, or contra-asset.",
        ),
        "tb-stock-debit": _teaching_hint(
            role_in_requirement="This cell places Trading stock in the correct column of the Post-closing Trial Balance.",
            evidence_from_question=f"The extracted balances list Trading stock at R{int(stock_balance):,}.",
            rule_or_principle="Trading stock is a current asset and therefore appears in the debit column.",
            method_or_formula="Copy the Trading stock balance unchanged into the debit column.",
            record_link="Trading stock remains on the Balance Sheet after the closing process and therefore stays in the trial balance.",
            how_to_derive=f"Copy Trading stock = R{int(stock_balance):,} to the debit side.",
            transfer_tip="Do not confuse Trading stock as an asset on the Post-closing Trial Balance with Cost of Sales, which is already closed off.",
        ),
        "tb-equipment-debit": _teaching_hint(
            role_in_requirement="This cell places the Equipment balance in the debit column of the Post-closing Trial Balance.",
            evidence_from_question=f"The extracted balances list Equipment at R{int(equipment_balance):,}.",
            rule_or_principle="Non-current assets appear on the debit side of the Post-closing Trial Balance.",
            method_or_formula="Copy the Equipment balance unchanged into the debit column.",
            record_link="Equipment remains a Balance Sheet asset after closing transfers are complete.",
            how_to_derive=f"Copy Equipment = R{int(equipment_balance):,} to the debit side.",
            transfer_tip="When there is no accumulated depreciation line shown in a compact extract, place the asset balance itself on the debit side.",
        ),
        "tb-capital-credit": _teaching_hint(
            role_in_requirement="This cell places the capital balance in the correct side of the trial balance.",
            evidence_from_question="Capital is listed in the extracted balances.",
            rule_or_principle="Capital and liabilities appear in the credit column of the Post-closing Trial Balance.",
            method_or_formula="Copy the Capital balance unchanged into the credit column.",
            record_link="Capital remains after the income and expense accounts have been closed and therefore appears in the Post-closing Trial Balance.",
            how_to_derive="Copy the capital amount to the credit side only.",
            transfer_tip="On a Post-closing Trial Balance, ask first: asset, liability, or capital?",
        ),
        "tb-creditors-credit": _teaching_hint(
            role_in_requirement="This cell places the Creditors control balance in the correct column.",
            evidence_from_question=f"The extracted balances list Creditors control at R{int(creditors_balance):,}.",
            rule_or_principle="Liabilities appear in the credit column of the Post-closing Trial Balance.",
            method_or_formula="Copy the Creditors control balance unchanged into the credit column.",
            record_link="Creditors control is a Balance Sheet liability and therefore remains after the nominal accounts are closed.",
            how_to_derive=f"Copy Creditors control = R{int(creditors_balance):,} to the credit side.",
            transfer_tip="Trade payables and other liabilities usually stay on the credit side unless the question clearly indicates an abnormal balance.",
        ),
        "tb-loan-credit": _teaching_hint(
            role_in_requirement="This cell places the Loan balance in the correct side of the Post-closing Trial Balance.",
            evidence_from_question=f"The extracted balances list Loan at R{int(loan_balance):,}.",
            rule_or_principle="Loan balances are liabilities and therefore appear in the credit column.",
            method_or_formula="Copy the Loan amount unchanged into the credit column.",
            record_link="The loan remains in the Balance Sheet after year-end closing and must appear in the Post-closing Trial Balance.",
            how_to_derive=f"Copy Loan = R{int(loan_balance):,} to the credit side.",
            transfer_tip="Use the account nature rather than the word 'loan' alone; if it is money owed, it usually belongs on the credit side.",
        ),
        "tb-total-debit": _teaching_hint(
            role_in_requirement="This cell gives the total of the debit column.",
            evidence_from_question="Use all balances you have already placed on the debit side.",
            rule_or_principle="A correct trial balance has equal debit and credit totals.",
            method_or_formula="Add the three asset balances already placed in the debit column.",
            record_link="The matching credit total checks that all remaining Balance Sheet accounts were placed on the correct side.",
            how_to_derive=f"R{bank_balance:,} + R{stock_balance:,} + R{equipment_balance:,} = R{post_closing_total:,}",
            transfer_tip="In multipart bookkeeping questions, total cells are a check on your earlier placements.",
        ),
        "tb-total-credit": _teaching_hint(
            role_in_requirement="This cell completes the credit total of the Post-closing Trial Balance.",
            evidence_from_question="The credit side contains Capital, Creditors control, and Loan after all nominal accounts have been closed.",
            rule_or_principle="The credit total in a correct trial balance must equal the debit total.",
            method_or_formula="Use the same balanced total as the debit side once all credit balances have been placed correctly.",
            record_link="This total is the final check that the remaining Balance Sheet balances have been classified correctly.",
            how_to_derive=f"Credit total = R{post_closing_total:,} to match the debit total.",
            transfer_tip="If the totals do not agree, first re-check placement errors before assuming an arithmetic mistake.",
        ),
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="trial_balance_table",
        prompt="Use the extracted balances below to complete the Post-closing Trial Balance. Enter each amount on the correct side and total the two columns.",
        prompt_table=prompt_table,
        table=trial_balance_table,
        correct_map=trial_balance_correct_map,
        derivation_map=trial_balance_derivation_map,
        cell_hints=trial_balance_cell_hints,
        cell_teaching_map=trial_balance_cell_teaching_map,
        working_map={
            "tb-bank-debit": "Complete the asset rows first because they determine the debit total later on.",
            "tb-capital-credit": "Once the asset side is in place, classify the remaining rows as capital or liabilities for the credit side.",
            "tb-total-debit": "Add the finished debit column only after every asset has been placed.",
            "tb-total-credit": "The final credit total is a balance check against the completed debit side.",
        },
        guidelines=["Only Balance Sheet accounts appear on the Post-closing Trial Balance.", "Assets go to the debit column.", "Capital and liabilities go to the credit column."],
        marks=8,
    ), "post_closing_trial_balance_fill", expected_cells=8, total=post_closing_total))

    postclosing_scenarios = [
        {
            "bank": 82000,
            "debtors": 54000,
            "trading_stock": 28000,
            "equipment": 120000,
            "vehicles": 90000,
            "accum_equipment": 18000,
            "accum_vehicles": 12000,
            "creditors": 26000,
            "loan": 50000,
        },
        {
            "bank": 76000,
            "debtors": 48000,
            "trading_stock": 32000,
            "equipment": 100000,
            "vehicles": 110000,
            "accum_equipment": 15000,
            "accum_vehicles": 14000,
            "creditors": 30000,
            "loan": 60000,
        },
        {
            "bank": 68000,
            "debtors": 62000,
            "trading_stock": 26000,
            "equipment": 98000,
            "vehicles": 84000,
            "accum_equipment": 16000,
            "accum_vehicles": 10000,
            "creditors": 24000,
            "loan": 45000,
        },
    ]
    for scenario in postclosing_scenarios:
        postclosing_total = _round_money(float(scenario["bank"]) + float(scenario["debtors"]) + float(scenario["trading_stock"]) + float(scenario["equipment"]) + float(scenario["vehicles"]))
        capital = _round_money(float(postclosing_total) - float(scenario["accum_equipment"]) - float(scenario["accum_vehicles"]) - float(scenario["creditors"]) - float(scenario["loan"]))
        expanded_prompt_tables = [
            {
                "heading": f"{biz} — Extracted balances after closing transfers",
                "headers": ["Account", "Amount"],
                "rows": [
                    [_cell("Bank"), _cell(scenario["bank"])],
                    [_cell("Debtors control"), _cell(scenario["debtors"])],
                    [_cell("Trading stock"), _cell(scenario["trading_stock"])],
                    [_cell("Equipment"), _cell(scenario["equipment"])],
                    [_cell("Vehicles"), _cell(scenario["vehicles"])],
                    [_cell("Accumulated depreciation on equipment"), _cell(scenario["accum_equipment"])],
                    [_cell("Accumulated depreciation on vehicles"), _cell(scenario["accum_vehicles"])],
                    [_cell("Creditors control"), _cell(scenario["creditors"])],
                    [_cell("Loan"), _cell(scenario["loan"])],
                    [_cell("Capital"), _cell(capital)],
                ],
            },
        ]
        expanded_table = {
            "heading": "Post-closing Trial Balance (fuller extract)",
            "headers": ["Account", "Debit", "Credit"],
            "rows": [
                [_cell("Bank"), _cell("", editable=True, cell_id="pctb-bank-debit"), _cell("")],
                [_cell("Debtors control"), _cell("", editable=True, cell_id="pctb-debtors-debit"), _cell("")],
                [_cell("Trading stock"), _cell("", editable=True, cell_id="pctb-stock-debit"), _cell("")],
                [_cell("Equipment"), _cell("", editable=True, cell_id="pctb-equipment-debit"), _cell("")],
                [_cell("Vehicles"), _cell("", editable=True, cell_id="pctb-vehicles-debit"), _cell("")],
                [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="pctb-capital-credit")],
                [_cell("Accumulated depreciation on equipment"), _cell(""), _cell("", editable=True, cell_id="pctb-accum-equip-credit")],
                [_cell("Accumulated depreciation on vehicles"), _cell(""), _cell("", editable=True, cell_id="pctb-accum-veh-credit")],
                [_cell("Creditors control"), _cell(""), _cell("", editable=True, cell_id="pctb-creditors-credit")],
                [_cell("Loan"), _cell(""), _cell("", editable=True, cell_id="pctb-loan-credit")],
                [_cell("Total"), _cell("", editable=True, cell_id="pctb-total-debit"), _cell("", editable=True, cell_id="pctb-total-credit")],
            ],
        }
        expanded_correct_map = {
            "pctb-bank-debit": scenario["bank"],
            "pctb-debtors-debit": scenario["debtors"],
            "pctb-stock-debit": scenario["trading_stock"],
            "pctb-equipment-debit": scenario["equipment"],
            "pctb-vehicles-debit": scenario["vehicles"],
            "pctb-capital-credit": capital,
            "pctb-accum-equip-credit": scenario["accum_equipment"],
            "pctb-accum-veh-credit": scenario["accum_vehicles"],
            "pctb-creditors-credit": scenario["creditors"],
            "pctb-loan-credit": scenario["loan"],
            "pctb-total-debit": postclosing_total,
            "pctb-total-credit": postclosing_total,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="trial_balance_table",
            prompt=f"Use the extracted balances for {biz} to complete the fuller Post-closing Trial Balance. Place every balance on the correct side and total the two columns.",
            prompt_tables=expanded_prompt_tables,
            table=expanded_table,
            correct_map=expanded_correct_map,
            derivation_map={
                "pctb-total-debit": f"Debit total = R{int(scenario['bank']):,} + R{int(scenario['debtors']):,} + R{int(scenario['trading_stock']):,} + R{int(scenario['equipment']):,} + R{int(scenario['vehicles']):,} = R{int(postclosing_total):,}.",
                "pctb-total-credit": f"Credit total = Capital R{int(capital):,} + Accumulated depreciation on equipment R{int(scenario['accum_equipment']):,} + Accumulated depreciation on vehicles R{int(scenario['accum_vehicles']):,} + Creditors R{int(scenario['creditors']):,} + Loan R{int(scenario['loan']):,} = R{int(postclosing_total):,}.",
            },
            cell_hints={
                "pctb-bank-debit": "Bank is an asset, so it belongs on the debit side.",
                "pctb-debtors-debit": "Debtors control is an asset and therefore appears in the debit column.",
                "pctb-stock-debit": "Trading stock is a current asset and goes to the debit side.",
                "pctb-equipment-debit": "Equipment is a non-current asset and appears on the debit side.",
                "pctb-vehicles-debit": "Vehicles are assets and therefore belong in the debit column.",
                "pctb-accum-equip-credit": "Accumulated depreciation is a contra-asset with a credit balance.",
                "pctb-accum-veh-credit": "Accumulated depreciation on vehicles is also a contra-asset and belongs on the credit side.",
                "pctb-capital-credit": "Capital belongs on the credit side of the Post-closing Trial Balance.",
                "pctb-creditors-credit": "Creditors control is a liability and therefore appears in the credit column.",
                "pctb-loan-credit": "A loan is a liability and appears in the credit column.",
                "pctb-total-debit": "Total the debit column only after all the balances have been placed correctly.",
                "pctb-total-credit": "The credit total must match the debit total once the trial balance is complete.",
            },
            cell_teaching_map={
                "pctb-bank-debit": _teaching_hint(
                    role_in_requirement="This cell places the Bank balance in the debit column of the fuller Post-closing Trial Balance.",
                    evidence_from_question=f"The extracted balances show Bank at R{int(scenario['bank']):,}.",
                    rule_or_principle="Asset balances appear in the debit column.",
                    method_or_formula="Copy the Bank balance unchanged into the debit column.",
                    record_link="Bank remains a Balance Sheet item after all nominal-account closing transfers are complete.",
                    how_to_derive=f"Copy Bank = R{int(scenario['bank']):,} to the debit side.",
                    transfer_tip="Start by separating assets from claims against the business before totaling the columns.",
                ),
                "pctb-accum-equip-credit": _teaching_hint(
                    role_in_requirement="This cell places accumulated depreciation on equipment in the correct side of the Post-closing Trial Balance.",
                    evidence_from_question=f"The extracted balances show accumulated depreciation on equipment of R{int(scenario['accum_equipment']):,}.",
                    rule_or_principle="Accumulated depreciation is a contra-asset and therefore carries a credit balance in the trial balance.",
                    method_or_formula="Copy the accumulated-depreciation amount unchanged into the credit column.",
                    record_link="This contra-asset remains paired with the related asset account on the Balance Sheet side of the records.",
                    how_to_derive=f"Copy R{int(scenario['accum_equipment']):,} to the credit column.",
                    transfer_tip="Even though accumulated depreciation relates to an asset, it is not placed on the debit side because its balance is the opposite of the asset account.",
                ),
                "pctb-capital-credit": _teaching_hint(
                    role_in_requirement="This cell places the owner's capital in the credit column of the Post-closing Trial Balance.",
                    evidence_from_question=f"The extracted balances include Capital of R{int(capital):,} after closing transfers.",
                    rule_or_principle="Capital is part of owner's equity and appears on the credit side of the Post-closing Trial Balance.",
                    method_or_formula="Copy the Capital balance unchanged into the credit column.",
                    record_link="Capital remains after closing transfers and is shown together with liabilities on the credit side.",
                    how_to_derive=f"Copy the Capital balance R{int(capital):,} to the credit column.",
                    transfer_tip="On a Post-closing Trial Balance, ask whether the account is an asset or a claim against the business; equity and liabilities go to credit.",
                ),
                "pctb-total-debit": _teaching_hint(
                    role_in_requirement="This cell gives the total of the debit column in the fuller Post-closing Trial Balance.",
                    evidence_from_question="All asset balances have already been placed in the debit column above this total line.",
                    rule_or_principle="A correct Post-closing Trial Balance must still balance after all income and expense accounts have been closed.",
                    method_or_formula="Add the five asset balances already placed in the debit column.",
                    record_link="The matching credit total confirms that the remaining capital, liability, and contra-asset balances were placed correctly.",
                    how_to_derive=f"Add the five debit balances to get R{int(postclosing_total):,}.",
                    transfer_tip="Leave the total row until the end and use it as a check that every balance has been placed on the correct side.",
                ),
                "pctb-total-credit": _teaching_hint(
                    role_in_requirement="This cell gives the total of the credit column in the fuller Post-closing Trial Balance.",
                    evidence_from_question="The credit side contains Capital, accumulated depreciation balances, Creditors control, and Loan.",
                    rule_or_principle="A correct Post-closing Trial Balance has equal debit and credit totals.",
                    method_or_formula="Use the same balanced total as the debit side after all credit balances are placed correctly.",
                    record_link="This total is the last check that all remaining Balance Sheet accounts have been classified correctly.",
                    how_to_derive=f"Credit total = R{int(postclosing_total):,} to match the debit total.",
                    transfer_tip="If totals differ, check account placement before checking arithmetic.",
                ),
            },
            working_map={
                "pctb-bank-debit": "The fuller extract still follows the same rule: list all asset balances on the debit side first.",
                "pctb-capital-credit": "After the assets are placed, complete the claims-against-the-business side with capital, liabilities, and contra-assets.",
                "pctb-total-debit": "Total the completed asset side only after all debit placements are finished.",
                "pctb-total-credit": "The credit total is the final agreement check against the debit total.",
            },
            guidelines=[
                "Only Balance Sheet accounts remain after closing transfers.",
                "Assets go to the debit column; capital, liabilities, and contra-assets go to the credit column.",
                "Total the two finished columns and check that they are equal.",
            ],
            marks=12,
        ), "post_closing_trial_balance_expanded_fill", expected_cells=12, cell_expectations=expanded_correct_map, total=postclosing_total))

    postadj_scenarios = [
        {
            "income_label": "Rent income",
            "income_adjustment_label": "Rent income owing at year-end",
            "income_base": 18000,
            "income_adjustment": 4000,
            "prepaid_label": "Insurance",
            "prepaid_adjustment_label": "Insurance paid in advance",
            "prepaid_base": 12000,
            "prepaid_adjustment": 9000,
            "expense_label": "Telephone",
            "expense_adjustment_label": "Telephone expense owing",
            "expense_base": 7200,
            "expense_adjustment": 1800,
            "asset_label": "Equipment",
            "asset_cost": 90000,
            "depreciation_amount": 9000,
            "bank": 52000,
            "stock": 24000,
            "debtors": 65000,
            "cost_of_sales": 280000,
            "sales": 390000,
            "creditors": 15000,
            "loan": 30000,
        },
        {
            "income_label": "Commission income",
            "income_adjustment_label": "Commission income owing at year-end",
            "income_base": 24000,
            "income_adjustment": 6000,
            "prepaid_label": "Advertising",
            "prepaid_adjustment_label": "Advertising paid in advance",
            "prepaid_base": 18000,
            "prepaid_adjustment": 12000,
            "expense_label": "Wages",
            "expense_adjustment_label": "Wages owing at year-end",
            "expense_base": 15600,
            "expense_adjustment": 2400,
            "asset_label": "Vehicles",
            "asset_cost": 120000,
            "depreciation_amount": 12000,
            "bank": 61000,
            "stock": 28000,
            "debtors": 54000,
            "cost_of_sales": 310000,
            "sales": 450000,
            "creditors": 21000,
            "loan": 36000,
        },
        {
            "income_label": "Interest income",
            "income_adjustment_label": "Interest income owing at year-end",
            "income_base": 12000,
            "income_adjustment": 3000,
            "prepaid_label": "Rates",
            "prepaid_adjustment_label": "Rates paid in advance",
            "prepaid_base": 15000,
            "prepaid_adjustment": 6000,
            "expense_label": "Water and electricity",
            "expense_adjustment_label": "Water and electricity owing at year-end",
            "expense_base": 9600,
            "expense_adjustment": 1400,
            "asset_label": "Fixtures",
            "asset_cost": 80000,
            "depreciation_amount": 8000,
            "bank": 47000,
            "stock": 20000,
            "debtors": 58000,
            "cost_of_sales": 260000,
            "sales": 360000,
            "creditors": 17000,
            "loan": 25000,
        },
    ]
    for scenario in postadj_scenarios:
        preadj_capital = _round_money(
            float(scenario["bank"]) + float(scenario["stock"]) + float(scenario["debtors"]) + float(scenario["asset_cost"]) + float(scenario["expense_base"]) + float(scenario["prepaid_base"]) + float(scenario["cost_of_sales"]) - float(scenario["sales"]) - float(scenario["income_base"]) - float(scenario["creditors"]) - float(scenario["loan"])
        )
        adjusted_expense = _round_money(float(scenario["expense_base"]) + float(scenario["expense_adjustment"]))
        adjusted_prepaid_balance = _round_money(float(scenario["prepaid_base"]) - float(scenario["prepaid_adjustment"]))
        adjusted_income = _round_money(float(scenario["income_base"]) + float(scenario["income_adjustment"]))
        income_label_lower = str(scenario["income_label"]).lower()
        prepaid_label_lower = str(scenario["prepaid_label"]).lower()
        expense_label_lower = str(scenario["expense_label"]).lower()
        asset_label_lower = str(scenario["asset_label"]).lower()
        postadj_total = _round_money(
            float(scenario["bank"]) + float(scenario["stock"]) + float(scenario["debtors"]) + float(scenario["asset_cost"]) + float(scenario["income_adjustment"]) + float(scenario["prepaid_adjustment"]) + adjusted_expense + adjusted_prepaid_balance + float(scenario["depreciation_amount"]) + float(scenario["cost_of_sales"])
        )
        postadj_prompt_tables = [
            {
                "heading": "Pre-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell(scenario["bank"]), _cell("")],
                    [_cell("Trading stock"), _cell(scenario["stock"]), _cell("")],
                    [_cell("Debtors control"), _cell(scenario["debtors"]), _cell("")],
                    [_cell(scenario["asset_label"]), _cell(scenario["asset_cost"]), _cell("")],
                    [_cell(scenario["expense_label"]), _cell(scenario["expense_base"]), _cell("")],
                    [_cell(scenario["prepaid_label"]), _cell(scenario["prepaid_base"]), _cell("")],
                    [_cell("Cost of Sales"), _cell(scenario["cost_of_sales"]), _cell("")],
                    [_cell("Sales"), _cell(""), _cell(scenario["sales"])],
                    [_cell(scenario["income_label"]), _cell(""), _cell(scenario["income_base"])],
                    [_cell("Creditors control"), _cell(""), _cell(scenario["creditors"])],
                    [_cell("Loan"), _cell(""), _cell(scenario["loan"])],
                    [_cell("Capital"), _cell(""), _cell(preadj_capital)],
                ],
            },
            {
                "heading": "Year-end adjustments",
                "headers": ["No.", "Adjustment"],
                "rows": [
                    [_cell("1"), _cell(f"{scenario['income_adjustment_label']}: R{int(scenario['income_adjustment']):,}")],
                    [_cell("2"), _cell(f"{scenario['prepaid_adjustment_label']}: R{int(scenario['prepaid_adjustment']):,}")],
                    [_cell("3"), _cell(f"{scenario['expense_adjustment_label']}: R{int(scenario['expense_adjustment']):,}")],
                    [_cell("4"), _cell(f"Depreciation on {str(scenario['asset_label']).lower()} to be recorded: R{int(scenario['depreciation_amount']):,}")],
                ],
            },
        ]
        postadj_table = {
            "heading": "Post-adjustment Trial Balance",
            "headers": ["Account", "Debit", "Credit"],
            "rows": [
                [_cell("Bank"), _cell("", editable=True, cell_id="patb-bank-debit"), _cell("")],
                [_cell("Trading stock"), _cell("", editable=True, cell_id="patb-stock-debit"), _cell("")],
                [_cell("Debtors control"), _cell("", editable=True, cell_id="patb-debtors-debit"), _cell("")],
                [_cell(scenario["asset_label"]), _cell("", editable=True, cell_id="patb-asset-debit"), _cell("")],
                [_cell("Accrued income"), _cell("", editable=True, cell_id="patb-accrued-income-debit"), _cell("")],
                [_cell("Prepaid expenses"), _cell("", editable=True, cell_id="patb-prepaid-debit"), _cell("")],
                [_cell(scenario["expense_label"]), _cell("", editable=True, cell_id="patb-expense-debit"), _cell("")],
                [_cell(scenario["prepaid_label"]), _cell("", editable=True, cell_id="patb-prepaid-account-debit"), _cell("")],
                [_cell("Depreciation"), _cell("", editable=True, cell_id="patb-depreciation-debit"), _cell("")],
                [_cell("Cost of Sales"), _cell("", editable=True, cell_id="patb-cos-debit"), _cell("")],
                [_cell("Sales"), _cell(""), _cell("", editable=True, cell_id="patb-sales-credit")],
                [_cell(scenario["income_label"]), _cell(""), _cell("", editable=True, cell_id="patb-income-credit")],
                [_cell("Accrued expenses"), _cell(""), _cell("", editable=True, cell_id="patb-accrued-expenses-credit")],
                [_cell(f"Accumulated depreciation on {str(scenario['asset_label']).lower()}"), _cell(""), _cell("", editable=True, cell_id="patb-accumdep-credit")],
                [_cell("Creditors control"), _cell(""), _cell("", editable=True, cell_id="patb-creditors-credit")],
                [_cell("Loan"), _cell(""), _cell("", editable=True, cell_id="patb-loan-credit")],
                [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="patb-capital-credit")],
                [_cell("Total"), _cell("", editable=True, cell_id="patb-total-debit"), _cell("", editable=True, cell_id="patb-total-credit")],
            ],
        }
        postadj_correct_map = {
            "patb-bank-debit": scenario["bank"],
            "patb-stock-debit": scenario["stock"],
            "patb-debtors-debit": scenario["debtors"],
            "patb-asset-debit": scenario["asset_cost"],
            "patb-accrued-income-debit": scenario["income_adjustment"],
            "patb-prepaid-debit": scenario["prepaid_adjustment"],
            "patb-expense-debit": adjusted_expense,
            "patb-prepaid-account-debit": adjusted_prepaid_balance,
            "patb-depreciation-debit": scenario["depreciation_amount"],
            "patb-cos-debit": scenario["cost_of_sales"],
            "patb-sales-credit": scenario["sales"],
            "patb-income-credit": adjusted_income,
            "patb-accrued-expenses-credit": scenario["expense_adjustment"],
            "patb-accumdep-credit": scenario["depreciation_amount"],
            "patb-creditors-credit": scenario["creditors"],
            "patb-loan-credit": scenario["loan"],
            "patb-capital-credit": preadj_capital,
            "patb-total-debit": postadj_total,
            "patb-total-credit": postadj_total,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="trial_balance_table",
            prompt=f"Use the Pre-adjustment Trial Balance and the year-end adjustments for {income_label_lower}, {prepaid_label_lower}, {expense_label_lower}, and depreciation on {asset_label_lower} to complete the Post-adjustment Trial Balance.",
            prompt_tables=postadj_prompt_tables,
            table=postadj_table,
            correct_map=postadj_correct_map,
            derivation_map={
                "patb-expense-debit": f"{scenario['expense_label']} after adjustment = old balance + accrued expense = R{int(scenario['expense_base']):,} + R{int(scenario['expense_adjustment']):,} = R{adjusted_expense:,}",
                "patb-prepaid-account-debit": f"{scenario['prepaid_label']} after adjustment = old balance - prepaid portion = R{int(scenario['prepaid_base']):,} - R{int(scenario['prepaid_adjustment']):,} = R{adjusted_prepaid_balance:,}",
                "patb-income-credit": f"{scenario['income_label']} after adjustment = old balance + accrued income = R{int(scenario['income_base']):,} + R{int(scenario['income_adjustment']):,} = R{adjusted_income:,}",
                "patb-total-debit": f"Add all adjusted debit balances to get R{postadj_total:,}",
            },
            cell_hints={
                "patb-asset-debit": f"Copy the {asset_label_lower} cost balance to the debit side; the reduction from depreciation goes to accumulated depreciation, not here.",
                "patb-accrued-income-debit": "Amounts still receivable appear as assets in the debit column.",
                "patb-prepaid-debit": "A prepaid expense is an asset, so it is debited in the trial balance.",
                "patb-expense-debit": f"Adjust the {expense_label_lower} account first before placing it in the debit column.",
                "patb-prepaid-account-debit": f"This is the adjusted balance of the {prepaid_label_lower} expense account after removing the prepaid portion.",
                "patb-income-credit": f"Increase {income_label_lower} by the amount still receivable before placing it on the credit side.",
                "patb-accrued-expenses-credit": "Outstanding expenses are liabilities and appear in the credit column.",
                "patb-accumdep-credit": "Accumulated depreciation is a contra-asset with a credit balance.",
                "patb-capital-credit": "Capital is copied from the pre-adjustment Trial Balance unless the question tells you to recalculate it.",
                "patb-total-debit": "Total all adjusted debit balances and make sure the credit column agrees.",
            },
            cell_teaching_map={
                "patb-asset-debit": _teaching_hint(
                    role_in_requirement=f"This cell places the {asset_label_lower} balance in the debit column of the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance shows {scenario['asset_label']} at R{int(scenario['asset_cost']):,} and the adjustments separately show depreciation.",
                    rule_or_principle="The asset account stays at cost on the debit side; accumulated depreciation carries the reduction separately on the credit side.",
                    how_to_derive=f"Copy the cost figure R{int(scenario['asset_cost']):,} into the debit column for {scenario['asset_label']}.",
                    transfer_tip="Do not reduce the asset account itself when the question uses accumulated depreciation as the contra-account.",
                ),
                "patb-accrued-income-debit": _teaching_hint(
                    role_in_requirement="This cell creates the new asset for income earned but not yet received.",
                    evidence_from_question=f"Adjustment 1 states {scenario['income_adjustment_label']}: R{int(scenario['income_adjustment']):,}.",
                    rule_or_principle="Accrued income is an asset and therefore appears in the debit column.",
                    how_to_derive=f"Enter the accrued portion R{int(scenario['income_adjustment']):,} as Accrued income in the debit column.",
                    transfer_tip="Whenever income is owing at year-end, create a separate asset for the amount receivable.",
                ),
                "patb-prepaid-debit": _teaching_hint(
                    role_in_requirement="This cell shows the asset created by the prepaid portion of an expense.",
                    evidence_from_question=f"Adjustment 2 states {scenario['prepaid_adjustment_label']}: R{int(scenario['prepaid_adjustment']):,}.",
                    rule_or_principle="A prepaid expense is a current asset because the business will benefit in the next period.",
                    how_to_derive=f"Enter the prepaid portion R{int(scenario['prepaid_adjustment']):,} as Prepaid expenses in the debit column.",
                    transfer_tip="Separate the prepaid asset from the adjusted expense-account balance; both can appear in the debit column.",
                ),
                "patb-expense-debit": _teaching_hint(
                    role_in_requirement=f"This cell shows the adjusted expense-account balance for {expense_label_lower}.",
                    evidence_from_question=f"Use the original {scenario['expense_label']} balance R{int(scenario['expense_base']):,} and the accrued amount R{int(scenario['expense_adjustment']):,}.",
                    rule_or_principle="Outstanding expenses increase the expense account for the current year.",
                    how_to_derive=f"R{int(scenario['expense_base']):,} + R{int(scenario['expense_adjustment']):,} = R{adjusted_expense:,}.",
                    transfer_tip="For accrued expenses, adjust the expense account upward and also create a liability for the same amount.",
                ),
                "patb-prepaid-account-debit": _teaching_hint(
                    role_in_requirement=f"This cell gives the remaining current-year expense for {prepaid_label_lower} after removing the prepaid part.",
                    evidence_from_question=f"Use the original {scenario['prepaid_label']} balance R{int(scenario['prepaid_base']):,} and the prepaid portion R{int(scenario['prepaid_adjustment']):,}.",
                    rule_or_principle="Prepaid expenses reduce the current-period expense because part of the payment belongs to the next year.",
                    how_to_derive=f"R{int(scenario['prepaid_base']):,} - R{int(scenario['prepaid_adjustment']):,} = R{adjusted_prepaid_balance:,}.",
                    transfer_tip="When an expense is paid in advance, split it into the current expense and the prepaid asset.",
                ),
                "patb-income-credit": _teaching_hint(
                    role_in_requirement=f"This cell shows the adjusted income-account balance for {income_label_lower}.",
                    evidence_from_question=f"Use the original {scenario['income_label']} balance R{int(scenario['income_base']):,} and the accrued amount R{int(scenario['income_adjustment']):,}.",
                    rule_or_principle="Income earned but not yet received still belongs to the current period and increases the income account.",
                    how_to_derive=f"R{int(scenario['income_base']):,} + R{int(scenario['income_adjustment']):,} = R{adjusted_income:,}.",
                    transfer_tip="For accrued income, increase the income account and create an asset for the same amount.",
                ),
                "patb-accrued-expenses-credit": _teaching_hint(
                    role_in_requirement="This cell creates the liability for expenses owing at year-end.",
                    evidence_from_question=f"Adjustment 3 states {scenario['expense_adjustment_label']}: R{int(scenario['expense_adjustment']):,}.",
                    rule_or_principle="Outstanding expenses are liabilities and appear in the credit column.",
                    how_to_derive=f"Enter the accrued portion R{int(scenario['expense_adjustment']):,} as Accrued expenses in the credit column.",
                    transfer_tip="When an expense is owing, you usually need both an increased expense and a new liability.",
                ),
                "patb-accumdep-credit": _teaching_hint(
                    role_in_requirement=f"This cell records accumulated depreciation on {asset_label_lower}.",
                    evidence_from_question=f"Adjustment 4 gives depreciation on {asset_label_lower}: R{int(scenario['depreciation_amount']):,}.",
                    rule_or_principle="Accumulated depreciation is a contra-asset and has a credit balance.",
                    how_to_derive=f"Enter the depreciation amount R{int(scenario['depreciation_amount']):,} as accumulated depreciation in the credit column.",
                    transfer_tip="In trial balance questions, depreciation expense and accumulated depreciation often appear together on opposite sides.",
                ),
                "patb-capital-credit": _teaching_hint(
                    role_in_requirement="This cell places the existing capital balance on the credit side.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance already shows Capital at R{int(preadj_capital):,}.",
                    rule_or_principle="Unless the question asks for a capital adjustment, copy the capital balance through to the trial balance.",
                    how_to_derive=f"Copy R{int(preadj_capital):,} to the credit column for Capital.",
                    transfer_tip="Only change capital when additional information such as drawings, net profit, or extra capital is given for that purpose.",
                ),
                "patb-total-debit": _teaching_hint(
                    role_in_requirement="This cell gives the final total of the adjusted debit column.",
                    evidence_from_question="Use every debit balance after you have processed the adjustments and placed each account in the correct column.",
                    rule_or_principle="A correctly adjusted trial balance must still balance: total debits = total credits.",
                    how_to_derive=f"Add the debit balances to get R{postadj_total:,} and check that the credit total matches.",
                    transfer_tip="Leave totals until the end so you can use them as a final self-check.",
                ),
            },
            guidelines=[
                "Adjust each affected account before placing it in the Post-adjustment Trial Balance.",
                "Include new asset and liability accounts created by the adjustments.",
                "The adjusted debit and credit totals must still agree.",
            ],
            marks=20,
        ), "post_adjustment_trial_balance_fill", expected_cells=19, total=postadj_total))

        preadj_total = _round_money(
            float(scenario["bank"]) + float(scenario["stock"]) + float(scenario["debtors"]) + float(scenario["asset_cost"]) + float(scenario["expense_base"]) + float(scenario["prepaid_base"]) + float(scenario["cost_of_sales"])
        )
        adjustment_total = _round_money(
            float(scenario["income_adjustment"]) + float(scenario["prepaid_adjustment"]) + float(scenario["expense_adjustment"]) + float(scenario["depreciation_amount"])
        )
        worksheet_table = {
            "heading": "Adjustment-columns worksheet extract",
            "headers": ["Account", "Pre-adjustment Debit", "Pre-adjustment Credit", "Adjustment Debit", "Adjustment Credit", "Post-adjustment Debit", "Post-adjustment Credit"],
            "rows": [
                [_cell("Bank"), _cell(scenario["bank"]), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-bank-post-dr"), _cell("")],
                [_cell("Trading stock"), _cell(scenario["stock"]), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-stock-post-dr"), _cell("")],
                [_cell("Debtors control"), _cell(scenario["debtors"]), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-debtors-post-dr"), _cell("")],
                [_cell(scenario["asset_label"]), _cell(scenario["asset_cost"]), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-asset-post-dr"), _cell("")],
                [_cell("Accrued income"), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-acc-inc-adj-dr"), _cell(""), _cell("", editable=True, cell_id="ws-acc-inc-post-dr"), _cell("")],
                [_cell("Prepaid expenses"), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-prepaid-asset-adj-dr"), _cell(""), _cell("", editable=True, cell_id="ws-prepaid-asset-post-dr"), _cell("")],
                [_cell(scenario["expense_label"]), _cell(scenario["expense_base"]), _cell(""), _cell("", editable=True, cell_id="ws-expense-adj-dr"), _cell(""), _cell("", editable=True, cell_id="ws-expense-post-dr"), _cell("")],
                [_cell(scenario["prepaid_label"]), _cell(scenario["prepaid_base"]), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-prepaid-account-adj-cr"), _cell("", editable=True, cell_id="ws-prepaid-account-post-dr"), _cell("")],
                [_cell("Depreciation"), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-dep-adj-dr"), _cell(""), _cell("", editable=True, cell_id="ws-dep-post-dr"), _cell("")],
                [_cell("Cost of Sales"), _cell(scenario["cost_of_sales"]), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-cos-post-dr"), _cell("")],
                [_cell("Sales"), _cell(""), _cell(scenario["sales"]), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-sales-post-cr")],
                [_cell(scenario["income_label"]), _cell(""), _cell(scenario["income_base"]), _cell(""), _cell("", editable=True, cell_id="ws-income-adj-cr"), _cell(""), _cell("", editable=True, cell_id="ws-income-post-cr")],
                [_cell("Accrued expenses"), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-acc-exp-adj-cr"), _cell(""), _cell("", editable=True, cell_id="ws-acc-exp-post-cr")],
                [_cell(f"Accumulated depreciation on {str(scenario['asset_label']).lower()}"), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-accumdep-adj-cr"), _cell(""), _cell("", editable=True, cell_id="ws-accumdep-post-cr")],
                [_cell("Creditors control"), _cell(""), _cell(scenario["creditors"]), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-creditors-post-cr")],
                [_cell("Loan"), _cell(""), _cell(scenario["loan"]), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-loan-post-cr")],
                [_cell("Capital"), _cell(""), _cell(preadj_capital), _cell(""), _cell(""), _cell(""), _cell("", editable=True, cell_id="ws-capital-post-cr")],
                [_cell("Totals"), _cell("", editable=True, cell_id="ws-total-pre-dr"), _cell("", editable=True, cell_id="ws-total-pre-cr"), _cell("", editable=True, cell_id="ws-total-adj-dr"), _cell("", editable=True, cell_id="ws-total-adj-cr"), _cell("", editable=True, cell_id="patb-total-debit"), _cell("", editable=True, cell_id="patb-total-credit")],
            ],
        }
        worksheet_correct_map = {
            "ws-bank-post-dr": scenario["bank"],
            "ws-stock-post-dr": scenario["stock"],
            "ws-debtors-post-dr": scenario["debtors"],
            "ws-asset-post-dr": scenario["asset_cost"],
            "ws-acc-inc-adj-dr": scenario["income_adjustment"],
            "ws-acc-inc-post-dr": scenario["income_adjustment"],
            "ws-prepaid-asset-adj-dr": scenario["prepaid_adjustment"],
            "ws-prepaid-asset-post-dr": scenario["prepaid_adjustment"],
            "ws-expense-adj-dr": scenario["expense_adjustment"],
            "ws-expense-post-dr": adjusted_expense,
            "ws-prepaid-account-adj-cr": scenario["prepaid_adjustment"],
            "ws-prepaid-account-post-dr": adjusted_prepaid_balance,
            "ws-dep-adj-dr": scenario["depreciation_amount"],
            "ws-dep-post-dr": scenario["depreciation_amount"],
            "ws-cos-post-dr": scenario["cost_of_sales"],
            "ws-sales-post-cr": scenario["sales"],
            "ws-income-adj-cr": scenario["income_adjustment"],
            "ws-income-post-cr": adjusted_income,
            "ws-acc-exp-adj-cr": scenario["expense_adjustment"],
            "ws-acc-exp-post-cr": scenario["expense_adjustment"],
            "ws-accumdep-adj-cr": scenario["depreciation_amount"],
            "ws-accumdep-post-cr": scenario["depreciation_amount"],
            "ws-creditors-post-cr": scenario["creditors"],
            "ws-loan-post-cr": scenario["loan"],
            "ws-capital-post-cr": preadj_capital,
            "ws-total-pre-dr": preadj_total,
            "ws-total-pre-cr": preadj_total,
            "ws-total-adj-dr": adjustment_total,
            "ws-total-adj-cr": adjustment_total,
            "patb-total-debit": postadj_total,
            "patb-total-credit": postadj_total,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="trial_balance_table",
            prompt=f"Use the worksheet-style adjustment columns to process the year-end adjustments for {income_label_lower}, {prepaid_label_lower}, {expense_label_lower}, and depreciation on {asset_label_lower}. Complete the adjustment columns and the post-adjustment columns.",
            prompt_tables=postadj_prompt_tables,
            table=worksheet_table,
            correct_map=worksheet_correct_map,
            derivation_map={
                "ws-expense-post-dr": f"Adjusted {scenario['expense_label']} = R{int(scenario['expense_base']):,} + R{int(scenario['expense_adjustment']):,} = R{int(adjusted_expense):,}",
                "ws-prepaid-account-post-dr": f"Adjusted {scenario['prepaid_label']} = R{int(scenario['prepaid_base']):,} - R{int(scenario['prepaid_adjustment']):,} = R{int(adjusted_prepaid_balance):,}",
                "ws-income-post-cr": f"Adjusted {scenario['income_label']} = R{int(scenario['income_base']):,} + R{int(scenario['income_adjustment']):,} = R{int(adjusted_income):,}",
                "patb-total-debit": f"Add the final post-adjustment debit balances to get R{int(postadj_total):,}",
            },
            cell_hints={
                "ws-acc-inc-adj-dr": "Place the accrued income amount in the adjustment debit column because it creates an asset.",
                "ws-prepaid-account-adj-cr": f"Credit the {prepaid_label_lower} account in the adjustment columns to remove the prepaid portion from the current-period expense.",
                "ws-income-adj-cr": f"Credit the {income_label_lower} account in the adjustment columns because accrued income increases the income account.",
                "ws-acc-exp-adj-cr": "Outstanding expenses create a liability, so they go in the adjustment credit column.",
                "ws-total-adj-dr": "The total of the adjustment debit column must equal the total of the adjustment credit column.",
                "patb-total-debit": "After transferring all balances to the post-adjustment columns, total the final debit column and check it agrees with the credit total.",
            },
            cell_teaching_map={
                "ws-acc-inc-adj-dr": _teaching_hint(
                    role_in_requirement="This cell places the accrued-income adjustment in the worksheet adjustment columns.",
                    evidence_from_question=f"Adjustment 1 states {scenario['income_adjustment_label']}: R{int(scenario['income_adjustment']):,}.",
                    rule_or_principle="In worksheet columns, accrued income is debited as an asset and credited to the related income account.",
                    how_to_derive=f"Write R{int(scenario['income_adjustment']):,} in the adjustment debit column for Accrued income.",
                    transfer_tip="When using adjustment columns, first identify the double entry, then place each side in the correct adjustment column before extending balances to the final columns.",
                ),
                "ws-prepaid-account-post-dr": _teaching_hint(
                    role_in_requirement=f"This cell shows the remaining current-year expense for {prepaid_label_lower} after the adjustment columns are processed.",
                    evidence_from_question=f"The pre-adjustment balance is R{int(scenario['prepaid_base']):,} and the prepaid portion is R{int(scenario['prepaid_adjustment']):,}.",
                    rule_or_principle="A prepaid expense reduces the current-period expense and creates a separate asset.",
                    how_to_derive=f"Subtract the adjustment credit from the pre-adjustment debit: R{int(scenario['prepaid_base']):,} - R{int(scenario['prepaid_adjustment']):,} = R{int(adjusted_prepaid_balance):,}.",
                    transfer_tip="In a worksheet, compare the pre-adjustment and adjustment columns account by account to determine the final balance that extends to the post-adjustment columns.",
                ),
                "ws-total-adj-dr": _teaching_hint(
                    role_in_requirement="This cell totals the worksheet adjustment debit column.",
                    evidence_from_question="All four year-end adjustments must be entered in the adjustment columns before the worksheet can balance.",
                    rule_or_principle="The adjustment debit and adjustment credit columns must balance because each adjustment is a double entry.",
                    how_to_derive=f"Add the four adjustment debits: R{int(scenario['income_adjustment']):,} + R{int(scenario['prepaid_adjustment']):,} + R{int(scenario['expense_adjustment']):,} + R{int(scenario['depreciation_amount']):,} = R{int(adjustment_total):,}.",
                    transfer_tip="Before moving to the final columns, always check whether the worksheet adjustment columns themselves balance.",
                ),
            },
            guidelines=[
                "Place each side of every year-end adjustment in the adjustment columns before extending balances to the final columns.",
                "If an account has both a pre-adjustment balance and an adjustment, combine them to determine the post-adjustment balance.",
                "The pre-adjustment totals, adjustment totals, and post-adjustment totals should each balance across debit and credit columns.",
            ],
            marks=28,
        ), "post_adjustment_trial_balance_worksheet_fill", expected_cells=31, cell_expectations=worksheet_correct_map))

    pool.append(_make_mcq(
        prompt="What appears on a Post-closing Trial Balance?",
        options=[
            "All income and expense accounts with their balances.",
            "Only Balance Sheet accounts (assets, liabilities, capital) — all income and expense accounts are closed.",
            "Only the Trading account and Profit & Loss account.",
            "The same accounts as the Pre-adjustment Trial Balance.",
        ],
        correct_index=1,
        explanation="After closing transfers, all income and expense accounts have zero balances. The Post-closing Trial Balance only contains Balance Sheet items (assets, owner's equity, liabilities).",
    ))

    pool.append(_make_mcq(
        prompt="What is the purpose of the Pre-adjustment Trial Balance?",
        options=[
            "To determine the net profit before adjustments.",
            "To check that total debits equal total credits before year-end adjustments are processed.",
            "To prepare the Income Statement.",
            "To close all nominal accounts.",
        ],
        correct_index=1,
        explanation="The Pre-adjustment Trial Balance verifies that debits = credits before any year-end adjustments are processed.",
    ))

    pool.append(_make_mcq(
        prompt="Which of these accounts will NOT appear on a Post-closing Trial Balance?",
        options=[
            "Capital",
            "Vehicles",
            "Wages (expense)",
            "Creditors control",
        ],
        correct_index=2,
        explanation="Wages is an expense (nominal account) — it is closed to the P&L account during closing transfers and does not appear on the Post-closing Trial Balance.",
    ))

    pool.append(_with_validation(_make_typed(
        prompt="Explain why certain year-end adjustments (accruals, income received in advance, prepayments) must be reversed at the beginning of the next financial period.",
        sample_answer="These adjustments were made to ensure correct matching at year-end. At the start of the new year, they must be reversed so that when the actual payment/receipt occurs, it is correctly allocated to the new period. Without reversal, amounts would be double-counted.",
        grading_rubric=["correct matching at year-end", "reversed at start of new year", "avoid double-counting"],
    ), "reversals_explain_typed", minimum_parts=1))

    return pool
