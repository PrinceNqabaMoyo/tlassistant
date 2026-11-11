from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

# CLUSTER 3: VOLUME & CAPACITY MEASUREMENT & LIQUID COSTING (13 Archetypes)
# ==============================================================================

def _gen_meas_vol_jug_meniscus_reading(r: random.Random) -> Dict[str, Any]:
    base_ml = r.choice([200, 400, 600, 800])
    subdiv_ml = 50
    ticks = r.randint(1, 3)
    extra_ml = ticks * subdiv_ml
    total_ml = base_ml + extra_ml
    total_l = total_ml / 1000.0
    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} measures cooking oil in a transparent 1-litre kitchen measuring jug. "
        f"The measuring jug has major calibrated markings every 100 ml, with **subdivisions every {subdiv_ml} ml**.\n\n"
        f"When held flat at eye level, the bottom of the liquid curved meniscus rests **{ticks} subdivision tick(s) above the {base_ml} ml mark**.\n\n"
        f"Record the volume of oil in millilitres (**ml**) and litres (**l**)."
    )
    ans_str = f"{total_ml} ml ({_fmt(total_l)} l)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• When reading transparent liquid in a measuring jug or cylinder, always view horizontally at eye level and read at the **bottom of the meniscus**.\n"
        f"• Value of each subdivision = ${subdiv_ml}\\text{{ ml}}$.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Volume in ml}} = {base_ml}\\text{{ ml}} + ({ticks} \\times {subdiv_ml}\\text{{ ml}}) = {base_ml} + {extra_ml} = {total_ml}\\text{{ ml}}$$\n"
        f"$$\\text{{Volume in litres}} = \\frac{{{total_ml}}}{{1\\ 000}} = {_fmt(total_l)}\\text{{ l}}$$\n"
        f"✓ **[1 Mark: Method – adding meniscus subdivision intervals to base mark and dividing by 1 000]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct volume in ml and litres]**"
    )
    return _make_q(
        subskill="meas_vol_jug_meniscus_reading",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – base ml + ticks × subdiv and convert to l", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Each tick represents {subdiv_ml} ml. Read the bottom of the meniscus at eye level.",
            "tier_2": f"Add {ticks} × {subdiv_ml} ml = {extra_ml} ml to {base_ml} ml.",
            "tier_3": f"{base_ml} + {extra_ml} = {total_ml} ml ({_fmt(total_l)} l)."
        },
        r=r
    )

def _gen_meas_vol_measuring_cylinder_precision(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    mark_ml = r.choice([35, 42, 68, 75, 84])
    capacity_ml = 100
    prompt = (
        f"In a science class experiment, {name} measures water volume using a **100 ml graduated measuring cylinder** "
        f"calibrated with 1 ml divisions. The water level meniscus aligns precisely with the **{mark_ml} ml graduation line**.\n\n"
        f"1. State the measured volume in millilitres (**ml**).\n"
        f"2. Convert this measurement to cubic centimetres (**cm³**), given that $1\\text{{ ml}} = 1\\text{{ cm}}^3$."
    )
    ans_str = f"{mark_ml} ml ({mark_ml} cm³)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• The direct reading on the cylinder scale is **{mark_ml} ml**.\n"
        f"• Fundamental metric capacity equivalence: $1\\text{{ ml}} = 1\\text{{ cm}}^3$.\n\n"
        f"**Step 2: Method Setup & Equivalence**\n"
        f"$$\\text{{Volume in cm³}} = {mark_ml}\\text{{ ml}} \\times 1\\text{{ cm³/ml}} = {mark_ml}\\text{{ cm³}}$$\n"
        f"✓ **[1 Mark: Method – recognizing the 1:1 equivalence between ml and cm³]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct ml and cm³ representation]**"
    )
    return _make_q(
        subskill="meas_vol_measuring_cylinder_precision",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 1 ml = 1 cm³ equivalence", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "1 millilitre (ml) is exactly equal to 1 cubic centimetre (cm³).",
            "tier_2": f"Volume in ml is {mark_ml} ml.",
            "tier_3": f"{mark_ml} ml = {mark_ml} cm³."
        },
        r=r
    )

