"""Grade 7 Mathematics - Algebraic Equations 2: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/05. Algebraic equations 2.md
Focus: Two-step linear equations, equations with brackets, variables on both sides, negative solutions, and geometric/word setups.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Two step add mult positive integers ax + b = c
def arch_01_two_step_add_mult_positive_integers(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5, 6])
    x_val = rng.randint(3, 9)
    b = rng.randint(4, 12)
    c = a * x_val + b
    ans = str(x_val)
    prompt = (
        f"Solve the two-step equation for \\(x\\):\n"
        f"\\[ {a}x + {b} = {c} \\]"
    )
    sol = (
        f"**Step 1:** Subtract {b} from both sides:\n"
        f"$${a}x = {c} - {b} = {c - b}$$\n\n"
        f"**Step 2:** Divide both sides by {a}:\n"
        f"$$x = \\frac{{{c - b}}}{{{a}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_01_{rng.randint(100000, 999999)}",
        "subskill": "01_two_step_add_mult_positive_integers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_01",
        "hints": {"tier_1": f"Subtract {b} from {c}.", "tier_2": f"{c - b} / {a} = {x_val}.", "tier_3": ans},
        "misconception_tags": ["dividing_before_subtracting_constant"]
    }


# 02. Two step sub mult positive integers ax - b = c
def arch_02_two_step_sub_mult_positive_integers(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5, 7])
    x_val = rng.randint(3, 8)
    b = rng.randint(3, 10)
    c = a * x_val - b
    ans = str(x_val)
    prompt = (
        f"Solve the equation for \\(x\\):\n"
        f"\\[ {a}x - {b} = {c} \\]"
    )
    sol = (
        f"**Step 1:** Add {b} to both sides:\n"
        f"$${a}x = {c} + {b} = {c + b}$$\n\n"
        f"**Step 2:** Divide both sides by {a}:\n"
        f"$$x = \\frac{{{c + b}}}{{{a}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_02_{rng.randint(100000, 999999)}",
        "subskill": "02_two_step_sub_mult_positive_integers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_02",
        "hints": {"tier_1": f"Add {b} to {c}.", "tier_2": f"{c + b} / {a} = {x_val}.", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_constant_in_two_step"]
    }


# 03. Two step with variable second b + ax = c
def arch_03_two_step_with_variable_second(rng: random.Random) -> Dict[str, Any]:
    b = rng.randint(5, 15)
    a = rng.choice([2, 3, 4, 5])
    x_val = rng.randint(3, 8)
    c = b + a * x_val
    ans = str(x_val)
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {b} + {a}x = {c} \\]"
    )
    sol = (
        f"**Step 1:** Subtract {b} from both sides:\n"
        f"$${a}x = {c} - {b} = {c - b}$$\n\n"
        f"**Step 2:** Divide by {a}:\n"
        f"$$x = \\frac{{{c - b}}}{{{a}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_03_{rng.randint(100000, 999999)}",
        "subskill": "03_two_step_with_variable_second",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_03",
        "hints": {"tier_1": f"Subtract {b} from {c}.", "tier_2": f"Then divide by {a}.", "tier_3": ans},
        "misconception_tags": ["confused_by_constant_term_written_first"]
    }


# 04. Two step subtraction from constant b - ax = c
def arch_04_two_step_subtraction_from_constant(rng: random.Random) -> Dict[str, Any]:
    b = rng.randint(25, 45)
    a = rng.choice([2, 3, 4])
    x_val = rng.randint(3, 7)
    c = b - a * x_val
    ans = str(x_val)
    prompt = (
        f"Solve the equation:\n"
        f"\\[ {b} - {a}x = {c} \\]"
    )
    sol = (
        f"**Step 1:** Rearrange to isolate the variable term:\n"
        f"$${a}x = {b} - {c} = {b - c}$$\n\n"
        f"**Step 2:** Divide both sides by {a}:\n"
        f"$$x = \\frac{{{b - c}}}{{{a}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_04_{rng.randint(100000, 999999)}",
        "subskill": "04_two_step_subtraction_from_constant",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_04",
        "hints": {"tier_1": f"{a}x = {b} - {c}.", "tier_2": f"x = {b - c} / {a}.", "tier_3": ans},
        "misconception_tags": ["sign_error_with_negative_variable_term"]
    }


# 05. Two step equation bracket positive a(x + b) = c
def arch_05_two_step_equation_bracket_positive(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    b = rng.randint(2, 6)
    x_val = rng.randint(3, 8)
    c = a * (x_val + b)
    ans = str(x_val)
    prompt = (
        f"Solve the equation involving brackets:\n"
        f"\\[ {a}(x + {b}) = {c} \\]"
    )
    sol = (
        f"**Method (Division First):**\n"
        f"Divide both sides by {a}:\n"
        f"$$x + {b} = \\frac{{{c}}}{{{a}}} = {c // a}$$\n\n"
        f"Subtract {b} from both sides:\n"
        f"$$x = {c // a} - {b} = \\mathbf{{{ans}}}$$\n\n"
        f"*(Alternatively, expand first: \\({a}x + {a * b} = {c} \\implies {a}x = {c - a * b} \\implies x = {ans}\\))*"
    )
    return {
        "id": f"g7_eq2_05_{rng.randint(100000, 999999)}",
        "subskill": "05_two_step_equation_bracket_positive",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_05",
        "hints": {"tier_1": f"Divide {c} by {a} first.", "tier_2": f"x + {b} = {c // a}.", "tier_3": ans},
        "misconception_tags": ["distributing_multiplier_to_variable_only"]
    }


# 06. Two step equation bracket subtraction a(x - b) = c
def arch_06_two_step_equation_bracket_subtraction(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    b = rng.randint(2, 5)
    x_val = rng.randint(b + 2, b + 7)
    c = a * (x_val - b)
    ans = str(x_val)
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {a}(x - {b}) = {c} \\]"
    )
    sol = (
        f"**Step 1:** Divide both sides by {a}:\n"
        f"$$x - {b} = \\frac{{{c}}}{{{a}}} = {c // a}$$\n\n"
        f"**Step 2:** Add {b} to both sides:\n"
        f"$$x = {c // a} + {b} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_06_{rng.randint(100000, 999999)}",
        "subskill": "06_two_step_equation_bracket_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_06",
        "hints": {"tier_1": f"Divide {c} by {a}, then add {b}.", "tier_2": f"x - {b} = {c // a}.", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_in_bracket_equation"]
    }


# 07. Two step equation negative bracket multiplier -a(x + b) = c
def arch_07_two_step_equation_negative_bracket_multiplier(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.randint(1, 5)
    x_val = rng.randint(2, 6)
    c = -a * (x_val + b)
    ans = str(x_val)
    prompt = (
        f"Solve the equation with a negative multiplier outside the bracket:\n"
        f"\\[ -{a}(x + {b}) = {c} \\]"
    )
    sol = (
        f"**Step 1:** Divide both sides by -{a}:\n"
        f"$$x + {b} = \\frac{{{c}}}{{-{a}}} = {c // -a}$$\n\n"
        f"**Step 2:** Subtract {b} from both sides:\n"
        f"$$x = {c // -a} - {b} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_07_{rng.randint(100000, 999999)}",
        "subskill": "07_two_step_equation_negative_bracket_multiplier",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_07",
        "hints": {"tier_1": f"Divide {c} by -{a}.", "tier_2": f"x + {b} = {c // -a}.", "tier_3": ans},
        "misconception_tags": ["negative_division_bracket_sign_error"]
    }


# 08. Two step equation negative multiplier with minus -a(x - b) = c
def arch_08_two_step_equation_negative_multiplier_with_minus(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    b = rng.randint(2, 4)
    x_val = rng.randint(b + 2, b + 6)
    c = -a * (x_val - b)
    ans = str(x_val)
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ -{a}(x - {b}) = {c} \\]"
    )
    sol = (
        f"**Step 1:** Divide both sides by -{a}:\n"
        f"$$x - {b} = \\frac{{{c}}}{{-{a}}} = {c // -a}$$\n\n"
        f"**Step 2:** Add {b} to both sides:\n"
        f"$$x = {c // -a} + {b} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_08_{rng.randint(100000, 999999)}",
        "subskill": "08_two_step_equation_negative_multiplier_with_minus",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_08",
        "hints": {"tier_1": f"Divide by -{a}.", "tier_2": f"x - {b} = {c // -a}.", "tier_3": ans},
        "misconception_tags": ["double_negative_bracket_sign_error"]
    }


# 09. Two step division form whole fraction (x + a)/b = c
def arch_09_two_step_division_form_whole_fraction(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4, 5])
    c = rng.randint(4, 9)
    a = rng.randint(2, 6)
    x_val = b * c - a
    ans = str(x_val)
    prompt = (
        f"Solve the equation:\n"
        f"\\[ \\frac{{x + {a}}}{{{b}}} = {c} \\]"
    )
    sol = (
        f"**Step 1:** Multiply both sides by the denominator {b}:\n"
        f"$$x + {a} = {c} \\times {b} = {c * b}$$\n\n"
        f"**Step 2:** Subtract {a} from both sides:\n"
        f"$$x = {c * b} - {a} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_09_{rng.randint(100000, 999999)}",
        "subskill": "09_two_step_division_form_whole_fraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_09",
        "hints": {"tier_1": f"Multiply {c} by {b} first.", "tier_2": f"x + {a} = {c * b}.", "tier_3": ans},
        "misconception_tags": ["subtracting_numerator_constant_before_multiplying_denominator"]
    }


# 10. Two step division form subtraction numerator (x - a)/b = c
def arch_10_two_step_division_form_subtraction_numerator(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4, 5])
    c = rng.randint(3, 8)
    a = rng.randint(2, 7)
    x_val = b * c + a
    ans = str(x_val)
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\frac{{x - {a}}}{{{b}}} = {c} \\]"
    )
    sol = (
        f"**Step 1:** Multiply both sides by {b}:\n"
        f"$$x - {a} = {c} \\times {b} = {c * b}$$\n\n"
        f"**Step 2:** Add {a} to both sides:\n"
        f"$$x = {c * b} + {a} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_10_{rng.randint(100000, 999999)}",
        "subskill": "10_two_step_division_form_subtraction_numerator",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_10",
        "hints": {"tier_1": f"Multiply {c} by {b}.", "tier_2": f"x - {a} = {c * b}.", "tier_3": ans},
        "misconception_tags": ["numerator_subtraction_order_error"]
    }


# 11. Variables both sides simple positive ax = bx + c
def arch_11_variables_both_sides_simple_positive(rng: random.Random) -> Dict[str, Any]:
    diff = rng.choice([2, 3, 4])
    b = rng.randint(2, 5)
    a = b + diff
    x_val = rng.randint(3, 8)
    c = diff * x_val
    ans = str(x_val)
    prompt = (
        f"Solve the equation with the variable on both sides:\n"
        f"\\[ {a}x = {b}x + {c} \\]"
    )
    sol = (
        f"**Step 1:** Subtract \\({b}x\\) from both sides to collect variable terms on the LHS:\n"
        f"$${a}x - {b}x = {c}$$\n"
        f"$${diff}x = {c}$$\n\n"
        f"**Step 2:** Divide both sides by {diff}:\n"
        f"$$x = \\frac{{{c}}}{{{diff}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_11_{rng.randint(100000, 999999)}",
        "subskill": "11_variables_both_sides_simple_positive",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_11",
        "hints": {"tier_1": f"Subtract {b}x from {a}x.", "tier_2": f"{diff}x = {c}.", "tier_3": ans},
        "misconception_tags": ["adding_variable_terms_across_equals_sign"]
    }


# 12. Variables both sides linear terms ax + b = cx
def arch_12_variables_both_sides_linear_terms(rng: random.Random) -> Dict[str, Any]:
    diff = rng.choice([2, 3, 5])
    a = rng.randint(2, 4)
    c = a + diff
    x_val = rng.randint(2, 7)
    b = diff * x_val
    ans = str(x_val)
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {a}x + {b} = {c}x \\]"
    )
    sol = (
        f"**Step 1:** Subtract \\({a}x\\) from both sides:\n"
        f"$${b} = {c}x - {a}x$$\n"
        f"$${b} = {diff}x$$\n\n"
        f"**Step 2:** Divide both sides by {diff}:\n"
        f"$$x = \\frac{{{b}}}{{{diff}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_12_{rng.randint(100000, 999999)}",
        "subskill": "12_variables_both_sides_linear_terms",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_12",
        "hints": {"tier_1": f"Subtract {a}x from {c}x.", "tier_2": f"{diff}x = {b}.", "tier_3": ans},
        "misconception_tags": ["confused_by_constant_remaining_on_lhs"]
    }


# 13. Variables both sides general ax + b = cx + d
def arch_13_variables_both_sides_general(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3])
    diff = rng.choice([2, 3])
    a = c + diff
    x_val = rng.randint(2, 6)
    b = rng.randint(2, 6)
    d = diff * x_val + b
    ans = str(x_val)
    prompt = (
        f"Solve the linear equation:\n"
        f"\\[ {a}x + {b} = {c}x + {d} \\]"
    )
    sol = (
        f"**Step 1:** Subtract \\({c}x\\) from both sides:\n"
        f"$${a}x - {c}x + {b} = {d}$$\n"
        f"$${diff}x + {b} = {d}$$\n\n"
        f"**Step 2:** Subtract {b} from both sides:\n"
        f"$${diff}x = {d} - {b} = {d - b}$$\n\n"
        f"**Step 3:** Divide by {diff}:\n"
        f"$$x = \\frac{{{d - b}}}{{{diff}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_13_{rng.randint(100000, 999999)}",
        "subskill": "13_variables_both_sides_general",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_eq2_13",
        "hints": {"tier_1": f"Subtract {c}x from both sides.", "tier_2": f"{diff}x + {b} = {d}.", "tier_3": ans},
        "misconception_tags": ["sign_errors_collecting_terms_across_equals"]
    }


# 14. Variables both sides with subtraction ax - b = cx + d
def arch_14_variables_both_sides_with_subtraction(rng: random.Random) -> Dict[str, Any]:
    c = 2
    diff = 3
    a = c + diff  # 5
    x_val = 4
    b = 3
    d = diff * x_val - b  # 3*4 - 3 = 9
    ans = str(x_val)
    prompt = (
        f"Solve the equation for \\(x\\):\n"
        f"\\[ {a}x - {b} = {c}x + {d} \\]"
    )
    sol = (
        f"**Step 1:** Subtract \\({c}x\\) from both sides:\n"
        f"$${diff}x - {b} = {d}$$\n\n"
        f"**Step 2:** Add {b} to both sides:\n"
        f"$${diff}x = {d} + {b} = {d + b}$$\n\n"
        f"**Step 3:** Divide by {diff}:\n"
        f"$$x = \\frac{{{d + b}}}{{{diff}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_14_{rng.randint(100000, 999999)}",
        "subskill": "14_variables_both_sides_with_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_eq2_14",
        "hints": {"tier_1": f"{diff}x - {b} = {d}.", "tier_2": f"{diff}x = {d + b}.", "tier_3": ans},
        "misconception_tags": ["transposition_subtraction_sign_error"]
    }


# 15. Negative coefficient two step -ax + b = c
def arch_15_negative_coefficient_two_step(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    x_val = rng.choice([-3, -4, -5])
    b = rng.randint(4, 10)
    c = -a * x_val + b
    ans = str(x_val)
    prompt = (
        f"Solve the equation in the set of integers:\n"
        f"\\[ -{a}x + {b} = {c} \\]"
    )
    sol = (
        f"**Step 1:** Subtract {b} from both sides:\n"
        f"$$-{a}x = {c} - {b} = {c - b}$$\n\n"
        f"**Step 2:** Divide both sides by the negative coefficient \\(-{a}\\):\n"
        f"$$x = \\frac{{{c - b}}}{{-{a}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_15_{rng.randint(100000, 999999)}",
        "subskill": "15_negative_coefficient_two_step",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_15",
        "hints": {"tier_1": f"-{a}x = {c - b}.", "tier_2": f"Divide {c - b} by -{a}.", "tier_3": ans},
        "misconception_tags": ["dividing_by_negative_number_sign_flip_error"]
    }


# 16. Negative solution two step
def arch_16_negative_solution_two_step(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5])
    x_val = rng.choice([-2, -3, -4, -5])
    b = rng.randint(14, 25)
    c = a * x_val + b
    ans = str(x_val)
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {a}x + {b} = {c} \\]"
    )
    sol = (
        f"**Step 1:** Subtract {b} from both sides:\n"
        f"$${a}x = {c} - {b} = {c - b}$$\n\n"
        f"**Step 2:** Divide by {a}:\n"
        f"$$x = \\frac{{{c - b}}}{{{a}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq2_16_{rng.randint(100000, 999999)}",
        "subskill": "16_negative_solution_two_step",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_16",
        "hints": {"tier_1": f"{a}x = {c - b}.", "tier_2": f"A negative divided by positive is negative.", "tier_3": ans},
        "misconception_tags": ["forgetting_negative_sign_in_integer_division"]
    }


# 17. Zero solution two step
def arch_17_zero_solution_two_step(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([4, 6, 7, 8])
    b = rng.randint(10, 25)
    ans = "0"
    prompt = (
        f"Solve the equation:\n"
        f"\\[ {a}x + {b} = {b} \\]"
    )
    sol = (
        f"**Step 1:** Subtract {b} from both sides:\n"
        f"$${a}x = {b} - {b} = 0$$\n\n"
        f"**Step 2:** Divide both sides by {a}:\n"
        f"$$x = \\frac{{0}}{{{a}}} = \\mathbf{{0}}$$"
    )
    return {
        "id": f"g7_eq2_17_{rng.randint(100000, 999999)}",
        "subskill": "17_zero_solution_two_step",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_17",
        "hints": {"tier_1": f"{a}x = 0.", "tier_2": "0 divided by any non-zero number is 0.", "tier_3": ans},
        "misconception_tags": ["thinking_zero_divided_by_a_number_is_undefined"]
    }


# 18. Geometric perimeter rectangle two step
def arch_18_geometric_perimeter_rectangle_two_step(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(4, 8)
    x_val = rng.randint(6, 12)
    p = 2 * (x_val + w)
    ans = str(x_val)
    prompt = (
        f"A rectangle has width \\({w}\\text{{ cm}}\\) and length \\(x\\text{{ cm}}\\).\n"
        f"Its total perimeter is \\({p}\\text{{ cm}}\\).\n\n"
        f"1. Write down an equation using \\(P = 2l + 2w\\).\n"
        f"2. Solve for the length \\(x\\)."
    )
    sol = (
        f"**Step 1:** Set up equation: \\(2x + 2({w}) = {p} \\implies 2x + {2 * w} = {p}\\).\n\n"
        f"**Step 2:** Subtract {2 * w} from both sides:\n"
        f"$$2x = {p} - {2 * w} = {p - 2 * w}$$\n\n"
        f"**Step 3:** Divide by 2:\n"
        f"$$x = \\frac{{{p - 2 * w}}}{{2}} = \\mathbf{{{ans}}}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_eq2_18_{rng.randint(100000, 999999)}",
        "subskill": "18_geometric_perimeter_rectangle_two_step",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_18",
        "hints": {"tier_1": f"2x + {2*w} = {p}.", "tier_2": f"2x = {p - 2*w}.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_double_width_in_perimeter"]
    }


# 19. Geometric perimeter isosceles triangle
def arch_19_geometric_perimeter_isosceles_triangle(rng: random.Random) -> Dict[str, Any]:
    base = rng.randint(5, 11)
    x_val = rng.randint(6, 12)
    p = 2 * x_val + base
    ans = str(x_val)
    prompt = (
        f"An isosceles triangle has two equal sides of length \\(x\\text{{ cm}}\\) and a base of \\({base}\\text{{ cm}}\\).\n"
        f"The perimeter is \\({p}\\text{{ cm}}\\).\n\n"
        f"Solve the equation \\(2x + {base} = {p}\\) to find the length of each equal side."
    )
    sol = (
        f"**Step 1:** Subtract {base} from both sides:\n"
        f"$$2x = {p} - {base} = {p - base}$$\n\n"
        f"**Step 2:** Divide by 2:\n"
        f"$$x = \\frac{{{p - base}}}{{2}} = \\mathbf{{{ans}}}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_eq2_19_{rng.randint(100000, 999999)}",
        "subskill": "19_geometric_perimeter_isosceles_triangle",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_19",
        "hints": {"tier_1": f"2x = {p} - {base}.", "tier_2": f"x = {p - base} / 2.", "tier_3": ans},
        "misconception_tags": ["dividing_by_three_instead_of_two_for_isosceles"]
    }


# 20. Geometric supplementary angles two step
def arch_20_geometric_supplementary_angles_two_step(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([20, 30, 40, 50])
    x_val = (180 - c) // 2
    ans = str(x_val)
    prompt = (
        f"Two adjacent angles on a straight line are \\(2x\\) and \\({c}^\\circ\\).\n\n"
        f"Since angles on a straight line sum to \\(180^\\circ\\), solve:\n"
        f"\\[ 2x + {c}^\\circ = 180^\\circ \\]"
    )
    sol = (
        f"**Step 1:** Subtract {c} from 180:\n"
        f"$$2x = 180 - {c} = {180 - c}$$\n\n"
        f"**Step 2:** Divide by 2:\n"
        f"$$x = \\frac{{{180 - c}}}{{2}} = \\mathbf{{{ans}}}^\\circ$$"
    )
    return {
        "id": f"g7_eq2_20_{rng.randint(100000, 999999)}",
        "subskill": "20_geometric_supplementary_angles_two_step",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_20",
        "hints": {"tier_1": f"2x = 180 - {c}.", "tier_2": f"x = {180 - c} / 2.", "tier_3": ans},
        "misconception_tags": ["straight_line_angle_sum_error"]
    }


# 21. Geometric complementary angles two step
def arch_21_geometric_complementary_angles_two_step(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([15, 24, 30])
    mult = 3
    x_val = (90 - c) // mult
    ans = str(x_val)
    prompt = (
        f"Two complementary angles add up to \\(90^\\circ\\).\n"
        f"The angles are \\(3x\\) and \\({c}^\\circ\\).\n\n"
        f"Solve the equation:\n"
        f"\\[ 3x + {c}^\\circ = 90^\\circ \\]"
    )
    sol = (
        f"**Step 1:** Subtract {c} from 90:\n"
        f"$$3x = 90 - {c} = {90 - c}$$\n\n"
        f"**Step 2:** Divide by 3:\n"
        f"$$x = \\frac{{{90 - c}}}{{3}} = \\mathbf{{{ans}}}^\\circ$$"
    )
    return {
        "id": f"g7_eq2_21_{rng.randint(100000, 999999)}",
        "subskill": "21_geometric_complementary_angles_two_step",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_21",
        "hints": {"tier_1": f"3x = 90 - {c}.", "tier_2": f"x = {90 - c} / 3.", "tier_3": ans},
        "misconception_tags": ["confusing_complementary_with_supplementary"]
    }


# 22. Geometric triangle angles algebraic
def arch_22_geometric_triangle_angles_algebraic(rng: random.Random) -> Dict[str, Any]:
    ang_c = rng.choice([30, 45, 60])
    # x + 2x + ang_c = 180 -> 3x = 180 - ang_c
    x_val = (180 - ang_c) // 3
    ans = str(x_val)
    prompt = (
        f"In a triangle, the three interior angles are \\(x\\), \\(2x\\), and \\({ang_c}^\\circ\\).\n\n"
        f"1. Set up an equation using the triangle angle sum property.\n"
        f"2. Solve for \\(x\\)."
    )
    sol = (
        f"**Step 1:** Triangle angle sum is \\(180^\\circ\\):\n"
        f"$$x + 2x + {ang_c} = 180$$\n"
        f"$$3x + {ang_c} = 180$$\n\n"
        f"**Step 2:** Solve for \\(x\\):\n"
        f"$$3x = 180 - {ang_c} = {180 - ang_c}$$\n"
        f"$$x = \\frac{{{180 - ang_c}}}{{3}} = \\mathbf{{{ans}}}^\\circ$$"
    )
    return {
        "id": f"g7_eq2_22_{rng.randint(100000, 999999)}",
        "subskill": "22_geometric_triangle_angles_algebraic",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_22",
        "hints": {"tier_1": f"Combine like terms: 3x + {ang_c} = 180.", "tier_2": f"3x = {180 - ang_c}.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_combine_angle_variables"]
    }


# 23. Word problem shopping unit cost plus fixed
def arch_23_word_problem_shopping_unit_cost_plus_fixed(rng: random.Random) -> Dict[str, Any]:
    entry_fee = 5
    ride_cost = 8
    rides = rng.randint(4, 8)
    tot = entry_fee + ride_cost * rides
    ans = str(rides)
    prompt = (
        f"A funfair charges an entry fee of R{entry_fee} plus R{ride_cost} per ride.\n"
        f"Ayanda spent a total of R{tot}.\n\n"
        f"Solve the equation \\({ride_cost}x + {entry_fee} = {tot}\\) to find how many rides (\\(x\\)) Ayanda went on."
    )
    sol = (
        f"**Step 1:** Subtract the entry fee:\n"
        f"$${ride_cost}x = {tot} - {entry_fee} = {tot - entry_fee}$$\n\n"
        f"**Step 2:** Divide by the cost per ride:\n"
        f"$$x = \\frac{{{tot - entry_fee}}}{{{ride_cost}}} = \\mathbf{{{ans}}}\\text{{ rides}}$$"
    )
    return {
        "id": f"g7_eq2_23_{rng.randint(100000, 999999)}",
        "subskill": "23_word_problem_shopping_unit_cost_plus_fixed",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_23",
        "hints": {"tier_1": f"{ride_cost}x = {tot} - {entry_fee}.", "tier_2": f"x = {tot - entry_fee} / {ride_cost}.", "tier_3": ans},
        "misconception_tags": ["dividing_total_cost_by_ride_cost_without_subtracting_entry"]
    }


# 24. Word problem taxi fare
def arch_24_word_problem_taxi_fare(rng: random.Random) -> Dict[str, Any]:
    base_fare = 15
    per_km = 8
    km = rng.randint(5, 12)
    tot = base_fare + per_km * km
    ans = str(km)
    prompt = (
        f"A taxi service charges a flat base fee of R{base_fare} plus R{per_km} per kilometre travelled.\n"
        f"If a passenger's total fare was R{tot}, write an equation and solve for the distance \\(d\\) in km."
    )
    sol = (
        f"**Step 1:** Equation: \\({per_km}d + {base_fare} = {tot}\\).\n\n"
        f"**Step 2:** Subtract the base fee:\n"
        f"$${per_km}d = {tot} - {base_fare} = {tot - base_fare}$$\n\n"
        f"**Step 3:** Divide by rate per km:\n"
        f"$$d = \\frac{{{tot - base_fare}}}{{{per_km}}} = \\mathbf{{{ans}}}\\text{{ km}}$$"
    )
    return {
        "id": f"g7_eq2_24_{rng.randint(100000, 999999)}",
        "subskill": "24_word_problem_taxi_fare",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_24",
        "hints": {"tier_1": f"{per_km}d + {base_fare} = {tot}.", "tier_2": f"d = {tot - base_fare} / {per_km}.", "tier_3": ans},
        "misconception_tags": ["adding_base_fare_to_total"]
    }


# 25. Word problem age multiplier plus years
def arch_25_word_problem_age_multiplier_plus_years(rng: random.Random) -> Dict[str, Any]:
    mult = 3
    extra = 4
    x_val = rng.randint(10, 14)
    father_age = mult * x_val + extra
    ans = str(x_val)
    prompt = (
        f"Mr. Khumalo is {father_age} years old. He is {extra} years older than {mult} times his son's age \\(x\\).\n\n"
        f"Set up an equation and solve for the son's age \\(x\\)."
    )
    sol = (
        f"**Step 1:** Equation: \\({mult}x + {extra} = {father_age}\\).\n\n"
        f"**Step 2:** Subtract {extra} from both sides:\n"
        f"$${mult}x = {father_age} - {extra} = {father_age - extra}$$\n\n"
        f"**Step 3:** Divide by {mult}:\n"
        f"$$x = \\frac{{{father_age - extra}}}{{{mult}}} = \\mathbf{{{ans}}}\\text{{ years old}}$$"
    )
    return {
        "id": f"g7_eq2_25_{rng.randint(100000, 999999)}",
        "subskill": "25_word_problem_age_multiplier_plus_years",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq2_25",
        "hints": {"tier_1": f"{mult}x + {extra} = {father_age}.", "tier_2": f"{mult}x = {father_age - extra}.", "tier_3": ans},
        "misconception_tags": ["age_word_problem_equation_setup_error"]
    }
