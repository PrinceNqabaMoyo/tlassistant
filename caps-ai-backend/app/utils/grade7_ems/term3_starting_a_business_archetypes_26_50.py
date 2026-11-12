"""Grade 7 EMS: Term 3 - Starting a Business Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/03. Starting a business.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List
from app.utils.ems_namelist import get_ems_scenario, RURAL_AREAS, NAMES
from .term3_entrepreneurs_day_archetypes_01_25 import _mcq_q, _calc_q, _rubric_q, _svg_spec
from .term3_the_entrepreneur_archetypes_01_25 import _given, _req, _ledger
from .term3_entrepreneurs_day_archetypes_26_50 import _empty_cell


def arch_26_budget_definition_receipts_and_payments(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    period = rng.choice(["Term 3 Entrepreneur's Day", "opening month", "first quarter"])
    prompt = (
        f"Before opening a venture in {area}, {person} draws up a **budget** for {period} (Doc Q32).\n\n"
        f"Which definition accurately describes a business budget?"
    )
    correct = "A forward-looking list estimating expected cash receipts (income) and expected payments (expenses) over a specific period to guide spending, saving, or borrowing"
    distractors = [
        "A list solely of bank loans already repaid ten years ago",
        "An artistic poster designed to decorate a shop window",
        "A government certificate registering company VAT numbers",
    ]
    sol = (
        f"Step 1: Budget definition:\n"
        f"A budget projects future **receipts** (money expected in) and **payments** (money expected out) for {period}."
    )
    return _mcq_q(
        rng, f"g7_sb_26_{rng.randint(100000, 999999)}", "26_budget_definition_receipts_and_payments",
        "Defining a Startup Budget", prompt, correct, distractors, sol,
        {"tier_1": "Think of receipts vs payments projected into the future.",
         "tier_2": "A budget plans expected earnings and expenses before spending begins.",
         "tier_3": correct},
        ["confuses_budget_with_past_statement"]
    )


def arch_27_four_categories_in_startup_budget(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    ex_pair = rng.choice([
        ("photocopying flyers and buying coloured cardboard for posters", "Materials for advertising"),
        ("fabric tablecloth, cardboard shop name sign, and paint", "Materials for decorating the stand"),
        ("scrap wooden boards, nails, and strong glue for shelving", "Materials for building the display stand"),
        ("ingredients, car shampoo, sponges, or card stock for the item itself", "Materials for making the good or providing the service"),
    ])
    items, cat = ex_pair
    prompt = (
        f"When assembling an Entrepreneur's Day budget (Doc Q33), {person} lists: '{items}'.\n\n"
        f"Under which of the four standard budget categories do these items fall?"
    )
    correct = cat
    all_cats = [
        "Materials for making the good or providing the service",
        "Materials for building the display stand",
        "Materials for decorating the stand",
        "Materials for advertising",
    ]
    distractors = [c for c in all_cats if c != cat]
    sol = f"Step 1: Budget categorisation: '{items}' belong specifically to **{cat}**."
    return _mcq_q(
        rng, f"g7_sb_27_{rng.randint(100000, 999999)}", "27_four_categories_in_startup_budget",
        "Four Entrepreneur's Day Budget Categories", prompt, correct, distractors, sol,
        {"tier_1": "Match the item to production, stand building, stand decoration, or promotion.",
         "tier_2": "Focus on what task the materials perform on the day.",
         "tier_3": correct},
        ["miscategorises_budget_expense_group"]
    )


def arch_28_recycled_materials_cost_and_profit(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    jars = rng.choice([30, 40, 50])
    new_cost = rng.choice([4, 5, 6])
    decor_glue = rng.choice([25, 35])
    saved = jars * new_cost
    prompt = (
        f"{person} reuses {jars} washed glass jars collected cleanly from community recycling instead of buying new jars at R{new_cost} each "
        f"(spending only R{decor_glue} on decorative ribbon and glue).\n\n"
        f"How much expense does {person} save using recycled jars, and how does this affect profit (Doc Q35)?"
    )
    ans = f"R{saved} saved; lowers total expenses and increases net profit while reducing environmental waste"
    sol = (
        f"Step 1: Avoided purchase = {jars} * R{new_cost} = R{saved}.\n"
        f"Step 2: Using recycled materials reduces materials to buy, lowering total expenses by R{saved} and boosting profit while protecting the environment."
    )
    return _calc_q(
        rng, f"g7_sb_28_{rng.randint(100000, 999999)}", "28_recycled_materials_cost_and_profit",
        "Using Recycled Materials to Cut Costs", prompt, ans, sol,
        {"tier_1": "Multiply recycled units by the avoided cost per new container.",
         "tier_2": f"Avoided expense = {jars} * R{new_cost}; connect lower expenses directly to profit.",
         "tier_3": ans},
        ["omits_profit_link_of_recycling"]
    )


def arch_29_fixed_costs_definition_examples(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    stall_fee = rng.choice([30, 40, 50])
    sign_paint = rng.choice([15, 20])
    prompt = (
        f"Before making any bookmarks, {person} pays R{stall_fee} for stand hire and R{sign_paint} for a reusable display banner. "
        f"Whether {person} produces 10 bookmarks or 120 bookmarks, that R{stall_fee + sign_paint} total stays identical.\n\n"
        f"Which term defines costs that remain unchanged regardless of output volume (Doc Q36)?"
    )
    correct = "Fixed costs"
    distractors = [
        "Variable costs",
        "Mark-up revenue",
        "Sales receipts",
    ]
    sol = f"Step 1: Define fixed costs: Expenses (R{stall_fee + sign_paint}) that do not vary with quantity produced are **fixed costs**."
    return _mcq_q(
        rng, f"g7_sb_29_{rng.randint(100000, 999999)}", "29_fixed_costs_definition_examples",
        "Defining Fixed Costs", prompt, correct, distractors, sol,
        {"tier_1": "Look at the clue: 'stays identical whether 10 or 120 items are made'.",
         "tier_2": "Costs 'fixed' independently of production output = ...",
         "tier_3": correct},
        ["confuses_fixed_and_variable_costs"]
    )


def arch_30_variable_costs_definition_examples(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    rate = rng.choice([3, 4, 5])
    q_low, q_high = 10, rng.choice([40, 60])
    prompt = (
        f"{person} buys beads and cord costing R{rate} per bracelet: making {q_low} bracelets costs R{q_low * rate}, "
        f"whereas making {q_high} bracelets costs R{q_high * rate}.\n\n"
        f"Which term describes costs that change according to how many goods a business produces (Doc Q37)?"
    )
    correct = "Variable costs"
    distractors = [
        "Fixed costs",
        "Start-up loan repayments",
        "Cash surpluses",
    ]
    sol = f"Step 1: Define variable costs: Costs (R{rate}/unit) changing in step with production output are **variable costs**."
    return _mcq_q(
        rng, f"g7_sb_30_{rng.randint(100000, 999999)}", "30_variable_costs_definition_examples",
        "Defining Variable Costs", prompt, correct, distractors, sol,
        {"tier_1": "Notice that total material spending 'varies' directly from R" + f"{q_low*rate} to R{q_high*rate}.",
         "tier_2": "Costs moving with production count = variable costs.",
         "tier_3": correct},
        ["treats_ingredients_as_fixed_costs"]
    )


def arch_31_fixed_vs_variable_cost_graph_svg(rng: random.Random) -> Dict[str, Any]:
    fc = rng.choice([40, 50, 60])
    vc_u = rng.choice([3, 4, 5])
    max_q = 40
    tc_max = fc + max_q * vc_u
    svg_body = (
        f'<text x="290" y="20" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">Fixed Cost (R{fc}) vs Total Cost (R{vc_u}/unit)</text>'
        f'<line x1="65" y1="185" x2="510" y2="185" stroke="#334155" stroke-width="2"/>'
        f'<line x1="65" y1="35" x2="65" y2="185" stroke="#334155" stroke-width="2"/>'
        f'<line x1="65" y1="150" x2="500" y2="150" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="6,4"/>'
        f'<line x1="65" y1="150" x2="500" y2="52" stroke="#dc2626" stroke-width="2.5"/>'
        f'<text x="415" y="142" font-size="11" font-weight="bold" fill="#1d4ed8">Fixed Cost = R{fc}</text>'
        f'<text x="405" y="48" font-size="11" font-weight="bold" fill="#b91c1c">Total Cost @ {max_q} = R{tc_max}</text>'
        f'<text x="285" y="206" font-size="11" text-anchor="middle" fill="#475569">Quantity Produced (0 to {max_q} units)</text>'
    )
    prompt = (
        f"Study the cost graph plotting Fixed Cost (blue dashed line) and Total Cost (red solid line) from 0 to {max_q} units.\n\n"
        f"Why does the blue Fixed Cost line stay flat at R{fc} while Total Cost climbs to R{tc_max} at {max_q} units?"
    )
    correct = f"Fixed cost stays constant at R{fc} for all quantities, while Total Cost adds Variable Cost (R{vc_u} per unit * quantity) onto R{fc}"
    distractors = [
        f"Total Cost actually stays lower than R{fc} whenever production increases",
        "Fixed costs climb higher with every extra item made",
        "At 0 units produced, Total Cost equals R0 even with R{fc} stand rent".replace("{fc}", str(fc)),
    ]
    sol = f"At Q=0, Total Cost = R{fc} (fixed). At Q={max_q}, Total Cost = R{fc} + ({max_q}*R{vc_u}) = R{tc_max}."
    return _mcq_q(
        rng, f"g7_sb_31_{rng.randint(100000, 999999)}", "31_fixed_vs_variable_cost_graph_svg",
        "Interpreting Fixed vs Total Cost Graph", prompt, correct, distractors, sol,
        {"tier_1": "Observe the flat blue line height (R" + f"{fc}) vs the rising red slope.",
         "tier_2": "Total Cost starts at Fixed Cost and slopes upward by Variable Cost per item.",
         "tier_3": correct},
        ["thinks_total_cost_starts_at_zero_when_fixed_costs_exist"],
        diagram_spec=_svg_spec(svg_body, 580, 220),
    )


def arch_32_total_cost_formula_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    fc = rng.choice([45, 60, 75])
    vc_u = rng.choice([4, 5, 6])
    units = rng.choice([30, 40, 50])
    tc = fc + vc_u * units
    prompt = (
        f"{person} incurs R{fc} in fixed costs (banner & stall fee) plus R{vc_u} per bracelet in beads and clasps.\n\n"
        f"Calculate the **total cost** of producing {units} bracelets."
    )
    ans = f"R{tc}"
    sol = f"Total Cost = Fixed Cost + (Variable Cost * Units) = R{fc} + (R{vc_u} * {units}) = R{fc} + R{vc_u * units} = R{tc}."
    return _calc_q(
        rng, f"g7_sb_32_{rng.randint(100000, 999999)}", "32_total_cost_formula_calc",
        "Total Cost = Fixed + Variable", prompt, ans, sol,
        {"tier_1": "Multiply variable unit cost by number of bracelets, then add fixed cost once.",
         "tier_2": f"R{fc} + ({units} * R{vc_u}).",
         "tier_3": ans},
        ["multiplies_fixed_cost_by_unit_quantity"]
    )


def arch_33_cost_per_item_unit_calculation(rng: random.Random) -> Dict[str, Any]:
    # Grounded in Doc Q9a (rusks)
    n1, n2 = rng.sample(NAMES, 2)
    qty = rng.choice([50, 80, 100])
    unit_c = rng.choice([3, 4, 5])
    tot_cost = qty * unit_c
    prompt = (
        f"{n1} and {n2} budget to bake {qty} small packs of home-made rusks for Entrepreneur's Day at a total cost of R{tot_cost}.\n\n"
        f"Calculate the **cost per item** (one pack of rusks)."
    )
    ans = f"R{unit_c}"
    sol = f"Cost per item = Total Cost / Number of goods = R{tot_cost} / {qty} = R{unit_c}."
    return _calc_q(
        rng, f"g7_sb_33_{rng.randint(100000, 999999)}", "33_cost_per_item_unit_calculation",
        "Cost Per Item Formula", prompt, ans, sol,
        {"tier_1": "Divide total cost by the total number of packs made.",
         "tier_2": f"R{tot_cost} / {qty}.",
         "tier_3": ans},
        ["divides_units_by_total_cost"]
    )


def arch_34_selling_price_formula_meaning(rng: random.Random) -> Dict[str, Any]:
    cost_u = rng.choice([6, 8, 10])
    markup = rng.choice([4, 5, 6])
    sp = cost_u + markup
    prompt = (
        f"If producing one decorated jar costs R{cost_u} and an entrepreneur decides to add a mark-up of R{markup} per jar, "
        f"what formula defines the **selling price** (Doc Q38), and what is its value?"
    )
    correct = f"Selling price = Cost price + Mark-up = R{cost_u} + R{markup} = R{sp}"
    distractors = [
        f"Selling price = Cost price - Mark-up = R{cost_u - markup}",
        f"Selling price = Cost price * Mark-up = R{cost_u * markup}",
        f"Selling price = Total fixed fees only = R{markup}",
    ]
    sol = f"Formula: Selling Price = Cost Price + Mark-up = R{cost_u} + R{markup} = R{sp}."
    return _mcq_q(
        rng, f"g7_sb_34_{rng.randint(100000, 999999)}", "34_selling_price_formula_meaning",
        "Selling Price Formula", prompt, correct, distractors, sol,
        {"tier_1": "Mark-up is the extra profit margin added ON TOP of cost price.",
         "tier_2": f"Add R{cost_u} + R{markup}.",
         "tier_3": correct},
        ["subtracts_markup_from_cost"]
    )


def arch_35_fudge_profit_target_selling_price(rng: random.Random) -> Dict[str, Any]:
    # Grounded directly in Doc Q8a
    n1, n2 = rng.sample(NAMES, 2)
    qty = rng.choice([20, 25, 30])
    tot_cost = qty * rng.choice([8, 10])
    desired_profit = qty * rng.choice([10, 12, 15])
    tot_income = tot_cost + desired_profit
    sp = tot_income // qty
    prompt = (
        f"{n1} and {n2} spend R{tot_cost} to make {qty} bags of homemade fudge and want to earn R{desired_profit} profit.\n\n"
        f"What **selling price** must they charge for each bag of fudge?"
    )
    ans = f"R{sp}"
    sol = (
        f"Step 1: Total Income required = Total Cost + Target Profit = R{tot_cost} + R{desired_profit} = R{tot_income}.\n"
        f"Step 2: Selling Price = Total Income / Quantity = R{tot_income} / {qty} = R{sp}."
    )
    return _calc_q(
        rng, f"g7_sb_35_{rng.randint(100000, 999999)}", "35_fudge_profit_target_selling_price",
        "Pricing Fudge Bags for Desired Profit", prompt, ans, sol,
        {"tier_1": "Remember income must recover BOTH R" + f"{tot_cost} cost AND R{desired_profit} profit.",
         "tier_2": f"(R{tot_cost} + R{desired_profit}) / {qty}.",
         "tier_3": ans},
        ["forgets_cost_when_calculating_target_selling_price"]
    )


def arch_36_markup_from_cost_and_selling_price(rng: random.Random) -> Dict[str, Any]:
    # Grounded directly in Doc Q8b & Q9c
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    qty = rng.choice([20, 40, 50])
    unit_c = rng.choice([6, 8, 10])
    tot_c = qty * unit_c
    markup = rng.choice([4, 6, 9])
    sp = unit_c + markup
    prompt = (
        f"{person} produces {qty} bags of fudge at a total batch cost of R{tot_c}, and sets the selling price at R{sp} per bag.\n\n"
        f"Calculate the **mark-up per bag**."
    )
    ans = f"R{markup}"
    sol = (
        f"Step 1: Cost price per bag = R{tot_c} / {qty} = R{unit_c}.\n"
        f"Step 2: Mark-up = Selling Price - Cost Price = R{sp} - R{unit_c} = R{markup} per bag."
    )
    return _calc_q(
        rng, f"g7_sb_36_{rng.randint(100000, 999999)}", "36_markup_from_cost_and_selling_price",
        "Calculating Mark-up Per Item", prompt, ans, sol,
        {"tier_1": "Find the unit cost of ONE bag first.",
         "tier_2": f"Unit cost = R{tot_c}/{qty}; subtract from R{sp}.",
         "tier_3": ans},
        ["subtracts_selling_price_from_batch_cost"]
    )


def arch_37_percentage_markup_on_cost_pricing(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, item = sc["entrepreneur"], sc["item_sold"]
    cost_u = rng.choice([8, 10, 12, 16])
    pct = rng.choice([25, 50])
    markup = cost_u * pct // 100
    sp = cost_u + markup
    prompt = (
        f"{person}'s unit production cost for {item} is R{cost_u}. To earn steady profit, {person} adds a **{pct}% mark-up** on cost.\n\n"
        f"Calculate the Rand mark-up and final **selling price** per item."
    )
    ans = f"Mark-up = R{markup}; Selling Price = R{sp}"
    sol = (
        f"Step 1: Mark-up = {pct}% of R{cost_u} = R{markup}.\n"
        f"Step 2: Selling Price = R{cost_u} + R{markup} = R{sp}."
    )
    return _calc_q(
        rng, f"g7_sb_37_{rng.randint(100000, 999999)}", "37_percentage_markup_on_cost_pricing",
        "Percentage Mark-up Calculation", prompt, ans, sol,
        {"tier_1": f"First calculate {pct}% of R{cost_u}.",
         "tier_2": f"Add the Rand mark-up to R{cost_u}.",
         "tier_3": ans},
        ["treats_percentage_number_as_rand_amount"]
    )


def arch_38_herb_gifts_entrepreneurs_day_budget_table(rng: random.Random) -> Dict[str, Any]:
    # Grounded directly in Doc Q14
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    qty = rng.choice([30, 40, 50])
    sp = rng.choice([10, 12])
    herb_c = rng.choice([4, 5])
    ribbon_m = 10
    ribbon_total = 25  # 10m * R2,50
    promo_etc = rng.choice([50, 60])
    tot_rec = qty * sp
    herbs_tot = qty * herb_c
    tot_pay = herbs_tot + ribbon_total + promo_etc
    surplus = tot_rec - tot_pay
    headers = ["Receipts", "R", "Payments", "R"]
    rows = [
        [_given("r0_c0", f"Sale of herb gifts ({qty} * R{sp})"), _req("r0_c1", str(tot_rec)), _given("r0_c2", "Recycled jars & public open soil"), _given("r0_c3", "0")],
        [_empty_cell("r1_c0"), _empty_cell("r1_c1"), _given("r1_c2", f"Herb seedlings ({qty} * R{herb_c})"), _req("r1_c3", str(herbs_tot))],
        [_empty_cell("r2_c0"), _empty_cell("r2_c1"), _given("r2_c2", f"Ribbon ({ribbon_m} m @ R2,50/m)"), _given("r2_c3", str(ribbon_total))],
        [_empty_cell("r3_c0"), _empty_cell("r3_c1"), _given("r3_c2", "Leaflets, paint, bags, glue, signage"), _given("r3_c3", str(promo_etc))],
        [_given("r4_c0", "Total Receipts"), _req("r4_c1", str(tot_rec)), _given("r4_c2", "Total Payments"), _req("r4_c3", str(tot_pay))],
        [_given("r5_c0", "Cash Surplus (Receipts - Payments)"), _req("r5_c1", str(surplus)), _empty_cell("r5_c2"), _empty_cell("r5_c3")],
    ]
    cmap = {"r0_c1": str(tot_rec), "r1_c3": str(herbs_tot), "r4_c1": str(tot_rec), "r4_c3": str(tot_pay), "r5_c1": str(surplus)}
    chints = {
        "r0_c1": f"{qty} * {sp}", "r1_c3": f"{qty} * {herb_c}",
        "r4_c1": "Copy/sum Total Receipts", "r4_c3": f"0 + {herbs_tot} + {ribbon_total} + {promo_etc}",
        "r5_c1": "Total Receipts minus Total Payments",
    }
    sol = f"1. Receipts={tot_rec}\n2. Herbs={herbs_tot}\n3. Total Payments={herbs_tot}+{ribbon_total}+{promo_etc}={tot_pay}\n4. Surplus={tot_rec}-{tot_pay}=R{surplus}."
    return _ledger(
        f"g7_sb_38_{rng.randint(100000, 999999)}", "38_herb_gifts_entrepreneurs_day_budget_table",
        "Recycled Herb Gifts Startup Budget",
        f"{person} plans to sell {qty} herb gifts in recycled jars for R{sp} each. Complete the Receipts and Payments budget table.",
        headers, rows, cmap, chints, f"Total Receipts = R{tot_rec}; Total Payments = R{tot_pay}; Cash Surplus = R{surplus}", sol,
        {"tier_1": "Note that recycled jars and soil cost R0.",
         "tier_2": f"Multiply {qty}*R{sp} for receipts and {qty}*R{herb_c} for seedlings, then total payments.",
         "tier_3": f"Rec {tot_rec}, Pay {tot_pay}, Surplus {surplus}."},
        ["counts_recycled_jars_as_expense"], marks=10,
    )


def arch_39_bookmarks_cards_budget_surplus_table(rng: random.Random) -> Dict[str, Any]:
    # Grounded directly in Doc Q34
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    tot_rec = rng.choice([450, 500, 600])
    card_c = rng.choice([45, 50, 60])
    decor_c = rng.choice([35, 45])
    promo_c = rng.choice([40, 50])
    bags_glue = rng.choice([35, 45])
    tot_pay = card_c + decor_c + promo_c + bags_glue
    surplus = tot_rec - tot_pay
    headers = ["Receipts", "R", "Payments", "R"]
    rows = [
        [_given("r0_c0", "Projected sales of bookmarks & cards"), _given("r0_c1", str(tot_rec)), _given("r0_c2", "Coloured card stock"), _given("r0_c3", str(card_c))],
        [_empty_cell("r1_c0"), _empty_cell("r1_c1"), _given("r1_c2", "Buttons, ribbon, stickers & glitter"), _given("r1_c3", str(decor_c))],
        [_empty_cell("r2_c0"), _empty_cell("r2_c1"), _given("r2_c2", "Leaflets, signage & paint"), _given("r2_c3", str(promo_c))],
        [_empty_cell("r3_c0"), _empty_cell("r3_c1"), _given("r3_c2", "Packaging bags & craft glue"), _given("r3_c3", str(bags_glue))],
        [_given("r4_c0", "Total Receipts"), _req("r4_c1", str(tot_rec)), _given("r4_c2", "Total Payments"), _req("r4_c3", str(tot_pay))],
        [_given("r5_c0", "Budgeted Cash Surplus"), _req("r5_c1", str(surplus)), _empty_cell("r5_c2"), _empty_cell("r5_c3")],
    ]
    cmap = {"r4_c1": str(tot_rec), "r4_c3": str(tot_pay), "r5_c1": str(surplus)}
    chints = {"r4_c1": "Total projected sales receipts", "r4_c3": "Add all 4 Payment rows", "r5_c1": "Receipts minus Payments"}
    sol = f"1. Total Receipts = R{tot_rec}\n2. Total Payments = R{card_c}+R{decor_c}+R{promo_c}+R{bags_glue}=R{tot_pay}\n3. Cash Surplus = R{tot_rec}-R{tot_pay}=R{surplus}."
    return _ledger(
        f"g7_sb_39_{rng.randint(100000, 999999)}", "39_bookmarks_cards_budget_surplus_table",
        "Greeting Cards & Bookmarks Startup Budget",
        f"Complete {person}'s Receipts & Payments budget for handmade bookmarks and greeting cards to determine Total Payments and Cash Surplus.",
        headers, rows, cmap, chints, f"Total Payments = R{tot_pay}; Cash Surplus = R{surplus}", sol,
        {"tier_1": "Sum all four payment lines first.",
         "tier_2": f"Subtract Total Payments from R{tot_rec}.",
         "tier_3": f"Payments {tot_pay}; Surplus {surplus}."},
        ["omits_packaging_and_glue_rows"], marks=6,
    )


def arch_40_budget_revision_when_costs_rise(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    rec = rng.choice([500, 600])
    old_ing = rng.choice([180, 200])
    hike = rng.choice([45, 65])
    new_ing = old_ing + hike
    fixed = rng.choice([70, 90])
    new_pay = new_ing + fixed
    new_surp = rec - new_pay
    headers = ["Revised Budget Line", "Original (R)", "Updated Cost (R)"]
    rows = [
        [_given("r0_c0", "Projected Receipts"), _given("r0_c1", str(rec)), _given("r0_c2", str(rec))],
        [_given("r1_c0", f"Ingredients (Supplier hike +R{hike})"), _given("r1_c1", str(old_ing)), _req("r1_c2", str(new_ing))],
        [_given("r2_c0", "Stand & Advertising Costs"), _given("r2_c1", str(fixed)), _given("r2_c2", str(fixed))],
        [_given("r3_c0", "Revised Total Payments"), _given("r3_c1", str(old_ing + fixed)), _req("r3_c2", str(new_pay))],
        [_given("r4_c0", "Revised Cash Surplus"), _given("r4_c1", str(rec - old_ing - fixed)), _req("r4_c2", str(new_surp))],
    ]
    cmap = {"r1_c2": str(new_ing), "r3_c2": str(new_pay), "r4_c2": str(new_surp)}
    chints = {"r1_c2": f"{old_ing}+{hike}", "r3_c2": "Add updated ingredients + stand/ads", "r4_c2": f"{rec} minus revised payments"}
    sol = f"1. Updated Ingredients = R{old_ing}+R{hike}=R{new_ing}\n2. Revised Payments = R{new_ing}+R{fixed}=R{new_pay}\n3. Revised Surplus = R{rec}-R{new_pay}=R{new_surp}."
    return _ledger(
        f"g7_sb_40_{rng.randint(100000, 999999)}", "40_budget_revision_when_costs_rise",
        "Updating Budget After Input Price Increase",
        f"Before launch, supplier prices jump by R{hike}. Update {person}'s startup budget figures in the Updated Cost column.",
        headers, rows, cmap, chints, f"New Ing = R{new_ing}; New Pay = R{new_pay}; New Surplus = R{new_surp}", sol,
        {"tier_1": f"Add R{hike} only to Ingredients, leaving stand & ad fees unchanged.",
         "tier_2": f"Recompute Total Payments and Cash Surplus from R{rec} receipts.",
         "tier_3": f"Ing {new_ing}, Pay {new_pay}, Surplus {new_surp}."},
        ["fails_to_recompute_surplus_after_cost_hike"], marks=6,
    )


def arch_41_advertising_channel_cost_efficiency_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    # Channel metrics: Print flyers vs Local radio vs Billboard
    f_cost, f_reach = rng.choice([40, 50]), rng.choice([200, 250])
    b_cost, b_reach = rng.choice([4000, 5000]), rng.choice([400, 500])
    f_cpm = round(f_cost / f_reach, 2)
    b_cpm = round(b_cost / b_reach, 2)
    svg_body = (
        f'<text x="290" y="22" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">Advertising Cost vs Target Market Reach</text>'
        f'<rect x="50" y="55" width="215" height="95" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="157" y="82" font-size="12" font-weight="bold" text-anchor="middle" fill="#14532d">School Flyers &amp; Posters</text>'
        f'<text x="157" y="106" font-size="11" text-anchor="middle" fill="#166534">Cost: R{f_cost} | Reaches: {f_reach} buyers</text>'
        f'<text x="157" y="126" font-size="11" text-anchor="middle" fill="#166534">R{f_cpm:.2f} per target buyer</text>'.replace(".", ",")
        + f'<rect x="305" y="55" width="225" height="95" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="417" y="82" font-size="12" font-weight="bold" text-anchor="middle" fill="#7f1d1d">Highway Billboard</text>'
        f'<text x="417" y="106" font-size="11" text-anchor="middle" fill="#991b1b">Cost: R{b_cost} | Reaches: {b_reach} locals</text>'
        f'<text x="417" y="126" font-size="11" text-anchor="middle" fill="#991b1b">R{b_cpm:.2f} per target buyer</text>'.replace(".", ",")
    )
    prompt = (
        f"Study the advertising cost-efficiency chart comparing School Flyers (R{f_cost} reaching {f_reach} buyers) "
        f"with a Highway Billboard (R{b_cost} reaching {b_reach} locals) for {person}'s startup.\n\n"
        f"Which option yields far better value per target buyer reached?"
    )
    correct = f"School Flyers & Posters at R{f_cpm:.2f} per buyer vs R{b_cpm:.2f} per buyer on the billboard".replace(".", ",")
    distractors = [
        f"Highway Billboard because spending R{b_cost} guarantees lower cost per buyer than R{f_cost}",
        "Neither channel reaches target customers",
        "Both options cost the exact same amount per buyer",
    ]
    sol = f"Flyers cost R{f_cost}/{f_reach} = R{f_cpm:.2f} per target buyer vs R{b_cost}/{b_reach} = R{b_cpm:.2f} per buyer.".replace(".", ",")
    return _mcq_q(
        rng, f"g7_sb_41_{rng.randint(100000, 999999)}", "41_advertising_channel_cost_efficiency_svg",
        "Advertising Cost Efficiency Comparison", prompt, correct, distractors, sol,
        {"tier_1": "Divide Total Cost by Target Buyers Reached in each box.",
         "tier_2": "Lower Rand per target buyer reached gives better budget efficiency.",
         "tier_3": correct},
        ["picks_largest_headline_spend_as_best_value"],
        diagram_spec=_svg_spec(svg_body, 580, 175),
    )


def arch_42_display_stand_budget_fixed_vs_variable_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    stand_c = rng.choice([30, 40])
    poster_c = rng.choice([20, 25])
    units = rng.choice([20, 30])
    mat_u = rng.choice([5, 6])
    bag_u = 1
    tot_fix = stand_c + poster_c
    tot_var = units * (mat_u + bag_u)
    tot_all = tot_fix + tot_var
    headers = ["Budget Cost Item", "Fixed or Variable", "Total Amount (R)"]
    rows = [
        [_given("r0_c0", "Strong glue & signage card for stand"), _req("r0_c1", "Fixed"), _given("r0_c2", str(stand_c))],
        [_given("r1_c0", "Promotional colour posters"), _req("r1_c1", "Fixed"), _given("r1_c2", str(poster_c))],
        [_given("r2_c0", f"Product materials ({units} * R{mat_u}) & bags ({units} * R1)"), _req("r2_c1", "Variable"), _req("r2_c2", str(tot_var))],
        [_given("r3_c0", "Total Budgeted Payments"), _given("r3_c1", f"Fixed (R{tot_fix}) + Variable"), _req("r3_c2", str(tot_all))],
    ]
    cmap = {"r0_c1": "Fixed", "r1_c1": "Fixed", "r2_c1": "Variable", "r2_c2": str(tot_var), "r3_c2": str(tot_all)}
    chints = {
        "r0_c1": "Stays constant regardless of units made.", "r1_c1": "Paid once for posters.",
        "r2_c1": "Changes directly with quantity made.", "r2_c2": f"{units} * ({mat_u} + 1)",
        "r3_c2": f"Sum all costs ({stand_c} + {poster_c} + variable).",
    }
    sol = f"1. Stand/Posters = Fixed (R{tot_fix})\n2. Product & bags = Variable ({units} * R{mat_u + 1} = R{tot_var})\n3. Grand Total = R{tot_all}."
    return _ledger(
        f"g7_sb_42_{rng.randint(100000, 999999)}", "42_display_stand_budget_fixed_vs_variable_table",
        "Classifying Startup Budget Costs",
        f"Classify each expense as Fixed or Variable and compute the Variable and Total cost figures for {person}'s {units}-unit startup budget.",
        headers, rows, cmap, chints, f"Fixed; Fixed; Variable (R{tot_var}); Total R{tot_all}", sol,
        {"tier_1": "Stand & posters are paid once (Fixed); per-unit materials & bags scale with units (Variable).",
         "tier_2": f"Variable total = {units} * R{mat_u + 1}.",
         "tier_3": f"Fixed, Fixed, Variable, Var={tot_var}, Total={tot_all}."},
        ["classifies_stand_decor_as_variable"], marks=10,
    )


def arch_43_breakeven_covering_fixed_costs(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    fc = rng.choice([60, 80, 100])
    cost_u = rng.choice([4, 5])
    sp = cost_u + rng.choice([4, 5])
    markup = sp - cost_u
    units_be = fc // markup if fc % markup == 0 else (fc // markup) + 1
    if fc % markup != 0:
        fc = markup * rng.choice([12, 15, 20])
        units_be = fc // markup
    prompt = (
        f"{person} has fixed setup costs of R{fc}. Each craft bag costs R{cost_u} in materials and sells for R{sp} (mark-up R{markup}/bag).\n\n"
        f"How many bags must {person} sell purely to recover all R{fc} fixed setup costs (break-even)?"
    )
    ans = f"{units_be} bags"
    sol = (
        f"Step 1: Mark-up contribution per bag = R{sp} - R{cost_u} = R{markup}.\n"
        f"Step 2: Bags to cover Fixed Costs = R{fc} / R{markup} = {units_be} bags."
    )
    return _calc_q(
        rng, f"g7_sb_43_{rng.randint(100000, 999999)}", "43_breakeven_covering_fixed_costs",
        "Units Needed to Cover Fixed Setup Costs", prompt, ans, sol,
        {"tier_1": "Divide Fixed Costs by the mark-up profit earned on each bag—not the full selling price!",
         "tier_2": f"R{fc} / (R{sp} - R{cost_u}).",
         "tier_3": ans},
        ["divides_fixed_cost_by_full_selling_price"]
    )


def arch_44_budget_deficit_prevention_scenario(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    rec = rng.choice([250, 300])
    pay = rec + rng.choice([70, 95])
    shortfall = pay - rec
    prompt = (
        f"{person}'s draft Entrepreneur's Day budget shows expected Receipts of R{rec} and Payments of R{pay} — "
        f"a projected **cash deficit of R{shortfall}**.\n\n"
        f"Which smart revision fixes the deficit BEFORE launch day?"
    )
    correct = f"Replace expensive bought containers with R0 recycled jars and cut decorative frills by at least R{shortfall} (or review pricing/volume)"
    distractors = [
        f"Spend an extra R{shortfall} on imported neon balloons to make payments even higher",
        "Ignore the deficit because actual cash automatically doubles on Entrepreneur's Day",
        "Delete two payment rows from the paper sheet without removing actual spending",
    ]
    sol = f"Step 1: Fix R{shortfall} deficit: Lower material payments (using recycled goods) or lift viable revenue until Receipts >= Payments."
    return _mcq_q(
        rng, f"g7_sb_44_{rng.randint(100000, 999999)}", "44_budget_deficit_prevention_scenario",
        "Resolving a Startup Budget Deficit", prompt, correct, distractors, sol,
        {"tier_1": "How do you shift Payments below Receipts legitimately?",
         "tier_2": f"Cut unnecessary costs by R{shortfall}+ (such as reusing jars) or adjust viable sales.",
         "tier_3": correct},
        ["deletes_budget_lines_without_cutting_real_costs"]
    )


def arch_45_compilation_of_business_portfolio(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    fmt = rng.choice(["an illustrated booklet", "a neatly mounted visual poster", "a physical stand prototype & structured report"])
    prompt = (
        f"After completing personal fit, consumer research, SWOT, SMART goals, budgeting, and advertisement drafting in {area}, "
        f"{person} compiles all project work into {fmt}.\n\n"
        f"Which principle governs assembling the final startup project presentation?"
    )
    correct = "Combining all five sequential stages clearly and creatively in a structured display (poster, booklet, report, or model) showing complete evidence"
    distractors = [
        "Throwing away market research and cost calculations to hand in only a blank drawing",
        "Submitting identical text with zero local pricing or target audience details",
        "Waiting until next school year to set goals or estimate receipts",
    ]
    sol = f"Step 1: Final compilation (Project Step f): Present all 5 completed startup steps creatively and clearly using {fmt}."
    return _mcq_q(
        rng, f"g7_sb_45_{rng.randint(100000, 999999)}", "45_compilation_of_business_portfolio",
        "Compiling a Complete Startup Presentation", prompt, correct, distractors, sol,
        {"tier_1": "Every startup section contributes evidence toward one cohesive proposal.",
         "tier_2": "Choose a creative format showcasing all five steps completely.",
         "tier_3": correct},
        ["submits_incomplete_or_unstructured_portfolio"]
    )


def arch_46_comparing_competing_business_ideas_table(rng: random.Random) -> Dict[str, Any]:
    m_a = rng.choice([2, 3])
    m_b = rng.choice([8, 9])
    m_c = rng.choice([5, 6])
    d_a, d_b, d_c = 20, rng.choice([45, 50]), 15
    p_a, p_b, p_c = m_a * d_a, m_b * d_b, m_c * d_c
    headers = ["Startup Idea", "Unit Mark-up (R)", "Verified Survey Demand (Units)", "Projected Gross Profit (R)"]
    rows = [
        [_given("r0_c0", "Idea A: Plain Bookmarks"), _given("r0_c1", str(m_a)), _given("r0_c2", str(d_a)), _req("r0_c3", str(p_a))],
        [_given("r1_c0", "Idea B: Fresh Vetkoek"), _given("r1_c1", str(m_b)), _given("r1_c2", str(d_b)), _req("r1_c3", str(p_b))],
        [_given("r2_c0", "Idea C: Pebble Weights"), _given("r2_c1", str(m_c)), _given("r2_c2", str(d_c)), _req("r2_c3", str(p_c))],
        [_given("r3_c0", "Best Idea Name (A, B, or C)"), _empty_cell("r3_c1"), _empty_cell("r3_c2"), _req("r3_c3", "Idea B")],
    ]
    cmap = {"r0_c3": str(p_a), "r1_c3": str(p_b), "r2_c3": str(p_c), "r3_c3": "Idea B"}
    chints = {
        "r0_c3": f"{m_a} * {d_a}", "r1_c3": f"{m_b} * {d_b}", "r2_c3": f"{m_c} * {d_c}",
        "r3_c3": "Enter the Idea label with highest Projected Gross Profit (Idea A, Idea B, or Idea C).",
    }
    sol = f"1. Idea A: {m_a}*{d_a}=R{p_a}\n2. Idea B: {m_b}*{d_b}=R{p_b}\n3. Idea C: {m_c}*{d_c}=R{p_c}\nBest choice: Idea B."
    return _ledger(
        f"g7_sb_46_{rng.randint(100000, 999999)}", "46_comparing_competing_business_ideas_table",
        "Evaluating Startup Feasibility Across Ideas",
        "Compare three competing school business ideas by multiplying Unit Mark-up by Survey Demand and selecting the strongest option.",
        headers, rows, cmap, chints, f"A=R{p_a}, B=R{p_b}, C=R{p_c}; Winner: Idea B", sol,
        {"tier_1": "Multiply mark-up per unit by verified demand on rows 1-3.",
         "tier_2": "Pick the Idea yielding the largest projected profit.",
         "tier_3": f"Profits: {p_a}, {p_b}, {p_c}; Winner: Idea B."},
        ["chooses_lowest_demand_product"], marks=8,
    )


def arch_47_rural_recycling_microenterprise_costing(rng: random.Random) -> Dict[str, Any]:
    rural = rng.choice(RURAL_AREAS)
    person = rng.choice(["Dakalo", "Thabo", "Naledi", "Siyanda"])
    taxi_fixed = rng.choice([40, 50, 60])
    var_paint = rng.choice([4, 5])
    units = rng.choice([25, 30])
    sp = rng.choice([12, 15])
    tot_cost = taxi_fixed + units * var_paint
    rev = units * sp
    profit = rev - tot_cost
    prompt = (
        f"In {rural}, {person} collects clean scrap tin cans at R0, spends R{taxi_fixed} on a round-trip taxi to fetch enamel paint "
        f"(Fixed Cost), and uses R{var_paint} of paint/varnish per pencil holder (Variable Cost) for {units} holders sold at R{sp} each.\n\n"
        f"Calculate {person}'s **net profit** after transport and paint."
    )
    ans = f"R{profit}"
    sol = (
        f"Step 1: Total Cost = Taxi Fixed (R{taxi_fixed}) + Paint Variable ({units} * R{var_paint} = R{units * var_paint}) = R{tot_cost}.\n"
        f"Step 2: Sales Income = {units} * R{sp} = R{rev}.\n"
        f"Step 3: Net Profit = R{rev} - R{tot_cost} = R{profit}."
    )
    return _calc_q(
        rng, f"g7_sb_47_{rng.randint(100000, 999999)}", "47_rural_recycling_microenterprise_costing",
        "Rural Transport and Recycled Craft Profit", prompt, ans, sol,
        {"tier_1": "Include the round-trip taxi cost alongside per-can varnish!",
         "tier_2": f"Sales = {units}*R{sp}; Costs = R{taxi_fixed} + ({units}*R{var_paint}).",
         "tier_3": f"R{profit}"},
        ["ignores_fixed_taxi_procurement_cost"]
    )


def arch_48_matching_startup_terms_exam_matrix(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("SWOT analysis", "Internal Strengths/Weaknesses and External Opportunities/Threats audit"),
        ("Mark-up", "The extra profit amount added onto cost price to reach selling price"),
        ("Mass media", "Expensive channels like national TV/newspapers reaching vast general audiences"),
        ("Cost per item", "Total production cost divided by total number of units made"),
    ])
    term, desc = pair
    prompt = f"Which key business startup concept corresponds accurately to the definition: **'{desc}'**?"
    correct = term
    all_terms = ["SWOT analysis", "Mark-up", "Mass media", "Cost per item"]
    distractors = [t for t in all_terms if t != term]
    sol = f"Definition Match: '{desc}' describes **{term}**."
    return _mcq_q(
        rng, f"g7_sb_48_{rng.randint(100000, 999999)}", "48_matching_startup_terms_exam_matrix",
        "Key Business Startup Terminology Match", prompt, correct, distractors, sol,
        {"tier_1": "Read the exact keywords in the definition carefully.",
         "tier_2": "Match audit vs profit margin vs broad media vs unit division.",
         "tier_3": term},
        ["confuses_markup_with_cost_per_item"]
    )


def arch_49_pricing_volume_vs_margin_tradeoff(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    cost_u = rng.choice([5, 6])
    fc = rng.choice([40, 50])
    # Option A: high price R15, low volume 12 -> profit = (15-c)*12 - fc
    # Option B: fair price R10, high volume 35 -> profit = (10-c)*35 - fc
    p_a, q_a = 15, rng.choice([10, 12])
    p_b, q_b = 10, rng.choice([30, 35])
    prof_a = (p_a - cost_u) * q_a - fc
    prof_b = (p_b - cost_u) * q_b - fc
    diff = prof_b - prof_a
    prompt = (
        f"{person} sells juice bottles costing R{cost_u} each plus R{fc} fixed stall fee:\n"
        f"- Strategy A: Charge R{p_a}/bottle, selling only {q_a} bottles.\n"
        f"- Strategy B: Charge affordable R{p_b}/bottle, selling {q_b} bottles.\n\n"
        f"How much **more total net profit** does Strategy B earn than Strategy A?"
    )
    ans = f"R{diff} more (Strategy B: R{prof_b} vs Strategy A: R{prof_a})"
    sol = (
        f"Step 1: Strategy A profit = {q_a}*(R{p_a}-R{cost_u}) - R{fc} = R{prof_a}.\n"
        f"Step 2: Strategy B profit = {q_b}*(R{p_b}-R{cost_u}) - R{fc} = R{prof_b}.\n"
        f"Step 3: Difference = R{prof_b} - R{prof_a} = R{diff} more profit."
    )
    return _calc_q(
        rng, f"g7_sb_49_{rng.randint(100000, 999999)}", "49_pricing_volume_vs_margin_tradeoff",
        "Pricing Volume vs Per-Unit Margin Tradeoff", prompt, ans, sol,
        {"tier_1": "Compute total profit = (selling price - unit cost)*units - fixed fee for BOTH strategies.",
         "tier_2": f"A profit = R{prof_a}; B profit = R{prof_b}. Subtract A from B.",
         "tier_3": ans},
        ["picks_highest_unit_price_ignoring_demand_drop"]
    )


def arch_50_comprehensive_business_startup_blueprint(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    units = rng.choice([40, 50, 60])
    var_u = rng.choice([4, 5])
    fc_stand = rng.choice([60, 80])
    markup_u = rng.choice([5, 6])
    sp_u = var_u + markup_u
    tot_var = units * var_u
    tot_pay = tot_var + fc_stand
    tot_rec = units * sp_u
    unit_full = round(tot_pay / units, 2)
    surplus = tot_rec - tot_pay
    headers = ["Startup Blueprint Element", "Given / Formula", "Calculated Value"]
    rows = [
        [_given("r0_c0", "Variable production cost (total)"), _given("r0_c1", f"{units} units * R{var_u}"), _req("r0_c2", str(tot_var))],
        [_given("r1_c0", "Fixed stand & flyers cost"), _given("r1_c1", "One-time setup"), _given("r1_c2", str(fc_stand))],
        [_given("r2_c0", "Total Budgeted Payments"), _given("r2_c1", "Total Variable + Fixed"), _req("r2_c2", str(tot_pay))],
        [_given("r3_c0", "Selling Price per unit"), _given("r3_c1", f"Variable unit R{var_u} + R{markup_u} mark-up"), _req("r3_c2", str(sp_u))],
        [_given("r4_c0", "Total Budgeted Receipts"), _given("r4_c1", f"{units} units * Selling Price"), _req("r4_c2", str(tot_rec))],
        [_given("r5_c0", "Projected Cash Surplus"), _given("r5_c1", "Total Receipts - Total Payments"), _req("r5_c2", str(surplus))],
    ]
    cmap = {"r0_c2": str(tot_var), "r2_c2": str(tot_pay), "r3_c2": str(sp_u), "r4_c2": str(tot_rec), "r5_c2": str(surplus)}
    chints = {
        "r0_c2": f"{units} * {var_u}", "r2_c2": "Add Variable + Fixed",
        "r3_c2": f"{var_u} + {markup_u}", "r4_c2": f"{units} * selling price",
        "r5_c2": "Total Receipts - Total Payments",
    }
    sol = (
        f"1. Total Variable = {units}*R{var_u} = R{tot_var}\n2. Total Payments = R{tot_var}+R{fc_stand} = R{tot_pay} (full unit cost R{unit_full:.2f})\n"
        f"3. Selling Price = R{var_u}+R{markup_u} = R{sp_u}\n4. Total Receipts = {units}*R{sp_u} = R{tot_rec}\n5. Cash Surplus = R{tot_rec}-R{tot_pay} = R{surplus}."
    )
    return _ledger(
        f"g7_sb_50_{rng.randint(100000, 999999)}", "50_comprehensive_business_startup_blueprint",
        "Capstone Business Launch Budget & Pricing Table",
        f"{person} prepares to launch a new craft venture in {area}. Complete every calculated cell (numeric Rand amounts) in the startup budget and pricing schedule.",
        headers, rows, cmap, chints, f"Payments = R{tot_pay}; Selling Price = R{sp_u}; Receipts = R{tot_rec}; Surplus = R{surplus}", sol,
        {"tier_1": "Work downwards through Variable Cost, Total Payments, Selling Price, Receipts, and Surplus.",
         "tier_2": f"Remember Fixed Setup = R{fc_stand} must be deducted before finding final Cash Surplus.",
         "tier_3": f"Var {tot_var}, Pay {tot_pay}, SP {sp_u}, Rec {tot_rec}, Surplus {surplus}."},
        ["omits_fixed_cost_from_cash_surplus"], marks=10,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_budget_definition_receipts_and_payments": arch_26_budget_definition_receipts_and_payments,
    "27_four_categories_in_startup_budget": arch_27_four_categories_in_startup_budget,
    "28_recycled_materials_cost_and_profit": arch_28_recycled_materials_cost_and_profit,
    "29_fixed_costs_definition_examples": arch_29_fixed_costs_definition_examples,
    "30_variable_costs_definition_examples": arch_30_variable_costs_definition_examples,
    "31_fixed_vs_variable_cost_graph_svg": arch_31_fixed_vs_variable_cost_graph_svg,
    "32_total_cost_formula_calc": arch_32_total_cost_formula_calc,
    "33_cost_per_item_unit_calculation": arch_33_cost_per_item_unit_calculation,
    "34_selling_price_formula_meaning": arch_34_selling_price_formula_meaning,
    "35_fudge_profit_target_selling_price": arch_35_fudge_profit_target_selling_price,
    "36_markup_from_cost_and_selling_price": arch_36_markup_from_cost_and_selling_price,
    "37_percentage_markup_on_cost_pricing": arch_37_percentage_markup_on_cost_pricing,
    "38_herb_gifts_entrepreneurs_day_budget_table": arch_38_herb_gifts_entrepreneurs_day_budget_table,
    "39_bookmarks_cards_budget_surplus_table": arch_39_bookmarks_cards_budget_surplus_table,
    "40_budget_revision_when_costs_rise": arch_40_budget_revision_when_costs_rise,
    "41_advertising_channel_cost_efficiency_svg": arch_41_advertising_channel_cost_efficiency_svg,
    "42_display_stand_budget_fixed_vs_variable_table": arch_42_display_stand_budget_fixed_vs_variable_table,
    "43_breakeven_covering_fixed_costs": arch_43_breakeven_covering_fixed_costs,
    "44_budget_deficit_prevention_scenario": arch_44_budget_deficit_prevention_scenario,
    "45_compilation_of_business_portfolio": arch_45_compilation_of_business_portfolio,
    "46_comparing_competing_business_ideas_table": arch_46_comparing_competing_business_ideas_table,
    "47_rural_recycling_microenterprise_costing": arch_47_rural_recycling_microenterprise_costing,
    "48_matching_startup_terms_exam_matrix": arch_48_matching_startup_terms_exam_matrix,
    "49_pricing_volume_vs_margin_tradeoff": arch_49_pricing_volume_vs_margin_tradeoff,
    "50_comprehensive_business_startup_blueprint": arch_50_comprehensive_business_startup_blueprint,
}
