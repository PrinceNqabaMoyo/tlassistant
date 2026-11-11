"""Grade 7 Mathematics - Perimeter and Area of 2D Shapes: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 4/01. Perimeter and area of 2D shapes.md & Syllabus.md
Focus: Reverse triangle area, composite L/T shapes, shaded regions, SI area unit conversions (mm², cm², m², km²), tiling/carpeting word problems, dimension scaling (k and k²), and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_l_shaped_polygon(w1: int, h1: int, w2: int, h2: int) -> str:
    """Renders a clean static 2D SVG L-shaped polygon."""
    w, h = 320, 200
    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'<polygon points="40,30 140,30 140,90 240,90 240,160 40,160" fill="#e0e7ff" stroke="#4338ca" stroke-width="2"/>'
        f'<text x="90" y="22" text-anchor="middle" font-size="11" font-weight="bold" fill="#312e81">{w1} m</text>'
        f'<text x="25" y="95" text-anchor="middle" font-size="11" font-weight="bold" fill="#312e81">{h1} m</text>'
        f'<text x="140" y="175" text-anchor="middle" font-size="11" font-weight="bold" fill="#312e81">{w1 + w2} m</text>'
        f'<text x="255" y="130" font-size="11" font-weight="bold" fill="#312e81">{h2} m</text>'
        f'</svg>'
    )


# 26. Area of triangle find height from area
def arch_26_area_of_triangle_find_height_from_area(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([8, 10, 12, 16])
    h = rng.randint(6, 15)
    area = (b * h) // 2
    ans = f"{h} cm"
    prompt = (
        f"A triangle has an area of ${area}\\text{{ cm}}^2$ and a base of ${b}\\text{{ cm}}$.\n\n"
        f"Calculate the **perpendicular height** of the triangle."
    )
    sol = (
        f"**Step 1: Formula for Triangle Area:**\n"
        f"$$A = \\frac{{1}}{{2}} \\times b \\times h \\implies 2A = b \\times h$$\n\n"
        f"**Step 2: Solve for height $h$:**\n"
        f"$$h = \\frac{{2A}}{{b}} = \\frac{{2 \\times {area}}}{{{b}}} = \\frac{{{2 * area}}}{{{b}}} = {h}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_pa_26_{rng.randint(100000, 999999)}",
        "subskill": "26_area_of_triangle_find_height_from_area",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{h} cm",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_26",
        "hints": {
            "tier_1": "Double the area first, then divide by the base: h = (2 × A) ÷ b.",
            "tier_2": f"2 × {area} = {2 * area}. Divide by {b}.",
            "tier_3": f"Height = {h} cm."
        },
        "misconception_tags": ["forgetting_to_double_area_when_finding_height"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Doubles area 2 * {area} = {2 * area}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Divides by base to get height = {h} cm", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 27. Area of triangle find base from area
def arch_27_area_of_triangle_find_base_from_area(rng: random.Random) -> Dict[str, Any]:
    b = rng.randint(6, 18)
    h = rng.choice([6, 8, 10, 12])
    area = (b * h) // 2
    ans = f"{b} m"
    prompt = (
        f"A triangular roof truss has an area of ${area}\\text{{ m}}^2$ and a perpendicular height of ${h}\\text{{ m}}$.\n\n"
        f"Calculate the **base length** of the truss."
    )
    sol = (
        f"**Step 1: Formula:**\n"
        f"$$b = \\frac{{2A}}{{h}}$$\n\n"
        f"**Step 2: Calculate:**\n"
        f"$$b = \\frac{{2 \\times {area}}}{{{h}}} = \\frac{{{2 * area}}}{{{h}}} = {b}\\text{{ m}}$$"
    )
    return {
        "id": f"g7_pa_27_{rng.randint(100000, 999999)}",
        "subskill": "27_area_of_triangle_find_base_from_area",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{b} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_27",
        "hints": {
            "tier_1": f"Double {area} and divide by height {h}.",
            "tier_2": f"{2 * area} ÷ {h} = {b}.",
            "tier_3": f"Base = {b} m."
        },
        "misconception_tags": ["forgetting_to_double_area_when_finding_base"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Sets up b = (2 * {area}) / {h}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates base = {b} m", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 28. Area triangle identifying correct perpendicular height
def arch_28_area_triangle_identifying_correct_perpendicular_height(rng: random.Random) -> Dict[str, Any]:
    # Triangle with side BC = 12, AC = 10, AB = 10, perpendicular altitude AT = 8
    ans = "Base = 12 cm, Perpendicular Height = 8 cm; Area = 48 cm^2"
    prompt = (
        "In triangle $\\Delta ABC$, the side lengths are $AB = 10\\text{ cm}$, $AC = 10\\text{ cm}$, "
        "and base $BC = 12\\text{ cm}$. A dotted perpendicular line segment $AT$ from vertex $A$ to base $BC$ measures $8\\text{ cm}$.\n\n"
        "1. Which measurement must be used as the height to calculate the area of $\\Delta ABC$?\n"
        "2. Calculate the area of $\\Delta ABC$."
    )
    sol = (
        "**1. Identifying Height:**\n"
        "The perpendicular height is the perpendicular distance from a vertex to the opposite base, which is **$AT = 8\\text{ cm}$**. "
        "(The side lengths $10\\text{ cm}$ are slant heights and cannot be used as the height in the area formula).\n\n"
        "**2. Area Calculation:**\n"
        "$$A = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 12 \\times 8 = 6 \\times 8 = 48\\text{ cm}^2$$"
    )
    return {
        "id": f"g7_pa_28_{rng.randint(100000, 999999)}",
        "subskill": "28_area_triangle_identifying_correct_perpendicular_height",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Height is AT = 8 cm; Area = 1/2 × 12 × 8 = 48 cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pa_28",
        "hints": {
            "tier_1": "Never use the slant side lengths (10 cm) as height! Use the 90° altitude.",
            "tier_2": "Height = 8 cm, Base = 12 cm.",
            "tier_3": "Area = 1/2 × 12 × 8 = 48 cm²."
        },
        "misconception_tags": ["using_slant_height_for_triangle_area"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies perpendicular altitude AT = 8 cm as height", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Rejects slant heights 10 cm", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Calculates area = 48 cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 29. Area of composite L-shaped polygon
def arch_29_area_of_composite_l_shaped_polygon(rng: random.Random) -> Dict[str, Any]:
    w1, h1 = rng.randint(4, 7), rng.randint(8, 12)
    w2, h2 = rng.randint(5, 9), rng.randint(3, 5)
    svg = _svg_l_shaped_polygon(w1, h1, w2, h2)
    area = (w1 * h1) + (w2 * h2)
    ans = f"{area} m^2"
    prompt = (
        f"Inspect the L-shaped floor plan in the diagram with given dimensions:\n\n"
        f"- Left vertical section: width = ${w1}\\text{{ m}}$, total height = ${h1}\\text{{ m}}$\n"
        f"- Right horizontal extension: width = ${w2}\\text{{ m}}$, height = ${h2}\\text{{ m}}$\n\n"
        f"Calculate the total area of the floor plan by dividing it into two non-overlapping rectangles."
    )
    sol = (
        f"**Step 1: Divide into two rectangles:**\n"
        f"- **Rectangle A (Left vertical):** $\\text{{Area}}_A = {w1} \\times {h1} = {w1 * h1}\\text{{ m}}^2$\n"
        f"- **Rectangle B (Right horizontal):** $\\text{{Area}}_B = {w2} \\times {h2} = {w2 * h2}\\text{{ m}}^2$\n\n"
        f"**Step 2: Add the two areas:**\n"
        f"$$\\text{{Total Area}} = \\text{{Area}}_A + \\text{{Area}}_B = {w1 * h1} + {w2 * h2} = {area}\\text{{ m}}^2$$"
    )
    return {
        "id": f"g7_pa_29_{rng.randint(100000, 999999)}",
        "subskill": "29_area_of_composite_l_shaped_polygon",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{area} m^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pa_29",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": f"Split the L-shape: Rect A = {w1} × {h1}, Rect B = {w2} × {h2}.",
            "tier_2": f"{w1 * h1} + {w2 * h2} = {area}.",
            "tier_3": f"Total area = {area} m²."
        },
        "misconception_tags": ["multiplying_outer_dimensions_for_composite_area"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates area of first rectangle = {w1 * h1} m^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates area of second rectangle = {w2 * h2} m^2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Sums to total area = {area} m^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


# 30. Area of composite T-shaped polygon
def arch_30_area_of_composite_t_shaped_polygon(rng: random.Random) -> Dict[str, Any]:
    # Top horizontal bar: 10 by 3 -> 30
    # Central stem: 4 by 6 -> 24
    # Total = 54
    top_w, top_h = 10, 3
    stem_w, stem_h = 4, 6
    total_area = (top_w * top_h) + (stem_w * stem_h)
    ans = f"{total_area} cm^2"
    prompt = (
        f"A T-shaped wooden plaque consists of a top crossbar measuring ${top_w}\\text{{ cm}}$ by ${top_h}\\text{{ cm}}$, "
        f"and a vertical stem measuring ${stem_w}\\text{{ cm}}$ wide by ${stem_h}\\text{{ cm}}$ high.\n\n"
        f"Calculate the total area of the plaque."
    )
    sol = (
        f"**Step 1: Area of top crossbar:**\n"
        f"$$\\text{{Area}}_{{\\text{{top}}}} = {top_w} \\times {top_h} = {top_w * top_h}\\text{{ cm}}^2$$\n\n"
        f"**Step 2: Area of vertical stem:**\n"
        f"$$\\text{{Area}}_{{\\text{{stem}}}} = {stem_w} \\times {stem_h} = {stem_w * stem_h}\\text{{ cm}}^2$$\n\n"
        f"**Step 3: Total Area:**\n"
        f"$$\\text{{Total Area}} = {top_w * top_h} + {stem_w * stem_h} = {total_area}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_pa_30_{rng.randint(100000, 999999)}",
        "subskill": "30_area_of_composite_t_shaped_polygon",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{total_area} cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_30",
        "hints": {
            "tier_1": f"Add the area of the top bar ({top_w} × {top_h}) and the stem ({stem_w} × {stem_h}).",
            "tier_2": f"{top_w * top_h} + {stem_w * stem_h} = {total_area}.",
            "tier_3": f"Total area = {total_area} cm²."
        },
        "misconception_tags": ["composite_subtraction_addition_confusion"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates both sub-rectangle areas", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Sums to get total area = {total_area} cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 31. Area of composite rectangle plus triangle
def arch_31_area_of_composite_rectangle_plus_triangle(rng: random.Random) -> Dict[str, Any]:
    # House shape: rectangle 8m by 5m -> 40m^2; triangular roof base 8m, height 3m -> 12m^2; total 52m^2
    rw, rh = 8, 5
    th = 3
    rect_a = rw * rh
    tri_a = (rw * th) // 2
    total_a = rect_a + tri_a
    ans = f"{total_a} m^2"
    prompt = (
        f"The side wall of a barn has the shape of a rectangle surmounted by a triangular gable roof.\n"
        f"- The rectangular base has width ${rw}\\text{{ m}}$ and height ${rh}\\text{{ m}}$.\n"
        f"- The triangular roof has the same base of ${rw}\\text{{ m}}$ and a perpendicular height of ${th}\\text{{ m}}$.\n\n"
        f"Calculate the total area of the barn wall."
    )
    sol = (
        f"**Step 1: Area of Rectangle:**\n"
        f"$$\\text{{Area}}_{{\\text{{rect}}}} = {rw} \\times {rh} = {rect_a}\\text{{ m}}^2$$\n\n"
        f"**Step 2: Area of Triangle:**\n"
        f"$$\\text{{Area}}_{{\\text{{tri}}}} = \\frac{{1}}{{2}} \\times {rw} \\times {th} = 4 \\times {th} = {tri_a}\\text{{ m}}^2$$\n\n"
        f"**Step 3: Total Area:**\n"
        f"$$\\text{{Total Area}} = {rect_a} + {tri_a} = {total_a}\\text{{ m}}^2$$"
    )
    return {
        "id": f"g7_pa_31_{rng.randint(100000, 999999)}",
        "subskill": "31_area_of_composite_rectangle_plus_triangle",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{total_a} m^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pa_31",
        "hints": {
            "tier_1": f"Rectangle area = {rw} × {rh} = {rect_a}. Triangle area = 1/2 × {rw} × {th} = {tri_a}.",
            "tier_2": f"Add them together: {rect_a} + {tri_a}.",
            "tier_3": f"Total area = {total_a} m²."
        },
        "misconception_tags": ["forgetting_half_factor_for_roof_triangle"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates rectangle area = {rect_a} m^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates triangle area = {tri_a} m^2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Sums to get total = {total_a} m^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


# 32. Area of shaded region rectangle with inner rectangle
def arch_32_area_of_shaded_region_rectangle_with_inner_rectangle(rng: random.Random) -> Dict[str, Any]:
    # Outer rectangle: 12 by 9 -> 108
    # Inner swimming pool: 8 by 5 -> 40
    # Shaded paved border = 108 - 40 = 68
    out_l, out_b = 12, 9
    in_l, in_b = 8, 5
    out_a = out_l * out_b
    in_a = in_l * in_b
    shaded_a = out_a - in_a
    ans = f"{shaded_a} m^2"
    prompt = (
        f"A rectangular courtyard measures ${out_l}\\text{{ m}}$ by ${out_b}\\text{{ m}}$. "
        f"Inside the courtyard, a swimming pool measuring ${in_l}\\text{{ m}}$ by ${in_b}\\text{{ m}}$ is built.\n"
        f"The remaining courtyard area surrounding the pool is paved.\n\n"
        f"Calculate the **area of the paved (shaded) region**."
    )
    sol = (
        f"**Step 1: Total courtyard area (outer):**\n"
        f"$$\\text{{Area}}_{{\\text{{outer}}}} = {out_l} \\times {out_b} = {out_a}\\text{{ m}}^2$$\n\n"
        f"**Step 2: Swimming pool area (inner):**\n"
        f"$$\\text{{Area}}_{{\\text{{inner}}}} = {in_l} \\times {in_b} = {in_a}\\text{{ m}}^2$$\n\n"
        f"**Step 3: Shaded paved area (subtract inner from outer):**\n"
        f"$$\\text{{Shaded Area}} = {out_a} - {in_a} = {shaded_a}\\text{{ m}}^2$$"
    )
    return {
        "id": f"g7_pa_32_{rng.randint(100000, 999999)}",
        "subskill": "32_area_of_shaded_region_rectangle_with_inner_rectangle",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{shaded_a} m^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pa_32",
        "hints": {
            "tier_1": f"Outer area = {out_l} × {out_b} = {out_a}. Inner area = {in_l} × {in_b} = {in_a}.",
            "tier_2": f"Subtract inner area from outer area: {out_a} - {in_a}.",
            "tier_3": f"Shaded area = {shaded_a} m²."
        },
        "misconception_tags": ["adding_instead_of_subtracting_inner_area"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates outer area = {out_a} m^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates inner area = {in_a} m^2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Subtracts to get shaded area = {shaded_a} m^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


# 33. Area of shaded region square with inner triangle
def arch_33_area_of_shaded_region_square_with_inner_triangle(rng: random.Random) -> Dict[str, Any]:
    # Square 10 by 10 -> 100
    # Triangle base 10, height 6 -> 30
    # Shaded = 100 - 30 = 70
    s = 10
    th = 6
    sq_a = s * s
    tri_a = (s * th) // 2
    shaded = sq_a - tri_a
    ans = f"{shaded} cm^2"
    prompt = (
        f"A square cardboard sheet has sides of length ${s}\\text{{ cm}}$ (area = ${sq_a}\\text{{ cm}}^2$).\n"
        f"A triangle with base ${s}\\text{{ cm}}$ and height ${th}\\text{{ cm}}$ is cut out of the square.\n\n"
        f"Calculate the area of the remaining (shaded) cardboard sheet."
    )
    sol = (
        f"**Step 1: Cardboard square area:**\n"
        f"$$\\text{{Area}}_{{\\text{{square}}}} = {s} \\times {s} = {sq_a}\\text{{ cm}}^2$$\n\n"
        f"**Step 2: Triangle cutout area:**\n"
        f"$$\\text{{Area}}_{{\\text{{triangle}}}} = \\frac{{1}}{{2}} \\times {s} \\times {th} = {tri_a}\\text{{ cm}}^2$$\n\n"
        f"**Step 3: Remaining shaded area:**\n"
        f"$$\\text{{Remaining Area}} = {sq_a} - {tri_a} = {shaded}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_pa_33_{rng.randint(100000, 999999)}",
        "subskill": "33_area_of_shaded_region_square_with_inner_triangle",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{shaded} cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_33",
        "hints": {
            "tier_1": f"Triangle cutout = 1/2 × {s} × {th} = {tri_a}.",
            "tier_2": f"Subtract from square: {sq_a} - {tri_a}.",
            "tier_3": f"Remaining area = {shaded} cm²."
        },
        "misconception_tags": ["subtraction_error_in_cutout"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates triangle cutout area = {tri_a} cm^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Subtracts from square to get {shaded} cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 34. Perimeter of composite L-shaped polygon
def arch_34_perimeter_of_composite_l_shaped_polygon(rng: random.Random) -> Dict[str, Any]:
    w1, h1 = 6, 10
    w2, h2 = 8, 4
    # Total width = 6 + 8 = 14, total height = 10
    # Perimeter of any orthogonal stepped polygon = 2 * (total width + total height) = 2 * (14 + 10) = 48
    tot_w = w1 + w2
    tot_h = h1
    perim = 2 * (tot_w + tot_h)
    ans = f"{perim} m"
    prompt = (
        f"An L-shaped lawn has the following boundary dimensions:\n"
        f"- Top horizontal edge: ${w1}\\text{{ m}}$\n"
        f"- Leftmost vertical edge: ${h1}\\text{{ m}}$\n"
        f"- Bottom horizontal edge: ${tot_w}\\text{{ m}}$\n"
        f"- Rightmost vertical edge: ${h2}\\text{{ m}}$\n\n"
        f"1. Explain how to find the missing inward boundary lengths.\n"
        f"2. Calculate the total perimeter of the lawn."
    )
    sol = (
        f"**Step 1: Determine missing edges:**\n"
        f"- Inward vertical step: ${tot_h} - {h2} = {tot_h - h2}\\text{{ m}}$\n"
        f"- Inward horizontal step: ${tot_w} - {w1} = {w2}\\text{{ m}}$\n\n"
        f"**Step 2: Perimeter calculation:**\n"
        f"Notice that the sum of the horizontal steps equals the total width (${tot_w}\\text{{ m}}$), "
        f"and the sum of the vertical steps equals the total height (${tot_h}\\text{{ m}}$).\n"
        f"$$P = 2(\\text{{Total Width}} + \\text{{Total Height}}) = 2({tot_w} + {tot_h}) = 2({tot_w + tot_h}) = {perim}\\text{{ m}}$$"
    )
    return {
        "id": f"g7_pa_34_{rng.randint(100000, 999999)}",
        "subskill": "34_perimeter_of_composite_l_shaped_polygon",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"P = 2({tot_w} + {tot_h}) = {perim} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pa_34",
        "hints": {
            "tier_1": "The perimeter of an L-shape equals the perimeter of the enclosing rectangle!",
            "tier_2": f"Total width = {tot_w} m, Total height = {tot_h} m. P = 2({tot_w} + {tot_h}).",
            "tier_3": f"Perimeter = {perim} m."
        },
        "misconception_tags": ["omitting_inward_step_edges"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates missing inward step edges", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Sets up total perimeter sum", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculates perimeter = {perim} m", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 35. Area unit conversion cm2 to mm2
def arch_35_area_unit_conversion_cm2_to_mm2(rng: random.Random) -> Dict[str, Any]:
    cm2 = rng.choice([3, 5, 8, 12, 25])
    mm2 = cm2 * 100
    ans = f"{mm2} mm^2"
    prompt = (
        f"Convert an area of ${cm2}\\text{{ cm}}^2$ into square millimetres ($\\text{{mm}}^2$).\n\n"
        f"Show your reasoning based on $1\\text{{ cm}} = 10\\text{{ mm}}$."
    )
    sol = (
        f"**Conversion Principle:**\n"
        f"Since $1\\text{{ cm}} = 10\\text{{ mm}}$, a square of $1\\text{{ cm}}$ by $1\\text{{ cm}}$ contains:\n"
        f"$$1\\text{{ cm}}^2 = 10\\text{{ mm}} \\times 10\\text{{ mm}} = 100\\text{{ mm}}^2$$\n\n"
        f"**Calculate:**\n"
        f"$${cm2}\\text{{ cm}}^2 = {cm2} \\times 100 = {mm2}\\text{{ mm}}^2$$"
    )
    return {
        "id": f"g7_pa_35_{rng.randint(100000, 999999)}",
        "subskill": "35_area_unit_conversion_cm2_to_mm2",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{mm2} mm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_35",
        "hints": {
            "tier_1": "1 cm² = 10 mm × 10 mm = 100 mm² (multiply by 100, not 10!).",
            "tier_2": f"{cm2} × 100 = {mm2}.",
            "tier_3": f"{mm2} mm²."
        },
        "misconception_tags": ["multiplying_by_10_instead_of_100_for_area"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States 1 cm^2 = 100 mm^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates {mm2} mm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 36. Area unit conversion mm2 to cm2
def arch_36_area_unit_conversion_mm2_to_cm2(rng: random.Random) -> Dict[str, Any]:
    mm2 = rng.choice([400, 750, 1200, 2500])
    cm2_val = mm2 / 100
    cm2_str = str(cm2_val).replace(".0", "").replace(".", "{,}")
    ans = f"{cm2_str} cm^2"
    prompt = (
        f"Convert ${mm2}\\text{{ mm}}^2$ to square centimetres ($\\text{{cm}}^2$)."
    )
    sol = (
        f"**Step 1:** $1\\text{{ cm}}^2 = 100\\text{{ mm}}^2$.\n"
        f"To convert $\\text{{mm}}^2$ to $\\text{{cm}}^2$, divide by $100$:\n\n"
        f"$${mm2}\\text{{ mm}}^2 = \\frac{{{mm2}}}{{100}} = {cm2_str}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_pa_36_{rng.randint(100000, 999999)}",
        "subskill": "36_area_unit_conversion_mm2_to_cm2",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{cm2_str} cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_36",
        "hints": {
            "tier_1": "Divide by 100.",
            "tier_2": f"{mm2} ÷ 100 = {cm2_str}.",
            "tier_3": f"{cm2_str} cm²."
        },
        "misconception_tags": ["dividing_by_10_instead_of_100_for_area"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Divides by 100", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates {cm2_str} cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 37. Area unit conversion m2 to cm2
def arch_37_area_unit_conversion_m2_to_cm2(rng: random.Random) -> Dict[str, Any]:
    m2 = rng.choice([2, 3, 5, 8])
    cm2 = m2 * 10000
    ans = f"{cm2} cm^2"
    prompt = (
        f"Convert ${m2}\\text{{ m}}^2$ into square centimetres ($\\text{{cm}}^2$).\n\n"
        f"Explain why $1\\text{{ m}}^2 = 10\\,000\\text{{ cm}}^2$."
    )
    sol = (
        f"**Reasoning:**\n"
        f"Since $1\\text{{ m}} = 100\\text{{ cm}}$, an area of $1\\text{{ m}}^2$ is:\n"
        f"$$1\\text{{ m}}^2 = 100\\text{{ cm}} \\times 100\\text{{ cm}} = 10\\,000\\text{{ cm}}^2$$\n\n"
        f"**Convert ${m2}\\text{{ m}}^2$:**\n"
        f"$${m2}\\text{{ m}}^2 = {m2} \\times 10\\,000 = {cm2}\\text{{ cm}}^2$$"
    )
    return {
        "id": f"g7_pa_37_{rng.randint(100000, 999999)}",
        "subskill": "37_area_unit_conversion_m2_to_cm2",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{cm2} cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_37",
        "hints": {
            "tier_1": "1 m² = 10 000 cm² (not 100!).",
            "tier_2": f"Multiply {m2} by 10 000.",
            "tier_3": f"{cm2} cm²."
        },
        "misconception_tags": ["multiplying_by_100_instead_of_10000_for_m2"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States 1 m^2 = 10 000 cm^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates {cm2} cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 38. Area unit conversion cm2 to m2
def arch_38_area_unit_conversion_cm2_to_m2(rng: random.Random) -> Dict[str, Any]:
    cm2 = rng.choice([20000, 35000, 50000, 80000])
    m2_val = cm2 / 10000
    m2_str = str(m2_val).replace(".0", "").replace(".", "{,}")
    ans = f"{m2_str} m^2"
    prompt = (
        f"Convert ${cm2}\\text{{ cm}}^2$ to square metres ($\\text{{m}}^2$)."
    )
    sol = (
        f"**Step 1:** To convert $\\text{{cm}}^2$ to $\\text{{m}}^2$, divide by $10\\,000$:\n\n"
        f"$${cm2}\\text{{ cm}}^2 = \\frac{{{cm2}}}{{10\\,000}} = {m2_str}\\text{{ m}}^2$$"
    )
    return {
        "id": f"g7_pa_38_{rng.randint(100000, 999999)}",
        "subskill": "38_area_unit_conversion_cm2_to_m2",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{m2_str} m^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_38",
        "hints": {
            "tier_1": "Divide by 10 000.",
            "tier_2": f"{cm2} ÷ 10 000 = {m2_str}.",
            "tier_3": f"{m2_str} m²."
        },
        "misconception_tags": ["dividing_by_100_instead_of_10000_for_m2"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Divides by 10 000", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates {m2_str} m^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 39. Area unit conversion km2 to m2
def arch_39_area_unit_conversion_km2_to_m2(rng: random.Random) -> Dict[str, Any]:
    km2 = rng.choice([2, 4, 5, 10])
    m2 = km2 * 1000000
    ans = f"{m2} m^2"
    prompt = (
        f"A game reserve has an area of ${km2}\\text{{ km}}^2$.\n\n"
        f"Express this area in square metres ($\\text{{m}}^2$)."
    )
    sol = (
        f"**Reasoning:**\n"
        f"Since $1\\text{{ km}} = 1\\,000\\text{{ m}}$:\n"
        f"$$1\\text{{ km}}^2 = 1\\,000\\text{{ m}} \\times 1\\,000\\text{{ m}} = 1\\,000\\,000\\text{{ m}}^2$$\n\n"
        f"**Calculate:**\n"
        f"$${km2}\\text{{ km}}^2 = {km2} \\times 1\\,000\\,000 = {m2}\\text{{ m}}^2$$"
    )
    return {
        "id": f"g7_pa_39_{rng.randint(100000, 999999)}",
        "subskill": "39_area_unit_conversion_km2_to_m2",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{m2} m^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_39",
        "hints": {
            "tier_1": "1 km² = 1 000 000 m².",
            "tier_2": f"Multiply {km2} by 1 000 000.",
            "tier_3": f"{m2} m²."
        },
        "misconception_tags": ["multiplying_by_1000_instead_of_1000000_for_km2"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States 1 km^2 = 1 000 000 m^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates {m2} m^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 40. Word problem tiling floor number of tiles
def arch_40_word_problem_tiling_floor_number_of_tiles(rng: random.Random) -> Dict[str, Any]:
    # Floor: 6 m by 4 m -> 24 m^2 = 240 000 cm^2
    # Square tile: 50 cm by 50 cm -> 2500 cm^2
    # Tiles = 240 000 / 2500 = 96 tiles
    fl_l, fl_w = 6, 4
    tile_s = 50
    floor_cm2 = (fl_l * 100) * (fl_w * 100)
    tile_cm2 = tile_s * tile_s
    num_tiles = floor_cm2 // tile_cm2
    ans = f"{num_tiles} tiles"
    prompt = (
        f"A kitchen floor measures ${fl_l}\\text{{ m}}$ by ${fl_w}\\text{{ m}}$.\n"
        f"It is to be tiled with square ceramic tiles measuring ${tile_s}\\text{{ cm}}$ by ${tile_s}\\text{{ cm}}$.\n\n"
        f"How many tiles are needed to cover the entire kitchen floor?"
    )
    sol = (
        f"**Step 1: Convert floor dimensions to cm:**\n"
        f"- Length: ${fl_l}\\text{{ m}} = {fl_l * 100}\\text{{ cm}}$\n"
        f"- Breadth: ${fl_w}\\text{{ m}} = {fl_w * 100}\\text{{ cm}}$\n"
        f"$$\\text{{Floor Area}} = {fl_l * 100} \\times {fl_w * 100} = {floor_cm2}\\text{{ cm}}^2$$\n\n"
        f"**Step 2: Calculate area of one tile:**\n"
        f"$$\\text{{Tile Area}} = {tile_s} \\times {tile_s} = {tile_cm2}\\text{{ cm}}^2$$\n\n"
        f"**Step 3: Divide floor area by tile area:**\n"
        f"$$\\text{{Number of Tiles}} = \\frac{{{floor_cm2}}}{{{tile_cm2}}} = {num_tiles}\\text{{ tiles}}$$"
    )
    return {
        "id": f"g7_pa_40_{rng.randint(100000, 999999)}",
        "subskill": "40_word_problem_tiling_floor_number_of_tiles",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{num_tiles}",
        "sample_answer": f"{num_tiles} tiles",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pa_40",
        "hints": {
            "tier_1": f"Convert metres to cm: {fl_l * 100} cm by {fl_w * 100} cm.",
            "tier_2": f"Floor area = {floor_cm2} cm²; Tile area = {tile_cm2} cm².",
            "tier_3": f"{num_tiles} tiles."
        },
        "misconception_tags": ["dividing_m2_by_cm2_without_conversion"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Converts units and finds floor area = {floor_cm2} cm^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates tile area = {tile_cm2} cm^2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Divides to get {num_tiles} tiles", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


# 41. Word problem carpeting room cost
def arch_41_word_problem_carpeting_room_cost(rng: random.Random) -> Dict[str, Any]:
    l, w = 5, 4
    rate = rng.choice([150, 180, 220])
    area = l * w
    cost = area * rate
    ans = f"R{cost}"
    prompt = (
        f"A bedroom measures ${l}\\text{{ m}}$ long and ${w}\\text{{ m}}$ wide. "
        f"Fitted wall-to-wall carpeting costs **R{rate} per square metre** ($\\text{{m}}^2$).\n\n"
        f"Calculate the total cost to carpet the room."
    )
    sol = (
        f"**Step 1: Calculate room area:**\n"
        f"$$A = {l} \\times {w} = {area}\\text{{ m}}^2$$\n\n"
        f"**Step 2: Calculate total cost:**\n"
        f"$$\\text{{Total Cost}} = {area} \\times \\text{{R}}{rate} = \\text{{R}}{cost}$$"
    )
    return {
        "id": f"g7_pa_41_{rng.randint(100000, 999999)}",
        "subskill": "41_word_problem_carpeting_room_cost",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"R{cost}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_41",
        "hints": {
            "tier_1": f"Area = {l} × {w} = {area} m².",
            "tier_2": f"Multiply {area} by R{rate}.",
            "tier_3": f"Cost = R{cost}."
        },
        "misconception_tags": ["using_perimeter_for_carpeting_cost"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates area = {area} m^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates total cost = R{cost}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 42. Word problem fertilizing lawn area
def arch_42_word_problem_fertilizing_lawn_area(rng: random.Random) -> Dict[str, Any]:
    l, w = 20, 15
    coverage_per_bag = 50
    area = l * w
    bags = area // coverage_per_bag
    ans = f"{bags} bags"
    prompt = (
        f"A rectangular school sports lawn measures ${l}\\text{{ m}}$ by ${w}\\text{{ m}}$.\n"
        f"One bag of organic lawn fertilizer covers an area of **{coverage_per_bag}\\text{{ m}}^2**.\n\n"
        f"How many bags of fertilizer must the groundkeeper purchase to treat the entire lawn?"
    )
    sol = (
        f"**Step 1: Calculate lawn area:**\n"
        f"$$A = {l} \\times {w} = {area}\\text{{ m}}^2$$\n\n"
        f"**Step 2: Number of bags needed:**\n"
        f"$$\\text{{Bags}} = \\frac{{{area}}}{{{coverage_per_bag}}} = {bags}\\text{{ bags}}$$"
    )
    return {
        "id": f"g7_pa_42_{rng.randint(100000, 999999)}",
        "subskill": "42_word_problem_fertilizing_lawn_area",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{bags}",
        "sample_answer": f"{bags} bags",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_42",
        "hints": {
            "tier_1": f"Area = {l} × {w} = {area} m².",
            "tier_2": f"Divide {area} by {coverage_per_bag}.",
            "tier_3": f"{bags} bags."
        },
        "misconception_tags": ["division_error_in_coverage"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates lawn area = {area} m^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates {bags} bags", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 43. Word problem painting wall area litres
def arch_43_word_problem_painting_wall_area_litres(rng: random.Random) -> Dict[str, Any]:
    l, h = 8, 3
    coverage = 6  # 1 litre covers 6 m^2
    area = l * h
    litres = area // coverage
    ans = f"{litres} litres"
    prompt = (
        f"A painter prepares to paint a classroom wall measuring ${l}\\text{{ m}}$ long by ${h}\\text{{ m}}$ high.\n"
        f"One litre of paint covers ${coverage}\\text{{ m}}^2$.\n\n"
        f"How many litres of paint are required to apply one coat of paint to the wall?"
    )
    sol = (
        f"**Step 1: Wall Area:**\n"
        f"$$A = {l} \\times {h} = {area}\\text{{ m}}^2$$\n\n"
        f"**Step 2: Litres required:**\n"
        f"$$\\text{{Litres}} = \\frac{{{area}}}{{{coverage}}} = {litres}\\text{{ litres}}$$"
    )
    return {
        "id": f"g7_pa_43_{rng.randint(100000, 999999)}",
        "subskill": "43_word_problem_painting_wall_area_litres",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"{litres}",
        "sample_answer": f"{litres} litres",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_43",
        "hints": {
            "tier_1": f"Area = {l} × {h} = {area} m².",
            "tier_2": f"Divide {area} by {coverage}.",
            "tier_3": f"{litres} litres."
        },
        "misconception_tags": ["rate_division_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates wall area = {area} m^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates {litres} litres", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 44. Scaling effect doubling dimensions on perimeter
def arch_44_scaling_effect_doubling_dimensions_on_perimeter(rng: random.Random) -> Dict[str, Any]:
    ans = "The perimeter doubles (multiplied by 2)"
    prompt = (
        "A rectangle has length $l$ and breadth $b$ with perimeter $P = 2(l + b)$.\n\n"
        "If both the length and breadth are **doubled** ($l' = 2l$ and $b' = 2b$), "
        "what happens to the perimeter of the new rectangle? Prove your answer algebraically."
    )
    sol = (
        "**Algebraic Proof:**\n"
        "Original perimeter: $P = 2(l + b)$.\n\n"
        "New perimeter $P'$:\n"
        "$$P' = 2(2l + 2b) = 2 \\times 2(l + b) = 2 \\times P$$\n\n"
        "$$\\therefore \\text{The perimeter doubles (is multiplied by 2)}$$"
    )
    return {
        "id": f"g7_pa_44_{rng.randint(100000, 999999)}",
        "subskill": "44_scaling_effect_doubling_dimensions_on_perimeter",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Perimeter doubles (multiplied by 2)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_44",
        "hints": {
            "tier_1": "Perimeter is linear (one-dimensional).",
            "tier_2": "If side lengths double, the boundary distance around doubles.",
            "tier_3": "The perimeter doubles."
        },
        "misconception_tags": ["assuming_perimeter_quadruples_when_doubled"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States perimeter doubles", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Demonstrates algebraic proof P' = 2P", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 45. Scaling effect doubling dimensions on area
def arch_45_scaling_effect_doubling_dimensions_on_area(rng: random.Random) -> Dict[str, Any]:
    ans = "The area quadruples (multiplied by 4 or 2^2)"
    prompt = (
        "A square has side length $s$ and area $A = s^2$.\n\n"
        "If the side length of the square is **doubled** ($s' = 2s$):\n"
        "1. By what factor does the area increase?\n"
        "2. Explain why this happens using algebra."
    )
    sol = (
        "**1. Factor of Increase:**\n"
        "The area increases by a factor of **$4$** ($2^2$).\n\n"
        "**2. Algebraic Explanation:**\n"
        "$$A' = (2s)^2 = 2^2 \\times s^2 = 4s^2 = 4 \\times A$$\n"
        "Because area is a two-dimensional measure ($s \\times s$), doubling each dimension multiplies the total area by $2 \\times 2 = 4$."
    )
    return {
        "id": f"g7_pa_45_{rng.randint(100000, 999999)}",
        "subskill": "45_scaling_effect_doubling_dimensions_on_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Area quadruples (multiplied by 4 because (2s)^2 = 4s^2)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_45",
        "hints": {
            "tier_1": "Area has two dimensions. If length doubles AND width doubles, what is 2 × 2?",
            "tier_2": "(2s)² = 4s².",
            "tier_3": "The area quadruples (multiplied by 4)."
        },
        "misconception_tags": ["assuming_area_doubles_when_dimensions_double"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States area quadruples / multiplied by 4", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Proves using (2s)^2 = 4s^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 46. Scaling effect tripling dimensions on area
def arch_46_scaling_effect_tripling_dimensions_on_area(rng: random.Random) -> Dict[str, Any]:
    ans = "The area increases by a factor of 9 (3^2 = 9 times larger)"
    prompt = (
        "If all side lengths of a rectangle are multiplied by a scale factor of $k = 3$ (tripled), "
        "by what factor does the area of the rectangle increase?"
    )
    sol = (
        "**Scaling Rule for Area:**\n"
        "When linear dimensions are multiplied by scale factor $k$, area is multiplied by $k^2$:\n"
        "$$k^2 = 3^2 = 9$$\n\n"
        "$$\\text{New Area} = (3l) \\times (3b) = 9(lb) = 9 \\times \\text{Original Area}$$\n"
        "$$\\therefore \\text{The area increases by a factor of } 9$$"
    )
    return {
        "id": f"g7_pa_46_{rng.randint(100000, 999999)}",
        "subskill": "46_scaling_effect_tripling_dimensions_on_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "9 times larger (factor of 3^2 = 9)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_46",
        "hints": {
            "tier_1": "Multiply factor by itself: 3 × 3.",
            "tier_2": "k² = 3² = 9.",
            "tier_3": "9 times larger."
        },
        "misconception_tags": ["assuming_area_triples_when_dimensions_triple"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Uses area scaling factor k^2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates 3^2 = 9 times larger", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 47. Common error confusing perimeter and area
def arch_47_common_error_confusing_perimeter_and_area(rng: random.Random) -> Dict[str, Any]:
    ans = "Perimeter is distance around boundary (1D, metres); Area is 2D surface enclosed (square metres)"
    prompt = (
        "A learner writes in a test: *'The perimeter of the classroom is 48 m² and its area is 140 m.'*\n\n"
        "1. Identify the conceptual and unit mistakes in the learner's statement.\n"
        "2. Clearly explain the difference between **perimeter** and **area**."
    )
    sol = (
        "**1. Mistakes:**\n"
        "- Perimeter is a linear 1D distance, so its unit must be metres ($\\text{m}$), not $\\text{m}^2$.\n"
        "- Area is a 2D surface measure, so its unit must be square metres ($\\text{m}^2$), not $\\text{m}$.\n\n"
        "**2. Conceptual Difference:**\n"
        "- **Perimeter:** The total boundary distance *around* the outside of a 2D shape (e.g. running a fence).\n"
        "- **Area:** The total amount of flat 2D surface space enclosed *inside* the boundary (e.g. laying carpet)."
    )
    return {
        "id": f"g7_pa_47_{rng.randint(100000, 999999)}",
        "subskill": "47_common_error_confusing_perimeter_and_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Perimeter is linear 1D boundary (m); Area is 2D enclosed surface (m²); learner swapped units",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_47",
        "hints": {
            "tier_1": "Which one measures the fence? Which one measures the grass inside?",
            "tier_2": "Perimeter has linear units (m), Area has square units (m²).",
            "tier_3": "Perimeter is 1D boundary; area is 2D enclosed surface."
        },
        "misconception_tags": ["confusing_perimeter_and_area"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies swapped units (m vs m^2)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains 1D boundary vs 2D enclosed surface", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 48. Common error using slant height for triangle area
def arch_48_common_error_using_slant_height_for_triangle_area(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: Multiplied slant side instead of perpendicular height; correct area is 1/2 × base × perpendicular height"
    prompt = (
        "An isosceles triangle has base $12\\text{ cm}$, two equal slant sides of $10\\text{ cm}$, "
        "and a vertical perpendicular height of $8\\text{ cm}$.\n\n"
        "A learner calculates the area as: $A = \\frac{1}{2} \\times 12 \\times 10 = 60\\text{ cm}^2$.\n\n"
        "1. Identify the learner's error.\n"
        "2. Calculate the correct area."
    )
    sol = (
        "**1. Error:**\n"
        "The learner used the **slant side length ($10\\text{ cm}$)** instead of the **perpendicular height ($8\\text{ cm}$)**. "
        "The triangle area formula strictly requires the height perpendicular ($90^\\circ$) to the base.\n\n"
        "**2. Correct Calculation:**\n"
        "$$A = \\frac{1}{2} \\times b \\times h = \\frac{1}{2} \\times 12 \\times 8 = 48\\text{ cm}^2$$"
    )
    return {
        "id": f"g7_pa_48_{rng.randint(100000, 999999)}",
        "subskill": "48_common_error_using_slant_height_for_triangle_area",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Used slant height 10 cm instead of perpendicular height 8 cm; correct area is 48 cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_48",
        "hints": {
            "tier_1": "Is the 10 cm line at right angles to the base? No, it's tilted.",
            "tier_2": "Use 8 cm for height. 1/2 × 12 × 8 = 48.",
            "tier_3": "Correct area is 48 cm²."
        },
        "misconception_tags": ["using_slant_height_for_triangle_area"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies incorrect use of slant side 10 cm", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates correct area = 48 cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 49. Common error metric area conversion 100 trap
def arch_49_common_error_metric_area_conversion_100_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: Multiplied by 100 instead of 10 000; 1 m^2 = 10 000 cm^2 because 100 cm × 100 cm = 10 000 cm^2"
    prompt = (
        "A learner writes: *'Since $1\\text{ m} = 100\\text{ cm}$, an area of $5\\text{ m}^2 = 500\\text{ cm}^2$.'*\n\n"
        "1. Identify the mathematical fallacy in the learner's reasoning.\n"
        "2. Provide the correct conversion of $5\\text{ m}^2$ into square centimetres."
    )
    sol = (
        "**1. Mathematical Fallacy:**\n"
        "The learner applied the linear conversion factor ($100$) directly to a two-dimensional area. "
        "A square metre is a square measuring $100\\text{ cm}$ on each of its two sides:\n"
        "$$1\\text{ m}^2 = 100\\text{ cm} \\times 100\\text{ cm} = 10\\,000\\text{ cm}^2$$\n"
        "The conversion factor must be squared ($100^2 = 10\\,000$).\n\n"
        "**2. Correct Conversion:**\n"
        "$$5\\text{ m}^2 = 5 \\times 10\\,000 = 50\\,000\\text{ cm}^2$$"
    )
    return {
        "id": f"g7_pa_49_{rng.randint(100000, 999999)}",
        "subskill": "49_common_error_metric_area_conversion_100_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Used linear factor 100 instead of 10 000; correct answer is 50 000 cm^2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pa_49",
        "hints": {
            "tier_1": "1 m × 1 m = 100 cm × 100 cm = 10 000 cm².",
            "tier_2": "5 × 10 000 = 50 000.",
            "tier_3": "Correct conversion is 50 000 cm²."
        },
        "misconception_tags": ["linear_factor_used_for_area_conversion"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Explains linear 100 vs area 100^2 = 10 000", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates correct 50 000 cm^2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 50. Perimeter and area 2D comprehensive diagnostic autopsy
def arch_50_perimeter_and_area_2d_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    ans = "Statement 1: False (perimeter doubles, area quadruples); Statement 2: False (obtuse height is outside); Statement 3: False (1 cm^2 = 100 mm^2)"
    prompt = (
        "Evaluate whether each of the following three geometric statements is True or False, "
        "and provide a short mathematical justification:\n\n"
        "1. **Statement 1:** 'Doubling the dimensions of a rectangle doubles both its perimeter and its area.'\n"
        "2. **Statement 2:** 'The height of any triangle must always lie inside the triangle.'\n"
        "3. **Statement 3:** 'An area of $1\\text{ cm}^2$ equals $10\\text{ mm}^2$.'"
    )
    sol = (
        "**Diagnostic Autopsy:**\n\n"
        "**1. Statement 1: False.**\n"
        "Doubling dimensions ($2l$ and $2b$) doubles the perimeter ($2P$), but **quadruples the area** ($4A$), "
        "because area is proportional to the square of the scale factor ($2^2 = 4$).\n\n"
        "**2. Statement 2: False.**\n"
        "In an **obtuse-angled triangle**, the perpendicular altitude from an acute vertex falls outside the triangle "
        "onto the extension of the opposite base.\n\n"
        "**3. Statement 3: False.**\n"
        "Since $1\\text{ cm} = 10\\text{ mm}$, $1\\text{ cm}^2 = 10\\text{ mm} \\times 10\\text{ mm} = 100\\text{ mm}^2$, not $10\\text{ mm}^2$."
    )
    return {
        "id": f"g7_pa_50_{rng.randint(100000, 999999)}",
        "subskill": "50_perimeter_and_area_2d_comprehensive_diagnostic_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "All three statements are False",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pa_50",
        "hints": {
            "tier_1": "Test each statement against the laws of scaling, obtuse triangles, and metric conversion.",
            "tier_2": "Statement 1 is False (area is 4x); Statement 2 is False (obtuse triangle); Statement 3 is False (100 mm²).",
            "tier_3": "All three statements are False."
        },
        "misconception_tags": ["scaling_perimeter_vs_area", "obtuse_triangle_exterior_altitude", "linear_factor_used_for_area_conversion"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Refutes Statement 1 (area quadruples, not doubles)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Refutes Statement 2 (obtuse height falls externally)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Refutes Statement 3 (1 cm^2 = 100 mm^2)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }
