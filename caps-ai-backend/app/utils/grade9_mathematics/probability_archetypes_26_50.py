"""Grade 9 Mathematics - Probability Archetypes 26-50 (CAPS Term 4).
Focus: Compound events, tree diagrams (with and without replacement), two-way contingency tables,
Venn diagrams (intersection, union, complement), mutually exclusive vs inclusive events,
and multi-stage probabilistic synthesis.
100% deterministic, zero LLM calls.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

from app.utils.grade9_mathematics.probability_svg import draw_two_stage_tree_diagram_svg


def _fmt(val: float, decimals: int = 1) -> str:
    s = f"{val:.{decimals}f}"
    return s.replace(".", "{,}")


# -----------------------------------------------------------------------------
# 26. Compound Event: Sum of Two Dice Greater Than 10
# -----------------------------------------------------------------------------
def arch_26_compound_event_sum_of_two_dice_greater_than_ten(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two fair six-sided dice are rolled simultaneously.\n"
        "Calculate the probability that the **sum of the faces is strictly greater than 10**, "
        "expressing your answer as a simplified fraction."
    )
    ans_str = "\\frac{1}{12}"
    sol = (
        "Total outcomes $n(S) = 36$.\n"
        "Sums strictly greater than 10 are sums of 11 or 12:\n"
        "• Sum = 11: $\\{(5, 6); (6, 5)\\}$ (2 pairs)\n"
        "• Sum = 12: $\\{(6, 6)\\}$ (1 pair)\n"
        "Total favourable outcomes $n(E) = 2 + 1 = 3$.\n"
        "$$P(\\text{Sum} > 10) = \\frac{3}{36} = \\frac{1}{12}$$"
    )
    return {
        "subskill": "26_compound_event_sum_of_two_dice_greater_than_ten",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/12",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify 3 favourable pairs: (5,6), (6,5), (6,6)", "marks": 1},
            {"step": "Simplify 3/36 to 1/12", "marks": 1},
        ],
        "hints": [
            "Strictly greater than 10 means sums of 11 or 12.",
            "List pairs: (5,6), (6,5), (6,6) -> 3 pairs out of 36. Simplify 3/36.",
        ],
        "misconception_tags": ["two_dice_inequality_sum_error"],
    }


# -----------------------------------------------------------------------------
# 27. Compound Event: Sum of Two Dice Doubles
# -----------------------------------------------------------------------------
def arch_27_compound_event_sum_of_two_dice_doubles(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two standard six-sided dice are rolled.\n"
        "Calculate the probability of rolling **doubles** (both dice displaying the identical number), "
        "giving your answer as a simplified fraction."
    )
    ans_str = "\\frac{1}{6}"
    sol = (
        "Total outcomes $n(S) = 36$.\n"
        "Doubles pairs: $\\{(1, 1); (2, 2); (3, 3); (4, 4); (5, 5); (6, 6)\\}$, so $n(E) = 6$.\n"
        "$$P(\\text{Doubles}) = \\frac{6}{36} = \\frac{1}{6}$$"
    )
    return {
        "subskill": "27_compound_event_sum_of_two_dice_doubles",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/6",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "List 6 doubles pairs: (1,1) through (6,6)", "marks": 1},
            {"step": "Simplify 6/36 to 1/6", "marks": 1},
        ],
        "hints": [
            "There are 6 possible matching pairs out of 36 total.",
            "6 ÷ 36 simplifies to 1/6.",
        ],
        "misconception_tags": ["doubles_pair_counting_error"],
    }


# -----------------------------------------------------------------------------
# 28. Tree Diagram: Two-Stage Coin Tosses
# -----------------------------------------------------------------------------
def arch_28_tree_diagram_two_stage_coin_tosses(r: random.Random) -> Dict[str, Any]:
    seed_val = r.randint(100, 999999)
    svg = draw_two_stage_tree_diagram_svg(
        stage1_labels=["H", "T"],
        stage1_probs=["1/2", "1/2"],
        stage2_labels=[["H", "T"], ["H", "T"]],
        stage2_probs=[["1/2", "1/2"], ["1/2", "1/2"]],
        title="Two Coin Flips Tree Diagram",
        seed=seed_val,
    )
    prompt = (
        "A fair coin is tossed twice in succession.\n"
        "Using the probabilities along the branches, calculate the probability of obtaining "
        "**one Head and one Tail in any order** (HT or TH) as a simplified fraction."
    )
    ans_str = "\\frac{1}{2}"
    sol = (
        "From the tree branches:\n"
        "• $P(H, T) = \\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}$\n"
        "• $P(T, H) = \\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}$\n"
        "$$P(\\text{one H and one T}) = \\frac{1}{4} + \\frac{1}{4} = \\frac{2}{4} = \\frac{1}{2}$$"
    )
    return {
        "subskill": "28_tree_diagram_two_stage_coin_tosses",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": "1/2",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Calculate branch probabilities: 1/4 and 1/4", "marks": 1},
            {"step": "Sum to get 2/4 = 1/2", "marks": 1},
        ],
        "hints": [
            "Multiply along the branches for (H, T): 1/2 × 1/2 = 1/4.",
            "Multiply for (T, H): 1/2 × 1/2 = 1/4. Add both outcomes together.",
        ],
        "misconception_tags": ["tree_diagram_branch_addition_vs_multiplication_confusion"],
    }


# -----------------------------------------------------------------------------
# 29. Tree Diagram: Independent Drawing With Replacement
# -----------------------------------------------------------------------------
def arch_29_tree_diagram_independent_drawing_with_replacement(r: random.Random) -> Dict[str, Any]:
    # Bag: 3 Red, 2 Blue (Total = 5)
    # Drawing with replacement -> 2nd draw remains out of 5
    prompt = (
        "A bag contains 3 Red marbles and 2 Blue marbles (Total = 5).\n"
        "A marble is selected at random, its color is recorded, and it is **placed back into the bag (with replacement)**.\n"
        "A second marble is then selected.\n"
        "Calculate the probability of selecting **two Red marbles in a row** ($P(R, R)$) as a simplified fraction."
    )
    # P(R) = 3/5, P(R, R) = 3/5 * 3/5 = 9/25
    ans_str = "\\frac{9}{25}"
    sol = (
        "Because the marble is replaced, the draws are independent and probabilities do not change:\n"
        "• Draw 1: $P(R) = \\frac{3}{5}$\n"
        "• Draw 2: $P(R) = \\frac{3}{5}$\n"
        "$$P(R, R) = \\frac{3}{5} \\times \\frac{3}{5} = \\frac{9}{25}$$"
    )
    return {
        "subskill": "29_tree_diagram_independent_drawing_with_replacement",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "9/25",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State P(R) = 3/5 for both draws (independence)", "marks": 1},
            {"step": "Multiply: 3/5 * 3/5 = 9/25", "marks": 1},
        ],
        "hints": [
            "With replacement, the total marbles remain 5 for the second draw.",
            "Multiply 3/5 by 3/5.",
        ],
        "misconception_tags": ["with_replacement_denominator_reduction_error"],
    }


# -----------------------------------------------------------------------------
# 30. Tree Diagram: Dependent Drawing Without Replacement
# -----------------------------------------------------------------------------
def arch_30_tree_diagram_dependent_drawing_without_replacement(r: random.Random) -> Dict[str, Any]:
    # Bag: 3 Red, 2 Blue (Total = 5)
    # Drawing without replacement -> 1st is 3/5, 2nd is 2/4
    prompt = (
        "A bag contains 3 Red marbles and 2 Blue marbles (Total = 5).\n"
        "One marble is drawn at random and **NOT replaced** in the bag.\n"
        "A second marble is then drawn.\n"
        "Calculate the probability that **both drawn marbles are Red** ($P(R, R)$), "
        "giving your answer as a simplified fraction."
    )
    # 3/5 * 2/4 = 6/20 = 3/10
    ans_str = "\\frac{3}{10}"
    sol = (
        "Because the first marble is not replaced, the total number of marbles decreases to 4:\n"
        "• 1st draw: $P(R_1) = \\frac{3}{5}$\n"
        "• 2nd draw: Remaining Red = 2, Total remaining = 4, so $P(R_2 \\mid R_1) = \\frac{2}{4} = \\frac{1}{2}$\n"
        "$$P(R_1 \\text{ and } R_2) = \\frac{3}{5} \\times \\frac{2}{4} = \\frac{6}{20} = \\frac{3}{10}$$"
    )
    return {
        "subskill": "30_tree_diagram_dependent_drawing_without_replacement",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "3/10",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify 2nd draw probability is 2/4", "marks": 1},
            {"step": "Multiply and simplify: (3/5) * (2/4) = 6/20 = 3/10", "marks": 1},
        ],
        "hints": [
            "After removing one red marble, how many red marbles remain? (2).",
            "How many total marbles remain in the bag? (4). Multiply 3/5 × 2/4.",
        ],
        "misconception_tags": ["without_replacement_fixed_denominator_error"],
    }


# -----------------------------------------------------------------------------
# 31. Tree Diagram: Weather Rain on Consecutive Days
# -----------------------------------------------------------------------------
def arch_31_tree_diagram_weather_rain_consecutive_days(r: random.Random) -> Dict[str, Any]:
    # P(Rain Saturday) = 0.4. If Rain Saturday, P(Rain Sunday) = 0.6.
    p_sat = 0.4
    p_sun_given_rain = 0.6
    p_both = round(p_sat * p_sun_given_rain, 2)  # 0.24

    prompt = (
        f"The probability of rain on Saturday is {p_sat}.\n"
        f"If it rains on Saturday, the probability of rain on Sunday increases to {p_sun_given_rain}.\n"
        f"Calculate the probability that it **rains on both Saturday and Sunday** (as a decimal and a percentage)."
    )
    pct = round(p_both * 100)
    ans_str = f"Decimal: {_fmt(p_both, 2)}; Percentage: {pct}%"
    sol = (
        f"$$P(\\text{{Rain Sat and Rain Sun}}) = P(\\text{{Sat}}) \\times P(\\text{{Sun}} \\mid \\text{{Sat}}) = {p_sat} \\times {p_sun_given_rain} = {_fmt(p_both, 2)}$$\n"
        f"As a percentage: ${pct}\\%$"
    )
    return {
        "subskill": "31_tree_diagram_weather_rain_consecutive_days",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.01,
        "marking_schema": [
            {"step": f"Multiply: 0.4 * 0.6 = {_fmt(p_both, 2)}", "marks": 1},
            {"step": f"Convert to percentage: {pct}%", "marks": 1},
        ],
        "hints": [
            "Multiply the probability of Saturday rain by Sunday rain: 0,4 × 0,6.",
            "Multiply the result by 100 for the percentage.",
        ],
        "misconception_tags": ["sequential_conditional_multiplication_error"],
    }


# -----------------------------------------------------------------------------
# 32. Two-Way Contingency Table: Joint Probability
# -----------------------------------------------------------------------------
def arch_32_two_way_table_gender_and_preferred_sport_joint_prob(r: random.Random) -> Dict[str, Any]:
    # 100 learners: Boys Soccer 30, Boys Rugby 20 (Total Boys 50)
    # Girls Soccer 25, Girls Netball 25 (Total Girls 50)
    prompt = (
        "A survey of 100 Grade 9 learners recorded preferred sports in a contingency table:\n\n"
        "| Gender | Soccer | Rugby / Netball | Total |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| Boys | 30 | 20 | 50 |\n"
        "| Girls | 25 | 25 | 50 |\n"
        "| **Total** | **55** | **45** | **100** |\n\n"
        "One learner is chosen at random from the 100 learners.\n"
        "Calculate the probability of selecting a **Boy who prefers Soccer** (as a simplified fraction and decimal)."
    )
    ans_str = "Fraction: 3/10; Decimal: 0,3"
    sol = (
        "Total learners $N = 100$.\n"
        "Learners who are Boys AND prefer Soccer: $n(E) = 30$.\n"
        "$$P(\\text{Boy and Soccer}) = \\frac{30}{100} = \\frac{3}{10} = 0,3$$"
    )
    return {
        "subskill": "32_two_way_table_gender_and_preferred_sport_joint_prob",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "3/10 (0,3)",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify intersection cell: 30", "marks": 1},
            {"step": "Divide by grand total 100: 30/100 = 3/10 = 0,3", "marks": 1},
        ],
        "hints": [
            "Find the row for Boys and column for Soccer (30).",
            "Divide by the grand total in the bottom-right corner (100).",
        ],
        "misconception_tags": ["joint_vs_marginal_table_reading_error"],
    }


# -----------------------------------------------------------------------------
# 33. Two-Way Contingency Table: Marginal Probability
# -----------------------------------------------------------------------------
def arch_33_two_way_table_gender_and_preferred_sport_marginal_prob(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Using the same survey of 100 learners:\n\n"
        "| Gender | Soccer | Rugby / Netball | Total |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| Boys | 30 | 20 | 50 |\n"
        "| Girls | 25 | 25 | 50 |\n"
        "| **Total** | **55** | **45** | **100** |\n\n"
        "Calculate the probability that a randomly chosen learner **prefers Soccer** (regardless of gender), "
        "giving your answer as a simplified fraction and percentage."
    )
    ans_str = "Fraction: 11/20; Percentage: 55%"
    sol = (
        "Total learners who prefer Soccer = $30 + 25 = 55$.\n"
        "Grand total $N = 100$.\n"
        "$$P(\\text{Soccer}) = \\frac{55}{100} = \\frac{11}{20} = 55\\%$$"
    )
    return {
        "subskill": "33_two_way_table_gender_and_preferred_sport_marginal_prob",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "11/20 (55%)",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify total Soccer column: 55", "marks": 1},
            {"step": "Simplify 55/100 to 11/20 (55%)", "marks": 1},
        ],
        "hints": [
            "Look at the column total for Soccer at the bottom: 55.",
            "Divide 55 by 100 and simplify by dividing by 5.",
        ],
        "misconception_tags": ["marginal_row_column_confusion"],
    }


# -----------------------------------------------------------------------------
# 34. Two-Way Table: Subject Choice and Grade
# -----------------------------------------------------------------------------
def arch_34_two_way_table_subject_choice_and_grade(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A school records learner participation in Art vs Music across two grades:\n\n"
        "| Grade | Art | Music | Total |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| Grade 8 | 40 | 60 | 100 |\n"
        "| Grade 9 | 50 | 50 | 100 |\n"
        "| **Total** | **90** | **110** | **200** |\n\n"
        "If a learner is selected at random from the 200 learners, calculate the probability that the learner is in **Grade 9 AND takes Art**, "
        "expressed as a simplified fraction."
    )
    ans_str = "\\frac{1}{4}"
    sol = (
        "Number of learners in Grade 9 taking Art: $n(E) = 50$.\n"
        "Grand total learners: $n(S) = 200$.\n"
        "$$P(\\text{Grade 9 and Art}) = \\frac{50}{200} = \\frac{1}{4}$$"
    )
    return {
        "subskill": "34_two_way_table_subject_choice_and_grade",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/4",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify cell count 50", "marks": 1},
            {"step": "Simplify 50/200 to 1/4", "marks": 1},
        ],
        "hints": [
            "Find the row for Grade 9 and column for Art: 50.",
            "Divide by the grand total 200.",
        ],
        "misconception_tags": ["table_cell_identification_error"],
    }


# -----------------------------------------------------------------------------
# 35. Two-Way Table: Pass/Fail and Attendance
# -----------------------------------------------------------------------------
def arch_35_two_way_table_pass_fail_and_attendance(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "An academic analysis classifies 150 learners by attendance and exam outcome:\n\n"
        "| Attendance | Passed Exam | Failed Exam | Total |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| High Attendance ($\\ge 90\\%$) | 90 | 10 | 100 |\n"
        "| Low Attendance ($< 90\\%$) | 15 | 35 | 50 |\n"
        "| **Total** | **105** | **45** | **150** |\n\n"
        "Calculate the probability that a randomly chosen learner **failed the exam**, "
        "giving your answer as a simplified fraction."
    )
    ans_str = "\\frac{3}{10}"
    sol = (
        "Total learners who failed: $n(\\text{Failed}) = 45$.\n"
        "Grand total: $n(S) = 150$.\n"
        "$$P(\\text{Failed}) = \\frac{45}{150} = \\frac{3}{10} = 0,3$$"
    )
    return {
        "subskill": "35_two_way_table_pass_fail_and_attendance",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "3/10",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify 45 total failures", "marks": 1},
            {"step": "Simplify 45/150 to 3/10", "marks": 1},
        ],
        "hints": [
            "Look at the column total for 'Failed Exam' (45).",
            "Divide 45 by 150 and simplify by dividing by 15.",
        ],
        "misconception_tags": ["table_marginal_failure_rate_error"],
    }


# -----------------------------------------------------------------------------
# 36. Venn Diagram Probability: Two Sets Intersection
# -----------------------------------------------------------------------------
def arch_36_venn_diagram_probability_two_sets_intersection(r: random.Random) -> Dict[str, Any]:
    # In a class of 30 learners: 18 play Soccer (S), 14 play Netball (N), 6 play both.
    total = 30
    both = 6
    only_s = 18 - both  # 12
    only_n = 14 - both  # 8
    neither = total - (only_s + only_n + both)  # 30 - 26 = 4

    prompt = (
        f"In a Grade 9 class of {total} learners:\n"
        f"• 18 play Soccer ($S$)\n"
        f"• 14 play Netball ($N$)\n"
        f"• {both} play both Soccer and Netball ($S \\cap N$)\n\n"
        f"A learner is selected at random from the class.\n"
        f"Calculate the probability that the learner plays **both Soccer and Netball** ($P(S \\cap N)$), "
        f"giving your answer as a simplified fraction."
    )
    ans_str = "\\frac{1}{5}"
    sol = (
        f"The number of learners in the intersection $n(S \\cap N) = {both}$.\n"
        f"Total learners $n(U) = {total}$.\n"
        f"$$P(S \\cap N) = \\frac{{{both}}}{{{total}}} = \\frac{{1}}{{5}}$$"
    )
    return {
        "subskill": "36_venn_diagram_probability_two_sets_intersection",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/5",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State intersection count n(S cap N) = {both}", "marks": 1},
            {"step": f"Simplify {both}/{total} to 1/5", "marks": 1},
        ],
        "hints": [
            f"The question directly gives the count for both: {both}.",
            f"Divide {both} by the class total ({total}) and simplify.",
        ],
        "misconception_tags": ["intersection_definition_confusion"],
    }


# -----------------------------------------------------------------------------
# 37. Venn Diagram Probability: Two Sets Union
# -----------------------------------------------------------------------------
def arch_37_venn_diagram_probability_two_sets_union(r: random.Random) -> Dict[str, Any]:
    total = 30
    both = 6
    only_s = 12
    only_n = 8
    union_count = only_s + only_n + both  # 26

    prompt = (
        f"Using the same class of {total} learners where 18 play Soccer, 14 play Netball, and 6 play both:\n"
        f"Calculate the probability that a randomly chosen learner plays **Soccer OR Netball** ($P(S \\cup N)$), "
        f"giving your answer as a simplified fraction."
    )
    ans_str = "\\frac{13}{15}"
    sol = (
        f"Using the addition rule for sets:\n"
        f"$$n(S \\cup N) = n(S) + n(N) - n(S \\cap N) = 18 + 14 - 6 = {union_count}$$\n"
        f"$$P(S \\cup N) = \\frac{{{union_count}}}{{{total}}} = \\frac{{13}}{{15}}$$"
    )
    return {
        "subskill": "37_venn_diagram_probability_two_sets_union",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "13/15",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate union count: 18 + 14 - 6 = {union_count}", "marks": 1},
            {"step": f"Simplify {union_count}/{total} to 13/15", "marks": 1},
        ],
        "hints": [
            "Union = n(S) + n(N) − n(both) to avoid double counting.",
            f"18 + 14 − 6 = {union_count}. Divide {union_count} by {total}.",
        ],
        "misconception_tags": ["double_counting_intersection_in_union"],
    }


# -----------------------------------------------------------------------------
# 38. Venn Diagram Probability: Complement (Neither Set)
# -----------------------------------------------------------------------------
def arch_38_venn_diagram_probability_complement_neither_set(r: random.Random) -> Dict[str, Any]:
    total = 30
    union_count = 26
    neither = total - union_count  # 4

    prompt = (
        f"In a class of {total} learners, 26 learners play either Soccer or Netball (or both).\n"
        f"Calculate the probability that a randomly chosen learner plays **neither Soccer nor Netball**, "
        f"expressing your answer as a simplified fraction."
    )
    ans_str = "\\frac{2}{15}"
    sol = (
        f"Number of learners playing neither sport:\n"
        f"$$n(\\text{{Neither}}) = {total} - {union_count} = {neither}$$\n"
        f"$$P(\\text{{Neither}}) = \\frac{{{neither}}}{{{total}}} = \\frac{{2}}{{15}}$$"
    )
    return {
        "subskill": "38_venn_diagram_probability_complement_neither_set",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "2/15",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Subtract union from total: {total} - {union_count} = {neither}", "marks": 1},
            {"step": f"Simplify {neither}/{total} to 2/15", "marks": 1},
        ],
        "hints": [
            f"Subtract 26 from {total} to find learners outside the circles.",
            f"Divide {neither} by {total} and simplify.",
        ],
        "misconception_tags": ["venn_complement_subtraction_error"],
    }


# -----------------------------------------------------------------------------
# 39. Mutually Exclusive Events: Definition and Addition Rule
# -----------------------------------------------------------------------------
def arch_39_mutually_exclusive_events_definition_and_addition_rule(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A standard six-sided die is rolled.\n"
        "Let Event $A$ = rolling a 2, and Event $B$ = rolling a 5.\n"
        "1. Explain why Event $A$ and Event $B$ are **mutually exclusive**.\n"
        "2. Calculate $P(A \\text{ or } B)$ as a simplified fraction."
    )
    ans_str = "\\frac{1}{3}"
    sol = (
        "1. Events $A$ and $B$ are **mutually exclusive** because a single die roll cannot land on both 2 and 5 simultaneously "
        "($A \\cap B = \\emptyset$, so $P(A \\cap B) = 0$).\n"
        "2. Addition rule for mutually exclusive events:\n"
        "$$P(A \\text{ or } B) = P(A) + P(B) = \\frac{1}{6} + \\frac{1}{6} = \\frac{2}{6} = \\frac{1}{3}$$"
    )
    return {
        "subskill": "39_mutually_exclusive_events_definition_and_addition_rule",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/3",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Explain mutually exclusive: cannot happen at the same time", "marks": 1},
            {"step": "Add probabilities: 1/6 + 1/6 = 2/6 = 1/3", "marks": 1},
        ],
        "hints": [
            "Can a die roll show both 2 and 5 on one single roll?",
            "For mutually exclusive events: P(A or B) = P(A) + P(B).",
        ],
        "misconception_tags": ["mutually_exclusive_addition_rule_confusion"],
    }


# -----------------------------------------------------------------------------
# 40. Non-Mutually Exclusive Events: Addition Rule
# -----------------------------------------------------------------------------
def arch_40_non_mutually_exclusive_events_addition_rule_subtraction(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A card is drawn from a standard 52-card deck.\n"
        "Let Event $A$ = drawing a King (4 Kings in deck).\n"
        "Let Event $B$ = drawing a Heart (13 Hearts in deck).\n"
        "1. Are Events $A$ and $B$ mutually exclusive? Explain.\n"
        "2. Calculate $P(A \\text{ or } B)$ as a simplified fraction."
    )
    ans_str = "\\frac{4}{13}"
    sol = (
        "1. **No**, they are not mutually exclusive because the King of Hearts belongs to both sets ($A \\cap B = \\{\\text{King of Hearts}\\}$).\n"
        "2. General addition rule:\n"
        "$$P(A \\text{ or } B) = P(A) + P(B) - P(A \\cap B) = \\frac{4}{52} + \\frac{13}{52} - \\frac{1}{52} = \\frac{16}{52} = \\frac{4}{13}$$"
    )
    return {
        "subskill": "40_non_mutually_exclusive_events_addition_rule_subtraction",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "4/13",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State NOT mutually exclusive because King of Hearts exists", "marks": 1},
            {"step": "Apply formula: (4 + 13 - 1)/52 = 16/52 = 4/13", "marks": 1},
        ],
        "hints": [
            "Is there a card that is BOTH a King and a Heart? Yes, the King of Hearts.",
            "Subtract 1/52 to prevent counting the King of Hearts twice.",
        ],
        "misconception_tags": ["non_mutually_exclusive_double_count_error"],
    }


# -----------------------------------------------------------------------------
# 41. Determining Fairness of a Game (Expected Value Concept)
# -----------------------------------------------------------------------------
def arch_41_determining_fairness_of_game_expected_payout(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "At a school carnival, a player pays R5 to roll a fair six-sided die. "
        "If they roll a 6, they win R24. If they roll anything else (1, 2, 3, 4, 5), they win nothing.\n"
        "1. Calculate the probability of winning R24 ($P(6)$).\n"
        "2. Calculate the average expected payout per roll ($\\frac{1}{6} \\times \\text{R}24$).\n"
        "3. Is the game mathematically fair to the player? Explain."
    )
    ans_str = "P(win) = 1/6; Expected payout = R4; Game is not fair (player loses R1 on average per game)"
    sol = (
        "1. $P(\\text{Win}) = P(6) = \\frac{1}{6}$.\n"
        "2. Expected payout = $\\frac{1}{6} \\times \\text{R}24 = \\text{R}4$.\n"
        "3. **The game is not fair**: The player pays R5 to play, but only wins back an average of R4 per roll. "
        "The player expects to lose R1 per roll on average."
    )
    return {
        "subskill": "41_determining_fairness_of_game_expected_payout",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "P(win) = 1/6", "marks": 1},
            {"step": "Expected return: (1/6) * R24 = R4", "marks": 1},
            {"step": "Explain unfairness: cost R5 exceeds expected return R4", "marks": 1},
        ],
        "hints": [
            "P(rolling a 6) = 1/6.",
            "Multiply 1/6 by R24 = R4. Compare R4 to the R5 entry fee.",
        ],
        "misconception_tags": ["fair_game_expected_value_error"],
    }


# -----------------------------------------------------------------------------
# 42. Frequency Tree: Hospital Test Results
# -----------------------------------------------------------------------------
def arch_42_frequency_tree_hospital_test_results(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Out of 1 000 patients tested for a condition:\n"
        "• 100 actually have the condition (90 test positive, 10 test negative)\n"
        "• 900 do NOT have the condition (45 test positive falsely, 855 test negative correctly)\n\n"
        "1. How many total patients tested positive?\n"
        "2. What is the probability that a randomly chosen patient tested positive?"
    )
    total_pos = 90 + 45  # 135
    pct = round((total_pos / 1000) * 100, 1)  # 13.5%
    ans_str = f"Total positive: {total_pos}; Probability: 135/1000 = 27/200 ({_fmt(pct)}%)"
    sol = (
        f"1. Total positive tests: $90 + 45 = {total_pos}$.\n"
        f"2. $$P(\\text{{Positive}}) = \\frac{{{total_pos}}}{{1\\,000}} = \\frac{{27}}{{200}} = {_fmt(pct)}\\%$$"
    )
    return {
        "subskill": "42_frequency_tree_hospital_test_results",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": f"27/200 ({_fmt(pct)}%)",
        "sample_answer": ans_str,
        "tolerance": 0.1,
        "marking_schema": [
            {"step": f"Calculate total positive tests: {total_pos}", "marks": 1},
            {"step": f"Probability: {total_pos}/1000 = 27/200", "marks": 1},
        ],
        "hints": [
            "Add true positives (90) and false positives (45).",
            f"Divide {total_pos} by 1 000.",
        ],
        "misconception_tags": ["false_positive_frequency_tree_error"],
    }


# -----------------------------------------------------------------------------
# 43. Marble Bag: Probability of Neither Color
# -----------------------------------------------------------------------------
def arch_43_marble_bag_three_colors_probability_of_neither_color(r: random.Random) -> Dict[str, Any]:
    red = 4
    blue = 5
    yellow = 6
    total = red + blue + yellow  # 15

    prompt = (
        f"A bag holds {red} red, {blue} blue, and {yellow} yellow marbles (Total = {total}).\n"
        f"One marble is selected at random.\n"
        f"Calculate the probability of selecting a marble that is **neither Red nor Blue**, "
        f"giving your answer as a simplified fraction."
    )
    # neither red nor blue = yellow = 6/15 = 2/5
    ans_str = "\\frac{2}{5}"
    sol = (
        f"Neither Red nor Blue means drawing a **Yellow marble**:\n"
        f"$$n(\\text{{Yellow}}) = {yellow}$$\n"
        f"$$P(\\text{{neither Red nor Blue}}) = \\frac{{{yellow}}}{{{total}}} = \\frac{{2}}{{5}}$$"
    )
    return {
        "subskill": "43_marble_bag_three_colors_probability_of_neither_color",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "2/5",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify favourable outcomes = Yellow ({yellow})", "marks": 1},
            {"step": f"Simplify {yellow}/{total} to 2/5", "marks": 1},
        ],
        "hints": [
            "If it is not Red and not Blue, what color must it be?",
            f"It must be Yellow ({yellow} marbles). Simplify {yellow}/{total}.",
        ],
        "misconception_tags": ["neither_nor_logic_in_probability"],
    }


# -----------------------------------------------------------------------------
# 44. Card Selection Without Replacement: Two Aces
# -----------------------------------------------------------------------------
def arch_44_card_selection_without_replacement_two_aces(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two cards are dealt at random from a standard 52-card deck without replacement.\n"
        "Calculate the probability that **both cards are Aces**, expressing your answer as a simplified fraction."
    )
    # 4/52 * 3/51 = (1/13) * (1/17) = 1/221
    ans_str = "\\frac{1}{221}"
    sol = (
        "• 1st card: 4 Aces out of 52 cards: $P(A_1) = \\frac{4}{52} = \\frac{1}{13}$\n"
        "• 2nd card: 3 Aces remaining out of 51 cards: $P(A_2 \\mid A_1) = \\frac{3}{51} = \\frac{1}{17}$\n"
        "$$P(\\text{both Aces}) = \\frac{1}{13} \\times \\frac{1}{17} = \\frac{1}{221}$$"
    )
    return {
        "subskill": "44_card_selection_without_replacement_two_aces",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "1/221",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "First draw: 4/52 = 1/13", "marks": 1},
            {"step": "Second draw: 3/51 = 1/17", "marks": 1},
            {"step": "Product: 1/221", "marks": 1},
        ],
        "hints": [
            "For the first card: 4/52.",
            "For the second card: only 3 Aces remain out of 51 cards.",
        ],
        "misconception_tags": ["dependent_card_draw_without_replacement_error"],
    }


# -----------------------------------------------------------------------------
# 45. Sock Drawer: Matching Pair Without Replacement
# -----------------------------------------------------------------------------
def arch_45_sock_drawer_drawing_matching_pair_without_replacement(r: random.Random) -> Dict[str, Any]:
    # Drawer: 4 black socks, 6 white socks (Total = 10)
    # P(two black) = 4/10 * 3/9 = 12/90 = 2/15
    prompt = (
        "A drawer contains 4 black socks and 6 white socks (Total = 10 socks).\n"
        "Two socks are pulled out at random in the dark (without replacement).\n"
        "Calculate the probability of selecting **two black socks**, as a simplified fraction."
    )
    ans_str = "\\frac{2}{15}"
    sol = (
        "• 1st sock Black: $P(B_1) = \\frac{4}{10} = \\frac{2}{5}$\n"
        "• 2nd sock Black: $P(B_2 \\mid B_1) = \\frac{3}{9} = \\frac{1}{3}$\n"
        "$$P(\\text{both Black}) = \\frac{2}{5} \\times \\frac{1}{3} = \\frac{2}{15}$$"
    )
    return {
        "subskill": "45_sock_drawer_drawing_matching_pair_without_replacement",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "2/15",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "P(1st black) = 4/10", "marks": 1},
            {"step": "P(2nd black) = 3/9", "marks": 1},
            {"step": "Multiply: (4/10) * (3/9) = 12/90 = 2/15", "marks": 1},
        ],
        "hints": [
            "After taking one black sock, 3 black socks remain out of 9 total.",
            "Multiply 4/10 × 3/9 and simplify.",
        ],
        "misconception_tags": ["sock_drawer_without_replacement_error"],
    }


# -----------------------------------------------------------------------------
# 46. Traffic Light: Independent Probability Consecutive Greens
# -----------------------------------------------------------------------------
def arch_46_traffic_light_independent_probability_two_consecutive_greens(r: random.Random) -> Dict[str, Any]:
    p_green = 0.6
    p_both = round(p_green * p_green, 2)  # 0.36

    prompt = (
        f"A commuter drives through two independent traffic lights. "
        f"Each light has a probability of {p_green} of being green when the commuter arrives.\n"
        f"Calculate the probability that **both traffic lights are green** (as a decimal and a percentage)."
    )
    pct = round(p_both * 100)
    ans_str = f"Decimal: {_fmt(p_both, 2)}; Percentage: {pct}%"
    sol = (
        f"Because the traffic lights operate independently:\n"
        f"$$P(\\text{{both green}}) = P(G_1) \\times P(G_2) = {p_green} \\times {p_green} = {_fmt(p_both, 2)}$$\n"
        f"As a percentage: ${pct}\\%$"
    )
    return {
        "subskill": "46_traffic_light_independent_probability_two_consecutive_greens",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.01,
        "marking_schema": [
            {"step": f"Multiply 0.6 * 0.6 = {_fmt(p_both, 2)}", "marks": 1},
            {"step": f"Convert to percentage: {pct}%", "marks": 1},
        ],
        "hints": [
            "For independent events, multiply the probabilities: 0,6 × 0,6.",
            "Convert the resulting decimal to a percentage by multiplying by 100.",
        ],
        "misconception_tags": ["independent_multiplication_rule_error"],
    }


# -----------------------------------------------------------------------------
# 47. Subject Grade Probability from School Contingency Table
# -----------------------------------------------------------------------------
def arch_47_subject_grade_probability_from_school_contingency_table(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A school records 80 learners achieving level 7 (distinctions):\n\n"
        "| Subject | Boys | Girls | Total |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| Mathematics | 24 | 16 | 40 |\n"
        "| Physical Sciences | 16 | 24 | 40 |\n"
        "| **Total** | **40** | **40** | **80** |\n\n"
        "One distinction achiever is chosen at random.\n"
        "Calculate the probability of selecting a **Girl who achieved a distinction in Physical Sciences**, "
        "giving your answer as a simplified fraction."
    )
    # 24 / 80 = 3/10
    ans_str = "\\frac{3}{10}"
    sol = (
        "Number of Girls with Science distinctions: $n(E) = 24$.\n"
        "Grand total distinction learners: $n(S) = 80$.\n"
        "$$P(\\text{Girl and Science}) = \\frac{24}{80} = \\frac{3}{10} = 0,3$$"
    )
    return {
        "subskill": "47_subject_grade_probability_from_school_contingency_table",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "3/10",
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify intersection count 24", "marks": 1},
            {"step": "Simplify 24/80 to 3/10", "marks": 1},
        ],
        "hints": [
            "Find the cell where 'Physical Sciences' and 'Girls' meet (24).",
            "Divide 24 by the total 80 and simplify by dividing by 8.",
        ],
        "misconception_tags": ["contingency_table_cell_probability_error"],
    }


# -----------------------------------------------------------------------------
# 48. Relative Frequency Prediction for Future Large Trials
# -----------------------------------------------------------------------------
def arch_48_relative_frequency_prediction_for_future_large_trials(r: random.Random) -> Dict[str, Any]:
    defect_rate = 0.02  # 2%
    future_n = 5000
    expected_defects = int(future_n * defect_rate)  # 100

    prompt = (
        f"A factory quality controller inspects a sample of parts and finds a defect rate of {int(defect_rate * 100)}% "
        f"(probability of defect = {defect_rate}).\n"
        f"In a production run of $N = {future_n}$ parts, how many defective parts should the factory expect?"
    )
    ans_str = str(expected_defects)
    sol = (
        f"$$\\text{{Expected Defective Parts}} = N \\times P(\\text{{Defect}}) = {future_n} \\times {defect_rate} = {expected_defects}$$"
    )
    return {
        "subskill": "48_relative_frequency_prediction_for_future_large_trials",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": f"{ans_str} defective parts",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Multiply {future_n} * {defect_rate} = {expected_defects}", "marks": 1},
        ],
        "hints": [
            f"Multiply the total parts ({future_n}) by the probability ({defect_rate}).",
            f"{future_n} × 0,02 = {expected_defects}.",
        ],
        "misconception_tags": ["expected_frequency_product_error"],
    }


# -----------------------------------------------------------------------------
# 49. Compare Theoretical Probability with Experimental Bias Check
# -----------------------------------------------------------------------------
def arch_49_compare_theoretical_probability_with_experimental_bias_check(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner rolls a suspected loaded die 600 times and records the number 6 a total of 250 times.\n"
        "1. What is the theoretical expected number of sixes for a fair die over 600 rolls?\n"
        "2. Calculate the relative frequency of rolling a 6 (to 3 decimal places).\n"
        "3. Does this experimental evidence suggest the die is biased? Explain."
    )
    # Expected: 600 * 1/6 = 100. Observed: 250 (rel freq 250/600 = 0.417 vs theo 0.167)
    ans_str = "Expected: 100; Relative frequency: 0,417 (vs theoretical 0,167); The die is heavily biased toward 6"
    sol = (
        "1. For a fair die: $\\text{Expected} = 600 \\times \\frac{1}{6} = 100$ sixes.\n"
        "2. Relative frequency $= \\frac{250}{600} \\approx 0,417$.\n"
        "3. **Yes, the die is biased**. Rolling 250 sixes when only 100 were expected over 600 trials is an extreme "
        "deviation that cannot reasonably be explained by chance alone."
    )
    return {
        "subskill": "49_compare_theoretical_probability_with_experimental_bias_check",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": sol,
        "tolerance": 0.005,
        "marking_schema": [
            {"step": "Calculate theoretical expected: 600 * (1/6) = 100", "marks": 1},
            {"step": "Calculate relative frequency: 250/600 ≈ 0,417", "marks": 1},
            {"step": "Conclude die is biased based on huge discrepancy", "marks": 1},
        ],
        "hints": [
            "A fair die should produce each number about 1/6 of the time: 600 ÷ 6 = 100.",
            "Compare 250 actual sixes to the expected 100 sixes.",
        ],
        "misconception_tags": ["die_fairness_statistical_deviation_unrecognised"],
    }


# -----------------------------------------------------------------------------
# 50. Compound Multi-Stage Decision Tree Synthesis
# -----------------------------------------------------------------------------
def arch_50_compound_multi_stage_probability_decision_tree_synthesis(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "A quality control system checks light bulbs in two successive stages:\n"
        "• Stage 1 (Filament check): 90% of bulbs pass, 10% fail.\n"
        "• Stage 2 (Vacuum seal check): Of the bulbs that pass Stage 1, 95% pass and 5% fail.\n\n"
        "1. Calculate the probability that a randomly chosen bulb passes **both inspection stages** (as a decimal and percentage).\n"
        "2. Out of a daily batch of 10 000 light bulbs, how many are expected to pass both stages successfully?"
    )
    p_both = round(0.90 * 0.95, 4)  # 0.855
    expected_qty = int(10000 * p_both)  # 8550
    pct = round(p_both * 100, 1)

    ans_str = f"P(passes both) = {_fmt(p_both, 3)} ({_fmt(pct)}%); Expected bulbs = {expected_qty}"
    sol = (
        f"1. $$P(\\text{{Pass Both}}) = P(\\text{{Stage 1 Pass}}) \\times P(\\text{{Stage 2 Pass}} \\mid \\text{{Stage 1 Pass}}) = 0,90 \\times 0,95 = {_fmt(p_both, 3)}$$\n"
        f"As a percentage: ${_fmt(pct)}\\%$\n\n"
        f"2. Expected bulbs: $10\\,000 \\times {_fmt(p_both, 3)} = {expected_qty}$ bulbs."
    )
    return {
        "subskill": "50_compound_multi_stage_probability_decision_tree_synthesis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": f"{expected_qty} bulbs ({_fmt(pct)}%)",
        "sample_answer": ans_str,
        "tolerance": 0.005,
        "marking_schema": [
            {"step": f"Multiply 0.90 * 0.95 = {_fmt(p_both, 3)} ({_fmt(pct)}%)", "marks": 1},
            {"step": f"Calculate expected quantity: 10 000 * {_fmt(p_both, 3)} = {expected_qty}", "marks": 1},
        ],
        "hints": [
            "Multiply 0,90 by 0,95 to find the joint probability.",
            f"Multiply that probability by 10 000 to find the total expected bulbs.",
        ],
        "misconception_tags": ["multi_stage_inspection_product_error"],
    }
