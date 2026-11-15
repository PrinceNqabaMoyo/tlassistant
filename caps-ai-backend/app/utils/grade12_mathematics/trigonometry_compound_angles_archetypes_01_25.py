"""Grade 12 Mathematics - Trigonometry: Compound and Double Angles (Archetypes 01-25).
100% Aligned with South African National Curriculum Standards (CAPS Grade 12 Paper 2).
Grounded strictly in curriculum_docs_auto/Mathematics_Gr12/Term 1/05. Trigonometry.md and Syllabus.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Common Contract & Helper Functions
# ---------------------------------------------------------------------------

def _base_contract(
    *,
    subskill: str,
    qtype: str,
    prompt: str,
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    hints: List[str],
    worked_solution: str,
    sample_answer: str,
    marking_schema: Dict[str, Any],
    duration_mins: int = 5,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "topic_id": "grade12_mathematics",
        "subtopic_id": "grade12_math_trigonometry",
        "subskill": subskill,
        "mode": f"elementary_{subskill}",
        "term": 1,
        "caps_weight_percent": 25.0,
        "suggested_duration_mins": duration_mins,
        "type": qtype,
        "question_type": qtype,
        "question": prompt,
        "question_text": prompt,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id,
        "misconception_tags": misconception_tags,
        "hints": hints,
        "worked_solution": worked_solution,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
    }
    if extra:
        q.update(extra)
    return q


def _mcq(
    rng: random.Random,
    *,
    subskill: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    hints: List[str],
    worked_solution: str,
    duration_mins: int = 4,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct] + list(distractors)
    rng.shuffle(options)
    extra: Dict[str, Any] = {
        "options": options,
        "correct_answer": correct,
        "answer": correct,
    }
    if diagram_spec:
        extra["diagram_spec"] = diagram_spec
    return _base_contract(
        subskill=subskill,
        qtype="mcq",
        prompt=prompt,
        learning_objective_id=learning_objective_id,
        concept_id=concept_id,
        misconception_tags=misconception_tags,
        hints=hints,
        worked_solution=worked_solution,
        sample_answer=f"Correct Option: {correct}\n\nWorking:\n{worked_solution}",
        marking_schema={"total_marks": 2, "rules": [{"step": "Correct option selected", "marks": 2}]},
        duration_mins=duration_mins,
        extra=extra,
    )


def _typed(
    *,
    subskill: str,
    prompt: str,
    correct_answer: str,
    accepted_answers: List[str],
    learning_objective_id: str,
    concept_id: str,
    misconception_tags: List[str],
    hints: List[str],
    worked_solution: str,
    marks: int = 4,
    duration_mins: int = 5,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    extra: Dict[str, Any] = {
        "correct_answer": correct_answer,
        "answer": correct_answer,
        "accepted_answers": accepted_answers,
    }
    if diagram_spec:
        extra["diagram_spec"] = diagram_spec
    return _base_contract(
        subskill=subskill,
        qtype="typed",
        prompt=prompt,
        learning_objective_id=learning_objective_id,
        concept_id=concept_id,
        misconception_tags=misconception_tags,
        hints=hints,
        worked_solution=worked_solution,
        sample_answer=f"Answer: {correct_answer}\n\nWorking:\n{worked_solution}",
        marking_schema={"total_marks": marks, "rules": [{"step": "Accurate derivation and simplification", "marks": marks}]},
        duration_mins=duration_mins,
        extra=extra,
    )


def _svg_triangle_2d(
    pA: Tuple[float, float],
    pB: Tuple[float, float],
    pC: Tuple[float, float],
    labels: Tuple[str, str, str] = ("A", "B", "C"),
    annotations: Optional[List[Dict[str, Any]]] = None,
    width: int = 450,
    height: int = 280,
) -> Dict[str, Any]:
    """Emit clean inline SVG for 2D triangle."""
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">',
        f'<polygon points="{pA[0]},{pA[1]} {pB[0]},{pB[1]} {pC[0]},{pC[1]}" fill="#f8fafc" stroke="#1e293b" stroke-width="2"/>',
        f'<text x="{pA[0]}" y="{pA[1]-10}" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">{labels[0]}</text>',
        f'<text x="{pB[0]-12}" y="{pB[1]+15}" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">{labels[1]}</text>',
        f'<text x="{pC[0]+12}" y="{pC[1]+15}" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">{labels[2]}</text>',
    ]
    if annotations:
        for ann in annotations:
            ax = ann.get("x", 0)
            ay = ann.get("y", 0)
            atxt = ann.get("text", "")
            acolor = ann.get("color", "#2563eb")
            svg_parts.append(f'<text x="{ax}" y="{ay}" text-anchor="middle" font-size="12" font-weight="bold" fill="{acolor}">{atxt}</text>')
    svg_parts.append("</svg>")
    return {
        "kind": "inline_svg",
        "title": "2D Triangle Construction",
        "svg": "".join(svg_parts),
        "diagram_role": "context",
    }


# ---------------------------------------------------------------------------
# Archetypes 01 - 10
# ---------------------------------------------------------------------------

def _b01_compound_angle_cos_expansion_numerical(rng: random.Random) -> Dict[str, Any]:
    angle_case = rng.choice([75, 15, 105])
    if angle_case == 75:
        expr = r"\cos 75^\circ"
        split = r"\cos(45^\circ + 30^\circ)"
        formula = r"\cos 45^\circ \cos 30^\circ - \sin 45^\circ \sin 30^\circ"
        val = r"\left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) - \left(\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right)"
        ans = r"\frac{\sqrt{6} - \sqrt{2}}{4}"
        accepted = [r"(\sqrt{6}-\sqrt{2})/4", r"(\sqrt{6} - \sqrt{2})/4", ans, r"\frac{\sqrt{6}-\sqrt{2}}{4}"]
    elif angle_case == 15:
        expr = r"\cos 15^\circ"
        split = r"\cos(45^\circ - 30^\circ)"
        formula = r"\cos 45^\circ \cos 30^\circ + \sin 45^\circ \sin 30^\circ"
        val = r"\left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right)"
        ans = r"\frac{\sqrt{6} + \sqrt{2}}{4}"
        accepted = [r"(\sqrt{6}+\sqrt{2})/4", r"(\sqrt{6} + \sqrt{2})/4", ans, r"\frac{\sqrt{6}+\sqrt{2}}{4}"]
    else:  # 105
        expr = r"\cos 105^\circ"
        split = r"\cos(60^\circ + 45^\circ)"
        formula = r"\cos 60^\circ \cos 45^\circ - \sin 60^\circ \sin 45^\circ"
        val = r"\left(\frac{1}{2}\right)\left(\frac{\sqrt{2}}{2}\right) - \left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{2}}{2}\right)"
        ans = r"\frac{\sqrt{2} - \sqrt{6}}{4}"
        accepted = [r"(\sqrt{2}-\sqrt{6})/4", r"(\sqrt{2} - \sqrt{6})/4", ans, r"\frac{\sqrt{2}-\sqrt{6}}{4}"]

    prompt = (
        f"Without using a calculator, determine the exact value of:\n"
        f"$${expr}$$\n"
        f"Show all steps using special angles."
    )
    sol = (
        f"1. Express {expr} in terms of special angles: $${expr} = {split}$$\n"
        f"2. Apply the compound angle formula $\\cos(\\alpha \\pm \\beta)$:\n"
        f"$${split} = {formula}$$\n"
        f"3. Substitute exact special angle values:\n"
        f"$$= {val} = {ans}$$"
    )
    return _typed(
        subskill="01_compound_angle_cos_expansion_numerical",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-01",
        concept_id="compound_angle_cos_special_angles",
        misconception_tags=["sign_error_in_cos_compound_formula", "special_angle_recall_error"],
        hints=[
            "Express the given angle as a sum or difference of known special angles: 30°, 45°, or 60°.",
            r"Recall that \cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta and \cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta.",
            f"The final simplified surd is {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b02_compound_angle_sin_expansion_numerical(rng: random.Random) -> Dict[str, Any]:
    angle_case = rng.choice([75, 15, 105])
    if angle_case == 75:
        expr = r"\sin 75^\circ"
        split = r"\sin(45^\circ + 30^\circ)"
        formula = r"\sin 45^\circ \cos 30^\circ + \cos 45^\circ \sin 30^\circ"
        ans = r"\frac{\sqrt{6} + \sqrt{2}}{4}"
        accepted = [r"(\sqrt{6}+\sqrt{2})/4", r"(\sqrt{6} + \sqrt{2})/4", ans, r"\frac{\sqrt{6}+\sqrt{2}}{4}"]
    elif angle_case == 15:
        expr = r"\sin 15^\circ"
        split = r"\sin(45^\circ - 30^\circ)"
        formula = r"\sin 45^\circ \cos 30^\circ - \cos 45^\circ \sin 30^\circ"
        ans = r"\frac{\sqrt{6} - \sqrt{2}}{4}"
        accepted = [r"(\sqrt{6}-\sqrt{2})/4", r"(\sqrt{6} - \sqrt{2})/4", ans, r"\frac{\sqrt{6}-\sqrt{2}}{4}"]
    else:  # 105
        expr = r"\sin 105^\circ"
        split = r"\sin(60^\circ + 45^\circ)"
        formula = r"\sin 60^\circ \cos 45^\circ + \cos 60^\circ \sin 45^\circ"
        ans = r"\frac{\sqrt{6} + \sqrt{2}}{4}"
        accepted = [r"(\sqrt{6}+\sqrt{2})/4", r"(\sqrt{6} + \sqrt{2})/4", ans, r"\frac{\sqrt{6}+\sqrt{2}}{4}"]

    prompt = (
        f"Without using a calculator, determine the exact value of:\n"
        f"$${expr}$$\n"
        f"Show all steps using special angles."
    )
    sol = (
        f"1. Express {expr} as special angles: $${expr} = {split}$$\n"
        f"2. Apply the compound sine formula:\n"
        f"$${split} = {formula}$$\n"
        f"3. Substitute special angles and simplify to get $${ans}$$."
    )
    return _typed(
        subskill="02_compound_angle_sin_expansion_numerical",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-02",
        concept_id="compound_angle_sin_special_angles",
        misconception_tags=["sign_error_in_sin_compound_formula"],
        hints=[
            r"Use \sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta.",
            "Substitute standard values: sin 30° = 1/2, cos 30° = √3/2, sin 45° = cos 45° = √2/2.",
            f"The exact value is {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b03_compound_angle_cos_condensation(rng: random.Random) -> Dict[str, Any]:
    ang1 = rng.choice([70, 80, 50, 65])
    diff = rng.choice([10, 20])
    ang2 = ang1 - diff
    # cos(A)cos(B) + sin(A)sin(B) = cos(A - B)
    # let A - B = 60 or 30 or 45
    target_special = rng.choice([60, 30, 45])
    ang_b = rng.choice([10, 15, 20, 25])
    ang_a = target_special + ang_b
    expr = rf"\cos {ang_a}^\circ \cos {ang_b}^\circ + \sin {ang_a}^\circ \sin {ang_b}^\circ"
    
    if target_special == 60:
        ans = r"\frac{1}{2}"
        val_str = "1/2"
    elif target_special == 30:
        ans = r"\frac{\sqrt{3}}{2}"
        val_str = r"\sqrt{3}/2"
    else:
        ans = r"\frac{\sqrt{2}}{2}"
        val_str = r"\sqrt{2}/2"

    prompt = (
        f"Simplify the following expression to a single numerical value without using a calculator:\n"
        f"$${expr}$$"
    )
    sol = (
        f"1. Recognise the compound cosine identity:\n"
        f"$$\\cos\\alpha\\cos\\beta + \\sin\\alpha\\sin\\beta = \\cos(\\alpha - \\beta)$$\n"
        f"2. Apply to the given angles:\n"
        f"$${expr} = \\cos({ang_a}^\\circ - {ang_b}^\\circ) = \\cos {target_special}^\\circ = {ans}$$"
    )
    return _typed(
        subskill="03_compound_angle_cos_condensation",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, val_str, "0.5" if target_special == 60 else val_str],
        learning_objective_id="G12-MATH-TRIG-03",
        concept_id="compound_cosine_condensation",
        misconception_tags=["confused_cos_condensation_sign"],
        hints=[
            r"Notice the pattern \cos A \cos B + \sin A \sin B.",
            rf"This condenses to \cos(A - B) = \cos({ang_a}^\circ - {ang_b}^\circ).",
            f"Evaluate the special angle to obtain {ans}.",
        ],
        worked_solution=sol,
        marks=3,
    )


def _b04_compound_angle_sin_condensation(rng: random.Random) -> Dict[str, Any]:
    target_special = rng.choice([30, 45, 60])
    ang_b = rng.choice([12, 18, 24, 25])
    ang_a = target_special + ang_b
    expr = rf"\sin {ang_a}^\circ \cos {ang_b}^\circ - \cos {ang_a}^\circ \sin {ang_b}^\circ"

    if target_special == 30:
        ans = r"\frac{1}{2}"
        val_str = "1/2"
    elif target_special == 60:
        ans = r"\frac{\sqrt{3}}{2}"
        val_str = r"\sqrt{3}/2"
    else:
        ans = r"\frac{\sqrt{2}}{2}"
        val_str = r"\sqrt{2}/2"

    prompt = (
        f"Simplify the following expression to a single numerical value without using a calculator:\n"
        f"$${expr}$$"
    )
    sol = (
        f"1. Recognise the compound sine identity:\n"
        f"$$\\sin\\alpha\\cos\\beta - \\cos\\alpha\\sin\\beta = \\sin(\\alpha - \\beta)$$\n"
        f"2. Apply to the given angles:\n"
        f"$${expr} = \\sin({ang_a}^\\circ - {ang_b}^\\circ) = \\sin {target_special}^\\circ = {ans}$$"
    )
    return _typed(
        subskill="04_compound_angle_sin_condensation",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=[ans, val_str, "0.5" if target_special == 30 else val_str],
        learning_objective_id="G12-MATH-TRIG-04",
        concept_id="compound_sine_condensation",
        misconception_tags=["confused_sin_with_cos_condensation"],
        hints=[
            r"Notice the alternating pattern \sin A \cos B - \cos A \sin B.",
            rf"This condenses to \sin(A - B) = \sin({ang_a}^\circ - {ang_b}^\circ).",
            f"Evaluate the resulting special angle: {ans}.",
        ],
        worked_solution=sol,
        marks=3,
    )


def _b05_compound_angle_tan_expansion(rng: random.Random) -> Dict[str, Any]:
    angle_case = rng.choice([75, 15])
    if angle_case == 75:
        expr = r"\tan 75^\circ"
        expansion = r"\frac{\tan 45^\circ + \tan 30^\circ}{1 - \tan 45^\circ \tan 30^\circ}"
        ans = r"2 + \sqrt{3}"
        accepted = ["2+sqrt(3)", "2 + sqrt(3)", ans, r"2+\sqrt{3}"]
    else:
        expr = r"\tan 15^\circ"
        expansion = r"\frac{\tan 45^\circ - \tan 30^\circ}{1 + \tan 45^\circ \tan 30^\circ}"
        ans = r"2 - \sqrt{3}"
        accepted = ["2-sqrt(3)", "2 - sqrt(3)", ans, r"2-\sqrt{3}"]

    prompt = (
        f"Without using a calculator, determine the exact value of:\n"
        f"$${expr}$$\n"
        f"Show your working using special angles $45^\\circ$ and $30^\\circ$ and rationalise the denominator."
    )
    sol = (
        f"1. Express {expr} using compound angles:\n"
        f"$${expr} = {expansion}$$\n"
        r"2. Substitute $\tan 45^\circ = 1$ and $\tan 30^\circ = \frac{1}{\sqrt{3}}$:" + "\n"
        r"$$= \frac{\sqrt{3} \pm 1}{\sqrt{3} \mp 1}$$" + "\n"
        f"3. Rationalising the denominator yields $${ans}$$."
    )
    return _typed(
        subskill="05_compound_angle_tan_expansion",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-05",
        concept_id="compound_angle_tan",
        misconception_tags=["rationalisation_error"],
        hints=[
            r"Use the identity \tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B}.",
            r"Substitute \tan 45^\circ = 1 and \tan 30^\circ = \frac{\sqrt{3}}{3}.",
            f"Rationalise by multiplying numerator and denominator by the conjugate to get {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b06_double_angle_sin_numerical(rng: random.Random) -> Dict[str, Any]:
    # Pythagorean triples: (3, 4, 5), (5, 12, 13), (8, 15, 17)
    triple = rng.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17)])
    y, x, r_val = triple
    # In quadrant 2: sin > 0, cos < 0
    # sin theta = y / r, cos theta = -x / r
    # sin 2theta = 2 sin cos = 2 * (y/r) * (-x/r) = -2xy / r^2
    num = -2 * x * y
    den = r_val * r_val
    ans = rf"-\frac{{{abs(num)}}}{{{den}}}"
    accepted = [f"{num}/{den}", ans, rf"-{abs(num)}/{den}"]

    prompt = (
        f"If $\\sin\\theta = \\frac{{{y}}}{{{r_val}}}$ and $90^\\circ < \\theta < 180^\\circ$, "
        f"determine the exact value of $\\sin 2\\theta$ without using a calculator."
    )
    sol = (
        f"1. In Quadrant 2, $x < 0$ and $y > 0$:\n"
        f"$$x^2 + y^2 = r^2 \\implies x^2 + {y}^2 = {r_val}^2 \\implies x = -{x}$$\n"
        f"2. Therefore, $\\cos\\theta = -\\frac{{{x}}}{{{r_val}}}$.\n"
        f"3. Use the double-angle formula for sine:\n"
        f"$$\\sin 2\\theta = 2\\sin\\theta\\cos\\theta = 2\\left(\\frac{{{y}}}{{{r_val}}}\\right)\\left(-\\frac{{{x}}}{{{r_val}}}\\right) = {ans}$$"
    )
    return _typed(
        subskill="06_double_angle_sin_numerical",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-06",
        concept_id="double_angle_sin_pythagoras",
        misconception_tags=["quadrant_sign_error_cosine", "forgot_factor_of_two_in_sin2A"],
        hints=[
            r"Find \cos\theta first using x^2 + y^2 = r^2. Notice \theta is in Quadrant 2, so \cos\theta is negative.",
            r"Use \sin 2\theta = 2\sin\theta\cos\theta.",
            f"Multiply the ratios: 2 * ({y}/{r_val}) * (-{x}/{r_val}) = {ans}.",
        ],
        worked_solution=sol,
        marks=4,
    )


def _b07_double_angle_cos_numerical(rng: random.Random) -> Dict[str, Any]:
    triple = rng.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17)])
    y, x, r_val = triple
    # cos theta = x / r
    # cos 2theta = cos^2 - sin^2 = (x^2 - y^2) / r^2
    num = x * x - y * y
    den = r_val * r_val
    sign_str = "-" if num < 0 else ""
    ans = rf"{sign_str}\frac{{{abs(num)}}}{{{den}}}"
    accepted = [f"{num}/{den}", ans, rf"{sign_str}{abs(num)}/{den}"]

    prompt = (
        f"If $\\cos\\theta = \\frac{{{x}}}{{{r_val}}}$ and $\\theta \\in [0^\\circ; 90^\\circ]$, "
        f"determine the exact value of $\\cos 2\\theta$ without using a calculator."
    )
    sol = (
        f"1. Use the double-angle formula for cosine:\n"
        f"$$\\cos 2\\theta = 2\\cos^2\\theta - 1$$\n"
        f"2. Substitute $\\cos\\theta = \\frac{{{x}}}{{{r_val}}}$:\n"
        f"$$\\cos 2\\theta = 2\\left(\\frac{{{x}}}{{{r_val}}}\\right)^2 - 1 = 2\\left(\\frac{{{x*x}}}{{{den}}}\\right) - 1 = \\frac{{{2*x*x} - {den}}}{{{den}}} = {ans}$$"
    )
    return _typed(
        subskill="07_double_angle_cos_numerical",
        prompt=prompt,
        correct_answer=ans,
        accepted_answers=accepted,
        learning_objective_id="G12-MATH-TRIG-07",
        concept_id="double_angle_cos_formulas",
        misconception_tags=["double_angle_formula_confusion"],
        hints=[
            r"You can use \cos 2\theta = 2\cos^2\theta - 1 directly since \cos\theta is already given.",
            rf"Calculate 2 * ({x}/{r_val})^2 - 1.",
            f"The final fraction is {ans}.",
        ],
        worked_solution=sol,
        marks=3,
    )


def _b08_double_angle_sin_algebraic_simplification(rng: random.Random) -> Dict[str, Any]:
    choice = rng.choice(["div_cos", "div_sin"])
    if choice == "div_cos":
        expr = r"\frac{\sin 2x}{2\cos x}"
        ans = r"\sin x"
        dist = [r"\cos x", r"2\sin x", r"\tan x"]
        sol = r"\frac{\sin 2x}{2\cos x} = \frac{2\sin x\cos x}{2\cos x} = \sin x"
    else:
        expr = r"\frac{\sin 2x}{\sin x}"
        ans = r"2\cos x"
        dist = [r"\cos x", r"2\sin x", r"\cos 2x"]
        sol = r"\frac{\sin 2x}{\sin x} = \frac{2\sin x\cos x}{\sin x} = 2\cos x"

    prompt = f"Simplify the expression to a single trigonometric term:\n$${expr}$$"
    return _mcq(
        rng,
        subskill="08_double_angle_sin_algebraic_simplification",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-08",
        concept_id="sin_double_angle_simplification",
        misconception_tags=["cancelled_angle_argument_directly"],
        hints=[
            r"Replace \sin 2x with its double-angle expansion 2\sin x\cos x.",
            "Cancel common factors in the numerator and denominator.",
            f"The simplified expression is {ans}.",
        ],
        worked_solution=sol,
    )


def _b09_double_angle_cos_algebraic_simplification(rng: random.Random) -> Dict[str, Any]:
    prompt = r"Simplify the expression to a single trigonometric ratio:" + "\n" + r"$$\frac{1 - \cos 2x}{\sin 2x}$$"
    ans = r"\tan x"
    dist = [r"\cot x", r"\sin x", r"\cos x"]
    sol = (
        r"1. Use \cos 2x = 1 - 2\sin^2 x:" + "\n"
        r"$$1 - \cos 2x = 1 - (1 - 2\sin^2 x) = 2\sin^2 x$$" + "\n"
        r"2. Use \sin 2x = 2\sin x\cos x:" + "\n"
        r"$$\frac{2\sin^2 x}{2\sin x\cos x} = \frac{\sin x}{\cos x} = \tan x$$"
    )
    return _mcq(
        rng,
        subskill="09_double_angle_cos_algebraic_simplification",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-09",
        concept_id="cos_double_angle_choice_of_identity",
        misconception_tags=["wrong_cos_double_angle_form"],
        hints=[
            r"Choose the form of \cos 2x that cancels the '1': \cos 2x = 1 - 2\sin^2 x.",
            r"The numerator becomes 2\sin^2 x and denominator is 2\sin x\cos x.",
            r"Divide out 2\sin x to get \frac{\sin x}{\cos x} = \tan x.",
        ],
        worked_solution=sol,
    )


def _b10_double_angle_quotient_simplification(rng: random.Random) -> Dict[str, Any]:
    prompt = r"Simplify the expression:" + "\n" + r"$$\frac{\cos 2x}{\cos x - \sin x}$$"
    ans = r"\cos x + \sin x"
    dist = [r"\cos x - \sin x", r"1", r"\tan x"]
    sol = (
        r"1. Expand \cos 2x as the difference of squares: \cos^2 x - \sin^2 x." + "\n"
        r"2. Factorise the numerator: (\cos x - \sin x)(\cos x + \sin x)." + "\n"
        r"3. Cancel the common factor (\cos x - \sin x) to obtain \cos x + \sin x."
    )
    return _mcq(
        rng,
        subskill="10_double_angle_quotient_simplification",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-10",
        concept_id="cos_difference_of_squares_factorisation",
        misconception_tags=["invalid_distribution_over_division"],
        hints=[
            r"Recall that \cos 2x = \cos^2 x - \sin^2 x.",
            r"Factorise \cos^2 x - \sin^2 x as a difference of two squares.",
            rf"Cancel (\cos x - \sin x) with the denominator to leave {ans}.",
        ],
        worked_solution=sol,
    )


# ---------------------------------------------------------------------------
# Archetypes 11 - 25
# ---------------------------------------------------------------------------

def _b11_pythagorean_identity_with_compound_angles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Which of the following expressions is identically equal to:" + "\n"
        r"$$\sin(\alpha + \beta)\sin(\alpha - \beta)$$"
    )
    ans = r"\sin^2\alpha - \sin^2\beta"
    dist = [
        r"\sin^2\alpha + \sin^2\beta",
        r"\cos^2\alpha - \cos^2\beta",
        r"\sin 2\alpha - \sin 2\beta",
    ]
    sol = (
        r"$$\sin(\alpha + \beta)\sin(\alpha - \beta) = (\sin\alpha\cos\beta + \cos\alpha\sin\beta)(\sin\alpha\cos\beta - \cos\alpha\sin\beta)$$" + "\n"
        r"$$= \sin^2\alpha\cos^2\beta - \cos^2\alpha\sin^2\beta$$" + "\n"
        r"$$= \sin^2\alpha(1 - \sin^2\beta) - (1 - \sin^2\alpha)\sin^2\beta = \sin^2\alpha - \sin^2\beta$$"
    )
    return _mcq(
        rng,
        subskill="11_pythagorean_identity_with_compound_angles",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-11",
        concept_id="compound_sine_product_identity",
        misconception_tags=["incorrect_binomial_expansion"],
        hints=[
            r"Multiply the two compound expansions as (A + B)(A - B) = A^2 - B^2.",
            r"Substitute \cos^2\beta = 1 - \sin^2\beta and \cos^2\alpha = 1 - \sin^2\alpha.",
            f"Expanding and cancelling yields {ans}.",
        ],
        worked_solution=sol,
    )


def _b12_trig_identity_proof_lhs_rhs_basic(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Prove the identity:" + "\n"
        r"$$\frac{\sin 2x}{1 + \cos 2x} = \tan x$$" + "\n"
        r"Which sequence of steps correctly establishes that $\text{LHS} = \text{RHS}$?"
    )
    correct = r"\text{LHS} = \frac{2\sin x\cos x}{1 + (2\cos^2 x - 1)} = \frac{2\sin x\cos x}{2\cos^2 x} = \frac{\sin x}{\cos x} = \tan x = \text{RHS}"
    dist = [
        r"\text{LHS} = \frac{2\sin x\cos x}{1 + (1 - 2\sin^2 x)} = \frac{2\sin x\cos x}{2 - 2\sin^2 x} = \tan x = \text{RHS}",
        r"\text{LHS} = \frac{\sin x\cos x}{\cos^2 x} = \tan x = \text{RHS}",
        r"\text{LHS} = \frac{2\sin x}{\cos 2x} = \tan x = \text{RHS}",
    ]
    sol = (
        r"To eliminate the '1' in the denominator, select \cos 2x = 2\cos^2 x - 1." + "\n"
        r"Then: \frac{2\sin x\cos x}{1 + 2\cos^2 x - 1} = \frac{2\sin x\cos x}{2\cos^2 x} = \frac{\sin x}{\cos x} = \tan x."
    )
    return _mcq(
        rng,
        subskill="12_trig_identity_proof_lhs_rhs_basic",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-12",
        concept_id="identity_proof_sin2x_cos2x",
        misconception_tags=["wrong_cos2x_choice_in_proof"],
        hints=[
            r"Start with the more complex side (LHS).",
            r"Substitute \sin 2x = 2\sin x\cos x and \cos 2x = 2\cos^2 x - 1.",
            r"Cancel common factors to reach \frac{\sin x}{\cos x} = \tan x.",
        ],
        worked_solution=sol,
    )


def _b13_trig_identity_proof_lhs_rhs_complex(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"In proving the identity:" + "\n"
        r"$$\frac{1 + \sin 2x}{\cos 2x} = \frac{\cos x + \sin x}{\cos x - \sin x}$$" + "\n"
        r"How should the numerator $1 + \sin 2x$ be rewritten on the LHS?"
    )
    correct = r"\cos^2 x + 2\sin x\cos x + \sin^2 x = (\cos x + \sin x)^2"
    dist = [
        r"1 + 2\sin x\cos x = (1 + \sin x)^2",
        r"\sin^2 x + \cos^2 x + \sin x\cos x = (\sin x + \cos x)^2",
        r"1 + \sin 2x = 2\sin x\cos x",
    ]
    sol = (
        r"Recall the fundamental identity 1 = \sin^2 x + \cos^2 x." + "\n"
        r"Thus 1 + \sin 2x = \cos^2 x + 2\sin x\cos x + \sin^2 x = (\cos x + \sin x)^2." + "\n"
        r"Combined with \cos 2x = (\cos x - \sin x)(\cos x + \sin x), the factor (\cos x + \sin x) cancels to yield RHS."
    )
    return _mcq(
        rng,
        subskill="13_trig_identity_proof_lhs_rhs_complex",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-13",
        concept_id="trinomial_square_in_trig_identities",
        misconception_tags=["failure_to_recognise_perfect_square"],
        hints=[
            r"Replace '1' with \sin^2 x + \cos^2 x.",
            r"Combine with \sin 2x = 2\sin x\cos x to form a complete trinomial square.",
            r"The numerator becomes (\cos x + \sin x)^2.",
        ],
        worked_solution=sol,
    )


def _b14_trig_identity_undefined_values(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"For which values of $x \in [0^\circ; 360^\circ]$ is the identity:" + "\n"
        r"$$\frac{\sin 2x}{1 + \cos 2x} = \tan x$$" + "\n"
        r"undefined?"
    )
    correct = r"x = 90^\circ, 180^\circ, 270^\circ"
    dist = [
        r"x = 0^\circ, 180^\circ, 360^\circ",
        r"x = 45^\circ, 135^\circ, 225^\circ",
        r"x = 90^\circ, 270^\circ \text{ only}",
    ]
    sol = (
        r"An expression is undefined when denominators are zero or tan is undefined:" + "\n"
        r"1. Denominator of LHS: 1 + \cos 2x = 0 \implies \cos 2x = -1 \implies 2x = 180^\circ, 540^\circ \implies x = 90^\circ, 270^\circ." + "\n"
        r"2. Function \tan x = \frac{\sin x}{\cos x} is undefined when \cos x = 0 \implies x = 90^\circ, 270^\circ." + "\n"
        r"3. Also at x = 180^\circ, \cos 2(180^\circ) = \cos 360^\circ = 1, but check endpoints." + "\n"
        r"Specifically: 1 + \cos 2x = 0 at 2x = 180^\circ \implies x = 90^\circ; 2x = 540^\circ \implies x = 270^\circ."
    )
    return _mcq(
        rng,
        subskill="14_trig_identity_undefined_values",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-14",
        concept_id="undefined_trig_values_restrictions",
        misconception_tags=["forgot_tan_asymptote_restrictions"],
        hints=[
            r"Find where the denominator 1 + \cos 2x = 0.",
            r"Find where \tan x is undefined (\cos x = 0).",
            "Combine all restricted angles in the interval [0°; 360°].",
        ],
        worked_solution=sol,
    )


def _b15_general_solution_sin_linear(rng: random.Random) -> Dict[str, Any]:
    val_choice = rng.choice([("1/2", 30), (r"\sqrt{3}/2", 60), (r"\sqrt{2}/2", 45)])
    val_str, ref_ang = val_choice
    shift = rng.choice([10, 15, 20])
    # sin(2x - shift) = val_str
    # 2x - shift = ref + k*360 or 2x - shift = (180 - ref) + k*360
    # x = (ref + shift)/2 + k*180 or x = (180 - ref + shift)/2 + k*180
    x1 = (ref_ang + shift) // 2
    x2 = (180 - ref_ang + shift) // 2
    ans = rf"x = {x1}^\circ + k \cdot 180^\circ \quad \text{{or}} \quad x = {x2}^\circ + k \cdot 180^\circ, \quad k \in \mathbb{{Z}}"
    dist = [
        rf"x = {x1}^\circ + k \cdot 360^\circ \quad \text{{or}} \quad x = {x2}^\circ + k \cdot 360^\circ, \quad k \in \mathbb{{Z}}",
        rf"x = {ref_ang + shift}^\circ + k \cdot 180^\circ, \quad k \in \mathbb{{Z}}",
        rf"x = {x1}^\circ + k \cdot 180^\circ \quad \text{{only}}, \quad k \in \mathbb{{Z}}",
    ]
    prompt = (
        f"Determine the general solution of the equation:\n"
        f"$$\\sin(2x - {shift}^\\circ) = {val_str}$$"
    )
    sol = (
        f"1. Reference angle = ${ref_ang}^\\circ$.\n"
        f"2. Quadrant 1:\n"
        f"$$2x - {shift}^\\circ = {ref_ang}^\\circ + k \\cdot 360^\\circ \\implies 2x = {ref_ang + shift}^\\circ + k \\cdot 360^\\circ \\implies x = {x1}^\\circ + k \\cdot 180^\\circ$$\n"
        f"3. Quadrant 2:\n"
        f"$$2x - {shift}^\\circ = (180^\\circ - {ref_ang}^\\circ) + k \\cdot 360^\\circ = {180 - ref_ang}^\\circ + k \\cdot 360^\\circ$$\n"
        f"$$2x = {180 - ref_ang + shift}^\\circ + k \\cdot 360^\\circ \\implies x = {x2}^\\circ + k \\cdot 180^\\circ, \\quad k \\in \\mathbb{{Z}}$$"
    )
    return _mcq(
        rng,
        subskill="15_general_solution_sin_linear",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-15",
        concept_id="general_solution_sine",
        misconception_tags=["forgot_to_divide_period_by_two"],
        hints=[
            rf"Find the reference angle: \arcsin({val_str}) = {ref_ang}^\circ.",
            r"Sine is positive in Quadrants 1 and 2: \theta = \text{ref} + k\cdot 360^\circ and \theta = 180^\circ - \text{ref} + k\cdot 360^\circ.",
            rf"Divide the entire equation (including k \cdot 360^\circ) by 2 to get k \cdot 180^\circ.",
        ],
        worked_solution=sol,
    )


def _b16_general_solution_cos_linear(rng: random.Random) -> Dict[str, Any]:
    ref_ang = rng.choice([30, 45, 60])
    shift = rng.choice([10, 20])
    val_str = r"\frac{1}{2}" if ref_ang == 60 else (r"\frac{\sqrt{3}}{2}" if ref_ang == 30 else r"\frac{\sqrt{2}}{2}")
    # cos(2x + shift) = val_str
    # 2x + shift = +/- ref + k*360
    # x = (+/- ref - shift)/2 + k*180
    ans1 = (ref_ang - shift) // 2
    ans2 = (-ref_ang - shift) // 2
    ans = rf"x = {ans1}^\circ + k \cdot 180^\circ \quad \text{{or}} \quad x = {ans2}^\circ + k \cdot 180^\circ, \quad k \in \mathbb{{Z}}"
    dist = [
        rf"x = {ans1}^\circ + k \cdot 360^\circ \quad \text{{or}} \quad x = {ans2}^\circ + k \cdot 360^\circ, \quad k \in \mathbb{{Z}}",
        rf"x = {ref_ang - shift}^\circ + k \cdot 180^\circ, \quad k \in \mathbb{{Z}}",
        rf"x = {ans1}^\circ + k \cdot 180^\circ \quad \text{{only}}",
    ]
    prompt = (
        f"Determine the general solution of:\n"
        f"$$\\cos(2x + {shift}^\\circ) = {val_str}$$"
    )
    sol = (
        f"1. Reference angle = ${ref_ang}^\\circ$.\n"
        f"2. For cosine, $2x + {shift}^\\circ = \\pm {ref_ang}^\\circ + k \\cdot 360^\\circ$.\n"
        f"3. First branch: $2x = {ref_ang - shift}^\\circ + k \\cdot 360^\\circ \\implies x = {ans1}^\\circ + k \\cdot 180^\\circ$.\n"
        f"4. Second branch: $2x = {-ref_ang - shift}^\\circ + k \\cdot 360^\\circ \\implies x = {ans2}^\\circ + k \\cdot 180^\\circ, \\quad k \\in \\mathbb{{Z}}$."
    )
    return _mcq(
        rng,
        subskill="16_general_solution_cos_linear",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-16",
        concept_id="general_solution_cosine",
        misconception_tags=["forgot_plus_minus_symmetry_in_cosine"],
        hints=[
            rf"Find the reference angle: {ref_ang}^\circ.",
            r"Cosine general solution: \theta = \pm \text{ref} + k \cdot 360^\circ.",
            "Solve for x and divide the period by 2.",
        ],
        worked_solution=sol,
    )


def _b17_general_solution_tan_linear(rng: random.Random) -> Dict[str, Any]:
    ref_ang = rng.choice([30, 45, 60])
    shift = rng.choice([15, 30])
    val_str = r"\sqrt{3}" if ref_ang == 60 else (r"\frac{1}{\sqrt{3}}" if ref_ang == 30 else "1")
    # tan(2x - shift) = val_str
    # 2x - shift = ref + k*180
    ans_val = (ref_ang + shift) // 2
    ans = rf"x = {ans_val}^\circ + k \cdot 90^\circ, \quad k \in \mathbb{{Z}}"
    dist = [
        rf"x = {ans_val}^\circ + k \cdot 180^\circ, \quad k \in \mathbb{{Z}}",
        rf"x = {ref_ang + shift}^\circ + k \cdot 90^\circ, \quad k \in \mathbb{{Z}}",
        rf"x = {ans_val}^\circ + k \cdot 360^\circ, \quad k \in \mathbb{{Z}}",
    ]
    prompt = (
        f"Determine the general solution of:\n"
        f"$$\\tan(2x - {shift}^\\circ) = {val_str}$$"
    )
    sol = (
        f"1. Reference angle = ${ref_ang}^\\circ$.\n"
        f"2. For tangent, the period is $180^\\circ$:\n"
        f"$$2x - {shift}^\\circ = {ref_ang}^\\circ + k \\cdot 180^\\circ$$\n"
        f"$$2x = {ref_ang + shift}^\\circ + k \\cdot 180^\\circ$$\n"
        f"$$x = {ans_val}^\\circ + k \\cdot 90^\\circ, \\quad k \\in \\mathbb{{Z}}$$"
    )
    return _mcq(
        rng,
        subskill="17_general_solution_tan_linear",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-17",
        concept_id="general_solution_tangent",
        misconception_tags=["used_360_period_for_tangent"],
        hints=[
            r"Tangent has a natural period of 180^\circ (not 360^\circ).",
            rf"Set 2x - {shift}^\circ = {ref_ang}^\circ + k \cdot 180^\circ.",
            r"Dividing by 2 gives a period of k \cdot 90^\circ.",
        ],
        worked_solution=sol,
    )


def _b18_general_solution_double_angle_sin(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Determine the general solution of the equation:" + "\n"
        r"$$\sin 2x = \cos x$$"
    )
    correct = r"x = 90^\circ + k \cdot 180^\circ \quad \text{or} \quad x = 30^\circ + k \cdot 360^\circ \quad \text{or} \quad x = 150^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}"
    dist = [
        r"x = 30^\circ + k \cdot 360^\circ \quad \text{only}",
        r"x = 45^\circ + k \cdot 180^\circ, \quad k \in \mathbb{Z}",
        r"x = 90^\circ + k \cdot 360^\circ \quad \text{or} \quad x = 30^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}",
    ]
    sol = (
        r"1. Substitute \sin 2x = 2\sin x\cos x:" + "\n"
        r"$$2\sin x\cos x - \cos x = 0 \implies \cos x(2\sin x - 1) = 0$$" + "\n"
        r"2. Case 1: \cos x = 0 \implies x = 90^\circ + k \cdot 180^\circ, k \in \mathbb{Z}." + "\n"
        r"3. Case 2: \sin x = \frac{1}{2} \implies x = 30^\circ + k \cdot 360^\circ \text{ or } x = 150^\circ + k \cdot 360^\circ, k \in \mathbb{Z}."
    )
    return _mcq(
        rng,
        subskill="18_general_solution_double_angle_sin",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-18",
        concept_id="double_angle_factorisation_general_sol",
        misconception_tags=["divided_by_cosx_losing_roots"],
        hints=[
            r"Do NOT divide by \cos x, as you will lose roots! Move everything to LHS and factorise.",
            r"Factorise \cos x(2\sin x - 1) = 0.",
            "Solve both factors: cos x = 0 and sin x = 1/2.",
        ],
        worked_solution=sol,
    )


def _b19_general_solution_double_angle_cos_quadratic(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Determine the general solution of:" + "\n"
        r"$$\cos 2x + 3\sin x - 2 = 0$$"
    )
    correct = r"x = 30^\circ + k \cdot 360^\circ \quad \text{or} \quad x = 150^\circ + k \cdot 360^\circ \quad \text{or} \quad x = 90^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}"
    dist = [
        r"x = 30^\circ + k \cdot 180^\circ, \quad k \in \mathbb{Z}",
        r"x = 60^\circ + k \cdot 360^\circ \quad \text{or} \quad x = 120^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}",
        r"x = 45^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}",
    ]
    sol = (
        r"1. Replace \cos 2x with 1 - 2\sin^2 x:" + "\n"
        r"$$1 - 2\sin^2 x + 3\sin x - 2 = 0 \implies -2\sin^2 x + 3\sin x - 1 = 0$$" + "\n"
        r"$$2\sin^2 x - 3\sin x + 1 = 0 \implies (2\sin x - 1)(\sin x - 1) = 0$$" + "\n"
        r"2. \sin x = \frac{1}{2} \implies x = 30^\circ + k \cdot 360^\circ \text{ or } x = 150^\circ + k \cdot 360^\circ." + "\n"
        r"3. \sin x = 1 \implies x = 90^\circ + k \cdot 360^\circ, \quad k \in \mathbb{Z}."
    )
    return _mcq(
        rng,
        subskill="19_general_solution_double_angle_cos_quadratic",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-19",
        concept_id="quadratic_trig_equation_cos2x",
        misconception_tags=["wrong_cos2x_formula_choice"],
        hints=[
            r"Choose \cos 2x = 1 - 2\sin^2 x so the whole equation is in terms of \sin x.",
            r"Factorise the quadratic: (2\sin x - 1)(\sin x - 1) = 0.",
            "Find the general solutions for sin x = 1/2 and sin x = 1.",
        ],
        worked_solution=sol,
    )


def _b20_general_solution_co_ratio_equality(rng: random.Random) -> Dict[str, Any]:
    angle_shift = rng.choice([20, 30, 40])
    prompt = (
        f"Determine the general solution of:\n"
        f"$$\\sin 2x = \\cos(x + {angle_shift}^\\circ)$$"
    )
    ref = 90 - angle_shift
    ans1 = (ref) // 1  # 2x = 90 - (x + shift) + k*360 => 3x = ref + k*360 => x = ref/3 + k*120
    ans_str1 = f"{ref // 3}^\\circ + k \\cdot 120^\\circ" if ref % 3 == 0 else rf"\frac{{{ref}}}{{3}}^\circ + k \cdot 120^\circ"
    
    correct = rf"x = {ans_str1} \quad \text{{or}} \quad x = {180 - ref}^\circ + k \cdot 360^\circ, \quad k \in \mathbb{{Z}}"
    dist = [
        rf"x = {ref}^\\circ + k \\cdot 180^\\circ, \\quad k \\in \\mathbb{{Z}}",
        rf"x = {angle_shift}^\\circ + k \\cdot 360^\\circ, \\quad k \\in \\mathbb{{Z}}",
        rf"x = 30^\\circ + k \\cdot 360^\\circ, \\quad k \\in \\mathbb{{Z}}",
    ]
    sol = (
        f"1. Use co-functions to convert $\\cos(x + {angle_shift}^\\circ)$ to $\\sin(90^\\circ - (x + {angle_shift}^\\circ)) = \\sin({ref}^\\circ - x)$.\n"
        f"2. Branch 1: $2x = ({ref}^\\circ - x) + k \\cdot 360^\\circ \\implies 3x = {ref}^\\circ + k \\cdot 360^\\circ \\implies x = {ans_str1}$.\n"
        f"3. Branch 2: $2x = 180^\\circ - ({ref}^\\circ - x) + k \\cdot 360^\\circ \\implies x = {180 - ref}^\\circ + k \\cdot 360^\\circ, \\quad k \\in \\mathbb{{Z}}$."
    )
    return _mcq(
        rng,
        subskill="20_general_solution_co_ratio_equality",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-20",
        concept_id="co_function_general_solution",
        misconception_tags=["forgot_co_ratio_90_minus_theta"],
        hints=[
            r"Convert cosine to sine using \cos \theta = \sin(90^\circ - \theta).",
            rf"\cos(x + {angle_shift}^\circ) = \sin(90^\circ - x - {angle_shift}^\circ) = \sin({ref}^\circ - x).",
            "Set up both sine quadrants (Q1: angle, Q2: 180° - angle) and solve for x.",
        ],
        worked_solution=sol,
    )


def _b21_specific_interval_solutions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Determine all solutions of the equation $\sin 2x = \cos x$ in the interval $x \in [-180^\circ; 180^\circ]$."
    )
    correct = r"x \in \{-90^\circ; 30^\circ; 90^\circ; 150^\circ\}"
    dist = [
        r"x \in \{30^\circ; 90^\circ; 150^\circ\}",
        r"x \in \{-150^\circ; -30^\circ; 30^\circ; 150^\circ\}",
        r"x \in \{0^\circ; 90^\circ; 180^\circ\}",
    ]
    sol = (
        r"From \sin 2x = \cos x, the general solutions are:" + "\n"
        r"1. x = 90^\circ + k \cdot 180^\circ \implies \text{for } k = -1: -90^\circ; \text{ for } k = 0: 90^\circ." + "\n"
        r"2. x = 30^\circ + k \cdot 360^\circ \implies \text{for } k = 0: 30^\circ." + "\n"
        r"3. x = 150^\circ + k \cdot 360^\circ \implies \text{for } k = 0: 150^\circ." + "\n"
        r"Combined solutions in [-180°; 180°] are \{-90°; 30°; 90°; 150°\}."
    )
    return _mcq(
        rng,
        subskill="21_specific_interval_solutions",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-21",
        concept_id="specific_solutions_on_interval",
        misconception_tags=["omitted_negative_angle_solutions"],
        hints=[
            "Find the general solution first, then test integer values of k.",
            "Ensure all angles lie strictly within the range -180° <= x <= 180°.",
            r"Check k = -1, 0, 1 to identify valid roots: {-90°, 30°, 90°, 150°}.",
        ],
        worked_solution=sol,
    )


def _b22_trig_graph_amplitude_and_period(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    k = rng.choice([2, 3])
    period = 360 // k
    prompt = (
        f"For the trigonometric function $f(x) = {a}\\cos({k}x) - 1$:\n"
        f"State the **amplitude** and the **period** of $f$."
    )
    ans = rf"Amplitude = {a}, Period = {period}^\circ"
    dist = [
        rf"Amplitude = {a - 1}, Period = {period}^\circ",
        rf"Amplitude = {a}, Period = 360^\circ",
        rf"Amplitude = {2*a}, Period = {period//2}^\circ",
    ]
    sol = (
        f"1. Amplitude = $|a| = {a}$ (the vertical shift of -1 does not change amplitude).\n"
        f"2. Period = $\\frac{{360^\\circ}}{{k}} = \\frac{{360^\\circ}}{{{k}}} = {period}^\\circ$."
    )
    return _mcq(
        rng,
        subskill="22_trig_graph_amplitude_and_period",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-22",
        concept_id="trig_graph_parameters",
        misconception_tags=["confused_vertical_shift_with_amplitude"],
        hints=[
            "Amplitude is the absolute value of the coefficient of cos.",
            "Period of cos(kx) is 360° / k.",
            f"Amplitude is {a} and Period is {period}°.",
        ],
        worked_solution=sol,
    )


def _b23_trig_graph_interpretation_svg(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    peak_y = 120 - 35 * a
    svg_data = {
        "kind": "inline_svg",
        "title": "Trigonometric Graphs: f(x) and g(x)",
        "svg": (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" style="background:#ffffff;font-family:Arial,sans-serif;">'
            '<line x1="40" y1="120" x2="460" y2="120" stroke="#334155" stroke-width="1.5"/>'
            '<line x1="250" y1="20" x2="250" y2="220" stroke="#334155" stroke-width="1.5"/>'
            '<text x="465" y="125" font-size="12" fill="#0f172a">x</text>'
            '<text x="255" y="25" font-size="12" fill="#0f172a">y</text>'
            f'<path d="M 50,120 Q 100,{peak_y} 150,120 T 250,120 T 350,120 T 450,120" fill="none" stroke="#2563eb" stroke-width="2"/>'
            '<path d="M 50,210 Q 150,30 250,120 T 450,120" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4"/>'
            f'<text x="140" y="45" font-size="12" font-weight="bold" fill="#2563eb">f(x) = {a}sin(2x)</text>'
            '<text x="320" y="45" font-size="12" font-weight="bold" fill="#dc2626">g(x) = cos(x)</text>'
            '</svg>'
        ),
        "diagram_role": "context",
    }
    prompt = (
        f"Refer to the sketch of $f(x) = {a}\\sin 2x$ and $g(x) = \\cos x$ below for $x \\in [0^\\circ; 180^\\circ]$.\n"
        "At what values of $x$ does $f(x) = g(x)$ on this interval?"
    )
    if a == 2:
        correct = r"x = 14{,}5^\circ \quad \text{and} \quad x = 90^\circ \quad \text{and} \quad x = 165{,}5^\circ"
        sol = (
            r"1. Set $2\sin 2x = \cos x \implies 4\sin x\cos x - \cos x = 0 \implies \cos x(4\sin x - 1) = 0$." + "\n"
            r"2. $\cos x = 0 \implies x = 90^\circ$ on $[0^\circ; 180^\circ]$." + "\n"
            r"3. $\sin x = \frac{1}{4} = 0{,}25 \implies x = 14{,}5^\circ$ or $x = 180^\circ - 14{,}5^\circ = 165{,}5^\circ$."
        )
    else:
        correct = r"x = 9{,}6^\circ \quad \text{and} \quad x = 90^\circ \quad \text{and} \quad x = 170{,}4^\circ"
        sol = (
            r"1. Set $3\sin 2x = \cos x \implies 6\sin x\cos x - \cos x = 0 \implies \cos x(6\sin x - 1) = 0$." + "\n"
            r"2. $\cos x = 0 \implies x = 90^\circ$ on $[0^\circ; 180^\circ]$." + "\n"
            r"3. $\sin x = \frac{1}{6} \approx 0{,}167 \implies x = 9{,}6^\circ$ or $x = 180^\circ - 9{,}6^\circ = 170{,}4^\circ$."
        )
    dist = [
        r"x = 30^\circ \quad \text{and} \quad x = 150^\circ",
        r"x = 45^\circ \quad \text{and} \quad x = 135^\circ",
        r"x = 0^\circ \quad \text{and} \quad x = 180^\circ",
    ]
    return _mcq(
        rng,
        subskill="23_trig_graph_interpretation_svg",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-23",
        concept_id="trig_graph_intersection",
        misconception_tags=["omitted_factorisation_root"],
        hints=[
            r"Equate the two functions: 2\sin 2x = \cos x.",
            r"Factorise \cos x(4\sin x - 1) = 0.",
            "Find angles where cos x = 0 and sin x = 0,25 in [0°; 180°].",
        ],
        worked_solution=sol,
        diagram_spec=svg_data,
    )


def _b24_max_min_value_compound_expression(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 5])
    k = rng.choice([2, 4])
    # f(x) = k*sin(x)*cos(x) + c = (k/2)*sin(2x) + c
    amp = k // 2
    max_val = c + amp
    min_val = c - amp
    prompt = (
        f"Determine the maximum value and minimum value of the expression:\n"
        f"$$f(x) = {k}\\sin x\\cos x + {c}$$"
    )
    ans = f"Maximum = {max_val}, Minimum = {min_val}"
    dist = [
        f"Maximum = {c + k}, Minimum = {c - k}",
        f"Maximum = {max_val}, Minimum = 0",
        f"Maximum = {k}, Minimum = {-k}",
    ]
    sol = (
        f"1. Rewrite using double-angle: ${k}\\sin x\\cos x = {amp}(2\\sin x\\cos x) = {amp}\\sin 2x$.\n"
        f"2. Thus $f(x) = {amp}\\sin 2x + {c}$.\n"
        f"3. Since $-1 \\le \\sin 2x \\le 1$:\n"
        f"- Maximum value $= {amp}(1) + {c} = {max_val}$\n"
        f"- Minimum value $= {amp}(-1) + {c} = {min_val}$"
    )
    return _mcq(
        rng,
        subskill="24_max_min_value_compound_expression",
        prompt=prompt,
        correct=ans,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-24",
        concept_id="amplitude_extrema_compound_trig",
        misconception_tags=["assumed_sin_and_cos_can_both_be_one_simultaneously"],
        hints=[
            r"Express the product \sin x \cos x as \frac{1}{2}\sin 2x.",
            f"The expression becomes {amp}\\sin 2x + {c}.",
            f"Since -1 <= sin 2x <= 1, Max = {max_val} and Min = {min_val}.",
        ],
        worked_solution=sol,
    )


def _b25_reduction_formula_with_negative_angles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        r"Simplify the following expression to a single term without using a calculator:" + "\n"
        r"$$\frac{\sin(180^\circ - x)\cos(360^\circ - x)\tan(-x)}{\cos(90^\circ - x)\sin(180^\circ + x)}$$"
    )
    correct = r"\frac{1}{\cos x}"
    dist = [
        r"-\frac{1}{\cos x}",
        r"\tan x",
        r"-1",
    ]
    sol = (
        r"1. Apply reduction formulas to each factor:" + "\n"
        r"- \sin(180^\circ - x) = \sin x" + "\n"
        r"- \cos(360^\circ - x) = \cos x" + "\n"
        r"- \tan(-x) = -\tan x = -\frac{\sin x}{\cos x}" + "\n"
        r"- \cos(90^\circ - x) = \sin x" + "\n"
        r"- \sin(180^\circ + x) = -\sin x" + "\n"
        r"2. Substitute into fraction:" + "\n"
        r"$$\frac{(\sin x)(\cos x)\left(-\frac{\sin x}{\cos x}\right)}{(\sin x)(-\sin x)} = \frac{-\sin^2 x}{-\sin^2 x \cos x} = \frac{1}{\cos x}$$"
    )
    return _mcq(
        rng,
        subskill="25_reduction_formula_with_negative_angles",
        prompt=prompt,
        correct=correct,
        distractors=dist,
        learning_objective_id="G12-MATH-TRIG-25",
        concept_id="reduction_and_negative_angle_simplification",
        misconception_tags=["sign_error_tan_negative_angle", "co_ratio_confusion"],
        hints=[
            r"Reduce each quadrant term: sin(180° - x) = sin x, cos(360° - x) = cos x, tan(-x) = -tan x.",
            r"Co-ratio: cos(90° - x) = sin x; Quadrant 3: sin(180° + x) = -sin x.",
            "Carefully count the negative signs and cancel matching terms.",
        ],
        worked_solution=sol,
    )


BUILDERS_01_25: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "01_compound_angle_cos_expansion_numerical": _b01_compound_angle_cos_expansion_numerical,
    "02_compound_angle_sin_expansion_numerical": _b02_compound_angle_sin_expansion_numerical,
    "03_compound_angle_cos_condensation": _b03_compound_angle_cos_condensation,
    "04_compound_angle_sin_condensation": _b04_compound_angle_sin_condensation,
    "05_compound_angle_tan_expansion": _b05_compound_angle_tan_expansion,
    "06_double_angle_sin_numerical": _b06_double_angle_sin_numerical,
    "07_double_angle_cos_numerical": _b07_double_angle_cos_numerical,
    "08_double_angle_sin_algebraic_simplification": _b08_double_angle_sin_algebraic_simplification,
    "09_double_angle_cos_algebraic_simplification": _b09_double_angle_cos_algebraic_simplification,
    "10_double_angle_quotient_simplification": _b10_double_angle_quotient_simplification,
    "11_pythagorean_identity_with_compound_angles": _b11_pythagorean_identity_with_compound_angles,
    "12_trig_identity_proof_lhs_rhs_basic": _b12_trig_identity_proof_lhs_rhs_basic,
    "13_trig_identity_proof_lhs_rhs_complex": _b13_trig_identity_proof_lhs_rhs_complex,
    "14_trig_identity_undefined_values": _b14_trig_identity_undefined_values,
    "15_general_solution_sin_linear": _b15_general_solution_sin_linear,
    "16_general_solution_cos_linear": _b16_general_solution_cos_linear,
    "17_general_solution_tan_linear": _b17_general_solution_tan_linear,
    "18_general_solution_double_angle_sin": _b18_general_solution_double_angle_sin,
    "19_general_solution_double_angle_cos_quadratic": _b19_general_solution_double_angle_cos_quadratic,
    "20_general_solution_co_ratio_equality": _b20_general_solution_co_ratio_equality,
    "21_specific_interval_solutions": _b21_specific_interval_solutions,
    "22_trig_graph_amplitude_and_period": _b22_trig_graph_amplitude_and_period,
    "23_trig_graph_interpretation_svg": _b23_trig_graph_interpretation_svg,
    "24_max_min_value_compound_expression": _b24_max_min_value_compound_expression,
    "25_reduction_formula_with_negative_angles": _b25_reduction_formula_with_negative_angles,
}