def _gen_meas_vol_office_urn_tea_servings(r: random.Random) -> Dict[str, Any]:
    urn_litres = r.choice([12, 15, 16, 20, 24])
    urn_ml = urn_litres * 1000
    cup_ml = 250
    cups_count = urn_ml // cup_ml
    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} manages an office kitchen where an electric hot water urn has a maximum liquid capacity of **{urn_litres} litres**.\n\n"
        f"Given that **1 metric cup = 250 ml**, how many full cups of tea can be served when the urn is filled to maximum capacity?"
    )
    ans_str = f"{cups_count} cups"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• First convert urn capacity from litres to millilitres ($1\\text{{ litre}} = 1\\ 000\\text{{ ml}}$):\n"
        f"  $$\\text{{Urn capacity in ml}} = {urn_litres} \\times 1\\ 000 = {urn_ml}\\text{{ ml}}$$\n\n"
        f"**Step 2: Method Setup & Division**\n"
        f"$$\\text{{Number of cups}} = \\frac{{{urn_ml}\\text{{ ml}}}}{{{cup_ml}\\text{{ ml/cup}}}} = {cups_count}\\text{{ cups}}$$\n"
        f"✓ **[1 Mark: Method – converting litres to ml and dividing by cup volume]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{cups_count}\\text{{ cups}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct number of servings]**"
    )
    return _make_q(
        subskill="meas_vol_office_urn_tea_servings",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (litres × 1000) ÷ 250", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Convert {urn_litres} litres to millilitres: {urn_litres} × 1 000 = {urn_ml} ml.",
            "tier_2": f"Divide total ml by 250 ml per cup: {urn_ml} ÷ 250.",
            "tier_3": f"{urn_ml} ÷ 250 = {cups_count} cups."
        },
        r=r
    )

def _gen_meas_vol_urn_percentage_remaining(r: random.Random) -> Dict[str, Any]:
    total_l = r.choice([15, 20, 25])
    remaining_l = r.choice([3, 4, 5, 6, 8])
    while remaining_l >= total_l:
        remaining_l -= 2
    percent_rem = round((remaining_l / total_l) * 100.0, 1)
    prompt = (
        f"A hot water urn at a community hall has a total capacity of **{total_l} litres**. "
        f"After a morning tea break, exactly **{remaining_l} litres** of water remain in the urn.\n\n"
        f"Calculate the percentage of the urn's capacity that still contains water."
    )
    ans_str = f"{_fmt(percent_rem)}%"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• To find the percentage remaining, divide the remaining volume by the total capacity and multiply by 100%:\n"
        f"  $$\\text{{Percentage remaining}} = \\left(\\frac{{\\text{{Remaining volume}}}}{{\\text{{Total capacity}}}}\\right) \\times 100\\%$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Percentage}} = \\left(\\frac{{{remaining_l}}}{{{total_l}}}\\right) \\times 100\\% = {_fmt(percent_rem)}\\%$$\n"
        f"✓ **[1 Mark: Method – remaining volume divided by total volume times 100]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct percentage]**"
    )
    return _make_q(
        subskill="meas_vol_urn_percentage_remaining",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (remaining ÷ total) × 100", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide remaining volume ({remaining_l} l) by total capacity ({total_l} l).",
            "tier_2": f"({remaining_l} ÷ {total_l}) × 100.",
            "tier_3": f"Result: {ans_str}."
        },
        r=r
    )

def _gen_meas_vol_garden_bucket_trips(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    bucket_l = r.choice([8, 10, 12, 15])
    total_l = r.choice([160, 240, 300, 360, 450])
    trips = total_l // bucket_l
    substance = r.choice(["borehole water to irrigate raised tomato vegetable beds", "liquid organic seaweed fertilizer for tomato seedlings", "fresh water for poultry drinking troughs in a chicken coop", "liquid compost tea for cabbage and spinach patches"])
    prompt = (
        f"{name} is irrigating a newly planted orchard bed with **{total_l} litres** of {substance}. "
        f"{name} carries the liquid using a garden bucket with a capacity of **{bucket_l} litres**, filling it to the top on every trip.\n\n"
        f"How many full trips must {name} make to transport all {total_l} litres?"
    )
    ans_str = f"{trips} trips"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• To find the number of trips, divide the total liquid volume by the bucket capacity:\n"
        f"  $$\\text{{Number of trips}} = \\frac{{\\text{{Total Volume}}}}{{\\text{{Bucket Capacity}}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Number of trips}} = \\frac{{{total_l}\\text{{ litres}}}}{{{bucket_l}\\text{{ litres/trip}}}} = {trips}\\text{{ trips}}$$\n"
        f"✓ **[1 Mark: Method – dividing total volume by bucket volume]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{trips}\\text{{ trips}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct number of bucket trips]**"
    )
    return _make_q(
        subskill="meas_vol_garden_bucket_trips",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total volume ÷ bucket capacity", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide total volume ({total_l} l) by bucket capacity ({bucket_l} l).",
            "tier_2": f"{total_l} ÷ {bucket_l}.",
            "tier_3": f"{total_l} ÷ {bucket_l} = {trips} trips."
        },
        r=r
    )

