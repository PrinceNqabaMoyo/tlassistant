"""Temperature and compound rates conversions (Subskills 28-36) for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_CITIES,
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def generate_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Celsius to Fahrenheit weather forecast (°F = (°C × 1,8) + 32)."""
    city = r.choice(SA_CITIES)
    deg_c = r.randint(18, 38)
    deg_f = round((deg_c * 1.8) + 32, 1)
    ans_str = f"{_fmt(deg_f)} °F"

    prompt = (
        f"A weather report forecasts a maximum temperature of {deg_c} °C in {city}. "
        f"An American tourist staying in {city} asks for this temperature in degrees Fahrenheit (°F).\n"
        f"Calculate the temperature in °F.\n"
        f"*(Given formula: °F = (°C × 1,8) + 32. Round to 1 decimal place if necessary.)*"
    )
    explanation = (
        f"Step 1: State the formula for converting °C to °F:\n"
        f"°\\text{{F}} = (°\\text{{C}} \\times 1,8) + 32. [1 mark]\n"
        f"Step 2: Substitute {deg_c} °C into the formula:\n"
        f"°\\text{{F}} = ({deg_c} \\times 1,8) + 32 = {deg_c * 1.8:.1f} + 32 [1 mark]\n"
        f"Step 3: Add to get the final Fahrenheit temperature:\n"
        f"\\text{{Temperature}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round((deg_c * 1.8) - 32, 1))} °F",
        f"{_fmt(round((deg_c - 32) / 1.8, 1))} °F",
        f"{_fmt(round(deg_c * 1.8, 1))} °F",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_28",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply °C by 1,8, then add 32.",
        f"Calculate ({deg_c} × 1,8) + 32.",
        f"Temperature = {ans_str}.",
        r,
    )


def generate_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Fahrenheit to Celsius medical thermometer/fever (°C = (°F - 32) ÷ 1,8)."""
    name = r.choice(SA_NAMES)
    deg_f = r.choice([99.5, 100.4, 101.3, 102.2, 103.1, 104.0])
    deg_c = round((deg_f - 32) / 1.8, 1)
    ans_str = f"{_fmt(deg_c)} °C"

    prompt = (
        f"{name}'s digital thermometer displays a body temperature of {_fmt(deg_f)} °F. "
        f"A South African clinic nurse needs to record the reading in degrees Celsius (°C).\n"
        f"Calculate the temperature in °C.\n"
        f"*(Given formula: °C = (°F - 32) ÷ 1,8. Round to 1 decimal place.)*"
    )
    explanation = (
        f"Step 1: Write down the conversion formula:\n"
        f"°\\text{{C}} = (°\\text{{F}} - 32) \\div 1,8. [1 mark]\n"
        f"Step 2: Subtract 32 from {_fmt(deg_f)} and divide by 1,8:\n"
        f"°\\text{{C}} = ({_fmt(deg_f)} - 32) \\div 1,8 = {deg_f - 32:.2f} \\div 1,8 [1 mark]\n"
        f"Step 3: State the resulting Celsius temperature:\n"
        f"\\text{{Body temperature}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round((deg_f * 1.8) + 32, 1))} °C",
        f"{_fmt(round((deg_f - 32) * 1.8, 1))} °C",
        f"{_fmt(round(deg_f / 1.8, 1))} °C",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_29",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract 32 first, then divide the result by 1,8.",
        f"Calculate ({_fmt(deg_f)} - 32) ÷ 1,8.",
        f"Temperature = {ans_str}.",
        r,
    )


def generate_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Baking oven temperature conversion (°C to °F)."""
    name = r.choice(SA_NAMES)
    c_temp = r.choice([160, 180, 200, 220])
    f_temp = int(round((c_temp * 1.8) + 32))
    ans_str = f"{f_temp} °F"

    prompt = (
        f"{name} is using an imported American baking oven that only has temperature settings in °F. "
        f"A recipe instructs baking rusks at {c_temp} °C.\n"
        f"To what temperature in °F should {name} set the oven?\n"
        f"*(Given formula: °F = (°C × 1,8) + 32.)*"
    )
    explanation = (
        f"Step 1: State the formula: °\\text{{F}} = (°\\text{{C}} \\times 1,8) + 32. [1 mark]\n"
        f"Step 2: Multiply {c_temp} by 1,8 and add 32:\n"
        f"°\\text{{F}} = ({c_temp} \\times 1,8) + 32 = {c_temp * 1.8:.0f} + 32 [1 mark]\n"
        f"Step 3: State the oven setting:\n"
        f"\\text{{Oven temperature}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{f_temp - 25} °F",
        f"{f_temp + 25} °F",
        f"{int(round(c_temp * 1.8))} °F",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_30",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate (°C × 1,8) + 32.",
        f"Calculate ({c_temp} × 1,8) + 32.",
        f"Setting = {ans_str}.",
        r,
    )


