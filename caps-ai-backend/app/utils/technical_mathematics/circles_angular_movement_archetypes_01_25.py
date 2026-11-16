"""Technical Mathematics — Circles, Angles & Angular Movement: Archetypes 01 to 25.

Ground truth: curriculum_docs_auto/TechnicalMathematics_Gr10/Term 3/01. Circles  angles and angular Movement.md
and curriculum_docs_auto/TechnicalMathematics_Gr11/Term 3/
Covers:
- 01–06: Radian & degree angle conversions (exact fractions of pi, decimal radians, DMS).
- 07–11: Arc length & sector perimeter calculations (s = r*theta, P = 2r + s).
- 12–16: Circular sector areas & inverse problems (A = 0.5*r^2*theta, A = 0.5*r*s).
- 17–21: Chord lengths, sagitta (segment height), and minor/major circular segment areas.
- 22–25: Annular rings (washers/pipe flanges), annular sectors, and circular pipe liquid levels.

Zero LLM, 100% deterministic SymPy-backed questions with step-by-step solutions.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade10_mathematics._math_common import (
    make_mcq,
    make_short,
    make_steps,
    nonzero,
    num,
    solution,
    step,
    to_latex,
    to_latex_safe,
    with_metadata,
)

TOPIC = "technical_mathematics_angular_movement"
LO = "tech_math_angular_movement"
theta_sym = sp.Symbol("theta")
r_sym = sp.Symbol("r")


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _add_pillars(q: Dict[str, Any], subskill_name: str, duration: int = 3, weight: int = 15) -> Dict[str, Any]:
    marks = int(q.get("marks", 2))
    schema = [
        {"criterion": "Application of circular / angular formula", "marks": max(1, marks - 1)},
        {"criterion": "Accurate calculation and unit conversion", "marks": 1},
    ]
    q.update({
        "term": 3,
        "caps_weight_percent": weight,
        "suggested_duration_mins": duration,
        "mode": f"elementary_{subskill_name}",
        "marking_schema": schema,
    })
    return q


# --------------------------------------------------------------------------- #
# 01_degree_to_radian_special_angles
# --------------------------------------------------------------------------- #
def _build_01_degree_to_radian_special_angles(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    deg_choices = [30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]
    deg = r.choice(deg_choices)
    frac = sp.Rational(deg, 180)
    rad_latex = "\\pi" if frac == 1 else f"\\frac{{{frac.numerator}\\pi}}{{{frac.denominator}}}" if frac.numerator != 1 else f"\\frac{{\\pi}}{{{frac.denominator}}}"

    sol = solution(
        goal=f"convert {deg} degrees to radians in terms of pi",
        chain_type="expression",
        var="theta",
        steps=[
            step(from_expr=f"\\theta = {deg}^\\circ \\times \\frac{{\\pi}}{{180^\\circ}}",
                 to_expr=f"\\theta = {rad_latex}",
                 op="simplify fraction", rule="degree to radian conversion"),
        ],
        final_expr=rad_latex,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Convert }} {deg}^\\circ \\text{{ to radians. Leave your answer in terms of }} \\pi.",
        answer_expr=rad_latex,
        answer_mode="expression",
        answer_latex=rad_latex,
        marks=2,
        canonical_solution=sol,
        explanation=f"To convert degrees to radians, multiply by $\\dfrac{{\\pi}}{{180^\\circ}}$: ${deg}^\\circ \\times \\dfrac{{\\pi}}{{180^\\circ}} = {rad_latex}$ rad.",
        hint="Multiply the degree angle by pi / 180 and simplify the fraction.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="01_degree_to_radian_special_angles",
        learning_objective_id=f"{LO}.01_deg_to_rad_special",
        misconception_tags=["multiplies_by_180_over_pi", "forgets_pi_in_answer"],
        diagnostic_tags=["angles", "radians"],
        keywords=["convert to radians", "special angles", "pi"],
    )
    return _add_pillars(q, "01_degree_to_radian_special_angles", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 02_radian_to_degree_exact_fractions
# --------------------------------------------------------------------------- #
def _build_02_radian_to_degree_exact_fractions(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    frac_pairs = [(1, 6, 30), (1, 4, 45), (1, 3, 60), (1, 2, 90), (2, 3, 120), (3, 4, 135), (5, 6, 150), (1, 1, 180), (7, 6, 210), (5, 4, 225), (4, 3, 240), (3, 2, 270), (5, 3, 300), (7, 4, 315), (11, 6, 330), (2, 1, 360)]
    num_p, den_p, deg_ans = r.choice(frac_pairs)
    rad_latex = "\\pi" if (num_p == 1 and den_p == 1) else (f"{num_p}\\pi" if den_p == 1 else (f"\\frac{{\\pi}}{{{den_p}}}" if num_p == 1 else f"\\frac{{{num_p}\\pi}}{{{den_p}}}"))

    sol = solution(
        goal=f"convert {rad_latex} radians to degrees",
        chain_type="expression",
        var="theta",
        steps=[
            step(from_expr=f"\\theta = ({rad_latex}) \\times \\frac{{180^\\circ}}{{\\pi}}",
                 to_expr=f"\\theta = {deg_ans}^\\circ",
                 op="cancel pi and simplify", rule="radian to degree conversion"),
        ],
        final_expr=sp.Integer(deg_ans),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Convert }} {rad_latex} \\text{{ radians to degrees.}}",
        answer_expr=sp.Integer(deg_ans),
        answer_mode="value",
        answer_latex=f"{deg_ans}^\\circ",
        marks=2,
        canonical_solution=sol,
        explanation=f"Multiply by $\\dfrac{{180^\\circ}}{{\\pi}}$: $\\left({rad_latex}\\right) \\times \\dfrac{{180^\\circ}}{{\\pi}} = {deg_ans}^\\circ$.",
        hint="Replace pi with 180 degrees and simplify.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="02_radian_to_degree_exact_fractions",
        learning_objective_id=f"{LO}.02_rad_to_deg_exact",
        misconception_tags=["multiplies_by_pi_over_180", "fraction_cancellation_error"],
        diagnostic_tags=["angles", "degrees"],
        keywords=["convert to degrees", "radians", "exact fractions"],
    )
    return _add_pillars(q, "02_radian_to_degree_exact_fractions", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 03_decimal_degrees_to_radians_conversion
# --------------------------------------------------------------------------- #
def _build_03_decimal_degrees_to_radians_conversion(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    deg_val = round(r.uniform(15.0, 345.0), 1)
    rad_val = round(deg_val * math.pi / 180.0, 3)
    deg_str = _fmt_sa(deg_val, 1)
    rad_str = _fmt_sa(rad_val, 3)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Convert }} {deg_str}^\\circ \\text{{ to radians. Round your answer to three decimal places.}}",
        answer_expr=rad_str,
        answer_mode="expression",
        answer_latex=rad_str,
        marks=2,
        explanation=f"$\\theta = {deg_str}^\\circ \\times \\dfrac{{\\pi}}{{180^\\circ}} = {rad_str}$ rad.",
        hint="Multiply the degree angle by pi / 180 and round to 3 decimal places.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="03_decimal_degrees_to_radians_conversion",
        learning_objective_id=f"{LO}.03_deg_to_rad_decimal",
        misconception_tags=["rounds_too_early", "divides_by_360_instead_of_180"],
        diagnostic_tags=["angles", "decimal_radians"],
        keywords=["decimal radians", "convert to radians", "rounding"],
    )
    return _add_pillars(q, "03_decimal_degrees_to_radians_conversion", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 04_radians_to_decimal_degrees_conversion
# --------------------------------------------------------------------------- #
def _build_04_radians_to_decimal_degrees_conversion(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    rad_val = round(r.uniform(0.5, 5.8), 2)
    deg_val = round(rad_val * 180.0 / math.pi, 2)
    rad_str = _fmt_sa(rad_val, 2)
    deg_str = _fmt_sa(deg_val, 2)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Convert }} {rad_str} \\text{{ radians to degrees. Round your answer to two decimal places.}}",
        answer_expr=deg_str,
        answer_mode="expression",
        answer_latex=f"{deg_str}^\\circ",
        marks=2,
        explanation=f"$\\theta = {rad_str} \\times \\dfrac{{180^\\circ}}{{\\pi}} = {deg_str}^\\circ$.",
        hint="Multiply the radian value by 180 / pi.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="04_radians_to_decimal_degrees_conversion",
        learning_objective_id=f"{LO}.04_rad_to_deg_decimal",
        misconception_tags=["multiplies_by_pi_instead_of_dividing", "unit_confusion"],
        diagnostic_tags=["angles", "decimal_degrees"],
        keywords=["decimal degrees", "convert to degrees", "radians"],
    )
    return _add_pillars(q, "04_radians_to_decimal_degrees_conversion", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 05_degrees_to_degrees_minutes_seconds_dms
# --------------------------------------------------------------------------- #
def _build_05_degrees_to_degrees_minutes_seconds_dms(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    d_int = r.randint(20, 150)
    m_int = r.randint(5, 55)
    s_int = r.randint(10, 50)
    dec_deg = round(d_int + m_int / 60.0 + s_int / 3600.0, 4)
    dec_str = _fmt_sa(dec_deg, 4)
    ans_str = f"{d_int}^\\circ {m_int}' {s_int}''"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Convert }} {dec_str}^\\circ \\text{{ to degrees, minutes, and seconds }} (D^\\circ M' S'').",
        answer_expr=f"{d_int} {m_int} {s_int}",
        answer_mode="expression",
        answer_latex=ans_str,
        marks=3,
        explanation=(
            f"1. Integer degrees $= {d_int}^\\circ$.\n"
            f"2. Remaining minutes: $({dec_str} - {d_int}) \\times 60 = {(dec_deg - d_int)*60:.2f}' \\implies {m_int}'$.\n"
            f"3. Remaining seconds: $({(dec_deg - d_int)*60:.4f} - {m_int}) \\times 60 \\approx {s_int}''$.\n"
            f"Result: ${ans_str}$."
        ),
        hint="Take the whole number as degrees, multiply the decimal fraction by 60 for minutes, and multiply the remaining fraction by 60 for seconds.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="05_degrees_to_degrees_minutes_seconds_dms",
        learning_objective_id=f"{LO}.05_deg_to_dms",
        misconception_tags=["divides_by_100_instead_of_60", "seconds_rounding_error"],
        diagnostic_tags=["angles", "dms"],
        keywords=["degrees minutes seconds", "DMS", "angle notation"],
    )
    return _add_pillars(q, "05_degrees_to_degrees_minutes_seconds_dms", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 06_dms_to_decimal_degrees
# --------------------------------------------------------------------------- #
def _build_06_dms_to_decimal_degrees(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    d_int = r.randint(25, 120)
    m_int = r.choice([15, 30, 45, 12, 24, 36])
    s_int = r.choice([0, 18, 36, 54])
    dec_deg = round(d_int + m_int / 60.0 + s_int / 3600.0, 3)
    dec_str = _fmt_sa(dec_deg, 3)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Convert }} {d_int}^\\circ {m_int}' {s_int}'' \\text{{ to decimal degrees. Round to three decimal places.}}",
        answer_expr=dec_str,
        answer_mode="expression",
        answer_latex=f"{dec_str}^\\circ",
        marks=2,
        explanation=f"$\\text{{Degrees}} = {d_int} + \\dfrac{{{m_int}}}{{60}} + \\dfrac{{{s_int}}}{{3600}} = {dec_str}^\\circ$.",
        hint="Degrees + (minutes / 60) + (seconds / 3600).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="06_dms_to_decimal_degrees",
        learning_objective_id=f"{LO}.06_dms_to_decimal",
        misconception_tags=["divides_seconds_by_60_instead_of_3600", "arithmetic_error"],
        diagnostic_tags=["angles", "decimal_conversion"],
        keywords=["DMS to decimal", "minutes to degrees", "seconds to degrees"],
    )
    return _add_pillars(q, "06_dms_to_decimal_degrees", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 07_calculate_arc_length_given_radius_and_radians
# --------------------------------------------------------------------------- #
def _build_07_calculate_arc_length_given_radius_and_radians(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    radius = r.choice([4.0, 5.0, 6.0, 8.0, 10.0, 12.0])
    theta_rad = round(r.uniform(0.6, 2.4), 2)
    s_ans = round(radius * theta_rad, 2)
    r_str = _fmt_sa(radius, 1)
    th_str = _fmt_sa(theta_rad, 2)
    s_str = _fmt_sa(s_ans, 2)

    svg = f"""<svg viewBox="0 0 300 200" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
  <!-- Arc length r={r_str} theta={th_str} -->
  <g stroke="#1E293B" stroke-width="2" fill="none">
    <path d="M 60 150 L 220 150 A 160 160 0 0 0 {60 + 160*math.cos(theta_rad):.1f} {150 - 160*math.sin(theta_rad):.1f} Z" fill="#E0F2FE" />
    <line x1="60" y1="150" x2="220" y2="150" stroke="#0F172A" stroke-width="3" />
    <line x1="60" y1="150" x2="{60 + 160*math.cos(theta_rad):.1f}" y2="{150 - 160*math.sin(theta_rad):.1f}" stroke="#0F172A" stroke-width="3" />
    <text x="50" y="155" font-size="14" fill="#0F172A" font-weight="bold">O</text>
    <text x="140" y="170" font-size="12" fill="#475569">r = {r_str} cm</text>
    <text x="100" y="140" font-size="12" fill="#0284C7">θ = {th_str} rad</text>
    <text x="210" y="100" font-size="13" fill="#DC2626" font-weight="bold">s = ?</text>
  </g>
