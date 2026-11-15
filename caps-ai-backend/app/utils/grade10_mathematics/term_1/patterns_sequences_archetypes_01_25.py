"""Grade 10 Mathematics — Term 1 — Number Patterns: Archetypes 01 to 25.

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
x_sym = sp.Symbol("x")


def _term_val(a: int, d: int, pos: int) -> int:
    return a + (pos - 1) * d


def _seq_str(a: int, d: int, count: int) -> str:
    return "; ".join(str(_term_val(a, d, i)) for i in range(1, count + 1))


def _add_pillars(q: Dict[str, Any], subskill_name: str, duration: int = 3, weight: int = 15) -> Dict[str, Any]:
    marks = int(q.get("marks", 2))
    schema = [
        {"criterion": "Application of linear sequence formula / concept", "marks": max(1, marks - 1)},
        {"criterion": "Correct calculation / evaluation", "marks": 1},
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
# 01_identify_linear_vs_non_linear_sequence
# --------------------------------------------------------------------------- #
def _build_01_identify_linear_vs_non_linear_sequence(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    is_linear = r.choice([True, False])
    if is_linear:
        a = r.randint(2, 10)
        d = nonzero(r, -6, 6)
        seq = [_term_val(a, d, i) for i in range(1, 5)]
        seq_tex = "; ".join(str(v) for v in seq)
        explanation = f"Consecutive terms have a constant first difference: $d = {d}$. Therefore, it is a linear (arithmetic) sequence."
        correct_idx = 0
    else:
        # quadratic or geometric
        pattern_kind = r.choice(["quadratic", "geometric"])
        if pattern_kind == "quadratic":
            seq = [i**2 for i in range(1, 5)]
            diffs = "3; 5; 7"
        else:
            base = r.choice([2, 3])
            seq = [base**i for i in range(1, 5)]
            diffs = f"{seq[1]-seq[0]}; {seq[2]-seq[1]}; {seq[3]-seq[2]}"
        seq_tex = "; ".join(str(v) for v in seq)
        explanation = f"Differences between consecutive terms are {diffs}, which are not constant. Therefore, it is not a linear sequence."
        correct_idx = 1

    q = make_mcq(
        prefix=TOPIC,
        prompt=f"Is the sequence ${seq_tex}; \\ldots$ a linear (arithmetic) sequence?",
        options=[
            "Yes, it has a constant first difference between consecutive terms.",
            "No, the differences between consecutive terms are not constant.",
            "Yes, because all terms are integers.",
            "No, because the terms increase too rapidly.",
        ],
        correct_index=correct_idx,
        explanation=explanation,
        marks=1,
        hint="Calculate the difference between consecutive terms: T_2 - T_1, T_3 - T_2, etc.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="01_identify_linear_vs_non_linear_sequence",
        learning_objective_id=f"{LO}.01_identify_linear",
        misconception_tags=["assumes_linear_without_checking", "confuses_ratio_and_difference"],
        diagnostic_tags=["sequences", "linear_identification"],
        keywords=["linear sequence", "arithmetic progression", "constant difference"],
    )
    return _add_pillars(q, "01_identify_linear_vs_non_linear_sequence", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 02_find_next_terms_positive_difference
# --------------------------------------------------------------------------- #
def _build_02_find_next_terms_positive_difference(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    a = r.randint(2, 15)
    d = r.randint(3, 9)
    seq = [_term_val(a, d, i) for i in range(1, 4)]
    next_two = [_term_val(a, d, 4), _term_val(a, d, 5)]
    ans_str = f"{next_two[0]}; {next_two[1]}"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Write down the next two terms of the sequence: }} {seq[0]};\\; {seq[1]};\\; {seq[2]}; \\ldots",
        answer_expr=ans_str,
        answer_mode="expression",
        marks=2,
        explanation=f"Common difference $d = {seq[1]} - {seq[0]} = {d}$. The next terms are ${seq[2]} + {d} = {next_two[0]}$ and ${next_two[0]} + {d} = {next_two[1]}$.",
        hint=f"Find the difference d = T_2 - T_1, then add {d} to get the next terms.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="02_find_next_terms_positive_difference",
        learning_objective_id=f"{LO}.02_next_terms_pos_diff",
        misconception_tags=["adds_wrong_difference", "off_by_one_calculation"],
        diagnostic_tags=["sequences", "next_terms"],
        keywords=["next terms", "positive difference", "linear"],
    )
    return _add_pillars(q, "02_find_next_terms_positive_difference", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 03_find_next_terms_negative_difference
# --------------------------------------------------------------------------- #
def _build_03_find_next_terms_negative_difference(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    a = r.randint(35, 60)
    d = -r.randint(4, 9)
    seq = [_term_val(a, d, i) for i in range(1, 4)]
    next_two = [_term_val(a, d, 4), _term_val(a, d, 5)]
    ans_str = f"{next_two[0]}; {next_two[1]}"

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Write down the next two terms of the decreasing sequence: }} {seq[0]};\\; {seq[1]};\\; {seq[2]}; \\ldots",
        answer_expr=ans_str,
        answer_mode="expression",
        marks=2,
        explanation=f"Common difference $d = {seq[1]} - {seq[0]} = {d}$. Subtracting ${abs(d)}$: next terms are ${next_two[0]};\\; {next_two[1]}$.",
        hint="The sequence is decreasing. Find d = T_2 - T_1 (which is negative) and continue subtracting.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="03_find_next_terms_negative_difference",
        learning_objective_id=f"{LO}.03_next_terms_neg_diff",
        misconception_tags=["adds_instead_of_subtracting", "negative_arithmetic_error"],
        diagnostic_tags=["sequences", "negative_difference"],
        keywords=["decreasing sequence", "negative difference", "next terms"],
    )
    return _add_pillars(q, "03_find_next_terms_negative_difference", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 04_find_next_terms_fractional_difference
# --------------------------------------------------------------------------- #
def _build_04_find_next_terms_fractional_difference(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    denom = r.choice([2, 3, 4])
    num_start = r.randint(1, 5)
    num_step = r.choice([1, 2])
    t1 = sp.Rational(num_start, denom)
    t2 = sp.Rational(num_start + num_step, denom)
    t3 = sp.Rational(num_start + 2 * num_step, denom)
    t4 = sp.Rational(num_start + 3 * num_step, denom)
    t4_tex = to_latex(t4)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Determine the 4th term }} (T_4) \\text{{ of the sequence: }} {to_latex(t1)};\\; {to_latex(t2)};\\; {to_latex(t3)}; \\ldots",
        answer_expr=t4,
        answer_mode="fraction",
        answer_latex=t4_tex,
        marks=2,
        explanation=f"Common difference $d = T_2 - T_1 = {to_latex(t2)} - {to_latex(t1)} = {to_latex(sp.Rational(num_step, denom))}$. Thus $T_4 = {to_latex(t3)} + {to_latex(sp.Rational(num_step, denom))} = {t4_tex}$.",
        hint="Find the common difference by subtracting the first fraction from the second.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="04_find_next_terms_fractional_difference",
        learning_objective_id=f"{LO}.04_next_terms_fractions",
        misconception_tags=["fraction_addition_error", "ignores_common_denominator"],
        diagnostic_tags=["sequences", "fractions"],
        keywords=["fractional difference", "next term", "arithmetic"],
    )
    return _add_pillars(q, "04_find_next_terms_fractional_difference", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 05_calculate_common_difference_integers
# --------------------------------------------------------------------------- #
def _build_05_calculate_common_difference_integers(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    a = r.randint(4, 25)
    d = r.randint(3, 12)
    s = _seq_str(a, d, 4)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Determine the common difference }} d \\text{{ of the arithmetic sequence: }} {s}; \\ldots",
        answer_expr=sp.Integer(d),
        answer_mode="value",
        answer_latex=str(d),
        marks=1,
        explanation=f"$d = T_2 - T_1 = {a + d} - {a} = {d}$.",
        hint="Subtract the first term from the second term: d = T_2 - T_1.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="05_calculate_common_difference_integers",
        learning_objective_id=f"{LO}.05_calc_d_integers",
        misconception_tags=["subtracts_in_reverse_order", "uses_first_term_as_d"],
        diagnostic_tags=["sequences", "common_difference"],
        keywords=["common difference", "integers", "d"],
    )
    return _add_pillars(q, "05_calculate_common_difference_integers", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 06_calculate_common_difference_negative
# --------------------------------------------------------------------------- #
def _build_06_calculate_common_difference_negative(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    a = r.randint(10, 30)
    d = -r.randint(3, 11)
    s = _seq_str(a, d, 4)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Determine the common difference }} d \\text{{ of the sequence: }} {s}; \\ldots",
        answer_expr=sp.Integer(d),
        answer_mode="value",
        answer_latex=str(d),
        marks=1,
        explanation=f"$d = T_2 - T_1 = {a + d} - {a} = {d}$. Since the sequence decreases, $d$ is negative.",
        hint="Remember d = T_2 - T_1. Because T_2 < T_1, the result must be negative.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="06_calculate_common_difference_negative",
        learning_objective_id=f"{LO}.06_calc_d_negative",
        misconception_tags=["forgets_negative_sign_in_d", "calculates_T1_minus_T2"],
        diagnostic_tags=["sequences", "negative_d"],
        keywords=["negative difference", "common difference", "d"],
    )
    return _add_pillars(q, "06_calculate_common_difference_negative", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 07_calculate_common_difference_fractions
# --------------------------------------------------------------------------- #
def _build_07_calculate_common_difference_fractions(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    denom = r.choice([3, 4, 5])
    step_n = r.choice([1, 2, 3])
    t1 = sp.Rational(1, denom)
    t2 = t1 + sp.Rational(step_n, denom)
    t3 = t2 + sp.Rational(step_n, denom)
    d_ans = sp.Rational(step_n, denom)

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the common difference }} d \\text{{ for the sequence: }} {to_latex(t1)};\\; {to_latex(t2)};\\; {to_latex(t3)}; \\ldots",
        answer_expr=d_ans,
        answer_mode="fraction",
        answer_latex=to_latex(d_ans),
        marks=2,
        explanation=f"$d = T_2 - T_1 = {to_latex(t2)} - {to_latex(t1)} = {to_latex(d_ans)}$.",
        hint="Calculate d = T_2 - T_1.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="07_calculate_common_difference_fractions",
        learning_objective_id=f"{LO}.07_calc_d_fractions",
        misconception_tags=["fraction_subtraction_error", "ignores_denominator"],
        diagnostic_tags=["sequences", "fraction_d"],
        keywords=["fraction difference", "common difference", "fractions"],
    )
    return _add_pillars(q, "07_calculate_common_difference_fractions", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 08_determine_general_term_positive_diff
# --------------------------------------------------------------------------- #
def _build_08_determine_general_term_positive_diff(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(2, 12)
    d = r.randint(2, 8)
    s = _seq_str(a, d, 4)
    c = a - d
    tn_expr = sp.expand(d * n + c)

    sol = solution(
        goal="determine general term Tn",
        chain_type="equation",
        var="n",
        steps=[
            step(from_expr="d = T_2 - T_1", to_expr=f"d = {a + d} - {a} = {d}", op="calculate common difference", rule="d = T_2 - T_1"),
            step(from_expr="T_n = a + (n - 1)d", to_expr=f"T_n = {a} + (n - 1)({d})", op="substitute a and d", rule="formula"),
            step(from_expr=f"T_n = {a} + {d}n - {d}", to_expr=f"T_n = {to_latex(tn_expr)}", op="expand and simplify", rule="algebra"),
        ],
        final_expr=tn_expr,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Determine the general formula }} T_n \\text{{ for the sequence: }} {s}; \\ldots",
        answer_expr=tn_expr,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"$a = {a}$, $d = {d}$. Using $T_n = a + (n - 1)d = {a} + (n - 1)({d}) = {to_latex(tn_expr)}$.",
        hint="Use T_n = a + (n - 1)d and simplify the expression.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="08_determine_general_term_positive_diff",
        learning_objective_id=f"{LO}.08_general_term_pos",
        misconception_tags=["forgets_to_distribute_d", "confuses_a_and_d"],
        diagnostic_tags=["sequences", "general_term"],
        keywords=["general term", "T_n", "formula"],
    )
    return _add_pillars(q, "08_determine_general_term_positive_diff", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 09_determine_general_term_negative_diff
# --------------------------------------------------------------------------- #
def _build_09_determine_general_term_negative_diff(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(25, 50)
    d = -r.randint(3, 8)
    s = _seq_str(a, d, 4)
    c = a - d
    tn_expr = sp.expand(d * n + c)

    sol = solution(
        goal="determine general term for decreasing sequence",
        chain_type="equation",
        var="n",
        steps=[
            step(from_expr="d = T_2 - T_1", to_expr=f"d = {d}", op="find common difference", rule="d = T_2 - T_1"),
            step(from_expr="T_n = a + (n - 1)d", to_expr=f"T_n = {a} + (n - 1)({d})", op="substitute into formula", rule="arithmetic formula"),
            step(from_expr=f"T_n = {a} - {abs(d)}n + {abs(d)}", to_expr=f"T_n = {to_latex(tn_expr)}", op="simplify", rule="algebra"),
        ],
        final_expr=tn_expr,
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the general term }} T_n \\text{{ for the decreasing sequence: }} {s}; \\ldots",
        answer_expr=tn_expr,
        answer_mode="expression",
        marks=2,
        canonical_solution=sol,
        explanation=f"$a = {a}$, $d = {d}$. $T_n = {a} + (n - 1)({d}) = {to_latex(tn_expr)}$.",
        hint="Substitute a and the negative common difference d into T_n = a + (n - 1)d.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="09_determine_general_term_negative_diff",
        learning_objective_id=f"{LO}.09_general_term_neg",
        misconception_tags=["sign_error_expanding_negative_d", "omits_negative_sign"],
        diagnostic_tags=["sequences", "general_term_negative"],
        keywords=["decreasing sequence", "T_n", "negative d"],
    )
    return _add_pillars(q, "09_determine_general_term_negative_diff", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 10_determine_general_term_fractional
# --------------------------------------------------------------------------- #
def _build_10_determine_general_term_fractional(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    denom = r.choice([2, 4])
    a_num = r.randint(1, 5)
    d_num = r.choice([1, 3])
    a_frac = sp.Rational(a_num, denom)
    d_frac = sp.Rational(d_num, denom)
    t1 = a_frac
    t2 = a_frac + d_frac
    t3 = a_frac + 2 * d_frac
    tn_expr = sp.expand(d_frac * n + (a_frac - d_frac))

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Determine }} T_n \\text{{ for: }} {to_latex(t1)};\\; {to_latex(t2)};\\; {to_latex(t3)}; \\ldots",
        answer_expr=tn_expr,
        answer_mode="expression",
        marks=2,
        explanation=f"$a = {to_latex(a_frac)}$, $d = {to_latex(d_frac)}$. $T_n = {to_latex(a_frac)} + (n - 1)\\left({to_latex(d_frac)}\\right) = {to_latex(tn_expr)}$.",
        hint="Use T_n = a + (n - 1)d with fractions.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="10_determine_general_term_fractional",
        learning_objective_id=f"{LO}.10_general_term_fractional",
        misconception_tags=["fraction_distribution_error", "confuses_numerator_and_denominator"],
        diagnostic_tags=["sequences", "fraction_formula"],
        keywords=["fraction general term", "T_n", "linear fractions"],
    )
    return _add_pillars(q, "10_determine_general_term_fractional", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 11_calculate_specific_term_from_formula
# --------------------------------------------------------------------------- #
def _build_11_calculate_specific_term_from_formula(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    d = r.randint(3, 8)
    c = nonzero(r, -15, 15)
    pos = r.choice([15, 20, 25, 50])
    ans_val = d * pos + c

    sol = solution(
        goal=f"calculate T_{{{pos}}} given T_n = {d}n + {c}",
        chain_type="equation",
        var="T_n",
        steps=[
            step(from_expr=f"T_n = {d}n {'+' if c >= 0 else ''} {c}",
                 to_expr=f"T_{{{pos}}} = {d}({pos}) {'+' if c >= 0 else ''} {c}",
                 op="substitute n with position", rule="evaluation"),
            step(from_expr=f"T_{{{pos}}} = {d * pos} {'+' if c >= 0 else ''} {c}",
                 to_expr=f"T_{{{pos}}} = {ans_val}",
                 op="evaluate", rule="arithmetic"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Given the formula }} T_n = {d}n {'+' if c >= 0 else ''} {c}, \\text{{ calculate }} T_{{{pos}}}.",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=2,
        canonical_solution=sol,
        explanation=f"Substitute $n = {pos}$: $T_{{{pos}}} = {d}({pos}) {'+' if c >= 0 else ''} {c} = {d * pos} {'+' if c >= 0 else ''} {c} = {ans_val}$.",
        hint=f"Replace n with {pos} in the formula and simplify.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="11_calculate_specific_term_from_formula",
        learning_objective_id=f"{LO}.11_term_from_formula",
        misconception_tags=["multiplication_before_addition_error", "substitutes_incorrectly"],
        diagnostic_tags=["sequences", "evaluate_term"],
        keywords=["evaluate term", "specific term", "formula"],
    )
    return _add_pillars(q, "11_calculate_specific_term_from_formula", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 12_calculate_specific_term_from_sequence
# --------------------------------------------------------------------------- #
def _build_12_calculate_specific_term_from_sequence(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(3, 15)
    d = r.randint(3, 7)
    pos = r.choice([12, 16, 20, 25])
    seq = [_term_val(a, d, i) for i in range(1, 4)]
    ans_val = a + (pos - 1) * d

    sol = solution(
        goal=f"find term at position {pos}",
        chain_type="equation",
        var="T_n",
        steps=[
            step(from_expr=f"T_1 = {seq[0]}, \\; T_2 = {seq[1]}", to_expr=f"d = {d}", op="find common difference", rule="d = T_2 - T_1"),
            step(from_expr="T_n = a + (n - 1)d", to_expr=f"T_{{{pos}}} = {a} + ({pos} - 1)({d})", op="substitute a, d, n", rule="arithmetic formula"),
            step(from_expr=f"T_{{{pos}}} = {a} + {pos - 1} \\times {d}", to_expr=f"T_{{{pos}}} = {ans_val}", op="evaluate", rule="arithmetic"),
        ],
        final_expr=sp.Integer(ans_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the }} {pos}\\text{{th term of the sequence: }} {seq[0]};\\; {seq[1]};\\; {seq[2]}; \\ldots",
        answer_expr=sp.Integer(ans_val),
        answer_mode="value",
        answer_latex=str(ans_val),
        marks=2,
        canonical_solution=sol,
        explanation=f"$a = {a}$, $d = {d}$. $T_{{{pos}}} = {a} + ({pos} - 1)({d}) = {ans_val}$.",
        hint="Find d first, then use T_n = a + (n - 1)d.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="12_calculate_specific_term_from_sequence",
        learning_objective_id=f"{LO}.12_term_from_sequence",
        misconception_tags=["off_by_one_position", "multiplies_n_by_a"],
        diagnostic_tags=["sequences", "specific_term"],
        keywords=["specific term", "position", "arithmetic sequence"],
    )
    return _add_pillars(q, "12_calculate_specific_term_from_sequence", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 13_find_term_position_given_value
# --------------------------------------------------------------------------- #
def _build_13_find_term_position_given_value(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(2, 12)
    d = r.randint(3, 8)
    n_target = r.randint(15, 35)
    val_target = a + (n_target - 1) * d
    s = _seq_str(a, d, 3)

    sol = solution(
        goal=f"find n such that T_n = {val_target}",
        chain_type="equation",
        var="n",
        steps=[
            step(from_expr=f"T_n = {a} + (n - 1)({d})", to_expr=f"{val_target} = {a} + (n - 1)({d})", op="set formula equal to target value", rule="substitution"),
            step(from_expr=f"{val_target - a} = (n - 1)({d})", to_expr=f"{n_target - 1} = n - 1", op="divide by d", rule="solve linear equation"),
            step(from_expr=f"n - 1 = {n_target - 1}", to_expr=f"n = {n_target}", op="add 1", rule="isolate n"),
        ],
        final_expr=sp.Integer(n_target),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Which term of the sequence }} {s}; \\ldots \\text{{ is equal to }} {val_target}?",
        answer_expr=sp.Integer(n_target),
        answer_mode="value",
        answer_latex=str(n_target),
        marks=2,
        canonical_solution=sol,
        explanation=f"$T_n = {a} + (n - 1)({d}) = {val_target} \\implies (n - 1)({d}) = {val_target - a} \\implies n - 1 = {n_target - 1} \\implies n = {n_target}$.",
        hint="Set T_n = a + (n - 1)d equal to the given value and solve for n.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="13_find_term_position_given_value",
        learning_objective_id=f"{LO}.13_find_position",
        misconception_tags=["forgets_to_add_one_to_n_minus_one", "algebraic_solving_error"],
        diagnostic_tags=["sequences", "solve_for_n"],
        keywords=["which term", "position n", "solve for n"],
    )
    return _add_pillars(q, "13_find_term_position_given_value", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 14_test_if_number_is_term_of_sequence
# --------------------------------------------------------------------------- #
def _build_14_test_if_number_is_term_of_sequence(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(3, 10)
    d = r.randint(4, 7)
    is_term = r.choice([True, False])
    if is_term:
        n_val = r.randint(12, 25)
        test_val = a + (n_val - 1) * d
        expl = f"Setting $T_n = {test_val} \\implies {a} + (n - 1)({d}) = {test_val} \\implies n = {n_val}$. Since $n$ is a positive integer, ${test_val}$ is a term (the {n_val}th term)."
        correct_idx = 0
    else:
        n_val = r.randint(12, 25)
        test_val = a + (n_val - 1) * d + r.choice([1, 2])
        frac_val = sp.Rational(test_val - a, d) + 1
        expl = f"Setting $T_n = {test_val} \\implies n = {to_latex(frac_val)}$. Since $n$ is not a natural number ($n \\notin \\mathbb{{N}}$), ${test_val}$ is NOT a term."
        correct_idx = 1

    s = _seq_str(a, d, 3)
    q = make_mcq(
        prefix=TOPIC,
        prompt=f"Is the number ${test_val}$ a term of the sequence ${s}; \\ldots$?",
        options=[
            f"Yes, it is the {n_val}th term." if is_term else "Yes, every number appears eventually.",
            f"No, because solving for n gives a non-integer ($n \\notin \\mathbb{{N}}$)." if not is_term else "No, it is too large.",
            "Yes, because it is positive.",
            "No, because it is an odd number.",
        ],
        correct_index=0 if is_term else 1,
        explanation=expl,
        marks=2,
        hint="Set T_n equal to the number and solve for n. If n is a positive integer, it is a term.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="14_test_if_number_is_term_of_sequence",
        learning_objective_id=f"{LO}.14_test_term_membership",
        misconception_tags=["accepts_non_integer_n", "calculation_error"],
        diagnostic_tags=["sequences", "natural_number_n"],
        keywords=["is a term", "membership", "integer n"],
    )
    return _add_pillars(q, "14_test_if_number_is_term_of_sequence", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 15_first_negative_term_of_decreasing_sequence
# --------------------------------------------------------------------------- #
def _build_15_first_negative_term_of_decreasing_sequence(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(50, 95)
    d = -r.randint(6, 12)
    # T_n < 0 => a + (n - 1)d < 0 => n - 1 > -a/d => n > 1 + a/abs(d)
    n_first_neg = math.floor(a / abs(d)) + 2
    term_first_neg = a + (n_first_neg - 1) * d

    sol = solution(
        goal="find first negative term",
        chain_type="equation",
        var="n",
        steps=[
            step(from_expr=f"T_n < 0", to_expr=f"{a} + (n - 1)({d}) < 0", op="set general term less than zero", rule="inequality"),
            step(from_expr=f"{abs(d)}n > {a + abs(d)}", to_expr=f"n > {to_latex(sp.Rational(a + abs(d), abs(d)))}", op="divide by coefficient", rule="isolate n"),
            step(from_expr=f"n > {float(a + abs(d))/abs(d):.2f}", to_expr=f"n = {n_first_neg}, \\; T_{{{n_first_neg}}} = {term_first_neg}", op="select smallest integer n and evaluate", rule="first negative term"),
        ],
        final_expr=sp.Integer(term_first_neg),
    )
    s = _seq_str(a, d, 3)
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the value of the first negative term of the sequence: }} {s}; \\ldots",
        answer_expr=sp.Integer(term_first_neg),
        answer_mode="value",
        answer_latex=str(term_first_neg),
        marks=2,
        canonical_solution=sol,
        explanation=f"Set $T_n < 0 \\implies {a} - {abs(d)}(n - 1) < 0 \\implies n > {1 + a/abs(d):.2f}$. Smallest integer is $n = {n_first_neg}$. $T_{{{n_first_neg}}} = {a} + ({n_first_neg} - 1)({d}) = {term_first_neg}$.",
        hint="Set T_n < 0, solve for n, choose the next whole number, then evaluate T_n.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="15_first_negative_term_of_decreasing_sequence",
        learning_objective_id=f"{LO}.15_first_negative_term",
        misconception_tags=["gives_position_instead_of_value", "rounding_direction_error"],
        diagnostic_tags=["sequences", "inequality_terms"],
        keywords=["first negative term", "decreasing", "T_n < 0"],
    )
    return _add_pillars(q, "15_first_negative_term_of_decreasing_sequence", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 16_first_term_exceeding_given_value
# --------------------------------------------------------------------------- #
def _build_16_first_term_exceeding_given_value(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(5, 20)
    d = r.randint(4, 9)
    threshold = r.choice([100, 150, 200, 250])
    # T_n > threshold => a + (n - 1)d > threshold => n - 1 > (threshold - a)/d
    n_ans = math.floor((threshold - a) / d) + 2

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the position }} n \\text{{ of the first term that exceeds }} {threshold} \\text{{ in the sequence: }} {_seq_str(a, d, 3)}; \\ldots",
        answer_expr=sp.Integer(n_ans),
        answer_mode="value",
        answer_latex=str(n_ans),
        marks=2,
        explanation=f"Set $T_n > {threshold} \\implies {a} + (n - 1)({d}) > {threshold} \\implies n - 1 > {(threshold - a)/d:.2f} \\implies n > {1 + (threshold - a)/d:.2f}$. The first whole number is $n = {n_ans}$.",
        hint="Set T_n > threshold and round up to the next integer.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="16_first_term_exceeding_given_value",
        learning_objective_id=f"{LO}.16_first_exceeding",
        misconception_tags=["rounds_down_instead_of_up", "gives_term_value_instead_of_n"],
        diagnostic_tags=["sequences", "inequalities"],
        keywords=["first term exceeding", "threshold", "n"],
    )
    return _add_pillars(q, "16_first_term_exceeding_given_value", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 17_solve_for_variable_in_linear_sequence
# --------------------------------------------------------------------------- #
def _build_17_solve_for_variable_in_linear_sequence(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # Terms in terms of x: T_1 = x + c1, T_2 = 2x + c2, T_3 = 4x + c3
    # d = T_2 - T_1 = T_3 - T_2 => (2x + c2) - (x + c1) = (4x + c3) - (2x + c2)
    # x + c2 - c1 = 2x + c3 - c2 => x = 2*c2 - c1 - c3
    x_val = r.randint(2, 9)
    c1 = r.randint(1, 6)
    c2 = r.randint(2, 8)
    # 2*c2 - c1 - c3 = x_val => c3 = 2*c2 - c1 - x_val
    c3 = 2 * c2 - c1 - x_val

    t1 = x_sym + c1
    t2 = 2 * x_sym + c2
    t3 = 4 * x_sym + c3

    sol = solution(
        goal="solve for x using constant difference",
        chain_type="equation",
        var="x",
        steps=[
            step(from_expr="T_2 - T_1 = T_3 - T_2",
                 to_expr=f"({to_latex(t2)}) - ({to_latex(t1)}) = ({to_latex(t3)}) - ({to_latex(t2)})",
                 op="equate consecutive differences", rule="common difference property"),
            step(from_expr=f"x + {c2 - c1} = 2x + {c3 - c2}",
                 to_expr=f"x = {x_val}",
                 op="solve linear equation for x", rule="algebra"),
        ],
        final_expr=sp.Integer(x_val),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{The terms }} {to_latex(t1)};\\; {to_latex(t2)};\\; {to_latex(t3)} \\text{{ form an arithmetic sequence. Solve for }} x.",
        answer_expr=sp.Integer(x_val),
        answer_mode="value",
        answer_latex=str(x_val),
        marks=3,
        canonical_solution=sol,
        explanation=f"Since the sequence is arithmetic, $T_2 - T_1 = T_3 - T_2$. Equating and simplifying gives $x = {x_val}$.",
        hint="Use the fact that T_2 - T_1 = T_3 - T_2.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="17_solve_for_variable_in_linear_sequence",
        learning_objective_id=f"{LO}.17_solve_for_variable",
        misconception_tags=["sign_error_subtracting_algebraic_terms", "confuses_T2_minus_T1_with_T1_minus_T2"],
        diagnostic_tags=["sequences", "algebraic_sequences"],
        keywords=["solve for x", "algebraic sequence", "common difference"],
    )
    return _add_pillars(q, "17_solve_for_variable_in_linear_sequence", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 18_find_terms_after_solving_variable
# --------------------------------------------------------------------------- #
def _build_18_find_terms_after_solving_variable(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # 2x - 1, 3x, 5x - 5
    # (3x) - (2x - 1) = x + 1
    # (5x - 5) - 3x = 2x - 5
    # x + 1 = 2x - 5 => x = 6
    x_val = r.randint(3, 8)
    # T1 = x + 2, T2 = 3x - 2, T3 = 4x + (x_val - 6)
    # Let d = 2x - 4 => T2 = T1 + d = 3x - 2. T3 = T2 + d = 5x - 6.
    # But let's construct simply with x:
    t1_val = r.randint(4, 12)
    d_val = r.randint(3, 7)
    t2_val = t1_val + d_val
    t3_val = t1_val + 2 * d_val

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{The sequence }} 2k + 1;\\; 4k - 1;\\; 5k + 2 \\text{{ is arithmetic. Find the numerical value of the first term.}}",
        answer_expr=sp.Integer(9),  # 4k - 1 - (2k + 1) = 2k - 2; 5k + 2 - (4k - 1) = k + 3 => 2k - 2 = k + 3 => k = 5 => 2(5)+1 = 11
        # Let's make it fully dynamic:
        # T2 - T1 = (3k) - (k + a) = 2k - a
        # T3 - T2 = (4k + b) - 3k = k + b
        # 2k - a = k + b => k = a + b
    )
    # Author cleanly with dynamic parameters:
    a_param = r.randint(2, 6)
    b_param = r.randint(1, 5)
    k_res = a_param + b_param
    first_num = k_res + a_param

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{The sequence }} k + {a_param};\\; 3k;\\; 4k + {b_param} \\text{{ is arithmetic. Find the numerical value of the first term.}}",
        answer_expr=sp.Integer(first_num),
        answer_mode="value",
        answer_latex=str(first_num),
        marks=3,
        explanation=f"Set $T_2 - T_1 = T_3 - T_2 \\implies 3k - (k + {a_param}) = (4k + {b_param}) - 3k \\implies 2k - {a_param} = k + {b_param} \\implies k = {k_res}$. First term $= k + {a_param} = {first_num}$.",
        hint="Equate T_2 - T_1 and T_3 - T_2, solve for k, then substitute back into the first term.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="18_find_terms_after_solving_variable",
        learning_objective_id=f"{LO}.18_find_numerical_terms",
        misconception_tags=["stops_at_solving_k", "substitution_into_wrong_term"],
        diagnostic_tags=["sequences", "solve_and_substitute"],
        keywords=["numerical value", "first term", "solve k"],
    )
    return _add_pillars(q, "18_find_terms_after_solving_variable", duration=3, weight=15)


# --------------------------------------------------------------------------- #
# 19_determine_sequence_from_two_given_terms
# --------------------------------------------------------------------------- #
def _build_19_determine_sequence_from_two_given_terms(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(3, 15)
    d = r.randint(3, 8)
    p1 = r.choice([3, 4])
    p2 = r.choice([7, 8, 10])
    v1 = a + (p1 - 1) * d
    v2 = a + (p2 - 1) * d

    sol = solution(
        goal="find common difference from two terms",
        chain_type="equation",
        var="d",
        steps=[
            step(from_expr=f"T_{{{p2}}} - T_{{{p1}}} = ({p2} - {p1})d",
                 to_expr=f"{v2} - {v1} = {p2 - p1}d",
                 op="difference between terms equals index difference times d", rule="arithmetic spacing"),
            step(from_expr=f"{p2 - p1}d = {v2 - v1}",
                 to_expr=f"d = {d}",
                 op="divide by index difference", rule="solve for d"),
        ],
        final_expr=sp.Integer(d),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{In an arithmetic sequence, }} T_{{{p1}}} = {v1} \\text{{ and }} T_{{{p2}}} = {v2}. \\text{{ Find the common difference }} d.",
        answer_expr=sp.Integer(d),
        answer_mode="value",
        answer_latex=str(d),
        marks=2,
        canonical_solution=sol,
        explanation=f"$d = \\dfrac{{T_{{{p2}}} - T_{{{p1}}}}}{{{p2} - {p1}}} = \\dfrac{{{v2} - {v1}}}{{{p2 - p1}}} = {d}$.",
        hint="Use d = (T_m - T_k) / (m - k).",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="19_determine_sequence_from_two_given_terms",
        learning_objective_id=f"{LO}.19_two_terms",
        misconception_tags=["divides_by_index_sum", "subtraction_order_reversal"],
        diagnostic_tags=["sequences", "simultaneous_terms"],
        keywords=["two terms", "common difference", "linear"],
    )
    return _add_pillars(q, "19_determine_sequence_from_two_given_terms", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 20_determine_number_of_terms_in_finite_sequence
# --------------------------------------------------------------------------- #
def _build_20_determine_number_of_terms_in_finite_sequence(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    a = r.randint(4, 16)
    d = r.randint(3, 8)
    n_terms = r.randint(18, 45)
    last_term = a + (n_terms - 1) * d
    seq_prompt = f"{a};\\; {a + d};\\; {a + 2*d}; \\ldots ;\\; {last_term}"

    sol = solution(
        goal="determine number of terms in finite sequence",
        chain_type="equation",
        var="n",
        steps=[
            step(from_expr="T_n = a + (n - 1)d", to_expr=f"{last_term} = {a} + (n - 1)({d})", op="equate last term to formula", rule="general term"),
            step(from_expr=f"(n - 1)({d}) = {last_term - a}", to_expr=f"n - 1 = {n_terms - 1}", op="divide by d", rule="solve for n"),
            step(from_expr=f"n - 1 = {n_terms - 1}", to_expr=f"n = {n_terms}", op="add 1", rule="count terms"),
        ],
        final_expr=sp.Integer(n_terms),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{How many terms are in the finite arithmetic sequence: }} {seq_prompt}?",
        answer_expr=sp.Integer(n_terms),
        answer_mode="value",
        answer_latex=str(n_terms),
        marks=2,
        canonical_solution=sol,
        explanation=f"Set $T_n = {last_term} \\implies {a} + (n - 1)({d}) = {last_term} \\implies n = {n_terms}$.",
        hint="Equate the last term to T_n = a + (n - 1)d and solve for n.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="20_determine_number_of_terms_in_finite_sequence",
        learning_objective_id=f"{LO}.20_finite_sequence_count",
        misconception_tags=["off_by_one_count", "divides_last_term_by_d_directly"],
        diagnostic_tags=["sequences", "number_of_terms"],
        keywords=["number of terms", "finite sequence", "last term"],
    )
    return _add_pillars(q, "20_determine_number_of_terms_in_finite_sequence", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 21_arithmetic_mean_between_two_numbers
# --------------------------------------------------------------------------- #
def _build_21_arithmetic_mean_between_two_numbers(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    n1 = r.randint(10, 40)
    diff = 2 * r.randint(3, 15)  # ensure even difference for integer mean
    n2 = n1 + diff
    mean_val = (n1 + n2) // 2

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Find the arithmetic mean between }} {n1} \\text{{ and }} {n2}.",
        answer_expr=sp.Integer(mean_val),
        answer_mode="value",
        answer_latex=str(mean_val),
        marks=1,
        explanation=f"Arithmetic mean $= \\dfrac{{{n1} + {n2}}}{{2}} = \\dfrac{{{n1 + n2}}}{{2}} = {mean_val}$.",
        hint="Add the two numbers together and divide by 2.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="21_arithmetic_mean_between_two_numbers",
        learning_objective_id=f"{LO}.21_arithmetic_mean",
        misconception_tags=["subtracts_numbers", "forgets_division_by_two"],
        diagnostic_tags=["sequences", "arithmetic_mean"],
        keywords=["arithmetic mean", "average", "linear"],
    )
    return _add_pillars(q, "21_arithmetic_mean_between_two_numbers", duration=1, weight=15)


# --------------------------------------------------------------------------- #
# 22_insert_multiple_arithmetic_means
# --------------------------------------------------------------------------- #
def _build_22_insert_multiple_arithmetic_means(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # Insert 2 arithmetic means between start and end => 4 terms total
    start = r.randint(5, 20)
    d = r.randint(3, 9)
    m1 = start + d
    m2 = start + 2 * d
    end = start + 3 * d

    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Insert two arithmetic means between }} {start} \\text{{ and }} {end}. \\text{{ State the two inserted numbers (separated by a semicolon).}}",
        answer_expr=f"{m1}; {m2}",
        answer_mode="expression",
        marks=2,
        explanation=f"With 2 inserted means, there are 4 terms: $T_1 = {start}$ and $T_4 = {end}$. $3d = {end} - {start} = {end - start} \\implies d = {d}$. The means are ${m1};\\; {m2}$.",
        hint="With 2 means, the end term is T_4, so 3d = end - start.",
    )
    with_metadata(
        q,
        topic=TOPIC,
        subskill="22_insert_multiple_arithmetic_means",
        learning_objective_id=f"{LO}.22_insert_means",
        misconception_tags=["divides_by_two_instead_of_three", "spacing_error"],
        diagnostic_tags=["sequences", "insert_means"],
        keywords=["insert arithmetic means", "intermediate terms", "linear spacing"],
    )
    return _add_pillars(q, "22_insert_multiple_arithmetic_means", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 23_matchstick_squares_visual_pattern
# --------------------------------------------------------------------------- #
def _build_23_matchstick_squares_visual_pattern(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # 1 square = 4 matches, 2 squares = 7, 3 squares = 10 -> T_n = 3n + 1
    pattern_n = r.choice([8, 10, 12, 15])
    ans_matches = 3 * pattern_n + 1

    svg = f"""<svg viewBox="0 0 520 120" width="100%" height="120" xmlns="http://www.w3.org/2000/svg">
  <!-- Target: Figure {pattern_n} -->
  <g stroke="#1E293B" stroke-width="4" stroke-linecap="round">
    <!-- Figure 1: 1 square (4 matches) -->
    <line x1="20" y1="20" x2="60" y2="20" />
    <line x1="60" y1="20" x2="60" y2="60" />
    <line x1="60" y1="60" x2="20" y2="60" />
    <line x1="20" y1="60" x2="20" y2="20" />
    <text x="40" y="90" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#475569" stroke="none">Fig. 1 (4)</text>

    <!-- Figure 2: 2 squares (7 matches) -->
    <line x1="120" y1="20" x2="160" y2="20" />
    <line x1="160" y1="20" x2="200" y2="20" />
    <line x1="200" y1="20" x2="200" y2="60" />
    <line x1="200" y1="60" x2="160" y2="60" />
    <line x1="160" y1="60" x2="120" y2="60" />
    <line x1="120" y1="60" x2="120" y2="20" />
    <line x1="160" y1="20" x2="160" y2="60" />
    <text x="160" y="90" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#475569" stroke="none">Fig. 2 (7)</text>

    <!-- Figure 3: 3 squares (10 matches) -->
    <line x1="260" y1="20" x2="300" y2="20" />
    <line x1="300" y1="20" x2="340" y2="20" />
    <line x1="340" y1="20" x2="380" y2="20" />
    <line x1="380" y1="20" x2="380" y2="60" />
    <line x1="380" y1="60" x2="340" y2="60" />
    <line x1="340" y1="60" x2="300" y2="60" />
    <line x1="300" y1="60" x2="260" y2="60" />
    <line x1="260" y1="60" x2="260" y2="20" />
    <line x1="300" y1="20" x2="300" y2="60" />
    <line x1="340" y1="20" x2="340" y2="60" />
    <text x="320" y="90" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#475569" stroke="none">Fig. 3 (10)</text>
    <text x="450" y="45" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#0284C7" stroke="none">Fig. {pattern_n} = ?</text>
  </g>
