"""
Grade 10 Accounting: Sole Trader Financial Statements and Notes
Strictly aligned with South African National Curriculum Standards for Grade 10 Accounting (Term 3).
"""
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "sole_trader_income_statement",
    "sole_trader_balance_sheet",
    "fixed_tangible_assets_note",
    "inventories_and_trade_receivables_notes",
    "owners_equity_note",
    "trade_and_other_payables_note",
]

TRADERS = [
    ("Zululand Outfitters", "S. Zulu"),
    ("Mokoena Hardware Traders", "T. Mokoena"),
    ("Baobab Bookshop", "L. Ndlovu"),
    ("Protea Tech Supplies", "K. van Wyk"),
]


def _make_hints(t1: str, t2: str, t3: str) -> List[Dict[str, str]]:
    return [
        {"tier": 1, "title": "Conceptual Nudge", "content": t1},
        {"tier": 2, "title": "Procedural Step", "content": t2},
        {"tier": 3, "title": "Full Worked Example", "content": t3},
    ]


def _gen_income_statement(r: random.Random) -> Dict[str, Any]:
    firm, owner = r.choice(TRADERS)
    sales = r.randint(480, 750) * 1000
    debtors_allow = r.randint(10, 25) * 1000
    net_sales = sales - debtors_allow
    cos = int(net_sales * 0.6)
    gp = net_sales - cos
    rent_inc = r.randint(24, 48) * 1000
    disc_rec = r.randint(4, 9) * 1000
    gross_op_inc = gp + rent_inc + disc_rec
    salaries = r.randint(85, 130) * 1000
    depr = r.randint(18, 35) * 1000
    utilities = r.randint(22, 38) * 1000
    tot_exp = salaries + depr + utilities
    op_profit = gross_op_inc - tot_exp
    int_inc = r.randint(3, 8) * 1000
    int_exp = r.randint(6, 14) * 1000
    net_profit = op_profit + int_inc - int_exp

    headers = ["Statement of Comprehensive Income Line Item", "Amount (R)"]
    rows = [
        [f"Turnover (Sales R{sales:,} less Debtors Allowances R{debtors_allow:,})", "{r0_c1}"],
        ["Cost of sales", f"(R{cos:,})"],
        ["Gross profit", "{r2_c1}"],
        [f"Other operating income (Rent income R{rent_inc:,} + Discount received R{disc_rec:,})", "{r3_c1}"],
        ["Gross operating income", "{r4_c1}"],
        [f"Operating expenses (Salaries R{salaries:,} + Depreciation R{depr:,} + Utilities R{utilities:,})", "{r5_c1}"],
        ["Operating profit", "{r6_c1}"],
        ["Interest income", f"R{int_inc:,}"],
        ["Interest expense", f"(R{int_exp:,})"],
        ["Net profit for the year", "{r9_c1}"],
    ]
    correct_map = {
        "r0_c1": net_sales,
        "r2_c1": gp,
        "r3_c1": rent_inc + disc_rec,
        "r4_c1": gross_op_inc,
        "r5_c1": tot_exp,
        "r6_c1": op_profit,
        "r9_c1": net_profit,
    }
    worked = (
        f"**{firm} — Statement of Comprehensive Income (Income Statement)**\n\n"
        f"- **Turnover**: `R{sales:,} - R{debtors_allow:,} = R{net_sales:,}`\n"
        f"- **Gross Profit**: `R{net_sales:,} - R{cos:,} = R{gp:,}`\n"
        f"- **Other Operating Income**: `R{rent_inc:,} + R{disc_rec:,} = R{rent_inc + disc_rec:,}`\n"
        f"- **Gross Operating Income**: `R{gp:,} + R{rent_inc + disc_rec:,} = R{gross_op_inc:,}`\n"
        f"- **Operating Expenses**: `R{salaries:,} + R{depr:,} + R{utilities:,} = R{tot_exp:,}`\n"
        f"- **Operating Profit**: `R{gross_op_inc:,} - R{tot_exp:,} = R{op_profit:,}`\n"
        f"- **Net Profit for the Year**: `R{op_profit:,} + R{int_inc:,} - R{int_exp:,} = R{net_profit:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "sole_trader_income_statement",
        "question_text": (
            f"Complete the **Statement of Comprehensive Income (Income Statement)** for **{firm}** (owner: {owner}) "
            f"for the financial year ended 28 February."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 7,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Follow the standard vertical Income Statement structure: Turnover -> Gross Profit -> Gross Operating Income -> Operating Profit -> Net Profit.",
            "Subtract Debtors Allowances from Sales first. Add Other Operating Income to Gross Profit, subtract Operating Expenses, then adjust for Interest.",
            worked,
        ),
    }


