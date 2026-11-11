"""Subskills 9 to 16: 2D Surface Area, Composite Polygons, Tiling & Paving.
Covers rectangular, triangular, circular, and trapezoidal areas, L-shaped composite decompositions,
tile box calculations with 10% cutting wastage, paving brick counts, and lawn turf installation.
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    PI,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_09(r: random.Random) -> Dict[str, Any]:
    """Subskill 09: Area of a rectangular room or paved driveway."""
    l = r.choice([6.5, 7.2, 8.0, 9.5])
    w = r.choice([4.0, 4.5, 5.0, 6.0])
    area = round(l * w, 2)

    prompt = (
        f"A homeowner plans to pave a rectangular driveway measuring {_fmt(l)} m in length and {_fmt(w)} m in width.\n\n"
        f"Calculate the total area of the driveway in square metres (m²)."
    )

    correct_ans = f"{_fmt(area)} m²"
    explanation = (
        f"1. Formula: Area = Length × Width.\n"
        f"2. Substitution: Area = {_fmt(l)} m × {_fmt(w)} m = {correct_ans}."
    )
    t1 = "Multiply length by width to find the area of a rectangle."
    t2 = f"Calculation: {l} × {w}."
    t3 = f"Area = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_09",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: Area of a triangular garden bed."""
    base = r.choice([5.0, 6.4, 7.2, 8.5])
    height = r.choice([3.0, 4.2, 5.0, 6.0])
    area = round(0.5 * base * height, 2)

    prompt = (
        f"A landscaping feature includes a triangular flower bed with a base of {_fmt(base)} m "
        f"and a perpendicular height of {_fmt(height)} m.\n\n"
        f"Using the formula: Area = ½ × base × height,\n"
        f"calculate the area of the flower bed in square metres (m²)."
    )

    correct_ans = f"{_fmt(area)} m²"
    explanation = (
        f"1. Formula: Area = ½ × base × height.\n"
        f"2. Substitution: Area = 0,5 × {_fmt(base)} m × {_fmt(height)} m = {correct_ans}."
    )
    t1 = "Multiply 0,5 by the base, then multiply by the perpendicular height."
    t2 = f"Calculation: 0,5 × {base} × {height}."
    t3 = f"Area = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_10",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Subskill 11: Area of a circular lawn or swimming pool cover."""
    diameter = r.choice([6.0, 8.0, 10.0, 12.0])
    radius = diameter / 2.0
    area = round(PI * (radius ** 2), 2)

    prompt = (
        f"A circular splash pool has a diameter of {_fmt(diameter)} m (radius = {_fmt(radius)} m).\n"
        f"A protective winter cover is ordered to fit the surface of the pool.\n\n"
        f"Using the formula: Area = π × (radius)² (where π = 3,142),\n"
        f"calculate the surface area of the pool cover (rounded to 2 decimal places)."
    )

    correct_ans = f"{_fmt(area)} m²"
    explanation = (
        f"1. Radius = Diameter ÷ 2 = {_fmt(diameter)} m ÷ 2 = {_fmt(radius)} m.\n"
        f"2. Formula: Area = π × r² = 3,142 × ({_fmt(radius)} m)²\n"
        f"   = 3,142 × {radius**2:.2f} m² = {correct_ans}."
    )
    t1 = f"Square the radius ({radius}² = {radius**2:.2f}), then multiply by π (3,142)."
    t2 = f"Calculation: 3,142 × {radius**2:.2f}."
    t3 = f"Area = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_11",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Subskill 12: Area of a trapezoidal plot of land."""
    a = r.choice([12.0, 15.0, 18.0])  # top parallel side
    b = r.choice([20.0, 24.0, 28.0])  # bottom parallel side
    h = r.choice([8.0, 10.0, 12.0])   # perpendicular height
    area = round(0.5 * (a + b) * h, 2)

    prompt = (
        f"A township residential erf has the shape of a trapezium with parallel boundary lengths of "
        f"{_fmt(a)} m and {_fmt(b)} m, and a perpendicular depth (height) of {_fmt(h)} m.\n\n"
        f"Using the formula: Area = ½ × (a + b) × h,\n"
        f"calculate the area of the erf in square metres (m²)."
    )

    correct_ans = f"{_fmt(area)} m²"
    explanation = (
        f"1. Sum of parallel sides = {_fmt(a)} m + {_fmt(b)} m = {a + b} m.\n"
        f"2. Formula: Area = 0,5 × ({a + b} m) × {_fmt(h)} m = {correct_ans}."
    )
    t1 = f"Add the two parallel sides: {a} + {b} = {a + b}."
    t2 = f"Multiply the sum by 0,5 and then by height ({h})."
    t3 = f"Area = 0,5 × {a + b} × {h} = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_12",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Area of an L-shaped room decomposed into two rectangles."""
    # Main rectangle: 8m x 5m; Extension: 4m x 3m
    l1, w1 = 8.0, 5.0
    l2, w2 = 4.0, 3.0
    area1 = l1 * w1
    area2 = l2 * w2
    total_area = area1 + area2

    prompt = (
        f"An open-plan living room and dining area has an L-shaped floor plan that can be decomposed "
        f"into two adjacent rectangular sections:\n"
        f"• Section A (Lounge): {_fmt(l1)} m long by {_fmt(w1)} m wide\n"
        f"• Section B (Dining nook): {_fmt(l2)} m long by {_fmt(w2)} m wide\n\n"
        f"Calculate the total floor area of the L-shaped room in square metres (m²)."
    )

    correct_ans = f"{_fmt(total_area)} m²"
    explanation = (
        f"1. Area of Section A = {_fmt(l1)} m × {_fmt(w1)} m = {_fmt(area1)} m².\n"
        f"2. Area of Section B = {_fmt(l2)} m × {_fmt(w2)} m = {_fmt(area2)} m².\n"
        f"3. Total area = {_fmt(area1)} m² + {_fmt(area2)} m² = {correct_ans}."
    )
    t1 = f"Calculate Area A: {l1} × {w1} = {area1} m²."
    t2 = f"Calculate Area B: {l2} × {w2} = {area2} m²."
    t3 = f"Add both areas: {area1} + {area2} = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_13",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Subskill 14: Floor tiling calculation: room area, 10% cutting wastage, and box counts."""
    room_l = r.choice([5.0, 6.0, 7.0])
    room_w = r.choice([4.0, 4.5, 5.0])
    room_area = room_l * room_w  # e.g. 24 m²

    area_with_waste = round(room_area * 1.10, 2)  # add 10%
    box_coverage = 1.44  # 1,44 m² per box of tiles
    boxes_needed = int((area_with_waste + box_coverage - 0.001) // box_coverage)
    price_per_box = 189.00
    total_cost = round(boxes_needed * price_per_box, 2)

    prompt = (
        f"A contractor is tiling a rectangular floor measuring {_fmt(room_l)} m by {_fmt(room_w)} m (Area = {_fmt(room_area)} m²).\n"
        f"• The contractor must add 10% extra area to allow for tile cutting, trimming, and breakage\n"
        f"• Ceramic floor tiles are sold in boxes containing 1,44 m² of tiles at {_fmt_curr(price_per_box)} per box\n\n"
        f"Calculate the total cost to purchase the required whole boxes of tiles."
    )

    correct_ans = _fmt_curr(total_cost)
    explanation = (
        f"1. Floor area with 10% wastage = {_fmt(room_area)} m² × 1,10 = {_fmt(area_with_waste)} m².\n"
        f"2. Boxes needed = {_fmt(area_with_waste)} m² ÷ 1,44 m²/box = {area_with_waste / box_coverage:.2f} boxes "
        f"→ round up to {boxes_needed} whole boxes.\n"
        f"3. Total cost = {boxes_needed} boxes × {_fmt_curr(price_per_box)} = {_fmt_curr(total_cost)}."
    )
    t1 = f"Add 10% wastage to floor area: {_fmt(room_area)} × 1,10 = {_fmt(area_with_waste)} m²."
    t2 = f"Divide by 1,44 m² per box and round up to the next whole box ({boxes_needed} boxes)."
    t3 = f"Multiply {boxes_needed} boxes by {_fmt_curr(price_per_box)} = {_fmt_curr(total_cost)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_14",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )


