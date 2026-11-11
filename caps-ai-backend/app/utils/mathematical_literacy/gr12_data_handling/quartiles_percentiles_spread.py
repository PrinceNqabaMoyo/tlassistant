"""Subskills 25 to 32: Measures of spread, quartiles, IQR, semi-IQR, and percentiles."""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_pct,
)


def generate_25_calculating_range_and_limitations(r: random.Random) -> Dict[str, Any]:
    """Calculate the range and evaluate its limitation as a measure of spread."""
    min_v = r.choice([25, 28, 32])
    max_v = r.choice([88, 92, 97])
    rng_val = max_v - min_v

    correct_ans = f"Range = {rng_val}%; it is heavily influenced by the two extreme scores and reveals nothing about clustering in the middle"
    custom_options = [
        correct_ans,
        f"Range = {rng_val}%; it is the most reliable measure because it covers 100% of all learners",
        f"Range = {int(rng_val / 2)}%; it proves that the group has identical academic abilities",
        f"Range = {min_v + max_v}%; it calculates the overall spread of the top quartile",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a Grade 12 trial exam, the lowest mark recorded was {min_v}% and the highest mark recorded was {max_v}%.\n\n"
        f"Calculate the range of the examination results and state its primary limitation as a measure of dispersion."
    )
    explanation = (
        f"Step 1: Formula: Range = Maximum - Minimum [M].\n"
        f"Step 2: Range = {max_v}% - {min_v}% = {rng_val}% [M].\n"
        f"Step 3: Limitation: It depends strictly on extreme values and ignores the distribution of the middle data [A]."
    )
    return _build_question_payload(
        subskill_id="25_calculating_range_and_limitations",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the minimum mark from the maximum mark.",
        tier_2=f"{max_v}% - {min_v}% = {rng_val}%.",
        tier_3="The range is sensitive to single extreme values and does not show how marks cluster in the middle.",
        r=r,
    )


