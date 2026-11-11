"""Subskills 09 to 16: Grouped frequency tables, class intervals, cumulative frequency, and ogives."""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_pct,
)


def generate_09_class_interval_width(r: random.Random) -> Dict[str, Any]:
    """Determine class width and lower/upper boundaries for grouped data."""
    start = r.choice([20, 30, 40, 50])
    width = r.choice([10, 15, 20])
    intervals = [
        f"{start + i * width} ≤ x < {start + (i + 1) * width}" for i in range(4)
    ]
    correct_ans = f"Class width: {width}; Lower boundary: {start}; Upper boundary: {start + width}"

    custom_options = [
        f"Class width: {width}; Lower boundary: {start}; Upper boundary: {start + width}",
        f"Class width: {width - 1}; Lower boundary: {start + 1}; Upper boundary: {start + width}",
        f"Class width: {width * 2}; Lower boundary: {start}; Upper boundary: {start + width * 2}",
        f"Class width: {width}; Lower boundary: {start + width}; Upper boundary: {start}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A traffic department records the speeds of vehicles on a national road using the following class intervals:\n"
        f"• {intervals[0]}\n"
        f"• {intervals[1]}\n"
        f"• {intervals[2]}\n"
        f"• {intervals[3]}\n\n"
        f"State the class interval width and the lower and upper boundaries of the first class interval ({intervals[0]})."
    )
    explanation = (
        f"Step 1: Lower boundary of first class = {start} [M].\n"
        f"Step 2: Upper boundary of first class = {start + width} [M].\n"
        f"Step 3: Class width = Upper boundary - Lower boundary = {start + width} - {start} = {width} [A]."
    )
    return _build_question_payload(
        subskill_id="09_class_interval_width",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the lower limit from the upper limit of the interval.",
        tier_2=f"For {intervals[0]}, subtract {start} from {start + width}.",
        tier_3=f"The class width is {width}, with lower boundary {start} and upper boundary {start + width}.",
        r=r,
    )


def generate_10_class_midpoints_calculation(r: random.Random) -> Dict[str, Any]:
    """Calculate the midpoint (class mark) of a class interval."""
    low = r.choice([30, 40, 50, 60, 70])
    high = low + r.choice([10, 20])
    mid = (low + high) / 2
    correct_ans = f"{_fmt(mid, 1)}"

    custom_options = [
        f"{_fmt(mid, 1)}",
        f"{_fmt(mid + 5, 1)}",
        f"{_fmt(mid - 5, 1)}",
        f"{_fmt(high - 2, 1)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In a study of weekly grocery expenditure among South African households, one of the grouped intervals "
        f"is recorded as:\n"
        f"R {low}00 to R {high}00 (i.e. {low} ≤ x < {high} in hundreds of Rands).\n\n"
        f"Calculate the class midpoint (class mark) for this interval."
    )
    explanation = (
        f"Step 1: Recall the midpoint formula: Midpoint = (Lower limit + Upper limit) ÷ 2 [M].\n"
        f"Step 2: Substitute: ({low} + {high}) ÷ 2 [M].\n"
        f"Step 3: Midpoint = {_fmt(mid, 1)} [A]."
    )
    return _build_question_payload(
        subskill_id="10_class_midpoints_calculation",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the lower and upper limits together and divide by 2.",
        tier_2=f"Calculate ({low} + {high}) ÷ 2.",
        tier_3=f"The class midpoint is {_fmt(mid, 1)}.",
        r=r,
    )


