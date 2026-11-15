"""Grade 11 Mathematics — Equations and Inequalities Archetypes 01–25.
Grounded in South African National Curriculum Standards for Grade 11 Mathematics (Term 1).
Reference: curriculum_docs_auto/Mathematics_Gr11/Term 1/02. Equations and inequalities.md

Covers Archetypes 01–25:
- 01–07: Quadratic equations by factorisation (monic, common factor, difference of squares, non-monic prime/composite a, expand first, algebraic fraction with LCD)
- 08–12: Completing the square (monic even b, surd roots, odd b, non-monic a > 1, identify constant to add)
- 13–16: Quadratic formula (exact surd roots, rounded to two decimals with comma separator, negative leading coefficient, discriminant evaluation)
- 17–20: k-substitution (quadratic bracket squared, biquadratic quartic, quartic with real and non-real roots, algebraic fraction bracket)
- 21–25: Forming quadratic equations (integer roots, fractional roots, conjugate surd roots, sum and product of roots, unknown coefficient)
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
# 01. Quadratic Factorisation: Monic with Integer Roots
# ---------------------------------------------------------------------------
def build_01_quadratic_factorisation_monic_integers(r: random.Random) -> Dict[str, Any]:
    r1 = r.choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
    r2 = r.choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
    while r1 == r2:
        r2 = r.choice([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])

    b = -(r1 + r2)
    c = r1 * r2
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"

    eq_latex = f"x^2 {sign_b}x {sign_c} = 0"
    ans_latex = f"x = {r1} \\quad \\text{{or}} \\quad x = {r2}"
    prompt = f"Solve for $x$ by factorising:\n\n$${eq_latex}$$"

    p1 = -r1
    p2 = -r2
    sign_p1 = f"+ {p1}" if p1 >= 0 else f"- {abs(p1)}"
    sign_p2 = f"+ {p2}" if p2 >= 0 else f"- {abs(p2)}"

    sol = solution_graph(
        goal="Solve monic quadratic equation by factorisation",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"(x {sign_p1})(x {sign_p2}) = 0", op="Factorise trinomial into two linear binomials", rule="Find numbers that multiply to c and add to b"),
            step(from_latex=f"(x {sign_p1})(x {sign_p2}) = 0", to_latex_str=ans_latex, op="Apply zero product rule: x - r1 = 0 or x - r2 = 0", rule="Zero product property"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="01_quadratic_factorisation_monic_integers",
        learning_objective_id=f"{LO_PREFIX}_01",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {r1} or x = {r2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Factorise trinomial", "marks": 1}, {"desc": f"Root x = {r1}", "marks": 1}, {"desc": f"Root x = {r2}", "marks": 1}]},
        hints={"nudge": f"Find two integers that multiply to {c} and add up to {b}.", "concept": "x² + bx + c = (x - r1)(x - r2) = 0.", "breakdown": f"(x {sign_p1})(x {sign_p2}) = 0 \\implies x = {r1} or x = {r2}."},
        misconception_tags=["sign_error_in_quadratic_factors"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 02. Quadratic Factorisation: Common Factor
# ---------------------------------------------------------------------------
def build_02_quadratic_factorisation_common_factor(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3, 4, 5])
    r2 = r.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    b = -a * r2
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"

    eq_latex = f"{a}x^2 {sign_b}x = 0"
    ans_latex = f"x = 0 \\quad \\text{{or}} \\quad x = {r2}"
    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic with no constant term by common factor",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"{a}x(x - {r2}) = 0" if r2 >= 0 else f"{a}x(x + {abs(r2)}) = 0", op=f"Factor out common factor {a}x", rule="Common monomial factor"),
            step(from_latex=f"{a}x = 0 \\text{{ or }} x - {r2} = 0", to_latex_str=ans_latex, op="Zero product rule", rule="x = 0 or x = r2"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="02_quadratic_factorisation_common_factor",
        learning_objective_id=f"{LO_PREFIX}_02",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = 0 or x = {r2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": "Factor out common factor", "marks": 1}, {"desc": f"Both solutions x = 0 or x = {r2}", "marks": 1}]},
        hints={"nudge": "Do NOT divide by x! Factor out x as a common factor.", "concept": "Dividing by x loses the solution x = 0. Always factorise.", "breakdown": f"x({a}x {sign_b}) = 0 \\implies x = 0 or x = {r2}."},
        misconception_tags=["dividing_by_variable_losing_zero_root"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 03. Quadratic Factorisation: Difference of Squares
# ---------------------------------------------------------------------------
def build_03_quadratic_factorisation_difference_of_squares(r: random.Random) -> Dict[str, Any]:
    sq1 = r.choice([1, 4, 9, 16, 25])
    root1 = int(math.isqrt(sq1))
    root2 = r.choice([2, 3, 4, 5, 6, 7])
    sq2 = root2 * root2

    eq_latex = f"{sq1}x^2 - {sq2} = 0" if sq1 > 1 else f"x^2 - {sq2} = 0"
    if root1 == 1:
        ans_latex = f"x = {root2} \\quad \\text{{or}} \\quad x = -{root2}"
        ans_sympy = f"x = {root2} or x = -{root2}"
    else:
        ans_latex = f"x = \\frac{{{root2}}}{{{root1}}} \\quad \\text{{or}} \\quad x = -\\frac{{{root2}}}{{{root1}}}"
        ans_sympy = f"x = {root2}/{root1} or x = -{root2}/{root1}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic difference of squares",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"({root1}x - {root2})({root1}x + {root2}) = 0" if root1 > 1 else f"(x - {root2})(x + {root2}) = 0", op="Factorise as difference of squares A² - B² = (A - B)(A + B)", rule="Difference of two squares"),
            step(from_latex=f"{root1}x = \\pm {root2}", to_latex_str=ans_latex, op="Solve each linear factor", rule="Zero product rule"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="03_quadratic_factorisation_difference_of_squares",
        learning_objective_id=f"{LO_PREFIX}_03",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=ans_sympy,
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": "Difference of squares factors", "marks": 1}, {"desc": "Both positive and negative roots", "marks": 1}]},
        hints={"nudge": "Factorise as a difference of squares: A² - B² = (A - B)(A + B).", "concept": "Remember that taking a square root always produces both + and - solutions.", "breakdown": f"({root1}x - {root2})({root1}x + {root2}) = 0 \\implies {ans_latex}."},
        misconception_tags=["forgetting_negative_root_in_square_root_solve"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 04. Quadratic Factorisation: Non-Monic Prime a
# ---------------------------------------------------------------------------
def build_04_quadratic_factorisation_non_monic_prime_a(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3])
    # (ax - p)(x - q) = ax^2 - (aq + p)x + pq = 0
    p = r.choice([-3, -1, 1, 3])
    q = r.choice([-4, -2, 2, 4])
    b = -(a * q + p)
    c = p * q

    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    eq_latex = f"{a}x^2 {sign_b}x {sign_c} = 0"

    # Roots: x = p/a or x = q
    ans_latex = f"x = \\frac{{{p}}}{{{a}}} \\quad \\text{{or}} \\quad x = {q}"
    ans_sympy = f"x = {p}/{a} or x = {q}"
    prompt = f"Solve for $x$ by factorising:\n\n$${eq_latex}$$"

    sign_p = f"- {p}" if p >= 0 else f"+ {abs(p)}"
    sign_q = f"- {q}" if q >= 0 else f"+ {abs(q)}"

    sol = solution_graph(
        goal="Solve non-monic quadratic with prime leading coefficient",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"({a}x {sign_p})(x {sign_q}) = 0", op=f"Factorise non-monic trinomial into ({a}x {sign_p})(x {sign_q})", rule="Trinomial factorisation"),
            step(from_latex=f"{a}x {sign_p} = 0 \\text{{ or }} x {sign_q} = 0", to_latex_str=ans_latex, op="Solve linear factors", rule="Zero product rule"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="04_quadratic_factorisation_non_monic_prime_a",
        learning_objective_id=f"{LO_PREFIX}_04",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=ans_sympy,
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Correct factors", "marks": 2}, {"desc": f"Both roots: {ans_latex}", "marks": 1}]},
        hints={"nudge": f"The first term is {a}x², so the factors start with ({a}x ...) and (x ...).", "concept": "Test factor pairs of {c} so that inner + outer products sum to {b}x.", "breakdown": f"({a}x {sign_p})(x {sign_q}) = 0 \\implies x = {p}/{a} or x = {q}."},
        misconception_tags=["incorrect_cross_multiplication_in_non_monic_trinomial"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 05. Quadratic Factorisation: Non-Monic Composite a
# ---------------------------------------------------------------------------
def build_05_quadratic_factorisation_non_monic_composite_a(r: random.Random) -> Dict[str, Any]:
    # (2x - 1)(2x - 3) = 4x^2 - 8x + 3 = 0
    # or (2x + 1)(3x - 2) = 6x^2 - x - 2 = 0
    case = r.choice([
        (2, 2, -1, -3, 4, -8, 3, "1/2", "3/2", "1/2", "3/2"),
        (2, 3, 1, -2, 6, -1, -2, "-1/2", "2/3", "-\\frac{1}{2}", "\\frac{2}{3}"),
        (2, 2, 1, -3, 4, -4, -3, "-1/2", "3/2", "-\\frac{1}{2}", "\\frac{3}{2}"),
        (2, 3, -1, 1, 6, -1, -1, "1/2", "-1/3", "\\frac{1}{2}", "-\\frac{1}{3}"),
    ])
    a1, a2, p1, p2, a_tot, b_tot, c_tot, s_r1, s_r2, lat_r1, lat_r2 = case

    sign_b = f"+ {b_tot}" if b_tot >= 0 else f"- {abs(b_tot)}"
    sign_c = f"+ {c_tot}" if c_tot >= 0 else f"- {abs(c_tot)}"
    eq_latex = f"{a_tot}x^2 {sign_b}x {sign_c} = 0"
    ans_latex = f"x = {lat_r1} \\quad \\text{{or}} \\quad x = {lat_r2}"
    ans_sympy = f"x = {s_r1} or x = {s_r2}"

    prompt = f"Solve for $x$ by factorising:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve non-monic quadratic with composite leading coefficient",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"({a1}x + {p1})({a2}x + {p2}) = 0", op="Factorise trinomial into binomial factors", rule="Grouping or trial-and-error factorisation"),
            step(from_latex=f"{a1}x + {p1} = 0 \\text{{ or }} {a2}x + {p2} = 0", to_latex_str=ans_latex, op="Solve linear factors", rule="Zero product rule"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="05_quadratic_factorisation_non_monic_composite_a",
        learning_objective_id=f"{LO_PREFIX}_05",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=ans_sympy,
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Binomial factors", "marks": 2}, {"desc": f"Both roots: {ans_latex}", "marks": 1}]},
        hints={"nudge": f"Factorise {a_tot}x² + {b_tot}x + {c_tot} = 0 using grouping or systematic trial-and-error.", "concept": "Find factors of a·c that add up to b.", "breakdown": f"({a1}x + {p1})({a2}x + {p2}) = 0 \\implies {ans_latex}."},
        misconception_tags=["failing_to_check_outer_and_inner_products"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 06. Quadratic: Expand Brackets First
# ---------------------------------------------------------------------------
def build_06_quadratic_expand_brackets_first(r: random.Random) -> Dict[str, Any]:
    # (x - a)(x + b) = k -> x^2 + (b-a)x - (ab + k) = 0
    # Let final roots be r1, r2
    r1 = r.choice([1, 2, 3])
    r2 = r.choice([-5, -4, -3])
    # final: (x - r1)(x - r2) = x^2 - (r1+r2)x + r1*r2 = 0
    # Let original LHS be (x - p)(x - q) where p, q != r1, r2
    p = r.choice([4, 5])
    q = -1
    # LHS: (x - p)(x - q) = x^2 - (p+q)x + pq
    # We want x^2 - (p+q)x + pq - k = x^2 - (r1+r2)x + r1*r2
    # So p+q must equal r1+r2:
    target_sum = r1 + r2
    q = target_sum - p
    k = (p * q) - (r1 * r2)

    sign_q = f"+ {abs(q)}" if q < 0 else f"- {q}"
    eq_latex = f"(x - {p})(x {sign_q}) = {k}"
    ans_latex = f"x = {r1} \\quad \\text{{or}} \\quad x = {r2}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Expand brackets and rearrange to standard quadratic form before factorising",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x^2 - {p + q}x + {p * q} = {k}", op="Expand LHS brackets", rule="FOIL expansion"),
            step(from_latex=f"x^2 - {p + q}x + {p * q} = {k}", to_latex_str=f"x^2 - {r1 + r2}x + {r1 * r2} = 0", op=f"Subtract {k} from both sides to form standard quadratic = 0", rule="Standard quadratic form ax² + bx + c = 0"),
            step(from_latex=f"(x - {r1})(x - {r2}) = 0", to_latex_str=ans_latex, op="Factorise and solve", rule="Zero product rule"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="06_quadratic_expand_brackets_first",
        learning_objective_id=f"{LO_PREFIX}_06",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {r1} or x = {r2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Expand LHS", "marks": 1}, {"desc": "Standard form = 0", "marks": 1}, {"desc": "Factorise", "marks": 1}, {"desc": "Both roots", "marks": 1}]},
        hints={"nudge": f"Do NOT set each bracket equal to {k}! Expand the brackets and bring all terms to one side = 0.", "concept": "The zero product property ONLY works when the RHS is 0: AB = 0. If AB = k, you must expand first.", "breakdown": f"Expand to x² - {p+q}x + {p*q} = {k} \\implies x² - {r1+r2}x + {r1*r2} = 0 \\implies x = {r1} or x = {r2}."},
        misconception_tags=["setting_factors_equal_to_non_zero_constant"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 07. Quadratic: Algebraic Fraction with LCD
# ---------------------------------------------------------------------------
def build_07_quadratic_algebraic_fraction_lcd(r: random.Random) -> Dict[str, Any]:
    # x + b/x = c -> x^2 - cx + b = 0
    # Let roots be r1, r2 (integers, r1, r2 > 0)
    r1 = r.choice([1, 2, 3])
    r2 = r.choice([4, 5, 6])
    c = r1 + r2
    b = r1 * r2

    eq_latex = f"x + \\frac{{{b}}}{{x}} = {c}"
    ans_latex = f"x = {r1} \\quad \\text{{or}} \\quad x = {r2}"
    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve fractional equation by multiplying by LCD",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x^2 + {b} = {c}x \\quad (x \\ne 0)", op="Multiply every term by LCD = x", rule="Clear fractions"),
            step(from_latex=f"x^2 + {b} = {c}x", to_latex_str=f"x^2 - {c}x + {b} = 0", op="Rearrange into standard form = 0", rule="Standard form"),
            step(from_latex=f"(x - {r1})(x - {r2}) = 0", to_latex_str=ans_latex, op="Factorise and solve", rule="Zero product rule"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="07_quadratic_algebraic_fraction_lcd",
        learning_objective_id=f"{LO_PREFIX}_07",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {r1} or x = {r2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Multiply by LCD x", "marks": 1}, {"desc": "Standard form = 0", "marks": 1}, {"desc": f"Roots x = {r1} or x = {r2}", "marks": 1}]},
        hints={"nudge": "Multiply every term in the equation by x to eliminate the denominator.", "concept": "x · x + x · (b/x) = x · c \\implies x² + b = cx.", "breakdown": f"x² - {c}x + {b} = 0 \\implies (x - {r1})(x - {r2}) = 0 \\implies x = {r1} or x = {r2}."},
        misconception_tags=["forgetting_to_multiply_first_term_by_lcd"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 08. Completing the Square: Monic Even b
# ---------------------------------------------------------------------------
def build_08_completing_the_square_monic_even_b(r: random.Random) -> Dict[str, Any]:
    k = r.choice([2, 3, 4, 5])
    # (x + k)^2 = sq_val
    sq_val = r.choice([9, 16, 25, 36])
    root_sq = int(math.isqrt(sq_val))
    r1 = -k + root_sq
    r2 = -k - root_sq
    c_orig = (k * k) - sq_val

    b_val = 2 * k
    sign_c = f"+ {c_orig}" if c_orig >= 0 else f"- {abs(c_orig)}"
    eq_latex = f"x^2 + {b_val}x {sign_c} = 0"
    ans_latex = f"x = {r1} \\quad \\text{{or}} \\quad x = {r2}"

    prompt = f"Solve for $x$ by **completing the square**:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic by completing the square",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x^2 + {b_val}x = {-c_orig}", op=f"Move constant term to RHS", rule="Isolate variable terms"),
            step(from_latex=f"x^2 + {b_val}x + {k * k} = {-c_orig} + {k * k}", to_latex_str=f"(x + {k})^2 = {sq_val}", op=f"Add (b/2)² = ({b_val}/2)² = {k*k} to both sides", rule="Completing the square"),
            step(from_latex=f"(x + {k})^2 = {sq_val}", to_latex_str=f"x + {k} = \\pm {root_sq}", op="Take square root of both sides", rule="Square root property"),
            step(from_latex=f"x = -{k} \\pm {root_sq}", to_latex_str=ans_latex, op="Solve for x", rule=f"x = {r1} or x = {r2}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="08_completing_the_square_monic_even_b",
        learning_objective_id=f"{LO_PREFIX}_08",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {r1} or x = {r2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Move constant to RHS", "marks": 1}, {"desc": f"Add ({b_val}/2)² = {k*k} to both sides", "marks": 1}, {"desc": f"(x + {k})² = {sq_val}", "marks": 1}, {"desc": "Both solutions", "marks": 1}]},
        hints={"nudge": f"Halve the coefficient of x ({b_val}/2 = {k}) and square it ({k*k}). Add to both sides.", "concept": "x² + 2kx + k² = (x + k)².", "breakdown": f"(x + {k})² = {sq_val} \\implies x + {k} = ±{root_sq} \\implies {ans_latex}."},
        misconception_tags=["adding_square_to_only_one_side_in_completing_square"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 09. Completing the Square: Monic Surd Roots
# ---------------------------------------------------------------------------
def build_09_completing_the_square_monic_surd_roots(r: random.Random) -> Dict[str, Any]:
    k = r.choice([1, 2, 3])
    # (x + k)^2 = prime_surd
    prime_surd = r.choice([2, 3, 5, 7])
    c_orig = (k * k) - prime_surd

    b_val = 2 * k
    sign_c = f"+ {c_orig}" if c_orig >= 0 else f"- {abs(c_orig)}"
    eq_latex = f"x^2 + {b_val}x {sign_c} = 0"
    ans_latex = f"x = -{k} + \\sqrt{{{prime_surd}}} \\quad \\text{{or}} \\quad x = -{k} - \\sqrt{{{prime_surd}}}"

    prompt = f"Solve for $x$ by completing the square (leave answer in simplest surd form):\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic by completing the square leaving surd form",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x^2 + {b_val}x = {-c_orig}", op="Move constant to RHS", rule="Isolate variable terms"),
            step(from_latex=f"x^2 + {b_val}x + {k * k} = {-c_orig} + {k * k}", to_latex_str=f"(x + {k})^2 = {prime_surd}", op=f"Add {k*k} to both sides", rule="Complete the square"),
            step(from_latex=f"(x + {k})^2 = {prime_surd}", to_latex_str=f"x + {k} = \\pm \\sqrt{{{prime_surd}}}", op="Take square root", rule="Square root property"),
            step(from_latex=f"x + {k} = \\pm \\sqrt{{{prime_surd}}}", to_latex_str=ans_latex, op="Subtract k", rule=f"x = -{k} ± √{prime_surd}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="09_completing_the_square_monic_surd_roots",
        learning_objective_id=f"{LO_PREFIX}_09",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = -{k} + sqrt({prime_surd}) or x = -{k} - sqrt({prime_surd})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Move constant", "marks": 1}, {"desc": f"Add {k*k} to both sides", "marks": 1}, {"desc": f"Perfect square (x + {k})² = {prime_surd}", "marks": 1}, {"desc": f"Surd answer x = -{k} ± √{prime_surd}", "marks": 1}]},
        hints={"nudge": f"Add ({b_val}/2)² = {k*k} to both sides.", "concept": "When the RHS is not a perfect square, leave the root in radical form.", "breakdown": f"(x + {k})² = {prime_surd} \\implies x = -{k} ± \\sqrt{{{prime_surd}}}."},
        misconception_tags=["rounding_when_simplest_surd_form_is_demanded"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 10. Completing the Square: Monic Odd b
# ---------------------------------------------------------------------------
def build_10_completing_the_square_monic_odd_b(r: random.Random) -> Dict[str, Any]:
    b = r.choice([3, 5, 7])
    # x^2 + bx - c = 0
    # Add (b/2)^2 = b^2 / 4
    # Let (b/2)^2 + c = sq_num / 4 where sq_num is a square
    # e.g. b = 3: (3/2)^2 + c = 9/4 + c. If c = 4 -> 9/4 + 16/4 = 25/4 -> root = 5/2
    # Then x + 3/2 = +- 5/2 -> x = 1 or x = -4
    case = r.choice([
        (3, 4, 25, 5, 1, -4),     # x^2 + 3x - 4 = 0
        (5, 6, 49, 7, 1, -6),     # x^2 + 5x - 6 = 0
        (3, 10, 49, 7, 2, -5),    # x^2 + 3x - 10 = 0
        (5, 14, 81, 9, 2, -7),    # x^2 + 5x - 14 = 0
    ])
    b_val, c_val, num_sq, root_num, r1, r2 = case

    eq_latex = f"x^2 + {b_val}x - {c_val} = 0"
    ans_latex = f"x = {r1} \\quad \\text{{or}} \\quad x = {r2}"
    prompt = f"Solve for $x$ by completing the square:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic with odd b by completing the square with fraction arithmetic",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x^2 + {b_val}x = {c_val}", op="Move constant to RHS", rule="Isolate variable terms"),
            step(from_latex=f"x^2 + {b_val}x + \\frac{{{b_val ** 2}}}{{4}} = {c_val} + \\frac{{{b_val ** 2}}}{{4}}", to_latex_str=f"\\left(x + \\frac{{{b_val}}}{{2}}\\right)^2 = \\frac{{{num_sq}}}{{4}}", op=f"Add (b/2)² = ({b_val}/2)² = {b_val**2}/4 to both sides", rule="Complete the square"),
            step(from_latex=f"\\left(x + \\frac{{{b_val}}}{{2}}\\right)^2 = \\frac{{{num_sq}}}{{4}}", to_latex_str=f"x + \\frac{{{b_val}}}{{2}} = \\pm \\frac{{{root_num}}}{{2}}", op="Take square root", rule="Square root of fraction"),
            step(from_latex=f"x = -\\frac{{{b_val}}}{{2}} \\pm \\frac{{{root_num}}}{{2}}", to_latex_str=ans_latex, op="Evaluate roots", rule=f"x = {r1} or x = {r2}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="10_completing_the_square_monic_odd_b",
        learning_objective_id=f"{LO_PREFIX}_10",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {r1} or x = {r2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Move constant", "marks": 1}, {"desc": f"Add {b_val**2}/4 to both sides", "marks": 1}, {"desc": f"Form (x + {b_val}/2)²", "marks": 1}, {"desc": "Both solutions", "marks": 1}]},
        hints={"nudge": f"Halve the odd coefficient: ({b_val}/2). Square it to get {b_val**2}/4 and add to both sides.", "concept": "Don't convert to decimals; keep fractions with common denominator 4.", "breakdown": f"(x + {b_val}/2)² = {num_sq}/4 \\implies x + {b_val}/2 = ±{root_num}/2 \\implies {ans_latex}."},
        misconception_tags=["converting_fractions_to_rounded_decimals_prematurely"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 11. Completing the Square: Non-Monic (Divide by a First)
# ---------------------------------------------------------------------------
def build_11_completing_the_square_non_monic(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3])
    # 2x^2 + 8x - 10 = 0 -> x^2 + 4x - 5 = 0 -> (x+2)^2 = 9 -> x = 1 or x = -5
    case = r.choice([
        (2, 8, 10, 4, 5, 9, 3, 2, 1, -5),
        (2, 4, 16, 2, 8, 9, 3, 1, 2, -4),
        (3, 12, 15, 4, 5, 9, 3, 2, 1, -5),
        (2, 12, 14, 6, 7, 16, 4, 3, 1, -7),
    ])
    a_val, b_orig, c_orig, b_red, c_red, sq_val, root_sq, k_val, r1, r2 = case

    eq_latex = f"{a_val}x^2 + {b_orig}x - {c_orig} = 0"
    ans_latex = f"x = {r1} \\quad \\text{{or}} \\quad x = {r2}"
    prompt = f"Solve for $x$ by completing the square:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Complete square for non-monic quadratic by dividing by leading coefficient first",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"x^2 + {b_red}x - {c_red} = 0", op=f"Divide entire equation by leading coefficient {a_val}", rule="Make leading coefficient equal to 1"),
            step(from_latex=f"x^2 + {b_red}x = {c_red}", to_latex_str=f"(x + {k_val})^2 = {sq_val}", op=f"Add ({b_red}/2)² = {k_val**2} to both sides", rule="Complete the square"),
            step(from_latex=f"(x + {k_val})^2 = {sq_val}", to_latex_str=f"x + {k_val} = \\pm {root_sq}", op="Take square root", rule="Square root property"),
            step(from_latex=f"x = -{k_val} \\pm {root_sq}", to_latex_str=ans_latex, op="Solve for x", rule=f"x = {r1} or x = {r2}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="11_completing_the_square_non_monic",
        learning_objective_id=f"{LO_PREFIX}_11",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {r1} or x = {r2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": f"Divide by {a_val}", "marks": 1}, {"desc": "Add square term to both sides", "marks": 1}, {"desc": "Form perfect square", "marks": 1}, {"desc": "Both solutions", "marks": 1}]},
        hints={"nudge": f"Divide every term by {a_val} first before completing the square.", "concept": "Completing the square requires the coefficient of x² to be 1.", "breakdown": f"x² + {b_red}x = {c_red} \\implies (x + {k_val})² = {sq_val} \\implies {ans_latex}."},
        misconception_tags=["completing_square_before_dividing_by_leading_coefficient"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 12. Completing the Square: Identify Constant Term to Add
# ---------------------------------------------------------------------------
def build_12_completing_the_square_identify_term_to_add(r: random.Random) -> Dict[str, Any]:
    b = r.choice([6, 8, 10, 12, 14, 16])
    half_b = b // 2
    c_add = half_b * half_b

    prompt = f"What constant term must be added to the expression $x^2 + {b}x$ to make it a perfect square trinomial?"
    ans_latex = str(c_add)

    sol = solution_graph(
        goal="Determine constant term to complete square",
        chain_type="calculation",
        steps=[
            step(from_latex=f"\\left(\\frac{{{b}}}{{2}}\\right)^2", to_latex_str=f"{half_b}^2 = {c_add}", op="Take half of coefficient of x and square it", rule="Term to add is (b/2)²"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="12_completing_the_square_identify_term_to_add",
        learning_objective_id=f"{LO_PREFIX}_12",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=ans_latex,
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": f"Halve coefficient: {b}/2 = {half_b}", "marks": 1}, {"desc": f"Square: {half_b}^2 = {c_add}", "marks": 1}]},
        hints={"nudge": "Take half of the coefficient of x, then square that number.", "concept": "In x² + bx + c, the constant for a perfect square is c = (b/2)².", "breakdown": f"({b}/2)² = {half_b}² = {c_add}."},
        misconception_tags=["halving_without_squaring_in_completing_square"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=2,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 13. Quadratic Formula: Exact Simplest Surd Form
# ---------------------------------------------------------------------------
def build_13_quadratic_formula_exact_surd_roots(r: random.Random) -> Dict[str, Any]:
    # x^2 - 4x + 1 = 0 -> Delta = 16 - 4 = 12 -> sqrt(12) = 2*sqrt(3) -> x = (4 +- 2*sqrt(3))/2 = 2 +- sqrt(3)
    case = r.choice([
        (1, -4, 1, 12, 2, 3, 2),    # x = 2 +- \sqrt{3}
        (1, -6, 7, 8, 3, 2, 2),     # x = 3 +- \sqrt{2}
        (1, -6, 4, 20, 3, 5, 2),    # x = 3 +- \sqrt{5}
        (1, -2, -2, 12, 1, 3, 2),   # x = 1 +- \sqrt{3}
        (1, -4, -1, 20, 2, 5, 2),   # x = 2 +- \sqrt{5}
    ])
    a, b, c, delta, p_int, rad, gcd_div = case

    sign_b = f"- {abs(b)}" if b < 0 else f"+ {b}"
    sign_c = f"- {abs(c)}" if c < 0 else f"+ {c}"
    eq_latex = f"x^2 {sign_b}x {sign_c} = 0"
    ans_latex = f"x = {p_int} + \\sqrt{{{rad}}} \\quad \\text{{or}} \\quad x = {p_int} - \\sqrt{{{rad}}}"

    prompt = f"Solve for $x$ using the quadratic formula (write answers in simplest surd form):\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic using formula with simplest surd answer",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=f"x = \\frac{{-({b}) \\pm \\sqrt{{({b})^2 - 4(1)({c})}}}}{{2(1)}}", to_latex_str=f"x = \\frac{{{abs(b)} \\pm \\sqrt{{{delta}}}}}{{2}}", op="Substitute a=1, b, c into quadratic formula", rule="Quadratic formula"),
            step(from_latex=f"\\sqrt{{{delta}}} = \\sqrt{{4 \\times {rad}}} = 2\\sqrt{{{rad}}}", to_latex_str=f"x = \\frac{{{abs(b)} \\pm 2\\sqrt{{{rad}}}}}{{2}}", op="Simplify surd in numerator", rule="Surd simplification"),
            step(from_latex=f"x = \\frac{{{abs(b)} \\pm 2\\sqrt{{{rad}}}}}{{2}}", to_latex_str=ans_latex, op="Divide through by 2", rule=f"x = {p_int} ± √{rad}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="13_quadratic_formula_exact_surd_roots",
        learning_objective_id=f"{LO_PREFIX}_13",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {p_int} + sqrt({rad}) or x = {p_int} - sqrt({rad})",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Formula substitution", "marks": 1}, {"desc": f"Simplify surd \\sqrt{{{delta}}} = 2\\sqrt{{{rad}}}", "marks": 1}, {"desc": f"Final simplest surd form {ans_latex}", "marks": 1}]},
        hints={"nudge": "Substitute a, b, c into x = (-b ± √(b² - 4ac)) / (2a).", "concept": "Simplify the radical before dividing by 2: √(12) = 2√3.", "breakdown": f"x = ({abs(b)} ± 2√{rad}) / 2 = {ans_latex}."},
        misconception_tags=["cancelling_only_one_term_in_fractional_numerator"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 14. Quadratic Formula: Rounded to Two Decimals (SA Comma)
# ---------------------------------------------------------------------------
def build_14_quadratic_formula_rounded_two_decimals(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3])
    b = r.choice([-7, -5, 5, 7])
    c = r.choice([1, -1, -2])
    delta = (b * b) - (4 * a * c)
    while delta <= 0 or math.isqrt(delta) ** 2 == delta:
        c = r.choice([1, -1, -2, -3])
        delta = (b * b) - (4 * a * c)

    root_delta = math.sqrt(delta)
    x1 = (-b + root_delta) / (2 * a)
    x2 = (-b - root_delta) / (2 * a)
    
    # Comma decimals
    s_x1 = f"{x1:.2f}".replace(".", "{,}")
    s_x2 = f"{x2:.2f}".replace(".", "{,}")

    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    eq_latex = f"{a}x^2 {sign_b}x {sign_c} = 0"
    ans_latex = f"x \\approx {s_x1} \\quad \\text{{or}} \\quad x \\approx {s_x2}"

    prompt = f"Solve for $x$ using the quadratic formula. Round your answers to **two decimal places**:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic with formula rounded to two decimal places",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=f"x = \\frac{{-({b}) \\pm \\sqrt{{({b})^2 - 4({a})({c})}}}}{{2({a})}}", to_latex_str=f"x = \\frac{{{-b} \\pm \\sqrt{{{delta}}}}}{{{2 * a}}}", op="Substitute coefficients into quadratic formula", rule="Quadratic formula"),
            step(from_latex=f"x = \\frac{{{-b} \\pm {num(round(root_delta, 3))}}}{{{2 * a}}}", to_latex_str=ans_latex, op="Calculate decimal values and round to two decimal places", rule="Rounding rule"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="14_quadratic_formula_rounded_two_decimals",
        learning_objective_id=f"{LO_PREFIX}_14",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {round(x1, 2)} or x = {round(x2, 2)}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Correct substitution into quadratic formula", "marks": 1}, {"desc": f"First rounded root x = {s_x1}", "marks": 1}, {"desc": f"Second rounded root x = {s_x2}", "marks": 1}]},
        hints={"nudge": f"Identify a = {a}, b = {b}, c = {c}. Use x = (-b ± √(b² - 4ac)) / (2a).", "concept": "Evaluate the discriminant b² - 4ac first, then calculate both values on your calculator.", "breakdown": f"Δ = {delta}. x = ({-b} ± √{delta}) / {2*a} \\implies x ≈ {s_x1} or x ≈ {s_x2}."},
        misconception_tags=["rounding_to_one_decimal_instead_of_two"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 15. Quadratic Formula: Negative Leading Coefficient
# ---------------------------------------------------------------------------
def build_15_quadratic_formula_negative_leading_coef(r: random.Random) -> Dict[str, Any]:
    # -2x^2 + 5x + 3 = 0 -> 2x^2 - 5x - 3 = 0 -> (2x + 1)(x - 3) = 0 -> x = -1/2 or x = 3
    case = r.choice([
        (-2, 5, 3, "-1/2", "3", "-\\frac{1}{2}", "3"),
        (-1, 2, 8, "-2", "4", "-2", "4"),
        (-3, 10, 8, "-2/3", "4", "-\\frac{2}{3}", "4"),
        (-2, 3, 2, "-1/2", "2", "-\\frac{1}{2}", "2"),
    ])
    a, b, c, s_r1, s_r2, lat_r1, lat_r2 = case

    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    eq_latex = f"{a}x^2 {sign_b}x {sign_c} = 0"
    ans_latex = f"x = {lat_r1} \\quad \\text{{or}} \\quad x = {lat_r2}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic with negative leading coefficient",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"{-a}x^2 - {b}x - {c} = 0", op="Multiply entire equation by -1 to make leading coefficient positive", rule="Multiplication property of equality"),
            step(from_latex=f"{-a}x^2 - {b}x - {c} = 0", to_latex_str=ans_latex, op="Solve by factorisation or quadratic formula", rule="Quadratic solve"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="15_quadratic_formula_negative_leading_coef",
        learning_objective_id=f"{LO_PREFIX}_15",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {s_r1} or x = {s_r2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": "Multiply by -1 to standard form", "marks": 1}, {"desc": f"Root x = {lat_r1}", "marks": 1}, {"desc": f"Root x = {lat_r2}", "marks": 1}]},
        hints={"nudge": "Multiply every term by -1 to make the x² coefficient positive.", "concept": "Multiplying by -1 simplifies factorisation: -ax² + bx + c = 0 \\implies ax² - bx - c = 0.", "breakdown": f"{-a}x² - {b}x - {c} = 0 \\implies {ans_latex}."},
        misconception_tags=["sign_error_in_quadratic_formula_denominator_2a"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 16. Quadratic Formula: Discriminant Calculation
# ---------------------------------------------------------------------------
def build_16_quadratic_formula_discriminant_identification(r: random.Random) -> Dict[str, Any]:
    a = r.choice([1, 2, 3])
    b = r.choice([-6, -5, -4, 4, 5, 6])
    c = r.choice([-3, -2, 1, 2, 4])
    delta = (b * b) - (4 * a * c)

    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    eq_latex = f"{a}x^2 {sign_b}x {sign_c} = 0" if a > 1 else f"x^2 {sign_b}x {sign_c} = 0"

    prompt = f"Calculate the numerical value of the discriminant $\\Delta$ for the equation:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Calculate discriminant Delta = b^2 - 4ac",
        chain_type="calculation",
        steps=[
            step(from_latex=f"\\Delta = b^2 - 4ac", to_latex_str=f"\\Delta = ({b})^2 - 4({a})({c})", op="Identify coefficients a, b, c and substitute into discriminant formula", rule="Definition of discriminant"),
            step(from_latex=f"\\Delta = {b * b} - ({4 * a * c})", to_latex_str=f"\\Delta = {delta}", op="Evaluate arithmetic", rule=f"\\Delta = {delta}"),
        ],
        final_latex=str(delta),
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="16_quadratic_formula_discriminant_identification",
        learning_objective_id=f"{LO_PREFIX}_16",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=str(delta),
        answer_sympy=str(delta),
        sample_answer=str(delta),
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": f"Substitute: ({b})^2 - 4({a})({c})", "marks": 1}, {"desc": f"Evaluate Delta = {delta}", "marks": 1}]},
        hints={"nudge": f"Identify a = {a}, b = {b}, c = {c}. Use Δ = b² - 4ac.", "concept": "Remember that (-b)² is always positive!", "breakdown": f"Δ = ({b})² - 4({a})({c}) = {b*b} - ({4*a*c}) = {delta}."},
        misconception_tags=["calculating_negative_b_squared_as_negative_number"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=2,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 17. k-Substitution: Quadratic Bracket Squared
# ---------------------------------------------------------------------------
def build_17_k_substitution_quadratic_bracket_squared(r: random.Random) -> Dict[str, Any]:
    # (x^2 - 2x)^2 - 11(x^2 - 2x) + 24 = 0
    # Let k = x^2 - 2x. (k - 3)(k - 8) = 0 -> k = 3 or k = 8
    # x^2 - 2x - 3 = 0 -> (x-3)(x+1)=0 -> x = 3 or x = -1
    # x^2 - 2x - 8 = 0 -> (x-4)(x+2)=0 -> x = 4 or x = -2
    k1 = 3
    k2 = 8
    b_k = k1 + k2
    c_k = k1 * k2

    eq_latex = f"\\left(x^2 - 2x\\right)^2 - {b_k}\\left(x^2 - 2x\\right) + {c_k} = 0"
    ans_latex = f"x = 3, \\; x = -1, \\; x = 4, \\; x = -2"
    ans_sympy = "x = 3 or x = -1 or x = 4 or x = -2"

    prompt = f"Solve for $x$ by using $k$-substitution:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve quadratic in a quadratic bracket using k-substitution",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"k^2 - {b_k}k + {c_k} = 0 \\quad \\text{{where }} k = x^2 - 2x", op="Substitute k = x^2 - 2x", rule="k-substitution"),
            step(from_latex=f"(k - {k1})(k - {k2}) = 0", to_latex_str=f"k = {k1} \\quad \\text{{or}} \\quad k = {k2}", op="Factorise quadratic in k", rule="Zero product rule"),
            step(from_latex=f"x^2 - 2x = 3 \\implies x^2 - 2x - 3 = 0", to_latex_str="x = 3 \\quad \\text{or} \\quad x = -1", op="Solve for x when k = 3", rule="Trinomial factorisation"),
            step(from_latex=f"x^2 - 2x = 8 \\implies x^2 - 2x - 8 = 0", to_latex_str="x = 4 \\quad \\text{or} \\quad x = -2", op="Solve for x when k = 8", rule="Trinomial factorisation"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="17_k_substitution_quadratic_bracket_squared",
        learning_objective_id=f"{LO_PREFIX}_17",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=ans_sympy,
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 5, "steps": [{"desc": "k-substitution", "marks": 1}, {"desc": "Solve for k", "marks": 1}, {"desc": "First quadratic in x", "marks": 1}, {"desc": "Second quadratic in x", "marks": 1}, {"desc": "All 4 solutions", "marks": 1}]},
        hints={"nudge": "Let k = x² - 2x to form a quadratic in k: k² - 11k + 24 = 0.", "concept": "After finding the values of k, set x² - 2x equal to each value and solve for x.", "breakdown": f"k = 3 gives (x-3)(x+1)=0; k = 8 gives (x-4)(x+2)=0. Solutions: x = 3, -1, 4, -2."},
        misconception_tags=["stopping_at_k_values_without_solving_for_x"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 18. k-Substitution: Biquadratic Quartic (Four Real Roots)
# ---------------------------------------------------------------------------
def build_18_k_substitution_quartic_biquadratic(r: random.Random) -> Dict[str, Any]:
    # x^4 - (a^2 + b^2)x^2 + a^2*b^2 = 0
    pair = r.choice([(1, 2, 5, 4), (1, 3, 10, 9), (2, 3, 13, 36), (1, 4, 17, 16), (2, 4, 20, 64)])
    a, b, sum_sq, prod_sq = pair

    eq_latex = f"x^4 - {sum_sq}x^2 + {prod_sq} = 0"
    ans_latex = f"x = \\pm {a} \\quad \\text{{or}} \\quad x = \\pm {b}"
    ans_sympy = f"x = {a} or x = -{a} or x = {b} or x = -{b}"

    prompt = f"Solve for $x$:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve biquadratic quartic equation",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"k^2 - {sum_sq}k + {prod_sq} = 0 \\quad (k = x^2)", op="Substitute k = x^2", rule="Quadratic substitution"),
            step(from_latex=f"(k - {a**2})(k - {b**2}) = 0", to_latex_str=f"k = {a**2} \\text{{ or }} k = {b**2}", op="Factorise quadratic in k", rule="Zero product rule"),
            step(from_latex=f"x^2 = {a**2} \\text{{ or }} x^2 = {b**2}", to_latex_str=ans_latex, op="Take square roots of each value", rule=f"x = ±{a} or x = ±{b}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="18_k_substitution_quartic_biquadratic",
        learning_objective_id=f"{LO_PREFIX}_18",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=ans_sympy,
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Substitute k = x²", "marks": 1}, {"desc": f"k = {a**2} or k = {b**2}", "marks": 1}, {"desc": f"x = ±{a}", "marks": 1}, {"desc": f"x = ±{b}", "marks": 1}]},
        hints={"nudge": "Let k = x². Then x⁴ = (x²)² = k².", "concept": "Solve the quadratic for k, then take the square root of each solution.", "breakdown": f"k² - {sum_sq}k + {prod_sq} = 0 \\implies k = {a**2} or {b**2} \\implies x = ±{a} or ±{b}."},
        misconception_tags=["forgetting_plus_minus_when_taking_square_root_of_k"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 19. k-Substitution: Quartic with Two Real and Two Non-Real Roots
# ---------------------------------------------------------------------------
def build_19_k_substitution_quartic_two_real_two_nonreal(r: random.Random) -> Dict[str, Any]:
    # x^4 - (a^2 - c)x^2 - a^2*c = 0 where k1 = a^2 (real) and k2 = -c (non-real)
    pair = r.choice([(2, 1, 3, 4), (3, 1, 8, 9), (2, 5, -1, 20), (3, 2, 7, 18)])
    a, c, b_coef, d_val = pair
    # (x^2 - a^2)(x^2 + c) = x^4 - (a^2 - c)x^2 - a^2*c = 0
    # Let's clean up coefficients:
    mid = a * a - c
    prod = a * a * c
    sign_mid = f"- {mid}" if mid >= 0 else f"+ {abs(mid)}"

    eq_latex = f"x^4 {sign_mid}x^2 - {prod} = 0"
    ans_latex = f"x = {a} \\quad \\text{{or}} \\quad x = -{a}"

    prompt = f"Solve for $x$ in the real number system:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve biquadratic equation and reject negative square root",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str=f"\\left(x^2 - {a**2}\\right)\\left(x^2 + {c}\\right) = 0", op="Factorise as quadratic in x²", rule="Trinomial factorisation"),
            step(from_latex=f"x^2 = {a**2} \\quad \\text{{or}} \\quad x^2 = -{c}", to_latex_str=ans_latex, op=f"Solve x² = {a**2} \\implies x = ±{a}; reject x² = -{c}", rule="x² >= 0 for all real x"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="19_k_substitution_quartic_two_real_two_nonreal",
        learning_objective_id=f"{LO_PREFIX}_19",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x = {a} or x = -{a}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Factorise in terms of x²", "marks": 1}, {"desc": f"x² = {a**2} or x² = -{c}", "marks": 1}, {"desc": f"Reject x² = -{c} (no real solution)", "marks": 1}, {"desc": f"x = ±{a}", "marks": 1}]},
        hints={"nudge": f"Let k = x². Note that x² cannot be negative for any real number.", "concept": "x² = -c has no real solutions. Only x² = a² yields real roots.", "breakdown": f"x² = {a**2} \\implies x = ±{a}. x² = -{c} is non-real."},
        misconception_tags=["taking_square_root_of_negative_number_in_real_system"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=4,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 20. k-Substitution: Algebraic Fraction Bracket
# ---------------------------------------------------------------------------
def build_20_k_substitution_algebraic_fraction(r: random.Random) -> Dict[str, Any]:
    # (x + 1/x)^2 - 4(x + 1/x) + 3 = 0
    # Let k = x + 1/x. (k - 1)(k - 3) = 0 -> k = 1 or k = 3
    # Case k = 1: x + 1/x = 1 -> x^2 - x + 1 = 0 -> Delta = 1 - 4 = -3 (no real roots)
    # Case k = 3: x + 1/x = 3 -> x^2 - 3x + 1 = 0 -> x = (3 +- sqrt(5))/2
    # Let's use simpler values where roots are rational:
    # (x - 2/x)^2 - (x - 2/x) - 2 = 0 -> k^2 - k - 2 = 0 -> k = 2 or k = -1
    # x - 2/x = 2 -> x^2 - 2x - 2 = 0
    # Or: k = x + 2/x, let k1 = 3 -> x + 2/x = 3 -> x^2 - 3x + 2 = 0 -> x = 1, 2
    # k2 = 3.5 -> 2x^2 - 7x + 4 = 0
    # Let's use: (x - 6/x)^2 + (x - 6/x) - 2 = 0 -> k = 1 or k = -2
    # x - 6/x = 1 -> x^2 - x - 6 = 0 -> (x-3)(x+2) = 0 -> x = 3, -2
    # x - 6/x = -2 -> x^2 + 2x - 6 = 0
    # Even cleaner:
    # 2(x + 1/x)^2 - 5(x + 1/x) + 2 = 0 -> (2k - 1)(k - 2) = 0 -> k = 2 or k = 1/2
    # x + 1/x = 2 -> x^2 - 2x + 1 = 0 -> (x-1)^2 = 0 -> x = 1
    # x + 1/x = 1/2 -> 2x^2 - x + 2 = 0 -> Delta = 1 - 16 < 0 (no real sol)
    eq_latex = "2\\left(x + \\frac{1}{x}\\right)^2 - 5\\left(x + \\frac{1}{x}\\right) + 2 = 0"
    ans_latex = "x = 1"

    prompt = f"Solve for $x$ in the real number system using $k$-substitution:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Solve fraction bracket quadratic via k-substitution",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=eq_latex, to_latex_str="2k^2 - 5k + 2 = 0 \\quad \\left(k = x + \\frac{1}{x}\\right)", op="Substitute k = x + 1/x", rule="k-substitution"),
            step(from_latex="2k^2 - 5k + 2 = 0", to_latex_str="k = 2 \\quad \\text{or} \\quad k = \\frac{1}{2}", op="Factorise (2k - 1)(k - 2) = 0", rule="Zero product rule"),
            step(from_latex="x + \\frac{1}{x} = 2 \\implies x^2 - 2x + 1 = 0", to_latex_str="x = 1", op="Solve for x when k = 2", rule="(x - 1)² = 0"),
            step(from_latex="x + \\frac{1}{x} = \\frac{1}{2} \\implies 2x^2 - x + 2 = 0", to_latex_str="\\text{No real solution} \\; (\\Delta = -15 < 0)", op="Check k = 1/2", rule="Discriminant test"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="20_k_substitution_algebraic_fraction",
        learning_objective_id=f"{LO_PREFIX}_20",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy="x = 1",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 4, "steps": [{"desc": "Substitute k = x + 1/x", "marks": 1}, {"desc": "Find k = 2 or k = 1/2", "marks": 1}, {"desc": "Solve x² - 2x + 1 = 0 to get x = 1", "marks": 1}, {"desc": "Reject k = 1/2 (Δ < 0)", "marks": 1}]},
        hints={"nudge": "Let k = x + 1/x. Factorise the quadratic in k.", "concept": "For each value of k, multiply through by x to form a quadratic in x.", "breakdown": "k = 2 gives x² - 2x + 1 = 0 \\implies x = 1. k = 1/2 gives 2x² - x + 2 = 0 which has Δ < 0 (no real roots)."},
        misconception_tags=["failing_to_verify_real_roots_for_all_k_branches"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=5,
        difficulty="hard",
    )


# ---------------------------------------------------------------------------
# 21. Form Quadratic Equation from Integer Roots
# ---------------------------------------------------------------------------
def build_21_find_quadratic_equation_from_integer_roots(r: random.Random) -> Dict[str, Any]:
    r1 = r.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    r2 = r.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    while r1 == r2:
        r2 = r.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

    b = -(r1 + r2)
    c = r1 * r2
    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    ans_latex = f"x^2 {sign_b}x {sign_c} = 0"

    prompt = f"Determine a quadratic equation in the form $x^2 + bx + c = 0$ that has roots $x = {r1}$ and $x = {r2}$."

    p1 = -r1
    p2 = -r2
    sign_p1 = f"+ {p1}" if p1 >= 0 else f"- {abs(p1)}"
    sign_p2 = f"+ {p2}" if p2 >= 0 else f"- {abs(p2)}"

    sol = solution_graph(
        goal="Determine quadratic equation from given roots",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=f"x = {r1}, \\; x = {r2}", to_latex_str=f"(x {sign_p1})(x {sign_p2}) = 0", op="Write linear factors from roots", rule="(x - r1)(x - r2) = 0"),
            step(from_latex=f"(x {sign_p1})(x {sign_p2}) = 0", to_latex_str=ans_latex, op="Expand binomial product", rule="FOIL expansion"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="21_find_quadratic_equation_from_integer_roots",
        learning_objective_id=f"{LO_PREFIX}_21",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x**2 + {b}*x + {c} = 0",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": "Factors (x - r1)(x - r2) = 0", "marks": 1}, {"desc": f"Expanded equation {ans_latex}", "marks": 1}]},
        hints={"nudge": "If the roots are r1 and r2, the equation is (x - r1)(x - r2) = 0.", "concept": "x² - (sum of roots)x + (product of roots) = 0.", "breakdown": f"Sum = {r1+r2}, Product = {r1*r2}. Equation: {ans_latex}."},
        misconception_tags=["using_wrong_signs_when_constructing_factors_from_roots"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 22. Form Quadratic Equation from Fractional Roots
# ---------------------------------------------------------------------------
def build_22_find_quadratic_equation_from_fractional_roots(r: random.Random) -> Dict[str, Any]:
    # Roots: x = p/q and x = r
    q_den = r.choice([2, 3, 5])
    p_num = r.choice([1, -1, 2, -2])
    while math.gcd(abs(p_num), q_den) != 1:
        p_num = r.choice([1, -1, 2, -2])
    r_int = r.choice([2, 3, 4, -2, -3])

    # (q*x - p)(x - r) = q*x^2 - (q*r + p)x + p*r = 0
    a = q_den
    b = -(q_den * r_int + p_num)
    c = p_num * r_int

    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    ans_latex = f"{a}x^2 {sign_b}x {sign_c} = 0"

    lat_frac = f"\\frac{{{p_num}}}{{{q_den}}}" if p_num > 0 else f"-\\frac{{{abs(p_num)}}}{{{q_den}}}"
    prompt = f"Determine a quadratic equation with integer coefficients ($ax^2 + bx + c = 0$, $a > 0$) that has roots $x = {lat_frac}$ and $x = {r_int}$."

    sol = solution_graph(
        goal="Determine quadratic equation with integer coefficients from fractional roots",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=f"x = {lat_frac}, \\; x = {r_int}", to_latex_str=f"({q_den}x - {p_num})(x - {r_int}) = 0" if p_num >= 0 else f"({q_den}x + {abs(p_num)})(x - {r_int}) = 0", op="Clear denominator in fractional factor", rule=f"x = p/q implies qx - p = 0"),
            step(from_latex=f"({q_den}x - {p_num})(x - {r_int}) = 0", to_latex_str=ans_latex, op="Expand binomial product", rule="FOIL expansion"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="22_find_quadratic_equation_from_fractional_roots",
        learning_objective_id=f"{LO_PREFIX}_22",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"{a}*x**2 + {b}*x + {c} = 0",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": f"Factor with integer coefficients ({q_den}x - {p_num})", "marks": 1}, {"desc": f"Second factor (x - {r_int})", "marks": 1}, {"desc": f"Expanded equation {ans_latex}", "marks": 1}]},
        hints={"nudge": f"If x = p/q, multiply by q to get qx - p = 0.", "concept": "The factor for x = p/q is (qx - p). Multiply by (x - r) to obtain integer coefficients.", "breakdown": f"({q_den}x - {p_num})(x - {r_int}) = 0 \\implies {ans_latex}."},
        misconception_tags=["leaving_fractions_in_equation_when_integer_coefficients_requested"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 23. Form Quadratic Equation from Conjugate Surd Roots
# ---------------------------------------------------------------------------
def build_23_find_quadratic_equation_from_surd_conjugates(r: random.Random) -> Dict[str, Any]:
    p = r.choice([1, 2, 3, 4])
    q = r.choice([2, 3, 5])
    # Roots: p + \sqrt{q} and p - \sqrt{q}
    # Sum of roots = 2p -> b = -2p
    # Product of roots = p^2 - q -> c = p^2 - q
    b = -2 * p
    c = (p * p) - q

    sign_b = f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    ans_latex = f"x^2 {sign_b}x {sign_c} = 0"

    prompt = f"Find a quadratic equation with rational coefficients in the form $x^2 + bx + c = 0$ having roots $x = {p} + \\sqrt{{{q}}}$ and $x = {p} - \\sqrt{{{q}}}$."

    sol = solution_graph(
        goal="Form quadratic equation from conjugate surd roots using sum and product",
        chain_type="equation",
        var="x",
        steps=[
            step(from_latex=f"\\text{{Sum}} = ({p} + \\sqrt{{{q}}}) + ({p} - \\sqrt{{{q}}}) = {2 * p}", to_latex_str=f"b = -\\text{{Sum}} = {-2 * p}", op="Add roots to find b", rule="Sum of roots = -b/a"),
            step(from_latex=f"\\text{{Product}} = ({p} + \\sqrt{{{q}}})({p} - \\sqrt{{{q}}}) = {p}^2 - (\\sqrt{{{q}}})^2 = {c}", to_latex_str=f"c = \\text{{Product}} = {c}", op="Multiply conjugate roots to find c", rule="Product of roots = c/a"),
            step(from_latex=f"x^2 - (\\text{{Sum}})x + (\\text{{Product}}) = 0", to_latex_str=ans_latex, op="Combine into quadratic equation", rule=ans_latex),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="23_find_quadratic_equation_from_surd_conjugates",
        learning_objective_id=f"{LO_PREFIX}_23",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"x**2 + {b}*x + {c} = 0",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": f"Sum of roots = {2*p}", "marks": 1}, {"desc": f"Product of roots = {c}", "marks": 1}, {"desc": f"Equation {ans_latex}", "marks": 1}]},
        hints={"nudge": "Use the relationship: x² - (Sum of roots)x + (Product of roots) = 0.", "concept": "Conjugate surds eliminate radicals when added and multiplied: (p + √q)(p - √q) = p² - q.", "breakdown": f"Sum = {2*p}, Product = {p}² - {q} = {c}. Equation: {ans_latex}."},
        misconception_tags=["failing_to_use_conjugate_product_to_eliminate_surd"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# 24. Sum and Product of Roots from Equation
# ---------------------------------------------------------------------------
def build_24_quadratic_sum_and_product_of_roots(r: random.Random) -> Dict[str, Any]:
    a = r.choice([2, 3, 4])
    b = r.choice([-7, -5, -3, 3, 5, 7])
    c = r.choice([-6, -4, 2, 4, 6])

    sign_b = f"+ {b}" if b >= 0 else f"- {abs(b)}"
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    eq_latex = f"{a}x^2 {sign_b}x {sign_c} = 0"

    sum_val = sp.Rational(-b, a)
    prod_val = sp.Rational(c, a)
    ans_latex = f"\\text{{Sum}} = {to_latex(sum_val)}, \\quad \\text{{Product}} = {to_latex(prod_val)}"

    prompt = f"Without solving the equation, determine the **sum** and **product** of the roots for:\n\n$${eq_latex}$$"

    sol = solution_graph(
        goal="Find sum and product of roots using coefficients",
        chain_type="calculation",
        steps=[
            step(from_latex="\\alpha + \\beta = -\\frac{b}{a}", to_latex_str=f"\\text{{Sum}} = -\\frac{{{b}}}{{{a}}} = {to_latex(sum_val)}", op="Apply sum of roots formula -b/a", rule="Sum of roots formula"),
            step(from_latex="\\alpha \\cdot \\beta = \\frac{c}{a}", to_latex_str=f"\\text{{Product}} = \\frac{{{c}}}{{{a}}} = {to_latex(prod_val)}", op="Apply product of roots formula c/a", rule="Product of roots formula"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="24_quadratic_sum_and_product_of_roots",
        learning_objective_id=f"{LO_PREFIX}_24",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"Sum = {sum_val}, Product = {prod_val}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 2, "steps": [{"desc": f"Sum = -b/a = {to_latex(sum_val)}", "marks": 1}, {"desc": f"Product = c/a = {to_latex(prod_val)}", "marks": 1}]},
        hints={"nudge": "For ax² + bx + c = 0, Sum = -b/a and Product = c/a.", "concept": "You do not need to solve the quadratic equation!", "breakdown": f"Sum = -({b})/{a} = {to_latex(sum_val)}. Product = ({c})/{a} = {to_latex(prod_val)}."},
        misconception_tags=["sign_error_in_sum_of_roots_formula"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=2,
        difficulty="easy",
    )


# ---------------------------------------------------------------------------
# 25. Quadratic with Unknown Parameter (Given One Root)
# ---------------------------------------------------------------------------
def build_25_quadratic_equation_with_unknown_coefficient(r: random.Random) -> Dict[str, Any]:
    r1 = r.choice([2, 3, 4])
    r2 = r.choice([-5, -4, -3, -2, -1, 1])
    while r1 == r2:
        r2 = r.choice([-5, -4, -3, -2, -1, 1])

    b = -(r1 + r2)
    c = r1 * r2

    # Give equation with k in place of b or c:
    # e.g. x^2 + kx + c = 0 has root x = r1. Find k.
    sign_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
    eq_latex = f"x^2 + kx {sign_c} = 0"
    ans_latex = f"k = {b}, \\quad \\text{{other root }} x = {r2}"

    prompt = f"Given that $x = {r1}$ is a root of the equation $${eq_latex}$$\n\nFind the value of $k$ and the second root of the equation."

    sol = solution_graph(
        goal="Find unknown coefficient and second root given one root",
        chain_type="equation",
        var="k",
        steps=[
            step(from_latex=f"({r1})^2 + k({r1}) {sign_c} = 0", to_latex_str=f"{r1**2} + {r1}k {sign_c} = 0", op=f"Substitute root x = {r1} into equation", rule="Root satisfies equation"),
            step(from_latex=f"{r1}k = -({r1**2} {sign_c})", to_latex_str=f"k = {b}", op=f"Solve for k", rule=f"k = {b}"),
            step(from_latex=f"x^2 + ({b})x {sign_c} = 0", to_latex_str=f"(x - {r1})(x - {r2}) = 0 \\implies x = {r2}", op="Substitute k and factorise to find second root", rule=f"Other root is {r2}"),
        ],
        final_latex=ans_latex,
    )

    return make_math_question(
        prefix="g11_eq",
        topic=TOPIC,
        subskill="25_quadratic_equation_with_unknown_coefficient",
        learning_objective_id=f"{LO_PREFIX}_25",
        prompt=prompt,
        prompt_latex=prompt,
        answer_mode="typed",
        question_type="math_short",
        answer_latex=ans_latex,
        answer_sympy=f"k = {b}, other root = {r2}",
        sample_answer=ans_latex,
        canonical_solution=sol,
        marking_schema={"total_marks": 3, "steps": [{"desc": f"Substitute x = {r1}", "marks": 1}, {"desc": f"Solve k = {b}", "marks": 1}, {"desc": f"Find second root x = {r2}", "marks": 1}]},
        hints={"nudge": f"Substitute x = {r1} directly into the equation to solve for k.", "concept": "Since x = r1 is a root, replacing x with {r1} makes the equation true.", "breakdown": f"({r1})² + k({r1}) + {c} = 0 \\implies k = {b}. Then factorise x² + {b}x + {c} = 0 to find the second root x = {r2}."},
        misconception_tags=["failing_to_substitute_given_root_into_equation"],
        term=1,
        caps_weight_percent=20,
        suggested_duration_mins=3,
        difficulty="medium",
    )


# ---------------------------------------------------------------------------
# Registry of Archetypes 01–25
# ---------------------------------------------------------------------------
BUILDERS_01_25: Dict[str, Any] = {
    "01_quadratic_factorisation_monic_integers": build_01_quadratic_factorisation_monic_integers,
    "02_quadratic_factorisation_common_factor": build_02_quadratic_factorisation_common_factor,
    "03_quadratic_factorisation_difference_of_squares": build_03_quadratic_factorisation_difference_of_squares,
    "04_quadratic_factorisation_non_monic_prime_a": build_04_quadratic_factorisation_non_monic_prime_a,
    "05_quadratic_factorisation_non_monic_composite_a": build_05_quadratic_factorisation_non_monic_composite_a,
    "06_quadratic_expand_brackets_first": build_06_quadratic_expand_brackets_first,
    "07_quadratic_algebraic_fraction_lcd": build_07_quadratic_algebraic_fraction_lcd,
    "08_completing_the_square_monic_even_b": build_08_completing_the_square_monic_even_b,
    "09_completing_the_square_monic_surd_roots": build_09_completing_the_square_monic_surd_roots,
    "10_completing_the_square_monic_odd_b": build_10_completing_the_square_monic_odd_b,
    "11_completing_the_square_non_monic": build_11_completing_the_square_non_monic,
    "12_completing_the_square_identify_term_to_add": build_12_completing_the_square_identify_term_to_add,
    "13_quadratic_formula_exact_surd_roots": build_13_quadratic_formula_exact_surd_roots,
    "14_quadratic_formula_rounded_two_decimals": build_14_quadratic_formula_rounded_two_decimals,
    "15_quadratic_formula_negative_leading_coef": build_15_quadratic_formula_negative_leading_coef,
    "16_quadratic_formula_discriminant_identification": build_16_quadratic_formula_discriminant_identification,
    "17_k_substitution_quadratic_bracket_squared": build_17_k_substitution_quadratic_bracket_squared,
    "18_k_substitution_quartic_biquadratic": build_18_k_substitution_quartic_biquadratic,
    "19_k_substitution_quartic_two_real_two_nonreal": build_19_k_substitution_quartic_two_real_two_nonreal,
    "20_k_substitution_algebraic_fraction": build_20_k_substitution_algebraic_fraction,
    "21_find_quadratic_equation_from_integer_roots": build_21_find_quadratic_equation_from_integer_roots,
    "22_find_quadratic_equation_from_fractional_roots": build_22_find_quadratic_equation_from_fractional_roots,
    "23_find_quadratic_equation_from_surd_conjugates": build_23_find_quadratic_equation_from_surd_conjugates,
    "24_quadratic_sum_and_product_of_roots": build_24_quadratic_sum_and_product_of_roots,
    "25_quadratic_equation_with_unknown_coefficient": build_25_quadratic_equation_with_unknown_coefficient,
}
