"""Grade 10 Physical Sciences - Vectors and Scalars (Subskills 26 to 50)
100% Deterministic & SymPy-backed. South African National Curriculum Standards aligned.
Covers:
- Vector component resolution (horizontal Fx = F*cos(theta), vertical Fy = F*sin(theta))
- Resolution with angles to vertical or bearings
- Reconstructing vectors from rectangular components
- Component sign conventions across 4 quadrants
- Resultant of multiple concurrent vectors via algebraic components table
- Equilibrant vector definition and calculations (1D, perpendicular, and angled systems)
- Equilibrium of concurrent forces: closed vector triangle/polygon condition
- Suspended objects and cable tension systems (symmetric and horizontal pull)
- Navigational vector mechanics: boat crossing flowing river, aircraft in crosswind
- Applied forces at angles: pulling a sled (reduced normal force) vs pushing a lawnmower (increased normal force)
- Capstone vector synthesis rider and post-exam diagnostic autopsy / misconception triage
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.physical_sciences.mechanics_archetypes_01_25 import _fmt_sa, _rng, _vector_svg


# ============================================================================
# ARCHETYPES 26–50 BUILDERS
# ============================================================================

def build_26_resolve_vector_horizontal_component(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate horizontal component Fx = F*cos(theta) for force inclined to horizontal."""
    r = _rng(seed)
    
    f_mag = r.randint(25, 95)
    theta = r.choice([20, 25, 30, 35, 40, 45, 50, 60])
    theta_rad = math.radians(theta)
    fx = round(f_mag * math.cos(theta_rad), 2)
    
    prompt = (
        f"A worker pulls a heavy trolley with a force of {_fmt_sa(f_mag)} N at an angle of "
        f"{_fmt_sa(theta)}° to the horizontal ground.\n"
        f"Calculate the magnitude of the horizontal component (F_x) of this pulling force."
    )
    
    calc_latex = rf"F_x = F \cos\theta = ({_fmt_sa(f_mag)})\cos({theta}^\circ) = {_fmt_sa(fx)}\text{{ N}}"
    
    return {
        "id": f"vec_26_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "26_resolve_vector_horizontal_component",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 3,
        "prompt": prompt,
        "ideal_answer": f"F_x = {_fmt_sa(fx)} N",
        "sample_answer": calc_latex,
        "marks": 3,
        "misconception_tags": ["confused_sin_and_cos", "calculator_in_radians_mode"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_f", "desc": "Formula F_x = F cos(theta)", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": f"Substitution: ({f_mag})cos({theta}°)", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"Correct value with unit: {_fmt_sa(fx)} N", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "The horizontal component is adjacent to the angle θ with the ground.",
            "2_concept": "Adjacent side = Hypotenuse × cos(θ), so F_x = F × cos(θ).",
            "3_breakdown": f"F_x = {f_mag} × cos({theta}°) = {_fmt_sa(fx)} N.",
        },
    }


