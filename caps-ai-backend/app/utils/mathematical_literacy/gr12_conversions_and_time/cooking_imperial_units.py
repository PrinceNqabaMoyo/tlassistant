"""Subskills 25 to 32: Cooking, baking, recipe scaling, oven temperatures, and imperial-to-metric conversions."""
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


def generate_25_recipe_cups_tablespoons_to_ml(r: random.Random) -> Dict[str, Any]:
    """Convert recipe volume units (cups, tablespoons, teaspoons) to millilitres."""
    cups = r.choice([1.5, 2.0, 2.5, 3.0])
    tbsp = r.choice([2, 3, 4])
    tsp = r.choice([1, 2, 3])

    ml_from_cups = cups * 250.0   # 1 cup = 250 ml
    ml_from_tbsp = tbsp * 15.0    # 1 tbsp = 15 ml
    ml_from_tsp = tsp * 5.0       # 1 tsp = 5 ml
    total_ml = ml_from_cups + ml_from_tbsp + ml_from_tsp

    correct_ans = f"Total = {_fmt(total_ml, 0)} ml ({_fmt(cups, 1)} cups = {_fmt(ml_from_cups, 0)} ml, {tbsp} tbsp = {int(ml_from_tbsp)} ml, {tsp} tsp = {int(ml_from_tsp)} ml)"

    custom_options = [
        correct_ans,
        f"Total = {_fmt(total_ml + 100, 0)} ml ({_fmt(cups, 1)} cups = {_fmt(ml_from_cups + 100, 0)} ml)",
        f"Total = {_fmt(total_ml / 10, 1)} ml",
        f"Total = {_fmt((cups + tbsp + tsp) * 50, 0)} ml",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A South African milk tart recipe requires the following liquid ingredients:\n"
        f"• {_fmt(cups, 1)} cups of full-cream milk (1 cup = 250 ml)\n"
        f"• {tbsp} tablespoons of condensed milk (1 tbsp = 15 ml)\n"
        f"• {tsp} teaspoons of vanilla extract (1 tsp = 5 ml)\n\n"
        f"Calculate the total volume of these liquid ingredients in millilitres (ml)."
    )
    explanation = (
        f"Step 1: Milk: {_fmt(cups, 1)} × 250 ml = {_fmt(ml_from_cups, 0)} ml [M].\n"
        f"Step 2: Condensed milk: {tbsp} × 15 ml = {int(ml_from_tbsp)} ml; Vanilla: {tsp} × 5 ml = {int(ml_from_tsp)} ml [M].\n"
        f"Step 3: Total = {_fmt(ml_from_cups, 0)} + {int(ml_from_tbsp)} + {int(ml_from_tsp)} = {_fmt(total_ml, 0)} ml [A]."
    )
    return _build_question_payload(
        subskill_id="25_recipe_cups_tablespoons_to_ml",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="1 cup = 250 ml, 1 tablespoon = 15 ml, 1 teaspoon = 5 ml.",
        tier_2=f"({cups} × 250) + ({tbsp} × 15) + ({tsp} × 5) = {total_ml} ml.",
        tier_3=f"Total = {_fmt(total_ml, 0)} ml.",
        r=r,
    )


