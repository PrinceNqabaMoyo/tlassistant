from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

# CLUSTER 2: MASS & WEIGHT MEASUREMENT, SCALES & PRACTICAL COSTS (13 Archetypes)
# ==============================================================================

def _gen_meas_mass_scale_instrument_selection(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("accurately measuring 250 g of castor sugar for baking a sponge cake", "Digital kitchen scale", ["Bathroom spring scale", "Digital kitchen scale", "Weighbridge", "Baby balance"]),
        ("weighing an articulated heavy freight truck transporting bulk agricultural produce on the N4 highway", "Road weighbridge", ["Hanging spring balance", "Road weighbridge", "Digital kitchen scale", "Bathroom scale"]),
        ("weighing crates of freshly harvested tomatoes at a municipal farm produce market", "Platform produce scale", ["Bathroom spring scale", "Platform produce scale", "Clinical oral scale", "Measuring jug"]),
        ("monitoring the live weight of broiler chickens on a poultry farm before market sale", "Hanging spring scale with poultry cone", ["Digital kitchen scale", "Hanging spring scale with poultry cone", "Highway weighbridge", "Laboratory micro-balance"]),
        ("monitoring the weekly body mass of a newborn baby at a community health clinic", "Clinic baby balance scale", ["Kitchen measuring jug", "Clinic baby balance scale", "Weighbridge", "Bathroom scale with 1 kg increments"]),
        ("weighing a freshly caught 3 kg fish on a small boat", "Hanging mechanical spring scale", ["Trundle wheel", "Weighbridge", "Hanging mechanical spring scale", "Clinic scale"])
    ]
    task, correct_scale, opts = r.choice(scenarios)
    prompt = (
        f"A user needs to choose the most suitable instrument for: **{task}**.\n\n"
        f"Select the most appropriate weighing scale from the options below."
    )
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• The choice of weighing instrument depends on the required precision, capacity, and physical context:\n"
        f"  - Baking / small grams (0 g – 5 kg): Digital kitchen scale (precise to 1 g)\n"
        f"  - Heavy commercial trucks (tonnes): Fixed highway weighbridge\n"
        f"  - Infants: Curved clinic baby scale for comfort and safety\n"
        f"  - Field / outdoor suspension: Hanging hook spring balance\n\n"
        f"**Step 2: Method Setup & Evaluation**\n"
        f"• For {task}, the standard instrument is the **{correct_scale}**.\n"
        f"✓ **[1 Mark: Method – matching mass magnitude and environment to instrument capability]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{correct_scale}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct scale selection]**"
    )
    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": "Mass Scale",
        "segment_value_km": 1,
        "total_km": 10,
        "title": f"Instrument Measurement Scale ({correct_scale})",
    }
    return _make_q(
        diagram_spec=d_spec,
        subskill="meas_mass_scale_instrument_selection",
        prompt=prompt,
        answer=correct_scale,
        sol=sol,
        rubric=["1 Mark: Method – instrument capability rationale", f"1 Mark: Accuracy – {correct_scale}"],
        hints={
            "tier_1": "Consider the weight range: grams, kilograms, or tonnes.",
            "tier_2": f"Which instrument has the right precision and design for {task}?",
            "tier_3": f"Correct instrument: {correct_scale}."
        },
        options=opts,
        r=r
    )