</svg>"""

    sol = solution(
        goal=f"calculate arc length with r={r_str} and theta={th_str} rad",
        chain_type="equation",
        var="s",
        steps=[
            step(from_expr="s = r\\theta",
                 to_expr=f"s = ({r_str})({th_str})",
                 op="substitute radius and radian angle", rule="arc length formula"),
            step(from_expr=f"s = ({r_str})({th_str})",
                 to_expr=f"s = {s_str}\\text{{ cm}}",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=s_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A circular sector has a radius of }} {r_str}\\text{{ cm and central angle }} \\theta = {th_str}\\text{{ rad. Calculate the arc length }} s.",
        answer_expr=s_str,
        answer_mode="expression",
        answer_latex=f"{s_str}\\text{{ cm}}",
        marks=2,
        canonical_solution=sol,
        explanation=f"Using $s = r\\theta$: $s = {r_str} \\times {th_str} = {s_str}\\text{{ cm}}$.",
        hint="Use the formula s = r * theta (ensure theta is in radians).",
    )
    q["diagram_spec"] = {"kind": "inline_svg", "svg": svg}
    with_metadata(
        q,
        topic=TOPIC,
        subskill="07_calculate_arc_length_given_radius_and_radians",
        learning_objective_id=f"{LO}.07_arc_length_radians",
        misconception_tags=["multiplies_by_pi_redundantly", "confuses_arc_with_sector_area"],
        diagnostic_tags=["circles", "arc_length"],
        keywords=["arc length", "s = r theta", "radians"],
    )
    return _add_pillars(q, "07_calculate_arc_length_given_radius_and_radians", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 08_calculate_arc_length_given_radius_and_degrees
# --------------------------------------------------------------------------- #
def _build_08_calculate_arc_length_given_radius_and_degrees(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    radius = r.choice([5.0, 7.5, 10.0, 12.0, 15.0])
    deg_angle = r.choice([40, 50, 72, 108, 144, 216])
    rad_angle = deg_angle * math.pi / 180.0
    s_ans = round(radius * rad_angle, 2)
    r_str = _fmt_sa(radius, 1)
    s_str = _fmt_sa(s_ans, 2)

    sol = solution(
        goal=f"calculate arc length with r={r_str} and theta={deg_angle} degrees",
        chain_type="equation",
        var="s",
        steps=[
            step(from_expr="\\theta = \\text{deg} \\times \\frac{\\pi}{180^\\circ}",
                 to_expr=f"\\theta = {deg_angle}^\\circ \\times \\frac{{\\pi}}{{180^\\circ}}",
                 op="convert degrees to radians", rule="angle conversion"),
            step(from_expr="s = r\\theta",
                 to_expr=f"s = {r_str} \\times \\left({deg_angle} \\times \\frac{{\\pi}}{{180}}\\right) = {s_str}",
                 op="substitute and evaluate", rule="arc length formula"),
        ],
        final_expr=s_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A circular sector with radius }} {r_str}\\text{{ m subtends a central angle of }} {deg_angle}^\\circ. \\text{{ Calculate the arc length }} s \\text{{ (rounded to two decimal places).}}",
        answer_expr=s_str,
        answer_mode="expression",
        answer_latex=f"{s_str}\\text{{ m}}",
        marks=2,
        canonical_solution=sol,
        explanation=f"First convert angle to radians: $\\theta = {deg_angle}^\\circ \\times \\dfrac{{\\pi}}{{180^\\circ}}$. Then $s = r\\theta = {r_str} \\times ({deg_angle} \\times \\pi \\div 180) = {s_str}\\text{{ m}}$.",
        hint="Convert the angle from degrees to radians before applying s = r * theta.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="08_calculate_arc_length_given_radius_and_degrees",
        learning_objective_id=f"{LO}.08_arc_length_degrees",
        misconception_tags=["uses_degrees_directly_in_formula", "conversion_error"],
        diagnostic_tags=["circles", "arc_degrees"],
        keywords=["arc length", "degrees to radians", "s = r theta"],
    )
    return _add_pillars(q, "08_calculate_arc_length_given_radius_and_degrees", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 09_calculate_radius_from_arc_length_and_angle
# --------------------------------------------------------------------------- #
def _build_09_calculate_radius_from_arc_length_and_angle(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    radius_true = r.choice([6.0, 8.0, 10.0, 12.0, 15.0])
    theta_rad = round(r.uniform(0.8, 2.2), 2)
    s_val = round(radius_true * theta_rad, 2)
    s_str = _fmt_sa(s_val, 2)
    th_str = _fmt_sa(theta_rad, 2)
    r_ans = round(s_val / theta_rad, 2)
    r_str = _fmt_sa(r_ans, 2)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{An arc of length }} s = {s_str}\\text{{ cm subtends a central angle of }} \\theta = {th_str}\\text{{ rad. Calculate the radius }} r \\text{{ of the circle.}}",
        answer_expr=r_str,
        answer_mode="expression",
        answer_latex=f"{r_str}\\text{{ cm}}",
        marks=2,
        explanation=f"Rearranging $s = r\\theta \\implies r = \\dfrac{{s}}{{\\theta}} = \\dfrac{{{s_str}}}{{{th_str}}} = {r_str}\\text{{ cm}}$.",
        hint="Rearrange s = r * theta to solve for r: r = s / theta.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="09_calculate_radius_from_arc_length_and_angle",
        learning_objective_id=f"{LO}.09_radius_from_arc",
        misconception_tags=["multiplies_s_and_theta", "division_order_reversed"],
        diagnostic_tags=["circles", "inverse_arc"],
        keywords=["radius", "arc length", "r = s / theta"],
    )
    return _add_pillars(q, "09_calculate_radius_from_arc_length_and_angle", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 10_calculate_central_angle_from_arc_length_and_radius
# --------------------------------------------------------------------------- #
def _build_10_calculate_central_angle_from_arc_length_and_radius(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    radius = r.choice([5.0, 8.0, 10.0, 12.0, 16.0])
    arc_len = round(r.uniform(6.0, 24.0), 1)
    theta_rad = round(arc_len / radius, 3)
    r_str = _fmt_sa(radius, 1)
    s_str = _fmt_sa(arc_len, 1)
    th_str = _fmt_sa(theta_rad, 3)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the central angle }} \\theta \\text{{ in radians subtended by an arc of length }} {s_str}\\text{{ cm in a circle of radius }} {r_str}\\text{{ cm. Round to three decimal places.}}",
        answer_expr=th_str,
        answer_mode="expression",
        answer_latex=f"{th_str}\\text{{ rad}}",
        marks=2,
        explanation=f"$\\theta = \\dfrac{{s}}{{r}} = \\dfrac{{{s_str}}}{{{r_str}}} = {th_str}\\text{{ rad}}$.",
        hint="Use theta = s / r.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="10_calculate_central_angle_from_arc_length_and_radius",
        learning_objective_id=f"{LO}.10_angle_from_arc",
        misconception_tags=["converts_to_degrees_when_radians_requested", "divides_r_by_s"],
        diagnostic_tags=["circles", "angle_calculation"],
        keywords=["central angle", "theta = s / r", "radians"],
    )
    return _add_pillars(q, "10_calculate_central_angle_from_arc_length_and_radius", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 11_perimeter_of_circular_sector
# --------------------------------------------------------------------------- #
def _build_11_perimeter_of_circular_sector(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    radius = r.choice([4.0, 6.0, 7.5, 9.0, 11.0])
    theta_rad = round(r.uniform(0.7, 1.8), 2)
    arc_len = round(radius * theta_rad, 2)
    perim = round(2 * radius + arc_len, 2)
    r_str = _fmt_sa(radius, 1)
    th_str = _fmt_sa(theta_rad, 2)
    p_str = _fmt_sa(perim, 2)

    sol = solution(
        goal=f"calculate perimeter of circular sector with r={r_str} and theta={th_str}",
        chain_type="equation",
        var="P",
        steps=[
            step(from_expr="s = r\\theta", to_expr=f"s = {r_str} \\times {th_str} = {_fmt_sa(arc_len, 2)}", op="calculate arc length", rule="arc length"),
            step(from_expr="P = 2r + s", to_expr=f"P = 2({r_str}) + {_fmt_sa(arc_len, 2)} = {p_str}", op="add two radii and arc length", rule="sector perimeter"),
        ],
        final_expr=p_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Calculate the total perimeter }} P \\text{{ of a circular sector with radius }} {r_str}\\text{{ m and central angle }} \\theta = {th_str}\\text{{ rad.}}",
        answer_expr=p_str,
        answer_mode="expression",
        answer_latex=f"{p_str}\\text{{ m}}",
        marks=3,
        canonical_solution=sol,
        explanation=f"Perimeter includes two straight radii and the curved arc: $P = 2r + s = 2({r_str}) + ({r_str} \\times {th_str}) = {_fmt_sa(2*radius, 1)} + {_fmt_sa(arc_len, 2)} = {p_str}\\text{{ m}}$.",
        hint="Remember a sector has two straight edges of length r and one curved edge of length s: P = 2r + s.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="11_perimeter_of_circular_sector",
        learning_objective_id=f"{LO}.11_sector_perimeter",
        misconception_tags=["calculates_arc_length_only", "adds_only_one_radius"],
        diagnostic_tags=["circles", "perimeter"],
        keywords=["sector perimeter", "P = 2r + s", "boundary"],
    )
    return _add_pillars(q, "11_perimeter_of_circular_sector", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 12_area_of_circular_sector_given_radians
# --------------------------------------------------------------------------- #
def _build_12_area_of_circular_sector_given_radians(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    radius = r.choice([4.0, 6.0, 8.0, 10.0, 12.0])
    theta_rad = round(r.uniform(0.5, 2.2), 2)
    area = round(0.5 * (radius**2) * theta_rad, 2)
    r_str = _fmt_sa(radius, 1)
    th_str = _fmt_sa(theta_rad, 2)
    a_str = _fmt_sa(area, 2)

    svg = f"""<svg viewBox="0 0 300 200" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
  <!-- Sector area r={r_str} theta={th_str} -->
  <g stroke="#1E293B" stroke-width="2" fill="none">
    <path d="M 60 150 L 220 150 A 160 160 0 0 0 {60 + 160*math.cos(theta_rad):.1f} {150 - 160*math.sin(theta_rad):.1f} Z" fill="#BAE6FD" stroke="#0284C7" stroke-width="2" />
    <text x="50" y="155" font-size="14" fill="#0F172A" font-weight="bold">O</text>
    <text x="130" y="170" font-size="12" fill="#475569">r = {r_str} cm</text>
    <text x="130" y="120" font-size="13" fill="#0369A1" font-weight="bold">Area = ?</text>
  </g>
