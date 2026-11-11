"""Subskills 33 to 40: Venn diagrams, sets, intersections, unions, exclusive subsets, and solving unknown overlaps."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_frac,
    _fmt_pct,
)


def generate_33_reading_intersection_venn(r: random.Random) -> Dict[str, Any]:
    """Calculate the probability of the intersection P(A and B) from a 2-set Venn diagram."""
    total = r.choice([80, 100, 120, 150, 200])
    both = r.randint(15, 30)
    only_a = r.randint(25, 40)
    only_b = r.randint(20, 35)
    neither = total - (only_a + both + only_b)
    if neither < 5:
        total += 25
        neither = total - (only_a + both + only_b)

    frac_str = _fmt_frac(both, total)
    pct = round((both / total) * 100.0, 1)
    correct_ans = f"{frac_str} ({_fmt_pct(pct, 1)})"

    distractor_pcts = [
        round(((only_a + both) / total) * 100.0, 1),
        round(((only_b + both) / total) * 100.0, 1),
        round((only_a / total) * 100.0, 1),
    ]
    custom_options = [
        correct_ans,
        f"{_fmt_frac(only_a + both, total)} ({_fmt_pct(distractor_pcts[0], 1)})",
        f"{_fmt_frac(only_b + both, total)} ({_fmt_pct(distractor_pcts[1], 1)})",
        f"{_fmt_frac(only_a, total)} ({_fmt_pct(distractor_pcts[2], 1)})",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A survey of {total} Grade 12 learners investigated participation in school cultural activities:\n\n"
        f"| Venn Diagram Region | Number of Learners |\n"
        f"| :--- | :--- |\n"
        f"| Debating Society ONLY | {only_a} |\n"
        f"| Choir ONLY | {only_b} |\n"
        f"| Both Debating AND Choir | {both} |\n"
        f"| Neither activity | {neither} |\n"
        f"| **Total cohort** | **{total}** |\n\n"
        f"What is the probability that a randomly chosen Grade 12 learner participates in **both** Debating and Choir?"
    )
    explanation = (
        f"Step 1: Identify the count in the central intersection region: n(Debating ∩ Choir) = {both} [M].\n"
        f"Step 2: Divide by the total sample space n(S) = {total}: P(Both) = {both} / {total} [M].\n"
        f"Step 3: Simplify the fraction to {frac_str} or {_fmt_pct(pct, 1)} [A]."
    )
    return _build_question_payload(
        subskill_id="33_reading_intersection_venn",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The intersection is the middle overlapping region where learners do both activities.",
        tier_2=f"P(Both) = {both} ÷ {total}.",
        tier_3=f"Simplified fraction: {frac_str} ({_fmt_pct(pct, 1)}).",
        r=r,
    )


def generate_34_exclusive_subsets_only_a(r: random.Random) -> Dict[str, Any]:
    """Calculate the count and probability of belonging strictly to subset 'A only'."""
    total = r.choice([100, 120, 140, 160])
    both = r.randint(18, 30)
    total_acc = r.randint(45, 65)  # total taking accounting (includes both)
    only_acc = total_acc - both
    total_bus = r.randint(40, 60)
    only_bus = total_bus - both
    neither = total - (only_acc + both + only_bus)
    if neither < 0:
        total += 40
        neither = total - (only_acc + both + only_bus)

    frac_str = _fmt_frac(only_acc, total)
    pct = round((only_acc / total) * 100.0, 1)
    correct_ans = f"{only_acc} learners; P(Only Accounting) = {frac_str} ({_fmt_pct(pct, 1)})"

    custom_options = [
        correct_ans,
        f"{total_acc} learners; P(Only Accounting) = {_fmt_frac(total_acc, total)} ({_fmt_pct(round(total_acc / total * 100, 1), 1)})",
        f"{both} learners; P(Only Accounting) = {_fmt_frac(both, total)} ({_fmt_pct(round(both / total * 100, 1), 1)})",
        f"{only_bus} learners; P(Only Accounting) = {_fmt_frac(only_bus, total)} ({_fmt_pct(round(only_bus / total * 100, 1), 1)})",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"At a high school with {total} Grade 12 Commerce learners:\n"
        f"- {total_acc} learners study Accounting\n"
        f"- {total_bus} learners study Business Studies\n"
        f"- {both} learners study BOTH Accounting and Business Studies\n\n"
        f"Calculate the number of learners who study **Accounting ONLY**, and the probability of selecting one of these learners at random."
    )
    explanation = (
        f"Step 1: Subtract the shared overlap from total Accounting learners: n(Accounting only) = {total_acc} - {both} = {only_acc} [M].\n"
        f"Step 2: Express as a fraction of the entire cohort: {only_acc} / {total} [M].\n"
        f"Step 3: Simplify fraction to {frac_str} ({_fmt_pct(pct, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="34_exclusive_subsets_only_a",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the learners who study both subjects from the total studying Accounting.",
        tier_2=f"{total_acc} - {both} = {only_acc}. Then divide by {total}.",
        tier_3=f"{only_acc} learners; P = {frac_str} ({_fmt_pct(pct, 1)}).",
        r=r,
    )


def generate_35_union_rule_venn(r: random.Random) -> Dict[str, Any]:
    """Calculate the union P(A or B) using set counts: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)."""
    total = r.choice([100, 150, 200, 250])
    only_a = r.randint(30, 60)
    both = r.randint(20, 40)
    only_b = r.randint(25, 50)
    neither = total - (only_a + both + only_b)
    if neither < 10:
        total += 50
        neither = total - (only_a + both + only_b)

    union_count = only_a + both + only_b
    frac_str = _fmt_frac(union_count, total)
    pct = round((union_count / total) * 100.0, 1)

    correct_ans = f"n(A ∪ B) = {union_count}; P(A or B) = {frac_str} ({_fmt_pct(pct, 1)})"

    custom_options = [
        correct_ans,
        f"n(A ∪ B) = {only_a + only_b}; P(A or B) = {_fmt_frac(only_a + only_b, total)} ({_fmt_pct(round((only_a + only_b)/total*100, 1), 1)})",
        f"n(A ∪ B) = {union_count + both}; P(A or B) = {_fmt_frac(union_count + both, total)} ({_fmt_pct(round((union_count + both)/total*100, 1), 1)})",
        f"n(A ∪ B) = {both}; P(A or B) = {_fmt_frac(both, total)} ({_fmt_pct(round(both/total*100, 1), 1)})",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A Venn diagram displays learner participation in two winter sports across a cohort of {total} learners:\n"
        f"- Soccer ONLY: {only_a}\n"
        f"- Rugby ONLY: {only_b}\n"
        f"- Both Soccer AND Rugby: {both}\n"
        f"- Neither sport: {neither}\n\n"
        f"Calculate the total number of learners playing **at least one** of these sports, and the probability P(Soccer ∪ Rugby)."
    )
    explanation = (
        f"Step 1: The union consists of all learners in the circles: n(Soccer ∪ Rugby) = {only_a} + {both} + {only_b} = {union_count} [M].\n"
        f"Step 2: Express as probability: P(Union) = {union_count} / {total} [M].\n"
        f"Step 3: Simplify fraction to {frac_str} or {_fmt_pct(pct, 1)} [A]."
    )
    return _build_question_payload(
        subskill_id="35_union_rule_venn",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add Soccer only + Both + Rugby only, or calculate Total minus Neither.",
        tier_2=f"{only_a} + {both} + {only_b} = {union_count}. P = {union_count}/{total}.",
        tier_3=f"n(A ∪ B) = {union_count}; P = {frac_str} ({_fmt_pct(pct, 1)}).",
        r=r,
    )


def generate_36_outside_region_neither(r: random.Random) -> Dict[str, Any]:
    """Calculate the count and probability of the complement region (neither event)."""
    total = r.choice([80, 100, 120, 150])
    only_a = r.randint(22, 38)
    both = r.randint(14, 25)
    only_b = r.randint(18, 32)
    neither = total - (only_a + both + only_b)
    if neither < 10:
        total += 40
        neither = total - (only_a + both + only_b)

    frac_str = _fmt_frac(neither, total)
    pct = round((neither / total) * 100.0, 1)
    correct_ans = f"{neither} learners; P(Neither) = {frac_str} ({_fmt_pct(pct, 1)})"

    custom_options = [
        correct_ans,
        f"{only_a + only_b} learners; P(Neither) = {_fmt_frac(only_a + only_b, total)} ({_fmt_pct(round((only_a + only_b)/total*100, 1), 1)})",
        f"{both} learners; P(Neither) = {_fmt_frac(both, total)} ({_fmt_pct(round(both/total*100, 1), 1)})",
        f"{total - both} learners; P(Neither) = {_fmt_frac(total - both, total)} ({_fmt_pct(round((total - both)/total*100, 1), 1)})",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a matric class of {total} learners, a survey was conducted on home internet connectivity:\n"
        f"- {only_a} have Fibre ONLY\n"
        f"- {only_b} have Mobile LTE data ONLY\n"
        f"- {both} have BOTH Fibre and Mobile LTE data\n\n"
        f"Calculate the number of learners who have **neither** Fibre nor Mobile LTE, and find P(Neither)."
    )
    explanation = (
        f"Step 1: Calculate the total with internet: {only_a} + {both} + {only_b} = {only_a + both + only_b} [M].\n"
        f"Step 2: Subtract from cohort: n(Neither) = {total} - {only_a + both + only_b} = {neither} [M].\n"
        f"Step 3: Probability P(Neither) = {neither} / {total} = {frac_str} ({_fmt_pct(pct, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="36_outside_region_neither",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Sum all learners with at least one connection type, then subtract from the class total.",
        tier_2=f"Total connected = {only_a + both + only_b}. Neither = {total} - {only_a + both + only_b} = {neither}.",
        tier_3=f"{neither} learners; P = {frac_str} ({_fmt_pct(pct, 1)}).",
        r=r,
    )


def generate_37_three_set_venn_categorization(r: random.Random) -> Dict[str, Any]:
    """Analyze a 3-set Venn diagram to determine counts for all three sets or specific two-set overlaps."""
    total = 120
    all_three = r.randint(6, 12)
    m_p_only = r.randint(8, 14)   # Maths and Physics only
    m_l_only = r.randint(10, 16)  # Maths and Life Sciences only
    p_l_only = r.randint(7, 12)   # Physics and Life Sciences only
    maths_only = r.randint(20, 30)
    physics_only = r.randint(15, 25)
    life_only = r.randint(18, 28)

    in_circles = all_three + m_p_only + m_l_only + p_l_only + maths_only + physics_only + life_only
    neither = total - in_circles
    if neither < 0:
        total = in_circles + 15
        neither = 15

    # Target question: Total taking Maths
    total_maths = maths_only + m_p_only + m_l_only + all_three
    pct_maths = round((total_maths / total) * 100.0, 1)
    correct_ans = f"n(Maths) = {total_maths}; P(Maths) = {_fmt_frac(total_maths, total)} ({_fmt_pct(pct_maths, 1)})"

    custom_options = [
        correct_ans,
        f"n(Maths) = {maths_only}; P(Maths) = {_fmt_frac(maths_only, total)} ({_fmt_pct(round(maths_only/total*100, 1), 1)})",
        f"n(Maths) = {maths_only + all_three}; P(Maths) = {_fmt_frac(maths_only + all_three, total)} ({_fmt_pct(round((maths_only+all_three)/total*100, 1), 1)})",
        f"n(Maths) = {total_maths + p_l_only}; P(Maths) = {_fmt_frac(total_maths + p_l_only, total)} ({_fmt_pct(round((total_maths+p_l_only)/total*100, 1), 1)})",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A 3-set Venn diagram classifies {total} Grade 12 STEM learners enrolled in Mathematics (M), "
        f"Physical Sciences (P), and Life Sciences (L):\n"
        f"- Mathematics ONLY: {maths_only}\n"
        f"- Physical Sciences ONLY: {physics_only}\n"
        f"- Life Sciences ONLY: {life_only}\n"
        f"- M and P only: {m_p_only}\n"
        f"- M and L only: {m_l_only}\n"
        f"- P and L only: {p_l_only}\n"
        f"- All three subjects (M ∩ P ∩ L): {all_three}\n"
        f"- Taking none of these three: {neither}\n\n"
        f"Determine the **total number of learners taking Mathematics**, and find P(Maths)."
    )
    explanation = (
        f"Step 1: Sum all four regions inside the Mathematics circle:\n"
        f"n(M) = n(M only) + n(M ∩ P only) + n(M ∩ L only) + n(All three) [M].\n"
        f"Step 2: n(M) = {maths_only} + {m_p_only} + {m_l_only} + {all_three} = {total_maths} [M].\n"
        f"Step 3: P(Maths) = {total_maths} / {total} = {_fmt_frac(total_maths, total)} ({_fmt_pct(pct_maths, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="37_three_set_venn_categorization",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember that the Mathematics circle contains 4 separate regions: M only, M & P only, M & L only, and all three.",
        tier_2=f"Sum: {maths_only} + {m_p_only} + {m_l_only} + {all_three} = {total_maths}.",
        tier_3=f"n(Maths) = {total_maths}; P = {_fmt_frac(total_maths, total)} ({_fmt_pct(pct_maths, 1)}).",
        r=r,
    )


def generate_38_deducting_double_counted_overlap(r: random.Random) -> Dict[str, Any]:
    """Identify the double-counting error when adding set cardinalities without subtracting the overlap."""
    total_cohort = r.choice([100, 120, 150, 180])
    num_a = r.randint(55, 75)
    num_b = r.randint(45, 65)
    overlap = r.randint(20, 35)

    sum_separate = num_a + num_b
    true_union = sum_separate - overlap
    error_amount = overlap

    correct_ans = f"Double-counted {overlap} learners; True unique total = {true_union} learners"

    custom_options = [
        correct_ans,
        f"Double-counted {sum_separate} learners; True unique total = {total_cohort} learners",
        f"No error made; True unique total = {sum_separate} learners",
        f"Under-counted by {overlap} learners; True unique total = {sum_separate + overlap} learners",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A school principal states: '{num_a} learners play Soccer and {num_b} learners play Athletics. "
        f"Therefore, {num_a} + {num_b} = {sum_separate} learners participate in school sport.'\n\n"
        f"However, records show that {overlap} learners participate in **both** Soccer and Athletics.\n"
        f"Explain the mathematical error in the principal's calculation and calculate the true number of unique learners participating."
    )
    explanation = (
        f"Step 1: The {overlap} learners who do both sports were counted twice: once in Soccer and once in Athletics [M].\n"
        f"Step 2: Correct by applying the Inclusion-Exclusion Principle: n(A ∪ B) = n(A) + n(B) - n(A ∩ B) [M].\n"
        f"Step 3: True total = {num_a} + {num_b} - {overlap} = {true_union} learners [A]."
    )
    return _build_question_payload(
        subskill_id="38_deducting_double_counted_overlap",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Learners in both activities were added twice. Subtract the overlap once to get the true union.",
        tier_2=f"{num_a} + {num_b} - {overlap} = {true_union}.",
        tier_3=f"Double-counted {overlap} learners; True unique total = {true_union} learners.",
        r=r,
    )


def generate_39_solve_unknown_overlap_x(r: random.Random) -> Dict[str, Any]:
    """Solve for the unknown overlap x given total cohort size and outside count."""
    total = r.choice([80, 90, 100, 110])
    x_true = r.randint(12, 24)
    only_drama = r.randint(18, 30)
    only_music = r.randint(16, 28)
    outside = total - (only_drama + x_true + only_music)
    if outside < 5:
        total += 20
        outside = total - (only_drama + x_true + only_music)

    total_drama = only_drama + x_true
    total_music = only_music + x_true

    correct_ans = f"x = {x_true} learners"

    custom_options = [
        correct_ans,
        f"x = {x_true + 6} learners",
        f"x = {abs(x_true - 5)} learners",
        f"x = {total_drama + total_music - total} learners" if (total_drama + total_music - total) != x_true else f"x = {x_true + 10} learners",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A cohort of {total} Grade 12 learners has the following participation data:\n"
        f"- {total_drama} participate in Drama\n"
        f"- {total_music} participate in Music\n"
        f"- {outside} participate in neither Drama nor Music\n"
        f"- x learners participate in BOTH Drama and Music\n\n"
        f"Set up an equation and solve for **x**, the number of learners participating in both activities."
    )
    explanation = (
        f"Step 1: Set up the equation using total sample space:\n"
        f"({total_drama} - x) + x + ({total_music} - x) + {outside} = {total} [M].\n"
        f"Step 2: Simplify: {total_drama + total_music + outside} - x = {total} [M].\n"
        f"Step 3: Solve for x: x = {total_drama + total_music + outside} - {total} = {x_true} [A]."
    )
    return _build_question_payload(
        subskill_id="39_solve_unknown_overlap_x",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Equation: (Drama - x) + x + (Music - x) + Neither = Total.",
        tier_2=f"{total_drama} + {total_music} + {outside} - x = {total}.",
        tier_3=f"x = {x_true} learners.",
        r=r,
    )


def generate_40_conditional_probability_from_venn(r: random.Random) -> Dict[str, Any]:
    """Calculate conditional probability P(B | A) by restricting the sample space to set A."""
    total = r.choice([100, 120, 150])
    only_a = r.randint(25, 45)
    both = r.randint(15, 30)
    only_b = r.randint(20, 40)
    neither = total - (only_a + both + only_b)
    if neither < 5:
        total += 25
        neither = total - (only_a + both + only_b)

    total_a = only_a + both
    frac_str = _fmt_frac(both, total_a)
    pct = round((both / total_a) * 100.0, 1)

    correct_ans = f"P(B | A) = {both}/{total_a} = {frac_str} ({_fmt_pct(pct, 1)})"

    custom_options = [
        correct_ans,
        f"P(B | A) = {both}/{total} = {_fmt_frac(both, total)} ({_fmt_pct(round(both/total*100, 1), 1)})",
        f"P(B | A) = {only_a}/{total_a} = {_fmt_frac(only_a, total_a)} ({_fmt_pct(round(only_a/total_a*100, 1), 1)})",
        f"P(B | A) = {only_b}/{total} = {_fmt_frac(only_b, total)} ({_fmt_pct(round(only_b/total*100, 1), 1)})",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A survey of {total} Grade 12 learners regarding driver license preparation shows:\n"
        f"- Passed Learner's Theory ONLY: {only_a}\n"
        f"- Passed Driving Practical ONLY: {only_b}\n"
        f"- Passed BOTH Theory and Practical: {both}\n"
        f"- Passed neither: {neither}\n\n"
        f"Given that a learner has **passed the Theory test**, what is the probability that they also **passed the Practical driving test**?"
    )
    explanation = (
        f"Step 1: The condition 'Given that a learner passed Theory' restricts the sample space to all Theory passes: n(Theory) = {only_a} + {both} = {total_a} [M].\n"
        f"Step 2: Identify the favorable outcomes in this restricted group (those who passed both): n(Both) = {both} [M].\n"
        f"Step 3: P(Practical | Theory) = {both} / {total_a} = {frac_str} ({_fmt_pct(pct, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="40_conditional_probability_from_venn",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The condition restricts the denominator to all learners who passed Theory, NOT the entire class.",
        tier_2=f"Total passed Theory = {only_a} + {both} = {total_a}. Favorable (both) = {both}.",
        tier_3=f"P = {both}/{total_a} = {frac_str} ({_fmt_pct(pct, 1)}).",
        r=r,
    )