def _gen_meas_mass_analog_kitchen_dial_subdivisions(r: random.Random) -> Dict[str, Any]:
    major_kg = r.choice([1, 2, 3])
    ticks_per_kg = r.choice([5, 10])
    g_per_tick = 1000 // ticks_per_kg
    tick_count = r.randint(1, ticks_per_kg - 1)
    extra_g = tick_count * g_per_tick
    total_g = (major_kg * 1000) + extra_g
    total_kg = round(total_g / 1000.0, 2)
    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} uses an analog dial kitchen scale to weigh a bowl of flour. "
        f"The dial has major numbered marks at every **1 kg**, and there are **{ticks_per_kg} equal subdivisions between each kilogram**.\n\n"
        f"1. What mass does each small subdivision tick represent?\n"
        f"2. If the dial pointer points **{tick_count} ticks past the {major_kg} kg mark**, what is the mass in kilograms (**kg**)?"
    )
    ans_str = f"{g_per_tick} g per tick ({_fmt(total_kg)} kg)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• There are 1 000 grams in 1 kilogram ($1\\text{{ kg}} = 1\\ 000\\text{{ g}}$).\n"
        f"• Value of each small tick subdivision:\n"
        f"  $$\\text{{Value per tick}} = \\frac{{1\\ 000\\text{{ g}}}}{{{ticks_per_kg}}} = {g_per_tick}\\text{{ g}}$$\n\n"
        f"**Step 2: Method Setup & Pointer Reading**\n"
        f"• The pointer is at {major_kg} kg plus {tick_count} ticks:\n"
        f"  $$\\text{{Extra mass}} = {tick_count} \\times {g_per_tick}\\text{{ g}} = {extra_g}\\text{{ g}} = {_fmt(round(extra_g / 1000.0, 2))}\\text{{ kg}}$$\n"
        f"  $$\\text{{Total mass}} = {major_kg} + {_fmt(round(extra_g / 1000.0, 2))} = {_fmt(total_kg)}\\text{{ kg}}$$\n"
        f"✓ **[1 Mark: Method – calculating subdivision value and adding to base mark]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{g_per_tick}\\text{{ g per tick}} \\ (\\text{{{_fmt(total_kg)} kg}})}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct tick value and total mass in kg]**"
    )
    return _make_q(
        subskill="meas_mass_analog_kitchen_dial_subdivisions",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 1000 ÷ ticks and pointer reading", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Each tick represents 1 000 g ÷ {ticks_per_kg} = {g_per_tick} g.",
            "tier_2": f"{tick_count} ticks = {tick_count} × {g_per_tick} g = {extra_g} g = {_fmt(round(extra_g/1000.0, 2))} kg.",
            "tier_3": f"Total mass = {major_kg} + {_fmt(round(extra_g/1000.0, 2))} = {_fmt(total_kg)} kg."
        },
        r=r
    )

def _gen_meas_mass_gross_tare_net_calculation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    tare_g = r.choice([350, 450, 600, 800, 1200])
    tare_kg = round(tare_g / 1000.0, 2)
    net_kg = round(r.choice([4.2, 5.5, 6.8, 8.4, 11.5]), 1)
    gross_kg = round(net_kg + tare_kg, 2)
    produce = r.choice(["freshly harvested Roma tomatoes", "farm-fresh round tomatoes", "dressed broiler chickens packed on ice", "farm-grown cabbages and spinach", "sweet potatoes"])
    prompt = (
        f"{name} weighs a plastic crate containing {produce} at a municipal fresh produce market. "
        f"The scale displays a **gross mass of {_fmt(gross_kg)} kg**. "
        f"The empty plastic crate has a **tare mass of {tare_g} g** ({_fmt(tare_kg)} kg).\n\n"
        f"Calculate the **net mass** of the {produce} in kilograms (**kg**)."
    )
    ans_str = f"{_fmt(net_kg)} kg"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• In commerce and measurement science:\n"
        f"  - **Gross Mass**: Total mass including the container and the contents.\n"
        f"  - **Tare Mass**: Mass of the empty packaging container alone.\n"
        f"  - **Net Mass**: Mass of the contents alone.\n"
        f"  $$\\text{{Net Mass}} = \\text{{Gross Mass}} - \\text{{Tare Mass}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Net Mass}} = {_fmt(gross_kg)}\\text{{ kg}} - {_fmt(tare_kg)}\\text{{ kg}} = {_fmt(net_kg)}\\text{{ kg}}$$\n"
        f"✓ **[1 Mark: Method – subtracting tare mass from gross mass with consistent units]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{_fmt(net_kg)}\\text{{ kg}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct net mass]**"
    )
    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "scale": f"Net {_fmt(net_kg)} kg | Tare {_fmt(tare_kg)} kg",
        "segment_value_km": 1,
        "total_km": 5,
        "title": f"Balance Scale ({_fmt(gross_kg)} kg)",
    }
    return _make_q(
        diagram_spec=d_spec,
        subskill="meas_mass_gross_tare_net_calculation",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – Gross minus Tare", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Net Mass = Gross Mass - Tare Mass.",
            "tier_2": f"Subtract {_fmt(tare_kg)} kg (tare) from {_fmt(gross_kg)} kg (gross).",
            "tier_3": f"{_fmt(gross_kg)} - {_fmt(tare_kg)} = {_fmt(net_kg)} kg."
        },
        r=r
    )

