"""
Grade 11 Accounting: Accounting Equation (Partnerships & Year-End Adjustments)
Strictly aligned with South African National Curriculum Standards for Grade 11 Accounting.
Zero "Ltd" or company share capital items — 100% Partnership and Sole Trader entities.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "partnership_capital_and_drawings_aol",
    "partnership_current_account_appropriations_aol",
    "year_end_accruals_and_prepayments_aol",
    "depreciation_and_asset_disposal_aol",
    "control_accounts_and_bad_debts_aol",
]

PARTNERSHIPS = [
    ("Mokoena & Dlamini Traders", "S. Mokoena", "L. Dlamini"),
    ("Naidoo & Van Wyk Partnership", "R. Naidoo", "K. van Wyk"),
    ("Khumalo & Botha Outfitters", "B. Khumalo", "J. Botha"),
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_capital_and_drawings_aol(r: random.Random) -> Dict[str, Any]:
    firm, p1, p2 = r.choice(PARTNERSHIPS)
    cap_veh = r.randint(140, 220) * 1000
    draw_stock = r.randint(4, 9) * 1000

    headers = ["Transaction", "Account Debited", "Account Credited", "Assets Effect (R)", "Owner's Equity Effect (R)", "Liabilities Effect (R)"]
    rows = [
        [f"Partner {p1} contributed a delivery vehicle worth R{cap_veh:,} as additional capital", "{r0_c1}", f"Capital: {p1}", "{r0_c3}", f"+{cap_veh}", "0"],
        [f"Partner {p2} took trading stock costing R{draw_stock:,} for personal use", f"Drawings: {p2}", "{r1_c2}", f"-{draw_stock}", "{r1_c4}", "0"],
    ]
    correct_map = {
        "r0_c1": "Vehicles",
        "r0_c3": f"+{cap_veh}",
        "r1_c2": "Trading Stock",
        "r1_c4": f"-{draw_stock}",
    }
    worked = (
        f"**Partnership Capital & Drawings on the Accounting Equation ({firm})**\n\n"
        f"- **Capital contribution of vehicle (`R{cap_veh:,}`)**: Debit **Vehicles** (`Assets +{cap_veh}`), Credit **Capital: {p1}** (`Owner's Equity +{cap_veh}`).\n"
        f"- **Drawings of stock (`R{draw_stock:,}`)**: Debit **Drawings: {p2}** (`Owner's Equity -{draw_stock}`), Credit **Trading Stock** (`Assets -{draw_stock}`)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "partnership_capital_and_drawings_aol",
        "question_text": (
            f"Analyse the effect of the following partnership transactions of **{firm}** on the Accounting Equation (`A = OE + L`)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Capital contributions increase Owner's Equity, whereas partner drawings decrease Owner's Equity.",
            "Include the `+` or `-` sign before the Rand amount in the Assets and Owner's Equity columns.",
            worked,
        ),
    }


def _gen_appropriations_aol(r: random.Random) -> Dict[str, Any]:
    firm, p1, p2 = r.choice(PARTNERSHIPS)
    sal = r.randint(120, 180) * 1000
    draw_close = r.randint(35, 65) * 1000

    headers = ["Year-End Partnership Entry", "Account Debited", "Account Credited", "Assets (R)", "Owner's Equity (R)", "Liabilities (R)"]
    rows = [
        [f"Credited partner {p1} with annual partner's salary of R{sal:,}", f"Salary: {p1}", f"Current Account: {p1}", "{r0_c3}", "{r0_c4}", "0"],
        [f"Transferred {p2}'s Drawings of R{draw_close:,} to their Current Account at year-end", f"Current Account: {p2}", f"Drawings: {p2}", "0", "{r1_c4}", "{r1_c5}"],
    ]
    correct_map = {
        "r0_c3": "0",
        "r0_c4": "0",
        "r1_c4": "0",
        "r1_c5": "0",
    }
    worked = (
        f"**Partnership Appropriations & Closing Transfers ({firm})**\n\n"
        f"- Both entries reallocate equity between internal partnership equity accounts (`Salary` / `Drawings` / `Current Account`).\n"
        f"- Neither Assets nor Liabilities change (`0`), and total Owner's Equity remains unchanged (`0` net effect: `-OE` and `+OE` of equal amount)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "partnership_current_account_appropriations_aol",
        "question_text": (
            f"Complete the **Net Accounting Equation Effect** (`0` where +OE and -OE offset each other) for **{firm}**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Internal transfers between Owner's Equity accounts (Drawings, Partner Salaries, Appropriation, Current Accounts) have a net zero effect on total Owner's Equity.",
            "Enter 0 in each cell where the transaction only shifts balances within Owner's Equity.",
            worked,
        ),
    }


def _gen_accruals_and_prepayments_aol(r: random.Random) -> Dict[str, Any]:
    firm, _, _ = r.choice(PARTNERSHIPS)
    prepaid = r.randint(6, 14) * 1000
    accrued_exp = r.randint(5, 11) * 1000
    inc_adv = r.randint(4, 9) * 1000

    headers = ["Year-End Adjustment", "Account Debited", "Account Credited", "Assets Effect", "Owner's Equity Effect", "Liabilities Effect"]
    rows = [
        [f"Insurance of R{prepaid:,} was paid in advance for the next financial year", "Prepaid Expenses", "Insurance", "{r0_c3}", f"+{prepaid}", "0"],
        [f"Water and electricity of R{accrued_exp:,} is still owing at year-end", "Water and Electricity", "Accrued Expenses", "0", f"-{accrued_exp}", "{r1_c5}"],
        [f"Rent income of R{inc_adv:,} was received in advance for March next year", "Rent Income", "Income Received in Advance", "0", "{r2_c4}", f"+{inc_adv}"],
    ]
    correct_map = {
        "r0_c3": f"+{prepaid}",
        "r1_c5": f"+{accrued_exp}",
        "r2_c4": f"-{inc_adv}",
    }
    worked = (
        f"**Year-End Accruals & Prepayments ({firm})**\n\n"
        f"- **Prepaid Expenses (`R{prepaid:,}`)**: Creates a Current Asset (`+{prepaid}`) and reduces Insurance expense (`OE +{prepaid}`).\n"
        f"- **Accrued Expenses (`R{accrued_exp:,}`)**: Increases expense (`OE -{accrued_exp}`) and creates a Current Liability (`+{accrued_exp}`).\n"
        f"- **Income Received in Advance (`R{inc_adv:,}`)**: Reduces current year Rent Income (`OE -{inc_adv}`) and creates a Current Liability (`+{inc_adv}`)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "year_end_accruals_and_prepayments_aol",
        "question_text": (
            f"Complete the Accounting Equation analysis for the year-end adjustments of **{firm}** (include `+` or `-` signs)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Prepaid expenses are Current Assets; Accrued expenses and Income received in advance are Current Liabilities.",
            "Include the `+` or `-` sign before the number.",
            worked,
        ),
    }


def _gen_depreciation_and_disposal_aol(r: random.Random) -> Dict[str, Any]:
    firm, _, _ = r.choice(PARTNERSHIPS)
    depr = r.randint(15, 32) * 1000
    cv_sold = r.randint(40, 75) * 1000

    headers = ["Adjustment", "Account Debited", "Account Credited", "Assets Effect", "Owner's Equity Effect", "Liabilities Effect"]
    rows = [
        [f"Recorded annual depreciation of R{depr:,} on equipment", "Depreciation", "Accumulated Depreciation on Equipment", "{r0_c3}", "{r0_c4}", "0"],
        [f"Sold old equipment at its exact carrying value of R{cv_sold:,} on credit", "Debtors for Equipment", "Asset Disposal", "{r1_c3}", "0", "{r1_c5}"],
    ]
    correct_map = {
        "r0_c3": f"-{depr}",
        "r0_c4": f"-{depr}",
        "r1_c3": "0",
        "r1_c5": "0",
    }
    worked = (
        f"**Depreciation & Disposal on the Accounting Equation ({firm})**\n\n"
        f"- **Depreciation (`R{depr:,}`)**: Increases Accumulated Depreciation (negative asset: `Assets -{depr}`) and increases Depreciation expense (`OE -{depr}`).\n"
        f"- **Selling asset at exact carrying value**: Replaces fixed asset carrying value (`-{cv_sold}`) with receivable (`+{cv_sold}`), so net Assets effect is `0` and Liabilities is `0`."
    )
    return {
        "question_type": "table_fill",
        "subskill": "depreciation_and_asset_disposal_aol",
        "question_text": (
            f"Determine the effect on **Assets**, **Owner's Equity**, and **Liabilities** for **{firm}**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Accumulated Depreciation is a negative asset (contra-asset), so crediting it reduces Total Assets.",
            "Enter `-` followed by the depreciation amount for Row 1, and `0` where asset exchange leaves total assets unchanged.",
            worked,
        ),
    }


def _gen_control_and_bad_debts_aol(r: random.Random) -> Dict[str, Any]:
    firm, _, _ = r.choice(PARTNERSHIPS)
    bad = r.randint(3, 7) * 1000
    prov_dec = r.randint(1, 3) * 1000

    headers = ["Transaction", "Account Debited", "Account Credited", "Assets Effect", "Owner's Equity Effect", "Liabilities Effect"]
    rows = [
        [f"Wrote off an insolvent debtor's balance of R{bad:,} as irrecoverable", "Bad Debts", "Debtors Control", "{r0_c3}", f"-{bad}", "0"],
        [f"Decreased the Provision for Bad Debts by R{prov_dec:,} at year-end", "Provision for Bad Debts", "Provision for Bad Debts Adjustment", "{r1_c3}", "{r1_c4}", "0"],
    ]
    correct_map = {
        "r0_c3": f"-{bad}",
        "r1_c3": f"+{prov_dec}",
        "r1_c4": f"+{prov_dec}",
    }
    worked = (
        f"**Bad Debts & Provision Adjustment ({firm})**\n\n"
        f"- **Bad debts written off (`R{bad:,}`)**: Decreases Debtors Control (`Assets -{bad}`) and increases Bad Debts expense (`OE -{bad}`).\n"
        f"- **Decrease in Provision for Bad Debts (`R{prov_dec:,}`)**: Reduces negative asset (`Assets +{prov_dec}`) and creates adjustment income (`OE +{prov_dec}`)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "control_accounts_and_bad_debts_aol",
        "question_text": (
            f"Complete the Accounting Equation table for **{firm}** (include `+` or `-` signs)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Provision for Bad Debts is a contra-asset (negative asset). Decreasing a negative asset increases Net Trade Receivables (Assets +).",
            "Enter `-{bad}` for Row 1 Assets, and `+{prov_dec}` for Row 2 Assets and Owner's Equity.",
            worked,
        ),
    }


_BUILDERS = {
    "partnership_capital_and_drawings_aol": _gen_capital_and_drawings_aol,
    "partnership_current_account_appropriations_aol": _gen_appropriations_aol,
    "year_end_accruals_and_prepayments_aol": _gen_accruals_and_prepayments_aol,
    "depreciation_and_asset_disposal_aol": _gen_depreciation_and_disposal_aol,
    "control_accounts_and_bad_debts_aol": _gen_control_and_bad_debts_aol,
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
        q["topic"] = "Accounting equation"
        q["grade"] = "11"
        out.append(q)
    return out
