"""Subskills 33 to 40: Five-number summaries, box-and-whisker plots, skewness, and 1.5 x IQR outlier rule."""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_pct,
)


def generate_33_five_number_summary(r: random.Random) -> Dict[str, Any]:
    """Extract the complete five-number summary (Min, Q1, Median, Q3, Max)."""
    min_v = r.choice([28, 32, 35])
    q1 = min_v + r.choice([10, 12, 14])
    med = q1 + r.choice([8, 10, 12])
    q3 = med + r.choice([10, 12, 14])
    max_v = q3 + r.choice([15, 18, 20])

    correct_ans = f"Min: {min_v}%; Q1: {q1}%; Median: {med}%; Q3: {q3}%; Max: {max_v}%"
    custom_options = [
        f"Min: {min_v}%; Q1: {q1}%; Median: {med}%; Q3: {q3}%; Max: {max_v}%",
        f"Min: {min_v}%; Q1: {q1 - 4}%; Median: {med}%; Q3: {q3 + 5}%; Max: {max_v}%",
        f"Min: {min_v + 5}%; Q1: {q1}%; Median: {med}%; Q3: {q3}%; Max: {max_v - 6}%",
        f"Min: 0%; Q1: 25%; Median: 50%; Q3: 75%; Max: 100%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A set of matric test marks has the following statistical benchmarks:\n"
        f"• Lowest mark = {min_v}%\n"
        f"• Lower quartile = {q1}%\n"
        f"• Middle mark (50th percentile) = {med}%\n"
        f"• Upper quartile = {q3}%\n"
        f"• Highest mark = {max_v}%\n\n"
        f"State the formal Five-Number Summary for this distribution."
    )
    explanation = (
        f"Step 1: The Five-Number Summary consists of: Minimum, Q1, Median, Q3, Maximum [M].\n"
        f"Step 2: Read each value in ascending order [M].\n"
        f"Step 3: Summary: Min: {min_v}%; Q1: {q1}%; Median: {med}%; Q3: {q3}%; Max: {max_v}% [A]."
    )
    return _build_question_payload(
        subskill_id="33_five_number_summary",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="List the 5 key values in order: Minimum, Q1, Median (Q2), Q3, Maximum.",
        tier_2=f"Min is {min_v}%, Q1 is {q1}%, Median is {med}%, Q3 is {q3}%, Max is {max_v}%.",
        tier_3=f"The five-number summary is Min: {min_v}%; Q1: {q1}%; Median: {med}%; Q3: {q3}%; Max: {max_v}%.",
        r=r,
    )


def generate_34_reading_box_and_whisker_plot(r: random.Random) -> Dict[str, Any]:
    """Read specific values from a box-and-whisker plot."""
    min_v = r.choice([25, 28, 30, 32, 35])
    q1 = min_v + r.choice([15, 18, 20])
    med = q1 + r.choice([10, 12, 14, 15])
    q3 = med + r.choice([10, 12, 15])
    max_v = q3 + r.choice([18, 20, 22])

    diagram_spec = {
        "diagram_role": "context",
        "kind": "box_and_whisker",
        "diagram_type": "box_and_whisker",
        "min": min_v,
        "q1": q1,
        "median": med,
        "q3": q3,
        "max": max_v,
        "label": "June Trial Exam Marks",
    }
    correct_ans = f"Whisker ends: {min_v}% and {max_v}%; Box boundaries: {q1}% and {q3}%; Vertical line inside box: {med}%"

    custom_options = [
        correct_ans,
        f"Whisker ends: {q1}% and {q3}%; Box boundaries: {min_v}% and {max_v}%; Vertical line inside box: {med}%",
        f"Whisker ends: 0% and 100%; Box boundaries: 25% and 75%; Vertical line inside box: 50%",
        f"Whisker ends: {min_v}% and {max_v}%; Box boundaries: {med}% and {q3}%; Vertical line inside box: {q1}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A box-and-whisker plot represents a distribution with 5-number summary: [{min_v}; {q1}; {med}; {q3}; {max_v}].\n\n"
        f"Describe how each of these values is visually depicted on the box-and-whisker diagram."
    )
    explanation = (
        f"Step 1: The outer ends of the two whiskers represent the Minimum ({min_v}%) and Maximum ({max_v}%) [M].\n"
        f"Step 2: The left and right edges of the central box represent Q1 ({q1}%) and Q3 ({q3}%) [M].\n"
        f"Step 3: The vertical line drawn inside the box represents the Median ({med}%) [A]."
    )
    return _build_question_payload(
        subskill_id="34_reading_box_and_whisker_plot",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Recall what each feature of a box-and-whisker plot represents.",
        tier_2="Whiskers extend to the minimum and maximum; the box spans from Q1 to Q3; the internal line is the median.",
        tier_3="Whiskers: Min/Max; Box edges: Q1/Q3; Inside line: Median.",
        diagram_spec=diagram_spec,
        r=r,
    )


