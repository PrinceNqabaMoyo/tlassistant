"""Cluster 3: Area of Polygons & Standard Shapes (Subskills 19 to 27)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)

# --------------------------------------------------------------------------- #
# Subskill 19: Square Area
# --------------------------------------------------------------------------- #
def _gen_area_square_formula_and_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_square_formula_and_calculation"
    name = r.choice(SA_NAMES)
    side = r.choice([4, 5, 6, 7, 8, 9, 11, 12, 15, 20])
    area = side * side
    correct_ans = f"{area} m²"

    prompt = (
        f"{name} is calculating the floor area of a square patio with side length {side} m.\n\n"
        f"Calculate the area of the patio in square metres (m²).\n\n"
        f"**Formula**: $\\text{{Area}} = \\text{{side}} \\times \\text{{side}} = s^2$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The area of a square represents the amount of 2D space enclosed, calculated by squaring the side length.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Area}} = s^2 = {side}^2 = {side} \\times {side}$$ ✓ [1 Mark: Method – squaring side length]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Area}} = {area}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate product with square units]"
    )

    d1 = f"{4 * side} m²"  # perimeter error
    d2 = f"{2 * side} m²"
    d3 = f"{area + side} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Area is the surface inside: multiply side by side.",
        tier_2=f"Calculate {side} × {side}.",
        tier_3=f"{side}² = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 20: Rectangle Area
# --------------------------------------------------------------------------- #
def _gen_area_rectangle_formula_and_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_rectangle_formula_and_calculation"
    name = r.choice(SA_NAMES)
    length = r.choice([7, 8, 9, 10, 12, 14, 15, 18, 20])
    width = r.choice([3, 4, 5, 6, 7, 8])
    area = length * width
    correct_ans = f"{area} m²"

    prompt = (
        f"{name} is measuring the floor area of a rectangular classroom that is {length} m long and {width} m wide.\n\n"
        f"Calculate the total area of the classroom floor in m².\n\n"
        f"**Formula**: $\\text{{Area}} = \\text{{length}} \\times \\text{{width}}$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The area of a rectangle is the product of its length and width.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Area}} = l \\times w = {length} \\times {width}$$ ✓ [1 Mark: Method – substituting length and width into area formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Area}} = {area}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – correct evaluation with unit m²]"
    )

    d1 = f"{2 * (length + width)} m²"  # perimeter error
    d2 = f"{length + width} m²"
    d3 = f"{area - width} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Area of a rectangle = length × width.",
        tier_2=f"Multiply {length} by {width}.",
        tier_3=f"{length} × {width} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 21: Triangle Area (Base and Height)
# --------------------------------------------------------------------------- #
def _gen_area_triangle_base_and_height(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_triangle_base_and_height"
    name = r.choice(SA_NAMES)
    base = r.choice([6, 8, 10, 12, 14, 16, 18])
    height = r.choice([4, 5, 6, 7, 8, 9, 10])
    slant = r.choice([height + 2, height + 3])
    area = round(0.5 * base * height, 1)
    correct_ans = f"{_fmt(area)} m²"

    prompt = (
        f"{name} is planting lawn on a triangular garden plot.\n"
        f"The base of the triangle is {base} m, the perpendicular height is {height} m, and the slant side is {slant} m.\n\n"
        f"Calculate the area of the triangular garden.\n\n"
        f"**Formula**: $\\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The area of a triangle uses the perpendicular height (height at 90° to the base), NOT the slant side.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}$$\n"
        f"$$\\text{{Area}} = \\frac{{1}}{{2}} \\times {base} \\times {height} = {_fmt(0.5 * base)} \\times {height}$$ ✓ [1 Mark: Method – selecting perpendicular height and substituting into formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Area}} = {_fmt(area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – correct product with units]"
    )

    d1 = f"{_fmt(base * height)} m²"  # forgot 1/2
    d2 = f"{_fmt(round(0.5 * base * slant, 1))} m²"  # used slant side
    d3 = f"{_fmt(base + height + slant)} m²"  # perimeter
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Always use the perpendicular height, not the slant side.",
        tier_2=f"Area = 0,5 × base × height = 0,5 × {base} × {height}.",
        tier_3=f"Area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 22: Right-Angled Triangle Area
# --------------------------------------------------------------------------- #
def _gen_area_right_angled_triangle(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_right_angled_triangle"
    name = r.choice(SA_NAMES)
    base = r.choice([4, 6, 8, 10, 12])
    height = r.choice([3, 5, 7, 9, 11])
    hypot = round(math.sqrt(base**2 + height**2), 1)
    area = round(0.5 * base * height, 1)
    correct_ans = f"{_fmt(area)} m²"

    prompt = (
        f"{name} is tiling a right-angled triangular hearth.\n"
        f"The two perpendicular sides measuring {base} m and {height} m meet at a 90° angle. The hypotenuse is {_fmt(hypot)} m.\n\n"
        f"Calculate the area of the hearth.\n\n"
        f"**Formula**: $\\text{{Area}} = \\frac{{1}}{{2}} \\times b \\times h$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In a right-angled triangle, the two perpendicular legs act directly as base and perpendicular height.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Area}} = \\frac{{1}}{{2}} \\times {base} \\times {height} = {_fmt(0.5 * base)} \\times {height}$$ ✓ [1 Mark: Method – identifying perpendicular legs]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Area}} = {_fmt(area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate product]"
    )

    d1 = f"{base * height} m²"
    d2 = f"{_fmt(round(0.5 * base * hypot, 1))} m²"
    d3 = f"{_fmt(round(base + height + hypot, 1))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The two sides meeting at 90° are the base and perpendicular height.",
        tier_2=f"Calculate 0,5 × {base} × {height}.",
        tier_3=f"Area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 23: Circle Area from Radius
# --------------------------------------------------------------------------- #
def _gen_area_circle_from_radius(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_circle_from_radius"
    name = r.choice(SA_NAMES)
    radius = r.choice([2, 3, 4, 5, 6, 7, 8, 10])
    pi_val = 3.142
    area = round(pi_val * (radius ** 2), 2)
    correct_ans = f"{_fmt(area)} m²"

    prompt = (
        f"{name} is paving a circular entertainment patio that has a radius of $r = {radius}$ m.\n\n"
        f"Calculate the area of the circular patio. (Use $\\pi = 3,142$ and round to 2 decimal places).\n\n"
        f"**Formula**: $\\text{{Area}} = \\pi \\times r^2$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The area of a circle requires squaring the radius first ($r^2$), then multiplying by $\\pi$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$r^2 = {radius}^2 = {radius * radius}$$\n"
        f"$$\\text{{Area}} = 3,142 \\times {radius * radius}$$ ✓ [1 Mark: Method – squaring radius and multiplying by π]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Area}} = {_fmt(area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate product rounded to 2 d.p.]"
    )

    d1 = f"{_fmt(round(2 * pi_val * radius, 2))} m²"  # circumference error
    d2 = f"{_fmt(round(pi_val * 2 * radius, 2))} m²"  # multiplied by 2 instead of squaring
    d3 = f"{_fmt(round(area + 5, 2))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Area = π × r². Remember to square the radius first.",
        tier_2=f"Calculate {radius}² = {radius * radius}, then multiply by 3,142.",
        tier_3=f"3,142 × {radius * radius} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 24: Circle Area from Diameter
# --------------------------------------------------------------------------- #
def _gen_area_circle_from_diameter(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_circle_from_diameter"
    name = r.choice(SA_NAMES)
    diameter = r.choice([4, 6, 8, 10, 12, 14, 16, 20])
    radius = diameter / 2
    pi_val = 3.142
    area = round(pi_val * (radius ** 2), 2)
    correct_ans = f"{_fmt(area)} m²"

    prompt = (
        f"{name} is buying a safety net for a circular swimming pool with a diameter of $d = {diameter}$ m.\n\n"
        f"Calculate the water surface area of the pool. (Use $\\pi = 3,142$ and round to 2 decimal places).\n\n"
        f"**Formula**: $\\text{{Area}} = \\pi \\times r^2$ where $r = \\frac{{d}}{{2}}$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The formula for area uses the radius, NOT the diameter. Divide diameter by 2 first: $r = \\frac{{{diameter}}}{{2}} = {_fmt(radius)}\\text{{ m}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$r = \\frac{{{diameter}}}{{2}} = {_fmt(radius)}\\text{{ m}}$$\n"
        f"$$\\text{{Area}} = 3,142 \\times ({_fmt(radius)})^2 = 3,142 \\times {_fmt(radius * radius)}$$ ✓ [1 Mark: Method – dividing diameter by 2 and squaring radius]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Area}} = {_fmt(area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate product rounded to 2 d.p.]"
    )

    d1 = f"{_fmt(round(pi_val * (diameter ** 2), 2))} m²"  # squared diameter without dividing
    d2 = f"{_fmt(round(pi_val * diameter, 2))} m²"
    d3 = f"{_fmt(round(area / 2, 2))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="First divide the diameter by 2 to get the radius: r = d ÷ 2.",
        tier_2=f"r = {diameter} ÷ 2 = {_fmt(radius)} m. Area = 3,142 × ({_fmt(radius)})².",
        tier_3=f"Area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 25: Semicircle Area
# --------------------------------------------------------------------------- #
def _gen_area_semicircle_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_semicircle_calculation"
    name = r.choice(SA_NAMES)
    radius = r.choice([3, 4, 5, 6, 7, 8, 10])
    pi_val = 3.142
    full_area = pi_val * (radius ** 2)
    semi_area = round(full_area / 2, 2)
    correct_ans = f"{_fmt(semi_area)} m²"

    prompt = (
        f"{name} is paving a semicircular flower bed that has a radius of $r = {radius}$ m.\n\n"
        f"Calculate the area of the semicircular flower bed. (Use $\\pi = 3,142$ and round to 2 decimal places).\n\n"
        f"**Formula**: $\\text{{Area of semicircle}} = \\frac{{1}}{{2}} \\times \\pi \\times r^2$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A semicircle is exactly half of a full circle. Calculate the full circular area and divide by 2.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Full circle area}} = 3,142 \\times {radius}^2 = 3,142 \\times {radius * radius} = {_fmt(round(full_area, 2))}\\text{{ m}}^2$$\n"
        f"$$\\text{{Semicircle area}} = \\frac{{{_fmt(round(full_area, 2))}}}{{2}}$$ ✓ [1 Mark: Method – dividing full circle area by 2]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Semicircle area}} = {_fmt(semi_area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate division to 2 d.p.]"
    )

    d1 = f"{_fmt(round(full_area, 2))} m²"  # forgot to divide by 2
    d2 = f"{_fmt(round(pi_val * radius, 2))} m²"
    d3 = f"{_fmt(round(semi_area / 2, 2))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the full circle area πr² and divide by 2.",
        tier_2=f"Calculate (3,142 × {radius * radius}) ÷ 2.",
        tier_3=f"Semicircle area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 26: Quarter Circle Area
# --------------------------------------------------------------------------- #
def _gen_area_quarter_circle_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_quarter_circle_calculation"
    name = r.choice(SA_NAMES)
    radius = r.choice([2, 4, 6, 8, 10])
    pi_val = 3.142
    full_area = pi_val * (radius ** 2)
    quarter_area = round(full_area / 4, 2)
    correct_ans = f"{_fmt(quarter_area)} m²"

    prompt = (
        f"{name} is planting lawn on a quarter-circle section of a park with radius $r = {radius}$ m.\n\n"
        f"Calculate the area of the quarter-circle. (Use $\\pi = 3,142$, round to 2 decimal places).\n\n"
        f"**Formula**: $\\text{{Area}} = \\frac{{1}}{{4}} \\times \\pi \\times r^2$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A quarter-circle is one fourth of a full circle. Calculate the full circular area and divide by 4.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Full circle area}} = 3,142 \\times {radius}^2 = 3,142 \\times {radius * radius} = {_fmt(round(full_area, 2))}\\text{{ m}}^2$$\n"
        f"$$\\text{{Quarter circle area}} = \\frac{{{_fmt(round(full_area, 2))}}}{{4}}$$ ✓ [1 Mark: Method – dividing full circle area by 4]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Quarter circle area}} = {_fmt(quarter_area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate quotient]"
    )

    d1 = f"{_fmt(round(full_area, 2))} m²"
    d2 = f"{_fmt(round(full_area / 2, 2))} m²"  # semicircle
    d3 = f"{_fmt(round(quarter_area * 1.5, 2))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate full area πr² and divide by 4.",
        tier_2=f"Calculate (3,142 × {radius * radius}) ÷ 4.",
        tier_3=f"Area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 27: Trapezium Area
# --------------------------------------------------------------------------- #
def _gen_area_trapezium_parallel_sides(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_trapezium_parallel_sides"
    name = r.choice(SA_NAMES)
    a = r.choice([6, 8, 10, 12])
    b = r.choice([14, 16, 18, 20])
    h = r.choice([4, 5, 6, 8])
    area = round(0.5 * (a + b) * h, 1)
    correct_ans = f"{_fmt(area)} m²"

    prompt = (
        f"{name} is calculating the area of a trapezoidal plot of land.\n"
        f"The two parallel boundary sides measure $a = {a}$ m and $b = {b}$ m, and the perpendicular distance between them is $h = {h}$ m.\n\n"
        f"Calculate the area of the trapezoidal plot.\n\n"
        f"**Formula**: $\\text{{Area}} = \\frac{{1}}{{2}}(a + b) \\times h$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A trapezium has two parallel sides. The area is the average of the two parallel sides multiplied by the perpendicular height.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Sum of parallel sides}} = {a} + {b} = {a + b}\\text{{ m}}$$\n"
        f"$$\\text{{Area}} = \\frac{{1}}{{2}} \\times {a + b} \\times {h} = {_fmt(0.5 * (a + b))} \\times {h}$$ ✓ [1 Mark: Method – substituting parallel sides and height into trapezium formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Area}} = {_fmt(area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate product]"
    )

    d1 = f"{_fmt((a + b) * h)} m²"  # forgot 1/2
    d2 = f"{_fmt(a * h)} m²"
    d3 = f"{_fmt(b * h)} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the two parallel sides first: (a + b).",
        tier_2=f"Multiply 0,5 × ({a} + {b}) × {h}.",
        tier_3=f"Area = {correct_ans}.",
        r=r,
    )
