"""Grade 10 Physical Sciences - Vectors and Scalars (Subskills 01 to 25)
100% Deterministic & SymPy-backed. South African National Curriculum Standards aligned.
Covers:
- Vector vs scalar definitions, magnitude and direction
- Distance vs displacement (1D), speed vs velocity (1D), mass vs weight
- Graphical representation, vector scale drawings, compass conventions, 3-figure bearings
- Equality of vectors and negative vectors
- Collinear vector addition and subtraction (1D), sign conventions, net forces
- Resultant vector definition and concepts
- Tail-to-head and parallelogram methods
- Perpendicular vectors: resultant magnitude (Pythagoras) & direction (trig/bearing)
- Pythagorean triples (3-4-5, 5-12-13, 8-15-17)
- Multi-stage orthogonal vectors and seed-varied inline vector SVG diagrams
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float, places: int = 2) -> str:
    """Format decimal number using South African comma decimal convention."""
    if abs(val - round(val)) < 1e-9:
        return f"{int(round(val))}"
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _vector_svg(
    vectors: List[Dict[str, Any]],
    origin: Tuple[int, int] = (100, 180),
    scale: float = 4.0,
    width: int = 500,
    height: int = 320,
    show_compass: bool = True,
    seed_tag: Optional[int] = None,
) -> str:
    """Build a crisp, high-contrast inline SVG representing 2D vectors.
    vectors: list of dicts with:
      - 'dx': x displacement in units
      - 'dy': y displacement in units (positive = UP)
      - 'start': optional (x, y) start offset in units from origin (default (0, 0))
      - 'color': stroke color (default #1e3a8a navy, #b91c1c red, #047857 green)
      - 'label': text label
      - 'dashed': bool
      - 'arrow': bool (default True)
    """
    ox, oy = origin
    uid = f"vec_{seed_tag if seed_tag is not None else random.randint(100, 99999)}"
    
    elements = []
    # Grid lines / axes
    elements.append(
        f'<defs>'
        f'<marker id="arrow_{uid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b"/>'
        f'</marker>'
        f'<marker id="arrow_red_{uid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 1 L 10 5 L 0 9 z" fill="#b91c1c"/>'
        f'</marker>'
        f'<marker id="arrow_green_{uid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 1 L 10 5 L 0 9 z" fill="#047857"/>'
        f'</marker>'
        f'</defs>'
    )
    
    # Background
    elements.append(f'<rect width="{width}" height="{height}" fill="#f8fafc" rx="8" stroke="#cbd5e1" stroke-width="1"/>')
    
    # Origin marker
    elements.append(f'<circle cx="{ox}" cy="{oy}" r="3.5" fill="#0f172a"/>')
    elements.append(f'<text x="{ox - 14}" y="{oy + 14}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#334155">O</text>')
    
    # Compass rose
    if show_compass:
        cx, cy = width - 45, 45
        elements.append(
            f'<g>'
            f'<circle cx="{cx}" cy="{cy}" r="22" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>'
            f'<line x1="{cx}" y1="{cy+18}" x2="{cx}" y2="{cy-18}" stroke="#475569" stroke-width="1.5"/>'
            f'<line x1="{cx-18}" y1="{cy}" x2="{cx+18}" y2="{cy}" stroke="#475569" stroke-width="1.5"/>'
            f'<text x="{cx-4}" y="{cy-20}" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a">N</text>'
            f'<text x="{cx-3}" y="{cy+28}" font-family="sans-serif" font-size="9" fill="#64748b">S</text>'
            f'<text x="{cx+20}" y="{cy+3}" font-family="sans-serif" font-size="9" fill="#64748b">E</text>'
            f'<text x="{cx-28}" y="{cy+3}" font-family="sans-serif" font-size="9" fill="#64748b">W</text>'
            f'</g>'
        )

    # Render vectors
    for v in vectors:
        s_off = v.get("start", (0, 0))
        x1 = ox + s_off[0] * scale
        y1 = oy - s_off[1] * scale
        x2 = x1 + v["dx"] * scale
        y2 = y1 - v["dy"] * scale
        
        color = v.get("color", "#1e293b")
        marker = f'url(#arrow_{uid})'
        if color == "#b91c1c":
            marker = f'url(#arrow_red_{uid})'
        elif color == "#047857":
            marker = f'url(#arrow_green_{uid})'
            
        dash_attr = ' stroke-dasharray="4,4"' if v.get("dashed") else ""
        sw = v.get("stroke_width", 2.5)
        
        elements.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{sw}"{dash_attr} marker-end="{marker}"/>'
        )
        
        lbl = v.get("label")
        if lbl:
            mx = (x1 + x2) / 2
            my = (y1 + y2) / 2
            # Offset label perpendicular to vector
            vlen = math.hypot(x2 - x1, y2 - y1) or 1.0
            nx = -(y2 - y1) / vlen * 14
            ny = (x2 - x1) / vlen * 14
            elements.append(
                f'<text x="{mx + nx:.1f}" y="{my + ny:.1f}" font-family="sans-serif" font-size="12" font-weight="600" fill="{color}" text-anchor="middle">{lbl}</text>'
            )

    svg_content = "".join(elements)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" data-seed="{seed_tag}">{svg_content}</svg>'


# ============================================================================
# ARCHETYPES 01–25 BUILDERS
# ============================================================================

def build_01_scalar_vs_vector_definition_and_classification(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Classify physical quantities as vectors or scalars with foundational definitions."""
    r = _rng(seed)
    
    scalar_pool = [
        ("time", "s", "has only magnitude (elapsed duration) and no spatial direction"),
        ("mass", "kg", "measures quantity of matter and has only magnitude"),
        ("distance", "m", "is the total length of the actual path travelled, independent of direction"),
        ("speed", "m·s⁻¹", "measures rate of distance covered with magnitude only"),
        ("temperature", "°C / K", "describes thermal state with magnitude only"),
        ("electric charge", "C", "measures quantity of charge with magnitude and algebraic sign only"),
    ]
    vector_pool = [
        ("force", "N", "has both magnitude and a specific direction in which it acts"),
        ("weight", "N", "is the gravitational attraction force directed towards the centre of the Earth"),
        ("displacement", "m", "is the change in position pointing from the initial to final position"),
        ("velocity", "m·s⁻¹", "is the rate of change of position, possessing both magnitude and direction"),
        ("acceleration", "m·s⁻²", "is the rate of change of velocity, having both magnitude and direction"),
    ]
    
    chosen_scalar = r.choice(scalar_pool)
    chosen_vector = r.choice(vector_pool)
    
    # Decide tested quantity
    test_vector = (r.random() < 0.5)
    target = chosen_vector if test_vector else chosen_scalar
    target_type = "vector" if test_vector else "scalar"
    other_type = "scalar" if test_vector else "vector"
    
    prompt = (
        f"Define a {target_type} quantity. Then state whether {target[0]} is a scalar or a vector, "
        f"and justify your answer by referring to its properties."
    )
    
    def_text = (
        "A vector is a physical quantity that has both magnitude and direction."
        if test_vector
        else "A scalar is a physical quantity that has only magnitude (size) and no direction."
    )
    
    sample_answer = (
        f"1. Definition: {def_text}\n"
        f"2. Classification: {target[0].capitalize()} is a {target_type}.\n"
        f"3. Justification: {target[0].capitalize()} {target[2]}."
    )
    
    return {
        "id": f"vec_01_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "01_scalar_vs_vector_definition_and_classification",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"{def_text} {target[0].capitalize()} is a {target_type}.",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["confused_scalar_and_vector", "omitted_direction_in_vector_definition"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_def", "desc": f"Accurate definition of {target_type}", "marks": 1, "editable": True},
                {"id": "mp_class", "desc": f"Correct classification as {target_type}", "marks": 1, "editable": True},
                {"id": "mp_just", "desc": "Valid scientific justification (magnitude vs direction)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": f"Think about whether {target[0]} needs an arrow or compass heading to fully describe it.",
            "2_concept": "Scalars require only a number and unit (magnitude). Vectors require magnitude AND direction.",
            "3_breakdown": f"{target[0].capitalize()} {target[2]}, making it a {target_type}.",
        },
    }