def generate_26_scaling_recipe_yield_quantities(r: random.Random) -> Dict[str, Any]:
    """Scale recipe ingredient quantities proportionally from a base serving size to a large gathering."""
    base_servings = 6
    target_servings = r.choice([30, 36, 42, 48, 60])
    scale_factor = target_servings / base_servings  # e.g. 60 / 6 = 10

    base_flour_g = 500.0  # 500 g
    base_butter_g = 125.0
    base_sugar_g = 200.0

    scaled_flour_kg = (base_flour_g * scale_factor) / 1000.0
    scaled_butter_g = base_butter_g * scale_factor
    scaled_sugar_kg = (base_sugar_g * scale_factor) / 1000.0

    correct_ans = f"Scale factor = {_fmt(scale_factor, 1)}; Flour = {_fmt(scaled_flour_kg, 2)} kg; Butter = {_fmt(scaled_butter_g, 0)} g; Sugar = {_fmt(scaled_sugar_kg, 2)} kg"

    custom_options = [
        correct_ans,
        f"Scale factor = {_fmt(scale_factor, 1)}; Flour = {_fmt(base_flour_g * scale_factor, 0)} kg; Butter = {_fmt(scaled_butter_g, 0)} g",
        f"Scale factor = {_fmt(scale_factor / 2, 1)}; Flour = {_fmt(scaled_flour_kg / 2, 2)} kg; Butter = {_fmt(scaled_butter_g / 2, 0)} g",
        f"Scale factor = {_fmt(scale_factor * 2, 1)}; Flour = {_fmt(scaled_flour_kg * 2, 2)} kg; Butter = {_fmt(scaled_butter_g * 2, 0)} g",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} is catering for a school valedictory tea for {target_servings} guests.\n"
        f"The standard scone recipe makes enough for {base_servings} servings and requires:\n"
        f"• 500 g flour\n"
        f"• 125 g butter\n"
        f"• 200 g sugar\n\n"
        f"Calculate the scaling factor and the required quantities of flour (in kg), butter (in g), "
        f"and sugar (in kg) to feed all {target_servings} guests."
    )
    explanation = (
        f"Step 1: Scaling factor = {target_servings} ÷ {base_servings} = {_fmt(scale_factor, 1)} [M].\n"
        f"Step 2: Flour: 500 g × {_fmt(scale_factor, 1)} = {_fmt(base_flour_g * scale_factor, 0)} g = {_fmt(scaled_flour_kg, 2)} kg [M].\n"
        f"Step 3: Butter: 125 g × {_fmt(scale_factor, 1)} = {_fmt(scaled_butter_g, 0)} g; Sugar: 200 g × {_fmt(scale_factor, 1)} = {_fmt(base_sugar_g * scale_factor, 0)} g = {_fmt(scaled_sugar_kg, 2)} kg [A]."
    )
    return _build_question_payload(
        subskill_id="26_scaling_recipe_yield_quantities",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide target servings by base servings to find the scale factor, then multiply each ingredient.",
        tier_2=f"Scale factor = {target_servings} ÷ {base_servings} = {scale_factor}. Multiply each quantity by {scale_factor}.",
        tier_3=f"Flour = {_fmt(scaled_flour_kg, 2)} kg; Butter = {_fmt(scaled_butter_g, 0)} g; Sugar = {_fmt(scaled_sugar_kg, 2)} kg.",
        r=r,
    )


def generate_27_dry_ingredient_cup_to_grams(r: random.Random) -> Dict[str, Any]:
    """Convert volume in cups to mass in grams using ingredient density conversion factors."""
    flour_cups = r.choice([2.5, 3.0, 3.5, 4.0])
    sugar_cups = r.choice([1.5, 2.0, 2.5])

    # 1 cup cake flour = 125 g
    # 1 cup white granulated sugar = 200 g
    flour_g = flour_cups * 125.0
    sugar_g = sugar_cups * 200.0
    total_g = flour_g + sugar_g
    total_kg = total_g / 1000.0

    correct_ans = f"Flour = {_fmt(flour_g, 0)} g; Sugar = {_fmt(sugar_g, 0)} g; Total Mass = {_fmt(total_g, 0)} g ({_fmt(total_kg, 2)} kg)"

    custom_options = [
        correct_ans,
        f"Flour = {_fmt(flour_cups * 250, 0)} g; Sugar = {_fmt(sugar_cups * 250, 0)} g; Total Mass = {_fmt((flour_cups + sugar_cups) * 250, 0)} g",
        f"Flour = {_fmt(flour_g, 0)} g; Sugar = {_fmt(sugar_g, 0)} g; Total Mass = {_fmt(total_kg * 10, 2)} kg",
        f"Flour = {_fmt(flour_g / 2, 0)} g; Sugar = {_fmt(sugar_g / 2, 0)} g; Total Mass = {_fmt(total_g / 2, 0)} g",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A baking recipe lists ingredients by cup volume:\n"
        f"• {_fmt(flour_cups, 1)} cups of cake flour\n"
        f"• {_fmt(sugar_cups, 1)} cups of granulated white sugar\n\n"
        f"Conversion reference:\n"
        f"• 1 cup of cake flour = 125 g\n"
        f"• 1 cup of white sugar = 200 g\n\n"
        f"Calculate the mass of flour, the mass of sugar, and the combined dry mass in grams (g) and kilograms (kg)."
    )
    explanation = (
        f"Step 1: Flour mass = {_fmt(flour_cups, 1)} cups × 125 g/cup = {_fmt(flour_g, 0)} g [M].\n"
        f"Step 2: Sugar mass = {_fmt(sugar_cups, 1)} cups × 200 g/cup = {_fmt(sugar_g, 0)} g [M].\n"
        f"Step 3: Total = {_fmt(flour_g, 0)} + {_fmt(sugar_g, 0)} = {_fmt(total_g, 0)} g = {_fmt(total_kg, 2)} kg [A]."
    )
    return _build_question_payload(
        subskill_id="27_dry_ingredient_cup_to_grams",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Different ingredients have different densities: flour is 125 g/cup, sugar is 200 g/cup.",
        tier_2=f"Flour: {flour_cups} × 125 = {_fmt(flour_g, 0)} g. Sugar: {sugar_cups} × 200 = {_fmt(sugar_g, 0)} g.",
        tier_3=f"Total = {_fmt(total_g, 0)} g ({_fmt(total_kg, 2)} kg).",
        r=r,
    )


