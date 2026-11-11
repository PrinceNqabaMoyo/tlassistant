from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

# CLUSTER 4: TEMPERATURE MEASUREMENT, WEATHER & THERMAL APPLICATIONS (8 Archetypes)
# ==============================================================================

def _gen_meas_temp_thermometer_types(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("monitoring a child's suspected fever at a clinic without contact", "Infrared non-contact forehead thermometer", ["Oven dial gauge", "Infrared non-contact forehead thermometer", "Hydrometer", "Soil probe thermometer"]),
        ("checking whether the centre of a roasted leg of lamb has reached a safe cooked temperature", "Probe meat thermometer", ["Clinical oral thermometer", "Probe meat thermometer", "Room wall thermometer", "Rain gauge"]),
        ("monitoring the daily maximum and minimum ambient outdoor temperatures for agricultural frost warnings", "Six's maximum-minimum weather thermometer", ["Infrared ear thermometer", "Six's maximum-minimum weather thermometer", "Meat thermometer", "Clinical thermometer"]),
        ("checking ambient living room comfort temperature in an eco-house", "Liquid-in-glass room wall thermometer", ["Oven temperature dial", "Liquid-in-glass room wall thermometer", "Probe thermometer", "Weighbridge"])
    ]
    task, correct_device, opts = r.choice(scenarios)
    prompt = (
        f"A user needs to select the most appropriate temperature measuring device for: **{task}**.\n\n"
        f"Identify the correct thermometer from the choices below."
    )
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Different thermometers are calibrated for specific temperature ranges and contact requirements:\n"
        f"  - Clinical body temperature (35 °C – 42 °C): Digital oral or infrared forehead thermometer\n"
        f"  - Food / butchery cooking (up to 120 °C): Long stainless steel probe thermometer\n"
        f"  - Weather forecasting: Maximum-minimum recording thermometer\n"
        f"  - Indoor ambient comfort: Wall thermometer\n\n"
        f"**Step 2: Method Setup & Instrument Evaluation**\n"
        f"• For {task}, the instrument designed specifically for this purpose is the **{correct_device}**.\n"
        f"✓ **[1 Mark: Method – matching thermal range and application to thermometer type]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{correct_device}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct thermometer selection]**"
    )
    return _make_q(
        subskill="meas_temp_thermometer_types",
        prompt=prompt,
        answer=correct_device,
        sol=sol,
        rubric=["1 Mark: Method – thermometer application matching", f"1 Mark: Accuracy – {correct_device}"],
        hints={
            "tier_1": "Consider whether the task requires measuring food, human body, weather, or room air.",
            "tier_2": f"Which tool is designed for {task}?",
            "tier_3": f"Correct tool: {correct_device}."
        },
        options=opts,
        r=r
    )

def _gen_meas_temp_reading_mercury_alcohol_column(r: random.Random) -> Dict[str, Any]:
    major_deg = r.choice([20, 25, 30, 35])
    subdiv = 1
    ticks = r.randint(1, 4)
    total_temp = major_deg + (ticks * subdiv)
    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} reads a laboratory red-alcohol liquid-in-glass thermometer to measure water temperature in a water bath. "
        f"The scale has numbered marks every 5 °C and subdivision lines every **1 °C**.\n\n"
        f"When reading horizontally at eye level, the top of the red liquid column rests **{ticks} small subdivision line(s) above the {major_deg} °C mark**.\n\n"
        f"Record the exact temperature measurement in degrees Celsius (**°C**)."
    )
    ans_str = f"{total_temp} °C"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Liquid-in-glass thermometers must always be read horizontally at the top of the liquid meniscus to avoid parallax error.\n"
        f"• Each subdivision line represents $1\\ \\text{{°C}}$.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Temperature}} = {major_deg}\\ \\text{{°C}} + ({ticks} \\times 1\\ \\text{{°C}}) = {total_temp}\\ \\text{{°C}}$$\n"
        f"✓ **[1 Mark: Method – reading scale subdivisions at eye level without parallax error]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{total_temp}\\ \\text{{°C}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct temperature in °C]**"
    )
    return _make_q(
        subskill="meas_temp_reading_mercury_alcohol_column",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – base temp + subdivision count", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Each small tick mark on this thermometer scale represents 1 °C.",
            "tier_2": f"Add {ticks} °C to {major_deg} °C.",
            "tier_3": f"{major_deg} + {ticks} = {total_temp} °C."
        },
        r=r
    )

