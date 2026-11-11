"""Grade 7 Mathematics - Algebraic Expressions 2: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/04. Algebraic expressions 2.md
Focus: Combining like terms (linear, compound, two-variable), distributive expansion, and geometric perimeters.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Collect like terms simple addition
def arch_01_collect_like_terms_simple_addition(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 8)
    b = rng.randint(4, 9)
    ans = f"{a + b}x"
    prompt = (
        f"Simplify the expression by combining like terms:\n"
        f"\\[ {a}x + {b}x \\]"
    )
    sol = (
        f"**Step 1:** Add the coefficients of \\(x\\):\n"
        f"$$({a} + {b})x = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_01_{rng.randint(100000, 999999)}",
        "subskill": "01_collect_like_terms_simple_addition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg2_01",
        "hints": {"tier_1": f"Add {a} + {b} and keep the variable x.", "tier_2": f"({a} + {b})x.", "tier_3": ans},
        "misconception_tags": ["adding_exponents_when_adding_terms"]
    }


# 02. Collect like terms simple subtraction
def arch_02_collect_like_terms_simple_subtraction(rng: random.Random) -> Dict[str, Any]:
    b = rng.randint(3, 7)
    diff = rng.randint(2, 6)
    a = b + diff
    ans = f"{diff}y"
    prompt = (
        f"Simplify by collecting like terms:\n"
        f"\\[ {a}y - {b}y \\]"
    )
    sol = (
        f"**Step 1:** Subtract the coefficients:\n"
        f"$$({a} - {b})y = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_02_{rng.randint(100000, 999999)}",
        "subskill": "02_collect_like_terms_simple_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg2_02",
        "hints": {"tier_1": f"Subtract {b} from {a}.", "tier_2": f"{diff}y.", "tier_3": ans},
        "misconception_tags": ["subtraction_arithmetic_slip"]
    }


# 03. Collect like terms three linear terms
def arch_03_collect_like_terms_three_linear_terms(rng: random.Random) -> Dict[str, Any]:
    # 7m - 3m + 5m -> 9m
    ans = "9m"
    prompt = (
        "Simplify the following three-term linear expression:\n"
        "\\[ 7m - 3m + 5m \\]"
    )
    sol = (
        "**Step 1:** Work left to right with like terms:\n"
        "$$7m - 3m = 4m$$\n"
        "$$4m + 5m = \\mathbf{9m}$$"
    )
    return {
        "id": f"g7_alg2_03_{rng.randint(100000, 999999)}",
        "subskill": "03_collect_like_terms_three_linear_terms",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_03",
        "hints": {"tier_1": "7 - 3 = 4, then 4 + 5 = 9.", "tier_2": "9m.", "tier_3": ans},
        "misconception_tags": ["left_to_right_evaluation_error"]
    }


# 04. Collect like terms with implicit one coefficient
def arch_04_collect_like_terms_with_implicit_one_coefficient(rng: random.Random) -> Dict[str, Any]:
    # 4a + a -> 5a
    ans = "5a"
    prompt = (
        "Simplify: \\[ 4a + a \\]"
    )
    sol = (
        "**Step 1:** Recall that \\(a = 1a\\):\n"
        "$$4a + 1a = (4 + 1)a = \\mathbf{5a}$$"
    )
    return {
        "id": f"g7_alg2_04_{rng.randint(100000, 999999)}",
        "subskill": "04_collect_like_terms_with_implicit_one_coefficient",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg2_04",
        "hints": {"tier_1": "The single 'a' has a coefficient of 1.", "tier_2": "4 + 1 = 5.", "tier_3": ans},
        "misconception_tags": ["treating_bare_variable_as_zero"]
    }


# 05. Collect like terms resulting in zero
def arch_05_collect_like_terms_resulting_in_zero(rng: random.Random) -> Dict[str, Any]:
    # 6k - 6k -> 0 (not 0k)
    ans = "0"
    prompt = (
        "Simplify completely: \\[ 6k - 6k \\]"
    )
    sol = (
        "**Step 1:** Subtract the coefficients:\n"
        "$$6k - 6k = (6 - 6)k = 0k = \\mathbf{0}$$\n\n"
        "*(In algebra, \\(0k\\) is written simply as 0)*."
    )
    return {
        "id": f"g7_alg2_05_{rng.randint(100000, 999999)}",
        "subskill": "05_collect_like_terms_resulting_in_zero",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg2_05",
        "hints": {"tier_1": "6 minus 6 equals 0.", "tier_2": "0.", "tier_3": ans},
        "misconception_tags": ["writing_zero_variable_instead_of_zero"]
    }


# 06. Collect like terms with negative coefficients
def arch_06_collect_like_terms_with_negative_coefficients(rng: random.Random) -> Dict[str, Any]:
    # -8x + 3x -> -5x
    ans = "-5x"
    prompt = (
        "Simplify the integer linear expression: \\[ -8x + 3x \\]"
    )
    sol = (
        "**Step 1:** Combine the coefficients: \\(-8 + 3 = -5\\)\n\n"
        "**Answer:** **\\(-5x\\)**"
    )
    return {
        "id": f"g7_alg2_06_{rng.randint(100000, 999999)}",
        "subskill": "06_collect_like_terms_with_negative_coefficients",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg2_06",
        "hints": {"tier_1": "-8 + 3 = -5.", "tier_2": "-5x.", "tier_3": ans},
        "misconception_tags": ["negative_integer_addition_error"]
    }


# 07. Collect like terms two variables addition
def arch_07_collect_like_terms_two_variables_addition(rng: random.Random) -> Dict[str, Any]:
    # 3x + 4y + 5x + 2y -> 8x + 6y
    ans = "8x + 6y"
    prompt = (
        "Simplify by grouping and combining like terms:\n"
        "\\[ 3x + 4y + 5x + 2y \\]"
    )
    sol = (
        "**Step 1:** Group terms with the same variable:\n"
        "$$(3x + 5x) + (4y + 2y)$$\n\n"
        "**Step 2:** Combine each group:\n"
        "$$8x + 6y$$\n\n"
        "*(Note: \\(8x\\) and \\(6y\\) are unlike terms and cannot be combined into 14xy!)*"
    )
    return {
        "id": f"g7_alg2_07_{rng.randint(100000, 999999)}",
        "subskill": "07_collect_like_terms_two_variables_addition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_07",
        "hints": {"tier_1": "Combine the x-terms together, and the y-terms together.", "tier_2": "3x+5x=8x, 4y+2y=6y.", "tier_3": ans},
        "misconception_tags": ["combining_unlike_variables_into_product"]
    }


# 08. Collect like terms two variables subtraction
def arch_08_collect_like_terms_two_variables_subtraction(rng: random.Random) -> Dict[str, Any]:
    # 9a + 7b - 4a - 5b -> 5a + 2b
    ans = "5a + 2b"
    prompt = (
        "Simplify: \\[ 9a + 7b - 4a - 5b \\]"
    )
    sol = (
        "**Step 1:** Group \\(a\\)-terms and \\(b\\)-terms:\n"
        "$$(9a - 4a) + (7b - 5b)$$\n\n"
        "**Step 2:** Combine like terms:\n"
        "$$\\mathbf{5a + 2b}$$"
    )
    return {
        "id": f"g7_alg2_08_{rng.randint(100000, 999999)}",
        "subskill": "08_collect_like_terms_two_variables_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_08",
        "hints": {"tier_1": "9a - 4a = 5a; 7b - 5b = 2b.", "tier_2": "5a + 2b.", "tier_3": ans},
        "misconception_tags": ["subtraction_grouping_sign_slip"]
    }


# 09. Collect like terms variable and constant
def arch_09_collect_like_terms_variable_and_constant(rng: random.Random) -> Dict[str, Any]:
    # 4x + 7 + 2x - 3 -> 6x + 4
    ans = "6x + 4"
    prompt = (
        "Simplify by combining like terms:\n"
        "\\[ 4x + 7 + 2x - 3 \\]"
    )
    sol = (
        "**Step 1:** Group variables and constants:\n"
        "$$(4x + 2x) + (7 - 3)$$\n\n"
        "**Step 2:** Combine:\n"
        "$$\\mathbf{6x + 4}$$"
    )
    return {
        "id": f"g7_alg2_09_{rng.randint(100000, 999999)}",
        "subskill": "09_collect_like_terms_variable_and_constant",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_09",
        "hints": {"tier_1": "Add 4x + 2x = 6x; 7 - 3 = 4.", "tier_2": "6x + 4 (do NOT write 10x!).", "tier_3": ans},
        "misconception_tags": ["adding_constants_into_variable_term"]
    }


# 10. Collect like terms multiple variables and constants
def arch_10_collect_like_terms_multiple_variables_and_constants(rng: random.Random) -> Dict[str, Any]:
    # 5x + 3y + 8 - 2x + 4y - 5 -> 3x + 7y + 3
    ans = "3x + 7y + 3"
    prompt = (
        "Simplify completely:\n"
        "\\[ 5x + 3y + 8 - 2x + 4y - 5 \\]"
    )
    sol = (
        "**Step 1:** Group like terms:\n"
        "$$(5x - 2x) + (3y + 4y) + (8 - 5)$$\n\n"
        "**Step 2:** Combine:\n"
        "$$\\mathbf{3x + 7y + 3}$$"
    )
    return {
        "id": f"g7_alg2_10_{rng.randint(100000, 999999)}",
        "subskill": "10_collect_like_terms_multiple_variables_and_constants",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_10",
        "hints": {"tier_1": "Group x-terms, y-terms, and numbers.", "tier_2": "3x + 7y + 3.", "tier_3": ans},
        "misconception_tags": ["compound_term_collection_slip"]
    }


# 11. Distributive law single bracket positive multiplier
def arch_11_distributive_law_single_bracket_positive_multiplier(rng: random.Random) -> Dict[str, Any]:
    # 3(2x + 5) -> 6x + 15
    ans = "6x + 15"
    prompt = (
        "Apply the distributive property to expand the brackets:\n"
        "\\[ 3(2x + 5) \\]"
    )
    sol = (
        "**Step 1:** Multiply 3 by each term inside the bracket:\n"
        "$$3 \\times 2x + 3 \\times 5 = \\mathbf{6x + 15}$$"
    )
    return {
        "id": f"g7_alg2_11_{rng.randint(100000, 999999)}",
        "subskill": "11_distributive_law_single_bracket_positive_multiplier",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_11",
        "hints": {"tier_1": "Multiply 3 by 2x, and 3 by 5.", "tier_2": "6x + 15.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_multiply_second_term_in_bracket"]
    }


# 12. Distributive law single bracket with subtraction
def arch_12_distributive_law_single_bracket_with_subtraction(rng: random.Random) -> Dict[str, Any]:
    # 4(3y - 7) -> 12y - 28
    ans = "12y - 28"
    prompt = (
        "Expand: \\[ 4(3y - 7) \\]"
    )
    sol = (
        "**Step 1:** Multiply 4 across both terms:\n"
        "$$4(3y) - 4(7) = \\mathbf{12y - 28}$$"
    )
    return {
        "id": f"g7_alg2_12_{rng.randint(100000, 999999)}",
        "subskill": "12_distributive_law_single_bracket_with_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_12",
        "hints": {"tier_1": "4 * 3y = 12y; 4 * 7 = 28.", "tier_2": "12y - 28.", "tier_3": ans},
        "misconception_tags": ["distributive_subtraction_slip"]
    }


# 13. Distributive law negative outside multiplier
def arch_13_distributive_law_negative_outside_multiplier(rng: random.Random) -> Dict[str, Any]:
    # -2(4x + 3) -> -8x - 6
    ans = "-8x - 6"
    prompt = (
        "Expand and simplify: \\[ -2(4x + 3) \\]"
    )
    sol = (
        "**Step 1:** Multiply \\(-2\\) by each term inside, observing sign rules:\n"
        "$$(-2) \\times 4x + (-2) \\times 3 = \\mathbf{-8x - 6}$$"
    )
    return {
        "id": f"g7_alg2_13_{rng.randint(100000, 999999)}",
        "subskill": "13_distributive_law_negative_outside_multiplier",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_13",
        "hints": {"tier_1": "A negative times a positive is negative.", "tier_2": "-8x - 6.", "tier_3": ans},
        "misconception_tags": ["sign_rule_error_with_negative_multiplier"]
    }


# 14. Distributive law negative outside with subtraction
def arch_14_distributive_law_negative_outside_with_subtraction(rng: random.Random) -> Dict[str, Any]:
    # -3(2x - 5) -> -6x + 15
    ans = "-6x + 15"
    prompt = (
        "Expand: \\[ -3(2x - 5) \\]"
    )
    sol = (
        "**Step 1:** Multiply \\(-3\\) by \\(2x\\): \\(-6x\\)\n\n"
        "**Step 2:** Multiply \\(-3\\) by \\(-5\\): \\((-3) \\times (-5) = +15\\)\n\n"
        "**Answer:** **\\(-6x + 15\\)**"
    )
    return {
        "id": f"g7_alg2_14_{rng.randint(100000, 999999)}",
        "subskill": "14_distributive_law_negative_outside_with_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_14",
        "hints": {"tier_1": "Negative times negative is positive (+15).", "tier_2": "-6x + 15.", "tier_3": ans},
        "misconception_tags": ["negative_times_negative_sign_error"]
    }


# 15. Distributive law variable multiplier x times x
def arch_15_distributive_law_variable_multiplier_x_times_x(rng: random.Random) -> Dict[str, Any]:
    # x(x + 4) -> x^2 + 4x
    ans = "x^2 + 4x"
    prompt = (
        "Expand: \\[ x(x + 4) \\]"
    )
    sol = (
        "**Step 1:** Multiply \\(x\\) by \\(x\\): \\(x \\times x = x^2\\)\n\n"
        "**Step 2:** Multiply \\(x\\) by 4: \\(4x\\)\n\n"
        "**Answer:** **\\(x^2 + 4x\\)**"
    )
    return {
        "id": f"g7_alg2_15_{rng.randint(100000, 999999)}",
        "subskill": "15_distributive_law_variable_multiplier_x_times_x",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_15",
        "hints": {"tier_1": "x * x = x² (not 2x!).", "tier_2": "x² + 4x.", "tier_3": ans},
        "misconception_tags": ["confusing_x_times_x_with_2x"]
    }


# 16. Expand and simplify bracket plus term
def arch_16_expand_and_simplify_bracket_plus_term(rng: random.Random) -> Dict[str, Any]:
    # 2(3x + 4) + 5x -> 6x + 8 + 5x = 11x + 8
    ans = "11x + 8"
    prompt = (
        "Expand the brackets and simplify by collecting like terms:\n"
        "\\[ 2(3x + 4) + 5x \\]"
    )
    sol = (
        "**Step 1:** Expand \\(2(3x + 4)\\):\n"
        "$$6x + 8$$\n\n"
        "**Step 2:** Add \\(+ 5x\\) and combine like terms:\n"
        "$$6x + 5x + 8 = \\mathbf{11x + 8}$$"
    )
    return {
        "id": f"g7_alg2_16_{rng.randint(100000, 999999)}",
        "subskill": "16_expand_and_simplify_bracket_plus_term",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_16",
        "hints": {"tier_1": "Expand 2(3x + 4) = 6x + 8.", "tier_2": "6x + 5x + 8 = 11x + 8.", "tier_3": ans},
        "misconception_tags": ["expanding_bracket_then_collecting_error"]
    }


# 17. Expand and simplify bracket minus term
def arch_17_expand_and_simplify_bracket_minus_term(rng: random.Random) -> Dict[str, Any]:
    # 3(4x - 2) - 5x -> 12x - 6 - 5x = 7x - 6
    ans = "7x - 6"
    prompt = (
        "Simplify completely: \\[ 3(4x - 2) - 5x \\]"
    )
    sol = (
        "**Step 1:** Expand \\(3(4x - 2)\\):\n"
        "$$12x - 6$$\n\n"
        "**Step 2:** Combine with \\(- 5x\\):\n"
        "$$12x - 5x - 6 = \\mathbf{7x - 6}$$"
    )
    return {
        "id": f"g7_alg2_17_{rng.randint(100000, 999999)}",
        "subskill": "17_expand_and_simplify_bracket_minus_term",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_17",
        "hints": {"tier_1": "12x - 6 - 5x.", "tier_2": "7x - 6.", "tier_3": ans},
        "misconception_tags": ["linear_bracket_simplification_slip"]
    }


# 18. Expand and simplify term minus bracket
def arch_18_expand_and_simplify_term_minus_bracket(rng: random.Random) -> Dict[str, Any]:
    # 10x - (3x + 4) -> 10x - 3x - 4 = 7x - 4
    ans = "7x - 4"
    prompt = (
        "Simplify by expanding the negative bracket:\n"
        "\\[ 10x - (3x + 4) \\]"
    )
    sol = (
        "**Step 1:** Distribute the negative sign across both terms inside:\n"
        "$$10x - 3x - 4$$\n\n"
        "**Step 2:** Combine like terms:\n"
        "$$\\mathbf{7x - 4}$$"
    )
    return {
        "id": f"g7_alg2_18_{rng.randint(100000, 999999)}",
        "subskill": "18_expand_and_simplify_term_minus_bracket",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_18",
        "hints": {"tier_1": "The minus changes both signs inside: - 3x - 4.", "tier_2": "7x - 4.", "tier_3": ans},
        "misconception_tags": ["failing_to_distribute_negative_to_second_term"]
    }


# 19. Expand and simplify two added brackets
def arch_19_expand_and_simplify_two_added_brackets(rng: random.Random) -> Dict[str, Any]:
    # 2(x + 4) + 3(2x - 1) -> 2x + 8 + 6x - 3 = 8x + 5
    ans = "8x + 5"
    prompt = (
        "Expand and simplify the sum of two bracketed expressions:\n"
        "\\[ 2(x + 4) + 3(2x - 1) \\]"
    )
    sol = (
        "**Step 1:** Expand both brackets:\n"
        "$$2x + 8 + 6x - 3$$\n\n"
        "**Step 2:** Combine like terms:\n"
        "$$(2x + 6x) + (8 - 3) = \\mathbf{8x + 5}$$"
    )
    return {
        "id": f"g7_alg2_19_{rng.randint(100000, 999999)}",
        "subskill": "19_expand_and_simplify_two_added_brackets",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_19",
        "hints": {"tier_1": "2x + 8 + 6x - 3.", "tier_2": "8x + 5.", "tier_3": ans},
        "misconception_tags": ["double_bracket_expansion_slip"]
    }


# 20. Expand and simplify two subtracted brackets
def arch_20_expand_and_simplify_two_subtracted_brackets(rng: random.Random) -> Dict[str, Any]:
    # 4(2x + 3) - 2(3x - 1) -> 8x + 12 - 6x + 2 = 2x + 14
    ans = "2x + 14"
    prompt = (
        "Expand and simplify:\n"
        "\\[ 4(2x + 3) - 2(3x - 1) \\]"
    )
    sol = (
        "**Step 1:** Expand the first bracket: $$8x + 12$$\n\n"
        "**Step 2:** Expand the second bracket with \\(-2\\):\n"
        "$$(-2) \\times 3x = -6x, \\quad (-2) \\times (-1) = +2$$\n\n"
        "**Step 3:** Combine all terms:\n"
        "$$8x + 12 - 6x + 2 = \\mathbf{2x + 14}$$"
    )
    return {
        "id": f"g7_alg2_20_{rng.randint(100000, 999999)}",
        "subskill": "20_expand_and_simplify_two_subtracted_brackets",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_20",
        "hints": {"tier_1": "Watch the negative: -2 * (-1) = +2.", "tier_2": "8x - 6x + 12 + 2 = 2x + 14.", "tier_3": ans},
        "misconception_tags": ["double_bracket_negative_sign_error"]
    }


# 21. Equivalent expressions verify by simplification
def arch_21_equivalent_expressions_verify_by_simplification(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Are the expressions \\(3(2x + 4) - 2x\\) and \\(4x + 12\\) equivalent? "
        "Show algebraic simplification to justify your answer."
    )
    sol = (
        "**Step 1:** Expand and simplify the first expression:\n"
        "$$3(2x + 4) - 2x = 6x + 12 - 2x$$\n"
        "$$= 4x + 12$$\n\n"
        "**Step 2:** Compare with second expression:\n"
        "Both simplify to \\(4x + 12\\).\n\n"
        "**Conclusion:** **Yes**, the expressions are equivalent."
    )
    ans = "Yes, both simplify to 4x + 12"
    return {
        "id": f"g7_alg2_21_{rng.randint(100000, 999999)}",
        "subskill": "21_equivalent_expressions_verify_by_simplification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_21",
        "hints": {"tier_1": "Simplify 3(2x + 4) - 2x.", "tier_2": "6x + 12 - 2x = 4x + 12.", "tier_3": ans},
        "misconception_tags": ["equivalence_verification_slip"]
    }


# 22. Equivalent expressions verify by substitution
def arch_22_equivalent_expressions_verify_by_substitution(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner claims that \\(2(x + 3) = 2x + 3\\).\n\n"
        "Test this claim by substituting \\(x = 4\\) into both sides. Is the claim true or false?"
    )
    sol = (
        "**Step 1:** Substitute \\(x = 4\\) into \\(\\text{LHS} = 2(x + 3)\\):\n"
        "$$2(4 + 3) = 2(7) = 14$$\n\n"
        "**Step 2:** Substitute \\(x = 4\\) into \\(\\text{RHS} = 2x + 3\\):\n"
        "$$2(4) + 3 = 8 + 3 = 11$$\n\n"
        "**Conclusion:** Since \\(14 \\neq 11\\), the claim is **False** "
        "(correct expansion is \\(2x + 6\\))."
    )
    ans = "False (14 != 11)"
    return {
        "id": f"g7_alg2_22_{rng.randint(100000, 999999)}",
        "subskill": "22_equivalent_expressions_verify_by_substitution",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_22",
        "hints": {"tier_1": "Evaluate 2(4+3) and 2(4)+3.", "tier_2": "14 vs 11.", "tier_3": ans},
        "misconception_tags": ["distributive_property_counterexample_failure"]
    }


# 23. Equivalent expressions identify from four choices
def arch_23_equivalent_expressions_identify_from_four_choices(rng: random.Random) -> Dict[str, Any]:
    # 5(x - 2) is equivalent to: A) 5x - 2, B) 5x - 10, C) x - 10, D) 5x + 10
    ans = "B (5x - 10)"
    prompt = (
        "Which of the following is equivalent to \\(5(x - 2)\\)?\n\n"
        "A) \\(5x - 2\\)\n"
        "B) \\(5x - 10\\)\n"
        "C) \\(x - 10\\)\n"
        "D) \\(5x + 10\\)"
    )
    sol = (
        "**Step 1:** Distribute 5 across both terms:\n"
        "$$5 \\times x - 5 \\times 2 = \\mathbf{5x - 10}$$\n\n"
        "**Correct Choice:** **B**"
    )
    return {
        "id": f"g7_alg2_23_{rng.randint(100000, 999999)}",
        "subskill": "23_equivalent_expressions_identify_from_four_choices",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg2_23",
        "hints": {"tier_1": "Multiply 5 by both x and -2.", "tier_2": "Choice B.", "tier_3": ans},
        "misconception_tags": ["distributive_multiple_choice_trap"]
    }


# 24. Perimeter of triangle algebraic simplification
def arch_24_perimeter_of_triangle_algebraic_simplification(rng: random.Random) -> Dict[str, Any]:
    # Sides: 2x + 1, 3x - 2, 4x + 5 -> P = 9x + 4
    ans = "9x + 4"
    prompt = (
        "A triangle has side lengths \\((2x + 1)\\) cm, \\((3x - 2)\\) cm, and \\((4x + 5)\\) cm.\n\n"
        "Find a simplified algebraic expression for the perimeter of the triangle."
    )
    sol = (
        "**Step 1:** Add all three sides:\n"
        "$$P = (2x + 1) + (3x - 2) + (4x + 5)$$\n\n"
        "**Step 2:** Combine like terms:\n"
        "$$P = (2x + 3x + 4x) + (1 - 2 + 5) = \\mathbf{9x + 4}$$"
    )
    return {
        "id": f"g7_alg2_24_{rng.randint(100000, 999999)}",
        "subskill": "24_perimeter_of_triangle_algebraic_simplification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_24",
        "hints": {"tier_1": "Add the x-terms: 2x+3x+4x. Add constants: 1-2+5.", "tier_2": "9x + 4.", "tier_3": ans},
        "misconception_tags": ["triangle_perimeter_algebraic_collection_slip"]
    }


# 25. Perimeter of rectangle algebraic simplification
def arch_25_perimeter_of_rectangle_algebraic_simplification(rng: random.Random) -> Dict[str, Any]:
    # Length 3x + 2, width x + 5 -> P = 2(3x + 2) + 2(x + 5) = 6x + 4 + 2x + 10 = 8x + 14
    ans = "8x + 14"
    prompt = (
        "A rectangle has length \\((3x + 2)\\) cm and width \\((x + 5)\\) cm.\n\n"
        "Write a simplified algebraic expression for its perimeter \\(P\\)."
    )
    sol = (
        "**Step 1:** Use perimeter formula \\(P = 2l + 2w\\):\n"
        "$$P = 2(3x + 2) + 2(x + 5)$$\n\n"
        "**Step 2:** Expand brackets:\n"
        "$$P = 6x + 4 + 2x + 10$$\n\n"
        "**Step 3:** Combine like terms:\n"
        "$$P = \\mathbf{8x + 14}$$"
    )
    return {
        "id": f"g7_alg2_25_{rng.randint(100000, 999999)}",
        "subskill": "25_perimeter_of_rectangle_algebraic_simplification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_25",
        "hints": {"tier_1": "2(length) + 2(width).", "tier_2": "2(3x+2) + 2(x+5) = 8x + 14.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_double_both_dimensions_in_perimeter"]
    }
