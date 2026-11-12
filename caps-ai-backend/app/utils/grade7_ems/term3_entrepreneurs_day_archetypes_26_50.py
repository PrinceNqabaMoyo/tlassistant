"""Grade 7 EMS: Term 3 - Entrepreneur's Day Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/01. Entrepreneur's Day.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, RURAL_AREAS, URBAN_AREAS
from .term3_entrepreneurs_day_archetypes_01_25 import _mcq_q, _calc_q, _rubric_q, _svg_spec


def _ledger_q(
    qid: str,
    subskill: str,
    title: str,
    prompt: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, str],
    cell_hints: Dict[str, str],
    expected_summary: str,
    worked_solution: str,
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: Optional[int] = None,
    curriculum_ref: str = "Term 3 > Entrepreneur's Day > Income and Expenditure Statement",
) -> Dict[str, Any]:
    total_m = marks if marks is not None else max(2, len(correct_map) * 2)
    return {
        "id": qid,
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
        "expected_answer": expected_summary,
        "sample_answer": expected_summary,
        "correct_answer": expected_summary,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": total_m,
        "total_marks": total_m,
        "curriculum_reference": curriculum_ref,
        "hints": hints,
        "misconception_tags": misconception_tags,
    }


def _given_cell(cid: str, val: str) -> Dict[str, Any]:
    return {"cell_id": cid, "value": val, "type": "given", "editable": False}


def _req_cell(cid: str, expected: str) -> Dict[str, Any]:
    return {"cell_id": cid, "value": "", "expected": expected, "type": "required", "editable": True}


def _empty_cell(cid: str) -> Dict[str, Any]:
    return {"cell_id": cid, "value": "", "type": "must_be_empty", "editable": False}


def arch_26_variable_vs_fixed_stall_costs(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    fee = rng.choice([20, 25, 30, 35])
    unit_cost = rng.choice([3, 4, 5])
    item = rng.choice(["pancake", "fruit cup", "boerewors roll", "ice lolly"])
    prompt = (
        f"In {area}, {person} pays R{fee} once for the school table and R{unit_cost} per {item} for fresh ingredients and napkins.\n\n"
        f"Which statement accurately classifies these two Entrepreneur's Day expenses?"
    )
    correct = f"The R{fee} table fee is a fixed cost; the R{unit_cost} per {item} is a variable cost because total ingredients rise with volume"
    distractors = [
        f"The R{fee} table fee is a variable cost; ingredients stay constant whether 5 or 100 units are made",
        "Both expenses are fixed costs regardless of how many items get prepared",
        "Neither cost needs recording in an Income and Expenditure Statement",
    ]
    sol = (
        f"Step 1: Compare cost behaviour:\n"
        f"- Fixed cost: R{fee} table hire stays fixed even if output changes.\n"
        f"- Variable cost: R{unit_cost} per {item} scales directly with units made."
    )
    return _mcq_q(
        rng, f"g7_ed_26_{rng.randint(100000, 999999)}", "26_variable_vs_fixed_stall_costs",
        "Fixed vs Variable Stall Costs", prompt, correct, distractors, sol,
        {"tier_1": "Check which cost changes when output doubles and which stays constant.",
         "tier_2": "Table rental does not depend on sales volume; ingredients do.",
         "tier_3": correct},
        ["inverts_fixed_and_variable_costs"]
    )


def arch_27_per_unit_ingredient_costing_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    roll_c = rng.choice([1.50, 2.00])
    vienna_c = rng.choice([3.00, 3.50, 4.00])
    sauce_c = 0.50
    wrap_c = 0.50
    total_unit = round(roll_c + vienna_c + sauce_c + wrap_c, 2)
    qty = rng.choice([20, 30, 40])
    total_batch = round(total_unit * qty, 2)
    f_u = f"R{total_unit:.2f}".replace(".", ",")
    f_b = f"R{total_batch:.2f}".replace(".", ",")
    headers = ["Ingredient / Wrapping", "Cost per Unit (R)", f"Total for {qty} Units (R)"]
    rows = [
        [_given_cell("r0_c0", "Bread roll"), _given_cell("r0_c1", f"{roll_c:.2f}".replace(".", ",")), _given_cell("r0_c2", f"{roll_c*qty:.2f}".replace(".", ","))],
        [_given_cell("r1_c0", "Vienna sausage"), _given_cell("r1_c1", f"{vienna_c:.2f}".replace(".", ",")), _given_cell("r1_c2", f"{vienna_c*qty:.2f}".replace(".", ","))],
        [_given_cell("r2_c0", "Tomato sauce & margarine"), _given_cell("r2_c1", "0,50"), _given_cell("r2_c2", f"{0.50*qty:.2f}".replace(".", ","))],
        [_given_cell("r3_c0", "Wax wrapping paper"), _given_cell("r3_c1", "0,50"), _given_cell("r3_c2", f"{0.50*qty:.2f}".replace(".", ","))],
        [_given_cell("r4_c0", "TOTAL VARIABLE COST"), _req_cell("r4_c1", f"{total_unit:.2f}".replace(".", ",")), _req_cell("r4_c2", f"{total_batch:.2f}".replace(".", ","))],
    ]
    cmap = {"r4_c1": f"{total_unit:.2f}".replace(".", ","), "r4_c2": f"{total_batch:.2f}".replace(".", ",")}
    chints = {
        "r4_c1": "Sum all four per-unit amounts in column 2.",
        "r4_c2": f"Multiply total unit cost by {qty} hotdogs (or sum column 3).",
    }
    sol = (
        f"1. Unit cost = {roll_c:.2f} + {vienna_c:.2f} + 0,50 + 0,50 = {f_u}.\n"
        f"2. Total batch variable cost ({qty} hotdogs) = {qty} * {f_u} = {f_b}."
    )
    return _ledger_q(
        f"g7_ed_27_{rng.randint(100000, 999999)}", "27_per_unit_ingredient_costing_table",
        "Hotdog Per-Unit and Batch Costing",
        f"{person} plans to sell {qty} wrapped hotdogs. Complete row 5 in the table by entering the total cost per hotdog (R, with comma) and total cost for all {qty} hotdogs.",
        headers, rows, cmap, chints, f"Unit Cost = {f_u}; Batch Total = {f_b}", sol,
        {"tier_1": "Add all unit costs down column 2 first.",
         "tier_2": f"Multiply your unit cost total by {qty}.",
         "tier_3": f"Unit cost: {cmap['r4_c1']}; Batch cost: {cmap['r4_c2']}."},
        ["omits_packaging_cost_in_unit_sum"], marks=4,
    )


def arch_28_total_cost_variable_plus_setup(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    qty = rng.choice([30, 40, 50, 60])
    vc = rng.choice([4, 5, 6])
    decor = rng.choice([20, 25, 30])
    poster = rng.choice([10, 15])
    fc = decor + poster
    tc = qty * vc + fc
    prompt = (
        f"{person} makes {qty} smoothie cups costing R{vc} each in fruit and cups, spends R{decor} on booth decorations, "
        f"and R{poster} on cardboard posters.\n\n"
        f"Calculate {person}'s **total production and set-up cost**."
    )
    ans = f"R{tc}"
    sol = (
        f"Step 1: Total Variable Cost = {qty} * R{vc} = R{qty * vc}.\n"
        f"Step 2: Total Fixed / Set-up Costs = R{decor} + R{poster} = R{fc}.\n"
        f"Step 3: Total Cost = R{qty * vc} + R{fc} = R{tc}."
    )
    return _calc_q(
        rng, f"g7_ed_28_{rng.randint(100000, 999999)}", "28_total_cost_variable_plus_setup",
        "Total Production and Set-up Cost", prompt, ans, sol,
        {"tier_1": "Add variable costs for all units plus all fixed set-up/poster expenses.",
         "tier_2": f"({qty} * R{vc}) + R{decor} + R{poster}.",
         "tier_3": f"R{tc}"},
        ["omits_poster_and_decor_costs"]
    )


def arch_29_selling_price_target_profit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    qty = rng.choice([25, 40, 50])
    tot_cost = qty * rng.choice([3, 4, 5])
    target_profit = qty * rng.choice([4, 5, 6])
    req_income = tot_cost + target_profit
    sp = req_income // qty
    prompt = (
        f"{person} calculates it will cost R{tot_cost} in total to make {qty} fudge bags. "
        f"If {person} wants to earn exactly R{target_profit} net profit, what selling price must be charged per bag?"
    )
    ans = f"R{sp}"
    sol = (
        f"Step 1: Required Total Income = Total Cost + Desired Profit = R{tot_cost} + R{target_profit} = R{req_income}.\n"
        f"Step 2: Selling Price per bag = Total Income / Quantity = R{req_income} / {qty} = R{sp}."
    )
    return _calc_q(
        rng, f"g7_ed_29_{rng.randint(100000, 999999)}", "29_selling_price_target_profit",
        "Setting Selling Price for Target Profit", prompt, ans, sol,
        {"tier_1": "Total sales income must cover both total costs and target profit.",
         "tier_2": f"Divide (R{tot_cost} + R{target_profit}) by {qty} bags.",
         "tier_3": f"R{sp} per bag."},
        ["divides_profit_only_ignoring_cost"]
    )


def arch_30_markup_per_unit_calculation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    qty = rng.choice([20, 40, 50, 100])
    unit_cost = rng.choice([3, 4, 5, 6])
    tot_cost = qty * unit_cost
    markup = rng.choice([3, 4, 5])
    sell_p = unit_cost + markup
    prompt = (
        f"{person} spends R{tot_cost} in total to pack {qty} bags of salted peanuts and decides to sell each bag for R{sell_p}.\n\n"
        f"Calculate the **cost per bag** and the **mark-up added per bag**."
    )
    ans = f"Cost per bag = R{unit_cost}; Mark-up = R{markup}"
    sol = (
        f"Step 1: Cost per bag = Total Cost / Units = R{tot_cost} / {qty} = R{unit_cost}.\n"
        f"Step 2: Mark-up = Selling Price - Cost Price = R{sell_p} - R{unit_cost} = R{markup}."
    )
    return _calc_q(
        rng, f"g7_ed_30_{rng.randint(100000, 999999)}", "30_markup_per_unit_calculation",
        "Unit Cost and Rand Mark-up", prompt, ans, sol,
        {"tier_1": "Find the unit cost first by dividing total cost by quantity.",
         "tier_2": f"Subtract cost per bag (R{tot_cost}/{qty}) from selling price R{sell_p}.",
         "tier_3": ans},
        ["subtracts_selling_price_from_total_cost"], marks=4,
    )


def arch_31_cash_float_reconciliation(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    opening_float = rng.choice([50, 80, 100, 120])
    sales_rev = rng.choice([340, 420, 485, 560])
    closing_box = opening_float + sales_rev
    prompt = (
        f"Before opening the stall, {person} puts R{opening_float} in small coins and R10 notes into the cash tin as a **cash float** to give change. "
        f"At the end of Entrepreneur's Day, the cash tin holds R{closing_box} in total.\n\n"
        f"What was {person}'s actual **sales income** for the day?"
    )
    ans = f"R{sales_rev}"
    sol = (
        f"Step 1: Exclude opening change float:\n"
        f"Actual Sales Income = Closing Cash (R{closing_box}) - Opening Float (R{opening_float}) = R{sales_rev}."
    )
    return _calc_q(
        rng, f"g7_ed_31_{rng.randint(100000, 999999)}", "31_cash_float_reconciliation",
        "Reconciling Cash Tin with Opening Float", prompt, ans, sol,
        {"tier_1": "Remember that your starting change float was already your money, not sales.",
         "tier_2": f"Subtract R{opening_float} float from the R{closing_box} closing tin.",
         "tier_3": f"R{sales_rev}"},
        ["counts_opening_float_as_revenue"]
    )


def arch_32_multi_item_sales_revenue_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    q1, p1 = rng.choice([30, 40]), rng.choice([6, 7])
    q2, p2 = rng.choice([25, 35]), rng.choice([5, 8])
    q3, p3 = rng.choice([15, 20]), rng.choice([10, 12])
    r1, r2, r3 = q1 * p1, q2 * p2, q3 * p3
    tot = r1 + r2 + r3
    headers = ["Product Sold", "Quantity", "Selling Price (R)", "Line Income (R)"]
    rows = [
        [_given_cell("r0_c0", "Fruit kebabs"), _given_cell("r0_c1", str(q1)), _given_cell("r0_c2", str(p1)), _req_cell("r0_c3", str(r1))],
        [_given_cell("r1_c0", "Iced rooibos"), _given_cell("r1_c1", str(q2)), _given_cell("r1_c2", str(p2)), _req_cell("r1_c3", str(r2))],
        [_given_cell("r2_c0", "Caramel popcorn"), _given_cell("r2_c1", str(q3)), _given_cell("r2_c2", str(p3)), _req_cell("r2_c3", str(r3))],
        [_given_cell("r3_c0", "TOTAL SALES INCOME"), _empty_cell("r3_c1"), _empty_cell("r3_c2"), _req_cell("r3_c3", str(tot))],
    ]
    cmap = {"r0_c3": str(r1), "r1_c3": str(r2), "r2_c3": str(r3), "r3_c3": str(tot)}
    chints = {
        "r0_c3": f"Multiply {q1} * {p1}.",
        "r1_c3": f"Multiply {q2} * {p2}.",
        "r2_c3": f"Multiply {q3} * {p3}.",
        "r3_c3": "Add the three product line incomes together.",
    }
    sol = f"1. Kebabs = {q1}*R{p1} = R{r1}\n2. Tea = {q2}*R{p2} = R{r2}\n3. Popcorn = {q3}*R{p3} = R{r3}\n4. Total Income = R{tot}."
    return _ledger_q(
        f"g7_ed_32_{rng.randint(100000, 999999)}", "32_multi_item_sales_revenue_table",
        "Multi-Product Sales Income Schedule",
        f"Complete the sales income columns in the table for {person}'s stall by entering each product's revenue and the grand total (numbers only).",
        headers, rows, cmap, chints, f"Total Sales Income = R{tot}", sol,
        {"tier_1": "Multiply Quantity by Selling Price on each product row.",
         "tier_2": f"Line revenues: {q1}*{p1}, {q2}*{p2}, {q3}*{p3}; then sum down.",
         "tier_3": f"Rows: {r1}, {r2}, {r3}; Total: {tot}."},
        ["mismultiplies_price_and_quantity"], marks=4,
    )


def arch_33_multi_product_expense_ledger(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    dough, sugar = rng.choice([50, 60]), rng.choice([15, 20])
    tea, lemons = rng.choice([30, 40]), rng.choice([15, 25])
    decor, poster = rng.choice([25, 30]), rng.choice([10, 15])
    sub1, sub2, sub3 = dough + sugar, tea + lemons, decor + poster
    tot = sub1 + sub2 + sub3
    headers = ["Expense Group", "Items Bought", "Group Subtotal (R)"]
    rows = [
        [_given_cell("r0_c0", "Biscuit ingredients"), _given_cell("r0_c1", f"Dough R{dough} + Sugar R{sugar}"), _req_cell("r0_c2", str(sub1))],
        [_given_cell("r1_c0", "Iced tea ingredients"), _given_cell("r1_c1", f"Tea bags R{tea} + Lemons R{lemons}"), _req_cell("r1_c2", str(sub2))],
        [_given_cell("r2_c0", "Set-up & posters"), _given_cell("r2_c1", f"Decorations R{decor} + Paint/Card R{poster}"), _req_cell("r2_c2", str(sub3))],
        [_given_cell("r3_c0", "TOTAL EXPENDITURE"), _given_cell("r3_c1", "Sum of all costs"), _req_cell("r3_c2", str(tot))],
    ]
    cmap = {"r0_c2": str(sub1), "r1_c2": str(sub2), "r2_c2": str(sub3), "r3_c2": str(tot)}
    chints = {k: "Sum the two R amounts in column 2." for k in ("r0_c2", "r1_c2", "r2_c2")}
    chints["r3_c2"] = "Sum all three group subtotals."
    sol = f"1. Biscuits: R{dough}+R{sugar}=R{sub1}\n2. Tea: R{tea}+R{lemons}=R{sub2}\n3. Set-up: R{decor}+R{poster}=R{sub3}\n4. Total Expenditure: R{tot}."
    return _ledger_q(
        f"g7_ed_33_{rng.randint(100000, 999999)}", "33_multi_product_expense_ledger",
        "Grouping Stall Expenditure",
        f"Group and total all expenses incurred by {person} in the expenditure schedule below (enter numeric Rand totals).",
        headers, rows, cmap, chints, f"Total Expenditure = R{tot}", sol,
        {"tier_1": "Add each row's two items first, then sum the subtotal column.",
         "tier_2": f"Subtotals: {dough}+{sugar}, {tea}+{lemons}, {decor}+{poster}.",
         "tier_3": f"Subtotals: {sub1}, {sub2}, {sub3}; Total: {tot}."},
        ["omits_setup_expense_from_total"], marks=4,
    )


def arch_34_net_profit_vs_net_loss_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    exp = rng.choice([240, 280, 320])
    is_loss = rng.choice([True, False])
    delta = rng.choice([45, 75, 110])
    inc = (exp - delta) if is_loss else (exp + delta)
    res_word = "Net Loss" if is_loss else "Net Profit"
    prompt = (
        f"At closing time on Entrepreneur's Day, {person}'s records show Total Income of R{inc} and Total Expenditure of R{exp}.\n\n"
        f"Calculate the financial outcome and state clearly whether the stall made a **Net Profit** or a **Net Loss**."
    )
    ans = f"{res_word} of R{delta}"
    sol = (
        f"Step 1: Compare Income and Expenditure:\n"
        f"Total Income = R{inc}; Total Expenditure = R{exp}.\n"
        f"Step 2: Outcome = R{inc} - R{exp} = {'-' if is_loss else '+'}R{delta}, giving a {res_word} of R{delta}."
    )
    return _calc_q(
        rng, f"g7_ed_34_{rng.randint(100000, 999999)}", "34_net_profit_vs_net_loss_calc",
        "Net Profit vs Net Loss Outcome", prompt, ans, sol,
        {"tier_1": "Check whether Income > Expenditure (profit) or Expenditure > Income (loss).",
         "tier_2": f"Find the difference between R{inc} and R{exp}.",
         "tier_3": ans},
        ["confuses_profit_with_loss_polarity"]
    )


def arch_35_breakeven_unit_volume_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    sp = rng.choice([10, 12, 15])
    vc = rng.choice([4, 6, 7])
    margin = sp - vc
    be_units = rng.choice([10, 12, 15])
    fc = be_units * margin
    be_rev = be_units * sp
    max_u = be_units * 2
    max_r = max_u * sp
    svg_body = (
        f'<text x="290" y="22" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">Stall Break-Even Graph (Price R{sp}, Fixed R{fc})</text>'
        f'<line x1="65" y1="190" x2="520" y2="190" stroke="#334155" stroke-width="2"/>'
        f'<line x1="65" y1="40" x2="65" y2="190" stroke="#334155" stroke-width="2"/>'
        f'<line x1="65" y1="190" x2="500" y2="48" stroke="#16a34a" stroke-width="2.5"/>'
        f'<line x1="65" y1="150" x2="500" y2="90" stroke="#dc2626" stroke-width="2.5"/>'
        f'<circle cx="282" cy="119" r="5" fill="#1d4ed8"/>'
        f'<text x="292" y="114" font-size="11" font-weight="bold" fill="#1d4ed8">Break-Even: ({be_units} units, R{be_rev})</text>'
        f'<text x="485" y="44" font-size="10" fill="#16a34a">Income (R{max_r} @ {max_u})</text>'
        f'<text x="485" y="106" font-size="10" fill="#dc2626">Total Cost</text>'
        f'<text x="290" y="212" font-size="11" text-anchor="middle" fill="#475569">Units Sold (0 to {max_u})</text>'
    )
    prompt = (
        f"Study the break-even graph for {person}'s stall (Fixed cost R{fc}, Selling Price R{sp}, Variable cost R{vc}/unit).\n\n"
        f"How many units must {person} sell to reach **break-even** (Income = Total Cost), and what is the sales income at that point?"
    )
    ans = f"{be_units} units (R{be_rev})"
    sol = (
        f"Step 1: Verify from break-even formula & intersection point:\n"
        f"Contribution per unit = R{sp} - R{vc} = R{margin}.\n"
        f"Break-even units = Fixed Cost / Contribution = R{fc} / R{margin} = {be_units} units.\n"
        f"Break-even income = {be_units} * R{sp} = R{be_rev}."
    )
    return _calc_q(
        rng, f"g7_ed_35_{rng.randint(100000, 999999)}", "35_breakeven_unit_volume_svg",
        "Reading and Calculating Break-Even Point", prompt, ans, sol,
        {"tier_1": "Locate where the Income and Total Cost lines intersect on the graph.",
         "tier_2": f"Each item adds R{sp}-R{vc}=R{margin} toward the R{fc} fixed cost.",
         "tier_3": ans},
        ["ignores_variable_cost_in_breakeven"],
        diagram_spec=_svg_spec(svg_body, 580, 225),
    )


def arch_36_unsold_perishable_stock_profit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    made = rng.choice([50, 60])
    unsold = rng.choice([8, 10, 12])
    sold = made - unsold
    cost_u = rng.choice([4, 5])
    sell_p = rng.choice([8, 10])
    tot_cost = made * cost_u
    tot_rev = sold * sell_p
    profit = tot_rev - tot_cost
    prompt = (
        f"{person} bakes {made} scones at a total production cost of R{tot_cost} (R{cost_u} each) and prices them at R{sell_p} each. "
        f"By the end of Entrepreneur's Day, {unsold} scones remain unsold and spoil.\n\n"
        f"Calculate {person}'s **actual net profit** accounting for the unsold spoilage."
    )
    ans = f"R{profit}"
    sol = (
        f"Step 1: Units sold = {made} - {unsold} = {sold} scones.\n"
        f"Step 2: Sales Income = {sold} * R{sell_p} = R{tot_rev}.\n"
        f"Step 3: Total Cost remains R{tot_cost} because all {made} scones were baked.\n"
        f"Step 4: Actual Net Profit = R{tot_rev} - R{tot_cost} = R{profit}."
    )
    return _calc_q(
        rng, f"g7_ed_36_{rng.randint(100000, 999999)}", "36_unsold_perishable_stock_profit",
        "Unsold Perishable Stock Impact", prompt, ans, sol,
        {"tier_1": "You still paid for making all units even though some went unsold!",
         "tier_2": f"Income = ({made}-{unsold}) * R{sell_p} = R{tot_rev}; Cost = R{tot_cost}.",
         "tier_3": f"R{profit}"},
        ["excludes_cost_of_unsold_stock"]
    )


def arch_37_clearance_discount_revenue(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    full_qty = rng.choice([30, 40])
    disc_qty = rng.choice([10, 12])
    full_p = rng.choice([10, 12, 14])
    disc_p = full_p // 2
    rev = full_qty * full_p + disc_qty * disc_p
    prompt = (
        f"{person} sells {full_qty} bags of vetkoek at the full price of R{full_p} each. In the final 20 minutes, "
        f"{person} discounts the last {disc_qty} bags to half price (R{disc_p} each) to avoid waste, and sells them all.\n\n"
        f"Calculate total **sales income** for the day."
    )
    ans = f"R{rev}"
    sol = (
        f"Step 1: Full-price sales = {full_qty} * R{full_p} = R{full_qty * full_p}.\n"
        f"Step 2: Clearance sales = {disc_qty} * R{disc_p} = R{disc_qty * disc_p}.\n"
        f"Step 3: Total Sales Income = R{full_qty * full_p} + R{disc_qty * disc_p} = R{rev}."
    )
    return _calc_q(
        rng, f"g7_ed_37_{rng.randint(100000, 999999)}", "37_clearance_discount_revenue",
        "End-of-Day Clearance Discount Revenue", prompt, ans, sol,
        {"tier_1": "Calculate full-price revenue and discounted revenue separately, then add.",
         "tier_2": f"{full_qty}*R{full_p} + {disc_qty}*R{disc_p}.",
         "tier_3": f"R{rev}"},
        ["applies_discount_to_entire_batch"]
    )


def arch_38_income_expenditure_statement_purpose(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    n_partners = rng.choice([2, 3, 4])
    prompt = (
        f"After finishing sales on Entrepreneur's Day in {area}, {person}'s team of {n_partners} learners must draw up an "
        f"**Income and Expenditure Statement**.\n\n"
        f"Give THREE clear reasons why finalising this statement is essential. (3 marks)"
    )
    sample = (
        f"1. To finalise financial records and confirm total income received against total expenses paid.\n"
        f"2. To verify accurately whether the stall achieved a net profit or incurred a net loss.\n"
        f"3. To calculate fair equal profit shares among the {n_partners} group members (or repay loans)."
    )
    pts = [
        "Finalises financial records by matching total cash income and expenses [1 mark]",
        "Determines objectively whether a net profit or net loss was made [1 mark]",
        f"Enables equal sharing of profit among the {n_partners} team members [1 mark]",
    ]
    sol = "Marking Rubric (3 marks):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_ed_38_{rng.randint(100000, 999999)}", "38_income_expenditure_statement_purpose",
        "Purpose of Income and Expenditure Statement", prompt, sample, pts, sol,
        {"tier_1": "Think about checking results and splitting earnings fairly in a group.",
         "tier_2": "Covers financial closure, profit/loss calculation, and fair team division.",
         "tier_3": sample},
        ["thinks_statement_is_only_teacher_formality"], marks=3,
    )


def arch_39_side_by_side_income_expenditure_statement(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    q_s, p_s = rng.choice([40, 50]), rng.choice([8, 10])
    q_d, p_d = rng.choice([30, 35]), rng.choice([6, 8])
    inc1, inc2 = q_s * p_s, q_d * p_d
    tot_inc = inc1 + inc2
    mat1 = rng.choice([120, 140])
    mat2 = rng.choice([70, 90])
    setup = rng.choice([35, 45])
    tot_exp = mat1 + mat2 + setup
    net_prof = tot_inc - tot_exp
    headers = ["Income", "Amount (R)", "Expenditure", "Amount (R)"]
    rows = [
        [_given_cell("r0_c0", f"Snack packs ({q_s} * R{p_s})"), _req_cell("r0_c1", str(inc1)), _given_cell("r0_c2", "Snack ingredients"), _given_cell("r0_c3", str(mat1))],
        [_given_cell("r1_c0", f"Drinks ({q_d} * R{p_d})"), _req_cell("r1_c1", str(inc2)), _given_cell("r1_c2", "Drink supplies"), _given_cell("r1_c3", str(mat2))],
        [_empty_cell("r2_c0"), _empty_cell("r2_c1"), _given_cell("r2_c2", "Decor & stall fee"), _given_cell("r2_c3", str(setup))],
        [_given_cell("r3_c0", "Total income"), _req_cell("r3_c1", str(tot_inc)), _given_cell("r3_c2", "Total expenditure"), _req_cell("r3_c3", str(tot_exp))],
        [_given_cell("r4_c0", "Net profit (Income - Expenditure)"), _req_cell("r4_c1", str(net_prof)), _empty_cell("r4_c2"), _empty_cell("r4_c3")],
    ]
    cmap = {"r0_c1": str(inc1), "r1_c1": str(inc2), "r3_c1": str(tot_inc), "r3_c3": str(tot_exp), "r4_c1": str(net_prof)}
    chints = {
        "r0_c1": f"{q_s} * {p_s}", "r1_c1": f"{q_d} * {p_d}",
        "r3_c1": "Sum both Income lines.", "r3_c3": "Sum all three Expenditure lines.",
        "r4_c1": "Total income minus Total expenditure.",
    }
    sol = f"1. Snacks: {q_s}*R{p_s}=R{inc1}; Drinks: {q_d}*R{p_d}=R{inc2}; Total Income=R{tot_inc}.\n2. Total Expenditure=R{mat1}+R{mat2}+R{setup}=R{tot_exp}.\n3. Net Profit=R{tot_inc}-R{tot_exp}=R{net_prof}."
    return _ledger_q(
        f"g7_ed_39_{rng.randint(100000, 999999)}", "39_side_by_side_income_expenditure_statement",
        "Side-by-Side Income and Expenditure Statement",
        f"Complete the side-by-side Income and Expenditure Statement for {person}'s Entrepreneur's Day stall (enter numbers only).",
        headers, rows, cmap, chints, f"Total Income = R{tot_inc}; Total Expenditure = R{tot_exp}; Net Profit = R{net_prof}", sol,
        {"tier_1": "Compute each sales income line first, then total both sides.",
         "tier_2": f"Income = R{inc1} + R{inc2}. Expenses = R{mat1} + R{mat2} + R{setup}.",
         "tier_3": f"Total Income {tot_inc}; Total Exp {tot_exp}; Net Profit {net_prof}."},
        ["places_profit_before_totaling_columns"], marks=10,
    )


def arch_40_themed_snack_stand_income_expenditure(rng: random.Random) -> Dict[str, Any]:
    # Grounded directly in Doc Q6: "Eat It!" insect-themed stand
    n1, n2 = rng.sample(NAMES, 2)
    bisc_qty, bisc_p = rng.choice([40, 50]), rng.choice([7, 8])
    tea_qty, tea_p = rng.choice([30, 40]), rng.choice([5, 6])
    snake_qty, snake_p = rng.choice([20, 25]), rng.choice([8, 9])
    inc_b, inc_t, inc_s = bisc_qty * bisc_p, tea_qty * tea_p, snake_qty * snake_p
    tot_inc = inc_b + inc_t + inc_s
    mat_b = rng.choice([85, 95])
    mat_t = rng.choice([75, 85])
    mat_s = rng.choice([50, 60])
    setup = rng.choice([40, 50])
    tot_exp = mat_b + mat_t + mat_s + setup
    profit = tot_inc - tot_exp
    headers = ["Income", "R", "Expenditure", "R"]
    rows = [
        [_given_cell("r0_c0", f"Spider biscuits ({bisc_qty}*R{bisc_p})"), _req_cell("r0_c1", str(inc_b)), _given_cell("r0_c2", "Biscuit dough, sugar, colour"), _given_cell("r0_c3", str(mat_b))],
        [_given_cell("r1_c0", f"Beetle tea ({tea_qty}*R{tea_p})"), _req_cell("r1_c1", str(inc_t)), _given_cell("r1_c2", "Rooibos, sugar, sweets"), _given_cell("r1_c3", str(mat_t))],
        [_given_cell("r2_c0", f"Sausage snakes ({snake_qty}*R{snake_p})"), _req_cell("r2_c1", str(inc_s)), _given_cell("r2_c2", "Sausages, peppercorns, cucumber"), _given_cell("r2_c3", str(mat_s))],
        [_empty_cell("r3_c0"), _empty_cell("r3_c1"), _given_cell("r3_c2", "Set-up & poster paint"), _given_cell("r3_c3", str(setup))],
        [_given_cell("r4_c0", "Total income"), _req_cell("r4_c1", str(tot_inc)), _given_cell("r4_c2", "Total expenditure"), _req_cell("r4_c3", str(tot_exp))],
        [_given_cell("r5_c0", "Net profit"), _req_cell("r5_c1", str(profit)), _empty_cell("r5_c2"), _empty_cell("r5_c3")],
    ]
    cmap = {"r0_c1": str(inc_b), "r1_c1": str(inc_t), "r2_c1": str(inc_s), "r4_c1": str(tot_inc), "r4_c3": str(tot_exp), "r5_c1": str(profit)}
    chints = {
        "r0_c1": f"{bisc_qty} * {bisc_p}", "r1_c1": f"{tea_qty} * {tea_p}", "r2_c1": f"{snake_qty} * {snake_p}",
        "r4_c1": "Sum rows 1-3 Income.", "r4_c3": "Sum all 4 Expenditure rows.", "r5_c1": "Total income - Total expenditure.",
    }
    sol = f"1. Income lines: R{inc_b} + R{inc_t} + R{inc_s} = R{tot_inc}.\n2. Expenditure lines: R{mat_b} + R{mat_t} + R{mat_s} + R{setup} = R{tot_exp}.\n3. Net profit: R{tot_inc} - R{tot_exp} = R{profit}."
    return _ledger_q(
        f"g7_ed_40_{rng.randint(100000, 999999)}", "40_themed_snack_stand_income_expenditure",
        "Eat It! Stand Income and Expenditure Statement",
        f"{n1} and {n2} run the 'Eat It!' insect-themed stand selling everything made on Entrepreneur's Day. Complete all missing amounts in their Income and Expenditure Statement.",
        headers, rows, cmap, chints, f"Total Income = R{tot_inc}; Total Expenditure = R{tot_exp}; Net Profit = R{profit}", sol,
        {"tier_1": "Calculate each product line's sales revenue before summing totals.",
         "tier_2": f"Expenses include biscuits (R{mat_b}), tea (R{mat_t}), snakes (R{mat_s}), and set-up (R{setup}).",
         "tier_3": f"Total Inc: {tot_inc}; Total Exp: {tot_exp}; Net Profit: {profit}."},
        ["omits_setup_or_decoration_cost"], marks=12,
    )


def arch_41_budget_vs_actual_variance_statement(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    b_inc, a_inc = rng.choice([400, 450]), rng.choice([460, 520])
    b_exp, a_exp = rng.choice([180, 200]), rng.choice([210, 230])
    inc_var = a_inc - b_inc
    exp_var = a_exp - b_exp
    b_prof = b_inc - b_exp
    a_prof = a_inc - a_exp
    headers = ["Line Item", "Budgeted (R)", "Actual (R)", "Difference (Actual - Budget)"]
    rows = [
        [_given_cell("r0_c0", "Sales Income"), _given_cell("r0_c1", str(b_inc)), _given_cell("r0_c2", str(a_inc)), _req_cell("r0_c3", str(inc_var))],
        [_given_cell("r1_c0", "Total Expenditure"), _given_cell("r1_c1", str(b_exp)), _given_cell("r1_c2", str(a_exp)), _req_cell("r1_c3", str(exp_var))],
        [_given_cell("r2_c0", "Net Profit"), _given_cell("r2_c1", str(b_prof)), _req_cell("r2_c2", str(a_prof)), _empty_cell("r2_c3")],
    ]
    cmap = {"r0_c3": str(inc_var), "r1_c3": str(exp_var), "r2_c2": str(a_prof)}
    chints = {"r0_c3": f"{a_inc} - {b_inc}", "r1_c3": f"{a_exp} - {b_exp}", "r2_c2": f"{a_inc} - {a_exp}"}
    sol = f"1. Income variance = R{a_inc}-R{b_inc}=R{inc_var} (higher sales).\n2. Expense variance = R{a_exp}-R{b_exp}=R{exp_var} (overspend).\n3. Actual Net Profit = R{a_inc}-R{a_exp}=R{a_prof}."
    return _ledger_q(
        f"g7_ed_41_{rng.randint(100000, 999999)}", "41_budget_vs_actual_variance_statement",
        "Budget vs Actual Variance Table",
        f"Compare {person}'s pre-event budget against actual Entrepreneur's Day results in the variance table (enter positive integer differences).",
        headers, rows, cmap, chints, f"Income Diff = R{inc_var}; Exp Diff = R{exp_var}; Actual Profit = R{a_prof}", sol,
        {"tier_1": "Subtract Budgeted from Actual in rows 1 and 2.",
         "tier_2": "Row 3 asks for Actual Net Profit = Actual Sales - Actual Expenditure.",
         "tier_3": f"Income Diff: {inc_var}; Exp Diff: {exp_var}; Actual Profit: {a_prof}."},
        ["confuses_budgeted_with_actual_columns"], marks=6,
    )


def arch_42_monthly_recurring_stall_profit(rng: random.Random) -> Dict[str, Any]:
    # Grounded in Exam2 Q6: 4 Entrepreneur's Days per month with weekly stall rent
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    weekly_qty = rng.choice([25, 30, 40])
    sp = rng.choice([10, 12])
    vc = rng.choice([5, 6])
    rent_per_day = rng.choice([10, 15, 20])
    days = 4
    m_inc = weekly_qty * sp * days
    m_ing = weekly_qty * vc * days
    m_rent = rent_per_day * days
    m_prof = m_inc - m_ing - m_rent
    headers = ["Monthly Line (4 Days)", "Calculation Basis", "Amount (R)"]
    rows = [
        [_given_cell("r0_c0", "Monthly Sales Income"), _given_cell("r0_c1", f"{days} days * {weekly_qty} units * R{sp}"), _req_cell("r0_c2", str(m_inc))],
        [_given_cell("r1_c0", "Monthly Ingredients Cost"), _given_cell("r1_c1", f"{days} days * {weekly_qty} units * R{vc}"), _req_cell("r1_c2", str(m_ing))],
        [_given_cell("r2_c0", "Monthly Stall Rental"), _given_cell("r2_c1", f"{days} days * R{rent_per_day}"), _req_cell("r2_c2", str(m_rent))],
        [_given_cell("r3_c0", "Monthly Net Profit"), _given_cell("r3_c1", "Income - Ingredients - Rent"), _req_cell("r3_c2", str(m_prof))],
    ]
    cmap = {"r0_c2": str(m_inc), "r1_c2": str(m_ing), "r2_c2": str(m_rent), "r3_c2": str(m_prof)}
    chints = {"r0_c2": f"{days*weekly_qty}*{sp}", "r1_c2": f"{days*weekly_qty}*{vc}", "r2_c2": f"{days}*{rent_per_day}", "r3_c2": "Row1 - Row2 - Row3"}
    sol = f"1. Income={m_inc}\n2. Ingredients={m_ing}\n3. Rent={m_rent}\n4. Monthly Net Profit={m_inc}-{m_ing}-{m_rent}=R{m_prof}."
    return _ledger_q(
        f"g7_ed_42_{rng.randint(100000, 999999)}", "42_monthly_recurring_stall_profit",
        "Monthly Multi-Day Stall Summary",
        f"{person}'s school hosts {days} Entrepreneur's Days per month, paying R{rent_per_day} stall rent each time. Complete the monthly summary table.",
        headers, rows, cmap, chints, f"Monthly Profit = R{m_prof}", sol,
        {"tier_1": f"Remember to multiply every weekly figure by {days} events.",
         "tier_2": "Include both variable ingredients AND fixed stall rent before calculating profit.",
         "tier_3": f"Inc: {m_inc}; Ing: {m_ing}; Rent: {m_rent}; Net Profit: {m_prof}."},
        ["forgets_multiplying_stall_rent_by_4"], marks=8,
    )


def arch_43_equal_profit_sharing_partners(rng: random.Random) -> Dict[str, Any]:
    n_members = rng.choice([2, 3, 4])
    names = ", ".join(rng.sample(NAMES, n_members))
    share = rng.choice([75, 95, 110, 140])
    net_profit = n_members * share
    tot_inc = net_profit + rng.choice([180, 220])
    tot_exp = tot_inc - net_profit
    prompt = (
        f"At the end of Entrepreneur's Day, {n_members} partners ({names}) recorded R{tot_inc} in Total Income "
        f"and R{tot_exp} in Total Expenditure (including all loans repaid).\n\n"
        f"How much money does **each partner** receive when the net profit is shared equally?"
    )
    ans = f"R{share}"
    sol = (
        f"Step 1: Net Profit = R{tot_inc} - R{tot_exp} = R{net_profit}.\n"
        f"Step 2: Equal Share per partner = R{net_profit} / {n_members} = R{share}."
    )
    return _calc_q(
        rng, f"g7_ed_43_{rng.randint(100000, 999999)}", "43_equal_profit_sharing_partners",
        "Sharing Net Profit Equally Among Partners", prompt, ans, sol,
        {"tier_1": "First find Net Profit, not Total Income!",
         "tier_2": f"Net Profit = R{tot_inc} - R{tot_exp}; then divide equally by {n_members}.",
         "tier_3": f"R{share} each."},
        ["splits_gross_revenue_before_deducting_expenses"]
    )


def arch_44_profit_reinvestment_and_charity(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    net_prof = rng.choice([200, 300, 400, 500])
    charity_pct = rng.choice([10, 20])
    reinvest_pct = rng.choice([30, 40])
    charity_amt = net_prof * charity_pct // 100
    reinvest_amt = net_prof * reinvest_pct // 100
    personal_amt = net_prof - charity_amt - reinvest_amt
    prompt = (
        f"{person}'s stand finishes with R{net_prof} Net Profit. The team decides to donate {charity_pct}% to the school feeding scheme, "
        f"reinvest {reinvest_pct}% into next term's stock, and take the rest as personal reward.\n\n"
        f"How many Rand remain for personal reward?"
    )
    ans = f"R{personal_amt}"
    sol = (
        f"Step 1: School feeding donation ({charity_pct}%) = R{charity_amt}.\n"
        f"Step 2: Reinvested into business ({reinvest_pct}%) = R{reinvest_amt}.\n"
        f"Step 3: Remaining personal reward = R{net_prof} - R{charity_amt} - R{reinvest_amt} = R{personal_amt}."
    )
    return _calc_q(
        rng, f"g7_ed_44_{rng.randint(100000, 999999)}", "44_profit_reinvestment_and_charity",
        "Allocating Entrepreneur's Day Profit", prompt, ans, sol,
        {"tier_1": f"Find {charity_pct}% and {reinvest_pct}% of R{net_prof} first.",
         "tier_2": f"Remaining percentage = {100 - charity_pct - reinvest_pct}%.",
         "tier_3": f"R{personal_amt}"},
        ["miscalculates_remaining_percentage"]
    )


def arch_45_interpreting_stall_comparison_bar_chart_svg(rng: random.Random) -> Dict[str, Any]:
    n1, n2, n3 = rng.sample(NAMES, 3)
    i1, e1 = rng.choice([360, 400]), rng.choice([140, 160])
    i2, e2 = rng.choice([300, 320]), rng.choice([210, 240])
    i3, e3 = rng.choice([280, 310]), rng.choice([80, 95])
    p1, p2, p3 = i1 - e1, i2 - e2, i3 - e3
    profits = [(n1, p1), (n2, p2), (n3, p3)]
    best_name, best_p = max(profits, key=lambda x: x[1])
    svg_body = (
        f'<text x="290" y="22" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">Stall Performance: Income (Green) vs Expenditure (Red)</text>'
        f'<rect x="70" y="{190 - i1//3}" width="38" height="{i1//3}" fill="#16a34a"/>'
        f'<rect x="112" y="{190 - e1//3}" width="38" height="{e1//3}" fill="#ef4444"/>'
        f'<text x="89" y="{184 - i1//3}" font-size="10" text-anchor="middle" fill="#14532d">R{i1}</text>'
        f'<text x="131" y="{184 - e1//3}" font-size="10" text-anchor="middle" fill="#7f1d1d">R{e1}</text>'
        f'<text x="110" y="208" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{n1}</text>'
        f'<rect x="240" y="{190 - i2//3}" width="38" height="{i2//3}" fill="#16a34a"/>'
        f'<rect x="282" y="{190 - e2//3}" width="38" height="{e2//3}" fill="#ef4444"/>'
        f'<text x="259" y="{184 - i2//3}" font-size="10" text-anchor="middle" fill="#14532d">R{i2}</text>'
        f'<text x="301" y="{184 - e2//3}" font-size="10" text-anchor="middle" fill="#7f1d1d">R{e2}</text>'
        f'<text x="280" y="208" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{n2}</text>'
        f'<rect x="410" y="{190 - i3//3}" width="38" height="{i3//3}" fill="#16a34a"/>'
        f'<rect x="452" y="{190 - e3//3}" width="38" height="{e3//3}" fill="#ef4444"/>'
        f'<text x="429" y="{184 - i3//3}" font-size="10" text-anchor="middle" fill="#14532d">R{i3}</text>'
        f'<text x="471" y="{184 - e3//3}" font-size="10" text-anchor="middle" fill="#7f1d1d">R{e3}</text>'
        f'<text x="450" y="208" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">{n3}</text>'
    )
    prompt = (
        f"Study the comparison chart displaying Income and Expenditure for three Grade 7 stalls ({n1}, {n2}, and {n3}).\n\n"
        f"Which stall achieved the highest **net profit**, and how much was it?"
    )
    ans = f"{best_name} with R{best_p}"
    sol = (
        f"Step 1: Calculate net profit for each stall:\n"
        f"- {n1}: R{i1} - R{e1} = R{p1}\n"
        f"- {n2}: R{i2} - R{e2} = R{p2}\n"
        f"- {n3}: R{i3} - R{e3} = R{p3}\n"
        f"Step 2: Highest net profit is {ans}."
    )
    return _calc_q(
        rng, f"g7_ed_45_{rng.randint(100000, 999999)}", "45_interpreting_stall_comparison_bar_chart_svg",
        "Analysing Stall Profit Bar Chart", prompt, ans, sol,
        {"tier_1": "Highest Income does not always mean highest Profit! Check Expenditure too.",
         "tier_2": f"Subtract red bar (Expenditure) from green bar (Income) for {n1}, {n2}, and {n3}.",
         "tier_3": ans},
        ["picks_highest_revenue_instead_of_profit"],
        diagram_spec=_svg_spec(svg_body, 580, 225),
    )


def arch_46_troubleshooting_low_sales_four_ps(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    flaw = rng.choice([
        ("placed their stand behind an empty bicycle shed, made no posters, and charged R25 per mini muffin", "Place & Promotion & Price"),
        ("hung posters with no prices or booth location, and ran out of small coins for change", "Promotion & Cash Operations"),
    ])
    desc, tag = flaw
    prompt = (
        f"At Entrepreneur's Day in {area}, {person}'s team {desc}, resulting in almost zero sales. "
        f"Diagnose TWO marketing mistakes made and propose one practical fix for each. (4 marks)"
    )
    sample = (
        "1. Poor visibility/communication: Buyers could not find the stall or verify pricing -> Fix: move to high-traffic quad and put clear price + location signs.\n"
        "2. Price/change mismatch: High price or missing coin float blocked small purchases -> Fix: price within learners' pocket money and keep R1/R2/R5 change ready."
    )
    pts = [
        f"Identifies two distinct marketing or operational flaws ({tag}) [2 marks]",
        "Provides actionable fix aligned with the 4 Ps (Place, Promotion, Price, Product) [2 marks]",
    ]
    sol = f"Marking Rubric (4 marks):\n- {pts[0]}\n- {pts[1]}"
    return _rubric_q(
        f"g7_ed_46_{rng.randint(100000, 999999)}", "46_troubleshooting_low_sales_four_ps",
        "Troubleshooting Weak Stall Sales", prompt, sample, pts, sol,
        {"tier_1": "Review Product, Price, Place, and Promotion against the mistakes listed.",
         "tier_2": "Match each problem to a specific P and give a realistic school solution.",
         "tier_3": sample},
        ["gives_vague_marketing_advice"]
    )


def arch_47_rural_vs_urban_school_context_adaptation(rng: random.Random) -> Dict[str, Any]:
    rural = rng.choice(RURAL_AREAS)
    urban = rng.choice(URBAN_AREAS)
    person = rng.choice(["Luyanda", "Karabo", "Thabo", "Naledi"])
    prompt = (
        f"Entrepreneur's Day projects must adapt to local context: compare {person}'s school in {rural} versus a school in {urban}.\n\n"
        f"Which decision shows context-aware Entrepreneur's Day adaptation?"
    )
    correct = f"Sourcing locally grown ingredients and affordable R2-R5 portions in {rural}, while matching higher supplier access and competition in {urban}"
    distractors = [
        f"Copying identical R60 imported smoothies regardless of whether buyers live in {rural} or {urban}",
        "Banning agricultural or recycled homemade goods at schools outside city centres",
        "Closing all school markets unless learners have fast fibre Wi-Fi connections",
    ]
    sol = (
        f"Step 1: Context adaptation rule:\n"
        f"Rural ({rural}) vs urban ({urban}) schools differ in household disposable pocket money, ingredient access, and transport. "
        f"Entrepreneurs succeed by matching local buying power and accessible inputs."
    )
    return _mcq_q(
        rng, f"g7_ed_47_{rng.randint(100000, 999999)}", "47_rural_vs_urban_school_context_adaptation",
        "Rural and Urban Market Adaptation", prompt, correct, distractors, sol,
        {"tier_1": "Consider how household budgets and local supply chains differ across SA.",
         "tier_2": "Successful micro-ventures tailor portion prices and inputs to local community realities.",
         "tier_3": correct},
        ["ignores_local_socioeconomic_context"]
    )


def arch_48_cash_handling_change_error_check(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    sold_qty = rng.choice([25, 30, 35])
    unit_p = rng.choice([8, 10])
    expected_cash = sold_qty * unit_p
    shortage = rng.choice([12, 18, 24])
    actual_cash = expected_cash - shortage
    prompt = (
        f"{person}'s tally sheet shows {sold_qty} ice lollies sold at R{unit_p} each, so R{expected_cash} in sales cash was expected. "
        f"However, counting the tin (excluding the float) yields only R{actual_cash}.\n\n"
        f"Calculate the **cash shortage**, and name one cause during busy rush sales."
    )
    ans = f"R{shortage} shortage (e.g. giving too much change or unrecorded cash theft/loss)"
    sol = (
        f"Step 1: Cash discrepancy = Expected Sales (R{expected_cash}) - Actual Cash Counted (R{actual_cash}) = R{shortage}.\n"
        f"Step 2: Common cause = rush-hour change errors or unpaid items handed over before collecting coins."
    )
    return _calc_q(
        rng, f"g7_ed_48_{rng.randint(100000, 999999)}", "48_cash_handling_change_error_check",
        "Cash Control and Change Shortage", prompt, ans, sol,
        {"tier_1": "Compare recorded sales value with actual counted cash.",
         "tier_2": f"Shortage = ({sold_qty} * R{unit_p}) - R{actual_cash}.",
         "tier_3": ans},
        ["ignores_cash_control_shortage"], marks=3,
    )


def arch_49_post_event_feedback_iteration(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    stock_left = rng.choice([14, 18, 22])
    prompt = (
        f"Reviewing post-event records, {person} notices {stock_left} large cupcakes remained unsold, whereas small R5 cup juices sold out in 15 minutes.\n\n"
        f"What smart business adjustment should {person} apply at the next school market?"
    )
    correct = "Bake fewer cupcakes or shrink size to lower price, and scale up stock of fast-selling R5 cup juices"
    distractors = [
        "Double cupcake production next time even though buyers found them slow-selling",
        "Stop selling R5 cup juices altogether because selling out early is bad",
        "Throw away the Income and Expenditure Statement so nobody sees leftover stock",
    ]
    sol = (
        f"Step 1: Data-driven iteration:\n"
        f"Leftover inventory ({stock_left} units) signals excess supply or high unit price, while rapid sell-out on juices "
        f"reveals unmet demand. Reallocate capital toward higher-demand items."
    )
    return _mcq_q(
        rng, f"g7_ed_49_{rng.randint(100000, 999999)}", "49_post_event_feedback_iteration",
        "Using Sales Results to Improve", prompt, correct, distractors, sol,
        {"tier_1": "Look at which product had excess leftover supply vs excess demand.",
         "tier_2": "Shift resources away from slow leftovers toward fast-selling items.",
         "tier_3": correct},
        ["repeats_unprofitable_stock_mix"]
    )


def arch_50_comprehensive_entrepreneurs_day_synthesis(rng: random.Random) -> Dict[str, Any]:
    n1, n2 = rng.sample(NAMES, 2)
    q1, p1 = rng.choice([40, 50]), rng.choice([10, 12])
    q2, p2 = rng.choice([30, 40]), rng.choice([6, 8])
    rev1, rev2 = q1 * p1, q2 * p2
    tot_rev = rev1 + rev2
    ing_cost = rng.choice([210, 240, 260])
    poster_cost = rng.choice([20, 25])
    stall_fee = rng.choice([30, 40])
    tot_exp = ing_cost + poster_cost + stall_fee
    net_prof = tot_rev - tot_exp
    each_share = net_prof // 2 if net_prof % 2 == 0 else (net_prof - 1) // 2
    if net_prof % 2 != 0:
        stall_fee += 1
        tot_exp += 1
        net_prof -= 1
        each_share = net_prof // 2
    headers = ["Statement Line", "Category", "Amount (R)"]
    rows = [
        [_given_cell("r0_c0", f"Boerewors rolls ({q1} @ R{p1})"), _given_cell("r0_c1", "Income"), _req_cell("r0_c2", str(rev1))],
        [_given_cell("r1_c0", f"Cold drinks ({q2} @ R{p2})"), _given_cell("r1_c1", "Income"), _req_cell("r1_c2", str(rev2))],
        [_given_cell("r2_c0", "TOTAL INCOME"), _given_cell("r2_c1", "Subtotal"), _req_cell("r2_c2", str(tot_rev))],
        [_given_cell("r3_c0", "Meat, rolls & drinks stock"), _given_cell("r3_c1", "Variable Expense"), _given_cell("r3_c2", str(ing_cost))],
        [_given_cell("r4_c0", "Posters & school stall fee"), _given_cell("r4_c1", "Fixed Set-up"), _given_cell("r4_c2", str(poster_cost + stall_fee))],
        [_given_cell("r5_c0", "TOTAL EXPENDITURE"), _given_cell("r5_c1", "Subtotal"), _req_cell("r5_c2", str(tot_exp))],
        [_given_cell("r6_c0", "NET PROFIT"), _given_cell("r6_c1", "Income - Expenditure"), _req_cell("r6_c2", str(net_prof))],
        [_given_cell("r7_c0", "Equal Profit Share (per partner)"), _given_cell("r7_c1", "Divided by 2"), _req_cell("r7_c2", str(each_share))],
    ]
    cmap = {
        "r0_c2": str(rev1), "r1_c2": str(rev2), "r2_c2": str(tot_rev),
        "r5_c2": str(tot_exp), "r6_c2": str(net_prof), "r7_c2": str(each_share),
    }
    chints = {
        "r0_c2": f"{q1}*{p1}", "r1_c2": f"{q2}*{p2}", "r2_c2": "Add both Income rows.",
        "r5_c2": "Add Variable + Fixed expenses.", "r6_c2": "Total Income - Total Expenditure.",
        "r7_c2": "Divide Net Profit equally between 2 partners.",
    }
    sol = (
        f"1. Rolls: {q1}*R{p1}=R{rev1}; Drinks: {q2}*R{p2}=R{rev2}; Total Income = R{tot_rev}.\n"
        f"2. Total Expenditure = R{ing_cost} + R{poster_cost + stall_fee} = R{tot_exp}.\n"
        f"3. Net Profit = R{tot_rev} - R{tot_exp} = R{net_prof}.\n"
        f"4. Equal partner share ({n1} & {n2}) = R{net_prof}/2 = R{each_share}."
    )
    return _ledger_q(
        f"g7_ed_50_{rng.randint(100000, 999999)}", "50_comprehensive_entrepreneurs_day_synthesis",
        "Capstone Entrepreneur's Day Statement & Profit Split",
        f"Partners {n1} and {n2} wrap up Entrepreneur's Day. Complete their Income and Expenditure Statement and calculate each partner's equal share (enter whole Rand figures).",
        headers, rows, cmap, chints, f"Total Income = R{tot_rev}; Net Profit = R{net_prof}; Each Partner = R{each_share}", sol,
        {"tier_1": "Work row by row: sales lines -> total income -> total expenses -> profit -> partner split.",
         "tier_2": f"Set-up = R{poster_cost}+{stall_fee}. Divide Net Profit by 2 at the bottom.",
         "tier_3": f"Inc {tot_rev}, Exp {tot_exp}, Profit {net_prof}, Share {each_share}."},
        ["omits_partner_division_or_setup_fee"], marks=12,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_variable_vs_fixed_stall_costs": arch_26_variable_vs_fixed_stall_costs,
    "27_per_unit_ingredient_costing_table": arch_27_per_unit_ingredient_costing_table,
    "28_total_cost_variable_plus_setup": arch_28_total_cost_variable_plus_setup,
    "29_selling_price_target_profit": arch_29_selling_price_target_profit,
    "30_markup_per_unit_calculation": arch_30_markup_per_unit_calculation,
    "31_cash_float_reconciliation": arch_31_cash_float_reconciliation,
    "32_multi_item_sales_revenue_table": arch_32_multi_item_sales_revenue_table,
    "33_multi_product_expense_ledger": arch_33_multi_product_expense_ledger,
    "34_net_profit_vs_net_loss_calc": arch_34_net_profit_vs_net_loss_calc,
    "35_breakeven_unit_volume_svg": arch_35_breakeven_unit_volume_svg,
    "36_unsold_perishable_stock_profit": arch_36_unsold_perishable_stock_profit,
    "37_clearance_discount_revenue": arch_37_clearance_discount_revenue,
    "38_income_expenditure_statement_purpose": arch_38_income_expenditure_statement_purpose,
    "39_side_by_side_income_expenditure_statement": arch_39_side_by_side_income_expenditure_statement,
    "40_themed_snack_stand_income_expenditure": arch_40_themed_snack_stand_income_expenditure,
    "41_budget_vs_actual_variance_statement": arch_41_budget_vs_actual_variance_statement,
    "42_monthly_recurring_stall_profit": arch_42_monthly_recurring_stall_profit,
    "43_equal_profit_sharing_partners": arch_43_equal_profit_sharing_partners,
    "44_profit_reinvestment_and_charity": arch_44_profit_reinvestment_and_charity,
    "45_interpreting_stall_comparison_bar_chart_svg": arch_45_interpreting_stall_comparison_bar_chart_svg,
    "46_troubleshooting_low_sales_four_ps": arch_46_troubleshooting_low_sales_four_ps,
    "47_rural_vs_urban_school_context_adaptation": arch_47_rural_vs_urban_school_context_adaptation,
    "48_cash_handling_change_error_check": arch_48_cash_handling_change_error_check,
    "49_post_event_feedback_iteration": arch_49_post_event_feedback_iteration,
    "50_comprehensive_entrepreneurs_day_synthesis": arch_50_comprehensive_entrepreneurs_day_synthesis,
}
