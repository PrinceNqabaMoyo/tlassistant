"""Grade 7 Mathematics - Algebraic Expressions 2: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 2/04. Algebraic expressions 2.md
Focus: Geometric perimeter & area expressions, fractional/decimal like terms, powers, algebraic word problems, error traps, and diagnostic autopsy.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Perimeter of square algebraic simplification
def arch_26_perimeter_of_square_algebraic_simplification(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(2, 5)
    k = rng.randint(1, 6)
    sign = rng.choice(["+", "-"])
    if sign == "+":
        ans = f"{4 * c}x + {4 * k}"
        expr = f"{c}x + {k}"
        step2 = f"4({c}x + {k}) = 4 \\times {c}x + 4 \\times {k} = {ans}"
    else:
        ans = f"{4 * c}x - {4 * k}"
        expr = f"{c}x - {k}"
        step2 = f"4({c}x - {k}) = 4 \\times {c}x - 4 \\times {k} = {ans}"
    prompt = (
        f"A square has side length \\(({expr})\\) cm.\n\n"
        f"Write a simplified algebraic expression for its perimeter \\(P\\)."
    )
    sol = (
        f"**Step 1:** The perimeter of a square is 4 times the side length:\n"
        f"$$P = 4s = 4({expr})$$\n\n"
        f"**Step 2:** Expand using the distributive property:\n"
        f"$${step2}$$\n\n"
        f"Perimeter: **\\({ans}\\) cm**."
    )
    return {
        "id": f"g7_alg2_26_{rng.randint(100000, 999999)}",
        "subskill": "26_perimeter_of_square_algebraic_simplification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_26",
        "hints": {"tier_1": "Multiply the side length by 4.", "tier_2": f"4({expr}) = {ans}.", "tier_3": ans},
        "misconception_tags": ["multiplying_only_the_first_term_by_four"]
    }


# 27. Perimeter of equilateral triangle algebraic
def arch_27_perimeter_of_equilateral_triangle_algebraic(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(2, 6)
    k = rng.randint(2, 7)
    ans = f"{3 * c}a + {3 * k}"
    prompt = (
        f"An equilateral triangle has side length \\(({c}a + {k})\\) mm.\n\n"
        f"Write down a simplified algebraic expression for its perimeter."
    )
    sol = (
        f"**Step 1:** An equilateral triangle has 3 equal sides:\n"
        f"$$P = 3 \\times ({c}a + {k})$$\n\n"
        f"**Step 2:** Distribute the factor 3:\n"
        f"$$P = 3({c}a) + 3({k}) = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_27_{rng.randint(100000, 999999)}",
        "subskill": "27_perimeter_of_equilateral_triangle_algebraic",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_27",
        "hints": {"tier_1": "Multiply the side length by 3.", "tier_2": f"3({c}a + {k}) = {ans}.", "tier_3": ans},
        "misconception_tags": ["adding_instead_of_multiplying_three_sides"]
    }


# 28. Perimeter of regular pentagon algebraic
def arch_28_perimeter_of_regular_pentagon_algebraic(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(2, 4)
    k = rng.randint(1, 5)
    ans = f"{5 * c}y - {5 * k}"
    prompt = (
        f"A regular pentagon has five equal sides, each of length \\(({c}y - {k})\\) cm.\n\n"
        f"Write a simplified expression for the perimeter of the pentagon."
    )
    sol = (
        f"**Step 1:** A regular pentagon has 5 equal sides:\n"
        f"$$P = 5 \\times ({c}y - {k})$$\n\n"
        f"**Step 2:** Distribute 5 to both terms inside the bracket:\n"
        f"$$P = 5({c}y) - 5({k}) = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_28_{rng.randint(100000, 999999)}",
        "subskill": "28_perimeter_of_regular_pentagon_algebraic",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_28",
        "hints": {"tier_1": "A regular pentagon has 5 equal sides.", "tier_2": f"5({c}y - {k}) = {ans}.", "tier_3": ans},
        "misconception_tags": ["confusing_pentagon_with_hexagon"]
    }


# 29. Perimeter of regular hexagon algebraic
def arch_29_perimeter_of_regular_hexagon_algebraic(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(2, 5)
    k = rng.randint(1, 4)
    ans = f"{6 * c}m + {6 * k}"
    prompt = (
        f"A regular hexagon has sides of length \\(({c}m + {k})\\) metres.\n\n"
        f"Determine the simplified expression for its perimeter."
    )
    sol = (
        f"**Step 1:** A regular hexagon has 6 equal sides:\n"
        f"$$P = 6 \\times ({c}m + {k})$$\n\n"
        f"**Step 2:** Expand the bracket:\n"
        f"$$P = 6({c}m) + 6({k}) = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_29_{rng.randint(100000, 999999)}",
        "subskill": "29_perimeter_of_regular_hexagon_algebraic",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_29",
        "hints": {"tier_1": "Hexagon has 6 sides.", "tier_2": f"6({c}m + {k}) = {ans}.", "tier_3": ans},
        "misconception_tags": ["distributive_bracket_expansion_error"]
    }


# 30. Perimeter of composite L-shape algebraic
def arch_30_perimeter_of_composite_l_shape_algebraic(rng: random.Random) -> Dict[str, Any]:
    # L-shape: horizontal outer = 3x + 4, vertical outer = 2x + 5.
    # Total perimeter = 2(horizontal outer + vertical outer) = 2(3x + 4 + 2x + 5) = 2(5x + 9) = 10x + 18
    ans = "10x + 18"
    prompt = (
        "An L-shaped polygon has overall width \\((3x + 4)\\) cm and overall height \\((2x + 5)\\) cm.\n"
        "All corners meet at right angles.\n\n"
        "Find the simplified algebraic expression for the total perimeter of the L-shape."
    )
    sol = (
        "**Step 1:** In any rectilinear polygon (meeting at right angles), the sum of the horizontal steps "
        "equals the total width, and the sum of the vertical steps equals the total height.\n\n"
        "**Step 2:** Therefore, the total perimeter is equivalent to a rectangle with dimensions \\((3x + 4)\\) by \\((2x + 5)\\):\n"
        "$$P = 2(3x + 4) + 2(2x + 5)$$\n\n"
        "**Step 3:** Expand and collect like terms:\n"
        "$$P = 6x + 8 + 4x + 10 = \\mathbf{10x + 18}$$"
    )
    return {
        "id": f"g7_alg2_30_{rng.randint(100000, 999999)}",
        "subskill": "30_perimeter_of_composite_l_shape_algebraic",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_30",
        "hints": {"tier_1": "Perimeter = 2(width + height) for rectilinear L-shape.", "tier_2": "2(3x + 4) + 2(2x + 5).", "tier_3": ans},
        "misconception_tags": ["attempting_to_subtract_inner_corners_from_perimeter"]
    }


# 31. Area of rectangle monomial by binomial
def arch_31_area_of_rectangle_monomial_by_binomial(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(2, 6)
    c = rng.randint(2, 5)
    k = rng.randint(3, 8)
    ans = f"{w * c}x + {w * k}"
    prompt = (
        f"A rectangle has width \\({w}\\) cm and length \\(({c}x + {k})\\) cm.\n\n"
        f"Write down a simplified algebraic expression for the area \\(A\\) of the rectangle."
    )
    sol = (
        f"**Step 1:** Use the area formula \\(A = \\text{{length}} \\times \\text{{width}}\\):\n"
        f"$$A = {w} \\times ({c}x + {k})$$\n\n"
        f"**Step 2:** Apply the distributive law:\n"
        f"$$A = {w}({c}x) + {w}({k}) = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_31_{rng.randint(100000, 999999)}",
        "subskill": "31_area_of_rectangle_monomial_by_binomial",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_31",
        "hints": {"tier_1": "Area = length × width.", "tier_2": f"{w}({c}x + {k}) = {ans}.", "tier_3": ans},
        "misconception_tags": ["confusing_area_with_perimeter_formula"]
    }


# 32. Area of square algebraic side length
def arch_32_area_of_square_algebraic_side_length(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(2, 7)
    ans = f"{c * c}x^2"
    prompt = (
        f"A square has side length \\({c}x\\) cm.\n\n"
        f"Determine the simplified expression for its area."
    )
    sol = (
        f"**Step 1:** Area of a square is \\(\\text{{side}}^2\\):\n"
        f"$$A = ({c}x)^2 = ({c}x) \\times ({c}x)$$\n\n"
        f"**Step 2:** Multiply numerical coefficients and variable powers:\n"
        f"$$A = ({c} \\times {c}) \\times (x \\times x) = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_32_{rng.randint(100000, 999999)}",
        "subskill": "32_area_of_square_algebraic_side_length",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_32",
        "hints": {"tier_1": "Square both the coefficient and the variable.", "tier_2": f"({c}x) × ({c}x) = {c*c}x^2.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_square_the_coefficient"]
    }


# 33. Fractional coefficients collecting like terms
def arch_33_fractional_coefficients_collecting_like_terms(rng: random.Random) -> Dict[str, Any]:
    # 1/2 x + 1/4 x = 3/4 x
    ans = "3/4x"
    prompt = (
        "Simplify the algebraic expression by combining like terms:\n"
        "\\[ \\frac{1}{2}x + \\frac{1}{4}x \\]"
    )
    sol = (
        "**Step 1:** Find a common denominator for the fractional coefficients (LCD = 4):\n"
        "$$\\frac{1}{2} = \\frac{2}{4}$$\n\n"
        "**Step 2:** Add the numerators:\n"
        "$$\\left(\\frac{2}{4} + \\frac{1}{4}\\right)x = \\mathbf{\\frac{3}{4}x}$$"
    )
    return {
        "id": f"g7_alg2_33_{rng.randint(100000, 999999)}",
        "subskill": "33_fractional_coefficients_collecting_like_terms",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_33",
        "hints": {"tier_1": "Convert 1/2 to 2/4.", "tier_2": "2/4 + 1/4 = 3/4.", "tier_3": ans},
        "misconception_tags": ["adding_numerators_and_denominators_directly"]
    }


# 34. Fractional coefficients subtraction
def arch_34_fractional_coefficients_subtraction(rng: random.Random) -> Dict[str, Any]:
    # 5/6 y - 1/3 y = 5/6 y - 2/6 y = 3/6 y = 1/2 y
    ans = "1/2y"
    prompt = (
        "Simplify the algebraic expression:\n"
        "\\[ \\frac{5}{6}y - \\frac{1}{3}y \\]"
    )
    sol = (
        "**Step 1:** Convert \\(\\frac{1}{3}\\) to an equivalent fraction with denominator 6:\n"
        "$$\\frac{1}{3} = \\frac{2}{6}$$\n\n"
        "**Step 2:** Subtract coefficients:\n"
        "$$\\left(\\frac{5}{6} - \\frac{2}{6}\\right)y = \\frac{3}{6}y = \\mathbf{\\frac{1}{2}y}$$"
    )
    return {
        "id": f"g7_alg2_34_{rng.randint(100000, 999999)}",
        "subskill": "34_fractional_coefficients_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_34",
        "hints": {"tier_1": "Express 1/3 as 2/6.", "tier_2": "5/6 - 2/6 = 3/6 = 1/2.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_simplify_fractional_coefficient"]
    }


# 35. Decimal coefficients addition
def arch_35_decimal_coefficients_addition(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([0.3, 0.4, 0.6, 0.7])
    b = rng.choice([1.1, 1.2, 1.5, 2.3])
    total = round(a + b, 1)
    ans = f"{total}x"
    prompt = (
        f"Simplify the following expression by collecting like terms:\n"
        f"\\[ {a}x + {b}x \\]"
    )
    sol = (
        f"**Step 1:** Add the decimal coefficients:\n"
        f"$$({a} + {b})x = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_35_{rng.randint(100000, 999999)}",
        "subskill": "35_decimal_coefficients_addition",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg2_35",
        "hints": {"tier_1": f"Add {a} and {b}.", "tier_2": f"({a} + {b})x = {ans}.", "tier_3": ans},
        "misconception_tags": ["decimal_point_misalignment_addition"]
    }


# 36. Decimal coefficients subtraction
def arch_36_decimal_coefficients_subtraction(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([4.5, 3.8, 5.2, 6.7])
    b = rng.choice([1.2, 1.5, 2.1, 2.3])
    diff = round(a - b, 1)
    ans = f"{diff}m"
    prompt = (
        f"Simplify the expression:\n"
        f"\\[ {a}m - {b}m \\]"
    )
    sol = (
        f"**Step 1:** Subtract the decimal coefficients:\n"
        f"$$({a} - {b})m = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_36_{rng.randint(100000, 999999)}",
        "subskill": "36_decimal_coefficients_subtraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_alg2_36",
        "hints": {"tier_1": f"Calculate {a} - {b}.", "tier_2": f"({a} - {b})m = {ans}.", "tier_3": ans},
        "misconception_tags": ["decimal_borrowing_subtraction_error"]
    }


# 37. Like terms with squared variables
def arch_37_like_terms_with_squared_variables(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(4, 9)
    c2 = rng.randint(2, 5)
    c3 = rng.randint(1, 4)
    res = c1 + c2 - c3
    ans = f"{res}x^2"
    prompt = (
        f"Simplify the following expression:\n"
        f"\\[ {c1}x^2 + {c2}x^2 - {c3}x^2 \\]"
    )
    sol = (
        f"**Step 1:** Notice that all terms have the exact same variable part \\(x^2\\), so they are like terms:\n"
        f"$$({c1} + {c2} - {c3})x^2$$\n\n"
        f"**Step 2:** Combine coefficients: \\({c1} + {c2} - {c3} = {res}\\).\n\n"
        f"Result: **\\({ans}\\)**."
    )
    return {
        "id": f"g7_alg2_37_{rng.randint(100000, 999999)}",
        "subskill": "37_like_terms_with_squared_variables",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_37",
        "hints": {"tier_1": "All terms share x^2.", "tier_2": f"({c1} + {c2} - {c3})x^2 = {ans}.", "tier_3": ans},
        "misconception_tags": ["adding_powers_when_collecting_like_terms"]
    }


# 38. Distinguishing x and x squared terms
def arch_38_distinguishing_x_and_x_squared_terms(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.randint(3, 7)
    a2 = rng.randint(2, 5)
    b1 = rng.randint(2, 6)
    b2 = rng.randint(3, 7)
    tot_sq = a1 + a2
    tot_lin = b1 + b2
    ans = f"{tot_sq}x^2 + {tot_lin}x"
    prompt = (
        f"Simplify by collecting like terms:\n"
        f"\\[ {a1}x^2 + {b1}x + {a2}x^2 + {b2}x \\]"
    )
    sol = (
        f"**Step 1:** Group \\(x^2\\) terms together and \\(x\\) terms together:\n"
        f"$$({a1}x^2 + {a2}x^2) + ({b1}x + {b2}x)$$\n\n"
        f"**Step 2:** Combine each group:\n"
        f"$$({a1} + {a2})x^2 + ({b1} + {b2})x = \\mathbf{{{ans}}}$$\n\n"
        f"*(Note: \\(x^2\\) and \\(x\\) are unlike terms and cannot be added together).* "
    )
    return {
        "id": f"g7_alg2_38_{rng.randint(100000, 999999)}",
        "subskill": "38_distinguishing_x_and_x_squared_terms",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_38",
        "hints": {"tier_1": "x^2 and x are different terms.", "tier_2": f"Combine {a1}x^2+{a2}x^2 and {b1}x+{b2}x.", "tier_3": ans},
        "misconception_tags": ["combining_x_and_x_squared_terms"]
    }


# 39. Cubed and squared terms combining
def arch_39_cubed_and_squared_terms_combining(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(4, 8)
    c2 = rng.randint(2, 3)
    s1 = rng.randint(3, 6)
    s2 = rng.randint(2, 4)
    tot_c = c1 - c2
    tot_s = s1 + s2
    ans = f"{tot_c}x^3 + {tot_s}x^2"
    prompt = (
        f"Simplify the following expression:\n"
        f"\\[ {c1}x^3 + {s1}x^2 - {c2}x^3 + {s2}x^2 \\]"
    )
    sol = (
        f"**Step 1:** Group cubic \\(x^3\\) terms and quadratic \\(x^2\\) terms:\n"
        f"$$({c1}x^3 - {c2}x^3) + ({s1}x^2 + {s2}x^2)$$\n\n"
        f"**Step 2:** Combine like terms:\n"
        f"$$({c1} - {c2})x^3 + ({s1} + {s2})x^2 = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_39_{rng.randint(100000, 999999)}",
        "subskill": "39_cubed_and_squared_terms_combining",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_39",
        "hints": {"tier_1": "Group x^3 terms together and x^2 terms together.", "tier_2": f"{c1-c2}x^3 + {s1+s2}x^2.", "tier_3": ans},
        "misconception_tags": ["adding_different_power_terms_together"]
    }


# 40. Algebraic word problem consecutive integers
def arch_40_algebraic_word_problem_consecutive_integers(rng: random.Random) -> Dict[str, Any]:
    ans = "3n + 3"
    prompt = (
        "Let \\(n\\) represent the first of three consecutive integers.\n\n"
        "1. Write down expressions for the next two consecutive integers in terms of \\(n\\).\n"
        "2. Write a simplified expression for the sum of all three consecutive integers."
    )
    sol = (
        "**Step 1:** Consecutive integers increase by 1:\n"
        "- First integer: \\(n\\)\n"
        "- Second integer: \\(n + 1\\)\n"
        "- Third integer: \\(n + 2\\)\n\n"
        "**Step 2:** Add all three integers together:\n"
        "$$\\text{Sum} = n + (n + 1) + (n + 2)$$\n\n"
        "**Step 3:** Group like terms:\n"
        "$$\\text{Sum} = (n + n + n) + (1 + 2) = \\mathbf{3n + 3}$$"
    )
    return {
        "id": f"g7_alg2_40_{rng.randint(100000, 999999)}",
        "subskill": "40_algebraic_word_problem_consecutive_integers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_40",
        "hints": {"tier_1": "Consecutive integers are n, n+1, and n+2.", "tier_2": "Add them: n + n + 1 + n + 2 = 3n + 3.", "tier_3": ans},
        "misconception_tags": ["consecutive_numbers_step_error"]
    }


# 41. Algebraic word problem ages in years
def arch_41_algebraic_word_problem_ages_in_years(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([3, 4])
    extra = rng.randint(2, 6)
    ans = f"{mult + 1}x + {extra}"
    prompt = (
        f"Thabo is \\(x\\) years old. His father is \\({extra}\\) years older than \\({mult}\\) times Thabo's age.\n\n"
        f"Write a simplified algebraic expression for the sum of their ages."
    )
    sol = (
        f"**Step 1:** Write the expression for the father's age:\n"
        f"$$\\text{{Father's age}} = {mult}x + {extra}$$\n\n"
        f"**Step 2:** Add Thabo's age to his father's age:\n"
        f"$$\\text{{Total age}} = x + ({mult}x + {extra})$$\n\n"
        f"**Step 3:** Combine like terms:\n"
        f"$$\\text{{Total age}} = (1 + {mult})x + {extra} = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_41_{rng.randint(100000, 999999)}",
        "subskill": "41_algebraic_word_problem_ages_in_years",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_41",
        "hints": {"tier_1": f"Father = {mult}x + {extra}.", "tier_2": f"Total = x + {mult}x + {extra} = {ans}.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_include_thabos_own_age_in_sum"]
    }


# 42. Algebraic word problem shopping cost
def arch_42_algebraic_word_problem_shopping_cost(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.randint(2, 4)
    p1 = rng.randint(3, 5)
    n2 = rng.randint(1, 3)
    p2 = rng.randint(2, 4)
    tot_n = n1 + n2
    tot_p = p1 + p2
    ans = f"{tot_n}x + {tot_p}y"
    prompt = (
        f"A notebook costs \\(x\\) rands and a pen costs \\(y\\) rands.\n"
        f"On Monday, a school buys \\({n1}\\) notebooks and \\({p1}\\) pens.\n"
        f"On Friday, they buy \\({n2}\\) more notebooks and \\({p2}\\) more pens.\n\n"
        f"Write a simplified algebraic expression for the total cost of all the items purchased."
    )
    sol = (
        f"**Step 1:** Write the cost for each day:\n"
        f"- Monday: \\({n1}x + {p1}y\\)\n"
        f"- Friday: \\({n2}x + {p2}y\\)\n\n"
        f"**Step 2:** Combine like terms:\n"
        f"$$\\text{{Total}} = ({n1}x + {n2}x) + ({p1}y + {p2}y) = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_42_{rng.randint(100000, 999999)}",
        "subskill": "42_algebraic_word_problem_shopping_cost",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_42",
        "hints": {"tier_1": "Combine the notebooks (x) and pens (y).", "tier_2": f"({n1}+{n2})x + ({p1}+{p2})y = {ans}.", "tier_3": ans},
        "misconception_tags": ["combining_different_item_cost_variables"]
    }


# 43. Algebraic word problem travel distance
def arch_43_algebraic_word_problem_travel_distance(rng: random.Random) -> Dict[str, Any]:
    s1 = 60
    s2 = 80
    ans = "140t - 80"
    prompt = (
        "A car travels at \\(60\\text{ km/h}\\) for \\(t\\) hours in the morning, "
        "and at \\(80\\text{ km/h}\\) for \\((t - 1)\\) hours in the afternoon.\n\n"
        "Write a simplified algebraic expression for the total distance travelled by the car."
    )
    sol = (
        "**Step 1:** Use \\(\\text{Distance} = \\text{speed} \\times \\text{time}\\):\n"
        "- Morning distance: \\(60t\\)\n"
        "- Afternoon distance: \\(80(t - 1) = 80t - 80\\)\n\n"
        "**Step 2:** Add the distances and simplify:\n"
        "$$\\text{Total} = 60t + 80t - 80 = \\mathbf{140t - 80}$$"
    )
    return {
        "id": f"g7_alg2_43_{rng.randint(100000, 999999)}",
        "subskill": "43_algebraic_word_problem_travel_distance",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_43",
        "hints": {"tier_1": "Total = 60t + 80(t - 1).", "tier_2": "60t + 80t - 80 = 140t - 80.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_expand_bracket_in_distance"]
    }


# 44. Substitution into simplified expression
def arch_44_substitution_into_simplified_expression(rng: random.Random) -> Dict[str, Any]:
    # 3(2x + 4) - 2(x - 1) = 6x + 12 - 2x + 2 = 4x + 14. For x = 3: 4(3) + 14 = 26
    x_val = rng.choice([2, 3, 4])
    ans_val = 4 * x_val + 14
    ans = str(ans_val)
    prompt = (
        f"1. Simplify the expression by expanding brackets and combining like terms:\n"
        f"\\[ 3(2x + 4) - 2(x - 1) \\]\n\n"
        f"2. Hence, calculate its value when \\(x = {x_val}\\)."
    )
    sol = (
        f"**Step 1:** Expand both sets of brackets:\n"
        f"$$3(2x + 4) = 6x + 12$$\n"
        f"$$-2(x - 1) = -2x + 2$$\n\n"
        f"**Step 2:** Combine like terms:\n"
        f"$$6x - 2x + 12 + 2 = 4x + 14$$\n\n"
        f"**Step 3:** Substitute \\(x = {x_val}\\):\n"
        f"$$4({x_val}) + 14 = {4 * x_val} + 14 = \\mathbf{{{ans}}}$$"
    )
    return {
        "id": f"g7_alg2_44_{rng.randint(100000, 999999)}",
        "subskill": "44_substitution_into_simplified_expression",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_44",
        "hints": {"tier_1": "Simplified form is 4x + 14.", "tier_2": f"4({x_val}) + 14 = {ans_val}.", "tier_3": ans},
        "misconception_tags": ["sign_error_expanding_negative_bracket"]
    }


# 45. Verify algebraic identity for multiple values
def arch_45_verify_algebraic_identity_for_multiple_values(rng: random.Random) -> Dict[str, Any]:
    ans = "Both expressions evaluate to 16 for x = 1, and to 34 for x = 4; hence equivalent."
    prompt = (
        "Consider the two algebraic expressions:\n"
        "Expression A: \\(2(3x + 5)\\)\n"
        "Expression B: \\(6x + 10\\)\n\n"
        "Verify that these expressions are equivalent by calculating their values for:\n"
        "a) \\(x = 1\\)\n"
        "b) \\(x = 4\\)"
    )
    sol = (
        "**Step 1:** Test \\(x = 1\\):\n"
        "- Expression A: \\(2(3(1) + 5) = 2(3 + 5) = 2(8) = 16\\)\n"
        "- Expression B: \\(6(1) + 10 = 6 + 10 = 16\\)\n"
        "Both equal 16.\n\n"
        "**Step 2:** Test \\(x = 4\\):\n"
        "- Expression A: \\(2(3(4) + 5) = 2(12 + 5) = 2(17) = 34\\)\n"
        "- Expression B: \\(6(4) + 10 = 24 + 10 = 34\\)\n"
        "Both equal 34.\n\n"
        "**Conclusion:** Both expressions yield identical values, verifying equivalence."
    )
    return {
        "id": f"g7_alg2_45_{rng.randint(100000, 999999)}",
        "subskill": "45_verify_algebraic_identity_for_multiple_values",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_45",
        "hints": {"tier_1": "Substitute x=1 into both, then x=4 into both.", "tier_2": "For x=1: both equal 16; for x=4: both equal 34.", "tier_3": ans},
        "misconception_tags": ["arithmetic_order_of_operations_in_bracket_substitution"]
    }


# 46. Common error adding unlike terms trap
def arch_46_common_error_adding_unlike_terms_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "3x and 4 are unlike terms and cannot be added to form 7x."
    prompt = (
        "A learner claims that \\(3x + 4 = 7x\\).\n\n"
        "1. Is this claim correct? (Yes / No)\n"
        "2. Explain why, using the concept of like and unlike terms."
    )
    sol = (
        "**Step 1:** The claim is **No (incorrect)**.\n\n"
        "**Step 2:** Explanation:\n"
        "- \\(3x\\) is a variable term with coefficient 3.\n"
        "- \\(4\\) is a constant term with no variable.\n"
        "- Terms can only be combined if they have the exact same variable parts (like terms).\n"
        "- For example, if \\(x = 2\\), \\(3(2) + 4 = 10\\), but \\(7(2) = 14\\). They are not equal!"
    )
    return {
        "id": f"g7_alg2_46_{rng.randint(100000, 999999)}",
        "subskill": "46_common_error_adding_unlike_terms_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_46",
        "hints": {"tier_1": "Can you add a number of apples to a number without apples?", "tier_2": "3x and 4 are unlike terms.", "tier_3": ans},
        "misconception_tags": ["adding_constants_directly_to_variable_coefficients"]
    }


# 47. Common error distributive law omission trap
def arch_47_common_error_distributive_law_omission_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: 3 was not multiplied by 5. Correct expression is 3x + 15."
    prompt = (
        "A student wrote: \\(3(x + 5) = 3x + 5\\).\n\n"
        "1. Identify the error in the student's working.\n"
        "2. Write down the correct simplified expression."
    )
    sol = (
        "**Step 1:** Identify the error:\n"
        "The student multiplied the first term \\(x\\) by 3, but forgot to multiply the second term \\(5\\) by 3.\n\n"
        "**Step 2:** Correct expansion using the distributive property:\n"
        "$$3(x + 5) = 3 \\times x + 3 \\times 5 = \\mathbf{3x + 15}$$"
    )
    return {
        "id": f"g7_alg2_47_{rng.randint(100000, 999999)}",
        "subskill": "47_common_error_distributive_law_omission_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_47",
        "hints": {"tier_1": "The number outside the bracket multiplies EVERY term inside.", "tier_2": "3 × 5 = 15, so 3x + 15.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_multiply_second_bracket_term"]
    }


# 48. Common error sign change subtraction trap
def arch_48_common_error_sign_change_subtraction_trap(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: -(-3) should be +3. Correct expression is 3x + 3."
    prompt = (
        "A student simplified an expression as follows:\n"
        "\\[ 5x - (2x - 3) = 5x - 2x - 3 = 3x - 3 \\]\n\n"
        "1. Point out the mistake made in handling the negative sign.\n"
        "2. Write down the correct simplified expression."
    )
    sol = (
        "**Step 1:** Identify the error:\n"
        "The negative sign outside the bracket applies to BOTH terms inside.\n"
        "Multiplying \\(-1 \\times (-3)\\) yields \\(+3\\), not \\(-3\\).\n\n"
        "**Step 2:** Correct simplification:\n"
        "$$5x - (2x - 3) = 5x - 2x + 3 = \\mathbf{3x + 3}$$"
    )
    return {
        "id": f"g7_alg2_48_{rng.randint(100000, 999999)}",
        "subskill": "48_common_error_sign_change_subtraction_trap",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_alg2_48",
        "hints": {"tier_1": "Subtracting a negative number gives a positive.", "tier_2": "-(2x - 3) = -2x + 3.", "tier_3": ans},
        "misconception_tags": ["negative_sign_bracket_distribution_error"]
    }


# 49. Nested algebraic simplification
def arch_49_nested_algebraic_simplification(rng: random.Random) -> Dict[str, Any]:
    # 2[3(x + 2) + 4] = 2[3x + 6 + 4] = 2[3x + 10] = 6x + 20
    ans = "6x + 20"
    prompt = (
        "Simplify the algebraic expression containing nested brackets:\n"
        "\\[ 2[3(x + 2) + 4] \\]"
    )
    sol = (
        "**Step 1:** Work inside the square brackets first (expand round brackets):\n"
        "$$3(x + 2) = 3x + 6$$\n"
        "So inside brackets: \\(3x + 6 + 4 = 3x + 10\\)\n\n"
        "**Step 2:** Multiply the whole inner expression by 2:\n"
        "$$2(3x + 10) = 2(3x) + 2(10) = \\mathbf{6x + 20}$$"
    )
    return {
        "id": f"g7_alg2_49_{rng.randint(100000, 999999)}",
        "subskill": "49_nested_algebraic_simplification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_alg2_49",
        "hints": {"tier_1": "Expand inner round brackets first.", "tier_2": "2(3x + 10) = 6x + 20.", "tier_3": ans},
        "misconception_tags": ["order_of_operations_with_nested_brackets"]
    }


# 50. Comprehensive diagnostic autopsy
def arch_50_algebraic_expressions_2_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    ans = "a) 7x + 11; b) 2x + 14; c) 35"
    prompt = (
        "**Comprehensive Algebraic Expressions 2 Diagnostic Autopsy**\n\n"
        "1. Simplify by combining like terms: \\(4x + 6 + 3x + 5\\).\n"
        "2. Expand and simplify: \\(5(x + 2) - 3(x - 1) + 1\\).\n"
        "3. If \\(x = 3\\), calculate the numerical value of your answer to (1)."
    )
    sol = (
        "**Question 1:**\n"
        "$$4x + 3x + 6 + 5 = \\mathbf{7x + 11}$$\n\n"
        "**Question 2:**\n"
        "$$5(x + 2) - 3(x - 1) + 1 = 5x + 10 - 3x + 3 + 1$$\n"
        "$$= (5x - 3x) + (10 + 3 + 1) = \\mathbf{2x + 14}$$\n\n"
        "**Question 3:**\n"
        "Substitute \\(x = 3\\) into \\(7x + 11\\):\n"
        "$$7(3) + 11 = 21 + 11 = \\mathbf{35}$$"
    )
    return {
        "id": f"g7_alg2_50_{rng.randint(100000, 999999)}",
        "subskill": "50_algebraic_expressions_2_comprehensive_diagnostic_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "learning_objective_id": "math_g7_alg2_50",
        "hints": {
            "tier_1": "1: Combine x terms and numbers. 2: Watch -3(-1) = +3. 3: 7(3) + 11.",
            "tier_2": "1: 7x + 11. 2: 2x + 14. 3: 21 + 11 = 35.",
            "tier_3": ans
        },
        "misconception_tags": [
            "adding_constants_directly_to_variable_coefficients",
            "negative_sign_bracket_distribution_error",
            "substitution_arithmetic_error"
        ]
    }