def _gen_meas_vol_medicine_liquid_dosage_duration(r: random.Random) -> Dict[str, Any]:
    dose_ml = r.choice([5, 7.5, 10, 15])
    times_daily = r.choice([2, 3])
    days = r.choice([5, 7, 10])
    total_ml = round(dose_ml * times_daily * days, 1)
    prompt = (
        f"A medical clinic prescription directs a patient to take a cough syrup dosage of "
        f"**{_fmt(dose_ml)} ml**, **{times_daily} times per day**, for a duration of **{days} consecutive days**.\n\n"
        f"Calculate the total volume of cough syrup in millilitres (**ml**) required to complete the full treatment course."
    )
    ans_str = f"{_fmt(total_ml)} ml"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Calculate the daily volume by multiplying single dose by doses per day:\n"
        f"  $$\\text{{Daily volume}} = {_fmt(dose_ml)}\\text{{ ml}} \\times {times_daily} = {_fmt(round(dose_ml * times_daily, 1))}\\text{{ ml/day}}$$\n\n"
        f"**Step 2: Method Setup & Full Course Calculation**\n"
        f"$$\\text{{Total Volume}} = {_fmt(round(dose_ml * times_daily, 1))}\\text{{ ml/day}} \\times {days}\\text{{ days}} = {_fmt(total_ml)}\\text{{ ml}}$$\n"
        f"✓ **[1 Mark: Method – dose per intake × frequency per day × duration in days]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total volume in ml]**"
    )
    return _make_q(
        subskill="meas_vol_medicine_liquid_dosage_duration",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – dose × frequency × days", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Daily dose = {_fmt(dose_ml)} ml × {times_daily} = {_fmt(round(dose_ml * times_daily, 1))} ml.",
            "tier_2": f"Multiply daily dose by {days} days.",
            "tier_3": f"{_fmt(round(dose_ml * times_daily, 1))} × {days} = {ans_str}."
        },
        r=r
    )

def _gen_meas_vol_medicine_dosage_bottles_to_buy(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_needed_ml = r.choice([120, 140, 175, 220, 260])
    bottle_size_ml = 100
    bottles_to_buy = math.ceil(total_needed_ml / bottle_size_ml)
    total_purchased_ml = bottles_to_buy * bottle_size_ml
    leftover_ml = total_purchased_ml - total_needed_ml
    prompt = (
        f"{name} needs a total volume of **{total_needed_ml} ml** of pediatric antibiotic liquid for a child. "
        f"The pharmacy only dispenses the medicine in **{bottle_size_ml} ml sealed bottles**.\n\n"
        f"1. How many bottles must {name} purchase to have enough medicine?\n"
        f"2. How many millilitres of medicine will remain unused after completing the course?"
    )
    ans_str = f"{bottles_to_buy} bottles ({leftover_ml} ml leftover)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Medicine cannot be purchased in open partial bottles. To guarantee enough volume, round UP to the next whole bottle:\n"
        f"  $$\\text{{Bottles}} = \\lceil \\frac{{{total_needed_ml}}}{{{bottle_size_ml}}} \\rceil = {bottles_to_buy}\\text{{ bottles}}$$\n\n"
        f"**Step 2: Method Setup & Leftover Calculation**\n"
        f"$$\\text{{Total purchased}} = {bottles_to_buy} \\times {bottle_size_ml}\\text{{ ml}} = {total_purchased_ml}\\text{{ ml}}$$\n"
        f"$$\\text{{Leftover volume}} = {total_purchased_ml}\\text{{ ml}} - {total_needed_ml}\\text{{ ml}} = {leftover_ml}\\text{{ ml}}$$\n"
        f"✓ **[1 Mark: Method – dividing required volume by bottle size, rounding up, and finding difference]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct bottles to buy and remaining volume]**"
    )
    return _make_q(
        subskill="meas_vol_medicine_dosage_bottles_to_buy",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – round up required volume ÷ bottle size", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide {total_needed_ml} ml by {bottle_size_ml} ml and round UP to the next whole bottle.",
            "tier_2": f"{total_needed_ml} ÷ {bottle_size_ml} = {total_needed_ml / bottle_size_ml:.2f} -> {bottles_to_buy} bottles.",
            "tier_3": f"{bottles_to_buy} × {bottle_size_ml} - {total_needed_ml} = {leftover_ml} ml leftover."
        },
        r=r
    )