def generate_26_quartiles_odd_dataset(r: random.Random) -> Dict[str, Any]:
    """Calculate Q1 and Q3 for an odd-numbered ordered dataset (excluding median)."""
    # 11 numbers: median is at index 5. Lower half has 5 numbers (index 0..4), Q1 is at index 2.
    # Upper half has 5 numbers (index 6..10), Q3 is at index 8.
    data = sorted([
        r.randint(30, 42), r.randint(43, 49), r.randint(50, 55),
        r.randint(56, 60), r.randint(61, 64), r.randint(65, 68),
        r.randint(69, 72), r.randint(73, 76), r.randint(77, 82),
        r.randint(83, 89), r.randint(90, 98)
    ])
    q1 = data[2]
    med = data[5]
    q3 = data[8]

    correct_ans = f"Q1 = {q1}%; Median (Q2) = {med}%; Q3 = {q3}%"
    custom_options = [
        f"Q1 = {q1}%; Median (Q2) = {med}%; Q3 = {q3}%",
        f"Q1 = {data[1]}%; Median (Q2) = {med}%; Q3 = {data[7]}%",
        f"Q1 = {data[3]}%; Median (Q2) = {med}%; Q3 = {data[9]}%",
        f"Q1 = {int((data[0] + med) / 2)}%; Median (Q2) = {med}%; Q3 = {int((med + data[-1]) / 2)}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    data_str = ", ".join(f"{x}%" for x in data)
    prompt = (
        f"Consider the following 11 ordered test percentages achieved by a study group:\n"
        f"{data_str}\n\n"
        f"Calculate the lower quartile (Q1), median (Q2), and upper quartile (Q3)."
    )
    explanation = (
        f"Step 1: The median (Q2) is the 6th value: {med}% [M].\n"
        f"Step 2: Excluding the median, the lower half is 5 values; Q1 is the middle of the lower half (3rd value): {q1}% [M].\n"
        f"Step 3: The upper half is 5 values; Q3 is the middle of the upper half (9th value): {q3}% [A]."
    )
    return _build_question_payload(
        subskill_id="26_quartiles_odd_dataset",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Locate the middle number (median), then find the middle of the bottom half (Q1) and top half (Q3).",
        tier_2=f"The median is {med}%. The bottom half middle is {q1}%, and the top half middle is {q3}%.",
        tier_3=f"Q1 = {q1}%, Median = {med}%, Q3 = {q3}%.",
        r=r,
    )


def generate_27_quartiles_even_dataset(r: random.Random) -> Dict[str, Any]:
    """Calculate Q1, median, and Q3 for an even-numbered dataset."""
    # 12 numbers: split into two halves of 6 numbers each
    data = sorted([
        35, 36, 42, 48, 52, 54, 58, 62, 65, 70, 78, 85
    ])
    # add small random variation
    shift = r.randint(0, 5)
    data = [x + shift for x in data]

    q1 = (data[2] + data[3]) / 2
    med = (data[5] + data[6]) / 2
    q3 = (data[8] + data[9]) / 2

    correct_ans = f"Q1 = {_fmt(q1, 1)}%; Median = {_fmt(med, 1)}%; Q3 = {_fmt(q3, 1)}%"
    custom_options = [
        f"Q1 = {_fmt(q1, 1)}%; Median = {_fmt(med, 1)}%; Q3 = {_fmt(q3, 1)}%",
        f"Q1 = {_fmt(data[2], 1)}%; Median = {_fmt(med, 1)}%; Q3 = {_fmt(data[9], 1)}%",
        f"Q1 = {_fmt(data[3], 1)}%; Median = {_fmt(med, 1)}%; Q3 = {_fmt(data[8], 1)}%",
        f"Q1 = {_fmt(q1 - 4, 1)}%; Median = {_fmt(med + 2, 1)}%; Q3 = {_fmt(q3 + 3, 1)}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    data_str = "  ".join(str(x) for x in data)
    prompt = (
        f"A set of 12 examination scores is arranged in ascending order:\n"
        f"**{data_str}**\n\n"
        f"Determine Quartile 1 (Q1), the Median (Q2), and Quartile 3 (Q3)."
    )
    explanation = (
        f"Step 1: Split into two halves of 6 values each [M].\n"
        f"Step 2: Median = average of 6th and 7th values: ({data[5]} + {data[6]}) ÷ 2 = {_fmt(med, 1)}% [M].\n"
        f"Step 3: Q1 = average of 3rd and 4th values: ({data[2]} + {data[3]}) ÷ 2 = {_fmt(q1, 1)}% [M].\n"
        f"Step 4: Q3 = average of 9th and 10th values: ({data[8]} + {data[9]}) ÷ 2 = {_fmt(q3, 1)}% [A]."
    )
    return _build_question_payload(
        subskill_id="27_quartiles_even_dataset",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Split the 12 numbers into two equal groups of 6 numbers.",
        tier_2=f"Q1 is the average of {data[2]} and {data[3]}; Q3 is the average of {data[8]} and {data[9]}.",
        tier_3=f"Q1 = {_fmt(q1, 1)}%, Median = {_fmt(med, 1)}%, Q3 = {_fmt(q3, 1)}%.",
        r=r,
    )


def generate_28_calculating_iqr(r: random.Random) -> Dict[str, Any]:
    """Calculate the Interquartile Range (IQR) and explain its meaning."""
    q1 = r.choice([44, 48, 50, 52])
    iqr = r.choice([12, 14, 16, 18, 20])
    q3 = q1 + iqr

    correct_ans = f"IQR = {iqr}%; it measures the spread of the middle 50% of the scores"
    custom_options = [
        correct_ans,
        f"IQR = {iqr}%; it represents the top 25% of learners only",
        f"IQR = {q1 + q3}%; it represents the sum of the quartiles",
        f"IQR = {int(iqr / 2)}%; it represents the average deviation from the median",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In an analysis of Grade 12 preliminary marks, the lower quartile (Q1) is {q1}% "
        f"and the upper quartile (Q3) is {q3}%.\n\n"
        f"Calculate the Interquartile Range (IQR) and state what it represents."
    )
    explanation = (
        f"Step 1: Formula: IQR = Q3 - Q1 [M].\n"
        f"Step 2: IQR = {q3}% - {q1}% = {iqr}% [M].\n"
        f"Step 3: The IQR represents the spread/range of the middle 50% of the dataset [A]."
    )
    return _build_question_payload(
        subskill_id="28_calculating_iqr",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract Q1 from Q3.",
        tier_2=f"{q3}% - {q1}% = {iqr}%.",
        tier_3=f"The IQR is {iqr}%, representing the spread of the middle 50% of data.",
        r=r,
    )


def generate_29_semi_interquartile_range(r: random.Random) -> Dict[str, Any]:
    """Calculate the semi-interquartile range (SIQR)."""
    q1 = r.choice([40, 46, 50])
    iqr = r.choice([14, 16, 22, 26])
    q3 = q1 + iqr
    siqr = iqr / 2

    correct_ans = f"Semi-IQR = {_fmt(siqr, 1)}%"
    custom_options = [
        f"Semi-IQR = {_fmt(siqr, 1)}%",
        f"Semi-IQR = {_fmt(iqr, 1)}%",
        f"Semi-IQR = {_fmt(siqr * 2, 1)}%",
        f"Semi-IQR = {_fmt((q1 + q3) / 2, 1)}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A data set of matric examination results has a lower quartile (Q1) of {q1}% "
        f"and an upper quartile (Q3) of {q3}%.\n\n"
        f"Calculate the semi-interquartile range (SIQR) for this dataset."
    )
    explanation = (
        f"Step 1: Formula: Semi-IQR = (Q3 - Q1) ÷ 2 [M].\n"
        f"Step 2: IQR = {q3}% - {q1}% = {iqr}% [M].\n"
        f"Step 3: Semi-IQR = {iqr}% ÷ 2 = {_fmt(siqr, 1)}% [A]."
    )
    return _build_question_payload(
        subskill_id="29_semi_interquartile_range",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="First find the IQR by subtracting Q1 from Q3, then divide by 2.",
        tier_2=f"({q3} - {q1}) ÷ 2 = {iqr} ÷ 2.",
        tier_3=f"The semi-IQR is {_fmt(siqr, 1)}%.",
        r=r,
    )


def generate_30_interpreting_percentile_ranks(r: random.Random) -> Dict[str, Any]:
    """Differentiate between an examination percentage mark and a percentile rank."""
    score = r.choice([62, 65, 68])
    percentile = r.choice([75, 80, 85])
    correct_ans = f"{percentile}% of learners scored equal to or less than {score}%, while {100 - percentile}% scored higher"

    custom_options = [
        correct_ans,
        f"The learner scored {percentile}% on the test paper instead of {score}%",
        f"The learner answered {percentile}% of the questions correctly",
        f"The learner is in the bottom {100 - percentile}% of the class",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Patrick achieved a test mark of {score}%, which places him in the {percentile}th percentile of Grade 12.\n\n"
        f"Explain precisely what it means to be in the '{percentile}th percentile'."
    )
    explanation = (
        f"Step 1: A percentile rank indicates the percentage of scores in a distribution that are at or below that value [M].\n"
        f"Step 2: {percentile}th percentile means {percentile}% of learners obtained {score}% or less [M].\n"
        f"Step 3: The remaining {100 - percentile}% achieved higher than {score}% [A]."
    )
    return _build_question_payload(
        subskill_id="30_interpreting_percentile_ranks",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Percentile rank measures standing relative to the rest of the cohort, not the actual test mark.",
        tier_2=f"The {percentile}th percentile means {percentile}% of students scored at or below Patrick's score of {score}%.",
        tier_3=f"{percentile}% scored ≤ {score}%, and {100 - percentile}% scored > {score}%.",
        r=r,
    )


def generate_31_reading_growth_charts_percentiles(r: random.Random) -> Dict[str, Any]:
    """Read child stature-for-age percentiles and interpret health status."""
    age_yrs = r.choice([8, 9, 10, 11])
    height_cm = r.choice([122, 126, 134, 138])
    d_spec_31 = {
        "kind": "line_graph",
        "title": f"Road to Health Growth Chart (Age {age_yrs})",
        "x_label": "Age (years)",
        "y_label": "Height (cm)",
        "series": [
            {"name": "10th Percentile", "points": [[age_yrs, height_cm - 2]]},
            {"name": "Child Height", "points": [[age_yrs, height_cm]]},
            {"name": "25th Percentile", "points": [[age_yrs, height_cm + 4]]},
        ],
    }
    correct_ans = "Between the 10th and 25th percentiles (classified as shorter than average, but within normal clinical limits)"

    custom_options = [
        correct_ans,
        "Above the 97th percentile (severely abnormal growth requiring immediate hormonal therapy)",
        "Below the 3rd percentile (severely stunted / clinically underweight)",
        "Exactly at the 50th percentile (exact median height for age)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the Road to Health growth chart for a {age_yrs}-year-old girl with height {height_cm} cm.\n"
        f"The 10th percentile curve is at {height_cm - 2} cm and the 25th percentile curve is at {height_cm + 4} cm.\n\n"
        f"Interpret the girl's growth percentile and health classification."
    )
    explanation = (
        f"Step 1: Compare {height_cm} cm to the percentile bands: {height_cm - 2} cm (P10) < {height_cm} cm < {height_cm + 4} cm (P25) [M].\n"
        f"Step 2: The girl falls between the 10th and 25th percentiles [M].\n"
        f"Step 3: Clinical interpretation: Shorter than average, but within the normal reference range (P3 to P97) [A]."
    )
    return _build_question_payload(
        subskill_id="31_reading_growth_charts_percentiles",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Locate the measured height relative to the percentile thresholds given.",
        tier_2=f"{height_cm} cm lies between the 10th percentile ({height_cm - 2} cm) and 25th percentile ({height_cm + 4} cm).",
        tier_3="Since it lies between P10 and P25, she is shorter than the median but clinically normal.",
        r=r,
    )


def generate_32_position_of_kth_percentile(r: random.Random) -> Dict[str, Any]:
    """Calculate the rank position of the k-th percentile in a dataset."""
    n = r.choice([40, 50, 60, 80])
    p = r.choice([20, 60, 80, 90])
    rank = int(round((p / 100) * n))

    correct_ans = f"Rank position {rank} (the {rank}th value in ascending order)"
    custom_options = [
        f"Rank position {rank} (the {rank}th value in ascending order)",
        f"Rank position {rank + 5} (the {rank + 5}th value in ascending order)",
        f"Rank position {max(1, rank - 6)} (the {max(1, rank - 6)}th value in ascending order)",
        f"Rank position {p} (the {p}th value in ascending order)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A dataset containing the examination scores of {n} learners is arranged from lowest to highest.\n\n"
        f"Calculate the position (rank) of the {p}th percentile in this dataset."
    )
    explanation = (
        f"Step 1: Percentile position formula: Rank = (p ÷ 100) × n [M].\n"
        f"Step 2: Rank = ({p} ÷ 100) × {n} = {rank} [M].\n"
        f"Step 3: The {p}th percentile is at position {rank} in the ordered list [A]."
    )
    return _build_question_payload(
        subskill_id="32_position_of_kth_percentile",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the percentile fraction (p / 100) by the total number of data values.",
        tier_2=f"Calculate ({p} ÷ 100) × {n}.",
        tier_3=f"The rank position is {rank}.",
        r=r,
    )
