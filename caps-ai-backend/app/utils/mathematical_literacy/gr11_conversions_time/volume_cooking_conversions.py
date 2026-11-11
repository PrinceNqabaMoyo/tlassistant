"""Volume and domestic cooking conversions (Subskills 19-27) for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def generate_subskill_19(r: random.Random) -> Dict[str, Any]:
    """UK gallons to litres (1 UK gallon ≈ 4,546 litres)."""
    name = r.choice(SA_NAMES)
    gallons = r.randint(3, 25)
    litres = round(gallons * 4.546, 2)
    ans_str = f"{_fmt(litres)} L"

    prompt = (
        f"{name} is restoring an imported vintage British car with a fuel tank capacity of "
        f"{gallons} UK gallons. Convert this capacity to litres.\n"
        f"*(Given: 1 UK gallon ≈ 4,546 litres. Round your answer to 2 decimal places if necessary.)*"
    )
    explanation = (
        f"Step 1: Identify the conversion factor:\n"
        f"1 UK gallon ≈ 4,546 L. [1 mark]\n"
        f"Step 2: Multiply the number of UK gallons by 4,546:\n"
        f"\\text{{Volume in litres}} = {gallons} \\times 4,546 = {litres:.3f} \\text{{ L}} [1 mark]\n"
        f"Step 3: State final value rounded to 2 decimal places:\n"
        f"\\text{{Capacity}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(gallons * 3.785, 2))} L",
        f"{_fmt(round(gallons / 4.546, 2))} L",
        f"{_fmt(round(gallons * 4.5, 2))} L",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_19",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply the number of UK gallons by 4,546 to find the volume in litres.",
        f"Calculate {gallons} × 4,546.",
        f"{gallons} × 4,546 = {ans_str}.",
        r,
    )


def generate_subskill_20(r: random.Random) -> Dict[str, Any]:
    """US liquid gallons to litres (1 US gallon ≈ 3,785 litres)."""
    name = r.choice(SA_NAMES)
    us_gal = r.randint(4, 30)
    litres = round(us_gal * 3.785, 2)
    ans_str = f"{_fmt(litres)} L"

    prompt = (
        f"{name} purchased an American industrial pressure washer with a detergent reservoir of "
        f"{us_gal} US liquid gallons. Calculate the capacity of this reservoir in litres.\n"
        f"*(Given: 1 US liquid gallon ≈ 3,785 litres. Round to 2 decimal places if necessary.)*"
    )
    explanation = (
        f"Step 1: Note the US gallon conversion factor:\n"
        f"1 US gallon ≈ 3,785 L. [1 mark]\n"
        f"Step 2: Multiply the given US gallons by 3,785:\n"
        f"\\text{{Volume}} = {us_gal} \\times 3,785 = {litres:.3f} \\text{{ L}} [1 mark]\n"
        f"Step 3: Round to 2 decimal places:\n"
        f"\\text{{Capacity}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(us_gal * 4.546, 2))} L",
        f"{_fmt(round(us_gal / 3.785, 2))} L",
        f"{_fmt(round(us_gal * 3.8, 2))} L",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_20",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply the number of US gallons by 3,785.",
        f"Calculate {us_gal} × 3,785.",
        f"{us_gal} × 3,785 = {ans_str}.",
        r,
    )


def generate_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Litres to UK gallons (1 UK gallon ≈ 4,546 litres)."""
    name = r.choice(SA_NAMES)
    litres = r.randint(25, 120)
    uk_gal = round(litres / 4.546, 2)
    ans_str = f"{_fmt(uk_gal)} UK gal"

    prompt = (
        f"A dairy container holds {_fmt(litres)} litres of milk. {name} needs to record this volume "
        f"in UK gallons for an export catalogue.\n"
        f"Convert {_fmt(litres)} litres to UK gallons.\n"
        f"*(Given: 1 UK gallon ≈ 4,546 litres. Round to 2 decimal places.)*"
    )
    explanation = (
        f"Step 1: Identify that converting from litres to gallons requires division:\n"
        f"\\text{{Gallons}} = \\text{{Litres}} \\div 4,546. [1 mark]\n"
        f"Step 2: Perform the division:\n"
        f"{litres} \\div 4,546 = {litres / 4.546:.4f} \\text{{ UK gal}} [1 mark]\n"
        f"Step 3: Round off to 2 decimal places:\n"
        f"\\text{{Volume}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(litres / 3.785, 2))} UK gal",
        f"{_fmt(round(litres * 4.546, 2))} UK gal",
        f"{_fmt(round(litres / 4.5, 2))} UK gal",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_21",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide the number of litres by 4,546.",
        f"Calculate {litres} ÷ 4,546.",
        f"{litres} ÷ 4,546 = {ans_str}.",
        r,
    )


