"""Cluster 1: Perimeter of Polygons & Basic Shapes (Subskills 1 to 9)."""
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
# Subskill 1: Square Perimeter
# --------------------------------------------------------------------------- #
def _gen_perim_square_formula_and_perimeter(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_square_formula_and_perimeter"
    name = r.choice(SA_NAMES)
    side = r.choice([4, 5, 6, 7, 8, 9, 12, 15, 18, 24, 35])
    context = r.choice(["square vegetable patch", "square paving slab", "square patio", "square courtyard"])
    perimeter = 4 * side
    correct_ans = f"{perimeter} m"

    prompt = (
        f"{name} is planning to place a decorative timber border around a {context} with side length {side} m.\n\n"
        f"Calculate the total perimeter of the square {context}.\n\n"
        f"**Formula**: Perimeter of a square = $4 \\times \\text{{side}}$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A square has 4 equal sides. The perimeter is the total distance around the outer boundary.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Perimeter}} = 4 \\times s$$\n"
        f"$$\\text{{Perimeter}} = 4 \\times {side}\\text{{ m}}$$ ✓ [1 Mark: Method – substituting side into square perimeter formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Perimeter}} = {perimeter}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – correct evaluation with unit]"
    )

    d1 = f"{side * 2} m"
    d2 = f"{side * side} m"
    d3 = f"{perimeter + 4} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Recall that a square has 4 equal sides.",
        tier_2=f"Multiply the side length {side} m by 4.",
        tier_3=f"4 × {side} = {perimeter} m.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 2: Rectangle Perimeter
# --------------------------------------------------------------------------- #
def _gen_perim_rectangle_formula_and_perimeter(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_rectangle_formula_and_perimeter"
    name = r.choice(SA_NAMES)
    length = r.choice([8, 10, 12, 14, 15, 16, 20, 25])
    width = r.choice([3, 4, 5, 6, 7, 8, 9])
    context = r.choice(["classroom floor", "sports field", "vegetable garden", "living room"])
    perimeter = 2 * (length + width)
    correct_ans = f"{perimeter} m"

    prompt = (
        f"{name} measures a rectangular {context}. The length is {length} m and the width is {width} m.\n\n"
        f"Calculate the perimeter of the {context}.\n\n"
        f"**Formula**: $\\text{{Perimeter}} = 2(l + w)$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A rectangle has two pairs of equal opposing sides. The boundary distance is the sum of both lengths and both widths.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Perimeter}} = 2 \\times (\\text{{length}} + \\text{{width}})$$\n"
        f"$$\\text{{Perimeter}} = 2 \\times ({length} + {width}) = 2 \\times {length + width}$$ ✓ [1 Mark: Method – correct formula substitution]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Perimeter}} = {perimeter}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – correct final perimeter]"
    )

    d1 = f"{length * width} m"
    d2 = f"{length + width} m"
    d3 = f"{2 * length + width} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the length and width together first.",
        tier_2=f"Double the sum: 2 × ({length} + {width}).",
        tier_3=f"2 × {length + width} = {perimeter} m.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 3: Triangle Perimeter (3 Sides)
# --------------------------------------------------------------------------- #
def _gen_perim_triangle_three_sides(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_triangle_three_sides"
    name = r.choice(SA_NAMES)
    a = r.choice([5, 6, 7, 8, 9, 11])
    b = r.choice([10, 12, 13, 14, 15])
    c = r.choice([8, 10, 12, 14, 16])
    perimeter = a + b + c
    correct_ans = f"{perimeter} m"

    prompt = (
        f"{name} is installing garden edging along the perimeter of a triangular flower bed.\n"
        f"The three side lengths are {a} m, {b} m, and {c} m.\n\n"
        f"Calculate the total perimeter of the triangular flower bed."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The perimeter of any triangle is the total sum of its three exterior boundary sides: $P = a + b + c$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Perimeter}} = {a} + {b} + {c}$$ ✓ [1 Mark: Method – summing all three boundary lengths]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Perimeter}} = {perimeter}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – accurate addition with units]"
    )

    d1 = f"{a + b} m"
    d2 = f"{perimeter - 2} m"
    d3 = f"{perimeter + 3} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Perimeter is the distance all the way around the outside of the shape.",
        tier_2=f"Add the three sides together: {a} + {b} + {c}.",
        tier_3=f"{a} + {b} + {c} = {perimeter} m.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 4: Equilateral & Isosceles Triangle
