"""Subskills 1 to 9: Perimeter, Circumference & 2D Base Area Foundation for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_1(r: random.Random) -> Dict[str, Any]:
    """Subskill 1: Rectangle perimeter and fencing cost estimation (with gate deduction)."""
    length = r.randint(15, 35)
    width = r.randint(8, 20)
    gate_width = r.choice([2, 3, 4])
    cost_per_m = r.choice([85.0, 110.0, 125.0, 140.0])

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} wants to fence a rectangular vegetable garden measuring **{length} m** long by **{width} m** wide.\n"
        f"A **{gate_width} m** wide gate will be left unfenced on one side.\n"
        f"Diamond mesh wire fencing costs **{_fmt_curr(cost_per_m)} per metre**.\n\n"
        f"Calculate the **total cost** of the wire fencing required to enclose the garden.\n"
        f"*(Formula: $\\text{{Perimeter}} = 2(l + w)$)*"
    )

    perim = 2 * (length + width)
    fence_length = perim - gate_width
    total_cost = fence_length * cost_per_m

    correct_ans = _fmt_curr(total_cost)

    # Distractor 1: Forgot gate deduction
    cost_no_gate = perim * cost_per_m
    # Distractor 2: Only length + width
    half_cost = (length + width - gate_width) * cost_per_m

    custom_opts = [
        correct_ans,
        _fmt_curr(cost_no_gate),
        _fmt_curr(half_cost),
        _fmt_curr(total_cost + cost_per_m * 5),
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the total perimeter of the rectangular garden [1 mark]:\n"
        f"Perimeter = 2({length} m + {width} m) = 2({length + width} m) = {perim} m.\n\n"
        f"Step 2: Deduct the gate width to find the fencing length required [1 mark]:\n"
        f"Fencing Length = {perim} m - {gate_width} m = {fence_length} m.\n\n"
        f"Step 3: Calculate total cost [1 mark]:\n"
        f"Total Cost = {fence_length} m × {_fmt_curr(cost_per_m)}/m = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_1",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the perimeter: 2 × (length + width), subtract the gate width, then multiply by the cost per metre.",
        tier_2=f"Perimeter = 2({length} + {width}) = {perim} m. Net fencing = {perim} - {gate_width} = {fence_length} m.",
        tier_3=f"Total cost = {fence_length} × R {cost_per_m:.2f} = {correct_ans}.",
        r=r,
    )


def generate_subskill_2(r: random.Random) -> Dict[str, Any]:
    """Subskill 2: Circular garden bed circumference & border edging."""
    diameter = r.choice([4.0, 5.0, 6.0, 7.0, 8.0])
    radius = diameter / 2.0
    cost_per_m = r.choice([45.0, 55.0, 65.0, 75.0])
    pi_val = 3.142

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is installing flexible plastic edging around the circumference of a circular rose garden.\n"
        f"The garden has a diameter of **{_fmt(diameter)} m**.\n"
        f"The edging material costs **{_fmt_curr(cost_per_m)} per linear metre**.\n\n"
        f"Calculate the **circumference** of the rose garden and the **total cost** of the edging.\n"
        f"*(Use $\\pi = 3,142$ and $\\text{{Circumference}} = \\pi \\times d$ or $2 \\times \\pi \\times r$. Round circumference to 2 decimal places)*"
    )

    circ = round(pi_val * diameter, 2)
    total_cost = round(circ * cost_per_m, 2)

    correct_ans = f"Circumference: {_fmt(circ)} m; Cost: {_fmt_curr(total_cost)}"

    # Distractor using radius as diameter
    circ_r = round(pi_val * radius, 2)
    cost_r = round(circ_r * cost_per_m, 2)
    dist_1 = f"Circumference: {_fmt(circ_r)} m; Cost: {_fmt_curr(cost_r)}"

    # Distractor using area formula
    area_c = round(pi_val * (radius ** 2), 2)
    cost_a = round(area_c * cost_per_m, 2)
    dist_2 = f"Circumference: {_fmt(area_c)} m; Cost: {_fmt_curr(cost_a)}"

    custom_opts = [
        correct_ans,
        dist_1,
        dist_2,
        f"Circumference: {_fmt(circ + 2.0)} m; Cost: {_fmt_curr(total_cost + cost_per_m * 2)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the circumference of the circle [1 mark]:\n"
        f"Circumference = $\\pi \\times d$ = 3,142 × {_fmt(diameter)} m = {_fmt(circ)} m.\n\n"
        f"Step 2: Multiply circumference by cost per linear metre [1 mark]:\n"
        f"Total Cost = {_fmt(circ)} m × {_fmt_curr(cost_per_m)}/m = {_fmt_curr(total_cost)}.\n\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_2",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Circumference = π × diameter. Then multiply by the cost per metre.",
        tier_2=f"Circumference = 3,142 × {diameter} = {circ} m. Cost = {circ} × R {cost_per_m:.2f}.",
        tier_3=f"Result: {correct_ans}.",
        r=r,
    )


def generate_subskill_3(r: random.Random) -> Dict[str, Any]:
    """Subskill 3: Semi-circular driveway turning circle perimeter."""
    radius = r.choice([3.5, 4.0, 5.0, 6.0])
    pi_val = 3.142

    name = r.choice(SA_NAMES)

    prompt = (
        f"A residential property has a semi-circular paved turning circle at the end of the driveway with radius **{_fmt(radius)} m**.\n"
        f"{name} needs to lay concrete kerbing along the entire closed perimeter (both the curved curved arc and the straight diameter base).\n\n"
        f"Calculate the **total perimeter** of this semi-circular area.\n"
        f"*(Use $\\pi = 3,142$ and $\\text{{Perimeter of semi-circle}} = (\\pi \\times r) + (2 \\times r)$. Round to 2 decimal places)*"
    )

    arc_len = round(pi_val * radius, 2)
    diameter = round(2 * radius, 2)
    total_perim = round(arc_len + diameter, 2)

    correct_ans = f"{_fmt(total_perim)} m"

    # Distractor: Only arc length
    dist_arc = f"{_fmt(arc_len)} m"
    # Distractor: Full circle perimeter
    full_c = round(2 * pi_val * radius, 2)
    dist_full = f"{_fmt(full_c)} m"

    custom_opts = [
        correct_ans,
        dist_arc,
        dist_full,
        f"{_fmt(round(total_perim + 3.0, 2))} m",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the curved semi-circular arc length [1 mark]:\n"
        f"Arc Length = $\\pi \\times r$ = 3,142 × {_fmt(radius)} m = {_fmt(arc_len)} m.\n\n"
        f"Step 2: Calculate the straight diameter edge [1 mark]:\n"
        f"Diameter = 2 × {_fmt(radius)} m = {_fmt(diameter)} m.\n\n"
        f"Step 3: Sum to find total closed perimeter [1 mark]:\n"
        f"Total Perimeter = {_fmt(arc_len)} m + {_fmt(diameter)} m = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_3",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="A closed semi-circle has two parts: the curved arc (π × r) plus the straight diameter (2 × r).",
        tier_2=f"Arc = 3,142 × {radius} = {arc_len} m. Straight edge = 2 × {radius} = {diameter} m.",
        tier_3=f"Total perimeter = {arc_len} + {diameter} = {correct_ans}.",
        r=r,
    )


def generate_subskill_4(r: random.Random) -> Dict[str, Any]:
    """Subskill 4: Rectangular room floor area & skirting board perimeter."""
    length = r.randint(5, 9)
    width = r.randint(4, 6)
    door_opening = r.choice([0.85, 0.90, 1.0])

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is renovating a rectangular bedroom measuring **{length} m** in length and **{width} m** in width.\n"
        f"They need to install wooden skirting boards around the base of the walls.\n"
        f"The bedroom door opening is **{_fmt(door_opening)} m** wide and requires no skirting board.\n\n"
        f"Calculate the **floor area** of the room and the **length of skirting board** needed.\n"
        f"*(Formulas: $\\text{{Area}} = l \\times w$; $\\text{{Perimeter}} = 2(l + w)$)*"
    )

    area = length * width
    perim = 2 * (length + width)
    skirting = round(perim - door_opening, 2)

    correct_ans = f"Floor Area: {_fmt(area)} m²; Skirting: {_fmt(skirting)} m"

    custom_opts = [
        correct_ans,
        f"Floor Area: {_fmt(area)} m²; Skirting: {_fmt(perim)} m",
        f"Floor Area: {_fmt(perim)} m²; Skirting: {_fmt(skirting)} m",
        f"Floor Area: {_fmt(area * 2)} m²; Skirting: {_fmt(skirting)} m",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate floor area [1 mark]:\n"
        f"Area = length × width = {length} m × {width} m = {_fmt(area)} m².\n\n"
        f"Step 2: Calculate room perimeter [1 mark]:\n"
        f"Perimeter = 2({length} m + {width} m) = 2({length + width}) = {perim} m.\n\n"
        f"Step 3: Deduct door opening to find skirting required [1 mark]:\n"
        f"Skirting = {perim} m - {_fmt(door_opening)} m = {_fmt(skirting)} m.\n"
        f"Conclusion: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_4",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Floor Area = length × width. Skirting = perimeter minus the door opening.",
        tier_2=f"Area = {length} × {width} = {area} m². Perimeter = 2({length}+{width}) = {perim} m. Skirting = {perim} - {door_opening}.",
        tier_3=f"Result: {correct_ans}.",
        r=r,
    )


def generate_subskill_5(r: random.Random) -> Dict[str, Any]:
    """Subskill 5: Triangular gable wall area."""
    base_m = r.choice([6.0, 7.0, 8.0, 9.0, 10.0])
    height_m = r.choice([2.4, 2.8, 3.0, 3.2, 3.5])

    name = r.choice(SA_NAMES)

    prompt = (
        f"A builder needs to paint the triangular gable end of a house roof pitch.\n"
        f"The base of the triangle measures **{_fmt(base_m)} m** and the vertical height from the base to the roof apex is **{_fmt(height_m)} m**.\n\n"
        f"Calculate the **area of the triangular gable wall**.\n"
        f"*(Formula: $\\text{{Area of Triangle}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}$)*"
    )

    area = round(0.5 * base_m * height_m, 2)
    correct_ans = f"{_fmt(area)} m²"

    # Distractor: Forgot 1/2
    dist_no_half = f"{_fmt(round(base_m * height_m, 2))} m²"
    # Distractor: perimeter sum
    dist_sum = f"{_fmt(round(base_m + height_m, 2))} m²"

    custom_opts = [
        correct_ans,
        dist_no_half,
        dist_sum,
        f"{_fmt(round(area + 4.0, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State the formula for area of a triangle [1 mark]:\n"
        f"Area = 1/2 × base × height.\n\n"
        f"Step 2: Substitute given measurements [1 mark]:\n"
        f"Area = 0,5 × {_fmt(base_m)} m × {_fmt(height_m)} m.\n\n"
        f"Step 3: Calculate final area [1 mark]:\n"
        f"Area = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_5",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Use the formula Area = 1/2 × base × height.",
        tier_2=f"Area = 0,5 × {base_m} × {height_m}.",
        tier_3=f"Area = {correct_ans}.",
        r=r,
    )


def generate_subskill_6(r: random.Random) -> Dict[str, Any]:
    """Subskill 6: Circular pond / pool surface area."""
    radius_m = r.choice([2.1, 2.5, 3.0, 3.5, 4.2])
    pi_val = 3.142

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is installing a protective safety cover over a circular swimming pool with a radius of **{_fmt(radius_m)} m**.\n\n"
        f"Calculate the **surface area** of the circular pool that the cover must span.\n"
        f"*(Use $\\pi = 3,142$ and $\\text{{Area}} = \\pi \\times r^2$. Round your answer to 2 decimal places)*"
    )

    area = round(pi_val * (radius_m ** 2), 2)
    correct_ans = f"{_fmt(area)} m²"

    # Distractor 1: Circumference formula 2*pi*r
    circ = round(2 * pi_val * radius_m, 2)
    # Distractor 2: (pi * r)^2
    dist_sq = round((pi_val * radius_m) ** 2, 2)

    custom_opts = [
        correct_ans,
        f"{_fmt(circ)} m²",
        f"{_fmt(round(area / 2, 2))} m²",
        f"{_fmt(round(area + 5.0, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State the formula for the area of a circle [1 mark]:\n"
        f"Area = $\\pi \\times r^2$.\n\n"
        f"Step 2: Substitute radius and square it [1 mark]:\n"
        f"Area = 3,142 × ({_fmt(radius_m)})² = 3,142 × {_fmt(round(radius_m ** 2, 4))}.\n\n"
        f"Step 3: Calculate surface area with units [1 mark]:\n"
        f"Area = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_6",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Square the radius first, then multiply by π (3,142).",
        tier_2=f"r² = {radius_m}² = {radius_m**2:.2f}. Area = 3,142 × {radius_m**2:.2f}.",
        tier_3=f"Area = {correct_ans}.",
        r=r,
    )


def generate_subskill_7(r: random.Random) -> Dict[str, Any]:
    """Subskill 7: Trapezoidal flower bed area."""
    side_a = r.randint(4, 7)
    side_b = side_a + r.randint(3, 5)
    height = r.randint(3, 6)

    name = r.choice(SA_NAMES)

    prompt = (
        f"A landscaping design features a flower bed shaped as a trapezium.\n"
        f"The two parallel sides measure **{side_a} m** and **{side_b} m**, and the perpendicular distance (height) between them is **{height} m**.\n\n"
        f"Calculate the **area of the trapezoidal flower bed**.\n"
        f"*(Formula: $\\text{{Area of Trapezium}} = \\frac{{a + b}}{{2}} \\times h$)*"
    )

    area = round(((side_a + side_b) / 2.0) * height, 2)
    correct_ans = f"{_fmt(area)} m²"

    # Distractor: Forgot / 2
    dist_no_div = f"{_fmt(round((side_a + side_b) * height, 2))} m²"
    # Distractor: a * b * h
    dist_mult = f"{_fmt(round(side_a * side_b, 2))} m²"

    custom_opts = [
        correct_ans,
        dist_no_div,
        dist_mult,
        f"{_fmt(round(area + 6.0, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State the formula for area of a trapezium [1 mark]:\n"
        f"Area = ((a + b) ÷ 2) × height.\n\n"
        f"Step 2: Add parallel sides and average them [1 mark]:\n"
        f"Average width = ({side_a} + {side_b}) ÷ 2 = {side_a + side_b} ÷ 2 = {_fmt((side_a + side_b)/2)} m.\n\n"
        f"Step 3: Multiply by height [1 mark]:\n"
        f"Area = {_fmt((side_a + side_b)/2)} m × {height} m = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_7",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the two parallel sides, divide by 2, then multiply by the height.",
        tier_2=f"({side_a} + {side_b}) ÷ 2 = {(side_a + side_b)/2}. Multiply by {height}.",
        tier_3=f"Area = {correct_ans}.",
        r=r,
    )


def generate_subskill_8(r: random.Random) -> Dict[str, Any]:
    """Subskill 8: L-shaped composite room floor area (decomposition method)."""
    # L-shape: Rect A (L1 x W1) + Rect B (L2 x W2)
    l1 = r.randint(6, 10)
    w1 = r.randint(4, 6)
    l2 = r.randint(3, 5)
    w2 = r.randint(3, 4)

    # Outer bounding dimensions
    total_l = l1
    total_w = w1 + w2

    name = r.choice(SA_NAMES)

    prompt = (
        f"An open-plan living area is shaped like an **L-shape**.\n"
        f"The room can be partitioned into two simpler rectangles:\n"
        f"- **Section A (Lounge)**: **{l1} m** long by **{w1} m** wide.\n"
        f"- **Section B (Dining Area)**: **{l2} m** long by **{w2} m** wide.\n\n"
        f"Calculate the **total combined floor area** of the open-plan room."
    )

    area_a = l1 * w1
    area_b = l2 * w2
    total_area = area_a + area_b

    correct_ans = f"{_fmt(total_area)} m²"

    # Distractor: Multiplied outer bounding box
    dist_outer = f"{_fmt(total_l * total_w)} m²"
    # Distractor: Added all sides as perimeter
    dist_perim = f"{_fmt(2 * (total_l + total_w))} m²"

    custom_opts = [
        correct_ans,
        dist_outer,
        dist_perim,
        f"{_fmt(total_area + 8)} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area of Section A (Lounge) [1 mark]:\n"
        f"Area A = {l1} m × {w1} m = {_fmt(area_a)} m².\n\n"
        f"Step 2: Calculate the area of Section B (Dining Area) [1 mark]:\n"
        f"Area B = {l2} m × {w2} m = {_fmt(area_b)} m².\n\n"
        f"Step 3: Sum the areas of both sections [1 mark]:\n"
        f"Total Area = {_fmt(area_a)} m² + {_fmt(area_b)} m² = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_8",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the area of each rectangular section separately and add them together.",
        tier_2=f"Section A = {l1} × {w1} = {area_a} m². Section B = {l2} × {w2} = {area_b} m².",
        tier_3=f"Total area = {area_a} + {area_b} = {correct_ans}.",
        r=r,
    )


def generate_subskill_9(r: random.Random) -> Dict[str, Any]:
    """Subskill 9: Wall net area calculation with doors and windows deducted."""
    wall_length = r.randint(6, 12)
    wall_height = round(r.choice([2.7, 2.8, 3.0]), 1)
    
    door_w = 0.9
    door_h = 2.1
    num_windows = r.choice([1, 2])
    win_w = 1.5
    win_h = 1.2

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is preparing to paint an exterior feature wall measuring **{wall_length} m** long and **{_fmt(wall_height)} m** high.\n"
        f"The wall contains:\n"
        f"- One entrance door measuring **0,9 m** wide by **2,1 m** high.\n"
        f"- **{num_windows} window{'s' if num_windows > 1 else ''}**, each measuring **1,5 m** wide by **1,2 m** high.\n\n"
        f"Calculate the **net paintable wall surface area** after subtracting the door and window openings.\n"
        f"*(Round answer to 2 decimal places)*"
    )

    gross_wall_area = round(wall_length * wall_height, 2)
    door_area = round(door_w * door_h, 2)
    window_area = round(num_windows * (win_w * win_h), 2)
    deductions = round(door_area + window_area, 2)
    net_area = round(gross_wall_area - deductions, 2)

    correct_ans = f"{_fmt(net_area)} m²"

    # Distractor 1: Gross wall area without deductions
    dist_gross = f"{_fmt(gross_wall_area)} m²"
    # Distractor 2: Deducted only door
    dist_door_only = f"{_fmt(round(gross_wall_area - door_area, 2))} m²"

    custom_opts = [
        correct_ans,
        dist_gross,
        dist_door_only,
        f"{_fmt(round(net_area + 3.5, 2))} m²",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate gross wall area [1 mark]:\n"
        f"Gross Area = {wall_length} m × {_fmt(wall_height)} m = {_fmt(gross_wall_area)} m².\n\n"
        f"Step 2: Calculate total area of openings to deduct [1 mark]:\n"
        f"- Door: 0,9 m × 2,1 m = {_fmt(door_area)} m².\n"
        f"- {num_windows} window{'s' if num_windows > 1 else ''}: {num_windows} × (1,5 m × 1,2 m) = {_fmt(window_area)} m².\n"
        f"Total Deductions = {_fmt(door_area)} + {_fmt(window_area)} = {_fmt(deductions)} m².\n\n"
        f"Step 3: Subtract openings from gross area [1 mark]:\n"
        f"Net Area = {_fmt(gross_wall_area)} m² - {_fmt(deductions)} m² = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_9",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the total wall area, calculate the area of the door and windows, then subtract the openings.",
        tier_2=f"Gross = {wall_length} × {wall_height} = {gross_wall_area} m². Deductions = {door_area} + {window_area} = {deductions} m².",
        tier_3=f"Net paintable area = {gross_wall_area} - {deductions} = {correct_ans}.",
        r=r,
    )
