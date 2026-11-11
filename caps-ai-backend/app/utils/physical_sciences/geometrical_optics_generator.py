"""Physical Sciences & Senior Phase Natural Sciences — Geometrical Optics & Wavefronts.
Covers Snell's Law, refractive index, critical angle, total internal reflection, and Huygens' diffraction.
Strictly complies with the 6-Pillar Generator Contract:
- Multi-grade vertical strand (Gr8 NS, Gr11 PS)
- Procedural seeded PRNG determinism (random.Random(seed))
- Atomic elementary sub-drills (mode="compound" | "elementary_*")
- Standardized misconception taxonomy
- Teacher-editable marking schema with [M] and [A] marks
- Deterministic 3-tier pre-baked hints
- South African comma decimal convention (",")
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

C_LIGHT = 3.0e8  # m/s in vacuum


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_gr8_visible_light(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 8 Natural Sciences: Properties of visible light, reflection, and spectrum."""
    colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
    medium = r.choice([
        ("water", 2.25e8),
        ("crown glass", 2.0e8),
        ("diamond", 1.24e8),
        ("perspex", 2.01e8),
    ])
    qid = _make_id("ns8_light", seed, idx)

    prompt = (
        f"Visible light is a form of electromagnetic radiation that travels as transverse waves.\n"
        f"In a vacuum or air, light travels at a speed of $3 \\times 10^8\\text{{ m/s}}$, but when passing into {medium[0]}, "
        f"its speed decreases to ${medium[1]:.2e}\\text{{ m/s}}$.\n\n"
        f"1. Explain what causes a ray of light to refract (bend) when it passes from air into {medium[0]}.\n"
        f"2. Arrange the following three colours of visible light in order of increasing frequency: {r.choice(colors)}, {r.choice(colors)}, {r.choice(colors)}."
    )
    ans_str = f"1. Change in wave speed as light enters an optically denser medium; 2. Red has lowest frequency, Violet has highest."
    memo = (
        f"1. Refraction occurs because the speed of light decreases when entering an optically denser medium ({medium[0]}), "
        f"causing the wave to change direction towards the normal line [2].\n"
        f"2. Frequency increases across the visible spectrum from Red (lowest frequency, longest wavelength) to Violet (highest frequency, shortest wavelength) [2]."
    )
    hints = {
        "tier_1": "Think about why a car veers when one wheel hits sand (speed changes). Remember ROYGBIV.",
        "tier_2": "Refraction is caused by a change in wave speed across mediums. Red has the lowest frequency; violet has the highest.",
        "tier_3": "1. Change in wave speed. 2. Red -> Orange -> Yellow -> Green -> Blue -> Indigo -> Violet.",
    }
    marks = 4

    return {
        "id": qid,
        "question_id": qid,
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["frequency_wavelength_relationship_inverted", "refraction_mechanism_misunderstood"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Refraction speed change explanation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Frequency ordering of visible spectrum", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr11_snell_optics(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11 Physical Sciences: Snell's Law, critical angle, and total internal reflection."""
    medium_data = r.choice([
        ("water", 1.33),
        ("crown glass", 1.52),
        ("flint glass", 1.66),
        ("diamond", 2.42),
        ("perspex", 1.49),
    ])
    med_name, n2 = medium_data
    n1 = 1.00  # air

    # Angle of incidence in air between 20 and 60 degrees
    theta1_deg = r.choice([25, 30, 35, 40, 45, 50, 60])
    theta1_rad = math.radians(theta1_deg)

    # Snell's Law: n1 * sin(theta1) = n2 * sin(theta2)
    sin_theta2 = (n1 * math.sin(theta1_rad)) / n2
    theta2_deg = math.degrees(math.asin(sin_theta2))

    # Critical angle when light travels from dense medium into air: sin(theta_c) = 1 / n2
    sin_thetac = 1.0 / n2
    thetac_deg = math.degrees(math.asin(sin_thetac))

    # Speed in medium: v = c / n2
    v_medium = C_LIGHT / n2

    qid = _make_id("ps11_optics", seed, idx)

    optics_spec = {
        "medium_1": {"name": "Air", "refractive_index": 1.00},
        "medium_2": {"name": med_name.title(), "refractive_index": n2},
        "angle_incidence_deg": theta1_deg,
        "angle_refraction_deg": round(theta2_deg, 1),
        "critical_angle_deg": round(thetac_deg, 1),
        "is_tir": False,
        "normal_line": True,
        "boundary_label": f"Air / {med_name.title()} Interface",
    }

    if mode == "elementary_snell_law":
        prompt = (
            f"A ray of monochromatic light travels through air ($n_1 = 1{{,}}00$) and strikes the flat surface of a "
            f"block of {med_name} ($n_2 = {_fmt_sa(n2)}$) at an angle of incidence of ${theta1_deg}^\\circ$ to the normal.\n\n"
            f"Calculate the angle of refraction ($\\theta_2$) of the light inside the {med_name}."
        )
        ans_str = f"theta_2 = {_fmt_sa(round(theta2_deg, 1))} degrees"
        memo = (
            f"1. Formula: $n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2$ [M]\n"
            f"2. Substitution: $(1{{,}}00) \\sin({theta1_deg}^\\circ) = ({_fmt_sa(n2)}) \\sin \\theta_2$ [M]\n"
            f"3. $\\sin \\theta_2 = \\frac{{\\sin({theta1_deg}^\\circ)}}{{{_fmt_sa(n2)}}} = {sin_theta2:.4f}$\n"
            f"4. Angle of refraction: $\\theta_2 = {_fmt_sa(round(theta2_deg, 1))}^\\circ$ [A]"
        )
        hints = {
            "tier_1": "Apply Snell's Law: $n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2$. Ensure your calculator is in DEGREE mode.",
            "tier_2": "Substitute: 1.00 * sin(" + f"{theta1_deg}) = {n2} * sin(theta_2). Solve for theta_2 = arcsin(sin_theta_2).",
            "tier_3": f"Calculate: sin(theta_2) = sin({theta1_deg}) / {n2} = {sin_theta2:.4f}. Then theta_2 = {_fmt_sa(round(theta2_deg, 1))} degrees.",
        }
        marks = 4
    elif mode == "elementary_critical_angle":
        prompt = (
            f"Light travels from inside a block of {med_name} ($n = {_fmt_sa(n2)}$) towards an air boundary ($n = 1{{,}}00$).\n\n"
            f"1. Define the term 'critical angle'.\n"
            f"2. Calculate the critical angle ($\\theta_c$) for the {med_name}-air boundary."
        )
        ans_str = f"1. Angle of incidence in optically denser medium yielding angle of refraction of 90 degrees; 2. theta_c = {_fmt_sa(round(thetac_deg, 1))} degrees"
        memo = (
            f"1. The critical angle is the angle of incidence in the optically denser medium for which the angle of refraction in the optically less dense medium is 90° [2].\n"
            f"2. Calculation [3]:\n"
            f"   $$\\sin \\theta_c = \\frac{{n_2}}{{n_1}} = \\frac{{1{{,}}00}}{{{_fmt_sa(n2)}}} = {sin_thetac:.4f}$$ [M]\n"
            f"   $$\\theta_c = \\sin^{{-1}}({sin_thetac:.4f}) = {_fmt_sa(round(thetac_deg, 1))}^\\circ$$ [A]"
        )
        hints = {
            "tier_1": "Critical angle occurs when theta_2 = 90 degrees: sin(theta_c) = n_air / n_medium.",
            "tier_2": "Formula: sin(theta_c) = 1.00 / n_medium.",
            "tier_3": f"sin(theta_c) = 1.00 / {n2} = {sin_thetac:.4f} -> theta_c = {_fmt_sa(round(thetac_deg, 1))} degrees.",
        }
        marks = 5
    else:
        # Full compound Gr11 question: Snell's Law + Speed of Light + Total Internal Reflection
        test_angle = int(thetac_deg + 10)
        prompt = (
            f"A ray of light traveling in air ($n = 1{{,}}00$) enters a triangular prism made of {med_name} "
            f"($n = {_fmt_sa(n2)}$) with an angle of incidence of ${theta1_deg}^\\circ$.\n\n"
            f"1. Calculate the speed of light inside the {med_name}.\n"
            f"2. Calculate the angle of refraction ($\\theta_2$) inside the prism.\n"
            f"3. Calculate the critical angle ($\\theta_c$) for the {med_name}-air interface.\n"
            f"4. State whether total internal reflection will occur if the ray strikes the internal prism-air boundary "
            f"at an angle of incidence of ${test_angle}^\\circ$, and give the two essential conditions required for total internal reflection."
        )
        ans_str = (
            f"1. v = {_fmt_sa(round(v_medium, 1))} m/s; "
            f"2. theta_2 = {_fmt_sa(round(theta2_deg, 1))} degrees; "
            f"3. theta_c = {_fmt_sa(round(thetac_deg, 1))} degrees; "
            f"4. Yes, TIR occurs because {test_angle} > {_fmt_sa(round(thetac_deg, 1))} degrees and traveling from denser to less dense medium."
        )
        memo = (
            f"1. Speed of light [2]: $v = \\frac{{c}}{{n}} = \\frac{{3 \\times 10^8}}{{{_fmt_sa(n2)}}} = {v_medium:.2e}\\text{{ m/s}}$ [A]\n"
            f"2. Angle of refraction [3]:\n"
            f"   $$n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2 \\implies (1{{,}}00)\\sin({theta1_deg}^\\circ) = ({_fmt_sa(n2)})\\sin \\theta_2$$\n"
            f"   $$\\theta_2 = \\sin^{{-1}}\\left(\\frac{{\\sin({theta1_deg}^\\circ)}}{{{_fmt_sa(n2)}}}\\right) = {_fmt_sa(round(theta2_deg, 1))}^\\circ$$ [A]\n"
            f"3. Critical angle [2]:\n"
            f"   $$\\sin \\theta_c = \\frac{{1}}{{{_fmt_sa(n2)}}} = {sin_thetac:.4f} \\implies \\theta_c = {_fmt_sa(round(thetac_deg, 1))}^\\circ$$ [A]\n"
            f"4. Total Internal Reflection [3]: Yes [1].\n"
            f"   Conditions: Light must travel from an optically denser medium to an optically less dense medium [1]; "
            f"   The angle of incidence (${test_angle}^\\circ$) must be greater than the critical angle (${_fmt_sa(round(thetac_deg, 1))}^\\circ$) [1]."
        )
        hints = {
            "tier_1": "Break into steps: v = c/n, then Snell's law, then sin(theta_c) = 1/n.",
            "tier_2": "TIR requires: 1. Optically denser to rarer medium. 2. Angle of incidence > critical angle.",
            "tier_3": f"1. v = {v_medium:.2e} m/s. 2. theta_2 = {_fmt_sa(round(theta2_deg, 1))} deg. 3. theta_c = {_fmt_sa(round(thetac_deg, 1))} deg. 4. Yes, TIR occurs.",
        }
        marks = 10

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "modality": "optics_ray",
        "diagram_spec": {
            "diagram_role": "context","kind": "ray_diagram", "optics": optics_spec},
        "optics_spec": optics_spec,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["normal_line_angle_confusion", "total_internal_reflection_condition_omitted", "snell_index_inversion"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Speed of light calculation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Snell's Law substitution and angle of refraction", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Critical angle calculation", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Total internal reflection conditions and verification", "marks": 3, "editable": True},
            ],
            "deductions": [{"rule": "omitted_units_degrees", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }




def _generate_gr11_thin_lens_ray_tracing(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11 Physical Sciences: Geometrical Optics thin lens equation, magnification, and 3-ray ray tracing."""
    f = r.choice([10.0, 12.0, 15.0, 20.0])
    
    # 3 classic exam configurations for converging biconvex lens
    case = r.choice(["beyond_2f", "between_f_and_2f", "at_2f"])
    if case == "beyond_2f":
        do = round(2.2 * f + r.choice([2.0, 4.0, 6.0]), 1)
        ho = round(r.choice([3.0, 4.0, 5.0]), 1)
    elif case == "between_f_and_2f":
        do = round(1.4 * f + r.choice([1.0, 2.0]), 1)
        ho = round(r.choice([2.5, 3.0, 4.0]), 1)
    else:
        do = round(2.0 * f, 1)
        ho = round(r.choice([3.0, 4.0]), 1)

    # 1/f = 1/do + 1/di => di = (f * do) / (do - f)
    di = round((f * do) / (do - f), 1)
    m = round(-di / do, 2)
    hi = round(m * ho, 1)

    if di > 0:
        if abs(m) < 0.95:
            nature = "Real, inverted, and diminished"
        elif abs(m) > 1.05:
            nature = "Real, inverted, and magnified"
        else:
            nature = "Real, inverted, and same size"
    else:
        nature = "Virtual, upright, and magnified"

    qid = _make_id("ps11_lens", seed, idx)

    optics_spec = {
        "type": "thin_lens",
        "lens_type": "converging",
        "focal_length_cm": f,
        "object_distance_cm": do,
        "object_height_cm": ho,
        "image_distance_cm": di,
        "image_height_cm": hi,
        "magnification": m,
        "image_nature": nature,
    }

    prompt = (
        f"An object of height **${_fmt_sa(ho)}\\text{{ cm}}$** is placed perpendicular to the principal axis at a distance "
        f"of **${_fmt_sa(do)}\\text{{ cm}}$** in front of a thin converging (convex) lens with a focal length of **${_fmt_sa(f)}\\text{{ cm}}$**.\n\n"
        f"1. Use the thin lens equation $\\frac{{1}}{{f}} = \\frac{{1}}{{d_o}} + \\frac{{1}}{{d_i}}$ to calculate the image distance ($d_i$).\n"
        f"2. Calculate the linear magnification ($m$) and determine the height of the image ($h_i$).\n"
        f"3. State the THREE characteristics of the image formed (nature, orientation, and size relative to the object).\n"
        f"4. Describe the paths of the three standard principal rays used in geometric ray construction to locate the image."
    )

    ans_str = (
        f"1. di = {_fmt_sa(di)} cm; "
        f"2. m = {_fmt_sa(m)}, hi = {_fmt_sa(hi)} cm; "
        f"3. {nature}; "
        f"4. Ray 1: Parallel to axis refracts through F2; Ray 2: Passes through optical centre O undeviated; Ray 3: Through F1 refracts parallel to axis."
    )

    memo = (
        f"1. Image distance [3]:\n"
        f"   $$\\frac{{1}}{{f}} = \\frac{{1}}{{d_o}} + \\frac{{1}}{{d_i}} \\implies \\frac{{1}}{{{_fmt_sa(f)}}} = \\frac{{1}}{{{_fmt_sa(do)}}} + \\frac{{1}}{{d_i}}$$\n"
        f"   $$\\frac{{1}}{{d_i}} = \\frac{{1}}{{{_fmt_sa(f)}}} - \\frac{{1}}{{{_fmt_sa(do)}}} = \\frac{{{_fmt_sa(do)} - {_fmt_sa(f)}}}{{{_fmt_sa(f)} \\times {_fmt_sa(do)}}}$$\n"
        f"   $$d_i = \\frac{{{_fmt_sa(f)} \\times {_fmt_sa(do)}}}{{{_fmt_sa(do)} - {_fmt_sa(f)}}} = {_fmt_sa(di)}\\text{{ cm}}$$ [A]\n"
        f"2. Magnification & Image height [2]:\n"
        f"   $$m = -\\frac{{d_i}}{{d_o}} = -\\frac{{{_fmt_sa(di)}}}{{{_fmt_sa(do)}}} = {_fmt_sa(m)}$$ [M]\n"
        f"   $$h_i = m \\times h_o = ({_fmt_sa(m)}) \\times {_fmt_sa(ho)} = {_fmt_sa(hi)}\\text{{ cm}}$$ [A]\n"
        f"3. Image characteristics [3]: **{nature}** (positive $d_i$ indicates a real image formed on the opposite side of the lens; negative $m$ indicates an inverted image).\n"
        f"4. Principal ray construction [3]:\n"
        f"   - Ray 1 (Red): Incident parallel to the principal axis, refracts through the principal focus $F_2$.\n"
        f"   - Ray 2 (Blue): Incident through the optical centre $O$, passes straight through without deviation.\n"
        f"   - Ray 3 (Emerald): Incident through the front focus $F_1$, refracts parallel to the principal axis."
    )

    hints = {
        "tier_1": "Recall the thin lens equation: $\\frac{1}{f} = \\frac{1}{d_o} + \\frac{1}{d_i}$. Solve for $\\frac{1}{d_i}$.",
        "tier_2": f"Substitute: 1/{f} = 1/{do} + 1/di. Find common denominator. Then $m = -d_i / d_o$.",
        "tier_3": f"1. di = {f}*{do} / ({do} - {f}) = {_fmt_sa(di)} cm. 2. m = {_fmt_sa(m)}, hi = {_fmt_sa(hi)} cm. 3. {nature}.",
    }

    marks = 11

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "compound",
        "modality": "optics_ray",
        "diagram_spec": {
            "diagram_role": "context","kind": "ray_diagram", "optics": optics_spec},
        "optics_spec": optics_spec,
        "question": prompt,
        "prompt": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "sub_parts": [
            {"part": "1", "label": "1. Image distance (di)", "prompt": "Calculate the image distance (di) in cm.", "expected_answer": _fmt_sa(di), "marks": 3},
            {"part": "2", "label": "2. Magnification & Image height", "prompt": "Calculate linear magnification (m) and image height (hi).", "expected_answer": f"m = {_fmt_sa(m)}, hi = {_fmt_sa(hi)} cm", "marks": 2},
            {"part": "3", "label": "3. Image characteristics", "prompt": "State the three characteristics of the image formed.", "expected_answer": nature, "marks": 3},
            {"part": "4", "label": "4. Principal rays", "prompt": "Describe the three standard rays used to locate the image.", "expected_answer": "Ray 1 parallel->F2, Ray 2 through O undeviated, Ray 3 through F1->parallel", "marks": 3},
        ],
        "hints": hints,
        "misconception_tags": ["lens_reciprocal_addition_error", "confused_real_and_virtual_image", "inverted_magnification_ratio"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Thin lens equation formula and correct di calculation", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Magnification and image height calculation", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Three correct image characteristics (nature, orientation, size)", "marks": 3, "editable": True},
                {"id": "mp_4", "desc": "Three standard principal ray rules described", "marks": 3, "editable": True},
            ],
            "deductions": [{"rule": "reciprocal_addition_error", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: str = "11",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Geometrical Optics & Wavefronts."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    grade_num = "".join(ch for ch in str(grade) if ch.isdigit()) or "11"

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if grade_num in ("7", "8") or subskill in ("visible_light", "spectrum", "reflection_gr8"):
            q = _generate_gr8_visible_light(sub_r, sub_seed, i, mode)
        elif subskill in ("thin_lens", "lenses", "ray_tracing") or mode in ("elementary_thin_lens", "thin_lens"):
            q = _generate_gr11_thin_lens_ray_tracing(sub_r, sub_seed, i, mode)
        else:
            # Alternating or mixed mode for Grade 11 Optics
            s_val = (int(seed or 0) + i) if seed is not None else sub_r.randint(0, 10000)
            if s_val % 2 == 1:
                q = _generate_gr11_thin_lens_ray_tracing(sub_r, sub_seed, i, mode)
            else:
                q = _generate_gr11_snell_optics(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
