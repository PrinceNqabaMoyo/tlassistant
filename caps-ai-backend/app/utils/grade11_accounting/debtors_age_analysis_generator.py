"""
Grade 11 Accounting: Debtors Age Analysis
Strictly aligned with South African National Curriculum Standards for Grade 11 Accounting.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "debtors_age_schedule_completion",
    "allocating_returns_and_receipts_to_aging_buckets",
    "identifying_credit_limit_and_term_breaches",
    "overdue_interest_and_bad_debt_provision_from_aging",
    "credit_control_remedial_actions_table",
]

PARTNERSHIPS = [
    "Sibanda & Khoza Traders",
    "Highveld Hardware Partnership",
    "Coastal Electrical Suppliers",
    "Jacaranda Wholesalers",
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_age_schedule_completion(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    d1_curr, d1_30, d1_60 = r.randint(4, 9) * 1000, r.randint(3, 6) * 1000, 0
    d1_tot = d1_curr + d1_30

    d2_curr, d2_30, d2_60 = r.randint(2, 5) * 1000, r.randint(4, 8) * 1000, r.randint(3, 6) * 1000
    d2_tot = d2_curr + d2_30 + d2_60

    tot_curr = d1_curr + d2_curr
    tot_30 = d1_30 + d2_30
    tot_60 = d1_60 + d2_60
    grand_tot = d1_tot + d2_tot

    headers = ["Debtor", "Total Owing (R)", "Current (R)", "30 Days (R)", "60+ Days (R)"]
    rows = [
        ["T. Nkosi", "{r0_c1}", f"R{d1_curr:,}", f"R{d1_30:,}", "R0"],
        ["M. Venter", f"R{d2_tot:,}", f"R{d2_curr:,}", "{r1_c3}", f"R{d2_60:,}"],
        ["Total Debtors", "{r2_c1}", f"R{tot_curr:,}", f"R{tot_30:,}", "{r2_c4}"],
    ]
    correct_map = {
        "r0_c1": d1_tot,
        "r1_c3": d2_30,
        "r2_c1": grand_tot,
        "r2_c4": tot_60,
    }
    worked = (
        f"**Debtors Age Schedule ({firm})**\n\n"
        f"- **T. Nkosi Total**: `R{d1_curr:,} + R{d1_30:,} = R{d1_tot:,}`\n"
        f"- **M. Venter 30 Days**: `R{d2_tot:,} - R{d2_curr:,} - R{d2_60:,} = R{d2_30:,}`\n"
        f"- **Total Debtors**: `R{d1_tot:,} + R{d2_tot:,} = R{grand_tot:,}`\n"
        f"- **60+ Days Total**: `R{tot_60:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "debtors_age_schedule_completion",
        "question_text": f"Complete the missing figures in the **Debtors Age Analysis** schedule of **{firm}**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Each row's aging buckets must sum to that debtor's Total Owing, and each column must sum vertically.",
            "Add T. Nkosi's buckets for r0_c1, subtract M. Venter's known buckets from their total for r1_c3, and sum the totals.",
            worked,
        ),
    }


def _gen_allocating_returns_and_receipts(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    curr = r.randint(6, 12) * 1000
    d30 = r.randint(5, 9) * 1000
    d60 = r.randint(4, 7) * 1000
    payment_oldest = d60
    return_current = r.randint(1, 2) * 1000

    new_curr = curr - return_current
    new_60 = 0
    new_tot = new_curr + d30

    headers = ["Debtor: P. Mahlangu", "Total (R)", "Current (R)", "30 Days (R)", "60 Days (R)"]
    rows = [
        ["Balance before adjustments", f"R{curr + d30 + d60:,}", f"R{curr:,}", f"R{d30:,}", f"R{d60:,}"],
        [f"Less: EFT received settling 60-day balance (R{payment_oldest:,})", f"(R{payment_oldest:,})", "0", "0", f"(R{payment_oldest:,})"],
        [f"Less: Goods returned from current month's invoice (R{return_current:,})", f"(R{return_current:,})", f"(R{return_current:,})", "0", "0"],
        ["Adjusted Age Analysis Balance", "{r3_c1}", "{r3_c2}", f"R{d30:,}", "{r3_c4}"],
    ]
    correct_map = {
        "r3_c1": new_tot,
        "r3_c2": new_curr,
        "r3_c4": new_60,
    }
    worked = (
        f"**Allocating Payments & Returns to Aging Buckets ({firm})**\n\n"
        f"- Payments from debtors reduce the **oldest debt first** (`60 Days`: `R{d60:,} - R{payment_oldest:,} = R0`).\n"
        f"- Credit notes (returns) reduce the **specific invoice bucket** (`Current`: `R{curr:,} - R{return_current:,} = R{new_curr:,}`).\n"
        f"- **Adjusted Total**: `R{new_curr:,} + R{d30:,} = R{new_tot:,}`."
    )
    return {
        "question_type": "table_fill",
        "subskill": "allocating_returns_and_receipts_to_aging_buckets",
        "question_text": (
            f"Update **P. Mahlangu's** age analysis at **{firm}** after recording an EFT payment of **R{payment_oldest:,}** "
            f"(allocated to the oldest debt) and a credit note of **R{return_current:,}** for goods returned from the current month's purchase."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Receipts from debtors are allocated against the oldest balance first (60 days), while returns are deducted from the month in which the sale occurred.",
            "Deduct the return from Current and deduct the EFT payment from 60 Days.",
            worked,
        ),
    }


def _gen_credit_limit_and_term_breaches(r: random.Random) -> Dict[str, Any]:
    headers = ["Debtor", "Credit Limit (R)", "Total Owing (R)", "Current (R)", "30 Days (R)", "60+ Days (R)", "Violation Type (Exceeded Credit Limit / Overdue 30-Day Terms / Compliant)"]
    rows = [
        ["A. Sithole", "R15,000", "R18,500", "R18,500", "R0", "R0", "{r0_c6}"],
        ["B. Jacobs", "R20,000", "R14,000", "R2,000", "R5,000", "R7,000", "{r1_c6}"],
        ["C. Govender", "R12,000", "R9,500", "R9,500", "R0", "R0", "{r2_c6}"],
    ]
    correct_map = {
        "r0_c6": "Exceeded Credit Limit",
        "r1_c6": "Overdue 30-Day Terms",
        "r2_c6": "Compliant",
    }
    worked = (
        "**Identifying Credit Limit & Credit Term Breaches**\n\n"
        "- **A. Sithole**: Total owing (`R18,500`) exceeds Credit Limit (`R15,000`) $\\rightarrow$ **Exceeded Credit Limit**.\n"
        "- **B. Jacobs**: Within limit (`R14,000 < R20,000`), but has balances in 30 Days and 60+ Days $\\rightarrow$ **Overdue 30-Day Terms**.\n"
        "- **C. Govender**: Within limit (`R9,500 < R12,000`) and 100% in Current $\\rightarrow$ **Compliant**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "identifying_credit_limit_and_term_breaches",
        "question_text": (
            "Credit terms are strictly **30 days (Current)**. Identify each debtor's status using the options in the final column header."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Check two criteria for every debtor: (1) Is Total Owing <= Credit Limit? (2) Are there any amounts older than Current?",
            "Classify A. Sithole, B. Jacobs, and C. Govender using the three options provided.",
            worked,
        ),
    }


def _gen_overdue_interest_and_provision(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    bal_60 = r.choice([20000, 30000, 40000])
    bal_90 = r.choice([10000, 15000, 20000])
    overdue_tot = bal_60 + bal_90
    int_month = int(overdue_tot * 0.12 / 12)
    prov_req = int(overdue_tot * 0.10)

    headers = ["Overdue Debtors Calculation", "Basis", "Amount (R)"]
    rows = [
        [f"Total overdue debt (60 Days R{bal_60:,} + 90 Days R{bal_90:,})", "Sum of balances > 30 days", "{r0_c2}"],
        ["One month's interest charged on overdue accounts", "12% p.a. for 1 month", "{r1_c2}"],
        ["Provision for bad debts required at year-end", "10% of total overdue debt", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c2": overdue_tot,
        "r1_c2": int_month,
        "r2_c2": prov_req,
    }
    worked = (
        f"**Overdue Interest & Provision for Bad Debts ({firm})**\n\n"
        f"- **Total Overdue Debt**: `R{bal_60:,} + R{bal_90:,} = R{overdue_tot:,}`\n"
        f"- **Monthly Interest (12% p.a.)**: `R{overdue_tot:,} × 12% × (1/12) = R{int_month:,}`\n"
        f"- **Provision for Bad Debts (10%)**: `R{overdue_tot:,} × 10% = R{prov_req:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "overdue_interest_and_bad_debt_provision_from_aging",
        "question_text": (
            f"**{firm}** charges **12% p.a. interest** for one month on all accounts in the **60 Days (R{bal_60:,})** "
            f"and **90 Days (R{bal_90:,})** buckets, and maintains a **Provision for Bad Debts at 10% of overdue debt**. Complete the table."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "12% p.a. for 1 month equals 1% for that month (`12% ÷ 12`).",
            "Sum the 60-day and 90-day buckets first, then calculate 1% for monthly interest and 10% for the bad debt provision.",
            worked,
        ),
    }


def _gen_credit_control_actions(r: random.Random) -> Dict[str, Any]:
    headers = ["Age Analysis Observation", "Recommended Control Action (Suspend Further Credit Sales / Offer Early Settlement Discount / Screen Credit References Before Opening Account)"]
    rows = [
        ["Debtor has a balance in the 90-day bucket and continues buying on credit", "{r0_c1}"],
        ["New customers default on their very first credit purchase", "{r1_c1}"],
        ["Most debtors pay in 60 days instead of within the 30-day statement period", "{r2_c1}"],
    ]
    correct_map = {
        "r0_c1": "Suspend Further Credit Sales",
        "r1_c1": "Screen Credit References Before Opening Account",
        "r2_c1": "Offer Early Settlement Discount",
    }
    worked = (
        "**Credit Control Remedial Actions**\n\n"
        "- **90-day overdue debtor still buying**: **Suspend Further Credit Sales** until arrears are settled.\n"
        "- **New customers defaulting**: **Screen Credit References Before Opening Account** (credit checks, payslips, bank references).\n"
        "- **Slow 60-day collections**: **Offer Early Settlement Discount** for payment within 30 days and send monthly statements promptly."
    )
    return {
        "question_type": "table_fill",
        "subskill": "credit_control_remedial_actions_table",
        "question_text": (
            "Match each **Debtors Age Analysis** problem to the most effective internal control action."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Preventative controls stop bad debtors from opening accounts; corrective controls stop overdue debtors from increasing their debt.",
            "Match each observation to the appropriate control action from the column heading.",
            worked,
        ),
    }


_BUILDERS = {
    "debtors_age_schedule_completion": _gen_age_schedule_completion,
    "allocating_returns_and_receipts_to_aging_buckets": _gen_allocating_returns_and_receipts,
    "identifying_credit_limit_and_term_breaches": _gen_credit_limit_and_term_breaches,
    "overdue_interest_and_bad_debt_provision_from_aging": _gen_overdue_interest_and_provision,
    "credit_control_remedial_actions_table": _gen_credit_control_actions,
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
        q["topic"] = "Debtors age analysis"
        q["grade"] = "11"
        out.append(q)
    return out