</svg>"""

    sol = solution(
        goal=f"calculate sector area with r={r_str} and theta={th_str} rad",
        chain_type="equation",
        var="A",
        steps=[
            step(from_expr="A = \\frac{1}{2}r^2\\theta",
                 to_expr=f"A = 0,5 \\times ({r_str})^2 \\times ({th_str})",
                 op="substitute radius and radian angle", rule="sector area formula"),
            step(from_expr=f"A = 0,5 \\times {_fmt_sa(radius**2, 1)} \\times {th_str}",
                 to_expr=f"A = {a_str}\\text{{ cm}}^2",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=a_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the area }} A \\text{{ of a circular sector with radius }} r = {r_str}\\text{{ cm and central angle }} \\theta = {th_str}\\text{{ rad.}}",
        answer_expr=a_str,
        answer_mode="expression",
        answer_latex=f"{a_str}\\text{{ cm}}^2",
        marks=2,
        canonical_solution=sol,
        explanation=f"Sector area $A = \\dfrac{{1}}{{2}}r^2\\theta = 0,5 \\times ({r_str})^2 \\times {th_str} = {a_str}\\text{{ cm}}^2$.",
        hint="Use the formula A = 0,5 * r^2 * theta.",
    )
    q["diagram_spec"] = {"kind": "inline_svg", "svg": svg}
    with_metadata(
        q,
        topic=TOPIC,
        subskill="12_area_of_circular_sector_given_radians",
        learning_objective_id=f"{LO}.12_sector_area_radians",
        misconception_tags=["forgets_half_factor", "forgets_to_square_radius"],
        diagnostic_tags=["circles", "sector_area"],
        keywords=["sector area", "A = 1/2 r^2 theta", "radians"],
    )
    return _add_pillars(q, "12_area_of_circular_sector_given_radians", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 13_area_of_circular_sector_given_degrees
# --------------------------------------------------------------------------- #
def _build_13_area_of_circular_sector_given_degrees(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    radius = r.choice([6.0, 8.0, 10.0, 12.0, 14.0])
    deg = r.choice([45, 60, 75, 90, 120, 150])
    rad_val = deg * math.pi / 180.0
    area = round(0.5 * (radius**2) * rad_val, 2)
    r_str = _fmt_sa(radius, 1)
    a_str = _fmt_sa(area, 2)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Calculate the area }} A \\text{{ of a circular sector with radius }} {r_str}\\text{{ m and central angle }} {deg}^\\circ. \\text{{ Round to two decimal places.}}",
        answer_expr=a_str,
        answer_mode="expression",
        answer_latex=f"{a_str}\\text{{ m}}^2",
        marks=2,
        explanation=f"Convert degrees to radians: $\\theta = {deg} \\times \\dfrac{{\\pi}}{{180}}$. Then $A = \\dfrac{{1}}{{2}}r^2\\theta = 0,5 \\times ({r_str})^2 \\times \\left({deg} \\times \\dfrac{{\\pi}}{{180}}\\right) = {a_str}\\text{{ m}}^2$.",
        hint="Convert the angle to radians first or use A = (deg / 360) * pi * r^2.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="13_area_of_circular_sector_given_degrees",
        learning_objective_id=f"{LO}.13_sector_area_degrees",
        misconception_tags=["uses_degrees_without_conversion", "squaring_error"],
        diagnostic_tags=["circles", "sector_area_degrees"],
        keywords=["sector area", "degrees", "A = 1/2 r^2 theta"],
    )
    return _add_pillars(q, "13_area_of_circular_sector_given_degrees", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 14_find_radius_from_sector_area_and_angle
# --------------------------------------------------------------------------- #
def _build_14_find_radius_from_sector_area_and_angle(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    radius_true = r.choice([5.0, 6.0, 8.0, 10.0, 12.0])
    theta_rad = round(r.uniform(0.8, 1.8), 2)
    area_val = round(0.5 * (radius_true**2) * theta_rad, 2)
    a_str = _fmt_sa(area_val, 2)
    th_str = _fmt_sa(theta_rad, 2)
    r_ans = round(math.sqrt((2.0 * area_val) / theta_rad), 2)
    r_str = _fmt_sa(r_ans, 2)

    sol = solution(
        goal="find radius from sector area and radian angle",
        chain_type="equation",
        var="r",
        steps=[
            step(from_expr="A = \\frac{1}{2}r^2\\theta", to_expr=f"{a_str} = 0,5 \\times r^2 \\times {th_str}", op="substitute given values", rule="sector formula"),
            step(from_expr=f"r^2 = \\frac{{2 \\times {a_str}}}{{{th_str}}}", to_expr=f"r = \\sqrt{{{_fmt_sa(2*area_val/theta_rad, 2)}}}", op="isolate r squared and take square root", rule="algebra"),
            step(from_expr=f"r = \\sqrt{{{_fmt_sa(2*area_val/theta_rad, 2)}}}", to_expr=f"r = {r_str}\\text{{ cm}}", op="evaluate", rule="arithmetic"),
        ],
        final_expr=r_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A sector has an area of }} {a_str}\\text{{ cm}}^2 \\text{{ and central angle }} \\theta = {th_str}\\text{{ rad. Calculate the radius }} r \\text{{ of the sector.}}",
        answer_expr=r_str,
        answer_mode="expression",
        answer_latex=f"{r_str}\\text{{ cm}}",
        marks=3,
        canonical_solution=sol,
        explanation=f"$A = \\dfrac{{1}}{{2}}r^2\\theta \\implies r = \\sqrt{{\\dfrac{{2A}}{{\\theta}}}} = \\sqrt{{\\dfrac{{2 \\times {a_str}}}{{{th_str}}}}} = {r_str}\\text{{ cm}}$.",
        hint="Rearrange A = 0,5 * r^2 * theta to solve for r: r = sqrt(2A / theta).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="14_find_radius_from_sector_area_and_angle",
        learning_objective_id=f"{LO}.14_radius_from_sector_area",
        misconception_tags=["forgets_square_root", "forgets_factor_of_two"],
        diagnostic_tags=["circles", "inverse_sector"],
        keywords=["radius", "sector area", "square root"],
    )
    return _add_pillars(q, "14_find_radius_from_sector_area_and_angle", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 15_find_angle_from_sector_area_and_radius
# --------------------------------------------------------------------------- #
def _build_15_find_angle_from_sector_area_and_radius(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    radius = r.choice([4.0, 5.0, 7.0, 8.0, 10.0])
    area_val = round(r.uniform(12.0, 48.0), 1)
    theta_rad = round((2.0 * area_val) / (radius**2), 3)
    r_str = _fmt_sa(radius, 1)
    a_str = _fmt_sa(area_val, 1)
    th_str = _fmt_sa(theta_rad, 3)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A circular sector of radius }} {r_str}\\text{{ m has an area of }} {a_str}\\text{{ m}}^2. \\text{{ Calculate the central angle }} \\theta \\text{{ in radians.}}",
        answer_expr=th_str,
        answer_mode="expression",
        answer_latex=f"{th_str}\\text{{ rad}}",
        marks=2,
        explanation=f"$\\theta = \\dfrac{{2A}}{{r^2}} = \\dfrac{{2 \\times {a_str}}}{{({r_str})^2}} = {th_str}\\text{{ rad}}$.",
        hint="Use theta = 2A / r^2.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="15_find_angle_from_sector_area_and_radius",
        learning_objective_id=f"{LO}.15_angle_from_sector_area",
        misconception_tags=["forgets_to_square_radius_in_denominator", "forgets_two_in_numerator"],
        diagnostic_tags=["circles", "inverse_sector_angle"],
        keywords=["central angle", "sector area", "theta = 2A / r^2"],
    )
    return _add_pillars(q, "15_find_angle_from_sector_area_and_radius", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 16_relationship_sector_area_from_arc_length
# --------------------------------------------------------------------------- #
def _build_16_relationship_sector_area_from_arc_length(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    radius = r.choice([5.0, 6.0, 8.0, 10.0, 12.0, 15.0])
    arc_len = round(r.uniform(4.0, 20.0), 1)
    area = round(0.5 * radius * arc_len, 2)
    r_str = _fmt_sa(radius, 1)
    s_str = _fmt_sa(arc_len, 1)
    a_str = _fmt_sa(area, 2)

    sol = solution(
        goal=f"calculate sector area from r={r_str} and s={s_str}",
        chain_type="equation",
        var="A",
        steps=[
            step(from_expr="A = \\frac{1}{2}rs",
                 to_expr=f"A = 0,5 \\times {r_str} \\times {s_str}",
                 op="substitute radius and arc length", rule="arc-area relationship"),
            step(from_expr=f"A = 0,5 \\times {r_str} \\times {s_str}",
                 to_expr=f"A = {a_str}\\text{{ cm}}^2",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=a_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A circular sector has radius }} r = {r_str}\\text{{ cm and arc length }} s = {s_str}\\text{{ cm. Calculate its area }} A \\text{{ directly.}}",
        answer_expr=a_str,
        answer_mode="expression",
        answer_latex=f"{a_str}\\text{{ cm}}^2",
        marks=2,
        canonical_solution=sol,
        explanation=f"Since $s = r\\theta$, the sector area can be written as $A = \\dfrac{{1}}{{2}}r(r\\theta) = \\dfrac{{1}}{{2}}rs = 0,5 \\times {r_str} \\times {s_str} = {a_str}\\text{{ cm}}^2$.",
        hint="Use the direct formula A = 0,5 * r * s.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="16_relationship_sector_area_from_arc_length",
        learning_objective_id=f"{LO}.16_area_from_arc_length",
        misconception_tags=["calculates_theta_unnecessarily_with_rounding_error", "forgets_half"],
        diagnostic_tags=["circles", "area_arc_relationship"],
        keywords=["sector area", "A = 1/2 r s", "arc length"],
    )
    return _add_pillars(q, "16_relationship_sector_area_from_arc_length", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 17_chord_length_from_radius_and_central_angle
# --------------------------------------------------------------------------- #
def _build_17_chord_length_from_radius_and_central_angle(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    radius = r.choice([6.0, 8.0, 10.0, 12.0, 15.0])
    deg = r.choice([60, 90, 120])
    # c = 2*r*sin(theta/2)
    half_rad = (deg / 2.0) * math.pi / 180.0
    chord_len = round(2.0 * radius * math.sin(half_rad), 2)
    r_str = _fmt_sa(radius, 1)
    c_str = _fmt_sa(chord_len, 2)

    sol = solution(
        goal=f"calculate chord length with r={r_str} and theta={deg} degrees",
        chain_type="equation",
        var="c",
        steps=[
            step(from_expr="c = 2r\\sin\\left(\\frac{\\theta}{2}\\right)",
                 to_expr=f"c = 2({r_str})\\sin({deg//2}^\\circ)",
                 op="substitute into chord formula", rule="chord geometry"),
            step(from_expr=f"c = {_fmt_sa(2*radius, 1)} \\times \\sin({deg//2}^\\circ)",
                 to_expr=f"c = {c_str}\\text{{ cm}}",
                 op="evaluate", rule="trigonometry"),
        ],
        final_expr=c_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A chord subtends a central angle of }} {deg}^\\circ \\text{{ in a circle of radius }} {r_str}\\text{{ cm. Calculate the length of the chord }} c.",
        answer_expr=c_str,
        answer_mode="expression",
        answer_latex=f"{c_str}\\text{{ cm}}",
        marks=2,
        canonical_solution=sol,
        explanation=f"Using the chord formula $c = 2r\\sin\\left(\\dfrac{{\\theta}}{{2}}\\right) = 2({r_str})\\sin({deg//2}^\\circ) = {c_str}\\text{{ cm}}$.",
        hint="Use the formula c = 2r * sin(theta / 2).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="17_chord_length_from_radius_and_central_angle",
        learning_objective_id=f"{LO}.17_chord_length",
        misconception_tags=["uses_sin_theta_instead_of_half_theta", "confuses_chord_with_arc"],
        diagnostic_tags=["circles", "chord"],
        keywords=["chord length", "c = 2r sin(theta/2)", "circle geometry"],
    )
    return _add_pillars(q, "17_chord_length_from_radius_and_central_angle", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 18_height_of_segment_sagitta_formula
# --------------------------------------------------------------------------- #
def _build_18_height_of_segment_sagitta_formula(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    radius = r.choice([10.0, 12.0, 15.0, 20.0, 25.0])
    deg = r.choice([60, 90, 120])
    half_rad = (deg / 2.0) * math.pi / 180.0
    h_val = round(radius * (1.0 - math.cos(half_rad)), 2)
    r_str = _fmt_sa(radius, 1)
    h_str = _fmt_sa(h_val, 2)

    svg = f"""<svg viewBox="0 0 300 200" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
  <!-- Sagitta height r={r_str} theta={deg} -->
  <g stroke="#1E293B" stroke-width="2" fill="none">
    <circle cx="150" cy="110" r="80" stroke="#94A3B8" />
    <path d="M 80 110 A 80 80 0 0 0 220 110 Z" fill="#FED7AA" stroke="#EA580C" stroke-width="2" />
    <line x1="80" y1="110" x2="220" y2="110" stroke="#0F172A" stroke-width="2" />
    <line x1="150" y1="110" x2="150" y2="190" stroke="#EA580C" stroke-width="2" stroke-dasharray="3,3" />
    <text x="155" y="150" font-size="12" fill="#C2410C" font-weight="bold">h = ?</text>
    <text x="150" y="90" font-size="12" fill="#475569" text-anchor="middle">r = {r_str} mm</text>
  </g>