def generate_28_oven_temperature_celsius_to_fahrenheit(r: random.Random) -> Dict[str, Any]:
    """Convert oven temperature from degrees Celsius (°C) to degrees Fahrenheit (°F)."""
    c_temp = r.choice([160, 180, 200, 220])
    # F = (C * 1.8) + 32
    f_temp = int((c_temp * 1.8) + 32)

    correct_ans = f"{c_temp} °C = {f_temp} °F"

    custom_options = [
        correct_ans,
        f"{c_temp} °C = {c_temp + 32} °F",
        f"{c_temp} °C = {int(c_temp * 1.8)} °F",
        f"{c_temp} °C = {f_temp + 30} °F",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A South African recipe specifies pre-heating the oven to {c_temp} °C.\n"
        f"An imported American convection oven only displays temperature settings in degrees Fahrenheit (°F).\n\n"
        f"Formula: °F = (°C × 1,8) + 32\n\n"
        f"Convert {c_temp} °C to degrees Fahrenheit (°F)."
    )
    explanation = (
        f"Step 1: Multiply Celsius temperature by 1,8: {c_temp} × 1,8 = {int(c_temp * 1.8)} [M].\n"
        f"Step 2: Add 32: {int(c_temp * 1.8)} + 32 = {f_temp} [M].\n"
        f"Step 3: {c_temp} °C = {f_temp} °F [A]."
    )
    return _build_question_payload(
        subskill_id="28_oven_temperature_celsius_to_fahrenheit",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply Celsius temperature by 1,8, then add 32.",
        tier_2=f"({c_temp} × 1,8) + 32 = {f_temp}.",
        tier_3=f"{c_temp} °C = {f_temp} °F.",
        r=r,
    )


def generate_29_oven_temperature_fahrenheit_to_celsius(r: random.Random) -> Dict[str, Any]:
    """Convert oven temperature from degrees Fahrenheit (°F) to degrees Celsius (°C)."""
    f_temp = r.choice([350, 375, 400, 425])
    # C = (F - 32) / 1.8
    c_temp = round((f_temp - 32) / 1.8, 1)
    c_rounded = round(c_temp)

    correct_ans = f"{f_temp} °F = {_fmt(c_temp, 1)} °C ≈ {c_rounded} °C"

    custom_options = [
        correct_ans,
        f"{f_temp} °F = {_fmt((f_temp - 32) * 1.8, 1)} °C",
        f"{f_temp} °F = {_fmt(f_temp / 1.8, 1)} °C",
        f"{f_temp} °F = {f_temp - 32} °C",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An American cooking website gives the roasting temperature for a whole chicken as {f_temp} °F.\n\n"
        f"Formula: °C = (°F - 32) ÷ 1,8\n\n"
        f"Convert {f_temp} °F to degrees Celsius (°C), rounded to the nearest whole degree."
    )
    explanation = (
        f"Step 1: Subtract 32 from Fahrenheit: {f_temp} - 32 = {f_temp - 32} [M].\n"
        f"Step 2: Divide by 1,8: {f_temp - 32} ÷ 1,8 = {_fmt(c_temp, 1)} °C [M].\n"
        f"Step 3: Round to the nearest whole degree: {c_rounded} °C [A]."
    )
    return _build_question_payload(
        subskill_id="29_oven_temperature_fahrenheit_to_celsius",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract 32 first, then divide by 1,8.",
        tier_2=f"({f_temp} - 32) ÷ 1,8 = {_fmt(c_temp, 1)} °C.",
        tier_3=f"Approximately {c_rounded} °C.",
        r=r,
    )