def _gen_meas_vol_paint_spreading_rate_litres(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    area_m2 = r.choice([48, 64, 72, 80, 96, 120])
    spread_rate = r.choice([6, 8, 10])  # m² per litre
    coats = r.choice([1, 2])
    total_coverage_m2 = area_m2 * coats
    litres_needed = round(total_coverage_m2 / spread_rate, 1)
    prompt = (
        f"{name} is painting the interior walls of a classroom with a total surface area of **{area_m2} m²**. "
        f"The paint specifications on the tin state a spreading rate of **{spread_rate} m² per litre per coat**. "
        f"The specifications require **{coats} coat(s)** of paint.\n\n"
        f"Calculate the total volume of paint required in litres (**l**)."
    )
    ans_str = f"{_fmt(litres_needed)} l"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Total area to cover = $\\text{{Wall area}} \\times \\text{{coats}} = {area_m2}\\text{{ m²}} \\times {coats} = {total_coverage_m2}\\text{{ m²}}$.\n"
        f"• Litres required equals total area divided by spreading rate per litre:\n"
        f"  $$\\text{{Litres required}} = \\frac{{\\text{{Total Coverage Area}}}}{{\\text{{Spreading Rate}}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Litres}} = \\frac{{{total_coverage_m2}\\text{{ m²}}}}{{{spread_rate}\\text{{ m²/l}}}} = {_fmt(litres_needed)}\\text{{ litres}}$$\n"
        f"✓ **[1 Mark: Method – dividing total coverage area by spreading rate]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct volume in litres]**"
    )
    return _make_q(
        subskill="meas_vol_paint_spreading_rate_litres",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (area × coats) ÷ spreading rate", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Total area = {area_m2} m² × {coats} = {total_coverage_m2} m².",
            "tier_2": f"Divide total area by spreading rate: {total_coverage_m2} ÷ {spread_rate}.",
            "tier_3": f"{total_coverage_m2} ÷ {spread_rate} = {ans_str}."
        },
        r=r
    )

def _gen_meas_vol_paint_can_sizes_selection(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    litres_needed = r.choice([7, 11, 12, 14])
    price_5l = 280.00
    price_1l = 75.00
    # Option A: Buy in 5l tins (rounded up)
    tins_5l_only = math.ceil(litres_needed / 5.0)
    cost_5l_only = tins_5l_only * price_5l
    # Option B: Optimal combo (max 5l tins + remaining in 1l tins)
    num_5l = litres_needed // 5
    rem_litres = litres_needed % 5
    cost_combo = (num_5l * price_5l) + (rem_litres * price_1l)
    best_cost = min(cost_5l_only, cost_combo)
    if cost_combo < cost_5l_only:
        best_desc = f"{num_5l} × 5 l tin(s) and {rem_litres} × 1 l tin(s) ({_fmt_curr(best_cost)})"
    else:
        best_desc = f"{tins_5l_only} × 5 l tin(s) ({_fmt_curr(best_cost)})"
    prompt = (
        f"{name} needs **{litres_needed} litres** of exterior roof paint. The hardware store sells:\n\n"
        f"• **5-litre tin**: {_fmt_curr(price_5l)}\n"
        f"• **1-litre tin**: {_fmt_curr(price_1l)}\n\n"
        f"Determine the most cost-effective combination of tins to purchase and the total minimum cost."
    )
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Compare total costs of available purchasing options:\n"
        f"  - Option 1 (5 l tins only): {litres_needed} l requires {tins_5l_only} × 5 l tins = ${tins_5l_only} \\times {_fmt_curr(price_5l)} = {_fmt_curr(cost_5l_only)}$.\n"
        f"  - Option 2 (Combination): {num_5l} × 5 l tin(s) + {rem_litres} × 1 l tin(s) = $({num_5l} \\times 280) + ({rem_litres} \\times 75) = {_fmt_curr(cost_combo)}$.\n\n"
        f"**Step 2: Method Setup & Cost Comparison**\n"
        f"• Comparing {_fmt_curr(cost_5l_only)} vs {_fmt_curr(cost_combo)} shows the cheaper combination is **{best_desc}**.\n"
        f"✓ **[1 Mark: Method – comparing alternative tin purchase combinations]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{best_desc}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct optimal tin combination and minimum cost]**"
    )
    return _make_q(
        subskill="meas_vol_paint_can_sizes_selection",
        prompt=prompt,
        answer=best_desc,
        sol=sol,
        rubric=["1 Mark: Method – cost comparison of packaging options", f"1 Mark: Accuracy – {best_desc}"],
        hints={
            "tier_1": f"Compare buying {tins_5l_only} × 5 l tins ({_fmt_curr(cost_5l_only)}) vs {num_5l} × 5 l + {rem_litres} × 1 l ({_fmt_curr(cost_combo)}).",
            "tier_2": "Select the combination with the lower overall total cost.",
            "tier_3": f"Best purchase: {best_desc}."
        },
        r=r
    )

