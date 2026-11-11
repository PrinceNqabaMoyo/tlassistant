"""
Grade 12 Accounting: The Accounting Equation for Companies (A = OE + L)
Strictly aligned with South African National Curriculum Standards for Grade 12 Accounting.
100% Public and Private Company entities (Ltd / (Pty) Ltd) — Share Capital, Share Buybacks,
SARS (Income Tax), Interim & Final Dividends, Directors' & Audit Fees, and Company Adjustments.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "share_issue_and_capital_aol",
    "share_repurchase_buyback_aol",
    "provisional_and_final_income_tax_aol",
    "interim_and_final_dividends_aol",
    "directors_and_audit_fees_accruals_aol",
]

COMPANIES = [
    "Protea Holdings Ltd",
    "Highveld Logistics Ltd",
    "Ubuntu Pharmaceuticals Ltd",
    "Zululand Industrials Ltd",
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_share_issue_aol(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    shares = r.choice([100000, 150000, 200000])
    issue_price = r.choice([8, 10, 12])
    tot_issue = shares * issue_price
    equip_shares = r.randint(150, 300) * 1000

    headers = ["Company Transaction", "Account Debited", "Account Credited", "Assets (A)", "Shareholders' Equity (OE)", "Liabilities (L)"]
    rows = [
        [f"Issued {shares:,} new ordinary shares at R{issue_price} each for cash", "Bank", "{r0_c2}", "{r0_c3}", f"+{tot_issue}", "0"],
        [f"Issued ordinary shares worth R{equip_shares:,} to acquire new factory machinery", "{r1_c1}", "Ordinary Share Capital", f"+{equip_shares}", "{r1_c4}", "0"],
    ]
    correct_map = {
        "r0_c2": "Ordinary Share Capital",
        "r0_c3": f"+{tot_issue}",
        "r1_c1": "Equipment",
        "r1_c4": f"+{equip_shares}",
    }
    worked = (
        f"**Company Share Issue on the Accounting Equation ({co})**\n\n"
        f"- **Cash share issue (`{shares:,} × R{issue_price} = R{tot_issue:,}`)**: Debit **Bank** (`Assets +{tot_issue}`), Credit **Ordinary Share Capital** (`Equity +{tot_issue}`).\n"
        f"- **Shares issued for equipment (`R{equip_shares:,}`)**: Debit **Equipment** (`Assets +{equip_shares}`), Credit **Ordinary Share Capital** (`Equity +{equip_shares}`)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "share_issue_and_capital_aol",
        "question_text": f"Complete the Accounting Equation analysis for the share issue transactions of **{co}** (include `+` or `-` signs).",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Issuing ordinary shares increases both Company Assets (Bank or Equipment) and Shareholders' Equity (Ordinary Share Capital).",
            "Enter Ordinary Share Capital in Row 1 and Equipment in Row 2, with `+` signs before the Rand amounts.",
            worked,
        ),
    }


def _gen_share_buyback_aol(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    rep_shares = r.choice([20000, 30000, 40000])
    avg_price = r.choice([6, 8, 10])
    buyback_price = avg_price + r.choice([2, 3])
    osc_part = rep_shares * avg_price
    ri_part = rep_shares * (buyback_price - avg_price)
    tot_bank = osc_part + ri_part

    headers = ["Share Buyback Component", "Account Debited", "Account Credited", "Assets (A)", "Shareholders' Equity (OE)", "Liabilities (L)"]
    rows = [
        [f"Repurchased {rep_shares:,} shares: Average issue price portion (R{avg_price} per share)", "{r0_c1}", "Bank", f"-{osc_part}", "{r0_c4}", "0"],
        [f"Repurchased {rep_shares:,} shares: Premium above average price (R{buyback_price - avg_price} per share)", "{r1_c1}", "Bank", f"-{ri_part}", f"-{ri_part}", "0"],
        [f"Combined net effect of buying back {rep_shares:,} shares at R{buyback_price} each", "OSC & Retained Income", "Bank", "{r2_c3}", "{r2_c4}", "0"],
    ]
    correct_map = {
        "r0_c1": "Ordinary Share Capital",
        "r0_c4": f"-{osc_part}",
        "r1_c1": "Retained Income",
        "r2_c3": f"-{tot_bank}",
        "r2_c4": f"-{tot_bank}",
    }
    worked = (
        f"**Share Repurchase (Buyback) on the Accounting Equation ({co})**\n\n"
        f"- **Average Issue Price Portion (`{rep_shares:,} × R{avg_price} = R{osc_part:,}`)**: Debit **Ordinary Share Capital** (`Equity -{osc_part}`), Credit **Bank** (`Assets -{osc_part}`).\n"
        f"- **Amount Above Average Price (`{rep_shares:,} × R{buyback_price - avg_price} = R{ri_part:,}`)**: Debit **Retained Income** (`Equity -{ri_part}`), Credit **Bank** (`Assets -{ri_part}`).\n"
        f"- **Total Effect**: `Assets -{tot_bank}`, `Shareholders' Equity -{tot_bank}`."
    )
    return {
        "question_type": "table_fill",
        "subskill": "share_repurchase_buyback_aol",
        "question_text": (
            f"**{co}** repurchased **{rep_shares:,} ordinary shares** at **R{buyback_price} per share** by EFT "
            f"(the average issue price was **R{avg_price} per share**). Complete the Accounting Equation analysis."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "In a share buyback, Ordinary Share Capital is reduced by the average issue price per share, and Retained Income is reduced by the amount paid above average price.",
            "Enter Ordinary Share Capital for Row 1, Retained Income for Row 2, and `-` followed by the total cash paid in Row 3.",
            worked,
        ),
    }


def _gen_income_tax_aol(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    prov_tax = r.randint(180, 280) * 1000
    annual_tax = prov_tax * 2 + r.randint(20, 45) * 1000

    headers = ["Company Tax Transaction", "Account Debited", "Account Credited", "Assets (A)", "Shareholders' Equity (OE)", "Liabilities (L)"]
    rows = [
        [f"Paid first provisional income tax of R{prov_tax:,} to SARS by EFT", "{r0_c1}", "Bank", f"-{prov_tax}", "0", f"-{prov_tax}"],
        [f"Recorded total annual income tax assessment of R{annual_tax:,} at year-end", "{r1_c1}", "SARS: Income Tax", "0", "{r1_c4}", "{r1_c5}"],
    ]
    correct_map = {
        "r0_c1": "SARS: Income Tax",
        "r1_c1": "Income Tax",
        "r1_c4": f"-{annual_tax}",
        "r1_c5": f"+{annual_tax}",
    }
    worked = (
        f"**Provisional & Annual Income Tax ({co})**\n\n"
        f"- **Provisional tax payment (`R{prov_tax:,}`)**: Debit **SARS: Income Tax**, Credit **Bank** (`Assets -{prov_tax}`, `Liabilities -{prov_tax}`).\n"
        f"- **Annual tax assessment (`R{annual_tax:,}`)**: Debit **Income Tax** (`Equity -{annual_tax}`), Credit **SARS: Income Tax** (`Liabilities +{annual_tax}`)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "provisional_and_final_income_tax_aol",
        "question_text": f"Complete the Accounting Equation analysis for the income tax transactions of **{co}**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Paying SARS reduces Bank and reduces the SARS liability (`SARS: Income Tax`); recording the annual tax assessment increases the `Income Tax` expense (reducing Equity) and increases the `SARS: Income Tax` liability.",
            "Distinguish carefully between the nominal expense account (`Income Tax`) and the balance sheet liability account (`SARS: Income Tax`).",
            worked,
        ),
    }


def _gen_dividends_aol(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    interim_div = r.randint(120, 200) * 1000
    final_div = r.randint(160, 260) * 1000

    headers = ["Dividend Transaction", "Account Debited", "Account Credited", "Assets (A)", "Shareholders' Equity (OE)", "Liabilities (L)"]
    rows = [
        [f"Paid interim dividends of R{interim_div:,} to shareholders via EFT", "Dividends on Ordinary Shares", "Bank", "{r0_c3}", "{r0_c4}", "0"],
        [f"Declared final dividends of R{final_div:,} at year-end (to be paid next year)", "Dividends on Ordinary Shares", "{r1_c2}", "0", f"-{final_div}", "{r1_c5}"],
    ]
    correct_map = {
        "r0_c3": f"-{interim_div}",
        "r0_c4": f"-{interim_div}",
        "r1_c2": "Shareholders for Dividends",
        "r1_c5": f"+{final_div}",
    }
    worked = (
        f"**Interim vs Final Dividends on the Accounting Equation ({co})**\n\n"
        f"- **Interim dividend paid (`R{interim_div:,}`)**: Debit **Dividends on Ordinary Shares** (`Equity -{interim_div}`), Credit **Bank** (`Assets -{interim_div}`).\n"
        f"- **Final dividend declared (`R{final_div:,}`)**: Debit **Dividends on Ordinary Shares** (`Equity -{final_div}`), Credit **Shareholders for Dividends** (`Liabilities +{final_div}`)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "interim_and_final_dividends_aol",
        "question_text": f"Analyse the interim and final dividend transactions of **{co}** on the Accounting Equation.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Interim dividends are paid immediately out of Bank (`Assets -`), whereas Final dividends declared at year-end create a current liability (`Shareholders for Dividends`).",
            "Include `+` or `-` signs before the Rand amounts.",
            worked,
        ),
    }


def _gen_directors_and_audit_fees_aol(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    dir_fee = r.randint(45, 85) * 1000
    audit_fee = r.randint(25, 55) * 1000

    headers = ["Company Adjustment", "Account Debited", "Account Credited", "Assets (A)", "Shareholders' Equity (OE)", "Liabilities (L)"]
    rows = [
        [f"Directors' fees of R{dir_fee:,} for February are still unpaid at year-end", "{r0_c1}", "Accrued Expenses", "0", "{r0_c4}", f"+{dir_fee}"],
        [f"Paid external auditors R{audit_fee:,} by EFT for the annual statutory audit", "{r1_c1}", "Bank", f"-{audit_fee}", f"-{audit_fee}", "{r1_c5}"],
    ]
    correct_map = {
        "r0_c1": "Directors' Fees",
        "r0_c4": f"-{dir_fee}",
        "r1_c1": "Audit Fees",
        "r1_c5": "0",
    }
    worked = (
        f"**Directors' Fees & Audit Fees ({co})**\n\n"
        f"- **Accrued Directors' Fees (`R{dir_fee:,}`)**: Debit **Directors' Fees** (`Equity -{dir_fee}`), Credit **Accrued Expenses** (`Liabilities +{dir_fee}`).\n"
        f"- **Audit Fees Paid (`R{audit_fee:,}`)**: Debit **Audit Fees** (`Equity -{audit_fee}`), Credit **Bank** (`Assets -{audit_fee}`, `Liabilities 0`)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "directors_and_audit_fees_accruals_aol",
        "question_text": f"Complete the Accounting Equation table for **{co}**.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Directors' Fees and Audit Fees are company operating expenses that reduce Shareholders' Equity.",
            "Enter Directors' Fees and `-{dir_fee}` in Row 1, and Audit Fees and `0` in Row 2.",
            worked,
        ),
    }


_BUILDERS = {
    "share_issue_and_capital_aol": _gen_share_issue_aol,
    "share_repurchase_buyback_aol": _gen_share_buyback_aol,
    "provisional_and_final_income_tax_aol": _gen_income_tax_aol,
    "interim_and_final_dividends_aol": _gen_dividends_aol,
    "directors_and_audit_fees_accruals_aol": _gen_directors_and_audit_fees_aol,
}


def generate(
    seed: Optional[int] = None,
    count: int = 1,
    mode: str = "compound",
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    **kwargs,
) -> List[Dict[str, Any]]:
    r = random.Random(seed)
    out: List[Dict[str, Any]] = []
    for _ in range(count):
        chosen = subskill if (subskill and subskill in _BUILDERS) else r.choice(SUBSKILLS)
        q = _BUILDERS[chosen](r)
        q["subskill"] = chosen
        q["topic"] = "The accounting equation"
        q["grade"] = "12"
        out.append(q)
    return out


def generate_questions(
    count: int = 1,
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    return generate(seed=seed, count=count, subskill=subskill, **kwargs)