def _gen_meas_mass_bathroom_scale_tracking(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    base_m = r.randint(62, 78)
    week1 = round(base_m + 0.8, 1)
    week2 = round(base_m + 0.3, 1)
    week3 = round(base_m - 0.5, 1)
    week4 = round(base_m - 1.2, 1)
    loss = round(week1 - week4, 1)
    prompt = (
        f"{name} weighs himself on a digital bathroom scale once a week at 07:00 and logs the readings:\n\n"
        f"| Date | Week 1 | Week 2 | Week 3 | Week 4 |\n"
        f"| :--- | :---: | :---: | :---: | :---: |\n"
        f"| **Mass (kg)** | {_fmt(week1)} | {_fmt(week2)} | {_fmt(week3)} | {_fmt(week4)} |\n\n"
        f"1. Identify the highest and lowest mass recorded.\n"
        f"2. Calculate the total change in mass over the 4-week period."
    )
    ans_str = f"Lost {_fmt(loss)} kg (Highest: {_fmt(week1)} kg, Lowest: {_fmt(week4)} kg)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Track data chronologically to identify extremes and calculate net change:\n"
        f"  - Highest reading: {_fmt(week1)} kg (Week 1)\n"
        f"  - Lowest reading: {_fmt(week4)} kg (Week 4)\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Net Change}} = {_fmt(week1)}\\text{{ kg}} - {_fmt(week4)}\\text{{ kg}} = {_fmt(loss)}\\text{{ kg (mass reduction)}}$$\n"
        f"✓ **[1 Mark: Method – subtracting lowest reading from initial/highest reading]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct difference and identification of extremes]**"
    )
    d_spec = {
        "diagram_role": "context",
        "kind": "line_graph",
        "categories": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "values": [week1, week2, week3, week4],
        "title": f"Mass Tracking Chart ({name}: {week1} kg to {week4} kg)",
    }
    return _make_q(
        diagram_spec=d_spec,
        subskill="meas_mass_bathroom_scale_tracking",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – difference between Week 1 and Week 4", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Highest is {_fmt(week1)} kg, lowest is {_fmt(week4)} kg.",
            "tier_2": f"Subtract {_fmt(week4)} from {_fmt(week1)}.",
            "tier_3": f"{_fmt(week1)} - {_fmt(week4)} = {_fmt(loss)} kg lost."
        },
        r=r
    )

