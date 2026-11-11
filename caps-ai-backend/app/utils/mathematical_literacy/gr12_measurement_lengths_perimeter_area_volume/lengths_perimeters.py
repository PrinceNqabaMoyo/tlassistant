"""Subskills 1 to 8: Measuring, Estimation, Lengths & Perimeters.
Covers body/indigenous benchmarks, perimeter reasonableness checks, rectangular boundaries,
circular circumferences, composite running tracks, bordering with joint spacing, gate deductions, and multi-strand fencing.
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


def gen_subskill_01(r: random.Random) -> Dict[str, Any]:
    """Subskill 01: Estimating dimensions using indigenous/body benchmarks."""
    unit_info = r.choice([
        ("1 pace (stride)", "approximately 1 metre (1 m)", "estimating the length of a boundary fence across a soccer field"),
        ("1 hand span (from thumb to pinky)", "approximately 20 cm (0,2 m)", "estimating the width of a small desk or book"),
        ("1 cubit (elbow to middle fingertip)", "approximately 45 to 50 cm (0,5 m)", "estimating the depth of a flower bed or trench"),
    ])
    unit_name, approx_metric, context = unit_info

    prompt = (
        f"In practical mathematical estimation, indigenous and body-based units of measurement "
        f"provide reliable approximations when measuring tools are unavailable.\n\n"
        f"Which of the following correctly pairs '{unit_name}' with its approximate metric equivalent "
        f"and an appropriate real-world estimation context?"
    )

    correct_ans = f"{unit_name} ≈ {approx_metric}; suitable for {context}"
    custom_opts = [
        f"{unit_name} ≈ {approx_metric}; suitable for {context}",
        f"{unit_name} ≈ approximately 5 metres; suitable for measuring highway distances between towns",
        f"{unit_name} ≈ approximately 1 millimetre; suitable for measuring sheet metal thickness",
        f"{unit_name} ≈ approximately 10 metres; suitable for measuring Olympic swimming pool depth",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"1. Body-based estimation benchmarks:\n"
        f"   • 1 pace ≈ 1 m (distance, field boundaries)\n"
        f"   • 1 hand span ≈ 20 cm (furniture, desktop items)\n"
        f"   • 1 cubit ≈ 45–50 cm (trenches, fabric)\n"
        f"2. Therefore, '{unit_name}' is {correct_ans}."
    )
    t1 = "Recall the metric benchmarks for common body measurements."
    t2 = "A pace is roughly 1 m, a hand span is about 20 cm, and a cubit is about 0,5 m."
    t3 = f"Correct pairing: {correct_ans}."

    return _build_question_payload(
        "gr12_meas_subskill_01",
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


def gen_subskill_02(r: random.Random) -> Dict[str, Any]:
    """Subskill 02: Reasonableness check of a perimeter measurement against a soccer pitch benchmark."""
    field_l = 100
    field_w = 80
    soccer_perimeter = 2 * (field_l + field_w)  # 360 m

    claimed_perimeter = r.choice([150, 180, 220])  # student claimed school perimeter

    prompt = (
        f"A standard South African school soccer pitch has a length of {field_l} m and a width of {field_w} m "
        f"(total perimeter = {soccer_perimeter} m).\n\n"
        f"A learner was tasked with measuring the entire boundary fencing around the school grounds "
        f"(which contains four sports fields, classroom blocks, and parking lots).\n"
        f"The learner submitted an answer of {claimed_perimeter} m.\n\n"
        f"Referring to the soccer pitch benchmark, assess whether this answer is reasonable."
    )

    correct_ans = f"Unreasonable: The entire school boundary ({claimed_perimeter} m) cannot be less than a single soccer pitch ({soccer_perimeter} m)"
    custom_opts = [
        f"Unreasonable: The entire school boundary ({claimed_perimeter} m) cannot be less than a single soccer pitch ({soccer_perimeter} m)",
        f"Reasonable: {claimed_perimeter} m is an appropriate perimeter for a large secondary school property",
        f"Reasonable: A soccer pitch perimeter is 100 m, so {claimed_perimeter} m is sufficient",
        f"Cannot be assessed without knowing the exact width of the fencing posts",
    ]
    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"1. Perimeter of a single soccer pitch = 2 × (100 m + 80 m) = 360 m.\n"
        f"2. A full school campus containing multiple fields and buildings must have a perimeter much larger than 360 m.\n"
        f"3. A figure of {claimed_perimeter} m is far too small (less than one field), so it is completely unreasonable."
    )
    t1 = f"Compare {claimed_perimeter} m with the benchmark perimeter of a single soccer pitch ({soccer_perimeter} m)."
    t2 = "A school with multiple fields must have a perimeter significantly greater than a single soccer field."
    t3 = f"Conclusion: {correct_ans}."

    return _build_question_payload(
        "gr12_meas_subskill_02",
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


def gen_subskill_03(r: random.Random) -> Dict[str, Any]:
    """Subskill 03: Perimeter of a rectangular property boundary."""
    name = r.choice(SA_NAMES)
    length = r.randint(45, 75)
    width = r.randint(25, 40)
    perimeter = 2 * (length + width)

    prompt = (
        f"{name}'s family property has a rectangular plot with a street frontage length of {length} m "
        f"and a depth (width) of {width} m.\n\n"
        f"Calculate the total perimeter of the property in metres (m)."
    )

    correct_ans = f"{perimeter} m"
    explanation = (
        f"1. Formula: Perimeter = 2 × (Length + Width).\n"
        f"2. Substitution: Perimeter = 2 × ({length} m + {width} m) = 2 × {length + width} m = {perimeter} m."
    )
    t1 = "Add length and width, then multiply by 2."
    t2 = f"Perimeter = 2 × ({length} + {width})."
    t3 = f"Calculate: 2 × {length + width} = {perimeter} m."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_03",
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


def gen_subskill_04(r: random.Random) -> Dict[str, Any]:
    """Subskill 04: Perimeter / Circumference of a circular garden or roundabout."""
    diameter = r.choice([14.0, 20.0, 28.0, 35.0])
    radius = diameter / 2.0
    # Circumference = pi * d
    circumference = round(PI * diameter, 2)

    prompt = (
        f"A landscaping design features a circular traffic roundabout with a diameter of {diameter} m.\n"
        f"Precast concrete kerbing stones will be placed along the entire circumference of the circle.\n\n"
        f"Using the formula: Circumference = π × diameter (where π = 3,142),\n"
        f"calculate the length of kerbing required (rounded to 2 decimal places)."
    )

    correct_ans = f"{_fmt(circumference)} m"
    explanation = (
        f"1. Formula: Circumference = π × d.\n"
        f"2. Substitution: Circumference = 3,142 × {diameter} m = {circumference:.2f} m.\n"
        f"3. Result = {correct_ans}."
    )
    t1 = f"Multiply the diameter ({diameter} m) by π (3,142)."
    t2 = f"Calculation: 3,142 × {diameter}."
    t3 = f"Result = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_04",
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


def gen_subskill_05(r: random.Random) -> Dict[str, Any]:
    """Subskill 05: Perimeter of an athletic track (rectangle with two semi-circular ends)."""
    straight_l = r.choice([80.0, 90.0, 100.0])
    width_d = r.choice([60.0, 64.0, 70.0])  # diameter of semi-circular ends

    # Perimeter = 2 straights + 1 full circle circumference (2 semi-circles = 1 circle)
    straights_total = 2 * straight_l
    curve_circumference = round(PI * width_d, 2)
    total_track_perimeter = round(straights_total + curve_circumference, 2)

    prompt = (
        f"A school sports running track consists of a rectangular infield with two straight sections "
        f"measuring {straight_l} m each, flanked by two semi-circular curved ends with a diameter of {width_d} m.\n\n"
        f"Using the formula: Circumference of a circle = π × diameter (where π = 3,142),\n"
        f"calculate the total perimeter of the running track (rounded to 2 decimal places)."
    )

    correct_ans = f"{_fmt(total_track_perimeter)} m"
    explanation = (
        f"1. Two straight sections = 2 × {straight_l} m = {straights_total} m.\n"
        f"2. Two semi-circular ends combine to form one full circle with diameter {width_d} m.\n"
        f"   Circumference = 3,142 × {width_d} m = {_fmt(curve_circumference)} m.\n"
        f"3. Total track perimeter = {straights_total} m + {_fmt(curve_circumference)} m = {correct_ans}."
    )
    t1 = f"Sum the two straights (2 × {straight_l} m) and the two semi-circles (1 full circle: 3,142 × {width_d} m)."
    t2 = f"Straights = {straights_total} m; Curves = {curve_circumference} m."
    t3 = f"Total = {straights_total} + {curve_circumference} = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_05",
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


def gen_subskill_06(r: random.Random) -> Dict[str, Any]:
    """Subskill 06: Bordering with tiles taking into account grout/spacing width and rounding up."""
    wall_length_cm = r.choice([420, 508, 560, 640])
    tile_width_cm = 20.0
    grout_cm = 0.5  # 5 mm joint spacing
    effective_width = tile_width_cm + grout_cm  # 20,5 cm

    exact_tiles = wall_length_cm / effective_width
    tiles_needed = int(exact_tiles + 0.999)  # round up

    prompt = (
        f"A tiler is installing decorative border tiles along a bathroom wall measuring {wall_length_cm} cm in length.\n"
        f"• Each border tile is 20 cm wide\n"
        f"• A grout spacer of 0,5 cm (5 mm) is placed between adjacent tiles\n\n"
        f"Calculate the minimum number of border tiles required to complete the wall border (round up to the next whole tile)."
    )

    correct_ans = f"{tiles_needed} tiles"
    explanation = (
        f"1. Effective width of one tile including grout spacing = 20 cm + 0,5 cm = {effective_width} cm.\n"
        f"2. Number of tiles = Total wall length ÷ Effective width\n"
        f"   = {wall_length_cm} cm ÷ {effective_width} cm = {exact_tiles:.2f} tiles.\n"
        f"3. Round up to whole tiles: {tiles_needed} tiles."
    )
    t1 = f"Add the tile width (20 cm) and grout spacer (0,5 cm) to get effective width ({effective_width} cm)."
    t2 = f"Divide wall length ({wall_length_cm} cm) by effective width ({effective_width} cm)."
    t3 = f"Round up {exact_tiles:.2f} to {tiles_needed} tiles."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_06",
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


def gen_subskill_07(r: random.Random) -> Dict[str, Any]:
    """Subskill 07: Fencing cost calculation: deducting gate openings and multiplying by cost/m."""
    name = r.choice(SA_NAMES)
    l = 60
    w = 40
    perimeter = 2 * (l + w)  # 200 m

    # Gate openings: 1 vehicle gate of 4 m and 1 pedestrian gate of 1 m
    gate_total_m = 5.0
    fence_length = perimeter - gate_total_m  # 195 m
    cost_per_metre = r.choice([165.0, 185.0, 210.0])
    total_fence_cost = round(fence_length * cost_per_metre, 2)

    prompt = (
        f"{name} is installing ClearVu security fencing around a rectangular depot measuring {l} m by {w} m.\n"
        f"The boundary includes a 4 m vehicle gate and a 1 m pedestrian gate that will not be fenced.\n"
        f"The fencing costs {_fmt_curr(cost_per_metre)} per metre installed.\n\n"
        f"Calculate the total cost of the security fence (excluding the gates)."
    )

    correct_ans = _fmt_curr(total_fence_cost)
    explanation = (
        f"1. Total plot perimeter = 2 × ({l} m + {w} m) = {perimeter} m.\n"
        f"2. Deduct gates: Fencing length = {perimeter} m - (4 m + 1 m) = {fence_length} m.\n"
        f"3. Total fencing cost = {fence_length} m × {_fmt_curr(cost_per_metre)}/m = {_fmt_curr(total_fence_cost)}."
    )
    t1 = f"Find total boundary perimeter: 2 × ({l} + {w}) = {perimeter} m."
    t2 = f"Subtract gate openings (5 m): {perimeter} - 5 = {fence_length} m."
    t3 = f"Multiply by cost per metre: {fence_length} × {_fmt_curr(cost_per_metre)} = {_fmt_curr(total_fence_cost)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_07",
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


def gen_subskill_08(r: random.Random) -> Dict[str, Any]:
    """Subskill 08: Multi-strand farm wire fencing: total wire length and roll requirements."""
    farm_l = 120
    farm_w = 80
    perimeter = 2 * (farm_l + farm_w)  # 400 m
    strands = 4  # 4-strand barbed wire fence
    total_wire_needed = perimeter * strands  # 1 600 m

    roll_length = 500  # 500 m per roll
    rolls_needed = int((total_wire_needed + roll_length - 1) // roll_length)  # 4 rolls
    price_per_roll = 1250.00
    total_cost = round(rolls_needed * price_per_roll, 2)

    prompt = (
        f"A farmer fences a rectangular grazing paddock measuring {farm_l} m by {farm_w} m with a 4-strand barbed wire fence.\n"
        f"• The perimeter requires 4 separate parallel strands of wire all the way around\n"
        f"• Barbed wire is sold in 500 m rolls at {_fmt_curr(price_per_roll)} per roll\n\n"
        f"Calculate the total cost to purchase the required number of full wire rolls (rounded up to the nearest whole roll)."
    )

    correct_ans = _fmt_curr(total_cost)
    explanation = (
        f"1. Perimeter of paddock = 2 × ({farm_l} m + {farm_w} m) = {perimeter} m.\n"
        f"2. Total wire length for {strands} strands = {perimeter} m × {strands} = {total_wire_needed} m.\n"
        f"3. Rolls needed = {total_wire_needed} m ÷ {roll_length} m = {total_wire_needed / roll_length:.1f} rolls "
        f"→ round up to {rolls_needed} full rolls.\n"
        f"4. Total cost = {rolls_needed} rolls × {_fmt_curr(price_per_roll)} = {_fmt_curr(total_cost)}."
    )
    t1 = f"Calculate paddock perimeter: 2 × ({farm_l} + {farm_w}) = {perimeter} m."
    t2 = f"Multiply by 4 strands: {perimeter} × 4 = {total_wire_needed} m, then divide by 500 m to find rolls."
    t3 = f"Multiply {rolls_needed} rolls by {_fmt_curr(price_per_roll)} = {_fmt_curr(total_cost)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_08",
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
