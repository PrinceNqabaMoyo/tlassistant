"""Fundile Learning - Grade 12 Accounting Cash Flow Statement Generator.
NSC Accounting Paper 1 Exam Standard: Cash Flow Statement & Notes.
100% deterministic zero-LLM question generator conforming to the 6-Pillar Contract.

Features:
- Exam Ceiling (mode='compound', 15 marks): Complete 2D tabular Cash Flow Statement:
  * Operating activities: Cash generated from operations, working capital changes,
    interest paid, dividends paid, taxation paid.
  * Investing activities: Purchase of fixed assets, proceeds from disposal of fixed assets.
  * Financing activities: Proceeds from new shares issued, buyback of shares, change in borrowings.
  * Net change in cash and cash equivalents, opening and closing cash balances.
- 2D tabular schema with cell coordinates t0_r{rix}_c{cix} and cell types:
  'required', 'given', 'must_be_empty'.
- Deduction rules: {"rule": "must_be_empty_filled", "penalty": -1}.
- Misconception tags:
  'added_instead_of_subtracted_dividends_paid'
  'forgot_negative_tax_paid'
  'inverted_working_capital_inventory'
  'omitted_fixed_asset_disposal_proceeds'
- Adaptive scaffolding sub-drills (3-4 marks each):
  * 'elementary_taxation_paid'
  * 'elementary_dividends_paid'
  * 'elementary_working_capital'
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional, Tuple

from ..sa_naming_engine import generate_sa_enterprise


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int) -> str:
    """Format integer/float as South African currency spacing without decimal if integer."""
    rounded = int(round(val))
    return f"{rounded:,}".replace(",", " ")


def _fmt_bracket(val: float | int) -> str:
    """Format negative amounts in accounting brackets (xxx)."""
    num = int(round(val))
    if num < 0:
        return f"({_fmt_sa(abs(num))})"
    return _fmt_sa(num)


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _pick_company(r: random.Random) -> str:
    ent = generate_sa_enterprise(r, form="Public Company")
    return ent.get("business_name") or "Khumalo Holdings Ltd"


# ============================================================================
# SUB-DRILL 1: Elementary Taxation Paid (4 Marks)
# ============================================================================
def _build_taxation_paid_drill(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    year = r.choice([2024, 2025, 2026])

    # SARS liability opening: R30k - R95k
    sars_open = r.randint(30, 95) * 1000
    # Income tax expense for year: R180k - R450k
    tax_expense = r.randint(18, 45) * 10000
    # SARS liability closing: R25k - R85k
    sars_close = r.randint(25, 85) * 1000

    # Tax paid = Opening liability + Tax expense - Closing liability
    tax_paid = sars_open + tax_expense - sars_close

    prompt = (
        f"You are provided with extracts from the accounting records of **{company}** "
        f"for the financial year ended 28 February {year}.\n\n"
        f"**Information from Balance Sheet and Income Statement:**\n"
        f"• SARS: Income tax owing on 1 March {year-1} (Opening balance): R{_fmt_sa(sars_open)}\n"
        f"• Income tax expense per Income Statement for the year: R{_fmt_sa(tax_expense)}\n"
        f"• SARS: Income tax owing on 28 February {year} (Closing balance): R{_fmt_sa(sars_close)}\n\n"
        f"**Required:**\n"
        f"Complete the table below to calculate the **Taxation paid** to be reflected in the "
        f"Cash Flow Statement for the year ended 28 February {year}. Show outflows in brackets."
    )

    headers = ["SARS (Income Tax) Calculation Note", "Amount (R)"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "Amount owing at beginning of year", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": _fmt_sa(sars_open), "type": "given", "editable": False},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "Income tax expense per Income Statement", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": str(tax_expense), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "Subtotal: Total tax obligation", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": str(sars_open + tax_expense), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "Less: Amount owing at end of year", "type": "given", "editable": False},
            {"coordinate": "t0_r3_c1", "value": f"({_fmt_sa(sars_close)})", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r4_c0", "value": "Taxation paid in cash during the year", "type": "given", "editable": False},
            {"coordinate": "t0_r4_c1", "value": f"({_fmt_sa(tax_paid)})", "type": "required", "editable": True},
        ],
    ]

    correct_map = {
        "t0_r1_c1": str(tax_expense),
        "t0_r2_c1": str(sars_open + tax_expense),
        "t0_r3_c1": f"({sars_close})",
        "t0_r4_c1": f"({tax_paid})",
    }

    cell_hints = {
        "t0_r1_c1": f"Enter the income tax expense for the current year: R{_fmt_sa(tax_expense)}.",
        "t0_r2_c1": f"Total tax obligation = Opening balance (R{_fmt_sa(sars_open)}) + Current tax expense (R{_fmt_sa(tax_expense)}) = R{_fmt_sa(sars_open + tax_expense)}.",
        "t0_r3_c1": f"Deduct the closing liability still owing to SARS at year end: ({_fmt_sa(sars_close)}).",
        "t0_r4_c1": f"Taxation paid in cash = R{_fmt_sa(sars_open + tax_expense)} - R{_fmt_sa(sars_close)} = ({_fmt_sa(tax_paid)}) outflow.",
    }

    return {
        "id": _make_id("acct12_cfs_tax"),
        "title": "Cash Flow Statement - Taxation Paid Note",
        "topic": "Cash Flow Statement",
        "subskill": "elementary_taxation_paid",
        "mode": "elementary_taxation_paid",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "marks": 4,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "ideal_answer": f"Taxation paid: ({_fmt_sa(tax_paid)}) outflow",
        "sample_answer": f"Opening (R{_fmt_sa(sars_open)}) + Tax expense (R{_fmt_sa(tax_expense)}) - Closing (R{_fmt_sa(sars_close)}) = ({_fmt_sa(tax_paid)})",
        "misconception_tags": [
            "forgot_negative_tax_paid",
            "added_closing_tax_liability",
        ],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_tax_exp", "desc": f"Income tax expense: R{_fmt_sa(tax_expense)}", "marks": 1, "editable": True},
                {"id": "mp_tax_subtot", "desc": f"Total tax obligation subtotal: R{_fmt_sa(sars_open + tax_expense)}", "marks": 1, "editable": True},
                {"id": "mp_tax_close", "desc": f"Closing tax liability deducted: ({_fmt_sa(sars_close)})", "marks": 1, "editable": True},
                {"id": "mp_tax_paid", "desc": f"Taxation paid cash outflow: ({_fmt_sa(tax_paid)})", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "forgot_negative_tax_paid", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Use the SARS (Income Tax) ledger intuition: Opening Liability + Current Expense - Closing Liability = Cash Paid.",
            "tier2_directional_rule": "Paying tax reduces company cash; the final figure in the Cash Flow Statement must be in brackets as an outflow.",
            "tier3_worked_step": f"Taxation paid = R{_fmt_sa(sars_open)} + R{_fmt_sa(tax_expense)} - R{_fmt_sa(sars_close)} = R{_fmt_sa(tax_paid)} outflow -> ({_fmt_sa(tax_paid)}).",
        },
    }


# ============================================================================
# SUB-DRILL 2: Elementary Dividends Paid (4 Marks)
# ============================================================================
def _build_dividends_paid_drill(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    year = r.choice([2024, 2025, 2026])

    # Shareholders for dividends opening: R40k - R120k
    div_open = r.randint(40, 120) * 1000
    # Interim dividend declared and paid: R80k - R220k
    interim_div = r.randint(8, 22) * 10000
    # Final dividend declared at year-end: R90k - R250k
    final_div = r.randint(9, 25) * 10000
    # Shareholders for dividends closing: equals the final dividend declared at year-end!
    div_close = final_div

    # Dividends paid = Opening balance + Interim dividend paid = Opening + Total declared - Closing
    total_declared = interim_div + final_div
    div_paid = div_open + total_declared - div_close  # exactly div_open + interim_div

    prompt = (
        f"You are provided with financial information relating to **{company}** "
        f"for the year ended 28 February {year}.\n\n"
        f"**Information relating to Dividends:**\n"
        f"• Shareholders for dividends on 1 March {year-1} (Opening balance): R{_fmt_sa(div_open)}\n"
        f"• Interim dividend declared and paid during the financial year: R{_fmt_sa(interim_div)}\n"
        f"• Final dividend declared on 28 February {year}: R{_fmt_sa(final_div)}\n"
        f"• Shareholders for dividends on 28 February {year} (Closing balance): R{_fmt_sa(div_close)}\n\n"
        f"**Required:**\n"
        f"Complete the note to calculate the **Dividends paid** in the Cash Flow Statement. "
        f"Indicate cash outflows in brackets."
    )

    headers = ["Dividends Paid Calculation Note", "Amount (R)"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": "Shareholders for dividends at beginning of year", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": _fmt_sa(div_open), "type": "given", "editable": False},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": "Add: Total dividends declared during the year", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": str(total_declared), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": "Subtotal: Total dividend obligation", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": str(div_open + total_declared), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "Less: Shareholders for dividends at end of year", "type": "given", "editable": False},
            {"coordinate": "t0_r3_c1", "value": f"({_fmt_sa(div_close)})", "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r4_c0", "value": "Dividends paid in cash during the year", "type": "given", "editable": False},
            {"coordinate": "t0_r4_c1", "value": f"({_fmt_sa(div_paid)})", "type": "required", "editable": True},
        ],
    ]

    correct_map = {
        "t0_r1_c1": str(total_declared),
        "t0_r2_c1": str(div_open + total_declared),
        "t0_r3_c1": f"({div_close})",
        "t0_r4_c1": f"({div_paid})",
    }

    cell_hints = {
        "t0_r1_c1": f"Total dividends declared = Interim (R{_fmt_sa(interim_div)}) + Final (R{_fmt_sa(final_div)}) = R{_fmt_sa(total_declared)}.",
        "t0_r2_c1": f"Total dividend obligation = Opening payable (R{_fmt_sa(div_open)}) + Total declared (R{_fmt_sa(total_declared)}) = R{_fmt_sa(div_open + total_declared)}.",
        "t0_r3_c1": f"Deduct closing Shareholders for dividends still unpaid: ({_fmt_sa(div_close)}).",
        "t0_r4_c1": f"Dividends paid = Opening balance (R{_fmt_sa(div_open)}) + Interim dividend (R{_fmt_sa(interim_div)}) = ({_fmt_sa(div_paid)}) outflow.",
    }

    return {
        "id": _make_id("acct12_cfs_div"),
        "title": "Cash Flow Statement - Dividends Paid Note",
        "topic": "Cash Flow Statement",
        "subskill": "elementary_dividends_paid",
        "mode": "elementary_dividends_paid",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "marks": 4,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "ideal_answer": f"Dividends paid: ({_fmt_sa(div_paid)}) outflow",
        "sample_answer": f"Opening (R{_fmt_sa(div_open)}) + Declared (R{_fmt_sa(total_declared)}) - Closing (R{_fmt_sa(div_close)}) = ({_fmt_sa(div_paid)})",
        "misconception_tags": [
            "added_instead_of_subtracted_dividends_paid",
            "omitted_interim_dividend",
        ],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_div_decl", "desc": f"Total dividends declared: R{_fmt_sa(total_declared)}", "marks": 1, "editable": True},
                {"id": "mp_div_subtot", "desc": f"Total obligation subtotal: R{_fmt_sa(div_open + total_declared)}", "marks": 1, "editable": True},
                {"id": "mp_div_close", "desc": f"Closing dividends liability deducted: ({_fmt_sa(div_close)})", "marks": 1, "editable": True},
                {"id": "mp_div_paid", "desc": f"Dividends paid cash outflow: ({_fmt_sa(div_paid)})", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "added_instead_of_subtracted_dividends_paid", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Dividends paid = Opening balance of Shareholders for Dividends + Interim dividends paid (or Opening + Declared - Closing).",
            "tier2_directional_rule": "Paying dividends to shareholders is a cash outflow — enter the amount in brackets.",
            "tier3_worked_step": f"Dividends paid = R{_fmt_sa(div_open)} + R{_fmt_sa(interim_div)} = R{_fmt_sa(div_paid)} -> ({_fmt_sa(div_paid)}).",
        },
    }


# ============================================================================
# SUB-DRILL 3: Elementary Net Working Capital Changes (4 Marks)
# ============================================================================
def _build_working_capital_drill(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    year = r.choice([2024, 2025, 2026])

    # Inventory: let it increase (outflow) or decrease (inflow)
    inv_prev = r.randint(40, 75) * 10000
    inv_curr = inv_prev + r.choice([-1, 1]) * r.randint(3, 12) * 10000
    inv_diff = inv_curr - inv_prev
    # Increase in inventory is an OUTFLOW (negative), decrease is an INFLOW (positive)
    inv_effect = -inv_diff

    # Receivables (Debtors): let it change
    rec_prev = r.randint(25, 50) * 10000
    rec_curr = rec_prev + r.choice([-1, 1]) * r.randint(2, 9) * 10000
    rec_diff = rec_curr - rec_prev
    # Increase in receivables is an OUTFLOW (negative), decrease is an INFLOW (positive)
    rec_effect = -rec_diff

    # Payables (Creditors): let it change
    pay_prev = r.randint(20, 45) * 10000
    pay_curr = pay_prev + r.choice([-1, 1]) * r.randint(2, 8) * 10000
    pay_diff = pay_curr - pay_prev
    # Increase in payables is an INFLOW (positive), decrease is an OUTFLOW (negative)
    pay_effect = pay_diff

    net_wc = inv_effect + rec_effect + pay_effect

    prompt = (
        f"You are provided with comparative balance sheet figures for **{company}**.\n\n"
        f"| Balance Sheet Item | 28 Feb {year-1} (R) | 28 Feb {year} (R) |\n"
        f"| :--- | :--- | :--- |\n"
        f"| Inventories (Trading stock) | {_fmt_sa(inv_prev)} | {_fmt_sa(inv_curr)} |\n"
        f"| Trade and other receivables (Trade debtors) | {_fmt_sa(rec_prev)} | {_fmt_sa(rec_curr)} |\n"
        f"| Trade and other payables (Trade creditors) | {_fmt_sa(pay_prev)} | {_fmt_sa(pay_curr)} |\n\n"
        f"**Required:**\n"
        f"Calculate the cash effects of the changes in working capital in the table below. "
        f"Indicate cash outflows in brackets (e.g. (50 000))."
    )

    headers = ["Working Capital Changes", "Cash Effect (R)"]
    rows = [
        [
            {"coordinate": "t0_r0_c0", "value": f"Change in Inventories ({'Increase' if inv_diff > 0 else 'Decrease'})", "type": "given", "editable": False},
            {"coordinate": "t0_r0_c1", "value": _fmt_bracket(inv_effect), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r1_c0", "value": f"Change in Receivables ({'Increase' if rec_diff > 0 else 'Decrease'})", "type": "given", "editable": False},
            {"coordinate": "t0_r1_c1", "value": _fmt_bracket(rec_effect), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r2_c0", "value": f"Change in Payables ({'Increase' if pay_diff > 0 else 'Decrease'})", "type": "given", "editable": False},
            {"coordinate": "t0_r2_c1", "value": _fmt_bracket(pay_effect), "type": "required", "editable": True},
        ],
        [
            {"coordinate": "t0_r3_c0", "value": "NET CHANGE IN WORKING CAPITAL", "type": "given", "editable": False},
            {"coordinate": "t0_r3_c1", "value": _fmt_bracket(net_wc), "type": "required", "editable": True},
        ],
    ]

    correct_map = {
        "t0_r0_c1": f"({abs(inv_effect)})" if inv_effect < 0 else str(inv_effect),
        "t0_r1_c1": f"({abs(rec_effect)})" if rec_effect < 0 else str(rec_effect),
        "t0_r2_c1": f"({abs(pay_effect)})" if pay_effect < 0 else str(pay_effect),
        "t0_r3_c1": f"({abs(net_wc)})" if net_wc < 0 else str(net_wc),
    }

    cell_hints = {
        "t0_r0_c1": f"Inventory {'increased' if inv_diff > 0 else 'decreased'} by R{_fmt_sa(abs(inv_diff))}. An increase uses cash (outflow in brackets); a decrease generates cash.",
        "t0_r1_c1": f"Receivables {'increased' if rec_diff > 0 else 'decreased'} by R{_fmt_sa(abs(rec_diff))}. An increase ties up cash with customers (outflow); a decrease means cash was collected.",
        "t0_r2_c1": f"Payables {'increased' if pay_diff > 0 else 'decreased'} by R{_fmt_sa(abs(pay_diff))}. An increase delays cash payment to suppliers (inflow); a decrease means suppliers were paid (outflow).",
        "t0_r3_c1": f"Net working capital change = Inventories effect ({_fmt_bracket(inv_effect)}) + Receivables effect ({_fmt_bracket(rec_effect)}) + Payables effect ({_fmt_bracket(pay_effect)}) = {_fmt_bracket(net_wc)}.",
    }

    return {
        "id": _make_id("acct12_cfs_wc"),
        "title": "Cash Flow Statement - Working Capital Changes",
        "topic": "Cash Flow Statement",
        "subskill": "elementary_working_capital",
        "mode": "elementary_working_capital",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "marks": 4,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "ideal_answer": f"Net working capital change: {_fmt_bracket(net_wc)}",
        "sample_answer": f"Inventory: {_fmt_bracket(inv_effect)}, Receivables: {_fmt_bracket(rec_effect)}, Payables: {_fmt_bracket(pay_effect)} -> Net: {_fmt_bracket(net_wc)}",
        "misconception_tags": [
            "inverted_working_capital_inventory",
            "inverted_working_capital_receivables",
            "inverted_working_capital_payables",
        ],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_wc_inv", "desc": f"Inventories cash effect: {_fmt_bracket(inv_effect)}", "marks": 1, "editable": True},
                {"id": "mp_wc_rec", "desc": f"Receivables cash effect: {_fmt_bracket(rec_effect)}", "marks": 1, "editable": True},
                {"id": "mp_wc_pay", "desc": f"Payables cash effect: {_fmt_bracket(pay_effect)}", "marks": 1, "editable": True},
                {"id": "mp_wc_net", "desc": f"Net working capital change: {_fmt_bracket(net_wc)}", "marks": 1, "editable": True},
            ],
            "deductions": [
                {"rule": "inverted_working_capital_inventory", "penalty": -1},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier1_location": "Look at the direction of change: Assets increase = Cash Outflow; Liabilities increase = Cash Inflow.",
            "tier2_directional_rule": "Buying more stock or giving credit reduces cash; delaying supplier payments conserves cash.",
            "tier3_worked_step": f"Inventories = {_fmt_bracket(inv_effect)}. Receivables = {_fmt_bracket(rec_effect)}. Payables = {_fmt_bracket(pay_effect)}. Total Net = {_fmt_bracket(net_wc)}.",
        },
    }


# ============================================================================
# EXAM CEILING (MODE: COMPOUND - 15 MARKS): Official NSC Paper 1 Standard
# ============================================================================
def _build_compound_cash_flow_statement(r: random.Random) -> Dict[str, Any]:
    company = _pick_company(r)
    year = r.choice([2024, 2025, 2026])

    # 1. Operating Activities Figures
    # Net profit before tax: R600k - R1.2m
    profit_before_tax = r.randint(60, 120) * 10000
    depreciation = r.randint(40, 90) * 1000
    interest_paid = r.randint(35, 75) * 1000

    operating_profit_before_wc = profit_before_tax + interest_paid + depreciation

    # Working capital movements
    inv_diff = r.randint(15, 45) * 1000  # stock increased
    inv_effect = -inv_diff

    rec_diff = -r.randint(10, 30) * 1000  # debtors decreased (cash collected)
    rec_effect = -rec_diff

    pay_diff = r.randint(12, 35) * 1000  # creditors increased
    pay_effect = pay_diff

    net_wc_change = inv_effect + rec_effect + pay_effect
    cash_generated_from_ops = operating_profit_before_wc + net_wc_change

    # Taxation paid
    sars_open = r.randint(25, 60) * 1000
    tax_expense = int(round(profit_before_tax * 0.28))
    sars_close = r.randint(20, 50) * 1000
    taxation_paid = sars_open + tax_expense - sars_close

    # Dividends paid
    div_open = r.randint(30, 80) * 1000
    interim_div = r.randint(50, 110) * 1000
    final_div = r.randint(60, 130) * 1000
    div_close = final_div
    dividends_paid = div_open + interim_div  # Open + (Interim + Final) - Final

    # Net cash from operating activities
    net_cash_operating = cash_generated_from_ops - interest_paid - taxation_paid - dividends_paid

    # 2. Investing Activities Figures
    # Fixed assets carrying value:
    fa_open = r.randint(20, 40) * 100000
    disposal_carrying_val = r.randint(25, 60) * 1000
    proceeds_disposal = disposal_carrying_val + r.choice([0, 5000, -3000])  # sold near book value
    purchase_fixed_assets = r.randint(18, 45) * 10000

    # Closing carrying value: fa_open + purchase_fixed_assets - depreciation - disposal_carrying_val
    fa_close = fa_open + purchase_fixed_assets - depreciation - disposal_carrying_val

    net_cash_investing = proceeds_disposal - purchase_fixed_assets

    # 3. Financing Activities Figures
    proceeds_shares = r.randint(15, 35) * 10000  # new shares issued
    share_buyback = r.randint(40, 90) * 1000    # repurchase of shares

    loan_open = r.randint(30, 60) * 10000
    # Long term loan repaid: e.g. R80k - R150k
    loan_repaid = r.randint(8, 15) * 10000
    loan_close = loan_open - loan_repaid
    change_borrowings = -loan_repaid  # outflow

    net_cash_financing = proceeds_shares - share_buyback + change_borrowings

    # 4. Net Change in Cash & Cash Equivalents
    net_change_cash = net_cash_operating + net_cash_investing + net_cash_financing
    cash_open = r.randint(15, 55) * 1000
    cash_close = cash_open + net_change_cash

    prompt = (
        f"You are provided with financial information relating to **{company}** for the financial "
        f"year ended 28 February {year}.\n\n"
        f"**1. Extracts from Income Statement for the year ended 28 February {year}:**\n"
        f"• Operating profit before interest: R{_fmt_sa(profit_before_tax + interest_paid)}\n"
        f"• Interest expense: R{_fmt_sa(interest_paid)} (all paid in cash)\n"
        f"• Net profit before tax: R{_fmt_sa(profit_before_tax)}\n"
        f"• Income tax expense: R{_fmt_sa(tax_expense)}\n"
        f"• Depreciation for the year: R{_fmt_sa(depreciation)}\n\n"
        f"**2. Balance Sheet Extracts and Note Movements:**\n"
        f"• Inventories: Increased by R{_fmt_sa(inv_diff)}\n"
        f"• Trade and other receivables: Decreased by R{_fmt_sa(abs(rec_diff))}\n"
        f"• Trade and other payables: Increased by R{_fmt_sa(pay_diff)}\n"
        f"• SARS (Income tax): Opening balance R{_fmt_sa(sars_open)}; Closing balance R{_fmt_sa(sars_close)}\n"
        f"• Shareholders for dividends: Opening balance R{_fmt_sa(div_open)}; Final dividend declared R{_fmt_sa(final_div)}\n"
        f"• Interim dividends paid during the year: R{_fmt_sa(interim_div)}\n"
        f"• Fixed assets: Carrying value on 1 March {year-1} was R{_fmt_sa(fa_open)}; on 28 Feb {year} was R{_fmt_sa(fa_close)}\n"
        f"• Equipment with a carrying value of R{_fmt_sa(disposal_carrying_val)} was sold for R{_fmt_sa(proceeds_disposal)} cash.\n"
        f"• Additions to fixed assets (purchases) were paid for in cash.\n"
        f"• New ordinary shares were issued for R{_fmt_sa(proceeds_shares)} cash.\n"
        f"• The company repurchased ordinary shares from a retiring shareholder for R{_fmt_sa(share_buyback)} cash.\n"
        f"• Long-term borrowings (Nedbank Loan): Opening balance R{_fmt_sa(loan_open)}; Closing balance R{_fmt_sa(loan_close)}.\n"
        f"• Cash and cash equivalents: Opening balance on 1 March {year-1} was R{_fmt_sa(cash_open)}.\n\n"
        f"**Required:**\n"
        f"Complete the **Cash Flow Statement** for the year ended 28 February {year} in accordance with official "
        f"NSC Paper 1 standards. Enter cash outflows in brackets (e.g. (50 000)). "
        f"Section header rows must be left completely empty."
    )

    headers = [f"Cash Flow Statement for the year ended 28 February {year}", "Amount (R)"]

    rows_def = [
        # (Row text, amount_val, is_header, is_required)
        ("CASH FLOW FROM OPERATING ACTIVITIES", "", True, False),
        ("Cash generated from operations", str(cash_generated_from_ops), False, True),
        ("Interest paid", f"({_fmt_sa(interest_paid)})", False, True),
        ("Dividends paid", f"({_fmt_sa(dividends_paid)})", False, True),
        ("Taxation paid", f"({_fmt_sa(taxation_paid)})", False, True),
        ("Net cash flow from operating activities", _fmt_bracket(net_cash_operating), False, True),
        ("CASH FLOW FROM INVESTING ACTIVITIES", "", True, False),
        ("Purchase of fixed assets", f"({_fmt_sa(purchase_fixed_assets)})", False, True),
        ("Proceeds from disposal of fixed assets", str(proceeds_disposal), False, True),
        ("Net cash flow from investing activities", _fmt_bracket(net_cash_investing), False, True),
        ("CASH FLOW FROM FINANCING ACTIVITIES", "", True, False),
        ("Proceeds from new shares issued", str(proceeds_shares), False, True),
        ("Repurchase of shares", f"({_fmt_sa(share_buyback)})", False, True),
        ("Change in long-term borrowings", _fmt_bracket(change_borrowings), False, True),
        ("Net cash flow from financing activities", _fmt_bracket(net_cash_financing), False, True),
        ("Net change in cash and cash equivalents", _fmt_bracket(net_change_cash), False, True),
        ("Cash and cash equivalents at beginning of year", str(cash_open), False, False),  # given
        ("Cash and cash equivalents at end of year", _fmt_bracket(cash_close), False, True),
    ]

    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for rix, (desc, val, is_hdr, is_req) in enumerate(rows_def):
        coord_c0 = f"t0_r{rix}_c0"
        coord_c1 = f"t0_r{rix}_c1"

        if is_hdr:
            c1_type = "must_be_empty"
            c1_val = ""
            correct_map[coord_c1] = ""
            cell_hints[coord_c1] = "Section header row: do NOT enter any amounts here; leave blank."
        elif is_req:
            c1_type = "required"
            c1_val = val
            correct_map[coord_c1] = val.replace(" ", "")
            # Also store formatted version
            cell_hints[coord_c1] = f"{desc} = {val}."
        else:
            c1_type = "given"
            c1_val = val

        rows.append([
            {"coordinate": coord_c0, "value": desc, "type": "given", "editable": False},
            {"coordinate": coord_c1, "value": c1_val if not is_req else "", "type": c1_type, "editable": True if is_req or is_hdr else False},
        ])

    # Refined pedagogical hints for key cells
    cell_hints["t0_r1_c1"] = (
        f"Cash generated from operations = Operating profit (R{_fmt_sa(profit_before_tax + interest_paid)}) "
        f"+ Depreciation (R{_fmt_sa(depreciation)}) + Net working capital changes ({_fmt_bracket(net_wc_change)}) = R{_fmt_sa(cash_generated_from_ops)}."
    )
    cell_hints["t0_r2_c1"] = f"Interest paid = ({_fmt_sa(interest_paid)}) cash outflow."
    cell_hints["t0_r3_c1"] = (
        f"Dividends paid = Opening Shareholders for Dividends (R{_fmt_sa(div_open)}) "
        f"+ Interim dividends (R{_fmt_sa(interim_div)}) = ({_fmt_sa(dividends_paid)}) cash outflow."
    )
    cell_hints["t0_r4_c1"] = (
        f"Taxation paid = Opening SARS (R{_fmt_sa(sars_open)}) + Current tax expense (R{_fmt_sa(tax_expense)}) "
        f"- Closing SARS (R{_fmt_sa(sars_close)}) = ({_fmt_sa(taxation_paid)}) cash outflow."
    )
    cell_hints["t0_r5_c1"] = f"Net cash flow from operating activities = R{_fmt_sa(cash_generated_from_ops)} - R{_fmt_sa(interest_paid)} - R{_fmt_sa(dividends_paid)} - R{_fmt_sa(taxation_paid)} = {_fmt_bracket(net_cash_operating)}."
    cell_hints["t0_r7_c1"] = f"Purchase of fixed assets = Closing (R{_fmt_sa(fa_close)}) - Opening (R{_fmt_sa(fa_open)}) + Depreciation (R{_fmt_sa(depreciation)}) + Disposals (R{_fmt_sa(disposal_carrying_val)}) = ({_fmt_sa(purchase_fixed_assets)}) outflow."
    cell_hints["t0_r8_c1"] = f"Proceeds from disposal of fixed assets = R{_fmt_sa(proceeds_disposal)} cash received (inflow)."
    cell_hints["t0_r9_c1"] = f"Net cash from investing activities = Proceeds (R{_fmt_sa(proceeds_disposal)}) - Purchases ({_fmt_sa(purchase_fixed_assets)}) = {_fmt_bracket(net_cash_investing)}."
    cell_hints["t0_r11_c1"] = f"Proceeds from new shares issued = R{_fmt_sa(proceeds_shares)} cash inflow."
    cell_hints["t0_r12_c1"] = f"Repurchase of shares = ({_fmt_sa(share_buyback)}) cash outflow."
    cell_hints["t0_r13_c1"] = f"Change in borrowings = Closing loan (R{_fmt_sa(loan_close)}) - Opening loan (R{_fmt_sa(loan_open)}) = ({_fmt_sa(loan_repaid)}) outflow."
    cell_hints["t0_r14_c1"] = f"Net cash from financing activities = Shares (R{_fmt_sa(proceeds_shares)}) - Buyback ({_fmt_sa(share_buyback)}) - Loan repayment ({_fmt_sa(loan_repaid)}) = {_fmt_bracket(net_cash_financing)}."
    cell_hints["t0_r15_c1"] = f"Net change in cash = Operating ({_fmt_bracket(net_cash_operating)}) + Investing ({_fmt_bracket(net_cash_investing)}) + Financing ({_fmt_bracket(net_cash_financing)}) = {_fmt_bracket(net_change_cash)}."
    cell_hints["t0_r17_c1"] = f"Cash at end of year = Opening cash (R{_fmt_sa(cash_open)}) + Net change ({_fmt_bracket(net_change_cash)}) = {_fmt_bracket(cash_close)}."

    marking_points = [
        {"id": "mp_cf_ops", "desc": f"Cash generated from operations: R{_fmt_sa(cash_generated_from_ops)}", "marks": 2, "editable": True},
        {"id": "mp_int", "desc": f"Interest paid outflow: ({_fmt_sa(interest_paid)})", "marks": 1, "editable": True},
        {"id": "mp_div", "desc": f"Dividends paid outflow: ({_fmt_sa(dividends_paid)})", "marks": 1, "editable": True},
        {"id": "mp_tax", "desc": f"Taxation paid outflow: ({_fmt_sa(taxation_paid)})", "marks": 1, "editable": True},
        {"id": "mp_net_ops", "desc": f"Net cash flow from operating activities: {_fmt_bracket(net_cash_operating)}", "marks": 1, "editable": True},
        {"id": "mp_fa_purch", "desc": f"Purchase of fixed assets outflow: ({_fmt_sa(purchase_fixed_assets)})", "marks": 1, "editable": True},
        {"id": "mp_fa_disp", "desc": f"Proceeds from disposal of fixed assets: R{_fmt_sa(proceeds_disposal)}", "marks": 1, "editable": True},
        {"id": "mp_net_inv", "desc": f"Net cash flow from investing activities: {_fmt_bracket(net_cash_investing)}", "marks": 1, "editable": True},
        {"id": "mp_shares", "desc": f"Proceeds from shares issued: R{_fmt_sa(proceeds_shares)}", "marks": 1, "editable": True},
        {"id": "mp_buyback", "desc": f"Repurchase of shares outflow: ({_fmt_sa(share_buyback)})", "marks": 1, "editable": True},
        {"id": "mp_loan", "desc": f"Change in long-term borrowings: {_fmt_bracket(change_borrowings)}", "marks": 1, "editable": True},
        {"id": "mp_net_fin", "desc": f"Net cash flow from financing activities: {_fmt_bracket(net_cash_financing)}", "marks": 1, "editable": True},
        {"id": "mp_net_change", "desc": f"Net change in cash and cash equivalents: {_fmt_bracket(net_change_cash)}", "marks": 1, "editable": True},
        {"id": "mp_closing_cash", "desc": f"Closing cash and cash equivalents: {_fmt_bracket(cash_close)}", "marks": 1, "editable": True},
    ]

    marking_schema = {
        "total_marks": 15,
        "marking_points": marking_points,
        "deductions": [
            {"rule": "must_be_empty_filled", "penalty": -1},
            {"rule": "added_instead_of_subtracted_dividends_paid", "penalty": -1},
            {"rule": "forgot_negative_tax_paid", "penalty": -1},
            {"rule": "omitted_fixed_asset_disposal_proceeds", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    return {
        "id": _make_id("acct12_cfs_compound"),
        "title": "Cash Flow Statement (Complete Exam Standard)",
        "topic": "Cash Flow Statement",
        "subskill": "cash_flow_statement",
        "mode": "compound",
        "difficulty": "hard",
        "term": 1,
        "caps_weight_percent": 30,
        "suggested_duration_mins": 25,
        "question_type": "table_completion",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 15,
        "ideal_answer": f"Net change in cash: {_fmt_bracket(net_change_cash)}; Closing cash: {_fmt_bracket(cash_close)}",
        "sample_answer": f"Completed 2D Cash Flow Statement conforming to NSC Paper 1 standard totaling {_fmt_bracket(net_change_cash)} net change.",
        "misconception_tags": [
            "added_instead_of_subtracted_dividends_paid",
            "forgot_negative_tax_paid",
            "inverted_working_capital_inventory",
            "omitted_fixed_asset_disposal_proceeds",
        ],
        "marking_schema": marking_schema,
        "hints": {
            "tier1_location": "Follow the official NSC Paper 1 three-section format: Operating Activities, Investing Activities, and Financing Activities.",
            "tier2_directional_rule": (
                "Show all cash outflows in brackets: Interest paid, Dividends paid, Taxation paid, Fixed assets purchased, "
                "Share repurchased, and Loan repayments. Header rows must be left empty."
            ),
            "tier3_worked_step": (
                f"Net Operating = {_fmt_bracket(net_cash_operating)}. "
                f"Net Investing = {_fmt_bracket(net_cash_investing)}. "
                f"Net Financing = {_fmt_bracket(net_cash_financing)}. "
                f"Net Change = {_fmt_bracket(net_change_cash)}. Closing Cash = {_fmt_bracket(cash_close)}."
            ),
        },
    }


# ============================================================================
# MASTER DISPATCHER
# ============================================================================
BUILDERS = {
    "compound": _build_compound_cash_flow_statement,
    "cash_flow_statement": _build_compound_cash_flow_statement,
    "elementary_taxation_paid": _build_taxation_paid_drill,
    "elementary_dividends_paid": _build_dividends_paid_drill,
    "elementary_working_capital": _build_working_capital_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Accounting Cash Flow Statement questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_cash_flow_statement)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}


def generate_questions(
    subskill: str = "mixed",
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Adapter for compatibility with multi-item registry generators."""
    res = generate(subskill=subskill, difficulty=difficulty, count=count, seed=seed, mode=mode, **kwargs)
    return res["questions"]
