"""Grade 11 Mathematics — Equations and Inequalities Archetypes 26–50.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 1).
Reference: curriculum_docs_auto/Mathematics_Gr11/Term 1/02. Equations and inequalities.md

Covers Archetypes 26–50:
- 26–30: Nature of roots (discriminant classification, parameter k for equal/real/non-real roots, prove roots real for all k)
- 31–40: Quadratic inequalities (standard strict less/greater than, non-strict interval & disjoint, negative leading coefficient,
         common factor, difference of squares, expand & rearrange first, perfect squares, algebraic fraction inequalities)
- 41–45: Simultaneous equations (line and parabola, linear sum and product hyperbola, difference forms, line and circle, coordinates of intersection)
- 46–49: Word problems (consecutive integer products, rectangle dimensions from area/perimeter, right-angled triangle Pythagoras, speed-distance-time)
- 50: Comprehensive synthesis capstone
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade11_mathematics._math_common import (
    make_math_question,
    step,
    solution_graph,
    num,
    to_latex,
    nonzero,
)

TOPIC = "Equations and inequalities"
LO_PREFIX = "math11_eq_ineq"


# ---------------------------------------------------------------------------
# 26. Nature of Roots: Classify from Equation
# ---------------------------------------------------------------------------
def build_26_nature_of_roots_classify_from_equation(r: random.Random) -> Dict[str, Any]:
    case = r.choice(["perf_sq", "non_perf_sq", "zero", "negative"])
    if case == "perf_sq":
        a, b, c = 1, -5, 6  # delta = 25 - 24 = 1 (perf sq)
        delta = 1
        correct = "Real, rational and unequal"
        reason = f"\\Delta = ({b})^2 - 4({a})({c}) = {delta} > 0 and is a perfect square, so roots are real, rational and unequal."
        distractors = ["Real, irrational and unequal", "Real, rational and equal", "Non-real"]
    elif case == "non_perf_sq":
        a, b, c = 1, -4, 1  # delta = 16 - 4 = 12
        delta = 12
        correct = "Real, irrational and unequal"
        reason = f"\\Delta = ({b})^2 - 4({a})({c}) = {delta} > 0 but is not a perfect square, so roots are real, irrational and unequal."
        distractors = ["Real, rational and unequal", "Real, rational and equal", "Non-real"]
    elif case == "zero":
        a, b, c = 1, -6, 9  # delta = 36 - 36 = 0
        delta = 0
        correct = "Real, rational and equal"
        reason = f"\\Delta = ({b})^2 - 4({a})({c}) = 0, so roots are real, rational and equal."
        distractors = ["Real, rational and unequal", "Real, irrational and unequal", "Non-real"]
    else:
        a, b, c = 1, 2, 5  # delta = 4 - 20 = -16
        delta = -16
        correct = "Non-real"
        reason = f"\\Delta = ({b})^2 - 4({a})({c}) = {delta} < 0, so roots are non-real (imaginary)."
        distractors = ["Real, rational and unequal", "Real, irrational and unequal", "Real, rational and equal"]

    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    eq_latex = f"x^2 {sign_b}x {sign_c} = 0"

    options = [correct] + distractors
    r.shuffle(options)

    prompt = f"Without solving the equation, determine the **nature of the roots** of:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Determine nature of roots from discriminant",
        chain_type="classification",
        steps=[step(from_latex=f"\\Delta = ({b})^2 - 4({a})({c}) = {delta}", to_latex_str=correct, op="Calculate discriminant and classify", rule=reason)],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="26_nature_of_roots_classify_from_equation",
        learning_objective_id=f"{LO_PREFIX}_26",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=correct,
        sample_answer=correct,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": f"Compute Delta = {delta}", "marks": 1}, {"desc": f"Classification: {correct}", "marks": 1}]},
        hints={"nudge": "Calculate Δ = b² - 4ac first.", "concept": "Δ > 0 square: rational; Δ > 0 not square: irrational; Δ = 0: equal; Δ < 0: non-real.", "breakdown": reason},
        misconception_tags=["confusing_rational_and_irrational_roots"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 27. Nature of Roots: Condition for Equal Roots (Δ = 0)
# ---------------------------------------------------------------------------
def build_27_nature_of_roots_condition_for_equal_roots(r: random.Random) -> Dict[str, Any]:
    # x^2 + kx + c = 0 -> Delta = k^2 - 4c = 0 -> k^2 = 4c
    root_val = r.choice([2, 3, 4, 5, 6])
    c = root_val * root_val
    k_pos = 2 * root_val
    k_neg = -2 * root_val

    eq_latex = f"x^2 + kx + {c} = 0"
    ans_latex = f"k = {k_pos} \\quad \\text{{or}} \\quad k = {k_neg}"

    prompt = f"For which value(s) of $k$ will the equation have **equal (repeated) roots**?\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Find parameter k for equal roots",
        chain_type="equation",
        var="k",
        steps=[
            step(from_latex="\\Delta = 0", to_latex_str=f"k^2 - 4(1)({c}) = 0", op="Set discriminant to zero for equal roots", rule="Condition for equal roots: Delta = 0"),
            step(from_latex=f"k^2 - {4 * c} = 0", to_latex_str=f"k^2 = {4 * c}", op="Isolate k^2", rule=f"k^2 = {4*c}"),
            step(from_latex=f"k^2 = {4 * c}", to_latex_str=ans_latex, op="Take square roots", rule=f"k = ±{2*root_val}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="27_nature_of_roots_condition_for_equal_roots",
        learning_objective_id=f"{LO_PREFIX}_27",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"k = {k_pos} or k = {k_neg}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Set Delta = 0: k^2 - 4c = 0", "marks": 1}, {"desc": f"k^2 = {4*c}", "marks": 1}, {"desc": f"Both values k = ±{2*root_val}", "marks": 1}]},
        hints={"nudge": "For equal roots, set the discriminant Δ = b² - 4ac equal to 0.", "concept": "Δ = 0 \\implies k² - 4ac = 0. Remember to take both + and - square roots.", "breakdown": f"k² - 4(1)({c}) = 0 \\implies k² = {4*c} \\implies k = ±{2*root_val}."},
        misconception_tags=["forgetting_negative_value_of_k_for_equal_roots"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 28. Nature of Roots: Condition for Real Roots (Δ ≥ 0)
# ---------------------------------------------------------------------------
def build_28_nature_of_roots_condition_for_real_roots(r: random.Random) -> Dict[str, Any]:
    b = r.choice([4, 6, 8, 10])
    b_sq = b * b
    max_k = b_sq // 4

    eq_latex = f"x^2 - {b}x + k = 0"
    ans_latex = f"k \\le {max_k}"

    prompt = f"For which values of $k$ will the equation have **real roots**?\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Find condition on k for real roots",
        chain_type="inequality",
        var="k",
        steps=[
            step(from_latex="\\Delta \\ge 0", to_latex_str=f"(-{b})^2 - 4(1)(k) \\ge 0", op="Set discriminant >= 0 for real roots", rule="Condition for real roots: Delta >= 0"),
            step(from_latex=f"{b_sq} - 4k \\ge 0", to_latex_str=f"-4k \\ge -{b_sq}", op="Subtract b^2 from both sides", rule="Linear inequality rearrangement"),
            step(from_latex=f"-4k \\ge -{b_sq}", to_latex_str=ans_latex, op="Divide by -4 and reverse inequality sign", rule="Division by negative reverses inequality"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="28_nature_of_roots_condition_for_real_roots",
        learning_objective_id=f"{LO_PREFIX}_28",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"k <= {max_k}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Condition Delta >= 0", "marks": 1}, {"desc": f"{b_sq} - 4k >= 0", "marks": 1}, {"desc": f"Reverse inequality: k <= {max_k}", "marks": 1}]},
        hints={"nudge": "For real roots, the discriminant must be greater than or equal to zero: Δ ≥ 0.", "concept": "When dividing by -4, remember to reverse the inequality sign: ≥ becomes ≤.", "breakdown": f"({b})² - 4k ≥ 0 \\implies 4k ≤ {b_sq} \\implies k ≤ {max_k}."},
        misconception_tags=["forgetting_to_reverse_inequality_when_dividing_by_negative"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 29. Nature of Roots: Condition for Non-Real Roots (Δ < 0)
# ---------------------------------------------------------------------------
def build_29_nature_of_roots_condition_for_nonreal_roots(r: random.Random) -> Dict[str, Any]:
    b = r.choice([2, 4, 6, 8])
    b_sq = b * b
    min_k = b_sq // 4

    eq_latex = f"x^2 + {b}x + k = 0"
    ans_latex = f"k > {min_k}"

    prompt = f"For which values of $k$ will the equation have **non-real roots**?\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Find condition on k for non-real roots",
        chain_type="inequality",
        var="k",
        steps=[
            step(from_latex="\\Delta < 0", to_latex_str=f"{b}^2 - 4(1)(k) < 0", op="Set discriminant < 0 for non-real roots", rule="Condition for non-real roots: Delta < 0"),
            step(from_latex=f"{b_sq} - 4k < 0", to_latex_str=f"-4k < -{b_sq}", op="Subtract b^2", rule="Inequality isolation"),
            step(from_latex=f"-4k < -{b_sq}", to_latex_str=ans_latex, op="Divide by -4 and reverse inequality sign", rule="k > min_k"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="29_nature_of_roots_condition_for_nonreal_roots",
        learning_objective_id=f"{LO_PREFIX}_29",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"k > {min_k}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Condition Delta < 0", "marks": 1}, {"desc": f"{b_sq} - 4k < 0", "marks": 1}, {"desc": f"Solve k > {min_k}", "marks": 1}]},
        hints={"nudge": "For non-real roots, the discriminant must be strictly negative: Δ < 0.", "concept": "Δ < 0 means the expression under the square root is negative.", "breakdown": f"{b_sq} - 4k < 0 \\implies 4k > {b_sq} \\implies k > {min_k}."},
        misconception_tags=["using_less_than_or_equal_to_zero_for_non_real_roots"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 30. Nature of Roots: Prove Real for All k
# ---------------------------------------------------------------------------
def build_30_nature_of_roots_prove_real_for_all_k(r: random.Random) -> Dict[str, Any]:
    a_int = r.choice([1, 2, 3])
    # x^2 - 2ax + a^2 - k^2 = 0 -> Delta = 4a^2 - 4(a^2 - k^2) = 4k^2 >= 0
    eq_latex = f"x^2 - {2 * a_int}x + {a_int ** 2} = k^2"
    correct = "Since \\Delta = 4k^2 \\ge 0 for all real k, the roots are always real."
    distractors = [
        "The roots are only real if k > 0.",
        "The roots are non-real because k^2 is always positive.",
        "The roots are only real if k is an integer.",
    ]
    options = [correct] + distractors
    r.shuffle(options)

    prompt = (
        f"Consider the equation:\n\n$${eq_latex}$$\n\n"
        f"Which statement correctly proves the nature of the roots for all real values of $k$?"
    )

    sol = solution_graph(
        goal="Prove roots are real for all real k by showing Delta is a perfect square >= 0",
        chain_type="proof",
        steps=[
            step(from_latex=f"x^2 - {2 * a_int}x + ({a_int ** 2} - k^2) = 0", to_latex_str=f"\\Delta = (-{2 * a_int})^2 - 4(1)({a_int ** 2} - k^2)", op="Form standard quadratic and calculate Delta", rule="b^2 - 4ac"),
            step(from_latex=f"\\Delta = {4 * a_int ** 2} - {4 * a_int ** 2} + 4k^2", to_latex_str="\\Delta = 4k^2 \\ge 0 \\; \\forall k \\in \\mathbb{R}", op="Simplify Delta to 4k^2", rule="A square is always >= 0 for all real numbers"),
        ],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="30_nature_of_roots_prove_real_for_all_k",
        learning_objective_id=f"{LO_PREFIX}_30",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=correct,
        sample_answer=correct,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": "Simplify Delta to 4k^2", "marks": 1}, {"desc": "State that 4k^2 >= 0 for all real k", "marks": 1}]},
        hints={"nudge": "Bring k² to the LHS to write the equation in standard form: x² - 2ax + (a² - k²) = 0.", "concept": "Any real number squared is non-negative: k² ≥ 0, so 4k² ≥ 0.", "breakdown": f"Δ = 4k² ≥ 0 for all real k, which guarantees real roots."},
        misconception_tags=["assuming_k_must_be_positive_for_k_squared_to_be_positive"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="medium",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 31. Quadratic Inequality: Standard Strict Less Than (< 0)
# ---------------------------------------------------------------------------
def build_31_quadratic_inequality_standard_less_than(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-4, -3, -2, -1, 1, 2])
    b = a + r.choice([2, 3, 4, 5])
    # (x - a)(x - b) < 0 -> a < x < b
    sum_ab = a + b
    prod_ab = a * b
    sign_sum = f"- {sum_ab}" if sum_ab >= 0 else f"+ {abs(sum_ab)}"
    sign_prod = f"+ {prod_ab}" if prod_ab >= 0 else f"- {abs(prod_ab)}"

    eq_latex = f"x^2 {sign_sum}x {sign_prod} < 0"
    ans_latex = f"{a} < x < {b}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve strict quadratic inequality less than zero",
        chain_type="inequality",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"(x - {a})(x - {b}) < 0", op="Factorise quadratic into linear factors", rule="Trinomial factorisation"),
            step(from_latex=f"\\text{{Critical values: }} x = {a} \\text{{ or }} x = {b}", to_latex_str=ans_latex, op="Determine region between critical values where parabola is below x-axis", rule="Standard interval a < x < b"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="31_quadratic_inequality_standard_less_than",
        learning_objective_id=f"{LO_PREFIX}_31",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{a} < x and x < {b}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Factorise trinomial", "marks": 1}, {"desc": f"Critical values {a} and {b}", "marks": 1}, {"desc": f"Single interval {a} < x < {b}", "marks": 1}]},
        hints={"nudge": f"Factorise to find the critical values: x = {a} and x = {b}.", "concept": "For a concave-up parabola, f(x) < 0 BETWEEN the two critical values.", "breakdown": f"(x - {a})(x - {b}) < 0 \\implies {a} < x < {b}."},
        misconception_tags=["writing_disjoint_inequalities_for_less_than_zero"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 32. Quadratic Inequality: Standard Strict Greater Than (> 0)
# ---------------------------------------------------------------------------
def build_32_quadratic_inequality_standard_greater_than(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, -1, 1, 2])
    b = a + r.choice([2, 3, 4, 5])
    # (x - a)(x - b) > 0 -> x < a or x > b
    sum_ab = a + b
    prod_ab = a * b
    sign_sum = f"- {sum_ab}" if sum_ab >= 0 else f"+ {abs(sum_ab)}"
    sign_prod = f"+ {prod_ab}" if prod_ab >= 0 else f"- {abs(prod_ab)}"

    eq_latex = f"x^2 {sign_sum}x {sign_prod} > 0"
    ans_latex = f"x < {a} \\quad \\text{{or}} \\quad x > {b}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve strict quadratic inequality greater than zero",
        chain_type="inequality",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"(x - {a})(x - {b}) > 0", op="Factorise quadratic", rule="Trinomial factorisation"),
            step(from_latex=f"\\text{{Critical values: }} x = {a} \\text{{ or }} x = {b}", to_latex_str=ans_latex, op="Determine disjoint intervals outside roots where parabola is above x-axis", rule="Disjoint intervals x < a or x > b"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="32_quadratic_inequality_standard_greater_than",
        learning_objective_id=f"{LO_PREFIX}_32",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x < {a} or x > {b}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Factorise trinomial", "marks": 1}, {"desc": f"Critical values {a} and {b}", "marks": 1}, {"desc": f"Disjoint intervals x < {a} or x > {b}", "marks": 1}]},
        hints={"nudge": f"Find the critical values: x = {a} and x = {b}.", "concept": "For a concave-up parabola, f(x) > 0 OUTSIDE the roots: x < smaller or x > larger.", "breakdown": f"(x - {a})(x - {b}) > 0 \\implies x < {a} or x > {b}."},
        misconception_tags=["joining_disjoint_inequalities_with_illegal_compound_notation"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 33. Quadratic Inequality: Non-Strict Interval (≤ 0)
# ---------------------------------------------------------------------------
def build_33_quadratic_inequality_non_strict_interval(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-4, -3, -2, -1, 1, 2])
    b = a + r.choice([2, 3, 4])
    sum_ab = a + b
    prod_ab = a * b
    sign_sum = f"- {sum_ab}" if sum_ab >= 0 else f"+ {abs(sum_ab)}"
    sign_prod = f"+ {prod_ab}" if prod_ab >= 0 else f"- {abs(prod_ab)}"

    eq_latex = f"x^2 {sign_sum}x {sign_prod} \\le 0"
    ans_latex = f"{a} \\le x \\le {b}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve non-strict quadratic inequality less than or equal to zero",
        chain_type="inequality",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"(x - {a})(x - {b}) \\le 0", op="Factorise trinomial", rule="Trinomial factorisation"),
            step(from_latex=f"\\text{{Critical values: }} x = {a} \\text{{ and }} x = {b}", to_latex_str=ans_latex, op="Combine endpoints and interior interval", rule="Inclusive interval a <= x <= b"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="33_quadratic_inequality_non_strict_interval",
        learning_objective_id=f"{LO_PREFIX}_33",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{a} <= x and x <= {b}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Factorise", "marks": 1}, {"desc": f"Critical values {a}, {b}", "marks": 1}, {"desc": f"Closed interval {a} <= x <= {b}", "marks": 1}]},
        hints={"nudge": "Because the inequality has ≤, the endpoints are included in the solution.", "concept": "f(x) ≤ 0 gives a closed interval [a; b].", "breakdown": f"{a} ≤ x ≤ {b}."},
        misconception_tags=["using_strict_inequality_when_original_is_non_strict"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 34. Quadratic Inequality: Non-Strict Disjoint (≥ 0)
# ---------------------------------------------------------------------------
def build_34_quadratic_inequality_non_strict_disjoint(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, -1, 1, 2])
    b = a + r.choice([2, 3, 4])
    sum_ab = a + b
    prod_ab = a * b
    sign_sum = f"- {sum_ab}" if sum_ab >= 0 else f"+ {abs(sum_ab)}"
    sign_prod = f"+ {prod_ab}" if prod_ab >= 0 else f"- {abs(prod_ab)}"

    eq_latex = f"x^2 {sign_sum}x {sign_prod} \\ge 0"
    ans_latex = f"x \\le {a} \\quad \\text{{or}} \\quad x \\ge {b}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve non-strict quadratic inequality greater than or equal to zero",
        chain_type="inequality",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"(x - {a})(x - {b}) \\ge 0", op="Factorise trinomial", rule="Trinomial factorisation"),
            step(from_latex=f"\\text{{Critical values: }} x = {a} \\text{{ and }} x = {b}", to_latex_str=ans_latex, op="Combine endpoints and exterior regions", rule="Disjoint inclusive intervals"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="34_quadratic_inequality_non_strict_disjoint",
        learning_objective_id=f"{LO_PREFIX}_34",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x <= {a} or x >= {b}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Factorise", "marks": 1}, {"desc": f"Critical values {a}, {b}", "marks": 1}, {"desc": f"Disjoint intervals x <= {a} or x >= {b}", "marks": 1}]},
        hints={"nudge": "For ≥ 0, the solution lies on or outside the critical values.", "concept": "x ≤ smaller or x ≥ larger.", "breakdown": f"x ≤ {a} or x ≥ {b}."},
        misconception_tags=["omitting_equality_bars_in_non_strict_inequality"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 35. Quadratic Inequality: Negative Leading Coefficient
# ---------------------------------------------------------------------------
def build_35_quadratic_inequality_negative_leading_coef(r: random.Random) -> Dict[str, Any]:
    a = r.choice([-3, -2, -1, 1])
    b = a + r.choice([2, 3, 4])
    # -x^2 + (a+b)x - ab > 0
    # Multiply by -1: x^2 - (a+b)x + ab < 0 -> a < x < b
    sum_ab = a + b
    prod_ab = a * b
    sign_sum = f"+ {sum_ab}" if sum_ab >= 0 else f"- {abs(sum_ab)}"
    sign_prod = f"- {prod_ab}" if prod_ab >= 0 else f"+ {abs(prod_ab)}"

    eq_latex = f"-x^2 {sign_sum}x {sign_prod} > 0"
    ans_latex = f"{a} < x < {b}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic inequality with negative x^2 coefficient",
        chain_type="inequality",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x^2 - {sum_ab}x + {prod_ab} < 0", op="Multiply entire inequality by -1 and reverse > to <", rule="Multiplication by negative reverses inequality sign"),
            step(from_latex=f"(x - {a})(x - {b}) < 0", to_latex_str=ans_latex, op="Factorise and determine interval between roots", rule=f"{a} < x < {b}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="35_quadratic_inequality_negative_leading_coef",
        learning_objective_id=f"{LO_PREFIX}_35",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{a} < x and x < {b}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Multiply by -1 and reverse inequality sign", "marks": 1}, {"desc": "Factorise", "marks": 1}, {"desc": f"Solution {a} < x < {b}", "marks": 1}]},
        hints={"nudge": "Multiply by -1 first, and remember to FLIP the inequality sign (> becomes <).", "concept": "Always work with a positive x² coefficient to avoid graphing errors.", "breakdown": f"x² - {sum_ab}x + {prod_ab} < 0 \\implies (x - {a})(x - {b}) < 0 \\implies {a} < x < {b}."},
        misconception_tags=["forgetting_to_reverse_inequality_sign_when_multiplying_by_negative_one"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 36. Quadratic Inequality: Common Factor
# ---------------------------------------------------------------------------
def build_36_quadratic_inequality_common_factor(r: random.Random) -> Dict[str, Any]:
    k = r.choice([3, 4, 5, 6])
    # x^2 - kx <= 0 -> x(x - k) <= 0 -> 0 <= x <= k
    eq_latex = f"x^2 - {k}x \\le 0"
    ans_latex = f"0 \\le x \\le {k}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic inequality with no constant term",
        chain_type="inequality",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x(x - {k}) \\le 0", op="Factor out x as common factor", rule="Common monomial factor"),
            step(from_latex=f"\\text{{Critical values: }} x = 0 \\text{{ and }} x = {k}", to_latex_str=ans_latex, op="Region between critical values", rule="0 <= x <= k"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="36_quadratic_inequality_common_factor",
        learning_objective_id=f"{LO_PREFIX}_36",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"0 <= x and x <= {k}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Factor out x", "marks": 1}, {"desc": f"Critical values 0 and {k}", "marks": 1}, {"desc": f"Interval 0 <= x <= {k}", "marks": 1}]},
        hints={"nudge": "Do NOT divide by x! Factor out x: x(x - k) ≤ 0.", "concept": "The critical values are x = 0 and x = k.", "breakdown": f"x(x - {k}) ≤ 0 \\implies 0 ≤ x ≤ {k}."},
        misconception_tags=["dividing_inequality_by_x"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 37. Quadratic Inequality: Difference of Squares
# ---------------------------------------------------------------------------
def build_37_quadratic_inequality_difference_of_squares(r: random.Random) -> Dict[str, Any]:
    k = r.choice([2, 3, 4, 5])
    sq = k * k
    eq_latex = f"x^2 - {sq} > 0"
    ans_latex = f"x < -{k} \\quad \\text{{or}} \\quad x > {k}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve difference of squares inequality",
        chain_type="inequality",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"(x - {k})(x + {k}) > 0", op="Factorise as difference of squares", rule="A² - B² = (A - B)(A + B)"),
            step(from_latex=f"\\text{{Critical values: }} x = -{k} \\text{{ and }} x = {k}", to_latex_str=ans_latex, op="Exterior disjoint intervals", rule="x < -k or x > k"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="37_quadratic_inequality_difference_of_squares",
        learning_objective_id=f"{LO_PREFIX}_37",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x < -{k} or x > {k}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Difference of squares factorisation", "marks": 1}, {"desc": f"Critical values ±{k}", "marks": 1}, {"desc": f"Disjoint solution x < -{k} or x > {k}", "marks": 1}]},
        hints={"nudge": f"Factorise into (x - {k})(x + {k}) > 0.", "concept": "For > 0, the solution lies outside the two critical values.", "breakdown": f"x < -{k} or x > {k}."},
        misconception_tags=["simply_taking_square_root_to_write_x_greater_than_k"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 38. Quadratic Inequality: Rearrange First
# ---------------------------------------------------------------------------
def build_38_quadratic_inequality_rearrange_first(r: random.Random) -> Dict[str, Any]:
    # x(x - 3) <= 4 -> x^2 - 3x - 4 <= 0 -> (x-4)(x+1) <= 0 -> -1 <= x <= 4
    case = r.choice([
        (3, 4, 4, -1),   # x(x-3) <= 4 -> -1 <= x <= 4
        (2, 8, 4, -2),   # x(x-2) <= 8 -> -2 <= x <= 4
        (1, 6, 3, -2),   # x(x-1) <= 6 -> -2 <= x <= 3
        (4, 5, 5, -1),   # x(x-4) <= 5 -> -1 <= x <= 5
    ])
    p, c, r_hi, r_lo = case

    eq_latex = f"x(x - {p}) \\le {c}"
    ans_latex = f"{r_lo} \\le x \\le {r_hi}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Expand and rearrange quadratic inequality before solving",
        chain_type="inequality",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x^2 - {p}x - {c} \\le 0", op=f"Expand LHS and subtract {c} to set inequality to 0", rule="Standard form for quadratic inequality"),
            step(from_latex=f"x^2 - {p}x - {c} \\le 0", to_latex_str=f"(x - {r_hi})(x - {r_lo}) \\le 0", op="Factorise trinomial", rule="Trinomial factorisation"),
            step(from_latex=f"\\text{{Critical values: }} x = {r_lo} \\text{{ and }} x = {r_hi}", to_latex_str=ans_latex, op="Region between critical values", rule=f"{r_lo} <= x <= {r_hi}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="38_quadratic_inequality_rearrange_first",
        learning_objective_id=f"{LO_PREFIX}_38",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{r_lo} <= x and x <= {r_hi}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Expand and standard form <= 0", "marks": 1}, {"desc": "Factorise", "marks": 1}, {"desc": "Critical values", "marks": 1}, {"desc": f"Interval {ans_latex}", "marks": 1}]},
        hints={"nudge": f"Expand x(x - {p}) and subtract {c} from both sides before finding critical values.", "concept": "You CANNOT determine critical values until one side is 0.", "breakdown": f"x² - {p}x - {c} ≤ 0 \\implies (x - {r_hi})(x + {abs(r_lo)}) ≤ 0 \\implies {ans_latex}."},
        misconception_tags=["finding_critical_values_before_setting_rhs_to_zero"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 39. Quadratic Inequality: Perfect Square
# ---------------------------------------------------------------------------
def build_39_quadratic_inequality_perfect_square(r: random.Random) -> Dict[str, Any]:
    a = r.randint(2, 7)
    q_type = r.choice(["strict_pos", "non_strict_neg"])
    
    if q_type == "strict_pos":
        prompt = f"Solve for $x$:\n\n$$(x - {a})^2 > 0$$"
        correct = f"x \\ne {a}"
        distractors = [f"x > {a}", f"x < {a}", "No solution"]
        reason = f"A square is always positive or zero. $(x - {a})^2 = 0$ when $x = {a}$. For all other values of $x$, $(x - {a})^2 > 0$. Hence $x \\ne {a}$."
    else:
        prompt = f"Solve for $x$:\n\n$$(x - {a})^2 \\le 0$$"
        correct = f"x = {a}"
        distractors = [f"x \\le {a}", "No solution", f"x < {a}"]
        reason = f"A real square cannot be negative. Therefore $(x - {a})^2 \\le 0$ is only satisfied when $(x - {a})^2 = 0$, giving the single solution $x = {a}$."

    options = [f"${correct}$"] + [f"${d}$" for d in distractors]
    r.shuffle(options)

    sol = solution_graph(
        goal="Solve perfect square inequality",
        chain_type="inequality",
        var="x",
        steps=[step(from_latex=f"(x - {a})^2", to_latex_str=correct, op="Apply non-negative property of real squares", rule=reason)],
        final_latex=correct,
    )

    q = make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="39_quadratic_inequality_perfect_square",
        learning_objective_id=f"{LO_PREFIX}_39",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="mcq",
        question_type="mcq",
        answer_latex=f"${correct}$",
        sample_answer=f"${correct}$",
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": "Analyze non-negative property of square", "marks": 1}, {"desc": f"Correct solution {correct}", "marks": 1}]},
        hints={"nudge": "Remember that a squared real number is ALWAYS greater than or equal to 0.", "concept": "(x - a)² ≥ 0 for all real x.", "breakdown": reason},
        misconception_tags=["assuming_perfect_square_inequalities_always_have_interval_solutions"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=2,
        difficulty="medium",
    )
    q["options"] = options
    return q


# ---------------------------------------------------------------------------
# 40. Quadratic Inequality: Algebraic Fraction
# ---------------------------------------------------------------------------
def build_40_quadratic_inequality_algebraic_fraction(r: random.Random) -> Dict[str, Any]:
    # (x - a)/(x - b) >= 0 where a < b
    # Critical values are a (included) and b (excluded due to zero denominator!)
    # Solution: x <= a or x > b
    a = r.choice([1, 2, 3])
    b = a + r.choice([2, 3, 4])

    eq_latex = f"\\frac{{x - {a}}}{{x - {b}}} \\ge 0"
    ans_latex = f"x \\le {a} \\quad \\text{{or}} \\quad x > {b}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve rational inequality noting excluded denominator value",
        chain_type="inequality",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"\\text{{Critical values: }} x = {a} \\text{{ (numerator)}}, \\; x = {b} \\text{{ (denominator)}}", op="Identify critical values", rule="Roots of numerator and denominator"),
            step(from_latex=f"x \\ne {b}", to_latex_str=ans_latex, op=f"Determine signs on intervals, noting x = {b} cannot be included", rule=f"x <= {a} or x > {b}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="40_quadratic_inequality_algebraic_fraction",
        learning_objective_id=f"{LO_PREFIX}_40",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x <= {a} or x > {b}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Critical values", "marks": 1}, {"desc": f"Exclude x = {b} (denominator != 0)", "marks": 1}, {"desc": f"Solution {ans_latex}", "marks": 1}]},
        hints={"nudge": f"The quotient has the same sign as the product (x - {a})(x - {b}), BUT x cannot equal {b}!", "concept": "Division by zero is undefined. The denominator endpoint is ALWAYS an open circle (strictly >).", "breakdown": f"x ≤ {a} (included) or x > {b} (excluded)."},
        misconception_tags=["including_denominator_root_in_non_strict_inequality"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 41. Simultaneous Equations: Line and Parabola
# ---------------------------------------------------------------------------
def build_41_simultaneous_linear_quadratic_substitution_parabola(r: random.Random) -> Dict[str, Any]:
    # y = x + d
    # y = x^2 - c
    # x^2 - x - (c + d) = 0
    # Let roots be x1, x2 (integers)
    x1 = r.choice([2, 3, 4])
    x2 = r.choice([-3, -2, -1])
    # x^2 - x - 6 = 0 -> x1 = 3, x2 = -2. sum = 1, prod = -6
    # x^2 - (x1+x2)x + x1*x2 = 0
    # If line is y = mx + d: let m = 1, so x1 + x2 = 1.
    # Pairs with sum = 1: (2, -1) -> prod = -2; (3, -2) -> prod = -6; (4, -3) -> prod = -12
    pair = r.choice([(2, -1, 1, 2), (3, -2, 1, 6), (4, -3, 1, 12)])
    x_pos, x_neg, m_val, cd_sum = pair
    d = r.choice([1, 2])
    c = cd_sum - d

    y1 = x_pos + d
    y2 = x_neg + d

    eq1_latex = f"y - x = {d}"
    eq2_latex = f"y = x^2 - {c}"
    ans_latex = f"(x = {x_pos}, \\; y = {y1}) \\quad \\text{{or}} \\quad (x = {x_neg}, \\; y = {y2})"

    prompt = f"Solve simultaneously for $x$ and $y$:\n\n$$\\begin{{aligned}} {eq1_latex} \\\\[4pt] {eq2_latex} \\end{{aligned}}$$"

    sol = solution_graph(
        goal="Solve simultaneous linear and quadratic equations by substitution",
        chain_type="system",
        steps=[
            step(from_latex=eq1_latex, to_latex_str=f"y = x + {d}", op="Isolate y in linear equation", rule="Linear substitution expression"),
            step(from_latex=f"x + {d} = x^2 - {c}", to_latex_str=f"x^2 - x - {cd_sum} = 0", op="Substitute into quadratic equation and set to zero", rule="Substitution into quadratic"),
            step(from_latex=f"(x - {x_pos})(x - {x_neg}) = 0", to_latex_str=f"x = {x_pos} \\quad \\text{{or}} \\quad x = {x_neg}", op="Factorise to solve for x", rule="Zero product rule"),
            step(from_latex=f"y = x + {d}", to_latex_str=ans_latex, op="Substitute each x-value back to find corresponding y-values", rule="Find corresponding y-coordinates"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="41_simultaneous_linear_quadratic_substitution_parabola",
        learning_objective_id=f"{LO_PREFIX}_41",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"(x={x_pos}, y={y1}) or (x={x_neg}, y={y2})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 5, "steps": [{"desc": f"Isolate y = x + {d}", "marks": 1}, {"desc": f"Substitute and form quadratic x² - x - {cd_sum} = 0", "marks": 1}, {"desc": f"Values of x: {x_pos} and {x_neg}", "marks": 1}, {"desc": f"First pair ({x_pos}; {y1})", "marks": 1}, {"desc": f"Second pair ({x_neg}; {y2})", "marks": 1}]},
        hints={"nudge": f"From the first equation, make y the subject: y = x + {d}. Substitute this into the second equation.", "concept": "Solve the quadratic equation for x, then substitute each x back into y = x + d to find the corresponding y.", "breakdown": f"x² - x - {cd_sum} = 0 \\implies x = {x_pos} (y = {y1}) or x = {x_neg} (y = {y2})."},
        misconception_tags=["pairing_wrong_x_and_y_values_in_simultaneous_equations"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 42. Simultaneous Equations: Sum and Product (Hyperbola)
# ---------------------------------------------------------------------------
def build_42_simultaneous_linear_quadratic_hyperbola_product(r: random.Random) -> Dict[str, Any]:
    # x + y = s and xy = p
    # x and y are roots of t^2 - st + p = 0
    r1 = r.choice([2, 3, 4, 5])
    r2 = r.choice([1, 2, 3])
    while r1 == r2:
        r2 = r.choice([1, 2, 3])
    s = r1 + r2
    p = r1 * r2

    eq1_latex = f"x + y = {s}"
    eq2_latex = f"xy = {p}"
    ans_latex = f"(x = {r1}, \\; y = {r2}) \\quad \\text{{or}} \\quad (x = {r2}, \\; y = {r1})"

    prompt = f"Solve simultaneously for $x$ and $y$:\n\n$$\\begin{{aligned}} {eq1_latex} \\\\[4pt] {eq2_latex} \\end{{aligned}}$$"

    sol = solution_graph(
        goal="Solve sum and product simultaneous system",
        chain_type="system",
        steps=[
            step(from_latex=eq1_latex, to_latex_str=f"y = {s} - x", op="Make y the subject of linear equation", rule="Linear isolation"),
            step(from_latex=f"x({s} - x) = {p}", to_latex_str=f"x^2 - {s}x + {p} = 0", op="Substitute into xy = p and rearrange to standard quadratic", rule="Quadratic equation in x"),
            step(from_latex=f"(x - {r1})(x - {r2}) = 0", to_latex_str=f"x = {r1} \\text{{ or }} x = {r2}", op="Factorise to solve for x", rule="Zero product rule"),
            step(from_latex=f"y = {s} - x", to_latex_str=ans_latex, op="Compute corresponding y-values", rule="Pair coordinates"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="42_simultaneous_linear_quadratic_hyperbola_product",
        learning_objective_id=f"{LO_PREFIX}_42",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"(x={r1}, y={r2}) or (x={r2}, y={r1})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": f"Substitute y = {s} - x", "marks": 1}, {"desc": f"Form quadratic x² - {s}x + {p} = 0", "marks": 1}, {"desc": "Find both x values", "marks": 1}, {"desc": "Find both coordinate pairs", "marks": 1}]},
        hints={"nudge": f"Express y as ({s} - x) and substitute into xy = {p}.", "concept": "x({s} - x) = {p} \\implies x² - {s}x + {p} = 0.", "breakdown": f"x = {r1} gives y = {r2}; x = {r2} gives y = {r1}."},
        misconception_tags=["forgetting_the_symmetric_second_solution_pair"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 43. Simultaneous Equations: Difference Form with xy Term
# ---------------------------------------------------------------------------
def build_43_simultaneous_linear_quadratic_difference_forms(r: random.Random) -> Dict[str, Any]:
    # y - 2x = 1 -> y = 2x + 1
    # x^2 + xy = c
    # x^2 + x(2x + 1) = 3x^2 + x = c
    # Let x = 1 -> 3(1) + 1 = 4. Let c = 4.
    # 3x^2 + x - 4 = 0 -> (3x + 4)(x - 1) = 0 -> x = 1 (y = 3) or x = -4/3 (y = -5/3)
    eq1_latex = "y - 2x = 1"
    eq2_latex = "x^2 + xy = 4"
    ans_latex = "(x = 1, \\; y = 3) \\quad \\text{or} \\quad \\left(x = -\\frac{4}{3}, \\; y = -\\frac{5}{3}\\right)"

    prompt = f"Solve simultaneously for $x$ and $y$:\n\n$$\\begin{{aligned}} {eq1_latex} \\\\[4pt] {eq2_latex} \\end{{aligned}}$$"

    sol = solution_graph(
        goal="Solve simultaneous system with xy cross-term",
        chain_type="system",
        steps=[
            step(from_latex=eq1_latex, to_latex_str="y = 2x + 1", op="Isolate y in linear equation", rule="Linear equation isolation"),
            step(from_latex="x^2 + x(2x + 1) = 4", to_latex_str="3x^2 + x - 4 = 0", op="Substitute into second equation and simplify", rule="Substitution into quadratic"),
            step(from_latex="3x^2 + x - 4 = 0", to_latex_str="x = 1 \\quad \\text{or} \\quad x = -\\frac{4}{3}", op="Factorise: (x - 1)(3x + 4) = 0", rule="Zero product rule"),
            step(from_latex="y = 2x + 1", to_latex_str=ans_latex, op="Compute corresponding y-values", rule="Pair solutions"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="43_simultaneous_linear_quadratic_difference_forms",
        learning_objective_id=f"{LO_PREFIX}_43",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy="(x=1, y=3) or (x=-4/3, y=-5/3)",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 5, "steps": [{"desc": "y = 2x + 1", "marks": 1}, {"desc": "Quadratic 3x² + x - 4 = 0", "marks": 1}, {"desc": "Values of x", "marks": 1}, {"desc": "Pair (1; 3)", "marks": 1}, {"desc": "Pair (-4/3; -5/3)", "marks": 1}]},
        hints={"nudge": "Express y = 2x + 1 from the first equation, then substitute into x² + xy = 4.", "concept": "x² + x(2x + 1) = x² + 2x² + x = 3x² + x.", "breakdown": "3x² + x - 4 = 0 \\implies (x - 1)(3x + 4) = 0. When x = 1, y = 3. When x = -4/3, y = -5/3."},
        misconception_tags=["distributing_x_incorrectly_into_binomial_y"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 44. Simultaneous Equations: Line and Circle Intersection
# ---------------------------------------------------------------------------
def build_44_simultaneous_linear_quadratic_circle_intersection(r: random.Random) -> Dict[str, Any]:
    # x + y = a and x^2 + y^2 = r^2
    # e.g. x + y = 7, x^2 + y^2 = 25 -> (4, 3) and (3, 4)
    # or x + y = 1, x^2 + y^2 = 25 -> (4, -3) and (-3, 4)
    case = r.choice([
        (7, 25, 4, 3),   # x=4, y=3 or x=3, y=4
        (1, 25, 4, -3),  # x=4, y=-3 or x=-3, y=4
        (5, 13, 3, 2),   # x=3, y=2 or x=2, y=3
    ])
    sum_a, r_sq, x1, y1 = case
    x2, y2 = y1, x1

    eq1_latex = f"x + y = {sum_a}"
    eq2_latex = f"x^2 + y^2 = {r_sq}"
    ans_latex = f"(x = {x1}, \\; y = {y1}) \\quad \\text{{or}} \\quad (x = {x2}, \\; y = {y2})"

    prompt = f"Solve simultaneously for $x$ and $y$:\n\n$$\\begin{{aligned}} {eq1_latex} \\\\[4pt] {eq2_latex} \\end{{aligned}}$$"

    sol = solution_graph(
        goal="Solve line and circle simultaneous equations",
        chain_type="system",
        steps=[
            step(from_latex=eq1_latex, to_latex_str=f"y = {sum_a} - x", op="Isolate y", rule="Linear equation rearrangement"),
            step(from_latex=f"x^2 + ({sum_a} - x)^2 = {r_sq}", to_latex_str=f"2x^2 - {2 * sum_a}x + {sum_a ** 2 - r_sq} = 0", op="Substitute and expand circle equation", rule="Substitution"),
            step(from_latex=f"x^2 - {sum_a}x + {(sum_a ** 2 - r_sq) // 2} = 0", to_latex_str=f"x = {x1} \\quad \\text{{or}} \\quad x = {x2}", op="Divide by 2 and factorise", rule="Zero product rule"),
            step(from_latex=f"y = {sum_a} - x", to_latex_str=ans_latex, op="Compute corresponding y-values", rule="Pair solutions"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="44_simultaneous_linear_quadratic_circle_intersection",
        learning_objective_id=f"{LO_PREFIX}_44",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"(x={x1}, y={y1}) or (x={x2}, y={y2})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 5, "steps": [{"desc": f"y = {sum_a} - x", "marks": 1}, {"desc": f"Expand ({sum_a} - x)²", "marks": 1}, {"desc": "Quadratic equation in x", "marks": 1}, {"desc": "Values for x", "marks": 1}, {"desc": "Both pairs of coordinates", "marks": 1}]},
        hints={"nudge": f"Substitute y = {sum_a} - x into x² + y² = {r_sq}.", "concept": "Remember to expand ({sum_a} - x)² correctly: {sum_a}² - 2({sum_a})x + x².", "breakdown": f"2x² - {2*sum_a}x + {sum_a**2 - r_sq} = 0 \\implies x = {x1} or x = {x2}."},
        misconception_tags=["expanding_binomial_squared_without_middle_term_in_simultaneous"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 45. Simultaneous: Interpret Points of Intersection
# ---------------------------------------------------------------------------
def build_45_simultaneous_quadratic_interpret_intersection_points(r: random.Random) -> Dict[str, Any]:
    # Find the coordinates of the points of intersection of y = 2x - 1 and y = x^2 - 4
    # x^2 - 2x - 3 = 0 -> (x-3)(x+1) = 0 -> x = 3 (y = 5) and x = -1 (y = -3)
    x1, x2 = 3, -1
    y1 = 2 * x1 - 1  # 5
    y2 = 2 * x2 - 1  # -3

    ans_latex = f"(3; 5) \\quad \\text{{and}} \\quad (-1; -3)"
    prompt = "Find the coordinates of the points of intersection of the line $y = 2x - 1$ and the parabola $y = x^2 - 4$."

    sol = solution_graph(
        goal="Find intersection points of line and parabola",
        chain_type="system",
        steps=[
            step(from_latex="x^2 - 4 = 2x - 1", to_latex_str="x^2 - 2x - 3 = 0", op="Equate expressions for y", rule="Intersection condition"),
            step(from_latex="(x - 3)(x + 1) = 0", to_latex_str="x = 3 \\quad \\text{or} \\quad x = -1", op="Factorise to find x-coordinates", rule="Zero product rule"),
            step(from_latex="y = 2x - 1", to_latex_str=ans_latex, op="Compute corresponding y-coordinates and state points", rule="State coordinate pairs"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="45_simultaneous_quadratic_interpret_intersection_points",
        learning_objective_id=f"{LO_PREFIX}_45",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy="(3, 5) and (-1, -3)",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Equate y-values: x² - 4 = 2x - 1", "marks": 1}, {"desc": "Solve for x: x = 3 or x = -1", "marks": 1}, {"desc": "Point (3; 5)", "marks": 1}, {"desc": "Point (-1; -3)", "marks": 1}]},
        hints={"nudge": "Equate the two functions: x² - 4 = 2x - 1.", "concept": "Points of intersection occur where both graphs have identical (x; y) coordinates.", "breakdown": "x² - 2x - 3 = 0 \\implies x = 3 (y = 5) and x = -1 (y = -3)."},
        misconception_tags=["giving_only_x_values_when_points_are_requested"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 46. Word Problem: Consecutive Integer Product
# ---------------------------------------------------------------------------
def build_46_word_problem_consecutive_integers_product(r: random.Random) -> Dict[str, Any]:
    n = r.choice([5, 6, 7, 8, 9, 11, 12])
    prod = n * (n + 1)
    ans_latex = f"{n} \\text{{ and }} {n + 1}"

    prompt = f"The product of two consecutive positive integers is ${prod}$. Determine the two integers."

    sol = solution_graph(
        goal="Solve quadratic word problem for consecutive integers",
        chain_type="word_problem",
        var="x",
        steps=[
            step(from_latex=f"x(x + 1) = {prod}", to_latex_str=f"x^2 + x - {prod} = 0", op="Form quadratic equation from problem statement", rule="Consecutive integers x and x+1"),
            step(from_latex=f"(x - {n})(x + {n + 1}) = 0", to_latex_str=f"x = {n} \\quad (x = -{n + 1} \\text{{ rejected as integers are positive}})", op="Factorise and reject negative root", rule="x > 0 restriction"),
            step(from_latex=f"x = {n}", to_latex_str=ans_latex, op=f"Find consecutive pair: {n} and {n+1}", rule="State integers"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="46_word_problem_consecutive_integers_product",
        learning_objective_id=f"{LO_PREFIX}_46",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{n} and {n+1}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": f"Equation x(x + 1) = {prod}", "marks": 1}, {"desc": f"x² + x - {prod} = 0", "marks": 1}, {"desc": f"Solve x = {n} (reject -{n+1})", "marks": 1}, {"desc": f"Integers: {n} and {n+1}", "marks": 1}]},
        hints={"nudge": "Let the two positive integers be x and x + 1. Their product is x(x + 1).", "concept": "Form the quadratic x² + x - prod = 0 and reject the negative solution.", "breakdown": f"x² + x - {prod} = 0 \\implies (x - {n})(x + {n+1}) = 0 \\implies x = {n}. The numbers are {n} and {n+1}."},
        misconception_tags=["forgetting_to_reject_negative_root_when_positive_integers_specified"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 47. Word Problem: Rectangle Perimeter and Area
# ---------------------------------------------------------------------------
def build_47_word_problem_rectangle_perimeter_area(r: random.Random) -> Dict[str, Any]:
    # Length L, Width W: L + W = semi_perim, L * W = area
    l_val = r.choice([8, 10, 12, 14, 15])
    w_val = r.choice([3, 4, 5, 6])
    while l_val <= w_val:
        l_val += 5

    perim = 2 * (l_val + w_val)
    area = l_val * w_val
    semi = l_val + w_val

    ans_latex = f"\\text{{Length}} = {l_val}\\text{{ m}}, \\quad \\text{{Width}} = {w_val}\\text{{ m}}"

    prompt = (
        f"A rectangular garden has a perimeter of ${perim}\\text{{ m}}$ and an area of ${area}\\text{{ m}}^2$. "
        f"Calculate the dimensions (length and width) of the garden."
    )

    sol = solution_graph(
        goal="Find dimensions of rectangle using perimeter and area",
        chain_type="word_problem",
        var="L",
        steps=[
            step(from_latex=f"2(L + W) = {perim} \\implies L + W = {semi}", to_latex_str=f"W = {semi} - L", op="Express width in terms of length from perimeter", rule="Perimeter formula"),
            step(from_latex=f"L({semi} - L) = {area}", to_latex_str=f"L^2 - {semi}L + {area} = 0", op="Substitute into area formula and set to zero", rule="Area formula"),
            step(from_latex=f"(L - {l_val})(L - {w_val}) = 0", to_latex_str=ans_latex, op=f"Factorise to find dimensions: {l_val} m and {w_val} m", rule="State dimensions"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="47_word_problem_rectangle_perimeter_area",
        learning_objective_id=f"{LO_PREFIX}_47",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"Length = {l_val}, Width = {w_val}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": f"L + W = {semi}", "marks": 1}, {"desc": f"L² - {semi}L + {area} = 0", "marks": 1}, {"desc": "Solve quadratic", "marks": 1}, {"desc": f"Length = {l_val} m, Width = {w_val} m", "marks": 1}]},
        hints={"nudge": f"Semi-perimeter is {perim}/2 = {semi}. So Width = {semi} - Length.", "concept": "Area = Length × Width = L({semi} - L) = {area}.", "breakdown": f"L² - {semi}L + {area} = 0 \\implies (L - {l_val})(L - {w_val}) = 0. Dimensions are {l_val} m by {w_val} m."},
        misconception_tags=["using_full_perimeter_instead_of_semi_perimeter_in_substitution"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 48. Word Problem: Right-Angled Triangle Pythagoras
# ---------------------------------------------------------------------------
def build_48_word_problem_pythagoras_right_triangle(r: random.Random) -> Dict[str, Any]:
    # Pythagorean triples: (3, 4, 5)*k, (5, 12, 13)
    triple = r.choice([(6, 8, 10), (9, 12, 15), (5, 12, 13), (8, 15, 17)])
    leg1, leg2, hyp = triple
    diff = abs(leg2 - leg1)

    ans_latex = f"{min(leg1, leg2)}\\text{{ cm and }} {max(leg1, leg2)}\\text{{ cm}}"

    prompt = (
        f"The hypotenuse of a right-angled triangle is ${hyp}\\text{{ cm}}$. "
        f"One of the perpendicular sides is ${diff}\\text{{ cm}}$ longer than the other. "
        f"Calculate the lengths of the two perpendicular sides."
    )

    sol = solution_graph(
        goal="Solve right triangle dimensions using Pythagoras theorem",
        chain_type="word_problem",
        var="x",
        steps=[
            step(from_latex=f"x^2 + (x + {diff})^2 = {hyp}^2", to_latex_str=f"x^2 + x^2 + {2 * diff}x + {diff ** 2} = {hyp ** 2}", op="Apply Pythagorean theorem: a² + b² = c²", rule="Pythagoras"),
            step(from_latex=f"2x^2 + {2 * diff}x + {diff ** 2 - hyp ** 2} = 0", to_latex_str=f"x^2 + {diff}x - {(hyp ** 2 - diff ** 2) // 2} = 0", op="Divide by 2 and standard form", rule="Standard quadratic form"),
            step(from_latex=f"(x - {min(leg1, leg2)})(x + {max(leg1, leg2)}) = 0", to_latex_str=ans_latex, op=f"Solve for positive length: x = {min(leg1, leg2)}", rule="Lengths must be positive"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="48_word_problem_pythagoras_right_triangle",
        learning_objective_id=f"{LO_PREFIX}_48",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{min(leg1, leg2)} and {max(leg1, leg2)}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": f"Pythagoras equation: x² + (x + {diff})² = {hyp}²", "marks": 1}, {"desc": "Standard quadratic form", "marks": 1}, {"desc": f"Solve x = {min(leg1, leg2)} (reject negative)", "marks": 1}, {"desc": f"Sides {min(leg1, leg2)} cm and {max(leg1, leg2)} cm", "marks": 1}]},
        hints={"nudge": f"Let the shorter side be x. The longer side is x + {diff}. Apply x² + (x + {diff})² = {hyp}².", "concept": "Expand (x + diff)² carefully and form a quadratic equation.", "breakdown": f"2x² + {2*diff}x - {hyp**2 - diff**2} = 0 \\implies x = {min(leg1, leg2)}. Sides are {min(leg1, leg2)} cm and {max(leg1, leg2)} cm."},
        misconception_tags=["failing_to_square_the_binomial_side_correctly_in_pythagoras"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 49. Word Problem: Speed, Distance and Time
# ---------------------------------------------------------------------------
def build_49_word_problem_speed_distance_time(r: random.Random) -> Dict[str, Any]:
    # Distance D = 120 km. Increased speed by 20 km/h saves 1 hour.
    # Time1 - Time2 = 1 -> 120/v - 120/(v+20) = 1
    # 120(v + 20) - 120v = v(v + 20) -> 2400 = v^2 + 20v -> v^2 + 20v - 2400 = 0
    # (v + 60)(v - 40) = 0 -> v = 40 km/h
    case = r.choice([
        (120, 20, 1, 40),    # D=120, extra=20, time_diff=1, v=40
        (180, 15, 1, 45),    # 180/v - 180/(v+15) = 1 -> 2700 = v^2 + 15v -> (v-45)(v+60)=0 -> v=45
        (240, 20, 1, 60),    # 240/v - 240/(v+20) = 1 -> 4800 = v^2 + 20v -> (v-60)(v+80)=0 -> v=60
        (100, 10, 0.5, 40),  # 100/v - 100/(v+10) = 0.5 -> 2000 = v^2 + 10v -> (v-40)(v+50)=0 -> v=40
    ])
    d_km, extra_v, t_diff, ans_v = case

    eq_desc = f"{d_km}\\text{{ km}}"
    ans_latex = f"{ans_v}\\text{{ km/h}}"

    prompt = (
        f"A motorist travels a distance of ${eq_desc}$. If the motorist increases the average speed by "
        f"${extra_v}\\text{{ km/h}}$, the journey takes ${num(t_diff)}\\text{{ hour(s)}}$ less. "
        f"Calculate the original average speed."
    )

    sol = solution_graph(
        goal="Solve speed-distance-time quadratic problem",
        chain_type="word_problem",
        var="v",
        steps=[
            step(from_latex=f"\\frac{{{d_km}}}{{v}} - \\frac{{{d_km}}}{{v + {extra_v}}} = {t_diff}", to_latex_str=f"{d_km}(v + {extra_v}) - {d_km}v = {t_diff}v(v + {extra_v})", op="Form time difference equation and multiply by LCD v(v + extra)", rule="Time = Distance / Speed"),
            step(from_latex=f"{d_km * extra_v} = {t_diff}v^2 + {t_diff * extra_v}v", to_latex_str=f"v^2 + {extra_v}v - {int(d_km * extra_v / t_diff)} = 0", op="Rearrange into standard quadratic form", rule="Standard quadratic form"),
            step(from_latex=f"(v - {ans_v})(v + {ans_v + extra_v}) = 0", to_latex_str=ans_latex, op=f"Solve for positive speed: v = {ans_v} km/h", rule="Speed must be positive"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="49_word_problem_speed_distance_time",
        learning_objective_id=f"{LO_PREFIX}_49",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{ans_v} km/h",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 5, "steps": [{"desc": "Time difference equation", "marks": 1}, {"desc": "Clear fractions with LCD", "marks": 1}, {"desc": "Standard quadratic form", "marks": 1}, {"desc": "Factorise", "marks": 1}, {"desc": f"Original speed {ans_v} km/h", "marks": 1}]},
        hints={"nudge": "Time = Distance / Speed. Time 1 = D/v and Time 2 = D/(v + extra).", "concept": "Time 1 - Time 2 = time saved. Multiply through by v(v + extra) to clear denominators.", "breakdown": f"v² + {extra_v}v - {int(d_km*extra_v/t_diff)} = 0 \\implies v = {ans_v} km/h."},
        misconception_tags=["subtracting_speeds_instead_of_times_in_motion_problems"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 50. Comprehensive Equations and Inequalities Synthesis
# ---------------------------------------------------------------------------
def build_50_comprehensive_equations_inequalities_synthesis(r: random.Random) -> Dict[str, Any]:
    # Multi-part synthesis:
    # 1. Solve the inequality x^2 - 4x - 5 <= 0  -> -1 <= x <= 5
    # 2. For what values of k does x^2 - 4x + k = 0 have equal roots? -> k = 4
    # 3. State whether k = 4 lies within the solution interval of the inequality.
    ans_latex = "-1 \\le x \\le 5, \\quad k = 4, \\quad \\text{Yes, } k=4 \\text{ lies in the interval}"

    prompt = (
        "Given the quadratic expression $f(x) = x^2 - 4x - 5$:\n\n"
        "1. Solve the inequality $f(x) \\le 0$.\n"
        "2. Determine the value of $k$ for which the equation $x^2 - 4x + k = 0$ has equal roots.\n"
        "3. Does this value of $k$ satisfy the inequality in (1)?"
    )

    sol = solution_graph(
        goal="Synthesize quadratic inequality and nature of roots",
        chain_type="synthesis",
        steps=[
            step(from_latex="x^2 - 4x - 5 \\le 0", to_latex_str="-1 \\le x \\le 5", op="Factorise (x - 5)(x + 1) <= 0", rule="Inequality solution"),
            step(from_latex="\\Delta = (-4)^2 - 4(1)(k) = 0", to_latex_str="16 - 4k = 0 \\implies k = 4", op="Set discriminant to zero for equal roots", rule="Equal roots condition"),
            step(from_latex="-1 \\le 4 \\le 5", to_latex_str="\\text{Yes, } k=4 \\text{ lies within } [-1; 5]", op="Verify whether k lies in solution interval", rule="Interval verification"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="50_comprehensive_equations_inequalities_synthesis",
        learning_objective_id=f"{LO_PREFIX}_50",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy="[-1, 5], k = 4, Yes",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 5, "steps": [{"desc": "Inequality solution -1 <= x <= 5", "marks": 2}, {"desc": "Equal roots condition k = 4", "marks": 2}, {"desc": "Verification: Yes", "marks": 1}]},
        hints={"nudge": "Part 1: Factorise (x - 5)(x + 1) ≤ 0. Part 2: Set Δ = (-4)² - 4k = 0.", "concept": "Combine the inequality interval with the discriminant parameter.", "breakdown": "-1 ≤ x ≤ 5. k = 4. Since -1 ≤ 4 ≤ 5, the answer to (3) is Yes."},
        misconception_tags=["failing_to_synthesize_inequality_interval_with_parameter_value"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# Registry of Archetypes 26–50
# ---------------------------------------------------------------------------
BUILDERS_26_50: Dict[str, Any] = {
    "26_nature_of_roots_classify_from_equation": build_26_nature_of_roots_classify_from_equation,
    "27_nature_of_roots_condition_for_equal_roots": build_27_nature_of_roots_condition_for_equal_roots,
    "28_nature_of_roots_condition_for_real_roots": build_28_nature_of_roots_condition_for_real_roots,
    "29_nature_of_roots_condition_for_nonreal_roots": build_29_nature_of_roots_condition_for_nonreal_roots,
    "30_nature_of_roots_prove_real_for_all_k": build_30_nature_of_roots_prove_real_for_all_k,
    "31_quadratic_inequality_standard_less_than": build_31_quadratic_inequality_standard_less_than,
    "32_quadratic_inequality_standard_greater_than": build_32_quadratic_inequality_standard_greater_than,
    "33_quadratic_inequality_non_strict_interval": build_33_quadratic_inequality_non_strict_interval,
    "34_quadratic_inequality_non_strict_disjoint": build_34_quadratic_inequality_non_strict_disjoint,
    "35_quadratic_inequality_negative_leading_coef": build_35_quadratic_inequality_negative_leading_coef,
    "36_quadratic_inequality_common_factor": build_36_quadratic_inequality_common_factor,
    "37_quadratic_inequality_difference_of_squares": build_37_quadratic_inequality_difference_of_squares,
    "38_quadratic_inequality_rearrange_first": build_38_quadratic_inequality_rearrange_first,
    "39_quadratic_inequality_perfect_square": build_39_quadratic_inequality_perfect_square,
    "40_quadratic_inequality_algebraic_fraction": build_40_quadratic_inequality_algebraic_fraction,
    "41_simultaneous_linear_quadratic_substitution_parabola": build_41_simultaneous_linear_quadratic_substitution_parabola,
    "42_simultaneous_linear_quadratic_hyperbola_product": build_42_simultaneous_linear_quadratic_hyperbola_product,
    "43_simultaneous_linear_quadratic_difference_forms": build_43_simultaneous_linear_quadratic_difference_forms,
    "44_simultaneous_linear_quadratic_circle_intersection": build_44_simultaneous_linear_quadratic_circle_intersection,
    "45_simultaneous_quadratic_interpret_intersection_points": build_45_simultaneous_quadratic_interpret_intersection_points,
    "46_word_problem_consecutive_integers_product": build_46_word_problem_consecutive_integers_product,
    "47_word_problem_rectangle_perimeter_area": build_47_word_problem_rectangle_perimeter_area,
    "48_word_problem_pythagoras_right_triangle": build_48_word_problem_pythagoras_right_triangle,
    "49_word_problem_speed_distance_time": build_49_word_problem_speed_distance_time,
    "50_comprehensive_equations_inequalities_synthesis": build_50_comprehensive_equations_inequalities_synthesis,
}
