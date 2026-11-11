"""Subskills 19 to 27: Measures of Central Tendency (Mean, Median, Mode) & Range for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Subskill 19: Calculate the arithmetic mean from raw data."""
    name = r.choice(SA_NAMES)
    scores = [r.randint(45, 85) for _ in range(6)]
    total_sum = sum(scores)
    n = len(scores)
    mean_val = round(total_sum / n, 1)

    prompt = (
        f"{name} recorded the following percentages in 6 Mathematical Literacy class tests:\n"
        f"**{', '.join(f'{s}%' for s in scores)}**\n"
        f"Calculate {name}'s mean (average) test mark (round to one decimal place)."
    )

    correct_ans = f"{_fmt(mean_val, 1)}%"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: State the formula for the mean [1 mark].\n"
        f"\\text{{Mean}} = \\frac{{\\sum x}}{{n}} = \\frac{{{total_sum}}}{{{n}}}.\n"
        f"Step 2: Add all test marks together [1 mark].\n"
        f"Sum = {' + '.join(str(s) for s in scores)} = {total_sum}.\n"
        f"Step 3: Divide by {n} tests [1 mark].\n"
        f"Mean = {total_sum} ÷ {n} = {_fmt(mean_val, 1)}% ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="19",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Mean = (Sum of all values) ÷ (Number of values).",
        tier_2=f"Sum of marks = {total_sum}. Divide by {n}.",
        tier_3=f"Mean = {_fmt(mean_val, 1)}%.",
        r=r,
    )


def generate_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Subskill 20: Find a missing value given the target mean."""
    name = r.choice(SA_NAMES)
    target_mean = r.choice([60, 65, 70, 75])
    n = 5
    required_total = target_mean * n

    # Choose 4 known scores such that the 5th is between 40 and 95
    known_scores = [r.randint(target_mean - 15, target_mean + 15) for _ in range(3)]
    sum_3 = sum(known_scores)
    # pick 4th score so 5th is clean
    score_4 = r.randint(target_mean - 10, target_mean + 10)
    known_scores.append(score_4)
    sum_known = sum(known_scores)

    missing_score = required_total - sum_known

    prompt = (
        f"{name} wants to achieve an average of {_fmt(target_mean)}% across 5 term tests. "
        f"{name}'s marks for the first 4 tests are: "
        f"**{', '.join(f'{s}%' for s in known_scores)}**.\n"
        f"What mark must {name} obtain in the 5th test to achieve the target mean of {_fmt(target_mean)}%?"
    )

    correct_ans = f"{missing_score}%"
    wrong_1 = f"{missing_score + 10}%"
    wrong_2 = f"{missing_score - 8}%"
    wrong_3 = f"{target_mean}%"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the required total points for 5 tests [1 mark].\n"
        f"Required total = 5 × {_fmt(target_mean)}% = {required_total}%.\n"
        f"Step 2: Calculate sum of the 4 known test scores [1 mark].\n"
        f"Current sum = {' + '.join(str(s) for s in known_scores)} = {sum_known}%.\n"
        f"Step 3: Subtract current sum from required total [1 mark].\n"
        f"5th test mark = {required_total}% - {sum_known}% = {missing_score}% ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="20",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply target mean by total number of tests (5), then subtract the sum of the known tests.",
        tier_2=f"Total needed = 5 × {_fmt(target_mean)} = {required_total}. Current sum = {sum_known}.",
        tier_3=f"Mark needed = {required_total} - {sum_known} = {missing_score}%.",
        r=r,
    )


def generate_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Determine median from an odd number of data observations."""
    name = r.choice(SA_NAMES)
    raw_vals = [r.randint(12, 45) for _ in range(7)]
    sorted_vals = sorted(raw_vals)
    median_val = sorted_vals[3]  # middle of 7 (index 3)

    prompt = (
        f"The number of customers served daily at a local post office counter over 7 days was recorded as:\n"
        f"**{', '.join(str(v) for v in raw_vals)}**\n"
        f"Determine the median number of customers served."
    )

    correct_ans = f"{median_val} customers"
    wrong_1 = f"{sorted_vals[2]} customers"
    wrong_2 = f"{sorted_vals[4]} customers"
    wrong_3 = f"{round(sum(raw_vals) / 7, 1)} customers"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Arrange data in ascending numerical order [1 mark].\n"
        f"Ordered data: {', '.join(str(v) for v in sorted_vals)}.\n"
        f"Step 2: Find position of the median [1 mark].\n"
        f"Position = (n + 1) ÷ 2 = (7 + 1) ÷ 2 = 4th value.\n"
        f"Step 3: Stated median [1 mark]: The 4th value is {median_val} ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="21",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="First sort the numbers in order from smallest to largest, then locate the middle number.",
        tier_2=f"Sorted list: {', '.join(str(v) for v in sorted_vals)}.",
        tier_3=f"The middle (4th) number is {median_val}.",
        r=r,
    )