def _gen_meas_mass_schoolbag_health_ratio(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    body_mass = r.choice([40, 45, 50, 55, 60])
    threshold_percent = 10
    safe_bag_limit = round(body_mass * (threshold_percent / 100.0), 1)
    bag_mass = round(safe_bag_limit + r.choice([1.5, 2.0, 2.5, 3.0]), 1)
    excess = round(bag_mass - safe_bag_limit, 1)
    prompt = (
        f"According to South African paediatric health guidelines, a learner's packed school bag should not exceed **10% of their body mass**.\n\n"
        f"{name} has a body mass of **{body_mass} kg** and their school bag weighs **{_fmt(bag_mass)} kg** on a bathroom scale.\n\n"
        f"1. Calculate the maximum safe school bag mass for {name}.\n"
        f"2. Determine whether the bag is too heavy and by how many kilograms it exceeds the safe limit."
    )
    ans_str = f"Too heavy by {_fmt(excess)} kg (Safe limit: {_fmt(safe_bag_limit)} kg)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Calculate the 10% safety threshold of the learner's body mass:\n"
        f"  $$\\text{{Safe limit}} = 10\\% \\times {body_mass}\\text{{ kg}} = 0{{,}}10 \\times {body_mass} = {_fmt(safe_bag_limit)}\\text{{ kg}}$$\n\n"
        f"**Step 2: Method Setup & Excess Calculation**\n"
        f"• Compare actual bag mass to safe limit:\n"
        f"  $$\\text{{Excess mass}} = {_fmt(bag_mass)}\\text{{ kg}} - {_fmt(safe_bag_limit)}\\text{{ kg}} = {_fmt(excess)}\\text{{ kg}}$$\n"
        f"✓ **[1 Mark: Method – finding 10% of body mass and subtracting from bag mass]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct safe limit and excess mass calculation]**"
    )
    return _make_q(
        subskill="meas_mass_schoolbag_health_ratio",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 10% of body mass and difference", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Safe bag limit = 10% of {body_mass} kg = {_fmt(safe_bag_limit)} kg.",
            "tier_2": f"Subtract {_fmt(safe_bag_limit)} kg from {_fmt(bag_mass)} kg.",
            "tier_3": f"{_fmt(bag_mass)} - {_fmt(safe_bag_limit)} = {_fmt(excess)} kg excess."
        },
        r=r
    )

def _gen_meas_mass_loose_produce_cost_per_kg(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    mass_kg = round(r.choice([1.4, 1.8, 2.2, 2.6, 3.4, 4.2]), 1)
    price_per_kg = r.choice([12.50, 14.99, 16.50, 18.90, 22.00])
    total_cost = round(mass_kg * price_per_kg, 2)
    veg = r.choice(["farm-fresh vine tomatoes", "organic Roma tomatoes", "farmhouse broiler chicken portions", "red onions", "green bell peppers"])
    prompt = (
        f"{name} buys **{_fmt(mass_kg)} kg** of loose {veg} at a farm stall. "
        f"The electronic digital scale prints a label showing the price is **{_fmt_curr(price_per_kg)} per kg**.\n\n"
        f"Calculate the total amount {name} must pay. Round your answer to two decimal places."
    )
    ans_str = _fmt_curr(total_cost)
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• For weighed produce, total cost equals weighed mass multiplied by unit price per kilogram:\n"
        f"  $$\\text{{Total Cost}} = \\text{{Mass in kg}} \\times \\text{{Price per kg}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total Cost}} = {_fmt(mass_kg)}\\text{{ kg}} \\times \\text{{{_fmt_curr(price_per_kg)}}} = \\text{{{_fmt_curr(total_cost)}}}$\\n"
        f"✓ **[1 Mark: Method – multiplying mass in kg by price per kg]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total Rand cost]**"
    )
    return _make_q(
        subskill="meas_mass_loose_produce_cost_per_kg",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – mass × price per kg", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Cost = Mass (in kg) × Price per kg.",
            "tier_2": f"Multiply {_fmt(mass_kg)} by {_fmt_curr(price_per_kg)}.",
            "tier_3": f"{_fmt(mass_kg)} × {_fmt_curr(price_per_kg)} = {ans_str}."
        },
        r=r
    )