</svg>"""

    sol = solution(
        goal=f"calculate matches in figure {pattern_n}",
        chain_type="equation",
        var="T_n",
        steps=[
            step(from_expr="T_1 = 4, \\; T_2 = 7, \\; T_3 = 10", to_expr="d = 3", op="find common difference from figures", rule="pattern inspection"),
            step(from_expr="T_n = 3n + 1", to_expr=f"T_{{{pattern_n}}} = 3({pattern_n}) + 1", op="substitute figure number", rule="formula"),
            step(from_expr=f"T_{{{pattern_n}}} = {3 * pattern_n} + 1", to_expr=f"T_{{{pattern_n}}} = {ans_matches}", op="evaluate", rule="arithmetic"),
        ],
        final_expr=sp.Integer(ans_matches),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{The sequence of matchstick squares below follows the pattern: }} 4;\\; 7;\\; 10; \\ldots \\text{{ How many matchsticks are needed for Figure }} {pattern_n}?",
        answer_expr=sp.Integer(ans_matches),
        answer_mode="value",
        answer_latex=str(ans_matches),
        marks=2,
        canonical_solution=sol,
        explanation=f"First term $a = 4$ and common difference $d = 3$. General formula: $T_n = 3n + 1$. For Figure {pattern_n}: $T_{{{pattern_n}}} = 3({pattern_n}) + 1 = {ans_matches}$ matchsticks.",
        hint="Each additional square adds 3 matchsticks (since they share sides). T_n = 3n + 1.",
    )
    q["diagram_spec"] = {"kind": "inline_svg", "svg": svg}
    with_metadata(
        q,
        topic=TOPIC,
        subskill="23_matchstick_squares_visual_pattern",
        learning_objective_id=f"{LO}.23_matchstick_squares",
        misconception_tags=["multiplies_squares_by_four_ignoring_shared_sides", "off_by_one_match"],
        diagnostic_tags=["visual_patterns", "matchsticks"],
        keywords=["matchsticks", "squares", "visual pattern", "3n + 1"],
    )
    return _add_pillars(q, "23_matchstick_squares_visual_pattern", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 24_matchstick_triangles_visual_pattern
# --------------------------------------------------------------------------- #
def _build_24_matchstick_triangles_visual_pattern(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # 1 triangle = 3 matches, 2 triangles = 5 matches, 3 triangles = 7 matches -> T_n = 2n + 1
    pattern_n = r.choice([10, 15, 20, 25])
    ans_matches = 2 * pattern_n + 1

    svg = f"""<svg viewBox="0 0 520 120" width="100%" height="120" xmlns="http://www.w3.org/2000/svg">
  <!-- Target: Figure {pattern_n} -->
  <g stroke="#1E293B" stroke-width="4" stroke-linecap="round">
    <!-- Fig 1: 1 triangle -->
    <line x1="20" y1="60" x2="60" y2="60" />
    <line x1="20" y1="60" x2="40" y2="20" />
    <line x1="60" y1="60" x2="40" y2="20" />
    <text x="40" y="90" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#475569" stroke="none">Fig. 1 (3)</text>

    <!-- Fig 2: 2 triangles sharing side -->
    <line x1="110" y1="60" x2="150" y2="60" />
    <line x1="150" y1="60" x2="190" y2="60" />
    <line x1="110" y1="60" x2="130" y2="20" />
    <line x1="150" y1="60" x2="130" y2="20" />
    <line x1="150" y1="60" x2="170" y2="20" />
    <line x1="190" y1="60" x2="170" y2="20" />
    <text x="150" y="90" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#475569" stroke="none">Fig. 2 (5)</text>

    <!-- Fig 3: 3 triangles -->
    <line x1="240" y1="60" x2="280" y2="60" />
    <line x1="280" y1="60" x2="320" y2="60" />
    <line x1="320" y1="60" x2="360" y2="60" />
    <line x1="240" y1="60" x2="260" y2="20" />
    <line x1="280" y1="60" x2="260" y2="20" />
    <line x1="280" y1="60" x2="300" y2="20" />
    <line x1="320" y1="60" x2="300" y2="20" />
    <line x1="320" y1="60" x2="340" y2="20" />
    <line x1="360" y1="60" x2="340" y2="20" />
    <text x="300" y="90" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#475569" stroke="none">Fig. 3 (7)</text>
    <text x="440" y="45" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#0284C7" stroke="none">Fig. {pattern_n} = ?</text>
  </g>