def generate_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Subskill 22: Determine median from an even number of data observations."""
    name = r.choice(SA_NAMES)
    raw_vals = [r.randint(50, 95) for _ in range(8)]
    sorted_vals = sorted(raw_vals)
    m1 = sorted_vals[3]
    m2 = sorted_vals[4]
    median_val = round((m1 + m2) / 2, 1)

    prompt = (
        f"A clinic recorded the systolic blood pressure readings of 8 adult patients:\n"
        f"**{', '.join(str(v) for v in raw_vals)}**\n"
        f"Determine the median blood pressure reading."
    )

    correct_ans = f"{_fmt(median_val, 1)}"
    wrong_1 = f"{m1}"
    wrong_2 = f"{m2}"
    wrong_3 = f"{_fmt(median_val + 3.0, 1)}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Arrange data in ascending order [1 mark].\n"
        f"Ordered: {', '.join(str(v) for v in sorted_vals)}.\n"
        f"Step 2: Identify the two middle values (4th and 5th values) [1 mark].\n"
        f"The two central values are {m1} and {m2}.\n"
        f"Step 3: Calculate their average [1 mark].\n"
        f"Median = ({m1} + {m2}) ÷ 2 = {_fmt(median_val, 1)} ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="22",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="For an even number of observations, arrange in order and find the mean of the two middle values.",
        tier_2=f"Sorted: {', '.join(str(v) for v in sorted_vals)}. Middle values: {m1} and {m2}.",
        tier_3=f"Median = ({m1} + {m2}) ÷ 2 = {_fmt(median_val, 1)}.",
        r=r,
    )


def generate_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Subskill 23: Mode identification (unimodal, bimodal, or no mode)."""
    mode_val = r.choice([14, 18, 22, 25, 28, 30])
    # Build list where mode_val appears 3 times, others appear 1 time
    other_vals = [v for v in [12, 15, 17, 20, 24, 27, 29, 32] if v != mode_val][:4]
    data_list = [mode_val, mode_val, mode_val] + other_vals
    r.shuffle(data_list)

    prompt = (
        f"The ages of participants in a community leadership workshop are recorded below:\n"
        f"**{', '.join(str(v) for v in data_list)}**\n"
        f"Identify the mode of this data set."
    )

    correct_ans = f"{mode_val}"
    options, _ = _build_options(correct_ans, r, custom_options=[str(mode_val)] + [str(v) for v in other_vals[:3]])

    explanation = (
        f"Step 1: Count the frequency of each value in the data set [1 mark].\n"
        f"Value {mode_val} appears 3 times, while all other values appear only once.\n"
        f"Step 2: Recall definition of mode [1 mark].\n"
        f"The mode is the value that occurs most frequently.\n"
        f"Step 3: Stated mode [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="23",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The mode is the number that appears most often in the list.",
        tier_2=f"Check which number is repeated the most times.",
        tier_3=f"Mode = {mode_val}.",
        r=r,
    )


def generate_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Subskill 24: Selecting the most appropriate measure of central tendency (Mean vs Median)."""
    scenario = r.choice([
        (
            "monthly household incomes in an informal settlement where 9 families earn between R 3 000 and R 6 000, but one wealthy property owner earns R 150 000",
            "Median",
            "The median is not distorted by extreme high outliers, whereas the mean would give a falsely inflated impression of typical resident income"
        ),
        (
            "the masses of 50 standard 500 g butter bricks produced by a high-precision automated factory line with minimal symmetrical variation",
            "Mean",
            "The data is symmetrically distributed with no outliers, making the mean the most comprehensive measure that incorporates all data points"
        ),
        (
            "the shoe sizes of 200 soccer boots ordered for a youth tournament to determine which single size to order the most of",
            "Mode",
            "Shoe sizes are discrete sizes where the most frequently requested size indicates inventory demand"
        ),
    ])
    context, best_measure, rationale = scenario

    prompt = (
        f"Consider a data collection project measuring {context}.\n"
        f"Which measure of central tendency is the most suitable and representative to summarize this data?"
    )

    correct_ans = f"{best_measure} ({rationale})"
    distractors = [
        f"{m} ({rat})"
        for m, rat in [
            ("Mean", "The data is symmetrically distributed with no outliers"),
            ("Median", "It is resistant to extreme outliers in skewed distributions"),
            ("Mode", "It identifies the single most popular discrete category"),
        ]
        if m != best_measure
    ][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Inspect the distribution characteristics of the data [1 mark].\n"
        f"The scenario involves: {context}.\n"
        f"Step 2: Evaluate sensitivity to outliers or data type [1 mark].\n"
        f"{rationale}.\n"
        f"Step 3: Stated conclusion [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="24",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="When data has an extreme outlier, the median is preferred. For symmetrical data, the mean is preferred. For stock sizes, the mode is preferred.",
        tier_2=f"The most suitable measure here is {best_measure}.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Subskill 25: Calculate data range: Range = Max - Min."""
    name = r.choice(SA_NAMES)
    vals = [r.randint(15, 85) for _ in range(8)]
    min_v = min(vals)
    max_v = max(vals)
    range_val = max_v - min_v

    prompt = (
        f"{name} monitors the daily maximum temperatures (in °C) over 8 days in Upington:\n"
        f"**{', '.join(f'{v}°C' for v in vals)}**\n"
        f"Calculate the range of the temperatures."
    )

    correct_ans = f"{range_val}°C"
    wrong_1 = f"{range_val + 5}°C"
    wrong_2 = f"{range_val - 3}°C"
    wrong_3 = f"{round(sum(vals) / 8, 1)}°C"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify the maximum and minimum values [1 mark].\n"
        f"Maximum = {max_v}°C; Minimum = {min_v}°C.\n"
        f"Step 2: Apply the range formula [1 mark].\n"
        f"\\text{{Range}} = \\text{{Maximum}} - \\text{{Minimum}} = {max_v} - {min_v} = {range_val}°C.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="25",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Range = Highest value - Lowest value.",
        tier_2=f"Highest = {max_v}°C, Lowest = {min_v}°C.",
        tier_3=f"Range = {max_v} - {min_v} = {range_val}°C.",
        r=r,
    )


