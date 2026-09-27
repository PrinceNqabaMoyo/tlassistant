"""Fundile Learning — Grade 12 Accounting: Budgets & Cash Budget Variance Generator.
NSC Accounting Paper 2 Exam Standard (15-20 marks).
100% deterministic zero-LLM question generator conforming to the 6-Pillar Contract.

Archetypes sourced from curriculum_docs_auto/Accounting_Gr12/Budgets.md:
- Projected Income Statement (sole trader or company): sales, cost of sales, expenses, income, profits
- Cash Budget: receipts, payments, debtors' collection, creditors' payment, cash balances
- Cash Budget Variance Analysis: comparison of budgeted vs actual figures with explanations
- Ethical issues relating to budgeting & projections

Supports compound (15 marks) and elementary sub-drills:
- elementary_projected_income (5 marks)
- elementary_cash_budget (6 marks)
- elementary_variance (4 marks)
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from ..sa_naming_engine import generate_sa_enterprise


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    r.seed(int(seed) if seed is not None else None)
    return r


def _fmt(val: float | int) -> str:
    """Format as SA currency: spaces for thousands, no decimals."""
    rounded = int(round(val))
    return f"{rounded:,}".replace(",", " ")


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _pick_entity(r: random.Random, form: str = "Public Company") -> str:
    ent = generate_sa_enterprise(r, form=form)
    return ent.get("business_name") or "Mandela Trading Ltd"


MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


# --------------------------------------------------------------------------- #
# Sub-drill 1: Projected Income Statement (5 marks)
# --------------------------------------------------------------------------- #
def _build_projected_income(r: random.Random) -> Dict[str, Any]:
    company = _pick_entity(r)
    year = r.choice([2024, 2025, 2026])
    qtr_start = r.choice([0, 3, 6])
    month_names = [MONTHS[qtr_start + i] for i in range(3)]

    # Generate realistic sales figures
    base_sales = r.randint(80, 200) * 10000
    growth_pct = r.choice([5, 8, 10, 12, 15])
    sales = [base_sales]
    for i in range(1, 3):
        sales.append(int(sales[-1] * (1 + growth_pct / 100)))

    markup_pct = r.choice([40, 50, 60, 75, 100])
    cos = [int(s * 100 / (100 + markup_pct)) for s in sales]

    # Operating expenses
    rent = r.randint(8, 20) * 1000
    salaries = r.randint(25, 60) * 1000
    water_elec = r.randint(3, 8) * 1000
    dep = r.randint(2, 6) * 1000
    total_expenses = rent + salaries + water_elec + dep

    gross_profits = [s - c for s, c in zip(sales, cos)]
    net_profits = [gp - total_expenses for gp in gross_profits]

    prompt = (
        f"You are the accountant of **{company}**. Prepare a Projected Income Statement "
        f"for the three months ending {month_names[2]} {year}.\n\n"
        f"**Information:**\n"
        f"• Sales are expected to be R{_fmt(base_sales)} in {month_names[0]} and increase "
        f"by {growth_pct}% each month.\n"
        f"• The business uses a mark-up of {markup_pct}% on cost.\n"
        f"• Monthly operating expenses: Rent R{_fmt(rent)}, Salaries R{_fmt(salaries)}, "
        f"Water & Electricity R{_fmt(water_elec)}, Depreciation R{_fmt(dep)}.\n\n"
        f"**Required:** Complete the Projected Income Statement for {month_names[0]}, "
        f"{month_names[1]}, and {month_names[2]} {year}. Show Net Profit for each month."
    )

    # Build 2D tabular schema
    headers = ["Item"] + month_names
    rows_data = []
    items = ["Sales", "Cost of Sales", "Gross Profit", "Operating Expenses", "Net Profit"]
    values = [sales, cos, gross_profits, [total_expenses]*3, net_profits]

    for rix, (item, vals) in enumerate(zip(items, values)):
        row = [
            {"coordinate": f"t0_r{rix}_c0", "value": item, "type": "given", "editable": False},
        ]
        for cix, v in enumerate(vals, 1):
            cell_type = "required"
            if item == "Operating Expenses":
                cell_type = "given"  # given since it's constant
            row.append({
                "coordinate": f"t0_r{rix}_c{cix}",
                "value": str(v),
                "type": cell_type,
                "editable": cell_type == "required",
            })
        rows_data.append(row)

    correct_map = {}
    marking_points = []
    mp_count = 0
    for rix, (item, vals) in enumerate(zip(items, values)):
        for cix, v in enumerate(vals, 1):
            coord = f"t0_r{rix}_c{cix}"
            if item != "Operating Expenses":
                correct_map[coord] = str(v)
                mp_count += 1
                marking_points.append({
                    "id": f"mp_{mp_count}",
                    "desc": f"{item} — {MONTHS[qtr_start + cix - 1]}",
                    "marks": 1,
                    "editable": True,
                })

    return {
        "id": _make_id("budget_proj_inc"),
        "question_type": "tabular_fill",
        "question_text": prompt,
        "correct_answer": correct_map,
        "sample_answer": f"Net Profit for {month_names[2]}: R{_fmt(net_profits[2])}",
        "table_schema": {"headers": headers, "rows": rows_data},
        "marks": 5,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "learning_objective_id": "acct12_budgets_projected_income",
        "mode": "elementary_projected_income",
        "misconception_tags": ["markup_vs_margin_confusion", "forgot_monthly_growth"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": marking_points[:5],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": f"Check: does sales grow by {growth_pct}% each month?",
            "tier_2": f"Cost of Sales = Sales ÷ (1 + {markup_pct}/100). Mark-up is on cost, not on selling price.",
            "tier_3": f"Month 1 Sales = R{_fmt(sales[0])}, CoS = R{_fmt(cos[0])}, GP = R{_fmt(gross_profits[0])}, "
                      f"NP = R{_fmt(net_profits[0])}.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 2: Cash Budget (6 marks)
# --------------------------------------------------------------------------- #
def _build_cash_budget(r: random.Random) -> Dict[str, Any]:
    company = _pick_entity(r, form="Sole Trader")
    year = r.choice([2024, 2025, 2026])
    qtr_start = r.choice([0, 3, 6])
    month_names = [MONTHS[qtr_start + i] for i in range(3)]

    # Sales
    total_sales = [r.randint(120, 300) * 10000 for _ in range(5)]  # 5 months (2 prior + 3 budget)
    credit_pct = r.choice([30, 40, 50, 60])
    cash_pct = 100 - credit_pct

    # Collection pattern
    same_month_pct = r.choice([30, 40, 50])
    next_month_pct = r.choice([30, 35, 40])
    month_after_pct = r.choice([15, 20, 25])
    bad_debt_pct = 100 - same_month_pct - next_month_pct - month_after_pct

    # Cash receipts for the 3 budget months
    cash_receipts = []
    for m in range(2, 5):  # months index 2,3,4 = budget months
        cash_sales = int(total_sales[m] * cash_pct / 100)
        credit_sales_m = int(total_sales[m] * credit_pct / 100)
        credit_sales_m1 = int(total_sales[m-1] * credit_pct / 100)
        credit_sales_m2 = int(total_sales[m-2] * credit_pct / 100)

        collections = (
            cash_sales
            + int(credit_sales_m * same_month_pct / 100)
            + int(credit_sales_m1 * next_month_pct / 100)
            + int(credit_sales_m2 * month_after_pct / 100)
        )
        cash_receipts.append(collections)

    # Cash payments
    purch_pct = r.choice([50, 55, 60, 65])
    purchases = [int(total_sales[m] * purch_pct / 100) for m in range(2, 5)]
    rent = r.randint(5, 15) * 1000
    wages = r.randint(20, 50) * 1000
    other = r.randint(3, 10) * 1000
    payments = [p + rent + wages + other for p in purchases]

    opening_bal = r.randint(10, 50) * 1000
    net_cash = []
    closing = []
    bal = opening_bal
    for i in range(3):
        net = cash_receipts[i] - payments[i]
        net_cash.append(net)
        bal = bal + net
        closing.append(bal)

    prompt = (
        f"**{company}** prepares a Cash Budget for {month_names[0]} to {month_names[2]} {year}.\n\n"
        f"**Information:**\n"
        f"• Total budgeted sales: "
        + ", ".join(f"{month_names[i]}: R{_fmt(total_sales[i+2])}" for i in range(3)) + "\n"
        f"• Prior months sales: {MONTHS[qtr_start-2]}: R{_fmt(total_sales[0])}, "
        f"{MONTHS[qtr_start-1]}: R{_fmt(total_sales[1])}\n"
        f"• {credit_pct}% of sales are on credit; {cash_pct}% are for cash.\n"
        f"• Credit collection: {same_month_pct}% same month, {next_month_pct}% next month, "
        f"{month_after_pct}% month after, {bad_debt_pct}% bad debts.\n"
        f"• Purchases = {purch_pct}% of sales (all cash). Rent R{_fmt(rent)}/month, "
        f"Wages R{_fmt(wages)}/month, Other R{_fmt(other)}/month.\n"
        f"• Opening bank balance: R{_fmt(opening_bal)}.\n\n"
        f"**Required:** Complete the Cash Budget."
    )

    headers = ["Description"] + month_names
    rows_data = []
    items = ["Cash Receipts", "Cash Payments", "Net Cash Flow", "Opening Balance", "Closing Balance"]
    values = [cash_receipts, payments, net_cash,
              [opening_bal, closing[0], closing[1]], closing]

    for rix, (item, vals) in enumerate(zip(items, values)):
        row = [{"coordinate": f"t0_r{rix}_c0", "value": item, "type": "given", "editable": False}]
        for cix, v in enumerate(vals, 1):
            row.append({
                "coordinate": f"t0_r{rix}_c{cix}",
                "value": str(v),
                "type": "required",
                "editable": True,
            })
        rows_data.append(row)

    correct_map = {}
    for rix, (item, vals) in enumerate(zip(items, values)):
        for cix, v in enumerate(vals, 1):
            correct_map[f"t0_r{rix}_c{cix}"] = str(v)

    return {
        "id": _make_id("budget_cash"),
        "question_type": "tabular_fill",
        "question_text": prompt,
        "correct_answer": correct_map,
        "sample_answer": f"Closing Balance {month_names[2]}: R{_fmt(closing[2])}",
        "table_schema": {"headers": headers, "rows": rows_data},
        "marks": 6,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 10,
        "learning_objective_id": "acct12_budgets_cash_budget",
        "mode": "elementary_cash_budget",
        "misconception_tags": ["forgot_prior_month_collections", "confused_credit_cash_split",
                               "omitted_bad_debts_from_collection"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Cash Receipts calculation (collection schedule)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Cash Payments total", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Net Cash Flow", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Opening and Closing balances", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Look at the collection schedule: which prior months contribute to this month's cash receipts?",
            "tier_2": f"Cash Receipts = Cash Sales ({cash_pct}%) + Collections from credit sales "
                      f"({same_month_pct}% same month + {next_month_pct}% prior month + {month_after_pct}% 2 months prior).",
            "tier_3": f"Month 1 Cash Receipts = R{_fmt(cash_receipts[0])}, Payments = R{_fmt(payments[0])}, "
                      f"Net = R{_fmt(net_cash[0])}, Closing = R{_fmt(closing[0])}.",
        },
    }


# --------------------------------------------------------------------------- #
# Sub-drill 3: Cash Budget Variance Analysis (4 marks)
# --------------------------------------------------------------------------- #
def _build_variance(r: random.Random) -> Dict[str, Any]:
    company = _pick_entity(r)
    year = r.choice([2024, 2025, 2026])
    month = r.choice(MONTHS)

    items = ["Sales", "Cost of Sales", "Rent Expense", "Salaries", "Advertising"]
    budgeted = [r.randint(50, 300) * 10000 for _ in items]
    # Actual with variance
    actual = []
    for b in budgeted:
        var_pct = r.uniform(-15, 15)
        actual.append(int(b * (1 + var_pct / 100)))

    variances = [a - b for a, b in zip(actual, budgeted)]
    fav_unfav = []
    for i, item in enumerate(items):
        v = variances[i]
        if item in ["Sales"]:
            fav_unfav.append("Favourable" if v > 0 else "Unfavourable")
        else:  # expenses
            fav_unfav.append("Favourable" if v < 0 else "Unfavourable")

    prompt = (
        f"**{company}** — Cash Budget Variance Analysis for {month} {year}.\n\n"
        f"Compare the budgeted and actual figures below. For each item, calculate the "
        f"variance and state whether it is Favourable or Unfavourable.\n\n"
        f"| Item | Budgeted (R) | Actual (R) | Variance (R) | Fav/Unfav |\n"
        f"|------|-------------|-----------|-------------|----------|\n"
    )
    for i, item in enumerate(items):
        prompt += f"| {item} | {_fmt(budgeted[i])} | {_fmt(actual[i])} | ? | ? |\n"

    correct_map = {}
    for i, item in enumerate(items):
        correct_map[f"variance_{i}"] = str(variances[i])
        correct_map[f"fav_unfav_{i}"] = fav_unfav[i]

    return {
        "id": _make_id("budget_variance"),
        "question_type": "structured",
        "question_text": prompt,
        "correct_answer": correct_map,
        "sample_answer": f"Sales variance: R{_fmt(variances[0])} ({fav_unfav[0]})",
        "marks": 4,
        "term": 3,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "learning_objective_id": "acct12_budgets_variance",
        "mode": "elementary_variance",
        "misconception_tags": ["confused_fav_unfav_expense", "variance_sign_error",
                               "fav_unfav_income_vs_expense_inversion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct variance calculations", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Correct Fav/Unfav classification", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Variance = Actual − Budgeted. But is higher income good or bad?",
            "tier_2": "For income items (Sales): higher actual = Favourable. For expense items: lower actual = Favourable.",
            "tier_3": f"Sales variance = R{_fmt(actual[0])} − R{_fmt(budgeted[0])} = R{_fmt(variances[0])} ({fav_unfav[0]}).",
        },
    }


# --------------------------------------------------------------------------- #
# COMPOUND: Full Budget Question (15 marks)
# --------------------------------------------------------------------------- #
def _build_compound(r: random.Random) -> List[Dict[str, Any]]:
    return [
        _build_projected_income(r),
        _build_cash_budget(r),
        _build_variance(r),
    ]


# --------------------------------------------------------------------------- #
# PUBLIC API
# --------------------------------------------------------------------------- #
def generate(
    seed: Optional[int] = None,
    count: int = 1,
    mode: str = "compound",
    subskill: str = "mixed",
    difficulty: str = "medium",
    **kwargs,
) -> List[Dict[str, Any]]:
    """Generate Grade 12 Accounting Budget questions.

    Args:
        seed: Deterministic seed for reproducibility.
        count: Number of questions to generate.
        mode: 'compound' | 'elementary_projected_income' | 'elementary_cash_budget' | 'elementary_variance'
        subskill: Ignored (kept for API compatibility).
        difficulty: Ignored (CAPS exam standard throughout).
    """
    r = _rng(seed)
    questions: List[Dict[str, Any]] = []

    builders = {
        "elementary_projected_income": _build_projected_income,
        "elementary_cash_budget": _build_cash_budget,
        "elementary_variance": _build_variance,
    }

    for _ in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = _rng(sub_seed)

        if mode == "compound":
            questions.extend(_build_compound(sub_r))
        elif mode in builders:
            questions.append(builders[mode](sub_r))
        else:
            questions.extend(_build_compound(sub_r))

    return questions
