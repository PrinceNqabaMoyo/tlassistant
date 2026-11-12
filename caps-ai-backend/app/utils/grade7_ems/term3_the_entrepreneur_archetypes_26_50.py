"""Grade 7 EMS: Term 3 - The Entrepreneur Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/01. The entrepreneur.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List
from app.utils.ems_namelist import get_ems_scenario, RURAL_AREAS, URBAN_AREAS
from .term3_entrepreneurs_day_archetypes_01_25 import _mcq_q, _calc_q, _rubric_q, _svg_spec
from .term3_the_entrepreneur_archetypes_01_25 import _given, _req, _ledger


def arch_26_four_entrepreneurial_actions_cycle_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, item = sc["entrepreneur"], sc["item_sold"]
    cost = rng.choice([120, 150, 180])
    rev = cost + rng.choice([90, 110, 140])
    svg_body = (
        f'<text x="290" y="22" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">Four Entrepreneurial Actions ({item})</text>'
        f'<rect x="20" y="55" width="115" height="65" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="77" y="84" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e3a8a">1. Buying</text>'
        f'<text x="77" y="102" font-size="10" text-anchor="middle" fill="#1e40af">Inputs R{cost}</text>'
        f'<rect x="160" y="55" width="115" height="65" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="217" y="84" font-size="12" font-weight="bold" text-anchor="middle" fill="#78350f">2. Producing</text>'
        f'<text x="217" y="102" font-size="10" text-anchor="middle" fill="#92400e">Make {item}</text>'
        f'<rect x="300" y="55" width="115" height="65" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="357" y="84" font-size="12" font-weight="bold" text-anchor="middle" fill="#14532d">3. Selling</text>'
        f'<text x="357" y="102" font-size="10" text-anchor="middle" fill="#166534">Sales R{rev}</text>'
        f'<rect x="440" y="55" width="120" height="65" rx="8" fill="#f3e8ff" stroke="#7c3aed" stroke-width="2"/>'
        f'<text x="500" y="84" font-size="12" font-weight="bold" text-anchor="middle" fill="#4c1d95">4. Making Profit</text>'
        f'<text x="500" y="102" font-size="10" text-anchor="middle" fill="#5b21b6">Profit R{rev - cost}</text>'
    )
    prompt = (
        f"Study the four-stage entrepreneurial action diagram for {person}'s {item} venture (Inputs R{cost}, Sales R{rev}).\n\n"
        f"Which sequence lists the **four entrepreneurial actions** to earn money?"
    )
    correct = "Buying goods or raw materials -> Producing goods -> Selling goods or services -> Making a profit"
    distractors = [
        "Making a profit -> Paying wages -> Buying raw materials -> Closing the stall",
        "Selling imaginary goods -> Paying taxes -> Buying inputs next month",
        "Borrowing money -> Spending profit personally -> Advertising -> Researching afterwards",
    ]
    sol = (
        f"Step 1: Recall the 4 entrepreneurial actions:\n"
        f"1. Buying raw materials (R{cost}) -> 2. Producing {item} -> 3. Selling (R{rev}) -> 4. Making a profit (R{rev - cost})."
    )
    return _mcq_q(
        rng, f"g7_ent_26_{rng.randint(100000, 999999)}", "26_four_entrepreneurial_actions_cycle_svg",
        "Four Entrepreneurial Actions Cycle", prompt, correct, distractors, sol,
        {"tier_1": "Read the four numbered boxes from left to right.",
         "tier_2": "Buying inputs -> Producing -> Selling -> Making profit.",
         "tier_3": correct},
        ["reverses_production_and_buying"],
        diagram_spec=_svg_spec(svg_body, 580, 150),
    )


def arch_27_buying_low_cost_vs_quality(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    good = rng.choice(["leather school belts", "fresh fruit smoothies", "cotton work aprons"])
    prompt = (
        f"When purchasing raw materials to produce {good} in {area}, what TWO rules must {person} balance carefully?"
    )
    correct = "Buy raw materials at a low-enough cost to still allow profit, while maintaining good enough quality so customers keep returning"
    distractors = [
        "Always buy the absolute cheapest faulty materials even if customers throw products away",
        "Pay the highest retail luxury price possible regardless of whether anyone buys the product",
        "Purchase raw materials only after selling finished goods to customers",
    ]
    sol = (
        f"Step 1: Buying action criteria (Doc Q5):\n"
        f"1. Cost control: inputs for {good} must be priced low enough to protect profit margins.\n"
        f"2. Quality control: buyers prefer durable, good-quality products over flimsy defective items."
    )
    return _mcq_q(
        rng, f"g7_ent_27_{rng.randint(100000, 999999)}", "27_buying_low_cost_vs_quality",
        "Buying Rule: Cost vs Quality", prompt, correct, distractors, sol,
        {"tier_1": "Think of both profitability AND customer satisfaction.",
         "tier_2": "Inputs must be affordable yet still deliver acceptable quality.",
         "tier_3": correct},
        ["sacrifices_quality_completely_for_cheapness"]
    )


def arch_28_raw_materials_unit_cost_comparison(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, sup1, sup2 = sc["entrepreneur"], sc["supplier"], sc["competitor"]
    u1, p1 = rng.choice([20, 25]), rng.choice([120, 150])
    u2, p2 = rng.choice([30, 40]), rng.choice([150, 160])
    unit_a = p1 // u1
    unit_b = p2 // u2
    # Ensure exact integer division with distinct unit prices
    u1, unit_a = rng.choice([(20, 7), (25, 8), (30, 6)])
    u2, unit_b = rng.choice([(40, 5), (50, 4)])
    p1, p2 = u1 * unit_a, u2 * unit_b
    better = sup2 if unit_b < unit_a else sup1
    diff = abs(unit_a - unit_b)
    prompt = (
        f"{person} compares fabric packs for sewing aprons:\n"
        f"- {sup1} sells a pack of {u1} sheets for R{p1}.\n"
        f"- {sup2} sells a bulk bale of {u2} sheets for R{p2}.\n\n"
        f"Which supplier offers the lower cost per sheet, and by how many Rand per sheet?"
    )
    ans = f"{better} by R{diff} per sheet (R{min(unit_a, unit_b)} vs R{max(unit_a, unit_b)})"
    sol = (
        f"Step 1: Unit price at {sup1} = R{p1} / {u1} = R{unit_a}/sheet.\n"
        f"Step 2: Unit price at {sup2} = R{p2} / {u2} = R{unit_b}/sheet.\n"
        f"Step 3: {better} is cheaper by R{diff} per sheet."
    )
    return _calc_q(
        rng, f"g7_ent_28_{rng.randint(100000, 999999)}", "28_raw_materials_unit_cost_comparison",
        "Comparing Bulk Raw Material Unit Costs", prompt, ans, sol,
        {"tier_1": "Compare price PER sheet, not total pack price!",
         "tier_2": f"Divide R{p1} by {u1} and R{p2} by {u2}.",
         "tier_3": ans},
        ["compares_pack_totals_ignoring_quantities"]
    )


def arch_29_producing_action_value_addition(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    flour_c = rng.choice([45, 55, 65])
    yeast_oil = rng.choice([25, 35])
    loaves = rng.choice([12, 15, 18])
    price_loaf = rng.choice([12, 14, 15])
    raw_tot = flour_c + yeast_oil
    output_val = loaves * price_loaf
    val_added = output_val - raw_tot
    prompt = (
        f"Through the **producing** action, {person} combines R{flour_c} of flour and R{yeast_oil} of yeast/oil to bake {loaves} loaves "
        f"sold for R{price_loaf} per loaf.\n\n"
        f"Calculate the **value added** (Finished Sales Value minus Raw Material Cost)."
    )
    ans = f"R{val_added}"
    sol = (
        f"Step 1: Raw material cost = R{flour_c} + R{yeast_oil} = R{raw_tot}.\n"
        f"Step 2: Finished loaves market value = {loaves} * R{price_loaf} = R{output_val}.\n"
        f"Step 3: Value added by production = R{output_val} - R{raw_tot} = R{val_added}."
    )
    return _calc_q(
        rng, f"g7_ent_29_{rng.randint(100000, 999999)}", "29_producing_action_value_addition",
        "Production and Value Addition", prompt, ans, sol,
        {"tier_1": "Compare finished goods total revenue against total raw input costs.",
         "tier_2": f"({loaves} * R{price_loaf}) - (R{flour_c} + R{yeast_oil}).",
         "tier_3": f"R{val_added}"},
        ["adds_raw_cost_to_output_value"]
    )


def arch_30_outsourcing_definition_and_examples(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, biz = sc["entrepreneur"], sc["business_type"]
    task = rng.choice([
        "hiring an independent local courier service to deliver customer parcels",
        "paying an external printing shop to bind full-colour product brochures",
        "contracting an independent bookkeeper once a month to prepare tax filings",
    ])
    prompt = (
        f"To focus on core operations in {person}'s {biz}, the business arranges {task} instead of employing full-time internal staff for that task.\n\n"
        f"Which term defines assigning parts of a business's work to another person or external enterprise?"
    )
    correct = "Outsourcing"
    distractors = [
        "Bartering",
        "Sole proprietorship",
        "Mass consumption",
    ]
    sol = (
        f"Step 1: Curriculum definition (Doc Q10):\n"
        f"**Outsourcing** occurs when a business hands over specialised parts of its work ({task}) to another person or specialist company."
    )
    return _mcq_q(
        rng, f"g7_ent_30_{rng.randint(100000, 999999)}", "30_outsourcing_definition_and_examples",
        "Outsourcing in Entrepreneurship", prompt, correct, distractors, sol,
        {"tier_1": "Think of paying an 'outside' specialist to handle a support task.",
         "tier_2": "Giving work out to another person/business is called out...",
         "tier_3": correct},
        ["confuses_outsourcing_with_insourcing"]
    )


def arch_31_outsourcing_cost_comparison_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    deliveries = rng.choice([40, 50, 60])
    in_fuel = rng.choice([400, 500])
    in_driver = rng.choice([1200, 1400])
    tot_in = in_fuel + in_driver
    per_del = rng.choice([22, 25, 28])
    tot_out = deliveries * per_del
    saving = tot_in - tot_out
    headers = ["Delivery Option", "Cost Components", "Monthly Total (R)"]
    rows = [
        [_given("r0_c0", "In-House Moped Delivery"), _given("r0_c1", f"Fuel R{in_fuel} + Rider R{in_driver}"), _req("r0_c2", str(tot_in))],
        [_given("r1_c0", "Outsourced Courier"), _given("r1_c1", f"{deliveries} drops @ R{per_del}"), _req("r1_c2", str(tot_out))],
        [_given("r2_c0", "Monthly Savings by Outsourcing"), _given("r2_c1", "In-House minus Outsourced"), _req("r2_c2", str(saving))],
    ]
    cmap = {"r0_c2": str(tot_in), "r1_c2": str(tot_out), "r2_c2": str(saving)}
    chints = {"r0_c2": f"{in_fuel}+{in_driver}", "r1_c2": f"{deliveries}*{per_del}", "r2_c2": "Row 1 minus Row 2"}
    sol = f"1. In-house = R{in_fuel}+R{in_driver}=R{tot_in}\n2. Outsourced = {deliveries}*R{per_del}=R{tot_out}\n3. Savings = R{tot_in}-R{tot_out}=R{saving}."
    return _ledger(
        f"g7_ent_31_{rng.randint(100000, 999999)}", "31_outsourcing_cost_comparison_table",
        "Outsourcing vs In-House Cost Analysis",
        f"{person} delivers {deliveries} food parcels per month. Complete the comparison table to calculate how much outsourcing saves monthly.",
        headers, rows, cmap, chints, f"In-House = R{tot_in}; Outsourced = R{tot_out}; Savings = R{saving}", sol,
        {"tier_1": "Calculate both delivery option totals first.",
         "tier_2": f"Row 1: {in_fuel}+{in_driver}; Row 2: {deliveries}*{per_del}; subtract to find savings.",
         "tier_3": f"In-house {tot_in}, Outsourced {tot_out}, Saving {saving}."},
        ["ignores_labour_cost_of_inhouse_option"], marks=6,
    )


def arch_32_selling_action_visibility_and_demand(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    stock = rng.choice([60, 80, 100])
    prompt = (
        f"{person} crafts {stock} high-quality woven baskets, packs them neatly in a back storeroom, creates zero signs, "
        f"and tells nobody the price.\n\n"
        f"According to curriculum guidelines on the **selling** action (Doc Q6), what TWO essential steps prevent goods from sitting unsold?"
    )
    correct = "Conducting market research into customer wants plus actively informing potential buyers about the product, location, and competitors"
    distractors = [
        "Hiding inventory indoors until baskets become antiques",
        "Making goods first and checking if anyone wants them three years later",
        "Raising prices secretly every hour without informing shoppers",
    ]
    sol = (
        f"Step 1: Selling action principles:\n"
        f"Even {stock} quality baskets will not sell if nobody knows about them or nobody wants them. Market research, competitor awareness, "
        f"and visible promotion are vital."
    )
    return _mcq_q(
        rng, f"g7_ent_32_{rng.randint(100000, 999999)}", "32_selling_action_visibility_and_demand",
        "Why Products Fail to Sell", prompt, correct, distractors, sol,
        {"tier_1": "Ask: can shoppers buy goods they do not even know exist?",
         "tier_2": "Combine pre-launch demand research with visible customer communication.",
         "tier_3": correct},
        ["assumes_good_product_sells_without_marketing"]
    )


def arch_33_making_profit_covering_overheads(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    sales = rng.choice([2400, 3200, 4000])
    materials = rng.choice([900, 1100, 1300])
    rent_elec = rng.choice([450, 550, 650])
    tot_cost = materials + rent_elec
    profit = sales - tot_cost
    prompt = (
        f"Over one week, {person}'s bakery records R{sales:,} in bread sales. Flour/ingredients cost R{materials:,} "
        f"and electricity plus kiosk rental cost R{rent_elec:,}.\n\n"
        f"Calculate {person}'s **profit** after covering all costs."
    )
    ans = f"R{profit:,}"
    sol = (
        f"Step 1: Total Costs = Materials (R{materials:,}) + Electricity/Rental (R{rent_elec:,}) = R{tot_cost:,}.\n"
        f"Step 2: Profit = Sales Revenue (R{sales:,}) - Total Costs (R{tot_cost:,}) = R{profit:,}."
    )
    return _calc_q(
        rng, f"g7_ent_33_{rng.randint(100000, 999999)}", "33_making_profit_covering_overheads",
        "Profit After Materials and Overheads", prompt, ans, sol,
        {"tier_1": "Remember to deduct BOTH raw materials AND electricity/rent!",
         "tier_2": f"Total costs = R{materials:,} + R{rent_elec:,}.",
         "tier_3": ans},
        ["subtracts_materials_only_forgetting_overheads"]
    )


def arch_34_reinvesting_profits_growth_rule(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, biz = sc["entrepreneur"], sc["business_type"]
    prof = rng.choice([1800, 2400, 3000])
    prompt = (
        f"{person}'s {biz} finishes the month with R{prof:,} in net profit (Doc Q7).\n\n"
        f"What is one crucial action every growth-oriented entrepreneur should take with part of these profits?"
    )
    correct = "Reinvest (plough back) a portion of the profit into the business—such as better equipment or bulk stock—so the venture can grow"
    distractors = [
        "Spend 100% immediately on luxury personal wants, leaving zero cash for extra stock",
        "Give away business equipment so turnover stays capped forever",
        "Destroy cash receipts to avoid tracking profit next month",
    ]
    sol = (
        f"Step 1: Profit reinvestment principle:\n"
        f"Ploughing part of the R{prof:,} profit back into bulk materials, upgraded tools, or marketing grows capacity and future profit."
    )
    return _mcq_q(
        rng, f"g7_ent_34_{rng.randint(100000, 999999)}", "34_reinvesting_profits_growth_rule",
        "Reinvesting Profits for Growth", prompt, correct, distractors, sol,
        {"tier_1": "How can R" + f"{prof:,}" + " profit help the business expand next month?",
         "tier_2": "Reinvesting profits into stock/assets fuels expansion.",
         "tier_3": correct},
        ["treats_profit_solely_as_personal_spending"]
    )


def arch_35_profit_retention_and_drawings_table(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    m1_p = rng.choice([1000, 1200, 1500])
    m2_p = rng.choice([1400, 1800, 2000])
    reinv_pct = rng.choice([40, 50])
    r1 = m1_p * reinv_pct // 100
    d1 = m1_p - r1
    r2 = m2_p * reinv_pct // 100
    d2 = m2_p - r2
    tot_reinv = r1 + r2
    headers = ["Month", "Net Profit (R)", f"Reinvested ({reinv_pct}%) (R)", "Owner Drawings (R)"]
    rows = [
        [_given("r0_c0", "Month 1"), _given("r0_c1", str(m1_p)), _req("r0_c2", str(r1)), _req("r0_c3", str(d1))],
        [_given("r1_c0", "Month 2"), _given("r1_c1", str(m2_p)), _req("r1_c2", str(r2)), _req("r1_c3", str(d2))],
        [_given("r2_c0", "Total Retained Growth Capital"), _given("r2_c1", f"{m1_p + m2_p}"), _req("r2_c2", str(tot_reinv)), _given("r2_c3", str(d1 + d2))],
    ]
    cmap = {"r0_c2": str(r1), "r0_c3": str(d1), "r1_c2": str(r2), "r1_c3": str(d2), "r2_c2": str(tot_reinv)}
    chints = {
        "r0_c2": f"{reinv_pct}% of {m1_p}", "r0_c3": f"{m1_p} minus reinvested",
        "r1_c2": f"{reinv_pct}% of {m2_p}", "r1_c3": f"{m2_p} minus reinvested",
        "r2_c2": "Add Month 1 and Month 2 reinvested.",
    }
    sol = f"1. Month 1: Reinv=R{r1}, Draw=R{d1}\n2. Month 2: Reinv=R{r2}, Draw=R{d2}\n3. Total Retained Growth Capital = R{tot_reinv}."
    return _ledger(
        f"g7_ent_35_{rng.randint(100000, 999999)}", "35_profit_retention_and_drawings_table",
        "Profit Retention vs Drawings Schedule",
        f"{person} retains {reinv_pct}% of monthly Net Profit to expand the business and withdraws the rest as Owner Drawings. Complete the allocation table.",
        headers, rows, cmap, chints, f"Total Growth Capital Reinvested = R{tot_reinv}", sol,
        {"tier_1": f"Multiply each month's Net Profit by {reinv_pct}% to get Reinvested.",
         "tier_2": "Subtract Reinvested from Net Profit to find Owner Drawings.",
         "tier_3": f"M1({r1},{d1}), M2({r2},{d2}), Total Reinvested {tot_reinv}."},
        ["confuses_drawings_with_reinvestment"], marks=10,
    )


def arch_36_entrepreneurs_driving_economic_growth(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    area = sc["area"]
    prompt = (
        f"Using South African communities such as {area} as context, explain THREE ways entrepreneurs contribute directly to **economic growth**. (3 marks)"
    )
    sample = (
        "1. Innovation: Entrepreneurs introduce new ideas, goods, services, and practical technology.\n"
        "2. Market expansion: They open new local and export markets where goods circulate.\n"
        "3. Employment & output: Growing firms create jobs, pay wages, and increase overall production."
    )
    pts = [
        "Introduce new ideas, products, services, or technology [1 mark]",
        "Create and expand markets [1 mark]",
        "Generate new jobs and higher household spending/production [1 mark]",
    ]
    sol = "Marking Rubric (3 marks):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_ent_36_{rng.randint(100000, 999999)}", "36_entrepreneurs_driving_economic_growth",
        "How Entrepreneurs Drive Economic Growth", prompt, sample, pts, sol,
        {"tier_1": "Think about innovation, markets, and jobs (Doc Q11).",
         "tier_2": "Cover new ideas/technology, new markets, and employment growth.",
         "tier_3": sample},
        ["omits_innovation_or_market_creation"], marks=3,
    )


def arch_37_fighting_unemployment_and_inequality(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    staff = rng.choice([3, 4, 5])
    prompt = (
        f"{person}'s growing enterprise in {area} employs {staff} previously unemployed youth. "
        f"Explain TWO ways supporting small entrepreneurs helps reduce South Africa's high unemployment and socio-economic inequality. (4 marks)"
    )
    sample = (
        f"1. Job creation & self-employment: Owners employ themselves and hire others (like {staff} local youth), lifting families out of joblessness.\n"
        f"2. Local income circulation & empowerment: Wages paid stay in {area}, building SMME ownership and reducing historic wealth gaps."
    )
    pts = [
        "Direct job creation & self-employment reducing dependency [2 marks]",
        "Wage income & local wealth circulation empowering disadvantaged communities [2 marks]",
    ]
    sol = "Marking Rubric (4 marks):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_ent_37_{rng.randint(100000, 999999)}", "37_fighting_unemployment_and_inequality",
        "Reducing Unemployment and Imbalances", prompt, sample, pts, sol,
        {"tier_1": "Connect small business employment to household income and community upliftment.",
         "tier_2": "Explain both jobs created and how wages empower local households.",
         "tier_3": sample},
        ["ignores_socioeconomic_multiplier"]
    )


def arch_38_poverty_line_household_threshold(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    area = sc["area"]
    members = rng.choice([4, 5])
    pov_pp = rng.choice([760, 796])
    threshold = members * pov_pp
    prompt = (
        f"In a survey of {area}, economists apply a food-and-essentials **poverty line** benchmark of R{pov_pp} per person per month "
        f"(R{threshold:,} for a household of {members}).\n\n"
        f"What does the term **poverty line** accurately represent?"
    )
    correct = "The minimum level of income needed to secure basic survival necessities (adequate food, clean water, essential shelter)"
    distractors = [
        "The top income tax rate paid by commercial banks in Gauteng",
        "A fence separating rural farms from metropolitan shopping malls",
        "The total annual advertising budget of multinational factories",
    ]
    sol = (
        f"Step 1: Define poverty line:\n"
        f"The poverty line (here R{pov_pp}/person, R{threshold:,} for {members} people) measures the minimum monthly income needed for essential survival needs."
    )
    return _mcq_q(
        rng, f"g7_ent_38_{rng.randint(100000, 999999)}", "38_poverty_line_household_threshold",
        "Poverty Line Benchmark Definition", prompt, correct, distractors, sol,
        {"tier_1": "Think about minimum survival income for food and shelter.",
         "tier_2": "Families below this threshold cannot afford basic necessities.",
         "tier_3": correct},
        ["confuses_poverty_line_with_tax_or_geography"]
    )


def arch_39_entrepreneurial_cash_cycle_ledger(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, item = sc["entrepreneur"], sc["item_sold"]
    qty = rng.choice([40, 50])
    buy_raw = qty * rng.choice([4, 5])
    pack_cost = rng.choice([30, 40])
    tot_buy_prod = buy_raw + pack_cost
    sell_price = rng.choice([9, 10, 11])
    rev = qty * sell_price
    profit = rev - tot_buy_prod
    headers = ["Entrepreneurial Action", "Details", "Cash Flow / Result (R)"]
    rows = [
        [_given("r0_c0", "1. Buying Raw Materials"), _given("r0_c1", f"Bulk supplies for {qty} {item}"), _given("r0_c2", str(buy_raw))],
        [_given("r1_c0", "2. Producing & Packaging"), _given("r1_c1", "Bags, labels & fuel"), _given("r1_c2", str(pack_cost))],
        [_given("r2_c0", "Total Production Cost"), _given("r2_c1", "Buying + Producing costs"), _req("r2_c2", str(tot_buy_prod))],
        [_given("r3_c0", "3. Selling Output"), _given("r3_c1", f"{qty} units @ R{sell_price}"), _req("r3_c2", str(rev))],
        [_given("r4_c0", "4. Making a Profit"), _given("r4_c1", "Selling minus Total Cost"), _req("r4_c2", str(profit))],
    ]
    cmap = {"r2_c2": str(tot_buy_prod), "r3_c2": str(rev), "r4_c2": str(profit)}
    chints = {"r2_c2": f"{buy_raw} + {pack_cost}", "r3_c2": f"{qty} * {sell_price}", "r4_c2": "Selling minus Total Cost"}
    sol = f"1. Total Cost = R{buy_raw}+R{pack_cost}=R{tot_buy_prod}\n2. Selling Revenue = {qty}*R{sell_price}=R{rev}\n3. Net Profit = R{rev}-R{tot_buy_prod}=R{profit}."
    return _ledger(
        f"g7_ent_39_{rng.randint(100000, 999999)}", "39_entrepreneurial_cash_cycle_ledger",
        "Buying-Producing-Selling-Profit Table",
        f"Track all four entrepreneurial actions for {person}'s batch of {qty} {item} by filling in the three blank Rand figures.",
        headers, rows, cmap, chints, f"Total Cost = R{tot_buy_prod}; Sales = R{rev}; Profit = R{profit}", sol,
        {"tier_1": "Add Buying + Packaging first, then compute Selling Income.",
         "tier_2": f"Sales = {qty} * R{sell_price}. Subtract Total Cost for Profit.",
         "tier_3": f"Cost {tot_buy_prod}, Sales {rev}, Profit {profit}."},
        ["confuses_selling_revenue_with_profit"], marks=6,
    )


def arch_40_daily_hotdog_entrepreneur_cost_profit(rng: random.Random) -> Dict[str, Any]:
    # Grounded directly in Doc Exam2 Q6
    qty = rng.choice([20, 30, 40])
    sp = rng.choice([10, 12])
    roll, marg, sauce, vienna, wax = 1.50, 0.50, 0.50, rng.choice([3.00, 3.50]), 0.50
    unit_cost = roll + marg + sauce + vienna + wax
    tot_inc = int(qty * sp)
    tot_exp = int(round(qty * unit_cost))
    profit = tot_inc - tot_exp
    headers = ["Hotdog Financial Metric", "Calculation Basis", "Amount (R)"]
    rows = [
        [_given("r0_c0", "Daily Sales Income"), _given("r0_c1", f"{qty} hotdogs @ R{sp}"), _req("r0_c2", str(tot_inc))],
        [_given("r1_c0", "Ingredient & Wrap Cost per Hotdog"), _given("r1_c1", f"Roll R1,50 + Marg 50c + Sauce 50c + Vienna R{vienna:.2f} + Wax 50c".replace(".", ",")), _req("r1_c2", f"{unit_cost:.2f}".replace(".", ","))],
        [_given("r2_c0", "Daily Total Expenses"), _given("r2_c1", f"{qty} hotdogs * unit cost"), _req("r2_c2", str(tot_exp))],
        [_given("r3_c0", "Daily Net Profit"), _given("r3_c1", "Daily Income - Daily Expenses"), _req("r3_c2", str(profit))],
    ]
    cmap = {"r0_c2": str(tot_inc), "r1_c2": f"{unit_cost:.2f}".replace(".", ","), "r2_c2": str(tot_exp), "r3_c2": str(profit)}
    chints = {"r0_c2": f"{qty}*{sp}", "r1_c2": "Sum all 5 unit ingredients in R (use comma)", "r2_c2": f"{qty}*unit cost", "r3_c2": "Income - Expenses"}
    sol = f"1. Income={qty}*R{sp}=R{tot_inc}\n2. Unit cost=R{unit_cost:.2f}\n3. Total Exp={qty}*R{unit_cost:.2f}=R{tot_exp}\n4. Daily Profit=R{tot_inc}-R{tot_exp}=R{profit}."
    return _ledger(
        f"g7_ent_40_{rng.randint(100000, 999999)}", "40_daily_hotdog_entrepreneur_cost_profit",
        "Hotdog Venture Daily Income, Expenses & Profit",
        f"Complete the daily summary table for selling {qty} hotdogs at R{sp} each using the listed ingredient costs.",
        headers, rows, cmap, chints, f"Income = R{tot_inc}; Unit Cost = R{unit_cost:.2f}; Expenses = R{tot_exp}; Profit = R{profit}", sol,
        {"tier_1": "Convert 50 cents to R0,50 carefully when summing the 5 ingredients.",
         "tier_2": f"Unit cost * {qty} gives Total Expenses; subtract from {qty} * R{sp}.",
         "tier_3": f"Inc {tot_inc}, Unit {cmap['r1_c2']}, Exp {tot_exp}, Profit {profit}."},
        ["adds_cents_as_whole_rands"], marks=8,
    )


def arch_41_monthly_four_market_days_profit(rng: random.Random) -> Dict[str, Any]:
    # Grounded directly in Doc Exam2 Q6.4-6.5
    daily_inc = rng.choice([300, 360, 420])
    daily_ing = rng.choice([180, 210, 240])
    stall_rent = rng.choice([5, 10, 15])
    days = 4
    m_inc = days * daily_inc
    m_exp = days * (daily_ing + stall_rent)
    m_prof = m_inc - m_exp
    headers = ["Monthly Component (4 Market Days)", "Per-Day Rate (R)", "Monthly Total (R)"]
    rows = [
        [_given("r0_c0", "Monthly Gross Income"), _given("r0_c1", str(daily_inc)), _req("r0_c2", str(m_inc))],
        [_given("r1_c0", "Monthly Ingredients"), _given("r1_c1", str(daily_ing)), _given("r1_c2", str(days * daily_ing))],
        [_given("r2_c0", "Monthly Stall Rental"), _given("r2_c1", str(stall_rent)), _given("r2_c2", str(days * stall_rent))],
        [_given("r3_c0", "Total Monthly Expenses"), _given("r3_c1", f"{daily_ing + stall_rent}"), _req("r3_c2", str(m_exp))],
        [_given("r4_c0", "Monthly Net Profit"), _given("r4_c1", f"{daily_inc - daily_ing - stall_rent}"), _req("r4_c2", str(m_prof))],
    ]
    cmap = {"r0_c2": str(m_inc), "r3_c2": str(m_exp), "r4_c2": str(m_prof)}
    chints = {"r0_c2": f"4 * {daily_inc}", "r3_c2": "Add monthly ingredients + monthly rental", "r4_c2": "Monthly Income - Total Monthly Expenses"}
    sol = f"1. Monthly Income = 4*R{daily_inc}=R{m_inc}\n2. Monthly Expenses = 4*(R{daily_ing}+R{stall_rent})=R{m_exp}\n3. Monthly Profit = R{m_inc}-R{m_exp}=R{m_prof}."
    return _ledger(
        f"g7_ent_41_{rng.randint(100000, 999999)}", "41_monthly_four_market_days_profit",
        "Monthly Scaling with Fixed Stall Rent",
        f"Suppose there are {days} school market days per month, and each time it costs R{stall_rent} to rent a stall on top of R{daily_ing} ingredients. Complete the monthly totals.",
        headers, rows, cmap, chints, f"Monthly Income = R{m_inc}; Monthly Expenses = R{m_exp}; Monthly Profit = R{m_prof}", sol,
        {"tier_1": "Multiply daily sales by 4 and include all 4 days of stall rent.",
         "tier_2": f"Expenses = R{days*daily_ing} + R{days*stall_rent}.",
         "tier_3": f"Inc {m_inc}, Exp {m_exp}, Profit {m_prof}."},
        ["omits_stall_rental_across_four_days"], marks=6,
    )


def arch_42_assets_liabilities_expenses_capital_classification(rng: random.Random) -> Dict[str, Any]:
    # Grounded directly in Doc Exam15 Q1.1
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    equip_v = rng.choice([4500, 6000])
    loan_v = rng.choice([3000, 5000])
    util_v = rng.choice([450, 650])
    cap_v = rng.choice([10000, 12000])
    headers = ["Business Item", "Example / Amount", "Correct Accounting Term (Asset / Liability / Expense / Capital)"]
    rows = [
        [_given("r0_c0", "Baking oven & cash in bank"), _given("r0_c1", f"R{equip_v:,}"), _req("r0_c2", "Asset")],
        [_given("r1_c0", "Business start-up loan owed to uncle"), _given("r1_c1", f"R{loan_v:,}"), _req("r1_c2", "Liability")],
        [_given("r2_c0", "Monthly water, electricity & stationery"), _given("r2_c1", f"R{util_v}"), _req("r2_c2", "Expense")],
        [_given("r3_c0", "Money invested by owner to launch business"), _given("r3_c1", f"R{cap_v:,}"), _req("r3_c2", "Capital")],
    ]
    cmap = {"r0_c2": "Asset", "r1_c2": "Liability", "r2_c2": "Expense", "r3_c2": "Capital"}
    chints = {
        "r0_c2": "Possession owned by the business with monetary value.",
        "r1_c2": "Amount/debt owed to an outside lender.",
        "r2_c2": "Day-to-day running costs paid out.",
        "r3_c2": "Owner's money/property invested to run the venture.",
    }
    sol = "1. Owned oven/cash = Asset\n2. Unpaid loan owed = Liability\n3. Water/electricity/stationery = Expense\n4. Owner launch funds = Capital."
    return _ledger(
        f"g7_ent_42_{rng.randint(100000, 999999)}", "42_assets_liabilities_expenses_capital_classification",
        "Classifying Asset, Liability, Expense & Capital",
        f"Classify each financial item from {person}'s enterprise by typing exactly one term per cell: Asset, Liability, Expense, or Capital.",
        headers, rows, cmap, chints, "Asset; Liability; Expense; Capital", sol,
        {"tier_1": "Assets = owned; Liabilities = owed; Expenses = running costs; Capital = owner investment.",
         "tier_2": "Check whether money flows in permanently from the owner (Capital) or is owed back (Liability).",
         "tier_3": "1. Asset, 2. Liability, 3. Expense, 4. Capital."},
        ["confuses_capital_and_liability"], marks=8,
    )


def arch_43_rural_service_gap_entrepreneurship(rng: random.Random) -> Dict[str, Any]:
    rural = rng.choice(RURAL_AREAS)
    person = rng.choice(["Aluwani", "Thabo", "Naledi", "Siyanda"])
    km = rng.choice([25, 35, 45])
    prompt = (
        f"In {rural}, storm-damaged power lines leave households without electricity and pensioners must travel {km} km to town to charge phones or buy prepaid electricity.\n\n"
        f"How does {person}'s solar phone-charging and water kiosk demonstrate context-sensitive rural entrepreneurship?"
    )
    correct = f"It solves critical local distance/infrastructure barriers in {rural}, saving residents travel money while building sustainable local cash flow"
    distractors = [
        f"It ignores {rural}'s power outages and relies entirely on mains grid sockets",
        "It requires customers to pay expensive international shipping fees",
        "It shifts jobs away from the village into distant city malls",
    ]
    sol = (
        f"Step 1: Rural opportunity analysis:\n"
        f"Solving {km}-km travel burdens and power interruptions directly helps pensioners and learners in {rural} while generating steady demand."
    )
    return _mcq_q(
        rng, f"g7_ent_43_{rng.randint(100000, 999999)}", "43_rural_service_gap_entrepreneurship",
        "Rural Community Entrepreneurship", prompt, correct, distractors, sol,
        {"tier_1": "Look at what cost and travel headache the solar kiosk removes for villagers.",
         "tier_2": f"Eliminating {km} km trips gives buyers real value right at home.",
         "tier_3": correct},
        ["ignores_rural_infrastructure_opportunities"]
    )


def arch_44_urban_township_enterprise_dynamics(rng: random.Random) -> Dict[str, Any]:
    urban = rng.choice(URBAN_AREAS)
    person = rng.choice(["Bongani", "Zanele", "Tariq", "Palesa"])
    prompt = (
        f"{person} runs a bustling takeaway stall near a busy taxi rank in {urban}. Foot traffic surges at month-end, "
        f"yet profits shrink when stock transport fees and electricity tariffs climb.\n\n"
        f"What key urban micro-enterprise discipline must {person} prioritise?"
    )
    correct = "Balancing peak month-end stock volumes carefully against fluctuating input, transport, and tariff costs plus nearby rival prices"
    distractors = [
        "Closing every month-end payday when commuters carry the most money",
        "Assuming high commuter crowds mean costs never need tracking",
        "Never adjusting stock levels between mid-month quiet days and month-end rush",
    ]
    sol = (
        f"Step 1: Township commuter rank economics in {urban}:\n"
        f"High competition and fluctuating tariffs mean success requires matching month-end demand peaks while strictly controlling stock transport and utility costs."
    )
    return _mcq_q(
        rng, f"g7_ent_44_{rng.randint(100000, 999999)}", "44_urban_township_enterprise_dynamics",
        "Urban Township Micro-Enterprise Management", prompt, correct, distractors, sol,
        {"tier_1": "Look at the twin urban realities: month-end demand spikes + rising operating costs.",
         "tier_2": "Combine demand forecasting with strict expense monitoring.",
         "tier_3": correct},
        ["neglects_operating_cost_escalation"]
    )


def arch_45_risk_vs_reward_ventures_chart_svg(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    p_a, c_a = rng.choice([300, 350]), rng.choice([2500, 3000])
    p_b, c_b = rng.choice([900, 1100]), rng.choice([450, 550])
    p_c, c_c = rng.choice([120, 150]), rng.choice([200, 250])
    svg_body = (
        f'<text x="290" y="22" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">3 Venture Ideas: Monthly Profit vs Capital Needed</text>'
        f'<rect x="55" y="60" width="140" height="105" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="125" y="88" font-size="11" font-weight="bold" text-anchor="middle" fill="#7f1d1d">Idea A: Arcade</text>'
        f'<text x="125" y="110" font-size="11" text-anchor="middle" fill="#991b1b">Capital: R{c_a}</text>'
        f'<text x="125" y="130" font-size="11" text-anchor="middle" fill="#991b1b">Profit: R{p_a}/mo</text>'
        f'<rect x="220" y="60" width="140" height="105" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="290" y="88" font-size="11" font-weight="bold" text-anchor="middle" fill="#14532d">Idea B: Tuck Kiosk</text>'
        f'<text x="290" y="110" font-size="11" text-anchor="middle" fill="#166534">Capital: R{c_b}</text>'
        f'<text x="290" y="130" font-size="11" text-anchor="middle" fill="#166534">Profit: R{p_b}/mo</text>'
        f'<rect x="385" y="60" width="140" height="105" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="455" y="88" font-size="11" font-weight="bold" text-anchor="middle" fill="#78350f">Idea C: Car Mats</text>'
        f'<text x="455" y="110" font-size="11" text-anchor="middle" fill="#92400e">Capital: R{c_c}</text>'
        f'<text x="455" y="130" font-size="11" text-anchor="middle" fill="#92400e">Profit: R{p_c}/mo</text>'
    )
    prompt = (
        f"Study the comparison chart of three startup ideas for {person}, who saved R600.\n\n"
        f"Which venture gives the best combination of **affordability within R600 savings** and **monthly net profit**?"
    )
    correct = f"Idea B (Tuck Kiosk): fits within R600 savings (R{c_b} capital) and yields the highest monthly profit (R{p_b}/mo)"
    distractors = [
        f"Idea A (Arcade): costs R{c_a} (unaffordable) and yields only R{p_a}/mo",
        f"Idea C (Car Mats): earns R{p_c}/mo which beats R{p_b}/mo",
        "None of the ventures generate positive monthly earnings",
    ]
    sol = (
        f"Step 1: Compare Capital vs Savings (R600):\n"
        f"Idea A (R{c_a}) exceeds savings. Between Idea B (R{c_b}) and Idea C (R{c_c}), Idea B earns R{p_b}/mo vs Idea C's R{p_c}/mo."
    )
    return _mcq_q(
        rng, f"g7_ent_45_{rng.randint(100000, 999999)}", "45_risk_vs_reward_ventures_chart_svg",
        "Evaluating Capital Risk vs Return Chart", prompt, correct, distractors, sol,
        {"tier_1": "Filter out options needing more than R600 capital first!",
         "tier_2": f"Compare Idea B (R{p_b}) vs Idea C (R{p_c}).",
         "tier_3": correct},
        ["ignores_capital_budget_constraint"],
        diagram_spec=_svg_spec(svg_body, 580, 190),
    )


def arch_46_startup_capital_sources_match(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    seed_amt = rng.choice([400, 600, 800])
    prompt = (
        f"{person} needs R{seed_amt} to launch a weekend car-wash startup but has no formal assets for commercial bank collateral.\n\n"
        f"Which startup financing path is most realistic for this early micro-enterprise?"
    )
    correct = "Personal savings combined with small interest-free/low-interest family support, growing gradually from reinvested weekly profits"
    distractors = [
        "Issuing multi-million Rand shares on the Johannesburg Stock Exchange tomorrow",
        "Borrowing R500 000 with zero trading records and zero repayment strategy",
        "Ignoring washing equipment costs completely",
    ]
    sol = (
        f"Step 1: Match funding stage:\n"
        f"Micro startups needing R{seed_amt} without collateral typically bootstrap with personal savings, family backing, and reinvested profits."
    )
    return _mcq_q(
        rng, f"g7_ent_46_{rng.randint(100000, 999999)}", "46_startup_capital_sources_match",
        "Appropriate Micro-Startup Funding", prompt, correct, distractors, sol,
        {"tier_1": "Consider realistic options for R" + f"{seed_amt}" + " without corporate collateral.",
         "tier_2": "Personal savings + family micro-loans fit micro-startups.",
         "tier_3": correct},
        ["confuses_micro_funding_with_stock_exchange"]
    )


def arch_47_quality_compromise_lost_sales_calc(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person = sc["entrepreneur"]
    prev_cust = rng.choice([50, 60])
    lost_cust = rng.choice([20, 25])
    remain = prev_cust - lost_cust
    profit_unit = rng.choice([6, 8])
    lost_profit = lost_cust * profit_unit
    prompt = (
        f"{person} switches to cheap stale rolls to save R1 per burger. Next week, {lost_cust} out of {prev_cust} regular buyers stop buying "
        f"(leaving only {remain} buyers). Each burger earned R{profit_unit} profit.\n\n"
        f"How much weekly profit did {person} **lose from upset returning customers**?"
    )
    ans = f"R{lost_profit}"
    sol = f"Lost weekly profit = {lost_cust} lost buyers * R{profit_unit} profit each = R{lost_profit}."
    return _calc_q(
        rng, f"g7_ent_47_{rng.randint(100000, 999999)}", "47_quality_compromise_lost_sales_calc",
        "Cost of Sacrificing Input Quality", prompt, ans, sol,
        {"tier_1": "Multiply lost buyers by the profit earned per burger.",
         "tier_2": f"{lost_cust} * R{profit_unit}.",
         "tier_3": f"R{lost_profit}"},
        ["ignores_repeat_customer_loss"]
    )


def arch_48_smme_household_support_multiplier(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    staff = rng.choice([4, 5, 6])
    dependants = rng.choice([3, 4])
    tot_supported = (staff + 1) * dependants
    prompt = (
        f"{person}'s growing catering business in {area} supports {person} (the owner) plus {staff} hired workers. "
        f"If each worker's income feeds a household of {dependants} people, how many community members benefit directly from household wages?"
    )
    ans = f"{tot_supported} people"
    sol = (
        f"Step 1: Total income earners = 1 owner + {staff} staff = {staff + 1} earners.\n"
        f"Step 2: Community members fed/supported = {staff + 1} * {dependants} = {tot_supported} people."
    )
    return _calc_q(
        rng, f"g7_ent_48_{rng.randint(100000, 999999)}", "48_smme_household_support_multiplier",
        "Entrepreneurial Job Multiplier Effect", prompt, ans, sol,
        {"tier_1": "Remember to include the entrepreneur (owner) as 1 earner alongside the hired staff!",
         "tier_2": f"({staff} + 1) * {dependants}.",
         "tier_3": ans},
        ["omits_owner_in_earner_count"]
    )


def arch_49_case_study_diagnosing_failing_venture(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    prompt = (
        f"{person}'s new kiosk in {area} failed after 3 weeks because: (a) {person} never asked neighbours what flavours they liked, "
        f"(b) {person} bought bruised fruit just because it was cheap, and (c) {person} spent every cent of Day 1 cash receipts personally.\n\n"
        f"Identify THREE entrepreneurial mistakes made and prescribe the matching fix for each. (6 marks)"
    )
    sample = (
        "1. Skipped market research -> Fix: survey buyers' preferred items and prices before purchasing stock.\n"
        "2. Compromised raw-material quality -> Fix: buy fresh, good-quality supplies at competitive wholesale prices.\n"
        "3. Spent gross cash personally without covering costs or reinvesting -> Fix: deduct costs first and reinvest profit back into stock."
    )
    pts = [
        "Diagnoses skipped market research + proposes customer survey fix [2 marks]",
        "Diagnoses poor input quality + proposes cost-quality balance fix [2 marks]",
        "Diagnoses draining receipts personally + proposes covering expenses and reinvesting profit [2 marks]",
    ]
    sol = "Marking Rubric (6 marks):\n" + "\n".join(f"- {p}" for p in pts)
    return _rubric_q(
        f"g7_ent_49_{rng.randint(100000, 999999)}", "49_case_study_diagnosing_failing_venture",
        "Diagnosing Venture Failures", prompt, sample, pts, sol,
        {"tier_1": "Examine problems (a), (b), and (c) one by one.",
         "tier_2": "Tie each symptom to market research, buying quality, and profit reinvestment.",
         "tier_3": sample},
        ["ignores_reinvestment_and_quality"], marks=6,
    )


def arch_50_comprehensive_entrepreneurship_ledger(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    person, area = sc["entrepreneur"], sc["area"]
    units = rng.choice([60, 80, 100])
    mat_u = rng.choice([4, 5])
    sp_u = rng.choice([10, 12])
    outsource_del = rng.choice([120, 150])
    raw_tot = units * mat_u
    tot_cost = raw_tot + outsource_del
    sales_tot = units * sp_u
    net_prof = sales_tot - tot_cost
    reinv = net_prof // 2 if net_prof % 2 == 0 else (net_prof + 1) // 2
    if net_prof % 2 != 0:
        outsource_del += 1
        tot_cost += 1
        net_prof -= 1
        reinv = net_prof // 2
    headers = ["Entrepreneurial Stage", "Activity Description", "Amount (R)"]
    rows = [
        [_given("r0_c0", "1. Buying Raw Materials"), _given("r0_c1", f"{units} raw kits @ R{mat_u}"), _req("r0_c2", str(raw_tot))],
        [_given("r1_c0", "2. Producing & Outsourced Delivery"), _given("r1_c1", "Assembled in-house + courier fee"), _given("r1_c2", str(outsource_del))],
        [_given("r2_c0", "Total Operating Cost"), _given("r2_c1", "Materials + Delivery"), _req("r2_c2", str(tot_cost))],
        [_given("r3_c0", "3. Selling Output"), _given("r3_c1", f"{units} finished goods @ R{sp_u}"), _req("r3_c2", str(sales_tot))],
        [_given("r4_c0", "4. Making Net Profit"), _given("r4_c1", "Sales - Total Operating Cost"), _req("r4_c2", str(net_prof))],
        [_given("r5_c0", "5. Business Reinvestment (50%)"), _given("r5_c1", "Ploughed back into growth"), _req("r5_c2", str(reinv))],
    ]
    cmap = {"r0_c2": str(raw_tot), "r2_c2": str(tot_cost), "r3_c2": str(sales_tot), "r4_c2": str(net_prof), "r5_c2": str(reinv)}
    chints = {
        "r0_c2": f"{units} * {mat_u}", "r2_c2": "Add rows 1 and 2",
        "r3_c2": f"{units} * {sp_u}", "r4_c2": "Sales minus Total Operating Cost",
        "r5_c2": "50% (half) of Net Profit",
    }
    sol = f"1. Raw={raw_tot}\n2. Total Cost={raw_tot}+{outsource_del}={tot_cost}\n3. Sales={sales_tot}\n4. Profit={net_prof}\n5. Reinvest (50%)={reinv}."
    return _ledger(
        f"g7_ent_50_{rng.randint(100000, 999999)}", "50_comprehensive_entrepreneurship_ledger",
        "Capstone Entrepreneurial Operations & Growth Ledger",
        f"Complete the full entrepreneurial operations summary for {person}'s SMME in {area}, calculating costs, sales, profit, and 50% growth reinvestment.",
        headers, rows, cmap, chints, f"Total Cost = R{tot_cost}; Sales = R{sales_tot}; Profit = R{net_prof}; Reinvest = R{reinv}", sol,
        {"tier_1": "Work downwards: raw materials -> total cost -> total sales -> profit -> 50% reinvestment.",
         "tier_2": f"Sales = {units}*R{sp_u}; deduct R{tot_cost} before taking 50%.",
         "tier_3": f"Raw {raw_tot}, Cost {tot_cost}, Sales {sales_tot}, Profit {net_prof}, Reinv {reinv}."},
        ["takes_half_of_sales_instead_of_profit"], marks=10,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_four_entrepreneurial_actions_cycle_svg": arch_26_four_entrepreneurial_actions_cycle_svg,
    "27_buying_low_cost_vs_quality": arch_27_buying_low_cost_vs_quality,
    "28_raw_materials_unit_cost_comparison": arch_28_raw_materials_unit_cost_comparison,
    "29_producing_action_value_addition": arch_29_producing_action_value_addition,
    "30_outsourcing_definition_and_examples": arch_30_outsourcing_definition_and_examples,
    "31_outsourcing_cost_comparison_table": arch_31_outsourcing_cost_comparison_table,
    "32_selling_action_visibility_and_demand": arch_32_selling_action_visibility_and_demand,
    "33_making_profit_covering_overheads": arch_33_making_profit_covering_overheads,
    "34_reinvesting_profits_growth_rule": arch_34_reinvesting_profits_growth_rule,
    "35_profit_retention_and_drawings_table": arch_35_profit_retention_and_drawings_table,
    "36_entrepreneurs_driving_economic_growth": arch_36_entrepreneurs_driving_economic_growth,
    "37_fighting_unemployment_and_inequality": arch_37_fighting_unemployment_and_inequality,
    "38_poverty_line_household_threshold": arch_38_poverty_line_household_threshold,
    "39_entrepreneurial_cash_cycle_ledger": arch_39_entrepreneurial_cash_cycle_ledger,
    "40_daily_hotdog_entrepreneur_cost_profit": arch_40_daily_hotdog_entrepreneur_cost_profit,
    "41_monthly_four_market_days_profit": arch_41_monthly_four_market_days_profit,
    "42_assets_liabilities_expenses_capital_classification": arch_42_assets_liabilities_expenses_capital_classification,
    "43_rural_service_gap_entrepreneurship": arch_43_rural_service_gap_entrepreneurship,
    "44_urban_township_enterprise_dynamics": arch_44_urban_township_enterprise_dynamics,
    "45_risk_vs_reward_ventures_chart_svg": arch_45_risk_vs_reward_ventures_chart_svg,
    "46_startup_capital_sources_match": arch_46_startup_capital_sources_match,
    "47_quality_compromise_lost_sales_calc": arch_47_quality_compromise_lost_sales_calc,
    "48_smme_household_support_multiplier": arch_48_smme_household_support_multiplier,
    "49_case_study_diagnosing_failing_venture": arch_49_case_study_diagnosing_failing_venture,
    "50_comprehensive_entrepreneurship_ledger": arch_50_comprehensive_entrepreneurship_ledger,
}
