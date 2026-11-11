"""
Grade 10 Accounting: Financial Accounting vs Managerial Accounting
Strictly aligned with South African National Curriculum Standards for Grade 10 Accounting.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "financial_vs_managerial_comparison_table",
    "internal_vs_external_decision_makers",
    "historical_reports_vs_future_projections",
    "classifying_accounting_reports_table",
    "case_study_financial_and_managerial_integration",
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_comparison_table(r: random.Random) -> Dict[str, Any]:
    headers = ["Feature / Criterion", "Financial Accounting", "Managerial Accounting"]
    rows = [
        ["Primary users of reports (Internal / External)", "{r0_c1}", "{r0_c2}"],
        ["Time focus (Past / Future)", "{r1_c1}", "{r1_c2}"],
        ["Governing rules (GAAP / Flexible)", "{r2_c1}", "{r2_c2}"],
        ["Reporting frequency (Annual / As needed)", "{r3_c1}", "{r3_c2}"],
    ]
    correct_map = {
        "r0_c1": "External",
        "r0_c2": "Internal",
        "r1_c1": "Past",
        "r1_c2": "Future",
        "r2_c1": "GAAP",
        "r2_c2": "Flexible",
        "r3_c1": "Annual",
        "r3_c2": "As needed",
    }
    worked = (
        "**Financial vs Managerial Accounting Comparison**\n\n"
        "- **Primary users**: Financial Accounting serves **External** stakeholders (banks, SARS, creditors); Managerial Accounting serves **Internal** managers/owners.\n"
        "- **Time focus**: Financial Accounting reports on **Past** historical performance; Managerial Accounting plans for the **Future**.\n"
        "- **Governing rules**: Financial Accounting strictly follows **GAAP**; Managerial Accounting is **Flexible** to management needs.\n"
        "- **Frequency**: Financial Accounting is prepared **Annual**ly; Managerial Accounting is prepared **As needed** (weekly/monthly)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "financial_vs_managerial_comparison_table",
        "question_text": (
            "Complete the comparison table distinguishing **Financial Accounting** from **Managerial Accounting** "
            "using the options provided in brackets in each row."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Financial Accounting focuses on external reporting of historical results under GAAP, whereas Managerial Accounting supports internal planning.",
            "Match External/Past/GAAP/Annual to Financial Accounting and Internal/Future/Flexible/As needed to Managerial Accounting.",
            worked,
        ),
    }


def _gen_decision_makers(r: random.Random) -> Dict[str, Any]:
    headers = ["Stakeholder", "User Type (Internal / External)", "Primary Accounting Branch Used (Financial / Managerial)"]
    rows = [
        ["Store Manager setting next month's sales targets", "{r0_c1}", "{r0_c2}"],
        ["South African Revenue Service (SARS) assessing tax compliance", "{r1_c1}", "{r1_c2}"],
        ["Commercial Bank evaluating a mortgage loan application", "{r2_c1}", "{r2_c2}"],
        ["Production Supervisor tracking weekly raw material wastage", "{r3_c1}", "{r3_c2}"],
    ]
    correct_map = {
        "r0_c1": "Internal",
        "r0_c2": "Managerial",
        "r1_c1": "External",
        "r1_c2": "Financial",
        "r2_c1": "External",
        "r2_c2": "Financial",
        "r3_c1": "Internal",
        "r3_c2": "Managerial",
    }
    worked = (
        "**Internal vs External Decision Makers**\n\n"
        "- **Store Manager**: **Internal** $\\rightarrow$ **Managerial** Accounting\n"
        "- **SARS**: **External** $\\rightarrow$ **Financial** Accounting\n"
        "- **Commercial Bank**: **External** $\\rightarrow$ **Financial** Accounting\n"
        "- **Production Supervisor**: **Internal** $\\rightarrow$ **Managerial** Accounting"
    )
    return {
        "question_type": "table_fill",
        "subskill": "internal_vs_external_decision_makers",
        "question_text": (
            "For each stakeholder listed below, identify whether they are an **Internal** or **External** user "
            "and state whether they rely primarily on **Financial** or **Managerial** accounting reports."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Internal users work inside the business managing day-to-day operations; external users are outside parties.",
            "Internal users rely on Managerial Accounting; External users rely on Financial Accounting.",
            worked,
        ),
    }


def _gen_historical_vs_future(r: random.Random) -> Dict[str, Any]:
    headers = ["Accounting Activity", "Orientation (Historical / Future-Oriented)", "Branch (Financial / Managerial)"]
    rows = [
        ["Recording February credit invoices from suppliers in the Creditors Journal", "{r0_c1}", "{r0_c2}"],
        ["Forecasting monthly cash inflows and outflows for Quarter 3", "{r1_c1}", "{r1_c2}"],
        ["Preparing the Statement of Financial Position at 28 February", "{r2_c1}", "{r2_c2}"],
        ["Calculating the break-even selling price for a new product line", "{r3_c1}", "{r3_c2}"],
    ]
    correct_map = {
        "r0_c1": "Historical",
        "r0_c2": "Financial",
        "r1_c1": "Future-Oriented",
        "r1_c2": "Managerial",
        "r2_c1": "Historical",
        "r2_c2": "Financial",
        "r3_c1": "Future-Oriented",
        "r3_c2": "Managerial",
    }
    worked = (
        "**Historical vs Future-Oriented Activities**\n\n"
        "- Recording February invoices: **Historical** $\\rightarrow$ **Financial**\n"
        "- Forecasting Quarter 3 cash flows: **Future-Oriented** $\\rightarrow$ **Managerial**\n"
        "- Preparing the Balance Sheet: **Historical** $\\rightarrow$ **Financial**\n"
        "- Calculating break-even selling price: **Future-Oriented** $\\rightarrow$ **Managerial**"
    )
    return {
        "question_type": "table_fill",
        "subskill": "historical_reports_vs_future_projections",
        "question_text": (
            "Classify each accounting activity by its time orientation (**Historical** or **Future-Oriented**) "
            "and accounting branch (**Financial** or **Managerial**)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Activities that record past transactions are Historical (Financial); activities that project future targets are Future-Oriented (Managerial).",
            "Identify whether the activity looks back at completed transactions or forward at budgets/targets.",
            worked,
        ),
    }


def _gen_classifying_reports(r: random.Random) -> Dict[str, Any]:
    headers = ["Document / Report", "Branch (Financial / Managerial)"]
    rows = [
        ["Statement of Comprehensive Income (Income Statement)", "{r0_c1}"],
        ["Monthly Cash Budget and Debtors Collection Schedule", "{r1_c1}"],
        ["Post-Adjustment Trial Balance", "{r2_c1}"],
        ["Departmental Cost Variance and Unit Production Cost Report", "{r3_c1}"],
        ["Statement of Financial Position (Balance Sheet)", "{r4_c1}"],
    ]
    correct_map = {
        "r0_c1": "Financial",
        "r1_c1": "Managerial",
        "r2_c1": "Financial",
        "r3_c1": "Managerial",
        "r4_c1": "Financial",
    }
    worked = (
        "**Classifying Accounting Reports**\n\n"
        "- **Income Statement**: **Financial**\n"
        "- **Monthly Cash Budget**: **Managerial**\n"
        "- **Post-Adjustment Trial Balance**: **Financial**\n"
        "- **Departmental Cost Variance Report**: **Managerial**\n"
        "- **Balance Sheet**: **Financial**"
    )
    return {
        "question_type": "table_fill",
        "subskill": "classifying_accounting_reports_table",
        "question_text": (
            "Classify each accounting report below as belonging to either **Financial** or **Managerial** accounting."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Annual financial statements and trial balances belong to Financial Accounting; budgets and cost reports belong to Managerial Accounting.",
            "Enter either 'Financial' or 'Managerial' for each report.",
            worked,
        ),
    }


def _gen_case_study_integration(r: random.Random) -> Dict[str, Any]:
    last_yr_sales = r.randint(500, 700) * 1000
    growth_pct = r.choice([10, 15, 20])
    budget_sales = int(last_yr_sales * (1 + growth_pct / 100))
    target_gp = int(budget_sales * 0.40)

    headers = ["Metric", "Accounting Branch (Financial / Managerial)", "Amount (R)"]
    rows = [
        ["Audited sales from last year's Income Statement", "{r0_c1}", f"R{last_yr_sales:,}"],
        [f"Projected sales for next year ({growth_pct}% budgeted increase)", "{r1_c1}", "{r1_c2}"],
        ["Target Gross Profit for next year (40% gross margin target)", "Managerial", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c1": "Financial",
        "r1_c1": "Managerial",
        "r1_c2": budget_sales,
        "r2_c2": target_gp,
    }
    worked = (
        f"**Integrating Financial and Managerial Accounting**\n\n"
        f"- Last year's audited sales (`R{last_yr_sales:,}`) come from **Financial** Accounting.\n"
        f"- Projected sales for next year belong to **Managerial** Accounting: `R{last_yr_sales:,} × (1 + {growth_pct}%) = R{budget_sales:,}`.\n"
        f"- Target Gross Profit (40%): `R{budget_sales:,} × 40% = R{target_gp:,}`."
    )
    return {
        "question_type": "table_fill",
        "subskill": "case_study_financial_and_managerial_integration",
        "question_text": (
            f"A sole trader uses last year's **Financial Accounting** sales of **R{last_yr_sales:,}** to prepare next year's "
            f"**Managerial Accounting** budget assuming a **{growth_pct}% increase in sales** and a **40% gross profit margin**. Complete the table."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Financial Accounting provides the historical baseline that Managerial Accounting uses to project future budgets.",
            f"Increase R{last_yr_sales:,} by {growth_pct}% for Row 2, then calculate 40% of that projected sales figure for Row 3.",
            worked,
        ),
    }


_BUILDERS = {
    "financial_vs_managerial_comparison_table": _gen_comparison_table,
    "internal_vs_external_decision_makers": _gen_decision_makers,
    "historical_reports_vs_future_projections": _gen_historical_vs_future,
    "classifying_accounting_reports_table": _gen_classifying_reports,
    "case_study_financial_and_managerial_integration": _gen_case_study_integration,
}


def generate_questions(
    count: int = 1,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    r = random.Random(seed)
    out: List[Dict[str, Any]] = []
    for i in range(count):
        chosen = subskill if (subskill and subskill in _BUILDERS) else r.choice(SUBSKILLS)
        q = _BUILDERS[chosen](r)
        q["subskill"] = chosen
        q["topic"] = "Financial accounting vs Managerial accounting"
        q["grade"] = "10"
        out.append(q)
    return out
