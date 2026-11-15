"""Grade 10 Mathematics — Term 2/3 — Euclidean Geometry: Archetypes 01 to 25.

Grounded in curriculum_docs_auto/Mathematics_Gr10/Term 3/04. Euclidean geometry 1.md
and 04. Euclidean geometry 2.md.
Covers:
  01-05: Angles, intersections, straight lines, revolution, complementary
  06-10: Parallel lines and transversals (alternate, corresponding, co-interior, algebraic, converse)
  11-15: Triangles (interior angle sum, exterior angle theorem, isosceles, equilateral, algebraic)
  16-19: Right-angled triangles & Pythagoras (hypotenuse, leg, converse, contextual)
  20-25: Congruence (SSS, SAS, AAS, RHS, corresponding parts deduction, overlapping triangles)

100% deterministic, zero LLM, publication-grade inline SVG specs, South African comma decimals {{,}} in KaTeX.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "grade10_math_euclidean_geometry"
LO = "math10_euclidean_geometry"


def _add_pillars(
    q: Dict[str, Any],
    subskill_name: str,
    duration: int = 3,
    weight: int = 30,
) -> Dict[str, Any]:
    marks = int(q.get("marks", 2))
    schema = [
        {"criterion": "Correct geometric statement and valid theorem reason", "marks": max(1, marks - 1)},
        {"criterion": "Accurate algebraic calculation and correct final numerical value", "marks": 1},
    ]
    q.update({
        "topic": TOPIC,
        "topic_id": TOPIC,
        "subtopic_id": "euclidean_geometry",
        "grade": "10",
        "subject": "Mathematics",
        "difficulty": q.get("difficulty", "medium"),
        "mode": f"elementary_{subskill_name}",
        "term": 2,
        "caps_weight_percent": weight,
        "suggested_duration_mins": duration,
        "marking_schema": schema,
    })
    return q


# --------------------------------------------------------------------------- #
# SVG HELPER FUNCTIONS
# --------------------------------------------------------------------------- #
def _svg_wrapper(inner_elements: str, width: int = 360, height: int = 240, view_box: str = "0 0 360 240") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" width="{width}" height="{height}" '
        f'style="background:#ffffff; font-family:system-ui,-apple-system,sans-serif;">\n'
        f'{inner_elements}\n'
        f'</svg>'
    )


def _svg_angle_ray(v_x: int, v_y: int, deg: float, length: int = 120, label: str = "") -> str:
    rad = math.radians(deg)
    e_x = v_x + length * math.cos(rad)
    e_y = v_y - length * math.sin(rad)
    arrow = f'<line x1="{v_x}" y1="{v_y}" x2="{e_x:.1f}" y2="{e_y:.1f}" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>'
    lbl = ""
    if label:
        lx = v_x + (length + 15) * math.cos(rad)
        ly = v_y - (length + 15) * math.sin(rad) + 4
        lbl = f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{label}</text>'
    return f"{arrow}\n{lbl}"


# --------------------------------------------------------------------------- #
# 01_angle_classification_and_estimation
# --------------------------------------------------------------------------- #
def _build_01_angle_classification_and_estimation(r: random.Random) -> Dict[str, Any]:
    angle_types = [
        ("acute", r.randint(25, 75), "greater than 0° and less than 90°"),
        ("right", 90, "exactly equal to 90°"),
        ("obtuse", r.randint(95, 165), "greater than 90° and less than 180°"),
        ("straight", 180, "exactly equal to 180°"),
        ("reflex", r.randint(195, 330), "greater than 180° and less than 360°"),
    ]
    correct_type, angle_val, definition = r.choice(angle_types)
    distractors = [t[0] for t in angle_types if t[0] != correct_type]
    opts = [correct_type.capitalize()] + [d.capitalize() for d in r.sample(distractors, 3)]
    r.shuffle(opts)

    # Generate crisp SVG of the angle
    rad = math.radians(angle_val)
    arc_end_x = 180 + 35 * math.cos(-rad)
    arc_end_y = 150 + 35 * math.sin(-rad)
    large_arc = 1 if angle_val > 180 else 0
    svg = _svg_wrapper(
        f'<line x1="80" y1="150" x2="280" y2="150" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>\n'
        f'{_svg_angle_ray(180, 150, 0, 100, "A")}\n'
        f'{_svg_angle_ray(180, 150, angle_val, 100, "B")}\n'
        f'<circle cx="180" cy="150" r="4" fill="#0f172a"/>\n'
        f'<text x="175" y="170" font-size="13" font-weight="bold" fill="#0f172a">O</text>\n'
        f'<path d="M 215 150 A 35 35 0 {large_arc} 0 {arc_end_x:.1f} {arc_end_y:.1f}" fill="none" stroke="#2563eb" stroke-width="2"/>\n'
        f'<text x="180" y="110" font-size="14" font-weight="bold" fill="#2563eb" text-anchor="middle">{angle_val}°</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angle_val": angle_val, "vertex": "O"}

    prompt = f"In the diagram below, ray $OA$ and ray $OB$ meet at vertex $O$ to form an angle of {angle_val}$^\\circ$. Classify the type of angle $A\\hat{{O}}B$."
    corr = correct_type.capitalize()
    return _add_pillars({
        "id": f"g10_euclid_01_{r.randint(1000, 9999)}",
        "subskill": "01_angle_classification_and_estimation",
        "question_type": "mcq",
        "title": "Angle Classification and Definitions",
        "prompt": prompt,
        "question": prompt,
        "options": opts,
        "correct_answer": corr,
        "expected_answer": corr,
        "sample_answer": corr,
        "worked_solution": f"An angle measuring {angle_val}$^\\circ$ is {definition}. Therefore, $A\\hat{{O}}B$ is a {correct_type} angle.",
        "explanation": f"{angle_val}$^\\circ$ is {definition}, which defines a {correct_type} angle.",
        "marks": 1,
        "hints": {
            "tier_1": "Recall angle categories: acute (< 90°), right (= 90°), obtuse (90°–180°), straight (= 180°), reflex (180°–360°).",
            "tier_2": f"Compare {angle_val}° against the reference angles 90°, 180°, and 360°.",
            "tier_3": f"{angle_val}° falls into the {correct_type} range.",
        },
        "misconception_tags": ["confuses_obtuse_and_reflex", "confuses_acute_and_obtuse"],
        "diagram_spec": diag,
    }, "01_angle_classification_and_estimation", duration=2, weight=10)


# --------------------------------------------------------------------------- #
# 02_adjacent_angles_on_straight_line
# --------------------------------------------------------------------------- #
def _build_02_adjacent_angles_on_straight_line(r: random.Random) -> Dict[str, Any]:
    angle_a = r.randint(35, 145)
    angle_b = 180 - angle_a
    unknown_is_b = r.choice([True, False])

    svg = _svg_wrapper(
        f'<line x1="40" y1="160" x2="320" y2="160" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'{_svg_angle_ray(180, 160, angle_a, 110, "C")}\n'
        f'<circle cx="180" cy="160" r="3.5" fill="#0f172a"/>\n'
        f'<text x="40" y="185" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="180" y="185" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">B</text>\n'
        f'<text x="320" y="185" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="end">D</text>\n'
        f'<text x="225" y="145" font-size="13" font-weight="bold" fill="#2563eb">{"x" if unknown_is_b else f"{angle_b}°"}</text>\n'
        f'<text x="135" y="145" font-size="13" font-weight="bold" fill="#059669">{f"{angle_a}°" if unknown_is_b else "x"}</text>'
    )
    ans_val = angle_b if unknown_is_b else angle_a
    given_val = angle_a if unknown_is_b else angle_b
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "given_val": given_val, "line": "ABD", "vertex": "B"}

    prompt = f"In the diagram below, $ABD$ is a straight line. $B\\hat{{C}}$ forms two adjacent angles. If one angle is {given_val}$^\\circ$, calculate the value of $x$."
    opts = [f"{ans_val}^\\circ", f"{ans_val - 10}^\\circ", f"{180 - ans_val + 10}^\\circ", f"{90 - (given_val % 50)}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_02_{r.randint(1000, 9999)}",
        "subskill": "02_adjacent_angles_on_straight_line",
        "question_type": "mcq",
        "title": "Adjacent Angles on a Straight Line",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${ans_val}^\\circ$",
        "expected_answer": f"${ans_val}^\\circ$",
        "sample_answer": f"${ans_val}^\\circ$",
        "worked_solution": f"$x + {given_val}^\\circ = 180^\\circ \\quad \\text{{(angles on a straight line)}}\\\\x = 180^\\circ - {given_val}^\\circ = {ans_val}^\\circ$.",
        "explanation": f"Adjacent angles on a straight line are supplementary and sum to 180°. $180° - {given_val}° = {ans_val}°$.",
        "marks": 2,
        "hints": {
            "tier_1": "Angles on a straight line always add up to 180°.",
            "tier_2": f"Set up the equation: $x + {given_val}^\\circ = 180^\\circ$.",
            "tier_3": f"Subtract {given_val}° from 180° to obtain {ans_val}°.",
        },
        "misconception_tags": ["assumes_right_angle_sum_90", "arithmetic_subtraction_error"],
        "diagram_spec": diag,
    }, "02_adjacent_angles_on_straight_line")


# --------------------------------------------------------------------------- #
# 03_vertically_opposite_angles_intersection
# --------------------------------------------------------------------------- #
def _build_03_vertically_opposite_angles_intersection(r: random.Random) -> Dict[str, Any]:
    angle_acute = r.randint(35, 75)
    angle_obtuse = 180 - angle_acute
    pick_target = r.choice(["vert_opp", "adjacent"])

    svg = _svg_wrapper(
        f'<line x1="50" y1="60" x2="310" y2="180" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<line x1="50" y1="180" x2="310" y2="60" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<circle cx="180" cy="120" r="3.5" fill="#0f172a"/>\n'
        f'<text x="40" y="55" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="320" y="190" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="40" y="190" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="320" y="55" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="180" y="145" font-size="13" font-weight="bold" fill="#0f172a">O</text>\n'
        f'<text x="120" y="125" font-size="13" font-weight="bold" fill="#2563eb">{angle_acute}°</text>\n'
        f'<text x="240" y="125" font-size="13" font-weight="bold" fill="#dc2626">{"x" if pick_target == "vert_opp" else f"{angle_acute}°"}</text>\n'
        f'<text x="180" y="80" font-size="13" font-weight="bold" fill="#059669">{"y" if pick_target == "adjacent" else f"{angle_obtuse}°"}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angle_acute": angle_acute, "vertex": "O"}

    if pick_target == "vert_opp":
        prompt = f"In the diagram below, straight lines $AB$ and $CD$ intersect at $O$. Given $A\\hat{{O}}C = {angle_acute}^\\circ$, calculate the value of $x = D\\hat{{O}}B$."
        ans = angle_acute
        reason = "vertically opposite angles are equal"
    else:
        prompt = f"In the diagram below, straight lines $AB$ and $CD$ intersect at $O$. Given $A\\hat{{O}}C = {angle_acute}^\\circ$, calculate the value of $y = A\\hat{{O}}D$."
        ans = angle_obtuse
        reason = "adjacent angles on straight line $CD$ sum to 180°"

    opts = [f"{ans}^\\circ", f"{180 - ans}^\\circ", f"{ans + 15}^\\circ", f"{90 - (ans % 40)}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_03_{r.randint(1000, 9999)}",
        "subskill": "03_vertically_opposite_angles_intersection",
        "question_type": "mcq",
        "title": "Vertically Opposite Angles",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${ans}^\\circ$",
        "expected_answer": f"${ans}^\\circ$",
        "sample_answer": f"${ans}^\\circ$",
        "worked_solution": f"The required angle is {ans}$^\\circ$ because {reason}.",
        "explanation": f"When two lines intersect, vertically opposite angles are equal, and adjacent angles sum to 180°. Here, the angle is {ans}° ({reason}).",
        "marks": 2,
        "hints": {
            "tier_1": "Check whether the required angle is vertically opposite or adjacent on a straight line.",
            "tier_2": f"Vertically opposite angles share vertex $O$ across intersecting lines and are equal ({angle_acute}°).",
            "tier_3": f"The answer is {ans}°.",
        },
        "misconception_tags": ["confuses_vertically_opposite_with_supplementary"],
        "diagram_spec": diag,
    }, "03_vertically_opposite_angles_intersection")


# --------------------------------------------------------------------------- #
# 04_angles_around_a_point_revolution
# --------------------------------------------------------------------------- #
def _build_04_angles_around_a_point_revolution(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(60, 110)
    a2 = r.randint(70, 120)
    a3 = r.randint(50, 90)
    a4 = 360 - (a1 + a2 + a3)

    svg = _svg_wrapper(
        f'{_svg_angle_ray(180, 120, 0, 90, "P")}\n'
        f'{_svg_angle_ray(180, 120, a1, 90, "Q")}\n'
        f'{_svg_angle_ray(180, 120, a1 + a2, 90, "R")}\n'
        f'{_svg_angle_ray(180, 120, a1 + a2 + a3, 90, "S")}\n'
        f'<circle cx="180" cy="120" r="4" fill="#0f172a"/>\n'
        f'<text x="175" y="140" font-size="13" font-weight="bold" fill="#0f172a">O</text>\n'
        f'<text x="210" y="90" font-size="12" font-weight="bold" fill="#2563eb">{a1}°</text>\n'
        f'<text x="140" y="80" font-size="12" font-weight="bold" fill="#059669">{a2}°</text>\n'
        f'<text x="130" y="150" font-size="12" font-weight="bold" fill="#d97706">{a3}°</text>\n'
        f'<text x="210" y="160" font-size="13" font-weight="bold" fill="#dc2626">x</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angles": [a1, a2, a3], "vertex": "O"}

    prompt = f"In the diagram below, four angles meet around the common point $O$. Three angles measure {a1}$^\\circ$, {a2}$^\\circ$, and {a3}$^\\circ$. Calculate the value of $x$."
    opts = [f"{a4}^\\circ", f"{a4 + 10}^\\circ", f"{a4 - 10}^\\circ", f"{180 - a4}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_04_{r.randint(1000, 9999)}",
        "subskill": "04_angles_around_a_point_revolution",
        "question_type": "mcq",
        "title": "Angles at a Point (Revolution)",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${a4}^\\circ$",
        "expected_answer": f"${a4}^\\circ$",
        "sample_answer": f"${a4}^\\circ$",
        "worked_solution": f"x + {a1}^\\circ + {a2}^\\circ + {a3}^\\circ = 360^\\circ \\quad \\text{{(angles around a point)}}\\\\x + {a1+a2+a3}^\\circ = 360^\\circ \\implies x = 360^\\circ - {a1+a2+a3}^\\circ = {a4}^\\circ$.",
        "explanation": f"Angles around a single point form a complete revolution and sum to 360°. $360° - ({a1}° + {a2}° + {a3}°) = {a4}°$.",
        "marks": 2,
        "hints": {
            "tier_1": "Angles around a point make a full circle (revolution) summing to 360°.",
            "tier_2": f"Add the known angles: {a1}° + {a2}° + {a3}° = {a1+a2+a3}°.",
            "tier_3": f"Subtract from 360°: 360° - {a1+a2+a3}° = {a4}°.",
        },
        "misconception_tags": ["uses_180_instead_of_360", "addition_error_in_sum"],
        "diagram_spec": diag,
    }, "04_angles_around_a_point_revolution")


# --------------------------------------------------------------------------- #
# 05_complementary_angles_right_angle
# --------------------------------------------------------------------------- #
def _build_05_complementary_angles_right_angle(r: random.Random) -> Dict[str, Any]:
    angle_known = r.randint(22, 68)
    angle_unknown = 90 - angle_known

    svg = _svg_wrapper(
        f'<line x1="80" y1="180" x2="260" y2="180" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<line x1="80" y1="180" x2="80" y2="40" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'{_svg_angle_ray(80, 180, angle_known, 130, "B")}\n'
        f'<rect x="80" y="162" width="18" height="18" fill="none" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<circle cx="80" cy="180" r="4" fill="#0f172a"/>\n'
        f'<text x="65" y="195" font-size="13" font-weight="bold" fill="#0f172a">O</text>\n'
        f'<text x="270" y="185" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="75" y="30" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="135" y="165" font-size="13" font-weight="bold" fill="#2563eb">{angle_known}°</text>\n'
        f'<text x="105" y="125" font-size="13" font-weight="bold" fill="#059669">x</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angle_known": angle_known, "vertex": "O"}

    prompt = f"In the diagram below, $OA \\perp OC$ such that $A\\hat{{O}}C = 90^\\circ$. Ray $OB$ divides the right angle into two complementary angles. If $A\\hat{{O}}B = {angle_known}^\\circ$, calculate the value of $x = B\\hat{{O}}C$."
    opts = [f"{angle_unknown}^\\circ", f"{180 - angle_known}^\\circ", f"{angle_unknown + 5}^\\circ", f"{45}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_05_{r.randint(1000, 9999)}",
        "subskill": "05_complementary_angles_right_angle",
        "question_type": "mcq",
        "title": "Complementary Angles in a Right Angle",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${angle_unknown}^\\circ$",
        "expected_answer": f"${angle_unknown}^\\circ$",
        "sample_answer": f"${angle_unknown}^\\circ$",
        "worked_solution": f"x + {angle_known}^\\circ = 90^\\circ \\quad \\text{{(complementary angles, }} OA \\perp OC\\text{{)}}\\\\x = 90^\\circ - {angle_known}^\\circ = {angle_unknown}^\\circ$.",
        "explanation": f"Complementary angles sum to 90°. $90° - {angle_known}° = {angle_unknown}°$.",
        "marks": 2,
        "hints": {
            "tier_1": "Perpendicular lines form a 90° angle.",
            "tier_2": f"Complementary angles add to 90°: $x + {angle_known}^\\circ = 90^\\circ$.",
            "tier_3": f"Subtract: 90° - {angle_known}° = {angle_unknown}°.",
        },
        "misconception_tags": ["subtracts_from_180_instead_of_90"],
        "diagram_spec": diag,
    }, "05_complementary_angles_right_angle")


# --------------------------------------------------------------------------- #
# 06_alternate_interior_angles_parallel
# --------------------------------------------------------------------------- #
def _build_06_alternate_interior_angles_parallel(r: random.Random) -> Dict[str, Any]:
    angle_val = r.randint(42, 84)

    svg = _svg_wrapper(
        f'<line x1="40" y1="70" x2="320" y2="70" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<line x1="40" y1="170" x2="320" y2="170" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<path d="M 180 65 L 190 70 L 180 75" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<path d="M 180 165 L 190 170 L 180 175" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<line x1="100" y1="30" x2="260" y2="210" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<text x="35" y="65" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="325" y="65" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="35" y="165" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="325" y="165" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="145" y="95" font-size="13" font-weight="bold" fill="#2563eb">{angle_val}°</text>\n'
        f'<text x="195" y="160" font-size="13" font-weight="bold" fill="#059669">x</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angle_val": angle_val, "parallel_lines": ["AB", "CD"]}

    prompt = f"In the diagram below, line $AB \\parallel CD$, and transversal line $EF$ cuts both lines. If the interior alternate angle shown is {angle_val}$^\\circ$, determine the value of $x$ and state the geometric reason."
    corr = f"{angle_val}^\\circ \\text{{(alt angles, }} AB \\parallel CD\\text{{)}}"
    opts = [
        f"{angle_val}^\\circ \\text{{(alt angles, }} AB \\parallel CD\\text{{)}}",
        f"{180 - angle_val}^\\circ \\text{{(co-int angles, }} AB \\parallel CD\\text{{)}}",
        f"{angle_val}^\\circ \\text{{(corresp angles, }} AB \\parallel CD\\text{{)}}",
        f"{180 - angle_val}^\\circ \\text{{(alt angles, }} AB \\parallel CD\\text{{)}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_06_{r.randint(1000, 9999)}",
        "subskill": "06_alternate_interior_angles_parallel",
        "question_type": "mcq",
        "title": "Alternate Interior Angles on Parallel Lines",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"x = {angle_val}^\\circ \\quad \\text{{(alt angles, }} AB \\parallel CD\\text{{)}}.",
        "explanation": f"Alternate interior angles between parallel lines form a Z-pattern and are equal. Therefore, $x = {angle_val}°$.",
        "marks": 2,
        "hints": {
            "tier_1": "Look for the 'Z' shape formed between the two parallel lines and the transversal.",
            "tier_2": "Alternate interior angles are equal when lines are parallel.",
            "tier_3": f"$x = {angle_val}^\\circ$ with reason (alt $\\angle$s, $AB \\parallel CD$).",
        },
        "misconception_tags": ["confuses_alternate_with_cointerior", "omits_parallel_lines_in_reason"],
        "diagram_spec": diag,
    }, "06_alternate_interior_angles_parallel")


# --------------------------------------------------------------------------- #
# 07_corresponding_angles_parallel_f_shape
# --------------------------------------------------------------------------- #
def _build_07_corresponding_angles_parallel_f_shape(r: random.Random) -> Dict[str, Any]:
    angle_val = r.randint(45, 85)

    svg = _svg_wrapper(
        f'<line x1="40" y1="80" x2="320" y2="80" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<line x1="40" y1="170" x2="320" y2="170" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<path d="M 180 75 L 190 80 L 180 85" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<path d="M 180 165 L 190 170 L 180 175" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<line x1="80" y1="20" x2="260" y2="220" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<text x="35" y="75" font-size="13" font-weight="bold" fill="#0f172a">P</text>\n'
        f'<text x="325" y="75" font-size="13" font-weight="bold" fill="#0f172a">Q</text>\n'
        f'<text x="35" y="165" font-size="13" font-weight="bold" fill="#0f172a">R</text>\n'
        f'<text x="325" y="165" font-size="13" font-weight="bold" fill="#0f172a">S</text>\n'
        f'<text x="145" y="70" font-size="13" font-weight="bold" fill="#2563eb">{angle_val}°</text>\n'
        f'<text x="225" y="160" font-size="13" font-weight="bold" fill="#059669">x</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angle_val": angle_val, "parallel_lines": ["PQ", "RS"]}

    prompt = f"In the diagram below, line $PQ \\parallel RS$. A transversal intersects both lines at matching relative positions (an 'F' pattern). If the top corresponding angle is {angle_val}$^\\circ$, calculate $x$."
    corr = f"{angle_val}^\\circ \\text{{(corresp angles, }} PQ \\parallel RS\\text{{)}}"
    opts = [
        f"{angle_val}^\\circ \\text{{(corresp angles, }} PQ \\parallel RS\\text{{)}}",
        f"{180 - angle_val}^\\circ \\text{{(co-int angles, }} PQ \\parallel RS\\text{{)}}",
        f"{angle_val}^\\circ \\text{{(vert opp angles)}}",
        f"{180 - angle_val}^\\circ \\text{{(corresp angles, }} PQ \\parallel RS\\text{{)}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_07_{r.randint(1000, 9999)}",
        "subskill": "07_corresponding_angles_parallel_f_shape",
        "question_type": "mcq",
        "title": "Corresponding Angles on Parallel Lines",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"x = {angle_val}^\\circ \\quad \\text{{(corresp angles, }} PQ \\parallel RS\\text{{)}}.",
        "explanation": f"Corresponding angles lie in the same relative position at each intersection and are equal when lines are parallel.",
        "marks": 2,
        "hints": {
            "tier_1": "Look for the 'F' shape formed by the parallel lines and the transversal.",
            "tier_2": "Corresponding angles are equal because $PQ \\parallel RS$.",
            "tier_3": f"Therefore, $x = {angle_val}^\\circ$.",
        },
        "misconception_tags": ["confuses_corresponding_with_alternate"],
        "diagram_spec": diag,
    }, "07_corresponding_angles_parallel_f_shape")


# --------------------------------------------------------------------------- #
# 08_co_interior_angles_parallel_c_shape
# --------------------------------------------------------------------------- #
def _build_08_co_interior_angles_parallel_c_shape(r: random.Random) -> Dict[str, Any]:
    angle_known = r.randint(65, 125)
    angle_unknown = 180 - angle_known

    svg = _svg_wrapper(
        f'<line x1="40" y1="70" x2="320" y2="70" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<line x1="40" y1="170" x2="320" y2="170" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<path d="M 180 65 L 190 70 L 180 75" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<path d="M 180 165 L 190 170 L 180 175" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<line x1="120" y1="30" x2="220" y2="210" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<text x="35" y="65" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="325" y="65" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="35" y="165" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="325" y="165" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="155" y="95" font-size="13" font-weight="bold" fill="#2563eb">{angle_known}°</text>\n'
        f'<text x="185" y="160" font-size="13" font-weight="bold" fill="#059669">x</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angle_known": angle_known, "parallel_lines": ["AB", "CD"]}

    prompt = f"In the diagram below, line $AB \\parallel CD$. The two interior angles on the same side of transversal $EF$ form a 'C' (or 'U') shape. Given that one co-interior angle is {angle_known}$^\\circ$, calculate the value of $x$."
    corr = f"{angle_unknown}^\\circ"
    opts = [f"{angle_unknown}^\\circ", f"{angle_known}^\\circ", f"{angle_unknown + 15}^\\circ", f"{90 - (angle_known % 45)}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_08_{r.randint(1000, 9999)}",
        "subskill": "08_co_interior_angles_parallel_c_shape",
        "question_type": "mcq",
        "title": "Co-interior Angles on Parallel Lines",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"x + {angle_known}^\\circ = 180^\\circ \\quad \\text{{(co-int angles, }} AB \\parallel CD\\text{{)}}\\\\x = 180^\\circ - {angle_known}^\\circ = {angle_unknown}^\\circ$.",
        "explanation": f"Co-interior angles between parallel lines are supplementary and sum to 180°. $180° - {angle_known}° = {angle_unknown}°$.",
        "marks": 2,
        "hints": {
            "tier_1": "Co-interior angles lie inside the parallel lines on the same side of the transversal ('C' shape).",
            "tier_2": "Unlike alternate or corresponding angles, co-interior angles are NOT equal; they sum to 180°.",
            "tier_3": f"Calculate $180^\\circ - {angle_known}^\\circ = {angle_unknown}^\\circ$.",
        },
        "misconception_tags": ["assumes_cointerior_angles_are_equal"],
        "diagram_spec": diag,
    }, "08_co_interior_angles_parallel_c_shape")


# --------------------------------------------------------------------------- #
# 09_parallel_lines_multi_step_algebraic
# --------------------------------------------------------------------------- #
def _build_09_parallel_lines_multi_step_algebraic(r: random.Random) -> Dict[str, Any]:
    # 2x + a and 3x - b are alternate interior angles (so equal)
    x_val = r.randint(25, 45)
    c1 = 2
    c2 = 3
    # c1 * x + a = c2 * x - b  => a + b = (c2 - c1)*x = x
    a_const = r.randint(10, 20)
    b_const = x_val - a_const
    angle_deg = c1 * x_val + a_const

    svg = _svg_wrapper(
        f'<line x1="40" y1="70" x2="320" y2="70" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<line x1="40" y1="170" x2="320" y2="170" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<path d="M 180 65 L 190 70 L 180 75" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<path d="M 180 165 L 190 170 L 180 175" fill="none" stroke="#dc2626" stroke-width="2"/>\n'
        f'<line x1="100" y1="30" x2="260" y2="210" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<text x="130" y="95" font-size="12" font-weight="bold" fill="#2563eb">2x + {a_const}°</text>\n'
        f'<text x="180" y="160" font-size="12" font-weight="bold" fill="#059669">3x - {b_const}°</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "x_val": x_val, "parallel": True}

    prompt = f"In the diagram below, lines are parallel. The alternate interior angles are given by $(2x + {a_const}^\\circ)$ and $(3x - {b_const}^\\circ)$. Solve for $x$ and hence determine the angle size."
    corr = f"x = {x_val}^\\circ, \\text{{ angle}} = {angle_deg}^\\circ"
    opts = [
        f"x = {x_val}^\\circ, \\text{{ angle}} = {angle_deg}^\\circ",
        f"x = {x_val + 5}^\\circ, \\text{{ angle}} = {angle_deg + 10}^\\circ",
        f"x = {x_val - 5}^\\circ, \\text{{ angle}} = {angle_deg - 10}^\\circ",
        f"x = {x_val}^\\circ, \\text{{ angle}} = {180 - angle_deg}^\\circ",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_09_{r.randint(1000, 9999)}",
        "subskill": "09_parallel_lines_multi_step_algebraic",
        "question_type": "mcq",
        "title": "Algebraic Equation on Parallel Lines",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"3x - {b_const}^\\circ = 2x + {a_const}^\\circ \\quad \\text{{(alt angles equal)}}\\\\3x - 2x = {a_const}^\\circ + {b_const}^\\circ \\implies x = {x_val}^\\circ.\\\\2({x_val}^\\circ) + {a_const}^\\circ = {angle_deg}^\\circ.",
        "explanation": f"Equate the two alternate angles: $3x - {b_const} = 2x + {a_const} \\implies x = {x_val}$. The angle is $2({x_val}) + {a_const} = {angle_deg}°$.",
        "marks": 3,
        "hints": {
            "tier_1": "Alternate interior angles between parallel lines are equal.",
            "tier_2": f"Set up the linear equation: $3x - {b_const} = 2x + {a_const}$.",
            "tier_3": f"Solve for $x$: $x = {x_val}$, then substitute into either expression to get {angle_deg}°.",
        },
        "misconception_tags": ["adds_angles_to_180_instead_of_equating", "algebraic_sign_error"],
        "diagram_spec": diag,
    }, "09_parallel_lines_multi_step_algebraic")


# --------------------------------------------------------------------------- #
# 10_converse_parallel_lines_test
# --------------------------------------------------------------------------- #
def _build_10_converse_parallel_lines_test(r: random.Random) -> Dict[str, Any]:
    angle1 = r.randint(50, 80)
    is_parallel = r.choice([True, False])
    angle2 = angle1 if is_parallel else (angle1 + r.choice([-8, -5, 5, 8]))

    svg = _svg_wrapper(
        f'<line x1="40" y1="70" x2="320" y2="70" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<line x1="40" y1="170" x2="320" y2="170" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<line x1="100" y1="30" x2="260" y2="210" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<text x="35" y="65" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="325" y="65" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="35" y="165" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="325" y="165" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="145" y="95" font-size="13" font-weight="bold" fill="#2563eb">{angle1}°</text>\n'
        f'<text x="195" y="160" font-size="13" font-weight="bold" fill="#059669">{angle2}°</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "angle1": angle1, "angle2": angle2}

    prompt = f"In the diagram below, a transversal intersects lines $AB$ and $CD$. The alternate angles measure {angle1}$^\\circ$ and {angle2}$^\\circ$. Is line $AB \\parallel CD$? Give the correct geometric deduction."
    if is_parallel:
        corr = f"Yes, AB \\parallel CD \\text{{ because alternate angles are equal ({angle1}^\\circ = {angle2}^\\circ)}}"
        expl = f"Since the alternate angles are equal ({angle1}° = {angle2}°), the lines $AB$ and $CD$ are parallel (converse of alternate angles)."
    else:
        corr = f"No, AB \\not\\parallel CD \\text{{ because alternate angles are not equal ({angle1}^\\circ \\neq {angle2}^\\circ)}}"
        expl = f"Since the alternate angles are not equal ({angle1}° != {angle2}°), $AB$ is NOT parallel to $CD$."

    opts = [
        f"Yes, AB \\parallel CD \\text{{ because alternate angles are equal ({angle1}^\\circ = {angle2}^\\circ)}}",
        f"No, AB \\not\\parallel CD \\text{{ because alternate angles are not equal ({angle1}^\\circ \\neq {angle2}^\\circ)}}",
        f"Yes, AB \\parallel CD \\text{{ because co-interior angles sum to 180^\\circ}}",
        f"No, AB \\not\\parallel CD \\text{{ because angles are acute}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_10_{r.randint(1000, 9999)}",
        "subskill": "10_converse_parallel_lines_test",
        "question_type": "mcq",
        "title": "Converse Parallel Lines Test",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": corr,
        "explanation": expl,
        "marks": 2,
        "hints": {
            "tier_1": "To prove lines are parallel, check if alternate angles are equal, corresponding angles are equal, or co-interior angles sum to 180°.",
            "tier_2": f"Here the alternate angles are {angle1}° and {angle2}°.",
            "tier_3": f"Since {angle1}° {'=' if is_parallel else '≠'} {angle2}°, the lines {'are' if is_parallel else 'are not'} parallel.",
        },
        "misconception_tags": ["assumes_lines_parallel_without_checking_angles"],
        "diagram_spec": diag,
    }, "10_converse_parallel_lines_test")


# --------------------------------------------------------------------------- #
# 11_triangle_interior_angle_sum
# --------------------------------------------------------------------------- #
def _build_11_triangle_interior_angle_sum(r: random.Random) -> Dict[str, Any]:
    a = r.randint(35, 75)
    b = r.randint(40, 75)
    c = 180 - (a + b)

    svg = _svg_wrapper(
        f'<polygon points="180,40 60,200 300,200" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<text x="180" y="28" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>\n'
        f'<text x="45" y="215" font-size="14" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="315" y="215" font-size="14" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="180" y="70" font-size="13" font-weight="bold" fill="#2563eb" text-anchor="middle">{a}°</text>\n'
        f'<text x="95" y="190" font-size="13" font-weight="bold" fill="#059669">{b}°</text>\n'
        f'<text x="260" y="190" font-size="13" font-weight="bold" fill="#dc2626" text-anchor="middle">x</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "a": a, "b": b, "vertices": ["A", "B", "C"]}

    prompt = f"In $\\triangle ABC$ shown below, $\\hat{{A}} = {a}^\\circ$ and $\\hat{{B}} = {b}^\\circ$. Calculate the value of $x = \\hat{{C}}$."
    corr = f"{c}^\\circ"
    opts = [f"{c}^\\circ", f"{c + 10}^\\circ", f"{c - 10}^\\circ", f"{180 - c}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_11_{r.randint(1000, 9999)}",
        "subskill": "11_triangle_interior_angle_sum",
        "question_type": "mcq",
        "title": "Sum of Interior Angles of a Triangle",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\hat{{A}} + \\hat{{B}} + \\hat{{C}} = 180^\\circ \\quad \\text{{(sum of angles in }}\\triangle ABC\\text{{)}}\\\\{a}^\\circ + {b}^\\circ + x = 180^\\circ \\implies x = 180^\\circ - {a+b}^\\circ = {c}^\\circ$.",
        "explanation": f"The sum of interior angles of any triangle is 180°. $180° - ({a}° + {b}°) = {c}°$.",
        "marks": 2,
        "hints": {
            "tier_1": "The interior angles of a triangle always sum to 180°.",
            "tier_2": f"Add the two known angles: {a}° + {b}° = {a+b}°.",
            "tier_3": f"Subtract from 180°: 180° - {a+b}° = {c}°.",
        },
        "misconception_tags": ["arithmetic_addition_error", "confuses_with_quadrilateral_360"],
        "diagram_spec": diag,
    }, "11_triangle_interior_angle_sum")


# --------------------------------------------------------------------------- #
# 12_triangle_exterior_angle_theorem
# --------------------------------------------------------------------------- #
def _build_12_triangle_exterior_angle_theorem(r: random.Random) -> Dict[str, Any]:
    a = r.randint(32, 65)
    b = r.randint(45, 75)
    ext_c = a + b

    svg = _svg_wrapper(
        f'<polygon points="140,50 50,190 230,190" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="230" y1="190" x2="330" y2="190" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>\n'
        f'<text x="140" y="38" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>\n'
        f'<text x="40" y="205" font-size="14" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="225" y="205" font-size="14" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="335" y="205" font-size="14" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="140" y="80" font-size="13" font-weight="bold" fill="#2563eb" text-anchor="middle">{a}°</text>\n'
        f'<text x="85" y="180" font-size="13" font-weight="bold" fill="#059669">{b}°</text>\n'
        f'<text x="260" y="180" font-size="13" font-weight="bold" fill="#dc2626">x</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "a": a, "b": b, "ext_c": ext_c}

    prompt = f"In the diagram below, side $BC$ of $\\triangle ABC$ is extended to $D$. If $\\hat{{A}} = {a}^\\circ$ and $\\hat{{B}} = {b}^\\circ$, calculate the exterior angle $x = A\\hat{{C}}D$."
    corr = f"{ext_c}^\\circ"
    opts = [f"{ext_c}^\\circ", f"{180 - ext_c}^\\circ", f"{ext_c + 15}^\\circ", f"{180 - a}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_12_{r.randint(1000, 9999)}",
        "subskill": "12_triangle_exterior_angle_theorem",
        "question_type": "mcq",
        "title": "Exterior Angle of a Triangle Theorem",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"A\\hat{{C}}D = \\hat{{A}} + \\hat{{B}} \\quad \\text{{(ext angle of }}\\triangle ABC\\text{{)}}\\\\x = {a}^\\circ + {b}^\\circ = {ext_c}^\\circ$.",
        "explanation": f"The exterior angle of a triangle equals the sum of the two opposite interior angles: ${a}^\\circ + {b}^\\circ = {ext_c}^\\circ$.",
        "marks": 2,
        "hints": {
            "tier_1": "The exterior angle equals the sum of the two opposite interior angles.",
            "tier_2": f"Opposite interior angles are $\\hat{{A}} = {a}^\\circ$ and $\\hat{{B}} = {b}^\\circ$.",
            "tier_3": f"Add them together: {a}° + {b}° = {ext_c}°.",
        },
        "misconception_tags": ["subtracts_interior_angles", "uses_straight_line_with_wrong_angle"],
        "diagram_spec": diag,
    }, "12_triangle_exterior_angle_theorem")


# --------------------------------------------------------------------------- #
# 13_isosceles_triangle_base_angles
# --------------------------------------------------------------------------- #
def _build_13_isosceles_triangle_base_angles(r: random.Random) -> Dict[str, Any]:
    apex = r.randint(30, 80)
    base = (180 - apex) // 2
    # Ensure apex is even for integer base
    if (180 - apex) % 2 != 0:
        apex += 1
        base = (180 - apex) // 2

    svg = _svg_wrapper(
        f'<polygon points="180,40 80,200 280,200" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="125" y1="120" x2="135" y2="120" stroke="#dc2626" stroke-width="2.5"/>\n'
        f'<line x1="225" y1="120" x2="235" y2="120" stroke="#dc2626" stroke-width="2.5"/>\n'
        f'<text x="180" y="28" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>\n'
        f'<text x="65" y="215" font-size="14" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="295" y="215" font-size="14" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="180" y="70" font-size="13" font-weight="bold" fill="#2563eb" text-anchor="middle">{apex}°</text>\n'
        f'<text x="110" y="190" font-size="13" font-weight="bold" fill="#059669">x</text>\n'
        f'<text x="250" y="190" font-size="13" font-weight="bold" fill="#059669">x</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "apex": apex, "base": base, "equal_sides": ["AB", "AC"]}

    prompt = f"In the diagram below, $\\triangle ABC$ has $AB = AC$ (marked with tick marks). If the apex angle $\\hat{{A}} = {apex}^\\circ$, calculate the base angle $x = \\hat{{B}}$."
    corr = f"{base}^\\circ"
    opts = [f"{base}^\\circ", f"{180 - apex}^\\circ", f"{base + 10}^\\circ", f"{base - 10}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_13_{r.randint(1000, 9999)}",
        "subskill": "13_isosceles_triangle_base_angles",
        "question_type": "mcq",
        "title": "Isosceles Triangle Base Angles",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\hat{{B}} = \\hat{{C}} = x \\quad \\text{{(angles opp equal sides, }} AB = AC\\text{{)}}\\\\x + x + {apex}^\\circ = 180^\\circ \\implies 2x = 180^\\circ - {apex}^\\circ = {180-apex}^\\circ \\implies x = {base}^\\circ$.",
        "explanation": f"Angles opposite equal sides of a triangle are equal. Subtract the apex angle from 180° and divide by 2: $(180° - {apex}°) / 2 = {base}°$.",
        "marks": 2,
        "hints": {
            "tier_1": "An isosceles triangle has two equal sides and two equal base angles.",
            "tier_2": f"Subtract the apex angle {apex}° from 180°: {180 - apex}°.",
            "tier_3": f"Divide by 2 to find each base angle: {180 - apex}° / 2 = {base}°.",
        },
        "misconception_tags": ["forgets_to_divide_by_two", "confuses_apex_and_base"],
        "diagram_spec": diag,
    }, "13_isosceles_triangle_base_angles")


# --------------------------------------------------------------------------- #
# 14_equilateral_triangle_properties
# --------------------------------------------------------------------------- #
def _build_14_equilateral_triangle_properties(r: random.Random) -> Dict[str, Any]:
    side_len = r.randint(5, 18)
    perimeter = 3 * side_len

    svg = _svg_wrapper(
        f'<polygon points="180,40 70,200 290,200" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="120" y1="120" x2="130" y2="120" stroke="#2563eb" stroke-width="2.5"/>\n'
        f'<line x1="230" y1="120" x2="240" y2="120" stroke="#2563eb" stroke-width="2.5"/>\n'
        f'<line x1="180" y1="195" x2="180" y2="205" stroke="#2563eb" stroke-width="2.5"/>\n'
        f'<text x="180" y="28" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">P</text>\n'
        f'<text x="55" y="215" font-size="14" font-weight="bold" fill="#0f172a">Q</text>\n'
        f'<text x="305" y="215" font-size="14" font-weight="bold" fill="#0f172a">R</text>\n'
        f'<text x="110" y="110" font-size="13" font-weight="bold" fill="#2563eb">{side_len} cm</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "side_len": side_len, "type": "equilateral"}

    prompt = f"In the diagram below, $\\triangle PQR$ is equilateral with side length $PQ = {side_len}\\text{{ cm}}$. State the size of each interior angle and calculate the perimeter."
    corr = f"\\text{{Each angle }} = 60^\\circ, \\text{{ Perimeter }} = {perimeter}\\text{{ cm}}"
    opts = [
        f"\\text{{Each angle }} = 60^\\circ, \\text{{ Perimeter }} = {perimeter}\\text{{ cm}}",
        f"\\text{{Each angle }} = 90^\\circ, \\text{{ Perimeter }} = {perimeter}\\text{{ cm}}",
        f"\\text{{Each angle }} = 60^\\circ, \\text{{ Perimeter }} = {2 * side_len}\\text{{ cm}}",
        f"\\text{{Each angle }} = 45^\\circ, \\text{{ Perimeter }} = {perimeter}\\text{{ cm}}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_14_{r.randint(1000, 9999)}",
        "subskill": "14_equilateral_triangle_properties",
        "question_type": "mcq",
        "title": "Equilateral Triangle Properties",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{In an equilateral triangle, all three sides are equal and all three interior angles are equal:}}\\\\180^\\circ / 3 = 60^\\circ.\\\\text{{Perimeter}} = 3 \\times {side_len}\\text{{ cm}} = {perimeter}\\text{{ cm}}.",
        "explanation": f"An equilateral triangle has three equal angles of 60° and three equal sides, giving perimeter $3 \\times {side_len} = {perimeter}$ cm.",
        "marks": 2,
        "hints": {
            "tier_1": "All three sides and all three angles of an equilateral triangle are equal.",
            "tier_2": "Divide 180° by 3 to find each interior angle.",
            "tier_3": f"Perimeter is $3 \\times {side_len} = {perimeter}$ cm.",
        },
        "misconception_tags": ["confuses_equilateral_with_isosceles"],
        "diagram_spec": diag,
    }, "14_equilateral_triangle_properties")


# --------------------------------------------------------------------------- #
# 15_isosceles_triangle_algebraic_solve
# --------------------------------------------------------------------------- #
def _build_15_isosceles_triangle_algebraic_solve(r: random.Random) -> Dict[str, Any]:
    x_val = r.randint(15, 35)
    # Base angles are 2x + 10, apex is 180 - 2*(2x + 10) = 160 - 4x
    apex = 180 - 2 * (2 * x_val + 10)
    base_deg = 2 * x_val + 10

    svg = _svg_wrapper(
        f'<polygon points="180,40 70,200 290,200" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="120" y1="120" x2="130" y2="120" stroke="#dc2626" stroke-width="2.5"/>\n'
        f'<line x1="230" y1="120" x2="240" y2="120" stroke="#dc2626" stroke-width="2.5"/>\n'
        f'<text x="180" y="28" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>\n'
        f'<text x="55" y="215" font-size="14" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="305" y="215" font-size="14" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="180" y="75" font-size="13" font-weight="bold" fill="#2563eb" text-anchor="middle">{apex}°</text>\n'
        f'<text x="110" y="190" font-size="12" font-weight="bold" fill="#059669">2x + 10°</text>\n'
        f'<text x="250" y="190" font-size="12" font-weight="bold" fill="#059669">2x + 10°</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "apex": apex, "x_val": x_val}

    prompt = f"In the diagram below, $\\triangle ABC$ is isosceles with $AB = AC$. The base angles are given as $(2x + 10^\\circ)$ each, and the apex angle is {apex}$^\\circ$. Solve for $x$."
    corr = f"x = {x_val}^\\circ"
    opts = [f"x = {x_val}^\\circ", f"x = {x_val + 5}^\\circ", f"x = {x_val - 5}^\\circ", f"x = {base_deg}^\\circ"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_15_{r.randint(1000, 9999)}",
        "subskill": "15_isosceles_triangle_algebraic_solve",
        "question_type": "mcq",
        "title": "Algebraic Equation in an Isosceles Triangle",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"2(2x + 10^\\circ) + {apex}^\\circ = 180^\\circ \\quad \\text{{(sum of angles in }}\\triangle ABC\\text{{)}}\\\\4x + 20^\\circ + {apex}^\\circ = 180^\\circ \\implies 4x = 180^\\circ - {20+apex}^\\circ = {4*x_val}^\\circ \\implies x = {x_val}^\\circ.",
        "explanation": f"Set the sum of all three angles to 180°: $2(2x + 10) + {apex} = 180 \\implies 4x = {4*x_val} \\implies x = {x_val}$.",
        "marks": 3,
        "hints": {
            "tier_1": "Sum of all three angles in the triangle is 180°.",
            "tier_2": f"Write the equation: $(2x + 10^\\circ) + (2x + 10^\\circ) + {apex}^\\circ = 180^\\circ$.",
            "tier_3": f"Simplify: $4x + {20+apex}^\\circ = 180^\\circ \\implies 4x = {4*x_val}^\\circ \\implies x = {x_val}^\\circ$.",
        },
        "misconception_tags": ["forgets_both_base_angles_equal", "distributive_law_error"],
        "diagram_spec": diag,
    }, "15_isosceles_triangle_algebraic_solve")


# --------------------------------------------------------------------------- #
# 16_pythagoras_calculate_hypotenuse
# --------------------------------------------------------------------------- #
def _build_16_pythagoras_calculate_hypotenuse(r: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (7, 24, 25), (9, 12, 15)]
    a, b, c = r.choice(triples)
    scale = r.choice([1, 2])
    a, b, c = a * scale, b * scale, c * scale

    svg = _svg_wrapper(
        f'<polygon points="80,180 260,180 80,60" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<rect x="80" y="162" width="18" height="18" fill="none" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<text x="65" y="195" font-size="14" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="275" y="195" font-size="14" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="65" y="55" font-size="14" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="50" y="125" font-size="13" font-weight="bold" fill="#2563eb">{a}</text>\n'
        f'<text x="170" y="200" font-size="13" font-weight="bold" fill="#059669">{b}</text>\n'
        f'<text x="180" y="110" font-size="13" font-weight="bold" fill="#dc2626">c</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "a": a, "b": b, "hyp": c}

    prompt = f"In the right-angled triangle $\\triangle ABC$ shown below ($\\,\\hat{{B}} = 90^\\circ$), side $AB = {a}$ and side $BC = {b}$. Calculate the length of the hypotenuse $AC = c$."
    corr = f"{c}"
    opts = [f"{c}", f"{a + b}", f"{int(math.sqrt(a**2 + b**2)) + 2}", f"{c - 1}"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_16_{r.randint(1000, 9999)}",
        "subskill": "16_pythagoras_calculate_hypotenuse",
        "question_type": "mcq",
        "title": "Pythagoras Theorem: Calculate Hypotenuse",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"AC^2 = AB^2 + BC^2 \\quad \\text{{(Theorem of Pythagoras)}}\\\\c^2 = {a}^2 + {b}^2 = {a**2} + {b**2} = {c**2}\\\\c = \\sqrt{{{c**2}}} = {c}.",
        "explanation": f"According to Pythagoras' Theorem in a right triangle, the square of the hypotenuse equals the sum of the squares of the other two sides: $c = \\sqrt{{{a}^2 + {b}^2}} = {c}$.",
        "marks": 2,
        "hints": {
            "tier_1": "Apply the Theorem of Pythagoras: $c^2 = a^2 + b^2$.",
            "tier_2": f"Substitute the known legs: $c^2 = {a}^2 + {b}^2 = {a**2} + {b**2} = {c**2}$.",
            "tier_3": f"Take the square root: $\\sqrt{{{c**2}}} = {c}$.",
        },
        "misconception_tags": ["adds_lengths_without_squaring", "forgets_square_root"],
        "diagram_spec": diag,
    }, "16_pythagoras_calculate_hypotenuse")


# --------------------------------------------------------------------------- #
# 17_pythagoras_calculate_shorter_side
# --------------------------------------------------------------------------- #
def _build_17_pythagoras_calculate_shorter_side(r: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)]
    a, b, c = r.choice(triples)
    scale = r.choice([1, 2])
    a, b, c = a * scale, b * scale, c * scale

    svg = _svg_wrapper(
        f'<polygon points="80,180 260,180 80,60" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<rect x="80" y="162" width="18" height="18" fill="none" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<text x="65" y="195" font-size="14" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="275" y="195" font-size="14" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="65" y="55" font-size="14" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="50" y="125" font-size="13" font-weight="bold" fill="#dc2626">x</text>\n'
        f'<text x="170" y="200" font-size="13" font-weight="bold" fill="#059669">{b}</text>\n'
        f'<text x="180" y="110" font-size="13" font-weight="bold" fill="#2563eb">{c}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "hyp": c, "b": b, "leg": a}

    prompt = f"In right-angled triangle $\\triangle ABC$ below ($\\hat{{B}} = 90^\\circ$), hypotenuse $AC = {c}$ and base $BC = {b}$. Calculate the length of the unknown side $AB = x$."
    corr = f"{a}"
    opts = [f"{a}", f"{c - b}", f"{int(math.sqrt(c**2 + b**2))}", f"{a + 2}"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_17_{r.randint(1000, 9999)}",
        "subskill": "17_pythagoras_calculate_shorter_side",
        "question_type": "mcq",
        "title": "Pythagoras Theorem: Calculate Shorter Side",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"AB^2 = AC^2 - BC^2 \\quad \\text{{(Theorem of Pythagoras)}}\\\\x^2 = {c}^2 - {b}^2 = {c**2} - {b**2} = {a**2}\\\\x = \\sqrt{{{a**2}}} = {a}.",
        "explanation": f"To find a shorter side, subtract the square of the known leg from the square of the hypotenuse: $x = \\sqrt{{{c}^2 - {b}^2}} = {a}$.",
        "marks": 2,
        "hints": {
            "tier_1": "Rearrange Pythagoras to find a leg: $x^2 = c^2 - b^2$.",
            "tier_2": f"Substitute: $x^2 = {c}^2 - {b}^2 = {c**2} - {b**2} = {a**2}$.",
            "tier_3": f"Take the square root: $\\sqrt{{{a**2}}} = {a}$.",
        },
        "misconception_tags": ["adds_instead_of_subtracting_for_leg", "subtracts_without_squaring"],
        "diagram_spec": diag,
    }, "17_pythagoras_calculate_shorter_side")


# --------------------------------------------------------------------------- #
# 18_converse_pythagoras_triangle_test
# --------------------------------------------------------------------------- #
def _build_18_converse_pythagoras_triangle_test(r: random.Random) -> Dict[str, Any]:
    cases = [
        ((6, 8, 10), True, "right-angled", "6^2 + 8^2 = 36 + 64 = 100 = 10^2"),
        ((5, 12, 13), True, "right-angled", "5^2 + 12^2 = 25 + 144 = 169 = 13^2"),
        ((4, 5, 7), False, "obtuse-angled", "4^2 + 5^2 = 16 + 25 = 41 < 7^2 = 49"),
        ((6, 7, 8), False, "acute-angled", "6^2 + 7^2 = 36 + 49 = 85 > 8^2 = 64"),
    ]
    sides, is_right, tri_type, calc_str = r.choice(cases)
    a, b, c = sides

    svg = _svg_wrapper(
        f'<polygon points="90,170 270,170 120,60" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>\n'
        f'<text x="80" y="185" font-size="14" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="280" y="185" font-size="14" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="115" y="45" font-size="14" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="90" y="110" font-size="13" font-weight="bold" fill="#2563eb">{a}</text>\n'
        f'<text x="180" y="190" font-size="13" font-weight="bold" fill="#059669">{c}</text>\n'
        f'<text x="210" y="110" font-size="13" font-weight="bold" fill="#dc2626">{b}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "sides": [a, b, c], "tri_type": tri_type}

    prompt = f"A triangle has side lengths {a}, {b}, and {c}. Use the converse of the Theorem of Pythagoras to determine whether the triangle is right-angled, acute-angled, or obtuse-angled."
    corr = f"{tri_type.capitalize()} (since {calc_str})"
    opts = [
        f"Right-angled (since {a}^2 + {b}^2 = {c}^2)",
        f"Obtuse-angled (since {a}^2 + {b}^2 < {c}^2)",
        f"Acute-angled (since {a}^2 + {b}^2 > {c}^2)",
        f"Equilateral (since all sides are integer lengths)",
    ]
    if corr not in opts:
        opts[0] = corr
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_18_{r.randint(1000, 9999)}",
        "subskill": "18_converse_pythagoras_triangle_test",
        "question_type": "mcq",
        "title": "Converse of Pythagoras Theorem",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{Compare }} a^2 + b^2 \\text{{ with }} c^2:\\\\{a}^2 + {b}^2 = {a**2} + {b**2} = {a**2 + b**2}.\\\\c^2 = {c}^2 = {c**2}.\\\\\n\\text{{Conclusion: }} {tri_type}.",
        "explanation": f"If $a^2 + b^2 = c^2$, the triangle is right-angled. If $a^2 + b^2 < c^2$, it is obtuse. If $a^2 + b^2 > c^2$, it is acute.",
        "marks": 2,
        "hints": {
            "tier_1": "Calculate the sum of squares of the two smaller sides, and compare to the square of the longest side.",
            "tier_2": f"Small sides: ${a}^2 + {b}^2 = {a**2 + b**2}$. Longest side: ${c}^2 = {c**2}$.",
            "tier_3": f"{calc_str}, which means the triangle is {tri_type}.",
        },
        "misconception_tags": ["confuses_acute_and_obtuse_pythagoras_inequality"],
        "diagram_spec": diag,
    }, "18_converse_pythagoras_triangle_test")


# --------------------------------------------------------------------------- #
# 19_pythagorean_triples_word_problem
# --------------------------------------------------------------------------- #
def _build_19_pythagorean_triples_word_problem(r: random.Random) -> Dict[str, Any]:
    ladder = r.choice([5, 10, 13, 15, 17])
    if ladder == 5:
        base, height = 3, 4
    elif ladder == 10:
        base, height = 6, 8
    elif ladder == 13:
        base, height = 5, 12
    elif ladder == 15:
        base, height = 9, 12
    else:
        base, height = 8, 15

    svg = _svg_wrapper(
        f'<line x1="60" y1="200" x2="280" y2="200" stroke="#64748b" stroke-width="3"/>\n'
        f'<line x1="100" y1="200" x2="100" y2="40" stroke="#334155" stroke-width="4"/>\n'
        f'<line x1="100" y1="40" x2="240" y2="200" stroke="#2563eb" stroke-width="3.5" stroke-linecap="round"/>\n'
        f'<rect x="100" y="182" width="18" height="18" fill="none" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<text x="60" y="120" font-size="13" font-weight="bold" fill="#0f172a">Wall</text>\n'
        f'<text x="170" y="220" font-size="13" font-weight="bold" fill="#0f172a">Ground ({base} m)</text>\n'
        f'<text x="190" y="110" font-size="13" font-weight="bold" fill="#2563eb">Ladder ({ladder} m)</text>\n'
        f'<text x="105" y="120" font-size="13" font-weight="bold" fill="#dc2626">h = ?</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "ladder": ladder, "base": base, "height": height}

    prompt = f"A ladder of length {ladder} m rests against a vertical wall. The foot of the ladder is placed {base} m away from the base of the wall on level ground. Calculate how high up the wall the ladder reaches ($h$)."
    corr = f"{height}\\text{{ m}}"
    opts = [f"{height}\\text{{ m}}", f"{ladder - base}\\text{{ m}}", f"{int(math.sqrt(ladder**2 + base**2))}\\text{{ m}}", f"{height + 1}\\text{{ m}}"]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_19_{r.randint(1000, 9999)}",
        "subskill": "19_pythagorean_triples_word_problem",
        "question_type": "mcq",
        "title": "Application of Pythagoras in Context",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"h^2 + \\text{{base}}^2 = \\text{{ladder}}^2 \\quad \\text{{(Theorem of Pythagoras)}}\\\\h^2 = {ladder}^2 - {base}^2 = {ladder**2} - {base**2} = {height**2}\\\\h = \\sqrt{{{height**2}}} = {height}\\text{{ m}}.",
        "explanation": f"Using the Theorem of Pythagoras with hypotenuse {ladder} m and base {base} m: $h = \\sqrt{{{ladder}^2 - {base}^2}} = {height}$ m.",
        "marks": 2,
        "hints": {
            "tier_1": "The wall, ground, and ladder form a right-angled triangle with the ladder as the hypotenuse.",
            "tier_2": f"Apply Pythagoras: $h^2 = {ladder}^2 - {base}^2 = {ladder**2} - {base**2} = {height**2}$.",
            "tier_3": f"Take the square root: $\\sqrt{{{height**2}}} = {height}$ m.",
        },
        "misconception_tags": ["adds_ladder_and_base_lengths", "confuses_hypotenuse_with_vertical_wall"],
        "diagram_spec": diag,
    }, "19_pythagorean_triples_word_problem")


# --------------------------------------------------------------------------- #
# 20_congruence_condition_sss
# --------------------------------------------------------------------------- #
def _build_20_congruence_condition_sss(r: random.Random) -> Dict[str, Any]:
    s1, s2, s3 = r.choice([(4, 6, 7), (5, 8, 9), (6, 7, 8), (5, 7, 10)])

    svg = _svg_wrapper(
        f'<polygon points="40,160 140,160 80,60" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="75" y="45" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="30" y="175" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="145" y="175" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="45" y="105" font-size="12" font-weight="bold" fill="#2563eb">{s1}</text>\n'
        f'<text x="120" y="105" font-size="12" font-weight="bold" fill="#059669">{s2}</text>\n'
        f'<text x="90" y="180" font-size="12" font-weight="bold" fill="#dc2626">{s3}</text>\n'
        f'<polygon points="200,160 300,160 240,60" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="235" y="45" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="190" y="175" font-size="13" font-weight="bold" fill="#0f172a">E</text>\n'
        f'<text x="305" y="175" font-size="13" font-weight="bold" fill="#0f172a">F</text>\n'
        f'<text x="205" y="105" font-size="12" font-weight="bold" fill="#2563eb">{s1}</text>\n'
        f'<text x="280" y="105" font-size="12" font-weight="bold" fill="#059669">{s2}</text>\n'
        f'<text x="250" y="180" font-size="12" font-weight="bold" fill="#dc2626">{s3}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "sides": [s1, s2, s3], "condition": "SSS"}

    prompt = f"In the diagram below, $\\triangle ABC$ and $\\triangle DEF$ have side lengths $AB = DE = {s1}$, $AC = DF = {s2}$, and $BC = EF = {s3}$. State the condition of congruence that proves $\\triangle ABC \\equiv \\triangle DEF$."
    corr = "\\text{SSS (Side, Side, Side)}"
    opts = [
        "\\text{SSS (Side, Side, Side)}",
        "\\text{SAS (Side, Included Angle, Side)}",
        "\\text{AAS (Angle, Angle, Side)}",
        "\\text{RHS (Right angle, Hypotenuse, Side)}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_20_{r.randint(1000, 9999)}",
        "subskill": "20_congruence_condition_sss",
        "question_type": "mcq",
        "title": "Congruence Condition: SSS",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{In }} \\triangle ABC \\text{{ and }} \\triangle DEF:\\\\1.\\; AB = DE = {s1} \\quad \\text{{(given)}}\\\\2.\\; AC = DF = {s2} \\quad \\text{{(given)}}\\\\3.\\; BC = EF = {s3} \\quad \\text{{(given)}}\\\\ \\therefore \\triangle ABC \\equiv \\triangle DEF \\quad \\text{{(SSS)}}.",
        "explanation": f"All three pairs of corresponding sides are equal, which proves congruence by SSS.",
        "marks": 2,
        "hints": {
            "tier_1": "Look at what is given: are three sides, two sides and an angle, or two angles and a side given?",
            "tier_2": "Three pairs of corresponding sides are equal.",
            "tier_3": "The condition is SSS (Side, Side, Side).",
        },
        "misconception_tags": ["confuses_sss_with_aaa_similarity"],
        "diagram_spec": diag,
    }, "20_congruence_condition_sss")


# --------------------------------------------------------------------------- #
# 21_congruence_condition_sas
# --------------------------------------------------------------------------- #
def _build_21_congruence_condition_sas(r: random.Random) -> Dict[str, Any]:
    s1 = r.randint(5, 9)
    s2 = r.randint(6, 11)
    ang = r.randint(40, 75)

    svg = _svg_wrapper(
        f'<polygon points="40,160 150,160 90,60" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="85" y="45" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="30" y="175" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="155" y="175" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="50" y="105" font-size="12" font-weight="bold" fill="#2563eb">{s1}</text>\n'
        f'<text x="95" y="180" font-size="12" font-weight="bold" fill="#059669">{s2}</text>\n'
        f'<text x="65" y="150" font-size="12" font-weight="bold" fill="#dc2626">{ang}°</text>\n'
        f'<polygon points="200,160 310,160 250,60" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="245" y="45" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="190" y="175" font-size="13" font-weight="bold" fill="#0f172a">E</text>\n'
        f'<text x="315" y="175" font-size="13" font-weight="bold" fill="#0f172a">F</text>\n'
        f'<text x="210" y="105" font-size="12" font-weight="bold" fill="#2563eb">{s1}</text>\n'
        f'<text x="255" y="180" font-size="12" font-weight="bold" fill="#059669">{s2}</text>\n'
        f'<text x="225" y="150" font-size="12" font-weight="bold" fill="#dc2626">{ang}°</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "s1": s1, "s2": s2, "ang": ang, "condition": "SAS"}

    prompt = f"In the diagram below, $\\triangle ABC$ and $\\triangle DEF$ have $AB = DE = {s1}$, $BC = EF = {s2}$, and included angles $\\hat{{B}} = \\hat{{E}} = {ang}^\\circ$. State the condition of congruence that proves $\\triangle ABC \\equiv \\triangle DEF$."
    corr = "\\text{SAS (Side, Included Angle, Side)}"
    opts = [
        "\\text{SAS (Side, Included Angle, Side)}",
        "\\text{ASS (Angle, Side, Side)}",
        "\\text{SSS (Side, Side, Side)}",
        "\\text{AAS (Angle, Angle, Side)}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_21_{r.randint(1000, 9999)}",
        "subskill": "21_congruence_condition_sas",
        "question_type": "mcq",
        "title": "Congruence Condition: SAS",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{In }} \\triangle ABC \\text{{ and }} \\triangle DEF:\\\\1.\\; AB = DE = {s1} \\quad \\text{{(given)}}\\\\2.\\; \\hat{{B}} = \\hat{{E}} = {ang}^\\circ \\quad \\text{{(included angle)}}\\\\3.\\; BC = EF = {s2} \\quad \\text{{(given)}}\\\\ \\therefore \\triangle ABC \\equiv \\triangle DEF \\quad \\text{{(SAS)}}.",
        "explanation": f"Two pairs of sides and the INCLUDED angle between them are equal, which proves congruence by SAS.",
        "marks": 2,
        "hints": {
            "tier_1": "Check whether the angle is situated BETWEEN the two given sides (included angle).",
            "tier_2": "The angle at B lies between sides AB and BC; similarly angle E lies between DE and EF.",
            "tier_3": "The correct reason is SAS (Side, Included Angle, Side).",
        },
        "misconception_tags": ["confuses_included_and_non_included_angle"],
        "diagram_spec": diag,
    }, "21_congruence_condition_sas")


# --------------------------------------------------------------------------- #
# 22_congruence_condition_aas
# --------------------------------------------------------------------------- #
def _build_22_congruence_condition_aas(r: random.Random) -> Dict[str, Any]:
    a1 = r.randint(45, 65)
    a2 = r.randint(55, 75)
    side = r.randint(6, 12)

    svg = _svg_wrapper(
        f'<polygon points="40,160 150,160 100,50" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="95" y="35" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="30" y="175" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="155" y="175" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="60" y="150" font-size="12" font-weight="bold" fill="#2563eb">{a1}°</text>\n'
        f'<text x="115" y="150" font-size="12" font-weight="bold" fill="#059669">{a2}°</text>\n'
        f'<text x="60" y="95" font-size="12" font-weight="bold" fill="#dc2626">{side}</text>\n'
        f'<polygon points="200,160 310,160 260,50" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="255" y="35" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="190" y="175" font-size="13" font-weight="bold" fill="#0f172a">E</text>\n'
        f'<text x="315" y="175" font-size="13" font-weight="bold" fill="#0f172a">F</text>\n'
        f'<text x="220" y="150" font-size="12" font-weight="bold" fill="#2563eb">{a1}°</text>\n'
        f'<text x="275" y="150" font-size="12" font-weight="bold" fill="#059669">{a2}°</text>\n'
        f'<text x="220" y="95" font-size="12" font-weight="bold" fill="#dc2626">{side}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "a1": a1, "a2": a2, "side": side, "condition": "AAS"}

    prompt = f"In the diagram below, $\\triangle ABC$ and $\\triangle DEF$ have $\\hat{{B}} = \\hat{{E}} = {a1}^\\circ$, $\\hat{{C}} = \\hat{{F}} = {a2}^\\circ$, and non-included side $AB = DE = {side}$. State the condition of congruence that proves $\\triangle ABC \\equiv \\triangle DEF$."
    corr = "\\text{AAS (Angle, Angle, Side)}"
    opts = [
        "\\text{AAS (Angle, Angle, Side)}",
        "\\text{SAS (Side, Included Angle, Side)}",
        "\\text{SSS (Side, Side, Side)}",
        "\\text{AAA (Similarity only, not congruence)}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_22_{r.randint(1000, 9999)}",
        "subskill": "22_congruence_condition_aas",
        "question_type": "mcq",
        "title": "Congruence Condition: AAS",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{In }} \\triangle ABC \\text{{ and }} \\triangle DEF:\\\\1.\\; \\hat{{B}} = \\hat{{E}} = {a1}^\\circ \\quad \\text{{(given)}}\\\\2.\\; \\hat{{C}} = \\hat{{F}} = {a2}^\\circ \\quad \\text{{(given)}}\\\\3.\\; AB = DE = {side} \\quad \\text{{(given)}}\\\\ \\therefore \\triangle ABC \\equiv \\triangle DEF \\quad \\text{{(AAS)}}.",
        "explanation": f"Two pairs of corresponding angles and one pair of corresponding sides are equal, which proves congruence by AAS.",
        "marks": 2,
        "hints": {
            "tier_1": "Two angles and one side are given.",
            "tier_2": "Because the side is not between the two angles, the condition is AAS (Angle, Angle, Side).",
            "tier_3": "Correct reason: AAS.",
        },
        "misconception_tags": ["confuses_aas_with_aaa"],
        "diagram_spec": diag,
    }, "22_congruence_condition_aas")


# --------------------------------------------------------------------------- #
# 23_congruence_condition_rhs
# --------------------------------------------------------------------------- #
def _build_23_congruence_condition_rhs(r: random.Random) -> Dict[str, Any]:
    leg = r.randint(4, 9)
    hyp = r.randint(10, 16)

    svg = _svg_wrapper(
        f'<polygon points="40,160 140,160 40,60" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<rect x="40" y="142" width="18" height="18" fill="none" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<text x="30" y="55" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="30" y="175" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="145" y="175" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="90" y="180" font-size="12" font-weight="bold" fill="#2563eb">{leg}</text>\n'
        f'<text x="100" y="105" font-size="12" font-weight="bold" fill="#059669">{hyp}</text>\n'
        f'<polygon points="200,160 300,160 200,60" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<rect x="200" y="142" width="18" height="18" fill="none" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<text x="190" y="55" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="190" y="175" font-size="13" font-weight="bold" fill="#0f172a">E</text>\n'
        f'<text x="305" y="175" font-size="13" font-weight="bold" fill="#0f172a">F</text>\n'
        f'<text x="250" y="180" font-size="12" font-weight="bold" fill="#2563eb">{leg}</text>\n'
        f'<text x="260" y="105" font-size="12" font-weight="bold" fill="#059669">{hyp}</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "leg": leg, "hyp": hyp, "condition": "RHS"}

    prompt = f"In the diagram below, $\\triangle ABC$ and $\\triangle DEF$ are both right-angled at $B$ and $E$ respectively ($\\hat{{B}} = \\hat{{E}} = 90^\\circ$). The hypotenuses are $AC = DF = {hyp}$, and one corresponding leg is $BC = EF = {leg}$. State the condition of congruence."
    corr = "\\text{RHS (Right angle, Hypotenuse, Side)}"
    opts = [
        "\\text{RHS (Right angle, Hypotenuse, Side)}",
        "\\text{SAS (Side, Included Angle, Side)}",
        "\\text{ASS (Angle, Side, Side)}",
        "\\text{SSS (Side, Side, Side)}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_23_{r.randint(1000, 9999)}",
        "subskill": "23_congruence_condition_rhs",
        "question_type": "mcq",
        "title": "Congruence Condition: RHS",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{In }} \\triangle ABC \\text{{ and }} \\triangle DEF:\\\\1.\\; \\hat{{B}} = \\hat{{E}} = 90^\\circ \\quad \\text{{(Right angle)}}\\\\2.\\; AC = DF = {hyp} \\quad \\text{{(Hypotenuse)}}\\\\3.\\; BC = EF = {leg} \\quad \\text{{(Side)}}\\\\ \\therefore \\triangle ABC \\equiv \\triangle DEF \\quad \\text{{(RHS)}}.",
        "explanation": f"Right-angled triangles with equal hypotenuses and one pair of equal legs are congruent by RHS.",
        "marks": 2,
        "hints": {
            "tier_1": "Both triangles have a 90° angle, equal hypotenuses, and one pair of equal legs.",
            "tier_2": "The abbreviation stands for Right angle, Hypotenuse, Side.",
            "tier_3": "Correct condition: RHS.",
        },
        "misconception_tags": ["mislabels_rhs_as_sas"],
        "diagram_spec": diag,
    }, "23_congruence_condition_rhs")


# --------------------------------------------------------------------------- #
# 24_congruence_deduce_corresponding_parts
# --------------------------------------------------------------------------- #
def _build_24_congruence_deduce_corresponding_parts(r: random.Random) -> Dict[str, Any]:
    side_ab = r.randint(7, 14)
    angle_c = r.randint(35, 65)

    svg = _svg_wrapper(
        f'<polygon points="40,150 140,150 90,60" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="85" y="45" font-size="13" font-weight="bold" fill="#0f172a">A</text>\n'
        f'<text x="30" y="165" font-size="13" font-weight="bold" fill="#0f172a">B</text>\n'
        f'<text x="145" y="165" font-size="13" font-weight="bold" fill="#0f172a">C</text>\n'
        f'<text x="50" y="100" font-size="12" font-weight="bold" fill="#2563eb">{side_ab}</text>\n'
        f'<text x="115" y="140" font-size="12" font-weight="bold" fill="#059669">{angle_c}°</text>\n'
        f'<polygon points="200,150 300,150 250,60" fill="#f8fafc" stroke="#334155" stroke-width="2"/>\n'
        f'<text x="245" y="45" font-size="13" font-weight="bold" fill="#0f172a">D</text>\n'
        f'<text x="190" y="165" font-size="13" font-weight="bold" fill="#0f172a">E</text>\n'
        f'<text x="305" y="165" font-size="13" font-weight="bold" fill="#0f172a">F</text>\n'
        f'<text x="210" y="100" font-size="12" font-weight="bold" fill="#dc2626">DE = ?</text>\n'
        f'<text x="275" y="140" font-size="12" font-weight="bold" fill="#dc2626">\\hat{{F}} = ?</text>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "side_ab": side_ab, "angle_c": angle_c}

    prompt = f"It has been proven that $\\triangle ABC \\equiv \\triangle DEF$. Given that $AB = {side_ab}$ and $\\hat{{C}} = {angle_c}^\\circ$, deduce the corresponding side length $DE$ and corresponding angle $\\hat{{F}}$."
    corr = f"DE = {side_ab}, \\; \\hat{{F}} = {angle_c}^\\circ"
    opts = [
        f"DE = {side_ab}, \\; \\hat{{F}} = {angle_c}^\\circ",
        f"DE = {side_ab + 2}, \\; \\hat{{F}} = {angle_c}^\\circ",
        f"DE = {side_ab}, \\; \\hat{{F}} = {180 - angle_c}^\\circ",
        f"DE = {angle_c}, \\; \\hat{{F}} = {side_ab}^\\circ",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_24_{r.randint(1000, 9999)}",
        "subskill": "24_congruence_deduce_corresponding_parts",
        "question_type": "mcq",
        "title": "Deduce Corresponding Parts from Congruence",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{Since }} \\triangle ABC \\equiv \\triangle DEF:\\\\DE = AB = {side_ab} \\quad \\text{{(corresponding sides of congruent triangles)}}\\\\\\hat{{F}} = \\hat{{C}} = {angle_c}^\\circ \\quad \\text{{(corresponding angles of congruent triangles)}}.",
        "explanation": f"Congruent triangles have identical corresponding sides and angles: $DE = AB = {side_ab}$ and $\\hat{{F}} = \\hat{{C}} = {angle_c}^\\circ$.",
        "marks": 2,
        "hints": {
            "tier_1": "Congruent triangles are identical in shape and size.",
            "tier_2": "Look at the order of letters: $\\triangle ABC \\equiv \\triangle DEF$ means vertex A corresponds to D, B to E, and C to F.",
            "tier_3": f"Therefore $DE = AB = {side_ab}$ and $\\hat{{F}} = \\hat{{C}} = {angle_c}^\\circ$.",
        },
        "misconception_tags": ["mismatches_corresponding_vertices"],
        "diagram_spec": diag,
    }, "24_congruence_deduce_corresponding_parts")


# --------------------------------------------------------------------------- #
# 25_congruence_overlapping_triangles
# --------------------------------------------------------------------------- #
def _build_25_congruence_overlapping_triangles(r: random.Random) -> Dict[str, Any]:
    angle_apex = r.randint(40, 70)
    variant = r.choice([("A", "B", "C", "D"), ("P", "Q", "R", "S"), ("K", "L", "M", "N")])
    top, left, right, foot = variant

    svg = _svg_wrapper(
        f'<polygon points="180,40 60,190 300,190" fill="none" stroke="#334155" stroke-width="2.5"/>\n'
        f'<line x1="180" y1="40" x2="180" y2="190" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,4"/>\n'
        f'<rect x="180" y="172" width="18" height="18" fill="none" stroke="#dc2626" stroke-width="1.8"/>\n'
        f'<text x="180" y="28" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">{top}</text>\n'
        f'<text x="45" y="205" font-size="14" font-weight="bold" fill="#0f172a">{left}</text>\n'
        f'<text x="310" y="205" font-size="14" font-weight="bold" fill="#0f172a">{right}</text>\n'
        f'<text x="180" y="210" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">{foot}</text>\n'
        f'<line x1="115" y1="110" x2="125" y2="110" stroke="#dc2626" stroke-width="2"/>\n'
        f'<line x1="235" y1="110" x2="245" y2="110" stroke="#dc2626" stroke-width="2"/>'
    )
    diag = {"kind": "inline_svg", "svg": svg, "diagram_role": "context", "apex": angle_apex, "vertex": top}

    prompt = f"In $\\triangle {top}{left}{right}$ below, ${top}{left} = {top}{right}$, apex angle $\\hat{{{top}}} = {angle_apex}^\\circ$, and ${top}{foot} \\perp {left}{right}$ with ${foot}$ on ${left}{right}$. To prove that $\\triangle {top}{left}{foot} \\equiv \\triangle {top}{right}{foot}$, which congruence condition is used?"
    corr = f"\\text{{RHS (Right angle, Hypotenuse }} {top}{left}={top}{right}, \\text{{ Common side }} {top}{foot}\\text{{)}}"
    opts = [
        f"\\text{{RHS (Right angle, Hypotenuse }} {top}{left}={top}{right}, \\text{{ Common side }} {top}{foot}\\text{{)}}",
        "\\text{SSS (all three sides equal)}",
        "\\text{AAA (equiangular)}",
        "\\text{AAS (two angles and one side)}",
    ]
    r.shuffle(opts)

    return _add_pillars({
        "id": f"g10_euclid_25_{r.randint(1000, 9999)}",
        "subskill": "25_congruence_overlapping_triangles",
        "question_type": "mcq",
        "title": "Congruence in Symmetrical / Overlapping Triangles",
        "prompt": prompt,
        "question": prompt,
        "options": [f"${o}$" for o in opts],
        "correct_answer": f"${corr}$",
        "expected_answer": f"${corr}$",
        "sample_answer": f"${corr}$",
        "worked_solution": f"\\text{{In }} \\triangle {top}{left}{foot} \\text{{ and }} \\triangle {top}{right}{foot}:\\\\1.\\; {top}\\hat{{{foot}}}{left} = {top}\\hat{{{foot}}}{right} = 90^\\circ \\quad \\text{{(given }} {top}{foot} \\perp {left}{right}\\text{{)}}\\\\2.\\; {top}{left} = {top}{right} \\quad \\text{{(hypotenuse, given)}}\\\\3.\\; {top}{foot} \\text{{ is common side}}\\\\ \\therefore \\triangle {top}{left}{foot} \\equiv \\triangle {top}{right}{foot} \\quad \\text{{(RHS)}}.",
        "explanation": f"Both triangles are right-angled, share hypotenuse length (${top}{left} = {top}{right}$), and share common leg ${top}{foot}$, giving congruence by RHS.",
        "marks": 2,
        "hints": {
            "tier_1": f"${top}{foot}$ is a shared vertical line segment common to both triangles.",
            "tier_2": f"Both triangles have a 90° angle at {foot} and equal hypotenuses ${top}{left} = {top}{right}$.",
            "tier_3": "Right angle + Hypotenuse + shared Side = RHS.",
        },
        "misconception_tags": ["forgets_common_side_as_valid_reason"],
        "diagram_spec": diag,
    }, "25_congruence_overlapping_triangles")


# --------------------------------------------------------------------------- #
# EXPORTED BUILDERS DICT (01 to 25)
# --------------------------------------------------------------------------- #
BUILDERS_01_25: Dict[str, Any] = {
    "01_angle_classification_and_estimation": _build_01_angle_classification_and_estimation,
    "02_adjacent_angles_on_straight_line": _build_02_adjacent_angles_on_straight_line,
    "03_vertically_opposite_angles_intersection": _build_03_vertically_opposite_angles_intersection,
    "04_angles_around_a_point_revolution": _build_04_angles_around_a_point_revolution,
    "05_complementary_angles_right_angle": _build_05_complementary_angles_right_angle,
    "06_alternate_interior_angles_parallel": _build_06_alternate_interior_angles_parallel,
    "07_corresponding_angles_parallel_f_shape": _build_07_corresponding_angles_parallel_f_shape,
    "08_co_interior_angles_parallel_c_shape": _build_08_co_interior_angles_parallel_c_shape,
    "09_parallel_lines_multi_step_algebraic": _build_09_parallel_lines_multi_step_algebraic,
    "10_converse_parallel_lines_test": _build_10_converse_parallel_lines_test,
    "11_triangle_interior_angle_sum": _build_11_triangle_interior_angle_sum,
    "12_triangle_exterior_angle_theorem": _build_12_triangle_exterior_angle_theorem,
    "13_isosceles_triangle_base_angles": _build_13_isosceles_triangle_base_angles,
    "14_equilateral_triangle_properties": _build_14_equilateral_triangle_properties,
    "15_isosceles_triangle_algebraic_solve": _build_15_isosceles_triangle_algebraic_solve,
    "16_pythagoras_calculate_hypotenuse": _build_16_pythagoras_calculate_hypotenuse,
    "17_pythagoras_calculate_shorter_side": _build_17_pythagoras_calculate_shorter_side,
    "18_converse_pythagoras_triangle_test": _build_18_converse_pythagoras_triangle_test,
    "19_pythagorean_triples_word_problem": _build_19_pythagorean_triples_word_problem,
    "20_congruence_condition_sss": _build_20_congruence_condition_sss,
    "21_congruence_condition_sas": _build_21_congruence_condition_sas,
    "22_congruence_condition_aas": _build_22_congruence_condition_aas,
    "23_congruence_condition_rhs": _build_23_congruence_condition_rhs,
    "24_congruence_deduce_corresponding_parts": _build_24_congruence_deduce_corresponding_parts,
    "25_congruence_overlapping_triangles": _build_25_congruence_overlapping_triangles,
}