def _gen_meas_vol_fuel_tank_fillup_cost(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    tank_capacity_l = r.choice([45, 50, 55, 60, 70])
    fuel_price_per_l = round(r.choice([21.85, 22.40, 23.15, 24.10]), 2)
    total_cost = round(tank_capacity_l * fuel_price_per_l, 2)
    fuel_type = r.choice(["Unleaded 95 petrol", "50ppm diesel"])
    prompt = (
        f"{name} stops at a service station with an empty fuel tank of capacity **{tank_capacity_l} litres**. "
        f"The pump price board indicates {fuel_type} costs **{_fmt_curr(fuel_price_per_l)} per litre**.\n\n"
        f"Calculate the total cost to fill the vehicle's tank to maximum capacity."
    )
    ans_str = _fmt_curr(total_cost)
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• The total cost to fill the tank equals tank capacity multiplied by unit fuel price per litre:\n"
        f"  $$\\text{{Total Cost}} = \\text{{Tank Capacity in litres}} \\times \\text{{Price per litre}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total Cost}} = {tank_capacity_l}\\text{{ l}} \\times \\text{{{_fmt_curr(fuel_price_per_l)}}} = \\text{{{_fmt_curr(total_cost)}}}$\\n"
        f"✓ **[1 Mark: Method – multiplying capacity in litres by price per litre]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct Rand cost to fill the tank]**"
    )
    return _make_q(
        subskill="meas_vol_fuel_tank_fillup_cost",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – capacity × price per litre", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Cost = Capacity (in litres) × Price per litre.",
            "tier_2": f"Multiply {tank_capacity_l} by {_fmt_curr(fuel_price_per_l)}.",
            "tier_3": f"{tank_capacity_l} × {_fmt_curr(fuel_price_per_l)} = {ans_str}."
        },
        r=r
    )

def _gen_meas_vol_fuel_litres_from_cash_budget(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    budget = r.choice([200.0, 300.0, 400.0, 500.0])
    price_per_l = round(r.choice([18.50, 21.20, 22.80, 23.50]), 2)
    litres = round(budget / price_per_l, 2)
    fuel_type = r.choice(["illuminating paraffin", "unleaded petrol", "diesel"])
    prompt = (
        f"{name} has a fixed cash budget of **{_fmt_curr(budget)}** to purchase {fuel_type}. "
        f"The retail price is **{_fmt_curr(price_per_l)} per litre**.\n\n"
        f"Calculate the maximum number of litres {name} can purchase. Round your answer to **two decimal places**."
    )
    ans_str = f"{_fmt(litres)} litres"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• To find the volume purchased from a fixed cash budget, divide total budget by unit price per litre:\n"
        f"  $$\\text{{Litres}} = \\frac{{\\text{{Budget Amount}}}}{{\\text{{Price per litre}}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Litres}} = \\frac{{\\text{{{_fmt_curr(budget)}}}}}{{\\text{{{_fmt_curr(price_per_l)}}}}} = {_fmt(litres)}\\text{{ litres}}$$\n"
        f"✓ **[1 Mark: Method – dividing cash budget by unit price per litre]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct volume rounded to 2 decimal places]**"
    )
    return _make_q(
        subskill="meas_vol_fuel_litres_from_cash_budget",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – budget ÷ price per litre", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Litres = Budget ÷ Price per litre.",
            "tier_2": f"Divide {_fmt_curr(budget)} by {_fmt_curr(price_per_l)}.",
            "tier_3": f"{_fmt_curr(budget)} ÷ {_fmt_curr(price_per_l)} = {ans_str}."
        },
        r=r
    )

