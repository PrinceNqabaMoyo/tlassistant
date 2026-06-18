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
def _gen_bad_debts_and_recoveries(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    biz = _pick_business_name(r=r)

    write_off_scenarios = [
        {"debtor": "D. Davids", "amount": 1800, "opening_debtors": 24500},
        {"debtor": "K. Mokoena", "amount": 2400, "opening_debtors": 31800},
        {"debtor": "L. Jacobs", "amount": 3250, "opening_debtors": 40600},
    ]
    for scenario in write_off_scenarios:
        closing_debtors = _round_money(float(scenario["opening_debtors"]) - float(scenario["amount"]))
        debtor_lower = str(scenario["debtor"]).lower()

        pool.append(_with_validation(_make_calc(
            prompt=f"{biz} has a Debtors control balance of R{int(scenario['opening_debtors']):,} before year-end adjustments. {scenario['debtor']} owing R{int(scenario['amount']):,} must be written off as irrecoverable.\n\nCalculate the Debtors control balance after the bad debt is written off.",
            correct_answer=closing_debtors,
            working_formula=f"Adjusted Debtors control = R{int(scenario['opening_debtors']):,} - R{int(scenario['amount']):,}",
            formula_hint="Adjusted Debtors control = balance before write-off - bad debt written off",
        ), "bad_debts_net_debtors_calc", opening_debtors=scenario["opening_debtors"], amount=scenario["amount"]))

        write_off_journal_table = {
            "heading": "General Journal",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="bd-wo-dr-details"), _cell("", editable=True, cell_id="bd-wo-dr-amount"), _cell("")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="bd-wo-cr-details"), _cell(""), _cell("", editable=True, cell_id="bd-wo-cr-amount")],
            ],
        }
        write_off_journal_correct_map = {
            "bd-wo-dr-details": "Bad debts",
            "bd-wo-dr-amount": scenario["amount"],
            "bd-wo-cr-details": "Debtors control",
            "bd-wo-cr-amount": scenario["amount"],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=f"{scenario['debtor']} owing R{int(scenario['amount']):,} is irrecoverable and must be written off. Prepare the General Journal entry for the write-off.",
            table=write_off_journal_table,
            correct_map=write_off_journal_correct_map,
            derivation_map={
                "bd-wo-dr-amount": f"Use the amount to be written off: R{int(scenario['amount']):,}.",
                "bd-wo-cr-amount": f"The same write-off amount must be credited to Debtors control: R{int(scenario['amount']):,}.",
            },
            cell_hints={
                "bd-wo-dr-details": "The loss is treated as an expense account on the debit side.",
                "bd-wo-cr-details": "The debtor balance must be removed from Debtors control on the credit side.",
                "bd-wo-dr-amount": "Use the irrecoverable amount given for the debtor.",
                "bd-wo-cr-amount": "The credit side uses exactly the same write-off amount.",
            },
            cell_teaching_map={
                "bd-wo-dr-details": _teaching_hint(
                    role_in_requirement="This cell names the account debited when the bad debt is written off.",
                    evidence_from_question=f"{scenario['debtor']} is irrecoverable, so the business must recognise the loss of R{int(scenario['amount']):,}.",
                    rule_or_principle="Writing off an irrecoverable debtor creates an expense for the business.",
                    method_or_formula="Journal entry: Dr Bad debts / Cr Debtors control.",
                    record_link="This debit creates the bad-debts expense that later reduces profit in the Income Statement.",
                    how_to_derive="Debit Bad debts because the loss reduces profit for the period.",
                    transfer_tip="When a debtor will not pay, think expense up and debtor asset down.",
                ),
                "bd-wo-cr-details": _teaching_hint(
                    role_in_requirement="This cell names the account credited to remove the debtor from the books.",
                    evidence_from_question=f"The amount owed by {debtor_lower} can no longer be shown as collectible.",
                    rule_or_principle="Debtors control is a current asset, so it is credited when a debtor balance is removed.",
                    method_or_formula="Credit Debtors control with the same amount debited to Bad debts.",
                    record_link="This credit reduces the receivables figure that would otherwise remain in Debtors control / current assets.",
                    how_to_derive="Credit Debtors control with the amount written off.",
                    transfer_tip="Bad debt write-off means the receivable is no longer an asset of the business.",
                ),
                "bd-wo-dr-amount": _teaching_hint(
                    role_in_requirement="This cell records the debit amount of the bad-debt write-off entry.",
                    evidence_from_question=f"The question gives the irrecoverable amount for {scenario['debtor']} as R{int(scenario['amount']):,}.",
                    rule_or_principle="A write-off journal uses the exact irrecoverable amount on both sides of the entry.",
                    method_or_formula=f"Use R{int(scenario['amount']):,} on the debit side and repeat it on the credit side.",
                    record_link="This amount must match the credit to Debtors control and the reduction later seen in the debtors balance / analysis work.",
                    how_to_derive="Copy the irrecoverable amount directly from the question because no new calculation is needed here.",
                    transfer_tip="For a straight write-off journal, transfer the given debtor amount exactly rather than recalculating it.",
                ),
                "bd-wo-cr-amount": _teaching_hint(
                    role_in_requirement="This cell records the credit amount that removes the debtor from Debtors control.",
                    evidence_from_question=f"The same irrecoverable amount of R{int(scenario['amount']):,} must be removed from receivables.",
                    rule_or_principle="A balanced journal entry repeats the same amount on the opposite side when one debtor is written off in full.",
                    method_or_formula=f"Credit Debtors control with R{int(scenario['amount']):,}.",
                    record_link="This amount must equal the debit to Bad debts and the fall in current assets caused by the write-off.",
                    how_to_derive="Use the same amount as the debit side because the entire debtor balance is being removed.",
                    transfer_tip="Check the debit amount first, then mirror that exact figure on the credit side of the journal.",
                ),
            },
            working_map={
                "bd-wo-dr-details": "Start with the double-entry idea: the loss goes to Bad debts while the receivable is removed from Debtors control.",
                "bd-wo-dr-amount": "Use the debtor amount given in the prompt and keep it unchanged through both sides of the journal.",
                "bd-wo-cr-details": "The credit side clears the receivable from the books after the debit recognises the loss.",
                "bd-wo-cr-amount": "The journal balances because the same irrecoverable amount is repeated on the credit side.",
            },
            guidelines=[
                "Debit the expense account for the loss.",
                "Credit Debtors control to remove the amount receivable.",
                "Enter the same amount on both sides.",
            ],
            marks=8,
        ), "bad_debts_write_off_journal_fill", expected_cells=4, amount=scenario["amount"], amount_cell_ids=["bd-wo-dr-amount", "bd-wo-cr-amount"]))

        write_off_analysis_table = {
            "heading": "Adjustment analysis: bad debts written off",
            "headers": ["Adjustment", "Amount", "Account debited", "Account credited", "Income Statement effect", "Balance Sheet effect"],
            "rows": [
                [_cell(f"Write off {scenario['debtor']} as irrecoverable"), _cell("", editable=True, cell_id="bd-an-amount"), _cell("", editable=True, cell_id="bd-an-dr"), _cell("", editable=True, cell_id="bd-an-cr"), _cell("", editable=True, cell_id="bd-an-is"), _cell("", editable=True, cell_id="bd-an-bs")],
            ],
        }
        write_off_analysis_correct_map = {
            "bd-an-amount": scenario["amount"],
            "bd-an-dr": "Bad debts",
            "bd-an-cr": "Debtors control",
            "bd-an-is": "Expense increases by R" + f"{int(scenario['amount']):,}",
            "bd-an-bs": "Current asset decreases by R" + f"{int(scenario['amount']):,}",
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="adjustment_analysis_table",
            prompt=f"{scenario['debtor']} owing R{int(scenario['amount']):,} must be written off as irrecoverable. Complete the adjustment analysis table.",
            table=write_off_analysis_table,
            correct_map=write_off_analysis_correct_map,
            derivation_map={
                "bd-an-amount": f"Use the write-off amount given: R{int(scenario['amount']):,}.",
            },
            cell_hints={
                "bd-an-amount": "Use the same irrecoverable amount that is being written off.",
                "bd-an-dr": "The business records the loss as an expense.",
                "bd-an-cr": "The debtor asset must be reduced.",
                "bd-an-is": "Think about what happens to expenses when a bad debt is recognised.",
                "bd-an-bs": "Debtors control is part of current assets.",
            },
            cell_teaching_map={
                "bd-an-amount": _teaching_hint(
                    role_in_requirement="This cell records the amount column of the write-off analysis table.",
                    evidence_from_question=f"The irrecoverable amount for {scenario['debtor']} is given as R{int(scenario['amount']):,}.",
                    rule_or_principle="The same write-off amount must be used consistently in the amount column, the double entry, and the statement effects.",
                    method_or_formula=f"Enter the given write-off amount: R{int(scenario['amount']):,}.",
                    record_link="This amount must agree with both the journal entry and the Income Statement / Balance Sheet effects in the same analysis row.",
                    how_to_derive="Copy the irrecoverable debtor amount from the question because no new calculation is required.",
                    transfer_tip="In analysis tables, fix the amount first, then use that same figure across every other cell in the row.",
                ),
                "bd-an-dr": _teaching_hint(
                    role_in_requirement="This cell identifies the account debited when the write-off is analysed.",
                    evidence_from_question=f"{scenario['debtor']} owing R{int(scenario['amount']):,} is irrecoverable.",
                    rule_or_principle="A bad debt write-off is treated as an expense because the business has suffered a loss.",
                    method_or_formula="Debit Bad debts and credit Debtors control with the same amount.",
                    record_link="This debit explains why the Income Statement effect is an increase in expenses.",
                    how_to_derive="Use Bad debts because the irrecoverable amount is recognised as a loss expense.",
                    transfer_tip="If a debtor will not pay, the write-off moves out of receivables and into an expense account.",
                ),
                "bd-an-cr": _teaching_hint(
                    role_in_requirement="This cell identifies the account credited when the debtor is removed from the books.",
                    evidence_from_question="The debtor balance is no longer collectible and must be removed from receivables.",
                    rule_or_principle="Debtors control is a current asset, so it is credited when a debtor balance is written off.",
                    method_or_formula="Credit Debtors control with the write-off amount.",
                    record_link="This credit explains why the Balance Sheet effect is a decrease in current assets.",
                    how_to_derive="Use Debtors control because that asset account must be reduced by the irrecoverable balance.",
                    transfer_tip="Ask which account still contains the receivable that must be removed from the records.",
                ),
                "bd-an-is": _teaching_hint(
                    role_in_requirement="This cell shows the Income Statement effect of the bad debt write-off.",
                    evidence_from_question=f"The debtor balance of R{int(scenario['amount']):,} is no longer recoverable.",
                    rule_or_principle="Bad debts are treated as an operating expense in the Income Statement.",
                    method_or_formula="Show an increase in expense equal to the write-off amount.",
                    record_link="This effect must agree with the debit entry to Bad debts.",
                    how_to_derive=f"Show that expenses increase by R{int(scenario['amount']):,}.",
                    transfer_tip="When an adjustment is debited to an expense account, the Income Statement effect is usually an increase in expenses.",
                ),
                "bd-an-bs": _teaching_hint(
                    role_in_requirement="This cell shows how the write-off affects the Balance Sheet.",
                    evidence_from_question="Debtors control is reduced because one debtor's balance is removed.",
                    rule_or_principle="A write-off reduces current assets because the business is no longer owed that amount.",
                    method_or_formula="Show a decrease in current assets equal to the amount removed from Debtors control.",
                    record_link="This effect must agree with the credit to Debtors control in the double entry.",
                    how_to_derive=f"Show a decrease in current assets of R{int(scenario['amount']):,}.",
                    transfer_tip="Link the credited asset account to the Balance Sheet category it belongs to.",
                ),
            },
            working_map={
                "bd-an-dr": "The analysis follows the same logic as the journal entry: recognise the loss as Bad debts and remove the receivable from Debtors control.",
                "bd-an-bs": "The same amount that increases Bad debts reduces current assets because the debtor is no longer collectible.",
            },
            guidelines=[
                "Use the same amount across the double entry and statement effects.",
                "Bad debts increase expenses and reduce current assets.",
            ],
            marks=6,
        ), "bad_debts_write_off_analysis_fill", expected_cells=5, amount=scenario["amount"], amount_cell_id="bd-an-amount"))

    recovery_scenarios = [
        {"debtor": "T. Nkosi", "amount": 900},
        {"debtor": "S. Pillay", "amount": 1400},
        {"debtor": "R. Adams", "amount": 1850},
    ]
    for scenario in recovery_scenarios:
        debtor_lower = str(scenario["debtor"]).lower()
        recovery_journal_table = {
            "heading": "General Journal",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell("01 Mar 2026"), _cell("", editable=True, cell_id="bd-rec-dr-details"), _cell("", editable=True, cell_id="bd-rec-dr-amount"), _cell("")],
                [_cell("01 Mar 2026"), _cell("", editable=True, cell_id="bd-rec-cr-details"), _cell(""), _cell("", editable=True, cell_id="bd-rec-cr-amount")],
            ],
        }
        recovery_journal_correct_map = {
            "bd-rec-dr-details": "Bad debts",
            "bd-rec-dr-amount": scenario["amount"],
            "bd-rec-cr-details": "Bad debts recovered",
            "bd-rec-cr-amount": scenario["amount"],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=f"{scenario['debtor']}, whose account had previously been written off, paid R{int(scenario['amount']):,}. The business uses the correcting entry through Bad debts and Bad debts recovered. Prepare the General Journal entry for the recovery adjustment.",
            table=recovery_journal_table,
            correct_map=recovery_journal_correct_map,
            derivation_map={
                "bd-rec-dr-amount": f"Use the amount recovered from {debtor_lower}: R{int(scenario['amount']):,}.",
                "bd-rec-cr-amount": f"Credit Bad debts recovered with the same amount: R{int(scenario['amount']):,}.",
            },
            cell_hints={
                "bd-rec-dr-details": "Use the debit account named in the existing recovery correction approach.",
                "bd-rec-cr-details": "The credit side recognises income recovered from a debt previously written off.",
                "bd-rec-dr-amount": "Use the amount actually recovered from the debtor.",
                "bd-rec-cr-amount": "The same recovered amount appears on the credit side.",
            },
            cell_teaching_map={
                "bd-rec-dr-details": _teaching_hint(
                    role_in_requirement="This cell names the account debited in the correcting recovery entry.",
                    evidence_from_question=f"The prompt states that the business uses the correcting entry through Bad debts and Bad debts recovered for the recovered amount of R{int(scenario['amount']):,}.",
                    rule_or_principle="In this recovery treatment, Bad debts is debited to reverse the earlier expense recognition before showing the recovery as income.",
                    method_or_formula="Debit Bad debts and credit Bad debts recovered with the same recovered amount.",
                    record_link="This treatment first corrects the earlier expense effect and then recognises the recovered amount as income.",
                    how_to_derive="Debit Bad debts with the recovered amount.",
                    transfer_tip="Follow the treatment explicitly stated in the question when a recovery correction method is specified.",
                ),
                "bd-rec-cr-details": _teaching_hint(
                    role_in_requirement="This cell names the income account credited for the recovery.",
                    evidence_from_question=f"The amount recovered from {debtor_lower} is no longer an ordinary debtor balance; it is treated as recovered bad debt income.",
                    rule_or_principle="Recovered amounts previously written off are credited to Bad debts recovered.",
                    method_or_formula="Credit Bad debts recovered with the same recovered amount used on the debit side.",
                    record_link="This credit recognises the recovery separately from normal sales or debtor balances.",
                    how_to_derive="Credit Bad debts recovered with the recovered amount.",
                    transfer_tip="Recovered bad debts are shown separately from normal sales income.",
                ),
                "bd-rec-dr-amount": _teaching_hint(
                    role_in_requirement="This cell records the debit amount in the correcting recovery entry.",
                    evidence_from_question=f"{scenario['debtor']} paid back R{int(scenario['amount']):,} after the debt had already been written off.",
                    rule_or_principle="The correcting recovery entry uses the exact amount recovered on both sides of the journal.",
                    method_or_formula=f"Enter R{int(scenario['amount']):,} on the debit side and repeat it on the credit side.",
                    record_link="This amount must match the credit to Bad debts recovered and the income recognised from the recovery.",
                    how_to_derive="Copy the recovered amount directly from the question because the task is to journalise the recovery, not recalculate it.",
                    transfer_tip="In recovery journals, use the cash recovered figure exactly as given, then mirror it on the opposite side.",
                ),
                "bd-rec-cr-amount": _teaching_hint(
                    role_in_requirement="This cell records the credit amount posted to Bad debts recovered.",
                    evidence_from_question=f"The recovered amount from {debtor_lower} is R{int(scenario['amount']):,}.",
                    rule_or_principle="A balanced recovery journal repeats the same recovered amount on the credit side.",
                    method_or_formula=f"Credit Bad debts recovered with R{int(scenario['amount']):,}.",
                    record_link="This amount must equal the debit amount and represent the recovery income recognised from the debtor payment.",
                    how_to_derive="Use the same amount as the debit side because the full recovered amount is being recognised as recovery income.",
                    transfer_tip="Check the debit figure first, then carry the identical amount to the credit side to keep the journal balanced.",
                ),
            },
            working_map={
                "bd-rec-dr-details": "This question specifies the correcting recovery method, so follow that stated treatment rather than inventing a different recovery entry.",
                "bd-rec-dr-amount": "Use the recovered amount from the debtor as the fixed amount for the whole journal entry.",
                "bd-rec-cr-details": "The income side of the recovery is recognised in Bad debts recovered after the debit reverses the earlier bad-debts effect.",
                "bd-rec-cr-amount": "Mirror the same recovered amount on the credit side so the correcting recovery entry balances exactly.",
            },
            guidelines=[
                "Use the correction treatment stated in the question.",
                "Debit Bad debts and credit Bad debts recovered.",
                "The debit and credit amounts must be equal.",
            ],
            marks=8,
        ), "bad_debts_recovery_journal_fill", expected_cells=4, amount=scenario["amount"], amount_cell_ids=["bd-rec-dr-amount", "bd-rec-cr-amount"]))

    pool.append(_with_validation(_make_typed(
        prompt="Explain why a bad debt write-off decreases Debtors control and affects profit for the year.",
        sample_answer="When a debtor is written off as irrecoverable, the amount can no longer be shown as receivable, so Debtors control decreases. The loss is recognised as Bad debts, which is an expense, so profit for the year decreases.",
        grading_rubric=["no longer receivable / debtors reduced", "bad debts is an expense", "profit decreases"],
    ), "bad_debts_write_off_typed", minimum_parts=1))

    return pool