def generate_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Subskill 26: Impact of adding a constant c to all data points."""
    name = r.choice(SA_NAMES)
    bonus = r.choice([5, 10, 15])
    old_mean = r.choice([55, 60, 65])
    old_range = r.choice([30, 35, 40])

    prompt = (
        f"In a test, the original mean score was {_fmt(old_mean)}% and the range of scores was {_fmt(old_range)}%. "
        f"Because of a disputed question, the teacher decides to award a bonus of {_fmt(bonus)}% to EVERY learner's score.\n"
        f"What will be the NEW mean and the NEW range of the scores?"
    )

    new_mean = old_mean + bonus
    new_range = old_range  # range does not change when adding a constant!

    correct_ans = f"New Mean = {_fmt(new_mean)}%; New Range = {_fmt(new_range)}% (unchanged)"
    wrong_1 = f"New Mean = {_fmt(new_mean)}%; New Range = {_fmt(new_range + bonus)}%"
    wrong_2 = f"New Mean = {_fmt(old_mean)}%; New Range = {_fmt(new_range)}%"
    wrong_3 = f"New Mean = {_fmt(new_mean + bonus)}%; New Range = {_fmt(new_range * 2)}%"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Effect of adding a constant on the mean [1 mark].\n"
        f"Adding {bonus} to every score increases the mean by exactly {bonus}: New Mean = {old_mean} + {bonus} = {new_mean}%.\n"
        f"Step 2: Effect of adding a constant on the range [1 mark].\n"
        f"Range = (Max + {bonus}) - (Min + {bonus}) = Max - Min = {old_range}% (remains completely unchanged).\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="26",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Adding a constant shifts all values upward, so the mean increases, but the spread (range) stays the same.",
        tier_2=f"Mean increases by {bonus} to {new_mean}%. Range stays at {old_range}%.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Subskill 27: Impact of multiplying all data points by a factor k."""
    factor = r.choice([2, 3])
    old_mean = r.choice([20, 25, 30])
    old_range = r.choice([15, 20])

    new_mean = old_mean * factor
    new_range = old_range * factor

    prompt = (
        f"A data set of worker overtime hours has a mean of {_fmt(old_mean)} hours and a range of {_fmt(old_range)} hours. "
        f"If every worker's overtime hours are multiplied by a factor of {factor} due to a production surge, "
        f"what will be the new mean and the new range?"
    )

    correct_ans = f"New Mean = {_fmt(new_mean)} hours; New Range = {_fmt(new_range)} hours"
    wrong_1 = f"New Mean = {_fmt(new_mean)} hours; New Range = {_fmt(old_range)} hours (unchanged)"
    wrong_2 = f"New Mean = {_fmt(old_mean)} hours; New Range = {_fmt(new_range)} hours"
    wrong_3 = f"New Mean = {_fmt(new_mean + 5)} hours; New Range = {_fmt(new_range + 5)} hours"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Effect of multiplying by a factor on the mean [1 mark].\n"
        f"When every value is multiplied by {factor}, the new mean is {factor} × {old_mean} = {new_mean} hours.\n"
        f"Step 2: Effect of multiplying by a factor on the range [1 mark].\n"
        f"New Range = ({factor} × Max) - ({factor} × Min) = {factor} × (Max - Min) = {factor} × {old_range} = {new_range} hours.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="27",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiplying every value by a constant multiplies both the measures of center (mean) and measures of spread (range).",
        tier_2=f"Multiply both the mean ({old_mean}) and range ({old_range}) by {factor}.",
        tier_3=f"New Mean = {new_mean} hours; New Range = {new_range} hours.",
        r=r,
    )
