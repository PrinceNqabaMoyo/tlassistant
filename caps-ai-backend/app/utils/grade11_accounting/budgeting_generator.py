"""
Grade 11 Accounting: Budgets & Cash Budget Variance Analysis (Partnerships & Sole Traders)
Strictly aligned with South African National Curriculum Standards for Grade 11 Accounting (Term 3).
Zero "Ltd", company tax, or dividend items — strictly Partnership and Sole Trader entities.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "debtors_collection_schedule_with_discount",
    "creditors_payment_schedule_from_markup",
    "partnership_cash_budget_table",
    "projected_income_statement_percentage_changes",
    "cash_budget_vs_projected_income_statement_distinction",
    "budget_vs_actual_variance_analysis_table",
]

PARTNERSHIPS = [
    ("Mokoena & Dlamini Traders", "S. Mokoena", "L. Dlamini"),
    ("Naidoo & Botha Wholesalers", "R. Naidoo", "P. Botha"),
    ("Khumalo & Van Wyk Outfitters", "B. Khumalo", "K. van Wyk"),
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_debtors_collection_schedule(r: random.Random) -> Dict[str, Any]:
    firm, _, _ = r.choice(PARTNERSHIPS)
    cred_may = r.choice([100000, 120000, 150000])
    cred_june = r.choice([120000, 140000, 160000])
    cred_july = r.choice([150000, 180000, 200000])

    # Collection policy: 30% in month of sale less 5% discount (= 28.5% net), 50% in month after, 15% two months after
    july_from_may = int(cred_may * 0.15)
    july_from_june = int(cred_june * 0.50)
    july_from_july = int(cred_july * 0.30 * 0.95)
    tot_july = july_from_may + july_from_june + july_from_july

    headers = ["Month of Credit Sale", "Credit Sales (R)", "Collection Policy in July", "July Cash Collection (R)"]
    rows = [
        ["May", f"R{cred_may:,}", "15% collected 60 days after sale", "{r0_c3}"],
        ["June", f"R{cred_june:,}", "50% collected 30 days after sale", "{r1_c3}"],
        ["July", f"R{cred_july:,}", "30% in month of sale less 5% settlement discount", "{r2_c3}"],
        ["Total Receipts from Debtors in July", "", "", "{r3_c3}"],
    ]
    correct_map = {
        "r0_c3": july_from_may,
        "r1_c3": july_from_june,
        "r2_c3": july_from_july,
        "r3_c3": tot_july,
    }
    worked = (
        f"**Debtors Collection Schedule for July ({firm})**\n\n"
        f"- **From May credit sales (15%)**: `R{cred_may:,} × 15% = R{july_from_may:,}`\n"
        f"- **From June credit sales (50%)**: `R{cred_june:,} × 50% = R{july_from_june:,}`\n"
        f"- **From July credit sales (30% × 95%)**: `R{cred_july:,} × 30% × 95% = R{july_from_july:,}`\n"
        f"- **Total Cash Collected in July**: `R{tot_july:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "debtors_collection_schedule_with_discount",
        "question_text": (
            f"Complete the **July Debtors Collection Schedule** for **{firm}**. Debtors settle **30%** in the month of sale "
            f"(entitled to a **5% settlement discount**), **50%** in the month following the sale, and **15%** two months after the sale."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "When a 5% settlement discount applies to same-month collections, the business receives 95% of that 30% tranche (`30% × 95%`).",
            "Calculate 15% of May, 50% of June, and 28.5% of July credit sales, then sum all three.",
            worked,
        ),
    }


def _gen_creditors_payment_schedule(r: random.Random) -> Dict[str, Any]:
    firm, _, _ = r.choice(PARTNERSHIPS)
    sales_aug = r.choice([240000, 300000, 360000])
    cos_aug = int(sales_aug * (100 / 150))  # 50% mark-up on cost
    credit_purch_aug = int(cos_aug * 0.75)  # 75% bought on credit
    pay_sept = int(credit_purch_aug * 0.90)  # paid in full in following month less 10% trade/settlement discount or 90%

    headers = ["Creditors Payment Calculation (August Stock Purchases)", "Basis", "Amount (R)"]
    rows = [
        [f"Budgeted Total Sales for August (R{sales_aug:,}) — Cost of Sales", "Mark-up of 50% on cost (Sales × 100/150)", "{r0_c2}"],
        ["Credit purchases of trading stock in August", "75% of Cost of Sales bought on credit", "{r1_c2}"],
        ["Cash paid to creditors in September (90% of August credit purchases)", "90% settled in month following purchase", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c2": cos_aug,
        "r1_c2": credit_purch_aug,
        "r2_c2": pay_sept,
    }
    worked = (
        f"**Creditors Payment Calculation ({firm})**\n\n"
        f"- **Cost of Sales**: `R{sales_aug:,} × (100 ÷ 150) = R{cos_aug:,}`\n"
        f"- **Credit Purchases (75%)**: `R{cos_aug:,} × 75% = R{credit_purch_aug:,}`\n"
        f"- **Paid to Creditors in September (90%)**: `R{credit_purch_aug:,} × 90% = R{pay_sept:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "creditors_payment_schedule_from_markup",
        "question_text": (
            f"**{firm}** maintains a **50% mark-up on cost** and replaces all stock sold monthly. "
            f"**75%** of stock is purchased on credit. Complete the schedule for August sales of **R{sales_aug:,}**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "First convert Sales to Cost of Sales using `Sales × 100 / (100 + Mark-up %)`.",
            "Multiply Cost of Sales by 75% to find Credit Purchases, then multiply by 90%.",
            worked,
        ),
    }


def _gen_partnership_cash_budget(r: random.Random) -> Dict[str, Any]:
    firm, p1, p2 = r.choice(PARTNERSHIPS)
    rec = r.randint(140, 210) * 1000
    pay_ops = r.randint(95, 140) * 1000
    part_sal = r.randint(24, 36) * 1000
    cash_draw = r.randint(8, 15) * 1000
    tot_pay = pay_ops + part_sal + cash_draw
    surplus = rec - tot_pay
    open_overdraft = -r.randint(15, 30) * 1000
    close_bank = open_overdraft + surplus

    headers = ["Partnership Cash Budget (October)", "Amount (R)"]
    rows = [
        ["Total Cash Receipts (Cash sales + Debtors collections)", f"R{rec:,}"],
        ["Operating cash payments (Creditors, wages, rent, utilities)", f"R{pay_ops:,}"],
        [f"Monthly cash salaries paid to partners ({p1} and {p2})", f"R{part_sal:,}"],
        ["Cash drawings by partners", f"R{cash_draw:,}"],
        ["Total Cash Payments", "{r4_c1}"],
        ["Cash Surplus / (Deficit) for October", "{r5_c1}"],
        ["Opening Bank Balance (Overdraft)", f"({abs(open_overdraft):,})"],
        ["Closing Bank Balance at 31 October", "{r7_c1}"],
    ]
    correct_map = {
        "r4_c1": tot_pay,
        "r5_c1": surplus,
        "r7_c1": close_bank,
    }
    worked = (
        f"**Partnership Cash Budget ({firm})**\n\n"
        f"- **Total Cash Payments**: `R{pay_ops:,} + R{part_sal:,} + R{cash_draw:,} = R{tot_pay:,}`\n"
        f"- **Cash Surplus**: `R{rec:,} - R{tot_pay:,} = R{surplus:,}`\n"
        f"- **Closing Bank Balance**: `({abs(open_overdraft):,}) + R{surplus:,} = R{close_bank:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "partnership_cash_budget_table",
        "question_text": (
            f"Complete the October **Cash Budget** for the partnership **{firm}** (note that the opening bank balance is an **overdraft of R{abs(open_overdraft):,}**)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "An opening bank overdraft is a negative starting balance, so a positive cash surplus reduces the overdraft or turns it into a positive balance.",
            "Sum the three payment lines for Total Cash Payments, subtract from Total Receipts, and add to the negative opening balance.",
            worked,
        ),
    }


def _gen_projected_income_statement(r: random.Random) -> Dict[str, Any]:
    firm, _, _ = r.choice(PARTNERSHIPS)
    oct_sales = r.choice([200000, 250000, 300000])
    nov_sales = int(oct_sales * 1.10)  # 10% increase
    nov_cos = int(nov_sales * 0.60)
    nov_gp = nov_sales - nov_cos
    oct_sal = 40000
    nov_sal = int(oct_sal * 1.08)  # 8% wage increase
    depr = 12000
    nov_op_profit = nov_gp - nov_sal - depr

    headers = ["Projected Income Statement Item", "October (R)", "Projected Change", "November (R)"]
    rows = [
        ["Sales", f"R{oct_sales:,}", "+10% seasonal increase", "{r0_c3}"],
        ["Cost of sales (60% of sales)", f"(R{int(oct_sales * 0.6):,})", "Maintained at 60% of sales", "{r1_c3}"],
        ["Gross profit", f"R{int(oct_sales * 0.4):,}", "Sales less Cost of sales", "{r2_c3}"],
        ["Staff salaries and wages", f"R{oct_sal:,}", "+8% annual wage increase", "{r3_c3}"],
        ["Depreciation on equipment", f"R{depr:,}", "Unchanged", f"R{depr:,}"],
        ["Projected Operating Profit", f"R{int(oct_sales * 0.4) - oct_sal - depr:,}", "", "{r5_c3}"],
    ]
    correct_map = {
        "r0_c3": nov_sales,
        "r1_c3": nov_cos,
        "r2_c3": nov_gp,
        "r3_c3": nov_sal,
        "r5_c3": nov_op_profit,
    }
    worked = (
        f"**Projected Income Statement ({firm})**\n\n"
        f"- **November Sales (+10%)**: `R{oct_sales:,} × 1.10 = R{nov_sales:,}`\n"
        f"- **November Cost of Sales (60%)**: `R{nov_sales:,} × 60% = R{nov_cos:,}`\n"
        f"- **November Gross Profit**: `R{nov_sales:,} - R{nov_cos:,} = R{nov_gp:,}`\n"
        f"- **November Staff Salaries (+8%)**: `R{oct_sal:,} × 1.08 = R{nov_sal:,}`\n"
        f"- **Projected Operating Profit**: `R{nov_gp:,} - R{nov_sal:,} - R{depr:,} = R{nov_op_profit:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "projected_income_statement_percentage_changes",
        "question_text": f"Complete the November **Projected Income Statement** for **{firm}** (enter positive Rand values).",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Unlike a Cash Budget, a Projected Income Statement includes credit sales, cost of sales, and non-cash expenses like depreciation.",
            "Apply the percentage increases to October figures and compute Gross Profit and Operating Profit.",
            worked,
        ),
    }


def _gen_cash_budget_vs_pis_distinction(r: random.Random) -> Dict[str, Any]:
    headers = ["Transaction for November", "Amount in November Cash Budget (R)", "Amount in November Projected Income Statement (R)"]
    rows = [
        ["Credit sales of R90,000 made in November (to be collected in December)", "{r0_c1}", "{r0_c2}"],
        ["Monthly depreciation of R6,500 on delivery vehicles", "{r1_c1}", "{r1_c2}"],
        ["Cash drawings of R12,000 taken by Partner A in November", "{r2_c1}", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c1": 0,
        "r0_c2": 90000,
        "r1_c1": 0,
        "r1_c2": 6500,
        "r2_c1": 12000,
        "r2_c2": 0,
    }
    worked = (
        "**Cash Budget vs Projected Income Statement Distinction**\n\n"
        "- **Credit sales collected next month (`R90,000`)**: `R0` in November Cash Budget; `R90,000` in November Projected Income Statement.\n"
        "- **Depreciation (`R6,500`)**: `R0` in Cash Budget (non-cash); `R6,500` in Projected Income Statement.\n"
        "- **Cash drawings (`R12,000`)**: `R12,000` in Cash Budget; `R0` in Projected Income Statement (balance sheet equity item, not an operating expense)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "cash_budget_vs_projected_income_statement_distinction",
        "question_text": (
            "Enter the Rand amount (`0` if excluded) that will appear in the **November Cash Budget** and the **November Projected Income Statement** for each item."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Cash Budget tracks actual cash movement in November; Projected Income Statement tracks earned income and incurred expenses in November.",
            "Remember that partner cash drawings reduce cash in the Cash Budget but are not an expense in the Income Statement.",
            worked,
        ),
    }


def _gen_variance_analysis_table(r: random.Random) -> Dict[str, Any]:
    firm, _, _ = r.choice(PARTNERSHIPS)
    b_rec = 120000
    a_rec = 96000
    var_rec = a_rec - b_rec

    b_adv = 10000
    a_adv = 14500
    var_adv = a_adv - b_adv

    b_rep = 8000
    a_rep = 6200
    var_rep = a_rep - b_rep

    headers = ["Cash Budget Item", "Budgeted (R)", "Actual (R)", "Variance Amount (positive R)", "Impact on Cash Flow (Favourable / Unfavourable)"]
    rows = [
        ["Receipts from debtors", f"R{b_rec:,}", f"R{a_rec:,}", "{r0_c3}", "{r0_c4}"],
        ["Advertising cash payments", f"R{b_adv:,}", f"R{a_adv:,}", "{r1_c3}", "{r1_c4}"],
        ["Delivery vehicle maintenance", f"R{b_rep:,}", f"R{a_rep:,}", "{r2_c3}", "{r2_c4}"],
    ]
    correct_map = {
        "r0_c3": abs(var_rec),
        "r0_c4": "Unfavourable",
        "r1_c3": abs(var_adv),
        "r1_c4": "Unfavourable",
        "r2_c3": abs(var_rep),
        "r2_c4": "Favourable",
    }
    worked = (
        f"**Cash Budget Variance Analysis ({firm})**\n\n"
        f"- **Receipts from debtors**: `R{b_rec:,} - R{a_rec:,} = R{abs(var_rec):,}` (**Unfavourable** — collected less cash than budgeted).\n"
        f"- **Advertising payments**: `R{a_adv:,} - R{b_adv:,} = R{abs(var_adv):,}` (**Unfavourable** — overspent on advertising).\n"
        f"- **Vehicle maintenance**: `R{b_rep:,} - R{a_rep:,} = R{abs(var_rep):,}` (**Favourable** — spent less than budgeted)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "budget_vs_actual_variance_analysis_table",
        "question_text": (
            f"Complete the **Cash Budget Variance Analysis** table for **{firm}** (enter positive Rand differences and classify as **Favourable** or **Unfavourable**)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Collecting less cash than budgeted or paying more cash than budgeted is Unfavourable.",
            "Enter the absolute Rand difference in Column 4 and Favourable/Unfavourable in Column 5.",
            worked,
        ),
    }


_BUILDERS = {
    "debtors_collection_schedule_with_discount": _gen_debtors_collection_schedule,
    "creditors_payment_schedule_from_markup": _gen_creditors_payment_schedule,
    "partnership_cash_budget_table": _gen_partnership_cash_budget,
    "projected_income_statement_percentage_changes": _gen_projected_income_statement,
    "cash_budget_vs_projected_income_statement_distinction": _gen_cash_budget_vs_pis_distinction,
    "budget_vs_actual_variance_analysis_table": _gen_variance_analysis_table,
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
        q["topic"] = "Budgets"
        q["grade"] = "11"
        out.append(q)
    return out
