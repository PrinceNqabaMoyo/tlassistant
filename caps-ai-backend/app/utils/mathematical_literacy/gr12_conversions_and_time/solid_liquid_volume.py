"""Subskills 01 to 08: Solid, liquid, and calculated volume conversions (cm3, m3, ml, litres, kl, density)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_frac,
    _fmt_pct,
)


def generate_01_calculated_volume_to_liquid_litres(r: random.Random) -> Dict[str, Any]:
    """Convert calculated rectangular volume from cubic centimetres (cm3) to millilitres and litres."""
    l = r.choice([20, 25, 30, 40])
    w = r.choice([15, 20, 25])
    h = r.choice([6, 8, 10, 12])
    vol_cm3 = l * w * h  # e.g. 25 * 20 * 8 = 4000 cm3
    vol_ml = vol_cm3
    vol_litres = vol_ml / 1000.0

    correct_ans = f"Volume = {_fmt(vol_cm3, 0)} cm³ = {_fmt(vol_ml, 0)} ml = {_fmt(vol_litres, 2)} ℓ"

    custom_options = [
        correct_ans,
        f"Volume = {_fmt(vol_cm3, 0)} cm³ = {_fmt(vol_litres * 10, 2)} ℓ",
        f"Volume = {_fmt(vol_cm3, 0)} cm³ = {_fmt(vol_litres / 10, 3)} ℓ",
        f"Volume = {_fmt(l + w + h, 0)} cm³ = {_fmt((l + w + h) / 1000, 3)} ℓ",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A glass baking dish has internal dimensions of length {l} cm, width {w} cm, and depth {h} cm.\n\n"
        f"Using the conversion factors:\n"
        f"• 1 cm³ = 1 ml\n"
        f"• 1 000 ml = 1 ℓ\n\n"
        f"Calculate the liquid capacity of the dish in cubic centimetres (cm³), millilitres (ml), and litres (ℓ)."
    )
    explanation = (
        f"Step 1: Calculate volume: V = l × w × h = {l} cm × {w} cm × {h} cm = {_fmt(vol_cm3, 0)} cm³ [M].\n"
        f"Step 2: Convert to millilitres: {_fmt(vol_cm3, 0)} cm³ = {_fmt(vol_ml, 0)} ml [M].\n"
        f"Step 3: Convert to litres: {_fmt(vol_ml, 0)} ÷ 1 000 = {_fmt(vol_litres, 2)} ℓ [A]."
    )
    return _build_question_payload(
        subskill_id="01_calculated_volume_to_liquid_litres",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply length × width × height to get cm³. 1 cm³ = 1 ml, and 1 000 ml = 1 litre.",
        tier_2=f"Volume = {l} × {w} × {h} = {vol_cm3} cm³. Divide by 1 000 to get litres.",
        tier_3=f"{vol_cm3} cm³ = {_fmt(vol_litres, 2)} ℓ.",
        r=r,
    )


def generate_02_cubic_metres_to_kilolitres(r: random.Random) -> Dict[str, Any]:
    """Convert calculated foundation excavation or water reservoir volume from m3 to kilolitres and litres."""
    vol_m3 = round(r.uniform(2.4, 8.5), 1)  # e.g. 3.5 m3
    vol_kl = vol_m3
    vol_litres = int(vol_m3 * 1000)

    correct_ans = f"{_fmt(vol_m3, 1)} m³ = {_fmt(vol_kl, 1)} kl = {_fmt(vol_litres, 0)} ℓ"

    custom_options = [
        correct_ans,
        f"{_fmt(vol_m3, 1)} m³ = {_fmt(vol_m3 * 10, 1)} kl = {_fmt(vol_litres * 10, 0)} ℓ",
        f"{_fmt(vol_m3, 1)} m³ = {_fmt(vol_m3 / 1000, 4)} kl = {_fmt(vol_m3, 1)} ℓ",
        f"{_fmt(vol_m3, 1)} m³ = {_fmt(vol_kl, 1)} kl = {_fmt(vol_m3 * 100, 0)} ℓ",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An underground concrete rainwater storage reservoir has a calculated internal capacity of {_fmt(vol_m3, 1)} m³.\n\n"
        f"Using the conversion standards:\n"
        f"• 1 m³ = 1 kl\n"
        f"• 1 kl = 1 000 ℓ\n\n"
        f"Convert this capacity into kilolitres (kl) and total litres (ℓ)."
    )
    explanation = (
        f"Step 1: Apply the direct identity 1 m³ = 1 kl: {_fmt(vol_m3, 1)} m³ = {_fmt(vol_kl, 1)} kl [M].\n"
        f"Step 2: Multiply by 1 000 to convert kilolitres to litres: {_fmt(vol_kl, 1)} × 1 000 [M].\n"
        f"Step 3: Total capacity = {_fmt(vol_litres, 0)} ℓ [A]."
    )
    return _build_question_payload(
        subskill_id="02_cubic_metres_to_kilolitres",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="1 cubic metre equals 1 kilolitre. 1 kilolitre equals 1 000 litres.",
        tier_2=f"{vol_m3} m³ = {vol_m3} kl. Multiply by 1 000 to find litres.",
        tier_3=f"{_fmt(vol_m3, 1)} m³ = {_fmt(vol_kl, 1)} kl = {_fmt(vol_litres, 0)} ℓ.",
        r=r,
    )


def generate_03_millimetres_cubed_to_millilitres(r: random.Random) -> Dict[str, Any]:
    """Convert small medical vial or laboratory pipette volumes from mm3 to millilitres."""
    l_mm = r.choice([20, 25, 30])
    w_mm = r.choice([10, 15, 20])
    h_mm = r.choice([15, 20, 25])
    vol_mm3 = l_mm * w_mm * h_mm  # e.g. 25 * 10 * 20 = 5000 mm3
    vol_cm3 = vol_mm3 / 1000.0  # 5.0 cm3
    vol_ml = vol_cm3  # 5.0 ml

    correct_ans = f"Volume = {_fmt(vol_mm3, 0)} mm³ = {_fmt(vol_cm3, 1)} cm³ = {_fmt(vol_ml, 1)} ml"

    custom_options = [
        correct_ans,
        f"Volume = {_fmt(vol_mm3, 0)} mm³ = {_fmt(vol_cm3 * 10, 1)} cm³ = {_fmt(vol_ml * 10, 1)} ml",
        f"Volume = {_fmt(vol_mm3, 0)} mm³ = {_fmt(vol_cm3 / 10, 2)} cm³ = {_fmt(vol_ml / 10, 2)} ml",
        f"Volume = {_fmt(vol_mm3, 0)} mm³ = {_fmt(vol_mm3, 0)} ml",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A rectangular glass testing cell used in a pathology laboratory measures {l_mm} mm by {w_mm} mm by {h_mm} mm.\n\n"
        f"Given that:\n"
        f"• 1 000 mm³ = 1 cm³\n"
        f"• 1 cm³ = 1 ml\n\n"
        f"Calculate the volume of the cell in cubic millimetres (mm³), cubic centimetres (cm³), and millilitres (ml)."
    )
    explanation = (
        f"Step 1: Calculate volume: V = {l_mm} × {w_mm} × {h_mm} = {_fmt(vol_mm3, 0)} mm³ [M].\n"
        f"Step 2: Convert to cm³ by dividing by 1 000: {_fmt(vol_mm3, 0)} ÷ 1 000 = {_fmt(vol_cm3, 1)} cm³ [M].\n"
        f"Step 3: Since 1 cm³ = 1 ml, the volume is {_fmt(vol_ml, 1)} ml [A]."
    )
    return _build_question_payload(
        subskill_id="03_millimetres_cubed_to_millilitres",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There are 1 000 mm³ in 1 cm³, and 1 cm³ equals 1 ml.",
        tier_2=f"Volume in mm³ = {vol_mm3}. Divide by 1 000 to get cm³ and ml.",
        tier_3=f"Volume = {_fmt(vol_mm3, 0)} mm³ = {_fmt(vol_ml, 1)} ml.",
        r=r,
    )


def generate_04_liquid_volume_to_mass_density(r: random.Random) -> Dict[str, Any]:
    """Convert liquid volume in litres to mass in kilograms using liquid density."""
    liquid, density = r.choice([
        ("Sunflower cooking oil", 0.92),
        ("Diesel fuel", 0.835),
        ("Petrol (unleaded)", 0.74),
        ("Milk (full cream)", 1.03),
    ])
    litres = r.choice([20, 25, 40, 50, 60, 200])
    mass_kg = litres * density

    correct_ans = f"Mass = {litres} ℓ × {_fmt(density, 3)} kg/ℓ = {_fmt(mass_kg, 2)} kg"

    custom_options = [
        correct_ans,
        f"Mass = {litres} ℓ ÷ {_fmt(density, 3)} = {_fmt(litres / density, 2)} kg",
        f"Mass = {litres} kg",
        f"Mass = {_fmt(mass_kg * 10, 1)} kg",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A commercial delivery truck carries a drum holding {litres} litres of {liquid}.\n"
        f"The density of {liquid} is given as {_fmt(density, 3)} kg per litre (1 ℓ has a mass of {_fmt(density, 3)} kg).\n\n"
        f"Calculate the mass of the liquid in kilograms (kg)."
    )
    explanation = (
        f"Step 1: Identify the relationship: Mass = Volume (ℓ) × Density (kg/ℓ) [M].\n"
        f"Step 2: Multiply: {litres} × {_fmt(density, 3)} [M].\n"
        f"Step 3: Mass = {_fmt(mass_kg, 2)} kg [A]."
    )
    return _build_question_payload(
        subskill_id="04_liquid_volume_to_mass_density",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the volume in litres by the mass per litre (density).",
        tier_2=f"Mass = {litres} × {density}.",
        tier_3=f"Mass = {_fmt(mass_kg, 2)} kg.",
        r=r,
    )


def generate_05_cylindrical_tank_capacity_litres(r: random.Random) -> Dict[str, Any]:
    """Calculate the liquid capacity of a cylindrical JoJo rainwater tank in litres."""
    radius_m = r.choice([0.75, 0.90, 1.00, 1.10])
    height_m = r.choice([1.80, 2.00, 2.20, 2.50])
    # V = pi * r^2 * h
    pi_val = 3.14159
    vol_m3 = pi_val * (radius_m ** 2) * height_m
    litres = round(vol_m3 * 1000.0)

    correct_ans = f"Volume = {_fmt(vol_m3, 3)} m³ = {_fmt(litres, 0)} ℓ (approx {_fmt(round(litres / 100) * 100, 0)} ℓ)"

    custom_options = [
        correct_ans,
        f"Volume = {_fmt(vol_m3 * 10, 2)} m³ = {_fmt(litres * 10, 0)} ℓ",
        f"Volume = {_fmt(vol_m3 / 10, 3)} m³ = {_fmt(round(litres / 10), 0)} ℓ",
        f"Volume = {_fmt(2 * pi_val * radius_m * height_m, 2)} m³ = {_fmt(round(2 * pi_val * radius_m * height_m * 1000), 0)} ℓ",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A cylindrical JoJo rainwater harvesting tank has an internal radius of {_fmt(radius_m, 2)} m and a height of {_fmt(height_m, 2)} m.\n\n"
        f"Formula: Volume = π × (radius)² × height (Use π = 3,14159)\n"
        f"Conversion: 1 m³ = 1 000 ℓ\n\n"
        f"Calculate the volume of the tank in cubic metres (m³) and find its water capacity in litres (ℓ), rounded to the nearest litre."
    )
    explanation = (
        f"Step 1: Substitute dimensions into cylinder volume formula: V = 3,14159 × ({_fmt(radius_m, 2)})² × {_fmt(height_m, 2)} [M].\n"
        f"Step 2: V = 3,14159 × {round(radius_m**2, 4)} × {_fmt(height_m, 2)} = {_fmt(vol_m3, 3)} m³ [M].\n"
        f"Step 3: Convert to litres: {_fmt(vol_m3, 3)} × 1 000 = {_fmt(litres, 0)} ℓ [A]."
    )
    return _build_question_payload(
        subskill_id="05_cylindrical_tank_capacity_litres",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate volume using V = π × r² × h, then multiply m³ by 1 000 to convert to litres.",
        tier_2=f"V = 3,14159 × ({radius_m})² × {height_m} = {_fmt(vol_m3, 3)} m³. Multiply by 1 000.",
        tier_3=f"Capacity = {_fmt(litres, 0)} ℓ.",
        r=r,
    )


def generate_06_swimming_pool_drainage_time(r: random.Random) -> Dict[str, Any]:
    """Calculate the time in hours and minutes required to drain a pool given pump discharge rate."""
    capacity_litres = r.choice([36000, 45000, 54000, 60000])
    pump_rate_lpm = r.choice([150, 200, 250])  # litres per minute
    total_minutes = capacity_litres / pump_rate_lpm
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)

    correct_ans = f"{int(total_minutes)} minutes = {hours} hours {minutes} minutes"

    custom_options = [
        correct_ans,
        f"{int(total_minutes + 60)} minutes = {hours + 1} hours {minutes} minutes",
        f"{int(total_minutes - 45)} minutes = {hours} hours {abs(minutes - 45)} minutes",
        f"{int(total_minutes * 1.5)} minutes = {int(hours * 1.5)} hours 0 minutes",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A residential swimming pool holding {_fmt(capacity_litres, 0)} litres of water must be drained for maintenance.\n"
        f"A submersible drainage pump discharges water at a constant rate of {pump_rate_lpm} litres per minute (ℓ/min).\n\n"
        f"Calculate the total time required to drain the pool completely. Express your answer in **hours and minutes**."
    )
    explanation = (
        f"Step 1: Calculate total minutes: {_fmt(capacity_litres, 0)} ℓ ÷ {pump_rate_lpm} ℓ/min = {int(total_minutes)} minutes [M].\n"
        f"Step 2: Convert minutes to hours and minutes: {int(total_minutes)} ÷ 60 = {hours} hours with a remainder of {minutes} minutes [M].\n"
        f"Step 3: Total drainage time = {hours} hours {minutes} minutes [A]."
    )
    return _build_question_payload(
        subskill_id="06_swimming_pool_drainage_time",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide pool capacity by the pump rate to find total minutes, then divide by 60.",
        tier_2=f"{capacity_litres} ÷ {pump_rate_lpm} = {int(total_minutes)} minutes. {int(total_minutes)} ÷ 60 = {hours} h {minutes} min.",
        tier_3=f"{hours} hours {minutes} minutes.",
        r=r,
    )


def generate_07_municipal_water_meter_kl_to_litres(r: random.Random) -> Dict[str, Any]:
    """Calculate monthly water consumption from meter readings in kl and find average daily litres."""
    prev_reading = r.randint(1420, 1850)
    days_in_month = 31
    kl_used = r.randint(18, 35)
    current_reading = prev_reading + kl_used

    total_litres = kl_used * 1000
    avg_daily_litres = round(total_litres / days_in_month, 1)

    correct_ans = f"Monthly = {kl_used} kl ({_fmt(total_litres, 0)} ℓ); Daily Average = {_fmt(avg_daily_litres, 1)} ℓ/day"

    custom_options = [
        correct_ans,
        f"Monthly = {kl_used} kl ({_fmt(total_litres, 0)} ℓ); Daily Average = {_fmt(round(total_litres / 30, 1), 1)} ℓ/day",
        f"Monthly = {current_reading} kl; Daily Average = {_fmt(round(current_reading * 1000 / 31, 1), 1)} ℓ/day",
        f"Monthly = {kl_used * 10} kl; Daily Average = {_fmt(avg_daily_litres * 10, 1)} ℓ/day",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    name = r.choice(SA_NAMES)
    prompt = (
        f"{name}'s municipal water meter readings for a {days_in_month}-day billing cycle are:\n"
        f"• Previous reading (1 July): {_fmt(prev_reading, 0)} kl\n"
        f"• Current reading (1 August): {_fmt(current_reading, 0)} kl\n\n"
        f"1. Calculate the total water consumed during July in kilolitres (kl) and litres (ℓ).\n"
        f"2. Calculate the household's average daily water consumption in litres per day (ℓ/day), rounded to 1 decimal place."
    )
    explanation = (
        f"Step 1: Subtract readings: {_fmt(current_reading, 0)} - {_fmt(prev_reading, 0)} = {kl_used} kl [M].\n"
        f"Step 2: Convert to litres: {kl_used} × 1 000 = {_fmt(total_litres, 0)} ℓ [M].\n"
        f"Step 3: Average daily consumption: {_fmt(total_litres, 0)} ÷ {days_in_month} = {_fmt(avg_daily_litres, 1)} ℓ/day [A]."
    )
    return _build_question_payload(
        subskill_id="07_municipal_water_meter_kl_to_litres",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the previous meter reading from the current reading. 1 kl = 1 000 litres.",
        tier_2=f"{current_reading} - {prev_reading} = {kl_used} kl = {total_litres} ℓ. Divide by {days_in_month} days.",
        tier_3=f"Monthly = {kl_used} kl; Daily = {_fmt(avg_daily_litres, 1)} ℓ/day.",
        r=r,
    )


def generate_08_aggregate_sand_weight_to_volume(r: random.Random) -> Dict[str, Any]:
    """Convert building sand or crushed stone weight in tonnes to volume in m3 using bulk density."""
    tonnes_ordered = r.choice([9.6, 12.8, 16.0, 19.2])
    bulk_density = 1.6  # 1.6 tonnes per m3
    vol_m3 = round(tonnes_ordered / bulk_density, 1)  # e.g. 16.0 / 1.6 = 10.0 m3
    truck_capacity = 6.0  # 6 m3 tipper truck
    truck_loads = math.ceil(vol_m3 / truck_capacity)

    correct_ans = f"Volume = {_fmt(vol_m3, 1)} m³; Requires {truck_loads} truck loads (6 m³ tipper truck)"

    custom_options = [
        correct_ans,
        f"Volume = {_fmt(tonnes_ordered * bulk_density, 1)} m³; Requires {truck_loads + 1} truck loads",
        f"Volume = {_fmt(vol_m3, 1)} m³; Requires {math.floor(vol_m3 / truck_capacity)} truck loads",
        f"Volume = {_fmt(tonnes_ordered, 1)} m³; Requires {math.ceil(tonnes_ordered / truck_capacity)} truck loads",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A building contractor orders {_fmt(tonnes_ordered, 1)} tonnes of river sand for plastering.\n"
        f"• Bulk loose density of river sand: 1,6 tonnes per m³ (1 m³ has a mass of 1,6 tonnes)\n"
        f"• The supplier delivers aggregate using 6 m³ tipper trucks\n\n"
        f"1. Convert the ordered mass of river sand into volume in cubic metres (m³).\n"
        f"2. How many full 6 m³ tipper truck deliveries will be needed to deliver this sand?"
    )
    explanation = (
        f"Step 1: Volume = Mass (tonnes) ÷ Density (t/m³) = {_fmt(tonnes_ordered, 1)} ÷ 1,6 = {_fmt(vol_m3, 1)} m³ [M].\n"
        f"Step 2: Number of truck loads = {_fmt(vol_m3, 1)} ÷ 6 m³ = {vol_m3 / truck_capacity:.2f} loads [M].\n"
        f"Step 3: Round UP to the next whole load: {truck_loads} truck loads [A]."
    )
    return _build_question_payload(
        subskill_id="08_aggregate_sand_weight_to_volume",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide mass by bulk density (1,6 t/m³) to find volume in m³. Round truck loads UP.",
        tier_2=f"Volume = {tonnes_ordered} ÷ 1,6 = {vol_m3} m³. Loads = {vol_m3} ÷ 6.",
        tier_3=f"Volume = {_fmt(vol_m3, 1)} m³; Requires {truck_loads} truck loads.",
        r=r,
    )
