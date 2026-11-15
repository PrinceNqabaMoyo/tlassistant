"""Grade 10 Mathematics — Term 1 — Number Patterns: Archetypes 26 to 50.

Ground truth: curriculum_docs/Mathematics_Gr10/Term 1/3 Patterns and Sequences .md
Zero LLM, 100% deterministic SymPy-backed questions with step-by-step solutions.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
import sympy as sp

from app.utils.grade10_mathematics._math_common import (
    make_mcq,
    make_short,
    make_steps,
    nonzero,
    num,
    solution,
    step,
    to_latex,
    to_latex_safe,
    with_metadata,
)

TOPIC = "grade10_math_patterns_sequences"
LO = "math10_patterns_sequences"
n = sp.Symbol("n")
k_sym = sp.Symbol("k")


def _term_val(a: int, d: int, pos: int) -> int:
    return a + (pos - 1) * d


def _add_pillars(q: Dict[str, Any], subskill_name: str, duration: int = 3, weight: int = 15) -> Dict[str, Any]:
    marks = int(q.get("marks", 2))
    schema = [
        {"criterion": "Application of arithmetic sequence properties / modeling", "marks": max(1, marks - 1)},
        {"criterion": "Accurate calculation / formula / classification", "marks": 1},
    ]
    q.update({
        "term": 1,
        "caps_weight_percent": weight,
        "suggested_duration_mins": duration,
        "mode": f"elementary_{subskill_name}",
        "marking_schema": schema,
    })
    return q


# --------------------------------------------------------------------------- #
# 26_fence_post_and_rail_pattern
# --------------------------------------------------------------------------- #
def _build_26_fence_post_and_rail_pattern(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    rails_per_section = r.choice([2, 3])
    sections = r.choice([10, 15, 20, 25])
    posts_needed = sections + 1
    rails_needed = rails_per_section * sections

    q = make_short(
        prefix=TOPIC,
        prompt_latex=(
            f"\\text{{A wooden fence has }} {rails_per_section} \\text{{ horizontal rails per section. "
            f"Each section requires vertical posts at its ends, so }} n \\text{{ sections require }} n + 1 "
            f"\\text{{ posts. How many posts are needed for a fence with }} {sections} \\text{{ sections?}}"
        ),
        answer_expr=sp.Integer(posts_needed),
        answer_mode="value",
        answer_latex=str(posts_needed),
        marks=1,
        explanation=f"Number of posts = $\\text{{sections}} + 1 = {sections} + 1 = {posts_needed}$.",
        hint="The number of posts is always one more than the number of sections.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="26_fence_post_and_rail_pattern",
        learning_objective_id=f"{LO}.26_fence_pattern",
        misconception_tags=["off_by_one_posts", "multiplies_sections_by_two"],
        diagnostic_tags=["visual_patterns", "fence_model"],
        keywords=["fence posts", "sections", "linear model"],
    )
    return _add_pillars(q, "26_fence_post_and_rail_pattern", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 27_tile_border_paving_pattern
# --------------------------------------------------------------------------- #
def _build_27_tile_border_paving_pattern(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_pond = r.choice([5, 8, 10, 12])
    tiles = 4 * n_pond + 4

    sol = solution(
        goal="calculate border tiles around square pond",
        chain_type="expression",
        var="n",
        steps=[
            step(from_expr="T_n = (n + 2)^2 - n^2", to_expr="T_n = 4n + 4", op="expand area difference", rule="border formula"),
            step(from_expr=f"T_{{{n_pond}}} = 4({n_pond}) + 4", to_expr=f"T_{{{n_pond}}} = {tiles}", op="substitute pond side length", rule="evaluation"),
        ],
        final_expr=sp.Integer(tiles),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A border of unit square paving tiles surrounds an }} {n_pond} \\times {n_pond} \\text{{ garden. How many border tiles are needed?}}",
        answer_expr=sp.Integer(tiles),
        answer_mode="value",
        answer_latex=str(tiles),
        marks=2,
        canonical_solution=sol,
        explanation=f"A border of width 1 around an $n \\times n$ square requires $(n + 2)^2 - n^2 = 4n + 4$ tiles. For $n = {n_pond}$: $4({n_pond}) + 4 = {tiles}$.",
        hint="Consider the 4 sides of length n plus the 4 corner tiles: 4n + 4.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="27_tile_border_paving_pattern",
        learning_objective_id=f"{LO}.27_tile_border",
        misconception_tags=["forgets_the_4_corners", "calculates_perimeter_only"],
        diagnostic_tags=["visual_patterns", "paving_border"],
        keywords=["paving tiles", "border pattern", "4n + 4"],
    )
    return _add_pillars(q, "27_tile_border_paving_pattern", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 28_staircase_blocks_linear_difference
# --------------------------------------------------------------------------- #
def _build_28_staircase_blocks_linear_difference(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    step_height = r.randint(2, 5)
    base_height = r.randint(3, 8)
    step_num = r.choice([10, 15, 20])
    h_ans = base_height + (step_num - 1) * step_height

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A staircase starts at }} {base_height}\\text{{ cm and increases by }} {step_height}\\text{{ cm with each step. Find the height at step }} {step_num}.",
        answer_expr=sp.Integer(h_ans),
        answer_mode="value",
        answer_latex=str(h_ans),
        marks=2,
        explanation=f"$H(n) = a + (n - 1)d = {base_height} + ({step_num} - 1)({step_height}) = {h_ans}$ cm.",
        hint="Use the linear formula H_n = a + (n - 1)d.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="28_staircase_blocks_linear_difference",
        learning_objective_id=f"{LO}.28_staircase_blocks",
        misconception_tags=["multiplies_step_by_step_height_directly", "off_by_one_step"],
        diagnostic_tags=["sequences", "linear_growth"],
        keywords=["staircase", "height", "arithmetic progression"],
    )
    return _add_pillars(q, "28_staircase_blocks_linear_difference", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 29_dots_geometric_grid_pattern
# --------------------------------------------------------------------------- #
def _build_29_dots_geometric_grid_pattern(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    grid_size = r.choice([8, 12, 16, 20])
    ans_dots = 4 * (grid_size - 1)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Dots are arranged along the perimeter of a square grid of size }} {grid_size} \\times {grid_size}. \\text{{ How many dots lie on the boundary?}}",
        answer_expr=sp.Integer(ans_dots),
        answer_mode="value",
        answer_latex=str(ans_dots),
        marks=2,
        explanation=f"A square of side $n$ has $4(n - 1)$ dots on its boundary (accounting for shared corners). For $n = {grid_size}$: $4({grid_size} - 1) = {ans_dots}$.",
        hint="Each of the 4 sides has n dots, but the 4 corner dots are shared: 4n - 4.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="29_dots_geometric_grid_pattern",
        learning_objective_id=f"{LO}.29_perimeter_dots",
        misconception_tags=["double_counts_corners", "calculates_area_of_grid"],
        diagnostic_tags=["visual_patterns", "dot_patterns"],
        keywords=["dots", "perimeter", "grid"],
    )
    return _add_pillars(q, "29_dots_geometric_grid_pattern", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 30_word_problem_constant_rate_savings
# --------------------------------------------------------------------------- #
def _build_30_word_problem_constant_rate_savings(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    init_savings = r.randint(100, 300)
    weekly_deposit = r.randint(25, 75)
    weeks = r.choice([8, 12, 16, 20])
    total = init_savings + weeks * weekly_deposit

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A learner has R{init_savings} in savings and adds R{weekly_deposit} every week. What is the total savings after }} {weeks} \\text{{ weeks?}}",
        answer_expr=sp.Integer(total),
        answer_mode="value",
        answer_latex=f"R{total}",
        marks=2,
        explanation=f"Total savings = $\\text{{initial}} + \\text{{weeks}} \\times \\text{{deposit}} = R{init_savings} + {weeks} \\times R{weekly_deposit} = R{total}$.",
        hint="Initial amount plus (number of weeks * weekly deposit).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="30_word_problem_constant_rate_savings",
        learning_objective_id=f"{LO}.30_savings_word_problem",
        misconception_tags=["omits_initial_deposit", "multiplication_error"],
        diagnostic_tags=["applications", "word_problems"],
        keywords=["savings", "linear growth", "word problem"],
    )
    return _add_pillars(q, "30_word_problem_constant_rate_savings", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 31_word_problem_constant_rate_depletion
# --------------------------------------------------------------------------- #
def _build_31_word_problem_constant_rate_depletion(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    init_vol = r.randint(3000, 6000)
    drain_rate = r.randint(120, 250)
    hours = r.randint(6, 12)
    rem_vol = init_vol - drain_rate * hours

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A water reservoir starts with }} {init_vol}\\text{{ litres of water and is drained at a constant rate of }} {drain_rate}\\text{{ litres/hour. Find the volume remaining after }} {hours} \\text{{ hours.}}",
        answer_expr=sp.Integer(rem_vol),
        answer_mode="value",
        answer_latex=str(rem_vol),
        marks=2,
        explanation=f"Remaining volume = ${init_vol} - {drain_rate} \\times {hours} = {rem_vol}$ litres.",
        hint="Subtract the drained amount (rate * hours) from the initial volume.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="31_word_problem_constant_rate_depletion",
        learning_objective_id=f"{LO}.31_depletion_word_problem",
        misconception_tags=["adds_rate_instead_of_subtracting", "arithmetic_error"],
        diagnostic_tags=["applications", "depletion"],
        keywords=["reservoir", "depletion", "constant rate"],
    )
    return _add_pillars(q, "31_word_problem_constant_rate_depletion", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 32_word_problem_growing_plant_height
# --------------------------------------------------------------------------- #
def _build_32_word_problem_growing_plant_height(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    h0 = r.randint(8, 20)
    weekly_cm = r.randint(2, 6)
    target_h = h0 + weekly_cm * r.randint(6, 14)
    weeks_ans = (target_h - h0) // weekly_cm

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{A plant is currently }} {h0}\\text{{ cm tall and grows by }} {weekly_cm}\\text{{ cm each week. After how many weeks will it reach a height of }} {target_h}\\text{{ cm?}}",
        answer_expr=sp.Integer(weeks_ans),
        answer_mode="value",
        answer_latex=str(weeks_ans),
        marks=2,
        explanation=f"Set ${h0} + {weekly_cm}w = {target_h} \\implies {weekly_cm}w = {target_h - h0} \\implies w = {weeks_ans}$ weeks.",
        hint="Subtract initial height from target height and divide by the weekly growth rate.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="32_word_problem_growing_plant_height",
        learning_objective_id=f"{LO}.32_plant_growth",
        misconception_tags=["divides_target_height_directly", "off_by_one_week"],
        diagnostic_tags=["applications", "plant_growth"],
        keywords=["plant growth", "rate of change", "weeks"],
    )
    return _add_pillars(q, "32_word_problem_growing_plant_height", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 33_find_terms_with_subscript_operations
# --------------------------------------------------------------------------- #
def _build_33_find_terms_with_subscript_operations(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    d = r.randint(3, 8)
    c_val = nonzero(r, -9, 9)
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{If the general term of a sequence is }} T_n = {d}n {'+' if c_val >= 0 else ''} {c_val}, \\text{{ evaluate }} T_{{n+1}} - T_n.",
        answer_expr=sp.Integer(d),
        answer_mode="value",
        answer_latex=str(d),
        marks=2,
        explanation=f"$T_{{n+1}} - T_n$ represents the common difference $d$ of an arithmetic sequence. For $T_n = {d}n {'+' if c_val >= 0 else ''} {c_val}$, $d = {d}$.",
        hint="T_(n+1) - T_n is the definition of the common difference d.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="33_find_terms_with_subscript_operations",
        learning_objective_id=f"{LO}.33_subscript_operations",
        misconception_tags=["attempts_algebraic_expansion_with_errors", "thinks_difference_depends_on_n"],
        diagnostic_tags=["sequences", "subscript_algebra"],
        keywords=["T_(n+1) - T_n", "common difference", "algebraic"],
    )
    return _add_pillars(q, "33_find_terms_with_subscript_operations", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 34_algebraic_linear_sequence_with_powers
# --------------------------------------------------------------------------- #
def _build_34_algebraic_linear_sequence_with_powers(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    var_sym = sp.Symbol("x")
    d_num = r.randint(3, 7)
    k_init = r.randint(1, 5)
    t1 = var_sym + k_init
    t2 = var_sym + k_init + d_num
    t3 = var_sym + k_init + 2 * d_num
    prompt = f"{to_latex(t1)};\\; {to_latex(t2)};\\; {to_latex(t3)}; \\ldots"

    sol = solution(
        goal="find common difference of algebraic sequence",
        chain_type="equation",
        var="d",
        steps=[
            step(from_expr="d = T_2 - T_1",
                 to_expr=f"d = ({to_latex(t2)}) - ({to_latex(t1)}) = {d_num}",
                 op="subtract terms", rule="d = T_2 - T_1"),
        ],
        final_expr=sp.Integer(d_num),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the common difference }} d \\text{{ for the sequence: }} {prompt}",
        answer_expr=sp.Integer(d_num),
        answer_mode="value",
        answer_latex=str(d_num),
        marks=1,
        canonical_solution=sol,
        explanation=f"$d = T_2 - T_1 = ({to_latex(t2)}) - ({to_latex(t1)}) = {d_num}$. The variable $x$ cancels out.",
        hint="Subtract the first term from the second term; the variable x will cancel out.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="34_algebraic_linear_sequence_with_powers",
        learning_objective_id=f"{LO}.34_alg_linear_diff",
        misconception_tags=["retains_x_in_difference", "sign_error_subtracting_binomial"],
        diagnostic_tags=["sequences", "algebraic_terms"],
        keywords=["algebraic sequence", "common difference", "cancel x"],
    )
    return _add_pillars(q, "34_algebraic_linear_sequence_with_powers", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 35_sequence_with_alternating_signs_linear_magnitude
# --------------------------------------------------------------------------- #
def _build_35_sequence_with_alternating_signs_linear_magnitude(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    d_mag = r.randint(2, 6)
    seq = [(-1)**i * (d_mag * i) for i in range(1, 5)]
    seq_str = "; ".join(str(v) for v in seq)

    q = make_mcq(
        prefix=TOPIC,
        prompt=f"Is the sequence ${seq_str}; \\ldots$ an arithmetic (linear) sequence?",
        options=[
            "No, because the consecutive differences alternate in sign and are not constant.",
            f"Yes, because the absolute value of the terms increases by {d_mag}.",
            f"Yes, because all terms are multiples of {d_mag}.",
            "No, because odd numbers cannot form a sequence.",
        ],
        correct_index=0,
        explanation=f"Calculating consecutive differences: $T_2 - T_1 = {seq[1]} - ({seq[0]}) = {seq[1] - seq[0]}$ while $T_3 - T_2 = {seq[2]} - {seq[1]} = {seq[2] - seq[1]}$. Since the difference is not constant, the sequence is NOT arithmetic.",
        marks=1,
        hint="Calculate the actual differences T_2 - T_1 and T_3 - T_2 including their negative signs.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="35_sequence_with_alternating_signs_linear_magnitude",
        learning_objective_id=f"{LO}.35_alternating_signs",
        misconception_tags=["ignores_alternating_signs", "claims_arithmetic_due_to_magnitudes"],
        diagnostic_tags=["sequences", "alternating_signs"],
        keywords=["alternating signs", "not arithmetic", "common difference"],
    )
    return _add_pillars(q, "35_sequence_with_alternating_signs_linear_magnitude", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 36_odd_numbers_sequence_properties
# --------------------------------------------------------------------------- #
def _build_36_odd_numbers_sequence_properties(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k_val = r.randint(30, 80)
    ans_val = 2 * k_val - 1

    sol = solution(
        goal=f"find the {k_val}th odd positive integer",
        chain_type="equation",
        var="n",
        steps=[
            step(from_expr="T_n = 2n - 1", to_expr=f"T_{{{k_val}}} = 2({k_val}) - 1", op="substitute into odd number formula", rule="odd formula"),
            step(from_expr=f"T_{{{k_val}}} = {2 * k_val} - 1", to_expr=f"T_{{{k_val}}} = {ans_val}", op="evaluate", rule="arithmetic"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{What is the }} {k_val}\\text{{th positive odd integer?}}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=1,
        canonical_solution=sol,
        explanation=f"The sequence of odd numbers is $1; 3; 5; \\ldots$ with general term $T_n = 2n - 1$. For $n = {k_val}$, $T_{{{k_val}}} = 2({k_val}) - 1 = {ans_val}$.",
        hint="Use the formula for odd integers: T_n = 2n - 1.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="36_odd_numbers_sequence_properties",
        learning_objective_id=f"{LO}.36_odd_numbers",
        misconception_tags=["uses_2n_instead_of_2n_minus_one", "off_by_one_odd"],
        diagnostic_tags=["sequences", "odd_numbers"],
        keywords=["odd numbers", "2n - 1", "kth odd number"],
    )
    return _add_pillars(q, "36_odd_numbers_sequence_properties", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 37_even_numbers_sequence_properties
# --------------------------------------------------------------------------- #
def _build_37_even_numbers_sequence_properties(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k_val = r.randint(30, 80)
    ans_val = 2 * k_val

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{What is the }} {k_val}\\text{{th positive even integer?}}",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=1,
        explanation=f"The sequence of even positive integers is $2; 4; 6; \\ldots$ with $T_n = 2n$. For $n = {k_val}$, $T_{{{k_val}}} = 2({k_val}) = {ans_val}$.",
        hint="The nth even number is given by 2n.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="37_even_numbers_sequence_properties",
        learning_objective_id=f"{LO}.37_even_numbers",
        misconception_tags=["uses_2n_plus_two", "confuses_even_and_odd_formula"],
        diagnostic_tags=["sequences", "even_numbers"],
        keywords=["even numbers", "2n", "kth even number"],
    )
    return _add_pillars(q, "37_even_numbers_sequence_properties", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 38_multiples_of_k_sequence
# --------------------------------------------------------------------------- #
def _build_38_multiples_of_k_sequence(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = r.choice([4, 6, 7, 8, 9])
    pos = r.randint(15, 40)
    ans_val = k * pos

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the }} {pos}\\text{{th positive multiple of }} {k}.",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=1,
        explanation=f"The sequence of multiples of {k} is ${k}; {2*k}; {3*k}; \\ldots$ with $T_n = {k}n$. For $n = {pos}$, $T_{{{pos}}} = {k} \\times {pos} = {ans_val}$.",
        hint=f"Multiply {k} by {pos}.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="38_multiples_of_k_sequence",
        learning_objective_id=f"{LO}.38_multiples_of_k",
        misconception_tags=["adds_instead_of_multiplying", "off_by_one_multiple"],
        diagnostic_tags=["sequences", "multiples"],
        keywords=["multiples", "k * n", "arithmetic pattern"],
    )
    return _add_pillars(q, "38_multiples_of_k_sequence", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 39_count_multiples_between_two_numbers
# --------------------------------------------------------------------------- #
def _build_39_count_multiples_between_two_numbers(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    k = r.choice([3, 4, 5, 6, 7])
    start = r.randint(15, 30)
    end = r.randint(120, 200)
    first_mult = ((start + k - 1) // k) * k
    last_mult = (end // k) * k
    count = (last_mult - first_mult) // k + 1

    sol = solution(
        goal="count multiples of k in interval",
        chain_type="equation",
        var="n",
        steps=[
            step(from_expr=f"T_1 = {first_mult}, \\quad T_n = {last_mult}",
                 to_expr=f"{first_mult} + (n - 1)({k}) = {last_mult}",
                 op="find first and last multiples and set arithmetic formula", rule="counting multiples"),
            step(from_expr=f"(n - 1)({k}) = {last_mult - first_mult}",
                 to_expr=f"n = {count}",
                 op="solve for n", rule="linear equation"),
        ],
        final_expr=sp.Integer(count),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{How many multiples of }} {k} \\text{{ lie between }} {start} \\text{{ and }} {end} \\text{{ (inclusive)?}}",
        answer_expr=sp.Integer(count),
        answer_mode="value",
        answer_latex=str(count),
        marks=2,
        canonical_solution=sol,
        explanation=f"The first multiple is {first_mult} and the last multiple is {last_mult}. Total multiples = $\\dfrac{{{last_mult} - {first_mult}}}{{{k}}} + 1 = {count}$.",
        hint="Find the first and last multiples, then use n = (last - first)/k + 1.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="39_count_multiples_between_two_numbers",
        learning_objective_id=f"{LO}.39_count_multiples",
        misconception_tags=["forgets_plus_one_fencepost", "subtracts_bounds_directly"],
        diagnostic_tags=["sequences", "counting_terms"],
        keywords=["multiples", "counting", "interval"],
    )
    return _add_pillars(q, "39_count_multiples_between_two_numbers", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 40_sequence_with_common_difference_involving_surds
# --------------------------------------------------------------------------- #
def _build_40_sequence_with_common_difference_involving_surds(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    surd_val = r.choice([2, 3, 5])
    a_coeff = r.randint(1, 4)
    d_coeff = r.randint(2, 5)
    t1_str = f"{a_coeff}\\sqrt{{{surd_val}}}" if a_coeff > 1 else f"\\sqrt{{{surd_val}}}"
    t2_str = f"{a_coeff + d_coeff}\\sqrt{{{surd_val}}}"
    t3_str = f"{a_coeff + 2*d_coeff}\\sqrt{{{surd_val}}}"
    t4_str = f"{a_coeff + 3*d_coeff}\\sqrt{{{surd_val}}}"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the 4th term }} (T_4) \\text{{ of the sequence: }} {t1_str};\\; {t2_str};\\; {t3_str}; \\ldots",
        answer_expr=t4_str,
        answer_mode="expression",
        answer_latex=t4_str,
        marks=2,
        explanation=f"The common difference is $d = {d_coeff}\\sqrt{{{surd_val}}}$. Adding $d$ to $T_3$ gives $T_4 = {t4_str}$.",
        hint="Treat the surd like an algebraic like-term and add the coefficients.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="40_sequence_with_common_difference_involving_surds",
        learning_objective_id=f"{LO}.40_surd_sequence",
        misconception_tags=["adds_under_surd", "multiplies_surd_radicand"],
        diagnostic_tags=["sequences", "surds"],
        keywords=["surd sequence", "common difference", "like surds"],
    )
    return _add_pillars(q, "40_sequence_with_common_difference_involving_surds", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 41_first_difference_analysis_of_quadratic
# --------------------------------------------------------------------------- #
def _build_41_first_difference_analysis_of_quadratic(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    c = r.randint(1, 5)
    seq = [i**2 + c for i in range(1, 6)]
    d1 = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    d1_str = "; ".join(str(v) for v in d1)
    seq_str = "; ".join(str(v) for v in seq)

    sol = solution(
        goal="determine first differences of non-linear sequence",
        chain_type="expression",
        var="n",
        steps=[
            step(from_expr=seq_str, to_expr=d1_str, op="subtract consecutive terms", rule="first difference d_1"),
        ],
        final_expr=d1_str,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Write down the first differences of the sequence }} {seq_str}; \\ldots",
        answer_expr=d1_str,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"Subtract consecutive terms: ${seq[1]} - {seq[0]} = {d1[0]}$, ${seq[2]} - {seq[1]} = {d1[1]}$, etc. First differences: ${d1_str}$.",
        hint="Calculate T_2 - T_1, T_3 - T_2, T_4 - T_3, and T_5 - T_4.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="41_first_difference_analysis_of_quadratic",
        learning_objective_id=f"{LO}.41_first_differences",
        misconception_tags=["calculates_second_differences_too_early", "subtraction_errors"],
        diagnostic_tags=["sequences", "first_differences"],
        keywords=["first differences", "quadratic sequence", "consecutive differences"],
    )
    return _add_pillars(q, "41_first_difference_analysis_of_quadratic", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 42_identify_pattern_type_linear_vs_quadratic_vs_geometric
# --------------------------------------------------------------------------- #
def _build_42_identify_pattern_type_linear_vs_quadratic_vs_geometric(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    choice = r.choice(["linear", "quadratic", "geometric"])
    if choice == "linear":
        a = r.randint(3, 10)
        d = r.randint(3, 7)
        seq = [_term_val(a, d, i) for i in range(1, 5)]
        expl = f"Constant first difference ($d = {d}$), so it is a linear (arithmetic) sequence."
        correct_idx = 0
    elif choice == "quadratic":
        seq = [i**2 + 2 for i in range(1, 5)]
        expl = "First differences are 3; 5; 7 (not constant), but second differences are constant (2), so it is a quadratic sequence."
        correct_idx = 1
    else:
        seq = [2 * (3**(i - 1)) for i in range(1, 5)]
        expl = "Terms increase by a constant factor of 3 (common ratio), so it is a geometric sequence."
        correct_idx = 2

    seq_str = "; ".join(str(v) for v in seq)
    q = make_mcq(
        prefix=TOPIC,
        prompt=f"Classify the type of pattern formed by: ${seq_str}; \\ldots$",
        options=[
            "Linear (arithmetic)",
            "Quadratic",
            "Geometric",
            "None of the above",
        ],
        correct_index=correct_idx,
        explanation=expl,
        marks=1,
        hint="Check for a constant first difference (linear), constant ratio (geometric), or constant second difference (quadratic).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="42_identify_pattern_type_linear_vs_quadratic_vs_geometric",
        learning_objective_id=f"{LO}.42_classify_pattern",
        misconception_tags=["confuses_quadratic_with_geometric", "claims_linear_without_checking_differences"],
        diagnostic_tags=["sequences", "classification"],
        keywords=["classify sequence", "linear", "quadratic", "geometric"],
    )
    return _add_pillars(q, "42_identify_pattern_type_linear_vs_quadratic_vs_geometric", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 43_two_interleaved_sequences
# --------------------------------------------------------------------------- #
def _build_43_two_interleaved_sequences(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a1, d1 = r.randint(2, 6), r.randint(2, 4)
    a2, d2 = r.randint(20, 30), -r.randint(2, 4)

    terms = []
    for i in range(1, 7):
        if i % 2 != 0:
            k = (i + 1) // 2
            terms.append(a1 + (k - 1) * d1)
        else:
            k = i // 2
            terms.append(a2 + (k - 1) * d2)

    seq_str = "; ".join(str(v) for v in terms)
    t7 = a1 + 3 * d1

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the next term }} (T_7) \\text{{ in the interleaved pattern: }} {seq_str}; \\ldots",
        answer_expr=sp.Integer(t7),
        answer_mode="value",
        answer_latex=str(t7),
        marks=2,
        explanation=f"Notice that the terms alternate between two sequences. The odd positions form: ${terms[0]}; {terms[2]}; {terms[4]}; \\ldots$ with $d = {d1}$. The next odd term $T_7$ is ${terms[4]} + {d1} = {t7}$.",
        hint="Examine the odd positions (1st, 3rd, 5th) and even positions (2nd, 4th, 6th) separately.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="43_two_interleaved_sequences",
        learning_objective_id=f"{LO}.43_interleaved_pattern",
        misconception_tags=["calculates_single_difference_across_all_terms", "takes_even_pattern_instead_of_odd"],
        diagnostic_tags=["sequences", "interleaved_patterns"],
        keywords=["interleaved sequence", "alternating patterns", "next term"],
    )
    return _add_pillars(q, "43_two_interleaved_sequences", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 44_find_missing_middle_term_in_linear_sequence
# --------------------------------------------------------------------------- #
def _build_44_find_missing_middle_term_in_linear_sequence(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(4, 20)
    d = r.randint(3, 9)
    t1 = a
    t2 = a + d
    t3 = a + 2 * d

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{The sequence }} {t1};\\; p;\\; {t3} \\text{{ is arithmetic. Find the value of }} p.",
        answer_expr=sp.Integer(t2),
        answer_mode="value",
        answer_latex=str(t2),
        marks=2,
        explanation=f"In an arithmetic sequence, the middle term is the arithmetic mean of the two outer terms: $p = \\dfrac{{{t1} + {t3}}}{{2}} = \\dfrac{{{t1 + t3}}}{{2}} = {t2}$.",
        hint="The middle term between two numbers in an arithmetic sequence is their average.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="44_find_missing_middle_term_in_linear_sequence",
        learning_objective_id=f"{LO}.44_missing_middle_term",
        misconception_tags=["subtracts_terms_directly", "arithmetic_mean_error"],
        diagnostic_tags=["sequences", "missing_terms"],
        keywords=["missing term", "arithmetic mean", "linear"],
    )
    return _add_pillars(q, "44_find_missing_middle_term_in_linear_sequence", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 45_formula_for_sum_of_n_terms_linear_intuitive
# --------------------------------------------------------------------------- #
def _build_45_formula_for_sum_of_n_terms_linear_intuitive(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    n_count = r.choice([20, 50, 100])
    sum_val = (n_count * (n_count + 1)) // 2

    sol = solution(
        goal=f"calculate sum of first {n_count} natural numbers",
        chain_type="equation",
        var="S",
        steps=[
            step(from_expr=f"S = 1 + 2 + \\dots + {n_count}",
                 to_expr=f"S = \\frac{{{n_count}({n_count} + 1)}}{{2}}",
                 op="use Gauss pairing formula", rule="sum of first n integers"),
            step(from_expr=f"S = \\frac{{{n_count}({n_count + 1})}}{{2}}",
                 to_expr=f"S = {sum_val}",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=sp.Integer(sum_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Calculate the sum of the first }} {n_count} \\text{{ natural numbers: }} 1 + 2 + 3 + \\dots + {n_count}.",
        answer_expr=sp.Integer(sum_val),
        answer_mode="value",
        answer_latex=str(sum_val),
        marks=2,
        canonical_solution=sol,
        explanation=f"Using the pairing method: $\\text{{Sum}} = \\dfrac{{n(n + 1)}}{{2}} = \\dfrac{{{n_count}({n_count + 1})}}{{2}} = {sum_val}$.",
        hint="Pair 1 with n, 2 with n-1, etc., so each pair sums to n+1.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="45_formula_for_sum_of_n_terms_linear_intuitive",
        learning_objective_id=f"{LO}.45_gauss_sum",
        misconception_tags=["multiplies_n_by_n_only", "forgets_to_divide_by_two"],
        diagnostic_tags=["sequences", "series_intuition"],
        keywords=["sum of natural numbers", "Gauss method", "series"],
    )
    return _add_pillars(q, "45_formula_for_sum_of_n_terms_linear_intuitive", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 46_calculate_sum_of_first_n_terms
# --------------------------------------------------------------------------- #
def _build_46_calculate_sum_of_first_n_terms(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(2, 8)
    d = r.randint(2, 5)
    num_terms = r.choice([5, 6, 8])
    terms = [a + (i - 1) * d for i in range(1, num_terms + 1)]
    sum_val = sum(terms)
    terms_str = " + ".join(str(t) for t in terms[:4]) + f" + \\dots + {terms[-1]}"

    sol = solution(
        goal=f"calculate sum of first {num_terms} terms",
        chain_type="equation",
        var="S",
        steps=[
            step(from_expr=f"S_{{{num_terms}}} = \\frac{{{num_terms}}}{{2}}(T_1 + T_{{{num_terms}}})",
                 to_expr=f"S_{{{num_terms}}} = \\frac{{{num_terms}}}{{2}}({a} + {terms[-1]})",
                 op="use average of first and last term multiplied by n", rule="pairing sum"),
            step(from_expr=f"S_{{{num_terms}}} = \\frac{{{num_terms}}}{{2}}({a + terms[-1]})",
                 to_expr=f"S_{{{num_terms}}} = {sum_val}",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=sp.Integer(sum_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the sum of the first }} {num_terms} \\text{{ terms of the arithmetic sequence: }} {a};\\; {a+d};\\; {a+2*d}; \\ldots",
        answer_expr=sp.Integer(sum_val),
        answer_mode="value",
        answer_latex=str(sum_val),
        marks=2,
        canonical_solution=sol,
        explanation=f"The {num_terms}th term is $T_{{{num_terms}}} = {a} + ({num_terms}-1)({d}) = {terms[-1]}$. Sum = $\\dfrac{{{num_terms}}}{{2}}({a} + {terms[-1]}) = {sum_val}$.",
        hint="Find the last term, then multiply the average of the first and last terms by the number of terms.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="46_calculate_sum_of_first_n_terms",
        learning_objective_id=f"{LO}.46_sum_first_n_terms",
        misconception_tags=["forgets_division_by_two", "last_term_calculation_error"],
        diagnostic_tags=["sequences", "arithmetic_sum"],
        keywords=["sum", "arithmetic series", "first n terms"],
    )
    return _add_pillars(q, "46_calculate_sum_of_first_n_terms", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 47_sigma_notation_introduction_linear
# --------------------------------------------------------------------------- #
def _build_47_sigma_notation_introduction_linear(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    m_coeff = r.randint(2, 5)
    c_val = r.randint(1, 4)
    top_k = r.choice([3, 4, 5])
    # sum_{k=1}^{top_k} (m_coeff * k + c_val)
    terms = [m_coeff * k + c_val for k in range(1, top_k + 1)]
    sum_val = sum(terms)
    terms_expr = " + ".join(f"({m_coeff}({k}) + {c_val})" for k in range(1, top_k + 1))
    terms_eval = " + ".join(str(t) for t in terms)

    sol = solution(
        goal="evaluate sigma sum of linear expression",
        chain_type="equation",
        var="S",
        steps=[
            step(from_expr=f"\\sum_{{k=1}}^{{{top_k}}} ({m_coeff}k + {c_val})",
                 to_expr=f"{terms_eval}",
                 op="expand each term from k=1 to top index", rule="sigma definition"),
            step(from_expr=terms_eval, to_expr=str(sum_val), op="add terms", rule="arithmetic"),
        ],
        final_expr=sp.Integer(sum_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Evaluate: }} \\sum_{{k=1}}^{{{top_k}}} ({m_coeff}k + {c_val})",
        answer_expr=sp.Integer(sum_val),
        answer_mode="value",
        answer_latex=str(sum_val),
        marks=2,
        canonical_solution=sol,
        explanation=f"Substitute $k = 1, 2, \\dots, {top_k}$: ${terms_eval} = {sum_val}$.",
        hint=f"Substitute each integer from k=1 up to k={top_k} into the expression and add the results.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="47_sigma_notation_introduction_linear",
        learning_objective_id=f"{LO}.47_sigma_notation",
        misconception_tags=["evaluates_only_at_boundaries", "misunderstands_sigma_symbol"],
        diagnostic_tags=["sequences", "sigma_notation"],
        keywords=["sigma notation", "summation", "linear expression"],
    )
    return _add_pillars(q, "47_sigma_notation_introduction_linear", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 48_practical_linear_sequence_auditorium_seats
# --------------------------------------------------------------------------- #
def _build_48_practical_linear_sequence_auditorium_seats(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(14, 25)
    d = r.choice([2, 3, 4])
    row_num = r.choice([12, 15, 18, 20])
    seats = a + (row_num - 1) * d

    sol = solution(
        goal=f"find number of seats in row {row_num}",
        chain_type="equation",
        var="T_n",
        steps=[
            step(from_expr="T_n = a + (n - 1)d",
                 to_expr=f"T_{{{row_num}}} = {a} + ({row_num} - 1)({d})",
                 op="substitute row number and difference into arithmetic formula", rule="general term"),
            step(from_expr=f"T_{{{row_num}}} = {a} + {row_num - 1} \\times {d}",
                 to_expr=f"T_{{{row_num}}} = {seats}",
                 op="simplify", rule="arithmetic"),
        ],
        final_expr=sp.Integer(seats),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=(
            f"\\text{{An auditorium has }} {a} \\text{{ seats in the first row. Each successive row has }} "
            f"{d} \\text{{ more seats than the row in front of it. How many seats are in row }} {row_num}?"
        ),
        answer_expr=sp.Integer(seats),
        answer_mode="value",
        answer_latex=str(seats),
        marks=2,
        canonical_solution=sol,
        explanation=f"$T_n = a + (n - 1)d = {a} + ({row_num} - 1)({d}) = {a} + {(row_num - 1)*d} = {seats}$ seats.",
        hint="Use the linear formula T_n = a + (n - 1)d with a as row 1 seats and d as the extra seats per row.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="48_practical_linear_sequence_auditorium_seats",
        learning_objective_id=f"{LO}.48_auditorium_seats",
        misconception_tags=["multiplies_row_by_difference_without_minus_one", "off_by_one_row"],
        diagnostic_tags=["applications", "auditorium_model"],
        keywords=["auditorium", "seats", "linear sequence", "word problem"],
    )
    return _add_pillars(q, "48_practical_linear_sequence_auditorium_seats", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 49_practical_linear_sequence_piling_pipes
# --------------------------------------------------------------------------- #
def _build_49_practical_linear_sequence_piling_pipes(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    top_layer = r.randint(3, 7)
    layers = r.choice([6, 8, 10, 12])
    # Each layer has 1 more pipe than the one above it
    bottom_layer = top_layer + (layers - 1)

    sol = solution(
        goal=f"find number of pipes in layer {layers}",
        chain_type="equation",
        var="T_n",
        steps=[
            step(from_expr="T_n = a + (n - 1)d",
                 to_expr=f"T_{{{layers}}} = {top_layer} + ({layers} - 1)(1)",
                 op="substitute top layer count with d=1", rule="linear term"),
            step(from_expr=f"T_{{{layers}}} = {top_layer} + {layers - 1}",
                 to_expr=f"T_{{{layers}}} = {bottom_layer}",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=sp.Integer(bottom_layer),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=(
            f"\\text{{Cylindrical pipes are stacked in a trapezoidal pile. The top layer has }} {top_layer} "
            f"\\text{{ pipes, and each layer below it has 1 more pipe than the layer directly above. "
            f"How many pipes are in the }} {layers}\\text{{th layer from the top?}}"
        ),
        answer_expr=sp.Integer(bottom_layer),
        answer_mode="value",
        answer_latex=str(bottom_layer),
        marks=2,
        canonical_solution=sol,
        explanation=f"$T_n = a + (n - 1)d = {top_layer} + ({layers} - 1)(1) = {bottom_layer}$ pipes.",
        hint="The sequence of pipes per layer is arithmetic with d = 1.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="49_practical_linear_sequence_piling_pipes",
        learning_objective_id=f"{LO}.49_pipe_stack",
        misconception_tags=["adds_layers_instead_of_difference", "off_by_one_layer"],
        diagnostic_tags=["applications", "stacked_pipes"],
        keywords=["pipe stack", "layers", "linear sequence"],
    )
    return _add_pillars(q, "49_practical_linear_sequence_piling_pipes", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 50_comprehensive_investigation_linear_pattern
# --------------------------------------------------------------------------- #
def _build_50_comprehensive_investigation_linear_pattern(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(5, 18)
    d = r.randint(4, 9)
    target_pos = r.choice([25, 30, 40])
    target_val = a + (target_pos - 1) * d
    t1, t2, t3 = a, a + d, a + 2 * d

    sol = solution(
        goal=f"determine which term equals {target_val}",
        chain_type="equation",
        var="n",
        steps=[
            step(from_expr=f"T_1 = {t1}, \\quad T_2 = {t2}",
                 to_expr=f"d = {t2} - {t1} = {d}",
                 op="find common difference", rule="d = T_2 - T_1"),
            step(from_expr=f"T_n = {d}n + ({a - d})",
                 to_expr=f"{target_val} = {d}n + ({a - d})",
                 op="equate general formula to target value", rule="T_n formula"),
            step(from_expr=f"{d}n = {target_val - (a - d)}",
                 to_expr=f"n = {target_pos}",
                 op="solve for term position", rule="linear equation"),
        ],
        final_expr=sp.Integer(target_pos),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=(
            f"\\text{{Consider the arithmetic pattern: }} {t1};\\; {t2};\\; {t3}; \\ldots \\quad "
            f"\\text{{Determine which term in the pattern is equal to }} {target_val}."
        ),
        answer_expr=sp.Integer(target_pos),
        answer_mode="value",
        answer_latex=str(target_pos),
        marks=3,
        canonical_solution=sol,
        explanation=(
            f"Common difference $d = {t2} - {t1} = {d}$. General formula: $T_n = {a} + (n - 1)({d}) = {d}n + {a - d}$. "
            f"Set $T_n = {target_val} \\implies {d}n + {a - d} = {target_val} \\implies {d}n = {target_val - (a - d)} \\implies n = {target_pos}$."
        ),
        hint="Find d first, write the formula T_n = dn + c, and solve T_n = target for n.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="50_comprehensive_investigation_linear_pattern",
        learning_objective_id=f"{LO}.50_capstone_investigation",
        misconception_tags=["solves_for_Tn_instead_of_n", "algebraic_manipulation_error"],
        diagnostic_tags=["sequences", "synthesis"],
        keywords=["capstone", "which term", "general term", "investigation"],
    )
    return _add_pillars(q, "50_comprehensive_investigation_linear_pattern", duration=3, weight=15)


BUILDERS_26_50: Dict[str, Any] = {
    "26_fence_post_and_rail_pattern": _build_26_fence_post_and_rail_pattern,
    "27_tile_border_paving_pattern": _build_27_tile_border_paving_pattern,
    "28_staircase_blocks_linear_difference": _build_28_staircase_blocks_linear_difference,
    "29_dots_geometric_grid_pattern": _build_29_dots_geometric_grid_pattern,
    "30_word_problem_constant_rate_savings": _build_30_word_problem_constant_rate_savings,
    "31_word_problem_constant_rate_depletion": _build_31_word_problem_constant_rate_depletion,
    "32_word_problem_growing_plant_height": _build_32_word_problem_growing_plant_height,
    "33_find_terms_with_subscript_operations": _build_33_find_terms_with_subscript_operations,
    "34_algebraic_linear_sequence_with_powers": _build_34_algebraic_linear_sequence_with_powers,
    "35_sequence_with_alternating_signs_linear_magnitude": _build_35_sequence_with_alternating_signs_linear_magnitude,
    "36_odd_numbers_sequence_properties": _build_36_odd_numbers_sequence_properties,
    "37_even_numbers_sequence_properties": _build_37_even_numbers_sequence_properties,
    "38_multiples_of_k_sequence": _build_38_multiples_of_k_sequence,
    "39_count_multiples_between_two_numbers": _build_39_count_multiples_between_two_numbers,
    "40_sequence_with_common_difference_involving_surds": _build_40_sequence_with_common_difference_involving_surds,
    "41_first_difference_analysis_of_quadratic": _build_41_first_difference_analysis_of_quadratic,
    "42_identify_pattern_type_linear_vs_quadratic_vs_geometric": _build_42_identify_pattern_type_linear_vs_quadratic_vs_geometric,
    "43_two_interleaved_sequences": _build_43_two_interleaved_sequences,
    "44_find_missing_middle_term_in_linear_sequence": _build_44_find_missing_middle_term_in_linear_sequence,
    "45_formula_for_sum_of_n_terms_linear_intuitive": _build_45_formula_for_sum_of_n_terms_linear_intuitive,
    "46_calculate_sum_of_first_n_terms": _build_46_calculate_sum_of_first_n_terms,
    "47_sigma_notation_introduction_linear": _build_47_sigma_notation_introduction_linear,
    "48_practical_linear_sequence_auditorium_seats": _build_48_practical_linear_sequence_auditorium_seats,
    "49_practical_linear_sequence_piling_pipes": _build_49_practical_linear_sequence_piling_pipes,
    "50_comprehensive_investigation_linear_pattern": _build_50_comprehensive_investigation_linear_pattern,
}