</svg>"""

    sol = solution(
        goal=f"calculate sagitta h with r={r_str} and theta={deg} degrees",
        chain_type="equation",
        var="h",
        steps=[
            step(from_expr="h = r\\left(1 - \\cos\\left(\\frac{\\theta}{2}\\right)\\right)",
                 to_expr=f"h = {r_str}\\left(1 - \\cos({deg//2}^\\circ)\\right)",
                 op="substitute radius and half angle", rule="sagitta formula"),
            step(from_expr=f"h = {r_str}\\left(1 - {math.cos(half_rad):.3f}\\right)",
                 to_expr=f"h = {h_str}\\text{{ mm}}",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=h_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A circular disc of radius }} r = {r_str}\\text{{ mm has a chord subtending a central angle of }} {deg}^\\circ. \\text{{ Calculate the height of the segment (sagitta) }} h.",
        answer_expr=h_str,
        answer_mode="expression",
        answer_latex=f"{h_str}\\text{{ mm}}",
        marks=3,
        canonical_solution=sol,
        explanation=f"Height of segment $h = r\\left(1 - \\cos\\left(\\dfrac{{\\theta}}{{2}}\\right)\\right) = {r_str}\\left(1 - \\cos({deg//2}^\\circ)\\right) = {h_str}\\text{{ mm}}$.",
        hint="Use the sagitta formula h = r * (1 - cos(theta / 2)).",
    )
    q["diagram_spec"] = {"kind": "inline_svg", "svg": svg}
    with_metadata(
        q,
        topic=TOPIC,
        subskill="18_height_of_segment_sagitta_formula",
        learning_objective_id=f"{LO}.18_sagitta_height",
        misconception_tags=["uses_cos_theta_instead_of_half_theta", "forgets_one_minus_cos"],
        diagnostic_tags=["circles", "sagitta"],
        keywords=["sagitta", "height of segment", "chord geometry"],
    )
    return _add_pillars(q, "18_height_of_segment_sagitta_formula", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 19_diameter_from_chord_and_segment_height
# --------------------------------------------------------------------------- #
def _build_19_diameter_from_chord_and_segment_height(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # Technical engineering relation: 4h^2 - 4dh + x^2 = 0 => d = (x^2 / 4h) + h
    # where x is chord length, h is height, d is diameter.
    # Choose integer/clean values: e.g. x = 24, h = 6 => d = 576 / 24 + 6 = 24 + 6 = 30.
    triples = [
        (12, 2, 20), (16, 4, 20), (20, 5, 25), (24, 6, 30),
        (28, 7, 35), (30, 5, 50), (32, 8, 40), (36, 9, 45),
        (40, 10, 50), (48, 8, 80), (48, 12, 60), (60, 15, 75)
    ]
    x_chord, h_seg, d_diam = r.choice(triples)

    sol = solution(
        goal=f"find diameter d given chord x={x_chord} and height h={h_seg}",
        chain_type="equation",
        var="d",
        steps=[
            step(from_expr="4h^2 - 4dh + x^2 = 0 \\implies d = \\frac{x^2}{4h} + h",
                 to_expr=f"d = \\frac{{{x_chord}^2}}{{4({h_seg})}} + {h_seg}",
                 op="substitute chord and height", rule="technical circle diameter formula"),
            step(from_expr=f"d = \\frac{{{x_chord**2}}}{{{4*h_seg}}} + {h_seg}",
                 to_expr=f"d = {d_diam}\\text{{ mm}}",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=sp.Integer(d_diam),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=(
            f"\\text{{In an engineering workshop, a circular flange has a chord of length }} x = {x_chord}\\text{{ mm}} "
            f"\\text{{ and height of segment }} h = {h_seg}\\text{{ mm. Use the formula }} 4h^2 - 4dh + x^2 = 0 "
            f"\\text{{ to calculate the diameter }} d \\text{{ of the flange.}}"
        ),
        answer_expr=sp.Integer(d_diam),
        answer_mode="value",
        answer_latex=f"{d_diam}\\text{{ mm}}",
        marks=3,
        canonical_solution=sol,
        explanation=f"Rearranging: $4dh = 4h^2 + x^2 \\implies d = h + \\dfrac{{x^2}}{{4h}} = {h_seg} + \\dfrac{{{x_chord}^2}}{{4({h_seg})}} = {h_seg} + {x_chord**2 // (4*h_seg)} = {d_diam}\\text{{ mm}}$.",
        hint="Rearrange the formula to isolate d: d = (x^2 / 4h) + h.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="19_diameter_from_chord_and_segment_height",
        learning_objective_id=f"{LO}.19_diameter_from_sagitta",
        misconception_tags=["algebraic_transposition_error", "forgets_four_in_denominator"],
        diagnostic_tags=["circles", "technical_formula"],
        keywords=["diameter", "chord and sagitta", "4h^2 - 4dh + x^2 = 0"],
    )
    return _add_pillars(q, "19_diameter_from_chord_and_segment_height", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 20_area_of_minor_circular_segment
# --------------------------------------------------------------------------- #
def _build_20_area_of_minor_circular_segment(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    radius = r.choice([4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 14.0, 15.0])
    deg = r.choice([30, 45, 60, 75, 90, 105, 120, 135, 150])
    theta_rad = deg * math.pi / 180.0
    # Area = 0.5 * r^2 * (theta - sin(theta))
    area_seg = round(0.5 * (radius**2) * (theta_rad - math.sin(theta_rad)), 2)
    r_str = _fmt_sa(radius, 1)
    a_str = _fmt_sa(area_seg, 2)

    svg = f"""<svg viewBox="0 0 300 200" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
  <!-- Minor segment r={r_str} theta={deg} -->
  <g stroke="#1E293B" stroke-width="2" fill="none">
    <path d="M 60 150 L 220 150 A 160 160 0 0 0 {60 + 160*math.cos(theta_rad):.1f} {150 - 160*math.sin(theta_rad):.1f} Z" fill="#F1F5F9" />
    <path d="M 220 150 A 160 160 0 0 0 {60 + 160*math.cos(theta_rad):.1f} {150 - 160*math.sin(theta_rad):.1f} Z" fill="#FCA5A5" stroke="#DC2626" stroke-width="2" />
    <line x1="60" y1="150" x2="220" y2="150" />
    <line x1="60" y1="150" x2="{60 + 160*math.cos(theta_rad):.1f}" y2="{150 - 160*math.sin(theta_rad):.1f}" />
    <text x="50" y="155" font-size="14" fill="#0F172A">O</text>
    <text x="140" y="170" font-size="12" fill="#475569">r = {r_str} cm</text>
    <text x="190" y="120" font-size="12" fill="#B91C1C" font-weight="bold">Segment Area = ?</text>
  </g>
