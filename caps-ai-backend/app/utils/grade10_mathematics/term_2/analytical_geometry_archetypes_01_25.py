"""Grade 10 Mathematics — Term 2 — Analytical Geometry Archetypes 01 to 25.

Grounded strictly in CAPS Grade 10 Mathematics Term 2 Chapter 8 Analytical Geometry syllabus.
Covers:
- Cartesian plane, quadrants, coordinate plotting and reading
- Distance formula: horizontal/vertical, integer Pythagorean triples, surds, unknown coordinates, triangle classifications
- Midpoint formula: integer and fractional coordinates, finding endpoints, triangle medians, midpoint theorem
- Gradient formula: positive/negative slopes, horizontal (m=0), vertical (undefined), collinearity, parallel and perpendicular conditions

100% deterministic, zero-LLM, South African National Curriculum Standards compliant.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

TERM = 2
CAPS_WEIGHT = 15
SUGGESTED_DURATION = 8
TOPIC_ID = "grade10_math_analytical_geometry"
LEARNING_OBJECTIVE = "math10_analytical_geometry"


def _fmt_num(n: float | int) -> str:
    """Format number with SA comma decimal separator."""
    if isinstance(n, int) or (isinstance(n, float) and n.is_integer()):
        return str(int(n))
    s = f"{n:.2f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _coord(x: float | int, y: float | int) -> str:
    """Ordered pair in SA notation (semicolon separator)."""
    return f"({_fmt_num(x)};\\, {_fmt_num(y)})"


def _signed(n: int | float, space: bool = True) -> str:
    """Format signed number with plus or minus."""
    val_str = _fmt_num(abs(n))
    if n >= 0:
        return f"+ {val_str}" if space else f"+{val_str}"
    else:
        return f"- {val_str}" if space else f"-{val_str}"


def _make_svg_plane(
    points: List[Tuple[str, float, float]],
    lines: Optional[List[Tuple[str, str]]] = None,
    viewbox: str = "0 0 400 300",
    origin: Tuple[int, int] = (200, 150),
    scale: float = 16.0,
) -> str:
    """Build clean dynamic SVG for Cartesian geometry with points and segments."""
    ox, oy = origin
    svg_parts = [
        f'<svg viewBox="{viewbox}" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">',
        '<style>',
        '  .grid { stroke: #e2e8f0; stroke-width: 1; }',
        '  .axis { stroke: #1e293b; stroke-width: 1.5; }',
        '  .seg { stroke: #2563eb; stroke-width: 2; stroke-linecap: round; }',
        '  .dot { fill: #2563eb; stroke: #ffffff; stroke-width: 1.5; }',
        '  .label { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px; fill: #1e293b; font-weight: 600; }',
        '  .axis-label { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 13px; font-weight: bold; fill: #1e293b; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#f8fafc" rx="6" />',
    ]

    # Grid
    for x in range(-10, 11):
        if x != 0:
            px = ox + x * scale
            svg_parts.append(f'<line x1="{px}" y1="10" x2="{px}" y2="{oy*2 - 10}" class="grid" />')
    for y in range(-8, 9):
        if y != 0:
            py = oy - y * scale
            svg_parts.append(f'<line x1="10" y1="{py}" x2="{ox*2 - 10}" y2="{py}" class="grid" />')

    # Axes
    svg_parts.append(f'<line x1="10" y1="{oy}" x2="{ox*2 - 10}" y2="{oy}" class="axis" />')
    svg_parts.append(f'<line x1="{ox}" y1="{oy*2 - 10}" x2="{ox}" y2="10" class="axis" />')
    svg_parts.append(f'<text x="{ox*2 - 18}" y="{oy - 6}" class="axis-label">x</text>')
    svg_parts.append(f'<text x="{ox + 8}" y="22" class="axis-label">y</text>')
    svg_parts.append(f'<text x="{ox - 14}" y="{oy + 14}" class="label" font-weight="normal">O</text>')

    pt_map = {name: (ox + x * scale, oy - y * scale) for name, x, y in points}

    # Segments
    if lines:
        for p1, p2 in lines:
            if p1 in pt_map and p2 in pt_map:
                x1, y1 = pt_map[p1]
                x2, y2 = pt_map[p2]
                svg_parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="seg" />')

    # Points & labels
    for name, x, y in points:
        px, py = pt_map[name]
        svg_parts.append(f'<circle cx="{px}" cy="{py}" r="4.5" class="dot" />')
        svg_parts.append(f'<text x="{px + 7}" y="{py - 5}" class="label">{name}({int(x)}; {int(y)})</text>')

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


def _base_contract(
    subskill: str,
    prompt: str,
    answer: str,
    options: Optional[List[str]],
    sol_steps: List[Dict[str, str]],
    t1: str,
    t2: str,
    t3: str,
    misconceptions: List[str],
    marks: int = 3,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Helper to enforce universal 6-pillar contract."""
    q: Dict[str, Any] = {
        "term": TERM,
        "caps_weight_percent": CAPS_WEIGHT,
        "suggested_duration_mins": SUGGESTED_DURATION,
        "topic": TOPIC_ID,
        "learning_objective_id": LEARNING_OBJECTIVE,
        "subskill": subskill,
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "mcq" if options else "short_answer",
        "total_marks": marks,
        "misconception_tags": misconceptions,
        "hints": [
            {"tier": 1, "title": "Key Concept", "text": t1},
            {"tier": 2, "title": "Formula / Method", "text": t2},
            {"tier": 3, "title": "Worked Step", "text": t3},
        ],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp_{subskill}_{i+1}", "desc": s.get("rule", "Correct calculation step"), "marks": 1, "editable": True}
                for i, s in enumerate(sol_steps[:marks])
            ],
            "deductions": [{"rule": "sign_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "solution_steps": sol_steps,
        "sample_answer": answer,
        "worked_solution": "\n".join([f"- **Step {i+1}**: {s.get('op', '')} $\\implies$ ${s.get('to', '')}$" for i, s in enumerate(sol_steps)]),
    }
    if options:
        q["options"] = options
        q["correct_index"] = options.index(answer)
        q["options_latex"] = options
    else:
        q["answer_latex"] = answer
        q["answer_value"] = answer
    if diagram_spec:
        q["diagram_spec"] = diagram_spec
    return q


# =========================================================================== #
# Archetypes 01 to 25
# =========================================================================== #

def _build_01(rng: random.Random) -> Dict[str, Any]:
    sub = "01_cartesian_plane_quadrant_and_sign_identification"
    cases = [
        (rng.randint(2, 8), rng.randint(2, 8), "Quadrant I", "both x > 0 and y > 0"),
        (rng.randint(-8, -2), rng.randint(2, 8), "Quadrant II", "x < 0 and y > 0"),
        (rng.randint(-8, -2), rng.randint(-8, -2), "Quadrant III", "both x < 0 and y < 0"),
        (rng.randint(2, 8), rng.randint(-8, -2), "Quadrant IV", "x > 0 and y < 0"),
    ]
    px, py, quad, reason = rng.choice(cases)
    pt_name = rng.choice(["A", "B", "C", "P", "Q", "T"])
    prompt = f"Identify the quadrant in which the point ${pt_name}{_coord(px, py)}$ lies on the Cartesian plane."
    opts = ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"]
    steps = [
        {"from": f"Point {pt_name}{_coord(px, py)}", "to": f"Inspect signs: x = {px} ({'x > 0' if px>0 else 'x < 0'}), y = {py} ({'y > 0' if py>0 else 'y < 0'}).", "rule": "coordinate sign rule", "op": "analyze signs"},
        {"from": f"Sign condition: {reason}", "to": f"{quad}", "rule": "quadrant identification", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, quad, opts, steps,
        "Recall quadrant signs: QI (+; +), QII (-; +), QIII (-; -), QIV (+; -).",
        f"Examine the sign of $x = {px}$ and $y = {py}$.",
        f"Since {reason}, the point is in {quad}.",
        ["confuses_quadrant_numbering", "swaps_x_and_y_signs"],
        marks=2,
    )


def _build_02(rng: random.Random) -> Dict[str, Any]:
    sub = "02_plot_and_read_cartesian_coordinates"
    px = rng.choice([-6, -4, -2, 2, 4, 6])
    py = rng.choice([-5, -3, -1, 1, 3, 5])
    pt_label = rng.choice(["K", "M", "N", "P", "R", "S"])
    svg_diag = {
        "kind": "inline_svg",
        "svg": _make_svg_plane([(pt_label, px, py)]),
        "diagram_role": "context",
        "caption": f"Cartesian plane showing point {pt_label}.",
    }
    prompt = f"In the accompanying Cartesian diagram, read and determine the coordinates of the plotted point ${pt_label}$."
    ans = f"{_coord(px, py)}"
    opts = [
        ans,
        f"{_coord(py, px)}",
        f"{_coord(-px, py)}",
        f"{_coord(px, -py)}",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": f"Locate point {pt_label} horizontally", "to": f"Align with horizontal x-axis: x = {px}", "rule": "x-coordinate", "op": "read x"},
        {"from": f"Locate point {pt_label} vertically", "to": f"Align with vertical y-axis: y = {py}", "rule": "y-coordinate", "op": "read y"},
        {"from": "Write ordered pair", "to": ans, "rule": "ordered pair convention (x; y)", "op": "finalize"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "The first number in the coordinate pair is always the horizontal value $x$.",
        "The second number in the coordinate pair is the vertical value $y$.",
        f"Point ${pt_label}$ is at ${ans}$.",
        ["swaps_x_and_y_coordinates", "reads_wrong_axis_sign"],
        marks=2,
        diagram_spec=svg_diag,
    )


def _build_03(rng: random.Random) -> Dict[str, Any]:
    sub = "03_distance_formula_horizontal_and_vertical_lines"
    is_horiz = rng.choice([True, False])
    l1, l2 = rng.choice([("A", "B"), ("P", "Q"), ("C", "D"), ("E", "F")])
    if is_horiz:
        y_val = rng.randint(-8, 8)
        x1 = rng.randint(-9, 0)
        dist = rng.randint(4, 15)
        x2 = x1 + dist
        p1 = f"{l1}{_coord(x1, y_val)}"
        p2 = f"{l2}{_coord(x2, y_val)}"
        line_desc = "horizontal"
        calc_step = f"d = |x_2 - x_1| = |{x2} - ({x1})| = {dist}"
    else:
        x_val = rng.randint(-8, 8)
        y1 = rng.randint(-9, 0)
        dist = rng.randint(4, 15)
        y2 = y1 + dist
        p1 = f"{l1}{_coord(x_val, y1)}"
        p2 = f"{l2}{_coord(x_val, y2)}"
        line_desc = "vertical"
        calc_step = f"d = |y_2 - y_1| = |{y2} - ({y1})| = {dist}"

    prompt = f"Calculate the distance between points ${p1}$ and ${p2}$ along the {line_desc} line segment."
    ans = f"{dist} \\text{{ units}}"
    steps = [
        {"from": f"Points {p1} and {p2}", "to": f"Notice this is a {line_desc} line segment because one coordinate is identical.", "rule": f"{line_desc} segment", "op": "inspect coordinates"},
        {"from": "Distance calculation", "to": f"{calc_step} \\text{{ units}}", "rule": "1D distance", "op": "subtract coordinates"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        f"For a {line_desc} line, subtract the coordinates that differ.",
        "Distance is always positive: $d = |x_2 - x_1|$ or $d = |y_2 - y_1|$.",
        f"Distance $= {dist}$ units.",
        ["negative_distance_error", "subtraction_sign_error"],
        marks=2,
    )


def _build_04(rng: random.Random) -> Dict[str, Any]:
    sub = "04_distance_formula_integer_pythagorean_triples"
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (7, 24, 25)]
    dx, dy, d_ans = rng.choice(triples)
    if rng.choice([True, False]):
        dx, dy = dy, dx
    x1 = rng.randint(-10, 5)
    y1 = rng.randint(-10, 5)
    sx = rng.choice([-1, 1])
    sy = rng.choice([-1, 1])
    x2 = x1 + sx * dx
    y2 = y1 + sy * dy
    l1, l2 = rng.choice([("A", "B"), ("P", "Q"), ("M", "N"), ("R", "S")])
    prompt = f"Use the distance formula to calculate the exact distance between points ${l1}{_coord(x1, y1)}$ and ${l2}{_coord(x2, y2)}$."
    ans = f"{d_ans} \\text{{ units}}"
    steps = [
        {"from": f"Distance formula: d = \\sqrt{{(x_2 - x_1)^2 + (y_2 - y_1)^2}}", "to": f"d = \\sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}}", "rule": "distance formula substitution", "op": "substitute"},
        {"from": f"d = \\sqrt{{{dx}^2 + {dy}^2}}", "to": f"d = \\sqrt{{{dx**2 + dy**2}}} = \\sqrt{{{d_ans**2}}} = {d_ans}", "rule": "evaluate squares and root", "op": "evaluate"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Apply the distance formula: $d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
        f"Differences: $\\Delta x = {x2 - x1}$ and $\\Delta y = {y2 - y1}$.",
        f"$d = \\sqrt{{{dx**2} + {dy**2}}} = \\sqrt{{{d_ans**2}}} = {d_ans}$ units.",
        ["forgot_square_root", "sign_error_difference"],
        marks=3,
    )


def _build_05(rng: random.Random) -> Dict[str, Any]:
    sub = "05_distance_formula_simplest_surd_form"
    # Choose pairs where sum of squares simplifies into a surd a*sqrt(b)
    surd_specs = [
        (1, 3, 10, "1", "10"),
        (2, 4, 20, "2", "5"),
        (3, 3, 18, "3", "2"),
        (2, 6, 40, "2", "10"),
        (4, 4, 32, "4", "2"),
        (3, 6, 45, "3", "5"),
        (5, 5, 50, "5", "2"),
        (2, 8, 68, "2", "17"),
    ]
    dx, dy, total_sq, coeff, rad = rng.choice(surd_specs)
    x1 = rng.randint(-8, 5)
    y1 = rng.randint(-8, 5)
    x2 = x1 + dx
    y2 = y1 + dy
    l1, l2 = rng.choice([("A", "B"), ("P", "Q"), ("C", "D")])
    surd_ans = f"\\sqrt{{{total_sq}}}" if coeff == "1" else f"{coeff}\\sqrt{{{rad}}}"
    prompt = f"Calculate the distance between points ${l1}{_coord(x1, y1)}$ and ${l2}{_coord(x2, y2)}$. Leave your answer in simplest surd form."
    steps = [
        {"from": "Substitute coordinates into distance formula", "to": f"{l1}{l2} = \\sqrt{{({x2} - ({x1}))^2 + ({y2} - ({y1}))^2}}", "rule": "distance formula substitution", "op": "substitute"},
        {"from": f"Evaluate squares: {dx}^2 + {dy}^2", "to": f"{l1}{l2} = \\sqrt{{{dx**2} + {dy**2}}} = \\sqrt{{{total_sq}}}", "rule": "sum of squares", "op": "add squares"},
        {"from": "Simplify surd", "to": f"{l1}{l2} = {surd_ans}", "rule": "surd simplification", "op": "simplify surd"},
    ]
    return _base_contract(
        sub, prompt, surd_ans, None, steps,
        "Substitute coordinates into $d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.",
        f"Compute the sum under the radical: $\\Delta x^2 + \\Delta y^2 = {dx**2} + {dy**2} = {total_sq}$.",
        f"Simplify $\\sqrt{{{total_sq}}} = {surd_ans}$.",
        ["fails_to_simplify_surd", "arithmetic_error_squares"],
        marks=3,
    )


def _build_06(rng: random.Random) -> Dict[str, Any]:
    sub = "06_distance_formula_with_negative_coordinates"
    # Testing sign distribution when subtracting negative numbers
    x1 = rng.randint(-12, -4)
    y1 = rng.randint(3, 9)
    x2 = rng.randint(2, 8)
    y2 = rng.randint(-9, -3)
    dx = x2 - x1
    dy = y2 - y1
    dist_sq = dx**2 + dy**2
    root_val = math.isqrt(dist_sq)
    is_perf = root_val * root_val == dist_sq
    ans_tex = str(root_val) if is_perf else f"\\sqrt{{{dist_sq}}}"
    l1, l2 = rng.choice([("M", "N"), ("P", "Q"), ("A", "B")])
    prompt = f"Calculate the length of the line segment joining ${l1}{_coord(x1, y1)}$ and ${l2}{_coord(x2, y2)}$. Be careful with the negative signs."
    steps = [
        {"from": f"Subtract negative x-coordinate", "to": f"x_2 - x_1 = {x2} - ({x1}) = {x2} + {abs(x1)} = {dx}", "rule": "double negative rule", "op": "subtract x"},
        {"from": f"Subtract positive from negative y", "to": f"y_2 - y_1 = {y2} - ({y1}) = {dy}", "rule": "negative subtraction", "op": "subtract y"},
        {"from": "Distance calculation", "to": f"d = \\sqrt{{{dx}^2 + ({dy})^2}} = \\sqrt{{{dx**2} + {dy**2}}} = {ans_tex}", "rule": "evaluate distance", "op": "compute distance"},
    ]
    return _base_contract(
        sub, prompt, ans_tex, None, steps,
        "Remember that subtracting a negative number becomes addition: $x_2 - (-x_1) = x_2 + x_1$.",
        "Squaring any real difference always yields a positive number: $(-y)^2 = +y^2$.",
        f"Result: $\\sqrt{{{dx**2} + {dy**2}}} = {ans_tex}$.",
        ["sign_error_subtraction", "squares_negative_difference_to_negative"],
        marks=3,
    )


def _build_07(rng: random.Random) -> Dict[str, Any]:
    sub = "07_distance_formula_solve_unknown_coordinate"
    # Given d and points A(x1, y1), B(x, y2)
    # (x - x1)^2 + dy^2 = d^2 -> (x - x1)^2 = d^2 - dy^2 = dx^2 -> x - x1 = +/- dx
    triple = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13)])
    dx, dy, d_dist = triple
    x1 = rng.randint(-5, 5)
    y1 = rng.randint(-5, 5)
    y2 = y1 + dy
    x_pos = x1 + dx
    x_neg = x1 - dx
    prompt = f"The distance between points $A{_coord(x1, y1)}$ and $B(x;\\, {y2})$ is ${d_dist}$ units. Find all possible values of $x$."
    ans = f"x = {x_pos} \\text{{ or }} x = {x_neg}"
    steps = [
        {"from": f"Distance equation: (x - x_1)^2 + (y_2 - y_1)^2 = d^2", "to": f"(x - ({x1}))^2 + ({y2} - {y1})^2 = {d_dist}^2", "rule": "distance formula equation", "op": "substitute"},
        {"from": f"(x - ({x1}))^2 + {dy**2} = {d_dist**2}", "to": f"(x - ({x1}))^2 = {d_dist**2 - dy**2} = {dx**2}", "rule": "isolate squared term", "op": "subtract dy^2"},
        {"from": f"x - ({x1}) = \\pm {dx}", "to": ans, "rule": "square root property", "op": "solve for x"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        f"Set up the equation using $d^2 = (x - x_1)^2 + (y_2 - y_1)^2 = {d_dist**2}$.",
        f"Isolate $(x - ({x1}))^2 = {dx**2}$, then take the square root on both sides ($x - ({x1}) = \\pm {dx}$).",
        f"Values: $x = {x_pos}$ or $x = {x_neg}$.",
        ["forgets_plus_minus_solution", "arithmetic_error_squaring_d"],
        marks=3,
    )


def _build_08(rng: random.Random) -> Dict[str, Any]:
    sub = "08_collinear_points_using_distance"
    # Three points along a straight line: AB + BC = AC
    dx = rng.choice([2, 3])
    dy = rng.choice([1, 2])
    x_a = rng.randint(-6, 0)
    y_a = rng.randint(-6, 0)
    x_b = x_a + dx
    y_b = y_a + dy
    x_c = x_b + dx
    y_c = y_b + dy
    is_collinear = True
    prompt = f"Use distance calculations to determine whether the points $A{_coord(x_a, y_a)}$, $B{_coord(x_b, y_b)}$, and $C{_coord(x_c, y_c)}$ are collinear."
    ans = "Collinear; because AB + BC = AC"
    opts = [
        ans,
        "Not collinear; because AB + BC > AC",
        "Not collinear; because AB = BC",
        "Collinear; because AB + AC = BC",
    ]
    rng.shuffle(opts)
    ab_sq = dx**2 + dy**2
    ac_sq = (2*dx)**2 + (2*dy)**2
    steps = [
        {"from": f"Calculate lengths AB, BC, AC", "to": f"AB = \\sqrt{{{ab_sq}}}, \\, BC = \\sqrt{{{ab_sq}}}, \\, AC = \\sqrt{{{ac_sq}}} = 2\\sqrt{{{ab_sq}}}", "rule": "distance calculations", "op": "compute lengths"},
        {"from": f"Compare sums: AB + BC = \\sqrt{{{ab_sq}}} + \\sqrt{{{ab_sq}}} = 2\\sqrt{{{ab_sq}}} = AC", "to": ans, "rule": "collinearity condition", "op": "verify condition"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "Three points are collinear if and only if the sum of the two shorter distances equals the total distance: $AB + BC = AC$.",
        f"Check whether $AB + BC = AC$.",
        f"Conclusion: {ans}.",
        ["confuses_triangle_inequality", "misinterprets_surd_addition"],
        marks=3,
    )


def _build_09(rng: random.Random) -> Dict[str, Any]:
    sub = "09_classify_triangle_equilateral_isosceles_scalene"
    # Triangle types: Isosceles (two sides equal) or Scalene
    is_iso = rng.choice([True, False])
    if is_iso:
        # A(0, h), B(-b, 0), C(b, 0) -> AB = AC != BC
        b_val = rng.choice([3, 4, 5])
        h_val = rng.choice([4, 5, 6])
        xa, ya = 0, h_val
        xb, yb = -b_val, 0
        xc, yc = b_val, 0
        tri_type = "Isosceles triangle (two sides equal: AB = AC)"
        reason = f"AB = AC = \\sqrt{{{b_val**2 + h_val**2}}} \\text{{ and }} BC = {2*b_val}"
    else:
        # Scalene: all 3 side lengths distinct
        xa, ya = 1, 2
        xb, yb = 5, 3
        xc, yc = 2, 7
        tri_type = "Scalene triangle (all three sides have different lengths)"
        reason = "AB = \\sqrt{17}, \\, BC = \\sqrt{25} = 5, \\, AC = \\sqrt{26}"

    prompt = f"Given the vertices of $\\Delta ABC$ with $A{_coord(xa, ya)}$, $B{_coord(xb, yb)}$, and $C{_coord(xc, yc)}$, classify the triangle according to its side lengths."
    opts = [
        tri_type,
        "Equilateral triangle (all three sides equal)",
        "Isosceles triangle (two sides equal)" if not is_iso else "Scalene triangle (all sides different)",
        "Right-angled equilateral triangle",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Calculate all 3 side lengths via distance formula", "to": reason, "rule": "side length computation", "op": "compute lengths"},
        {"from": "Classify by definition", "to": tri_type, "rule": "triangle classification", "op": "classify"},
    ]
    return _base_contract(
        sub, prompt, tri_type, opts, steps,
        "Calculate the lengths of all three sides ($AB$, $BC$, $AC$) using the distance formula.",
        "Equilateral: all 3 sides equal. Isosceles: exactly 2 sides equal. Scalene: all 3 sides different.",
        f"Classification: {tri_type}.",
        ["misclassifies_triangle_type", "distance_calculation_error"],
        marks=3,
    )


def _build_10(rng: random.Random) -> Dict[str, Any]:
    sub = "10_verify_right_angled_triangle_converse_pythagoras"
    # Right-angled at B: AB^2 + BC^2 = AC^2
    # Use Pythagorean triple
    dx1, dy1 = 3, 0
    dx2, dy2 = 0, 4
    x_b = rng.randint(-4, 2)
    y_b = rng.randint(-4, 2)
    x_a = x_b + dx1
    y_a = y_b + dy1
    x_c = x_b + dx2
    y_c = y_b + dy2
    ab_sq = dx1**2 + dy1**2
    bc_sq = dx2**2 + dy2**2
    ac_sq = (x_c - x_a)**2 + (y_c - y_a)**2
    # Inline SVG sketch of triangle
    svg_diag = {
        "kind": "inline_svg",
        "svg": _make_svg_plane([("A", x_a, y_a), ("B", x_b, y_b), ("C", x_c, y_c)], [("A", "B"), ("B", "C"), ("C", "A")]),
        "diagram_role": "context",
        "caption": "Triangle ABC plotted in the Cartesian plane.",
    }
    prompt = f"In the accompanying Cartesian diagram, $\\Delta ABC$ has vertices $A{_coord(x_a, y_a)}$, $B{_coord(x_b, y_b)}$, and $C{_coord(x_c, y_c)}$. Use the converse of Pythagoras to prove whether $\\Delta ABC$ is a right-angled triangle."
    ans = f"Right-angled at B; because AB^2 + BC^2 = {ab_sq} + {bc_sq} = {ac_sq} = AC^2"
    opts = [
        ans,
        f"Not right-angled; because AB^2 + BC^2 \\neq AC^2",
        f"Right-angled at A; because BC^2 + AC^2 = AB^2",
        f"Right-angled at C; because AB^2 + AC^2 = BC^2",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Calculate squares of side lengths", "to": f"AB^2 = {ab_sq}, \\, BC^2 = {bc_sq}, \\, AC^2 = {ac_sq}", "rule": "side length squares", "op": "compute squares"},
        {"from": "Apply converse of Pythagoras", "to": f"AB^2 + BC^2 = {ab_sq} + {bc_sq} = {ac_sq} = AC^2 \\implies \\hat{{B}} = 90^\\circ", "rule": "converse of pythagoras", "op": "verify theorem"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "Calculate the square of each side length: $AB^2$, $BC^2$, and $AC^2$.",
        "Check whether the sum of the two smaller squares equals the square of the longest side ($AB^2 + BC^2 = AC^2$).",
        f"Conclusion: {ans}.",
        ["confuses_which_vertex_is_right_angled", "forgets_to_square_side_lengths"],
        marks=3,
        diagram_spec=svg_diag,
    )


def _build_11(rng: random.Random) -> Dict[str, Any]:
    sub = "11_midpoint_formula_integer_coordinates"
    # Choose endpoints such that sum is even
    x_m = rng.randint(-8, 8)
    y_m = rng.randint(-8, 8)
    dx = rng.choice([1, 2, 3, 4, 5])
    dy = rng.choice([1, 2, 3, 4, 5])
    x1, y1 = x_m - dx, y_m - dy
    x2, y2 = x_m + dx, y_m + dy
    l1, l2 = rng.choice([("A", "B"), ("P", "Q"), ("M", "N"), ("C", "D")])
    prompt = f"Calculate the coordinates of the midpoint $M$ of the line segment joining ${l1}{_coord(x1, y1)}$ and ${l2}{_coord(x2, y2)}$."
    ans = f"{_coord(x_m, y_m)}"
    steps = [
        {"from": "Midpoint formula: M = ((x_1 + x_2)/2; (y_1 + y_2)/2)", "to": f"M = \\left(\\dfrac{{{x1} + ({x2})}}{{2}};\\, \\dfrac{{{y1} + ({y2})}}{{2}}\\right)", "rule": "midpoint formula substitution", "op": "substitute"},
        {"from": "Evaluate averages", "to": f"M = \\left(\\dfrac{{{x1 + x2}}}{{2}};\\, \\dfrac{{{y1 + y2}}}{{2}}\\right) = {ans}", "rule": "simplification", "op": "evaluate coordinates"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "The midpoint formula averages the coordinates: $M = \\left(\\dfrac{x_1 + x_2}{2};\\, \\dfrac{y_1 + y_2}{2}\\right)$.",
        f"Add the $x$-values: $\\dfrac{{{x1} + ({x2})}}{{2}} = {x_m}$; add the $y$-values: $\\dfrac{{{y1} + ({y2})}}{{2}} = {y_m}$.",
        f"Midpoint: ${ans}$.",
        ["subtracts_coordinates_instead_of_adding", "divides_by_wrong_number"],
        marks=2,
    )


def _build_12(rng: random.Random) -> Dict[str, Any]:
    sub = "12_midpoint_formula_fractional_coordinates"
    # Choose endpoints where sum is odd
    x1 = rng.randint(-7, 7)
    x2 = x1 + rng.choice([1, 3, 5])
    y1 = rng.randint(-7, 7)
    y2 = y1 + rng.choice([1, 3, 5])
    sum_x = x1 + x2
    sum_y = y1 + y2
    frac_x = f"\\dfrac{{{sum_x}}}{{2}}"
    frac_y = f"\\dfrac{{{sum_y}}}{{2}}"
    ans = f"\\left({frac_x};\\, {frac_y}\\right)"
    l1, l2 = rng.choice([("A", "B"), ("P", "Q"), ("C", "D")])
    prompt = f"Determine the coordinates of the midpoint of line segment ${l1}{_coord(x1, y1)}$ and ${l2}{_coord(x2, y2)}$. Write your answer in simplest fraction form."
    steps = [
        {"from": "Substitute into midpoint formula", "to": f"M = \\left(\\dfrac{{{x1} + ({x2})}}{{2}};\\, \\dfrac{{{y1} + ({y2})}}{{2}}\\right)", "rule": "midpoint formula", "op": "substitute"},
        {"from": "Simplify fractions", "to": ans, "rule": "fractional midpoint", "op": "simplify"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Apply $M = \\left(\\dfrac{x_1 + x_2}{2};\\, \\dfrac{y_1 + y_2}{2}\\right)$.",
        f"Sum of $x$-coordinates is ${sum_x}$, and sum of $y$-coordinates is ${sum_y}$.",
        f"Midpoint: ${ans}$.",
        ["rounds_fractions_to_integers", "subtraction_error_in_midpoint"],
        marks=2,
    )


def _build_13(rng: random.Random) -> Dict[str, Any]:
    sub = "13_midpoint_formula_with_negative_coordinates"
    x1 = rng.randint(-12, -4)
    y1 = rng.randint(-10, -2)
    x2 = rng.randint(2, 10)
    y2 = rng.randint(4, 12)
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2
    xm_str = _fmt_num(xm)
    ym_str = _fmt_num(ym)
    ans = f"({xm_str};\\, {ym_str})"
    prompt = f"Find the midpoint of the line segment connecting points $A{_coord(x1, y1)}$ and $B{_coord(x2, y2)}$, paying careful attention to the signs."
    steps = [
        {"from": "Substitute coordinates with signs", "to": f"M = \\left(\\dfrac{{{x1} + ({x2})}}{{2}};\\, \\dfrac{{{y1} + ({y2})}}{{2}}\\right)", "rule": "midpoint substitution", "op": "substitute"},
        {"from": "Evaluate arithmetic", "to": f"M = \\left(\\dfrac{{{x1 + x2}}}{{2}};\\, \\dfrac{{{y1 + y2}}}{{2}}\\right) = {ans}", "rule": "arithmetic evaluation", "op": "evaluate"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Add coordinates taking their signs into account: $x_1 + x_2 = {x1} + ({x2}) = {x1 + x2}$.",
        "Divide each sum by 2.",
        f"Midpoint: ${ans}$.",
        ["sign_error_adding_negatives", "swaps_midpoint_coordinates"],
        marks=2,
    )


def _build_14(rng: random.Random) -> Dict[str, Any]:
    sub = "14_find_endpoint_given_midpoint_and_one_endpoint"
    # Given M(xm, ym) and A(x1, y1), find B(x2, y2)
    # x2 = 2*xm - x1; y2 = 2*ym - y1
    xm = rng.randint(-6, 6)
    ym = rng.randint(-6, 6)
    x1 = rng.randint(-8, 8)
    y1 = rng.randint(-8, 8)
    x2 = 2 * xm - x1
    y2 = 2 * ym - y1
    prompt = f"Point $M{_coord(xm, ym)}$ is the midpoint of line segment $AB$. If the coordinates of endpoint $A$ are ${_coord(x1, y1)}$, determine the coordinates of endpoint $B$."
    ans = f"{_coord(x2, y2)}"
    steps = [
        {"from": f"Midpoint x-formula: (x_1 + x_2)/2 = x_m", "to": f"\\dfrac{{{x1} + x_2}}{{2}} = {xm} \\implies {x1} + x_2 = {2*xm} \\implies x_2 = {2*xm} - ({x1}) = {x2}", "rule": "solve for x_2", "op": "isolate x2"},
        {"from": f"Midpoint y-formula: (y_1 + y_2)/2 = y_m", "to": f"\\dfrac{{{y1} + y_2}}{{2}} = {ym} \\implies {y1} + y_2 = {2*ym} \\implies y_2 = {2*ym} - ({y1}) = {y2}", "rule": "solve for y_2", "op": "isolate y2"},
        {"from": "Endpoint coordinates", "to": f"B{ans}", "rule": "coordinate pair", "op": "finalize"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Use the midpoint formulas: $\\dfrac{x_1 + x_2}{2} = x_m$ and $\\dfrac{y_1 + y_2}{2} = y_m$.",
        f"Multiply by 2 and solve for $x_2$ and $y_2$: $x_2 = 2({xm}) - ({x1}) = {x2}$.",
        f"Endpoint $B$ is ${ans}$.",
        ["treats_M_as_an_endpoint_and_finds_new_midpoint", "algebraic_sign_error_isolation"],
        marks=3,
    )


def _build_15(rng: random.Random) -> Dict[str, Any]:
    sub = "15_midpoint_median_of_a_triangle"
    # Triangle ABC with median from A to midpoint M of BC
    xm = rng.choice([-3, -2, -1, 0, 1, 2, 3])
    ym = rng.choice([-3, -2, -1, 0, 1, 2, 3])
    dx = rng.choice([2, 3, 4])
    dy = rng.choice([2, 3, 4])
    xb, yb = xm - dx, ym - dy
    xc, yc = xm + dx, ym + dy
    am_triples = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)]
    pdx, pdy, dist_am = rng.choice(am_triples)
    sx = rng.choice([1, -1])
    sy = rng.choice([1, -1])
    xa = xm + sx * pdx
    ya = ym + sy * pdy
    svg_diag = {
        "kind": "inline_svg",
        "svg": _make_svg_plane([("A", xa, ya), ("B", xb, yb), ("C", xc, yc), ("M", xm, ym)], [("A", "B"), ("B", "C"), ("C", "A"), ("A", "M")]),
        "diagram_role": "context",
        "caption": "Triangle ABC with median AM drawn to midpoint M of side BC.",
    }
    prompt = f"In the accompanying Cartesian diagram, the vertices of $\\Delta ABC$ are $A{_coord(xa, ya)}$, $B{_coord(xb, yb)}$, and $C{_coord(xc, yc)}$. Determine the coordinates of midpoint $M$ of side $BC$, and calculate the length of median $AM$."
    ans = f"M{_coord(xm, ym)};\\, AM = {dist_am} \\text{{ units}}"
    steps = [
        {"from": "Find midpoint M of BC", "to": f"M = \\left(\\dfrac{{{xb} + ({xc})}}{{2}};\\, \\dfrac{{{yb} + ({yc})}}{{2}}\\right) = {_coord(xm, ym)}", "rule": "midpoint calculation", "op": "compute midpoint"},
        {"from": "Calculate length AM using distance formula", "to": f"AM = \\sqrt{{({xm} - ({xa}))^2 + ({ym} - ({ya}))^2}} = \\sqrt{{{abs(xm-xa)**2 + abs(ym-ya)**2}}} = {dist_am} \\text{{ units}}", "rule": "distance calculation", "op": "compute distance"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "A median is a line segment drawn from a vertex to the midpoint of the opposite side.",
        f"Step 1: Calculate midpoint $M$ of $BC$. Step 2: Use the distance formula to find length $AM$.",
        f"Result: $M{_coord(xm, ym)}$ and $AM = {dist_am}$ units.",
        ["confuses_median_with_altitude", "calculates_distance_to_wrong_vertex"],
        marks=4,
        diagram_spec=svg_diag,
    )


def _build_16(rng: random.Random) -> Dict[str, Any]:
    sub = "16_midpoint_theorem_coordinate_proof"
    # Triangle ABC with midpoints D on AB and E on AC
    # DE = 1/2 BC and slope DE = slope BC
    xa, ya = 0, 8
    xb, yb = -6, 0
    xc, yc = 6, 0
    xd, yd = (xa + xb) / 2, (ya + yb) / 2  # (-3; 4)
    xe, ye = (xa + xc) / 2, (ya + yc) / 2  # (3; 4)
    de_len = xe - xd  # 6
    bc_len = xc - xb  # 12
    prompt = f"In $\\Delta ABC$ with $A{_coord(xa, ya)}$, $B{_coord(xb, yb)}$, and $C{_coord(xc, yc)}$, the points $D$ and $E$ are the midpoints of $AB$ and $AC$ respectively. Show that $DE = \\dfrac{1}{2}BC$ and state the geometric theorem verified."
    ans = f"DE = {int(de_len)} \\text{{ and }} BC = {int(bc_len)} \\implies DE = \\dfrac{{1}}{{2}}BC;\\, \\text{{The Midpoint Theorem}}"
    steps = [
        {"from": "Find midpoints D and E", "to": f"D{_coord(xd, yd)} \\text{{ and }} E{_coord(xe, ye)}", "rule": "midpoint formula", "op": "compute midpoints"},
        {"from": "Calculate lengths DE and BC", "to": f"DE = {int(de_len)} \\text{{ and }} BC = {int(bc_len)}", "rule": "length comparison", "op": "compute lengths"},
        {"from": "Conclude ratio", "to": ans, "rule": "midpoint theorem verification", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "The Midpoint Theorem states that the segment joining the midpoints of two sides of a triangle is parallel to the third side and half its length.",
        f"Calculate coordinates of $D$ and $E$, then compare lengths $DE$ and $BC$.",
        f"Verification: {ans}.",
        ["confuses_midpoint_theorem_with_pythagoras", "ratio_arithmetic_error"],
        marks=3,
    )


def _build_17(rng: random.Random) -> Dict[str, Any]:
    sub = "17_gradient_formula_positive_slope"
    dx = rng.choice([2, 3, 4, 5])
    dy = rng.choice([2, 3, 4, 6, 8])
    x1 = rng.randint(-8, 2)
    y1 = rng.randint(-8, 2)
    x2 = x1 + dx
    y2 = y1 + dy
    g = math.gcd(dy, dx)
    num_m = dy // g
    den_m = dx // g
    m_str = str(num_m) if den_m == 1 else f"\\dfrac{{{num_m}}}{{{den_m}}}"
    l1, l2 = rng.choice([("A", "B"), ("P", "Q"), ("C", "D")])
    prompt = f"Calculate the gradient of the line passing through points ${l1}{_coord(x1, y1)}$ and ${l2}{_coord(x2, y2)}$."
    ans = f"m = {m_str}"
    steps = [
        {"from": "Gradient formula: m = (y_2 - y_1)/(x_2 - x_1)", "to": f"m = \\dfrac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\dfrac{{{dy}}}{{{dx}}}", "rule": "gradient formula", "op": "substitute"},
        {"from": "Simplify fraction", "to": f"m = {m_str}", "rule": "fraction simplification", "op": "simplify"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Apply the gradient formula: $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$.",
        f"Vertical change $\\Delta y = {y2} - ({y1}) = {dy}$; Horizontal change $\\Delta x = {x2} - ({x1}) = {dx}$.",
        f"Gradient: $m = {m_str}$.",
        ["inverted_gradient_delta_x_over_delta_y", "sign_error_gradient"],
        marks=2,
    )


def _build_18(rng: random.Random) -> Dict[str, Any]:
    sub = "18_gradient_formula_negative_slope"
    dx = rng.choice([2, 3, 4, 5])
    dy = rng.choice([2, 3, 4, 6, 8])
    x1 = rng.randint(-8, 2)
    y1 = rng.randint(2, 10)
    x2 = x1 + dx
    y2 = y1 - dy
    g = math.gcd(dy, dx)
    num_m = dy // g
    den_m = dx // g
    m_str = f"-{num_m}" if den_m == 1 else f"-\\dfrac{{{num_m}}}{{{den_m}}}"
    l1, l2 = rng.choice([("M", "N"), ("P", "Q"), ("K", "L")])
    prompt = f"Calculate the gradient of the line passing through points ${l1}{_coord(x1, y1)}$ and ${l2}{_coord(x2, y2)}$. Explain why the gradient is negative."
    ans = f"m = {m_str}; \\text{{ negative because the line slopes downwards from left to right}}"
    steps = [
        {"from": "Gradient formula: m = (y_2 - y_1)/(x_2 - x_1)", "to": f"m = \\dfrac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\dfrac{{-{dy}}}{{{dx}}} = {m_str}", "rule": "gradient calculation", "op": "substitute"},
        {"from": "Geometric meaning", "to": "As x increases, y decreases, meaning the line slopes downwards.", "rule": "gradient sign interpretation", "op": "interpret"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Apply $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$. Take care when subtracting.",
        "A negative gradient indicates a line that slopes downwards from left to right.",
        f"Gradient: $m = {m_str}$.",
        ["omits_negative_sign_in_gradient", "swaps_numerator_and_denominator"],
        marks=2,
    )


def _build_19(rng: random.Random) -> Dict[str, Any]:
    sub = "19_gradient_zero_horizontal_line"
    y_common = rng.randint(-8, 8)
    x1 = rng.randint(-9, -1)
    x2 = rng.randint(1, 9)
    prompt = f"Calculate the gradient of the straight line passing through $P{_coord(x1, y_common)}$ and $Q{_coord(x2, y_common)}$, and describe its geometric orientation."
    ans = "m = 0; \\text{ Horizontal line}"
    opts = [
        ans,
        "m \\text{ is undefined}; \\text{ Vertical line}",
        "m = 1; \\text{ Sloping line at } 45^\\circ",
        f"m = {y_common}; \\text{{ Parallel to y-axis}}",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Gradient formula", "to": f"m = \\dfrac{{{y_common} - ({y_common})}}{{{x2} - ({x1})}} = \\dfrac{{0}}{{{x2 - x1}}} = 0", "rule": "zero numerator", "op": "evaluate fraction"},
        {"from": "Orientation", "to": "A line with gradient zero is completely flat (horizontal).", "rule": "horizontal orientation", "op": "interpret"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "When the $y$-coordinates of two points are identical, the vertical change is $\\Delta y = 0$.",
        "$\\dfrac{0}{\\Delta x} = 0$, so the line is horizontal.",
        f"Result: {ans}.",
        ["confuses_zero_gradient_with_undefined_gradient", "claims_gradient_equals_y_coordinate"],
        marks=2,
    )


def _build_20(rng: random.Random) -> Dict[str, Any]:
    sub = "20_gradient_undefined_vertical_line"
    x_common = rng.randint(-8, 8)
    y1 = rng.randint(-9, -1)
    y2 = rng.randint(1, 9)
    prompt = f"Calculate the gradient of the straight line passing through $R{_coord(x_common, y1)}$ and $S{_coord(x_common, y2)}$, and describe its geometric orientation."
    ans = "m \\text{ is undefined}; \\text{ Vertical line}"
    opts = [
        ans,
        "m = 0; \\text{ Horizontal line}",
        "m = 1; \\text{ Sloping line}",
        f"m = {x_common}; \\text{{ Parallel to x-axis}}",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Gradient formula", "to": f"m = \\dfrac{{{y2} - ({y1})}}{{{x_common} - ({x_common})}} = \\dfrac{{{y2 - y1}}}{{0}}", "rule": "zero denominator", "op": "evaluate fraction"},
        {"from": "Division by zero", "to": "Division by zero is undefined; the line is strictly vertical.", "rule": "vertical line rule", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "When the $x$-coordinates are identical, the horizontal change is $\\Delta x = 0$.",
        "Division by zero is mathematically undefined, so vertical lines have undefined gradient.",
        f"Result: {ans}.",
        ["claims_undefined_gradient_is_zero", "claims_gradient_equals_x_coordinate"],
        marks=2,
    )


def _build_21(rng: random.Random) -> Dict[str, Any]:
    sub = "21_gradient_fractional_simplification"
    # Testing proper reduction of fractions like -6/8 -> -3/4
    g = rng.choice([2, 3, 4])
    num_un = g * rng.choice([-5, -3, 3, 5])
    den_un = g * rng.choice([2, 4, 7])
    x1 = rng.randint(-5, 2)
    y1 = rng.randint(-5, 2)
    x2 = x1 + den_un
    y2 = y1 + num_un
    num_simp = num_un // g
    den_simp = den_un // g
    sign_prefix = "-" if num_simp < 0 else ""
    m_tex = f"{sign_prefix}\\dfrac{{{abs(num_simp)}}}{{{den_simp}}}"
    prompt = f"Calculate and simplify the gradient of the line connecting $A{_coord(x1, y1)}$ and $B{_coord(x2, y2)}$ to its simplest fraction form."
    ans = f"m = {m_tex}"
    steps = [
        {"from": "Compute unsimplified gradient", "to": f"m = \\dfrac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\dfrac{{{num_un}}}{{{den_un}}}", "rule": "gradient formula", "op": "substitute"},
        {"from": f"Divide numerator and denominator by HCF = {g}", "to": f"m = {m_tex}", "rule": "fraction simplification", "op": "reduce fraction"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Apply $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$.",
        f"Simplify $\\dfrac{{{num_un}}}{{{den_un}}}$ by dividing top and bottom by their highest common factor ${g}$.",
        f"Simplified gradient: $m = {m_tex}$.",
        ["fails_to_reduce_fraction_to_lowest_terms", "sign_error_in_fraction"],
        marks=2,
    )


def _build_22(rng: random.Random) -> Dict[str, Any]:
    sub = "22_collinear_points_using_gradients"
    m_val = rng.choice([-2, -1, 1, 2, 3])
    c_val = rng.randint(-5, 5)
    x_a = rng.randint(-6, -2)
    x_b = rng.randint(-1, 2)
    x_c = rng.randint(3, 7)
    y_a = m_val * x_a + c_val
    y_b = m_val * x_b + c_val
    y_c = m_val * x_c + c_val
    prompt = f"Use gradient calculations to prove whether points $A{_coord(x_a, y_a)}$, $B{_coord(x_b, y_b)}$, and $C{_coord(x_c, y_c)}$ are collinear."
    ans = f"Collinear; because m_{{AB}} = m_{{BC}} = {m_val}"
    opts = [
        ans,
        f"Not collinear; because m_{{AB}} \\neq m_{{BC}}",
        f"Collinear; because m_{{AB}} \\times m_{{BC}} = -1",
        f"Not collinear; because points are in different quadrants",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Calculate gradient m_AB", "to": f"m_{{AB}} = \\dfrac{{{y_b} - ({y_a})}}{{{x_b} - ({x_a})}} = {m_val}", "rule": "gradient AB", "op": "compute m_AB"},
        {"from": "Calculate gradient m_BC", "to": f"m_{{BC}} = \\dfrac{{{y_c} - ({y_b})}}{{{x_c} - ({x_b})}} = {m_val}", "rule": "gradient BC", "op": "compute m_BC"},
        {"from": "Compare gradients and common point B", "to": f"m_{{AB}} = m_{{BC}} = {m_val} \\text{{ with common point }} B \\implies \\text{{points are collinear}}.", "rule": "collinearity theorem", "op": "conclude"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "Points $A$, $B$, and $C$ are collinear if they lie on the same straight line, which requires $m_{AB} = m_{BC}$.",
        f"Calculate both gradients and verify that $m_{{AB}} = m_{{BC}} = {m_val}$.",
        f"Conclusion: {ans}.",
        ["confuses_collinearity_with_perpendicularity", "gradient_calculation_error"],
        marks=3,
    )


def _build_23(rng: random.Random) -> Dict[str, Any]:
    sub = "23_parallel_lines_equal_gradients"
    m = rng.choice([-4, -3, -2, 2, 3, 4])
    x1, y1 = rng.randint(-5, 0), rng.randint(-5, 0)
    x2 = x1 + rng.choice([2, 3, 4])
    y2 = y1 + m * (x2 - x1)
    # Line CD is parallel to AB: m_CD = m
    # Point C(x3, y3), D(x4, k)
    x3, y3 = rng.randint(1, 5), rng.randint(1, 5)
    dx_cd = rng.choice([2, 3, 5])
    x4 = x3 + dx_cd
    k_val = y3 + m * dx_cd
    prompt = f"Line $AB$ passes through $A{_coord(x1, y1)}$ and $B{_coord(x2, y2)}$. Line $CD$ passes through $C{_coord(x3, y3)}$ and $D({x4};\\, k)$. If line $AB$ is parallel to line $CD$, calculate the value of $k$."
    ans = f"k = {k_val}"
    steps = [
        {"from": "Calculate gradient of AB", "to": f"m_{{AB}} = \\dfrac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = {m}", "rule": "gradient AB", "op": "compute m_AB"},
        {"from": "Parallel condition: m_CD = m_AB", "to": f"\\dfrac{{k - ({y3})}}{{{x4} - ({x3})}} = {m}", "rule": "parallel condition", "op": "equate gradients"},
        {"from": f"k - ({y3}) = {m} \\times ({x4 - x3}) = {m * dx_cd}", "to": f"k = {y3} + {m * dx_cd} = {k_val}", "rule": "solve for k", "op": "isolate k"},
    ]
    return _base_contract(
        sub, prompt, ans, None, steps,
        "Parallel lines have equal gradients: $m_1 = m_2$.",
        f"Find $m_{{AB}} = {m}$, then equate $\\dfrac{{k - ({y3})}}{{{x4 - x3}}} = {m}$.",
        f"Solve for $k$: $k = {k_val}$.",
        ["uses_negative_reciprocal_instead_of_equal_gradient", "sign_error_isolating_k"],
        marks=3,
    )


def _build_24(rng: random.Random) -> Dict[str, Any]:
    sub = "24_perpendicular_lines_product_of_gradients"
    # m1 * m2 = -1
    m1 = rng.choice([-3, -2, 2, 3])
    # m2 = -1/m1
    x1, y1 = 0, 0
    x2, y2 = 1, m1
    # Line 2 through (0, 0) and (m1, -1)
    prompt = f"The line $L_1$ has a gradient of $m_1 = {m1}$. If line $L_2$ is perpendicular to $L_1$, calculate the gradient $m_2$ of line $L_2$."
    if m1 > 0:
        ans_tex = f"-\\dfrac{{1}}{{{m1}}}"
        wrong = f"\\dfrac{{1}}{{{m1}}}"
    else:
        ans_tex = f"\\dfrac{{1}}{{{abs(m1)}}}"
        wrong = f"-\\dfrac{{1}}{{{abs(m1)}}}"
    opts = [
        ans_tex,
        wrong,
        f"{m1}",
        f"-{m1}",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Perpendicular condition: m_1 * m_2 = -1", "to": f"{m1} \\times m_2 = -1", "rule": "perpendicular lines theorem", "op": "apply theorem"},
        {"from": "Solve for m_2", "to": f"m_2 = -\\dfrac{{1}}{{{m1}}} = {ans_tex}", "rule": "negative reciprocal", "op": "divide by m1"},
    ]
    return _base_contract(
        sub, prompt, ans_tex, opts, steps,
        "Two lines are perpendicular if the product of their gradients equals $-1$: $m_1 \\times m_2 = -1$.",
        f"The perpendicular gradient is the negative reciprocal of ${m1}$: $m_2 = -\\dfrac{{1}}{{{m1}}}$.",
        f"Gradient $m_2 = {ans_tex}$.",
        ["forgets_negative_sign_in_reciprocal", "takes_negative_without_reciprocal"],
        marks=2,
    )


def _build_25(rng: random.Random) -> Dict[str, Any]:
    sub = "25_verify_perpendicular_sides_in_triangle"
    # Triangle ABC right-angled at B using gradients
    m_ab = rng.choice([2, 3])
    # m_bc = -1/m_ab
    xb, yb = 1, 2
    xa, ya = xb + 1, yb + m_ab
    xc, yc = xb + m_ab, yb - 1
    # Check m_ab = (ya - yb)/(xa - xb) = m_ab / 1 = m_ab
    # Check m_bc = (yc - yb)/(xc - xb) = -1 / m_ab
    svg_diag = {
        "kind": "inline_svg",
        "svg": _make_svg_plane([("A", xa, ya), ("B", xb, yb), ("C", xc, yc)], [("A", "B"), ("B", "C"), ("C", "A")]),
        "diagram_role": "context",
        "caption": "Triangle ABC plotted with sides AB and BC.",
    }
    prompt = f"In the accompanying Cartesian diagram, $\\Delta ABC$ has vertices $A{_coord(xa, ya)}$, $B{_coord(xb, yb)}$, and $C{_coord(xc, yc)}$. Use the gradients of $AB$ and $BC$ to determine whether $\\hat{{B}} = 90^\\circ$."
    ans = f"m_{{AB}} \\times m_{{BC}} = {m_ab} \\times \\left(-\\dfrac{{1}}{{{m_ab}}}\\right) = -1 \\implies \\hat{{B}} = 90^\\circ"
    opts = [
        ans,
        f"m_{{AB}} \\times m_{{BC}} \\neq -1 \\implies \\hat{{B}} \\neq 90^\\circ",
        f"m_{{AB}} = m_{{BC}} \\implies \\text{{sides are parallel}}",
        f"m_{{AB}} + m_{{BC}} = 0 \\implies \\hat{{B}} = 90^\\circ",
    ]
    rng.shuffle(opts)
    steps = [
        {"from": "Calculate gradient m_AB", "to": f"m_{{AB}} = \\dfrac{{{ya} - ({yb})}}{{{xa} - ({xb})}} = {m_ab}", "rule": "gradient AB", "op": "compute m_AB"},
        {"from": "Calculate gradient m_BC", "to": f"m_{{BC}} = \\dfrac{{{yc} - ({yb})}}{{{xc} - ({xb})}} = -\\dfrac{{1}}{{{m_ab}}}", "rule": "gradient BC", "op": "compute m_BC"},
        {"from": "Product of gradients", "to": ans, "rule": "perpendicular gradients", "op": "multiply gradients"},
    ]
    return _base_contract(
        sub, prompt, ans, opts, steps,
        "Calculate the gradients of the two intersecting sides: $m_{AB}$ and $m_{BC}$.",
        "If $m_{AB} \\times m_{BC} = -1$, the sides are perpendicular, confirming a $90^\\circ$ angle.",
        f"Conclusion: {ans}.",
        ["adds_gradients_instead_of_multiplying", "gradient_sign_error"],
        marks=3,
        diagram_spec=svg_diag,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_cartesian_plane_quadrant_and_sign_identification": _build_01,
    "02_plot_and_read_cartesian_coordinates": _build_02,
    "03_distance_formula_horizontal_and_vertical_lines": _build_03,
    "04_distance_formula_integer_pythagorean_triples": _build_04,
    "05_distance_formula_simplest_surd_form": _build_05,
    "06_distance_formula_with_negative_coordinates": _build_06,
    "07_distance_formula_solve_unknown_coordinate": _build_07,
    "08_collinear_points_using_distance": _build_08,
    "09_classify_triangle_equilateral_isosceles_scalene": _build_09,
    "10_verify_right_angled_triangle_converse_pythagoras": _build_10,
    "11_midpoint_formula_integer_coordinates": _build_11,
    "12_midpoint_formula_fractional_coordinates": _build_12,
    "13_midpoint_formula_with_negative_coordinates": _build_13,
    "14_find_endpoint_given_midpoint_and_one_endpoint": _build_14,
    "15_midpoint_median_of_a_triangle": _build_15,
    "16_midpoint_theorem_coordinate_proof": _build_16,
    "17_gradient_formula_positive_slope": _build_17,
    "18_gradient_formula_negative_slope": _build_18,
    "19_gradient_zero_horizontal_line": _build_19,
    "20_gradient_undefined_vertical_line": _build_20,
    "21_gradient_fractional_simplification": _build_21,
    "22_collinear_points_using_gradients": _build_22,
    "23_parallel_lines_equal_gradients": _build_23,
    "24_perpendicular_lines_product_of_gradients": _build_24,
    "25_verify_perpendicular_sides_in_triangle": _build_25,
}