def _gen_meas_temp_fever_threshold_interpretation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    temp = round(r.choice([37.6, 37.9, 38.2, 38.5, 38.8]), 1)
    baseline = 37.0
    fever_threshold = 37.5
    excess = round(temp - baseline, 1)
    prompt = (
        f"{name} feels unwell and uses a digital oral clinical thermometer to measure their body temperature. "
        f"The digital display shows **{_fmt(temp)} °C**.\n\n"
        f"Medical health standards define:\n"
        f"• Normal body temperature: **36,0 °C to 37,2 °C** (baseline: 37,0 °C)\n"
        f"• Fever threshold: Above **37,5 °C**\n\n"
        f"1. Does {name} have a fever?\n"
        f"2. By how many degrees Celsius does {name}'s temperature exceed the normal baseline of 37,0 °C?"
    )
    ans_str = f"Fever (exceeds baseline by {_fmt(excess)} °C)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Compare the measured temperature ({_fmt(temp)} °C) against the medical threshold ({fever_threshold} °C):\n"
        f"  - {_fmt(temp)} °C > {fever_threshold} °C $\\implies$ **The patient has a fever**.\n\n"
        f"**Step 2: Method Setup & Difference Calculation**\n"
        f"$$\\text{{Difference above baseline}} = {_fmt(temp)}\\ \\text{{°C}} - {_fmt(baseline)}\\ \\text{{°C}} = {_fmt(excess)}\\ \\text{{°C}}$$\n"
        f"✓ **[1 Mark: Method – comparing with threshold and calculating difference from baseline]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct fever diagnosis and numerical elevation]**"
    )
    return _make_q(
        subskill="meas_temp_fever_threshold_interpretation",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – compare threshold and subtract 37,0", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Compare {_fmt(temp)} °C to the fever threshold of {fever_threshold} °C.",
            "tier_2": f"Subtract 37,0 °C from {_fmt(temp)} °C.",
            "tier_3": f"{_fmt(temp)} - 37,0 = {_fmt(excess)} °C."
        },
        r=r
    )

def _gen_meas_temp_daily_body_temp_fluctuation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    mon = 36.2
    tue = 36.6
    wed = round(r.choice([38.2, 38.5, 38.8]), 1)  # peak fever
    thu = 37.8
    fri = 37.1
    sat = 36.5
    sun = 36.3
    lowest = min(mon, tue, wed, thu, fri, sat, sun)
    highest = max(mon, tue, wed, thu, fri, sat, sun)
    diff = round(highest - lowest, 1)
    prompt = (
        f"{name} monitors their body temperature daily for a week while recovering from an infection:\n\n"
        f"| Day | Mon | Tue | Wed | Thu | Fri | Sat | Sun |\n"
        f"| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
        f"| **Temp (°C)** | {_fmt(mon)} | {_fmt(tue)} | {_fmt(wed)} | {_fmt(thu)} | {_fmt(fri)} | {_fmt(sat)} | {_fmt(sun)} |\n\n"
        f"1. Identify the day and value of the highest temperature recorded.\n"
        f"2. Calculate the difference between the highest and lowest temperatures recorded during the week."
    )
    ans_str = f"Wednesday at {_fmt(highest)} °C (Difference: {_fmt(diff)} °C)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Scan the weekly record to identify extremes:\n"
        f"  - Peak temperature: Wednesday at {_fmt(highest)} °C\n"
        f"  - Lowest temperature: Monday at {_fmt(lowest)} °C\n\n"
        f"**Step 2: Method Setup & Difference Calculation**\n"
        f"$$\\text{{Temperature Range}} = {_fmt(highest)}\\ \\text{{°C}} - {_fmt(lowest)}\\ \\text{{°C}} = {_fmt(diff)}\\ \\text{{°C}}$$\n"
        f"✓ **[1 Mark: Method – identifying maximum and minimum and subtracting]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct peak day, temperature, and range]**"
    )
    return _make_q(
        subskill="meas_temp_daily_body_temp_fluctuation",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – identify max, min, and subtract", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Highest is Wednesday ({_fmt(highest)} °C). Lowest is Monday ({_fmt(lowest)} °C).",
            "tier_2": f"Subtract {_fmt(lowest)} from {_fmt(highest)}.",
            "tier_3": f"{_fmt(highest)} - {_fmt(lowest)} = {_fmt(diff)} °C."
        },
        r=r
    )