</svg>"""

    sol = solution(
        goal=f"calculate matches for {pattern_n} triangles",
        chain_type="equation",
        var="T_n",
        steps=[
            step(from_expr="T_1 = 3, \\; T_2 = 5, \\; T_3 = 7", to_expr="d = 2", op="observe common difference", rule="linear growth"),
            step(from_expr="T_n = 2n + 1", to_expr=f"T_{{{pattern_n}}} = 2({pattern_n}) + 1", op="substitute into formula", rule="evaluation"),
            step(from_expr=f"T_{{{pattern_n}}} = {2 * pattern_n} + 1", to_expr=f"T_{{{pattern_n}}} = {ans_matches}", op="evaluate", rule="arithmetic"),
        ],
        final_expr=sp.Integer(ans_matches),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{The visual sequence displays joined matchstick triangles: }} 3;\\; 5;\\; 7; \\ldots \\text{{ How many matchsticks make up Figure }} {pattern_n}?",
        answer_expr=sp.Integer(ans_matches),
        answer_mode="value",
        answer_latex=str(ans_matches),
        marks=2,
        canonical_solution=sol,
        explanation=f"Formula is $T_n = 2n + 1$. For Figure {pattern_n}: $T_{{{pattern_n}}} = 2({pattern_n}) + 1 = {ans_matches}$ matchsticks.",
        hint="Starting at 3, each additional triangle adds 2 matchsticks: T_n = 2n + 1.",
    )
    q["diagram_spec"] = {"kind": "inline_svg", "svg": svg}
    with_metadata(
        q,
        topic=TOPIC,
        subskill="24_matchstick_triangles_visual_pattern",
        learning_objective_id=f"{LO}.24_matchstick_triangles",
        misconception_tags=["multiplies_by_three", "off_by_one_triangle"],
        diagnostic_tags=["visual_patterns", "triangles"],
        keywords=["matchstick triangles", "2n + 1", "visual sequence"],
    )
    return _add_pillars(q, "24_matchstick_triangles_visual_pattern", duration=2, weight=15)


# --------------------------------------------------------------------------- #
# 25_table_seating_arrangement_visual_pattern
# --------------------------------------------------------------------------- #
def _build_25_table_seating_arrangement_visual_pattern(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    # 1 table = 4 seats, 2 tables = 6 seats, 3 tables = 8 seats -> T_n = 2n + 2
    num_tables = r.choice([10, 14, 18, 22])
    ans_seats = 2 * num_tables + 2

    svg = f"""<svg viewBox="0 0 520 120" width="100%" height="120" xmlns="http://www.w3.org/2000/svg">
  <!-- Target: {num_tables} tables -->
  <g fill="#0284C7" stroke="#0F172A" stroke-width="2">
    <!-- 1 table (4 seats) -->
    <rect x="30" y="30" width="40" height="40" fill="#E2E8F0" />
    <circle cx="50" cy="18" r="6" />
    <circle cx="50" cy="82" r="6" />
    <circle cx="18" cy="50" r="6" />
    <circle cx="82" cy="50" r="6" />
    <text x="50" y="105" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#475569" stroke="none">1 Table (4)</text>

    <!-- 2 tables joined (6 seats) -->
    <rect x="130" y="30" width="80" height="40" fill="#E2E8F0" />
    <line x1="170" y1="30" x2="170" y2="70" stroke="#94A3B8" />
    <circle cx="150" cy="18" r="6" />
    <circle cx="190" cy="18" r="6" />
    <circle cx="150" cy="82" r="6" />
    <circle cx="190" cy="82" r="6" />
    <circle cx="118" cy="50" r="6" />
    <circle cx="222" cy="50" r="6" />
    <text x="170" y="105" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#475569" stroke="none">2 Tables (6)</text>

    <!-- 3 tables joined (8 seats) -->
    <rect x="270" y="30" width="120" height="40" fill="#E2E8F0" />
    <line x1="310" y1="30" x2="310" y2="70" stroke="#94A3B8" />
    <line x1="350" y1="30" x2="350" y2="70" stroke="#94A3B8" />
    <circle cx="290" cy="18" r="6" />
    <circle cx="330" cy="18" r="6" />
    <circle cx="370" cy="18" r="6" />
    <circle cx="290" cy="82" r="6" />
    <circle cx="330" cy="82" r="6" />
    <circle cx="370" cy="82" r="6" />
    <circle cx="258" cy="50" r="6" />
    <circle cx="402" cy="50" r="6" />
    <text x="330" y="105" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#475569" stroke="none">3 Tables (8)</text>
    <text x="460" y="55" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#0284C7" stroke="none">{num_tables} Tables = ?</text>
  </g>