def gen_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Subskill 15: Paving brick count and cost calculation."""
    driveway_area_m2 = r.choice([36.0, 45.0, 54.0])
    # Standard bevel brick: 50 bricks per m²
    bricks_per_m2 = 50
    total_bricks = int(driveway_area_m2 * bricks_per_m2)
    cost_per_brick = 2.40
    total_brick_cost = round(total_bricks * cost_per_brick, 2)

    prompt = (
        f"A homeowner is paving an outdoor courtyard with an area of {_fmt(driveway_area_m2)} m².\n"
        f"• The chosen interlocking paving bricks require 50 bricks per square metre (m²)\n"
        f"• Each brick costs R 2,40\n\n"
        f"Calculate the total cost of the paving bricks required for the courtyard."
    )

    correct_ans = _fmt_curr(total_brick_cost)
    explanation = (
        f"1. Total bricks needed = {_fmt(driveway_area_m2)} m² × 50 bricks/m² = {total_bricks} bricks.\n"
        f"2. Total cost = {total_bricks} bricks × R 2,40/brick = {_fmt_curr(total_brick_cost)}."
    )
    t1 = f"Multiply the area ({_fmt(driveway_area_m2)} m²) by 50 to find total bricks."
    t2 = f"Multiply {total_bricks} bricks by R 2,40."
    t3 = f"Cost = {_fmt_curr(total_brick_cost)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_15",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Subskill 16: Instant lawn turf rolls installation (yard area minus patio)."""
    yard_l, yard_w = 12.0, 8.0
    patio_l, patio_w = 4.0, 3.0

    yard_area = yard_l * yard_w  # 96 m²
    patio_area = patio_l * patio_w  # 12 m²
    lawn_area = yard_area - patio_area  # 84 m²

    turf_roll_area = 1.0  # 1 m² per roll (e.g. Kikuyu instant lawn)
    price_per_roll = 35.00
    total_turf_cost = round(lawn_area * price_per_roll, 2)

    prompt = (
        f"A landscaper is planting instant Kikuyu lawn in a backyard measuring 12 m by 8 m.\n"
        f"The yard contains a concrete patio slab measuring 4 m by 3 m that will not be grassed.\n"
        f"Each roll of instant lawn covers exactly 1 m² and costs R 35,00.\n\n"
        f"Calculate the total cost to purchase the required rolls of instant lawn."
    )

    correct_ans = _fmt_curr(total_turf_cost)
    explanation = (
        f"1. Total yard area = 12 m × 8 m = {yard_area} m².\n"
        f"2. Patio area = 4 m × 3 m = {patio_area} m².\n"
        f"3. Lawn area to grass = {yard_area} m² - {patio_area} m² = {lawn_area} m².\n"
        f"4. Total cost = {lawn_area} rolls × R 35,00/roll = {_fmt_curr(total_turf_cost)}."
    )
    t1 = "Calculate total yard area and subtract the patio area."
    t2 = f"Net grass area = {yard_area} - {patio_area} = {lawn_area} m²."
    t3 = f"Multiply {lawn_area} rolls by R 35,00 = {_fmt_curr(total_turf_cost)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_16",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )
