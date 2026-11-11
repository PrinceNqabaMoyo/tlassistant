"""Cluster 4: Measures of Spread & Quartiles (Subskills 26 to 34).

Covers:
26. Range calculation: Maximum value minus Minimum value
27. Range involving negative values (e.g. sub-zero winter temperatures)
28. Lower Quartile (Q1 / 25th percentile) determination from ordered data
29. Upper Quartile (Q3 / 75th percentile) determination from ordered data
30. Interquartile Range (IQR = Q3 - Q1) calculation
31. Semi-interquartile range calculation (Semi-IQR = IQR / 2)
32. Outlier impact analysis: vulnerability of Mean vs robustness of Median
33. Numerical identification of extreme outliers in raw datasets
34. Comparative consistency analysis between two groups using Range and IQR
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_data_range_calculation_max_minus_min(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    marks = [r.randint(35, 95) for _ in range(r.choice([7, 8, 9]))]
    min_m = min(marks)
    max_m = max(marks)
    rng_val = max_m - min_m
    marks_str = ", ".join(map(str, marks))

    prompt = (
        f"{name} records the marks obtained by a study group in a test:\n"
        f"**{marks_str}**\n\n"
        f"Formula: Range = Maximum value − Minimum value\n\n"
        f"1. Identify the maximum and minimum mark in this dataset.\n"
        f"2. Calculate the **range** of marks."
    )
    ans = f"Range = {rng_val} (Maximum = {max_m}, Minimum = {min_m})"

    s1 = f"Identify the largest number (Maximum = {max_m}) and the smallest number (Minimum = {min_m}) in the list, then subtract."
    s2 = f"✓ [1 Mark: Method – Identifying extreme values and applying range formula]\nRange = Maximum − Minimum = {max_m} − {min_m}."
    s3 = f"✓ [1 Mark: Accuracy – Final calculated range]\nRange = {rng_val}."

    return _build_question_payload(
        "data_range_calculation_max_minus_min",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the largest mark ({max_m}) and the smallest mark ({min_m}).",
        tier_2_hint=f"Subtract the minimum from the maximum: {max_m} − {min_m}.",
        tier_3_hint=f"Range = {rng_val}.",
    )


def _gen_data_range_temperature_negative_integers(r: random.Random) -> Dict[str, Any]:
    town = r.choice(["Sutherland (Northern Cape)", "Barkly East (Eastern Cape)", "Underberg (KwaZulu-Natal)"])
    min_temp = r.randint(-7, -2) # Negative integer
    max_temp = r.randint(14, 22) # Positive integer
    temp_range = max_temp - min_temp

    prompt = (
        f"During a cold winter front, the weather bureau records the following extreme temperatures in {town}:\n"
        f"• Minimum overnight temperature: {min_temp} °C\n"
        f"• Maximum afternoon temperature: {max_temp} °C\n\n"
        f"Formula: Temperature Range = Maximum Temperature − Minimum Temperature\n\n"
        f"Calculate the temperature range (temperature difference) in degrees Celsius (°C)."
    )
    ans = f"{temp_range} °C"

    s1 = f"Subtract the negative minimum temperature from the positive maximum temperature: {max_temp} − ({min_temp}) = {max_temp} + {abs(min_temp)}."
    s2 = f"✓ [1 Mark: Method – Range with double negative subtraction setup]\nRange = {max_temp} °C − ({min_temp} °C) = {max_temp} + {abs(min_temp)}."
    s3 = f"✓ [1 Mark: Accuracy – Temperature range value]\nRange = {temp_range} °C."

    return _build_question_payload(
        "data_range_temperature_negative_integers",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Subtracting a negative number is the same as adding: {max_temp} − ({min_temp}) = {max_temp} + {abs(min_temp)}.",
        tier_2_hint=f"{max_temp} + {abs(min_temp)} = {temp_range}.",
        tier_3_hint=f"Range = {temp_range} °C.",
    )


def _gen_data_quartiles_lower_q1_calculation(r: random.Random) -> Dict[str, Any]:
    # 7 ordered numbers: Q1 is 2nd value, Median is 4th, Q3 is 6th
    nums = sorted(random.sample(range(20, 85), 7))
    q1 = nums[1]
    q2 = nums[3]
    q3 = nums[5]
    nums_str = ", ".join(map(str, nums))

    prompt = (
        f"Consider the ordered dataset of 7 learner scores:\n"
        f"**{nums_str}**\n\n"
        f"The median (Q2) of this dataset is {q2} (the middle value at position 4).\n\n"
        f"Calculate the **Lower Quartile (Q1 / 25th percentile)** of this dataset, which is the median "
        f"of the lower half of data values lying below Q2."
    )
    ans = f"Q1 = {q1}"

    s1 = f"Identify the lower half of values below the median ({q2}): {nums[0]}, {nums[1]}, {nums[2]}. The Lower Quartile (Q1) is the middle value of this lower subset, which is {q1}."
    s2 = f"✓ [1 Mark: Method – Identifying lower half and its median]\nLower half = [{nums[0]}, {nums[1]}, {nums[2]}].\nMiddle of lower half = {q1}."
    s3 = f"✓ [1 Mark: Accuracy – Value of Lower Quartile Q1]\nQ1 = {q1}."

    return _build_question_payload(
        "data_quartiles_lower_q1_calculation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Look at the 3 numbers below the median {q2}: {nums[0]}, {nums[1]}, {nums[2]}.",
        tier_2_hint=f"The middle of these 3 numbers is {q1}.",
        tier_3_hint=f"Q1 = {q1}.",
    )


def _gen_data_quartiles_upper_q3_calculation(r: random.Random) -> Dict[str, Any]:
    nums = sorted(random.sample(range(25, 90), 7))
    q1 = nums[1]
    q2 = nums[3]
    q3 = nums[5]
    nums_str = ", ".join(map(str, nums))

    prompt = (
        f"Consider the ordered dataset of 7 examination scores:\n"
        f"**{nums_str}**\n\n"
        f"The median (Q2) of this dataset is {q2} (the middle value at position 4).\n\n"
        f"Calculate the **Upper Quartile (Q3 / 75th percentile)** of this dataset, which is the median "
        f"of the upper half of data values lying above Q2."
    )
    ans = f"Q3 = {q3}"

    s1 = f"Identify the upper half of values above the median ({q2}): {nums[4]}, {nums[5]}, {nums[6]}. The Upper Quartile (Q3) is the middle value of this upper subset, which is {q3}."
    s2 = f"✓ [1 Mark: Method – Identifying upper half and its median]\nUpper half = [{nums[4]}, {nums[5]}, {nums[6]}].\nMiddle of upper half = {q3}."
    s3 = f"✓ [1 Mark: Accuracy – Value of Upper Quartile Q3]\nQ3 = {q3}."

    return _build_question_payload(
        "data_quartiles_upper_q3_calculation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Look at the 3 numbers above the median {q2}: {nums[4]}, {nums[5]}, {nums[6]}.",
        tier_2_hint=f"The middle number of this upper half is {q3}.",
        tier_3_hint=f"Q3 = {q3}.",
    )


def _gen_data_interquartile_range_iqr_calculation(r: random.Random) -> Dict[str, Any]:
    q1 = r.randint(35, 55)
    q3 = q1 + r.randint(18, 38)
    iqr = q3 - q1

    prompt = (
        f"A statistical analysis of monthly household grocery spending yields the following quartiles:\n"
        f"• Lower Quartile (Q1) = R {q1}00\n"
        f"• Median (Q2) = R {(q1 + q3) // 2}00\n"
        f"• Upper Quartile (Q3) = R {q3}00\n\n"
        f"Formula: Interquartile Range (IQR) = Q3 − Q1\n\n"
        f"Calculate the Interquartile Range (IQR) of this dataset in Rands."
    )
    ans = f"R {iqr}00"

    s1 = f"Subtract the Lower Quartile (Q1 = R {q1}00) from the Upper Quartile (Q3 = R {q3}00)."
    s2 = f"✓ [1 Mark: Method – IQR formula substitution]\nIQR = Q3 − Q1 = R {q3}00 − R {q1}00."
    s3 = f"✓ [1 Mark: Accuracy – Final IQR value]\nIQR = R {iqr}00."

    return _build_question_payload(
        "data_interquartile_range_iqr_calculation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Subtract Q1 from Q3: R {q3}00 − R {q1}00.",
        tier_2_hint=f"IQR = R {q3}00 − R {q1}00 = R {iqr}00.",
        tier_3_hint=f"IQR = R {iqr}00.",
    )


def _gen_data_semi_interquartile_range_calculation(r: random.Random) -> Dict[str, Any]:
    q1 = r.randint(40, 60)
    iqr = r.choice([16, 20, 24, 28, 32])
    q3 = q1 + iqr
    semi_iqr = round(iqr / 2, 1)

    prompt = (
        f"The test marks of a Grade 10 class have a Lower Quartile (Q1) of {q1}% and an Upper Quartile (Q3) of {q3}%.\n\n"
        f"Formula: Semi-interquartile range = (Q3 − Q1) ÷ 2\n\n"
        f"Calculate the **semi-interquartile range** of the marks."
    )
    ans = f"{_fmt(semi_iqr)}%"

    s1 = f"First calculate the Interquartile Range (IQR = Q3 − Q1 = {q3} − {q1} = {iqr}%), then divide by 2."
    s2 = f"✓ [1 Mark: Method – Calculating IQR and halving it]\nIQR = {q3} − {q1} = {iqr}%.\nSemi-IQR = {iqr}% ÷ 2."
    s3 = f"✓ [1 Mark: Accuracy – Semi-interquartile range]\nSemi-IQR = {_fmt(semi_iqr)}%."

    return _build_question_payload(
        "data_semi_interquartile_range_calculation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the IQR first: {q3} − {q1} = {iqr}%.",
        tier_2_hint=f"Divide the IQR by 2: {iqr} ÷ 2.",
        tier_3_hint=f"Semi-IQR = {_fmt(semi_iqr)}%.",
    )


def _gen_data_outliers_impact_on_mean_vs_median(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a small bakery business, 5 employees earn the following monthly salaries:\n"
        f"R 5 000, R 5 200, R 5 500, R 5 800, and R 6 000.\n"
        f"The managing director earns a monthly salary of **R 120 000**.\n\n"
        f"1. Mean salary with director = R 24 583,33\n"
        f"2. Median salary with director = R 5 650,00\n\n"
        f"Which measure of central tendency (Mean or Median) gives a more realistic reflection of the "
        f"typical worker's monthly earnings in this bakery, and why?"
    )
    ans = "The Median — The extreme high outlier (R 120 000) severely distorts and inflates the Mean upwards, whereas the Median is robust and unaffected by extreme outliers."
    opts = [
        "The Median — The extreme high outlier (R 120 000) severely distorts and inflates the Mean upwards, whereas the Median is robust and unaffected by extreme outliers.",
        "The Mean — The Mean is always mathematically superior because it uses all data numbers.",
        "Both Mean and Median reflect the workers equally well.",
        "Neither — Only the Range can measure typical salary.",
    ]

    s1 = f"Evaluate the sensitivity of the arithmetic mean to extreme skewed outliers versus the positional stability and robustness of the median."
    s2 = f"✓ [1 Mark: Method – Explaining skewness and outlier sensitivity]\nThe extreme outlier of R 120 000 artificially pulls the mean to R 24 583, even though no worker earns anything close to that figure. The median of R 5 650 accurately represents the middle worker."
    s3 = f"✓ [1 Mark: Accuracy – Selection of median and outlier rationale]\nSelection: {ans}"

    return _build_question_payload(
        "data_outliers_impact_on_mean_vs_median",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Does any typical bakery worker earn R 24 583? No.",
        tier_2_hint="The director's massive salary distorts the mean, making the median a much fairer measure of typical earnings.",
        tier_3_hint=f"{ans}",
    )


def _gen_data_identifying_extreme_outliers(r: random.Random) -> Dict[str, Any]:
    normal_data = [r.randint(18, 26) for _ in range(7)]
    outlier = r.choice([72, 85, 95])  # Extreme high value
    data = normal_data + [outlier]
    r.shuffle(data)
    data_str = ", ".join(map(str, data))

    prompt = (
        f"A laboratory technician records the ambient daily temperature (in °C) inside a refrigerated seed vault:\n"
        f"**{data_str}**\n\n"
        f"1. Identify the **extreme outlier** in this dataset.\n"
        f"2. Explain what a statistical outlier is."
    )
    ans = f"Outlier = {outlier} °C (a data value that lies an abnormal distance away from all other values in the sample)"

    s1 = f"Identify the value that diverges drastically from the clustering pattern of all other observations ({outlier} vs range 18–26)."
    s2 = f"✓ [1 Mark: Method – Identifying extreme value far removed from data cluster]\nNormal cluster: 18 °C to 26 °C; extreme deviant point = {outlier} °C."
    s3 = f"✓ [1 Mark: Accuracy – Outlier identification and definition]\nOutlier = {outlier} °C."

    return _build_question_payload(
        "data_identifying_extreme_outliers",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Find the single number that is drastically different from all the rest.",
        tier_2_hint=f"All numbers are between 18 and 26 except {outlier}.",
        tier_3_hint=f"Outlier = {outlier} °C.",
    )


def _gen_data_comparing_spread_between_two_groups(r: random.Random) -> Dict[str, Any]:
    r_A = r.randint(10, 18)
    r_B = r.randint(35, 55)

    prompt = (
        f"Two Grade 10 classes wrote the same standardized test. Summary spread statistics are:\n"
        f"• Class 10A: Mean = 62%, Range = {r_A}%\n"
        f"• Class 10B: Mean = 62%, Range = {r_B}%\n\n"
        f"Both classes have the exact same average (62%).\n\n"
        f"Which class demonstrated greater **consistency** (less variation) in their performance, and why?"
    )
    ans = f"Class 10A is more consistent — Its smaller range ({r_A}% vs {r_B}%) indicates that learner scores are tightly clustered close to the average with less variation."
    opts = [
        f"Class 10A is more consistent — Its smaller range ({r_A}% vs {r_B}%) indicates that learner scores are tightly clustered close to the average with less variation.",
        f"Class 10B is more consistent — A larger range proves that learners have a wider range of talents.",
        "Both classes have identical consistency because their means are both 62%.",
        "Consistency cannot be determined without knowing the teacher's name.",
    ]

    s1 = f"Interpret measures of spread: a smaller range or IQR signifies greater consistency, reliability, and less variation among data values."
    s2 = f"✓ [1 Mark: Method – Linking smaller spread with greater consistency]\nSmaller range = {r_A}% (Class 10A) vs {r_B}% (Class 10B). Lower spread equals higher consistency."
    s3 = f"✓ [1 Mark: Accuracy – Selection of Class 10A and statistical justification]\nConclusion: {ans}"

    return _build_question_payload(
        "data_comparing_spread_between_two_groups",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="A smaller range means test scores are closer together, which means greater consistency.",
        tier_2_hint=f"Class 10A has a range of only {r_A}%, compared to {r_B}% for Class 10B.",
        tier_3_hint=f"{ans}",
    )