def _gen_meas_temp_weather_report_min_max(r: random.Random) -> Dict[str, Any]:
    cities = [
        ("Polokwane", 12, 28),
        ("Bloemfontein", 8, 25),
        ("George", 10, 22),
        ("Kimberley", 9, 27),
        ("Johannesburg", 11, 24)
    ]
    city, min_t, max_t = r.choice(cities)
    range_t = max_t - min_t
    prompt = (
        f"The official South African Weather Service forecast for **{city}** predicts:\n\n"
        f"• **Minimum temperature**: {min_t} °C\n"
        f"• **Maximum temperature**: {max_t} °C\n\n"
        f"Calculate the **diurnal temperature range** (the difference between the maximum and minimum temperatures) for {city}."
    )
    ans_str = f"{range_t} °C"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• The diurnal temperature range is defined as the difference between the daily maximum and daily minimum temperatures:\n"
        f"  $$\\text{{Temperature Range}} = \\text{{Maximum Temperature}} - \\text{{Minimum Temperature}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Temperature Range}} = {max_t}\\ \\text{{°C}} - {min_t}\\ \\text{{°C}} = {range_t}\\ \\text{{°C}}$$\n"
        f"✓ **[1 Mark: Method – subtracting minimum temperature from maximum temperature]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{range_t}\\ \\text{{°C}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct temperature range]**"
    )
    return _make_q(
        subskill="meas_temp_weather_report_min_max",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – Max temp minus Min temp", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Diurnal temperature range = Maximum temperature - Minimum temperature.",
            "tier_2": f"Subtract {min_t} °C from {max_t} °C.",
            "tier_3": f"{max_t} - {min_t} = {range_t} °C."
        },
        r=r
    )

def _gen_meas_temp_weather_sub_zero_frost(r: random.Random) -> Dict[str, Any]:
    min_t = -r.choice([3, 4, 5, 6])  # negative winter sub-zero
    max_t = r.choice([12, 14, 15, 16])
    total_change = max_t - min_t  # max - (-min) = max + abs(min)
    town = r.choice(["Sutherland (Northern Cape)", "Barkly East (Eastern Cape)", "Belfast (Mpumalanga)", "Tzaneen Agricultural Valley (Limpopo)"])
    prompt = (
        f"An agricultural weather warning alert is issued for vegetable and tomato growers in **{town}**. "
        f"On a cold winter night, the minimum temperature plummets to **{min_t} °C** (sub-zero frost capable of damaging vulnerable tomato crops). "
        f"By 14:00 the following afternoon, bright sunshine warms the air to a maximum temperature of **{max_t} °C**.\n\n"
        f"Calculate the total rise in temperature from the overnight low to the afternoon high in degrees Celsius (**°C**)."
    )
    ans_str = f"{total_change} °C"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• When calculating temperature rise across zero degrees Celsius, subtract the negative minimum from the positive maximum:\n"
        f"  $$\\text{{Temperature Rise}} = \\text{{Maximum}} - \\text{{Minimum}} = {max_t} - ({min_t})$$\n"
        f"• Subtracting a negative number is equivalent to addition: ${max_t} + {abs(min_t)} = {total_change}\\ \\text{{°C}}$.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total rise}} = {max_t} - ({min_t}) = {max_t} + {abs(min_t)} = {total_change}\\ \\text{{°C}}$$\n"
        f"✓ **[1 Mark: Method – correctly accounting for double negative subtraction across 0 °C]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{total_change}\\ \\text{{°C}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total temperature rise]**"
    )
    return _make_q(
        subskill="meas_temp_weather_sub_zero_frost",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – Max minus (Min) with sign handling", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Temperature rise = {max_t} - ({min_t}) = {max_t} + {abs(min_t)}.",
            "tier_2": f"Add {abs(min_t)} to {max_t}.",
            "tier_3": f"{max_t} - ({min_t}) = {total_change} °C."
        },
        r=r
    )

