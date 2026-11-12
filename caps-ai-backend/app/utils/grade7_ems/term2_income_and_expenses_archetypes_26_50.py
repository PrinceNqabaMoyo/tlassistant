"""Grade 7 Economic and Management Sciences - Term 2: Income and Expenses (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/EMS_Gr7/Term 2/02. Income and Expenses.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, BUSINESS_TYPES, NAMES, get_ems_scenario
from .term2_income_and_expenses_archetypes_01_25 import (
    _fmt_r,
    _make_calc,
    _make_ledger,
    _make_mcq,
    _make_typed,
)


def _svg_profit_waterfall(biz: str, sales: int, cos: int, opex: int) -> str:
    """Seed-varied business profitability waterfall bars."""
    gp = sales - cos
    np = gp - opex
    max_v = max(sales, 1)
    h_s = 132
    h_gp = max(24, int(round((gp / max_v) * 132)))
    h_np = max(18, int(round((max(np, 0) / max_v) * 132)))
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 235" width="540" height="235">'
        '<rect width="540" height="235" fill="#f8fafc" rx="8"/>'
        f'<text x="270" y="24" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{biz}: Revenue to Net Profit Breakdown</text>'
        '<line x1="55" y1="184" x2="495" y2="184" stroke="#64748b" stroke-width="2"/>'
        f'<rect x="75" y="{184 - h_s}" width="105" height="{h_s}" fill="#0284c7" rx="4"/>'
        f'<text x="127" y="{174 - h_s}" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#0369a1">{_fmt_r(sales)}</text>'
        '<text x="127" y="203" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#1e293b">Sales Income</text>'
        f'<rect x="218" y="{184 - h_gp}" width="105" height="{h_gp}" fill="#0d9488" rx="4"/>'
        f'<text x="270" y="{174 - h_gp}" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#0f766e">{_fmt_r(gp)}</text>'
        '<text x="270" y="203" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#1e293b">Gross Profit</text>'
        f'<rect x="361" y="{184 - h_np}" width="105" height="{h_np}" fill="#16a34a" rx="4"/>'
        f'<text x="413" y="{174 - h_np}" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#15803d">Net Profit = ?</text>'
        '<text x="413" y="203" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#1e293b">Net Profit</text>'
        f'<text x="270" y="224" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#475569">Cost of Sales: {_fmt_r(cos)} | Operating Expenses: {_fmt_r(opex)}</text>'
        "</svg>"
    )


def _svg_unit_trust_flow(n_inv: int, monthly: int, firm: str) -> str:
    """Seed-varied collective Unit Trust pooling visual."""
    pool = n_inv * monthly
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 190" width="560" height="190">'
        '<rect width="560" height="190" fill="#f8fafc" rx="8"/>'
        f'<text x="280" y="24" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0f172a">Unit Trust Collective Investment Flow ({firm})</text>'
        '<rect x="28" y="64" width="142" height="76" fill="#e0f2fe" stroke="#0284c7" rx="6"/>'
        f'<text x="99" y="96" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0c4a6e">{n_inv} Small Investors</text>'
        f'<text x="99" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#0369a1">{_fmt_r(monthly)} each/month</text>'
        '<line x1="170" y1="102" x2="205" y2="102" stroke="#475569" stroke-width="2.5"/>'
        '<polygon points="205,97 215,102 205,107" fill="#475569"/>'
        '<rect x="217" y="64" width="128" height="76" fill="#fef3c7" stroke="#d97706" rx="6"/>'
        '<text x="281" y="96" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#78350f">Bank / Trust</text>'
        f'<text x="281" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#92400e">Pooled = ? ({_fmt_r(pool)})</text>'
        '<line x1="345" y1="102" x2="380" y2="102" stroke="#475569" stroke-width="2.5"/>'
        '<polygon points="380,97 390,102 380,107" fill="#475569"/>'
        '<rect x="392" y="64" width="142" height="76" fill="#dcfce7" stroke="#16a34a" rx="6"/>'
        f'<text x="463" y="96" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#14532d">{firm}</text>'
        '<text x="463" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#166534">Diversified Shares</text>'
        "</svg>"
    )


def build_26_service_vs_retail_primary_business_income(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("hairdressing salon", "Current Income (fees for services rendered)", "Sales of retail inventory"),
        ("plumbing repair business", "Current Income (fees for services rendered)", "Dividend income from JSE shares"),
        ("grocery tuckshop", "Sales of trading goods", "Royalties on mineral extraction"),
    ]
    biz, correct, alt = rng.choice(cases)
    amt = rng.randrange(14000, 32000, 2000)
    prompt = (
        f"A {biz} in {rng.choice(AREAS)} collects {_fmt_r(amt)} from customers this week for its core activity. "
        f"What accounting name is given to this primary business income?"
    )
    distractors = [
        alt,
        "Capital contribution borrowed from commercial suppliers",
        "Municipal rates and water expense",
    ]
    sol = f"Service enterprises (salons, plumbers) record core revenue as **Current Income**; trading/retail enterprises (tuckshops) record core revenue as **Sales**. Answer: **{correct}**."
    return _make_mcq(
        rng, "26_service_vs_retail_primary_business_income", "Service vs Retail Primary Income", prompt,
        correct, distractors, sol,
        "Ask whether the business sells physical goods (Sales) or performs work/skills (Current Income).",
        "Distinguish trading income (Sales) from service fees (Current Income).",
        ["ems_confuses_sales_and_current_income"],
    )


def build_27_business_income_sources_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    v1 = rng.randrange(18000, 36000, 2000)
    v2 = rng.randrange(2500, 6000, 500)
    v3 = rng.randrange(300, 900, 100)
    v4 = rng.randrange(1200, 3200, 200)
    headers = ["Business Cash Inflow Description", "Amount (R)", "Standard Income Account"]
    rows_meta = [
        ("Cash received for goods sold to shoppers", v1, "Sales"),
        ("Monthly rent collected from sub-tenant", v2, "Rent Income"),
        ("Bank interest credited on savings balance", v3, "Interest Income"),
        ("Fee earned for repair services rendered", v4, "Current Income"),
    ]
    rows: List[List[Dict[str, Any]]] = []
    cmap: Dict[str, str] = {}
    chints: Dict[str, str] = {}
    md_lines = [f"| {' | '.join(headers)} |", "|---|---:|---|"]
    for i, (desc, amt, acct) in enumerate(rows_meta):
        cid = f"r{i}_c2"
        cmap[cid] = acct
        chints[cid] = "Enter exact account name: Sales, Rent Income, Interest Income, or Current Income."
        rows.append([
            {"cell_id": f"r{i}_c0", "value": desc, "editable": False, "prefilled": True},
            {"cell_id": f"r{i}_c1", "value": _fmt_r(amt), "editable": False, "prefilled": True},
            {"cell_id": cid, "value": "", "editable": True, "expected": acct},
        ])
        md_lines.append(f"| {desc} | {_fmt_r(amt)} | {acct} |")
    prompt = f"Classify {sc['business_type']}'s four inflows in the business income schedule below."
    return _make_ledger(
        rng, "27_business_income_sources_classification_table", "Business Income Accounts Schedule",
        prompt, headers, rows, cmap, chints, "\n".join(md_lines),
        "Match each inflow to: Sales, Rent Income, Interest Income, or Current Income.",
        "Goods sold = Sales; services = Current Income; property rent = Rent Income; bank interest = Interest Income.",
        ["ems_business_income_account_error"], marks=8,
    )


def build_28_royalties_and_mineral_royalty_bill(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("a South African author receiving a percentage on every textbook sold", "Royalties for intellectual property"),
        ("a platinum mining house paying the state for extracting non-renewable minerals", "Mineral resource royalties paid to the state"),
        ("a musician earning streaming fees each time a recorded song is licensed", "Royalties for creative copyright usage"),
    ]
    desc, correct = rng.choice(cases)
    amt = rng.randrange(15000, 60000, 5000)
    prompt = (
        f"In EMS, **royalties** cover payments for using either intellectual property (books, music, patents) OR extracting mineral resources "
        f"(such as under South Africa's Mineral and Petroleum Resources Royalty legislation). Which description matches {desc} ({_fmt_r(amt)})?"
    )
    distractors = [
        "Dividends distributed exclusively to municipal electricity technicians",
        "Hourly factory wages paid for overtime shifts",
        "Monthly shop rent paid for storing stationery",
    ]
    sol = f"**{correct}** accurately describes royalty cash flows of {_fmt_r(amt)} in that context."
    return _make_mcq(
        rng, "28_royalties_and_mineral_royalty_bill", "Intellectual & Mineral Royalties", prompt,
        correct, distractors, sol,
        "Remember royalties apply both to copyright/patents and to natural mineral extraction.",
        "Royalties differ from wages (work) and dividends (share ownership profits).",
        ["ems_royalties_misconception"],
    )


def build_29_shares_shareholders_and_dividends_concept(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cap = rng.randrange(200000, 600000, 50000)
    prompt = (
        f"To raise {_fmt_r(cap)} for expansion, {sc['business_type']} converts into a company and issues **shares** to public buyers. "
        f"Define the terms **shares**, **shareholders**, and **dividends**, and explain how the business and investors both benefit."
    )
    mps = [
        f"Shares are equal ownership units issued by a company to raise capital (here {_fmt_r(cap)}).",
        "Shareholders are the people or institutions who buy shares and become part-owners of the company.",
        "Dividends are the portion of company profits distributed back to shareholders as a return on investment.",
        "The company receives capital without bank loan interest, while shareholders earn passive dividend income and potential share value growth.",
    ]
    sample = (
        f"- **Shares**: Ownership portions sold to raise {_fmt_r(cap)} in capital.\n"
        "- **Shareholders**: Part-owners who purchased those shares.\n"
        "- **Dividends**: Cash profits shared among shareholders when the business performs profitably."
    )
    return _make_typed(
        rng, "29_shares_shareholders_and_dividends_concept", "Shares, Shareholders & Dividends", prompt,
        mps, ["shares", "shareholders", "dividends", "capital", "profit"], sample,
        "Define each of the three words in turn: ownership units, owners, and profit payouts.",
        "Contrast equity share capital with interest-bearing loans.",
        ["ems_confuses_dividends_and_interest"],
    )


def build_30_dividend_payout_income_calculation(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    shares = rng.randrange(400, 1800, 100)
    div_rands = rng.choice([2, 3, 4, 5])
    total = shares * div_rands
    prompt = (
        f"{name} holds {shares} ordinary shares in a South African retail company. At financial year-end, the board declares a dividend of "
        f"{_fmt_r(div_rands)} per share. Calculate {name}'s total dividend income (numbers only)."
    )
    sol = f"Dividend Income = {shares} shares × {_fmt_r(div_rands)}/share = **{_fmt_r(total)}**"
    return _make_calc(
        rng, "30_dividend_payout_income_calculation", "Total Dividend Income Calculation", prompt,
        total, "Dividends = Number of Shares × Dividend per Share", sol,
        "Multiply shares held by the dividend declared per share.",
        f"{shares} × {div_rands} = {total}.",
        ["ems_dividend_multiplication_error"], marks=2,
    )


def build_31_business_startup_capital_vs_running_expenses(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("bakery", "buying two industrial deck ovens", "buying monthly flour, yeast, and paying electricity"),
        ("courier firm", "purchasing a commercial delivery bakkie", "buying weekly petrol and paying toll fees"),
        ("tailoring studio", "buying heavy-duty industrial sewing machines", "paying monthly shop rent and thread supplies"),
    ]
    biz, cap_item, run_item = rng.choice(cases)
    cap_amt = rng.randrange(35000, 95000, 5000)
    prompt = (
        f"A new {biz} in {rng.choice(AREAS)} must manage start-up equipment vs ongoing running expenses. "
        f"Which outlay represents a **capital equipment investment (asset)** worth {_fmt_r(cap_amt)} rather than an operating expense?"
    )
    correct = f"{cap_item.capitalize()} for multi-year production"
    distractors = [
        run_item.capitalize(),
        "Paying weekly casual assistant wages",
        "Replacing burnt-out light bulbs and cleaning detergent",
    ]
    sol = f"**{correct}** acquires a durable productive asset used for years, whereas {run_item} is a recurring day-to-day running expense."
    return _make_mcq(
        rng, "31_business_startup_capital_vs_running_expenses", "Capital Equipment vs Running Expenses", prompt,
        correct, distractors, sol,
        "Look for long-lasting machinery/vehicles bought once to enable production.",
        "Consumables (flour, petrol, thread) and monthly rent/wages are running expenses.",
        ["ems_confuses_capex_and_opex"],
    )


def build_32_business_operational_and_statutory_expenses(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    uif = rng.randrange(400, 1200, 100)
    prompt = (
        f"{sc['business_type']} employs three full-time assistants and pays employer UIF ({_fmt_r(uif)}), municipal water & electricity, "
        f"advertising flyers, and fire insurance. Which statement correctly classifies all four outlays?"
    )
    correct = "All four are legitimate operating and statutory business expenses deducted from gross profit to find net profit."
    distractors = [
        "All four count as personal household expenses because staff work in town.",
        "UIF and fire insurance are non-current assets listed on a Statement of Net Worth.",
        "Advertising and electricity increase sales revenue directly on the balance sheet.",
    ]
    sol = "Wages/UIF, utilities, advertising, and insurance are essential business operating expenses required to keep the enterprise compliant and trading."
    return _make_mcq(
        rng, "32_business_operational_and_statutory_expenses", "Operational & Statutory Business Expenses", prompt,
        correct, distractors, sol,
        "Check whether each outlay is consumed in running the business legally and safely.",
        "Statutory staff contributions like UIF, municipal bills, marketing, and insurance are operating expenses.",
        ["ems_statutory_expense_misclassification"],
    )


def build_33_industry_specific_expense_profile_analysis(rng: random.Random) -> Dict[str, Any]:
    b1, b2 = ("local bakery", "transport courier") if rng.choice([True, False]) else ("hair salon", "brick-making workshop")
    rent = rng.randrange(4500, 8500, 500)
    prompt = (
        f"In {rng.choice(AREAS)}, both a **{b1}** and a **{b2}** pay {_fmt_r(rent)}/month shop rent, yet their other main costs differ sharply. "
        f"Identify two industry-specific expenses for each business and explain why managers must budget for those differences."
    )
    mps = [
        f"Identifies two genuine industry-specific costs for the {b1} (e.g., ingredients/utilities/salon stock).",
        f"Identifies two genuine industry-specific costs for the {b2} (e.g., fuel/tyres/maintenance/cement/kiln energy).",
        "Explains that specialised inputs rise and fall with production/service volume (variable costs).",
        "Shows accurate cost forecasting prevents pricing errors and cash shortages.",
    ]
    sample = (
        f"- **{b1.capitalize()}**: Specialised materials/stock and heavy utility/equipment costs tied directly to customer orders.\n"
        f"- **{b2.capitalize()}**: Dedicated fleet/production consumables and maintenance.\n"
        f"- **Why it matters**: Beyond shared rent ({_fmt_r(rent)}), each business must price goods/services above its unique variable costs."
    )
    return _make_typed(
        rng, "33_industry_specific_expense_profile_analysis", "Industry-Specific Expense Profiles", prompt,
        mps, [b1.split()[-1], b2.split()[-1], "variable", "budget", "pricing"], sample,
        f"List specific materials or energy used only by a {b1} vs a {b2}.",
        "Link unique business costs to accurate selling prices and cash planning.",
        ["ems_generic_expense_answers"],
    )


def build_34_business_expense_categories_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    c_cos = rng.randrange(15000, 32000, 1000)
    c_sal = rng.randrange(6000, 14000, 500)
    c_adv = rng.randrange(900, 2400, 100)
    c_int = rng.randrange(400, 1200, 100)
    headers = ["Business Payment Description", "Amount (R)", "Expense Category"]
    rows_meta = [
        ("Wholesale stock purchased for resale", c_cos, "Cost of Sales"),
        ("Monthly staff salaries and UIF", c_sal, "Operating Expense"),
        ("Radio and poster advertising campaign", c_adv, "Operating Expense"),
        ("Interest paid on business bank overdraft", c_int, "Finance Cost"),
    ]
    rows: List[List[Dict[str, Any]]] = []
    cmap: Dict[str, str] = {}
    chints: Dict[str, str] = {}
    md_lines = [f"| {' | '.join(headers)} |", "|---|---:|---|"]
    for i, (desc, amt, cat) in enumerate(rows_meta):
        cid = f"r{i}_c2"
        cmap[cid] = cat
        chints[cid] = "Enter exact phrase: 'Cost of Sales', 'Operating Expense', or 'Finance Cost'."
        rows.append([
            {"cell_id": f"r{i}_c0", "value": desc, "editable": False, "prefilled": True},
            {"cell_id": f"r{i}_c1", "value": _fmt_r(amt), "editable": False, "prefilled": True},
            {"cell_id": cid, "value": "", "editable": True, "expected": cat},
        ])
        md_lines.append(f"| {desc} | {_fmt_r(amt)} | {cat} |")
    prompt = f"Classify {sc['business_type']}'s four business expenses below using **Cost of Sales**, **Operating Expense**, or **Finance Cost**."
    return _make_ledger(
        rng, "34_business_expense_categories_table", "Business Expense Categories Table",
        prompt, headers, rows, cmap, chints, "\n".join(md_lines),
        "Cost of Sales = cost of stock bought to resell; Finance Cost = interest on loans/overdrafts.",
        "Salaries, rent, electricity, and marketing are Operating Expenses.",
        ["ems_cos_vs_opex_error"], marks=8,
    )


def build_35_gross_profit_formula_and_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sales = rng.randrange(32000, 72000, 2000)
    cos = rng.randrange(18000, sales - 8000, 1000)
    gp = sales - cos
    prompt = (
        f"During July, {sc['business_type']} recorded total Sales of {_fmt_r(sales)}. The Cost of Sales for goods sold to customers was {_fmt_r(cos)}. "
        f"Calculate {sc['business_type']}'s **Gross Profit** (numbers only)."
    )
    sol = f"Gross Profit = Sales Income - Cost of Sales = {_fmt_r(sales)} - {_fmt_r(cos)} = **{_fmt_r(gp)}**"
    return _make_calc(
        rng, "35_gross_profit_formula_and_calculation", "Gross Profit Calculation", prompt,
        gp, "Gross Profit = Sales - Cost of Sales", sol,
        "Subtract the cost of inventory sold from total Sales revenue.",
        f"{sales} - {cos} = {gp}.",
        ["ems_adds_cos_to_sales"], marks=3,
    )


def build_36_net_profit_after_operating_expenses_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sales = rng.randrange(48000, 88000, 2000)
    cos = rng.randrange(22000, 36000, 2000)
    rent = rng.randrange(4500, 7500, 500)
    wages = rng.randrange(5000, 9000, 500)
    util = rng.randrange(1200, 2400, 200)
    gp = sales - cos
    opex = rent + wages + util
    np = gp - opex
    prompt = (
        f"{sc['business_type']} achieves Sales of {_fmt_r(sales)} with Cost of Sales of {_fmt_r(cos)}. Operating expenses for the month are "
        f"Rent {_fmt_r(rent)}, Wages {_fmt_r(wages)}, and Electricity {_fmt_r(util)}. Calculate **Net Profit** (numbers only)."
    )
    sol = (
        f"1. Gross Profit = {_fmt_r(sales)} - {_fmt_r(cos)} = {_fmt_r(gp)}\n"
        f"2. Total Operating Expenses = {_fmt_r(rent)} + {_fmt_r(wages)} + {_fmt_r(util)} = {_fmt_r(opex)}\n"
        f"3. Net Profit = {_fmt_r(gp)} - {_fmt_r(opex)} = **{_fmt_r(np)}**"
    )
    return _make_calc(
        rng, "36_net_profit_after_operating_expenses_calc", "Net Profit Calculation", prompt,
        np, "Net Profit = (Sales - Cost of Sales) - Total Operating Expenses", sol,
        "First find Gross Profit (Sales - Cost of Sales), then subtract all operating expenses.",
        f"GP = {gp}; OpEx = {opex}; Net Profit = {np}.",
        ["ems_forgets_operating_expenses_in_net_profit"], marks=5,
    )


def build_37_profitability_waterfall_bar_visual(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sales = rng.randrange(55000, 95000, 5000)
    cos = rng.randrange(20000, 35000, 2500)
    opex = rng.randrange(8000, 16000, 1000)
    gp = sales - cos
    np = gp - opex
    svg = _svg_profit_waterfall(sc["business_type"], sales, cos, opex)
    prompt = (
        f"Use the profitability breakdown for {sc['business_type']}: Sales Income is {_fmt_r(sales)}, Cost of Sales is {_fmt_r(cos)} "
        f"(leaving Gross Profit {_fmt_r(gp)}), and Operating Expenses are {_fmt_r(opex)}. Calculate the missing **Net Profit** (numbers only)."
    )
    sol = f"Net Profit = Gross Profit ({_fmt_r(gp)}) - Operating Expenses ({_fmt_r(opex)}) = **{_fmt_r(np)}**."
    return _make_calc(
        rng, "37_profitability_waterfall_bar_visual", "Profitability Waterfall Visual Calculation", prompt,
        np, "Net Profit = Gross Profit - Operating Expenses", sol,
        "Gross Profit already accounts for Cost of Sales; now subtract Operating Expenses.",
        f"{gp} - {opex} = {np}.",
        ["ems_double_subtracts_cost_of_sales"], marks=3,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_38_business_income_summary_statement_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    ci = rng.randrange(24000, 42000, 2000)
    ri = rng.randrange(3000, 6000, 500)
    tot_inc = ci + ri
    sal = rng.randrange(8000, 14000, 1000)
    ad = rng.randrange(1200, 2800, 200)
    wat = rng.randrange(1500, 3000, 300)
    tot_exp = sal + ad + wat
    np = tot_inc - tot_exp
    headers = ["Account", "Category", "Amount (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Current Income (services)", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": "Income", "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": str(ci), "editable": False, "prefilled": True}],
        [{"cell_id": "r1_c0", "value": "Rent Income (sub-let stall)", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": "Income", "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": str(ri), "editable": False, "prefilled": True}],
        [{"cell_id": "r2_c0", "value": "Total Business Income", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": "Subtotal", "editable": False, "prefilled": True},
         {"cell_id": "r2_c2", "value": "", "editable": True, "expected": str(tot_inc)}],
        [{"cell_id": "r3_c0", "value": "Staff Salaries & UIF", "editable": False, "prefilled": True},
         {"cell_id": "r3_c1", "value": "Expense", "editable": False, "prefilled": True},
         {"cell_id": "r3_c2", "value": str(sal), "editable": False, "prefilled": True}],
        [{"cell_id": "r4_c0", "value": "Advertising & Signage", "editable": False, "prefilled": True},
         {"cell_id": "r4_c1", "value": "Expense", "editable": False, "prefilled": True},
         {"cell_id": "r4_c2", "value": str(ad), "editable": False, "prefilled": True}],
        [{"cell_id": "r5_c0", "value": "Water & Electricity", "editable": False, "prefilled": True},
         {"cell_id": "r5_c1", "value": "Expense", "editable": False, "prefilled": True},
         {"cell_id": "r5_c2", "value": str(wat), "editable": False, "prefilled": True}],
        [{"cell_id": "r6_c0", "value": "Total Business Expenses", "editable": False, "prefilled": True},
         {"cell_id": "r6_c1", "value": "Subtotal", "editable": False, "prefilled": True},
         {"cell_id": "r6_c2", "value": "", "editable": True, "expected": str(tot_exp)}],
        [{"cell_id": "r7_c0", "value": "Net Profit", "editable": False, "prefilled": True},
         {"cell_id": "r7_c1", "value": "Result", "editable": False, "prefilled": True},
         {"cell_id": "r7_c2", "value": "", "editable": True, "expected": str(np)}],
    ]
    cmap = {"r2_c2": str(tot_inc), "r6_c2": str(tot_exp), "r7_c2": str(np)}
    chints = {
        "r2_c2": "Add Current Income + Rent Income (digits only).",
        "r6_c2": "Add Salaries + Advertising + Water & Electricity (digits only).",
        "r7_c2": "Subtract Total Expenses from Total Income.",
    }
    md_memo = (
        f"| Account | Category | Amount (R) |\n|---|---|---:|\n"
        f"| Current Income | Income | {ci} |\n| Rent Income | Income | {ri} |\n"
        f"| **Total Business Income** | Subtotal | **{tot_inc}** |\n"
        f"| Staff Salaries & UIF | Expense | {sal} |\n| Advertising | Expense | {ad} |\n| Water & Electricity | Expense | {wat} |\n"
        f"| **Total Business Expenses** | Subtotal | **{tot_exp}** |\n| **Net Profit** | Result | **{np}** |"
    )
    prompt = f"Complete {sc['business_type']}'s Income Summary table below (enter plain integer amounts without 'R' or spaces)."
    return _make_ledger(
        rng, "38_business_income_summary_statement_table", "Business Income & Profit Table",
        prompt, headers, rows, cmap, chints, md_memo,
        "Sum all incomes first, sum all expenses second, then subtract.",
        f"Total Income = {tot_inc}; Total Expenses = {tot_exp}; Net Profit = {np}.",
        ["ems_income_summary_table_error"], marks=6,
    )


def build_39_break_even_revenue_deficit_reverse_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    tot_exp = rng.randrange(18000, 34000, 1000)
    earned = rng.randrange(11000, tot_exp - 2000, 1000)
    shortfall = tot_exp - earned
    prompt = (
        f"{sc['business_type']} has total monthly expenses of {_fmt_r(tot_exp)} and has earned {_fmt_r(earned)} in sales so far. "
        f"How much additional income must the business generate before month-end just to break even (R0 loss) (numbers only)?"
    )
    sol = f"Break-even Shortfall = Total Expenses - Current Income = {_fmt_r(tot_exp)} - {_fmt_r(earned)} = **{_fmt_r(shortfall)}**"
    return _make_calc(
        rng, "39_break_even_revenue_deficit_reverse_calc", "Break-Even Revenue Shortfall", prompt,
        shortfall, "Additional Income = Total Expenses - Income Earned So Far", sol,
        "To avoid a loss, Total Income must at least equal Total Expenses.",
        f"{tot_exp} - {earned} = {shortfall}.",
        ["ems_breakeven_shortfall_error"], marks=3,
    )


def build_40_current_cheque_account_daily_transactions_role(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    bal = rng.randrange(3500, 14500, 500)
    prompt = (
        f"{name} keeps {_fmt_r(bal)} in a bank Current (Cheque) account rather than a fixed-term savings account. "
        f"What is the primary purpose and key interest trade-off of a Current/Cheque account?"
    )
    correct = "It supports daily EFTs, debit card payments, and cash access, while typically earning zero or minimal interest."
    distractors = [
        "It locks funds away for 5 years to guarantee the highest possible stock-market return.",
        "It prevents the owner from buying groceries or paying supplier invoices during the month.",
        "It automatically converts personal utility bills into long-term company shares.",
    ]
    sol = f"Current/Cheque accounts prioritise convenient daily spending and payments on {_fmt_r(bal)}, so banks usually pay little or no interest on them."
    return _make_mcq(
        rng, "40_current_cheque_account_daily_transactions_role", "Current (Cheque) Account Role", prompt,
        correct, distractors, sol,
        "Compare everyday payment convenience (transactional account) vs high-interest long-term growth.",
        "Transactional convenience comes at the cost of zero/very low interest.",
        ["ems_confuses_cheque_with_investment_account"],
    )


def build_41_separating_personal_vs_business_savings(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randrange(8000, 24000, 2000)
    prompt = (
        f"{sc['entrepreneur']} saved {_fmt_r(amt)} from profits at {sc['business_type']} inside the same personal bank account used for household expenses. "
        f"Give three clear financial reasons why {sc['entrepreneur']} should move business savings into a separate business account."
    )
    mps = [
        "Measures true business performance clearly without mixing household cash inflows and outflows.",
        "Protects business emergency cash flow for restocking or quiet trading months from accidental personal spending.",
        "Simplifies bookkeeping, SARS tax reporting, and bank loan applications when needed.",
        f"Makes tracking the {_fmt_r(amt)} retained profit for business reinvestment straightforward.",
    ]
    sample = (
        f"1. **Accurate Tracking**: Separates household spending from {sc['business_type']}'s true {_fmt_r(amt)} profit reserve.\n"
        "2. **Cash-Flow Protection**: Prevents family emergencies from draining working capital needed to buy stock.\n"
        "3. **Tax & Audit Clarity**: Clean records make tax filing and financing far easier."
    )
    return _make_typed(
        rng, "41_separating_personal_vs_business_savings", "Separating Personal & Business Savings", prompt,
        mps, ["separate", "cash flow", "profit", "stock", "records"], sample,
        "Think about measuring real business profit, keeping emergency stock money safe, and clean records.",
        "Cover cash-flow protection plus financial accuracy.",
        ["ems_commingles_business_savings"],
    )


def build_42_retaining_profits_in_business_savings_strategy(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prof = rng.randrange(6000, 15000, 1000)
    pct = rng.choice([25, 30, 40])
    saved = (prof * pct) // 100
    prompt = (
        f"{sc['business_type']} earned {_fmt_r(prof)} net profit this month, and {sc['entrepreneur']} keeps {pct}% ({_fmt_r(saved)}) in a dedicated business savings reserve "
        f"instead of withdrawing everything. Explain two strategic advantages of saving part of business profits."
    )
    mps = [
        f"Builds internal expansion capital ({_fmt_r(saved)}/month) to buy new stock or equipment without costly interest-bearing loans.",
        "Provides an emergency buffer to pay fixed expenses like rent and wages during slow trading months or repairs.",
        "Earns interest income on idle reserves while strengthening business financial resilience.",
    ]
    sample = (
        f"1. **Debt-Free Growth**: Retaining {_fmt_r(saved)} monthly funds new inventory or equipment without borrowing at high interest.\n"
        "2. **Emergency Cushion**: Covers rent, wages, and sudden repairs if sales drop temporarily."
    )
    return _make_typed(
        rng, "42_retaining_profits_in_business_savings_strategy", "Retaining Business Profits Strategy", prompt,
        mps, ["reinvest", "emergency", "interest", "avoid loans", "reserve"], sample,
        "Think about funding expansion AND surviving quiet months without bank debt.",
        "Contrast self-funded growth using retained profits against high-interest loans.",
        ["ems_ignores_retained_earnings"],
    )


def build_43_investments_as_forced_tied_up_saving(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    yrs = rng.choice([3, 5])
    amt = rng.randrange(10000, 40000, 5000)
    prompt = (
        f"{name} places {_fmt_r(amt)} into a {yrs}-year investment product where funds cannot be withdrawn casually at an ATM. "
        f"In EMS, why is an investment described as 'forced saving'?"
    )
    correct = "Because the money is tied up out of easy circulation for a set medium-to-long term, preventing impulse spending while it grows in value."
    distractors = [
        "Because the commercial bank charges a fine for earning positive net profit.",
        "Because investors are legally forbidden from ever receiving their original capital back.",
        "Because the money sits in a daily cheque account earning 0% interest.",
    ]
    sol = f"Tying {_fmt_r(amt)} up for {yrs} years removes temptation to spend casually, giving compound returns time to grow wealth."
    return _make_mcq(
        rng, "43_investments_as_forced_tied_up_saving", "Investments as Forced Saving", prompt,
        correct, distractors, sol,
        "Consider why locking cash away for years helps discipline long-term wealth building.",
        "Money is tied up for medium/long-term growth rather than instant ATM withdrawal.",
        ["ems_misunderstands_forced_saving"],
    )


def build_44_savings_account_vs_investment_return_risk(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    amt = rng.randrange(15000, 50000, 5000)
    prompt = (
        f"{name} has {_fmt_r(amt)} to put aside and is choosing between an everyday **bank savings account** and a **medium/long-term investment** (e.g., shares or unit trusts). "
        f"Compare the two options in terms of **access (liquidity)**, **expected return**, **time horizon**, and **risk**."
    )
    mps = [
        "Liquidity/Access: Bank savings offer quick/easy withdrawal; investments tie money up longer.",
        "Expected Return: Investments generally earn higher long-term growth than ordinary savings accounts.",
        "Time Horizon: Savings suit short-term goals (<1 year); investments target medium-to-long term (3–5+ years).",
        "Risk: Bank savings carry very low risk to capital; market investments fluctuate and carry higher risk.",
    ]
    sample = (
        f"- **Bank Savings Account**: Immediate access for {_fmt_r(amt)}, very low risk, modest interest rate, best for short-term emergencies.\n"
        "- **Medium/Long-term Investment**: Funds committed for several years, higher potential growth above inflation, but returns carry market risk."
    )
    return _make_typed(
        rng, "44_savings_account_vs_investment_return_risk", "Savings Account vs Long-Term Investment", prompt,
        mps, ["access", "liquidity", "return", "time horizon", "risk"], sample,
        "Organise your comparison directly under the four headings asked: access, return, time horizon, risk.",
        "Remember the risk-return trade-off: higher potential long-term growth carries higher risk and lower instant liquidity.",
        ["ems_ignores_risk_return_tradeoff"],
    )


def build_45_unit_trust_collective_investment_pooling(rng: random.Random) -> Dict[str, Any]:
    amt = rng.randrange(300, 1000, 100)
    prompt = (
        f"Many South African savers can only contribute {_fmt_r(amt)} per month—too small to buy a diversified basket of major company shares alone. "
        f"How does a **Unit Trust** solve this problem?"
    )
    correct = "It pools small sums from many investors so a professional fund manager can invest the combined fund across diverse assets."
    distractors = [
        "It lends every saver's cash interest-free to local supermarkets for groceries.",
        "It replaces the saver's personal cheque card with an unpaid store credit card.",
        "It guarantees zero market movement by burying physical banknotes inside a bank vault.",
    ]
    sol = f"Unit trusts combine small contributions (like {_fmt_r(amt)}/month) from many people into one large professionally managed, diversified portfolio."
    return _make_mcq(
        rng, "45_unit_trust_collective_investment_pooling", "How Unit Trusts Work", prompt,
        correct, distractors, sol,
        "Focus on two core words: 'pooling' money together and 'professional' diversification.",
        "Small savers gain shared access to diversified assets run by asset managers.",
        ["ems_unit_trust_misconception"],
    )


def build_46_unit_trust_pooling_flow_diagram_visual(rng: random.Random) -> Dict[str, Any]:
    firm = rng.choice(["Allan Gray", "Coronation Fund Managers", "Old Mutual", "Investec"])
    n_inv = rng.randrange(200, 600, 50)
    monthly = rng.randrange(250, 750, 50)
    pool = n_inv * monthly
    svg = _svg_unit_trust_flow(n_inv, monthly, firm)
    prompt = (
        f"Inspect the collective Unit Trust flow managed by {firm}: {n_inv} small investors each contribute {_fmt_r(monthly)} per month "
        f"through their bank into the pooled trust. Calculate the total pooled investment capital collected each month (numbers only)."
    )
    sol = f"Total Monthly Pooled Capital for {firm} = {n_inv} × {_fmt_r(monthly)} = **{_fmt_r(pool)}**."
    return _make_calc(
        rng, "46_unit_trust_pooling_flow_diagram_visual", "Unit Trust Pooled Capital Visual", prompt,
        pool, "Total Pooled Capital = Number of Investors × Monthly Contribution", sol,
        "Multiply the number of investors by each person's monthly deposit.",
        f"{n_inv} × {monthly} = {pool}.",
        ["ems_unit_trust_pooling_calc_error"], marks=3,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def build_47_south_african_asset_managers_identification(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    valid_sets = [
        "Allan Gray, Coronation Fund Managers, Old Mutual, and Investec",
        "Coronation Fund Managers, Liberty Life, RMB, and Old Mutual",
        "Allan Gray, Investec, RMB, and Liberty Life",
    ]
    correct = rng.choice(valid_sets)
    amt = rng.randrange(500, 2000, 250)
    prompt = (
        f"{name} wants to open a regulated South African Unit Trust investing {_fmt_r(amt)} monthly. "
        f"Which group lists recognized South African financial institutions/asset managers from our curriculum?"
    )
    distractors = [
        "Pick n Pay Tuckshop, City Water Meter Board, and Local Hardware CC",
        "Department of Traffic Fines, Municipal Refuse Truck, and School Canteen",
        "Private Loan Shark Desk, Unregistered Cash Stokvel Box, and Grocery Till",
    ]
    sol = f"**{correct}** are established South African asset management / financial institutions offering unit trust investments."
    return _make_mcq(
        rng, "47_south_african_asset_managers_identification", "South African Investment Firms", prompt,
        correct, distractors, sol,
        "Look for genuine South African asset managers and life/investment houses.",
        "Recognize names such as Allan Gray, Coronation Fund Managers, Old Mutual, Investec, RMB, and Liberty Life.",
        ["ems_fails_to_recognize_sa_firms"],
    )


def build_48_simple_annual_investment_return_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    principal = rng.randrange(12000, 48000, 2000)
    rate = rng.choice([6, 8, 9, 10])
    interest = (principal * rate) // 100
    final_val = principal + interest
    prompt = (
        f"{sc['business_type']} invests {_fmt_r(principal)} of retained profit into a 1-year fixed deposit earning {rate}% simple interest per year. "
        f"Calculate the total final value of the investment (capital + interest) after 1 year (numbers only)."
    )
    sol = (
        f"Interest Earned = {rate}% × {_fmt_r(principal)} = {_fmt_r(interest)}\n"
        f"Total Final Value = {_fmt_r(principal)} + {_fmt_r(interest)} = **{_fmt_r(final_val)}**"
    )
    return _make_calc(
        rng, "48_simple_annual_investment_return_calc", "1-Year Investment Value Calculation", prompt,
        final_val, "Final Value = Principal + (Principal × Rate)", sol,
        "Note the question asks for the TOTAL final value (principal plus interest), not just the interest.",
        f"Interest = {interest}; add back {principal}.",
        ["ems_forgets_to_add_principal_on_investment"], marks=4,
    )


def build_49_compound_savings_two_year_growth_calc(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    principal = rng.choice([2000, 4000, 5000, 8000, 10000])
    yr1 = principal + (principal * 10) // 100
    yr2 = yr1 + (yr1 * 10) // 100
    prompt = (
        f"{name} invests {_fmt_r(principal)} for 2 years in an account earning 10% compound interest per annum (reinvesting year 1 interest). "
        f"Calculate the exact balance at the end of Year 2 (numbers only)."
    )
    sol = (
        f"End of Year 1 = {_fmt_r(principal)} × 1,10 = {_fmt_r(yr1)}\n"
        f"End of Year 2 = {_fmt_r(yr1)} × 1,10 = **{_fmt_r(yr2)}** (interest earned on Year 1 interest!)"
    )
    return _make_calc(
        rng, "49_compound_savings_two_year_growth_calc", "2-Year Compound Growth Calculation", prompt,
        yr2, "Year 2 Balance = Principal × 1,10 × 1,10", sol,
        "In Year 2, calculate 10% on the NEW Year 1 balance, not just the original deposit.",
        f"Yr 1 = {yr1}; 10% of {yr1} = {yr1 // 10}; Yr 2 = {yr2}.",
        ["ems_uses_simple_instead_of_compound_interest"], marks=4,
    )


def build_50_capstone_net_worth_and_profit_review_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sales = rng.randrange(40000, 75000, 5000)
    cos = rng.randrange(18000, 28000, 2000)
    opex = rng.randrange(6000, 11000, 1000)
    gp = sales - cos
    np = gp - opex
    p_assets = rng.randrange(320000, 620000, 20000)
    p_liab = rng.randrange(90000, 210000, 10000)
    p_nw = p_assets - p_liab
    headers = ["Financial Review Metric", "Scope", "Amount (R)"]
    rows = [
        [{"cell_id": "r0_c0", "value": f"Retail Sales = {_fmt_r(sales)}, Cost of Sales = {_fmt_r(cos)} -> Gross Profit", "editable": False, "prefilled": True},
         {"cell_id": "r0_c1", "value": "Business", "editable": False, "prefilled": True},
         {"cell_id": "r0_c2", "value": "", "editable": True, "expected": str(gp)}],
        [{"cell_id": "r1_c0", "value": f"Less Operating Expenses ({_fmt_r(opex)}) -> Net Profit", "editable": False, "prefilled": True},
         {"cell_id": "r1_c1", "value": "Business", "editable": False, "prefilled": True},
         {"cell_id": "r1_c2", "value": "", "editable": True, "expected": str(np)}],
        [{"cell_id": "r2_c0", "value": "Personal Assets (Home + Bank + Unit Trust)", "editable": False, "prefilled": True},
         {"cell_id": "r2_c1", "value": "Personal", "editable": False, "prefilled": True},
         {"cell_id": "r2_c2", "value": str(p_assets), "editable": False, "prefilled": True}],
        [{"cell_id": "r3_c0", "value": "Personal Liabilities (Bond + Store Card)", "editable": False, "prefilled": True},
         {"cell_id": "r3_c1", "value": "Personal", "editable": False, "prefilled": True},
         {"cell_id": "r3_c2", "value": str(p_liab), "editable": False, "prefilled": True}],
        [{"cell_id": "r4_c0", "value": "Personal Net Worth", "editable": False, "prefilled": True},
         {"cell_id": "r4_c1", "value": "Personal", "editable": False, "prefilled": True},
         {"cell_id": "r4_c2", "value": "", "editable": True, "expected": str(p_nw)}],
        [{"cell_id": "r5_c0", "value": "Personal Worth Position (Surplus or Deficit)", "editable": False, "prefilled": True},
         {"cell_id": "r5_c1", "value": "Status", "editable": False, "prefilled": True},
         {"cell_id": "r5_c2", "value": "", "editable": True, "expected": "Surplus"}],
    ]
    cmap = {"r0_c2": str(gp), "r1_c2": str(np), "r4_c2": str(p_nw), "r5_c2": "Surplus"}
    chints = {
        "r0_c2": f"Gross Profit = {sales} - {cos} (digits only).",
        "r1_c2": f"Net Profit = Gross Profit - {opex} (digits only).",
        "r4_c2": f"Net Worth = {p_assets} - {p_liab} (digits only).",
        "r5_c2": "Enter 'Surplus' since Personal Assets exceed Liabilities.",
    }
    md_memo = (
        f"| Financial Review Metric | Scope | Amount (R) |\n|---|---|---:|\n"
        f"| Gross Profit | Business | {gp} |\n| Net Profit | Business | {np} |\n"
        f"| Personal Assets | Personal | {p_assets} |\n| Personal Liabilities | Personal | {p_liab} |\n"
        f"| **Personal Net Worth** | Personal | **{p_nw}** |\n| Position | Status | **Surplus** |"
    )
    prompt = f"Complete {sc['entrepreneur']}'s capstone Business Profit and Personal Net Worth review schedule below ({sc['business_type']} vs household records; numbers without 'R')."
    return _make_ledger(
        rng, "50_capstone_net_worth_and_profit_review_table", "Capstone Profit & Net Worth Review",
        prompt, headers, rows, cmap, chints, md_memo,
        "Keep Business Profit calculations separate from Personal Net Worth.",
        f"GP = {gp}; NP = {np}; Personal Net Worth = {p_nw} (Surplus).",
        ["ems_capstone_income_networth_error"], marks=8,
    )


BUILDERS_26_50 = {
    "26_service_vs_retail_primary_business_income": build_26_service_vs_retail_primary_business_income,
    "27_business_income_sources_classification_table": build_27_business_income_sources_classification_table,
    "28_royalties_and_mineral_royalty_bill": build_28_royalties_and_mineral_royalty_bill,
    "29_shares_shareholders_and_dividends_concept": build_29_shares_shareholders_and_dividends_concept,
    "30_dividend_payout_income_calculation": build_30_dividend_payout_income_calculation,
    "31_business_startup_capital_vs_running_expenses": build_31_business_startup_capital_vs_running_expenses,
    "32_business_operational_and_statutory_expenses": build_32_business_operational_and_statutory_expenses,
    "33_industry_specific_expense_profile_analysis": build_33_industry_specific_expense_profile_analysis,
    "34_business_expense_categories_table": build_34_business_expense_categories_table,
    "35_gross_profit_formula_and_calculation": build_35_gross_profit_formula_and_calculation,
    "36_net_profit_after_operating_expenses_calc": build_36_net_profit_after_operating_expenses_calc,
    "37_profitability_waterfall_bar_visual": build_37_profitability_waterfall_bar_visual,
    "38_business_income_summary_statement_table": build_38_business_income_summary_statement_table,
    "39_break_even_revenue_deficit_reverse_calc": build_39_break_even_revenue_deficit_reverse_calc,
    "40_current_cheque_account_daily_transactions_role": build_40_current_cheque_account_daily_transactions_role,
    "41_separating_personal_vs_business_savings": build_41_separating_personal_vs_business_savings,
    "42_retaining_profits_in_business_savings_strategy": build_42_retaining_profits_in_business_savings_strategy,
    "43_investments_as_forced_tied_up_saving": build_43_investments_as_forced_tied_up_saving,
    "44_savings_account_vs_investment_return_risk": build_44_savings_account_vs_investment_return_risk,
    "45_unit_trust_collective_investment_pooling": build_45_unit_trust_collective_investment_pooling,
    "46_unit_trust_pooling_flow_diagram_visual": build_46_unit_trust_pooling_flow_diagram_visual,
    "47_south_african_asset_managers_identification": build_47_south_african_asset_managers_identification,
    "48_simple_annual_investment_return_calc": build_48_simple_annual_investment_return_calc,
    "49_compound_savings_two_year_growth_calc": build_49_compound_savings_two_year_growth_calc,
    "50_capstone_net_worth_and_profit_review_table": build_50_capstone_net_worth_and_profit_review_table,
}