def generate_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Gas mark table to Celsius and Fahrenheit."""
    gas_marks = [
        (1, 140, 275),
        (2, 150, 300),
        (3, 160, 325),
        (4, 180, 350),
        (5, 190, 375),
        (6, 200, 400),
        (7, 220, 425),
    ]
    gm, c_val, f_val = r.choice(gas_marks)
    name = r.choice(SA_NAMES)
    ans_str = f"{c_val} °C"

    prompt = (
        f"{name} is using an antique British recipe book that specifies baking a roast at Gas Mark {gm}.\n"
        f"The conversion reference card states:\n"
        f"• Gas Mark 1 = 140 °C (275 °F)\n"
        f"• Gas Mark 2 = 150 °C (300 °F)\n"
        f"• Gas Mark 3 = 160 °C (325 °F)\n"
        f"• Gas Mark 4 = 180 °C (350 °F)\n"
        f"• Gas Mark 5 = 190 °C (375 °F)\n"
        f"• Gas Mark 6 = 200 °C (400 °F)\n"
        f"• Gas Mark 7 = 220 °C (425 °F)\n\n"
        f"Determine the corresponding temperature in degrees Celsius (°C) for Gas Mark {gm}."
    )
    explanation = (
        f"Step 1: Locate Gas Mark {gm} in the reference table. [1 mark]\n"
        f"Step 2: Read across to the corresponding Celsius column value. [1 mark]\n"
        f"Step 3: State the matching temperature:\n"
        f"\\text{{Temperature}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{c_val - 20} °C",
        f"{c_val + 20} °C",
        f"{f_val} °C",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_31",
        prompt,
        ans_str,
        options,
        explanation,
        f"Look up Gas Mark {gm} in the provided table.",
        f"Find the Celsius equivalent for Gas Mark {gm}.",
        f"Gas Mark {gm} = {ans_str}.",
        r,
    )


def generate_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Fuel consumption: L/100 km to km/L (km/L = 100 ÷ (L/100km))."""
    name = r.choice(SA_NAMES)
    l_per_100km = r.choice([5.0, 6.25, 6.4, 7.5, 8.0, 10.0, 12.5])
    km_per_l = round(100.0 / l_per_100km, 2)
    ans_str = f"{_fmt(km_per_l)} km/L"

    prompt = (
        f"{name}'s car dashboard shows an average fuel consumption of {_fmt(l_per_100km)} L/100 km.\n"
        f"Convert this rate to kilometres per litre (km/L).\n"
        f"*(Given formula: km/L = 100 ÷ (L/100 km). Round to 2 decimal places if needed.)*"
    )
    explanation = (
        f"Step 1: State the conversion formula between L/100 km and km/L:\n"
        f"\\text{{km/L}} = 100 \\div (\\text{{L/100 km}}). [1 mark]\n"
        f"Step 2: Divide 100 by {_fmt(l_per_100km)}:\n"
        f"\\text{{km/L}} = 100 \\div {_fmt(l_per_100km)} [1 mark]\n"
        f"Step 3: State the final rate:\n"
        f"\\text{{Rate}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(l_per_100km / 100, 3))} km/L",
        f"{_fmt(round(100 - l_per_100km, 1))} km/L",
        f"{_fmt(round(km_per_l * 1.2, 2))} km/L",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_32",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide 100 by the fuel consumption in L/100 km.",
        f"Calculate 100 ÷ {_fmt(l_per_100km)}.",
        f"Consumption rate = {ans_str}.",
        r,
    )