def generate_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Fluid ounces (fl oz) to millilitres (1 fl oz ≈ 29,57 mL)."""
    name = r.choice(SA_NAMES)
    floz = r.randint(4, 24)
    ml = round(floz * 29.57, 1)
    ans_str = f"{_fmt(ml)} mL"

    prompt = (
        f"{name} bought a bottle of imported perfume/cologne labelled {floz} fluid ounces (fl oz). "
        f"Convert this volume to millilitres (mL).\n"
        f"*(Given: 1 fluid ounce (fl oz) ≈ 29,57 mL. Round to 1 decimal place.)*"
    )
    explanation = (
        f"Step 1: Identify the conversion factor:\n"
        f"1 \\text{{ fl oz}} \\approx 29,57 \\text{{ mL}}. [1 mark]\n"
        f"Step 2: Multiply the fluid ounces by 29,57:\n"
        f"{floz} \\times 29,57 = {floz * 29.57:.2f} \\text{{ mL}} [1 mark]\n"
        f"Step 3: Round off to 1 decimal place:\n"
        f"\\text{{Volume}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(round(floz * 28.35, 1))} mL",
        f"{_fmt(round(floz / 29.57, 1))} mL",
        f"{_fmt(round(floz * 30.0, 1))} mL",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_22",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply the number of fluid ounces by 29,57.",
        f"Calculate {floz} × 29,57.",
        f"{floz} × 29,57 = {ans_str}.",
        r,
    )


def generate_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Domestic baking measures (cups, tbsp, tsp) to millilitres."""
    name = r.choice(SA_NAMES)
    cups = r.choice([1, 2, 3, 4])
    tbsp = r.choice([1, 2, 3])
    tsp = r.choice([1, 2])
    total_ml = (cups * 250) + (tbsp * 15) + (tsp * 5)
    ans_str = f"{_fmt(total_ml)} mL"

    prompt = (
        f"{name} is preparing a traditional South African malva pudding. The recipe calls for:\n"
        f"- {cups} metric cups of milk\n"
        f"- {tbsp} tablespoons of apricot jam\n"
        f"- {tsp} teaspoons of bicarbonate of soda\n"
        f"Calculate the total combined volume of these ingredients in millilitres (mL).\n"
        f"*(Given: 1 metric cup = 250 mL; 1 tablespoon (tbsp) = 15 mL; 1 teaspoon (tsp) = 5 mL.)*"
    )
    explanation = (
        f"Step 1: Convert each domestic measure to millilitres using standard SA kitchen units:\n"
        f"- Milk: {cups} \\times 250\\text{{ mL}} = {cups * 250}\\text{{ mL}}\n"
        f"- Jam: {tbsp} \\times 15\\text{{ mL}} = {tbsp * 15}\\text{{ mL}}\n"
        f"- Bicarbonate of soda: {tsp} \\times 5\\text{{ mL}} = {tsp * 5}\\text{{ mL}} [1 mark]\n"
        f"Step 2: Add all the volumes together:\n"
        f"\\text{{Total}} = {cups * 250} + {tbsp * 15} + {tsp * 5} [1 mark]\n"
        f"Step 3: State the final total volume:\n"
        f"\\text{{Total volume}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(total_ml - 20)} mL",
        f"{_fmt(total_ml + 50)} mL",
        f"{_fmt((cups * 200) + (tbsp * 15) + (tsp * 5))} mL",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_23",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply cups by 250, tbsp by 15, and tsp by 5, then sum them up.",
        f"Sum: ({cups} × 250) + ({tbsp} × 15) + ({tsp} × 5).",
        f"Total volume = {ans_str}.",
        r,
    )


