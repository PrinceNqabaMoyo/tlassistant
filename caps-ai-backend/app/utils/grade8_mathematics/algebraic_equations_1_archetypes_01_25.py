"""
Grade 8 Mathematics - Algebraic Equations 1 Archetypes (01 to 25).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/02. Algebraic equations 1.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_inspection_one_step_addition(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(4, 25)
    a = rng.randint(3, 19)
    b = ans + a

    return {
        "title": "Solving One-Step Equations by Inspection: Addition",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "01_inspection_one_step_addition",
        "difficulty": "easy",
        "question_text": (
            f"Solve for $x$ by inspection:\n\n"
            f"$$x + {a} = {b}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Identify missing value $x = {b} - {a} = {ans}$ [1 mark]",
        ],
        "hints": [
            f"Think: what number added to {a} gives {b}?",
            f"Subtract {a} from {b}: {b} - {a} = {ans}.",
            f"Solution: $x = {ans}$.",
        ],
        "misconception_tags": ["one_step_addition_subtraction_error"],
        "diagram_spec": None,
    }


def arch_02_inspection_one_step_subtraction(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(5, 30)
    a = rng.randint(3, 15)
    b = ans - a

    return {
        "title": "Solving One-Step Equations by Inspection: Subtraction",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "02_inspection_one_step_subtraction",
        "difficulty": "easy",
        "question_text": (
            f"Solve for $x$ by inspection:\n\n"
            f"$$x - {a} = {b}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Add {a} to {b}: $x = {b} + {a} = {ans}$ [1 mark]",
        ],
        "hints": [
            f"What number minus {a} leaves {b}?",
            f"Add {a} to {b}: {b} + {a} = {ans}.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["subtraction_inverse_addition_error"],
        "diagram_spec": None,
    }


def arch_03_inspection_subtrahend_unknown(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(3, 18)
    b = rng.randint(4, 20)
    a = ans + b

    return {
        "title": "Solving by Inspection: Unknown Subtrahend ($a - x = b$)",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "03_inspection_subtrahend_unknown",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$ by inspection:\n\n"
            f"$${a} - x = {b}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Calculate $x = {a} - {b} = {ans}$ [1 mark]",
        ],
        "hints": [
            f"Think: how much must you subtract from {a} to get {b}?",
            f"Calculate {a} - {b} = {ans}.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["subtrahend_sign_error"],
        "diagram_spec": None,
    }


def arch_04_inspection_one_step_multiplication(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 9)
    ans = rng.randint(3, 12)
    b = a * ans

    return {
        "title": "Solving One-Step Equations by Inspection: Multiplication",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "04_inspection_one_step_multiplication",
        "difficulty": "easy",
        "question_text": (
            f"Solve for $x$ by inspection:\n\n"
            f"$${a}x = {b}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Divide {b} by {a}: $x = {b}/{a} = {ans}$ [1 mark]",
        ],
        "hints": [
            f"What number multiplied by {a} gives {b}?",
            f"{b} ÷ {a} = {ans}.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["multiplication_inverse_division_error"],
        "diagram_spec": None,
    }


def arch_05_inspection_one_step_division(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 7)
    b = rng.randint(3, 11)
    ans = a * b

    return {
        "title": "Solving One-Step Equations by Inspection: Division",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "05_inspection_one_step_division",
        "difficulty": "easy",
        "question_text": (
            f"Solve for $x$ by inspection:\n\n"
            f"$$\\frac{{x}}{{{a}}} = {b}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Multiply {b} by {a}: $x = {b} \\times {a} = {ans}$ [1 mark]",
        ],
        "hints": [
            f"What number divided by {a} equals {b}?",
            f"Multiply both sides by {a}: {b} x {a} = {ans}.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["division_inverse_multiplication_error"],
        "diagram_spec": None,
    }


def arch_06_inspection_divisor_unknown(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(2, 8)
    b = rng.randint(3, 9)
    a = ans * b

    return {
        "title": "Solving by Inspection: Unknown Divisor ($a / x = b$)",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "06_inspection_divisor_unknown",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$ by inspection:\n\n"
            f"$$\\frac{{{a}}}{{x}} = {b}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Calculate $x = {a}/{b} = {ans}$ [1 mark]",
        ],
        "hints": [
            f"What number divides {a} into {b} equal parts?",
            f"Calculate {a} ÷ {b} = {ans}.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["divisor_inversion_error"],
        "diagram_spec": None,
    }


def arch_07_inspection_two_step_mult_add(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    ans = rng.randint(2, 9)
    b = rng.randint(3, 12)
    c = a * ans + b

    return {
        "title": "Solving Two-Step Equations by Inspection: $ax + b = c$",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "07_inspection_two_step_mult_add",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$ by inspection:\n\n"
            f"$${a}x + {b} = {c}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Subtract {b}: {a}x = {c - b} [1 mark]",
            f"Divide by {a}: x = {ans} [1 mark]",
        ],
        "hints": [
            f"First find what {a}x equals: {c} - {b} = {c - b}.",
            f"Now find what number multiplied by {a} equals {c - b}.",
            f"{c - b} ÷ {a} = {ans}.",
        ],
        "misconception_tags": ["two_step_order_inversion_error"],
        "diagram_spec": None,
    }


def arch_08_inspection_two_step_mult_subtract(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    ans = rng.randint(2, 9)
    b = rng.randint(3, 12)
    c = a * ans - b

    return {
        "title": "Solving Two-Step Equations by Inspection: $ax - b = c$",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "08_inspection_two_step_mult_subtract",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$ by inspection:\n\n"
            f"$${a}x - {b} = {c}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Add {b}: {a}x = {c + b} [1 mark]",
            f"Divide by {a}: x = {ans} [1 mark]",
        ],
        "hints": [
            f"First find the value of {a}x: {c} + {b} = {c + b}.",
            f"Then divide {c + b} by {a}.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["two_step_subtraction_addition_inversion"],
        "diagram_spec": None,
    }


def arch_09_inspection_two_step_div_add(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    k = rng.randint(2, 6)
    ans = a * k
    b = rng.randint(2, 8)
    c = k + b

    return {
        "title": "Solving Two-Step Equations by Inspection: Division and Addition",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "09_inspection_two_step_div_add",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$\\frac{{x}}{{{a}}} + {b} = {c}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Subtract {b}: x/{a} = {c - b} [1 mark]",
            f"Multiply by {a}: x = {ans} [1 mark]",
        ],
        "hints": [
            f"First isolate the fraction: $\\frac{{x}}{{{a}}} = {c} - {b} = {k}$.",
            f"Now multiply {k} by {a}: {k} x {a} = {ans}.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["fraction_equation_subtraction_step_error"],
        "diagram_spec": None,
    }


def arch_10_inspection_two_step_div_subtract(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    k = rng.randint(2, 6)
    ans = a * k
    b = rng.randint(2, 8)
    c = k - b

    return {
        "title": "Solving Two-Step Equations by Inspection: Division and Subtraction",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "10_inspection_two_step_div_subtract",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$\\frac{{x}}{{{a}}} - {b} = {c}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Add {b}: x/{a} = {c + b} [1 mark]",
            f"Multiply by {a}: x = {ans} [1 mark]",
        ],
        "hints": [
            f"First add {b} to both sides: $\\frac{{x}}{{{a}}} = {c} + {b} = {k}$.",
            f"Then multiply by {a}: {k} x {a} = {ans}.",
        ],
        "misconception_tags": ["fraction_equation_addition_step_error"],
        "diagram_spec": None,
    }


def arch_11_inspection_negative_solution_addition(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(8, 18)
    b = rng.randint(2, a - 2)
    ans = b - a  # negative integer

    return {
        "title": "Solving One-Step Equations: Negative Integer Solution",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "11_inspection_negative_solution_addition",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$x + {a} = {b}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Subtract {a}: $x = {b} - {a} = {ans}$ [1 mark]",
        ],
        "hints": [
            f"Notice that the target ({b}) is smaller than the added number ({a}).",
            f"This means $x$ must be a negative number.",
            f"$x = {b} - {a} = {ans}$.",
        ],
        "misconception_tags": ["negative_integer_subtraction_result_error"],
        "diagram_spec": None,
    }


def arch_12_inspection_negative_solution_multiplication(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 8)
    k = rng.randint(2, 9)
    b = a * k
    ans = -k

    return {
        "title": "Solving Equations: Negative Product ($ax = -b$)",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "12_inspection_negative_solution_multiplication",
        "difficulty": "easy",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$${a}x = -{b}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Divide -{b} by {a}: $x = -{b}/{a} = {ans}$ [1 mark]",
        ],
        "hints": [
            "A positive multiplied by what gives a negative?",
            f"Divide -{b} by {a}.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["negative_division_sign_rule_error"],
        "diagram_spec": None,
    }


def arch_13_inspection_negative_coefficient_solution(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 7)
    k = rng.randint(2, 9)
    b = a * k
    ans = -k

    return {
        "title": "Solving Equations: Negative Coefficient ($-ax = b$)",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "13_inspection_negative_coefficient_solution",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$-{a}x = {b}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Divide {b} by -{a}: $x = {b}/(-{a}) = {ans}$ [1 mark]",
        ],
        "hints": [
            f"Divide both sides by -{a}.",
            f"Positive divided by negative is negative: {b} ÷ (-{a}) = {ans}.",
        ],
        "misconception_tags": ["dividing_by_negative_coefficient_error"],
        "diagram_spec": None,
    }


def arch_14_inspection_two_step_negative_solution(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    ans = -rng.randint(2, 6)
    b = rng.randint(2, 8)
    c = a * ans + b

    return {
        "title": "Solving Two-Step Equations with Negative Solutions",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "14_inspection_two_step_negative_solution",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$${a}x + {b} = {c}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Subtract {b}: {a}x = {c - b} [1 mark]",
            f"Divide by {a}: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Subtract {b} from {c}: {c} - {b} = {c - b}.",
            f"Divide {c - b} by {a}: ({c - b}) ÷ {a} = {ans}.",
        ],
        "misconception_tags": ["two_step_negative_integer_arithmetic"],
        "diagram_spec": None,
    }


def arch_15_inspection_variable_on_both_sides_simple(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(2, 8)
    a = rng.randint(2, 4)
    c = a + 1
    # ax + b = cx => b = (c - a)x = 1*x => b = ans
    b = ans

    return {
        "title": "Solving Equations: Variable on Both Sides ($ax + b = (a+1)x$)",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "15_inspection_variable_on_both_sides_simple",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$ by inspection:\n\n"
            f"$${a}x + {b} = {c}x$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Subtract {a}x from both sides: {b} = {c - a}x => x = {ans} [1 mark]",
        ],
        "hints": [
            f"Subtract {a}x from both sides.",
            f"On the right: {c}x - {a}x = x.",
            f"Therefore, $x = {b}$.",
        ],
        "misconception_tags": ["variable_on_both_sides_subtraction_error"],
        "diagram_spec": None,
    }


def arch_16_trial_and_improvement_bracket_evaluation(rng: random.Random) -> Dict[str, Any]:
    a = 2
    b = 5
    ans = 4
    target = a * ans + b  # 13

    return {
        "title": "Solving by Trial and Improvement: Testing Candidates",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "16_trial_and_improvement_bracket_evaluation",
        "difficulty": "medium",
        "question_text": (
            f"Consider the equation **$2x + 5 = {target}$**.\n\n"
            "Test the three candidate values **$x = 3$**, **$x = 4$**, and **$x = 5$** "
            "by evaluating the left-hand side. State which value is the true solution."
        ),
        "correct_answer": f"x = {ans}",
        "marking_schema": [
            "Test x = 3: 2(3) + 5 = 11 (too low) [1 mark]",
            "Test x = 4: 2(4) + 5 = 13 (correct solution) [1 mark]",
        ],
        "hints": [
            "Substitute each value into $2x + 5$:",
            f"For x = 3: 2(3) + 5 = 11.",
            f"For x = 4: 2(4) + 5 = 13.",
            f"Since 13 equals the right-hand side, $x = {ans}$ is the solution.",
        ],
        "misconception_tags": ["trial_and_improvement_substitution_error"],
        "diagram_spec": None,
    }


def arch_17_trial_and_improvement_identifying_too_high_too_low(rng: random.Random) -> Dict[str, Any]:
    a = 3
    b = 2
    ans = 7
    target = a * ans - b  # 19

    return {
        "title": "Trial and Improvement: Assessing Too High vs Too Low",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "17_trial_and_improvement_identifying_too_high_too_low",
        "difficulty": "medium",
        "question_text": (
            f"To solve **${a}x - {b} = {target}$**, a learner tries **$x = 6$**.\n\n"
            f"1. Evaluate the left-hand side for $x = 6$.\n"
            "2. State whether $x = 6$ is too large or too small, and predict the exact solution."
        ),
        "correct_answer": f"1. {a}(6) - {b} = 16. 2. Too small (16 < {target}); the exact solution is x = {ans}.",
        "marking_schema": [
            f"Calculate at x = 6: {a}(6) - {b} = 16 [1 mark]",
            f"State too small and identify exact root x = {ans} [1 mark]",
        ],
        "hints": [
            f"At x = 6: {a} x 6 - {b} = 18 - {b} = 16.",
            f"16 is less than {target}, so 6 is too small.",
            f"Try the next integer up: x = {ans}.",
        ],
        "misconception_tags": ["trial_and_improvement_direction_confusion"],
        "diagram_spec": None,
    }


def arch_18_trial_and_improvement_quadratic_inspection(rng: random.Random) -> Dict[str, Any]:
    ans = rng.choice([3, 4, 5, 6])
    val = ans ** 2 + ans

    return {
        "title": "Solving Quadratic Equations by Inspection / Trial ($x^2 + x = k$)",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "18_trial_and_improvement_quadratic_inspection",
        "difficulty": "hard",
        "question_text": (
            f"Find the positive integer solution to:\n\n"
            f"$$x^2 + x = {val}$$\n\n"
            "by testing consecutive positive integers."
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Test integers to find {ans}^2 + {ans} = {ans**2} + {ans} = {val} [1 mark]",
            f"Conclude positive root x = {ans} [1 mark]",
        ],
        "hints": [
            "Test small positive integers: 1, 2, 3, 4, 5...",
            f"Try x = {ans}: ({ans})^2 + {ans} = {ans**2} + {ans} = {val}.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["quadratic_trial_inspection_gap"],
        "diagram_spec": None,
    }


def arch_19_additive_inverse_property(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 12)
    b = rng.randint(15, 30)

    return {
        "title": "Algebraic Operations: The Additive Inverse Property",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "19_additive_inverse_property",
        "difficulty": "easy",
        "question_text": (
            f"To solve the equation **$x + {a} = {b}$**, what operation must be applied "
            "to both sides to isolate $x$ using the **additive inverse**?"
        ),
        "correct_answer": f"Subtract {a} from both sides (add -{a})",
        "marking_schema": [
            f"Identify operation: subtract {a} from both sides [1 mark]",
        ],
        "hints": [
            f"The additive inverse of +{a} is -{a}.",
            f"Subtracting {a} from both sides leaves $x$ alone on the left.",
        ],
        "misconception_tags": ["additive_inverse_operation_confusion"],
        "diagram_spec": None,
    }


def arch_20_multiplicative_inverse_property(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 9)
    b = rng.randint(12, 45)

    return {
        "title": "Algebraic Operations: The Multiplicative Inverse Property",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "20_multiplicative_inverse_property",
        "difficulty": "easy",
        "question_text": (
            f"To solve the equation **${a}x = {b}$**, what operation must be applied "
            "to both sides using the **multiplicative inverse** of {a}?"
        ),
        "correct_answer": f"Multiply both sides by 1/{a} (or divide both sides by {a})",
        "marking_schema": [
            f"State dividing by {a} / multiplying by 1/{a} [1 mark]",
        ],
        "hints": [
            f"The multiplicative inverse (reciprocal) of {a} is $\\frac{{1}}{{{a}}}$.",
            f"Multiplying by $\\frac{{1}}{{{a}}}$ is equivalent to dividing by {a}.",
        ],
        "misconception_tags": ["multiplicative_inverse_operation_confusion"],
        "diagram_spec": None,
    }


def arch_21_verifying_solution_lhs_equals_rhs(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(3, 9)
    ans = rng.randint(2, 6)
    target = a * ans + b

    return {
        "title": "Verifying Solutions: LHS and RHS Equivalence",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "21_verifying_solution_lhs_equals_rhs",
        "difficulty": "medium",
        "question_text": (
            f"Verify whether **$x = {ans}$** is the correct solution to the equation:\n\n"
            f"$${a}x + {b} = {target}$$\n\n"
            "Show your calculations for the Left-Hand Side (LHS) and compare it to the Right-Hand Side (RHS)."
        ),
        "correct_answer": f"LHS = {a}({ans}) + {b} = {a * ans} + {b} = {target}. Since LHS = RHS = {target}, x = {ans} is confirmed as the correct solution.",
        "marking_schema": [
            f"Calculate LHS: {a}({ans}) + {b} = {target} [1 mark]",
            "Conclude LHS = RHS, confirming solution [1 mark]",
        ],
        "hints": [
            f"Replace $x$ in the left side with ({ans}).",
            f"{a} x {ans} + {b} = {a * ans} + {b} = {target}.",
            "Does the result equal the number on the right side?",
        ],
        "misconception_tags": ["lhs_rhs_verification_gap"],
        "diagram_spec": None,
    }


def arch_22_distinguishing_equation_from_expression(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 6)
    b = rng.randint(3, 9)
    c = rng.randint(12, 25)

    return {
        "title": "Distinguishing an Equation from an Algebraic Expression",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "22_distinguishing_equation_from_expression",
        "difficulty": "easy",
        "question_text": (
            f"Explain the mathematical difference between the algebraic expression **${a}x + {b}$** "
            f"and the algebraic equation **${a}x + {b} = {c}$**."
        ),
        "correct_answer": f"An expression ({a}x + {b}) has no equals sign and represents a calculation phrase with many possible values depending on x. An equation ({a}x + {b} = {c}) has an equality sign and states a condition that can be solved for a specific unknown value of x.",
        "marking_schema": [
            "State expression has no equals sign / represents a phrase [1 mark]",
            "State equation contains equals sign / can be solved for specific value [1 mark]",
        ],
        "hints": [
            "Look for the equals sign ($=$).",
            "Can you solve an expression? No, you can only evaluate or simplify it.",
            "An equation states two sides are equal and has a solution.",
        ],
        "misconception_tags": ["equation_expression_conflation"],
        "diagram_spec": None,
    }


def arch_23_identifying_root_from_multiple_choice(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    b = rng.randint(2, 7)
    ans = rng.choice([2, 3, 4, 5])
    target = a * ans - b
    options = [ans - 2, ans, ans + 1, ans + 3]
    rng.shuffle(options)
    opt_str = ", ".join(f"x = {o}" for o in options)

    return {
        "title": "Identifying the Solution from a Given Set of Values",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "23_identifying_root_from_multiple_choice",
        "difficulty": "easy",
        "question_text": (
            f"Which value from the set **\\{{{opt_str}\\}}** satisfies the equation:\n\n"
            f"$${a}x - {b} = {target}$$?"
        ),
        "correct_answer": f"x = {ans}",
        "marking_schema": [
            f"Select correct root x = {ans} [1 mark]",
        ],
        "hints": [
            "Test each candidate value by substituting it into the equation.",
            f"For x = {ans}: {a}({ans}) - {b} = {a * ans} - {b} = {target}.",
        ],
        "misconception_tags": ["root_selection_verification_error"],
        "diagram_spec": None,
    }


def arch_24_translating_thinking_of_a_number_puzzle(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(2, 5)
    ans = rng.randint(3, 9)
    b = rng.randint(3, 9)
    target = a * ans + b

    return {
        "title": "Translating Number Mystery Puzzles into Equations",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "24_translating_thinking_of_a_number_puzzle",
        "difficulty": "medium",
        "question_text": (
            f"I am thinking of a number. If I multiply it by **{a}** and then add **{b}**, "
            f"the result is **{target}**.\n\n"
            "1. Write an algebraic equation for this puzzle using the variable $x$.\n"
            "2. Solve the equation to find the mystery number."
        ),
        "correct_answer": f"1. {a}x + {b} = {target}. 2. x = {ans}.",
        "marking_schema": [
            f"Equation: {a}x + {b} = {target} [1 mark]",
            f"Solution: x = {ans} [1 mark]",
        ],
        "hints": [
            f"Let the mystery number be $x$.",
            f"Multiply by {a} and add {b}: {a}x + {b}.",
            f"Set equal to {target}: {a}x + {b} = {target}.",
            f"Solve: {a}x = {target - b} => x = {ans}.",
        ],
        "misconception_tags": ["number_puzzle_translation_gap"],
        "diagram_spec": None,
    }


def arch_25_translating_difference_number_puzzle(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(12, 35)
    sub = rng.randint(5, 15)
    res = ans - sub

    return {
        "title": "Translating Subtraction Puzzles into Equations",
        "topic": "Algebraic equations 1",
        "grade": 8,
        "term": 2,
        "subskill": "25_translating_difference_number_puzzle",
        "difficulty": "easy",
        "question_text": (
            f"A certain number decreased by **{sub}** gives **{res}**.\n\n"
            "1. Formulate the equation using the variable $n$.\n"
            "2. Solve for $n$."
        ),
        "correct_answer": f"1. n - {sub} = {res}. 2. n = {ans}.",
        "marking_schema": [
            f"Equation: n - {sub} = {res} [1 mark]",
            f"Solution: n = {ans} [1 mark]",
        ],
        "hints": [
            f"'Decreased by {sub}' means subtracting {sub}.",
            f"$n - {sub} = {res}$.",
            f"Add {sub} to both sides: $n = {res} + {sub} = {ans}$.",
        ],
        "misconception_tags": ["decreased_by_subtraction_direction_error"],
        "diagram_spec": None,
    }


BUILDERS_01_25 = [
    arch_01_inspection_one_step_addition,
    arch_02_inspection_one_step_subtraction,
    arch_03_inspection_subtrahend_unknown,
    arch_04_inspection_one_step_multiplication,
    arch_05_inspection_one_step_division,
    arch_06_inspection_divisor_unknown,
    arch_07_inspection_two_step_mult_add,
    arch_08_inspection_two_step_mult_subtract,
    arch_09_inspection_two_step_div_add,
    arch_10_inspection_two_step_div_subtract,
    arch_11_inspection_negative_solution_addition,
    arch_12_inspection_negative_solution_multiplication,
    arch_13_inspection_negative_coefficient_solution,
    arch_14_inspection_two_step_negative_solution,
    arch_15_inspection_variable_on_both_sides_simple,
    arch_16_trial_and_improvement_bracket_evaluation,
    arch_17_trial_and_improvement_identifying_too_high_too_low,
    arch_18_trial_and_improvement_quadratic_inspection,
    arch_19_additive_inverse_property,
    arch_20_multiplicative_inverse_property,
    arch_21_verifying_solution_lhs_equals_rhs,
    arch_22_distinguishing_equation_from_expression,
    arch_23_identifying_root_from_multiple_choice,
    arch_24_translating_thinking_of_a_number_puzzle,
    arch_25_translating_difference_number_puzzle,
]