def generate_11_estimated_mean_grouped_data(r: random.Random) -> Dict[str, Any]:
    """Calculate the estimated mean from a grouped frequency table."""
    # 4 intervals with width 10
    base = r.choice([40, 50])
    midpoints = [base + 5, base + 15, base + 25, base + 35]
    freqs = [r.randint(4, 8), r.randint(8, 14), r.randint(6, 12), r.randint(2, 6)]
    total_f = sum(freqs)
    sum_fm = sum(m * f for m, f in zip(midpoints, freqs))
    est_mean = sum_fm / total_f
    correct_ans = f"{_fmt(est_mean, 2)}%"

    custom_options = [
        f"{_fmt(est_mean, 2)}%",
        f"{_fmt(est_mean + 4.5, 2)}%",
        f"{_fmt(est_mean - 3.8, 2)}%",
        f"{_fmt(sum(midpoints) / 4, 2)}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    table_md = (
        "| Mark Interval (%) | Midpoint (m) | Frequency (f) | f × m |\n"
        "|---|---|---|---|\n"
        f"| {base} – {base+9} | {midpoints[0]} | {freqs[0]} | {midpoints[0] * freqs[0]} |\n"
        f"| {base+10} – {base+19} | {midpoints[1]} | {freqs[1]} | {midpoints[1] * freqs[1]} |\n"
        f"| {base+20} – {base+29} | {midpoints[2]} | {freqs[2]} | {midpoints[2] * freqs[2]} |\n"
        f"| {base+30} – {base+39} | {midpoints[3]} | {freqs[3]} | {midpoints[3] * freqs[3]} |\n"
        f"| **Total** | | **{total_f}** | **{sum_fm}** |\n"
    )

    prompt = (
        f"The test results of a Grade 12 Mathematical Literacy class are summarized in the grouped frequency table below:\n\n"
        f"{table_md}\n"
        f"Calculate the estimated mean mark for this group of learners, rounded to two decimal places."
    )
    explanation = (
        f"Step 1: Formula for estimated mean = Σ(f × m) ÷ Σf [M].\n"
        f"Step 2: Σ(f × m) = {sum_fm} and Σf = {total_f} [M].\n"
        f"Step 3: Estimated Mean = {sum_fm} ÷ {total_f} = {_fmt(est_mean, 2)}% [A]."
    )
    return _build_question_payload(
        subskill_id="11_estimated_mean_grouped_data",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the total of the (f × m) column by the total frequency.",
        tier_2=f"Calculate {sum_fm} ÷ {total_f}.",
        tier_3=f"The estimated mean is {_fmt(est_mean, 2)}%.",
        r=r,
    )


def generate_12_modal_class_interval(r: random.Random) -> Dict[str, Any]:
    """Identify the modal class interval from a grouped frequency table."""
    intervals = ["40 – 49", "50 – 59", "60 – 69", "70 – 79", "80 – 89"]
    freqs = [6, 12, 28, 14, 5]
    r.shuffle(freqs)
    # Ensure one unique maximum
    max_f = max(freqs)
    modal_idx = freqs.index(max_f)
    modal_interval = intervals[modal_idx]

    correct_ans = f"{modal_interval} (Frequency = {max_f})"
    custom_options = [
        f"{intervals[i]} (Frequency = {freqs[i]})" for i in range(len(intervals)) if i != modal_idx
    ][:3]
    custom_options.insert(0, correct_ans)
    options, _ = _build_options(correct_ans, r, custom_options)

    rows = "\n".join([f"| {intervals[i]} | {freqs[i]} |" for i in range(len(intervals))])
    table_md = (
        "| Score Range | Frequency |\n"
        "|---|---|\n"
        f"{rows}\n"
    )

    prompt = (
        f"A regional hospital records the recovery time (in hours) of patients in the table below:\n\n"
        f"{table_md}\n"
        f"Identify the modal class interval for this dataset."
    )
    explanation = (
        f"Step 1: Identify the highest frequency in the frequency column: {max_f} [M].\n"
        f"Step 2: Read the corresponding interval: {modal_interval} [M].\n"
        f"Step 3: The modal class interval is {modal_interval} [A]."
    )
    return _build_question_payload(
        subskill_id="12_modal_class_interval",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look for the class interval that has the highest frequency count.",
        tier_2=f"The highest frequency is {max_f}.",
        tier_3=f"The corresponding class interval is {modal_interval}.",
        r=r,
    )