def generate_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Fuel consumption: km/L to L/100 km (L/100km = 100 ÷ (km/L))."""
    name = r.choice(SA_NAMES)
    km_per_l = r.choice([12.0, 14.0, 15.0, 16.0, 18.0, 20.0])
    l_per_100km = round(100.0 / km_per_l, 2)
    ans_str = f"{_fmt(l_per_100km)} L/100 km"

    prompt = (
        f"An economy delivery motorcycle achieves a fuel efficiency of {_fmt(km_per_l)} km/L. "
        f"{name} needs to express this in standard South African automobile specification units (L/100 km).\n"
        f"Calculate the fuel consumption in L/100 km.\n"
        f"*(Given formula: L/100 km = 100 ÷ (km/L). Round to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: State the formula: \\text{{L/100 km}} = 100 \\div (\\text{{km/L}}). [1 mark]\n"
        f"Step 2: Divide 100 by {_fmt(km_per_l)}:\n"
        f"100 \\div {_fmt(km_per_l)} = {100 / km_per_l:.3f} [1 mark]\n"
        f"Step 3: Round off to 2 decimal places:\n"
        f"\\text{{Fuel consumption}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(100 / (km_per_l + 2), 2))} L/100 km",
        f"{_fmt(round(km_per_l / 100, 3))} L/100 km",
        f"{_fmt(round(l_per_100km + 1.5, 2))} L/100 km",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_33",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide 100 by the kilometres per litre.",
        f"Calculate 100 ÷ {_fmt(km_per_l)}.",
        f"Consumption = {ans_str}.",
        r,
    )


def generate_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Flow rate: L/min to m³/h (1 m³/h = 1 000 L / 60 min ≈ 16,67 L/min)."""
    name = r.choice(SA_NAMES)
    l_per_min = r.choice([30, 45, 60, 75, 90, 120, 150])
    # 1 L/min = 60 L/hour = 60 / 1000 m3/hour = 0.06 m3/hour
    m3_per_hour = round(l_per_min * 60 / 1000, 2)
    ans_str = f"{_fmt(m3_per_hour)} m³/h"

    prompt = (
        f"A borehole water pump on {name}'s smallholding pumps water at a flow rate of "
        f"{l_per_min} litres per minute (L/min).\n"
        f"Calculate the pumping rate in cubic metres per hour (m³/h).\n"
        f"*(Given: 1 m³ = 1 000 litres; 1 hour = 60 minutes.)*"
    )
    explanation = (
        f"Step 1: Calculate the litres pumped per hour:\n"
        f"\\text{{Hourly rate}} = {l_per_min} \\times 60 = {l_per_min * 60}\\text{{ L/h}}. [1 mark]\n"
        f"Step 2: Convert litres per hour to cubic metres per hour by dividing by 1 000:\n"
        f"\\text{{Rate in m}}^3/\\text{{h}} = {l_per_min * 60} \\div 1\\,000 [1 mark]\n"
        f"Step 3: State the final rate:\n"
        f"\\text{{Flow rate}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(l_per_min / 60, 2))} m³/h",
        f"{_fmt(round(l_per_min * 1000 / 60, 1))} m³/h",
        f"{_fmt(round(m3_per_hour * 10, 2))} m³/h",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_34",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply L/min by 60 to get L/h, then divide by 1 000 to get m³/h.",
        f"Calculate ({l_per_min} × 60) ÷ 1 000.",
        f"Flow rate = {ans_str}.",
        r,
    )


