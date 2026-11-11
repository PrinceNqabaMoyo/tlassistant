"""Grade 9 Mathematics - Collect, Organise & Summarise Data Archetypes 01 to 25
=============================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 4 Topic: Collect, organise and summarise data
  - curriculum_docs_auto/Mathematics_Gr9/Term 4/ Data Handling
  - Data collection methods, sampling, bias, tally charts, ungrouped frequency tables,
    measures of central tendency (mean, median, mode), measures of dispersion (range,
    outliers, quartiles Q1/Q3, IQR, semi-IQR).

Covers Archetypes 01 - 25:
  01: Population vs sample identification
  02: Data collection methods (questionnaire, survey, observation, experiment)
  03: Random sampling vs stratified sampling
  04: Identifying bias in survey questions
  05: Tally chart reading and frequency counts
  06: Completing ungrouped frequency distribution table
  07: Mean of ungrouped data (integer result)
  08: Mean of ungrouped data (decimal result)
  09: Median of ungrouped data (odd number of items)
  10: Median of ungrouped data (even number of items)
  11: Mode of ungrouped data (unimodal)
  12: Mode of ungrouped data (bimodal or no mode)
  13: Range of ungrouped data (maximum minus minimum)
  14: Find missing data value given mean
  15: Find missing frequency in distribution given total
  16: Identifying outliers in raw dataset
  17: Effect of outlier on mean vs median
  18: Choosing appropriate measure of central tendency (skewed vs symmetric)
  19: Mean from ungrouped frequency table (sum(f*x) / sum(f))
  20: Median from ungrouped frequency table using cumulative frequency
  21: Mode from ungrouped frequency table (score with highest frequency)
  22: Lower quartile (Q1) calculation
  23: Upper quartile (Q3) calculation
  24: Interquartile range (IQR = Q3 - Q1)
  25: Semi-interquartile range ((Q3 - Q1) / 2)
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.data_summarise_svg import (
    draw_tally_chart_svg,
    draw_frequency_table_svg,
    draw_dot_plot_svg,
)


def arch_01_population_vs_sample_identification(rng: random.Random) -> Dict[str, Any]:
    """Distinguish between a population and a sample in a research context."""
    scenarios = [
        (
            "A high school principal surveys 50 Grade 9 learners to determine student satisfaction with the school tuckshop.",
            "All learners in Grade 9 at the school",
            "The 50 Grade 9 learners who completed the survey",
        ),
        (
            "A cellular network provider tests network speeds on 500 mobile phones across Gauteng to estimate regional coverage.",
            "All mobile phones connected to the network in Gauteng",
            "The 500 mobile phones tested",
        ),
        (
            "A quality controller inspects 30 light bulbs from a factory production batch of 1 000 bulbs.",
            "The entire batch of 1 000 light bulbs",
            "The 30 light bulbs inspected",
        ),
    ]
    scen, pop, samp = rng.choice(scenarios)

    prompt = (
        f"Consider the following research scenario:\n"
        f"\"{scen}\"\n\n"
        f"Identify the **sample** in this study.\n"
        f"State: **{samp}**"
    )

    return {
        "subskill": "01_population_vs_sample_identification",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": samp,
        "sample_answer": samp,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recall definition: a sample is a smaller subset selected from the larger population to represent it", "marks": 1},
            {"step": f"Identify sample: {samp}", "marks": 1},
        ],
        "hints": [
            "The population is the complete group of individuals or objects being studied.",
            "The sample is the specific smaller group from which data is actually gathered.",
            f"Answer: **{samp}**.",
        ],
        "misconception_tags": ["population_vs_sample_confusion"],
    }


def arch_02_data_collection_methods_survey_vs_observation_vs_experiment(rng: random.Random) -> Dict[str, Any]:
    """Classify the most appropriate data collection method."""
    scenarios = [
        (
            "Counting how many minibus taxis pass through a busy traffic intersection between 07:00 and 08:00.",
            "observation",
            "the researcher watches and records events as they occur naturally without asking questions",
        ),
        (
            "Finding out which brand of breakfast cereal Grade 9 teenagers prefer by giving them written questionnaires.",
            "survey",
            "participants are asked questions directly using a questionnaire or interview",
        ),
        (
            "Testing whether a new fertilizer increases maize crop height by comparing treated and untreated plants under controlled conditions.",
            "experiment",
            "variables are controlled and tested under experimental conditions to measure the effect",
        ),
    ]
    scen, method, reason = rng.choice(scenarios)

    prompt = (
        f"Which data collection method (**survey**, **observation**, or **experiment**) is most appropriate for:\n"
        f"\"{scen}\"?"
    )

    return {
        "subskill": "02_data_collection_methods_survey_vs_observation_vs_experiment",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": method,
        "sample_answer": method,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify data collection method: {method}", "marks": 1},
            {"step": f"Justify: {reason}", "marks": 1},
        ],
        "hints": [
            "Surveys use questionnaires/interviews. Observation involves watching without intervening. Experiments test variables.",
            f"In this scenario, {reason}.",
            f"Answer: **{method}**.",
        ],
        "misconception_tags": ["data_collection_method_misclassification"],
    }


def arch_03_random_sampling_vs_stratified_sampling(rng: random.Random) -> Dict[str, Any]:
    """Distinguish between simple random sampling and stratified sampling."""
    is_stratified = rng.choice([True, False])
    if is_stratified:
        scen = "A researcher selects 10 boys and 10 girls proportionally from each grade (Grades 8 to 12) so every subgroup is represented."
        ans = "stratified sampling"
        reason = "the population is divided into distinct subgroups (strata) and samples are drawn proportionally from each group"
    else:
        scen = "A researcher places the names of all 600 learners into a drum, shakes it thoroughly, and draws 50 names at random."
        ans = "simple random sampling"
        reason = "every single member of the population has an equal chance of being selected"

    prompt = (
        f"A school conducts an investigation:\n"
        f"\"{scen}\"\n\n"
        f"What sampling method was used? (State: **simple random sampling** or **stratified sampling**)."
    )

    return {
        "subskill": "03_random_sampling_vs_stratified_sampling",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans,
        "sample_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify sampling technique: {ans}", "marks": 1},
            {"step": f"Justify: {reason}", "marks": 1},
        ],
        "hints": [
            "Simple random sampling gives every individual an equal chance (e.g. names from a hat).",
            "Stratified sampling divides the population into proportional groups (e.g. by grade or gender).",
            f"Answer: **{ans}**.",
        ],
        "misconception_tags": ["sampling_technique_confusion"],
    }


def arch_04_identifying_bias_in_survey_questions(rng: random.Random) -> Dict[str, Any]:
    """Identify why a survey question is biased / leading."""
    prompt = (
        f"Consider the following question from a school questionnaire:\n"
        f"\"*Don't you agree that homework is boring and should be completely abolished?*\"\n\n"
        f"Why is this survey question biased?\n"
        f"State: **it is a leading question that suggests the desired answer**"
    )

    return {
        "subskill": "04_identifying_bias_in_survey_questions",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "it is a leading question that suggests the desired answer",
        "sample_answer": "it is a leading question that suggests the desired answer",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that a leading question influences the respondent towards a specific opinion rather than remaining neutral", "marks": 1},
        ],
        "hints": [
            "Unbiased survey questions must remain neutral and not encourage one specific answer.",
            "Phrasing like 'Don't you agree...' leads respondents to agree.",
            "Answer: **it is a leading question that suggests the desired answer**.",
        ],
        "misconception_tags": ["questionnaire_bias_concept", "leading_question_error"],
    }


def arch_05_tally_chart_reading_and_frequency_counts(rng: random.Random) -> Dict[str, Any]:
    """Read frequency count from an SVG tally chart."""
    sports = [("Soccer", rng.randint(8, 14)), ("Netball", rng.randint(6, 12)), ("Rugby", rng.randint(5, 11)), ("Cricket", rng.randint(4, 9))]
    target_sport, target_freq = rng.choice(sports)
    seed_val = rng.randint(1000, 999999)
    svg = draw_tally_chart_svg(sports, title="Favorite Sports Survey", col1_label="Sport", seed=seed_val)

    prompt = (
        f"Refer to the tally chart below summarizing the favorite sports of Grade 9 learners:\n\n"
        f"How many learners chose **{target_sport}** as their favorite sport?"
    )

    return {
        "subskill": "05_tally_chart_reading_and_frequency_counts",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_freq),
        "sample_answer": str(target_freq),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Locate row for {target_sport} and count tally bundles: {target_freq}", "marks": 1},
        ],
        "hints": [
            "Each complete bundle with a diagonal slash represents $5$ tally marks.",
            f"Count the tallies in the **{target_sport}** row.",
            f"Frequency $= {target_freq}$.",
        ],
        "misconception_tags": ["tally_bundle_counting_error"],
    }


def arch_06_completing_ungrouped_frequency_distribution_table(rng: random.Random) -> Dict[str, Any]:
    """Count how many times a target number appears in a raw data list."""
    target_num = rng.choice([2, 3, 4, 5])
    other_nums = [n for n in [1, 2, 3, 4, 5, 6] if n != target_num]
    
    # Generate list of 16-20 numbers where target_num appears target_count times
    target_count = rng.randint(4, 7)
    data = [target_num] * target_count
    for _ in range(16 - target_count):
        data.append(rng.choice(other_nums))
    rng.shuffle(data)
    data_str = ", ".join(str(x) for x in data)

    prompt = (
        f"The following raw dataset represents the number of books read by a group of learners:\n"
        f"**{data_str}**\n\n"
        f"Determine the **frequency** of the score **{target_num}** (the number of times it appears in the data)."
    )

    return {
        "subskill": "06_completing_ungrouped_frequency_distribution_table",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(target_count),
        "sample_answer": str(target_count),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Tally occurrences of score {target_num}: count = {target_count}", "marks": 1},
        ],
        "hints": [
            f"Carefully count every occurrence of the number {target_num} in the list.",
            f"The number {target_num} appears {target_count} times.",
            f"Frequency $= {target_count}$.",
        ],
        "misconception_tags": ["frequency_counting_omission_error"],
    }


def arch_07_mean_of_ungrouped_data_integer_result(rng: random.Random) -> Dict[str, Any]:
    """Calculate mean of ungrouped numbers where result is an exact integer."""
    mean_val = rng.randint(12, 25)
    n = 5
    # Generate 5 numbers summing to 5 * mean_val
    diffs = [rng.randint(-5, -1), rng.randint(-3, -1), 0, rng.randint(1, 4)]
    diffs.append(-sum(diffs))
    values = [mean_val + d for d in diffs]
    rng.shuffle(values)
    val_str = ", ".join(str(v) for v in values)
    total_sum = sum(values)

    prompt = (
        f"The test marks of 5 learners are:\n"
        f"**{val_str}**\n\n"
        f"Calculate the **mean** (average) test mark."
    )

    return {
        "subskill": "07_mean_of_ungrouped_data_integer_result",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(mean_val),
        "sample_answer": str(mean_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Sum all values: {total_sum}", "marks": 1},
            {"step": f"Divide by count (n = 5): {total_sum} / 5 = {mean_val}", "marks": 1},
        ],
        "hints": [
            "Formula for mean: $\\bar{x} = \\frac{\\sum x}{n}$.",
            f"Add all 5 numbers: ${total_sum}$.",
            f"Divide by $5$: $\\frac{{{total_sum}}}{{5}} = {mean_val}$.",
        ],
        "misconception_tags": ["mean_arithmetic_sum_error", "mean_divided_by_wrong_count"],
    }


def arch_08_mean_of_ungrouped_data_decimal_result(rng: random.Random) -> Dict[str, Any]:
    """Calculate mean of ungrouped numbers with decimal result (rounded to 1 decimal place)."""
    # 6 values summing to S where S % 6 != 0
    base = rng.randint(10, 20)
    values = [base + rng.randint(1, 8) for _ in range(6)]
    while sum(values) % 6 == 0:
        values[0] += 1
    total = sum(values)
    mean_exact = round(total / 6.0, 1)
    val_str = ", ".join(str(v) for v in values)

    prompt = (
        f"The daily maximum temperatures recorded in Cape Town over 6 days were:\n"
        f"**{val_str}^\\circ\\text{{C}}**\n\n"
        f"Calculate the **mean temperature** in $^\\circ\\text{{C}}$, rounded to **one decimal place**."
    )

    return {
        "subskill": "08_mean_of_ungrouped_data_decimal_result",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": f"{mean_exact:.1f}",
        "sample_answer": f"{mean_exact:.1f}°C",
        "tolerance": 0.05,
        "marking_schema": [
            {"step": f"Sum temperatures: {total}", "marks": 1},
            {"step": f"Divide by 6: {total} / 6 = {total / 6:.2f} => {mean_exact:.1f}°C", "marks": 1},
        ],
        "hints": [
            "Sum all 6 temperatures and divide by 6.",
            f"Sum $= {total}$. Divide by $6$: ${total} \\div 6 \\approx {mean_exact:.1f}$.",
            f"Mean $= {mean_exact:.1f}^\\circ\\text{{C}}$.",
        ],
        "misconception_tags": ["decimal_rounding_error_in_mean"],
    }


def arch_09_median_of_ungrouped_data_odd_number_of_items(rng: random.Random) -> Dict[str, Any]:
    """Calculate median for odd number of items (middle element)."""
    n = 7
    values = sorted([rng.randint(10, 40) for _ in range(n)])
    median_val = values[3]
    # Shuffle for prompt
    shuffled = list(values)
    rng.shuffle(shuffled)
    val_str = ", ".join(str(v) for v in shuffled)
    sorted_str = ", ".join(str(v) for v in values)

    prompt = (
        f"Consider the following set of 7 numbers:\n"
        f"**{val_str}**\n\n"
        f"Calculate the **median** of the dataset."
    )

    return {
        "subskill": "09_median_of_ungrouped_data_odd_number_of_items",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(median_val),
        "sample_answer": str(median_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Order the numbers from smallest to largest: {sorted_str}", "marks": 1},
            {"step": f"Select middle (4th) element: {median_val}", "marks": 1},
        ],
        "hints": [
            "First arrange all 7 numbers in ascending order from smallest to largest.",
            f"Ordered list: {sorted_str}.",
            f"The middle number is the 4th value: **{median_val}**.",
        ],
        "misconception_tags": ["did_not_order_numbers_before_finding_median"],
    }


def arch_10_median_of_ungrouped_data_even_number_of_items(rng: random.Random) -> Dict[str, Any]:
    """Calculate median for even number of items (average of two middle elements)."""
    n = 6
    values = sorted([rng.randint(12, 35) for _ in range(n)])
    mid1, mid2 = values[2], values[3]
    median_val = (mid1 + mid2) / 2.0
    ans_str = f"{median_val:.1f}".rstrip("0").rstrip(".")

    shuffled = list(values)
    rng.shuffle(shuffled)
    val_str = ", ".join(str(v) for v in shuffled)
    sorted_str = ", ".join(str(v) for v in values)

    prompt = (
        f"Consider the following set of 6 test scores:\n"
        f"**{val_str}**\n\n"
        f"Calculate the **median** of the scores."
    )

    return {
        "subskill": "10_median_of_ungrouped_data_even_number_of_items",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Order scores in ascending order: {sorted_str}", "marks": 1},
            {"step": f"Average the 3rd and 4th scores: ({mid1} + {mid2}) / 2 = {ans_str}", "marks": 1},
        ],
        "hints": [
            "When the number of data values is even, the median is the average of the two middle values.",
            f"Ordered data: {sorted_str}. The two middle values are {mid1} and {mid2}.",
            f"Median $= \\frac{{{mid1} + {mid2}}}{{2}} = {ans_str}$.",
        ],
        "misconception_tags": ["even_n_median_average_error", "selected_only_one_middle_number"],
    }


def arch_11_mode_of_ungrouped_data_unimodal(rng: random.Random) -> Dict[str, Any]:
    """Find mode of unimodal dataset."""
    mode_val = rng.randint(5, 25)
    others = [n for n in range(5, 30) if n != mode_val]
    # Mode appears 3 times, others appear 1 time
    data = [mode_val] * 3 + rng.sample(others, 4)
    rng.shuffle(data)
    val_str = ", ".join(str(x) for x in data)

    prompt = (
        f"Find the **mode** of the following dataset:\n"
        f"**{val_str}**"
    )

    return {
        "subskill": "11_mode_of_ungrouped_data_unimodal",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(mode_val),
        "sample_answer": str(mode_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State definition: the mode is the value that occurs most frequently in the dataset", "marks": 1},
            {"step": f"Identify mode: {mode_val} (occurs 3 times)", "marks": 1},
        ],
        "hints": [
            "The mode is the number that appears most often.",
            f"Count how many times each number appears in the list.",
            f"The mode is **{mode_val}**.",
        ],
        "misconception_tags": ["mode_definition_error", "confused_mode_with_median"],
    }


def arch_12_mode_of_ungrouped_data_bimodal_or_no_mode(rng: random.Random) -> Dict[str, Any]:
    """Identify bimodal dataset or no mode."""
    is_bimodal = rng.choice([True, False])
    if is_bimodal:
        m1, m2 = sorted(rng.sample(range(10, 30), 2))
        others = [n for n in range(10, 35) if n not in (m1, m2)]
        data = [m1, m1, m2, m2] + rng.sample(others, 3)
        rng.shuffle(data)
        ans = f"{m1} and {m2}"
        desc = f"Both {m1} and {m2} appear twice (bimodal)"
    else:
        # All distinct => no mode
        data = sorted(rng.sample(range(10, 40), 7))
        rng.shuffle(data)
        ans = "no mode"
        desc = "Every value appears exactly once, so there is no mode"

    val_str = ", ".join(str(x) for x in data)

    prompt = (
        f"Determine the **mode** of the following dataset (if bimodal, state both values; if none, state **no mode**):\n"
        f"**{val_str}**"
    )

    return {
        "subskill": "12_mode_of_ungrouped_data_bimodal_or_no_mode",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": ans,
        "sample_answer": ans,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Analyse frequency of values: {desc}", "marks": 1},
            {"step": f"State answer: {ans}", "marks": 1},
        ],
        "hints": [
            "If two numbers tie for the highest frequency, the dataset is bimodal.",
            "If every number appears with the same frequency, there is no mode.",
            f"Answer: **{ans}**.",
        ],
        "misconception_tags": ["bimodal_identification_error", "stated_zero_instead_of_no_mode"],
    }


def arch_13_range_of_ungrouped_data_maximum_minus_minimum(rng: random.Random) -> Dict[str, Any]:
    """Calculate range = maximum - minimum."""
    min_val = rng.randint(8, 18)
    max_val = min_val + rng.randint(15, 35)
    r_val = max_val - min_val
    middle_vals = [rng.randint(min_val + 1, max_val - 1) for _ in range(5)]
    data = [min_val, max_val] + middle_vals
    rng.shuffle(data)
    val_str = ", ".join(str(x) for x in data)

    prompt = (
        f"A learner records the test scores of 7 classmates:\n"
        f"**{val_str}**\n\n"
        f"Calculate the **range** of the test scores."
    )

    return {
        "subskill": "13_range_of_ungrouped_data_maximum_minus_minimum",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(r_val),
        "sample_answer": str(r_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify maximum ({max_val}) and minimum ({min_val}) values", "marks": 1},
            {"step": f"Calculate range: {max_val} - {min_val} = {r_val}", "marks": 1},
        ],
        "hints": [
            "Formula for range: $\\text{Range} = \\text{Maximum} - \\text{Minimum}$.",
            f"Maximum $= {max_val}$, Minimum $= {min_val}$.",
            f"Range $= {max_val} - {min_val} = {r_val}$.",
        ],
        "misconception_tags": ["range_formula_error", "subtracted_wrong_extremes"],
    }


def arch_14_find_missing_data_value_given_mean(rng: random.Random) -> Dict[str, Any]:
    """Solve for unknown value x given the mean of the dataset."""
    target_mean = rng.randint(15, 25)
    n = 5
    total = target_mean * n
    # Choose 4 known values
    vals = [rng.randint(target_mean - 6, target_mean + 6) for _ in range(4)]
    x_val = total - sum(vals)
    while x_val <= 0:
        vals = [rng.randint(target_mean - 6, target_mean + 6) for _ in range(4)]
        x_val = total - sum(vals)

    known_str = ", ".join(str(v) for v in vals)

    prompt = (
        f"The mean of five numbers is **${target_mean}$**.\n"
        f"Four of the numbers are: **{known_str}**, and the fifth number is **$x$**.\n\n"
        f"Calculate the value of **$x$**."
    )

    return {
        "subskill": "14_find_missing_data_value_given_mean",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(x_val),
        "sample_answer": f"x = {x_val}",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate total required sum: 5 * {target_mean} = {total}", "marks": 1},
            {"step": f"Sum known values: {sum(vals)}", "marks": 1},
            {"step": f"Solve for x: {total} - {sum(vals)} = {x_val}", "marks": 1},
        ],
        "hints": [
            f"If the mean of $5$ numbers is ${target_mean}$, their total sum must be $5 \\times {target_mean} = {total}$.",
            f"Add the 4 known numbers: ${' + '.join(str(v) for v in vals)} = {sum(vals)}$.",
            f"$x = {total} - {sum(vals)} = {x_val}$.",
        ],
        "misconception_tags": ["missing_mean_value_algebraic_error"],
    }


def arch_15_find_missing_frequency_in_distribution_given_total(rng: random.Random) -> Dict[str, Any]:
    """Find missing frequency f given the total number of observations."""
    tot = rng.choice([30, 40, 50])
    f1 = rng.randint(6, 12)
    f2 = rng.randint(8, 14)
    f3 = rng.randint(5, 10)
    missing_f = tot - (f1 + f2 + f3)

    prompt = (
        f"A survey of **${tot}$ learners** records the number of pets per household:\n"
        f"- 0 pets: **${f1}$ learners**\n"
        f"- 1 pet: **${f2}$ learners**\n"
        f"- 2 pets: **$f$ learners**\n"
        f"- 3 or more pets: **${f3}$ learners**\n\n"
        f"Calculate the missing frequency **$f$**."
    )

    return {
        "subskill": "15_find_missing_frequency_in_distribution_given_total",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(missing_f),
        "sample_answer": str(missing_f),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Sum known frequencies: {f1} + {f2} + {f3} = {f1 + f2 + f3}", "marks": 1},
            {"step": f"Subtract from total: {tot} - {f1 + f2 + f3} = {missing_f}", "marks": 1},
        ],
        "hints": [
            "The sum of all frequencies must equal the total number of surveyed learners.",
            f"Sum known frequencies: ${f1} + {f2} + {f3} = {f1 + f2 + f3}$.",
            f"$f = {tot} - {f1 + f2 + f3} = {missing_f}$.",
        ],
        "misconception_tags": ["missing_frequency_summation_error"],
    }


def arch_16_identifying_outliers_in_raw_dataset(rng: random.Random) -> Dict[str, Any]:
    """Identify extreme high or low outlier in a dataset."""
    cluster_vals = [rng.randint(20, 28) for _ in range(6)]
    outlier = rng.choice([rng.randint(70, 95), rng.randint(1, 3)])
    data = cluster_vals + [outlier]
    rng.shuffle(data)
    data_str = ", ".join(str(x) for x in data)

    prompt = (
        f"Examine the following set of data values:\n"
        f"**{data_str}**\n\n"
        f"Identify the **outlier** (extreme value) in this dataset."
    )

    return {
        "subskill": "16_identifying_outliers_in_raw_dataset",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(outlier),
        "sample_answer": str(outlier),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recognize that {outlier} lies far away from the main cluster of values (around 20-28)", "marks": 1},
        ],
        "hints": [
            "An outlier is a value that lies an abnormal distance from other values in the dataset.",
            "Look for a number that is much higher or much lower than the rest.",
            f"The outlier is **{outlier}**.",
        ],
        "misconception_tags": ["outlier_identification_error"],
    }


def arch_17_effect_of_outlier_on_mean_vs_median(rng: random.Random) -> Dict[str, Any]:
    """Explain which measure of central tendency is significantly affected by an outlier."""
    prompt = (
        f"When an extreme outlier (such as a mark of 98% in a class where most learners scored around 45%) "
        f"is introduced into a dataset:\n\n"
        f"Which measure of central tendency is **substantially pulled towards the outlier**?\n"
        f"State: **mean**"
    )

    return {
        "subskill": "17_effect_of_outlier_on_mean_vs_median",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "mean",
        "sample_answer": "mean",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that the mean uses the sum of all numerical values and is heavily distorted by extreme outliers, while the median depends only on position", "marks": 1},
        ],
        "hints": [
            "The median depends only on the rank order of values, so an extreme number barely changes it.",
            "The mean sums every value, so an outlier has a dramatic effect on it.",
            "Answer: **mean**.",
        ],
        "misconception_tags": ["mean_vs_median_outlier_sensitivity"],
    }


def arch_18_choosing_appropriate_measure_of_central_tendency_skewed_vs_symmetric(rng: random.Random) -> Dict[str, Any]:
    """Select the best measure of central tendency for a skewed distribution with extreme values."""
    prompt = (
        f"A company reports the monthly salaries of its 20 employees. Nineteen factory workers earn "
        f"around R8 000 each, while the managing director earns R350 000.\n\n"
        f"Which measure of central tendency (**mean**, **median**, or **mode**) gives the most realistic "
        f"and typical representation of an employee's salary?\n"
        f"State: **median**"
    )

    return {
        "subskill": "18_choosing_appropriate_measure_of_central_tendency_skewed_vs_symmetric",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "median",
        "sample_answer": "median",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that for skewed data with extreme outliers (executive salary), the median is the best measure because it is resistant to extreme values", "marks": 1},
        ],
        "hints": [
            "The mean salary would be artificially inflated by the director's R350 000 salary.",
            "The median is not distorted by extreme outliers and represents the typical worker.",
            "Answer: **median**.",
        ],
        "misconception_tags": ["measure_of_central_tendency_selection_error"],
    }


def arch_19_mean_from_ungrouped_frequency_table_sum_fx_over_n(rng: random.Random) -> Dict[str, Any]:
    """Calculate mean from frequency table: sum(f*x) / sum(f)."""
    # 4 scores 1, 2, 3, 4 with frequencies chosen so sum(f*x) % sum(f) == 0 or clean .5
    scores = [1, 2, 3, 4]
    freqs = [rng.randint(2, 5) for _ in range(4)]
    tot_f = sum(freqs)
    tot_fx = sum(s * f for s, f in zip(scores, freqs))
    mean_val = round(tot_fx / float(tot_f), 1)
    ans_str = f"{mean_val:.1f}".rstrip("0").rstrip(".")

    seed_val = rng.randint(1000, 999999)
    svg = draw_frequency_table_svg(scores, freqs, val_label="Score (x)", title="Test Score Frequencies", include_fx=True, seed=seed_val)

    prompt = (
        f"Refer to the frequency table below:\n\n"
        f"Calculate the **mean score** ($\\bar{{x}} = \\frac{{\\sum f \\cdot x}}{{\\sum f}}$)."
    )

    return {
        "subskill": "19_mean_from_ungrouped_frequency_table_sum_fx_over_n",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "tolerance": 0.05,
        "marking_schema": [
            {"step": f"Calculate sum of products: Σ(f·x) = {tot_fx}", "marks": 1},
            {"step": f"Calculate total frequency: Σf = {tot_f}", "marks": 1},
            {"step": f"Calculate mean: {tot_fx} / {tot_f} = {ans_str}", "marks": 1},
        ],
        "hints": [
            "Formula: $\\bar{x} = \\frac{\\sum f \\cdot x}{\\sum f}$.",
            f"Total product $\\sum (f \\cdot x) = {tot_fx}$, Total frequency $\\sum f = {tot_f}$.",
            f"Mean $= \\frac{{{tot_fx}}}{{{tot_f}}} = {ans_str}$.",
        ],
        "misconception_tags": ["divided_by_number_of_rows_instead_of_sum_of_frequencies"],
    }


def arch_20_median_from_ungrouped_frequency_table_cumulative_frequency(rng: random.Random) -> Dict[str, Any]:
    """Determine median score from frequency table."""
    scores = [1, 2, 3, 4, 5]
    freqs = [rng.randint(3, 7) for _ in range(5)]
    tot_f = sum(freqs)
    # Target middle index = (tot_f + 1) / 2
    mid_pos = (tot_f + 1) / 2.0
    
    # Accumulate
    cum = 0
    med_score = scores[0]
    for s, f in zip(scores, freqs):
        cum += f
        if cum >= mid_pos:
            med_score = s
            break

    seed_val = rng.randint(1000, 999999)
    svg = draw_frequency_table_svg(scores, freqs, val_label="Rating (x)", title="Customer Ratings", include_fx=False, seed=seed_val)

    prompt = (
        f"Refer to the customer rating frequency table below with a total of **${tot_f}$ responses**:\n\n"
        f"Determine the **median rating**."
    )

    return {
        "subskill": "20_median_from_ungrouped_frequency_table_cumulative_frequency",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(med_score),
        "sample_answer": str(med_score),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Find middle position: (n + 1)/2 = ({tot_f} + 1)/2 = {mid_pos}", "marks": 1},
            {"step": f"Locate cumulative frequency interval: score {med_score}", "marks": 1},
        ],
        "hints": [
            f"Total responses $n = {tot_f}$. The median is located at position $\\frac{{{tot_f} + 1}}{{2}} = {mid_pos}$.",
            "Add the frequencies down the table until you reach or pass this position.",
            f"The median rating is **{med_score}**.",
        ],
        "misconception_tags": ["frequency_table_median_position_error"],
    }


def arch_21_mode_from_ungrouped_frequency_table_highest_frequency(rng: random.Random) -> Dict[str, Any]:
    """Identify mode from frequency table (the score with maximum frequency)."""
    scores = [10, 11, 12, 13, 14]
    freqs = [rng.randint(3, 6) for _ in range(5)]
    mode_idx = rng.randint(0, 4)
    freqs[mode_idx] = max(freqs) + rng.randint(3, 6)
    mode_score = scores[mode_idx]

    seed_val = rng.randint(1000, 999999)
    svg = draw_frequency_table_svg(scores, freqs, val_label="Age in years (x)", title="Youth Club Attendance", seed=seed_val)

    prompt = (
        f"Refer to the age frequency table below:\n\n"
        f"What is the **mode** (modal age) of the group?"
    )

    return {
        "subskill": "21_mode_from_ungrouped_frequency_table_highest_frequency",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(mode_score),
        "sample_answer": str(mode_score),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify highest frequency: {freqs[mode_idx]}", "marks": 1},
            {"step": f"State corresponding score (mode): {mode_score}", "marks": 1},
        ],
        "hints": [
            "Look for the largest number in the Frequency column.",
            f"The highest frequency is {freqs[mode_idx]}, which corresponds to age {mode_score}.",
            f"The mode is **{mode_score}** (do not state the frequency).",
        ],
        "misconception_tags": ["reported_frequency_instead_of_score_as_mode"],
    }


def arch_22_lower_quartile_q1_calculation(rng: random.Random) -> Dict[str, Any]:
    """Calculate lower quartile (Q1) from ordered list of 11 items."""
    # 11 items: Q1 is the 3rd item, median is the 6th, Q3 is the 9th
    vals = sorted(rng.sample(range(10, 50), 11))
    q1 = vals[2]
    val_str = ", ".join(str(v) for v in vals)

    prompt = (
        f"Consider the ordered dataset of 11 exam marks:\n"
        f"**{val_str}**\n\n"
        f"Calculate the **lower quartile ($Q_1$)** of the dataset."
    )

    return {
        "subskill": "22_lower_quartile_q1_calculation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(q1),
        "sample_answer": str(q1),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that for 11 items, the median splits the data into lower half of 5 items", "marks": 1},
            {"step": f"Find median of the lower 5 items (3rd value): Q1 = {q1}", "marks": 1},
        ],
        "hints": [
            "The median is the 6th item. The lower half consists of the first 5 numbers.",
            f"Lower half: {', '.join(str(x) for x in vals[:5])}.",
            f"The median of this lower half is the 3rd value: **{q1}**.",
        ],
        "misconception_tags": ["quartile_q1_position_error"],
    }


def arch_23_upper_quartile_q3_calculation(rng: random.Random) -> Dict[str, Any]:
    """Calculate upper quartile (Q3) from ordered list of 11 items."""
    vals = sorted(rng.sample(range(15, 60), 11))
    q3 = vals[8]
    val_str = ", ".join(str(v) for v in vals)

    prompt = (
        f"Consider the ordered dataset of 11 test marks:\n"
        f"**{val_str}**\n\n"
        f"Calculate the **upper quartile ($Q_3$)** of the dataset."
    )

    return {
        "subskill": "23_upper_quartile_q3_calculation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(q3),
        "sample_answer": str(q3),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify that the upper half consists of the last 5 numbers", "marks": 1},
            {"step": f"Find median of the upper half (9th value): Q3 = {q3}", "marks": 1},
        ],
        "hints": [
            "The median is the 6th number. The upper half consists of the last 5 numbers.",
            f"Upper half: {', '.join(str(x) for x in vals[6:])}.",
            f"The median of this upper half is the middle (9th overall) number: **{q3}**.",
        ],
        "misconception_tags": ["quartile_q3_position_error"],
    }


def arch_24_interquartile_range_iqr_q3_minus_q1(rng: random.Random) -> Dict[str, Any]:
    """Calculate Interquartile Range (IQR = Q3 - Q1)."""
    q1 = rng.randint(20, 35)
    iqr = rng.randint(12, 24)
    q3 = q1 + iqr

    prompt = (
        f"In a statistical investigation, the quartiles of a dataset are found to be:\n"
        f"- Lower quartile ($Q_1$) = **${q1}$**\n"
        f"- Median ($Q_2$) = **${(q1 + q3) // 2}$**\n"
        f"- Upper quartile ($Q_3$) = **${q3}$**\n\n"
        f"Calculate the **Interquartile Range (IQR)**."
    )

    return {
        "subskill": "24_interquartile_range_iqr_q3_minus_q1",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(iqr),
        "sample_answer": str(iqr),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State IQR formula: IQR = Q3 - Q1", "marks": 1},
            {"step": f"Calculate: {q3} - {q1} = {iqr}", "marks": 1},
        ],
        "hints": [
            "The Interquartile Range is the difference between the upper and lower quartiles: $\\text{IQR} = Q_3 - Q_1$.",
            f"Subtract $Q_1$ from $Q_3$: ${q3} - {q1}$.",
            f"$\\text{{IQR}} = {iqr}$.",
        ],
        "misconception_tags": ["iqr_formula_error", "subtracted_median_instead_of_q1"],
    }


def arch_25_semi_interquartile_range_calculation(rng: random.Random) -> Dict[str, Any]:
    """Calculate Semi-interquartile range = (Q3 - Q1) / 2."""
    semi_iqr = rng.choice([6, 7, 8, 9, 10, 11])
    iqr = 2 * semi_iqr
    q1 = rng.randint(25, 45)
    q3 = q1 + iqr

    prompt = (
        f"A dataset has a lower quartile of **$Q_1 = {q1}$** and an upper quartile of **$Q_3 = {q3}$**.\n\n"
        f"Calculate the **semi-interquartile range** of the data."
    )

    return {
        "subskill": "25_semi_interquartile_range_calculation",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(semi_iqr),
        "sample_answer": str(semi_iqr),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate IQR: Q3 - Q1 = {q3} - {q1} = {iqr}", "marks": 1},
            {"step": f"Divide by 2: {iqr} / 2 = {semi_iqr}", "marks": 1},
        ],
        "hints": [
            "Semi-interquartile range is half of the interquartile range: $\\frac{Q_3 - Q_1}{2}$.",
            f"$\\text{{IQR}} = {q3} - {q1} = {iqr}$.",
            f"Semi-IQR $= \\frac{{{iqr}}}{{2}} = {semi_iqr}$.",
        ],
        "misconception_tags": ["forgot_to_divide_by_two_in_semi_iqr"],
    }