</svg>"""

    sol = solution(
        goal=f"calculate minor segment area with r={r_str} and theta={deg} degrees",
        chain_type="equation",
        var="A",
        steps=[
            step(from_expr="\\theta = \\text{deg} \\times \\frac{\\pi}{180^\\circ}",
                 to_expr=f"\\theta = {deg}^\\circ \\times \\frac{{\\pi}}{{180^\\circ}} = {theta_rad:.3f}\\text{{ rad}}",
                 op="convert angle to radians", rule="angle conversion"),
            step(from_expr="A_{\\text{segment}} = \\frac{1}{2}r^2(\\theta - \\sin\\theta)",
                 to_expr=f"A = 0,5 \\times ({r_str})^2 \\times ({theta_rad:.3f} - \\sin({deg}^\\circ))",
                 op="substitute into segment area formula", rule="segment area"),
            step(from_expr=f"A = 0,5 \\times {_fmt_sa(radius**2, 1)} \\times ({theta_rad - math.sin(theta_rad):.3f})",
                 to_expr=f"A = {a_str}\\text{{ cm}}^2",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=a_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Calculate the area of the minor circular segment bounded by a chord subtending }} {deg}^\\circ \\text{{ in a circle of radius }} {r_str}\\text{{ cm.}}",
        answer_expr=a_str,
        answer_mode="expression",
        answer_latex=f"{a_str}\\text{{ cm}}^2",
        marks=3,
        canonical_solution=sol,
        explanation=f"Area of segment = Area of sector - Area of triangle: $A = \\dfrac{{1}}{{2}}r^2(\\theta - \\sin\\theta) = 0,5 \\times ({r_str})^2 \\times \\left({deg}\\times\\dfrac{{\\pi}}{{180}} - \\sin({deg}^\\circ)\\right) = {a_str}\\text{{ cm}}^2$.",
        hint="Area of minor segment = 0,5 * r^2 * (theta - sin(theta)), where theta is in radians.",
    )
    q["diagram_spec"] = {"kind": "inline_svg", "svg": svg}
    with_metadata(
        q,
        topic=TOPIC,
        subskill="20_area_of_minor_circular_segment",
        learning_objective_id=f"{LO}.20_minor_segment_area",
        misconception_tags=["uses_degrees_in_first_theta_term", "adds_triangle_instead_of_subtracting"],
        diagnostic_tags=["circles", "segment_area"],
        keywords=["minor segment", "A = 1/2 r^2 (theta - sin theta)", "circular segment"],
    )
    return _add_pillars(q, "20_area_of_minor_circular_segment", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 21_area_of_major_circular_segment
# --------------------------------------------------------------------------- #
def _build_21_area_of_major_circular_segment(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    radius = r.choice([3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0])
    deg = r.choice([30, 45, 60, 75, 90, 105, 120, 135, 150])
    theta_rad = deg * math.pi / 180.0
    area_total = math.pi * (radius**2)
    area_minor = 0.5 * (radius**2) * (theta_rad - math.sin(theta_rad))
    area_major = round(area_total - area_minor, 2)
    r_str = _fmt_sa(radius, 1)
    a_maj_str = _fmt_sa(area_major, 2)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A chord subtends a central angle of }} {deg}^\\circ \\text{{ in a circle of radius }} {r_str}\\text{{ m. Calculate the area of the major circular segment.}}",
        answer_expr=a_maj_str,
        answer_mode="expression",
        answer_latex=f"{a_maj_str}\\text{{ m}}^2",
        marks=3,
        explanation=f"Area of major segment = $\\text{{Total circle area}} - \\text{{Minor segment area}} = \\pi({r_str})^2 - {_fmt_sa(area_minor, 2)} = {a_maj_str}\\text{{ m}}^2$.",
        hint="Calculate the total circle area (pi * r^2) and subtract the minor segment area.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="21_area_of_major_circular_segment",
        learning_objective_id=f"{LO}.21_major_segment_area",
        misconception_tags=["calculates_minor_segment_only", "arithmetic_subtraction_error"],
        diagnostic_tags=["circles", "major_segment"],
        keywords=["major segment", "total area minus minor", "circle geometry"],
    )
    return _add_pillars(q, "21_area_of_major_circular_segment", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 22_concentric_circles_annulus_area
# --------------------------------------------------------------------------- #
def _build_22_concentric_circles_annulus_area(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    r_inner = r.choice([2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
    r_outer = r_inner + r.choice([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    annulus_area = round(math.pi * (r_outer**2 - r_inner**2), 2)
    r_in_str = _fmt_sa(r_inner, 1)
    r_out_str = _fmt_sa(r_outer, 1)
    a_str = _fmt_sa(annulus_area, 2)

    svg = f"""<svg viewBox="0 0 300 200" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
  <!-- Annulus R={r_out_str} r={r_in_str} -->
  <g stroke="#0F172A" stroke-width="2" fill="none">
    <circle cx="150" cy="100" r="70" fill="#E2E8F0" />
    <circle cx="150" cy="100" r="40" fill="#FFFFFF" />
    <line x1="150" y1="100" x2="190" y2="100" stroke="#0284C7" stroke-width="2" />
    <line x1="150" y1="100" x2="220" y2="100" stroke="#0F172A" stroke-width="2" />
    <text x="170" y="95" font-size="11" fill="#0284C7">r={r_in_str}</text>
    <text x="205" y="95" font-size="11" fill="#0F172A">R={r_out_str}</text>
    <text x="150" y="150" font-size="12" fill="#334155" text-anchor="middle">Washer Flange Area = ?</text>
  </g>