def _gen_balance_sheet(r: random.Random) -> Dict[str, Any]:
    firm, owner = r.choice(TRADERS)
    tangible = r.randint(320, 520) * 1000
    fixed_dep = r.randint(40, 80) * 1000
    non_curr_assets = tangible + fixed_dep
    inv = r.randint(75, 130) * 1000
    rec = r.randint(45, 85) * 1000
    cash = r.randint(25, 60) * 1000
    curr_assets = inv + rec + cash
    total_assets = non_curr_assets + curr_assets

    non_curr_liab = r.randint(80, 150) * 1000
    curr_liab = r.randint(50, 95) * 1000
    owners_eq = total_assets - non_curr_liab - curr_liab
    total_eq_liab = owners_eq + non_curr_liab + curr_liab

    headers = ["Statement of Financial Position (Balance Sheet)", "Amount (R)"]
    rows = [
        [f"Non-Current Assets (Fixed Assets R{tangible:,} + Fixed Deposit R{fixed_dep:,})", "{r0_c1}"],
        [f"Current Assets (Inventories R{inv:,} + Receivables R{rec:,} + Cash R{cash:,})", "{r1_c1}"],
        ["TOTAL ASSETS", "{r2_c1}"],
        ["Owner's Equity (balancing figure)", "{r3_c1}"],
        ["Non-Current Liabilities (Mortgage Loan)", f"R{non_curr_liab:,}"],
        ["Current Liabilities (Trade and other payables)", f"R{curr_liab:,}"],
        ["TOTAL EQUITY AND LIABILITIES", "{r6_c1}"],
    ]
    correct_map = {
        "r0_c1": non_curr_assets,
        "r1_c1": curr_assets,
        "r2_c1": total_assets,
        "r3_c1": owners_eq,
        "r6_c1": total_eq_liab,
    }
    worked = (
        f"**{firm} — Statement of Financial Position (Balance Sheet)**\n\n"
        f"- **Non-Current Assets**: `R{tangible:,} + R{fixed_dep:,} = R{non_curr_assets:,}`\n"
        f"- **Current Assets**: `R{inv:,} + R{rec:,} + R{cash:,} = R{curr_assets:,}`\n"
        f"- **Total Assets**: `R{non_curr_assets:,} + R{curr_assets:,} = R{total_assets:,}`\n"
        f"- **Owner's Equity** (`A - L`): `R{total_assets:,} - R{non_curr_liab:,} - R{curr_liab:,} = R{owners_eq:,}`\n"
        f"- **Total Equity and Liabilities**: `R{total_eq_liab:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "sole_trader_balance_sheet",
        "question_text": (
            f"Complete the **Statement of Financial Position (Balance Sheet)** for **{firm}** (owner: {owner}) as at 28 February."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Total Assets must equal Total Equity and Liabilities (`A = OE + L`).",
            "Sum Non-Current Assets and Current Assets to find Total Assets, then subtract Non-Current and Current Liabilities to determine Owner's Equity.",
            worked,
        ),
    }