def generate_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Compound volume loss from a dripping tap over days/months."""
    name = r.choice(SA_NAMES)
    drips_per_min = r.choice([20, 30, 40, 50])
    ml_per_drip = 0.25
    days = 30
    # drips in 30 days = drips_per_min * 60 * 24 * days
    total_drips = drips_per_min * 60 * 24 * days
    total_ml = total_drips * ml_per_drip
    total_litres = round(total_ml / 1000, 1)
    ans_str = f"{_fmt(total_litres)} L"

    prompt = (
        f"A leaking garden tap at {name}'s school drips at an average rate of {drips_per_min} drops per minute. "
        f"Each water drop has an estimated volume of 0,25 mL.\n"
        f"Calculate the total volume of water wasted in litres (L) over a 30-day month.\n"
        f"*(Given: 1 day = 24 hours; 1 hour = 60 minutes; 1 litre = 1 000 mL.)*"
    )
    explanation = (
        f"Step 1: Calculate total minutes in 30 days:\n"
        f"\\text{{Minutes}} = 30 \\times 24 \\times 60 = 43\\,200\\text{{ minutes}}. [1 mark]\n"
        f"Step 2: Find total volume in millilitres:\n"
        f"\\text{{Total drops}} = {drips_per_min} \\times 43\\,200 = {total_drips:,}\\text{{ drops}}\n"
        f"\\text{{Volume in mL}} = {total_drips:,} \\times 0,25 = {total_ml:,.0f}\\text{{ mL}} [1 mark]\n"
        f"Step 3: Convert mL to litres by dividing by 1 000:\n"
        f"\\text{{Volume wasted}} = {total_ml:,.0f} \\div 1\\,000 = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(total_litres / 10, 1))} L",
        f"{_fmt(round(total_litres * 1.5, 1))} L",
        f"{_fmt(round(total_ml / 60, 1))} L",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_35",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate total minutes in 30 days, multiply by drips/min and volume/drip, then divide by 1 000.",
        f"Total minutes = 30 × 24 × 60 = 43 200 min. Litres = (43 200 × {drips_per_min} × 0,25) ÷ 1 000.",
        f"Wasted volume = {ans_str}.",
        r,
    )


def generate_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Liquid density mass-to-volume conversion (mass = volume × density)."""
    name = r.choice(SA_NAMES)
    density = 0.92  # Cooking oil density in g/mL
    volume_l = r.choice([2, 5, 10, 20])
    volume_ml = volume_l * 1000
    mass_g = round(volume_ml * density, 1)
    mass_kg = round(mass_g / 1000, 2)
    ans_str = f"{_fmt(mass_kg)} kg"

    prompt = (
        f"{name} runs a bakery and orders a {volume_l}-litre container of sunflower cooking oil. "
        f"The density of sunflower cooking oil is 0,92 g/mL.\n"
        f"Calculate the mass of the cooking oil in kilograms (kg).\n"
        f"*(Given formula: \\text{{Mass}} = \\text{{Volume (in mL)}} \\times \\text{{Density}}; 1 L = 1 000 mL; 1 kg = 1 000 g.)*"
    )
    explanation = (
        f"Step 1: Convert volume from litres to millilitres:\n"
        f"\\text{{Volume}} = {volume_l} \\times 1\\,000 = {volume_ml}\\text{{ mL}}. [1 mark]\n"
        f"Step 2: Calculate mass in grams using the density formula:\n"
        f"\\text{{Mass in grams}} = {volume_ml} \\times 0,92 = {mass_g:,.0f}\\text{{ g}} [1 mark]\n"
        f"Step 3: Convert grams to kilograms by dividing by 1 000:\n"
        f"\\text{{Mass in kg}} = {mass_g:,.0f} \\div 1\\,000 = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(volume_l)} kg",
        f"{_fmt(round(volume_l / 0.92, 2))} kg",
        f"{_fmt(round(mass_kg * 1.1, 2))} kg",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_36",
        prompt,
        ans_str,
        options,
        explanation,
        "Convert litres to mL, multiply by density to get grams, then divide by 1 000 to get kg.",
        f"Volume = {volume_ml} mL. Mass = ({volume_ml} × 0,92) ÷ 1 000.",
        f"Mass = {ans_str}.",
        r,
    )