def _gen_meas_mass_fertilizer_field_bulk_cost(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    kg_per_bag = 30
    bags_count = r.choice([40, 60, 80, 96, 120])
    price_per_bag = r.choice([42.60, 48.50, 52.00, 55.40])
    total_kg = bags_count * kg_per_bag
    total_cost = round(bags_count * price_per_bag, 2)
    prompt = (
        f"{name} is the sports field manager for a high school. Two rugby fields must be fertilized before winter. "
        f"A **{kg_per_bag} kg bag** of lawn fertilizer costs **{_fmt_curr(price_per_bag)}**. "
        f"The grounds crew determines that **{bags_count} bags** are needed.\n\n"
        f"1. How many kilograms of fertilizer will they purchase altogether?\n"
        f"2. Calculate the total cost for the fertilizer."
    )
    ans_str = f"{_fmt(total_kg)} kg ({_fmt_curr(total_cost)})"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Total mass equals number of bags multiplied by mass per bag ($1\\text{{ bag}} = {kg_per_bag}\\text{{ kg}}$).\n"
        f"• Total cost equals number of bags multiplied by price per bag.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total Mass}} = {bags_count} \\times {kg_per_bag}\\text{{ kg}} = {_fmt(total_kg)}\\text{{ kg}}$$\n"
        f"$$\\text{{Total Cost}} = {bags_count} \\times \\text{{{_fmt_curr(price_per_bag)}}} = \\text{{{_fmt_curr(total_cost)}}}$\\n"
        f"✓ **[1 Mark: Method – multiplying bags by kg per bag and price per bag]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{_fmt(total_kg)}\\text{{ kg}} \\ (\\text{{{_fmt_curr(total_cost)}}})}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total mass and total cost]**"
    )
    return _make_q(
        subskill="meas_mass_fertilizer_field_bulk_cost",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – bags × kg and bags × price", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Total kg = {bags_count} bags × {kg_per_bag} kg.",
            "tier_2": f"Total cost = {bags_count} bags × {_fmt_curr(price_per_bag)}.",
            "tier_3": f"Result: {ans_str}."
        },
        r=r
    )

def _gen_meas_mass_building_sand_tonnes_bags(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    tonnes = round(r.choice([0.8, 1.2, 1.5, 2.0]), 1)
    kg_needed = int(tonnes * 1000)
    bag_size = 50
    bags_needed = kg_needed // bag_size
    price_per_bag = r.choice([25.00, 32.50, 38.00, 45.00])
    total_cost = bags_needed * price_per_bag
    prompt = (
        f"{name} is building a paved patio and requires **{_fmt(tonnes)} tonnes** of building sand. "
        f"The local building supplier sells sand in **{bag_size} kg bags** at **{_fmt_curr(price_per_bag)} per bag**.\n\n"
        f"1. Convert the required sand into kilograms (**kg**).\n"
        f"2. How many {bag_size} kg bags must {name} purchase?\n"
        f"3. Calculate the total cost of the sand."
    )
    ans_str = f"{_fmt(kg_needed)} kg ({bags_needed} bags, {_fmt_curr(total_cost)})"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• $1\\text{{ tonne}} = 1\\ 000\\text{{ kg}}$. Multiply tonnes by 1 000 to convert to kg:\n"
        f"  $${_fmt(tonnes)}\\text{{ tonnes}} \\times 1\\ 000 = {_fmt(kg_needed)}\\text{{ kg}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Bags needed}} = \\frac{{{_fmt(kg_needed)}\\text{{ kg}}}}{{{bag_size}\\text{{ kg/bag}}}} = {bags_needed}\\text{{ bags}}$$\n"
        f"$$\\text{{Total cost}} = {bags_needed} \\times \\text{{{_fmt_curr(price_per_bag)}}} = \\text{{{_fmt_curr(total_cost)}}}$\\n"
        f"✓ **[1 Mark: Method – converting tonnes to kg and dividing by bag mass]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{_fmt(kg_needed)}\\text{{ kg}} \\ ({bags_needed}\\text{{ bags, }} \\text{{{_fmt_curr(total_cost)}}})}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct kg, bags count, and total cost]**"
    )
    return _make_q(
        subskill="meas_mass_building_sand_tonnes_bags",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – tonnes to kg, divide by 50, multiply price", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"1 tonne = 1 000 kg. {_fmt(tonnes)} tonnes = {_fmt(kg_needed)} kg.",
            "tier_2": f"Bags = {_fmt(kg_needed)} ÷ {bag_size} = {bags_needed} bags.",
            "tier_3": f"Total cost = {bags_needed} × {_fmt_curr(price_per_bag)} = {_fmt_curr(total_cost)}."
        },
        r=r
    )

