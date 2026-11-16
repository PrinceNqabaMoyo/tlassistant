"""Physical Sciences (Grades 10 & 11) — Electromagnetism & Synthesis Archetypes 26 to 50.

Grounded strictly in the South African National Physical Sciences Curriculum:
- Magnetic field associated with current-carrying conductors (straight wire, circular loop, solenoid).
- Right-Hand Rule and Right-Hand Solenoid Rule.
- Magnetic flux: Phi = B * A * cos(theta).
- Faraday's Law of Electromagnetic Induction: emf = -N * (Delta Phi / Delta t).
- Lenz's Law and direction of induced current opposing change in magnetic flux.
- Motional emf in a straight rod moving in a magnetic field: emf = B * L * v.
- Magnetic force on moving charges (F = q * v * B * sin(theta)) and wires (F = I * L * B * sin(theta)).
- AC generators vs DC generators, ideal transformers (Vs/Vp = Ns/Np), synthesis, and diagnostic autopsy.

100% deterministic, math backed, zero-LLM, compliant with 6-pillar contract.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict

from .electrostatics_electromagnetism_archetypes_01_25 import (
    E_CHARGE,
    K_COULOMB,
    _clean_svg,
    _fmt_sa,
    _fmt_sci,
)

MU_0 = 4.0 * math.pi * 1e-7  # T*m/A (permeability of free space)


# Archetype 26: Magnetic field around a straight current-carrying conductor
def _b26_magnetic_field_around_straight_conductor(r: random.Random) -> Dict[str, Any]:
    curr_a = r.choice([2.0, 3.5, 4.0, 5.0, 6.5, 8.0, 10.0, 12.0])
    direction = r.choice([
        ("upwards (+y)", "anticlockwise (viewed from top)", "into the plane (away from observer)", "out of the plane (towards observer)"),
        ("downwards (-y)", "clockwise (viewed from top)", "out of the plane (towards observer)", "into the plane (away from observer)"),
    ])
    curr_dir, loop_sense, right_side, left_side = direction

    svg = _clean_svg(f"""
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="200" fill="#f8fafc" rx="8"/>
  <ellipse cx="180" cy="105" rx="95" ry="35" fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="5,4"/>
  <ellipse cx="180" cy="105" rx="55" ry="20" fill="none" stroke="#2563eb" stroke-width="2"/>
  <line x1="180" y1="25" x2="180" y2="185" stroke="#dc2626" stroke-width="5"/>
  <text x="192" y="45" font-size="12" font-weight="bold" fill="#b91c1c">I = {_fmt_sa(curr_a)} A ({curr_dir})</text>
  <text x="80" y="108" font-size="11" font-weight="bold" fill="#1e293b">Point P</text>
  <text x="250" y="108" font-size="11" font-weight="bold" fill="#1e293b">Point Q</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing a long, straight vertical wire carrying a conventional electric current "
        f"of $I = {_fmt_sa(curr_a)}\\text{{ A}}$ oriented {curr_dir}.\n\n"
        f"1. State the Right-Hand Rule used to determine the orientation of the magnetic flux lines surrounding a straight wire.\n"
        f"2. Describe the geometric shape and rotational sense of the flux lines when viewed from above.\n"
        f"3. State the orientation of the magnetic vector $\\vec{{B}}$ at point $Q$ and at point $P$."
    )

    ans_latex = (
        rf"1.\; \text{{Hold the conductor in the right hand with the thumb pointing in the direction of conventional current (from + to -); "
        rf"the curled fingers point in the direction of the magnetic field.}}\n"
        rf"2.\; \text{{Concentric circles around the wire, directed {loop_sense}.}}\n"
        rf"3.\; \text{{At Q (right): {right_side}; at P (left): {left_side}.}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Right-Hand Rule statement (thumb = conventional current, fingers = B field)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Concentric circles, {loop_sense}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"At Q: {right_side}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"At P: {left_side}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "used_left_hand_electron_flow_without_specifying", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Point your right thumb in the direction of conventional current $I$.",
        "tier_2": f"With thumb pointing {curr_dir.split()[0]}, observe which way your fingers curl on the left and right of the wire.",
        "tier_3": f"Field forms concentric circles ({loop_sense}): at Q it points {right_side}, at P it points {left_side}.",
    }

    return {
        "id": f"ps_em_wire_dir_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_wire_dir_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "26_magnetic_field_around_straight_conductor",
        "learning_objective_id": "ps_em_26_straight_wire_rhr",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_left_hand_for_conventional_current", "confused_dot_and_cross_notation"],
        "keywords": ["Right-Hand Rule", "straight conductor", "concentric circles", "magnetic field"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 27: Magnetic field magnitude scaling around a straight wire
def _b27_magnetic_field_magnitude_straight_wire(r: random.Random) -> Dict[str, Any]:
    i_amp = r.choice([4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 15.0, 20.0])
    d_cm = r.choice([2.0, 4.0, 5.0, 8.0, 10.0, 12.0, 16.0, 20.0])
    d_m = d_cm / 100.0
    b_tesla = (MU_0 * i_amp) / (2.0 * math.pi * d_m)
    i_factor = r.choice([2, 3, 4])
    r_factor = r.choice([2, 3])
    b_new = b_tesla * (i_factor / r_factor)

    prompt = (
        f"A long straight wire carries a constant current of $I = {_fmt_sa(i_amp)}\\text{{ A}}$. "
        f"At a perpendicular distance of $r = {_fmt_sa(d_cm)}\\text{{ cm}}$ from the wire, the magnetic flux density "
        f"has magnitude $B = {_fmt_sci(b_tesla)}\\text{{ T}}$ (given $B = \\frac{{\\mu_0 I}}{{2\\pi r}}$).\n\n"
        f"1. State how the magnetic field strength $B$ depends on the current $I$ and perpendicular distance $r$.\n"
        f"2. Calculate the new magnetic flux density if the current is multiplied by ${i_factor}$ and the distance from the wire is multiplied by ${r_factor}$."
    )

    ans_latex = (
        rf"1.\; B \propto I \text{{ (directly proportional to current) and }} B \propto \frac{{1}}{{r}} \text{{ (inversely proportional to distance).}}\n"
        rf"2.\; B_{{\text{{new}}}} = B \times \frac{{{i_factor}}}{{{r_factor}}} = ({_fmt_sci(b_tesla)}) \times \frac{{{i_factor}}}{{{r_factor}}} = {_fmt_sci(b_new)}\text{{ T}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "State B is directly proportional to I and inversely proportional to r", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Apply scaling ratio {i_factor}/{r_factor}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate B_new = {_fmt_sci(b_new)} T", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "squared_distance_for_straight_wire", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Unlike Coulomb's Law, the magnetic field around a long straight wire is inversely proportional to $r$ (not $r^2$): $B \\propto I/r$.",
        "tier_2": f"Multiply original $B$ by $\\frac{{{i_factor}}}{{{r_factor}}}$.",
        "tier_3": f"$B_{{\\text{{new}}}} = {_fmt_sci(b_new)}\\text{{ T}}$.",
    }

    return {
        "id": f"ps_em_wire_mag_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_wire_mag_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "27_magnetic_field_magnitude_straight_wire",
        "learning_objective_id": "ps_em_27_straight_wire_scaling",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["applied_inverse_square_law_to_long_wire", "inverted_current_and_distance_factors"],
        "keywords": ["magnetic flux density", "straight wire", "proportionality"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 28: Magnetic field of a current-carrying circular loop
def _b28_magnetic_field_current_loop(r: random.Random) -> Dict[str, Any]:
    curr_a = r.choice([1.5, 2.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.0])
    rad_cm = r.choice([4.0, 5.0, 6.0, 8.0, 10.0, 12.0])
    sense, center_dir, face_pole = r.choice([
        ("anticlockwise", "out of the page (towards the observer, ⊙)", "North pole"),
        ("clockwise", "into the page (away from the observer, ⊗)", "South pole"),
    ])

    svg = _clean_svg(f"""
<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="200" fill="#f8fafc" rx="8"/>
  <circle cx="160" cy="100" r="60" fill="none" stroke="#d97706" stroke-width="4"/>
  <circle cx="160" cy="100" r="5" fill="#1e293b"/>
  <text x="160" y="88" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">Centre O (r = {_fmt_sa(rad_cm)} cm)</text>
  <text x="160" y="182" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">Circular loop: I = {_fmt_sa(curr_a)} A ({sense})</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing a single circular conducting loop of radius $r = {_fmt_sa(rad_cm)}\\text{{ cm}}$ "
        f"lying in the plane of the page and carrying a conventional current of $I = {_fmt_sa(curr_a)}\\text{{ A}}$ in a {sense} direction.\n\n"
        f"1. Determine the direction of the magnetic field at the centre $O$ of the loop.\n"
        f"2. Which magnetic pole (North or South) does this face of the current loop represent?\n"
        f"3. State two ways to increase the magnetic field strength at the centre $O$."
    )

    ans_latex = (
        rf"1.\; \text{{At the centre }} O\text{{, the magnetic field is directed {center_dir}.}}\n"
        rf"2.\; \text{{{face_pole} (since {sense} current corresponds to a {face_pole}).}}\n"
        rf"3.\; \text{{(i) Increase the current }} I\text{{; (ii) Increase the number of turns }} N\text{{ (or decrease the radius }} r\text{{ of the loop).}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Center magnetic field direction: {center_dir}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Magnetic polarity: {face_pole}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Two valid methods to increase B at center (increase I, add turns N, decrease r)", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Curl the fingers of your right hand in the direction of the current around the loop; your thumb points along the magnetic field inside the loop.",
        "tier_2": "An anticlockwise current produces field lines coming out towards you (North pole); clockwise goes away (South pole).",
        "tier_3": f"For {sense} current: field at O is {center_dir} ({face_pole}).",
    }

    return {
        "id": f"ps_em_loop_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_loop_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "28_magnetic_field_current_loop",
        "learning_objective_id": "ps_em_28_circular_loop",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["reversed_clock_face_rule", "claimed_field_at_centre_is_zero"],
        "keywords": ["circular loop", "magnetic field", "clock rule", "Right-Hand Rule"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 29: Solenoid magnetic field polarity and strength factors
def _b29_solenoid_magnetic_field_polarity_and_factors(r: random.Random) -> Dict[str, Any]:
    turns = r.choice([150, 200, 250, 300, 400, 500, 600])
    curr_a = r.choice([1.2, 1.8, 2.4, 3.0, 3.6, 4.5, 5.0])
    left_pole, right_pole, front_dir = r.choice([
        ("North pole", "South pole", "downwards across the front of the solenoid"),
        ("South pole", "North pole", "upwards across the front of the solenoid"),
    ])

    svg = _clean_svg(f"""
<svg viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" fill="#f8fafc" rx="8"/>
  <rect x="90" y="65" width="220" height="50" rx="6" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
  <path d="M 110,65 L 125,115 M 145,65 L 160,115 M 180,65 L 195,115 M 215,65 L 230,115 M 250,65 L 265,115 M 285,65 L 295,115" stroke="#d97706" stroke-width="3.5"/>
  <text x="55" y="95" font-size="13" font-weight="bold" fill="#0f172a">End X</text>
  <text x="325" y="95" font-size="13" font-weight="bold" fill="#0f172a">End Y</text>
  <text x="200" y="155" font-size="11" fill="#334155" text-anchor="middle">Solenoid: N = {turns} turns, I = {_fmt_sa(curr_a)} A ({front_dir.split()[0]} in front)</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing a solenoid with $N = {turns}$ turns carrying a current of $I = {_fmt_sa(curr_a)}\\text{{ A}}$ "
        f"such that conventional current flows {front_dir}.\n\n"
        f"1. State the Right-Hand Solenoid Rule to find the magnetic polarity of the solenoid.\n"
        f"2. Identify the magnetic polarity (North or South) of **End X** and **End Y**.\n"
        f"3. Describe the magnetic field pattern **inside** the solenoid and state three ways to strengthen the electromagnet."
    )

    ans_latex = (
        rf"1.\; \text{{Grip the solenoid with the right hand so the fingers curl in the direction of conventional current around the coils; "
        rf"the extended thumb points towards the North pole.}}\n"
        rf"2.\; \text{{End X is a {left_pole}; End Y is a {right_pole}.}}\n"
        rf"3.\; \text{{Inside field: uniform (parallel, equally spaced lines from South to North). Strengthen by: (i) increasing current }} I\text{{, "
        rf"(ii) increasing number of turns per unit length, (iii) inserting a soft iron core.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Right-Hand Solenoid Rule statement", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"End X = {left_pole}, End Y = {right_pole}", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Uniform magnetic field inside solenoid", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Three factors: increase I, increase N/L, insert soft iron core", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Wrap the fingers of your right hand in the direction of current across the front of the coil.",
        "tier_2": f"When fingers curl {front_dir}, your right thumb points towards the {left_pole if left_pole == 'North pole' else right_pole}.",
        "tier_3": f"End X is {left_pole}, End Y is {right_pole}. A soft iron core concentrates the magnetic flux.",
    }

    return {
        "id": f"ps_em_solenoid_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_solenoid_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "29_solenoid_magnetic_field_polarity_and_factors",
        "learning_objective_id": "ps_em_29_solenoid_polarity",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_thumb_and_fingers_in_solenoid_rule", "claimed_field_inside_solenoid_is_zero"],
        "keywords": ["solenoid", "electromagnet", "Right-Hand Rule", "soft iron core"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 30: Magnetic flux through a surface perpendicular to the field
def _b30_magnetic_flux_perpendicular_surface(r: random.Random) -> Dict[str, Any]:
    b_val = r.choice([0.15, 0.25, 0.40, 0.50, 0.65, 0.80, 1.20, 1.50])
    area_m2 = r.choice([0.02, 0.04, 0.05, 0.08, 0.12, 0.15, 0.20, 0.25])
    phi = round(b_val * area_m2, 4)

    prompt = (
        f"A flat wire loop of cross-sectional area $A = {_fmt_sa(area_m2, 3)}\\text{{ m}}^2$ is placed inside a uniform "
        f"magnetic field of flux density $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$ such that the plane of the loop is perpendicular "
        f"to the magnetic field lines ($\\theta = 0^\\circ$ between $\\vec{{B}}$ and the normal to the loop).\n\n"
        f"1. Define **magnetic flux** ($\\Phi$) and state its SI unit.\n"
        f"2. Calculate the magnetic flux $\\Phi$ passing through the loop."
    )

    ans_latex = (
        rf"1.\; \text{{Magnetic flux is the product of the magnetic flux density }} B\text{{, the area }} A\text{{, and the cosine of the angle }} \theta "
        rf"\text{{ between the magnetic field and the normal to the surface. SI unit: weber (Wb).}}\n"
        rf"2.\; \Phi = B A \cos\theta = ({_fmt_sa(b_val, 2)})({_fmt_sa(area_m2, 3)})\cos(0^\circ) = {_fmt_sa(phi, 4)}\text{{ Wb}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Definition of magnetic flux and unit weber (Wb)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Formula: Phi = B * A * cos(theta) with theta = 0 deg", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculation: Phi = {_fmt_sa(phi, 4)} Wb", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "used_theta_90_when_plane_perpendicular", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "When the plane of the coil is perpendicular to $\\vec{B}$, the normal vector $\\hat{n}$ is parallel to $\\vec{B}$, so $\\theta = 0^\\circ$ and $\\cos(0^\\circ) = 1$.",
        "tier_2": "Use $\\Phi = B A \\cos(0^\\circ)$.",
        "tier_3": f"$\\Phi = {_fmt_sa(b_val, 2)} \\times {_fmt_sa(area_m2, 3)} = {_fmt_sa(phi, 4)}\\text{{ Wb}}$.",
    }

    return {
        "id": f"ps_em_flux_perp_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_flux_perp_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "30_magnetic_flux_perpendicular_surface",
        "learning_objective_id": "ps_em_30_flux_perpendicular",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["substituted_90_deg_for_perpendicular_plane", "confused_flux_with_flux_density"],
        "keywords": ["magnetic flux", "weber", "normal vector"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "easy",
        "marks": 4,
    }


# Archetype 31: Magnetic flux through an angled surface
def _b31_magnetic_flux_angled_surface(r: random.Random) -> Dict[str, Any]:
    b_val = r.choice([0.30, 0.45, 0.60, 0.75, 0.90, 1.20, 1.50])
    area_m2 = r.choice([0.04, 0.06, 0.08, 0.10, 0.15, 0.20, 0.25])
    plane_angle = r.choice([20, 25, 30, 35, 40, 50, 60, 70])
    normal_angle = 90 - plane_angle
    phi = b_val * area_m2 * math.cos(math.radians(normal_angle))

    svg = _clean_svg(f"""
<svg viewBox="0 0 380 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="180" fill="#f8fafc" rx="8"/>
  <line x1="40" y1="60" x2="340" y2="60" stroke="#3b82f6" stroke-width="1.8"/>
  <line x1="40" y1="95" x2="340" y2="95" stroke="#3b82f6" stroke-width="1.8"/>
  <line x1="40" y1="130" x2="340" y2="130" stroke="#3b82f6" stroke-width="1.8"/>
  <text x="348" y="98" font-size="12" font-weight="bold" fill="#1d4ed8">B = {_fmt_sa(b_val, 2)} T</text>
  <line x1="130" y1="145" x2="250" y2="45" stroke="#dc2626" stroke-width="4"/>
  <line x1="190" y1="95" x2="140" y2="35" stroke="#16a34a" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="125" y="28" font-size="11" font-weight="bold" fill="#15803d">Normal (θ = {normal_angle}°)</text>
  <text x="190" y="168" font-size="11" fill="#334155" text-anchor="middle">Plane angle with B = {plane_angle}°, A = {_fmt_sa(area_m2, 2)} m²</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing a flat coil of area $A = {_fmt_sa(area_m2, 2)}\\text{{ m}}^2$ placed in a uniform "
        f"magnetic field of $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$. The **plane** of the coil makes an angle of ${plane_angle}^\\circ$ "
        f"with the magnetic field lines.\n\n"
        f"1. Determine the angle $\\theta$ between the magnetic field $\\vec{{B}}$ and the **normal** to the coil.\n"
        f"2. Calculate the magnetic flux $\\Phi$ through the coil."
    )

    ans_latex = (
        rf"1.\; \theta = 90^\circ - {plane_angle}^\circ = {normal_angle}^\circ\n"
        rf"2.\; \Phi = B A \cos\theta = ({_fmt_sa(b_val, 2)})({_fmt_sa(area_m2, 2)})\cos({normal_angle}^\circ) = {_fmt_sa(phi, 4)}\text{{ Wb}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Angle with normal: theta = 90 - {plane_angle} = {normal_angle} deg", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Formula: Phi = B * A * cos(theta)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Substitute theta = {normal_angle} deg and evaluate: {_fmt_sa(phi, 4)} Wb", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "used_plane_angle_directly_in_cos", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "In $\\Phi = B A \\cos\\theta$, $\\theta$ is always measured between $\\vec{B}$ and the **normal** (perpendicular) to the loop.",
        "tier_2": f"Since the plane makes ${plane_angle}^\\circ$ with $\\vec{{B}}$, the normal makes $\\theta = 90^\\circ - {plane_angle}^\\circ = {normal_angle}^\\circ$.",
        "tier_3": f"$\\Phi = {_fmt_sa(b_val, 2)} \\times {_fmt_sa(area_m2, 2)} \\times \\cos({normal_angle}^\\circ) = {_fmt_sa(phi, 4)}\\text{{ Wb}}$.",
    }

    return {
        "id": f"ps_em_flux_ang_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_flux_ang_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "31_magnetic_flux_angled_surface",
        "learning_objective_id": "ps_em_31_flux_angled",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_angle_with_plane_instead_of_normal", "used_sin_without_converting_angle"],
        "keywords": ["magnetic flux", "normal angle", "inclined coil"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 32: Magnetic flux through a circular coil of given radius
def _b32_magnetic_flux_circular_coil(r: random.Random) -> Dict[str, Any]:
    rad_cm = r.choice([4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 15.0])
    rad_m = rad_cm / 100.0
    b_val = r.choice([0.20, 0.35, 0.50, 0.60, 0.80, 1.10])
    theta_deg = r.choice([0, 25, 30, 45, 60])
    area = math.pi * (rad_m ** 2)
    phi = b_val * area * math.cos(math.radians(theta_deg))

    prompt = (
        f"A circular coil of radius $r = {_fmt_sa(rad_cm)}\\text{{ cm}}$ is situated in a uniform magnetic field of "
        f"$B = {_fmt_sa(b_val, 2)}\\text{{ T}}$. The normal to the circular coil makes an angle of $\\theta = {theta_deg}^\\circ$ "
        f"with the magnetic field.\n\n"
        f"1. Calculate the cross-sectional area $A = \\pi r^2$ of the coil in $\\text{{m}}^2$.\n"
        f"2. Calculate the magnetic flux $\\Phi$ through a single turn of the coil."
    )

    ans_latex = (
        rf"1.\; A = \pi r^2 = \pi ({_fmt_sa(rad_m, 2)})^2 = {_fmt_sa(area, 5)}\text{{ m}}^2\n"
        rf"2.\; \Phi = B A \cos\theta = ({_fmt_sa(b_val, 2)})({_fmt_sa(area, 5)})\cos({theta_deg}^\circ) = {_fmt_sa(phi, 5)}\text{{ Wb}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Convert radius to m ({_fmt_sa(rad_m, 2)} m) and calculate A = pi*r^2 = {_fmt_sa(area, 5)} m^2", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Formula: Phi = B * A * cos(theta)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate Phi = {_fmt_sa(phi, 5)} Wb", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "forgot_cm_to_m_conversion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "First convert radius $r$ from centimetres to metres ($r / 100$), then compute $A = \\pi r^2$.",
        "tier_2": f"Here $A = {_fmt_sa(area, 5)}\\text{{ m}}^2$ and $\\theta = {theta_deg}^\\circ$.",
        "tier_3": f"$\\Phi = {_fmt_sa(phi, 5)}\\text{{ Wb}}$.",
    }

    return {
        "id": f"ps_em_flux_circ_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_flux_circ_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "32_magnetic_flux_circular_coil",
        "learning_objective_id": "ps_em_32_flux_circular",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_cm_to_m_conversion", "used_2_pi_r_instead_of_pi_r_squared"],
        "keywords": ["circular coil", "area", "magnetic flux"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 33: Magnetic flux linkage through a rectangular multi-turn coil
def _b33_magnetic_flux_rectangular_coil(r: random.Random) -> Dict[str, Any]:
    l_cm = r.choice([10.0, 12.0, 15.0, 20.0, 25.0])
    w_cm = r.choice([6.0, 8.0, 10.0, 12.0])
    n_turns = r.choice([20, 40, 50, 80, 100, 120])
    b_val = r.choice([0.25, 0.40, 0.50, 0.75, 1.00])
    theta_deg = r.choice([0, 30, 45, 60])

    area = (l_cm / 100.0) * (w_cm / 100.0)
    phi_single = b_val * area * math.cos(math.radians(theta_deg))
    flux_linkage = n_turns * phi_single

    prompt = (
        f"A rectangular coil of dimensions $L = {_fmt_sa(l_cm)}\\text{{ cm}}$ by $W = {_fmt_sa(w_cm)}\\text{{ cm}}$ "
        f"consists of $N = {n_turns}$ tightly wound turns. It is placed in a uniform magnetic field of $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$ "
        f"with its normal at an angle of $\\theta = {theta_deg}^\\circ$ to the field.\n\n"
        f"1. Calculate the area $A$ of the rectangular coil in $\\text{{m}}^2$.\n"
        f"2. Calculate the magnetic flux $\\Phi$ through a single turn and the total flux linkage $N\\Phi$."
    )

    ans_latex = (
        rf"1.\; A = L \times W = ({_fmt_sa(l_cm/100, 2)})({_fmt_sa(w_cm/100, 2)}) = {_fmt_sa(area, 4)}\text{{ m}}^2\n"
        rf"2.\; \Phi = B A \cos({theta_deg}^\circ) = {_fmt_sa(phi_single, 5)}\text{{ Wb}}, \quad N\Phi = {n_turns} \times {_fmt_sa(phi_single, 5)} = {_fmt_sa(flux_linkage, 4)}\text{{ Wb-turns}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Area in m^2: A = {_fmt_sa(area, 4)} m^2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Single turn flux Phi = {_fmt_sa(phi_single, 5)} Wb", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Total flux linkage N*Phi = {_fmt_sa(flux_linkage, 4)} Wb", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "cm2_not_converted_to_m2", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Convert both length and width from cm to m before multiplying: $A = L \\times W$.",
        "tier_2": f"Calculate $\\Phi = B A \\cos({theta_deg}^\\circ)$, then multiply by $N = {n_turns}$ turns.",
        "tier_3": f"$A = {_fmt_sa(area, 4)}\\text{{ m}}^2$, $N\\Phi = {_fmt_sa(flux_linkage, 4)}\\text{{ Wb}}$.",
    }

    return {
        "id": f"ps_em_flux_rect_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_flux_rect_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "33_magnetic_flux_rectangular_coil",
        "learning_objective_id": "ps_em_33_flux_rectangular",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["divided_cm2_by_100_instead_of_10000", "omitted_number_of_turns_in_linkage"],
        "keywords": ["flux linkage", "rectangular coil", "turns"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 34: Faraday's Law with changing magnetic flux density B
def _b34_faradays_law_change_in_magnetic_field(r: random.Random) -> Dict[str, Any]:
    n_turns = r.choice([50, 80, 100, 120, 150, 200, 250])
    area_m2 = r.choice([0.02, 0.04, 0.05, 0.08, 0.10, 0.12])
    b_init = r.choice([0.10, 0.15, 0.20, 0.25])
    b_final = r.choice([0.60, 0.75, 0.85, 1.00, 1.20])
    dt = r.choice([0.05, 0.10, 0.20, 0.25, 0.40, 0.50])

    d_phi = (b_final - b_init) * area_m2
    emf = -n_turns * (d_phi / dt)

    prompt = (
        f"A coil of $N = {n_turns}$ turns and cross-sectional area $A = {_fmt_sa(area_m2, 2)}\\text{{ m}}^2$ is placed with its plane "
        f"perpendicular to a uniform magnetic field ($\\theta = 0^\\circ$). The magnetic flux density increases uniformly "
        f"from $B_i = {_fmt_sa(b_init, 2)}\\text{{ T}}$ to $B_f = {_fmt_sa(b_final, 2)}\\text{{ T}}$ in a time interval of $\\Delta t = {_fmt_sa(dt, 2)}\\text{{ s}}$.\n\n"
        f"1. State Faraday's Law of Electromagnetic Induction in words.\n"
        f"2. Calculate the change in magnetic flux $\\Delta\\Phi$ through one turn of the coil.\n"
        f"3. Calculate the magnitude of the average induced emf ($\\varepsilon$) across the coil."
    )

    ans_latex = (
        rf"1.\; \text{{The magnitude of the induced emf across the ends of a conductor is directly proportional to the rate of change "
        rf"of magnetic flux linkage with the conductor.}}\n"
        rf"2.\; \Delta\Phi = (B_f - B_i) A \cos(0^\circ) = ({_fmt_sa(b_final, 2)} - {_fmt_sa(b_init, 2)})({_fmt_sa(area_m2, 2)}) = {_fmt_sa(d_phi, 4)}\text{{ Wb}}\n"
        rf"3.\; |\varepsilon| = N \frac{{\Delta\Phi}}{{\Delta t}} = {n_turns} \times \frac{{{_fmt_sa(d_phi, 4)}}}{{{_fmt_sa(dt, 2)}}} = {_fmt_sa(abs(emf), 2)}\text{{ V}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Statement of Faraday's Law of Electromagnetic Induction", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate Delta Phi = {_fmt_sa(d_phi, 4)} Wb", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Formula: emf = -N * Delta Phi / Delta t", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculate |emf| = {_fmt_sa(abs(emf), 2)} V", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "multiplied_by_dt_instead_of_dividing", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Faraday's Law: $\\varepsilon = -N \\frac{\\Delta\\Phi}{\\Delta t}$, where $\\Delta\\Phi = (B_f - B_i) A \\cos\\theta$.",
        "tier_2": f"First find $\\Delta\\Phi = ({_fmt_sa(b_final, 2)} - {_fmt_sa(b_init, 2)}) \\times {_fmt_sa(area_m2, 2)} = {_fmt_sa(d_phi, 4)}\\text{{ Wb}}$.",
        "tier_3": f"$|\\varepsilon| = {n_turns} \\times {_fmt_sa(d_phi, 4)} / {_fmt_sa(dt, 2)} = {_fmt_sa(abs(emf), 2)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps_em_farad_b_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_farad_b_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "34_faradays_law_change_in_magnetic_field",
        "learning_objective_id": "ps_em_34_faraday_delta_b",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_final_B_instead_of_delta_B", "omitted_N_turns"],
        "keywords": ["Faraday's Law", "induced emf", "rate of change of flux"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 35: Faraday's Law with changing loop area A
def _b35_faradays_law_change_in_coil_area(r: random.Random) -> Dict[str, Any]:
    n_turns = r.choice([1, 10, 20, 40, 50, 80])
    b_val = r.choice([0.40, 0.50, 0.60, 0.80, 1.20, 1.50])
    a_init = r.choice([0.12, 0.15, 0.18, 0.20, 0.25, 0.30])
    a_final = r.choice([0.02, 0.04, 0.05, 0.06])
    dt = r.choice([0.10, 0.20, 0.25, 0.40, 0.50])

    d_phi = b_val * (a_final - a_init)
    emf = -n_turns * (d_phi / dt)

    prompt = (
        f"A flexible conducting coil of $N = {n_turns}$ turns is perpendicular to a uniform magnetic field of $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$. "
        f"The coil is stretched/compressed so that its cross-sectional area decreases uniformly from $A_i = {_fmt_sa(a_init, 2)}\\text{{ m}}^2$ "
        f"to $A_f = {_fmt_sa(a_final, 2)}\\text{{ m}}^2$ over $\\Delta t = {_fmt_sa(dt, 2)}\\text{{ s}}$.\n\n"
        f"1. Calculate the change in magnetic flux $\\Delta\\Phi$ through one turn of the coil.\n"
        f"2. Calculate the induced emf $\\varepsilon$ in the coil and explain the physical meaning of the negative sign in Faraday's formula."
    )

    ans_latex = (
        rf"1.\; \Delta\Phi = B (A_f - A_i)\cos(0^\circ) = {_fmt_sa(b_val, 2)}({_fmt_sa(a_final, 2)} - {_fmt_sa(a_init, 2)}) = {_fmt_sa(d_phi, 4)}\text{{ Wb}}\n"
        rf"2.\; \varepsilon = -N \frac{{\Delta\Phi}}{{\Delta t}} = -{n_turns} \left(\frac{{{_fmt_sa(d_phi, 4)}}}{{{_fmt_sa(dt, 2)}}}\right) = {_fmt_sa(emf, 2)}\text{{ V}}. "
        rf"\text{{ The negative sign represents Lenz's Law (the induced emf opposes the change in magnetic flux).}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate Delta Phi = {_fmt_sa(d_phi, 4)} Wb", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate induced emf = {_fmt_sa(emf, 2)} V", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Explain negative sign represents Lenz's Law (opposing flux change)", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Here $B$ is constant while area changes: $\\Delta\\Phi = B (A_f - A_i)$.",
        "tier_2": "Substitute $\\Delta\\Phi$ into $\\varepsilon = -N \\frac{\\Delta\\Phi}{\\Delta t}$.",
        "tier_3": f"$\\Delta\\Phi = {_fmt_sa(d_phi, 4)}\\text{{ Wb}}$, $\\varepsilon = {_fmt_sa(emf, 2)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps_em_farad_a_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_farad_a_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "35_faradays_law_change_in_coil_area",
        "learning_objective_id": "ps_em_35_faraday_delta_a",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_initial_and_final_area", "misinterpreted_negative_sign_in_faraday"],
        "keywords": ["Faraday's Law", "changing area", "Lenz's Law sign"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 36: Faraday's Law when coil flips 180 degrees (half turn)
def _b36_faradays_law_coil_rotation_half_turn(r: random.Random) -> Dict[str, Any]:
    n_turns = r.choice([40, 60, 80, 100, 120, 150, 200])
    area_m2 = r.choice([0.02, 0.03, 0.04, 0.05, 0.06, 0.08])
    b_val = r.choice([0.25, 0.30, 0.40, 0.50, 0.60, 0.80])
    dt = r.choice([0.04, 0.05, 0.08, 0.10, 0.20, 0.25])

    phi_i = b_val * area_m2
    phi_f = -b_val * area_m2
    d_phi = phi_f - phi_i
    emf = -n_turns * (d_phi / dt)

    prompt = (
        f"A flat coil of $N = {n_turns}$ turns and area $A = {_fmt_sa(area_m2, 2)}\\text{{ m}}^2$ is initially perpendicular "
        f"to a uniform magnetic field of $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$ ($\\theta_i = 0^\\circ$). The coil is rapidly "
        f"flipped through $180^\\circ$ (a half-turn, so $\\theta_f = 180^\\circ$) in $\\Delta t = {_fmt_sa(dt, 2)}\\text{{ s}}$.\n\n"
        f"1. Explain why the change in magnetic flux for a $180^\\circ$ flip is $\\Delta\\Phi = -2BA$ and not zero.\n"
        f"2. Calculate the magnitude of the average emf induced in the coil during the half-turn."
    )

    ans_latex = (
        rf"1.\; \Phi_i = BA\cos(0^\circ) = +BA \text{{ and }} \Phi_f = BA\cos(180^\circ) = -BA\text{{, so }} \Delta\Phi = \Phi_f - \Phi_i = -2BA = {_fmt_sa(d_phi, 4)}\text{{ Wb.}}\n"
        rf"2.\; |\varepsilon| = N \frac{{|\Delta\Phi|}}{{\Delta t}} = {n_turns} \times \frac{{{_fmt_sa(abs(d_phi), 4)}}}{{{_fmt_sa(dt, 2)}}} = {_fmt_sa(abs(emf), 2)}\text{{ V}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Show Phi_i = +BA and Phi_f = -BA so Delta Phi = -2BA", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Formula: |emf| = N * |Delta Phi| / Delta t", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate |emf| = {_fmt_sa(abs(emf), 2)} V", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "claimed_delta_phi_is_zero", "penalty": -2}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Note that $\\cos(0^\\circ) = +1$ and $\\cos(180^\\circ) = -1$.",
        "tier_2": "Therefore $\\Delta\\Phi = BA(\\cos 180^\\circ - \\cos 0^\\circ) = -2BA$.",
        "tier_3": f"$|\\Delta\\Phi| = {_fmt_sa(abs(d_phi), 4)}\\text{{ Wb}}$, $|\\varepsilon| = {_fmt_sa(abs(emf), 2)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps_em_flip180_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_flip180_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "36_faradays_law_coil_rotation_half_turn",
        "learning_objective_id": "ps_em_36_half_turn_flip",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_180_flip_gives_zero_flux_change", "forgot_factor_of_2_in_reversal"],
        "keywords": ["half-turn", "180 degree rotation", "Faraday's Law"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 4,
    }


# Archetype 37: Faraday's Law when coil rotates 90 degrees (quarter turn)
def _b37_faradays_law_coil_rotation_quarter_turn(r: random.Random) -> Dict[str, Any]:
    n_turns = r.choice([50, 75, 100, 125, 150, 200, 250])
    area_m2 = r.choice([0.02, 0.03, 0.04, 0.05, 0.08, 0.10])
    b_val = r.choice([0.20, 0.35, 0.45, 0.60, 0.75, 0.90])
    dt = r.choice([0.05, 0.10, 0.15, 0.20, 0.25])

    phi_i = b_val * area_m2
    phi_f = 0.0
    d_phi = phi_f - phi_i
    emf = -n_turns * (d_phi / dt)

    prompt = (
        f"A rectangular coil with $N = {n_turns}$ turns and area $A = {_fmt_sa(area_m2, 2)}\\text{{ m}}^2$ is initially "
        f"perpendicular to a magnetic field of $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$ ($\\theta_i = 0^\\circ$). It is rotated "
        f"through a quarter-turn ($90^\\circ$) in $\\Delta t = {_fmt_sa(dt, 2)}\\text{{ s}}$ so that its plane lies parallel to the field ($\\theta_f = 90^\\circ$).\n\n"
        f"1. State the final magnetic flux $\\Phi_f$ when the plane of the coil is parallel to the field.\n"
        f"2. Calculate the induced emf $\\varepsilon$ in the coil during this quarter-turn rotation."
    )

    ans_latex = (
        rf"1.\; \Phi_f = BA\cos(90^\circ) = 0\text{{ Wb}}\n"
        rf"2.\; \Delta\Phi = 0 - ({_fmt_sa(b_val, 2)})({_fmt_sa(area_m2, 2)}) = {_fmt_sa(d_phi, 4)}\text{{ Wb}} \implies "
        rf"\varepsilon = -{n_turns} \left(\frac{{{_fmt_sa(d_phi, 4)}}}{{{_fmt_sa(dt, 2)}}}\right) = {_fmt_sa(emf, 2)}\text{{ V}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "State final flux Phi_f = 0 Wb", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate Delta Phi = {_fmt_sa(d_phi, 4)} Wb", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Calculate induced emf = {_fmt_sa(emf, 2)} V", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "When the plane of the coil is parallel to $\\vec{B}$, the normal is at $90^\\circ$ to $\\vec{B}$, so $\\Phi_f = 0$.",
        "tier_2": "Compute $\\Delta\\Phi = 0 - BA$, then $\\varepsilon = -N \\frac{\\Delta\\Phi}{\\Delta t}$.",
        "tier_3": f"$\\varepsilon = {_fmt_sa(emf, 2)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps_em_rot90_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_rot90_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "37_faradays_law_coil_rotation_quarter_turn",
        "learning_objective_id": "ps_em_37_quarter_turn",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_parallel_plane_has_maximum_flux", "inverted_dt_in_rate"],
        "keywords": ["quarter-turn", "90 degree rotation", "induced emf"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 38: Induced current in a closed circuit (I = emf / R)
def _b38_induced_current_in_closed_circuit(r: random.Random) -> Dict[str, Any]:
    n_turns = r.choice([40, 50, 80, 100, 120, 160])
    d_phi = r.choice([0.02, 0.03, 0.04, 0.05, 0.06, 0.08])
    dt = r.choice([0.10, 0.20, 0.25, 0.40, 0.50])
    res_ohm = r.choice([2.0, 4.0, 5.0, 8.0, 10.0, 16.0])

    emf_mag = n_turns * (d_phi / dt)
    curr_a = emf_mag / res_ohm

    prompt = (
        f"A closed circular coil of $N = {n_turns}$ turns has a total electrical resistance of $R = {_fmt_sa(res_ohm)}\\;\\Omega$. "
        f"The magnetic flux through each turn changes by $|\\Delta\\Phi| = {_fmt_sa(d_phi, 2)}\\text{{ Wb}}$ in a time of $\\Delta t = {_fmt_sa(dt, 2)}\\text{{ s}}$.\n\n"
        f"1. Calculate the magnitude of the induced emf $|\\varepsilon|$ in the coil.\n"
        f"2. Calculate the magnitude of the induced current $I$ flowing through the closed coil."
    )

    ans_latex = (
        rf"1.\; |\varepsilon| = N \frac{{|\Delta\Phi|}}{{\Delta t}} = {n_turns} \times \frac{{{_fmt_sa(d_phi, 2)}}}{{{_fmt_sa(dt, 2)}}} = {_fmt_sa(emf_mag, 2)}\text{{ V}}\n"
        rf"2.\; I = \frac{{|\varepsilon|}}{{R}} = \frac{{{_fmt_sa(emf_mag, 2)}}}{{{_fmt_sa(res_ohm)}}} = {_fmt_sa(curr_a, 2)}\text{{ A}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula: |emf| = N * |Delta Phi| / Delta t", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate |emf| = {_fmt_sa(emf_mag, 2)} V", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Ohm's Law: I = |emf| / R", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculate I = {_fmt_sa(curr_a, 2)} A", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "First apply Faraday's Law to find $|\\varepsilon|$, then apply Ohm's Law $I = \\frac{|\\varepsilon|}{R}$.",
        "tier_2": f"$|\\varepsilon| = {n_turns} \\times {_fmt_sa(d_phi, 2)} / {_fmt_sa(dt, 2)} = {_fmt_sa(emf_mag, 2)}\\text{{ V}}$.",
        "tier_3": f"$I = {_fmt_sa(emf_mag, 2)} / {_fmt_sa(res_ohm)} = {_fmt_sa(curr_a, 2)}\\text{{ A}}$.",
    }

    return {
        "id": f"ps_em_ind_curr_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_ind_curr_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "38_induced_current_in_closed_circuit",
        "learning_objective_id": "ps_em_38_induced_current",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["multiplied_emf_by_R_instead_of_dividing", "omitted_turns_N"],
        "keywords": ["induced current", "Ohm's Law", "Faraday's Law"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 39: Total induced charge flow through a galvanometer
def _b39_induced_charge_flow_through_galvanometer(r: random.Random) -> Dict[str, Any]:
    n_turns = r.choice([25, 40, 50, 60, 80, 100])
    d_phi = r.choice([0.015, 0.020, 0.025, 0.030, 0.040, 0.050])
    res_ohm = r.choice([5.0, 10.0, 12.5, 20.0, 25.0])
    dt = r.choice([0.05, 0.10, 0.20, 0.40])

    emf = n_turns * (d_phi / dt)
    curr = emf / res_ohm
    delta_q = (n_turns * d_phi) / res_ohm

    prompt = (
        f"A search coil of $N = {n_turns}$ turns is connected in series with a ballistic galvanometer. "
        f"The total resistance of the coil-galvanometer circuit is $R = {_fmt_sa(res_ohm)}\\;\\Omega$. "
        f"When the coil is pulled out of a magnetic field in $\\Delta t = {_fmt_sa(dt, 2)}\\text{{ s}}$, the flux through each turn "
        f"changes by $|\\Delta\\Phi| = {_fmt_sa(d_phi, 3)}\\text{{ Wb}}$.\n\n"
        f"1. Calculate the average induced current $I$ during the $\\Delta t = {_fmt_sa(dt, 2)}\\text{{ s}}$ interval.\n"
        f"2. Calculate the total electric charge $\\Delta Q = I \\Delta t$ that flows through the galvanometer, and state whether $\\Delta Q$ depends on $\\Delta t$."
    )

    ans_latex = (
        rf"1.\; I = \frac{{N |\Delta\Phi|}}{{R \Delta t}} = \frac{{{n_turns} \times {_fmt_sa(d_phi, 3)}}}{{{_fmt_sa(res_ohm)} \times {_fmt_sa(dt, 2)}}} = {_fmt_sa(curr, 3)}\text{{ A}}\n"
        rf"2.\; \Delta Q = I \Delta t = \frac{{N |\Delta\Phi|}}{{R}} = {_fmt_sa(delta_q, 4)}\text{{ C (independent of }} \Delta t\text{{)}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate average induced current I = {_fmt_sa(curr, 3)} A", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate total induced charge Delta Q = {_fmt_sa(delta_q, 4)} C", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "State that Delta Q = N*Delta Phi / R is independent of time interval Delta t", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Since $I = \\frac{|\\varepsilon|}{R} = \\frac{N |\\Delta\\Phi|}{R \\Delta t}$, multiplying by $\\Delta t$ gives $\\Delta Q = \\frac{N |\\Delta\\Phi|}{R}$.",
        "tier_2": f"First compute $I = {_fmt_sa(curr, 3)}\\text{{ A}}$, then $\\Delta Q = I \\Delta t$.",
        "tier_3": f"$\\Delta Q = {_fmt_sa(delta_q, 4)}\\text{{ C}}$, which is independent of $\\Delta t$.",
    }

    return {
        "id": f"ps_em_ind_chg_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_ind_chg_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "39_induced_charge_flow_through_galvanometer",
        "learning_objective_id": "ps_em_39_induced_charge",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["claimed_total_charge_depends_on_speed_of_removal", "divided_by_dt_twice"],
        "keywords": ["induced charge", "galvanometer", "search coil"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 4,
    }


# Archetype 40: Lenz's Law — bar magnet approaching a solenoid
def _b40_lenzs_law_bar_magnet_entering_solenoid(r: random.Random) -> Dict[str, Any]:
    pole_approaching = r.choice(["North", "South"])
    speed_ms = r.choice([1.2, 1.5, 2.0, 2.4, 2.8, 3.0, 3.5, 4.0, 4.5, 5.0])
    induced_near_pole = pole_approaching
    far_pole = "South" if induced_near_pole == "North" else "North"

    svg = _clean_svg(f"""
<svg viewBox="0 0 420 170" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="170" fill="#f8fafc" rx="8"/>
  <rect x="25" y="65" width="90" height="34" fill="#ef4444" stroke="#991b1b" stroke-width="2"/>
  <text x="70" y="87" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">{pole_approaching} Pole</text>
  <line x1="120" y1="82" x2="160" y2="82" stroke="#1e293b" stroke-width="3"/>
  <polygon points="165,82 155,77 155,87" fill="#1e293b"/>
  <text x="142" y="68" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">v = {_fmt_sa(speed_ms)} m/s</text>
  <rect x="195" y="55" width="170" height="54" rx="6" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
  <text x="215" y="87" font-size="12" font-weight="bold" fill="#0f172a">End A</text>
  <text x="340" y="87" font-size="12" font-weight="bold" fill="#0f172a">End B</text>
  <text x="280" y="145" font-size="11" fill="#334155" text-anchor="middle">Solenoid connected to sensitive galvanometer</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing the **{pole_approaching} pole** of a bar magnet being pushed towards **End A** "
        f"of a stationary solenoid at a speed of $v = {_fmt_sa(speed_ms)}\\text{{ m/s}}$.\n\n"
        f"1. State **Lenz's Law** in words.\n"
        f"2. Identify the magnetic polarity induced at **End A** and **End B** of the solenoid as the magnet approaches.\n"
        f"3. State whether the magnetic force between the approaching magnet and the solenoid is attractive or repulsive."
    )

    ans_latex = (
        rf"1.\; \text{{The direction of the induced current is such that its magnetic field opposes the change in magnetic flux that produces it.}}\n"
        rf"2.\; \text{{To oppose the approaching {pole_approaching} pole, End A becomes a {induced_near_pole} pole and End B becomes a {far_pole} pole.}}\n"
        rf"3.\; \text{{Repulsive (like poles repel to oppose the inward motion).}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Statement of Lenz's Law (induced current opposes change in magnetic flux)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"End A = {induced_near_pole} pole, End B = {far_pole} pole", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Repulsive force opposing approach", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "stated_opposes_flux_instead_of_change_in_flux", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Lenz's Law: The solenoid induces a magnetic pole at End A that repels the approaching magnet pole.",
        "tier_2": f"To repel an approaching {pole_approaching} pole, End A must become a {induced_near_pole} pole.",
        "tier_3": f"End A = {induced_near_pole} pole, End B = {far_pole} pole; force is repulsive.",
    }

    return {
        "id": f"ps_em_lenz_in_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_lenz_in_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "40_lenzs_law_bar_magnet_entering_solenoid",
        "learning_objective_id": "ps_em_40_lenz_entering",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["induced_opposite_pole_on_approach", "omitted_word_change_in_lenz_law"],
        "keywords": ["Lenz's Law", "approaching magnet", "induced polarity"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 41: Lenz's Law — bar magnet pulled away from a solenoid
def _b41_lenzs_law_bar_magnet_leaving_solenoid(r: random.Random) -> Dict[str, Any]:
    pole_receding = r.choice(["North", "South"])
    speed_ms = r.choice([1.0, 1.4, 1.8, 2.2, 2.5, 3.2, 3.8, 4.2, 4.8])
    induced_near_pole = "South" if pole_receding == "North" else "North"
    far_pole = pole_receding

    svg = _clean_svg(f"""
<svg viewBox="0 0 420 170" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="170" fill="#f8fafc" rx="8"/>
  <rect x="65" y="65" width="90" height="34" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
  <text x="110" y="87" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">{pole_receding} Pole</text>
  <line x1="60" y1="82" x2="20" y2="82" stroke="#1e293b" stroke-width="3"/>
  <polygon points="15,82 25,77 25,87" fill="#1e293b"/>
  <text x="42" y="62" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">v = {_fmt_sa(speed_ms)} m/s</text>
  <rect x="195" y="55" width="170" height="54" rx="6" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
  <text x="215" y="87" font-size="12" font-weight="bold" fill="#0f172a">End A</text>
  <text x="340" y="87" font-size="12" font-weight="bold" fill="#0f172a">End B</text>
  <text x="280" y="145" font-size="11" fill="#334155" text-anchor="middle">Magnet pulled away from End A</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing the **{pole_receding} pole** of a bar magnet being pulled away from **End A** "
        f"of a stationary solenoid at $v = {_fmt_sa(speed_ms)}\\text{{ m/s}}$.\n\n"
        f"1. Explain how the magnetic flux through the solenoid changes as the magnet recedes.\n"
        f"2. Identify the magnetic polarity induced at **End A** and **End B** to oppose this change.\n"
        f"3. Explain how Lenz's Law is a direct consequence of the **Law of Conservation of Energy**."
    )

    ans_latex = (
        rf"1.\; \text{{The magnetic flux linking the solenoid decreases as the magnet moves away.}}\n"
        rf"2.\; \text{{To oppose the withdrawal of the {pole_receding} pole, End A becomes a {induced_near_pole} pole (attracting it) and End B becomes a {far_pole} pole.}}\n"
        rf"3.\; \text{{Mechanical work must be done against the attractive magnetic force to pull the magnet away; this mechanical energy is converted into electrical energy.}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Magnetic flux decreases", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"End A = {induced_near_pole} pole, End B = {far_pole} pole", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Mechanical work done against magnetic attraction converts to electrical energy", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "When a magnet is pulled away, the solenoid induces an opposite pole at the near end to attract it back.",
        "tier_2": f"To attract the receding {pole_receding} pole, End A must become a {induced_near_pole} pole.",
        "tier_3": f"End A = {induced_near_pole}, End B = {far_pole}. Work done pulling against attraction becomes electrical energy.",
    }

    return {
        "id": f"ps_em_lenz_out_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_lenz_out_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "41_lenzs_law_bar_magnet_leaving_solenoid",
        "learning_objective_id": "ps_em_41_lenz_leaving",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["induced_same_pole_when_magnet_recedes", "failed_to_link_lenz_law_to_energy_conservation"],
        "keywords": ["Lenz's Law", "receding magnet", "conservation of energy"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 42: Lenz's Law for a planar loop in a time-varying magnetic field
def _b42_lenzs_law_current_loop_in_varying_field(r: random.Random) -> Dict[str, Any]:
    rate_ts = r.choice([0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85])
    scenario = r.choice([
        ("inward perpendicular to the plane (⊗)", "increasing", "outward perpendicular to the plane (⊙)", "anticlockwise"),
        ("inward perpendicular to the plane (⊗)", "decreasing", "inward perpendicular to the plane (⊗)", "clockwise"),
        ("outward perpendicular to the plane (⊙)", "increasing", "inward perpendicular to the plane (⊗)", "clockwise"),
        ("outward perpendicular to the plane (⊙)", "decreasing", "outward perpendicular to the plane (⊙)", "anticlockwise"),
    ])
    ext_dir, change_type, ind_b_dir, ind_curr_dir = scenario

    prompt = (
        f"A stationary circular metallic ring rests in the xy-plane within a uniform external flux density $\\vec{{B}}_{{\\text{{ext}}}}$ oriented **{ext_dir}**. "
        f"The magnitude $B_{{\\text{{ext}}}}$ is **{change_type}** at a constant rate of $\\frac{{\\Delta B}}{{\\Delta t}} = {_fmt_sa(rate_ts, 2)}\\text{{ T/s}}$.\n\n"
        f"1. State the orientation of the **induced flux density** $\\vec{{B}}_{{\\text{{ind}}}}$ inside the ring required to oppose the flux change.\n"
        f"2. Determine the rotational sense in which the induced conventional charge carriers circulate through the ring."
    )

    ans_latex = (
        rf"1.\; \text{{Because the field directed {ext_dir} is {change_type}, the induced magnetic field points {ind_b_dir} to oppose the change.}}\n"
        rf"2.\; \text{{By the Right-Hand Rule, an induced field pointing {ind_b_dir} corresponds to a {ind_curr_dir} induced current.}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": f"Induced B field direction: {ind_b_dir}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Induced current sense: {ind_curr_dir}", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "If flux is increasing, $\\vec{B}_{\\text{ind}}$ points opposite to $\\vec{B}_{\\text{ext}}$. If flux is decreasing, $\\vec{B}_{\\text{ind}}$ points in the same direction as $\\vec{B}_{\\text{ext}}$ to reinforce it.",
        "tier_2": f"Here $\\vec{{B}}_{{\\text{{ind}}}}$ must point {ind_b_dir}.",
        "tier_3": f"Point your right thumb {ind_b_dir}: your curled fingers show {ind_curr_dir} current.",
    }

    return {
        "id": f"ps_em_lenz_loop_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_lenz_loop_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "42_lenzs_law_current_loop_in_varying_field",
        "learning_objective_id": "ps_em_42_lenz_planar_loop",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["always_opposed_external_B_even_when_decreasing", "reversed_right_hand_curl"],
        "keywords": ["Lenz's Law", "planar loop", "induced current direction"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 43: Motional emf in a conducting rod sliding on rails
def _b43_motional_emf_conducting_rod_on_rails(r: random.Random) -> Dict[str, Any]:
    b_val = r.choice([0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50])
    length_m = r.choice([0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.80])
    vel_ms = r.choice([2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0])
    emf = b_val * length_m * vel_ms

    svg = _clean_svg(f"""
<svg viewBox="0 0 380 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="180" fill="#f8fafc" rx="8"/>
  <line x1="60" y1="45" x2="330" y2="45" stroke="#475569" stroke-width="3"/>
  <line x1="60" y1="135" x2="330" y2="135" stroke="#475569" stroke-width="3"/>
  <line x1="60" y1="45" x2="60" y2="135" stroke="#475569" stroke-width="3"/>
  <line x1="210" y1="35" x2="210" y2="145" stroke="#dc2626" stroke-width="5"/>
  <line x1="215" y1="90" x2="265" y2="90" stroke="#16a34a" stroke-width="3"/>
  <polygon points="270,90 260,85 260,95" fill="#16a34a"/>
  <text x="245" y="78" font-size="11" font-weight="bold" fill="#15803d">v = {_fmt_sa(vel_ms)} m/s</text>
  <text x="135" y="95" font-size="12" font-weight="bold" fill="#1d4ed8">B = {_fmt_sa(b_val, 2)} T (⊗)</text>
  <text x="200" y="168" font-size="11" fill="#334155" text-anchor="middle">Sliding rod of length L = {_fmt_sa(length_m, 2)} m on conducting rails</text>
</svg>""")

    prompt = (
        f"Refer to the accompanying diagram showing a straight conducting rod of length $L = {_fmt_sa(length_m, 2)}\\text{{ m}}$ "
        f"sliding to the right at a constant speed of $v = {_fmt_sa(vel_ms)}\\text{{ m/s}}$ along frictionless horizontal rails "
        f"in a uniform magnetic field $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$ directed perpendicularly into the page ($\\otimes$).\n\n"
        f"1. Show from Faraday's Law ($|\\varepsilon| = \\frac{{\\Delta\\Phi}}{{\\Delta t}}$) that the motional emf induced across the rod is given by $|\\varepsilon| = B L v$.\n"
        f"2. Calculate the magnitude of the motional emf induced across the rod."
    )

    ans_latex = (
        rf"1.\; \Delta\Phi = B \Delta A = B L \Delta x \implies |\varepsilon| = \frac{{\Delta\Phi}}{{\Delta t}} = B L \frac{{\Delta x}}{{\Delta t}} = B L v\n"
        rf"2.\; |\varepsilon| = B L v = ({_fmt_sa(b_val, 2)})({_fmt_sa(length_m, 2)})({_fmt_sa(vel_ms)}) = {_fmt_sa(emf, 2)}\text{{ V}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Derivation: Delta A = L * Delta x and v = Delta x / Delta t => |emf| = BLv", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Substitution and calculation: |emf| = {_fmt_sa(emf, 2)} V", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "In time $\\Delta t$, the rod sweeps out an area $\\Delta A = L \\cdot v \\Delta t$.",
        "tier_2": "Substitute $\\Delta\\Phi = B L v \\Delta t$ into $|\\varepsilon| = \\Delta\\Phi / \\Delta t = B L v$.",
        "tier_3": f"$|\\varepsilon| = {_fmt_sa(b_val, 2)} \\times {_fmt_sa(length_m, 2)} \\times {_fmt_sa(vel_ms)} = {_fmt_sa(emf, 2)}\\text{{ V}}$.",
    }

    return {
        "id": f"ps_em_motional_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_motional_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "43_motional_emf_conducting_rod_on_rails",
        "learning_objective_id": "ps_em_43_motional_emf",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["divided_by_velocity_instead_of_multiplying", "confused_length_with_area"],
        "keywords": ["motional emf", "conducting rails", "swept area"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 44: Motional emf, induced current, and magnetic braking force
def _b44_motional_emf_induced_current_and_magnetic_drag(r: random.Random) -> Dict[str, Any]:
    b_val = r.choice([0.50, 0.80, 1.00, 1.20, 1.50])
    length_m = r.choice([0.20, 0.30, 0.40, 0.50])
    vel_ms = r.choice([2.0, 3.0, 4.0, 5.0, 6.0])
    res_ohm = r.choice([0.5, 1.0, 1.5, 2.0, 2.5, 4.0])

    emf = b_val * length_m * vel_ms
    curr = emf / res_ohm
    f_mag = curr * length_m * b_val

    prompt = (
        f"A conducting bar of length $L = {_fmt_sa(length_m, 2)}\\text{{ m}}$ slides to the right at a constant velocity of "
        f"$v = {_fmt_sa(vel_ms)}\\text{{ m/s}}$ along frictionless horizontal rails connected through a resistor of $R = {_fmt_sa(res_ohm)}\\;\\Omega$. "
        f"A uniform magnetic field $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$ points vertically downwards through the rails.\n\n"
        f"1. Calculate the induced emf $|\\varepsilon| = B L v$ and the induced current $I = |\\varepsilon|/R$.\n"
        f"2. Calculate the magnitude of the magnetic braking force $F_B = I L B$ acting on the bar, and state its direction."
    )

    ans_latex = (
        rf"1.\; |\varepsilon| = B L v = ({_fmt_sa(b_val, 2)})({_fmt_sa(length_m, 2)})({_fmt_sa(vel_ms)}) = {_fmt_sa(emf, 2)}\text{{ V}}, \quad "
        rf"I = \frac{{|\varepsilon|}}{{R}} = \frac{{{_fmt_sa(emf, 2)}}}{{{_fmt_sa(res_ohm)}}} = {_fmt_sa(curr, 2)}\text{{ A}}\n"
        rf"2.\; F_B = I L B = ({_fmt_sa(curr, 2)})({_fmt_sa(length_m, 2)})({_fmt_sa(b_val, 2)}) = {_fmt_sa(f_mag, 3)}\text{{ N directed to the left (opposing motion)}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate |emf| = {_fmt_sa(emf, 2)} V", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate current I = {_fmt_sa(curr, 2)} A", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Formula: F_B = I * L * B", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Calculate F_B = {_fmt_sa(f_mag, 3)} N", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Direction: to the left (opposing the rightward velocity)", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "First find $|\\varepsilon| = B L v$, then $I = |\\varepsilon| / R$.",
        "tier_2": "The current-carrying rod in magnetic field $B$ experiences a magnetic force $F_B = I L B$.",
        "tier_3": f"$I = {_fmt_sa(curr, 2)}\\text{{ A}}$, $F_B = {_fmt_sa(f_mag, 3)}\\text{{ N}}$ to the left.",
    }

    return {
        "id": f"ps_em_drag_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_drag_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "44_motional_emf_induced_current_and_magnetic_drag",
        "learning_objective_id": "ps_em_44_magnetic_drag",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["claimed_magnetic_force_accelerates_rod_forward", "omitted_B_in_force_formula"],
        "keywords": ["magnetic braking", "eddy drag", "motional emf"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 5,
    }


# Archetype 45: Magnetic Lorentz force on a moving charged particle
def _b45_magnetic_force_on_moving_charged_particle(r: random.Random) -> Dict[str, Any]:
    v_exp = r.choice([5, 6])
    v_base = r.choice([2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0])
    vel = v_base * (10 ** v_exp)
    b_val = r.choice([0.10, 0.20, 0.25, 0.40, 0.50, 0.80])
    theta_deg = r.choice([30, 45, 60, 90])

    force = E_CHARGE * vel * b_val * math.sin(math.radians(theta_deg))

    prompt = (
        f"A proton ($q = +1{{,}}6 \\times 10^{{-19}}\\text{{ C}}$) enters a uniform magnetic field of flux density "
        f"$B = {_fmt_sa(b_val, 2)}\\text{{ T}}$ with a speed of $v = {_fmt_sci(vel)}\\text{{ m/s}}$ at an angle of "
        f"$\\theta = {theta_deg}^\\circ$ to the magnetic field lines.\n\n"
        f"1. Write down the formula for the magnitude of the magnetic force $F$ acting on a moving charge.\n"
        f"2. Calculate the magnitude of the magnetic force experienced by the proton.\n"
        f"3. State the magnitude of the magnetic force if the proton instead moves parallel to the magnetic field lines ($\\theta = 0^\\circ$)."
    )

    ans_latex = (
        rf"1.\; F = |q| v B \sin\theta\n"
        rf"2.\; F = (1{{,}}6 \times 10^{{-19}})({_fmt_sci(vel)})({_fmt_sa(b_val, 2)})\sin({theta_deg}^\circ) = {_fmt_sci(force)}\text{{ N}}\n"
        rf"3.\; F = 0\text{{ N (since }}\sin 0^\circ = 0\text{{)}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula: F = q * v * B * sin(theta)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Substitution and evaluation: F = {_fmt_sci(force)} N", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "State F = 0 N when moving parallel to B", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "used_cos_instead_of_sin", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "For magnetic force on a moving charge, use $F = |q| v B \\sin\\theta$ where $\\theta$ is the angle between $\\vec{v}$ and $\\vec{B}$.",
        "tier_2": f"Substitute $q = 1{{,}}6 \\times 10^{{-19}}\\text{{ C}}$, $v = {_fmt_sci(vel)}\\text{{ m/s}}$, $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$, and $\\theta = {theta_deg}^\\circ$.",
        "tier_3": f"$F = {_fmt_sci(force)}\\text{{ N}}$; when $\\theta = 0^\\circ$, $F = 0\\text{{ N}}$.",
    }

    return {
        "id": f"ps_em_lorentz_q_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_lorentz_q_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "45_magnetic_force_on_moving_charged_particle",
        "learning_objective_id": "ps_em_45_force_on_charge",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_cos_instead_of_sin_in_lorentz_force", "claimed_stationary_charge_experiences_magnetic_force"],
        "keywords": ["Lorentz force", "moving charge", "magnetic deflection"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 46: Magnetic force on a current-carrying wire (motor effect)
def _b46_magnetic_force_on_current_carrying_conductor(r: random.Random) -> Dict[str, Any]:
    curr_a = r.choice([2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0])
    len_m = r.choice([0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60])
    b_val = r.choice([0.20, 0.30, 0.40, 0.50, 0.60, 0.80])
    theta_deg = r.choice([30, 45, 60, 90])

    force = curr_a * len_m * b_val * math.sin(math.radians(theta_deg))

    prompt = (
        f"A straight wire of active length $L = {_fmt_sa(len_m, 2)}\\text{{ m}}$ carries a current of $I = {_fmt_sa(curr_a)}\\text{{ A}}$ "
        f"at an angle of $\\theta = {theta_deg}^\\circ$ to a uniform magnetic field of $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$.\n\n"
        f"1. Calculate the magnitude of the magnetic force $F = I L B \\sin\\theta$ acting on the wire.\n"
        f"2. State how the direction of the force changes if the direction of the current is reversed."
    )

    ans_latex = (
        rf"1.\; F = I L B \sin\theta = ({_fmt_sa(curr_a)})({_fmt_sa(len_m, 2)})({_fmt_sa(b_val, 2)})\sin({theta_deg}^\circ) = {_fmt_sa(force, 3)}\text{{ N}}\n"
        rf"2.\; \text{{The magnetic force reverses direction (180}}^\circ\text{{ opposite).}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Formula: F = I * L * B * sin(theta)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate F = {_fmt_sa(force, 3)} N", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "State that reversing current reverses force direction", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Use the motor-effect formula $F = I L B \\sin\\theta$.",
        "tier_2": f"Substitute $I = {_fmt_sa(curr_a)}\\text{{ A}}$, $L = {_fmt_sa(len_m, 2)}\\text{{ m}}$, $B = {_fmt_sa(b_val, 2)}\\text{{ T}}$, and $\\theta = {theta_deg}^\\circ$.",
        "tier_3": f"$F = {_fmt_sa(force, 3)}\\text{{ N}}$; reversing $I$ reverses $\\vec{{F}}$.",
    }

    return {
        "id": f"ps_em_motor_f_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_motor_f_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "46_magnetic_force_on_current_carrying_conductor",
        "learning_objective_id": "ps_em_46_force_on_wire",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["used_cos_instead_of_sin_in_BIL", "omitted_angle_factor"],
        "keywords": ["motor effect", "magnetic force on conductor", "BIL sin theta"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


# Archetype 47: AC generator (slip rings) vs DC generator (split-ring commutator)
def _b47_ac_generator_slip_rings_vs_dc_commutator(r: random.Random) -> Dict[str, Any]:
    freq_hz = r.choice([25, 40, 50, 60, 80, 100])
    v_peak = r.choice([12, 24, 36, 48, 100, 150, 220, 311])
    period_s = 1.0 / freq_hz

    prompt = (
        f"An alternating current (AC) generator rotates at a constant frequency of $f = {freq_hz}\\text{{ Hz}}$ "
        f"and produces a peak emf of $\\varepsilon_{{\\max}} = {v_peak}\\text{{ V}}$.\n\n"
        f"1. State the energy conversion that takes place in an electrical generator.\n"
        f"2. Calculate the period $T = \\frac{{1}}{{f}}$ of one complete rotation of the generator coil.\n"
        f"3. State the structural component that distinguishes an **AC generator** from a **DC generator**, and explain how the coil orientation relates to maximum vs zero induced emf."
    )

    ans_latex = (
        rf"1.\; \text{{Mechanical energy is converted into electrical energy.}}\n"
        rf"2.\; T = \frac{{1}}{{f}} = \frac{{1}}{{{freq_hz}}} = {_fmt_sa(period_s, 4)}\text{{ s}}\n"
        rf"3.\; \text{{An AC generator uses two continuous slip rings, whereas a DC generator uses a split-ring commutator. "
        rf"Induced emf is maximum when the coil plane is parallel to }}\vec{{B}}\text{{ (rate of cutting flux is greatest) and zero when the coil plane is perpendicular to }}\vec{{B}}\text{{.}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Mechanical energy to electrical energy", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Period T = 1/{freq_hz} = {_fmt_sa(period_s, 4)} s", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "AC uses slip rings; DC uses split-ring commutator", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Max emf when coil plane is parallel to B; zero emf when perpendicular to B", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Generators convert mechanical work into electrical energy via electromagnetic induction.",
        "tier_2": "AC generators use slip rings; DC generators use a split-ring commutator.",
        "tier_3": f"Period $T = 1/{freq_hz} = {_fmt_sa(period_s, 4)}\\text{{ s}}$. Max emf occurs when flux is zero (coil parallel to $\\vec{{B}}$) because $\\Delta\\Phi/\\Delta t$ is steepest.",
    }

    return {
        "id": f"ps_em_gen_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_gen_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "47_ac_generator_slip_rings_vs_dc_commutator",
        "learning_objective_id": "ps_em_47_generators",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_slip_rings_and_commutator", "claimed_max_emf_occurs_at_max_flux"],
        "keywords": ["AC generator", "slip rings", "split-ring commutator", "Faraday induction"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 48: Ideal step-up and step-down transformers
def _b48_step_up_and_step_down_transformer_turns_ratio(r: random.Random) -> Dict[str, Any]:
    vp = r.choice([220, 230, 240, 400, 1100])
    np = r.choice([200, 400, 500, 800, 1000, 1200])
    ns = r.choice([50, 100, 250, 1500, 2000, 3000])
    while ns == np:
        ns = r.choice([50, 100, 250, 1500, 2000, 3000])
    ip = r.choice([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0])

    vs = vp * (ns / np)
    is_curr = ip * (np / ns)
    t_type = "step-up" if ns > np else "step-down"

    prompt = (
        f"An ideal transformer has $N_p = {np}$ turns on its primary coil and $N_s = {ns}$ turns on its secondary coil. "
        f"An alternating potential difference of $V_p = {vp}\\text{{ V}}$ is applied across the primary coil, drawing a primary current of $I_p = {_fmt_sa(ip)}\\text{{ A}}$.\n\n"
        f"1. State whether this is a **step-up** or **step-down** transformer, and explain why a transformer requires alternating current (AC) rather than steady direct current (DC).\n"
        f"2. Calculate the secondary output voltage $V_s$.\n"
        f"3. Calculate the secondary current $I_s$ assuming $100\\%$ efficiency ($V_p I_p = V_s I_s$)."
    )

    ans_latex = (
        rf"1.\; \text{{{t_type.capitalize()} transformer (since }} N_s {' > ' if ns > np else ' < '} N_p\text{{). AC creates a continuously changing magnetic flux in the soft iron core required by Faraday's Law.}}\n"
        rf"2.\; \frac{{V_s}}{{V_p}} = \frac{{N_s}}{{N_p}} \implies V_s = {vp} \times \frac{{{ns}}}{{{np}}} = {_fmt_sa(vs, 2)}\text{{ V}}\n"
        rf"3.\; I_s = I_p \frac{{N_p}}{{N_s}} = {_fmt_sa(ip)} \times \frac{{{np}}}{{{ns}}} = {_fmt_sa(is_curr, 3)}\text{{ A}}"
    )

    marking_schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": f"Identify as {t_type} and explain AC creates changing flux", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate Vs = {_fmt_sa(vs, 2)} V", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Calculate Is = {_fmt_sa(is_curr, 3)} A", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Use the transformer turns-ratio equation: $\\frac{V_s}{V_p} = \\frac{N_s}{N_p} = \\frac{I_p}{I_s}$.",
        "tier_2": f"If $N_s > N_p$ it is step-up; if $N_s < N_p$ it is step-down. Here $N_s = {ns}$ and $N_p = {np}$.",
        "tier_3": f"$V_s = {_fmt_sa(vs, 2)}\\text{{ V}}$, $I_s = {_fmt_sa(is_curr, 3)}\\text{{ A}}$.",
    }

    return {
        "id": f"ps_em_trans_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_trans_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "48_step_up_and_step_down_transformer_turns_ratio",
        "learning_objective_id": "ps_em_48_transformers",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["assumed_transformer_works_on_steady_dc", "inverted_current_ratio"],
        "keywords": ["transformer", "turns ratio", "step-up", "step-down", "mutual induction"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 5,
    }


# Archetype 49: Multi-concept Electrostatics & Electromagnetism synthesis rider
def _b49_electrostatics_and_electromagnetism_synthesis_rider(r: random.Random) -> Dict[str, Any]:
    n_turns = r.choice([100, 120, 150, 200, 250])
    area_m2 = r.choice([0.02, 0.04, 0.05, 0.08])
    d_b = r.choice([0.30, 0.40, 0.50, 0.60, 0.80])
    dt = r.choice([0.05, 0.10, 0.20, 0.25])
    plate_d_mm = r.choice([4.0, 5.0, 8.0, 10.0])
    q_nc = r.choice([2.0, 3.0, 4.0, 5.0, 6.0])

    emf = n_turns * (d_b * area_m2) / dt
    e_field = emf / (plate_d_mm / 1000.0)
    f_elec = e_field * (q_nc * 1e-9)

    prompt = (
        f"A coil of $N = {n_turns}$ turns and area $A = {_fmt_sa(area_m2, 2)}\\text{{ m}}^2$ experiences a uniform change in perpendicular "
        f"magnetic flux density of $|\\Delta B| = {_fmt_sa(d_b, 2)}\\text{{ T}}$ in $\\Delta t = {_fmt_sa(dt, 2)}\\text{{ s}}$. "
        f"The ends of the coil are connected directly to two parallel metal plates separated by $d = {_fmt_sa(plate_d_mm)}\\text{{ mm}}$.\n\n"
        f"1. Calculate the magnitude of the induced emf $|\\varepsilon|$ generated across the coil.\n"
        f"2. Calculate the uniform electric field strength $E = \\frac{{|\\varepsilon|}}{{d}}$ between the parallel plates.\n"
        f"3. Calculate the electrostatic force $F_E = q E$ acting on a small dust particle carrying charge $q = +{_fmt_sa(q_nc)}\\text{{ nC}}$ between the plates."
    )

    ans_latex = (
        rf"1.\; |\varepsilon| = N \frac{{|\Delta B| A}}{{\Delta t}} = {n_turns} \times \frac{{{_fmt_sa(d_b, 2)} \times {_fmt_sa(area_m2, 2)}}}{{{_fmt_sa(dt, 2)}}} = {_fmt_sa(emf, 2)}\text{{ V}}\n"
        rf"2.\; E = \frac{{|\varepsilon|}}{{d}} = \frac{{{_fmt_sa(emf, 2)}}}{{{_fmt_sa(plate_d_mm/1000, 4)}}} = {_fmt_sci(e_field)}\text{{ N/C}}\n"
        rf"3.\; F_E = q E = ({_fmt_sa(q_nc)} \times 10^{{-9}})({_fmt_sci(e_field)}) = {_fmt_sci(f_elec)}\text{{ N}}"
    )

    marking_schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculate induced emf = {_fmt_sa(emf, 2)} V", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Calculate electric field E = {_fmt_sci(e_field)} N/C", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"Calculate electrostatic force FE = {_fmt_sci(f_elec)} N", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "omitted_mm_or_nC_conversion", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Step 1: Find $|\\varepsilon| = N \\frac{|\\Delta B| A}{\\Delta t}$. This emf acts as the voltage $V$ across the parallel plates.",
        "tier_2": "Step 2: Find the electric field between the plates $E = \\frac{|\\varepsilon|}{d}$ (convert mm to m).",
        "tier_3": f"Step 3: Multiply $E$ by $q = {_fmt_sa(q_nc)} \\times 10^{{-9}}\\text{{ C}}$ to obtain $F_E = {_fmt_sci(f_elec)}\\text{{ N}}$.",
    }

    return {
        "id": f"ps_em_synth_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_synth_{r.randint(100000, 999999)}",
        "topic": "Electromagnetism",
        "subskill": "49_electrostatics_and_electromagnetism_synthesis_rider",
        "learning_objective_id": "ps_em_49_synthesis_rider",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["failed_to_link_induced_emf_to_plate_voltage", "forgot_nano_or_milli_conversions"],
        "keywords": ["synthesis", "Faraday induction", "parallel plates", "electrostatic force"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 7,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 6,
    }


# Archetype 50: Diagnostic autopsy and misconception repair
def _b50_electrostatics_electromagnetism_diagnostic_autopsy(r: random.Random) -> Dict[str, Any]:
    q1_uc = r.choice([2.0, 3.0, 4.0, 5.0, 6.0])
    q2_uc = r.choice([4.0, 6.0, 8.0])
    r_cm = r.choice([10.0, 20.0, 25.0, 50.0])
    r_m = r_cm / 100.0

    wrong_f = K_COULOMB * (q1_uc * 1e-6) * (q2_uc * 1e-6) / r_m
    correct_f = K_COULOMB * (q1_uc * 1e-6) * (q2_uc * 1e-6) / (r_m ** 2)

    prompt = (
        f"A learner attempts to calculate the electrostatic force between two point charges "
        f"$Q_1 = +{_fmt_sa(q1_uc)}\\mu\\text{{C}}$ and $Q_2 = -{_fmt_sa(q2_uc)}\\mu\\text{{C}}$ separated by $r = {_fmt_sa(r_cm)}\\text{{ cm}}$ "
        f"and writes the following working:\n"
        f"$$F = \\frac{{(9{{,}}0 \\times 10^9)({_fmt_sa(q1_uc)} \\times 10^{{-6}})(-{_fmt_sa(q2_uc)} \\times 10^{{-6}})}}{{{_fmt_sa(r_m)}}} = -{_fmt_sa(wrong_f, 2)}\\text{{ N}}$$\n\n"
        f"1. Identify **two conceptual/mathematical errors** in the learner's substitution.\n"
        f"2. Write down the corrected calculation and state the magnitude and nature of the force."
    )

    ans_latex = (
        rf"1.\; \text{{Error 1: The learner omitted squaring the distance }} r \text{{ in the denominator (wrote }} r \text{{ instead of }} r^2\text{{). "
        rf"Error 2: The learner substituted the negative sign of }} Q_2 \text{{ into the vector magnitude formula.}}\n"
        rf"2.\; F = \frac{{(9{{,}}0 \times 10^9)({_fmt_sa(q1_uc)} \times 10^{{-6}})({_fmt_sa(q2_uc)} \times 10^{{-6}})}}{{({_fmt_sa(r_m)})^2}} = {_fmt_sa(correct_f, 2)}\text{{ N (attractive)}}"
    )

    marking_schema = {
        "total_marks": 4,
        "marking_points": [
            {"id": "mp1", "desc": "Identify omitted square on distance r^2", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Identify improper substitution of negative charge sign in magnitude calculation", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct force calculation: {_fmt_sa(correct_f, 2)} N (attractive)", "marks": 2, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Compare the learner's denominator and charge signs against $F = \\frac{k |Q_1 Q_2|}{r^2}$.",
        "tier_2": "Notice that the distance $r$ was not squared, and a negative sign was included in a magnitude formula.",
        "tier_3": f"Corrected force = {_fmt_sa(correct_f, 2)} N (attractive).",
    }

    return {
        "id": f"ps_em_diag_{r.randint(100000, 999999)}",
        "question_id": f"ps_em_diag_{r.randint(100000, 999999)}",
        "topic": "Electrostatics",
        "subskill": "50_electrostatics_electromagnetism_diagnostic_autopsy",
        "learning_objective_id": "ps_em_50_diagnostic_autopsy",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": ans_latex,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["omitted_square_on_distance", "substituted_charge_sign_into_coulomb_law"],
        "keywords": ["diagnostic autopsy", "error analysis", "Coulomb's Law"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "compound",
        "difficulty": "medium",
        "marks": 4,
    }


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_magnetic_field_around_straight_conductor": _b26_magnetic_field_around_straight_conductor,
    "27_magnetic_field_magnitude_straight_wire": _b27_magnetic_field_magnitude_straight_wire,
    "28_magnetic_field_current_loop": _b28_magnetic_field_current_loop,
    "29_solenoid_magnetic_field_polarity_and_factors": _b29_solenoid_magnetic_field_polarity_and_factors,
    "30_magnetic_flux_perpendicular_surface": _b30_magnetic_flux_perpendicular_surface,
    "31_magnetic_flux_angled_surface": _b31_magnetic_flux_angled_surface,
    "32_magnetic_flux_circular_coil": _b32_magnetic_flux_circular_coil,
    "33_magnetic_flux_rectangular_coil": _b33_magnetic_flux_rectangular_coil,
    "34_faradays_law_change_in_magnetic_field": _b34_faradays_law_change_in_magnetic_field,
    "35_faradays_law_change_in_coil_area": _b35_faradays_law_change_in_coil_area,
    "36_faradays_law_coil_rotation_half_turn": _b36_faradays_law_coil_rotation_half_turn,
    "37_faradays_law_coil_rotation_quarter_turn": _b37_faradays_law_coil_rotation_quarter_turn,
    "38_induced_current_in_closed_circuit": _b38_induced_current_in_closed_circuit,
    "39_induced_charge_flow_through_galvanometer": _b39_induced_charge_flow_through_galvanometer,
    "40_lenzs_law_bar_magnet_entering_solenoid": _b40_lenzs_law_bar_magnet_entering_solenoid,
    "41_lenzs_law_bar_magnet_leaving_solenoid": _b41_lenzs_law_bar_magnet_leaving_solenoid,
    "42_lenzs_law_current_loop_in_varying_field": _b42_lenzs_law_current_loop_in_varying_field,
    "43_motional_emf_conducting_rod_on_rails": _b43_motional_emf_conducting_rod_on_rails,
    "44_motional_emf_induced_current_and_magnetic_drag": _b44_motional_emf_induced_current_and_magnetic_drag,
    "45_magnetic_force_on_moving_charged_particle": _b45_magnetic_force_on_moving_charged_particle,
    "46_magnetic_force_on_current_carrying_conductor": _b46_magnetic_force_on_current_carrying_conductor,
    "47_ac_generator_slip_rings_vs_dc_commutator": _b47_ac_generator_slip_rings_vs_dc_commutator,
    "48_step_up_and_step_down_transformer_turns_ratio": _b48_step_up_and_step_down_transformer_turns_ratio,
    "49_electrostatics_and_electromagnetism_synthesis_rider": _b49_electrostatics_and_electromagnetism_synthesis_rider,
    "50_electrostatics_electromagnetism_diagnostic_autopsy": _b50_electrostatics_electromagnetism_diagnostic_autopsy,
}