def generate_30_mass_pounds_ounces_to_kg(r: random.Random) -> Dict[str, Any]:
    """Convert mass from imperial pounds (lb) and ounces (oz) to kilograms."""
    lbs = r.choice([4, 5, 6, 8, 10])
    oz = r.choice([4, 8, 12])
    # 1 lb = 0.4536 kg, 1 oz = 28.35 g = 0.02835 kg
    total_kg = round((lbs * 0.4536) + (oz * 0.02835), 2)

    correct_ans = f"{lbs} lb {oz} oz = {_fmt(total_kg, 2)} kg"

    custom_options = [
        correct_ans,
        f"{lbs} lb {oz} oz = {_fmt(total_kg * 2.2046, 2)} kg",
        f"{lbs} lb {oz} oz = {_fmt((lbs + oz) * 0.4536, 2)} kg",
        f"{lbs} lb {oz} oz = {_fmt(total_kg / 10, 3)} kg",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An imported baby stroller package states a gross shipping weight of {lbs} pounds and {oz} ounces ({lbs} lb {oz} oz).\n\n"
        f"Conversion factors:\n"
        f"• 1 pound (lb) = 0,4536 kg\n"
        f"• 1 ounce (oz) = 28,35 g = 0,02835 kg\n\n"
        f"Convert this shipping weight into kilograms (kg), rounded to 2 decimal places."
    )
    explanation = (
        f"Step 1: Convert pounds to kg: {lbs} × 0,4536 kg = {_fmt(lbs * 0.4536, 3)} kg [M].\n"
        f"Step 2: Convert ounces to kg: {oz} × 0,02835 kg = {_fmt(oz * 0.02835, 3)} kg [M].\n"
        f"Step 3: Sum and round: {_fmt(lbs * 0.4536, 3)} + {_fmt(oz * 0.02835, 3)} = {_fmt(total_kg, 2)} kg [A]."
    )
    return _build_question_payload(
        subskill_id="30_mass_pounds_ounces_to_kg",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply pounds by 0,4536 and ounces by 0,02835, then add together.",
        tier_2=f"({lbs} × 0,4536) + ({oz} × 0,02835) = {_fmt(total_kg, 2)} kg.",
        tier_3=f"{_fmt(total_kg, 2)} kg.",
        r=r,
    )


