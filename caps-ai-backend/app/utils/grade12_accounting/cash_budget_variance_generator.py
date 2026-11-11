"""
Grade 12 Accounting: Cash Budget Variance Analysis (Companies)
Strictly aligned with South African National Curriculum Standards for Grade 12 Accounting (Term 3).
Dedicated generator for Budget vs Actual Variance Calculations, Percentage Variances,
Sales & Collection Strategy Evaluation, Expense Overrun Investigation, and Projected Income Statement Variances.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "cash_receipts_variance_table",
    "cash_payments_variance_table",
    "projected_income_statement_variance_analysis",
    "sales_policy_and_delivery_expense_variance_evaluation",
    "capital_expenditure_and_loan_variance_analysis",
]

COMPANIES = [
    "Protea Retailers Ltd",
    "Highveld Appliances Ltd",
    "Ubuntu Distributors Ltd",
    "Zululand Furnishers Ltd",
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_cash_receipts_variance(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    b_cash = 200000
    a_cash = 230000
    var_cash_pct = round(((a_cash - b_cash) / b_cash) * 100, 1)

    b_debt = 150000
    a_debt = 120000
    var_debt_pct = round(((b_debt - a_debt) / b_debt) * 100, 1)

    headers = ["Cash Receipts Item", "Budgeted (R)", "Actual (R)", "Variance (positive R)", "Variance (%)", "Favourable / Unfavourable"]
    rows = [
        ["Cash sales", f"R{b_cash:,}", f"R{a_cash:,}", "{r0_c3}", f"{var_cash_pct}%", "{r0_c5}"],
        ["Collections from debtors", f"R{b_debt:,}", f"R{a_debt:,}", "{r1_c3}", "{r1_c4}", "{r1_c5}"],
    ]
    correct_map = {
        "r0_c3": a_cash - b_cash,
        "r0_c5": "Favourable",
        "r1_c3": b_debt - a_debt,
        "r1_c4": var_debt_pct,
        "r1_c5": "Unfavourable",
    }
    worked = (
        f"**Cash Receipts Variance Analysis ({co})**\n\n"
        f"- **Cash sales**: `R{a_cash:,} - R{b_cash:,} = R{a_cash - b_cash:,}` (`+{var_cash_pct}%`, **Favourable**).\n"
        f"- **Collections from debtors**: `R{b_debt:,} - R{a_debt:,} = R{b_debt - a_debt:,}` (`-{var_debt_pct}%`, **Unfavourable**)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "cash_receipts_variance_table",
        "question_text": f"Complete the **Cash Receipts Variance Analysis** schedule for **{co}**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Percentage variance is calculated as `(Difference ÷ Budgeted Amount) × 100`.",
            "Higher actual cash receipts than budgeted are Favourable; lower actual collections from debtors are Unfavourable.",
            worked,
        ),
    }


def _gen_cash_payments_variance(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    b_adv = 40000
    a_adv = 52000
    pct_adv = round(((a_adv - b_adv) / b_adv) * 100, 1)

    b_pack = 25000
    a_pack = 21250
    pct_pack = round(((b_pack - a_pack) / b_pack) * 100, 1)

    headers = ["Cash Payments Item", "Budgeted (R)", "Actual (R)", "Variance (positive R)", "Variance (%)", "Favourable / Unfavourable"]
    rows = [
        ["Advertising & marketing", f"R{b_adv:,}", f"R{a_adv:,}", "{r0_c3}", "{r0_c4}", "{r0_c5}"],
        ["Packing materials", f"R{b_pack:,}", f"R{a_pack:,}", "{r1_c3}", f"{pct_pack}%", "{r1_c5}"],
    ]
    correct_map = {
        "r0_c3": a_adv - b_adv,
        "r0_c4": pct_adv,
        "r0_c5": "Unfavourable",
        "r1_c3": b_pack - a_pack,
        "r1_c5": "Favourable",
    }
    worked = (
        f"**Cash Payments Variance Analysis ({co})**\n\n"
        f"- **Advertising**: Overspent by `R{a_adv - b_adv:,}` (`{pct_adv}%` above budget $\\rightarrow$ **Unfavourable**).\n"
        f"- **Packing materials**: Saved `R{b_pack - a_pack:,}` (`{pct_pack}%` below budget $\\rightarrow$ **Favourable**)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "cash_payments_variance_table",
        "question_text": f"Complete the **Cash Payments Variance Analysis** table for **{co}**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "For expenses/payments, spending more than budgeted is Unfavourable; spending less than budgeted is Favourable.",
            "Divide the Rand variance by the Budgeted figure and multiply by 100 to find the percentage variance.",
            worked,
        ),
    }


def _gen_pis_variance_analysis(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    b_sales = 500000
    a_sales = 550000
    b_cos = 300000
    a_cos = 352000
    b_gp = b_sales - b_cos
    a_gp = a_sales - a_cos

    headers = ["Projected Income Statement Item", "Budgeted (R)", "Actual (R)", "Variance (positive R)", "Favourable / Unfavourable"]
    rows = [
        ["Sales", f"R{b_sales:,}", f"R{a_sales:,}", "{r0_c3}", "{r0_c4}"],
        ["Cost of sales", f"(R{b_cos:,})", f"(R{a_cos:,})", "{r1_c3}", "{r1_c4}"],
        ["Gross profit", f"R{b_gp:,}", "{r2_c2}", "{r2_c3}", "{r2_c4}"],
    ]
    correct_map = {
        "r0_c3": a_sales - b_sales,
        "r0_c4": "Favourable",
        "r1_c3": a_cos - b_cos,
        "r1_c4": "Unfavourable",
        "r2_c2": a_gp,
        "r2_c3": b_gp - a_gp,
        "r2_c4": "Unfavourable",
    }
    worked = (
        f"**Projected Income Statement Variance Analysis ({co})**\n\n"
        f"- **Sales**: `R{a_sales:,} - R{b_sales:,} = R{a_sales - b_sales:,}` (**Favourable** — turnover increased by 10%).\n"
        f"- **Cost of sales**: `R{a_cos:,} - R{b_cos:,} = R{a_cos - b_cos:,}` (**Unfavourable** — rose faster than sales because trade discounts were granted).\n"
        f"- **Actual Gross Profit**: `R{a_sales:,} - R{a_cos:,} = R{a_gp:,}`, which is `R{b_gp - a_gp:,}` below the budgeted Gross Profit of `R{b_gp:,}` (**Unfavourable**)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "projected_income_statement_variance_analysis",
        "question_text": (
            f"**{co}** reduced its mark-up percentage to boost sales volume. Complete the **Projected Income Statement Variance** table."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 7,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Even if Actual Sales exceed Budgeted Sales, a sharp drop in mark-up % can cause Actual Gross Profit to fall below Budgeted Gross Profit.",
            "Calculate Actual Gross Profit first (`R550,000 - R352,000`), then compare it with Budgeted Gross Profit (`R200,000`).",
            worked,
        ),
    }


def _gen_strategy_variance_evaluation(r: random.Random) -> Dict[str, Any]:
    headers = ["Observed Variance Pattern", "Budgeted (R)", "Actual (R)", "Root Cause Diagnosis (Free Delivery Policy Boosted Credit Sales / Commission Cut Reduced Sales Effort / Unplanned Tariff Hike)"]
    rows = [
        ["Credit sales rose by 25% while Delivery Expenses rose by 30%", "R400,000", "R500,000", "{r0_c3}"],
        ["Salesperson commission fell by 40% and Cash Sales dropped by 35%", "R60,000", "R36,000", "{r1_c3}"],
        ["Water and electricity rose by 22% despite unchanged store hours", "R18,000", "R21,960", "{r2_c3}"],
    ]
    correct_map = {
        "r0_c3": "Free Delivery Policy Boosted Credit Sales",
        "r1_c3": "Commission Cut Reduced Sales Effort",
        "r2_c3": "Unplanned Tariff Hike",
    }
    worked = (
        "**Linked Operational Variance Diagnosis**\n\n"
        "- **Credit sales +25% & Delivery expenses +30%**: **Free Delivery Policy Boosted Credit Sales** (justifying the higher delivery cost).\n"
        "- **Commission -40% & Cash sales -35%**: **Commission Cut Reduced Sales Effort**.\n"
        "- **Utilities +22%**: **Unplanned Tariff Hike**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "sales_policy_and_delivery_expense_variance_evaluation",
        "question_text": "Link each observed budget variance pattern to its underlying operational cause.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "In Grade 12 variance interpretation, expense variances must be evaluated in relation to linked revenue items (e.g. Delivery Expenses vs Sales).",
            "Match each scenario to the correct diagnosis from the column header.",
            worked,
        ),
    }


def _gen_capex_and_loan_variance(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    b_loan_int = 12000
    a_loan_int = 9000
    int_rate = 12
    loan_repaid = 300000

    headers = ["Financing & Capital Variance Item", "Calculation", "Amount (R)"]
    rows = [
        [f"Monthly interest before loan repayment (R{b_loan_int:,} at {int_rate}% p.a.) — Opening Loan Balance", "R12,000 × 12 ÷ 0.12", "{r0_c2}"],
        [f"Monthly interest after loan repayment (R{a_loan_int:,} at {int_rate}% p.a.) — Closing Loan Balance", "R9,000 × 12 ÷ 0.12", "{r1_c2}"],
        ["Capital portion of loan repaid at the start of the month", "Opening Loan - Closing Loan", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c2": 1200000,
        "r1_c2": 900000,
        "r2_c2": loan_repaid,
    }
    worked = (
        f"**Loan & Interest Variance Back-Calculation ({co})**\n\n"
        f"- **Opening Loan Balance**: `R12,000 × 12 ÷ 12% = R1,200,000`\n"
        f"- **Closing Loan Balance**: `R9,000 × 12 ÷ 12% = R900,000`\n"
        f"- **Loan Capital Repaid**: `R1,200,000 - R900,000 = R300,000`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "capital_expenditure_and_loan_variance_analysis",
        "question_text": (
            f"**{co}** budgeted **R{b_loan_int:,}** for monthly loan interest (at **12% p.a.**), but actual monthly interest "
            f"dropped to **R{a_loan_int:,}** after an unbudgeted capital repayment on the loan. Calculate the loan balances and capital repaid."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "At 12% p.a., monthly interest is exactly 1% (`12% ÷ 12`) of the outstanding loan balance.",
            "Multiply monthly interest by 100 (`× 12 ÷ 0.12`) to find the loan balance before and after the repayment.",
            worked,
        ),
    }


_BUILDERS = {
    "cash_receipts_variance_table": _gen_cash_receipts_variance,
    "cash_payments_variance_table": _gen_cash_payments_variance,
    "projected_income_statement_variance_analysis": _gen_pis_variance_analysis,
    "sales_policy_and_delivery_expense_variance_evaluation": _gen_strategy_variance_evaluation,
    "capital_expenditure_and_loan_variance_analysis": _gen_capex_and_loan_variance,
}


def generate_questions(
    count: int = 1,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    r = random.Random(seed)
    out: List[Dict[str, Any]] = []
    for _ in range(count):
        chosen = subskill if (subskill and subskill in _BUILDERS) else r.choice(SUBSKILLS)
        q = _BUILDERS[chosen](r)
        q["subskill"] = chosen
        q["topic"] = "Cash Budget Variance Analysis"
        q["grade"] = "12"
        out.append(q)
    return out
