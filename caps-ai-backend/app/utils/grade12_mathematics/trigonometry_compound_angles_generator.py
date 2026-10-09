"""Grade 12 Mathematics - Trigonometry: Compound and Double Angles Generator.
Covers:
  - Compound Angles: cos(A - B), cos(A + B), sin(A - B), sin(A + B).
  - Double Angles: sin(2A) = 2sin(A)cos(A), cos(2A) = cos^2(A) - sin^2(A) = 2cos^2(A) - 1 = 1 - 2sin^2(A).
  - Determining values without a calculator using special angles (e.g. 75 deg = 45 deg + 30 deg, 15 deg = 45 deg - 30 deg).
  - Proving trigonometric identities with LHS = RHS structure.
  - General solution of trigonometric equations with double angles.

Follows South African CAPS curriculum specifications and the 6-Pillar Generator Contract.
Strictly zero-LLM, deterministic execution.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def generate_grade12_compound_trig_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> Dict[str, Any]:
    r = _rng(seed)
    subskill = mode if mode.startswith("elementary_") else "trig_compound_double_angles"

    archetype = r.choice(["special_angle_compound", "double_angle_identity", "general_solution_quadratic", "double_angle_numerical"])
    if subskill == "elementary_special_angles":
        archetype = "special_angle_compound"
    elif subskill == "elementary_identity":
        archetype = "double_angle_identity"

    if archetype == "special_angle_compound":
        # cos(75) = cos(45 + 30) = cos45 cos30 - sin45 sin30 = (sqrt(6) - sqrt(2)) / 4
        # or sin(75) = sin(45 + 30) = sin45 cos30 + cos45 sin30 = (sqrt(6) + sqrt(2)) / 4
        # or cos(15) = cos(45 - 30) = (sqrt(6) + sqrt(2)) / 4
        func = r.choice(["cos", "sin"])
        ang = r.choice([75, 15])
        if func == "cos" and ang == 75:
            expr_str = r"\cos 75^\circ"
            expansion = r"\cos(45^\circ + 30^\circ) = \cos 45^\circ \cos 30^\circ - \sin 45^\circ \sin 30^\circ"
            calc = r"\left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) - \left(\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right)"
            ans_str = r"\frac{\sqrt{6} - \sqrt{2}}{4}"
        elif func == "sin" and ang == 75:
            expr_str = r"\sin 75^\circ"
            expansion = r"\sin(45^\circ + 30^\circ) = \sin 45^\circ \cos 30^\circ + \cos 45^\circ \sin 30^\circ"
            calc = r"\left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right)"
            ans_str = r"\frac{\sqrt{6} + \sqrt{2}}{4}"
        elif func == "cos" and ang == 15:
            expr_str = r"\cos 15^\circ"
            expansion = r"\cos(45^\circ - 30^\circ) = \cos 45^\circ \cos 30^\circ + \sin 45^\circ \sin 30^\circ"
            calc = r"\left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right)"
            ans_str = r"\frac{\sqrt{6} + \sqrt{2}}{4}"
        else:
            expr_str = r"\sin 15^\circ"
            expansion = r"\sin(45^\circ - 30^\circ) = \sin 45^\circ \cos 30^\circ - \cos 45^\circ \sin 30^\circ"
            calc = r"\left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) - \left(\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right)"
            ans_str = r"\frac{\sqrt{6} - \sqrt{2}}{4}"

        prompt = (
            f"Without using a calculator, determine the exact numerical value of:\n"
            f"$${expr_str}$$\n"
            f"Show all steps, using special angles \\(45^\\circ\\) and \\(30^\\circ\\)."
        )
        sample_answer = rf"{expr_str} = {expansion} = {calc} = {ans_str}"

        return {
            "id": f"g12_trig_comp_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-12",
            "topic": "Trigonometry",
            "subskill": "compound_angles_special_angles",
            "learning_objective_id": "g12_math_trig_compound_special",
            "archetype": "special_angle_compound",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": ans_str,
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Correct compound angle expansion ({expansion})", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Substituting special angle values (45 deg and 30 deg)", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Simplified surd form {ans_str}", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "calculator_decimal_given_instead_of_surd", "penalty": 2}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": f"Express ${ang}^\\circ$ as the sum or difference of known special angles: $45^\\circ$ and $30^\\circ$.",
                "tier_2": rf"Apply the compound angle formula: ${expansion}$.",
                "tier_3": rf"Substitute special angle ratios: $\cos 45^\circ = \sin 45^\circ = \frac{{\sqrt{2}}}{{2}}$, $\cos 30^\circ = \frac{{\sqrt{3}}}{{2}}$, $\sin 30^\circ = \frac{{1}}{{2}}$. Answer: ${ans_str}$.",
            },
            "misconception_tags": ["compound_angle_sign_inversion", "special_angles_recall_error"],
            "term": 2,
            "caps_weight_percent": 20,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }

    elif archetype == "double_angle_identity":
        # Prove: sin(2x) / (1 + cos(2x)) = tan(x)
        prompt = (
            f"Prove the following trigonometric identity for all valid values of \\(x\\):\n"
            f"$$\\frac{{\\sin 2x}}{{1 + \\cos 2x}} = \\tan x$$"
        )
        sample_answer = (
            rf"\text{{LHS}} = \frac{{\sin 2x}}{{1 + \cos 2x}}\\\ "
            rf"= \frac{{2\sin x \cos x}}{{1 + (2\cos^2 x - 1)}}\\\ "
            rf"= \frac{{2\sin x \cos x}}{{2\cos^2 x}}\\\ "
            rf"= \frac{{\sin x}}{{\cos x}} = \tan x = \text{{RHS}}"
        )

        return {
            "id": f"g12_trig_id_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-12",
            "topic": "Trigonometry",
            "subskill": "double_angle_identities",
            "learning_objective_id": "g12_math_trig_identities",
            "archetype": "double_angle_identity",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": "LHS = RHS = tan(x)",
            "marks": 4,
            "marking_schema": {
                "total_marks": 4,
                "marking_points": [
                    {"id": "mp_1", "desc": "Expanding numerator sin(2x) = 2sin(x)cos(x)", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Expanding denominator cos(2x) = 2cos^2(x) - 1 to eliminate +1", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Simplifying fraction 2sin(x)cos(x) / 2cos^2(x) = sin(x)/cos(x)", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": "Final identity quotient sin(x)/cos(x) = tan(x) = RHS", "marks": 1, "editable": True},
                ],
                "deductions": [],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": r"Expand $\sin 2x$ in the numerator, and choose the version of $\cos 2x$ that cancels the $+1$ in the denominator.",
                "tier_2": r"Use $\sin 2x = 2\sin x \cos x$ and $\cos 2x = 2\cos^2 x - 1$.",
                "tier_3": r"The denominator becomes $1 + (2\cos^2 x - 1) = 2\cos^2 x$. Cancelling $2\cos x$ leaves $\frac{\sin x}{\cos x} = \tan x$.",
            },
            "misconception_tags": ["incorrect_double_angle_cosine_selection", "treating_sin_2x_as_2_sin_x"],
            "term": 2,
            "caps_weight_percent": 20,
            "suggested_duration_mins": 4,
            "mode": mode,
            "difficulty": "hard",
        }

    else:
        # General solution with double angle: 2cos^2 x + cos x - 1 = 0
        prompt = (
            f"Determine the general solution of the trigonometric equation:\n"
            f"$$2\\cos^2 x + \\cos x - 1 = 0$$"
        )
        sample_answer = (
            rf"(2\cos x - 1)(\cos x + 1) = 0\\\ "
            rf"\cos x = \frac{{1}}{{2}} \quad \text{{or}} \quad \cos x = -1\\\ "
            rf"\text{{Case 1: }} \cos x = \frac{{1}}{{2}} \implies x = \pm 60^\circ + k \cdot 360^\circ, \quad k \in \mathbb{{Z}}\\\ "
            rf"\text{{Case 2: }} \cos x = -1 \implies x = 180^\circ + k \cdot 360^\circ, \quad k \in \mathbb{{Z}}"
        )

        return {
            "id": f"g12_trig_gensol_{random.randint(100000, 999999)}",
            "subject": "mathematics",
            "grade": "grade-12",
            "topic": "Trigonometry",
            "subskill": "general_solution",
            "learning_objective_id": "g12_math_trig_general_solution",
            "archetype": "general_solution_quadratic",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": "x = ±60° + k·360° or x = 180° + k·360°, k ∈ Z",
            "marks": 5,
            "marking_schema": {
                "total_marks": 5,
                "marking_points": [
                    {"id": "mp_1", "desc": "Factorising into (2cos x - 1)(cos x + 1) = 0", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": "Setting factors to zero: cos x = 1/2 or cos x = -1", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Reference angle 60 deg for cos x = 1/2", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": "General solution branches x = ±60° + k·360°", "marks": 1, "editable": True},
                    {"id": "mp_5", "desc": "General solution branch x = 180° + k·360° with k ∈ Z", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "omitted_k_element_Z", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Treat $\\cos x$ as an algebraic variable $u$ so the equation becomes $2u^2 + u - 1 = 0$. Factorise.",
                "tier_2": r"Factorise: $(2\cos x - 1)(\cos x + 1) = 0$, giving $\cos x = \frac{1}{2}$ or $\cos x = -1$.",
                "tier_3": r"For $\cos x = \frac{1}{2}$, reference angle is $60^\circ \implies x = \pm 60^\circ + k \cdot 360^\circ$. For $\cos x = -1 \implies x = 180^\circ + k \cdot 360^\circ, k \in \mathbb{Z}$.",
            },
            "misconception_tags": ["omitted_negative_branch_for_cosine", "omitted_k_element_Z"],
            "term": 2,
            "caps_weight_percent": 20,
            "suggested_duration_mins": 5,
            "mode": mode,
            "difficulty": "hard",
        }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> List[Dict[str, Any]]:
    base_seed = seed if seed is not None else 42
    return [
        generate_grade12_compound_trig_question(
            seed=base_seed + i,
            difficulty=difficulty,
            mode=mode,
        )
        for i in range(count)
    ]