</svg>"""

    sol = solution(
        goal=f"calculate annular ring area with R={r_out_str} and r={r_in_str}",
        chain_type="equation",
        var="A",
        steps=[
            step(from_expr="A = \\pi(R^2 - r^2)",
                 to_expr=f"A = \\pi(({r_out_str})^2 - ({r_in_str})^2)",
                 op="substitute outer and inner radii", rule="annulus formula"),
            step(from_expr=f"A = \\pi({r_outer**2:.2f} - {r_inner**2:.2f}) = \\pi({r_outer**2 - r_inner**2:.2f})",
                 to_expr=f"A = {a_str}\\text{{ cm}}^2",
                 op="evaluate with pi", rule="arithmetic"),
        ],
        final_expr=a_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A circular steel washer has an inner radius of }} {r_in_str}\\text{{ cm and outer radius of }} {r_out_str}\\text{{ cm. Calculate the surface area of the washer.}}",
        answer_expr=a_str,
        answer_mode="expression",
        answer_latex=f"{a_str}\\text{{ cm}}^2",
        marks=2,
        canonical_solution=sol,
        explanation=f"Area of annulus $A = \\pi(R^2 - r^2) = \\pi(({r_out_str})^2 - ({r_in_str})^2) = {a_str}\\text{{ cm}}^2$.",
        hint="Area = pi * (R^2 - r^2).",
    )
    q["diagram_spec"] = {"kind": "inline_svg", "svg": svg}
    with_metadata(
        q,
        topic=TOPIC,
        subskill="22_concentric_circles_annulus_area",
        learning_objective_id=f"{LO}.22_annulus_area",
        misconception_tags=["squares_the_difference_of_radii", "forgets_pi"],
        diagnostic_tags=["circles", "annulus"],
        keywords=["annulus", "washer area", "concentric circles"],
    )
    return _add_pillars(q, "22_concentric_circles_annulus_area", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 23_annular_sector_area_and_perimeter
# --------------------------------------------------------------------------- #
def _build_23_annular_sector_area_and_perimeter(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    r_in = r.choice([3.0, 4.0, 5.0, 6.0, 7.0])
    r_out = r_in + r.choice([2.0, 3.0, 4.0, 5.0])
    deg = r.choice([30, 45, 60, 75, 90, 120, 135, 150])
    th_rad = deg * math.pi / 180.0
    area_ann_sec = round(0.5 * th_rad * (r_out**2 - r_in**2), 2)
    rin_str = _fmt_sa(r_in, 1)
    rout_str = _fmt_sa(r_out, 1)
    a_str = _fmt_sa(area_ann_sec, 2)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{An annular sector has inner radius }} r = {rin_str}\\text{{ m, outer radius }} R = {rout_str}\\text{{ m, and central angle }} {deg}^\\circ. \\text{{ Calculate its area.}}",
        answer_expr=a_str,
        answer_mode="expression",
        answer_latex=f"{a_str}\\text{{ m}}^2",
        marks=3,
        explanation=f"Area $= \\dfrac{{1}}{{2}}\\theta(R^2 - r^2) = 0,5 \\times \\left({deg} \\times \\dfrac{{\\pi}}{{180}}\\right) \\times (({rout_str})^2 - ({rin_str})^2) = {a_str}\\text{{ m}}^2$.",
        hint="Subtract the inner sector area from the outer sector area: 0,5 * theta * (R^2 - r^2).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="23_annular_sector_area_and_perimeter",
        learning_objective_id=f"{LO}.23_annular_sector",
        misconception_tags=["uses_degrees_without_converting_to_radians", "forgets_half_factor"],
        diagnostic_tags=["circles", "annular_sector"],
        keywords=["annular sector", "sector of annulus", "area"],
    )
    return _add_pillars(q, "23_annular_sector_area_and_perimeter", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 24_circular_pipe_liquid_cross_section_level
# --------------------------------------------------------------------------- #
def _build_24_circular_pipe_liquid_cross_section_level(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    radius = r.choice([15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0])  # cm
    deg = r.choice([60, 90, 120])
    theta_rad = deg * math.pi / 180.0
    area_liquid = round(0.5 * (radius**2) * (theta_rad - math.sin(theta_rad)), 2)
    r_str = _fmt_sa(radius, 1)
    a_str = _fmt_sa(area_liquid, 2)

    svg = f"""<svg viewBox="0 0 300 200" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
  <!-- Pipe fluid r={r_str} angle={deg} -->
  <g stroke="#1E293B" stroke-width="2" fill="none">
    <circle cx="150" cy="100" r="70" stroke="#334155" stroke-width="3" />
    <path d="M {150 - 70*math.sin(theta_rad/2):.1f} {100 + 70*math.cos(theta_rad/2):.1f} A 70 70 0 0 0 {150 + 70*math.sin(theta_rad/2):.1f} {100 + 70*math.cos(theta_rad/2):.1f} Z" fill="#38BDF8" stroke="#0284C7" stroke-width="2" />
    <line x1="150" y1="100" x2="{150 - 70*math.sin(theta_rad/2):.1f}" y2="{100 + 70*math.cos(theta_rad/2):.1f}" stroke="#0F172A" stroke-dasharray="2,2" />
    <line x1="150" y1="100" x2="{150 + 70*math.sin(theta_rad/2):.1f}" y2="{100 + 70*math.cos(theta_rad/2):.1f}" stroke="#0F172A" stroke-dasharray="2,2" />
    <text x="150" y="90" font-size="12" fill="#0F172A" text-anchor="middle">r = {r_str} cm</text>
    <text x="150" y="160" font-size="12" fill="#0369A1" font-weight="bold" text-anchor="middle">Liquid Area = ?</text>
  </g>
