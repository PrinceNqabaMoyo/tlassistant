"""Grade 9 EMS - Credit Transactions (Debtors 2): Archetypes 26 to 50.

Grounded strictly in:
- curriculum_docs_auto/EMS_Gr9/Term 3/01. Credit transactions (Debtors 2).md
- curriculum_docs/EMS_Gr9/Term 3/9-Credit transactions Debtors (2).md

Imports shared builders and SA scenario helpers from `.term3_debtors_ledger_archetypes_01_25`.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from app.utils.ems_namelist import get_ems_scenario
from .term3_debtors_ledger_archetypes_01_25 import (
    DEBTOR_POOL,
    MONTH_DATA,
    biz_name,
    build_mcq,
    build_short,
    build_table,
    fmt_cell,
    fmt_r,
    make_grid_rows,
    pick_debtors,
)


def arch_26_complete_trading_stock_t_account_with_dj_crj_cpj_daj_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, end_d, next_m, next_d = rng.choice(MONTH_DATA)
    open_stock = rng.randint(40, 75) * 1000
    cpj_buy = rng.randint(12, 28) * 1000
    daj_ret_cp = rng.randint(1, 3) * 1000
    crj_cos = rng.randint(18, 30) * 1000
    dj_cos = rng.randint(4, 12) * 1000
    tot_dr = open_stock + cpj_buy + daj_ret_cp
    closing_stock = tot_dr - crj_cos - dj_cos

    headers = ["Dr Details", "Dr Fol", "Dr Amount", "Cr Details", "Cr Fol", "Cr Amount"]
    data_rows = [
        ["Balance", "b/d", str(open_stock), "Cost of sales", "CRJ", str(crj_cos)],
        ["Bank", "CPJ", str(cpj_buy), "Cost of sales", "DJ", str(dj_cos)],
        ["Cost of sales", "DAJ", str(daj_ret_cp), "Balance", "c/d", str(closing_stock)],
        ["TOTAL", "", str(tot_dr), "TOTAL", "", str(tot_dr)],
        ["Balance", "b/d", str(closing_stock), "", "", ""],
    ]
    given = {(0, 0), (0, 1), (0, 2), (3, 0), (3, 1), (3, 3), (3, 4), (4, 3), (4, 4), (4, 5)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r1_c2": f"Cash stock purchases from CPJ enter Debit = {cpj_buy}.",
        "t0_r2_c2": f"Stock returned by debtors (DAJ CoS) enters Debit = {daj_ret_cp}.",
        "t0_r0_c5": f"Cash sales cost price (CRJ) reduces Trading Stock on Credit = {crj_cos}.",
        "t0_r1_c5": f"Credit sales cost price (DJ) reduces Trading Stock on Credit = {dj_cos}.",
        "t0_r2_c5": f"Closing Balance c/d = {tot_dr} - ({crj_cos} + {dj_cos}) = {closing_stock}.",
        "t0_r4_c2": f"Next month Balance b/d on Dr side = {closing_stock}.",
    }
    prompt = (
        f"Complete the General Ledger **Trading Stock (`B5`)** T-account of **{biz}** for **{m_name} {yr}** *(digits only)*:\n"
        f"- Opening stock (`b/d`): {fmt_r(open_stock)}\n"
        f"- Cash stock bought (`CPJ Bank`): {fmt_r(cpj_buy)}\n"
        f"- Stock returned by debtors (`DAJ Cost of sales`): {fmt_r(daj_ret_cp)}\n"
        f"- Cash sales cost price (`CRJ Cost of sales`): {fmt_r(crj_cos)}\n"
        f"- Credit sales cost price (`DJ Cost of sales`): {fmt_r(dj_cos)}"
    )
    worked = (
        f"**General Ledger: Trading Stock (B5) — {m_name} {yr}** [10 marks]\n\n"
        "| Dr Details | Fol | Dr Amount | Cr Details | Fol | Cr Amount |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| Balance | b/d | {open_stock} | Cost of sales | CRJ | {crj_cos} |\n"
        f"| Bank | CPJ | {cpj_buy} | Cost of sales | DJ | {dj_cos} |\n"
        f"| Cost of sales | DAJ | {daj_ret_cp} | Balance | c/d | **{closing_stock}** |\n"
        f"| **TOTAL** | | **{tot_dr}** | **TOTAL** | | **{tot_dr}** |\n"
        f"| Balance | b/d | **{closing_stock}** | | | |"
    )
    return build_table(
        rng,
        qid="g9_dl_26",
        subskill="26_complete_trading_stock_t_account_with_dj_crj_cpj_daj_table",
        title="Complete Trading Stock (B5) T-Account (CPJ, DAJ, CRJ, DJ)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Total={tot_dr}; Closing Stock b/d={closing_stock}",
        marks=10,
        hints={
            "tier_1": "Stock inflows (b/d, CPJ purchases, DAJ returns) sit on Debit; outflows (CRJ & DJ Cost of Sales) sit on Credit.",
            "tier_2": f"Dr total = {open_stock} + {cpj_buy} + {daj_ret_cp} = {tot_dr}.",
            "tier_3": f"Closing Trading Stock c/d & b/d = {closing_stock}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Dr CPJ ({cpj_buy}) & DAJ ({daj_ret_cp})", "marks": 4, "editable": True},
            {"id": "mp_2", "desc": f"Cr CRJ ({crj_cos}) & DJ ({dj_cos})", "marks": 3, "editable": True},
            {"id": "mp_3", "desc": f"Balanced c/d & b/d = {closing_stock}", "marks": 3, "editable": True},
        ],
        misconception_tags=["crediting_daj_returns_in_trading_stock"],
        journal_type="t_account",
    )


def arch_27_complete_sales_nominal_t_account_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, end_d, _, _ = rng.choice(MONTH_DATA)
    open_sales = rng.randint(50, 95) * 1000
    crj_sales = rng.randint(20, 42) * 1000
    dj_sales = rng.randint(6, 18) * 1000
    tot_sales = open_sales + crj_sales + dj_sales

    headers = ["Cr Date", "Details (Contra Account)", "Fol", "Credit Amount (R)"]
    data_rows = [
        [f"{m_name[:3]} 1", "Balance", "b/d", str(open_sales)],
        [f"{m_name[:3]} {end_d}", "Bank", "CRJ", str(crj_sales)],
        [f"{m_name[:3]} {end_d}", "Debtors control", "DJ", str(dj_sales)],
        ["", "Total Credit Sales & Cash Sales Balance", "", str(tot_sales)],
    ]
    given = {(0, j) for j in range(4)} | {(1, 0), (2, 0), (3, 0), (3, 1), (3, 2)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r1_c1": "Cash sales come via 'Bank'.",
        "t0_r1_c2": "Folio is 'CRJ'.",
        "t0_r1_c3": f"CRJ Sales total = {crj_sales}.",
        "t0_r2_c1": "Credit sales contra account is 'Debtors control'.",
        "t0_r2_c2": "Folio is 'DJ'.",
        "t0_r2_c3": f"DJ Sales total = {dj_sales}.",
        "t0_r3_c3": f"Total Sales balance = {open_sales} + {crj_sales} + {dj_sales} = {tot_sales}.",
    }
    prompt = (
        f"Complete the Credit side of the Nominal account **Sales (`N1`)** for **{biz}** ({m_name} {yr}):\n"
        f"- Opening Sales balance (`b/d`): {fmt_r(open_sales)}\n"
        f"- Cash Sales (`CRJ`): {fmt_r(crj_sales)}\n"
        f"- Credit Sales (`DJ`): {fmt_r(dj_sales)}\n"
        "*(Enter digits without spaces or R.)*"
    )
    worked = (
        "**General Ledger: Sales (N1) — Credit Side** [6 marks]\n\n"
        "| Date | Details | Fol | Amount (R) |\n| --- | --- | --- | --- |\n"
        f"| {m_name[:3]} 1 | Balance | b/d | {open_sales} |\n"
        f"| {m_name[:3]} {end_d} | **Bank** | **CRJ** | **{crj_sales}** |\n"
        f"| {m_name[:3]} {end_d} | **Debtors control** | **DJ** | **{dj_sales}** |\n"
        f"| | **Total Sales** | | **{tot_sales}** |"
    )
    return build_table(
        rng,
        qid="g9_dl_27",
        subskill="27_complete_sales_nominal_t_account_table",
        title="Post Cash & Credit Sales to Sales (N1) Nominal Account",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Bank CRJ {crj_sales}; Debtors control DJ {dj_sales}; Total {tot_sales}",
        marks=6,
        hints={
            "tier_1": "Sales is Income (Credit side): enter contra accounts Bank (CRJ) and Debtors control (DJ).",
            "tier_2": f"Sum {open_sales} + {crj_sales} + {dj_sales}.",
            "tier_3": f"Total Sales = {tot_sales}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Bank (CRJ) {crj_sales}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Debtors control (DJ) {dj_sales}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Total Sales = {tot_sales}", "marks": 2, "editable": True},
        ],
        misconception_tags=["writing_sales_as_details_inside_sales_account"],
        journal_type="t_account",
    )


def arch_28_complete_cost_of_sales_nominal_t_account_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, end_d, _, _ = rng.choice(MONTH_DATA)
    open_cos = rng.randint(40, 70) * 1000
    crj_cos = rng.randint(15, 28) * 1000
    dj_cos = rng.randint(4, 12) * 1000
    daj_cos = rng.randint(1, 3) * 1000
    net_cos = open_cos + crj_cos + dj_cos - daj_cos

    headers = ["Dr Details", "Dr Fol", "Dr Amount", "Cr Details", "Cr Fol", "Cr Amount"]
    data_rows = [
        ["Balance", "b/d", str(open_cos), "Trading stock", "DAJ", str(daj_cos)],
        ["Trading stock", "CRJ", str(crj_cos), "", "", ""],
        ["Trading stock", "DJ", str(dj_cos), "", "", ""],
        ["Net Cost of Sales Balance", "", str(net_cos), "", "", ""],
    ]
    given = {(0, 0), (0, 1), (0, 2), (1, 5), (2, 5), (3, 0), (3, 1), (3, 3), (3, 4), (3, 5)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r1_c0": "Contra account for Cost of Sales is always 'Trading stock'.",
        "t0_r1_c2": f"CRJ Cost of sales = {crj_cos}.",
        "t0_r2_c2": f"DJ Cost of sales = {dj_cos}.",
        "t0_r0_c5": f"DAJ returns reverse Cost of sales on Credit = {daj_cos}.",
        "t0_r3_c2": f"Net Cost of Sales = {open_cos} + {crj_cos} + {dj_cos} - {daj_cos} = {net_cos}.",
    }
    prompt = (
        f"Post the **Cost of Sales (`N2`)** nominal account for **{biz}** ({m_name} {yr}):\n"
        f"- Opening Cost of sales (`b/d`): {fmt_r(open_cos)}\n"
        f"- CRJ Cost of sales: {fmt_r(crj_cos)} | DJ Cost of sales: {fmt_r(dj_cos)}\n"
        f"- DAJ Cost of sales returned: {fmt_r(daj_cos)}\n"
        "*(Enter digits without spaces or R; leave unused cells blank.)*"
    )
    worked = (
        "**General Ledger: Cost of Sales (N2)** [6 marks]\n\n"
        "| Dr Details | Fol | Dr Amount | Cr Details | Fol | Cr Amount |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| Balance | b/d | {open_cos} | **Trading stock** | **DAJ** | **{daj_cos}** |\n"
        f"| **Trading stock** | **CRJ** | **{crj_cos}** | | | |\n"
        f"| **Trading stock** | **DJ** | **{dj_cos}** | | | |\n"
        f"| **Net Balance** | | **{net_cos}** | | | |"
    )
    return build_table(
        rng,
        qid="g9_dl_28",
        subskill="28_complete_cost_of_sales_nominal_t_account_table",
        title="Post CRJ, DJ & DAJ to Cost of Sales (N2)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Trading stock CRJ {crj_cos}, DJ {dj_cos}; Cr Trading stock DAJ {daj_cos}; Net {net_cos}",
        marks=6,
        hints={
            "tier_1": "Cost of Sales is an Expense: sales increase it on Debit (Trading stock CRJ/DJ); returns reduce it on Credit (DAJ).",
            "tier_2": f"Net CoS = {open_cos} + {crj_cos} + {dj_cos} - {daj_cos}.",
            "tier_3": f"Net Cost of Sales Balance = {net_cos}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Dr Trading stock CRJ {crj_cos} & DJ {dj_cos}", "marks": 3, "editable": True},
            {"id": "mp_2", "desc": f"Cr Trading stock DAJ {daj_cos} & Net {net_cos}", "marks": 3, "editable": True},
        ],
        misconception_tags=["omitting_daj_credit_reversal_in_cost_of_sales"],
        journal_type="t_account",
    )


def arch_29_complete_debtors_allowance_t_account_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, yr, end_d, _, _ = rng.choice(MONTH_DATA)
    open_da = rng.randint(8, 22) * 100
    daj_tot = rng.randint(12, 36) * 100
    tot_da = open_da + daj_tot

    headers = ["Dr Date", "Dr Details (Contra Account)", "Fol", "Debit Amount (R)"]
    data_rows = [
        [f"{m_name[:3]} 1", "Balance", "b/d", str(open_da)],
        [f"{m_name[:3]} {end_d}", "Debtors control", "DAJ", str(daj_tot)],
        ["", "Total Debtors Allowance", "", str(tot_da)],
    ]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(0, j) for j in range(4)} | {(1, 0), (2, 0), (2, 1), (2, 2)})
    cell_hints = {
        "t0_r1_c1": "Contra account for DAJ posting is 'Debtors control'.",
        "t0_r1_c2": "Folio is 'DAJ'.",
        "t0_r1_c3": f"DAJ Debtors Allowance total = {daj_tot}.",
        "t0_r2_c3": f"Total = {open_da} + {daj_tot} = {tot_da}.",
    }
    prompt = (
        f"Post the monthly **Debtors Allowance Journal (DAJ)** total (**{fmt_r(daj_tot)}**) into the "
        f"**Debtors Allowance (`N3`)** General Ledger account of **{biz}** (opening balance `b/d` = {fmt_r(open_da)})."
    )
    worked = (
        "**General Ledger: Debtors Allowance (N3)** [4 marks]\n\n"
        "| Date | Details | Fol | Amount (R) |\n| --- | --- | --- | --- |\n"
        f"| {m_name[:3]} 1 | Balance | b/d | {open_da} |\n"
        f"| {m_name[:3]} {end_d} | **Debtors control** | **DAJ** | **{daj_tot}** |\n"
        f"| | **Total** | | **{tot_da}** |"
    )
    return build_table(
        rng,
        qid="g9_dl_29",
        subskill="29_complete_debtors_allowance_t_account_table",
        title="Post DAJ Total to Debtors Allowance (N3)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Debtors control (DAJ) {daj_tot}; Total {tot_da}",
        marks=4,
        hints={
            "tier_1": "Debtors Allowance reduces Sales income, so it sits on the Debit side.",
            "tier_2": "Contra account = Debtors control; Folio = DAJ.",
            "tier_3": f"Amount = {daj_tot}; New Total = {tot_da}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Contra account Debtors control & Fol DAJ", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Amount {daj_tot} and Total {tot_da}", "marks": 2, "editable": True},
        ],
        misconception_tags=["crediting_debtors_allowance_account"],
        journal_type="t_account",
    )


def arch_30_calculate_markup_profit_pct_from_ledger_balances(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    pct = rng.choice([20, 25, 30, 40, 50, 60])
    cos_bal = rng.randint(25, 65) * 1000
    sales_bal = cos_bal * (100 + pct) // 100
    profit = sales_bal - cos_bal

    prompt = (
        f"In the General Ledger of **{biz}** (matching the curriculum mark-up method), the closing balances are:\n"
        f"- **Sales (`N1`):** {fmt_r(sales_bal)}\n"
        f"- **Cost of Sales (`N2`):** {fmt_r(cos_bal)}\n\n"
        "Calculate the **profit mark-up percentage on cost price** achieved by the business [3].\n"
        "*(Enter the percentage number only, e.g. `25`.)*"
    )
    worked = (
        "**Step 1 — Gross Profit from Ledger Balances:**\n"
        f"`Profit = Sales - Cost of sales = {fmt_r(sales_bal)} - {fmt_r(cos_bal)} = {fmt_r(profit)}` [1]\n\n"
        "**Step 2 — Mark-up Percentage on Cost Price:**\n"
        f"$$\\frac{{\\text{{Profit}}}}{{\\text{{Cost Price}}}} \\times 100 = \\frac{{{profit}}}{{{cos_bal}}} \\times 100 = {pct}\\%$$ [2]\n"
        f"Answer: `{pct}`"
    )
    return build_short(
        rng,
        qid="g9_dl_30",
        subskill="30_calculate_markup_profit_pct_from_ledger_balances",
        title="Calculate Mark-up Percentage from General Ledger",
        prompt=prompt,
        expected_answer=str(pct),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "First find Gross Profit (Sales minus Cost of Sales), then divide by Cost of Sales.",
            "tier_2": f"Profit = {sales_bal} - {cos_bal} = {profit}.",
            "tier_3": f"({profit} / {cos_bal}) × 100 = {pct}%.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Gross Profit = {fmt_r(profit)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Profit % on cost = {pct}%", "marks": 2, "editable": True},
        ],
        misconception_tags=["dividing_profit_by_sales_instead_of_cost_price"],
    )


def arch_31_derive_missing_dj_or_crj_cos_from_trading_stock_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    open_s = rng.randint(40, 70) * 1000
    cpj_s = rng.randint(15, 30) * 1000
    crj_cos = rng.randint(20, 35) * 1000
    dj_cos = rng.randint(6, 15) * 1000
    close_s = open_s + cpj_s - crj_cos - dj_cos

    prompt = (
        f"Examine the **Trading Stock (`B5`)** General Ledger account of **{biz}**:\n"
        f"- **Debit side:** Opening Balance `b/d` = {fmt_r(open_s)}; Cash Purchases (`Bank CPJ`) = {fmt_r(cpj_s)}\n"
        f"- **Credit side:** Cash Sales (`Cost of sales CRJ`) = {fmt_r(crj_cos)}; Closing Balance `c/d` = {fmt_r(close_s)}\n\n"
        "Calculate the missing **Cost of sales from Debtors Journal (`DJ`)** figure needed to balance the account [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Step 1 — Debit Side Total (Total Available Stock):**\n"
        f"`{fmt_r(open_s)} + {fmt_r(cpj_s)} = {fmt_r(open_s + cpj_s)}` [1]\n\n"
        "**Step 2 — Deduce Missing Credit Entry (`Cost of sales DJ`):**\n"
        f"`DJ Cost of sales = {open_s + cpj_s} - {crj_cos} - {close_s} = {dj_cos}` [2]"
    )
    return build_short(
        rng,
        qid="g9_dl_31",
        subskill="31_derive_missing_dj_or_crj_cos_from_trading_stock_calc",
        title="Deduce Missing DJ Cost of Sales from Trading Stock",
        prompt=prompt,
        expected_answer=str(dj_cos),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Both sides of Trading Stock must balance to the exact same total.",
            "tier_2": f"Dr total = {open_s + cpj_s}. Subtract known Cr items ({crj_cos} and {close_s}).",
            "tier_3": f"Missing DJ Cost of sales = {dj_cos}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Dr total = {open_s + cpj_s}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Missing DJ CoS = {dj_cos}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_closing_balance_instead_of_subtracting_from_debit_total"],
    )


def arch_32_debit_credit_sign_rules_assets_equity_liabilities_svg(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    cases = [
        ("Debtors Control (Current Asset)", "Debit (+) / Credit (-)", "Debit increases (+); Credit decreases (-)."),
        ("Sales (Income -> Owner's Equity)", "Debit (-) / Credit (+)", "Credit increases (+); Debit decreases (-)."),
        ("Cost of Sales (Expense -> Owner's Equity)", "Debit (+) increases Expense", "Increases on Debit (+), which decreases Owner's Equity (-)."),
    ]
    acct, rule_ans, why = rng.choice(cases)
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 190" width="520" height="190">'
        '<rect x="6" y="6" width="508" height="178" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<rect x="6" y="6" width="508" height="36" rx="8" fill="#0f172a"/>'
        f'<text x="260" y="29" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Rules of Debit &amp; Credit ({biz})</text>'
        '<rect x="20" y="54" width="230" height="114" rx="6" fill="#eff6ff" stroke="#1d4ed8"/>'
        '<text x="135" y="76" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">DEBIT (+ Side for D.E.A.)</text>'
        '<text x="135" y="98" font-size="11" fill="#0f172a" text-anchor="middle">Drawings | Expenses | Assets</text>'
        '<text x="135" y="122" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">Debit (+) Increases | Credit (-) Decreases</text>'
        f'<text x="135" y="148" font-size="10" fill="#334155" text-anchor="middle">Focus: {acct[:24]}</text>'
        '<rect x="270" y="54" width="230" height="114" rx="6" fill="#f0fdf4" stroke="#15803d"/>'
        '<text x="385" y="76" font-size="12" font-weight="bold" fill="#14532d" text-anchor="middle">CREDIT (+ Side for C.I.L.)</text>'
        '<text x="385" y="98" font-size="11" fill="#0f172a" text-anchor="middle">Capital (OE) | Income | Liabilities</text>'
        '<text x="385" y="122" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">Credit (+) Increases | Debit (-) Decreases</text>'
        '<text x="385" y="148" font-size="10" fill="#334155" text-anchor="middle">Accounting Eq: A = OE + L</text>'
        '</svg>'
    )
    prompt = (
        f"Study the **Debit & Credit Rules** diagram for **{biz}** below.\n\n"
        f"Which rule correctly describes how **{acct}** behaves in the General Ledger?"
    )
    all_opts = [
        "Debit increases (+) and Credit decreases (-) Assets like Debtors Control.",
        "Credit increases (+) and Debit decreases (-) Income like Sales.",
        "Debit increases (+) Expense accounts like Cost of Sales (which lowers Owner's Equity).",
        "Credit increases (+) Drawings and Assets while Debit decreases Liabilities.",
    ]
    if "Debtors Control" in acct:
        correct = all_opts[0]
        distractors = [all_opts[1], all_opts[2], all_opts[3]]
    elif "Sales" in acct:
        correct = all_opts[1]
        distractors = [all_opts[0], all_opts[2], all_opts[3]]
    else:
        correct = all_opts[2]
        distractors = [all_opts[0], all_opts[1], all_opts[3]]
    return build_mcq(
        rng,
        qid="g9_dl_32",
        subskill="32_debit_credit_sign_rules_assets_equity_liabilities_svg",
        title="Debit & Credit Classification Rules (DEA vs CIL)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"**{acct}:** {why}",
        hints={
            "tier_1": "Use D.E.A. (Drawings, Expenses, Assets increase on Debit) vs C.I.L. (Capital, Income, Liabilities increase on Credit).",
            "tier_2": f"Target account: {acct} -> {rule_ans}.",
            "tier_3": correct,
        },
        misconception_tags=["reversing_debit_credit_rules_for_income_and_expenses"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_33_accounting_equation_credit_sale_selling_price_leg_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    sp = rng.randint(15, 48) * 100
    inv = rng.randint(120, 310)

    headers = ["Account Debited", "Account Credited", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    data_rows = [["Debtors control", "Sales", f"+{sp}", f"+{sp}", "0"]]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints = {
        "t0_r0_c0": "Customer owes us money -> Asset account 'Debtors control'.",
        "t0_r0_c1": "Income earned from selling goods -> 'Sales'.",
        "t0_r0_c2": f"Debtors Control increases Assets -> +{sp}.",
        "t0_r0_c3": f"Sales Income increases Owner's Equity -> +{sp}.",
        "t0_r0_c4": "No liability changes -> 0.",
    }
    prompt = (
        f"**{biz}** sells goods on credit to **{debtor}** for **{fmt_r(sp)}** (Duplicate Invoice {inv}).\n\n"
        "Complete the **Selling Price leg** ONLY in the Accounting Equation table below *(use `+amount`, `-amount`, or `0`)*."
    )
    worked = (
        "**Accounting Equation — Selling Price Leg (DJ)** [5 marks]\n\n"
        "| Account Debited | Account Credited | A | OE | L |\n| --- | --- | --- | --- | --- |\n"
        f"| **Debtors control** | **Sales** | **+{sp}** | **+{sp}** | **0** |"
    )
    return build_table(
        rng,
        qid="g9_dl_33",
        subskill="33_accounting_equation_credit_sale_selling_price_leg_table",
        title="Accounting Equation: Credit Sale (Selling Price Leg)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Debtors control; Cr Sales; A +{sp}; OE +{sp}; L 0",
        marks=5,
        hints={
            "tier_1": "Selling on credit creates a debtor (Asset +) and earns Sales revenue (OE +).",
            "tier_2": f"Dr Debtors control | Cr Sales | +{sp} | +{sp} | 0.",
            "tier_3": f"Debtors control / Sales / +{sp} / +{sp} / 0.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Dr Debtors control, Cr Sales", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"A +{sp}, OE +{sp}, L 0", "marks": 3, "editable": True},
        ],
        misconception_tags=["debiting_bank_on_credit_sale_equation"],
        journal_type="accounting_equation",
    )


def arch_34_accounting_equation_credit_sale_cost_price_leg_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    cp = rng.randint(10, 32) * 100
    sp = int(cp * 1.5)

    headers = ["Account Debited", "Account Credited", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    data_rows = [["Cost of sales", "Trading stock", f"-{cp}", f"-{cp}", "0"]]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints = {
        "t0_r0_c0": "Expense account recording cost of goods sold -> 'Cost of sales'.",
        "t0_r0_c1": "Asset leaving the storeroom -> 'Trading stock'.",
        "t0_r0_c2": f"Trading stock leaves the store -> -{cp}.",
        "t0_r0_c3": f"Expense (Cost of sales) reduces profit/equity -> -{cp}.",
        "t0_r0_c4": "Liabilities unaffected -> 0.",
    }
    prompt = (
        f"**{biz}** sells merchandise on credit to **{debtor}** for {fmt_r(sp)} (the **cost price** is **{fmt_r(cp)}**).\n\n"
        "Complete the **Cost of Sales leg** ONLY in the Accounting Equation table *(use `+amount`, `-amount`, or `0`)*."
    )
    worked = (
        "**Accounting Equation — Cost Price Leg (DJ)** [5 marks]\n\n"
        "| Account Debited | Account Credited | A | OE | L |\n| --- | --- | --- | --- | --- |\n"
        f"| **Cost of sales** | **Trading stock** | **-{cp}** | **-{cp}** | **0** |"
    )
    return build_table(
        rng,
        qid="g9_dl_34",
        subskill="34_accounting_equation_credit_sale_cost_price_leg_table",
        title="Accounting Equation: Credit Sale (Cost Price Leg)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Cost of sales; Cr Trading stock; A -{cp}; OE -{cp}; L 0",
        marks=5,
        hints={
            "tier_1": "Use COST PRICE ({0}) for the inventory outflow leg.".format(fmt_r(cp)),
            "tier_2": f"Cost of sales (Expense, OE -) debited; Trading stock (Asset -) credited -> -{cp}.",
            "tier_3": f"Cost of sales / Trading stock / -{cp} / -{cp} / 0.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Dr Cost of sales, Cr Trading stock", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"A -{cp}, OE -{cp}, L 0", "marks": 3, "editable": True},
        ],
        misconception_tags=["using_selling_price_in_cost_of_sales_leg"],
        journal_type="accounting_equation",
    )


def arch_35_accounting_equation_credit_sale_dual_entry_full_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    markup = rng.choice([25, 50])
    cp = rng.randint(12, 28) * 100
    sp = cp * (100 + markup) // 100

    headers = ["Leg", "Account Debited", "Account Credited", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    data_rows = [
        ["1. Selling Price", "Debtors control", "Sales", f"+{sp}", f"+{sp}", "0"],
        ["2. Cost Price", "Cost of sales", "Trading stock", f"-{cp}", f"-{cp}", "0"],
    ]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(0, 0), (1, 0)})
    cell_hints = {
        "t0_r0_c3": f"Debtors Control increases Assets by Selling Price +{sp}.",
        "t0_r1_c3": f"Cost of Sales = {sp} × 100/{100+markup} = {cp} -> Trading Stock drops -{cp}.",
    }
    prompt = (
        f"Sold trading stock on credit to **{debtor}** at **{biz}** for **{fmt_r(sp)}** (mark-up is **{markup}% on cost**).\n\n"
        "Complete **both legs** of the credit sale in the Accounting Equation table *(use `+amount`, `-amount`, or `0`)*."
    )
    worked = (
        f"**Dual Accounting Equation Effect (Credit Sale {fmt_r(sp)}, Cost {fmt_r(cp)})** [8 marks]\n\n"
        "| Leg | Dr | Cr | A | OE | L |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| 1. Selling Price | Debtors control | Sales | +{sp} | +{sp} | 0 |\n"
        f"| 2. Cost Price | Cost of sales | Trading stock | -{cp} | -{cp} | 0 |"
    )
    return build_table(
        rng,
        qid="g9_dl_35",
        subskill="35_accounting_equation_credit_sale_dual_entry_full_table",
        title="Full Dual-Leg Accounting Equation for Credit Sale",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Debtors control/Cr Sales (+{sp}); Dr Cost of sales/Cr Trading stock (-{cp})",
        marks=8,
        hints={
            "tier_1": "Every sale has two simultaneous double entries: Selling Price (Debtors/Sales) and Cost Price (CoS/Stock).",
            "tier_2": f"First compute Cost Price = {sp} × 100/{100+markup} = {cp}.",
            "tier_3": f"Row 1: +{sp} / +{sp}; Row 2: -{cp} / -{cp}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"SP leg: Debtors control/Sales +{sp}", "marks": 4, "editable": True},
            {"id": "mp_2", "desc": f"CP leg: Cost of sales/Trading stock -{cp}", "marks": 4, "editable": True},
        ],
        misconception_tags=["omitting_second_leg_on_credit_sale"],
        journal_type="accounting_equation",
    )


def arch_36_accounting_equation_net_profit_impact_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    cp = rng.randint(15, 45) * 100
    markup = rng.choice([25, 40, 50, 60])
    sp = cp * (100 + markup) // 100
    net_oe = sp - cp

    prompt = (
        f"**{biz}** records a single credit sale of **{fmt_r(sp)}** (cost price **{fmt_r(cp)}**) to a debtor.\n\n"
        "After posting BOTH the Selling Price and Cost Price double entries, what is the **NET Rand increase** in Total Assets "
        "and Owner's Equity? [3]\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Net Accounting Equation Effect of a Credit Sale** [3 marks]\n\n"
        f"- Selling Price increases A and OE by `+{fmt_r(sp)}`\n"
        f"- Cost Price decreases A and OE by `-{fmt_r(cp)}`\n"
        f"- **Net Increase** (equals Gross Profit): `+{sp} - {cp} = +{net_oe}` -> Answer: `{net_oe}`"
    )
    return build_short(
        rng,
        qid="g9_dl_36",
        subskill="36_accounting_equation_net_profit_impact_calc",
        title="Net Assets & Equity Impact of Credit Sale",
        prompt=prompt,
        expected_answer=str(net_oe),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "Combine the positive Selling Price effect and the negative Cost Price effect.",
            "tier_2": f"Net change = +{sp} - {cp}.",
            "tier_3": f"Net increase in Assets and Owner's Equity = {net_oe} (Gross Profit).",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Net change = +{net_oe}", "marks": 3, "editable": True},
        ],
        misconception_tags=["reporting_selling_price_as_net_equity_gain"],
    )


def arch_37_accounting_equation_debtor_payment_receipt_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    amt = rng.randint(12, 42) * 100

    headers = ["Account Debited", "Account Credited", "Net Effect on Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    data_rows = [["Bank", "Debtors control", "0", "0", "0"]]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints = {
        "t0_r0_c0": "Cash/EFT received enters 'Bank'.",
        "t0_r0_c1": "Debtor's owed balance decreases -> 'Debtors control'.",
        "t0_r0_c2": f"Bank +{amt} and Debtors Control -{amt} cancel to NET 0 on Total Assets!",
        "t0_r0_c3": "Collecting debt does NOT earn new income -> OE effect = 0.",
        "t0_r0_c4": "Liabilities unaffected -> 0.",
    }
    prompt = (
        f"**{debtor}** pays **{biz}** **{fmt_r(amt)}** in settlement of an existing credit account (CRJ Duplicate Receipt).\n\n"
        "Complete the **Accounting Equation** table showing the **NET effect** (`0` for unchanged total or net swap)."
    )
    worked = (
        f"**Accounting Equation: Debtor Receipt ({fmt_r(amt)})** [5 marks]\n\n"
        "| Account Debited | Account Credited | Net Assets | OE | L |\n| --- | --- | --- | --- | --- |\n"
        f"| **Bank** | **Debtors control** | **0** (+{amt} Bank, -{amt} Debtors) | **0** | **0** |"
    )
    return build_table(
        rng,
        qid="g9_dl_37",
        subskill="37_accounting_equation_debtor_payment_receipt_table",
        title="Accounting Equation: Debtor Payment (Asset Swap)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Bank, Cr Debtors control; Net A=0 (+{amt}/-{amt}), OE=0, L=0",
        marks=5,
        hints={
            "tier_1": "Both Bank and Debtors control are Assets: one goes UP, the other goes DOWN by the exact same Rand value.",
            "tier_2": "Dr Bank | Cr Debtors control; Assets net 0; Owner's Equity 0 (no new Sales).",
            "tier_3": "Bank / Debtors control / 0 / 0 / 0.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Dr Bank, Cr Debtors control", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Net A = 0, OE = 0, L = 0", "marks": 3, "editable": True},
        ],
        misconception_tags=["increasing_owners_equity_on_debtor_payment"],
        journal_type="accounting_equation",
    )


def arch_38_accounting_equation_debtors_return_selling_price_leg_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    sp = rng.randint(4, 15) * 100

    headers = ["Account Debited", "Account Credited", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    data_rows = [["Debtors allowance", "Debtors control", f"-{sp}", f"-{sp}", "0"]]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints = {
        "t0_r0_c0": "Contra-income reversal account -> 'Debtors allowance'.",
        "t0_r0_c1": "Debtor owes less -> 'Debtors control'.",
        "t0_r0_c2": f"Debtors Control asset drops -> -{sp}.",
        "t0_r0_c3": f"Allowance reverses Sales revenue -> -{sp}.",
    }
    prompt = (
        f"**{debtor}** returns damaged stock originally billed at **{fmt_r(sp)}** to **{biz}** (Credit Note issued, DAJ).\n\n"
        "Complete the **Debtors Allowance (Selling Price) leg** in the Accounting Equation table *(use `+amount`, `-amount`, or `0`)*."
    )
    worked = (
        "**Accounting Equation — DAJ Allowance Leg** [5 marks]\n\n"
        "| Account Debited | Account Credited | A | OE | L |\n| --- | --- | --- | --- | --- |\n"
        f"| **Debtors allowance** | **Debtors control** | **-{sp}** | **-{sp}** | **0** |"
    )
    return build_table(
        rng,
        qid="g9_dl_38",
        subskill="38_accounting_equation_debtors_return_selling_price_leg_table",
        title="Accounting Equation: DAJ Allowance Leg (SP)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Debtors allowance; Cr Debtors control; A -{sp}; OE -{sp}; L 0",
        marks=5,
        hints={
            "tier_1": "This leg reverses the original Debtors Control (+) and Sales (+) entry.",
            "tier_2": f"Dr Debtors allowance | Cr Debtors control | -{sp} | -{sp} | 0.",
            "tier_3": f"Debtors allowance / Debtors control / -{sp} / -{sp} / 0.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Dr Debtors allowance, Cr Debtors control", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"A -{sp}, OE -{sp}, L 0", "marks": 3, "editable": True},
        ],
        misconception_tags=["reversing_debtors_allowance_and_debtors_control"],
        journal_type="accounting_equation",
    )


def arch_39_accounting_equation_debtors_return_cost_price_leg_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    cp = rng.randint(3, 12) * 100
    sp = int(cp * 1.5)

    headers = ["Account Debited", "Account Credited", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    data_rows = [["Trading stock", "Cost of sales", f"+{cp}", f"+{cp}", "0"]]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints = {
        "t0_r0_c0": "Returned physical goods go back into 'Trading stock'.",
        "t0_r0_c1": "Original stock expense reverses in 'Cost of sales'.",
        "t0_r0_c2": f"Trading stock increases back up -> +{cp}.",
        "t0_r0_c3": f"Reducing an expense (Cost of sales) increases Owner's Equity -> +{cp}.",
    }
    prompt = (
        f"**{debtor}** returns undamaged goods worth **{fmt_r(sp)}** (cost price **{fmt_r(cp)}**) to **{biz}**.\n\n"
        "Complete the **Cost Price (Stock Return) leg** ONLY in the Accounting Equation table *(use `+amount`, `-amount`, or `0`)*."
    )
    worked = (
        "**Accounting Equation — DAJ Cost Price Leg** [5 marks]\n\n"
        "| Account Debited | Account Credited | A | OE | L |\n| --- | --- | --- | --- | --- |\n"
        f"| **Trading stock** | **Cost of sales** | **+{cp}** | **+{cp}** | **0** |"
    )
    return build_table(
        rng,
        qid="g9_dl_39",
        subskill="39_accounting_equation_debtors_return_cost_price_leg_table",
        title="Accounting Equation: DAJ Stock Return Leg (CP)",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Trading stock; Cr Cost of sales; A +{cp}; OE +{cp}; L 0",
        marks=5,
        hints={
            "tier_1": "Physical stock returns to shelves (Asset +) and reverses Cost of sales expense (OE +).",
            "tier_2": f"Dr Trading stock | Cr Cost of sales | +{cp} | +{cp} | 0.",
            "tier_3": f"Trading stock / Cost of sales / +{cp} / +{cp} / 0.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Dr Trading stock, Cr Cost of sales", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"A +{cp}, OE +{cp}, L 0", "marks": 3, "editable": True},
        ],
        misconception_tags=["subtracting_returned_stock_cost_from_assets"],
        journal_type="accounting_equation",
    )


def arch_40_accounting_equation_debtors_allowance_overcharge_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    rebate = rng.choice([150, 220, 300, 450])

    headers = ["Account Debited", "Account Credited", "Assets (A)", "Owner's Equity (OE)", "Liabilities (L)"]
    data_rows = [["Debtors allowance", "Debtors control", f"-{rebate}", f"-{rebate}", "0"]]
    rows, correct_map = make_grid_rows(data_rows)
    cell_hints = {
        "t0_r0_c0": "Price overcharge correction -> 'Debtors allowance'.",
        "t0_r0_c1": "Reduces customer balance -> 'Debtors control'.",
        "t0_r0_c2": f"Only ONE entry (no stock returned!): A -{rebate}.",
        "t0_r0_c3": f"OE -{rebate}.",
    }
    prompt = (
        f"**{biz}** grants **{debtor}** a Credit Note for **{fmt_r(rebate)}** to correct a billing **overcharge** (no goods were physically returned).\n\n"
        "Complete the **single** Accounting Equation entry required *(use `+amount`, `-amount`, or `0`)*."
    )
    worked = (
        "**Accounting Equation — Price Overcharge Rebate (No Stock Return)** [5 marks]\n\n"
        "| Dr | Cr | A | OE | L |\n| --- | --- | --- | --- | --- |\n"
        f"| **Debtors allowance** | **Debtors control** | **-{rebate}** | **-{rebate}** | **0** |\n\n"
        "*No Trading Stock / Cost of Sales entry is made because zero physical goods returned.*"
    )
    return build_table(
        rng,
        qid="g9_dl_40",
        subskill="40_accounting_equation_debtors_allowance_overcharge_table",
        title="Accounting Equation: DAJ Overcharge Rebate",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr Debtors allowance; Cr Debtors control; A -{rebate}; OE -{rebate}; L 0",
        marks=5,
        hints={
            "tier_1": "Since no goods came back into the storeroom, only the debtor-allowance leg occurs.",
            "tier_2": f"Dr Debtors allowance | Cr Debtors control | -{rebate} | -{rebate} | 0.",
            "tier_3": f"Debtors allowance / Debtors control / -{rebate} / -{rebate} / 0.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Dr Debtors allowance, Cr Debtors control", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"A -{rebate}, OE -{rebate}, L 0", "marks": 3, "editable": True},
        ],
        misconception_tags=["adding_stock_entry_on_pure_price_overcharge"],
        journal_type="accounting_equation",
    )


def arch_41_accounting_equation_cash_vs_credit_sale_comparison_svg(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    sp = rng.randint(18, 45) * 100
    cp = int(sp * 100 // 150)

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 185" width="520" height="185">'
        '<rect x="6" y="6" width="508" height="173" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        '<rect x="6" y="6" width="508" height="36" rx="8" fill="#1e3a8a"/>'
        f'<text x="260" y="29" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Cash Sale vs Credit Sale Double Entry ({biz})</text>'
        '<rect x="20" y="54" width="230" height="110" rx="6" fill="#ecfdf5" stroke="#059669"/>'
        '<text x="135" y="75" font-size="11.5" font-weight="bold" fill="#065f46" text-anchor="middle">CASH SALE (CRJ)</text>'
        f'<text x="135" y="96" font-size="11" fill="#0f172a" text-anchor="middle">Dr Bank (+{sp}) | Cr Sales (+{sp})</text>'
        f'<text x="135" y="116" font-size="11" fill="#0f172a" text-anchor="middle">Dr Cost of sales (-{cp} OE)</text>'
        f'<text x="135" y="136" font-size="11" fill="#0f172a" text-anchor="middle">Cr Trading stock (-{cp} A)</text>'
        '<rect x="270" y="54" width="230" height="110" rx="6" fill="#eff6ff" stroke="#2563eb"/>'
        '<text x="385" y="75" font-size="11.5" font-weight="bold" fill="#1e40af" text-anchor="middle">CREDIT SALE (DJ)</text>'
        f'<text x="385" y="96" font-size="11" fill="#0f172a" text-anchor="middle">Dr Debtors control (+{sp}) | Cr Sales (+{sp})</text>'
        f'<text x="385" y="116" font-size="11" fill="#0f172a" text-anchor="middle">Dr Cost of sales (-{cp} OE)</text>'
        f'<text x="385" y="136" font-size="11" fill="#0f172a" text-anchor="middle">Cr Trading stock (-{cp} A)</text>'
        '</svg>'
    )
    prompt = (
        f"Compare the **Cash Sale** and **Credit Sale** flows of **{fmt_r(sp)}** (cost **{fmt_r(cp)}**) for **{biz}** shown in the diagram below.\n\n"
        "Which statement correctly summarises the ONLY double-entry difference between a Cash Sale and a Credit Sale?"
    )
    correct = f"Both credit Sales (+{fmt_r(sp)}) and adjust Cost of Sales / Trading Stock ({fmt_r(cp)}) identically; ONLY the Asset account debited changes from Bank (CRJ) to Debtors control (DJ)."
    distractors = [
        "Only a Cash Sale records Sales and Cost of Sales; Credit Sales wait until Bank is paid.",
        "Credit Sales debit Trading Stock instead of Cost of Sales.",
        "Cash Sales debit Debtors control and credit Liabilities.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_41",
        subskill="41_accounting_equation_cash_vs_credit_sale_comparison_svg",
        title="Compare Cash Sale vs Credit Sale Accounting Effect",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Whether stock is sold for cash (`CRJ`) or on credit (`DJ`), **Sales** (`+{fmt_r(sp)}`), **Cost of Sales**, and "
            f"**Trading Stock** (`-{fmt_r(cp)}`) behave identically—only **Bank** is replaced by **Debtors control**."
        ),
        hints={
            "tier_1": "Look closely at the first debit line in each box of the diagram.",
            "tier_2": "Bank (cash) vs Debtors control (credit) is the sole difference.",
            "tier_3": correct,
        },
        misconception_tags=["omitting_sales_or_cos_on_credit_sales"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_42_multi_transaction_accounting_equation_5rows_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL[:4])
    cp1 = rng.randint(10, 20) * 100
    sp1 = int(cp1 * 1.5)
    ret_sp = rng.randint(2, 4) * 150
    pay = rng.randint(8, 14) * 100

    txns = [
        f"1. Sold goods on credit to {debtor} for {fmt_r(sp1)} (cost price {fmt_r(cp1)}) — Selling price leg.",
        f"2. Record the Cost of sales ({fmt_r(cp1)}) for transaction 1.",
        f"3. Issued Credit Note to {debtor} for {fmt_r(ret_sp)} overcharge allowance (no stock returned).",
        f"4. Received {fmt_r(pay)} EFT from {debtor} in partial settlement.",
    ]
    headers = ["Row", "Account Debited", "Account Credited", "A", "OE", "L"]
    data_rows = [
        ["1 (SP)", "Debtors control", "Sales", f"+{sp1}", f"+{sp1}", "0"],
        ["2 (CP)", "Cost of sales", "Trading stock", f"-{cp1}", f"-{cp1}", "0"],
        ["3 (DAJ)", "Debtors allowance", "Debtors control", f"-{ret_sp}", f"-{ret_sp}", "0"],
        ["4 (CRJ)", "Bank", "Debtors control", "0", "0", "0"],
    ]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(0, 0), (1, 0), (2, 0), (3, 0), (0, 5), (1, 5), (2, 5), (3, 5)})
    cell_hints = {
        "t0_r0_c3": f"Debtors control increases A by +{sp1}.",
        "t0_r1_c3": f"Trading stock decreases A by -{cp1}.",
        "t0_r2_c3": f"Overcharge allowance reduces Debtors control -> -{ret_sp}.",
        "t0_r3_c3": f"Bank +{pay} and Debtors control -{pay} net to 0.",
    }
    prompt = (
        f"Complete all 4 rows in the Accounting Equation summary for **{biz}** *(enter `+amount`, `-amount`, or `0`)*."
    )
    worked = (
        "**Multi-Transaction Accounting Equation** [12 marks]\n\n"
        "| Row | Dr | Cr | A | OE | L |\n| --- | --- | --- | --- | --- | --- |\n"
        f"| 1 | Debtors control | Sales | +{sp1} | +{sp1} | 0 |\n"
        f"| 2 | Cost of sales | Trading stock | -{cp1} | -{cp1} | 0 |\n"
        f"| 3 | Debtors allowance | Debtors control | -{ret_sp} | -{ret_sp} | 0 |\n"
        f"| 4 | Bank | Debtors control | 0 | 0 | 0 |"
    )
    return build_table(
        rng,
        qid="g9_dl_42",
        subskill="42_multi_transaction_accounting_equation_5rows_table",
        title="4-Transaction Credit Accounting Equation Table",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"1:+{sp1}, 2:-{cp1}, 3:-{ret_sp}, 4:0",
        marks=12,
        hints={
            "tier_1": "Track Debtors control, Sales, Cost of sales, Trading stock, Debtors allowance, and Bank cleanly.",
            "tier_2": f"Row 1 +{sp1}; Row 2 -{cp1}; Row 3 -{ret_sp}; Row 4 net 0.",
            "tier_3": "All Liabilities = 0 throughout.",
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Row {i+1} accounts & A/OE effects", "marks": 3, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["mixing_up_crj_receipt_net_zero_asset_effect"],
        journal_type="accounting_equation",
        transactions=txns,
    )


def arch_43_net_asset_and_equity_movement_summary_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    open_eq = rng.randint(80, 150) * 1000
    dj_sp = rng.randint(12, 24) * 1000
    dj_cp = int(dj_sp * 100 // 150)
    daj_sp = rng.randint(1, 3) * 1500
    daj_cp = int(daj_sp * 100 // 150)
    crj_rec = rng.randint(8, 16) * 1000
    net_change = (dj_sp - dj_cp) - (daj_sp - daj_cp)
    closing_eq = open_eq + net_change

    prompt = (
        f"On 1 September, **{biz}** has **Owner's Equity** of **{fmt_r(open_eq)}**.\n\n"
        "During September, the business records:\n"
        f"- Credit Sales (DJ): **{fmt_r(dj_sp)}** (Cost of Sales **{fmt_r(dj_cp)}**)\n"
        f"- Debtors Allowances (DAJ returns): **{fmt_r(daj_sp)}** (Cost of Sales returned **{fmt_r(daj_cp)}**)\n"
        f"- Receipts from Debtors (CRJ): **{fmt_r(crj_rec)}**\n\n"
        "Calculate **{0}**'s closing **Owner's Equity** at 30 September [4].\n"
        "*(Enter whole digits without spaces or the R symbol.)*".format(biz)
    )
    worked = (
        "**Closing Owner's Equity Calculation** [4 marks]\n\n"
        f"- Net Gross Profit from DJ: `{dj_sp} - {dj_cp} = +{dj_sp - dj_cp}` [1]\n"
        f"- Less Profit reversed by DAJ returns: `-({daj_sp} - {daj_cp}) = -{daj_sp - daj_cp}` [1]\n"
        f"- CRJ receipts from debtors (`{fmt_r(crj_rec)}`): `0` effect on Owner's Equity (asset swap only) [1]\n"
        f"- Closing Owner's Equity: `{open_eq} + {dj_sp - dj_cp} - {daj_sp - daj_cp} = {closing_eq}` [1]"
    )
    return build_short(
        rng,
        qid="g9_dl_43",
        subskill="43_net_asset_and_equity_movement_summary_calc",
        title="Net Movement in Owner's Equity Across DJ, DAJ & CRJ",
        prompt=prompt,
        expected_answer=str(closing_eq),
        worked_solution=worked,
        marks=4,
        hints={
            "tier_1": "Remember: collections from debtors (CRJ) change Assets composition, NOT Owner's Equity!",
            "tier_2": f"Equity change = ({dj_sp} - {dj_cp}) - ({daj_sp} - {daj_cp}) = {net_change}.",
            "tier_3": f"Closing Equity = {open_eq} + {net_change} = {closing_eq}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": "Ignores CRJ debtor receipts in OE calculation", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Closing Equity = {closing_eq}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_debtor_cash_receipts_to_owners_equity"],
    )


def arch_44_identify_error_treating_debtor_receipt_as_income_mcq(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, _ = rng.choice(DEBTOR_POOL)
    amt = rng.randint(15, 45) * 100

    prompt = (
        f"When **{debtor}** paid **{fmt_r(amt)}** to **{biz}** toward an old invoice, a trainee wrote:\n"
        f"`Assets: +{amt} | Owner's Equity: +{amt} | Account Credited: Sales`.\n\n"
        "Why is the trainee's entry **incorrect**?"
    )
    correct = "The sale was already credited to Owner's Equity (Sales) when the invoice was raised; receiving cash swaps Debtors control (-Asset) for Bank (+Asset) with 0 effect on OE."
    distractors = [
        "Receiving cash from a debtor reduces Owner's Equity by double the amount.",
        "Bank is a Liability that increases Liabilities (+L) when debtors pay.",
        "All debtor receipts must credit Cost of Sales to restore inventory.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_44",
        subskill="44_identify_error_treating_debtor_receipt_as_income_mcq",
        title="Diagnose Accounting Equation Error on Debtor Payment",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Under accrual bookkeeping, income (`Sales`) is earned **at the time of sale**, NOT when the debtor pays later. "
            f"Paying **{fmt_r(amt)}** simply turns one asset (`Debtors control`) into another (`Bank`)."
        ),
        hints={
            "tier_1": "Ask whether the business earned a NEW sale today or collected an old debt.",
            "tier_2": "Collecting old debt swaps Debtors control for Bank: Assets net 0, Owner's Equity 0.",
            "tier_3": correct,
        },
        misconception_tags=["treating_debtor_collection_as_new_income"],
    )


def arch_45_posting_date_rule_individual_daily_vs_month_end_totals(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    m_name, _, end_d, _, _ = rng.choice(MONTH_DATA)
    tx_day = rng.randint(5, 22)

    prompt = (
        f"On **{tx_day} {m_name}**, **{biz}** issues an invoice on credit to a debtor (recorded in the DJ).\n\n"
        "Which posting dates are used in the **Debtors Ledger** versus the General Ledger **Debtors Control** account?"
    )
    correct = f"Debtors Ledger posts individually on the transaction date ({tx_day} {m_name}); General Ledger Debtors Control posts the monthly DJ column total at month-end ({end_d} {m_name})."
    distractors = [
        f"Both Debtors Ledger and General Ledger Debtors Control post every single invoice individually on {tx_day} {m_name}.",
        f"Debtors Ledger waits until month-end ({end_d} {m_name}), while General Ledger Debtors Control posts daily on {tx_day} {m_name}.",
        "Neither ledger records dates because totals carry over from the Trial Balance.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_45",
        subskill="45_posting_date_rule_individual_daily_vs_month_end_totals",
        title="Posting Dates: Daily Debtors Ledger vs Month-End Control",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Individual customer balances must always stay current during the month, so **Debtors Ledger** posts on each "
            f"transaction date (`{tx_day} {m_name}`). **General Ledger Control** posts monthly journal totals on `{end_d} {m_name}`."
        ),
        hints={
            "tier_1": "Which ledger needs daily updates so a clerk knows what a customer owes right now?",
            "tier_2": "Daily transaction dates -> Debtors Ledger; Month-end column totals -> General Ledger.",
            "tier_3": correct,
        },
        misconception_tags=["posting_individual_invoices_to_debtors_control"],
    )


def arch_46_reconstruct_crj_bank_receipts_from_debtors_control_gl_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    open_bal = rng.randint(15, 30) * 1000
    dj_sales = rng.randint(20, 42) * 1000
    daj_ret = rng.randint(1, 4) * 1000
    crj_bank = rng.randint(18, 32) * 1000
    close_bal = open_bal + dj_sales - daj_ret - crj_bank

    prompt = (
        f"The **Debtors Control (`B6`)** account of **{biz}** shows:\n"
        f"- Opening Balance (`b/d`): **{fmt_r(open_bal)}**\n"
        f"- Monthly Credit Sales (`DJ`): **{fmt_r(dj_sales)}**\n"
        f"- Monthly Debtors Allowances (`DAJ`): **{fmt_r(daj_ret)}**\n"
        f"- Closing Balance (`c/d`): **{fmt_r(close_bal)}**\n\n"
        "Calculate the total cash collected from debtors in the **CRJ (`Bank`)** during the month [3].\n"
        "*(Enter whole digits without spaces or the R symbol.)*"
    )
    worked = (
        "**Deduce CRJ Cash Receipts from Debtors Control** [3 marks]\n\n"
        f"`Total Dr = {open_bal} + {dj_sales} = {open_bal + dj_sales}` [1]\n"
        f"`CRJ Bank Receipts = {open_bal + dj_sales} - {daj_ret} - {close_bal} = {crj_bank}` [2]"
    )
    return build_short(
        rng,
        qid="g9_dl_46",
        subskill="46_reconstruct_crj_bank_receipts_from_debtors_control_gl_calc",
        title="Deduce Cash Collected from Debtors Control",
        prompt=prompt,
        expected_answer=str(crj_bank),
        worked_solution=worked,
        marks=3,
        hints={
            "tier_1": "On Debtors Control, Dr total (`b/d + DJ`) equals Cr total (`Bank + DAJ + c/d`).",
            "tier_2": f"Dr total = {open_bal + dj_sales}. Subtract DAJ ({daj_ret}) and c/d ({close_bal}).",
            "tier_3": f"CRJ Bank Receipts = {crj_bank}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Dr total = {open_bal + dj_sales}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"CRJ Bank Receipts = {crj_bank}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_daj_to_receipts_instead_of_balancing_t_account"],
    )


def arch_47_trial_balance_extract_after_debtors_postings_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    dc = rng.randint(14, 38) * 1000
    ts = rng.randint(28, 65) * 1000
    sales = rng.randint(55, 110) * 1000
    cos = int(sales * 100 // 150)
    da = rng.randint(1, 5) * 1000

    headers = ["Account", "Folio", "Debit (R)", "Credit (R)"]
    data_rows = [
        ["Debtors control", "B6", str(dc), ""],
        ["Trading stock", "B5", str(ts), ""],
        ["Sales", "N1", "", str(sales)],
        ["Cost of sales", "N2", str(cos), ""],
        ["Debtors allowance", "N3", str(da), ""],
    ]
    rows, correct_map = make_grid_rows(data_rows, given_coords={(i, 0) for i in range(5)} | {(i, 1) for i in range(5)})
    cell_hints = {
        "t0_r0_c2": f"Debtors control is an Asset -> Debit = {dc}.",
        "t0_r1_c2": f"Trading stock is an Asset -> Debit = {ts}.",
        "t0_r2_c3": f"Sales is Income -> Credit = {sales}.",
        "t0_r3_c2": f"Cost of sales is an Expense -> Debit = {cos}.",
        "t0_r4_c2": f"Debtors allowance reduces Sales (contra-income) -> Debit = {da}.",
    }
    prompt = (
        f"Place these closing General Ledger balances of **{biz}** into the correct **Debit** or **Credit** column "
        "of the **Trial Balance extract** *(leave opposite side empty; digits only)*:\n"
        f"Debtors control {fmt_r(dc)} | Trading stock {fmt_r(ts)} | Sales {fmt_r(sales)} | Cost of sales {fmt_r(cos)} | Debtors allowance {fmt_r(da)}."
    )
    md_rows = "\n".join(f"| {r[0]} | {r[1]} | {r[2] or '—'} | {r[3] or '—'} |" for r in data_rows)
    worked = "**Trial Balance Extract** [5 marks]\n\n| Account | Fol | Debit | Credit |\n| --- | --- | --- | --- |\n" + md_rows
    return build_table(
        rng,
        qid="g9_dl_47",
        subskill="47_trial_balance_extract_after_debtors_postings_table",
        title="Place Debtors & Sales Accounts in Trial Balance",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"Dr: DC {dc}, TS {ts}, CoS {cos}, DA {da}; Cr: Sales {sales}",
        marks=5,
        hints={
            "tier_1": "Assets, Expenses, and Debtors Allowance sit on Debit; Income (Sales) sits on Credit.",
            "tier_2": "Only Sales belongs in Credit among these 5 accounts.",
            "tier_3": f"Dr: {dc}, {ts}, {cos}, {da}; Cr: {sales}.",
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"{r[0]} placed on correct side", "marks": 1, "editable": True}
            for i, r in enumerate(data_rows)
        ],
        misconception_tags=["crediting_debtors_allowance_or_cost_of_sales_in_trial_balance"],
        journal_type="trial_balance",
    )


def arch_48_credit_control_collection_ratio_days_assessment_calc(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    credit_sales = rng.randint(20, 50) * 1000
    pct_collected = rng.choice([65, 70, 75, 80, 85])
    collected = credit_sales * pct_collected // 100

    prompt = (
        f"**{biz}** recorded total credit sales (`DJ`) of **{fmt_r(credit_sales)}** and collected **{fmt_r(collected)}** "
        f"from debtors (`CRJ Debtors Control`) during the same period (opening debtors balance was R0).\n\n"
        "Calculate the **collection percentage (%)** achieved on credit sales [2].\n"
        "*(Enter the percentage number only, e.g. `80`.)*"
    )
    worked = (
        "**Debtors Collection Efficiency** [2 marks]\n\n"
        f"$$\\frac{{\\text{{CRJ Collections}}}}{{\\text{{DJ Credit Sales}}}} \\times 100 = \\frac{{{collected}}}{{{credit_sales}}} \\times 100 = {pct_collected}\\%$$\n"
        f"Answer: `{pct_collected}`"
    )
    return build_short(
        rng,
        qid="g9_dl_48",
        subskill="48_credit_control_collection_ratio_days_assessment_calc",
        title="Calculate Debtors Collection Percentage",
        prompt=prompt,
        expected_answer=str(pct_collected),
        worked_solution=worked,
        marks=2,
        hints={
            "tier_1": "Divide cash collected from debtors by total credit sales, then multiply by 100.",
            "tier_2": f"Calculate ({collected} / {credit_sales}) × 100.",
            "tier_3": f"Collection rate = {pct_collected}%.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Collection rate = {pct_collected}%", "marks": 2, "editable": True},
        ],
        misconception_tags=["dividing_credit_sales_by_cash_collected"],
    )


def arch_49_trace_credit_note_to_dl_gl_and_accounting_equation_mcq(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    debtor, fol = rng.choice(DEBTOR_POOL[:4])
    sp = rng.choice([600, 900, 1200, 1500])
    cp = sp * 100 // 150

    prompt = (
        f"**{debtor} ({fol})** returns undamaged stock invoiced at **{fmt_r(sp)}** (cost **{fmt_r(cp)}**) to **{biz}**.\n\n"
        "Which option traces **every single effect** of this Credit Note across Subsidiary Journal, Debtors Ledger, General Ledger, and Accounting Equation?"
    )
    correct = f"DAJ -> {debtor} ({fol}) Credit (-) {fmt_r(sp)} -> GL Dr Debtors allowance/Cr Debtors control ({fmt_r(sp)}) & Dr Trading stock/Cr Cost of sales ({fmt_r(cp)}) -> Net A -{fmt_r(sp - cp)}, OE -{fmt_r(sp - cp)}."
    distractors = [
        f"DJ -> {debtor} ({fol}) Debit (+) {fmt_r(sp)} -> GL Dr Debtors control/Cr Sales ({fmt_r(sp)}) -> Net A +{fmt_r(sp - cp)}.",
        f"CRJ -> {debtor} ({fol}) Credit (-) {fmt_r(sp)} -> GL Dr Bank/Cr Debtors control ({fmt_r(sp)}) -> Net A 0.",
        f"DAJ -> {debtor} ({fol}) Debit (+) {fmt_r(sp)} -> GL Dr Cost of sales/Cr Trading stock ({fmt_r(cp)}) -> L -{fmt_r(cp)}.",
    ]
    return build_mcq(
        rng,
        qid="g9_dl_49",
        subskill="49_trace_credit_note_to_dl_gl_and_accounting_equation_mcq",
        title="Full Trace of Credit Note Across Books & Equation",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A stock return enters the **DAJ**, credits `{debtor} ({fol})`, reverses Selling Price (`Dr Debtors allowance / Cr Debtors control`) "
            f"and Cost Price (`Dr Trading stock / Cr Cost of sales`), leaving net Assets and Equity down by gross profit `{fmt_r(sp - cp)}`."
        ),
        hints={
            "tier_1": "Trace Source -> DAJ -> Debtors Ledger Credit (-) -> Dual GL reversal -> Net Gross Profit reversal.",
            "tier_2": f"Selling leg -{sp}, Cost leg +{cp} -> Net A & OE = -{sp - cp}.",
            "tier_3": correct,
        },
        misconception_tags=["forgetting_dual_impact_across_dl_gl_and_equation"],
    )


def arch_50_capstone_dl_control_gl_and_accounting_equation_audit_table(rng: random.Random, mode: str = "practice") -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    biz = biz_name(rng, sc)
    d1, d2 = pick_debtors(rng, 2)
    open1, open2 = rng.randint(5, 12) * 1000, rng.randint(3, 9) * 1000
    open_tot = open1 + open2
    sale1 = rng.randint(4, 10) * 1000
    sale2 = rng.randint(2, 8) * 1000
    dj_tot = sale1 + sale2
    ret1 = 1000
    rec1 = rng.randint(3, 6) * 1000
    rec2 = rng.randint(2, 5) * 1000
    crj_tot = rec1 + rec2

    close1 = open1 + sale1 - ret1 - rec1
    close2 = open2 + sale2 - rec2
    close_tot = close1 + close2

    headers = ["Capstone Reconciliation Item", "Amount (R)"]
    data_rows = [
        [f"{d1[0]} (D1) Closing Debtors Ledger Balance", str(close1)],
        [f"{d2[0]} (D2) Closing Debtors Ledger Balance", str(close2)],
        ["Total Debtors List", str(close_tot)],
        ["General Ledger Debtors Control (B6) Opening b/d", str(open_tot)],
        ["Add: Total Credit Sales (DJ)", str(dj_tot)],
        ["Less: DAJ Allowances & CRJ Receipts", str(ret1 + crj_tot)],
        ["General Ledger Debtors Control (B6) Closing b/d", str(close_tot)],
    ]
    given = {(i, 0) for i in range(7)} | {(3, 1), (4, 1), (5, 1)}
    rows, correct_map = make_grid_rows(data_rows, given_coords=given)
    cell_hints = {
        "t0_r0_c1": f"{d1[0]}: {open1} + {sale1} - {ret1} - {rec1} = {close1}.",
        "t0_r1_c1": f"{d2[0]}: {open2} + {sale2} - {rec2} = {close2}.",
        "t0_r2_c1": f"Total Debtors List = {close1} + {close2} = {close_tot}.",
        "t0_r6_c1": f"Debtors Control Closing = {open_tot} + {dj_tot} - {ret1 + crj_tot} = {close_tot} (must match List!).",
    }
    prompt = (
        f"Perform a full **Debtors Reconciliation Capstone** for **{biz}**:\n"
        f"- **{d1[0]} (D1):** b/d {fmt_r(open1)}; DJ +{fmt_r(sale1)}; DAJ -{fmt_r(ret1)}; CRJ -{fmt_r(rec1)}\n"
        f"- **{d2[0]} (D2):** b/d {fmt_r(open2)}; DJ +{fmt_r(sale2)}; CRJ -{fmt_r(rec2)}\n\n"
        "Complete D1 closing, D2 closing, Total Debtors List, and GL Debtors Control Closing Balance *(digits only)*."
    )
    worked = (
        "**Capstone Debtors Ledger & Control Reconciliation** [8 marks]\n\n"
        "| Item | Amount (R) |\n| --- | --- |\n"
        f"| {d1[0]} (D1) Closing | **{close1}** |\n"
        f"| {d2[0]} (D2) Closing | **{close2}** |\n"
        f"| **Total Debtors List** | **{close_tot}** |\n"
        f"| GL Debtors Control (B6) Closing | **{close_tot}** |\n\n"
        f"*Reconciled: Debtors List ({fmt_r(close_tot)}) == Debtors Control ({fmt_r(close_tot)}).*"
    )
    return build_table(
        rng,
        qid="g9_dl_50",
        subskill="50_capstone_dl_control_gl_and_accounting_equation_audit_table",
        title="Capstone: Reconcile Debtors Ledger, List & Control",
        prompt=prompt,
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=f"D1={close1}; D2={close2}; Debtors List=Debtors Control={close_tot}",
        marks=8,
        hints={
            "tier_1": "Compute each debtor's individual DL closing balance first, then verify their sum matches GL Control.",
            "tier_2": f"D1 = {open1}+{sale1}-{ret1}-{rec1}; D2 = {open2}+{sale2}-{rec2}.",
            "tier_3": f"D1={close1}, D2={close2}, Total List = Debtors Control = {close_tot}.",
        },
        marking_points=[
            {"id": "mp_1", "desc": f"D1={close1} & D2={close2}", "marks": 4, "editable": True},
            {"id": "mp_2", "desc": f"Debtors List & Debtors Control reconcile at {close_tot}", "marks": 4, "editable": True},
        ],
        misconception_tags=["unreconciled_debtors_list_and_control_account"],
        journal_type="reconciliation_capstone",
    )


ARCHETYPE_BUILDERS_26_50: Dict[str, Callable[[random.Random, str], Dict[str, Any]]] = {
    "26_complete_trading_stock_t_account_with_dj_crj_cpj_daj_table": arch_26_complete_trading_stock_t_account_with_dj_crj_cpj_daj_table,
    "27_complete_sales_nominal_t_account_table": arch_27_complete_sales_nominal_t_account_table,
    "28_complete_cost_of_sales_nominal_t_account_table": arch_28_complete_cost_of_sales_nominal_t_account_table,
    "29_complete_debtors_allowance_t_account_table": arch_29_complete_debtors_allowance_t_account_table,
    "30_calculate_markup_profit_pct_from_ledger_balances": arch_30_calculate_markup_profit_pct_from_ledger_balances,
    "31_derive_missing_dj_or_crj_cos_from_trading_stock_calc": arch_31_derive_missing_dj_or_crj_cos_from_trading_stock_calc,
    "32_debit_credit_sign_rules_assets_equity_liabilities_svg": arch_32_debit_credit_sign_rules_assets_equity_liabilities_svg,
    "33_accounting_equation_credit_sale_selling_price_leg_table": arch_33_accounting_equation_credit_sale_selling_price_leg_table,
    "34_accounting_equation_credit_sale_cost_price_leg_table": arch_34_accounting_equation_credit_sale_cost_price_leg_table,
    "35_accounting_equation_credit_sale_dual_entry_full_table": arch_35_accounting_equation_credit_sale_dual_entry_full_table,
    "36_accounting_equation_net_profit_impact_calc": arch_36_accounting_equation_net_profit_impact_calc,
    "37_accounting_equation_debtor_payment_receipt_table": arch_37_accounting_equation_debtor_payment_receipt_table,
    "38_accounting_equation_debtors_return_selling_price_leg_table": arch_38_accounting_equation_debtors_return_selling_price_leg_table,
    "39_accounting_equation_debtors_return_cost_price_leg_table": arch_39_accounting_equation_debtors_return_cost_price_leg_table,
    "40_accounting_equation_debtors_allowance_overcharge_table": arch_40_accounting_equation_debtors_allowance_overcharge_table,
    "41_accounting_equation_cash_vs_credit_sale_comparison_svg": arch_41_accounting_equation_cash_vs_credit_sale_comparison_svg,
    "42_multi_transaction_accounting_equation_5rows_table": arch_42_multi_transaction_accounting_equation_5rows_table,
    "43_net_asset_and_equity_movement_summary_calc": arch_43_net_asset_and_equity_movement_summary_calc,
    "44_identify_error_treating_debtor_receipt_as_income_mcq": arch_44_identify_error_treating_debtor_receipt_as_income_mcq,
    "45_posting_date_rule_individual_daily_vs_month_end_totals": arch_45_posting_date_rule_individual_daily_vs_month_end_totals,
    "46_reconstruct_crj_bank_receipts_from_debtors_control_gl_calc": arch_46_reconstruct_crj_bank_receipts_from_debtors_control_gl_calc,
    "47_trial_balance_extract_after_debtors_postings_table": arch_47_trial_balance_extract_after_debtors_postings_table,
    "48_credit_control_collection_ratio_days_assessment_calc": arch_48_credit_control_collection_ratio_days_assessment_calc,
    "49_trace_credit_note_to_dl_gl_and_accounting_equation_mcq": arch_49_trace_credit_note_to_dl_gl_and_accounting_equation_mcq,
    "50_capstone_dl_control_gl_and_accounting_equation_audit_table": arch_50_capstone_dl_control_gl_and_accounting_equation_audit_table,
}