def build_27_resolve_vector_vertical_component(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate vertical component Fy = F*sin(theta) for force inclined to horizontal."""
    r = _rng(seed)
    
    f_mag = r.randint(30, 110)
    theta = r.choice([20, 30, 35, 45, 55, 60, 70])
    theta_rad = math.radians(theta)
    fy = round(f_mag * math.sin(theta_rad), 2)
    
    prompt = (
        f"A tow truck cable exerts a tension force of {_fmt_sa(f_mag)} N on a vehicle at an angle of "
        f"{_fmt_sa(theta)}° above the horizontal.\n"
        f"Calculate the magnitude of the vertical component (F_y) of this tension force."
    )
    
    calc_latex = rf"F_y = F \sin\theta = ({_fmt_sa(f_mag)})\sin({theta}^\circ) = {_fmt_sa(fy)}\text{{ N}}"
    
    return {
        "id": f"vec_27_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "27_resolve_vector_vertical_component",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 3,
        "prompt": prompt,
        "ideal_answer": f"F_y = {_fmt_sa(fy)} N",
        "sample_answer": calc_latex,
        "marks": 3,
        "misconception_tags": ["confused_sin_and_cos", "calculator_in_radians_mode"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_f", "desc": "Formula F_y = F sin(theta)", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": f"Substitution: ({f_mag})sin({theta}°)", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"Correct value with unit: {_fmt_sa(fy)} N", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "The vertical component is opposite to the angle θ with the horizontal.",
            "2_concept": "Opposite side = Hypotenuse × sin(θ), so F_y = F × sin(θ).",
            "3_breakdown": f"F_y = {f_mag} × sin({theta}°) = {_fmt_sa(fy)} N.",
        },
    }


def build_28_resolve_vector_both_components_horizontal_reference(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate both horizontal and vertical components with seed-varied inline vector SVG."""
    r = _rng(seed)
    
    f_mag = r.randint(40, 120)
    theta = r.choice([25, 30, 40, 50, 60])
    theta_rad = math.radians(theta)
    
    fx = round(f_mag * math.cos(theta_rad), 2)
    fy = round(f_mag * math.sin(theta_rad), 2)
    
    scale_fac = 140.0 / f_mag
    svg_vectors = [
        {"dx": fx, "dy": 0, "start": (0, 0), "color": "#1e3a8a", "label": f"Fx = {_fmt_sa(fx)} N", "dashed": True},
        {"dx": 0, "dy": fy, "start": (fx, 0), "color": "#047857", "label": f"Fy = {_fmt_sa(fy)} N", "dashed": True},
        {"dx": fx, "dy": fy, "start": (0, 0), "color": "#b91c1c", "label": f"F = {f_mag} N ({theta}°)", "stroke_width": 3},
    ]
    svg_markup = _vector_svg(
        svg_vectors,
        origin=(80, 220),
        scale=scale_fac,
        width=500,
        height=280,
        show_compass=False,
        seed_tag=seed,
    )
    
    prompt = (
        f"Refer to the vector diagram showing a force F = {_fmt_sa(f_mag)} N acting at an angle of "
        f"{_fmt_sa(theta)}° to the positive horizontal axis.\n"
        f"1. Calculate the magnitude of the horizontal component (F_x).\n"
        f"2. Calculate the magnitude of the vertical component (F_y)."
    )
    
    calc_latex = (
        rf"1. F_x = F \cos\theta = ({_fmt_sa(f_mag)})\cos({theta}^\circ) = {_fmt_sa(fx)}\text{{ N}}\\"
        rf"2. F_y = F \sin\theta = ({_fmt_sa(f_mag)})\sin({theta}^\circ) = {_fmt_sa(fy)}\text{{ N}}"
    )
    
    return {
        "id": f"vec_28_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "28_resolve_vector_both_components_horizontal_reference",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg_markup,
            "diagram_role": "context",
        },
        "prompt": prompt,
        "ideal_answer": f"F_x = {_fmt_sa(fx)} N, F_y = {_fmt_sa(fy)} N",
        "sample_answer": calc_latex,
        "marks": 4,
        "misconception_tags": ["swapped_horizontal_and_vertical_components", "omitted_units"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_fx_f", "desc": "Formula F_x = F cos(theta)", "marks": 1, "editable": True},
                {"id": "mp_fx_a", "desc": f"F_x = {_fmt_sa(fx)} N", "marks": 1, "editable": True},
                {"id": "mp_fy_f", "desc": "Formula F_y = F sin(theta)", "marks": 1, "editable": True},
                {"id": "mp_fy_a", "desc": f"F_y = {_fmt_sa(fy)} N", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Horizontal uses cosine when the angle is with the horizontal. Vertical uses sine.",
            "2_concept": "F_x = F cos(θ) and F_y = F sin(θ).",
            "3_breakdown": f"F_x = {f_mag} cos({theta}°) = {_fmt_sa(fx)} N. F_y = {f_mag} sin({theta}°) = {_fmt_sa(fy)} N.",
        },
    }


def build_29_resolve_vector_angle_to_vertical(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Resolve vector components when the angle given is measured with respect to the vertical."""
    r = _rng(seed)
    
    f_mag = r.randint(35, 120)
    alpha = r.choice([20, 25, 30, 35, 40, 50]) # angle to vertical
    alpha_rad = math.radians(alpha)
    
    # Adjacent to vertical is Fy, opposite is Fx
    fy = round(f_mag * math.cos(alpha_rad), 2)
    fx = round(f_mag * math.sin(alpha_rad), 2)
    comp_angle = 90 - alpha
    
    prompt = (
        f"A pendulum bob is pulled aside by a string such that the tension force of {_fmt_sa(f_mag)} N in the string "
        f"makes an angle of {_fmt_sa(alpha)}° with the VERTICAL.\n"
        f"1. State the angle that the string makes with the horizontal.\n"
        f"2. Calculate the vertical component (T_y) of the tension force.\n"
        f"3. Calculate the horizontal component (T_x) of the tension force."
    )
    
    sample_answer = (
        rf"1. \text{{Angle with horizontal}} = 90^\circ - {alpha}^\circ = {comp_angle}^\circ\\"
        rf"2. T_y = T \cos({alpha}^\circ) = ({_fmt_sa(f_mag)})\cos({alpha}^\circ) = {_fmt_sa(fy)}\text{{ N}}\\"
        rf"3. T_x = T \sin({alpha}^\circ) = ({_fmt_sa(f_mag)})\sin({alpha}^\circ) = {_fmt_sa(fx)}\text{{ N}}"
    )
    
    return {
        "id": f"vec_29_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "29_resolve_vector_angle_to_vertical",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"Angle to horiz = {comp_angle}°; T_y = {_fmt_sa(fy)} N; T_x = {_fmt_sa(fx)} N",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["used_cos_for_horizontal_when_angle_is_to_vertical", "subtracted_from_180_instead_of_90"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_ang", "desc": f"Horizontal angle: 90° - {alpha}° = {comp_angle}°", "marks": 1, "editable": True},
                {"id": "mp_ty", "desc": f"Vertical component: T cos({alpha}°) = {_fmt_sa(fy)} N", "marks": 1, "editable": True},
                {"id": "mp_tx_f", "desc": f"Horizontal formula: T sin({alpha}°)", "marks": 1, "editable": True},
                {"id": "mp_tx_a", "desc": f"Horizontal value: {_fmt_sa(fx)} N", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Careful! The angle is given to the VERTICAL, so the vertical side is adjacent.",
            "2_concept": "When measured to vertical: T_y = T cos(α) and T_x = T sin(α).",
            "3_breakdown": f"T_y = {f_mag} cos({alpha}°) = {_fmt_sa(fy)} N; T_x = {f_mag} sin({alpha}°) = {_fmt_sa(fx)} N.",
        },
    }


def build_30_resolve_vector_bearing_reference(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Resolve a navigational displacement or velocity specified by bearing into North and East components."""
    r = _rng(seed)
    
    v_mag = r.randint(120, 350) # km/h
    bearing_deg = r.choice([30, 45, 60, 120, 135, 150])
    
    bearing_str = f"{bearing_deg:03d}°"
    bearing_rad = math.radians(bearing_deg)
    
    # True bearing: North component is v * cos(bearing), East component is v * sin(bearing)
    v_north = round(v_mag * math.cos(bearing_rad), 2)
    v_east = round(v_mag * math.sin(bearing_rad), 2)
    
    prompt = (
        f"An aircraft flies with an airspeed of {_fmt_sa(v_mag)} km·h⁻¹ on a true bearing of {bearing_str}.\n"
        f"1. Calculate the North component of the aircraft's velocity (v_N).\n"
        f"2. Calculate the East component of the aircraft's velocity (v_E)."
    )
    
    sample_answer = (
        f"For a true bearing θ measured clockwise from North:\n"
        rf"v_{{\text{{North}}}} = v \cos\theta = ({_fmt_sa(v_mag)})\cos({bearing_deg}^\circ) = {_fmt_sa(v_north)}\text{{ km·h}}^{{-1}}\\"
        rf"v_{{\text{{East}}}} = v \sin\theta = ({_fmt_sa(v_mag)})\sin({bearing_deg}^\circ) = {_fmt_sa(v_east)}\text{{ km·h}}^{{-1}}"
    )
    
    return {
        "id": f"vec_30_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "30_resolve_vector_bearing_reference",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"v_North = {_fmt_sa(v_north)} km·h⁻¹, v_East = {_fmt_sa(v_east)} km·h⁻¹",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["confused_bearing_components", "swapped_north_and_east_trig_functions"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_vn_f", "desc": "Formula v_North = v cos(bearing)", "marks": 1, "editable": True},
                {"id": "mp_vn_a", "desc": f"v_North = {_fmt_sa(v_north)} km·h⁻¹", "marks": 1, "editable": True},
                {"id": "mp_ve_f", "desc": "Formula v_East = v sin(bearing)", "marks": 1, "editable": True},
                {"id": "mp_ve_a", "desc": f"v_East = {_fmt_sa(v_east)} km·h⁻¹", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Bearings are measured from North, so the North component is the adjacent side (cosine).",
            "2_concept": "v_North = v cos(bearing), v_East = v sin(bearing).",
            "3_breakdown": f"v_North = {v_mag} cos({bearing_deg}°) = {_fmt_sa(v_north)} km·h⁻¹; v_East = {v_mag} sin({bearing_deg}°) = {_fmt_sa(v_east)} km·h⁻¹.",
        },
    }


def build_31_reconstruct_vector_from_components(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Reconstruct vector magnitude and direction from its rectangular components."""
    r = _rng(seed)
    
    fx = r.randint(18, 55)
    fy = r.randint(18, 55)
    
    f_mag = round(math.hypot(fx, fy), 2)
    theta = round(math.degrees(math.atan2(fy, fx)), 1)
    
    prompt = (
        f"A force has rectangular components F_x = +{_fmt_sa(fx)} N and F_y = +{_fmt_sa(fy)} N.\n"
        f"1. Calculate the magnitude of the force F.\n"
        f"2. Calculate the direction angle θ that the force makes with the positive x-axis."
    )
    
    calc_latex = (
        rf"1. F = \sqrt{{F_x^2 + F_y^2}} = \sqrt{{({_fmt_sa(fx)})^2 + ({_fmt_sa(fy)})^2}} = {_fmt_sa(f_mag)}\text{{ N}}\\"
        rf"2. \tan\theta = \frac{{F_y}}{{F_x}} = \frac{{{_fmt_sa(fy)}}}{{{_fmt_sa(fx)}}} \implies \theta = \arctan\left(\frac{{{_fmt_sa(fy)}}}{{{_fmt_sa(fx)}}}\right) = {_fmt_sa(theta)}^\circ"
    )
    
    return {
        "id": f"vec_31_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "31_reconstruct_vector_from_components",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"F = {_fmt_sa(f_mag)} N at {_fmt_sa(theta)}° above positive x-axis",
        "sample_answer": calc_latex,
        "marks": 4,
        "misconception_tags": ["inverted_tangent_ratio", "omitted_square_root_in_magnitude"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_f", "desc": "Formula F = sqrt(Fx^2 + Fy^2)", "marks": 1, "editable": True},
                {"id": "mp_mag", "desc": f"Magnitude F = {_fmt_sa(f_mag)} N", "marks": 1, "editable": True},
                {"id": "mp_trig", "desc": "Formula tan(theta) = Fy / Fx", "marks": 1, "editable": True},
                {"id": "mp_dir", "desc": f"Angle θ = {_fmt_sa(theta)}°", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Use Pythagoras theorem to combine Fx and Fy into the total magnitude.",
            "2_concept": "F = sqrt(Fx^2 + Fy^2), and tan(θ) = Fy / Fx.",
            "3_breakdown": f"F = sqrt({fx}^2 + {fy}^2) = {_fmt_sa(f_mag)} N. θ = arctan({fy}/{fx}) = {_fmt_sa(theta)}°.",
        },
    }


def build_32_component_sign_conventions_in_four_quadrants(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Determine algebraic signs (+ / -) of vector components in different Cartesian quadrants."""
    r = _rng(seed)
    
    quadrant = r.choice([2, 3, 4])
    if quadrant == 2:
        q_name = "Quadrant II (North-West: 90° to 180° / West of North)"
        sign_x, sign_y = "-", "+"
        ex_x, ex_y = -30, 40
        card_dir = "North-West"
    elif quadrant == 3:
        q_name = "Quadrant III (South-West: 180° to 270° / West of South)"
        sign_x, sign_y = "-", "-"
        ex_x, ex_y = -30, -40
        card_dir = "South-West"
    else:
        q_name = "Quadrant IV (South-East: 270° to 360° / East of South)"
        sign_x, sign_y = "+", "-"
        ex_x, ex_y = 30, -40
        card_dir = "South-East"
        
    prompt = (
        f"A displacement vector points into {q_name}.\n"
        f"1. Taking East as the positive x-direction and North as the positive y-direction, state the algebraic signs (+ or -) "
        f"of the horizontal component (Δx) and the vertical component (Δy).\n"
        f"2. If the magnitude of the displacement is 50 m directed into this quadrant with |Δx| = 30 m and |Δy| = 40 m, "
        f"write down the signed rectangular components (Δx; Δy)."
    )
    
    sample_answer = (
        f"1. In {q_name}:\n"
        f"   - Horizontal component (Δx) has a {sign_x} sign (pointing {'East (+)' if sign_x=='+' else 'West (-)'}).\n"
        f"   - Vertical component (Δy) has a {sign_y} sign (pointing {'North (+)' if sign_y=='+' else 'South (-)'}).\n"
        f"2. Signed components: (Δx; Δy) = ({ex_x} m; {ex_y} m)."
    )
    
    return {
        "id": f"vec_32_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "32_component_sign_conventions_in_four_quadrants",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"Δx sign: {sign_x}, Δy sign: {sign_y}; Components: ({ex_x} m; {ex_y} m)",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["sign_error_in_cartesian_components", "confused_quadrant_signs"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_x", "desc": f"Correct sign for Δx: {sign_x}", "marks": 1, "editable": True},
                {"id": "mp_y", "desc": f"Correct sign for Δy: {sign_y}", "marks": 1, "editable": True},
                {"id": "mp_pair", "desc": f"Signed component pair ({ex_x} m; {ex_y} m)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "East is positive x (+), West is negative x (-). North is positive y (+), South is negative y (-).",
            "2_concept": f"Points towards {card_dir}: check horizontal and vertical directions.",
            "3_breakdown": f"Δx is {sign_x}30 m; Δy is {sign_y}40 m.",
        },
    }


def build_33_multiple_vectors_algebraic_components_forces(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Find resultant of two concurrent forces using algebraic components table."""
    r = _rng(seed)
    
    # Vector 1: purely horizontal
    f1 = r.randint(30, 80) # N East (angle 0)
    # Vector 2: angled
    f2 = r.randint(40, 90) # N at theta North of East
    theta = r.choice([30, 45, 60])
    theta_rad = math.radians(theta)
    
    f1x, f1y = f1, 0.0
    f2x = round(f2 * math.cos(theta_rad), 2)
    f2y = round(f2 * math.sin(theta_rad), 2)
    
    rx = round(f1x + f2x, 2)
    ry = round(f1y + f2y, 2)
    
    r_mag = round(math.hypot(rx, ry), 2)
    r_theta = round(math.degrees(math.atan2(ry, rx)), 1)
    
    prompt = (
        f"Two concurrent forces act on a ring:\n"
        f"- Force 1: F_1 = {_fmt_sa(f1)} N acting due East (along the +x axis).\n"
        f"- Force 2: F_2 = {_fmt_sa(f2)} N acting at {_fmt_sa(theta)}° North of East.\n\n"
        f"1. Resolve Force 2 into horizontal (F_2x) and vertical (F_2y) components.\n"
        f"2. Calculate the sum of the horizontal forces (R_x) and the sum of the vertical forces (R_y).\n"
        f"3. Calculate the magnitude of the resultant force (R)."
    )
    
    calc_latex = (
        rf"1. F_{{2x}} = F_2 \cos({theta}^\circ) = ({_fmt_sa(f2)})\cos({theta}^\circ) = {_fmt_sa(f2x)}\text{{ N}}\\"
        rf"   F_{{2y}} = F_2 \sin({theta}^\circ) = ({_fmt_sa(f2)})\sin({theta}^\circ) = {_fmt_sa(f2y)}\text{{ N}}\\"
        rf"2. R_x = F_{{1x}} + F_{{2x}} = {_fmt_sa(f1)} + {_fmt_sa(f2x)} = {_fmt_sa(rx)}\text{{ N}}\\"
        rf"   R_y = F_{{1y}} + F_{{2y}} = 0 + {_fmt_sa(f2y)} = {_fmt_sa(ry)}\text{{ N}}\\"
        rf"3. R = \sqrt{{R_x^2 + R_y^2}} = \sqrt{{({_fmt_sa(rx)})^2 + ({_fmt_sa(ry)})^2}} = {_fmt_sa(r_mag)}\text{{ N}}"
    )
    
    return {
        "id": f"vec_33_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "33_multiple_vectors_algebraic_components_forces",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 6,
        "prompt": prompt,
        "ideal_answer": f"F_2x = {_fmt_sa(f2x)} N, F_2y = {_fmt_sa(f2y)} N; R_x = {_fmt_sa(rx)} N, R_y = {_fmt_sa(ry)} N; R = {_fmt_sa(r_mag)} N",
        "sample_answer": calc_latex,
        "marks": 5,
        "misconception_tags": ["added_vector_magnitudes_directly_without_components", "omitted_one_component_in_sum"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_res_x", "desc": f"F_2x = {_fmt_sa(f2x)} N", "marks": 1, "editable": True},
                {"id": "mp_res_y", "desc": f"F_2y = {_fmt_sa(f2y)} N", "marks": 1, "editable": True},
                {"id": "mp_rx", "desc": f"Sum of x-components R_x = {_fmt_sa(rx)} N", "marks": 1, "editable": True},
                {"id": "mp_ry", "desc": f"Sum of y-components R_y = {_fmt_sa(ry)} N", "marks": 1, "editable": True},
                {"id": "mp_r", "desc": f"Resultant magnitude R = {_fmt_sa(r_mag)} N", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "You cannot add vectors at different angles directly; resolve each vector into x and y components first.",
            "2_concept": "R_x = sum of all x-components; R_y = sum of all y-components. Then R = sqrt(Rx^2 + Ry^2).",
            "3_breakdown": f"F2x = {f2} cos({theta}°) = {_fmt_sa(f2x)} N. Rx = {f1} + {_fmt_sa(f2x)} = {_fmt_sa(rx)} N. R = sqrt({_fmt_sa(rx)}^2 + {_fmt_sa(ry)}^2) = {_fmt_sa(r_mag)} N.",
        },
    }


def build_34_multiple_vectors_algebraic_components_displacements(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Find net displacement of a hiker following two non-orthogonal legs using component summation."""
    r = _rng(seed)
    
    d1 = r.randint(4, 12) # km East
    d2 = r.randint(5, 15) # km at 45 deg North of East
    d2x = round(d2 * math.cos(math.radians(45)), 2)
    d2y = round(d2 * math.sin(math.radians(45)), 2)
    
    rx = round(d1 + d2x, 2)
    ry = round(d2y, 2)
    r_disp = round(math.hypot(rx, ry), 2)
    theta = round(math.degrees(math.atan2(ry, rx)), 1)
    
    prompt = (
        f"A hiker embarks on a two-leg trail:\n"
        f"- Leg 1: Walks {_fmt_sa(d1)} km due East.\n"
        f"- Leg 2: Walks {_fmt_sa(d2)} km at an angle of 45° North of East.\n\n"
        f"1. Calculate the components of Leg 2 (d_2x and d_2y).\n"
        f"2. Calculate the resultant displacement components (R_x and R_y).\n"
        f"3. Calculate the magnitude of the hiker's resultant displacement from the starting point."
    )
    
    calc_latex = (
        rf"1. d_{{2x}} = ({_fmt_sa(d2)})\cos(45^\circ) = {_fmt_sa(d2x)}\text{{ km}}\\"
        rf"   d_{{2y}} = ({_fmt_sa(d2)})\sin(45^\circ) = {_fmt_sa(d2y)}\text{{ km}}\\"
        rf"2. R_x = {_fmt_sa(d1)} + {_fmt_sa(d2x)} = {_fmt_sa(rx)}\text{{ km}}\\"
        rf"   R_y = 0 + {_fmt_sa(d2y)} = {_fmt_sa(ry)}\text{{ km}}\\"
        rf"3. R = \sqrt{{({_fmt_sa(rx)})^2 + ({_fmt_sa(ry)})^2}} = {_fmt_sa(r_disp)}\text{{ km}}"
    )
    
    return {
        "id": f"vec_34_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "34_multiple_vectors_algebraic_components_displacements",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"R = {_fmt_sa(r_disp)} km (Rx = {_fmt_sa(rx)} km, Ry = {_fmt_sa(ry)} km)",
        "sample_answer": calc_latex,
        "marks": 5,
        "misconception_tags": ["added_distances_instead_of_vector_components", "omitted_leg1_in_rx"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_d2x", "desc": f"d_2x = {_fmt_sa(d2x)} km", "marks": 1, "editable": True},
                {"id": "mp_d2y", "desc": f"d_2y = {_fmt_sa(d2y)} km", "marks": 1, "editable": True},
                {"id": "mp_rx", "desc": f"R_x = {_fmt_sa(rx)} km", "marks": 1, "editable": True},
                {"id": "mp_ry", "desc": f"R_y = {_fmt_sa(ry)} km", "marks": 1, "editable": True},
                {"id": "mp_r", "desc": f"Resultant magnitude R = {_fmt_sa(r_disp)} km", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Break the second leg into its East and North components using sin(45°) and cos(45°).",
            "2_concept": "Add the East component of Leg 1 to the East component of Leg 2. Then apply Pythagoras.",
            "3_breakdown": f"Rx = {d1} + {_fmt_sa(d2x)} = {_fmt_sa(rx)} km. Ry = {_fmt_sa(ry)} km. R = sqrt({_fmt_sa(rx)}^2 + {_fmt_sa(ry)}^2) = {_fmt_sa(r_disp)} km.",
        },
    }


def build_35_three_coplanar_forces_component_sum(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate resultant of three coplanar concurrent forces along axes."""
    r = _rng(seed)
    
    f_east = r.randint(40, 90)
    f_west = r.randint(15, 35)
    f_north = r.randint(30, 80)
    
    rx = f_east - f_west
    ry = f_north
    r_mag = round(math.hypot(rx, ry), 2)
    theta = round(math.degrees(math.atan2(ry, rx)), 1)
    
    prompt = (
        f"Three coplanar forces act concurrently on a central pin:\n"
        f"- F_1 = {_fmt_sa(f_east)} N due East\n"
        f"- F_2 = {_fmt_sa(f_west)} N due West\n"
        f"- F_3 = {_fmt_sa(f_north)} N due North\n\n"
        f"1. Calculate the sum of the horizontal components (ΣF_x).\n"
        f"2. Calculate the sum of the vertical components (ΣF_y).\n"
        f"3. Calculate the magnitude and direction of the resultant force."
    )
    
    calc_latex = (
        rf"1. \Sigma F_x = {_fmt_sa(f_east)} - {_fmt_sa(f_west)} = +{_fmt_sa(rx)}\text{{ N (East)}}\\"
        rf"2. \Sigma F_y = +{_fmt_sa(f_north)}\text{{ N (North)}}\\"
        rf"3. R = \sqrt{{(\Sigma F_x)^2 + (\Sigma F_y)^2}} = \sqrt{{({_fmt_sa(rx)})^2 + ({_fmt_sa(ry)})^2}} = {_fmt_sa(r_mag)}\text{{ N}}\\"
        rf"\theta = \arctan\left(\frac{{{_fmt_sa(ry)}}}{{{_fmt_sa(rx)}}}\right) = {_fmt_sa(theta)}^\circ\text{{ North of East}}"
    )
    
    return {
        "id": f"vec_35_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "35_three_coplanar_forces_component_sum",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"R = {_fmt_sa(r_mag)} N at {_fmt_sa(theta)}° North of East",
        "sample_answer": calc_latex,
        "marks": 5,
        "misconception_tags": ["added_west_force_as_positive", "omitted_direction_in_resultant"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_rx", "desc": f"Net horizontal force ΣF_x = {_fmt_sa(rx)} N", "marks": 1, "editable": True},
                {"id": "mp_ry", "desc": f"Net vertical force ΣF_y = {_fmt_sa(ry)} N", "marks": 1, "editable": True},
                {"id": "mp_pyth_sub", "desc": "Pythagoras formula and substitution", "marks": 1, "editable": True},
                {"id": "mp_rmag", "desc": f"Resultant magnitude = {_fmt_sa(r_mag)} N", "marks": 1, "editable": True},
                {"id": "mp_rdir", "desc": f"Resultant direction = {_fmt_sa(theta)}° North of East", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "East and West are on the same line: subtract the West force from the East force.",
            "2_concept": "ΣFx = East - West. ΣFy = North. Then use Pythagoras and tan(θ) = ΣFy / ΣFx.",
            "3_breakdown": f"Rx = {f_east} - {f_west} = {rx} N. Ry = {f_north} N. R = sqrt({rx}^2 + {f_north}^2) = {_fmt_sa(r_mag)} N.",
        },
    }


def build_36_resultant_magnitude_and_direction_from_sum_components(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Complete determination of resultant magnitude and compass direction from net components."""
    r = _rng(seed)
    
    rx = r.randint(25, 75)
    ry = r.randint(25, 75)
    r_mag = round(math.hypot(rx, ry), 2)
    theta = round(math.degrees(math.atan2(ry, rx)), 1)
    
    prompt = (
        f"A system of concurrent forces resolves to a total horizontal component ΣF_x = +{_fmt_sa(rx)} N (East) "
        f"and a total vertical component ΣF_y = +{_fmt_sa(ry)} N (North).\n"
        f"1. Calculate the magnitude of the resultant force (R).\n"
        f"2. Calculate the direction of the resultant force, expressing your answer in the form: East θ° North."
    )
    
    calc_latex = (
        rf"1. R = \sqrt{{(\Sigma F_x)^2 + (\Sigma F_y)^2}} = \sqrt{{({_fmt_sa(rx)})^2 + ({_fmt_sa(ry)})^2}} = {_fmt_sa(r_mag)}\text{{ N}}\\"
        rf"2. \tan\theta = \frac{{\Sigma F_y}}{{\Sigma F_x}} = \frac{{{_fmt_sa(ry)}}}{{{_fmt_sa(rx)}}}\\"
        rf"\theta = \arctan\left(\frac{{{_fmt_sa(ry)}}}{{{_fmt_sa(rx)}}}\right) = {_fmt_sa(theta)}^\circ\\"
        f"Direction = East {_fmt_sa(theta)}° North (E {_fmt_sa(theta)}° N)."
    )
    
    return {
        "id": f"vec_36_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "36_resultant_magnitude_and_direction_from_sum_components",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"R = {_fmt_sa(r_mag)} N, Direction: E {_fmt_sa(theta)}° N",
        "sample_answer": calc_latex,
        "marks": 4,
        "misconception_tags": ["inverted_tangent_ratio", "omitted_direction_in_resultant"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_pyth_f", "desc": "Formula R = sqrt(Rx^2 + Ry^2)", "marks": 1, "editable": True},
                {"id": "mp_mag", "desc": f"Magnitude R = {_fmt_sa(r_mag)} N", "marks": 1, "editable": True},
                {"id": "mp_trig_f", "desc": "Formula tan(theta) = Ry / Rx", "marks": 1, "editable": True},
                {"id": "mp_dir", "desc": f"Compass direction: E {_fmt_sa(theta)}° N", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Rx is East and Ry is North.",
            "2_concept": "Apply Pythagoras for magnitude and tan(θ) = Ry / Rx for the angle.",
            "3_breakdown": f"R = sqrt({rx}^2 + {ry}^2) = {_fmt_sa(r_mag)} N. θ = arctan({ry}/{rx}) = {_fmt_sa(theta)}° North of East.",
        },
    }


def build_37_equilibrant_vector_definition_and_relation(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Define the equilibrant vector and state its mechanical relationship to the resultant vector."""
    r = _rng(seed)
    
    r_mag = r.randint(20, 80)
    direction = r.choice(["due East", "due North", "30° North of East", "due West"])
    
    opp_dict = {
        "due East": "due West",
        "due North": "due South",
        "30° North of East": "30° South of West (or 210° bearing)",
        "due West": "due East",
    }
    eq_dir = opp_dict[direction]
    
    prompt = (
        f"1. Define the term 'equilibrant' of a system of vectors.\n"
        f"2. A system of forces has a resultant of {_fmt_sa(r_mag)} N {direction}. "
        f"State the magnitude and direction of the equilibrant vector of this system.\n"
        f"3. What is the vector sum of the resultant vector and the equilibrant vector?"
    )
    
    sample_answer = (
        "1. Definition: The equilibrant is the single vector that has the SAME magnitude as the resultant vector, but acts in the OPPOSITE direction.\n"
        f"2. Equilibrant Magnitude: {_fmt_sa(r_mag)} N.\n"
        f"   Equilibrant Direction: {eq_dir}.\n"
        rf"3. Vector sum: \vec{{R}} + \vec{{E}} = \vec{{R}} + (-\vec{{R}}) = \vec{{0}}\text{{ (Zero / balanced system in static equilibrium)}}."
    )
    
    return {
        "id": f"vec_37_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "37_equilibrant_vector_definition_and_relation",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"Equilibrant: {_fmt_sa(r_mag)} N {eq_dir}; Vector sum = 0 N",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["thought_equilibrant_has_different_magnitude", "omitted_opposite_direction_in_equilibrant"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_def", "desc": "Definition: same magnitude but opposite direction to resultant", "marks": 2, "editable": True},
                {"id": "mp_val", "desc": f"Equilibrant: {_fmt_sa(r_mag)} N {eq_dir}", "marks": 1, "editable": True},
                {"id": "mp_sum", "desc": "Sum R + E = 0 (equilibrium)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "The equilibrant balances the resultant so the object is in equilibrium.",
            "2_concept": "Equilibrant magnitude = Resultant magnitude. Equilibrant direction = opposite to resultant.",
            "3_breakdown": f"Equilibrant is {_fmt_sa(r_mag)} N in the opposite direction ({eq_dir}). R + E = 0.",
        },
    }


def build_38_find_equilibrant_collinear_system(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Determine equilibrant for a 1D system of forces along a straight line."""
    r = _rng(seed)
    
    f1 = r.randint(40, 90) # N to right
    f2 = r.randint(15, 35) # N to left
    
    r_val = f1 - f2
    r_dir = "to the right"
    eq_val = r_val
    eq_dir = "to the left"
    
    prompt = (
        f"Two horizontal forces act on a stationary block: F_1 = {_fmt_sa(f1)} N to the right, and F_2 = {_fmt_sa(f2)} N to the left.\n"
        f"1. Calculate the resultant force (F_net) acting on the block, stating magnitude and direction.\n"
        f"2. Determine the magnitude and direction of the equilibrant force required to keep the block in static equilibrium."
    )
    
    sample_answer = (
        rf"1. F_{{\text{{net}}}} = {_fmt_sa(f1)} - {_fmt_sa(f2)} = {_fmt_sa(r_val)}\text{{ N to the right}}\\"
        f"2. The equilibrant has the same magnitude but opposite direction to F_net:\n"
        rf"   F_{{\text{{equilibrant}}}} = {_fmt_sa(eq_val)}\text{{ N {eq_dir}}}."
    )
    
    return {
        "id": f"vec_38_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "38_find_equilibrant_collinear_system",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 3,
        "prompt": prompt,
        "ideal_answer": f"F_net = {_fmt_sa(r_val)} N right; Equilibrant = {_fmt_sa(eq_val)} N left",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["confused_equilibrant_direction_with_resultant_direction"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Resultant = {_fmt_sa(r_val)} N to the right", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Equilibrant magnitude = {_fmt_sa(eq_val)} N", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Equilibrant direction = {eq_dir}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_direction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "First find the net force by subtracting the opposing forces.",
            "2_concept": "The equilibrant points in the opposite direction to the net force.",
            "3_breakdown": f"Net force = {f1} - {f2} = {r_val} N right. Equilibrant = {eq_val} N left.",
        },
    }


def build_39_find_equilibrant_perpendicular_forces(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Determine magnitude and direction of equilibrant for two perpendicular forces."""
    r = _rng(seed)
    
    k = r.choice([2, 3, 4, 5, 10])
    fx = 3 * k # N East
    fy = 4 * k # N North
    fr = 5 * k # N
    
    theta_r = round(math.degrees(math.atan2(fy, fx)), 1) # ~ 53.1 deg North of East
    # Equilibrant is South of West
    eq_dir = f"{_fmt_sa(theta_r)}° South of West (or W {_fmt_sa(theta_r)}° S)"
    
    prompt = (
        f"Two perpendicular forces act on a body: F_x = {_fmt_sa(fx)} N East and F_y = {_fmt_sa(fy)} N North.\n"
        f"1. Calculate the magnitude of the resultant force R.\n"
        f"2. Calculate the direction of the resultant force relative to the East axis.\n"
        f"3. Write down the magnitude and direction of the equilibrant force."
    )
    
    calc_latex = (
        rf"1. R = \sqrt{{({_fmt_sa(fx)})^2 + ({_fmt_sa(fy)})^2}} = {_fmt_sa(fr)}\text{{ N}}\\"
        rf"2. \theta = \arctan\left(\frac{{{_fmt_sa(fy)}}}{{{_fmt_sa(fx)}}}\right) = {_fmt_sa(theta_r)}^\circ\text{{ North of East}}\\"
        f"3. Equilibrant has equal magnitude and exactly opposite direction:\n"
        rf"   E = {_fmt_sa(fr)}\text{{ N directed at }} {eq_dir}."
    )
    
    return {
        "id": f"vec_39_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "39_find_equilibrant_perpendicular_forces",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"R = {_fmt_sa(fr)} N ({_fmt_sa(theta_r)}° N of E); Equilibrant = {_fmt_sa(fr)} N ({eq_dir})",
        "sample_answer": calc_latex,
        "marks": 5,
        "misconception_tags": ["reversed_only_one_axis_for_equilibrant", "confused_equilibrant_magnitude"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_pyth", "desc": f"Resultant magnitude = {_fmt_sa(fr)} N", "marks": 2, "editable": True},
                {"id": "mp_rdir", "desc": f"Resultant direction = {_fmt_sa(theta_r)}° North of East", "marks": 1, "editable": True},
                {"id": "mp_emag", "desc": f"Equilibrant magnitude = {_fmt_sa(fr)} N", "marks": 1, "editable": True},
                {"id": "mp_edir", "desc": f"Equilibrant direction = {eq_dir}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "The equilibrant must reverse BOTH the East and North components (becoming West and South).",
            "2_concept": "Resultant = 53,1° North of East; Equilibrant = 53,1° South of West with equal magnitude.",
            "3_breakdown": f"R = {fr} N at {_fmt_sa(theta_r)}° N of E. E = {fr} N at {_fmt_sa(theta_r)}° S of W.",
        },
    }


def build_40_find_equilibrant_angled_force_system(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Determine equilibrant for a system of forces resolved from arbitrary components."""
    r = _rng(seed)
    
    rx = r.randint(20, 60)
    ry = r.randint(20, 60)
    r_mag = round(math.hypot(rx, ry), 2)
    theta = round(math.degrees(math.atan2(ry, rx)), 1)
    
    prompt = (
        f"A system of concurrent forces produces a resultant force of {_fmt_sa(r_mag)} N at an angle of "
        f"{_fmt_sa(theta)}° North of East.\n"
        f"1. State the magnitude of the equilibrant of this force system.\n"
        f"2. State the direction of the equilibrant in terms of compass directions (South of West).\n"
        f"3. Calculate the bearing of the equilibrant vector."
    )
    
    bearing_r = 90 - theta
    bearing_e = round(bearing_r + 180)
    bearing_e_str = f"{bearing_e:03d}°"
    
    sample_answer = (
        f"1. Equilibrant magnitude = {_fmt_sa(r_mag)} N (identical to resultant magnitude).\n"
        f"2. Compass direction: {_fmt_sa(theta)}° South of West (W {_fmt_sa(theta)}° S).\n"
        rf"3. Bearing of resultant = 90^\circ - {_fmt_sa(theta)}^\circ = {round(bearing_r):03d}^\circ.\\"
        rf"   \text{{Bearing of equilibrant}} = {round(bearing_r):03d}^\circ + 180^\circ = {bearing_e_str}."
    )
    
    return {
        "id": f"vec_40_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "40_find_equilibrant_angled_force_system",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"E = {_fmt_sa(r_mag)} N, {_fmt_sa(theta)}° South of West, Bearing = {bearing_e_str}",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["added_90_instead_of_180_for_opposite_bearing"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_emag", "desc": f"Equilibrant magnitude: {_fmt_sa(r_mag)} N", "marks": 1, "editable": True},
                {"id": "mp_edir", "desc": f"Compass direction: {_fmt_sa(theta)}° South of West", "marks": 1, "editable": True},
                {"id": "mp_ebearing", "desc": f"Bearing = {bearing_e_str}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_leading_zero", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Opposite bearing is found by adding 180° to the resultant bearing.",
            "2_concept": "Resultant and equilibrant lie along the same straight line in opposite directions.",
            "3_breakdown": f"Magnitude is {_fmt_sa(r_mag)} N. Bearing = resultant bearing + 180° = {bearing_e_str}.",
        },
    }


def build_41_equilibrium_concurrent_forces_closed_triangle(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Understand the condition of static equilibrium as a closed vector polygon/triangle."""
    r = _rng(seed)
    
    prompt = (
        "Three concurrent forces (F_1, F_2, F_3) act on a body in static equilibrium.\n"
        "1. Write down the vector mathematical condition for equilibrium in terms of the net force.\n"
        "2. Explain what happens when these three forces are drawn tail-to-head in a vector diagram.\n"
        "3. What is the magnitude of the resultant force of any system in equilibrium?"
    )
    
    sample_answer = (
        rf"1. Mathematical Condition: \vec{{F}}_{{\text{{net}}}} = \vec{{F}}_1 + \vec{{F}}_2 + \vec{{F}}_3 = \vec{{0}}\text{{ (or }}\Sigma F_x = 0\text{{ and }}\Sigma F_y = 0).\n"
        "2. Graphical Representation: When the vectors are drawn tail-to-head, they form a CLOSED TRIANGLE (or closed polygon). "
        "The head of the final vector (F_3) ends exactly at the tail of the first vector (F_1), resulting in zero gap between start and end.\n"
        "3. Magnitude of Resultant: R = 0 N."
    )
    
    return {
        "id": f"vec_41_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "41_equilibrium_concurrent_forces_closed_triangle",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": "F_net = 0; forces form a closed vector triangle; resultant magnitude is 0 N.",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["open_polygon_in_equilibrium", "confused_closed_triangle_with_pythagoras"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_eq", "desc": "Vector condition: F_net = F1 + F2 + F3 = 0", "marks": 1, "editable": True},
                {"id": "mp_geom", "desc": "Head of last vector meets tail of first to form a closed triangle", "marks": 1, "editable": True},
                {"id": "mp_res", "desc": "Resultant magnitude is 0 N", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "If an object is in equilibrium, what is its net acceleration and net force?",
            "2_concept": "Net force is zero. When vectors add to zero tail-to-head, they close the shape completely.",
            "3_breakdown": "Condition: F_net = 0. Geometry: closed triangle. Resultant: 0 N.",
        },
    }


def build_42_three_forces_equilibrium_solve_unknown_force(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Solve for unknown third force that keeps two known perpendicular forces in static equilibrium."""
    r = _rng(seed)
    
    k = r.choice([2, 3, 5, 8, 10])
    f1 = 3 * k # N East
    f2 = 4 * k # N North
    f3_mag = 5 * k # N Equilibrant
    theta = round(math.degrees(math.atan2(f2, f1)), 1)
    
    prompt = (
        f"A small metal ring on a test board is in static equilibrium under the action of three coplanar forces:\n"
        f"- F_1 = {_fmt_sa(f1)} N acting due East\n"
        f"- F_2 = {_fmt_sa(f2)} N acting due North\n"
        f"- F_3 is an unknown third force acting on the ring.\n\n"
        f"1. Explain why F_3 is the equilibrant of F_1 and F_2.\n"
        f"2. Calculate the magnitude of F_3.\n"
        f"3. State the direction of F_3."
    )
    
    sample_answer = (
        rf"1. For equilibrium, \vec{{F}}_1 + \vec{{F}}_2 + \vec{{F}}_3 = \vec{{0}} \implies \vec{{F}}_3 = -(\vec{{F}}_1 + \vec{{F}}_2) = -\vec{{R}}_{{1,2}}. "
        f"Therefore, F_3 balances the resultant of F_1 and F_2, making it the equilibrant.\n"
        rf"2. F_3 = \sqrt{{F_1^2 + F_2^2}} = \sqrt{{({_fmt_sa(f1)})^2 + ({_fmt_sa(f2)})^2}} = {_fmt_sa(f3_mag)}\text{{ N}}\\"
        rf"3. Direction: The resultant of F_1 and F_2 is {_fmt_sa(theta)}^\circ\text{{ North of East}}. "
        f"Therefore, F_3 points in the exact opposite direction: {_fmt_sa(theta)}° South of West."
    )
    
    return {
        "id": f"vec_42_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "42_three_forces_equilibrium_solve_unknown_force",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"F_3 = {_fmt_sa(f3_mag)} N at {_fmt_sa(theta)}° South of West",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["forgot_opposite_direction_for_f3", "pythagoras_error"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_equil", "desc": "Explained F3 = -R12 (equilibrant of F1 and F2)", "marks": 1, "editable": True},
                {"id": "mp_pyth", "desc": "Pythagoras calculation for magnitude", "marks": 1, "editable": True},
                {"id": "mp_mag", "desc": f"F_3 magnitude = {_fmt_sa(f3_mag)} N", "marks": 1, "editable": True},
                {"id": "mp_dir", "desc": f"F_3 direction = {_fmt_sa(theta)}° South of West", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "For the ring to be balanced, F3 must cancel out the resultant of F1 and F2.",
            "2_concept": "F3 has the same magnitude as sqrt(F1^2 + F2^2) and points opposite to their resultant.",
            "3_breakdown": f"F3 magnitude = sqrt({f1}^2 + {f2}^2) = {f3_mag} N. Direction = {_fmt_sa(theta)}° South of West.",
        },
    }


def build_43_suspended_object_symmetrical_cable_tensions(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate tension in two symmetrical cables supporting a suspended weight: 2T*sin(theta) = W."""
    r = _rng(seed)
    
    mass_kg = r.randint(10, 40)
    w = round(mass_kg * 9.8, 1)
    theta = r.choice([30, 45, 60]) # angle to ceiling
    theta_rad = math.radians(theta)
    
    # 2 * T * sin(theta) = W  => T = W / (2 * sin(theta))
    t_val = round(w / (2 * math.sin(theta_rad)), 2)
    
    prompt = (
        f"A heavy chandelier of mass {_fmt_sa(mass_kg)} kg is suspended in static equilibrium by two identical "
        f"symmetrical steel cables attached to a horizontal ceiling. Each cable makes an angle of {_fmt_sa(theta)}° "
        f"with the horizontal ceiling. Taking g = 9,8 m·s⁻²:\n"
        f"1. Calculate the weight of the chandelier (W).\n"
        f"2. Write down the equation for the vertical equilibrium of the hanging point.\n"
        f"3. Calculate the tension (T) in each cable."
    )
    
    calc_latex = (
        rf"1. W = m g = ({_fmt_sa(mass_kg)})(9{{,}}8) = {_fmt_sa(w)}\text{{ N}}\\"
        rf"2. \Sigma F_y = 0 \implies 2 T \sin({theta}^\circ) - W = 0 \implies 2 T \sin({theta}^\circ) = W\\"
        rf"3. T = \frac{{W}}{{2 \sin({theta}^\circ)}} = \frac{{{_fmt_sa(w)}}}{{2 \sin({theta}^\circ)}} = {_fmt_sa(t_val)}\text{{ N}}"
    )
    
    return {
        "id": f"vec_43_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "43_suspended_object_symmetrical_cable_tensions",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 6,
        "prompt": prompt,
        "ideal_answer": f"W = {_fmt_sa(w)} N; T = {_fmt_sa(t_val)} N in each cable",
        "sample_answer": calc_latex,
        "marks": 5,
        "misconception_tags": ["forgot_factor_of_two_for_two_cables", "confused_sin_and_cos_with_ceiling_angle"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_w", "desc": f"Weight W = mg = {_fmt_sa(w)} N", "marks": 1, "editable": True},
                {"id": "mp_eq_f", "desc": "Equilibrium equation 2T sin(theta) = W", "marks": 2, "editable": True},
                {"id": "mp_sub", "desc": f"Substitution: T = {w} / (2 sin({theta}°))", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"Tension T = {_fmt_sa(t_val)} N", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Both cables pull upwards with vertical component T sin(θ). Together they balance the weight W.",
            "2_concept": "Vertical equilibrium: 2 × T × sin(θ) = W.",
            "3_breakdown": f"W = {mass_kg} × 9,8 = {_fmt_sa(w)} N. T = {w} / (2 sin({theta}°)) = {_fmt_sa(t_val)} N.",
        },
    }


def build_44_suspended_object_horizontal_pull_tension(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Object suspended on a string deflected by horizontal pull force F."""
    r = _rng(seed)
    
    mass_kg = r.randint(2, 10)
    w = round(mass_kg * 9.8, 1)
    theta = r.choice([20, 25, 30, 35, 40]) # angle to vertical
    theta_rad = math.radians(theta)
    
    # T * cos(theta) = W => T = W / cos(theta)
    # T * sin(theta) = F => F = W * tan(theta)
    t_val = round(w / math.cos(theta_rad), 2)
    f_pull = round(w * math.tan(theta_rad), 2)
    
    prompt = (
        f"A small brass sphere of mass {_fmt_sa(mass_kg)} kg hangs from a light string attached to the ceiling. "
        f"A horizontal force F is applied to the sphere, deflecting the string so that it rests in static equilibrium "
        f"at an angle of {_fmt_sa(theta)}° to the VERTICAL. Taking g = 9,8 m·s⁻²:\n"
        f"1. Calculate the gravitational force (weight W) acting on the sphere.\n"
        f"2. Calculate the tension T in the deflected string.\n"
        f"3. Calculate the magnitude of the horizontal applied force F."
    )
    
    calc_latex = (
        rf"1. W = m g = ({_fmt_sa(mass_kg)})(9{{,}}8) = {_fmt_sa(w)}\text{{ N}}\\"
        rf"2. \Sigma F_y = 0 \implies T \cos({theta}^\circ) = W \implies T = \frac{{{_fmt_sa(w)}}}{{\cos({theta}^\circ)}} = {_fmt_sa(t_val)}\text{{ N}}\\"
        rf"3. \Sigma F_x = 0 \implies F = T \sin({theta}^\circ) = W \tan({theta}^\circ) = {_fmt_sa(f_pull)}\text{{ N}}"
    )
    
    return {
        "id": f"vec_44_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "44_suspended_object_horizontal_pull_tension",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 6,
        "prompt": prompt,
        "ideal_answer": f"W = {_fmt_sa(w)} N; T = {_fmt_sa(t_val)} N; F = {_fmt_sa(f_pull)} N",
        "sample_answer": calc_latex,
        "marks": 5,
        "misconception_tags": ["swapped_sin_and_cos_for_vertical_angle", "assumed_tension_equals_weight"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_w", "desc": f"Weight W = {_fmt_sa(w)} N", "marks": 1, "editable": True},
                {"id": "mp_t_f", "desc": "Formula T cos(theta) = W", "marks": 1, "editable": True},
                {"id": "mp_t_a", "desc": f"Tension T = {_fmt_sa(t_val)} N", "marks": 1, "editable": True},
                {"id": "mp_f_f", "desc": "Formula F = T sin(theta) or W tan(theta)", "marks": 1, "editable": True},
                {"id": "mp_f_a", "desc": f"Horizontal force F = {_fmt_sa(f_pull)} N", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "The angle θ is to the vertical, so T cos(θ) balances the downward weight.",
            "2_concept": "Vertical equilibrium: T cos(θ) = W. Horizontal equilibrium: F = T sin(θ).",
            "3_breakdown": f"T = {w} / cos({theta}°) = {_fmt_sa(t_val)} N. F = {w} × tan({theta}°) = {_fmt_sa(f_pull)} N.",
        },
    }


def build_45_navigation_boat_crossing_flowing_river(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate resultant velocity and heading of a motorboat crossing a flowing river."""
    r = _rng(seed)
    
    v_boat = r.randint(4, 9) # m/s due North
    v_river = r.randint(2, 6) # m/s due East
    
    v_res = round(math.hypot(v_boat, v_river), 2)
    theta = round(math.degrees(math.atan2(v_river, v_boat)), 1) # angle from North towards East
    
    prompt = (
        f"A motorboat points directly across a river, moving through the water with an engine speed of "
        f"{_fmt_sa(v_boat)} m·s⁻¹ due North. The river flows at {_fmt_sa(v_river)} m·s⁻¹ due East.\n"
        f"1. Calculate the magnitude of the boat's resultant velocity relative to the riverbank.\n"
        f"2. Calculate the direction of the resultant velocity as an angle measured East of North."
    )
    
    calc_latex = (
        rf"1. v_{{\text{{res}}}} = \sqrt{{v_{{\text{{boat}}}}^2 + v_{{\text{{river}}}}^2}} = \sqrt{{({_fmt_sa(v_boat)})^2 + ({_fmt_sa(v_river)})^2}} = {_fmt_sa(v_res)}\text{{ m·s}}^{{-1}}\\"
        rf"2. \tan\theta = \frac{{v_{{\text{{river}}}}}}{{v_{{\text{{boat}}}}}} = \frac{{{_fmt_sa(v_river)}}}{{{_fmt_sa(v_boat)}}}\\"
        rf"\theta = \arctan\left(\frac{{{_fmt_sa(v_river)}}}{{{_fmt_sa(v_boat)}}}\right) = {_fmt_sa(theta)}^\circ\text{{ East of North}}"
    )
    
    return {
        "id": f"vec_45_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "45_navigation_boat_crossing_flowing_river",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"v_res = {_fmt_sa(v_res)} m·s⁻¹ at {_fmt_sa(theta)}° East of North",
        "sample_answer": calc_latex,
        "marks": 4,
        "misconception_tags": ["added_speeds_linearly_for_river_crossing", "inverted_river_drift_tangent"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_pyth", "desc": "Pythagoras formula and substitution", "marks": 1, "editable": True},
                {"id": "mp_mag", "desc": f"Resultant speed = {_fmt_sa(v_res)} m·s⁻¹", "marks": 1, "editable": True},
                {"id": "mp_trig", "desc": "Tangent formula tan(theta) = v_river / v_boat", "marks": 1, "editable": True},
                {"id": "mp_dir", "desc": f"Direction = {_fmt_sa(theta)}° East of North", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "The boat moves North while the current carries it East. These velocities are perpendicular.",
            "2_concept": "v_res = sqrt(v_boat^2 + v_river^2), and tan(θ) = v_river / v_boat.",
            "3_breakdown": f"v_res = sqrt({v_boat}^2 + {v_river}^2) = {_fmt_sa(v_res)} m·s⁻¹. θ = arctan({v_river}/{v_boat}) = {_fmt_sa(theta)}° East of North.",
        },
    }


def build_46_navigation_boat_river_drift_distance(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate crossing time and downstream drift distance for river crossing."""
    r = _rng(seed)
    
    width_m = r.choice([60, 80, 100, 120, 150]) # width across
    v_boat = r.choice([3, 4, 5, 6]) # m/s across
    v_river = r.choice([2, 2.5, 3, 3.5]) # m/s downstream
    
    t_cross = round(width_m / v_boat, 1)
    d_drift = round(v_river * t_cross, 1)
    
    prompt = (
        f"A river is {_fmt_sa(width_m)} m wide and flows downstream at {_fmt_sa(v_river)} m·s⁻¹ due East. "
        f"A boat steers directly across the river due North with a speed of {_fmt_sa(v_boat)} m·s⁻¹ relative to the water.\n"
        f"1. Calculate the time taken for the boat to reach the opposite bank.\n"
        f"2. Calculate the distance downstream that the boat is carried by the river current during the crossing."
    )
    
    calc_latex = (
        rf"1. \Delta t = \frac{{\text{{Width}}}}{{v_{{\text{{boat}}}}}} = \frac{{{_fmt_sa(width_m)}}}{{{_fmt_sa(v_boat)}}} = {_fmt_sa(t_cross)}\text{{ s}}\\"
        rf"2. d_{{\text{{drift}}}} = v_{{\text{{river}}}} \times \Delta t = ({_fmt_sa(v_river)})({_fmt_sa(t_cross)}) = {_fmt_sa(d_drift)}\text{{ m downstream}}"
    )
    
    return {
        "id": f"vec_46_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "46_navigation_boat_river_drift_distance",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"Time = {_fmt_sa(t_cross)} s; Drift distance = {_fmt_sa(d_drift)} m downstream",
        "sample_answer": calc_latex,
        "marks": 4,
        "misconception_tags": ["used_resultant_speed_to_find_crossing_time", "omitted_units"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_t_f", "desc": "Formula t = width / v_boat (independent components)", "marks": 1, "editable": True},
                {"id": "mp_t_a", "desc": f"Time = {_fmt_sa(t_cross)} s", "marks": 1, "editable": True},
                {"id": "mp_d_f", "desc": "Formula d_drift = v_river * t", "marks": 1, "editable": True},
                {"id": "mp_d_a", "desc": f"Drift distance = {_fmt_sa(d_drift)} m", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "The river flow does not affect the time to cross because the two velocities are perpendicular (independent).",
            "2_concept": "Time to cross = Width / v_boat. Downstream distance = v_river × time.",
            "3_breakdown": f"Time = {width_m} / {v_boat} = {_fmt_sa(t_cross)} s. Drift = {v_river} × {t_cross} = {_fmt_sa(d_drift)} m.",
        },
    }


def build_47_navigation_aircraft_crosswind_ground_speed(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate ground speed and true track bearing of an aircraft in a perpendicular crosswind."""
    r = _rng(seed)
    
    v_air = r.randint(180, 280) # km/h heading North
    v_wind = r.randint(35, 75)  # km/h blowing East
    
    v_ground = round(math.hypot(v_air, v_wind), 1)
    drift_angle = round(math.degrees(math.atan2(v_wind, v_air)), 1)
    bearing_val = round(drift_angle)
    bearing_str = f"{bearing_val:03d}°"
    
    prompt = (
        f"An aeroplane heads due North with an indicated airspeed of {_fmt_sa(v_air)} km·h⁻¹. "
        f"A strong crosswind blows due East at a constant speed of {_fmt_sa(v_wind)} km·h⁻¹.\n"
        f"1. Calculate the ground speed (magnitude of resultant velocity) of the aeroplane.\n"
        f"2. Calculate the drift angle (angle of actual flight track East of North).\n"
        f"3. State the true three-figure bearing of the aircraft's track over the ground."
    )
    
    sample_answer = (
        rf"1. v_{{\text{{ground}}}} = \sqrt{{v_{{\text{{air}}}}^2 + v_{{\text{{wind}}}}^2}} = \sqrt{{({_fmt_sa(v_air)})^2 + ({_fmt_sa(v_wind)})^2}} = {_fmt_sa(v_ground)}\text{{ km·h}}^{{-1}}\\"
        rf"2. \tan\theta = \frac{{v_{{\text{{wind}}}}}}{{v_{{\text{{air}}}}}} = \frac{{{_fmt_sa(v_wind)}}}{{{_fmt_sa(v_air)}}} \implies \theta = \arctan\left(\frac{{{_fmt_sa(v_wind)}}}{{{_fmt_sa(v_air)}}}\right) = {_fmt_sa(drift_angle)}^\circ\text{{ East of North}}\\"
        f"3. True track bearing = {bearing_str}."
    )
    
    return {
        "id": f"vec_47_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "47_navigation_aircraft_crosswind_ground_speed",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"Ground speed = {_fmt_sa(v_ground)} km·h⁻¹; Bearing = {bearing_str}",
        "sample_answer": sample_answer,
        "marks": 5,
        "misconception_tags": ["subtracted_crosswind_speed", "inverted_wind_drift_angle"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_pyth_f", "desc": "Formula v_ground = sqrt(v_air^2 + v_wind^2)", "marks": 1, "editable": True},
                {"id": "mp_pyth_a", "desc": f"Ground speed = {_fmt_sa(v_ground)} km·h⁻¹", "marks": 2, "editable": True},
                {"id": "mp_trig", "desc": f"Drift angle = {_fmt_sa(drift_angle)}° East of North", "marks": 1, "editable": True},
                {"id": "mp_bearing", "desc": f"Three-figure bearing = {bearing_str}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_leading_zero", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "The aircraft's motion relative to the ground is the vector sum of airspeed and wind velocity.",
            "2_concept": "v_ground = sqrt(v_air^2 + v_wind^2). Bearing is clockwise from North towards East.",
            "3_breakdown": f"v_ground = sqrt({v_air}^2 + {v_wind}^2) = {_fmt_sa(v_ground)} km·h⁻¹. Bearing = {bearing_str}.",
        },
    }


def build_48_force_applied_at_angle_pulling_sled(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Resolve pulling force at angle on sled: effective horizontal force and normal force reduction."""
    r = _rng(seed)
    
    mass_kg = r.randint(15, 45)
    f_pull = r.randint(40, 100)
    theta = r.choice([25, 30, 35, 40, 45])
    theta_rad = math.radians(theta)
    
    w = round(mass_kg * 9.8, 1)
    fx = round(f_pull * math.cos(theta_rad), 2)
    fy = round(f_pull * math.sin(theta_rad), 2)
    fn = round(w - fy, 2)
    
    prompt = (
        f"A child pulls a wooden sled of mass {_fmt_sa(mass_kg)} kg across a horizontal snow field by a rope. "
        f"The rope exerts a tension force of {_fmt_sa(f_pull)} N inclined at an angle of {_fmt_sa(theta)}° above the horizontal. "
        f"Taking g = 9,8 m·s⁻²:\n"
        f"1. Calculate the horizontal component of the tension force (F_x).\n"
        f"2. Calculate the vertical component of the tension force (F_y).\n"
        f"3. Calculate the weight of the sled (Fg).\n"
        f"4. Calculate the normal force (F_N) exerted by the ground on the sled."
    )
    
    calc_latex = (
        rf"1. F_x = F \cos({theta}^\circ) = ({_fmt_sa(f_pull)})\cos({theta}^\circ) = {_fmt_sa(fx)}\text{{ N}}\\"
        rf"2. F_y = F \sin({theta}^\circ) = ({_fmt_sa(f_pull)})\sin({theta}^\circ) = {_fmt_sa(fy)}\text{{ N}}\\"
        rf"3. F_g = m g = ({_fmt_sa(mass_kg)})(9{{,}}8) = {_fmt_sa(w)}\text{{ N}}\\"
        rf"4. \Sigma F_y = 0 \implies F_N + F_y - F_g = 0 \implies F_N = F_g - F_y = {_fmt_sa(w)} - {_fmt_sa(fy)} = {_fmt_sa(fn)}\text{{ N}}"
    )
    
    return {
        "id": f"vec_48_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "48_force_applied_at_angle_pulling_sled",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 6,
        "prompt": prompt,
        "ideal_answer": f"F_x = {_fmt_sa(fx)} N; F_y = {_fmt_sa(fy)} N; F_N = {_fmt_sa(fn)} N",
        "sample_answer": calc_latex,
        "marks": 6,
        "misconception_tags": ["assumed_normal_force_equals_weight", "added_fy_to_weight_when_pulling_upward"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_fx", "desc": f"F_x = {_fmt_sa(fx)} N", "marks": 1, "editable": True},
                {"id": "mp_fy", "desc": f"F_y = {_fmt_sa(fy)} N", "marks": 1, "editable": True},
                {"id": "mp_fg", "desc": f"Weight F_g = {_fmt_sa(w)} N", "marks": 1, "editable": True},
                {"id": "mp_fn_eq", "desc": "Normal force equation F_N = F_g - F_y", "marks": 2, "editable": True},
                {"id": "mp_fn_a", "desc": f"Normal force F_N = {_fmt_sa(fn)} N", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Because the rope pulls UP and forward, the vertical component Fy lifts part of the weight.",
            "2_concept": "F_N + F_y = F_g, which means F_N = F_g - F_y.",
            "3_breakdown": f"Fx = {_fmt_sa(fx)} N. Fy = {_fmt_sa(fy)} N. Fg = {_fmt_sa(w)} N. Fn = {w} - {_fmt_sa(fy)} = {_fmt_sa(fn)} N.",
        },
    }


def build_49_force_applied_at_angle_pushing_lawnmower(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Resolve downward pushing force at angle on lawnmower: effective horizontal force and normal force increase."""
    r = _rng(seed)
    
    mass_kg = r.randint(18, 35)
    f_push = r.randint(50, 120)
    theta = r.choice([30, 35, 40, 45, 50]) # angle below horizontal
    theta_rad = math.radians(theta)
    
    w = round(mass_kg * 9.8, 1)
    fx = round(f_push * math.cos(theta_rad), 2)
    fy = round(f_push * math.sin(theta_rad), 2)
    fn = round(w + fy, 2)
    
    prompt = (
        f"A gardener pushes a lawnmower of mass {_fmt_sa(mass_kg)} kg with a force of {_fmt_sa(f_push)} N "
        f"directed along the handle at an angle of {_fmt_sa(theta)}° BELOW the horizontal. Taking g = 9,8 m·s⁻²:\n"
        f"1. Calculate the horizontal forward component of the pushing force (F_x).\n"
        f"2. Calculate the downward vertical component of the pushing force (F_y).\n"
        f"3. Calculate the normal force (F_N) exerted by the lawn on the mower.\n"
        f"4. Briefly explain why it is mechanically harder to push a lawnmower than to pull it across rough grass."
    )
    
    sample_answer = (
        rf"1. F_x = F \cos({theta}^\circ) = ({_fmt_sa(f_push)})\cos({theta}^\circ) = {_fmt_sa(fx)}\text{{ N}}\\"
        rf"2. F_y = F \sin({theta}^\circ) = ({_fmt_sa(f_push)})\sin({theta}^\circ) = {_fmt_sa(fy)}\text{{ N}}\\"
        rf"3. \Sigma F_y = 0 \implies F_N - F_g - F_y = 0 \implies F_N = F_g + F_y\\"
        rf"   F_N = ({_fmt_sa(mass_kg)})(9{{,}}8) + {_fmt_sa(fy)} = {_fmt_sa(w)} + {_fmt_sa(fy)} = {_fmt_sa(fn)}\text{{ N}}\\"
        f"4. Explanation: When pushing, the downward component (F_y) adds to the weight, INCREASING the normal force (F_N = F_g + F_y). "
        f"A higher normal force increases maximum frictional resistance (f = μ F_N), making it harder to push than to pull (where F_y reduces F_N)."
    )
    
    return {
        "id": f"vec_49_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "49_force_applied_at_angle_pushing_lawnmower",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 6,
        "prompt": prompt,
        "ideal_answer": f"F_x = {_fmt_sa(fx)} N; F_N = {_fmt_sa(fn)} N; pushing increases normal force and friction",
        "sample_answer": sample_answer,
        "marks": 6,
        "misconception_tags": ["subtracted_downward_push_from_weight", "confused_push_and_pull_normal_force_effects"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_fx", "desc": f"Horizontal forward force F_x = {_fmt_sa(fx)} N", "marks": 1, "editable": True},
                {"id": "mp_fy", "desc": f"Downward force F_y = {_fmt_sa(fy)} N", "marks": 1, "editable": True},
                {"id": "mp_fn_eq", "desc": "Normal force equation F_N = F_g + F_y", "marks": 2, "editable": True},
                {"id": "mp_fn_a", "desc": f"Normal force F_N = {_fmt_sa(fn)} N", "marks": 1, "editable": True},
                {"id": "mp_reason", "desc": "Explanation: increased normal force increases friction", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Pushing downward on the handle presses the mower into the lawn, increasing the contact force.",
            "2_concept": "F_N = F_g + F_y. Greater normal force means greater frictional opposition.",
            "3_breakdown": f"Fx = {_fmt_sa(fx)} N. Fy = {_fmt_sa(fy)} N. Fn = {w} + {_fmt_sa(fy)} = {_fmt_sa(fn)} N.",
        },
    }


def build_50_capstone_vector_mechanics_synthesis_autopsy(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Capstone multi-part synthesis rider & post-exam diagnostic autopsy / misconception triage."""
    r = _rng(seed)
    
    # Perpendicular forces with Pythagoras
    k = r.choice([2, 4, 6, 8])
    fx = 4 * k # East
    fy = 3 * k # North
    r_mag = 5 * k
    theta = round(math.degrees(math.atan2(fy, fx)), 1)
    
    # Scale SVG
    svg_vectors = [
        {"dx": fx, "dy": 0, "start": (0, 0), "color": "#1e3a8a", "label": f"Fx = {fx} N"},
        {"dx": 0, "dy": fy, "start": (fx, 0), "color": "#047857", "label": f"Fy = {fy} N"},
        {"dx": fx, "dy": fy, "start": (0, 0), "color": "#b91c1c", "label": f"R = {r_mag} N", "stroke_width": 3},
        {"dx": -fx, "dy": -fy, "start": (0, 0), "color": "#7c3aed", "label": f"E = {r_mag} N", "dashed": True},
    ]
    svg_markup = _vector_svg(
        svg_vectors,
        origin=(180, 160),
        scale=120.0 / r_mag,
        width=500,
        height=320,
        show_compass=True,
        seed_tag=seed,
    )
    
    prompt = (
        f"Refer to the vector diagram showing a concurrent two-force system acting on an object at origin O:\n"
        f"Force 1: F_x = {_fmt_sa(fx)} N East; Force 2: F_y = {_fmt_sa(fy)} N North.\n\n"
        f"1. Define the term 'resultant vector'.\n"
        f"2. Use the Theorem of Pythagoras and trigonometry to calculate the magnitude and direction of the resultant force R.\n"
        f"3. State the magnitude and direction of the equilibrant vector E.\n"
        f"4. Diagnostic Analysis: A learner erroneously states that 'the resultant of F_x and F_y is {fx + fy} N'. "
        f"Identify and rectify this misconception."
    )
    
    sample_answer = (
        "1. Definition: The resultant vector is the single vector that produces the same physical effect as the individual vectors acting together.\n"
        rf"2. Magnitude: R = \sqrt{{({_fmt_sa(fx)})^2 + ({_fmt_sa(fy)})^2}} = {_fmt_sa(r_mag)}\text{{ N}}\\"
        rf"   Direction: \tan\theta = \frac{{{_fmt_sa(fy)}}}{{{_fmt_sa(fx)}}} = \frac{{3}}{{4}} \implies \theta = {_fmt_sa(theta)}^\circ\text{{ North of East}}\\"
        f"3. Equilibrant: E = {_fmt_sa(r_mag)} N directed at {_fmt_sa(theta)}° South of West (opposite direction to R).\n"
        f"4. Diagnostic Rectification: The learner committed the scalar addition misconception (adding {_fmt_sa(fx)} + {_fmt_sa(fy)} = {_fmt_sa(fx + fy)} N). "
        "Because vectors possess direction and act at right angles (90°), their magnitudes cannot be added algebraically; "
        f"vector addition must account for direction via the Theorem of Pythagoras, yielding {_fmt_sa(r_mag)} N, NOT {_fmt_sa(fx + fy)} N."
    )
    
    return {
        "id": f"vec_50_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "50_capstone_vector_mechanics_synthesis_autopsy",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 8,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg_markup,
            "diagram_role": "context",
        },
        "prompt": prompt,
        "ideal_answer": f"R = {_fmt_sa(r_mag)} N at {_fmt_sa(theta)}° N of E; E = {_fmt_sa(r_mag)} N at {_fmt_sa(theta)}° S of W; scalar addition error corrected",
        "sample_answer": sample_answer,
        "marks": 8,
        "misconception_tags": ["added_vector_magnitudes_algebraically", "confused_equilibrant_with_resultant"],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_def", "desc": "Accurate curriculum definition of resultant vector", "marks": 1, "editable": True},
                {"id": "mp_pyth", "desc": f"Resultant magnitude R = {_fmt_sa(r_mag)} N", "marks": 2, "editable": True},
                {"id": "mp_dir", "desc": f"Resultant direction θ = {_fmt_sa(theta)}° North of East", "marks": 2, "editable": True},
                {"id": "mp_eq", "desc": f"Equilibrant magnitude and direction ({_fmt_sa(r_mag)} N South of West)", "marks": 1, "editable": True},
                {"id": "mp_diag", "desc": "Identified scalar addition misconception and explained vector addition at right angles", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Forces at 90° form a right triangle; you cannot simply add their numbers together.",
            "2_concept": "R = sqrt(Fx^2 + Fy^2) and tan(θ) = Fy / Fx. The equilibrant is equal and opposite to R.",
            "3_breakdown": f"R = sqrt({fx}^2 + {fy}^2) = {r_mag} N. Angle = {_fmt_sa(theta)}° N of E. E = {r_mag} N {_fmt_sa(theta)}° S of W.",
        },
    }


# ============================================================================
# EXPORT REGISTRIES FOR SUBSKILLS 26–50
# ============================================================================

BUILDERS_26_50: Dict[str, Any] = {
    "26_resolve_vector_horizontal_component": build_26_resolve_vector_horizontal_component,
    "27_resolve_vector_vertical_component": build_27_resolve_vector_vertical_component,
    "28_resolve_vector_both_components_horizontal_reference": build_28_resolve_vector_both_components_horizontal_reference,
    "29_resolve_vector_angle_to_vertical": build_29_resolve_vector_angle_to_vertical,
    "30_resolve_vector_bearing_reference": build_30_resolve_vector_bearing_reference,
    "31_reconstruct_vector_from_components": build_31_reconstruct_vector_from_components,
    "32_component_sign_conventions_in_four_quadrants": build_32_component_sign_conventions_in_four_quadrants,
    "33_multiple_vectors_algebraic_components_forces": build_33_multiple_vectors_algebraic_components_forces,
    "34_multiple_vectors_algebraic_components_displacements": build_34_multiple_vectors_algebraic_components_displacements,
    "35_three_coplanar_forces_component_sum": build_35_three_coplanar_forces_component_sum,
    "36_resultant_magnitude_and_direction_from_sum_components": build_36_resultant_magnitude_and_direction_from_sum_components,
    "37_equilibrant_vector_definition_and_relation": build_37_equilibrant_vector_definition_and_relation,
    "38_find_equilibrant_collinear_system": build_38_find_equilibrant_collinear_system,
    "39_find_equilibrant_perpendicular_forces": build_39_find_equilibrant_perpendicular_forces,
    "40_find_equilibrant_angled_force_system": build_40_find_equilibrant_angled_force_system,
    "41_equilibrium_concurrent_forces_closed_triangle": build_41_equilibrium_concurrent_forces_closed_triangle,
    "42_three_forces_equilibrium_solve_unknown_force": build_42_three_forces_equilibrium_solve_unknown_force,
    "43_suspended_object_symmetrical_cable_tensions": build_43_suspended_object_symmetrical_cable_tensions,
    "44_suspended_object_horizontal_pull_tension": build_44_suspended_object_horizontal_pull_tension,
    "45_navigation_boat_crossing_flowing_river": build_45_navigation_boat_crossing_flowing_river,
    "46_navigation_boat_river_drift_distance": build_46_navigation_boat_river_drift_distance,
    "47_navigation_aircraft_crosswind_ground_speed": build_47_navigation_aircraft_crosswind_ground_speed,
    "48_force_applied_at_angle_pulling_sled": build_48_force_applied_at_angle_pulling_sled,
    "49_force_applied_at_angle_pushing_lawnmower": build_49_force_applied_at_angle_pushing_lawnmower,
    "50_capstone_vector_mechanics_synthesis_autopsy": build_50_capstone_vector_mechanics_synthesis_autopsy,
}

SUBSKILLS_26_50: List[str] = list(BUILDERS_26_50.keys())