def generate_35_positively_skewed_distribution(r: random.Random) -> Dict[str, Any]:
    """Identify positive (right) skewness from box-and-whisker plot dimensions."""
    q1 = 40
    med = 45  # median is closer to Q1
    q3 = 68  # long right half
    min_v = 35
    max_v = 95  # long right whisker

    correct_ans = "Positively skewed (skewed to the right): The right whisker and upper box half (Q3 - Median) are much longer, and Mean > Median"
    custom_options = [
        correct_ans,
        "Negatively skewed (skewed to the left): The majority of learners scored above 80%",
        "Symmetrical: The median is at the exact center of the box",
        "Normal distribution: The whiskers are identical in length to the nearest millimeter",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A box-and-whisker plot displays the following values: Min = {min_v}%, Q1 = {q1}%, Median = {med}%, "
        f"Q3 = {q3}%, Max = {max_v}%.\n"
        f"Note that Median - Q1 = {med - q1}%, whereas Q3 - Median = {q3 - med}%.\n\n"
        f"Determine the skewness of this distribution and provide mathematical justification."
    )
    explanation = (
        f"Step 1: Calculate left box length: Median - Q1 = {med} - {q1} = {med - q1}% [M].\n"
        f"Step 2: Calculate right box length: Q3 - Median = {q3} - {med} = {q3 - med}% [M].\n"
        f"Step 3: Since Q3 - Median ({q3 - med}%) > Median - Q1 ({med - q1}%), the data is stretched out to the right (positively skewed) [A]."
    )
    return _build_question_payload(
        subskill_id="35_positively_skewed_distribution",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Compare the distance from Q1 to Median with the distance from Median to Q3.",
        tier_2=f"Q3 - Median is {q3 - med}%, which is much larger than Median - Q1 ({med - q1}%).",
        tier_3="A longer right side means the distribution is positively skewed (skewed to the right).",
        r=r,
    )


def generate_36_negatively_skewed_distribution(r: random.Random) -> Dict[str, Any]:
    """Identify negative (left) skewness from box-and-whisker plot dimensions."""
    min_v = 20
    q1 = 55
    med = 72
    q3 = 78
    max_v = 85

    correct_ans = "Negatively skewed (skewed to the left): The left whisker and lower box half (Median - Q1) are much longer, and Mean < Median"
    custom_options = [
        correct_ans,
        "Positively skewed (skewed to the right): Most learners performed below the pass mark",
        "Symmetrical: The distance from minimum to median equals median to maximum",
        "Bimodal: The data has two separate peaks on the left whisker",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A box-and-whisker plot of matric test scores shows:\n"
        f"Min = {min_v}%, Q1 = {q1}%, Median = {med}%, Q3 = {q3}%, Max = {max_v}%.\n"
        f"Here, Median - Q1 = {med - q1}%, whereas Q3 - Median = {q3 - med}%.\n\n"
        f"State whether this distribution is symmetrical, positively skewed, or negatively skewed, with reasons."
    )
    explanation = (
        f"Step 1: Compare the halves of the box: Median - Q1 = {med - q1}% vs Q3 - Median = {q3 - med}% [M].\n"
        f"Step 2: The lower half and lower whisker (length {q1 - min_v}%) are much more spread out than the upper half [M].\n"
        f"Step 3: This distribution is negatively skewed (skewed to the left) [A]."
    )
    return _build_question_payload(
        subskill_id="36_negatively_skewed_distribution",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look at which side of the box and whisker is longer and more stretched out.",
        tier_2=f"Median - Q1 ({med - q1}%) is much larger than Q3 - Median ({q3 - med}%).",
        tier_3="A longer tail/whisker to the left indicates negative skewness.",
        r=r,
    )


