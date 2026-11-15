"""Grade 10 Mathematics — Term 1 — Equations and Inequalities: Archetypes 26 to 50.
Grounded in CAPS curriculum_docs_auto/Mathematics_Gr10/Term 1/04. Equations and inequalities.md
Focus: Simultaneous equations (elimination, fractions, geometry), Word problems (numbers, age, perimeter, speed, financial),
Literal equations (change of subject, physics/financial formulas), and Linear Inequalities (reversal, compound, SVG number line, interval notation).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Simultaneous linear substitution rearranging first: x - ay = b and cx + dy = e
def arch_26_simultaneous_linear_substitution_rearranging_first(rng: random.Random) -> Dict[str, Any]:
    # x - a*y = b => x = a*y + b
    a = rng.choice([2, 3])
    y_val = rng.randint(1, 5)
    b = rng.randint(-5, 5)
    x_val = a * y_val + b
    # eq2: c*x + d*y = e
    c = rng.choice([2, 3])
    d = rng.choice([2, 4, 5])
    e = c * x_val + d * y_val

    sign_b = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sign_ay = f"- {a}y"

    prompt = (
        f"Solve simultaneously for \\(x\\) and \\(y\\) using the substitution method:\n"
        f"\\[ (1) \\quad x {sign_ay} = {b} \\]\n"
        f"\\[ (2) \\quad {c}x + {d}y = {e} \\]"
    )
    ans = f"x = {x_val}, y = {y_val}"
    rearranged_str = f"x = {a}y {sign_b}"

    sol = (
        f"**Step 1:** From equation (1), isolate \\(x\\):\n"
        f"\\[ {rearranged_str} \\]\n\n"
        f"**Step 2:** Substitute into equation (2):\n"
        f"\\[ {c}({a}y {sign_b}) + {d}y = {e} \\]\n"
        f"\\[ {c * a}y {'+' if c*b>=0 else '-'} {abs(c*b)} + {d}y = {e} \\]\n"
        f"\\[ {c * a + d}y = {e - c * b} \\]\n"
        f"\\[ y = {y_val} \\]\n\n"
        f"**Step 3:** Substitute \\(y = {y_val}\\) back to find \\(x\\):\n"
        f"\\[ x = {a}({y_val}) {sign_b} = {x_val} \\]\n\n"
        f"**Solution:** \\(x = {x_val},\\; y = {y_val}\\)"
    )
    return {
        "id": f"g10_eq_26_{rng.randint(100000, 999999)}",
        "subskill": "26_simultaneous_linear_substitution_rearranging_first",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"x = {x_val}, y = {y_val}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_eq_26",
        "misconception_tags": ["rearranging_variable_sign_error", "omitting_second_variable"],
        "marking_schema": [
            {"step": 1, "criterion": "Make x the subject of equation (1)", "marks": 1},
            {"step": 2, "criterion": "Substitute into (2) and solve for y", "marks": 2},
            {"step": 3, "criterion": "Solve for x and state solution", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Rearrange equation (1) to get {rearranged_str}.",
            "tier_2": f"Substitute ({a}y {sign_b}) in place of x in equation (2).",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_26_simultaneous_linear_substitution_rearranging_first",
    }


# 27. Simultaneous linear elimination direct addition: ax + by = c and dx - by = f
def arch_27_simultaneous_linear_elimination_direct_addition(rng: random.Random) -> Dict[str, Any]:
    # Opposite y coefficients (+b and -b)
    b = rng.choice([2, 3, 4, 5])
    a = rng.choice([2, 3, 4])
    d = rng.choice([1, 2, 3])
    x_val = rng.randint(1, 6)
    y_val = rng.randint(1, 6)
    c = a * x_val + b * y_val
    f = d * x_val - b * y_val

    prompt = (
        f"Solve simultaneously using the **elimination method**:\n"
        f"\\[ (1) \\quad {a}x + {b}y = {c} \\]\n"
        f"\\[ (2) \\quad {d}x - {b}y = {f} \\]"
    )
    ans = f"x = {x_val}, y = {y_val}"
    sum_a_d = a + d
    sum_c_f = c + f

    sol = (
        f"**Step 1:** Add equation (1) and equation (2) to eliminate \\(y\\):\n"
        f"\\[ ({a}x + {d}x) + ({b}y - {b}y) = {c} + {f} \\]\n"
        f"\\[ {sum_a_d}x = {sum_c_f} \\]\n"
        f"\\[ x = \\frac{{{sum_c_f}}}{{{sum_a_d}}} = {x_val} \\]\n\n"
        f"**Step 2:** Substitute \\(x = {x_val}\\) into equation (1):\n"
        f"\\[ {a}({x_val}) + {b}y = {c} \\]\n"
        f"\\[ {a * x_val} + {b}y = {c} \\]\n"
        f"\\[ {b}y = {c - a * x_val} \\]\n"
        f"\\[ y = {y_val} \\]\n\n"
        f"**Solution:** \\(x = {x_val},\\; y = {y_val}\\)"
    )
    return {
        "id": f"g10_eq_27_{rng.randint(100000, 999999)}",
        "subskill": "27_simultaneous_linear_elimination_direct_addition",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"x = {x_val}, y = {y_val}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_27",
        "misconception_tags": ["subtracting_instead_of_adding_opposite_signs", "elimination_arithmetic_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Add equations to eliminate y term", "marks": 1},
            {"step": 2, "criterion": "Solve for x", "marks": 1},
            {"step": 3, "criterion": "Substitute to find y", "marks": 1},
        ],
        "hints": {
            "tier_1": f"The y terms (+{b}y and -{b}y) are opposites. Add the equations together.",
            "tier_2": f"{sum_a_d}x = {sum_c_f}, so x = {x_val}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_27_simultaneous_linear_elimination_direct_addition",
    }


# 28. Simultaneous linear elimination direct subtraction: ax + by = c and ax + dy = f
def arch_28_simultaneous_linear_elimination_direct_subtraction(rng: random.Random) -> Dict[str, Any]:
    # Identical x coefficients
    a = rng.choice([2, 3, 4, 5])
    b = rng.choice([5, 6, 7])
    d = rng.choice([2, 3])
    x_val = rng.randint(1, 5)
    y_val = rng.randint(1, 5)
    c = a * x_val + b * y_val
    f = a * x_val + d * y_val

    prompt = (
        f"Solve simultaneously using the elimination method:\n"
        f"\\[ (1) \\quad {a}x + {b}y = {c} \\]\n"
        f"\\[ (2) \\quad {a}x + {d}y = {f} \\]"
    )
    ans = f"x = {x_val}, y = {y_val}"
    diff_b_d = b - d
    diff_c_f = c - f

    sol = (
        f"**Step 1:** Subtract equation (2) from equation (1) to eliminate \\(x\\):\n"
        f"\\[ ({a}x - {a}x) + ({b}y - {d}y) = {c} - {f} \\]\n"
        f"\\[ {diff_b_d}y = {diff_c_f} \\]\n"
        f"\\[ y = \\frac{{{diff_c_f}}}{{{diff_b_d}}} = {y_val} \\]\n\n"
        f"**Step 2:** Substitute \\(y = {y_val}\\) into equation (2):\n"
        f"\\[ {a}x + {d}({y_val}) = {f} \\]\n"
        f"\\[ {a}x = {f - d * y_val} \\]\n"
        f"\\[ x = {x_val} \\]\n\n"
        f"**Solution:** \\(x = {x_val},\\; y = {y_val}\\)"
    )
    return {
        "id": f"g10_eq_28_{rng.randint(100000, 999999)}",
        "subskill": "28_simultaneous_linear_elimination_direct_subtraction",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"x = {x_val}, y = {y_val}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_28",
        "misconception_tags": ["subtraction_sign_error_across_terms", "elimination_variable_drop"],
        "marking_schema": [
            {"step": 1, "criterion": "Subtract equations to eliminate x", "marks": 1},
            {"step": 2, "criterion": "Solve for y", "marks": 1},
            {"step": 3, "criterion": "Substitute to solve for x", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Both equations have {a}x. Subtract equation (2) from equation (1).",
            "tier_2": f"{diff_b_d}y = {diff_c_f}, so y = {y_val}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_28_simultaneous_linear_elimination_direct_subtraction",
    }


# 29. Simultaneous linear elimination multiplication one equation: x + by = c and dx + ey = f
def arch_29_simultaneous_linear_elimination_multiplication_one_equation(rng: random.Random) -> Dict[str, Any]:
    # Eq 1 has coefficient 1 for x: x + b*y = c, Eq 2: d*x + e*y = f
    d = rng.choice([2, 3, 4])
    b = rng.choice([2, 3])
    e_coeff = rng.choice([4, 5, 7])
    while d * b == e_coeff:
        e_coeff += 1
    x_val = rng.randint(1, 5)
    y_val = rng.randint(1, 5)
    c = x_val + b * y_val
    f = d * x_val + e_coeff * y_val

    prompt = (
        f"Solve simultaneously by multiplying one equation:\n"
        f"\\[ (1) \\quad x + {b}y = {c} \\]\n"
        f"\\[ (2) \\quad {d}x + {e_coeff}y = {f} \\]"
    )
    ans = f"x = {x_val}, y = {y_val}"
    sol = (
        f"**Step 1:** Multiply equation (1) by \\({d}\\) to match coefficients of \\(x\\):\n"
        f"\\[ (3) \\quad {d}x + {d * b}y = {d * c} \\]\n\n"
        f"**Step 2:** Subtract equation (3) from equation (2) (or vice versa):\n"
        f"\\[ ({e_coeff} - {d * b})y = {f} - {d * c} \\]\n"
        f"\\[ {e_coeff - d * b}y = {f - d * c} \\]\n"
        f"\\[ y = {y_val} \\]\n\n"
        f"**Step 3:** Substitute \\(y = {y_val}\\) into equation (1):\n"
        f"\\[ x + {b}({y_val}) = {c} \\]\n"
        f"\\[ x = {c - b * y_val} = {x_val} \\]\n\n"
        f"**Solution:** \\(x = {x_val},\\; y = {y_val}\\)"
    )
    return {
        "id": f"g10_eq_29_{rng.randint(100000, 999999)}",
        "subskill": "29_simultaneous_linear_elimination_multiplication_one_equation",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"x = {x_val}, y = {y_val}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_eq_29",
        "misconception_tags": ["failure_to_multiply_rhs_constant", "elimination_subtraction_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Multiply entire equation (1) by d", "marks": 1},
            {"step": 2, "criterion": "Subtract to eliminate x and solve for y", "marks": 2},
            {"step": 3, "criterion": "Find x and state solution", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Multiply equation (1) by {d} so both equations have {d}x.",
            "tier_2": f"Remember to multiply {c} by {d} as well: {d}x + {d*b}y = {d*c}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_29_simultaneous_linear_elimination_multiplication_one_equation",
    }


# 30. Simultaneous linear elimination multiplication both equations
def arch_30_simultaneous_linear_elimination_multiplication_both_equations(rng: random.Random) -> Dict[str, Any]:
    # 2x + 3y = c and 3x + 2y = f
    a1, b1 = 2, 3
    a2, b2 = 3, 2
    x_val = rng.randint(1, 5)
    y_val = rng.randint(1, 5)
    c1 = a1 * x_val + b1 * y_val
    c2 = a2 * x_val + b2 * y_val

    prompt = (
        f"Solve simultaneously:\n"
        f"\\[ (1) \\quad {a1}x + {b1}y = {c1} \\]\n"
        f"\\[ (2) \\quad {a2}x + {b2}y = {c2} \\]"
    )
    ans = f"x = {x_val}, y = {y_val}"
    sol = (
        f"**Step 1:** Multiply equation (1) by 3 and equation (2) by 2 to align \\(x\\) coefficients:\n"
        f"\\[ (3) \\quad 6x + 9y = {3 * c1} \\]\n"
        f"\\[ (4) \\quad 6x + 4y = {2 * c2} \\]\n\n"
        f"**Step 2:** Subtract equation (4) from equation (3):\n"
        f"\\[ (9y - 4y) = {3 * c1} - {2 * c2} \\]\n"
        f"\\[ 5y = {3 * c1 - 2 * c2} \\]\n"
        f"\\[ y = {y_val} \\]\n\n"
        f"**Step 3:** Substitute \\(y = {y_val}\\) into equation (1):\n"
        f"\\[ 2x + 3({y_val}) = {c1} \\]\n"
        f"\\[ 2x = {c1 - 3 * y_val} \\]\n"
        f"\\[ x = {x_val} \\]\n\n"
        f"**Solution:** \\(x = {x_val},\\; y = {y_val}\\)"
    )
    return {
        "id": f"g10_eq_30_{rng.randint(100000, 999999)}",
        "subskill": "30_simultaneous_linear_elimination_multiplication_both_equations",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"x = {x_val}, y = {y_val}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_eq_30",
        "misconception_tags": ["scaling_equations_arithmetic_error", "partial_multiplication"],
        "marking_schema": [
            {"step": 1, "criterion": "Multiply both equations appropriately to match a coefficient", "marks": 1},
            {"step": 2, "criterion": "Subtract equations to eliminate one variable", "marks": 1},
            {"step": 3, "criterion": "Solve for first variable", "marks": 1},
            {"step": 4, "criterion": "Solve for second variable", "marks": 1},
        ],
        "hints": {
            "tier_1": "Multiply equation (1) by 3 and equation (2) by 2.",
            "tier_2": f"Subtract the two new equations to get 5y = {3*c1 - 2*c2}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_30_simultaneous_linear_elimination_multiplication_both_equations",
    }


# 31. Simultaneous linear fractional coefficients: x/2 + y/3 = c and x - y = d
def arch_31_simultaneous_linear_fractional_coefficients(rng: random.Random) -> Dict[str, Any]:
    x_val = rng.choice([2, 4, 6, 8])
    y_val = rng.choice([3, 6, 9])
    c = (x_val // 2) + (y_val // 3)
    d = x_val - y_val

    sign_d = f"- {abs(d)}" if d < 0 else f"+ {d}"

    prompt = (
        f"Solve simultaneously:\n"
        f"\\[ (1) \\quad \\frac{{x}}{{2}} + \\frac{{y}}{{3}} = {c} \\]\n"
        f"\\[ (2) \\quad x - y = {d} \\]"
    )
    ans = f"x = {x_val}, y = {y_val}"
    sol = (
        f"**Step 1:** Clear the fractions in equation (1) by multiplying by the LCD = 6:\n"
        f"\\[ 6\\left(\\frac{{x}}{{2}}\\right) + 6\\left(\\frac{{y}}{{3}}\\right) = 6({c}) \\]\n"
        f"\\[ (3) \\quad 3x + 2y = {6 * c} \\]\n\n"
        f"**Step 2:** From equation (2), express \\(x\\) in terms of \\(y\\):\n"
        f"\\[ x = y {'+' if d>=0 else '-'} {abs(d)} \\]\n\n"
        f"**Step 3:** Substitute into equation (3):\n"
        f"\\[ 3(y {'+' if d>=0 else '-'} {abs(d)}) + 2y = {6 * c} \\]\n"
        f"\\[ 3y {'+' if 3*d>=0 else '-'} {abs(3*d)} + 2y = {6 * c} \\]\n"
        f"\\[ 5y = {6 * c - 3 * d} \\]\n"
        f"\\[ y = {y_val} \\]\n\n"
        f"**Step 4:** Find \\(x\\):\n"
        f"\\[ x = {y_val} {'+' if d>=0 else '-'} {abs(d)} = {x_val} \\]\n\n"
        f"**Solution:** \\(x = {x_val},\\; y = {y_val}\\)"
    )
    return {
        "id": f"g10_eq_31_{rng.randint(100000, 999999)}",
        "subskill": "31_simultaneous_linear_fractional_coefficients",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"x = {x_val}, y = {y_val}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g10_eq_31",
        "misconception_tags": ["clearing_fractions_error", "substitution_in_fractional_system"],
        "marking_schema": [
            {"step": 1, "criterion": "Multiply equation (1) by 6 to clear fractions", "marks": 1},
            {"step": 2, "criterion": "Substitute expression for x into modified equation", "marks": 1},
            {"step": 3, "criterion": "Solve for y", "marks": 1},
            {"step": 4, "criterion": "Solve for x", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Multiply equation (1) by 6 to get 3x + 2y = {6*c}.",
            "tier_2": f"From (2), x = y + ({d}). Substitute into 3x + 2y = {6*c}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "mode": "elementary_31_simultaneous_linear_fractional_coefficients",
    }


# 32. Simultaneous linear geometric intersection point: lines intersecting at (x, y)
def arch_32_simultaneous_linear_geometric_intersection_point(rng: random.Random) -> Dict[str, Any]:
    # Lines y = m1*x + c1 and y = m2*x + c2
    m1 = rng.choice([1, 2, 3])
    m2 = rng.choice([-2, -1])
    x_val = rng.randint(1, 5)
    c1 = rng.randint(-4, 4)
    y_val = m1 * x_val + c1
    # y = m2*x + c2 => c2 = y_val - m2*x_val
    c2 = y_val - m2 * x_val

    sign_c1 = f"+ {c1}" if c1 >= 0 else f"- {abs(c1)}"
    sign_c2 = f"+ {c2}" if c2 >= 0 else f"- {abs(c2)}"

    prompt = (
        f"Find the coordinates \\((x;\\, y)\\) of the point of intersection of the two straight lines:\n"
        f"\\[ y = {m1}x {sign_c1} \\]\n"
        f"\\[ y = {m2}x {sign_c2} \\]"
    )
    ans = f"({x_val}; {y_val})"
    sol = (
        f"**Step 1:** At the point of intersection, the \\(y\\)-values are equal:\n"
        f"\\[ {m1}x {sign_c1} = {m2}x {sign_c2} \\]\n\n"
        f"**Step 2:** Group like terms and solve for \\(x\\):\n"
        f"\\[ {m1}x - ({m2}x) = {c2} - ({c1}) \\]\n"
        f"\\[ {m1 - m2}x = {c2 - c1} \\]\n"
        f"\\[ x = \\frac{{{c2 - c1}}}{{{m1 - m2}}} = {x_val} \\]\n\n"
        f"**Step 3:** Substitute \\(x = {x_val}\\) to find \\(y\\):\n"
        f"\\[ y = {m1}({x_val}) {sign_c1} = {y_val} \\]\n\n"
        f"**Point of intersection:** \\(({x_val};\\, {y_val})\\)"
    )
    return {
        "id": f"g10_eq_32_{rng.randint(100000, 999999)}",
        "subskill": "32_simultaneous_linear_geometric_intersection_point",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"({x_val}; {y_val})",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_32",
        "misconception_tags": ["geometric_algebraic_bridge_error", "coordinate_format_omission"],
        "marking_schema": [
            {"step": 1, "criterion": "Equate expressions for y", "marks": 1},
            {"step": 2, "criterion": "Solve for x", "marks": 1},
            {"step": 3, "criterion": "Find y and write as ordered coordinate pair (x; y)", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Set {m1}x {sign_c1} = {m2}x {sign_c2}.",
            "tier_2": f"Solve for x: {m1 - m2}x = {c2 - c1}, then calculate y.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_32_simultaneous_linear_geometric_intersection_point",
    }


# 33. Word problem sum and difference of two numbers
def arch_33_word_problem_sum_and_difference_two_numbers(rng: random.Random) -> Dict[str, Any]:
    x = rng.randint(15, 45)
    diff = rng.randint(4, 16)
    y = x - diff
    total = x + y

    prompt = (
        f"The sum of two numbers is {total}, and their difference is {diff}.\n\n"
        f"Determine the two numbers by setting up and solving a pair of linear equations."
    )
    ans = f"{x} and {y}"
    sol = (
        f"**Step 1:** Define variables:\n"
        f"Let the larger number be \\(x\\) and the smaller number be \\(y\\).\n\n"
        f"**Step 2:** Formulate equations:\n"
        f"\\[ (1) \\quad x + y = {total} \\]\n"
        f"\\[ (2) \\quad x - y = {diff} \\]\n\n"
        f"**Step 3:** Add equations (1) and (2):\n"
        f"\\[ 2x = {total + diff} \\implies x = {x} \\]\n\n"
        f"**Step 4:** Substitute \\(x = {x}\\) into (1):\n"
        f"\\[ {x} + y = {total} \\implies y = {total - x} = {y} \\]\n\n"
        f"The two numbers are **{x}** and **{y}**."
    )
    return {
        "id": f"g10_eq_33_{rng.randint(100000, 999999)}",
        "subskill": "33_word_problem_sum_and_difference_two_numbers",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{x} and {y}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_33",
        "misconception_tags": ["word_problem_translation_error", "simultaneous_setup_failure"],
        "marking_schema": [
            {"step": 1, "criterion": "Set up equations x + y = S and x - y = D", "marks": 1},
            {"step": 2, "criterion": "Solve for x", "marks": 1},
            {"step": 3, "criterion": "Solve for y and state both numbers", "marks": 1},
        ],
        "hints": {
            "tier_1": "Let the numbers be x and y. Then x + y = total and x - y = difference.",
            "tier_2": f"Add the two equations: 2x = {total + diff}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_33_word_problem_sum_and_difference_two_numbers",
    }


# 34. Word problem consecutive integers: three consecutive integers sum to S
def arch_34_word_problem_consecutive_integers(rng: random.Random) -> Dict[str, Any]:
    n = rng.randint(10, 40)
    total = n + (n + 1) + (n + 2)  # 3n + 3

    prompt = (
        f"The sum of three consecutive integers is {total}.\n\n"
        f"Find the three integers by setting up and solving an algebraic equation."
    )
    ans = f"{n}, {n + 1}, {n + 2}"
    sol = (
        f"**Step 1:** Define the three consecutive integers in terms of \\(n\\):\n"
        f"Let the integers be \\(n\\), \\(n + 1\\), and \\(n + 2\\).\n\n"
        f"**Step 2:** Formulate the equation:\n"
        f"\\[ n + (n + 1) + (n + 2) = {total} \\]\n"
        f"\\[ 3n + 3 = {total} \\]\n\n"
        f"**Step 3:** Solve for \\(n\\):\n"
        f"\\[ 3n = {total - 3} \\]\n"
        f"\\[ n = \\frac{{{total - 3}}}{{3}} = {n} \\]\n\n"
        f"The three integers are **{n}**, **{n + 1}**, and **{n + 2}**."
    )
    return {
        "id": f"g10_eq_34_{rng.randint(100000, 999999)}",
        "subskill": "34_word_problem_consecutive_integers",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{n}, {n+1}, {n+2}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_34",
        "misconception_tags": ["consecutive_integer_algebraic_setup", "omitting_other_consecutive_values"],
        "marking_schema": [
            {"step": 1, "criterion": "Define terms as n, n+1, n+2 and equate sum", "marks": 1},
            {"step": 2, "criterion": "Solve for n", "marks": 1},
            {"step": 3, "criterion": "List all three consecutive integers", "marks": 1},
        ],
        "hints": {
            "tier_1": "Let the consecutive integers be n, n+1, and n+2.",
            "tier_2": f"3n + 3 = {total} => 3n = {total - 3}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_34_word_problem_consecutive_integers",
    }


# 35. Word problem perimeter rectangle dimensions: length is k metres more than width
def arch_35_word_problem_perimeter_rectangle_dimensions(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(4, 18)
    diff = rng.randint(3, 12)
    l = w + diff
    p = 2 * (l + w)

    prompt = (
        f"The length of a rectangular garden is {diff} m longer than its width. "
        f"The perimeter of the garden is {p} m.\n\n"
        f"Determine the length and width of the garden."
    )
    ans = f"Length = {l} m, Width = {w} m"
    sol = (
        f"**Step 1:** Let width be \\(w\\) metres. Then length is \\(l = w + {diff}\\) metres.\n\n"
        f"**Step 2:** Use the perimeter formula \\(P = 2(l + w)\\):\n"
        f"\\[ 2((w + {diff}) + w) = {p} \\]\n"
        f"\\[ 2(2w + {diff}) = {p} \\]\n"
        f"\\[ 4w + {2 * diff} = {p} \\]\n\n"
        f"**Step 3:** Solve for \\(w\\):\n"
        f"\\[ 4w = {p - 2 * diff} \\]\n"
        f"\\[ w = \\frac{{{p - 2 * diff}}}{{4}} = {w}\\text{{ m}} \\]\n\n"
        f"**Step 4:** Calculate length:\n"
        f"\\[ l = {w} + {diff} = {l}\\text{{ m}} \\]\n\n"
        f"**Conclusion:** Length = **{l} m**, Width = **{w} m**"
    )
    return {
        "id": f"g10_eq_35_{rng.randint(100000, 999999)}",
        "subskill": "35_word_problem_perimeter_rectangle_dimensions",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{l} and {w}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_35",
        "misconception_tags": ["perimeter_formula_forgetting_factor_2", "dimension_misassignment"],
        "marking_schema": [
            {"step": 1, "criterion": "Set up perimeter equation 2(w + diff + w) = P", "marks": 1},
            {"step": 2, "criterion": "Solve for width w", "marks": 1},
            {"step": 3, "criterion": "Calculate length l and state units", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Perimeter = 2*(length + width) = 2*(w + {diff} + w) = {p}.",
            "tier_2": f"4w + {2*diff} = {p}, so 4w = {p - 2*diff}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_35_word_problem_perimeter_rectangle_dimensions",
    }


# 36. Word problem age relation future past
def arch_36_word_problem_age_relation_future_past(rng: random.Random) -> Dict[str, Any]:
    # Sipho is 3 times as old as his sister. In 5 years, he will be twice as old.
    # s = 3*y. In k years: s + k = 2*(y + k) => 3y + k = 2y + 2k => y = k
    k = rng.randint(4, 10)
    sister_age = k
    sipho_age = 3 * sister_age

    prompt = (
        f"Sipho is currently three times as old as his younger sister Busi. "
        f"In {k} years' time, Sipho will be twice as old as Busi.\n\n"
        f"Find their current ages."
    )
    ans = f"Sipho: {sipho_age} years, Busi: {sister_age} years"
    sol = (
        f"**Step 1:** Define variables:\n"
        f"Let Busi's current age be \\(x\\) years. Then Sipho's current age is \\(3x\\) years.\n\n"
        f"**Step 2:** Formulate equation for ages in {k} years:\n"
        f"In {k} years, Busi will be \\(x + {k}\\) and Sipho will be \\(3x + {k}\\).\n"
        f"\\[ 3x + {k} = 2(x + {k}) \\]\n\n"
        f"**Step 3:** Expand and solve for \\(x\\):\n"
        f"\\[ 3x + {k} = 2x + {2 * k} \\]\n"
        f"\\[ 3x - 2x = {2 * k} - {k} \\]\n"
        f"\\[ x = {sister_age} \\]\n\n"
        f"**Step 4:** Calculate Sipho's age:\n"
        f"\\[ 3({sister_age}) = {sipho_age} \\]\n\n"
        f"**Conclusion:** Sipho is **{sipho_age}** years old and Busi is **{sister_age}** years old."
    )
    return {
        "id": f"g10_eq_36_{rng.randint(100000, 999999)}",
        "subskill": "36_word_problem_age_relation_future_past",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": f"{sipho_age} and {sister_age}",
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_36",
        "misconception_tags": ["forgetting_to_add_years_to_both_people", "ratio_setup_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Define current and future ages correctly", "marks": 1},
            {"step": 2, "criterion": "Solve equation 3x + k = 2(x + k)", "marks": 1},
            {"step": 3, "criterion": "State both correct ages", "marks": 1},
        ],
        "hints": {
            "tier_1": f"In {k} years, both siblings age by {k} years!",
            "tier_2": f"3x + {k} = 2(x + {k}) => 3x + {k} = 2x + {2*k}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_36_word_problem_age_relation_future_past",
    }


# 37. Word problem speed distance time linear
def arch_37_word_problem_speed_distance_time_linear(rng: random.Random) -> Dict[str, Any]:
    # A car travels at speed v km/h for 2 hours, then at (v + 20) km/h for 3 hours, covering total distance D.
    v = rng.choice([60, 70, 80, 90])
    diff = 20
    t1 = 2
    t2 = 3
    d_total = t1 * v + t2 * (v + diff)

    prompt = (
        f"A motorist travels at an average speed of \\(v\\) km/h for {t1} hours, "
        f"and then increases speed to \\((v + {diff})\\) km/h for the next {t2} hours. "
        f"The total distance travelled is {d_total} km.\n\n"
        f"Calculate the initial speed \\(v\\)."
    )
    ans = f"{v} km/h"
    sol = (
        f"**Step 1:** Use \\(\\text{{Distance}} = \\text{{Speed}} \\times \\text{{Time}}\\):\n"
        f"- First segment: \\(d_1 = {t1}v\\)\n"
        f"- Second segment: \\(d_2 = {t2}(v + {diff})\\)\n\n"
        f"**Step 2:** Formulate equation for total distance:\n"
        f"\\[ {t1}v + {t2}(v + {diff}) = {d_total} \\]\n"
        f"\\[ {t1}v + {t2}v + {t2 * diff} = {d_total} \\]\n"
        f"\\[ {t1 + t2}v + {t2 * diff} = {d_total} \\]\n\n"
        f"**Step 3:** Solve for \\(v\\):\n"
        f"\\[ {t1 + t2}v = {d_total - t2 * diff} \\]\n"
        f"\\[ v = \\frac{{{d_total - t2 * diff}}}{{{t1 + t2}}} = {v}\\text{{ km/h}} \\]"
    )
    return {
        "id": f"g10_eq_37_{rng.randint(100000, 999999)}",
        "subskill": "37_word_problem_speed_distance_time_linear",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(v),
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_37",
        "misconception_tags": ["speed_distance_time_formula_confusion", "bracket_expansion_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Express distance of each segment using d = s * t", "marks": 1},
            {"step": 2, "criterion": "Equate sum to total distance", "marks": 1},
            {"step": 3, "criterion": "Solve for initial speed v with correct units", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Distance 1 = {t1}v; Distance 2 = {t2}(v + {diff}). Total distance = {d_total}.",
            "tier_2": f"{t1+t2}v + {t2*diff} = {d_total}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_37_word_problem_speed_distance_time_linear",
    }


# 38. Word problem financial fixed and variable cost
def arch_38_word_problem_financial_fixed_variable_cost(rng: random.Random) -> Dict[str, Any]:
    fixed = rng.choice([150, 200, 250, 300])
    rate = rng.choice([25, 30, 40, 50])
    n = rng.randint(8, 25)
    total_cost = fixed + rate * n

    prompt = (
        f"A caterer charges a fixed setup fee of R{fixed} plus R{rate} per guest. "
        f"A school spent a total of R{total_cost} on catering for an event.\n\n"
        f"Determine the number of guests who attended."
    )
    ans = f"{n} guests"
    sol = (
        f"**Step 1:** Let the number of guests be \\(n\\).\n\n"
        f"**Step 2:** Set up the total cost equation:\n"
        f"\\[ \\text{{Total Cost}} = \\text{{Fixed Fee}} + (\\text{{Rate per guest}} \\times n) \\]\n"
        f"\\[ {fixed} + {rate}n = {total_cost} \\]\n\n"
        f"**Step 3:** Subtract the fixed fee from both sides:\n"
        f"\\[ {rate}n = {total_cost} - {fixed} = {total_cost - fixed} \\]\n\n"
        f"**Step 4:** Divide by the rate per guest:\n"
        f"\\[ n = \\frac{{{total_cost - fixed}}}{{{rate}}} = {n} \\]\n\n"
        f"**Conclusion:** There were **{n}** guests."
    )
    return {
        "id": f"g10_eq_38_{rng.randint(100000, 999999)}",
        "subskill": "38_word_problem_financial_fixed_variable_cost",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": str(n),
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_38",
        "misconception_tags": ["dividing_before_subtracting_fixed_cost", "linear_cost_modeling_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Set up linear cost equation fixed + rate * n = total", "marks": 1},
            {"step": 2, "criterion": "Isolate variable term rate * n", "marks": 1},
            {"step": 3, "criterion": "Solve for n", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Setup fee R{fixed} is paid once. The rest comes from {rate} * n.",
            "tier_2": f"{rate}n = {total_cost - fixed}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_38_word_problem_financial_fixed_variable_cost",
    }


# 39. Literal equation linear isolate single term: ax + by = c make x the subject
def arch_39_literal_equation_linear_isolate_single_term(rng: random.Random) -> Dict[str, Any]:
    target = "x"
    other = "y"
    a = rng.choice([2, 3, 4, 5])
    b = rng.choice([3, 4, 6])
    c = "c"

    prompt = (
        f"Make \\({target}\\) the subject of the formula:\n"
        f"\\[ {a}{target} + {b}{other} = {c} \\]"
    )
    ans = f"({c} - {b}{other})/{a}"
    sol = (
        f"**Step 1:** Subtract \\({b}{other}\\) from both sides to isolate the \\({target}\\)-term:\n"
        f"\\[ {a}{target} = {c} - {b}{other} \\]\n\n"
        f"**Step 2:** Divide both sides by the coefficient \\({a}\\):\n"
        f"\\[ {target} = \\frac{{{c} - {b}{other}}}{{{a}}} \\]"
    )
    return {
        "id": f"g10_eq_39_{rng.randint(100000, 999999)}",
        "subskill": "39_literal_equation_linear_isolate_single_term",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"x = ({c} - {b}y)/{a}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_39",
        "misconception_tags": ["sign_error_literal_transposition", "dividing_only_one_term_by_coefficient"],
        "marking_schema": [
            {"step": 1, "criterion": "Transpose other variable term with sign flip", "marks": 1},
            {"step": 2, "criterion": "Divide entire numerator by coefficient", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Isolate {a}{target} first by subtracting {b}{other}.",
            "tier_2": f"Divide the entire RHS by {a}.",
            "tier_3": f"{target} = ({c} - {b}{other})/{a}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_39_literal_equation_linear_isolate_single_term",
    }


# 40. Literal equation common factor isolation: ax + bx = c -> x(a + b) = c
def arch_40_literal_equation_common_factor_isolation(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice(["x", "y", "t", "p"])
    c1, c2 = rng.choice([("a", "b"), ("p", "q"), ("m", "n"), ("k", "h")])
    rhs_var = rng.choice(["c", "d", "w", "R"])
    prompt = (
        f"Make \\({target}\\) the subject of the formula:\n"
        f"\\[ {c1}{target} + {c2}{target} = {rhs_var} \\]"
    )
    ans = f"{rhs_var}/({c1} + {c2})"
    sol = (
        f"**Step 1:** Notice that \\({target}\\) appears in two terms on the left. Factor out the common factor \\({target}\\):\n"
        f"\\[ {target}({c1} + {c2}) = {rhs_var} \\]\n\n"
        f"**Step 2:** Divide both sides by the bracket \\(({c1} + {c2})\\):\n"
        f"\\[ {target} = \\frac{{{rhs_var}}}{{{c1} + {c2}}} \\quad \\text{{(provided }} {c1} + {c2} \\neq 0\\text{{)}} \\]"
    )
    return {
        "id": f"g10_eq_40_{rng.randint(100000, 999999)}",
        "subskill": "40_literal_equation_common_factor_isolation",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"{target} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_40",
        "misconception_tags": ["dividing_by_individual_variables_instead_of_factoring", "common_factor_omission"],
        "marking_schema": [
            {"step": 1, "criterion": f"Factor out {target} to get {target}({c1} + {c2}) = {rhs_var}", "marks": 1},
            {"step": 2, "criterion": f"Divide by ({c1} + {c2}) to isolate {target}", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Take out {target} as a common factor on the left-hand side.",
            "tier_2": f"{target}({c1} + {c2}) = {rhs_var}. Now divide by ({c1} + {c2}).",
            "tier_3": f"{target} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_40_literal_equation_common_factor_isolation",
    }


# 41. Literal equation simple interest formula: A = P(1 + in) solve for n
def arch_41_literal_equation_simple_interest_formula(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice(["n", "i", "P"])
    prompt = (
        f"The formula for simple interest growth is \\(A = P(1 + in)\\).\n\n"
        f"Make \\({target}\\) the subject of the formula."
    )
    if target == "P":
        ans = "A/(1 + in)"
        sol = (
            f"**Step 1:** To isolate \\(P\\), divide both sides by \\((1 + in)\\):\n"
            f"\\[ P = \\frac{{A}}{{1 + in}} \\]"
        )
    elif target == "n":
        ans = "(A - P)/(P*i)"
        sol = (
            f"**Step 1:** Divide both sides by \\(P\\):\n"
            f"\\[ \\frac{{A}}{{P}} = 1 + in \\]\n\n"
            f"**Step 2:** Subtract 1:\n"
            f"\\[ \\frac{{A}}{{P}} - 1 = in \\implies \\frac{{A - P}}{{P}} = in \\]\n\n"
            f"**Step 3:** Divide by \\(i\\):\n"
            f"\\[ n = \\frac{{A - P}}{{Pi}} \\]"
        )
    else:  # i
        ans = "(A - P)/(P*n)"
        sol = (
            f"**Step 1:** Divide both sides by \\(P\\):\n"
            f"\\[ \\frac{{A}}{{P}} = 1 + in \\]\n\n"
            f"**Step 2:** Subtract 1:\n"
            f"\\[ \\frac{{A - P}}{{P}} = in \\]\n\n"
            f"**Step 3:** Divide by \\(n\\):\n"
            f"\\[ i = \\frac{{A - P}}{{Pn}} \\]"
        )

    return {
        "id": f"g10_eq_41_{rng.randint(100000, 999999)}",
        "subskill": "41_literal_equation_simple_interest_formula",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"{target} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_41",
        "misconception_tags": ["order_of_operations_literal_unwinding", "bracket_division_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Divide by P or expand brackets", "marks": 1},
            {"step": 2, "criterion": "Subtract 1 and isolate target term", "marks": 1},
            {"step": 3, "criterion": f"Correctly isolate {target}", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Start by dividing both sides by P to get A/P = 1 + in.",
            "tier_2": f"Subtract 1, then divide by the coefficient of {target}.",
            "tier_3": f"{target} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_41_literal_equation_simple_interest_formula",
    }


# 42. Literal equation physics kinematics linear: v = u + at solve for a or t
def arch_42_literal_equation_physics_kinematics_linear(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice(["a", "t", "u"])
    prompt = (
        f"In kinematics, the velocity equation is given by \\(v = u + at\\).\n\n"
        f"Make \\({target}\\) the subject of the formula."
    )
    if target == "u":
        ans = "v - at"
        sol = (
            f"**Step 1:** Subtract \\(at\\) from both sides:\n"
            f"\\[ u = v - at \\]"
        )
    elif target == "a":
        ans = "(v - u)/t"
        sol = (
            f"**Step 1:** Subtract \\(u\\) from both sides:\n"
            f"\\[ at = v - u \\]\n\n"
            f"**Step 2:** Divide both sides by \\(t\\):\n"
            f"\\[ a = \\frac{{v - u}}{{t}} \\]"
        )
    else:  # t
        ans = "(v - u)/a"
        sol = (
            f"**Step 1:** Subtract \\(u\\) from both sides:\n"
            f"\\[ at = v - u \\]\n\n"
            f"**Step 2:** Divide both sides by \\(a\\):\n"
            f"\\[ t = \\frac{{v - u}}{{a}} \\]"
        )

    return {
        "id": f"g10_eq_42_{rng.randint(100000, 999999)}",
        "subskill": "42_literal_equation_physics_kinematics_linear",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"{target} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_42",
        "misconception_tags": ["sign_error_kinematics_transposition", "division_omission"],
        "marking_schema": [
            {"step": 1, "criterion": "Subtract u from both sides", "marks": 1},
            {"step": 2, "criterion": f"Divide by coefficient to isolate {target}", "marks": 1},
        ],
        "hints": {
            "tier_1": f"First subtract u: v - u = at.",
            "tier_2": f"Now divide by the other factor to isolate {target}.",
            "tier_3": f"{target} = {ans}",
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_42_literal_equation_physics_kinematics_linear",
    }


# 43. Literal equation geometry surface area / volume
def arch_43_literal_equation_geometry_surface_area_volume(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice(["cone", "cylinder", "prism"])
    if case == "cone":
        prompt = (
            f"The volume of a right circular cone is given by \\(V = \\frac{{1}}{{3}}\\pi r^2 h\\).\n\n"
            f"Make the height \\(h\\) the subject of the formula."
        )
        ans = "3V/(pi*r^2)"
        sol = (
            f"**Step 1:** Multiply both sides by 3 to clear the fraction:\n"
            f"\\[ 3V = \\pi r^2 h \\]\n\n"
            f"**Step 2:** Divide both sides by \\(\\pi r^2\\):\n"
            f"\\[ h = \\frac{{3V}}{{\\pi r^2}} \\]"
        )
    elif case == "cylinder":
        prompt = (
            f"The volume of a cylinder is given by \\(V = \\pi r^2 h\\).\n\n"
            f"Make the height \\(h\\) the subject of the formula."
        )
        ans = "V/(pi*r^2)"
        sol = (
            f"**Step 1:** Divide both sides by \\(\\pi r^2\\):\n"
            f"\\[ h = \\frac{{V}}{{\\pi r^2}} \\]"
        )
    else:  # prism
        prompt = (
            f"The volume of a rectangular prism is given by \\(V = l \\times w \\times h\\).\n\n"
            f"Make the width \\(w\\) the subject of the formula."
        )
        ans = "V/(l*h)"
        sol = (
            f"**Step 1:** Divide both sides by \\(l \\times h\\):\n"
            f"\\[ w = \\frac{{V}}{{lh}} \\]"
        )

    return {
        "id": f"g10_eq_43_{rng.randint(100000, 999999)}",
        "subskill": "43_literal_equation_geometry_surface_area_volume",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_43",
        "misconception_tags": ["fraction_reciprocal_clearing_error", "composite_denominator_grouping"],
        "marking_schema": [
            {"step": 1, "criterion": "Clear constant fraction if applicable", "marks": 1},
            {"step": 2, "criterion": "Divide by coefficient product to isolate variable", "marks": 1},
        ],
        "hints": {
            "tier_1": "Isolate the target variable by dividing by all other multiplying factors.",
            "tier_2": f"Target = {ans}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_43_literal_equation_geometry_surface_area_volume",
    }


# 44. Literal equation reciprocal fractions resistance: 1/R = 1/R1 + 1/R2 solve for R
def arch_44_literal_equation_reciprocal_fractions_resistance(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice(["resistance", "optics"])
    if case == "resistance":
        target = rng.choice(["R", "R_1"])
        if target == "R":
            prompt = (
                f"The total resistance \\(R\\) of two parallel resistors is given by:\n"
                f"\\[ \\frac{{1}}{{R}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_2}} \\]\n\n"
                f"Make \\(R\\) the subject of the formula."
            )
            ans = "(R1*R2)/(R1 + R2)"
            sol = (
                f"**Step 1:** Combine fractions on the RHS using LCD \\(R_1 R_2\\):\n"
                f"\\[ \\frac{{1}}{{R}} = \\frac{{R_2 + R_1}}{{R_1 R_2}} = \\frac{{R_1 + R_2}}{{R_1 R_2}} \\]\n\n"
                f"**Step 2:** Invert both sides:\n"
                f"\\[ R = \\frac{{R_1 R_2}}{{R_1 + R_2}} \\]"
            )
        else:
            prompt = (
                f"In the parallel resistance formula \\(\\frac{{1}}{{R}} = \\frac{{1}}{{R_1}} + \\frac{{1}}{{R_2}}\\), "
                f"make \\(R_1\\) the subject of the formula."
            )
            ans = "(R*R2)/(R2 - R)"
            sol = (
                f"**Step 1:** Isolate \\(\\frac{{1}}{{R_1}}\\):\n"
                f"\\[ \\frac{{1}}{{R_1}} = \\frac{{1}}{{R}} - \\frac{{1}}{{R_2}} = \\frac{{R_2 - R}}{{R R_2}} \\]\n\n"
                f"**Step 2:** Invert both sides:\n"
                f"\\[ R_1 = \\frac{{R R_2}}{{R_2 - R}} \\]"
            )
    else:  # optics thin lens
        prompt = (
            f"The thin lens formula is given by \\(\\frac{{1}}{{f}} = \\frac{{1}}{{u}} + \\frac{{1}}{{v}}\\).\n\n"
            f"Make the focal length \\(f\\) the subject of the formula."
        )
        ans = "(u*v)/(u + v)"
        sol = (
            f"**Step 1:** Combine fractions over LCD \\(uv\\):\n"
            f"\\[ \\frac{{1}}{{f}} = \\frac{{v + u}}{{uv}} = \\frac{{u + v}}{{uv}} \\]\n\n"
            f"**Step 2:** Invert both sides:\n"
            f"\\[ f = \\frac{{uv}}{{u + v}} \\]"
        )

    return {
        "id": f"g10_eq_44_{rng.randint(100000, 999999)}",
        "subskill": "44_literal_equation_reciprocal_fractions_resistance",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_44",
        "misconception_tags": ["inverting_terms_individually_fallacy", "algebraic_lcd_failure"],
        "marking_schema": [
            {"step": 1, "criterion": "Combine fractions over common denominator", "marks": 2},
            {"step": 2, "criterion": "Invert both sides to isolate target", "marks": 1},
        ],
        "hints": {
            "tier_1": "Combine fractions over their lowest common denominator first, then invert.",
            "tier_2": f"Target = {ans}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_44_literal_equation_reciprocal_fractions_resistance",
    }


# 45. Linear inequality one step positive coeff: ax + b < c (a > 0)
def arch_45_linear_inequality_one_step_positive_coeff(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4, 5])
    k = rng.randint(-5, 8)
    b = rng.choice([-8, -6, -4, 2, 4, 6, 8])
    c = a * k + b
    symb = rng.choice(["<", ">", "\\leq", "\\geq"])

    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"

    prompt = (
        f"Solve the linear inequality for \\(x\\):\n"
        f"\\[ {a}x {sign_b} {symb} {c} \\]"
    )
    ans = f"x {symb} {k}"
    sol = (
        f"**Step 1:** Subtract {b} from both sides:\n"
        f"\\[ {a}x {symb} {c} - ({b}) \\]\n"
        f"\\[ {a}x {symb} {c - b} \\]\n\n"
        f"**Step 2:** Divide both sides by {a} (since {a} > 0, the inequality sign does not flip):\n"
        f"\\[ x {symb} \\frac{{{c - b}}}{{{a}}} \\]\n"
        f"\\[ x {symb} {k} \\]"
    )
    return {
        "id": f"g10_eq_45_{rng.randint(100000, 999999)}",
        "subskill": "45_linear_inequality_one_step_positive_coeff",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_45",
        "misconception_tags": ["sign_error_inequality", "unnecessary_inequality_reversal"],
        "marking_schema": [
            {"step": 1, "criterion": "Transpose constant term", "marks": 1},
            {"step": 2, "criterion": "Divide by positive coefficient preserving inequality direction", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Isolate {a}x by subtracting {b}.",
            "tier_2": f"Divide by {a}. Since {a} is positive, do not flip the sign.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_45_linear_inequality_one_step_positive_coeff",
    }


# 46. Linear inequality division by negative reversal: -ax + b <= c
def arch_46_linear_inequality_division_by_negative_reversal(rng: random.Random) -> Dict[str, Any]:
    pos_a = rng.choice([2, 3, 4, 5])
    a = -pos_a
    k = rng.randint(-6, 6)
    b = rng.randint(-10, 10)
    c = a * k + b

    # If original is <=, flipping gives >=
    orig_symb, flipped_symb = rng.choice([("<", ">"), (">", "<"), ("\\leq", "\\geq"), ("\\geq", "\\leq")])
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"

    prompt = (
        f"Solve the linear inequality for \\(x\\):\n"
        f"\\[ {a}x {sign_b} {orig_symb} {c} \\]"
    )
    ans = f"x {flipped_symb} {k}"
    sol = (
        f"**Step 1:** Subtract {b} from both sides:\n"
        f"\\[ {a}x {orig_symb} {c - b} \\]\n\n"
        f"**Step 2:** Divide both sides by \\({a}\\). **Crucial rule:** dividing by a negative number **reverses** the inequality sign!\n"
        f"\\[ x {flipped_symb} \\frac{{{c - b}}}{{{a}}} \\]\n"
        f"\\[ x {flipped_symb} {k} \\]"
    )
    return {
        "id": f"g10_eq_46_{rng.randint(100000, 999999)}",
        "subskill": "46_linear_inequality_division_by_negative_reversal",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_46",
        "misconception_tags": ["failure_to_reverse_inequality_when_dividing_by_negative", "negative_division_arithmetic"],
        "marking_schema": [
            {"step": 1, "criterion": "Transpose constant term", "marks": 1},
            {"step": 2, "criterion": "Reverse inequality sign when dividing by negative number", "marks": 1},
            {"step": 3, "criterion": "Correct calculation of boundary value", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Move {b} to the RHS first.",
            "tier_2": f"When dividing by {a} (a negative number), you MUST flip {orig_symb} to {flipped_symb}!",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_46_linear_inequality_division_by_negative_reversal",
    }


# 47. Linear inequality two step brackets: a(x + b) > c(x + d)
def arch_47_linear_inequality_two_step_brackets(rng: random.Random) -> Dict[str, Any]:
    a = 3
    c = 1
    k = rng.randint(-5, 5)
    b = rng.randint(-4, 4)
    # 3(x + b) > x + d => 3x + 3b > x + d => 2x > d - 3b => x > (d - 3b)/2
    d = 2 * k + 3 * b
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_d = f"+ {d}" if d >= 0 else f"- {abs(d)}"

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ 3(x {sign_b}) > x {sign_d} \\]"
    )
    ans = f"x > {k}"
    sol = (
        f"**Step 1:** Expand the brackets on the LHS:\n"
        f"\\[ 3x {'+' if 3*b>=0 else '-'} {abs(3*b)} > x {sign_d} \\]\n\n"
        f"**Step 2:** Collect like terms:\n"
        f"\\[ 3x - x > {d} - ({3*b}) \\]\n"
        f"\\[ 2x > {d - 3*b} \\]\n\n"
        f"**Step 3:** Divide by 2:\n"
        f"\\[ x > \\frac{{{d - 3*b}}}{{2}} \\implies x > {k} \\]"
    )
    return {
        "id": f"g10_eq_47_{rng.randint(100000, 999999)}",
        "subskill": "47_linear_inequality_two_step_brackets",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_47",
        "misconception_tags": ["bracket_expansion_error", "inequality_direction_confusion"],
        "marking_schema": [
            {"step": 1, "criterion": "Expand brackets accurately", "marks": 1},
            {"step": 2, "criterion": "Collect variable terms on LHS and constants on RHS", "marks": 1},
            {"step": 3, "criterion": "Divide to find boundary condition", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Expand 3(x {sign_b}) first.",
            "tier_2": f"3x - x > {d - 3*b}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_47_linear_inequality_two_step_brackets",
    }


# 48. Linear inequality compound double boundary: a <= bx + c < d
def arch_48_linear_inequality_compound_double_boundary(rng: random.Random) -> Dict[str, Any]:
    b = rng.choice([2, 3, 4])
    lo = rng.randint(-4, 0)
    hi = lo + rng.randint(3, 6)
    c = rng.randint(-5, 5)
    lhs = b * lo + c
    rhs = b * hi + c

    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"

    prompt = (
        f"Solve the compound linear inequality for \\(x\\):\n"
        f"\\[ {lhs} \\leq {b}x {sign_c} < {rhs} \\]"
    )
    ans = f"{lo} <= x < {hi}"
    sol = (
        f"**Step 1:** Subtract {c} from all three parts of the inequality:\n"
        f"\\[ {lhs} - ({c}) \\leq {b}x < {rhs} - ({c}) \\]\n"
        f"\\[ {lhs - c} \\leq {b}x < {rhs - c} \\]\n\n"
        f"**Step 2:** Divide all three parts by \\({b}\\):\n"
        f"\\[ \\frac{{{lhs - c}}}{{{b}}} \\leq x < \\frac{{{rhs - c}}}{{{b}}} \\]\n"
        f"\\[ {lo} \\leq x < {hi} \\]"
    )
    return {
        "id": f"g10_eq_48_{rng.randint(100000, 999999)}",
        "subskill": "48_linear_inequality_compound_double_boundary",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": f"{lo} <= x < {hi}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_48",
        "misconception_tags": ["operating_on_only_two_sides_of_double_inequality", "boundary_sign_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Subtract constant from all three parts", "marks": 1},
            {"step": 2, "criterion": "Divide all parts by coefficient b", "marks": 1},
            {"step": 3, "criterion": "Correct compound inequality solution", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Whatever operation you perform, apply it to all THREE parts of the inequality!",
            "tier_2": f"Subtract {c} from {lhs}, middle, and {rhs}, then divide by {b}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "mode": "elementary_48_linear_inequality_compound_double_boundary",
    }


# 49. Linear inequality number line representation SVG
def arch_49_linear_inequality_number_line_representation_svg(rng: random.Random) -> Dict[str, Any]:
    val = rng.randint(-3, 3)
    is_strict = rng.choice([True, False])
    direction = rng.choice(["greater", "less"])

    if direction == "greater":
        symb = ">" if is_strict else "\\geq"
        cond_text = f"x {symb} {val}"
        circle_fill = "#FFFFFF" if is_strict else "#2563EB"
        circle_type = "an open circle (not included)" if is_strict else "a solid circle (included)"
        arrow_dir = "to the right (towards positive infinity)"
        ray_x2 = 460
    else:
        symb = "<" if is_strict else "\\leq"
        cond_text = f"x {symb} {val}"
        circle_fill = "#FFFFFF" if is_strict else "#2563EB"
        circle_type = "an open circle (not included)" if is_strict else "a solid circle (included)"
        arrow_dir = "to the left (towards negative infinity)"
        ray_x2 = 40

    # Build SVG number line from -5 to +5 (centered at x = 250, spacing = 40px)
    cx = 250 + val * 40

    ticks_svg = []
    labels_svg = []
    for t in range(-5, 6):
        tx = 250 + t * 40
        ticks_svg.append(f'<line x1="{tx}" y1="55" x2="{tx}" y2="65" stroke="#1E293B" stroke-width="2"/>')
        labels_svg.append(f'<text x="{tx}" y="85" font-size="14" font-family="sans-serif" text-anchor="middle" fill="#1E293B">{t}</text>')

    ray_svg = f'<line x1="{cx}" y1="60" x2="{ray_x2}" y2="60" stroke="#2563EB" stroke-width="4"/>'
    arrow_head = (
        f'<polygon points="460,55 475,60 460,65" fill="#2563EB"/>'
        if direction == "greater"
        else f'<polygon points="40,55 25,60 40,65" fill="#2563EB"/>'
    )
    circle_svg = f'<circle cx="{cx}" cy="60" r="6" fill="{circle_fill}" stroke="#2563EB" stroke-width="3"/>'

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 120" width="100%" height="120">
  <defs>
    <marker id="arr-left" viewBox="0 0 10 10" refX="0" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 10 0 L 0 5 L 10 10 z" fill="#1E293B"/>
    </marker>
    <marker id="arr-right" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1E293B"/>
    </marker>
  </defs>
  <!-- Main Axis -->
  <line x1="30" y1="60" x2="470" y2="60" stroke="#1E293B" stroke-width="2" marker-start="url(#arr-left)" marker-end="url(#arr-right)"/>
  {''.join(ticks_svg)}
  {''.join(labels_svg)}
  <!-- Solution Ray -->
  {ray_svg}
  {arrow_head}
  {circle_svg}
</svg>'''

    diagram_spec = {
        "kind": "inline_svg",
        "svg": svg_content,
        "diagram_role": "context",
        "caption": f"Number line representation for inequality with boundary at {val}",
    }

    prompt = (
        f"Represent the solution to the inequality \\({cond_text}\\) on a real number line.\n\n"
        f"State whether the boundary at \\({val}\\) is indicated by an open or solid circle, "
        f"and state the direction of the shaded arrow."
    )
    ans = f"{'Open' if is_strict else 'Solid'} circle at {val}, pointing {'right' if direction == 'greater' else 'left'}"
    sol = (
        f"**Step 1: Boundary circle type:**\n"
        f"Since the inequality \\({cond_text}\\) uses the strictness \\({symb}\\), the value \\({val}\\) is "
        f"represented by **{circle_type}**.\n\n"
        f"**Step 2: Ray direction:**\n"
        f"Values satisfying \\({cond_text}\\) lie **{arrow_dir}**.\n\n"
        f"**Conclusion:** {ans}."
    )
    return {
        "id": f"g10_eq_49_{rng.randint(100000, 999999)}",
        "subskill": "49_linear_inequality_number_line_representation_svg",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g10_eq_49",
        "misconception_tags": ["open_vs_closed_circle_confusion", "number_line_arrow_direction_error"],
        "diagram_spec": diagram_spec,
        "marking_schema": [
            {"step": 1, "criterion": "Correct circle type (open vs closed)", "marks": 1},
            {"step": 2, "criterion": "Correct arrow direction", "marks": 1},
            {"step": 3, "criterion": "Accurate boundary position on number line", "marks": 1},
        ],
        "hints": {
            "tier_1": f"Solid circle is used for <= or >= (value included); open circle for < or >.",
            "tier_2": f"For {cond_text}, {val} is {'not included (open circle)' if is_strict else 'included (solid circle)'}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_49_linear_inequality_number_line_representation_svg",
    }


# 50. Linear inequality interval and set builder notation
def arch_50_linear_inequality_interval_and_set_builder_notation(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(-5, 0)
    b = a + rng.randint(3, 7)
    left_strict = rng.choice([True, False])
    right_strict = rng.choice([True, False])

    left_symb = "<" if left_strict else "\\leq"
    right_symb = "<" if right_strict else "\\leq"
    left_bracket = "(" if left_strict else "["
    right_bracket = ")" if right_strict else "]"

    ineq_str = f"{a} {left_symb} x {right_symb} {b}"
    interval_str = f"{left_bracket}{a}; {b}{right_bracket}"
    set_builder_str = f"\\{{ x \\in \\mathbb{{R}} \\mid {ineq_str} \\}}"

    prompt = (
        f"Write the solution set \\({ineq_str}\\) in **interval notation**."
    )
    ans = interval_str
    sol = (
        f"**Step 1:** Inspect boundary types:\n"
        f"- Left boundary \\(x {'>' if left_strict else '\\geq'} {a}\\): uses **{left_bracket}** because {a} is {('excluded' if left_strict else 'included')}.\n"
        f"- Right boundary \\(x {'<' if right_strict else '\\leq'} {b}\\): uses **{right_bracket}** because {b} is {('excluded' if right_strict else 'included')}.\n\n"
        f"**Step 2:** Combine into interval notation:\n"
        f"\\[ x \\in {interval_str} \\]\n\n"
        f"*(Note: in set-builder notation this is written as \\({set_builder_str}\\))*"
    )
    return {
        "id": f"g10_eq_50_{rng.randint(100000, 999999)}",
        "subskill": "50_linear_inequality_interval_and_set_builder_notation",
        "question_type": "short_answer",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g10_eq_50",
        "misconception_tags": ["round_vs_square_bracket_interval_notation", "boundary_inclusion_error"],
        "marking_schema": [
            {"step": 1, "criterion": "Correct boundary brackets (round vs square)", "marks": 1},
            {"step": 2, "criterion": "Accurate interval notation [a; b]", "marks": 1},
        ],
        "hints": {
            "tier_1": "Square brackets [ or ] mean included (<= or >=); round brackets ( or ) mean excluded (< or >).",
            "tier_2": f"Left side: {left_bracket}{a}; Right side: {b}{right_bracket}.",
            "tier_3": ans,
        },
        "topic": "Equations and inequalities",
        "grade": "10",
        "subject": "Mathematics",
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 2,
        "mode": "elementary_50_linear_inequality_interval_and_set_builder_notation",
    }


BUILDERS_26_50 = {
    "26_simultaneous_linear_substitution_rearranging_first": arch_26_simultaneous_linear_substitution_rearranging_first,
    "27_simultaneous_linear_elimination_direct_addition": arch_27_simultaneous_linear_elimination_direct_addition,
    "28_simultaneous_linear_elimination_direct_subtraction": arch_28_simultaneous_linear_elimination_direct_subtraction,
    "29_simultaneous_linear_elimination_multiplication_one_equation": arch_29_simultaneous_linear_elimination_multiplication_one_equation,
    "30_simultaneous_linear_elimination_multiplication_both_equations": arch_30_simultaneous_linear_elimination_multiplication_both_equations,
    "31_simultaneous_linear_fractional_coefficients": arch_31_simultaneous_linear_fractional_coefficients,
    "32_simultaneous_linear_geometric_intersection_point": arch_32_simultaneous_linear_geometric_intersection_point,
    "33_word_problem_sum_and_difference_two_numbers": arch_33_word_problem_sum_and_difference_two_numbers,
    "34_word_problem_consecutive_integers": arch_34_word_problem_consecutive_integers,
    "35_word_problem_perimeter_rectangle_dimensions": arch_35_word_problem_perimeter_rectangle_dimensions,
    "36_word_problem_age_relation_future_past": arch_36_word_problem_age_relation_future_past,
    "37_word_problem_speed_distance_time_linear": arch_37_word_problem_speed_distance_time_linear,
    "38_word_problem_financial_fixed_variable_cost": arch_38_word_problem_financial_fixed_variable_cost,
    "39_literal_equation_linear_isolate_single_term": arch_39_literal_equation_linear_isolate_single_term,
    "40_literal_equation_common_factor_isolation": arch_40_literal_equation_common_factor_isolation,
    "41_literal_equation_simple_interest_formula": arch_41_literal_equation_simple_interest_formula,
    "42_literal_equation_physics_kinematics_linear": arch_42_literal_equation_physics_kinematics_linear,
    "43_literal_equation_geometry_surface_area_volume": arch_43_literal_equation_geometry_surface_area_volume,
    "44_literal_equation_reciprocal_fractions_resistance": arch_44_literal_equation_reciprocal_fractions_resistance,
    "45_linear_inequality_one_step_positive_coeff": arch_45_linear_inequality_one_step_positive_coeff,
    "46_linear_inequality_division_by_negative_reversal": arch_46_linear_inequality_division_by_negative_reversal,
    "47_linear_inequality_two_step_brackets": arch_47_linear_inequality_two_step_brackets,
    "48_linear_inequality_compound_double_boundary": arch_48_linear_inequality_compound_double_boundary,
    "49_linear_inequality_number_line_representation_svg": arch_49_linear_inequality_number_line_representation_svg,
    "50_linear_inequality_interval_and_set_builder_notation": arch_50_linear_inequality_interval_and_set_builder_notation,
}
