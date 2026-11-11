"""Grade 9 Mathematics - Patterns Archetypes 01 to 25.
Grounded in curriculum_docs_auto/Mathematics_Gr9/Term 1/04. Patterns.md:
Linear numeric sequences, common difference, general term Tn = dn + c,
term values, term positions, matchstick patterns, geometric sequences, and special number sequences.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .patterns_svg import (
    draw_matchstick_squares_svg,
    draw_matchstick_triangles_svg,
)


# ----------------------------------------------------------------------
# 01. Linear Sequence: Constant Difference Positive
# ----------------------------------------------------------------------
def arch_01_linear_sequence_constant_difference_positive(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 6, 7, 8])
    c = rng.randint(-9, 12)
    t1 = d * 1 + c
    t2 = d * 2 + c
    t3 = d * 3 + c
    t4 = d * 4 + c

    sign_c = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
    ans = f"{d}n {sign_c}".strip()

    prompt = (
        f"Consider the arithmetic number sequence:\n\n"
        f"\\[ {t1};\\ {t2};\\ {t3};\\ {t4};\\ \\dots \\]\n\n"
        f"Determine the general term rule (\\(T_n\\)) in terms of \\(n\\)."
    )
    sol = (
        f"**Linear Sequence Formula:**\n"
        f"1. Common difference: \\(d = T_2 - T_1 = {t2} - ({t1}) = {d}\\).\n"
        f"2. General form: \\(T_n = dn + c\\).\n"
        f"3. Using \\(T_1\\): \\({d}(1) + c = {t1} \\implies c = {t1} - {d} = {c}\\).\n"
        f"Therefore: \\(T_n = {ans}\\)."
    )
    return {
        "id": f"g9_pat_lin_pos_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Determine constant difference d = {d}", "marks": 1},
            {"desc": f"State correct general formula T_n = {ans}", "marks": 1},
        ],
        "hints": [
            "Find the difference between successive terms: d = T2 - T1.",
            "Write the rule in the form Tn = dn + c, where c = T1 - d.",
            f"Rule: Tn = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 02. Linear Sequence: Constant Difference Negative
# ----------------------------------------------------------------------
def arch_02_linear_sequence_constant_difference_negative(rng: random.Random) -> Dict[str, Any]:
    d = -rng.choice([3, 4, 5, 6, 7])
    c = rng.randint(35, 75)
    t1 = d * 1 + c
    t2 = d * 2 + c
    t3 = d * 3 + c
    t4 = d * 4 + c

    ans = f"{d}n + {c}"
    prompt = (
        f"Consider the decreasing linear sequence:\n\n"
        f"\\[ {t1};\\ {t2};\\ {t3};\\ {t4};\\ \\dots \\]\n\n"
        f"Determine the general term formula \\(T_n\\)."
    )
    sol = (
        f"**Decreasing Sequence Rule:**\n"
        f"1. Common difference: \\(d = {t2} - {t1} = {d}\\).\n"
        f"2. Constant term: \\(c = T_1 - d = {t1} - ({d}) = {c}\\).\n"
        f"Result: \\(T_n = {ans}\\)."
    )
    return {
        "id": f"g9_pat_lin_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Find negative difference d = {d}", "marks": 1},
            {"desc": f"State general formula T_n = {ans}", "marks": 1},
        ],
        "hints": [
            "Because the sequence decreases, the difference is negative.",
            f"Difference is {d}.",
            f"Formula: Tn = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 03. Linear Sequence: Calculate Specific Terms T10 and T50
# ----------------------------------------------------------------------
def arch_03_linear_sequence_calculate_specific_term_t10_t50(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 6])
    c = rng.choice([-5, -2, 1, 4, 7])
    t_idx1 = 10
    t_idx2 = 50
    v1 = d * t_idx1 + c
    v2 = d * t_idx2 + c

    sign_c = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
    rule_str = f"T_n = {d}n {sign_c}".strip()

    prompt = (
        f"A linear pattern has the general term \\({rule_str}\\).\n\n"
        f"Calculate the value of:\n"
        f"1. The 10th term (\\(T_{{10}}\\))\n"
        f"2. The 50th term (\\(T_{{50}}\\))"
    )
    sol = (
        f"**Substituting Position Values:**\n"
        f"1. \\(T_{{10}} = {d}(10) {sign_c} = {v1}\\).\n"
        f"2. \\(T_{{50}} = {d}(50) {sign_c} = {v2}\\)."
    )
    return {
        "id": f"g9_pat_calc_terms_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"T_10 = {v1}; T_50 = {v2}",
        "expected_answer": f"T_10 = {v1}; T_50 = {v2}",
        "sample_answer": f"T_10 = {v1}; T_50 = {v2}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Substitute n = 10 to obtain {v1}", "marks": 1},
            {"desc": f"Substitute n = 50 to obtain {v2}", "marks": 1},
        ],
        "hints": [
            "Substitute n = 10 into the formula.",
            "Substitute n = 50 into the formula.",
            f"Results: {v1} and {v2}.",
        ],
    }


# ----------------------------------------------------------------------
# 04. Linear Sequence: Find Term Position Given Value
# ----------------------------------------------------------------------
def arch_04_linear_sequence_find_term_position_given_value(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([4, 5, 6, 7])
    c = rng.choice([-3, -1, 2, 5])
    n_target = rng.choice([24, 35, 42, 55])
    val_target = d * n_target + c

    sign_c = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
    rule_str = f"T_n = {d}n {sign_c}".strip()

    prompt = (
        f"The general term of a sequence is given by \\({rule_str}\\).\n\n"
        f"Which term of the sequence is equal to \\({val_target}\\)? (Find \\(n\\))."
    )
    sol = (
        f"**Solving for Position \\(n\\):**\n"
        f"Set \\(T_n = {val_target}\\):\n"
        f"\\[ {d}n {sign_c} = {val_target} \\]\n"
        f"\\[ {d}n = {val_target - c} \\implies n = \\frac{{{val_target - c}}}{{{d}}} = {n_target} \\]\n"
        f"The {n_target}th term equals {val_target}."
    )
    return {
        "id": f"g9_pat_find_pos_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(n_target),
        "expected_answer": str(n_target),
        "sample_answer": str(n_target),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Set up equation {d}n {sign_c} = {val_target}", "marks": 1},
            {"desc": f"Solve for n = {n_target}", "marks": 1},
        ],
        "hints": [
            f"Set {rule_str} = {val_target}.",
            "Solve the linear equation for n.",
            f"n = {n_target}.",
        ],
    }


# ----------------------------------------------------------------------
# 05. Linear Sequence: Fractional Terms Common Difference
# ----------------------------------------------------------------------
def arch_05_linear_sequence_fractional_terms_common_difference(rng: random.Random) -> Dict[str, Any]:
    # e.g., 1/4, 3/4, 5/4, 7/4... d = 2/4 = 1/2
    # Tn = (2n - 1) / 4
    den = rng.choice([3, 4, 5])
    d_num = rng.choice([1, 2])
    t1_num = rng.choice([1, 2])

    t1_str = f"\\frac{{{t1_num}}}{{{den}}}"
    t2_str = f"\\frac{{{t1_num + d_num}}}{{{den}}}"
    t3_str = f"\\frac{{{t1_num + 2*d_num}}}{{{den}}}"
    diff_str = f"\\frac{{{d_num}}}{{{den}}}"

    prompt = (
        f"Determine the constant common difference (\\(d\\)) and the 5th term (\\(T_5\\)) "
        f"of the fractional sequence:\n\n"
        f"\\[ {t1_str};\\ {t2_str};\\ {t3_str};\\ \\dots \\]"
    )
    t5_num = t1_num + 4 * d_num
    t5_str = f"\\frac{{{t5_num}}}{{{den}}}"
    sol = (
        f"**Fractional Sequence:**\n"
        f"1. Common difference: \\(d = {t2_str} - {t1_str} = {diff_str}\\).\n"
        f"2. 5th term: \\(T_5 = {t1_str} + 4 \\times \\left({diff_str}\\right) = {t5_str}\\)."
    )
    return {
        "id": f"g9_pat_frac_seq_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"d = {diff_str}; T_5 = {t5_str}",
        "expected_answer": f"d = {diff_str}; T_5 = {t5_str}",
        "sample_answer": f"d = {diff_str}; T_5 = {t5_str}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State common difference d = {diff_str}", "marks": 1},
            {"desc": f"Calculate 5th term T_5 = {t5_str}", "marks": 1},
        ],
        "hints": [
            "Subtract the first fraction from the second.",
            f"Add 4 times the common difference to T1.",
            f"Results: d = {diff_str} and T5 = {t5_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 06. Linear Sequence: Decimal Terms Step
# ----------------------------------------------------------------------
def arch_06_linear_sequence_decimal_terms_step(rng: random.Random) -> Dict[str, Any]:
    step = rng.choice([0.4, 0.6, 0.7, 0.8])
    start = round(rng.choice([1.2, 1.5, 2.1]), 1)
    terms = [round(start + i * step, 1) for i in range(4)]

    s_str = "; ".join(f"{x:.1f}".replace(".", ",") for x in terms)
    diff_str = f"{step:.1f}".replace(".", ",")
    t10 = round(start + 9 * step, 1)
    t10_str = f"{t10:.1f}".replace(".", ",")

    prompt = (
        f"For the decimal number pattern:\n\n"
        f"\\[ {s_str};\\ \\dots \\]\n\n"
        f"1. State the constant step (common difference).\n"
        f"2. Calculate the 10th term (\\(T_{{10}}\\))."
    )
    sol = (
        f"**Decimal Pattern Steps:**\n"
        f"1. Step: \\(d = {terms[1]:.1f} - {terms[0]:.1f} = {diff_str}\\).\n"
        f"2. \\(T_{{10}} = {terms[0]:.1f} + 9 \\times {diff_str} = {t10_str}\\)."
    )
    return {
        "id": f"g9_pat_dec_step_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"d = {diff_str}; T_10 = {t10_str}",
        "expected_answer": f"d = {diff_str}; T_10 = {t10_str}",
        "sample_answer": f"d = {diff_str}; T_10 = {t10_str}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State common difference d = {diff_str}", "marks": 1},
            {"desc": f"Calculate T_10 = {t10_str}", "marks": 1},
        ],
        "hints": [
            "Find the step by subtracting consecutive terms.",
            "T10 = T1 + 9 * d.",
            f"Answers: d = {diff_str} and T10 = {t10_str}.",
        ],
    }


# ----------------------------------------------------------------------
# 07. Matchstick Square Pattern Formula Derivation
# ----------------------------------------------------------------------
def arch_07_matchstick_square_pattern_formula_derivation(rng: random.Random) -> Dict[str, Any]:
    svg = draw_matchstick_squares_svg(stages=3, seed=rng.randint(1, 9999))
    ans = "3n + 1"

    prompt = (
        f"Consider the sequence of linked matchstick squares shown below.\n\n"
        f"Stage 1 requires 4 sticks, Stage 2 requires 7 sticks, and Stage 3 requires 10 sticks.\n\n"
        f"Write down the general formula \\(T_n\\) for the number of matchsticks required for Stage \\(n\\)."
    )
    sol = (
        f"**Deriving Matchstick Formula:**\n"
        f"Terms: \\(4;\\ 7;\\ 10;\\ \\dots\\)\n"
        f"1. Common difference: \\(d = 7 - 4 = 3\\) (each new square shares 1 side and adds 3 sticks).\n"
        f"2. Constant: \\(c = 4 - 3 = 1\\).\n"
        f"General formula: \\(T_n = {ans}\\)."
    )
    return {
        "id": f"g9_pat_match_sq_rule_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify difference of 3 sticks per square", "marks": 1},
            {"desc": f"State general formula T_n = {ans}", "marks": 1},
        ],
        "hints": [
            "Each additional square adds 3 matchsticks.",
            "Use Tn = dn + c.",
            f"Rule: Tn = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 08. Matchstick Triangle Pattern Formula Derivation
# ----------------------------------------------------------------------
def arch_08_matchstick_triangle_pattern_formula_derivation(rng: random.Random) -> Dict[str, Any]:
    svg = draw_matchstick_triangles_svg(stages=3, seed=rng.randint(1, 9999))
    ans = "2n + 1"

    prompt = (
        f"Consider the row of linked matchstick triangles shown below.\n\n"
        f"Stage 1 has 3 sticks, Stage 2 has 5 sticks, and Stage 3 has 7 sticks.\n\n"
        f"Derive the general formula \\(T_n\\) for the total number of matchsticks in Stage \\(n\\)."
    )
    sol = (
        f"**Triangle Pattern Formula:**\n"
        f"Terms: \\(3;\\ 5;\\ 7;\\ \\dots\\)\n"
        f"1. Common difference: \\(d = 5 - 3 = 2\\).\n"
        f"2. Constant term: \\(c = 3 - 2 = 1\\).\n"
        f"General formula: \\(T_n = {ans}\\)."
    )
    return {
        "id": f"g9_pat_match_tri_rule_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marks": 2,
        "marking_schema": [
            {"desc": "Identify difference d = 2", "marks": 1},
            {"desc": f"State formula T_n = {ans}", "marks": 1},
        ],
        "hints": [
            "Notice each added triangle requires 2 more sticks.",
            "Initial triangle has 3 sticks.",
            f"Formula: Tn = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 09. Matchstick Pattern: Total Sticks for Stage k
# ----------------------------------------------------------------------
def arch_09_matchstick_pattern_total_sticks_for_stage_k(rng: random.Random) -> Dict[str, Any]:
    # e.g., squares: Tn = 3n + 1
    stage_k = rng.choice([25, 30, 45, 60])
    ans = 3 * stage_k + 1

    prompt = (
        f"A pattern of linked squares formed by matchsticks follows the rule \\(T_n = 3n + 1\\).\n\n"
        f"How many matchsticks are needed to build a row of **{stage_k}** squares?"
    )
    sol = (
        f"**Substitution:**\n"
        f"\\[ T_{{{stage_k}}} = 3({stage_k}) + 1 = {3 * stage_k} + 1 = {ans} \\]"
    )
    return {
        "id": f"g9_pat_match_stage_k_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "expected_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Substitute n = {stage_k} to obtain {ans}", "marks": 1},
        ],
        "hints": [
            f"Multiply {stage_k} by 3 and add 1.",
            f"Total matchsticks: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 10. Matchstick Pattern: Determine Stage from Total Sticks
# ----------------------------------------------------------------------
def arch_10_matchstick_pattern_determine_stage_from_total_sticks(rng: random.Random) -> Dict[str, Any]:
    # Tn = 3n + 1
    n_squares = rng.choice([40, 55, 65, 80])
    tot_sticks = 3 * n_squares + 1

    prompt = (
        f"A builder uses a box containing exactly **{tot_sticks}** matchsticks to create a single row "
        f"of linked squares following the rule \\(T_n = 3n + 1\\).\n\n"
        f"How many squares did the builder construct?"
    )
    sol = (
        f"**Inverse Problem:**\n"
        f"\\[ 3n + 1 = {tot_sticks} \\]\n"
        f"\\[ 3n = {tot_sticks - 1} \\implies n = \\frac{{{tot_sticks - 1}}}{{3}} = {n_squares} \\]"
    )
    return {
        "id": f"g9_pat_match_find_stage_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(n_squares),
        "expected_answer": str(n_squares),
        "sample_answer": str(n_squares),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Set 3n + 1 = {tot_sticks}", "marks": 1},
            {"desc": f"Solve to get n = {n_squares} squares", "marks": 1},
        ],
        "hints": [
            f"Subtract 1 from {tot_sticks}.",
            "Divide by 3 to find n.",
            f"Answer: {n_squares} squares.",
        ],
    }


# ----------------------------------------------------------------------
# 11. Tile Paving Border Pattern Formula
# ----------------------------------------------------------------------
def arch_11_tile_paving_border_pattern_formula(rng: random.Random) -> Dict[str, Any]:
    # A square pond of n x n blue tiles is surrounded by a single border of white tiles.
    # Total border tiles = (n + 2)^2 - n^2 = 4n + 4
    ans = "4n + 4"
    n_test = rng.choice([6, 8, 10])
    ans_test = 4 * n_test + 4

    prompt = (
        f"A square garden pond of size \\(n \\times n\\) is bordered by a single row of paving stones.\n\n"
        f"Stage 1 (\\(1 \\times 1\\)) has 8 border stones; Stage 2 (\\(2 \\times 2\\)) has 12 border stones; "
        f"Stage 3 (\\(3 \\times 3\\)) has 16 border stones.\n\n"
        f"1. Derive the general formula for the number of border stones (\\(B_n\\)) in terms of \\(n\\).\n"
        f"2. Calculate the number of border stones required for a pond of size \\({n_test} \\times {n_test}\\)."
    )
    sol = (
        f"**Paving Border Analysis:**\n"
        f"Terms: \\(8;\\ 12;\\ 16;\\ \\dots\\)\n"
        f"1. Constant difference \\(d = 12 - 8 = 4\\).\n"
        f"2. \\(c = 8 - 4 = 4\\).\n"
        f"Formula: \\(B_n = {ans}\\).\n"
        f"For \\(n = {n_test}\\): \\(B_{{{n_test}}} = 4({n_test}) + 4 = {ans_test}\\)."
    )
    return {
        "id": f"g9_pat_tile_border_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"B_n = {ans}; B_{n_test} = {ans_test}",
        "expected_answer": f"B_n = {ans}; B_{n_test} = {ans_test}",
        "sample_answer": f"B_n = {ans}; B_{n_test} = {ans_test}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "marking_schema": [
            {"desc": f"Derive formula B_n = {ans}", "marks": 2},
            {"desc": f"Evaluate for n = {n_test} to get {ans_test}", "marks": 1},
        ],
        "hints": [
            "Notice the terms increase by 4 each stage.",
            f"Use Bn = 4n + 4.",
            f"Results: {ans} and {ans_test}.",
        ],
    }


# ----------------------------------------------------------------------
# 12. Geometric Sequence: Constant Ratio Integer
# ----------------------------------------------------------------------
def arch_12_geometric_sequence_constant_ratio_integer(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    r_val = rng.choice([2, 3])
    terms = [a * (r_val ** i) for i in range(4)]
    next_term = a * (r_val ** 4)

    terms_str = "; ".join(str(x) for x in terms)
    prompt = (
        f"Consider the geometric pattern:\n\n"
        f"\\[ {terms_str};\\ \\dots \\]\n\n"
        f"1. Identify the constant common ratio (\\(r\\)).\n"
        f"2. Write down the next term (\\(T_5\\))."
    )
    sol = (
        f"**Geometric Sequence Analysis:**\n"
        f"1. Common ratio: \\(r = \\frac{{T_2}}{{T_1}} = \\frac{{{terms[1]}}}{{{terms[0]}}} = {r_val}\\).\n"
        f"2. 5th term: \\(T_5 = {terms[3]} \\times {r_val} = {next_term}\\)."
    )
    return {
        "id": f"g9_pat_geom_int_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"r = {r_val}; T_5 = {next_term}",
        "expected_answer": f"r = {r_val}; T_5 = {next_term}",
        "sample_answer": f"r = {r_val}; T_5 = {next_term}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify common ratio r = {r_val}", "marks": 1},
            {"desc": f"Calculate next term T_5 = {next_term}", "marks": 1},
        ],
        "hints": [
            "Divide consecutive terms: T2 / T1.",
            f"Multiply T4 by {r_val} to get T5.",
            f"Answers: r = {r_val} and T5 = {next_term}.",
        ],
    }


# ----------------------------------------------------------------------
# 13. Geometric Sequence: Constant Ratio Fractional
# ----------------------------------------------------------------------
def arch_13_geometric_sequence_constant_ratio_fractional(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (81, 3, [81, 27, 9, 3], 1),
        (64, 2, [64, 32, 16, 8], 4),
        (125, 5, [125, 25, 5, 1], "\\frac{1}{5}"),
    ]
    a, div, terms, t5 = rng.choice(cases)
    terms_str = "; ".join(str(x) for x in terms)

    prompt = (
        f"For the decreasing geometric number sequence:\n\n"
        f"\\[ {terms_str};\\ \\dots \\]\n\n"
        f"State the common ratio \\(r\\) and calculate the 5th term (\\(T_5\\))."
    )
    sol = (
        f"**Fractional Ratio:**\n"
        f"\\(r = \\frac{{{terms[1]}}}{{{terms[0]}}} = \\frac{{1}}{{{div}}}\\).\n"
        f"\\(T_5 = {terms[3]} \\times \\frac{{1}}{{{div}}} = {t5}\\)."
    )
    return {
        "id": f"g9_pat_geom_frac_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"r = 1/{div}; T_5 = {t5}",
        "expected_answer": f"r = 1/{div}; T_5 = {t5}",
        "sample_answer": f"r = 1/{div}; T_5 = {t5}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State common ratio r = 1/{div}", "marks": 1},
            {"desc": f"Calculate 5th term T_5 = {t5}", "marks": 1},
        ],
        "hints": [
            f"Notice each term is divided by {div}.",
            f"The ratio is r = 1/{div}.",
            f"Next term is {t5}.",
        ],
    }


# ----------------------------------------------------------------------
# 14. Geometric Sequence: Alternating Signs
# ----------------------------------------------------------------------
def arch_14_geometric_sequence_alternating_signs(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 5])
    r_val = -2
    terms = [a * (r_val ** i) for i in range(4)]
    next_two = [a * (r_val ** 4), a * (r_val ** 5)]
    terms_str = "; ".join(str(x) for x in terms)

    prompt = (
        f"Observe the alternating pattern:\n\n"
        f"\\[ {terms_str};\\ \\dots;\\ \\dots \\]\n\n"
        f"Identify the common ratio and calculate the next two terms."
    )
    sol = (
        f"**Alternating Sequence:**\n"
        f"Ratio: \\(r = \\frac{{{terms[1]}}}{{{terms[0]}}} = {r_val}\\).\n"
        f"Next term 1: \\({terms[3]} \\times ({r_val}) = {next_two[0]}\\).\n"
        f"Next term 2: \\({next_two[0]} \\times ({r_val}) = {next_two[1]}\\)."
    )
    return {
        "id": f"g9_pat_geom_alt_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"r = {r_val}; {next_two[0]}; {next_two[1]}",
        "expected_answer": f"r = {r_val}; {next_two[0]}; {next_two[1]}",
        "sample_answer": f"r = {r_val}; {next_two[0]}; {next_two[1]}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Identify negative ratio r = {r_val}", "marks": 1},
            {"desc": f"State next two terms {next_two[0]} and {next_two[1]}", "marks": 1},
        ],
        "hints": [
            "The signs alternate between positive and negative, so r is negative.",
            f"Common ratio is {r_val}.",
            f"Next terms: {next_two[0]} and {next_two[1]}.",
        ],
    }


# ----------------------------------------------------------------------
# 15. Geometric Sequence: Find kth Term
# ----------------------------------------------------------------------
def arch_15_geometric_sequence_find_kth_term(rng: random.Random) -> Dict[str, Any]:
    a = 2
    r_val = 2
    # Tn = 2 * 2^(n-1) = 2^n
    k = rng.choice([7, 8, 9])
    ans = a * (r_val ** (k - 1))

    prompt = (
        f"A geometric sequence begins \\(2;\\ 4;\\ 8;\\ 16;\\ \\dots\\)\n\n"
        f"Calculate the value of the **{k}th** term (\\(T_{{{k}}}\\))."
    )
    sol = (
        f"**Geometric Term Formula (\\(T_n = a \\cdot r^{{n-1}}\\)):**\n"
        f"Here \\(a = 2\\) and \\(r = 2\\).\n"
        f"\\[ T_{{{k}}} = 2 \\times 2^{{{k - 1}}} = 2^{{{k}}} = {ans} \\]"
    )
    return {
        "id": f"g9_pat_geom_kth_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "expected_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State formula T_{k} = 2^{k}", "marks": 1},
            {"desc": f"Compute evaluated term {ans}", "marks": 1},
        ],
        "hints": [
            "Tn = a * r^(n-1).",
            f"Evaluate 2^{k}.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 16. Square Numbers Sequence
# ----------------------------------------------------------------------
def arch_16_square_numbers_sequence(rng: random.Random) -> Dict[str, Any]:
    target_n = rng.choice([12, 15, 20, 25])
    ans = target_n ** 2

    prompt = (
        f"Consider the sequence of perfect square numbers:\n\n"
        f"\\[ 1;\\ 4;\\ 9;\\ 16;\\ 25;\\ \\dots \\]\n\n"
        f"1. State the general term formula \\(T_n\\).\n"
        f"2. Calculate the {target_n}th term (\\(T_{{{target_n}}}\\))."
    )
    sol = (
        f"**Square Numbers Sequence:**\n"
        f"1. General term: \\(T_n = n^2\\).\n"
        f"2. For \\(n = {target_n}\\): \\(T_{{{target_n}}} = {target_n}^2 = {ans}\\)."
    )
    return {
        "id": f"g9_pat_sq_nums_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"T_n = n^2; T_{target_n} = {ans}",
        "expected_answer": f"T_n = n^2; T_{target_n} = {ans}",
        "sample_answer": f"T_n = n^2; T_{target_n} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "State formula T_n = n^2", "marks": 1},
            {"desc": f"Calculate {target_n}^2 = {ans}", "marks": 1},
        ],
        "hints": [
            "Each term is the square of its position number: 1^2, 2^2, 3^2...",
            f"Square {target_n}.",
            f"Results: Tn = n^2 and T{target_n} = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 17. Cube Numbers Sequence
# ----------------------------------------------------------------------
def arch_17_cube_numbers_sequence(rng: random.Random) -> Dict[str, Any]:
    target_n = rng.choice([6, 7, 8, 10])
    ans = target_n ** 3

    prompt = (
        f"Consider the sequence of cube numbers:\n\n"
        f"\\[ 1;\\ 8;\\ 27;\\ 64;\\ 125;\\ \\dots \\]\n\n"
        f"1. State the formula for the general term \\(T_n\\).\n"
        f"2. Calculate the value of \\(T_{{{target_n}}}\\)."
    )
    sol = (
        f"**Cube Numbers Sequence:**\n"
        f"1. General rule: \\(T_n = n^3\\).\n"
        f"2. \\(T_{{{target_n}}} = {target_n}^3 = {ans}\\)."
    )
    return {
        "id": f"g9_pat_cube_nums_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"T_n = n^3; T_{target_n} = {ans}",
        "expected_answer": f"T_n = n^3; T_{target_n} = {ans}",
        "sample_answer": f"T_n = n^3; T_{target_n} = {ans}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": "State formula T_n = n^3", "marks": 1},
            {"desc": f"Evaluate {target_n}^3 = {ans}", "marks": 1},
        ],
        "hints": [
            "Each term is n cubed: 1^3, 2^3, 3^3...",
            f"Calculate {target_n} * {target_n} * {target_n}.",
            f"Answers: Tn = n^3 and {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 18. Triangular Numbers Sequence
# ----------------------------------------------------------------------
def arch_18_triangular_numbers_sequence(rng: random.Random) -> Dict[str, Any]:
    target_n = rng.choice([10, 12, 15, 20])
    ans = (target_n * (target_n + 1)) // 2

    prompt = (
        f"The triangular numbers sequence is formed by counting dots in triangular arrangements:\n\n"
        f"\\[ 1;\\ 3;\\ 6;\\ 10;\\ 15;\\ \\dots \\]\n\n"
        f"Using the triangular number formula \\(T_n = \\frac{{n(n+1)}}{{2}}\\), calculate the "
        f"**{target_n}th** triangular number."
    )
    sol = (
        f"**Triangular Number Calculation:**\n"
        f"\\[ T_{{{target_n}}} = \\frac{{{target_n}({target_n} + 1)}}{{2}} = \\frac{{{target_n} \\times {target_n + 1}}}{{2}} = {ans} \\]"
    )
    return {
        "id": f"g9_pat_triangular_nums_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "expected_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Substitute n = {target_n} into formula", "marks": 1},
            {"desc": f"Calculate {target_n} * {target_n+1} / 2 = {ans}", "marks": 1},
        ],
        "hints": [
            f"Multiply {target_n} by {target_n + 1}.",
            "Divide the result by 2.",
            f"Answer: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 19. Quadratic Sequence: Second Difference Constant
# ----------------------------------------------------------------------
def arch_19_quadratic_sequence_second_difference_constant(rng: random.Random) -> Dict[str, Any]:
    # Tn = n^2 + 1: 2, 5, 10, 17, 26...
    # 1st diff: 3, 5, 7, 9...
    # 2nd diff: 2, 2, 2...
    c_shift = rng.choice([-1, 1, 2, 3])
    terms = [i**2 + c_shift for i in range(1, 6)]
    terms_str = "; ".join(str(x) for x in terms)

    diff1 = [terms[i+1] - terms[i] for i in range(4)]
    diff2 = diff1[1] - diff1[0]
    sign_c = f"+ {c_shift}" if c_shift > 0 else (f"- {abs(c_shift)}" if c_shift < 0 else "")
    ans_rule = f"n^2 {sign_c}".strip()

    prompt = (
        f"Consider the sequence:\n\n"
        f"\\[ {terms_str};\\ \\dots \\]\n\n"
        f"1. Calculate the first and second differences of the sequence.\n"
        f"2. State what the constant second difference tells us about the type of sequence."
    )
    sol = (
        f"**Differences:**\n"
        f"1. First differences: \\({diff1[0]};\\ {diff1[1]};\\ {diff1[2]};\\ {diff1[3]}\\).\n"
        f"2. Second difference: constant at \\({diff2}\\).\n"
        f"A constant second difference confirms that the sequence is **quadratic** (involving \\(n^2\\))."
    )
    return {
        "id": f"g9_pat_quad_diff2_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": f"Second difference = {diff2}; Sequence is quadratic",
        "expected_answer": f"Second difference = {diff2}; Sequence is quadratic",
        "sample_answer": f"Second difference = {diff2}; Sequence is quadratic",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"State constant second difference = {diff2}", "marks": 1},
            {"desc": "Identify sequence type as quadratic", "marks": 1},
        ],
        "hints": [
            "Subtract consecutive terms twice.",
            f"The second difference is {diff2}.",
            "A constant second difference indicates a quadratic sequence.",
        ],
    }


# ----------------------------------------------------------------------
# 20. Quadratic Sequence: Find Specific Term
# ----------------------------------------------------------------------
def arch_20_quadratic_sequence_find_specific_term(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    b = rng.choice([-1, 1, 2])
    target_n = 10
    ans = a * (target_n ** 2) + b

    sign_b = f"+ {b}" if b > 0 else (f"- {abs(b)}" if b < 0 else "")
    rule_str = f"T_n = {a}n^2 {sign_b}".strip()

    prompt = (
        f"A quadratic pattern follows the rule \\({rule_str}\\).\n\n"
        f"Calculate the value of the 10th term (\\(T_{{10}}\\))."
    )
    sol = (
        f"**Evaluating Quadratic Term:**\n"
        f"\\[ T_{{10}} = {a}(10)^2 {sign_b} = {a}(100) {sign_b} = {ans} \\]"
    )
    return {
        "id": f"g9_pat_quad_t10_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(ans),
        "expected_answer": str(ans),
        "sample_answer": str(ans),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Square 10 to get 100", "marks": 1},
            {"desc": f"Evaluate final answer {ans}", "marks": 1},
        ],
        "hints": [
            "Square the position number 10 first (10^2 = 100).",
            f"Multiply by {a} and apply {sign_b}.",
            f"T10 = {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 21. Fibonacci-Type Additive Sequence
# ----------------------------------------------------------------------
def arch_21_fibonacci_type_additive_sequence(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice([1, 2, 3])
    t2 = rng.choice([1, 3, 4])
    terms = [t1, t2]
    for _ in range(4):
        terms.append(terms[-1] + terms[-2])

    shown = terms[:4]
    next_two = terms[4:6]
    shown_str = "; ".join(str(x) for x in shown)
    ans = f"{next_two[0]}; {next_two[1]}"

    prompt = (
        f"In a Fibonacci-type sequence, each term is obtained by adding together the two preceding terms.\n\n"
        f"Given the start of the sequence:\n\n"
        f"\\[ {shown_str};\\ \\dots;\\ \\dots \\]\n\n"
        f"Calculate the next two terms."
    )
    sol = (
        f"**Additive Rule:**\n"
        f"1. Next term 1: \\({shown[2]} + {shown[3]} = {next_two[0]}\\).\n"
        f"2. Next term 2: \\({shown[3]} + {next_two[0]} = {next_two[1]}\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_pat_fibonacci_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate term 5 = {next_two[0]}", "marks": 1},
            {"desc": f"Calculate term 6 = {next_two[1]}", "marks": 1},
        ],
        "hints": [
            "Add the last two numbers to find the next one.",
            f"Add {shown[-2]} + {shown[-1]}.",
            f"Next terms: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 22. Table Representation: Complete Missing Outputs
# ----------------------------------------------------------------------
def arch_22_table_representation_complete_missing_outputs(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([3, 4, 5])
    c = rng.choice([2, 5, 7])
    # y = m*x + c
    x_vals = [1, 2, 3, 5, 10]
    y_vals = [m * x + c for x in x_vals]

    ans = f"For x = 5: y = {y_vals[3]}; For x = 10: y = {y_vals[4]}"

    prompt = (
        f"A relationship between input \\(x\\) and output \\(y\\) is given by the rule \\(y = {m}x + {c}\\).\n\n"
        f"When \\(x = 1\\), \\(y = {y_vals[0]}\\)\n"
        f"When \\(x = 2\\), \\(y = {y_vals[1]}\\)\n"
        f"When \\(x = 3\\), \\(y = {y_vals[2]}\\)\n\n"
        f"Calculate the corresponding output values \\(y\\) when:\n"
        f"1. \\(x = 5\\)\n"
        f"2. \\(x = 10\\)"
    )
    sol = (
        f"**Evaluating Outputs:**\n"
        f"1. For \\(x = 5\\): \\(y = {m}(5) + {c} = {y_vals[3]}\\).\n"
        f"2. For \\(x = 10\\): \\(y = {m}(10) + {c} = {y_vals[4]}\\)."
    )
    return {
        "id": f"g9_pat_table_outputs_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Substitute x = 5 to get y = {y_vals[3]}", "marks": 1},
            {"desc": f"Substitute x = 10 to get y = {y_vals[4]}", "marks": 1},
        ],
        "hints": [
            f"Multiply x by {m} and add {c}.",
            f"For x = 5: y = {y_vals[3]}.",
            f"For x = 10: y = {y_vals[4]}.",
        ],
    }


# ----------------------------------------------------------------------
# 23. Table Representation: Find Rule from Input-Output Pairs
# ----------------------------------------------------------------------
def arch_23_table_representation_find_rule_from_input_output_table(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 4, 6])
    c = rng.choice([-3, -1, 3, 5])
    # x: 1, 2, 3 -> y: m*1+c, m*2+c, m*3+c
    y1 = m * 1 + c
    y2 = m * 2 + c
    y3 = m * 3 + c

    sign_c = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
    ans = f"y = {m}x {sign_c}".strip()

    prompt = (
        f"The following input-output pairs belong to a linear relationship:\n\n"
        f"\\((1;\\ {y1})\\), \\((2;\\ {y2})\\), \\((3;\\ {y3})\\)\n\n"
        f"Determine the general formula connecting \\(y\\) in terms of \\(x\\)."
    )
    sol = (
        f"**Linear Rule Derivation:**\n"
        f"1. Rate of change (gradient): \\(m = \\frac{{{y2} - {y1}}}{{2 - 1}} = {m}\\).\n"
        f"2. \\(y\\)-intercept: when \\(x = 1\\), \\(y = {y1} \\implies {m}(1) + c = {y1} \\implies c = {c}\\).\n"
        f"Result: \\({ans}\\)."
    )
    return {
        "id": f"g9_pat_table_find_rule_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "expected_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Calculate gradient m = {m}", "marks": 1},
            {"desc": f"State full linear equation {ans}", "marks": 1},
        ],
        "hints": [
            "Find how much y increases when x increases by 1.",
            "Use y = mx + c.",
            f"Formula: {ans}.",
        ],
    }


# ----------------------------------------------------------------------
# 24. Flow Diagram: Input Rule Output Representation
# ----------------------------------------------------------------------
def arch_24_flow_diagram_input_rule_output_representation(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([3, 5, 7])
    sub_val = rng.choice([2, 4, 6])
    x = rng.randint(4, 9)
    y = mult * x - sub_val

    prompt = (
        f"A flow diagram applies the following two operations in sequence to an input number \\(x\\):\n\n"
        f"$$\\text{{Input }} x \\longrightarrow [\\times {mult}] \\longrightarrow [- {sub_val}] \\longrightarrow \\text{{Output }} y$$\n\n"
        f"Calculate the output \\(y\\) when the input is \\(x = {x}\\)."
    )
    sol = (
        f"**Following Flow Steps:**\n"
        f"Step 1: Multiply by {mult}: \\({x} \\times {mult} = {x * mult}\\).\n"
        f"Step 2: Subtract {sub_val}: \\({x * mult} - {sub_val} = {y}\\).\n"
        f"Output: \\(y = {y}\\)."
    )
    return {
        "id": f"g9_pat_flow_direct_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(y),
        "expected_answer": str(y),
        "sample_answer": str(y),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "marking_schema": [
            {"desc": f"Execute flow diagram operations to yield {y}", "marks": 1},
        ],
        "hints": [
            f"Multiply {x} by {mult}.",
            f"Subtract {sub_val}.",
            f"Answer: {y}.",
        ],
    }


# ----------------------------------------------------------------------
# 25. Inverse Flow Diagram: Find Input from Output
# ----------------------------------------------------------------------
def arch_25_inverse_flow_diagram_find_input_from_output(rng: random.Random) -> Dict[str, Any]:
    mult = rng.choice([4, 6, 8])
    add_val = rng.choice([3, 5, 7])
    x = rng.randint(3, 8)
    y = mult * x + add_val

    prompt = (
        f"A number machine processes inputs as follows:\n\n"
        f"$$\\text{{Input }} x \\longrightarrow [\\times {mult}] \\longrightarrow [+ {add_val}] \\longrightarrow \\text{{Output }} y$$\n\n"
        f"If the machine outputs \\(y = {y}\\), use inverse operations to determine the original input \\(x\\)."
    )
    sol = (
        f"**Inverse Flow Operations:**\n"
        f"Work backwards using opposite operations:\n"
        f"1. Reverse addition: \\({y} - {add_val} = {y - add_val}\\).\n"
        f"2. Reverse multiplication: \\({y - add_val} \\div {mult} = {x}\\).\n"
        f"Input: \\(x = {x}\\)."
    )
    return {
        "id": f"g9_pat_flow_inverse_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": str(x),
        "expected_answer": str(x),
        "sample_answer": str(x),
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "marking_schema": [
            {"desc": f"Subtract {add_val} to get {y - add_val}", "marks": 1},
            {"desc": f"Divide by {mult} to get input x = {x}", "marks": 1},
        ],
        "hints": [
            "Reverse the flow: do the opposite operation in reverse order.",
            f"Subtract {add_val} from {y}, then divide by {mult}.",
            f"Original input: x = {x}.",
        ],
    }
