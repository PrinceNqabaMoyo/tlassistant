"""Grade 7 Mathematics - Transformation Geometry: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/04. Transformation geometry.md
Focus: Lines of symmetry of 2D shapes, symmetry verification, translations on square grids, coordinate rules, vectors, and preserved properties.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_shape_with_symmetry_line(shape: str, has_symmetry: bool, line_type: str = "vertical", dim_label: str = "") -> str:
    """Renders a clean 2D SVG shape showing an attempted line of symmetry."""
    w, h = 300, 200
    if shape == "rectangle":
        body = '<rect x="60" y="40" width="180" height="120" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
        if line_type == "diagonal":
            line = '<line x1="60" y1="40" x2="240" y2="160" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>'
        elif line_type == "vertical":
            line = '<line x1="150" y1="20" x2="150" y2="180" stroke="#16a34a" stroke-width="2" stroke-dasharray="6,4"/>'
        else:
            line = '<line x1="40" y1="100" x2="260" y2="100" stroke="#16a34a" stroke-width="2" stroke-dasharray="6,4"/>'
    elif shape == "square":
        body = '<rect x="75" y="25" width="150" height="150" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        if line_type == "diagonal":
            line = '<line x1="75" y1="25" x2="225" y2="175" stroke="#16a34a" stroke-width="2" stroke-dasharray="6,4"/>'
        else:
            line = '<line x1="150" y1="10" x2="150" y2="190" stroke="#16a34a" stroke-width="2" stroke-dasharray="6,4"/>'
    elif shape == "isosceles_triangle":
        body = '<polygon points="150,30 80,170 220,170" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>'
        line = '<line x1="150" y1="15" x2="150" y2="185" stroke="#16a34a" stroke-width="2" stroke-dasharray="6,4"/>'
    else:  # parallelogram
        body = '<polygon points="90,40 240,40 210,160 60,160" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        line = '<line x1="60" y1="160" x2="240" y2="40" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>'

    legend_text = f"Dashed line ({line_type}) {dim_label}".strip()
    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'{body}{line}'
        f'<text x="150" y="195" text-anchor="middle" font-size="12" fill="#475569">{legend_text}</text>'
        f'</svg>'
    )


def _svg_grid_translation(ox: int, oy: int, tx: int, ty: int) -> str:
    """Renders a coordinate grid showing original point A and translated point A'."""
    w, h = 320, 240
    # Map grid (0..10) to svg (30..290, 210..30)
    def to_svg(x: int, y: int):
        sx = 40 + x * 24
        sy = 200 - y * 18
        return sx, sy

    grid_lines = []
    for i in range(11):
        x1, y1 = to_svg(i, 0)
        x2, y2 = to_svg(i, 10)
        grid_lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#e2e8f0" stroke-width="1"/>')
        x3, y3 = to_svg(0, i)
        x4, y4 = to_svg(10, i)
        grid_lines.append(f'<line x1="{x3}" y1="{y3}" x2="{x4}" y2="{y4}" stroke="#e2e8f0" stroke-width="1"/>')

    ax, ay = to_svg(ox, oy)
    a_prime_x, a_prime_y = to_svg(tx, ty)

    orig_pt = f'<circle cx="{ax}" cy="{ay}" r="5" fill="#2563eb"/><text x="{ax+8}" y="{ay-5}" font-size="12" font-weight="bold" fill="#1e3a8a">A({ox}; {oy})</text>'
    trans_pt = f'<circle cx="{a_prime_x}" cy="{a_prime_y}" r="5" fill="#16a34a"/><text x="{a_prime_x+8}" y="{a_prime_y-5}" font-size="12" font-weight="bold" fill="#14532d">A\'({tx}; {ty})</text>'
    arrow = f'<line x1="{ax}" y1="{ay}" x2="{a_prime_x}" y2="{a_prime_y}" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,3"/>'

    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'{"".join(grid_lines)}'
        f'{arrow}{orig_pt}{trans_pt}'
        f'</svg>'
    )


