"""Cluster 1: Metric to Imperial Mass & Weight Conversions (Subskills 1 to 9)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def _gen_kg_to_pounds_with_factor(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_kg_to_pounds_with_factor"
    name = r.choice(SA_NAMES)
    kg_val = r.choice([55, 62, 68, 74, 82, 90, 95])
    factor = 2.20462  # 1 kg ≈ 2.205 lb
    pounds = round(kg_val * 2.205, 1)
    correct_ans = f"{_fmt(pounds)} lb"

    prompt = (
        f"{name} weighs a parcel at a South African post office and finds its mass is **{kg_val} kg**.\n"
        f"An international courier document requires the weight to be declared in **pounds (lb)**.\n\n"
        f"**Given conversion factor**: $1\\text{{ kg}} \\approx 2,205\\text{{ lb}}$\n\n"
        f"Convert {kg_val} kg to pounds, rounded to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To convert from kilograms to pounds using a direct rate factor, multiply the mass in kilograms by 2,205: "
        f"$$\\text{{Mass in lb}} = \\text{{Mass in kg}} \\times 2,205$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Mass}} = {kg_val} \\times 2,205 = {_fmt(kg_val * 2.205, 3)}\\text{{ lb}}$$ "
        f"✓ [1 Mark: Method – multiplying kilograms by 2,205 conversion factor]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Mass}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate rounded decimal with unit]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the kilograms by 2,205.",
        tier_2=f"{kg_val} × 2,205 = {_fmt(kg_val * 2.205, 2)} lb.",
        tier_3=f"Mass = {correct_ans}.",
        r=r,
    )


def _gen_pounds_to_kg_with_factor(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_pounds_to_kg_with_factor"
    name = r.choice(SA_NAMES)
    pounds = r.choice([130, 150, 165, 180, 200, 220])
    kg_val = round(pounds / 2.205, 1)
    correct_ans = f"{_fmt(kg_val)} kg"

    prompt = (
        f"{name} imports gym weights from the United States with a stamped mass of **{pounds} lb**.\n\n"
        f"**Given conversion factor**: $1\\text{{ kg}} \\approx 2,205\\text{{ lb}}$\n\n"
        f"Convert {pounds} lb into **kilograms (kg)**, rounded to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To convert from pounds back to kilograms, divide the number of pounds by the conversion factor 2,205: "
        f"$$\\text{{Mass in kg}} = \\frac{{\\text{{Mass in lb}}}}{{2,205}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Mass}} = \\frac{{{pounds}}}{{2,205}} = {_fmt(pounds / 2.205, 3)}\\text{{ kg}}$$ "
        f"✓ [1 Mark: Method – dividing pounds by 2,205]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Mass}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate kilograms rounded to 1 decimal]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the pounds by 2,205.",
        tier_2=f"{pounds} ÷ 2,205 = {_fmt(kg_val)} kg.",
        tier_3=f"Mass = {correct_ans}.",
        r=r,
    )


def _gen_body_weight_stones_and_pounds_to_kg(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_body_weight_stones_and_pounds_to_kg"
    name = r.choice(SA_NAMES)
    stones = r.randint(10, 15)
    pounds = r.randint(2, 12)
    total_pounds = (stones * 14) + pounds
    kg_val = round(total_pounds / 2.205, 1)
    correct_ans = f"{_fmt(kg_val)} kg"

    prompt = (
        f"A medical record imported from the United Kingdom lists {name}'s body weight as **{stones} stones and {pounds} lb**.\n\n"
        f"**Given conversion factors**:\n"
        f"  • $1\\text{{ stone}} = 14\\text{{ lb}}$\n"
        f"  • $1\\text{{ kg}} \\approx 2,205\\text{{ lb}}$\n\n"
        f"Calculate {name}'s weight in **kilograms (kg)**, rounded off to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First convert stones into pounds: $\\text{{Stones in lb}} = {stones} \\times 14 = {stones * 14}\\text{{ lb}}$.\n"
        f"Add the extra pounds: $\\text{{Total lb}} = {stones * 14} + {pounds} = {total_pounds}\\text{{ lb}}$.\n"
        f"Finally, divide total pounds by 2,205 to convert to kilograms.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total Pounds}} = ({stones} \\times 14) + {pounds} = {total_pounds}\\text{{ lb}}$$\n"
        f"$$\\text{{Kilograms}} = \\frac{{{total_pounds}}}{{2,205}} = {_fmt(total_pounds / 2.205, 3)}\\text{{ kg}}$$ "
        f"✓ [1 Mark: Method – converting stones to pounds and dividing by 2,205]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Weight}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate kilograms]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Convert stones to pounds: ({stones} × 14) + {pounds}. Then divide by 2,205.",
        tier_2=f"Total lb = {total_pounds}. {total_pounds} ÷ 2,205 = {correct_ans}.",
        tier_3=f"Weight = {correct_ans}.",
        r=r,
    )


def _gen_ounces_to_grams_cooking(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_ounces_to_grams_cooking"
    name = r.choice(SA_NAMES)
    ounces = r.choice([4, 6, 8, 12, 16])
    factor = 28.35  # 1 oz ≈ 28.35 g
    grams = round(ounces * factor, 1)
    correct_ans = f"{_fmt(grams)} g"

    prompt = (
        f"{name} is following an imported British recipe that calls for **{ounces} ounces (oz)** of butter.\n\n"
        f"**Given conversion factor**: $1\\text{{ ounce (oz)}} \\approx 28,35\\text{{ g}}$\n\n"
        f"Calculate the mass of butter required in **grams (g)**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Multiply the number of ounces by 28,35 to convert to grams: "
        f"$$\\text{{Mass in grams}} = \\text{{Mass in oz}} \\times 28,35$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Mass}} = {ounces} \\times 28,35$$ "
        f"✓ [1 Mark: Method – multiplying ounces by 28,35 g/oz]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Mass}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate grams]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply ounces by 28,35.",
        tier_2=f"{ounces} × 28,35 = {correct_ans}.",
        tier_3=f"Grams = {correct_ans}.",
        r=r,
    )


def _gen_grams_to_ounces_baking(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_grams_to_ounces_baking"
    name = r.choice(SA_NAMES)
    grams = r.choice([250, 300, 450, 500])
    ounces = round(grams / 28.35, 1)
    correct_ans = f"{_fmt(ounces)} oz"

    prompt = (
        f"{name} bakes a cake using **{grams} g** of flour.\n\n"
        f"**Given conversion factor**: $1\\text{{ ounce (oz)}} \\approx 28,35\\text{{ g}}$\n\n"
        f"Convert {grams} g to **ounces (oz)**, rounded to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To convert grams to ounces, divide grams by 28,35: "
        f"$$\\text{{Ounces}} = \\frac{{\\text{{Grams}}}}{{28,35}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Ounces}} = \\frac{{{grams}}}{{28,35}} = {_fmt(grams / 28.35, 3)}\\text{{ oz}}$$ "
        f"✓ [1 Mark: Method – dividing grams by 28,35]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Mass}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate rounded ounces]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide grams by 28,35.",
        tier_2=f"{grams} ÷ 28,35 = {_fmt(ounces)} oz.",
        tier_3=f"Ounces = {correct_ans}.",
        r=r,
    )


def _gen_metric_tonnes_to_imperial_tons(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_metric_tonnes_to_imperial_tons"
    tonnes = r.choice([15, 24, 30, 45, 60])
    # 1 metric tonne = 1 000 kg ≈ 0.9842 imperial long tons (or 1.1023 US short tons)
    # CAPS textbook standard uses: 1 metric tonne ≈ 0,9842 imperial tons
    factor = 0.9842
    imp_tons = round(tonnes * factor, 2)
    correct_ans = f"{_fmt(imp_tons)} imperial tons"

    prompt = (
        f"A shipping cargo container holds **{tonnes} metric tonnes (t)** of export fruit.\n\n"
        f"**Given conversion factor**: $1\\text{{ metric tonne}} \\approx 0,9842\\text{{ imperial tons}}$\n\n"
        f"Convert {tonnes} metric tonnes into **imperial tons**, rounded to 2 decimal places."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Multiply metric tonnes by 0,9842 to obtain imperial tons: "
        f"$$\\text{{Imperial Tons}} = \\text{{Metric Tonnes}} \\times 0,9842$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Imperial Tons}} = {tonnes} \\times 0,9842 = {_fmt(tonnes * factor, 4)}$$ "
        f"✓ [1 Mark: Method – multiplying metric tonnes by 0,9842]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Mass}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate conversion rounded to 2 decimals]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the metric tonnes by 0,9842.",
        tier_2=f"{tonnes} × 0,9842 = {correct_ans}.",
        tier_3=f"Imperial tons = {correct_ans}.",
        r=r,
    )


def _gen_airline_baggage_weight_limit_pounds_to_kg(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_airline_baggage_weight_limit_pounds_to_kg"
    name = r.choice(SA_NAMES)
    weight_lb = r.choice([48, 50, 52, 54, 56])
    weight_kg = round(weight_lb / 2.205, 2)
    limit_kg = 23.00
    exceeds = weight_kg > limit_kg
    diff = round(abs(weight_kg - limit_kg), 2)

    if exceeds:
        correct_ans = f"Exceeds limit by {_fmt(diff)} kg ({_fmt(weight_kg)} kg > 23 kg)"
    else:
        correct_ans = f"Within limit by {_fmt(diff)} kg ({_fmt(weight_kg)} kg ≤ 23 kg)"

    prompt = (
        f"{name} is checking in a suitcase for an international flight with a free baggage allowance limit of **23 kg**.\n"
        f"The bathroom scale at home displays the suitcase weight as **{weight_lb} lb**.\n\n"
        f"**Given conversion factor**: $1\\text{{ kg}} \\approx 2,205\\text{{ lb}}$\n\n"
        f"Determine whether {name}'s suitcase complies with the 23 kg airline limit."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Convert the suitcase mass from pounds to kilograms by dividing by 2,205, then compare with 23 kg.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Mass in kg}} = \\frac{{{weight_lb}}}{{2,205}} = {_fmt(weight_kg)}\\text{{ kg}}$$\n"
        f"$$\\text{{Difference from limit}} = |{_fmt(weight_kg)} - 23,00| = {_fmt(diff)}\\text{{ kg}}$$ "
        f"✓ [1 Mark: Method – converting pounds to kilograms and comparing with 23 kg limit]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate compliance evaluation and difference]"
    )

    d1 = f"Within limit by {_fmt(diff)} kg ({_fmt(weight_kg)} kg ≤ 23 kg)" if exceeds else f"Exceeds limit by {_fmt(diff)} kg ({_fmt(weight_kg)} kg > 23 kg)"
    d2 = f"Exceeds limit by {_fmt(weight_lb - 23)} kg"
    d3 = f"Exactly on the limit at 23,00 kg"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Convert {weight_lb} lb to kg by dividing by 2,205.",
        tier_2=f"{weight_lb} ÷ 2,205 = {_fmt(weight_kg)} kg. Compare with 23 kg.",
        tier_3=f"Status: {correct_ans}.",
        r=r,
    )


def _gen_baby_birth_weight_grams_to_pounds_ounces(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_baby_birth_weight_grams_to_pounds_ounces"
    grams = r.choice([3200, 3400, 3600, 3800])
    total_oz = round(grams / 28.35, 1)
    pounds = int(total_oz // 16)
    rem_oz = round(total_oz % 16, 1)
    correct_ans = f"{pounds} lb {_fmt(rem_oz)} oz"

    prompt = (
        f"A newborn baby has a birth weight recorded at a hospital as **{grams} g**.\n\n"
        f"**Given conversion factors**:\n"
        f"  • $1\\text{{ ounce (oz)}} \\approx 28,35\\text{{ g}}$\n"
        f"  • $1\\text{{ pound (lb)}} = 16\\text{{ ounces}}$\n\n"
        f"Convert the baby's birth weight into **pounds and ounces**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Convert grams to total ounces by dividing by 28,35, then divide total ounces by 16 to find pounds and remainder ounces.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total Ounces}} = \\frac{{{grams}}}{{28,35}} = {_fmt(total_oz)}\\text{{ oz}}$$\n"
        f"$$\\text{{Pounds}} = {total_oz} \\div 16 = {pounds}\\text{{ full pounds with remainder }}{_fmt(rem_oz)}\\text{{ oz}}$$ "
        f"✓ [1 Mark: Method – dividing grams by 28,35 and separating into pounds and ounces (16 oz/lb)]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Weight}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate pounds and ounces]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide grams by 28,35 to get total ounces. Then divide by 16 to find pounds.",
        tier_2=f"{grams} ÷ 28,35 = {_fmt(total_oz)} oz = {pounds} lb {_fmt(rem_oz)} oz.",
        tier_3=f"Weight = {correct_ans}.",
        r=r,
    )


def _gen_agricultural_feed_bulk_bags_conversion(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_agricultural_feed_bulk_bags_conversion"
    num_bags = r.choice([20, 40, 50, 100])
    bag_lb = 50.0  # 50-pound bag
    total_lb = num_bags * bag_lb
    total_kg = round(total_lb / 2.205, 1)
    correct_ans = f"{_fmt(total_kg)} kg"

    prompt = (
        f"A dairy farmer orders **{num_bags} bags** of cattle feed supplement from an agricultural importer.\n"
        f"Each bag weighs **50 lb**.\n\n"
        f"**Given conversion factor**: $1\\text{{ kg}} \\approx 2,205\\text{{ lb}}$\n\n"
        f"Calculate the **total mass of the order in kilograms (kg)**, rounded to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate total pounds ({num_bags} bags $\\times 50\\text{{ lb}}$), then divide by 2,205 to convert to kilograms.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total Pounds}} = {num_bags} \\times 50 = {_fmt(int(total_lb))}\\text{{ lb}}$$\n"
        f"$$\\text{{Total Kilograms}} = \\frac{{{_fmt(int(total_lb))}}}{{2,205}} = {_fmt(total_kg)}\\text{{ kg}}$$ "
        f"✓ [1 Mark: Method – multiplying bags by weight and dividing by 2,205]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Mass}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate order mass in kg]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Total lb = {num_bags} × 50 lb. Divide total by 2,205.",
        tier_2=f"{total_lb} ÷ 2,205 = {correct_ans}.",
        tier_3=f"Total mass = {correct_ans}.",
        r=r,
    )
