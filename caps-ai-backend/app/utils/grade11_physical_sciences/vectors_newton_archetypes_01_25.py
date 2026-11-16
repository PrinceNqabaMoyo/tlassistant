"""Grade 11 Physical Sciences — Vectors in Two Dimensions: Archetypes 01–25
==========================================================================
100% Aligned with South African National Curriculum Standards (Grade 11 Term 1).
Grounded strictly in curriculum_docs_auto/PhysicalSciences_Gr11/Term 1/01. Vectors in two dimensions.md.

Covers subskills 01–25:
- 01_vector_scalar_definition_and_identification
- 02_vector_graphical_representation_scale
- 03_cartesian_plane_vector_equality_and_translation
- 04_negative_vectors_opposite_direction
- 05_collinear_vectors_addition_1d
- 06_vector_components_horizontal_cosine
- 07_vector_components_vertical_sine
- 08_vector_components_angle_with_vertical
- 09_vector_reconstruction_from_rectangular_components
- 10_vector_components_quadrant_signs
- 11_resultant_two_perpendicular_forces_pythagoras
- 12_resultant_direction_perpendicular_forces_angle
- 13_resultant_perpendicular_vectors_bearing
- 14_perpendicular_vectors_tail_to_head_sketch
- 15_resultant_of_three_orthogonal_forces
- 16_multiple_vectors_sum_of_horizontal_components
- 17_multiple_vectors_sum_of_vertical_components
- 18_multiple_vectors_resultant_magnitude
- 19_multiple_vectors_resultant_direction
- 20_multiple_forces_applied_to_single_point_engineering
- 21_equilibrant_vector_definition_and_relation_to_resultant
- 22_equilibrant_perpendicular_forces_calculation
- 23_equilibrant_multiple_coplanar_forces
- 24_closed_vector_triangle_static_equilibrium
- 25_equilibrium_suspended_mass_two_cables_tensions
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Tuple


def _fmt_sa(val: float | int, places: int = 1) -> str:
    """Format numeric values with South African decimal comma."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_vector_cartesian_svg(
    vectors: List[Tuple[float, float, str, str, bool]],  # (vx, vy, label, color, is_dashed)
    title: str = "Vector Diagram",
    seed: int = 42,
    max_coord: float = 100.0,
    show_components: bool = False,
) -> str:
    """Generate dynamic seed-varied inline SVG for 2D Cartesian vector diagrams."""
    width, height = 400, 340
    cx, cy = 200, 170
    scale = 140.0 / max(max_coord, 1.0)

    elements: List[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" data-seed="{seed}" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px;">',
        '<defs>',
        '  <marker id="arr-blue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2563eb"/></marker>',
        '  <marker id="arr-red" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#dc2626"/></marker>',
        '  <marker id="arr-green" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#16a34a"/></marker>',
        '  <marker id="arr-purple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#9333ea"/></marker>',
        '  <marker id="arr-amber" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#d97706"/></marker>',
        '</defs>',
    ]

    # Grid
    for step in [-100, -50, 50, 100]:
        elements.append(f'<line x1="{cx + step}" y1="20" x2="{cx + step}" y2="320" stroke="#f1f5f9" stroke-width="1"/>')
        elements.append(f'<line x1="20" y1="{cy + step}" x2="380" y2="{cy + step}" stroke="#f1f5f9" stroke-width="1"/>')

    # Axes
    elements.append(f'<line x1="20" y1="{cy}" x2="380" y2="{cy}" stroke="#475569" stroke-width="2"/>')
    elements.append(f'<line x1="{cx}" y1="320" x2="{cx}" y2="20" stroke="#475569" stroke-width="2"/>')
    elements.append(f'<text x="375" y="{cy - 8}" font-size="11" font-family="sans-serif" font-weight="bold" fill="#334155" text-anchor="end">+x (East)</text>')
    elements.append(f'<text x="{cx + 8}" y="32" font-size="11" font-family="sans-serif" font-weight="bold" fill="#334155">+y (North)</text>')
    elements.append(f'<text x="{cx - 12}" y="{cy + 16}" font-size="11" font-family="sans-serif" fill="#64748b">O</text>')

    color_markers = {
        "#2563eb": "arr-blue",
        "#dc2626": "arr-red",
        "#16a34a": "arr-green",
        "#9333ea": "arr-purple",
        "#d97706": "arr-amber",
    }

    for vx, vy, label, col, is_dashed in vectors:
        x_end = cx + vx * scale
        y_end = cy - vy * scale
        mk = color_markers.get(col, "arr-blue")
        dash_attr = ' stroke-dasharray="4,3"' if is_dashed else ""

        if show_components and not is_dashed:
            # Component projections
            elements.append(f'<line x1="{x_end:.1f}" y1="{cy}" x2="{x_end:.1f}" y2="{y_end:.1f}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>')
            elements.append(f'<line x1="{cx}" y1="{y_end:.1f}" x2="{x_end:.1f}" y2="{y_end:.1f}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>')

        elements.append(f'<line x1="{cx}" y1="{cy}" x2="{x_end:.1f}" y2="{y_end:.1f}" stroke="{col}" stroke-width="2.5"{dash_attr} marker-end="url(#{mk})"/>')
        elements.append(f'<circle cx="{x_end:.1f}" cy="{y_end:.1f}" r="3" fill="{col}"/>')

        # Offset text label
        off_x = 10 if vx >= 0 else -10
        off_y = -8 if vy >= 0 else 14
        anchor = "start" if vx >= 0 else "end"
        elements.append(f'<text x="{x_end + off_x:.1f}" y="{y_end + off_y:.1f}" font-size="11" font-family="sans-serif" font-weight="600" fill="{col}" text-anchor="{anchor}">{label}</text>')

    elements.append('</svg>')
    return "".join(elements)


