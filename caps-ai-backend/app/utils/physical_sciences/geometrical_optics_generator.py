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
        else:
            q = _generate_gr11_snell_optics(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