def generate_13_cumulative_frequency_table(r: random.Random) -> Dict[str, Any]:
    """Calculate missing values in a cumulative frequency column."""
    f1 = r.randint(4, 8)
    f2 = r.randint(6, 10)
    f3 = r.randint(10, 16)
    f4 = r.randint(5, 9)
    c1 = f1
    c2 = c1 + f2
    c3 = c2 + f3
    c4 = c3 + f4

    correct_ans = f"Value A = {c2}; Value B = {c4}"
    custom_options = [
        f"Value A = {c2}; Value B = {c4}",
        f"Value A = {c2 + 3}; Value B = {c4 - 2}",
        f"Value A = {f2}; Value B = {f4}",
        f"Value A = {c1 + f3}; Value B = {c3}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    table_md = (
        "| Interval | Frequency (f) | Cumulative Frequency (cf) |\n"
        "|---|---|---|\n"
        f"| 10 – 19 | {f1} | {c1} |\n"
        f"| 20 – 29 | {f2} | **A** |\n"
        f"| 30 – 39 | {f3} | {c3} |\n"
        f"| 40 – 49 | {f4} | **B** |\n"
    )

    prompt = (
        f"Consider the incomplete frequency distribution table below:\n\n"
        f"{table_md}\n"
        f"Calculate the missing cumulative frequency values A and B."
    )
    explanation = (
        f"Step 1: Calculate cumulative frequency A: {c1} + {f2} = {c2} [M].\n"
        f"Step 2: Calculate cumulative frequency B: {c3} + {f4} = {c4} [M].\n"
        f"Step 3: A = {c2} and B = {c4} [A]."
    )
    return _build_question_payload(
        subskill_id="13_cumulative_frequency_table",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Cumulative frequency is found by adding each frequency to the sum of the preceding frequencies.",
        tier_2=f"A = {c1} + {f2} = {c2}; B = {c3} + {f4} = {c4}.",
        tier_3=f"A = {c2} and B = {c4}.",
        r=r,
    )


def generate_14_reading_median_from_ogive(r: random.Random) -> Dict[str, Any]:
    """Read the median value from an ogive (cumulative frequency curve)."""
    n_total = r.choice([100, 120, 200])
    half_n = n_total // 2
    median_val = r.choice([54, 58, 62, 65, 68])

    correct_ans = f"Position: {half_n} on vertical axis; Median = {median_val}%"
    custom_options = [
        f"Position: {half_n} on vertical axis; Median = {median_val}%",
        f"Position: {int(n_total * 0.25)} on vertical axis; Median = {median_val - 12}%",
        f"Position: {int(n_total * 0.75)} on vertical axis; Median = {median_val + 14}%",
        f"Position: {n_total} on vertical axis; Median = 100%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An ogive (cumulative frequency curve) representing the trial exam marks of {n_total} Grade 12 learners "
        f"has cumulative frequency on the vertical y-axis (0 to {n_total}) and examination marks (%) on the horizontal x-axis.\n\n"
        f"If the horizontal projection line from the 50% cumulative frequency position intersects the ogive at {median_val}%, "
        f"state the cumulative frequency rank used and the resulting median examination mark."
    )
    explanation = (
        f"Step 1: The median corresponds to 50% of total candidates: 50% of {n_total} = {half_n} [M].\n"
        f"Step 2: Read across from cf = {half_n} to the curve, then down to the horizontal mark axis [M].\n"
        f"Step 3: The median mark is {median_val}% [A]."
    )
    return _build_question_payload(
        subskill_id="14_reading_median_from_ogive",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The median is at the 50% mark of the total sample size on the cumulative frequency axis.",
        tier_2=f"Calculate 50% of {n_total} = {half_n}.",
        tier_3=f"Reading down from cf = {half_n} gives a median mark of {median_val}%.",
        r=r,
    )


def generate_15_reading_quartiles_iqr_from_ogive(r: random.Random) -> Dict[str, Any]:
    """Determine Q1, Q3, and calculate IQR from an ogive curve."""
    n_total = r.choice([200, 400, 500])
    q1_pos = int(n_total * 0.25)
    q3_pos = int(n_total * 0.75)
    q1_val = r.choice([42, 45, 48])
    q3_val = r.choice([66, 70, 74])
    iqr = q3_val - q1_val

    correct_ans = f"Q1 = {q1_val}%; Q3 = {q3_val}%; IQR = {iqr}%"
    custom_options = [
        f"Q1 = {q1_val}%; Q3 = {q3_val}%; IQR = {iqr}%",
        f"Q1 = {q1_val - 5}%; Q3 = {q3_val + 5}%; IQR = {iqr + 10}%",
        f"Q1 = {q1_pos}%; Q3 = {q3_pos}%; IQR = {q3_pos - q1_pos}%",
        f"Q1 = {q1_val}%; Q3 = {q3_val}%; IQR = {int(iqr / 2)}%",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"From an ogive plotting the scores of {n_total} learners:\n"
        f"• The 25% position (cf = {q1_pos}) corresponds to a score of {q1_val}%.\n"
        f"• The 75% position (cf = {q3_pos}) corresponds to a score of {q3_val}%.\n\n"
        f"Determine Quartile 1 (Q1), Quartile 3 (Q3), and calculate the Interquartile Range (IQR)."
    )
    explanation = (
        f"Step 1: Q1 is read at 25% cumulative frequency = {q1_val}% [M].\n"
        f"Step 2: Q3 is read at 75% cumulative frequency = {q3_val}% [M].\n"
        f"Step 3: Calculate IQR = Q3 - Q1 = {q3_val}% - {q1_val}% = {iqr}% [A]."
    )
    return _build_question_payload(
        subskill_id="15_reading_quartiles_iqr_from_ogive",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Recall that Q1 is at the 25% cumulative frequency mark and Q3 is at 75%.",
        tier_2=f"IQR is calculated by subtracting Q1 from Q3: {q3_val} - {q1_val}.",
        tier_3=f"Q1 = {q1_val}%, Q3 = {q3_val}%, and IQR = {iqr}%.",
        r=r,
    )


def generate_16_ogive_benchmark_percentage(r: random.Random) -> Dict[str, Any]:
    """Determine the number and percentage of candidates exceeding a benchmark from an ogive."""
    n_total = r.choice([250, 300, 400, 500])
    pass_mark = 50
    cf_at_pass = int(n_total * r.choice([0.28, 0.35, 0.40]))
    passed_count = n_total - cf_at_pass
    passed_pct = (passed_count / n_total) * 100

    correct_ans = f"{passed_count} learners ({_fmt(passed_pct, 1)}%) passed"
    custom_options = [
        f"{passed_count} learners ({_fmt(passed_pct, 1)}%) passed",
        f"{cf_at_pass} learners ({_fmt((cf_at_pass/n_total)*100, 1)}%) passed",
        f"{passed_count - 30} learners ({_fmt(passed_pct - 10, 1)}%) passed",
        f"{int(n_total * 0.5)} learners (50,0%) passed",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An ogive curve represents the final exam results of {n_total} learners. "
        f"Reading up from the pass mark of {pass_mark}% on the horizontal axis to the curve gives a cumulative "
        f"frequency of {cf_at_pass} learners.\n\n"
        f"Calculate how many learners passed the examination (scored {pass_mark}% or higher) and express this as a percentage."
    )
    explanation = (
        f"Step 1: The cumulative frequency {cf_at_pass} represents learners who scored LESS than {pass_mark}% [M].\n"
        f"Step 2: Number of learners who passed = Total - Failed = {n_total} - {cf_at_pass} = {passed_count} learners [M].\n"
        f"Step 3: Percentage passed = ({passed_count} ÷ {n_total}) × 100% = {_fmt(passed_pct, 1)}% [A]."
    )
    return _build_question_payload(
        subskill_id="16_ogive_benchmark_percentage",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember that cumulative frequency indicates the number of candidates scoring up to that mark.",
        tier_2=f"Subtract {cf_at_pass} from {n_total} to get the number who passed.",
        tier_3=f"{passed_count} learners passed ({_fmt(passed_pct, 1)}%).",
        r=r,
    )
