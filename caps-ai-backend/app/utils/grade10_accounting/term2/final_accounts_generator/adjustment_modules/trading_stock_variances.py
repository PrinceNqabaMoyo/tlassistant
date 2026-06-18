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
def _gen_trading_stock_variances(r: random.Random) -> List[Dict[str, Any]]:
    pool: List[Dict[str, Any]] = []
    biz = _pick_business_name(r=r)

    scenarios = [
        {"per_records": 45000, "actual_count": 43000},
        {"per_records": 62000, "actual_count": 59500},
        {"per_records": 52000, "actual_count": 52800},
        {"per_records": 71000, "actual_count": 72400},
    ]
    for scenario in scenarios:
        variance_amount = _round_money(abs(float(scenario["actual_count"]) - float(scenario["per_records"])))
        is_deficit = float(scenario["actual_count"]) < float(scenario["per_records"])
        variance_label = "Trading stock deficit" if is_deficit else "Trading stock surplus"
        p_and_l_label = "Profit and loss"
        adjusted_stock = _round_money(float(scenario["actual_count"]))

        pool.append(_with_validation(_make_calc(
            prompt=f"{biz} shows trading stock per records of R{int(scenario['per_records']):,}. The physical stock count at year-end is R{int(scenario['actual_count']):,}.\n\nCalculate the trading stock {'deficit' if is_deficit else 'surplus'}.",
            correct_answer=variance_amount,
            working_formula=f"{variance_label} = |R{int(scenario['actual_count']):,} - R{int(scenario['per_records']):,}| = R{int(variance_amount):,}",
            formula_hint="Trading stock variance = |physical stock - stock per records|",
        ), "trading_stock_variance_calc", per_records=scenario["per_records"], actual_count=scenario["actual_count"]))

        journal_dr_details = variance_label if is_deficit else "Trading stock"
        journal_cr_details = "Trading stock" if is_deficit else variance_label
        journal_table = {
            "heading": "General Journal",
            "headers": ["Date", "Details", "Debit", "Credit"],
            "rows": [
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="tsv-j-dr-details"), _cell("", editable=True, cell_id="tsv-j-dr-amount"), _cell("")],
                [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="tsv-j-cr-details"), _cell(""), _cell("", editable=True, cell_id="tsv-j-cr-amount")],
            ],
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="journal",
            prompt=f"{biz} has trading stock per records of R{int(scenario['per_records']):,} and an actual stock count of R{int(scenario['actual_count']):,}. Prepare the General Journal entry to record the {variance_label.lower()}.",
            table=journal_table,
            correct_map={
                "tsv-j-dr-details": journal_dr_details,
                "tsv-j-dr-amount": variance_amount,
                "tsv-j-cr-details": journal_cr_details,
                "tsv-j-cr-amount": variance_amount,
            },
            derivation_map={
                "tsv-j-dr-amount": f"Use the variance amount calculated from the stock count difference: R{int(variance_amount):,}.",
                "tsv-j-cr-amount": f"The same amount is posted to the opposite side of the journal entry: R{int(variance_amount):,}.",
            },
            cell_hints={
                "tsv-j-dr-details": "Decide whether the variance is a loss or a gain before choosing the debit account.",
                "tsv-j-cr-details": "The opposite side either adjusts Trading stock or records the stock variance account.",
                "tsv-j-dr-amount": "Use the stock-count difference as the journal amount.",
                "tsv-j-cr-amount": "Repeat the same variance amount on the credit side.",
            },
            cell_teaching_map={
                "tsv-j-dr-details": _teaching_hint(
                    role_in_requirement="This cell names the account debited in the stock-variance adjustment.",
                    evidence_from_question=f"The physical count is {'lower' if is_deficit else 'higher'} than the stock per records by R{int(variance_amount):,}.",
                    rule_or_principle="A stock deficit is treated as a loss, while a stock surplus increases the stock asset first.",
                    how_to_derive=f"Debit {journal_dr_details} for the variance amount.",
                    transfer_tip="First decide whether the stock count reveals a shortage or an excess, then choose the correct account side.",
                ),
                "tsv-j-cr-details": _teaching_hint(
                    role_in_requirement="This cell names the account credited in the stock-variance adjustment.",
                    evidence_from_question="Trading stock must be adjusted to the physical count, and the opposite side records the loss or gain.",
                    rule_or_principle="The adjustment entry must both update Trading stock and recognise the stock variance in profit determination.",
                    method_or_formula=f"Credit {journal_cr_details} with R{int(variance_amount):,}.",
                    record_link="This credit must agree with the ledger posting that updates Trading stock or the variance account before closing to Profit and loss.",
                    how_to_derive=f"Credit {journal_cr_details} with the same variance amount.",
                    transfer_tip="Use the opposite side of the entry to make sure Trading stock ends at the physical count.",
                ),
                "tsv-j-dr-amount": _teaching_hint(
                    role_in_requirement="This cell records the debit amount of the stock-variance journal entry.",
                    evidence_from_question=f"The difference between stock per records and the physical count is R{int(variance_amount):,}.",
                    rule_or_principle="The journal uses the stock-count difference as the adjustment amount, whether the difference is a deficit or a surplus.",
                    method_or_formula=f"Use the variance amount R{int(variance_amount):,} on the debit side.",
                    record_link="This amount must match the credit amount and the linked ledger postings in Trading stock and the variance account.",
                    how_to_derive="Calculate the difference between stock per records and physical stock, then use that variance amount in the journal.",
                    transfer_tip="First work out the variance amount, then decide the account names; the amount itself stays the same on both sides.",
                ),
                "tsv-j-cr-amount": _teaching_hint(
                    role_in_requirement="This cell records the matching credit amount of the stock-variance journal entry.",
                    evidence_from_question=f"The same stock variance of R{int(variance_amount):,} must be posted on both sides of the journal entry.",
                    rule_or_principle="Every journal entry balances, so the stock-variance amount is mirrored on the opposite side.",
                    method_or_formula=f"Credit amount = debit amount = R{int(variance_amount):,}.",
                    record_link="This amount must equal the debit side and then flow into the corresponding ledger accounts.",
                    how_to_derive="Copy the variance amount used on the debit side to the credit side.",
                    transfer_tip="After finding the stock difference once, mirror it exactly on the other side instead of recalculating it.",
                ),
            },
            working_map={
                "tsv-j-dr-details": f"Because the stock difference is {'a deficit' if is_deficit else 'a surplus'}, the debit account is {journal_dr_details}.",
                "tsv-j-cr-details": f"The credit side uses {journal_cr_details} so the entry both adjusts Trading stock and records the variance correctly.",
                "tsv-j-dr-amount": "Use the stock-count difference as the fixed journal amount before you place it into the correct debit account.",
                "tsv-j-cr-amount": "Mirror the same variance amount on the credit side so the stock-adjustment journal balances.",
            },
            guidelines=[
                "Use the stock-count difference as the journal amount.",
                "A deficit records a loss; a surplus records a gain.",
                "The debit and credit amounts must be equal.",
            ],
            marks=8,
        ), "trading_stock_variance_journal_fill", expected_cells=4, amount=variance_amount, amount_cell_ids=["tsv-j-dr-amount", "tsv-j-cr-amount"]))

        stock_debit_amount = variance_amount if not is_deficit else ""
        stock_credit_amount = variance_amount if is_deficit else ""
        variance_debit_amount = variance_amount if is_deficit else ""
        variance_credit_amount = variance_amount if not is_deficit else ""
        variance_close_debit_amount = variance_amount if not is_deficit else ""
        variance_close_credit_amount = variance_amount if is_deficit else ""
        profit_loss_debit_amount = variance_amount if is_deficit else ""
        profit_loss_credit_amount = variance_amount if not is_deficit else ""
        ledger_amount_cell_ids = [
            "tsv-l-var-entry-debit",
            "tsv-l-var-close-credit",
            "tsv-l-pl-debit",
            "tsv-l-stock-credit",
        ] if is_deficit else [
            "tsv-l-stock-debit",
            "tsv-l-var-entry-credit",
            "tsv-l-var-close-debit",
            "tsv-l-pl-credit",
        ]
        ledger_tables = [
            {
                "heading": "Trading stock account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="tsv-l-stock-details"), _cell("GJ"), _cell("", editable=True, cell_id="tsv-l-stock-debit"), _cell("", editable=True, cell_id="tsv-l-stock-credit")],
                ],
            },
            {
                "heading": f"{variance_label} account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="tsv-l-var-entry-details"), _cell("GJ"), _cell("", editable=True, cell_id="tsv-l-var-entry-debit"), _cell("", editable=True, cell_id="tsv-l-var-entry-credit")],
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="tsv-l-var-close-details"), _cell("GJ"), _cell("", editable=True, cell_id="tsv-l-var-close-debit"), _cell("", editable=True, cell_id="tsv-l-var-close-credit")],
                ],
            },
            {
                "heading": "Profit and loss account",
                "headers": ["Date", "Details", "Folio", "Debit", "Credit"],
                "rows": [
                    [_cell("28 Feb 2026"), _cell("", editable=True, cell_id="tsv-l-pl-details"), _cell("GJ"), _cell("", editable=True, cell_id="tsv-l-pl-debit"), _cell("", editable=True, cell_id="tsv-l-pl-credit")],
                ],
            },
        ]
        ledger_correct_map = {
            "tsv-l-stock-details": variance_label,
            "tsv-l-stock-debit": stock_debit_amount,
            "tsv-l-stock-credit": stock_credit_amount,
            "tsv-l-var-entry-details": "Trading stock",
            "tsv-l-var-entry-debit": variance_debit_amount,
            "tsv-l-var-entry-credit": variance_credit_amount,
            "tsv-l-var-close-details": p_and_l_label,
            "tsv-l-var-close-debit": variance_close_debit_amount,
            "tsv-l-var-close-credit": variance_close_credit_amount,
            "tsv-l-pl-details": variance_label,
            "tsv-l-pl-debit": profit_loss_debit_amount,
            "tsv-l-pl-credit": profit_loss_credit_amount,
        }
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="ledger",
            prompt=f"{biz} identified a {variance_label.lower()} of R{int(variance_amount):,}. Post the adjustment and the closing transfer to the General Ledger accounts shown below.",
            tables=ledger_tables,
            correct_map=ledger_correct_map,
            derivation_map={
                "tsv-l-stock-debit": f"For a surplus, increase Trading stock by R{int(variance_amount):,}." if not is_deficit else "Trading stock is not debited in the initial deficit entry.",
                "tsv-l-stock-credit": f"For a deficit, decrease Trading stock by R{int(variance_amount):,}." if is_deficit else "Trading stock is not credited in the initial surplus entry.",
                "tsv-l-pl-debit": f"A stock deficit closes to Profit and loss on the debit side for R{int(variance_amount):,}." if is_deficit else "Profit and loss is not debited when a stock surplus is closed.",
                "tsv-l-pl-credit": f"A stock surplus closes to Profit and loss on the credit side for R{int(variance_amount):,}." if not is_deficit else "Profit and loss is not credited when a stock deficit is closed.",
            },
            cell_hints={
                "tsv-l-stock-details": "The Trading stock account references the stock-variance account in the details column.",
                "tsv-l-stock-debit": "Only a stock surplus increases Trading stock on the debit side.",
                "tsv-l-stock-credit": "Only a stock deficit decreases Trading stock on the credit side.",
                "tsv-l-var-entry-details": "The first entry in the variance account comes from Trading stock.",
                "tsv-l-var-entry-debit": "A deficit puts the loss into the variance account on the debit side.",
                "tsv-l-var-entry-credit": "A surplus puts the gain into the variance account on the credit side.",
                "tsv-l-var-close-details": "The closing transfer goes to Profit and loss.",
                "tsv-l-var-close-debit": "A stock surplus is closed from the variance account on the debit side.",
                "tsv-l-var-close-credit": "A stock deficit is closed from the variance account on the credit side.",
                "tsv-l-pl-details": "Profit and loss references the variance account being closed off.",
                "tsv-l-pl-debit": "Profit and loss is debited when a stock deficit is transferred as an expense.",
                "tsv-l-pl-credit": "Profit and loss is credited when a stock surplus is transferred as income.",
            },
            cell_teaching_map={
                "tsv-l-stock-details": _teaching_hint(
                    role_in_requirement="This cell identifies the opposite account used in the Trading stock ledger posting.",
                    evidence_from_question=f"The stock adjustment is posted against the {variance_label.lower()} account.",
                    rule_or_principle="In the ledger details column, write the account appearing on the opposite side of the double entry.",
                    method_or_formula="Trading stock is adjusted against the stock-variance account for the same variance amount.",
                    record_link="This posting must agree with the General Journal entry that recorded the deficit or surplus.",
                    how_to_derive=f"Use {variance_label} as the details in the Trading stock account because that is the opposing account in the adjustment entry.",
                    transfer_tip="When posting to the ledger, first identify the paired account from the journal entry and use it in the details column.",
                ),
                "tsv-l-stock-debit": _teaching_hint(
                    role_in_requirement="This cell records the debit amount, if any, in the Trading stock account for the stock adjustment.",
                    evidence_from_question=f"The scenario shows {'a surplus' if not is_deficit else 'a deficit'} of R{int(variance_amount):,}.",
                    rule_or_principle="Trading stock is debited when the physical count is higher than the records figure because the asset must be increased; in a deficit, this debit side stays blank.",
                    method_or_formula=f"{'Debit Trading stock with R' + format(int(variance_amount), ',') if not is_deficit else 'Leave the debit side blank because Trading stock is reduced on the credit side in a deficit entry.'}",
                    record_link="This amount must agree with the journal entry that adjusts Trading stock to the physical count.",
                    how_to_derive=f"Because this scenario is {'a surplus' if not is_deficit else 'a deficit'}, {'enter the variance amount on the debit side' if not is_deficit else 'do not place an amount on the debit side of Trading stock'}.",
                    transfer_tip="Ask first whether stock is being increased or decreased; that tells you whether Trading stock takes the debit amount or stays blank there.",
                ),
                "tsv-l-stock-credit": _teaching_hint(
                    role_in_requirement="This cell records the credit amount, if any, in the Trading stock account for the stock adjustment.",
                    evidence_from_question=f"The scenario shows {'a deficit' if is_deficit else 'a surplus'} of R{int(variance_amount):,}.",
                    rule_or_principle="Trading stock is credited when the physical count is lower than the records figure because the asset must be reduced; in a surplus, this credit side stays blank.",
                    method_or_formula=f"{'Credit Trading stock with R' + format(int(variance_amount), ',') if is_deficit else 'Leave the credit side blank because Trading stock is increased on the debit side in a surplus entry.'}",
                    record_link="This amount must agree with the journal entry and ensures the Trading stock asset is reduced to the physical count when there is a deficit.",
                    how_to_derive=f"Because this scenario is {'a deficit' if is_deficit else 'a surplus'}, {'enter the variance amount on the credit side' if is_deficit else 'leave the credit side blank'}.",
                    transfer_tip="If the stock asset must fall to the counted amount, expect the Trading stock account to be credited by the variance.",
                ),
                "tsv-l-var-entry-details": _teaching_hint(
                    role_in_requirement="This cell names the opposite account in the first variance-account posting.",
                    evidence_from_question="The stock-variance account is opened by the journal entry that also updates Trading stock.",
                    rule_or_principle="The details column in a ledger account shows the opposing account from the original journal entry.",
                    method_or_formula="The variance account is posted against Trading stock for the initial adjustment.",
                    record_link="This details entry must match the corresponding Trading stock posting in the adjustment journal and ledger.",
                    how_to_derive="Use Trading stock because that is the account paired with the variance account in the initial adjustment.",
                    transfer_tip="For ledger details, always look back to the journal entry and write the account on the opposite side of that row.",
                ),
                "tsv-l-var-entry-debit": _teaching_hint(
                    role_in_requirement="This cell records the debit amount, if any, in the variance account when the adjustment is first posted.",
                    evidence_from_question=f"The stock difference is {'a deficit' if is_deficit else 'a surplus'} of R{int(variance_amount):,}.",
                    rule_or_principle="A stock deficit is a loss and is first recorded on the debit side of the variance account; a surplus does not use this debit side.",
                    method_or_formula=f"{'Debit the variance account with R' + format(int(variance_amount), ',') if is_deficit else 'Leave the debit side blank because a surplus is first entered on the credit side of the variance account.'}",
                    record_link="This amount must match the Trading stock adjustment and later close to Profit and loss.",
                    how_to_derive=f"Because this scenario is {'a deficit' if is_deficit else 'a surplus'}, {'enter the variance amount on the debit side' if is_deficit else 'leave the debit side blank'}.",
                    transfer_tip="Decide whether the variance is loss-type or gain-type first; that determines which side of the variance account receives the initial amount.",
                ),
                "tsv-l-var-entry-credit": _teaching_hint(
                    role_in_requirement="This cell records the credit amount, if any, in the variance account when the adjustment is first posted.",
                    evidence_from_question=f"The stock difference is {'a surplus' if not is_deficit else 'a deficit'} of R{int(variance_amount):,}.",
                    rule_or_principle="A stock surplus is a gain and is first recorded on the credit side of the variance account; a deficit does not use this credit side.",
                    method_or_formula=f"{'Credit the variance account with R' + format(int(variance_amount), ',') if not is_deficit else 'Leave the credit side blank because a deficit is first entered on the debit side of the variance account.'}",
                    record_link="This amount must match the Trading stock adjustment and later close to Profit and loss.",
                    how_to_derive=f"Because this scenario is {'a surplus' if not is_deficit else 'a deficit'}, {'enter the variance amount on the credit side' if not is_deficit else 'leave the credit side blank'}.",
                    transfer_tip="If the variance increases profit, expect the variance account to receive its opening amount on the credit side.",
                ),
                "tsv-l-var-close-details": _teaching_hint(
                    role_in_requirement="This cell names the account used to close the stock-variance account at year-end.",
                    evidence_from_question=f"The {variance_label.lower()} must affect the business's profit determination for the period.",
                    rule_or_principle="Stock deficit and stock surplus accounts are closed to the Profit and loss account at year-end.",
                    method_or_formula="Close the stock-variance account to Profit and loss for the same variance amount.",
                    record_link="This closing reference connects the temporary variance account to the final profit determination for the period.",
                    how_to_derive="Use Profit and loss as the closing-entry details account.",
                    transfer_tip="After posting the adjustment, ask where that income or expense account is transferred during closing.",
                ),
                "tsv-l-var-close-debit": _teaching_hint(
                    role_in_requirement="This cell records the debit amount, if any, for closing the variance account to Profit and loss.",
                    evidence_from_question=f"The variance is {'a surplus' if not is_deficit else 'a deficit'} of R{int(variance_amount):,}.",
                    rule_or_principle="A credit-balance stock surplus account is closed by debiting it for the same amount before the gain appears in Profit and loss.",
                    method_or_formula=f"{'Debit the variance account with R' + format(int(variance_amount), ',') + ' to close the surplus.' if not is_deficit else 'Leave the debit side blank because a deficit account closes on the credit side.'}",
                    record_link="This closing amount must match the Profit and loss credit entry when a surplus is transferred.",
                    how_to_derive=f"Because this scenario is {'a surplus' if not is_deficit else 'a deficit'}, {'enter the variance amount on the debit side of the closing row' if not is_deficit else 'leave this debit side blank'}.",
                    transfer_tip="For closing entries, reverse the side on which the temporary income/expense account first received its balance.",
                ),
                "tsv-l-var-close-credit": _teaching_hint(
                    role_in_requirement="This cell records the credit amount, if any, for closing the variance account to Profit and loss.",
                    evidence_from_question=f"The variance is {'a deficit' if is_deficit else 'a surplus'} of R{int(variance_amount):,}.",
                    rule_or_principle="A debit-balance stock deficit account is closed by crediting it for the same amount before the loss appears in Profit and loss.",
                    method_or_formula=f"{'Credit the variance account with R' + format(int(variance_amount), ',') + ' to close the deficit.' if is_deficit else 'Leave the credit side blank because a surplus account closes on the debit side.'}",
                    record_link="This closing amount must match the Profit and loss debit entry when a deficit is transferred.",
                    how_to_derive=f"Because this scenario is {'a deficit' if is_deficit else 'a surplus'}, {'enter the variance amount on the credit side of the closing row' if is_deficit else 'leave this credit side blank'}.",
                    transfer_tip="A temporary loss account usually closes on the credit side so the matching debit can go to Profit and loss.",
                ),
                "tsv-l-pl-debit": _teaching_hint(
                    role_in_requirement="This cell records the amount debited to Profit and loss when a stock deficit is closed.",
                    evidence_from_question=f"The scenario shows a {variance_label.lower()} of R{int(variance_amount):,}.",
                    rule_or_principle="A stock deficit is a loss and therefore closes to Profit and loss on the debit side.",
                    method_or_formula=f"If the variance is a deficit, debit Profit and loss with R{int(variance_amount):,}; otherwise leave this side blank.",
                    record_link="This closing transfer is how the stock loss affects the period profit figure.",
                    how_to_derive=f"Because this scenario is {'a deficit' if is_deficit else 'a surplus'}, {'enter R' + format(int(variance_amount), ',') if is_deficit else 'leave the debit side blank'}.",
                    transfer_tip="Ask whether the variance is an expense or income effect before deciding which side of Profit and loss is used.",
                ),
                "tsv-l-pl-credit": _teaching_hint(
                    role_in_requirement="This cell records the amount credited to Profit and loss when a stock surplus is closed.",
                    evidence_from_question=f"The scenario shows a {variance_label.lower()} of R{int(variance_amount):,}.",
                    rule_or_principle="A stock surplus increases profit and therefore closes to Profit and loss on the credit side.",
                    method_or_formula=f"If the variance is a surplus, credit Profit and loss with R{int(variance_amount):,}; otherwise leave this side blank.",
                    record_link="This closing transfer is how the stock gain affects the period profit figure.",
                    how_to_derive=f"Because this scenario is {'a surplus' if not is_deficit else 'a deficit'}, {'enter R' + format(int(variance_amount), ',') if not is_deficit else 'leave the credit side blank'}.",
                    transfer_tip="Income-type transfers close to the credit side of Profit and loss, while expense-type transfers close to the debit side.",
                ),
                "tsv-l-pl-details": _teaching_hint(
                    role_in_requirement="This cell shows which account is being transferred into Profit and loss.",
                    evidence_from_question=f"The closing transfer comes from the {variance_label.lower()} account.",
                    rule_or_principle="Profit and loss receives the closing entry from the stock-variance account so the period result reflects the variance.",
                    how_to_derive=f"Use {variance_label} as the details in the Profit and loss account.",
                    transfer_tip="On closing entries, the receiving account shows the account being transferred in the details column.",
                ),
            },
            working_map={
                "tsv-l-stock-details": "The Trading stock account is adjusted against the stock-variance account before the variance is closed to Profit and loss.",
                "tsv-l-stock-debit": "Use the Trading stock debit only for a surplus, because that is when the asset must increase to the counted amount.",
                "tsv-l-stock-credit": "Use the Trading stock credit only for a deficit, because that is when the asset must be reduced to the counted amount.",
                "tsv-l-var-entry-details": "Open the variance account against Trading stock first, then close that temporary account to Profit and loss.",
                "tsv-l-var-entry-debit": "A deficit starts in the variance account on the debit side; a surplus leaves this side blank.",
                "tsv-l-var-entry-credit": "A surplus starts in the variance account on the credit side; a deficit leaves this side blank.",
                "tsv-l-var-close-debit": "Close a surplus by debiting the variance account before crediting Profit and loss.",
                "tsv-l-var-close-credit": "Close a deficit by crediting the variance account before debiting Profit and loss.",
                "tsv-l-pl-debit": "Use the variance amount on the debit side only when the stock difference is a deficit (loss).",
                "tsv-l-pl-credit": "Use the variance amount on the credit side only when the stock difference is a surplus (gain).",
            },
            guidelines=[
                "First post the stock-variance adjustment to Trading stock and the variance account.",
                "Then close the variance account to Profit and loss.",
                "Use the same variance amount throughout the ledger postings.",
            ],
            marks=12,
        ), "trading_stock_variance_ledger_fill", expected_cells=12, amount=variance_amount, amount_cell_ids=ledger_amount_cell_ids))

        final_accounts_tables = [
            {
                "heading": "Profit and Loss Account (extract)",
                "headers": ["Item", "Amount"],
                "rows": [[_cell(variance_label), _cell("", editable=True, cell_id="tsv-fa-variance")]],
            },
            {
                "heading": "Balance Sheet (extract)",
                "headers": ["Current assets", "Amount"],
                "rows": [[_cell("Trading stock"), _cell("", editable=True, cell_id="tsv-fa-stock")]],
            },
        ]
        pool.append(_with_validation(_make_fill_in_table_question(
            question_type="final_account_table",
            prompt=f"Use the stock information below to carry the effect of the {variance_label.lower()} into the Profit and Loss Account and the Balance Sheet extracts.",
            prompt_table={
                "heading": "Source stock information",
                "headers": ["Item", "Amount"],
                "rows": [
                    [_cell("Trading stock per records"), _cell(scenario["per_records"])],
                    [_cell("Physical stock count"), _cell(scenario["actual_count"])],
                    [_cell(variance_label), _cell(variance_amount)],
                ],
            },
            tables=final_accounts_tables,
            correct_map={
                "tsv-fa-variance": variance_amount,
                "tsv-fa-stock": adjusted_stock,
            },
            derivation_map={
                "tsv-fa-variance": f"Carry the {variance_label.lower()} amount to Profit and loss: R{int(variance_amount):,}.",
                "tsv-fa-stock": f"Trading stock in the Balance Sheet must equal the physical stock count: R{int(adjusted_stock):,}.",
            },
            cell_hints={
                "tsv-fa-variance": f"The {variance_label.lower()} affects Profit and loss for the period.",
                "tsv-fa-stock": "Use the physical stock count as the final Trading stock figure.",
            },
            cell_teaching_map={
                "tsv-fa-variance": _teaching_hint(
                    role_in_requirement="This cell carries the stock variance into the Profit and Loss Account.",
                    evidence_from_question=f"The source table already gives the {variance_label.lower()} as R{int(variance_amount):,}.",
                    rule_or_principle="Trading stock deficits and surpluses are transferred to Profit and loss so they affect the year's result.",
                    method_or_formula=f"Carry R{int(variance_amount):,} to the {variance_label} line in Profit and loss.",
                    record_link="This amount must match the closing transfer from the stock-variance ledger account.",
                    how_to_derive=f"Copy R{int(variance_amount):,} into the {variance_label} line in the Profit and Loss Account extract.",
                    transfer_tip="When a question asks for statement carry-through, move the already-determined adjustment amount into the correct statement section.",
                ),
                "tsv-fa-stock": _teaching_hint(
                    role_in_requirement="This cell shows the final Trading stock figure in the Balance Sheet.",
                    evidence_from_question=f"The physical stock count is R{int(adjusted_stock):,}, which is the amount the stock asset must be shown at after adjustment.",
                    rule_or_principle="The Balance Sheet reports Trading stock at the adjusted physical count, not at the pre-adjustment records figure.",
                    method_or_formula=f"Use the physical stock count: R{int(adjusted_stock):,}.",
                    record_link="This stock figure is the adjusted asset balance after the journal and ledger postings update Trading stock.",
                    how_to_derive=f"Use the physical count amount R{int(adjusted_stock):,} for Trading stock.",
                    transfer_tip="Where stock is adjusted to a physical count, the Balance Sheet carries the counted amount after the variance has been recorded.",
                ),
            },
            working_map={
                "tsv-fa-variance": "Carry the temporary variance account through to Profit and loss because that is where the gain or loss affects the period result.",
                "tsv-fa-stock": "Carry the counted stock amount, not the old records amount, because the balance sheet must show stock at the physical count after adjustment.",
            },
            guidelines=[
                "Carry the stock variance to Profit and loss.",
                "Carry the physical stock count to Trading stock in the Balance Sheet.",
            ],
            marks=4,
        ), "trading_stock_variance_carrythrough_fill", expected_cells=2, amount=variance_amount, adjusted_stock=adjusted_stock, amount_cell_id="tsv-fa-variance", adjusted_stock_cell_id="tsv-fa-stock"))

    return pool