def _gen_meas_temp_oven_preheating_adjustment(r: random.Random) -> Dict[str, Any]:
    current_temp = r.choice([200, 220, 240])
    target_temp = r.choice([160, 180])
    drop = current_temp - target_temp
    prompt = (
        f"A domestic electric stove oven was used for grilling and is currently heated to **{current_temp} °C**. "
        f"A recipe for traditional rusks specifies baking at **{target_temp} °C**.\n\n"
        f"By how many degrees Celsius must the oven cool down before the rusks can be placed inside to bake?"
    )
    ans_str = f"Cool down by {drop} °C"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• To adjust baking temperature, subtract the desired target recipe temperature from the current oven temperature:\n"
        f"  $$\\text{{Required decrease}} = \\text{{Current Temperature}} - \\text{{Target Temperature}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Temperature Drop}} = {current_temp}\\ \\text{{°C}} - {target_temp}\\ \\text{{°C}} = {drop}\\ \\text{{°C}}$$\n"
        f"✓ **[1 Mark: Method – subtracting target baking temperature from current oven temperature]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct cooling adjustment in °C]**"
    )
    return _make_q(
        subskill="meas_temp_oven_preheating_adjustment",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – Current temp minus target temp", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Subtract target temperature ({target_temp} °C) from current temperature ({current_temp} °C).",
            "tier_2": f"{current_temp} - {target_temp}.",
            "tier_3": f"{current_temp} - {target_temp} = {drop} °C."
        },
        r=r
    )

def _gen_meas_temp_food_safety_danger_zone(r: random.Random) -> Dict[str, Any]:
    fridge_temp = r.choice([6, 7, 8, 9])
    safe_limit = 5
    excess = fridge_temp - safe_limit
    prompt = (
        f"South African Department of Health food safety standards specify that perishable agricultural produce, "
        f"dressed poultry (chicken carcasses), and dairy products must be kept out of the bacterial 'temperature danger zone' "
        f"(between 5 °C and 60 °C), meaning a farm walk-in cold room or refrigerator must maintain an internal temperature of **5 °C or below**.\n\n"
        f"A poultry farm cold storage display unit thermometer reads **{fridge_temp} °C**.\n\n"
        f"1. Is this cold room operating at a safe temperature?\n"
        f"2. By how many degrees Celsius is the temperature too warm?"
    )
    ans_str = f"Unsafe (Too warm by {excess} °C)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• The refrigerator temperature must be $\\le 5\\ \\text{{°C}}$ to prevent rapid bacterial growth.\n"
        f"• At {fridge_temp} °C, the temperature is higher than 5 °C $\\implies$ **Unsafe**.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Excess temperature}} = {fridge_temp}\\ \\text{{°C}} - {safe_limit}\\ \\text{{°C}} = {excess}\\ \\text{{°C too warm}}$$\n"
        f"✓ **[1 Mark: Method – evaluating safety threshold and finding difference above safe limit]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct safety verdict and numerical excess]**"
    )
    return _make_q(
        subskill="meas_temp_food_safety_danger_zone",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – comparison to 5 °C threshold and difference", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Safe refrigeration temperature must be 5 °C or colder.",
            "tier_2": f"Subtract 5 °C from {fridge_temp} °C.",
            "tier_3": f"{fridge_temp} - 5 = {excess} °C too warm."
        },
        r=r
    )


# ==============================================================================
# CLUSTER 5: INTEGRATED MEASUREMENT, RECIPE COSTING & MULTI-STEP APPLICATIONS (6 Archetypes)
# ==============================================================================

