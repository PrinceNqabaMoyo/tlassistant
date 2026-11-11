"""
Grade 11 Accounting: Ethics (Partnership Ethics, Fiduciary Duty & King Code Principles)
Strictly aligned with South African National Curriculum Standards for Grade 11 Accounting.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "partnership_fiduciary_duty_and_good_faith",
    "conflict_of_interest_in_partnership_procurement",
    "fairness_in_partnership_agreement_and_remuneration",
    "ethical_treatment_of_assets_and_drawings",
    "king_code_governance_pillars_in_partnerships",
    "ethical_reporting_and_tax_compliance",
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_fiduciary_duty(r: random.Random) -> Dict[str, Any]:
    headers = ["Partner Scenario", "Ethical Evaluation (Ethical / Unethical)", "Governing Partnership Principle (Utmost Good Faith / Mutual Agency / Joint & Several Liability)"]
    rows = [
        ["Partner A secretly diverts a partnership customer contract to their private side business", "{r0_c1}", "{r0_c2}"],
        ["Partner B signs a supplier contract on behalf of the partnership within agreed authority", "{r1_c1}", "{r1_c2}"],
        ["Personal assets of both partners can be attached if the partnership cannot pay its business debts", "Ethical", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c1": "Unethical",
        "r0_c2": "Utmost Good Faith",
        "r1_c1": "Ethical",
        "r1_c2": "Mutual Agency",
        "r2_c2": "Joint & Several Liability",
    }
    worked = (
        "**Partnership Fiduciary Duty & Legal Principles**\n\n"
        "- Secretly diverting partnership business is **Unethical** and breaches **Utmost Good Faith**.\n"
        "- Signing an authorised supplier contract is **Ethical** and reflects **Mutual Agency**.\n"
        "- Partners being personally liable for unpaid partnership debts is **Joint & Several Liability**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "partnership_fiduciary_duty_and_good_faith",
        "question_text": "Complete the partnership ethics and legal principles table using the options in the column headers.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Partners owe each other a fiduciary duty of Utmost Good Faith, act as agents for the firm (Mutual Agency), and share unlimited liability (Joint & Several Liability).",
            "Match each scenario to Ethical/Unethical and the corresponding principle.",
            worked,
        ),
    }


def _gen_conflict_of_interest(r: random.Random) -> Dict[str, Any]:
    mkt_price = r.randint(120, 160) * 1000
    inflated = mkt_price + r.randint(25, 45) * 1000
    overcharge = inflated - mkt_price

    headers = ["Procurement Ethics Analysis", "Answer / Amount"]
    rows = [
        [f"Market price from independent supplier (R{mkt_price:,}) vs price paid to Partner's relative (R{inflated:,}) — Overcharge (R)", "{r0_c1}"],
        ["Ethical issue identified (Conflict of Interest / Normal Trade Discount)", "{r1_c1}"],
        ["Required control before awarding contract (Full Disclosure & Partner Approval / No Action Needed)", "{r2_c1}"],
    ]
    correct_map = {
        "r0_c1": overcharge,
        "r1_c1": "Conflict of Interest",
        "r2_c1": "Full Disclosure & Partner Approval",
    }
    worked = (
        f"**Conflict of Interest in Partnership Procurement**\n\n"
        f"- **Overcharge to Partnership**: `R{inflated:,} - R{mkt_price:,} = R{overcharge:,}`\n"
        f"- **Ethical Issue**: **Conflict of Interest**\n"
        f"- **Required Control**: **Full Disclosure & Partner Approval** (plus obtaining at least three competitive quotes)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "conflict_of_interest_in_partnership_procurement",
        "question_text": (
            f"Partner X awarded a contract of **R{inflated:,}** to a family member without informing Partner Y, even though "
            f"an independent supplier quoted **R{mkt_price:,}** for identical goods. Complete the analysis."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Awarding contracts to related parties at inflated prices without informing co-partners is a classic Conflict of Interest.",
            "Subtract the market quote from the inflated contract price, then select the correct ethical issue and control.",
            worked,
        ),
    }


def _gen_fairness_in_remuneration(r: random.Random) -> Dict[str, Any]:
    headers = ["Partnership Agreement Clause", "Purpose (Reward Active Daily Management / Reward Capital Risk / Encourage Profit Growth)"]
    rows = [
        ["Monthly partner salary paid to the managing partner who works 45 hours a week", "{r0_c1}"],
        ["Interest on Capital calculated at 10% p.a. on each partner's capital balance", "{r1_c1}"],
        ["Annual performance bonus paid to the partner who exceeded sales targets", "{r2_c1}"],
    ]
    correct_map = {
        "r0_c1": "Reward Active Daily Management",
        "r1_c1": "Reward Capital Risk",
        "r2_c1": "Encourage Profit Growth",
    }
    worked = (
        "**Fairness in Partnership Remuneration**\n\n"
        "- **Partner's Salary**: **Reward Active Daily Management** (time and skill contributed).\n"
        "- **Interest on Capital**: **Reward Capital Risk** (compensates partners who invest larger capital amounts).\n"
        "- **Performance Bonus**: **Encourage Profit Growth**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "fairness_in_partnership_agreement_and_remuneration",
        "question_text": "Match each appropriation item in a Partnership Agreement to its ethical and economic purpose.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Because partners contribute different amounts of time, skill, and capital, the Partnership Agreement uses salaries, interest, and bonuses to ensure fairness before splitting remaining profits.",
            "Match each clause to the correct purpose in brackets.",
            worked,
        ),
    }


def _gen_ethical_treatment_of_assets_and_drawings(r: random.Random) -> Dict[str, Any]:
    headers = ["Partner Action", "Wrong Account Used by Partner", "Correct Account Required by GAAP (Business Entity Rule)"]
    rows = [
        ["Partner paid personal home electricity bill using business EFT and recorded it under Water & Electricity", "Water and Electricity", "{r0_c2}"],
        ["Partner took merchandise from the storeroom for family use and included it in Stock Deficit", "Trading Stock Deficit", "{r1_c2}"],
        ["Partner used business delivery fuel for a private holiday and recorded it under Fuel Expense", "Fuel Expense", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c2": "Drawings",
        "r1_c2": "Drawings",
        "r2_c2": "Drawings",
    }
    worked = (
        "**Ethical Treatment of Partner Drawings (Business Entity Principle)**\n\n"
        "- All three personal expenses/withdrawals must be debited to **Drawings** (reducing that specific partner's equity) and never disguised as partnership operating expenses, which would unfairly reduce the co-partner's profit share and evade income tax."
    )
    return {
        "question_type": "table_fill",
        "subskill": "ethical_treatment_of_assets_and_drawings",
        "question_text": (
            "In each case below, a partner disguised personal consumption as a business expense. "
            "Enter the **Correct Account** that must be debited (`Drawings`)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Under the Business Entity principle, personal expenses of a partner must never be charged to partnership expense accounts.",
            "Enter Drawings as the correct account to be debited in each row.",
            worked,
        ),
    }


def _gen_king_code_pillars(r: random.Random) -> Dict[str, Any]:
    headers = ["Governance Practice in the Partnership", "King Code Pillar (Transparency / Accountability / Responsibility / Discipline)"]
    rows = [
        ["Sharing full, accurate monthly financial statements and bank statements with all partners", "{r0_c1}"],
        ["Being able to explain and justify every expenditure decision to co-partners and SARS", "{r1_c1}"],
        ["Adhering strictly to GAAP, tax laws, and the signed Partnership Agreement", "{r2_c1}"],
        ["Implementing environmentally sustainable waste disposal and fair labour practices", "{r3_c1}"],
    ]
    correct_map = {
        "r0_c1": "Transparency",
        "r1_c1": "Accountability",
        "r2_c1": "Discipline",
        "r3_c1": "Responsibility",
    }
    worked = (
        "**King Code Governance Pillars**\n\n"
        "- Open, honest information sharing $\\rightarrow$ **Transparency**\n"
        "- Answering for actions and decisions $\\rightarrow$ **Accountability**\n"
        "- Obeying laws, standards, and internal rules $\\rightarrow$ **Discipline**\n"
        "- Caring for community, staff, and environment $\\rightarrow$ **Responsibility**"
    )
    return {
        "question_type": "table_fill",
        "subskill": "king_code_governance_pillars_in_partnerships",
        "question_text": "Match each partnership governance practice to the correct **King Code** pillar.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 8,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Recall the four core governance pillars: Transparency, Accountability, Discipline, and Responsibility.",
            "Match open reporting to Transparency, justifying decisions to Accountability, rule-following to Discipline, and social/environmental care to Responsibility.",
            worked,
        ),
    }


def _gen_ethical_reporting_and_tax(r: random.Random) -> Dict[str, Any]:
    headers = ["Unethical Manipulation Attempt", "Effect on Reported Net Profit (Overstated / Understated)", "GAAP Principle Violated (Prudence / Historical Cost / Matching)"]
    rows = [
        ["Omitting R25,000 of accrued expenses at year-end to qualify for a bank loan", "{r0_c1}", "{r0_c2}"],
        ["Refusing to write off R14,000 owed by an insolvent debtor to make assets look higher", "{r1_c1}", "{r1_c2}"],
        ["Recording Land & Buildings at an unverified guesstimate instead of original purchase price", "Overstated", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c1": "Overstated",
        "r0_c2": "Matching",
        "r1_c1": "Overstated",
        "r1_c2": "Prudence",
        "r2_c2": "Historical Cost",
    }
    worked = (
        "**Ethical Financial Reporting & GAAP Compliance**\n\n"
        "- **Omitting accrued expenses**: **Overstated** profit; violates **Matching**.\n"
        "- **Refusing to write off bad debts**: **Overstated** profit and assets; violates **Prudence**.\n"
        "- **Inflating property value without cost basis**: Violates **Historical Cost**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "ethical_reporting_and_tax_compliance",
        "question_text": "Analyse the ethical reporting violations below by completing the table.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Leaving out expenses or bad debts artificially inflates (overstates) Net Profit.",
            "Identify whether profit is Overstated or Understated and which GAAP principle is violated.",
            worked,
        ),
    }


_BUILDERS = {
    "partnership_fiduciary_duty_and_good_faith": _gen_fiduciary_duty,
    "conflict_of_interest_in_partnership_procurement": _gen_conflict_of_interest,
    "fairness_in_partnership_agreement_and_remuneration": _gen_fairness_in_remuneration,
    "ethical_treatment_of_assets_and_drawings": _gen_ethical_treatment_of_assets_and_drawings,
    "king_code_governance_pillars_in_partnerships": _gen_king_code_pillars,
    "ethical_reporting_and_tax_compliance": _gen_ethical_reporting_and_tax,
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
        q["topic"] = "Ethics"
        q["grade"] = "11"
        out.append(q)
    return out
