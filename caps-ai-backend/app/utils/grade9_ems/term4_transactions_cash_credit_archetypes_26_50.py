"""Grade 9 EMS — Transactions (Cash and Credit): Archetypes 26-50.
100% Aligned with South African National Curriculum Standards (Term 4: Financial Literacy).
Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 4/04. Transactions (Cash and Credit).md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .term4_transactions_cash_credit_archetypes_01_25 import (
    _BIZ_NAMES,
    _CREDITOR_NAMES,
    _DEBTOR_NAMES,
    _fmt_cell_amt,
    _fmt_zar,
    _mcq,
    _svg_bar_chart,
    _svg_cycle_flow,
    _table_q,
    _typed,
)


# ---------------------------------------------------------------------------
# Archetypes 26 - 38
# ---------------------------------------------------------------------------

def _b26_gl_bs_vs_nominal_classification_2d(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    headers = ["Account Name", "Trial Balance Section", "Normal Balance Side"]
    raw_rows = [
        [
            {"value": "Capital (B1)", "status": "given"},
            {"value": "Balance Sheet accounts", "status": "required"},
            {"value": "Credit", "status": "required"},
        ],
        [
            {"value": "Trading stock (B6)", "status": "given"},
            {"value": "Balance Sheet accounts", "status": "required"},
            {"value": "Debit", "status": "required"},
        ],
        [
            {"value": "Bank overdraft (B8)", "status": "given"},
            {"value": "Balance Sheet accounts", "status": "required"},
            {"value": "Credit", "status": "required"},
        ],
        [
            {"value": "Sales (N1)", "status": "given"},
            {"value": "Nominal accounts", "status": "required"},
            {"value": "Credit", "status": "required"},
        ],
        [
            {"value": "Cost of sales (N2)", "status": "given"},
            {"value": "Nominal accounts", "status": "required"},
            {"value": "Debit", "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Owner's Equity accounts (`B` folios) belong to `Balance Sheet accounts`.",
        "r0_c2": "Equity increases on the `Credit` side.",
        "r1_c1": "Assets (`B` folios) belong to `Balance Sheet accounts`.",
        "r1_c2": "Assets have a `Debit` balance.",
        "r2_c1": "Bank overdraft (`B` folio) is in `Balance Sheet accounts`.",
        "r2_c2": "An overdrawn bank balance is a Current Liability, so its balance is `Credit`.",
        "r3_c1": "Income accounts (`N` folios) belong to `Nominal accounts`.",
        "r3_c2": "Sales income increases Equity, so it has a `Credit` balance.",
        "r4_c1": "Expense accounts (`N` folios) belong to `Nominal accounts`.",
        "r4_c2": "Expenses reduce Equity, so they carry a `Debit` balance.",
    }
    derivations = [
        "Balance Sheet accounts (`B` folios): Assets (Dr), Owner's Equity/Capital (Cr; Drawings Dr), Liabilities/Overdraft (Cr).",
        "Nominal accounts (`N` folios): Income such as Sales & Rent income (Cr), Expenses such as Cost of sales & Stationery (Dr).",
    ]
    return _table_q(
        subskill="26_general_ledger_balance_sheet_vs_nominal_classification_2d_table",
        title=f"General Ledger Section & Normal Balance — {biz}",
        prompt=f"Classify each General Ledger account of {biz} into its Trial Balance section (`Balance Sheet accounts` or `Nominal accounts`) and its normal balance side (`Debit` or `Credit`).",
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Folio codes `B` belong to Balance Sheet accounts; `N` belong to Nominal accounts.",
            "Assets and Expenses have Debit balances; Liabilities, Capital, and Income have Credit balances.",
            "Remember Bank overdraft is a Credit liability.",
        ],
        learning_objective_id="EMS9-T4-TXN-26",
        concept_id="bs_vs_nominal_normal_balance",
        misconception_tags=["placed_bank_overdraft_on_debit_side", "placed_cost_of_sales_in_balance_sheet"],
    )


def _b27_gl_trading_stock_t_account_2d(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    bal_open = rng.randrange(8000, 22000, 1000)
    cpj_bank = rng.randrange(3000, 9000, 500)
    cj_cred = rng.randrange(4000, 11000, 500)
    cos_crj = rng.randrange(1500, 4500, 250)
    cos_dj = rng.randrange(2500, 6500, 250)
    tot_dr = bal_open + cpj_bank + cj_cred
    bal_close = tot_dr - cos_crj - cos_dj

    headers = ["Dr Details", "Dr Fol", "Dr Amount", "Cr Details", "Cr Fol", "Cr Amount"]
    raw_rows = [
        [
            {"value": "Balance b/d", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(bal_open), "status": "given"},
            {"value": "Cost of sales", "status": "required"},
            {"value": "CRJ", "status": "given"},
            {"value": _fmt_cell_amt(cos_crj), "status": "required"},
        ],
        [
            {"value": "Bank", "status": "required"},
            {"value": "CPJ", "status": "given"},
            {"value": _fmt_cell_amt(cpj_bank), "status": "required"},
            {"value": "Cost of sales", "status": "given"},
            {"value": "DJ", "status": "given"},
            {"value": _fmt_cell_amt(cos_dj), "status": "required"},
        ],
        [
            {"value": "Creditors control", "status": "required"},
            {"value": "CJ", "status": "given"},
            {"value": _fmt_cell_amt(cj_cred), "status": "required"},
            {"value": "Balance c/d", "status": "required"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(bal_close), "status": "required"},
        ],
        [
            {"value": "Total Dr", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(tot_dr), "status": "required"},
            {"value": "Total Cr", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(tot_dr), "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c3": "Contra account for CRJ stock sold is `Cost of sales`.",
        "r0_c5": f"Cash sales cost of sales = {_fmt_cell_amt(cos_crj)}.",
        "r1_c0": "Cash stock purchases come from `Bank` (CPJ).",
        "r1_c2": f"CPJ Trading stock = {_fmt_cell_amt(cpj_bank)}.",
        "r1_c5": f"DJ Cost of sales = {_fmt_cell_amt(cos_dj)}.",
        "r2_c0": "Credit stock purchases come from `Creditors control` (CJ).",
        "r2_c2": f"CJ Trading stock = {_fmt_cell_amt(cj_cred)}.",
        "r2_c3": "Closing balance label before month-end total: `Balance c/d`.",
        "r2_c5": f"Closing stock = {_fmt_cell_amt(tot_dr)} - ({_fmt_cell_amt(cos_crj)} + {_fmt_cell_amt(cos_dj)}) = {_fmt_cell_amt(bal_close)}.",
        "r3_c2": f"Sum Dr side = {_fmt_cell_amt(tot_dr)}.",
        "r3_c5": f"Cr total must match Dr total = {_fmt_cell_amt(tot_dr)}.",
    }
    derivations = [
        f"Dr side increases Trading Stock: Opening {_fmt_zar(bal_open)} + Bank CPJ {_fmt_zar(cpj_bank)} + Creditors control CJ {_fmt_zar(cj_cred)} = {_fmt_zar(tot_dr)}.",
        f"Cr side records stock sold at cost price: Cost of sales CRJ ({_fmt_zar(cos_crj)}) + Cost of sales DJ ({_fmt_zar(cos_dj)}) = {_fmt_zar(cos_crj + cos_dj)}.",
        f"Balance c/d = {_fmt_zar(tot_dr)} - {_fmt_zar(cos_crj + cos_dj)} = {_fmt_zar(bal_close)} (brought down Dr on 1st of next month).",
    ]
    return _table_q(
        subskill="27_general_ledger_trading_stock_t_account_2d_table",
        title=f"General Ledger: Trading Stock (B6) — {biz}",
        prompt=(
            f"Complete and balance the Trading Stock (B6) General Ledger account of {biz} for May:\n"
            f"- Opening balance (1 May): {_fmt_zar(bal_open)}\n"
            f"- Cash stock purchases (CPJ): {_fmt_zar(cpj_bank)}\n"
            f"- Credit stock purchases (CJ): {_fmt_zar(cj_cred)}\n"
            f"- Cost of cash sales (CRJ): {_fmt_zar(cos_crj)}; Cost of credit sales (DJ): {_fmt_zar(cos_dj)}"
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Trading Stock is an Asset (+ on Debit for purchases, - on Credit for Cost of sales).",
            "Always use Cost of sales figures—never Selling price—on the Credit side.",
            f"Total Dr = {_fmt_cell_amt(tot_dr)}; Closing Balance c/d = {_fmt_cell_amt(bal_close)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-27",
        concept_id="trading_stock_general_ledger_balancing",
        misconception_tags=["credited_sales_selling_price_to_trading_stock", "put_purchases_on_credit_side"],
        journal_type="general_ledger",
        duration_mins=8,
    )


def _b28_gl_debtors_control_t_account_2d(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    bal_open = rng.randrange(2000, 8000, 500)
    dj_sales = rng.randrange(4000, 12000, 500)
    crj_bank = rng.randrange(3000, 7500, 250)
    tot_dr = bal_open + dj_sales
    bal_close = tot_dr - crj_bank

    headers = ["Dr Details", "Dr Fol", "Dr Amount", "Cr Details", "Cr Fol", "Cr Amount"]
    raw_rows = [
        [
            {"value": "Balance b/d", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(bal_open), "status": "given"},
            {"value": "Bank", "status": "required"},
            {"value": "CRJ", "status": "given"},
            {"value": _fmt_cell_amt(crj_bank), "status": "required"},
        ],
        [
            {"value": "Sales", "status": "required"},
            {"value": "DJ", "status": "given"},
            {"value": _fmt_cell_amt(dj_sales), "status": "required"},
            {"value": "Balance c/d", "status": "required"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(bal_close), "status": "required"},
        ],
        [
            {"value": "Total Dr", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(tot_dr), "status": "required"},
            {"value": "Total Cr", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(tot_dr), "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c3": "Receipts from debtors come from `Bank` (CRJ).",
        "r0_c5": f"Debtors control collected in CRJ = {_fmt_cell_amt(crj_bank)}.",
        "r1_c0": "Credit sales contra account in DJ is `Sales`.",
        "r1_c2": f"DJ Sales total = {_fmt_cell_amt(dj_sales)}.",
        "r1_c3": "Enter `Balance c/d`.",
        "r1_c5": f"Closing balance = {_fmt_cell_amt(tot_dr)} - {_fmt_cell_amt(crj_bank)} = {_fmt_cell_amt(bal_close)}.",
        "r2_c2": f"Dr total = {_fmt_cell_amt(tot_dr)}.",
        "r2_c5": f"Cr total = {_fmt_cell_amt(tot_dr)}.",
    }
    derivations = [
        f"Debtors Control (Asset) increases Dr: Opening {_fmt_zar(bal_open)} + Credit Sales (DJ) {_fmt_zar(dj_sales)} = {_fmt_zar(tot_dr)}.",
        f"Receipts from debtors (CRJ Bank) {_fmt_zar(crj_bank)} reduce Debtors Control on the Cr side.",
        f"Balance c/d = {_fmt_zar(bal_close)} (brought down Dr next month).",
    ]
    return _table_q(
        subskill="28_general_ledger_debtors_control_t_account_2d_table",
        title=f"General Ledger: Debtors Control (B7) — {biz}",
        prompt=(
            f"Complete and balance Debtors Control (B7) of {biz}:\n"
            f"- Opening balance b/d: {_fmt_zar(bal_open)}\n"
            f"- Total Credit Sales (DJ): {_fmt_zar(dj_sales)}\n"
            f"- Cash received from debtors (CRJ): {_fmt_zar(crj_bank)}"
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Debtors Control is a Current Asset (+ Debit from DJ Sales, - Credit from CRJ Bank).",
            "Do NOT include Cash Sales from CRJ or Cost of Sales in Debtors Control.",
            f"Closing Balance c/d = {_fmt_cell_amt(bal_close)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-28",
        concept_id="debtors_control_general_ledger",
        misconception_tags=["included_cash_sales_in_debtors_control", "reversed_dr_cr_sides"],
        journal_type="general_ledger",
        duration_mins=7,
    )


def _b29_gl_creditors_control_t_account_2d(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    bal_open = rng.randrange(4000, 12000, 500)
    cj_tot = rng.randrange(8000, 22000, 500)
    cpj_pay = rng.randrange(3000, 9500, 250)
    tot_cr = bal_open + cj_tot
    bal_close = tot_cr - cpj_pay

    headers = ["Dr Details", "Dr Fol", "Dr Amount", "Cr Details", "Cr Fol", "Cr Amount"]
    raw_rows = [
        [
            {"value": "Bank", "status": "required"},
            {"value": "CPJ", "status": "given"},
            {"value": _fmt_cell_amt(cpj_pay), "status": "required"},
            {"value": "Balance b/d", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(bal_open), "status": "given"},
        ],
        [
            {"value": "Balance c/d", "status": "required"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(bal_close), "status": "required"},
            {"value": "Sundry purchases", "status": "required"},
            {"value": "CJ", "status": "given"},
            {"value": _fmt_cell_amt(cj_tot), "status": "required"},
        ],
        [
            {"value": "Total Dr", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(tot_cr), "status": "required"},
            {"value": "Total Cr", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(tot_cr), "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c0": "Payments to creditors reduce liability on Dr side: `Bank` (CPJ).",
        "r0_c2": f"CPJ Creditors control paid = {_fmt_cell_amt(cpj_pay)}.",
        "r1_c0": "Closing balance on Dr side before balancing off: `Balance c/d`.",
        "r1_c2": f"Closing liability = {_fmt_cell_amt(tot_cr)} - {_fmt_cell_amt(cpj_pay)} = {_fmt_cell_amt(bal_close)}.",
        "r1_c3": "Total credit purchases (stock + stationery + equipment) use `Sundry purchases` (CJ).",
        "r1_c5": f"CJ Creditors control column total = {_fmt_cell_amt(cj_tot)}.",
        "r2_c2": f"Total Dr = {_fmt_cell_amt(tot_cr)}.",
        "r2_c5": f"Total Cr = {_fmt_cell_amt(tot_cr)}.",
    }
    derivations = [
        f"Creditors Control (Liability) increases Cr: Opening {_fmt_zar(bal_open)} + Sundry purchases CJ {_fmt_zar(cj_tot)} = {_fmt_zar(tot_cr)}.",
        f"Payments to creditors (CPJ Bank {_fmt_zar(cpj_pay)}) reduce the liability on the Dr side.",
        f"Balance c/d = {_fmt_zar(bal_close)} (brought down Cr next month).",
    ]
    return _table_q(
        subskill="29_general_ledger_creditors_control_t_account_2d_table",
        title=f"General Ledger: Creditors Control (B8) — {biz}",
        prompt=(
            f"Complete and balance Creditors Control (B8) of {biz}:\n"
            f"- Opening balance b/d (Cr): {_fmt_zar(bal_open)}\n"
            f"- Total credit purchases (CJ Sundry purchases): {_fmt_zar(cj_tot)}\n"
            f"- Payments to creditors (CPJ): {_fmt_zar(cpj_pay)}"
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Creditors Control is a Liability (+ Credit from CJ Sundry purchases, - Debit from CPJ Bank).",
            "Closing Balance c/d sits on the Dr side so totals balance, then opens Cr next month.",
            f"Closing Balance c/d = {_fmt_cell_amt(bal_close)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-29",
        concept_id="creditors_control_general_ledger",
        misconception_tags=["placed_opening_balance_on_debit_side", "wrote_trading_stock_instead_of_sundry_purchases"],
        journal_type="general_ledger",
        duration_mins=7,
    )


def _b30_gl_bank_overdraft_2d(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(["Nani Traders", "Valley Traders", "Viwe Enterprises", "Slamet Stores"])
    open_dr = rng.randrange(3000, 8000, 500)
    crj_tot = rng.randrange(4000, 9500, 500)
    extra_od = rng.randrange(2500, 7500, 500)
    cpj_tot = open_dr + crj_tot + extra_od  # forces overdraft

    headers = ["Dr Details", "Dr Fol", "Dr Amount", "Cr Details", "Cr Fol", "Cr Amount"]
    raw_rows = [
        [
            {"value": "Balance b/d", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(open_dr), "status": "given"},
            {"value": "Total payments", "status": "required"},
            {"value": "CPJ", "status": "given"},
            {"value": _fmt_cell_amt(cpj_tot), "status": "required"},
        ],
        [
            {"value": "Total receipts", "status": "required"},
            {"value": "CRJ", "status": "given"},
            {"value": _fmt_cell_amt(crj_tot), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
        ],
        [
            {"value": "Balance c/d", "status": "required"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(extra_od), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
        ],
        [
            {"value": "Total Dr", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(cpj_tot), "status": "required"},
            {"value": "Total Cr", "status": "given"},
            {"value": "", "status": "given"},
            {"value": _fmt_cell_amt(cpj_tot), "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c3": "CPJ Bank column total posts on Cr side as `Total payments`.",
        "r0_c5": f"Total payments = {_fmt_cell_amt(cpj_tot)}.",
        "r1_c0": "CRJ Bank column total posts on Dr side as `Total receipts`.",
        "r1_c2": f"Total receipts = {_fmt_cell_amt(crj_tot)}.",
        "r2_c0": "Because Cr exceeds Dr, `Balance c/d` goes on the smaller Dr side.",
        "r2_c2": f"Overdraft c/d = {_fmt_cell_amt(cpj_tot)} - ({_fmt_cell_amt(open_dr)} + {_fmt_cell_amt(crj_tot)}) = {_fmt_cell_amt(extra_od)}.",
        "r3_c2": f"Larger side total = {_fmt_cell_amt(cpj_tot)}.",
        "r3_c5": f"Cr total = {_fmt_cell_amt(cpj_tot)}.",
    }
    derivations = [
        f"Available Bank funds on Dr side = {_fmt_zar(open_dr)} (b/d) + {_fmt_zar(crj_tot)} (Total receipts) = {_fmt_zar(open_dr + crj_tot)}.",
        f"Total payments (CPJ) on Cr side = {_fmt_zar(cpj_tot)}, exceeding available funds by {_fmt_zar(extra_od)}.",
        f"Insert Balance c/d = {_fmt_zar(extra_od)} on the Dr side to balance both totals to {_fmt_zar(cpj_tot)}; next month opens Cr {_fmt_zar(extra_od)} (Bank Overdraft).",
    ]
    return _table_q(
        subskill="30_general_ledger_bank_account_favourable_to_overdraft_2d_table",
        title=f"General Ledger: Bank Account Entering Overdraft — {biz}",
        prompt=(
            f"Complete and balance the Bank account of {biz} given:\n"
            f"- Opening favourable balance b/d (Dr): {_fmt_zar(open_dr)}\n"
            f"- Total receipts for the month (CRJ): {_fmt_zar(crj_tot)}\n"
            f"- Total payments for the month (CPJ): {_fmt_zar(cpj_tot)}\n"
            "Leave unused Cr lines blank."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Compare Dr total (`b/d + CRJ`) with Cr (`CPJ`). Whichever side is larger sets the balancing total.",
            "Since payments exceed receipts + opening balance, Balance c/d sits on the Dr side (creating a Cr overdraft b/d next month).",
            f"Overdraft c/d = {_fmt_cell_amt(extra_od)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-30",
        concept_id="bank_overdraft_general_ledger_balancing",
        misconception_tags=["forced_balance_cd_onto_credit_side_even_in_overdraft"],
        journal_type="general_ledger",
        duration_mins=8,
    )


def _b31_posting_crj_dj_to_sales_and_cos_mcq(rng: random.Random) -> Dict[str, Any]:
    cash_s = rng.randrange(4000, 12000, 500)
    cred_s = rng.randrange(6000, 18000, 500)
    return _mcq(
        rng,
        subskill="31_posting_crj_dj_to_sales_and_cost_of_sales_ledger_mcq",
        prompt=f"In the General Ledger, Cash Sales from the CRJ ({_fmt_zar(cash_s)}) and Credit Sales from the DJ ({_fmt_zar(cred_s)}) are posted to `Sales (N1)`. What details and side are entered in `Sales (N1)`?",
        correct=f"Credit side: `Bank CRJ` ({_fmt_zar(cash_s)}) and `Debtors control DJ` ({_fmt_zar(cred_s)}).",
        distractors=[
            f"Debit side: `Bank CRJ` ({_fmt_zar(cash_s)}) and `Debtors control DJ` ({_fmt_zar(cred_s)}).",
            f"Credit side: `Trading stock CRJ` ({_fmt_zar(cash_s)}) and `Cost of sales DJ` ({_fmt_zar(cred_s)}).",
            f"Only `Debtors control DJ` ({_fmt_zar(cred_s)}) enters Sales; Cash sales remain inside Bank.",
        ],
        learning_objective_id="EMS9-T4-TXN-31",
        concept_id="sales_nominal_ledger_posting_details",
        misconception_tags=["wrote_cash_sales_instead_of_bank_in_sales_ledger"],
        hints=[
            "Sales is an Income account, so increases are posted on the Credit side.",
            "Remember ledger rule: write the name of the CONTRA account debited (`Bank` for CRJ, `Debtors control` for DJ).",
            f"Credit `Sales` with `Bank CRJ` ({_fmt_zar(cash_s)}) and `Debtors control DJ` ({_fmt_zar(cred_s)}).",
        ],
        worked_solution=f"`Sales (N1)` is credited at month-end with `Bank CRJ` ({_fmt_zar(cash_s)}) and `Debtors control DJ` ({_fmt_zar(cred_s)}).",
    )


def _b32_nominal_expense_cpj_and_cj_combined_calc(rng: random.Random) -> Dict[str, Any]:
    acct = rng.choice(["Stationery (N3)", "Consumable goods (N6)", "Packing material (N5)"])
    open_bal = rng.randrange(400, 1800, 100)
    cpj_cash = rng.randrange(300, 1200, 50)
    cj_cred = rng.randrange(450, 1500, 50)
    closing = open_bal + cpj_cash + cj_cred
    sol = f"Closing balance of {acct} = {_fmt_zar(open_bal)} (b/d) + {_fmt_zar(cpj_cash)} (Bank CPJ) + {_fmt_zar(cj_cred)} (Creditors control CJ) = {_fmt_zar(closing)}."
    return _typed(
        subskill="32_nominal_expense_account_cpj_and_cj_combined_posting_typed",
        prompt=(
            f"On 1 March, `{acct}` has a Debit balance b/d of {_fmt_zar(open_bal)}. "
            f"During March, cash purchases in the CPJ total {_fmt_zar(cpj_cash)} and credit purchases in the CJ total {_fmt_zar(cj_cred)}. "
            f"Calculate the closing total of `{acct}` on 31 March."
        ),
        correct_answer=_fmt_zar(closing),
        accepted_answers=[str(closing), _fmt_zar(closing), _fmt_cell_amt(closing), f"R{closing}"],
        learning_objective_id="EMS9-T4-TXN-32",
        concept_id="nominal_expense_accumulation_cpj_cj",
        misconception_tags=["excluded_credit_purchases_from_nominal_expense"],
        hints=[
            "Nominal expense accounts accumulate both cash (Bank CPJ) and credit (Creditors control CJ) debits.",
            f"Add all three Dr entries: {_fmt_zar(open_bal)} + {_fmt_zar(cpj_cash)} + {_fmt_zar(cj_cred)}.",
            sol,
        ],
        worked_solution=sol,
    )


def _b33_debtors_ledger_3col_2d(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    debtor = rng.choice(_DEBTOR_NAMES)
    open_bal = rng.randrange(800, 2400, 100)
    inv_amt = rng.randrange(1100, 3200, 100)
    rec_amt = rng.randrange(500, 1500, 100)
    b1 = open_bal + inv_amt
    b2 = b1 - rec_amt

    headers = ["Date", "Details / Doc no.", "Fol.", "Debit (+)", "Credit (-)", "Balance"]
    raw_rows = [
        [
            {"value": "May 01", "status": "given"},
            {"value": "Account rendered", "status": "given"},
            {"value": "", "status": "given"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(open_bal), "status": "given"},
        ],
        [
            {"value": "11", "status": "given"},
            {"value": "Invoice no. 322", "status": "given"},
            {"value": "DJ5", "status": "required"},
            {"value": _fmt_cell_amt(inv_amt), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(b1), "status": "required"},
        ],
        [
            {"value": "20", "status": "given"},
            {"value": "Receipt no. 88", "status": "given"},
            {"value": "CRJ5", "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(rec_amt), "status": "required"},
            {"value": _fmt_cell_amt(b2), "status": "required"},
        ],
    ]
    cell_hints = {
        "r1_c2": "Credit invoices to debtors come from `DJ5`.",
        "r1_c3": f"Credit sale increases what the debtor owes: Debit (+) {_fmt_cell_amt(inv_amt)}.",
        "r1_c5": f"Running balance = {_fmt_cell_amt(open_bal)} + {_fmt_cell_amt(inv_amt)} = {_fmt_cell_amt(b1)}.",
        "r2_c2": "Cash receipts from debtors come from `CRJ5`.",
        "r2_c4": f"Payment reduces what the debtor owes: Credit (-) {_fmt_cell_amt(rec_amt)}.",
        "r2_c5": f"Running balance = {_fmt_cell_amt(b1)} - {_fmt_cell_amt(rec_amt)} = {_fmt_cell_amt(b2)}.",
    }
    derivations = [
        f"Opening balance: {_fmt_zar(open_bal)}.",
        f"May 11 Inv 322 (DJ5): +{_fmt_zar(inv_amt)} on Debit (+) -> Balance = {_fmt_zar(b1)}.",
        f"May 20 Receipt 88 (CRJ5): -{_fmt_zar(rec_amt)} on Credit (-) -> Final Balance = {_fmt_zar(b2)}.",
    ]
    return _table_q(
        subskill="33_debtors_ledger_three_column_dr_plus_cr_minus_2d_table",
        title=f"Debtors Ledger: {debtor} (D1) — {biz}",
        prompt=(
            f"Complete the 3-column Debtors Ledger account for {debtor} (D1) at {biz}:\n"
            f"- May 01: Account rendered balance {_fmt_zar(open_bal)}\n"
            f"- May 11: Credit sale on Invoice 322 (DJ5) for {_fmt_zar(inv_amt)}\n"
            f"- May 20: Receipt 88 (CRJ5) received on account for {_fmt_zar(rec_amt)}"
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Debtors Ledger uses Debit (+) for sales invoices and Credit (-) for receipts/returns (the exact opposite of Creditors Ledger).",
            f"Add {_fmt_cell_amt(inv_amt)} on May 11, then subtract {_fmt_cell_amt(rec_amt)} on May 20.",
            f"Closing balance = {_fmt_cell_amt(b2)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-33",
        concept_id="three_column_debtors_ledger",
        misconception_tags=["applied_creditor_signs_to_debtors_ledger"],
        journal_type="debtors_ledger",
        duration_mins=7,
    )


def _b34_creditors_ledger_3col_2d(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    cred = rng.choice(_CREDITOR_NAMES)
    open_bal = rng.randrange(1200, 4200, 100)
    inv_amt = rng.randrange(1500, 3800, 100)
    pay_amt = rng.randrange(1000, 2400, 100)
    dn_amt = rng.randrange(200, 600, 50)
    b1 = open_bal + inv_amt
    b2 = b1 - pay_amt
    b3 = b2 - dn_amt

    headers = ["Date", "Details / Doc no.", "Fol.", "Debit (-)", "Credit (+)", "Balance"]
    raw_rows = [
        [
            {"value": "Mar 01", "status": "given"},
            {"value": "Account rendered", "status": "given"},
            {"value": "", "status": "given"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(open_bal), "status": "given"},
        ],
        [
            {"value": "06", "status": "given"},
            {"value": "Invoice no. 304", "status": "given"},
            {"value": "CJ3", "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(inv_amt), "status": "required"},
            {"value": _fmt_cell_amt(b1), "status": "required"},
        ],
        [
            {"value": "18", "status": "given"},
            {"value": "EFT / Cheque 188", "status": "given"},
            {"value": "CPJ3", "status": "required"},
            {"value": _fmt_cell_amt(pay_amt), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(b2), "status": "required"},
        ],
        [
            {"value": "24", "status": "given"},
            {"value": "Debit note 41", "status": "given"},
            {"value": "CAJ3", "status": "required"},
            {"value": _fmt_cell_amt(dn_amt), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(b3), "status": "required"},
        ],
    ]
    cell_hints = {
        "r1_c2": "Supplier invoices post from `CJ3`.",
        "r1_c4": f"Credit purchase increases liability: Credit (+) {_fmt_cell_amt(inv_amt)}.",
        "r1_c5": f"Balance = {_fmt_cell_amt(open_bal)} + {_fmt_cell_amt(inv_amt)} = {_fmt_cell_amt(b1)}.",
        "r2_c2": "Payments post from `CPJ3`.",
        "r2_c3": f"Payment reduces what we owe: Debit (-) {_fmt_cell_amt(pay_amt)}.",
        "r2_c5": f"Balance = {_fmt_cell_amt(b1)} - {_fmt_cell_amt(pay_amt)} = {_fmt_cell_amt(b2)}.",
        "r3_c2": "Returns via debit note post from `CAJ3`.",
        "r3_c3": f"Goods returned reduce creditor balance: Debit (-) {_fmt_cell_amt(dn_amt)}.",
        "r3_c5": f"Closing balance = {_fmt_cell_amt(b2)} - {_fmt_cell_amt(dn_amt)} = {_fmt_cell_amt(b3)}.",
    }
    derivations = [
        f"Mar 01 Opening: {_fmt_zar(open_bal)}.",
        f"Mar 06 Inv 304 (CJ3): Credit (+) {_fmt_zar(inv_amt)} -> {_fmt_zar(b1)}.",
        f"Mar 18 Cheque 188 (CPJ3): Debit (-) {_fmt_zar(pay_amt)} -> {_fmt_zar(b2)}.",
        f"Mar 24 Debit note 41 (CAJ3): Debit (-) {_fmt_zar(dn_amt)} -> {_fmt_zar(b3)}.",
    ]
    return _table_q(
        subskill="34_creditors_ledger_three_column_cr_plus_dr_minus_2d_table",
        title=f"Creditors Ledger: {cred} (C1) — {biz}",
        prompt=(
            f"Complete the 3-column Creditors Ledger for {cred} (C1) at {biz}:\n"
            f"- Mar 01: Account rendered {_fmt_zar(open_bal)}\n"
            f"- Mar 06: Original Invoice 304 (CJ3) for {_fmt_zar(inv_amt)}\n"
            f"- Mar 18: EFT / Cheque 188 (CPJ3) paid {_fmt_zar(pay_amt)}\n"
            f"- Mar 24: Debit note 41 (CAJ3) for stock returned {_fmt_zar(dn_amt)}"
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Creditors Ledger uses Credit (+) for invoices and Debit (-) for payments and returns.",
            "Do not forget to subtract the Debit note from CAJ3 on the Debit (-) side.",
            f"Final closing balance = {_fmt_cell_amt(b3)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-34",
        concept_id="three_column_creditors_ledger_integrated",
        misconception_tags=["added_debit_note_instead_of_subtracting"],
        journal_type="creditors_ledger",
        duration_mins=8,
    )


def _b35_debtors_schedule_reconciliation_2d(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    d1, d2, d3, d4 = rng.sample(_DEBTOR_NAMES, 4)
    v1 = rng.randrange(900, 2900, 50)
    v2 = 0
    v3 = rng.randrange(1200, 3800, 50)
    v4 = rng.randrange(600, 1900, 50)
    tot = v1 + v2 + v3 + v4

    headers = ["Debtor", "Folio", "Closing Balance"]
    raw_rows = [
        [{"value": d1, "status": "given"}, {"value": "D1", "status": "given"}, {"value": _fmt_cell_amt(v1), "status": "required"}],
        [{"value": d2, "status": "given"}, {"value": "D2", "status": "given"}, {"value": _fmt_cell_amt(v2), "status": "required"}],
        [{"value": d3, "status": "given"}, {"value": "D3", "status": "given"}, {"value": _fmt_cell_amt(v3), "status": "required"}],
        [{"value": d4, "status": "given"}, {"value": "D4", "status": "given"}, {"value": _fmt_cell_amt(v4), "status": "required"}],
        [{"value": "Debtors control", "status": "required"}, {"value": "B7", "status": "given"}, {"value": _fmt_cell_amt(tot), "status": "required"}],
    ]
    cell_hints = {
        "r0_c2": f"{d1} closing balance = {_fmt_cell_amt(v1)}.",
        "r1_c2": f"{d2} settled in full -> 0.00.",
        "r2_c2": f"{d3} closing balance = {_fmt_cell_amt(v3)}.",
        "r3_c2": f"{d4} closing balance = {_fmt_cell_amt(v4)}.",
        "r4_c0": "Schedule total reconciles to `Debtors control`.",
        "r4_c2": f"Sum = {_fmt_cell_amt(v1)} + 0.00 + {_fmt_cell_amt(v3)} + {_fmt_cell_amt(v4)} = {_fmt_cell_amt(tot)}.",
    }
    derivations = [
        f"{d1} (D1): {_fmt_zar(v1)}; {d2} (D2): R 0,00; {d3} (D3): {_fmt_zar(v3)}; {d4} (D4): {_fmt_zar(v4)}.",
        f"List total = {_fmt_zar(tot)}, reconciling directly with General Ledger `Debtors control (B7)`.",
    ]
    return _table_q(
        subskill="35_debtors_schedule_reconciliation_with_control_2d_table",
        title=f"Debtors Schedule (List of Balances) — {biz}",
        prompt=(
            f"Compile the List (Schedule) of Balances of Debtors on 31 March for {biz}:\n"
            f"- {d1} (D1): owes {_fmt_zar(v1)}\n"
            f"- {d2} (D2): account settled in full (zero balance)\n"
            f"- {d3} (D3): owes {_fmt_zar(v3)}\n"
            f"- {d4} (D4): owes {_fmt_zar(v4)}"
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Even a debtor with a R 0,00 balance is listed on the Debtors Schedule to confirm all accounts were checked.",
            "The bottom control row must label `Debtors control` and sum all four balances.",
            f"Total Debtors control = {_fmt_cell_amt(tot)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-35",
        concept_id="debtors_schedule_reconciliation",
        misconception_tags=["omitted_zero_balance_debtor"],
        journal_type="debtors_schedule",
        duration_mins=6,
    )


def _b36_creditors_schedule_missing_account_deduction(rng: random.Random) -> Dict[str, Any]:
    ctrl_open = rng.randrange(4000, 9500, 100)
    c2_open = rng.randrange(1200, 3200, 50)
    c3_open = rng.randrange(1000, 2800, 50)
    c1_open = ctrl_open - c2_open - c3_open
    inv1 = rng.randrange(400, 1200, 50)
    inv2 = rng.randrange(500, 1400, 50)
    pay1 = rng.randrange(300, 800, 50)
    c1_close = c1_open + inv1 + inv2 - pay1
    sol = (
        f"1. Missing opening balance of D1 (`Account rendered`) = {_fmt_zar(ctrl_open)} - {_fmt_zar(c2_open)} - {_fmt_zar(c3_open)} = {_fmt_zar(c1_open)}.\n"
        f"2. Add credit invoices ({_fmt_zar(inv1)} + {_fmt_zar(inv2)}) and subtract payment ({_fmt_zar(pay1)}):\n"
        f"   Closing balance = {_fmt_zar(c1_open)} + {_fmt_zar(inv1 + inv2)} - {_fmt_zar(pay1)} = {_fmt_zar(c1_close)}."
    )
    return _typed(
        subskill="36_creditors_schedule_and_missing_account_deduction",
        prompt=(
            f"General Ledger `Debtors Control` had an opening balance on 1 June of {_fmt_zar(ctrl_open)} across 3 debtors.\n"
            f"D2 owed {_fmt_zar(c2_open)} and D3 owed {_fmt_zar(c3_open)} on 1 June.\n"
            f"During June, debtor D1 bought goods on credit for {_fmt_zar(inv1)} and {_fmt_zar(inv2)}, and paid {_fmt_zar(pay1)} on account.\n"
            "Calculate D1's closing balance on 30 June."
        ),
        correct_answer=_fmt_zar(c1_close),
        accepted_answers=[str(c1_close), _fmt_zar(c1_close), _fmt_cell_amt(c1_close), f"R{c1_close}"],
        learning_objective_id="EMS9-T4-TXN-36",
        concept_id="deduce_missing_opening_subledger_balance",
        misconception_tags=["forgot_to_find_opening_balance_first"],
        hints=[
            "The sum of all opening sub-ledger balances must equal the opening Control account balance.",
            f"First find D1 opening balance = {_fmt_zar(ctrl_open)} - ({_fmt_zar(c2_open)} + {_fmt_zar(c3_open)}).",
            sol,
        ],
        worked_solution=sol,
        marks=5,
        duration_mins=6,
    )


def _b37_trial_balance_missing_capital_2d(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    veh = rng.randrange(45000, 95000, 5000)
    stock = rng.randrange(12000, 26000, 1000)
    bank_od = rng.randrange(4000, 11000, 500)
    cred = rng.randrange(7000, 16000, 500)
    sales = rng.randrange(36000, 72000, 2000)
    cos = rng.randrange(20000, 38000, 1000)
    wages = rng.randrange(6000, 14000, 500)
    tot_dr = veh + stock + cos + wages
    cap = tot_dr - bank_od - cred - sales

    headers = ["Account", "Fol.", "Debit", "Credit"]
    raw_rows = [
        [{"value": "Capital", "status": "given"}, {"value": "B1", "status": "given"}, {"value": "", "status": "must_be_empty"}, {"value": _fmt_cell_amt(cap), "status": "required"}],
        [{"value": "Vehicles", "status": "given"}, {"value": "B4", "status": "given"}, {"value": _fmt_cell_amt(veh), "status": "given"}, {"value": "", "status": "must_be_empty"}],
        [{"value": "Trading stock", "status": "given"}, {"value": "B6", "status": "given"}, {"value": _fmt_cell_amt(stock), "status": "required"}, {"value": "", "status": "must_be_empty"}],
        [{"value": "Bank (Overdraft)", "status": "given"}, {"value": "B8", "status": "given"}, {"value": "", "status": "must_be_empty"}, {"value": _fmt_cell_amt(bank_od), "status": "required"}],
        [{"value": "Creditors control", "status": "given"}, {"value": "B9", "status": "given"}, {"value": "", "status": "must_be_empty"}, {"value": _fmt_cell_amt(cred), "status": "given"}],
        [{"value": "Sales", "status": "given"}, {"value": "N1", "status": "given"}, {"value": "", "status": "must_be_empty"}, {"value": _fmt_cell_amt(sales), "status": "required"}],
        [{"value": "Cost of sales", "status": "given"}, {"value": "N2", "status": "given"}, {"value": _fmt_cell_amt(cos), "status": "given"}, {"value": "", "status": "must_be_empty"}],
        [{"value": "Wages", "status": "given"}, {"value": "N4", "status": "given"}, {"value": _fmt_cell_amt(wages), "status": "required"}, {"value": "", "status": "must_be_empty"}],
        [{"value": "Total", "status": "given"}, {"value": "", "status": "given"}, {"value": _fmt_cell_amt(tot_dr), "status": "required"}, {"value": _fmt_cell_amt(tot_dr), "status": "required"}],
    ]
    cell_hints = {
        "r0_c3": f"Capital balances Total Dr ({_fmt_cell_amt(tot_dr)}) minus other Cr items = {_fmt_cell_amt(cap)}.",
        "r2_c2": f"Trading stock is an Asset -> Debit {_fmt_cell_amt(stock)}.",
        "r3_c3": f"Bank overdraft is a Liability -> Credit {_fmt_cell_amt(bank_od)}.",
        "r5_c3": f"Sales is Income -> Credit {_fmt_cell_amt(sales)}.",
        "r7_c2": f"Wages is an Expense -> Debit {_fmt_cell_amt(wages)}.",
        "r8_c2": f"Total Debits = {_fmt_cell_amt(tot_dr)}.",
        "r8_c3": f"Total Credits must match Total Debits = {_fmt_cell_amt(tot_dr)}.",
    }
    derivations = [
        f"Debit column = Vehicles ({_fmt_zar(veh)}) + Trading stock ({_fmt_zar(stock)}) + Cost of sales ({_fmt_zar(cos)}) + Wages ({_fmt_zar(wages)}) = {_fmt_zar(tot_dr)}.",
        f"Known Credit items = Bank overdraft ({_fmt_zar(bank_od)}) + Creditors ({_fmt_zar(cred)}) + Sales ({_fmt_zar(sales)}) = {_fmt_zar(bank_od + cred + sales)}.",
        f"Missing Capital = {_fmt_zar(tot_dr)} - {_fmt_zar(bank_od + cred + sales)} = {_fmt_zar(cap)}.",
    ]
    return _table_q(
        subskill="37_trial_balance_completion_and_missing_capital_2d_table",
        title=f"Trial Balance Completion — {biz}",
        prompt=(
            f"Complete the Trial Balance of {biz} by placing Trading stock ({_fmt_zar(stock)}), Bank Overdraft ({_fmt_zar(bank_od)}), "
            f"Sales ({_fmt_zar(sales)}), and Wages ({_fmt_zar(wages)}) in their correct Debit or Credit columns, then solve for the missing `Capital` balance."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Place Assets and Expenses in Debit; Income and Liabilities (including Bank Overdraft!) in Credit.",
            "Sum the entire Debit column first, then subtract all known Credit items to find Capital.",
            f"Total Dr = Total Cr = {_fmt_cell_amt(tot_dr)}; Capital = {_fmt_cell_amt(cap)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-37",
        concept_id="trial_balance_dr_cr_and_capital",
        misconception_tags=["placed_bank_overdraft_in_debit_column", "placed_wages_in_credit_column"],
        journal_type="trial_balance",
        duration_mins=9,
    )


def _b38_tb_assets_vs_equity_liabilities_bar_graph(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    nca = rng.randrange(90000, 180000, 10000)
    ca = rng.randrange(30000, 70000, 5000)
    liab = rng.randrange(15000, 45000, 5000)
    oe = nca + ca - liab
    svg = _svg_bar_chart(
        f"{biz} — Statement Position from Trial Balance",
        "Balance Sheet Elements Summary",
        [
            ("Non-Current Assets", float(nca), "#0284c7"),
            ("Current Assets", float(ca), "#0ea5e9"),
            ("Owner's Equity", float(oe), "#16a34a"),
            ("Current Liabilities", float(liab), "#dc2626"),
        ],
    )
    sol = f"Total Assets = Non-Current Assets ({_fmt_zar(nca)}) + Current Assets ({_fmt_zar(ca)}) = {_fmt_zar(nca + ca)}. Check: Owner's Equity ({_fmt_zar(oe)}) + Current Liabilities ({_fmt_zar(liab)}) = {_fmt_zar(oe + liab)}."
    return _typed(
        subskill="38_trial_balance_assets_vs_equity_liabilities_bar_graph",
        prompt=f"Refer to the bar graph below showing {biz}'s Balance Sheet balances. Calculate Total Assets and verify that it equals Owner's Equity + Current Liabilities.",
        correct_answer=_fmt_zar(nca + ca),
        accepted_answers=[str(nca + ca), _fmt_zar(nca + ca), _fmt_cell_amt(nca + ca), f"R{nca + ca}"],
        learning_objective_id="EMS9-T4-TXN-38",
        concept_id="accounting_identity_from_trial_balance",
        misconception_tags=["subtracted_liabilities_instead_of_summing_assets"],
        hints=[
            "Total Assets = Non-Current Assets + Current Assets.",
            f"Add {_fmt_zar(nca)} + {_fmt_zar(ca)}.",
            sol,
        ],
        worked_solution=sol,
        diagram_spec=svg,
    )


# ---------------------------------------------------------------------------
# Archetypes 39 - 50
# ---------------------------------------------------------------------------

def _b39_tb_bank_overdraft_credit_mcq(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(["Electrics for All", "Nani Traders", "Valley Traders"])
    od = rng.randrange(7500, 68500, 500)
    return _mcq(
        rng,
        subskill="39_trial_balance_bank_overdraft_credit_column_mcq",
        prompt=f"In the Trial Balance of {biz}, `Bank (B8)` is entered as {_fmt_zar(od)} in the **Credit** column. What does this indicate?",
        correct=f"{biz} has a Bank Overdraft of {_fmt_zar(od)} (a Current Liability owed to the bank).",
        distractors=[
            f"{biz} holds {_fmt_zar(od)} positive cash on deposit in its current bank account.",
            "The bookkeeper made a reversal error because Bank is strictly only ever a Debit item.",
            f"Debtors deposited {_fmt_zar(od)} extra cash at month-end that belongs under Nominal Income.",
        ],
        learning_objective_id="EMS9-T4-TXN-39",
        concept_id="bank_overdraft_credit_trial_balance",
        misconception_tags=["assumed_bank_can_never_appear_in_credit_column"],
        hints=[
            "Recall Nani Traders and Electrics for All: when payments exceed receipts + opening funds, Bank flips sides.",
            "Credit balances in Balance Sheet accounts represent Owner's Equity or Liabilities.",
            "A Credit balance in Bank means Bank Overdraft — money owed to the bank.",
        ],
        worked_solution=f"When `Total payments (CPJ)` exceed available cash, Bank closes with a Credit balance b/d, representing a Bank Overdraft (Current Liability) listed in the Trial Balance Credit column.",
    )


def _b40_ae_cash_and_credit_sales_2d(rng: random.Random) -> Dict[str, Any]:
    s_cash = rng.randrange(1200, 3600, 300)
    c_cash = int(round(s_cash * 2 / 3))
    s_cred = rng.randrange(900, 2700, 300)
    c_cred = int(round(s_cred * 2 / 3))

    headers = ["Transaction", "Account Dr", "Account Cr", "Assets (A)", "Equity (OE)", "Liabilities (L)"]
    raw_rows = [
        [
            {"value": f"1a. Cash sales revenue ({_fmt_zar(s_cash)})", "status": "given"},
            {"value": "Bank", "status": "required"},
            {"value": "Sales", "status": "required"},
            {"value": f"+{s_cash}", "status": "required"},
            {"value": f"+{s_cash}", "status": "required"},
            {"value": "0", "status": "required"},
        ],
        [
            {"value": f"1b. Cash sales stock cost ({_fmt_zar(c_cash)})", "status": "given"},
            {"value": "Cost of sales", "status": "required"},
            {"value": "Trading stock", "status": "required"},
            {"value": f"-{c_cash}", "status": "required"},
            {"value": f"-{c_cash}", "status": "required"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"2a. Credit sale revenue ({_fmt_zar(s_cred)})", "status": "given"},
            {"value": "Debtors control", "status": "required"},
            {"value": "Sales", "status": "given"},
            {"value": f"+{s_cred}", "status": "required"},
            {"value": f"+{s_cred}", "status": "given"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"2b. Credit sale stock cost ({_fmt_zar(c_cred)})", "status": "given"},
            {"value": "Cost of sales", "status": "given"},
            {"value": "Trading stock", "status": "required"},
            {"value": f"-{c_cred}", "status": "required"},
            {"value": f"-{c_cred}", "status": "required"},
            {"value": "0", "status": "given"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Cash inflow increases `Bank`.",
        "r0_c2": "Revenue earned is `Sales`.",
        "r0_c3": f"Bank Asset increases: +{s_cash}.",
        "r0_c4": f"Sales income increases Equity: +{s_cash}.",
        "r0_c5": "No liability affected: 0.",
        "r1_c1": "Expense recognizing stock cost: `Cost of sales`.",
        "r1_c2": "Asset leaving business: `Trading stock`.",
        "r1_c3": f"Trading stock decreases: -{c_cash}.",
        "r1_c4": f"Cost of sales expense reduces Equity: -{c_cash}.",
        "r2_c1": "Customer owes money on credit: `Debtors control`.",
        "r2_c3": f"Debtors control increases Assets: +{s_cred}.",
        "r3_c2": "Stock asset decreases: `Trading stock`.",
        "r3_c3": f"Trading stock decreases: -{c_cred}.",
        "r3_c4": f"Cost of sales reduces Equity: -{c_cred}.",
    }
    derivations = [
        f"Every sale (cash OR credit) has TWO parts: revenue (+A Bank/Debtors, +OE Sales) and cost of stock (-A Trading stock, -OE Cost of sales).",
        f"Cash sale net profit = +{s_cash} - {c_cash} = +{s_cash - c_cash} to both A and OE.",
        f"Credit sale net profit = +{s_cred} - {c_cred} = +{s_cred - c_cred} to both A and OE.",
    ]
    return _table_q(
        subskill="40_accounting_equation_cash_and_credit_sales_2d_table",
        title="Accounting Equation: Cash Sales vs Credit Sales",
        prompt=(
            f"Record BOTH parts (selling price and cost price) on the Accounting Equation (`A = OE + L`) using signed integers like `+{s_cash}` or `-{c_cash}` and `0`:\n"
            f"1. Cash sales per CRR: {_fmt_zar(s_cash)} (Cost price {_fmt_zar(c_cash)}).\n"
            f"2. Credit sale to D Parsons per DJ: {_fmt_zar(s_cred)} (Cost price {_fmt_zar(c_cred)})."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Selling price rows use `+amount` on both Assets (Bank or Debtors control) and OE (Sales).",
            "Cost price rows use `-amount` on both Assets (Trading stock) and OE (Cost of sales).",
            "Liabilities remain `0` on all four lines.",
        ],
        learning_objective_id="EMS9-T4-TXN-40",
        concept_id="accounting_equation_dual_sales_entries",
        misconception_tags=["omitted_cost_of_sales_equation_row", "mixed_bank_and_debtors_control"],
        journal_type="accounting_equation",
        duration_mins=8,
    )


def _b41_ae_asset_swap_and_debtor_receipt_2d(rng: random.Random) -> Dict[str, Any]:
    equip = rng.randrange(4000, 12000, 500)
    deb_rec = rng.randrange(800, 2600, 100)
    headers = ["Transaction", "Account Dr", "Account Cr", "Assets (A)", "Equity (OE)", "Liabilities (L)"]
    raw_rows = [
        [
            {"value": f"1. Bought equipment cash ({_fmt_zar(equip)})", "status": "given"},
            {"value": "Equipment", "status": "required"},
            {"value": "Bank", "status": "required"},
            {"value": f"+{equip} / -{equip}", "status": "required"},
            {"value": "0", "status": "required"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"2. Debtor paid account ({_fmt_zar(deb_rec)})", "status": "given"},
            {"value": "Bank", "status": "required"},
            {"value": "Debtors control", "status": "required"},
            {"value": f"+{deb_rec} / -{deb_rec}", "status": "required"},
            {"value": "0", "status": "required"},
            {"value": "0", "status": "given"},
        ],
    ]
    cell_hints = {
        "r0_c1": "New asset acquired: `Equipment`.",
        "r0_c2": "Asset given up: `Bank`.",
        "r0_c3": f"Equipment +{equip} and Bank -{equip} -> write `+{equip} / -{equip}`.",
        "r0_c4": "Buying an asset for cash is not an expense -> OE = `0`.",
        "r1_c1": "Cash inflow increases `Bank`.",
        "r1_c2": "Amount owed by customer decreases: `Debtors control`.",
        "r1_c3": f"Bank +{deb_rec} and Debtors control -{deb_rec} -> write `+{deb_rec} / -{deb_rec}`.",
        "r1_c4": "Revenue was already earned at credit sale time -> OE = `0`.",
    }
    derivations = [
        f"1. Buying Equipment for cash swaps one Asset for another: +{equip} (Equipment) / -{equip} (Bank), net A change = 0, OE = 0, L = 0.",
        f"2. Collecting from a debtor converts Debtors control into Bank cash: +{deb_rec} (Bank) / -{deb_rec} (Debtors control), OE = 0, L = 0.",
    ]
    return _table_q(
        subskill="41_accounting_equation_asset_swap_and_debtor_receipt_2d_table",
        title="Accounting Equation: Asset-for-Asset Swaps",
        prompt=(
            f"Show the effect of these two cash transactions on the Accounting Equation (enter dual Asset effects formatted like `+5000 / -5000`):\n"
            f"1. Bought computer equipment cash via EFT, {_fmt_zar(equip)}.\n"
            f"2. Received {_fmt_zar(deb_rec)} from a debtor in settlement of their account."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Both transactions exchange one Asset for another Asset (net change in Total Assets is zero).",
            "Neither transaction creates Income or Expense, so Equity (OE) is `0`.",
            f"Row 1 Assets = `+{equip} / -{equip}`; Row 2 Assets = `+{deb_rec} / -{deb_rec}`.",
        ],
        learning_objective_id="EMS9-T4-TXN-41",
        concept_id="accounting_equation_asset_swaps",
        misconception_tags=["treated_debtor_collection_as_plus_equity"],
        journal_type="accounting_equation",
    )


def _b42_ae_split_cheque_and_split_invoice_2d(rng: random.Random) -> Dict[str, Any]:
    veh = rng.randrange(80000, 140000, 5000)
    fuel = rng.randrange(500, 1500, 100)
    stock = rng.randrange(3000, 7500, 500)
    stat = rng.randrange(400, 1200, 100)
    headers = ["Transaction Part", "Account Dr", "Account Cr", "Assets (A)", "Equity (OE)", "Liabilities (L)"]
    raw_rows = [
        [
            {"value": f"1a. Cash purchase of vehicle ({_fmt_zar(veh)})", "status": "given"},
            {"value": "Vehicles", "status": "required"},
            {"value": "Bank", "status": "given"},
            {"value": f"+{veh} / -{veh}", "status": "required"},
            {"value": "0", "status": "required"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"1b. Cash fuel on same cheque ({_fmt_zar(fuel)})", "status": "given"},
            {"value": "Fuel", "status": "required"},
            {"value": "Bank", "status": "given"},
            {"value": f"-{fuel}", "status": "required"},
            {"value": f"-{fuel}", "status": "required"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"2a. Credit stock on invoice ({_fmt_zar(stock)})", "status": "given"},
            {"value": "Trading stock", "status": "required"},
            {"value": "Creditors control", "status": "required"},
            {"value": f"+{stock}", "status": "required"},
            {"value": "0", "status": "given"},
            {"value": f"+{stock}", "status": "required"},
        ],
        [
            {"value": f"2b. Credit stationery on same invoice ({_fmt_zar(stat)})", "status": "given"},
            {"value": "Stationery", "status": "required"},
            {"value": "Creditors control", "status": "given"},
            {"value": "0", "status": "given"},
            {"value": f"-{stat}", "status": "required"},
            {"value": f"+{stat}", "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Asset account: `Vehicles`.",
        "r0_c3": f"+{veh} / -{veh}.",
        "r0_c4": "Buying vehicle for cash: OE = 0.",
        "r1_c1": "Expense account: `Fuel`.",
        "r1_c3": f"Bank cash leaves: -{fuel}.",
        "r1_c4": f"Fuel expense lowers Equity: -{fuel}.",
        "r2_c1": "Asset bought on credit: `Trading stock`.",
        "r2_c2": "Liability created: `Creditors control`.",
        "r2_c3": f"Stock rises: +{stock}.",
        "r2_c5": f"Creditors owed rises: +{stock}.",
        "r3_c1": "Expense bought on credit: `Stationery`.",
        "r3_c4": f"Stationery expense reduces Equity: -{stat}.",
        "r3_c5": f"Creditors owed rises: +{stat}.",
    }
    derivations = [
        f"Split CPJ cheque: Vehicle swaps Assets (+{veh} / -{veh}); Fuel reduces Bank (-{fuel}) and OE (-{fuel}).",
        f"Split CJ invoice: Stock raises Assets (+{stock}) and Liabilities (+{stock}); Stationery lowers OE (-{stat}) and raises Liabilities (+{stat}).",
    ]
    return _table_q(
        subskill="42_accounting_equation_split_cheque_and_split_invoice_2d_table",
        title="Accounting Equation: Split Cheque & Split Supplier Invoice",
        prompt=(
            f"Analyze both compound transactions on `A = OE + L`:\n"
            f"1. Paid one EFT for a vehicle ({_fmt_zar(veh)}) plus a tank of fuel ({_fmt_zar(fuel)}).\n"
            f"2. Received one credit invoice for Trading stock ({_fmt_zar(stock)}) plus Stationery ({_fmt_zar(stat)})."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Separate the Asset part from the Expense part inside each split document.",
            "Remember Trading stock on credit increases Assets + Liabilities, whereas Stationery on credit decreases Equity + increases Liabilities.",
            "Double-check signs on each line so A = OE + L holds row by row.",
        ],
        learning_objective_id="EMS9-T4-TXN-42",
        concept_id="accounting_equation_compound_split_items",
        misconception_tags=["put_stationery_under_assets", "treated_vehicle_purchase_as_expense"],
        journal_type="accounting_equation",
        duration_mins=9,
    )


def _b43_ae_drawings_and_operating_expense_2d(rng: random.Random) -> Dict[str, Any]:
    draw = rng.randrange(200, 900, 50)
    wages = rng.randrange(800, 2200, 100)
    stat_c = rng.randrange(250, 750, 50)
    headers = ["Transaction", "Account Dr", "Account Cr", "Assets (A)", "Equity (OE)", "Liabilities (L)"]
    raw_rows = [
        [
            {"value": f"1. Owner took cash for personal phone ({_fmt_zar(draw)})", "status": "given"},
            {"value": "Drawings", "status": "required"},
            {"value": "Bank", "status": "given"},
            {"value": f"-{draw}", "status": "required"},
            {"value": f"-{draw}", "status": "required"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"2. Paid weekly wages cash ({_fmt_zar(wages)})", "status": "given"},
            {"value": "Wages", "status": "required"},
            {"value": "Bank", "status": "given"},
            {"value": f"-{wages}", "status": "required"},
            {"value": f"-{wages}", "status": "required"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"3. Bought stationery on credit ({_fmt_zar(stat_c)})", "status": "given"},
            {"value": "Stationery", "status": "required"},
            {"value": "Creditors control", "status": "required"},
            {"value": "0", "status": "required"},
            {"value": f"-{stat_c}", "status": "required"},
            {"value": f"+{stat_c}", "status": "required"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Owner's private use of business funds is `Drawings`.",
        "r0_c3": f"Bank decreases: -{draw}.",
        "r0_c4": f"Drawings reduces Equity: -{draw}.",
        "r1_c1": "Expense paid: `Wages`.",
        "r1_c3": f"Bank decreases: -{wages}.",
        "r1_c4": f"Wages expense reduces Equity: -{wages}.",
        "r2_c1": "Expense incurred: `Stationery`.",
        "r2_c2": "Supplier owed: `Creditors control`.",
        "r2_c3": "No asset bought and no cash paid yet -> Assets = `0`.",
        "r2_c4": f"Expense reduces Equity: -{stat_c}.",
        "r2_c5": f"Liability rises: +{stat_c}.",
    }
    derivations = [
        f"1. Drawings: Bank -{draw} (A) = Drawings -{draw} (OE).",
        f"2. Cash Wages: Bank -{wages} (A) = Wages -{wages} (OE).",
        f"3. Credit Stationery: 0 (A) = -{stat_c} (OE) + {stat_c} (L).",
    ]
    return _table_q(
        subskill="43_accounting_equation_drawings_and_operating_expense_2d_table",
        title="Accounting Equation: Drawings vs Cash & Credit Expenses",
        prompt="Show the Accounting Equation effect of Drawings, cash Wages, and credit Stationery.",
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Both Drawings and Cash Expenses reduce Assets (`Bank`) and Equity (`OE`).",
            "An Expense on credit keeps Assets `0` while lowering Equity (`-`) and increasing Liabilities (`+`).",
            "Check each row satisfies `A = OE + L`.",
        ],
        learning_objective_id="EMS9-T4-TXN-43",
        concept_id="accounting_equation_drawings_expenses",
        misconception_tags=["debited_telephone_instead_of_drawings", "treated_credit_stationery_as_asset"],
        journal_type="accounting_equation",
    )


def _b44_working_capital_cash_credit_flow_diagram(rng: random.Random) -> Dict[str, Any]:
    stock_val = rng.randrange(15000, 35000, 2500)
    debtors_val = rng.randrange(12000, 28000, 2000)
    svg = _svg_cycle_flow(
        "Working Capital Flow: Stock to Credit to Cash",
        [
            ("CPJ / CJ", f"Buy Stock ({_fmt_zar(stock_val)})", "#fef3c7"),
            ("DJ", f"Credit Sales ({_fmt_zar(debtors_val)})", "#e0f2fe"),
            ("CRJ", "Debtor Receipts", "#dcfce7"),
            ("Bank", "Fund Next Cycle", "#ede9fe"),
        ],
    )
    return _mcq(
        rng,
        subskill="44_working_capital_cash_credit_flow_diagram",
        prompt="Refer to the flowchart below. Why can a profitable business with strong `DJ` Credit Sales still face a Bank Overdraft in `CPJ`?",
        correct="Because credit sales tie cash up in Debtors Control until customers actually pay in the `CRJ`, while suppliers and wages must be paid in cash via `CPJ` first.",
        distractors=[
            "Because Credit Sales in the `DJ` always reduce Owner's Equity and create cash outflows.",
            "Because `Cost of sales` is paid twice—once in `CJ` and once in `DJ`.",
            "Because `Trading stock` bought on credit in `CJ` deducts cash from `Bank` immediately.",
        ],
        learning_objective_id="EMS9-T4-TXN-44",
        concept_id="profit_vs_cash_flow_credit_cycle",
        misconception_tags=["equated_credit_sales_profit_with_immediate_cash"],
        hints=[
            "Trace the gap between the `DJ` box (selling on credit) and the `CRJ` box (collecting cash).",
            "Cash only enters `Bank` at the `CRJ` stage, NOT when an invoice is issued in `DJ`.",
            "Slow debtor collections delay `CRJ` inflows while `CPJ` outflows happen immediately.",
        ],
        worked_solution="Profitable credit sales (`DJ`) increase Debtors Control rather than Bank; if debtors pay slowly (`CRJ`) while expenses/creditors are paid via `CPJ`, Bank can run into overdraft.",
        diagram_spec=svg,
    )


def _b45_error_detection_bank_reversal_in_gl_mcq(rng: random.Random) -> Dict[str, Any]:
    crj_tot = rng.randrange(18000, 42000, 1000)
    cpj_tot = rng.randrange(12000, 32000, 1000)
    return _mcq(
        rng,
        subskill="45_cash_credit_error_detection_bank_reversal_in_gl_mcq",
        prompt=(
            f"A trainee bookkeeper posted `Total receipts CRJ` ({_fmt_zar(crj_tot)}) to the **Credit** side of `Bank (B9)` "
            f"and `Total payments CPJ` ({_fmt_zar(cpj_tot)}) to the **Debit** side of `Bank (B9)`. What mistake did they make?"
        ),
        correct="They reversed the Bank ledger rules: Bank is an Asset, so CRJ receipts must be Debited (+) and CPJ payments must be Credited (-).",
        distractors=[
            "They posted the correct sides for Bank, but forgot to write `Sales` as the details.",
            "Only `CPJ` should post to Bank; `CRJ` posts directly to Debtors Control.",
            "Bank is a Liability account, so receipts always go on the Credit side.",
        ],
        learning_objective_id="EMS9-T4-TXN-45",
        concept_id="bank_ledger_reversal_audit",
        misconception_tags=["confused_bank_statement_credit_with_ledger_debit"],
        hints=[
            "From the business's own General Ledger point of view, what element is `Bank`?",
            "Assets increase on Debit (`CRJ Total receipts`) and decrease on Credit (`CPJ Total payments`).",
            "They reversed Dr and Cr in the Bank General Ledger account.",
        ],
        worked_solution="In the business's General Ledger, `Bank` is an Asset: cash receipts (`CRJ Total receipts`) belong on the Debit (+) side and cash payments (`CPJ Total payments`) belong on the Credit (-) side.",
    )


def _b46_reconciling_debtors_schedule_discrepancy_mcq(rng: random.Random) -> Dict[str, Any]:
    inv = rng.randrange(450, 1450, 50)
    debtor = rng.choice(_DEBTOR_NAMES)
    return _mcq(
        rng,
        subskill="46_reconciling_debtors_schedule_discrepancy_diagnosis_mcq",
        prompt=(
            f"At month-end, General Ledger `Debtors Control (B7)` exceeds the `Debtors Schedule` total by exactly {_fmt_zar(inv)}. "
            "Which posting mistake explains this discrepancy?"
        ),
        correct=f"Credit invoice no. 331 for {_fmt_zar(inv)} was included in the `DJ` column total posted to `Debtors Control`, but omitted from {debtor}'s individual Debtors Ledger account.",
        distractors=[
            f"Cash sales of {_fmt_zar(inv)} from the `CRJ` were omitted from `Sales (N1)`.",
            f"A supplier invoice of {_fmt_zar(inv)} was posted to `Creditors Control` twice.",
            f"The bookkeeper omitted {debtor}'s R 0,00 settled balance from the Debtors Schedule.",
        ],
        learning_objective_id="EMS9-T4-TXN-46",
        concept_id="debtors_control_vs_schedule_error_diagnosis",
        misconception_tags=["ignored_daily_posting_vs_monthly_total_split"],
        hints=[
            "Remember: Debtors Control gets the monthly DJ total, whereas the Debtors Schedule sums the daily individual Debtors Ledger pages.",
            f"If Control is {_fmt_zar(inv)} higher than the Schedule, an invoice debit is missing from a specific debtor's account.",
            f"An invoice of {_fmt_zar(inv)} was cast in DJ total (`Debtors Control`) but skipped in `{debtor}`'s ledger.",
        ],
        worked_solution=f"Because `Debtors Control` is {_fmt_zar(inv)} higher than the Debtors Schedule, the monthly DJ total included an invoice of {_fmt_zar(inv)} that was left out when posting daily to `{debtor}`'s Debtors Ledger.",
    )


def _b47_tb_gross_profit_from_nominal_calc(rng: random.Random) -> Dict[str, Any]:
    markup = rng.choice([25, 40, 50, 60])
    cos = rng.randrange(40000, 96000, 4000)
    sales = int(round(cos * (100 + markup) / 100))
    gp = sales - cos
    sol = (
        f"Gross Profit = Sales (N1 Cr) - Cost of sales (N2 Dr) = {_fmt_zar(sales)} - {_fmt_zar(cos)} = {_fmt_zar(gp)}.\n"
        f"Check mark-up % = ({gp} / {cos}) × 100 = {markup}%."
    )
    return _typed(
        subskill="47_trial_balance_gross_profit_from_nominal_section_calc",
        prompt=(
            f"The Nominal accounts section of a Trial Balance reports:\n"
            f"- Sales (N1 Cr): {_fmt_zar(sales)}\n"
            f"- Cost of sales (N2 Dr): {_fmt_zar(cos)}\n\n"
            "Calculate the Gross Profit (Rand value)."
        ),
        correct_answer=_fmt_zar(gp),
        accepted_answers=[str(gp), _fmt_zar(gp), _fmt_cell_amt(gp), f"R{gp}"],
        learning_objective_id="EMS9-T4-TXN-47",
        concept_id="gross_profit_from_trial_balance",
        misconception_tags=["subtracted_expenses_before_gross_profit"],
        hints=[
            "Gross Profit uses ONLY Sales minus Cost of sales.",
            f"Subtract {_fmt_zar(cos)} from {_fmt_zar(sales)}.",
            sol,
        ],
        worked_solution=sol,
    )


def _b48_integrated_discount_to_creditors_ledger_2d(rng: random.Random) -> Dict[str, Any]:
    sup = rng.choice(_CREDITOR_NAMES)
    open_bal = rng.randrange(1500, 4500, 500)
    list_price = rng.randrange(2000, 6000, 200)
    disc = rng.choice([10, 25])
    net_inv = int(round(list_price * (100 - disc) / 100))
    b1 = open_bal + net_inv
    pay = rng.randrange(1000, 2200, 100)
    b2 = b1 - pay

    headers = ["Date", "Details / Doc no.", "Fol.", "Debit (-)", "Credit (+)", "Balance"]
    raw_rows = [
        [
            {"value": "Aug 01", "status": "given"},
            {"value": "Account rendered", "status": "given"},
            {"value": "", "status": "given"},
            {"value": "", "status": "must_be_empty"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(open_bal), "status": "given"},
        ],
        [
            {"value": "08", "status": "given"},
            {"value": "Invoice 509 (net)", "status": "given"},
            {"value": "CJ8", "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(net_inv), "status": "required"},
            {"value": _fmt_cell_amt(b1), "status": "required"},
        ],
        [
            {"value": "22", "status": "given"},
            {"value": "EFT / Cheque 215", "status": "given"},
            {"value": "CPJ8", "status": "required"},
            {"value": _fmt_cell_amt(pay), "status": "required"},
            {"value": "", "status": "must_be_empty"},
            {"value": _fmt_cell_amt(b2), "status": "required"},
        ],
    ]
    cell_hints = {
        "r1_c2": "Supplier invoice posts from `CJ8`.",
        "r1_c4": f"Net invoice = {_fmt_cell_amt(list_price)} × {100 - disc}% = {_fmt_cell_amt(net_inv)}.",
        "r1_c5": f"Balance = {_fmt_cell_amt(open_bal)} + {_fmt_cell_amt(net_inv)} = {_fmt_cell_amt(b1)}.",
        "r2_c2": "EFT payment posts from `CPJ8`.",
        "r2_c3": f"Payment decreases liability: Debit (-) {_fmt_cell_amt(pay)}.",
        "r2_c5": f"Closing balance = {_fmt_cell_amt(b1)} - {_fmt_cell_amt(pay)} = {_fmt_cell_amt(b2)}.",
    }
    derivations = [
        f"Trade discount first: {_fmt_zar(list_price)} - {disc}% = {_fmt_zar(net_inv)} net invoice entered Cr (+) from CJ8.",
        f"After EFT payment of {_fmt_zar(pay)} on Debit (-) from CPJ8, final balance = {_fmt_zar(b2)}.",
    ]
    return _table_q(
        subskill="48_integrated_invoice_discount_to_creditors_ledger_2d_table",
        title=f"Discounted Invoice to Creditors Ledger — {sup}",
        prompt=(
            f"Update {sup}'s Creditors Ledger after:\n"
            f"- Aug 01: Opening balance {_fmt_zar(open_bal)}\n"
            f"- Aug 08: Received Invoice 509 listed at {_fmt_zar(list_price)} less {disc}% trade discount\n"
            f"- Aug 22: Paid {_fmt_zar(pay)} via EFT (Cheque/EFT 215)"
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            f"Deduct {disc}% trade discount BEFORE posting to the Credit (+) column.",
            "Subtract the EFT payment on the Debit (-) side.",
            f"Net invoice = {_fmt_cell_amt(net_inv)}; Closing balance = {_fmt_cell_amt(b2)}.",
        ],
        learning_objective_id="EMS9-T4-TXN-48",
        concept_id="trade_discount_to_creditors_ledger_chain",
        misconception_tags=["posted_gross_price_to_creditors_ledger"],
        journal_type="creditors_ledger",
        duration_mins=8,
    )


def _b49_ae_comprehensive_six_transaction_2d(rng: random.Random) -> Dict[str, Any]:
    t_cap = rng.randrange(15000, 35000, 5000)
    t_rent = rng.randrange(1200, 3200, 200)
    t_stock_gross = rng.randrange(1000, 3000, 200)
    t_stock_net = int(round(t_stock_gross * 0.9))  # 10% trade discount
    t_sale_s = rng.randrange(900, 2100, 150)
    t_sale_c = int(round(t_sale_s * 2 / 3))
    t_pay_cred = rng.randrange(500, 1300, 100)
    t_draw = rng.randrange(150, 550, 50)

    headers = ["No.", "Journal", "Account Dr", "Account Cr", "A", "OE", "L"]
    raw_rows = [
        [
            {"value": f"1. Owner deposited capital ({_fmt_zar(t_cap)})", "status": "given"},
            {"value": "CRJ", "status": "required"},
            {"value": "Bank", "status": "required"},
            {"value": "Capital", "status": "required"},
            {"value": f"+{t_cap}", "status": "required"},
            {"value": f"+{t_cap}", "status": "required"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"2. Received rent from tenant ({_fmt_zar(t_rent)})", "status": "given"},
            {"value": "CRJ", "status": "required"},
            {"value": "Bank", "status": "given"},
            {"value": "Rent income", "status": "required"},
            {"value": f"+{t_rent}", "status": "required"},
            {"value": f"+{t_rent}", "status": "required"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"3. Bought stock on credit {_fmt_zar(t_stock_gross)} less 10% disc", "status": "given"},
            {"value": "CJ", "status": "required"},
            {"value": "Trading stock", "status": "required"},
            {"value": "Creditors control", "status": "required"},
            {"value": f"+{t_stock_net}", "status": "required"},
            {"value": "0", "status": "given"},
            {"value": f"+{t_stock_net}", "status": "required"},
        ],
        [
            {"value": f"4a. Credit sale ({_fmt_zar(t_sale_s)})", "status": "given"},
            {"value": "DJ", "status": "required"},
            {"value": "Debtors control", "status": "required"},
            {"value": "Sales", "status": "given"},
            {"value": f"+{t_sale_s}", "status": "required"},
            {"value": f"+{t_sale_s}", "status": "required"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"4b. Cost of credit sale ({_fmt_zar(t_sale_c)})", "status": "given"},
            {"value": "DJ", "status": "given"},
            {"value": "Cost of sales", "status": "required"},
            {"value": "Trading stock", "status": "required"},
            {"value": f"-{t_sale_c}", "status": "required"},
            {"value": f"-{t_sale_c}", "status": "required"},
            {"value": "0", "status": "given"},
        ],
        [
            {"value": f"5. Paid creditor by EFT ({_fmt_zar(t_pay_cred)})", "status": "given"},
            {"value": "CPJ", "status": "required"},
            {"value": "Creditors control", "status": "required"},
            {"value": "Bank", "status": "given"},
            {"value": f"-{t_pay_cred}", "status": "required"},
            {"value": "0", "status": "given"},
            {"value": f"-{t_pay_cred}", "status": "required"},
        ],
        [
            {"value": f"6. Owner private bill paid by EFT ({_fmt_zar(t_draw)})", "status": "given"},
            {"value": "CPJ", "status": "given"},
            {"value": "Drawings", "status": "required"},
            {"value": "Bank", "status": "given"},
            {"value": f"-{t_draw}", "status": "required"},
            {"value": f"-{t_draw}", "status": "required"},
            {"value": "0", "status": "given"},
        ],
    ]
    cell_hints = {
        "r0_c1": "CRJ", "r0_c2": "Bank", "r0_c3": "Capital", "r0_c4": f"+{t_cap}", "r0_c5": f"+{t_cap}",
        "r1_c1": "CRJ", "r1_c3": "Rent income", "r1_c4": f"+{t_rent}", "r1_c5": f"+{t_rent}",
        "r2_c1": "CJ", "r2_c2": "Trading stock", "r2_c3": "Creditors control", "r2_c4": f"+{t_stock_net}", "r2_c6": f"+{t_stock_net}",
        "r3_c1": "DJ", "r3_c2": "Debtors control", "r3_c4": f"+{t_sale_s}", "r3_c5": f"+{t_sale_s}",
        "r4_c2": "Cost of sales", "r4_c3": "Trading stock", "r4_c4": f"-{t_sale_c}", "r4_c5": f"-{t_sale_c}",
        "r5_c1": "CPJ", "r5_c2": "Creditors control", "r5_c4": f"-{t_pay_cred}", "r5_c6": f"-{t_pay_cred}",
        "r6_c2": "Drawings", "r6_c4": f"-{t_draw}", "r6_c5": f"-{t_draw}",
    }
    derivations = [
        f"1. Capital deposit: CRJ | Dr Bank / Cr Capital | +{t_cap} A = +{t_cap} OE.",
        f"2. Rent received: CRJ | Dr Bank / Cr Rent income | +{t_rent} A = +{t_rent} OE.",
        f"3. Net credit stock = {_fmt_zar(t_stock_gross)} × 90% = {_fmt_zar(t_stock_net)}: CJ | +{t_stock_net} A = +{t_stock_net} L.",
        f"4. Credit sale revenue (+{t_sale_s} A/OE) & stock cost (-{t_sale_c} A/OE).",
        f"5. Paid creditor: CPJ | -{t_pay_cred} A = -{t_pay_cred} L.",
        f"6. Owner private bill: CPJ | Dr Drawings / Cr Bank | -{t_draw} A = -{t_draw} OE.",
    ]
    return _table_q(
        subskill="49_accounting_equation_comprehensive_six_transaction_2d_table",
        title="Integrated Cash & Credit Accounting Equation",
        prompt="Complete the Journal, Debit/Credit accounts, and `A = OE + L` effects for all six integrated cash and credit transactions.",
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints=[
            "Apply the 10% trade discount immediately in row 3 before writing `Trading stock` and `Creditors control`.",
            "Every sale splits into revenue (+A/+OE) and Cost of sales (-A/-OE).",
            "Owner private payments via business funds debit `Drawings` (-A/-OE).",
        ],
        learning_objective_id="EMS9-T4-TXN-49",
        concept_id="comprehensive_cash_credit_accounting_equation",
        misconception_tags=["forgot_10pct_trade_discount", "confused_creditor_payment_with_expense"],
        journal_type="accounting_equation",
        duration_mins=10,
    )


def _b50_integrated_mastery_synthesis(rng: random.Random) -> Dict[str, Any]:
    biz = rng.choice(_BIZ_NAMES)
    open_stock = rng.randrange(15000, 32000, 1000)
    cpj_stock = rng.randrange(4000, 9500, 500)
    cj_stock = rng.randrange(6000, 14000, 500)
    crj_cos = rng.randrange(2000, 5000, 500)
    dj_cos = rng.randrange(3000, 7500, 500)
    close_stock = open_stock + cpj_stock + cj_stock - crj_cos - dj_cos

    open_bank = rng.randrange(6000, 14000, 500)
    crj_tot = rng.randrange(14000, 28000, 500)
    cpj_tot = rng.randrange(9000, 19000, 500)
    close_bank = open_bank + crj_tot - cpj_tot

    sol = (
        f"1. Closing Trading stock = {_fmt_zar(open_stock)} + {_fmt_zar(cpj_stock)} (CPJ) + {_fmt_zar(cj_stock)} (CJ) - {_fmt_zar(crj_cos)} (CRJ CoS) - {_fmt_zar(dj_cos)} (DJ CoS) = {_fmt_zar(close_stock)}.\n"
        f"2. Closing Bank = {_fmt_zar(open_bank)} + {_fmt_zar(crj_tot)} (CRJ) - {_fmt_zar(cpj_tot)} (CPJ) = {_fmt_zar(close_bank)}.\n"
        f"3. Combined closing asset balance = {_fmt_zar(close_stock)} + {_fmt_zar(close_bank)} = {_fmt_zar(close_stock + close_bank)}."
    )
    tot_combined = close_stock + close_bank
    return _typed(
        subskill="50_integrated_cash_credit_end_to_end_mastery_synthesis",
        prompt=(
            f"Synthesize all four subsidiary journals of {biz} for October:\n"
            f"- Opening balances: Trading stock {_fmt_zar(open_stock)}, Bank (Dr) {_fmt_zar(open_bank)}\n"
            f"- CRJ totals: Bank receipts {_fmt_zar(crj_tot)}, Cost of cash sales {_fmt_zar(crj_cos)}\n"
            f"- CPJ totals: Bank payments {_fmt_zar(cpj_tot)}, Cash stock purchases {_fmt_zar(cpj_stock)}\n"
            f"- DJ total Cost of credit sales: {_fmt_zar(dj_cos)}\n"
            f"- CJ total Credit stock purchases: {_fmt_zar(cj_stock)}\n\n"
            "Calculate the combined closing balance of `Trading stock + Bank` on 31 October."
        ),
        correct_answer=_fmt_zar(tot_combined),
        accepted_answers=[str(tot_combined), _fmt_zar(tot_combined), _fmt_cell_amt(tot_combined), f"R{tot_combined}"],
        learning_objective_id="EMS9-T4-TXN-50",
        concept_id="end_to_end_journal_to_asset_synthesis",
        misconception_tags=["subtracted_purchases_or_added_cost_of_sales", "confused_total_cpj_with_stock_cpj"],
        hints=[
            "Compute Closing Trading Stock using ONLY stock movements (`open + CPJ stock + CJ stock - CRJ CoS - DJ CoS`).",
            "Compute Closing Bank using `open Bank + CRJ Bank receipts - CPJ Bank payments`.",
            sol,
        ],
        worked_solution=sol,
        marks=6,
        duration_mins=8,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_general_ledger_balance_sheet_vs_nominal_classification_2d_table": _b26_gl_bs_vs_nominal_classification_2d,
    "27_general_ledger_trading_stock_t_account_2d_table": _b27_gl_trading_stock_t_account_2d,
    "28_general_ledger_debtors_control_t_account_2d_table": _b28_gl_debtors_control_t_account_2d,
    "29_general_ledger_creditors_control_t_account_2d_table": _b29_gl_creditors_control_t_account_2d,
    "30_general_ledger_bank_account_favourable_to_overdraft_2d_table": _b30_gl_bank_overdraft_2d,
    "31_posting_crj_dj_to_sales_and_cost_of_sales_ledger_mcq": _b31_posting_crj_dj_to_sales_and_cos_mcq,
    "32_nominal_expense_account_cpj_and_cj_combined_posting_typed": _b32_nominal_expense_cpj_and_cj_combined_calc,
    "33_debtors_ledger_three_column_dr_plus_cr_minus_2d_table": _b33_debtors_ledger_3col_2d,
    "34_creditors_ledger_three_column_cr_plus_dr_minus_2d_table": _b34_creditors_ledger_3col_2d,
    "35_debtors_schedule_reconciliation_with_control_2d_table": _b35_debtors_schedule_reconciliation_2d,
    "36_creditors_schedule_and_missing_account_deduction": _b36_creditors_schedule_missing_account_deduction,
    "37_trial_balance_completion_and_missing_capital_2d_table": _b37_trial_balance_missing_capital_2d,
    "38_trial_balance_assets_vs_equity_liabilities_bar_graph": _b38_tb_assets_vs_equity_liabilities_bar_graph,
    "39_trial_balance_bank_overdraft_credit_column_mcq": _b39_tb_bank_overdraft_credit_mcq,
    "40_accounting_equation_cash_and_credit_sales_2d_table": _b40_ae_cash_and_credit_sales_2d,
    "41_accounting_equation_asset_swap_and_debtor_receipt_2d_table": _b41_ae_asset_swap_and_debtor_receipt_2d,
    "42_accounting_equation_split_cheque_and_split_invoice_2d_table": _b42_ae_split_cheque_and_split_invoice_2d,
    "43_accounting_equation_drawings_and_operating_expense_2d_table": _b43_ae_drawings_and_operating_expense_2d,
    "44_working_capital_cash_credit_flow_diagram": _b44_working_capital_cash_credit_flow_diagram,
    "45_cash_credit_error_detection_bank_reversal_in_gl_mcq": _b45_error_detection_bank_reversal_in_gl_mcq,
    "46_reconciling_debtors_schedule_discrepancy_diagnosis_mcq": _b46_reconciling_debtors_schedule_discrepancy_mcq,
    "47_trial_balance_gross_profit_from_nominal_section_calc": _b47_tb_gross_profit_from_nominal_calc,
    "48_integrated_invoice_discount_to_creditors_ledger_2d_table": _b48_integrated_discount_to_creditors_ledger_2d,
    "49_accounting_equation_comprehensive_six_transaction_2d_table": _b49_ae_comprehensive_six_transaction_2d,
    "50_integrated_cash_credit_end_to_end_mastery_synthesis": _b50_integrated_mastery_synthesis,
}