def generate_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Millilitres to domestic cooking measures (cups, tablespoons)."""
    name = r.choice(SA_NAMES)
    cups_count = r.choice([1.5, 2.5, 3.0, 3.5, 4.0])
    ml = int(cups_count * 250)
    ans_str = f"{_fmt(cups_count)} cups"

    prompt = (
        f"{name}'s measuring jug only has millilitre (mL) markings. A recipe requires {_fmt(ml)} mL of chicken stock.\n"
        f"How many metric cups of chicken stock is this?\n"
        f"*(Given: 1 metric cup = 250 mL.)*"
    )
    explanation = (
        f"Step 1: State the conversion factor:\n"
        f"1 \\text{{ metric cup}} = 250\\text{{ mL}}. [1 mark]\n"
        f"Step 2: Divide the volume in millilitres by 250:\n"
        f"\\text{{Number of cups}} = {ml} \\div 250 [1 mark]\n"
        f"Step 3: State the final answer:\n"
        f"\\text{{Cups}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(cups_count - 0.5)} cups",
        f"{_fmt(cups_count + 1.0)} cups",
        f"{_fmt(ml / 200)} cups",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_24",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide the millilitres by 250.",
        f"Calculate {ml} ÷ 250.",
        f"{ml} ÷ 250 = {ans_str}.",
        r,
    )


def generate_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Multi-unit recipe scaling with volumetric adjustments."""
    name = r.choice(SA_NAMES)
    base_servings = 4
    target_servings = r.choice([8, 12, 16, 20])
    scale_factor = target_servings // base_servings
    base_oil_tbsp = r.choice([2, 3, 4])
    base_milk_cups = r.choice([1, 2])

    target_oil_tbsp = base_oil_tbsp * scale_factor
    target_oil_ml = target_oil_tbsp * 15
    target_milk_cups = base_milk_cups * scale_factor
    target_milk_ml = target_milk_cups * 250
    total_liquid_ml = target_oil_ml + target_milk_ml
    ans_str = f"{_fmt(total_liquid_ml)} mL"

    prompt = (
        f"{name} is catering for a school function and needs to scale up a muffin recipe from {base_servings} "
        f"servings to {target_servings} servings.\n"
        f"The original recipe for {base_servings} servings requires:\n"
        f"- {base_milk_cups} cup(s) of milk\n"
        f"- {base_oil_tbsp} tablespoons of cooking oil\n"
        f"Calculate the total combined volume (in millilitres) of milk and oil needed for {target_servings} servings.\n"
        f"*(Given: 1 cup = 250 mL; 1 tbsp = 15 mL.)*"
    )
    explanation = (
        f"Step 1: Calculate the scaling factor:\n"
        f"\\text{{Scale factor}} = {target_servings} \\div {base_servings} = {scale_factor}. [1 mark]\n"
        f"Step 2: Scale both ingredients and convert to mL:\n"
        f"- Milk: {base_milk_cups} \\times {scale_factor} = {target_milk_cups}\\text{{ cups}} = "
        f"{target_milk_cups} \\times 250 = {target_milk_ml}\\text{{ mL}}\n"
        f"- Oil: {base_oil_tbsp} \\times {scale_factor} = {target_oil_tbsp}\\text{{ tbsp}} = "
        f"{target_oil_tbsp} \\times 15 = {target_oil_ml}\\text{{ mL}} [1 mark]\n"
        f"Step 3: Add to find total volume:\n"
        f"\\text{{Total}} = {target_milk_ml} + {target_oil_ml} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(total_liquid_ml - 150)} mL",
        f"{_fmt(total_liquid_ml + 250)} mL",
        f"{_fmt((base_milk_cups * 250 + base_oil_tbsp * 15) * (scale_factor - 1))} mL",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_25",
        prompt,
        ans_str,
        options,
        explanation,
        "Find the scale factor, multiply the ingredients by it, convert to mL and sum.",
        f"Scale factor = {scale_factor}. Milk = {target_milk_ml} mL, Oil = {target_oil_ml} mL.",
        f"Total volume = {ans_str}.",
        r,
    )


def generate_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Cubic metres (m³) to litres (1 m³ = 1 000 L)."""
    name = r.choice(SA_NAMES)
    m3 = r.choice([2.5, 4.0, 7.5, 12.0, 18.5, 25.0, 45.0])
    litres = int(m3 * 1000)
    ans_str = f"{_fmt(litres)} L"

    prompt = (
        f"{name}'s family installed a municipal rainwater harvesting tank with a capacity of "
        f"{_fmt(m3)} cubic metres (m³).\n"
        f"Convert this capacity to litres (L).\n"
        f"*(Given: 1 m³ = 1 000 litres.)*"
    )
    explanation = (
        f"Step 1: State the conversion factor between cubic metres and litres:\n"
        f"1\\text{{ m}}^3 = 1\\,000\\text{{ L}}. [1 mark]\n"
        f"Step 2: Multiply the volume in m³ by 1 000:\n"
        f"\\text{{Volume in litres}} = {_fmt(m3)} \\times 1\\,000 [1 mark]\n"
        f"Step 3: Write down the final answer:\n"
        f"\\text{{Capacity}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(int(m3 * 100))} L",
        f"{_fmt(int(m3 * 10000))} L",
        f"{_fmt(round(m3 / 1000, 4))} L",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_26",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply the number of cubic metres by 1 000.",
        f"Calculate {_fmt(m3)} × 1 000.",
        f"{_fmt(m3)} × 1 000 = {ans_str}.",
        r,
    )


def generate_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Litres to cubic metres (m³)."""
    name = r.choice(SA_NAMES)
    litres = r.choice([3500, 7800, 15000, 24500, 48000, 65000])
    m3 = round(litres / 1000, 2)
    ans_str = f"{_fmt(m3)} m³"

    prompt = (
        f"A municipal water bill indicates that {name}'s household consumed {_fmt(litres)} litres "
        f"of water during November.\n"
        f"Convert this consumption to cubic metres (m³).\n"
        f"*(Given: 1 m³ = 1 000 litres.)*"
    )
    explanation = (
        f"Step 1: Note that converting litres to cubic metres requires division by 1 000:\n"
        f"\\text{{Volume in m}}^3 = \\text{{Volume in litres}} \\div 1\\,000. [1 mark]\n"
        f"Step 2: Divide {_fmt(litres)} by 1 000:\n"
        f"{_fmt(litres)} \\div 1\\,000 = {m3} [1 mark]\n"
        f"Step 3: State the final answer with units:\n"
        f"\\text{{Consumption}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(m3 * 10)} m³",
        f"{_fmt(round(m3 / 10, 3))} m³",
        f"{_fmt(litres * 1000)} m³",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_27",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide the number of litres by 1 000.",
        f"Calculate {_fmt(litres)} ÷ 1 000.",
        f"{_fmt(litres)} ÷ 1 000 = {ans_str}.",
        r,
    )