</svg>"""

    sol = solution(
        goal=f"calculate liquid cross section area in pipe with r={r_str} cm and theta={deg} deg",
        chain_type="equation",
        var="A",
        steps=[
            step(from_expr="A = \\frac{1}{2}r^2(\\theta - \\sin\\theta)",
                 to_expr=f"A = 0,5 \\times ({r_str})^2 \\times \\left({theta_rad:.3f} - \\sin({deg}^\\circ)\\right)",
                 op="substitute into segment area formula", rule="circular segment area"),
            step(from_expr=f"A = 0,5 \\times {_fmt_sa(radius**2, 1)} \\times ({theta_rad - math.sin(theta_rad):.3f})",
                 to_expr=f"A = {a_str}\\text{{ cm}}^2",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=a_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Water flows in a circular stormwater pipe of radius }} r = {r_str}\\text{{ cm. The water surface forms a chord subtending an angle of }} {deg}^\\circ \\text{{ at the pipe centre. Calculate the cross-sectional area of water.}}",
        answer_expr=a_str,
        answer_mode="expression",
        answer_latex=f"{a_str}\\text{{ cm}}^2",
        marks=3,
        canonical_solution=sol,
        explanation=f"The liquid cross-section is a circular segment: $A = \\dfrac{{1}}{{2}}r^2(\\theta - \\sin\\theta) = 0,5 \\times ({r_str})^2 \\times \\left({deg} \\times \\dfrac{{\\pi}}{{180}} - \\sin({deg}^\\circ)\\right) = {a_str}\\text{{ cm}}^2$.",
        hint="Model the liquid cross-section as a circular segment with theta in radians.",
    )
    q["diagram_spec"] = {"kind": "inline_svg", "svg": svg}
    with_metadata(
        q,
        topic=TOPIC,
        subskill="24_circular_pipe_liquid_cross_section_level",
        learning_objective_id=f"{LO}.24_pipe_liquid_level",
        misconception_tags=["calculates_entire_pipe_area", "omits_triangle_subtraction"],
        diagnostic_tags=["applications", "pipe_flow"],
        keywords=["drainage pipe", "liquid cross-section", "circular segment"],
    )
    return _add_pillars(q, "24_circular_pipe_liquid_cross_section_level", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 25_cylindrical_tank_liquid_volume_horizontal
# --------------------------------------------------------------------------- #
def _build_25_cylindrical_tank_liquid_volume_horizontal(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    radius = r.choice([0.6, 0.8, 1.0, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0, 2.2, 2.5])  # meters
    length = r.choice([2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])  # meters
    deg = r.choice([60, 90, 120, 150])
    theta_rad = deg * math.pi / 180.0
    area_seg = 0.5 * (radius**2) * (theta_rad - math.sin(theta_rad))
    volume_liquid = round(area_seg * length, 2)
    r_str = _fmt_sa(radius, 1)
    l_str = _fmt_sa(length, 1)
    v_str = _fmt_sa(volume_liquid, 2)

    sol = solution(
        goal=f"calculate liquid volume in horizontal tank r={r_str} l={l_str} theta={deg} deg",
        chain_type="equation",
        var="V",
        steps=[
            step(from_expr="A_{\\text{segment}} = \\frac{1}{2}r^2(\\theta - \\sin\\theta)",
                 to_expr=f"A = 0,5 \\times ({r_str})^2 \\times \\left({theta_rad:.3f} - \\sin({deg}^\\circ)\\right) = {_fmt_sa(area_seg, 3)}\\text{{ m}}^2",
                 op="calculate segment cross-sectional area", rule="segment area"),
            step(from_expr="V = A_{\\text{segment}} \\times L",
                 to_expr=f"V = {_fmt_sa(area_seg, 3)} \\times {l_str} = {v_str}\\text{{ m}}^3",
                 op="multiply cross-sectional area by length", rule="volume of prism"),
        ],
        final_expr=v_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=(
            f"\\text{{A horizontal cylindrical fuel storage tank has a radius of }} {r_str}\\text{{ m and length }} {l_str}\\text{{ m. "
            f"Fuel inside fills the bottom of the tank such that the wet cross-section subtends a central angle of }} {deg}^\\circ. "
            f"\\text{{ Calculate the volume of fuel in the tank to 2 decimal places.}}"
        ),
        answer_expr=v_str,
        answer_mode="expression",
        answer_latex=f"{v_str}\\text{{ m}}^3",
        marks=4,
        canonical_solution=sol,
        explanation=f"Volume = Area of segment $\\times$ Length $= \\left[\\dfrac{{1}}{{2}}r^2(\\theta - \\sin\\theta)\\right] \\times L = \\left[0,5 \\times ({r_str})^2 \\times \\left({deg}\\times\\dfrac{{\\pi}}{{180}} - \\sin({deg}^\\circ)\\right)\\right] \\times {l_str} = {v_str}\\text{{ m}}^3$.",
        hint="First calculate the cross-sectional area of the liquid segment, then multiply by the length of the tank.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="25_cylindrical_tank_liquid_volume_horizontal",
        learning_objective_id=f"{LO}.25_tank_liquid_volume",
        misconception_tags=["uses_full_cylinder_volume", "forgets_to_multiply_by_length"],
        diagnostic_tags=["applications", "tank_volume"],
        keywords=["horizontal tank", "liquid volume", "circular segment volume"],
    )
    return _add_pillars(q, "25_cylindrical_tank_liquid_volume_horizontal", duration=4, weight=15)
    area_seg = 0.5 * (radius**2) * (theta_rad - math.sin(theta_rad))
    vol = round(area_seg * length, 2)
    r_str = _fmt_sa(radius, 1)
    l_str = _fmt_sa(length, 1)
    v_str = _fmt_sa(vol, 2)

    sol = solution(
        goal=f"calculate liquid volume in horizontal tank r={r_str}m, L={l_str}m, theta=120 deg",
        chain_type="equation",
        var="V",
        steps=[
            step(from_expr="A_{\\text{segment}} = \\frac{1}{2}r^2(\\theta - \\sin\\theta)",
                 to_expr=f"A = 0,5 \\times ({r_str})^2 \\times \\left(\\frac{{2\\pi}}{{3}} - \\sin(120^\\circ)\\right) = {_fmt_sa(area_seg, 3)}",
                 op="calculate cross-sectional segment area", rule="segment area formula"),
            step(from_expr="V = A_{\\text{segment}} \\times L",
                 to_expr=f"V = {_fmt_sa(area_seg, 3)} \\times {l_str} = {v_str}\\text{{ m}}^3",
                 op="multiply cross-sectional area by length", rule="prism volume"),
        ],
        final_expr=v_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A horizontal cylindrical diesel tank of radius }} r = {r_str}\\text{{ m and length }} L = {l_str}\\text{{ m contains fuel subtending }} 120^\\circ \\text{{ at the circular end centre. Calculate the fuel volume in }} \\text{{m}}^3.",
        answer_expr=v_str,
        answer_mode="expression",
        answer_latex=f"{v_str}\\text{{ m}}^3",
        marks=3,
        canonical_solution=sol,
        explanation=f"Cross-sectional area $A = \\dfrac{{1}}{{2}}r^2\\left(\\dfrac{{2\\pi}}{{3}} - \\sin(120^\\circ)\\right) = {_fmt_sa(area_seg, 3)}\\text{{ m}}^2$. Volume $V = A \\times L = {_fmt_sa(area_seg, 3)} \\times {l_str} = {v_str}\\text{{ m}}^3$.",
        hint="Calculate the circular segment cross-sectional area first, then multiply by the length of the tank.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="25_cylindrical_tank_liquid_volume_horizontal",
        learning_objective_id=f"{LO}.25_tank_liquid_volume",
        misconception_tags=["multiplies_full_cylinder_volume", "forgets_tank_length"],
        diagnostic_tags=["applications", "tank_volume"],
        keywords=["diesel tank", "horizontal cylinder", "segment volume"],
    )
    return _add_pillars(q, "25_cylindrical_tank_liquid_volume_horizontal", duration=3, weight=15)


BUILDERS_01_25: Dict[str, Any] = {
    "01_degree_to_radian_special_angles": _build_01_degree_to_radian_special_angles,
    "02_radian_to_degree_exact_fractions": _build_02_radian_to_degree_exact_fractions,
    "03_decimal_degrees_to_radians_conversion": _build_03_decimal_degrees_to_radians_conversion,
    "04_radians_to_decimal_degrees_conversion": _build_04_radians_to_decimal_degrees_conversion,
    "05_degrees_to_degrees_minutes_seconds_dms": _build_05_degrees_to_degrees_minutes_seconds_dms,
    "06_dms_to_decimal_degrees": _build_06_dms_to_decimal_degrees,
    "07_calculate_arc_length_given_radius_and_radians": _build_07_calculate_arc_length_given_radius_and_radians,
    "08_calculate_arc_length_given_radius_and_degrees": _build_08_calculate_arc_length_given_radius_and_degrees,
    "09_calculate_radius_from_arc_length_and_angle": _build_09_calculate_radius_from_arc_length_and_angle,
    "10_calculate_central_angle_from_arc_length_and_radius": _build_10_calculate_central_angle_from_arc_length_and_radius,
    "11_perimeter_of_circular_sector": _build_11_perimeter_of_circular_sector,
    "12_area_of_circular_sector_given_radians": _build_12_area_of_circular_sector_given_radians,
    "13_area_of_circular_sector_given_degrees": _build_13_area_of_circular_sector_given_degrees,
    "14_find_radius_from_sector_area_and_angle": _build_14_find_radius_from_sector_area_and_angle,
    "15_find_angle_from_sector_area_and_radius": _build_15_find_angle_from_sector_area_and_radius,
    "16_relationship_sector_area_from_arc_length": _build_16_relationship_sector_area_from_arc_length,
    "17_chord_length_from_radius_and_central_angle": _build_17_chord_length_from_radius_and_central_angle,
    "18_height_of_segment_sagitta_formula": _build_18_height_of_segment_sagitta_formula,
    "19_diameter_from_chord_and_segment_height": _build_19_diameter_from_chord_and_segment_height,
    "20_area_of_minor_circular_segment": _build_20_area_of_minor_circular_segment,
    "21_area_of_major_circular_segment": _build_21_area_of_major_circular_segment,
    "22_concentric_circles_annulus_area": _build_22_concentric_circles_annulus_area,
    "23_annular_sector_area_and_perimeter": _build_23_annular_sector_area_and_perimeter,
    "24_circular_pipe_liquid_cross_section_level": _build_24_circular_pipe_liquid_cross_section_level,
    "25_cylindrical_tank_liquid_volume_horizontal": _build_25_cylindrical_tank_liquid_volume_horizontal,
}
