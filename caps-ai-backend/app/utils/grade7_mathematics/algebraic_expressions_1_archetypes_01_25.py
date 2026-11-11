"""Grade 7 Mathematics - Algebraic Expressions 1: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/04. Algebraic expressions 1.md
Focus: Algebraic language, variables, coefficients, constants, number of terms, verbal-to-algebra translation, and substitution evaluation.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Identify variable in linear expression
def arch_01_identify_variable_in_linear_expression(rng: random.Random) -> Dict[str, Any]:
    # e.g., 5x + 9
    var = rng.choice(["x", "y", "a", "m", "p", "t"])
    coeff = rng.randint(3, 9)
    const = rng.randint(2, 15)
    expr = f"{coeff}{var} + {const}"
    ans = var
    prompt = (
        f"Consider the algebraic expression:\n"
        f"\\[ {expr} \\]\n\n"
        f"State the **variable** in this expression."
    )
    sol = (
        f"**Step 1:** In algebra, a variable is the letter representing an unknown or changeable quantity.\n\n"
        f"**Answer:** **\\({var}\\)**"
    )
    return {
        "id": f"g7_alg1_01_{rng.randint(100000, 999999)}",
        "subskill": "01_identify_variable_in_linear_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_01",
        "hints": {"tier_1": "Which letter is used?", "tier_2": f"The variable is {var}.", "tier_3": ans},
        "misconception_tags": ["confusing_variable_with_coefficient"]
    }


# 02. Identify coefficient positive integer
def arch_02_identify_coefficient_positive_integer(rng: random.Random) -> Dict[str, Any]:
    coeff = rng.choice([4, 6, 7, 8, 9])
    expr = f"{coeff}x - 5"
    ans = str(coeff)
    prompt = (
        f"In the expression \\({expr}\\), what is the **coefficient** of \\(x\\)?"
    )
    sol = (
        f"**Step 1:** The coefficient is the number multiplied by the variable.\n\n"
        f"**Answer:** **{coeff}**"
    )
    return {
        "id": f"g7_alg1_02_{rng.randint(100000, 999999)}",
        "subskill": "02_identify_coefficient_positive_integer",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_02",
        "hints": {"tier_1": "The number directly in front of x.", "tier_2": f"Coefficient is {coeff}.", "tier_3": ans},
        "misconception_tags": ["including_variable_in_coefficient"]
    }


# 03. Identify coefficient negative integer
def arch_03_identify_coefficient_negative_integer(rng: random.Random) -> Dict[str, Any]:
    coeff = rng.choice([3, 5, 6, 8])
    expr = f"-{coeff}y + 11"
    ans = f"-{coeff}"
    prompt = (
        f"Identify the coefficient of \\(y\\) in the expression \\({expr}\\) (include the sign)."
    )
    sol = (
        f"**Step 1:** The sign in front belongs to the term.\n\n"
        f"**Answer:** **-{coeff}**"
    )
    return {
        "id": f"g7_alg1_03_{rng.randint(100000, 999999)}",
        "subskill": "03_identify_coefficient_negative_integer",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_03",
        "hints": {"tier_1": "Remember to include the negative sign.", "tier_2": f"-{coeff}.", "tier_3": ans},
        "misconception_tags": ["dropping_negative_sign_from_coefficient"]
    }


# 04. Identify coefficient implicit one and minus one
def arch_04_identify_coefficient_implicit_one_and_minus_one(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "1. What is the numerical coefficient of \\(x\\) in the term \\(x\\)?\n"
        "2. What is the coefficient of \\(y\\) in the term \\(-y\\)?"
    )
    sol = (
        "**Step 1:** When no number is written before a variable, the coefficient is an implicit **1**:\n"
        "\\(x = 1x \\implies\\) coefficient is **1**.\n\n"
        "**Step 2:** For \\(-y\\), the implicit multiplier is **-1**:\n"
        "\\(-y = -1y \\implies\\) coefficient is **-1**.\n\n"
        "**Summary:** 1. 1; 2. -1"
    )
    ans = "1. 1; 2. -1"
    return {
        "id": f"g7_alg1_04_{rng.randint(100000, 999999)}",
        "subskill": "04_identify_coefficient_implicit_one_and_minus_one",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_04",
        "hints": {"tier_1": "x means 1x; -y means -1y.", "tier_2": "1 and -1.", "tier_3": ans},
        "misconception_tags": ["claiming_coefficient_is_zero_when_none_written"]
    }


# 05. Identify constant term positive
def arch_05_identify_constant_term_positive(rng: random.Random) -> Dict[str, Any]:
    const = rng.randint(7, 24)
    expr = f"4x + {const}"
    ans = str(const)
    prompt = (
        f"State the **constant term** in the expression \\({expr}\\)."
    )
    sol = (
        f"**Step 1:** The constant term is the standalone numerical term with no variable attached.\n\n"
        f"**Answer:** **{const}**"
    )
    return {
        "id": f"g7_alg1_05_{rng.randint(100000, 999999)}",
        "subskill": "05_identify_constant_term_positive",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_05",
        "hints": {"tier_1": "Which number has no x attached?", "tier_2": f"Constant is {const}.", "tier_3": ans},
        "misconception_tags": ["confusing_constant_with_coefficient"]
    }


# 06. Identify constant term negative
def arch_06_identify_constant_term_negative(rng: random.Random) -> Dict[str, Any]:
    const = rng.randint(8, 25)
    expr = f"7a - {const}"
    ans = f"-{const}"
    prompt = (
        f"State the constant term in the expression \\({expr}\\) (include the sign)."
    )
    sol = (
        f"**Step 1:** The subtraction sign belongs to the constant: \\(+ (-{const})\\).\n\n"
        f"**Answer:** **-{const}**"
    )
    return {
        "id": f"g7_alg1_06_{rng.randint(100000, 999999)}",
        "subskill": "06_identify_constant_term_negative",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_06",
        "hints": {"tier_1": "Include the negative sign.", "tier_2": f"-{const}.", "tier_3": ans},
        "misconception_tags": ["omitting_negative_sign_from_constant"]
    }


# 07. Identify constant term implicit zero
def arch_07_identify_constant_term_implicit_zero(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the algebraic expression \\(8x\\), what is the value of the **constant term**?"
    )
    sol = (
        "**Step 1:** The expression can be written as \\(8x + 0\\).\n\n"
        "**Answer:** **0** (there is no constant added, so it is zero)."
    )
    ans = "0"
    return {
        "id": f"g7_alg1_07_{rng.randint(100000, 999999)}",
        "subskill": "07_identify_constant_term_implicit_zero",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_07",
        "hints": {"tier_1": "8x + 0.", "tier_2": "Constant is 0.", "tier_3": ans},
        "misconception_tags": ["claiming_no_constant_exists_instead_of_zero"]
    }


# 08. Count number of terms monomial
def arch_08_count_number_of_terms_monomial(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider the expression \\(5xy\\).\n\n"
        "1. How many terms are in this expression?\n"
        "2. What is the special name given to an algebraic expression with this number of terms?"
    )
    sol = (
        "**Step 1:** Terms are separated only by \\(+\\) or \\(-\\) signs. Multiplication does not separate terms.\n"
        "There is **1 term**.\n\n"
        "**Step 2:** An expression with one single term is called a **monomial**.\n\n"
        "**Summary:** 1. 1 term; 2. Monomial"
    )
    ans = "1. 1 term; 2. Monomial"
    return {
        "id": f"g7_alg1_08_{rng.randint(100000, 999999)}",
        "subskill": "08_count_number_of_terms_monomial",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_08",
        "hints": {"tier_1": "Multiplication binds items into a single term.", "tier_2": "1 term = monomial.", "tier_3": ans},
        "misconception_tags": ["counting_multiplied_variables_as_separate_terms"]
    }


# 09. Count number of terms binomial
def arch_09_count_number_of_terms_binomial(rng: random.Random) -> Dict[str, Any]:
    expr = "3x + 7"
    ans = "2 terms (binomial)"
    prompt = (
        f"How many terms are in the expression \\({expr}\\), and what is it called?"
    )
    sol = (
        f"**Step 1:** The \\(+\\) sign separates two terms: \\(3x\\) and \\(7\\).\n\n"
        f"**Step 2:** An expression with two terms is called a **binomial**.\n\n"
        f"**Answer:** **2 terms (binomial)**"
    )
    return {
        "id": f"g7_alg1_09_{rng.randint(100000, 999999)}",
        "subskill": "09_count_number_of_terms_binomial",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_09",
        "hints": {"tier_1": "Separated by plus: 3x and 7.", "tier_2": "2 terms = binomial.", "tier_3": ans},
        "misconception_tags": ["term_counting_error"]
    }


# 10. Count number of terms trinomial
def arch_10_count_number_of_terms_trinomial(rng: random.Random) -> Dict[str, Any]:
    expr = "2x^2 + 5x - 8"
    ans = "3 terms (trinomial)"
    prompt = (
        f"State the number of terms and the classification of \\({expr}\\)."
    )
    sol = (
        f"**Step 1:** The terms are \\(2x^2\\), \\(+5x\\), and \\(-8\\) (total of 3 terms).\n\n"
        f"**Step 2:** A three-term expression is a **trinomial**.\n\n"
        f"**Answer:** **3 terms (trinomial)**"
    )
    return {
        "id": f"g7_alg1_10_{rng.randint(100000, 999999)}",
        "subskill": "10_count_number_of_terms_trinomial",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_10",
        "hints": {"tier_1": "Count: 2x², 5x, -8.", "tier_2": "3 terms = trinomial.", "tier_3": ans},
        "misconception_tags": ["trinomial_classification_slip"]
    }


# 11. Algebraic convention multiplication omission
def arch_11_algebraic_convention_multiplication_omission(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In algebra, how do we write \\(4 \\times a \\times b\\) in standard, simplified algebraic convention?"
    )
    sol = (
        "**Convention:** Multiplication signs (\\(\\times\\)) between numbers and variables are omitted, "
        "and variables are listed in alphabetical order.\n\n"
        "**Answer:** **\\(4ab\\)**"
    )
    ans = "4ab"
    return {
        "id": f"g7_alg1_11_{rng.randint(100000, 999999)}",
        "subskill": "11_algebraic_convention_multiplication_omission",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_11",
        "hints": {"tier_1": "Omit the multiplication signs.", "tier_2": "4ab.", "tier_3": ans},
        "misconception_tags": ["retaining_multiplication_crosses"]
    }


# 12. Algebraic convention division as fraction
def arch_12_algebraic_convention_division_as_fraction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Write \\(x \\div 5\\) according to standard algebraic notation."
    )
    sol = (
        "**Convention:** In algebra, division is written as a common fraction with numerator and denominator.\n\n"
        "**Answer:** **\\(\\frac{x}{5}\\)**"
    )
    ans = "x/5"
    return {
        "id": f"g7_alg1_12_{rng.randint(100000, 999999)}",
        "subskill": "12_algebraic_convention_division_as_fraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_12",
        "hints": {"tier_1": "Write as a fraction with x on top.", "tier_2": "x/5.", "tier_3": ans},
        "misconception_tags": ["retaining_division_obelus_sign"]
    }


# 13. Translate sum and more than to algebraic expression
def arch_13_translate_sum_and_more_than_to_algebraic_expression(rng: random.Random) -> Dict[str, Any]:
    # "6 more than a number n" -> n + 6
    ans = "n + 6"
    prompt = (
        "Write an algebraic expression for:\n\n"
        "\"*6 more than a number \\(n\\)*\""
    )
    sol = (
        "**Step 1:** 'More than' represents addition.\n\n"
        "**Answer:** **\\(n + 6\\)**"
    )
    return {
        "id": f"g7_alg1_13_{rng.randint(100000, 999999)}",
        "subskill": "13_translate_sum_and_more_than_to_algebraic_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_13",
        "hints": {"tier_1": "Add 6 to n.", "tier_2": "n + 6.", "tier_3": ans},
        "misconception_tags": ["verbal_addition_translation_slip"]
    }


# 14. Translate difference and less than to algebraic expression
def arch_14_translate_difference_and_less_than_to_algebraic_expression(rng: random.Random) -> Dict[str, Any]:
    # "8 less than a number x" -> x - 8 (not 8 - x!)
    ans = "x - 8"
    prompt = (
        "Write an algebraic expression for:\n\n"
        "\"*8 less than a number \\(x\\)*\""
    )
    sol = (
        "**Step 1:** '8 less than \\(x\\)' means starting with \\(x\\) and subtracting 8.\n\n"
        "**Answer:** **\\(x - 8\\)**\n\n"
        "*(Caution: \\(8 - x\\) means 'x subtracted from 8', which is different!)*"
    )
    return {
        "id": f"g7_alg1_14_{rng.randint(100000, 999999)}",
        "subskill": "14_translate_difference_and_less_than_to_algebraic_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_14",
        "hints": {"tier_1": "Start with x and take away 8.", "tier_2": "x - 8 (not 8 - x).", "tier_3": ans},
        "misconception_tags": ["subtraction_reversal_in_less_than"]
    }


# 15. Translate product and times to algebraic expression
def arch_15_translate_product_and_times_to_algebraic_expression(rng: random.Random) -> Dict[str, Any]:
    # "The product of 9 and a number y" -> 9y
    ans = "9y"
    prompt = (
        "Write an algebraic expression for:\n\n"
        "\"*The product of 9 and a number \\(y\\)*\""
    )
    sol = (
        "**Step 1:** Product means multiplication:\n"
        "$$9 \\times y = \\mathbf{9y}$$"
    )
    return {
        "id": f"g7_alg1_15_{rng.randint(100000, 999999)}",
        "subskill": "15_translate_product_and_times_to_algebraic_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_15",
        "hints": {"tier_1": "Multiply 9 by y.", "tier_2": "9y.", "tier_3": ans},
        "misconception_tags": ["product_definition_slip"]
    }


# 16. Translate quotient to algebraic expression
def arch_16_translate_quotient_to_algebraic_expression(rng: random.Random) -> Dict[str, Any]:
    ans = "m/7"
    prompt = (
        "Write an algebraic expression for:\n\n"
        "\"*The quotient of a number \\(m\\) and 7*\""
    )
    sol = (
        "**Step 1:** Quotient represents division:\n"
        "$$\\mathbf{\\frac{m}{7}}$$"
    )
    return {
        "id": f"g7_alg1_16_{rng.randint(100000, 999999)}",
        "subskill": "16_translate_quotient_to_algebraic_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_16",
        "hints": {"tier_1": "Write m divided by 7 as a fraction.", "tier_2": "m/7.", "tier_3": ans},
        "misconception_tags": ["quotient_division_order_slip"]
    }


# 17. Translate two step multiplication then addition
def arch_17_translate_two_step_multiplication_then_addition(rng: random.Random) -> Dict[str, Any]:
    # "5 more than three times a number x" -> 3x + 5
    ans = "3x + 5"
    prompt = (
        "Translate into an algebraic expression:\n\n"
        "\"*5 more than three times a number \\(x\\)*\""
    )
    sol = (
        "**Step 1:** Three times \\(x\\): \\(3x\\)\n\n"
        "**Step 2:** 5 more than that: \\(\\mathbf{3x + 5}\\)"
    )
    return {
        "id": f"g7_alg1_17_{rng.randint(100000, 999999)}",
        "subskill": "17_translate_two_step_multiplication_then_addition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_17",
        "hints": {"tier_1": "Multiply by 3 first, then add 5.", "tier_2": "3x + 5.", "tier_3": ans},
        "misconception_tags": ["two_step_operation_transposition"]
    }


# 18. Translate two step multiplication then subtraction
def arch_18_translate_two_step_multiplication_then_subtraction(rng: random.Random) -> Dict[str, Any]:
    # "4 less than double a number y" -> 2y - 4
    ans = "2y - 4"
    prompt = (
        "Translate into an algebraic expression:\n\n"
        "\"*4 less than double a number \\(y\\)*\""
    )
    sol = (
        "**Step 1:** Double \\(y\\): \\(2y\\)\n\n"
        "**Step 2:** 4 less than that: \\(\\mathbf{2y - 4}\\)"
    )
    return {
        "id": f"g7_alg1_18_{rng.randint(100000, 999999)}",
        "subskill": "18_translate_two_step_multiplication_then_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_18",
        "hints": {"tier_1": "Double = 2y. 4 less = - 4.", "tier_2": "2y - 4.", "tier_3": ans},
        "misconception_tags": ["subtraction_order_inversion_two_step"]
    }


# 19. Translate two step addition then multiplication brackets
def arch_19_translate_two_step_addition_then_multiplication_brackets(rng: random.Random) -> Dict[str, Any]:
    # "Multiply the sum of x and 7 by 4" -> 4(x + 7)
    ans = "4(x + 7)"
    prompt = (
        "Write an expression for:\n\n"
        "\"*Multiply the sum of \\(x\\) and 7 by 4*\""
    )
    sol = (
        "**Step 1:** The 'sum of \\(x\\) and 7' is grouped in brackets: \\((x + 7)\\)\n\n"
        "**Step 2:** Multiply the entire sum by 4:\n"
        "$$\\mathbf{4(x + 7)}$$"
    )
    return {
        "id": f"g7_alg1_19_{rng.randint(100000, 999999)}",
        "subskill": "19_translate_two_step_addition_then_multiplication_brackets",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_19",
        "hints": {"tier_1": "Brackets around (x + 7).", "tier_2": "4(x + 7).", "tier_3": ans},
        "misconception_tags": ["omitting_brackets_around_sum"]
    }


# 20. Translate subtraction order critical x less than y
def arch_20_translate_subtraction_order_critical_x_less_than_y(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain the exact difference in meaning between:\n"
        "1. \\(x - 10\\)\n"
        "2. \\(10 - x\\)"
    )
    sol = (
        "**Step 1:** \\(x - 10\\) means **\"10 less than \\(x\\)\"** (or 10 subtracted from \\(x\\)).\n\n"
        "**Step 2:** \\(10 - x\\) means **\"\\(x\\) less than 10\"** (or \\(x\\) subtracted from 10).\n\n"
        "Subtraction is not commutative, so the order of terms is critical."
    )
    ans = "x - 10 is 10 less than x; 10 - x is x subtracted from 10"
    return {
        "id": f"g7_alg1_20_{rng.randint(100000, 999999)}",
        "subskill": "20_translate_subtraction_order_critical_x_less_than_y",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_20",
        "hints": {"tier_1": "Which value is being reduced?", "tier_2": "Subtraction order matters.", "tier_3": ans},
        "misconception_tags": ["assuming_subtraction_is_commutative"]
    }


# 21. Evaluate expression single term substitution
def arch_21_evaluate_expression_single_term_substitution(rng: random.Random) -> Dict[str, Any]:
    # 7x when x = 8 -> 56
    ans = "56"
    prompt = (
        "Evaluate the expression \\(7x\\) when \\(x = 8\\)."
    )
    sol = (
        "**Step 1:** Substitute \\(x = 8\\):\n"
        "$$7x = 7(8) = 7 \\times 8 = \\mathbf{56}$$"
    )
    return {
        "id": f"g7_alg1_21_{rng.randint(100000, 999999)}",
        "subskill": "21_evaluate_expression_single_term_substitution",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_21",
        "hints": {"tier_1": "Multiply 7 by 8.", "tier_2": "7 * 8 = 56.", "tier_3": ans},
        "misconception_tags": ["concatenating_digits_7_and_8_as_78"]
    }


# 22. Evaluate linear expression positive integer substitution
def arch_22_evaluate_linear_expression_positive_integer_substitution(rng: random.Random) -> Dict[str, Any]:
    # 4x + 9 when x = 6 -> 24 + 9 = 33
    ans = "33"
    prompt = (
        "Calculate the numerical value of \\(4x + 9\\) when \\(x = 6\\)."
    )
    sol = (
        "**Step 1:** Substitute \\(x = 6\\):\n"
        "$$4(6) + 9 = 24 + 9 = \\mathbf{33}$$"
    )
    return {
        "id": f"g7_alg1_22_{rng.randint(100000, 999999)}",
        "subskill": "22_evaluate_linear_expression_positive_integer_substitution",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_22",
        "hints": {"tier_1": "4 * 6 = 24, then add 9.", "tier_2": "24 + 9 = 33.", "tier_3": ans},
        "misconception_tags": ["substitution_bodmas_order_error"]
    }


# 23. Evaluate linear expression zero substitution
def arch_23_evaluate_linear_expression_zero_substitution(rng: random.Random) -> Dict[str, Any]:
    # 5x - 8 when x = 0 -> -8
    ans = "-8"
    prompt = (
        "Evaluate the expression \\(5x - 8\\) when \\(x = 0\\)."
    )
    sol = (
        "**Step 1:** Substitute \\(x = 0\\):\n"
        "$$5(0) - 8 = 0 - 8 = \\mathbf{-8}$$"
    )
    return {
        "id": f"g7_alg1_23_{rng.randint(100000, 999999)}",
        "subskill": "23_evaluate_linear_expression_zero_substitution",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg1_23",
        "hints": {"tier_1": "5 * 0 = 0.", "tier_2": "0 - 8 = -8.", "tier_3": ans},
        "misconception_tags": ["zero_multiplication_misconception"]
    }


# 24. Evaluate linear expression negative integer substitution
def arch_24_evaluate_linear_expression_negative_integer_substitution(rng: random.Random) -> Dict[str, Any]:
    # 3x + 14 when x = -4 -> 3(-4) + 14 = -12 + 14 = 2
    ans = "2"
    prompt = (
        "Calculate the value of \\(3x + 14\\) when \\(x = -4\\)."
    )
    sol = (
        "**Step 1:** Substitute \\(x = -4\\):\n"
        "$$3(-4) + 14 = -12 + 14 = \\mathbf{2}$$"
    )
    return {
        "id": f"g7_alg1_24_{rng.randint(100000, 999999)}",
        "subskill": "24_evaluate_linear_expression_negative_integer_substitution",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_24",
        "hints": {"tier_1": "3 * (-4) = -12.", "tier_2": "-12 + 14 = 2.", "tier_3": ans},
        "misconception_tags": ["negative_integer_multiplication_sign_error"]
    }


# 25. Evaluate linear expression fractional substitution
def arch_25_evaluate_linear_expression_fractional_substitution(rng: random.Random) -> Dict[str, Any]:
    # 6x - 1 when x = 1/2 -> 6(1/2) - 1 = 3 - 1 = 2
    ans = "2"
    prompt = (
        "Evaluate the expression \\(6x - 1\\) when \\(x = \\frac{1}{2}\\)."
    )
    sol = (
        "**Step 1:** Substitute \\(x = \\frac{1}{2}\\):\n"
        "$$6\\left(\\frac{1}{2}\\right) - 1 = 3 - 1 = \\mathbf{2}$$"
    )
    return {
        "id": f"g7_alg1_25_{rng.randint(100000, 999999)}",
        "subskill": "25_evaluate_linear_expression_fractional_substitution",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg1_25",
        "hints": {"tier_1": "Half of 6 is 3.", "tier_2": "3 - 1 = 2.", "tier_3": ans},
        "misconception_tags": ["fraction_substitution_arithmetic_slip"]
    }
