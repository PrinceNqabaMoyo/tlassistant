"""Grade 9 EMS - Term 4 Business Plan: Archetypes 26 to 50.

Grounded strictly in curriculum_docs_auto/EMS_Gr9/Term 4/04. Business Plan.md
and EMS_Gr9/Syllabus.md.
Zero-LLM, 100% deterministic, financial planning, cost classification, break-even,
mark-up, profit ratios, cash flow, balance sheet, and synthesis contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES

from .term4_business_plan_archetypes_01_25 import (
    _build_mcq,
    _build_short,
    _build_table,
    _esc,
    _fmt_r,
    _make_cell,
    get_ems_scenario,
)


def arch_26_financial_plan_five_core_statements_overview(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Inside **{sc['business']}**'s financial projections in **{sc['area']}**, accountants assemble quantitative schedules for funders.\n\n"
        "Which set lists the **core financial statements and analyses** expected inside a formal business proposal?"
    )
    correct = "Start-up capital budget, 3-year cash flow projection, projected income statement, break-even analysis, and projected balance sheet."
    distractors = [
        "Only a shop-window poster and three customer names.",
        "Employee leave calendars and monthly delivery truck routes only.",
        "Raw plastic recycling logs without Rand values or budgets.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_26",
        subskill="26_financial_plan_five_core_statements_overview",
        title="Core Schedules in a Financial Section",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"A credible financial section for **{sc['business']}** proves start-up needs, cash survival (cash flow), profitability (income statement), break-even volume, and solvency (balance sheet)."
        ),
        hints={
            "tier_1": "Think about what shows capital needed, monthly cash survival, profit, break-even, and net worth.",
            "tier_2": "Capital budget, cash flow projection, income statement, break-even analysis, balance sheet.",
            "tier_3": correct,
        },
        misconception_tags=["omitting_cash_flow_and_break_even_from_financial_projections"],
    )


def arch_27_startup_capital_vs_operating_working_capital_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    equip = rng.choice([85000, 110000, 140000])
    init_stock = rng.choice([25000, 35000, 45000])
    monthly_opex = rng.choice([18000, 22000, 25000])
    months_reserve = 3
    working_cap = monthly_opex * months_reserve
    total_start = equip + init_stock + working_cap
    prompt = (
        f"**{sc['entrepreneur']}** budgets the launch costs of **{sc['business']}** in **{sc['area']}**:\n"
        f"- Equipment & machinery (fixed assets): **{_fmt_r(equip)}**\n"
        f"- Initial trading stock & packaging: **{_fmt_r(init_stock)}**\n"
        f"- Monthly operating expenses (rent, wages, utilities): **{_fmt_r(monthly_opex)}/month** — must keep **{months_reserve} months** of working capital reserve.\n\n"
        "Calculate the **working capital reserve** needed and the **total start-up capital** required."
    )
    expected = (
        f"Working capital reserve = {_fmt_r(working_cap)}; "
        f"Total start-up capital = {_fmt_r(total_start)}."
    )
    sol = (
        f"**Start-Up Capital Budget ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Working Capital ({months_reserve} months):** ${months_reserve} \\times {_fmt_r(monthly_opex)} = {_fmt_r(working_cap)}$ **[2]**\n"
        f"2. **Total Start-Up Capital:** ${_fmt_r(equip)} + {_fmt_r(init_stock)} + {_fmt_r(working_cap)} = {_fmt_r(total_start)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_27",
        subskill="27_startup_capital_vs_operating_working_capital_calc",
        title="Calculating Start-Up & Working Capital",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Multiply monthly operating costs by 3 months first, then add equipment and opening stock.",
            "tier_2": f"{_fmt_r(equip)} + {_fmt_r(init_stock)} + ({months_reserve} x {_fmt_r(monthly_opex)}).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Working capital reserve {_fmt_r(working_cap)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Total start-up capital {_fmt_r(total_start)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["forgetting_working_capital_months_when_budgeting_startup_needs"],
    )


def arch_28_fixed_vs_variable_costs_classification_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pool = [
        ("Monthly shop rental of R8 500 regardless of units sold", "Fixed Cost", "Constant even at zero output"),
        ("Raw ingredients per baked unit (R12 per item)", "Variable Cost", "Scales directly with production"),
        ("Permanent store manager fixed monthly salary", "Fixed Cost", "Does not change with output"),
        ("Cardboard packaging boxes used only per item sold", "Variable Cost", "Zero boxes needed if zero sold"),
        ("Monthly business insurance premium", "Fixed Cost", "Contractual time-based cost"),
        ("Salesperson commission of R15 per completed sale", "Variable Cost", "Varies directly with sales volume"),
    ]
    chosen = rng.sample(pool, 4)
    headers = ["Expense Item", "Cost Behaviour", "Classification (Fixed Cost vs Variable Cost)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Expense Item | Cost Behaviour | Classification |", "| :--- | :--- | :--- |"]
    for idx, (item, cls, beh) in enumerate(chosen):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", item, "given"),
            _make_cell(f"t0_r{idx}_c1", beh, "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = cls
        cell_hints[coord] = "Enter exact label: Fixed Cost or Variable Cost."
        memo_lines.append(f"| {item} | {beh} | {cls} |")

    sample = "; ".join(f"{i+1}: {chosen[i][1]}" for i in range(4))
    worked = f"**Cost Classification Schedule ({sc['business']}) [4 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bp_28",
        subskill="28_fixed_vs_variable_costs_classification_table",
        title="Fixed Costs vs Variable Costs Matrix",
        prompt=(
            f"Classify four monthly expenses for **{sc['business']}** in **{sc['area']}** as **Fixed Cost** or **Variable Cost** in Column 3."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=4,
        hints={
            "tier_1": "Fixed Costs stay constant even when 0 units are made; Variable Costs rise and fall directly with units made.",
            "tier_2": "Write exact labels: Fixed Cost or Variable Cost.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"Classifies as {chosen[i][1]}", "marks": 1, "editable": True}
            for i in range(4)
        ],
        misconception_tags=["classifying_raw_materials_or_commissions_as_fixed_costs"],
    )


def arch_29_semi_variable_and_stepped_fixed_costs_concept(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    base_fee = rng.choice([950, 1200, 1500])
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** pays a municipal utility tariff of **{_fmt_r(base_fee)}/month** fixed network charge PLUS **R2,50 per unit** consumed.\n\n"
        "How is a cost with both a **fixed base fee** and a **usage-linked portion** classified?"
    )
    correct = "A semi-variable (mixed) cost, because part remains fixed while the remainder increases with activity."
    distractors = [
        "A strictly fixed cost that remains unchanged even during 24-hour double production shifts.",
        "An equity capital contribution by shareholders.",
        "A pure variable cost equal to R0 whenever production pauses.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_29",
        subskill="29_semi_variable_and_stepped_fixed_costs_concept",
        title="Semi-Variable (Mixed) Costs",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Because **{_fmt_r(base_fee)}** is payable regardless of usage while extra units add **R2,50** each, utility bills combine fixed and variable elements (**semi-variable cost**)."
        ),
        hints={
            "tier_1": "Look at the word combining both Fixed + Variable.",
            "tier_2": "Semi-variable (mixed) cost = fixed component + usage component.",
            "tier_3": correct,
        },
        misconception_tags=["forcing_utility_tariffs_into_pure_fixed_or_pure_variable"],
    )


def arch_30_total_cost_tc_linear_equation_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    fc = rng.choice([12000, 15000, 18000])
    vc_unit = rng.choice([35, 45, 55])
    qty = rng.choice([400, 500, 600])
    total_vc = vc_unit * qty
    total_cost = fc + total_vc
    prompt = (
        f"For **{sc['business']}** in **{sc['area']}**, monthly **Fixed Costs (FC)** equal **{_fmt_r(fc)}**, and **Variable Cost per unit (VC)** is **{_fmt_r(vc_unit)}**.\n\n"
        f"If the business produces **{qty} units** this month, calculate:\n"
        "1. **Total Variable Costs**.\n"
        "2. **Total Production Cost (TC = FC + Total VC)**."
    )
    expected = f"1. Total Variable Costs = {_fmt_r(total_vc)}; 2. Total Cost = {_fmt_r(total_cost)}."
    sol = (
        f"**Total Cost Calculation ({qty} units at {sc['business']}) [3 marks]:**\n\n"
        f"1. **Total Variable Cost:** ${qty} \\times {_fmt_r(vc_unit)} = {_fmt_r(total_vc)}$ **[1]**\n"
        f"2. **Total Cost (TC):** ${_fmt_r(fc)} + {_fmt_r(total_vc)} = {_fmt_r(total_cost)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_30",
        subskill="30_total_cost_tc_linear_equation_calculation",
        title="Calculating Total Cost (TC = FC + VC x Q)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Multiply Variable Cost per unit by quantity produced, then add Fixed Costs.",
            "tier_2": f"({qty} x {_fmt_r(vc_unit)}) + {_fmt_r(fc)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Total Variable Cost {_fmt_r(total_vc)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Total Cost {_fmt_r(total_cost)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["multiplying_fixed_costs_by_quantity_produced"],
    )


def arch_31_contribution_margin_per_unit_and_ratio(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sp = rng.choice([200, 250, 400])
    vc = rng.choice([120, 150, 240]) if sp == 400 else (120 if sp == 200 else 150)
    if sp == 400 and vc not in (160, 240):
        vc = 240
    cm = sp - vc
    cm_ratio = round((cm / sp) * 100)
    prompt = (
        f"**{sc['business']}** sells handmade hampers in **{sc['area']}** at a **Selling Price (SP)** of **{_fmt_r(sp)}** each, "
        f"with **Variable Cost (VC)** of **{_fmt_r(vc)} per unit**.\n\n"
        "Calculate:\n"
        "1. The **Contribution Margin per unit (SP - VC)**.\n"
        "2. The **Contribution Margin Ratio (%)** as a percentage of Selling Price, and state what each unit's contribution pays toward first."
    )
    expected = (
        f"1. Contribution Margin = {_fmt_r(cm)} per unit. "
        f"2. Contribution Margin Ratio = {cm_ratio}%; it pays toward covering monthly Fixed Costs first (and once exceeded, generates profit)."
    )
    sol = (
        f"**Contribution Margin Analysis ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Contribution per Unit:** ${_fmt_r(sp)} - {_fmt_r(vc)} = {_fmt_r(cm)}$ **[1]**\n"
        f"2. **Contribution Ratio:** $\\frac{{{cm}}}{{{sp}}} \\times 100 = {cm_ratio}\\%$ **[2]**\n"
        f"3. **Meaning:** Every unit sold contributes **{_fmt_r(cm)}** toward covering **Fixed Costs** until break-even is reached **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_31",
        subskill="31_contribution_margin_per_unit_and_ratio",
        title="Contribution Margin & Contribution Ratio",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Contribution = Selling Price - Variable Cost; divide by Selling Price x 100 for ratio.",
            "tier_2": f"{sp} - {vc} = {cm}; ({cm}/{sp}) x 100 = {cm_ratio}%.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Contribution Margin {_fmt_r(cm)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Contribution Ratio {cm_ratio}%", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Covers Fixed Costs first before profit", "marks": 1, "editable": True},
        ],
        misconception_tags=["confusing_contribution_margin_with_net_profit"],
    )


def arch_32_breakeven_point_units_formula_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sp = rng.choice([250, 300, 350])
    vc = rng.choice([150, 180, 210])
    if sp == 250:
        vc = 150
    elif sp == 300:
        vc = 180
    else:
        vc = 210
    cm = sp - vc
    bep_units = rng.choice([80, 120, 150])
    fc = bep_units * cm
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** has monthly **Fixed Costs** of **{_fmt_r(fc)}**, sells each item for **{_fmt_r(sp)}**, "
        f"and incurs **Variable Costs** of **{_fmt_r(vc)} per unit**.\n\n"
        "Show the formula and calculate the exact **Break-Even Point (BEP) in units** per month."
    )
    expected = f"Contribution Margin = {_fmt_r(cm)}/unit; BEP = {_fmt_r(fc)} / {_fmt_r(cm)} = {bep_units} units."
    sol = (
        f"**Break-Even Point Calculation ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Formula:** $\\text{{BEP (units)}} = \\frac{{\\text{{Fixed Costs}}}}{{\\text{{Selling Price}} - \\text{{Variable Cost per unit}}}}$ **[1]**\n"
        f"2. **Contribution Margin:** ${_fmt_r(sp)} - {_fmt_r(vc)} = {_fmt_r(cm)}$ per unit **[1]**\n"
        f"3. **Break-Even Units:** $\\frac{{{fc}}}{{{cm}}} = {bep_units}$ units per month **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_32",
        subskill="32_breakeven_point_units_formula_calculation",
        title="Break-Even Point (BEP) in Units",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "BEP = Fixed Costs / (Selling Price - Variable Cost).",
            "tier_2": f"Divide {_fmt_r(fc)} by ({_fmt_r(sp)} - {_fmt_r(vc)}) = {_fmt_r(cm)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Correct BEP formula", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Contribution Margin {_fmt_r(cm)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"BEP = {bep_units} units", "marks": 2, "editable": True},
        ],
        misconception_tags=["dividing_fixed_costs_by_selling_price_instead_of_contribution"],
    )


def arch_33_breakeven_point_rand_turnover_value_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sp = rng.choice([200, 300, 500])
    cm = int(sp * 0.4)
    vc = sp - cm
    bep_units = rng.choice([100, 150, 200])
    fc = bep_units * cm
    bep_rand = bep_units * sp
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** budgets **Fixed Costs = {_fmt_r(fc)}**, **Selling Price = {_fmt_r(sp)}**, and **Variable Cost = {_fmt_r(vc)}/unit**.\n\n"
        "Calculate the **Break-Even Point in units** AND the **Break-Even Point in Rand turnover (Rand sales value)**."
    )
    expected = f"BEP = {bep_units} units; Break-Even Turnover (Rand value) = {_fmt_r(bep_rand)}."
    sol = (
        f"**Break-Even Units & Rand Turnover ({sc['business']}) [4 marks]:**\n\n"
        f"1. **BEP (units):** $\\frac{{{fc}}}{{{sp} - {vc}}} = \\frac{{{fc}}}{{{cm}}} = {bep_units}$ units **[2]**\n"
        f"2. **BEP (Rand Sales Value):** ${bep_units} \\times {_fmt_r(sp)} = {_fmt_r(bep_rand)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_33",
        subskill="33_breakeven_point_rand_turnover_value_calculation",
        title="Break-Even Point in Rand Turnover",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Find Break-Even units first, then multiply by Selling Price per unit.",
            "tier_2": f"BEP units = {fc} / {cm} = {bep_units}; Rand BEP = {bep_units} x {_fmt_r(sp)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"BEP units = {bep_units}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"BEP Rand turnover = {_fmt_r(bep_rand)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["multiplying_bep_units_by_variable_cost_instead_of_selling_price"],
    )


def arch_34_breakeven_graph_interpretation_tr_tc_fc_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sp = rng.choice([200, 250, 300])
    cm = int(sp * 0.4)
    vc = sp - cm
    bep_u = rng.choice([100, 120, 150])
    fc = bep_u * cm
    bep_r = bep_u * sp
    max_u = bep_u * 2
    max_tr = max_u * sp
    max_tc = fc + (max_u * vc)
    # SVG coordinates: plot origin (100, 220), x max=560 (2*bep_u -> x=560), y top=45 (max_tr)
    # BEP point is exactly halfway x = 330, y = 220 - 175*(bep_r/max_tr) = 220 - 87.5 = 132.5 -> 132
    fc_y = int(round(220 - 175 * (fc / max_tr)))
    tc_end_y = int(round(220 - 175 * (max_tc / max_tr)))
    profit_at_max = max_tr - max_tc
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 275" width="100%" height="auto">'
        '<rect x="0" y="0" width="640" height="275" fill="#f8fafc" rx="10"/>'
        f'<text x="320" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Break-Even Chart: {_esc(sc["business"])} (SP {_fmt_r(sp)}, VC {_fmt_r(vc)}, FC {_fmt_r(fc)})</text>'
        '<polygon points="100,220 330,132 100,' + str(fc_y) + '" fill="#fee2e2" opacity="0.65"/>'
        '<polygon points="330,132 560,45 560,' + str(tc_end_y) + '" fill="#dcfce7" opacity="0.7"/>'
        '<line x1="100" y1="220" x2="575" y2="220" stroke="#334155" stroke-width="2"/>'
        '<line x1="100" y1="38" x2="100" y2="220" stroke="#334155" stroke-width="2"/>'
        f'<line x1="100" y1="{fc_y}" x2="560" y2="{fc_y}" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5,4"/>'
        f'<text x="94" y="{fc_y + 4}" text-anchor="end" font-size="10" fill="#475569">{_fmt_r(fc)} (FC)</text>'
        '<line x1="100" y1="220" x2="560" y2="45" stroke="#16a34a" stroke-width="2.5"/>'
        '<text x="564" y="49" font-size="10.5" font-weight="bold" fill="#15803d">TR</text>'
        f'<line x1="100" y1="{fc_y}" x2="560" y2="{tc_end_y}" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="564" y="{tc_end_y + 4}" font-size="10.5" font-weight="bold" fill="#b91c1c">TC</text>'
        '<line x1="330" y1="132" x2="330" y2="220" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="4,3"/>'
        '<line x1="100" y1="132" x2="330" y2="132" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="4,3"/>'
        '<circle cx="330" cy="132" r="5" fill="#2563eb"/>'
        f'<text x="330" y="120" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e3a8a">BEP ({bep_u} u, {_fmt_r(bep_r)})</text>'
        '<text x="175" y="182" font-size="10" font-weight="bold" fill="#991b1b">LOSS ZONE</text>'
        '<text x="455" y="96" font-size="10" font-weight="bold" fill="#14532d">PROFIT ZONE</text>'
        f'<text x="94" y="136" text-anchor="end" font-size="10" fill="#1e40af">{_fmt_r(bep_r)}</text>'
        '<text x="100" y="236" text-anchor="middle" font-size="10" fill="#334155">0</text>'
        f'<text x="330" y="236" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e40af">{bep_u}</text>'
        f'<text x="560" y="236" text-anchor="middle" font-size="10" fill="#334155">{max_u} units</text>'
        '<text x="330" y="258" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">Monthly Output / Sales Volume (Units)</text>'
        '</svg>'
    )
    prompt = (
        f"Study the Cost-Volume-Profit break-even graph for **{sc['business']}** (**SP = {_fmt_r(sp)}**, **VC = {_fmt_r(vc)}**, **FC = {_fmt_r(fc)}**).\n\n"
        f"1. Read the **Break-Even Point** (units and Rand turnover) where the **TR** and **TC** lines intersect.\n"
        f"2. Calculate the **net profit** earned if **{sc['business']}** produces and sells **{max_u} units** in the **Profit Zone**."
    )
    expected = (
        f"1. Break-Even Point = {bep_u} units / {_fmt_r(bep_r)} sales value. "
        f"2. At {max_u} units: TR = {_fmt_r(max_tr)}, TC = {_fmt_r(max_tc)}, Net Profit = {_fmt_r(profit_at_max)}."
    )
    sol = (
        f"**Break-Even Graph Interpretation ({sc['business']}) [5 marks]:**\n\n"
        f"1. **Intersection (TR = TC):** Occurs at **{bep_u} units** and **{_fmt_r(bep_r)}** turnover **[2]**.\n"
        f"2. **Profit at {max_u} units:**\n"
        f"   - Total Revenue (TR): ${max_u} \\times {_fmt_r(sp)} = {_fmt_r(max_tr)}$ **[1]**\n"
        f"   - Total Cost (TC): ${_fmt_r(fc)} + ({max_u} \\times {_fmt_r(vc)}) = {_fmt_r(max_tc)}$ **[1]**\n"
        f"   - **Net Profit:** ${_fmt_r(max_tr)} - {_fmt_r(max_tc)} = {_fmt_r(profit_at_max)}$ **[1]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_34",
        subskill="34_breakeven_graph_interpretation_tr_tc_fc_svg",
        title="Break-Even Chart Interpretation (TR, TC & FC)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=5,
        hints={
            "tier_1": "Read the blue intersection dot for BEP, then compute TR - TC at full capacity.",
            "tier_2": f"BEP = ({bep_u} units, {_fmt_r(bep_r)}); Profit = ({max_u} x {sp}) - ({fc} + {max_u} x {vc}).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Reads BEP {bep_u} units & {_fmt_r(bep_r)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Total Revenue {_fmt_r(max_tr)} & Total Cost {_fmt_r(max_tc)}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Net Profit {_fmt_r(profit_at_max)}", "marks": 1, "editable": True},
        ],
        misconception_tags=["reading_y_intercept_fc_as_zero_instead_of_fixed_cost"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_35_margin_of_safety_units_and_rand_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    bep_u = rng.choice([120, 150, 200])
    budget_u = bep_u + rng.choice([45, 60, 80])
    sp = rng.choice([150, 200, 250])
    mos_u = budget_u - bep_u
    mos_r = mos_u * sp
    prompt = (
        f"**{sc['business']}** breaks even at **{bep_u} units per month** and budgets actual monthly sales of **{budget_u} units** at **{_fmt_r(sp)} each**.\n\n"
        "Calculate the **Margin of Safety** in **units** and **Rand turnover**, and briefly state what it tells the owner."
    )
    expected = (
        f"Margin of Safety = {mos_u} units ({_fmt_r(mos_r)}); "
        f"sales can drop by up to {mos_u} units before {sc['business']} begins making a loss."
    )
    sol = (
        f"**Margin of Safety ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Margin of Safety (units):** ${budget_u} - {bep_u} = {mos_u}$ units **[2]**\n"
        f"2. **Margin of Safety (Rand):** ${mos_u} \\times {_fmt_r(sp)} = {_fmt_r(mos_r)}$ **[1]**\n"
        f"3. **Meaning:** Revenue can fall by **{_fmt_r(mos_r)}** (**{mos_u} units**) before dipping below break-even into losses **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_35",
        subskill="35_margin_of_safety_units_and_rand_calculation",
        title="Margin of Safety (Units & Rand Buffer)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Margin of Safety = Budgeted Sales - Break-Even Sales.",
            "tier_2": f"({budget_u} - {bep_u}) units x {_fmt_r(sp)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Margin of Safety = {mos_u} units", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Rand buffer = {_fmt_r(mos_r)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Explains drop buffer before losses begin", "marks": 1, "editable": True},
        ],
        misconception_tags=["adding_bep_to_budgeted_sales_for_margin_of_safety"],
    )


def arch_36_target_profit_required_sales_volume_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sp = rng.choice([250, 300, 350])
    vc = 150 if sp == 250 else (180 if sp == 300 else 210)
    cm = sp - vc
    fc = rng.choice([12000, 15000, 18000])
    target_profit = rng.choice([18000, 24000, 30000])
    # Ensure exact divisibility by adjusting fc/target slightly if needed:
    rem = (fc + target_profit) % cm
    if rem != 0:
        fc += (cm - rem)
    req_units = (fc + target_profit) // cm
    prompt = (
        f"**{sc['business']}** faces monthly **Fixed Costs of {_fmt_r(fc)}**, sells goods at **{_fmt_r(sp)}**, with **Variable Costs of {_fmt_r(vc)}/unit**.\n\n"
        f"How many **units** must be sold per month to earn a **target net profit of {_fmt_r(target_profit)}**?"
    )
    expected = f"Contribution = {_fmt_r(cm)}/unit; Required sales = ({_fmt_r(fc)} + {_fmt_r(target_profit)}) / {_fmt_r(cm)} = {req_units} units."
    sol = (
        f"**Target Profit Volume Calculation ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Contribution per Unit:** ${_fmt_r(sp)} - {_fmt_r(vc)} = {_fmt_r(cm)}$ **[1]**\n"
        f"2. **Required Units:** $\\frac{{\\text{{FC}} + \\text{{Target Profit}}}}{{\\text{{CM}}}} = \\frac{{{fc} + {target_profit}}}{{{cm}}} = \\frac{{{fc + target_profit}}}{{{cm}}} = {req_units}$ units **[3]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_36",
        subskill="36_target_profit_required_sales_volume_calculation",
        title="Sales Volume Needed for Target Profit",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Add Fixed Costs + Target Profit together first, then divide by Contribution Margin per unit.",
            "tier_2": f"({fc} + {target_profit}) / ({sp} - {vc}).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Contribution margin {_fmt_r(cm)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Adds FC + Target Profit = {_fmt_r(fc + target_profit)} & divides by {cm}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Final answer {req_units} units", "marks": 2, "editable": True},
        ],
        misconception_tags=["computing_bep_only_and_forgetting_to_add_target_profit"],
    )


def arch_37_effect_of_price_or_cost_change_on_bep_sensitivity(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sp = 250
    old_vc = 130
    new_vc = rng.choice([150, 170])
    old_cm = sp - old_vc  # 120
    new_cm = sp - new_vc  # 100 or 80
    fc = 24000
    old_bep = fc // old_cm  # 200
    new_bep = fc // new_cm  # 240 or 300
    extra_units = new_bep - old_bep
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** has **Fixed Costs = {_fmt_r(fc)}**, **Selling Price = {_fmt_r(sp)}**, and **Variable Cost = {_fmt_r(old_vc)}/unit**.\n"
        f"Due to supplier inflation, **Variable Cost rises to {_fmt_r(new_vc)}/unit** while Selling Price stays at **{_fmt_r(sp)}**.\n\n"
        "Calculate the **old break-even units**, the **new break-even units**, and state how many **extra units** must now be sold just to avoid losses."
    )
    expected = f"Old BEP = {old_bep} units; New BEP = {new_bep} units; {extra_units} extra units needed."
    sol = (
        f"**BEP Cost-Inflation Impact ({sc['business']}) [5 marks]:**\n\n"
        f"1. **Original BEP:** $\\frac{{{fc}}}{{{sp} - {old_vc}}} = \\frac{{{fc}}}{{{old_cm}}} = {old_bep}$ units **[2]**\n"
        f"2. **Revised BEP:** $\\frac{{{fc}}}{{{sp} - {new_vc}}} = \\frac{{{fc}}}{{{new_cm}}} = {new_bep}$ units **[2]**\n"
        f"3. **Impact:** Break-even threshold jumps by **{extra_units} extra units** (+{round((extra_units / old_bep) * 100)}%) **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_37",
        subskill="37_effect_of_price_or_cost_change_on_bep_sensitivity",
        title="How Variable Cost Rises Shift Break-Even Point",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=5,
        hints={
            "tier_1": "Calculate BEP before and after Variable Cost increases; rising VC shrinks contribution margin.",
            "tier_2": f"Old BEP = {fc} / {old_cm}; New BEP = {fc} / {new_cm}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Old BEP = {old_bep} units", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"New BEP = {new_bep} units", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": f"Extra units needed = {extra_units}", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_rising_variable_cost_lowers_break_even_units"],
    )


def arch_38_cost_price_selling_price_and_markup_percentage_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cp = rng.choice([120, 160, 200, 250])
    markup_pct = rng.choice([25, 40, 50])
    sp = int(cp * (1 + markup_pct / 100))
    profit = sp - cp
    prompt = (
        f"**{sc['business']}** in **{sc['area']}** buys wholesale backpacks at a **Cost Price of {_fmt_r(cp)}** and sells them for **{_fmt_r(sp)}** each.\n\n"
        "Show the formula and calculate the **percentage mark-up on cost price**."
    )
    expected = f"Profit per item = {_fmt_r(profit)}; Mark-up % = ({profit} / {cp}) x 100 = {markup_pct}%."
    sol = (
        f"**Mark-Up Percentage ({sc['business']}) [4 marks]:**\n\n"
        "1. **Formula:** $\\text{Mark-up \\%} = \\frac{\\text{Selling Price} - \\text{Cost Price}}{\\text{Cost Price}} \\times 100$ **[1]**\n"
        f"2. **Profit per Unit:** ${_fmt_r(sp)} - {_fmt_r(cp)} = {_fmt_r(profit)}$ **[1]**\n"
        f"3. **Mark-up %:** $\\frac{{{profit}}}{{{cp}}} \\times 100 = {markup_pct}\\%$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_38",
        subskill="38_cost_price_selling_price_and_markup_percentage_calc",
        title="Calculating Mark-Up Percentage on Cost",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Divide (Selling Price - Cost Price) by Cost Price, then multiply by 100.",
            "tier_2": f"(({sp} - {cp}) / {cp}) x 100.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Uses Cost Price in denominator", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Unit profit {_fmt_r(profit)}", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": f"Mark-up = {markup_pct}%", "marks": 2, "editable": True},
        ],
        misconception_tags=["dividing_by_selling_price_instead_of_cost_price_for_markup"],
    )


def arch_39_calculating_selling_price_from_cost_and_markup_pct(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cp = rng.choice([80, 140, 180, 220])
    markup = rng.choice([30, 45, 60])
    sp = cp * (100 + markup) / 100
    markup_rand = sp - cp
    prompt = (
        f"**{sc['business']}** purchases stock for **{_fmt_r(cp)} per item** and applies a standard **{markup}% mark-up on cost**.\n\n"
        "Calculate the **Rand mark-up added** and the final **Selling Price**."
    )
    expected = f"Mark-up added = {_fmt_r(markup_rand)}; Selling Price = {_fmt_r(sp)}."
    sol = (
        f"**Selling Price Pricing ({sc['business']}) [3 marks]:**\n\n"
        f"1. **Mark-Up Amount ({markup}%):** $\\frac{{{markup}}}{{100}} \\times {_fmt_r(cp)} = {_fmt_r(markup_rand)}$ **[1]**\n"
        f"2. **Selling Price:** ${_fmt_r(cp)} + {_fmt_r(markup_rand)} = {_fmt_r(sp)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_39",
        subskill="39_calculating_selling_price_from_cost_and_markup_pct",
        title="Determining Selling Price Using Mark-Up %",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Multiply Cost Price by (100 + mark-up%) / 100.",
            "tier_2": f"{_fmt_r(cp)} + ({markup}% of {_fmt_r(cp)}).",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Mark-up Rand {_fmt_r(markup_rand)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Selling Price {_fmt_r(sp)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["subtracting_markup_from_100_instead_of_adding"],
    )


def arch_40_calculating_cost_price_backward_from_selling_price(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    cp = rng.choice([120, 200, 240, 300])
    markup = rng.choice([25, 50])
    sp = int(cp * (100 + markup) / 100)
    prompt = (
        f"**{sc['business']}** prices an item at a **Selling Price of {_fmt_r(sp)}** using a **{markup}% mark-up on cost**.\n\n"
        "Working backward, calculate the **original wholesale Cost Price**."
    )
    expected = f"Cost Price = ({_fmt_r(sp)} x 100) / {100 + markup} = {_fmt_r(cp)}."
    sol = (
        f"**Backward Cost Price Calculation ({sc['business']}) [3 marks]:**\n\n"
        f"- **Formula:** $\\text{{CP}} = \\text{{SP}} \\times \\frac{{100}}{{100 + \\text{{Mark-up \\%}}}}$ **[1]**\n"
        f"- **Calculation:** $\\text{{CP}} = {_fmt_r(sp)} \\times \\frac{{100}}{{{100 + markup}}} = {_fmt_r(cp)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_40",
        subskill="40_calculating_cost_price_backward_from_selling_price",
        title="Working Backward from Selling Price to Cost Price",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Never multiply Selling Price by (1 - markup%). Divide by 1 + (markup%/100).",
            "tier_2": f"CP = {_fmt_r(sp)} x 100 / {100 + markup}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Divides by {100 + markup}% (multiplies by 100/{100 + markup})", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Cost Price = {_fmt_r(cp)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["subtracting_markup_pct_directly_from_selling_price"],
    )


def arch_41_gross_profit_margin_vs_markup_percentage_distinction(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"During financial checks at **{sc['business']}** in **{sc['area']}**, learners compare **Mark-up %** against **Gross Profit Margin % on Sales**.\n\n"
        "What is the **exact mathematical difference** between the two ratios?"
    )
    correct = "Mark-up % divides Gross Profit by Cost Price (x 100), whereas Gross Profit Margin % divides Gross Profit by Selling Price / Sales Revenue (x 100)."
    distractors = [
        "Mark-up % divides Fixed Costs by Revenue while Gross Profit Margin divides Rent by Assets.",
        "Both ratios are always identical percentages whenever Selling Price exceeds Cost Price.",
        "Gross Profit Margin deducts owner personal drawings before dividing by Cost Price.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_41",
        subskill="41_gross_profit_margin_vs_markup_percentage_distinction",
        title="Mark-Up % vs Gross Profit Margin %",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            "Since Cost Price is smaller than Selling Price on profitable items, **Mark-up %** (denominator = CP) is always higher than **Gross Profit Margin %** (denominator = SP)."
        ),
        hints={
            "tier_1": "Check the denominator of each percentage formula.",
            "tier_2": "Mark-up denominator = Cost Price; Gross Profit Margin denominator = Sales / Selling Price.",
            "tier_3": correct,
        },
        misconception_tags=["treating_markup_percentage_and_gross_margin_percentage_as_equal"],
    )


def arch_42_projected_income_statement_revenue_expenses_profit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sales = rng.choice([180000, 220000, 260000])
    cos = rng.choice([100000, 120000, 140000])
    gp = sales - cos
    opex = rng.choice([45000, 52000, 60000])
    net_profit = gp - opex
    prompt = (
        f"Prepare a summary **Projected Income Statement** calculation for **{sc['business']}**'s first quarter in **{sc['area']}**:\n"
        f"- Sales Revenue (Turnover): **{_fmt_r(sales)}**\n"
        f"- Cost of Sales: **{_fmt_r(cos)}**\n"
        f"- Total Operating Expenses (rent, wages, utilities): **{_fmt_r(opex)}**\n\n"
        "Calculate the **Gross Profit** and **Net Profit**."
    )
    expected = f"Gross Profit = {_fmt_r(gp)}; Net Profit = {_fmt_r(net_profit)}."
    sol = (
        f"**Projected Income Statement ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Gross Profit:** ${_fmt_r(sales)} - {_fmt_r(cos)} = {_fmt_r(gp)}$ **[2]**\n"
        f"2. **Net Profit:** ${_fmt_r(gp)} - {_fmt_r(opex)} = {_fmt_r(net_profit)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_42",
        subskill="42_projected_income_statement_revenue_expenses_profit",
        title="Projected Income Statement (Gross & Net Profit)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Sales - Cost of Sales = Gross Profit; Gross Profit - Operating Expenses = Net Profit.",
            "tier_2": f"GP = {_fmt_r(sales)} - {_fmt_r(cos)}; NP = GP - {_fmt_r(opex)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Gross Profit {_fmt_r(gp)}", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": f"Net Profit {_fmt_r(net_profit)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["omitting_cost_of_sales_or_subtracting_opex_twice"],
    )


def arch_43_net_profit_percentage_on_revenue_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    revenue = rng.choice([200000, 250000, 400000])
    net_pct = rng.choice([15, 18, 22])
    net_profit = int(revenue * net_pct / 100)
    prompt = (
        f"**{sc['business']}** forecasts annual **Revenue of {_fmt_r(revenue)}** and a projected **Net Profit of {_fmt_r(net_profit)}**.\n\n"
        "Write the formula and calculate the **Net Profit Percentage on Revenue**."
    )
    expected = f"Profit % = ({net_profit} / {revenue}) x 100 = {net_pct}%."
    sol = (
        f"**Net Profit Percentage ({sc['business']}) [3 marks]:**\n\n"
        "- **Formula:** $\\text{Profit \\%} = \\frac{\\text{Net Profit}}{\\text{Revenue}} \\times 100$ **[1]**\n"
        f"- **Calculation:** $\\frac{{{net_profit}}}{{{revenue}}} \\times 100 = {net_pct}\\%$ **[2]**\n\n"
        f"*(Meaning **{sc['business']}** keeps **{net_pct} cents** of net profit from every **R1,00** of revenue.)*"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_43",
        subskill="43_net_profit_percentage_on_revenue_calculation",
        title="Net Profit Percentage on Revenue",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Net Profit % = (Net Profit / Revenue) x 100.",
            "tier_2": f"({net_profit} / {revenue}) x 100.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Formula Net Profit / Revenue x 100", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Profit % = {net_pct}%", "marks": 2, "editable": True},
        ],
        misconception_tags=["dividing_revenue_by_net_profit_instead_of_profit_over_revenue"],
    )


def arch_44_three_year_cash_flow_projection_purpose_vs_profit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Even though **{sc['business']}** forecasts healthy Net Profit in Year 1 in **{sc['area']}**, banks demand a **3-Year Cash Flow Projection** alongside Income Statements.\n\n"
        "Why can a profitable new venture still fail without an accurate **Cash Flow Projection**?"
    )
    correct = "Because credit sales count as profit before cash arrives, whereas staff wages, rent, and supplier invoices require actual cash in the bank on exact dates."
    distractors = [
        "Because Cash Flow Projections legally cancel all municipal property rates.",
        "Because profitable businesses are banned from opening commercial bank accounts.",
        "Because cash flow statements replace break-even pricing entirely.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_44",
        subskill="44_three_year_cash_flow_projection_purpose_vs_profit",
        title="Why Cash Flow Timing Differs from Profit",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"'Cash is king': if **{sc['business']}** sells on 60-day credit while paying rent and wages upfront, a liquidity crunch can force closure despite positive accounting profit."
        ),
        hints={
            "tier_1": "Profit happens on invoice date; cash only arrives when debtors actually pay.",
            "tier_2": "Credit sales create timing gaps between booked profit and bank cash needed to pay bills.",
            "tier_3": correct,
        },
        misconception_tags=["equating_accounting_profit_immediately_with_bank_cash"],
    )


def arch_45_balance_sheet_accounting_equation_assets_liabilities_equity(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    assets = rng.choice([450000, 560000, 680000])
    liabilities = rng.choice([150000, 210000, 240000])
    equity = assets - liabilities
    prompt = (
        f"A projected end-of-Year-1 **Balance Sheet** for **{sc['business']}** in **{sc['area']}** shows:\n"
        f"- **Total Assets** (equipment, stock & bank): **{_fmt_r(assets)}**\n"
        f"- **Total Liabilities** (bank loan & creditors): **{_fmt_r(liabilities)}**\n\n"
        "Using the accounting equation (**Assets = Liabilities + Equity**), calculate **Owner's Equity**."
    )
    expected = f"Owner's Equity = {_fmt_r(assets)} - {_fmt_r(liabilities)} = {_fmt_r(equity)}."
    sol = (
        f"**Projected Balance Sheet Equation ({sc['business']}) [3 marks]:**\n\n"
        "- **Equation:** $\\text{Equity} = \\text{Assets} - \\text{Liabilities}$ **[1]**\n"
        f"- **Calculation:** ${_fmt_r(assets)} - {_fmt_r(liabilities)} = {_fmt_r(equity)}$ **[2]**"
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_45",
        subskill="45_balance_sheet_accounting_equation_assets_liabilities_equity",
        title="Projected Balance Sheet (A = L + E)",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Rearrange Assets = Liabilities + Equity to solve for Equity.",
            "tier_2": f"Equity = {_fmt_r(assets)} - {_fmt_r(liabilities)}.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Uses Equity = Assets - Liabilities", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Owner's Equity = {_fmt_r(equity)}", "marks": 2, "editable": True},
        ],
        misconception_tags=["adding_assets_and_liabilities_instead_of_subtracting"],
    )


def arch_46_break_even_loss_vs_profit_decision_scenarios_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sp = 200
    vc = 120
    cm = sp - vc  # 80
    fc = rng.choice([8000, 12000])
    bep = fc // cm  # 100 or 150
    below = bep - 40
    above = bep + 50
    scenarios = [
        (below, f"Profit / (Loss) at {below} units", str((below * cm) - fc)),
        (bep, f"Profit / (Loss) at {bep} units", "0"),
        (above, f"Profit / (Loss) at {above} units", str((above * cm) - fc)),
    ]
    headers = ["Monthly Sales Volume (Units)", "Cost & Contribution Check", "Net Profit / Loss (Enter Integer Rand, use - for loss)"]
    rows: List[List[Dict[str, Any]]] = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    memo_lines = ["| Monthly Sales Volume | Calculation | Net Profit / Loss (R) |", "| :--- | :--- | :--- |"]
    for idx, (u, lbl, ans) in enumerate(scenarios):
        coord = f"t0_r{idx}_c2"
        rows.append([
            _make_cell(f"t0_r{idx}_c0", f"{u} units", "given"),
            _make_cell(f"t0_r{idx}_c1", f"CM R{cm}/u; FC R{fc}", "given"),
            _make_cell(coord, "", "required"),
        ])
        correct_map[coord] = ans
        cell_hints[coord] = f"Net = ({u} x R{cm}) - R{fc}. Use minus sign for a loss (e.g. -3200)."
        memo_lines.append(f"| {u} units | ({u} x {cm}) - {fc} | {ans} |")

    sample = "; ".join(f"{s[0]}u -> {s[2]}" for s in scenarios)
    worked = f"**Break-Even Profit/Loss Scenarios ({sc['business']}) [6 marks]:**\n\n" + "\n".join(memo_lines)
    return _build_table(
        rng,
        qid_prefix="g9_bp_46",
        subskill="46_break_even_loss_vs_profit_decision_scenarios_table",
        title="Profit vs Loss Across Output Volumes",
        prompt=(
            f"**{sc['business']}** sells units for **{_fmt_r(sp)}** with **Variable Cost = {_fmt_r(vc)}/unit** (**CM = R{cm}**) and **Fixed Costs = {_fmt_r(fc)}**.\n\n"
            "Enter the exact integer Rand **Net Profit or Loss** in Column 3 for each output level (enter `0` at break-even, or prefix `-` for a loss)."
        ),
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Net Profit = (Units x Contribution Margin) - Fixed Costs.",
            "tier_2": f"CM = R{cm}/unit, FC = R{fc}. Compute ({below}x{cm})-{fc}, ({bep}x{cm})-{fc}, ({above}x{cm})-{fc}.",
            "tier_3": sample,
        },
        marking_points=[
            {"id": f"mp_{i+1}", "desc": f"At {scenarios[i][0]} units: R{scenarios[i][2]}", "marks": 2, "editable": True}
            for i in range(3)
        ],
        misconception_tags=["forgetting_to_deduct_fixed_costs_above_breakeven"],
    )


def arch_47_breakeven_unit_economics_and_pricing_strategy_case(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    bep_units = rng.choice([620, 740, 850])
    max_cap = 500
    prompt = (
        f"Initial calculations show **{sc['business']}** in **{sc['area']}** needs **{bep_units} monthly units** to break even, "
        f"yet maximum shop capacity is only **{max_cap} units per month**.\n\n"
        f"1. Why is this business proposal currently **NOT financially viable**?\n"
        "2. Suggest **two** practical financial adjustments to bring Break-Even below **500 units**."
    )
    expected = (
        f"1. Break-even ({bep_units}) exceeds maximum capacity ({max_cap} units), guaranteeing a monthly loss even at 100% output. "
        "2. Lower Fixed Costs (cheaper premises), lower Variable Cost per unit (negotiate bulk material discounts), or slightly raise Selling Price."
    )
    sol = (
        f"**Viability Diagnosis ({sc['business']}) [4 marks]:**\n\n"
        f"1. **Unviable Break-Even:** Maximum production is **{max_cap} units**, which cannot even reach **{bep_units} units**, so the enterprise would lose cash every month **[2]**.\n"
        "2. **Corrective Levers (any two):** Cut **Fixed Costs** (smaller premises/lower overheads), negotiate cheaper **Variable Costs** per unit, or reposition for a higher **Selling Price** **[2]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_47",
        subskill="47_breakeven_unit_economics_and_pricing_strategy_case",
        title="Diagnosing & Fixing Unviable Break-Even",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Compare required BEP sales against maximum monthly shop capacity.",
            "tier_2": "BEP > max capacity = guaranteed loss; fix via lower FC, lower VC, or higher SP.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Identifies BEP ({bep_units}) > capacity ({max_cap}) causes loss", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Two valid levers (cut FC, cut VC, or lift SP)", "marks": 2, "editable": True},
        ],
        misconception_tags=["ignoring_capacity_constraints_when_evaluating_break_even"],
    )


def arch_48_risk_assessment_and_contingency_plan_in_business_plan(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Before submitting funding paperwork for **{sc['business']}** in **{sc['area']}**, **{sc['entrepreneur']}** adds a **Risk & Contingency Section**.\n\n"
        "Why do prudent lenders value a realistic **Risk & Contingency Section** inside an entrepreneur's proposal?"
    )
    correct = "It demonstrates honest foresight by identifying key threats (like load-shedding, price shocks, or slow sales) alongside practical backup steps."
    distractors = [
        "It proves the entrepreneur expects 0% competition and zero operational challenges.",
        "It allows owners to cancel commercial insurance policies legally.",
        "It forces customers to pay refundable deposits before any adverts appear.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g9_bp_48",
        subskill="48_risk_assessment_and_contingency_plan_in_business_plan",
        title="Risk Assessment & Contingency Planning",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=(
            f"Addressing foreseeable risks realistically reassures lenders that **{sc['business']}** already has backup suppliers, cash cushions, and power alternatives ready."
        ),
        hints={
            "tier_1": "Do investors trust founders who claim 'zero risks exist' or founders with backup steps?",
            "tier_2": "Shows realism and preparedness with actionable backup safeguards.",
            "tier_3": correct,
        },
        misconception_tags=["hiding_known_risks_from_a_funding_proposal"],
    )


def arch_49_business_plan_review_updating_and_viability_check(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"Six months after launching **{sc['business']}** in **{sc['area']}**, fuel costs change and digital sales outpace walk-in traffic.\n\n"
        "Explain why successful entrepreneurs treat a **business plan** as a **living management tool** after opening day rather than shelving it permanently."
    )
    expected = (
        f"Comparing actual monthly revenue and expenses against projected budgets lets {sc['entrepreneur']} spot variances early, "
        "revise marketing channels toward digital growth, and adjust prices or costs before cash runs short."
    )
    sol = (
        f"**Ongoing Review & Control ({sc['business']}) [3 marks]:**\n\n"
        "- **Variance Monitoring:** Contrasting real bank cash flow and sales against original targets reveals problems early **[1.5]**.\n"
        "- **Agile Adaptation:** Allows owners to reallocate budget toward thriving digital sales and recalibrate prices when macro costs shift **[1.5]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_49",
        subskill="49_business_plan_review_updating_and_viability_check",
        title="Reviewing & Updating a Living Business Plan",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Think about General Management 'Control': compare actual results vs projections and adapt.",
            "tier_2": "Detect budget/sales variances early and pivot strategy when market costs or buyer habits change.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Measures actual performance against budgeted targets", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Adapts strategy/pricing to shifting costs or customer channels", "marks": 1, "editable": True},
        ],
        misconception_tags=["assuming_business_planning_ends_once_funding_is_approved"],
    )


def arch_50_holistic_sa_business_plan_and_financial_viability_synthesis(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    sp = 300
    vc = 180
    cm = sp - vc  # 120
    fc = rng.choice([24000, 30000, 36000])
    bep = fc // cm
    prompt = (
        f"**{sc['entrepreneur']}** prepares a full start-up proposal for **{sc['business']}** in **{sc['area']}** (**SP = {_fmt_r(sp)}**, **VC = {_fmt_r(vc)}**, **FC = {_fmt_r(fc)}/month**):\n\n"
        "1. Calculate the monthly **Break-Even Point (units and Rand turnover)**.\n"
        "2. Name **one** section where SWOT/competitor advantage appears and explain how **Place & Promotion** drive reaching that break-even volume.\n"
        "3. State **one** South African legal compliance requirement (besides tax) that must appear in the legal section."
    )
    bep_r = bep * sp
    expected = (
        f"1. BEP = {bep} units ({_fmt_r(bep_r)} turnover). "
        "2. Competitive edge appears in SWOT/Competitor/Executive Summary; accessible Place + targeted Promotion convert target buyers to hit sales > BEP. "
        "3. BCEA/LRA employment compliance, municipal trading licence, NCA (if selling on credit), or IP registration."
    )
    sol = (
        f"**Holistic Business Plan Viability Synthesis ({sc['business']}) [6 marks]:**\n\n"
        f"1. **Break-Even Calculation:**\n"
        f"   - Contribution: ${_fmt_r(sp)} - {_fmt_r(vc)} = {_fmt_r(cm)}$/unit **[1]**\n"
        f"   - BEP (units): $\\frac{{{fc}}}{{{cm}}} = {bep}$ units; Rand Turnover: ${bep} \\times {_fmt_r(sp)} = {_fmt_r(bep_r)}$ **[2]**\n"
        f"2. **Marketing & SWOT Link:** Strengths/USP from **SWOT & Competitor Analysis** guide visible **Place** (high-foot-traffic outlets/online) and targeted **Promotion** to reliably surpass **{bep} monthly sales** **[2]**.\n"
        "3. **Legal Compliance:** Include **municipal trading licence**, **BCEA/LRA** staff compliance, or **NCA/IP** registrations **[1]**."
    )
    return _build_short(
        rng,
        qid_prefix="g9_bp_50",
        subskill="50_holistic_sa_business_plan_and_financial_viability_synthesis",
        title="Holistic Start-Up Feasibility & Financial Synthesis",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=6,
        hints={
            "tier_1": "Compute BEP first, link SWOT/7Ps marketing to sales above BEP, and name a concrete SA legal rule.",
            "tier_2": f"BEP = {bep} units / {_fmt_r(bep_r)} + SWOT/Place+Promotion + BCEA/LRA/Trading Licence.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Contribution {_fmt_r(cm)}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"BEP = {bep} units & {_fmt_r(bep_r)}", "marks": 2, "editable": True},
            {"id": "mp_3", "desc": "Connects SWOT/Competitor edge + Place/Promotion to sales target", "marks": 2, "editable": True},
            {"id": "mp_4", "desc": "Valid legal compliance (BCEA, LRA, NCA, trading licence)", "marks": 1, "editable": True},
        ],
        misconception_tags=["isolating_financial_numbers_from_marketing_and_legal_sections"],
    )


BUILDERS_26_50 = {
    "26_financial_plan_five_core_statements_overview": arch_26_financial_plan_five_core_statements_overview,
    "27_startup_capital_vs_operating_working_capital_calc": arch_27_startup_capital_vs_operating_working_capital_calc,
    "28_fixed_vs_variable_costs_classification_table": arch_28_fixed_vs_variable_costs_classification_table,
    "29_semi_variable_and_stepped_fixed_costs_concept": arch_29_semi_variable_and_stepped_fixed_costs_concept,
    "30_total_cost_tc_linear_equation_calculation": arch_30_total_cost_tc_linear_equation_calculation,
    "31_contribution_margin_per_unit_and_ratio": arch_31_contribution_margin_per_unit_and_ratio,
    "32_breakeven_point_units_formula_calculation": arch_32_breakeven_point_units_formula_calculation,
    "33_breakeven_point_rand_turnover_value_calculation": arch_33_breakeven_point_rand_turnover_value_calculation,
    "34_breakeven_graph_interpretation_tr_tc_fc_svg": arch_34_breakeven_graph_interpretation_tr_tc_fc_svg,
    "35_margin_of_safety_units_and_rand_calculation": arch_35_margin_of_safety_units_and_rand_calculation,
    "36_target_profit_required_sales_volume_calculation": arch_36_target_profit_required_sales_volume_calculation,
    "37_effect_of_price_or_cost_change_on_bep_sensitivity": arch_37_effect_of_price_or_cost_change_on_bep_sensitivity,
    "38_cost_price_selling_price_and_markup_percentage_calc": arch_38_cost_price_selling_price_and_markup_percentage_calc,
    "39_calculating_selling_price_from_cost_and_markup_pct": arch_39_calculating_selling_price_from_cost_and_markup_pct,
    "40_calculating_cost_price_backward_from_selling_price": arch_40_calculating_cost_price_backward_from_selling_price,
    "41_gross_profit_margin_vs_markup_percentage_distinction": arch_41_gross_profit_margin_vs_markup_percentage_distinction,
    "42_projected_income_statement_revenue_expenses_profit": arch_42_projected_income_statement_revenue_expenses_profit,
    "43_net_profit_percentage_on_revenue_calculation": arch_43_net_profit_percentage_on_revenue_calculation,
    "44_three_year_cash_flow_projection_purpose_vs_profit": arch_44_three_year_cash_flow_projection_purpose_vs_profit,
    "45_balance_sheet_accounting_equation_assets_liabilities_equity": arch_45_balance_sheet_accounting_equation_assets_liabilities_equity,
    "46_break_even_loss_vs_profit_decision_scenarios_table": arch_46_break_even_loss_vs_profit_decision_scenarios_table,
    "47_breakeven_unit_economics_and_pricing_strategy_case": arch_47_breakeven_unit_economics_and_pricing_strategy_case,
    "48_risk_assessment_and_contingency_plan_in_business_plan": arch_48_risk_assessment_and_contingency_plan_in_business_plan,
    "49_business_plan_review_updating_and_viability_check": arch_49_business_plan_review_updating_and_viability_check,
    "50_holistic_sa_business_plan_and_financial_viability_synthesis": arch_50_holistic_sa_business_plan_and_financial_viability_synthesis,
}
