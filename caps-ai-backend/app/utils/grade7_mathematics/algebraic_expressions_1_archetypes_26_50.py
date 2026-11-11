"""Grade 7 Mathematics - Algebraic Expressions 1: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/04. Algebraic expressions 1.md
Focus: Brackets, powers, consecutive numbers, word problems, geometric modeling, expression anatomy, and diagnostic autopsies.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Evaluate expression with brackets substitution
def arch_26_evaluate_expression_with_brackets_substitution(rng: random.Random) -> Dict[str, Any]:
    # 4(x + 3) when x = 5 -> 4(8) = 32
    ans = "32"
    prompt = (
        "Evaluate the expression \\(4(x + 3)\\) when \\(x = 5\\)."
    )
    sol = (
        "**Step 1:** Evaluate inside brackets first:\n"
        "$$x + 3 = 5 + 3 = 8$$\n\n"
        "**Step 2:** Multiply by 4:\n"
        "$$4(8) = \\mathbf{32}$$"
    )
    return {
        "id": f"g7_alg1_26_{rng.randint(100000, 999999)}",
        "subskill": "26_evaluate_expression_with_brackets_substitution",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_26",
        "hints": {"tier_1": "Calculate 5 + 3 first.", "tier_2": "4 * 8 = 32.", "tier_3": ans},
        "misconception_tags": ["brackets_order_of_operations_error"]
    }


# 27. Evaluate quadratic term x squared substitution
def arch_27_evaluate_quadratic_term_x_squared_substitution(rng: random.Random) -> Dict[str, Any]:
    # 2x^2 + 3 when x = 4 -> 2(16) + 3 = 35
    ans = "35"
    prompt = (
        "Calculate the value of \\(2x^2 + 3\\) when \\(x = 4\\)."
    )
    sol = (
        "**Step 1:** Apply exponent first (BODMAS):\n"
        "$$4^2 = 16$$\n\n"
        "**Step 2:** Multiply by 2:\n"
        "$$2 \\times 16 = 32$$\n\n"
        "**Step 3:** Add 3:\n"
        "$$32 + 3 = \\mathbf{35}$$"
    )
    return {
        "id": f"g7_alg1_27_{rng.randint(100000, 999999)}",
        "subskill": "27_evaluate_quadratic_term_x_squared_substitution",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_27",
        "hints": {"tier_1": "Square 4 first to get 16.", "tier_2": "2(16) + 3 = 35.", "tier_3": ans},
        "misconception_tags": ["multiplying_before_squaring_in_substitution"]
    }


# 28. Evaluate cubic term x cubed substitution
def arch_28_evaluate_cubic_term_x_cubed_substitution(rng: random.Random) -> Dict[str, Any]:
    # x^3 - 5 when x = 3 -> 27 - 5 = 22
    ans = "22"
    prompt = (
        "Evaluate the expression \\(x^3 - 5\\) when \\(x = 3\\)."
    )
    sol = (
        "**Step 1:** Cube 3:\n"
        "$$3^3 = 3 \\times 3 \\times 3 = 27$$\n\n"
        "**Step 2:** Subtract 5:\n"
        "$$27 - 5 = \\mathbf{22}$$"
    )
    return {
        "id": f"g7_alg1_28_{rng.randint(100000, 999999)}",
        "subskill": "28_evaluate_cubic_term_x_cubed_substitution",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_28",
        "hints": {"tier_1": "3 * 3 * 3 = 27.", "tier_2": "27 - 5 = 22.", "tier_3": ans},
        "misconception_tags": ["cubing_evaluated_as_multiplying_by_3"]
    }


# 29. Evaluate two variable expression substitution
def arch_29_evaluate_two_variable_expression_substitution(rng: random.Random) -> Dict[str, Any]:
    # 3a + 2b when a = 4, b = 7 -> 3(4) + 2(7) = 12 + 14 = 26
    ans = "26"
    prompt = (
        "Calculate the value of \\(3a + 2b\\) given \\(a = 4\\) and \\(b = 7\\)."
    )
    sol = (
        "**Step 1:** Substitute both variables:\n"
        "$$3(4) + 2(7) = 12 + 14 = \\mathbf{26}$$"
    )
    return {
        "id": f"g7_alg1_29_{rng.randint(100000, 999999)}",
        "subskill": "29_evaluate_two_variable_expression_substitution",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_29",
        "hints": {"tier_1": "3(4) = 12 and 2(7) = 14.", "tier_2": "12 + 14 = 26.", "tier_3": ans},
        "misconception_tags": ["two_variable_substitution_slip"]
    }


# 30. Translate consecutive numbers algebraic expression
def arch_30_translate_consecutive_numbers_algebraic_expression(rng: random.Random) -> Dict[str, Any]:
    ans = "n and n + 1"
    prompt = (
        "If \\(n\\) represents any integer, write an algebraic expression for the **next consecutive integer**."
    )
    sol = (
        "**Step 1:** Consecutive integers increase by 1:\n"
        "Next integer = **\\(n + 1\\)**"
    )
    return {
        "id": f"g7_alg1_30_{rng.randint(100000, 999999)}",
        "subskill": "30_translate_consecutive_numbers_algebraic_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": "n + 1",
        "sample_answer": "n + 1",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_30",
        "hints": {"tier_1": "Consecutive numbers differ by 1.", "tier_2": "n + 1.", "tier_3": "n + 1"},
        "misconception_tags": ["consecutive_number_algebraic_expression_error"]
    }


# 31. Translate even and odd numbers algebraic representation
def arch_31_translate_even_and_odd_numbers_algebraic_representation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "For any integer \\(k\\):\n"
        "1. How can any **even number** be expressed algebraically?\n"
        "2. How can any **odd number** be expressed algebraically?"
    )
    sol = (
        "**1. Even Number:** Any integer multiplied by 2 is guaranteed to be even: **\\(2k\\)**.\n\n"
        "**2. Odd Number:** Any even number plus 1 (or minus 1) is odd: **\\(2k + 1\\)** (or \\(2k - 1\\)).\n\n"
        "**Summary:** 1. \\(2k\\); 2. \\(2k + 1\\)"
    )
    ans = "1. 2k; 2. 2k + 1"
    return {
        "id": f"g7_alg1_31_{rng.randint(100000, 999999)}",
        "subskill": "31_translate_even_and_odd_numbers_algebraic_representation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_31",
        "hints": {"tier_1": "Even numbers are multiples of 2.", "tier_2": "2k and 2k + 1.", "tier_3": ans},
        "misconception_tags": ["even_odd_algebraic_notation_confusion"]
    }


# 32. Translate age word problem to expression
def arch_32_translate_age_word_problem_to_expression(rng: random.Random) -> Dict[str, Any]:
    # Sipho is x years old. His father is 4 years older than three times Sipho's age -> 3x + 4
    ans = "3x + 4"
    prompt = (
        "Sipho is \\(x\\) years old. His father is 4 years older than three times Sipho's age.\n\n"
        "Write an algebraic expression for the father's age."
    )
    sol = (
        "**Step 1:** Three times Sipho's age: \\(3x\\)\n\n"
        "**Step 2:** 4 years older: \\(\\mathbf{3x + 4}\\)"
    )
    return {
        "id": f"g7_alg1_32_{rng.randint(100000, 999999)}",
        "subskill": "32_translate_age_word_problem_to_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_32",
        "hints": {"tier_1": "3 times x, plus 4.", "tier_2": "3x + 4.", "tier_3": ans},
        "misconception_tags": ["age_word_problem_translation_slip"]
    }


# 33. Translate money rand cents to expression
def arch_33_translate_money_rand_cents_to_expression(rng: random.Random) -> Dict[str, Any]:
    # r Rand and c cents. Total cents = 100r + c
    ans = "100r + c"
    prompt = (
        "A wallet contains \\(r\\) Rand and \\(c\\) cents.\n\n"
        "Write an expression for the total amount of money in **cents**."
    )
    sol = (
        "**Step 1:** Since R1 = 100 cents, \\(r\\) Rand is equal to \\(100r\\) cents.\n\n"
        "**Step 2:** Add the remaining \\(c\\) cents:\n"
        "$$\\text{Total cents} = \\mathbf{100r + c}$$"
    )
    return {
        "id": f"g7_alg1_33_{rng.randint(100000, 999999)}",
        "subskill": "33_translate_money_rand_cents_to_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_33",
        "hints": {"tier_1": "How many cents in 1 Rand?", "tier_2": "100r + c.", "tier_3": ans},
        "misconception_tags": ["currency_conversion_in_algebraic_expression"]
    }


# 34. Translate geometric perimeter square to expression
def arch_34_translate_geometric_perimeter_square_to_expression(rng: random.Random) -> Dict[str, Any]:
    ans = "4s"
    prompt = (
        "Write an algebraic expression for the perimeter \\(P\\) of a square with side length \\(s\\)."
    )
    sol = (
        "**Step 1:** A square has 4 equal sides:\n"
        "$$P = s + s + s + s = \\mathbf{4s}$$"
    )
    return {
        "id": f"g7_alg1_34_{rng.randint(100000, 999999)}",
        "subskill": "34_translate_geometric_perimeter_square_to_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_34",
        "hints": {"tier_1": "Add all 4 sides.", "tier_2": "4s.", "tier_3": ans},
        "misconception_tags": ["perimeter_vs_area_formula_confusion"]
    }


# 35. Translate geometric perimeter triangle to expression
def arch_35_translate_geometric_perimeter_triangle_to_expression(rng: random.Random) -> Dict[str, Any]:
    # Triangle sides: a, a+2, a+5 -> P = a + a+2 + a+5 = 3a + 7
    ans = "3a + 7"
    prompt = (
        "A triangle has side lengths \\(a\\), \\(a + 2\\), and \\(a + 5\\).\n\n"
        "Write a simplified algebraic expression for its perimeter."
    )
    sol = (
        "**Step 1:** Add the lengths of all three sides:\n"
        "$$P = a + (a + 2) + (a + 5)$$\n\n"
        "**Step 2:** Combine like terms:\n"
        "$$P = (a + a + a) + (2 + 5) = \\mathbf{3a + 7}$$"
    )
    return {
        "id": f"g7_alg1_35_{rng.randint(100000, 999999)}",
        "subskill": "35_translate_geometric_perimeter_triangle_to_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_35",
        "hints": {"tier_1": "Add the 3 sides together.", "tier_2": "3a + 7.", "tier_3": ans},
        "misconception_tags": ["combining_unlike_terms_in_perimeter"]
    }


# 36. Translate geometric area rectangle to expression
def arch_36_translate_geometric_area_rectangle_to_expression(rng: random.Random) -> Dict[str, Any]:
    # Length x+4, width 3 -> Area = 3(x + 4) = 3x + 12
    ans = "3(x + 4)"
    prompt = (
        "A rectangle has width 3 cm and length \\((x + 4)\\) cm.\n\n"
        "Write an expression for the area of the rectangle."
    )
    sol = (
        "**Step 1:** \\(\\text{Area} = \\text{width} \\times \\text{length}\\)\n\n"
        "**Step 2:**\n"
        "$$\\text{Area} = \\mathbf{3(x + 4)} \\quad (\\text{or } 3x + 12)$$"
    )
    return {
        "id": f"g7_alg1_36_{rng.randint(100000, 999999)}",
        "subskill": "36_translate_geometric_area_rectangle_to_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_36",
        "hints": {"tier_1": "Multiply width by length.", "tier_2": "3(x + 4).", "tier_3": ans},
        "misconception_tags": ["rectangle_area_formula_slip"]
    }


# 37. Identify like vs unlike terms concept
def arch_37_identify_like_vs_unlike_terms_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain what makes two algebraic terms **like terms**.\n\n"
        "Are \\(5x\\) and \\(5x^2\\) like terms? Justify your answer."
    )
    sol = (
        "**Definition:** Like terms have the **exact same variables raised to the exact same powers (exponents)**.\n\n"
        "**Critique:** \\(5x\\) and \\(5x^2\\) are **unlike terms** because \\(x\\) has power 1 while \\(x^2\\) has power 2. "
        "They cannot be combined into a single term."
    )
    ans = "No, because the exponents are different"
    return {
        "id": f"g7_alg1_37_{rng.randint(100000, 999999)}",
        "subskill": "37_identify_like_vs_unlike_terms_concept",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_37",
        "hints": {"tier_1": "Check the powers of x.", "tier_2": "Power 1 vs power 2 = unlike.", "tier_3": ans},
        "misconception_tags": ["treating_different_powers_as_like_terms"]
    }


# 38. Identify coefficient in fractional algebraic term
def arch_38_identify_coefficient_in_fractional_algebraic_term(rng: random.Random) -> Dict[str, Any]:
    # Term: x/4 -> coefficient is 1/4
    ans = "1/4"
    prompt = (
        "What is the numerical coefficient of \\(x\\) in the algebraic term \\(\\frac{x}{4}\\)?"
    )
    sol = (
        "**Step 1:** Rewrite \\(\\frac{x}{4}\\) with an explicit multiplier:\n"
        "$$\\frac{x}{4} = \\frac{1}{4}x$$\n\n"
        "**Answer:** **\\(\\frac{1}{4}\\)** (not 4!)."
    )
    return {
        "id": f"g7_alg1_38_{rng.randint(100000, 999999)}",
        "subskill": "38_identify_coefficient_in_fractional_algebraic_term",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_38",
        "hints": {"tier_1": "x/4 is the same as (1/4) * x.", "tier_2": "Coefficient is 1/4.", "tier_3": ans},
        "misconception_tags": ["reporting_denominator_alone_as_coefficient"]
    }


# 39. Identify degree of linear expression
def arch_39_identify_degree_of_linear_expression(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "What is the **degree** of the algebraic expression \\(7x - 4\\)?"
    )
    sol = (
        "**Step 1:** The degree of an expression in one variable is the highest exponent of the variable.\n"
        "In \\(7x - 4\\), \\(x = x^1\\).\n\n"
        "**Answer:** **Degree 1 (Linear)**"
    )
    ans = "1"
    return {
        "id": f"g7_alg1_39_{rng.randint(100000, 999999)}",
        "subskill": "39_identify_degree_of_linear_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_39",
        "hints": {"tier_1": "What is the highest power of x?", "tier_2": "Degree is 1.", "tier_3": ans},
        "misconception_tags": ["degree_identification_slip"]
    }


# 40. Identify degree of quadratic expression
def arch_40_identify_degree_of_quadratic_expression(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "State the degree of the expression \\(3x^2 - 5x + 9\\)."
    )
    sol = (
        "**Step 1:** Find the term with the highest power of \\(x\\):\n"
        "The highest exponent is 2 in \\(3x^2\\).\n\n"
        "**Answer:** **Degree 2 (Quadratic)**"
    )
    ans = "2"
    return {
        "id": f"g7_alg1_40_{rng.randint(100000, 999999)}",
        "subskill": "40_identify_degree_of_quadratic_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_40",
        "hints": {"tier_1": "Look at the highest power of x.", "tier_2": "Degree is 2.", "tier_3": ans},
        "misconception_tags": ["quadratic_degree_slip"]
    }


# 41. Expression vs equation fundamental difference
def arch_41_expression_vs_equation_fundamental_difference(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain the key difference between an **algebraic expression** and an **algebraic equation**.\n\n"
        "Classify \\(3x + 5\\) and \\(3x + 5 = 20\\)."
    )
    sol = (
        "**Differences:**\n"
        "- **Algebraic Expression:** A mathematical phrase containing numbers, variables, and operations, with **no equals sign** (e.g. \\(3x + 5\\)).\n"
        "- **Algebraic Equation:** A mathematical statement asserting that two expressions are equal, containing an **equals sign (=)** (e.g. \\(3x + 5 = 20\\)).\n\n"
        "**Summary:** \\(3x + 5\\) is an expression; \\(3x + 5 = 20\\) is an equation."
    )
    ans = "3x + 5 is an expression; 3x + 5 = 20 is an equation"
    return {
        "id": f"g7_alg1_41_{rng.randint(100000, 999999)}",
        "subskill": "41_expression_vs_equation_fundamental_difference",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_41",
        "hints": {"tier_1": "Does it have an equals sign (=)?", "tier_2": "Equals sign makes it an equation.", "tier_3": ans},
        "misconception_tags": ["confusing_expression_with_equation"]
    }


# 42. Evaluate expression table multiple substitutions
def arch_42_evaluate_expression_table_multiple_substitutions(rng: random.Random) -> Dict[str, Any]:
    # Expression: 2x - 3 for x in 1, 2, 3 -> -1, 1, 3
    ans = "-1, 1, 3"
    prompt = (
        "Evaluate the expression \\(2x - 3\\) for \\(x = 1\\), \\(x = 2\\), and \\(x = 3\\)."
    )
    sol = (
        "**Step 1:** \\(x = 1 \\implies 2(1) - 3 = 2 - 3 = -1\\)\n\n"
        "**Step 2:** \\(x = 2 \\implies 2(2) - 3 = 4 - 3 = 1\\)\n\n"
        "**Step 3:** \\(x = 3 \\implies 2(3) - 3 = 6 - 3 = 3\\)\n\n"
        "**Values:** **-1, 1, 3**"
    )
    return {
        "id": f"g7_alg1_42_{rng.randint(100000, 999999)}",
        "subskill": "42_evaluate_expression_table_multiple_substitutions",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg1_42",
        "hints": {"tier_1": "Substitute 1, 2, 3 into 2x - 3.", "tier_2": "-1, 1, 3.", "tier_3": ans},
        "misconception_tags": ["multiple_substitution_integer_slip"]
    }


# 43. Evaluate expression comparing two expressions same input
def arch_43_evaluate_expression_comparing_two_expressions_same_input(rng: random.Random) -> Dict[str, Any]:
    # E1: 3x + 4, E2: 4x - 1. For x = 6: E1 = 22, E2 = 23
    ans = "4x - 1 (23 vs 22)"
    prompt = (
        "Compare the expressions \\(3x + 4\\) and \\(4x - 1\\) when \\(x = 6\\).\n\n"
        "Which expression has the larger numerical value?"
    )
    sol = (
        "**Step 1:** \\(3(6) + 4 = 18 + 4 = 22$$\n\n"
        "**Step 2:** \\(4(6) - 1 = 24 - 1 = 23$$\n\n"
        "**Conclusion:** **\\(4x - 1\\)** produces the larger value (23 vs 22)."
    )
    return {
        "id": f"g7_alg1_43_{rng.randint(100000, 999999)}",
        "subskill": "43_evaluate_expression_comparing_two_expressions_same_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_43",
        "hints": {"tier_1": "Substitute 6 into both.", "tier_2": "22 vs 23.", "tier_3": ans},
        "misconception_tags": ["expression_comparison_slip"]
    }


# 44. Translate perimeter of compound shape to expression
def arch_44_translate_perimeter_of_compound_shape_to_expression(rng: random.Random) -> Dict[str, Any]:
    # L-shape: horizontal sides x, 3, vertical sides y, 4 -> P = 2x + 2y (perimeter of bounding box)
    ans = "2x + 2y"
    prompt = (
        "An L-shaped garden has total horizontal width \\(x\\) and total vertical height \\(y\\).\n\n"
        "Write a simplified algebraic expression for its total outer perimeter."
    )
    sol = (
        "**Step 1:** An L-shape with bounding width \\(x\\) and height \\(y\\) has the same outer perimeter "
        "as a rectangle with dimensions \\(x\\) and \\(y\\).\n\n"
        "**Perimeter:** **\\(2x + 2y\\)** (or \\(2(x + y)\\))."
    )
    return {
        "id": f"g7_alg1_44_{rng.randint(100000, 999999)}",
        "subskill": "44_translate_perimeter_of_compound_shape_to_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_44",
        "hints": {"tier_1": "The perimeter of an L-shape equals 2(width + height).", "tier_2": "2x + 2y.", "tier_3": ans},
        "misconception_tags": ["compound_shape_perimeter_inner_edge_miscount"]
    }


# 45. Translate discount and markup to expression
def arch_45_translate_discount_and_markup_to_expression(rng: random.Random) -> Dict[str, Any]:
    # Item price P. Markup of R30: P + 30. Discount of R15: P - 15
    ans = "P + 30 and P - 15"
    prompt = (
        "An item has normal price \\(P\\).\n\n"
        "1. Write an expression for the price after a markup of R30.\n"
        "2. Write an expression for the price after a discount of R15."
    )
    sol = (
        "**1. Markup:** Increases price: **\\(P + 30\\)**\n\n"
        "**2. Discount:** Decreases price: **\\(P - 15\\)**"
    )
    return {
        "id": f"g7_alg1_45_{rng.randint(100000, 999999)}",
        "subskill": "45_translate_discount_and_markup_to_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_45",
        "hints": {"tier_1": "Markup adds, discount subtracts.", "tier_2": "P + 30 and P - 15.", "tier_3": ans},
        "misconception_tags": ["markup_discount_operation_inversion"]
    }


# 46. Translate speed distance time to expression
def arch_46_translate_speed_distance_time_to_expression(rng: random.Random) -> Dict[str, Any]:
    ans = "d/t"
    prompt = (
        "Write the algebraic expression for average speed when distance \\(d\\) is traveled in time \\(t\\)."
    )
    sol = (
        "**Step 1:** \\(\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}}\\)\n\n"
        "**Answer:** **\\(\\frac{d}{t}\\)**"
    )
    return {
        "id": f"g7_alg1_46_{rng.randint(100000, 999999)}",
        "subskill": "46_translate_speed_distance_time_to_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_46",
        "hints": {"tier_1": "Distance divided by time.", "tier_2": "d/t.", "tier_3": ans},
        "misconception_tags": ["speed_formula_fraction_inversion"]
    }


# 47. Identify parts of algebraic expression complete anatomy
def arch_47_identify_parts_of_algebraic_expression_complete_anatomy(rng: random.Random) -> Dict[str, Any]:
    expr = "-6x^2 + 7x - 15"
    ans = "1. -6; 2. 7; 3. -15; 4. 3 terms (trinomial)"
    prompt = (
        f"For the algebraic expression \\({expr}\\), identify:\n"
        f"1. The coefficient of \\(x^2\\)\n"
        f"2. The coefficient of \\(x\\)\n"
        f"3. The constant term\n"
        f"4. The number of terms and its classification"
    )
    sol = (
        f"**1. Coefficient of \\(x^2\\):** **-6**\n\n"
        f"**2. Coefficient of \\(x\\):** **7**\n\n"
        f"**3. Constant term:** **-15**\n\n"
        f"**4. Classification:** **3 terms (trinomial)**"
    )
    return {
        "id": f"g7_alg1_47_{rng.randint(100000, 999999)}",
        "subskill": "47_identify_parts_of_algebraic_expression_complete_anatomy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g7_alg1_47",
        "hints": {"tier_1": "Include signs with numbers.", "tier_2": "-6, 7, -15, trinomial.", "tier_3": ans},
        "misconception_tags": ["expression_anatomy_identification_slip"]
    }


# 48. Detecting algebraic syntax errors misconceptions
def arch_48_detecting_algebraic_syntax_errors_misconceptions(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner writes: \"\\(3 \\times x = 3^x\\)\".\n\n"
        "Explain the learner's error and provide the correct algebraic notation."
    )
    sol = (
        "**Error Analysis:**\n"
        "The learner confused multiplication with exponentiation.\n"
        "- \\(3 \\times x\\) is repeated addition, written as **\\(3x\\)**.\n"
        "- \\(3^x\\) represents 3 raised to the power \\(x\\).\n\n"
        "**Correct notation:** **\\(3x\\)**"
    )
    ans = "3x (confused multiplication with exponentiation)"
    return {
        "id": f"g7_alg1_48_{rng.randint(100000, 999999)}",
        "subskill": "48_detecting_algebraic_syntax_errors_misconceptions",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_48",
        "hints": {"tier_1": "3 times x is written without the times sign.", "tier_2": "3x, not 3^x.", "tier_3": ans},
        "misconception_tags": ["confusing_multiplication_with_exponents"]
    }


# 49. Reverse evaluation find input for given expression value
def arch_49_reverse_evaluation_find_input_for_given_expression_value(rng: random.Random) -> Dict[str, Any]:
    # Expression 5x - 3 equals 27 -> 5x = 30 -> x = 6
    ans = "6"
    prompt = (
        "For what value of \\(x\\) does the expression \\(5x - 3\\) have a numerical value of 27?"
    )
    sol = (
        "**Step 1:** Set expression equal to 27:\n"
        "$$5x - 3 = 27$$\n\n"
        "**Step 2:** Add 3:\n"
        "$$5x = 30$$\n\n"
        "**Step 3:** Divide by 5:\n"
        "$$x = \\frac{30}{5} = \\mathbf{6}$$"
    )
    return {
        "id": f"g7_alg1_49_{rng.randint(100000, 999999)}",
        "subskill": "49_reverse_evaluation_find_input_for_given_expression_value",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_49",
        "hints": {"tier_1": "Add 3 to 27, then divide by 5.", "tier_2": "30 / 5 = 6.", "tier_3": ans},
        "misconception_tags": ["reverse_algebraic_substitution_slip"]
    }


# 50. Algebraic expression comprehensive diagnostic autopsy
def arch_50_algebraic_expression_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    # Expression: 4(x + 2) - 3
    # 1. Expand: 4x + 8 - 3 = 4x + 5
    # 2. Evaluate at x = 7 -> 4(7) + 5 = 33
    # 3. Classify: Binomial of degree 1
    ans = "1. 4x + 5; 2. 33; 3. Binomial of degree 1"
    prompt = (
        "Given the algebraic expression \\(4(x + 2) - 3\\):\n\n"
        "1. Simplify the expression by expanding the brackets and combining like terms.\n"
        "2. Calculate its value when \\(x = 7\\).\n"
        "3. State its final classification by number of terms and degree."
    )
    sol = (
        "**Part 1: Simplification:**\n"
        "$$4(x + 2) - 3 = 4x + 8 - 3 = \\mathbf{4x + 5}$$\n\n"
        "**Part 2: Evaluation at \\(x = 7\\):**\n"
        "$$4(7) + 5 = 28 + 5 = \\mathbf{33}$$\n\n"
        "**Part 3: Classification:**\n"
        "Has 2 terms (\\(4x\\) and \\(5\\)) and highest power of \\(x\\) is 1: **Binomial of degree 1 (linear)**.\n\n"
        "**Summary:** 1. \\(4x + 5\\); 2. \\(33\\); 3. Binomial of degree 1"
    )
    return {
        "id": f"g7_alg1_50_{rng.randint(100000, 999999)}",
        "subskill": "50_algebraic_expression_comprehensive_diagnostic_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g7_alg1_50",
        "hints": {"tier_1": "1: Expand 4x + 8 - 3; 2: Substitute 7; 3: 2 terms = binomial.", "tier_2": "4x + 5, 33, Binomial degree 1.", "tier_3": ans},
        "misconception_tags": ["comprehensive_algebraic_expression_autopsy_slip"]
    }