def build_02_magnitude_and_direction_specification(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Extract and specify magnitude (number + unit) and direction from physical vector statements."""
    r = _rng(seed)
    
    scenarios = [
        ("aircraft", "flying at", r.randint(180, 260), "m·s⁻¹", "on a bearing of 045°"),
        ("delivery vehicle", "travelling at", r.randint(15, 30), "m·s⁻¹", "due East"),
        ("crane cable", "exerting an upward tension force of", r.randint(4, 12) * 500, "N", "vertically upwards"),
        ("tugboat", "pulling a barge with a force of", r.randint(25, 60) * 100, "N", "at 30° North of West"),
        ("swimmer", "crossing a channel at", round(r.uniform(1.2, 2.8), 1), "m·s⁻¹", "directed South"),
    ]
    name, action, mag, unit, direction = r.choice(scenarios)
    
    prompt = (
        f"Consider the following statement: 'A {name} is {action} {_fmt_sa(mag)} {unit} {direction}.'\n"
        f"1. Identify the physical quantity described and state whether it is a vector or scalar.\n"
        f"2. Write down the magnitude of this quantity (including the correct SI unit).\n"
        f"3. Write down the direction of this quantity."
    )
    
    qty_name = "Velocity" if "m·s⁻¹" in unit else "Force"
    
    sample_answer = (
        f"1. Physical Quantity: {qty_name} (Vector)\n"
        f"2. Magnitude: {_fmt_sa(mag)} {unit}\n"
        f"3. Direction: {direction}"
    )
    
    return {
        "id": f"vec_02_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "02_magnitude_and_direction_specification",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"Quantity: {qty_name} (Vector), Magnitude: {_fmt_sa(mag)} {unit}, Direction: {direction}",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["omitted_unit_from_magnitude", "confused_magnitude_with_scalar"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Identified quantity as {qty_name} (Vector)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct magnitude with unit: {_fmt_sa(mag)} {unit}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct direction: {direction}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Magnitude means 'how much' (number plus unit). Direction means 'which way'.",
            "2_concept": "A vector statement bundles both the magnitude (size + unit) and spatial direction.",
            "3_breakdown": f"Magnitude is {_fmt_sa(mag)} {unit}; direction is {direction}.",
        },
    }


def build_03_distance_vs_displacement_1d(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate 1D distance (scalar path) vs net displacement (vector change in position)."""
    r = _rng(seed)
    
    d1 = r.randint(6, 18)  # metres east
    d2 = r.randint(2, d1 - 1)  # metres west
    
    total_dist = d1 + d2
    net_disp = d1 - d2
    
    prompt = (
        f"A learner walks {_fmt_sa(d1)} m due East from point A to point B, and then walks {_fmt_sa(d2)} m "
        f"due West from point B to point C along the same straight corridor.\n"
        f"1. Calculate the total distance covered by the learner.\n"
        f"2. Calculate the resultant displacement of the learner relative to point A."
    )
    
    sample_answer = (
        f"1. Total distance = d_1 + d_2 = {_fmt_sa(d1)} + {_fmt_sa(d2)} = {_fmt_sa(total_dist)} m\n"
        f"2. Taking East as the positive reference direction (+):\n"
        rf"\Delta x = (+{_fmt_sa(d1)}) + (-{_fmt_sa(d2)}) = +{_fmt_sa(net_disp)}\text{{ m}}\\"
        f"Net displacement = {_fmt_sa(net_disp)} m due East"
    )
    
    return {
        "id": f"vec_03_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "03_distance_vs_displacement_1d",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"Distance = {_fmt_sa(total_dist)} m; Displacement = {_fmt_sa(net_disp)} m East",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["confused_distance_and_displacement", "omitted_direction_in_displacement"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_dist_f", "desc": "Summing path segments for distance", "marks": 1, "editable": True},
                {"id": "mp_dist_a", "desc": f"Distance = {_fmt_sa(total_dist)} m", "marks": 1, "editable": True},
                {"id": "mp_disp_calc", "desc": "Vector difference with sign convention", "marks": 1, "editable": True},
                {"id": "mp_disp_ans", "desc": f"Displacement = {_fmt_sa(net_disp)} m East (magnitude and direction)", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_direction_for_displacement", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Distance is the total path travelled (scalar, always positive). Displacement is final position minus initial position (vector).",
            "2_concept": "For displacement: choose East as positive (+). Then displacement is (+d1) + (-d2).",
            "3_breakdown": f"Distance = {d1} + {d2} = {total_dist} m. Displacement = {d1} - {d2} = {net_disp} m East.",
        },
    }