def generate_31_liquid_fluid_ounces_pints_to_litres(r: random.Random) -> Dict[str, Any]:
    """Convert liquid volume from US fluid ounces (fl oz) to millilitres and litres."""
    fl_oz = r.choice([16, 24, 32, 40, 64])
    # 1 US fl oz = 29.57 ml
    total_ml = round(fl_oz * 29.57, 1)
    total_litres = round(total_ml / 1000.0, 2)

    correct_ans = f"{fl_oz} fl oz = {_fmt(total_ml, 1)} ml = {_fmt(total_litres, 2)} ℓ"

    custom_options = [
        correct_ans,
        f"{fl_oz} fl oz = {_fmt(fl_oz * 250, 0)} ml = {_fmt(fl_oz * 0.25, 2)} ℓ",
        f"{fl_oz} fl oz = {_fmt(total_ml * 10, 0)} ml = {_fmt(total_litres * 10, 1)} ℓ",
        f"{fl_oz} fl oz = {_fmt(total_litres, 2)} ml",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A bottle of imported maple syrup is labeled as containing {fl_oz} US fluid ounces ({fl_oz} fl oz).\n\n"
        f"Given that 1 US fluid ounce (fl oz) = 29,57 ml:\n\n"
        f"Calculate the volume of the syrup in millilitres (ml) and in litres (ℓ), rounded to 2 decimal places."
    )
    explanation = (
        f"Step 1: Multiply fluid ounces by 29,57 ml: {fl_oz} × 29,57 ml = {_fmt(total_ml, 1)} ml [M].\n"
        f"Step 2: Convert to litres: {_fmt(total_ml, 1)} ÷ 1 000 = {_fmt(total_litres, 2)} ℓ [M].\n"
        f"Step 3: {fl_oz} fl oz = {_fmt(total_litres, 2)} ℓ [A]."
    )
    return _build_question_payload(
        subskill_id="31_liquid_fluid_ounces_pints_to_litres",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply fluid ounces by 29,57 ml to get ml, then divide by 1 000 for litres.",
        tier_2=f"{fl_oz} × 29,57 = {_fmt(total_ml, 1)} ml. Divide by 1 000 = {_fmt(total_litres, 2)} ℓ.",
        tier_3=f"{_fmt(total_litres, 2)} ℓ.",
        r=r,
    )


def generate_32_cost_per_unit_volume_comparison(r: random.Random) -> Dict[str, Any]:
    """Compare unit prices (per 100 ml) between two different package volumes to determine best value."""
    price_small = 38.99   # 750 ml bottle
    vol_small = 750
    price_large = 89.99   # 2 000 ml bottle
    vol_large = 2000

    unit_small = (price_small / vol_small) * 100.0  # R 5.20 per 100 ml
    unit_large = (price_large / vol_large) * 100.0  # R 4.50 per 100 ml

    diff_per_100ml = unit_small - unit_large
    cheaper = "2 ℓ bottle"

    correct_ans = f"750 ml: {_fmt_curr(unit_small)}/100 ml; 2 ℓ: {_fmt_curr(unit_large)}/100 ml; {cheaper} is cheaper by {_fmt_curr(diff_per_100ml)}/100 ml"

    custom_options = [
        correct_ans,
        f"750 ml: {_fmt_curr(price_small / 7.5)}/100 ml; 2 ℓ: {_fmt_curr(price_large / 20)}/100 ml; 750 ml bottle is cheaper",
        f"Both bottles have identical unit costs of R 4,85/100 ml",
        f"750 ml: R 38,99/100 ml; 2 ℓ: R 89,99/100 ml; 750 ml is cheaper",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A shopper compares two different sizes of tomato sauce at a supermarket:\n"
        f"• Brand A: 750 ml glass bottle selling for {_fmt_curr(price_small)}\n"
        f"• Brand B: 2 ℓ (2 000 ml) plastic bottle selling for {_fmt_curr(price_large)}\n\n"
        f"1. Calculate the unit price per 100 ml for each bottle.\n"
        f"2. Determine which bottle offers the better value for money and by how much per 100 ml."
    )
    explanation = (
        f"Step 1: Brand A unit cost = ({_fmt_curr(price_small)} ÷ 750) × 100 = {_fmt_curr(unit_small)} per 100 ml [M].\n"
        f"Step 2: Brand B unit cost = ({_fmt_curr(price_large)} ÷ 2 000) × 100 = {_fmt_curr(unit_large)} per 100 ml [M].\n"
        f"Step 3: Difference = {_fmt_curr(unit_small)} - {_fmt_curr(unit_large)} = {_fmt_curr(diff_per_100ml)} per 100 ml, so the 2 ℓ bottle is better value [A]."
    )
    return _build_question_payload(
        subskill_id="32_cost_per_unit_volume_comparison",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Convert both volumes to ml, then calculate price ÷ volume × 100 for each option.",
        tier_2=f"750 ml: ({price_small} ÷ 750) × 100 = {_fmt_curr(unit_small)}. 2 ℓ: ({price_large} ÷ 2 000) × 100 = {_fmt_curr(unit_large)}.",
        tier_3=f"2 ℓ bottle is cheaper by {_fmt_curr(diff_per_100ml)} per 100 ml.",
        r=r,
    )