def _gen_meas_vol_paraffin_lamp_refills(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    lamp_ml = r.choice([400, 500, 600, 750])
    bulk_l = r.choice([2, 3, 5])
    bulk_ml = bulk_l * 1000
    refills = bulk_ml // lamp_ml
    rem_ml = bulk_ml % lamp_ml
    prompt = (
        f"{name} uses an illuminating paraffin heater with a tank capacity of **{lamp_ml} ml**. "
        f"{name} purchases a **{bulk_l}-litre container** of paraffin from a local distributor.\n\n"
        f"1. How many complete times can {name} refill the heater?\n"
        f"2. How many millilitres of paraffin will remain in the container?"
    )
    ans_str = f"{refills} complete refills ({rem_ml} ml remaining)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Convert the bulk container capacity to millilitres ($1\\text{{ l}} = 1\\ 000\\text{{ ml}}$):\n"
        f"  $$\\text{{Container volume}} = {bulk_l} \\times 1\\ 000 = {bulk_ml}\\text{{ ml}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Refills}} = \\lfloor \\frac{{{bulk_ml}}}{{{lamp_ml}}} \\rfloor = {refills}\\text{{ complete refills}}$$\n"
        f"$$\\text{{Remainder}} = {bulk_ml} - ({refills} \\times {lamp_ml}) = {rem_ml}\\text{{ ml}}$$\n"
        f"✓ **[1 Mark: Method – converting litres to ml and integer division with remainder]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct complete refills and remaining millilitres]**"
    )
    return _make_q(
        subskill="meas_vol_paraffin_lamp_refills",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – bulk ml ÷ lamp ml integer division", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Convert {bulk_l} litres to ml: {bulk_l} × 1 000 = {bulk_ml} ml.",
            "tier_2": f"Divide {bulk_ml} ml by {lamp_ml} ml.",
            "tier_3": f"{bulk_ml} ÷ {lamp_ml} = {refills} with {rem_ml} ml leftover."
        },
        r=r
    )

def _gen_meas_vol_beverage_cost_per_litre(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    can_ml = 500
    can_price = r.choice([9.50, 11.00, 12.50])
    can_unit = round(can_price / (can_ml / 1000.0), 2)
    bottle_l = 2.0
    bottle_price = r.choice([16.00, 18.00, 20.00])
    bottle_unit = round(bottle_price / bottle_l, 2)
    diff = round(abs(can_unit - bottle_unit), 2)
    cheaper = "2-litre bottle" if bottle_unit < can_unit else "500 ml can"
    drink = r.choice(["pure apple juice", "fresh full cream milk", "flavoured iced tea", "sparkling mineral water"])
    prompt = (
        f"{name} compares two packaging options for {drink}:\n\n"
        f"• **Option A**: 500 ml bottle at **{_fmt_curr(can_price)}**\n"
        f"• **Option B**: 2-litre bottle at **{_fmt_curr(bottle_price)}**\n\n"
        f"1. Calculate the price per litre for each option.\n"
        f"2. Determine which option is cheaper per litre and calculate the saving per litre."
    )
    ans_str = f"{cheaper} is cheaper by {_fmt_curr(diff)}/l"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Calculate unit cost per 1 litre for both options:\n"
        f"  - Option A (500 ml = 0,5 l): $\\frac{{{_fmt_curr(can_price)}}}{{0{{,}}5\\text{{ l}}}} = {_fmt_curr(can_unit)}\\text{{/l}}$\n"
        f"  - Option B (2 litres): $\\frac{{{_fmt_curr(bottle_price)}}}{{2\\text{{ l}}}} = {_fmt_curr(bottle_unit)}\\text{{/l}}$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Difference per litre}} = {_fmt_curr(can_unit)} - {_fmt_curr(bottle_unit)} = {_fmt_curr(diff)}\\text{{/l}}$$\n"
        f"✓ **[1 Mark: Method – calculating both unit rates per litre and finding difference]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct cheaper option and Rand saving per litre]**"
    )
    return _make_q(
        subskill="meas_vol_beverage_cost_per_litre",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – unit rates per litre and difference", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Option A: {_fmt_curr(can_price)} ÷ 0,5 l = {_fmt_curr(can_unit)}/l.",
            "tier_2": f"Option B: {_fmt_curr(bottle_price)} ÷ 2 l = {_fmt_curr(bottle_unit)}/l.",
            "tier_3": f"{cheaper} is cheaper by {_fmt_curr(diff)} per litre."
        },
        r=r
    )

# ==============================================================================