def _gen_meas_integ_recipe_multi_cake_scaling(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    batches = r.choice([4, 6, 8, 9])
    cups_per_cake = round(r.choice([1.5, 2.0, 2.5]), 1)
    total_cups = round(batches * cups_per_cake, 1)
    prompt = (
        f"{name} is baking **{batches} cakes** for a school fundraising cake sale. "
        f"The base recipe for a single cake requires **{_fmt(cups_per_cake)} metric cups** of self-raising flour.\n\n"
        f"Calculate the total number of metric cups of flour required to bake all {batches} cakes."
    )
    ans_str = f"{_fmt(total_cups)} metric cups"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Scale ingredient quantity proportionally by multiplying single batch requirement by number of batches:\n"
        f"  $$\\text{{Total cups}} = \\text{{Cakes}} \\times \\text{{Cups per cake}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total cups}} = {batches} \\times {_fmt(cups_per_cake)} = {_fmt(total_cups)}\\text{{ metric cups}}$$\n"
        f"✓ **[1 Mark: Method – multiplying batch count by ingredient quantity per unit]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{_fmt(total_cups)}\\text{{ metric cups}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct scaled cups of flour]**"
    )
    return _make_q(
        subskill="meas_integ_recipe_multi_cake_scaling",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – batches × cups per cake", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Multiply {batches} cakes by {_fmt(cups_per_cake)} cups per cake.",
            "tier_2": f"{batches} × {_fmt(cups_per_cake)}.",
            "tier_3": f"{batches} × {_fmt(cups_per_cake)} = {ans_str}."
        },
        r=r
    )

def _gen_meas_integ_recipe_liquid_volume_litres(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    cakes = r.choice([4, 6, 8])
    milk_ml = 250
    oil_ml = 125
    liquid_per_cake = milk_ml + oil_ml  # 375 ml
    total_ml = cakes * liquid_per_cake
    total_litres = round(total_ml / 1000.0, 3)
    prompt = (
        f"{name} prepares liquid ingredients to bake **{cakes} cakes**. Each cake requires:\n\n"
        f"• **{milk_ml} ml** of full cream milk\n"
        f"• **{oil_ml} ml** of sunflower cooking oil\n\n"
        f"Calculate the total combined volume of liquid required for all {cakes} cakes in litres (**l**)."
    )
    ans_str = f"{_fmt(total_litres)} l"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Find liquid volume per cake: ${milk_ml}\\text{{ ml}} + {oil_ml}\\text{{ ml}} = {liquid_per_cake}\\text{{ ml}}$.\n"
        f"• Total ml for {cakes} cakes = ${cakes} \\times {liquid_per_cake}\\text{{ ml}} = {total_ml}\\text{{ ml}}$.\n\n"
        f"**Step 2: Method Setup & Conversion to Litres**\n"
        f"$$\\text{{Total litres}} = \\frac{{{total_ml}\\text{{ ml}}}}{{1\\ 000}} = {_fmt(total_litres)}\\text{{ litres}}$$\n"
        f"✓ **[1 Mark: Method – summing liquids per cake, multiplying by cakes, and dividing by 1 000]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct volume in litres]**"
    )
    return _make_q(
        subskill="meas_integ_recipe_liquid_volume_litres",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (liquid per cake × cakes) ÷ 1000", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Liquid per cake = {milk_ml} ml + {oil_ml} ml = {liquid_per_cake} ml.",
            "tier_2": f"Total ml = {cakes} × {liquid_per_cake} ml = {total_ml} ml.",
            "tier_3": f"{total_ml} ml ÷ 1 000 = {ans_str}."
        },
        r=r
    )

