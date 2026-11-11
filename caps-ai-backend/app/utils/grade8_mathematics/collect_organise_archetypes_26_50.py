"""
Grade 8 Mathematics - Collect, Organise & Summarise Data Archetypes (26 to 50).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/05. Collect organise and summarise data.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float, places: int = 1) -> str:
    s = f"{val:.{places}f}".rstrip("0").rstrip(".") if places > 1 else f"{val:.{places}f}"
    if s == "-0":
        s = "0"
    return s.replace(".", ",")


def arch_26_calculating_mean_of_ungrouped_data_set(rng: random.Random) -> Dict[str, Any]:
    n = 5
    mean_val = rng.randint(12, 28)
    # Generate 5 numbers summing to mean_val * 5
    d1 = mean_val - rng.randint(2, 6)
    d2 = mean_val - rng.randint(1, 4)
    d3 = mean_val + rng.randint(0, 3)
    d4 = mean_val + rng.randint(2, 5)
    d5 = mean_val * n - (d1 + d2 + d3 + d4)
    vals = [d1, d2, d3, d4, d5]
    rng.shuffle(vals)

    vals_str = ", ".join(str(v) for v in vals)

    return {
        "title": "Calculating Mean of Ungrouped Data",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "26_calculating_mean_of_ungrouped_data_set",
        "difficulty": "easy",
        "question_text": (
            f"Calculate the **mean** (average) of the following set of 5 numbers:\n\n"
            f"$${vals_str}$$"
        ),
        "correct_answer": str(mean_val),
        "marking_schema": [
            f"Sum numbers ({sum(vals)}) and divide by 5: {sum(vals)} / 5 = {mean_val} (2 marks)",
        ],
        "hints": [
            "Formula: $\\text{Mean} = \\frac{\\text{Sum of all values}}{\\text{Number of values}}$.",
            f"Sum = ${' + '.join(str(v) for v in vals)} = {sum(vals)}$.",
            f"Mean = $\\frac{{{sum(vals)}}}{{5}} = {mean_val}$.",
        ],
        "misconception_tags": ["mean_division_count_slip"],
        "diagram_spec": None,
    }


def arch_27_finding_median_of_ordered_data_odd_number(rng: random.Random) -> Dict[str, Any]:
    vals = sorted(rng.sample(range(10, 50), 7))
    median_val = vals[3]
    vals_str = ", ".join(str(v) for v in vals)

    return {
        "title": "Finding Median of Ordered Data (Odd Count)",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "27_finding_median_of_ordered_data_odd_number",
        "difficulty": "easy",
        "question_text": (
            f"Consider the ordered list of 7 numbers:\n\n"
            f"$${vals_str}$$\n\n"
            "Find the **median** of this data set."
        ),
        "correct_answer": str(median_val),
        "marking_schema": [
            f"Identify middle (4th) value: {median_val} (1 mark)",
        ],
        "hints": [
            "For an ordered data set with an odd count $n = 7$, the median is the middle value at position $\\frac{7 + 1}{2} = 4^{\\text{th}}$.",
            f"The 4th number in the ordered list is {median_val}.",
            f"Median = {median_val}.",
        ],
        "misconception_tags": ["median_middle_position_miscount"],
        "diagram_spec": None,
    }


def arch_28_finding_median_of_ordered_data_even_number(rng: random.Random) -> Dict[str, Any]:
    vals = sorted(rng.sample(range(12, 60), 6))
    mid1, mid2 = vals[2], vals[3]
    median_val = (mid1 + mid2) / 2.0
    med_str = _fmt_sa(median_val, 1)
    vals_str = ", ".join(str(v) for v in vals)

    return {
        "title": "Finding Median of Ordered Data (Even Count)",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "28_finding_median_of_ordered_data_even_number",
        "difficulty": "medium",
        "question_text": (
            f"Consider the ordered list of 6 values:\n\n"
            f"$${vals_str}$$\n\n"
            "Calculate the **median** of this data set."
        ),
        "correct_answer": med_str,
        "marking_schema": [
            f"Average 3rd ({mid1}) and 4th ({mid2}) values: ({mid1} + {mid2})/2 = {med_str} (2 marks)",
        ],
        "hints": [
            "When the number of values $n = 6$ is even, the median is the mean of the two central numbers (3rd and 4th).",
            f"Two central values are {mid1} and {mid2}.",
            f"Median = $\\frac{{{mid1} + {mid2}}}{{2}} = {med_str}$.",
        ],
        "misconception_tags": ["median_even_count_single_pick_error"],
        "diagram_spec": None,
    }


def arch_29_finding_median_of_unordered_data_set(rng: random.Random) -> Dict[str, Any]:
    vals = rng.sample(range(15, 65), 5)
    sorted_vals = sorted(vals)
    median_val = sorted_vals[2]
    raw_str = ", ".join(str(v) for v in vals)
    ord_str = ", ".join(str(v) for v in sorted_vals)

    return {
        "title": "Finding Median of Unordered Data",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "29_finding_median_of_unordered_data_set",
        "difficulty": "medium",
        "question_text": (
            f"Find the **median** of the following unordered data set:\n\n"
            f"$${raw_str}$$"
        ),
        "correct_answer": str(median_val),
        "marking_schema": [
            f"Arrange in ascending order ({ord_str}) [1M]",
            f"Identify middle value {median_val} [1A]",
        ],
        "hints": [
            "You must arrange the numbers in ascending order before finding the median.",
            f"Ordered list: {ord_str}.",
            f"The middle value is {median_val}.",
        ],
        "misconception_tags": ["median_without_ordering_fallacy"],
        "diagram_spec": None,
    }


def arch_30_identifying_mode_of_discrete_data_set(rng: random.Random) -> Dict[str, Any]:
    mode_val = rng.randint(14, 35)
    other_vals = rng.sample([x for x in range(10, 45) if x != mode_val], 4)
    dataset = [mode_val, mode_val, mode_val] + other_vals
    rng.shuffle(dataset)

    ds_str = ", ".join(str(v) for v in dataset)

    return {
        "title": "Identifying Mode of Discrete Data",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "30_identifying_mode_of_discrete_data_set",
        "difficulty": "easy",
        "question_text": (
            f"Identify the **mode** of the following set of values:\n\n"
            f"$${ds_str}$$"
        ),
        "correct_answer": str(mode_val),
        "marking_schema": [
            f"Identify most frequently occurring value: {mode_val} (appears 3 times) (1 mark)",
        ],
        "hints": [
            "The mode is the value that appears most often in the data set.",
            f"{mode_val} appears 3 times, while all other numbers appear once.",
            f"Mode = {mode_val}.",
        ],
        "misconception_tags": ["mode_identification_frequency_error"],
        "diagram_spec": None,
    }


def arch_31_identifying_bimodal_data_set(rng: random.Random) -> Dict[str, Any]:
    m1, m2 = sorted(rng.sample(range(10, 30), 2))
    others = rng.sample([x for x in range(10, 40) if x not in (m1, m2)], 3)
    dataset = [m1, m1, m2, m2] + others
    rng.shuffle(dataset)
    ds_str = ", ".join(str(v) for v in dataset)

    return {
        "title": "Bimodal Data Set Identification",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "31_identifying_bimodal_data_set",
        "difficulty": "medium",
        "question_text": (
            f"State the **mode(s)** of the following data set:\n\n"
            f"$${ds_str}$$"
        ),
        "correct_answer": f"{m1} and {m2} (bimodal)",
        "marking_schema": [
            f"Identify both modes {m1} and {m2}: 1 mark",
        ],
        "hints": [
            "When two values appear with the same highest frequency, the data set is bimodal.",
            f"Both {m1} and {m2} appear twice, which is more than any other number.",
            f"Modes: {m1} and {m2}.",
        ],
        "misconception_tags": ["bimodal_single_mode_assumption"],
        "diagram_spec": None,
    }


def arch_32_identifying_no_mode_in_data_set(rng: random.Random) -> Dict[str, Any]:
    vals = rng.sample(range(11, 49), 6)
    ds_str = ", ".join(str(v) for v in vals)

    return {
        "title": "Recognizing a Data Set with No Mode",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "32_identifying_no_mode_in_data_set",
        "difficulty": "easy",
        "question_text": (
            f"Consider the numbers: **{ds_str}**.\n\n"
            "State the **mode** of this data set."
        ),
        "correct_answer": "No mode",
        "marking_schema": [
            "State 'no mode' because every value occurs with equal frequency (once): 1 mark",
        ],
        "hints": [
            "A mode only exists if at least one number appears more often than the others.",
            "Here, every number appears exactly once.",
            "There is no mode (do not say 0).",
        ],
        "misconception_tags": ["mode_zero_vs_no_mode_confusion"],
        "diagram_spec": None,
    }


def arch_33_calculating_range_of_raw_data_set(rng: random.Random) -> Dict[str, Any]:
    min_v = rng.randint(8, 18)
    diff = rng.randint(22, 45)
    max_v = min_v + diff
    in_betweens = rng.sample(range(min_v + 1, max_v), 4)
    vals = [min_v, max_v] + in_betweens
    rng.shuffle(vals)
    ds_str = ", ".join(str(v) for v in vals)

    return {
        "title": "Calculating Range of Raw Data",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "33_calculating_range_of_raw_data_set",
        "difficulty": "easy",
        "question_text": (
            f"Calculate the **range** of the following set of values:\n\n"
            f"$${ds_str}$$"
        ),
        "correct_answer": str(diff),
        "marking_schema": [
            f"Range = maximum - minimum = {max_v} - {min_v} = {diff} (1 mark)",
        ],
        "hints": [
            "Range is the difference between the largest and smallest values.",
            f"Highest value = {max_v}; Lowest value = {min_v}.",
            f"$\\text{{Range}} = {max_v} - {min_v} = {diff}$.",
        ],
        "misconception_tags": ["range_extreme_identification_slip"],
        "diagram_spec": None,
    }


def arch_34_calculating_mean_with_decimal_result(rng: random.Random) -> Dict[str, Any]:
    vals = [rng.randint(10, 25) for _ in range(4)]
    tot = sum(vals)
    mean_val = round(tot / 4.0, 2)
    mean_str = _fmt_sa(mean_val, 2)
    ds_str = ", ".join(str(v) for v in vals)

    return {
        "title": "Calculating Mean with Decimal Result",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "34_calculating_mean_with_decimal_result",
        "difficulty": "medium",
        "question_text": (
            f"Calculate the **mean** of the following 4 scores, expressing your answer as a decimal fraction:\n\n"
            f"$${ds_str}$$"
        ),
        "correct_answer": mean_str,
        "marking_schema": [
            f"Sum = {tot}, Mean = {tot}/4 = {mean_str} (2 marks)",
        ],
        "hints": [
            f"Sum the 4 scores: ${' + '.join(str(v) for v in vals)} = {tot}$.",
            f"Divide by 4: $\\frac{{{tot}}}{{4}} = {mean_str}$.",
            f"Mean = {mean_str}.",
        ],
        "misconception_tags": ["mean_decimal_division_rounding_slip"],
        "diagram_spec": None,
    }


def arch_35_effect_of_extreme_value_outlier_on_mean(rng: random.Random) -> Dict[str, Any]:
    base_vals = [14, 15, 16, 17, 18]
    mean_orig = 16
    outlier = 90
    new_mean = round((sum(base_vals) + outlier) / 6.0, 1)

    return {
        "title": "Effect of an Outlier on the Mean",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "35_effect_of_extreme_value_outlier_on_mean",
        "difficulty": "medium",
        "question_text": (
            f"A data set consists of five values: **14, 15, 16, 17, 18** with a mean of **{mean_orig}**.\n\n"
            f"If an extreme outlier of **{outlier}** is added to the data set, does the mean **increase**, **decrease**, or stay the **same**?"
        ),
        "correct_answer": "Increase substantially",
        "marking_schema": [
            f"State that the mean increases significantly (to {_fmt_sa(new_mean, 1)}): 1 mark",
        ],
        "hints": [
            "The mean is sensitive to extreme values (outliers) because every value is included in the total sum.",
            f"Adding {outlier} raises the sum from 80 to 170, increasing the average from 16 to {_fmt_sa(new_mean, 1)}.",
            "The mean increases substantially.",
        ],
        "misconception_tags": ["outlier_mean_sensitivity_misunderstanding"],
        "diagram_spec": None,
    }


def arch_36_effect_of_outlier_on_median_resistance(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Resistance of Median to Outliers",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "36_effect_of_outlier_on_median_resistance",
        "difficulty": "medium",
        "question_text": (
            "Why is the **median** often preferred over the **mean** when summarizing a data set that contains extreme outliers (such as household incomes)?"
        ),
        "correct_answer": "The median is resistant to extreme values because it only depends on the middle position, not on the magnitudes of extreme numbers.",
        "marking_schema": [
            "Explain that median is not distorted/pulled by extreme outliers: 1 mark",
        ],
        "hints": [
            "Outliers pull the mean heavily in their direction (skewing the average).",
            "The median merely identifies the middle ranking value, regardless of how large the highest number is.",
            "The median provides a more realistic representation of typical values in skewed data.",
        ],
        "misconception_tags": ["median_outlier_resistance_concept_gap"],
        "diagram_spec": None,
    }


def arch_37_choosing_appropriate_measure_of_central_tendency(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A shoe store manager wants to know which shoe size to order most stock of for the new season.", "mode", "The manager needs the most popular / most frequently purchased shoe size."),
        ("A housing report describes typical home prices in a town where five luxury mansions cost R50 million while most houses cost R1,5 million.", "median", "The median is not distorted by the few extreme mansion prices."),
        ("A teacher calculates the overall class performance on an exam where marks are fairly evenly distributed without extreme outliers.", "mean", "The mean includes every learner's exact score when marks are evenly spread."),
    ]
    context, chosen_measure, reason = rng.choice(scenarios)

    return {
        "title": "Choosing Appropriate Measure of Central Tendency",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "37_choosing_appropriate_measure_of_central_tendency",
        "difficulty": "medium",
        "question_text": (
            f"Consider this scenario:\n\n"
            f"**\"{context}\"**\n\n"
            "Which measure of central tendency (**mean**, **median**, or **mode**) is most appropriate? Give a reason."
        ),
        "correct_answer": f"{chosen_measure.capitalize()}, because {reason}",
        "marking_schema": [
            f"Select {chosen_measure} with valid justification: 1 mark",
        ],
        "hints": [
            "Use mode for categorical data or finding the most popular item.",
            "Use median when data has severe outliers or is heavily skewed.",
            "Use mean for symmetric, evenly distributed numerical data.",
            f"Most appropriate: {chosen_measure.capitalize()} ({reason}).",
        ],
        "misconception_tags": ["central_tendency_measure_selection_error"],
        "diagram_spec": None,
    }


def arch_38_finding_missing_value_given_the_mean(rng: random.Random) -> Dict[str, Any]:
    target_mean = rng.randint(15, 25)
    known = [target_mean - 4, target_mean + 2, target_mean - 1, target_mean + 5]
    total_needed = target_mean * 5
    missing = total_needed - sum(known)
    known_str = ", ".join(str(k) for k in known)

    return {
        "title": "Finding Missing Value Given the Mean",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "38_finding_missing_value_given_the_mean",
        "difficulty": "hard",
        "question_text": (
            f"The mean of five test scores is **{target_mean}**.\n\n"
            f"Four of the scores are: **{known_str}**, and the fifth score is **$x$**.\n\n"
            "Calculate the value of $x$."
        ),
        "correct_answer": str(missing),
        "marking_schema": [
            f"Total sum needed = 5 * {target_mean} = {total_needed} [1M]",
            f"Subtract known sum: {total_needed} - {sum(known)} = {missing} [1A]",
        ],
        "hints": [
            f"Total required sum = $5 \\times {target_mean} = {total_needed}$.",
            f"Sum of known four values = ${sum(known)}$.",
            f"$x = {total_needed} - {sum(known)} = {missing}$.",
        ],
        "misconception_tags": ["missing_mean_value_algebraic_reversal_slip"],
        "diagram_spec": None,
    }


def arch_39_finding_missing_value_given_the_range(rng: random.Random) -> Dict[str, Any]:
    min_v = rng.randint(14, 25)
    rng_val = rng.randint(18, 35)
    max_v = min_v + rng_val

    return {
        "title": "Finding Highest Value Given the Range",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "39_finding_missing_value_given_the_range",
        "difficulty": "easy",
        "question_text": (
            f"In a set of exam marks, the range is **{rng_val}** and the lowest mark is **{min_v}**.\n\n"
            "Calculate the highest mark in the data set."
        ),
        "correct_answer": str(max_v),
        "marking_schema": [
            f"Highest = lowest + range = {min_v} + {rng_val} = {max_v} (1 mark)",
        ],
        "hints": [
            "Formula: $\\text{Range} = \\text{Highest} - \\text{Lowest}$.",
            f"$\\text{{Highest}} = \\text{{Lowest}} + \\text{{Range}} = {min_v} + {rng_val}$.",
            f"Highest mark = {max_v}.",
        ],
        "misconception_tags": ["range_formula_reversal_subtraction_error"],
        "diagram_spec": None,
    }


def arch_40_calculating_mean_from_frequency_table(rng: random.Random) -> Dict[str, Any]:
    # x = 1, 2, 3, 4
    # f = 2, 4, 3, 1 => total f = 10
    scores = [1, 2, 3, 4]
    freqs = [2, 4, 3, 1]
    products = [s * f for s, f in zip(scores, freqs)]
    tot_fx = sum(products)
    tot_f = sum(freqs)
    mean_val = round(tot_fx / tot_f, 1)

    return {
        "title": "Calculating Mean from Frequency Table",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "40_calculating_mean_from_frequency_table",
        "difficulty": "hard",
        "question_text": (
            "Refer to the frequency table below:\n\n"
            "| Score ($x$) | Frequency ($f$) |\n"
            "| :---: | :---: |\n"
            f"| 1 | {freqs[0]} |\n"
            f"| 2 | {freqs[1]} |\n"
            f"| 3 | {freqs[2]} |\n"
            f"| 4 | {freqs[3]} |\n\n"
            "Calculate the **mean** score."
        ),
        "correct_answer": _fmt_sa(mean_val, 1),
        "marking_schema": [
            f"Calculate sum(f*x) = {tot_fx} and sum(f) = {tot_f} [1M]",
            f"Mean = {tot_fx} / {tot_f} = {_fmt_sa(mean_val, 1)} [1A]",
        ],
        "hints": [
            "Multiply each score by its frequency: $\\sum(x \\cdot f)$.",
            f"$\\sum(x \\cdot f) = 1({freqs[0]}) + 2({freqs[1]}) + 3({freqs[2]}) + 4({freqs[3]}) = {tot_fx}$.",
            f"Divide by total frequency ${tot_f}$: $\\frac{{{tot_fx}}}{{{tot_f}}} = {_fmt_sa(mean_val, 1)}$.",
        ],
        "misconception_tags": ["frequency_table_mean_dividing_by_categories_count_error"],
        "diagram_spec": None,
    }


def arch_41_identifying_mode_from_frequency_table(rng: random.Random) -> Dict[str, Any]:
    scores = [5, 6, 7, 8, 9]
    freqs = [3, 8, 4, 2, 1]
    mode_score = 6

    return {
        "title": "Identifying Mode from Frequency Table",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "41_identifying_mode_from_frequency_table",
        "difficulty": "easy",
        "question_text": (
            "Consider the frequency table below:\n\n"
            "| Mark | Frequency |\n"
            "| :---: | :---: |\n"
            f"| 5 | {freqs[0]} |\n"
            f"| 6 | {freqs[1]} |\n"
            f"| 7 | {freqs[2]} |\n"
            f"| 8 | {freqs[3]} |\n"
            f"| 9 | {freqs[4]} |\n\n"
            "What is the **mode** mark?"
        ),
        "correct_answer": str(mode_score),
        "marking_schema": [
            f"Identify mark with highest frequency: {mode_score} (frequency 8) (1 mark)",
        ],
        "hints": [
            "The mode is the score that has the highest frequency.",
            f"The highest frequency is {max(freqs)}, which belongs to mark {mode_score}.",
            f"Mode = {mode_score}.",
        ],
        "misconception_tags": ["mode_value_vs_frequency_confusion"],
        "diagram_spec": None,
    }


def arch_42_identifying_median_from_cumulative_frequency(rng: random.Random) -> Dict[str, Any]:
    # 11 learners: 1 (2), 2 (4), 3 (3), 4 (2)
    # Total = 11, middle is 6th
    # 1, 1, 2, 2, 2, 2 (6th is 2)
    return {
        "title": "Finding Median Position in Frequency Table",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "42_identifying_median_from_cumulative_frequency",
        "difficulty": "hard",
        "question_text": (
            "A test out of 4 marks was taken by 11 learners:\n\n"
            "| Score | Frequency |\n"
            "| :---: | :---: |\n"
            "| 1 | 2 |\n"
            "| 2 | 4 |\n"
            "| 3 | 3 |\n"
            "| 4 | 2 |\n\n"
            "Determine the **median** score."
        ),
        "correct_answer": "2",
        "marking_schema": [
            "Find position (11+1)/2 = 6th learner => score 2: 2 marks",
        ],
        "hints": [
            "With 11 learners, the median is the 6th ordered value.",
            "Scores 1 to 2 belong to mark 1; scores 3 to 6 belong to mark 2.",
            "The 6th learner scored 2. Median = 2.",
        ],
        "misconception_tags": ["median_from_table_ranking_error"],
        "diagram_spec": None,
    }


def arch_43_two_way_contingency_table_reading_cell_frequency(rng: random.Random) -> Dict[str, Any]:
    boys_tea = rng.randint(8, 15)
    boys_coffee = rng.randint(6, 12)
    girls_tea = rng.randint(10, 18)
    girls_coffee = rng.randint(7, 14)

    return {
        "title": "Two-Way Table: Reading Cell Frequency",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "43_two_way_contingency_table_reading_cell_frequency",
        "difficulty": "easy",
        "question_text": (
            "Refer to the two-way contingency table below:\n\n"
            "| Gender | Tea | Coffee |\n"
            "| :--- | :---: | :---: |\n"
            f"| Boys | {boys_tea} | {boys_coffee} |\n"
            f"| Girls | {girls_tea} | {girls_coffee} |\n\n"
            "How many **girls** prefer **tea**?"
        ),
        "correct_answer": str(girls_tea),
        "marking_schema": [
            f"Read intersection of Girls row and Tea column: {girls_tea} (1 mark)",
        ],
        "hints": [
            "Find the row for 'Girls' and trace across to the column labeled 'Tea'.",
            f"The value in that cell is {girls_tea}.",
        ],
        "misconception_tags": ["two_way_table_row_column_confusion"],
        "diagram_spec": None,
    }


def arch_44_two_way_table_calculating_marginal_row_or_column_total(rng: random.Random) -> Dict[str, Any]:
    b_tea = rng.randint(10, 16)
    g_tea = rng.randint(12, 20)
    total_tea = b_tea + g_tea

    return {
        "title": "Two-Way Table: Column Marginal Total",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "44_two_way_table_calculating_marginal_row_or_column_total",
        "difficulty": "easy",
        "question_text": (
            "In a two-way table, **"
            f"{b_tea} boys** and **{g_tea} girls** choose tea.\n\n"
            "Calculate the total number of learners who choose tea."
        ),
        "correct_answer": str(total_tea),
        "marking_schema": [
            f"Add boys and girls: {b_tea} + {g_tea} = {total_tea} (1 mark)",
        ],
        "hints": [
            "Add the frequencies down the 'Tea' column.",
            f"${b_tea} + {g_tea} = {total_tea}$.",
            f"Total = {total_tea}.",
        ],
        "misconception_tags": ["marginal_total_addition_slip"],
        "diagram_spec": None,
    }


def arch_45_two_way_table_finding_missing_cell_value(rng: random.Random) -> Dict[str, Any]:
    tot_boys = 35
    b_tea = rng.randint(14, 22)
    b_coffee = tot_boys - b_tea

    return {
        "title": "Two-Way Table: Finding Missing Cell Entry",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "45_two_way_table_finding_missing_cell_value",
        "difficulty": "medium",
        "question_text": (
            f"Out of **{tot_boys} boys** surveyed, **{b_tea} boys** prefer tea and the rest prefer coffee.\n\n"
            "Calculate how many boys prefer coffee."
        ),
        "correct_answer": str(b_coffee),
        "marking_schema": [
            f"Subtract tea from total boys: {tot_boys} - {b_tea} = {b_coffee} (1 mark)",
        ],
        "hints": [
            f"Total boys = ${tot_boys}$.",
            f"Subtract those who prefer tea: ${tot_boys} - {b_tea} = {b_coffee}$.",
            f"Answer: {b_coffee}.",
        ],
        "misconception_tags": ["two_way_table_missing_cell_subtraction_error"],
        "diagram_spec": None,
    }


def arch_46_comparing_two_data_sets_by_means(rng: random.Random) -> Dict[str, Any]:
    mean_a = rng.randint(58, 68)
    diff = rng.randint(4, 9)
    mean_b = mean_a + diff

    return {
        "title": "Comparing Two Data Sets by Means",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "46_comparing_two_data_sets_by_means",
        "difficulty": "medium",
        "question_text": (
            f"Class 8A achieved a mean test score of **{mean_a}%**, while Class 8B achieved a mean test score of **{mean_b}%**.\n\n"
            "Which class performed better overall on average? Justify your answer."
        ),
        "correct_answer": f"Class 8B, because its mean of {mean_b}% is {diff}% higher than Class 8A's mean of {mean_a}%.",
        "marking_schema": [
            f"Identify Class 8B with comparison {mean_b}% > {mean_a}%: 1 mark",
        ],
        "hints": [
            "The mean represents the overall average performance of each group.",
            f"Compare: {mean_b}% > {mean_a}%.",
            "Class 8B performed better on average.",
        ],
        "misconception_tags": ["mean_comparison_inversion"],
        "diagram_spec": None,
    }


def arch_47_comparing_two_data_sets_by_range_consistency(rng: random.Random) -> Dict[str, Any]:
    rng_p = rng.randint(12, 18)
    rng_q = rng.randint(28, 42)

    return {
        "title": "Comparing Consistency Using the Range",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "47_comparing_two_data_sets_by_range_consistency",
        "difficulty": "medium",
        "question_text": (
            f"Athlete P's race times have a range of **{rng_p} seconds**, while Athlete Q's race times have a range of **{rng_q} seconds**.\n\n"
            "Which athlete had the more **consistent** race times? Explain why."
        ),
        "correct_answer": f"Athlete P, because a smaller range ({rng_p} s < {rng_q} s) indicates less variation in performance.",
        "marking_schema": [
            f"Identify Athlete P because smaller range indicates greater consistency: 1 mark",
        ],
        "hints": [
            "Range measures spread and variability.",
            "A smaller range means scores are closer together, indicating greater consistency.",
            f"Athlete P is more consistent because {rng_p} < {rng_q}.",
        ],
        "misconception_tags": ["consistency_range_inverse_misunderstanding"],
        "diagram_spec": None,
    }


def arch_48_data_collection_method_survey_vs_experiment(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Investigating whether fertilizer brand X or brand Y produces taller bean plants under controlled laboratory conditions", "experiment"),
        ("Gathering opinions from community members on proposed municipal traffic circle construction", "survey / questionnaire"),
        ("Recording the number of cars passing an intersection between 07:00 and 08:00 without interacting with drivers", "observation"),
    ]
    scenario, method = rng.choice(cases)

    return {
        "title": "Choosing Data Collection Method",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "48_data_collection_method_survey_vs_experiment",
        "difficulty": "easy",
        "question_text": (
            f"Identify the most appropriate data collection method (**experiment**, **survey**, or **observation**) for:\n\n"
            f"**\"{scenario}\"**"
        ),
        "correct_answer": method,
        "marking_schema": [
            f"Identify collection method: {method} (1 mark)",
        ],
        "hints": [
            "An experiment tests cause and effect under controlled conditions.",
            "A survey collects opinions, preferences, or self-reported information.",
            "Observation monitors behavior or events without interfering.",
            f"Method: {method}.",
        ],
        "misconception_tags": ["data_collection_method_confusion"],
        "diagram_spec": None,
    }


def arch_49_identifying_measurement_units_and_instruments(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Measuring the time taken by an athlete to sprint 100 meters", "stopwatch", "seconds"),
        ("Measuring the body temperature of a patient in a clinic", "thermometer", "degrees Celsius (°C)"),
        ("Measuring the mass of a schoolbag", "scale / balance", "kilograms (kg)"),
    ]
    scenario, tool, unit = rng.choice(cases)

    return {
        "title": "Measurement Instruments and Units",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "49_identifying_measurement_units_and_instruments",
        "difficulty": "easy",
        "question_text": (
            f"For the task: **\"{scenario}\"**:\n\n"
            f"1. Name the appropriate measuring instrument.\n"
            f"2. State the standard unit of measurement."
        ),
        "correct_answer": f"1. {tool}; 2. {unit}",
        "marking_schema": [
            f"Instrument: {tool} [1 mark], Unit: {unit} [1 mark]",
        ],
        "hints": [
            f"Tool used: {tool}.",
            f"Unit used: {unit}.",
            f"Answer: 1. {tool}; 2. {unit}.",
        ],
        "misconception_tags": ["measurement_tool_unit_mismatch"],
        "diagram_spec": None,
    }


def arch_50_full_data_cycle_summary_evaluation(rng: random.Random) -> Dict[str, Any]:
    # 5 numbers: e.g. 10, 12, 12, 14, 22
    m = rng.choice([12, 14, 16])
    d1 = m - 4
    d2 = m
    d3 = m
    d4 = m + 2
    d5 = m + 12
    vals = [d1, d2, d3, d4, d5]
    vals_str = ", ".join(str(v) for v in vals)

    mean_v = sum(vals) / 5.0
    median_v = m
    mode_v = m
    range_v = d5 - d1

    return {
        "title": "Comprehensive Summary: Mean, Median, Mode, Range",
        "topic": "Collect organise and summarise data",
        "grade": 8,
        "term": 1,
        "subskill": "50_full_data_cycle_summary_evaluation",
        "difficulty": "hard",
        "question_text": (
            f"For the ordered data set: **{vals_str}**:\n\n"
            "1. Calculate the **mean**.\n"
            "2. State the **median**.\n"
            "3. State the **mode**.\n"
            "4. Calculate the **range**."
        ),
        "correct_answer": f"1. Mean = {_fmt_sa(mean_v, 1)}; 2. Median = {median_v}; 3. Mode = {mode_v}; 4. Range = {range_v}",
        "marking_schema": [
            f"Mean = {sum(vals)}/5 = {_fmt_sa(mean_v, 1)} [1 mark]",
            f"Median = {median_v} [1 mark]",
            f"Mode = {mode_v} [1 mark]",
            f"Range = {d5} - {d1} = {range_v} [1 mark]",
        ],
        "hints": [
            f"Mean: $\\frac{{{sum(vals)}}}{{5}} = {_fmt_sa(mean_v, 1)}$.",
            f"Median: Middle (3rd) value = {median_v}.",
            f"Mode: Most frequent value = {mode_v}.",
            f"Range: ${d5} - {d1} = {range_v}$.",
        ],
        "misconception_tags": ["central_tendency_summary_confusion"],
        "diagram_spec": None,
    }


BUILDERS_26_50 = [
    arch_26_calculating_mean_of_ungrouped_data_set,
    arch_27_finding_median_of_ordered_data_odd_number,
    arch_28_finding_median_of_ordered_data_even_number,
    arch_29_finding_median_of_unordered_data_set,
    arch_30_identifying_mode_of_discrete_data_set,
    arch_31_identifying_bimodal_data_set,
    arch_32_identifying_no_mode_in_data_set,
    arch_33_calculating_range_of_raw_data_set,
    arch_34_calculating_mean_with_decimal_result,
    arch_35_effect_of_extreme_value_outlier_on_mean,
    arch_36_effect_of_outlier_on_median_resistance,
    arch_37_choosing_appropriate_measure_of_central_tendency,
    arch_38_finding_missing_value_given_the_mean,
    arch_39_finding_missing_value_given_the_range,
    arch_40_calculating_mean_from_frequency_table,
    arch_41_identifying_mode_from_frequency_table,
    arch_42_identifying_median_from_cumulative_frequency,
    arch_43_two_way_contingency_table_reading_cell_frequency,
    arch_44_two_way_table_calculating_marginal_row_or_column_total,
    arch_45_two_way_table_finding_missing_cell_value,
    arch_46_comparing_two_data_sets_by_means,
    arch_47_comparing_two_data_sets_by_range_consistency,
    arch_48_data_collection_method_survey_vs_experiment,
    arch_49_identifying_measurement_units_and_instruments,
    arch_50_full_data_cycle_summary_evaluation,
]
