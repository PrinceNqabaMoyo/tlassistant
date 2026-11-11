"""Subskills 10 to 18: Frequency Tables, Grouped Intervals, Relative/Cumulative Frequency & Two-Way Tables for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: Frequency table construction and total sample count N = sum(f)."""
    name = r.choice(SA_NAMES)
    categories = ["Walking", "Minibus Taxi", "Bicycle", "Bus", "Private Car"]
    counts = [r.choice([12, 15, 18]), r.choice([25, 30, 35]), r.choice([4, 6, 8]), r.choice([16, 20, 22]), r.choice([8, 10, 12])]
    total_n = sum(counts)

    table_rows = "\n".join([f"| {cat} | {cnt} |" for cat, cnt in zip(categories, counts)])
    prompt = (
        f"{name} conducted a survey on modes of transport used by learners to travel to school:\n\n"
        f"| Mode of Transport | Frequency (Learners) |\n"
        f"| :--- | :--- |\n"
        f"{table_rows}\n\n"
        f"How many total learners were surveyed altogether?"
    )

    correct_ans = f"{total_n} learners"
    wrong_1 = f"{total_n + 10} learners"
    wrong_2 = f"{total_n - 5} learners"
    wrong_3 = f"{total_n * 2} learners"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Sum the frequencies for all categories [1 mark].\n"
        f"Total N = {' + '.join(str(c) for c in counts)} [1 mark].\n"
        f"Step 2: Calculate sum [1 mark].\n"
        f"Total N = {total_n} learners.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="10",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add up all the numbers in the frequency column to find the total sample size.",
        tier_2=f"Sum: {' + '.join(str(c) for c in counts)}.",
        tier_3=f"Total = {total_n} learners.",
        r=r,
    )


def generate_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Subskill 11: Identify class limits, midpoint, and class width of a grouped interval."""
    low = r.choice([20, 30, 40, 50, 60])
    width = r.choice([10, 15, 20])
    high = low + width
    interval_str = f"{low} ≤ x < {high}"
    midpoint = (low + high) / 2

    prompt = (
        f"In a grouped frequency table of test scores, one class interval is given as:\n"
        f"**{interval_str}**\n"
        f"What are the lower class boundary, upper class boundary, and class midpoint for this interval?"
    )

    correct_ans = f"Lower: {_fmt(low)}, Upper: {_fmt(high)}, Midpoint: {_fmt(midpoint)}"
    wrong_1 = f"Lower: {_fmt(low + 1)}, Upper: {_fmt(high - 1)}, Midpoint: {_fmt(midpoint)}"
    wrong_2 = f"Lower: {_fmt(low)}, Upper: {_fmt(high)}, Midpoint: {_fmt(width)}"
    wrong_3 = f"Lower: {_fmt(high)}, Upper: {_fmt(low)}, Midpoint: {_fmt(midpoint * 2)}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify lower and upper class limits [1 mark].\n"
        f"Lower limit = {low}; Upper limit = {high}.\n"
        f"Step 2: Calculate class midpoint [1 mark].\n"
        f"Midpoint = (Lower + Upper) ÷ 2 = ({low} + {high}) ÷ 2 = {low + high} ÷ 2 = {_fmt(midpoint)}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="11",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The lower limit is the starting value; the upper limit is the ending value. The midpoint is their average.",
        tier_2=f"Lower = {low}, Upper = {high}. Midpoint = ({low} + {high}) ÷ 2 = {_fmt(midpoint)}.",
        tier_3=f"Result: {correct_ans}.",
        r=r,
    )


def generate_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Subskill 12: Determine the modal class interval from a grouped frequency table."""
    intervals = ["40 ≤ x < 50", "50 ≤ x < 60", "60 ≤ x < 70", "70 ≤ x < 80", "80 ≤ x < 90"]
    freqs = [6, 14, 25, 18, 7]
    r.shuffle(freqs)
    # Ensure one strictly highest frequency
    max_idx = freqs.index(max(freqs))
    modal_interval = intervals[max_idx]
    max_freq = freqs[max_idx]

    table_rows = "\n".join([f"| {inter} | {f} |" for inter, f in zip(intervals, freqs)])
    prompt = (
        f"Consider the following grouped frequency distribution for a Mathematics test:\n\n"
        f"| Test Mark Interval (%) | Frequency (Number of Learners) |\n"
        f"| :--- | :--- |\n"
        f"{table_rows}\n\n"
        f"What is the modal class interval for this data set?"
    )

    correct_ans = modal_interval
    options, _ = _build_options(correct_ans, r, custom_options=intervals[:4])

    explanation = (
        f"Step 1: Identify the highest frequency in the table [1 mark].\n"
        f"The maximum frequency is {max_freq}.\n"
        f"Step 2: Read the corresponding class interval [1 mark].\n"
        f"The interval with frequency {max_freq} is {modal_interval}.\n"
        f"Step 3: Stated modal class [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="12",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The modal class is the interval that has the highest frequency count.",
        tier_2=f"The highest frequency is {max_freq}, which belongs to the interval {modal_interval}.",
        tier_3=f"Modal class: {modal_interval}.",
        r=r,
    )