def _gen_meas_integ_recipe_eggs_box_packaging(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    hens = r.choice([20, 25, 30, 35, 40])
    eggs_per_hen = r.choice([5, 6, 7])
    total_eggs = hens * eggs_per_hen
    box_size = r.choice([6, 12])  # 6-egg half-dozen or 12-egg dozen cartons
    boxes_packed = total_eggs // box_size
    leftover = total_eggs % box_size
    carton_name = "half-dozen cartons (6 eggs)" if box_size == 6 else "dozen cartons (12 eggs)"
    prompt = (
        f"{name} operates a smallholder poultry farming project with free-range layer chickens. "
        f"Over the weekend, {name} collects **{total_eggs} fresh eggs** from the chicken coop nesting boxes. "
        f"The eggs are packed into commercial **{carton_name}** for distribution to local spaza shops and farm stalls.\n\n"
        f"1. How many full {box_size}-egg cartons can {name} pack?\n"
        f"2. How many loose eggs will be left over?"
    )
    ans_str = f"{boxes_packed} cartons ({leftover} leftover eggs)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• To find full cartons, divide total eggs collected by carton capacity using integer division:\n"
        f"  $$\\text{{Full cartons}} = \\lfloor \\frac{{{total_eggs}}}{{{box_size}}} \\rfloor = {boxes_packed}\\text{{ cartons}}$$\n\n"
        f"**Step 2: Method Setup & Leftover Remainder Calculation**\n"
        f"• Calculate eggs packed: ${boxes_packed} \\times {box_size} = {boxes_packed * box_size}\\text{{ eggs}}$.\n"
        f"• Leftover loose eggs = ${total_eggs} - {boxes_packed * box_size} = {leftover}\\text{{ loose eggs}}$.\n"
        f"✓ **[1 Mark: Method – integer division by {box_size} and remainder calculation]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct full cartons and leftover egg count]**"
    )
    d_spec = {
        "diagram_role": "context",
        "kind": "packaging_packing",
        "carton_l": total_eggs,
        "box_l": box_size,
        "title": f"Egg Packaging Arrangement ({total_eggs} eggs in {box_size}-packs)",
    }
    return _make_q(
        diagram_spec=d_spec,
        subskill="meas_integ_recipe_eggs_box_packaging",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total eggs ÷ 6 round up, find leftover", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide total eggs ({total_eggs}) by carton size ({box_size}).",
            "tier_2": f"Full cartons = {total_eggs} // {box_size} = {boxes_packed} cartons.",
            "tier_3": f"Leftover = {total_eggs} % {box_size} = {leftover} loose eggs."
        },
        r=r
    )

def _gen_meas_integ_recipe_ingredient_costing(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    egg_cartons = r.choice([3, 4, 5])
    egg_price = r.choice([24.50, 26.00, 28.50])
    vanilla_bottles = r.choice([2, 3])
    vanilla_price = r.choice([14.20, 16.50, 18.00])
    total_cost = round((egg_cartons * egg_price) + (vanilla_bottles * vanilla_price), 2)
    prompt = (
        f"{name} purchases baking ingredients for a school tuckshop event:\n\n"
        f"• **{egg_cartons} cartons of eggs** at **{_fmt_curr(egg_price)} per carton**\n"
        f"• **{vanilla_bottles} bottles of vanilla essence** at **{_fmt_curr(vanilla_price)} per bottle**\n\n"
        f"Calculate the total cost of these ingredients."
    )
    ans_str = _fmt_curr(total_cost)
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Calculate cost of each item type: Quantity × Unit Price.\n"
        f"• Sum the costs to find the total invoice amount.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Eggs Cost}} = {egg_cartons} \\times {_fmt_curr(egg_price)} = {_fmt_curr(round(egg_cartons * egg_price, 2))}$$\n"
        f"$$\\text{{Vanilla Cost}} = {vanilla_bottles} \\times {_fmt_curr(vanilla_price)} = {_fmt_curr(round(vanilla_bottles * vanilla_price, 2))}$$\n"
        f"$$\\text{{Total Cost}} = {_fmt_curr(round(egg_cartons * egg_price, 2))} + {_fmt_curr(round(vanilla_bottles * vanilla_price, 2))} = {_fmt_curr(total_cost)}$$\n"
        f"✓ **[1 Mark: Method – calculating product of quantities and unit prices and summing]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total expenditure]**"
    )
    return _make_q(
        subskill="meas_integ_recipe_ingredient_costing",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (cartons × price) + (bottles × price)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Eggs: {egg_cartons} × {_fmt_curr(egg_price)} = {_fmt_curr(round(egg_cartons * egg_price, 2))}.",
            "tier_2": f"Vanilla: {vanilla_bottles} × {_fmt_curr(vanilla_price)} = {_fmt_curr(round(vanilla_bottles * vanilla_price, 2))}.",
            "tier_3": f"Total: {_fmt_curr(round(egg_cartons * egg_price, 2))} + {_fmt_curr(round(vanilla_bottles * vanilla_price, 2))} = {ans_str}."
        },
        r=r
    )