def build_04_speed_vs_velocity_1d_average(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Compare average speed (scalar) and average velocity (vector) for 1D round-trip motion."""
    r = _rng(seed)
    
    d_out = r.randint(40, 100) # metres forward
    d_back = r.randint(10, d_out - 10) # metres backward
    t_sec = r.randint(15, 30) # seconds
    
    dist_total = d_out + d_back
    disp_net = d_out - d_back
    
    avg_speed = round(dist_total / t_sec, 2)
    avg_velocity = round(disp_net / t_sec, 2)
    
    prompt = (
        f"A sprint athlete runs {_fmt_sa(d_out)} m forwards (North) and then turns and jogs {_fmt_sa(d_back)} m "
        f"backwards (South) along the track. The entire movement takes {_fmt_sa(t_sec)} seconds.\n"
        f"1. Calculate the athlete's average speed.\n"
        f"2. Calculate the athlete's average velocity."
    )
    
    sample_answer = (
        rf"\text{{Average speed}} = \frac{{\text{{Total distance}}}}{{\Delta t}} = \frac{{{_fmt_sa(dist_total)}}}{{{_fmt_sa(t_sec)}}} = {_fmt_sa(avg_speed)}\text{{ m·s}}^{{-1}}\\"
        rf"\text{{Taking North as positive: }}\Delta x = +{_fmt_sa(d_out)} - {_fmt_sa(d_back)} = +{_fmt_sa(disp_net)}\text{{ m}}\\"
        rf"\vec{{v}}_{{\text{{avg}}}} = \frac{{\Delta \vec{{x}}}}{{\Delta t}} = \frac{{{_fmt_sa(disp_net)}}}{{{_fmt_sa(t_sec)}}} = {_fmt_sa(avg_velocity)}\text{{ m·s}}^{{-1}}\text{{ North}}"
    )
    
    return {
        "id": f"vec_04_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "04_speed_vs_velocity_1d_average",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"Average speed = {_fmt_sa(avg_speed)} m·s⁻¹; Average velocity = {_fmt_sa(avg_velocity)} m·s⁻¹ North",
        "sample_answer": sample_answer,
        "marks": 5,
        "misconception_tags": ["confused_speed_and_velocity", "omitted_direction_in_velocity"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_spd_f", "desc": "Formula: average speed = total distance / delta t", "marks": 1, "editable": True},
                {"id": "mp_spd_a", "desc": f"Average speed = {_fmt_sa(avg_speed)} m·s⁻¹", "marks": 1, "editable": True},
                {"id": "mp_vel_f", "desc": "Formula: average velocity = net displacement / delta t", "marks": 1, "editable": True},
                {"id": "mp_vel_sub", "desc": "Substitution of net displacement and time", "marks": 1, "editable": True},
                {"id": "mp_vel_a", "desc": f"Average velocity = {_fmt_sa(avg_velocity)} m·s⁻¹ North", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_direction_in_velocity", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Average speed uses total distance. Average velocity uses net displacement.",
            "2_concept": "Speed = distance / time. Velocity = displacement / time with direction.",
            "3_breakdown": f"Distance = {dist_total} m, so speed = {dist_total}/{t_sec} = {_fmt_sa(avg_speed)} m·s⁻¹. Displacement = {disp_net} m North, so velocity = {disp_net}/{t_sec} = {_fmt_sa(avg_velocity)} m·s⁻¹ North.",
        },
    }


def build_05_mass_vs_weight_distinction(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Differentiate between scalar mass (kg) and vector weight (N downward) on Earth and Moon."""
    r = _rng(seed)
    
    mass_kg = r.randint(45, 95)
    g_earth = 9.8
    w_earth = round(mass_kg * g_earth, 1)
    
    g_moon = 1.63 # m/s^2 on moon
    w_moon = round(mass_kg * g_moon, 1)
    
    prompt = (
        f"An astronaut has a mass of {_fmt_sa(mass_kg)} kg on Earth.\n"
        f"1. State whether mass is a scalar or a vector quantity.\n"
        f"2. Taking g_Earth = 9,8 m·s⁻², calculate the astronaut's weight on Earth, specifying both magnitude and direction.\n"
        f"3. On the Moon, the gravitational acceleration is 1,63 m·s⁻². State the astronaut's mass on the Moon, and calculate their weight on the Moon."
    )
    
    sample_answer = (
        f"1. Mass is a scalar quantity (it possesses only magnitude and no direction).\n"
        rf"2. \vec{{w}}_{{\text{{Earth}}}} = m \vec{{g}} = ({_fmt_sa(mass_kg)})(9{{,}}8) = {_fmt_sa(w_earth)}\text{{ N downwards (towards Earth's centre)}}\\"
        f"3. Mass on the Moon = {_fmt_sa(mass_kg)} kg (mass remains constant everywhere).\n"
        rf"\vec{{w}}_{{\text{{Moon}}}} = m g_{{\text{{Moon}}}} = ({_fmt_sa(mass_kg)})(1{{,}}63) = {_fmt_sa(w_moon)}\text{{ N downwards}}"
    )
    
    return {
        "id": f"vec_05_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "05_mass_vs_weight_distinction",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"Mass is scalar; Weight on Earth = {_fmt_sa(w_earth)} N downwards; Mass on Moon = {_fmt_sa(mass_kg)} kg; Weight on Moon = {_fmt_sa(w_moon)} N downwards",
        "sample_answer": sample_answer,
        "marks": 5,
        "misconception_tags": ["confused_mass_and_weight", "thought_mass_changes_on_moon"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Identified mass as scalar", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Weight on Earth calculation: w = mg = {_fmt_sa(w_earth)} N", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Specified downward direction for weight on Earth", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Correct constant mass on Moon: {_fmt_sa(mass_kg)} kg", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Weight on Moon = {_fmt_sa(w_moon)} N downwards", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_direction_for_weight", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Mass measures the amount of matter and never changes. Weight is the gravitational pull force and depends on g.",
            "2_concept": "Weight w = m * g (vector directed downwards towards planetary centre).",
            "3_breakdown": f"Earth weight = {mass_kg} * 9,8 = {_fmt_sa(w_earth)} N down. Moon mass = {mass_kg} kg; Moon weight = {mass_kg} * 1,63 = {_fmt_sa(w_moon)} N down.",
        },
    }


def build_06_vector_arrow_representation_and_scale(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Translate between physical vector magnitudes and arrow lengths using a defined scale."""
    r = _rng(seed)
    
    scale_cm = 1
    scale_unit = r.choice([2, 5, 10, 20]) # 1 cm represents scale_unit N
    length_cm = r.randint(4, 9)
    force_val = length_cm * scale_unit
    
    direction = r.choice(["due East", "due North", "due West", "due South"])
    
    # Second question: convert a given force to arrow length
    force2_val = r.choice([scale_unit * 3, scale_unit * 7, scale_unit * 11])
    length2_cm = force2_val // scale_unit
    
    prompt = (
        f"A physics scale drawing uses the scale: 1 cm represents {_fmt_sa(scale_unit)} N.\n"
        f"1. Determine the force represented by an arrow of length {_fmt_sa(length_cm)} cm pointing {direction}.\n"
        f"2. Calculate the length in centimetres of an arrow required to represent a force of {_fmt_sa(force2_val)} N using the same scale."
    )
    
    v_num = _fmt_sa(force2_val)
    v_den = _fmt_sa(scale_unit)
    v_ans = _fmt_sa(length2_cm)
    sample_answer = (
        f"1. Force = arrow length × scale factor = {_fmt_sa(length_cm)} cm × {_fmt_sa(scale_unit)} N·cm⁻¹ = {_fmt_sa(force_val)} N {direction}\n"
        rf"2. \text{{Arrow length}} = \frac{{{v_num}\text{{ N}}}}{{{v_den}\text{{ N\cdot cm}}^{{-1}}}} = {v_ans}\text{{ cm}}"
    )
    
    return {
        "id": f"vec_06_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "06_vector_arrow_representation_and_scale",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"Force = {_fmt_sa(force_val)} N {direction}; Arrow length = {_fmt_sa(length2_cm)} cm",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["inverted_scale_conversion", "omitted_direction_in_force_answer"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Force magnitude: {_fmt_sa(force_val)} N", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Force direction included: {direction}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculated arrow length: {_fmt_sa(length2_cm)} cm", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": f"Each 1 cm represents {scale_unit} N of force.",
            "2_concept": "Multiply centimetres by scale factor to find Newtons; divide Newtons by scale factor to find centimetres.",
            "3_breakdown": f"{length_cm} cm × {scale_unit} N/cm = {force_val} N. {force2_val} N / {scale_unit} N/cm = {length2_cm} cm.",
        },
    }


def build_07_vector_compass_direction_conventions(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Convert between compass direction descriptions (e.g. 35° North of East vs E 35° N vs N 55° E)."""
    r = _rng(seed)
    
    angle = r.choice([25, 30, 35, 40, 50, 55, 65, 70])
    comp_angle = 90 - angle
    
    base_dirs = [
        ("East", "North", "E", "N", "North of East"),
        ("West", "North", "W", "N", "North of West"),
        ("East", "South", "E", "S", "South of East"),
        ("West", "South", "W", "S", "South of West"),
    ]
    ref_main, ref_sub, code_main, code_sub, phrase = r.choice(base_dirs)
    
    mag = r.randint(15, 85)
    
    prompt = (
        f"A force vector of magnitude {_fmt_sa(mag)} N is directed at an angle of {_fmt_sa(angle)}° {phrase}.\n"
        f"1. Write down this direction using standard compass notation starting from {ref_main} (e.g. {code_main} θ° {code_sub}).\n"
        f"2. Write down the equivalent direction measured from {ref_sub} (e.g. {code_sub} α° {code_main})."
    )
    
    ans1 = f"{code_main} {angle}° {code_sub}"
    ans2 = f"{code_sub} {comp_angle}° {code_main}"
    
    sample_answer = (
        f"1. Direction from {ref_main}: {ans1}\n"
        f"2. Equivalent complementary direction from {ref_sub}: 90° - {angle}° = {comp_angle}°, so {ans2}."
    )
    
    return {
        "id": f"vec_07_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "07_vector_compass_direction_conventions",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"1. {ans1}; 2. {ans2}",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["confused_compass_reference_angles", "subtracted_from_180_instead_of_90"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct notation from main axis: {ans1}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Complementary angle calculation: 90° - {angle}° = {comp_angle}°", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct complementary notation: {ans2}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": f"'{phrase}' means start pointing {ref_main} and rotate {angle}° towards {ref_sub}.",
            "2_concept": "The two cardinal directions are 90° apart, so the angle from the other direction is 90° - angle.",
            "3_breakdown": f"Starting at {ref_main}: {ans1}. Starting at {ref_sub}: 90 - {angle} = {comp_angle}°, so {ans2}.",
        },
    }


def build_08_vector_three_figure_bearing(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Convert compass directions to standard 3-figure bearings (000° to 360° clockwise from North)."""
    r = _rng(seed)
    
    quadrant = r.choice([1, 2, 3, 4])
    angle = r.choice([20, 30, 45, 60, 75])
    
    if quadrant == 1:
        # N theta E
        bearing = angle
        desc = f"{angle}° East of North (N {angle}° E)"
        calc_note = f"In the first quadrant, bearing = {angle}° = {bearing:03d}°."
    elif quadrant == 2:
        # E theta S or S alpha E
        bearing = 90 + angle
        desc = f"{angle}° South of East (E {angle}° S)"
        calc_note = f"Start at East (090°) and rotate {angle}° clockwise: 90° + {angle}° = {bearing:03d}°."
    elif quadrant == 3:
        # S theta W
        bearing = 180 + angle
        desc = f"{angle}° West of South (S {angle}° W)"
        calc_note = f"Start at South (180°) and rotate {angle}° clockwise: 180° + {angle}° = {bearing:03d}°."
    else:
        # W theta N
        bearing = 270 + angle
        desc = f"{angle}° North of West (W {angle}° N)"
        calc_note = f"Start at West (270°) and rotate {angle}° clockwise: 270° + {angle}° = {bearing:03d}°."
        
    bearing_str = f"{bearing:03d}°"
    
    prompt = (
        f"Define what is meant by a 'bearing' in vector navigation.\n"
        f"Then convert the following compass direction into a standard three-figure bearing: {desc}."
    )
    
    sample_answer = (
        f"1. Definition: A bearing is a navigational direction specified as an angle measured clockwise from true North (000° to 360°), written with three digits.\n"
        f"2. Calculation: {calc_note}\n"
        f"Final bearing = {bearing_str}"
    )
    
    return {
        "id": f"vec_08_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "08_vector_three_figure_bearing",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"Bearing = {bearing_str}",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["measured_counter_clockwise", "omitted_leading_zero_in_bearing"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_def", "desc": "Definition: angle clockwise from North (000° to 360°)", "marks": 1, "editable": True},
                {"id": "mp_calc", "desc": f"Correct angle addition/subtraction: {calc_note}", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"Three-figure bearing format: {bearing_str}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_leading_zero", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Bearings are always measured CLOCKWISE starting from North (000°).",
            "2_concept": "North is 000°, East is 090°, South is 180°, West is 270°.",
            "3_breakdown": calc_note,
        },
    }


def build_09_equality_and_negative_vectors(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Test conditions for equality of vectors and negative vectors."""
    r = _rng(seed)
    
    force_val = r.choice([25, 40, 60, 100])
    
    prompt = (
        f"Two forces are given: Force A = {_fmt_sa(force_val)} N directed upwards, and Force B = {_fmt_sa(force_val)} N directed downwards.\n"
        f"1. State the two conditions required for two vectors to be equal.\n"
        f"2. Are Force A and Force B equal? Justify your answer.\n"
        f"3. Taking the upward direction as the reference positive direction (+), express Force B in terms of Force A and state its algebraic value."
    )
    
    sample_answer = (
        f"1. Two vectors are equal if and only if they have the same magnitude AND the same direction.\n"
        f"2. No, Force A and Force B are NOT equal. Although they have identical magnitudes ({_fmt_sa(force_val)} N), they act in opposite directions.\n"
        rf"3. Force B is the negative vector of Force A: \vec{{F}}_B = -\vec{{F}}_A = -{_fmt_sa(force_val)}\text{{ N}}."
    )
    
    return {
        "id": f"vec_09_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "09_equality_and_negative_vectors",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"Vectors are not equal (opposite directions); Force B = -Force A = -{_fmt_sa(force_val)} N",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["claimed_equal_due_to_same_magnitude", "omitted_negative_sign_for_opposite_direction"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_cond", "desc": "Stated two conditions: same magnitude and same direction", "marks": 1, "editable": True},
                {"id": "mp_judge", "desc": "Concluded not equal", "marks": 1, "editable": True},
                {"id": "mp_just", "desc": "Justified: directions are opposite", "marks": 1, "editable": True},
                {"id": "mp_neg", "desc": f"Expressed as negative vector: F_B = -F_A = -{_fmt_sa(force_val)} N", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Do Force A and Force B point the same way?",
            "2_concept": "Equal vectors must share BOTH magnitude and direction. A negative vector points in the exact opposite direction.",
            "3_breakdown": f"Force B points opposite to Force A, so F_B = -F_A = -{force_val} N.",
        },
    }


def build_10_collinear_vectors_same_direction_addition(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """1D Collinear addition of vectors acting in the same direction."""
    r = _rng(seed)
    
    f1 = r.randint(25, 75)
    f2 = r.randint(30, 80)
    f_total = f1 + f2
    direction = r.choice(["to the right", "due East", "forwards"])
    
    prompt = (
        f"Two workers push a heavy storage crate across a smooth floor in the same direction. "
        f"Worker 1 exerts a horizontal force of {_fmt_sa(f1)} N {direction}, while Worker 2 exerts a horizontal "
        f"force of {_fmt_sa(f2)} N {direction}.\n"
        f"Calculate the resultant force acting on the crate, specifying both magnitude and direction."
    )
    
    sample_answer = (
        f"Taking {direction} as the positive reference direction (+):\n"
        rf"\vec{{F}}_{{\text{{net}}}} = \vec{{F}}_1 + \vec{{F}}_2 = (+{_fmt_sa(f1)}) + (+{_fmt_sa(f2)}) = +{_fmt_sa(f_total)}\text{{ N}}\\"
        f"Resultant force = {_fmt_sa(f_total)} N {direction}."
    )
    
    return {
        "id": f"vec_10_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "10_collinear_vectors_same_direction_addition",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 3,
        "prompt": prompt,
        "ideal_answer": f"{_fmt_sa(f_total)} N {direction}",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["omitted_direction_in_resultant", "subtracted_same_direction_forces"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_sub", "desc": f"Addition of forces: {_fmt_sa(f1)} + {_fmt_sa(f2)}", "marks": 1, "editable": True},
                {"id": "mp_mag", "desc": f"Magnitude = {_fmt_sa(f_total)} N", "marks": 1, "editable": True},
                {"id": "mp_dir", "desc": f"Direction specified: {direction}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_direction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "When two forces act in the same straight line in the same direction, you simply add their magnitudes.",
            "2_concept": "F_net = F1 + F2 in the common direction.",
            "3_breakdown": f"F_net = {f1} + {f2} = {f_total} N {direction}.",
        },
    }


def build_11_collinear_vectors_opposite_direction_subtraction(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """1D Collinear vector subtraction using opposite directions and sign conventions."""
    r = _rng(seed)
    
    f_right = r.randint(60, 140)
    f_left = r.randint(20, f_right - 15) # ensures right is larger or flip
    if r.random() < 0.5:
        f_right, f_left = f_left, f_right
        
    net_val = f_right - f_left
    net_dir = "to the right" if net_val > 0 else "to the left"
    mag = abs(net_val)
    
    prompt = (
        f"In a game of tug-of-war, Team A pulls with a force of {_fmt_sa(f_right)} N to the right, "
        f"while Team B pulls with a force of {_fmt_sa(f_left)} N to the left.\n"
        f"1. Choose a reference positive direction and write down the algebraic value of each force.\n"
        f"2. Calculate the overall resultant force on the rope, stating both magnitude and direction."
    )
    
    sample_answer = (
        f"1. Choose 'to the right' as positive (+):\n"
        f"   Force A = +{_fmt_sa(f_right)} N\n"
        f"   Force B = -{_fmt_sa(f_left)} N\n"
        rf"2. F_{{\text{{net}}}} = (+{_fmt_sa(f_right)}) + (-{_fmt_sa(f_left)}) = {'+' if net_val > 0 else '-'}{_fmt_sa(mag)}\text{{ N}}\\"
        f"Resultant force = {_fmt_sa(mag)} N {net_dir}."
    )
    
    return {
        "id": f"vec_11_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "11_collinear_vectors_opposite_direction_subtraction",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"F_net = {_fmt_sa(mag)} N {net_dir}",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["added_opposing_forces", "omitted_direction_in_resultant"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_ref", "desc": "Stated reference positive direction", "marks": 1, "editable": True},
                {"id": "mp_signs", "desc": "Assigned correct positive and negative signs", "marks": 1, "editable": True},
                {"id": "mp_mag", "desc": f"Correct magnitude: {_fmt_sa(mag)} N", "marks": 1, "editable": True},
                {"id": "mp_dir", "desc": f"Correct direction: {net_dir}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_direction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Forces in opposite directions oppose each other; subtract the smaller from the larger.",
            "2_concept": "F_net = F_right - F_left. The direction of F_net is in the direction of the larger force.",
            "3_breakdown": f"Net force = |{f_right} - {f_left}| = {mag} N in the direction of the larger force ({net_dir}).",
        },
    }


def build_12_collinear_multi_stage_displacements_1d(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Multi-stage 1D displacements with multiple direction reversals."""
    r = _rng(seed)
    
    s1 = r.randint(12, 35) # East
    s2 = r.randint(5, 20)  # West
    s3 = r.randint(8, 25)  # East
    
    dist_total = s1 + s2 + s3
    disp_net = s1 - s2 + s3
    
    prompt = (
        f"A delivery drone flies along a straight east-west test corridor:\n"
        f"- Stage 1: Flies {_fmt_sa(s1)} m East.\n"
        f"- Stage 2: Reverses and flies {_fmt_sa(s2)} m West.\n"
        f"- Stage 3: Turns again and flies {_fmt_sa(s3)} m East.\n\n"
        f"1. Calculate the total distance flown by the drone.\n"
        f"2. Calculate the overall resultant displacement of the drone from its starting position."
    )
    
    sample_answer = (
        f"1. Total distance = s_1 + s_2 + s_3 = {_fmt_sa(s1)} + {_fmt_sa(s2)} + {_fmt_sa(s3)} = {_fmt_sa(dist_total)} m\n"
        f"2. Taking East as positive (+):\n"
        rf"\Delta x = (+{_fmt_sa(s1)}) + (-{_fmt_sa(s2)}) + (+{_fmt_sa(s3)}) = +{_fmt_sa(disp_net)}\text{{ m}}\\"
        f"Resultant displacement = {_fmt_sa(disp_net)} m due East."
    )
    
    return {
        "id": f"vec_12_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "12_collinear_multi_stage_displacements_1d",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"Distance = {_fmt_sa(dist_total)} m; Displacement = {_fmt_sa(disp_net)} m East",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["confused_distance_and_displacement", "sign_error_in_reversal"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_dist_sub", "desc": "Summing absolute segments for distance", "marks": 1, "editable": True},
                {"id": "mp_dist_ans", "desc": f"Distance = {_fmt_sa(dist_total)} m", "marks": 1, "editable": True},
                {"id": "mp_disp_sub", "desc": "Algebraic sum with signs: (+s1) - s2 + (+s3)", "marks": 1, "editable": True},
                {"id": "mp_disp_ans", "desc": f"Displacement = {_fmt_sa(disp_net)} m East", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_direction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Distance adds every metre travelled. Displacement keeps track of position using plus and minus signs.",
            "2_concept": "Displacement = (+s1) + (-s2) + (+s3) with East as positive.",
            "3_breakdown": f"Distance = {s1}+{s2}+{s3} = {dist_total} m. Displacement = {s1}-{s2}+{s3} = {disp_net} m East.",
        },
    }


def build_13_collinear_net_force_horizontal(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Net horizontal force with applied forces and opposing friction."""
    r = _rng(seed)
    
    f_pull1 = r.randint(40, 90)
    f_pull2 = r.randint(30, 80)
    f_friction = r.randint(20, 60)
    
    f_applied_total = f_pull1 + f_pull2
    f_net = f_applied_total - f_friction
    
    prompt = (
        f"A heavy crate on a rough warehouse floor is pulled to the right by two ropes. "
        f"Rope 1 exerts a force of {_fmt_sa(f_pull1)} N to the right, and Rope 2 exerts a force of {_fmt_sa(f_pull2)} N to the right. "
        f"A frictional force of {_fmt_sa(f_friction)} N acts to the left.\n"
        f"1. Calculate the total applied pulling force.\n"
        f"2. Calculate the resultant horizontal force (F_net) acting on the crate, stating both magnitude and direction."
    )
    
    sample_answer = (
        rf"1. F_{{\text{{app}}}} = {_fmt_sa(f_pull1)} + {_fmt_sa(f_pull2)} = {_fmt_sa(f_applied_total)}\text{{ N to the right}}\\"
        f"2. Taking right as positive (+):\n"
        rf"F_{{\text{{net}}}} = (+{_fmt_sa(f_applied_total)}) + (-{_fmt_sa(f_friction)}) = +{_fmt_sa(f_net)}\text{{ N}}\\"
        f"Net force = {_fmt_sa(f_net)} N to the right."
    )
    
    return {
        "id": f"vec_13_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "13_collinear_net_force_horizontal",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"F_net = {_fmt_sa(f_net)} N to the right",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["added_friction_to_pulling_force", "omitted_direction_in_fnet"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Total applied pulling force = {_fmt_sa(f_applied_total)} N", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Net force formula: F_net = F_app - f_friction", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Net force magnitude = {_fmt_sa(f_net)} N", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Direction: to the right", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_direction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Add the two pulling forces together first because they act in the same direction.",
            "2_concept": "Friction opposes motion, so subtract friction from the total forward force.",
            "3_breakdown": f"Pulling = {f_pull1} + {f_pull2} = {f_applied_total} N. F_net = {f_applied_total} - {f_friction} = {f_net} N to the right.",
        },
    }


def build_14_collinear_net_force_vertical(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Net vertical force calculation (lift tension vs downward weight)."""
    r = _rng(seed)
    
    mass_kg = r.randint(15, 60)
    g = 9.8
    weight_n = round(mass_kg * g, 1)
    
    # Tension greater than weight (accelerating upward) or less (accelerating downward)
    upward = (r.random() < 0.6)
    delta_f = r.randint(20, 80)
    tension_n = round(weight_n + (delta_f if upward else -delta_f), 1)
    
    f_net = round(abs(tension_n - weight_n), 1)
    net_dir = "vertically upwards" if tension_n > weight_n else "vertically downwards"
    
    prompt = (
        f"A package of mass {_fmt_sa(mass_kg)} kg is lifted by a crane cable that exerts an upward tension force of "
        f"{_fmt_sa(tension_n)} N. Taking g = 9,8 m·s⁻²:\n"
        f"1. Calculate the weight of the package (Fg).\n"
        f"2. Calculate the resultant vertical force (F_net) acting on the package, stating both magnitude and direction."
    )
    
    sample_answer = (
        rf"1. F_g = m g = ({_fmt_sa(mass_kg)})(9{{,}}8) = {_fmt_sa(weight_n)}\text{{ N downwards}}\\"
        f"2. Taking upwards as positive (+):\n"
        rf"F_{{\text{{net}}}} = T - F_g = {_fmt_sa(tension_n)} - {_fmt_sa(weight_n)} = {'+' if tension_n > weight_n else '-'}{_fmt_sa(f_net)}\text{{ N}}\\"
        f"Net vertical force = {_fmt_sa(f_net)} N {net_dir}."
    )
    
    return {
        "id": f"vec_14_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "14_collinear_net_force_vertical",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"F_g = {_fmt_sa(weight_n)} N down; F_net = {_fmt_sa(f_net)} N {net_dir}",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["confused_mass_with_weight", "omitted_direction_in_fnet"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_fg_f", "desc": "Formula F_g = mg", "marks": 1, "editable": True},
                {"id": "mp_fg_a", "desc": f"Weight = {_fmt_sa(weight_n)} N downwards", "marks": 1, "editable": True},
                {"id": "mp_fnet_mag", "desc": f"Magnitude of net force = {_fmt_sa(f_net)} N", "marks": 1, "editable": True},
                {"id": "mp_fnet_dir", "desc": f"Direction of net force: {net_dir}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_direction", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "First find the downward weight force: F_g = mass × 9,8.",
            "2_concept": "The cable pulls up (T) while gravity pulls down (Fg). F_net = T - Fg.",
            "3_breakdown": f"Weight = {mass_kg} × 9,8 = {_fmt_sa(weight_n)} N. F_net = |{tension_n} - {_fmt_sa(weight_n)}| = {_fmt_sa(f_net)} N {net_dir}.",
        },
    }


def build_15_resultant_vector_concept_and_definition(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Define resultant vector and describe how it replaces multiple concurrent vectors."""
    r = _rng(seed)
    
    prompt = (
        f"1. State the official curriculum definition of the 'resultant vector'.\n"
        f"2. A box is acted upon by two forces: 15 N East and 20 N North. "
        f"Explain what it means in practice to replace these two forces with their resultant vector."
    )
    
    sample_answer = (
        "1. Definition: The resultant vector is the single vector whose effect is the same as the individual vectors acting together.\n"
        "2. Practical Meaning: If the two original forces (15 N East and 20 N North) are removed and replaced by the single resultant vector, "
        "the box will experience exactly the same net acceleration, physical motion, and mechanical outcome as when both original forces acted simultaneously."
    )
    
    return {
        "id": f"vec_15_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "15_resultant_vector_concept_and_definition",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": "The single vector whose effect is the same as the individual vectors acting together.",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["imprecise_definition_of_resultant", "thought_resultant_is_just_an_average"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: single vector having the same effect as all original vectors combined", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Explanation: produces the identical physical effect / acceleration", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "What does a single resultant do compared to the multiple original vectors?",
            "2_concept": "The resultant is the single vector whose effect is the same as the individual vectors acting together.",
            "3_breakdown": "Define: single vector with same effect. Meaning: produces identical net acceleration.",
        },
    }


def build_16_tail_to_head_vector_addition_concept(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Explain and sequence the tail-to-head (head-to-tail) graphical vector addition method."""
    r = _rng(seed)
    
    v1_val = r.randint(20, 50)
    v2_val = r.randint(20, 50)
    
    prompt = (
        f"Describe step-by-step the 'tail-to-head' method of graphical vector addition to find the resultant "
        f"of two vectors: Vector A ({_fmt_sa(v1_val)} N East) and Vector B ({_fmt_sa(v2_val)} N North). "
        f"In your response, explicitly state where the resultant arrow starts and ends."
    )
    
    sample_answer = (
        "Head-to-Tail (Tail-to-Head) Method Steps:\n"
        "1. Choose a suitable scale (e.g. 1 cm = 10 N) and establish a reference direction frame (e.g. compass directions).\n"
        f"2. Draw Vector A as an arrow pointing East with length corresponding to {_fmt_sa(v1_val)} N, marking its tail (start) and head (arrowhead).\n"
        f"3. From the HEAD of Vector A, draw Vector B pointing North with length corresponding to {_fmt_sa(v2_val)} N.\n"
        "4. Draw the RESULTANT vector as an arrow starting at the TAIL of the first vector (Vector A) and ending at the HEAD of the second vector (Vector B).\n"
        "5. Measure the length of the resultant arrow with a ruler to find magnitude (using the scale), and measure the angle with a protractor to find direction."
    )
    
    return {
        "id": f"vec_16_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "16_tail_to_head_vector_addition_concept",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": "Connect tail of second vector to head of first; resultant runs from tail of first to head of last.",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["reversed_resultant_arrow_direction", "joined_tails_instead_of_tail_to_head"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Scale and first vector drawn accurately", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Second vector drawn starting from head of first", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Resultant starts at tail of first and ends at head of second", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Measurement of magnitude (ruler) and angle (protractor)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Where do you place the tail of the second vector?",
            "2_concept": "Place the tail of Vector B at the head of Vector A. The resultant connects tail of A to head of B.",
            "3_breakdown": "Resultant arrow always points from the origin (tail of 1st) to the final destination (head of last).",
        },
    }


def build_17_parallelogram_law_vector_addition_concept(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Understand and interpret the parallelogram method of vector addition for concurrent vectors."""
    r = _rng(seed)
    
    prompt = (
        "Explain how the 'Parallelogram Method' is used to determine the resultant of two concurrent vectors "
        "acting at the same point.\n"
        "1. How are the two given vectors positioned relative to each other?\n"
        "2. How is the parallelogram constructed?\n"
        "3. Which feature of the parallelogram represents the resultant vector?"
    )
    
    sample_answer = (
        "1. Positioning: Both vectors are drawn starting from the SAME common origin point (tail-to-tail).\n"
        "2. Parallelogram Construction: Complete the parallelogram by drawing parallel lines from the head of each vector parallel to the other vector.\n"
        "3. Resultant: The resultant vector is represented by the DIAGONAL of the parallelogram drawn from the common origin (tails) to the opposite intersecting vertex."
    )
    
    return {
        "id": f"vec_17_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "17_parallelogram_law_vector_addition_concept",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": "Draw tail-to-tail, complete parallelogram, resultant is the diagonal from the common origin.",
        "sample_answer": sample_answer,
        "marks": 3,
        "misconception_tags": ["confused_diagonal_endpoints", "confused_parallelogram_with_triangle_method"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Vectors drawn tail-to-tail from common point", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Completion of parallelogram with parallel sides", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Resultant is diagonal from common origin to opposite vertex", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "In the parallelogram method, vectors start at the same point (tail-to-tail).",
            "2_concept": "Draw the two vectors tail-to-tail, complete the 4-sided figure, and draw the diagonal.",
            "3_breakdown": "The diagonal starting from the common tail represents the resultant.",
        },
    }


def build_18_perpendicular_vectors_pythagoras_magnitude(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate resultant magnitude of two perpendicular vectors using Pythagoras theorem."""
    r = _rng(seed)
    
    rx = r.randint(12, 45)
    ry = r.randint(12, 45)
    r_mag = round(math.hypot(rx, ry), 2)
    
    prompt = (
        f"Two perpendicular forces act on a body: a horizontal force F_x = {_fmt_sa(rx)} N to the right, "
        f"and a vertical force F_y = {_fmt_sa(ry)} N upwards.\n"
        f"Use the Theorem of Pythagoras to calculate the magnitude of the resultant force acting on the body."
    )
    
    calc_latex = rf"R = \sqrt{{F_x^2 + F_y^2}} = \sqrt{{({_fmt_sa(rx)})^2 + ({_fmt_sa(ry)})^2}} = \sqrt{{{rx**2 + ry**2}}} = {_fmt_sa(r_mag)}\text{{ N}}"
    
    return {
        "id": f"vec_18_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "18_perpendicular_vectors_pythagoras_magnitude",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"{_fmt_sa(r_mag)} N",
        "sample_answer": calc_latex,
        "marks": 3,
        "misconception_tags": ["omitted_square_root_in_pythagoras", "added_vectors_linearly_instead_of_pythagoras"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_f", "desc": "Formula R^2 = Rx^2 + Ry^2", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": f"Substitution: sqrt(({rx})^2 + ({ry})^2)", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"Final magnitude: {_fmt_sa(r_mag)} N", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Because the vectors are perpendicular (at 90°), they form the legs of a right-angled triangle.",
            "2_concept": "Apply Pythagoras: R = sqrt(Fx^2 + Fy^2).",
            "3_breakdown": f"R = sqrt({rx}^2 + {ry}^2) = sqrt({rx**2 + ry**2}) = {_fmt_sa(r_mag)} N.",
        },
    }


def build_19_perpendicular_displacements_pythagoras_east_north(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate resultant displacement magnitude and total distance for East then North journey."""
    r = _rng(seed)
    
    d_east = r.randint(15, 60) # km
    d_north = r.randint(15, 60) # km
    d_total = d_east + d_north
    r_disp = round(math.hypot(d_east, d_north), 2)
    
    prompt = (
        f"A safari tourist vehicle drives {_fmt_sa(d_east)} km due East and then {_fmt_sa(d_north)} km due North.\n"
        f"1. Calculate the total distance travelled by the vehicle.\n"
        f"2. Calculate the magnitude of the resultant displacement of the vehicle from its starting point."
    )
    
    sample_answer = (
        rf"1. \text{{Total distance}} = {_fmt_sa(d_east)} + {_fmt_sa(d_north)} = {_fmt_sa(d_total)}\text{{ km}}\\"
        rf"2. \Delta x = \sqrt{{d_{{\text{{East}}}}^2 + d_{{\text{{North}}}}^2}} = \sqrt{{({_fmt_sa(d_east)})^2 + ({_fmt_sa(d_north)})^2}} = {_fmt_sa(r_disp)}\text{{ km}}"
    )
    
    return {
        "id": f"vec_19_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "19_perpendicular_displacements_pythagoras_east_north",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"Distance = {_fmt_sa(d_total)} km; Displacement magnitude = {_fmt_sa(r_disp)} km",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["confused_distance_and_displacement", "omitted_square_in_pythagoras"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_dist_sub", "desc": f"Distance addition: {d_east} + {d_north}", "marks": 1, "editable": True},
                {"id": "mp_dist_ans", "desc": f"Total distance = {_fmt_sa(d_total)} km", "marks": 1, "editable": True},
                {"id": "mp_disp_f", "desc": "Pythagoras formula: R = sqrt(dx^2 + dy^2)", "marks": 1, "editable": True},
                {"id": "mp_disp_ans", "desc": f"Displacement magnitude = {_fmt_sa(r_disp)} km", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Distance is simple scalar addition. Displacement magnitude requires Pythagoras.",
            "2_concept": "Displacement = hypotenuse of right triangle with legs d_East and d_North.",
            "3_breakdown": f"Distance = {d_east} + {d_north} = {d_total} km. Displacement = sqrt({d_east}^2 + {d_north}^2) = {_fmt_sa(r_disp)} km.",
        },
    }


def build_20_perpendicular_vectors_trig_direction_angle(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate the direction angle of perpendicular resultant using tan(theta) = Ry / Rx."""
    r = _rng(seed)
    
    rx = r.randint(15, 50)
    ry = r.randint(15, 50)
    theta_deg = round(math.degrees(math.atan2(ry, rx)), 1)
    
    prompt = (
        f"A resultant force vector is composed of two perpendicular components: F_x = {_fmt_sa(rx)} N (East) "
        f"and F_y = {_fmt_sa(ry)} N (North).\n"
        f"Use trigonometry to calculate the angle θ that the resultant force makes with the horizontal (East) axis."
    )
    
    calc_latex = (
        rf"\tan\theta = \frac{{F_y}}{{F_x}} = \frac{{{_fmt_sa(ry)}}}{{{_fmt_sa(rx)}}} = {_fmt_sa(round(ry/rx, 4), 4)}\\"
        rf"\theta = \arctan\left(\frac{{{_fmt_sa(ry)}}}{{{_fmt_sa(rx)}}}\right) = {_fmt_sa(theta_deg)}^\circ\text{{ North of East}}"
    )
    
    return {
        "id": f"vec_20_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "20_perpendicular_vectors_trig_direction_angle",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"θ = {_fmt_sa(theta_deg)}° North of East",
        "sample_answer": calc_latex,
        "marks": 3,
        "misconception_tags": ["inverted_tangent_ratio", "used_sin_or_cos_without_hypotenuse"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_f", "desc": "Formula tan(theta) = Fy / Fx (opposite / adjacent)", "marks": 1, "editable": True},
                {"id": "mp_sub", "desc": f"Substitution: tan(theta) = {ry} / {rx}", "marks": 1, "editable": True},
                {"id": "mp_ans", "desc": f"Calculated angle: {_fmt_sa(theta_deg)}° North of East", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_reference_axis", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "In a right triangle, tan(θ) = Opposite / Adjacent.",
            "2_concept": "The vertical component Fy is the opposite side; the horizontal component Fx is the adjacent side.",
            "3_breakdown": f"tan(θ) = {ry}/{rx}. θ = arctan({ry}/{rx}) = {_fmt_sa(theta_deg)}°.",
        },
    }


def build_21_perpendicular_displacements_bearing(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Calculate true 3-figure bearing of resultant perpendicular displacements."""
    r = _rng(seed)
    
    d_east = r.randint(15, 60)
    d_north = r.randint(15, 60)
    
    # Angle from North clockwise towards East is theta_n = arctan(d_east / d_north)
    theta_from_north = round(math.degrees(math.atan2(d_east, d_north)), 1)
    bearing_val = round(theta_from_north)
    bearing_str = f"{bearing_val:03d}°"
    
    r_mag = round(math.hypot(d_east, d_north), 1)
    
    prompt = (
        f"A search helicopter flies {_fmt_sa(d_north)} km due North, then {_fmt_sa(d_east)} km due East.\n"
        f"1. Calculate the magnitude of the helicopter's resultant displacement.\n"
        f"2. Calculate the true three-figure bearing of the helicopter from its takeoff point."
    )
    
    sample_answer = (
        rf"1. R = \sqrt{{({_fmt_sa(d_north)})^2 + ({_fmt_sa(d_east)})^2}} = {_fmt_sa(r_mag)}\text{{ km}}\\"
        rf"2. \text{{Angle clockwise from North: }}\tan\theta = \frac{{d_{{\text{{East}}}}}}{{d_{{\text{{North}}}}}} = \frac{{{_fmt_sa(d_east)}}}{{{_fmt_sa(d_north)}}}\\"
        rf"\theta = \arctan\left(\frac{{{_fmt_sa(d_east)}}}{{{_fmt_sa(d_north)}}}\right) = {_fmt_sa(theta_from_north)}^\circ \approx {bearing_str}\\"
        f"True bearing = {bearing_str}."
    )
    
    return {
        "id": f"vec_21_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "21_perpendicular_displacements_bearing",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": f"Magnitude = {_fmt_sa(r_mag)} km; Bearing = {bearing_str}",
        "sample_answer": sample_answer,
        "marks": 4,
        "misconception_tags": ["measured_bearing_from_east_instead_of_north", "inverted_bearing_tangent_ratio"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_pyth", "desc": f"Pythagoras magnitude = {_fmt_sa(r_mag)} km", "marks": 2, "editable": True},
                {"id": "mp_trig", "desc": "Trigonometric equation from North: tan(theta) = d_East / d_North", "marks": 1, "editable": True},
                {"id": "mp_bearing", "desc": f"Three-figure bearing = {bearing_str}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_leading_zero", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Bearings start at North (000°). Measure the angle clockwise towards East.",
            "2_concept": "tan(bearing) = Opposite (East) / Adjacent (North).",
            "3_breakdown": f"R = sqrt({d_north}^2 + {d_east}^2) = {_fmt_sa(r_mag)} km. Bearing = arctan({d_east}/{d_north}) = {bearing_str}.",
        },
    }


def build_22_perpendicular_forces_pythagorean_triple_3_4_5(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Solve resultant force with exact integer 3-4-5 Pythagorean scaling."""
    r = _rng(seed)
    
    k = r.choice([2, 3, 4, 5, 8, 10, 15, 20])
    fx = 3 * k # N East
    fy = 4 * k # N North
    fr = 5 * k # N
    
    theta_deg = round(math.degrees(math.atan2(fy, fx)), 2) # approx 53.13 deg
    
    prompt = (
        f"Two perpendicular forces act on a peg in the ground: a force of {_fmt_sa(fx)} N East and a force of {_fmt_sa(fy)} N North.\n"
        f"1. Calculate the exact magnitude of the resultant force.\n"
        f"2. Calculate the direction of the resultant force as an angle to the East axis."
    )
    
    calc_latex = (
        rf"1. R = \sqrt{{({_fmt_sa(fx)})^2 + ({_fmt_sa(fy)})^2}} = \sqrt{{{fx**2} + {fy**2}}} = \sqrt{{{fr**2}}} = {_fmt_sa(fr)}\text{{ N}}\\"
        rf"2. \tan\theta = \frac{{{_fmt_sa(fy)}}}{{{_fmt_sa(fx)}}} = \frac{{4}}{{3}} \implies \theta = \arctan(1{{,}}333) = {_fmt_sa(theta_deg)}^\circ\text{{ North of East}}"
    )
    
    return {
        "id": f"vec_22_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "22_perpendicular_forces_pythagorean_triple_3_4_5",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"R = {_fmt_sa(fr)} N, θ = {_fmt_sa(theta_deg)}° North of East",
        "sample_answer": calc_latex,
        "marks": 4,
        "misconception_tags": ["arithmetic_error_in_square", "omitted_direction_in_resultant"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_pyth_f", "desc": "Formula R = sqrt(Fx^2 + Fy^2)", "marks": 1, "editable": True},
                {"id": "mp_mag", "desc": f"Exact magnitude R = {_fmt_sa(fr)} N", "marks": 1, "editable": True},
                {"id": "mp_trig", "desc": "Formula tan(theta) = Fy / Fx", "marks": 1, "editable": True},
                {"id": "mp_dir", "desc": f"Direction θ = {_fmt_sa(theta_deg)}° North of East", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "Notice that the ratio of forces is 3:4. This forms a standard 3-4-5 right triangle.",
            "2_concept": "R = sqrt((3k)^2 + (4k)^2) = 5k. Angle is arctan(4/3).",
            "3_breakdown": f"R = sqrt({fx}^2 + {fy}^2) = {fr} N. Angle = arctan({fy}/{fx}) = {_fmt_sa(theta_deg)}°.",
        },
    }


def build_23_perpendicular_forces_pythagorean_triple_5_12_13(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Solve resultant force with exact integer 5-12-13 Pythagorean scaling."""
    r = _rng(seed)
    
    k = r.choice([1, 2, 3, 4, 5, 10])
    fx = 5 * k # N
    fy = 12 * k # N
    fr = 13 * k # N
    
    theta_deg = round(math.degrees(math.atan2(fy, fx)), 2) # approx 67.38 deg
    
    prompt = (
        f"A tethered weather buoy experiences a tidal current force of {_fmt_sa(fx)} N East and a wind force of {_fmt_sa(fy)} N North.\n"
        f"1. Calculate the exact magnitude of the resultant force acting on the buoy.\n"
        f"2. Calculate the direction of the resultant force as an angle relative to the East direction."
    )
    
    calc_latex = (
        rf"1. R = \sqrt{{({_fmt_sa(fx)})^2 + ({_fmt_sa(fy)})^2}} = \sqrt{{{fx**2} + {fy**2}}} = \sqrt{{{fr**2}}} = {_fmt_sa(fr)}\text{{ N}}\\"
        rf"2. \tan\theta = \frac{{{_fmt_sa(fy)}}}{{{_fmt_sa(fx)}}} = \frac{{12}}{{5}} = 2{{,}}4 \implies \theta = \arctan(2{{,}}4) = {_fmt_sa(theta_deg)}^\circ\text{{ North of East}}"
    )
    
    return {
        "id": f"vec_23_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "23_perpendicular_forces_pythagorean_triple_5_12_13",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"R = {_fmt_sa(fr)} N, θ = {_fmt_sa(theta_deg)}° North of East",
        "sample_answer": calc_latex,
        "marks": 4,
        "misconception_tags": ["inverted_tangent_ratio", "rounding_error_in_magnitude"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_f", "desc": "Formula R = sqrt(Fx^2 + Fy^2)", "marks": 1, "editable": True},
                {"id": "mp_mag", "desc": f"Exact magnitude R = {_fmt_sa(fr)} N", "marks": 1, "editable": True},
                {"id": "mp_trig", "desc": "Trigonometric formula tan(theta) = Fy / Fx", "marks": 1, "editable": True},
                {"id": "mp_dir", "desc": f"Direction θ = {_fmt_sa(theta_deg)}° North of East", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "The components 5k and 12k match the 5-12-13 Pythagorean triple.",
            "2_concept": "R = sqrt(5^2 + 12^2) × k = 13k.",
            "3_breakdown": f"R = sqrt({fx}^2 + {fy}^2) = {fr} N. Angle = arctan({fy}/{fx}) = {_fmt_sa(theta_deg)}° North of East.",
        },
    }


def build_24_perpendicular_forces_pythagorean_triple_8_15_17(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Solve resultant force with exact integer 8-15-17 Pythagorean scaling."""
    r = _rng(seed)
    
    k = r.choice([1, 2, 3, 4, 5])
    fx = 8 * k
    fy = 15 * k
    fr = 17 * k
    
    theta_deg = round(math.degrees(math.atan2(fy, fx)), 2) # approx 61.93 deg
    
    prompt = (
        f"Two cables pull a support pylon horizontally with {_fmt_sa(fx)} kN East and {_fmt_sa(fy)} kN North.\n"
        f"1. Determine the magnitude of the resultant pull force on the pylon.\n"
        f"2. Determine the bearing of the resultant force."
    )
    
    bearing_val = round(90 - theta_deg)
    bearing_str = f"{bearing_val:03d}°"
    
    calc_latex = (
        rf"1. R = \sqrt{{({_fmt_sa(fx)})^2 + ({_fmt_sa(fy)})^2}} = \sqrt{{{fx**2} + {fy**2}}} = \sqrt{{{fr**2}}} = {_fmt_sa(fr)}\text{{ kN}}\\"
        rf"2. \theta = \arctan\left(\frac{{{_fmt_sa(fy)}}}{{{_fmt_sa(fx)}}}\right) = {_fmt_sa(theta_deg)}^\circ\text{{ North of East}}\\"
        rf"\text{{Bearing}} = 90^\circ - {_fmt_sa(theta_deg)}^\circ = {bearing_str}"
    )
    
    return {
        "id": f"vec_24_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "24_perpendicular_forces_pythagorean_triple_8_15_17",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": f"R = {_fmt_sa(fr)} kN, Bearing = {bearing_str}",
        "sample_answer": calc_latex,
        "marks": 4,
        "misconception_tags": ["confused_bearing_with_angle_to_horizontal", "wrong_pythagoras_evaluation"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_pyth", "desc": "Pythagoras substitution and evaluation", "marks": 1, "editable": True},
                {"id": "mp_mag", "desc": f"Resultant magnitude = {_fmt_sa(fr)} kN", "marks": 1, "editable": True},
                {"id": "mp_trig", "desc": "Calculation of angle to East", "marks": 1, "editable": True},
                {"id": "mp_bearing", "desc": f"Converted to 3-figure bearing = {bearing_str}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "8-15-17 is an integer Pythagorean triple.",
            "2_concept": "R = sqrt(8^2 + 15^2) * k = 17k. Bearing from North = 90° - θ_East.",
            "3_breakdown": f"R = {fr} kN. Angle to East = {_fmt_sa(theta_deg)}°. Bearing = 90 - {_fmt_sa(theta_deg)} = {bearing_str}.",
        },
    }


def build_25_orthogonal_resultant_with_vector_diagram(seed: Optional[int] = None, mode: str = "compound") -> Dict[str, Any]:
    """Orthogonal resultant calculation accompanied by a seed-varied inline SVG vector diagram."""
    r = _rng(seed)
    
    fx = r.randint(20, 60) # N East
    fy = r.randint(20, 60) # N North
    fr = round(math.hypot(fx, fy), 1)
    theta = round(math.degrees(math.atan2(fy, fx)), 1)
    
    # Scale vector for SVG
    max_f = max(fx, fy)
    scale_factor = 140.0 / max(1, max_f)
    
    vectors_for_svg = [
        {"dx": fx, "dy": 0, "start": (0, 0), "color": "#1e3a8a", "label": f"Fx = {fx} N"},
        {"dx": 0, "dy": fy, "start": (fx, 0), "color": "#047857", "label": f"Fy = {fy} N"},
        {"dx": fx, "dy": fy, "start": (0, 0), "color": "#b91c1c", "label": f"R = {_fmt_sa(fr)} N", "dashed": False, "stroke_width": 3},
    ]
    svg_markup = _vector_svg(
        vectors_for_svg,
        origin=(80, 220),
        scale=scale_factor,
        width=500,
        height=280,
        show_compass=True,
        seed_tag=seed,
    )
    
    prompt = (
        f"Refer to the vector diagram showing two perpendicular force vectors acting in a tail-to-head arrangement: "
        f"a horizontal force F_x = {_fmt_sa(fx)} N East, and a vertical force F_y = {_fmt_sa(fy)} N North.\n"
        f"1. Use the Theorem of Pythagoras to calculate the magnitude of the resultant force R.\n"
        f"2. Use trigonometry to calculate the direction angle θ of the resultant force relative to the East axis."
    )
    
    calc_latex = (
        rf"1. R = \sqrt{{F_x^2 + F_y^2}} = \sqrt{{({_fmt_sa(fx)})^2 + ({_fmt_sa(fy)})^2}} = \sqrt{{{fx**2 + fy**2}}} = {_fmt_sa(fr)}\text{{ N}}\\"
        rf"2. \tan\theta = \frac{{F_y}}{{F_x}} = \frac{{{_fmt_sa(fy)}}}{{{_fmt_sa(fx)}}} = {_fmt_sa(round(fy/fx, 4), 4)}\\"
        rf"\theta = \arctan\left(\frac{{{_fmt_sa(fy)}}}{{{_fmt_sa(fx)}}}\right) = {_fmt_sa(theta)}^\circ\text{{ North of East}}"
    )
    
    return {
        "id": f"vec_25_{r.randint(100000, 999999)}",
        "topic": "Vectors and scalars",
        "subskill": "25_orthogonal_resultant_with_vector_diagram",
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg_markup,
            "diagram_role": "context",
        },
        "prompt": prompt,
        "ideal_answer": f"R = {_fmt_sa(fr)} N, θ = {_fmt_sa(theta)}° North of East",
        "sample_answer": calc_latex,
        "marks": 5,
        "misconception_tags": ["inverted_tangent_ratio", "misread_tail_to_head_diagram"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_pyth_f", "desc": "Pythagoras formula R = sqrt(Fx^2 + Fy^2)", "marks": 1, "editable": True},
                {"id": "mp_pyth_sub", "desc": f"Substitution: sqrt({fx}^2 + {fy}^2)", "marks": 1, "editable": True},
                {"id": "mp_mag", "desc": f"Magnitude R = {_fmt_sa(fr)} N", "marks": 1, "editable": True},
                {"id": "mp_trig_sub", "desc": f"Trig substitution: tan(theta) = {fy} / {fx}", "marks": 1, "editable": True},
                {"id": "mp_dir", "desc": f"Direction θ = {_fmt_sa(theta)}° North of East", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "omitted_unit", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "1_nudge": "In the diagram, Fx and Fy form the legs of the right triangle, and the red vector R is the hypotenuse.",
            "2_concept": "Apply Pythagoras for magnitude and tan(θ) = Fy / Fx for direction.",
            "3_breakdown": f"R = sqrt({fx}^2 + {fy}^2) = {_fmt_sa(fr)} N. θ = arctan({fy}/{fx}) = {_fmt_sa(theta)}° North of East.",
        },
    }


# ============================================================================
# EXPORT REGISTRIES FOR SUBSKILLS 01–25
# ============================================================================

BUILDERS_01_25: Dict[str, Any] = {
    "01_scalar_vs_vector_definition_and_classification": build_01_scalar_vs_vector_definition_and_classification,
    "02_magnitude_and_direction_specification": build_02_magnitude_and_direction_specification,
    "03_distance_vs_displacement_1d": build_03_distance_vs_displacement_1d,
    "04_speed_vs_velocity_1d_average": build_04_speed_vs_velocity_1d_average,
    "05_mass_vs_weight_distinction": build_05_mass_vs_weight_distinction,
    "06_vector_arrow_representation_and_scale": build_06_vector_arrow_representation_and_scale,
    "07_vector_compass_direction_conventions": build_07_vector_compass_direction_conventions,
    "08_vector_three_figure_bearing": build_08_vector_three_figure_bearing,
    "09_equality_and_negative_vectors": build_09_equality_and_negative_vectors,
    "10_collinear_vectors_same_direction_addition": build_10_collinear_vectors_same_direction_addition,
    "11_collinear_vectors_opposite_direction_subtraction": build_11_collinear_vectors_opposite_direction_subtraction,
    "12_collinear_multi_stage_displacements_1d": build_12_collinear_multi_stage_displacements_1d,
    "13_collinear_net_force_horizontal": build_13_collinear_net_force_horizontal,
    "14_collinear_net_force_vertical": build_14_collinear_net_force_vertical,
    "15_resultant_vector_concept_and_definition": build_15_resultant_vector_concept_and_definition,
    "16_tail_to_head_vector_addition_concept": build_16_tail_to_head_vector_addition_concept,
    "17_parallelogram_law_vector_addition_concept": build_17_parallelogram_law_vector_addition_concept,
    "18_perpendicular_vectors_pythagoras_magnitude": build_18_perpendicular_vectors_pythagoras_magnitude,
    "19_perpendicular_displacements_pythagoras_east_north": build_19_perpendicular_displacements_pythagoras_east_north,
    "20_perpendicular_vectors_trig_direction_angle": build_20_perpendicular_vectors_trig_direction_angle,
    "21_perpendicular_displacements_bearing": build_21_perpendicular_displacements_bearing,
    "22_perpendicular_forces_pythagorean_triple_3_4_5": build_22_perpendicular_forces_pythagorean_triple_3_4_5,
    "23_perpendicular_forces_pythagorean_triple_5_12_13": build_23_perpendicular_forces_pythagorean_triple_5_12_13,
    "24_perpendicular_forces_pythagorean_triple_8_15_17": build_24_perpendicular_forces_pythagorean_triple_8_15_17,
    "25_orthogonal_resultant_with_vector_diagram": build_25_orthogonal_resultant_with_vector_diagram,
}

SUBSKILLS_01_25: List[str] = list(BUILDERS_01_25.keys())