def generate_37_symmetrical_distribution(r: random.Random) -> Dict[str, Any]:
    """Recognize a symmetrical distribution in a box plot."""
    min_v = 30
    q1 = 50
    med = 65
    q3 = 80
    max_v = 100

    correct_ans = "Symmetrical: Median is centered in the box (Q3 - Median = Median - Q1 = 15%), and whiskers are equal in length (20%)"
    custom_options = [
        correct_ans,
        "Positively skewed: All scores are clustered above 50%",
        "Negatively skewed: The maximum score is 100%",
        "Non-symmetrical: A difference of 15% indicates significant skewness",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A box-and-whisker plot displays: Min = {min_v}%, Q1 = {q1}%, Median = {med}%, Q3 = {q3}%, Max = {max_v}%.\n\n"
        f"Classify the symmetry or skewness of this dataset with mathematical reasoning."
    )
    explanation = (
        f"Step 1: Check whisker lengths: Q1 - Min = {q1 - min_v}% and Max - Q3 = {max_v - q3}% (both equal 20%) [M].\n"
        f"Step 2: Check box halves: Median - Q1 = {med - q1}% and Q3 - Median = {q3 - med}% (both equal 15%) [M].\n"
        f"Step 3: Because both sides are balanced, the distribution is symmetrical [A]."
    )
    return _build_question_payload(
        subskill_id="37_symmetrical_distribution",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the distance of both whiskers and both box sections.",
        tier_2="Notice that Median - Q1 = 15% and Q3 - Median = 15%, while both whiskers are 20%.",
        tier_3="Since both sides are balanced, the distribution is symmetrical.",
        r=r,
    )


def generate_38_outlier_detection_1_5_iqr(r: random.Random) -> Dict[str, Any]:
    """Apply the 1.5 x IQR rule to identify mathematical outliers."""
    q1 = r.choice([40, 44, 48])
    iqr = r.choice([16, 20, 24])
    q3 = q1 + iqr

    fence_lower = q1 - 1.5 * iqr
    fence_upper = q3 + 1.5 * iqr

    test_val = int(round(fence_upper + r.choice([4, 8, 12])))
    correct_ans = f"Upper fence = {_fmt(fence_upper, 1)}%; Since {test_val}% > {_fmt(fence_upper, 1)}%, it is a mathematical outlier"

    custom_options = [
        correct_ans,
        f"Upper fence = {_fmt(fence_upper + 10, 1)}%; {test_val}% is within normal limits",
        f"Lower fence = {_fmt(fence_lower, 1)}%; {test_val}% is an outlier because it exceeds the median",
        f"Outliers are defined strictly as marks above 95%, regardless of IQR",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A set of examination scores has Q1 = {q1}% and Q3 = {q3}% (IQR = {iqr}%).\n"
        f"One extraordinary learner achieved a mark of {test_val}%.\n\n"
        f"Use the 1,5 × IQR outlier detection rule to determine whether {test_val}% is statistically classified as an outlier."
    )
    explanation = (
        f"Step 1: Calculate 1,5 × IQR = 1,5 × {iqr}% = {_fmt(1.5 * iqr, 1)}% [M].\n"
        f"Step 2: Calculate upper boundary (fence) = Q3 + (1,5 × IQR) = {q3}% + {_fmt(1.5 * iqr, 1)}% = {_fmt(fence_upper, 1)}% [M].\n"
        f"Step 3: Since {test_val}% > {_fmt(fence_upper, 1)}%, {test_val}% is a confirmed outlier [A]."
    )
    return _build_question_payload(
        subskill_id="38_outlier_detection_1_5_iqr",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the upper fence using the formula: Upper Fence = Q3 + (1,5 × IQR).",
        tier_2=f"1,5 × {iqr} = {_fmt(1.5 * iqr, 1)}. Add this to Q3 ({q3}%): {_fmt(fence_upper, 1)}%.",
        tier_3=f"Since {test_val}% exceeds {_fmt(fence_upper, 1)}%, it is an outlier.",
        r=r,
    )