def _gen_meas_mass_butchery_meat_portioning(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    mass_g = r.choice([400, 500, 750, 800, 1250, 1500])
    mass_kg = mass_g / 1000.0
    price_per_kg = r.choice([89.00, 95.00, 110.00, 125.00, 140.00])
    cost = round(mass_kg * price_per_kg, 2)
    cut = r.choice(["fresh farm dressed broiler chicken", "farmhouse chicken drumsticks", "free-range whole broiler chickens", "beef stewing meat", "lamb chops"])
    prompt = (
        f"{name} visits a local butchery to buy **{mass_g} g** of {cut}. "
        f"The price board indicates that the meat is priced at **{_fmt_curr(price_per_kg)} per kg**.\n\n"
        f"1. Convert the mass of meat to kilograms (**kg**).\n"
        f"2. Calculate the total cost {name} will pay at the till."
    )
    ans_str = f"{_fmt(mass_kg)} kg ({_fmt_curr(cost)})"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Since price is given per kilogram, first convert grams to kilograms by dividing by 1 000:\n"
        f"  $$\\text{{Mass in kg}} = \\frac{{{mass_g}}}{{1\\ 000}} = {_fmt(mass_kg)}\\text{{ kg}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total Cost}} = {_fmt(mass_kg)}\\text{{ kg}} \\times \\text{{{_fmt_curr(price_per_kg)}}} = \\text{{{_fmt_curr(cost)}}}$\\n"
        f"✓ **[1 Mark: Method – dividing grams by 1 000 and multiplying by price per kg]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{_fmt(mass_kg)}\\text{{ kg}} \\ (\\text{{{_fmt_curr(cost)}}})}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct converted mass and total cost]**"
    )
    return _make_q(
        subskill="meas_mass_butchery_meat_portioning",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – grams to kg and multiply by rate", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Convert grams to kg: {mass_g} g ÷ 1 000 = {_fmt(mass_kg)} kg.",
            "tier_2": f"Multiply mass in kg by price per kg: {_fmt(mass_kg)} × {_fmt_curr(price_per_kg)}.",
            "tier_3": f"Cost = {_fmt_curr(cost)}."
        },
        r=r
    )

def _gen_meas_mass_postage_courier_tier_pricing(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    parcel_g = r.choice([85, 240, 420, 750, 1400, 1850])
    tiers = [
        (0, 100, 15.00, "Up to 100 g"),
        (101, 500, 32.50, "101 g to 500 g"),
        (501, 1000, 58.00, "501 g to 1 000 g (1 kg)"),
        (1001, 2000, 89.00, "1 001 g to 2 000 g (2 kg)")
    ]
    correct_tier = next(t for t in tiers if t[0] <= parcel_g <= t[1])
    tier_label = correct_tier[3]
    price = correct_tier[2]
    table_md = (
        "| Mass Bracket | Postal Fee |\n"
        "| :--- | :--- |\n"
        "| Up to 100 g | R 15,00 |\n"
        "| 101 g to 500 g | R 32,50 |\n"
        "| 501 g to 1 000 g (1 kg) | R 58,00 |\n"
        "| 1 001 g to 2 000 g (2 kg) | R 89,00 |"
    )
    prompt = (
        f"{name} sends a parcel containing textbooks. The post office digital scale shows a mass of **{parcel_g} g**.\n\n"
        f"Refer to the postal tariff schedule below:\n\n"
        f"{table_md}\n\n"
        f"Identify the applicable mass bracket and determine the postal fee payable."
    )
    ans_str = f"{tier_label} ({_fmt_curr(price)})"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Compare the measured mass ({parcel_g} g) against the tariff brackets in the table.\n"
        f"• {parcel_g} g falls strictly within the bracket: **{tier_label}**.\n\n"
        f"**Step 2: Method Setup & Reading Tariff**\n"
        f"• The corresponding fee for the {tier_label} tier is **{_fmt_curr(price)}**.\n"
        f"✓ **[1 Mark: Method – locating the correct bracket on the tariff schedule]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct tier identification and postal charge]**"
    )
    return _make_q(
        subskill="meas_mass_postage_courier_tier_pricing",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – matching mass to table bracket", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Locate which bracket {parcel_g} g falls into.",
            "tier_2": f"{parcel_g} g is between {correct_tier[0]} g and {correct_tier[1]} g.",
            "tier_3": f"Tariff: {tier_label} = {_fmt_curr(price)}."
        },
        r=r
    )