def _gen_fixed_assets_note(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    eq_cost = r.randint(150, 260) * 1000
    eq_acc_open = r.randint(30, 60) * 1000
    eq_open_cv = eq_cost - eq_acc_open
    additions = r.randint(20, 50) * 1000
    depr = int(eq_cost * 0.10)
    close_cost = eq_cost + additions
    close_acc = eq_acc_open + depr
    close_cv = close_cost - close_acc

    headers = ["Note 3: Fixed / Tangible Assets (Equipment)", "Amount (R)"]
    rows = [
        ["Cost at beginning of year", f"R{eq_cost:,}"],
        ["Accumulated depreciation at beginning of year", f"(R{eq_acc_open:,})"],
        ["Carrying value at beginning of year", "{r2_c1}"],
        ["Additions at cost during the year", f"R{additions:,}"],
        ["Depreciation for the year (10% p.a. on opening cost)", "{r4_c1}"],
        ["Cost at end of year", "{r5_c1}"],
        ["Accumulated depreciation at end of year", "{r6_c1}"],
        ["Carrying value at end of year", "{r7_c1}"],
    ]
    correct_map = {
        "r2_c1": eq_open_cv,
        "r4_c1": depr,
        "r5_c1": close_cost,
        "r6_c1": close_acc,
        "r7_c1": close_cv,
    }
    worked = (
        f"**Fixed / Tangible Assets Note ({firm})**\n\n"
        f"- Opening Carrying Value: `R{eq_cost:,} - R{eq_acc_open:,} = R{eq_open_cv:,}`\n"
        f"- Depreciation for the year: `10% × R{eq_cost:,} = R{depr:,}`\n"
        f"- Closing Cost: `R{eq_cost:,} + R{additions:,} = R{close_cost:,}`\n"
        f"- Closing Accumulated Depreciation: `R{eq_acc_open:,} + R{depr:,} = R{close_acc:,}`\n"
        f"- **Closing Carrying Value**: `R{close_cost:,} - R{close_acc:,} = R{close_cv:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "fixed_tangible_assets_note",
        "question_text": (
            f"Complete **Note 3: Fixed / Tangible Assets (Equipment)** for **{firm}**. "
            f"Additions of **R{additions:,}** were purchased on the last day of the financial year; depreciation is calculated at **10% p.a. on opening cost**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 5,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Carrying Value always equals Cost minus Accumulated Depreciation.",
            "Calculate opening carrying value, then add additions to cost and add current depreciation to accumulated depreciation.",
            worked,
        ),
    }


def _gen_inventories_and_receivables_notes(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    trad_stock = r.randint(65, 120) * 1000
    consumables = r.randint(3, 8) * 1000
    tot_inv = trad_stock + consumables

    debtors = r.randint(40, 80) * 1000
    prepaid = r.randint(4, 9) * 1000
    accrued_inc = r.randint(2, 6) * 1000
    tot_rec = debtors + prepaid + accrued_inc

    headers = ["Balance Sheet Note Item", "Amount (R)"]
    rows = [
        ["Note 4: Inventories — Trading stock", f"R{trad_stock:,}"],
        ["Note 4: Inventories — Consumable stores on hand", f"R{consumables:,}"],
        ["Total Inventories", "{r2_c1}"],
        ["Note 5: Trade and other receivables — Trade debtors", f"R{debtors:,}"],
        ["Note 5: Trade and other receivables — Prepaid expenses", f"R{prepaid:,}"],
        ["Note 5: Trade and other receivables — Accrued income", f"R{accrued_inc:,}"],
        ["Total Trade and other receivables", "{r6_c1}"],
    ]
    correct_map = {
        "r2_c1": tot_inv,
        "r6_c1": tot_rec,
    }
    worked = (
        f"**Notes 4 & 5: Inventories and Trade & Other Receivables ({firm})**\n\n"
        f"- **Total Inventories** = Trading stock (`R{trad_stock:,}`) + Consumable stores on hand (`R{consumables:,}`) = `R{tot_inv:,}`\n"
        f"- **Total Trade and Other Receivables** = Trade debtors (`R{debtors:,}`) + Prepaid expenses (`R{prepaid:,}`) + Accrued income (`R{accrued_inc:,}`) = `R{tot_rec:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "inventories_and_trade_receivables_notes",
        "question_text": (
            f"Complete **Note 4 (Inventories)** and **Note 5 (Trade and other receivables)** to the financial statements of **{firm}**."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Inventories combine trading stock and unused consumable stores on hand. Receivables combine trade debtors, prepaid expenses, and accrued income.",
            "Add the two inventory items for Row 3, and add the three receivable items for Row 7.",
            worked,
        ),
    }


def _gen_owners_equity_note(r: random.Random) -> Dict[str, Any]:
    firm, owner = r.choice(TRADERS)
    open_cap = r.randint(350, 550) * 1000
    add_cap = r.randint(40, 80) * 1000
    net_profit = r.randint(90, 180) * 1000
    drawings = r.randint(35, 75) * 1000
    close_cap = open_cap + add_cap + net_profit - drawings

    headers = ["Note 7: Owner's Equity", "Amount (R)"]
    rows = [
        ["Capital balance at beginning of year", f"R{open_cap:,}"],
        ["Additional capital contributed during the year", f"R{add_cap:,}"],
        ["Net profit for the year", f"R{net_profit:,}"],
        ["Less: Drawings by owner (cash and trading stock)", f"(R{drawings:,})"],
        ["Capital balance at end of year", "{r4_c1}"],
    ]
    correct_map = {"r4_c1": close_cap}
    worked = (
        f"**Note 7: Owner's Equity ({firm} — {owner})**\n\n"
        f"- Opening Capital: `R{open_cap:,}`\n"
        f"- Add Additional Capital: `+ R{add_cap:,}`\n"
        f"- Add Net Profit: `+ R{net_profit:,}`\n"
        f"- Less Drawings: `- R{drawings:,}`\n"
        f"- **Closing Capital Balance**: `R{close_cap:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "owners_equity_note",
        "question_text": (
            f"Complete **Note 7: Owner's Equity** for **{firm}** (owner: {owner}) for the financial year ended 28 February."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Additional capital and net profit increase Owner's Equity, whereas drawings reduce Owner's Equity.",
            "Add Opening Capital, Additional Capital, and Net Profit, then subtract Drawings.",
            worked,
        ),
    }


def _gen_payables_note(r: random.Random) -> Dict[str, Any]:
    firm, _ = r.choice(TRADERS)
    creditors = r.randint(35, 75) * 1000
    accrued_exp = r.randint(5, 14) * 1000
    income_in_adv = r.randint(4, 10) * 1000
    sars_paye = r.randint(6, 12) * 1000
    total_payables = creditors + accrued_exp + income_in_adv + sars_paye

    headers = ["Note 8: Trade and Other Payables", "Amount (R)"]
    rows = [
        ["Trade creditors", f"R{creditors:,}"],
        ["Accrued expenses (Expenses payable)", f"R{accrued_exp:,}"],
        ["Income received in advance (Deferred income)", f"R{income_in_adv:,}"],
        ["SARS (PAYE) & Pension/UIF liabilities", f"R{sars_paye:,}"],
        ["Total Trade and other payables", "{r4_c1}"],
    ]
    correct_map = {"r4_c1": total_payables}
    worked = (
        f"**Note 8: Trade and Other Payables ({firm})**\n\n"
        f"- Trade creditors: `R{creditors:,}`\n"
        f"- Accrued expenses: `R{accrued_exp:,}`\n"
        f"- Income received in advance: `R{income_in_adv:,}`\n"
        f"- SARS (PAYE) & statutory funds: `R{sars_paye:,}`\n"
        f"- **Total Trade and Other Payables**: `R{total_payables:,}`"
    )
    return {
        "question_type": "table_fill",
        "subskill": "trade_and_other_payables_note",
        "question_text": (
            f"Complete **Note 8: Trade and other payables** for **{firm}** at year-end."
        ),
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "marks": 4,
        "worked_solution": worked,
        "canonical_solution": worked,
        "hints": _make_hints(
            "Trade and other payables group all short-term obligations payable within 12 months.",
            "Add Trade Creditors, Accrued Expenses, Income Received in Advance, and SARS/statutory liabilities.",
            worked,
        ),
    }


_BUILDERS = {
    "sole_trader_income_statement": _gen_income_statement,
    "sole_trader_balance_sheet": _gen_balance_sheet,
    "fixed_tangible_assets_note": _gen_fixed_assets_note,
    "inventories_and_trade_receivables_notes": _gen_inventories_and_receivables_notes,
    "owners_equity_note": _gen_owners_equity_note,
    "trade_and_other_payables_note": _gen_payables_note,
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
        q["topic"] = "Financial Statements of a Sole Trader"
        q["grade"] = "10"
        out.append(q)
    return out
