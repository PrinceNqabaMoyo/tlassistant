"""Grade 11 Physical Sciences: Geometrical Optics (Subskills 01–25)
Focus: Reflection, Refraction, Snell's Law, Critical Angles, Total Internal Reflection (TIR), Prisms & Lenses.

Complies strictly with the 6-Pillar Generator Contract:
- Seed-deterministic via random.Random(seed)
- South African comma decimal convention ({{,}})
- Zero curriculum trademarks (CAPS/IEB/DBE/NSC)
- Valid DiagramRenderer inline_svg specifications with dynamic seed variation
- Teacher-editable marking schema with [M] and [A] marks
- Deterministic 3-tier pre-baked hints
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

C_LIGHT = 3.0e8  # m/s in vacuum or air


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    """Format float with South African comma decimal separator."""
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


# ==============================================================================
# SUBSKILL 01: Rectilinear propagation and shadow formation
# ==============================================================================
def builder_01_rectilinear_propagation_and_shadow_formation(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    obj_h = rng.choice([10, 15, 20, 25])
    d_src_obj = rng.choice([30, 40, 50, 60])
    d_obj_screen = rng.choice([60, 80, 100, 120])
    d_total = d_src_obj + d_obj_screen
    shadow_h = round(obj_h * (d_total / d_src_obj), 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <circle cx="50" cy="120" r="8" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
  <text x="35" y="145" font-size="11" fill="#475569" font-family="sans-serif">Point Source</text>
  <line x1="200" y1="{120 - obj_h*2}" x2="200" y2="{120 + obj_h*2}" stroke="#1e293b" stroke-width="6"/>
  <text x="180" y="70" font-size="11" fill="#1e293b" font-family="sans-serif">Object ({obj_h} cm)</text>
  <line x1="420" y1="20" x2="420" y2="220" stroke="#64748b" stroke-width="4"/>
  <text x="430" y="50" font-size="11" fill="#475569" font-family="sans-serif">Screen</text>
  <line x1="50" y1="120" x2="420" y2="{120 - shadow_h*1.2}" stroke="#f97316" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="50" y1="120" x2="420" y2="{120 + shadow_h*1.2}" stroke="#f97316" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="420" y1="{120 - shadow_h*1.2}" x2="420" y2="{120 + shadow_h*1.2}" stroke="#dc2626" stroke-width="6"/>
  <text x="430" y="125" font-size="11" fill="#dc2626" font-family="sans-serif">Umbra ({_fmt_sa(shadow_h)} cm)</text>
</svg>"""

    prompt = (
        f"A point source of light illuminates an opaque vertical barrier of height **${obj_h}\\text{{ cm}}$**. "
        f"The obstacle is positioned at distance **${d_src_obj}\\text{{ cm}}$** from the light source, "
        f"and a display screen stands **${d_obj_screen}\\text{{ cm}}$** further back.\n\n"
        f"1. State the property of light demonstrated by the formation of sharp shadows.\n"
        f"2. Use similar geometric triangles to calculate the height of the shadow (umbra) cast on the screen in centimetres."
    )
    ans = f"1. Rectilinear propagation (light travels in straight lines); 2. Height = {_fmt_sa(shadow_h)} cm"
    memo = (
        f"1. Property [1]: Rectilinear propagation (light travels in straight lines through a uniform medium).\n"
        f"2. Geometric ratio [3]:\n"
        f"   $$\\frac{{\\text{{Height of shadow}}}}{{\\text{{Height of object}}}} = \\frac{{\\text{{Total distance to screen}}}}{{\\text{{Distance to object}}}}\n"
        f"   \\implies \\frac{{h_s}}{{{obj_h}}} = \\frac{{{d_src_obj} + {d_obj_screen}}}{{{d_src_obj}}} = \\frac{{{d_total}}}{{{d_src_obj}}}$$\n"
        f"   $$h_s = {obj_h} \\times \\frac{{{d_total}}}{{{d_src_obj}}} = {_fmt_sa(shadow_h)}\\text{{ cm}}$$ [A]"
    )
    return {
        "id": _make_id("optics_01", seed, 1),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Light travels in straight lines in a uniform medium.",
            "tier_2": f"Set up the proportion: Shadow / Object = ({d_src_obj} + {d_obj_screen}) / {d_src_obj}.",
            "tier_3": f"Shadow height = {obj_h} * ({d_total} / {d_src_obj}) = {_fmt_sa(shadow_h)} cm.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["rectilinear_propagation_misunderstood", "shadow_ratio_subtraction_error"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Statement of rectilinear propagation", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Proportional triangle formula ratio", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Final shadow height with unit", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 02: Law of reflection plane mirror
# ==============================================================================
def builder_02_law_of_reflection_plane_mirror(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    angle_glance = rng.choice([25, 30, 35, 40, 45, 55])
    angle_inc = 90 - angle_glance
    angle_ref = angle_inc
    total_dev = 180 - 2 * angle_inc

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="80" y1="180" x2="420" y2="180" stroke="#0f172a" stroke-width="4"/>
  <line x1="250" y1="30" x2="250" y2="180" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="2"/>
  <text x="255" y="50" font-size="11" fill="#64748b" font-family="sans-serif">Normal</text>
  <line x1="130" y1="70" x2="250" y2="180" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="250" y1="180" x2="370" y2="70" stroke="#dc2626" stroke-width="2.5"/>
  <text x="160" y="170" font-size="11" fill="#2563eb" font-family="sans-serif">{angle_glance}&deg; to mirror</text>
  <text x="215" y="110" font-size="11" fill="#2563eb" font-family="sans-serif">&theta;i</text>
  <text x="270" y="110" font-size="11" fill="#dc2626" font-family="sans-serif">&theta;r</text>
  <text x="220" y="210" font-size="12" fill="#0f172a" font-weight="bold" font-family="sans-serif">Plane Mirror</text>
</svg>"""

    prompt = (
        f"A light ray strikes a flat plane mirror such that the angle between the incident ray and the mirror surface "
        f"is **${angle_glance}^\\circ$**.\n\n"
        f"1. State the Law of Reflection.\n"
        f"2. Determine the angle of incidence ($\\theta_i$).\n"
        f"3. State the angle of reflection ($\\theta_r$).\n"
        f"4. Calculate the total angle of deviation of the ray from its original path."
    )
    ans = f"1. Angle of incidence equals angle of reflection; 2. theta_i = {angle_inc} deg; 3. theta_r = {angle_ref} deg; 4. Deviation = {total_dev} deg"
    memo = (
        f"1. Law of Reflection [1]: The angle of incidence is equal to the angle of reflection, and the incident ray, reflected ray, and normal all lie in the same plane.\n"
        f"2. Angle of incidence [1]: Measured to the normal: $\\theta_i = 90^\\circ - {angle_glance}^\\circ = {angle_inc}^\\circ$ [A]\n"
        f"3. Angle of reflection [1]: $\\theta_r = \\theta_i = {angle_ref}^\\circ$ [A]\n"
        f"4. Angle of deviation [1]: $\\delta = 180^\\circ - 2\\theta_i = 180^\\circ - 2({angle_inc}^\\circ) = {total_dev}^\\circ$ [A]"
    )
    return {
        "id": _make_id("optics_02", seed, 2),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Angles of incidence and reflection are always measured relative to the normal line (perpendicular to mirror).",
            "tier_2": f"Normal is at 90 degrees. So angle of incidence = 90 - {angle_glance}.",
            "tier_3": f"theta_i = {angle_inc} deg, theta_r = {angle_ref} deg, deviation = 180 - 2*{angle_inc} = {total_dev} deg.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["glancing_angle_confused_with_incidence_angle", "law_of_reflection_inverted"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Statement of Law of Reflection", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Angle of incidence calculated relative to normal", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Angle of reflection stated", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Angle of deviation calculated", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 03: Refractive index and wave speed
# ==============================================================================
def builder_03_refractive_index_and_wave_speed(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    medium, n_val = rng.choice([
        ("water", 1.33),
        ("crown glass", 1.52),
        ("flint glass", 1.66),
        ("diamond", 2.42),
        ("perspex", 1.49),
        ("zircon", 1.92),
    ])
    v_med = C_LIGHT / n_val
    v_sci = f"{v_med / 1e8:.2f}".replace(".", ",") + " \\times 10^8"

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="110" width="400" height="110" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
  <text x="60" y="80" font-size="13" fill="#0369a1" font-weight="bold" font-family="sans-serif">Air (n = 1,00, c = 3,00 &times; 10&sup8; m/s)</text>
  <text x="60" y="145" font-size="13" fill="#0f172a" font-weight="bold" font-family="sans-serif">{medium.title()} (n = {_fmt_sa(n_val)})</text>
  <line x1="250" y1="30" x2="250" y2="210" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="150" y1="40" x2="250" y2="110" stroke="#2563eb" stroke-width="3"/>
  <line x1="250" y1="110" x2="310" y2="210" stroke="#2563eb" stroke-width="3"/>
</svg>"""

    prompt = (
        f"Light travels from air ($c = 3{{,}}00 \\times 10^8\\text{{ m/s}}$) into a block of **{medium}** with a "
        f"refractive index of **${_fmt_sa(n_val)}$**.\n\n"
        f"1. Define the term 'refractive index' of a medium.\n"
        f"2. Calculate the speed of light inside the {medium} in $\\text{{m/s}}$."
    )
    ans = f"1. Ratio of speed of light in vacuum to speed in medium (n = c/v); 2. v = {v_sci} m/s"
    memo = (
        f"1. Definition [2]: Refractive index is the ratio of the speed of light in a vacuum (or air) to the speed of light in the optical medium ($n = c/v$).\n"
        f"2. Speed calculation [3]:\n"
        f"   $$n = \\frac{{c}}{{v}} \\implies v = \\frac{{c}}{{n}}$$ [M]\n"
        f"   $$v = \\frac{{3{{,}}00 \\times 10^8}}{{{_fmt_sa(n_val)}}} = {v_sci}\\text{{ m/s}}$$ [A]"
    )
    return {
        "id": _make_id("optics_03", seed, 3),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Recall the defining equation: $n = c / v$.",
            "tier_2": f"Rearrange to solve for v: $v = c / n = 3.00 \\times 10^8 / {_fmt_sa(n_val)}$.",
            "tier_3": f"v = {v_sci} m/s.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["refractive_index_formula_inverted", "speed_of_light_unit_conversion_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Definition of refractive index", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Formula n = c/v rearranged", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Correct substitution and answer with units", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 04: Wavelength change in refraction frequency constant
# ==============================================================================
def builder_04_wavelength_change_in_refraction_frequency_constant(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    lambda_air_nm = rng.choice([450, 500, 550, 600, 650])
    n_val = rng.choice([1.33, 1.49, 1.52, 1.66])
    f_hz = C_LIGHT / (lambda_air_nm * 1e-9)
    f_sci = f"{f_hz / 1e14:.2f}".replace(".", ",") + " \\times 10^{14}"
    lambda_med_nm = round(lambda_air_nm / n_val, 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="40" y="120" width="420" height="100" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
  <text x="60" y="70" font-size="12" fill="#1e293b" font-weight="bold" font-family="sans-serif">Air: &lambda; = {lambda_air_nm} nm</text>
  <text x="60" y="170" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Medium (n = {_fmt_sa(n_val)}): &lambda; = {_fmt_sa(lambda_med_nm)} nm</text>
  <path d="M 80,90 Q 95,70 110,90 T 140,90 T 170,90 T 200,90" fill="none" stroke="#e11d48" stroke-width="2.5"/>
  <path d="M 80,180 Q 90,165 100,180 T 120,180 T 140,180 T 160,180 T 180,180" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  <text x="220" y="95" font-size="11" fill="#e11d48" font-family="sans-serif">Longer &lambda; in air</text>
  <text x="220" y="185" font-size="11" fill="#2563eb" font-family="sans-serif">Shorter &lambda; in medium (compressed wave)</text>
</svg>"""

    prompt = (
        f"Monochromatic light of wavelength **${lambda_air_nm}\\text{{ nm}}$** in air enters a transparent substance "
        f"with refractive index **${_fmt_sa(n_val)}$**.\n\n"
        f"1. Explain why the frequency of light remains constant when it refracts into the medium.\n"
        f"2. Calculate the frequency ($f$) of the light wave in $\\text{{Hz}}$.\n"
        f"3. Calculate the wavelength ($\\lambda$) of the light inside the substance in nanometres ($\\text{{nm}}$)."
    )
    ans = f"1. Frequency is determined by the source oscillation; 2. f = {f_sci} Hz; 3. lambda = {_fmt_sa(lambda_med_nm)} nm"
    memo = (
        f"1. Explanation [1]: The frequency of a wave is determined solely by the source that emitted it and does not change when crossing boundaries.\n"
        f"2. Frequency calculation [3]:\n"
        f"   $$c = f \\lambda \\implies f = \\frac{{c}}{{\\lambda}} = \\frac{{3{{,}}00 \\times 10^8}}{{{lambda_air_nm} \\times 10^{{-9}}}} = {f_sci}\\text{{ Hz}}$$ [A]\n"
        f"3. Wavelength in medium [2]:\n"
        f"   $$\\lambda_{{\\text{{med}}}} = \\frac{{\\lambda_{{\\text{{air}}}}}}{{n}} = \\frac{{{lambda_air_nm}}}{{{_fmt_sa(n_val)}}} = {_fmt_sa(lambda_med_nm)}\\text{{ nm}}$$ [A]"
    )
    return {
        "id": _make_id("optics_04", seed, 4),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "hints": {
            "tier_1": "Frequency depends on the source, not the medium. Use $v = f \\lambda$.",
            "tier_2": f"In air: $c = f \\lambda_0$. In medium: $\\lambda = \\lambda_0 / n$.",
            "tier_3": f"f = {f_sci} Hz, lambda = {lambda_air_nm} / {n_val} = {_fmt_sa(lambda_med_nm)} nm.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["frequency_changes_during_refraction", "wavelength_dilation_error"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Explanation of frequency conservation", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Frequency formula and calculation", "marks": 3, "editable": True},
                {"id": "mp3", "desc": "Wavelength in medium calculation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 05: Optical density and ray bending towards/away from normal
# ==============================================================================
def builder_05_optical_density_and_ray_bending_towards_away_normal(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    scenarios = [
        ("air (n=1,00)", "water (n=1,33)", "towards the normal", "decreases", "optically denser"),
        ("glass (n=1,52)", "air (n=1,00)", "away from the normal", "increases", "optically less dense"),
        ("water (n=1,33)", "diamond (n=2,42)", "towards the normal", "decreases", "optically denser"),
        ("perspex (n=1,49)", "water (n=1,33)", "away from the normal", "increases", "optically less dense"),
    ]
    med1, med2, bend, speed_change, dense_desc = rng.choice(scenarios)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="120" width="400" height="100" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>
  <line x1="250" y1="20" x2="250" y2="220" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <text x="255" y="40" font-size="11" fill="#64748b" font-family="sans-serif">Normal</text>
  <text x="60" y="80" font-size="12" fill="#1e293b" font-weight="bold" font-family="sans-serif">Medium 1: {med1}</text>
  <text x="60" y="160" font-size="12" fill="#1e293b" font-weight="bold" font-family="sans-serif">Medium 2: {med2}</text>
  <line x1="160" y1="50" x2="250" y2="120" stroke="#0284c7" stroke-width="3"/>
  <line x1="250" y1="120" x2="{310 if 'towards' in bend else 360}" y2="200" stroke="#0284c7" stroke-width="3"/>
</svg>"""

    prompt = (
        f"A ray of light traveling obliquely passes across the boundary from **{med1}** into **{med2}**.\n\n"
        f"1. Contrast optical density with physical (mass) density.\n"
        f"2. State whether the speed of light increases or decreases as it crosses into medium 2.\n"
        f"3. State whether the refracted ray bends **towards the normal** or **away from the normal**, and provide the scientific reason."
    )
    ans = f"1. Optical density measures how much medium slows light, physical density is mass per volume; 2. Speed {speed_change}; 3. Bends {bend} because medium 2 is {dense_desc}."
    memo = (
        f"1. Density contrast [2]: Optical density is a measure of the speed at which light travels through a substance (related to refractive index), "
        f"whereas physical density is mass per unit volume ($\\rho = m/V$).\n"
        f"2. Speed change [1]: The speed of light **{speed_change}** in medium 2.\n"
        f"3. Bending direction and reason [2]: The ray bends **{bend}** because medium 2 is **{dense_desc}** than medium 1, "
        f"causing the wave front to alter speed and change direction [A]."
    )
    return {
        "id": _make_id("optics_05", seed, 5),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Light bends TOWARDS the normal when entering an optically denser medium (slower speed).",
            "tier_2": f"Check refractive indices: {med1} vs {med2}. Denser medium slows light down.",
            "tier_3": f"Speed {speed_change}, bends {bend}.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["optical_vs_mass_density_confusion", "normal_bending_direction_inverted"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Optical vs physical density distinction", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Speed change correctly identified", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Ray bending direction and explanation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 06: Snell's Law solve angle of refraction
# ==============================================================================
def builder_06_snells_law_solve_angle_of_refraction(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n1 = 1.00  # air
    n2 = rng.choice([1.33, 1.49, 1.52, 1.66])
    theta1 = rng.choice([30, 40, 45, 50, 60])
    sin_theta2 = (n1 * math.sin(math.radians(theta1))) / n2
    theta2 = math.degrees(math.asin(sin_theta2))

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="120" width="400" height="100" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
  <line x1="250" y1="20" x2="250" y2="220" stroke="#64748b" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="130" y1="50" x2="250" y2="120" stroke="#1d4ed8" stroke-width="3"/>
  <line x1="250" y1="120" x2="{250 + int(90 * math.sin(math.radians(theta2)))}" y2="{120 + int(90 * math.cos(math.radians(theta2)))}" stroke="#1d4ed8" stroke-width="3"/>
  <text x="210" y="80" font-size="12" fill="#1d4ed8" font-family="sans-serif">&theta;1 = {theta1}&deg;</text>
  <text x="260" y="170" font-size="12" fill="#0369a1" font-family="sans-serif">&theta;2 = ?</text>
  <text x="60" y="70" font-size="12" fill="#475569" font-family="sans-serif">Air (n1 = 1,00)</text>
  <text x="60" y="150" font-size="12" fill="#0369a1" font-family="sans-serif">Medium (n2 = {_fmt_sa(n2)})</text>
</svg>"""

    prompt = (
        f"A ray of light traveling in air ($n_1 = 1{{,}}00$) strikes the flat surface of a transparent medium "
        f"($n_2 = {_fmt_sa(n2)}$) at an angle of incidence of **${theta1}^\\circ$**.\n\n"
        f"1. State Snell's Law in words or as a formula.\n"
        f"2. Calculate the angle of refraction ($\\theta_2$) of the ray inside the medium in degrees."
    )
    ans = f"1. n1 sin(theta1) = n2 sin(theta2); 2. theta2 = {_fmt_sa(round(theta2, 1))} degrees"
    memo = (
        f"1. Formula [1]: $n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2$ [M]\n"
        f"2. Calculation [3]:\n"
        f"   $$(1{{,}}00) \\sin({theta1}^\\circ) = ({_fmt_sa(n2)}) \\sin \\theta_2$$\n"
        f"   $$\\sin \\theta_2 = \\frac{{\\sin({theta1}^\\circ)}}{{{_fmt_sa(n2)}}} = \\frac{{{math.sin(math.radians(theta1)):.4f}}}{{{_fmt_sa(n2)}}} = {sin_theta2:.4f}$$\n"
        f"   $$\\theta_2 = \\sin^{{-1}}({sin_theta2:.4f}) = {_fmt_sa(round(theta2, 1))}^\\circ$$ [A]"
    )
    return {
        "id": _make_id("optics_06", seed, 6),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Snell's Law: $n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2$.",
            "tier_2": f"$\\sin \\theta_2 = (1.00 \\times \\sin({theta1}^\\circ)) / {_fmt_sa(n2)}$.",
            "tier_3": f"$\\theta_2 = \\arcsin({sin_theta2:.4f}) = {_fmt_sa(round(theta2, 1))}^\\circ$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["snells_law_calculator_radian_mode", "snells_law_ratio_inverted"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Snell's law formula stated", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct substitution into formula", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Angle of refraction calculated with degrees unit", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 07: Snell's Law solve angle of incidence
# ==============================================================================
def builder_07_snells_law_solve_angle_of_incidence(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n1 = 1.00
    n2 = rng.choice([1.33, 1.50, 1.54, 1.62])
    theta2 = rng.choice([20, 25, 30, 35])
    sin_theta1 = (n2 * math.sin(math.radians(theta2))) / n1
    theta1 = math.degrees(math.asin(sin_theta1))

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="120" width="400" height="100" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <line x1="250" y1="20" x2="250" y2="220" stroke="#64748b" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="{250 - int(90 * math.sin(math.radians(theta1)))}" y1="{120 - int(90 * math.cos(math.radians(theta1)))}" x2="250" y2="120" stroke="#0284c7" stroke-width="3"/>
  <line x1="250" y1="120" x2="{250 + int(90 * math.sin(math.radians(theta2)))}" y2="{120 + int(90 * math.cos(math.radians(theta2)))}" stroke="#0284c7" stroke-width="3"/>
  <text x="180" y="60" font-size="12" fill="#0284c7" font-family="sans-serif">&theta;1 = ?</text>
  <text x="260" y="170" font-size="12" fill="#0369a1" font-family="sans-serif">&theta;2 = {theta2}&deg;</text>
  <text x="60" y="60" font-size="12" fill="#475569" font-family="sans-serif">Air (n1 = 1,00)</text>
  <text x="60" y="150" font-size="12" fill="#0369a1" font-family="sans-serif">Glass (n2 = {_fmt_sa(n2)})</text>
</svg>"""

    prompt = (
        f"A light ray enters a glass slab of refractive index **${_fmt_sa(n2)}$** from air ($n_1 = 1{{,}}00$). "
        f"The angle of refraction inside the glass is measured to be **${theta2}^\\circ$**.\n\n"
        f"Calculate the angle of incidence ($\\theta_1$) in air."
    )
    ans = f"theta1 = {_fmt_sa(round(theta1, 1))} degrees"
    memo = (
        f"1. Snell's Law [1]: $n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2$ [M]\n"
        f"2. Substitution [2]:\n"
        f"   $$(1{{,}}00) \\sin \\theta_1 = ({_fmt_sa(n2)}) \\sin({theta2}^\\circ)$$\n"
        f"   $$\\sin \\theta_1 = {_fmt_sa(n2)} \\times {math.sin(math.radians(theta2)):.4f} = {sin_theta1:.4f}$$\n"
        f"3. Angle of incidence [1]:\n"
        f"   $$\\theta_1 = \\sin^{{-1}}({sin_theta1:.4f}) = {_fmt_sa(round(theta1, 1))}^\\circ$$ [A]"
    )
    return {
        "id": _make_id("optics_07", seed, 7),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Snell's Law: $n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2$. Solve for $\\sin \\theta_1$.",
            "tier_2": f"$\\sin \\theta_1 = {_fmt_sa(n2)} \\times \\sin({theta2}^\\circ)$.",
            "tier_3": f"$\\theta_1 = \\arcsin({sin_theta1:.4f}) = {_fmt_sa(round(theta1, 1))}^\\circ$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["snell_variable_isolation_error", "trig_inverse_sine_miscalculated"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Snell's law formula", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Substitution and evaluation of sin(theta1)", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Final angle with degree unit", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 08: Snell's Law solve refractive index of unknown medium
# ==============================================================================
def builder_08_snells_law_solve_refractive_index_of_unknown_medium(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    theta1 = rng.choice([40, 45, 50, 60])
    target_n = rng.choice([1.36, 1.44, 1.55, 1.70, 2.10])
    sin_theta2 = math.sin(math.radians(theta1)) / target_n
    theta2 = round(math.degrees(math.asin(sin_theta2)), 1)
    calc_n = round(math.sin(math.radians(theta1)) / math.sin(math.radians(theta2)), 2)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="120" width="400" height="100" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
  <line x1="250" y1="20" x2="250" y2="220" stroke="#64748b" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="140" y1="40" x2="250" y2="120" stroke="#d97706" stroke-width="3"/>
  <line x1="250" y1="120" x2="{250 + int(90 * math.sin(math.radians(theta2)))}" y2="{120 + int(90 * math.cos(math.radians(theta2)))}" stroke="#d97706" stroke-width="3"/>
  <text x="180" y="80" font-size="12" fill="#b45309" font-family="sans-serif">&theta;1 = {theta1}&deg;</text>
  <text x="260" y="170" font-size="12" fill="#b45309" font-family="sans-serif">&theta;2 = {_fmt_sa(theta2)}&deg;</text>
  <text x="60" y="70" font-size="12" fill="#475569" font-family="sans-serif">Air (n1 = 1,00)</text>
  <text x="60" y="150" font-size="12" fill="#b45309" font-weight="bold" font-family="sans-serif">Unknown Liquid (n2 = ?)</text>
</svg>"""

    prompt = (
        f"In an experiment to identify an unknown transparent liquid, a laser beam traveling in air ($n_1 = 1{{,}}00$) "
        f"strikes the liquid surface at an angle of incidence of **${theta1}^\\circ$**. "
        f"The measured angle of refraction is **${_fmt_sa(theta2)}^\\circ$**.\n\n"
        f"1. Use Snell's Law to calculate the refractive index ($n_2$) of the unknown liquid.\n"
        f"2. Explain why refractive index has no physical units."
    )
    ans = f"1. n2 = {_fmt_sa(calc_n)}; 2. It is a ratio of identical quantities (speeds or sines of angles), making it dimensionless."
    memo = (
        f"1. Calculation [3]:\n"
        f"   $$n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2 \\implies n_2 = \\frac{{n_1 \\sin \\theta_1}}{{\\sin \\theta_2}}$$ [M]\n"
        f"   $$n_2 = \\frac{{(1{{,}}00) \\sin({theta1}^\\circ)}}{{\\sin({_fmt_sa(theta2)}^\\circ)}} = \\frac{{{math.sin(math.radians(theta1)):.4f}}}{{{math.sin(math.radians(theta2)):.4f}}} = {_fmt_sa(calc_n)}$$ [A]\n"
        f"2. Unit explanation [1]: Refractive index is a dimensionless ratio of two speeds ($n = c/v$), so units cancel out [A]."
    )
    return {
        "id": _make_id("optics_08", seed, 8),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "$n_2 = (n_1 \\sin \\theta_1) / \\sin \\theta_2$.",
            "tier_2": f"Substitute: $\\sin({theta1}^\\circ) / \\sin({_fmt_sa(theta2)}^\\circ)$.",
            "tier_3": f"$n_2 = {_fmt_sa(calc_n)}$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["ratio_dimensionless_misconception", "snell_index_calculation_error"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Snell's law rearranged for n2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculation of refractive index", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Explanation of dimensionless quantity", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 09: Rectangular glass block lateral displacement parallel emergence
# ==============================================================================
def builder_09_rectangular_glass_block_lateral_displacement_parallel_emergence(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_glass = rng.choice([1.50, 1.52, 1.55])
    thickness_cm = rng.choice([4.0, 5.0, 6.0])
    theta1 = rng.choice([35, 45, 55])
    sin_theta2 = math.sin(math.radians(theta1)) / n_glass
    theta2 = math.degrees(math.asin(sin_theta2))
    # Lateral displacement d = t * sin(theta1 - theta2) / cos(theta2)
    d_cm = round(thickness_cm * math.sin(math.radians(theta1 - theta2)) / math.cos(math.radians(theta2)), 2)

    svg = f"""<svg viewBox="0 0 500 260" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="260" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="100" y="80" width="300" height="100" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <line x1="200" y1="40" x2="200" y2="120" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="250" y1="140" x2="250" y2="220" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="130" y1="30" x2="200" y2="80" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="200" y1="80" x2="250" y2="180" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="250" y1="180" x2="320" y2="230" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="200" y1="80" x2="350" y2="187" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="290" y1="144" x2="270" y2="194" stroke="#dc2626" stroke-width="2"/>
  <text x="285" y="180" font-size="11" fill="#dc2626" font-family="sans-serif">d = {_fmt_sa(d_cm)} cm</text>
  <text x="110" y="105" font-size="11" fill="#0369a1" font-weight="bold" font-family="sans-serif">Glass Block ({_fmt_sa(thickness_cm)} cm)</text>
</svg>"""

    prompt = (
        f"Consider a monochromatic optical beam entering the top interface of a clear glass plate with thickness "
        f"**${_fmt_sa(thickness_cm)}\\text{{ cm}}$** and index **${_fmt_sa(n_glass)}$** from ambient air at incident angle **${theta1}^\\circ$**.\n\n"
        f"1. Demonstrate that the beam emerging from the lower boundary travels parallel to the original incident path.\n"
        f"2. Determine the refraction angle ($\\theta_2$) at the first interface.\n"
        f"3. Compute the lateral shift ($d$) of the emergent beam in centimetres using: "
        f"$$d = \\frac{{t \\sin(\\theta_1 - \\theta_2)}}{{\\cos \\theta_2}}$$"
    )
    ans = f"1. Emergent angle equals incident angle by alternating interior angles and Snell's law; 2. theta2 = {_fmt_sa(round(theta2, 1))} deg; 3. d = {_fmt_sa(d_cm)} cm"
    memo = (
        f"1. Parallel emergence proof [2]: At the first surface, $\\sin \\theta_1 = n \\sin \\theta_2$. "
        f"By alternate interior angles between parallel surfaces, the angle of incidence at the bottom surface is $\\theta_2$. "
        f"Applying Snell's law at exit: $n \\sin \\theta_2 = 1 \\sin \\theta_3 \\implies \\theta_3 = \\theta_1$. "
        f"Hence the emergent ray travels in the identical direction as the incident ray [A].\n"
        f"2. Angle of refraction [2]:\n"
        f"   $$\\sin \\theta_2 = \\frac{{\\sin({theta1}^\\circ)}}{{{_fmt_sa(n_glass)}}} = {sin_theta2:.4f} \\implies \\theta_2 = {_fmt_sa(round(theta2, 1))}^\\circ$$ [A]\n"
        f"3. Lateral displacement [3]:\n"
        f"   $$d = \\frac{{{_fmt_sa(thickness_cm)} \\sin({theta1}^\\circ - {_fmt_sa(round(theta2, 1))}^\\circ)}}{{\\cos({_fmt_sa(round(theta2, 1))}^\\circ)}} = {_fmt_sa(d_cm)}\\text{{ cm}}$$ [A]"
    )
    return {
        "id": _make_id("optics_09", seed, 9),
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 7,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 7,
        "hints": {
            "tier_1": "The surfaces are parallel, so the ray refracts towards the normal upon entering and away by the same amount upon exiting.",
            "tier_2": f"Find $\\theta_2$ first, then substitute into the lateral displacement formula.",
            "tier_3": f"$\\theta_2 = {_fmt_sa(round(theta2, 1))}^\\circ$ and $d = {_fmt_sa(d_cm)}\\text{{ cm}}$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["parallel_emergence_misunderstood", "lateral_displacement_formula_error"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp1", "desc": "Proof of parallel emergence", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Angle of refraction calculated", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Lateral displacement calculation", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 10: Apparent depth real depth refraction
# ==============================================================================
def builder_10_apparent_depth_real_depth_refraction(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    medium, n_val = rng.choice([("water", 1.33), ("clear oil", 1.45), ("dense brine", 1.38)])
    real_depth_m = rng.choice([1.5, 2.0, 2.5, 3.0, 3.5])
    app_depth_m = round(real_depth_m / n_val, 2)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="70" width="400" height="150" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
  <text x="60" y="55" font-size="12" fill="#475569" font-family="sans-serif">Observer in Air</text>
  <text x="60" y="95" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">{medium.title()} (n = {_fmt_sa(n_val)})</text>
  <circle cx="250" cy="200" r="6" fill="#1e293b"/>
  <text x="265" y="205" font-size="11" fill="#1e293b" font-family="sans-serif">Real Fish (Depth: {_fmt_sa(real_depth_m)} m)</text>
  <circle cx="250" cy="{70 + int(app_depth_m * 35)}" r="6" fill="#dc2626" stroke="#991b1b" stroke-dasharray="2,2"/>
  <text x="265" y="{75 + int(app_depth_m * 35)}" font-size="11" fill="#dc2626" font-family="sans-serif">Apparent Position ({_fmt_sa(app_depth_m)} m)</text>
</svg>"""

    prompt = (
        f"An observer looks nearly vertically downwards into a pool of **{medium}** ($n = {_fmt_sa(n_val)}$). "
        f"A coin rests at the bottom at an actual depth of **${_fmt_sa(real_depth_m)}\\text{{ m}}$**.\n\n"
        f"1. Explain why objects immersed in water appear shallower than their true position.\n"
        f"2. Use the relation $n = \\frac{{\\text{{Real Depth}}}}{{\\text{{Apparent Depth}}}}$ to calculate the apparent depth in metres."
    )
    ans = f"1. Light rays emerging from water bend away from the normal, projecting a virtual image higher up; 2. Apparent depth = {_fmt_sa(app_depth_m)} m"
    memo = (
        f"1. Refraction mechanism [2]: Rays originating from the coin travel from an optically denser medium ({medium}) into air, "
        f"bending away from the normal. The observer's eye traces these rays back in straight lines, producing a virtual image located higher than the real coin [A].\n"
        f"2. Apparent depth calculation [2]:\n"
        f"   $$n = \\frac{{\\text{{Real Depth}}}}{{\\text{{Apparent Depth}}}} \\implies \\text{{Apparent Depth}} = \\frac{{{_fmt_sa(real_depth_m)}}}{{{_fmt_sa(n_val)}}} = {_fmt_sa(app_depth_m)}\\text{{ m}}$$ [A]"
    )
    return {
        "id": _make_id("optics_10", seed, 10),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Apparent depth = Real depth / n.",
            "tier_2": f"Divide real depth ({_fmt_sa(real_depth_m)} m) by refractive index ({_fmt_sa(n_val)}).",
            "tier_3": f"Apparent depth = {_fmt_sa(app_depth_m)} m.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["apparent_depth_multiplied_instead_of_divided", "virtual_image_depth_misunderstood"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Explanation of rays bending away from normal", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Calculation of apparent depth with units", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 11: Critical angle definition and formula
# ==============================================================================
def builder_11_critical_angle_definition_and_formula(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    medium, n_val = rng.choice([("water", 1.33), ("perspex", 1.49), ("crown glass", 1.52), ("diamond", 2.42)])
    sin_c = 1.0 / n_val
    theta_c = math.degrees(math.asin(sin_c))

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="120" width="400" height="100" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
  <line x1="250" y1="20" x2="250" y2="220" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="{250 - int(90 * math.sin(math.radians(theta_c)))}" y1="{120 + int(90 * math.cos(math.radians(theta_c)))}" x2="250" y2="120" stroke="#0284c7" stroke-width="3"/>
  <line x1="250" y1="120" x2="420" y2="120" stroke="#dc2626" stroke-width="3"/>
  <text x="210" y="170" font-size="12" fill="#0284c7" font-family="sans-serif">&theta;c = {_fmt_sa(round(theta_c, 1))}&deg;</text>
  <text x="320" y="110" font-size="11" fill="#dc2626" font-family="sans-serif">Refracted along boundary (&theta;r = 90&deg;)</text>
  <text x="60" y="80" font-size="12" fill="#475569" font-family="sans-serif">Air (n2 = 1,00)</text>
  <text x="60" y="160" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">{medium.title()} (n1 = {_fmt_sa(n_val)})</text>
</svg>"""

    prompt = (
        f"A light ray travels from inside **{medium}** ($n = {_fmt_sa(n_val)}$) towards an air boundary ($n = 1{{,}}00$).\n\n"
        f"1. Define the term 'critical angle'.\n"
        f"2. State the two essential conditions required for total internal reflection to occur.\n"
        f"3. Derive the formula for $\\sin \\theta_c$ from Snell's Law."
    )
    ans = "1. Angle of incidence in optically denser medium where angle of refraction is 90 deg; 2. Travel denser to less dense, theta_i > theta_c; 3. sin(theta_c) = 1/n"
    memo = (
        f"1. Definition [2]: The critical angle is the angle of incidence in the optically denser medium for which the angle of refraction in the optically less dense medium is $90^\\circ$ [A].\n"
        f"2. Conditions for TIR [2]:\n"
        f"   - Light must travel from an optically denser medium to an optically less dense medium [1].\n"
        f"   - The angle of incidence must be greater than the critical angle ($\\theta_i > \\theta_c$) [1].\n"
        f"3. Formula derivation [2]:\n"
        f"   $$n_1 \\sin \\theta_c = n_2 \\sin(90^\\circ)$$\n"
        f"   Since $\\sin(90^\\circ) = 1$ and for air $n_2 = 1{{,}}00$:\n"
        f"   $$\\sin \\theta_c = \\frac{{1}}{{n_1}}$$ [A]"
    )
    return {
        "id": _make_id("optics_11", seed, 11),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "hints": {
            "tier_1": "Set $\\theta_2 = 90^\\circ$ in Snell's Law.",
            "tier_2": "$n_1 \\sin \\theta_c = n_2 \\sin(90^\\circ) = n_2(1)$.",
            "tier_3": "Critical angle definition requires specifying the 90-degree refraction angle in the less dense medium.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["critical_angle_definition_incomplete", "tir_conditions_omitted"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Accurate definition of critical angle", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Two TIR conditions stated", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Derivation of sin(theta_c) = 1/n", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 12: Critical angle calculation dense to air
# ==============================================================================
def builder_12_critical_angle_calculation_dense_to_air(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    medium, n_val = rng.choice([
        ("water", 1.33),
        ("glycerol", 1.47),
        ("perspex", 1.49),
        ("flint glass", 1.62),
        ("zircon", 1.92),
        ("diamond", 2.42),
    ])
    sin_c = 1.0 / n_val
    theta_c = math.degrees(math.asin(sin_c))

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="110" width="400" height="110" fill="#ede9fe" stroke="#8b5cf6" stroke-width="2"/>
  <line x1="250" y1="20" x2="250" y2="210" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="{250 - int(80 * math.sin(math.radians(theta_c)))}" y1="{110 + int(80 * math.cos(math.radians(theta_c)))}" x2="250" y2="110" stroke="#7c3aed" stroke-width="3"/>
  <line x1="250" y1="110" x2="410" y2="110" stroke="#dc2626" stroke-width="3"/>
  <text x="195" y="160" font-size="12" fill="#7c3aed" font-family="sans-serif">&theta;c = ?</text>
  <text x="60" y="60" font-size="12" fill="#475569" font-family="sans-serif">Air (n = 1,00)</text>
  <text x="60" y="150" font-size="12" fill="#6d28d9" font-weight="bold" font-family="sans-serif">{medium.title()} (n = {_fmt_sa(n_val)})</text>
</svg>"""

    prompt = (
        f"Calculate the critical angle ($\\theta_c$) for a **{medium}**-air boundary given that the refractive index "
        f"of {medium} is **${_fmt_sa(n_val)}$** and that of air is **$1{{,}}00$**."
    )
    ans = f"theta_c = {_fmt_sa(round(theta_c, 1))} degrees"
    memo = (
        f"1. Formula [1]: $\\sin \\theta_c = \\frac{{n_2}}{{n_1}} = \\frac{{1{{,}}00}}{{n}}$ [M]\n"
        f"2. Substitution [1]: $\\sin \\theta_c = \\frac{{1{{,}}00}}{{{_fmt_sa(n_val)}}} = {sin_c:.4f}$ [M]\n"
        f"3. Critical angle [1]: $\\theta_c = \\sin^{{-1}}({sin_c:.4f}) = {_fmt_sa(round(theta_c, 1))}^\\circ$ [A]"
    )
    return {
        "id": _make_id("optics_12", seed, 12),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 4,
        "mode": "elementary_critical_angle",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 3,
        "hints": {
            "tier_1": "$\\sin \\theta_c = 1 / n$.",
            "tier_2": f"$\\sin \\theta_c = 1 / {_fmt_sa(n_val)} = {sin_c:.4f}$.",
            "tier_3": f"$\\theta_c = \\arcsin({sin_c:.4f}) = {_fmt_sa(round(theta_c, 1))}^\\circ$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["critical_angle_inverse_sine_error", "confused_medium_indices"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Formula for critical angle", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Substitution into formula", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Correct answer with degree units", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 13: Critical angle calculation between two dense media
# ==============================================================================
def builder_13_critical_angle_calculation_between_two_dense_media(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    pairs = [
        ("flint glass", 1.66, "water", 1.33),
        ("crown glass", 1.52, "water", 1.33),
        ("diamond", 2.42, "crown glass", 1.52),
        ("diamond", 2.42, "water", 1.33),
        ("flint glass", 1.62, "perspex", 1.49),
    ]
    med1, n1, med2, n2 = rng.choice(pairs)
    sin_c = n2 / n1
    theta_c = math.degrees(math.asin(sin_c))

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="20" width="400" height="100" fill="#f0fdf4" stroke="#4ade80" stroke-width="2"/>
  <rect x="50" y="120" width="400" height="100" fill="#dcfce7" stroke="#22c55e" stroke-width="2"/>
  <line x1="250" y1="20" x2="250" y2="220" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="{250 - int(80 * math.sin(math.radians(theta_c)))}" y1="{120 + int(80 * math.cos(math.radians(theta_c)))}" x2="250" y2="120" stroke="#15803d" stroke-width="3"/>
  <line x1="250" y1="120" x2="410" y2="120" stroke="#dc2626" stroke-width="3"/>
  <text x="60" y="60" font-size="12" fill="#166534" font-weight="bold" font-family="sans-serif">Medium 2: {med2.title()} (n2 = {_fmt_sa(n2)})</text>
  <text x="60" y="160" font-size="12" fill="#14532d" font-weight="bold" font-family="sans-serif">Medium 1: {med1.title()} (n1 = {_fmt_sa(n1)})</text>
  <text x="190" y="170" font-size="12" fill="#15803d" font-family="sans-serif">&theta;c = ?</text>
</svg>"""

    prompt = (
        f"A light ray travels inside a block of **{med1}** ($n_1 = {_fmt_sa(n1)}$) towards a boundary with **{med2}** "
        f"($n_2 = {_fmt_sa(n2)}$).\n\n"
        f"1. Explain why total internal reflection can occur only when light travels from {med1} towards {med2}, and not vice versa.\n"
        f"2. Calculate the critical angle ($\\theta_c$) for the interface between these two media."
    )
    ans = f"1. TIR requires traveling from optically denser to less dense (n1 > n2); 2. theta_c = {_fmt_sa(round(theta_c, 1))} degrees"
    memo = (
        f"1. Condition explanation [1]: Light must travel from an optically denser medium ($n_1 = {_fmt_sa(n1)}$) into an optically less dense medium ($n_2 = {_fmt_sa(n2)}$) "
        f"so that the refracted ray bends away from the normal towards the $90^\\circ$ boundary [A].\n"
        f"2. Critical angle calculation [3]:\n"
        f"   $$\\sin \\theta_c = \\frac{{n_2}}{{n_1}} = \\frac{{{_fmt_sa(n2)}}}{{{_fmt_sa(n1)}}} = {sin_c:.4f}$$ [M]\n"
        f"   $$\\theta_c = \\sin^{{-1}}({sin_c:.4f}) = {_fmt_sa(round(theta_c, 1))}^\\circ$$ [A]"
    )
    return {
        "id": _make_id("optics_13", seed, 13),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "$\\sin \\theta_c = n_2 / n_1$ where $n_1 > n_2$.",
            "tier_2": f"$\\sin \\theta_c = {_fmt_sa(n2)} / {_fmt_sa(n1)} = {sin_c:.4f}$.",
            "tier_3": f"$\\theta_c = {_fmt_sa(round(theta_c, 1))}^\\circ$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["ratio_inverted_in_two_media_critical_angle", "tir_directionality_misunderstood"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Explanation of optical density requirement", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula and substitution sin(theta_c) = n2/n1", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Calculated critical angle with degree unit", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 14: Total internal reflection two conditions evaluation
# ==============================================================================
def builder_14_total_internal_reflection_two_conditions_evaluation(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_glass = 1.52
    sin_c = 1.0 / n_glass
    theta_c = round(math.degrees(math.asin(sin_c)), 1)
    angle_inc = rng.choice([35, 38, 41, 45, 50, 60])
    will_tir = angle_inc > theta_c

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="120" width="400" height="100" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
  <line x1="250" y1="20" x2="250" y2="220" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="{250 - int(80 * math.sin(math.radians(angle_inc)))}" y1="{120 + int(80 * math.cos(math.radians(angle_inc)))}" x2="250" y2="120" stroke="#0284c7" stroke-width="3"/>
  <text x="210" y="160" font-size="12" fill="#0284c7" font-family="sans-serif">&theta;i = {angle_inc}&deg;</text>
  <text x="60" y="60" font-size="12" fill="#475569" font-family="sans-serif">Air (n = 1,00)</text>
  <text x="60" y="160" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Crown Glass (n = 1,52, &theta;c = {_fmt_sa(theta_c)}&deg;)</text>
</svg>"""

    prompt = (
        f"A light ray inside crown glass ($n = 1{{,}}52$, critical angle $\\theta_c = {_fmt_sa(theta_c)}^\\circ$) strikes the "
        f"glass-air boundary at an angle of incidence of **${angle_inc}^\\circ$**.\n\n"
        f"1. State whether total internal reflection will occur. Give a clear reason.\n"
        f"2. State what happens to the energy of the ray if total internal reflection does occur compared to reflection by a silvered mirror."
    )
    ans = f"1. {'Yes' if will_tir else 'No'}, because angle of incidence ({angle_inc} deg) is {'>' if will_tir else '<'} critical angle ({_fmt_sa(theta_c)} deg); 2. 100% of light energy is reflected (zero absorption)."
    memo = (
        f"1. Decision and justification [3]:\n"
        f"   - **{'YES' if will_tir else 'NO'}** [1].\n"
        f"   - Reason: The ray is traveling from an optically denser medium (glass) to a less dense medium (air) [1], "
        f"   and the angle of incidence (${angle_inc}^\\circ$) is **{'>' if will_tir else '<'}** the critical angle (${_fmt_sa(theta_c)}^\\circ$) [1].\n"
        f"2. Energy comparison [1]: In total internal reflection, **$100\\%$ of light energy is reflected** with zero absorption or transmission, "
        f"making it more efficient than silvered mirrors which absorb 4–10% of light [A]."
    )
    return {
        "id": _make_id("optics_14", seed, 14),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": f"Compare angle of incidence ({angle_inc} degrees) with critical angle ({_fmt_sa(theta_c)} degrees).",
            "tier_2": "TIR occurs ONLY if angle of incidence > critical angle.",
            "tier_3": f"{'TIR occurs' if will_tir else 'TIR does NOT occur'}. 100% energy reflection.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["tir_threshold_comparison_inverted", "partial_transmission_assumed_in_tir"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Correct binary yes/no prediction", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Justification comparing angles", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "100% energy reflection stated", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 15: TIR in 45-degree right angle prisms periscope
# ==============================================================================
def builder_15_tir_in_45_degree_right_angle_prisms_periscope(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_glass = rng.choice([1.50, 1.52, 1.55])
    theta_c = round(math.degrees(math.asin(1.0 / n_glass)), 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <!-- 45-45-90 Prism -->
  <polygon points="120,40 120,200 280,200" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
  <!-- Light Ray entering normal -->
  <line x1="40" y1="120" x2="120" y2="120" stroke="#dc2626" stroke-width="3"/>
  <line x1="120" y1="120" x2="200" y2="120" stroke="#dc2626" stroke-width="3"/>
  <!-- TIR at hypotenuse -->
  <line x1="200" y1="120" x2="200" y2="200" stroke="#dc2626" stroke-width="3"/>
  <line x1="200" y1="200" x2="200" y2="235" stroke="#dc2626" stroke-width="3"/>
  <line x1="160" y1="80" x2="240" y2="160" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.5"/>
  <text x="210" y="105" font-size="11" fill="#1e293b" font-family="sans-serif">&theta;i = 45&deg;</text>
  <text x="300" y="120" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">45&deg;-45&deg;-90&deg; Crown Glass</text>
  <text x="300" y="140" font-size="11" fill="#475569" font-family="sans-serif">n = {_fmt_sa(n_glass)}, &theta;c = {_fmt_sa(theta_c)}&deg;</text>
</svg>"""

    prompt = (
        f"A ray of light enters normally (at $90^\\circ$) into one of the shorter legs of a $45^\\circ$-$45^\\circ$-$90^\\circ$ "
        f"crown glass prism ($n = {_fmt_sa(n_glass)}$, critical angle $\\theta_c = {_fmt_sa(theta_c)}^\\circ$).\n\n"
        f"1. Explain why the ray experiences zero refraction upon entering the first surface.\n"
        f"2. Determine the angle of incidence when the ray strikes the hypotenuse face inside the prism.\n"
        f"3. Explain why the ray is totally internally reflected through $90^\\circ$ rather than escaping into air.\n"
        f"4. Name one practical optical instrument that uses this $90^\\circ$ reflection configuration."
    )
    ans = f"1. Angle of incidence is 0 deg to the normal; 2. theta_i = 45 deg; 3. 45 deg > critical angle ({_fmt_sa(theta_c)} deg) and travels denser to less dense; 4. Periscope."
    memo = (
        f"1. Normal entry [1]: The ray strikes the surface at $90^\\circ$ to the boundary, meaning angle of incidence to the normal is $0^\\circ$. "
        f"By Snell's law, $\\theta_r = 0^\\circ$ and the ray passes straight through [A].\n"
        f"2. Angle of incidence on hypotenuse [1]: $\\theta_i = 45^\\circ$ [A].\n"
        f"3. TIR explanation [2]: The ray travels from glass into air (optically denser to less dense) and the angle of incidence ($45^\\circ$) "
        f"exceeds the critical angle (${_fmt_sa(theta_c)}^\\circ$). Therefore total internal reflection occurs, turning the ray by $90^\\circ$ [A].\n"
        f"4. Instrument [1]: Periscope (or single-lens reflex camera pentaprism) [A]."
    )
    return {
        "id": _make_id("optics_15", seed, 15),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Light striking normal to a surface travels straight through (zero angle of incidence to normal).",
            "tier_2": f"At the hypotenuse, angle of incidence is 45 degrees. Compare 45 with {_fmt_sa(theta_c)}.",
            "tier_3": "TIR occurs because 45 > critical angle. Common in periscopes.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["normal_incidence_bending_misconception", "prism_hypotenuse_angle_geometry_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Reason for zero deviation at normal entry", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Angle of incidence at hypotenuse", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "TIR explanation comparing with critical angle", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Application named (periscope)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 16: TIR in Porro prisms binoculars
# ==============================================================================
def builder_16_tir_in_porro_prisms_binoculars(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_val = rng.choice([1.50, 1.52, 1.56])
    theta_c = round(math.degrees(math.asin(1.0 / n_val)), 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <polygon points="150,40 250,140 150,240" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <line x1="40" y1="80" x2="150" y2="80" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="150" y1="80" x2="190" y2="80" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="190" y1="80" x2="190" y2="200" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="190" y1="200" x2="150" y2="200" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="150" y1="200" x2="40" y2="200" stroke="#2563eb" stroke-width="2.5"/>
  <text x="270" y="100" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Porro Prism (180&deg; Deviation)</text>
  <text x="270" y="130" font-size="11" fill="#475569" font-family="sans-serif">Double TIR inside prism</text>
  <text x="270" y="150" font-size="11" fill="#475569" font-family="sans-serif">&theta;c = {_fmt_sa(theta_c)}&deg; &lt; 45&deg;</text>
</svg>"""

    prompt = (
        f"In binoculars, a pair of right-angled Porro prisms is used to invert and revert the image formed by the objective lens.\n\n"
        f"1. Describe how a Porro prism turns a beam of light through **$180^\\circ$** using total internal reflection.\n"
        f"2. State TWO reasons why glass prisms are preferred over plane silvered mirrors in precision optical instruments like binoculars."
    )
    ans = "1. Two successive 90 deg TIR reflections at 45 deg incidence inside hypotenuse face; 2. 100% reflectance (no light loss) and no silver coating tarnishing/multiple ghost reflections."
    memo = (
        f"1. Mechanism [2]: The ray enters the hypotenuse face normally and undergoes **two successive total internal reflections** "
        f"at $45^\\circ$ incidence at each of the two perpendicular faces, turning the ray through $90^\\circ + 90^\\circ = 180^\\circ$ [A].\n"
        f"2. Advantages over mirrors [2]:\n"
        f"   - **100% reflectance**: Prisms reflect all light without absorption, whereas silvered mirrors absorb 4–10% of light [1].\n"
        f"   - **Durability and clarity**: No reflective silver coating that can tarnish or scratch, and avoids multiple ghost reflections from front glass surfaces [1]."
    )
    return {
        "id": _make_id("optics_16", seed, 16),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Double reflection turns the beam 180 degrees back.",
            "tier_2": "Prisms provide 100% reflection via TIR without silver coating degradation.",
            "tier_3": "180 degree turn via two 90 degree reflections; 100% light efficiency and no ghosting.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["porro_prism_reflection_count_error", "mirror_vs_prism_efficiency_misunderstood"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Description of two 90-degree TIR reflections", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Advantage 1: 100% reflectance", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Advantage 2: No silver tarnishing/ghosting", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 17: Optical fibre core cladding acceptance angle
# ==============================================================================
def builder_17_optical_fibre_core_cladding_acceptance_angle(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_core = rng.choice([1.48, 1.50, 1.52, 1.60])
    delta_n = rng.choice([0.03, 0.04, 0.05])
    n_clad = round(n_core - delta_n, 2)
    sin_c = n_clad / n_core
    theta_c = math.degrees(math.asin(sin_c))
    na = math.sqrt(n_core**2 - n_clad**2)
    theta_max_deg = math.degrees(math.asin(min(na, 1.0)))

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <!-- Cladding top -->
  <rect x="50" y="40" width="400" height="40" fill="#cbd5e1" stroke="#64748b" stroke-width="1.5"/>
  <!-- Core -->
  <rect x="50" y="80" width="400" height="80" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <!-- Cladding bottom -->
  <rect x="50" y="160" width="400" height="40" fill="#cbd5e1" stroke="#64748b" stroke-width="1.5"/>
  <text x="60" y="65" font-size="11" fill="#334155" font-family="sans-serif">Cladding (n = {_fmt_sa(n_clad)})</text>
  <text x="60" y="125" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Core (n = {_fmt_sa(n_core)})</text>
  <text x="60" y="185" font-size="11" fill="#334155" font-family="sans-serif">Cladding (n = {_fmt_sa(n_clad)})</text>
  <!-- Light Ray undergoing TIR -->
  <path d="M 50,140 L 150,80 L 270,160 L 390,80 L 450,110" fill="none" stroke="#dc2626" stroke-width="3"/>
</svg>"""

    prompt = (
        f"An optical fibre consists of a cylindrical glass core ($n_{{\\text{{core}}}} = {_fmt_sa(n_core)}$) "
        f"surrounded by a protective cladding ($n_{{\\text{{clad}}}} = {_fmt_sa(n_clad)}$).\n\n"
        f"1. Explain why the core MUST have a higher refractive index than the cladding.\n"
        f"2. Calculate the critical angle ($\\theta_c$) for the core-cladding interface.\n"
        f"3. State TWO advantages of optical fibre telecommunications over traditional copper wire cables."
    )
    ans = f"1. TIR requires traveling from higher n to lower n; 2. theta_c = {_fmt_sa(round(theta_c, 1))} degrees; 3. Higher bandwidth (data rate) and immunity to electromagnetic interference."
    memo = (
        f"1. Refractive index requirement [2]: Total internal reflection can ONLY occur when light travels from an optically denser medium "
        f"to an optically less dense medium ($n_{{\\text{{core}}}} > n_{{\\text{{clad}}}}$) [A].\n"
        f"2. Critical angle calculation [3]:\n"
        f"   $$\\sin \\theta_c = \\frac{{n_{{\\text{{clad}}}}}}{{n_{{\\text{{core}}}}}} = \\frac{{{_fmt_sa(n_clad)}}}{{{_fmt_sa(n_core)}}} = {sin_c:.4f}$$ [M]\n"
        f"   $$\\theta_c = \\sin^{{-1}}({sin_c:.4f}) = {_fmt_sa(round(theta_c, 1))}^\\circ$$ [A]\n"
        f"3. Advantages [2]: Much higher data carrying capacity (bandwidth), immune to electromagnetic interference (EMI), "
        f"lower signal attenuation over long distances, and lighter weight [A]."
    )
    return {
        "id": _make_id("optics_17", seed, 17),
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 7,
        "hints": {
            "tier_1": "$n_{\\text{core}} > n_{\\text{clad}}$ is essential for TIR.",
            "tier_2": f"$\\sin \\theta_c = n_{{\\text{{clad}}}} / n_{{\\text{{core}}}} = {_fmt_sa(n_clad)} / {_fmt_sa(n_core)}$.",
            "tier_3": f"$\\theta_c = {_fmt_sa(round(theta_c, 1))}^\\circ$. Faster speeds, zero EMI.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["optical_fibre_cladding_density_inverted", "critical_angle_formula_numerator_denominator_swap"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp1", "desc": "Refractive index requirement explained", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Critical angle calculated", "marks": 3, "editable": True},
                {"id": "mp3", "desc": "Two advantages of optical fibres", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 18: Triangular prism minimum deviation angle
# ==============================================================================
def builder_18_triangular_prism_minimum_deviation_angle(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    apex_a = rng.choice([60])  # equilateral prism standard
    n_glass = rng.choice([1.50, 1.52, 1.55, 1.62])
    # n = sin((A + Dm)/2) / sin(A/2) => sin((A + Dm)/2) = n * sin(A/2)
    sin_half = n_glass * math.sin(math.radians(apex_a / 2))
    half_angle = math.degrees(math.asin(sin_half))
    d_m = round(2 * half_angle - apex_a, 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <polygon points="250,30 150,200 350,200" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="240" y="25" font-size="12" fill="#0f172a" font-weight="bold" font-family="sans-serif">A = {apex_a}&deg;</text>
  <!-- Symmetrical ray passing through at minimum deviation -->
  <line x1="80" y1="170" x2="185" y2="140" stroke="#dc2626" stroke-width="2.5"/>
  <line x1="185" y1="140" x2="315" y2="140" stroke="#dc2626" stroke-width="2.5"/>
  <line x1="315" y1="140" x2="420" y2="170" stroke="#dc2626" stroke-width="2.5"/>
  <line x1="185" y1="140" x2="380" y2="85" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.5"/>
  <text x="360" y="130" font-size="11" fill="#dc2626" font-family="sans-serif">Dm = {_fmt_sa(d_m)}&deg;</text>
  <text x="220" y="160" font-size="11" fill="#0369a1" font-family="sans-serif">Ray parallel to base</text>
</svg>"""

    prompt = (
        f"An equilateral triangular prism with apex angle **$A = {apex_a}^\\circ$** is fabricated from glass with "
        f"refractive index **${_fmt_sa(n_glass)}$**.\n\n"
        f"1. State the symmetry condition inside the prism when light passes at minimum deviation ($D_m$).\n"
        f"2. Use the prism formula $$n = \\frac{{\\sin\\left(\\frac{{A + D_m}}{{2}}\\right)}}{{\\sin\\left(\\frac{{A}}{{2}}\\right)}}$$ "
        f"to calculate the angle of minimum deviation ($D_m$) in degrees."
    )
    ans = f"1. Refracted ray travels parallel to the base; 2. Dm = {_fmt_sa(d_m)} degrees"
    memo = (
        f"1. Symmetry condition [1]: At minimum deviation, the refracted ray inside the prism travels **parallel to the base**, "
        f"and the angle of incidence equals the angle of emergence ($\\theta_i = \\theta_e$) [A].\n"
        f"2. Minimum deviation calculation [3]:\n"
        f"   $${_fmt_sa(n_glass)} = \\frac{{\\sin\\left(\\frac{{{apex_a}^\\circ + D_m}}{{2}}\\right)}}{{\\sin({apex_a / 2}^\\circ)}}$$\n"
        f"   $$\\sin\\left(\\frac{{{apex_a}^\\circ + D_m}}{{2}}\\right) = {_fmt_sa(n_glass)} \\times \\sin(30^\\circ) = {_fmt_sa(n_glass)} \\times 0{{,}}5 = {sin_half:.4f}$$\n"
        f"   $$\\frac{{{apex_a}^\\circ + D_m}}{{2}} = \\sin^{{-1}}({sin_half:.4f}) = {half_angle:.2f}^\\circ$$\n"
        f"   $$D_m = 2({half_angle:.2f}^\\circ) - {apex_a}^\\circ = {_fmt_sa(d_m)}^\\circ$$ [A]"
    )
    return {
        "id": _make_id("optics_18", seed, 18),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "At minimum deviation, the ray passes symmetrically (parallel to the base).",
            "tier_2": f"$\\sin((A + D_m)/2) = n \\sin(A/2) = {_fmt_sa(n_glass)} \\times 0.5$.",
            "tier_3": f"$D_m = 2 \\times \\arcsin({sin_half:.4f}) - {apex_a} = {_fmt_sa(d_m)}^\\circ$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["minimum_deviation_formula_algebraic_error", "prism_symmetry_misunderstood"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Statement of ray parallel to base at Dm", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Substitution into prism formula", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Calculated Dm with degree unit", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 19: Dispersion of white light prism refractive index vs wavelength
# ==============================================================================
def builder_19_dispersion_of_white_light_prism_refractive_index_vs_wavelength(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_red = 1.51
    n_violet = 1.53
    theta1 = rng.choice([40, 45, 50])
    sin_r = math.sin(math.radians(theta1)) / n_red
    sin_v = math.sin(math.radians(theta1)) / n_violet
    theta_r = round(math.degrees(math.asin(sin_r)), 2)
    theta_v = round(math.degrees(math.asin(sin_v)), 2)
    ang_disp = round(theta_r - theta_v, 2)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <polygon points="250,30 150,200 350,200" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <line x1="60" y1="130" x2="190" y2="130" stroke="#f8fafc" stroke-width="6"/>
  <line x1="60" y1="130" x2="190" y2="130" stroke="#475569" stroke-width="2.5"/>
  <text x="70" y="115" font-size="11" fill="#475569" font-family="sans-serif">White Light</text>
  <!-- Dispersed rays -->
  <line x1="190" y1="130" x2="310" y2="140" stroke="#dc2626" stroke-width="2"/>
  <line x1="190" y1="130" x2="310" y2="155" stroke="#7c3aed" stroke-width="2"/>
  <line x1="310" y1="140" x2="430" y2="150" stroke="#dc2626" stroke-width="2"/>
  <line x1="310" y1="155" x2="430" y2="190" stroke="#7c3aed" stroke-width="2"/>
  <text x="440" y="155" font-size="12" fill="#dc2626" font-weight="bold" font-family="sans-serif">Red (least bent)</text>
  <text x="440" y="195" font-size="12" fill="#7c3aed" font-weight="bold" font-family="sans-serif">Violet (most bent)</text>
</svg>"""

    prompt = (
        f"A narrow beam of white light strikes a glass prism at an angle of incidence of **${theta1}^\\circ$**.\n"
        f"The refractive index of the glass is **${_fmt_sa(n_red)}$** for red light and **${_fmt_sa(n_violet)}$** for violet light.\n\n"
        f"1. Define the phenomenon of 'dispersion'.\n"
        f"2. Explain why violet light bends more than red light when entering the prism.\n"
        f"3. Calculate the difference in the angles of refraction (angular separation) between red and violet light inside the prism."
    )
    ans = f"1. Splitting of white light into its component colors; 2. Violet has shorter wavelength and higher refractive index (slower speed); 3. Angular separation = {_fmt_sa(ang_disp)} degrees"
    memo = (
        f"1. Definition [1]: Dispersion is the splitting of white light into its component spectral colours due to differences in wave speed (and refractive index) for different wavelengths [A].\n"
        f"2. Explanation [2]: Violet light has a shorter wavelength and experiences a **higher refractive index** ($n_{{\\text{{violet}}}} = {_fmt_sa(n_violet)} > n_{{\\text{{red}}}} = {_fmt_sa(n_red)}$), "
        f"meaning it slows down more and bends more sharply towards the normal [A].\n"
        f"3. Calculation [3]:\n"
        f"   $$\\sin \\theta_r = \\frac{{\\sin({theta1}^\\circ)}}{{{_fmt_sa(n_red)}}} = {sin_r:.4f} \\implies \\theta_r = {_fmt_sa(theta_r)}^\\circ$$\n"
        f"   $$\\sin \\theta_v = \\frac{{\\sin({theta1}^\\circ)}}{{{_fmt_sa(n_violet)}}} = {sin_v:.4f} \\implies \\theta_v = {_fmt_sa(theta_v)}^\\circ$$\n"
        f"   $$\\Delta \\theta = \\theta_r - \\theta_v = {_fmt_sa(theta_r)}^\\circ - {_fmt_sa(theta_v)}^\\circ = {_fmt_sa(ang_disp)}^\\circ$$ [A]"
    )
    return {
        "id": _make_id("optics_19", seed, 19),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "hints": {
            "tier_1": "Violet light has shorter wavelength -> higher refractive index -> bends more.",
            "tier_2": "Calculate $\\theta_r$ for red and $\\theta_v$ for violet using Snell's Law.",
            "tier_3": f"$\\theta_r = {_fmt_sa(theta_r)}^\\circ$, $\\theta_v = {_fmt_sa(theta_v)}^\\circ$, difference = {_fmt_sa(ang_disp)}^\\circ$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["dispersion_frequency_dependence_inverted", "refraction_angle_difference_miscalculated"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Definition of dispersion", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explanation of violet bending more due to higher n", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Calculation of both refraction angles and difference", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 20: Atmospheric refraction mirages and delayed sunset
# ==============================================================================
def builder_20_atmospheric_refraction_mirages_and_delayed_sunset(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    temp_hot = rng.choice([40, 45, 50])
    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="0" y="190" width="500" height="50" fill="#78716c"/>
  <text x="20" y="220" font-size="12" fill="#f8fafc" font-family="sans-serif">Hot Tar Road Surface ({temp_hot}&deg;C)</text>
  <text x="20" y="50" font-size="12" fill="#0284c7" font-weight="bold" font-family="sans-serif">Cool Denser Air (Higher n)</text>
  <text x="20" y="160" font-size="12" fill="#ea580c" font-weight="bold" font-family="sans-serif">Hot Rarefied Air (Lower n)</text>
  <!-- Curved light path -->
  <path d="M 50,60 Q 220,195 420,140" fill="none" stroke="#2563eb" stroke-width="3"/>
  <line x1="420" y1="140" x2="250" y2="200" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.5"/>
  <text x="360" y="215" font-size="11" fill="#0284c7" font-family="sans-serif">Virtual Image (Apparent water)</text>
</svg>"""

    prompt = (
        f"On a scorching hot summer day, the air temperature directly above a tar road reaches **${temp_hot}^\\circ\\text{{C}}$**, "
        f"while the air higher up is cooler.\n\n"
        f"1. Explain how temperature variations affect the optical density (and refractive index) of air.\n"
        f"2. Explain the physical mechanism that causes a driver to see an apparent pool of water (inferior mirage) on the road ahead.\n"
        f"3. Explain why the Sun remains visible for approximately 2 minutes after it has geometrically set below the horizon."
    )
    ans = "1. Hot air expands, is less dense, and has a lower refractive index; 2. Light rays from the sky curve upward into cooler air, forming a virtual image of the sky; 3. Atmospheric refraction bends light rays around Earth's curvature."
    memo = (
        f"1. Optical density vs temperature [1]: Hot air expands and is physically less dense, giving it a **lower optical density** (lower refractive index) "
        f"than cooler, denser air higher up [A].\n"
        f"2. Mirage mechanism [2]: Downward-traveling light rays from the sky pass from cooler air into hotter air, bending continuously **away from the normal**. "
        f"When the critical angle is reached, the rays undergo total internal reflection / upward curvature into the observer's eyes, "
        f"who projects them straight down as a virtual image of the sky (looking like water) [A].\n"
        f"3. Delayed sunset [2]: Earth's atmosphere becomes progressively denser toward the surface. Light rays from the sun below the horizon "
        f"refract continuously towards the normal, bending around Earth's curvature and reaching the observer's eyes [A]."
    )
    return {
        "id": _make_id("optics_20", seed, 20),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Warm air = lower optical density (lower n). Rays curve upward.",
            "tier_2": "The mirage is a virtual image of the sky reflected off the hot boundary layer.",
            "tier_3": "Atmospheric refraction bends sunlight around the Earth's curved horizon.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["mirage_reflection_vs_refraction_confusion", "atmospheric_refraction_direction_misunderstood"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Temperature and refractive index correlation", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Mirage upward curving ray mechanism", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Atmospheric bending around Earth curvature explanation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 21: Diamond brilliance critical angle cut geometry
# ==============================================================================
def builder_21_diamond_brilliance_critical_angle_cut_geometry(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_dia = 2.42
    n_glass = 1.52
    sin_dia = 1.0 / n_dia
    sin_glass = 1.0 / n_glass
    theta_c_dia = round(math.degrees(math.asin(sin_dia)), 1)
    theta_c_glass = round(math.degrees(math.asin(sin_glass)), 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <!-- Diamond facet outline -->
  <polygon points="170,50 330,50 380,100 250,220 120,100" fill="#f0fdfa" stroke="#0d9488" stroke-width="2.5"/>
  <line x1="250" y1="50" x2="160" y2="150" stroke="#0d9488" stroke-width="1.5"/>
  <line x1="250" y1="50" x2="340" y2="150" stroke="#0d9488" stroke-width="1.5"/>
  <line x1="200" y1="20" x2="230" y2="50" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="230" y1="50" x2="340" y2="140" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="340" y1="140" x2="160" y2="140" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="160" y1="140" x2="260" y2="50" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="260" y1="50" x2="280" y2="20" stroke="#2563eb" stroke-width="2.5"/>
  <text x="390" y="80" font-size="12" fill="#0d9488" font-weight="bold" font-family="sans-serif">Diamond Cut</text>
  <text x="390" y="105" font-size="11" fill="#475569" font-family="sans-serif">n = 2,42</text>
  <text x="390" y="125" font-size="11" fill="#0f172a" font-family="sans-serif">&theta;c = {_fmt_sa(theta_c_dia)}&deg;</text>
  <text x="390" y="150" font-size="11" fill="#2563eb" font-family="sans-serif">Multiple TIR bounces</text>
</svg>"""

    prompt = (
        f"The refractive index of diamond is **${_fmt_sa(n_dia)}$**, whereas the refractive index of ordinary crown glass "
        f"is **${_fmt_sa(n_glass)}$**.\n\n"
        f"1. Calculate the critical angle for diamond in air and compare it with that of crown glass in air.\n"
        f"2. Explain why diamonds sparkle with intense brilliance (fire) when cut with faceted geometries."
    )
    ans = f"1. Diamond theta_c = {_fmt_sa(theta_c_dia)} deg vs glass theta_c = {_fmt_sa(theta_c_glass)} deg; 2. Very small critical angle causes light to undergo multiple TIR reflections and emerge from top facets with high dispersion."
    memo = (
        f"1. Critical angle comparison [3]:\n"
        f"   - Diamond: $\\sin \\theta_c = \\frac{{1}}{{2{{,}}42}} = {sin_dia:.4f} \\implies \\theta_c = {_fmt_sa(theta_c_dia)}^\\circ$ [M][A]\n"
        f"   - Crown glass: $\\sin \\theta_c = \\frac{{1}}{{1{{,}}52}} = {sin_glass:.4f} \\implies \\theta_c = {_fmt_sa(theta_c_glass)}^\\circ$ [A]\n"
        f"2. Brilliance explanation [2]: Because diamond has an exceptionally **small critical angle** (${_fmt_sa(theta_c_dia)}^\\circ$), "
        f"most light entering the diamond strikes interior facets at angles $> {_fmt_sa(theta_c_dia)}^\\circ$, undergoing **multiple total internal reflections** "
        f"before exiting through the top facets, coupled with high dispersion that spreads light into vibrant spectral colours [A]."
    )
    return {
        "id": _make_id("optics_21", seed, 21),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Calculate critical angles: $\\sin \\theta_c = 1 / n$.",
            "tier_2": f"Diamond critical angle is only {_fmt_sa(theta_c_dia)} degrees.",
            "tier_3": "Small critical angle traps light inside diamond for multiple TIR reflections.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["diamond_brilliance_attributed_to_reflection_only", "critical_angle_comparison_inverted"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Calculation of diamond critical angle", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Calculation of glass critical angle", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Explanation of small critical angle and facet TIR", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 22: Snell's Law graphical analysis sin theta i vs sin theta r
# ==============================================================================
def builder_22_snells_law_graphical_analysis_sin_theta_i_vs_sin_theta_r(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_target = rng.choice([1.45, 1.50, 1.54, 1.60])
    pts = [(0.20, round(0.20 / n_target, 3)), (0.40, round(0.40 / n_target, 3)), (0.60, round(0.60 / n_target, 3)), (0.80, round(0.80 / n_target, 3))]

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="80" y1="200" x2="440" y2="200" stroke="#0f172a" stroke-width="2"/>
  <line x1="80" y1="200" x2="80" y2="30" stroke="#0f172a" stroke-width="2"/>
  <text x="210" y="230" font-size="12" fill="#0f172a" font-weight="bold" font-family="sans-serif">sin(&theta;r)</text>
  <text x="15" y="110" font-size="12" fill="#0f172a" font-weight="bold" font-family="sans-serif" transform="rotate(-90,25,110)">sin(&theta;i)</text>
  <line x1="80" y1="200" x2="400" y2="40" stroke="#2563eb" stroke-width="2.5"/>
  <circle cx="160" cy="160" r="4" fill="#dc2626"/>
  <circle cx="240" cy="120" r="4" fill="#dc2626"/>
  <circle cx="320" cy="80" r="4" fill="#dc2626"/>
  <circle cx="400" cy="40" r="4" fill="#dc2626"/>
  <text x="260" y="70" font-size="12" fill="#2563eb" font-family="sans-serif">Gradient = n = {_fmt_sa(n_target)}</text>
</svg>"""

    prompt = (
        f"A student plots a graph of **$\\sin \\theta_i$** (on the $y$-axis) versus **$\\sin \\theta_r$** (on the $x$-axis) "
        f"for light passing from air into an unknown liquid.\n"
        f"A straight line passing through the origin is obtained, with two data points at "
        f"$(0{{,}}25; {round(0.25 * n_target, 3):.3f})$ and $(0{{,}}50; {round(0.50 * n_target, 3):.3f})$.\n\n"
        f"1. Explain why this linear relationship confirms Snell's Law.\n"
        f"2. Determine the physical meaning of the gradient of the graph.\n"
        f"3. Calculate the gradient and state the refractive index of the liquid."
    )
    ans = f"1. Snell's law states sin(theta_i) is directly proportional to sin(theta_r); 2. Gradient equals refractive index (n); 3. Gradient = n = {_fmt_sa(n_target)}"
    memo = (
        f"1. Linearity justification [1]: Snell's Law states $\\sin \\theta_i = n \\sin \\theta_r$. "
        f"Comparing this to $y = mx + c$, the graph is a straight line through the origin, confirming direct proportionality [A].\n"
        f"2. Physical meaning [1]: The gradient represents the **refractive index ($n$)** of the liquid relative to air [A].\n"
        f"3. Gradient calculation [2]:\n"
        f"   $$m = \\frac{{\\Delta y}}{{\\Delta x}} = \\frac{{{round(0.50 * n_target, 3):.3f} - {round(0.25 * n_target, 3):.3f}}}{{0{{,}}50 - 0{{,}}25}} = \\frac{{{round(0.25 * n_target, 3):.3f}}}{{0{{,}}25}} = {_fmt_sa(n_target)}$$ [M]\n"
        f"   Hence $n = {_fmt_sa(n_target)}$ [A]."
    )
    return {
        "id": _make_id("optics_22", seed, 22),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Compare $\\sin \\theta_i = n \\sin \\theta_r$ to $y = mx$.",
            "tier_2": "The gradient of $\\sin \\theta_i$ vs $\\sin \\theta_r$ is $n$.",
            "tier_3": f"Gradient = {n_target}.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["snell_graph_axis_gradient_inversion", "proportionality_origin_intercept_misunderstood"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Direct proportionality confirmation", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Gradient physical meaning identified as n", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Gradient calculation shown", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 23: Multi-layer parallel refraction air water glass
# ==============================================================================
def builder_23_multi_layer_parallel_refraction_air_water_glass(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_air = 1.00
    n_water = 1.33
    n_glass = 1.52
    theta_air = rng.choice([40, 50, 60])
    sin_w = (n_air * math.sin(math.radians(theta_air))) / n_water
    theta_w = math.degrees(math.asin(sin_w))
    sin_g = (n_water * math.sin(math.radians(theta_w))) / n_glass
    theta_g = math.degrees(math.asin(sin_g))

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="20" width="400" height="60" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <rect x="50" y="80" width="400" height="70" fill="#bae6fd" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="50" y="150" width="400" height="70" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
  <text x="60" y="55" font-size="11" fill="#475569" font-family="sans-serif">Air (n = 1,00)</text>
  <text x="60" y="120" font-size="11" fill="#0369a1" font-weight="bold" font-family="sans-serif">Water (n = 1,33)</text>
  <text x="60" y="190" font-size="11" fill="#0f172a" font-weight="bold" font-family="sans-serif">Crown Glass (n = 1,52)</text>
  <line x1="140" y1="30" x2="200" y2="80" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="200" y1="80" x2="245" y2="150" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="245" y1="150" x2="280" y2="220" stroke="#2563eb" stroke-width="2.5"/>
</svg>"""

    prompt = (
        f"A ray of light in air strikes a horizontal layer of water ($n_2 = 1{{,}}33$) floating on crown glass "
        f"($n_3 = 1{{,}}52$) at an angle of incidence of **${theta_air}^\\circ$**.\n\n"
        f"1. Calculate the angle of refraction inside the water layer ($\\theta_2$).\n"
        f"2. Calculate the angle of refraction inside the crown glass ($\\theta_3$).\n"
        f"3. Show that the final angle $\\theta_3$ depends only on $n_1, \\theta_1$ and $n_3$, independent of the intermediate water layer."
    )
    ans = f"1. theta2 = {_fmt_sa(round(theta_w, 1))} deg; 2. theta3 = {_fmt_sa(round(theta_g, 1))} deg; 3. n1 sin(theta1) = n2 sin(theta2) = n3 sin(theta3)."
    memo = (
        f"1. Angle in water [2]:\n"
        f"   $$(1{{,}}00) \\sin({theta_air}^\\circ) = (1{{,}}33) \\sin \\theta_2 \\implies \\theta_2 = {_fmt_sa(round(theta_w, 1))}^\\circ$$ [A]\n"
        f"2. Angle in glass [2]:\n"
        f"   $$(1{{,}}33) \\sin({_fmt_sa(round(theta_w, 1))}^\\circ) = (1{{,}}52) \\sin \\theta_3 \\implies \\theta_3 = {_fmt_sa(round(theta_g, 1))}^\\circ$$ [A]\n"
        f"3. Invariant chain [2]: By consecutive Snell's laws, $n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2 = n_3 \\sin \\theta_3$. "
        f"Thus $n_1 \\sin \\theta_1 = n_3 \\sin \\theta_3$, meaning the intermediate layer does not alter the final direction of propagation [A]."
    )
    return {
        "id": _make_id("optics_23", seed, 23),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "hints": {
            "tier_1": "Apply Snell's Law across each boundary sequentially.",
            "tier_2": "$n_1 \\sin \\theta_1 = n_2 \\sin \\theta_2 = n_3 \\sin \\theta_3$.",
            "tier_3": f"$\\theta_2 = {_fmt_sa(round(theta_w, 1))}^\\circ$, $\\theta_3 = {_fmt_sa(round(theta_g, 1))}^\\circ$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["multi_layer_boundary_angle_mismatch", "intermediate_layer_impact_misunderstood"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Calculation of angle in water", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Calculation of angle in glass", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Proof of independence from intermediate layer", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 24: Semi-circular glass block refraction at curved vs flat surface
# ==============================================================================
def builder_24_semi_circular_glass_block_refraction_at_curved_vs_flat_surface(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_glass = rng.choice([1.50, 1.52, 1.55])
    theta_c = round(math.degrees(math.asin(1.0 / n_glass)), 1)
    test_angle = rng.choice([30, 40, 48, 55])
    is_tir = test_angle > theta_c

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <path d="M 150,140 A 100,100 0 0,1 350,140 Z" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
  <circle cx="250" cy="140" r="3" fill="#0f172a"/>
  <text x="245" y="155" font-size="11" fill="#0f172a" font-family="sans-serif">O</text>
  <line x1="{250 - int(120 * math.cos(math.radians(test_angle)))}" y1="{140 - int(120 * math.sin(math.radians(test_angle)))}" x2="250" y2="140" stroke="#dc2626" stroke-width="2.5"/>
  <text x="120" y="80" font-size="11" fill="#dc2626" font-family="sans-serif">Incident along radius</text>
  <text x="280" y="190" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Semi-circular Block (n = {_fmt_sa(n_glass)})</text>
</svg>"""

    prompt = (
        f"A ray of light is directed towards the centre $O$ of the flat face of a semi-circular glass block "
        f"($n = {_fmt_sa(n_glass)}$, critical angle $\\theta_c = {_fmt_sa(theta_c)}^\\circ$). The ray strikes the curved edge "
        f"at an angle of incidence of **${test_angle}^\\circ$** to the normal at the flat face.\n\n"
        f"1. Explain why the ray passes through the curved outer surface without any refraction (bending).\n"
        f"2. Predict whether the ray will undergo total internal reflection or refract into the air at the flat face."
    )
    ans = f"1. The ray travels along a radius and strikes the curved surface at 90 deg (normal incidence); 2. {'TIR occurs' if is_tir else 'Refracts into air'} because {test_angle} deg is {'>' if is_tir else '<'} {_fmt_sa(theta_c)} deg."
    memo = (
        f"1. Zero deviation at curved surface [2]: Any ray directed toward the centre $O$ travels along a radius of the semi-circle. "
        f"A radius is perpendicular to the tangent of the curve at every point, meaning the angle of incidence is $0^\\circ$ relative to the normal. "
        f"Hence $\\theta_r = 0^\\circ$ and the ray enters without bending [A].\n"
        f"2. Flat surface prediction [2]: At the flat face, the ray travels from glass into air (denser to less dense). "
        f"Since the angle of incidence (${test_angle}^\\circ$) is **{'>' if is_tir else '<'}** the critical angle (${_fmt_sa(theta_c)}^\\circ$), "
        f"the ray will **{'undergo TOTAL INTERNAL REFLECTION' if is_tir else 'REFRACT OUT INTO THE AIR'}** [A]."
    )
    return {
        "id": _make_id("optics_24", seed, 24),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Rays aimed at the centre of a circle are normal to the circular arc.",
            "tier_2": f"Compare incident angle {test_angle} degrees with critical angle {_fmt_sa(theta_c)} degrees.",
            "tier_3": f"{'TIR occurs' if is_tir else 'Refracts into air'}.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["radial_incidence_bending_misconception", "curved_surface_normal_misidentified"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Explanation of radial normal incidence", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Correct prediction comparing angle to theta_c", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 25: Geometrical optics diagnostic misconception autopsy part1
# ==============================================================================
def builder_25_geometrical_optics_diagnostic_misconception_autopsy_part1(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_mat = rng.choice([1.45, 1.55, 1.65])
    theta_c = round(math.degrees(math.asin(1.0 / n_mat)), 1)
    angle_surface = rng.choice([30, 40, 50])
    angle_inc = 90 - angle_surface

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="110" width="400" height="110" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
  <text x="60" y="70" font-size="12" fill="#991b1b" font-weight="bold" font-family="sans-serif">Air (n = 1,00)</text>
  <text x="60" y="150" font-size="12" fill="#991b1b" font-weight="bold" font-family="sans-serif">Medium (n = {_fmt_sa(n_mat)}, &theta;c = {_fmt_sa(theta_c)}&deg;)</text>
  <line x1="250" y1="20" x2="250" y2="210" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5"/>
  <line x1="150" y1="50" x2="250" y2="110" stroke="#b91c1c" stroke-width="3"/>
  <text x="170" y="100" font-size="11" fill="#b91c1c" font-family="sans-serif">{angle_surface}&deg; to surface</text>
  <text x="210" y="140" font-size="12" fill="#0f172a" font-weight="bold" font-family="sans-serif">Autopsy Desk</text>
</svg>"""

    prompt = (
        f"A learner analyzing a ray of light entering a block of material ($n = {_fmt_sa(n_mat)}$) writes the following in a test:\n"
        f"\"The ray makes an angle of ${angle_surface}^\\circ$ with the surface, so the angle of incidence is $\\theta_i = {angle_surface}^\\circ$. "
        f"Because this angle is less than $\\theta_c = {_fmt_sa(theta_c)}^\\circ$, the ray cannot experience total internal reflection, but if light were "
        f"entering from air at an angle $> {_fmt_sa(theta_c)}^\\circ$, it would undergo total internal reflection.\"\n\n"
        f"Identify and rectify the THREE major conceptual physics errors in the learner's statement."
    )
    ans = "1. Angle of incidence is measured to the normal (90 - angle), not the surface; 2. TIR can NEVER occur when entering from air into a denser medium; 3. Angle of incidence in this case is actually 90 - angle."
    memo = (
        f"Diagnostic Autopsy [3]:\n"
        f"1. **Glancing angle vs Incident angle error [1]**: The angle of incidence is ALWAYS measured relative to the normal line, "
        f"not the surface. Here $\\theta_i = 90^\\circ - {angle_surface}^\\circ = {angle_inc}^\\circ$ [A].\n"
        f"2. **TIR directionality violation [1]**: Total internal reflection can **NEVER** occur when light enters an optically denser medium from air. "
        f"It requires light traveling from a denser medium toward a less dense medium ($n_1 > n_2$) [A].\n"
        f"3. **Refraction law violation [1]**: When light enters from air into glass, the refracted ray bends towards the normal and ALWAYS enters the medium, "
        f"regardless of the incident angle [A]."
    )
    return {
        "id": _make_id("optics_25", seed, 25),
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 3,
        "hints": {
            "tier_1": "Angles are measured to the normal, not the boundary.",
            "tier_2": "Can light undergo TIR when going from AIR into glass?",
            "tier_3": "TIR requires traveling from denser to rarer medium. Angle to normal is 90 - surface angle.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["glancing_angle_confused_with_normal", "tir_impossible_entering_denser_medium"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Identification of glancing angle error", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identification of TIR impossible from air into dense medium", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Correct calculation of true angle of incidence", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


BUILDERS_01_25 = [
    builder_01_rectilinear_propagation_and_shadow_formation,
    builder_02_law_of_reflection_plane_mirror,
    builder_03_refractive_index_and_wave_speed,
    builder_04_wavelength_change_in_refraction_frequency_constant,
    builder_05_optical_density_and_ray_bending_towards_away_normal,
    builder_06_snells_law_solve_angle_of_refraction,
    builder_07_snells_law_solve_angle_of_incidence,
    builder_08_snells_law_solve_refractive_index_of_unknown_medium,
    builder_09_rectangular_glass_block_lateral_displacement_parallel_emergence,
    builder_10_apparent_depth_real_depth_refraction,
    builder_11_critical_angle_definition_and_formula,
    builder_12_critical_angle_calculation_dense_to_air,
    builder_13_critical_angle_calculation_between_two_dense_media,
    builder_14_total_internal_reflection_two_conditions_evaluation,
    builder_15_tir_in_45_degree_right_angle_prisms_periscope,
    builder_16_tir_in_porro_prisms_binoculars,
    builder_17_optical_fibre_core_cladding_acceptance_angle,
    builder_18_triangular_prism_minimum_deviation_angle,
    builder_19_dispersion_of_white_light_prism_refractive_index_vs_wavelength,
    builder_20_atmospheric_refraction_mirages_and_delayed_sunset,
    builder_21_diamond_brilliance_critical_angle_cut_geometry,
    builder_22_snells_law_graphical_analysis_sin_theta_i_vs_sin_theta_r,
    builder_23_multi_layer_parallel_refraction_air_water_glass,
    builder_24_semi_circular_glass_block_refraction_at_curved_vs_flat_surface,
    builder_25_geometrical_optics_diagnostic_misconception_autopsy_part1,
]