def _gen_meas_integ_garden_lawn_fertilizer_coverage(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    length = r.choice([15, 20, 25])
    width = r.choice([10, 12, 14])
    area_m2 = length * width
    g_per_m2 = 50
    total_g = area_m2 * g_per_m2
    total_kg = total_g / 1000.0
    bag_size = 5  # 5 kg bags
    bags_needed = math.ceil(total_kg / bag_size)
    prompt = (
        f"{name} manages a commercial vegetable garden with a rectangular tomato growing bed measuring **{length} m in length** and **{width} m in width** ($Area = length \\times width$).\n\n"
        f"Agricultural organic fertilizer must be applied at a rate of **{g_per_m2} g per m²** before planting tomato seedlings. "
        f"The local agricultural co-op sells fertilizer in **{bag_size} kg bags**.\n\n"
        f"1. Calculate the total area of the tomato bed in m².\n"
        f"2. How many kilograms of fertilizer are required?\n"
        f"3. How many {bag_size} kg bags must {name} purchase?"
    )
    ans_str = f"{bags_needed} bags ({area_m2} m², {_fmt(total_kg)} kg required)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Lawn area = ${length}\\text{{ m}} \\times {width}\\text{{ m}} = {area_m2}\\text{{ m²}}$.\n"
        f"• Total fertilizer in grams = ${area_m2}\\text{{ m²}} \\times {g_per_m2}\\text{{ g/m²}} = {total_g}\\text{{ g}}$.\n"
        f"• In kilograms: ${total_g} \\div 1\\ 000 = {_fmt(total_kg)}\\text{{ kg}}$.\n\n"
        f"**Step 2: Method Setup & Bag Calculation**\n"
        f"$$\\text{{Bags to purchase}} = \\lceil \\frac{{{_fmt(total_kg)}}}{{{bag_size}}} \\rceil = {bags_needed}\\text{{ bags}}$$\n"
        f"✓ **[1 Mark: Method – calculating area, mass in kg, and rounding up bags division]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct area, mass required, and bags to purchase]**"
    )
    return _make_q(
        subskill="meas_integ_garden_lawn_fertilizer_coverage",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – area × rate ÷ 1000, then divide by bag size", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Area = {length} × {width} = {area_m2} m².",
            "tier_2": f"Total kg = ({area_m2} × {g_per_m2}) ÷ 1 000 = {_fmt(total_kg)} kg.",
            "tier_3": f"Bags needed = {_fmt(total_kg)} ÷ {bag_size} = {bags_needed} bags."
        },
        r=r
    )

def _gen_meas_integ_rainwater_harvesting_tank_days(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    tank_l = r.choice([2500, 5000])
    daily_usage_l = r.choice([100, 125, 200, 250])
    days = tank_l // daily_usage_l
    prompt = (
        f"{name} installs a rooftop rainwater harvesting JoJo tank with a maximum capacity of **{_fmt(tank_l)} litres**. "
        f"The stored water is used to drip-irrigate an open-field tomato patch and provide clean drinking water for a broiler chicken coop, consuming an average of **{daily_usage_l} litres of water per day**.\n\n"
        f"Assuming no rainfall occurs, how many full days of watering will a completely full tank provide?"
    )
    ans_str = f"{days} days"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• To determine the duration of water storage, divide the total volume stored by the average daily consumption rate:\n"
        f"  $$\\text{{Days of water}} = \\frac{{\\text{{Tank Capacity in litres}}}}{{\\text{{Daily Consumption in litres/day}}}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Days}} = \\frac{{{_fmt(tank_l)}\\text{{ litres}}}}{{{daily_usage_l}\\text{{ litres/day}}}} = {days}\\text{{ days}}$$\n"
        f"✓ **[1 Mark: Method – dividing tank capacity by daily consumption rate]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{days}\\text{{ days}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct number of days]**"
    )
    return _make_q(
        subskill="meas_integ_rainwater_harvesting_tank_days",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – tank capacity ÷ daily usage", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide total tank capacity ({_fmt(tank_l)} l) by daily usage ({daily_usage_l} l).",
            "tier_2": f"{tank_l} ÷ {daily_usage_l}.",
            "tier_3": f"{tank_l} ÷ {daily_usage_l} = {days} days."
        },
        r=r
    )


# ==============================================================================
