"""
Grade 8 Mathematics - Interpret, Analyse and Report on Data Archetypes (01 to 25).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/01. Interpret analyse and report on data.md.
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


def arch_01_calculating_arithmetic_mean_integer_result(rng: random.Random) -> Dict[str, Any]:
    n = 5
    mean_val = rng.randint(45, 75)
    offsets = [rng.randint(-12, 12) for _ in range(n - 1)]
    rem = sum(offsets) % n
    last_offset = (n - rem) % n
    offsets.append(last_offset)
    scores = [mean_val + off for off in offsets]
    rng.shuffle(scores)
    tot = sum(scores)
    scores_str = ", ".join(str(s) for s in scores)

    return {
        "title": "Calculating Arithmetic Mean (Integer Result)",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "01_calculating_arithmetic_mean_integer_result",
        "difficulty": "easy",
        "question_text": (
            f"Five Grade 8 learners achieved the following test scores:\n\n"
            f"$${scores_str}$$\n\n"
            "Calculate the **mean (average)** score for this group."
        ),
        "correct_answer": str(mean_val),
        "marking_schema": [
            f"Sum scores ({tot}) and divide by 5: {tot}/5 = {mean_val} (2 marks)",
        ],
        "hints": [
            "Add all 5 scores together.",
            f"Sum = ${' + '.join(str(s) for s in scores)} = {tot}$.",
            f"Mean = $\\frac{{{tot}}}{{5}} = {mean_val}$.",
        ],
        "misconception_tags": ["mean_arithmetic_sum_slip"],
        "diagram_spec": None,
    }


def arch_02_calculating_arithmetic_mean_decimal_rounded(rng: random.Random) -> Dict[str, Any]:
    scores = [rng.randint(50, 85) for _ in range(5)]
    tot = sum(scores)
    mean_val = round(tot / 5.0, 1)
    mean_str = _fmt_sa(mean_val, 1)
    scores_str = ", ".join(str(s) for s in scores)

    return {
        "title": "Calculating Mean with Decimal Result",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "02_calculating_arithmetic_mean_decimal_rounded",
        "difficulty": "medium",
        "question_text": (
            f"Consider the five scores: **{scores_str}**.\n\n"
            "Calculate the **mean**, rounding off your answer to **one decimal place**."
        ),
        "correct_answer": mean_str,
        "marking_schema": [
            f"Sum = {tot}, Mean = {tot}/5 = {mean_str} (2 marks)",
        ],
        "hints": [
            f"Sum = ${tot}$.",
            f"Divide by 5: $\\frac{{{tot}}}{{5}} = {mean_str}$.",
            f"Mean = {mean_str}.",
        ],
        "misconception_tags": ["mean_decimal_rounding_slip"],
        "diagram_spec": None,
    }


def arch_03_finding_median_odd_sample_size(rng: random.Random) -> Dict[str, Any]:
    vals = sorted(rng.sample(range(20, 90), 7))
    median_val = vals[3]
    raw_vals = list(vals)
    rng.shuffle(raw_vals)
    raw_str = ", ".join(str(v) for v in raw_vals)
    ord_str = ", ".join(str(v) for v in vals)

    return {
        "title": "Finding Median of Odd-Sized Data Set",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "03_finding_median_odd_sample_size",
        "difficulty": "medium",
        "question_text": (
            f"Determine the **median** of the following 7 test marks:\n\n"
            f"$${raw_str}$$"
        ),
        "correct_answer": str(median_val),
        "marking_schema": [
            f"Sort data ({ord_str}) and identify middle (4th) score: {median_val} (2 marks)",
        ],
        "hints": [
            f"First sort the marks in ascending order: {ord_str}.",
            "For 7 items, the median is the 4th value: position $\\frac{7+1}{2} = 4$.",
            f"Median = {median_val}.",
        ],
        "misconception_tags": ["median_without_sorting_error"],
        "diagram_spec": None,
    }


def arch_04_finding_median_even_sample_size(rng: random.Random) -> Dict[str, Any]:
    m1 = rng.choice([44, 48, 52, 56])
    m2 = m1 + rng.choice([2, 4])
    sorted_vals = [m1 - 10, m1 - 4, m1, m2, m2 + 6, m2 + 12]
    shuffled = list(sorted_vals)
    rng.shuffle(shuffled)
    median_val = (m1 + m2) / 2
    med_str = _fmt_sa(median_val, 1)
    raw_str = ", ".join(str(v) for v in shuffled)
    ord_str = ", ".join(str(v) for v in sorted_vals)

    return {
        "title": "Finding Median of Even-Sized Data Set",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "04_finding_median_even_sample_size",
        "difficulty": "medium",
        "question_text": (
            f"Find the **median** of the following 6 test scores:\n\n"
            f"$${raw_str}$$"
        ),
        "correct_answer": med_str,
        "marking_schema": [
            f"Order scores ({ord_str}) and average 3rd ({m1}) and 4th ({m2}) values: {med_str} (2 marks)",
        ],
        "hints": [
            f"Sort the values in ascending order: {ord_str}.",
            f"The two middle numbers are {m1} and {m2}.",
            f"Median = $\\frac{{{m1} + {m2}}}{{2}} = {med_str}$.",
        ],
        "misconception_tags": ["median_even_count_single_pick_error"],
        "diagram_spec": None,
    }


def arch_05_finding_median_after_sorting_unordered_list(rng: random.Random) -> Dict[str, Any]:
    vals = rng.sample(range(10, 50), 5)
    sorted_vals = sorted(vals)
    med = sorted_vals[2]
    raw_str = ", ".join(str(v) for v in vals)

    return {
        "title": "Sorting and Finding Median",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "05_finding_median_after_sorting_unordered_list",
        "difficulty": "easy",
        "question_text": (
            f"Arrange the numbers **{raw_str}** in order and state the **median**."
        ),
        "correct_answer": str(med),
        "marking_schema": [
            f"Ordered list: {', '.join(str(v) for v in sorted_vals)} => Median = {med} (2 marks)",
        ],
        "hints": [
            f"Ascending order: {', '.join(str(v) for v in sorted_vals)}.",
            f"The middle (3rd) value is {med}.",
        ],
        "misconception_tags": ["median_without_sorting_error"],
        "diagram_spec": None,
    }


def arch_06_identifying_mode_single_most_frequent_value(rng: random.Random) -> Dict[str, Any]:
    mode_val = rng.randint(15, 40)
    others = rng.sample([x for x in range(10, 50) if x != mode_val], 4)
    data = [mode_val, mode_val, mode_val] + others
    rng.shuffle(data)
    data_str = ", ".join(str(d) for d in data)

    return {
        "title": "Identifying Mode in Data Set",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "06_identifying_mode_single_most_frequent_value",
        "difficulty": "easy",
        "question_text": (
            f"Identify the **mode** of the following set of marks:\n\n"
            f"$${data_str}$$"
        ),
        "correct_answer": str(mode_val),
        "marking_schema": [
            f"Identify most frequent mark: {mode_val} (occurs 3 times) (1 mark)",
        ],
        "hints": [
            "The mode is the number that occurs most frequently.",
            f"{mode_val} appears three times.",
            f"Mode = {mode_val}.",
        ],
        "misconception_tags": ["mode_identification_frequency_error"],
        "diagram_spec": None,
    }


def arch_07_identifying_bimodal_distribution(rng: random.Random) -> Dict[str, Any]:
    m1, m2 = sorted(rng.sample(range(20, 50), 2))
    others = rng.sample([x for x in range(20, 60) if x not in (m1, m2)], 3)
    data = [m1, m1, m2, m2] + others
    rng.shuffle(data)
    data_str = ", ".join(str(d) for d in data)

    return {
        "title": "Identifying Bimodal Distribution",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "07_identifying_bimodal_distribution",
        "difficulty": "medium",
        "question_text": (
            f"State the **mode(s)** of the following data set:\n\n"
            f"$${data_str}$$"
        ),
        "correct_answer": f"{m1} and {m2}",
        "marking_schema": [
            f"Identify both modes {m1} and {m2} (bimodal): 1 mark",
        ],
        "hints": [
            f"Both {m1} and {m2} appear twice, which is more than any other number.",
            f"This distribution is bimodal with modes {m1} and {m2}.",
        ],
        "misconception_tags": ["bimodal_single_mode_assumption"],
        "diagram_spec": None,
    }


def arch_08_identifying_no_mode_equal_frequencies(rng: random.Random) -> Dict[str, Any]:
    vals = rng.sample(range(15, 60), 6)
    data_str = ", ".join(str(v) for v in vals)

    return {
        "title": "Recognizing When No Mode Exists",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "08_identifying_no_mode_equal_frequencies",
        "difficulty": "easy",
        "question_text": (
            f"Consider the data set: **{data_str}**.\n\n"
            "What is the **mode** of this data set?"
        ),
        "correct_answer": "No mode",
        "marking_schema": [
            "State 'No mode' because each score appears exactly once: 1 mark",
        ],
        "hints": [
            "A mode only exists if at least one number appears more often than others.",
            "Each value appears only once.",
            "Answer: No mode.",
        ],
        "misconception_tags": ["mode_zero_vs_no_mode_confusion"],
        "diagram_spec": None,
    }


def arch_09_calculating_range_of_sample(rng: random.Random) -> Dict[str, Any]:
    low = rng.randint(18, 30)
    diff = rng.randint(25, 45)
    high = low + diff
    in_betweens = rng.sample(range(low + 1, high), 4)
    vals = [low, high] + in_betweens
    rng.shuffle(vals)
    data_str = ", ".join(str(v) for v in vals)

    return {
        "title": "Calculating Range of a Sample",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "09_calculating_range_of_sample",
        "difficulty": "easy",
        "question_text": (
            f"Calculate the **range** of the following data values:\n\n"
            f"$${data_str}$$"
        ),
        "correct_answer": str(diff),
        "marking_schema": [
            f"Range = {high} - {low} = {diff} (1 mark)",
        ],
        "hints": [
            "Range = Highest value - Lowest value.",
            f"Highest = {high}; Lowest = {low}.",
            f"$\\text{{Range}} = {high} - {low} = {diff}$.",
        ],
        "misconception_tags": ["range_extreme_identification_slip"],
        "diagram_spec": None,
    }


def arch_10_identifying_extreme_outlier_value(rng: random.Random) -> Dict[str, Any]:
    cluster = [rng.randint(22, 28) for _ in range(5)]
    outlier = rng.choice([85, 92, 95])
    dataset = cluster + [outlier]
    rng.shuffle(dataset)
    data_str = ", ".join(str(d) for d in dataset)

    return {
        "title": "Identifying an Extreme Outlier",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "10_identifying_extreme_outlier_value",
        "difficulty": "easy",
        "question_text": (
            f"Consider the numbers: **{data_str}**.\n\n"
            "Identify the **extreme value (outlier)** in this data set."
        ),
        "correct_answer": str(outlier),
        "marking_schema": [
            f"Identify outlier: {outlier} (lies far above the cluster in the 20s) (1 mark)",
        ],
        "hints": [
            "An outlier is a data point that differs significantly from other observations in the sample.",
            f"Most values are in the 20s, whereas {outlier} is significantly higher.",
            f"Outlier = {outlier}.",
        ],
        "misconception_tags": ["outlier_recognition_failure"],
        "diagram_spec": None,
    }


def arch_11_effect_of_adding_outlier_on_mean(rng: random.Random) -> Dict[str, Any]:
    vals = [20, 22, 24, 26, 28]  # mean = 24
    outlier = 90
    new_mean = round((sum(vals) + outlier) / 6.0, 1)

    return {
        "title": "Quantifying Effect of Outlier on Mean",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "11_effect_of_adding_outlier_on_mean",
        "difficulty": "medium",
        "question_text": (
            "A group of five scores: **20, 22, 24, 26, 28** has a mean of **24**.\n\n"
            f"If an extreme score of **{outlier}** is added, calculate the **new mean** (to one decimal place)."
        ),
        "correct_answer": _fmt_sa(new_mean, 1),
        "marking_schema": [
            f"Sum = 120 + {outlier} = {120 + outlier}, New mean = {120 + outlier}/6 = {_fmt_sa(new_mean, 1)} (2 marks)",
        ],
        "hints": [
            f"New sum = $120 + {outlier} = {120 + outlier}$.",
            f"Divide by 6: $\\frac{{{120 + outlier}}}{{6}} = {_fmt_sa(new_mean, 1)}$.",
            f"New mean = {_fmt_sa(new_mean, 1)}.",
        ],
        "misconception_tags": ["outlier_mean_recalculation_slip"],
        "diagram_spec": None,
    }


def arch_12_effect_of_adding_outlier_on_median(rng: random.Random) -> Dict[str, Any]:
    # 20, 22, 24, 26, 28 (median 24)
    # Add 90 -> 20, 22, 24, 26, 28, 90 (median is (24+26)/2 = 25)
    return {
        "title": "Minimal Effect of Outlier on Median",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "12_effect_of_adding_outlier_on_median",
        "difficulty": "medium",
        "question_text": (
            "The data set **20, 22, 24, 26, 28** has a median of **24**.\n\n"
            "If an extreme outlier of **90** is added, calculate the **new median**."
        ),
        "correct_answer": "25",
        "marking_schema": [
            "Order with outlier: 20, 22, 24, 26, 28, 90 => Median = (24 + 26)/2 = 25 (2 marks)",
        ],
        "hints": [
            "New ordered set: 20, 22, 24, 26, 28, 90.",
            "The two middle numbers are now 24 and 26.",
            "New median = $\\frac{24 + 26}{2} = 25$.",
        ],
        "misconception_tags": ["median_outlier_overreaction_misconception"],
        "diagram_spec": None,
    }


def arch_13_effect_of_adding_outlier_on_range(rng: random.Random) -> Dict[str, Any]:
    old_min, old_max = 20, 30
    outlier = 95
    old_range = old_max - old_min
    new_range = outlier - old_min

    return {
        "title": "Effect of Outlier on Range",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "13_effect_of_adding_outlier_on_range",
        "difficulty": "easy",
        "question_text": (
            f"A data set has a minimum of **{old_min}** and a maximum of **{old_max}** (range = **{old_range}**).\n\n"
            f"If an extreme outlier of **{outlier}** is added, what is the **new range**?"
        ),
        "correct_answer": str(new_range),
        "marking_schema": [
            f"New range = {outlier} - {old_min} = {new_range} (1 mark)",
        ],
        "hints": [
            f"The new maximum is {outlier}, while the minimum remains {old_min}.",
            f"$\\text{{New range}} = {outlier} - {old_min} = {new_range}$.",
        ],
        "misconception_tags": ["range_outlier_expansion_slip"],
        "diagram_spec": None,
    }


def arch_14_choosing_mean_vs_median_for_skewed_salary_data(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Choosing Median for Skewed Income Data",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "14_choosing_mean_vs_median_for_skewed_salary_data",
        "difficulty": "medium",
        "question_text": (
            "In a small company of 10 workers, 9 employees earn R15 000 per month while the CEO earns R500 000.\n\n"
            "Which measure of central tendency (**mean** or **median**) gives a fairer picture of a typical employee's salary? Explain why."
        ),
        "correct_answer": "Median, because the mean is heavily distorted upward by the CEO's extreme salary, whereas the median reflects the typical salary of R15 000.",
        "marking_schema": [
            "Select median with explanation that outlier distorts the mean: 2 marks",
        ],
        "hints": [
            "Calculate or estimate the mean: $\\frac{9(15\\,000) + 500\\,000}{10} = \\text{R}63\\,500$.",
            "Almost everyone earns only R15 000, so R63 500 is completely misleading.",
            "The median is R15 000 and is not distorted by the CEO's salary.",
        ],
        "misconception_tags": ["mean_vs_median_skewness_misconception"],
        "diagram_spec": None,
    }


def arch_15_choosing_mode_for_commercial_inventory(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Why Retailers Use the Mode",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "15_choosing_mode_for_commercial_inventory",
        "difficulty": "easy",
        "question_text": (
            "Explain why a shoe store manager orders stock based on the **mode** of shoe sizes sold, rather than the mean."
        ),
        "correct_answer": "Because shoe sizes are discrete categories, and the store needs to stock the exact size that is most frequently purchased (the mode).",
        "marking_schema": [
            "Explain that mode indicates the most popular/demanded shoe size to stock: 1 mark",
        ],
        "hints": [
            "The mean shoe size might be a decimal like 7,34 which does not exist as a real manufactured shoe.",
            "The mode identifies the single most popular size requested by customers.",
            "Answer: The mode shows the most frequently demanded item.",
        ],
        "misconception_tags": ["mode_commercial_application_concept_gap"],
        "diagram_spec": None,
    }


def arch_16_finding_missing_value_given_mean_and_n_minus_one_values(rng: random.Random) -> Dict[str, Any]:
    target_mean = rng.randint(40, 60)
    known = [target_mean - 6, target_mean + 4, target_mean - 2, target_mean + 8]
    total_needed = target_mean * 5
    missing = total_needed - sum(known)
    known_str = ", ".join(str(k) for k in known)

    return {
        "title": "Finding Missing Value from Target Mean",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "16_finding_missing_value_given_mean_and_n_minus_one_values",
        "difficulty": "hard",
        "question_text": (
            f"A learner wrote 5 tests and achieved an overall mean of **{target_mean}%**.\n\n"
            f"The marks for the first four tests were: **{known_str}**.\n\n"
            "What mark did the learner achieve on the **fifth test**?"
        ),
        "correct_answer": f"{missing}%",
        "marking_schema": [
            f"Required total = 5 * {target_mean} = {total_needed} [1M]",
            f"Fifth score = {total_needed} - {sum(known)} = {missing}% [1A]",
        ],
        "hints": [
            f"Total sum required = $5 \\times {target_mean} = {total_needed}$.",
            f"Sum of first 4 tests = ${sum(known)}$.",
            f"Fifth mark = ${total_needed} - {sum(known)} = {missing}\\%$.",
        ],
        "misconception_tags": ["missing_mean_value_algebraic_reversal_slip"],
        "diagram_spec": None,
    }


def arch_17_finding_missing_value_given_range_and_extremes(rng: random.Random) -> Dict[str, Any]:
    high = rng.randint(65, 95)
    rng_val = rng.randint(30, 45)
    low = high - rng_val

    return {
        "title": "Finding Lowest Mark Given the Range",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "17_finding_missing_value_given_range_and_extremes",
        "difficulty": "easy",
        "question_text": (
            f"In a science test, the highest score was **{high}%** and the range was **{rng_val}%**.\n\n"
            "Calculate the lowest score achieved in the test."
        ),
        "correct_answer": f"{low}%",
        "marking_schema": [
            f"Lowest = highest - range = {high} - {rng_val} = {low}% (1 mark)",
        ],
        "hints": [
            "Formula: $\\text{Lowest} = \\text{Highest} - \\text{Range}$.",
            f"$\\text{{Lowest}} = {high} - {rng_val} = {low}\\%$.",
        ],
        "misconception_tags": ["range_formula_reversal_subtraction_error"],
        "diagram_spec": None,
    }


def arch_18_calculating_percentage_of_population_in_provincial_sample(rng: random.Random) -> Dict[str, Any]:
    tot_samp = 2500
    prov_count = rng.choice([250, 375, 500, 625])
    pct = (prov_count / tot_samp) * 100
    pct_str = _fmt_sa(pct, 1)

    return {
        "title": "Provincial Sample Percentage Calculation",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "18_calculating_percentage_of_population_in_provincial_sample",
        "difficulty": "medium",
        "question_text": (
            f"In a national survey of **{tot_samp:,} schools**, exactly **{prov_count} schools** were from Gauteng.\n\n"
            "What percentage of the sample schools were from Gauteng?"
        ),
        "correct_answer": f"{pct_str}%",
        "marking_schema": [
            f"Percentage = ({prov_count} / {tot_samp}) * 100% = {pct_str}% (1 mark)",
        ],
        "hints": [
            f"Divide Gauteng count by total sample: $\\frac{{{prov_count}}}{{{tot_samp}}}$.",
            f"Multiply by 100%: $\\frac{{{prov_count}}}{{{tot_samp}}} \\times 100\\% = {pct_str}\\%$.",
        ],
        "misconception_tags": ["sample_percentage_scaling_error"],
        "diagram_spec": None,
    }


def arch_19_ranking_categories_from_tabular_summary(rng: random.Random) -> Dict[str, Any]:
    provinces = ["KZN", "EC", "GP", "WC"]
    counts = [400, 350, 300, 250]
    ans = "KZN, EC, GP, WC"

    return {
        "title": "Ranking Categories from Tabular Summary",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "19_ranking_categories_from_tabular_summary",
        "difficulty": "easy",
        "question_text": (
            "A survey report lists school counts by province:\n"
            "- EC: 350 schools\n"
            "- GP: 300 schools\n"
            "- KZN: 400 schools\n"
            "- WC: 250 schools\n\n"
            "Rank the four provinces in order from **most schools to fewest schools**."
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"List in descending order: {ans} (1 mark)",
        ],
        "hints": [
            "Compare counts: 400 > 350 > 300 > 250.",
            "Ranking: KZN (400), EC (350), GP (300), WC (250).",
        ],
        "misconception_tags": ["category_ranking_order_slip"],
        "diagram_spec": None,
    }


def arch_20_calculating_actual_quantity_from_total_and_percentage(rng: random.Random) -> Dict[str, Any]:
    pop = rng.choice([100000, 150000, 200000])
    pct = rng.choice([48.0, 51.0, 52.0])
    calc_val = int((pct / 100.0) * pop)

    return {
        "title": "Calculating Actual Quantity from Percentage",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "20_calculating_actual_quantity_from_total_and_percentage",
        "difficulty": "medium",
        "question_text": (
            f"If **{pop:,} Grade 8 learners** took part in a national survey and **{_fmt_sa(pct, 1)}%** were girls, "
            "calculate the total number of girls who participated."
        ),
        "correct_answer": f"{calc_val:,}",
        "marking_schema": [
            f"Calculate {pct}% of {pop}: {pop} * ({pct}/100) = {calc_val:,} (1 mark)",
        ],
        "hints": [
            f"Multiply total by percentage fraction: ${pop} \\times \\frac{{{pct}}}{{100}}$.",
            f"Total girls = {calc_val:,}.",
        ],
        "misconception_tags": ["percentage_multiplication_decimal_comma_error"],
        "diagram_spec": None,
    }


def arch_21_comparing_two_classes_by_mean_score(rng: random.Random) -> Dict[str, Any]:
    m1 = rng.randint(62, 70)
    diff = rng.randint(4, 8)
    m2 = m1 + diff

    return {
        "title": "Comparing Two Classes by Mean Score",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "21_comparing_two_classes_by_mean_score",
        "difficulty": "easy",
        "question_text": (
            f"Class 8A achieved a mean mark of **{m1}%** and Class 8B achieved a mean mark of **{m2}%**.\n\n"
            "Which class performed better overall on average, and by how many percentage points?"
        ),
        "correct_answer": f"Class 8B, by {diff} percentage points",
        "marking_schema": [
            f"Identify Class 8B and difference {diff} percentage points: 1 mark",
        ],
        "hints": [
            f"Compare means: {m2}% > {m1}%.",
            f"Difference = ${m2} - {m1} = {diff}$ percentage points.",
        ],
        "misconception_tags": ["mean_comparison_inversion"],
        "diagram_spec": None,
    }


def arch_22_comparing_two_athletes_by_range_consistency(rng: random.Random) -> Dict[str, Any]:
    r_sipho = rng.randint(4, 7)
    r_lunga = rng.randint(12, 18)

    return {
        "title": "Evaluating Performance Consistency Using Range",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "22_comparing_two_athletes_by_range_consistency",
        "difficulty": "medium",
        "question_text": (
            f"Sipho's high jump heights have a range of **{r_sipho} cm**, while Lunga's jumps have a range of **{r_lunga} cm**.\n\n"
            "Which athlete is more **consistent** in his jumping performance? Explain."
        ),
        "correct_answer": f"Sipho, because his smaller range ({r_sipho} cm < {r_lunga} cm) indicates less variation in results.",
        "marking_schema": [
            f"Identify Sipho because smaller range indicates greater consistency: 1 mark",
        ],
        "hints": [
            "A smaller range means that measurements are clustered closely together.",
            f"Sipho's range ({r_sipho} cm) is much smaller than Lunga's ({r_lunga} cm).",
            "Sipho is more consistent.",
        ],
        "misconception_tags": ["consistency_range_inverse_misunderstanding"],
        "diagram_spec": None,
    }


def arch_23_identifying_convenience_sampling_bias(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Identifying Convenience Sampling Bias",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "23_identifying_convenience_sampling_bias",
        "difficulty": "medium",
        "question_text": (
            "A learner surveys only his four closest friends at lunch to find the most popular music genre among all 1 000 learners at school.\n\n"
            "Explain why this convenience sampling method produces **biased** results."
        ),
        "correct_answer": "Friends typically share similar tastes and backgrounds, meaning the sample is not representative of the wider, diverse school population.",
        "marking_schema": [
            "Explain that friends share similar tastes and do not represent the whole school: 1 mark",
        ],
        "hints": [
            "Convenience sampling surveys whoever is easiest to reach.",
            "Friends often share similar interests, omitting the opinions of other age groups and cultures.",
            "The sample is biased.",
        ],
        "misconception_tags": ["convenience_sample_bias_unawareness"],
        "diagram_spec": None,
    }


def arch_24_identifying_voluntary_response_bias(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Identifying Voluntary Response Bias",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "24_identifying_voluntary_response_bias",
        "difficulty": "medium",
        "question_text": (
            "A radio station asks listeners to phone in and vote 'Yes' or 'No' on a controversial new law.\n\n"
            "Explain why voluntary phone-in polls suffer from **voluntary response bias**."
        ),
        "correct_answer": "People with strong or extreme negative opinions are much more likely to make the effort to call in, overrepresenting extreme views.",
        "marking_schema": [
            "Explain that phone-in polls attract respondents with strong/extreme views: 1 mark",
        ],
        "hints": [
            "Call-in polls rely on self-selection.",
            "Listeners with neutral or moderate opinions rarely bother to phone in.",
            "The poll results overrepresent passionate or extreme opinions.",
        ],
        "misconception_tags": ["voluntary_response_bias_concept_gap"],
        "diagram_spec": None,
    }


def arch_25_critiquing_advertiser_sample_claim(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Critiquing Misleading Commercial Claims",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "25_critiquing_advertiser_sample_claim",
        "difficulty": "hard",
        "question_text": (
            "An advertisement claims that **'4 out of 5 dentists recommend Brand X toothpaste'**.\n\n"
            "State **two critical questions** you should ask about the survey to determine if this claim is trustworthy."
        ),
        "correct_answer": "1. How many total dentists were surveyed (sample size)? 2. How were the dentists selected (randomly or paid/sponsored)?",
        "marking_schema": [
            "Ask about sample size [1 mark] and sampling method/independence [1 mark]",
        ],
        "hints": [
            "If only 5 dentists were asked in total, the sample is far too small.",
            "If the dentists were paid by the company, their answers may be biased.",
            "Question sample size and independence.",
        ],
        "misconception_tags": ["commercial_claim_critical_thinking_gap"],
        "diagram_spec": None,
    }


BUILDERS_01_25 = [
    arch_01_calculating_arithmetic_mean_integer_result,
    arch_02_calculating_arithmetic_mean_decimal_rounded,
    arch_03_finding_median_odd_sample_size,
    arch_04_finding_median_even_sample_size,
    arch_05_finding_median_after_sorting_unordered_list,
    arch_06_identifying_mode_single_most_frequent_value,
    arch_07_identifying_bimodal_distribution,
    arch_08_identifying_no_mode_equal_frequencies,
    arch_09_calculating_range_of_sample,
    arch_10_identifying_extreme_outlier_value,
    arch_11_effect_of_adding_outlier_on_mean,
    arch_12_effect_of_adding_outlier_on_median,
    arch_13_effect_of_adding_outlier_on_range,
    arch_14_choosing_mean_vs_median_for_skewed_salary_data,
    arch_15_choosing_mode_for_commercial_inventory,
    arch_16_finding_missing_value_given_mean_and_n_minus_one_values,
    arch_17_finding_missing_value_given_range_and_extremes,
    arch_18_calculating_percentage_of_population_in_provincial_sample,
    arch_19_ranking_categories_from_tabular_summary,
    arch_20_calculating_actual_quantity_from_total_and_percentage,
    arch_21_comparing_two_classes_by_mean_score,
    arch_22_comparing_two_athletes_by_range_consistency,
    arch_23_identifying_convenience_sampling_bias,
    arch_24_identifying_voluntary_response_bias,
    arch_25_critiquing_advertiser_sample_claim,
]