def generate_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Estimate the mean from a grouped frequency table using class midpoints."""
    # 3 intervals for clean hand calculation
    # Interval 1: 10 - 20 (midpoint 15), f1
    # Interval 2: 20 - 30 (midpoint 25), f2
    # Interval 3: 30 - 40 (midpoint 35), f3
    f1 = r.choice([4, 5, 6])
    f2 = r.choice([8, 10, 12])
    f3 = r.choice([4, 5, 6])

    m1, m2, m3 = 15, 25, 35
    total_fm = f1 * m1 + f2 * m2 + f3 * m3
    total_f = f1 + f2 + f3
    mean_est = round(total_fm / total_f, 1)

    prompt = (
        f"A survey recorded the daily commute times of factory workers in minutes:\n\n"
        f"| Commute Time Interval (min) | Midpoint (m) | Frequency (f) |\n"
        f"| :--- | :--- | :--- |\n"
        f"| 10 ≤ t < 20 | 15 | {f1} |\n"
        f"| 20 ≤ t < 30 | 25 | {f2} |\n"
        f"| 30 ≤ t < 40 | 35 | {f3} |\n\n"
        f"Using the formula Estimated Mean = Σ(f × m) ÷ Σf, calculate the estimated mean commute time in minutes."
    )

    correct_ans = f"{_fmt(mean_est, 1)} minutes"
    wrong_1 = f"{_fmt(mean_est + 4.0, 1)} minutes"
    wrong_2 = f"{_fmt(mean_est - 3.5, 1)} minutes"
    wrong_3 = f"{_fmt((m1 + m2 + m3) / 3, 1)} minutes"  # unweighted mean
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate (f × m) for each interval [1 mark].\n"
        f"Row 1: {f1} × 15 = {f1 * 15}.\n"
        f"Row 2: {f2} × 25 = {f2 * 25}.\n"
        f"Row 3: {f3} × 35 = {f3 * 35}.\n"
        f"Step 2: Sum products and sum frequencies [1 mark].\n"
        f"Σ(f × m) = {f1 * 15} + {f2 * 25} + {f3 * 35} = {total_fm}.\n"
        f"Σf = {f1} + {f2} + {f3} = {total_f}.\n"
        f"Step 3: Divide to calculate mean [1 mark].\n"
        f"Estimated Mean = {total_fm} ÷ {total_f} = {_fmt(mean_est, 1)} minutes ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="13",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply each midpoint by its frequency, sum those products, and divide by the total frequency.",
        tier_2=f"Σ(f × m) = {total_fm}; Σf = {total_f}.",
        tier_3=f"{total_fm} ÷ {total_f} = {_fmt(mean_est, 1)} minutes.",
        r=r,
    )


def generate_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Subskill 14: Calculate relative frequency as a fraction or decimal."""
    name = r.choice(SA_NAMES)
    total_n = r.choice([20, 25, 40, 50, 100])
    category_f = r.choice([4, 5, 8, 10, 12, 15])
    # Ensure category_f < total_n
    category_f = min(category_f, total_n // 2)

    rel_freq = round(category_f / total_n, 2)

    prompt = (
        f"In a sample of {_fmt(total_n)} patients visiting a community clinic, exactly {_fmt(category_f)} "
        f"were diagnosed with seasonal influenza.\n"
        f"Calculate the relative frequency of influenza diagnoses in this sample (expressed as a decimal)."
    )

    correct_ans = f"{_fmt(rel_freq)}"
    wrong_1 = f"{_fmt(rel_freq * 10)}"
    wrong_2 = f"{_fmt(rel_freq * 0.1)}"
    wrong_3 = f"{_fmt(round(category_f / (total_n + 10), 2))}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State the relative frequency formula [1 mark].\n"
        f"\\text{{Relative Frequency}} = \\frac{{\\text{{Category Frequency}}}}{{\\text{{Total Sample Size}}}} = \\frac{{{category_f}}}{{{total_n}}}.\n"
        f"Step 2: Convert to decimal [1 mark].\n"
        f"{category_f} ÷ {total_n} = {_fmt(rel_freq)}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="14",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Relative Frequency = Frequency ÷ Total.",
        tier_2=f"Divide {category_f} by {total_n}.",
        tier_3=f"{category_f} ÷ {total_n} = {_fmt(rel_freq)}.",
        r=r,
    )


def generate_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Subskill 15: Calculate percentage frequency: (f / N) * 100%."""
    name = r.choice(SA_NAMES)
    total_n = r.choice([40, 50, 80, 120, 200])
    cat_f = r.choice([12, 15, 18, 24, 30])
    pct = round((cat_f / total_n) * 100, 1)

    prompt = (
        f"Out of a total of {_fmt(total_n)} consumers surveyed at a retail mall, {_fmt(cat_f)} "
        f"indicated that they pay using contactless mobile smartphone apps.\n"
        f"What percentage frequency of consumers use mobile smartphone payments?"
    )

    correct_ans = f"{_fmt(pct, 1)}%"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Formulate percentage calculation [1 mark].\n"
        f"\\text{{Percentage}} = \\left( \\frac{{{cat_f}}}{{{total_n}}} \\right) \\times 100\\%.\n"
        f"Step 2: Perform division and multiplication [1 mark].\n"
        f"({cat_f} ÷ {total_n}) × 100% = {_fmt(pct, 1)}%.\n"
        f"Step 3: Stated percentage [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="15",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Percentage Frequency = (Frequency ÷ Total) × 100%.",
        tier_2=f"Divide {cat_f} by {total_n} and multiply by 100.",
        tier_3=f"Result = {_fmt(pct, 1)}%.",
        r=r,
    )


def generate_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Subskill 16: Construct cumulative frequency and answer threshold question."""
    intervals = ["0 ≤ x < 20", "20 ≤ x < 40", "40 ≤ x < 60", "60 ≤ x < 80", "80 ≤ x ≤ 100"]
    f1, f2, f3, f4, f5 = 4, 8, 15, 18, 5
    cum_f = [f1, f1 + f2, f1 + f2 + f3, f1 + f2 + f3 + f4, f1 + f2 + f3 + f4 + f5]

    target_thresh = 60
    # Number of learners who scored less than 60% = f1 + f2 + f3
    ans_count = cum_f[2]

    prompt = (
        f"A teacher compiles the following test score distribution for a class:\n\n"
        f"| Test Mark Interval (%) | Frequency (f) |\n"
        f"| :--- | :--- |\n"
        f"| 0 ≤ x < 20 | {f1} |\n"
        f"| 20 ≤ x < 40 | {f2} |\n"
        f"| 40 ≤ x < 60 | {f3} |\n"
        f"| 60 ≤ x < 80 | {f4} |\n"
        f"| 80 ≤ x ≤ 100 | {f5} |\n\n"
        f"Using cumulative frequencies, how many learners scored LESS THAN 60% in this test?"
    )

    correct_ans = f"{ans_count} learners"
    wrong_1 = f"{f3} learners"  # only that single interval
    wrong_2 = f"{cum_f[3]} learners"  # included 60-80
    wrong_3 = f"{cum_f[4] - ans_count} learners"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify all intervals representing scores below 60% [1 mark].\n"
        f"The intervals are: 0–20% (freq {f1}), 20–40% (freq {f2}), and 40–60% (freq {f3}).\n"
        f"Step 2: Sum their cumulative frequencies [1 mark].\n"
        f"Cumulative total = {f1} + {f2} + {f3} = {ans_count} learners.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="16",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the frequencies of all intervals that are strictly less than 60%.",
        tier_2=f"Sum: {f1} + {f2} + {f3}.",
        tier_3=f"Total = {ans_count} learners.",
        r=r,
    )


def generate_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Subskill 17: Two-way contingency table completion (finding missing cell value)."""
    # Boys vs Girls, Soccer vs Netball
    b_soccer = r.choice([25, 30, 35])
    b_netball = r.choice([5, 8, 10])
    total_boys = b_soccer + b_netball

    g_soccer = r.choice([10, 12, 15])
    g_netball = r.choice([28, 32, 35])
    total_girls = g_soccer + g_netball

    total_soccer = b_soccer + g_soccer
    total_netball = b_netball + g_netball
    grand_total = total_boys + total_girls

    prompt = (
        f"The following two-way table shows sports participation among Grade 11 learners:\n\n"
        f"| Gender | Soccer | Netball | Total |\n"
        f"| :--- | :--- | :--- | :--- |\n"
        f"| Boys | {b_soccer} | [ X ] | {total_boys} |\n"
        f"| Girls | {g_soccer} | {g_netball} | {total_girls} |\n"
        f"| **Total** | {total_soccer} | {total_netball} | {grand_total} |\n\n"
        f"Calculate the missing value for [ X ] (the number of boys playing Netball)."
    )

    correct_ans = f"{b_netball}"
    wrong_1 = f"{b_netball + 5}"
    wrong_2 = f"{b_soccer - g_soccer}"
    wrong_3 = f"{total_netball - g_netball + 2}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Use the row total or column total equation [1 mark].\n"
        f"Row equation: {b_soccer} + X = {total_boys}  (or Column equation: X + {g_netball} = {total_netball}).\n"
        f"Step 2: Solve for X [1 mark].\n"
        f"X = {total_boys} - {b_soccer} = {b_netball}.\n"
        f"Step 3: Stated value [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="17",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the known value in the row from the row total: Total Boys - Boys playing soccer.",
        tier_2=f"{total_boys} - {b_soccer} = {b_netball}.",
        tier_3=f"X = {b_netball}.",
        r=r,
    )


def generate_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Subskill 18: Read conditional frequency from a two-way table."""
    b_pass = r.choice([36, 40, 44])
    b_fail = r.choice([4, 6, 8])
    total_boys = b_pass + b_fail

    g_pass = r.choice([42, 45, 48])
    g_fail = r.choice([3, 5, 6])
    total_girls = g_pass + g_fail

    total_pass = b_pass + g_pass
    total_fail = b_fail + g_fail
    grand_total = total_boys + total_girls

    # Question: What percentage of GIRLS passed the test?
    pct_girls_passed = round((g_pass / total_girls) * 100, 1)

    prompt = (
        f"Refer to the test result breakdown in the two-way contingency table below:\n\n"
        f"| Gender | Passed | Failed | Total |\n"
        f"| :--- | :--- | :--- | :--- |\n"
        f"| Boys | {b_pass} | {b_fail} | {total_boys} |\n"
        f"| Girls | {g_pass} | {g_fail} | {total_girls} |\n"
        f"| **Total** | {total_pass} | {total_fail} | {grand_total} |\n\n"
        f"What percentage of the GIRLS passed the test (round to one decimal place)?"
    )

    correct_ans = f"{_fmt(pct_girls_passed, 1)}%"
    wrong_1 = f"{_fmt(round((g_pass / total_pass) * 100, 1), 1)}%"  # divided by total passed instead of total girls
    wrong_2 = f"{_fmt(round((g_pass / grand_total) * 100, 1), 1)}%"  # divided by grand total
    wrong_3 = f"{_fmt(pct_girls_passed - 5.0, 1)}%"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify the subgroup denominator and numerator [1 mark].\n"
        f"The question specifies 'of the GIRLS', so the denominator is Total Girls ({total_girls}).\n"
        f"The numerator is Girls who passed ({g_pass}).\n"
        f"Step 2: Calculate percentage [1 mark].\n"
        f"Percentage = ({g_pass} ÷ {total_girls}) × 100% = {_fmt(pct_girls_passed, 1)}%.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="18",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Make sure you use the Total Girls as the denominator, not the grand total.",
        tier_2=f"Divide Girls who passed ({g_pass}) by Total Girls ({total_girls}) and multiply by 100.",
        tier_3=f"Percentage = {_fmt(pct_girls_passed, 1)}%.",
        r=r,
    )