def _gen_meas_mass_unit_price_best_value(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    small_kg = 2.5
    small_price = r.choice([38.00, 40.00, 42.50])
    small_unit = round(small_price / small_kg, 2)
    large_kg = 10.0
    large_price = r.choice([120.00, 130.00, 140.00])
    large_unit = round(large_price / large_kg, 2)
    diff = round(abs(small_unit - large_unit), 2)
    cheaper = "10 kg bag" if large_unit < small_unit else "2,5 kg bag"
    prompt = (
        f"{name} compares two packaging sizes of super maize meal at a supermarket:\n\n"
        f"• **Option A**: 2,5 kg bag for **{_fmt_curr(small_price)}**\n"
        f"• **Option B**: 10 kg bag for **{_fmt_curr(large_price)}**\n\n"
        f"1. Calculate the unit price per kilogram for each option.\n"
        f"2. Determine which option offers better value for money and by how much per kilogram."
    )
    ans_str = f"{cheaper} is cheaper by {_fmt_curr(diff)}/kg"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• To compare value between different package sizes, calculate the unit cost per 1 kg:\n"
        f"  $$\\text{{Unit Price}} = \\frac{{\\text{{Package Cost}}}}{{\\text{{Package Mass in kg}}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Option A (2,5 kg)}} = \\frac{{{_fmt_curr(small_price)}}}{{2{{,}}5\\text{{ kg}}}} = {_fmt_curr(small_unit)}\\text{{/kg}}$$\n"
        f"$$\\text{{Option B (10 kg)}} = \\frac{{{_fmt_curr(large_price)}}}{{10\\text{{ kg}}}} = {_fmt_curr(large_unit)}\\text{{/kg}}$$\n"
        f"$$\\text{{Difference}} = |{_fmt_curr(small_unit)} - {_fmt_curr(large_unit)}| = {_fmt_curr(diff)}\\text{{/kg}}$$\n"
        f"✓ **[1 Mark: Method – calculating both unit prices per kg and finding difference]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct comparison conclusion and saving per kg]**"
    )
    return _make_q(
        subskill="meas_mass_unit_price_best_value",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – unit rates calculation and comparison", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Divide total price by kg for each option to find price per 1 kg.",
            "tier_2": f"Option A: {_fmt_curr(small_price)} ÷ 2,5 = {_fmt_curr(small_unit)}/kg. Option B: {_fmt_curr(large_price)} ÷ 10 = {_fmt_curr(large_unit)}/kg.",
            "tier_3": f"{cheaper} is cheaper by {_fmt_curr(diff)} per kg."
        },
        r=r
    )

