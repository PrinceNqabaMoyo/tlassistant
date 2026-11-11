"""Subskills 47 to 52: Financial Statements, Budgets & National Economic Data.
Covers small business income-and-expenditure statements, Rand variance analysis,
percentage variance, national budget allocations, fiscal deficit calculations, and multi-month cash flow budgets.
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: Small business monthly Income-and-Expenditure statement: net surplus or deficit."""
    biz_name = r.choice(["Soweto Clean Car Wash", "Dikeledi Hair Salon", "Kagiso Tech Repairs", "Bafana Fast Foods"])
    sales = r.randint(38, 55) * 1000
    commissions = r.randint(2, 6) * 1000
    total_income = sales + commissions

    rent = 8000.00
    wages = 14500.00
    stock_supplies = r.randint(7, 12) * 1000
    utilities = 3200.00
    total_expenditure = round(rent + wages + stock_supplies + utilities, 2)

    net_surplus = round(total_income - total_expenditure, 2)

    d_spec_47 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"{biz_name} Monthly Statement ({_fmt_curr(total_income)})",
        "categories": ["Total Income", "Total Expenditure", "Net Surplus"],
        "series": [
            {"name": "Amount", "values": [total_income, total_expenditure, net_surplus]}
        ],
    }

    prompt = (
        f"Refer to the monthly Income-and-Expenditure statement for {biz_name}:\n\n"
        f"Income:\n"
        f"• Service sales revenue: {_fmt_curr(sales)}\n"
        f"• Additional agency commissions: {_fmt_curr(commissions)}\n\n"
        f"Expenditure:\n"
        f"• Shop rental: {_fmt_curr(rent)}\n"
        f"• Employee wages: {_fmt_curr(wages)}\n"
        f"• Consumable stock & materials: {_fmt_curr(stock_supplies)}\n"
        f"• Water and electricity: {_fmt_curr(utilities)}\n\n"
        f"Calculate the net monthly surplus (profit) for the business."
    )

    correct_ans = _fmt_curr(net_surplus)
    explanation = (
        f"1. Total Income = {_fmt_curr(sales)} + {_fmt_curr(commissions)} = {_fmt_curr(total_income)}.\n"
        f"2. Total Expenditure = {_fmt_curr(rent)} + {_fmt_curr(wages)} + {_fmt_curr(stock_supplies)} + {_fmt_curr(utilities)} = {_fmt_curr(total_expenditure)}.\n"
        f"3. Net Surplus = Total Income ({_fmt_curr(total_income)}) - Total Expenditure ({_fmt_curr(total_expenditure)}) = {_fmt_curr(net_surplus)}."
    )
    t1 = f"Sum the income line items: {_fmt_curr(sales)} + {_fmt_curr(commissions)}."
    t2 = "Sum all four expenditure line items."
    t3 = f"Net Surplus = Total Income - Total Expenditure = {_fmt_curr(net_surplus)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_47",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_47,
    )


