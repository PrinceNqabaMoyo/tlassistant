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
def _gen_error_corrections_and_reclassification(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    biz = _pick_business_name(r=r)

    scenarios = [
        {
            "prompt": f"In the books of {biz}, interest on overdraft of R1,250 was incorrectly debited to Bank charges. Prepare the General Journal entry to correct the classification error.",
            "amount": 1250,
            "debit_account": "Interest on overdraft",
            "credit_account": "Bank charges",
            "wrong_account": "Bank charges",
            "correct_account": "Interest on overdraft",
            "reason": "The amount belongs to Interest on overdraft, so it must be removed from Bank charges and transferred to the correct expense account.",
            "statement_effect": "No net effect on profit; expense classification corrected.",
            "balance_sheet_effect": "No Balance Sheet effect.",
        },
        {
            "prompt": f"In the books of {biz}, commission income of R2,400 was incorrectly credited to Rent income. Prepare the General Journal entry to correct the error.",
            "amount": 2400,
            "debit_account": "Rent income",
            "credit_account": "Commission income",
            "wrong_account": "Rent income",
            "correct_account": "Commission income",
            "reason": "The wrong income account was credited, so the correction must remove the amount from Rent income and credit Commission income instead.",
            "statement_effect": "No net effect on profit; income classification corrected.",
            "balance_sheet_effect": "No Balance Sheet effect.",
        },
        {
            "prompt": f"{biz} paid the owner's personal insurance of R1,800 from the business bank account, but the bookkeeper debited Insurance. Prepare the General Journal entry to reclassify the amount correctly.",
            "amount": 1800,
            "debit_account": "Drawings",
            "credit_account": "Insurance",
            "wrong_account": "Insurance",
            "correct_account": "Drawings",
            "reason": "The payment is personal, not a business expense, so it must be transferred from Insurance to Drawings.",
            "statement_effect": "Expenses decrease by R1,800.",
            "balance_sheet_effect": "Owner's equity decreases by R1,800 through drawings.",
        },
    ]

    for scenario in scenarios:
        correction_prompt_table = {
            "heading": "Correction note",
            "headers": ["Item", "Detail"],
            "rows": [
                [_cell("Amount"), _cell(scenario["amount"])],
                [_cell("Incorrect account currently used"), _cell(scenario["wrong_account"])],
                [_cell("Correct account required"), _cell(scenario["correct_account"])],
            ],
        }
        correction_journal_table = {
            "heading": "General Journal correction entry",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="errcorr-dr-details"), _cell("", editable=True, cell_id="errcorr-dr-amount"), _cell("")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="errcorr-cr-details"), _cell(""), _cell("", editable=True, cell_id="errcorr-cr-amount")],
            ],
        }
        correction_correct_map = {
            "errcorr-dr-details": scenario["debit_account"],
            "errcorr-dr-amount": scenario["amount"],
            "errcorr-cr-details": scenario["credit_account"],
            "errcorr-cr-amount": scenario["amount"],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=scenario["prompt"],
            prompt_table=correction_prompt_table,
            table=correction_journal_table,
            correct_map=correction_correct_map,
            derivation_map={
                "errcorr-dr-amount": f"Use the amount to be reclassified: R{int(scenario['amount']):,}.",
                "errcorr-cr-amount": f"The same amount must be credited to remove it from the incorrect account: R{int(scenario['amount']):,}.",
            },
            cell_hints={
                "errcorr-dr-details": f"Debit the account that should finally contain the amount: {scenario['debit_account']}.",
                "errcorr-cr-details": f"Credit the account that was used incorrectly so the error is reversed: {scenario['credit_account']}.",
                "errcorr-dr-amount": "The correction uses the original amount of the error.",
                "errcorr-cr-amount": "Repeat the same original amount on the credit side to remove it from the wrong account.",
            },
            cell_teaching_map={
                "errcorr-dr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the account that must receive the debit in the correction entry.",
                    evidence_from_question=f"The correction note says the amount is currently in {scenario['wrong_account']} but should be in {scenario['correct_account']}.",
                    rule_or_principle="A rectification entry removes the amount from the wrong account and transfers it to the correct account without changing the original total amount.",
                    method_or_formula=f"Debit {scenario['debit_account']} and credit {scenario['credit_account']} with the same amount.",
                    record_link=f"This debit must align with the corrected classification that will appear in {scenario['correct_account']} after the transfer.",
                    how_to_derive=f"Ask which account should finally show the amount. That account is debited here: {scenario['debit_account']}.",
                    transfer_tip="In a reclassification error, identify the wrong account first, then move the amount to the correct account using one debit and one credit.",
                ),
                "errcorr-cr-details": _teaching_hint(
                    role_in_requirement="This cell identifies the account credited to cancel the incorrect treatment.",
                    evidence_from_question=scenario["reason"],
                    rule_or_principle="The wrong account must be reversed by posting the opposite side needed to remove the original misclassification.",
                    method_or_formula=f"Credit {scenario['credit_account']} to remove the amount from the wrong classification.",
                    record_link=f"This credit removes the amount from {scenario['wrong_account']} so only {scenario['correct_account']} keeps the corrected classification.",
                    how_to_derive=f"Because the amount is sitting in {scenario['credit_account']} incorrectly, crediting this line removes the error while the debit transfers it to {scenario['debit_account']}.",
                    transfer_tip="Correction entries are transfer entries: one side removes the wrong classification and the other side puts the amount where it belongs.",
                ),
                "errcorr-dr-amount": _teaching_hint(
                    role_in_requirement="This cell enters the amount of the correction entry.",
                    evidence_from_question=f"The correction note gives the amount as R{int(scenario['amount']):,}.",
                    rule_or_principle="A rectification entry uses the same original amount on both sides of the journal.",
                    method_or_formula=f"Use R{int(scenario['amount']):,} on both the debit and credit sides.",
                    record_link="This amount must match the credit amount because the entry is transferring one existing amount, not creating a new total.",
                    how_to_derive="Copy the amount from the error note, because the correction is reclassifying the same value rather than calculating a new one.",
                    transfer_tip="If the task is to correct a misclassification, do not invent a new amount. Transfer the original amount exactly.",
                ),
                "errcorr-cr-amount": _teaching_hint(
                    role_in_requirement="This cell enters the credit amount that removes the original misclassification.",
                    evidence_from_question=f"The correction note gives the same original error amount as R{int(scenario['amount']):,}.",
                    rule_or_principle="The credit side of a rectification entry repeats the same transferred amount used on the debit side.",
                    method_or_formula=f"Credit the wrong account with R{int(scenario['amount']):,}.",
                    record_link="This amount must match the debit amount exactly so the correction entry balances while shifting the classification.",
                    how_to_derive="Use the same amount shown in the source note because the correction removes the original value from the wrong account.",
                    transfer_tip="Check the debit amount first, then mirror that exact figure on the credit side of the correction entry.",
                ),
            },
            working_map={
                "errcorr-dr-details": f"This correction shifts the amount out of {scenario['wrong_account']} and into {scenario['correct_account']}.",
                "errcorr-cr-details": f"After this entry, {scenario['wrong_account']} no longer includes the misclassified amount and {scenario['correct_account']} does.",
                "errcorr-dr-amount": "Use the source-note amount as the fixed transfer figure for the whole correction entry.",
                "errcorr-cr-amount": "Mirror the same amount on the credit side so the wrong classification is removed without changing the total amount involved.",
            },
            guidelines=[
                "Use one debit and one credit to transfer the amount from the wrong account to the correct account.",
                "Keep the original amount the same on both sides of the correction entry.",
                "Think of the correction as removing the wrong classification first, then placing the amount where it belongs.",
            ],
            marks=8,
        ), "error_correction_journal_fill", expected_cells=4, cell_expectations=correction_correct_map))

        correction_analysis_table = {
            "heading": "Correction analysis table",
            "headers": ["Correction", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet / owner's equity effect"],
            "rows": [
                [_cell(f"Transfer from {scenario['wrong_account']} to {scenario['correct_account']}"), _cell("", editable=True, cell_id="errcorr-an-amount"), _cell("", editable=True, cell_id="errcorr-an-dr"), _cell("", editable=True, cell_id="errcorr-an-cr"), _cell("", editable=True, cell_id="errcorr-an-is"), _cell("", editable=True, cell_id="errcorr-an-bs")],
            ],
        }
        correction_analysis_correct_map = {
            "errcorr-an-amount": scenario["amount"],
            "errcorr-an-dr": scenario["debit_account"],
            "errcorr-an-cr": scenario["credit_account"],
            "errcorr-an-is": scenario["statement_effect"],
            "errcorr-an-bs": scenario["balance_sheet_effect"],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="adjustment_analysis_table",
            prompt=f"{scenario['prompt']} Then complete the correction analysis table to show the amount, debit account, credit account, Income Statement effect, and Balance Sheet / owner's equity effect.",
            prompt_table=correction_prompt_table,
            table=correction_analysis_table,
            correct_map=correction_analysis_correct_map,
            derivation_map={
                "errcorr-an-amount": f"Use the same correction amount: R{int(scenario['amount']):,}.",
                "errcorr-an-is": f"Analyse whether this correction changes totals or only changes classification. Expected effect: {scenario['statement_effect']}",
            },
            cell_hints={
                "errcorr-an-amount": "Use the same amount as the rectification entry.",
                "errcorr-an-dr": f"The debit account is the account that should finally contain the amount: {scenario['debit_account']}.",
                "errcorr-an-cr": f"The credit account removes the amount from the incorrect classification: {scenario['credit_account']}.",
                "errcorr-an-is": "Ask whether the correction changes total profit or only reclassifies an item already recorded.",
                "errcorr-an-bs": "Only some correction entries change assets, liabilities, or owner's equity directly.",
            },
            cell_teaching_map={
                "errcorr-an-amount": _teaching_hint(
                    role_in_requirement="This cell records the amount column of the correction analysis row.",
                    evidence_from_question=f"The correction note gives the transferred amount as R{int(scenario['amount']):,}.",
                    rule_or_principle="The analysis table uses the same amount as the rectification journal because it is analysing that exact transfer.",
                    method_or_formula=f"Enter R{int(scenario['amount']):,} in the amount column.",
                    record_link="This amount must agree with both the debit and credit sides of the rectification journal entry.",
                    how_to_derive="Copy the correction amount directly from the source note before completing the rest of the analysis row.",
                    transfer_tip="In analysis tables, lock in the source amount first and then carry that same figure across the account and effect columns.",
                ),
                "errcorr-an-dr": _teaching_hint(
                    role_in_requirement="This cell identifies the account debited in the correction analysis table.",
                    evidence_from_question=f"The amount must end up in {scenario['correct_account']} instead of {scenario['wrong_account']}.",
                    rule_or_principle="The debit account in a correction analysis table is the account that should finally contain the amount after rectification.",
                    method_or_formula=f"Debit {scenario['debit_account']} and credit {scenario['credit_account']}.",
                    record_link="This account must match the debit side of the corresponding rectification journal entry.",
                    how_to_derive=f"Choose the correct destination account for the amount: {scenario['debit_account']}.",
                    transfer_tip="When analysing a rectification, ask where the amount belongs after the correction is complete.",
                ),
                "errcorr-an-cr": _teaching_hint(
                    role_in_requirement="This cell identifies the account credited in the correction analysis table.",
                    evidence_from_question=f"The amount is sitting incorrectly in {scenario['wrong_account']} and must be removed from that classification.",
                    rule_or_principle="The credit account in a correction analysis table is the account from which the misclassified amount is removed.",
                    method_or_formula=f"Credit {scenario['credit_account']} to clear the wrong classification.",
                    record_link="This account must match the credit side of the rectification journal entry.",
                    how_to_derive=f"Identify the incorrect account currently holding the amount: {scenario['credit_account']}.",
                    transfer_tip="Treat the credit cell as the account being cleared out so the debit cell can receive the corrected classification.",
                ),
                "errcorr-an-is": _teaching_hint(
                    role_in_requirement="This cell explains the Income Statement effect of the correction.",
                    evidence_from_question=scenario["reason"],
                    rule_or_principle="Some correction entries only reclassify an amount within the same statement, while others remove an item from profit entirely.",
                    method_or_formula="Decide whether the correction changes total income/expenses or only changes the label of the account used.",
                    record_link="This effect must agree with the debit and credit accounts chosen in the correction entry.",
                    how_to_derive=f"From the accounts affected, conclude the statement effect: {scenario['statement_effect']}",
                    transfer_tip="When a correction moves between two expense accounts or two income accounts, profit usually stays the same. When it moves to Drawings, profit can change.",
                ),
                "errcorr-an-bs": _teaching_hint(
                    role_in_requirement="This cell explains whether the correction affects the Balance Sheet or owner's equity.",
                    evidence_from_question=f"The correction moves the amount from {scenario['wrong_account']} to {scenario['correct_account']}.",
                    rule_or_principle="Only corrections involving assets, liabilities, or drawings create a Balance Sheet / equity effect; pure nominal reclassifications usually do not.",
                    method_or_formula="Link the corrected account to its accounting category before deciding the effect.",
                    record_link="The Balance Sheet / equity effect must agree with the corrected account classification used in the journal entry.",
                    how_to_derive=f"Use the account type of {scenario['correct_account']} and the nature of the correction to conclude: {scenario['balance_sheet_effect']}",
                    transfer_tip="Always ask whether the corrected account is a statement of profit item only or whether it also changes owner's equity / Balance Sheet presentation.",
                ),
            },
            working_map={
                "errcorr-an-amount": "Use the same transfer amount as the journal entry, then keep that figure fixed across the whole analysis row.",
                "errcorr-an-dr": f"The debit column shows where the amount should finally sit after it is moved out of {scenario['wrong_account']}.",
                "errcorr-an-cr": f"The credit column clears the incorrect classification so the amount no longer remains in {scenario['wrong_account']}.",
                "errcorr-an-is": f"The analysis follows directly from shifting the amount out of {scenario['wrong_account']} and into {scenario['correct_account']}.",
                "errcorr-an-bs": f"Use the final classification in {scenario['correct_account']} to decide whether any Balance Sheet or equity category changes.",
            },
            guidelines=[
                "Use the same amount as the journal correction entry.",
                "Match the analysis table accounts to the accounts used in the rectification journal.",
                "Decide the statement effects from the nature of the corrected account, not from the wording alone.",
            ],
            marks=6,
        ), "error_correction_analysis_fill", expected_cells=5, cell_expectations=correction_analysis_correct_map))

    grouped_prompt_table = {
        "heading": "Rectification source list",
        "headers": ["Error", "Amount", "Incorrect account", "Correct account"],
        "rows": [
            [_cell("Interest on overdraft misclassified"), _cell(scenarios[0]["amount"]), _cell(scenarios[0]["wrong_account"]), _cell(scenarios[0]["correct_account"])],
            [_cell("Commission income misclassified"), _cell(scenarios[1]["amount"]), _cell(scenarios[1]["wrong_account"]), _cell(scenarios[1]["correct_account"])],
            [_cell("Owner's personal insurance treated as a business expense"), _cell(scenarios[2]["amount"]), _cell(scenarios[2]["wrong_account"]), _cell(scenarios[2]["correct_account"])],
        ],
    }
    grouped_rows = []
    grouped_correct_map: Dict[str, Any] = {}
    grouped_derivation_map: Dict[str, str] = {}
    grouped_cell_hints: Dict[str, str] = {}
    grouped_cell_teaching_map: Dict[str, Dict[str, str]] = {}
    grouped_working_map: Dict[str, str] = {}
    for index, scenario in enumerate(scenarios, start=1):
        prefix = f"errwf-{index}"
        grouped_rows.append([_cell("28 Feb 2026"), _cell("", editable=True, cell_id=f"{prefix}-dr-details"), _cell("", editable=True, cell_id=f"{prefix}-dr-amount"), _cell("")])
        grouped_rows.append([_cell("28 Feb 2026"), _cell("", editable=True, cell_id=f"{prefix}-cr-details"), _cell(""), _cell("", editable=True, cell_id=f"{prefix}-cr-amount")])
        grouped_correct_map[f"{prefix}-dr-details"] = scenario["debit_account"]
        grouped_correct_map[f"{prefix}-dr-amount"] = scenario["amount"]
        grouped_correct_map[f"{prefix}-cr-details"] = scenario["credit_account"]
        grouped_correct_map[f"{prefix}-cr-amount"] = scenario["amount"]
        grouped_derivation_map[f"{prefix}-dr-amount"] = f"Use the rectification amount given for this error: R{int(scenario['amount']):,}."
        grouped_derivation_map[f"{prefix}-cr-amount"] = f"Credit the same amount to remove it from {scenario['wrong_account']}: R{int(scenario['amount']):,}."
        grouped_cell_hints[f"{prefix}-dr-details"] = f"This debit line must show the correct account: {scenario['debit_account']}."
        grouped_cell_hints[f"{prefix}-cr-details"] = f"This credit line removes the amount from the wrong account: {scenario['credit_account']}."
        grouped_cell_hints[f"{prefix}-dr-amount"] = f"Use the source-row correction amount for this error: R{int(scenario['amount']):,}."
        grouped_cell_hints[f"{prefix}-cr-amount"] = "Each rectification entry must balance, so the credit amount matches the debit amount."
        grouped_cell_teaching_map[f"{prefix}-dr-details"] = _teaching_hint(
            role_in_requirement="This cell identifies the debit account for one rectification entry in the grouped workflow.",
            evidence_from_question=f"The source list states that the amount is currently in {scenario['wrong_account']} but belongs in {scenario['correct_account']}.",
            rule_or_principle="Each correction transfers one amount from the wrong account to the correct account using equal debit and credit amounts.",
            method_or_formula=f"Debit {scenario['debit_account']} and credit {scenario['credit_account']} with R{int(scenario['amount']):,}.",
            record_link="The grouped journal still follows the same rule as a single correction entry; each pair of lines must balance and match the source list.",
            how_to_derive=f"Choose the account that should finally contain the amount: {scenario['debit_account']}.",
            transfer_tip="In grouped rectifications, complete one correction at a time so that each debit/credit pair stays linked to its own source row.",
        )
        grouped_cell_teaching_map[f"{prefix}-cr-details"] = _teaching_hint(
            role_in_requirement="This cell identifies the credit account that removes the incorrect classification in the grouped workflow.",
            evidence_from_question=f"The amount is currently sitting in {scenario['wrong_account']} even though it should belong in {scenario['correct_account']}.",
            rule_or_principle="A rectification entry credits the wrong account to reverse the original misclassification while the debit moves the amount to the correct account.",
            method_or_formula=f"Credit {scenario['credit_account']} with R{int(scenario['amount']):,} to clear the error.",
            record_link="This credit line must pair with the debit line for the same source-row correction, not with another row.",
            how_to_derive=f"Use {scenario['credit_account']} because that is the account from which the amount must be removed.",
            transfer_tip="When several rectifications are grouped together, finish one debit/credit pair fully before starting the next source-row error.",
        )
        grouped_working_map[f"{prefix}-dr-details"] = f"For this source-row correction, move the amount from {scenario['wrong_account']} to {scenario['correct_account']} before moving to the next error."
        grouped_working_map[f"{prefix}-cr-details"] = f"This credit line belongs to the same source-row transfer and removes the amount from {scenario['wrong_account']} so that only {scenario['correct_account']} keeps it."

    grouped_journal_table = {
        "heading": "General Journal rectification workflow",
        "headers": ["Date", "Details", "Debit", "Credit"],
        "rows": grouped_rows,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="journal",
        prompt="Use the rectification source list to prepare all the General Journal entries needed to correct the three errors shown. Treat each error as a separate two-line entry.",
        prompt_table=grouped_prompt_table,
        table=grouped_journal_table,
        correct_map=grouped_correct_map,
        derivation_map=grouped_derivation_map,
        cell_hints=grouped_cell_hints,
        cell_teaching_map=grouped_cell_teaching_map,
        working_map=grouped_working_map,
        guidelines=[
            "Prepare each correction as its own two-line journal entry.",
            "Use the source-list amount exactly for each correction; do not combine different errors into one total.",
            "Complete one row-pair at a time so the debit and credit stay tied to the same source error.",
        ],
        marks=12,
    ), "error_correction_journal_workflow_fill", expected_cells=12, cell_expectations=grouped_correct_map))

    owner_name, clerk_name = _pick_person_names(r=r, k=2)
    mixed_loan_balance = 90000
    mixed_loan_rate = 12
    mixed_loan_months = 3
    mixed_loan_amount = _round_money(float(mixed_loan_balance) * float(mixed_loan_rate) / 100 * float(mixed_loan_months) / 12)
    mixed_income_amount = 1200
    mixed_prompt_table = {
        "heading": "Integrated year-end notes",
        "headers": ["No.", "Adjustment / correction"],
        "rows": [
            [_cell("1"), _cell(f"Personal insurance of {owner_name} amounting to R1,800 was paid from the business bank account and debited to Insurance instead of Drawings.")],
            [_cell("2"), _cell(f"Interest on loan on R{int(mixed_loan_balance):,} at {int(mixed_loan_rate)}% p.a. for the last {int(mixed_loan_months)} month(s) is still owing at year-end.")],
            [_cell("3"), _cell(f"Interest income on a fixed deposit of R{int(mixed_income_amount):,} is still receivable. {clerk_name} highlighted that this accrual has not yet been journalised.")],
        ],
    }
    mixed_journal_table = {
        "heading": "General Journal: integrated corrections and adjustments",
        "headers": ["Date", "Details", "Debit", "Credit"],
        "rows": [
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="errmix-1-dr-details"), _cell("", editable=True, cell_id="errmix-1-dr-amount"), _cell("")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="errmix-1-cr-details"), _cell(""), _cell("", editable=True, cell_id="errmix-1-cr-amount")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="errmix-2-dr-details"), _cell("", editable=True, cell_id="errmix-2-dr-amount"), _cell("")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="errmix-2-cr-details"), _cell(""), _cell("", editable=True, cell_id="errmix-2-cr-amount")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="errmix-3-dr-details"), _cell("", editable=True, cell_id="errmix-3-dr-amount"), _cell("")],
            [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="errmix-3-cr-details"), _cell(""), _cell("", editable=True, cell_id="errmix-3-cr-amount")],
        ],
    }
    mixed_correct_map = {
        "errmix-1-dr-details": "Drawings",
        "errmix-1-dr-amount": 1800,
        "errmix-1-cr-details": "Insurance",
        "errmix-1-cr-amount": 1800,
        "errmix-2-dr-details": "Interest on loan",
        "errmix-2-dr-amount": mixed_loan_amount,
        "errmix-2-cr-details": "Accrued expenses",
        "errmix-2-cr-amount": mixed_loan_amount,
        "errmix-3-dr-details": "Accrued income",
        "errmix-3-dr-amount": mixed_income_amount,
        "errmix-3-cr-details": "Interest income",
        "errmix-3-cr-amount": mixed_income_amount,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="journal",
        prompt=f"Use the integrated year-end notes for {biz} to prepare all the General Journal entries required. The set includes one rectification entry and two ordinary accrual adjustments.",
        prompt_table=mixed_prompt_table,
        table=mixed_journal_table,
        correct_map=mixed_correct_map,
        derivation_map={
            "errmix-1-dr-amount": "The rectification uses the original misclassified personal-insurance amount of R1,800.",
            "errmix-2-dr-amount": f"Accrued interest on loan = R{int(mixed_loan_balance):,} × {int(mixed_loan_rate)}% × {int(mixed_loan_months)}/12 = R{int(mixed_loan_amount):,}.",
            "errmix-3-dr-amount": f"Use the interest income still receivable from the source note: R{int(mixed_income_amount):,}.",
        },
        cell_hints={
            "errmix-1-dr-details": "For the rectification item, debit the account that should finally contain the personal payment.",
            "errmix-1-cr-details": "Credit the wrong account so the personal payment is removed from business expenses.",
            "errmix-2-dr-details": "Unpaid loan interest belongs to this period, so start with the expense account on the debit side.",
            "errmix-2-cr-details": "Outstanding expenses are credited to a liability account.",
            "errmix-3-dr-details": "Income still receivable is debited to an asset account.",
            "errmix-3-cr-details": "The related income account is credited because the income has been earned this period.",
        },
        cell_teaching_map={
            "errmix-1-dr-details": _teaching_hint(
                role_in_requirement="This cell records the debit account for the rectification item within a mixed year-end journal workflow.",
                evidence_from_question=f"The source note states that personal insurance for {owner_name} was charged to Insurance instead of Drawings.",
                rule_or_principle="Even inside a mixed year-end journal, a rectification entry still transfers the amount from the wrong account to the correct account.",
                method_or_formula="Debit Drawings and credit Insurance for R1,800.",
                record_link="This correction must agree with the later ledger / final-account effects where Insurance decreases and Drawings increases.",
                how_to_derive="Ask which account should finally show the personal payment. That account is Drawings.",
                transfer_tip="In mixed journal questions, isolate each source row first so you do not confuse rectifications with ordinary accrual adjustments.",
            ),
            "errmix-2-dr-details": _teaching_hint(
                role_in_requirement="This cell records the expense account debited for unpaid loan interest in the mixed journal workflow.",
                evidence_from_question="The source note says the final months of loan interest are still owing.",
                rule_or_principle="Accrued expenses increase the current-period expense and create a matching current liability.",
                method_or_formula=f"Accrued interest = R{int(mixed_loan_balance):,} × {int(mixed_loan_rate)}% × {int(mixed_loan_months)}/12.",
                record_link="This amount would later increase Interest on loan in Profit and Loss and create Accrued expenses in the Balance Sheet.",
                how_to_derive="Debit Interest on loan because the expense belongs to the current year.",
                transfer_tip="Mixed journal workflows still follow the same individual double-entry rules for each adjustment source row.",
            ),
            "errmix-2-cr-details": _teaching_hint(
                role_in_requirement="This cell records the liability account credited for the unpaid loan-interest adjustment in the mixed workflow.",
                evidence_from_question="The final months of interest are still owing and have not yet been paid.",
                rule_or_principle="Outstanding expenses are credited to a current-liability account until settlement.",
                method_or_formula="Credit Accrued expenses with the same accrued-interest amount used on the debit side.",
                record_link="This credit creates the Balance Sheet liability matching the increased Interest on loan expense.",
                how_to_derive="Use Accrued expenses because the amount is still payable at year-end.",
                transfer_tip="If an expense is owing, the credit side usually creates or increases a payable account.",
            ),
            "errmix-3-dr-details": _teaching_hint(
                role_in_requirement="This cell records the asset account debited for interest income still receivable in the mixed workflow.",
                evidence_from_question=f"The note says interest income of R{int(mixed_income_amount):,} is still receivable and has not yet been journalised.",
                rule_or_principle="Income earned but not yet received is recorded as an accrued-income asset.",
                method_or_formula="Debit Accrued income and credit Interest income with the receivable amount.",
                record_link="This amount later appears in the Balance Sheet as Accrued income and increases Interest income in the statements.",
                how_to_derive="Debit Accrued income because the business has earned the amount and is still owed it.",
                transfer_tip="When income is still owing, think asset up and income up.",
            ),
            "errmix-3-cr-details": _teaching_hint(
                role_in_requirement="This cell records the income account credited for the accrued interest-income adjustment in the mixed workflow.",
                evidence_from_question="The interest income belongs to the current year even though it has not yet been received in cash.",
                rule_or_principle="Income earned in the current period must be credited to the relevant nominal income account.",
                method_or_formula="Credit Interest income with the receivable amount from the source note.",
                record_link="This increases the current-period interest-income figure that later appears in the Income Statement.",
                how_to_derive="Use Interest income because that is the revenue account affected by the accrual.",
                transfer_tip="In mixed workflows, separate the receivable asset from the matching income account before filling the two sides.",
            ),
        },
        working_map={
            "errmix-1-dr-details": "Treat note 1 as a rectification entry before moving on to the accrual adjustments in notes 2 and 3.",
            "errmix-2-dr-details": "Calculate the unpaid loan-interest amount separately, then journal it with Accrued expenses.",
            "errmix-3-dr-details": "Note 3 is an accrued-income adjustment, so the receivable asset is debited and Interest income is credited.",
            "errmix-1-cr-details": "The rectification is complete only when the wrong Insurance classification is cleared by the matching credit line.",
        },
        guidelines=[
            "Read each source note separately and identify whether it is a rectification or an ordinary accrual adjustment.",
            "Use the original amount for the rectification item and calculate only the accrual note that requires a formula.",
            "Keep each debit and credit pair linked to its own source row.",
        ],
        marks=14,
    ), "error_correction_integrated_adjustment_journal_fill", expected_cells=12, cell_expectations=mixed_correct_map))

    ledger_prompt_tables = [
        {
            "heading": "Rectification note",
            "headers": ["Item", "Detail"],
            "rows": [
                [_cell("Owner"), _cell(owner_name)],
                [_cell("Amount"), _cell(1800)],
                [_cell("Incorrect account"), _cell("Insurance")],
                [_cell("Correct account"), _cell("Drawings")],
            ],
        },
    ]
    ledger_tables = [
        {
            "heading": "Insurance account",
            "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
            "rows": [
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="errled-ins-details"), _cell("GJ"), _cell(""), _cell("", editable=True, cell_id="errled-ins-credit")],
            ],
        },
        {
            "heading": "Drawings account",
            "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
            "rows": [
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="errled-drw-details"), _cell("GJ"), _cell("", editable=True, cell_id="errled-drw-debit"), _cell("")],
            ],
        },
    ]
    ledger_correct_map = {
        "errled-ins-details": "Drawings",
        "errled-ins-credit": 1800,
        "errled-drw-details": "Insurance",
        "errled-drw-debit": 1800,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="ledger",
        prompt=f"{biz} must post the rectification for {owner_name}'s personal insurance payment to the General Ledger accounts shown. Post only the correction entry lines.",
        prompt_tables=ledger_prompt_tables,
        tables=ledger_tables,
        correct_map=ledger_correct_map,
        derivation_map={
            "errled-ins-credit": "Credit Insurance with the original personal-payment amount to remove it from business expenses: R1,800.",
            "errled-drw-debit": "Debit Drawings with the same amount so the owner's personal use is shown correctly: R1,800.",
        },
        cell_hints={
            "errled-ins-details": "In the Insurance account, the details column shows the opposite account from the correction entry.",
            "errled-drw-details": "In the Drawings account, write the account on the opposite side of the rectification entry.",
        },
        cell_teaching_map={
            "errled-ins-details": _teaching_hint(
                role_in_requirement="This cell names the opposite account in the Insurance ledger posting.",
                evidence_from_question="Insurance was used incorrectly and must now be reduced by the rectification entry.",
                rule_or_principle="In a ledger account, the details column records the account on the other side of the journal entry.",
                method_or_formula="Insurance is credited against Drawings in this rectification.",
                record_link="This ledger posting must agree with the correction journal entry Dr Drawings / Cr Insurance.",
                how_to_derive="Because Insurance is credited against Drawings, write Drawings in the details column.",
                transfer_tip="When posting to ledger, always check the opposite account from the journal entry before filling the details column.",
            ),
            "errled-drw-details": _teaching_hint(
                role_in_requirement="This cell names the opposite account in the Drawings ledger posting.",
                evidence_from_question="The personal payment belongs in Drawings rather than Insurance.",
                rule_or_principle="The receiving ledger account shows the account on the other side of the source journal entry in its details column.",
                method_or_formula="Drawings is debited against Insurance for the same amount.",
                record_link="This posting links directly to the corrected final-account effect where Drawings increases and Insurance decreases.",
                how_to_derive="Because Drawings is debited against Insurance, write Insurance in the details column.",
                transfer_tip="Use the journal entry as the bridge between the source correction note and the ledger posting.",
            ),
        },
        working_map={
            "errled-ins-details": "Insurance is the wrong account being cleared, so its ledger line must reference Drawings as the opposite account.",
            "errled-drw-details": "Drawings is the correct destination of the personal payment, so its ledger line references Insurance as the source being corrected.",
        },
        guidelines=[
            "Post only the rectification entry to the two ledger accounts shown.",
            "Use the opposite account name in the Details column of each ledger line.",
            "Use the original misclassified amount on both ledger postings.",
        ],
        marks=6,
    ), "error_correction_ledger_fill", expected_cells=4, cell_expectations=ledger_correct_map))

    carry_prompt_table = {
        "heading": "Corrected source extract",
        "headers": ["Item", "Amount"],
        "rows": [
            [_cell("Insurance before rectification"), _cell(9600)],
            [_cell("Drawings before rectification"), _cell(12000)],
            [_cell("Personal insurance to transfer to Drawings"), _cell(1800)],
        ],
    }
    carry_tables = [
        {
            "heading": "Profit and Loss Account (extract)",
            "headers": ["Expense", "Amount"],
            "rows": [[_cell("Insurance"), _cell("", editable=True, cell_id="errfa-insurance")]],
        },
        {
            "heading": "Owner's equity extract",
            "headers": ["Item", "Amount"],
            "rows": [[_cell("Drawings"), _cell("", editable=True, cell_id="errfa-drawings")]],
        },
    ]
    carry_correct_map = {
        "errfa-insurance": 7800,
        "errfa-drawings": 13800,
    }
    pool.append(_with_validation(_make_fill_in_table_question(
        question_type="final_account_table",
        prompt=f"Use the corrected source extract for {biz} to show the final Insurance and Drawings figures after the rectification entry has been posted.",
        prompt_table=carry_prompt_table,
        tables=carry_tables,
        correct_map=carry_correct_map,
        derivation_map={
            "errfa-insurance": "Corrected Insurance = R9,600 - R1,800 = R7,800.",
            "errfa-drawings": "Corrected Drawings = R12,000 + R1,800 = R13,800.",
        },
        cell_hints={
            "errfa-insurance": "Remove the personal-insurance amount from the business Insurance expense.",
            "errfa-drawings": "Add the transferred personal amount to Drawings.",
        },
        cell_teaching_map={
            "errfa-insurance": _teaching_hint(
                role_in_requirement="This cell shows the corrected Insurance figure after the rectification.",
                evidence_from_question="The source extract gives Insurance before rectification and the amount that must be removed from it.",
                rule_or_principle="A personal payment should not remain in a business expense account, so the expense must be reduced by the misclassified amount.",
                method_or_formula="Corrected Insurance = Insurance before rectification - amount transferred to Drawings.",
                record_link="This corrected figure links back to the journal and ledger correction where Insurance was credited with R1,800.",
                how_to_derive="Subtract R1,800 from R9,600 to get R7,800.",
                transfer_tip="Whenever a personal amount is removed from an expense, the corrected expense figure is lower in Profit and Loss.",
            ),
            "errfa-drawings": _teaching_hint(
                role_in_requirement="This cell shows the corrected Drawings figure after the personal payment is reclassified.",
                evidence_from_question="The source extract shows Drawings before rectification and the personal amount that must be added to it.",
                rule_or_principle="Owner's personal use of business funds is treated as Drawings, not as an expense of the business.",
                method_or_formula="Corrected Drawings = Drawings before rectification + amount transferred from Insurance.",
                record_link="This amount must agree with the debit posting to Drawings in the correction journal and ledger.",
                how_to_derive="Add R1,800 to R12,000 to get R13,800.",
                transfer_tip="When a personal payment is reclassified to Drawings, owner's equity is reduced through a higher drawings figure.",
            ),
        },
        working_map={
            "errfa-insurance": "The correction removes the personal amount from business expenses, so the Insurance line must decrease.",
            "errfa-drawings": "The same amount is added to Drawings because it represents the owner's personal use of business funds.",
        },
        guidelines=[
            "Reduce the wrongly charged expense by the amount transferred out of it.",
            "Increase Drawings by the same amount so the owner's personal use is shown correctly.",
        ],
        marks=4,
    ), "error_correction_carrythrough_fill", expected_cells=2, cell_expectations=carry_correct_map))

    return pool