def _gen_meas_mass_baby_clinic_growth_chart(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    birth_kg = round(r.choice([3.1, 3.3, 3.5, 3.8]), 1)
    weeks = r.choice([4, 6, 8])
    gain_g_per_week = r.choice([200, 220, 250, 280])
    total_gain_g = weeks * gain_g_per_week
    total_gain_kg = total_gain_g / 1000.0
    current_kg = round(birth_kg + total_gain_kg, 2)
    prompt = (
        f"A baby named {name} had a birth mass of **{_fmt(birth_kg)} kg**. "
        f"At a **{weeks}-week clinic check-up**, the pediatric balance scale records a mass of **{_fmt(current_kg)} kg**.\n\n"
        f"1. What is the baby's total mass gain in grams (**g**)?\n"
        f"2. Calculate the average mass gain per week in grams (**g/week**)."
    )
    ans_str = f"{total_gain_g} g total ({gain_g_per_week} g/week)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Subtract birth mass from current mass to find total gain:\n"
        f"  $$\\text{{Gain in kg}} = {_fmt(current_kg)} - {_fmt(birth_kg)} = {_fmt(round(current_kg - birth_kg, 2))}\\text{{ kg}}$$\n"
        f"  $$\\text{{Gain in g}} = {_fmt(round(current_kg - birth_kg, 2))} \\times 1\\ 000 = {total_gain_g}\\text{{ g}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Average weekly gain}} = \\frac{{{total_gain_g}\\text{{ g}}}}{{{weeks}\\text{{ weeks}}}} = {gain_g_per_week}\\text{{ g/week}}$$\n"
        f"✓ **[1 Mark: Method – finding total mass gain in grams and dividing by weeks]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total grams and weekly average]**"
    )
    return _make_q(
        subskill="meas_mass_baby_clinic_growth_chart",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total gain in g ÷ weeks", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Total gain = {_fmt(current_kg)} kg - {_fmt(birth_kg)} kg = {_fmt(round(current_kg-birth_kg, 2))} kg = {total_gain_g} g.",
            "tier_2": f"Divide total gain by {weeks} weeks.",
            "tier_3": f"{total_gain_g} g ÷ {weeks} = {gain_g_per_week} g/week."
        },
        r=r
    )

def _gen_meas_mass_animal_veterinary_dosage(r: random.Random) -> Dict[str, Any]:
    animal = r.choice(["A Boer goat on a livestock farm", "A Nguni calf in an agricultural kraal", "A Boerboel farm watch dog", "A Merino sheep"])
    mass_kg = r.choice([20, 25, 30, 35, 40])
    dose_per_5kg = 2  # 2 ml per 5 kg body mass
    total_dose_ml = (mass_kg // 5) * dose_per_5kg
    prompt = (
        f"{animal} weighs **{mass_kg} kg** on the veterinary clinic walk-on platform scale. "
        f"The veterinary medicine instructions state a deworming suspension dosage of **{dose_per_5kg} ml for every 5 kg of body mass**.\n\n"
        f"Calculate the correct total dosage of medication to administer in millilitres (**ml**)."
    )
    ans_str = f"{total_dose_ml} ml"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Determine how many 5 kg units are in the animal's total body mass:\n"
        f"  $$\\text{{5 kg units}} = \\frac{{{mass_kg}\\text{{ kg}}}}{{5\\text{{ kg}}}} = {mass_kg // 5}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total dose}} = {mass_kg // 5} \\times {dose_per_5kg}\\text{{ ml}} = {total_dose_ml}\\text{{ ml}}$$\n"
        f"✓ **[1 Mark: Method – dividing mass by 5 and multiplying by dosage rate]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{total_dose_ml}\\text{{ ml}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct volume in ml]**"
    )
    return _make_q(
        subskill="meas_mass_animal_veterinary_dosage",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (mass ÷ 5) × dosage rate", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide body mass ({mass_kg} kg) by 5 kg.",
            "tier_2": f"Multiply the result ({mass_kg // 5}) by {dose_per_5kg} ml.",
            "tier_3": f"{mass_kg // 5} × {dose_per_5kg} ml = {total_dose_ml} ml."
        },
        r=r
    )

# ==============================================================================
