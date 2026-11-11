"""Cluster 5: Ratios, Rates & Proportions (10 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_num_rat_simplify_two_term_ratio(r: random.Random) -> Dict[str, Any]:
    # e.g. 15 : 25 -> 3 : 5
    common_factor = r.choice([3, 4, 5, 6, 8, 12])
    term1 = r.choice([2, 3, 4, 5, 7])
    term2 = r.choice([i for i in [2, 3, 4, 5, 7, 9] if math.gcd(i, term1) == 1])
    raw_a = term1 * common_factor
    raw_b = term2 * common_factor
    ans_str = f"{term1} : {term2}"

    prompt = (
        f"In a high school sports club, there are **{raw_a} soccer players** and **{raw_b} netball players**.\n\n"
        f"1. Write down the ratio of soccer players to netball players in the form **{raw_a} : {raw_b}**.\n"
        f"2. Simplify this ratio to its **simplest whole number integer form**."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• To simplify a ratio, divide both terms by their Highest Common Factor (HCF):\n"
        f"  $$\\text{{HCF}}({raw_a}, {raw_b}) = {common_factor}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• First term: ${raw_a} \\div {common_factor} = {term1}$.\n"
        f"• Second term: ${raw_b} \\div {common_factor} = {term2}$.\n"
        f"• Simplified ratio: **{ans_str}**.\n"
        f"✓ **[1 Mark: Method – dividing both terms by highest common factor {common_factor}]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct simplified ratio]**"
    )
    return _make_q(
        subskill="num_rat_simplify_two_term_ratio",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – divide by HCF", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Find the common factor that divides both {raw_a} and {raw_b}.",
            "tier_2": f"Both numbers divide by {common_factor}: {raw_a} ÷ {common_factor} and {raw_b} ÷ {common_factor}.",
            "tier_3": f"Simplified ratio = {ans_str}."
        },
        r=r
    )

def _gen_num_rat_simplify_mixed_units_ratio(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        (500, "ml", 2, "L", 2000, "1 : 4"),
        (250, "ml", 1, "L", 1000, "1 : 4"),
        (750, "ml", 3, "L", 3000, "1 : 4"),
        (50, "cm", 2, "m", 200, "1 : 4"),
        (25, "cm", 1, "m", 100, "1 : 4"),
        (200, "g", 1, "kg", 1000, "1 : 5"),
        (500, "g", 2, "kg", 2000, "1 : 4")
    ]
    val1, unit1, val2, unit2, val2_converted, ans_str = r.choice(scenarios)

    prompt = (
        f"A recipe specifies mixing liquid ingredients in the proportion:\n\n"
        f"**{val1} {unit1} to {val2} {unit2}**\n\n"
        f"Simplify this ratio to its simplest form, ensuring that both quantities are converted to the **same unit** first."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• A ratio can only compare quantities that share identical measurement units.\n"
        f"• Convert the larger unit ({unit2}) to the smaller unit ({unit1}):\n"
        f"  $${val2}\\text{{ {unit2}}} = {val2_converted}\\text{{ {unit1}}}$$\n\n"
        f"**Step 2: Method Setup & Simplification**\n"
        f"• Unsimplified same-unit ratio: ${val1} : {val2_converted}$.\n"
        f"• Divide both terms by ${val1}$: $\\frac{{{val1}}}{{{val1}}} : \\frac{{{val2_converted}}}{{{val1}}} = {ans_str}$.\n"
        f"✓ **[1 Mark: Method – converting units to common base and simplifying by common factor]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct simplified ratio]**"
    )
    return _make_q(
        subskill="num_rat_simplify_mixed_units_ratio",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – convert to same unit and divide", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Convert {val2} {unit2} into {unit1} ({val2_converted} {unit1}) before simplifying.",
            "tier_2": f"Simplify {val1} : {val2_converted}.",
            "tier_3": f"Simplified ratio = {ans_str}."
        },
        r=r
    )

def _gen_num_rat_divide_quantity_two_parts(r: random.Random) -> Dict[str, Any]:
    name1 = r.choice(SA_NAMES)
    name2 = r.choice([n for n in SA_NAMES if n != name1])
    p1 = r.choice([2, 3, 4])
    p2 = r.choice([3, 5, 7])
    total_parts = p1 + p2
    part_value = r.choice([400, 500, 600, 800, 1000])
    total_amount = total_parts * part_value
    share1 = p1 * part_value
    ans_str = _fmt_curr(share1)

    prompt = (
        f"{name1} and {name2} partner in a community produce enterprise and agree to divide a monthly profit of **{_fmt_curr(total_amount)}** in the ratio **{p1} : {p2}**.\n\n"
        f"Calculate **{name1}'s share** of the profit."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• To divide a quantity in ratio $a : b$:\n"
        f"  1. Find total ratio parts: $\\text{{Total Parts}} = {p1} + {p2} = {total_parts}$.\n"
        f"  2. Find value of one part: $\\frac{{\\text{{Total Amount}}}}{{\\text{{Total Parts}}}} = \\frac{{{_fmt_curr(total_amount)}}}{{{total_parts}}} = \\text{{{_fmt_curr(part_value)}}}$.\n"
        f"  3. Multiply by {name1}'s share ({p1} parts).\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• Value per part: $\\frac{{{total_amount}}}{{{total_parts}}} = {part_value}$.\n"
        f"• $\\text{{{name1}'s Share}} = {p1} \\times {part_value} = {share1}$.\n"
        f"✓ **[1 Mark: Method – summing ratio parts, dividing total by parts, and multiplying by {p1}]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct share in Rands]**"
    )
    return _make_q(
        subskill="num_rat_divide_quantity_two_parts",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total ÷ total_parts × share_parts", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Add the ratio parts: {p1} + {p2} = {total_parts} parts.",
            "tier_2": f"Find 1 part: {_fmt_curr(total_amount)} ÷ {total_parts} = {_fmt_curr(part_value)}. Multiply by {p1}.",
            "tier_3": f"{name1}'s share = {_fmt_curr(share1)}."
        },
        r=r
    )

def _gen_num_rat_divide_quantity_three_parts(r: random.Random) -> Dict[str, Any]:
    p1, p2, p3 = 2, 3, 5
    total_parts = p1 + p2 + p3  # 10
    total_amount = round(r.choice([15000.00, 20000.00, 25000.00, 30000.00]), 2)
    part_value = total_amount / total_parts
    largest_share = round(p3 * part_value, 2)
    ans_str = _fmt_curr(largest_share)

    prompt = (
        f"A community trust allocates a grant of **{_fmt_curr(total_amount)}** to three local school programmes in the ratio **{p1} : {p2} : {p3}**.\n\n"
        f"Calculate the **largest allocation share** paid out from this grant."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Total parts = ${p1} + {p2} + {p3} = {total_parts}$.\n"
        f"• Value of 1 part = $\\frac{{{_fmt_curr(total_amount)}}}{{{total_parts}}} = \\text{{{_fmt_curr(part_value)}}}$.\n"
        f"• The largest share corresponds to the largest ratio term ({p3} parts):\n"
        f"  $$\\text{{Largest Share}} = {p3} \\times \\text{{{_fmt_curr(part_value)}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Largest Share}} = {p3} \\times \\text{{{_fmt_curr(part_value)}}} = \\text{{{_fmt_curr(largest_share)}}}$.\n"
        f"✓ **[1 Mark: Method – summing all 3 parts, dividing total by {total_parts}, and multiplying by {p3}]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct largest share in Rands]**"
    )
    return _make_q(
        subskill="num_rat_divide_quantity_three_parts",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total ÷ 10 × 5", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Sum all parts: {p1} + {p2} + {p3} = {total_parts} total parts.",
            "tier_2": f"Divide {_fmt_curr(total_amount)} by {total_parts} = {_fmt_curr(part_value)}. Multiply by {p3}.",
            "tier_3": f"Largest share = {_fmt_curr(largest_share)}."
        },
        r=r
    )

def _gen_num_rat_find_missing_term_proportion(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    items_known = r.choice([3, 4, 5])
    cost_known = round(r.choice([45.00, 60.00, 75.00, 90.00]), 2)
    unit_cost = cost_known / items_known
    target_items = r.choice([8, 12, 15, 20])
    target_cost = round(target_items * unit_cost, 2)
    ans_str = _fmt_curr(target_cost)

    prompt = (
        f"{name} buys **{items_known} identical school notebooks** for a total of **{_fmt_curr(cost_known)}**.\n\n"
        f"Assuming the unit price remains directly proportional, calculate the **total cost to purchase {target_items} notebooks**."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• In direct proportion, the unit price is constant:\n"
        f"  $$\\text{{Unit Price}} = \\frac{{\\text{{Cost}}}}{{\\text{{Quantity}}}} = \\frac{{{_fmt_curr(cost_known)}}}{{{items_known}}} = \\text{{{_fmt_curr(unit_cost)}}}\\text{{ per notebook}}$$\n"
        f"• Total Cost for {target_items} notebooks = $\\text{{Target Items}} \\times \\text{{Unit Price}}$.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Unit Price}} = \\frac{{{_fmt(cost_known)}}}{{{items_known}}} = {_fmt(unit_cost)}$.\n"
        f"• $\\text{{Total Cost}} = {target_items} \\times {_fmt(unit_cost)} = \\text{{{_fmt_curr(target_cost)}}}$.\n"
        f"✓ **[1 Mark: Method – finding unit cost and multiplying by target quantity]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct proportional cost in Rands]**"
    )
    return _make_q(
        subskill="num_rat_find_missing_term_proportion",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (cost ÷ known_items) × target_items", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Find the price of 1 notebook: {_fmt_curr(cost_known)} ÷ {items_known} = {_fmt_curr(unit_cost)}.",
            "tier_2": f"Multiply {_fmt_curr(unit_cost)} by {target_items}.",
            "tier_3": f"Total cost = {_fmt_curr(target_cost)}."
        },
        r=r
    )

def _gen_num_rat_mixing_ratio_recipe_or_fertilizer(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    ratio_parts_water = r.choice([4, 5, 8])  # 1 part concentrate : N parts water
    total_water_litres = r.choice([10, 15, 20])
    concentrate_litres = round(total_water_litres / ratio_parts_water, 2)
    ans_str = f"{_fmt(concentrate_litres)} L"

    prompt = (
        f"{name} prepares an organic soluble fertilizer mixture for an urban tomato crop.\n\n"
        f"The manufacturer's label specifies a dilution ratio of **1 part liquid fertilizer concentrate to {ratio_parts_water} parts water** (1 : {ratio_parts_water}).\n\n"
        f"If {name} fills a spray knapsack with **{total_water_litres} litres of water**, calculate the **volume of fertilizer concentrate** that must be added."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• The ratio of concentrate to water is $1 : {ratio_parts_water}$.\n"
        f"• To find the required concentrate volume:\n"
        f"  $$\\text{{Concentrate}} = \\frac{{\\text{{Water Volume}}}}{{{ratio_parts_water}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Concentrate}} = \\frac{{{total_water_litres}}}{{{ratio_parts_water}}} = {_fmt(concentrate_litres)}\\text{{ litres}}$.\n"
        f"✓ **[1 Mark: Method – dividing water volume by dilution ratio denominator]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct concentrate volume with units]**"
    )
    return _make_q(
        subskill="num_rat_mixing_ratio_recipe_or_fertilizer",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – water ÷ ratio_parts", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide the water volume ({total_water_litres} L) by the dilution ratio parts ({ratio_parts_water}).",
            "tier_2": f"{total_water_litres} ÷ {ratio_parts_water} = {concentrate_litres}.",
            "tier_3": f"Concentrate volume = {ans_str}."
        },
        r=r
    )

def _gen_num_rat_unit_rate_best_value_comparison(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    # Option A: 2.5 kg bag maize meal for R 34.50 -> R 13.80 / kg
    # Option B: 10 kg bag maize meal for R 125.00 -> R 12.50 / kg
    cost_a = round(r.choice([32.50, 34.50, 36.00]), 2)
    mass_a = 2.5
    rate_a = round(cost_a / mass_a, 2)

    cost_b = round(r.choice([115.00, 125.00, 130.00]), 2)
    mass_b = 10.0
    rate_b = round(cost_b / mass_b, 2)

    cheaper_pack = "10 kg bag" if rate_b < rate_a else "2,5 kg bag"
    cheaper_rate = min(rate_a, rate_b)
    diff = round(abs(rate_a - rate_b), 2)
    ans_str = f"{cheaper_pack} by {_fmt_curr(diff)} per kg"

    prompt = (
        f"{name} compares two bulk package options for super maize meal at the supermarket:\n\n"
        f"• **Option 1**: A **2,5 kg bag** selling for **{_fmt_curr(cost_a)}**\n"
        f"• **Option 2**: A **10 kg bag** selling for **{_fmt_curr(cost_b)}**\n\n"
        f"1. Calculate the unit price per kilogram (R/kg) for both package sizes.\n"
        f"2. Determine which option is the **best value (cheaper per kg)** and by **how much per kilogram**."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Unit price per kilogram is calculated by dividing total package cost by total mass:\n"
        f"  $$\\text{{Unit Price}} = \\frac{{\\text{{Price}}}}{{\\text{{Mass (kg)}}}}$$\n"
        f"• Compare both unit rates to find the cheaper option and calculate the price difference.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Option 1 (2,5 kg)}} = \\frac{{{_fmt_curr(cost_a)}}}{{2,5}} = \\text{{{_fmt_curr(rate_a)}}}\\text{{/kg}}$.\n"
        f"• $\\text{{Option 2 (10 kg)}} = \\frac{{{_fmt_curr(cost_b)}}}{{10}} = \\text{{{_fmt_curr(rate_b)}}}\\text{{/kg}}$.\n"
        f"• Difference: $|\\text{{{_fmt_curr(rate_a)}}} - \\text{{{_fmt_curr(rate_b)}}}| = \\text{{{_fmt_curr(diff)}}}\\text{{/kg}}$.\n"
        f"• The **{cheaper_pack}** is cheaper by **{_fmt_curr(diff)} per kg**.\n"
        f"✓ **[1 Mark: Method – calculating both unit rates per kg and determining difference]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct package choice and price difference per kg]**"
    )
    custom_opts = [
        f"10 kg bag by {_fmt_curr(diff)} per kg",
        f"2,5 kg bag by {_fmt_curr(diff)} per kg",
        f"10 kg bag by {_fmt_curr(round(diff * 1.2, 2))} per kg",
        f"2,5 kg bag by {_fmt_curr(round(diff * 1.2, 2))} per kg"
    ]
    return _make_q(
        subskill="num_rat_unit_rate_best_value_comparison",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – comparing unit rates per kg", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Option 1: {_fmt_curr(cost_a)} ÷ 2,5 kg = {_fmt_curr(rate_a)}/kg. Option 2: {_fmt_curr(cost_b)} ÷ 10 kg = {_fmt_curr(rate_b)}/kg.",
            "tier_2": f"Subtract the cheaper unit rate from the more expensive one: {_fmt_curr(diff)}/kg.",
            "tier_3": f"Best value = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_rat_consumption_rate_fuel_economy(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    distance_km = r.choice([450, 520, 600, 650])
    fuel_litres = round(r.choice([36.0, 41.6, 48.0, 52.0]), 1)
    # L per 100 km = (Litres / Distance) * 100
    litres_per_100km = round((fuel_litres / distance_km) * 100, 1)
    ans_str = f"{_fmt(litres_per_100km, 1)} L/100 km"

    prompt = (
        f"{name} undertakes a long-distance road trip covering **{distance_km} km**.\n\n"
        f"During the journey, the vehicle consumes **{_fmt(fuel_litres, 1)} litres of petrol**.\n\n"
        f"Calculate the vehicle's **fuel consumption rate in litres per 100 km (L/100 km)**, rounded to 1 decimal place."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• In South Africa, vehicle fuel economy is measured in litres consumed per 100 kilometres:\n"
        f"  $$\\text{{Fuel Consumption}} = \\left( \\frac{{\\text{{Litres consumed}}}}{{\\text{{Distance (km)}}}} \\right) \\times 100$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Rate}} = \\left( \\frac{{{_fmt(fuel_litres, 1)}}}{{{distance_km}}} \\right) \\times 100 = {fuel_litres / distance_km * 100:.4f} \\approx {_fmt(litres_per_100km, 1)}\\text{{ L/100 km}}$.\n"
        f"✓ **[1 Mark: Method – dividing litres by distance and multiplying by 100]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct fuel consumption rate with units]**"
    )
    return _make_q(
        subskill="num_rat_consumption_rate_fuel_economy",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (litres ÷ distance) × 100", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide fuel consumed ({_fmt(fuel_litres, 1)} L) by distance ({distance_km} km), then multiply by 100.",
            "tier_2": f"({fuel_litres} ÷ {distance_km}) × 100 = {litres_per_100km}.",
            "tier_3": f"Consumption rate = {ans_str}."
        },
        r=r
    )

def _gen_num_rat_inverse_proportion_workers_time(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    w1 = r.choice([2, 3, 4])
    d1 = r.choice([6, 8, 12])
    total_man_days = w1 * d1
    w2 = r.choice([i for i in [2, 3, 4, 6] if i != w1 and total_man_days % i == 0])
    d2 = total_man_days // w2
    ans_str = f"{d2} days"

    prompt = (
        f"{w1} experienced bricklayers take **{d1} days** to construct a boundary security wall working at a constant pace.\n\n"
        f"Assuming all workers work at the identical rate (an **inverse proportion relationship** where $W_1 \\times D_1 = W_2 \\times D_2$):\n\n"
        f"How many days would it take **{w2} bricklayers** to build the same wall?"
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• In inverse proportion, as the number of workers increases, the time required decreases proportionally:\n"
        f"  $$\\text{{Total Worker-Days}} = W_1 \\times D_1 = {w1} \\times {d1} = {total_man_days}\\text{{ worker-days}}$$\n"
        f"  $$\\text{{New Duration}} = \\frac{{\\text{{Total Worker-Days}}}}{{W_2}} = \\frac{{{total_man_days}}}{{{w2}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Total Worker-Days}} = {w1} \\times {d1} = {total_man_days}$.\n"
        f"• $\\text{{Days for {w2} workers}} = \\frac{{{total_man_days}}}{{{w2}}} = {d2}\\text{{ days}}$.\n"
        f"✓ **[1 Mark: Method – finding total worker-days product and dividing by new worker count]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct days with units]**"
    )
    custom_opts = [
        f"{d2} days",
        f"{d1} days",
        f"{d2 + 2} days",
        f"{max(1, d2 - 2)} days"
    ]
    return _make_q(
        subskill="num_rat_inverse_proportion_workers_time",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (w1 × d1) ÷ w2", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Find total worker-days: {w1} × {d1} = {total_man_days}.",
            "tier_2": f"Divide {total_man_days} by {w2} workers.",
            "tier_3": f"Days needed = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_num_rat_speed_distance_time_rate(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    speed_kmh = r.choice([60, 80, 100, 120])
    hours = r.choice([2.5, 3.0, 3.5, 4.0])
    distance = round(speed_kmh * hours, 1)
    ans_str = f"{_fmt(distance, 1)} km"

    prompt = (
        f"A long-distance passenger bus travels at an average speed of **{speed_kmh} km/h** along the N1 highway.\n\n"
        f"Calculate the **distance covered** after travelling for **{_fmt(hours, 1)} hours** at this constant rate ($\text{{Distance}} = \text{{Speed}} \\times \text{{Time}}$)."
    )
    sol = (
        f"**Step 1: Mathematical Concept & Thought Process**\n"
        f"• Distance is the product of speed rate and travel time:\n"
        f"  $$\\text{{Distance}} = \\text{{Speed}} \\times \\text{{Time}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• $\\text{{Distance}} = {speed_kmh} \\times {_fmt(hours, 1)} = {_fmt(distance, 1)}\\text{{ km}}$.\n"
        f"✓ **[1 Mark: Method – multiplying speed by time]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct distance with units]**"
    )
    return _make_q(
        subskill="num_rat_speed_distance_time_rate",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – speed × time", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Multiply speed ({speed_kmh} km/h) by time ({_fmt(hours, 1)} hours).",
            "tier_2": f"{speed_kmh} × {hours} = {distance}.",
            "tier_3": f"Distance = {ans_str}."
        },
        r=r
    )
