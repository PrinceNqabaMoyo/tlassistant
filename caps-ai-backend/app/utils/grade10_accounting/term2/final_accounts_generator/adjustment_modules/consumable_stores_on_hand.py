from __future__ import annotations

import random
from typing import Any, Dict, List

from .....sole_trader.names import pick_business_name as _pick_business_name
from .....sole_trader.names import pick_person_names as _pick_person_names
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
def _gen_consumable_stores_on_hand(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    biz = _pick_business_name(r=r)
    keeper_name, owner_name = _pick_person_names(r=r, k=2)

    calc_purchased = r.choice([3600, 4200, 5400, 6800])
    calc_on_hand = r.choice([450, 600, 750, 900])
    while float(calc_on_hand) >= float(calc_purchased):
        calc_on_hand = r.choice([450, 600, 750, 900])
    calc_used = _round_money(float(calc_purchased) - float(calc_on_hand))
    pool.append(_with_validation(_make_calc(
        prompt=f"{biz} bought consumable stores costing R{int(calc_purchased):,} during the year. {keeper_name} counted consumable stores on hand of R{int(calc_on_hand):,} at year-end.\n\nCalculate the consumable stores expense for the year.",
        correct_answer=calc_used,
        working_formula=f"Consumable stores expense = Purchased - On hand = R{int(calc_purchased):,} - R{int(calc_on_hand):,}",
        formula_hint="Consumable stores expense = purchases during the year - consumable stores on hand",
    ), "consumable_stores_used_calc", purchased=calc_purchased, on_hand=calc_on_hand))

    scenarios = [
        {
            "expense_label": "Stationery",
            "amount": 600,
            "base_balance": 4200,
            "bank": 56000,
            "stock": 34000,
            "year_end_date": "28 Feb 2026",
            "reversal_date": "1 Mar 2026",
            "prompt_intro": f"{keeper_name} completed the year-end stationery count for {biz} and found consumable stores on hand of R600.",
        },
        {
            "expense_label": "Packing material",
            "amount": 850,
            "base_balance": 6100,
            "bank": 62000,
            "stock": 38000,
            "year_end_date": "30 Jun 2026",
            "reversal_date": "1 Jul 2026",
            "prompt_intro": f"At {biz}, {owner_name} approved the year-end packing-material count. Consumable stores on hand amount to R850.",
        },
        {
            "expense_label": "Cleaning materials",
            "amount": 700,
            "base_balance": 5000,
            "bank": 59000,
            "stock": 36000,
            "year_end_date": "31 Dec 2026",
            "reversal_date": "1 Jan 2027",
            "prompt_intro": f"{biz} counted unused cleaning materials at year-end. {keeper_name} confirmed consumable stores on hand of R700.",
        },
    ]

    for scenario in scenarios:
        expense_label = str(scenario["expense_label"])
        amount = _round_money(float(scenario["amount"]))
        adjusted_balance = _round_money(float(scenario["base_balance"]) - float(amount))
        tb_total = _round_money(float(scenario["bank"]) + float(scenario["stock"]) + float(adjusted_balance) + float(amount))
        capital = tb_total

        prompt_table = {
            "heading": "Consumable stores source note",
            "headers": ["Item", "Amount / detail"],
            "rows": [
                [_cell(f"{expense_label} balance before adjustment"), _cell(scenario["base_balance"])],
                [_cell("Consumable stores on hand at year-end"), _cell(amount)],
                [_cell("Reversal required next period"), _cell("Yes")],
            ],
        }

        journal_table = {
            "heading": "General Journal: consumable stores adjustment and reversal",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="cons-j-dr-details"), _cell("", editable=True, cell_id="cons-j-dr-amount"), _cell("")],
                [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="cons-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="cons-j-cr-amount")],
                [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="cons-j-rev-dr-details"), _cell("", editable=True, cell_id="cons-j-rev-dr-amount"), _cell("")],
                [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="cons-j-rev-cr-details"), _cell(""), _cell("", editable=True, cell_id="cons-j-rev-cr-amount")],
            ],
        }
        journal_correct_map = {
            "cons-j-dr-details": "Consumable stores on hand",
            "cons-j-dr-amount": amount,
            "cons-j-cr-details": expense_label,
            "cons-j-cr-amount": amount,
            "cons-j-rev-dr-details": expense_label,
            "cons-j-rev-dr-amount": amount,
            "cons-j-rev-cr-details": "Consumable stores on hand",
            "cons-j-rev-cr-amount": amount,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=f"{scenario['prompt_intro']} Prepare the General Journal entry for the year-end adjustment dated {scenario['year_end_date']} and the reversal on {scenario['reversal_date']}.",
            prompt_table=prompt_table,
            table=journal_table,
            correct_map=journal_correct_map,
            derivation_map={
                "cons-j-dr-amount": f"Use the consumable stores on hand amount given: R{int(amount):,}.",
                "cons-j-rev-dr-amount": f"The reversal uses the same amount as the year-end adjustment: R{int(amount):,}.",
            },
            cell_hints={
                "cons-j-dr-details": "At year-end, the unused consumable stores become an asset on hand.",
                "cons-j-cr-details": f"Credit {expense_label} to remove the unused portion from this year's expense.",
                "cons-j-rev-dr-details": f"The reversal next period debits the original expense account: {expense_label}.",
                "cons-j-rev-cr-details": "The reversal credits the consumable-stores-on-hand asset account.",
            },
            cell_teaching_map={
                "cons-j-dr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the debit account for the year-end consumable-stores adjustment.",
                    evidence_from_question=f"The source note says unused {expense_label.lower()} worth R{int(amount):,} is still on hand at year-end.",
                    rule_or_principle="Consumable stores not yet used are carried forward as an asset called Consumable stores on hand.",
                    method_or_formula="Year-end adjustment: Dr Consumable stores on hand / Cr expense account.",
                    record_link="This same amount will appear later in the Balance Sheet / statement carry-through and the Post-adjustment Trial Balance as an asset.",
                    how_to_derive="Debit Consumable stores on hand because the unused portion is an asset for the next period.",
                    transfer_tip="If part of consumable purchases remains unused at year-end, move that portion out of expense and into an asset account.",
                ),
                "cons-j-cr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the expense account credited to remove the unused portion from the current year.",
                    evidence_from_question=f"The pre-adjustment {expense_label} balance includes goods that are still on hand and therefore not consumed this year.",
                    rule_or_principle="The current-year expense must only reflect the portion actually used during the year.",
                    method_or_formula=f"Credit {expense_label} with the stores-on-hand amount.",
                    record_link="This credit reduces the expense balance to the adjusted amount that is carried to the Income Statement.",
                    how_to_derive=f"Credit {expense_label} because the unused amount must be removed from this year's expense total.",
                    transfer_tip="The year-end asset adjustment reduces the matching expense by exactly the same amount.",
                ),
                "cons-j-rev-cr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the credit account for the reversal on the first day of the next period.",
                    evidence_from_question=f"The question explicitly requires the reversal on {scenario['reversal_date']}.",
                    rule_or_principle="A reversal posts the original adjustment on the opposite sides so the next period can record usage normally.",
                    method_or_formula="Reversal: Dr expense account / Cr Consumable stores on hand.",
                    record_link="The reversal clears the temporary year-end asset created by the adjustment entry.",
                    how_to_derive="Because the original year-end entry debited Consumable stores on hand, the reversal credits that same account.",
                    transfer_tip="For reversal entries, use the same account pair and amount as the year-end adjustment, but swap the debit and credit sides.",
                ),
            },
            working_map={
                "cons-j-dr-details": "Treat the stores count as the unused portion that must be carried forward as an asset.",
                "cons-j-cr-details": f"The same amount is removed from {expense_label} so that only the used portion remains in this year's expense.",
                "cons-j-rev-cr-details": "The reversal clears the year-end asset so the next period can record actual usage without duplication.",
            },
            guidelines=[
                "Year-end: debit Consumable stores on hand and credit the related expense account.",
                "Reversal next period: debit the expense account and credit Consumable stores on hand.",
                "Use the same stores-on-hand amount throughout the journal and reversal.",
            ],
            marks=8,
        ), "consumable_stores_reversal_journal_fill", expected_cells=8, amount=amount, amount_cell_ids=["cons-j-dr-amount", "cons-j-cr-amount", "cons-j-rev-dr-amount", "cons-j-rev-cr-amount"]))

        analysis_table = {
            "heading": "Adjustment analysis: consumable stores on hand",
            "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
            "rows": [
                [_cell(f"Unused {expense_label.lower()} on hand at year-end"), _cell("", editable=True, cell_id="cons-a-amount"), _cell("", editable=True, cell_id="cons-a-dr"), _cell("", editable=True, cell_id="cons-a-cr"), _cell("", editable=True, cell_id="cons-a-is"), _cell("", editable=True, cell_id="cons-a-bs")],
            ],
        }
        analysis_correct_map = {
            "cons-a-amount": amount,
            "cons-a-dr": "Consumable stores on hand",
            "cons-a-cr": expense_label,
            "cons-a-is": "Expense decreases by R" + f"{int(amount):,}",
            "cons-a-bs": "Current asset increases by R" + f"{int(amount):,}",
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="adjustment_analysis_table",
            prompt=f"{scenario['prompt_intro']} Complete the adjustment analysis table for consumable stores on hand.",
            prompt_table=prompt_table,
            table=analysis_table,
            correct_map=analysis_correct_map,
            derivation_map={
                "cons-a-amount": f"Use the stores-on-hand amount from the count sheet: R{int(amount):,}.",
            },
            cell_hints={
                "cons-a-dr": "The unused portion becomes an asset on hand.",
                "cons-a-cr": f"Credit {expense_label} to reduce the expense for the amount not yet used.",
                "cons-a-is": "Unused consumable stores reduce this year's expense.",
                "cons-a-bs": "Stores on hand at year-end are shown as a current asset.",
            },
            cell_teaching_map={
                "cons-a-is": _teaching_hint(
                    role_in_requirement="This cell explains the Income Statement effect of consumable stores on hand.",
                    evidence_from_question=f"The source note says R{int(amount):,} of {expense_label.lower()} remains unused at year-end.",
                    rule_or_principle="Only the portion consumed during the current year should remain as an expense of the period.",
                    method_or_formula=f"Decrease {expense_label} by the unused portion R{int(amount):,}.",
                    record_link="This effect must match the credit to the expense account in the journal and ledger, and the adjusted expense carried to the Income Statement.",
                    how_to_derive=f"Because the unused amount is not this year's expense, show that expense decreases by R{int(amount):,}.",
                    transfer_tip="When stock of consumables remains on hand, the Income Statement effect is usually a decrease in the related expense.",
                ),
                "cons-a-bs": _teaching_hint(
                    role_in_requirement="This cell explains the Balance Sheet effect of the year-end consumable-stores count.",
                    evidence_from_question=f"The unused portion of R{int(amount):,} still has future benefit for the business.",
                    rule_or_principle="Consumable stores on hand are current assets because they will be used in a later period.",
                    method_or_formula="Carry the stores-on-hand amount to a current-asset category.",
                    record_link="This Balance Sheet effect must match the debit to Consumable stores on hand and the carry-through extract.",
                    how_to_derive=f"Show that current assets increase by R{int(amount):,}.",
                    transfer_tip="If the business still holds usable supplies at year-end, expect a current-asset effect.",
                ),
            },
            working_map={
                "cons-a-is": "The analysis follows from moving the unused amount out of expense and into a stores-on-hand asset.",
                "cons-a-bs": "The same amount that leaves expense becomes a current asset for the next period.",
            },
            guidelines=[
                "Use the same stores-on-hand amount across the double entry and the statement effects.",
                "Consumable stores on hand reduce the expense and increase current assets.",
            ],
            marks=6,
        ), "consumable_stores_analysis_fill", expected_cells=5, amount=amount, amount_cell_id="cons-a-amount"))

        ledger_tables = [
            {
                "heading": "Consumable stores on hand account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="cons-l-asset-dr-details"), _cell("GJ"), _cell("", editable=True, cell_id="cons-l-asset-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="cons-l-asset-rev-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="cons-l-asset-rev-amount")],
                ],
            },
            {
                "heading": f"{expense_label} account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="cons-l-exp-cr-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="cons-l-exp-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="cons-l-exp-rev-details"), _cell("GJ"), _cell("", editable=True, cell_id="cons-l-exp-rev-amount"), _cell("")],
                ],
            },
        ]
        ledger_correct_map = {
            "cons-l-asset-dr-details": expense_label,
            "cons-l-asset-dr-amount": amount,
            "cons-l-asset-rev-details": expense_label,
            "cons-l-asset-rev-amount": amount,
            "cons-l-exp-cr-details": "Consumable stores on hand",
            "cons-l-exp-cr-amount": amount,
            "cons-l-exp-rev-details": "Consumable stores on hand",
            "cons-l-exp-rev-amount": amount,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="ledger",
            prompt=f"{scenario['prompt_intro']} Post the year-end consumable-stores adjustment dated {scenario['year_end_date']} and the reversal on {scenario['reversal_date']} to the ledger accounts shown.",
            prompt_table=prompt_table,
            tables=ledger_tables,
            correct_map=ledger_correct_map,
            derivation_map={
                "cons-l-asset-dr-amount": f"Use the stores-on-hand amount from the count sheet: R{int(amount):,}.",
                "cons-l-asset-rev-amount": f"Reverse the same stores-on-hand amount on {scenario['reversal_date']}: R{int(amount):,}.",
            },
            cell_hints={
                "cons-l-asset-dr-details": f"In the Consumable stores on hand account, the details column shows the opposite account: {expense_label}.",
                "cons-l-asset-rev-details": f"On reversal, the Consumable stores on hand account still uses {expense_label} as the opposite account.",
                "cons-l-exp-cr-details": "In the expense account, the details column shows the stores-on-hand asset account.",
                "cons-l-exp-cr-amount": "Use the same stores-on-hand amount credited in the year-end journal entry.",
                "cons-l-exp-rev-details": "The reversal keeps the same opposite account in the details column.",
                "cons-l-exp-rev-amount": "The reversal uses the same amount as the original year-end adjustment.",
            },
            cell_teaching_map={
                "cons-l-asset-dr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the opposite account for the year-end debit in the Consumable stores on hand ledger account.",
                    evidence_from_question=f"The year-end adjustment is Dr Consumable stores on hand / Cr {expense_label}.",
                    rule_or_principle="In a ledger account, the details column records the account used on the other side of the double entry.",
                    method_or_formula=f"Because Consumable stores on hand is debited against {expense_label}, write {expense_label} in the details column.",
                    record_link="This ledger posting must agree with the General Journal adjustment entry.",
                    how_to_derive=f"Use {expense_label} as the opposite account for the debit posting.",
                    transfer_tip="When posting to ledger, identify the opposite account from the journal before filling the details column.",
                ),
                "cons-l-asset-rev-details": _teaching_hint(
                    role_in_requirement="This cell identifies the opposite account for the reversal credit in the Consumable stores on hand ledger account.",
                    evidence_from_question=f"The question includes a reversal on {scenario['reversal_date']} after the original year-end entry.",
                    rule_or_principle="A reversal uses the same two accounts as the original adjustment, but the debit and credit sides switch.",
                    method_or_formula=f"Reversal: Dr {expense_label} / Cr Consumable stores on hand.",
                    record_link="This reversal clears the temporary asset raised at year-end.",
                    how_to_derive=f"Because the reversal still pairs Consumable stores on hand with {expense_label}, write {expense_label} in the details column.",
                    transfer_tip="For reversal ledger postings, keep the same account pair but reverse the side used by each account.",
                ),
                "cons-l-exp-cr-amount": _teaching_hint(
                    role_in_requirement="This cell records the amount credited to the expense account at year-end.",
                    evidence_from_question=f"The unused {expense_label.lower()} on hand amounts to R{int(amount):,}.",
                    rule_or_principle="The unused portion is removed from the current-year expense and carried forward as an asset.",
                    method_or_formula=f"Credit {expense_label} with R{int(amount):,}.",
                    record_link="This reduced expense balance is the amount later carried into the Income Statement extract.",
                    how_to_derive=f"Use the stores-on-hand amount R{int(amount):,} as the credit to {expense_label}.",
                    transfer_tip="Whenever an unused portion remains on hand, that same amount leaves the expense account.",
                ),
                "cons-l-exp-rev-amount": _teaching_hint(
                    role_in_requirement="This cell records the debit amount posted back to the expense account when the adjustment is reversed.",
                    evidence_from_question=f"The question explicitly requires reversal of the stores-on-hand entry on {scenario['reversal_date']}.",
                    rule_or_principle="Reversal entries repeat the original amount but swap the debit and credit sides in the next period.",
                    method_or_formula=f"Debit {expense_label} with the same amount: R{int(amount):,}.",
                    record_link="This restores the expense account so next-period usage can be recorded normally without double counting.",
                    how_to_derive=f"Use the same stores-on-hand amount R{int(amount):,} that was used in the year-end adjustment.",
                    transfer_tip="Unless the question says otherwise, a reversal uses exactly the same amount as the original adjusting entry.",
                ),
            },
            working_map={
                "cons-l-asset-dr-details": "The asset account records the unused stores being carried forward to the next period.",
                "cons-l-exp-cr-amount": f"The expense account is reduced by the unused {expense_label.lower()} portion so only the used amount remains.",
                "cons-l-asset-rev-details": "The reversal removes the temporary year-end asset using the same paired expense account.",
                "cons-l-exp-rev-amount": f"The next period starts by restoring R{int(amount):,} to {expense_label} through the reversal entry.",
                "cons-l-exp-rev-details": "The reversal clears the year-end asset so the next period can record actual usage without duplication.",
            },
            guidelines=[
                f"Year-end: Dr Consumable stores on hand / Cr {expense_label}.",
                f"Reversal next period: Dr {expense_label} / Cr Consumable stores on hand.",
                "Use the stores-count amount consistently in both ledger accounts.",
            ],
            marks=8,
        ), "consumable_stores_reversal_ledger_fill", expected_cells=8, cell_expectations=ledger_correct_map))

        carry_tables = [
            {
                "heading": "Income Statement extract",
                "headers": ["Expense", "Amount"],
                "rows": [[_cell(expense_label), _cell("", editable=True, cell_id="cons-fa-expense")]],
            },
            {
                "heading": "Balance Sheet extract",
                "headers": ["Current assets", "Amount"],
                "rows": [[_cell("Consumable stores on hand"), _cell("", editable=True, cell_id="cons-fa-asset")]],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the consumable-stores source note for {biz} to carry the year-end effect into the Income Statement and Balance Sheet extracts.",
            prompt_table=prompt_table,
            tables=carry_tables,
            correct_map={
                "cons-fa-expense": adjusted_balance,
                "cons-fa-asset": amount,
            },
            derivation_map={
                "cons-fa-expense": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} - R{int(amount):,} = R{int(adjusted_balance):,}.",
                "cons-fa-asset": f"Carry the unused stores amount to Consumable stores on hand: R{int(amount):,}.",
            },
            cell_hints={
                "cons-fa-expense": "Subtract the stores on hand from the pre-adjustment expense balance.",
                "cons-fa-asset": "The unused portion appears as a current asset in the Balance Sheet.",
            },
            cell_teaching_map={
                "cons-fa-expense": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {expense_label.lower()} amount into the Income Statement extract.",
                    evidence_from_question=f"The source note gives a pre-adjustment {expense_label} balance of R{int(scenario['base_balance']):,} and stores on hand of R{int(amount):,}.",
                    rule_or_principle="The Income Statement must show only the portion of consumable stores used during the period.",
                    method_or_formula=f"Adjusted {expense_label} = pre-adjustment balance - consumable stores on hand.",
                    record_link="This adjusted amount must match the reduced expense balance after the credit entry in the journal and ledger.",
                    how_to_derive=f"Subtract R{int(amount):,} from R{int(scenario['base_balance']):,} to get R{int(adjusted_balance):,}.",
                    transfer_tip="For stores-on-hand adjustments, the Income Statement receives the expense after the unused portion has been removed.",
                ),
                "cons-fa-asset": _teaching_hint(
                    role_in_requirement="This cell carries the unused consumable stores amount to the Balance Sheet.",
                    evidence_from_question=f"The count sheet confirms consumable stores on hand of R{int(amount):,} at year-end.",
                    rule_or_principle="Unused consumable stores are current assets because they will benefit a later accounting period.",
                    method_or_formula="Carry the year-end stores-on-hand amount to the Balance Sheet asset section.",
                    record_link="This amount must match the debit to Consumable stores on hand in the journal and ledger, and the Post-adjustment Trial Balance asset line.",
                    how_to_derive=f"Use the counted amount R{int(amount):,} as the Balance Sheet asset figure.",
                    transfer_tip="If consumables remain unused at year-end, carry only the unused portion to the Balance Sheet, not the full expense balance.",
                ),
            },
            working_map={
                "cons-fa-expense": "The adjusted expense is the used portion after the stores-on-hand amount has been removed.",
                "cons-fa-asset": "The Balance Sheet receives the unused portion as a current asset for the next period.",
            },
            guidelines=[
                "Carry the adjusted expense balance to the Income Statement.",
                "Carry the stores-on-hand amount to the Balance Sheet as a current asset.",
            ],
            marks=4,
        ), "consumable_stores_carrythrough_fill", expected_cells=2, adjusted_amount=adjusted_balance, carry_amount=amount, adjusted_cell_id="cons-fa-expense", carry_cell_id="cons-fa-asset"))

        patb_prompt_tables = [
            {
                "heading": "Pre-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell(scenario["bank"]), _cell("")],
                    [_cell("Trading stock"), _cell(scenario["stock"]), _cell("")],
                    [_cell(expense_label), _cell(scenario["base_balance"]), _cell("")],
                    [_cell("Capital"), _cell(""), _cell(capital)],
                ],
            },
            prompt_table,
        ]
        patb_table = {
            "heading": "Post-adjustment Trial Balance extract",
            "headers": ["Account", "Debit", "Credit"],
            "rows": [
                [_cell("Bank"), _cell("", editable=True, cell_id="cons-patb-bank-debit"), _cell("")],
                [_cell("Trading stock"), _cell("", editable=True, cell_id="cons-patb-stock-debit"), _cell("")],
                [_cell(expense_label), _cell("", editable=True, cell_id="cons-patb-expense-debit"), _cell("")],
                [_cell("Consumable stores on hand"), _cell("", editable=True, cell_id="cons-patb-asset-debit"), _cell("")],
                [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="cons-patb-capital-credit")],
                [_cell("Total"), _cell("", editable=True, cell_id="cons-patb-total-debit"), _cell("", editable=True, cell_id="cons-patb-total-credit")],
            ],
        }
        patb_correct_map = {
            "cons-patb-bank-debit": scenario["bank"],
            "cons-patb-stock-debit": scenario["stock"],
            "cons-patb-expense-debit": adjusted_balance,
            "cons-patb-asset-debit": amount,
            "cons-patb-capital-credit": capital,
            "cons-patb-total-debit": tb_total,
            "cons-patb-total-credit": tb_total,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="trial_balance_table",
            prompt=f"Use the Pre-adjustment Trial Balance extract and the consumable-stores count for {biz} to complete the Post-adjustment Trial Balance extract.",
            prompt_tables=patb_prompt_tables,
            table=patb_table,
            correct_map=patb_correct_map,
            derivation_map={
                "cons-patb-expense-debit": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} - R{int(amount):,} = R{int(adjusted_balance):,}.",
                "cons-patb-total-debit": f"Total debit = Bank + Trading stock + adjusted {expense_label} + Consumable stores on hand = R{int(scenario['bank']):,} + R{int(scenario['stock']):,} + R{int(adjusted_balance):,} + R{int(amount):,} = R{int(tb_total):,}.",
                "cons-patb-total-credit": f"Total credit must match the completed debit total in the Post-adjustment Trial Balance: R{int(tb_total):,}.",
            },
            cell_hints={
                "cons-patb-expense-debit": f"Reduce the {expense_label} balance by the stores on hand before placing it in the adjusted trial balance.",
                "cons-patb-asset-debit": "Add Consumable stores on hand as a new asset in the debit column.",
                "cons-patb-total-debit": "Total the debit column only after inserting the adjusted expense and new asset balance.",
                "cons-patb-total-credit": "The credit total must equal the completed debit total once all balances have been entered.",
            },
            cell_teaching_map={
                "cons-patb-expense-debit": _teaching_hint(
                    role_in_requirement=f"This cell shows the adjusted {expense_label.lower()} balance in the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance gives {expense_label} at R{int(scenario['base_balance']):,}, and the stores count removes R{int(amount):,} from that balance.",
                    rule_or_principle="The Post-adjustment Trial Balance includes the adjusted expense after the stores-on-hand amount has been transferred to an asset account.",
                    method_or_formula=f"Adjusted {expense_label} = original balance - stores on hand.",
                    record_link="This amount must match the Income Statement carry-through figure and the reduced expense after the journal / ledger adjustment.",
                    how_to_derive=f"Subtract R{int(amount):,} from R{int(scenario['base_balance']):,} to get R{int(adjusted_balance):,}.",
                    transfer_tip="Update the original expense balance first, then place the adjusted figure in the Post-adjustment Trial Balance.",
                ),
                "cons-patb-asset-debit": _teaching_hint(
                    role_in_requirement="This cell adds the stores-on-hand asset to the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The year-end count created Consumable stores on hand of R{int(amount):,}.",
                    rule_or_principle="A new asset created by the adjustment must appear in the debit column of the Post-adjustment Trial Balance.",
                    method_or_formula="Enter Consumable stores on hand at the year-end counted amount.",
                    record_link="This asset amount must agree with the journal debit, ledger asset account, and Balance Sheet carry-through figure.",
                    how_to_derive=f"Use the counted stores-on-hand amount R{int(amount):,} as the new debit balance.",
                    transfer_tip="Whenever an adjustment creates a new asset, check whether it needs to be inserted as a fresh line in the adjusted trial balance.",
                ),
                "cons-patb-total-debit": _teaching_hint(
                    role_in_requirement="This cell totals the debit column of the Post-adjustment Trial Balance after the adjustment has been carried through.",
                    evidence_from_question=f"The completed debit side contains Bank R{int(scenario['bank']):,}, Trading stock R{int(scenario['stock']):,}, adjusted {expense_label} R{int(adjusted_balance):,}, and Consumable stores on hand R{int(amount):,}.",
                    rule_or_principle="The total row is completed only after every adjusted balance and new asset line has been entered.",
                    method_or_formula=f"R{int(scenario['bank']):,} + R{int(scenario['stock']):,} + R{int(adjusted_balance):,} + R{int(amount):,} = R{int(tb_total):,}.",
                    record_link="This debit total must equal the credit total in the completed Post-adjustment Trial Balance.",
                    how_to_derive="Add all completed debit balances after the adjustment has been processed.",
                    transfer_tip="Leave totals until last so you do not omit a new adjustment line or use an unadjusted balance.",
                ),
                "cons-patb-total-credit": _teaching_hint(
                    role_in_requirement="This cell completes the credit total for the Post-adjustment Trial Balance.",
                    evidence_from_question=f"The adjusted trial balance must balance at R{int(tb_total):,} on both sides once every carried-through balance has been entered.",
                    rule_or_principle="The total credit must equal the total debit in a correctly completed adjusted trial balance.",
                    method_or_formula=f"Enter the same total on the credit side: R{int(tb_total):,}.",
                    record_link="This amount must match the completed debit total in the same total row.",
                    how_to_derive="Copy the final balanced total once the debit side has been fully added and checked.",
                    transfer_tip="In trial-balance totals, confirm the debit calculation first, then mirror that final balanced amount on the credit side.",
                ),
            },
            working_map={
                "cons-patb-expense-debit": "Only the consumed portion stays in the expense account after adjustment.",
                "cons-patb-asset-debit": "The unused portion appears as a separate asset line in the adjusted trial balance.",
                "cons-patb-total-debit": "Total the Post-adjustment Trial Balance only after the adjusted expense and the new asset line are both in place.",
            },
            guidelines=[
                "Reduce the expense balance by the stores on hand before carrying it to the Post-adjustment Trial Balance.",
                "Insert Consumable stores on hand as a new current-asset debit balance.",
                "Total the completed columns only after all adjusted balances have been entered.",
            ],
            marks=6,
        ), "consumable_stores_post_adjustment_tb_fill", expected_cells=6, adjusted_amount=adjusted_balance, carry_amount=amount, total=tb_total, adjusted_cell_id="cons-patb-expense-debit", carry_cell_id="cons-patb-asset-debit", total_debit_cell_id="cons-patb-total-debit", total_credit_cell_id="cons-patb-total-credit"))

        mini_tables = [
            {
                "heading": "Part A: General Journal adjustment and reversal",
                "headers": ["Date", "Details", "Debit", "Credit"],
                "rows": [
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="cons-mini-j-dr-details"), _cell("", editable=True, cell_id="cons-mini-j-dr-amount"), _cell("")],
                    [_cell(scenario["year_end_date"]), _cell("", editable=True, cell_id="cons-mini-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="cons-mini-j-cr-amount")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="cons-mini-j-rev-dr-details"), _cell("", editable=True, cell_id="cons-mini-j-rev-dr-amount"), _cell("")],
                    [_cell(scenario["reversal_date"]), _cell("", editable=True, cell_id="cons-mini-j-rev-cr-details"), _cell(""), _cell("", editable=True, cell_id="cons-mini-j-rev-cr-amount")],
                ],
            },
            {
                "heading": "Part B1: Income Statement extract",
                "headers": ["Expense", "Amount"],
                "rows": [[_cell(expense_label), _cell("", editable=True, cell_id="cons-mini-fa-expense")]],
            },
            {
                "heading": "Part B2: Balance Sheet extract",
                "headers": ["Current assets", "Amount"],
                "rows": [[_cell("Consumable stores on hand"), _cell("", editable=True, cell_id="cons-mini-fa-asset")]],
            },
            {
                "heading": "Part C: Post-adjustment Trial Balance extract",
                "headers": ["Account", "Debit", "Credit"],
                "rows": [
                    [_cell("Bank"), _cell("", editable=True, cell_id="cons-mini-patb-bank-debit"), _cell("")],
                    [_cell("Trading stock"), _cell("", editable=True, cell_id="cons-mini-patb-stock-debit"), _cell("")],
                    [_cell(expense_label), _cell("", editable=True, cell_id="cons-mini-patb-expense-debit"), _cell("")],
                    [_cell("Consumable stores on hand"), _cell("", editable=True, cell_id="cons-mini-patb-asset-debit"), _cell("")],
                    [_cell("Capital"), _cell(""), _cell("", editable=True, cell_id="cons-mini-patb-capital-credit")],
                    [_cell("Total"), _cell("", editable=True, cell_id="cons-mini-patb-total-debit"), _cell("", editable=True, cell_id="cons-mini-patb-total-credit")],
                ],
            },
        ]
        mini_correct_map = {
            "cons-mini-j-dr-details": "Consumable stores on hand",
            "cons-mini-j-dr-amount": amount,
            "cons-mini-j-cr-details": expense_label,
            "cons-mini-j-cr-amount": amount,
            "cons-mini-j-rev-dr-details": expense_label,
            "cons-mini-j-rev-dr-amount": amount,
            "cons-mini-j-rev-cr-details": "Consumable stores on hand",
            "cons-mini-j-rev-cr-amount": amount,
            "cons-mini-fa-expense": adjusted_balance,
            "cons-mini-fa-asset": amount,
            "cons-mini-patb-bank-debit": scenario["bank"],
            "cons-mini-patb-stock-debit": scenario["stock"],
            "cons-mini-patb-expense-debit": adjusted_balance,
            "cons-mini-patb-asset-debit": amount,
            "cons-mini-patb-capital-credit": capital,
            "cons-mini-patb-total-debit": tb_total,
            "cons-mini-patb-total-credit": tb_total,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the consumable-stores information for {biz} to complete the integrated workflow: (A) prepare the year-end adjustment and the reversal, (B) carry the effect to the Income Statement and Balance Sheet extracts, and (C) complete the Post-adjustment Trial Balance extract.",
            prompt_tables=patb_prompt_tables,
            tables=mini_tables,
            correct_map=mini_correct_map,
            derivation_map={
                "cons-mini-j-dr-amount": f"Use the stores-on-hand amount from the count sheet: R{int(amount):,}.",
                "cons-mini-fa-expense": f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} - R{int(amount):,} = R{int(adjusted_balance):,}.",
                "cons-mini-patb-total-debit": f"Total debit = R{int(scenario['bank']):,} + R{int(scenario['stock']):,} + R{int(adjusted_balance):,} + R{int(amount):,} = R{int(tb_total):,}.",
                "cons-mini-patb-total-credit": f"Total credit must match the completed debit total in the Post-adjustment Trial Balance: R{int(tb_total):,}.",
            },
            cell_hints={
                "cons-mini-j-dr-details": "Start by moving the unused stores amount into Consumable stores on hand at year-end.",
                "cons-mini-j-cr-details": f"The year-end journal credits {expense_label} to remove the unused portion from this year's expense.",
                "cons-mini-j-rev-dr-details": f"The reversal journal debits {expense_label} to reinstate the unused portion at the start of the next period.",
                "cons-mini-j-rev-cr-details": "The reversal journal credits Consumable stores on hand to remove the asset at the start of the next period.",
                "cons-mini-fa-asset": "Carry the stores-on-hand amount to the Balance Sheet extract as a current asset.",
                "cons-mini-fa-expense": "Carry only the used portion to the Income Statement.",
                "cons-mini-patb-expense-debit": f"Use the same adjusted {expense_label} figure in the Post-adjustment Trial Balance that you used in the Income Statement extract.",
                "cons-mini-patb-asset-debit": "Insert Consumable stores on hand as a new debit balance in the Post-adjustment Trial Balance.",
                "cons-mini-patb-total-debit": "Total the debit column only after the adjusted expense and stores-on-hand asset have both been inserted.",
                "cons-mini-patb-total-credit": "The credit total must equal the completed debit total once all balances have been entered.",
            },
            cell_teaching_map={
                "cons-mini-j-dr-details": _teaching_hint(
                    role_in_requirement="This cell starts the year-end adjustment by moving the unused stores amount into Consumable stores on hand.",
                    evidence_from_question=f"The year-end count created Consumable stores on hand of R{int(amount):,}.",
                    rule_or_principle="The year-end adjustment must move the unused stores amount into a new asset account.",
                    method_or_formula="Debit Consumable stores on hand with the counted amount.",
                    record_link="This amount must agree with the ledger asset account and the Balance Sheet carry-through figure.",
                    how_to_derive=f"Use R{int(amount):,} because that is the counted unused consumable-stores amount.",
                    transfer_tip="Track the asset amount across every linked record so it never changes unless a new transaction is introduced.",
                ),
                "cons-mini-j-cr-details": _teaching_hint(
                    role_in_requirement=f"This cell completes the year-end adjustment by removing the unused portion from {expense_label}.",
                    evidence_from_question=f"The Pre-adjustment Trial Balance gives {expense_label} at R{int(scenario['base_balance']):,} before adjustment.",
                    rule_or_principle="The year-end adjustment must remove the unused portion from the expense account.",
                    method_or_formula=f"Credit {expense_label} with the stores-on-hand amount.",
                    record_link="This amount must agree with the ledger expense account and the Income Statement carry-through figure.",
                    how_to_derive=f"Use R{int(amount):,} because that is the counted unused consumable-stores amount.",
                    transfer_tip="When one adjustment reduces an expense, track the same reduced expense figure through every later statement section.",
                ),
                "cons-mini-j-rev-dr-details": _teaching_hint(
                    role_in_requirement=f"This cell reinstates the unused portion in {expense_label} at the start of the next period.",
                    evidence_from_question=f"The year-end count created Consumable stores on hand of R{int(amount):,}.",
                    rule_or_principle="The reversal must reinstate the unused portion in the expense account at the start of the next period.",
                    method_or_formula=f"Debit {expense_label} with the stores-on-hand amount.",
                    record_link="This amount must agree with the ledger expense account and the Income Statement carry-through figure.",
                    how_to_derive=f"Use R{int(amount):,} because that is the counted unused consumable-stores amount.",
                    transfer_tip="When one adjustment reduces an expense, track the same reduced expense figure through every later statement section.",
                ),
                "cons-mini-j-rev-cr-details": _teaching_hint(
                    role_in_requirement="This cell removes the asset at the start of the next period.",
                    evidence_from_question=f"The year-end count created Consumable stores on hand of R{int(amount):,}.",
                    rule_or_principle="The reversal must remove the asset at the start of the next period.",
                    method_or_formula="Credit Consumable stores on hand with the counted amount.",
                    record_link="This amount must agree with the ledger asset account and the Balance Sheet carry-through figure.",
                    how_to_derive=f"Use R{int(amount):,} because that is the counted unused consumable-stores amount.",
                    transfer_tip="Track the asset amount across every linked record so it never changes unless a new transaction is introduced.",
                ),
                "cons-mini-fa-expense": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {expense_label.lower()} amount through the integrated workflow.",
                    evidence_from_question=f"The integrated source information gives {expense_label} at R{int(scenario['base_balance']):,} before adjustment and stores on hand of R{int(amount):,}.",
                    rule_or_principle="The integrated workflow must use the same adjusted expense amount consistently in every later record.",
                    method_or_formula=f"Adjusted {expense_label} = original balance - stores on hand.",
                    record_link="This amount must match the credited expense adjustment in the journal and the adjusted debit balance in the Post-adjustment Trial Balance.",
                    how_to_derive=f"Subtract R{int(amount):,} from R{int(scenario['base_balance']):,} to get R{int(adjusted_balance):,}.",
                    transfer_tip="In multipart workflows, compute the adjusted expense once and then reuse exactly the same figure in every linked extract.",
                ),
                "cons-mini-fa-asset": _teaching_hint(
                    role_in_requirement="This cell carries the stores-on-hand asset into the Balance Sheet extract in the integrated workflow.",
                    evidence_from_question=f"The year-end count created Consumable stores on hand of R{int(amount):,}.",
                    rule_or_principle="Unused consumable stores at year-end are shown as a current asset and must stay consistent across every linked extract.",
                    method_or_formula="Carry the counted stores-on-hand amount to the Balance Sheet extract unchanged.",
                    record_link="This amount must agree with the journal debit and the Post-adjustment Trial Balance asset line.",
                    how_to_derive=f"Use R{int(amount):,} because that is the year-end amount still on hand.",
                    transfer_tip="When one adjustment creates an asset, track the same asset figure through every later statement section.",
                ),
                "cons-mini-patb-expense-debit": _teaching_hint(
                    role_in_requirement=f"This cell carries the adjusted {expense_label.lower()} amount into the Post-adjustment Trial Balance section of the integrated workflow.",
                    evidence_from_question=f"The integrated workflow starts with {expense_label} at R{int(scenario['base_balance']):,} and removes stores on hand of R{int(amount):,}, leaving an adjusted balance of R{int(adjusted_balance):,}.",
                    rule_or_principle="The same adjusted expense figure must be reused consistently when it moves from the Income Statement carry-through to the adjusted trial balance.",
                    method_or_formula=f"Adjusted {expense_label} = R{int(scenario['base_balance']):,} - R{int(amount):,} = R{int(adjusted_balance):,}.",
                    record_link="This amount must match the Income Statement extract and the reduced expense after the year-end journal entry.",
                    how_to_derive=f"Subtract the stores-on-hand amount from the original {expense_label} balance, then carry that exact adjusted figure into Part C.",
                    transfer_tip="In integrated workflows, calculate the adjusted expense once and reuse the identical figure in every later section.",
                ),
                "cons-mini-patb-asset-debit": _teaching_hint(
                    role_in_requirement="This cell carries the stores-on-hand asset into the Post-adjustment Trial Balance section of the integrated workflow.",
                    evidence_from_question=f"The year-end count created Consumable stores on hand of R{int(amount):,}.",
                    rule_or_principle="A year-end asset created by an adjustment must remain consistent across the journal, Balance Sheet extract, and adjusted trial balance.",
                    method_or_formula="Carry the same stores-on-hand amount to every asset section in the workflow.",
                    record_link="This amount must equal the journal debit and the Balance Sheet carry-through amount.",
                    how_to_derive=f"Use R{int(amount):,} because that is the counted unused consumable-stores amount.",
                    transfer_tip="Track the asset amount across every linked record so it never changes unless a new transaction is introduced.",
                ),
                "cons-mini-patb-total-debit": _teaching_hint(
                    role_in_requirement="This cell totals the debit column in Part C of the integrated workflow.",
                    evidence_from_question=f"The completed debit side contains Bank R{int(scenario['bank']):,}, Trading stock R{int(scenario['stock']):,}, adjusted {expense_label} R{int(adjusted_balance):,}, and Consumable stores on hand R{int(amount):,}.",
                    rule_or_principle="The Post-adjustment Trial Balance is totalled only after every adjusted balance and new asset line has been carried through.",
                    method_or_formula=f"R{int(scenario['bank']):,} + R{int(scenario['stock']):,} + R{int(adjusted_balance):,} + R{int(amount):,} = R{int(tb_total):,}.",
                    record_link="This debit total must equal the credit total in the same Part C total row.",
                    how_to_derive="Add all completed debit balances after finishing the carry-through entries for Part C.",
                    transfer_tip="Leave the total row until last so you do not omit a new asset line or use an unadjusted expense figure.",
                ),
                "cons-mini-patb-total-credit": _teaching_hint(
                    role_in_requirement="This cell completes the credit total in Part C of the integrated workflow.",
                    evidence_from_question=f"The completed Post-adjustment Trial Balance must balance at R{int(tb_total):,} on both sides once every carried-through balance has been entered.",
                    rule_or_principle="A correctly completed adjusted trial balance has equal debit and credit totals.",
                    method_or_formula=f"Enter the same balanced total on the credit side: R{int(tb_total):,}.",
                    record_link="This amount must match the debit total already calculated in the same total row.",
                    how_to_derive="Copy the final balanced total after checking the completed debit-side calculation.",
                    transfer_tip="Check the debit-side addition first, then mirror that final balanced total on the credit side.",
                ),
            },
            working_map={
                "cons-mini-j-dr-details": "Part A creates the asset and reduces the expense; Parts B and C then carry those same adjusted figures forward.",
                "cons-mini-j-cr-details": "The year-end adjustment reduces the expense by the stores-on-hand amount.",
                "cons-mini-j-rev-dr-details": "The reversal reinstates the expense by the stores-on-hand amount at the start of the next period.",
                "cons-mini-j-rev-cr-details": "The reversal removes the asset by the stores-on-hand amount at the start of the next period.",
                "cons-mini-fa-asset": "The Balance Sheet receives the unused portion as a current asset for the next period.",
                "cons-mini-fa-expense": "The integrated workflow keeps one adjusted expense figure across the Income Statement and Post-adjustment Trial Balance.",
                "cons-mini-patb-expense-debit": "Part C reuses the same adjusted expense amount already calculated in Part B1.",
                "cons-mini-patb-asset-debit": "The stores-on-hand asset appears in both the Balance Sheet extract and the Post-adjustment Trial Balance with the same amount.",
                "cons-mini-patb-total-debit": "Finish Part C by adding the completed debit balances and then matching that total on the credit side.",
            },
            guidelines=[
                "Carry the same stores-on-hand amount consistently through the journal, statements, and Post-adjustment Trial Balance.",
                f"Use the adjusted {expense_label} figure in both the Income Statement extract and the Post-adjustment Trial Balance.",
                "Reverse the year-end adjustment on the first day of the next period using the same amount.",
            ],
            marks=17,
        ), "consumable_stores_reversal_mini_project", expected_cells=17, amount=amount, amount_cell_ids=["cons-mini-j-dr-amount", "cons-mini-j-cr-amount", "cons-mini-j-rev-dr-amount", "cons-mini-j-rev-cr-amount", "cons-mini-fa-asset", "cons-mini-patb-asset-debit"], adjusted_amount=adjusted_balance, adjusted_cell_ids=["cons-mini-fa-expense", "cons-mini-patb-expense-debit"], total=tb_total, total_debit_cell_id="cons-mini-patb-total-debit", total_credit_cell_id="cons-mini-patb-total-credit"))

    return pool



