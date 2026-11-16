"""Grade 11 Physical Sciences: Geometrical Optics & Wavefronts (Subskills 26–50)
Focus: Lenses, Optical Instruments, Wavefronts, Huygens' Principle & Single-Slit Diffraction.

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
# SUBSKILL 26: Thin converging lens focal point and principal rays
# ==============================================================================
def builder_26_thin_converging_lens_focal_point_and_principal_rays(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    f_cm = rng.choice([10, 12, 15, 20])
    d_o = rng.choice([25, 30, 35, 40])
    # 1/di = 1/f - 1/do
    d_i = round((f_cm * d_o) / (d_o - f_cm), 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="30" y1="120" x2="470" y2="120" stroke="#0f172a" stroke-width="2"/>
  <!-- Converging lens -->
  <ellipse cx="250" cy="120" rx="8" ry="85" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
  <circle cx="{250 - f_cm*7}" cy="120" r="4" fill="#0284c7"/>
  <circle cx="{250 + f_cm*7}" cy="120" r="4" fill="#0284c7"/>
  <text x="{245 - f_cm*7}" y="140" font-size="11" fill="#0284c7" font-family="sans-serif">F1</text>
  <text x="{245 + f_cm*7}" y="140" font-size="11" fill="#0284c7" font-family="sans-serif">F2</text>
  <text x="235" y="25" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Convex Lens (f = {f_cm} cm)</text>
  <!-- Object -->
  <line x1="120" y1="120" x2="120" y2="60" stroke="#16a34a" stroke-width="3"/>
  <polygon points="115,65 120,55 125,65" fill="#16a34a"/>
  <!-- Principal rays -->
  <line x1="120" y1="60" x2="250" y2="60" stroke="#dc2626" stroke-width="1.5"/>
  <line x1="250" y1="60" x2="420" y2="170" stroke="#dc2626" stroke-width="1.5"/>
  <line x1="120" y1="60" x2="420" y2="185" stroke="#2563eb" stroke-width="1.5"/>
</svg>"""

    prompt = (
        f"A thin biconvex (converging) glass lens has a focal length of **${f_cm}\\text{{ cm}}$**. "
        f"An upright object is placed at a distance of **${d_o}\\text{{ cm}}$** in front of the lens.\n\n"
        f"1. Define the 'principal focus' ($F$) of a converging lens.\n"
        f"2. Describe the paths of the THREE standard principal construction rays used to locate the image geometrically."
    )
    ans = "1. Point where rays parallel to principal axis converge after refraction; 2. Ray 1 parallel to axis refracts through F2; Ray 2 through optical centre undeviated; Ray 3 through F1 refracts parallel to axis."
    memo = (
        f"1. Definition [2]: The principal focus of a converging lens is the point on the principal axis through which rays "
        f"incident parallel to the axis pass (converge) after refracting through the lens [A].\n"
        f"2. Three standard principal rays [3]:\n"
        f"   - **Ray 1**: Incident parallel to the principal axis, refracts through the principal focus ($F_2$) on the opposite side [1].\n"
        f"   - **Ray 2**: Passes through the optical centre ($O$) of the lens undeviated in a straight line [1].\n"
        f"   - **Ray 3**: Passes through the front focus ($F_1$) before the lens, refracting parallel to the principal axis [1]."
    )
    return {
        "id": _make_id("optics_26", seed, 26),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Think about parallel rays converging at F.",
            "tier_2": "Ray through optical center does not bend. Ray parallel to axis bends through focus.",
            "tier_3": "Ray 1: parallel -> F2. Ray 2: through O undeviated. Ray 3: through F1 -> parallel.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["principal_focus_definition_ambiguous", "principal_ray_rules_confused"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Definition of principal focus", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Ray 1 description", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Ray 2 description", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Ray 3 description", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 27: Thin diverging lens virtual focus and ray diagram
# ==============================================================================
def builder_27_thin_diverging_lens_virtual_focus_and_ray_diagram(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    f_neg = rng.choice([-10, -15, -20])
    d_o = rng.choice([20, 30, 40])
    # 1/di = 1/f - 1/do => di = (f*do)/(do - f)
    d_i = round((f_neg * d_o) / (d_o - f_neg), 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="30" y1="120" x2="470" y2="120" stroke="#0f172a" stroke-width="2"/>
  <!-- Diverging lens profile -->
  <path d="M 245,35 C 255,80 255,160 245,205 L 255,205 C 245,160 245,80 255,35 Z" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>
  <circle cx="{250 + f_neg*5}" cy="120" r="4" fill="#4f46e5"/>
  <text x="{240 + f_neg*5}" y="140" font-size="11" fill="#4f46e5" font-family="sans-serif">F</text>
  <text x="210" y="25" font-size="12" fill="#4338ca" font-weight="bold" font-family="sans-serif">Concave Lens (f = {f_neg} cm)</text>
  <!-- Diverging rays -->
  <line x1="120" y1="60" x2="250" y2="60" stroke="#dc2626" stroke-width="1.5"/>
  <line x1="250" y1="60" x2="420" y2="10" stroke="#dc2626" stroke-width="1.5"/>
  <line x1="{250 + f_neg*5}" y1="120" x2="250" y2="60" stroke="#dc2626" stroke-dasharray="3,3" stroke-width="1.5"/>
</svg>"""

    prompt = (
        f"A thin biconcave (diverging) lens has a focal length of **${f_neg}\\text{{ cm}}$** (using the Cartesian sign convention).\n\n"
        f"1. Explain why the focal point of a concave lens is termed a 'virtual' focus.\n"
        f"2. State the THREE image characteristics (nature, orientation, relative size) formed by a diverging lens for ANY real object position."
    )
    ans = "1. Refracted rays diverge and only appear to originate from the focus when extrapolated backward; 2. Virtual, upright, and diminished."
    memo = (
        f"1. Virtual focus explanation [2]: Incident rays parallel to the principal axis diverge after passing through the lens. "
        f"They do not actually pass through the focal point, but their backward extensions (extrapolated rays) intersect at a common point on the axis [A].\n"
        f"2. Image characteristics [3]: For any real object positioned in front of a diverging lens, the image is ALWAYS:\n"
        f"   - **Virtual** (formed on the same side as the object, cannot be projected onto a screen) [1]\n"
        f"   - **Upright** (erect, same vertical orientation as object) [1]\n"
        f"   - **Diminished** (smaller in height than the object, $|m| < 1$) [1]."
    )
    return {
        "id": _make_id("optics_27", seed, 27),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Diverging lenses spread rays outward. Trace rays backward to find the virtual focus.",
            "tier_2": "A concave lens always produces the same type of image regardless of object distance.",
            "tier_3": "Virtual focus because rays diverge; image is always virtual, upright, and diminished.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["diverging_lens_real_image_assumption", "virtual_focus_definition_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Virtual focus explanation", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Image nature (virtual)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Image orientation (upright)", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Image size (diminished)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 28: Lens equation converging real image
# ==============================================================================
def builder_28_lens_equation_converging_real_image(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    f = rng.choice([10.0, 12.0, 15.0, 20.0])
    d_o = round(rng.choice([1.5, 2.0, 2.5, 3.0]) * f, 1)
    # 1/di = 1/f - 1/do => di = (f*do)/(do - f)
    d_i = round((f * d_o) / (d_o - f), 1)
    m = round(-d_i / d_o, 2)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="30" y1="120" x2="470" y2="120" stroke="#0f172a" stroke-width="2"/>
  <ellipse cx="250" cy="120" rx="6" ry="80" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
  <text x="210" y="25" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Converging Lens (f = {_fmt_sa(f)} cm)</text>
  <line x1="{250 - int(d_o * 4.5)}" y1="120" x2="{250 - int(d_o * 4.5)}" y2="60" stroke="#16a34a" stroke-width="3"/>
  <line x1="{250 + int(d_i * 4.5)}" y1="120" x2="{250 + int(d_i * 4.5)}" y2="{120 - int(m * 60)}" stroke="#dc2626" stroke-width="3"/>
  <text x="{240 - int(d_o * 4.5)}" y="140" font-size="11" fill="#16a34a" font-family="sans-serif">do = {_fmt_sa(d_o)} cm</text>
  <text x="{240 + int(d_i * 4.5)}" y="140" font-size="11" fill="#dc2626" font-family="sans-serif">di = {_fmt_sa(d_i)} cm</text>
</svg>"""

    prompt = (
        f"An object is positioned at a distance of **${_fmt_sa(d_o)}\\text{{ cm}}$** in front of a thin converging lens "
        f"with a focal length of **${_fmt_sa(f)}\\text{{ cm}}$**.\n\n"
        f"1. Use the thin lens formula $$\\frac{{1}}{{f}} = \\frac{{1}}{{d_o}} + \\frac{{1}}{{d_i}}$$ to calculate the image distance ($d_i$) in centimetres.\n"
        f"2. Calculate the magnification ($m$).\n"
        f"3. State whether the image is real or virtual, and give the mathematical justification based on your calculated $d_i$."
    )
    ans = f"1. di = {_fmt_sa(d_i)} cm; 2. m = {_fmt_sa(m)}; 3. Real, because di > 0 (formed on opposite side of lens)."
    memo = (
        f"1. Lens formula calculation [3]:\n"
        f"   $$\\frac{{1}}{{f}} = \\frac{{1}}{{d_o}} + \\frac{{1}}{{d_i}} \\implies \\frac{{1}}{{d_i}} = \\frac{{1}}{{f}} - \\frac{{1}}{{d_o}}$$ [M]\n"
        f"   $$\\frac{{1}}{{d_i}} = \\frac{{1}}{{{_fmt_sa(f)}}} - \\frac{{1}}{{{_fmt_sa(d_o)}}} = \\frac{{{_fmt_sa(d_o)} - {_fmt_sa(f)}}}{{{_fmt_sa(f)} \\times {_fmt_sa(d_o)}}}$$\n"
        f"   $$d_i = \\frac{{{_fmt_sa(f)} \\times {_fmt_sa(d_o)}}}{{{_fmt_sa(d_o)} - {_fmt_sa(f)}}} = {_fmt_sa(d_i)}\\text{{ cm}}$$ [A]\n"
        f"2. Magnification [2]:\n"
        f"   $$m = -\\frac{{d_i}}{{d_o}} = -\\frac{{{_fmt_sa(d_i)}}}{{{_fmt_sa(d_o)}}} = {_fmt_sa(m)}$$ [A]\n"
        f"3. Nature [1]: Real image, because $d_i > 0$ (light rays converge physically on the far side of the lens) [A]."
    )
    return {
        "id": _make_id("optics_28", seed, 28),
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "hints": {
            "tier_1": "$1/d_i = 1/f - 1/d_o$.",
            "tier_2": f"$1/d_i = 1/{_fmt_sa(f)} - 1/{_fmt_sa(d_o)}$.",
            "tier_3": f"$d_i = {_fmt_sa(d_i)}\\text{{ cm}}$, $m = {_fmt_sa(m)}$. Positive $d_i$ indicates a real image.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["lens_fraction_subtraction_error", "magnification_sign_misunderstood"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Lens equation rearrangement", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculation of image distance with unit", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Calculation of linear magnification", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Real nature justified via positive di", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 29: Lens equation converging virtual image magnifying glass
# ==============================================================================
def builder_29_lens_equation_converging_virtual_image_magnifying_glass(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    f = rng.choice([10.0, 15.0, 20.0])
    d_o = round(rng.choice([0.4, 0.5, 0.6, 0.75]) * f, 1)
    d_i = round((f * d_o) / (d_o - f), 1)  # negative
    m = round(-d_i / d_o, 2)  # positive > 1

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="30" y1="140" x2="470" y2="140" stroke="#0f172a" stroke-width="2"/>
  <ellipse cx="320" cy="140" rx="6" ry="75" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
  <text x="250" y="30" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Simple Magnifier (do &lt; f)</text>
  <!-- Object inside focus -->
  <line x1="{320 - int(d_o * 8)}" y1="140" x2="{320 - int(d_o * 8)}" y2="100" stroke="#16a34a" stroke-width="3"/>
  <text x="{305 - int(d_o * 8)}" y="160" font-size="11" fill="#16a34a" font-family="sans-serif">Object</text>
  <!-- Virtual magnified image -->
  <line x1="{320 + int(d_i * 4)}" y1="140" x2="{320 + int(d_i * 4)}" y2="{140 - int(m * 40)}" stroke="#dc2626" stroke-dasharray="3,3" stroke-width="3"/>
  <text x="{300 + int(d_i * 4)}" y="160" font-size="11" fill="#dc2626" font-family="sans-serif">Virtual Image</text>
</svg>"""

    prompt = (
        f"A magnifying glass consists of a converging lens of focal length **${_fmt_sa(f)}\\text{{ cm}}$**. "
        f"A stamp is placed at a distance of **${_fmt_sa(d_o)}\\text{{ cm}}$** in front of the lens.\n\n"
        f"1. Calculate the image distance ($d_i$) and interpret the physical meaning of its algebraic sign.\n"
        f"2. Calculate the magnification ($m$) of the stamp.\n"
        f"3. State why this configuration produces an upright image rather than an inverted image."
    )
    ans = f"1. di = {_fmt_sa(d_i)} cm (negative indicates virtual image on same side as object); 2. m = {_fmt_sa(m)}; 3. Object lies inside the focal point (do < f)."
    memo = (
        f"1. Image distance [3]:\n"
        f"   $$\\frac{{1}}{{d_i}} = \\frac{{1}}{{f}} - \\frac{{1}}{{d_o}} = \\frac{{1}}{{{_fmt_sa(f)}}} - \\frac{{1}}{{{_fmt_sa(d_o)}}}$$\n"
        f"   $$d_i = \\frac{{{_fmt_sa(f)} \\times {_fmt_sa(d_o)}}}{{{_fmt_sa(d_o)} - {_fmt_sa(f)}}} = {_fmt_sa(d_i)}\\text{{ cm}}$$ [A]\n"
        f"   The negative sign confirms that the image is **virtual** and located on the same side of the lens as the object [A].\n"
        f"2. Magnification [2]:\n"
        f"   $$m = -\\frac{{d_i}}{{d_o}} = -\\frac{{{_fmt_sa(d_i)}}}{{{_fmt_sa(d_o)}}} = {_fmt_sa(m)}$$ [A]\n"
        f"3. Upright explanation [1]: Because the object is placed inside the focal length ($d_o < f$), the refracted rays diverge on exit, "
        f"and their backward extrapolations form an erect virtual image [A]."
    )
    return {
        "id": _make_id("optics_29", seed, 29),
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "hints": {
            "tier_1": "When $d_o < f$, the image distance $d_i$ becomes negative.",
            "tier_2": f"Calculate $d_i = ({f} \\times {d_o}) / ({d_o} - {f})$.",
            "tier_3": f"$d_i = {_fmt_sa(d_i)}\\text{{ cm}}$, $m = {_fmt_sa(m)}$. Upright and virtual.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["negative_image_distance_rejected", "magnifier_focal_position_error"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Calculation of negative di", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Sign interpretation as virtual image", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Magnification calculation", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Condition do < f stated for upright image", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 30: Lens equation diverging virtual diminished image
# ==============================================================================
def builder_30_lens_equation_diverging_virtual_diminished_image(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    f = -rng.choice([10.0, 15.0, 20.0, 25.0])
    d_o = rng.choice([15.0, 20.0, 30.0, 40.0])
    # 1/di = 1/f - 1/do
    d_i = round((f * d_o) / (d_o - f), 1)
    m = round(-d_i / d_o, 2)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="30" y1="130" x2="470" y2="130" stroke="#0f172a" stroke-width="2"/>
  <path d="M 295,45 C 305,90 305,170 295,215 L 305,215 C 295,170 295,90 305,45 Z" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="210" y="30" font-size="12" fill="#4338ca" font-weight="bold" font-family="sans-serif">Diverging Lens (f = {_fmt_sa(f)} cm)</text>
  <line x1="{300 - int(d_o * 4)}" y1="130" x2="{300 - int(d_o * 4)}" y2="70" stroke="#16a34a" stroke-width="3"/>
  <line x1="{300 + int(d_i * 4)}" y1="130" x2="{300 + int(d_i * 4)}" y2="{130 - int(m * 60)}" stroke="#dc2626" stroke-dasharray="3,3" stroke-width="2.5"/>
  <text x="{285 - int(d_o * 4)}" y="150" font-size="11" fill="#16a34a" font-family="sans-serif">do = {_fmt_sa(d_o)} cm</text>
  <text x="{290 + int(d_i * 4)}" y="150" font-size="11" fill="#dc2626" font-family="sans-serif">di = {_fmt_sa(d_i)} cm</text>
</svg>"""

    prompt = (
        f"A diverging lens has a focal length of **${_fmt_sa(f)}\\text{{ cm}}$**. "
        f"An object is placed **${_fmt_sa(d_o)}\\text{{ cm}}$** in front of the lens.\n\n"
        f"1. Use the thin lens equation to calculate the image position ($d_i$).\n"
        f"2. Calculate the magnification ($m$).\n"
        f"3. Explain why the image formed by a diverging lens is always diminished ($|m| < 1$)."
    )
    ans = f"1. di = {_fmt_sa(d_i)} cm; 2. m = {_fmt_sa(m)}; 3. Virtual image is always closer to lens than object (|di| < do), hence magnification |di|/do < 1."
    memo = (
        f"1. Calculation [3]:\n"
        f"   $$\\frac{{1}}{{d_i}} = \\frac{{1}}{{f}} - \\frac{{1}}{{d_o}} = \\frac{{1}}{{{_fmt_sa(f)}}} - \\frac{{1}}{{{_fmt_sa(d_o)}}}$$\n"
        f"   $$d_i = \\frac{{({_fmt_sa(f)}) \\times {_fmt_sa(d_o)}}}{{{_fmt_sa(d_o)} - ({_fmt_sa(f)})}} = {_fmt_sa(d_i)}\\text{{ cm}}$$ [A]\n"
        f"2. Magnification [2]:\n"
        f"   $$m = -\\frac{{d_i}}{{d_o}} = -\\frac{{{_fmt_sa(d_i)}}}{{{_fmt_sa(d_o)}}} = {_fmt_sa(m)}$$ [A]\n"
        f"3. Diminished explanation [1]: The virtual image is always formed between the front focus and the optical centre, "
        f"so $|d_i| < d_o$. Therefore $|m| = |d_i| / d_o < 1$, always producing a diminished image [A]."
    )
    return {
        "id": _make_id("optics_30", seed, 30),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "hints": {
            "tier_1": "Remember that focal length of a diverging lens is NEGATIVE.",
            "tier_2": f"Substitute $f = {_fmt_sa(f)}$ and $d_o = {_fmt_sa(d_o)}$.",
            "tier_3": f"$d_i = {_fmt_sa(d_i)}\\text{{ cm}}$, $m = {_fmt_sa(m)}$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["diverging_lens_positive_focus_error", "diminished_image_ratio_error"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Negative focal length used in formula", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculation of image distance with unit", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Calculation of magnification", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Explanation of diminished property", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 31: Linear magnification and image height calculation
# ==============================================================================
def builder_31_linear_magnification_and_image_height_calculation(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    h_o = rng.choice([2.0, 3.0, 4.0, 5.0])
    d_o = rng.choice([20.0, 30.0, 40.0])
    d_i = rng.choice([40.0, 60.0, 80.0])
    m = round(-d_i / d_o, 2)
    h_i = round(abs(m) * h_o, 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="30" y1="120" x2="470" y2="120" stroke="#0f172a" stroke-width="2"/>
  <ellipse cx="220" cy="120" rx="6" ry="80" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
  <line x1="{220 - int(d_o * 3)}" y1="120" x2="{220 - int(d_o * 3)}" y2="{120 - int(h_o * 10)}" stroke="#16a34a" stroke-width="3"/>
  <line x1="{220 + int(d_i * 2)}" y1="120" x2="{220 + int(d_i * 2)}" y2="{120 + int(h_i * 10)}" stroke="#dc2626" stroke-width="3"/>
  <text x="{205 - int(d_o * 3)}" y="80" font-size="11" fill="#16a34a" font-family="sans-serif">ho = {_fmt_sa(h_o)} cm</text>
  <text x="{205 + int(d_i * 2)}" y="160" font-size="11" fill="#dc2626" font-family="sans-serif">hi = {_fmt_sa(h_i)} cm</text>
</svg>"""

    prompt = (
        f"An object of height **${_fmt_sa(h_o)}\\text{{ cm}}$** is positioned **${_fmt_sa(d_o)}\\text{{ cm}}$** in front of a thin lens. "
        f"A sharp real image is captured on a screen placed **${_fmt_sa(d_i)}\\text{{ cm}}$** behind the lens.\n\n"
        f"1. State the formula for linear magnification ($m$) in terms of image height ($h_i$) and object height ($h_o$), "
        f"as well as in terms of image distance ($d_i$) and object distance ($d_o$).\n"
        f"2. Calculate the linear magnification ($m$).\n"
        f"3. Calculate the height of the image ($h_i$) in centimetres."
    )
    ans = f"1. m = hi/ho = -di/do; 2. m = {_fmt_sa(m)}; 3. hi = {_fmt_sa(h_i)} cm (inverted)"
    memo = (
        f"1. Magnification formulas [2]:\n"
        f"   $$m = \\frac{{h_i}}{{h_o}} = -\\frac{{d_i}}{{d_o}}$$ [A]\n"
        f"2. Magnification calculation [2]:\n"
        f"   $$m = -\\frac{{{_fmt_sa(d_i)}}}{{{_fmt_sa(d_o)}}} = {_fmt_sa(m)}$$ [A]\n"
        f"3. Image height calculation [2]:\n"
        f"   $$|h_i| = |m| \\times h_o = {_fmt_sa(abs(m))} \\times {_fmt_sa(h_o)} = {_fmt_sa(h_i)}\\text{{ cm}}$$ [A]\n"
        f"   (The negative sign in $m$ indicates that the real image is inverted relative to the object)."
    )
    return {
        "id": _make_id("optics_31", seed, 31),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "hints": {
            "tier_1": "$m = -d_i / d_o = h_i / h_o$.",
            "tier_2": f"Calculate $m = -{_fmt_sa(d_i)} / {_fmt_sa(d_o)}$. Then $h_i = |m| \\times h_o$.",
            "tier_3": f"$m = {_fmt_sa(m)}$ and $h_i = {_fmt_sa(h_i)}\\text{{ cm}}$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["magnification_inverted_ratio", "image_height_sign_confusion"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Both magnification formulas stated", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Magnification calculation", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Image height calculation with unit", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 32: Compound microscope or refracting telescope principles
# ==============================================================================
def builder_32_compound_microscope_or_refracting_telescope_principles(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    instrument, fo_cm, fe_cm = rng.choice([
        ("astronomical telescope", 100.0, 5.0),
        ("terrestrial telescope", 80.0, 4.0),
        ("compound microscope", 1.0, 5.0),
    ])
    if "telescope" in instrument:
        mag = round(fo_cm / fe_cm, 1)
        tube_len = round(fo_cm + fe_cm, 1)
        role_desc = "Objective has large focal length to collect maximum light; Eyepiece has short focal length to magnify intermediate real image."
    else:
        mag = 100  # qualitative
        tube_len = 16.0
        role_desc = "Objective has very short focal length to form a magnified real image; Eyepiece acts as a magnifier to produce a final virtual image."

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="30" y1="120" x2="470" y2="120" stroke="#0f172a" stroke-width="2"/>
  <ellipse cx="140" cy="120" rx="8" ry="70" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
  <ellipse cx="380" cy="120" rx="6" ry="50" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="110" y="40" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Objective (fo = {_fmt_sa(fo_cm)} cm)</text>
  <text x="350" y="55" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Eyepiece (fe = {_fmt_sa(fe_cm)} cm)</text>
  <text x="210" y="210" font-size="12" fill="#0f172a" font-weight="bold" font-family="sans-serif">{instrument.title()}</text>
</svg>"""

    prompt = (
        f"A two-lens optical instrument is constructed as an **{instrument}** with an objective lens "
        f"of focal length **${_fmt_sa(fo_cm)}\\text{{ cm}}$** and an eyepiece of focal length **${_fmt_sa(fe_cm)}\\text{{ cm}}$**.\n\n"
        f"1. Explain the role of the objective lens in forming the intermediate image.\n"
        f"2. Explain how the eyepiece acts as a simple magnifier on that intermediate image.\n"
        f"3. For a telescope in normal adjustment, calculate the angular magnification ($M = f_o / f_e$) "
        f"and the length of the telescope tube ($L = f_o + f_e$)."
    )
    ans = f"1. Objective forms real inverted intermediate image; 2. Eyepiece forms virtual, enlarged final image; 3. M = {_fmt_sa(mag)}, Tube length L = {_fmt_sa(tube_len)} cm."
    memo = (
        f"1. Objective role [2]: {role_desc} It forms an intermediate, real, inverted image [A].\n"
        f"2. Eyepiece role [2]: The intermediate image is positioned inside the focal length of the eyepiece ($d_o < f_e$), "
        f"allowing the eyepiece to act as a magnifying glass that produces a magnified virtual final image [A].\n"
        f"3. Telescope parameters [2]:\n"
        f"   $$M = \\frac{{f_o}}{{f_e}} = \\frac{{{_fmt_sa(fo_cm)}}}{{{_fmt_sa(fe_cm)}}} = {_fmt_sa(mag)}$$ [A]\n"
        f"   $$L = f_o + f_e = {_fmt_sa(fo_cm)} + {_fmt_sa(fe_cm)} = {_fmt_sa(tube_len)}\\text{{ cm}}$$ [A]"
    )
    return {
        "id": _make_id("optics_32", seed, 32),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "hints": {
            "tier_1": "Objective forms real intermediate image; eyepiece magnifies it.",
            "tier_2": "In normal adjustment: $M = f_o / f_e$ and $L = f_o + f_e$.",
            "tier_3": f"Magnification = {_fmt_sa(mag)}, tube length = {_fmt_sa(tube_len)} cm.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["telescope_magnification_inverted_ratio", "intermediate_image_nature_misunderstood"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Role of objective lens explained", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Role of eyepiece explained", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Magnification and tube length calculation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 33: Wavefront definition and ray perpendicularity
# ==============================================================================
def builder_33_wavefront_definition_and_ray_perpendicularity(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    src_type = rng.choice(["point source", "distant planar source", "line source"])
    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <!-- Plane wavefronts -->
  <line x1="80" y1="40" x2="80" y2="200" stroke="#0284c7" stroke-width="3"/>
  <line x1="140" y1="40" x2="140" y2="200" stroke="#0284c7" stroke-width="3"/>
  <line x1="200" y1="40" x2="200" y2="200" stroke="#0284c7" stroke-width="3"/>
  <line x1="260" y1="40" x2="260" y2="200" stroke="#0284c7" stroke-width="3"/>
  <!-- Wave rays perpendicular -->
  <line x1="50" y1="80" x2="350" y2="80" stroke="#dc2626" stroke-width="2.5"/>
  <line x1="50" y1="160" x2="350" y2="160" stroke="#dc2626" stroke-width="2.5"/>
  <text x="360" y="85" font-size="12" fill="#dc2626" font-family="sans-serif">Ray (Wave direction)</text>
  <text x="85" y="30" font-size="11" fill="#0284c7" font-family="sans-serif">Wavefronts (in phase)</text>
  <polygon points="340,75 355,80 340,85" fill="#dc2626"/>
  <polygon points="340,155 355,160 340,165" fill="#dc2626"/>
  <!-- 90 deg marker -->
  <rect x="140" y="80" width="10" height="10" fill="none" stroke="#0f172a"/>
</svg>"""

    prompt = (
        f"Waves propagating through a uniform medium can be described using both wave rays and wavefronts (e.g. from a {src_type}).\n\n"
        f"1. Define the term 'wavefront'.\n"
        f"2. State the geometric relationship between a wave ray (direction of wave propagation) and the wavefront at every point.\n"
        f"3. Explain what physical distance corresponds to the separation between two consecutive wavefronts in phase."
    )
    ans = "1. An imaginary line or surface joining all adjacent points vibrating in phase; 2. Rays are perpendicular (at 90 degrees) to wavefronts; 3. One wavelength (lambda)."
    memo = (
        f"1. Definition [2]: A wavefront is an imaginary line or surface connecting adjacent points of a wave that are in the same phase of oscillation (e.g. all crests or all troughs) [A].\n"
        f"2. Geometric relationship [1]: Wave rays are always **perpendicular ($90^\\circ$)** to the wavefronts at every point [A].\n"
        f"3. Separation distance [1]: The distance between two consecutive in-phase wavefronts equals **one wavelength ($\\lambda$)** [A]."
    )
    return {
        "id": _make_id("optics_33", seed, 33),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Wavefront connects points in the same phase (e.g. all crests).",
            "tier_2": "Rays show the direction of energy propagation.",
            "tier_3": "Wavefront: surface in phase; Rays are perpendicular (90 deg) to wavefronts; Separation is wavelength lambda.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["wavefront_ray_parallel_confusion", "wavefront_separation_period_confusion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Accurate definition of wavefront", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Statement of perpendicular relationship", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Distance between wavefronts identified as wavelength", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 34: Circular vs plane wavefronts propagation
# ==============================================================================
def builder_34_circular_vs_plane_wavefronts_propagation(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    lambda_cm = rng.choice([2.0, 3.0, 4.0, 5.0])
    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <!-- Circular wavefronts from point source -->
  <circle cx="120" cy="120" r="20" fill="none" stroke="#2563eb" stroke-width="2"/>
  <circle cx="120" cy="120" r="45" fill="none" stroke="#2563eb" stroke-width="2"/>
  <circle cx="120" cy="120" r="70" fill="none" stroke="#2563eb" stroke-width="2"/>
  <circle cx="120" cy="120" r="95" fill="none" stroke="#2563eb" stroke-width="2"/>
  <circle cx="120" cy="120" r="4" fill="#0f172a"/>
  <text x="70" y="230" font-size="12" fill="#1e293b" font-weight="bold" font-family="sans-serif">Circular Wavefronts</text>
  <!-- Plane wavefronts -->
  <line x1="330" y1="40" x2="330" y2="200" stroke="#059669" stroke-width="2.5"/>
  <line x1="365" y1="40" x2="365" y2="200" stroke="#059669" stroke-width="2.5"/>
  <line x1="400" y1="40" x2="400" y2="200" stroke="#059669" stroke-width="2.5"/>
  <line x1="435" y1="40" x2="435" y2="200" stroke="#059669" stroke-width="2.5"/>
  <text x="330" y="230" font-size="12" fill="#1e293b" font-weight="bold" font-family="sans-serif">Plane Wavefronts (&lambda; = {_fmt_sa(lambda_cm)} cm)</text>
</svg>"""

    prompt = (
        f"In a ripple tank experiment, waves with wavelength **$\\lambda = {_fmt_sa(lambda_cm)}\\text{{ cm}}$** are generated.\n\n"
        f"1. Contrast circular (spherical) wavefronts produced by a point dipper with plane wavefronts produced by a straight bar dipper.\n"
        f"2. Explain why circular wavefronts from a distant source (such as starlight reaching Earth) can be accurately approximated as plane wavefronts."
    )
    ans = "1. Point dipper radiates concentric circles with radial rays; straight dipper produces parallel straight lines with parallel rays; 2. At very large radius of curvature, the arc curvature is negligible, resembling a flat plane."
    memo = (
        f"1. Contrast [2]:\n"
        f"   - **Circular wavefronts**: Form concentric circles radiating outward from a single point disturbance, with rays diverging radially [1].\n"
        f"   - **Plane wavefronts**: Form parallel straight lines moving in a single direction, with rays that are parallel to one another [1].\n"
        f"2. Distant source approximation [2]: As the distance $r$ from a point source becomes very large, the radius of curvature approaches infinity ($R \\to \\infty$). "
        f"Over any small observation aperture on Earth, the curved wavefront is indistinguishable from a straight, flat plane [A]."
    )
    return {
        "id": _make_id("optics_34", seed, 34),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Point source produces circular ripples; straight vibrator produces plane ripples.",
            "tier_2": "Think about the Earth looking flat to an observer on the ground because the sphere is so large.",
            "tier_3": "Concentric vs parallel; very large radius of curvature approximates a plane wavefront.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["wavefront_curvature_radius_scaling_error", "circular_vs_plane_ray_direction_confusion"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Contrast between circular and plane wavefronts", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Large radius curvature explanation for distant plane approximation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 35: Huygens' principle statement and secondary wavelets
# ==============================================================================
def builder_35_huygens_principle_statement_and_secondary_wavelets(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    c_speed = rng.choice([2.0, 3.0, 4.0])
    dt = 0.5
    r_wavelet = round(c_speed * dt, 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <!-- Primary wavefront -->
  <line x1="80" y1="40" x2="80" y2="200" stroke="#0f172a" stroke-width="3"/>
  <text x="40" y="30" font-size="11" fill="#0f172a" font-weight="bold" font-family="sans-serif">Primary Wavefront (t)</text>
  <!-- Secondary point sources -->
  <circle cx="80" cy="70" r="4" fill="#dc2626"/>
  <circle cx="80" cy="120" r="4" fill="#dc2626"/>
  <circle cx="80" cy="170" r="4" fill="#dc2626"/>
  <!-- Secondary wavelets (radius v*dt) -->
  <path d="M 80,30 A 40,40 0 0,1 80,110" fill="none" stroke="#f87171" stroke-dasharray="3,3" stroke-width="2"/>
  <path d="M 80,80 A 40,40 0 0,1 80,160" fill="none" stroke="#f87171" stroke-dasharray="3,3" stroke-width="2"/>
  <path d="M 80,130 A 40,40 0 0,1 80,210" fill="none" stroke="#f87171" stroke-dasharray="3,3" stroke-width="2"/>
  <!-- Tangent envelope (new wavefront) -->
  <line x1="{80 + int(r_wavelet * 25)}" y1="40" x2="{80 + int(r_wavelet * 25)}" y2="200" stroke="#2563eb" stroke-width="3"/>
  <text x="{60 + int(r_wavelet * 25)}" y="30" font-size="11" fill="#2563eb" font-weight="bold" font-family="sans-serif">New Wavefront (t + &Delta;t)</text>
</svg>"""

    prompt = (
        f"Christiaan Huygens proposed a wave construction model to explain wave propagation.\n\n"
        f"1. State Huygens' Principle.\n"
        f"2. Explain how the forward envelope of secondary spherical wavelets forms the new position of the wavefront.\n"
        f"3. Explain why the backward-propagating wavelets are omitted in physical wave propagation."
    )
    ans = "1. Every point on a wavefront acts as a source of secondary spherical wavelets; 2. The common tangent envelope to these wavelets forms the new wavefront; 3. Destructive interference cancels backward wave propagation."
    memo = (
        f"1. Huygens' Principle statement [2]: **Every point on a wavefront acts as a point source of secondary spherical wavelets** "
        f"that spread out in the forward direction at the same speed as the wave. After a time $\\Delta t$, the new position of the wavefront "
        f"is the surface **tangent to all these secondary wavelets** [A].\n"
        f"2. Envelope construction [2]: Each point source emits a wavelet of radius $r = v \\Delta t$. "
        f"The constructive superposition of all these individual spherical crests creates a smooth tangent envelope that constitutes the advanced wavefront [A].\n"
        f"3. Backward propagation [1]: Destructive interference between wavelets prevents backward propagation, ensuring waves propagate purely forward in the direction of energy flow [A]."
    )
    return {
        "id": _make_id("optics_35", seed, 35),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Recall: 'Every point on a wavefront acts as a point source of secondary wavelets...'",
            "tier_2": "The new wavefront is the tangent line/surface enclosing the wavelets.",
            "tier_3": "Statement includes: secondary spherical wavelets, forward direction, tangent surface.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["huygens_principle_statement_imprecise", "wavelet_envelope_geometry_misunderstood"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Statement of Huygens' principle", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Explanation of forward envelope construction", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Explanation of no backward wavelets", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 36: Huygens' construction proving law of reflection
# ==============================================================================
def builder_36_huygens_construction_proving_law_of_reflection(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    angle_i = rng.choice([30, 40, 50, 60])
    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="50" y1="180" x2="450" y2="180" stroke="#0f172a" stroke-width="4"/>
  <text x="210" y="210" font-size="12" fill="#0f172a" font-weight="bold" font-family="sans-serif">Reflecting Surface</text>
  <!-- Incident wavefront AB -->
  <line x1="120" y1="60" x2="200" y2="180" stroke="#2563eb" stroke-width="3"/>
  <text x="110" y="55" font-size="11" fill="#2563eb" font-family="sans-serif">A</text>
  <text x="195" y="195" font-size="11" fill="#2563eb" font-family="sans-serif">B</text>
  <!-- Reflected wavefront CD -->
  <line x1="200" y1="180" x2="320" y2="180" stroke="#059669" stroke-dasharray="3,3" stroke-width="2"/>
  <text x="320" y="195" font-size="11" fill="#059669" font-family="sans-serif">C</text>
  <line x1="240" y1="60" x2="320" y2="180" stroke="#dc2626" stroke-width="3"/>
  <text x="235" y="55" font-size="11" fill="#dc2626" font-family="sans-serif">D</text>
  <text x="220" y="120" font-size="11" fill="#1e293b" font-family="sans-serif">&Delta;t = BC/v = AD/v</text>
</svg>"""

    prompt = (
        f"A plane wavefront strikes a flat reflecting barrier at an angle of incidence **$\\theta_i = {angle_i}^\\circ$**.\n\n"
        f"1. Use Huygens' wave construction to show that the angle of incidence equals the angle of reflection ($\\theta_i = \\theta_r$).\n"
        f"2. Identify the common side and congruent right triangles in the geometric proof."
    )
    ans = "1. In time dt, wave from B reaches C (dist v*dt), while wavelet from A expands into radius v*dt to touch tangent at D. Right triangles ABC and ADC are congruent, so theta_i = theta_r; 2. Common hypotenuse BC/AC and legs AD = BC = v*dt."
    memo = (
        f"1. Proof of reflection via Huygens [3]:\n"
        f"   - Let the incident wavefront strike the mirror at point $A$ at time $t=0$, while end $B$ is still traveling towards point $C$ on the mirror [1].\n"
        f"   - In time $\\Delta t$, point $B$ travels distance $BC = v \\Delta t$ to reach the surface at $C$. "
        f"During this same time $\\Delta t$, the secondary wavelet emitted from point $A$ expands into a hemisphere of radius $AD = v \\Delta t$ [1].\n"
        f"   - The tangent line $CD$ from $C$ to the wavelet represents the reflected wavefront [1].\n"
        f"2. Congruence of triangles [2]:\n"
        f"   - Triangles $\\triangle ABC$ and $\\triangle ADC$ share common hypotenuse $AC$ [1].\n"
        f"   - Both are right-angled ($\\angle B = \\angle D = 90^\\circ$), and leg $BC = AD = v \\Delta t$ [1].\n"
        f"   - By the RHS congruence theorem, $\\triangle ABC \\cong \\triangle ADC$, which implies $\\theta_i = \\theta_r$ [A]."
    )
    return {
        "id": _make_id("optics_36", seed, 36),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Compare the distance traveled in air by both ends of the wavefront during time interval dt.",
            "tier_2": "The two triangles share the mirror boundary as hypotenuse and have equal legs $v \\Delta t$.",
            "tier_3": "Congruent right triangles prove that angle of incidence equals angle of reflection.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["huygens_reflection_geometric_congruence_error", "wavefront_triangle_orientation_confusion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Wavelet radius and distance relation shown", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Identification of congruent triangles with RHS", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Conclusion theta_i = theta_r stated", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 37: Huygens' construction proving Snell's law of refraction
# ==============================================================================
def builder_37_huygens_construction_proving_snells_law_of_refraction(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    v1_ratio = 1.00
    v2_ratio = rng.choice([0.66, 0.75, 0.60])
    n2 = round(1.0 / v2_ratio, 2)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="120" width="400" height="100" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
  <line x1="50" y1="120" x2="450" y2="120" stroke="#0f172a" stroke-width="2"/>
  <text x="60" y="60" font-size="12" fill="#475569" font-family="sans-serif">Medium 1 (Speed v1)</text>
  <text x="60" y="160" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Medium 2 (Speed v2 &lt; v1, n = {_fmt_sa(n2)})</text>
  <!-- Incident and refracted wavefronts -->
  <line x1="140" y1="40" x2="220" y2="120" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="220" y1="120" x2="280" y2="190" stroke="#dc2626" stroke-width="2.5"/>
  <text x="150" y="100" font-size="11" fill="#2563eb" font-family="sans-serif">v1 &Delta;t</text>
  <text x="260" y="150" font-size="11" fill="#dc2626" font-family="sans-serif">v2 &Delta;t</text>
</svg>"""

    prompt = (
        f"A plane wavefront passes from medium 1 (wave speed $v_1$) into medium 2 (wave speed $v_2 < v_1$), "
        f"where the refractive index of medium 2 is **${_fmt_sa(n2)}$**.\n\n"
        f"1. Use Huygens' principle to derive Snell's Law in the form $$\\frac{{\\sin \\theta_1}}{{\\sin \\theta_2}} = \\frac{{v_1}}{{v_2}} = \\frac{{n_2}}{{n_1}}$$\n"
        f"2. Explain why the wavefront bends towards the normal when passing into a medium where wave speed decreases."
    )
    ans = "1. sin(theta1) = v1*dt / L and sin(theta2) = v2*dt / L, dividing gives sin(theta1)/sin(theta2) = v1/v2 = n2/n1; 2. The side of the wavefront entering first slows down while the outer part continues at higher speed, pivoting the wavefront towards the normal."
    memo = (
        f"1. Huygens Snell derivation [3]:\n"
        f"   - Let the wavefront intersect the interface along common length $L$ between points $A$ and $C$ [1].\n"
        f"   - In time $\\Delta t$, the wave in medium 1 travels distance $d_1 = v_1 \\Delta t$. In right triangle $\\triangle ABC$: $\\sin \\theta_1 = \\frac{{v_1 \\Delta t}}{{L}}$ [1].\n"
        f"   - In the same time $\\Delta t$, the secondary wavelet in medium 2 spreads to distance $d_2 = v_2 \\Delta t$. In right triangle $\\triangle ADC$: $\\sin \\theta_2 = \\frac{{v_2 \\Delta t}}{{L}}$ [1].\n"
        f"   - Dividing the two equations: $$\\frac{{\\sin \\theta_1}}{{\\sin \\theta_2}} = \\frac{{v_1 \\Delta t / L}}{{v_2 \\Delta t / L}} = \\frac{{v_1}}{{v_2}} = \\frac{{c/n_1}}{{c/n_2}} = \\frac{{n_2}}{{n_1}}$$ [A]\n"
        f"2. Bending explanation [1]: One side of the wavefront enters medium 2 and slows down first, while the remaining portion still in medium 1 continues at higher speed. "
        f"This speed differential pivots the wavefront, turning the wave direction towards the normal [A]."
    )
    return {
        "id": _make_id("optics_37", seed, 37),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Express $\\sin \\theta_1$ and $\\sin \\theta_2$ using the common interface hypotenuse $L$.",
            "tier_2": "$\\sin \\theta_1 = (v_1 \\Delta t)/L$ and $\\sin \\theta_2 = (v_2 \\Delta t)/L$.",
            "tier_3": "Divide both expressions to get $\\sin \\theta_1 / \\sin \\theta_2 = v_1 / v_2 = n_2 / n_1$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["huygens_refraction_derivation_algebra_error", "speed_ratio_inverted_in_snell"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Geometric expressions for sin(theta1) and sin(theta2)", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Derivation of ratio v1/v2 = n2/n1", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Physical explanation of wavefront pivoting", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 38: Diffraction definition and wave nature evidence
# ==============================================================================
def builder_38_diffraction_definition_and_wave_nature_evidence(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    wave_type = rng.choice(["monochromatic laser light", "sound waves", "ocean water waves"])
    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <!-- Barrier with slit -->
  <line x1="200" y1="20" x2="200" y2="90" stroke="#0f172a" stroke-width="6"/>
  <line x1="200" y1="150" x2="200" y2="220" stroke="#0f172a" stroke-width="6"/>
  <!-- Plane waves approaching -->
  <line x1="80" y1="30" x2="80" y2="210" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="120" y1="30" x2="120" y2="210" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="160" y1="30" x2="160" y2="210" stroke="#2563eb" stroke-width="2.5"/>
  <!-- Diffracted circular waves -->
  <path d="M 200,90 A 30,30 0 0,1 200,150" fill="none" stroke="#dc2626" stroke-width="2.5"/>
  <path d="M 200,70 A 50,50 0 0,1 200,170" fill="none" stroke="#dc2626" stroke-width="2.5"/>
  <path d="M 200,50 A 70,70 0 0,1 200,190" fill="none" stroke="#dc2626" stroke-width="2.5"/>
  <text x="50" y="230" font-size="12" fill="#2563eb" font-family="sans-serif">Plane Waves</text>
  <text x="260" y="230" font-size="12" fill="#dc2626" font-family="sans-serif">Diffracted Circular Waves into Shadow Zone</text>
</svg>"""

    prompt = (
        f"Diffraction is a characteristic property demonstrated by all wave phenomena, including **{wave_type}**.\n\n"
        f"1. Define the term 'diffraction'.\n"
        f"2. Explain why diffraction cannot be explained by classical ray (particle) models of light.\n"
        f"3. State how the observation of light diffraction proves the wave nature of light."
    )
    ans = "1. Bending of waves around corners or edges of an obstacle, or through an aperture into the region of geometrical shadow; 2. Particles travel in straight lines and would create sharp-edged shadows without spreading; 3. Spreading and interference fringes are exclusive wave characteristics."
    memo = (
        f"1. Definition [2]: Diffraction is the **bending (spreading) of waves** around the edges of an obstacle or through an aperture (opening) "
        f"into the region of geometrical shadow [A].\n"
        f"2. Failure of ray/particle model [2]: Under a pure particle or geometric ray model, light travels in strictly straight lines and would produce "
        f"a sharply defined illuminated patch with crisp shadows. Particles cannot spontaneously curve around corners into the shadow region [A].\n"
        f"3. Wave nature proof [1]: The observed spreading and resulting interference fringe patterns can only be modeled through the superposition "
        f"of Huygens wavelets, confirming conclusively that light propagates as a wave [A]."
    )
    return {
        "id": _make_id("optics_38", seed, 38),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Diffraction involves bending around corners into the shadow region.",
            "tier_2": "Particles cannot bend around sharp corners without external forces.",
            "tier_3": "Wave nature proof: interference patterns and spreading into shadow zones.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["diffraction_refraction_confusion", "geometrical_shadow_bending_misunderstood"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Accurate definition of diffraction", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Explanation of particle model limitation", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Proof of wave nature concluded", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 39: Diffraction qualitative aperture size vs wavelength ratio
# ==============================================================================
def builder_39_diffraction_qualitative_aperture_size_vs_wavelength_ratio(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    lambda_mm = rng.choice([5.0, 10.0, 15.0])
    a_small = lambda_mm
    a_large = 6 * lambda_mm

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <!-- Narrow slit: pronounced spreading -->
  <line x1="120" y1="20" x2="120" y2="85" stroke="#0f172a" stroke-width="4"/>
  <line x1="120" y1="115" x2="120" y2="180" stroke="#0f172a" stroke-width="4"/>
  <path d="M 120,85 A 30,30 0 0,1 120,115" fill="none" stroke="#2563eb" stroke-width="2"/>
  <path d="M 120,70 A 50,50 0 0,1 120,130" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="30" y="210" font-size="11" fill="#2563eb" font-family="sans-serif">Slit a &approx; &lambda; (Pronounced)</text>
  <!-- Wide slit: negligible spreading -->
  <line x1="360" y1="20" x2="360" y2="60" stroke="#0f172a" stroke-width="4"/>
  <line x1="360" y1="140" x2="360" y2="180" stroke="#0f172a" stroke-width="4"/>
  <line x1="380" y1="65" x2="440" y2="65" stroke="#dc2626" stroke-width="2"/>
  <line x1="380" y1="135" x2="440" y2="135" stroke="#dc2626" stroke-width="2"/>
  <text x="270" y="210" font-size="11" fill="#dc2626" font-family="sans-serif">Slit a &gt;&gt; &lambda; (Negligible / Straight)</text>
</svg>"""

    prompt = (
        f"A series of water waves with wavelength **$\\lambda = {_fmt_sa(lambda_mm)}\\text{{ mm}}$** approaches an opening (slit) in a barrier.\n\n"
        f"1. Describe the wavefront appearance after passing through a narrow aperture of width $a = {_fmt_sa(a_small)}\\text{{ mm}}$ ($a \\approx \\lambda$).\n"
        f"2. Describe the wavefront appearance after passing through a wide aperture of width $a = {_fmt_sa(a_large)}\\text{{ mm}}$ ($a \\gg \\lambda$).\n"
        f"3. State the general condition under which significant (pronounced) diffraction occurs."
    )
    ans = f"1. Circular wavefronts with pronounced spreading; 2. Straight plane waves with slight edge curving (straight beam); 3. Significant diffraction occurs when wavelength is comparable to or greater than aperture width (lambda/a >= 1)."
    memo = (
        f"1. Narrow slit ($a \\approx \\lambda$) [1]: Waves spread out radially in circular wavefronts, acting as a virtual point source with **pronounced diffraction** [A].\n"
        f"2. Wide slit ($a \\gg \\lambda$) [1]: Waves pass straight through the centre as plane waves with almost no spreading, with only minimal curving at the sharp outer edges (**negligible diffraction**) [A].\n"
        f"3. General diffraction condition [2]: Pronounced diffraction occurs when the wavelength is comparable to or larger than the slit width: $$\\frac{{\\lambda}}{{a}} \\ge 1 \\quad \\text{{or}} \\quad \\lambda \\approx a$$ [A]"
    )
    return {
        "id": _make_id("optics_39", seed, 39),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Compare the wavelength $\\lambda$ to the aperture width $a$.",
            "tier_2": "When $a \\approx \\lambda$, waves bend circular. When $a \\gg \\lambda$, waves pass straight through.",
            "tier_3": "Condition for pronounced diffraction: $\\lambda / a \\ge 1$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["diffraction_aperture_ratio_inverted", "wide_slit_spreading_misconception"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Description of narrow slit circular wave pattern", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Description of wide slit plane wave pattern", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "General condition lambda/a >= 1 stated", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 40: Single-slit diffraction pattern central broad maximum
# ==============================================================================
def builder_40_single_slit_diffraction_pattern_central_broad_maximum(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    laser_color, lambda_nm = rng.choice([
        ("red helium-neon", 633),
        ("green diode", 532),
        ("blue argon", 488),
    ])
    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#0f172a"/>
  <!-- Seed: {seed} -->
  <!-- Central broad bright band -->
  <rect x="200" y="30" width="100" height="40" fill="{ '#ef4444' if 'red' in laser_color else ('#22c55e' if 'green' in laser_color else '#3b82f6') }" opacity="0.95"/>
  <!-- First secondary bands (dimmer, narrower) -->
  <rect x="130" y="35" width="45" height="30" fill="{ '#ef4444' if 'red' in laser_color else ('#22c55e' if 'green' in laser_color else '#3b82f6') }" opacity="0.35"/>
  <rect x="325" y="35" width="45" height="30" fill="{ '#ef4444' if 'red' in laser_color else ('#22c55e' if 'green' in laser_color else '#3b82f6') }" opacity="0.35"/>
  <!-- Dark minima bands -->
  <rect x="175" y="30" width="25" height="40" fill="#0f172a"/>
  <rect x="300" y="30" width="25" height="40" fill="#0f172a"/>
  <text x="170" y="105" font-size="12" fill="#f8fafc" font-family="sans-serif">Central Maximum (Width 2w)</text>
  <text x="70" y="150" font-size="11" fill="#94a3b8" font-family="sans-serif">Dark Minima</text>
  <text x="320" y="150" font-size="11" fill="#94a3b8" font-family="sans-serif">Secondary Maxima</text>
  <text x="150" y="210" font-size="13" fill="#38bdf8" font-weight="bold" font-family="sans-serif">{laser_color.title()} Laser (&lambda; = {lambda_nm} nm)</text>
</svg>"""

    prompt = (
        f"Monochromatic light from a **{laser_color}** laser ($\\lambda = {lambda_nm}\\text{{ nm}}$) passes through a "
        f"single narrow vertical slit and falls onto a white viewing screen.\n\n"
        f"1. Describe the visual appearance of the single-slit diffraction pattern observed on the screen.\n"
        f"2. State TWO ways in which the central bright band differs from the secondary bright bands.\n"
        f"3. Explain in terms of wave interference what condition produces the dark fringes on either side."
    )
    ans = "1. Alternating bright and dark horizontal bands with a broad, intense central maximum; 2. Central maximum is twice as wide and much brighter (higher intensity); 3. Destructive interference where path difference between wavelets is an integer multiple of wavelength."
    memo = (
        f"1. Appearance [2]: A pattern of alternating bright and dark fringes consisting of a **very bright, broad central maximum** "
        f"flanked by symmetrical, increasingly dimmer and narrower secondary maxima separated by dark minima [A].\n"
        f"2. Differences of central maximum [2]:\n"
        f"   - **Width**: The central maximum is **twice as wide** ($2\\theta_1$) as the secondary bright bands [1].\n"
        f"   - **Intensity (brightness)**: The central maximum contains ~85% of total light energy and is **substantially brighter** than secondary maxima [1].\n"
        f"3. Dark fringe mechanism [1]: Dark bands occur due to **complete destructive interference**, where Huygens wavelets from the top and bottom halves "
        f"of the slit arrive out of phase with a path difference of $\\lambda/2$ (giving zero resultant amplitude) [A]."
    )
    return {
        "id": _make_id("optics_40", seed, 40),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Single-slit pattern has a prominent central maximum twice as wide as the outer fringes.",
            "tier_2": "Central band is twice as wide and much brighter than any secondary band.",
            "tier_3": "Dark fringes arise from destructive interference (path difference = m*lambda).",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["central_maximum_width_equal_assumption", "destructive_vs_constructive_condition_confused"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Description of alternating fringe pattern", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Two differences (width and intensity)", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Destructive interference mechanism explained", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 41: Single-slit diffraction first minimum condition formula
# ==============================================================================
def builder_41_single_slit_diffraction_first_minimum_condition_formula(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    lambda_nm = rng.choice([450, 532, 633, 680])
    a_microns = rng.choice([15.0, 20.0, 25.0, 30.0, 40.0])
    lambda_m = lambda_nm * 1e-9
    a_m = a_microns * 1e-6
    sin_theta = lambda_m / a_m
    theta_deg = math.degrees(math.asin(sin_theta))

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <!-- Slit barrier -->
  <line x1="80" y1="20" x2="80" y2="105" stroke="#0f172a" stroke-width="4"/>
  <line x1="80" y1="135" x2="80" y2="220" stroke="#0f172a" stroke-width="4"/>
  <text x="25" y="125" font-size="11" fill="#0f172a" font-family="sans-serif">a = {_fmt_sa(a_microns)} &mu;m</text>
  <!-- Screen -->
  <line x1="420" y1="20" x2="420" y2="220" stroke="#64748b" stroke-width="3"/>
  <text x="430" y="40" font-size="11" fill="#64748b" font-family="sans-serif">Screen</text>
  <!-- Central line and angle theta -->
  <line x1="80" y1="120" x2="420" y2="120" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="80" y1="120" x2="420" y2="60" stroke="#dc2626" stroke-width="2"/>
  <text x="140" y="110" font-size="11" fill="#dc2626" font-family="sans-serif">&theta;1</text>
  <text x="430" y="65" font-size="11" fill="#dc2626" font-weight="bold" font-family="sans-serif">1st Minimum</text>
  <text x="200" y="210" font-size="12" fill="#2563eb" font-family="sans-serif">&lambda; = {lambda_nm} nm</text>
</svg>"""

    prompt = (
        f"Monochromatic light of wavelength **${lambda_nm}\\text{{ nm}}$** passes through a single slit of width "
        f"**${_fmt_sa(a_microns)}\\mu\\text{{m}}$**.\n\n"
        f"1. State the formula for the angular position ($\\theta_m$) of the dark minima in a single-slit diffraction pattern.\n"
        f"2. Calculate the angular position ($\\theta_1$) of the FIRST diffraction minimum in degrees."
    )
    ans = f"1. sin(theta_m) = m*lambda / a (m = 1, 2, 3...); 2. theta_1 = {_fmt_sa(round(theta_deg, 3))} degrees"
    memo = (
        f"1. Formula [2]: The condition for dark minima in single-slit diffraction is: $$\\sin \\theta_m = \\frac{{m \\lambda}}{{a}} \\quad (m = \\pm 1, \\pm 2, \\pm 3, \\dots)$$ [A]\n"
        f"2. Calculation for first minimum ($m = 1$) [3]:\n"
        f"   $$\\sin \\theta_1 = \\frac{{\\lambda}}{{a}} = \\frac{{{lambda_nm} \\times 10^{{-9}}}}{{{_fmt_sa(a_microns)} \\times 10^{{-6}}}} = {sin_theta:.5f}$$ [M]\n"
        f"   $$\\theta_1 = \\sin^{{-1}}({sin_theta:.5f}) = {_fmt_sa(round(theta_deg, 3))}^\\circ$$ [A]"
    )
    return {
        "id": _make_id("optics_41", seed, 41),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Single-slit minima condition: $\\sin \\theta = m \\lambda / a$.",
            "tier_2": f"Convert units: $\\lambda = {lambda_nm} \\times 10^{{-9}}\\text{{ m}}$, $a = {_fmt_sa(a_microns)} \\times 10^{{-6}}\\text{{ m}}$.",
            "tier_3": f"$\\theta_1 = \\arcsin({sin_theta:.5f}) = {_fmt_sa(round(theta_deg, 3))}^\\circ$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["single_slit_minimum_formula_unit_conversion_error", "maxima_vs_minima_formula_inversion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Statement of formula sin(theta_m) = m*lambda/a", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Correct unit conversion and substitution", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Angle in degrees calculated", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 42: Single-slit diffraction angular width of central maximum
# ==============================================================================
def builder_42_single_slit_diffraction_angular_width_of_central_maximum(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    lambda_nm = rng.choice([500, 600, 650])
    a_microns = rng.choice([10.0, 12.0, 15.0, 20.0])
    d_screen_m = rng.choice([1.2, 1.5, 2.0])
    lambda_m = lambda_nm * 1e-9
    a_m = a_microns * 1e-6
    sin_theta = lambda_m / a_m
    theta_rad = sin_theta  # small angle approximation
    ang_width_rad = 2 * theta_rad
    ang_width_deg = math.degrees(ang_width_rad)
    # Linear width on screen W = 2 * D * tan(theta) approx 2 * D * lambda / a
    linear_w_cm = round(2 * d_screen_m * (lambda_m / a_m) * 100, 2)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="80" y1="20" x2="80" y2="220" stroke="#0f172a" stroke-width="4"/>
  <line x1="420" y1="20" x2="420" y2="220" stroke="#64748b" stroke-width="3"/>
  <line x1="80" y1="120" x2="420" y2="120" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.5"/>
  <line x1="80" y1="120" x2="420" y2="80" stroke="#2563eb" stroke-width="1.5"/>
  <line x1="80" y1="120" x2="420" y2="160" stroke="#2563eb" stroke-width="1.5"/>
  <line x1="420" y1="80" x2="420" y2="160" stroke="#dc2626" stroke-width="5"/>
  <text x="430" y="125" font-size="11" fill="#dc2626" font-family="sans-serif">Width W = {_fmt_sa(linear_w_cm)} cm</text>
  <text x="210" y="140" font-size="11" fill="#475569" font-family="sans-serif">D = {_fmt_sa(d_screen_m)} m</text>
</svg>"""

    prompt = (
        f"A single slit of width **${_fmt_sa(a_microns)}\\mu\\text{{m}}$** is illuminated by laser light of wavelength "
        f"**${lambda_nm}\\text{{ nm}}$**. A viewing screen is placed **${_fmt_sa(d_screen_m)}\\text{{ m}}$** from the slit.\n\n"
        f"1. State the relationship between the angular width of the central maximum ($2\\theta_1$) and the first minimum position ($\\theta_1$).\n"
        f"2. Calculate the angular width of the central maximum in degrees.\n"
        f"3. Calculate the linear width ($W$) of the central maximum on the screen in centimetres."
    )
    ans = f"1. Angular width is 2*theta_1; 2. 2*theta_1 = {_fmt_sa(round(ang_width_deg, 3))} degrees; 3. Linear width W = {_fmt_sa(linear_w_cm)} cm"
    memo = (
        f"1. Angular width relation [1]: The central maximum extends from $-\\theta_1$ to $+\\theta_1$, so its total angular width is $2\\theta_1$ [A].\n"
        f"2. Angular width calculation [2]:\n"
        f"   $$\\theta_1 \\approx \\sin \\theta_1 = \\frac{{\\lambda}}{{a}} = \\frac{{{lambda_nm} \\times 10^{{-9}}}}{{{_fmt_sa(a_microns)} \\times 10^{{-6}}}} = {theta_rad:.5f}\\text{{ rad}}$$\n"
        f"   $$2\\theta_1 = 2({math.degrees(theta_rad):.3f}^\\circ) = {_fmt_sa(round(ang_width_deg, 3))}^\\circ$$ [A]\n"
        f"3. Linear width calculation [3]:\n"
        f"   $$W = 2 D \\tan \\theta_1 \\approx \\frac{{2 D \\lambda}}{{a}}$$ [M]\n"
        f"   $$W = \\frac{{2 \\times {_fmt_sa(d_screen_m)} \\times ({lambda_nm} \\times 10^{{-9}})}}{{{_fmt_sa(a_microns)} \\times 10^{{-6}}}} = {linear_w_cm / 100:.4f}\\text{{ m}} = {_fmt_sa(linear_w_cm)}\\text{{ cm}}$$ [A]"
    )
    return {
        "id": _make_id("optics_42", seed, 42),
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 6,
        "hints": {
            "tier_1": "Central maximum width is $2 \\times \\theta_1$.",
            "tier_2": "Linear width on screen is $W = 2 D \\lambda / a$.",
            "tier_3": f"Angular width = {_fmt_sa(round(ang_width_deg, 3))}^\\circ$, linear width = {_fmt_sa(linear_w_cm)} cm.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["central_maximum_half_width_reported", "small_angle_linear_width_factor_2_omitted"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Relationship 2*theta1 stated", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculation of angular width in degrees", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Calculation of linear width with units", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 43: Single-slit effect of decreasing increasing slit width
# ==============================================================================
def builder_43_single_slit_effect_of_decreasing_increasing_slit_width(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    change_type = rng.choice(["DECREASED", "INCREASED"])
    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="30" width="400" height="80" fill="#0f172a"/>
  <!-- Original slit pattern -->
  <rect x="220" y="45" width="60" height="20" fill="#ef4444" opacity="0.9"/>
  <rect x="180" y="47" width="25" height="16" fill="#ef4444" opacity="0.4"/>
  <rect x="295" y="47" width="25" height="16" fill="#ef4444" opacity="0.4"/>
  <text x="60" y="95" font-size="11" fill="#f8fafc" font-family="sans-serif">Initial Slit Width a</text>
  <!-- Modified slit pattern -->
  <rect x="50" y="130" width="400" height="80" fill="#0f172a"/>
  <rect x="{ 170 if change_type == 'DECREASED' else 235 }" y="145" width="{ 160 if change_type == 'DECREASED' else 30 }" height="20" fill="#ef4444" opacity="{ 0.6 if change_type == 'DECREASED' else 1.0 }"/>
  <text x="60" y="195" font-size="11" fill="#f8fafc" font-family="sans-serif">Slit Width {change_type}</text>
</svg>"""

    prompt = (
        f"A student observing a single-slit diffraction pattern on a screen modifies the experimental apparatus "
        f"such that the slit width $a$ is **{change_type}** while keeping the laser wavelength and screen distance constant.\n\n"
        f"1. Predict the effect on the width of the central bright maximum (broader, narrower, or unchanged). Explain using a mathematical formula.\n"
        f"2. Predict the effect on the peak intensity (brightness) of the central maximum."
    )
    ans = f"1. Width becomes {'BROADER' if change_type == 'DECREASED' else 'NARROWER'} because width is inversely proportional to slit width (W proportional to 1/a); 2. Intensity {'DECREASES' if change_type == 'DECREASED' else 'INCREASES'}."
    memo = (
        f"1. Width effect [3]:\n"
        f"   - The angular half-width is given by $\\sin \\theta_1 = \\frac{{\\lambda}}{{a}}$, meaning $\\theta_1 \\propto \\frac{{1}}{{a}}$ [M].\n"
        f"   - When the slit width $a$ is **{change_type}**, the central maximum becomes **{'BROADER (wider spreading)' if change_type == 'DECREASED' else 'NARROWER (less spreading)'}** [A].\n"
        f"2. Intensity effect [2]: Peak intensity is proportional to $a^2$. When slit width is {change_type.lower()}, "
        f"the total light energy transmitted is {'less' if change_type == 'DECREASED' else 'greater'}, "
        f"so the peak brightness **{'DECREASES' if change_type == 'DECREASED' else 'INCREASES'}** [A]."
    )
    return {
        "id": _make_id("optics_43", seed, 43),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Recall: Width $\\propto 1/a$. Smaller aperture = greater diffraction spreading.",
            "tier_2": "Narrower slit gives broader, dimmer fringes.",
            "tier_3": f"Width becomes {'broader' if change_type == 'DECREASED' else 'narrower'}. Intensity {'decreases' if change_type == 'DECREASED' else 'increases'}.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["slit_width_direct_proportionality_misconception", "diffraction_intensity_scaling_error"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Formula theta = lambda/a referenced", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Correct prediction and explanation of width change", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Correct prediction and explanation of intensity change", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 44: Single-slit effect of changing wavelength red vs blue light
# ==============================================================================
def builder_44_single_slit_effect_of_changing_wavelength_red_vs_blue_light(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    lambda_red = 650
    lambda_blue = 450
    ratio = round(lambda_red / lambda_blue, 2)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="25" width="400" height="90" fill="#0f172a"/>
  <!-- Red fringe: wide -->
  <rect x="180" y="45" width="140" height="25" fill="#ef4444" opacity="0.9"/>
  <text x="60" y="100" font-size="11" fill="#fca5a5" font-family="sans-serif">Red Light (&lambda; = {lambda_red} nm): Wide Central Band</text>
  <rect x="50" y="130" width="400" height="90" fill="#0f172a"/>
  <!-- Blue fringe: narrower -->
  <rect x="205" y="150" width="90" height="25" fill="#3b82f6" opacity="0.9"/>
  <text x="60" y="205" font-size="11" fill="#93c5fd" font-family="sans-serif">Blue Light (&lambda; = {lambda_blue} nm): Narrower Central Band</text>
</svg>"""

    prompt = (
        f"A single slit of fixed width is illuminated sequentially with red light ($\\lambda_{{\\text{{red}}}} = {lambda_red}\\text{{ nm}}$) "
        f"and then blue light ($\\lambda_{{\\text{{blue}}}} = {lambda_blue}\\text{{ nm}}$).\n\n"
        f"1. State which light colour produces a broader central diffraction maximum.\n"
        f"2. Explain your answer using the relationship between wavelength and diffraction spreading.\n"
        f"3. Calculate the ratio of the width of the red central band to that of the blue central band."
    )
    ans = f"1. Red light; 2. Diffraction width is directly proportional to wavelength (sin(theta) proportional to lambda); 3. Ratio = {_fmt_sa(ratio)}"
    memo = (
        f"1. Color prediction [1]: **Red light** produces a broader central maximum [A].\n"
        f"2. Scientific explanation [2]: The angular spreading of diffraction is directly proportional to wavelength: $$\\sin \\theta_1 = \\frac{{\\lambda}}{{a}} \\implies \\theta_1 \\propto \\lambda$$ [M]\n"
        f"   Since red light has a longer wavelength than blue light (${lambda_red}\\text{{ nm}} > {lambda_blue}\\text{{ nm}}$), it diffracts (spreads) through a larger angle [A].\n"
        f"3. Ratio calculation [2]:\n"
        f"   $$\\frac{{W_{{\\text{{red}}}}}}{{W_{{\\text{{blue}}}}}} = \\frac{{\\lambda_{{\\text{{red}}}}}}{{\\lambda_{{\\text{{blue}}}}}} = \\frac{{{lambda_red}}}{{{lambda_blue}}} = {_fmt_sa(ratio)}$$ [A]"
    )
    return {
        "id": _make_id("optics_44", seed, 44),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Longer wavelength = greater diffraction. Red light has longer wavelength than blue light.",
            "tier_2": "Width $\\propto \\lambda$.",
            "tier_3": f"Red light spreads more. Ratio = {lambda_red} / {lambda_blue} = {_fmt_sa(ratio)}.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["blue_light_greater_diffraction_misconception", "wavelength_width_ratio_inversion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Red light correctly identified", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explanation of direct proportionality to wavelength", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Ratio calculated", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 45: Single-slit white light diffraction colored fringes
# ==============================================================================
def builder_45_single_slit_white_light_diffraction_colored_fringes(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#0f172a"/>
  <!-- Seed: {seed} -->
  <!-- Central white band with colored edges -->
  <rect x="210" y="60" width="80" height="40" fill="#f8fafc"/>
  <rect x="195" y="60" width="15" height="40" fill="#3b82f6"/>
  <rect x="180" y="60" width="15" height="40" fill="#ef4444"/>
  <rect x="290" y="60" width="15" height="40" fill="#3b82f6"/>
  <rect x="305" y="60" width="15" height="40" fill="#ef4444"/>
  <text x="180" y="140" font-size="12" fill="#f8fafc" font-weight="bold" font-family="sans-serif">Central White Band</text>
  <text x="70" y="180" font-size="11" fill="#ef4444" font-family="sans-serif">Red (outer, most bent)</text>
  <text x="320" y="180" font-size="11" fill="#3b82f6" font-family="sans-serif">Violet/Blue (inner, least bent)</text>
</svg>"""

    prompt = (
        "White light containing all visible wavelengths ($400\\text{ nm}$ to $700\\text{ nm}$) is passed through a single narrow slit.\n\n"
        "1. Describe the colour observed at the EXACT centre of the central maximum, and explain why.\n"
        "2. Describe the appearance of the edges of the central maximum, specifying which colour appears on the INNER edge and which appears on the OUTER edge.\n"
        "3. Explain why the secondary maxima appear as overlapping spectral rainbow colours."
    )
    ans = "1. Pure white, because all wavelengths have zero path difference and overlap constructively; 2. Inner edge is blue/violet (shorter wavelength, less spreading), outer edge is red (longer wavelength, more spreading); 3. Each wavelength has a different diffraction angle (theta = lambda/a), separating the colors into mini-spectra."
    memo = (
        "1. Centre colour [2]: At the exact centre ($\\theta = 0^\\circ$), the path difference for ALL visible wavelengths is zero. "
        "All colours undergo constructive interference simultaneously, recombining to produce **pure white light** [A].\n"
        "2. Edge appearance [2]: Because $\\sin \\theta = \\lambda / a$:\n"
        "   - **Violet/Blue** (shortest $\\lambda \\approx 400\\text{ nm}$) spreads the least, forming the **inner edge** [1].\n"
        "   - **Red** (longest $\\lambda \\approx 700\\text{ nm}$) spreads the most, forming the **outer edge** [1].\n"
        "3. Secondary maxima [1]: Each secondary maximum is dispersed into a continuous rainbow spectrum because each colour's peak occurs at an angle proportional to its wavelength [A]."
    )
    return {
        "id": _make_id("optics_45", seed, 45),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "At $\\theta = 0$, all colors combine constructively to give white.",
            "tier_2": "Red light has longer wavelength, so it diffracts further out than blue.",
            "tier_3": "Centre is white; inner edge is blue/violet; outer edge is red.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["white_light_dispersion_edge_color_order_inverted", "central_maximum_color_confusion"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "White centre explained via zero path difference", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Inner blue / outer red edge identified", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Secondary spectral rainbow explanation", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 46: Single-slit intensity distribution profile analysis
# ==============================================================================
def builder_46_single_slit_intensity_distribution_profile_analysis(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    i_0 = 100.0  # arbitrary relative intensity
    i_1 = round(i_0 * (2.0 / (3 * math.pi))**2, 1)  # approx 4.5%
    i_2 = round(i_0 * (2.0 / (5 * math.pi))**2, 1)  # approx 1.6%

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <line x1="40" y1="200" x2="460" y2="200" stroke="#0f172a" stroke-width="2"/>
  <line x1="250" y1="20" x2="250" y2="200" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1.5"/>
  <text x="210" y="225" font-size="12" fill="#0f172a" font-family="sans-serif">&theta; (Angle)</text>
  <text x="15" y="100" font-size="12" fill="#0f172a" font-family="sans-serif" transform="rotate(-90,20,100)">Intensity (I)</text>
  <!-- Sinc squared profile -->
  <path d="M 70,198 Q 110,190 130,195 T 160,200 Q 185,185 200,200 Q 225,50 250,30 Q 275,50 300,200 Q 315,185 340,200 T 370,195 Q 390,190 430,198" fill="none" stroke="#2563eb" stroke-width="3"/>
  <text x="255" y="35" font-size="11" fill="#2563eb" font-weight="bold" font-family="sans-serif">Io ({_fmt_sa(i_0)}%)</text>
  <text x="325" y="175" font-size="10" fill="#dc2626" font-family="sans-serif">I1 &approx; {_fmt_sa(i_1)}%</text>
  <text x="185" y="215" font-size="10" fill="#475569" font-family="sans-serif">-&lambda;/a</text>
  <text x="295" y="215" font-size="10" fill="#475569" font-family="sans-serif">+&lambda;/a</text>
</svg>"""

    prompt = (
        "The graph of relative intensity $I$ versus angle $\\theta$ for a single-slit diffraction pattern is characterized by a "
        "dominant central peak and rapid fall-off for secondary maxima.\n\n"
        "1. State the formula for the positions of the minima (zeros of intensity) in terms of $\\lambda$ and $a$.\n"
        "2. State the approximate relative intensity of the first secondary maximum as a percentage of the central peak intensity ($I_0$).\n"
        "3. Explain why the intensity drops off so dramatically for higher-order secondary maxima."
    )
    ans = f"1. sin(theta) = m*lambda / a (m = +/-1, +/-2...); 2. Approx 4.5% (or 4-5%); 3. Wavelets from most of the slit interfere destructively, leaving only a small uncancelled fraction of the aperture to contribute light."
    memo = (
        "1. Minima positions [1]: Intensity falls to zero at $\\sin \\theta = \\frac{m \\lambda}{a}$ for $m = \\pm 1, \\pm 2, \\dots$ [A].\n"
        f"2. Relative intensity [2]: The first secondary maximum has an intensity of approximately **{_fmt_sa(i_1)}\\%** ($I_1 \\approx \\frac{{4}}{{9\\pi^2}} I_0 \\approx 4{{,}}5\\%$) "
        f"of the central peak intensity [A].\n"
        "3. Dramatic drop-off explanation [2]: For the secondary maxima ($m=1{{,}}5, 2{{,}}5$), the slit is divided into an odd number of zones (3, 5, 7...). "
        "Two-thirds of the slit wavelets cancel each other out in pairs through destructive interference, leaving only an uncancelled $1/3$ (or $1/5$) "
        "of the aperture amplitude to contribute, resulting in $(1/3)^2$ or $(1/5)^2$ fraction of the intensity [A]."
    )
    return {
        "id": _make_id("optics_46", seed, 46),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "The first secondary peak contains less than 5% of the central intensity.",
            "tier_2": "Divide the slit into 3 equal zones; 2 zones cancel each other out.",
            "tier_3": "First secondary intensity is approx 4.5%. Higher orders drop off due to paired destructive cancellation.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["secondary_intensity_overestimated", "slit_zone_cancellation_misunderstood"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Formula for intensity zeros stated", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "First secondary intensity percentage (approx 4.5%)", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Slit zone cancellation explanation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 47: Diffraction of water waves in ripple tank
# ==============================================================================
def builder_47_diffraction_of_water_waves_in_ripple_tank(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    f_hz = rng.choice([5, 8, 10, 12])
    v_cm_s = rng.choice([20, 24, 30])
    lambda_cm = round(v_cm_s / f_hz, 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="30" width="400" height="180" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
  <line x1="220" y1="30" x2="220" y2="90" stroke="#0f172a" stroke-width="6"/>
  <line x1="220" y1="150" x2="220" y2="210" stroke="#0f172a" stroke-width="6"/>
  <text x="70" y="55" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Ripple Tank (f = {f_hz} Hz, v = {v_cm_s} cm/s)</text>
  <!-- Diffracting waves -->
  <path d="M 220,90 A 30,30 0 0,1 220,150" fill="none" stroke="#0284c7" stroke-width="2.5"/>
  <path d="M 220,70 A 50,50 0 0,1 220,170" fill="none" stroke="#0284c7" stroke-width="2.5"/>
  <text x="280" y="125" font-size="11" fill="#0369a1" font-family="sans-serif">&lambda; = {_fmt_sa(lambda_cm)} cm</text>
</svg>"""

    prompt = (
        f"In a ripple tank, a straight vibrator produces plane water waves at a frequency of **${f_hz}\\text{{ Hz}}$** "
        f"traveling at a speed of **${v_cm_s}\\text{{ cm/s}}$** towards a gap between two barriers.\n\n"
        f"1. Calculate the wavelength ($\\lambda$) of the water waves.\n"
        f"2. What gap width $a$ should the teacher choose to demonstrate maximum circular diffraction spreading?\n"
        f"3. State how increasing the vibrator frequency (with water depth and speed constant) will affect the diffraction pattern."
    )
    ans = f"1. lambda = {_fmt_sa(lambda_cm)} cm; 2. Gap width a = {_fmt_sa(lambda_cm)} cm (or a <= {_fmt_sa(lambda_cm)} cm); 3. Higher frequency means shorter wavelength, reducing diffraction spreading."
    memo = (
        f"1. Wavelength calculation [2]:\n"
        f"   $$v = f \\lambda \\implies \\lambda = \\frac{{v}}{{f}} = \\frac{{{v_cm_s}}}{{{f_hz}}} = {_fmt_sa(lambda_cm)}\\text{{ cm}}$$ [A]\n"
        f"2. Slit width for maximum diffraction [1]: To obtain maximum circular spreading, the aperture width should equal or be smaller than the wavelength: $a \\le {_fmt_sa(lambda_cm)}\\text{{ cm}}$ [A].\n"
        f"3. Frequency increase effect [2]: Higher frequency increases $f$, which **decreases wavelength** ($\\lambda = v/f$). "
        f"Since $\\lambda / a$ decreases, the waves will experience **less diffraction spreading**, passing more straight through [A]."
    )
    return {
        "id": _make_id("optics_47", seed, 47),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "$\\lambda = v / f$. Maximum diffraction occurs when $a \\approx \\lambda$.",
            "tier_2": "Higher frequency = shorter wavelength = less diffraction.",
            "tier_3": f"$\\lambda = {_fmt_sa(lambda_cm)}\\text{{ cm}}$. Gap should be $\\le {_fmt_sa(lambda_cm)}\\text{{ cm}}$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["wave_speed_frequency_dependence_error", "ripple_tank_diffraction_frequency_effect_inverted"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Calculation of wavelength with unit", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Gap width condition stated", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Effect of increasing frequency explained", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 48: Sound diffraction around corners vs light diffraction
# ==============================================================================
def builder_48_sound_diffraction_around_corners_vs_light_diffraction(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    f_sound = rng.choice([250, 340, 500])
    v_sound = 340  # m/s
    lambda_sound = round(v_sound / f_sound, 2)
    lambda_light_nm = 550
    door_w = 0.90  # m

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="230" y="20" width="40" height="70" fill="#0f172a"/>
  <rect x="230" y="150" width="40" height="70" fill="#0f172a"/>
  <text x="210" y="140" font-size="11" fill="#475569" font-family="sans-serif">Doorway ({_fmt_sa(door_w)} m)</text>
  <!-- Sound waves bending wide -->
  <path d="M 270,90 A 30,30 0 0,1 270,150" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  <path d="M 270,60 A 60,60 0 0,1 270,180" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  <text x="60" y="70" font-size="12" fill="#2563eb" font-weight="bold" font-family="sans-serif">Sound (&lambda; &approx; {_fmt_sa(lambda_sound)} m &approx; door)</text>
  <!-- Light ray straight through -->
  <line x1="80" y1="120" x2="420" y2="120" stroke="#eab308" stroke-width="4"/>
  <text x="60" y="210" font-size="12" fill="#ca8a04" font-weight="bold" font-family="sans-serif">Light (&lambda; &approx; {lambda_light_nm} nm &lt;&lt; door)</text>
</svg>"""

    prompt = (
        f"A person standing around the corner outside an open classroom door ($w = {_fmt_sa(door_w)}\\text{{ m}}$) "
        f"can easily hear a teacher's voice ($f = {f_sound}\\text{{ Hz}}$, $v = 340\\text{{ m/s}}$), "
        f"but cannot see the teacher.\n\n"
        f"1. Calculate the wavelength of the sound wave emitted by the teacher.\n"
        f"2. Explain why the sound waves diffract significantly around the door frame while visible light "
        f"($\\lambda \\approx {lambda_light_nm}\\text{{ nm}}$) casts a sharp shadow."
    )
    ans = f"1. lambda_sound = {_fmt_sa(lambda_sound)} m; 2. Sound wavelength ({_fmt_sa(lambda_sound)} m) is comparable to the doorway width ({_fmt_sa(door_w)} m), causing strong diffraction, whereas light wavelength ({lambda_light_nm} nm) is a million times smaller than the door, making diffraction negligible."
    memo = (
        f"1. Sound wavelength calculation [2]:\n"
        f"   $$\\lambda_{{\\text{{sound}}}} = \\frac{{v}}{{f}} = \\frac{{340}}{{{f_sound}}} = {_fmt_sa(lambda_sound)}\\text{{ m}}$$ [A]\n"
        f"2. Diffraction comparison [3]:\n"
        f"   - **Sound**: The wavelength of the sound wave (${_fmt_sa(lambda_sound)}\\text{{ m}}$) is comparable to the doorway opening (${_fmt_sa(door_w)}\\text{{ m}}$), "
        f"   yielding $\\frac{{\\lambda}}{{a}} \\approx 1$. Consequently, sound waves undergo pronounced diffraction and bend around the corner into the listener's ear [1].\n"
        f"   - **Light**: Visible light has an extremely tiny wavelength ($\\sim 5{{,}}5 \\times 10^{{-7}}\\text{{ m}}$). The ratio $\\frac{{\\lambda}}{{a}} \\approx 6 \\times 10^{{-7}} \\ll 1$, "
        f"   meaning light travels in essentially straight geometric rays with zero perceptible spreading around large macroscopic obstacles [2]."
    )
    return {
        "id": _make_id("optics_48", seed, 48),
        "term": 2,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 5,
        "hints": {
            "tier_1": "Compare the wavelength of sound and light to the width of the doorway.",
            "tier_2": "Sound: $\\lambda \\approx 1\\text{ m} \\approx a$. Light: $\\lambda \\ll a$.",
            "tier_3": "Sound diffracts because its wavelength matches the doorway size; light wavelength is too small.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["sound_vs_light_diffraction_scale_error", "wavelength_to_aperture_comparison_omitted"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Calculation of sound wavelength", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Sound diffraction justified via lambda/a approx 1", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Light lack of diffraction justified via lambda << a", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 49: Capstone optics wavefront synthesis multi-tier
# ==============================================================================
def builder_49_capstone_optics_wavefront_synthesis_multi_tier(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    n_glass = 1.52
    sin_c = 1.0 / n_glass
    theta_c = round(math.degrees(math.asin(sin_c)), 1)
    lambda_air_nm = 600
    lambda_glass_nm = round(lambda_air_nm / n_glass, 1)

    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="80" width="400" height="130" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="60" y="55" font-size="12" fill="#475569" font-family="sans-serif">Air (n = 1,00)</text>
  <text x="60" y="115" font-size="12" fill="#0369a1" font-weight="bold" font-family="sans-serif">Glass Slab (n = {_fmt_sa(n_glass)})</text>
  <line x1="120" y1="30" x2="190" y2="80" stroke="#dc2626" stroke-width="2.5"/>
  <line x1="190" y1="80" x2="230" y2="210" stroke="#dc2626" stroke-width="2.5"/>
  <text x="210" y="170" font-size="11" fill="#dc2626" font-family="sans-serif">&lambda;glass = {_fmt_sa(lambda_glass_nm)} nm</text>
</svg>"""

    prompt = (
        f"A laser generates monochromatic light of wavelength **${lambda_air_nm}\\text{{ nm}}$** in air.\n"
        f"The light beam strikes a glass slab of refractive index **${_fmt_sa(n_glass)}$**.\n\n"
        f"1. Calculate the speed and wavelength of this light inside the glass slab.\n"
        f"2. Calculate the critical angle ($\\theta_c$) for the glass-air boundary.\n"
        f"3. If the emergent beam subsequently passes through a slit of width $a = 15\\mu\\text{{m}}$ in air, "
        f"calculate the angular width ($2\\theta_1$) of the central diffraction maximum."
    )
    v_glass = C_LIGHT / n_glass
    v_sci = f"{v_glass / 1e8:.2f}".replace(".", ",") + " \\times 10^8"
    sin_theta1 = (lambda_air_nm * 1e-9) / (15e-6)
    theta1_deg = math.degrees(math.asin(sin_theta1))
    ang_w_deg = round(2 * theta1_deg, 3)

    ans = f"1. v = {v_sci} m/s, lambda = {_fmt_sa(lambda_glass_nm)} nm; 2. theta_c = {_fmt_sa(theta_c)} deg; 3. 2*theta_1 = {_fmt_sa(ang_w_deg)} deg"
    memo = (
        f"1. Speed and wavelength in glass [3]:\n"
        f"   $$v = \\frac{{c}}{{n}} = \\frac{{3{{,}}00 \\times 10^8}}{{{_fmt_sa(n_glass)}}} = {v_sci}\\text{{ m/s}}$$ [A]\n"
        f"   $$\\lambda_{{\\text{{glass}}}} = \\frac{{\\lambda_{{\\text{{air}}}}}}{{n}} = \\frac{{{lambda_air_nm}}}{{{_fmt_sa(n_glass)}}} = {_fmt_sa(lambda_glass_nm)}\\text{{ nm}}$$ [A]\n"
        f"2. Critical angle [2]:\n"
        f"   $$\\sin \\theta_c = \\frac{{1}}{{n}} = \\frac{{1}}{{{_fmt_sa(n_glass)}}} = {sin_c:.4f} \\implies \\theta_c = {_fmt_sa(theta_c)}^\\circ$$ [A]\n"
        f"3. Central diffraction angular width [3]:\n"
        f"   $$\\sin \\theta_1 = \\frac{{\\lambda}}{{a}} = \\frac{{{lambda_air_nm} \\times 10^{{-9}}}}{{15 \\times 10^{{-6}}}} = {sin_theta1:.5f} \\implies \\theta_1 = {theta1_deg:.3f}^\\circ$$\n"
        f"   $$\\text{{Angular Width}} = 2\\theta_1 = 2({theta1_deg:.3f}^\\circ) = {_fmt_sa(ang_w_deg)}^\\circ$$ [A]"
    )
    return {
        "id": _make_id("optics_49", seed, 49),
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 8,
        "hints": {
            "tier_1": "Break down: 1. $v = c/n$ and $\\lambda = \\lambda_0 / n$. 2. $\\sin \\theta_c = 1/n$. 3. $\\sin \\theta_1 = \\lambda / a$.",
            "tier_2": "Remember that in air, use the wavelength in air (not in glass) for the diffraction calculation.",
            "tier_3": f"v = {v_sci} m/s, $\\lambda = {_fmt_sa(lambda_glass_nm)}\\text{{ nm}}$, $\\theta_c = {_fmt_sa(theta_c)}^\\circ$, width = {_fmt_sa(ang_w_deg)}^\\circ$.",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["capstone_optical_synthesis_error", "wavelength_medium_context_confused"],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp1", "desc": "Speed and wavelength in glass", "marks": 3, "editable": True},
                {"id": "mp2", "desc": "Critical angle calculated", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Diffraction central width calculated", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# SUBSKILL 50: Wavefronts diffraction diagnostic misconception autopsy part2
# ==============================================================================
def builder_50_wavefronts_diffraction_diagnostic_misconception_autopsy_part2(rng: random.Random, seed: Optional[int] = None) -> Dict[str, Any]:
    svg = f"""<svg viewBox="0 0 500 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="240" fill="#f8fafc"/>
  <!-- Seed: {seed} -->
  <rect x="50" y="30" width="400" height="180" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
  <text x="70" y="60" font-size="13" fill="#991b1b" font-weight="bold" font-family="sans-serif">Diagnostic Autopsy: Wavefronts &amp; Diffraction</text>
  <text x="70" y="100" font-size="11" fill="#7f1d1d" font-family="sans-serif">Claim 1: "Light diffracts more through wide slits."</text>
  <text x="70" y="130" font-size="11" fill="#7f1d1d" font-family="sans-serif">Claim 2: "Blue light spreads wider than red light."</text>
  <text x="70" y="160" font-size="11" fill="#7f1d1d" font-family="sans-serif">Claim 3: "Wavefronts are parallel to wave rays."</text>
</svg>"""

    prompt = (
        "In a physics diagnostic test, three learners made the following assertions regarding wave optics:\n\n"
        "• **Learner A**: \"To make a laser diffraction pattern spread out wider across the room, we should make the slit aperture wider so more light can bend.\"\n"
        "• **Learner B**: \"Blue light diffracts more than red light because blue light has higher energy and higher frequency.\"\n"
        "• **Learner C**: \"A wavefront always travels parallel to the ray pointing in the direction of wave propagation.\"\n\n"
        "Provide the rigorous scientific correction and justification to refute each learner's misconception."
    )
    ans = "1. Refute A: Diffraction width is inversely proportional to slit width (theta ~ lambda/a); narrower slits produce broader spreading; 2. Refute B: Diffraction depends on wavelength, not frequency; red has longer wavelength and spreads more; 3. Refute C: Wavefronts are PERPENDICULAR (at 90 degrees) to rays, not parallel."
    memo = (
        "Diagnostic Misconception Autopsy [3]:\n"
        "1. **Refutation of Learner A [1]**: Diffraction spreading is **inversely proportional** to aperture size ($\\sin \\theta_1 = \\frac{\\lambda}{a}$). "
        "A narrower slit produces greater spreading; a wider slit approaches rectilinear geometric propagation with minimal spreading [A].\n"
        "2. **Refutation of Learner B [1]**: Diffraction extent depends directly on **wavelength** ($\\lambda$), not photon energy or frequency. "
        "Red light has a longer wavelength ($\\sim 700\\text{ nm}$) than blue light ($\\sim 450\\text{ nm}$), so red light bends through larger diffraction angles [A].\n"
        "3. **Refutation of Learner C [1]**: By definition, wave rays point in the direction of energy propagation and are strictly **perpendicular ($90^\\circ$)** "
        "to the wavefronts at every point in an isotropic medium [A]."
    )
    return {
        "id": _make_id("optics_50", seed, 50),
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "question": prompt,
        "correct_answer": ans,
        "worked_solution": memo,
        "marks": 3,
        "hints": {
            "tier_1": "Recall: Width $\\propto \\lambda / a$. Rays are perpendicular to wavefronts.",
            "tier_2": "Narrower slit = wider spread. Red spreads more than blue. Rays at 90 deg to wavefronts.",
            "tier_3": "Correct all 3: A (inversely proportional to a), B (red has longer wavelength), C (rays are perpendicular to wavefronts).",
        },
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "misconception_tags": ["diffraction_aperture_proportionality_misconception", "wavefront_ray_parallel_misconception", "wavelength_diffraction_confusion"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Refutation of Learner A (inverse proportionality to slit width)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Refutation of Learner B (red longer wavelength spreads more)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Refutation of Learner C (rays perpendicular to wavefronts)", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


BUILDERS_26_50 = [
    builder_26_thin_converging_lens_focal_point_and_principal_rays,
    builder_27_thin_diverging_lens_virtual_focus_and_ray_diagram,
    builder_28_lens_equation_converging_real_image,
    builder_29_lens_equation_converging_virtual_image_magnifying_glass,
    builder_30_lens_equation_diverging_virtual_diminished_image,
    builder_31_linear_magnification_and_image_height_calculation,
    builder_32_compound_microscope_or_refracting_telescope_principles,
    builder_33_wavefront_definition_and_ray_perpendicularity,
    builder_34_circular_vs_plane_wavefronts_propagation,
    builder_35_huygens_principle_statement_and_secondary_wavelets,
    builder_36_huygens_construction_proving_law_of_reflection,
    builder_37_huygens_construction_proving_snells_law_of_refraction,
    builder_38_diffraction_definition_and_wave_nature_evidence,
    builder_39_diffraction_qualitative_aperture_size_vs_wavelength_ratio,
    builder_40_single_slit_diffraction_pattern_central_broad_maximum,
    builder_41_single_slit_diffraction_first_minimum_condition_formula,
    builder_42_single_slit_diffraction_angular_width_of_central_maximum,
    builder_43_single_slit_effect_of_decreasing_increasing_slit_width,
    builder_44_single_slit_effect_of_changing_wavelength_red_vs_blue_light,
    builder_45_single_slit_white_light_diffraction_colored_fringes,
    builder_46_single_slit_intensity_distribution_profile_analysis,
    builder_47_diffraction_of_water_waves_in_ripple_tank,
    builder_48_sound_diffraction_around_corners_vs_light_diffraction,
    builder_49_capstone_optics_wavefront_synthesis_multi_tier,
    builder_50_wavefronts_diffraction_diagnostic_misconception_autopsy_part2,
]
