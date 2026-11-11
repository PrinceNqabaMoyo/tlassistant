"""
Grade 10 Accounting: Budgeting (Introductory Sole Trader Cash Budgets)
Strictly aligned with South African National Curriculum Standards for Grade 10 Accounting (Term 4).
No company ("Ltd") or corporate dividend/tax items.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "budgeting_concepts_and_types",
    "sole_trader_cash_receipts_and_payments_schedule",
    "sole_trader_cash_budget_table",
    "debtors_collection_from_credit_sales_basic",
    "budget_vs_actual_basic_comparison_table",
]

TRADERS = [
    ("Sibusiso Fresh Mart", "S. Dlamini"),
    ("Vhembe Stationery Shop", "R. Mudau"),
    ("Sunrise Bakery", "N. Pillay"),
    ("Karoo Cycle Repair", "J. Botha"),
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_budgeting_concepts(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    headers = ["Transaction / Item", "Included in Cash Budget? (Yes / No)", "Reason (Cash Inflow / Cash Outflow / Non-Cash Item)"]
    rows = [
        ["Cash sales of merchandise to customers", "{r0_c1}", "{r0_c2}"],
        ["Depreciation on shop equipment", "{r1_c1}", "{r1_c2}"],
        ["Monthly shop rent paid by EFT", "{r2_c1}", "{r2_c2}"],
        ["Bad debts written off", "{r3_c1}", "{r3_c2}"],
    ]
    correct_map = {
        "r0_c1": "Yes",
        "r0_c2": "Cash Inflow",
        "r1_c1": "No",
        "r1_c2": "Non-Cash Item",
        "r2_c1": "Yes",
        "r2_c2": "Cash Outflow",
        "r3_c1": "No",
        "r3_c2": "Non-Cash Item",
    }
    worked = (
        f"**Cash Budget Inclusion Rules ({firm})**\n\n"
        f"- **Cash sales**: **Yes** (**Cash Inflow**) — actual cash received.\n"
        f"- **Depreciation**: **No** (**Non-Cash Item**) — book entry with no cash movement.\n"
        f"- **Monthly rent paid**: **Yes** (**Cash Outflow**) — actual cash paid.\n"
        f"- **Bad debts written off**: **No** (**Non-Cash Item**) — no cash is paid out."
    )
    return {
        "question_type": "table_fill",
        "subskill": "budgeting_concepts_and_types",
        "question_text": (
            f"**{firm}** is preparing its monthly **Cash Budget**. Indicate whether each item is included in the "
            f"Cash Budget (**Yes** or **No**) and classify the reason (**Cash Inflow**, **Cash Outflow**, or **Non-Cash Item**)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "A Cash Budget only records actual projected cash receipts and cash payments.",
            "Exclude non-cash expenses such as depreciation, bad debts, and discount allowed.",
            worked,
        ),
    }


def _gen_cash_receipts_and_payments(r: random.Random) -> Dict[str, Any]:
    firm, owner = r.choice(TRADERS)
    cash_sales = r.randint(45, 85) * 1000
    debt_coll = r.randint(25, 50) * 1000
    rent_inc = r.randint(6, 12) * 1000
    tot_rec = cash_sales + debt_coll + rent_inc

    cash_purch = r.randint(30, 55) * 1000
    cred_pay = r.randint(15, 30) * 1000
    wages = r.randint(12, 22) * 1000
    drawings_cash = r.randint(4, 9) * 1000
    tot_pay = cash_purch + cred_pay + wages + drawings_cash

    headers = ["Cash Budget Section (October)", "Amount (R)"]
    rows = [
        ["Cash sales", f"R{cash_sales:,}"],
        ["Receipts from debtors", f"R{debt_coll:,}"],
        ["Rent income received", f"R{rent_inc:,}"],
        ["Total Cash Receipts", "{r3_c1}"],
        ["Cash purchases of trading stock", f"R{cash_purch:,}"],
        ["Payments to creditors", f"R{cred_pay:,}"],
        ["Staff wages and operating expenses", f"R{wages:,}"],
        [f"Cash drawings by owner ({owner})", f"R{drawings_cash:,}"],
        ["Total Cash Payments", "{r8_c1}"],
    ]
    correct_map = {
        "r3_c1": tot_rec,
        "r8_c1": tot_pay,
    }
    worked = (
        f"**Cash Receipts & Cash Payments Schedule ({firm})**\n\n"
        f"- **Total Cash Receipts**: `R{cash_sales:,} + R{debt_coll:,} + R{rent_inc:,} = R{tot_rec:,}`\n"
        f"- **Total Cash Payments**: `R{cash_purch:,} + R{cred_pay:,} + R{wages:,} + R{drawings_cash:,} = R{tot_pay:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "sole_trader_cash_receipts_and_payments_schedule",
        "question_text": (
            f"Calculate the **Total Cash Receipts** and **Total Cash Payments** for **{firm}** (owner: {owner}) for October."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Group all cash inflows under Total Cash Receipts and all cash outflows (including cash drawings) under Total Cash Payments.",
            "Sum the first three items for Total Cash Receipts, and sum the next four items for Total Cash Payments.",
            worked,
        ),
    }


def _gen_cash_budget_table(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    rec_m1 = r.randint(70, 110) * 1000
    pay_m1 = r.randint(55, 85) * 1000
    surp_m1 = rec_m1 - pay_m1
    open_m1 = r.randint(15, 35) * 1000
    close_m1 = open_m1 + surp_m1

    rec_m2 = r.randint(80, 120) * 1000
    pay_m2 = r.randint(65, 95) * 1000
    surp_m2 = rec_m2 - pay_m2
    open_m2 = close_m1
    close_m2 = open_m2 + surp_m2

    headers = ["Cash Budget Summary", "November (R)", "December (R)"]
    rows = [
        ["Total Cash Receipts", f"R{rec_m1:,}", f"R{rec_m2:,}"],
        ["Total Cash Payments", f"(R{pay_m1:,})", f"(R{pay_m2:,})"],
        ["Cash Surplus / (Deficit) for the month", "{r2_c1}", "{r2_c2}"],
        ["Opening Bank Balance (1st of month)", f"R{open_m1:,}", "{r3_c2}"],
        ["Closing Bank Balance (end of month)", "{r4_c1}", "{r4_c2}"],
    ]
    correct_map = {
        "r2_c1": surp_m1,
        "r2_c2": surp_m2,
        "r3_c2": open_m2,
        "r4_c1": close_m1,
        "r4_c2": close_m2,
    }
    worked = (
        f"**Two-Month Sole Trader Cash Budget ({firm})**\n\n"
        f"- **November**:\n"
        f"  - Cash Surplus: `R{rec_m1:,} - R{pay_m1:,} = R{surp_m1:,}`\n"
        f"  - Closing Bank Balance: `R{open_m1:,} + R{surp_m1:,} = R{close_m1:,}`\n"
        f"- **December**:\n"
        f"  - Opening Bank Balance = November Closing Balance = `R{open_m2:,}`\n"
        f"  - Cash Surplus: `R{rec_m2:,} - R{pay_m2:,} = R{surp_m2:,}`\n"
        f"  - Closing Bank Balance: `R{open_m2:,} + R{surp_m2:,} = R{close_m2:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "sole_trader_cash_budget_table",
        "question_text": (
            f"Complete the two-month **Cash Budget Summary** for **{firm}** for November and December."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "The closing bank balance of November automatically becomes the opening bank balance of December.",
            "Subtract Total Cash Payments from Total Cash Receipts to find the monthly surplus, then add the opening bank balance.",
            worked,
        ),
    }


def _gen_debtors_collection_basic(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    tot_sales = r.choice([100000, 120000, 150000])
    cash_pct = 60
    credit_pct = 40
    cash_sales = int(tot_sales * 0.60)
    credit_sales = int(tot_sales * 0.40)
    coll_same_month = int(credit_sales * 0.50)
    coll_next_month = int(credit_sales * 0.45)

    headers = ["Sales & Debtors Collection Item (March Sales)", "Basis", "Amount (R)"]
    rows = [
        [f"Total budgeted sales for March (R{tot_sales:,})", "100% of sales", f"R{tot_sales:,}"],
        ["Cash sales for March", f"{cash_pct}% of total sales", "{r1_c2}"],
        ["Credit sales for March", f"{credit_pct}% of total sales", "{r2_c2}"],
        ["Collected from March debtors in March", "50% of March credit sales", "{r3_c2}"],
        ["Collected from March debtors in April", "45% of March credit sales (5% uncollectable)", "{r4_c2}"],
    ]
    correct_map = {
        "r1_c2": cash_sales,
        "r2_c2": credit_sales,
        "r3_c2": coll_same_month,
        "r4_c2": coll_next_month,
    }
    worked = (
        f"**Basic Debtors Collection Calculation ({firm})**\n\n"
        f"- **Cash sales (60%)**: `60% × R{tot_sales:,} = R{cash_sales:,}`\n"
        f"- **Credit sales (40%)**: `40% × R{tot_sales:,} = R{credit_sales:,}`\n"
        f"- **Collected in March (50% of credit sales)**: `50% × R{credit_sales:,} = R{coll_same_month:,}`\n"
        f"- **Collected in April (45% of credit sales)**: `45% × R{credit_sales:,} = R{coll_next_month:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "debtors_collection_from_credit_sales_basic",
        "question_text": (
            f"**{firm}** budgets total sales of **R{tot_sales:,}** for March. **60%** of sales are for cash and **40%** are on credit. "
            f"Debtors pay **50%** in the month of sale and **45%** in the following month. Complete the schedule."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Debtors collections are calculated only on Credit Sales, not on Total Sales.",
            "First split Total Sales into 60% Cash Sales and 40% Credit Sales, then apply 50% and 45% to the Credit Sales figure.",
            worked,
        ),
    }


def _gen_budget_vs_actual(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    b_sales = r.randint(80, 110) * 1000
    a_sales = b_sales + r.randint(5, 15) * 1000
    b_tel = r.randint(3, 5) * 1000
    a_tel = b_tel + r.randint(1, 3) * 1000
    b_pack = r.randint(6, 10) * 1000
    a_pack = b_pack - r.randint(1, 2) * 1000

    headers = ["Budget Item", "Budgeted (R)", "Actual (R)", "Difference (R)", "Evaluation (Favourable / Unfavourable)"]
    rows = [
        ["Cash sales", f"R{b_sales:,}", f"R{a_sales:,}", "{r0_c3}", "{r0_c4}"],
        ["Telephone and internet expense", f"R{b_tel:,}", f"R{a_tel:,}", "{r1_c3}", "{r1_c4}"],
        ["Packing materials expense", f"R{b_pack:,}", f"R{a_pack:,}", "{r2_c3}", "{r2_c4}"],
    ]
    correct_map = {
        "r0_c3": a_sales - b_sales,
        "r0_c4": "Favourable",
        "r1_c3": a_tel - b_tel,
        "r1_c4": "Unfavourable",
        "r2_c3": b_pack - a_pack,
        "r2_c4": "Favourable",
    }
    worked = (
        f"**Budget vs Actual Comparison ({firm})**\n\n"
        f"- **Cash sales**: Actual (`R{a_sales:,}`) exceeded Budget (`R{b_sales:,}`) by `R{a_sales - b_sales:,}` $\\rightarrow$ **Favourable**.\n"
        f"- **Telephone expense**: Actual (`R{a_tel:,}`) exceeded Budget (`R{b_tel:,}`) by `R{a_tel - b_tel:,}` $\\rightarrow$ **Unfavourable**.\n"
        f"- **Packing materials**: Actual (`R{a_pack:,}`) was below Budget (`R{b_pack:,}`) by `R{b_pack - a_pack:,}` $\\rightarrow$ **Favourable**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "budget_vs_actual_basic_comparison_table",
        "question_text": (
            f"Compare the budgeted and actual figures for **{firm}**. Enter the positive Rand difference and state whether each variance "
            f"is **Favourable** or **Unfavourable**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Higher actual income than budgeted is Favourable; higher actual expenses than budgeted is Unfavourable.",
            "Calculate the positive difference between Budgeted and Actual for each row, then classify the impact on cash flow.",
            worked,
        ),
    }


_BUILDERS = {
    "budgeting_concepts_and_types": _gen_budgeting_concepts,
    "sole_trader_cash_receipts_and_payments_schedule": _gen_cash_receipts_and_payments,
    "sole_trader_cash_budget_table": _gen_cash_budget_table,
    "debtors_collection_from_credit_sales_basic": _gen_debtors_collection_basic,
    "budget_vs_actual_basic_comparison_table": _gen_budget_vs_actual,
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
        q["topic"] = "Budgeting"
        q["grade"] = "10"
        out.append(q)
    return out