def generate_39_comparing_two_boxplots(r: random.Random) -> Dict[str, Any]:
    """Compare consistency and performance between two classes using boxplots."""
    correct_ans = "Class 2 is more consistent because its IQR is much smaller (11% vs 24%), while Class 1 has more high-achieving learners"

    custom_options = [
        correct_ans,
        "Class 1 is more consistent because its maximum score is 98%",
        "Both classes performed identically because both ranges exceed 30%",
        "Class 2 is worse in all respects because its median is lower than Class 1's Q1",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Two Grade 12 classes have the following five-number summaries:\n"
        f"• Class 1: [28%; 44%; 58%; 68%; 98%] (IQR = 24%, Range = 70%)\n"
        f"• Class 2: [48%; 54%; 60%; 65%; 79%] (IQR = 11%, Range = 31%)\n\n"
        f"Compare the consistency and spread of performance between the two classes."
    )
    explanation = (
        f"Step 1: Compare IQR: Class 2's IQR is 11% compared to Class 1's 24% [M].\n"
        f"Step 2: A smaller IQR indicates that the middle 50% of learners are clustered much closer together (more consistent) [M].\n"
        f"Step 3: Class 1 has higher spread and reaches higher top marks (98%), but Class 2 is more consistent [A]."
    )
    return _build_question_payload(
        subskill_id="39_comparing_two_boxplots",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look at the Interquartile Range (IQR) of both classes to evaluate consistency.",
        tier_2="Class 2 has an IQR of only 11% compared to 24% for Class 1.",
        tier_3="A smaller IQR means higher consistency among learners.",
        r=r,
    )


def generate_40_outlier_removal_impact(r: random.Random) -> Dict[str, Any]:
    """Analyze the impact of removing an outlier on the five-number summary and range."""
    correct_ans = "The maximum and range decrease dramatically, while Q1, median, and Q3 remain virtually unchanged"

    custom_options = [
        correct_ans,
        "The median drops to zero because one piece of data was discarded",
        "The IQR doubles because the dataset has fewer learners",
        "All five values in the five-number summary decrease by 50%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A dataset of 25 marks contains a severe outlier: a maximum mark of 99% when the second highest mark is only 74%.\n"
        f"If the teacher decides to treat 99% as an anomaly and removes it from the dataset:\n\n"
        f"Describe how removing this outlier will affect the Five-Number Summary and the Range."
    )
    explanation = (
        f"Step 1: The maximum immediately drops from 99% to 74%, reducing the range drastically [M].\n"
        f"Step 2: The median and quartiles depend on relative rank order in the middle and shift marginally by at most one position [M].\n"
        f"Step 3: Conclusion: Maximum and range decrease dramatically; quartiles and median remain stable [A]."
    )
    return _build_question_payload(
        subskill_id="40_outlier_removal_impact",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Consider which values in the five-number summary depend directly on the extreme edge.",
        tier_2="Only the maximum value and the overall range are dictated by the extreme upper value.",
        tier_3="The median and quartiles are resistant to edge changes.",
        r=r,
    )
