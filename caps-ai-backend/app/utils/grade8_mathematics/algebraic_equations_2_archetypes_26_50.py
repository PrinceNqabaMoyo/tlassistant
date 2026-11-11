"""
Grade 8 Mathematics - Algebraic Equations 2 Archetypes (26 to 50).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/02. Algebraic equations 2.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_geometric_angles_quadrilateral_interior_sum(rng: random.Random) -> Dict[str, Any]:
    ans = 36
    a1 = ans
    a2 = 2 * ans
    a3 = 3 * ans
    a4 = 4 * ans

    return {
        "title": "Geometric Modelling: Interior Angles of a Quadrilateral",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "26_geometric_angles_quadrilateral_interior_sum",
        "difficulty": "medium",
        "question_text": (
            "The four interior angles of a convex quadrilateral are **$x^\\circ$**, **$2x^\\circ$**, "
            "**$3x^\\circ$**, and **$4x^\\circ$**.\n\n"
            "1. Set up an algebraic equation using the angle sum of a quadrilateral.\n"
            "2. Solve for $x$ and determine the size of the largest interior angle."
        ),
        "correct_answer": f"1. x + 2x + 3x + 4x = 360 (or 10x = 360). 2. x = {ans}°; largest angle = {a4}°.",
        "marking_schema": [
            "Equation: 10x = 360 [1 mark]",
            f"Solve: x = {ans}°; largest angle = {a4}° [1 mark]",
        ],
        "hints": [
            "The sum of interior angles in any quadrilateral is 360 degrees.",
            "x + 2x + 3x + 4x = 10x = 360.",
            f"x = 360 ÷ 10 = {ans}.",
            f"Largest angle = 4({ans}) = {a4}°.",
        ],
        "misconception_tags": ["quadrilateral_angle_sum_gap"],
        "diagram_spec": None,
    }


def arch_27_age_problem_parent_and_two_children(rng: random.Random) -> Dict[str, Any]:
    x = rng.randint(12, 18)
    diff = rng.randint(3, 6)
    c1 = x
    c2 = x + diff
    mother = c1 + c2  # 2x + diff

    return {
        "title": "Age Modelling: Parent's Age Equal to Sum of Children's Ages",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "27_age_problem_parent_and_two_children",
        "difficulty": "medium",
        "question_text": (
            f"A mother is currently **{mother} years old**. Her younger child is $x$ years old, "
            f"and her older child is **{diff} years older** than the younger child.\n\n"
            "If the mother's age is equal to the sum of the ages of her two children, "
            "write an algebraic equation and calculate the age of both children."
        ),
        "correct_answer": f"Equation: x + (x + {diff}) = {mother} (or 2x + {diff} = {mother}). Younger child = {c1} years; Older child = {c2} years.",
        "marking_schema": [
            f"Equation: 2x + {diff} = {mother} [1 mark]",
            f"Solve: x = {c1}; older = {c2} years [1 mark]",
        ],
        "hints": [
            f"Younger child is $x$, older child is $x + {diff}$.",
            f"Sum = $x + x + {diff} = 2x + {diff} = {mother}$.",
            f"$2x = {mother - diff} \\implies x = {c1}$.",
        ],
        "misconception_tags": ["age_sum_two_children_equation_error"],
        "diagram_spec": None,
    }


def arch_28_age_problem_future_years_ratio(rng: random.Random) -> Dict[str, Any]:
    # In 10 years, father (currently 3x) will be twice as old as son (x + 10)
    # 3x + 10 = 2(x + 10) => 3x + 10 = 2x + 20 => x = 10
    son_now = 10
    father_now = 30
    years = 10

    return {
        "title": "Age Modelling: Future Age Multiple Equations",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "28_age_problem_future_years_ratio",
        "difficulty": "hard",
        "question_text": (
            "Currently, Mr Dlamini is three times as old as his son Sipho. "
            f"In **{years} years' time**, Mr Dlamini will be **twice as old** as Sipho.\n\n"
            "1. Formulate an equation for their ages in 10 years (let Sipho's current age be $x$).\n"
            "2. Solve for $x$ and determine how old both Sipho and his father are now."
        ),
        "correct_answer": f"1. 3x + {years} = 2(x + {years}). 2. Sipho is {son_now} years old; Mr Dlamini is {father_now} years old.",
        "marking_schema": [
            f"Equation: 3x + {years} = 2(x + {years}) [1 mark]",
            f"Solve: x = {son_now}; father = {father_now} years [1 mark]",
        ],
        "hints": [
            "Now: Sipho = $x$, Father = $3x$.",
            f"In {years} years: Sipho = $x + {years}$, Father = $3x + {years}$.",
            f"Condition: $3x + {years} = 2(x + {years})$.",
            f"$3x + {years} = 2x + 20 \\implies x = {son_now}$.",
        ],
        "misconception_tags": ["future_age_bracket_multiplier_error"],
        "diagram_spec": None,
    }


def arch_29_distance_speed_time_meeting_problem(rng: random.Random) -> Dict[str, Any]:
    v1 = rng.choice([12, 15])
    v2 = rng.choice([18, 20])
    t = rng.choice([2, 3])
    d = (v1 + v2) * t

    return {
        "title": "Motion Modelling: Two Objects Travelling Toward Each Other",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "29_distance_speed_time_meeting_problem",
        "difficulty": "hard",
        "question_text": (
            f"Two cyclists start **{d}\\text{{ km}}** apart and ride toward each other on the same road.\n\n"
            f"- Cyclist A travels at **{v1}\\text{{ km/h}}**.\n"
            f"- Cyclist B travels at **{v2}\\text{{ km/h}}**.\n\n"
            "1. Write an algebraic equation in terms of time $t$ (hours) until they meet.\n"
            "2. Solve for $t$."
        ),
        "correct_answer": f"1. {v1}t + {v2}t = {d} (or {v1 + v2}t = {d}). 2. t = {t} hours.",
        "marking_schema": [
            f"Equation: {v1 + v2}t = {d} [1 mark]",
            f"Solve: t = {t} hours [1 mark]",
        ],
        "hints": [
            f"Distance travelled by A = {v1}t; Distance travelled by B = {v2}t.",
            f"Together they cover the full distance: {v1}t + {v2}t = {d}.",
            f"{v1 + v2}t = {d} \\implies t = {d} ÷ {v1 + v2} = {t} hours.",
        ],
        "misconception_tags": ["combined_motion_equation_setup"],
        "diagram_spec": None,
    }


def arch_30_distance_speed_time_overtaking_problem(rng: random.Random) -> Dict[str, Any]:
    v_slow = 60
    v_fast = 80
    headstart_hours = 1
    # 80t = 60(t + 1) => 20t = 60 => t = 3
    t_fast = 3
    d_meet = v_fast * t_fast  # 240 km

    return {
        "title": "Motion Modelling: Overtaking Problem",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "30_distance_speed_time_overtaking_problem",
        "difficulty": "hard",
        "question_text": (
            f"A delivery truck departs at **{v_slow}\\text{{ km/h}}**. "
            f"One hour later, a courier car departs along the same route at **{v_fast}\\text{{ km/h}}**.\n\n"
            "1. If $t$ is the travel time of the courier car, write an equation equating the distances travelled.\n"
            "2. How many hours will it take the courier car to catch up with the truck?"
        ),
        "correct_answer": f"1. {v_fast}t = {v_slow}(t + {headstart_hours}). 2. t = {t_fast} hours.",
        "marking_schema": [
            f"Equation: {v_fast}t = {v_slow}(t + 1) [1 mark]",
            f"Solve: 20t = 60 => t = {t_fast} hours [1 mark]",
        ],
        "hints": [
            f"Truck has travelled for $t + 1$ hours, so its distance is {v_slow}(t + 1).",
            f"Car travels for $t$ hours, so its distance is {v_fast}t.",
            f"{v_fast}t = {v_slow}t + {v_slow} \\implies {v_fast - v_slow}t = {v_slow} \\implies t = {t_fast}.",
        ],
        "misconception_tags": ["headstart_time_bracket_error"],
        "diagram_spec": None,
    }


def arch_31_money_coin_problem_two_denominations(rng: random.Random) -> Dict[str, Any]:
    diff = rng.randint(6, 12)  # 10 more R2 coins than R5 coins
    n5 = rng.randint(10, 20)
    n2 = n5 + diff
    tot = 2 * n2 + 5 * n5  # 2(x + diff) + 5x = 7x + 2*diff

    return {
        "title": "Financial Modelling: Coin Denominations",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "31_money_coin_problem_two_denominations",
        "difficulty": "hard",
        "question_text": (
            f"A money tin contains only R2 and R5 coins. There are **{diff} more R2 coins** than R5 coins. "
            f"The total value of the money in the tin is **R{tot}**.\n\n"
            "1. Write an algebraic equation in terms of $x$ (the number of R5 coins).\n"
            "2. Solve for $x$ and determine how many of each coin are in the tin."
        ),
        "correct_answer": f"1. 5x + 2(x + {diff}) = {tot} (or 7x + {2*diff} = {tot}). 2. {n5} R5 coins and {n2} R2 coins.",
        "marking_schema": [
            f"Equation: 7x + {2*diff} = {tot} [1 mark]",
            f"Solve: x = {n5} R5 coins; {n2} R2 coins [1 mark]",
        ],
        "hints": [
            f"Let $x$ = number of R5 coins. Value = 5x.",
            f"Number of R2 coins = $x + {diff}$. Value = 2(x + {diff}).",
            f"Total = $5x + 2x + {2*diff} = 7x + {2*diff} = {tot}$.",
            f"$7x = {tot - 2*diff} \\implies x = {n5}$.",
        ],
        "misconception_tags": ["coin_count_vs_value_confusion"],
        "diagram_spec": None,
    }


def arch_32_tickets_two_tier_pricing_equation(rng: random.Random) -> Dict[str, Any]:
    total_tickets = 100
    p_adult = 50
    p_child = 25
    adults = rng.choice([40, 50, 60])
    children = total_tickets - adults
    tot_revenue = adults * p_adult + children * p_child

    return {
        "title": "Financial Modelling: Two-Tier Event Ticket Sales",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "32_tickets_two_tier_pricing_equation",
        "difficulty": "hard",
        "question_text": (
            f"A school drama production sold **{total_tickets} tickets in total**, collecting **R{tot_revenue}**.\n\n"
            f"- Adult tickets cost **R{p_adult} each**.\n"
            f"- Learner tickets cost **R{p_child} each**.\n\n"
            "1. If $a$ represents the number of adult tickets sold, write an equation for the total ticket revenue.\n"
            "2. Solve for $a$ to find how many adult tickets were sold."
        ),
        "correct_answer": f"1. {p_adult}a + {p_child}({total_tickets} - a) = {tot_revenue}. 2. a = {adults} adult tickets.",
        "marking_schema": [
            f"Equation: {p_adult}a + {p_child}({total_tickets} - a) = {tot_revenue} [1 mark]",
            f"Solve: 25a + {p_child * total_tickets} = {tot_revenue} => a = {adults} [1 mark]",
        ],
        "hints": [
            f"If adult tickets = $a$, then learner tickets = ${total_tickets} - a$.",
            f"Revenue = {p_adult}a + {p_child}({total_tickets} - a) = {tot_revenue}.",
            f"{p_adult - p_child}a + {p_child * total_tickets} = {tot_revenue}.",
            f"25a = {tot_revenue - p_child * total_tickets} \\implies a = {adults}.",
        ],
        "misconception_tags": ["two_tier_pricing_algebraic_setup_error"],
        "diagram_spec": None,
    }


def arch_33_sharing_items_in_given_ratio_equation(rng: random.Random) -> Dict[str, Any]:
    r1 = 2
    r2 = 3
    x_val = rng.choice([15, 20, 25])
    tot_items = (r1 + r2) * x_val
    share1 = r1 * x_val
    share2 = r2 * x_val

    return {
        "title": "Ratio Modelling: Formulating and Solving Ratio Equations",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "33_sharing_items_in_given_ratio_equation",
        "difficulty": "medium",
        "question_text": (
            f"A prize of **{tot_items} books** is shared between School A and School B in the ratio **{r1} : {r2}**.\n\n"
            f"1. Let each ratio part be represented by $x$. Write an algebraic equation for the total books.\n"
            "2. Solve for $x$ and determine how many books each school receives."
        ),
        "correct_answer": f"1. {r1}x + {r2}x = {tot_items} (or 5x = {tot_items}). 2. School A = {share1} books; School B = {share2} books.",
        "marking_schema": [
            f"Equation: {r1 + r2}x = {tot_items} [1 mark]",
            f"Solve: x = {x_val}; School A = {share1}, School B = {share2} [1 mark]",
        ],
        "hints": [
            f"School A receives {r1}x and School B receives {r2}x.",
            f"{r1}x + {r2}x = 5x = {tot_items}.",
            f"x = {tot_items} ÷ 5 = {x_val}.",
            f"School A = 2({x_val}) = {share1}; School B = 3({x_val}) = {share2}.",
        ],
        "misconception_tags": ["ratio_equation_part_multiplier_error"],
        "diagram_spec": None,
    }


def arch_34_perimeter_of_parallelogram_equation(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(3, 7)
    # Opposite sides equal: 2x + 3 = x + 7 => x = 4
    # let's parameterize: 2x + a = x + b => x = b - a
    a = 3
    b = ans + a
    adj = rng.randint(5, 9)
    side_len = 2 * ans + a
    p = 2 * (side_len + adj)

    return {
        "title": "Geometric Modelling: Parallelogram Opposite Sides",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "34_perimeter_of_parallelogram_equation",
        "difficulty": "medium",
        "question_text": (
            f"In a parallelogram, two opposite sides are given by **$(2x + {a})\\text{{ cm}}$** "
            f"and **$(x + {b})\\text{{ cm}}$**. The adjacent side has length **{adj}\\text{{ cm}}**.\n\n"
            "1. Formulate an equation for $x$ using parallelogram properties.\n"
            "2. Solve for $x$ and calculate the total perimeter of the parallelogram."
        ),
        "correct_answer": f"1. 2x + {a} = x + {b}. 2. x = {ans}; Perimeter = {p} cm.",
        "marking_schema": [
            f"Equation: 2x + {a} = x + {b} [1 mark]",
            f"Solve: x = {ans}; Perimeter = {p} cm [1 mark]",
        ],
        "hints": [
            "Opposite sides of a parallelogram are equal.",
            f"2x + {a} = x + {b} \\implies x = {ans}.",
            f"Side length = 2({ans}) + {a} = {side_len} cm.",
            f"Perimeter = 2({side_len} + {adj}) = {p} cm.",
        ],
        "misconception_tags": ["parallelogram_side_equality_gap"],
        "diagram_spec": None,
    }


def arch_35_rhombus_side_length_equation(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(4, 9)
    # 3x - a = 2x + b => x = a + b
    a = 5
    b = ans - a if ans > a else 2
    if ans <= a:
        ans = a + b
    side_len = 3 * ans - a
    p = 4 * side_len

    return {
        "title": "Geometric Modelling: Rhombus All Sides Equal",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "35_rhombus_side_length_equation",
        "difficulty": "medium",
        "question_text": (
            f"Two sides of a rhombus measure **$(3x - {a})\\text{{ cm}}$** and **$(2x + {b})\\text{{ cm}}$**.\n\n"
            "1. Write an equation using the definition of a rhombus.\n"
            "2. Solve for $x$ and calculate the perimeter of the rhombus."
        ),
        "correct_answer": f"1. 3x - {a} = 2x + {b}. 2. x = {ans}; Perimeter = {p} cm.",
        "marking_schema": [
            f"Equation: 3x - {a} = 2x + {b} [1 mark]",
            f"Solve: x = {ans}; Perimeter = {p} cm [1 mark]",
        ],
        "hints": [
            "All four sides of a rhombus are equal in length.",
            f"3x - {a} = 2x + {b} \\implies x = {ans}.",
            f"Side = 3({ans}) - {a} = {side_len} cm.",
            f"Perimeter = 4 x {side_len} = {p} cm.",
        ],
        "misconception_tags": ["rhombus_side_equality_rule"],
        "diagram_spec": None,
    }


def arch_36_fraction_equation_single_fraction_equals_binomial(rng: random.Random) -> Dict[str, Any]:
    # (2x + 4)/3 = x - 1 => 2x + 4 = 3x - 3 => x = 7
    denom = 3
    ans = 7
    a = 2
    b = 4
    d = 1

    return {
        "title": "Solving Equations: Single Fraction Equated to a Binomial",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "36_fraction_equation_single_fraction_equals_binomial",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$ by clearing the denominator:\n\n"
            f"$$\\frac{{{a}x + {b}}}{{{denom}}} = x - {d}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Multiply both sides by {denom}: {a}x + {b} = {denom}(x - {d}) [1 mark]",
            f"Expand and solve: {a}x + {b} = {denom}x - {denom * d} => x = {ans} [1 mark]",
        ],
        "hints": [
            f"Multiply both sides by {denom} to eliminate the fraction: ${a}x + {b} = {denom}(x - {d})$.",
            f"Expand RHS: ${a}x + {b} = {denom}x - {denom * d}$.",
            f"Subtract {a}x and add {denom * d}: x = {ans}.",
        ],
        "misconception_tags": ["clearing_denominators_bracket_omission"],
        "diagram_spec": None,
    }


def arch_37_fraction_equation_difference_of_fractions(rng: random.Random) -> Dict[str, Any]:
    # x/2 - x/3 = k => 3x/6 - 2x/6 = x/6 = k => x = 6*k
    k = rng.choice([3, 4, 5, 6])
    ans = 6 * k

    return {
        "title": "Solving Fractional Linear Equations: Difference of Fractions",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "37_fraction_equation_difference_of_fractions",
        "difficulty": "hard",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$\\frac{{x}}{{2}} - \\frac{{x}}{{3}} = {k}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Find common denominator 6: 3x/6 - 2x/6 = x/6 = {k} [1 mark]",
            f"Multiply by 6: x = {ans} [1 mark]",
        ],
        "hints": [
            "The lowest common denominator of 2 and 3 is 6.",
            f"$\\frac{{3x}}{{6}} - \\frac{{2x}}{{6}} = \\frac{{x}}{{6}}$.",
            f"$\\frac{{x}}{{6}} = {k} \\implies x = {k} \\times 6 = {ans}$.",
        ],
        "misconception_tags": ["fraction_equation_lcd_subtraction_error"],
        "diagram_spec": None,
    }


def arch_38_fraction_equation_binomial_numerators(rng: random.Random) -> Dict[str, Any]:
    # (x + 1)/2 = (x + 5)/3 => 3(x + 1) = 2(x + 5) => 3x + 3 = 2x + 10 => x = 7
    return {
        "title": "Solving Proportion Equations: Binomial Numerators",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "38_fraction_equation_binomial_numerators",
        "difficulty": "hard",
        "question_text": (
            "Solve for $x$ by cross-multiplication:\n\n"
            "$$\\frac{x + 1}{2} = \\frac{x + 5}{3}$$"
        ),
        "correct_answer": "7",
        "marking_schema": [
            "Cross-multiply: 3(x + 1) = 2(x + 5) [1 mark]",
            "Expand and solve: 3x + 3 = 2x + 10 => x = 7 [1 mark]",
        ],
        "hints": [
            "Cross-multiply denominators: $3(x + 1) = 2(x + 5)$.",
            "Expand both sides: $3x + 3 = 2x + 10$.",
            "Subtract 2x and subtract 3: $x = 7$.",
        ],
        "misconception_tags": ["cross_multiplication_bracket_error"],
        "diagram_spec": None,
    }


def arch_39_fraction_equation_monomial_denominator_cancelling(rng: random.Random) -> Dict[str, Any]:
    a = 2
    b = 3
    denom = 5
    rhs = 4
    # 2(x - 3)/5 = 4 => 2(x - 3) = 20 => x - 3 = 10 => x = 13
    ans = 13

    return {
        "title": "Solving Equations: Monomial Fraction Multipliers",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "39_fraction_equation_monomial_denominator_cancelling",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$\\frac{{{a}(x - {b})}}{{{denom}}} = {rhs}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Multiply by {denom}: {a}(x - {b}) = {denom * rhs} [1 mark]",
            f"Divide by {a} and add {b}: x - {b} = 10 => x = {ans} [1 mark]",
        ],
        "hints": [
            f"Multiply both sides by {denom}: {a}(x - {b}) = {denom * rhs}.",
            f"Divide by {a}: $x - {b} = {denom * rhs // a}$.",
            f"Add {b}: $x = {ans}$.",
        ],
        "misconception_tags": ["fraction_multiplier_distribution_error"],
        "diagram_spec": None,
    }


def arch_40_equation_leading_to_identity_all_real_solutions(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.randint(2, 5)
    ab = a * b

    return {
        "title": "Special Equation Types: Identity (Infinitely Many Solutions)",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "40_equation_leading_to_identity_all_real_solutions",
        "difficulty": "hard",
        "question_text": (
            f"Attempt to solve the equation for $x$:\n\n"
            f"$${a}(x + {b}) = {a}x + {ab}$$\n\n"
            "State what happens when you simplify both sides, and explain what this reveals about the solution set."
        ),
        "correct_answer": f"Expanding the LHS gives {a}x + {ab} = {a}x + {ab}. Subtracting {a}x gives {ab} = {ab}, which is always true. This is an identity, meaning any real number is a valid solution (infinitely many solutions).",
        "marking_schema": [
            f"Expand LHS: {a}x + {ab} = {a}x + {ab} leading to {ab} = {ab} [1 mark]",
            "Conclude statement is an identity / all real numbers are solutions [1 mark]",
        ],
        "hints": [
            f"Expand the left side: {a}x + {ab}.",
            f"Notice both sides are completely identical: {a}x + {ab} = {a}x + {ab}.",
            "Any number substituted for $x$ will make the equation true.",
        ],
        "misconception_tags": ["identity_equation_zero_root_confusion"],
        "diagram_spec": None,
    }


def arch_41_equation_leading_to_contradiction_no_solution(rng: random.Random) -> Dict[str, Any]:
    a = rng.randint(3, 6)
    b = rng.randint(2, 6)
    c = b + rng.randint(3, 7)

    return {
        "title": "Special Equation Types: Contradiction (No Solution)",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "41_equation_leading_to_contradiction_no_solution",
        "difficulty": "hard",
        "question_text": (
            f"Solve the equation for $x$:\n\n"
            f"$${a}x + {b} = {a}x + {c}$$\n\n"
            "State what happens when you subtract ${a}x$ from both sides, and explain what this means for the solution."
        ),
        "correct_answer": f"Subtracting {a}x from both sides results in {b} = {c}, which is a false statement (contradiction). Therefore, this equation has no solution (no value of x can make it true).",
        "marking_schema": [
            f"Show cancellation to false statement: {b} = {c} [1 mark]",
            "Conclude no solution / contradiction [1 mark]",
        ],
        "hints": [
            f"Subtract {a}x from both sides.",
            f"You get ${b} = {c}$, which is impossible.",
            "Since the statement is false, there is no solution.",
        ],
        "misconception_tags": ["contradiction_equation_zero_confusion"],
        "diagram_spec": None,
    }


def arch_42_diagnosing_bracket_expansion_error_in_equations(rng: random.Random) -> Dict[str, Any]:
    a = 3
    b = 4
    rhs = 21
    # 3(x + 4) = 21 => 3x + 12 = 21 => 3x = 9 => x = 3
    # error writes 3x + 4 = 21 => 3x = 17 => x = 17/3
    return {
        "title": "Diagnosing Error: Partial Distribution in Equation Solving",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "42_diagnosing_bracket_expansion_error_in_equations",
        "difficulty": "medium",
        "question_text": (
            f"A learner solves $3(x + 4) = 21$ by writing:\n\n"
            "> *'3x + 4 = 21, so 3x = 17, x = 17/3'*\n\n"
            "Explain the learner's algebraic error and find the **correct integer solution**."
        ),
        "correct_answer": "The learner only distributed the 3 to x and forgot to multiply 4 by 3 (3 x 4 = 12). The correct equation is 3x + 12 = 21 => 3x = 9 => x = 3.",
        "marking_schema": [
            "Identify omission of multiplying 4 by 3 (should be +12) [1 mark]",
            "State correct solution: x = 3 [1 mark]",
        ],
        "hints": [
            "Remember the distributive law applies to EVERY term inside parentheses.",
            "3(x + 4) = 3x + 12.",
            "3x + 12 = 21 \\implies 3x = 9 \\implies x = 3.",
        ],
        "misconception_tags": ["partial_distribution_error"],
        "diagram_spec": None,
    }


def arch_43_diagnosing_variable_cancellation_fallacy(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Diagnosing Misconceptions: Distinguishing x = 0 from Infinite Solutions",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "43_diagnosing_variable_cancellation_fallacy",
        "difficulty": "medium",
        "question_text": (
            "When simplifying an equation, a learner arrives at $0x = 0$ and writes $x = 0$.\n\n"
            "Explain why $x = 0$ is not the only solution, and state the complete solution set."
        ),
        "correct_answer": "0 multiplied by ANY real number equals 0 (e.g. 0 x 5 = 0, 0 x (-3) = 0). Therefore, x is not only 0; any real number satisfies 0x = 0 (infinitely many solutions).",
        "marking_schema": [
            "Explain that 0 multiplied by any number equals 0 [1 mark]",
            "Conclude that solution set is all real numbers (infinitely many) [1 mark]",
        ],
        "hints": [
            "Try substituting $x = 7$: does $0 \\times 7 = 0$?",
            "Try substituting $x = -10$: does $0 \\times (-10) = 0$?",
            "Any number works, so there are infinitely many solutions.",
        ],
        "misconception_tags": ["zero_coefficient_root_fallacy"],
        "diagram_spec": None,
    }


def arch_44_equation_with_decimal_coefficients_both_sides(rng: random.Random) -> Dict[str, Any]:
    # 1,5x + 2 = 0,5x + 6 => x = 4
    ans = 4
    return {
        "title": "Solving Equations with Decimal Coefficients on Both Sides",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "44_equation_with_decimal_coefficients_both_sides",
        "difficulty": "medium",
        "question_text": (
            "Solve for $x$:\n\n"
            "$$1,5x + 2 = 0,5x + 6$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            "Subtract 0,5x from both sides: 1,0x + 2 = 6 [1 mark]",
            f"Subtract 2: x = {ans} [1 mark]",
        ],
        "hints": [
            "Collect $x$ terms on the left: $1{,}5x - 0{,}5x = 1{,}0x = x$.",
            "Collect constants on the right: $6 - 2 = 4$.",
            f"$x = {ans}$.",
        ],
        "misconception_tags": ["decimal_both_sides_arithmetic_error"],
        "diagram_spec": None,
    }


def arch_45_equation_with_square_root_term(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([3, 4, 5, 6])
    ans = k ** 2
    b = rng.randint(2, 7)
    c = k + b

    return {
        "title": "Solving Equations Involving Square Roots (Radical Inversion)",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "45_equation_with_square_root_term",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$\\sqrt{{x}} + {b} = {c}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Isolate square root: $\\sqrt{{x}} = {c - b} = {k}$ [1 mark]",
            f"Square both sides: x = {k}^2 = {ans} [1 mark]",
        ],
        "hints": [
            f"Subtract {b} from both sides: $\\sqrt{{x}} = {c} - {b} = {k}$.",
            f"Square both sides to eliminate the square root: $x = {k}^2 = {ans}$.",
        ],
        "misconception_tags": ["radical_equation_squaring_error"],
        "diagram_spec": None,
    }


def arch_46_equation_with_cube_root_term(rng: random.Random) -> Dict[str, Any]:
    k = rng.choice([2, 3, 4])
    ans = k ** 3
    b = rng.randint(1, 4)
    c = k - b

    return {
        "title": "Solving Equations Involving Cube Roots",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "46_equation_with_cube_root_term",
        "difficulty": "medium",
        "question_text": (
            f"Solve for $x$:\n\n"
            f"$$\\sqrt[3]{{x}} - {b} = {c}$$"
        ),
        "correct_answer": str(ans),
        "marking_schema": [
            f"Isolate cube root: $\\sqrt[3]{{x}} = {c + b} = {k}$ [1 mark]",
            f"Cube both sides: x = {k}^3 = {ans} [1 mark]",
        ],
        "hints": [
            f"Add {b} to both sides: $\\sqrt[3]{{x}} = {c} + {b} = {k}$.",
            f"Cube both sides: $x = {k}^3 = {ans}$.",
        ],
        "misconception_tags": ["cube_root_cubing_inversion_gap"],
        "diagram_spec": None,
    }


def arch_47_geometric_area_model_rectangle_area_equation(rng: random.Random) -> Dict[str, Any]:
    w = rng.randint(3, 6)
    b = rng.randint(2, 5)
    ans = rng.randint(3, 8)
    area = w * (ans + b)

    return {
        "title": "Geometric Modelling: Area of a Rectangle Equation",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "47_geometric_area_model_rectangle_area_equation",
        "difficulty": "medium",
        "question_text": (
            f"A rectangular banner has width **{w}\\text{{ m}}** and length **$(x + {b})\\text{{ m}}$**. "
            f"Its total area is **{area}\\text{{ m}}^2**.\n\n"
            "1. Formulate an equation for the area.\n"
            "2. Solve for $x$ and determine the actual length of the banner."
        ),
        "correct_answer": f"1. {w}(x + {b}) = {area}. 2. x = {ans}; length = {ans + b} m.",
        "marking_schema": [
            f"Equation: {w}(x + {b}) = {area} [1 mark]",
            f"Solve: x = {ans}; length = {ans + b} m [1 mark]",
        ],
        "hints": [
            f"Area = width x length: ${w}(x + {b}) = {area}$.",
            f"Divide by {w}: $x + {b} = {area // w}$.",
            f"Subtract {b}: $x = {ans}$.",
            f"Length = {ans} + {b} = {ans + b} m.",
        ],
        "misconception_tags": ["rectangle_area_equation_setup_error"],
        "diagram_spec": None,
    }


def arch_48_work_rate_problem_intro(rng: random.Random) -> Dict[str, Any]:
    # Pipe A takes 6 hours, Pipe B takes 3 hours. Together: t/6 + t/3 = 1 => 3t/6 = t/2 = 1 => t = 2 hours
    t = 2
    return {
        "title": "Rate Modelling: Cooperative Work Rates Equation",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "48_work_rate_problem_intro",
        "difficulty": "hard",
        "question_text": (
            "Pipe A can fill a municipal water reservoir in **6 hours**. "
            "Pipe B can fill the same reservoir in **3 hours**.\n\n"
            "If both pipes are opened together, the time $t$ (in hours) to fill the reservoir satisfies:\n\n"
            "$$\\frac{t}{6} + \\frac{t}{3} = 1$$\n\n"
            "Solve for $t$ to determine how many hours it takes both pipes working simultaneously."
        ),
        "correct_answer": f"t = {t} hours",
        "marking_schema": [
            "Combine fractions: t/6 + 2t/6 = 3t/6 = t/2 = 1 [1 mark]",
            f"Solve for t: t = {t} hours [1 mark]",
        ],
        "hints": [
            "Find common denominator 6: $\\frac{t}{6} + \\frac{2t}{6} = \\frac{3t}{6}$.",
            "$\\frac{3t}{6} = \\frac{t}{2} = 1$.",
            f"Multiply by 2: $t = {t}$ hours.",
        ],
        "misconception_tags": ["cooperative_work_rate_equation_error"],
        "diagram_spec": None,
    }


def arch_49_water_tank_drainage_linear_equation(rng: random.Random) -> Dict[str, Any]:
    cap = 500
    rate = 25
    target = 100
    # 500 - 25t = 100 => 25t = 400 => t = 16
    t = (cap - target) // rate

    return {
        "title": "Rate Modelling: Tank Drainage Linear Equation",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "49_water_tank_drainage_linear_equation",
        "difficulty": "medium",
        "question_text": (
            f"A rainwater tank holds **{cap}\\text{{ litres}}** of water. "
            f"A drainage valve empties the tank at a constant rate of **{rate}\\text{{ litres per minute}}**.\n\n"
            f"1. Write an equation for the time $t$ (in minutes) when exactly **{target}\\text{{ litres}}** remain.\n"
            "2. Solve for $t$."
        ),
        "correct_answer": f"1. {cap} - {rate}t = {target}. 2. t = {t} minutes.",
        "marking_schema": [
            f"Equation: {cap} - {rate}t = {target} [1 mark]",
            f"Solve: {rate}t = {cap - target} => t = {t} minutes [1 mark]",
        ],
        "hints": [
            f"Water remaining = Initial volume - Drained volume = {cap} - {rate}t.",
            f"Set equal to {target}: {cap} - {rate}t = {target}.",
            f"{rate}t = {cap - target} \\implies t = {t} minutes.",
        ],
        "misconception_tags": ["rate_subtraction_depletion_error"],
        "diagram_spec": None,
    }


def arch_50_algebraic_equations_2_capstone_synthesis(rng: random.Random) -> Dict[str, Any]:
    ans = rng.randint(3, 6)
    # 3(2x - 1) = 2(x + 4) + k => 6x - 3 = 2x + 8 + k => 4x = 11 + k => k = 4*ans - 11
    k = 4 * ans - 11
    sign = "+" if k >= 0 else "-"
    abs_k = abs(k)

    return {
        "title": "Comprehensive Multi-Step Equation Synthesis Challenge",
        "topic": "Algebraic equations 2",
        "grade": 8,
        "term": 2,
        "subskill": "50_algebraic_equations_2_capstone_synthesis",
        "difficulty": "hard",
        "question_text": (
            f"Solve the linear equation completely:\n\n"
            f"$$3(2x - 1) = 2(x + 4) {sign} {abs_k}$$\n\n"
            "1. Expand brackets on both sides.\n"
            "2. Collect variable terms and solve for $x$.\n"
            "3. Verify your solution by substitution."
        ),
        "correct_answer": f"1. 6x - 3 = 2x + 8 {sign} {abs_k}. 2. x = {ans}. 3. LHS = 3(2({ans}) - 1) = {3 * (2 * ans - 1)}; RHS = 2(({ans}) + 4) {sign} {abs_k} = {3 * (2 * ans - 1)} (verified).",
        "marking_schema": [
            f"Expand: 6x - 3 = 2x + {8 + k} [1 mark]",
            f"Solve: 4x = {11 + k} => x = {ans} [1 mark]",
            "Verify by substitution [1 mark]",
        ],
        "hints": [
            f"LHS = 6x - 3.",
            f"RHS = 2x + 8 {sign} {abs_k} = 2x + {8 + k}.",
            f"Subtract 2x: 4x - 3 = {8 + k}.",
            f"Add 3: 4x = {11 + k} \\implies x = {ans}.",
        ],
        "misconception_tags": ["capstone_equation_multistep_error"],
        "diagram_spec": None,
    }


BUILDERS_26_50 = [
    arch_26_geometric_angles_quadrilateral_interior_sum,
    arch_27_age_problem_parent_and_two_children,
    arch_28_age_problem_future_years_ratio,
    arch_29_distance_speed_time_meeting_problem,
    arch_30_distance_speed_time_overtaking_problem,
    arch_31_money_coin_problem_two_denominations,
    arch_32_tickets_two_tier_pricing_equation,
    arch_33_sharing_items_in_given_ratio_equation,
    arch_34_perimeter_of_parallelogram_equation,
    arch_35_rhombus_side_length_equation,
    arch_36_fraction_equation_single_fraction_equals_binomial,
    arch_37_fraction_equation_difference_of_fractions,
    arch_38_fraction_equation_binomial_numerators,
    arch_39_fraction_equation_monomial_denominator_cancelling,
    arch_40_equation_leading_to_identity_all_real_solutions,
    arch_41_equation_leading_to_contradiction_no_solution,
    arch_42_diagnosing_bracket_expansion_error_in_equations,
    arch_43_diagnosing_variable_cancellation_fallacy,
    arch_44_equation_with_decimal_coefficients_both_sides,
    arch_45_equation_with_square_root_term,
    arch_46_equation_with_cube_root_term,
    arch_47_geometric_area_model_rectangle_area_equation,
    arch_48_work_rate_problem_intro,
    arch_49_water_tank_drainage_linear_equation,
    arch_50_algebraic_equations_2_capstone_synthesis,
]