</svg>"""

    sol = solution(
        goal=f"calculate seats for {num_tables} tables",
        chain_type="equation",
        var="T_n",
        steps=[
            step(from_expr="T_1 = 4, \\; T_2 = 6, \\; T_3 = 8", to_expr="d = 2", op="find common difference from arrangement", rule="linear growth"),
            step(from_expr="T_n = 2n + 2", to_expr=f"T_{{{num_tables}}} = 2({num_tables}) + 2", op="substitute number of tables", rule="formula"),
            step(from_expr=f"T_{{{num_tables}}} = {2 * num_tables} + 2", to_expr=f"T_{{{num_tables}}} = {ans_seats}", op="evaluate", rule="arithmetic"),
        ],
        final_expr=sp.Integer(ans_seats),
    )
    q = make_short(
        prefix=TOPIC,
        prompt_latex=f"\\text{{Square tables are joined in a line. Each side seats 1 person. How many people can sit around }} {num_tables} \\text{{ joined tables?}}",
        answer_expr=sp.Integer(ans_seats),
        answer_mode="value",
        answer_latex=str(ans_seats),
        marks=2,
        canonical_solution=sol,
        explanation=f"Each table has 2 seats (top and bottom) plus 2 end seats: $T_n = 2n + 2$. For $n = {num_tables}$: $T_{{{num_tables}}} = 2({num_tables}) + 2 = {ans_seats}$ people.",
        hint="Each table provides 2 seats along its sides, and the two ends provide 1 seat each: 2n + 2.",
    )
    q["diagram_spec"] = {"kind": "inline_svg", "svg": svg}
    with_metadata(
        q,
        topic=TOPIC,
        subskill="25_table_seating_arrangement_visual_pattern",
        learning_objective_id=f"{LO}.25_table_seating",
        misconception_tags=["multiplies_tables_by_four", "forgets_end_seats"],
        diagnostic_tags=["visual_patterns", "table_seating"],
        keywords=["table seating", "joined tables", "2n + 2", "visual pattern"],
    )
    return _add_pillars(q, "25_table_seating_arrangement_visual_pattern", duration=2, weight=15)


BUILDERS_01_25: Dict[str, Any] = {
    "01_identify_linear_vs_non_linear_sequence": _build_01_identify_linear_vs_non_linear_sequence,
    "02_find_next_terms_positive_difference": _build_02_find_next_terms_positive_difference,
    "03_find_next_terms_negative_difference": _build_03_find_next_terms_negative_difference,
    "04_find_next_terms_fractional_difference": _build_04_find_next_terms_fractional_difference,
    "05_calculate_common_difference_integers": _build_05_calculate_common_difference_integers,
    "06_calculate_common_difference_negative": _build_06_calculate_common_difference_negative,
    "07_calculate_common_difference_fractions": _build_07_calculate_common_difference_fractions,
    "08_determine_general_term_positive_diff": _build_08_determine_general_term_positive_diff,
    "09_determine_general_term_negative_diff": _build_09_determine_general_term_negative_diff,
    "10_determine_general_term_fractional": _build_10_determine_general_term_fractional,
    "11_calculate_specific_term_from_formula": _build_11_calculate_specific_term_from_formula,
    "12_calculate_specific_term_from_sequence": _build_12_calculate_specific_term_from_sequence,
    "13_find_term_position_given_value": _build_13_find_term_position_given_value,
    "14_test_if_number_is_term_of_sequence": _build_14_test_if_number_is_term_of_sequence,
    "15_first_negative_term_of_decreasing_sequence": _build_15_first_negative_term_of_decreasing_sequence,
    "16_first_term_exceeding_given_value": _build_16_first_term_exceeding_given_value,
    "17_solve_for_variable_in_linear_sequence": _build_17_solve_for_variable_in_linear_sequence,
    "18_find_terms_after_solving_variable": _build_18_find_terms_after_solving_variable,
    "19_determine_sequence_from_two_given_terms": _build_19_determine_sequence_from_two_given_terms,
    "20_determine_number_of_terms_in_finite_sequence": _build_20_determine_number_of_terms_in_finite_sequence,
    "21_arithmetic_mean_between_two_numbers": _build_21_arithmetic_mean_between_two_numbers,
    "22_insert_multiple_arithmetic_means": _build_22_insert_multiple_arithmetic_means,
    "23_matchstick_squares_visual_pattern": _build_23_matchstick_squares_visual_pattern,
    "24_matchstick_triangles_visual_pattern": _build_24_matchstick_triangles_visual_pattern,
    "25_table_seating_arrangement_visual_pattern": _build_25_table_seating_arrangement_visual_pattern,
}
