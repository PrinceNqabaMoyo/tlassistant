"""Cluster 3: Measures of Central Tendency (Subskills 17 to 25).

Covers:
17. Arithmetic mean calculation for raw ungrouped datasets (Mean = ∑ x / n)
18. Weighted mean from a frequency table (Mean = ∑(f·x) / ∑ f)
19. Median calculation with an odd number of data values (position (n+1)/2)
20. Median calculation with an even number of data values (average of two middle terms)
21. Unsorted raw data ordering protocol before locating the median
22. Mode identification for unimodal numerical datasets
23. Bimodal distributions and datasets with no mode (equal frequencies)
24. Modal category identification for qualitative/categorical data
25. Reconstructing a missing score from a required target mean (algebraic tracking)
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_data_mean_raw_ungrouped_dataset(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    context = r.choice([
        ("mathematics test scores (%)", [r.randint(45, 88) for _ in range(r.choice([6, 7, 8]))]),
        ("daily maximum temperatures (°C)", [r.randint(18, 34) for _ in range(7)]),
        ("daily litres of milk produced by a dairy cow", [r.randint(15, 28) for _ in range(6)]),
    ])
    ctx_name, raw_data = context
    n = len(raw_data)
    total_sum = sum(raw_data)
    mean_val = round(total_sum / n, 2)
    data_str = ", ".join(map(str, raw_data))

    prompt = (
        f"{name} records the following dataset of {ctx_name} over {n} observations:\n"
        f"**{data_str}**\n\n"
        f"Formula: Mean = Sum of all values ÷ Number of values (Mean = ∑ x ÷ n)\n\n"
        f"Calculate the mean of this dataset (rounded to 2 decimal places)."
    )
    ans = f"{_fmt(mean_val)}"

    s1 = f"Sum all {n} values in the dataset ({total_sum}) and divide by the total number of observations ({n})."
    s2 = f"✓ [1 Mark: Method – Adding all values and dividing by count n]\nSum = {' + '.join(map(str, raw_data))} = {total_sum}.\nMean = {total_sum} ÷ {n}."
    s3 = f"✓ [1 Mark: Accuracy – Final calculated mean]\nMean = {_fmt(mean_val)}."

    return _build_question_payload(
        "data_mean_raw_ungrouped_dataset",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Add up all {n} numbers: sum = {total_sum}.",
        tier_2_hint=f"Divide the sum by the number of values: {total_sum} ÷ {n}.",
        tier_3_hint=f"Mean = {_fmt(mean_val)}.",
    )


def _gen_data_mean_frequency_table_weighted(r: random.Random) -> Dict[str, Any]:
    # Number of children per household (x = 0, 1, 2, 3, 4)
    x_vals = [0, 1, 2, 3, 4]
    f_vals = [r.randint(4, 8), r.randint(6, 12), r.randint(8, 15), r.randint(5, 10), r.randint(2, 6)]
    fx_vals = [x * f for x, f in zip(x_vals, f_vals)]
    sum_f = sum(f_vals)
    sum_fx = sum(fx_vals)
    mean_val = round(sum_fx / sum_f, 2)

    prompt = (
        f"A municipal housing survey records the number of school-going children per household in a street:\n\n"
        f"| Number of Children (x) | Number of Households (f) | f × x |\n"
        f"| :---: | :---: | :---: |\n"
        f"| 0 | {f_vals[0]} | {fx_vals[0]} |\n"
        f"| 1 | {f_vals[1]} | {fx_vals[1]} |\n"
        f"| 2 | {f_vals[2]} | {fx_vals[2]} |\n"
        f"| 3 | {f_vals[3]} | {fx_vals[3]} |\n"
        f"| 4 | {f_vals[4]} | {fx_vals[4]} |\n"
        f"| **Total** | **∑ f = {sum_f}** | **∑(f·x) = {sum_fx}** |\n\n"
        f"Formula: Mean = ∑(f × x) ÷ ∑ f\n\n"
        f"Calculate the mean number of school-going children per household (rounded to 2 decimal places)."
    )
    ans = f"{_fmt(mean_val)} children"

    s1 = f"Divide the sum of products ∑(f × x) ({sum_fx}) by the total number of households ∑ f ({sum_f})."
    s2 = f"✓ [1 Mark: Method – Weighted mean formula substitution]\nMean = ∑(f × x) ÷ ∑ f = {sum_fx} ÷ {sum_f}."
    s3 = f"✓ [1 Mark: Accuracy – Mean value rounded to 2 decimal places]\nMean = {_fmt(mean_val)} children."

    return _build_question_payload(
        "data_mean_frequency_table_weighted",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide the total of the f × x column ({sum_fx}) by the total frequency ({sum_f}).",
        tier_2_hint=f"{sum_fx} ÷ {sum_f} = {_fmt(mean_val)}.",
        tier_3_hint=f"Mean = {_fmt(mean_val)} children.",
    )


def _gen_data_median_odd_number_of_values(r: random.Random) -> Dict[str, Any]:
    n = r.choice([7, 9, 11])
    raw_nums = sorted([r.randint(12, 60) for _ in range(n)])
    median_val = raw_nums[n // 2]
    # Scramble to present unsorted
    scrambled = list(raw_nums)
    r.shuffle(scrambled)
    data_str = ", ".join(map(str, scrambled))
    sorted_str = ", ".join(map(str, raw_nums))
    pos = (n + 1) // 2

    prompt = (
        f"Study the following dataset containing an **odd number of {n} values**:\n"
        f"**{data_str}**\n\n"
        f"1. Arrange the data values in ascending order.\n"
        f"2. Determine the position of the median using position formula = (n + 1) ÷ 2.\n"
        f"3. State the value of the median."
    )
    ans = f"Median = {median_val} (at position {pos})"

    s1 = f"First arrange the {n} values in ascending order: {sorted_str}. Since n = {n} is odd, the median is the single middle value at position ({n} + 1) ÷ 2 = {pos}."
    s2 = f"✓ [1 Mark: Method – Arranging in order and locating middle position]\nOrdered: {sorted_str}.\nPosition = ({n} + 1) ÷ 2 = {pos}th value."
    s3 = f"✓ [1 Mark: Accuracy – Value of the median]\nMedian = {median_val}."

    return _build_question_payload(
        "data_median_odd_number_of_values",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"First sort the {n} numbers in ascending order from smallest to largest.",
        tier_2_hint=f"The median is at position ({n} + 1) ÷ 2 = {pos}.",
        tier_3_hint=f"The {pos}th value in the sorted list is {median_val}.",
    )


def _gen_data_median_even_number_of_values(r: random.Random) -> Dict[str, Any]:
    n = r.choice([8, 10])
    raw_nums = sorted([r.randint(15, 65) for _ in range(n)])
    mid1 = raw_nums[(n // 2) - 1]
    mid2 = raw_nums[n // 2]
    median_val = round((mid1 + mid2) / 2, 1)

    scrambled = list(raw_nums)
    r.shuffle(scrambled)
    data_str = ", ".join(map(str, scrambled))
    sorted_str = ", ".join(map(str, raw_nums))
    p1 = n // 2
    p2 = p1 + 1

    prompt = (
        f"Study the following dataset containing an **even number of {n} values**:\n"
        f"**{data_str}**\n\n"
        f"1. Arrange the data in ascending order.\n"
        f"2. Identify the two middle values at positions {p1} and {p2}.\n"
        f"3. Calculate the median."
    )
    ans = f"Median = {_fmt(median_val)} (average of {mid1} and {mid2})"

    s1 = f"Arrange data in ascending order: {sorted_str}. With an even sample size (n = {n}), the median is the mean of the two central numbers at positions {p1} ({mid1}) and {p2} ({mid2}): ({mid1} + {mid2}) ÷ 2."
    s2 = f"✓ [1 Mark: Method – Identifying two middle values and averaging them]\nOrdered: {sorted_str}.\nMiddle values: {mid1} and {mid2}.\nMedian = ({mid1} + {mid2}) ÷ 2."
    s3 = f"✓ [1 Mark: Accuracy – Calculated median]\nMedian = {_fmt(median_val)}."

    return _build_question_payload(
        "data_median_even_number_of_values",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Sort the numbers from smallest to largest.",
        tier_2_hint=f"Find the two middle numbers at positions {p1} and {p2}: {mid1} and {mid2}.",
        tier_3_hint=f"Median = ({mid1} + {mid2}) ÷ 2 = {_fmt(median_val)}.",
    )


def _gen_data_median_unsorted_list_ordering_step(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner is given an unsorted list of 7 test scores: 55, 82, 41, 63, 90, 72, 48.\n\n"
        f"The learner looks at the middle number in the written list (63) and writes down: 'Median = 63'.\n\n"
        f"Why is this learner's method mathematically incorrect?"
    )
    ans = "The data values MUST be arranged in ascending (or descending) order first before selecting the middle value."
    opts = [
        "The data values MUST be arranged in ascending (or descending) order first before selecting the middle value.",
        "The median can only be calculated on an even number of values.",
        "Test scores cannot have a median because they are percentages.",
        "The learner was supposed to add 15% VAT to the middle value.",
    ]

    s1 = f"By mathematical definition, the median is the value that splits an ordered dataset into two equal halves. Finding the middle of an unsorted list has no statistical meaning."
    s2 = f"✓ [1 Mark: Method – Identifying sorting prerequisite for median calculation]\nValues must be ranked from minimum to maximum: 41, 48, 55, 63, 72, 82, 90 (in this case, by coincidence, 63 is the sorted median, but the method was fundamentally flawed)."
    s3 = f"✓ [1 Mark: Accuracy – Correct methodological rule]\nRule: The data values MUST be arranged in ascending (or descending) order first before selecting the middle value."

    return _build_question_payload(
        "data_median_unsorted_list_ordering_step",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What must you always do with numbers before finding the median?",
        tier_2_hint="The numbers must be sorted in order from smallest to largest.",
        tier_3_hint="Sorting in ascending or descending order is a mandatory first step.",
    )


def _gen_data_mode_unimodal_raw_dataset(r: random.Random) -> Dict[str, Any]:
    mode_val = r.randint(18, 45)
    other_vals = [v for v in [r.randint(15, 50) for _ in range(5)] if v != mode_val]
    # mode_val appears 3 times, others appear once
    data = [mode_val, mode_val, mode_val] + other_vals[:4]
    r.shuffle(data)
    data_str = ", ".join(map(str, data))

    prompt = (
        f"Consider the following set of data values:\n"
        f"**{data_str}**\n\n"
        f"Identify the **mode** of this dataset and give a reason for your answer."
    )
    ans = f"Mode = {mode_val} (it appears most frequently: 3 times)"

    s1 = f"Count the frequency of occurrence of each distinct number in the dataset. The mode is the value that appears with the highest frequency."
    s2 = f"✓ [1 Mark: Method – Frequency tally of each number]\nFrequency of {mode_val} = 3; all other values appear once."
    s3 = f"✓ [1 Mark: Accuracy – Value of the mode]\nMode = {mode_val}."

    return _build_question_payload(
        "data_mode_unimodal_raw_dataset",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Find the number that appears most often in the list.",
        tier_2_hint=f"Count how many times each number appears. {mode_val} appears 3 times.",
        tier_3_hint=f"Mode = {mode_val}.",
    )


def _gen_data_mode_bimodal_and_no_mode(r: random.Random) -> Dict[str, Any]:
    is_bimodal = r.choice([True, False])
    if is_bimodal:
        m1, m2 = r.choice([(14, 28), (22, 35), (18, 42), (30, 55)])
        data = [m1, m1, m2, m2, m1 + 3, m2 + 5, m1 - 2]
        r.shuffle(data)
        data_str = ", ".join(map(str, data))
        ans = f"Bimodal: {m1} and {m2} (both appear twice with equal highest frequency)"
        explanation = f"Since both {m1} and {m2} appear twice and all other numbers appear once, the dataset is bimodal with two modes: {m1} and {m2}."
    else:
        distinct_nums = sorted(random.sample(range(10, 50), 6))
        data_str = ", ".join(map(str, distinct_nums))
        ans = "No mode (each value occurs exactly once with equal frequency)"
        explanation = "Every number in the list appears exactly once. When no value appears more frequently than the others, there is no mode."

    prompt = (
        f"Analyse the following dataset:\n"
        f"**{data_str}**\n\n"
        f"Determine the mode(s) of this dataset."
    )

    s1 = f"Examine frequency of each distinct value in the list."
    s2 = f"✓ [1 Mark: Method – Identifying frequency distribution and ties]\n{explanation}"
    s3 = f"✓ [1 Mark: Accuracy – Final modal classification]\n{ans}"

    return _build_question_payload(
        "data_mode_bimodal_and_no_mode",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Count how many times each number appears in the list.",
        tier_2_hint="Check if two numbers tie for highest frequency, or if every number appears only once.",
        tier_3_hint=f"{ans}.",
    )


def _gen_data_modal_category_qualitative(r: random.Random) -> Dict[str, Any]:
    colors = ["White", "Silver", "Black", "Blue", "Red"]
    counts = [r.randint(35, 55), r.randint(25, 35), r.randint(20, 30), r.randint(10, 18), r.randint(5, 12)]
    max_c = max(counts)
    modal_color = colors[counts.index(max_c)]

    prompt = (
        f"A parking lot survey records the exterior colours of passenger cars entering a shopping mall:\n\n"
        f"| Car Colour | Frequency |\n"
        f"| :--- | :---: |\n"
        f"| White | {counts[0]} |\n"
        f"| Silver | {counts[1]} |\n"
        f"| Black | {counts[2]} |\n"
        f"| Blue | {counts[3]} |\n"
        f"| Red | {counts[4]} |\n\n"
        f"1. Can a mathematical mean or median be calculated for this dataset? Explain why.\n"
        f"2. Identify the **modal category** of car colours."
    )
    ans = f"No mean/median (data is qualitative/categorical words, not numbers); Modal category = {modal_color} (highest frequency of {max_c})"
    opts = [
        f"No mean/median (data is qualitative/categorical words, not numbers); Modal category = {modal_color} (highest frequency of {max_c})",
        f"Yes (mean = 25); Modal category = Silver",
        f"Yes (median = Black); Modal category = White",
        "Categorical data has no mode under any circumstances.",
    ]

    s1 = f"Recognise that categorical data (words/labels) cannot undergo arithmetic addition or ranking required for mean and median, but the mode is always valid as the category with the highest frequency."
    s2 = f"✓ [1 Mark: Method – Explaining categorical restriction and identifying maximum frequency]\nWords cannot be averaged. Highest frequency = {max_c} in category '{modal_color}'."
    s3 = f"✓ [1 Mark: Accuracy – Modal category and conceptual explanation]\n{ans}"

    return _build_question_payload(
        "data_modal_category_qualitative",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Can you add colours like 'White + Blue' to find an average? No.",
        tier_2_hint=f"Which colour has the largest number of cars? {modal_color} with {max_c}.",
        tier_3_hint=f"{ans}",
    )


def _gen_data_mean_reconstructing_missing_test_score(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    t1, t2, t3 = r.randint(52, 75), r.randint(55, 78), r.randint(58, 80)
    target_mean = r.randint(70, 75)
    total_tests = 4
    required_total = total_tests * target_mean
    current_sum = t1 + t2 + t3
    needed_score = required_total - current_sum

    prompt = (
        f"{name} has written 3 out of 4 Mathematical Literacy tests this term. {name}'s marks are:\n"
        f"• Test 1: {t1}%\n"
        f"• Test 2: {t2}%\n"
        f"• Test 3: {t3}%\n\n"
        f"{name} aims to achieve an overall term mean mark of exactly **{target_mean}%** across all 4 tests.\n\n"
        f"Calculate the mark {name} must score on Test 4 to achieve this target mean."
    )
    ans = f"{needed_score}%"

    s1 = f"Calculate the total marks required across all 4 tests ({total_tests} × {target_mean}% = {required_total}%), sum the 3 completed tests ({t1} + {t2} + {t3} = {current_sum}%), then subtract to find Test 4."
    s2 = f"✓ [1 Mark: Method – Multiplying target mean by 4 and subtracting known marks]\nTotal required = 4 × {target_mean}% = {required_total}%.\nCurrent sum = {t1} + {t2} + {t3} = {current_sum}%.\nTest 4 = {required_total}% − {current_sum}%."
    s3 = f"✓ [1 Mark: Accuracy – Required score on final test]\nTest 4 mark needed = {needed_score}%."

    return _build_question_payload(
        "data_mean_reconstructing_missing_test_score",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the total points needed for 4 tests: 4 × {target_mean}% = {required_total}%.",
        tier_2_hint=f"Add the first 3 test scores: {t1} + {t2} + {t3} = {current_sum}%.",
        tier_3_hint=f"{required_total}% − {current_sum}% = {needed_score}%.",
    )
