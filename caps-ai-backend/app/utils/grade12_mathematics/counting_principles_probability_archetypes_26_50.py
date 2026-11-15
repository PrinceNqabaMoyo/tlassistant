"""Grade 12 Mathematics — Probability Archetypes 26 to 50.
Grounded in curriculum_docs_auto/Mathematics_Gr12/Term 3/02. Probability.md:
Fundamental counting principle m * n, exponential choices n^r, factorial notation n!,
permutations P(n, r), identical letters n! / (n1! n2! ...), grouping objects together,
objects not adjacent, digit/PIN codes with restrictions, and counting-based probabilities.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, Optional
import sympy as sp

from app.utils.grade12_mathematics._math_common import (
    make_math_question,
    num,
    solution_graph,
    step,
    to_latex,
)
from app.utils.grade12_mathematics.counting_principles_probability_archetypes_01_25 import (
    _venn_3_sets_svg,
)

TOPIC = "grade12_math_counting_probability"
LO_PREFIX = "math12_probability"


def _make_p2(
    subskill: str,
    prompt: str,
    prompt_latex: str,
    answer_latex: str,
    answer_sympy: str,
    sample_answer: str,
    marks: int = 3,
    difficulty: str = "medium",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    steps = [
        step(from_latex=prompt_latex, to_latex_str=answer_latex, op=f"compute {subskill}", rule=subskill),
    ]
    canonical = solution_graph(goal=subskill, steps=steps, final_latex=answer_latex)
    marking_schema = {
        "total_marks": marks,
        "marking_points": [
            {"id": "mp1", "desc": "Counting principle / permutation setup", "marks": max(1, marks - 1), "editable": True},
            {"id": "mp2", "desc": f"Final answer: {answer_latex}", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Apply the Fundamental Counting Principle, factorial permutations $n!$, or the block method for grouped objects.",
        "concept": "Divide by $n_1! n_2! ...$ for identical objects; group adjacent items into a single block and multiply by internal arrangements.",
        "breakdown": sample_answer,
    }
    return make_math_question(
        prefix=f"prob12_{subskill[:12]}",
        topic=TOPIC,
        subskill=subskill,
        learning_objective_id=f"{LO_PREFIX}_{subskill}",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        answer_sympy=answer_sympy,
        sample_answer=sample_answer,
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["omitted_internal_reordering", "forgot_identical_letter_division"],
        keywords=["counting principle", "permutations", subskill.replace("_", " ")],
        term=3,
        caps_weight_percent=15,
        suggested_duration_mins=max(3, marks),
        mode=subskill,
        difficulty=difficulty,
        diagram_spec=diagram_spec,
    )


# ---------------------------------------------------------------------------
# Archetypes 26 to 50
# ---------------------------------------------------------------------------
def build_26_fundamental_counting_principle_multi_stage_choices(r: random.Random) -> Dict[str, Any]:
    a, b, c = r.randint(3, 6), r.randint(4, 7), r.randint(2, 5)
    tot = a * b * c
    return _make_p2(
        "26_fundamental_counting_principle_multi_stage_choices",
        f"A school canteen offers {a} types of sandwiches, {b} flavours of fruit juice, and {c} desserts. In how many different ways can a learner choose a meal consisting of one sandwich, one juice, and one dessert?",
        rf"{a} \times {b} \times {c}",
        str(tot),
        str(tot),
        f"By the fundamental counting principle, total meal combinations $= {a} \\times {b} \\times {c} = {tot}$.",
        marks=2,
        difficulty="easy",
    )


def build_27_counting_with_repetition_exponential_rule(r: random.Random) -> Dict[str, Any]:
    n_opts = r.choice([3, 4, 5])
    k_q = r.randint(4, 7)
    tot = n_opts ** k_q
    return _make_p2(
        "27_counting_with_repetition_exponential_rule",
        f"A multiple-choice quiz consists of {k_q} questions, and each question has {n_opts} possible options. How many different ways can a learner answer all {k_q} questions if every question is answered?",
        rf"{n_opts}^{{{k_q}}}",
        str(tot),
        str(tot),
        f"Each of the {k_q} questions has {n_opts} choices: ${n_opts}^{{{k_q}}} = {tot}$.",
        marks=2,
        difficulty="easy",
    )


def build_28_factorial_notation_numeric_simplification(r: random.Random) -> Dict[str, Any]:
    n = r.randint(6, 11)
    ans = n * (n - 1)
    return _make_p2(
        "28_factorial_notation_numeric_simplification",
        f"Evaluate the factorial expression $\\frac{{{n}!}}{{{n-2}!}}$ without using a calculator.",
        rf"\frac{{{n}!}}{{{n-2}!}} = {n} \times {n-1}",
        str(ans),
        str(ans),
        f"$\\frac{{{n}!}}{{{n-2}!}} = \\frac{{{n} \\times {n-1} \\times {n-2}!}}{{{n-2}!}} = {n} \\times {n-1} = {ans}$.",
        marks=2,
        difficulty="easy",
    )


def build_29_factorial_algebraic_identity_reduction(r: random.Random) -> Dict[str, Any]:
    k = r.choice([1, 2, 3])
    val_n = r.randint(5, 10)
    ans_val = (val_n + k) * (val_n + k - 1)
    return _make_p2(
        "29_factorial_algebraic_identity_reduction",
        f"Simplify the expression $\\frac{{(n + {k})!}}{{(n + {k - 2})!}}$ and evaluate it when $n = {val_n}$.",
        rf"(n + {k})(n + {k - 1}) \text{{ at }} n = {val_n}",
        rf"(n + {k})(n + {k - 1}) = {ans_val}",
        str(ans_val),
        f"$\\frac{{(n+{k})!}}{{(n+{k-2})!}} = (n+{k})(n+{k-1})$. Substituting $n = {val_n}$ gives $({val_n+k})({val_n+k-1}) = {ans_val}$.",
        marks=3,
    )


def build_30_arrangements_of_n_distinct_objects_in_a_row(r: random.Random) -> Dict[str, Any]:
    n = r.randint(5, 8)
    tot = math.factorial(n)
    return _make_p2(
        "30_arrangements_of_n_distinct_objects_in_a_row",
        f"In how many different ways can {n} distinct finalists in an athletics sprint be arranged across {n} lanes?",
        rf"{n}!",
        str(tot),
        str(tot),
        f"The number of arrangements of {n} distinct athletes is ${n}! = {tot}$.",
        marks=2,
        difficulty="easy",
    )


def build_31_permutations_r_from_n_distinct_objects(r: random.Random) -> Dict[str, Any]:
    n = r.randint(7, 12)
    r_v = r.randint(3, 4)
    tot = math.perm(n, r_v)
    return _make_p2(
        "31_permutations_r_from_n_distinct_objects",
        f"From {n} candidates on a learner representative council, {r_v} distinct executive offices must be filled. In how many different ways can these {r_v} offices be filled if no candidate may hold more than one office?",
        rf"P({n}; {r_v}) = \frac{{{n}!}}{{({n} - {r_v})!}}",
        str(tot),
        str(tot),
        f"$P({n}; {r_v}) = \\frac{{{n}!}}{{{n - r_v}!}} = {tot}$.",
        marks=3,
    )


def build_32_letter_arrangements_distinct_vs_identical_letters(r: random.Random) -> Dict[str, Any]:
    words = [
        ("BASSOON", 7, "2! \\times 2!", 1260),
        ("SUCCESS", 7, "3! \\times 2!", 420),
        ("STATISTICS", 10, "3! \\times 3! \\times 2!", 50400),
        ("EXCELLENT", 9, "3! \\times 2!", 30240),
        ("COMMITTEE", 9, "2! \\times 2! \\times 2!", 45360),
        ("LIMPOPO", 7, "2! \\times 2!", 1260),
    ]
    w_str, n_len, denom_tex, ans = r.choice(words)
    return _make_p2(
        "32_letter_arrangements_distinct_vs_identical_letters",
        f"Consider the word **{w_str}**. How many distinct letter arrangements can be formed if repeated letters are treated as identical?",
        rf"\frac{{{n_len}!}}{{{denom_tex}}}",
        str(ans),
        str(ans),
        f"The word {w_str} has {n_len} letters with repetitions. Distinct arrangements $= \\frac{{{n_len}!}}{{{denom_tex}}} = {ans}$.",
        marks=3,
    )


def build_33_letter_arrangements_starting_with_fixed_letter(r: random.Random) -> Dict[str, Any]:
    opts = [
        ("BASSOON", "O", 6, "2!", 360),
        ("EXCELLENT", "L", 8, "3!", 6720),
        ("LIMPOPO", "P", 6, "2!", 360),
        ("SUCCESS", "C", 6, "3!", 120),
    ]
    w_str, ch, rem_n, denom_tex, ans = r.choice(opts)
    return _make_p2(
        "33_letter_arrangements_starting_with_fixed_letter",
        f"How many distinct arrangements of the letters of the word **{w_str}** start with the letter **{ch}** (treating repeated letters as identical)?",
        rf"\frac{{{rem_n}!}}{{{denom_tex}}}",
        str(ans),
        str(ans),
        f"Fixing one '{ch}' in the first position leaves {rem_n} letters to arrange: $\\frac{{{rem_n}!}}{{{denom_tex}}} = {ans}$.",
        marks=3,
    )


def build_34_letter_arrangements_starting_and_ending_same_letter(r: random.Random) -> Dict[str, Any]:
    opts = [
        ("BASSOON", "S or O", "5!/2! + 5!/2!", 120),
        ("LIMPOPO", "P or O", "5!/2! + 5!/2!", 120),
        ("MINIMUM", "M or I", "5!/2! + 5!/3!", 80),
        ("LEVEL", "L or E", "3! + 3!", 12),
    ]
    w_str, pair_desc, expr_str, ans = r.choice(opts)
    return _make_p2(
        "34_letter_arrangements_starting_and_ending_same_letter",
        f"Consider the word **{w_str}**. Calculate the number of distinct letter arrangements that start and end with the same letter ({pair_desc}) when repeated letters are treated as identical.",
        expr_str,
        str(ans),
        str(ans),
        f"Summing the disjoint cases for starting and ending with the same repeated letter ({pair_desc}) gives ${expr_str} = {ans}$.",
        marks=4,
        difficulty="hard",
    )


def build_35_letter_arrangements_all_vowels_grouped_together(r: random.Random) -> Dict[str, Any]:
    opts = [
        ("CAPETOWN", 8, 3, 5, math.factorial(6) * math.factorial(3)),
        ("GAUTENG", 7, 3, 4, (math.factorial(5) * math.factorial(3)) // 2),
        ("NUMBERS", 7, 2, 5, math.factorial(6) * math.factorial(2)),
        ("PROBLEMS", 8, 2, 6, math.factorial(7) * math.factorial(2)),
        ("FACTOR", 6, 2, 4, math.factorial(5) * math.factorial(2)),
    ]
    w_str, n_tot, v_cnt, c_cnt, ans = r.choice(opts)
    return _make_p2(
        "35_letter_arrangements_all_vowels_grouped_together",
        f"In how many distinct ways can the letters of the word **{w_str}** ({v_cnt} vowels and {c_cnt} consonants) be arranged in a row if all {v_cnt} vowels must stand together?",
        rf"({c_cnt} + 1)! \times {v_cnt}!",
        str(ans),
        str(ans),
        f"Grouping the {v_cnt} vowels into 1 block gives ${c_cnt} + 1 = {c_cnt+1}$ units, producing {ans} distinct arrangements.",
        marks=3,
    )


def build_36_grouping_single_group_together_block_method(r: random.Random) -> Dict[str, Any]:
    nb = r.randint(3, 5)
    ng = r.randint(3, 5)
    blocks = ng + 1
    ans = math.factorial(blocks) * math.factorial(nb)
    return _make_p2(
        "36_grouping_single_group_together_block_method",
        f"A group of {nb} boys and {ng} girls are seated in a row of {nb + ng} chairs. In how many different ways can they be seated if all {nb} boys must sit next to each other?",
        rf"({ng} + 1)! \times {nb}! = {blocks}! \times {nb}!",
        str(ans),
        str(ans),
        f"Treat the {nb} boys as 1 block: $({ng} + 1)! \\times {nb}! = {blocks}! \\times {nb}! = {ans}$.",
        marks=3,
    )


def build_37_grouping_multiple_subject_groups_together(r: random.Random) -> Dict[str, Any]:
    m_b = r.randint(2, 4)
    s_b = r.randint(2, 4)
    a_b = r.randint(2, 3)
    ans = math.factorial(3) * math.factorial(m_b) * math.factorial(s_b) * math.factorial(a_b)
    return _make_p2(
        "37_grouping_multiple_subject_groups_together",
        f"A shelf holds {m_b} different Mathematics books, {s_b} different Physical Sciences books, and {a_b} different Accounting books. In how many different ways can the books be arranged on the shelf if books of the same subject must stand together?",
        rf"3! \times {m_b}! \times {s_b}! \times {a_b}!",
        str(ans),
        str(ans),
        f"Arrange the 3 subject blocks in $3!$ ways and permute within each subject: $3! \\times {m_b}! \\times {s_b}! \\times {a_b}! = {ans}$.",
        marks=3,
    )


def build_38_two_objects_not_adjacent_complementary_counting(r: random.Random) -> Dict[str, Any]:
    n = r.randint(5, 8)
    tot = math.factorial(n)
    together = math.factorial(n - 1) * 2
    apart = tot - together
    return _make_p2(
        "38_two_objects_not_adjacent_complementary_counting",
        f"In how many different ways can {n} learners be seated in a row if two specific learners, Thabo and Lindiwe, must NOT sit next to each other?",
        rf"{n}! - ({n-1}! \times 2!) = {tot} - {together}",
        str(apart),
        str(apart),
        f"Total ways $= {n}! = {tot}$. Together $= {n-1}! \\times 2! = {together}$. Not adjacent $= {tot} - {together} = {apart}$.",
        marks=3,
    )


def build_39_seating_with_fixed_extreme_ends(r: random.Random) -> Dict[str, Any]:
    n = r.randint(5, 8)
    mid = n - 2
    ans = 2 * math.factorial(mid)
    return _make_p2(
        "39_seating_with_fixed_extreme_ends",
        f"A team of {n} sports captains stands in a row for a photograph. In how many different orders can they stand if the rugby captain and the netball captain must occupy the two extreme ends (leftmost or rightmost)?",
        rf"2! \times {mid}!",
        str(ans),
        str(ans),
        f"The two captains can occupy the two ends in $2! = 2$ ways, and the remaining {mid} captains can be arranged in ${mid}!$ ways: $2 \\times {math.factorial(mid)} = {ans}$.",
        marks=3,
    )


def build_40_alternating_gender_row_arrangements(r: random.Random) -> Dict[str, Any]:
    k = r.choice([3, 4])
    nb, ng = k, k + 1
    ans = math.factorial(ng) * math.factorial(nb)
    return _make_p2(
        "40_alternating_gender_row_arrangements",
        f"In how many different ways can {nb} boys and {ng} girls be seated in a row of {nb + ng} chairs if boys and girls must alternate positions?",
        rf"{ng}! \times {nb}!",
        str(ans),
        str(ans),
        f"To alternate with {ng} girls and {nb} boys, the pattern must be $G B G B ... G$. Thus the girls occupy {ng} positions in ${ng}!$ ways and the boys occupy {nb} positions in ${nb}!$ ways: ${ng}! \\times {nb}! = {ans}$.",
        marks=3,
    )


def build_41_digit_codes_with_and_without_repetition(r: random.Random) -> Dict[str, Any]:
    n_digs = r.choice([6, 7, 8, 9, 10])
    k_len = r.choice([3, 4])
    with_rep = n_digs ** k_len
    no_rep = math.perm(n_digs, k_len)
    diff = with_rep - no_rep
    return _make_p2(
        "41_digit_codes_with_and_without_repetition",
        f"A security PIN consists of {k_len} digits chosen from {n_digs} available digits. Calculate how many more PINs can be formed when repetition of digits is allowed compared to when repetition is NOT allowed.",
        rf"{n_digs}^{{{k_len}}} - P({n_digs}; {k_len}) = {with_rep} - {no_rep}",
        str(diff),
        str(diff),
        f"With repetition: ${n_digs}^{{{k_len}}} = {with_rep}$. Without repetition: $P({n_digs}; {k_len}) = {no_rep}$. Difference $= {diff}$.",
        marks=3,
    )


def build_42_digit_codes_even_or_odd_number_restriction(r: random.Random) -> Dict[str, Any]:
    n_tot = r.choice([6, 7, 8])
    evens = n_tot // 2
    ans = evens * (n_tot - 1) * (n_tot - 2) * (n_tot - 3)
    return _make_p2(
        "42_digit_codes_even_or_odd_number_restriction",
        f"How many four-digit EVEN numbers can be formed using the digits $1; 2; ...; {n_tot}$ if no digit may be repeated?",
        rf"{evens} \times {n_tot - 1} \times {n_tot - 2} \times {n_tot - 3}",
        str(ans),
        str(ans),
        f"There are {evens} even digits for the last position, leaving ${n_tot-1} \\times {n_tot-2} \\times {n_tot-3}$ choices for the first three digits: ${ans}$.",
        marks=3,
    )


def build_43_digit_codes_divisible_by_five_or_greater_than_threshold(r: random.Random) -> Dict[str, Any]:
    digs_count = r.choice([5, 6, 7])
    # Digits {1, 2, ..., digs_count} containing 5; 4-digit numbers divisible by 5 without repetition
    ans = 1 * (digs_count - 1) * (digs_count - 2) * (digs_count - 3)
    return _make_p2(
        "43_digit_codes_divisible_by_five_or_greater_than_threshold",
        f"Using the digits $1; 2; ...; {digs_count}$ without repetition, how many 4-digit numbers can be formed that are divisible by $5$?",
        rf"1 \times {digs_count - 1} \times {digs_count - 2} \times {digs_count - 3}",
        str(ans),
        str(ans),
        f"To be divisible by 5, the last digit must be 5 (1 choice). The remaining 3 positions can be filled in ${digs_count-1} \\times {digs_count-2} \\times {digs_count-3} = {ans}$ ways.",
        marks=3,
    )


def build_44_digit_codes_overlapping_prime_and_even_case_split(r: random.Random) -> Dict[str, Any]:
    code_len = r.choice([4, 5, 6])
    mid_len = code_len - 2
    mid_perm = math.perm(8, mid_len)
    c1 = 1 * 4 * mid_perm
    c2 = 3 * 5 * mid_perm
    tot = c1 + c2
    return _make_p2(
        "44_digit_codes_overlapping_prime_and_even_case_split",
        f"A {code_len}-digit code is formed from the digits $0$ to $9$ without repetition. Calculate how many codes start with a prime digit ($2, 3, 5, 7$) and end with an even digit ($0, 2, 4, 6, 8$).",
        rf"1 \times 4 \times P(8; {mid_len}) + 3 \times 5 \times P(8; {mid_len}) = {c1} + {c2}",
        str(tot),
        str(tot),
        f"Case 1 (starts with 2): $1 \\times 4 \\times P(8; {mid_len}) = {c1}$. Case 2 (starts with 3, 5, or 7): $3 \\times 5 \\times P(8; {mid_len}) = {c2}$. Total $= {tot}$.",
        marks=4,
        difficulty="hard",
    )


def build_45_vehicle_number_plates_excluded_vowels_and_digits(r: random.Random) -> Dict[str, Any]:
    excl = r.choice([5, 6, 7])
    letters = 26 - excl
    n_let = r.choice([2, 3])
    n_dig = r.choice([2, 3])
    tot = (letters ** n_let) * (9 ** n_dig)
    return _make_p2(
        "45_vehicle_number_plates_excluded_vowels_and_digits",
        f"A provincial vehicle number plate consists of {n_let} letters (chosen from 26 alphabet letters excluding {excl} restricted letters) followed by {n_dig} non-zero digits ($1$ to $9$), with repetition allowed. How many different number plates can be made?",
        rf"{letters}^{{{n_let}}} \times 9^{{{n_dig}}}",
        str(tot),
        str(tot),
        f"Available letters $= 26 - {excl} = {letters}$. Total plates $= {letters}^{{{n_let}}} \\times 9^{{{n_dig}}} = {tot}$.",
        marks=3,
    )


def build_46_probability_from_row_seating_grouping(r: random.Random) -> Dict[str, Any]:
    nb = r.randint(3, 5)
    ng = r.randint(3, 5)
    n_tot = nb + ng
    fav = math.factorial(ng + 1) * math.factorial(nb)
    tot = math.factorial(n_tot)
    prob = sp.Rational(fav, tot)
    return _make_p2(
        "46_probability_from_row_seating_grouping",
        f"If {nb} boys and {ng} girls are seated at random in a row of {n_tot} chairs, calculate the probability that all {nb} boys sit next to each other.",
        rf"\frac{{({ng}+1)! \times {nb}!}}{{{n_tot}!}} = \frac{{{fav}}}{{{tot}}}",
        to_latex(prob),
        str(prob),
        f"$P(\\text{{boys together}}) = \\frac{{{ng+1}! \\times {nb}!}}{{{n_tot}!}} = \\frac{{{fav}}}{{{tot}}} = {to_latex(prob)}$.",
        marks=3,
    )


def build_47_probability_from_identical_letter_word_arrangements(r: random.Random) -> Dict[str, Any]:
    opts = [
        ("BASSOON", "O", sp.Rational(2, 7)),
        ("SUCCESS", "S", sp.Rational(3, 7)),
        ("EXCELLENT", "E", sp.Rational(3, 9)),
        ("STATISTICS", "T", sp.Rational(3, 10)),
    ]
    w_str, ch, prob = r.choice(opts)
    return _make_p2(
        "47_probability_from_identical_letter_word_arrangements",
        f"The letters of the word **{w_str}** are arranged at random. Calculate the probability that the arrangement begins with the letter **{ch}**.",
        rf"P(\text{{starts with {ch}}}) = {to_latex(prob)}",
        to_latex(prob),
        str(prob),
        f"In **{w_str}**, the fraction of letters equal to '{ch}' gives $P(\\text{{starts with {ch}}}) = {to_latex(prob)}$.",
        marks=3,
    )


def build_48_probability_pin_contains_at_least_one_target_digit(r: random.Random) -> Dict[str, Any]:
    k_len = r.choice([3, 4, 5])
    target_d = r.randint(1, 9)
    tot = 10 ** k_len
    none_cnt = 9 ** k_len
    fav = tot - none_cnt
    prob = sp.Rational(fav, tot)
    return _make_p2(
        "48_probability_pin_contains_at_least_one_target_digit",
        f"A {k_len}-digit PIN is randomly generated from digits $0$ to $9$ with repetition allowed. Calculate the probability that the PIN contains at least one '{target_d}'.",
        rf"1 - \frac{{9^{{{k_len}}}}}{{10^{{{k_len}}}}} = \frac{{{fav}}}{{{tot}}}",
        to_latex(prob),
        str(prob),
        f"By complementary counting, $P(\\text{{no '{target_d}'}}) = \\frac{{9^{{{k_len}}}}}{{10^{{{k_len}}}}} = \\frac{{{none_cnt}}}{{{tot}}}$. Thus $P(\\text{{at least one '{target_d}'}}) = 1 - \\frac{{{none_cnt}}}{{{tot}}} = {to_latex(prob)}$.",
        marks=3,
    )


def build_49_quadratic_equation_in_unknown_beads_probability(r: random.Random) -> Dict[str, Any]:
    b_cnt = r.choice([3, 4, 5])
    y_ans = b_cnt * r.choice([2, 3])
    tot = b_cnt + y_ans
    prob_same = sp.Rational(b_cnt * b_cnt + y_ans * y_ans, tot * tot)
    return _make_p2(
        "49_quadratic_equation_in_unknown_beads_probability",
        f"A bag contains {b_cnt} black tokens and $y$ yellow tokens (with $y > {b_cnt}$). One token is selected at random, replaced in the bag, and a second token is selected. Given that the probability of selecting two tokens of the same colour is ${to_latex(prob_same)}$, calculate the value of $y$.",
        rf"\frac{{{b_cnt}^2 + y^2}}{{({b_cnt} + y)^2}} = {to_latex(prob_same)}",
        rf"y = {y_ans}",
        str(y_ans),
        f"$\\frac{{{b_cnt*b_cnt} + y^2}}{{({b_cnt} + y)^2}} = {to_latex(prob_same)}$. Solving the resulting quadratic equation for $y > {b_cnt}$ yields $y = {y_ans}$.",
        marks=4,
        difficulty="hard",
    )


def build_50_comprehensive_counting_and_venn_synthesis(r: random.Random) -> Dict[str, Any]:
    nb, ng = r.randint(3, 4), r.randint(3, 4)
    n_seat = nb + ng
    fav_seat = math.factorial(ng + 1) * math.factorial(nb)
    tot_seat = math.factorial(n_seat)
    prob_seat = sp.Rational(fav_seat, tot_seat)

    or_v, os_v, oc_v = r.randint(25, 40), r.randint(20, 35), r.randint(18, 30)
    rs, rc, sc = r.randint(6, 12), r.randint(5, 10), r.randint(7, 13)
    all3 = r.randint(5, 10)
    out = r.randint(6, 12)
    N_tot = or_v + os_v + oc_v + rs + rc + sc + all3 + out
    ge2 = rs + rc + sc + all3
    prob_ge2 = sp.Rational(ge2, N_tot)
    d_spec = _venn_3_sets_svg(str(or_v), str(os_v), str(oc_v), str(rs), str(rc), str(sc), str(all3), str(out), f"NSC Exam Synthesis (N = {N_tot})")

    return _make_p2(
        "50_comprehensive_counting_and_venn_synthesis",
        f"**Part A:** {nb} boys and {ng} girls are seated at random in a row of {n_seat} chairs. Calculate the probability that all {nb} boys sit together.\n\n"
        f"**Part B:** Refer to the 3-set Venn diagram for $N = {N_tot}$ learners with pairwise-only counts {rs}, {rc}, {sc} and three-set intersection {all3}. Determine the probability that a randomly selected learner participates in at least two sports.",
        rf"P(\text{{boys}}) = {to_latex(prob_seat)}, \quad P(\ge 2) = {to_latex(prob_ge2)}",
        rf"\text{{Part A: }} {to_latex(prob_seat)}; \quad \text{{Part B: }} {to_latex(prob_ge2)}",
        f"PartA={prob_seat}, PartB={prob_ge2}",
        f"Part A: $\\frac{{{ng+1}! \\times {nb}!}}{{{n_seat}!}} = \\frac{{{fav_seat}}}{{{tot_seat}}} = {to_latex(prob_seat)}$. Part B: $\\frac{{{rs}+{rc}+{sc}+{all3}}}{{{N_tot}}} = \\frac{{{ge2}}}{{{N_tot}}} = {to_latex(prob_ge2)}$.",
        marks=6,
        difficulty="hard",
        diagram_spec=d_spec,
    )


ARCHETYPES_26_50: Dict[str, Any] = {
    "26_fundamental_counting_principle_multi_stage_choices": build_26_fundamental_counting_principle_multi_stage_choices,
    "27_counting_with_repetition_exponential_rule": build_27_counting_with_repetition_exponential_rule,
    "28_factorial_notation_numeric_simplification": build_28_factorial_notation_numeric_simplification,
    "29_factorial_algebraic_identity_reduction": build_29_factorial_algebraic_identity_reduction,
    "30_arrangements_of_n_distinct_objects_in_a_row": build_30_arrangements_of_n_distinct_objects_in_a_row,
    "31_permutations_r_from_n_distinct_objects": build_31_permutations_r_from_n_distinct_objects,
    "32_letter_arrangements_distinct_vs_identical_letters": build_32_letter_arrangements_distinct_vs_identical_letters,
    "33_letter_arrangements_starting_with_fixed_letter": build_33_letter_arrangements_starting_with_fixed_letter,
    "34_letter_arrangements_starting_and_ending_same_letter": build_34_letter_arrangements_starting_and_ending_same_letter,
    "35_letter_arrangements_all_vowels_grouped_together": build_35_letter_arrangements_all_vowels_grouped_together,
    "36_grouping_single_group_together_block_method": build_36_grouping_single_group_together_block_method,
    "37_grouping_multiple_subject_groups_together": build_37_grouping_multiple_subject_groups_together,
    "38_two_objects_not_adjacent_complementary_counting": build_38_two_objects_not_adjacent_complementary_counting,
    "39_seating_with_fixed_extreme_ends": build_39_seating_with_fixed_extreme_ends,
    "40_alternating_gender_row_arrangements": build_40_alternating_gender_row_arrangements,
    "41_digit_codes_with_and_without_repetition": build_41_digit_codes_with_and_without_repetition,
    "42_digit_codes_even_or_odd_number_restriction": build_42_digit_codes_even_or_odd_number_restriction,
    "43_digit_codes_divisible_by_five_or_greater_than_threshold": build_43_digit_codes_divisible_by_five_or_greater_than_threshold,
    "44_digit_codes_overlapping_prime_and_even_case_split": build_44_digit_codes_overlapping_prime_and_even_case_split,
    "45_vehicle_number_plates_excluded_vowels_and_digits": build_45_vehicle_number_plates_excluded_vowels_and_digits,
    "46_probability_from_row_seating_grouping": build_46_probability_from_row_seating_grouping,
    "47_probability_from_identical_letter_word_arrangements": build_47_probability_from_identical_letter_word_arrangements,
    "48_probability_pin_contains_at_least_one_target_digit": build_48_probability_pin_contains_at_least_one_target_digit,
    "49_quadratic_equation_in_unknown_beads_probability": build_49_quadratic_equation_in_unknown_beads_probability,
    "50_comprehensive_counting_and_venn_synthesis": build_50_comprehensive_counting_and_venn_synthesis,
}
