"""Grade 7 Economic and Management Sciences - Term 2: Budgets (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/EMS_Gr7/Term 2/03. Budgets.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES, get_ems_scenario
from .term2_budgets_archetypes_01_25 import (
    _fmt_r,
    _make_calc,
    _make_ledger,
    _make_mcq,
    _make_typed,
)


def _svg_actual_vs_budget_bars(biz: str, line_item: str, actual: int, budget: int) -> str:
    """Seed-varied grouped Actual vs Budget comparison bars with variance indicator."""
    max_v = max(actual, budget, 1)
    h_b = max(24, int(round((budget / max_v) * 126)))
    h_a = max(24, int(round((actual / max_v) * 126)))
    diff = budget - actual
    status = "Underspend (Favourable)" if diff >= 0 else "Overspend (Unfavourable)"
    a_col = "#16a34a" if diff >= 0 else "#dc2626"
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 228" width="540" height="228">'
        '<rect width="540" height="228" fill="#f8fafc" rx="8"/>'
        f'<text x="270" y="24" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{biz}: {line_item} (Budget vs Actual)</text>'
        '<line x1="65" y1="178" x2="475" y2="178" stroke="#64748b" stroke-width="2"/>'
        f'<rect x="125" y="{178 - h_b}" width="100" height="{h_b}" fill="#0284c7" rx="4"/>'
        f'<text x="175" y="{168 - h_b}" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0369a1">{_fmt_r(budget)}</text>'
        '<text x="175" y="196" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1e293b">Budget (R)</text>'
        f'<rect x="315" y="{178 - h_a}" width="100" height="{h_a}" fill="{a_col}" rx="4"/>'
        f'<text x="365" y="{168 - h_a}" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="{a_col}">{_fmt_r(actual)}</text>'
        '<text x="365" y="196" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1e293b">Actual (R)</text>'
        f'<text x="270" y="216" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#475569">Outcome: {status} | Variance = ?</text>'
        "</svg>"
    )


def _svg_profit_reinvestment(biz: str, np: int, reinv: int, reserve: int, draw: int) -> str:
    """Seed-varied profit allocation visual showing reinvestment, reserve, and owner drawings."""
    w_tot = 440
    w1 = max(55, int(round((reinv / max(np, 1)) * w_tot)))
    w2 = max(55, int(round((reserve / max(np, 1)) * w_tot)))
    w3 = max(45, w_tot - w1 - w2)
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 190" width="540" height="190">'
        '<rect width="540" height="190" fill="#f8fafc" rx="8"/>'
        f'<text x="270" y="24" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{biz}: Budgeted Profit Reinvestment ({_fmt_r(np)})</text>'
        f'<rect x="50" y="56" width="{w1}" height="52" fill="#0284c7" rx="3"/>'
        f'<text x="{50 + w1 // 2}" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#ffffff">Stock {_fmt_r(reinv)}</text>'
        f'<rect x="{50 + w1}" y="56" width="{w2}" height="52" fill="#16a34a" rx="3"/>'
        f'<text x="{50 + w1 + w2 // 2}" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#ffffff">Reserve {_fmt_r(reserve)}</text>'
        f'<rect x="{50 + w1 + w2}" y="56" width="{w3}" height="52" fill="#f59e0b" rx="3"/>'
        f'<text x="{50 + w1 + w2 + w3 // 2}" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#1e293b">Draw ?</text>'
        f'<text x="270" y="138" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#334155">Total Net Profit: {_fmt_r(np)} | Reinvested Stock: {_fmt_r(reinv)} | Cash Reserve: {_fmt_r(reserve)}</text>'
        f'<text x="270" y="160" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#475569">Remaining Owner Drawings = {_fmt_r(draw)}</text>'
        "</svg>"
    )


def build_26_business_budget_framework_vertical_order(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"{sc['entrepreneur']} is preparing the standard annual operating budget framework for {sc['business_type']}. "
        f"Which vertical sequence matches the correct curriculum structure?"
    )
    correct = "Income items -> Total Income (A) -> Expenditure items -> Total Expenditure (B) -> Net Profit / Loss (A - B)"
    distractors = [
        "Personal Assets -> Bank Loans -> Gross Salary -> Municipal Fines",
        "Total Expenditure (B) -> Fixed Capital -> Owner Drawings -> Opening Inventory",
        "Net Profit (A - B) -> Expenditure -> Total Liabilities -> Sales Income (A)",
    ]
    sol = "A formal business budget lists **Income -> Total Income (A) -> Expenditure -> Total Expenditure (B) -> Net Profit or Loss (A - B)**."
    return _make_mcq(
        rng, "26_business_budget_framework_vertical_order", "Business Budget Vertical Framework", prompt,
        correct, distractors, sol,
        "Remember money flowing in (Income A) comes first, outflows (Expenditure B) second, and net profit/loss (A - B) at the bottom.",
        "Follow A - B = Net Profit (if positive) or Net Loss (if negative).",
        ["ems_wrong_budget_framework_order"],
    )


def build_27_business_budget_sections_A_and_B_totals(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    tot_a = rng.randrange(48000, 82000, 2000)
    tot_b = tot_a + rng.randrange(4000, 12000, 1000)
    net_res = tot_a - tot_b
    prompt = (
        f"In {sc['business_type']}'s operating budget, Total Income (A) is {_fmt_r(tot_a)} and Total Expenditure (B) is {_fmt_r(tot_b)}, "
        f"producing A - B = {_fmt_r(net_res)}. What does this negative result indicate?"
    )
    correct = f"A budgeted Net Loss of {_fmt_r(abs(net_res))} because planned expenses exceed expected income."
    distractors = [
        f"A budgeted Net Profit of {_fmt_r(abs(net_res))} available for immediate owner drawings.",
        f"Tax-free capital savings of {_fmt_r(tot_a + tot_b)} held inside a unit trust.",
        "An error proving that businesses cannot prepare budgets before year-end.",
    ]
    sol = f"When A ({_fmt_r(tot_a)}) is less than B ({_fmt_r(tot_b)}), A - B = {_fmt_r(net_res)}, warning managers of a **projected Net Loss** so they can revise prices or costs before trading starts."
    return _make_mcq(
        rng, "27_business_budget_sections_A_and_B_totals", "Interpreting Budget Section A - B", prompt,
        correct, distractors, sol,
        "Check the sign of Total Income (A) minus Total Expenditure (B).",
        "Negative (A - B) means projected costs outweigh expected revenue (Net Loss).",
        ["ems_confuses_net_loss_and_profit"],
    )


def build_28_operating_budget_definition_day_to_day(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Why is the recurring monthly or annual forecast for {sc['business_type']} called an **operating budget** rather than a personal savings jar?"
    )
    correct = "Because it projects ongoing trading revenues (sales/services) and day-to-day running costs like stock, wages, rent, and utilities."
    distractors = [
        "Because it records only once-in-a-lifetime personal wedding gifts.",
        "Because operating budgets forbid any monitoring against actual monthly figures.",
        "Because it lists personal bedroom furniture instead of trading sales or overheads.",
    ]
    sol = "An operating budget tracks expected regular trading inflows and operating expenses needed to keep a business running profitably."
    return _make_mcq(
        rng, "28_operating_budget_definition_day_to_day", "Operating Budget Purpose", prompt,
        correct, distractors, sol,
        "Think about the ongoing operations of trading every month: sales, stock, rent, staff, and water/electricity.",
        "Distinguish business operations from personal household consumption.",
        ["ems_misunderstands_operating_budget"],
    )


def build_29_business_net_profit_or_loss_budget_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sales = rng.randrange(54000, 96000, 3000)
    serv = rng.randrange(6000, 14000, 1000)
    stock = rng.randrange(22000, 36000, 2000)
    wages = rng.randrange(12000, 18000, 1000)
    rent_u = rng.randrange(6000, 10000, 1000)
    tot_a = sales + serv
    tot_b = stock + wages + rent_u
    np = tot_a - tot_b
    prompt = (
        f"{sc['business_type']} budgets monthly Sales {_fmt_r(sales)} and Delivery Fees {_fmt_r(serv)}, with expected Expenditure: "
        f"Stock purchases {_fmt_r(stock)}, Wages {_fmt_r(wages)}, and Rent & Utilities {_fmt_r(rent_u)}. "
        f"Calculate the budgeted **Net Profit (A - B)** (numbers only)."
    )
    sol = (
        f"Total Income (A) = {_fmt_r(sales)} + {_fmt_r(serv)} = {_fmt_r(tot_a)}\n"
        f"Total Expenditure (B) = {_fmt_r(stock)} + {_fmt_r(wages)} + {_fmt_r(rent_u)} = {_fmt_r(tot_b)}\n"
        f"Budgeted Net Profit (A - B) = {_fmt_r(tot_a)} - {_fmt_r(tot_b)} = **{_fmt_r(np)}**"
    )
    return _make_calc(
        rng, "29_business_net_profit_or_loss_budget_calc", "Budgeted Net Profit (A - B)", prompt,
        np, "Net Profit = Total Income (A) - Total Expenditure (B)", sol,
        "Add both income lines to get A, add all three expenditure lines to get B, then compute A - B.",
        f"A = {tot_a}; B = {tot_b}; A - B = {np}.",
        ["ems_business_budget_net_profit_error"], marks=4,
    )


def build_30_three_column_actual_budget_variance_columns(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    yr = rng.choice(["March 2025", "June 2025", "September 2025"])
    prompt = (
        f"When monitoring performance at month-end ({yr}), {sc['business_type']} extends its simple 1-column budget into a 3-column monitoring format. "
        f"Which three numeric columns appear side by side?"
    )
    correct = "Actual (R), Budget (R), and Variance (R)"
    distractors = [
        "Personal Debt (R), Jewellery (R), and Tax Fines (R)",
        "Opening Cash (R), Shares Sold (R), and Birthdays (R)",
        "Assets (R), Liabilities (R), and Net Worth (R)",
    ]
    sol = "Business performance monitoring compares **Actual (R)** results side by side against **Budget (R)** targets to show the **Variance (R)**."
    return _make_mcq(
        rng, "30_three_column_actual_budget_variance_columns", "3-Column Budget Monitoring Format", prompt,
        correct, distractors, sol,
        "What did the business expect to spend, what did it really spend, and what is the difference called?",
        "Actual, Budget, and Variance are the three columns in the Celebrate Catering curriculum layout.",
        ["ems_wrong_3column_budget_headers"],
    )


def build_31_budget_variance_definition_and_monitoring(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    bud = rng.randrange(12000, 24000, 2000)
    act = bud + rng.randrange(1500, 3500, 500)
    prompt = (
        f"{sc['business_type']} budgeted {_fmt_r(bud)} for raw ingredients this month, but actual invoices totalled {_fmt_r(act)}. "
        f"Define **budget variance** and explain why regular variance checking helps business owners."
    )
    mps = [
        "A budget variance is the Rand (or percentage) difference between actual financial results and the budgeted target.",
        f"Identifies favourable or unfavourable gaps early (here {_fmt_r(act - bud)} overspend on ingredients).",
        "Enables managers to spot waste, theft, or supplier price rises early and take corrective action before cash runs out.",
    ]
    sample = (
        f"A **variance** is the difference between actual performance ({_fmt_r(act)}) and the budgeted figure ({_fmt_r(bud)}). "
        "Monitoring variances regularly alerts managers quickly to overspending, supplier hikes, or rising income so budgets and operations stay on track."
    )
    return _make_typed(
        rng, "31_budget_variance_definition_and_monitoring", "Budget Variance Definition & Monitoring", prompt,
        mps, ["variance", "difference", "actual", "budget", "corrective"], sample,
        "Compare what actually happened against the forecast and state why finding gaps early protects cash.",
        "Mention early warning against waste, rising input prices, or unrealistic forecasts.",
        ["ems_fails_to_link_variance_to_control"],
    )


def build_32_unfavourable_expense_overspend_variance_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    bud = rng.randrange(36000, 60000, 4000)
    overspend = rng.randrange(1500, 4500, 500)
    act = bud + overspend
    var = bud - act  # negative = unfavourable overspend
    prompt = (
        f"{sc['business_type']} budgeted {_fmt_r(bud)} for catering ingredients, while actual ingredient spending reached {_fmt_r(act)}. "
        f"Using Budget minus Actual to calculate the **expense variance** (include a minus sign for unfavourable overspending; numbers only)."
    )
    sol = (
        f"Expense Variance = Budget - Actual = {_fmt_r(bud)} - {_fmt_r(act)} = **{_fmt_r(var)}**\n"
        "Because actual costs exceeded budget, this is an **unfavourable (negative)** variance."
    )
    return _make_calc(
        rng, "32_unfavourable_expense_overspend_variance_calc", "Unfavourable Expense Variance Calculation", prompt,
        var, "Expense Variance = Budgeted Expense - Actual Expense", sol,
        "For an expense, spending MORE than budgeted is negative (unfavourable).",
        f"{bud} - {act} = {var}.",
        ["ems_treats_overspend_as_positive_variance"], marks=3,
    )


def build_33_favourable_expense_underspend_variance_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    bud = rng.randrange(8000, 16000, 1000)
    saved = rng.randrange(800, 2200, 200)
    act = bud - saved
    prompt = (
        f"Through energy-saving LEDs, {sc['business_type']} spent only {_fmt_r(act)} on electricity despite budgeting {_fmt_r(bud)}. "
        f"Calculate the positive **favourable expense variance** saved (numbers only)."
    )
    sol = f"Expense Variance = Budget - Actual = {_fmt_r(bud)} - {_fmt_r(act)} = **+{_fmt_r(saved)}** (Favourable saving)."
    return _make_calc(
        rng, "33_favourable_expense_underspend_variance_calc", "Favourable Expense Underspend Calculation", prompt,
        saved, "Expense Variance = Budget - Actual", sol,
        "Spending LESS than budgeted on an expense leaves cash saved (favourable positive variance).",
        f"{bud} - {act} = {saved}.",
        ["ems_expense_underspend_polarity_error"], marks=3,
    )


def build_34_revenue_variance_favourable_vs_unfavourable_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    bud_sales = rng.randrange(45000, 80000, 5000)
    bonus = rng.randrange(3000, 9000, 1500)
    act_sales = bud_sales + bonus
    prompt = (
        f"Remember that for **Income/Sales**, earning MORE than budget is favourable (`Actual - Budget`). "
        f"If {sc['business_type']} budgeted Sales of {_fmt_r(bud_sales)} and achieved actual Sales of {_fmt_r(act_sales)}, "
        f"calculate the positive favourable Sales variance (numbers only)."
    )
    sol = f"Income Variance = Actual Sales - Budgeted Sales = {_fmt_r(act_sales)} - {_fmt_r(bud_sales)} = **+{_fmt_r(bonus)}** (Favourable)."
    return _make_calc(
        rng, "34_revenue_variance_favourable_vs_unfavourable_calc", "Favourable Sales Variance Calculation", prompt,
        bonus, "Income Variance = Actual Income - Budgeted Income", sol,
        "Higher-than-budgeted income improves profit, so Actual - Budget gives a positive favourable variance.",
        f"{act_sales} - {bud_sales} = {bonus}.",
        ["ems_inverts_income_variance_polarity"], marks=3,
    )


def build_35_interpreting_negative_variance_corrective_action(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    neg_v = rng.randrange(2000, 6000, 500)
    prompt = (
        f"At the end of the quarter, {sc['business_type']}'s packaging expense shows a negative variance of -{_fmt_r(neg_v)} "
        f"(actual costs exceeded budget by {_fmt_r(neg_v)}). Suggest two practical corrective actions {sc['entrepreneur']} should take."
    )
    mps = [
        f"Investigate root cause of the {_fmt_r(neg_v)} overspend (supplier price hike, wastage, or higher sales volume needing more boxes).",
        "Negotiate bulk discounts or switch to a more cost-effective supplier, or reduce packaging waste.",
        "If input inflation is permanent and sales stay strong, revise selling prices or adjust next month's budget upward realistically.",
    ]
    sample = (
        f"1. **Cut Waste / Negotiate Suppliers**: Check why packaging ran {_fmt_r(neg_v)} over budget and negotiate bulk rates or trim wastage.\n"
        "2. **Revise Budget or Selling Prices**: If cost increases are permanent (or due to higher sales), adjust selling prices or update future budget allocations."
    )
    return _make_typed(
        rng, "35_interpreting_negative_variance_corrective_action", "Responding to Negative Expense Variance", prompt,
        mps, ["cause", "supplier", "waste", "revise", "price"], sample,
        "Think like a business owner: investigate first, then trim costs or update forecasts/prices.",
        "Don't blindly slash boxes needed for paying customers if higher sales caused the cost jump!",
        ["ems_blind_cost_cutting_error"],
    )


def build_36_actual_vs_budget_variance_bars_visual(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    item = rng.choice(["Fuel & Delivery", "Raw Stock Supplies", "Workshop Electricity"])
    budget = rng.randrange(12000, 24000, 2000)
    actual = budget + rng.randrange(1500, 4500, 500)
    var = budget - actual
    svg = _svg_actual_vs_budget_bars(sc["business_type"], item, actual, budget)
    prompt = (
        f"Examine {sc['business_type']}'s {item} comparison: Budget was {_fmt_r(budget)} and Actual reached {_fmt_r(actual)}. "
        f"Calculate the expense variance (`Budget - Actual`, preserving the minus sign for overspending; numbers only)."
    )
    sol = f"Variance = Budget ({_fmt_r(budget)}) - Actual ({_fmt_r(actual)}) = **{_fmt_r(var)}** (Unfavourable overspend)."
    return _make_calc(
        rng, "36_actual_vs_budget_variance_bars_visual", "Budget vs Actual Comparison Bar Visual", prompt,
        var, "Expense Variance = Budget - Actual", sol,
        "Notice the red Actual bar rises higher than the blue Budget bar — an unfavourable overspend.",
        f"{budget} - {actual} = {var}.",
        ["ems_variance_bar_sign_error"], marks=3,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_37_startup_one_column_business_budget_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sales = rng.randrange(28000, 48000, 2000)
    serv = rng.randrange(4000, 8000, 1000)
    tot_a = sales + serv
    stock = rng.randrange(12000, 18000, 1000)
    rent = rng.randrange(4500, 6500, 500)
    wages = rng.randrange(5000, 7500, 500)
    tot_b = stock + rent + wages
    np = tot_a - tot_b
    headers = ["Business Budget Line Item", "Section", "Budget (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Cash sales", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": "Income", "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": str(sales), "editable": False, "prefilled": True}],
        [{"cell_id": "r1_c0", "value": "Delivery service fees", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": "Income", "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": str(serv), "editable": False, "prefilled": True}],
        [{"cell_id": "r2_c0", "value": "Total Income (A)", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": "Subtotal A", "editable": False, "prefilled": True},
         {"cell_id": "r2_c2", "value": "", "editable": True, "expected": str(tot_a)}],
        [{"cell_id": "r3_c0", "value": "Stock & materials", "editable": False, "prefilled": True},
         {"cell_id": "r3_c1", "value": "Expenditure", "editable": False, "prefilled": True},
         {"cell_id": "r3_c2", "value": str(stock), "editable": False, "prefilled": True}],
        [{"cell_id": "r4_c0", "value": "Shop rent", "editable": False, "prefilled": True},
         {"cell_id": "r4_c1", "value": "Expenditure", "editable": False, "prefilled": True},
         {"cell_id": "r4_c2", "value": str(rent), "editable": False, "prefilled": True}],
        [{"cell_id": "r5_c0", "value": "Staff wages", "editable": False, "prefilled": True},
         {"cell_id": "r5_c1", "value": "Expenditure", "editable": False, "prefilled": True},
         {"cell_id": "r5_c2", "value": str(wages), "editable": False, "prefilled": True}],
        [{"cell_id": "r6_c0", "value": "Total Expenditure (B)", "editable": False, "prefilled": True},
         {"cell_id": "r6_c1", "value": "Subtotal B", "editable": False, "prefilled": True},
         {"cell_id": "r6_c2", "value": "", "editable": True, "expected": str(tot_b)}],
        [{"cell_id": "r7_c0", "value": "Budgeted Net Profit (A - B)", "editable": False, "prefilled": True},
         {"cell_id": "r7_c1", "value": "Bottom Line", "editable": False, "prefilled": True},
         {"cell_id": "r7_c2", "value": "", "editable": True, "expected": str(np)}],
    ]
    cmap = {"r2_c2": str(tot_a), "r6_c2": str(tot_b), "r7_c2": str(np)}
    chints = {
        "r2_c2": "Add Cash sales + Delivery service fees (digits only).",
        "r6_c2": "Add Stock + Shop rent + Staff wages.",
        "r7_c2": "Compute Total Income (A) - Total Expenditure (B).",
    }
    md_memo = (
        f"| Business Budget Line Item | Section | Budget (R) |\n|---|---|---:|\n"
        f"| Cash sales | Income | {sales} |\n| Delivery service fees | Income | {serv} |\n"
        f"| **Total Income (A)** | Subtotal A | **{tot_a}** |\n"
        f"| Stock & materials | Expenditure | {stock} |\n| Shop rent | Expenditure | {rent} |\n| Staff wages | Expenditure | {wages} |\n"
        f"| **Total Expenditure (B)** | Subtotal B | **{tot_b}** |\n| **Budgeted Net Profit (A - B)** | Bottom Line | **{np}** |"
    )
    prompt = f"Complete {sc['business_type']}'s startup Operating Budget below (plain integers without 'R' or spaces)."
    return _make_ledger(
        rng, "37_startup_one_column_business_budget_table", "Startup Operating Budget Table",
        prompt, headers, rows, cmap, chints, md_memo,
        "Calculate Total Income (A) and Total Expenditure (B), then subtract A - B.",
        f"A = {tot_a}; B = {tot_b}; Net Profit = {np}.",
        ["ems_startup_budget_table_error"], marks=6,
    )


def build_38_celebrate_catering_three_column_variance_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    a_sal = rng.randrange(96000, 118000, 2000)
    b_sal = 90000
    v_sal = a_sal - b_sal  # favourable +
    a_ing = 48000 + rng.randrange(1000, 4000, 1000)
    b_ing = 48000
    v_ing = b_ing - a_ing  # negative overspend
    a_tr = 5000
    b_tr = 7000
    v_tr = b_tr - a_tr  # +2000 favourable
    a_tot_exp = a_ing + a_tr
    b_tot_exp = b_ing + b_tr
    a_np = a_sal - a_tot_exp
    b_np = b_sal - b_tot_exp
    v_np = a_np - b_np
    headers = ["Account", "Actual (R)", "Budget (R)", "Variance (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Sales Income", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": str(a_sal), "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": str(b_sal), "editable": False, "prefilled": True},
         {"cell_id": "r0_c3", "value": "", "editable": True, "expected": str(v_sal)}],
        [{"cell_id": "r1_c0", "value": "Ingredients & Supplies (Expense)", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": str(a_ing), "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": str(b_ing), "editable": False, "prefilled": True},
         {"cell_id": "r1_c3", "value": "", "editable": True, "expected": str(v_ing)}],
        [{"cell_id": "r2_c0", "value": "Transport & Delivery (Expense)", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": str(a_tr), "editable": False, "prefilled": True},
         {"cell_id": "r2_c2", "value": str(b_tr), "editable": False, "prefilled": True},
         {"cell_id": "r2_c3", "value": "", "editable": True, "expected": str(v_tr)}],
        [{"cell_id": "r3_c0", "value": "Net Profit (Income - Expenses)", "editable": False, "prefilled": True},
         {"cell_id": "r3_c1", "value": str(a_np), "editable": False, "prefilled": True},
         {"cell_id": "r3_c2", "value": str(b_np), "editable": False, "prefilled": True},
         {"cell_id": "r3_c3", "value": "", "editable": True, "expected": str(v_np)}],
    ]
    cmap = {"r0_c3": str(v_sal), "r1_c3": str(v_ing), "r2_c3": str(v_tr), "r3_c3": str(v_np)}
    chints = {
        "r0_c3": "Income variance = Actual Sales - Budget Sales.",
        "r1_c3": "Expense variance = Budget - Actual (enter negative number for overspend).",
        "r2_c3": "Expense variance = Budget - Actual (positive for saving).",
        "r3_c3": "Net Profit variance = Actual Net Profit - Budget Net Profit.",
    }
    md_memo = (
        f"| Account | Actual (R) | Budget (R) | Variance (R) |\n|---|---:|---:|---:|\n"
        f"| Sales Income | {a_sal} | {b_sal} | **{v_sal}** |\n"
        f"| Ingredients (Expense) | {a_ing} | {b_ing} | **{v_ing}** |\n"
        f"| Transport (Expense) | {a_tr} | {b_tr} | **{v_tr}** |\n"
        f"| **Net Profit** | {a_np} | {b_np} | **{v_np}** |"
    )
    prompt = f"Complete the Variance (R) column for {sc['business_type']}'s 3-column monitoring table below (use '-' before unfavourable overspends; no 'R' or '+' signs)."
    return _make_ledger(
        rng, "38_celebrate_catering_three_column_variance_table", "3-Column Budget Variance Schedule",
        prompt, headers, rows, cmap, chints, md_memo,
        "Remember: Income Variance = Actual - Budget; Expense Variance = Budget - Actual.",
        f"Variances: Sales = {v_sal}, Ingredients = {v_ing}, Transport = {v_tr}, Net Profit = {v_np}.",
        ["ems_3col_variance_sign_error"], marks=8,
    )


def build_39_missing_budget_line_item_reverse_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    tot_b = rng.randrange(28000, 44000, 2000)
    rent = rng.randrange(6000, 10000, 1000)
    wages = rng.randrange(9000, 14000, 1000)
    stock = tot_b - rent - wages
    prompt = (
        f"{sc['business_type']}'s total budgeted expenditure (B) is {_fmt_r(tot_b)}, made up solely of Shop Rent ({_fmt_r(rent)}), "
        f"Wages ({_fmt_r(wages)}), and Stock Purchases. Calculate the missing Stock Purchases budget (numbers only)."
    )
    sol = f"Stock Purchases = Total Expenditure (B) - (Rent + Wages) = {_fmt_r(tot_b)} - ({_fmt_r(rent)} + {_fmt_r(wages)}) = **{_fmt_r(stock)}**"
    return _make_calc(
        rng, "39_missing_budget_line_item_reverse_calc", "Missing Expenditure Line Item", prompt,
        stock, "Missing Line Item = Total Budgeted Expenditure - Known Expenses", sol,
        "Subtract the known expenses from Total Expenditure (B).",
        f"{tot_b} - ({rent} + {wages}) = {stock}.",
        ["ems_reverse_budget_line_error"], marks=3,
    )


def build_40_business_budget_cash_flow_and_reinvestment_role(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    surplus = rng.randrange(15000, 45000, 5000)
    prompt = (
        f"After revising its budget, {sc['business_type']} forecasts an annual surplus of {_fmt_r(surplus)}. "
        f"Explain two ways a structured business budget improves **cash flow management** and **business growth/reinvestment**."
    )
    mps = [
        "Cash flow control: Ensures enough cash is available on time for rent, wages, and supplier invoices during quiet weeks.",
        f"Reinvestment foresight: Shows clearly how much surplus ({_fmt_r(surplus)}) can safely be reinvested into new stock, machinery, or marketing.",
        "Prevents premature profit withdrawals that could starve daily operations of working capital.",
    ]
    sample = (
        "1. **Cash Flow Stability**: Forecasts upcoming bills so the business sets aside cash ahead of quiet trading periods.\n"
        f"2. **Planned Reinvestment**: Quantifies genuine surplus ({_fmt_r(surplus)}) safely available to buy extra stock or expand equipment."
    )
    return _make_typed(
        rng, "40_business_budget_cash_flow_and_reinvestment_role", "Cash Flow & Reinvestment Through Budgets", prompt,
        mps, ["cash flow", "reinvestment", "working capital", "bills", "growth"], sample,
        "Cover both day-to-day bill-paying liquidity AND long-term growth decisions.",
        "Mention preventing over-drawing cash before stock is replenished.",
        ["ems_ignores_cash_flow_role_of_budget"],
    )


def build_41_percentage_budget_variance_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    bud = rng.randrange(8000, 20000, 2000)
    pct = rng.choice([10, 15, 20, 25])
    act = bud + (bud * pct) // 100
    prompt = (
        f"{sc['business_type']} budgeted {_fmt_r(bud)} for fuel delivery, while actual fuel bills reached {_fmt_r(act)}. "
        f"By what percentage (%) did actual fuel spending exceed the budgeted target (numbers only)?"
    )
    sol = f"Percentage Overspend = ({_fmt_r(act - bud)} / {_fmt_r(bud)}) × 100% = **+{pct}%**"
    return _make_calc(
        rng, "41_percentage_budget_variance_calc", "Percentage Budget Variance", prompt,
        pct, "% Variance = ((Actual - Budget) / Budget) × 100", sol,
        "Always divide the Rand variance by the original BUDGET figure, never by Actual.",
        f"{act - bud} / {bud} × 100 = {pct}%.",
        ["ems_divides_by_actual_instead_of_budget"], marks=4, unit="%",
    )


def build_42_multi_revenue_stream_business_budget_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    s1 = rng.randrange(32000, 52000, 2000)
    s2 = rng.randrange(6000, 12000, 1000)
    s3 = rng.randrange(1500, 4500, 500)
    tot_a = s1 + s2 + s3
    tot_b = rng.randrange(24000, 32000, 2000)
    np = tot_a - tot_b
    headers = ["Revenue / Summary Row", "Stream Type", "Budget (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Shop counter sales", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": "Sales", "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": str(s1), "editable": False, "prefilled": True}],
        [{"cell_id": "r1_c0", "value": "Repair service fees", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": "Current Income", "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": str(s2), "editable": False, "prefilled": True}],
        [{"cell_id": "r2_c0", "value": "Sub-tenant storeroom rent", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": "Rent Income", "editable": False, "prefilled": True},
         {"cell_id": "r2_c2", "value": str(s3), "editable": False, "prefilled": True}],
        [{"cell_id": "r3_c0", "value": "Total Income (A)", "editable": False, "prefilled": True},
         {"cell_id": "r3_c1", "value": "Total A", "editable": False, "prefilled": True},
         {"cell_id": "r3_c2", "value": "", "editable": True, "expected": str(tot_a)}],
        [{"cell_id": "r4_c0", "value": "Less: Total Expenditure (B)", "editable": False, "prefilled": True},
         {"cell_id": "r4_c1", "value": "Total B", "editable": False, "prefilled": True},
         {"cell_id": "r4_c2", "value": str(tot_b), "editable": False, "prefilled": True}],
        [{"cell_id": "r5_c0", "value": "Projected Net Profit (A - B)", "editable": False, "prefilled": True},
         {"cell_id": "r5_c1", "value": "Profit", "editable": False, "prefilled": True},
         {"cell_id": "r5_c2", "value": "", "editable": True, "expected": str(np)}],
    ]
    cmap = {"r3_c2": str(tot_a), "r5_c2": str(np)}
    chints = {
        "r3_c2": "Add Sales + Current Income + Rent Income (digits only).",
        "r5_c2": "Subtract Total Expenditure (B) from Total Income (A).",
    }
    md_memo = (
        f"| Revenue / Summary Row | Stream Type | Budget (R) |\n|---|---|---:|\n"
        f"| Shop counter sales | Sales | {s1} |\n| Repair service fees | Current Income | {s2} |\n"
        f"| Sub-tenant rent | Rent Income | {s3} |\n| **Total Income (A)** | Total A | **{tot_a}** |\n"
        f"| Total Expenditure (B) | Total B | {tot_b} |\n| **Projected Net Profit** | Profit | **{np}** |"
    )
    prompt = f"Complete {sc['business_type']}'s multi-stream income budget table below (numbers without 'R' or spaces)."
    return _make_ledger(
        rng, "42_multi_revenue_stream_business_budget_table", "Multi-Stream Business Budget Table",
        prompt, headers, rows, cmap, chints, md_memo,
        "Sum all three revenue streams into Total Income (A) before subtracting Total Expenditure (B).",
        f"Total A = {tot_a}; Net Profit = {np}.",
        ["ems_misses_ancillary_business_income"], marks=6,
    )


def build_43_mixed_variance_polarity_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    s_b, s_a = 50000, rng.randrange(54000, 62000, 2000)
    r_b, r_a = 8000, 8000
    w_b, w_a = 12000, rng.randrange(13500, 16500, 500)
    m_b, m_a = 4000, rng.randrange(2500, 3500, 500)
    headers = ["Budget Line", "Type", "Budget vs Actual", "Favourable, Unfavourable, or Zero"]
    rows_meta = [
        ("Monthly Sales", "Income", f"Budget {_fmt_r(s_b)} vs Actual {_fmt_r(s_a)}", "Favourable"),
        ("Contractual Rent", "Expense", f"Budget {_fmt_r(r_b)} vs Actual {_fmt_r(r_a)}", "Zero"),
        ("Overtime Wages", "Expense", f"Budget {_fmt_r(w_b)} vs Actual {_fmt_r(w_a)}", "Unfavourable"),
        ("Printing Flyers", "Expense", f"Budget {_fmt_r(m_b)} vs Actual {_fmt_r(m_a)}", "Favourable"),
    ]
    rows: List[List[Dict[str, Any]]] = []
    cmap: Dict[str, str] = {}
    chints: Dict[str, str] = {}
    md_lines = [f"| {' | '.join(headers)} |", "|---|---|---|---|"]
    for i, (line, kind, comp, pol) in enumerate(rows_meta):
        cid = f"r{i}_c3"
        cmap[cid] = pol
        chints[cid] = "Enter 'Favourable', 'Unfavourable', or 'Zero'."
        rows.append([
            {"cell_id": f"r{i}_c0", "value": line, "editable": False, "prefilled": True},
            {"cell_id": f"r{i}_c1", "value": kind, "editable": False, "prefilled": True},
            {"cell_id": f"r{i}_c2", "value": comp, "editable": False, "prefilled": True},
            {"cell_id": cid, "value": "", "editable": True, "expected": pol},
        ])
        md_lines.append(f"| {line} | {kind} | {comp} | {pol} |")
    prompt = f"Classify each variance at {sc['business_type']} below as **Favourable**, **Unfavourable**, or **Zero**."
    return _make_ledger(
        rng, "43_mixed_variance_polarity_classification_table", "Variance Polarity Classification Table",
        prompt, headers, rows, cmap, chints, "\n".join(md_lines),
        "Notice Income vs Expense reversal: higher Sales is Favourable, whereas higher Expense is Unfavourable.",
        "Printing cost fell below budget -> Favourable; Overtime wages rose above budget -> Unfavourable.",
        ["ems_confuses_income_and_expense_variance_polarity"], marks=8,
    )


def build_44_net_profit_variance_reconciliation_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    inc_var = rng.randrange(4000, 10000, 1000)   # + favourable income
    exp_var = -rng.randrange(1500, 3500, 500)   # - unfavourable overspend
    np_var = inc_var + exp_var
    prompt = (
        f"{sc['business_type']} records a favourable Sales variance of +{_fmt_r(inc_var)} and an unfavourable Expense variance of -{_fmt_r(abs(exp_var))}. "
        f"Calculate the combined Net Profit variance compared to budget (numbers only)."
    )
    sol = f"Net Profit Variance = (+{_fmt_r(inc_var)}) + (-{_fmt_r(abs(exp_var))}) = **+{_fmt_r(np_var)}** better than budgeted."
    return _make_calc(
        rng, "44_net_profit_variance_reconciliation_calc", "Net Profit Variance Reconciliation", prompt,
        np_var, "Net Profit Variance = Favourable Sales Variance - Expense Overspend", sol,
        "Stronger sales boost profit, while overspending reduces profit.",
        f"{inc_var} - {abs(exp_var)} = {np_var}.",
        ["ems_adds_overspend_to_profit_variance"], marks=3,
    )


def build_45_fixed_vs_variable_business_overhead_budget(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    unit_c = rng.randrange(18, 35, 1)
    q_old = rng.randrange(400, 700, 50)
    q_new = q_old + 200
    fixed_rent = rng.randrange(4000, 7000, 500)
    tot_new = fixed_rent + unit_c * q_new
    prompt = (
        f"In {sc['business_type']}'s operating budget, shop rent stays fixed at {_fmt_r(fixed_rent)}/month, while packaging & stock materials cost "
        f"{_fmt_r(unit_c)} per unit sold. If expected monthly sales rise from {q_old} units to {q_new} units, "
        f"calculate the new total monthly expenditure budget (numbers only)."
    )
    sol = (
        f"Fixed Rent = {_fmt_r(fixed_rent)}\n"
        f"Variable Cost ({q_new} units × {_fmt_r(unit_c)}) = {_fmt_r(unit_c * q_new)}\n"
        f"Total Budgeted Expenditure = {_fmt_r(fixed_rent)} + {_fmt_r(unit_c * q_new)} = **{_fmt_r(tot_new)}**"
    )
    return _make_calc(
        rng, "45_fixed_vs_variable_business_overhead_budget", "Flexible Fixed + Variable Cost Budget", prompt,
        tot_new, "Total Cost = Fixed Rent + (Variable Cost per Unit × New Units)", sol,
        "Remember Fixed Rent does NOT double when unit volume rises, only Variable Unit Costs scale!",
        f"{fixed_rent} + ({unit_c} × {q_new}) = {tot_new}.",
        ["ems_scales_fixed_rent_with_sales_volume"], marks=4,
    )


def build_46_minimum_units_sold_to_balance_budget_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    tot_b = rng.choice([12000, 15000, 18000, 21000, 24000])
    price = rng.choice([50, 60, 75, 100])
    units = tot_b // price
    prompt = (
        f"{sc['business_type']} projects Total Expenditure (B) of {_fmt_r(tot_b)} for next month and sells each {sc['item_sold']} box at {_fmt_r(price)}. "
        f"How many boxes must be sold just to cover Total Expenditure (A = B) without a loss (numbers only)?"
    )
    sol = f"Minimum Boxes Required = Total Budgeted Expenditure / Price per Box = {_fmt_r(tot_b)} / {_fmt_r(price)} = **{units} boxes**"
    return _make_calc(
        rng, "46_minimum_units_sold_to_balance_budget_calc", "Units Needed to Balance Budget", prompt,
        units, "Units = Total Budgeted Expenditure ÷ Selling Price per Unit", sol,
        "Divide Total Expenditure (B) by the Rand selling price per box.",
        f"{tot_b} ÷ {price} = {units}.",
        ["ems_multiplies_price_and_expenditure"], marks=3, unit="units",
    )


def build_47_two_month_projected_operating_budget_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    m1_i = rng.randrange(30000, 44000, 2000)
    m1_e = rng.randrange(22000, 28000, 2000)
    m1_p = m1_i - m1_e
    m2_i = m1_i + 4000
    m2_e = m1_e + 2000
    m2_p = m2_i - m2_e
    tot_p = m1_p + m2_p
    headers = ["Budget Row", "Month 1 (R)", "Month 2 (R)", "2-Month Total (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Budgeted Income (A)", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": str(m1_i), "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": str(m2_i), "editable": False, "prefilled": True},
         {"cell_id": "r0_c3", "value": "", "editable": True, "expected": str(m1_i + m2_i)}],
        [{"cell_id": "r1_c0", "value": "Budgeted Expenditure (B)", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": str(m1_e), "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": str(m2_e), "editable": False, "prefilled": True},
         {"cell_id": "r1_c3", "value": "", "editable": True, "expected": str(m1_e + m2_e)}],
        [{"cell_id": "r2_c0", "value": "Net Profit (A - B)", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": "", "editable": True, "expected": str(m1_p)},
         {"cell_id": "r2_c2", "value": "", "editable": True, "expected": str(m2_p)},
         {"cell_id": "r2_c3", "value": "", "editable": True, "expected": str(tot_p)}],
    ]
    cmap = {
        "r0_c3": str(m1_i + m2_i),
        "r1_c3": str(m1_e + m2_e),
        "r2_c1": str(m1_p),
        "r2_c2": str(m2_p),
        "r2_c3": str(tot_p),
    }
    chints = {
        "r0_c3": "Add Month 1 + Month 2 Income.",
        "r1_c3": "Add Month 1 + Month 2 Expenditure.",
        "r2_c1": "Month 1 Income - Month 1 Expenditure.",
        "r2_c2": "Month 2 Income - Month 2 Expenditure.",
        "r2_c3": "Add Month 1 + Month 2 Net Profit (matches 2-Month Income - 2-Month Expenditure).",
    }
    md_memo = (
        f"| Budget Row | Month 1 (R) | Month 2 (R) | 2-Month Total (R) |\n|---|---:|---:|---:|\n"
        f"| Income (A) | {m1_i} | {m2_i} | **{m1_i + m2_i}** |\n"
        f"| Expenditure (B) | {m1_e} | {m2_e} | **{m1_e + m2_e}** |\n"
        f"| **Net Profit (A - B)** | **{m1_p}** | **{m2_p}** | **{tot_p}** |"
    )
    prompt = f"Complete {sc['business_type']}'s 2-month operating budget projection table below (digits only, no 'R' or spaces)."
    return _make_ledger(
        rng, "47_two_month_projected_operating_budget_table", "2-Month Projected Operating Budget",
        prompt, headers, rows, cmap, chints, md_memo,
        "Cross-check horizontally (Month 1 + Month 2 = Total) and vertically (Income - Expenditure = Net Profit).",
        f"M1 NP = {m1_p}, M2 NP = {m2_p}, Combined NP = {tot_p}.",
        ["ems_2month_crossfoot_budget_error"], marks=8,
    )


def build_48_profit_reinvestment_allocation_visual(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    np = rng.randrange(20000, 44000, 4000)
    reinv = int(np * 0.5)
    reserve = int(np * 0.25)
    draw = np - reinv - reserve
    svg = _svg_profit_reinvestment(sc["business_type"], np, reinv, reserve, draw)
    prompt = (
        f"{sc['business_type']} budgets an annual Net Profit of {_fmt_r(np)}. {sc['entrepreneur']} allocates {_fmt_r(reinv)} for extra Stock "
        f"and {_fmt_r(reserve)} into a Business Cash Reserve. Calculate the remaining Owner Drawings allocation (numbers only)."
    )
    sol = f"Remaining Owner Drawings = {_fmt_r(np)} - ({_fmt_r(reinv)} + {_fmt_r(reserve)}) = **{_fmt_r(draw)}**."
    return _make_calc(
        rng, "48_profit_reinvestment_allocation_visual", "Profit Reinvestment & Reserve Allocation", prompt,
        draw, "Drawings = Net Profit - (Reinvested Stock + Cash Reserve)", sol,
        "Subtract both reinvested stock and emergency business reserves from Total Net Profit.",
        f"{np} - ({reinv} + {reserve}) = {draw}.",
        ["ems_reinvestment_subtraction_error"], marks=3,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_49_case_study_variance_turnaround_evaluation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    loss = rng.randrange(1800, 4200, 300)
    prompt = (
        f"During Term 2 in {sc['area']}, {sc['business_type']} made an unplanned -{_fmt_r(loss)} loss because electricity bills spiked, "
        f"perishable stock spoiled, and {sc['entrepreneur']} drew random cash daily without tracking. "
        f"Design a three-point turnaround using EMS budgeting principles."
    )
    mps = [
        "Draw up a 3-column monitoring budget (Actual vs Budget vs Variance) reviewed monthly.",
        "Address negative cost variances directly: buy smaller frequent batches of perishable stock to curb spoilage and conserve electricity.",
        "Set a fixed monthly owner salary/drawing limit instead of unplanned cash withdrawals.",
    ]
    sample = (
        "1. **Track Variances Monthly**: Compare Actual vs Budget to spot negative spikes immediately.\n"
        f"2. **Cut Spoilage & Overheads**: Buy perishable goods closer to demand and control energy use to reverse the -{_fmt_r(loss)} loss.\n"
        f"3. **Cap Drawings**: Pay {sc['entrepreneur']} a fixed budgeted allowance instead of random cash till withdrawals."
    )
    return _make_typed(
        rng, "49_case_study_variance_turnaround_evaluation", "Case Study: Budget Turnaround Plan", prompt,
        mps, ["variance", "spoilage", "drawings", "monitor", "overheads"], sample,
        "Match one targeted budgeting solution to each of the three mistakes mentioned in the scenario.",
        "Include variance tracking, stock spoilage control, and fixed owner drawings.",
        ["ems_vague_turnaround_advice"],
    )


def build_50_capstone_business_three_column_budget_variance_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    b_sales = rng.randrange(70000, 95000, 5000)
    a_sales = b_sales + rng.randrange(4000, 8000, 2000)
    b_rent = 8000
    a_rent = 8000
    b_stock = rng.randrange(32000, 42000, 2000)
    a_stock = b_stock + 2500
    b_tot_e = b_rent + b_stock
    a_tot_e = a_rent + a_stock
    b_np = b_sales - b_tot_e
    a_np = a_sales - a_tot_e
    v_sales = a_sales - b_sales
    v_stock = b_stock - a_stock  # -2500
    v_np = a_np - b_np
    headers = ["Operating Budget Item", "Actual (R)", "Budget (R)", "Variance (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Total Income (A): Sales", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": str(a_sales), "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": str(b_sales), "editable": False, "prefilled": True},
         {"cell_id": "r0_c3", "value": "", "editable": True, "expected": str(v_sales)}],
        [{"cell_id": "r1_c0", "value": "Shop Rent (Expense)", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": str(a_rent), "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": str(b_rent), "editable": False, "prefilled": True},
         {"cell_id": "r1_c3", "value": "0", "editable": False, "prefilled": True}],
        [{"cell_id": "r2_c0", "value": "Stock Purchases (Expense)", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": str(a_stock), "editable": False, "prefilled": True},
         {"cell_id": "r2_c2", "value": str(b_stock), "editable": False, "prefilled": True},
         {"cell_id": "r2_c3", "value": "", "editable": True, "expected": str(v_stock)}],
        [{"cell_id": "r3_c0", "value": "Total Expenditure (B)", "editable": False, "prefilled": True},
         {"cell_id": "r3_c1", "value": "", "editable": True, "expected": str(a_tot_e)},
         {"cell_id": "r3_c2", "value": "", "editable": True, "expected": str(b_tot_e)},
         {"cell_id": "r3_c3", "value": str(v_stock), "editable": False, "prefilled": True}],
        [{"cell_id": "r4_c0", "value": "Net Profit (A - B)", "editable": False, "prefilled": True},
         {"cell_id": "r4_c1", "value": "", "editable": True, "expected": str(a_np)},
         {"cell_id": "r4_c2", "value": "", "editable": True, "expected": str(b_np)},
         {"cell_id": "r4_c3", "value": "", "editable": True, "expected": str(v_np)}],
    ]
    cmap = {
        "r0_c3": str(v_sales),
        "r2_c3": str(v_stock),
        "r3_c1": str(a_tot_e),
        "r3_c2": str(b_tot_e),
        "r4_c1": str(a_np),
        "r4_c2": str(b_np),
        "r4_c3": str(v_np),
    }
    chints = {
        "r0_c3": "Sales variance = Actual - Budget.",
        "r2_c3": "Expense variance = Budget - Actual (enter -2500).",
        "r3_c1": "Actual Rent + Actual Stock.",
        "r3_c2": "Budget Rent + Budget Stock.",
        "r4_c1": "Actual Income - Actual Expenditure.",
        "r4_c2": "Budget Income - Budget Expenditure.",
        "r4_c3": "Actual Net Profit - Budget Net Profit.",
    }
    md_memo = (
        f"| Operating Budget Item | Actual (R) | Budget (R) | Variance (R) |\n|---|---:|---:|---:|\n"
        f"| Total Income (A): Sales | {a_sales} | {b_sales} | **{v_sales}** |\n"
        f"| Shop Rent | {a_rent} | {b_rent} | 0 |\n"
        f"| Stock Purchases | {a_stock} | {b_stock} | **{v_stock}** |\n"
        f"| Total Expenditure (B) | **{a_tot_e}** | **{b_tot_e}** | {v_stock} |\n"
        f"| **Net Profit (A - B)** | **{a_np}** | **{b_np}** | **{v_np}** |"
    )
    prompt = f"Complete {sc['business_type']}'s capstone 3-column Business Operating Budget & Variance table below (digits only; '-' for negative)."
    return _make_ledger(
        rng, "50_capstone_business_three_column_budget_variance_table", "Capstone 3-Column Business Budget Table",
        prompt, headers, rows, cmap, chints, md_memo,
        "Compute column totals B first, then Net Profit (A - B), then reconcile variances.",
        f"Actual NP = {a_np}; Budget NP = {b_np}; Net Profit Variance = {v_np}.",
        ["ems_capstone_budget_variance_error"], marks=10,
    )


BUILDERS_26_50 = {
    "26_business_budget_framework_vertical_order": build_26_business_budget_framework_vertical_order,
    "27_business_budget_sections_A_and_B_totals": build_27_business_budget_sections_A_and_B_totals,
    "28_operating_budget_definition_day_to_day": build_28_operating_budget_definition_day_to_day,
    "29_business_net_profit_or_loss_budget_calc": build_29_business_net_profit_or_loss_budget_calc,
    "30_three_column_actual_budget_variance_columns": build_30_three_column_actual_budget_variance_columns,
    "31_budget_variance_definition_and_monitoring": build_31_budget_variance_definition_and_monitoring,
    "32_unfavourable_expense_overspend_variance_calc": build_32_unfavourable_expense_overspend_variance_calc,
    "33_favourable_expense_underspend_variance_calc": build_33_favourable_expense_underspend_variance_calc,
    "34_revenue_variance_favourable_vs_unfavourable_calc": build_34_revenue_variance_favourable_vs_unfavourable_calc,
    "35_interpreting_negative_variance_corrective_action": build_35_interpreting_negative_variance_corrective_action,
    "36_actual_vs_budget_variance_bars_visual": build_36_actual_vs_budget_variance_bars_visual,
    "37_startup_one_column_business_budget_table": build_37_startup_one_column_business_budget_table,
    "38_celebrate_catering_three_column_variance_table": build_38_celebrate_catering_three_column_variance_table,
    "39_missing_budget_line_item_reverse_calc": build_39_missing_budget_line_item_reverse_calc,
    "40_business_budget_cash_flow_and_reinvestment_role": build_40_business_budget_cash_flow_and_reinvestment_role,
    "41_percentage_budget_variance_calc": build_41_percentage_budget_variance_calc,
    "42_multi_revenue_stream_business_budget_table": build_42_multi_revenue_stream_business_budget_table,
    "43_mixed_variance_polarity_classification_table": build_43_mixed_variance_polarity_classification_table,
    "44_net_profit_variance_reconciliation_calc": build_44_net_profit_variance_reconciliation_calc,
    "45_fixed_vs_variable_business_overhead_budget": build_45_fixed_vs_variable_business_overhead_budget,
    "46_minimum_units_sold_to_balance_budget_calc": build_46_minimum_units_sold_to_balance_budget_calc,
    "47_two_month_projected_operating_budget_table": build_47_two_month_projected_operating_budget_table,
    "48_profit_reinvestment_allocation_visual": build_48_profit_reinvestment_allocation_visual,
    "49_case_study_variance_turnaround_evaluation": build_49_case_study_variance_turnaround_evaluation,
    "50_capstone_business_three_column_budget_variance_table": build_50_capstone_business_three_column_budget_variance_table,
}
