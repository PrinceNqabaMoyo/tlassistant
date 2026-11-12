"""Grade 7 Economic and Management Sciences - Term 2: Accounting Concepts (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/EMS_Gr7/Term 2/01. Accounting concepts.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import get_ems_scenario, NAMES


def _fmt_r(val: int | float) -> str:
    """Format Rand amounts cleanly with space thousands separator."""
    if isinstance(val, float) and not val.is_integer():
        whole, dec = f"{val:.2f}".split(".")
        whole_fmt = f"{int(whole):,}".replace(",", " ")
        return f"R{whole_fmt},{dec}"
    return f"R{int(val):,}".replace(",", " ")


def _make_mcq(
    rng: random.Random,
    subskill: str,
    title: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    sol: str,
    t1: str,
    t2: str,
    tags: List[str],
    marks: int = 2,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    opts = [correct] + distractors[:3]
    rng.shuffle(opts)
    idx = opts.index(correct)
    item: Dict[str, Any] = {
        "id": f"g7_ems_ac_{subskill[:2]}_{rng.randint(100000, 999999)}",
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "mcq",
        "modality": "math",
        "solution_type": "mcq",
        "prompt": prompt,
        "question": prompt,
        "options": opts,
        "correct_index": str(idx),
        "correct_answer": correct,
        "sample_answer": correct,
        "ideal_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "solution": sol,
        "marks": marks,
        "total_marks": marks,
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": max(2, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": f"Select: {correct}"},
        "marking_points": [correct],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [{"id": "mp_1", "desc": f"Correct selection: {correct}", "marks": marks, "editable": True}],
        },
        "misconception_tags": tags,
        "topic_id": "grade7_ems",
        "subtopic_id": "term2_accounting_concepts",
    }
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    return item


def _make_calc(
    rng: random.Random,
    subskill: str,
    title: str,
    prompt: str,
    val: int | float,
    formula: str,
    sol: str,
    t1: str,
    t2: str,
    tags: List[str],
    marks: int = 3,
    unit: str = "R",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    ans_str = f"{val:.2f}" if isinstance(val, float) and not val.is_integer() else str(int(val))
    disp_ans = _fmt_r(val) if unit == "R" else f"{ans_str}{(' ' + unit) if unit else ''}".strip()
    item: Dict[str, Any] = {
        "id": f"g7_ems_ac_{subskill[:2]}_{rng.randint(100000, 999999)}",
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "calc",
        "modality": "math",
        "solution_type": "calculation",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "correct_value": val,
        "unit": unit,
        "working_formula": formula,
        "sample_answer": disp_ans,
        "ideal_answer": disp_ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "solution": sol,
        "marks": marks,
        "total_marks": marks,
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": max(3, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": f"Final answer: {disp_ans}"},
        "marking_points": [formula, disp_ans],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct method/formula: {formula}", "marks": max(1, marks - 1), "editable": True},
                {"id": "mp_2", "desc": f"Accurate final value: {disp_ans}", "marks": 1, "editable": True},
            ],
        },
        "misconception_tags": tags,
        "topic_id": "grade7_ems",
        "subtopic_id": "term2_accounting_concepts",
    }
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    return item


def _make_typed(
    rng: random.Random,
    subskill: str,
    title: str,
    prompt: str,
    marking_points: List[str],
    key_concepts: List[str],
    sample_answer: str,
    t1: str,
    t2: str,
    tags: List[str],
    marks: int = 4,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    item: Dict[str, Any] = {
        "id": f"g7_ems_ac_{subskill[:2]}_{rng.randint(100000, 999999)}",
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "typed",
        "modality": "semantic",
        "solution_type": "marking_points",
        "prompt": prompt,
        "question": prompt,
        "marking_points": marking_points,
        "key_concepts": key_concepts,
        "sample_answer": sample_answer,
        "ideal_answer": sample_answer,
        "correct_answer": sample_answer,
        "worked_solution": sample_answer,
        "explanation": sample_answer,
        "canonical_solution": sample_answer,
        "solution": sample_answer,
        "marks": marks,
        "total_marks": marks,
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": max(3, marks + 1),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": sample_answer},
        "guidelines": [f"Cover {len(marking_points)} core marking points clearly."],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{i + 1}", "desc": mp, "marks": 1, "concepts": key_concepts[:3], "editable": True}
                for i, mp in enumerate(marking_points)
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": tags,
        "topic_id": "grade7_ems",
        "subtopic_id": "term2_accounting_concepts",
    }
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    return item


def _make_ledger(
    rng: random.Random,
    subskill: str,
    title: str,
    prompt: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, str],
    cell_hints: Dict[str, str],
    md_memo: str,
    t1: str,
    t2: str,
    tags: List[str],
    marks: int = 5,
) -> Dict[str, Any]:
    return {
        "id": f"g7_ems_ac_{subskill[:2]}_{rng.randint(100000, 999999)}",
        "title": title,
        "subskill": subskill,
        "question_family_id": subskill,
        "question_type": "journal",
        "modality": "ledger",
        "solution_type": "tabular_cells",
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "sample_answer": md_memo,
        "ideal_answer": md_memo,
        "expected_answer": md_memo,
        "worked_solution": md_memo,
        "explanation": md_memo,
        "canonical_solution": md_memo,
        "solution": md_memo,
        "marks": marks,
        "total_marks": marks,
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": max(4, marks + 2),
        "hints": {"tier_1": t1, "tier_2": t2, "tier_3": md_memo},
        "marking_points": [f"{k}: {v}" for k, v in correct_map.items()],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"cell_{k}", "desc": f"Cell {k} correctly completed as {v}", "marks": 1, "editable": True}
                for k, v in correct_map.items()
            ],
        },
        "misconception_tags": tags,
        "topic_id": "grade7_ems",
        "subtopic_id": "term2_accounting_concepts",
    }


def _svg_accounting_balance(rng: random.Random, assets: int, liabilities: int, equity: int, biz_name: str) -> Dict[str, Any]:
    """Parameterized SVG visual balance scale for Assets = Owner's Equity + Liabilities."""
    total_bar = max(1, assets)
    liab_w = max(35, int(190 * (liabilities / total_bar)))
    eq_w = max(35, 190 - liab_w)
    y_shift = rng.randint(-2, 2)
    svg = (
        f'<svg viewBox="0 0 460 205" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="460" height="205" fill="#ffffff" stroke="#e2e8f0" rx="8"/>'
        f'<text x="230" y="24" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">'
        f'{biz_name}: Accounting Balance</text>'
        f'<text x="125" y="{58 + y_shift}" font-size="11" font-weight="bold" fill="#1e40af" text-anchor="middle">'
        f'Total Assets: {_fmt_r(assets)}</text>'
        f'<rect x="30" y="{66 + y_shift}" width="190" height="36" rx="5" fill="#3b82f6" stroke="#1e3a8a" stroke-width="1.5"/>'
        f'<text x="125" y="{88 + y_shift}" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Assets = {_fmt_r(assets)}</text>'
        f'<text x="335" y="{58 + y_shift}" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">'
        f'Equity + Liabilities</text>'
        f'<rect x="240" y="{66 + y_shift}" width="{eq_w}" height="36" rx="4" fill="#10b981" stroke="#065f46" stroke-width="1.5"/>'
        f'<text x="{240 + eq_w // 2}" y="{88 + y_shift}" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Equity</text>'
        f'<rect x="{240 + eq_w}" y="{66 + y_shift}" width="{liab_w}" height="36" rx="4" fill="#f59e0b" stroke="#92400e" stroke-width="1.5"/>'
        f'<text x="{240 + eq_w + liab_w // 2}" y="{88 + y_shift}" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Liab.</text>'
        f'<polygon points="230,{118 + y_shift} 214,{148 + y_shift} 246,{148 + y_shift}" fill="#64748b"/>'
        f'<line x1="25" y1="{112 + y_shift}" x2="435" y2="{112 + y_shift}" stroke="#334155" stroke-width="3"/>'
        f'<text x="230" y="176" font-size="11" fill="#334155" text-anchor="middle">'
        f'Owner\'s Equity = {_fmt_r(equity)} | Liabilities = {_fmt_r(liabilities)}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_01_financial_literacy_scope_overview(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    startup = rng.choice([2500, 4000, 6500, 8500])
    prompt = (
        f"{sc['entrepreneur']} wants to open a {sc['business_type']} in {sc['area']} with {_fmt_r(startup)} "
        f"and learn how to track assets, liabilities, budgets, savings, and banking records.\n\n"
        f"Which branch of Economic and Management Sciences covers managing money, budgeting, banking, and recording financial transactions?"
    )
    correct = "Financial Literacy"
    return _make_mcq(
        rng, "01_financial_literacy_scope_overview", "Financial Literacy Scope", prompt, correct,
        ["Manufacturing Operations", "Human Resource Administration", "Physical Geography"],
        f"Managing capital, assets, liabilities, income, expenses, budgets, savings, banking, and financial records falls under **{correct}**.",
        "Which EMS strand focuses on money, accounts, budgets, and banking?",
        "It deals directly with financial decision-making and accounting terms.",
        ["confuses_financial_literacy_with_other_strands"], marks=2,
    )


def arch_02_capital_startup_contribution_definition(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(15, 60) * 500
    prompt = (
        f"{sc['entrepreneur']} transfers {_fmt_r(amt)} from personal savings into a new business bank account to launch a "
        f"{sc['business_type']} in {sc['area']}.\n\nIn accounting terminology, what is this start-up money contributed by the owner called?"
    )
    correct = "Capital"
    return _make_mcq(
        rng, "02_capital_startup_contribution_definition", "Identifying Start-Up Capital", prompt, correct,
        ["Current Liability", "Operating Expense", "Cash Float"],
        f"Money or assets contributed by the owner to start or expand a business is called **{correct}** ({_fmt_r(amt)}).",
        "What term describes the owner's financial contribution to start a business?",
        "It represents the owner's initial investment in the enterprise.",
        ["confuses_capital_with_income_or_loans"], marks=2,
    )


def arch_03_capital_calculation_cash_and_equipment(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cash_c = rng.randint(10, 35) * 1000
    equip_c = rng.randint(5, 20) * 1000
    stock_c = rng.randint(3, 12) * 1000
    total_cap = cash_c + equip_c + stock_c
    prompt = (
        f"To launch a {sc['business_type']} in {sc['area']}, {sc['entrepreneur']} contributes:\n"
        f"- Cash deposited into the business bank account: {_fmt_r(cash_c)}\n"
        f"- Equipment contributed from home: {_fmt_r(equip_c)}\n"
        f"- Initial stock bought with personal funds: {_fmt_r(stock_c)}\n\n"
        f"Calculate the owner's total **Capital** contribution."
    )
    sol = (
        f"**Step 1:** Capital includes all cash and non-cash possessions contributed by the owner.\n"
        f"**Step 2:** $\\text{{Capital}} = {_fmt_r(cash_c)} + {_fmt_r(equip_c)} + {_fmt_r(stock_c)} = {_fmt_r(total_cap)}$.\n"
        f"**Answer:** **{_fmt_r(total_cap)}**"
    )
    return _make_calc(
        rng, "03_capital_calculation_cash_and_equipment", "Calculating Total Owner Capital",
        prompt, total_cap, "Capital = Cash + Equipment + Initial Stock contributed by owner", sol,
        "Remember that Capital includes both cash and equipment brought into the business by the owner.",
        f"Add {_fmt_r(cash_c)} + {_fmt_r(equip_c)} + {_fmt_r(stock_c)}.",
        ["excludes_non_cash_capital_contributions"], marks=3,
    )


def arch_04_owners_equity_interest_concept(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    val = rng.randint(25, 90) * 1000
    prompt = (
        f"After one year of trading in {sc['area']}, {sc['entrepreneur']}'s net financial interest (share) in the {sc['business_type']} stands at {_fmt_r(val)}.\n\n"
        f"What accounting term refers to the interest or share that an owner holds in their business?"
    )
    correct = "Owner's Equity"
    return _make_mcq(
        rng, "04_owners_equity_interest_concept", "Defining Owner's Equity", prompt, correct,
        ["Long-Term Liability", "Trading Stock", "Credit Note"],
        f"The owner's financial interest or net share in the business ({_fmt_r(val)}) is called **{correct}**.",
        "Think about the share of the business owned outright by the entrepreneur.",
        "It increases with capital and profit, and decreases with drawings or losses.",
        ["confuses_owners_equity_with_liabilities"], marks=2,
    )


def arch_05_drawings_personal_use_identification(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(400, 2500)
    prompt = (
        f"{sc['entrepreneur']} owns a tuckshop selling {sc['item_sold']} in {sc['area']}. On Friday afternoon, {sc['entrepreneur']} takes "
        f"{_fmt_r(amt)} out of the business cash register to pay for personal family groceries.\n\n"
        f"Which accounting term correctly classifies the {_fmt_r(amt)} taken for personal use?"
    )
    correct = "Drawings"
    return _make_mcq(
        rng, "05_drawings_personal_use_identification", "Identifying Owner Drawings", prompt, correct,
        ["Cash Float", "Business Revenue", "Long-Term Liability"],
        f"Any cash or goods taken by the owner for personal use are recorded as **{correct}** ({_fmt_r(amt)}), which reduces Owner's Equity.",
        "Distinguish money left in the till for change from money taken home by the owner.",
        "When an owner withdraws business money for personal needs, it is called Drawings.",
        ["confuses_cash_float_with_drawings"], marks=2,
    )


def arch_06_cash_float_vs_drawings_distinction(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    float_amt = rng.choice([300, 450, 500, 600])
    draw_amt = rng.choice([750, 900, 1200, 1500])
    prompt = (
        f"At the start of the trading day in {sc['area']}, {sc['entrepreneur']} places {_fmt_r(float_amt)} in small notes and coins into the cash register. "
        f"Later that day, {sc['entrepreneur']} takes {_fmt_r(draw_amt)} from the till to buy personal shoes.\n\n"
        f"Distinguish clearly between **Cash Float** and **Drawings** using this scenario. (4 marks)"
    )
    pts = [
        f"Cash Float ({_fmt_r(float_amt)}) is cash kept in the till at the start of the day to give change to customers (a Current Asset).",
        f"Drawings ({_fmt_r(draw_amt)}) is money or stock taken by the owner for personal use.",
        "Cash Float remains inside the business for operations, whereas Drawings leaves the business and reduces Owner's Equity.",
        "Correct link to the scenario figures.",
    ]
    sample = (
        f"1. **Cash Float ({_fmt_r(float_amt)}):** Small change placed in the cash register at opening so cashiers can give change to customers; it is a Current Asset.\n"
        f"2. **Drawings ({_fmt_r(draw_amt)}):** Cash or goods withdrawn by the owner for personal family use; it reduces the owner's equity in the business."
    )
    return _make_typed(
        rng, "06_cash_float_vs_drawings_distinction", "Cash Float vs Drawings", prompt,
        pts, ["Cash Float", "change for customers", "Drawings", "personal use", "Owner's Equity"],
        sample,
        "Consider what stays in the till for customers versus what goes home with the owner.",
        "One is an operating till asset for giving change; the other reduces the owner's investment.",
        ["confuses_cash_float_with_drawings"], marks=4,
    )


def arch_07_drawings_impact_on_owners_equity_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cap = rng.randint(30, 80) * 1000
    profit = rng.randint(8, 25) * 1000
    drawings = rng.randint(3, 7) * 1000
    closing_eq = cap + profit - drawings
    prompt = (
        f"{sc['entrepreneur']} started a {sc['business_type']} in {sc['area']} with Capital of {_fmt_r(cap)}. "
        f"During the year, the business earned a Net Profit of {_fmt_r(profit)}, and {sc['entrepreneur']} took {_fmt_r(drawings)} in Drawings.\n\n"
        f"Calculate the closing **Owner's Equity** at the end of the year."
    )
    sol = (
        f"**Step 1:** $\\text{{Closing Owner's Equity}} = \\text{{Capital}} + \\text{{Net Profit}} - \\text{{Drawings}}$\n"
        f"**Step 2:** $= {_fmt_r(cap)} + {_fmt_r(profit)} - {_fmt_r(drawings)} = {_fmt_r(closing_eq)}$\n"
        f"**Answer:** **{_fmt_r(closing_eq)}**"
    )
    return _make_calc(
        rng, "07_drawings_impact_on_owners_equity_calc", "Calculating Closing Owner's Equity",
        prompt, closing_eq, "Closing Owner's Equity = Capital + Net Profit - Drawings", sol,
        "Profit increases the owner's share, while Drawings decreases it.",
        f"Add {_fmt_r(cap)} + {_fmt_r(profit)}, then subtract {_fmt_r(drawings)}.",
        ["adds_drawings_to_equity"], marks=3,
    )


def arch_08_assets_definition_business_possessions(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    val = rng.randint(18, 50) * 1000
    prompt = (
        f"{sc['entrepreneur']}'s {sc['business_type']} in {sc['area']} owns delivery equipment and cash totalling {_fmt_r(val)}.\n\n"
        f"In accounting, what are valuable goods and possessions owned by a business called?"
    )
    correct = "Assets"
    return _make_mcq(
        rng, "08_assets_definition_business_possessions", "Defining Business Assets", prompt, correct,
        ["Liabilities", "Expenses", "Losses"],
        f"Goods, cash, property, and possessions owned by a business ({_fmt_r(val)}) are called **{correct}**.",
        "Assets represent what a business owns; liabilities represent what it owes.",
        "Think of possessions of financial value owned outright or controlled by the enterprise.",
        ["confuses_assets_with_expenses"], marks=2,
    )


def arch_09_fixed_assets_long_term_identification(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    veh = rng.randint(90, 220) * 1000
    prompt = (
        f"{sc['entrepreneur']} buys a delivery bakkie for {_fmt_r(veh)} and shelving units to use in the shop in {sc['area']} for several years without intending to resell them.\n\n"
        f"Which category best classifies the delivery bakkie and shelving equipment?"
    )
    correct = "Fixed Assets"
    return _make_mcq(
        rng, "09_fixed_assets_long_term_identification", "Identifying Fixed Assets", prompt, correct,
        ["Current Assets", "Current Liabilities", "Operating Expenses"],
        f"Vehicles, land, buildings, and equipment kept for long-term business use ({_fmt_r(veh)}) are **{correct}**.",
        "Are vehicles and buildings kept for years or sold every week?",
        "Long-lasting possessions not bought for resale are Fixed Assets.",
        ["confuses_fixed_with_current_assets"], marks=2,
    )


def arch_10_current_assets_short_term_liquidity(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(4, 18) * 500
    prompt = (
        f"{sc['entrepreneur']} holds {_fmt_r(amt)} in the business bank account plus trading stock of {sc['item_sold']} that turns into cash quickly during daily sales in {sc['area']}.\n\n"
        f"Which term describes temporary assets that can be converted into cash easily within a short period?"
    )
    correct = "Current Assets"
    return _make_mcq(
        rng, "10_current_assets_short_term_liquidity", "Defining Current Assets", prompt, correct,
        ["Fixed Assets", "Long-Term Liabilities", "Capital Expenditure"],
        f"Temporary possessions easily converted into cash within a year (bank cash, cash float, trading stock of {_fmt_r(amt)}) are **{correct}**.",
        "Look for the asset category that moves and converts into cash rapidly.",
        "Unlike land or vehicles, cash and trading stock constantly circulate in the short term.",
        ["confuses_current_with_fixed_assets"], marks=2,
    )


def arch_11_fixed_vs_current_assets_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    v_veh = rng.randint(60, 140) * 1000
    v_eq = rng.randint(15, 35) * 1000
    v_stock = rng.randint(8, 22) * 1000
    v_bank = rng.randint(5, 18) * 1000
    v_float = rng.choice([400, 500, 800, 1000])
    tot_fixed = v_veh + v_eq
    tot_curr = v_stock + v_bank + v_float
    prompt = (
        f"{sc['entrepreneur']} owns the following business possessions for a {sc['business_type']} in {sc['area']}:\n"
        f"- Delivery Vehicle: {_fmt_r(v_veh)}\n"
        f"- Shop Equipment: {_fmt_r(v_eq)}\n"
        f"- Trading Stock ({sc['item_sold']}): {_fmt_r(v_stock)}\n"
        f"- Bank Balance: {_fmt_r(v_bank)}\n"
        f"- Cash Float: {_fmt_r(v_float)}\n\n"
        f"Complete the interactive schedule below by classifying each item as **Fixed Asset** or **Current Asset** and calculating **Total Fixed Assets** and **Total Current Assets**."
    )
    headers = ["Business Possession", "Amount (R)", "Asset Classification"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Delivery Vehicle", "editable": False}, {"cell_id": "r0_c1", "value": str(v_veh), "editable": False}, {"cell_id": "r0_c2", "value": "", "expected": "Fixed Asset", "editable": True}],
        [{"cell_id": "r1_c0", "value": "Shop Equipment", "editable": False}, {"cell_id": "r1_c1", "value": str(v_eq), "editable": False}, {"cell_id": "r1_c2", "value": "", "expected": "Fixed Asset", "editable": True}],
        [{"cell_id": "r2_c0", "value": f"Trading Stock ({sc['item_sold']})", "editable": False}, {"cell_id": "r2_c1", "value": str(v_stock), "editable": False}, {"cell_id": "r2_c2", "value": "", "expected": "Current Asset", "editable": True}],
        [{"cell_id": "r3_c0", "value": "Bank Balance", "editable": False}, {"cell_id": "r3_c1", "value": str(v_bank), "editable": False}, {"cell_id": "r3_c2", "value": "", "expected": "Current Asset", "editable": True}],
        [{"cell_id": "r4_c0", "value": "Cash Float", "editable": False}, {"cell_id": "r4_c1", "value": str(v_float), "editable": False}, {"cell_id": "r4_c2", "value": "", "expected": "Current Asset", "editable": True}],
        [{"cell_id": "r5_c0", "value": "Total Fixed Assets", "editable": False}, {"cell_id": "r5_c1", "value": "", "expected": str(tot_fixed), "editable": True}, {"cell_id": "r5_c2", "value": "Fixed Asset", "editable": False}],
        [{"cell_id": "r6_c0", "value": "Total Current Assets", "editable": False}, {"cell_id": "r6_c1", "value": "", "expected": str(tot_curr), "editable": True}, {"cell_id": "r6_c2", "value": "Current Asset", "editable": False}],
    ]
    cmap = {
        "r0_c2": "Fixed Asset",
        "r1_c2": "Fixed Asset",
        "r2_c2": "Current Asset",
        "r3_c2": "Current Asset",
        "r4_c2": "Current Asset",
        "r5_c1": str(tot_fixed),
        "r6_c1": str(tot_curr),
    }
    chints = {
        "r0_c2": "Vehicles are used long-term -> Fixed Asset.",
        "r1_c2": "Equipment lasts for several years -> Fixed Asset.",
        "r2_c2": "Trading stock is sold rapidly for cash -> Current Asset.",
        "r3_c2": "Bank cash is immediately liquid -> Current Asset.",
        "r4_c2": "Cash float is cash in the till -> Current Asset.",
        "r5_c1": f"Add Delivery Vehicle ({v_veh}) + Shop Equipment ({v_eq}).",
        "r6_c1": f"Add Trading Stock ({v_stock}) + Bank ({v_bank}) + Cash Float ({v_float}).",
    }
    memo = (
        f"| Business Possession | Amount (R) | Asset Classification |\n"
        f"| :--- | :---: | :--- |\n"
        f"| Delivery Vehicle | {v_veh} | Fixed Asset |\n"
        f"| Shop Equipment | {v_eq} | Fixed Asset |\n"
        f"| Trading Stock | {v_stock} | Current Asset |\n"
        f"| Bank Balance | {v_bank} | Current Asset |\n"
        f"| Cash Float | {v_float} | Current Asset |\n"
        f"| **Total Fixed Assets** | **{tot_fixed}** | **Fixed Asset** |\n"
        f"| **Total Current Assets** | **{tot_curr}** | **Current Asset** |\n\n"
        f"- Total Fixed Assets = {_fmt_r(v_veh)} + {_fmt_r(v_eq)} = **{_fmt_r(tot_fixed)}**\n"
        f"- Total Current Assets = {_fmt_r(v_stock)} + {_fmt_r(v_bank)} + {_fmt_r(v_float)} = **{_fmt_r(tot_curr)}**"
    )
    return _make_ledger(
        rng, "11_fixed_vs_current_assets_classification_table", "Fixed vs Current Assets Schedule",
        prompt, headers, rows, cmap, chints, memo,
        "Separate long-term items (Fixed Assets) from short-term liquid items (Current Assets).",
        "Sum Vehicle + Equipment for Fixed Assets, and Stock + Bank + Cash Float for Current Assets.",
        ["misclassifies_trading_stock_as_fixed_asset"], marks=7,
    )


def arch_12_trading_stock_purpose_for_profit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cost = rng.randint(800, 3500)
    prompt = (
        f"{sc['entrepreneur']} buys {_fmt_r(cost)} worth of {sc['item_sold']} from {sc['supplier']} in {sc['area']} "
        f"solely to resell them to customers at a higher price.\n\n"
        f"What accounting term identifies goods bought specifically to resell for a profit?"
    )
    correct = "Trading stock"
    return _make_mcq(
        rng, "12_trading_stock_purpose_for_profit", "Defining Trading Stock", prompt, correct,
        ["Fixed Equipment", "Owner's Drawings", "Long-Term Liability"],
        f"Items purchased with the primary purpose of selling them to customers at a profit ({_fmt_r(cost)} of {sc['item_sold']}) are called **{correct}** (a Current Asset).",
        "Look for the term describing merchandise meant for resale, not office furniture.",
        "Shops buy trading stock to sell it at a markup.",
        ["confuses_trading_stock_with_equipment"], marks=2,
    )


def arch_13_cash_float_calculation_register_notes(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    n50 = rng.randint(2, 6)
    n20 = rng.randint(4, 10)
    n10 = rng.randint(5, 12)
    c5 = rng.randint(4, 10)
    total_float = n50 * 50 + n20 * 20 + n10 * 10 + c5 * 5
    prompt = (
        f"Before opening the {sc['business_type']} in {sc['area']}, {sc['entrepreneur']} prepares the till's Cash Float consisting of:\n"
        f"- {n50} × R50 notes\n"
        f"- {n20} × R20 notes\n"
        f"- {n10} × R10 notes\n"
        f"- {c5} × R5 coins\n\n"
        f"Calculate the total value of the **Cash Float** in the register."
    )
    sol = (
        f"**Step 1:** Multiply each denomination by its quantity:\n"
        f"- R50 notes: {n50} × 50 = {_fmt_r(n50 * 50)}\n"
        f"- R20 notes: {n20} × 20 = {_fmt_r(n20 * 20)}\n"
        f"- R10 notes: {n10} × 10 = {_fmt_r(n10 * 10)}\n"
        f"- R5 coins: {c5} × 5 = {_fmt_r(c5 * 5)}\n"
        f"**Step 2:** Sum = **{_fmt_r(total_float)}**"
    )
    return _make_calc(
        rng, "13_cash_float_calculation_register_notes", "Calculating Till Cash Float",
        prompt, total_float, f"({n50}×50) + ({n20}×20) + ({n10}×10) + ({c5}×5)", sol,
        "Multiply each Rand note or coin value by how many you have, then add them up.",
        f"{n50*50} + {n20*20} + {n10*10} + {c5*5}.",
        ["arithmetic_error_counting_cash_float"], marks=3,
    )


def arch_14_liabilities_definition_external_debts(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    debt = rng.randint(5, 25) * 1000
    prompt = (
        f"To expand the {sc['business_type']} in {sc['area']}, {sc['entrepreneur']} buys supplies on credit from {sc['supplier']} and owes {_fmt_r(debt)} to be repaid next month.\n\n"
        f"In accounting, what is money owed by the business to another party called?"
    )
    correct = "Liability"
    return _make_mcq(
        rng, "14_liabilities_definition_external_debts", "Defining Business Liabilities", prompt, correct,
        ["Capital", "Current Asset", "Income"],
        f"Money or obligations owed by the business to external parties ({_fmt_r(debt)} owed to {sc['supplier']}) is a **{correct}**.",
        "Assets are what we own; what do we call debts we owe?",
        "Any external debt that must be repaid is a liability.",
        ["confuses_liabilities_with_expenses"], marks=2,
    )


def arch_15_long_term_liabilities_multi_year_loans(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    years = rng.choice([3, 5, 10, 15])
    loan = rng.randint(40, 180) * 1000
    prompt = (
        f"{sc['entrepreneur']} secures a {_fmt_r(loan)} business loan from a commercial bank in {sc['area']} to be repaid over **{years} years**.\n\n"
        f"How is a loan repayable over more than one year classified?"
    )
    correct = "Long-term Liability"
    return _make_mcq(
        rng, "15_long_term_liabilities_multi_year_loans", "Identifying Long-Term Liabilities", prompt, correct,
        ["Current Liability", "Current Asset", "Owner's Drawings"],
        f"Loans repayable over a period exceeding one year ({years} years for {_fmt_r(loan)}) are **Long-term Liabilities**.",
        "Check the repayment period: is it under 12 months or over several years?",
        "Debts extending beyond one year are Long-term Liabilities.",
        ["confuses_long_term_and_current_liabilities"], marks=2,
    )


def arch_16_current_liabilities_within_one_year(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    amt = rng.randint(1500, 9500)
    days = rng.choice([30, 60, 90])
    prompt = (
        f"{sc['entrepreneur']} buys {sc['item_sold']} on a {days}-day credit account from {sc['supplier']} for {_fmt_r(amt)}, due to be settled within the current year.\n\n"
        f"Which accounting classification describes debts payable within 12 months?"
    )
    correct = "Current Liability"
    return _make_mcq(
        rng, "16_current_liabilities_within_one_year", "Identifying Current Liabilities", prompt, correct,
        ["Long-term Liability", "Fixed Asset", "Capital Reserve"],
        f"Short-term debts due within one year (such as a {days}-day supplier account or bank overdraft of {_fmt_r(amt)}) are **Current Liabilities**.",
        "Notice the repayment term is under 12 months.",
        "Short-term obligations payable within a year are Current Liabilities.",
        ["confuses_current_and_long_term_liabilities"], marks=2,
    )


def arch_17_long_term_vs_current_liabilities_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    bond = rng.randint(120, 280) * 1000
    veh_loan = rng.randint(45, 95) * 1000
    cred = rng.randint(4, 15) * 1000
    overdraft = rng.randint(2, 9) * 1000
    tot_lt = bond + veh_loan
    tot_cur = cred + overdraft
    prompt = (
        f"{sc['entrepreneur']} reviews the debts of a {sc['business_type']} in {sc['area']}:\n"
        f"- Mortgage Bond (10-year repayment): {_fmt_r(bond)}\n"
        f"- 5-Year Vehicle Finance Loan: {_fmt_r(veh_loan)}\n"
        f"- Trade Creditor ({sc['supplier']}, 30 days): {_fmt_r(cred)}\n"
        f"- Bank Overdraft (short-term): {_fmt_r(overdraft)}\n\n"
        f"Complete the schedule below by classifying each item as **Long-term Liability** or **Current Liability** and computing the two sub-totals."
    )
    headers = ["Liability Item", "Amount (R)", "Liability Category"]
    rows = [
        [{"cell_id": "r0_c0", "value": "Mortgage Bond (10-year)", "editable": False}, {"cell_id": "r0_c1", "value": str(bond), "editable": False}, {"cell_id": "r0_c2", "value": "", "expected": "Long-term Liability", "editable": True}],
        [{"cell_id": "r1_c0", "value": "Vehicle Finance Loan (5-year)", "editable": False}, {"cell_id": "r1_c1", "value": str(veh_loan), "editable": False}, {"cell_id": "r1_c2", "value": "", "expected": "Long-term Liability", "editable": True}],
        [{"cell_id": "r2_c0", "value": f"Creditor: {sc['supplier']} (30 days)", "editable": False}, {"cell_id": "r2_c1", "value": str(cred), "editable": False}, {"cell_id": "r2_c2", "value": "", "expected": "Current Liability", "editable": True}],
        [{"cell_id": "r3_c0", "value": "Bank Overdraft (short-term)", "editable": False}, {"cell_id": "r3_c1", "value": str(overdraft), "editable": False}, {"cell_id": "r3_c2", "value": "", "expected": "Current Liability", "editable": True}],
        [{"cell_id": "r4_c0", "value": "Total Long-term Liabilities", "editable": False}, {"cell_id": "r4_c1", "value": "", "expected": str(tot_lt), "editable": True}, {"cell_id": "r4_c2", "value": "Long-term Liability", "editable": False}],
        [{"cell_id": "r5_c0", "value": "Total Current Liabilities", "editable": False}, {"cell_id": "r5_c1", "value": "", "expected": str(tot_cur), "editable": True}, {"cell_id": "r5_c2", "value": "Current Liability", "editable": False}],
    ]
    cmap = {
        "r0_c2": "Long-term Liability",
        "r1_c2": "Long-term Liability",
        "r2_c2": "Current Liability",
        "r3_c2": "Current Liability",
        "r4_c1": str(tot_lt),
        "r5_c1": str(tot_cur),
    }
    chints = {
        "r0_c2": "10 years > 1 year -> Long-term Liability.",
        "r1_c2": "5 years > 1 year -> Long-term Liability.",
        "r2_c2": "30 days <= 1 year -> Current Liability.",
        "r3_c2": "Bank overdraft is short-term -> Current Liability.",
        "r4_c1": f"Add {bond} + {veh_loan}.",
        "r5_c1": f"Add {cred} + {overdraft}.",
    }
    memo = (
        f"| Liability Item | Amount (R) | Category |\n| :--- | :---: | :--- |\n"
        f"| Mortgage Bond | {bond} | Long-term Liability |\n"
        f"| Vehicle Finance | {veh_loan} | Long-term Liability |\n"
        f"| Creditor ({sc['supplier']}) | {cred} | Current Liability |\n"
        f"| Bank Overdraft | {overdraft} | Current Liability |\n"
        f"| **Total Long-term Liabilities** | **{tot_lt}** | Long-term Liability |\n"
        f"| **Total Current Liabilities** | **{tot_cur}** | Current Liability |"
    )
    return _make_ledger(
        rng, "17_long_term_vs_current_liabilities_table", "Long-Term vs Current Liabilities Schedule",
        prompt, headers, rows, cmap, chints, memo,
        "Debts > 12 months are Long-term Liabilities; debts <= 12 months are Current Liabilities.",
        f"Long-term = {bond} + {veh_loan}; Current = {cred} + {overdraft}.",
        ["confuses_overdraft_with_long_term_liability"], marks=6,
    )


def arch_18_accounting_equation_balance_visual(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    liab = rng.randint(15, 45) * 1000
    eq = rng.randint(25, 75) * 1000
    assets = liab + eq
    dspec = _svg_accounting_balance(rng, assets, liab, eq, sc["business_type"])
    prompt = (
        f"Study the accounting balance diagram for {sc['entrepreneur']}'s {sc['business_type']} in {sc['area']}.\n\n"
        f"If Total Assets equal {_fmt_r(assets)} and Total Liabilities equal {_fmt_r(liab)}, calculate the **Owner's Equity** required to balance the accounting equation."
    )
    sol = (
        f"**Step 1:** Accounting Equation: $\\text{{Assets}} = \\text{{Owner's Equity}} + \\text{{Liabilities}}$\n"
        f"**Step 2:** $\\text{{Owner's Equity}} = {_fmt_r(assets)} - {_fmt_r(liab)} = {_fmt_r(eq)}$\n"
        f"**Answer:** **{_fmt_r(eq)}**"
    )
    return _make_calc(
        rng, "18_accounting_equation_balance_visual", "Accounting Equation Balance Scale",
        prompt, eq, "Owner's Equity = Assets - Liabilities", sol,
        "On a balanced scale, Assets on the left equal Equity plus Liabilities on the right.",
        f"Subtract Liabilities ({_fmt_r(liab)}) from Assets ({_fmt_r(assets)}).",
        ["adds_liabilities_to_assets_for_equity"], marks=3, diagram_spec=dspec,
    )


def arch_19_income_increases_equity_definition(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    rev = rng.randint(4, 15) * 1000
    prompt = (
        f"{sc['entrepreneur']} earns {_fmt_r(rev)} from selling {sc['item_sold']} to customers in {sc['area']}.\n\n"
        f"What accounting term defines money received or earned by a business that increases Owner's Equity?"
    )
    correct = "Income"
    return _make_mcq(
        rng, "19_income_increases_equity_definition", "Defining Business Income", prompt, correct,
        ["Liabilities", "Expenses", "Drawings"],
        f"Receipts or earnings from selling goods or rendering services ({_fmt_r(rev)}) that increase Owner's Equity are called **{correct}**.",
        "Which financial element flows into the business from sales or services and grows equity?",
        "Receipts that increase owner's equity are Income.",
        ["confuses_income_with_capital"], marks=2,
    )


def arch_20_expenses_operational_costs_definition(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    wage = rng.randint(2500, 6500)
    prompt = (
        f"At month-end in {sc['area']}, {sc['entrepreneur']} pays {_fmt_r(wage)} for assistant wages and electricity used to run the shop.\n\n"
        f"What accounting classification describes money spent on day-to-day running costs like wages and electricity?"
    )
    correct = "Expenses"
    return _make_mcq(
        rng, "20_expenses_operational_costs_definition", "Defining Business Expenses", prompt, correct,
        ["Fixed Assets", "Income", "Capital"],
        f"Costs incurred to operate the business such as wages and electricity ({_fmt_r(wage)}) are **Expenses**, which reduce Owner's Equity.",
        "Does paying monthly wages buy an asset or pay an operational running cost?",
        "Day-to-day running costs that decrease equity are Expenses.",
        ["confuses_expenses_with_assets"], marks=2,
    )


def arch_21_income_vs_expense_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sales = rng.randint(22, 48) * 1000
    rent_rec = rng.randint(3, 7) * 1000
    wages = rng.randint(7, 14) * 1000
    elec = rng.randint(2, 5) * 1000
    tot_inc = sales + rent_rec
    tot_exp = wages + elec
    profit = tot_inc - tot_exp
    prompt = (
        f"{sc['entrepreneur']} recorded four monthly items for the {sc['business_type']} in {sc['area']}:\n"
        f"- Cash Sales ({sc['item_sold']}): {_fmt_r(sales)}\n"
        f"- Sub-letting storage room (Rent Income): {_fmt_r(rent_rec)}\n"
        f"- Staff Wages paid: {_fmt_r(wages)}\n"
        f"- Electricity & Water bill: {_fmt_r(elec)}\n\n"
        f"Complete the schedule by classifying each item (**Income** or **Expense**) and computing **Total Income**, **Total Expenses**, and **Profit**."
    )
    headers = ["Item Description", "Amount (R)", "Classification"]
    rows = [
        [{"cell_id": "r0_c0", "value": f"Cash Sales ({sc['item_sold']})", "editable": False}, {"cell_id": "r0_c1", "value": str(sales), "editable": False}, {"cell_id": "r0_c2", "value": "", "expected": "Income", "editable": True}],
        [{"cell_id": "r1_c0", "value": "Rent Income Received", "editable": False}, {"cell_id": "r1_c1", "value": str(rent_rec), "editable": False}, {"cell_id": "r1_c2", "value": "", "expected": "Income", "editable": True}],
        [{"cell_id": "r2_c0", "value": "Staff Wages Paid", "editable": False}, {"cell_id": "r2_c1", "value": str(wages), "editable": False}, {"cell_id": "r2_c2", "value": "", "expected": "Expense", "editable": True}],
        [{"cell_id": "r3_c0", "value": "Electricity & Water", "editable": False}, {"cell_id": "r3_c1", "value": str(elec), "editable": False}, {"cell_id": "r3_c2", "value": "", "expected": "Expense", "editable": True}],
        [{"cell_id": "r4_c0", "value": "Total Income", "editable": False}, {"cell_id": "r4_c1", "value": "", "expected": str(tot_inc), "editable": True}, {"cell_id": "r4_c2", "value": "Income", "editable": False}],
        [{"cell_id": "r5_c0", "value": "Total Expenses", "editable": False}, {"cell_id": "r5_c1", "value": "", "expected": str(tot_exp), "editable": True}, {"cell_id": "r5_c2", "value": "Expense", "editable": False}],
        [{"cell_id": "r6_c0", "value": "Net Profit", "editable": False}, {"cell_id": "r6_c1", "value": "", "expected": str(profit), "editable": True}, {"cell_id": "r6_c2", "value": "Profit", "editable": False}],
    ]
    cmap = {
        "r0_c2": "Income", "r1_c2": "Income", "r2_c2": "Expense", "r3_c2": "Expense",
        "r4_c1": str(tot_inc), "r5_c1": str(tot_exp), "r6_c1": str(profit),
    }
    chints = {
        "r0_c2": "Money earned from selling goods -> Income.",
        "r1_c2": "Money earned from sub-letting space -> Income.",
        "r2_c2": "Money paid to employees -> Expense.",
        "r3_c2": "Utility running cost -> Expense.",
        "r4_c1": f"Add Sales ({sales}) + Rent Income ({rent_rec}).",
        "r5_c1": f"Add Wages ({wages}) + Electricity ({elec}).",
        "r6_c1": f"Subtract Total Expenses ({tot_exp}) from Total Income ({tot_inc}).",
    }
    memo = (
        f"| Item Description | Amount (R) | Classification |\n| :--- | :---: | :--- |\n"
        f"| Cash Sales | {sales} | Income |\n"
        f"| Rent Income | {rent_rec} | Income |\n"
        f"| Staff Wages | {wages} | Expense |\n"
        f"| Electricity & Water | {elec} | Expense |\n"
        f"| **Total Income** | **{tot_inc}** | Income |\n"
        f"| **Total Expenses** | **{tot_exp}** | Expense |\n"
        f"| **Net Profit** | **{profit}** | Profit |"
    )
    return _make_ledger(
        rng, "21_income_vs_expense_classification_table", "Income vs Expenses Schedule",
        prompt, headers, rows, cmap, chints, memo,
        "Group money coming in as Income and operating costs as Expenses.",
        f"Profit = Total Income ({tot_inc}) - Total Expenses ({tot_exp}).",
        ["confuses_rent_received_with_rent_paid"], marks=7,
    )


def arch_22_profit_motive_commercial_purpose(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"{sc['entrepreneur']} risks personal savings in {sc['area']} to start a {sc['business_type']} with the primary goal "
        f"of earning more revenue than costs.\n\n"
        f"What economic term describes the incentive that drives entrepreneurs to start businesses in order to earn a surplus?"
    )
    correct = "Profit motive"
    return _make_mcq(
        rng, "22_profit_motive_commercial_purpose", "Understanding the Profit Motive", prompt, correct,
        ["Net Loss", "Cash Float", "Liability Ratio"],
        "The **Profit motive** is the drive to earn financial gain (Income > Expenses), rewarding entrepreneurs for risking capital.",
        "Why do private business owners invest savings and take financial risks?",
        "They are motivated by earning a profit.",
        ["confuses_profit_motive_with_revenue"], marks=2,
    )


def arch_23_profit_calculation_income_minus_expenses(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    inc = rng.randint(18, 45) * 1000
    wages = rng.randint(4, 9) * 1000
    rent = rng.randint(3, 6) * 1000
    utils = rng.randint(1, 3) * 1000
    profit = inc - (wages + rent + utils)
    prompt = (
        f"During April in {sc['area']}, {sc['entrepreneur']}'s {sc['business_type']} earned total income of {_fmt_r(inc)}. "
        f"Expenses were: Wages {_fmt_r(wages)}, Rent {_fmt_r(rent)}, and Utilities {_fmt_r(utils)}.\n\n"
        f"Calculate the business's **Net Profit**."
    )
    sol = (
        f"**Step 1:** Total Expenses = ${_fmt_r(wages)} + {_fmt_r(rent)} + {_fmt_r(utils)} = {_fmt_r(wages + rent + utils)}$\n"
        f"**Step 2:** Net Profit = ${_fmt_r(inc)} - {_fmt_r(wages + rent + utils)} = {_fmt_r(profit)}$\n"
        f"**Answer:** **{_fmt_r(profit)}**"
    )
    return _make_calc(
        rng, "23_profit_calculation_income_minus_expenses", "Calculating Business Net Profit",
        prompt, profit, "Net Profit = Total Income - Total Expenses", sol,
        "First sum all three business expenses, then subtract that total from total income.",
        f"{_fmt_r(inc)} - ({_fmt_r(wages)} + {_fmt_r(rent)} + {_fmt_r(utils)}).",
        ["forgets_one_expense_item"], marks=3,
    )


def arch_24_net_loss_exceeding_expenses_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    receipts = rng.randint(10, 22) * 1000
    extra = rng.randint(2, 6) * 1000
    expenses = receipts + extra
    loss_amt = extra
    prompt = (
        f"In a slow winter month in {sc['area']}, {sc['entrepreneur']}'s service kiosk earned {_fmt_r(receipts)} for services rendered, "
        f"while total monthly operating expenses reached {_fmt_r(expenses)}.\n\n"
        f"Because expenses exceeded receipts, calculate the Rand magnitude of the **Net Loss** (enter a positive Rand amount)."
    )
    sol = (
        f"**Step 1:** A **Net Loss** occurs when $\\text{{Expenses}} > \\text{{Income}}$.\n"
        f"**Step 2:** $\\text{{Net Loss}} = {_fmt_r(expenses)} - {_fmt_r(receipts)} = {_fmt_r(loss_amt)}$.\n"
        f"**Answer:** **{_fmt_r(loss_amt)}**"
    )
    return _make_calc(
        rng, "24_net_loss_exceeding_expenses_calculation", "Calculating Net Loss",
        prompt, loss_amt, "Net Loss = Total Expenses - Total Income (when Expenses > Income)", sol,
        "Find by how much total expenses exceeded the receipts earned.",
        f"Subtract {_fmt_r(receipts)} from {_fmt_r(expenses)}.",
        ["confuses_net_loss_with_profit"], marks=2,
    )


def arch_25_trade_goods_vs_rendering_service_distinction(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("a spaza shop buying and reselling groceries", "a hair salon braiding and styling hair"),
        ("a clothing boutique selling jackets", "a plumber repairing leaking municipal pipes"),
        ("a stationery shop selling school exercise books", "a tutor offering after-school mathematics lessons"),
    ])
    trading_ex, service_ex = pair
    prompt = (
        f"In South Africa, consider two local businesses: (1) {trading_ex}, and (2) {service_ex}.\n\n"
        f"Which statement accurately distinguishes **trade** from **rendering a service**?"
    )
    correct = f"Trade involves buying and selling physical goods for a profit ({trading_ex}), whereas rendering a service provides skilled work or assistance for a fee ({service_ex})."
    return _make_mcq(
        rng, "25_trade_goods_vs_rendering_service_distinction", "Trade vs Rendering a Service", prompt, correct,
        [
            "Trade and rendering a service mean the exact same thing in accounting.",
            "Rendering a service means buying factory machines without charging customers.",
            "Trade only happens when banks lend money to schools without selling any goods.",
        ],
        f"**Trade** deals with tangible merchandise (trading stock), while **rendering a service** earns current income by performing work for clients.",
        "Ask which business sells physical stock and which sells skill or time.",
        "Trading buys/sells goods; service businesses perform tasks for fees.",
        ["thinks_trade_means_service_only"], marks=2,
    )


BUILDERS_01_25 = {
    "01_financial_literacy_scope_overview": arch_01_financial_literacy_scope_overview,
    "02_capital_startup_contribution_definition": arch_02_capital_startup_contribution_definition,
    "03_capital_calculation_cash_and_equipment": arch_03_capital_calculation_cash_and_equipment,
    "04_owners_equity_interest_concept": arch_04_owners_equity_interest_concept,
    "05_drawings_personal_use_identification": arch_05_drawings_personal_use_identification,
    "06_cash_float_vs_drawings_distinction": arch_06_cash_float_vs_drawings_distinction,
    "07_drawings_impact_on_owners_equity_calc": arch_07_drawings_impact_on_owners_equity_calc,
    "08_assets_definition_business_possessions": arch_08_assets_definition_business_possessions,
    "09_fixed_assets_long_term_identification": arch_09_fixed_assets_long_term_identification,
    "10_current_assets_short_term_liquidity": arch_10_current_assets_short_term_liquidity,
    "11_fixed_vs_current_assets_classification_table": arch_11_fixed_vs_current_assets_classification_table,
    "12_trading_stock_purpose_for_profit": arch_12_trading_stock_purpose_for_profit,
    "13_cash_float_calculation_register_notes": arch_13_cash_float_calculation_register_notes,
    "14_liabilities_definition_external_debts": arch_14_liabilities_definition_external_debts,
    "15_long_term_liabilities_multi_year_loans": arch_15_long_term_liabilities_multi_year_loans,
    "16_current_liabilities_within_one_year": arch_16_current_liabilities_within_one_year,
    "17_long_term_vs_current_liabilities_table": arch_17_long_term_vs_current_liabilities_table,
    "18_accounting_equation_balance_visual": arch_18_accounting_equation_balance_visual,
    "19_income_increases_equity_definition": arch_19_income_increases_equity_definition,
    "20_expenses_operational_costs_definition": arch_20_expenses_operational_costs_definition,
    "21_income_vs_expense_classification_table": arch_21_income_vs_expense_classification_table,
    "22_profit_motive_commercial_purpose": arch_22_profit_motive_commercial_purpose,
    "23_profit_calculation_income_minus_expenses": arch_23_profit_calculation_income_minus_expenses,
    "24_net_loss_exceeding_expenses_calculation": arch_24_net_loss_exceeding_expenses_calculation,
    "25_trade_goods_vs_rendering_service_distinction": arch_25_trade_goods_vs_rendering_service_distinction,
}
