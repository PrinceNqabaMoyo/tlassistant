"""Grade 7 Mathematics - Perimeter and Area of 2D Shapes: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 4/01. Perimeter and area of 2D shapes.md & Syllabus.md
Focus: Perimeter of squares, rectangles, triangles, regular/irregular polygons; circumference of circles; fencing/track word problems; area of squares, rectangles, and triangles (right, acute, obtuse).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_rectangle_dim(l: int, b: int, unit: str = "cm") -> str:
    """Renders a clean static 2D SVG rectangle with dimension labels."""
    w, h = 300, 180
    rw, rh = 180, 100
    rx, ry = 60, 40
    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
        f'<text x="{rx + rw // 2}" y="{ry - 8}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0369a1">{l} {unit}</text>'
        f'<text x="{rx + rw + 8}" y="{ry + rh // 2 + 4}" font-size="11" font-weight="bold" fill="#0369a1">{b} {unit}</text>'
        f'</svg>'
    )


def _svg_triangle_height(base: int, height: int, unit: str = "cm") -> str:
    """Renders a clean static 2D SVG acute triangle with interior perpendicular height."""
    w, h = 300, 180
    p1 = (50, 140)
    p2 = (230, 140)
    p3 = (130, 40)
    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'<polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]}" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<line x1="{p3[0]}" y1="{p3[1]}" x2="{p3[0]}" y2="{p1[1]}" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,3"/>'
        f'<rect x="{p3[0]}" y="{p1[1] - 10}" width="10" height="10" fill="none" stroke="#ef4444" stroke-width="1"/>'
        f'<text x="140" y="160" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">b = {base} {unit}</text>'
        f'<text x="{p3[0] + 6}" y="95" font-size="11" font-weight="bold" fill="#dc2626">h = {height} {unit}</text>'
        f'</svg>'
    )


# 01. Perimeter of square formula
def arch_01_perimeter_of_square_formula(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(5, 25)
    perim = 4 * s
    ans = f"{perim} cm"
    prompt = (
        f"A square has a side length of ${s}\\text{{ cm}}$.\n\n"
        f"1. State the formula for the perimeter of a square.\n"
        f"2. Calculate the perimeter of the square."
    )
    sol = (
        f"**Step 1: Perimeter Formula:**\n"
        f"$$\\text{{Perimeter}} = 4s$$\n\n"
        f"**Step 2: Calculate:**\n"
        f"$$\\text{{Perimeter}} = 4 \\times {s} = {perim}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_pa_01_{rng.randint(100000, 999999)}",
        "subskill": "01_perimeter_of_square_formula",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"P = 4s = 4 × {s} = {perim} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_01",
        "hints": {
            "tier_1": "All four sides of a square are equal.",
            "tier_2": f"Multiply {s} by 4.",
            "tier_3": f"Perimeter = {perim} cm."
        },
        "misconception_tags": ["squaring_side_for_perimeter"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States formula P = 4s", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates perimeter = {perim} cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 02. Perimeter of square find side from perimeter
def arch_02_perimeter_of_square_find_side_from_perimeter(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(6, 30)
    perim = 4 * s
    ans = f"{s} m"
    prompt = (
        f"A square garden has a total perimeter of ${perim}\\text{{ m}}$.\n\n"
        f"Calculate the length of one side of the square garden."
    )
    sol = (
        f"**Step 1: Formula:**\n"
        f"$$P = 4s \\implies s = \\frac{{P}}{{4}}$$\n\n"
        f"**Step 2: Solve for $s$:**\n"
        f"$$s = \\frac{{{perim}}}{{4}} = {s}\\text{{ m}}$$"
    )
    return {
        "id": f"g7_pa_02_{rng.randint(100000, 999999)}",
        "subskill": "02_perimeter_of_square_find_side_from_perimeter",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{s} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_02",
        "hints": {
            "tier_1": "Divide the perimeter by 4 to get one side.",
            "tier_2": f"{perim} ÷ 4 = {s}.",
            "tier_3": f"Side length = {s} m."
        },
        "misconception_tags": ["dividing_by_2_instead_of_4_for_square"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Sets up s = {perim} / 4", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates side = {s} m", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 03. Perimeter of rectangle standard
def arch_03_perimeter_of_rectangle_standard(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(12, 28)
    b = rng.randint(5, l - 3)
    p = 2 * (l + b)
    svg = _svg_rectangle_dim(l, b, "cm")
    ans = f"{p} cm"
    prompt = (
        f"Inspect the rectangle in the diagram with length ${l}\\text{{ cm}}$ and breadth ${b}\\text{{ cm}}$:\n\n"
        f"1. State the formula for the perimeter of a rectangle.\n"
        f"2. Calculate the perimeter of the rectangle."
    )
    sol = (
        f"**Step 1: Perimeter Formula:**\n"
        f"$$P = 2(l + b) \\quad \\text{{or}} \\quad P = 2l + 2b$$\n\n"
        f"**Step 2: Calculate:**\n"
        f"$$P = 2({l} + {b}) = 2({l + b}) = {p}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_pa_03_{rng.randint(100000, 999999)}",
        "subskill": "03_perimeter_of_rectangle_standard",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"P = 2({l} + {b}) = {p} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_03",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Add length and breadth, then double the result.",
            "tier_2": f"2 × ({l} + {b}) = 2 × {l + b} = {p}.",
            "tier_3": f"Perimeter = {p} cm."
        },
        "misconception_tags": ["adding_length_and_breadth_only_once"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States formula P = 2(l + b)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates perimeter = {p} cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 04. Perimeter of rectangle find breadth from perimeter
def arch_04_perimeter_of_rectangle_find_breadth_from_perimeter(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(15, 30)
    b = rng.randint(4, 12)
    perim = 2 * (l + b)
    ans = f"{b} m"
    prompt = (
        f"A rectangular soccer field has a perimeter of ${perim}\\text{{ m}}$ and a length of ${l}\\text{{ m}}$.\n\n"
        f"Calculate the **breadth** of the soccer field."
    )
    sol = (
        f"**Step 1: Use perimeter formula:**\n"
        f"$$P = 2(l + b) \\implies \\frac{{P}}{{2}} = l + b$$\n\n"
        f"**Step 2: Half of the perimeter:**\n"
        f"$$\\frac{{{perim}}}{{2}} = {perim // 2}\\text{{ m}}$$\n\n"
        f"**Step 3: Subtract length $l$ to solve for $b$:**\n"
        f"$$b = {perim // 2} - {l} = {b}\\text{{ m}}$$"
    )
    return {
        "id": f"g7_pa_04_{rng.randint(100000, 999999)}",
        "subskill": "04_perimeter_of_rectangle_find_breadth_from_perimeter",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{b} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pa_04",
        "hints": {
            "tier_1": f"Divide perimeter {perim} by 2 to find length + breadth.",
            "tier_2": f"{perim} ÷ 2 = {perim // 2}. Now subtract {l}.",
            "tier_3": f"Breadth = {b} m."
        },
        "misconception_tags": ["subtracting_length_directly_from_perimeter"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Uses P / 2 = l + b", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates l + b = {perim // 2}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculates breadth = {b} m", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


# 05. Perimeter of rectangle find length from perimeter
def arch_05_perimeter_of_rectangle_find_length_from_perimeter(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(18, 35)
    b = rng.randint(6, 14)
    perim = 2 * (l + b)
    ans = f"{l} mm"
    prompt = (
        f"A rectangular metal plate has a perimeter of ${perim}\\text{{ mm}}$ and a breadth of ${b}\\text{{ mm}}$.\n\n"
        f"Calculate the **length** of the plate."
    )
    sol = (
        f"**Step 1:** Half perimeter: $\\frac{{{perim}}}{{2}} = {perim // 2}\\text{{ mm}}$.\n\n"
        f"**Step 2:** Length $l = {perim // 2} - {b} = {l}\\text{{ mm}}$."
    )
    return {
        "id": f"g7_pa_05_{rng.randint(100000, 999999)}",
        "subskill": "05_perimeter_of_rectangle_find_length_from_perimeter",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{l} mm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_05",
        "hints": {
            "tier_1": f"Divide {perim} by 2, then subtract {b}.",
            "tier_2": f"{perim // 2} - {b} = {l}.",
            "tier_3": f"Length = {l} mm."
        },
        "misconception_tags": ["subtracting_breadth_directly_from_perimeter"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Divides {perim} by 2 to get {perim // 2}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates length = {l} mm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 06. Perimeter of equilateral triangle
def arch_06_perimeter_of_equilateral_triangle(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(6, 24)
    perim = 3 * s
    ans = f"{perim} cm"
    prompt = (
        f"An equilateral triangle has sides of length ${s}\\text{{ cm}}$.\n\n"
        f"Calculate the perimeter of this equilateral triangle."
    )
    sol = (
        f"**Perimeter Calculation:**\n"
        f"All three sides of an equilateral triangle are equal in length:\n"
        f"$$P = 3s = 3 \\times {s} = {perim}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_pa_06_{rng.randint(100000, 999999)}",
        "subskill": "06_perimeter_of_equilateral_triangle",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{perim} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_06",
        "hints": {
            "tier_1": "Multiply the side length by 3.",
            "tier_2": f"3 × {s} = {perim}.",
            "tier_3": f"Perimeter = {perim} cm."
        },
        "misconception_tags": ["confusing_triangle_perimeter_with_square"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Uses P = 3s", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates perimeter = {perim} cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 07. Perimeter of isosceles triangle
def arch_07_perimeter_of_isosceles_triangle(rng: random.Random) -> Dict[str, Any]:
    legs = rng.randint(8, 20)
    base = rng.randint(5, legs + 4)
    perim = 2 * legs + base
    ans = f"{perim} cm"
    prompt = (
        f"An isosceles triangle has two equal sides of length ${legs}\\text{{ cm}}$ and a base of length ${base}\\text{{ cm}}$.\n\n"
        f"Calculate the perimeter of the triangle."
    )
    sol = (
        f"**Calculation:**\n"
        f"$$P = 2(\\text{{equal side}}) + \\text{{base}}$$\n"
        f"$$P = 2({legs}) + {base} = {2 * legs} + {base} = {perim}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_pa_07_{rng.randint(100000, 999999)}",
        "subskill": "07_perimeter_of_isosceles_triangle",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{perim} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_07",
        "hints": {
            "tier_1": "Add the two equal sides and the base.",
            "tier_2": f"{legs} + {legs} + {base} = {perim}.",
            "tier_3": f"Perimeter = {perim} cm."
        },
        "misconception_tags": ["adding_equal_side_only_once"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Sets up 2({legs}) + {base}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates perimeter = {perim} cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 08. Perimeter of scalene triangle
def arch_08_perimeter_of_scalene_triangle(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(6, 12)
    b = rng.randint(a + 1, a + 6)
    c = rng.randint(b + 1, a + b - 1)
    perim = a + b + c
    ans = f"{perim} m"
    prompt = (
        f"A triangular flowerbed has side lengths of ${a}\\text{{ m}}$, ${b}\\text{{ m}}$, and ${c}\\text{{ m}}$.\n\n"
        f"Calculate the perimeter of the flowerbed."
    )
    sol = (
        f"**Perimeter:**\n"
        f"$$P = a + b + c = {a} + {b} + {c} = {perim}\\text{{ m}}$$"
    )
    return {
        "id": f"g7_pa_08_{rng.randint(100000, 999999)}",
        "subskill": "08_perimeter_of_scalene_triangle",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{perim} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_08",
        "hints": {
            "tier_1": "Add all three different side lengths.",
            "tier_2": f"{a} + {b} + {c} = {perim}.",
            "tier_3": f"Perimeter = {perim} m."
        },
        "misconception_tags": ["arithmetic_addition_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Sets up sum of 3 sides", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates perimeter = {perim} m", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 09. Perimeter of regular pentagon
def arch_09_perimeter_of_regular_pentagon(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(4, 18)
    perim = 5 * s
    ans = f"{perim} cm"
    prompt = (
        f"A regular pentagon has five equal sides, each measuring ${s}\\text{{ cm}}$.\n\n"
        f"Calculate the perimeter of the pentagon."
    )
    sol = (
        f"**Perimeter Calculation:**\n"
        f"$$P = 5 \\times s = 5 \\times {s} = {perim}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_pa_09_{rng.randint(100000, 999999)}",
        "subskill": "09_perimeter_of_regular_pentagon",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{perim} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_09",
        "hints": {
            "tier_1": "A pentagon has 5 sides. Multiply side length by 5.",
            "tier_2": f"5 × {s} = {perim}.",
            "tier_3": f"Perimeter = {perim} cm."
        },
        "misconception_tags": ["wrong_side_count_for_pentagon"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Uses P = 5s", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates perimeter = {perim} cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 10. Perimeter of regular hexagon
def arch_10_perimeter_of_regular_hexagon(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(5, 20)
    perim = 6 * s
    ans = f"{perim} mm"
    prompt = (
        f"A honeycomb cell has the shape of a regular hexagon with sides measuring ${s}\\text{{ mm}}$.\n\n"
        f"Calculate the perimeter of the hexagon."
    )
    sol = (
        f"**Perimeter Calculation:**\n"
        f"$$P = 6 \\times s = 6 \\times {s} = {perim}\\text{{ mm}}$$"
    )
    return {
        "id": f"g7_pa_10_{rng.randint(100000, 999999)}",
        "subskill": "10_perimeter_of_regular_hexagon",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{perim} mm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_10",
        "hints": {
            "tier_1": "A hexagon has 6 sides. Multiply side by 6.",
            "tier_2": f"6 × {s} = {perim}.",
            "tier_3": f"Perimeter = {perim} mm."
        },
        "misconception_tags": ["wrong_side_count_for_hexagon"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Uses P = 6s", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates perimeter = {perim} mm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 11. Perimeter of regular octagon
def arch_11_perimeter_of_regular_octagon(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(4, 15)
    perim = 8 * s
    ans = f"{perim} cm"
    prompt = (
        f"A standard road stop sign is a regular octagon with each edge measuring ${s}\\text{{ cm}}$.\n\n"
        f"Calculate the perimeter of the stop sign."
    )
    sol = (
        f"**Perimeter Calculation:**\n"
        f"A regular octagon has $8$ congruent sides:\n"
        f"$$P = 8 \\times s = 8 \\times {s} = {perim}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_pa_11_{rng.randint(100000, 999999)}",
        "subskill": "11_perimeter_of_regular_octagon",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{perim} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_11",
        "hints": {
            "tier_1": "An octagon has 8 sides. Multiply side by 8.",
            "tier_2": f"8 × {s} = {perim}.",
            "tier_3": f"Perimeter = {perim} cm."
        },
        "misconception_tags": ["wrong_side_count_for_octagon"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Uses P = 8s", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates perimeter = {perim} cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 12. Perimeter of irregular polygon missing side
def arch_12_perimeter_of_irregular_polygon_missing_side(rng: random.Random) -> Dict[str, Any]:
    s1, s2, s3, s4 = 8, 12, 10, 6
    known_sum = s1 + s2 + s3 + s4
    missing_s = rng.randint(5, 14)
    total_p = known_sum + missing_s
    ans = f"{missing_s} m"
    prompt = (
        f"A 5-sided irregular enclosure has a total perimeter of ${total_p}\\text{{ m}}$.\n"
        f"Four of the side lengths are ${s1}\\text{{ m}}$, ${s2}\\text{{ m}}$, ${s3}\\text{{ m}}$, and ${s4}\\text{{ m}}$.\n\n"
        f"Calculate the length of the fifth side."
    )
    sol = (
        f"**Step 1: Sum the known side lengths:**\n"
        f"$$\\text{{Sum of 4 sides}} = {s1} + {s2} + {s3} + {s4} = {known_sum}\\text{{ m}}$$\n\n"
        f"**Step 2: Subtract from total perimeter:**\n"
        f"$$\\text{{Fifth side}} = {total_p} - {known_sum} = {missing_s}\\text{{ m}}$$"
    )
    return {
        "id": f"g7_pa_12_{rng.randint(100000, 999999)}",
        "subskill": "12_perimeter_of_irregular_polygon_missing_side",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{missing_s} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_12",
        "hints": {
            "tier_1": f"Add the 4 known sides: {known_sum}.",
            "tier_2": f"Subtract {known_sum} from total perimeter {total_p}.",
            "tier_3": f"Fifth side = {missing_s} m."
        },
        "misconception_tags": ["arithmetic_subtraction_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Sums known sides = {known_sum}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates missing side = {missing_s} m", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 13. Circumference of circle given radius
def arch_13_circumference_of_circle_given_radius(rng: random.Random) -> Dict[str, Any]:
    r = rng.choice([7, 14, 21, 28])
    c = int(2 * (22 / 7) * r)
    ans = f"{c} cm"
    prompt = (
        f"Calculate the **circumference** of a circle with a radius of $r = {r}\\text{{ cm}}$.\n"
        f"(Use the approximation $\\pi \\approx \\frac{{22}}{{7}}$)."
    )
    sol = (
        f"**Step 1: Formula for Circumference:**\n"
        f"$$C = 2\\pi r$$\n\n"
        f"**Step 2: Substitute $r = {r}$ and $\\pi = \\frac{{22}}{{7}}$:**\n"
        f"$$C = 2 \\times \\frac{{22}}{{7}} \\times {r} = 2 \\times 22 \\times {r // 7} = {c}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_pa_13_{rng.randint(100000, 999999)}",
        "subskill": "13_circumference_of_circle_given_radius",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{c} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_13",
        "hints": {
            "tier_1": "Circumference = 2 × π × radius.",
            "tier_2": f"2 × (22/7) × {r} = 44 × {r // 7}.",
            "tier_3": f"Circumference = {c} cm."
        },
        "misconception_tags": ["using_area_formula_for_circumference"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States formula C = 2*pi*r", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates circumference = {c} cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 14. Circumference of circle given diameter
def arch_14_circumference_of_circle_given_diameter(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([14, 28, 35, 42])
    c = int((22 / 7) * d)
    ans = f"{c} m"
    prompt = (
        f"A circular swimming pool has a diameter of $d = {d}\\text{{ m}}$.\n\n"
        f"Calculate the circumference of the pool using $\\pi \\approx \\frac{{22}}{{7}}$."
    )
    sol = (
        f"**Step 1: Formula for Circumference using Diameter:**\n"
        f"$$C = \\pi d$$\n\n"
        f"**Step 2: Substitute $d = {d}$:**\n"
        f"$$C = \\frac{{22}}{{7}} \\times {d} = 22 \\times {d // 7} = {c}\\text{{ m}}$$"
    )
    return {
        "id": f"g7_pa_14_{rng.randint(100000, 999999)}",
        "subskill": "14_circumference_of_circle_given_diameter",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{c} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_14",
        "hints": {
            "tier_1": "Circumference = π × diameter.",
            "tier_2": f"(22/7) × {d} = {c}.",
            "tier_3": f"Circumference = {c} m."
        },
        "misconception_tags": ["doubling_diameter_in_circumference"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Uses C = pi*d", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates circumference = {c} m", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 15. Perimeter word problem fencing cost
def arch_15_perimeter_word_problem_fencing_cost(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(20, 40)
    b = rng.randint(10, 20)
    cost_per_m = rng.choice([45, 60, 80])
    perim = 2 * (l + b)
    total_cost = perim * cost_per_m
    ans = f"R{total_cost}"
    prompt = (
        f"A farmer fences a rectangular vegetable garden measuring ${l}\\text{{ m}}$ by ${b}\\text{{ m}}$.\n"
        f"Wire fencing costs **R{cost_per_m} per metre**.\n\n"
        f"1. Calculate the perimeter of the garden.\n"
        f"2. Calculate the total cost to fence the entire garden."
    )
    sol = (
        f"**Step 1: Calculate Perimeter:**\n"
        f"$$P = 2({l} + {b}) = 2({l + b}) = {perim}\\text{{ m}}$$\n\n"
        f"**Step 2: Total Cost:**\n"
        f"$$\\text{{Total Cost}} = {perim} \\times \\text{{R}}{cost_per_m} = \\text{{R}}{total_cost}$$"
    )
    return {
        "id": f"g7_pa_15_{rng.randint(100000, 999999)}",
        "subskill": "15_perimeter_word_problem_fencing_cost",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Perimeter = {perim} m; Total Cost = R{total_cost}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pa_15",
        "hints": {
            "tier_1": f"Perimeter = 2({l} + {b}) = {perim} m.",
            "tier_2": f"Multiply {perim} by R{cost_per_m}.",
            "tier_3": f"Cost = R{total_cost}."
        },
        "misconception_tags": ["multiplying_area_by_fencing_cost"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates perimeter = {perim} m", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Calculates total cost = R{total_cost}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


# 16. Perimeter word problem running track laps
def arch_16_perimeter_word_problem_running_track_laps(rng: random.Random) -> Dict[str, Any]:
    laps = rng.choice([4, 5, 8, 10])
    track_perim = 400
    total_m = laps * track_perim
    total_km = round(total_m / 1000, 2)
    ans = f"{total_km} km (or {total_m} m)"
    prompt = (
        f"An athletics running track has a lap perimeter of ${track_perim}\\text{{ m}}$.\n"
        f"An athlete completes **{laps} full laps** during a training session.\n\n"
        f"Calculate the total distance run in kilometres (km)."
    )
    sol = (
        f"**Step 1: Total distance in metres:**\n"
        f"$$\\text{{Distance}} = {laps} \\times {track_perim}\\text{{ m}} = {total_m}\\text{{ m}}$$\n\n"
        f"**Step 2: Convert to kilometres ($1\\text{{ km}} = 1\\,000\\text{{ m}}$):**\n"
        f"$$\\text{{Distance}} = \\frac{{{total_m}}}{{1\\,000}} = {total_km}\\text{{ km}}$$"
    )
    return {
        "id": f"g7_pa_16_{rng.randint(100000, 999999)}",
        "subskill": "16_perimeter_word_problem_running_track_laps",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{total_km} km",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_16",
        "hints": {
            "tier_1": f"Multiply {laps} by {track_perim} m to get total metres.",
            "tier_2": f"Divide {total_m} by 1 000 to convert to km.",
            "tier_3": f"{total_km} km."
        },
        "misconception_tags": ["dividing_by_100_instead_of_1000_for_km"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates total metres = {total_m} m", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Converts to km = {total_km} km", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 17. Area of square standard
def arch_17_area_of_square_standard(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(5, 20)
    area = s * s
    ans = f"{area} cm^2"
    prompt = (
        f"A square has a side length of ${s}\\text{{ cm}}$.\n\n"
        f"1. State the formula for the area of a square.\n"
        f"2. Calculate the area of the square with appropriate square units."
    )
    sol = (
        f"**Step 1: Formula for Area:**\n"
        f"$$A = s^2 \\quad \\text{{or}} \\quad A = s \\times s$$\n\n"
        f"**Step 2: Calculate:**\n"
        f"$$A = {s} \\times {s} = {area}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_pa_17_{rng.randint(100000, 999999)}",
        "subskill": "17_area_of_square_standard",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"A = s^2 = {s}^2 = {area} cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_17",
        "hints": {
            "tier_1": "Area is side multiplied by side.",
            "tier_2": f"{s} × {s} = {area}.",
            "tier_3": f"Area = {area} cm²."
        },
        "misconception_tags": ["multiplying_side_by_4_for_area"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States formula A = s^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates area = {area} cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 18. Area of square find side from area
def arch_18_area_of_square_find_side_from_area(rng: random.Random) -> Dict[str, Any]:
    s = rng.choice([6, 7, 8, 9, 10, 11, 12, 15, 20])
    area = s * s
    ans = f"{s} m"
    prompt = (
        f"A square tiled floor has a total area of ${area}\\text{{ m}}^2$.\n\n"
        f"Calculate the length of one side of the square floor."
    )
    sol = (
        f"**Step 1: Formula:**\n"
        f"$$A = s^2 \\implies s = \\sqrt{{A}}$$\n\n"
        f"**Step 2: Square Root:**\n"
        f"$$s = \\sqrt{{{area}}} = {s}\\text{{ m}}$$"
    )
    return {
        "id": f"g7_pa_18_{rng.randint(100000, 999999)}",
        "subskill": "18_area_of_square_find_side_from_area",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{s} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_18",
        "hints": {
            "tier_1": f"What number multiplied by itself gives {area}?",
            "tier_2": f"Find the square root of {area}.",
            "tier_3": f"Side = {s} m."
        },
        "misconception_tags": ["dividing_area_by_4_instead_of_square_root"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Applies square root: s = sqrt({area})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates side = {s} m", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 19. Area of rectangle standard
def arch_19_area_of_rectangle_standard(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(8, 25)
    b = rng.randint(4, l - 2)
    area = l * b
    svg = _svg_rectangle_dim(l, b, "cm")
    ans = f"{area} cm^2"
    prompt = (
        f"Look at the rectangle shown in the diagram with length ${l}\\text{{ cm}}$ and breadth ${b}\\text{{ cm}}$:\n\n"
        f"1. State the formula for the area of a rectangle.\n"
        f"2. Calculate the area of the rectangle."
    )
    sol = (
        f"**Step 1: Formula:**\n"
        f"$$A = l \\times b$$\n\n"
        f"**Step 2: Calculate:**\n"
        f"$$A = {l} \\times {b} = {area}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_pa_19_{rng.randint(100000, 999999)}",
        "subskill": "19_area_of_rectangle_standard",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"A = l × b = {l} × {b} = {area} cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_19",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Multiply length by breadth.",
            "tier_2": f"{l} × {b} = {area}.",
            "tier_3": f"Area = {area} cm²."
        },
        "misconception_tags": ["adding_dimensions_instead_of_multiplying_for_area"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States formula A = l * b", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates area = {area} cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 20. Area of rectangle with decimal dimensions
def arch_20_area_of_rectangle_with_decimal_dimensions(rng: random.Random) -> Dict[str, Any]:
    l_dec = rng.choice([4.5, 6.5, 8.5, 12.5])
    b = rng.choice([2, 4, 6])
    area = round(l_dec * b, 1)
    l_str = str(l_dec).replace(".", "{,}")
    area_str = str(area).replace(".0", "").replace(".", "{,}")
    ans = f"{area_str} m^2"
    prompt = (
        f"A rectangular driveway has a length of ${l_str}\\text{{ m}}$ and a breadth of ${b}\\text{{ m}}$.\n\n"
        f"Calculate the area of the driveway."
    )
    sol = (
        f"**Area Calculation:**\n"
        f"$$A = l \\times b = {l_str} \\times {b} = {area_str}\\text{{ m}}^2$$"
    )
    return {
        "id": f"g7_pa_20_{rng.randint(100000, 999999)}",
        "subskill": "20_area_of_rectangle_with_decimal_dimensions",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{area_str} m^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_20",
        "hints": {
            "tier_1": f"Multiply {l_str} by {b}.",
            "tier_2": f"{l_str} × {b} = {area_str}.",
            "tier_3": f"Area = {area_str} m²."
        },
        "misconception_tags": ["decimal_multiplication_comma_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Sets up {l_str} * {b}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates area = {area_str} m^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 21. Area of rectangle find breadth from area
def arch_21_area_of_rectangle_find_breadth_from_area(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(12, 25)
    b = rng.randint(4, 10)
    area = l * b
    ans = f"{b} cm"
    prompt = (
        f"A rectangle has an area of ${area}\\text{{ cm}}^2$ and a length of ${l}\\text{{ cm}}$.\n\n"
        f"Calculate the breadth of the rectangle."
    )
    sol = (
        f"**Step 1: Formula:**\n"
        f"$$A = l \\times b \\implies b = \\frac{{A}}{{l}}$$\n\n"
        f"**Step 2: Divide:**\n"
        f"$$b = \\frac{{{area}}}{{{l}}} = {b}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_pa_21_{rng.randint(100000, 999999)}",
        "subskill": "21_area_of_rectangle_find_breadth_from_area",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{b} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_21",
        "hints": {
            "tier_1": f"Divide area {area} by length {l}.",
            "tier_2": f"{area} ÷ {l} = {b}.",
            "tier_3": f"Breadth = {b} cm."
        },
        "misconception_tags": ["subtracting_instead_of_dividing_for_area_dimension"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Sets up b = {area} / {l}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates breadth = {b} cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 22. Area of rectangle find length from area
def arch_22_area_of_rectangle_find_length_from_area(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(14, 30)
    b = rng.randint(5, 12)
    area = l * b
    ans = f"{l} m"
    prompt = (
        f"A carpet covers an area of ${area}\\text{{ m}}^2$. If its width is ${b}\\text{{ m}}$, "
        f"what is the length of the carpet?"
    )
    sol = (
        f"**Calculation:**\n"
        f"$$l = \\frac{{A}}{{b}} = \\frac{{{area}}}{{{b}}} = {l}\\text{{ m}}$$"
    )
    return {
        "id": f"g7_pa_22_{rng.randint(100000, 999999)}",
        "subskill": "22_area_of_rectangle_find_length_from_area",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{l} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_22",
        "hints": {
            "tier_1": f"Divide {area} by {b}.",
            "tier_2": f"{area} ÷ {b} = {l}.",
            "tier_3": f"Length = {l} m."
        },
        "misconception_tags": ["division_arithmetic_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Sets up l = {area} / {b}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates length = {l} m", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 23. Area of right-angled triangle
def arch_23_area_of_right_angled_triangle(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([6, 8, 10, 12])
    h = rng.randint(4, 15)
    area = (b * h) // 2
    ans = f"{area} cm^2"
    prompt = (
        f"A right-angled triangle has perpendicular legs of length ${b}\\text{{ cm}}$ and ${h}\\text{{ cm}}$.\n\n"
        f"1. State the formula for the area of a triangle.\n"
        f"2. Calculate the area of the right-angled triangle."
    )
    sol = (
        f"**Step 1: Formula:**\n"
        f"$$A = \\frac{{1}}{{2}} \\times b \\times h$$\n\n"
        f"**Step 2: Calculate:**\n"
        f"$$A = \\frac{{1}}{{2}} \\times {b} \\times {h} = {b // 2} \\times {h} = {area}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_pa_23_{rng.randint(100000, 999999)}",
        "subskill": "23_area_of_right_angled_triangle",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"A = 1/2 × {b} × {h} = {area} cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_23",
        "hints": {
            "tier_1": "In a right-angled triangle, the two perpendicular legs serve as the base and height.",
            "tier_2": f"Area = 1/2 × {b} × {h}.",
            "tier_3": f"Area = {area} cm²."
        },
        "misconception_tags": ["forgetting_half_factor_in_triangle_area"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States formula A = 1/2 * b * h", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates area = {area} cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 24. Area of acute triangle interior height
def arch_24_area_of_acute_triangle_interior_height(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([10, 12, 14, 16])
    h = rng.randint(6, 12)
    area = (b * h) // 2
    svg = _svg_triangle_height(b, h, "cm")
    ans = f"{area} cm^2"
    prompt = (
        f"In the acute triangle $\\Delta ABC$ shown in the diagram, base $b = {b}\\text{{ cm}}$ "
        f"and perpendicular height $h = {h}\\text{{ cm}}$:\n\n"
        f"Calculate the area of $\\Delta ABC$."
    )
    sol = (
        f"**Step 1: Formula:**\n"
        f"$$A = \\frac{{1}}{{2}} \\times b \\times h$$\n\n"
        f"**Step 2: Calculate:**\n"
        f"$$A = \\frac{{1}}{{2}} \\times {b} \\times {h} = {b // 2} \\times {h} = {area}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_pa_24_{rng.randint(100000, 999999)}",
        "subskill": "24_area_of_acute_triangle_interior_height",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"A = 1/2 × {b} × {h} = {area} cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_24",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": f"Use base = {b} and perpendicular height = {h}.",
            "tier_2": f"Multiply {b} by {h} and divide by 2.",
            "tier_3": f"Area = {area} cm²."
        },
        "misconception_tags": ["using_slant_height_for_triangle_area"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Substitutes base and height into 1/2 * b * h", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates area = {area} cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 25. Area of obtuse triangle exterior height
def arch_25_area_of_obtuse_triangle_exterior_height(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([8, 10, 12, 14])
    h = rng.randint(5, 10)
    area = (b * h) // 2
    ans = f"{area} m^2"
    prompt = (
        f"An obtuse triangle has a base of ${b}\\text{{ m}}$. Its perpendicular height, "
        f"measured externally from the opposite apex to the extended base line, is ${h}\\text{{ m}}$.\n\n"
        f"Calculate the area of this obtuse triangle."
    )
    sol = (
        f"**Important Rule for Obtuse Triangles:**\n"
        f"The perpendicular height falls outside the triangle onto the extension of the base. "
        f"Only the actual base ($b = {b}\\text{{ m}}$) is used in the formula, not the extended length!\n\n"
        f"$$A = \\frac{{1}}{{2}} \\times b \\times h = \\frac{{1}}{{2}} \\times {b} \\times {h} = {b // 2} \\times {h} = {area}\\text{{ m}}^2$$"
    )
    return {
        "id": f"g7_pa_25_{rng.randint(100000, 999999)}",
        "subskill": "25_area_of_obtuse_triangle_exterior_height",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"A = 1/2 × {b} × {h} = {area} m^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_25",
        "hints": {
            "tier_1": "Do not add the extended base length! Use only the true base b.",
            "tier_2": f"1/2 × {b} × {h} = {area}.",
            "tier_3": f"Area = {area} m²."
        },
        "misconception_tags": ["adding_base_extension_to_triangle_base"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Uses only true base b in formula", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates area = {area} m^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }
