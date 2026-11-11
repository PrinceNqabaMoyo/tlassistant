"""Subskills 17 to 24: Measures of central tendency, weighted means, outlier distortion, and comparisons."""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_pct,
)


def generate_17_weighted_combined_mean(r: random.Random) -> Dict[str, Any]:
    """Calculate the combined (weighted) mean of two unequal classes."""
    n1 = r.choice([25, 30, 32])
    mean1 = r.choice([58.0, 62.0, 65.0])
    n2 = r.choice([18, 20, 22])
    mean2 = r.choice([52.0, 54.0, 56.0])

    tot1 = n1 * mean1
    tot2 = n2 * mean2
    combined_mean = (tot1 + tot2) / (n1 + n2)
    correct_ans = f"{_fmt(combined_mean, 2)}%"

    unweighted = (mean1 + mean2) / 2
    custom_options = [
        f"{_fmt(combined_mean, 2)}%",
        f"{_fmt(unweighted, 2)}%",
        f"{_fmt(combined_mean + 3.5, 2)}%",
        f"{_fmt(combined_mean - 4.2, 2)}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a high school in Gauteng, two Grade 12 Mathematical Literacy classes wrote the same Term 2 test:\n"
        f"• Class 12A ({n1} learners) achieved a mean mark of {_fmt(mean1, 1)}%.\n"
        f"• Class 12B ({n2} learners) achieved a mean mark of {_fmt(mean2, 1)}%.\n\n"
        f"Calculate the overall combined mean percentage mark for both classes together."
    )
    explanation = (
        f"Step 1: Calculate total marks for Class 12A: {n1} × {_fmt(mean1, 1)} = {_fmt(tot1, 1)} [M].\n"
        f"Step 2: Calculate total marks for Class 12B: {n2} × {_fmt(mean2, 1)} = {_fmt(tot2, 1)} [M].\n"
        f"Step 3: Combined Mean = ({_fmt(tot1, 1)} + {_fmt(tot2, 1)}) ÷ ({n1} + {n2}) = {_fmt(combined_mean, 2)}% [A]."
    )
    return _build_question_payload(
        subskill_id="17_weighted_combined_mean",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Do not simply average the two percentages because the class sizes are unequal.",
        tier_2=f"Find the total sum of marks: ({n1} × {_fmt(mean1, 1)}) + ({n2} × {_fmt(mean2, 1)}), then divide by {n1 + n2}.",
        tier_3=f"The combined weighted mean is {_fmt(combined_mean, 2)}%.",
        r=r,
    )


def generate_18_calculating_median_odd_even(r: random.Random) -> Dict[str, Any]:
    """Accurately determine the median in an ordered dataset of even length."""
    # 10 or 12 numbers
    length = r.choice([10, 12])
    base = r.randint(45, 60)
    data = sorted([base + r.randint(-15, 25) for _ in range(length)])
    mid1 = data[length // 2 - 1]
    mid2 = data[length // 2]
    median = (mid1 + mid2) / 2
    correct_ans = f"Median = {_fmt(median, 1)}"

    custom_options = [
        f"Median = {_fmt(median, 1)}",
        f"Median = {_fmt(mid1, 1)}",
        f"Median = {_fmt(mid2, 1)}",
        f"Median = {_fmt((data[0] + data[-1]) / 2, 1)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    data_str = "  ".join(str(x) for x in data)
    prompt = (
        f"Consider the following ordered marks achieved by {length} learners in an assignment:\n"
        f"**{data_str}**\n\n"
        f"Calculate the median mark for this dataset."
    )
    explanation = (
        f"Step 1: Since the dataset has an even number of values (n = {length}), the median is the average of the two middle values [M].\n"
        f"Step 2: The two middle values at positions {length//2} and {length//2 + 1} are {mid1} and {mid2} [M].\n"
        f"Step 3: Median = ({mid1} + {mid2}) ÷ 2 = {_fmt(median, 1)} [A]."
    )
    return _build_question_payload(
        subskill_id="18_calculating_median_odd_even",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="For an even number of items, locate the two middle values and calculate their average.",
        tier_2=f"The two middle values are {mid1} and {mid2}.",
        tier_3=f"({mid1} + {mid2}) ÷ 2 = {_fmt(median, 1)}.",
        r=r,
    )


def generate_19_bimodal_multimodal_datasets(r: random.Random) -> Dict[str, Any]:
    """Identify bimodal distributions and evaluate modal usefulness."""
    val1 = r.choice([52, 55, 58])
    val2 = r.choice([68, 72, 75])
    correct_ans = f"Bimodal with modes {val1}% and {val2}%; mode is of limited analytical value for continuous numerical marks"

    custom_options = [
        correct_ans,
        f"Unimodal with single mode {int((val1 + val2)/2)}%; mode is the most representative measure",
        f"No mode exists because every frequency in continuous data is random",
        f"Trimodal with modes {val1}%, {val2}%, and 100%; mode represents the highest peak",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a test analysis, both {val1}% and {val2}% appear with the highest equal frequency of 5 times each, "
        f"while all other scores appear fewer times.\n\n"
        f"Identify the modal characteristics of this dataset and state its usefulness in evaluating overall class ability."
    )
    explanation = (
        f"Step 1: When two values share the highest frequency, the dataset is bimodal [M].\n"
        f"Step 2: For continuous examination marks, the mode indicates popularity of specific scores but fails to reflect central tendency [M].\n"
        f"Step 3: Conclusion: Bimodal with modes {val1}% and {val2}%; mode has limited value [A]."
    )
    return _build_question_payload(
        subskill_id="19_bimodal_multimodal_datasets",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine whether there is one, two, or zero numbers with the highest frequency.",
        tier_2="When two numbers share the top frequency, the dataset is bimodal.",
        tier_3="The mode only tells which individual scores appeared most often, not the central balance of the entire group.",
        r=r,
    )


def generate_20_outlier_impact_mean_vs_median(r: random.Random) -> Dict[str, Any]:
    """Calculate the drastic shift in mean caused by an extreme outlier while median remains unaffected."""
    base_scores = [45, 48, 50, 52, 54, 55, 58, 60, 62]
    orig_mean = sum(base_scores) / len(base_scores)
    orig_median = base_scores[len(base_scores) // 2]

    outlier = r.choice([98, 100, 120])
    new_scores = base_scores + [outlier]
    new_mean = sum(new_scores) / len(new_scores)

    diff_mean = new_mean - orig_mean
    correct_ans = f"Mean increases by {_fmt(diff_mean, 1)}% (from {_fmt(orig_mean, 1)}% to {_fmt(new_mean, 1)}%); median remains virtually stable"

    custom_options = [
        correct_ans,
        f"Both mean and median increase equally by {_fmt(diff_mean, 1)}%",
        f"Median increases by {outlier - orig_median}% while mean remains unchanged",
        f"Mean decreases because the sample size increased from 9 to 10",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A group of 9 learners achieved the following test scores:\n"
        f"45, 48, 50, 52, 54, 55, 58, 60, 62 (Mean = {_fmt(orig_mean, 1)}%, Median = {orig_median}%).\n\n"
        f"A 10th learner with a remarkable score of {outlier}% is added to the dataset.\n"
        f"Calculate the new mean and describe how this extreme outlier affects the mean versus the median."
    )
    explanation = (
        f"Step 1: Calculate new total = {sum(base_scores)} + {outlier} = {sum(new_scores)} [M].\n"
        f"Step 2: New Mean = {sum(new_scores)} ÷ 10 = {_fmt(new_mean, 1)}% (increase of {_fmt(diff_mean, 1)}%) [M].\n"
        f"Step 3: The median only shifts between 54 and 55 ({54.5}%), proving that the mean is sensitive to outliers while the median is resistant [A]."
    )
    return _build_question_payload(
        subskill_id="20_outlier_impact_mean_vs_median",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Recalculate the mean by adding the outlier to the total and dividing by 10.",
        tier_2=f"Old total = {sum(base_scores)}, new total = {sum(new_scores)}. New mean = {_fmt(new_mean, 1)}%.",
        tier_3=f"The mean increases significantly by {_fmt(diff_mean, 1)}%, while the median is barely changed.",
        r=r,
    )


def generate_21_selecting_appropriate_central_tendency(r: random.Random) -> Dict[str, Any]:
    """Select between mean, median, and mode for skewed real-estate or income distributions."""
    suburb = r.choice(["Dawnview", "Cicily", "Sandton", "Khayelitsha"])
    correct_ans = "The median: It is not distorted by extreme high-value luxury sales and represents the typical middle property"

    custom_options = [
        correct_ans,
        "The mean: It takes every property sale into account and is preferred by commercial estate agents",
        "The mode: It reflects the exact price that buyers agreed on most frequently",
        "The midrange: It simply averages the lowest and highest sales prices",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A property analyst reports the following house prices sold in {suburb} during the past 6 months:\n"
        f"• R 300 000; R 320 000; R 340 000; R 350 000; R 360 000; R 380 000; R 400 000; R 1 850 000.\n"
        f"The mean house price is R 537 500, while the median house price is R 355 000.\n\n"
        f"Explain which measure of central tendency provides the most realistic representation of the typical house price."
    )
    explanation = (
        f"Step 1: Notice the extreme outlier of R 1 850 000 which inflates the mean to R 537 500 (higher than 7 out of 8 homes) [M].\n"
        f"Step 2: The median at R 355 000 divides the data in half without being influenced by the single extreme value [M].\n"
        f"Step 3: The median is the most appropriate measure [A]."
    )
    return _build_question_payload(
        subskill_id="21_selecting_appropriate_central_tendency",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look at whether most house prices are close to R 355 000 or R 537 500.",
        tier_2="Notice that 7 of the 8 homes sold for R 400 000 or less, meaning the mean of R 537 500 is artificially skewed.",
        tier_3="The median is the most accurate indicator of typical house prices because it resists outlier distortion.",
        r=r,
    )


def generate_22_missing_value_from_target_mean(r: random.Random) -> Dict[str, Any]:
    """Solve for the missing test score required to achieve a desired overall mean."""
    target_mean = r.choice([65, 70, 72, 75])
    n = 5
    scores = [r.randint(target_mean - 15, target_mean + 10) for _ in range(n - 1)]
    needed = target_mean * n - sum(scores)
    # Ensure realistic score between 40 and 100
    if needed < 40 or needed > 100:
        needed = target_mean + 5
        scores[-1] = target_mean * n - sum(scores[:-1]) - needed

    correct_ans = f"{needed}%"
    custom_options = [
        f"{needed}%",
        f"{needed + 6}%",
        f"{max(0, needed - 8)}%",
        f"{target_mean}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    scores_str = ", ".join(f"{s}%" for s in scores)
    prompt = (
        f"A Grade 12 learner has written 4 out of 5 Mathematical Literacy assessments this term, achieving:\n"
        f"{scores_str}.\n\n"
        f"Calculate the mark the learner must score in the 5th assessment to achieve an overall term mean of {target_mean}%."
    )
    explanation = (
        f"Step 1: Total marks required for 5 tests = 5 × {target_mean}% = {5 * target_mean}% [M].\n"
        f"Step 2: Total scored so far = {sum(scores)}% [M].\n"
        f"Step 3: Required mark = {5 * target_mean}% - {sum(scores)}% = {needed}% [A]."
    )
    return _build_question_payload(
        subskill_id="22_missing_value_from_target_mean",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the total marks required by multiplying the target mean by 5.",
        tier_2=f"Total required = 5 × {target_mean} = {5 * target_mean}%. Add up the 4 known scores ({sum(scores)}%).",
        tier_3=f"Subtract the sum of known scores from the total required: {needed}%.",
        r=r,
    )


def generate_23_comparing_groups_equal_median(r: random.Random) -> Dict[str, Any]:
    """Compare two groups that have identical medians but different means and distributions."""
    median = 59
    mean_a = 59.3
    mean_b = 60.5
    correct_ans = "Both groups have equal median (59%); Group B performed slightly better on average (mean 60,5% vs 59,3%) and is more consistent"

    custom_options = [
        correct_ans,
        "Group A performed substantially better because their mean is lower than their median",
        "It is impossible to compare the two groups because the medians are identical",
        "Group B is worse because higher means indicate excessive spread in marks",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Two Grade 12 classes achieved the following statistical summary in their June examination:\n"
        f"• Class A: Mean = {_fmt(mean_a, 1)}%; Median = {median}%; Mode = 63%\n"
        f"• Class B: Mean = {_fmt(mean_b, 1)}%; Median = {median}%; Mode = 54%\n\n"
        f"Compare the performance of the two classes based on their measures of central tendency."
    )
    explanation = (
        f"Step 1: Note that both classes share the identical median of {median}% [M].\n"
        f"Step 2: Class B has a slightly higher mean ({_fmt(mean_b, 1)}% vs {_fmt(mean_a, 1)}%) showing marginally stronger overall average [M].\n"
        f"Step 3: Correct comparison confirms equal medians with Class B slightly ahead on mean [A]."
    )
    return _build_question_payload(
        subskill_id="23_comparing_groups_equal_median",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Examine both the median and the mean for each class.",
        tier_2="Notice that the median is identical, so the mean provides the differentiating insight.",
        tier_3="Class B has a marginally higher mean, indicating slightly better aggregate performance.",
        r=r,
    )


def generate_24_linear_transformation_central_tendency(r: random.Random) -> Dict[str, Any]:
    """Determine changes to mean and median when all scores receive an adjustment."""
    old_mean = r.choice([54.0, 58.0, 62.0])
    old_median = r.choice([52.0, 56.0, 60.0])
    adjustment = r.choice([5, 8, 10])

    new_mean = old_mean + adjustment
    new_median = old_median + adjustment
    correct_ans = f"New Mean = {_fmt(new_mean, 1)}%; New Median = {_fmt(new_median, 1)}%"

    custom_options = [
        f"New Mean = {_fmt(new_mean, 1)}%; New Median = {_fmt(new_median, 1)}%",
        f"New Mean = {_fmt(new_mean, 1)}%; New Median = {_fmt(old_median, 1)}%",
        f"New Mean = {_fmt(old_mean, 1)}%; New Median = {_fmt(new_median, 1)}%",
        f"New Mean = {_fmt(old_mean + adjustment/2, 1)}%; New Median = {_fmt(new_median + 2, 1)}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"After remarking a challenging trial exam paper, the Department of Education decides to add a compensatory "
        f"{adjustment}% to every single learner's mark.\n"
        f"Prior to the adjustment, the class mean was {_fmt(old_mean, 1)}% and the median was {_fmt(old_median, 1)}%.\n\n"
        f"Determine the new mean and median for the class."
    )
    explanation = (
        f"Step 1: Adding a constant k to every data value increases the mean by k: {_fmt(old_mean, 1)}% + {adjustment}% = {_fmt(new_mean, 1)}% [M].\n"
        f"Step 2: Adding a constant k shifts all positions equally, increasing the median by k: {_fmt(old_median, 1)}% + {adjustment}% = {_fmt(new_median, 1)}% [M].\n"
        f"Step 3: New Mean = {_fmt(new_mean, 1)}% and New Median = {_fmt(new_median, 1)}% [A]."
    )
    return _build_question_payload(
        subskill_id="24_linear_transformation_central_tendency",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="When a constant number is added to every value in a dataset, both the mean and median increase by that exact amount.",
        tier_2=f"Add {adjustment}% to the old mean ({_fmt(old_mean, 1)}%) and to the old median ({_fmt(old_median, 1)}%).",
        tier_3=f"New Mean = {_fmt(new_mean, 1)}%, New Median = {_fmt(new_median, 1)}%.",
        r=r,
    )
