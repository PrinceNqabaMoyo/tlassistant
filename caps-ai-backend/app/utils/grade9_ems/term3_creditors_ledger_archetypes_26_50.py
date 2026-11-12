"""Grade 9 EMS — Credit Transactions (Creditors 2): Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards (Term 3: Financial Literacy).
Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Creditors 2).md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES

from .term3_creditors_ledger_archetypes_01_25 import (
    SUPPLIER_NAMES,
    TRADER_NAMES,
    _fmt_comma,
    _fmt_zar,
    _mcq,
    _svg_bar_chart,
    _svg_linear_flow,
    _table_q,
    _typed,
)


def arch_26_general_ledger_creditors_control_t_account_structure(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    prompt = (
        f"When drawing up the General Ledger **Creditors Control (B6)** T-account for {trader}, bookkeepers post "
        f"month-end journal totals and opening/closing balances.\n\n"
        f"Which pair of entries correctly appears on the CREDIT side of Creditors Control?"
    )
    correct = "Balance b/d (opening total owed) and Sundry purchases CJ (total credit invoices)"
    distractors = [
        "Bank CPJ (total payments made) and Balance c/d (closing total owed)",
        "Sales DJ (credit sales) and Cost of sales CRJ",
        "Drawings CPJ and Cash float b/d",
    ]
    return _mcq(
        rng,
        subskill="26_general_ledger_creditors_control_t_account_structure",
        title="Creditors Control General Ledger Account Structure",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Creditors Control is a Liability account: Opening Balance b/d and monthly Sundry purchases (CJ) increase the "
            "liability on the Credit side, whereas Bank (CPJ) payments and Balance c/d sit on the Debit side."
        ),
        hints={
            "tier_1": "Creditors Control is a Current Liability: which side holds the opening balance and increases?",
            "tier_2": "Credit side increases liabilities (`Balance b/d` + `Sundry purchases CJ`); Debit side decreases (`Bank CPJ`).",
            "tier_3": "Select 'Balance b/d (opening total owed) and Sundry purchases CJ (total credit invoices)'.",
        },
        learning_objective_id="lo_c2_gl_control_structure",
        concept_id="creditors_control_t_account",
        misconception_tags=["puts_cpj_payments_on_credit_side"],
    )


def arch_27_calculating_closing_creditors_control_balance(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    open_bal = rng.choice([435918, 284500, 315400])
    cj_tot = rng.choice([502172, 340200, 412800])
    cpj_tot = rng.choice([522913, 310600, 395100])
    close_bal = open_bal + cj_tot - cpj_tot

    prompt = (
        f"At {trader}, the General Ledger Creditors Control account shows the following monthly totals:\n"
        f"- Oct 01: Total owing to creditors (`Balance b/d`) = {_fmt_zar(open_bal)}\n"
        f"- Oct 31: Total credit purchases (`Sundry purchases CJ`) = {_fmt_zar(cj_tot)}\n"
        f"- Oct 31: Total payments to creditors (`Bank CPJ`) = {_fmt_zar(cpj_tot)}\n\n"
        f"Calculate the closing `Balance c/d` of Creditors Control on 31 October."
    )
    return _typed(
        rng,
        subskill="27_calculating_closing_creditors_control_balance",
        title="Balancing the Creditors Control Account",
        prompt=prompt,
        sample_answer=(
            f"Total Credit side = {_fmt_zar(open_bal)} + {_fmt_zar(cj_tot)} = {_fmt_zar(open_bal + cj_tot)}\n"
            f"Closing Balance c/d = {_fmt_zar(open_bal + cj_tot)} - {_fmt_zar(cpj_tot)} = {_fmt_zar(close_bal)}"
        ),
        marking_points=[
            f"Add opening balance + CJ purchases = {_fmt_zar(open_bal + cj_tot)} [1]",
            f"Subtract CPJ payments ({_fmt_zar(cpj_tot)}) = {_fmt_zar(close_bal)} [2]",
        ],
        hints={
            "tier_1": "Sum the two Credit-side amounts first (Balance b/d + Sundry purchases CJ).",
            "tier_2": f"Subtract total CPJ payments ({_fmt_zar(cpj_tot)}) to find closing Balance c/d.",
            "tier_3": f"({_fmt_zar(open_bal)} + {_fmt_zar(cj_tot)}) - {_fmt_zar(cpj_tot)} = {_fmt_zar(close_bal)}.",
        },
        learning_objective_id="lo_c2_closing_control_calc",
        concept_id="creditors_control_closing_balance",
        misconception_tags=["subtracts_cj_purchases_instead_of_cpj"],
        marks=3,
        correct_answer=_fmt_zar(close_bal),
        correct_value=float(close_bal),
        worked_solution=f"Credit total = {open_bal + cj_tot}; Closing c/d = {open_bal + cj_tot} - {cpj_tot} = {_fmt_zar(close_bal)}",
    )


def arch_28_general_ledger_creditors_control_2d_table(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    open_bal = rng.choice([5887, 8450, 11200])
    cj_tot = rng.choice([10590, 14200, 16800])
    cpj_tot = rng.choice([2422, 5100, 6400])
    tot_cr = open_bal + cj_tot
    close_bal = tot_cr - cpj_tot

    headers = ["Dr Date / Details", "Dr Fol.", "Dr Amount (R)", "Cr Date / Details", "Cr Fol.", "Cr Amount (R)"]
    raw_rows = [
        [
            {"type": "given", "value": "Jul 31 Bank"},
            {"type": "given", "value": "CPJ"},
            {"type": "given", "value": _fmt_zar(cpj_tot)},
            {"type": "given", "value": "Jul 01 Balance"},
            {"type": "given", "value": "b/d"},
            {"type": "given", "value": _fmt_zar(open_bal)},
        ],
        [
            {"type": "given", "value": "Jul 31 Balance"},
            {"type": "given", "value": "c/d"},
            {"type": "required", "expected": _fmt_zar(close_bal)},
            {"type": "given", "value": "Jul 31 Sundry purchases"},
            {"type": "given", "value": "CJ"},
            {"type": "given", "value": _fmt_zar(cj_tot)},
        ],
        [
            {"type": "given", "value": "Account Total"},
            {"type": "must_be_empty"},
            {"type": "required", "expected": _fmt_zar(tot_cr)},
            {"type": "given", "value": "Account Total"},
            {"type": "must_be_empty"},
            {"type": "required", "expected": _fmt_zar(tot_cr)},
        ],
        [
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "given", "value": "Aug 01 Balance"},
            {"type": "required", "expected": "b/d"},
            {"type": "required", "expected": _fmt_zar(close_bal)},
        ],
    ]
    cell_hints = {
        "r1_c2": f"Balance c/d = Credit total ({_fmt_zar(tot_cr)}) - Bank CPJ ({_fmt_zar(cpj_tot)}).",
        "r2_c2": f"Both Debit and Credit totals equal {_fmt_zar(tot_cr)}.",
        "r2_c5": f"Sum Credit side: {_fmt_zar(open_bal)} + {_fmt_zar(cj_tot)}.",
        "r3_c4": "New month brought-down folio: 'b/d'.",
        "r3_c5": f"Bring closing Balance c/d down to Credit opening side: {_fmt_zar(close_bal)}.",
    }
    derivations = [
        f"Credit total = {_fmt_zar(open_bal)} + {_fmt_zar(cj_tot)} = {_fmt_zar(tot_cr)}.",
        f"Balance c/d (Jul 31 Dr) = {_fmt_zar(tot_cr)} - {_fmt_zar(cpj_tot)} = {_fmt_zar(close_bal)}.",
        f"Aug 01 Balance b/d (Cr) = {_fmt_zar(close_bal)} with folio 'b/d'.",
    ]
    return _table_q(
        rng,
        subskill="28_general_ledger_creditors_control_2d_table",
        title=f"General Ledger: Creditors Control T-Account ({trader})",
        prompt=(
            f"Balance the General Ledger Creditors Control account of {trader} for July (Opening b/d {_fmt_zar(open_bal)}, "
            f"CJ purchases {_fmt_zar(cj_tot)}, CPJ Bank payments {_fmt_zar(cpj_tot)}) and bring down Aug 01 Balance b/d. "
            f"Leave shaded cells empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "First add the two Credit amounts to establish the larger side total.",
            "tier_2": "Subtract Dr Bank CPJ from that total to get Balance c/d, then bring it down to Aug 01 Credit b/d.",
            "tier_3": f"Total={_fmt_zar(tot_cr)}; Balance c/d and Aug 01 b/d={_fmt_zar(close_bal)}.",
        },
        learning_objective_id="lo_c2_gl_control_t_table",
        concept_id="general_ledger_creditors_control_table",
        misconception_tags=["brings_bd_down_on_debit_side", "fills_must_be_empty_cell"],
        journal_type="general_ledger",
    )


def arch_29_balancing_creditors_control_next_month_bd(rng: random.Random) -> Dict[str, Any]:
    close_bal = rng.choice([14055, 28629, 31608])
    prompt = (
        f"When closing Creditors Control on 31 July, a bookkeeper writes `Balance c/d` ({_fmt_zar(close_bal)}) on the "
        f"DEBIT side above the totals, and then writes `Balance b/d` ({_fmt_zar(close_bal)}) on 1 August on the CREDIT side.\n\n"
        f"Explain why `Balance c/d` appears on the Debit side even though a creditor's true balance on 1 August is a CREDIT balance."
    )
    return _typed(
        rng,
        subskill="29_balancing_creditors_control_next_month_bd",
        title="Understanding Balance c/d vs Balance b/d in Creditors Control",
        prompt=prompt,
        sample_answer=(
            f"Because the Credit side exceeds the Debit side by {_fmt_zar(close_bal)}, `Balance c/d` acts as a temporary "
            f"balancing figure on the shorter Debit side so both totals match at month-end. On 1 August, the true "
            f"opening Liability balance (`Balance b/d`, {_fmt_zar(close_bal)}) is brought down onto the Credit side."
        ),
        marking_points=[
            "Explains `Balance c/d` sits on the shorter (Debit) side solely to equalize month-end T-account totals [1]",
            "Explains `Balance b/d` moves back to the Credit side on the 1st because Creditors Control is a Liability [1]",
        ],
        hints={
            "tier_1": "Which side of a liability account is normally larger before balancing?",
            "tier_2": "c/d = carried down (balances the shorter side); b/d = brought down (true opening balance side).",
            "tier_3": "c/d equalizes the shorter Debit side at month-end; true Liability b/d restarts on Credit on the 1st.",
        },
        learning_objective_id="lo_c2_cd_vs_bd_logic",
        concept_id="balance_cd_vs_bd",
        misconception_tags=["thinks_debit_cd_means_asset_balance"],
        marks=2,
    )


def arch_30_creditors_list_purpose_internal_control(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    ctrl_bal = rng.choice([28629, 41517, 55967])
    prompt = (
        f"At month-end, {trader}'s bookkeeper lists all individual closing supplier balances from the Creditors Ledger "
        f"and compares their sum against the closing balance of General Ledger Creditors Control ({_fmt_zar(ctrl_bal)}).\n\n"
        f"What is the PRIMARY accounting purpose of compiling this Creditors List?"
    )
    correct = (
        "Internal control — verifying that individual Creditors Ledger postings agree mathematically with the summary Creditors Control account"
    )
    distractors = [
        "Calculating VAT refunds owed to overseas employees",
        "Replacing the Cash Receipts Journal for daily shop till sales",
        "Deleting settled supplier accounts permanently from the accounting archive",
    ]
    return _mcq(
        rng,
        subskill="30_creditors_list_purpose_internal_control",
        title="Creditors List as Internal Control",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Because Creditors Control posts monthly totals while the Creditors Ledger records daily entries per supplier, "
            "reconciling their totals detects arithmetic, omission, or reversal posting errors immediately."
        ),
        hints={
            "tier_1": "Why compare the sum of all individual supplier accounts against one control account?",
            "tier_2": "Matching individual details to the summary total detects bookkeeping mistakes.",
            "tier_3": "Select 'Internal control — verifying that individual Creditors Ledger postings agree mathematically with the summary Creditors Control account'.",
        },
        learning_objective_id="lo_c2_creditors_list_control",
        concept_id="creditors_list_internal_control",
        misconception_tags=["thinks_creditors_list_replaces_general_ledger"],
    )


def arch_31_compiling_creditors_list_2d_table(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    b1 = rng.randint(12, 34) * 100
    b2 = rng.randint(8, 22) * 100
    b3 = rng.randint(15, 38) * 100
    b4 = rng.randint(4, 14) * 100
    total = b1 + b2 + b3 + b4

    headers = ["Folio", "Creditor Name", "Closing Balance (R)", "Reconciled"]
    raw_rows = [
        [{"type": "given", "value": "C1"}, {"type": "given", "value": SUPPLIER_NAMES[0]}, {"type": "required", "expected": _fmt_zar(b1)}, {"type": "must_be_empty"}],
        [{"type": "given", "value": "C2"}, {"type": "given", "value": SUPPLIER_NAMES[1]}, {"type": "required", "expected": _fmt_zar(b2)}, {"type": "must_be_empty"}],
        [{"type": "given", "value": "C3"}, {"type": "given", "value": SUPPLIER_NAMES[2]}, {"type": "required", "expected": _fmt_zar(b3)}, {"type": "must_be_empty"}],
        [{"type": "given", "value": "C4"}, {"type": "given", "value": SUPPLIER_NAMES[3]}, {"type": "required", "expected": _fmt_zar(b4)}, {"type": "must_be_empty"}],
        [{"type": "given", "value": "B6"}, {"type": "given", "value": "Total Creditors Control"}, {"type": "required", "expected": _fmt_zar(total)}, {"type": "must_be_empty"}],
    ]
    cell_hints = {
        "r0_c2": f"C1 closing balance: {_fmt_zar(b1)}.",
        "r1_c2": f"C2 closing balance: {_fmt_zar(b2)}.",
        "r2_c2": f"C3 closing balance: {_fmt_zar(b3)}.",
        "r3_c2": f"C4 closing balance: {_fmt_zar(b4)}.",
        "r4_c2": "Add C1 + C2 + C3 + C4.",
    }
    derivations = [
        f"C1={_fmt_zar(b1)}, C2={_fmt_zar(b2)}, C3={_fmt_zar(b3)}, C4={_fmt_zar(b4)}.",
        f"Total Creditors List = {_fmt_zar(b1)} + {_fmt_zar(b2)} + {_fmt_zar(b3)} + {_fmt_zar(b4)} = {_fmt_zar(total)} (matches B6 Creditors Control).",
    ]
    return _table_q(
        rng,
        subskill="31_compiling_creditors_list_2d_table",
        title=f"Creditors List Schedule ({trader})",
        prompt=(
            f"Compile the month-end Creditors List of {trader} using closing ledger balances: C1 {SUPPLIER_NAMES[0]} "
            f"{_fmt_zar(b1)}, C2 {SUPPLIER_NAMES[1]} {_fmt_zar(b2)}, C3 {SUPPLIER_NAMES[2]} {_fmt_zar(b3)}, C4 "
            f"{SUPPLIER_NAMES[3]} {_fmt_zar(b4)}. Leave 'Reconciled' empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Enter each creditor's closing balance in its matching row.",
            "tier_2": "Sum all four supplier balances to get the Total Creditors Control line.",
            "tier_3": f"Total Creditors Control = {_fmt_zar(total)}.",
        },
        learning_objective_id="lo_c2_creditors_list_table",
        concept_id="creditors_list_schedule",
        misconception_tags=["arithmetic_addition_error_in_list", "fills_must_be_empty_cell"],
        journal_type="creditors_list",
    )


def arch_32_reconciling_creditors_list_with_control_discrepancy(rng: random.Random) -> Dict[str, Any]:
    ctrl_bal = rng.choice([14055, 18420, 22800])
    omitted_inv = rng.choice([450, 680, 920])
    list_bal = ctrl_bal - omitted_inv
    prompt = (
        f"On 31 July, the General Ledger **Creditors Control** balance is {_fmt_zar(ctrl_bal)}, whereas the **Creditors List** "
        f"totals only {_fmt_zar(list_bal)}. Investigation shows one supplier invoice entered in CJ was NOT posted to "
        f"C2's Creditors Ledger card.\n\n"
        f"Calculate the missing invoice amount that reconciles the Creditors List to Creditors Control."
    )
    return _typed(
        rng,
        subskill="32_reconciling_creditors_list_with_control_discrepancy",
        title="Reconciling a Creditors Control Discrepancy",
        prompt=prompt,
        sample_answer=(
            f"Discrepancy = {_fmt_zar(ctrl_bal)} - {_fmt_zar(list_bal)} = {_fmt_zar(omitted_inv)}.\n"
            f"Crediting {_fmt_zar(omitted_inv)} to C2's Creditors Ledger brings the Creditors List up to {_fmt_zar(ctrl_bal)}."
        ),
        marking_points=[
            f"Compute discrepancy: {_fmt_zar(ctrl_bal)} - {_fmt_zar(list_bal)} = {_fmt_zar(omitted_inv)} [1]",
            "States missing invoice must be posted to Credit (+) of C2's Creditors Ledger card [1]",
        ],
        hints={
            "tier_1": "Compare the General Ledger control balance with the Creditors List total.",
            "tier_2": f"Subtract {_fmt_zar(list_bal)} from {_fmt_zar(ctrl_bal)}.",
            "tier_3": f"{_fmt_zar(ctrl_bal)} - {_fmt_zar(list_bal)} = {_fmt_zar(omitted_inv)}.",
        },
        learning_objective_id="lo_c2_reconcile_discrepancy",
        concept_id="creditors_reconciliation_discrepancy",
        misconception_tags=["adjusts_control_instead_of_omitted_ledger"],
        marks=2,
        correct_answer=_fmt_zar(omitted_inv),
        correct_value=float(omitted_inv),
        worked_solution=f"Missing invoice = {ctrl_bal} - {list_bal} = {_fmt_zar(omitted_inv)}",
    )


def arch_33_multi_supplier_ledger_to_control_synthesis(rng: random.Random) -> Dict[str, Any]:
    c1_open, c2_open, c3_open = rng.randint(18, 25) * 100, rng.randint(12, 18) * 100, rng.randint(20, 28) * 100
    c1_cj, c2_cj, c3_cj = rng.randint(15, 25) * 100, rng.randint(18, 24) * 100, rng.randint(10, 16) * 100
    c2_pay, c3_pay = c2_open, rng.randint(8, 12) * 100
    tot_open = c1_open + c2_open + c3_open
    tot_cj = c1_cj + c2_cj + c3_cj
    tot_cpj = c2_pay + c3_pay
    closing = tot_open + tot_cj - tot_cpj

    prompt = (
        f"Across three creditors of Neverland Suppliers in July:\n"
        f"- C1: Opening {_fmt_zar(c1_open)}, CJ invoice {_fmt_zar(c1_cj)}, CPJ payment R0\n"
        f"- C2: Opening {_fmt_zar(c2_open)}, CJ invoice {_fmt_zar(c2_cj)}, CPJ payment {_fmt_zar(c2_pay)}\n"
        f"- C3: Opening {_fmt_zar(c3_open)}, CJ invoice {_fmt_zar(c3_cj)}, CPJ payment {_fmt_zar(c3_pay)}\n\n"
        f"Calculate the combined month-end closing **Creditors Control** balance owed across all three suppliers."
    )
    return _typed(
        rng,
        subskill="33_multi_supplier_ledger_to_control_synthesis",
        title="Multi-Supplier Ledger to Control Total",
        prompt=prompt,
        sample_answer=(
            f"Total Opening b/d = {_fmt_zar(tot_open)}\n"
            f"Total CJ Purchases = {_fmt_zar(tot_cj)}\n"
            f"Total CPJ Payments = {_fmt_zar(tot_cpj)}\n"
            f"Closing Creditors Control = {_fmt_zar(tot_open)} + {_fmt_zar(tot_cj)} - {_fmt_zar(tot_cpj)} = {_fmt_zar(closing)}"
        ),
        marking_points=[
            f"Sum Opening balances ({_fmt_zar(tot_open)}) and CJ purchases ({_fmt_zar(tot_cj)}) [1]",
            f"Subtract total CPJ payments ({_fmt_zar(tot_cpj)}) [1]",
            f"Closing Creditors Control = {_fmt_zar(closing)} [1]",
        ],
        hints={
            "tier_1": "Either compute each supplier's closing balance and sum them, OR sum Opening + CJ - CPJ.",
            "tier_2": f"Opening={_fmt_zar(tot_open)}, CJ={_fmt_zar(tot_cj)}, CPJ={_fmt_zar(tot_cpj)}.",
            "tier_3": f"{_fmt_zar(tot_open)} + {_fmt_zar(tot_cj)} - {_fmt_zar(tot_cpj)} = {_fmt_zar(closing)}.",
        },
        learning_objective_id="lo_c2_multi_supplier_synthesis",
        concept_id="multi_supplier_control_total",
        misconception_tags=["forgets_to_include_opening_balances"],
        marks=3,
        correct_answer=_fmt_zar(closing),
        correct_value=float(closing),
        worked_solution=f"{tot_open} + {tot_cj} - {tot_cpj} = {_fmt_zar(closing)}",
    )


def arch_34_creditors_payment_to_purchase_ratio_bar_graph(rng: random.Random) -> Dict[str, Any]:
    open_bal = rng.choice([8000, 10000, 12000])
    cj = rng.choice([15000, 18000, 21000])
    cpj = rng.choice([11000, 13000, 14500])
    close = open_bal + cj - cpj

    svg = _svg_bar_chart(
        title="Monthly Creditors Control Activity (R)",
        y_label="Amount (R)",
        bars=[
            ("Opening b/d", float(open_bal), "#64748B"),
            ("CJ Purchases", float(cj), "#DC2626"),
            ("CPJ Payments", float(cpj), "#15803D"),
        ],
        max_val=float(cj + 4000),
        unit_suffix="",
    )
    prompt = (
        f"Refer to the bar graph below displaying monthly Creditors Control activity: Opening b/d ({_fmt_zar(open_bal)}), "
        f"CJ Credit Purchases ({_fmt_zar(cj)}), and CPJ Cheque Payments ({_fmt_zar(cpj)}).\n\n"
        f"Calculate the closing Creditors Control balance at month-end."
    )
    return _typed(
        rng,
        subskill="34_creditors_payment_to_purchase_ratio_bar_graph",
        title="Creditors Activity & Closing Balance (Bar Graph)",
        prompt=prompt,
        sample_answer=f"Closing balance = {_fmt_zar(open_bal)} + {_fmt_zar(cj)} - {_fmt_zar(cpj)} = {_fmt_zar(close)}.",
        marking_points=[
            f"Reads Opening ({_fmt_zar(open_bal)}), CJ ({_fmt_zar(cj)}), and CPJ ({_fmt_zar(cpj)}) from graph [1]",
            f"Computes Closing balance = {_fmt_zar(close)} [2]",
        ],
        hints={
            "tier_1": "Opening b/d + CJ Purchases increases what is owed; CPJ Payments decreases what is owed.",
            "tier_2": f"Evaluate {_fmt_zar(open_bal)} + {_fmt_zar(cj)} - {_fmt_zar(cpj)}.",
            "tier_3": f"{_fmt_zar(open_bal)} + {_fmt_zar(cj)} - {_fmt_zar(cpj)} = {_fmt_zar(close)}.",
        },
        learning_objective_id="lo_c2_activity_bar_graph",
        concept_id="creditors_activity_graph",
        misconception_tags=["subtracts_cj_purchases"],
        marks=3,
        correct_answer=_fmt_zar(close),
        correct_value=float(close),
        diagram_spec={"kind": "inline_svg", "title": "Monthly Creditors Control Activity", "svg": svg, "diagram_role": "context"},
        worked_solution=f"Closing = {open_bal} + {cj} - {cpj} = {_fmt_zar(close)}",
    )


def arch_35_creditors_statement_reconciliation_purpose(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    bal_ledger = rng.choice([6420, 8150, 9300])
    bal_stmt = bal_ledger + rng.choice([750, 1200])
    prompt = (
        f"At month-end, {supplier} mails a monthly Statement of Account showing a balance owing of {_fmt_zar(bal_stmt)}, "
        f"while our Creditors Ledger shows {_fmt_zar(bal_ledger)}.\n\n"
        f"Explain TWO reasons why a bookkeeper always reconciles the Supplier Statement against the Creditors Ledger "
        f"BEFORE issuing a final settlement cheque."
    )
    return _typed(
        rng,
        subskill="35_creditors_statement_reconciliation_purpose",
        title="Reconciling Supplier Statements Before Payment",
        prompt=prompt,
        sample_answer=(
            f"1. Prevents overpaying or duplicate payments: Detects supplier billing errors, missing credit notes for returns, "
            f"or unrecorded invoices so we only pay valid verified debts instead of blindly paying {_fmt_zar(bal_stmt)}.\n"
            "2. Identifies timing differences: Explains cheques/EFTs we paid near month-end that have not yet reflected on the supplier's statement."
        ),
        marking_points=[
            "Catches omitted invoices, missing return credit notes, or arithmetic billing errors before paying [1]",
            "Identifies month-end payment timing differences (in-transit EFTs/cheques) to maintain accurate supplier relations [1]",
        ],
        hints={
            "tier_1": "What risks occur if a business pays whatever figure appears on a supplier statement without checking?",
            "tier_2": "Think of BOTH errors/omissions (missing credit notes/invoices) AND late-month payment timing delays.",
            "tier_3": "State preventing overpayments/missing return credits, and accounting for late-month timing differences.",
        },
        learning_objective_id="lo_c2_statement_recon",
        concept_id="supplier_statement_reconciliation",
        misconception_tags=["assumes_supplier_statement_is_always_error_free"],
        marks=2,
    )


def arch_36_statement_reconciliation_timing_differences(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    pay_amt = rng.choice([1800, 2400, 3100])
    prompt = (
        f"On 30 September, a business sends an EFT payment of {_fmt_zar(pay_amt)} to {supplier} (already recorded in CPJ "
        f"and debited in {supplier}'s Creditors Ledger). {supplier}'s statement was printed on 28 September, so the "
        f"{_fmt_zar(pay_amt)} does NOT appear on it.\n\n"
        f"How should the bookkeeper handle this {_fmt_zar(pay_amt)} timing difference?"
    )
    correct = (
        "Note it on the Creditors Reconciliation Statement as an in-transit payment already recorded correctly in our books — do NOT delete our CPJ entry"
    )
    distractors = [
        "Reverse our CPJ entry and mail the supplier a second duplicate payment immediately",
        "Add the payment again to our Credit (+) column in CJ",
        "Write off the entire creditor account as a bad debt",
    ]
    return _mcq(
        rng,
        subskill="36_statement_reconciliation_timing_differences",
        title="Handling Statement Reconciliation Timing Differences",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Because {supplier} printed their statement on 28 Sept before receiving the 30 Sept payment, our CPJ/Creditors "
            f"Ledger entry is correct; it is simply a timing difference shown on the reconciliation."
        ),
        hints={
            "tier_1": "Was our CPJ payment entry on 30 September wrong, or simply later than the statement cut-off date?",
            "tier_2": "Never reverse a valid payment or pay twice because of a statement cut-off date.",
            "tier_3": "Select 'Note it on the Creditors Reconciliation Statement as an in-transit payment already recorded correctly in our books — do NOT delete our CPJ entry'.",
        },
        learning_objective_id="lo_c2_timing_differences",
        concept_id="reconciliation_timing_difference",
        misconception_tags=["pays_twice_for_in_transit_payment"],
    )


def arch_37_invoice_vs_creditors_journal_sundry_allocation(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    amt = rng.choice([4881, 6600, 8118])
    prompt = (
        f"{trader}'s Creditors Journal has fixed analysis columns ONLY for `Creditors control`, `Trading stock`, and "
        f"`Stationery`, plus a `Sundry accounts` section. Today {trader} buys shop shelving (`Equipment`) on credit for {_fmt_zar(amt)}.\n\n"
        f"Where is {_fmt_zar(amt)} recorded in the Creditors Journal besides `Creditors control`?"
    )
    correct = "Sundry accounts (Amount, Fol., and Details written as Equipment)"
    distractors = [
        "Trading stock column — because Equipment is bought on credit",
        "Stationery column — because there is no Equipment column",
        "Cash Payments Journal Bank column — even though no cash was paid",
    ]
    return _mcq(
        rng,
        subskill="37_invoice_vs_creditors_journal_sundry_allocation",
        title="Allocating Non-Stock Credit Purchases to Sundry Accounts",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Any account lacking a dedicated analysis column in CJ (such as Equipment, Vehicles, Packing material, or "
            "Repairs) is entered in `Sundry accounts` with its exact account title under Details."
        ),
        hints={
            "tier_1": "Does CJ have an Equipment column here? No!",
            "tier_2": "Items without their own dedicated column go into Sundry accounts.",
            "tier_3": "Select 'Sundry accounts (Amount, Fol., and Details written as Equipment)'.",
        },
        learning_objective_id="lo_c2_cj_sundry_allocation",
        concept_id="cj_sundry_accounts",
        misconception_tags=["forces_equipment_into_trading_stock"],
    )


def arch_38_debit_note_caj_effect_on_creditor_balance(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    ret_amt = rng.choice([420, 650, 880])
    prompt = (
        f"A shop discovers {_fmt_zar(ret_amt)} of damaged stock delivered by {supplier} and issues Debit Note 33, "
        f"recorded in the Creditors Allowance Journal (CAJ).\n\n"
        f"How does this CAJ entry post to General Ledger `Creditors control` and `{supplier}`'s Creditors Ledger card?"
    )
    correct = (
        f"Debits Creditors control in General Ledger and posts {_fmt_zar(ret_amt)} to the Debit (-) column of {supplier}'s Creditors Ledger"
    )
    distractors = [
        f"Credits Creditors control and adds {_fmt_zar(ret_amt)} to what we owe {supplier}",
        f"Debits Debtors control and reduces customer balances instead",
        f"Increases Bank cash by {_fmt_zar(ret_amt)} in the Cash Receipts Journal",
    ]
    return _mcq(
        rng,
        subskill="38_debit_note_caj_effect_on_creditor_balance",
        title="Effect of CAJ Debit Notes on Creditors Ledgers",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Returning damaged goods cancels {_fmt_zar(ret_amt)} of liability owed to {supplier}: both Creditors Control "
            f"and the supplier's individual Creditors Ledger card are DEBITED (-)."
        ),
        hints={
            "tier_1": "When you return faulty stock you bought on credit, do you owe the supplier MORE or LESS?",
            "tier_2": "Less liability = Debit (-) side in both General Ledger Control and Creditors Ledger.",
            "tier_3": f"Select 'Debits Creditors control in General Ledger and posts {_fmt_zar(ret_amt)} to the Debit (-) column of {supplier}'s Creditors Ledger'.",
        },
        learning_objective_id="lo_c2_caj_debit_note_effect",
        concept_id="debit_note_caj_posting",
        misconception_tags=["credits_creditor_for_returned_stock"],
    )


def arch_39_partial_settlement_vs_full_settlement_calculation(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    open_bal = rng.choice([5000, 6000, 8000])
    new_inv = rng.choice([2500, 3000, 4000])
    pct_paid = rng.choice([50, 60, 75])
    part_pay = int(round(open_bal * pct_paid / 100.0))
    rem_bal = open_bal + new_inv - part_pay
    prompt = (
        f"An enterprise owes {supplier} {_fmt_zar(open_bal)} on 1 August, buys {_fmt_zar(new_inv)} of stock on credit on "
        f"10 August, and sends a partial settlement payment equal to {pct_paid}% of the opening 1 August balance on 20 August.\n\n"
        f"Calculate the remaining balance still owed to {supplier} after the partial payment."
    )
    return _typed(
        rng,
        subskill="39_partial_settlement_vs_full_settlement_calculation",
        title="Remaining Creditor Balance After Partial Settlement",
        prompt=prompt,
        sample_answer=(
            f"Partial payment = {pct_paid}% of {_fmt_zar(open_bal)} = {_fmt_zar(part_pay)}\n"
            f"Remaining balance = {_fmt_zar(open_bal)} + {_fmt_zar(new_inv)} - {_fmt_zar(part_pay)} = {_fmt_zar(rem_bal)}"
        ),
        marking_points=[
            f"Compute partial payment: {pct_paid}% x {_fmt_zar(open_bal)} = {_fmt_zar(part_pay)} [1]",
            f"Compute closing balance = {_fmt_zar(open_bal)} + {_fmt_zar(new_inv)} - {_fmt_zar(part_pay)} = {_fmt_zar(rem_bal)} [2]",
        ],
        hints={
            "tier_1": f"First compute {pct_paid}% of the opening balance ({_fmt_zar(open_bal)}).",
            "tier_2": f"Next add new credit invoice ({_fmt_zar(new_inv)}) and subtract that partial payment.",
            "tier_3": f"Payment={_fmt_zar(part_pay)}; Remaining balance={_fmt_zar(rem_bal)}.",
        },
        learning_objective_id="lo_c2_partial_settlement_calc",
        concept_id="partial_creditor_settlement",
        misconception_tags=["takes_pct_of_opening_plus_new_invoice"],
        marks=3,
        correct_answer=_fmt_zar(rem_bal),
        correct_value=float(rem_bal),
        worked_solution=f"Part pay={part_pay}; Balance={open_bal} + {new_inv} - {part_pay} = {_fmt_zar(rem_bal)}",
    )


def arch_40_settling_previous_month_account_on_first_day(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    prev_bal = rng.choice([3450, 4280, 5600])
    new_apr_inv = rng.choice([1900, 2350, 2800])
    rem_after_1st = new_apr_inv
    prompt = (
        f"On 1 April, a business settles ONLY the previous month's March rendered account balance of {_fmt_zar(prev_bal)} "
        f"to {supplier}. On 12 April, the business purchases another {_fmt_zar(new_apr_inv)} of stock on credit.\n\n"
        f"What balance appears on {supplier}'s Creditors Ledger card immediately after 12 April?"
    )
    return _typed(
        rng,
        subskill="40_settling_previous_month_account_on_first_day",
        title="Settling Previous Month's Balance on the 1st",
        prompt=prompt,
        sample_answer=(
            f"On 1 April: Balance {_fmt_zar(prev_bal)} - Payment {_fmt_zar(prev_bal)} = R0.\n"
            f"On 12 April: R0 + CJ Invoice {_fmt_zar(new_apr_inv)} = {_fmt_zar(rem_after_1st)}."
        ),
        marking_points=[
            f"1 April payment clears the March rendered balance ({_fmt_zar(prev_bal)}) to R0 [1]",
            f"12 April credit invoice establishes new balance = {_fmt_zar(rem_after_1st)} [1]",
        ],
        hints={
            "tier_1": "Track the running balance sequentially: 1 April opening -> 1 April payment -> 12 April purchase.",
            "tier_2": "Paying the previous month's balance clears the card to R0 before 12 April.",
            "tier_3": f"R{_fmt_comma(0, 0)} + {_fmt_zar(new_apr_inv)} = {_fmt_zar(rem_after_1st)}." if False else f"After clearing {_fmt_zar(prev_bal)} to R0, 12 April leaves {_fmt_zar(rem_after_1st)}.",
        },
        learning_objective_id="lo_c2_settle_first_day",
        concept_id="settling_previous_month_on_1st",
        misconception_tags=["forgets_march_balance_cleared_to_zero"],
        marks=2,
        correct_answer=_fmt_zar(rem_after_1st),
        correct_value=float(rem_after_1st),
        worked_solution=f"({prev_bal} - {prev_bal}) + {new_apr_inv} = {_fmt_zar(rem_after_1st)}",
    )


def arch_41_creditors_control_journal_folios_verification(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"Inspecting a Creditors Control General Ledger account in {area}, a learner sees folio references `CJ`, `CPJ`, "
        f"`b/d`, and `c/d`.\n\n"
        f"Which statement ACCUARATELY identifies one of those folio abbreviations?"
        .replace("ACCUARATELY", "ACCURATELY")
    )
    correct = "`b/d` means 'brought down' (opening balance at the start of the month), while `c/d` means 'carried down' (closing balance)"
    distractors = [
        "`CJ` stands for Cash Journal of immediate till sales",
        "`CPJ` stands for Credit Purchases Journal for unpaid supplier invoices",
        "`b/d` means 'bank deposit' paid to retail customers",
    ]
    return _mcq(
        rng,
        subskill="41_creditors_control_journal_folios_verification",
        title="Accounting Folios in Creditors Ledger & Control",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Authentic accounting folios keep audit trails clear: b/d (brought down), c/d (carried down), CJ (Creditors "
            "Journal), CPJ (Cash Payments Journal), and CAJ (Creditors Allowance Journal)."
        ),
        hints={
            "tier_1": "Expand each abbreviation: b/d, c/d, CJ, CPJ.",
            "tier_2": "Remember CJ = Creditors Journal, CPJ = Cash Payments Journal.",
            "tier_3": "Select '`b/d` means 'brought down' (opening balance at the start of the month), while `c/d` means 'carried down' (closing balance)'.",
        },
        learning_objective_id="lo_c2_folio_meanings",
        concept_id="accounting_folios_creditors",
        misconception_tags=["confuses_cpj_with_credit_purchases"],
    )


def arch_42_distinguishing_debtors_vs_creditors_ledger_rules_table(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    headers = ["Ledger Comparison Dimension", "Debtors Ledger (Customers)", "Creditors Ledger (Suppliers)", "Check"]
    raw_rows = [
        [
            {"type": "given", "value": "Account Classification"},
            {"type": "given", "value": "Current Asset"},
            {"type": "required", "expected": "Current Liability"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Invoice Entry Side"},
            {"type": "required", "expected": "Debit (+)"},
            {"type": "given", "value": "Credit (+)"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Cash Settlement Side & Journal"},
            {"type": "given", "value": "Credit (-) via CRJ"},
            {"type": "required", "expected": "Debit (-) via CPJ"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c2": "Exact classification: 'Current Liability'.",
        "r1_c1": "Invoices sent to debtors increase Asset: 'Debit (+)'.",
        "r2_c2": "Payments to creditors decrease Liability: 'Debit (-) via CPJ'.",
    }
    derivations = [
        "Debtors = Current Asset (DJ Invoices -> Debit +, CRJ Receipts -> Credit -).",
        "Creditors = Current Liability (CJ Invoices -> Credit +, CPJ Cheques -> Debit -).",
    ]
    return _table_q(
        rng,
        subskill="42_distinguishing_debtors_vs_creditors_ledger_rules_table",
        title=f"Debtors Ledger vs Creditors Ledger Matrix ({trader})",
        prompt=(
            f"Contrast Debtors Ledger and Creditors Ledger posting rules for {trader} using these exact phrases: "
            f"'Current Liability', 'Debit (+)', and 'Debit (-) via CPJ'. Leave 'Check' blank."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Debtors are mirror images of Creditors because one is an Asset and the other is a Liability.",
            "tier_2": "Invoices in DJ Debit debtors (+), whereas invoices in CJ Credit creditors (+).",
            "tier_3": "r0_c2='Current Liability'; r1_c1='Debit (+)'; r2_c2='Debit (-) via CPJ'.",
        },
        learning_objective_id="lo_c2_dl_vs_cl_table",
        concept_id="debtors_vs_creditors_matrix",
        misconception_tags=["applies_debtors_signs_to_creditors", "fills_must_be_empty_cell"],
    )


def arch_43_missing_cj_total_from_control_account(rng: random.Random) -> Dict[str, Any]:
    open_bal = rng.choice([12500, 15800, 19400])
    cpj_pay = rng.choice([16200, 18500, 21000])
    close_bal = rng.choice([18900, 22400, 26100])
    missing_cj = close_bal + cpj_pay - open_bal

    prompt = (
        f"In a General Ledger **Creditors Control** account:\n"
        f"- Opening Balance b/d (1 March) = {_fmt_zar(open_bal)}\n"
        f"- Total Payments (`Bank CPJ`, 31 March) = {_fmt_zar(cpj_pay)}\n"
        f"- Closing Balance c/d (31 March) = {_fmt_zar(close_bal)}\n\n"
        f"Assuming zero returns, calculate the missing **Sundry purchases (CJ)** total for March."
    )
    return _typed(
        rng,
        subskill="43_missing_cj_total_from_control_account",
        title="Solving Missing CJ Credit Purchases in Creditors Control",
        prompt=prompt,
        sample_answer=(
            f"Debit total = Bank CPJ ({_fmt_zar(cpj_pay)}) + Closing Balance c/d ({_fmt_zar(close_bal)}) = {_fmt_zar(cpj_pay + close_bal)}\n"
            f"Since Credit total = Debit total, CJ Sundry purchases = {_fmt_zar(cpj_pay + close_bal)} - {_fmt_zar(open_bal)} = {_fmt_zar(missing_cj)}."
        ),
        marking_points=[
            f"Calculate Debit side total = {_fmt_zar(cpj_pay + close_bal)} [1]",
            f"Subtract Opening Balance b/d ({_fmt_zar(open_bal)}) = {_fmt_zar(missing_cj)} [2]",
        ],
        hints={
            "tier_1": "Notice that BOTH Debit items (`Bank CPJ` and `Balance c/d`) are given!",
            "tier_2": "Debit total equals Credit total (`Balance b/d + Sundry purchases CJ`).",
            "tier_3": f"({_fmt_zar(cpj_pay)} + {_fmt_zar(close_bal)}) - {_fmt_zar(open_bal)} = {_fmt_zar(missing_cj)}.",
        },
        learning_objective_id="lo_c2_missing_cj_calc",
        concept_id="missing_cj_purchases",
        misconception_tags=["subtracts_cpj_instead_of_adds"],
        marks=3,
        correct_answer=_fmt_zar(missing_cj),
        correct_value=float(missing_cj),
        worked_solution=f"CJ = ({cpj_pay} + {close_bal}) - {open_bal} = {_fmt_zar(missing_cj)}",
    )


def arch_44_missing_cpj_payments_from_control_account(rng: random.Random) -> Dict[str, Any]:
    open_bal = rng.choice([24000, 28000, 32000])
    cj_tot = rng.choice([31500, 36000, 42500])
    close_bal = rng.choice([21000, 25500, 29000])
    missing_cpj = open_bal + cj_tot - close_bal

    prompt = (
        f"In a business's General Ledger **Creditors Control** account:\n"
        f"- Opening Balance b/d = {_fmt_zar(open_bal)}\n"
        f"- Total Credit Purchases (`Sundry purchases CJ`) = {_fmt_zar(cj_tot)}\n"
        f"- Closing Balance c/d = {_fmt_zar(close_bal)}\n\n"
        f"Assuming no returns, calculate the missing total **Bank (CPJ)** payments made to creditors during the month."
    )
    return _typed(
        rng,
        subskill="44_missing_cpj_payments_from_control_account",
        title="Solving Missing CPJ Payments in Creditors Control",
        prompt=prompt,
        sample_answer=(
            f"Credit total = {_fmt_zar(open_bal)} + {_fmt_zar(cj_tot)} = {_fmt_zar(open_bal + cj_tot)}\n"
            f"Missing Bank CPJ payments = {_fmt_zar(open_bal + cj_tot)} - {_fmt_zar(close_bal)} = {_fmt_zar(missing_cpj)}."
        ),
        marking_points=[
            f"Sum Credit side ({_fmt_zar(open_bal)} + {_fmt_zar(cj_tot)}) = {_fmt_zar(open_bal + cj_tot)} [1]",
            f"Subtract Closing Balance c/d ({_fmt_zar(close_bal)}) = {_fmt_zar(missing_cpj)} [2]",
        ],
        hints={
            "tier_1": "Add Opening b/d and CJ Purchases to get the full Credit total.",
            "tier_2": "Subtract Closing Balance c/d from the Credit total to reveal Bank CPJ.",
            "tier_3": f"({_fmt_zar(open_bal)} + {_fmt_zar(cj_tot)}) - {_fmt_zar(close_bal)} = {_fmt_zar(missing_cpj)}.",
        },
        learning_objective_id="lo_c2_missing_cpj_calc",
        concept_id="missing_cpj_payments",
        misconception_tags=["adds_closing_balance_to_credit_total"],
        marks=3,
        correct_answer=_fmt_zar(missing_cpj),
        correct_value=float(missing_cpj),
        worked_solution=f"CPJ Bank = ({open_bal} + {cj_tot}) - {close_bal} = {_fmt_zar(missing_cpj)}",
    )


def arch_45_internal_control_preventing_duplicate_supplier_payments(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    inv_amt = rng.choice([4500, 6200, 8900])
    prompt = (
        f"A bookkeeper at {trader} nearly pays the same {_fmt_zar(inv_amt)} supplier invoice twice because a photocopy "
        f"of the invoice was left in the unpaid tray.\n\n"
        f"Recommend TWO strict internal-control procedures over source documents and ledgers to prevent duplicate creditor payments."
    )
    return _typed(
        rng,
        subskill="45_internal_control_preventing_duplicate_supplier_payments",
        title="Internal Controls Against Duplicate Supplier Payments",
        prompt=prompt,
        sample_answer=(
            f"1. Pay ONLY from verified Original Invoices linked to signed goods-received notes, never unverified copies, "
            f"and immediately stamp each paid invoice 'PAID' with the Cheque/EFT number and date.\n"
            f"2. Update the individual Creditors Ledger daily and reconcile the supplier's monthly statement before authorising any {_fmt_zar(inv_amt)} payment."
        ),
        marking_points=[
            "Cancelling/stamping original invoices 'PAID' with payment reference and goods-received verification [1]",
            "Checking updated Creditors Ledger running balance & monthly supplier statement plus dual-authorisation before paying [1]",
        ],
        hints={
            "tier_1": "Think about marking paid documents AND verifying the running ledger before signing cheques/EFTs.",
            "tier_2": "Original-invoice-only rule + 'PAID' stamp + ledger/statement check.",
            "tier_3": "Stamp original invoices PAID with cheque/EFT number, and verify Creditors Ledger/statement with dual sign-off.",
        },
        learning_objective_id="lo_c2_duplicate_payment_control",
        concept_id="internal_control_creditors",
        misconception_tags=["relies_only_on_memory_for_paid_invoices"],
        marks=2,
    )


def arch_46_supplier_credit_limit_monitoring_calculation(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    limit = rng.choice([15000, 20000, 25000])
    curr_bal = rng.choice([6800, 8400, 10200])
    new_order = rng.choice([4500, 5600, 6400])
    headroom = limit - (curr_bal + new_order)
    prompt = (
        f"{supplier} sets a maximum credit limit of {_fmt_zar(limit)} for our shop. Currently, {supplier}'s Creditors "
        f"Ledger shows a balance owed of {_fmt_zar(curr_bal)}. Before ordering {_fmt_zar(new_order)} more stock on credit, "
        f"calculate how much remaining available credit limit will remain AFTER that {_fmt_zar(new_order)} invoice."
    )
    return _typed(
        rng,
        subskill="46_supplier_credit_limit_monitoring_calculation",
        title="Monitoring Available Supplier Credit Limit",
        prompt=prompt,
        sample_answer=(
            f"Projected balance = {_fmt_zar(curr_bal)} + {_fmt_zar(new_order)} = {_fmt_zar(curr_bal + new_order)}\n"
            f"Remaining credit headroom = {_fmt_zar(limit)} - {_fmt_zar(curr_bal + new_order)} = {_fmt_zar(headroom)}"
        ),
        marking_points=[
            f"Compute projected balance = {_fmt_zar(curr_bal + new_order)} [1]",
            f"Subtract from credit limit ({_fmt_zar(limit)}) = {_fmt_zar(headroom)} [1]",
        ],
        hints={
            "tier_1": "First add the new order onto the current balance owed.",
            "tier_2": f"Subtract that new total from the {_fmt_zar(limit)} limit.",
            "tier_3": f"{_fmt_zar(limit)} - ({_fmt_zar(curr_bal)} + {_fmt_zar(new_order)}) = {_fmt_zar(headroom)}.",
        },
        learning_objective_id="lo_c2_credit_limit_check",
        concept_id="supplier_credit_limit",
        misconception_tags=["ignores_current_balance_when_checking_limit"],
        marks=2,
        correct_answer=_fmt_zar(headroom),
        correct_value=float(headroom),
        worked_solution=f"Remaining limit = {limit} - ({curr_bal} + {new_order}) = {_fmt_zar(headroom)}",
    )


def arch_47_creditors_age_analysis_bar_graph(rng: random.Random) -> Dict[str, Any]:
    curr = rng.choice([8500, 9600, 11200])
    d30 = rng.choice([4200, 5100, 6000])
    d60 = rng.choice([1800, 2400, 3000])
    d90 = rng.choice([900, 1200, 1500])
    overdue = d60 + d90

    svg = _svg_bar_chart(
        title="Creditors Age Analysis by Days Outstanding (R)",
        y_label="Amount Owed (R)",
        bars=[
            ("Current", float(curr), "#15803D"),
            ("30 Days", float(d30), "#0284C7"),
            ("60 Days", float(d60), "#D97706"),
            ("90+ Days", float(d90), "#DC2626"),
        ],
        max_val=float(curr + 2000),
        unit_suffix="",
    )
    prompt = (
        f"Refer to the bar graph below showing a business's Creditors Age Analysis: Current ({_fmt_zar(curr)}), "
        f"30 Days ({_fmt_zar(d30)}), 60 Days ({_fmt_zar(d60)}), and 90+ Days ({_fmt_zar(d90)}).\n\n"
        f"Assuming standard 30-day credit terms, calculate the TOTAL OVERDUE debt sitting at 60 Days and 90+ Days combined."
    )
    return _typed(
        rng,
        subskill="47_creditors_age_analysis_bar_graph",
        title="Creditors Age Analysis Overdue Debt (Bar Graph)",
        prompt=prompt,
        sample_answer=f"Total 60+ days overdue = {_fmt_zar(d60)} + {_fmt_zar(d90)} = {_fmt_zar(overdue)}.",
        marking_points=[
            f"Reads 60 Days ({_fmt_zar(d60)}) and 90+ Days ({_fmt_zar(d90)}) bars [1]",
            f"Sums overdue amounts = {_fmt_zar(overdue)} [2]",
        ],
        hints={
            "tier_1": "Add ONLY the orange (60 Days) and red (90+ Days) bars.",
            "tier_2": f"Calculate {_fmt_zar(d60)} + {_fmt_zar(d90)}.",
            "tier_3": f"{_fmt_zar(d60)} + {_fmt_zar(d90)} = {_fmt_zar(overdue)}.",
        },
        learning_objective_id="lo_c2_age_analysis_graph",
        concept_id="creditors_age_analysis",
        misconception_tags=["includes_current_or_30_day_balance_in_overdue"],
        marks=3,
        correct_answer=_fmt_zar(overdue),
        correct_value=float(overdue),
        diagram_spec={"kind": "inline_svg", "title": "Creditors Age Analysis", "svg": svg, "diagram_role": "context"},
        worked_solution=f"Overdue (60+ days) = {d60} + {d90} = {_fmt_zar(overdue)}",
    )


def arch_48_creditors_ledger_to_cpj_cash_flow_impact(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    stock_amt = rng.choice([12000, 16000, 20000])
    prompt = (
        f"{trader} purchases {_fmt_zar(stock_amt)} of fast-selling seasonal goods on 30-day credit rather than paying cash on delivery.\n\n"
        f"Explain ONE cash-flow benefit of using supplier credit responsibly AND ONE risk if {trader} repeatedly pays creditors late."
    )
    return _typed(
        rng,
        subskill="48_creditors_ledger_to_cpj_cash_flow_impact",
        title="Cash-Flow Benefits vs Late-Payment Risks of Credit",
        prompt=prompt,
        sample_answer=(
            f"Benefit: {trader} sells part of the {_fmt_zar(stock_amt)} stock for cash during the 30 days before the supplier "
            "cheque leaves Bank, easing short-term working-capital pressure.\n"
            "Risk of paying late: Overdue interest penalties, lost settlement discounts, damaged supplier trust, and frozen future stock deliveries."
        ),
        marking_points=[
            "Benefit: Preserves immediate Bank cash and allows selling stock before paying suppliers [1]",
            "Risk: Overdue interest fees, lost discounts, reputational damage, or halted stock supply [1]",
        ],
        hints={
            "tier_1": "Think about Bank cash timing during the 30 days, and what suppliers do when accounts go overdue.",
            "tier_2": "Give one working-capital advantage and one consequence of late CPJ settlements.",
            "tier_3": "Benefit: preserve Bank liquidity / sell stock before payment; Risk: interest penalties and halted credit deliveries.",
        },
        learning_objective_id="lo_c2_cash_flow_vs_late_risk",
        concept_id="creditor_cash_flow_management",
        misconception_tags=["treats_supplier_credit_as_free_nonrepayable_money"],
        marks=2,
    )


def arch_49_combined_cj_cpj_equation_multi_transaction_table(rng: random.Random) -> Dict[str, Any]:
    supplier = rng.choice(SUPPLIER_NAMES)
    inv_stock = rng.choice([3000, 4200, 5000])
    inv_pack = rng.choice([350, 450, 600])
    ret_amt = rng.choice([300, 400, 500])
    pay_amt = inv_stock + inv_pack - ret_amt

    headers = ["Credit Cycle Step", "Journal", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    raw_rows = [
        [
            {"type": "given", "value": f"1. Bought stock on credit ({_fmt_zar(inv_stock)})"},
            {"type": "given", "value": "CJ"},
            {"type": "required", "expected": f"+{inv_stock}"},
            {"type": "given", "value": "0"},
            {"type": "given", "value": f"+{inv_stock}"},
        ],
        [
            {"type": "given", "value": f"2. Bought packing material on credit ({_fmt_zar(inv_pack)})"},
            {"type": "given", "value": "CJ"},
            {"type": "given", "value": "0"},
            {"type": "required", "expected": f"-{inv_pack}"},
            {"type": "required", "expected": f"+{inv_pack}"},
        ],
        [
            {"type": "given", "value": f"3. Returned damaged stock ({_fmt_zar(ret_amt)})"},
            {"type": "given", "value": "CAJ"},
            {"type": "required", "expected": f"-{ret_amt}"},
            {"type": "given", "value": "0"},
            {"type": "required", "expected": f"-{ret_amt}"},
        ],
        [
            {"type": "given", "value": f"4. Settled {supplier} in full ({_fmt_zar(pay_amt)})"},
            {"type": "given", "value": "CPJ"},
            {"type": "required", "expected": f"-{pay_amt}"},
            {"type": "given", "value": "0"},
            {"type": "required", "expected": f"-{pay_amt}"},
        ],
    ]
    cell_hints = {
        "r0_c2": f"Trading stock increases Assets: '+{inv_stock}'.",
        "r1_c3": f"Packing material expense decreases Owner's Equity: '-{inv_pack}'.",
        "r1_c4": f"Creditors control increases Liabilities: '+{inv_pack}'.",
        "r2_c2": f"Returned Trading stock decreases Assets: '-{ret_amt}'.",
        "r2_c4": f"Debit Note reduces Liabilities: '-{ret_amt}'.",
        "r3_c2": f"Bank cash decreases Assets: '-{pay_amt}'.",
        "r3_c4": f"Creditors control decreases Liabilities to R0: '-{pay_amt}'.",
    }
    derivations = [
        f"1. CJ Stock: A=+{inv_stock}, OE=0, L=+{inv_stock}.",
        f"2. CJ Packing Material (expense): A=0, OE=-{inv_pack}, L=+{inv_pack}.",
        f"3. CAJ Stock Return: A=-{ret_amt}, OE=0, L=-{ret_amt}.",
        f"4. CPJ Settlement ({pay_amt}): A=-{pay_amt}, OE=0, L=-{pay_amt}.",
    ]
    return _table_q(
        rng,
        subskill="49_combined_cj_cpj_equation_multi_transaction_table",
        title="Full Creditor Cycle: Accounting Equation Table",
        prompt=(
            f"Trace all four transactions with {supplier} on the Accounting Equation (A = OE + L). "
            f"Enter exact signed figures (e.g. '+{inv_stock}' or '-{inv_pack}')."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Check each step independently: A = OE + L must always balance.",
            "tier_2": "Remember Packing material is an expense (OE -), whereas Trading stock is an Asset (A + / - on return).",
            "tier_3": f"Row 1: +{inv_stock}; Row 2: OE=-{inv_pack}, L=+{inv_pack}; Row 3: -{ret_amt}/-{ret_amt}; Row 4: -{pay_amt}/-{pay_amt}.",
        },
        learning_objective_id="lo_c2_full_cycle_eq_table",
        concept_id="combined_creditor_equation_table",
        misconception_tags=["treats_packing_material_as_zero_oe_effect"],
        journal_type="accounting_equation",
    )


def arch_50_integrated_creditors_cycle_mastery_synthesis(rng: random.Random) -> Dict[str, Any]:
    trader = rng.choice(TRADER_NAMES)
    supplier = rng.choice(SUPPLIER_NAMES)
    inv = rng.choice([5400, 7200, 8800])
    pay = rng.choice([3000, 4200, 5000])
    rem = inv - pay
    prompt = (
        f"{trader} receives an original invoice of {_fmt_zar(inv)} from {supplier} (C1) on 5 October and sends EFT "
        f"payment of {_fmt_zar(pay)} on 28 October.\n\n"
        f"Synthesise FOUR stages of the accounting cycle by explaining: (1) source documents & journals (CJ vs CPJ), "
        f"(2) how {supplier}'s 3-column Creditors Ledger updates to {_fmt_zar(rem)}, (3) month-end posting to General "
        f"Ledger Creditors Control, and (4) how the Creditors List proves accuracy."
    )
    return _typed(
        rng,
        subskill="50_integrated_creditors_cycle_mastery_synthesis",
        title="Integrated Creditors Cycle Mastery Synthesis",
        prompt=prompt,
        sample_answer=(
            f"1. Journals: Original invoice ({_fmt_zar(inv)}) enters CJ (`Creditors control` & `Trading stock`); EFT/cheque "
            f"counterfoil ({_fmt_zar(pay)}) enters CPJ (`Bank` & `Creditors control`).\n"
            f"2. Creditors Ledger (C1): Credit (+) {_fmt_zar(inv)} on 5 Oct -> balance {_fmt_zar(inv)}; Debit (-) {_fmt_zar(pay)} on 28 Oct -> closing balance {_fmt_zar(rem)}.\n"
            "3. General Ledger Creditors Control: Month-end Credit `Sundry purchases CJ` total, Debit `Bank CPJ` total, leaving Credit Balance c/d / next-month Balance b/d.\n"
            f"4. Reconciliation: Total of all individual Creditors Ledger cards (including C1's {_fmt_zar(rem)}) on the Creditors List must equal General Ledger Creditors Control."
        ),
        marking_points=[
            "Stage 1: Original invoice in CJ and cheque/EFT in CPJ [1]",
            f"Stage 2: Individual Creditors Ledger credits {_fmt_zar(inv)}, debits {_fmt_zar(pay)}, yielding {_fmt_zar(rem)} [1]",
            "Stage 3: General Ledger Creditors Control receives month-end CJ (Cr) and CPJ (Dr) column totals [1]",
            "Stage 4: Month-end Creditors List total equals Creditors Control Balance as internal proof [1]",
        ],
        hints={
            "tier_1": "Walk cleanly through all 4 checkpoints in chronological accounting order.",
            "tier_2": "Include exact source docs, Debit/Credit signs, daily C1 vs monthly GL Control, and Creditors List control proof.",
            "tier_3": f"Cover CJ/CPJ docs -> C1 Cr {_fmt_zar(inv)} / Dr {_fmt_zar(pay)} = {_fmt_zar(rem)} -> GL Control totals -> Creditors List match.",
        },
        learning_objective_id="lo_c2_integrated_synthesis",
        concept_id="integrated_creditors_cycle_synthesis",
        misconception_tags=["omits_control_reconciliation_step"],
        marks=4,
    )


BUILDERS_26_50 = {
    "26_general_ledger_creditors_control_t_account_structure": arch_26_general_ledger_creditors_control_t_account_structure,
    "27_calculating_closing_creditors_control_balance": arch_27_calculating_closing_creditors_control_balance,
    "28_general_ledger_creditors_control_2d_table": arch_28_general_ledger_creditors_control_2d_table,
    "29_balancing_creditors_control_next_month_bd": arch_29_balancing_creditors_control_next_month_bd,
    "30_creditors_list_purpose_internal_control": arch_30_creditors_list_purpose_internal_control,
    "31_compiling_creditors_list_2d_table": arch_31_compiling_creditors_list_2d_table,
    "32_reconciling_creditors_list_with_control_discrepancy": arch_32_reconciling_creditors_list_with_control_discrepancy,
    "33_multi_supplier_ledger_to_control_synthesis": arch_33_multi_supplier_ledger_to_control_synthesis,
    "34_creditors_payment_to_purchase_ratio_bar_graph": arch_34_creditors_payment_to_purchase_ratio_bar_graph,
    "35_creditors_statement_reconciliation_purpose": arch_35_creditors_statement_reconciliation_purpose,
    "36_statement_reconciliation_timing_differences": arch_36_statement_reconciliation_timing_differences,
    "37_invoice_vs_creditors_journal_sundry_allocation": arch_37_invoice_vs_creditors_journal_sundry_allocation,
    "38_debit_note_caj_effect_on_creditor_balance": arch_38_debit_note_caj_effect_on_creditor_balance,
    "39_partial_settlement_vs_full_settlement_calculation": arch_39_partial_settlement_vs_full_settlement_calculation,
    "40_settling_previous_month_account_on_first_day": arch_40_settling_previous_month_account_on_first_day,
    "41_creditors_control_journal_folios_verification": arch_41_creditors_control_journal_folios_verification,
    "42_distinguishing_debtors_vs_creditors_ledger_rules_table": arch_42_distinguishing_debtors_vs_creditors_ledger_rules_table,
    "43_missing_cj_total_from_control_account": arch_43_missing_cj_total_from_control_account,
    "44_missing_cpj_payments_from_control_account": arch_44_missing_cpj_payments_from_control_account,
    "45_internal_control_preventing_duplicate_supplier_payments": arch_45_internal_control_preventing_duplicate_supplier_payments,
    "46_supplier_credit_limit_monitoring_calculation": arch_46_supplier_credit_limit_monitoring_calculation,
    "47_creditors_age_analysis_bar_graph": arch_47_creditors_age_analysis_bar_graph,
    "48_creditors_ledger_to_cpj_cash_flow_impact": arch_48_creditors_ledger_to_cpj_cash_flow_impact,
    "49_combined_cj_cpj_equation_multi_transaction_table": arch_49_combined_cj_cpj_equation_multi_transaction_table,
    "50_integrated_creditors_cycle_mastery_synthesis": arch_50_integrated_creditors_cycle_mastery_synthesis,
}
