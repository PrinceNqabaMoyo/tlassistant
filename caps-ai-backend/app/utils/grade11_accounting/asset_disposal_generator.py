"""
Grade 11 Accounting: Disposal of Tangible Assets
Strictly aligned with South African National Curriculum Standards for Grade 11 Accounting.
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "pro_rata_depreciation_on_disposed_asset",
    "carrying_value_and_profit_loss_on_disposal",
    "asset_disposal_taccount_completion",
    "general_journal_entries_for_asset_disposal",
    "fixed_assets_note_disposal_column",
    "trade_in_vs_cash_disposal_analysis",
]

PARTNERSHIPS = [
    "Mabaso & Steyn Logistics",
    "Ndlovu & Patel Deliveries",
    "Karoo Transport Partnership",
    "Highveld Couriers",
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t3},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_pro_rata_depreciation(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    cost = r.choice([180000, 240000, 300000])
    open_acc = int(cost * 0.40)
    open_cv = cost - open_acc
    months = r.choice([6, 9])
    rate = 20
    depr_curr_sl = int(cost * (rate / 100) * (months / 12))
    tot_acc_at_sale = open_acc + depr_curr_sl
    cv_at_sale = cost - tot_acc_at_sale

    headers = ["Pro-Rata Disposal Calculation (Straight-Line 20% p.a.)", "Amount (R)"]
    rows = [
        ["Original cost price of delivery vehicle", f"R{cost:,}"],
        ["Accumulated depreciation at beginning of financial year", f"R{open_acc:,}"],
        [f"Current year pro-rata depreciation ({months} months at 20% p.a. on cost)", "{r2_c1}"],
        ["Total accumulated depreciation at date of disposal", "{r3_c1}"],
        ["Carrying value at date of disposal", "{r4_c1}"],
    ]
    correct_map = {
        "r2_c1": depr_curr_sl,
        "r3_c1": tot_acc_at_sale,
        "r4_c1": cv_at_sale,
    }
    worked = (
        f"**Pro-Rata Depreciation on Disposed Vehicle ({firm})**\n\n"
        f"- **Current year depreciation ({months}/12 months)**: `R{cost:,} × 20% × ({months}/12) = R{depr_curr_sl:,}`\n"
        f"- **Total Accumulated Depreciation at sale**: `R{open_acc:,} + R{depr_curr_sl:,} = R{tot_acc_at_sale:,}`\n"
        f"- **Carrying Value at date of disposal**: `R{cost:,} - R{tot_acc_at_sale:,} = R{cv_at_sale:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "pro_rata_depreciation_on_disposed_asset",
        "question_text": (
            f"**{firm}** sold a delivery vehicle after **{months} months** of the current financial year. "
            f"Depreciation is calculated at **20% p.a. on cost**. Complete the schedule."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "When an asset is sold mid-year, calculate pro-rata depreciation from the start of the financial year up to the date of sale.",
            f"Multiply Cost (R{cost:,}) by 20% and by {months}/12, add to opening accumulated depreciation, and subtract from Cost.",
            worked,
        ),
    }


def _gen_profit_loss_on_disposal(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    cost = r.choice([160000, 200000, 250000])
    acc_dep = int(cost * 0.65)
    cv = cost - acc_dep
    proceeds = cv + r.choice([8000, 12000, -6000, -10000])
    diff = abs(proceeds - cv)
    outcome = "Profit on Sale of Asset" if proceeds > cv else "Loss on Sale of Asset"

    headers = ["Disposal Outcome Calculation", "Amount / Classification"]
    rows = [
        ["Cost price of equipment sold", f"R{cost:,}"],
        ["Less: Total accumulated depreciation to date of sale", f"(R{acc_dep:,})"],
        ["Carrying value at date of sale (R)", "{r2_c1}"],
        ["Selling price / proceeds received (R)", f"R{proceeds:,}"],
        ["Amount of gain or loss on disposal (positive R)", "{r4_c1}"],
        ["Classification (Profit on Sale of Asset / Loss on Sale of Asset)", "{r5_c1}"],
    ]
    correct_map = {
        "r2_c1": cv,
        "r4_c1": diff,
        "r5_c1": outcome,
    }
    worked = (
        f"**Profit / Loss on Disposal ({firm})**\n\n"
        f"- **Carrying Value**: `R{cost:,} - R{acc_dep:,} = R{cv:,}`\n"
        f"- **Proceeds**: `R{proceeds:,}`\n"
        f"- Since proceeds (`R{proceeds:,}`) {'exceed' if proceeds > cv else 'are less than'} carrying value (`R{cv:,}`), there is a **{outcome}** of **`R{diff:,}`**."
    )
    return {
        "question_type": "table_fill",
        "subskill": "carrying_value_and_profit_loss_on_disposal",
        "question_text": (
            f"**{firm}** disposed of equipment (Cost **R{cost:,}**, Accumulated Depreciation at sale **R{acc_dep:,}**) "
            f"for **R{proceeds:,}**. Complete the disposal outcome schedule."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Compare Selling Price (Proceeds) with Carrying Value (Cost - Accumulated Depreciation).",
            "If Proceeds > Carrying Value, it is a Profit on Sale of Asset; if Proceeds < Carrying Value, it is a Loss on Sale of Asset.",
            worked,
        ),
    }


def _gen_asset_disposal_taccount(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    cost = r.choice([180000, 220000, 260000])
    acc_dep = int(cost * 0.55)
    cv = cost - acc_dep
    profit = r.choice([6000, 9000, 12000])
    proceeds = cv + profit
    tot = cost + profit

    headers = ["Asset Disposal Account Entry", "Side (Debit / Credit)", "Amount (R)"]
    rows = [
        ["Vehicles / Equipment (Cost price transferred)", "Debit", "{r0_c2}"],
        ["Accumulated Depreciation on Vehicles (total to date of sale)", "Credit", "{r1_c2}"],
        ["Bank / Debtors Control (Selling price)", "Credit", f"R{proceeds:,}"],
        ["Profit on Sale of Asset (balancing figure)", "Debit", "{r3_c2}"],
        ["Account Total (Debit = Credit)", "Both", "{r4_c2}"],
    ]
    correct_map = {
        "r0_c2": cost,
        "r1_c2": acc_dep,
        "r3_c2": profit,
        "r4_c2": tot,
    }
    worked = (
        f"**Asset Disposal Ledger Account ({firm})**\n\n"
        f"- **Debit Vehicles (Cost)**: `R{cost:,}`\n"
        f"- **Credit Accumulated Depreciation**: `R{acc_dep:,}`\n"
        f"- **Credit Bank (Proceeds)**: `R{proceeds:,}`\n"
        f"- **Debit Profit on Sale of Asset**: `R{acc_dep:,} + R{proceeds:,} - R{cost:,} = R{profit:,}`\n"
        f"- **Total of Account**: `R{tot:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "asset_disposal_taccount_completion",
        "question_text": (
            f"Complete the **Asset Disposal Account** for **{firm}** given Cost **R{cost:,}**, "
            f"Accumulated Depreciation at sale **R{acc_dep:,}**, and Cash Proceeds **R{proceeds:,}**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "In the Asset Disposal account, Cost Price is entered on the Debit side, while Accumulated Depreciation and Proceeds are entered on the Credit side.",
            "Enter Cost in Row 1, Accumulated Depreciation in Row 2, Profit on Sale in Row 4, and the balancing total in Row 5.",
            worked,
        ),
    }


def _gen_journal_entries_disposal(r: random.Random) -> Dict[str, Any]:
    headers = ["Disposal Step in the General Journal", "Account Debited", "Account Credited"]
    rows = [
        ["Step 1: Transfer original cost price of vehicle sold", "{r0_c1}", "{r0_c2}"],
        ["Step 2: Record current year pro-rata depreciation up to sale date", "{r1_c1}", "{r1_c2}"],
        ["Step 3: Transfer total accumulated depreciation on vehicle sold", "{r2_c1}", "{r2_c2}"],
    ]
    correct_map = {
        "r0_c1": "Asset Disposal",
        "r0_c2": "Vehicles",
        "r1_c1": "Depreciation",
        "r1_c2": "Accumulated Depreciation on Vehicles",
        "r2_c1": "Accumulated Depreciation on Vehicles",
        "r2_c2": "Asset Disposal",
    }
    worked = (
        "**General Journal Entries for Asset Disposal**\n\n"
        "- **Step 1 (Transfer Cost)**: Debit **Asset Disposal**, Credit **Vehicles**\n"
        "- **Step 2 (Pro-rata Depreciation)**: Debit **Depreciation**, Credit **Accumulated Depreciation on Vehicles**\n"
        "- **Step 3 (Transfer Acc Dep)**: Debit **Accumulated Depreciation on Vehicles**, Credit **Asset Disposal**"
    )
    return {
        "question_type": "table_fill",
        "subskill": "general_journal_entries_for_asset_disposal",
        "question_text": (
            "State the **Account Debited** and **Account Credited** for the first three steps of recording the disposal of a **Vehicle** "
            "(choose from: `Asset Disposal`, `Vehicles`, `Depreciation`, `Accumulated Depreciation on Vehicles`)."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Removing an asset reduces the Vehicles asset account (Credit) and removes its Accumulated Depreciation contra-asset (Debit).",
            "Transfer Cost to the Debit of Asset Disposal and Accumulated Depreciation to the Credit of Asset Disposal.",
            worked,
        ),
    }


def _gen_fixed_assets_note_disposal(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    open_cost = 600000
    open_acc = 220000
    open_cv = open_cost - open_acc

    disp_cost = r.choice([120000, 150000])
    disp_acc = int(disp_cost * 0.60)
    disp_cv = disp_cost - disp_acc
    depr_total = 75000

    close_cost = open_cost - disp_cost
    close_acc = open_acc + depr_total - disp_acc
    close_cv = open_cv - disp_cv - depr_total

    headers = ["Note 3: Fixed / Tangible Assets (Vehicles)", "Amount (R)"]
    rows = [
        [f"Carrying value at beginning of year (Cost R{open_cost:,} less Acc Dep R{open_acc:,})", f"R{open_cv:,}"],
        [f"Disposals at carrying value (Cost R{disp_cost:,} less Acc Dep at sale R{disp_acc:,})", "{r1_c1}"],
        ["Depreciation for the year", f"(R{depr_total:,})"],
        ["Cost at end of year", "{r3_c1}"],
        ["Accumulated depreciation at end of year", "{r4_c1}"],
        ["Carrying value at end of year", "{r5_c1}"],
    ]
    correct_map = {
        "r1_c1": disp_cv,
        "r3_c1": close_cost,
        "r4_c1": close_acc,
        "r5_c1": close_cv,
    }
    worked = (
        f"**Fixed Assets Note with Disposal ({firm})**\n\n"
        f"- **Disposals at Carrying Value**: `R{disp_cost:,} - R{disp_acc:,} = R{disp_cv:,}`\n"
        f"- **Closing Cost**: `R{open_cost:,} - R{disp_cost:,} = R{close_cost:,}`\n"
        f"- **Closing Accumulated Depreciation**: `R{open_acc:,} + R{depr_total:,} - R{disp_acc:,} = R{close_acc:,}`\n"
        f"- **Closing Carrying Value**: `R{close_cost:,} - R{close_acc:,} = R{close_cv:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "fixed_assets_note_disposal_column",
        "question_text": (
            f"Complete the **Vehicles** column in **Note 3: Fixed / Tangible Assets** for **{firm}**. "
            f"(Enter positive Rand values; brackets are handled by the line description.)"
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 6,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "In Note 3, disposals are shown at Carrying Value in the movements section, while Closing Cost deducts the disposed asset's Cost and Closing Acc Dep deducts the disposed asset's Acc Dep.",
            "Calculate Disposal CV first, then update Closing Cost, Closing Acc Dep, and Closing CV.",
            worked,
        ),
    }


def _gen_trade_in_disposal(r: random.Random) -> Dict[str, Any]:
    firm = r.choice(PARTNERSHIPS)
    old_cost = 200000
    old_acc = 135000
    old_cv = old_cost - old_acc
    trade_in_val = r.choice([72000, 58000])
    new_veh_cost = 320000
    net_owing_creditor = new_veh_cost - trade_in_val
    gain_loss = abs(trade_in_val - old_cv)

    headers = ["Trade-In Disposal Analysis", "Amount (R)"]
    rows = [
        [f"Carrying value of old vehicle traded in (Cost R{old_cost:,} - Acc Dep R{old_acc:,})", "{r0_c1}"],
        ["Trade-in allowance granted by dealership", f"R{trade_in_val:,}"],
        ["Profit / Loss on trade-in (positive R difference)", "{r2_c1}"],
        [f"Net amount owing to Creditors Control for new vehicle (Cost R{new_veh_cost:,} less trade-in)", "{r3_c1}"],
    ]
    correct_map = {
        "r0_c1": old_cv,
        "r2_c1": gain_loss,
        "r3_c1": net_owing_creditor,
    }
    worked = (
        f"**Trade-In Disposal Analysis ({firm})**\n\n"
        f"- **Old Vehicle Carrying Value**: `R{old_cost:,} - R{old_acc:,} = R{old_cv:,}`\n"
        f"- **Profit / Loss on Trade-In**: `|R{trade_in_val:,} - R{old_cv:,}| = R{gain_loss:,}`\n"
        f"- **Net Balance Owing to Creditor**: `R{new_veh_cost:,} - R{trade_in_val:,} = R{net_owing_creditor:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "trade_in_vs_cash_disposal_analysis",
        "question_text": (
            f"**{firm}** traded in an old vehicle (Cost **R{old_cost:,}**, Accumulated Depreciation **R{old_acc:,}**) "
            f"for a trade-in allowance of **R{trade_in_val:,}** towards a new vehicle costing **R{new_veh_cost:,}**. Complete the schedule."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "A trade-in reduces the amount owing to the vehicle supplier (Creditors Control) by the trade-in value.",
            "Calculate the old vehicle's carrying value, compare with the trade-in allowance, and subtract the trade-in allowance from the new vehicle's cost.",
            worked,
        ),
    }


_BUILDERS = {
    "pro_rata_depreciation_on_disposed_asset": _gen_pro_rata_depreciation,
    "carrying_value_and_profit_loss_on_disposal": _gen_profit_loss_on_disposal,
    "asset_disposal_taccount_completion": _gen_asset_disposal_taccount,
    "general_journal_entries_for_asset_disposal": _gen_journal_entries_disposal,
    "fixed_assets_note_disposal_column": _gen_fixed_assets_note_disposal,
    "trade_in_vs_cash_disposal_analysis": _gen_trade_in_disposal,
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
        q["grade"] = "11"
        out.append(q)
    return out