# --------------------------------------------------------------------------- #
# Subskill 01: Vector and Scalar Definition & Identification
# --------------------------------------------------------------------------- #
def build_01_vector_scalar_definition_and_identification(rng: random.Random) -> Dict[str, Any]:
    quantities = [
        ("Force", "vector", "has both magnitude and direction (e.g. 50 N East)"),
        ("Mass", "scalar", "has magnitude only (e.g. 15 kg)"),
        ("Velocity", "vector", "has both magnitude and direction (e.g. 20 m/s North)"),
        ("Speed", "scalar", "has magnitude only (e.g. 20 m/s)"),
        ("Displacement", "vector", "has both magnitude and direction (e.g. 100 m [045°])"),
        ("Distance", "scalar", "has magnitude only (e.g. 100 m)"),
        ("Weight", "vector", "is gravitational force acting downwards"),
        ("Acceleration", "vector", "rate of change of velocity with direction"),
        ("Work", "scalar", "energy transfer with magnitude only (Joules)"),
        ("Temperature", "scalar", "state variable with magnitude only"),
    ]
    sampled = rng.sample(quantities, 4)
    target_q, target_type, target_reason = sampled[0]

    f_mag = rng.choice([20, 30, 40, 50])
    theta = rng.choice([30, 45, 60])

    prompt = (
        f"A laboratory experiment involves the physical quantities: "
        f"{', '.join([q[0] for q in sampled])}.\n\n"
        f"A representative force vector $\\vec{{F}} = {f_mag}\\,\\text{{N}}$ at an angle of {theta}° "
        f"above the horizontal is illustrated on the Cartesian plane shown.\n\n"
        f"1. Define the term **vector quantity**.\n"
        f"2. Classify **{target_q}** as either a scalar or a vector quantity and give a reason for your answer."
    )

    ans_latex = (
        rf"\text{{1. A physical quantity with both magnitude and direction; 2. {target_type.capitalize()}: {target_reason}}}"
    )
    worked_solution = (
        f"1. A vector quantity is defined as a physical quantity that has both magnitude and direction.\n"
        f"2. **{target_q}** is a **{target_type}** because it {target_reason}."
    )

    rad = math.radians(theta)
    vectors = [(f_mag * math.cos(rad), f_mag * math.sin(rad), f"F={f_mag}N({theta}deg)", "#2563eb", False)]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(f_mag) * 1.3, seed=rng.randint(1000, 999999))

    return {
        "subskill": "01_vector_scalar_definition_and_identification",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_vector_scalar",
        "difficulty": "easy",
        "marks": 4,
        "misconception_tags": ["confused_scalar_and_vector", "omitted_direction_in_vector_definition"],
        "hints": {
            "tier_1": "Recall: Scalars have magnitude only; vectors have both magnitude and direction.",
            "tier_2": f"Consider whether {target_q} requires a direction to be fully specified.",
            "tier_3": f"{target_q} is a {target_type} because it {target_reason}.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: Physical quantity having both magnitude and direction", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Correct classification as {target_type}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Valid scientific reason: {target_reason}", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 02: Vector Graphical Representation & Scale Drawing
# --------------------------------------------------------------------------- #
def build_02_vector_graphical_representation_scale(rng: random.Random) -> Dict[str, Any]:
    f_real = rng.choice([40, 60, 80, 100, 120, 150])
    scale_factor = rng.choice([10, 20])  # 1 cm : scale_factor N
    arrow_len_cm = round(f_real / scale_factor, 1)
    bearing = rng.choice([30, 45, 60, 120, 135, 150])

    prompt = (
        f"A surveyor represents a pulling force of $\\vec{{F}} = {f_real}\\,\\text{{N}}$ "
        f"acting on a bearing of {bearing:03d}° using a scale diagram.\n\n"
        f"The vector arrow is plotted on the Cartesian plane shown.\n\n"
        f"1. If a scale of $1\\,\\text{{cm}} : {scale_factor}\\,\\text{{N}}$ is chosen, "
        f"calculate the length of the arrow (in cm) needed to draw this force vector.\n"
        f"2. Explain what the arrow length and the arrowhead represent physically."
    )

    ans_latex = (
        rf"\text{{Length}} = {_fmt_sa(arrow_len_cm)}\,\text{{cm}}; \quad "
        rf"\text{{Length represents magnitude; Arrowhead represents direction}}"
    )
    worked_solution = (
        f"1. Arrow length calculation:\n"
        f"   $\\text{{Length}} = \\frac{{{f_real}\\,\\text{{N}}}}{{{scale_factor}\\,\\text{{N/cm}}}} = {_fmt_sa(arrow_len_cm)}\\,\\text{{cm}}$.\n"
        f"2. The length of the arrow represents the **magnitude** of the vector (scaled), "
        f"and the arrowhead indicates the **direction** ({bearing:03d}° bearing)."
    )

    # Convert bearing (from North / +y clockwise) to Cartesian angle
    cart_deg = (90 - bearing) % 360
    rad = math.radians(cart_deg)
    vectors = [(f_real * math.cos(rad), f_real * math.sin(rad), f"F={f_real}N[{bearing:03d}deg]", "#2563eb", False)]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(f_real) * 1.3, seed=rng.randint(1000, 999999))

    return {
        "subskill": "02_vector_graphical_representation_scale",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_scale_drawing",
        "difficulty": "easy",
        "marks": 4,
        "misconception_tags": ["multiplied_by_scale_instead_of_dividing", "confused_bearing_with_cartesian_angle"],
        "hints": {
            "tier_1": "Divide real force by the scale factor to get drawing length in cm.",
            "tier_2": f"Length = {f_real} N / {scale_factor} N/cm = {_fmt_sa(arrow_len_cm)} cm.",
            "tier_3": f"Arrow length: {_fmt_sa(arrow_len_cm)} cm. Length = magnitude, Arrowhead = direction.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Scale division {f_real} / {scale_factor}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Arrow length = {_fmt_sa(arrow_len_cm)} cm", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Length represents magnitude", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Arrowhead indicates direction", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 03: Cartesian Plane Vector Equality and Translation
# --------------------------------------------------------------------------- #
def build_03_cartesian_plane_vector_equality_and_translation(rng: random.Random) -> Dict[str, Any]:
    f_val = rng.choice([30, 40, 50, 60, 80])
    dir_name = rng.choice(["positive x-direction", "positive y-direction", "negative x-direction"])

    if "positive x" in dir_name:
        v1 = (f_val, 0, f"F1={f_val}N", "#2563eb", False)
        v2 = (f_val, 30, f"F2={f_val}N", "#dc2626", False)
    elif "positive y" in dir_name:
        v1 = (0, f_val, f"F1={f_val}N", "#2563eb", False)
        v2 = (30, f_val, f"F2={f_val}N", "#dc2626", False)
    else:
        v1 = (-f_val, 0, f"F1={f_val}N", "#2563eb", False)
        v2 = (-f_val, -30, f"F2={f_val}N", "#dc2626", False)

    prompt = (
        f"Two force vectors $\\vec{{F}}_1$ and $\\vec{{F}}_2$ are plotted on the Cartesian coordinate plane shown. "
        f"Both vectors have a magnitude of {f_val}\\,N and act in the {dir_name}, but start at different coordinates.\n\n"
        f"1. Explain whether $\\vec{{F}}_1$ and $\\vec{{F}}_2$ are equal vectors.\n"
        f"2. State the principle of **vector translation invariance** (equality of vectors)."
    )

    ans_latex = (
        rf"\text{{Yes, equal vectors. Vectors are equal if they have identical magnitude and direction, regardless of starting point.}}"
    )
    worked_solution = (
        f"1. Yes, $\\vec{{F}}_1 = \\vec{{F}}_2$. Both vectors have the same magnitude ({f_val}\\,N) "
        f"and act in the same direction ({dir_name}).\n"
        f"2. Equality of vectors: Two vectors are equal if they have the same magnitude and direction, "
        f"regardless of their starting positions on the Cartesian plane."
    )

    svg = _make_vector_cartesian_svg([v1, v2], max_coord=float(f_val) * 1.4, seed=rng.randint(1000, 999999))

    return {
        "subskill": "03_cartesian_plane_vector_equality_and_translation",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_vector_equality",
        "difficulty": "easy",
        "marks": 3,
        "misconception_tags": ["assumed_different_origins_make_vectors_unequal", "confused_position_with_vector_value"],
        "hints": {
            "tier_1": "Does the physical effect of a free vector depend on where its tail is placed?",
            "tier_2": "Vectors are defined solely by magnitude and direction. If both match, the vectors are equal.",
            "tier_3": "Yes, they are equal vectors.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Affirmation that vectors are equal", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Same magnitude ({f_val} N) and direction ({dir_name})", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Statement that initial position does not affect vector equality", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 04: Negative Vectors (Opposite Direction)
# --------------------------------------------------------------------------- #
def build_04_negative_vectors_opposite_direction(rng: random.Random) -> Dict[str, Any]:
    f_val = rng.choice([25, 35, 45, 55, 65, 75])
    theta = rng.choice([30, 45, 60])

    prompt = (
        f"A force vector $\\vec{{A}}$ has a magnitude of {f_val}\\,N and acts at an angle of {theta}° "
        f"East of North. Vector $\\vec{{A}}$ and its negative vector $-\\vec{{A}}$ are plotted on the Cartesian plane shown.\n\n"
        f"1. Define what is meant by the **negative vector** of a given vector.\n"
        f"2. Write down the magnitude and exact directional specification of $-\\vec{{A}}$."
    )

    opp_angle = (theta + 180) % 360
    ans_latex = (
        rf"|-\vec{{A}}| = {f_val}\,\text{{N}}, \quad \text{{Direction: {theta}^\circ\text{{ West of South (or bearing }}{opp_angle:03d}^\circ)}}"
    )
    worked_solution = (
        f"1. The negative of a vector is a vector that has the **same magnitude** but acts in the **exact opposite direction** (180° reversed).\n"
        f"2. For $-\\vec{{A}}$:\n"
        f"   - Magnitude: $|-\\vec{{A}}| = {f_val}\\,\\text{{N}}$ (magnitude is always positive).\n"
        f"   - Direction: {theta}° West of South (or bearing {opp_angle:03d}°)."
    )

    rad = math.radians(90 - theta)
    rad_opp = math.radians(90 - opp_angle)
    v1 = (f_val * math.cos(rad), f_val * math.sin(rad), f"A={f_val}N", "#2563eb", False)
    v2 = (f_val * math.cos(rad_opp), f_val * math.sin(rad_opp), f"-A={f_val}N", "#dc2626", False)
    svg = _make_vector_cartesian_svg([v1, v2], max_coord=float(f_val) * 1.35, seed=rng.randint(1000, 999999))

    return {
        "subskill": "04_negative_vectors_opposite_direction",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_negative_vector",
        "difficulty": "easy",
        "marks": 4,
        "misconception_tags": ["assigned_negative_sign_to_vector_magnitude", "incorrect_opposite_direction_reversal"],
        "hints": {
            "tier_1": "Magnitude of a negative vector is identical and always positive; only direction reverses by 180°.",
            "tier_2": f"Opposite of {theta}° East of North is {theta}° West of South.",
            "tier_3": f"Magnitude: {f_val} N. Direction: {theta}° West of South.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: Same magnitude, opposite direction", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Magnitude = {f_val} N (positive)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Direction: {theta} deg West of South", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 05: Collinear Vectors Addition (1D)
# --------------------------------------------------------------------------- #
def build_05_collinear_vectors_addition_1d(rng: random.Random) -> Dict[str, Any]:
    f1 = rng.choice([20, 30, 40, 50, 60])
    f2 = rng.choice([15, 25, 35, 45])
    f3 = rng.choice([10, 20, 30])

    # f1 and f2 East (+), f3 West (-)
    r_val = f1 + f2 - f3
    r_dir = "East (positive x-direction)" if r_val >= 0 else "West (negative x-direction)"

    prompt = (
        f"Three collinear horizontal forces act on an anchor point: "
        f"$\\vec{{F}}_1 = {f1}\\,\\text{{N}}$ East, "
        f"$\\vec{{F}}_2 = {f2}\\,\\text{{N}}$ East, and "
        f"$\\vec{{F}}_3 = {f3}\\,\\text{{N}}$ West.\n\n"
        f"The forces and the resultant vector are plotted on the Cartesian plane shown.\n\n"
        f"1. Choose a sign convention and calculate the net resultant force $\\vec{{R}}$.\n"
        f"2. State both the magnitude and direction of the resultant vector."
    )

    ans_latex = rf"\vec{{R}} = {abs(r_val)}\,\text{{N}}\text{{ {r_dir}}}"
    worked_solution = (
        f"1. Let East be the positive direction (+):\n"
        f"   $R_x = F_1 + F_2 - F_3 = ({f1}) + ({f2}) - ({f3}) = {r_val}\\,\\text{{N}}$.\n"
        f"2. Magnitude: $|\\vec{{R}}| = {abs(r_val)}\\,\\text{{N}}$.\n"
        f"   Direction: {r_dir}."
    )

    vectors = [
        (float(f1 + f2), 0.0, f"F1+F2={f1+f2}N", "#2563eb", False),
        (float(-f3), 15.0, f"F3={f3}N(W)", "#dc2626", False),
        (float(r_val), -15.0, f"R={abs(r_val)}N", "#16a34a", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(f1 + f2) * 1.3, seed=rng.randint(1000, 999999))

    return {
        "subskill": "05_collinear_vectors_addition_1d",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_collinear_addition",
        "difficulty": "easy",
        "marks": 4,
        "misconception_tags": ["added_all_magnitudes_ignoring_direction", "omitted_direction_in_resultant"],
        "hints": {
            "tier_1": "Choose East as positive (+) and West as negative (-).",
            "tier_2": f"Sum: +{f1} + {f2} - {f3} = {r_val} N.",
            "tier_3": f"Resultant: {abs(r_val)} N {r_dir}.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Sign convention stated (+ for East)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Algebraic addition: {f1} + {f2} - {f3}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Magnitude = {abs(r_val)} N", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Direction = {r_dir}", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 06: Vector Components Horizontal (Cosine)
# --------------------------------------------------------------------------- #
def build_06_vector_components_horizontal_cosine(rng: random.Random) -> Dict[str, Any]:
    f_mag = rng.choice([50, 60, 80, 100, 120, 150, 200])
    theta = rng.choice([25, 30, 35, 40, 45, 50, 60])

    rad = math.radians(theta)
    fx = round(f_mag * math.cos(rad), 2)

    prompt = (
        f"A tension force $\\vec{{F}} = {f_mag}\\,\\text{{N}}$ is applied to pull a heavy crate at an angle "
        f"of {theta}° above the horizontal ground.\n\n"
        f"The force vector and its horizontal component are shown on the Cartesian plane.\n\n"
        f"1. State the formula used to calculate the horizontal component ($F_x$).\n"
        f"2. Calculate the magnitude of $F_x$ in newtons (to 2 decimal places)."
    )

    ans_latex = rf"F_x = F\cos\theta = {f_mag}\cos({theta}^\circ) = {_fmt_sa(fx, 2)}\,\text{{N}}"
    worked_solution = (
        f"1. Formula: $F_x = F\\cos\\theta$.\n"
        f"2. Calculation:\n"
        f"   $F_x = ({f_mag})\\cos({theta}^\\circ) = {_fmt_sa(fx, 2)}\\,\\text{{N}}$ (directed horizontally)."
    )

    vectors = [
        (f_mag * math.cos(rad), f_mag * math.sin(rad), f"F={f_mag}N({theta}deg)", "#2563eb", False),
        (fx, 0.0, f"Fx={_fmt_sa(fx)}N", "#16a34a", True),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(f_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "06_vector_components_horizontal_cosine",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_vector_resolution",
        "difficulty": "easy",
        "marks": 3,
        "misconception_tags": ["used_sine_instead_of_cosine_for_horizontal_component", "calculator_in_radian_mode"],
        "hints": {
            "tier_1": "The horizontal side is adjacent to angle $\\theta$, so use $\\cos\\theta$.",
            "tier_2": f"Formula: $F_x = {f_mag} \\times \\cos({theta}^\\circ)$.",
            "tier_3": f"Final value: $F_x = {_fmt_sa(fx, 2)}\\,\\text{{N}}$.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Formula Fx = F * cos(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substitution: {f_mag} * cos({theta} deg)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct value: {_fmt_sa(fx, 2)} N", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 07: Vector Components Vertical (Sine)
# --------------------------------------------------------------------------- #
def build_07_vector_components_vertical_sine(rng: random.Random) -> Dict[str, Any]:
    f_mag = rng.choice([50, 60, 80, 100, 120, 150, 200])
    theta = rng.choice([25, 30, 35, 40, 45, 50, 60])

    rad = math.radians(theta)
    fy = round(f_mag * math.sin(rad), 2)

    prompt = (
        f"A force $\\vec{{F}} = {f_mag}\\,\\text{{N}}$ acts on an eye-bolt at an angle of {theta}° "
        f"above the horizontal.\n\n"
        f"The force vector and its vertical component are depicted on the Cartesian plane shown.\n\n"
        f"1. State the formula used to calculate the vertical component ($F_y$).\n"
        f"2. Calculate the magnitude of $F_y$ in newtons (to 2 decimal places)."
    )

    ans_latex = rf"F_y = F\sin\theta = {f_mag}\sin({theta}^\circ) = {_fmt_sa(fy, 2)}\,\text{{N}}"
    worked_solution = (
        f"1. Formula: $F_y = F\\sin\\theta$.\n"
        f"2. Calculation:\n"
        f"   $F_y = ({f_mag})\\sin({theta}^\\circ) = {_fmt_sa(fy, 2)}\\,\\text{{N}}$ (directed upwards)."
    )

    vectors = [
        (f_mag * math.cos(rad), f_mag * math.sin(rad), f"F={f_mag}N({theta}deg)", "#2563eb", False),
        (0.0, fy, f"Fy={_fmt_sa(fy)}N", "#dc2626", True),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(f_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "07_vector_components_vertical_sine",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_vector_resolution",
        "difficulty": "easy",
        "marks": 3,
        "misconception_tags": ["used_cosine_instead_of_sine_for_vertical_component", "calculator_in_radian_mode"],
        "hints": {
            "tier_1": "The vertical side is opposite to angle $\\theta$, so use $\\sin\\theta$.",
            "tier_2": f"Formula: $F_y = {f_mag} \\times \\sin({theta}^\\circ)$.",
            "tier_3": f"Final value: $F_y = {_fmt_sa(fy, 2)}\\,\\text{{N}}$.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Formula Fy = F * sin(theta)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substitution: {f_mag} * sin({theta} deg)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct value: {_fmt_sa(fy, 2)} N", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 08: Vector Components with Angle to Vertical
# --------------------------------------------------------------------------- #
def build_08_vector_components_angle_with_vertical(rng: random.Random) -> Dict[str, Any]:
    f_mag = rng.choice([60, 80, 100, 120, 160])
    alpha = rng.choice([20, 25, 30, 35, 40])  # angle to VERTICAL

    rad = math.radians(alpha)
    # When angle is to vertical: Fy = F*cos(alpha), Fx = F*sin(alpha)
    fy = round(f_mag * math.cos(rad), 2)
    fx = round(f_mag * math.sin(rad), 2)

    prompt = (
        f"A support cable exerts a tension force $\\vec{{T}} = {f_mag}\\,\\text{{N}}$ at an angle of {alpha}° "
        f"to the **vertical** ceiling.\n\n"
        f"The force vector and component triangle are plotted on the Cartesian plane shown.\n\n"
        f"1. Calculate the vertical component ($T_y$) in newtons.\n"
        f"2. Calculate the horizontal component ($T_x$) in newtons."
    )

    ans_latex = (
        rf"T_y = {f_mag}\cos({alpha}^\circ) = {_fmt_sa(fy, 2)}\,\text{{N}}, \quad "
        rf"T_x = {f_mag}\sin({alpha}^\circ) = {_fmt_sa(fx, 2)}\,\text{{N}}"
    )
    worked_solution = (
        f"1. Since the angle ${alpha}^\\circ$ is measured relative to the **vertical**:\n"
        f"   - Vertical component is adjacent: $T_y = T\\cos({alpha}^\\circ) = ({f_mag})\\cos({alpha}^\\circ) = {_fmt_sa(fy, 2)}\\,\\text{{N}}$.\n"
        f"2. Horizontal component is opposite:\n"
        f"   - $T_x = T\\sin({alpha}^\\circ) = ({f_mag})\\sin({alpha}^\\circ) = {_fmt_sa(fx, 2)}\\,\\text{{N}}$."
    )

    vectors = [
        (fx, fy, f"T={f_mag}N", "#2563eb", False),
        (fx, 0.0, f"Tx={_fmt_sa(fx)}N", "#16a34a", True),
        (0.0, fy, f"Ty={_fmt_sa(fy)}N", "#dc2626", True),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(f_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "08_vector_components_angle_with_vertical",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "elementary_components_vertical_angle",
        "difficulty": "medium",
        "marks": 4,
        "misconception_tags": ["swapped_sin_and_cos_for_angle_to_vertical", "assumed_horizontal_is_always_cosine"],
        "hints": {
            "tier_1": "Careful: The angle is with the vertical! The adjacent side is the vertical component ($T_y = T\\cos\\alpha$).",
            "tier_2": f"Vertical: $T_y = {f_mag} \\times \\cos({alpha}^\\circ)$. Horizontal: $T_x = {f_mag} \\times \\sin({alpha}^\\circ)$.",
            "tier_3": f"$T_y = {_fmt_sa(fy, 2)}\\,\\text{{N}}$, $T_x = {_fmt_sa(fx, 2)}\\,\\text{{N}}$.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Vertical component formula Ty = T * cos({alpha})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Vertical component value {_fmt_sa(fy, 2)} N", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Horizontal component formula Tx = T * sin({alpha})", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Horizontal component value {_fmt_sa(fx, 2)} N", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 09: Vector Reconstruction from Rectangular Components
# --------------------------------------------------------------------------- #
def build_09_vector_reconstruction_from_rectangular_components(rng: random.Random) -> Dict[str, Any]:
    triples = [(30, 40, 50), (60, 80, 100), (50, 120, 130), (40, 30, 50), (80, 60, 100)]
    fx, fy, f_mag = rng.choice(triples)

    theta = round(math.degrees(math.atan(fy / fx)), 1)

    prompt = (
        f"A force has horizontal component $F_x = {fx}\\,\\text{{N}}$ (East) and "
        f"vertical component $F_y = {fy}\\,\\text{{N}}$ (North).\n\n"
        f"The components and resultant vector are shown on the Cartesian plane.\n\n"
        f"1. Use the Theorem of Pythagoras to calculate the magnitude of the force vector $F$.\n"
        f"2. Calculate the direction angle $\\theta$ (above the horizontal positive x-axis) to 1 decimal place."
    )

    ans_latex = rf"F = {f_mag}\,\text{{N}}, \quad \theta = {_fmt_sa(theta)}^\circ"
    worked_solution = (
        f"1. Magnitude via Pythagoras:\n"
        f"   $F = \\sqrt{{F_x^2 + F_y^2}} = \\sqrt{{{fx}^2 + {fy}^2}} = \\sqrt{{{f_mag**2}}} = {f_mag}\\,\\text{{N}}$.\n"
        f"2. Direction angle:\n"
        f"   $\\tan\\theta = \\frac{{F_y}}{{F_x}} = \\frac{{{fy}}}{{{fx}}} \\implies \\theta = \\tan^{{-1}}\\left(\\frac{{{fy}}}{{{fx}}}\\right) = {_fmt_sa(theta)}^\\circ$."
    )

    vectors = [
        (float(fx), 0.0, f"Fx={fx}N", "#16a34a", True),
        (float(fx), float(fy), f"F={f_mag}N", "#2563eb", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(f_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "09_vector_reconstruction_from_rectangular_components",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "mode": "elementary_vector_reconstruction",
        "difficulty": "medium",
        "marks": 4,
        "misconception_tags": ["inverted_tangent_ratio_fx_over_fy", "added_components_directly_instead_of_pythagoras"],
        "hints": {
            "tier_1": "Magnitude: $F = \\sqrt{F_x^2 + F_y^2}$. Direction: $\\theta = \\arctan(F_y / F_x)$.",
            "tier_2": f"Pythagoras gives $\\sqrt{{{fx}^2 + {fy}^2}} = {f_mag}\\,\\text{{N}}$. Angle $\\theta = \\arctan({fy}/{fx})$.",
            "tier_3": f"Magnitude: {f_mag} N. Angle: {_fmt_sa(theta)}°.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Pythagoras formula substitution", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Magnitude = {f_mag} N", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Tangent formula tan(theta) = Fy / Fx", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Angle = {_fmt_sa(theta)} deg", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 10: Vector Components Quadrant Signs
# --------------------------------------------------------------------------- #
def build_10_vector_components_quadrant_signs(rng: random.Random) -> Dict[str, Any]:
    quad_info = [
        (2, -1, 1, 140, "Quadrant 2", "Fx is negative (West), Fy is positive (North)"),
        (3, -1, -1, 220, "Quadrant 3", "Fx is negative (West), Fy is negative (South)"),
        (4, 1, -1, 310, "Quadrant 4", "Fx is positive (East), Fy is negative (South)"),
    ]
    quad, sx, sy, angle_deg, quad_name, rule_desc = rng.choice(quad_info)
    f_mag = rng.choice([50, 75, 100])

    prompt = (
        f"A force vector $\\vec{{F}} = {f_mag}\\,\\text{{N}}$ acts at an angle of {angle_deg}° "
        f"measured counterclockwise from the positive x-axis.\n\n"
        f"The vector is plotted on the Cartesian plane shown.\n\n"
        f"1. Identify the Cartesian quadrant in which this vector lies.\n"
        f"2. State the correct algebraic signs (positive or negative) of the horizontal component ($F_x$) "
        f"and the vertical component ($F_y$)."
    )

    ans_latex = (
        rf"\text{{{quad_name}}}: \quad F_x \text{{ is {'positive' if sx > 0 else 'negative'}}}, \quad "
        rf"F_y \text{{ is {'positive' if sy > 0 else 'negative'}}}"
    )
    worked_solution = (
        f"1. An angle of {angle_deg}° lies in **{quad_name}** (between {quad * 90 - 90}° and {quad * 90}°).\n"
        f"2. In {quad_name}:\n"
        f"   - $F_x$ has a **{'positive' if sx > 0 else 'negative'}** sign ({'East' if sx > 0 else 'West'}).\n"
        f"   - $F_y$ has a **{'positive' if sy > 0 else 'negative'}** sign ({'North' if sy > 0 else 'South'})."
    )

    rad = math.radians(angle_deg)
    vectors = [(f_mag * math.cos(rad), f_mag * math.sin(rad), f"F={f_mag}N({angle_deg}deg)", "#2563eb", False)]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(f_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "10_vector_components_quadrant_signs",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_quadrant_signs",
        "difficulty": "easy",
        "marks": 3,
        "misconception_tags": ["incorrect_quadrant_sign_assignment", "assumed_all_magnitudes_are_positive_in_algebra"],
        "hints": {
            "tier_1": f"Check which quadrant {angle_deg}° belongs to.",
            "tier_2": f"Quadrant 2: (-x, +y); Quadrant 3: (-x, -y); Quadrant 4: (+x, -y).",
            "tier_3": f"{quad_name}: Fx is {'positive' if sx > 0 else 'negative'}, Fy is {'positive' if sy > 0 else 'negative'}.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct quadrant: {quad_name}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Fx sign: {'positive' if sx > 0 else 'negative'}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Fy sign: {'positive' if sy > 0 else 'negative'}", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 11: Resultant of Two Perpendicular Forces (Pythagoras)
# --------------------------------------------------------------------------- #
def build_11_resultant_two_perpendicular_forces_pythagoras(rng: random.Random) -> Dict[str, Any]:
    triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20)]
    mult = rng.choice([10, 20])
    a_base, b_base, c_base = rng.choice(triples)
    f1 = a_base * mult
    f2 = b_base * mult
    r_mag = c_base * mult

    prompt = (
        f"Two tugboats pull a disabled ship. Tugboat A exerts a force of $F_1 = {f1}\\,\\text{{N}}$ due East, "
        f"and Tugboat B exerts a force of $F_2 = {f2}\\,\\text{{N}}$ due North.\n\n"
        f"The two perpendicular forces and their resultant vector $\\vec{{R}}$ are plotted on the Cartesian plane shown.\n\n"
        f"Calculate the magnitude of the resultant force acting on the ship in newtons."
    )

    ans_latex = rf"R = \sqrt{{{f1}^2 + {f2}^2}} = {r_mag}\,\text{{N}}"
    worked_solution = (
        f"1. State the Theorem of Pythagoras for perpendicular vectors:\n"
        f"   $R = \\sqrt{{F_1^2 + F_2^2}}$.\n"
        f"2. Substitute values:\n"
        f"   $R = \\sqrt{{{f1}^2 + {f2}^2}} = \\sqrt{{{f1**2} + {f2**2}}} = \\sqrt{{{r_mag**2}}} = {r_mag}\\,\\text{{N}}$."
    )

    vectors = [
        (float(f1), 0.0, f"F1={f1}N(E)", "#2563eb", False),
        (0.0, float(f2), f"F2={f2}N(N)", "#dc2626", False),
        (float(f1), float(f2), f"R={r_mag}N", "#16a34a", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(r_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "11_resultant_two_perpendicular_forces_pythagoras",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_resultant_pythagoras",
        "difficulty": "easy",
        "marks": 3,
        "misconception_tags": ["added_perpendicular_magnitudes_linearly", "forgot_square_root_in_pythagoras"],
        "hints": {
            "tier_1": "Perpendicular vectors form a right-angled triangle. Use Pythagoras: $R = \\sqrt{F_1^2 + F_2^2}$.",
            "tier_2": f"Calculation: $R = \\sqrt{{{f1}^2 + {f2}^2}} = \\sqrt{{{r_mag**2}}}$.",
            "tier_3": f"Resultant magnitude: {r_mag} N.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Pythagoras formula R = sqrt(F1^2 + F2^2)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substitution: sqrt({f1}^2 + {f2}^2)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Magnitude R = {r_mag} N", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 12: Resultant Direction of Perpendicular Forces (Angle)
# --------------------------------------------------------------------------- #
def build_12_resultant_direction_perpendicular_forces_angle(rng: random.Random) -> Dict[str, Any]:
    fx = rng.choice([30, 40, 50, 60, 80])
    fy = rng.choice([30, 40, 50, 60, 80])

    theta = round(math.degrees(math.atan(fy / fx)), 1)
    r_mag = round(math.hypot(fx, fy), 1)

    prompt = (
        f"Two perpendicular forces act on an object: $F_x = {fx}\\,\\text{{N}}$ (East) and "
        f"$F_y = {fy}\\,\\text{{N}}$ (North).\n\n"
        f"The vector addition is shown on the Cartesian plane.\n\n"
        f"Calculate the direction angle $\\theta$ of the resultant vector measured North of East (to 1 decimal place)."
    )

    ans_latex = rf"\theta = \tan^{{-1}}\left(\frac{{{fy}}}{{{fx}}}\right) = {_fmt_sa(theta)}^\circ\text{{ North of East}}"
    worked_solution = (
        f"1. Apply tangent ratio: $\\tan\\theta = \\frac{{F_y}}{{F_x}} = \\frac{{{fy}}}{{{fx}}}$.\n"
        f"2. Solve for angle:\n"
        f"   $\\theta = \\tan^{{-1}}\\left(\\frac{{{fy}}}{{{fx}}}\\right) = {_fmt_sa(theta)}^\\circ$ North of East."
    )

    vectors = [
        (float(fx), 0.0, f"Fx={fx}N", "#2563eb", False),
        (0.0, float(fy), f"Fy={fy}N", "#dc2626", False),
        (float(fx), float(fy), f"R={_fmt_sa(r_mag)}N", "#16a34a", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(r_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "12_resultant_direction_perpendicular_forces_angle",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_resultant_direction",
        "difficulty": "medium",
        "marks": 3,
        "misconception_tags": ["inverted_tangent_ratio_adjacent_over_opposite", "omitted_directional_reference_north_of_east"],
        "hints": {
            "tier_1": "Use $\\tan\\theta = \\text{opposite} / \\text{adjacent} = F_y / F_x$.",
            "tier_2": f"$\\theta = \\arctan({fy} / {fx})$.",
            "tier_3": f"Direction: {_fmt_sa(theta)}° North of East.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Tangent formula tan(theta) = Fy / Fx", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substitution: arctan({fy} / {fx})", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle = {_fmt_sa(theta)} deg North of East", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 13: Resultant of Perpendicular Vectors as a Bearing
# --------------------------------------------------------------------------- #
def build_13_resultant_perpendicular_vectors_bearing(rng: random.Random) -> Dict[str, Any]:
    triples = [(30, 40, 50), (40, 30, 50), (60, 80, 100), (80, 60, 100)]
    fx, fy, r_mag = rng.choice(triples)

    # In navigation, bearing is clockwise from North: bearing = arctan(East / North) = arctan(fx / fy)
    bearing_deg = round(math.degrees(math.atan(fx / fy)))

    prompt = (
        f"A nautical navigation vessel experiences a horizontal tidal force of $F_{{\\text{{East}}}} = {fx}\\,\\text{{N}}$ "
        f"and an engine thrust of $F_{{\\text{{North}}}} = {fy}\\,\\text{{N}}$.\n\n"
        f"The perpendicular forces and the resultant course are shown on the Cartesian plane.\n\n"
        f"1. Calculate the magnitude of the resultant force in newtons.\n"
        f"2. Determine the direction of the resultant expressed as a standard **three-figure bearing** (measured clockwise from North)."
    )

    ans_latex = rf"R = {r_mag}\,\text{{N}}, \quad \text{{Bearing}} = {bearing_deg:03d}^\circ"
    worked_solution = (
        f"1. Resultant magnitude: $R = \\sqrt{{{fx}^2 + {fy}^2}} = {r_mag}\\,\\text{{N}}$.\n"
        f"2. Three-figure bearing (clockwise from North):\n"
        f"   $\\tan\\beta = \\frac{{F_{{\\text{{East}}}}}}{{F_{{\\text{{North}}}}}} = \\frac{{{fx}}}{{{fy}}} \\implies \\beta = \\tan^{{-1}}\\left(\\frac{{{fx}}}{{{fy}}}\\right) = {bearing_deg}^\\circ$.\n"
        f"   Written as a standard three-figure bearing: **{bearing_deg:03d}°**."
    )

    vectors = [
        (float(fx), 0.0, f"Feast={fx}N", "#2563eb", False),
        (0.0, float(fy), f"Fnorth={fy}N", "#dc2626", False),
        (float(fx), float(fy), f"R={r_mag}N[{bearing_deg:03d}deg]", "#16a34a", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(r_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "13_resultant_perpendicular_vectors_bearing",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "elementary_resultant_bearing",
        "difficulty": "medium",
        "marks": 4,
        "misconception_tags": ["measured_bearing_counterclockwise", "omitted_leading_zero_in_three_figure_bearing"],
        "hints": {
            "tier_1": "Bearings are measured clockwise from North (the positive y-axis).",
            "tier_2": f"Bearing angle $\\beta = \\arctan(F_{{\\text{{East}}}} / F_{{\\text{{North}}}}) = \\arctan({fx} / {fy})$.",
            "tier_3": f"Magnitude: {r_mag} N. Bearing: {bearing_deg:03d}°.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Pythagoras calculation R = sqrt(Fx^2 + Fy^2)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Resultant magnitude = {r_mag} N", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Bearing angle ratio tan(beta) = Feast / Fnorth", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Three-figure bearing format: {bearing_deg:03d} deg", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 14: Perpendicular Vectors Tail-to-Head Sketch
# --------------------------------------------------------------------------- #
def build_14_perpendicular_vectors_tail_to_head_sketch(rng: random.Random) -> Dict[str, Any]:
    f1 = rng.choice([20, 30, 40])
    f2 = rng.choice([15, 25, 35])
    r_val = round(math.hypot(f1, f2), 1)

    prompt = (
        f"A crate is acted upon by two forces: $\\vec{{F}}_1 = {f1}\\,\\text{{N}}$ horizontally to the right "
        f"and $\\vec{{F}}_2 = {f2}\\,\\text{{N}}$ vertically upwards.\n\n"
        f"The tail-to-head vector addition construction is shown on the Cartesian plane.\n\n"
        f"1. Describe the two essential steps of the **tail-to-head method** of vector addition in two dimensions.\n"
        f"2. Calculate the magnitude of the resultant vector $\\vec{{R}}$ in newtons (to 1 decimal place)."
    )

    ans_latex = (
        rf"R = \sqrt{{{f1}^2 + {f2}^2}} = {_fmt_sa(r_val)}\,\text{{N}}; \quad "
        rf"\text{{Draw first vector from origin; place tail of second at head of first; resultant spans from tail of first to head of last}}"
    )
    worked_solution = (
        f"1. Steps of the tail-to-head method:\n"
        f"   - Draw the first vector from the origin representing magnitude and direction.\n"
        f"   - Place the tail of the second vector at the head (arrow tip) of the first vector.\n"
        f"   - The resultant vector $\\vec{{R}}$ is drawn from the tail of the first vector to the head of the last vector.\n"
        f"2. Magnitude: $R = \\sqrt{{{f1}^2 + {f2}^2}} = {_fmt_sa(r_val)}\\,\\text{{N}}$."
    )

    vectors = [
        (float(f1), 0.0, f"F1={f1}N", "#2563eb", False),
        (float(f1), float(f2), f"R={_fmt_sa(r_val)}N", "#16a34a", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(r_val) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "14_perpendicular_vectors_tail_to_head_sketch",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_tail_to_head_method",
        "difficulty": "easy",
        "marks": 4,
        "misconception_tags": ["drew_resultant_from_head_to_tail", "confused_tail_to_head_with_parallelogram_method"],
        "hints": {
            "tier_1": "Tail of second vector connects to head of first vector.",
            "tier_2": "Resultant starts at tail of first and points to head of last.",
            "tier_3": f"Magnitude: $R = \\sqrt{{{f1}^2 + {f2}^2}} = {_fmt_sa(r_val)}\\,\\text{{N}}$.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Step 1: Place tail of second vector at head of first", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Step 2: Resultant connects tail of first to head of last", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Pythagoras formula and substitution: sqrt({f1}^2 + {f2}^2)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Resultant magnitude = {_fmt_sa(r_val)} N", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 15: Resultant of Three Orthogonal Forces
# --------------------------------------------------------------------------- #
def build_15_resultant_of_three_orthogonal_forces(rng: random.Random) -> Dict[str, Any]:
    f_east = rng.choice([50, 70, 90])
    f_west = rng.choice([20, 30, 40])
    f_north = rng.choice([40, 60, 80])

    rx = f_east - f_west  # net East
    ry = f_north          # net North
    r_mag = round(math.hypot(rx, ry), 1)
    theta = round(math.degrees(math.atan(ry / rx)), 1)

    prompt = (
        f"Three orthogonal forces act concurrently at an eye-bolt:\n"
        f"$\\vec{{F}}_1 = {f_east}\\,\\text{{N}}$ due East,\n"
        f"$\\vec{{F}}_2 = {f_west}\\,\\text{{N}}$ due West, and\n"
        f"$\\vec{{F}}_3 = {f_north}\\,\\text{{N}}$ due North.\n\n"
        f"The forces and resultant vector are shown on the Cartesian plane.\n\n"
        f"1. Calculate the net horizontal component ($R_x$) and net vertical component ($R_y$).\n"
        f"2. Calculate the magnitude of the overall resultant force $\\vec{{R}}$ (to 1 decimal place).\n"
        f"3. State the direction angle $\\theta$ of $\\vec{{R}}$ North of East."
    )

    ans_latex = (
        rf"R_x = {rx}\,\text{{N}}, \quad R_y = {ry}\,\text{{N}}, \quad "
        rf"R = {_fmt_sa(r_mag)}\,\text{{N}}, \quad \theta = {_fmt_sa(theta)}^\circ\text{{ North of East}}"
    )
    worked_solution = (
        f"1. Net components:\n"
        f"   - $R_x = F_{{\\text{{East}}}} - F_{{\\text{{West}}}} = {f_east} - {f_west} = {rx}\\,\\text{{N}}$ (East).\n"
        f"   - $R_y = F_{{\\text{{North}}}} = {ry}\\,\\text{{N}}$ (North).\n"
        f"2. Overall resultant magnitude:\n"
        f"   $R = \\sqrt{{R_x^2 + R_y^2}} = \\sqrt{{{rx}^2 + {ry}^2}} = {_fmt_sa(r_mag)}\\,\\text{{N}}$.\n"
        f"3. Direction: $\\theta = \\tan^{{-1}}\\left(\\frac{{{ry}}}{{{rx}}}\\right) = {_fmt_sa(theta)}^\\circ$ North of East."
    )

    vectors = [
        (float(rx), float(ry), f"R={_fmt_sa(r_mag)}N", "#16a34a", False),
        (float(rx), 0.0, f"Rx={rx}N", "#2563eb", True),
        (0.0, float(ry), f"Ry={ry}N", "#dc2626", True),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(r_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "15_resultant_of_three_orthogonal_forces",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "elementary_three_orthogonal_forces",
        "difficulty": "medium",
        "marks": 5,
        "misconception_tags": ["added_opposing_horizontal_forces_instead_of_subtracting", "forgot_to_combine_collinear_forces_first"],
        "hints": {
            "tier_1": "Combine collinear forces along each axis first: $R_x = \\text{East} - \\text{West}$.",
            "tier_2": f"Here $R_x = {f_east} - {f_west} = {rx}\\,\\text{{N}}$ and $R_y = {ry}\\,\\text{{N}}$.",
            "tier_3": f"Resultant: $R = \\sqrt{{{rx}^2 + {ry}^2}} = {_fmt_sa(r_mag)}\\,\\text{{N}}$ at {_fmt_sa(theta)}° North of East.",
        },
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Net Rx calculation: {f_east} - {f_west} = {rx} N", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Net Ry value: {ry} N", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Pythagoras substitution for resultant R", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Resultant magnitude = {_fmt_sa(r_mag)} N", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Direction angle = {_fmt_sa(theta)} deg North of East", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 16: Multiple Vectors Sum of Horizontal Components
# --------------------------------------------------------------------------- #
def build_16_multiple_vectors_sum_of_horizontal_components(rng: random.Random) -> Dict[str, Any]:
    f1_mag = rng.choice([40, 50, 60])
    theta1 = rng.choice([25, 30, 45])
    f2_mag = rng.choice([30, 40, 50])
    theta2 = rng.choice([30, 45, 60])  # in Quad 2: directed North of West

    rad1 = math.radians(theta1)
    rad2 = math.radians(theta2)

    f1x = f1_mag * math.cos(rad1)
    f2x = -f2_mag * math.cos(rad2)  # negative (West)
    rx = round(f1x + f2x, 2)

    prompt = (
        f"Two concurrent forces act on a bracket:\n"
        f"$\\vec{{F}}_1 = {f1_mag}\\,\\text{{N}}$ at {theta1}° North of East (Quadrant 1), and\n"
        f"$\\vec{{F}}_2 = {f2_mag}\\,\\text{{N}}$ at {theta2}° North of West (Quadrant 2).\n\n"
        f"The forces are illustrated on the Cartesian plane shown.\n\n"
        f"1. Write down the algebraic expressions for $F_{{1x}}$ and $F_{{2x}}$.\n"
        f"2. Calculate the net horizontal component $R_x = \\sum F_x$ in newtons (to 2 decimal places)."
    )

    ans_latex = rf"R_x = {f1_mag}\cos({theta1}^\circ) - {f2_mag}\cos({theta2}^\circ) = {_fmt_sa(rx, 2)}\,\text{{N}}"
    worked_solution = (
        f"1. Horizontal components:\n"
        f"   - $F_{{1x}} = +{f1_mag}\\cos({theta1}^\\circ) = +{_fmt_sa(f1x, 2)}\\,\\text{{N}}$ (East).\n"
        f"   - $F_{{2x}} = -{f2_mag}\\cos({theta2}^\\circ) = {_fmt_sa(f2x, 2)}\\,\\text{{N}}$ (West, negative).\n"
        f"2. Net horizontal component:\n"
        f"   $R_x = F_{{1x}} + F_{{2x}} = {_fmt_sa(f1x, 2)} + ({_fmt_sa(f2x, 2)}) = {_fmt_sa(rx, 2)}\\,\\text{{N}}$."
    )

    vectors = [
        (f1_mag * math.cos(rad1), f1_mag * math.sin(rad1), f"F1={f1_mag}N", "#2563eb", False),
        (-f2_mag * math.cos(rad2), f2_mag * math.sin(rad2), f"F2={f2_mag}N", "#dc2626", False),
        (rx, 0.0, f"Rx={_fmt_sa(rx)}N", "#16a34a", True),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(max(f1_mag, f2_mag)) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "16_multiple_vectors_sum_of_horizontal_components",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "elementary_component_sum_horizontal",
        "difficulty": "medium",
        "marks": 4,
        "misconception_tags": ["forgot_negative_sign_for_westward_component", "used_sine_instead_of_cosine_for_horizontal"],
        "hints": {
            "tier_1": "Recall: East is positive (+) and West is negative (-). Use cosine for angles to horizontal.",
            "tier_2": f"$F_{{1x}} = +{f1_mag}\\cos({theta1}^\\circ)$ and $F_{{2x}} = -{f2_mag}\\cos({theta2}^\\circ)$.",
            "tier_3": f"Sum $R_x = {_fmt_sa(rx, 2)}\\,\\text{{N}}$.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"F1x formula: +{f1_mag} * cos({theta1} deg)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"F2x formula with negative sign: -{f2_mag} * cos({theta2} deg)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Summation setup: Rx = F1x + F2x", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final Rx value: {_fmt_sa(rx, 2)} N", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 17: Multiple Vectors Sum of Vertical Components
# --------------------------------------------------------------------------- #
def build_17_multiple_vectors_sum_of_vertical_components(rng: random.Random) -> Dict[str, Any]:
    f1_mag = rng.choice([40, 50, 60])
    theta1 = rng.choice([25, 30, 45])
    f2_mag = rng.choice([30, 40, 50])
    theta2 = rng.choice([30, 45, 60])

    rad1 = math.radians(theta1)
    rad2 = math.radians(theta2)

    f1y = f1_mag * math.sin(rad1)
    f2y = f2_mag * math.sin(rad2)  # both North (+)
    ry = round(f1y + f2y, 2)

    prompt = (
        f"Two forces pull on a structural pin:\n"
        f"$\\vec{{F}}_1 = {f1_mag}\\,\\text{{N}}$ at {theta1}° above the horizontal (Quadrant 1), and\n"
        f"$\\vec{{F}}_2 = {f2_mag}\\,\\text{{N}}$ at {theta2}° above the horizontal (Quadrant 2).\n\n"
        f"The forces are shown on the Cartesian coordinate plane.\n\n"
        f"1. Write down the algebraic expressions for $F_{{1y}}$ and $F_{{2y}}$.\n"
        f"2. Calculate the net vertical component $R_y = \\sum F_y$ in newtons (to 2 decimal places)."
    )

    ans_latex = rf"R_y = {f1_mag}\sin({theta1}^\circ) + {f2_mag}\sin({theta2}^\circ) = {_fmt_sa(ry, 2)}\,\text{{N}}"
    worked_solution = (
        f"1. Vertical components:\n"
        f"   - $F_{{1y}} = +{f1_mag}\\sin({theta1}^\\circ) = {_fmt_sa(f1y, 2)}\\,\\text{{N}}$ (North).\n"
        f"   - $F_{{2y}} = +{f2_mag}\\sin({theta2}^\\circ) = {_fmt_sa(f2y, 2)}\\,\\text{{N}}$ (North).\n"
        f"2. Net vertical component:\n"
        f"   $R_y = F_{{1y}} + F_{{2y}} = {_fmt_sa(f1y, 2)} + {_fmt_sa(f2y, 2)} = {_fmt_sa(ry, 2)}\\,\\text{{N}}$."
    )

    vectors = [
        (f1_mag * math.cos(rad1), f1y, f"F1={f1_mag}N", "#2563eb", False),
        (-f2_mag * math.cos(rad2), f2y, f"F2={f2_mag}N", "#dc2626", False),
        (0.0, ry, f"Ry={_fmt_sa(ry)}N", "#16a34a", True),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(ry) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "17_multiple_vectors_sum_of_vertical_components",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "elementary_component_sum_vertical",
        "difficulty": "medium",
        "marks": 4,
        "misconception_tags": ["used_cosine_instead_of_sine_for_vertical", "subtracted_instead_of_adding_northward_components"],
        "hints": {
            "tier_1": "Both forces pull upward (North), so both vertical components are positive (+).",
            "tier_2": f"Use sine: $F_{{1y}} = {f1_mag}\\sin({theta1}^\\circ)$ and $F_{{2y}} = {f2_mag}\\sin({theta2}^\\circ)$.",
            "tier_3": f"Sum $R_y = {_fmt_sa(ry, 2)}\\,\\text{{N}}$.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"F1y formula: {f1_mag} * sin({theta1} deg)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"F2y formula: {f2_mag} * sin({theta2} deg)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Summation setup: Ry = F1y + F2y", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final Ry value: {_fmt_sa(ry, 2)} N", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 18: Multiple Vectors Resultant Magnitude
# --------------------------------------------------------------------------- #
def build_18_multiple_vectors_resultant_magnitude(rng: random.Random) -> Dict[str, Any]:
    rx = rng.choice([25, 30, 40, 50, 60])
    ry = rng.choice([35, 45, 55, 65, 75])

    r_mag = round(math.hypot(rx, ry), 2)

    prompt = (
        f"A system of concurrent coplanar forces has been resolved into net rectangular components:\n"
        f"$$\\sum F_x = {rx}\\,\\text{{N}} \\quad \\text{{and}} \\quad \\sum F_y = {ry}\\,\\text{{N}}$$\n\n"
        f"The net components and the resultant vector are plotted on the Cartesian plane shown.\n\n"
        f"1. State the formula used to calculate the magnitude of the resultant vector $R$.\n"
        f"2. Calculate the magnitude of $R$ in newtons (to 2 decimal places)."
    )

    ans_latex = rf"R = \sqrt{{(\sum F_x)^2 + (\sum F_y)^2}} = \sqrt{{{rx}^2 + {ry}^2}} = {_fmt_sa(r_mag, 2)}\,\text{{N}}"
    worked_solution = (
        f"1. Formula: $R = \\sqrt{{R_x^2 + R_y^2}} = \\sqrt{{(\\sum F_x)^2 + (\\sum F_y)^2}}$.\n"
        f"2. Calculation:\n"
        f"   $R = \\sqrt{{{rx}^2 + {ry}^2}} = \\sqrt{{{rx**2} + {ry**2}}} = {_fmt_sa(r_mag, 2)}\\,\\text{{N}}$."
    )

    vectors = [
        (float(rx), float(ry), f"R={_fmt_sa(r_mag)}N", "#16a34a", False),
        (float(rx), 0.0, f"Rx={rx}N", "#2563eb", True),
        (0.0, float(ry), f"Ry={ry}N", "#dc2626", True),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(r_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "18_multiple_vectors_resultant_magnitude",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "mode": "elementary_resultant_magnitude",
        "difficulty": "medium",
        "marks": 3,
        "misconception_tags": ["added_components_linearly_instead_of_quadrature", "forgot_square_root"],
        "hints": {
            "tier_1": "Combine the perpendicular components using the Theorem of Pythagoras.",
            "tier_2": f"Calculation: $R = \\sqrt{{{rx}^2 + {ry}^2}}$.",
            "tier_3": f"Result: $R = {_fmt_sa(r_mag, 2)}\\,\\text{{N}}$.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Pythagoras formula R = sqrt(Rx^2 + Ry^2)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substitution: sqrt({rx}^2 + {ry}^2)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Resultant magnitude = {_fmt_sa(r_mag, 2)} N", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 19: Multiple Vectors Resultant Direction
# --------------------------------------------------------------------------- #
def build_19_multiple_vectors_resultant_direction(rng: random.Random) -> Dict[str, Any]:
    rx = rng.choice([35, 45, 55, 65])
    ry = rng.choice([25, 35, 45, 55])

    theta = round(math.degrees(math.atan(ry / rx)), 1)
    r_mag = round(math.hypot(rx, ry), 1)

    prompt = (
        f"A system of coplanar forces yields net orthogonal components:\n"
        f"$$R_x = {rx}\\,\\text{{N}} \\quad \\text{{and}} \\quad R_y = {ry}\\,\\text{{N}}$$\n\n"
        f"The components and resultant angle $\\theta$ are plotted on the Cartesian plane shown.\n\n"
        f"1. State the trigonometric formula used to determine the direction angle $\\theta$.\n"
        f"2. Calculate the direction of the resultant vector in degrees North of East (to 1 decimal place)."
    )

    ans_latex = rf"\theta = \tan^{{-1}}\left(\frac{{{ry}}}{{{rx}}}\right) = {_fmt_sa(theta)}^\circ\text{{ North of East}}"
    worked_solution = (
        f"1. Formula: $\\tan\\theta = \\frac{{R_y}}{{R_x}}$.\n"
        f"2. Calculation:\n"
        f"   $\\theta = \\tan^{{-1}}\\left(\\frac{{{ry}}}{{{rx}}}\\right) = {_fmt_sa(theta)}^\\circ$ North of East."
    )

    vectors = [
        (float(rx), float(ry), f"R={_fmt_sa(r_mag)}N({_fmt_sa(theta)}deg)", "#16a34a", False),
        (float(rx), 0.0, f"Rx={rx}N", "#2563eb", True),
        (0.0, float(ry), f"Ry={ry}N", "#dc2626", True),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(r_mag) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "19_multiple_vectors_resultant_direction",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_resultant_direction",
        "difficulty": "medium",
        "marks": 3,
        "misconception_tags": ["inverted_tangent_ratio_rx_over_ry", "omitted_directional_reference_north_of_east"],
        "hints": {
            "tier_1": "Use $\\tan\\theta = \\text{opposite} / \\text{adjacent} = R_y / R_x$.",
            "tier_2": f"$\\theta = \\arctan({ry} / {rx})$.",
            "tier_3": f"Direction: {_fmt_sa(theta)}° North of East.",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Tangent formula tan(theta) = Ry / Rx", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Substitution: arctan({ry} / {rx})", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Angle = {_fmt_sa(theta)} deg North of East", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 20: Multiple Forces Applied to Single Point (Engineering)
# --------------------------------------------------------------------------- #
def build_20_multiple_forces_applied_to_single_point_engineering(rng: random.Random) -> Dict[str, Any]:
    f1 = rng.choice([60, 80, 100])
    th1 = 0  # along +x
    f2 = rng.choice([40, 50, 60])
    th2 = 90  # along +y
    f3 = rng.choice([50, 70])
    th3 = rng.choice([30, 45])  # in Quad 2: at th3 above -x

    rad3 = math.radians(th3)
    rx = round(f1 - f3 * math.cos(rad3), 2)
    ry = round(f2 + f3 * math.sin(rad3), 2)
    r_mag = round(math.hypot(rx, ry), 2)
    theta = round(math.degrees(math.atan(ry / rx)), 1)

    prompt = (
        f"Three structural cables apply concurrent tensile forces at joint $O$ of a tower:\n"
        f"$\\vec{{F}}_1 = {f1}\\,\\text{{N}}$ horizontally East,\n"
        f"$\\vec{{F}}_2 = {f2}\\,\\text{{N}}$ vertically North, and\n"
        f"$\\vec{{F}}_3 = {f3}\\,\\text{{N}}$ pulling at {th3}° above the negative x-axis (West).\n\n"
        f"The joint and cable forces are plotted on the Cartesian plane shown.\n\n"
        f"1. Calculate the net horizontal component $R_x$ and net vertical component $R_y$.\n"
        f"2. Calculate the magnitude of the resultant force $\\vec{{R}}$ on the joint (to 2 decimal places).\n"
        f"3. State the direction of $\\vec{{R}}$ in degrees North of East."
    )

    ans_latex = (
        rf"R_x = {_fmt_sa(rx, 2)}\,\text{{N}}, \quad R_y = {_fmt_sa(ry, 2)}\,\text{{N}}, \quad "
        rf"R = {_fmt_sa(r_mag, 2)}\,\text{{N}}, \quad \theta = {_fmt_sa(theta)}^\circ\text{{ North of East}}"
    )
    worked_solution = (
        f"1. Net components:\n"
        f"   - $R_x = F_1 - F_3\\cos({th3}^\\circ) = {f1} - ({f3})\\cos({th3}^\\circ) = {_fmt_sa(rx, 2)}\\,\\text{{N}}$.\n"
        f"   - $R_y = F_2 + F_3\\sin({th3}^\\circ) = {f2} + ({f3})\\sin({th3}^\\circ) = {_fmt_sa(ry, 2)}\\,\\text{{N}}$.\n"
        f"2. Resultant magnitude:\n"
        f"   $R = \\sqrt{{R_x^2 + R_y^2}} = \\sqrt{{{rx}^2 + {ry}^2}} = {_fmt_sa(r_mag, 2)}\\,\\text{{N}}$.\n"
        f"3. Resultant direction:\n"
        f"   $\\theta = \\tan^{{-1}}\\left(\\frac{{{ry}}}{{{rx}}}\\right) = {_fmt_sa(theta)}^\\circ$ North of East."
    )

    vectors = [
        (float(f1), 0.0, f"F1={f1}N(E)", "#2563eb", False),
        (0.0, float(f2), f"F2={f2}N(N)", "#dc2626", False),
        (-f3 * math.cos(rad3), f3 * math.sin(rad3), f"F3={f3}N", "#9333ea", False),
        (rx, ry, f"R={_fmt_sa(r_mag)}N", "#16a34a", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(max(f1, r_mag)) * 1.3, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "20_multiple_forces_applied_to_single_point_engineering",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
        "misconception_tags": ["sign_error_in_westward_component_resolution", "incorrect_quadrant_direction_classification"],
        "hints": {
            "tier_1": "Resolve $F_3$ into horizontal (West, -) and vertical (North, +) components. Then sum components.",
            "tier_2": f"$R_x = {f1} - {f3}\\cos({th3}^\\circ) = {_fmt_sa(rx, 2)}\\,\\text{{N}}$. $R_y = {f2} + {f3}\\sin({th3}^\\circ) = {_fmt_sa(ry, 2)}\\,\\text{{N}}$.",
            "tier_3": f"Resultant: $R = {_fmt_sa(r_mag, 2)}\\,\\text{{N}}$ at {_fmt_sa(theta)}° North of East.",
        },
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Rx resolution and calculation: {_fmt_sa(rx, 2)} N", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Ry resolution and calculation: {_fmt_sa(ry, 2)} N", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Resultant magnitude = {_fmt_sa(r_mag, 2)} N", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Resultant angle = {_fmt_sa(theta)} deg", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 21: Equilibrant Vector Definition and Relation to Resultant
# --------------------------------------------------------------------------- #
def build_21_equilibrant_vector_definition_and_relation_to_resultant(rng: random.Random) -> Dict[str, Any]:
    r_mag = rng.choice([40, 50, 60, 80, 100])
    theta = rng.choice([25, 30, 45, 60])

    prompt = (
        f"A system of forces acting on a ring has a resultant vector $\\vec{{R}} = {r_mag}\\,\\text{{N}}$ "
        f"at an angle of {theta}° North of East.\n\n"
        f"The resultant vector $\\vec{{R}}$ and the equilibrant vector $\\vec{{E}}$ are plotted on the Cartesian plane shown.\n\n"
        f"1. Define the term **equilibrant vector**.\n"
        f"2. State the magnitude of the equilibrant vector $\\vec{{E}}$.\n"
        f"3. State the exact direction of the equilibrant vector $\\vec{{E}}$."
    )

    opp_theta = theta  # South of West
    bearing = (theta + 180) % 360
    ans_latex = (
        rf"E = {r_mag}\,\text{{N}}, \quad \text{{Direction: {theta}^\circ\text{{ South of West (or bearing }}{bearing:03d}^\circ)}}"
    )
    worked_solution = (
        f"1. Definition: The equilibrant is the single force vector that balances two or more forces acting together, "
        f"bringing the system into static equilibrium.\n"
        f"2. Relationship to resultant:\n"
        f"   - Magnitude: The equilibrant has the **same magnitude** as the resultant: $E = {r_mag}\\,\\text{{N}}$.\n"
        f"   - Direction: The equilibrant acts in the **exact opposite direction** (180° reversed):\n"
        f"     $\\theta_{{\\text{{equilibrant}}}} = {theta}^\\circ$ South of West (bearing {bearing:03d}°)."
    )

    rad = math.radians(theta)
    v_res = (r_mag * math.cos(rad), r_mag * math.sin(rad), f"R={r_mag}N({theta}deg)", "#16a34a", False)
    v_eq = (-r_mag * math.cos(rad), -r_mag * math.sin(rad), f"E={r_mag}N", "#dc2626", False)
    svg = _make_vector_cartesian_svg([v_res, v_eq], max_coord=float(r_mag) * 1.35, seed=rng.randint(1000, 999999))

    return {
        "subskill": "21_equilibrant_vector_definition_and_relation_to_resultant",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_equilibrant_definition",
        "difficulty": "easy",
        "marks": 4,
        "misconception_tags": ["confused_equilibrant_with_resultant", "negated_equilibrant_magnitude"],
        "hints": {
            "tier_1": "The equilibrant is equal in magnitude and opposite in direction to the resultant: $\\vec{E} = -\\vec{R}$.",
            "tier_2": f"Magnitude is {r_mag} N. Direction is 180° opposite to {theta}° North of East.",
            "tier_3": f"E = {r_mag} N, {theta}° South of West.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: Force that balances a system of forces / produces equilibrium", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Equilibrant magnitude = {r_mag} N", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Direction = {theta} deg South of West (or opposite direction)", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 22: Equilibrant of Perpendicular Forces
# --------------------------------------------------------------------------- #
def build_22_equilibrant_perpendicular_forces_calculation(rng: random.Random) -> Dict[str, Any]:
    triples = [(30, 40, 50), (60, 80, 100), (50, 120, 130), (40, 30, 50)]
    fx, fy, r_mag = rng.choice(triples)

    theta = round(math.degrees(math.atan(fy / fx)), 1)
    eq_angle = theta  # South of West

    prompt = (
        f"Two perpendicular forces act on a stationary pin: $F_1 = {fx}\\,\\text{{N}}$ East "
        f"and $F_2 = {fy}\\,\\text{{N}}$ North.\n\n"
        f"The forces and the balancing equilibrant $\\vec{{E}}$ are shown on the Cartesian plane.\n\n"
        f"1. Calculate the magnitude of the equilibrant force $\\vec{{E}}$ needed to keep the pin in equilibrium.\n"
        f"2. State the direction of $\\vec{{E}}$ relative to the cardinal compass directions."
    )

    ans_latex = rf"E = {r_mag}\,\text{{N}}, \quad \text{{Direction: {_fmt_sa(eq_angle)}^\circ\text{{ South of West}}}}"
    worked_solution = (
        f"1. Calculate the resultant first:\n"
        f"   $R = \\sqrt{{F_1^2 + F_2^2}} = \\sqrt{{{fx}^2 + {fy}^2}} = {r_mag}\\,\\text{{N}}$.\n"
        f"   $\\theta = \\tan^{{-1}}\\left(\\frac{{{fy}}}{{{fx}}}\\right) = {_fmt_sa(theta)}^\\circ$ North of East.\n"
        f"2. Equilibrant is equal in magnitude and opposite in direction:\n"
        f"   - Magnitude: $E = R = {r_mag}\\,\\text{{N}}$.\n"
        f"   - Direction: {_fmt_sa(eq_angle)}° South of West."
    )

    vectors = [
        (float(fx), 0.0, f"F1={fx}N(E)", "#2563eb", False),
        (0.0, float(fy), f"F2={fy}N(N)", "#2563eb", False),
        (-float(fx), -float(fy), f"E={r_mag}N", "#dc2626", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(r_mag) * 1.35, seed=rng.randint(1000, 999999))

    return {
        "subskill": "22_equilibrant_perpendicular_forces_calculation",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "mode": "elementary_equilibrant_perpendicular",
        "difficulty": "medium",
        "marks": 4,
        "misconception_tags": ["gave_resultant_direction_instead_of_equilibrant", "calculated_wrong_opposite_angle"],
        "hints": {
            "tier_1": "Find resultant magnitude using Pythagoras, then reverse the direction by 180° for the equilibrant.",
            "tier_2": f"Resultant is {r_mag} N at {_fmt_sa(theta)}° North of East. Equilibrant points in the opposite direction.",
            "tier_3": f"E = {r_mag} N at {_fmt_sa(eq_angle)}° South of West.",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Pythagoras calculation of resultant magnitude", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Equilibrant magnitude = {r_mag} N", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Resultant angle calculation: {_fmt_sa(theta)} deg", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Equilibrant direction = {_fmt_sa(eq_angle)} deg South of West", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 23: Equilibrant of Multiple Coplanar Forces
# --------------------------------------------------------------------------- #
def build_23_equilibrant_multiple_coplanar_forces(rng: random.Random) -> Dict[str, Any]:
    rx = rng.choice([20, 30, 40, 50])
    ry = rng.choice([20, 30, 40, 50])

    r_mag = round(math.hypot(rx, ry), 2)
    theta = round(math.degrees(math.atan(ry / rx)), 1)

    ex = -rx
    ey = -ry

    prompt = (
        f"A particle is subjected to three coplanar forces whose vector sum yields net components:\n"
        f"$$R_x = {rx}\\,\\text{{N}} \\quad \\text{{and}} \\quad R_y = {ry}\\,\\text{{N}}$$\n\n"
        f"The net force and the required equilibrant force $\\vec{{E}}$ are shown on the Cartesian plane.\n\n"
        f"1. Determine the horizontal component ($E_x$) and vertical component ($E_y$) of the equilibrant force.\n"
        f"2. Calculate the magnitude of $\\vec{{E}}$ (to 2 decimal places).\n"
        f"3. State the direction of $\\vec{{E}}$ in degrees South of West."
    )

    ans_latex = (
        rf"E_x = {ex}\,\text{{N}}, \quad E_y = {ey}\,\text{{N}}, \quad "
        rf"E = {_fmt_sa(r_mag, 2)}\,\text{{N}}, \quad {_fmt_sa(theta)}^\circ\text{{ South of West}}"
    )
    worked_solution = (
        f"1. Equilibrant components are the exact negatives of the resultant components:\n"
        f"   - $E_x = -R_x = {ex}\\,\\text{{N}}$ (West).\n"
        f"   - $E_y = -R_y = {ey}\\,\\text{{N}}$ (South).\n"
        f"2. Magnitude: $E = \\sqrt{{E_x^2 + E_y^2}} = \\sqrt{{{ex}^2 + {ey}^2}} = {_fmt_sa(r_mag, 2)}\\,\\text{{N}}$.\n"
        f"3. Direction: $\\theta = \\tan^{{-1}}\\left(\\frac{{|E_y|}}{{|E_x|}}\\right) = {_fmt_sa(theta)}^\\circ$ South of West."
    )

    vectors = [
        (float(rx), float(ry), f"R={_fmt_sa(r_mag)}N", "#16a34a", True),
        (float(ex), float(ey), f"E={_fmt_sa(r_mag)}N", "#dc2626", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(r_mag) * 1.35, seed=rng.randint(1000, 999999), show_components=True)

    return {
        "subskill": "23_equilibrant_multiple_coplanar_forces",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "elementary_equilibrant_multiple",
        "difficulty": "medium",
        "marks": 5,
        "misconception_tags": ["negated_only_one_component_for_equilibrant", "confused_equilibrant_direction_quadrant"],
        "hints": {
            "tier_1": "For equilibrium, $\\vec{E} = -\\vec{R}$, which means $E_x = -R_x$ and $E_y = -R_y$.",
            "tier_2": f"$E_x = {ex}\\,\\text{{N}}$ and $E_y = {ey}\\,\\text{{N}}$.",
            "tier_3": f"Magnitude is {_fmt_sa(r_mag, 2)} N at {_fmt_sa(theta)}° South of West.",
        },
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Ex component = {ex} N", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Ey component = {ey} N", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Pythagoras calculation of magnitude", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Equilibrant magnitude = {_fmt_sa(r_mag, 2)} N", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Direction = {_fmt_sa(theta)} deg South of West", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 24: Closed Vector Triangle in Static Equilibrium
# --------------------------------------------------------------------------- #
def build_24_closed_vector_triangle_static_equilibrium(rng: random.Random) -> Dict[str, Any]:
    # 3 forces in equilibrium form a closed triangle
    w_mag = rng.choice([60, 80, 100, 120])
    theta = rng.choice([30, 45, 60])  # angle of string to vertical

    rad = math.radians(theta)
    # T*cos(theta) = w, F_horiz = T*sin(theta)
    t_mag = round(w_mag / math.cos(rad), 2)
    f_horiz = round(w_mag * math.tan(rad), 2)

    prompt = (
        f"A small metal sphere of weight $W = {w_mag}\\,\\text{{N}}$ is suspended by a light string. "
        f"A horizontal pulling force $\\vec{{F}}_{{\\text{{h}}}}$ holds the sphere in static equilibrium "
        f"so that the string makes an angle of {theta}° with the vertical ceiling.\n\n"
        f"The closed vector triangle representing the three forces in equilibrium is shown on the Cartesian plane.\n\n"
        f"1. Explain why the three force vectors form a closed triangle.\n"
        f"2. Calculate the tension $T$ in the string in newtons (to 2 decimal places).\n"
        f"3. Calculate the magnitude of the horizontal force $F_{{\\text{{h}}}}$ in newtons."
    )

    ans_latex = (
        rf"T = \frac{{{w_mag}}}{{\cos({theta}^\circ)}} = {_fmt_sa(t_mag, 2)}\,\text{{N}}, \quad "
        rf"F_{{\text{{h}}}} = {w_mag}\tan({theta}^\circ) = {_fmt_sa(f_horiz, 2)}\,\text{{N}}"
    )
    worked_solution = (
        f"1. The three forces form a closed triangle because the system is in static equilibrium, "
        f"meaning the net resultant force is zero ($\\vec{{F}}_{{\\text{{net}}}} = \\vec{{F}}_1 + \\vec{{F}}_2 + \\vec{{F}}_3 = 0$).\n"
        f"2. Using the right-angled vector triangle:\n"
        f"   - Vertical: $T\\cos({theta}^\\circ) = W \\implies T = \\frac{{{w_mag}}}{{\\cos({theta}^\\circ)}} = {_fmt_sa(t_mag, 2)}\\,\\text{{N}}$.\n"
        f"3. Horizontal:\n"
        f"   - $F_{{\\text{{h}}}} = T\\sin({theta}^\\circ) = W\\tan({theta}^\\circ) = ({w_mag})\\tan({theta}^\\circ) = {_fmt_sa(f_horiz, 2)}\\,\\text{{N}}$."
    )

    vectors = [
        (0.0, -float(w_mag), f"W={w_mag}N", "#dc2626", False),
        (float(f_horiz), 0.0, f"Fh={_fmt_sa(f_horiz)}N", "#2563eb", False),
        (-float(f_horiz), float(w_mag), f"T={_fmt_sa(t_mag)}N", "#16a34a", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(max(w_mag, t_mag)) * 1.3, seed=rng.randint(1000, 999999))

    return {
        "subskill": "24_closed_vector_triangle_static_equilibrium",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "elementary_closed_triangle_equilibrium",
        "difficulty": "medium",
        "marks": 5,
        "misconception_tags": ["swapped_sin_and_cos_in_equilibrium_triangle", "confused_resultant_with_zero_net_force"],
        "hints": {
            "tier_1": "In equilibrium, the net force is zero, so the vector polygon closes tail-to-head.",
            "tier_2": f"Vertical balance: $T\\cos({theta}^\\circ) = {w_mag}$. Horizontal balance: $F_h = T\\sin({theta}^\\circ)$.",
            "tier_3": f"Tension $T = {_fmt_sa(t_mag, 2)}\\,\\text{{N}}$, $F_h = {_fmt_sa(f_horiz, 2)}\\,\\text{{N}}$.",
        },
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Explanation: Net force is zero in static equilibrium", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Vertical equation T * cos(theta) = W", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Tension T = {_fmt_sa(t_mag, 2)} N", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Horizontal equation Fh = T * sin(theta) or W * tan(theta)", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Horizontal force Fh = {_fmt_sa(f_horiz, 2)} N", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Subskill 25: Equilibrium Suspended Mass Two Cables Tensions
# --------------------------------------------------------------------------- #
def build_25_equilibrium_suspended_mass_two_cables_tensions(rng: random.Random) -> Dict[str, Any]:
    # Symmetric two-cable suspension: 2*T*sin(theta) = mg (theta above horizontal)
    mass_kg = rng.choice([10, 15, 20, 25, 30])
    g_val = 9.8
    w_mag = round(mass_kg * g_val, 1)

    theta = rng.choice([30, 45, 60])  # angle of each cable above horizontal
    rad = math.radians(theta)

    t_each = round(w_mag / (2 * math.sin(rad)), 2)

    prompt = (
        f"A traffic light of mass $m = {mass_kg}\\,\\text{{kg}}$ is suspended in static equilibrium "
        f"by two identical cables connected symmetrically to horizontal posts. "
        f"Each cable makes an angle of {theta}° with the horizontal.\n\n"
        f"Take $g = 9{{,}}8\\,\\text{{m/s}}^2$. The cables, weight, and tension vectors are plotted on the Cartesian plane shown.\n\n"
        f"1. Calculate the weight ($W$) of the traffic light in newtons.\n"
        f"2. Apply equilibrium conditions ($\\sum F_y = 0$) to calculate the tension $T$ in each cable (to 2 decimal places)."
    )

    ans_latex = (
        rf"W = {mass_kg} \times 9{{,}}8 = {_fmt_sa(w_mag, 1)}\,\text{{N}}, \quad "
        rf"T = \frac{{{_fmt_sa(w_mag, 1)}}}{{2\sin({theta}^\circ)}} = {_fmt_sa(t_each, 2)}\,\text{{N}}"
    )
    worked_solution = (
        f"1. Weight calculation:\n"
        f"   $W = mg = ({mass_kg})(9{{,}}8) = {_fmt_sa(w_mag, 1)}\\,\\text{{N}}$.\n"
        f"2. Equilibrium in vertical direction:\n"
        f"   $\\sum F_y = 0 \\implies 2T\\sin({theta}^\\circ) - W = 0$.\n"
        f"   $2T\\sin({theta}^\\circ) = {_fmt_sa(w_mag, 1)}\n"
        f"   $T = \\frac{{{_fmt_sa(w_mag, 1)}}}{{2\\sin({theta}^\\circ)}} = {_fmt_sa(t_each, 2)}\\,\\text{{N}}$."
    )

    tx = t_each * math.cos(rad)
    ty = t_each * math.sin(rad)
    vectors = [
        (tx, ty, f"T1={_fmt_sa(t_each)}N", "#2563eb", False),
        (-tx, ty, f"T2={_fmt_sa(t_each)}N", "#2563eb", False),
        (0.0, -w_mag, f"W={_fmt_sa(w_mag)}N", "#dc2626", False),
    ]
    svg = _make_vector_cartesian_svg(vectors, max_coord=float(max(w_mag, t_each)) * 1.3, seed=rng.randint(1000, 999999))

    return {
        "subskill": "25_equilibrium_suspended_mass_two_cables_tensions",
        "topic": "grade11_physical_sciences_vectors_newton",
        "prompt": prompt,
        "answer_latex": ans_latex,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
        "misconception_tags": ["forgot_factor_of_two_for_symmetrical_cables", "used_cosine_instead_of_sine_for_vertical_tension"],
        "hints": {
            "tier_1": "Each cable provides an upward vertical component $T\\sin\\theta$. Together they support the entire weight: $2T\\sin\\theta = W$.",
            "tier_2": f"Weight $W = {mass_kg} \\times 9{{,}}8 = {_fmt_sa(w_mag, 1)}\\,\\text{{N}}$. Tension $T = W / (2\\sin({theta}^\\circ))$.",
            "tier_3": f"Tension in each cable: $T = {_fmt_sa(t_each, 2)}\\,\\text{{N}}$.",
        },
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Weight formula W = mg substitution", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Weight value = {_fmt_sa(w_mag, 1)} N", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Vertical equilibrium statement 2T * sin({theta}) = W", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Tension substitution W / (2 * sin({theta}))", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Tension value = {_fmt_sa(t_each, 2)} N", "marks": 1, "editable": True},
            ],
        },
    }


# --------------------------------------------------------------------------- #
# Export Dictionary
# --------------------------------------------------------------------------- #
BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_vector_scalar_definition_and_identification": build_01_vector_scalar_definition_and_identification,
    "02_vector_graphical_representation_scale": build_02_vector_graphical_representation_scale,
    "03_cartesian_plane_vector_equality_and_translation": build_03_cartesian_plane_vector_equality_and_translation,
    "04_negative_vectors_opposite_direction": build_04_negative_vectors_opposite_direction,
    "05_collinear_vectors_addition_1d": build_05_collinear_vectors_addition_1d,
    "06_vector_components_horizontal_cosine": build_06_vector_components_horizontal_cosine,
    "07_vector_components_vertical_sine": build_07_vector_components_vertical_sine,
    "08_vector_components_angle_with_vertical": build_08_vector_components_angle_with_vertical,
    "09_vector_reconstruction_from_rectangular_components": build_09_vector_reconstruction_from_rectangular_components,
    "10_vector_components_quadrant_signs": build_10_vector_components_quadrant_signs,
    "11_resultant_two_perpendicular_forces_pythagoras": build_11_resultant_two_perpendicular_forces_pythagoras,
    "12_resultant_direction_perpendicular_forces_angle": build_12_resultant_direction_perpendicular_forces_angle,
    "13_resultant_perpendicular_vectors_bearing": build_13_resultant_perpendicular_vectors_bearing,
    "14_perpendicular_vectors_tail_to_head_sketch": build_14_perpendicular_vectors_tail_to_head_sketch,
    "15_resultant_of_three_orthogonal_forces": build_15_resultant_of_three_orthogonal_forces,
    "16_multiple_vectors_sum_of_horizontal_components": build_16_multiple_vectors_sum_of_horizontal_components,
    "17_multiple_vectors_sum_of_vertical_components": build_17_multiple_vectors_sum_of_vertical_components,
    "18_multiple_vectors_resultant_magnitude": build_18_multiple_vectors_resultant_magnitude,
    "19_multiple_vectors_resultant_direction": build_19_multiple_vectors_resultant_direction,
    "20_multiple_forces_applied_to_single_point_engineering": build_20_multiple_forces_applied_to_single_point_engineering,
    "21_equilibrant_vector_definition_and_relation_to_resultant": build_21_equilibrant_vector_definition_and_relation_to_resultant,
    "22_equilibrant_perpendicular_forces_calculation": build_22_equilibrant_perpendicular_forces_calculation,
    "23_equilibrant_multiple_coplanar_forces": build_23_equilibrant_multiple_coplanar_forces,
    "24_closed_vector_triangle_static_equilibrium": build_24_closed_vector_triangle_static_equilibrium,
    "25_equilibrium_suspended_mass_two_cables_tensions": build_25_equilibrium_suspended_mass_two_cables_tensions,
}

ORDERED_SUBSKILLS_01_25: List[str] = list(BUILDERS_01_25.keys())
SUBSKILLS_01_25: List[str] = list(ORDERED_SUBSKILLS_01_25)