# --------------------------------------------------------------------------- #
def _gen_perim_equilateral_and_isosceles_triangle(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_equilateral_and_isosceles_triangle"
    name = r.choice(SA_NAMES)
    is_equilateral = r.choice([True, False])

    if is_equilateral:
        side = r.choice([6, 7, 8, 9, 12, 14, 15])
        perimeter = 3 * side
        correct_ans = f"{perimeter} m"
        prompt = (
            f"{name} is building an equilateral triangular herb garden. Each side measures {side} m.\n\n"
            f"Calculate the total perimeter of the garden."
        )
        explanation = (
            f"**Step 1: Conceptual Reasoning & Identification**\n"
            f"An equilateral triangle has 3 sides of equal length. Perimeter = $3 \\times \\text{{side}}$.\n\n"
            f"**Step 2: Technical Method & Working Setup**\n"
            f"$$\\text{{Perimeter}} = 3 \\times {side}\\text{{ m}}$$ ✓ [1 Mark: Method – multiplying equal side by 3]\n\n"
            f"**Step 3: Final Calculation & Answer**\n"
            f"$$\\text{{Perimeter}} = {perimeter}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – accurate product]"
        )
    else:
        equal_side = r.choice([8, 10, 12, 15, 16])
        base = r.choice([5, 6, 7, 9, 11])
        perimeter = 2 * equal_side + base
        correct_ans = f"{perimeter} m"
        prompt = (
            f"{name} designs an isosceles triangular patio where the two equal sides each measure {equal_side} m and the base measures {base} m.\n\n"
            f"Calculate the total perimeter of the patio."
        )
        explanation = (
            f"**Step 1: Conceptual Reasoning & Identification**\n"
            f"An isosceles triangle has two equal sides and one base side. Perimeter = $2 \\times \\text{{equal side}} + \\text{{base}}$.\n\n"
            f"**Step 2: Technical Method & Working Setup**\n"
            f"$$\\text{{Perimeter}} = (2 \\times {equal_side}) + {base} = {2 * equal_side} + {base}$$ ✓ [1 Mark: Method – accounting for both equal sides and base]\n\n"
            f"**Step 3: Final Calculation & Answer**\n"
            f"$$\\text{{Perimeter}} = {perimeter}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – correct final sum]"
        )

    d1 = f"{perimeter - 3} m"
    d2 = f"{perimeter + 4} m"
    d3 = f"{perimeter * 2} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Identify how many equal sides the triangle has.",
        tier_2="Sum all 3 exterior sides.",
        tier_3=f"The correct perimeter is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 5: Right-Angled Triangle Perimeter via Pythagoras
# --------------------------------------------------------------------------- #
def _gen_perim_right_angled_triangle_pythagoras(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_right_angled_triangle_pythagoras"
    name = r.choice(SA_NAMES)
    triples = [
        (3, 4, 5),
        (6, 8, 10),
        (5, 12, 13),
        (9, 12, 15),
        (8, 15, 17),
        (12, 16, 20),
    ]
    a, b, c = r.choice(triples)
    perimeter = a + b + c
    correct_ans = f"{perimeter} m"

    prompt = (
        f"{name} is installing fencing around a right-angled triangular plot of land.\n"
        f"The two perpendicular sides are {a} m and {b} m long. The hypotenuse is not marked.\n\n"
        f"Calculate the total perimeter of the plot.\n\n"
        f"**Formulas**: $c^2 = a^2 + b^2$ and $\\text{{Perimeter}} = a + b + c$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To find the perimeter, all three sides must be known. Use the Theorem of Pythagoras to calculate the hypotenuse first.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$c = \\sqrt{{{a}^2 + {b}^2}} = \\sqrt{{{a*a} + {b*b}}} = \\sqrt{{{c*c}}} = {c}\\text{{ m}}$$\n"
        f"$$\\text{{Perimeter}} = {a} + {b} + {c}$$ ✓ [1 Mark: Method – applying Pythagoras and summing 3 sides]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Perimeter}} = {perimeter}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – accurate perimeter]"
    )

    d1 = f"{a + b} m"
    d2 = f"{perimeter + 2} m"
    d3 = f"{c * 2} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="First find the hypotenuse using Pythagoras: c² = a² + b².",
        tier_2=f"c = √({a}² + {b}²) = {c} m.",
        tier_3=f"Perimeter = {a} + {b} + {c} = {perimeter} m.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 6: Circumference from Radius
# --------------------------------------------------------------------------- #
def _gen_perim_circle_circumference_from_radius(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_circle_circumference_from_radius"
    name = r.choice(SA_NAMES)
    radius = r.choice([2, 3, 4, 5, 6, 7, 8, 10, 14])
    pi_val = 3.142
    circ = round(2 * pi_val * radius, 2)
    correct_ans = f"{_fmt(circ)} m"

    prompt = (
        f"{name} is installing a decorative brick ring around a circular tree bed with radius $r = {radius}$ m.\n\n"
        f"Calculate the circumference of the circular bed. Use $\\pi = 3,142$ and round your answer to 2 decimal places.\n\n"
        f"**Formula**: $\\text{{Circumference}} = 2 \\times \\pi \\times r$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Circumference is the perimeter of a circle. The radius $r$ is the distance from the centre to the edge.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Circumference}} = 2 \\times \\pi \\times r$$\n"
        f"$$\\text{{Circumference}} = 2 \\times 3,142 \\times {radius} = {_fmt(2 * radius)} \\times 3,142$$ ✓ [1 Mark: Method – substituting radius and π into formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Circumference}} = {_fmt(circ)}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – accurate product rounded to 2 d.p.]"
    )

    d1 = f"{_fmt(round(pi_val * radius, 2))} m"
    d2 = f"{_fmt(round(pi_val * radius * radius, 2))} m"
    d3 = f"{_fmt(round(circ + 3.14, 2))} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Use the formula C = 2 × π × r.",
        tier_2=f"Multiply 2 × 3,142 × {radius}.",
        tier_3=f"2 × 3,142 × {radius} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 7: Circumference from Diameter
# --------------------------------------------------------------------------- #
def _gen_perim_circle_circumference_from_diameter(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_circle_circumference_from_diameter"
    name = r.choice(SA_NAMES)
    diameter = r.choice([3, 4, 5, 6, 8, 10, 12, 14, 16, 20])
    pi_val = 3.142
    circ = round(pi_val * diameter, 2)
    correct_ans = f"{_fmt(circ)} m"

    prompt = (
        f"{name} is buying edging for a circular fish pond with a diameter of $d = {diameter}$ m.\n\n"
        f"Calculate the circumference of the pond using $\\pi = 3,142$. Round to 2 decimal places.\n\n"
        f"**Formula**: $\\text{{Circumference}} = \\pi \\times d$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The diameter $d$ passes through the centre from edge to edge. The circumference formula using diameter is $C = \\pi \\times d$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Circumference}} = 3,142 \\times {diameter}$$ ✓ [1 Mark: Method – substituting diameter into C = πd]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Circumference}} = {_fmt(circ)}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – correct calculation with unit]"
    )

    d1 = f"{_fmt(round(circ * 2, 2))} m"
    d2 = f"{_fmt(round(circ / 2, 2))} m"
    d3 = f"{_fmt(round(pi_val * (diameter / 2)**2, 2))} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="When diameter is given, Circumference = π × d.",
        tier_2=f"Multiply 3,142 by {diameter}.",
        tier_3=f"3,142 × {diameter} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 8: Closed Semicircle Perimeter
# --------------------------------------------------------------------------- #
def _gen_perim_semicircle_total_perimeter(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_semicircle_total_perimeter"
    name = r.choice(SA_NAMES)
    radius = r.choice([3, 4, 5, 6, 7, 8, 10])
    pi_val = 3.142
    curved = round(pi_val * radius, 2)
    diameter = 2 * radius
    total_p = round(curved + diameter, 2)
    correct_ans = f"{_fmt(total_p)} m"

    prompt = (
        f"{name} is installing a border around a semicircular flower bed that has a radius of $r = {radius}$ m.\n"
        f"The border goes all the way around, including both the curved boundary and the straight diameter baseline.\n\n"
        f"Calculate the total perimeter of the closed semicircle. (Use $\\pi = 3,142$, round to 2 decimal places).\n\n"
        f"**Formula**: $\\text{{Perimeter}} = (\\pi \\times r) + 2r$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A closed semicircle consists of two parts: half the circumference (the curved arc = $\\pi r$) plus the straight diameter base ($2r$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Curved arc}} = \\pi \\times r = 3,142 \\times {radius} = {_fmt(curved)}\\text{{ m}}$$\n"
        f"$$\\text{{Straight base}} = 2 \\times {radius} = {diameter}\\text{{ m}}$$\n"
        f"$$\\text{{Total Perimeter}} = {_fmt(curved)} + {diameter}$$ ✓ [1 Mark: Method – adding curved arc and straight diameter]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Perimeter}} = {_fmt(total_p)}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – accurate sum with units]"
    )

    d1 = f"{_fmt(curved)} m"  # Common error: forgetting baseline
    d2 = f"{_fmt(round(2 * pi_val * radius, 2))} m"  # full circle
    d3 = f"{_fmt(round(total_p + 2, 2))} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember to include both the curved arc AND the straight baseline.",
        tier_2=f"Curved arc = 3,142 × {radius} = {_fmt(curved)} m. Straight base = 2 × {radius} = {diameter} m.",
        tier_3=f"Total perimeter = {_fmt(curved)} + {diameter} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 9: Closed Quarter Circle Perimeter
# --------------------------------------------------------------------------- #
def _gen_perim_quarter_circle_perimeter(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_quarter_circle_perimeter"
    name = r.choice(SA_NAMES)
    radius = r.choice([2, 4, 6, 8, 10])
    pi_val = 3.142
    arc = round(0.5 * pi_val * radius, 2)
    two_radii = 2 * radius
    total_p = round(arc + two_radii, 2)
    correct_ans = f"{_fmt(total_p)} m"

    prompt = (
        f"{name} is edging a corner flower bed shaped like a quarter-circle with radius $r = {radius}$ m.\n"
        f"The edging surrounds the entire shape: the curved arc and the two straight radial edges.\n\n"
        f"Calculate the total perimeter of the flower bed. (Use $\\pi = 3,142$, round to 2 decimal places).\n\n"
        f"**Formula**: $\\text{{Perimeter}} = \\left(\\frac{{1}}{{2}} \\times \\pi \\times r\\right) + 2r$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A closed quarter-circle boundary consists of one quarter of a full circle's circumference ($\\frac{{2\\pi r}}{{4}} = \\frac{{\\pi r}}{{2}}$) plus the two straight edges of length $r$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Curved arc}} = 0,5 \\times 3,142 \\times {radius} = {_fmt(arc)}\\text{{ m}}$$\n"
        f"$$\\text{{Two straight radii}} = {radius} + {radius} = {two_radii}\\text{{ m}}$$\n"
        f"$$\\text{{Total Perimeter}} = {_fmt(arc)} + {two_radii}$$ ✓ [1 Mark: Method – sum of arc and two straight radii]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Perimeter}} = {_fmt(total_p)}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – correct perimeter with units]"
    )

    d1 = f"{_fmt(arc)} m"
    d2 = f"{_fmt(round(arc + radius, 2))} m"
    d3 = f"{_fmt(round(pi_val * radius, 2))} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the curved arc and the two straight sides (radii).",
        tier_2=f"Arc = 0,5 × 3,142 × {radius} = {_fmt(arc)} m. Add 2 × {radius} = {two_radii} m.",
        tier_3=f"Perimeter = {_fmt(arc)} + {two_radii} = {correct_ans}.",
        r=r,
    )
