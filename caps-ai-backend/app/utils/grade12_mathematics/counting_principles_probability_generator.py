"""Grade 12 Mathematics — Counting Principles & Probability (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (NSC Paper 1, Questions 10 & 11: 15–20 marks).
Supports full 10-mark compound exam questions and atomic 3-mark elementary sub-drills for adaptive deconstruction.
Zero-LLM: 100% deterministic SymPy mathematics with South African comma decimals ({,}).
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade12_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    num,
    rng,
    solution_graph,
    step,
    to_latex,
)

TOPIC = "grade12_math_counting_probability"
LO = "math12_probability"


# --------------------------------------------------------------------------- #
# Sub-drill 1: elementary_factorial_calc (3 marks)
# --------------------------------------------------------------------------- #
def _build_factorial_calc(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding Sub-drill: Basic permutations n! and n! / (n-r)!."""
    n = r.randint(6, 10)
    r_val = r.randint(2, 4)

    total_perm = math.perm(n, r_val)
    denom = n - r_val

    contexts = [
        ("runners in an athletics final", "the top", "medal positions (Gold, Silver, Bronze)"),
        ("learners in a class", "a committee consisting of", "distinct executive roles (President, Secretary, Treasurer)"),
        ("photographs to be exhibited", "a row of", "selected spaces on a gallery wall"),
        ("books on a reading list", "a bookshelf with", "available slots"),
    ]
    ctx_subj, ctx_mid, ctx_end = r.choice(contexts)

    formula_latex = rf"P(n, r) = \frac{{n!}}{{(n - r)!}} = \frac{{{n}!}}{{({n} - {r_val})!}} = \frac{{{n}!}}{{{denom}!}}"
    calc_expansion = " \\times ".join(str(n - i) for i in range(r_val))

    steps = [
        step(
            from_latex=rf"P({n}; {r_val}) = \frac{{{n}!}}{{({n} - {r_val})!}}",
            to_latex_str=rf"= \frac{{{n}!}}{{{denom}!}}",
            op="apply permutation formula",
            rule="permutation definition",
        ),
        step(
            from_latex=rf"\frac{{{n}!}}{{{denom}!}}",
            to_latex_str=rf"= {calc_expansion}",
            op="cancel common factorial terms in numerator and denominator",
            rule="factorial simplification",
            common_errors=["calculated_full_factorials_prematurely", "subtraction_error_in_denominator"],
        ),
        step(
            from_latex=calc_expansion,
            to_latex_str=f"= {total_perm}",
            op="evaluate product of remaining factors",
            rule="arithmetic multiplication",
        ),
    ]

    canonical = solution_graph(
        goal=f"calculate permutations of {r_val} objects chosen from {n}",
        steps=steps,
        final_latex=str(total_perm),
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Selection of permutation formula n!/(n-r)! with n = {n} and r = {r_val}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct expansion or simplification to {calc_expansion}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct final answer: {total_perm}", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "used_combinations_instead_of_permutations", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": f"Since the order of arrangement matters, use the permutation formula $P(n, r) = \\frac{{n!}}{{(n-r)!}}$.",
        "concept": "When arranging $r$ items selected from $n$ distinct items without repetition, the first position has $n$ choices, the second has $n-1$, continuing down to $n-r+1$.",
        "breakdown": f"1. Identify $n = {n}$ and $r = {r_val}$.\n2. Compute $\\frac{{{n}!}}{{({n}-{r_val})!}} = \\frac{{{n}!}}{{{denom}!}}$.\n3. Multiply: ${calc_expansion} = {total_perm}$.",
    }

    prompt = (
        f"There are {n} {ctx_subj}. In how many different ways can {ctx_mid} "
        f"{r_val} {ctx_end} be awarded/arranged if each item/person can only be chosen once?"
    )

    return make_math_question(
        prefix="prob_fact",
        topic=TOPIC,
        subskill="elementary_factorial_calc",
        learning_objective_id=f"{LO}_factorial_permutations",
        prompt=prompt,
        prompt_latex=rf"\frac{{{n}!}}{{({n} - {r_val})!}}",
        answer_latex=str(total_perm),
        answer_sympy=sp.srepr(sp.Integer(total_perm)),
        sample_answer=f"Number of ways = {n}! / ({n} - {r_val})! = {n}! / {denom}! = {calc_expansion} = {total_perm}",
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["used_combinations_instead_of_permutations", "forgot_to_subtract_denominator", "repetition_confused"],
        keywords=["permutations", "factorials", "counting principle", "arrangements"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_factorial_calc",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Sub-drill 2: elementary_grouping_restriction (3 marks)
# --------------------------------------------------------------------------- #
def _build_grouping_restriction(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding Sub-drill: Calculating arrangements where items must sit together as a single block."""
    num_boys = r.randint(3, 5)
    num_girls = r.randint(3, 5)
    total_people = num_boys + num_girls

    # Group boys together as 1 block
    # Total units to arrange = (num_girls + 1)
    num_blocks = num_girls + 1
    blocks_perm = math.factorial(num_blocks)
    internal_perm = math.factorial(num_boys)
    total_arrangements = blocks_perm * internal_perm

    steps = [
        step(
            from_latex=rf"\text{{Treat {num_boys} boys as 1 single block}}",
            to_latex_str=rf"\text{{Number of units to arrange}} = {num_girls} \text{{ girls}} + 1 \text{{ block}} = {num_blocks}",
            op="group restricted items into a single composite entity",
            rule="block method for grouped arrangements",
        ),
        step(
            from_latex=rf"{num_blocks}! \text{{ block arrangements}}",
            to_latex_str=rf"{num_blocks}! \times {num_boys}!",
            op=f"multiply by the internal permutations of the {num_boys} boys",
            rule="multiplication principle",
            common_errors=["forgot_internal_permutation", "treated_block_as_zero_elements"],
        ),
        step(
            from_latex=rf"{blocks_perm} \times {internal_perm}",
            to_latex_str=f"{total_arrangements}",
            op="evaluate final product",
            rule="arithmetic multiplication",
        ),
    ]

    canonical = solution_graph(
        goal=f"calculate arrangements of {total_people} people where {num_boys} boys sit together",
        steps=steps,
        final_latex=str(total_arrangements),
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Treating {num_boys} boys as 1 block giving {num_blocks}! arrangements", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Accounting for internal arrangements of the boys: {num_boys}!", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct total arrangements: {num_blocks}! x {num_boys}! = {total_arrangements}", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "omitted_internal_reordering", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": f"Treat all {num_boys} boys as a single entity or 'block'. How many items are there now to arrange?",
        "concept": "The Block Method: 1. Treat the group of items that must stay together as 1 item. 2. Count arrangements of all items including the block. 3. Multiply by the arrangements within the block.",
        "breakdown": f"1. Treat the {num_boys} boys as 1 block. Total items = {num_girls} girls + 1 block = {num_blocks} items.\n2. Arrange these {num_blocks} items in {num_blocks}! = {blocks_perm} ways.\n3. Arrange the {num_boys} boys inside the block in {num_boys}! = {internal_perm} ways.\n4. Total = {num_blocks}! \\times {num_boys}! = {blocks_perm} \\times {internal_perm} = {total_arrangements}.",
    }

    prompt = (
        f"A group of {num_boys} boys and {num_girls} girls are to be seated in a straight row of {total_people} chairs. "
        f"Determine the number of different seating arrangements possible if all {num_boys} boys must sit next to each other."
    )

    return make_math_question(
        prefix="prob_grp",
        topic=TOPIC,
        subskill="elementary_grouping_restriction",
        learning_objective_id=f"{LO}_restricted_arrangements",
        prompt=prompt,
        prompt_latex=rf"({num_girls} + 1)! \times {num_boys}! = {num_blocks}! \times {num_boys}!",
        answer_latex=str(total_arrangements),
        answer_sympy=sp.srepr(sp.Integer(total_arrangements)),
        sample_answer=f"Number of arrangements = ({num_girls} + 1)! * {num_boys}! = {num_blocks}! * {num_boys}! = {blocks_perm} * {internal_perm} = {total_arrangements}",
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["omitted_internal_reordering", "confused_block_count", "added_factorials_instead_of_multiplying"],
        keywords=["block method", "restricted seating", "counting principle", "permutations", "grouping"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_grouping_restriction",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Sub-drill 3: elementary_independence_test (3 marks)
# --------------------------------------------------------------------------- #
def _build_independence_test(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding Sub-drill: Computing P(A) x P(B) and comparing against P(A and B)."""
    # Decide whether events will be independent or dependent
    is_independent = r.choice([True, False])

    # Generate probabilities using clean decimals (tenths or hundredths)
    denom_a = r.choice([2, 4, 5, 10])
    num_a = r.randint(1, denom_a - 1)
    p_a_rat = sp.Rational(num_a, denom_a)

    denom_b = r.choice([2, 4, 5, 10])
    num_b = r.randint(1, denom_b - 1)
    p_b_rat = sp.Rational(num_b, denom_b)

    prod_rat = p_a_rat * p_b_rat

    if is_independent:
        p_inter_rat = prod_rat
    else:
        # Alter the intersection slightly so P(A and B) != P(A) x P(B)
        delta = r.choice([sp.Rational(1, 20), sp.Rational(1, 25), -sp.Rational(1, 25), sp.Rational(1, 50)])
        cand = prod_rat + delta
        if 0 < cand < min(p_a_rat, p_b_rat):
            p_inter_rat = cand
        else:
            p_inter_rat = prod_rat / 2

    p_a_float = float(p_a_rat)
    p_b_float = float(p_b_rat)
    p_inter_float = float(p_inter_rat)
    prod_float = float(prod_rat)

    p_a_str = num(p_a_float, 2)
    p_b_str = num(p_b_float, 2)
    p_inter_str = num(p_inter_float, 4).rstrip("0").rstrip(",")
    prod_str = num(prod_float, 4).rstrip("0").rstrip(",")

    conclusion_word = "independent" if is_independent else "dependent (not independent)"
    comp_sym = "=" if is_independent else r"\neq"

    steps = [
        step(
            from_latex=rf"P(A) \times P(B) = {p_a_str} \times {p_b_str}",
            to_latex_str=rf"P(A) \times P(B) = {prod_str}",
            op="calculate product of individual probabilities",
            rule="product rule for independent events",
        ),
        step(
            from_latex=rf"P(A \cap B) = {p_inter_str}, \quad P(A) \times P(B) = {prod_str}",
            to_latex_str=rf"P(A \cap B) {comp_sym} P(A) \times P(B)",
            op="compare intersection probability with product",
            rule="independence criterion",
            common_errors=["confused_mutually_exclusive_with_independent", "incorrect_multiplication_of_decimals"],
        ),
        step(
            from_latex=rf"P(A \cap B) {comp_sym} P(A) \times P(B)",
            to_latex_str=rf"\therefore \text{{Events }} A \text{{ and }} B \text{{ are }} {conclusion_word}",
            op="deduce conclusion with formal mathematical reason",
            rule="mathematical justification",
        ),
    ]

    canonical = solution_graph(
        goal="test if two events are independent using probability product rule",
        steps=steps,
        final_latex=rf"\text{{Events are }} {conclusion_word} \text{{ since }} P(A \cap B) {comp_sym} P(A) \times P(B)",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Calculation of P(A) x P(B) = {p_a_str} x {p_b_str} = {prod_str}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Explicit comparison between P(A ∩ B) = {p_inter_str} and P(A) x P(B) = {prod_str}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Correct conclusion: events are {conclusion_word} with reason", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "stated_mutually_exclusive_instead_of_independent", "penalty": -1},
            {"rule": "no_reason_given_for_conclusion", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": r"Recall the definition of independent events: $A$ and $B$ are independent if and only if $P(A \cap B) = P(A) \times P(B)$.",
        "concept": "Calculate $P(A) \\times P(B)$ and compare the result to $P(A \\cap B)$. If they are equal, the events are independent; if not equal, they are dependent.",
        "breakdown": f"1. Compute $P(A) \\times P(B) = {p_a_str} \\times {p_b_str} = {prod_str}$.\n2. Note that $P(A \\cap B) = {p_inter_str}$.\n3. Since ${p_inter_str} {comp_sym} {prod_str}$, $P(A \\cap B) {comp_sym} P(A) \\times P(B)$. Therefore, events $A$ and $B$ are {conclusion_word}.",
    }

    prompt = (
        f"Two events $A$ and $B$ have probabilities $P(A) = {p_a_str}$, $P(B) = {p_b_str}$, "
        f"and $P(A \\text{{ and }} B) = {p_inter_str}$.\n\n"
        f"Determine, by means of a calculation, whether events $A$ and $B$ are independent. Give a reason for your answer."
    )

    return make_math_question(
        prefix="prob_indep",
        topic=TOPIC,
        subskill="elementary_independence_test",
        learning_objective_id=f"{LO}_independent_events",
        prompt=prompt,
        prompt_latex=rf"P(A) = {p_a_str}, \quad P(B) = {p_b_str}, \quad P(A \cap B) = {p_inter_str}",
        answer_latex=rf"P(A) \times P(B) = {prod_str} {comp_sym} P(A \cap B) \implies \text{{{conclusion_word}}}",
        answer_sympy=f"independent={is_independent}",
        sample_answer=(
            f"P(A) * P(B) = {p_a_str} * {p_b_str} = {prod_str}.\n"
            f"P(A and B) = {p_inter_str}.\n"
            f"Since P(A and B) {comp_sym} P(A) * P(B), events A and B are {conclusion_word}."
        ),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["confused_mutually_exclusive_with_independent", "added_probabilities_instead_of_multiplying", "no_reason_given"],
        keywords=["independent events", "probability", "product rule", "intersection"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_independence_test",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Compound Variation A: Seating Restrictions + 3-Event Venn Diagram (10 Marks)
# --------------------------------------------------------------------------- #
def _build_compound_seating_venn(r, difficulty: str) -> Dict[str, Any]:
    """Compound 10-mark NSC examination question:
    Part 1 (5 marks): Fundamental counting principle on seated learners with grouping restriction & probability.
    Part 2 (5 marks): 3-event Venn diagram with unknown x in intersection, equation solving, and conditional/restricted probability.
    """
    # --- Part 1: Seating Arrangement ---
    num_b = r.randint(4, 5)
    num_g = r.randint(3, 4)
    n_tot = num_b + num_g

    tot_arr = math.factorial(n_tot)
    blocks_count = num_g + 1
    restricted_arr = math.factorial(blocks_count) * math.factorial(num_b)
    prob_b_together = sp.Rational(restricted_arr, tot_arr)
    prob_b_float = float(prob_b_together)

    # --- Part 2: 3-Event Venn Diagram ---
    # Sports: Rugby (R), Soccer (S), Cricket (C)
    # Regions:
    # all three: k_all
    # R and S only: k_rs
    # R and C only: k_rc
    # S and C only: (x - k_all) where x is total who play S and C
    # only R: only_r
    # only S: (tot_s - k_rs - x)
    # only C: (tot_c - k_rc - x)
    # none: k_none
    # Total surveyed: N
    k_all = r.randint(12, 18)
    k_rs_only = r.randint(10, 16)
    k_rc_only = r.randint(8, 14)
    k_sc_only_actual = r.randint(10, 18)
    x_actual = k_sc_only_actual + k_all  # total who play S and C

    only_r = r.randint(40, 60)
    only_s_actual = r.randint(30, 50)
    only_c_actual = r.randint(25, 45)
    k_none = r.randint(8, 15)

    tot_r = only_r + k_rs_only + k_rc_only + k_all
    tot_s = only_s_actual + k_rs_only + k_sc_only_actual + k_all
    tot_c = only_c_actual + k_rc_only + k_sc_only_actual + k_all

    # Total learners N
    N_total = only_r + only_s_actual + only_c_actual + k_rs_only + k_rc_only + k_sc_only_actual + k_all + k_none

    # In question, we give:
    # tot_r, tot_s, tot_c
    # R and S: (k_rs_only + k_all)
    # R and C: (k_rc_only + k_all)
    # S and C: x
    # all three: k_all
    # none: k_none
    rs_both = k_rs_only + k_all
    rc_both = k_rc_only + k_all

    # At least two sports = k_rs_only + k_rc_only + k_sc_only_actual + k_all
    at_least_two_count = k_rs_only + k_rc_only + k_sc_only_actual + k_all
    prob_at_least_two = sp.Rational(at_least_two_count, N_total)
    prob_at_least_two_float = float(prob_at_least_two)

    venn_spec = {
        "kind": "venn_3_sets",
        "bounding_box": [-6, 6, 6, -6],
        "sets": ["Rugby (R)", "Soccer (S)", "Cricket (C)"],
        "labels": {
            "only_R": str(only_r),
            "only_S": f"{tot_s - rs_both} - (x - {k_all})",
            "only_C": f"{tot_c - rc_both} - (x - {k_all})",
            "R_and_S_only": str(k_rs_only),
            "R_and_C_only": str(k_rc_only),
            "S_and_C_only": f"x - {k_all}",
            "all_three": str(k_all),
            "outside": str(k_none),
        },
        "caption": f"Venn diagram for {N_total} Grade 12 learners participating in Rugby, Soccer, and Cricket.",
    }

    steps = [
        step(
            from_latex=rf"\text{{Total seating arrangements}} = {n_tot}!",
            to_latex_str=f"{tot_arr}",
            op="calculate total unrestricted permutations",
            rule="fundamental counting principle",
        ),
        step(
            from_latex=rf"\text{{Boys grouped together}} = ({num_g} + 1)! \times {num_b}!",
            to_latex_str=rf"{blocks_count}! \times {num_b}! = {restricted_arr}",
            op="calculate arrangements with boys grouped as a single block",
            rule="block method",
        ),
        step(
            from_latex=rf"P(\text{{all boys together}}) = \frac{{{restricted_arr}}}{{{tot_arr}}}",
            to_latex_str=rf"P = {to_latex(prob_b_together)} \approx {num(prob_b_float, 4)}",
            op="compute probability of restricted event",
            rule="classical probability definition",
        ),
        step(
            from_latex=rf"\sum \text{{all regions}} = {N_total}",
            to_latex_str=rf"{only_r} + {k_rs_only} + {k_rc_only} + {k_all} + ({tot_s - rs_both} - x + {k_all}) + ({tot_c - rc_both} - x + {k_all}) + (x - {k_all}) + {k_none} = {N_total}",
            op="set up linear equation for total surveyed learners in Venn diagram",
            rule="sum of disjoint regions in Venn diagram",
        ),
        step(
            from_latex=rf"\text{{Solving for }} x",
            to_latex_str=rf"x = {x_actual}",
            op="solve linear equation for unknown intersection x",
            rule="algebraic solution",
        ),
        step(
            from_latex=rf"P(\text{{at least two sports}}) = \frac{{{k_rs_only} + {k_rc_only} + {k_sc_only_actual} + {k_all}}}{{{N_total}}}",
            to_latex_str=rf"P = \frac{{{at_least_two_count}}}{{{N_total}}} = {to_latex(prob_at_least_two)} \approx {num(prob_at_least_two_float, 4)}",
            op="calculate probability of union of two-set intersections",
            rule="probability definition",
        ),
    ]

    canonical = solution_graph(
        goal="complete 10-mark NSC counting principles and Venn diagram probability analysis",
        steps=steps,
        final_latex=rf"\text{{Arrangements: }} {restricted_arr}; \quad x = {x_actual}; \quad P(\ge 2) = {to_latex(prob_at_least_two)}",
    )

    marking_schema = {
        "total_marks": 10,
        "marking_points": [
            {"id": "mp1", "desc": f"Part 1.1: Total arrangements {n_tot}! = {tot_arr}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Part 1.2: Recognising {blocks_count}! block arrangements and {num_b}! internal boys arrangements", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Part 1.2: Correct evaluated product {restricted_arr}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Part 1.3: Probability ratio {restricted_arr}/{tot_arr}", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Part 1.3: Simplified fraction {to_latex(prob_b_together)} or decimal {num(prob_b_float, 4)}", "marks": 1, "editable": True},
            {"id": "mp6", "desc": f"Part 2.1: Correct algebraic expressions in terms of x for Venn regions", "marks": 1, "editable": True},
            {"id": "mp7", "desc": f"Part 2.2: Equating sum of all regions to total {N_total}", "marks": 1, "editable": True},
            {"id": "mp8", "desc": f"Part 2.2: Correct solution x = {x_actual}", "marks": 1, "editable": True},
            {"id": "mp9", "desc": f"Part 2.3: Summing counts of learners playing at least two sports: {at_least_two_count}", "marks": 1, "editable": True},
            {"id": "mp10", "desc": f"Part 2.3: Final probability {to_latex(prob_at_least_two)} or {num(prob_at_least_two_float, 4)}", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "omitted_internal_reordering_of_boys", "penalty": -1},
            {"rule": "double_counted_three_set_intersection", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    prompt = (
        f"**QUESTION 10 [10 MARKS]**\n\n"
        f"**10.1** A group of {num_b} boys and {num_g} girls are to be seated in a row of {n_tot} chairs for a matric valedictory photograph.\n"
        f"  10.1.1 In how many different ways can all {n_tot} learners be seated? (1)\n"
        f"  10.1.2 In how many different ways can they be seated if all {num_b} boys must sit together? (2)\n"
        f"  10.1.3 If the seating arrangement is assigned completely at random, determine the probability that all {num_b} boys will sit together. (2)\n\n"
        f"**10.2** A survey was conducted among {N_total} Grade 12 learners to investigate participation in three school sports: Rugby ($R$), Soccer ($S$), and Cricket ($C$).\n"
        f"The survey revealed the following:\n"
        f"• {tot_r} learners play Rugby.\n"
        f"• {tot_s} learners play Soccer.\n"
        f"• {tot_c} learners play Cricket.\n"
        f"• {rs_both} learners play Rugby and Soccer.\n"
        f"• {rc_both} learners play Rugby and Cricket.\n"
        f"• $x$ learners play Soccer and Cricket.\n"
        f"• {k_all} learners play all three sports.\n"
        f"• {k_none} learners do not participate in any of these three sports.\n\n"
        f"  10.2.1 Express the number of learners who play ONLY Soccer, and ONLY Cricket, in terms of $x$. (1)\n"
        f"  10.2.2 Calculate the value of $x$. (2)\n"
        f"  10.2.3 Determine the probability that a learner chosen at random from this group participates in at least two of these sports. (2)"
    )

    hints = {
        "nudge": "For 10.1, treat the boys as a single block. For 10.2, remember that regions like 'Rugby and Soccer ONLY' require subtracting those who play all three sports.",
        "concept": "Fundamental counting principle: $n!$ for unrestricted arrangements, $(n_G + 1)! \\times n_B!$ for grouped arrangements. For the 3-event Venn diagram, the sum of all eight mutually disjoint regions equals the total surveyed ($N$).",
        "breakdown": (
            f"10.1.1: ${n_tot}! = {tot_arr}$.\n"
            f"10.1.2: Treat {num_b} boys as 1 block $\\implies ({num_g}+1)! \\times {num_b}! = {blocks_count}! \\times {num_b}! = {restricted_arr}$.\n"
            f"10.1.3: $P = \\frac{{{restricted_arr}}}{{{tot_arr}}} = {to_latex(prob_b_together)}$.\n"
            f"10.2.1: Only Soccer = ${tot_s} - {rs_both} - (x - {k_all}) = {tot_s - rs_both + k_all} - x$. Only Cricket = ${tot_c} - {rc_both} - (x - {k_all}) = {tot_c - rc_both + k_all} - x$.\n"
            f"10.2.2: Add all 8 regions and equate to {N_total} to get $x = {x_actual}$.\n"
            f"10.2.3: At least two sports = $(R \\cap S \\text{{ only}}) + (R \\cap C \\text{{ only}}) + (S \\cap C \\text{{ only}}) + (R \\cap S \\cap C) = {at_least_two_count}$. Probability = $\\frac{{{at_least_two_count}}}{{{N_total}}} = {to_latex(prob_at_least_two)}$."
        ),
    }

    return make_math_question(
        prefix="prob_cmp_venn",
        topic=TOPIC,
        subskill="counting_principles_venn_compound",
        learning_objective_id=f"{LO}_compound_exam",
        prompt=prompt,
        prompt_latex=rf"\text{{Total}} = {n_tot}!, \quad x = {x_actual}, \quad P(\ge 2) = {to_latex(prob_at_least_two)}",
        answer_latex=rf"10.1.1:\ {tot_arr};\ 10.1.2:\ {restricted_arr};\ 10.1.3:\ {to_latex(prob_b_together)};\ 10.2.2:\ x = {x_actual};\ 10.2.3:\ P = {to_latex(prob_at_least_two)}",
        answer_sympy=f"arrangements={restricted_arr}, x={x_actual}, prob={prob_at_least_two}",
        sample_answer=(
            f"10.1.1 Total ways = {n_tot}! = {tot_arr}\n"
            f"10.1.2 Boys together = ({num_g}+1)! * {num_b}! = {blocks_count}! * {num_b}! = {restricted_arr}\n"
            f"10.1.3 P(boys together) = {restricted_arr} / {tot_arr} = {to_latex(prob_b_together)} ({num(prob_b_float, 4)})\n"
            f"10.2.1 Only Soccer = {tot_s - rs_both + k_all} - x; Only Cricket = {tot_c - rc_both + k_all} - x\n"
            f"10.2.2 Sum = {N_total} => x = {x_actual}\n"
            f"10.2.3 P(at least 2 sports) = {at_least_two_count} / {N_total} = {to_latex(prob_at_least_two)} ({num(prob_at_least_two_float, 4)})"
        ),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["omitted_internal_reordering_of_boys", "double_counted_three_set_intersection", "confused_union_with_intersection"],
        keywords=["permutations", "block method", "Venn diagram", "3 sets", "probability", "NSC Paper 1"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=15,
        mode="compound",
        difficulty=difficulty,
        diagram_spec=venn_spec,
    )


# --------------------------------------------------------------------------- #
# Compound Variation B: Digit Codes Permutations & Independence Testing (10 Marks)
# --------------------------------------------------------------------------- #
def _build_compound_digits_independence(r, difficulty: str) -> Dict[str, Any]:
    """Compound 10-mark NSC examination question:
    Part 1 (6 marks): Digit permutations with and without repetition, restricted conditions (primes & even digits), probability.
    Part 2 (4 marks): Two-event probability: addition rule, testing mutually exclusive vs independent events.
    """
    code_len = 6
    total_digits = 10  # 0 to 9

    # 1.1 Repetition allowed
    rep_allowed = total_digits ** code_len  # 1,000,000

    # 1.2 No repetition allowed, starts with prime digit and ends with even digit
    # Digits: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    # Primes: {2, 3, 5, 7} (4 primes)
    # Evens: {0, 2, 4, 6, 8} (5 evens)
    # Notice '2' is both prime and even!
    # Case 1: Starts with '2' (1 choice).
    # Last digit: chosen from remaining 4 evens {0, 4, 6, 8} (4 choices).
    # Remaining 4 positions: chosen from remaining 8 digits: P(8, 4) = 8*7*6*5 = 1680.
    # Total Case 1 = 1 * 4 * 1680 = 6720.
    #
    # Case 2: Starts with prime {3, 5, 7} (3 choices).
    # Last digit: chosen from all 5 evens {0, 2, 4, 6, 8} (5 choices).
    # Remaining 4 positions: chosen from remaining 8 digits: P(8, 4) = 1680.
    # Total Case 2 = 3 * 5 * 1680 = 25200.
    #
    # Total restricted codes = 6720 + 25200 = 31920.
    perm_middle = 8 * 7 * 6 * 5  # 1680
    case1 = 1 * 4 * perm_middle
    case2 = 3 * 5 * perm_middle
    total_restricted_codes = case1 + case2

    # 1.3 Total codes without repetition
    tot_no_rep = math.perm(total_digits, code_len)  # 10*9*8*7*6*5 = 151200
    prob_restricted = sp.Rational(total_restricted_codes, tot_no_rep)  # 31920 / 151200 = 19 / 90
    prob_restr_float = float(prob_restricted)

    # --- Part 2: Independence vs Mutually Exclusive ---
    # Choose clean values
    p_a_val = r.choice([0.6, 0.7, 0.5])
    p_b_val = r.choice([0.4, 0.3, 0.5])
    is_indep = r.choice([True, False])

    prod_val = round(p_a_val * p_b_val, 4)
    if is_indep:
        p_inter_val = prod_val
    else:
        p_inter_val = round(prod_val - 0.08, 4) if prod_val > 0.15 else round(prod_val + 0.08, 4)

    # P(A or B) = P(A) + P(B) - P(A and B)
    p_union_val = round(p_a_val + p_b_val - p_inter_val, 4)

    p_a_str = num(p_a_val, 2)
    p_b_str = num(p_b_val, 2)
    p_inter_str = num(p_inter_val, 4).rstrip("0").rstrip(",")
    p_union_str = num(p_union_val, 4).rstrip("0").rstrip(",")
    prod_str = num(prod_val, 4).rstrip("0").rstrip(",")

    indep_conclusion = "independent" if is_indep else "dependent (not independent)"
    indep_comp = "=" if is_indep else r"\neq"

    steps = [
        step(
            from_latex=rf"\text{{Codes with repetition}} = 10^{{{code_len}}}",
            to_latex_str=f"{rep_allowed}",
            op="evaluate digits choice with replacement",
            rule="multiplication principle with repetition",
        ),
        step(
            from_latex=rf"\text{{Case 1: First digit is }} 2; \quad \text{{Case 2: First digit in }} \{{3; 5; 7\}}",
            to_latex_str=rf"\text{{Case 1}} = 1 \times 4 \times P(8; 4) = {case1}, \quad \text{{Case 2}} = 3 \times 5 \times P(8; 4) = {case2}",
            op="partition restricted counting by whether first digit is 2",
            rule="addition principle on disjoint cases",
        ),
        step(
            from_latex=rf"\text{{Total restricted}} = {case1} + {case2}",
            to_latex_str=f"{total_restricted_codes}",
            op="sum restricted permutations across disjoint cases",
            rule="addition principle",
        ),
        step(
            from_latex=rf"P(\text{{restricted code}}) = \frac{{{total_restricted_codes}}}{{P(10; {code_len})}} = \frac{{{total_restricted_codes}}}{{{tot_no_rep}}}",
            to_latex_str=rf"P = {to_latex(prob_restricted)} \approx {num(prob_restr_float, 4)}",
            op="calculate probability among all non-repeated codes",
            rule="probability definition",
        ),
        step(
            from_latex=rf"P(A \text{{ or }} B) = P(A) + P(B) - P(A \text{{ and }} B)",
            to_latex_str=rf"P(A \text{{ and }} B) = {p_a_str} + {p_b_str} - {p_union_str} = {p_inter_str}",
            op="solve addition rule for intersection probability",
            rule="addition rule of probability",
        ),
        step(
            from_latex=rf"P(A \cap B) = {p_inter_str} \neq 0",
            to_latex_str=rf"\therefore \text{{Events }} A \text{{ and }} B \text{{ are NOT mutually exclusive}}",
            op="test mutual exclusivity condition",
            rule="mutually exclusive test",
        ),
        step(
            from_latex=rf"P(A) \times P(B) = {p_a_str} \times {p_b_str} = {prod_str}, \quad P(A \cap B) = {p_inter_str}",
            to_latex_str=rf"P(A \cap B) {indep_comp} P(A) \times P(B) \implies \text{{Events are }} {indep_conclusion}",
            op="test independence condition",
            rule="independence test",
        ),
    ]

    canonical = solution_graph(
        goal="complete 10-mark digit permutations and probability independence verification",
        steps=steps,
        final_latex=rf"\text{{Restricted codes: }} {total_restricted_codes}; \quad P(A \cap B) = {p_inter_str}; \quad \text{{{indep_conclusion}}}",
    )

    marking_schema = {
        "total_marks": 10,
        "marking_points": [
            {"id": "mp1", "desc": f"Part 1.1: 10^{code_len} = {rep_allowed} codes", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Part 1.2: Identification of overlap digit 2 and setting up Case 1 (first digit 2) and Case 2 (first digit 3, 5, 7)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Part 1.2: Calculating middle digits P(8, 4) = {perm_middle}", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Part 1.2: Final restricted count: {case1} + {case2} = {total_restricted_codes}", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Part 1.3: Total without repetition P(10, 6) = {tot_no_rep}", "marks": 1, "editable": True},
            {"id": "mp6", "desc": f"Part 1.3: Probability ratio {to_latex(prob_restricted)} ({num(prob_restr_float, 4)})", "marks": 1, "editable": True},
            {"id": "mp7", "desc": f"Part 2.1: Substitution into addition rule to find P(A and B) = {p_inter_str}", "marks": 1, "editable": True},
            {"id": "mp8", "desc": f"Part 2.2: Correct test for mutually exclusive: P(A and B) != 0 therefore NOT mutually exclusive", "marks": 1, "editable": True},
            {"id": "mp9", "desc": f"Part 2.3: Calculating product P(A) x P(B) = {prod_str}", "marks": 1, "editable": True},
            {"id": "mp10", "desc": f"Part 2.3: Comparison and deduction that events are {indep_conclusion}", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "failed_to_separate_prime_even_digit_2", "penalty": -1},
            {"rule": "confused_mutually_exclusive_with_independent", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    prompt = (
        f"**QUESTION 11 [10 MARKS]**\n\n"
        f"**11.1** A security gate code consists of {code_len} digits chosen from the digits 0 to 9.\n"
        f"  11.1.1 How many different {code_len}-digit codes can be formed if digits may be repeated? (1)\n"
        f"  11.1.2 How many different {code_len}-digit codes can be formed if repetition of digits is NOT allowed, the code must start with a prime digit, and must end with an even digit? (3)\n"
        f"  11.1.3 If a code is randomly generated from all possible {code_len}-digit codes with NO repetition, calculate the probability that the code begins with a prime digit and ends with an even digit. (2)\n\n"
        f"**11.2** Two events, $A$ and $B$, have probabilities $P(A) = {p_a_str}$, $P(B) = {p_b_str}$, and $P(A \\text{{ or }} B) = {p_union_str}$.\n"
        f"  11.2.1 Calculate $P(A \\text{{ and }} B)$. (1)\n"
        f"  11.2.2 State, with a mathematical reason, whether events $A$ and $B$ are mutually exclusive. (1)\n"
        f"  11.2.3 Determine, with necessary calculations, whether events $A$ and $B$ are independent. (2)"
    )

    hints = {
        "nudge": "In 11.1.2, note that 2 is BOTH a prime number and an even number, so you must split your calculation into two cases: when the code starts with 2, and when it starts with another prime (3, 5, or 7).",
        "concept": "For mutually exclusive events, $P(A \\cap B) = 0$. For independent events, $P(A \\cap B) = P(A) \\times P(B)$.",
        "breakdown": (
            f"11.1.1: $10^{{{code_len}}} = {rep_allowed}$.\n"
            f"11.1.2: Case 1 (starts with 2): 1 choice for first, 4 choices for last (0, 4, 6, 8), $P(8, 4) = {perm_middle}$ for middle. Total = $1 \\times 4 \\times {perm_middle} = {case1}$.\n"
            f"Case 2 (starts with 3, 5, 7): 3 choices for first, 5 choices for last (0, 2, 4, 6, 8), $P(8, 4) = {perm_middle}$ for middle. Total = $3 \\times 5 \\times {perm_middle} = {case2}$.\n"
            f"Total = ${case1} + {case2} = {total_restricted_codes}$.\n"
            f"11.1.3: $P = \\frac{{{total_restricted_codes}}}{{P(10, 6)}} = \\frac{{{total_restricted_codes}}}{{{tot_no_rep}}} = {to_latex(prob_restricted)}$.\n"
            f"11.2.1: $P(A \\cap B) = P(A) + P(B) - P(A \\cup B) = {p_a_str} + {p_b_str} - {p_union_str} = {p_inter_str}$.\n"
            f"11.2.2: Since $P(A \\cap B) = {p_inter_str} \\neq 0$, the events are NOT mutually exclusive.\n"
            f"11.2.3: $P(A) \\times P(B) = {p_a_str} \\times {p_b_str} = {prod_str}$. Since $P(A \\cap B) = {p_inter_str} {indep_comp} {prod_str}$, the events are {indep_conclusion}."
        ),
    }

    return make_math_question(
        prefix="prob_cmp_digits",
        topic=TOPIC,
        subskill="counting_principles_digits_compound",
        learning_objective_id=f"{LO}_compound_exam",
        prompt=prompt,
        prompt_latex=rf"10^{{{code_len}}}, \quad \text{{Restricted}} = {total_restricted_codes}, \quad P(A \cap B) = {p_inter_str}",
        answer_latex=rf"11.1.1:\ {rep_allowed};\ 11.1.2:\ {total_restricted_codes};\ 11.1.3:\ {to_latex(prob_restricted)};\ 11.2.1:\ {p_inter_str};\ 11.2.2:\ \text{{No}};\ 11.2.3:\ \text{{{indep_conclusion}}}",
        answer_sympy=f"rep={rep_allowed}, restricted={total_restricted_codes}, p_inter={p_inter_val}, indep={is_indep}",
        sample_answer=(
            f"11.1.1 Repetition allowed: 10^{code_len} = {rep_allowed}\n"
            f"11.1.2 Case 1 (starts with 2): 1 * 4 * P(8, 4) = {case1}\n"
            f"       Case 2 (starts with 3, 5, 7): 3 * 5 * P(8, 4) = {case2}\n"
            f"       Total = {case1} + {case2} = {total_restricted_codes}\n"
            f"11.1.3 Probability = {total_restricted_codes} / P(10, 6) = {total_restricted_codes} / {tot_no_rep} = {to_latex(prob_restricted)}\n"
            f"11.2.1 P(A and B) = {p_a_str} + {p_b_str} - {p_union_str} = {p_inter_str}\n"
            f"11.2.2 Since P(A and B) = {p_inter_str} != 0, events A and B are NOT mutually exclusive.\n"
            f"11.2.3 P(A) * P(B) = {p_a_str} * {p_b_str} = {prod_str}. Since P(A and B) {indep_comp} P(A) * P(B), events are {indep_conclusion}."
        ),
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["failed_to_separate_prime_even_digit_2", "confused_mutually_exclusive_with_independent", "added_probabilities_instead_of_multiplying"],
        keywords=["permutations", "digit codes", "prime digits", "independent events", "mutually exclusive", "NSC Paper 1"],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=15,
        mode="compound",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Compound Dispatcher
# --------------------------------------------------------------------------- #
def _build_compound(r, difficulty: str) -> Dict[str, Any]:
    """Compound dispatcher: alternates between Seating Arrangements + Venn Diagram
    and Digit Permutations + Independence Testing."""
    if r.random() < 0.5:
        return _build_compound_seating_venn(r, difficulty)
    return _build_compound_digits_independence(r, difficulty)


# --------------------------------------------------------------------------- #
# Public Generator Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound,
    "compound_seating_venn": _build_compound_seating_venn,
    "compound_digits_independence": _build_compound_digits_independence,
    "elementary_factorial_calc": _build_factorial_calc,
    "factorial_permutations": _build_factorial_calc,
    "elementary_grouping_restriction": _build_grouping_restriction,
    "grouping_restriction": _build_grouping_restriction,
    "elementary_independence_test": _build_independence_test,
    "independence_test": _build_independence_test,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Counting Principles & Probability questions."""
    base_seed = 42 if seed is None else int(seed)
    target = subskill if (subskill and subskill in BUILDERS) else mode
    builder = BUILDERS.get(target, BUILDERS.get(mode, _build_compound))

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
