"""Grade 7 Mathematics - Algebraic Equations 1: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/05. Algebraic equations 1.md
Focus: Concept of an equation, equivalence, solving by inspection, additive & multiplicative inverses, one-step linear equations, and geometric/word setups.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Concept of equation balance LHS equals RHS
def arch_01_equation_balance_concept(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 8)
    b = rng.randint(4, 9)
    total = a + b
    ans = "True"
    prompt = (
        f"An equation is a mathematical statement that two expressions are equal in value.\n\n"
        f"Determine whether the statement \\({a} + {b} = {total}\\) is a true equation or a false equation."
    )
    sol = (
        f"**Step 1:** Calculate the Left-Hand Side (LHS):\n"
        f"$$\\text{{LHS}} = {a} + {b} = {total}$$\n\n"
        f"**Step 2:** Compare with the Right-Hand Side (RHS):\n"
        f"$$\\text{{RHS}} = {total}$$\n\n"
        f"Since \\(\\text{{LHS}} = \\text{{RHS}}\\), the equation is **{ans}**."
    )
    return {
        "id": f"g7_eq1_01_{rng.randint(100000, 999999)}",
        "subskill": "01_equation_balance_concept",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["True", "False"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_01",
        "hints": {"tier_1": f"Add {a} + {b}.", "tier_2": f"{a} + {b} = {total}.", "tier_3": ans},
        "misconception_tags": ["misunderstanding_the_equals_sign_as_an_operator"]
    }


# 02. Expression vs equation distinction
def arch_02_expression_vs_equation_distinction(rng: random.Random) -> Dict[str, Any]:
    ans = "Equation"
    prompt = (
        "Classify the following mathematical statement as either an **Expression** or an **Equation**:\n\n"
        "\\[ 3x + 7 = 22 \\]"
    )
    sol = (
        "**Definition:**\n"
        "- An **expression** represents a quantity and does not contain an equals sign (e.g. \\(3x + 7\\)).\n"
        "- An **equation** asserts that two expressions are equal using an equals sign \\(=\\).\n\n"
        "Because \\(3x + 7 = 22\\) contains an equals sign relating two expressions, it is an **Equation**."
    )
    return {
        "id": f"g7_eq1_02_{rng.randint(100000, 999999)}",
        "subskill": "02_expression_vs_equation_distinction",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["Expression", "Equation", "Inequality", "Formula"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_02",
        "hints": {"tier_1": "Does it have an equals sign '='?", "tier_2": "Statements with '=' are equations.", "tier_3": ans},
        "misconception_tags": ["confusing_expression_with_equation"]
    }


# 03. Solve one-step addition equation by inspection
def arch_03_solve_addition_equation_inspection(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(4, 15)
    a = rng.randint(3, 12)
    b = x_val + a
    ans = str(x_val)
    prompt = (
        f"Solve the equation by inspection (mental math):\n"
        f"\\[ x + {a} = {b} \\]"
    )
    sol = (
        f"**Step 1:** Ask: *What number added to {a} gives {b}?*\n"
        f"$$x = {b} - {a}$$\n\n"
        f"**Step 2:** Calculate: \\({b} - {a} = {x_val}\\).\n\n"
        f"Solution: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g7_eq1_03_{rng.randint(100000, 999999)}",
        "subskill": "03_solve_addition_equation_inspection",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_03",
        "hints": {"tier_1": f"Subtract {a} from {b}.", "tier_2": f"{b} - {a} = {x_val}.", "tier_3": ans},
        "misconception_tags": ["adding_instead_of_subtracting_constant"]
    }


# 04. Solve one-step addition equation with variable on RHS
def arch_04_solve_addition_equation_rhs_variable(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(5, 18)
    k = rng.randint(4, 14)
    tot = x_val + k
    ans = str(x_val)
    prompt = (
        f"Solve the equation for \\(x\\):\n"
        f"\\[ {tot} = {k} + x \\]"
    )
    sol = (
        f"**Step 1:** Rearrange mentally to isolate \\(x\\):\n"
        f"$$x = {tot} - {k}$$\n\n"
        f"**Step 2:** Calculate: \\({tot} - {k} = {x_val}\\).\n\n"
        f"Solution: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g7_eq1_04_{rng.randint(100000, 999999)}",
        "subskill": "04_solve_addition_equation_rhs_variable",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_04",
        "hints": {"tier_1": f"Subtract {k} from {tot}.", "tier_2": f"{tot} - {k} = {x_val}.", "tier_3": ans},
        "misconception_tags": ["confused_by_variable_on_rhs"]
    }


# 05. Solve one-step subtraction equation x minus a equals b
def arch_05_solve_subtraction_equation_inspection(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.randint(12, 28)
    a = rng.randint(3, 10)
    b = x_val - a
    ans = str(x_val)
    prompt = (
        f"Solve for \\(x\\) by inspection:\n"
        f"\\[ x - {a} = {b} \\]"
    )
    sol = (
        f"**Step 1:** The inverse operation of subtracting {a} is adding {a}:\n"
        f"$$x = {b} + {a}$$\n\n"
        f"**Step 2:** Calculate: \\({b} + {a} = {x_val}\\).\n\n"
        f"Solution: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g7_eq1_05_{rng.randint(100000, 999999)}",
        "subskill": "05_solve_subtraction_equation_inspection",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_05",
        "hints": {"tier_1": f"Add {a} to {b}.", "tier_2": f"{b} + {a} = {x_val}.", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_in_subtraction_equation"]
    }


# 06. Solve one-step subtraction equation with variable as subtrahend
def arch_06_solve_subtraction_variable_subtrahend(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(15, 30)
    x_val = rng.randint(4, 12)
    b = a - x_val
    ans = str(x_val)
    prompt = (
        f"Solve the equation for \\(x\\):\n"
        f"\\[ {a} - x = {b} \\]"
    )
    sol = (
        f"**Step 1:** Ask: *What number subtracted from {a} leaves {b}?*\n"
        f"$$x = {a} - {b}$$\n\n"
        f"**Step 2:** Calculate: \\({a} - {b} = {x_val}\\).\n\n"
        f"Solution: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g7_eq1_06_{rng.randint(100000, 999999)}",
        "subskill": "06_solve_subtraction_variable_subtrahend",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_06",
        "hints": {"tier_1": f"Subtract {b} from {a}.", "tier_2": f"{a} - {b} = {x_val}.", "tier_3": ans},
        "misconception_tags": ["adding_minuend_to_difference"]
    }


# 07. Solve one-step multiplication equation ax equals b
def arch_07_solve_multiplication_equation_inspection(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5, 6, 7, 8, 9])
    x_val = rng.randint(3, 12)
    b = a * x_val
    ans = str(x_val)
    prompt = (
        f"Solve the equation by inspection:\n"
        f"\\[ {a}x = {b} \\]"
    )
    sol = (
        f"**Step 1:** The inverse of multiplying by {a} is dividing by {a}:\n"
        f"$$x = \\frac{{{b}}}{{{a}}}$$\n\n"
        f"**Step 2:** Calculate: \\({b} \\div {a} = {x_val}\\).\n\n"
        f"Solution: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g7_eq1_07_{rng.randint(100000, 999999)}",
        "subskill": "07_solve_multiplication_equation_inspection",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_07",
        "hints": {"tier_1": f"Divide {b} by {a}.", "tier_2": f"{b} / {a} = {x_val}.", "tier_3": ans},
        "misconception_tags": ["subtracting_coefficient_instead_of_dividing"]
    }


# 08. Solve one-step division equation x over a equals b
def arch_08_solve_division_equation_inspection(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5, 6])
    b = rng.randint(3, 12)
    x_val = a * b
    ans = str(x_val)
    prompt = (
        f"Solve the division equation for \\(x\\):\n"
        f"\\[ \\frac{{x}}{{{a}}} = {b} \\]"
    )
    sol = (
        f"**Step 1:** The inverse of dividing by {a} is multiplying by {a}:\n"
        f"$$x = {b} \\times {a}$$\n\n"
        f"**Step 2:** Calculate: \\({b} \\times {a} = {x_val}\\).\n\n"
        f"Solution: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g7_eq1_08_{rng.randint(100000, 999999)}",
        "subskill": "08_solve_division_equation_inspection",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_08",
        "hints": {"tier_1": f"Multiply {b} by {a}.", "tier_2": f"{b} × {a} = {x_val}.", "tier_3": ans},
        "misconception_tags": ["dividing_instead_of_multiplying_in_division_equation"]
    }


# 09. Solve one-step division equation with variable in denominator
def arch_09_solve_division_variable_in_denominator(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.choice([2, 3, 4, 5, 6])
    b = rng.randint(3, 9)
    a = x_val * b
    ans = str(x_val)
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\frac{{{a}}}{{x}} = {b} \\]"
    )
    sol = (
        f"**Step 1:** Ask: *{a} divided by what number gives {b}?*\n"
        f"$$x = \\frac{{{a}}}{{{b}}}$$\n\n"
        f"**Step 2:** Calculate: \\({a} \\div {b} = {x_val}\\).\n\n"
        f"Solution: **\\(x = {ans}\\)**."
    )
    return {
        "id": f"g7_eq1_09_{rng.randint(100000, 999999)}",
        "subskill": "09_solve_division_variable_in_denominator",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_09",
        "hints": {"tier_1": f"Divide {a} by {b}.", "tier_2": f"{a} / {b} = {x_val}.", "tier_3": ans},
        "misconception_tags": ["multiplying_numerator_by_quotient"]
    }


# 10. Check solution by substitution LHS vs RHS
def arch_10_check_solution_by_substitution(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(3, 6)
    k = rng.randint(2, 7)
    x_test = rng.choice([3, 4, 5])
    actual_lhs = c * x_test + k
    ans = "Yes"
    prompt = (
        f"Consider the equation \\({c}x + {k} = {actual_lhs}\\).\n\n"
        f"Check whether \\(x = {x_test}\\) is the correct solution by substituting it into the Left-Hand Side (LHS).\n"
        f"Is \\(x = {x_test}\\) a solution? (Yes / No)"
    )
    sol = (
        f"**Step 1:** Substitute \\(x = {x_test}\\) into \\(\\text{{LHS}} = {c}x + {k}\\):\n"
        f"$$\\text{{LHS}} = {c}({x_test}) + {k} = {c * x_test} + {k} = {actual_lhs}$$\n\n"
        f"**Step 2:** Compare LHS to RHS:\n"
        f"$$\\text{{RHS}} = {actual_lhs}$$\n\n"
        f"Since \\(\\text{{LHS}} = \\text{{RHS}}\\), the value \\(x = {x_test}\\) **is** the solution (**{ans}**)."
    )
    return {
        "id": f"g7_eq1_10_{rng.randint(100000, 999999)}",
        "subskill": "10_check_solution_by_substitution",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["Yes", "No"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_10",
        "hints": {"tier_1": f"Calculate {c}({x_test}) + {k}.", "tier_2": f"{c * x_test} + {k} = {actual_lhs}.", "tier_3": ans},
        "misconception_tags": ["arithmetic_order_of_operations_in_substitution_check"]
    }


# 11. Additive inverse property in equations
def arch_11_additive_inverse_property(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(5, 15)
    ans = f"-{a}"
    prompt = (
        f"To isolate \\(x\\) in the equation \\(x + {a} = 25\\), what number must be added to both sides "
        f"as the additive inverse of \\({a}\\)?"
    )
    sol = (
        f"**Step 1:** The additive inverse of any number \\(k\\) is \\(-k\\), because \\(k + (-k) = 0\\).\n\n"
        f"**Step 2:** For \\({a}\\), the additive inverse is **\\({ans}\\)**."
    )
    return {
        "id": f"g7_eq1_11_{rng.randint(100000, 999999)}",
        "subskill": "11_additive_inverse_property",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_11",
        "hints": {"tier_1": f"What number added to {a} equals 0?", "tier_2": f"The negative of {a}.", "tier_3": ans},
        "misconception_tags": ["confusing_additive_inverse_with_multiplicative_inverse"]
    }


# 12. Multiplicative inverse property in equations
def arch_12_multiplicative_inverse_property(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([3, 4, 5, 7, 8])
    ans = f"1/{c}"
    prompt = (
        f"In the equation \\({c}x = 28\\), what is the multiplicative inverse (reciprocal) of \\({c}\\) "
        f"that can be used to isolate \\(x\\)?"
    )
    sol = (
        f"**Step 1:** The multiplicative inverse of a non-zero number \\(a\\) is \\(\\frac{{1}}{{a}}\\), because \\(a \\times \\frac{{1}}{{a}} = 1\\).\n\n"
        f"**Step 2:** Therefore, for \\({c}\\), the multiplicative inverse is **\\({ans}\\)** (or dividing by \\({c}\\))."
    )
    return {
        "id": f"g7_eq1_12_{rng.randint(100000, 999999)}",
        "subskill": "12_multiplicative_inverse_property",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_12",
        "hints": {"tier_1": f"The reciprocal of {c}.", "tier_2": f"1/{c}.", "tier_3": ans},
        "misconception_tags": ["confusing_reciprocal_with_opposite_sign"]
    }


# 13. Two-step linear equation ax + b = c by backtracking
def arch_13_two_step_addition_equation_backtracking(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    x_val = rng.randint(3, 9)
    b = rng.randint(3, 10)
    c = a * x_val + b
    ans = str(x_val)
    prompt = (
        f"Solve the two-step equation for \\(x\\) by backtracking (inverse operations):\n"
        f"\\[ {a}x + {b} = {c} \\]"
    )
    sol = (
        f"**Step 1:** Subtract {b} from both sides:\n"
        f"$${a}x = {c} - {b} = {c - b}$$\n\n"
        f"**Step 2:** Divide both sides by {a}:\n"
        f"$$x = \\frac{{{c - b}}}{{{a}}} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq1_13_{rng.randint(100000, 999999)}",
        "subskill": "13_two_step_addition_equation_backtracking",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_13",
        "hints": {"tier_1": f"First subtract {b} from {c}.", "tier_2": f"Then divide by {a}.", "tier_3": ans},
        "misconception_tags": ["dividing_before_subtracting_constant"]
    }


# 14. Two-step linear equation ax - b = c by backtracking
def arch_14_two_step_subtraction_equation_backtracking(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    x_val = rng.randint(3, 9)
    b = rng.randint(2, 8)
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
        "id": f"g7_eq1_14_{rng.randint(100000, 999999)}",
        "subskill": "14_two_step_subtraction_equation_backtracking",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_14",
        "hints": {"tier_1": f"First add {b} to {c}.", "tier_2": f"Then divide by {a}.", "tier_3": ans},
        "misconception_tags": ["subtracting_instead_of_adding_constant_in_two_step"]
    }


# 15. Translate number sentence sum to equation
def arch_15_translate_sum_sentence_to_equation(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(5, 15)
    tot = rng.randint(20, 40)
    ans = f"x + {k} = {tot}"
    prompt = (
        f"Translate the following verbal statement into an algebraic equation using \\(x\\) for the unknown:\n\n"
        f"\"A certain number increased by {k} is equal to {tot}.\""
    )
    sol = (
        f"**Step 1:** Identify parts:\n"
        f"- 'A certain number' \\(\\to x\\)\n"
        "- 'increased by' \\(\\to +\\)\n"
        f"- '{k}' \\(\\to {k}\\)\n"
        f"- 'is equal to {tot}' \\(\\to = {tot}\\)\n\n"
        f"Equation: **\\({ans}\\)**."
    )
    return {
        "id": f"g7_eq1_15_{rng.randint(100000, 999999)}",
        "subskill": "15_translate_sum_sentence_to_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_15",
        "hints": {"tier_1": "Increased by means addition.", "tier_2": f"x + {k} = {tot}.", "tier_3": ans},
        "misconception_tags": ["confusing_increased_by_with_multiplication"]
    }


# 16. Translate number sentence difference to equation
def arch_16_translate_difference_sentence_to_equation(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(4, 12)
    res = rng.randint(10, 25)
    ans = f"x - {k} = {res}"
    prompt = (
        f"Write an algebraic equation for the sentence:\n\n"
        f"\"{k} subtracted from a number yields {res}.\""
    )
    sol = (
        f"**Step 1:** '{k} subtracted from a number \\(x\\)' means \\(x - {k}\\).\n"
        f"**Step 2:** 'yields {res}' means \\(= {res}\\).\n\n"
        f"Equation: **\\({ans}\\)**."
    )
    return {
        "id": f"g7_eq1_16_{rng.randint(100000, 999999)}",
        "subskill": "16_translate_difference_sentence_to_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_16",
        "hints": {"tier_1": f"k subtracted from x is x - {k}.", "tier_2": f"x - {k} = {res}.", "tier_3": ans},
        "misconception_tags": ["reversing_subtraction_order_in_translation"]
    }


# 17. Translate number sentence product to equation
def arch_17_translate_product_sentence_to_equation(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5, 6, 7])
    tot = rng.randint(20, 50)
    ans = f"{m}x = {tot}"
    prompt = (
        f"Write an algebraic equation for the statement:\n\n"
        f"\"The product of {m} and a number is {tot}.\""
    )
    sol = (
        f"**Step 1:** 'Product' means multiplication: \\({m} \\times x = {m}x\\).\n"
        f"**Step 2:** 'is {tot}' means \\(= {tot}\\).\n\n"
        f"Equation: **\\({ans}\\)**."
    )
    return {
        "id": f"g7_eq1_17_{rng.randint(100000, 999999)}",
        "subskill": "17_translate_product_sentence_to_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_17",
        "hints": {"tier_1": "Product means multiply.", "tier_2": f"{m}x = {tot}.", "tier_3": ans},
        "misconception_tags": ["writing_product_as_addition"]
    }


# 18. Geometry perimeter square equation
def arch_18_geometry_perimeter_square_equation(rng: random.Random) -> Dict[str, Any]:
    s = rng.randint(4, 12)
    p = 4 * s
    ans = str(s)
    prompt = (
        f"The perimeter of a square is \\({p}\\text{{ cm}}\\).\n"
        f"If the side length is \\(s\\), write the equation \\(4s = {p}\\) and solve for \\(s\\)."
    )
    sol = (
        f"**Step 1:** Set up equation: \\(4s = {p}\\).\n\n"
        f"**Step 2:** Divide both sides by 4:\n"
        f"$$s = \\frac{{{p}}}{{4}} = \\mathbf{{{ans}}}\\text{{ cm}}$$"
    )
    return {
        "id": f"g7_eq1_18_{rng.randint(100000, 999999)}",
        "subskill": "18_geometry_perimeter_square_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_18",
        "hints": {"tier_1": f"Perimeter = 4s. Divide {p} by 4.", "tier_2": f"{p} / 4 = {s}.", "tier_3": ans},
        "misconception_tags": ["dividing_perimeter_by_two_instead_of_four"]
    }


# 19. Geometry angles on straight line equation
def arch_19_geometry_angles_straight_line_equation(rng: random.Random) -> Dict[str, Any]:
    ang = rng.choice([35, 45, 55, 65, 75, 110, 120, 135])
    x_val = 180 - ang
    ans = str(x_val)
    prompt = (
        f"Two adjacent angles on a straight line are \\(x\\) and \\({ang}^\\circ\\).\n\n"
        f"1. Write an equation using the property that angles on a straight line add up to \\(180^\\circ\\).\n"
        f"2. Solve for \\(x\\)."
    )
    sol = (
        f"**Step 1:** Set up the equation:\n"
        f"$$x + {ang}^\\circ = 180^\\circ$$\n\n"
        f"**Step 2:** Subtract {ang} from 180:\n"
        f"$$x = 180 - {ang} = \\mathbf{{{ans}}}^\\circ$$"
    )
    return {
        "id": f"g7_eq1_19_{rng.randint(100000, 999999)}",
        "subskill": "19_geometry_angles_straight_line_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_19",
        "hints": {"tier_1": "Angles on a straight line add up to 180°.", "tier_2": f"180 - {ang} = {x_val}.", "tier_3": ans},
        "misconception_tags": ["using_90_or_360_for_straight_line_angles"]
    }


# 20. Geometry angles in a triangle equation
def arch_20_geometry_angles_in_triangle_equation(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([50, 55, 60, 65, 70])
    b = rng.choice([40, 45, 50, 55])
    tot_given = a + b
    x_val = 180 - tot_given
    ans = str(x_val)
    prompt = (
        f"In triangle \\(ABC\\), angle \\(A = {a}^\\circ\\) and angle \\(B = {b}^\\circ\\).\n\n"
        f"Set up an equation and solve for the third angle \\(x = \\angle C\\)."
    )
    sol = (
        f"**Step 1:** The interior angles of a triangle add up to \\(180^\\circ\\):\n"
        f"$$x + {a} + {b} = 180$$\n"
        f"$$x + {tot_given} = 180$$\n\n"
        f"**Step 2:** Solve for \\(x\\):\n"
        f"$$x = 180 - {tot_given} = \\mathbf{{{ans}}}^\\circ$$"
    )
    return {
        "id": f"g7_eq1_20_{rng.randint(100000, 999999)}",
        "subskill": "20_geometry_angles_in_triangle_equation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_20",
        "hints": {"tier_1": "Angles in a triangle sum to 180°.", "tier_2": f"180 - ({a} + {b}) = {x_val}.", "tier_3": ans},
        "misconception_tags": ["triangle_angle_sum_arithmetic_error"]
    }


# 21. Table of substitution trial and error
def arch_21_table_trial_and_error_root_finding(rng: random.Random) -> Dict[str, Any]:
    m = 3
    c = 4
    x_root = 4
    rhs = m * x_root + c  # 16
    ans = str(x_root)
    prompt = (
        f"Given the equation \\({m}x + {c} = {rhs}\\), complete the table mentally to find the correct root \\(x\\):\n\n"
        f"| \\(x\\) | \\({m}x + {c}\\) | True or False? |\n"
        f"| :--- | :--- | :--- |\n"
        f"| 2 | {m*2 + c} | False |\n"
        f"| 3 | {m*3 + c} | False |\n"
        f"| 4 | ? | ? |\n"
        f"| 5 | {m*5 + c} | False |\n\n"
        f"Which value of \\(x\\) makes the equation true?"
    )
    sol = (
        f"**Step 1:** Test \\(x = 4\\):\n"
        f"$$\\text{{LHS}} = {m}(4) + {c} = {m*4} + {c} = {rhs}$$\n\n"
        f"**Step 2:** Since LHS equals RHS ({rhs}), the equation is True when \\(x = \\mathbf{{{ans}}}\\)."
    )
    return {
        "id": f"g7_eq1_21_{rng.randint(100000, 999999)}",
        "subskill": "21_table_trial_and_error_root_finding",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_21",
        "hints": {"tier_1": f"Calculate {m}(4) + {c}.", "tier_2": f"{m*4} + {c} = {rhs}.", "tier_3": ans},
        "misconception_tags": ["table_substitution_arithmetic_error"]
    }


# 22. Multiple choice root selection from set
def arch_22_multiple_choice_root_selection(rng: random.Random) -> Dict[str, Any]:
    ans = "6"
    prompt = (
        "Which value from the set \\(\\{3, 4, 6, 8\\}\\) is the solution to the equation:\n"
        "\\[ 2x + 5 = 17 \\]"
    )
    sol = (
        "**Test each value:**\n"
        "- If \\(x = 3\\): \\(2(3) + 5 = 11 \\neq 17\\)\n"
        "- If \\(x = 4\\): \\(2(4) + 5 = 13 \\neq 17\\)\n"
        "- If \\(x = 6\\): \\(2(6) + 5 = 12 + 5 = 17\\) (Correct!)\n"
        "- If \\(x = 8\\): \\(2(8) + 5 = 21 \\neq 17\\)\n\n"
        "Solution: **\\(x = 6\\)**."
    )
    return {
        "id": f"g7_eq1_22_{rng.randint(100000, 999999)}",
        "subskill": "22_multiple_choice_root_selection",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": ["3", "4", "6", "8"],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_eq1_22",
        "hints": {"tier_1": "Substitute each choice into 2x + 5.", "tier_2": "2(6) + 5 = 17.", "tier_3": ans},
        "misconception_tags": ["guessing_roots_without_substitution_check"]
    }


# 23. Identify inverse operation required
def arch_23_identify_inverse_operation_required(rng: random.Random) -> Dict[str, Any]:
    ans = "Subtract 14 from both sides"
    prompt = (
        "What is the first inverse operation you should perform to solve the equation:\n"
        "\\[ x + 14 = 35 \\]"
    )
    sol = (
        "**Reasoning:**\n"
        "The variable \\(x\\) has 14 added to it.\n"
        "The inverse operation of addition is subtraction.\n"
        "Therefore, you must **Subtract 14 from both sides**."
    )
    return {
        "id": f"g7_eq1_23_{rng.randint(100000, 999999)}",
        "subskill": "23_identify_inverse_operation_required",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": [
            "Subtract 14 from both sides",
            "Add 14 to both sides",
            "Multiply both sides by 14",
            "Divide both sides by 14"
        ],
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_23",
        "hints": {"tier_1": "Inverse of +14.", "tier_2": "Subtract 14.", "tier_3": ans},
        "misconception_tags": ["confusing_addition_inverse_with_multiplication"]
    }


# 24. Equations with zero: addition and subtraction
def arch_24_equations_with_zero_properties(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(7, 25)
    ans = str(k)
    prompt = (
        f"Solve the equation for \\(x\\):\n"
        f"\\[ x + 0 = {k} \\]"
    )
    sol = (
        f"**Step 1:** By the identity property of addition, adding 0 to any number leaves it unchanged:\n"
        f"$$x + 0 = x$$\n\n"
        f"**Step 2:** Therefore: \\(x = \\mathbf{{{ans}}}\\)."
    )
    return {
        "id": f"g7_eq1_24_{rng.randint(100000, 999999)}",
        "subskill": "24_equations_with_zero_properties",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_24",
        "hints": {"tier_1": "Adding 0 does not change a number.", "tier_2": f"x = {k}.", "tier_3": ans},
        "misconception_tags": ["treating_zero_addition_as_multiplication"]
    }


# 25. Equations with zero: subtraction to zero
def arch_25_equations_subtraction_resulting_in_zero(rng: random.Random) -> Dict[str, Any]:
    k = rng.randint(8, 30)
    ans = str(k)
    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ x - {k} = 0 \\]"
    )
    sol = (
        f"**Step 1:** Add {k} to both sides:\n"
        f"$$x = 0 + {k} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_eq1_25_{rng.randint(100000, 999999)}",
        "subskill": "25_equations_subtraction_resulting_in_zero",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_eq1_25",
        "hints": {"tier_1": f"Add {k} to 0.", "tier_2": f"x = {k}.", "tier_3": ans},
        "misconception_tags": ["thinking_solution_must_be_zero"]
    }