def gen_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Budget variance analysis: calculating Rand variance and classifying Favourable/Unfavourable."""
    expense_item = r.choice([
        ("Electricity & Water", 2500.0, 3150.0, "Unfavourable"),
        ("Raw Materials", 8000.0, 7200.0, "Favourable"),
        ("Vehicle Fuel", 4200.0, 4850.0, "Unfavourable"),
        ("Advertising & Promotions", 3000.0, 2450.0, "Favourable"),
    ])
    item_name, budgeted, actual, status = expense_item
    diff = round(abs(actual - budgeted), 2)

    prompt = (
        f"A small business budget review compares budgeted vs actual monthly expenses for '{item_name}':\n"
        f"• Budgeted Expense: {_fmt_curr(budgeted)}\n"
        f"• Actual Expense Incurred: {_fmt_curr(actual)}\n\n"
        f"Calculate the Rand variance and state whether it is Favourable (F) or Unfavourable (U) for the business."
    )

    correct_ans = f"{_fmt_curr(diff)} ({status})"
    custom_opts = [
        f"{_fmt_curr(diff)} (Favourable)",
        f"{_fmt_curr(diff)} (Unfavourable)",
        f"{_fmt_curr(round(diff * 1.15, 2))} (Favourable)",
        f"{_fmt_curr(round(diff * 1.15, 2))} (Unfavourable)",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"1. Absolute variance = |Actual ({_fmt_curr(actual)}) - Budgeted ({_fmt_curr(budgeted)})| = {_fmt_curr(diff)}.\n"
        f"2. For an expense, spending less than budgeted is Favourable; spending more than budgeted is Unfavourable.\n"
        f"3. Since actual expense ({_fmt_curr(actual)}) is {'greater' if actual > budgeted else 'less'} than budgeted ({_fmt_curr(budgeted)}), "
        f"the variance is {status}. Result = {correct_ans}."
    )
    t1 = f"Calculate the difference between actual ({_fmt_curr(actual)}) and budgeted ({_fmt_curr(budgeted)})."
    t2 = "For expenses: Actual < Budgeted is Favourable; Actual > Budgeted is Unfavourable."
    t3 = f"Variance = {correct_ans}."

    return _build_question_payload(
        "gr12_tariffs_subskill_48",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Percentage variance calculation: (Actual - Budgeted) / Budgeted x 100."""
    budgeted = r.choice([15000.0, 20000.0, 25000.0, 30000.0])
    # actual is either higher or lower
    pct_change = r.choice([-12.5, -8.0, 10.5, 15.0, 18.2])
    actual = round(budgeted * (1 + pct_change / 100.0), 2)

    diff = round(actual - budgeted, 2)
    pct_var = round((diff / budgeted) * 100.0, 1)

    prompt = (
        f"A department store budgeted {_fmt_curr(budgeted)} for inventory storage costs.\n"
        f"The actual invoices totaled {_fmt_curr(actual)}.\n\n"
        f"Calculate the percentage variance relative to the budgeted amount (rounded to 1 decimal place)."
    )

    sign_str = "+" if pct_var > 0 else ""
    correct_ans = f"{sign_str}{_fmt(pct_var, 1)}%"
    explanation = (
        f"1. Difference = Actual ({_fmt_curr(actual)}) - Budgeted ({_fmt_curr(budgeted)}) = {_fmt_curr(diff)}.\n"
        f"2. Percentage Variance = (Difference ÷ Budgeted) × 100%\n"
        f"   = ({_fmt_curr(diff)} ÷ {_fmt_curr(budgeted)}) × 100% = {correct_ans}."
    )
    t1 = f"Subtract budgeted ({_fmt_curr(budgeted)}) from actual ({_fmt_curr(actual)})."
    t2 = f"Divide the difference by the original budgeted amount ({_fmt_curr(budgeted)})."
    t3 = f"Multiply by 100%: ({diff} / {budgeted}) × 100% = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_49",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: Interpreting national budget table: percentage allocation to a key sector."""
    total_budget_billion = 2240.0  # R 2,24 trillion
    sector_alloc_billion = r.choice([298.5, 312.4, 345.0, 410.2])  # e.g. Basic Education & Learning
    sector_name = "Basic Education and Culture"

    pct_share = round((sector_alloc_billion / total_budget_billion) * 100.0, 2)

    prompt = (
        f"In the National Budget Speech presented by the Minister of Finance, total consolidated government "
        f"expenditure was budgeted at R {_fmt(total_budget_billion, 1)} billion.\n"
        f"Out of this total, the allocation to '{sector_name}' was set at R {_fmt(sector_alloc_billion, 1)} billion.\n\n"
        f"Calculate the percentage of the total national budget allocated to '{sector_name}' (rounded to 2 decimal places)."
    )

    correct_ans = f"{_fmt(pct_share, 2)}%"
    explanation = (
        f"1. Formula: (Sector Allocation ÷ Total National Expenditure) × 100%.\n"
        f"2. Calculation: (R {_fmt(sector_alloc_billion, 1)} billion ÷ R {_fmt(total_budget_billion, 1)} billion) × 100%.\n"
        f"3. Result: {sector_alloc_billion / total_budget_billion * 100:.4f}% = {correct_ans}."
    )
    t1 = "Divide the sector allocation by total national expenditure."
    t2 = f"Calculate: {sector_alloc_billion} ÷ {total_budget_billion}."
    t3 = f"Multiply by 100: ({sector_alloc_billion} / {total_budget_billion}) × 100% = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_50",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: National budget deficit calculation: revenue vs expenditure and deficit percentage."""
    revenue_billion = 1850.0       # R 1,850 trillion revenue
    expenditure_billion = 2170.0   # R 2,170 trillion expenditure

    deficit_billion = round(expenditure_billion - revenue_billion, 1)  # R 320 billion deficit
    deficit_pct_of_expenditure = round((deficit_billion / expenditure_billion) * 100.0, 1)

    prompt = (
        f"A national Treasury annual economic review reports the following fiscal figures:\n"
        f"• Total Projected Tax & Non-Tax Revenue: R {_fmt(revenue_billion, 1)} billion\n"
        f"• Total Planned National Expenditure: R {_fmt(expenditure_billion, 1)} billion\n\n"
        f"Calculate the national budget deficit (the shortfall that must be financed through government borrowing) in billions of Rands."
    )

    correct_ans = f"R {_fmt(deficit_billion, 1)} billion"
    explanation = (
        f"1. A budget deficit occurs when total expenditure exceeds total revenue.\n"
        f"2. Deficit = Total Planned Expenditure - Total Projected Revenue.\n"
        f"3. Deficit = R {_fmt(expenditure_billion, 1)} billion - R {_fmt(revenue_billion, 1)} billion = {correct_ans}."
    )
    t1 = "Subtract total revenue from total planned expenditure."
    t2 = f"Calculate: {expenditure_billion} - {revenue_billion}."
    t3 = f"Deficit = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_51",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Multi-month cash budget projection: opening balance + cash inflows - cash outflows."""
    opening_balance = r.choice([12000.0, 15000.0, 18500.0])
    month1_in = 32000.0
    month1_out = 28500.0
    month2_in = 35000.0
    month2_out = 39000.0  # cash deficit in month 2

    # Month 1 Closing = Opening + In - Out
    close_m1 = round(opening_balance + month1_in - month1_out, 2)
    # Month 2 Closing = Month 1 Closing + In - Out
    close_m2 = round(close_m1 + month2_in - month2_out, 2)

    prompt = (
        f"A small retail business prepares a two-month cash flow forecast starting with an opening bank balance of {_fmt_curr(opening_balance)}:\n\n"
        f"Month 1:\n"
        f"• Expected Cash Inflows: {_fmt_curr(month1_in)}\n"
        f"• Expected Cash Outflows: {_fmt_curr(month1_out)}\n\n"
        f"Month 2:\n"
        f"• Expected Cash Inflows: {_fmt_curr(month2_in)}\n"
        f"• Expected Cash Outflows: {_fmt_curr(month2_out)}\n\n"
        f"Calculate the projected closing cash balance at the end of Month 2."
    )

    correct_ans = _fmt_curr(close_m2)
    explanation = (
        f"1. Month 1 Closing Balance = Opening Balance ({_fmt_curr(opening_balance)}) + Inflows ({_fmt_curr(month1_in)}) - Outflows ({_fmt_curr(month1_out)})\n"
        f"   = {_fmt_curr(close_m1)}.\n"
        f"2. Month 2 Opening Balance = Month 1 Closing Balance = {_fmt_curr(close_m1)}.\n"
        f"3. Month 2 Closing Balance = {_fmt_curr(close_m1)} + Inflows ({_fmt_curr(month2_in)}) - Outflows ({_fmt_curr(month2_out)})\n"
        f"   = {_fmt_curr(close_m2)}."
    )
    t1 = f"Calculate Month 1 closing balance: {opening_balance} + {month1_in} - {month1_out} = {_fmt_curr(close_m1)}."
    t2 = f"Carry forward {_fmt_curr(close_m1)} as the opening balance for Month 2."
    t3 = f"Calculate Month 2 closing balance: {_fmt_curr(close_m1)} + {month2_in} - {month2_out} = {_fmt_curr(close_m2)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_52",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )
