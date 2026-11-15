"""Grade 10 Mathematics — Term 1 — Trigonometry: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr10/Term 1/05. Trigonometry 1.md and 05. Trigonometry 2.md
Focus: Trigonometric equations (basic, coefficients, multiple angles, special angles),
Cartesian plane (CAST rule, r = sqrt(x^2 + y^2), quadrants 1-4, evaluating expressions without calculator),
and 2D practical problems (angles of elevation and depression, ladders, masts, two-triangle setups, diagnostic autopsy).
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _build_cartesian_svg(x: int, y: int, pt_name: str = "P", angle_name: str = "θ") -> str:
    """Build a clean SVG of a point P(x, y) on the Cartesian plane with terminal ray and dropline."""
    # Origin at (200, 150), scale factor 12 px per unit
    ox, oy = 200, 150
    scale = 12
    px = ox + x * scale
    py = oy - y * scale

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="240">
  <defs>
    <marker id="ax-arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748B"/>
    </marker>
  </defs>
  <!-- Axes -->
  <line x1="20" y1="150" x2="380" y2="150" stroke="#64748B" stroke-width="1.8" marker-end="url(#ax-arr)"/>
  <line x1="200" y1="280" x2="200" y2="20" stroke="#64748B" stroke-width="1.8" marker-end="url(#ax-arr)"/>
  <text x="382" y="146" font-size="14" font-weight="bold" fill="#64748B">x</text>
  <text x="206" y="24" font-size="14" font-weight="bold" fill="#64748B">y</text>
  <text x="186" y="168" font-size="13" fill="#64748B">O</text>
  <!-- Dropline to x-axis -->
  <line x1="{px}" y1="{py}" x2="{px}" y2="150" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <!-- Radius vector r -->
  <line x1="200" y1="150" x2="{px}" y2="{py}" stroke="#2563EB" stroke-width="2.5"/>
  <circle cx="{px}" cy="{py}" r="5" fill="#2563EB"/>
  <text x="{px + (8 if x >= 0 else -60)}" y="{py + ( -8 if y >= 0 else 18)}" font-size="14" font-weight="bold" fill="#0F172A">{pt_name}({x}; {y})</text>
  <text x="{(ox + px)/2 + (8 if x >= 0 else -18)}" y="{(oy + py)/2 - 6}" font-size="13" font-weight="bold" fill="#2563EB">r</text>
</svg>'''


def _build_elevation_svg(dist: float, height: float, angle_deg: int, label_h: str = "h", label_d: str = "d") -> str:
    """Build an SVG diagram for angle of elevation scenarios."""
    ax, ay = 60, 220
    bx, by = 360, 220
    cx, cy = 360, 60

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 260" width="100%" height="240">
  <!-- Ground line -->
  <line x1="30" y1="220" x2="410" y2="220" stroke="#64748B" stroke-width="2"/>
  <!-- Triangle -->
  <polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#F1F5F9" stroke="#1E293B" stroke-width="2.5"/>
  <!-- Right angle box at B -->
  <path d="M 344 220 L 344 204 L 360 204" fill="none" stroke="#1E293B" stroke-width="1.8"/>
  <!-- Vertical Tower/Wall -->
  <line x1="360" y1="220" x2="360" y2="60" stroke="#0F172A" stroke-width="4"/>
  <!-- Angle arc at observer -->
  <path d="M 100 220 A 40 40 0 0 0 95 204" fill="none" stroke="#2563EB" stroke-width="2"/>
  <text x="108" y="212" font-size="14" font-weight="bold" fill="#2563EB">{angle_deg}°</text>
  <!-- Labels -->
  <text x="210" y="244" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">{label_d}</text>
  <text x="382" y="145" font-size="14" font-weight="bold" fill="#0F172A">{label_h}</text>
  <text x="45" y="240" font-size="13" fill="#64748B">Observer</text>
  <text x="340" y="46" font-size="13" fill="#64748B">Tower</text>
</svg>'''


# 26. Solve trig equation basic sin acute
def arch_26_solve_trig_equation_basic_sin_acute(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([25, 34, 46, 58, 67, 74])
    k_val = round(math.sin(math.radians(angle)), 4)
    k_str = f"{k_val:.4f}".replace(".", ",")

    prompt = (
        f"Solve for acute angle \\(\\theta\\) (where \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\)):\n"
        f"\\[ \\sin \\theta = {k_str} \\]\n\n"
        f"Round your answer to one decimal place."
    )
    ans = f"{angle:.1f}".replace(".", ",")
    sol = (
        f"**Step 1:** Apply the inverse sine function:\n"
        f"\\[ \\theta = \\sin^{{-1}}({k_str}) \\]\n\n"
        f"**Step 2:** Calculate and round to one decimal place:\n"
        f"\\[ \\theta = {ans}^\\circ \\]"
    )
    return {
        "id": f"g10_trig_26_{rng.randint(100000, 999999)}",
        "subskill": "26_solve_trig_equation_basic_sin_acute",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"θ = {ans}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_26",
        "misconception_tags": ["dividing_by_sin", "rounding_to_one_decimal_place"],
        "marking_schema": [
            {"step": 1, "criterion": "Apply arcsin", "marks": 1},
            {"step": 2, "criterion": "Correct angle in degrees rounded to 1 d.p.", "marks": 1},
        ],
        "hints": {
            "tier_1": f"theta = arcsin({k_str}).",
            "tier_2": "Calculate shift+sin on your calculator.",
            "tier_3": f"{ans}°",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_26_solve_trig_equation_basic_sin_acute",
    }


# 27. Solve trig equation basic cos acute
def arch_27_solve_trig_equation_basic_cos_acute(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([21, 37, 49, 61, 73])
    k_val = round(math.cos(math.radians(angle)), 4)
    k_str = f"{k_val:.4f}".replace(".", ",")

    prompt = (
        f"Solve for acute angle \\(\\theta\\) (where \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\)):\n"
        f"\\[ \\cos \\theta = {k_str} \\]\n\n"
        f"Round your answer to one decimal place."
    )
    ans = f"{angle:.1f}".replace(".", ",")
    sol = (
        f"**Step 1:** Apply inverse cosine:\n"
        f"\\[ \\theta = \\cos^{{-1}}({k_str}) \\]\n\n"
        f"**Step 2:** Calculate and round to one decimal place:\n"
        f"\\[ \\theta = {ans}^\\circ \\]"
    )
    return {
        "id": f"g10_trig_27_{rng.randint(100000, 999999)}",
        "subskill": "27_solve_trig_equation_basic_cos_acute",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"θ = {ans}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_27",
        "misconception_tags": ["dividing_by_cos", "rounding_to_one_decimal_place"],
        "marking_schema": [
            {"step": 1, "criterion": "Apply arccos", "marks": 1},
            {"step": 2, "criterion": "Correct angle rounded to 1 d.p.", "marks": 1},
        ],
        "hints": {
            "tier_1": f"theta = arccos({k_str}).",
            "tier_2": "Calculate shift+cos on your calculator.",
            "tier_3": f"{ans}°",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_27_solve_trig_equation_basic_cos_acute",
    }


# 28. Solve trig equation basic tan acute
def arch_28_solve_trig_equation_basic_tan_acute(rng: random.Random) -> Dict[str, Any]:
    angle = rng.choice([19, 32, 47, 53, 64])
    k_val = round(math.tan(math.radians(angle)), 4)
    k_str = f"{k_val:.4f}".replace(".", ",")

    prompt = (
        f"Solve for acute angle \\(\\theta\\) (where \\(0^\\circ \\leq \\theta < 90^\\circ\\)):\n"
        f"\\[ \\tan \\theta = {k_str} \\]\n\n"
        f"Round your answer to one decimal place."
    )
    ans = f"{angle:.1f}".replace(".", ",")
    sol = (
        f"**Step 1:** Apply inverse tangent:\n"
        f"\\[ \\theta = \\tan^{{-1}}({k_str}) \\]\n\n"
        f"**Step 2:** Calculate and round to one decimal place:\n"
        f"\\[ \\theta = {ans}^\\circ \\]"
    )
    return {
        "id": f"g10_trig_28_{rng.randint(100000, 999999)}",
        "subskill": "28_solve_trig_equation_basic_tan_acute",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"θ = {ans}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_28",
        "misconception_tags": ["dividing_by_tan", "rounding_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Apply arctan", "marks": 1},
            {"step": 2, "criterion": "Correct angle rounded to 1 d.p.", "marks": 1},
        ],
        "hints": {
            "tier_1": f"theta = arctan({k_str}).",
            "tier_2": "Calculate shift+tan on your calculator.",
            "tier_3": f"{ans}°",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_28_solve_trig_equation_basic_tan_acute",
    }


# 29. Solve trig equation with coefficient: a * sin θ = b
def arch_29_solve_trig_equation_with_coefficient(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    angle = rng.choice([23, 31, 42, 54, 65])
    rad = math.radians(angle)
    b_val = round(a * math.sin(rad), 2)
    b_str = f"{b_val:.2f}".replace(".", ",")

    prompt = (
        f"Solve for acute angle \\(\\theta\\) (where \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\)):\n"
        f"\\[ {a}\\sin \\theta = {b_str} \\]\n\n"
        f"Round your answer to one decimal place."
    )
    ans = f"{angle:.1f}".replace(".", ",")
    sol = (
        f"**Step 1:** Divide both sides by {a} to isolate \\(\\sin \\theta\\):\n"
        f"\\[ \\sin \\theta = \\frac{{{b_str}}}{{{a}}} \\approx {b_val / a:.4f} \\]\n\n"
        f"**Step 2:** Apply inverse sine:\n"
        f"\\[ \\theta = \\sin^{{-1}}\\left(\\frac{{{b_str}}}{{{a}}}\\right) = {ans}^\\circ \\]"
    )
    return {
        "id": f"g10_trig_29_{rng.randint(100000, 999999)}",
        "subskill": "29_solve_trig_equation_with_coefficient",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"θ = {ans}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_29",
        "misconception_tags": ["dividing_angle_by_coefficient", "failure_to_isolate_trig_ratio"],
        "marking_schema": [
            {"step": 1, "criterion": "Divide both sides by coefficient a", "marks": 1},
            {"step": 2, "criterion": "Apply arcsin to ratio", "marks": 1},
            {"step": 3, "criterion": "State angle rounded to 1 d.p.", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Divide both sides by {a} first: sin θ = {b_str}/{a}.",
            "tier_2": f"Now take arcsin({b_val / a:.4f}).",
            "tier_3": f"{ans}°",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_29_solve_trig_equation_with_coefficient",
    }


# 30. Solve trig equation transpose constant first: a cos θ + b = c
def arch_30_solve_trig_equation_transpose_constant_first(rng: random.Random) -> Dict[str, Any]:
    a = 2
    angle = rng.choice([30, 45, 60])
    b = rng.randint(1, 4)
    # 2*cos(angle) + b = c
    if angle == 30:
        # 2*(sqrt(3)/2) + b = sqrt(3) + b
        pass
    # Let's use clean numbers for angle = 60 (cos 60 = 0.5):
    angle = 60
    # 2*(0.5) + b = 1 + b
    c = 1 + b
    prompt = (
        f"Solve for acute angle \\(\\theta\\) (where \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\)):\n"
        f"\\[ 2\\cos \\theta + {b} = {c} \\]"
    )
    ans = "60°"
    sol = (
        f"**Step 1:** Subtract {b} from both sides:\n"
        f"\\[ 2\\cos \\theta = {c} - {b} = 1 \\]\n\n"
        f"**Step 2:** Divide both sides by 2:\n"
        f"\\[ \\cos \\theta = \\frac{{1}}{{2}} \\]\n\n"
        f"**Step 3:** Solve for \\(\\theta\\) using special angles:\n"
        f"\\[ \\theta = 60^\\circ \\]"
    )
    return {
        "id": f"g10_trig_30_{rng.randint(100000, 999999)}",
        "subskill": "30_solve_trig_equation_transpose_constant_first",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": "60°",
        "sample_answer": "θ = 60°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_30",
        "misconception_tags": ["order_of_operations_reversal", "sign_error_transposition"],
        "marking_schema": [
            {"step": 1, "criterion": "Subtract constant b from RHS", "marks": 1},
            {"step": 2, "criterion": "Divide by coefficient 2 to get cos theta = 1/2", "marks": 1},
            {"step": 3, "criterion": "State theta = 60°", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Subtract {b} from both sides to get 2 cos θ = 1.",
            "tier_2": "cos θ = 1/2. What special angle has a cosine of 1/2?",
            "tier_3": "60°",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_30_solve_trig_equation_transpose_constant_first",
    }


# 31. Solve trig equation multiple angle 2theta: sin(2theta) = k
def arch_31_solve_trig_equation_multiple_angle_2theta(rng: random.Random) -> Dict[str, Any]:
    two_theta = rng.choice([40, 50, 60, 70, 80])
    theta = two_theta / 2
    k_val = round(math.sin(math.radians(two_theta)), 4)
    k_str = f"{k_val:.4f}".replace(".", ",")

    prompt = (
        f"Solve for \\(\\theta\\) (where \\(0^\\circ \\leq \\theta \\leq 45^\\circ\\)):\n"
        f"\\[ \\sin(2\\theta) = {k_str} \\]\n\n"
        f"Round your answer to one decimal place."
    )
    ans = f"{theta:.1f}".replace(".", ",")
    sol = (
        f"**Step 1:** Solve for the entire angle \\(2\\theta\\) first using inverse sine:\n"
        f"\\[ 2\\theta = \\sin^{{-1}}({k_str}) \\approx {two_theta}^\\circ \\]\n\n"
        f"**Step 2:** Divide by 2 to isolate \\(\\theta\\):\n"
        f"\\[ \\theta = \\frac{{{two_theta}^\\circ}}{{2}} = {ans}^\\circ \\]"
    )
    return {
        "id": f"g10_trig_31_{rng.randint(100000, 999999)}",
        "subskill": "31_solve_trig_equation_multiple_angle_2theta",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"θ = {ans}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_31",
        "misconception_tags": ["dividing_by_2_before_inverse_sin_fallacy", "multiple_angle_isolation_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Apply arcsin to find 2*theta", "marks": 1},
            {"step": 2, "criterion": "Divide angle by 2", "marks": 1},
            {"step": 3, "criterion": "State final angle", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Do not divide by 2 first! Solve for (2θ) first: 2θ = arcsin({k_str}).",
            "tier_2": f"2θ = {two_theta}°, so θ = {two_theta} / 2.",
            "tier_3": f"{ans}°",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_31_solve_trig_equation_multiple_angle_2theta",
    }


# 32. Solve trig equation angle plus constant: cos(theta + alpha) = k
def arch_32_solve_trig_equation_angle_plus_constant(rng: random.Random) -> Dict[str, Any]:
    alpha = rng.choice([10, 15, 20])
    combined_angle = rng.choice([45, 60, 75])
    theta = combined_angle - alpha
    k_val = round(math.cos(math.radians(combined_angle)), 4)
    k_str = f"{k_val:.4f}".replace(".", ",")

    prompt = (
        f"Solve for acute angle \\(\\theta\\):\n"
        f"\\[ \\cos(\\theta + {alpha}^\\circ) = {k_str} \\]"
    )
    ans = f"{theta:.1f}".replace(".", ",")
    sol = (
        f"**Step 1:** Solve for the bracketed angle \\((\\theta + {alpha}^\\circ)\\):\n"
        f"\\[ \\theta + {alpha}^\\circ = \\cos^{{-1}}({k_str}) \\approx {combined_angle}^\\circ \\]\n\n"
        f"**Step 2:** Subtract {alpha}° to find \\(\\theta\\):\n"
        f"\\[ \\theta = {combined_angle}^\\circ - {alpha}^\\circ = {ans}^\\circ \\]"
    )
    return {
        "id": f"g10_trig_32_{rng.randint(100000, 999999)}",
        "subskill": "32_solve_trig_equation_angle_plus_constant",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"θ = {ans}°",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_32",
        "misconception_tags": ["subtracting_constant_before_inverse_trig", "compound_angle_misconception"],
        "marking_schema": [
            {"step": 1, "criterion": "Apply arccos to isolate theta + alpha", "marks": 1},
            {"step": 2, "criterion": "Subtract alpha to isolate theta", "marks": 1},
            {"step": 3, "criterion": "Correct final angle", "marks": 1},
        ],
        "hints": {
            "tier_1": f"First take arccos({k_str}) to find (θ + {alpha}°).",
            "tier_2": f"θ + {alpha}° = {combined_angle}°, then subtract {alpha}°.",
            "tier_3": f"{ans}°",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_32_solve_trig_equation_angle_plus_constant",
    }


# 33. Solve trig equation special angle without calculator: 2 sin θ - 1 = 0
def arch_33_solve_trig_equation_special_angle_without_calculator(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice(["sin30", "cos60", "tan45"])
    if case == "sin30":
        prompt = (
            "Without using a calculator, solve for \\(\\theta\\) (where \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\)):\n"
            "\\[ 2\\sin \\theta - 1 = 0 \\]"
        )
        ans = "30°"
        sol = (
            "**Step 1:** Transpose 1 and divide by 2:\n"
            "\\[ 2\\sin \\theta = 1 \\implies \\sin \\theta = \\frac{1}{2} \\]\n\n"
            "**Step 2:** From special angles, recall that \\(\\sin 30^\\circ = \\frac{1}{2}\\).\n"
            "Therefore, \\(\\theta = 30^\\circ\\)."
        )
    elif case == "cos60":
        prompt = (
            "Without using a calculator, solve for \\(\\theta\\) (where \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\)):\n"
            "\\[ 2\\cos \\theta - 1 = 0 \\]"
        )
        ans = "60°"
        sol = (
            "**Step 1:** Transpose 1 and divide by 2:\n"
            "\\[ 2\\cos \\theta = 1 \\implies \\cos \\theta = \\frac{1}{2} \\]\n\n"
            "**Step 2:** From special angles, \\(\\cos 60^\\circ = \\frac{1}{2}\\).\n"
            "Therefore, \\(\\theta = 60^\\circ\\)."
        )
    else:  # tan45
        prompt = (
            "Without using a calculator, solve for \\(\\theta\\) (where \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\)):\n"
            "\\[ \\tan \\theta - 1 = 0 \\]"
        )
        ans = "45°"
        sol = (
            "**Step 1:** Isolate \\(\\tan \\theta\\):\n"
            "\\[ \\tan \\theta = 1 \\]\n\n"
            "**Step 2:** From special angles, \\(\\tan 45^\\circ = 1\\).\n"
            "Therefore, \\(\\theta = 45^\\circ\\)."
        )

    return {
        "id": f"g10_trig_33_{rng.randint(100000, 999999)}",
        "subskill": "33_solve_trig_equation_special_angle_without_calculator",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_33",
        "misconception_tags": ["special_angle_recognition_failure", "transposition_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Isolate trig ratio to standard special fraction", "marks": 1},
            {"step": 2, "criterion": "State correct special angle", "marks": 1},
        ],
        "hints": {
            "tier_1": "Isolate the trig ratio first.",
            "tier_2": "Recall your special angles: 30°, 45°, 60°.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_33_solve_trig_equation_special_angle_without_calculator",
    }


# 34. Cartesian definition radius r from coordinates
def arch_34_cartesian_definition_radius_r_from_coordinates(rng: random.Random) -> Dict[str, Any]:
    x, y, r = rng.choice([
        (3, 4, 5), (-4, 3, 5), (-3, -4, 5), (4, -3, 5),
        (5, 12, 13), (-12, 5, 13), (-5, -12, 13), (12, -5, 13),
        (8, 15, 17), (-8, 15, 17),
    ])
    svg_str = _build_cartesian_svg(x, y, pt_name="P", angle_name="θ")
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Point P({x}; {y}) plotted on Cartesian axes with radius vector r",
    }

    prompt = (
        f"A point \\(P({x};\\, {y})\\) lies on the terminal ray of angle \\(\\theta\\) in standard position.\n\n"
        f"Calculate the length of the radius vector \\(r = OP\\)."
    )
    ans = str(r)
    sol = (
        f"**Step 1:** Recall the formula for the radius vector in the Cartesian plane:\n"
        f"\\[ r^2 = x^2 + y^2 \\]\n\n"
        f"**Step 2:** Substitute the coordinates \\(x = {x}\\) and \\(y = {y}\\):\n"
        f"\\[ r^2 = ({x})^2 + ({y})^2 = {x**2} + {y**2} = {r**2} \\]\n\n"
        f"**Step 3:** Take the positive square root (since radius \\(r > 0\\) always):\n"
        f"\\[ r = \\sqrt{{{r**2}}} = {r} \\]"
    )
    return {
        "id": f"g10_trig_34_{rng.randint(100000, 999999)}",
        "subskill": "34_cartesian_definition_radius_r_from_coordinates",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"r = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_34",
        "misconception_tags": ["negative_squaring_sign_error", "radius_must_be_positive"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Apply formula r^2 = x^2 + y^2", "marks": 1},
            {"step": 2, "criterion": "Calculate r accurately (positive value)", "marks": 1},
        ],
        "hints": {
            "tier_1": "r = sqrt(x^2 + y^2). Note that (-x)^2 is positive!",
            "tier_2": f"r^2 = ({x})^2 + ({y})^2 = {r**2}.",
            "tier_3": f"r = {ans}",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_34_cartesian_definition_radius_r_from_coordinates",
    }


# 35. Cartesian ratio sin cos tan from point Quadrant 1
def arch_35_cartesian_ratio_sin_cos_tan_from_point_quadrant1(rng: random.Random) -> Dict[str, Any]:
    x, y, r = rng.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17)])
    svg_str = _build_cartesian_svg(x, y, pt_name="P", angle_name="θ")
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Point P({x}; {y}) in Quadrant 1",
    }

    prompt = (
        f"The point \\(P({x};\\, {y})\\) lies in Quadrant 1 on the terminal arm of angle \\(\\theta\\).\n\n"
        f"Determine the exact value of \\(\\sin \\theta\\)."
    )
    ans = f"{y}/{r}"
    sol = (
        f"**Step 1:** Calculate \\(r\\):\n"
        f"\\[ r = \\sqrt{{{x}^2 + {y}^2}} = \\sqrt{{{x**2 + y**2}}} = {r} \\]\n\n"
        f"**Step 2:** Apply Cartesian definition \\(\\sin \\theta = \\frac{{y}}{{r}}\\):\n"
        f"\\[ \\sin \\theta = \\frac{{{y}}}{{{r}}} \\]"
    )
    return {
        "id": f"g10_trig_35_{rng.randint(100000, 999999)}",
        "subskill": "35_cartesian_ratio_sin_cos_tan_from_point_quadrant1",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"sin θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_35",
        "misconception_tags": ["confusing_x_and_y_in_cartesian_ratios", "cartesian_ratio_inversion"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Find radius r = hypotenuse", "marks": 1},
            {"step": 2, "criterion": "State sin theta = y/r", "marks": 1},
        ],
        "hints": {
            "tier_1": "sin θ = y / r. Calculate r = sqrt(x^2 + y^2).",
            "tier_2": f"x = {x}, y = {y}, r = {r}.",
            "tier_3": f"sin θ = {ans}",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_35_cartesian_ratio_sin_cos_tan_from_point_quadrant1",
    }


# 36. Cartesian ratio point Quadrant 2 (negative x, positive y)
def arch_36_cartesian_ratio_point_quadrant2_negative_x(rng: random.Random) -> Dict[str, Any]:
    pos_x, y, r = rng.choice([(4, 3, 5), (12, 5, 13), (15, 8, 17)])
    x = -pos_x
    svg_str = _build_cartesian_svg(x, y, pt_name="P", angle_name="θ")
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Point P({x}; {y}) in Quadrant 2",
    }

    prompt = (
        f"The point \\(P({x};\\, {y})\\) lies in Quadrant 2 on the terminal arm of angle \\(\\theta\\).\n\n"
        f"Determine the exact value of \\(\\cos \\theta\\)."
    )
    ans = f"{x}/{r}"
    sol = (
        f"**Step 1:** Calculate \\(r\\):\n"
        f"\\[ r = \\sqrt{{({x})^2 + {y}^2}} = \\sqrt{{{x**2 + y**2}}} = {r} \\]\n\n"
        f"**Step 2:** In Quadrant 2, cosine is negative because \\(x < 0\\):\n"
        f"\\[ \\cos \\theta = \\frac{{x}}{{r}} = \\frac{{{x}}}{{{r}}} \\]"
    )
    return {
        "id": f"g10_trig_36_{rng.randint(100000, 999999)}",
        "subskill": "36_cartesian_ratio_point_quadrant2_negative_x",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"cos θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_36",
        "misconception_tags": ["quadrant_2_cosine_sign_error", "omitting_negative_sign"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Compute radius r", "marks": 1},
            {"step": 2, "criterion": "State cos theta = x/r with negative sign", "marks": 1},
        ],
        "hints": {
            "tier_1": "cos θ = x / r. Since x is negative in Quadrant 2, cos θ is negative.",
            "tier_2": f"x = {x}, r = {r}.",
            "tier_3": f"cos θ = {ans}",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_36_cartesian_ratio_point_quadrant2_negative_x",
    }


# 37. Cartesian ratio point Quadrant 3 (negative x, negative y)
def arch_37_cartesian_ratio_point_quadrant3_both_negative(rng: random.Random) -> Dict[str, Any]:
    pos_x, pos_y, r = rng.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17)])
    x = -pos_x
    y = -pos_y
    svg_str = _build_cartesian_svg(x, y, pt_name="P", angle_name="θ")
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Point P({x}; {y}) in Quadrant 3",
    }

    prompt = (
        f"The point \\(P({x};\\, {y})\\) lies in Quadrant 3.\n\n"
        f"Determine the exact value of \\(\\tan \\theta\\)."
    )
    ans = f"{pos_y}/{pos_x}"
    sol = (
        f"**Step 1:** In Quadrant 3, both \\(x\\) and \\(y\\) are negative:\n"
        f"\\[ x = {x}, \\quad y = {y} \\]\n\n"
        f"**Step 2:** Apply \\(\\tan \\theta = \\frac{{y}}{{x}}\\):\n"
        f"\\[ \\tan \\theta = \\frac{{{y}}}{{{x}}} = \\frac{{{pos_y}}}{{{pos_x}}} \\]\n"
        f"*(Notice that dividing two negative numbers gives a positive result, in agreement with the CAST rule in Quadrant 3)*"
    )
    return {
        "id": f"g10_trig_37_{rng.randint(100000, 999999)}",
        "subskill": "37_cartesian_ratio_point_quadrant3_both_negative",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"tan θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_37",
        "misconception_tags": ["quadrant_3_tan_sign_confusion", "negative_division_sign_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Apply tan theta = y/x", "marks": 1},
            {"step": 2, "criterion": "Simplify negative divided by negative to positive", "marks": 1},
        ],
        "hints": {
            "tier_1": "tan θ = y / x. In Quadrant 3, negative / negative = positive.",
            "tier_2": f"tan θ = ({y}) / ({x}) = {pos_y}/{pos_x}.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_37_cartesian_ratio_point_quadrant3_both_negative",
    }


# 38. Cartesian ratio point Quadrant 4 (positive x, negative y)
def arch_38_cartesian_ratio_point_quadrant4_negative_y(rng: random.Random) -> Dict[str, Any]:
    x, pos_y, r = rng.choice([(4, 3, 5), (12, 5, 13), (15, 8, 17)])
    y = -pos_y
    svg_str = _build_cartesian_svg(x, y, pt_name="P", angle_name="θ")
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Point P({x}; {y}) in Quadrant 4",
    }

    prompt = (
        f"The point \\(P({x};\\, {y})\\) lies on the terminal arm of angle \\(\\theta\\) in Quadrant 4.\n\n"
        f"Determine the exact value of \\(\\sin \\theta\\)."
    )
    ans = f"{y}/{r}"
    sol = (
        f"**Step 1:** Calculate \\(r\\):\n"
        f"\\[ r = \\sqrt{{{x}^2 + ({y})^2}} = \\sqrt{{{x**2 + y**2}}} = {r} \\]\n\n"
        f"**Step 2:** In Quadrant 4, \\(y\\) is negative, so \\(\\sin \\theta\\) is negative:\n"
        f"\\[ \\sin \\theta = \\frac{{y}}{{r}} = \\frac{{{y}}}{{{r}}} \\]"
    )
    return {
        "id": f"g10_trig_38_{rng.randint(100000, 999999)}",
        "subskill": "38_cartesian_ratio_point_quadrant4_negative_y",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"sin θ = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_38",
        "misconception_tags": ["quadrant_4_sine_sign_error", "sin_cos_inversion"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Compute radius r", "marks": 1},
            {"step": 2, "criterion": "State sin theta = y/r with negative sign", "marks": 1},
        ],
        "hints": {
            "tier_1": "sin θ = y / r. In Quadrant 4, y is negative.",
            "tier_2": f"y = {y}, r = {r}.",
            "tier_3": f"sin θ = {ans}",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_38_cartesian_ratio_point_quadrant4_negative_y",
    }


# 39. CAST rule determine sign of ratios in quadrants
def arch_39_cast_rule_determine_sign_of_ratios_in_quadrants(rng: random.Random) -> Dict[str, Any]:
    quad = rng.choice([1, 2, 3, 4])
    fn = rng.choice(["sin", "cos", "tan"])
    ax = rng.randint(3, 8)
    ay = rng.randint(3, 8)
    # CAST rule:
    # Q1: all positive
    # Q2: sin positive, cos/tan negative
    # Q3: tan positive, sin/cos negative
    # Q4: cos positive, sin/tan negative
    is_pos = False
    if quad == 1:
        is_pos = True
        qx, qy = ax, ay
    elif quad == 2:
        is_pos = (fn == "sin")
        qx, qy = -ax, ay
    elif quad == 3:
        is_pos = (fn == "tan")
        qx, qy = -ax, -ay
    else:  # quad 4
        is_pos = (fn == "cos")
        qx, qy = ax, -ay

    ans = "Positive" if is_pos else "Negative"
    svg_str = _build_cartesian_svg(qx, qy, pt_name="P", angle_name="θ")
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Terminal ray of angle θ passing through P({qx}; {qy}) in Quadrant {quad}",
    }

    prompt = (
        f"Using the CAST rule and the terminal ray in **Quadrant {quad}** passing through \\(P({qx}; {qy})\\), "
        f"state whether \\(\\{fn} \\theta\\) is **Positive** or **Negative**."
    )
    sol = (
        f"**CAST Rule Analysis for Quadrant {quad}:**\n"
        f"- Quadrant 1 (0° to 90°): **A**ll ratios are positive.\n"
        f"- Quadrant 2 (90° to 180°): **S**in is positive (cos and tan are negative).\n"
        f"- Quadrant 3 (180° to 270°): **T**an is positive (sin and cos are negative).\n"
        f"- Quadrant 4 (270° to 360°): **C**os is positive (sin and tan are negative).\n\n"
        f"Therefore, in Quadrant {quad}, \\(\\{fn} \\theta\\) is **{ans}**."
    )
    return {
        "id": f"g10_trig_39_{rng.randint(100000, 999999)}",
        "subskill": "39_cast_rule_determine_sign_of_ratios_in_quadrants",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["Positive", "Negative"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g10_trig_39",
        "misconception_tags": ["cast_diagram_quadrant_misalignment", "trig_signs_confusion"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Correctly determine sign using CAST rule", "marks": 1},
        ],
        "hints": {
            "tier_1": "Recall CAST: C (Q4), A (Q1), S (Q2), T (Q3).",
            "tier_2": f"In Quadrant {quad}, which ratios are positive?",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 1,
        "mode": "elementary_39_cast_rule_determine_sign_of_ratios_in_quadrants",
    }


# 40. Cartesian given ratio and condition find other ratios
def arch_40_cartesian_given_ratio_and_condition_find_other_ratios(rng: random.Random) -> Dict[str, Any]:
    # e.g. sin θ = -3/5 and cos θ > 0 => Quadrant 4
    # or sin θ = 5/13 and cos θ < 0 => Quadrant 2
    # or tan θ = 4/3 and sin θ < 0 => Quadrant 3
    case = rng.choice(["sin_pos_cos_neg", "sin_neg_cos_pos", "tan_pos_sin_neg"])
    if case == "sin_pos_cos_neg":
        # Q2
        y, r = 5, 13
        x = -12
        prompt = (
            f"Given that \\(\\sin \\theta = \\frac{{5}}{{13}}\\) and \\(\\cos \\theta < 0\\):\n\n"
            f"1. Identify the quadrant in which \\(\\theta\\) lies.\n"
            f"2. Determine the exact value of \\(\\tan \\theta\\) without using a calculator."
        )
        ans = "Quadrant 2, tan θ = -5/12"
        sol = (
            f"**Step 1:** Determine the quadrant:\n"
            f"- \\(\\sin \\theta > 0\\) in Quadrants 1 and 2.\n"
            f"- \\(\\cos \\theta < 0\\) in Quadrants 2 and 3.\n"
            f"The overlap is **Quadrant 2**.\n\n"
            f"**Step 2:** Determine coordinates \\(x, y, r\\):\n"
            f"Since \\(\\sin \\theta = y/r = 5/13\\), let \\(y = 5\\) and \\(r = 13\\).\n"
            f"\\[ x^2 = r^2 - y^2 = 13^2 - 5^2 = 169 - 25 = 144 \\implies x = -12 \\quad (x < 0 \\text{{ in Q2}}) \\]\n\n"
            f"**Step 3:** Calculate \\(\\tan \\theta\\):\n"
            f"\\[ \\tan \\theta = \\frac{{y}}{{x}} = \\frac{{5}}{{-12}} = -\\frac{{5}}{{12}} \\]"
        )
    elif case == "sin_neg_cos_pos":
        # Q4
        y, r = -3, 5
        x = 4
        prompt = (
            f"Given that \\(\\sin \\theta = -\\frac{{3}}{{5}}\\) and \\(\\cos \\theta > 0\\):\n\n"
            f"1. Identify the quadrant in which \\(\\theta\\) lies.\n"
            f"2. Determine the exact value of \\(\\cos \\theta\\) without using a calculator."
        )
        ans = "Quadrant 4, cos θ = 4/5"
        sol = (
            f"**Step 1:** Determine the quadrant:\n"
            f"- \\(\\sin \\theta < 0\\) in Quadrants 3 and 4.\n"
            f"- \\(\\cos \\theta > 0\\) in Quadrants 1 and 4.\n"
            f"The overlap is **Quadrant 4**.\n\n"
            f"**Step 2:** Find \\(x\\):\n"
            f"\\[ x^2 = 5^2 - (-3)^2 = 25 - 9 = 16 \\implies x = +4 \\quad (x > 0 \\text{{ in Q4}}) \\]\n\n"
            f"**Step 3:** Calculate \\(\\cos \\theta\\):\n"
            f"\\[ \\cos \\theta = \\frac{{x}}{{r}} = \\frac{{4}}{{5}} \\]"
        )
    else:  # tan_pos_sin_neg => Q3
        x, y, r = -3, -4, 5
        prompt = (
            f"Given that \\(\\tan \\theta = \\frac{{4}}{{3}}\\) and \\(\\sin \\theta < 0\\):\n\n"
            f"1. Identify the quadrant in which \\(\\theta\\) lies.\n"
            f"2. Determine the exact value of \\(\\cos \\theta\\) without using a calculator."
        )
        ans = "Quadrant 3, cos θ = -3/5"
        sol = (
            f"**Step 1:** Determine the quadrant:\n"
            f"- \\(\\tan \\theta > 0\\) in Quadrants 1 and 3.\n"
            f"- \\(\\sin \\theta < 0\\) in Quadrants 3 and 4.\n"
            f"The overlap is **Quadrant 3**.\n\n"
            f"**Step 2:** In Quadrant 3, \\(x\\) and \\(y\\) are both negative:\n"
            f"Let \\(y = -4\\) and \\(x = -3\\).\n"
            f"\\[ r = \\sqrt{{(-3)^2 + (-4)^2}} = 5 \\]\n\n"
            f"**Step 3:** Calculate \\(\\cos \\theta\\):\n"
            f"\\[ \\cos \\theta = \\frac{{x}}{{r}} = -\\frac{{3}}{{5}} \\]"
        )

    return {
        "id": f"g10_trig_40_{rng.randint(100000, 999999)}",
        "subskill": "40_cartesian_given_ratio_and_condition_find_other_ratios",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_trig_40",
        "misconception_tags": ["quadrant_selection_error", "sign_of_x_or_y_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Identify correct quadrant", "marks": 1},
            {"step": 2, "criterion": "Calculate missing coordinate with proper sign", "marks": 2},
            {"step": 3, "criterion": "Calculate requested trig ratio", "marks": 1},
        ],
        "hints": {
            "tier_1": "Use the two given conditions to locate the single quadrant where both are satisfied.",
            "tier_2": "Use Pythagoras x^2 + y^2 = r^2 to find the missing coordinate.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_40_cartesian_given_ratio_and_condition_find_other_ratios",
    }


# 41. Cartesian evaluate expression without calculator
def arch_41_cartesian_evaluate_expression_without_calculator(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice(["cos_4_5", "sin_5_13", "sin_3_5"])
    if case == "cos_4_5":
        prompt = (
            "If \\(5\\cos \\theta - 4 = 0\\) and \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\), "
            "evaluate the expression without using a calculator:\n"
            "\\[ 10\\sin \\theta + 8\\tan \\theta \\]"
        )
        ans = "12"
        sol = (
            "**Step 1:** Isolate \\(\\cos \\theta\\):\n"
            "\\[ 5\\cos \\theta = 4 \\implies \\cos \\theta = \\frac{4}{5} \\]\n\n"
            "**Step 2:** Find \\(y\\) using Pythagoras (Quadrant 1, so \\(y > 0\\)):\n"
            "\\[ y = \\sqrt{5^2 - 4^2} = \\sqrt{25 - 16} = 3 \\]\n\n"
            "**Step 3:** State ratios:\n"
            "\\[ \\sin \\theta = \\frac{3}{5}, \\quad \\tan \\theta = \\frac{3}{4} \\]\n\n"
            "**Step 4:** Evaluate:\n"
            "\\[ 10\\left(\\frac{3}{5}\\right) + 8\\left(\\frac{3}{4}\\right) = 6 + 6 = 12 \\]"
        )
    elif case == "sin_5_13":
        prompt = (
            "If \\(13\\sin \\theta - 5 = 0\\) and \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\), "
            "evaluate the expression without using a calculator:\n"
            "\\[ 26\\cos \\theta + 24\\tan \\theta \\]"
        )
        ans = "34"
        sol = (
            "**Step 1:** Isolate \\(\\sin \\theta\\):\n"
            "\\[ 13\\sin \\theta = 5 \\implies \\sin \\theta = \\frac{5}{13} \\]\n\n"
            "**Step 2:** Find \\(x\\) using Pythagoras:\n"
            "\\[ x = \\sqrt{13^2 - 5^2} = \\sqrt{169 - 25} = 12 \\]\n\n"
            "**Step 3:** State ratios:\n"
            "\\[ \\cos \\theta = \\frac{12}{13}, \\quad \\tan \\theta = \\frac{5}{12} \\]\n\n"
            "**Step 4:** Evaluate:\n"
            "\\[ 26\\left(\\frac{12}{13}\\right) + 24\\left(\\frac{5}{12}\\right) = 24 + 10 = 34 \\]"
        )
    else:  # sin_3_5
        prompt = (
            "If \\(5\\sin \\theta - 3 = 0\\) and \\(0^\\circ \\leq \\theta \\leq 90^\\circ\\), "
            "evaluate the expression without using a calculator:\n"
            "\\[ 15\\cos \\theta + 12\\tan \\theta \\]"
        )
        ans = "21"
        sol = (
            "**Step 1:** Isolate \\(\\sin \\theta\\):\n"
            "\\[ 5\\sin \\theta = 3 \\implies \\sin \\theta = \\frac{3}{5} \\]\n\n"
            "**Step 2:** Find \\(x\\) using Pythagoras:\n"
            "\\[ x = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = 4 \\]\n\n"
            "**Step 3:** State ratios:\n"
            "\\[ \\cos \\theta = \\frac{4}{5}, \\quad \\tan \\theta = \\frac{3}{4} \\]\n\n"
            "**Step 4:** Evaluate:\n"
            "\\[ 15\\left(\\frac{4}{5}\\right) + 12\\left(\\frac{3}{4}\\right) = 12 + 9 = 21 \\]"
        )

    return {
        "id": f"g10_trig_41_{rng.randint(100000, 999999)}",
        "subskill": "41_cartesian_evaluate_expression_without_calculator",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_trig_41",
        "misconception_tags": ["calculator_use_instead_of_algebraic_eval", "arithmetic_evaluation_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Isolate given ratio", "marks": 1},
            {"step": 2, "criterion": "Determine missing coordinate with Pythagoras", "marks": 1},
            {"step": 3, "criterion": "Substitute into expression", "marks": 1},
            {"step": 4, "criterion": f"Evaluate accurately to {ans}", "marks": 1},
        ],
        "hints": {
            "tier_1": "Isolate the trig ratio first and use Pythagoras to find the missing side.",
            "tier_2": "Substitute the fraction ratios into the expression.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_41_cartesian_evaluate_expression_without_calculator",
    }


# 42. Angle of elevation calculate height of object SVG
def arch_42_angle_of_elevation_calculate_height_of_object_svg(rng: random.Random) -> Dict[str, Any]:
    dist = rng.randint(25, 60)
    angle = rng.choice([26, 32, 38, 44, 52])
    rad = math.radians(angle)
    height = dist * math.tan(rad)
    rounded_h = round(height, 2)
    ans_str = f"{rounded_h:.2f}".replace(".", ",")

    svg_str = _build_elevation_svg(dist, height, angle, label_h="h", label_d=f"{dist} m")
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Angle of elevation {angle}° from observer at distance {dist} m to top of tower",
    }

    prompt = (
        f"An observer standing {dist} m away from the base of a vertical communication tower "
        f"measures an angle of elevation of {angle}^\\circ to the top of the tower.\n\n"
        f"Calculate the height \\(h\\) of the tower, correct to two decimal places."
    )
    sol = (
        f"**Step 1:** Identify the right-angled triangle components:\n"
        f"- Adjacent side (distance from base) = \\({dist}\\text{{ m}}\\)\n"
        f"- Opposite side (height of tower) = \\(h\\)\n"
        f"- Angle of elevation = \\({angle}^\\circ\\)\n\n"
        f"**Step 2:** Use the tangent ratio:\n"
        f"\\[ \\tan({angle}^\\circ) = \\frac{{\\text{{opposite}}}}{{\\text{{adjacent}}}} = \\frac{{h}}{{{dist}}} \\]\n\n"
        f"**Step 3:** Solve for \\(h\\):\n"
        f"\\[ h = {dist} \\times \\tan({angle}^\\circ) \\]\n"
        f"\\[ h \\approx {dist} \\times {math.tan(rad):.4f} = {ans_str}\\text{{ m}} \\]"
    )
    return {
        "id": f"g10_trig_42_{rng.randint(100000, 999999)}",
        "subskill": "42_angle_of_elevation_calculate_height_of_object_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"h = {ans_str} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_42",
        "misconception_tags": ["confusing_sin_and_tan_in_elevation_problems", "rounding_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Select tangent ratio tan(theta) = h / dist", "marks": 1},
            {"step": 2, "criterion": "Isolate h = dist * tan(theta)", "marks": 1},
            {"step": 3, "criterion": "Accurate rounded height with unit m", "marks": 1},
        ],
        "hints": {
            "tier_1": f"tan({angle}°) = h / {dist}.",
            "tier_2": f"h = {dist} * tan({angle}°).",
            "tier_3": f"{ans_str} m",
        },
        "topic": "Trigonometry 2",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_42_angle_of_elevation_calculate_height_of_object_svg",
    }


# 43. Angle of elevation calculate distance from base SVG
def arch_43_angle_of_elevation_calculate_distance_from_base_svg(rng: random.Random) -> Dict[str, Any]:
    height = rng.randint(30, 85)
    angle = rng.choice([25, 34, 42, 50, 58])
    rad = math.radians(angle)
    dist = height / math.tan(rad)
    rounded_d = round(dist, 2)
    ans_str = f"{rounded_d:.2f}".replace(".", ",")

    svg_str = _build_elevation_svg(dist, height, angle, label_h=f"{height} m", label_d="d")
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Angle of elevation {angle}° to top of {height} m building",
    }

    prompt = (
        f"The top of a {height} m high building has an angle of elevation of {angle}^\\circ "
        f"when viewed by a surveyor on level ground.\n\n"
        f"Calculate the distance \\(d\\) from the surveyor to the base of the building, "
        f"correct to two decimal places."
    )
    sol = (
        f"**Step 1:** Set up the tangent ratio:\n"
        f"\\[ \\tan({angle}^\\circ) = \\frac{{\\text{{opposite}}}}{{\\text{{adjacent}}}} = \\frac{{{height}}}{{d}} \\]\n\n"
        f"**Step 2:** Rearrange to isolate \\(d\\):\n"
        f"\\[ d = \\frac{{{height}}}{{\\tan({angle}^\\circ)}} \\]\n\n"
        f"**Step 3:** Calculate and round to two decimal places:\n"
        f"\\[ d \\approx \\frac{{{height}}}{{{math.tan(rad):.4f}}} = {ans_str}\\text{{ m}} \\]"
    )
    return {
        "id": f"g10_trig_43_{rng.randint(100000, 999999)}",
        "subskill": "43_angle_of_elevation_calculate_distance_from_base_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"d = {ans_str} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_43",
        "misconception_tags": ["multiplying_instead_of_dividing_for_adjacent", "rounding_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Set up tan(theta) = height / d", "marks": 1},
            {"step": 2, "criterion": "Rearrange to d = height / tan(theta)", "marks": 1},
            {"step": 3, "criterion": "Accurate rounded distance with unit m", "marks": 1},
        ],
        "hints": {
            "tier_1": f"tan({angle}°) = {height} / d.",
            "tier_2": f"d = {height} / tan({angle}°).",
            "tier_3": f"{ans_str} m",
        },
        "topic": "Trigonometry 2",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_43_angle_of_elevation_calculate_distance_from_base_svg",
    }


# 44. Angle of depression calculate horizontal distance SVG
def arch_44_angle_of_depression_calculate_horizontal_distance_svg(rng: random.Random) -> Dict[str, Any]:
    cliff_h = rng.randint(40, 100)
    angle = rng.choice([20, 27, 33, 41, 48])
    rad = math.radians(angle)
    horiz_d = cliff_h / math.tan(rad)
    rounded_d = round(horiz_d, 2)
    ans_str = f"{rounded_d:.2f}".replace(".", ",")

    # SVG showing observer on top of cliff looking down at a boat
    svg_str = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 260" width="100%" height="240">
  <!-- Horizontal Sight Line -->
  <line x1="80" y1="60" x2="260" y2="60" stroke="#64748B" stroke-width="1.8" stroke-dasharray="5,5"/>
  <!-- Cliff -->
  <rect x="30" y="60" width="50" height="160" fill="#CBD5E1" stroke="#475569" stroke-width="2"/>
  <!-- Sea / Ground level -->
  <line x1="80" y1="220" x2="430" y2="220" stroke="#0284C7" stroke-width="2.5"/>
  <!-- Line of sight -->
  <line x1="80" y1="60" x2="380" y2="220" stroke="#2563EB" stroke-width="2.5"/>
  <!-- Angle of depression arc -->
  <path d="M 130 60 A 50 50 0 0 1 125 82" fill="none" stroke="#DC2626" stroke-width="2"/>
  <text x="140" y="78" font-size="13" font-weight="bold" fill="#DC2626">{angle}°</text>
  <!-- Angle of elevation arc at boat -->
  <path d="M 340 220 A 40 40 0 0 1 345 202" fill="none" stroke="#2563EB" stroke-width="2"/>
  <text x="312" y="212" font-size="13" font-weight="bold" fill="#2563EB">{angle}°</text>
  <!-- Labels -->
  <text x="20" y="145" font-size="13" font-weight="bold" fill="#0F172A">{cliff_h} m</text>
  <text x="230" y="244" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">d</text>
  <text x="375" y="240" font-size="13" fill="#0284C7">Boat</text>
  <text x="45" y="48" font-size="13" fill="#475569">Cliff</text>
</svg>'''
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Observer atop {cliff_h} m cliff measuring angle of depression {angle}° to boat",
    }

    prompt = (
        f"From the top of a cliff {cliff_h} m above sea level, an observer spots a boat at sea. "
        f"The angle of depression from the observer to the boat is {angle}^\\circ.\n\n"
        f"Calculate the horizontal distance \\(d\\) from the base of the cliff to the boat, "
        f"correct to two decimal places."
    )
    sol = (
        f"**Step 1:** Use alternate interior angles:\n"
        f"The angle of depression from the top of the cliff equals the angle of elevation from the boat to the top of the cliff (alternate interior angles between horizontal lines):\n"
        f"\\[ \\text{{Angle at boat}} = {angle}^\\circ \\]\n\n"
        f"**Step 2:** Formulate tangent equation:\n"
        f"\\[ \\tan({angle}^\\circ) = \\frac{{\\text{{opposite}}}}{{\\text{{adjacent}}}} = \\frac{{{cliff_h}}}{{d}} \\]\n\n"
        f"**Step 3:** Solve for \\(d\\):\n"
        f"\\[ d = \\frac{{{cliff_h}}}{{\\tan({angle}^\\circ)}} \\approx \\frac{{{cliff_h}}}{{{math.tan(rad):.4f}}} = {ans_str}\\text{{ m}} \\]"
    )
    return {
        "id": f"g10_trig_44_{rng.randint(100000, 999999)}",
        "subskill": "44_angle_of_depression_calculate_horizontal_distance_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"d = {ans_str} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_44",
        "misconception_tags": ["measuring_angle_of_depression_from_vertical_instead_of_horizontal", "tan_ratio_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Identify angle of elevation from boat = angle of depression", "marks": 1},
            {"step": 2, "criterion": "Set up tan(theta) = cliff_h / d", "marks": 1},
            {"step": 3, "criterion": "Accurate calculation of distance with unit m", "marks": 1},
        ],
        "hints": {
            "tier_1": f"The angle of depression is measured from the HORIZONTAL. The angle inside the triangle at the boat is {angle}°.",
            "tier_2": f"tan({angle}°) = {cliff_h} / d => d = {cliff_h} / tan({angle}°).",
            "tier_3": f"{ans_str} m",
        },
        "topic": "Trigonometry 2",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_44_angle_of_depression_calculate_horizontal_distance_svg",
    }


# 45. Angle of depression equals angle of elevation relation
def arch_45_angle_of_depression_equals_angle_of_elevation_relation(rng: random.Random) -> Dict[str, Any]:
    angle = rng.randint(25, 65)
    tower_h = rng.randint(20, 60)
    svg_str = _build_elevation_svg(40, tower_h, angle, label_h=f"Tower T ({tower_h} m)", label_d="Car C to Base")
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Tower T ({tower_h} m) and Car C with angle {angle}°",
    }
    prompt = (
        f"An observer at the top of a {tower_h} m tower \\(T\\) looks down at a car \\(C\\) with an angle of depression of {angle}^\\circ.\n\n"
        f"1. What is the angle of elevation from the car \\(C\\) to the top of the tower \\(T\\)?\n"
        f"2. Give the geometric reason why these two angles are equal."
    )
    ans = f"{angle}°, alternate interior angles"
    sol = (
        f"**Step 1: Angle of elevation:**\n"
        f"The angle of elevation from the car to the top of the tower is **{angle}°**.\n\n"
        f"**Step 2: Geometric reason:**\n"
        f"The horizontal line from the top of the tower and the horizontal ground line are parallel.\n"
        f"The line of sight acts as a transversal line intersecting these two parallel horizontal lines.\n"
        f"Therefore, the angle of depression and angle of elevation are **alternate interior angles** (\\(\\text{{alt }}\\angle\\text{{s, }} \\parallel \\text{{ lines}}\\)."
    )
    return {
        "id": f"g10_trig_45_{rng.randint(100000, 999999)}",
        "subskill": "45_angle_of_depression_equals_angle_of_elevation_relation",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_trig_45",
        "misconception_tags": ["confusing_depression_with_complementary_angle", "missing_parallel_lines_reason"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": f"State angle is {angle}°", "marks": 1},
            {"step": 2, "criterion": "State reason: alternate interior angles (parallel horizontal lines)", "marks": 1},
        ],
        "hints": {
            "tier_1": "The two horizontal lines are parallel.",
            "tier_2": "Alternate interior angles are equal.",
            "tier_3": ans,
        },
        "topic": "Trigonometry 2",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_45_angle_of_depression_equals_angle_of_elevation_relation",
    }


# 46. Practical ladder against wall height or angle SVG
def arch_46_practical_ladder_against_wall_height_or_angle_svg(rng: random.Random) -> Dict[str, Any]:
    ladder_L = rng.choice([5, 6, 8, 10])
    angle = rng.choice([65, 70, 75])
    rad = math.radians(angle)
    h = ladder_L * math.sin(rad)
    d = ladder_L * math.cos(rad)
    rounded_h = round(h, 2)
    ans_str = f"{rounded_h:.2f}".replace(".", ",")

    svg_str = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 260" width="100%" height="240">
  <!-- Wall and Ground -->
  <line x1="40" y1="220" x2="380" y2="220" stroke="#64748B" stroke-width="3"/>
  <line x1="300" y1="220" x2="300" y2="30" stroke="#475569" stroke-width="6"/>
  <!-- Ladder (slanted line) -->
  <line x1="120" y1="220" x2="300" y2="50" stroke="#D97706" stroke-width="4"/>
  <!-- Angle arc -->
  <path d="M 160 220 A 40 40 0 0 0 155 190" fill="none" stroke="#2563EB" stroke-width="2"/>
  <text x="168" y="206" font-size="14" font-weight="bold" fill="#2563EB">{angle}°</text>
  <!-- Labels -->
  <text x="195" y="125" font-size="14" font-weight="bold" fill="#D97706">Ladder: {ladder_L} m</text>
  <text x="316" y="135" font-size="14" font-weight="bold" fill="#0F172A">h</text>
  <text x="312" y="26" font-size="13" fill="#475569">Wall</text>
  <text x="100" y="240" font-size="13" fill="#64748B">Ground</text>
</svg>'''
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Ladder of length {ladder_L} m leaning against vertical wall at {angle}° angle with ground",
    }

    prompt = (
        f"A ladder of length {ladder_L} m leans against a vertical wall, making an angle of {angle}^\\circ "
        f"with the horizontal ground.\n\n"
        f"Calculate the vertical height \\(h\\) that the ladder reaches up the wall, "
        f"correct to two decimal places."
    )
    sol = (
        f"**Step 1:** Identify the sides of the right triangle:\n"
        f"- Hypotenuse = length of ladder = \\({ladder_L}\\text{{ m}}\\)\n"
        f"- Opposite side = vertical height \\(h\\)\n"
        f"- Angle with ground = \\({angle}^\\circ\\)\n\n"
        f"**Step 2:** Use the sine ratio:\n"
        f"\\[ \\sin({angle}^\\circ) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}} = \\frac{{h}}{{{ladder_L}}} \\]\n\n"
        f"**Step 3:** Solve for \\(h\\):\n"
        f"\\[ h = {ladder_L} \\times \\sin({angle}^\\circ) \\approx {ladder_L} \\times {math.sin(rad):.4f} = {ans_str}\\text{{ m}} \\]"
    )
    return {
        "id": f"g10_trig_46_{rng.randint(100000, 999999)}",
        "subskill": "46_practical_ladder_against_wall_height_or_angle_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"h = {ans_str} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_46",
        "misconception_tags": ["using_cos_instead_of_sin_for_wall_height", "rounding_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Set up equation sin(theta) = h / L", "marks": 1},
            {"step": 2, "criterion": "Isolate h = L * sin(theta)", "marks": 1},
            {"step": 3, "criterion": "Accurate rounded height with unit m", "marks": 1},
        ],
        "hints": {
            "tier_1": f"The ladder is the hypotenuse ({ladder_L} m). The wall is opposite the {angle}° angle.",
            "tier_2": f"h = {ladder_L} * sin({angle}°).",
            "tier_3": f"{ans_str} m",
        },
        "topic": "Trigonometry 2",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_46_practical_ladder_against_wall_height_or_angle_svg",
    }


# 47. Practical guy wire mast length calculation SVG
def arch_47_practical_guy_wire_mast_length_calculation_svg(rng: random.Random) -> Dict[str, Any]:
    mast_h = rng.randint(15, 35)
    anchor_d = rng.randint(12, 30)
    wire_L = math.hypot(mast_h, anchor_d)
    rounded_L = round(wire_L, 2)
    ans_str = f"{rounded_L:.2f}".replace(".", ",")

    svg_str = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 260" width="100%" height="240">
  <line x1="30" y1="220" x2="390" y2="220" stroke="#64748B" stroke-width="2.5"/>
  <!-- Mast -->
  <line x1="320" y1="220" x2="320" y2="40" stroke="#0F172A" stroke-width="5"/>
  <!-- Guy wire -->
  <line x1="100" y1="220" x2="320" y2="40" stroke="#2563EB" stroke-width="3"/>
  <!-- Right angle -->
  <path d="M 304 220 L 304 204 L 320 204" fill="none" stroke="#1E293B" stroke-width="1.8"/>
  <!-- Labels -->
  <text x="335" y="130" font-size="14" font-weight="bold" fill="#0F172A">Mast: {mast_h} m</text>
  <text x="210" y="244" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">Anchor: {anchor_d} m</text>
  <text x="190" y="115" font-size="14" font-weight="bold" fill="#2563EB">Wire L</text>
</svg>'''
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Vertical mast of height {mast_h} m with cable anchored {anchor_d} m from base",
    }

    prompt = (
        f"A vertical radio mast of height {mast_h} m is supported by a guy wire anchored to the ground "
        f"{anchor_d} m from the base of the mast.\n\n"
        f"Calculate the length of the guy wire \\(L\\), correct to two decimal places."
    )
    sol = (
        f"**Step 1:** The mast, ground, and wire form a right-angled triangle where the wire is the hypotenuse \\(L\\).\n\n"
        f"**Step 2:** Apply the Theorem of Pythagoras:\n"
        f"\\[ L^2 = ({mast_h})^2 + ({anchor_d})^2 = {mast_h**2} + {anchor_d**2} = {mast_h**2 + anchor_d**2} \\]\n\n"
        f"**Step 3:** Calculate \\(L\\):\n"
        f"\\[ L = \\sqrt{{{mast_h**2 + anchor_d**2}}} = {ans_str}\\text{{ m}} \\]"
    )
    return {
        "id": f"g10_trig_47_{rng.randint(100000, 999999)}",
        "subskill": "47_practical_guy_wire_mast_length_calculation_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"L = {ans_str} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_47",
        "misconception_tags": ["pythagoras_arithmetic_error", "rounding_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Apply Pythagoras L^2 = h^2 + d^2", "marks": 1},
            {"step": 2, "criterion": "Calculate square root", "marks": 1},
            {"step": 3, "criterion": "Accurate rounded length with unit m", "marks": 1},
        ],
        "hints": {
            "tier_1": f"L^2 = {mast_h}^2 + {anchor_d}^2.",
            "tier_2": f"L = sqrt({mast_h**2 + anchor_d**2}).",
            "tier_3": f"{ans_str} m",
        },
        "topic": "Trigonometry 2",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_47_practical_guy_wire_mast_length_calculation_svg",
    }


# 48. Practical two triangles shared height different angles SVG
def arch_48_practical_two_triangles_shared_height_different_angles_svg(rng: random.Random) -> Dict[str, Any]:
    h = rng.randint(20, 50)
    angle_A = rng.choice([25, 30, 35])
    angle_B = rng.choice([40, 45, 50])

    rad_A = math.radians(angle_A)
    rad_B = math.radians(angle_B)
    dist_A = h / math.tan(rad_A)
    dist_B = h / math.tan(rad_B)
    total_dist = dist_A + dist_B
    rounded_total = round(total_dist, 2)
    ans_str = f"{rounded_total:.2f}".replace(".", ",")

    svg_str = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 260" width="100%" height="240">
  <line x1="20" y1="220" x2="440" y2="220" stroke="#64748B" stroke-width="2.5"/>
  <!-- Tower -->
  <line x1="230" y1="220" x2="230" y2="60" stroke="#0F172A" stroke-width="5"/>
  <!-- Triangle from A -->
  <line x1="60" y1="220" x2="230" y2="60" stroke="#2563EB" stroke-width="2.5"/>
  <!-- Triangle from B -->
  <line x1="390" y1="220" x2="230" y2="60" stroke="#059669" stroke-width="2.5"/>
  <!-- Angles -->
  <text x="100" y="212" font-size="13" font-weight="bold" fill="#2563EB">{angle_A}°</text>
  <text x="350" y="212" font-size="13" font-weight="bold" fill="#059669">{angle_B}°</text>
  <!-- Labels -->
  <text x="240" y="140" font-size="14" font-weight="bold" fill="#0F172A">{h} m</text>
  <text x="45" y="240" font-size="14" font-weight="bold" fill="#2563EB">A</text>
  <text x="395" y="240" font-size="14" font-weight="bold" fill="#059669">B</text>
  <text x="230" y="46" font-size="13" fill="#64748B" text-anchor="middle">Tower</text>
</svg>'''
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Two observers A and B on opposite sides of {h} m tower with elevation angles {angle_A}° and {angle_B}°",
    }

    prompt = (
        f"Two observers \\(A\\) and \\(B\\) stand on level ground on opposite sides of a {h} m high tower. "
        f"The angle of elevation to the top of the tower from \\(A\\) is {angle_A}^\\circ, "
        f"and from \\(B\\) is {angle_B}^\\circ.\n\n"
        f"Calculate the distance between the two observers \\(AB\\), correct to two decimal places."
    )
    sol = (
        f"**Step 1:** Calculate distance from \\(A\\) to the base of the tower:\n"
        f"\\[ d_A = \\frac{{{h}}}{{\\tan({angle_A}^\\circ)}} \\approx \\frac{{{h}}}{{{math.tan(rad_A):.4f}}} = {dist_A:.2f}\\text{{ m}} \\]\n\n"
        f"**Step 2:** Calculate distance from \\(B\\) to the base of the tower:\n"
        f"\\[ d_B = \\frac{{{h}}}{{\\tan({angle_B}^\\circ)}} \\approx \\frac{{{h}}}{{{math.tan(rad_B):.4f}}} = {dist_B:.2f}\\text{{ m}} \\]\n\n"
        f"**Step 3:** Since they are on opposite sides, add the distances:\n"
        f"\\[ AB = d_A + d_B = {dist_A:.2f} + {dist_B:.2f} = {ans_str}\\text{{ m}} \\]"
    )
    return {
        "id": f"g10_trig_48_{rng.randint(100000, 999999)}",
        "subskill": "48_practical_two_triangles_shared_height_different_angles_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"AB = {ans_str} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_trig_48",
        "misconception_tags": ["subtracting_instead_of_adding_opposite_side_distances", "two_triangle_trig_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Calculate distance from A to base", "marks": 1},
            {"step": 2, "criterion": "Calculate distance from B to base", "marks": 1},
            {"step": 3, "criterion": "Add distances for opposite sides", "marks": 1},
            {"step": 4, "criterion": "Accurate rounded answer", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Compute d_A = {h} / tan({angle_A}°) and d_B = {h} / tan({angle_B}°).",
            "tier_2": "Because they are on opposite sides of the tower, add d_A and d_B.",
            "tier_3": f"{ans_str} m",
        },
        "topic": "Trigonometry 2",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_48_practical_two_triangles_shared_height_different_angles_svg",
    }


# 49. Practical two triangles flagpole on building SVG
def arch_49_practical_two_triangles_flagpole_on_building_svg(rng: random.Random) -> Dict[str, Any]:
    dist = rng.randint(20, 45)
    angle_bld = rng.choice([28, 32, 36])
    angle_flag = angle_bld + rng.choice([8, 10, 12])

    rad_bld = math.radians(angle_bld)
    rad_flag = math.radians(angle_flag)

    h_bld = dist * math.tan(rad_bld)
    h_tot = dist * math.tan(rad_flag)
    flag_h = h_tot - h_bld
    rounded_flag = round(flag_h, 2)
    ans_str = f"{rounded_flag:.2f}".replace(".", ",")

    svg_str = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 260" width="100%" height="240">
  <line x1="30" y1="220" x2="400" y2="220" stroke="#64748B" stroke-width="2.5"/>
  <!-- Building -->
  <rect x="290" y="110" width="70" height="110" fill="#E2E8F0" stroke="#475569" stroke-width="2"/>
  <!-- Flagpole -->
  <line x1="325" y1="110" x2="325" y2="40" stroke="#D97706" stroke-width="3"/>
  <polygon points="325,40 350,48 325,56" fill="#DC2626"/>
  <!-- Sight lines from observer -->
  <line x1="60" y1="220" x2="325" y2="110" stroke="#2563EB" stroke-width="2"/>
  <line x1="60" y1="220" x2="325" y2="40" stroke="#7C3AED" stroke-width="2"/>
  <!-- Angle arcs -->
  <text x="120" y="200" font-size="12" font-weight="bold" fill="#2563EB">{angle_bld}°</text>
  <text x="100" y="175" font-size="12" font-weight="bold" fill="#7C3AED">{angle_flag}°</text>
  <!-- Labels -->
  <text x="180" y="244" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">{dist} m</text>
  <text x="375" y="75" font-size="13" font-weight="bold" fill="#D97706">Flagpole</text>
  <text x="45" y="240" font-size="13" fill="#64748B">Observer</text>
</svg>'''
    d_spec = {
        "kind": "inline_svg",
        "svg": svg_str,
        "diagram_role": "context",
        "caption": f"Observer {dist} m away observing top of building ({angle_bld}°) and top of flagpole ({angle_flag}°)",
    }

    prompt = (
        f"From a point on horizontal ground {dist} m from the base of a building, the angle of elevation "
        f"to the top of the building is {angle_bld}^\\circ, and the angle of elevation to the top of a "
        f"flagpole mounted on the building is {angle_flag}^\\circ.\n\n"
        f"Calculate the height of the flagpole, correct to two decimal places."
    )
    sol = (
        f"**Step 1:** Calculate the height of the building \\(h_1\\):\n"
        f"\\[ h_1 = {dist} \\times \\tan({angle_bld}^\\circ) \\approx {dist} \\times {math.tan(rad_bld):.4f} = {h_bld:.2f}\\text{{ m}} \\]\n\n"
        f"**Step 2:** Calculate total height to the top of the flagpole \\(h_2\\):\n"
        f"\\[ h_2 = {dist} \\times \\tan({angle_flag}^\\circ) \\approx {dist} \\times {math.tan(rad_flag):.4f} = {h_tot:.2f}\\text{{ m}} \\]\n\n"
        f"**Step 3:** Subtract building height from total height:\n"
        f"\\[ \\text{{Height of flagpole}} = h_2 - h_1 = {h_tot:.2f} - {h_bld:.2f} = {ans_str}\\text{{ m}} \\]"
    )
    return {
        "id": f"g10_trig_49_{rng.randint(100000, 999999)}",
        "subskill": "49_practical_two_triangles_flagpole_on_building_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": f"Flagpole = {ans_str} m",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_trig_49",
        "misconception_tags": ["subtracting_angles_before_taking_tangent_fallacy", "two_triangle_subtraction_error"],
        "diagram_spec": d_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Calculate building height h1", "marks": 1},
            {"step": 2, "criterion": "Calculate total height h2", "marks": 1},
            {"step": 3, "criterion": "Subtract h2 - h1", "marks": 1},
            {"step": 4, "criterion": "Accurate rounded answer with unit m", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Warning: tan({angle_flag}° - {angle_bld}°) is NOT the difference! Calculate each height separately.",
            "tier_2": f"h_total = {dist} * tan({angle_flag}°) and h_building = {dist} * tan({angle_bld}°).",
            "tier_3": f"{ans_str} m",
        },
        "topic": "Trigonometry 2",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_49_practical_two_triangles_flagpole_on_building_svg",
    }


# 50. Trigonometry diagnostic autopsy and misconception repair
def arch_50_trigonometry_diagnostic_autopsy_and_misconception_repair(rng: random.Random) -> Dict[str, Any]:
    variants = [
        {
            "fn": "sin",
            "coef": 3,
            "val_str": "1{{,}}5",
            "val_num": 1.5,
            "target_ratio_str": "0{{,}}5",
            "theta_deg": "30^\\circ",
        },
        {
            "fn": "cos",
            "coef": 2,
            "val_str": "1",
            "val_num": 1.0,
            "target_ratio_str": "0{{,}}5",
            "theta_deg": "60^\\circ",
        },
        {
            "fn": "tan",
            "coef": 4,
            "val_str": "4",
            "val_num": 4.0,
            "target_ratio_str": "1",
            "theta_deg": "45^\\circ",
        },
        {
            "fn": "sin",
            "coef": 4,
            "val_str": "2",
            "val_num": 2.0,
            "target_ratio_str": "0{{,}}5",
            "theta_deg": "30^\\circ",
        },
    ]
    v = rng.choice(variants)
    fn = v["fn"]
    coef = v["coef"]
    val_str = v["val_str"]
    target_str = v["target_ratio_str"]
    theta_deg = v["theta_deg"]

    prompt = (
        f"A student is asked to solve the equation \\({coef}\\{fn} \\theta = {val_str}\\) for acute angle \\(\\theta\\).\n\n"
        f"The student writes:\n"
        f"\\[ \\theta = \\frac{{{val_str}}}{{{coef}\\{fn}}} \\]\n\n"
        f"Identify the fundamental algebraic and trigonometric misconception in the student's working, "
        f"and provide the correct step-by-step solution."
    )
    ans = f"Treating {fn} as a multiplying variable rather than a function; theta = {theta_deg}"
    sol = (
        f"**1. Misconception Autopsy:**\n"
        f"- The student treats the trigonometric operator \\(\\{fn}\\) as a multiplying variable that can be divided out.\n"
        f"- In reality, \\(\\{fn}\\) is a mathematical function that acts on an angle \\(\\theta\\).\n"
        f"- To isolate the angle \\(\\theta\\), one must first isolate the value of \\(\\{fn} \\theta\\), and then apply the inverse function \\(\\{fn}^{{-1}}\\).\n\n"
        f"**2. Correct Solution:**\n"
        f"**Step 1:** Divide both sides by {coef} to isolate \\(\\{fn} \\theta\\):\n"
        f"\\[ \\{fn} \\theta = \\frac{{{val_str}}}{{{coef}}} = {target_str} \\]\n\n"
        f"**Step 2:** Apply inverse {fn}:\n"
        f"\\[ \\theta = \\{fn}^{{-1}}({target_str}) = {theta_deg} \\]"
    )
    return {
        "id": f"g10_trig_50_{rng.randint(100000, 999999)}",
        "subskill": "50_trigonometry_diagnostic_autopsy_and_misconception_repair",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_trig_50",
        "misconception_tags": [f"treating_trig_operator_as_variable_multiplication", "inverse_function_neglect"],
        "marking_schema": [
            {"step": 1, "criterion": f"Explain misconception: treating {fn} as multiplying factor rather than function", "marks": 1},
            {"step": 2, "criterion": f"Demonstrate isolation {fn} theta = {target_str}", "marks": 1},
            {"step": 3, "criterion": f"Apply arc{fn} to get theta = {theta_deg}", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Can you divide by '{fn}' on its own? No, '{fn}' is a function, not a number!",
            "tier_2": f"Divide by {coef} to get {fn} θ = {target_str}, then use inverse {fn}.",
            "tier_3": f"Misconception: dividing by {fn}; Correct answer: θ = {theta_deg}",
        },
        "topic": "Trigonometry 1",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_50_trigonometry_diagnostic_autopsy_and_misconception_repair",
    }


BUILDERS_26_50 = {
    "26_solve_trig_equation_basic_sin_acute": arch_26_solve_trig_equation_basic_sin_acute,
    "27_solve_trig_equation_basic_cos_acute": arch_27_solve_trig_equation_basic_cos_acute,
    "28_solve_trig_equation_basic_tan_acute": arch_28_solve_trig_equation_basic_tan_acute,
    "29_solve_trig_equation_with_coefficient": arch_29_solve_trig_equation_with_coefficient,
    "30_solve_trig_equation_transpose_constant_first": arch_30_solve_trig_equation_transpose_constant_first,
    "31_solve_trig_equation_multiple_angle_2theta": arch_31_solve_trig_equation_multiple_angle_2theta,
    "32_solve_trig_equation_angle_plus_constant": arch_32_solve_trig_equation_angle_plus_constant,
    "33_solve_trig_equation_special_angle_without_calculator": arch_33_solve_trig_equation_special_angle_without_calculator,
    "34_cartesian_definition_radius_r_from_coordinates": arch_34_cartesian_definition_radius_r_from_coordinates,
    "35_cartesian_ratio_sin_cos_tan_from_point_quadrant1": arch_35_cartesian_ratio_sin_cos_tan_from_point_quadrant1,
    "36_cartesian_ratio_point_quadrant2_negative_x": arch_36_cartesian_ratio_point_quadrant2_negative_x,
    "37_cartesian_ratio_point_quadrant3_both_negative": arch_37_cartesian_ratio_point_quadrant3_both_negative,
    "38_cartesian_ratio_point_quadrant4_negative_y": arch_38_cartesian_ratio_point_quadrant4_negative_y,
    "39_cast_rule_determine_sign_of_ratios_in_quadrants": arch_39_cast_rule_determine_sign_of_ratios_in_quadrants,
    "40_cartesian_given_ratio_and_condition_find_other_ratios": arch_40_cartesian_given_ratio_and_condition_find_other_ratios,
    "41_cartesian_evaluate_expression_without_calculator": arch_41_cartesian_evaluate_expression_without_calculator,
    "42_angle_of_elevation_calculate_height_of_object_svg": arch_42_angle_of_elevation_calculate_height_of_object_svg,
    "43_angle_of_elevation_calculate_distance_from_base_svg": arch_43_angle_of_elevation_calculate_distance_from_base_svg,
    "44_angle_of_depression_calculate_horizontal_distance_svg": arch_44_angle_of_depression_calculate_horizontal_distance_svg,
    "45_angle_of_depression_equals_angle_of_elevation_relation": arch_45_angle_of_depression_equals_angle_of_elevation_relation,
    "46_practical_ladder_against_wall_height_or_angle_svg": arch_46_practical_ladder_against_wall_height_or_angle_svg,
    "47_practical_guy_wire_mast_length_calculation_svg": arch_47_practical_guy_wire_mast_length_calculation_svg,
    "48_practical_two_triangles_shared_height_different_angles_svg": arch_48_practical_two_triangles_shared_height_different_angles_svg,
    "49_practical_two_triangles_flagpole_on_building_svg": arch_49_practical_two_triangles_flagpole_on_building_svg,
    "50_trigonometry_diagnostic_autopsy_and_misconception_repair": arch_50_trigonometry_diagnostic_autopsy_and_misconception_repair,
}