# 01. Line of symmetry definition and reflection verification
def arch_01_line_of_symmetry_definition_and_verification(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(4, 12)
    ans = "A line dividing a figure into two identical mirror-image halves that coincide when folded"
    prompt = (
        f"In transformation geometry, define what a **line of symmetry** (axis of symmetry) is for a figure of base {s} cm, "
        "and state what happens to the two halves of a figure when it is folded along this line."
    )
    sol = (
        "**Definition:**\n"
        "A line of symmetry is an imaginary line that divides a figure into two congruent parts that are mirror images of each other.\n\n"
        "**Folding Property:**\n"
        "When the shape is folded along the line of symmetry, the two halves fit perfectly on top of one another (they coincide exactly)."
    )
    return {
        "id": f"g7_tg_01_{rng.randint(100000, 999999)}",
        "subskill": "01_line_of_symmetry_definition_and_verification",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_01",
        "diagram_spec": {"kind": "inline_svg", "svg": _svg_shape_with_symmetry_line("isosceles_triangle", True, "vertical", f"(base {s} cm)"), "diagram_role": "context"},
        "hints": {
            "tier_1": "Think about folding a piece of paper in half so the edges line up perfectly.",
            "tier_2": "The line divides the shape into two mirror images.",
            "tier_3": "It is a line dividing a shape into two congruent mirror-image halves that coincide when folded."
        },
        "misconception_tags": ["confusing_perimeter_with_symmetry"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Defines line of symmetry as dividing shape into mirror-image halves", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States halves coincide / fit perfectly upon folding", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 02. Square lines of symmetry
def arch_02_square_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(4, 15)
    ans = "4"
    svg = _svg_shape_with_symmetry_line("square", True, "diagonal", f"(side {s} cm)")
    prompt = (
        f"The diagram below illustrates a square (side {s} cm) with one of its diagonal lines shown:\n\n"
        "Determine the **total number of lines of symmetry** in a square, and describe each type."
    )
    sol = (
        "**Analysis of a Square:**\n"
        "A square has **4** lines of symmetry:\n"
        "1. Two lines passing through the midpoints of opposite sides (1 vertical, 1 horizontal).\n"
        "2. Two diagonal lines connecting opposite vertices.\n\n"
        "$$\\therefore \\text{Total lines of symmetry} = 4$$"
    )
    return {
        "id": f"g7_tg_02_{rng.randint(100000, 999999)}",
        "subskill": "02_square_lines_of_symmetry",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "4 lines of symmetry (2 mid-side lines and 2 diagonals)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_02",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Can you fold a square horizontally, vertically, and diagonally?",
            "tier_2": "Count: 1 vertical + 1 horizontal + 2 diagonals.",
            "tier_3": "A square has exactly 4 lines of symmetry."
        },
        "misconception_tags": ["missing_diagonal_symmetry_in_square"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies 4 lines of symmetry", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correctly states vertical, horizontal, and 2 diagonals", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 03. Rectangle lines of symmetry & diagonal trap
def arch_03_rectangle_lines_of_symmetry_diagonal_trap(rng: random.Random) -> Dict[str, Any]:
    l = rng.randint(8, 16)
    ans = "2"
    svg = _svg_shape_with_symmetry_line("rectangle", False, "diagonal", f"(length {l} cm)")
    prompt = (
        f"Consider a non-square rectangle (length {l} cm) shown in the diagram with a dashed red diagonal line:\n\n"
        "1. Is the diagonal line a line of symmetry for this rectangle? Explain.\n"
        "2. State the total number of lines of symmetry that a non-square rectangle has."
    )
    sol = (
        "**Step 1: Diagonal Analysis:**\n"
        "No, the diagonal of a non-square rectangle is **not** a line of symmetry. "
        "Although the diagonal divides the rectangle into two congruent triangles, "
        "folding along the diagonal causes the vertices to stick out; they do not coincide.\n\n"
        "**Step 2: Total Lines of Symmetry:**\n"
        "A rectangle has exactly **2** lines of symmetry: one vertical line through the midpoints of opposite horizontal sides, "
        "and one horizontal line through the midpoints of opposite vertical sides.\n\n"
        "$$\\therefore \\text{Total} = 2$$"
    )
    return {
        "id": f"g7_tg_03_{rng.randint(100000, 999999)}",
        "subskill": "03_rectangle_lines_of_symmetry_diagonal_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": "1. No, folding along the diagonal does not coincide; 2. 2 lines of symmetry (vertical and horizontal)",
        "sample_answer": "1. No; 2. 2 lines of symmetry",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_03",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "If you fold a standard sheet of paper diagonally, do the corners meet?",
            "tier_2": "The diagonal divides it into congruent triangles, but folding does not produce matching halves.",
            "tier_3": "Diagonal is NOT a line of symmetry. The rectangle has only 2 lines of symmetry (vertical and horizontal)."
        },
        "misconception_tags": ["rectangle_diagonal_symmetry_trap"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "States No for diagonal line", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains that folded corners do not coincide", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "States 2 lines of symmetry (vertical and horizontal)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 04. Equilateral triangle lines of symmetry
def arch_04_equilateral_triangle_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    ans = "3"
    prompt = (
        "An equilateral triangle has three sides of equal length and three interior angles of $60^\\circ$.\n\n"
        "How many lines of symmetry does an equilateral triangle have? Describe where each line passes."
    )
    sol = (
        "**Analysis of an Equilateral Triangle:**\n"
        "An equilateral triangle has **3** lines of symmetry.\n"
        "Each line of symmetry passes from one vertex perpendicular to the midpoint of the opposite side."
    )
    return {
        "id": f"g7_tg_04_{rng.randint(100000, 999999)}",
        "subskill": "04_equilateral_triangle_lines_of_symmetry",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "3 lines of symmetry (from each vertex to the midpoint of the opposite side)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_04",
        "hints": {
            "tier_1": "Since all three sides and angles are identical, each vertex can form a symmetry axis.",
            "tier_2": "3 vertices = 3 lines of symmetry.",
            "tier_3": "An equilateral triangle has 3 lines of symmetry."
        },
        "misconception_tags": ["confusing_equilateral_with_isosceles"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States 3 lines of symmetry", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identifies lines pass from vertex to opposite midpoint", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 05. Isosceles triangle lines of symmetry
def arch_05_isosceles_triangle_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(5, 14)
    ans = "1"
    svg = _svg_shape_with_symmetry_line("isosceles_triangle", True, "vertical", f"(equal sides {s} cm)")
    prompt = (
        f"The diagram below shows an isosceles triangle with two equal sides ({s} cm) and a dashed vertical line:\n\n"
        "State the number of lines of symmetry an isosceles triangle possesses, and describe where it runs."
    )
    sol = (
        "**Analysis of an Isosceles Triangle:**\n"
        "An isosceles triangle has **1** line of symmetry.\n"
        "It runs from the apex (angle between the two equal sides) perpendicular to the midpoint of the unequal base."
    )
    return {
        "id": f"g7_tg_05_{rng.randint(100000, 999999)}",
        "subskill": "05_isosceles_triangle_lines_of_symmetry",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1 line of symmetry (from apex to base midpoint)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_05",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Can you fold an isosceles triangle sideways across its non-equal sides?",
            "tier_2": "Only one fold line aligns the two equal sides.",
            "tier_3": "An isosceles triangle has exactly 1 line of symmetry."
        },
        "misconception_tags": ["overcounting_isosceles_symmetry"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States 1 line of symmetry", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Describes apex to base perpendicular bisector", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 06. Scalene triangle lines of symmetry
def arch_06_scalene_triangle_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    ans = "0"
    prompt = (
        "A scalene triangle has sides of length $5\\text{ cm}$, $7\\text{ cm}$, and $9\\text{ cm}$.\n\n"
        "How many lines of symmetry does this scalene triangle have? Justify your answer."
    )
    sol = (
        "**Analysis of a Scalene Triangle:**\n"
        "A scalene triangle has **0** (zero) lines of symmetry.\n\n"
        "**Justification:**\n"
        "All three side lengths and all three interior angles are unequal. "
        "No fold line can divide the triangle into two matching, congruent halves."
    )
    return {
        "id": f"g7_tg_06_{rng.randint(100000, 999999)}",
        "subskill": "06_scalene_triangle_lines_of_symmetry",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "0 (zero lines of symmetry because all sides and angles are unequal)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_06",
        "hints": {
            "tier_1": "A scalene triangle has no equal sides.",
            "tier_2": "Without equal sides or equal angles, folding produces no overlapping halves.",
            "tier_3": "A scalene triangle has 0 lines of symmetry."
        },
        "misconception_tags": ["assuming_all_triangles_have_symmetry"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States 0 lines of symmetry", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Justifies via unequal side lengths and angles", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 07. Parallelogram lines of symmetry
def arch_07_parallelogram_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    b = rng.randint(6, 15)
    ans = "0"
    svg = _svg_shape_with_symmetry_line("parallelogram", False, "diagonal", f"(base {b} cm)")
    prompt = (
        f"The diagram below shows a general (non-rectangular, non-rhombus) parallelogram (base {b} cm) with a diagonal line:\n\n"
        "1. Is the diagonal line a line of symmetry for the parallelogram?\n"
        "2. What is the total number of lines of symmetry in a general parallelogram?"
    )
    sol = (
        "**Step 1: Diagonal Check:**\n"
        "No, the diagonal is not a line of symmetry. Folding along the diagonal does not align the adjacent unequal sides or angles.\n\n"
        "**Step 2: Total Lines of Symmetry:**\n"
        "A general parallelogram has **0** (zero) lines of symmetry. (It has rotational symmetry of order 2, but no line symmetry)."
    )
    return {
        "id": f"g7_tg_07_{rng.randint(100000, 999999)}",
        "subskill": "07_parallelogram_lines_of_symmetry",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": "1. No; 2. 0 lines of symmetry",
        "sample_answer": "1. No; 2. 0",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_07",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Does folding a slanted box align its corners?",
            "tier_2": "A parallelogram has rotational symmetry, but no line symmetry.",
            "tier_3": "A general parallelogram has 0 lines of symmetry."
        },
        "misconception_tags": ["confusing_rotational_with_line_symmetry"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States No for diagonal", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States 0 lines of symmetry for general parallelogram", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 08. Rhombus lines of symmetry
def arch_08_rhombus_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    ans = "2"
    prompt = (
        "A rhombus is a quadrilateral with 4 equal sides and non-right angles.\n\n"
        "How many lines of symmetry does a non-square rhombus have, and where are they located?"
    )
    sol = (
        "**Analysis of a Rhombus:**\n"
        "A non-square rhombus has **2** lines of symmetry.\n"
        "They are the **two diagonals** connecting opposite vertices. The diagonals bisect each other at $90^\\circ$."
    )
    return {
        "id": f"g7_tg_08_{rng.randint(100000, 999999)}",
        "subskill": "08_rhombus_lines_of_symmetry",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "2 lines of symmetry (along the two diagonals)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_08",
        "hints": {
            "tier_1": "All four sides of a rhombus are equal.",
            "tier_2": "Unlike a rectangle, folding along the diagonals of a rhombus aligns the equal adjacent sides.",
            "tier_3": "A rhombus has 2 lines of symmetry (both diagonals)."
        },
        "misconception_tags": ["rhombus_mid_side_symmetry_trap"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies 2 lines of symmetry", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Specifies they lie along the diagonals", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 09. Kite lines of symmetry
def arch_09_kite_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    ans = "1"
    prompt = (
        "A kite is a quadrilateral with two distinct pairs of adjacent equal sides.\n\n"
        "How many lines of symmetry does a kite have, and which diagonal serves as this line?"
    )
    sol = (
        "**Analysis of a Kite:**\n"
        "A kite has exactly **1** line of symmetry.\n"
        "It is the **main diagonal** connecting the vertices between the pairs of equal sides."
    )
    return {
        "id": f"g7_tg_09_{rng.randint(100000, 999999)}",
        "subskill": "09_kite_lines_of_symmetry",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1 line of symmetry (the main diagonal between equal sides)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_09",
        "hints": {
            "tier_1": "Can you fold a kite across its shorter diagonal? No.",
            "tier_2": "Only the long diagonal folds the two matching wings together.",
            "tier_3": "A kite has 1 line of symmetry."
        },
        "misconception_tags": ["kite_two_diagonals_symmetry_trap"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States 1 line of symmetry", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identifies main diagonal as line of symmetry", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 10. Isosceles trapezium lines of symmetry
def arch_10_isosceles_trapezium_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    ans = "1"
    prompt = (
        "An isosceles trapezium has one pair of parallel sides and its non-parallel sides are equal in length.\n\n"
        "How many lines of symmetry does an isosceles trapezium have?"
    )
    sol = (
        "**Analysis of an Isosceles Trapezium:**\n"
        "An isosceles trapezium has **1** line of symmetry.\n"
        "It passes vertically through the midpoints of the two parallel bases."
    )
    return {
        "id": f"g7_tg_10_{rng.randint(100000, 999999)}",
        "subskill": "10_isosceles_trapezium_lines_of_symmetry",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1 line of symmetry (vertical line joining midpoints of parallel sides)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_10",
        "hints": {
            "tier_1": "Can it be folded vertically in half?",
            "tier_2": "The two slant legs match when folded vertically.",
            "tier_3": "An isosceles trapezium has 1 line of symmetry."
        },
        "misconception_tags": ["confusing_trapezium_types"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States 1 line of symmetry", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Describes midpoints of parallel sides", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 11. Regular hexagon lines of symmetry
def arch_11_regular_hexagon_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    ans = "6"
    prompt = (
        "A regular polygon with $n$ sides has $n$ lines of symmetry.\n\n"
        "For a **regular hexagon** ($n = 6$):\n"
        "1. How many lines of symmetry does it have?\n"
        "2. How many pass through opposite vertices, and how many pass through the midpoints of opposite sides?"
    )
    sol = (
        "**Analysis of a Regular Hexagon:**\n"
        "1. A regular hexagon has **6** lines of symmetry ($n = 6$).\n"
        "2. Breakdown:\n"
        "- **3** lines connect opposite vertices (diagonals).\n"
        "- **3** lines connect the midpoints of opposite parallel sides.\n"
        "$$\\therefore 3 + 3 = 6$$"
    )
    return {
        "id": f"g7_tg_11_{rng.randint(100000, 999999)}",
        "subskill": "11_regular_hexagon_lines_of_symmetry",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": "1. 6 lines of symmetry; 2. 3 through opposite vertices, 3 through midpoints of opposite sides",
        "sample_answer": "1. 6; 2. 3 vertex-to-vertex and 3 side-to-side",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_11",
        "hints": {
            "tier_1": "For any regular polygon, lines of symmetry = number of sides.",
            "tier_2": "A regular hexagon has 6 sides, so it has 6 lines of symmetry.",
            "tier_3": "6 lines of symmetry: 3 through vertices and 3 through midpoints of sides."
        },
        "misconception_tags": ["undercounting_polygon_symmetry"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "States 6 lines of symmetry", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identifies 3 lines through opposite vertices", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Identifies 3 lines through midpoints of opposite sides", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 12. Circle lines of symmetry
def arch_12_circle_lines_of_symmetry(rng: random.Random) -> Dict[str, Any]:
    ans = "Infinitely many"
    prompt = (
        "How many lines of symmetry does a circle have? What condition must every line of symmetry of a circle satisfy?"
    )
    sol = (
        "**Analysis of a Circle:**\n"
        "A circle has **infinitely many** lines of symmetry.\n\n"
        "**Condition:**\n"
        "Every diameter of the circle (any straight line passing through the centre of the circle) is a line of symmetry."
    )
    return {
        "id": f"g7_tg_12_{rng.randint(100000, 999999)}",
        "subskill": "12_circle_lines_of_symmetry",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": "Infinitely many (any straight line passing through the centre/diameter)",
        "sample_answer": "Infinitely many; every line passing through the center is a line of symmetry",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_12",
        "hints": {
            "tier_1": "How many diameters can you draw through the center of a circle?",
            "tier_2": "Any straight line passing through the center cuts the circle in half.",
            "tier_3": "A circle has an infinite number of lines of symmetry (any line through the center)."
        },
        "misconception_tags": ["finite_symmetry_in_circle"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States infinitely many lines of symmetry", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identifies condition: must pass through the center (diameter)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 13. Completing a symmetric figure across vertical line
def arch_13_completing_symmetric_figure_vertical_line(rng: random.Random) -> Dict[str, Any]:
    dist = rng.choice([3, 4, 5])
    y_val = rng.choice([2, 4, 6])
    ans = f"({5 + dist}; {y_val})"
    prompt = (
        f"A vertical line $x = 5$ acts as a mirror line of symmetry on a grid sheet.\n"
        f"Point $P$ has coordinates $({5 - dist}; {y_val})$ on the left of the symmetry line.\n\n"
        f"Determine the grid coordinates of the corresponding symmetric point $P'$ on the right of the line."
    )
    sol = (
        f"**Step 1: Distance from the vertical line:**\n"
        f"The mirror line is at $x = 5$.\n"
        f"Distance from $P({5 - dist}; {y_val})$ to $x = 5$ is $5 - ({5 - dist}) = {dist}$ units.\n\n"
        f"**Step 2: Calculate symmetric coordinates:**\n"
        f"- The $y$-coordinate remains unchanged: $y = {y_val}$.\n"
        f"- The $x$-coordinate is placed {dist} units to the right of $x = 5$:\n"
        f"$$x = 5 + {dist} = {5 + dist}$$\n\n"
        f"$$\\therefore P'({5 + dist}; {y_val})$$"
    )
    return {
        "id": f"g7_tg_13_{rng.randint(100000, 999999)}",
        "subskill": "13_completing_symmetric_figure_vertical_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"P'({5 + dist}; {y_val})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_13",
        "hints": {
            "tier_1": "Point P' must be the exact same distance from x = 5 on the opposite side.",
            "tier_2": f"P is {dist} units left of x=5, so P' is {dist} units right: 5 + {dist}.",
            "tier_3": f"Coordinates are ({5 + dist}; {y_val})."
        },
        "misconception_tags": ["changing_y_in_vertical_reflection"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct x-coordinate = {5 + dist}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct y-coordinate = {y_val}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 14. Completing a symmetric figure across horizontal line
def arch_14_completing_symmetric_figure_horizontal_line(rng: random.Random) -> Dict[str, Any]:
    dist = rng.choice([2, 3, 4])
    x_val = rng.choice([3, 5, 7])
    ans = f"({x_val}; {6 - dist})"
    prompt = (
        f"A horizontal line $y = 6$ is a line of symmetry on a coordinate grid.\n"
        f"Point $Q$ is located at $({x_val}; {6 + dist})$.\n\n"
        f"What are the coordinates of the transformed point $Q'$ reflected across this horizontal line?"
    )
    sol = (
        f"**Step 1: Distance from the horizontal line:**\n"
        f"The mirror line is at $y = 6$.\n"
        f"Distance from $Q$ to $y = 6$ is $({6 + dist}) - 6 = {dist}$ units above the line.\n\n"
        f"**Step 2: Reflect point:**\n"
        f"- The $x$-coordinate remains unchanged: $x = {x_val}$.\n"
        f"- The $y$-coordinate is placed {dist} units below $y = 6$:\n"
        f"$$y = 6 - {dist} = {6 - dist}$$\n\n"
        f"$$\\therefore Q'({x_val}; {6 - dist})$$"
    )
    return {
        "id": f"g7_tg_14_{rng.randint(100000, 999999)}",
        "subskill": "14_completing_symmetric_figure_horizontal_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Q'({x_val}; {6 - dist})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_14",
        "hints": {
            "tier_1": "In a horizontal reflection, the x-coordinate stays the same and y moves equidistant below the line.",
            "tier_2": f"y = 6 - {dist} = {6 - dist}.",
            "tier_3": f"Coordinates are ({x_val}; {6 - dist})."
        },
        "misconception_tags": ["changing_x_in_horizontal_reflection"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct x-coordinate = {x_val}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct y-coordinate = {6 - dist}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 15. Translation concept
def arch_15_translation_concept_and_isometry(rng: random.Random) -> Dict[str, Any]:
    ans = "A rigid slide of a figure in a specified direction and distance without turning or flipping"
    prompt = (
        "Explain what a **translation** is in geometry, and state whether the size, shape, and orientation "
        "of the shape change after a translation."
    )
    sol = (
        "**Definition:**\n"
        "A translation is a transformation that slides every point of a figure the exact same distance in the exact same direction.\n\n"
        "**Properties:**\n"
        "- **Size and shape:** Remain identical (the shape and its image are **congruent**).\n"
        "- **Orientation:** Remains unchanged (the shape does not rotate or flip)."
    )
    return {
        "id": f"g7_tg_15_{rng.randint(100000, 999999)}",
        "subskill": "15_translation_concept_and_isometry",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Slides a figure without turning or flipping; size, shape, and orientation remain unchanged",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_15",
        "hints": {
            "tier_1": "Think of pushing a book across a flat table without rotating it.",
            "tier_2": "The book slides to a new position, but it remains the exact same book facing the same way.",
            "tier_3": "Translation is a slide. Size, shape, and orientation are all preserved."
        },
        "misconception_tags": ["confusing_translation_with_rotation"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Defines translation as sliding same distance and direction", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States size, shape, and orientation remain unchanged", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 16. Translation horizontal: sliding h units right or left
def arch_16_translation_horizontal_units(rng: random.Random) -> Dict[str, Any]:
    orig_x = rng.randint(2, 6)
    orig_y = rng.randint(2, 8)
    dx = rng.choice([3, 4, 5])
    direction = rng.choice(["right", "left"])
    new_x = orig_x + dx if direction == "right" else orig_x - dx
    ans = f"({new_x}; {orig_y})"
    prompt = (
        f"Point $A({orig_x}; {orig_y})$ is translated **{dx} units to the {direction}**.\n\n"
        f"What are the coordinates of the transformed point $A'$?"
    )
    sol = (
        f"**Step 1: Horizontal Movement Rule:**\n"
        f"Translating to the {direction} affects only the $x$-coordinate:\n"
        f"$$x' = {orig_x} {'+' if direction == 'right' else '-'} {dx} = {new_x}$$\n\n"
        f"**Step 2: Vertical Coordinate:**\n"
        f"The $y$-coordinate does not change: $y' = {orig_y}$.\n\n"
        f"$$\\therefore A'({new_x}; {orig_y})$$"
    )
    return {
        "id": f"g7_tg_16_{rng.randint(100000, 999999)}",
        "subskill": "16_translation_horizontal_units",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"A'({new_x}; {orig_y})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_16",
        "hints": {
            "tier_1": "Right means add to x; left means subtract from x.",
            "tier_2": f"Calculate {orig_x} {'+' if direction == 'right' else '-'} {dx}.",
            "tier_3": f"Coordinates are ({new_x}; {orig_y})."
        },
        "misconception_tags": ["translation_sign_inversion"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct x-coordinate = {new_x}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct y-coordinate = {orig_y}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 17. Translation vertical: sliding k units up or down
def arch_17_translation_vertical_units(rng: random.Random) -> Dict[str, Any]:
    orig_x = rng.randint(2, 8)
    orig_y = rng.randint(4, 8)
    dy = rng.choice([2, 3, 4])
    direction = rng.choice(["up", "down"])
    new_y = orig_y + dy if direction == "up" else orig_y - dy
    ans = f"({orig_x}; {new_y})"
    prompt = (
        f"Point $B({orig_x}; {orig_y})$ is translated **{dy} units {direction}**.\n\n"
        f"State the coordinates of the transformed point $B'$."
    )
    sol = (
        f"**Step 1: Vertical Movement Rule:**\n"
        f"Translating {direction} affects only the $y$-coordinate:\n"
        f"$$y' = {orig_y} {'+' if direction == 'up' else '-'} {dy} = {new_y}$$\n\n"
        f"**Step 2: Horizontal Coordinate:**\n"
        f"The $x$-coordinate is unaffected: $x' = {orig_x}$.\n\n"
        f"$$\\therefore B'({orig_x}; {new_y})$$"
    )
    return {
        "id": f"g7_tg_17_{rng.randint(100000, 999999)}",
        "subskill": "17_translation_vertical_units",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"B'({orig_x}; {new_y})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_17",
        "hints": {
            "tier_1": "Up means add to y; down means subtract from y.",
            "tier_2": f"Calculate {orig_y} {'+' if direction == 'up' else '-'} {dy}.",
            "tier_3": f"Coordinates are ({orig_x}; {new_y})."
        },
        "misconception_tags": ["modifying_x_for_vertical_translation"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct x-coordinate = {orig_x}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct y-coordinate = {new_y}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 18. Translation combined: (x, y) -> (x + a, y + b) on grid
def arch_18_translation_combined_coordinate_rule(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.choice([-3, -2, 2, 3])
    x_val = rng.randint(2, 6)
    y_val = rng.randint(4, 7)
    tx = x_val + a
    ty = y_val + b
    ans = f"({tx}; {ty})"
    b_str = f"+ {b}" if b > 0 else f"- {abs(b)}"
    prompt = (
        f"A translation on a Cartesian plane is given by the coordinate mapping rule:\n"
        f"$$(x; y) \\to (x + {a}; y {b_str})$$\n\n"
        f"Apply this translation rule to find the transformed point coordinates of point $P({x_val}; {y_val})$."
    )
    sol = (
        f"**Step 1: Apply the transformation rule:**\n"
        f"- $x' = x + {a} = {x_val} + {a} = {tx}$\n"
        f"- $y' = y {b_str} = {y_val} {b_str} = {ty}$\n\n"
        f"$$\\therefore P'({tx}; {ty})$$"
    )
    return {
        "id": f"g7_tg_18_{rng.randint(100000, 999999)}",
        "subskill": "18_translation_combined_coordinate_rule",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"P'({tx}; {ty})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_18",
        "hints": {
            "tier_1": f"Substitute x = {x_val} and y = {y_val} into the rule.",
            "tier_2": f"x' = {x_val} + {a} = {tx}, and y' = {y_val} {b_str} = {ty}.",
            "tier_3": f"P'({tx}; {ty})."
        },
        "misconception_tags": ["arithmetic_error_in_translation"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates x' = {tx}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates y' = {ty}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 19. Translation coordinate calculation for single point
def arch_19_translation_point_from_description(rng: random.Random) -> Dict[str, Any]:
    orig_x = rng.randint(3, 7)
    orig_y = rng.randint(3, 7)
    dx = rng.choice([2, 3, 4])
    dy = rng.choice([2, 3, 4])
    ans_x = orig_x - dx
    ans_y = orig_y + dy
    ans = f"({ans_x}; {ans_y})"
    prompt = (
        f"Point $K({orig_x}; {orig_y})$ is translated **{dx} units left** and **{dy} units up**.\n\n"
        f"1. Write down the translation rule in the form $(x; y) \\to (\\dots ; \\dots)$.\n"
        f"2. Calculate the coordinates of the transformed point $K'$."
    )
    sol = (
        f"**Step 1: Write translation rule:**\n"
        f"Left {dx} means subtract {dx} from $x$.\n"
        f"Up {dy} means add {dy} to $y$.\n"
        f"$$(x; y) \\to (x - {dx}; y + {dy})$$\n\n"
        f"**Step 2: Calculate coordinates:**\n"
        f"$$K'({orig_x} - {dx}; {orig_y} + {dy}) = K'({ans_x}; {ans_y})$$"
    )
    return {
        "id": f"g7_tg_19_{rng.randint(100000, 999999)}",
        "subskill": "19_translation_point_from_description",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"1. (x; y) -> (x - {dx}; y + {dy}); 2. ({ans_x}; {ans_y})",
        "sample_answer": f"(x; y) -> (x - {dx}; y + {dy}) and K'({ans_x}; {ans_y})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_19",
        "hints": {
            "tier_1": "Left subtracts from x, up adds to y.",
            "tier_2": f"Rule is (x - {dx}; y + {dy}).",
            "tier_3": f"Coordinates are ({ans_x}; {ans_y})."
        },
        "misconception_tags": ["translation_sign_inversion"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"States rule (x - {dx}; y + {dy})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates x' = {ans_x}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculates y' = {ans_y}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 20. Translation coordinates of triangle vertices
def arch_20_translation_triangle_vertices(rng: random.Random) -> Dict[str, Any]:
    dx = rng.choice([3, 4])
    dy = rng.choice([2, 3])
    pts = {"A": [1, 2], "B": [4, 2], "C": [2, 5]}
    ans_pts = {k: [v[0] + dx, v[1] + dy] for k, v in pts.items()}
    ans = f"A'({ans_pts['A'][0]}; {ans_pts['A'][1]}), B'({ans_pts['B'][0]}; {ans_pts['B'][1]}), C'({ans_pts['C'][0]}; {ans_pts['C'][1]})"
    prompt = (
        f"Triangle $ABC$ has vertices at $A(1; 2)$, $B(4; 2)$, and $C(2; 5)$.\n"
        f"The triangle is translated **{dx} units right** and **{dy} units up**.\n\n"
        f"Find the coordinates of all three vertices of the transformed point triangle $A'B'C'$."
    )
    sol = (
        f"**Translation Rule:** $(x; y) \\to (x + {dx}; y + {dy})$\n\n"
        f"**Apply to each vertex:**\n"
        f"- $A'(1 + {dx}; 2 + {dy}) = A'({ans_pts['A'][0]}; {ans_pts['A'][1]})$\n"
        f"- $B'(4 + {dx}; 2 + {dy}) = B'({ans_pts['B'][0]}; {ans_pts['B'][1]})$\n"
        f"- $C'(2 + {dx}; 5 + {dy}) = C'({ans_pts['C'][0]}; {ans_pts['C'][1]})$\n\n"
        f"$$\\therefore A'({ans_pts['A'][0]}; {ans_pts['A'][1]}), B'({ans_pts['B'][0]}; {ans_pts['B'][1]}), C'({ans_pts['C'][0]}; {ans_pts['C'][1]})$$"
    )
    return {
        "id": f"g7_tg_20_{rng.randint(100000, 999999)}",
        "subskill": "20_translation_triangle_vertices",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_20",
        "hints": {
            "tier_1": f"Add {dx} to every x-coordinate and {dy} to every y-coordinate.",
            "tier_2": "Calculate for each of the three points independently.",
            "tier_3": f"{ans}"
        },
        "misconception_tags": ["translating_only_one_vertex"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct A'({ans_pts['A'][0]}; {ans_pts['A'][1]})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct B'({ans_pts['B'][0]}; {ans_pts['B'][1]})", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct C'({ans_pts['C'][0]}; {ans_pts['C'][1]})", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 21. Determining translation vector from original and image coordinates
def arch_21_determining_translation_vector(rng: random.Random) -> Dict[str, Any]:
    ox, oy = rng.randint(1, 5), rng.randint(2, 6)
    dx = rng.choice([3, 4, 5])
    dy = rng.choice([-3, -2, 2, 4])
    tx, ty = ox + dx, oy + dy
    h_dir = "right" if dx > 0 else "left"
    v_dir = "up" if dy > 0 else "down"
    ans = f"{abs(dx)} units {h_dir} and {abs(dy)} units {v_dir}"
    prompt = (
        f"An original point $M({ox}; {oy})$ is mapped onto its image $M'({tx}; {ty})$ by a single translation.\n\n"
        f"Describe the translation in words (horizontal and vertical units and directions)."
    )
    sol = (
        f"**Step 1: Horizontal change:**\n"
        f"$$\\Delta x = x' - x = {tx} - {ox} = {dx}$$\n"
        f"Since $\\Delta x = {dx}$, the point moved **{abs(dx)} units {h_dir}**.\n\n"
        f"**Step 2: Vertical change:**\n"
        f"$$\\Delta y = y' - y = {ty} - {oy} = {dy}$$\n"
        f"Since $\\Delta y = {dy}$, the point moved **{abs(dy)} units {v_dir}**.\n\n"
        f"$$\\therefore \\text{{Translation: }} {abs(dx)} \\text{{ units {h_dir} and }} {abs(dy)} \\text{{ units {v_dir}}}$$"
    )
    return {
        "id": f"g7_tg_21_{rng.randint(100000, 999999)}",
        "subskill": "21_determining_translation_vector",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_21",
        "hints": {
            "tier_1": "Find the difference between image coordinates and original coordinates: x' - x and y' - y.",
            "tier_2": f"Change in x = {tx} - {ox} = {dx}; Change in y = {ty} - {oy} = {dy}.",
            "tier_3": f"{abs(dx)} units {h_dir} and {abs(dy)} units {v_dir}."
        },
        "misconception_tags": ["calculating_original_minus_image"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct horizontal distance and direction: {abs(dx)} units {h_dir}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct vertical distance and direction: {abs(dy)} units {v_dir}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 22. Preserved properties under translation
def arch_22_preserved_properties_under_translation(rng: random.Random) -> Dict[str, Any]:
    ans = "Length of sides, size of angles, shape, area, and orientation (congruent)"
    prompt = (
        "When a geometric polygon undergoes a translation on a coordinate grid:\n\n"
        "1. List three geometric properties of the shape that are **preserved** (remain unchanged).\n"
        "2. Are the original shape and its image **congruent** or merely similar? Explain."
    )
    sol = (
        "**1. Preserved Properties:**\n"
        "- Side lengths (distances between corresponding points)\n"
        "- Interior angle sizes\n"
        "- Area and perimeter\n"
        "- Orientation (facing direction)\n\n"
        "**2. Congruence:**\n"
        "They are **congruent** because translation is an isometry (rigid transformation) that preserves both size and shape exactly."
    )
    return {
        "id": f"g7_tg_22_{rng.randint(100000, 999999)}",
        "subskill": "22_preserved_properties_under_translation",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Side lengths, angle sizes, area; they are congruent because size and shape are identical",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_22",
        "hints": {
            "tier_1": "Does sliding an object stretch it, shrink it, or change its angles?",
            "tier_2": "No, it stays exactly the same in every physical measurement.",
            "tier_3": "Side lengths, angles, and area are preserved. The figures are congruent."
        },
        "misconception_tags": ["thinking_translation_changes_size"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Lists side lengths and angles preserved", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Lists area/shape/orientation preserved", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "States congruent because size and shape are identical", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 23. Translation SVG visual representation on Cartesian grid
def arch_23_translation_svg_visual_grid(rng: random.Random) -> Dict[str, Any]:
    ox, oy = rng.randint(1, 3), rng.randint(1, 4)
    dx, dy = rng.randint(3, 5), rng.randint(2, 4)
    tx, ty = ox + dx, oy + dy
    svg = _svg_grid_translation(ox, oy, tx, ty)
    ans = f"{dx} units right and {dy} units up; ({tx}; {ty})"
    prompt = (
        "Inspect the coordinate grid diagram below showing point $A$ and its translated position $A'$:\n\n"
        f"1. Read the coordinates of original point $A$.\n"
        f"2. Read the coordinates of the transformed point $A'$.\n"
        f"3. State the translation in words."
    )
    sol = (
        f"**1. Original Point $A$:**\n"
        f"$$A({ox}; {oy})$$\n\n"
        f"**2. Image Point $A'$:**\n"
        f"$$A'({tx}; {ty})$$\n\n"
        f"**3. Translation in Words:**\n"
        f"Horizontal movement: ${tx} - {ox} = {dx}$ units right.\n"
        f"Vertical movement: ${ty} - {oy} = {dy}$ units up.\n"
        f"$$\\therefore \\text{{Translated {dx} units right and {dy} units up}}$$"
    )
    return {
        "id": f"g7_tg_23_{rng.randint(100000, 999999)}",
        "subskill": "23_translation_svg_visual_grid",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"A({ox}; {oy}), A'({tx}; {ty}), translated {dx} units right and {dy} units up",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_tg_23",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Look at the labels and follow the grid lines to the axes.",
            "tier_2": f"A is at ({ox}; {oy}) and A' is at ({tx}; {ty}).",
            "tier_3": f"{ans}"
        },
        "misconception_tags": ["reading_grid_axes_in_reverse"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Reads A({ox}; {oy})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Reads A'({tx}; {ty})", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"States {dx} units right and {dy} units up", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 24. Word problem: moving an object on a map/grid
def arch_24_word_problem_map_grid_translation(rng: random.Random) -> Dict[str, Any]:
    town_x = rng.randint(10, 20)
    town_y = rng.randint(15, 30)
    east_km = rng.choice([5, 8, 12])
    north_km = rng.choice([6, 10, 14])
    end_x = town_x + east_km
    end_y = town_y + north_km
    ans = f"({end_x}; {end_y})"
    prompt = (
        f"A game ranger starts at ranger station $S$ located at map grid coordinates $({town_x}; {town_y})$, "
        f"where 1 grid unit equals $1\\text{{ km}}$.\n"
        f"The ranger drives **{east_km}\\text{{ km}} due East** (positive $x$) and then **{north_km}\\text{{ km}} due North** (positive $y$).\n\n"
        f"What are the grid coordinates of the ranger's final location?"
    )
    sol = (
        f"**Step 1: Map compass directions to grid movements:**\n"
        f"- East corresponds to $+x$: $x' = {town_x} + {east_km} = {end_x}$\n"
        f"- North corresponds to $+y$: $y' = {town_y} + {north_km} = {end_y}$\n\n"
        f"$$\\therefore \\text{{Final location coordinates}} = ({end_x}; {end_y})$$"
    )
    return {
        "id": f"g7_tg_24_{rng.randint(100000, 999999)}",
        "subskill": "24_word_problem_map_grid_translation",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"({end_x}; {end_y})",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_24",
        "hints": {
            "tier_1": "East means right (+x); North means up (+y).",
            "tier_2": f"Add {east_km} to {town_x} and {north_km} to {town_y}.",
            "tier_3": f"Coordinates are ({end_x}; {end_y})."
        },
        "misconception_tags": ["compass_direction_mapping_confusion"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates East coordinate = {end_x}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates North coordinate = {end_y}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 25. Common error: subtracting when translating right/up or flipping coordinates
def arch_25_common_error_translation_sign_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: Subtracted 5 instead of adding 5 for rightward movement; correct coordinates are (8; 7)"
    prompt = (
        "A learner is given the following problem:\n"
        "'Point $P(3; 4)$ is translated $5$ units right and $3$ units up.'\n\n"
        "The learner writes the answer as $P'(3 - 5; 4 + 3) = P'(-2; 7)$.\n\n"
        "1. Identify the conceptual error made by the learner.\n"
        "2. Provide the correct coordinates of the transformed point point $P'$."
    )
    sol = (
        "**1. Error Identification:**\n"
        "The learner subtracted $5$ from the $x$-coordinate instead of adding $5$. "
        "Moving **right** along the horizontal axis increases values ($+5$), whereas subtracting moves to the left.\n\n"
        "**2. Correct Calculation:**\n"
        "$$x' = 3 + 5 = 8$$\n"
        "$$y' = 4 + 3 = 7$$\n\n"
        "$$\\therefore P'(8; 7)$$"
    )
    return {
        "id": f"g7_tg_25_{rng.randint(100000, 999999)}",
        "subskill": "25_common_error_translation_sign_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Subtracted instead of added for right; correct is P'(8; 7)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_tg_25",
        "hints": {
            "tier_1": "Does moving right on a number line increase or decrease numbers?",
            "tier_2": "Right is positive (+). 3 + 5 = 8.",
            "tier_3": "Learner subtracted instead of added; correct coordinates are (8; 7)."
        },
        "misconception_tags": ["translation_sign_inversion"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies subtraction instead of addition for rightward motion", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates correct coordinates (8; 7)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }
