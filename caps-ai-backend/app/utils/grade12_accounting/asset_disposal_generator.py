"""
Grade 12 Accounting: Disposal of Tangible Assets (Companies)
Strictly aligned with South African National Curriculum Standards for Grade 12 Accounting (Term 2).
Includes Company Asset Disposal T-account, Pro-rata Diminishing Balance & R1 Residual Value rules,
Fixed Assets Note (Note 3) Disposal & Additions Back-Calculation, and Cash Flow Proceeds from Sale of Fixed Assets.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "company_diminishing_balance_pro_rata_disposal",
    "r1_residual_value_rule_and_disposal",
    "company_asset_disposal_taccount",
    "fixed_assets_note_disposal_backcalc",
    "cash_flow_proceeds_from_disposal_at_carrying_value",
    "asset_disposal_audit_and_director_governance",
]

COMPANIES = [
    "Protea Logistics Ltd",
    "Highveld Freight Ltd",
    "Ubuntu Manufacturing Ltd",
    "Zululand Engineering Ltd",
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_diminishing_pro_rata_disposal(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    cost = 300000
    open_acc = 108000
    open_cv = cost - open_acc
    months = r.choice([6, 9])
    curr_depr = int(open_cv * 0.20 * (months / 12))
    tot_acc = open_acc + curr_depr
    cv_sale = cost - tot_acc

    headers = ["Company Asset Disposal Schedule (20% p.a. Diminishing Balance)", "Amount (R)"]
    rows = [
        ["Original cost price of delivery truck", f"R{cost:,}"],
        ["Accumulated depreciation at beginning of year", f"(R{open_acc:,})"],
        ["Carrying value at beginning of year", "{r2_c1}"],
        [f"Current year pro-rata depreciation ({months} months at 20% p.a. on carrying value)", "{r3_c1}"],
        ["Total accumulated depreciation at date of disposal", "{r4_c1}"],
        ["Carrying value at date of disposal", "{r5_c1}"],
    ]
    correct_map = {
        "r2_c1": open_cv,
        "r3_c1": curr_depr,
        "r4_c1": tot_acc,
        "r5_c1": cv_sale,
    }
    worked = (
        f"**Diminishing Balance Pro-Rata Disposal ({co})**\n\n"
        f"- **Opening Carrying Value**: `R{cost:,} - R{open_acc:,} = R{open_cv:,}`\n"
        f"- **Pro-Rata Depreciation ({months}/12)**: `R{open_cv:,} × 20% × ({months}/12) = R{curr_depr:,}`\n"
        f"- **Total Accumulated Depreciation at Sale**: `R{open_acc:,} + R{curr_depr:,} = R{tot_acc:,}`\n"
        f"- **Carrying Value at Sale**: `R{cost:,} - R{tot_acc:,} = R{cv_sale:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "company_diminishing_balance_pro_rata_disposal",
        "question_text": (
            f"**{co}** sold a delivery truck **{months} months** into the financial year. Depreciation is provided at **20% p.a. on the diminishing-balance method**. Complete the schedule."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Under the diminishing-balance method, current year depreciation is calculated on the Opening Carrying Value (`Cost - Opening Acc Dep`), not on Cost.",
            f"Calculate Opening Carrying Value first, then multiply by 20% and by {months}/12.",
            worked,
        ),
    }


def _gen_r1_residual_rule(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    cost = r.choice([120000, 150000, 180000])
    open_acc = cost - r.choice([8000, 10000, 12000])
    open_cv = cost - open_acc
    max_depr_allowed = open_cv - 1
    selling_price = r.choice([15000, 22000, 28000])
    profit_on_sale = selling_price - 1

    headers = ["Fully Depreciated Asset (R1 Rule) Disposal", "Amount (R)"]
    rows = [
        [f"Opening Carrying Value (Cost R{cost:,} less Opening Acc Dep R{open_acc:,})", f"R{open_cv:,}"],
        ["Maximum current depreciation allowed before sale (leaving R1 carrying value)", "{r1_c1}"],
        ["Carrying value at date of disposal (minimum nominal value)", "{r2_c1}"],
        [f"Profit on sale of asset when sold for R{selling_price:,}", "{r3_c1}"],
    ]
    correct_map = {
        "r1_c1": max_depr_allowed,
        "r2_c1": 1,
        "r3_c1": profit_on_sale,
    }
    worked = (
        f"**R1 Residual Carrying Value Rule & Disposal ({co})**\n\n"
        f"- Because an asset still in use cannot be depreciated below **R1**, current depreciation is capped at `R{open_cv:,} - R1 = R{max_depr_allowed:,}`.\n"
        f"- **Carrying Value at Disposal**: `R1`\n"
        f"- **Profit on Sale**: `R{selling_price:,} - R1 = R{profit_on_sale:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "r1_residual_value_rule_and_disposal",
        "question_text": (
            f"An old machine at **{co}** (Cost **R{cost:,}**, Opening Accumulated Depreciation **R{open_acc:,}**) would normally have annual depreciation of R30,000, "
            f"which exceeds its remaining carrying value. It is depreciated down to **R1** and then sold for **R{selling_price:,}**. Complete the table."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "When calculated annual depreciation exceeds an asset's remaining carrying value, depreciation is restricted so that Carrying Value equals R1.",
            "Subtract 1 from Opening Carrying Value for Row 2, enter 1 for Row 3, and subtract 1 from Selling Price for Row 4.",
            worked,
        ),
    }


def _gen_company_asset_disposal_taccount(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    cost = 450000
    acc_dep = 290000
    cv = cost - acc_dep
    loss = r.choice([12000, 18000, 25000])
    proceeds = cv - loss

    headers = ["Asset Disposal Account (General Ledger)", "Side (Debit / Credit)", "Amount (R)"]
    rows = [
        ["Equipment (Cost price transferred)", "Debit", f"R{cost:,}"],
        ["Accumulated Depreciation on Equipment (to date of sale)", "Credit", "{r1_c2}"],
        ["Bank / Debtors for Equipment (Proceeds)", "Credit", f"R{proceeds:,}"],
        ["Loss on Sale of Asset (balancing figure)", "Credit", "{r3_c2}"],
        ["Account Total (Debit = Credit)", "Both", "{r4_c2}"],
    ]
    correct_map = {
        "r1_c2": acc_dep,
        "r3_c2": loss,
        "r4_c2": cost,
    }
    worked = (
        f"**Company Asset Disposal T-Account ({co})**\n\n"
        f"- **Debit Equipment (Cost)**: `R{cost:,}`\n"
        f"- **Credit Accumulated Depreciation**: `R{acc_dep:,}`\n"
        f"- **Credit Bank (Proceeds)**: `R{proceeds:,}`\n"
        f"- **Credit Loss on Sale of Asset**: `R{cost:,} - R{acc_dep:,} - R{proceeds:,} = R{loss:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "company_asset_disposal_taccount",
        "question_text": (
            f"Complete the **Asset Disposal Account** for **{co}** given Cost **R{cost:,}**, "
            f"Accumulated Depreciation at sale **R{acc_dep:,}**, and Proceeds **R{proceeds:,}**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "A Loss on Sale of Asset appears on the Credit side of the Asset Disposal account because Proceeds + Accumulated Depreciation are less than Cost.",
            "Enter Accumulated Depreciation in Row 2, Loss on Sale in Row 4, and the total in Row 5.",
            worked,
        ),
    }


def _gen_fixed_assets_note_disposal_backcalc(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    open_cv = 1200000
    additions = r.choice([350000, 420000])
    depr = 190000
    close_cv = 1180000
    disp_cv = open_cv + additions - depr - close_cv

    headers = ["Note 3: Fixed / Tangible Assets Back-Calculation", "Amount (R)"]
    rows = [
        ["Carrying value at beginning of year", f"R{open_cv:,}"],
        ["Additions at cost during the year", f"R{additions:,}"],
        ["Disposals at carrying value (missing figure)", "{r2_c1}"],
        ["Depreciation for the year", f"(R{depr:,})"],
        ["Carrying value at end of year", f"R{close_cv:,}"],
    ]
    correct_map = {"r2_c1": disp_cv}
    worked = (
        f"**Back-Calculating Disposals at Carrying Value ({co})**\n\n"
        f"- Formula: `Opening CV + Additions - Disposals CV - Depreciation = Closing CV`\n"
        f"- **Disposals at Carrying Value**: `R{open_cv:,} + R{additions:,} - R{depr:,} - R{close_cv:,} = R{disp_cv:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "fixed_assets_note_disposal_backcalc",
        "question_text": (
            f"Calculate the missing **Disposals at Carrying Value** figure in **Note 3 (Fixed Assets)** of **{co}** (enter a positive Rand amount)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "In Note 3: `Opening CV + Additions - Disposals at CV - Depreciation = Closing CV`.",
            "Add Opening CV and Additions, subtract Depreciation and Closing CV.",
            worked,
        ),
    }


def _gen_cash_flow_proceeds_disposal(r: random.Random) -> Dict[str, Any]:
    co = r.choice(COMPANIES)
    disp_cost = 280000
    disp_acc = 175000
    disp_cv = disp_cost - disp_acc
    profit = r.choice([15000, 25000])
    cash_inflow = disp_cv + profit

    headers = ["Cash Flow from Investing Activities: Disposal of Fixed Assets", "Amount (R)"]
    rows = [
        [f"Carrying value of fixed assets disposed of (Cost R{disp_cost:,} less Acc Dep R{disp_acc:,})", "{r0_c1}"],
        [f"Add: Profit on sale of asset recorded in Income Statement (R{profit:,})", f"R{profit:,}"],
        ["Proceeds from sale of fixed assets (Cash Inflow in Cash Flow Statement)", "{r2_c1}"],
    ]
    correct_map = {
        "r0_c1": disp_cv,
        "r2_c1": cash_inflow,
    }
    worked = (
        f"**Cash Flow Proceeds from Disposal ({co})**\n\n"
        f"- **Carrying Value Disposed**: `R{disp_cost:,} - R{disp_acc:,} = R{disp_cv:,}`\n"
        f"- **Cash Proceeds**: `Carrying Value (R{disp_cv:,}) + Profit on Sale (R{profit:,}) = R{cash_inflow:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "cash_flow_proceeds_from_disposal_at_carrying_value",
        "question_text": (
            f"**{co}** disposed of equipment (Cost **R{disp_cost:,}**, Accumulated Depreciation **R{disp_acc:,}**) "
            f"at a **profit of R{profit:,}**. Calculate the Cash Flow Statement inflow from **Proceeds from sale of fixed assets**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "When an asset is sold at a profit, the cash proceeds received equal Carrying Value PLUS the Profit on Sale.",
            "Calculate Carrying Value in Row 1, then add the Profit on Sale to find Cash Proceeds in Row 3.",
            worked,
        ),
    }


def _gen_disposal_governance(r: random.Random) -> Dict[str, Any]:
    cv = 180000
    director_price = 95000
    loss_to_co = cv - director_price

    headers = ["Corporate Governance Audit of Asset Disposal", "Answer / Amount"]
    rows = [
        [f"Company vehicle (Carrying value & market value R{cv:,}) sold to a Director for R{director_price:,} — Loss suffered by company (R)", "{r0_c1}"],
        ["Governance breach identified (Self-Dealing & Conflict of Interest / Fair Market Disposal)", "{r1_c1}"],
        ["Required procedure before selling company assets (Board Approval & Independent Valuation / Verbal Decision by CEO)", "{r2_c1}"],
    ]
    correct_map = {
        "r0_c1": loss_to_co,
        "r1_c1": "Self-Dealing & Conflict of Interest",
        "r2_c1": "Board Approval & Independent Valuation",
    }
    worked = (
        f"**Corporate Governance in Asset Disposals**\n\n"
        f"- **Loss to Company**: `R{cv:,} - R{director_price:,} = R{loss_to_co:,}`\n"
        f"- **Breach**: **Self-Dealing & Conflict of Interest** (selling company assets to a director below market value prejudices shareholders).\n"
        f"- **Required Control**: **Board Approval & Independent Valuation** (plus public tender/auction)."
    )
    return {
        "question_type": "table_fill",
        "subskill": "asset_disposal_audit_and_director_governance",
        "question_text": (
            f"During the external audit, it was discovered that a company vehicle with a market and carrying value of **R{cv:,}** "
            f"was sold privately to a director for **R{director_price:,}**. Complete the audit analysis."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Directors have a fiduciary duty under the Companies Act not to enrich themselves at the expense of the company.",
            "Subtract the price paid by the director from the market/carrying value, then select the correct options from brackets.",
            worked,
        ),
    }


_BUILDERS = {
    "company_diminishing_balance_pro_rata_disposal": _gen_diminishing_pro_rata_disposal,
    "r1_residual_value_rule_and_disposal": _gen_r1_residual_rule,
    "company_asset_disposal_taccount": _gen_company_asset_disposal_taccount,
    "fixed_assets_note_disposal_backcalc": _gen_fixed_assets_note_disposal_backcalc,
    "cash_flow_proceeds_from_disposal_at_carrying_value": _gen_cash_flow_proceeds_disposal,
    "asset_disposal_audit_and_director_governance": _gen_disposal_governance,
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
        q["topic"] = "Disposal of tangible assets"
        q["grade"] = "12"
        out.append(q)
    return out
