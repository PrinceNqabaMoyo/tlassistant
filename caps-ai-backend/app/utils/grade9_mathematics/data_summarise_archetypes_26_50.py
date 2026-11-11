"""Grade 9 Mathematics - Collect, Organise & Summarise Data Archetypes 26 to 50
=============================================================================
Grounded strictly in:
  - CAPS Grade 9 Mathematics: Term 4 Topic: Collect, organise and summarise data
  - curriculum_docs_auto/Mathematics_Gr9/Term 4/ Data Handling
  - Five-number summary, stem-and-leaf plots, dot plots, grouped frequency tables
    (class intervals, midpoints, modal class, median class, estimated mean),
    relative and cumulative frequencies, discrete vs continuous data, data transformation
    effects, comparing distributions, SA real-world contexts, and diagnostic error analysis.

Covers Archetypes 26 - 50:
  26: Five-number summary (Min, Q1, Median, Q3, Max)
  27: Stem-and-leaf diagram reading values
  28: Stem-and-leaf diagram median and mode
  29: Dot plot reading frequency and spread
  30: Grouped frequency table identifying class intervals
  31: Class midpoints calculation for grouped intervals
  32: Modal class interval identification
  33: Median class interval identification
  34: Estimated mean of grouped data (sum(f*m) / sum(f))
  35: Relative frequency calculation as fraction or percentage
  36: Cumulative frequency calculation (running totals)
  37: Percentage of data above or below a given benchmark
  38: Discrete vs continuous numerical data classification
  39: Numerical vs categorical data classification
  40: Effect of adding a constant to all values on mean and range
  41: Effect of multiplying all values by a constant on mean and range
  42: Comparing two datasets using mean and range (consistency)
  43: Comparing two datasets using median and IQR (spread)
  44: Contextual SA temperatures mean and range
  45: Contextual SA mathematics exam scores analysis
  46: Contextual SA monthly household expenditure median
  47: Diagnostic error analysis: finding median without ordering raw data
  48: Diagnostic error analysis: reporting frequency instead of data score for mode
  49: Diagnostic error analysis: dividing by row count instead of total frequency in mean
  50: Compound multi-stage statistical investigation synthesis
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics.data_summarise_svg import (
    draw_stem_and_leaf_svg,
    draw_dot_plot_svg,
    draw_frequency_table_svg,
)


def arch_26_five_number_summary_min_q1_med_q3_max(rng: random.Random) -> Dict[str, Any]:
    """Calculate the five-number summary values for a dataset of 9 values."""
    # 9 values: min = [0], Q1 = ([1]+[2])/2, Med = [4], Q3 = ([6]+[7])/2, max = [8]
    # To keep integers, let [1]=[2] and [6]=[7]
    v_min = rng.randint(10, 15)
    q1 = rng.randint(v_min + 3, v_min + 8)
    med = rng.randint(q1 + 4, q1 + 10)
    q3 = rng.randint(med + 4, med + 10)
    v_max = rng.randint(q3 + 5, q3 + 15)

    data = [v_min, q1, q1, rng.randint(q1, med), med, rng.randint(med, q3), q3, q3, v_max]
    data.sort()
    shuffled = list(data)
    rng.shuffle(shuffled)
    val_str = ", ".join(str(x) for x in shuffled)

    ans_str = f"Min: {v_min}, Q1: {q1}, Median: {med}, Q3: {q3}, Max: {v_max}"

    prompt = (
        f"Consider the test marks of 9 learners:\n"
        f"**{val_str}**\n\n"
        f"1. What is the **minimum** mark?\n"
        f"2. What is the **maximum** mark?\n"
        f"3. What is the **median** ($Q_2$) mark?\n"
        f"(State the **median** mark)."
    )

    return {
        "subskill": "26_five_number_summary_min_q1_med_q3_max",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(med),
        "sample_answer": f"{med} (Five-number summary: {ans_str})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Order the 9 marks from smallest to largest: {', '.join(str(x) for x in data)}", "marks": 1},
            {"step": f"Identify median as the 5th value: {med}", "marks": 1},
        ],
        "hints": [
            "Sort all 9 values in ascending order.",
            f"The 5th value is the median: **{med}**.",
        ],
        "misconception_tags": ["five_number_summary_position_error"],
    }


def arch_27_stem_and_leaf_diagram_reading_values(rng: random.Random) -> Dict[str, Any]:
    """Read specific values from a stem-and-leaf plot."""
    stems = {
        2: [1, 4, 7],
        3: [0, 2, 5, 8],
        4: [1, 3, 6],
    }
    target_stem = rng.choice([2, 3, 4])
    target_leaf = rng.choice(stems[target_stem])
    target_val = target_stem * 10 + target_leaf

    seed_val = rng.randint(1000, 999999)
    svg = draw_stem_and_leaf_svg(stems, title="Learner Ages in Months", key_example="3 | 2 means 32", seed=seed_val)

    prompt = (
        f"Refer to the stem-and-leaf plot below:\n\n"
        f"What actual numerical value is represented by the stem **${target_stem}$** and leaf **${target_leaf}$**?"
    )

    return {
        "subskill": "27_stem_and_leaf_diagram_reading_values",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(target_val),
        "sample_answer": str(target_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Combine stem ({target_stem}) and leaf ({target_leaf}) using the key: {target_stem}*10 + {target_leaf} = {target_val}", "marks": 1},
        ],
        "hints": [
            "According to the key, a stem of $3$ and leaf of $2$ represents $32$.",
            f"Combine stem ${target_stem}$ and leaf ${target_leaf}$.",
            f"Value $= {target_val}$.",
        ],
        "misconception_tags": ["stem_and_leaf_key_misinterpretation"],
    }


def arch_28_stem_and_leaf_diagram_median_and_mode(rng: random.Random) -> Dict[str, Any]:
    """Find the mode from a stem-and-leaf plot."""
    stems = {
        1: [4, 7, 8],
        2: [1, 3, 3, 3, 8],
        3: [2, 5, 9],
    }
    mode_val = 23  # leaf 3 appears 3 times in stem 2
    seed_val = rng.randint(1000, 999999)
    svg = draw_stem_and_leaf_svg(stems, title="Quiz Scores Out of 40", key_example="2 | 1 means 21", seed=seed_val)

    prompt = (
        f"Refer to the stem-and-leaf plot below showing quiz scores:\n\n"
        f"Determine the **mode** of the dataset."
    )

    return {
        "subskill": "28_stem_and_leaf_diagram_median_and_mode",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(mode_val),
        "sample_answer": str(mode_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Identify repeated leaf '3' appearing three times on stem '2'", "marks": 1},
            {"step": f"Combine stem and leaf to state mode: {mode_val}", "marks": 1},
        ],
        "hints": [
            "Look for the leaf that repeats most frequently along a single stem row.",
            "Leaf $3$ appears three times in the row for stem $2$.",
            f"Mode $= {mode_val}$.",
        ],
        "misconception_tags": ["stem_and_leaf_mode_stated_leaf_only"],
    }


def arch_29_dot_plot_reading_frequency_and_spread(rng: random.Random) -> Dict[str, Any]:
    """Read frequency of a value from a dot plot."""
    points = [3, 4, 4, 5, 5, 5, 5, 6, 6, 7]
    target_val = 5
    freq = points.count(target_val)
    seed_val = rng.randint(1000, 999999)
    svg = draw_dot_plot_svg(points, title="Goals Scored per Match", x_label="Number of Goals", seed=seed_val)

    prompt = (
        f"Refer to the dot plot below showing the number of goals scored in 10 soccer matches:\n\n"
        f"In how many matches were exactly **${target_val}$ goals** scored?"
    )

    return {
        "subskill": "29_dot_plot_reading_frequency_and_spread",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": str(freq),
        "sample_answer": str(freq),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Count number of dots stacked vertically above {target_val}: {freq} dots", "marks": 1},
        ],
        "hints": [
            f"Locate the number {target_val} on the horizontal axis.",
            f"Count the number of blue dots stacked directly above it.",
            f"Frequency $= {freq}$.",
        ],
        "misconception_tags": ["dot_plot_reading_error"],
    }


def arch_30_grouped_frequency_table_identifying_class_intervals(rng: random.Random) -> Dict[str, Any]:
    """Calculate the class width of grouped intervals (e.g. 10 <= x < 20)."""
    width_val = rng.choice([5, 10, 15, 20])
    low = rng.choice([0, 10, 20, 50])
    high = low + width_val

    prompt = (
        f"In a grouped frequency table, one of the class intervals is written as:\n"
        f"**${low} \\le x < {high}$**\n\n"
        f"What is the **class width** (interval size) of this class interval?"
    )

    return {
        "subskill": "30_grouped_frequency_table_identifying_class_intervals",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(width_val),
        "sample_answer": str(width_val),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate class width: upper limit - lower limit = {high} - {low} = {width_val}", "marks": 1},
        ],
        "hints": [
            "Class width is the difference between the upper limit and the lower limit.",
            f"Subtract: ${high} - {low} = {width_val}$.",
            f"Class width $= {width_val}$.",
        ],
        "misconception_tags": ["class_width_subtraction_error"],
    }


def arch_31_class_midpoints_calculation_for_grouped_intervals(rng: random.Random) -> Dict[str, Any]:
    """Calculate the midpoint m of a class interval: (lower + upper) / 2."""
    low = rng.choice([10, 20, 30, 40, 50])
    width = rng.choice([10, 20])
    high = low + width
    mid = (low + high) // 2

    prompt = (
        f"Calculate the **class midpoint ($m$)** for the interval **${low} \\le x < {high}$**."
    )

    return {
        "subskill": "31_class_midpoints_calculation_for_grouped_intervals",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(mid),
        "sample_answer": str(mid),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State midpoint formula: m = (lower limit + upper limit) / 2", "marks": 1},
            {"step": f"Calculate: ({low} + {high}) / 2 = {low + high} / 2 = {mid}", "marks": 1},
        ],
        "hints": [
            "The midpoint is the exact average of the lower and upper limits.",
            f"Add the limits and divide by $2$: $\\frac{{{low} + {high}}}{{2}} = \\frac{{{low + high}}}{{2}}$.",
            f"Midpoint $= {mid}$.",
        ],
        "misconception_tags": ["class_midpoint_calculation_error"],
    }


def arch_32_modal_class_interval_identification(rng: random.Random) -> Dict[str, Any]:
    """Identify the modal class interval from grouped frequencies."""
    intervals = ["$0 \\le x < 10$", "$10 \\le x < 20$", "$20 \\le x < 30$", "$30 \\le x < 40$"]
    freqs = [rng.randint(4, 8) for _ in range(4)]
    max_idx = rng.randint(0, 3)
    freqs[max_idx] = max(freqs) + rng.randint(5, 9)
    modal_interval = intervals[max_idx]

    rows_text = "\n".join(f"- {inv}: **{f} learners**" for inv, f in zip(intervals, freqs))

    prompt = (
        f"A grouped frequency distribution of mathematics marks is given below:\n"
        f"{rows_text}\n\n"
        f"State the **modal class interval** (the interval with the highest frequency)."
    )

    clean_ans = modal_interval.replace("$", "")

    return {
        "subskill": "32_modal_class_interval_identification",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": clean_ans,
        "sample_answer": modal_interval,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Identify highest frequency: {freqs[max_idx]}", "marks": 1},
            {"step": f"State corresponding modal interval: {modal_interval}", "marks": 1},
        ],
        "hints": [
            "The modal class is the class interval containing the greatest frequency.",
            f"The largest frequency is {freqs[max_idx]}.",
            f"The modal class is **{modal_interval}**.",
        ],
        "misconception_tags": ["modal_class_stated_frequency_instead_of_interval"],
    }


def arch_33_median_class_interval_identification(rng: random.Random) -> Dict[str, Any]:
    """Identify the median class interval from cumulative frequencies."""
    intervals = ["$0 \\le x < 10$", "$10 \\le x < 20$", "$20 \\le x < 30$", "$30 \\le x < 40$"]
    freqs = [6, 12, 16, 6]  # total = 40
    # mid position = 20.5 => cumulative: 6, 18, 34 => in 3rd interval
    median_interval = intervals[2]

    rows_text = "\n".join(f"- {inv}: **{f} learners**" for inv, f in zip(intervals, freqs))

    prompt = (
        f"A total of **40 learners** wrote a test. Their marks are grouped as follows:\n"
        f"{rows_text}\n\n"
        f"In which **class interval** does the **median mark** lie?"
    )

    clean_ans = median_interval.replace("$", "")

    return {
        "subskill": "33_median_class_interval_identification",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": clean_ans,
        "sample_answer": median_interval,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Find median rank: 40 / 2 = 20th learner", "marks": 1},
            {"step": "Accumulate frequencies: 6, 18, 34 (20th learner lies in the 3rd interval)", "marks": 1},
            {"step": f"State interval: {median_interval}", "marks": 1},
        ],
        "hints": [
            "For $40$ learners, the median lies at position $\\approx 20$.",
            "Cumulative frequency: after 1st group = 6; after 2nd group = 18; after 3rd group = 34.",
            f"The 20th learner falls in **{median_interval}**.",
        ],
        "misconception_tags": ["median_class_interval_selection_error"],
    }


def arch_34_estimated_mean_of_grouped_data_sum_fm_over_sum_f(rng: random.Random) -> Dict[str, Any]:
    """Calculate estimated mean for grouped data using class midpoints."""
    # 3 intervals: 0 <= x < 10 (m=5), 10 <= x < 20 (m=15), 20 <= x < 30 (m=25)
    f1, f2, f3 = 4, 10, 6  # total = 20
    # sum(f*m) = 4*5 + 10*15 + 6*25 = 20 + 150 + 150 = 320
    # estimated mean = 320 / 20 = 16.0
    tot_f = f1 + f2 + f3
    tot_fm = f1 * 5 + f2 * 15 + f3 * 25
    est_mean = tot_fm // tot_f

    prompt = (
        f"Consider the grouped frequency distribution:\n"
        f"- $0 \\le x < 10$ (midpoint $m = 5$): **frequency $f = {f1}$**\n"
        f"- $10 \\le x < 20$ (midpoint $m = 15$): **frequency $f = {f2}$**\n"
        f"- $20 \\le x < 30$ (midpoint $m = 25$): **frequency $f = {f3}$**\n\n"
        f"Calculate the **estimated mean** ($\\text{{Estimated Mean}} = \\frac{{\\sum f \\cdot m}}{{\\sum f}}$)."
    )

    return {
        "subskill": "34_estimated_mean_of_grouped_data_sum_fm_over_sum_f",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(est_mean),
        "sample_answer": str(est_mean),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate sum(f * m) = ({f1}*5) + ({f2}*15) + ({f3}*25) = {tot_fm}", "marks": 1},
            {"step": f"Calculate sum(f) = {tot_f}", "marks": 1},
            {"step": f"Calculate estimated mean: {tot_fm} / {tot_f} = {est_mean}", "marks": 1},
        ],
        "hints": [
            "Multiply each class frequency $f$ by its midpoint $m$, add all products together, and divide by the total frequency $\\sum f$.",
            f"$\\sum (f \\cdot m) = {tot_fm}$, $\\sum f = {tot_f}$.",
            f"Estimated mean $= \\frac{{{tot_fm}}}{{{tot_f}}} = {est_mean}$.",
        ],
        "misconception_tags": ["estimated_mean_grouped_data_formula_error"],
    }


def arch_35_relative_frequency_calculation_as_fraction_or_percentage(rng: random.Random) -> Dict[str, Any]:
    """Calculate relative frequency as a percentage."""
    tot = rng.choice([20, 25, 40, 50])
    count = rng.choice([4, 5, 8, 10, 12])
    while count >= tot:
        count = tot // 2
    pct = int((count / tot) * 100)

    prompt = (
        f"Out of **${tot}$ surveyed commuters**, **${count}$** travel by train.\n\n"
        f"Calculate the **relative frequency** of train commuters as a **percentage (%)**."
    )

    return {
        "subskill": "35_relative_frequency_calculation_as_fraction_or_percentage",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(pct),
        "sample_answer": f"{pct}%",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"State relative frequency formula: frequency / total = {count} / {tot}", "marks": 1},
            {"step": f"Convert to percentage: ({count} / {tot}) * 100 = {pct}%", "marks": 1},
        ],
        "hints": [
            "Relative frequency as a percentage is $\\frac{\\text{frequency}}{\\text{total}} \\times 100\\%$.",
            f"Divide ${count}$ by ${tot}$ and multiply by $100$.",
            f"Answer: **{pct}%**.",
        ],
        "misconception_tags": ["relative_frequency_percentage_conversion_error"],
    }


def arch_36_cumulative_frequency_calculation_running_totals(rng: random.Random) -> Dict[str, Any]:
    """Calculate cumulative frequency running totals."""
    f1 = rng.randint(4, 8)
    f2 = rng.randint(6, 12)
    f3 = rng.randint(5, 10)
    cum3 = f1 + f2 + f3

    prompt = (
        f"A frequency distribution has the following successive frequencies:\n"
        f"- Category A: **${f1}$**\n"
        f"- Category B: **${f2}$**\n"
        f"- Category C: **${f3}$**\n\n"
        f"Calculate the **cumulative frequency** through Category C."
    )

    return {
        "subskill": "36_cumulative_frequency_calculation_running_totals",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(cum3),
        "sample_answer": str(cum3),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Add successive frequencies: {f1} + {f2} + {f3} = {cum3}", "marks": 1},
        ],
        "hints": [
            "Cumulative frequency is the running total of frequencies up to that category.",
            f"Add: ${f1} + {f2} + {f3} = {cum3}$.",
            f"Cumulative frequency $= {cum3}$.",
        ],
        "misconception_tags": ["cumulative_frequency_addition_error"],
    }


def arch_37_percentage_of_data_above_or_below_given_benchmark(rng: random.Random) -> Dict[str, Any]:
    """Calculate percentage of learners scoring above or equal to a pass mark."""
    tot = 50
    fail_count = rng.choice([10, 15, 20])
    pass_count = tot - fail_count
    pass_pct = int((pass_count / tot) * 100)

    prompt = (
        f"In a class of **50 learners**, **${pass_count}$ learners** scored $50\\%$ or higher on an examination.\n\n"
        f"What percentage of the class passed (scored $50\\%$ or higher)?"
    )

    return {
        "subskill": "37_percentage_of_data_above_or_below_given_benchmark",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(pass_pct),
        "sample_answer": f"{pass_pct}%",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate percentage: ({pass_count} / {tot}) * 100 = {pass_pct}%", "marks": 1},
        ],
        "hints": [
            "Divide the passing count by the total number of learners and multiply by 100.",
            f"$\\frac{{{pass_count}}}{{{tot}}} \\times 100 = {pass_pct}\\%$.",
            f"Answer: **{pass_pct}%**.",
        ],
        "misconception_tags": ["percentage_calculation_error"],
    }


def arch_38_discrete_vs_continuous_numerical_data_classification(rng: random.Random) -> Dict[str, Any]:
    """Classify numerical data as discrete (countable) or continuous (measurable)."""
    scenarios = [
        (
            "The number of text messages a teenager sends per day.",
            "discrete",
            "it is counted in whole numbers (you cannot send 3.7 messages)",
        ),
        (
            "The time taken (in seconds) by an athlete to run 100 metres.",
            "continuous",
            "time is measured on a continuous scale and can take any value with fractions of a second",
        ),
        (
            "The volume of petrol pumped into a motor car fuel tank in litres.",
            "continuous",
            "volume is measured continuously and can take any decimal value",
        ),
        (
            "The number of children in a household.",
            "discrete",
            "it is counted in discrete integer units",
        ),
    ]
    scen, kind, reason = rng.choice(scenarios)

    prompt = (
        f"Classify the following numerical data variable as **discrete** or **continuous**:\n"
        f"\"{scen}\""
    )

    return {
        "subskill": "38_discrete_vs_continuous_numerical_data_classification",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": kind,
        "sample_answer": kind,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Classify data type: {kind}", "marks": 1},
            {"step": f"Justify: {reason}", "marks": 1},
        ],
        "hints": [
            "Discrete data is counted in distinct separate values (usually whole numbers).",
            "Continuous data is measured on a continuous scale and can take any intermediate decimal value.",
            f"Answer: **{kind}**.",
        ],
        "misconception_tags": ["discrete_vs_continuous_confusion"],
    }


def arch_39_numerical_vs_categorical_data_classification(rng: random.Random) -> Dict[str, Any]:
    """Classify data as numerical (quantitative) or categorical (qualitative)."""
    scenarios = [
        ("Learners' favorite cold drink flavors (cola, orange, cream soda)", "categorical", "flavors are descriptive labels or categories, not numbers"),
        ("Learners' shoe sizes (size 4, 5, 6, 7)", "numerical", "shoe sizes are numeric quantities that can be averaged"),
        ("Makes of cars in a parking lot (Toyota, VW, Ford)", "categorical", "car brands are words representing categories"),
        ("Height of learners in centimetres", "numerical", "height is a measurable numerical value"),
    ]
    scen, kind, reason = rng.choice(scenarios)

    prompt = (
        f"Classify the following data variable as **categorical** or **numerical**:\n"
        f"\"{scen}\""
    )

    return {
        "subskill": "39_numerical_vs_categorical_data_classification",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": kind,
        "sample_answer": kind,
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Classify as {kind}", "marks": 1},
            {"step": f"Justify: {reason}", "marks": 1},
        ],
        "hints": [
            "Categorical data represents categories or qualities described by words.",
            "Numerical data represents quantities measured or counted as numbers.",
            f"Answer: **{kind}**.",
        ],
        "misconception_tags": ["categorical_vs_numerical_confusion"],
    }


def arch_40_effect_of_adding_constant_to_all_values_on_mean_and_range(rng: random.Random) -> Dict[str, Any]:
    """Adding constant c to all values increases mean by c, while range remains unchanged."""
    orig_mean = rng.randint(45, 65)
    orig_range = rng.randint(20, 35)
    c = rng.randint(5, 10)
    new_mean = orig_mean + c

    prompt = (
        f"A teacher realizes a test was marked out of 90 instead of 100, and adds **${c}$ bonus marks** "
        f"to every single learner's score.\n"
        f"Originally, the class **mean was ${orig_mean}$** and the **range was ${orig_range}$**.\n\n"
        f"1. What is the **new mean**?\n"
        f"2. What is the **new range**?\n"
        f"(State the **new range**)."
    )

    return {
        "subskill": "40_effect_of_adding_constant_to_all_values_on_mean_and_range",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(orig_range),
        "sample_answer": f"{orig_range} (new mean = {new_mean}, new range = {orig_range})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recall property: adding a constant c shifts all data equally, so range is unchanged: {orig_range}", "marks": 1},
        ],
        "hints": [
            "Adding a constant shifts every score up by the same amount.",
            f"Both the maximum and minimum increase by ${c}$, so their difference (Range) remains exactly ${orig_range}$.",
            f"New range $= {orig_range}$.",
        ],
        "misconception_tags": ["added_constant_to_range_error"],
    }


def arch_41_effect_of_multiplying_all_values_by_constant_on_mean_and_range(rng: random.Random) -> Dict[str, Any]:
    """Multiplying all values by constant c multiplies both mean and range by c."""
    orig_mean = rng.randint(20, 30)
    orig_range = rng.randint(10, 15)
    c = rng.choice([2, 3])
    new_mean = orig_mean * c
    new_range = orig_range * c

    prompt = (
        f"All values in a dataset with **mean = ${orig_mean}$** and **range = ${orig_range}$** are "
        f"multiplied by a factor of **${c}$**.\n\n"
        f"Calculate the **new range** of the transformed dataset."
    )

    return {
        "subskill": "41_effect_of_multiplying_all_values_by_constant_on_mean_and_range",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(new_range),
        "sample_answer": str(new_range),
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Recall scaling property: multiplying all values by c multiplies the range by c: {c} * {orig_range} = {new_range}", "marks": 1},
        ],
        "hints": [
            "Multiplying all values stretches the spread of the data by the same factor.",
            f"Multiply the original range by ${c}$: ${orig_range} \\times {c} = {new_range}$.",
            f"New range $= {new_range}$.",
        ],
        "misconception_tags": ["multiplied_data_range_scaling_error"],
    }


def arch_42_comparing_two_datasets_using_mean_and_range(rng: random.Random) -> Dict[str, Any]:
    """Compare consistency between two learners using range (smaller range = more consistent)."""
    prompt = (
        f"Two learners, Sipho and Thabo, wrote 5 mathematics tests. Both obtained an identical **mean mark of 72%**.\n"
        f"- Sipho's marks had a **range of 8%**.\n"
        f"- Thabo's marks had a **range of 34%**.\n\n"
        f"Which learner was **more consistent** in their performance across the tests?\n"
        f"State: **Sipho**"
    )

    return {
        "subskill": "42_comparing_two_datasets_using_mean_and_range",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Sipho",
        "sample_answer": "Sipho",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State that a smaller range indicates less spread/variation, meaning greater consistency", "marks": 1},
            {"step": "Identify Sipho as the more consistent performer (range 8% < 34%)", "marks": 1},
        ],
        "hints": [
            "A smaller range means test scores are clustered closely together, indicating higher consistency.",
            "Sipho's range (8%) is much smaller than Thabo's (34%).",
            "Answer: **Sipho**.",
        ],
        "misconception_tags": ["consistency_interpreted_as_higher_range"],
    }


def arch_43_comparing_two_datasets_using_median_and_iqr(rng: random.Random) -> Dict[str, Any]:
    """Compare spread of two distributions using interquartile range (IQR)."""
    prompt = (
        f"The waiting times at two clinic dispensaries are compared:\n"
        f"- Clinic A: **Median = 25 minutes**, **IQR = 6 minutes**\n"
        f"- Clinic B: **Median = 25 minutes**, **IQR = 22 minutes**\n\n"
        f"Which clinic has a more predictable and uniform waiting time for the middle 50% of patients?\n"
        f"State: **Clinic A**"
    )

    return {
        "subskill": "43_comparing_two_datasets_using_median_and_iqr",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "Clinic A",
        "sample_answer": "Clinic A",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Recognize that a smaller IQR indicates less variation in the middle 50% of data", "marks": 1},
            {"step": "Conclude that Clinic A has more consistent waiting times", "marks": 1},
        ],
        "hints": [
            "The IQR measures the spread of the middle 50% of the data.",
            "A smaller IQR means less variation and greater predictability.",
            "Answer: **Clinic A**.",
        ],
        "misconception_tags": ["iqr_comparison_spread_confusion"],
    }


def arch_44_contextual_sa_temperatures_mean_and_range(rng: random.Random) -> Dict[str, Any]:
    """Calculate temperature range in South African city."""
    min_temp = rng.randint(8, 14)
    max_temp = rng.randint(24, 34)
    r_temp = max_temp - min_temp
    city = rng.choice(["Durban", "Johannesburg", "Bloemfontein", "Polokwane"])

    prompt = (
        f"On a summer day in **{city}**, the minimum temperature was **${min_temp}^\\circ\\text{{C}}$** "
        f"and the maximum temperature was **${max_temp}^\\circ\\text{{C}}$**.\n\n"
        f"Calculate the **temperature range** for that day in $^\\circ\\text{{C}}$."
    )

    return {
        "subskill": "44_contextual_sa_temperatures_mean_and_range",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(r_temp),
        "sample_answer": f"{r_temp}°C",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate range: Maximum - Minimum = {max_temp} - {min_temp} = {r_temp}°C", "marks": 1},
        ],
        "hints": [
            "Range $= \\text{Maximum} - \\text{Minimum}$.",
            f"Subtract: ${max_temp} - {min_temp} = {r_temp}$.",
            f"Range $= {r_temp}^\\circ\\text{{C}}$.",
        ],
        "misconception_tags": ["temperature_range_subtraction_error"],
    }


def arch_45_contextual_sa_mathematics_exam_scores_analysis(rng: random.Random) -> Dict[str, Any]:
    """Calculate mean of 4 term marks for a South African learner."""
    t1 = rng.randint(55, 75)
    t2 = rng.randint(55, 75)
    t3 = rng.randint(55, 75)
    # Ensure divisible by 4
    rem = (t1 + t2 + t3) % 4
    t4 = rng.choice([60, 64, 68, 72]) - rem
    total = t1 + t2 + t3 + t4
    mean_mark = total // 4

    prompt = (
        f"Nqobile's mathematics marks across the four school terms were:\n"
        f"- Term 1: **${t1}\\%$**\n"
        f"- Term 2: **${t2}\\%$**\n"
        f"- Term 3: **${t3}\\%$**\n"
        f"- Term 4: **${t4}\\%$**\n\n"
        f"Calculate her **final year average (mean) mark** as a percentage (\\%)."
    )

    return {
        "subskill": "45_contextual_sa_mathematics_exam_scores_analysis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(mean_mark),
        "sample_answer": f"{mean_mark}%",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Sum four term marks: {t1} + {t2} + {t3} + {t4} = {total}", "marks": 1},
            {"step": f"Divide by 4: {total} / 4 = {mean_mark}%", "marks": 1},
        ],
        "hints": [
            "Add all 4 marks together and divide by 4.",
            f"Sum $= {total}$. Divide by $4$: ${total} \\div 4 = {mean_mark}$.",
            f"Average $= {mean_mark}\\%$.",
        ],
        "misconception_tags": ["term_average_calculation_error"],
    }


def arch_46_contextual_sa_monthly_household_expenditure_median(rng: random.Random) -> Dict[str, Any]:
    """Find median expenditure from 5 household budgets."""
    vals = sorted([rng.randint(2500, 6500) for _ in range(5)])
    med = vals[2]
    shuffled = list(vals)
    rng.shuffle(shuffled)
    s_str = ", ".join(f"R{v}" for v in shuffled)

    prompt = (
        f"Five households in Soweto reported their monthly grocery expenditure:\n"
        f"**{s_str}**\n\n"
        f"Calculate the **median monthly grocery expenditure** in Rands (R)."
    )

    return {
        "subskill": "46_contextual_sa_monthly_household_expenditure_median",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(med),
        "sample_answer": f"R{med}",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Order expenditures from lowest to highest: {', '.join(f'R{v}' for v in vals)}", "marks": 1},
            {"step": f"Identify middle (3rd) value: R{med}", "marks": 1},
        ],
        "hints": [
            "Sort the 5 expenditure amounts from smallest to largest.",
            f"The middle (3rd) amount is the median: **R{med}**.",
        ],
        "misconception_tags": ["grocery_median_ordering_error"],
    }


def arch_47_error_analysis_calculating_median_without_ordering_data(rng: random.Random) -> Dict[str, Any]:
    """Diagnose error of selecting the middle number of an unordered raw list."""
    prompt = (
        f"Given the raw dataset: **12, 45, 18, 9, 30**\n"
        f"A learner states: \"*The median is 18 because it is written in the middle.*\"\n\n"
        f"Explain why the learner's method is mathematically invalid.\n"
        f"State: **the numbers must be arranged in ascending order first**"
    )

    return {
        "subskill": "47_error_analysis_calculating_median_without_ordering_data",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "the numbers must be arranged in ascending order first",
        "sample_answer": "the numbers must be arranged in ascending order first",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "State rule: the median is the middle value of an ordered dataset (from smallest to largest)", "marks": 1},
        ],
        "hints": [
            "The physical middle of an unordered list is meaningless.",
            "You must sort the numbers from smallest to largest before locating the median.",
            "Answer: **the numbers must be arranged in ascending order first**.",
        ],
        "misconception_tags": ["median_requires_ordered_data_rule"],
    }


def arch_48_error_analysis_confusing_frequency_with_data_value_in_mode(rng: random.Random) -> Dict[str, Any]:
    """Diagnose stating the highest frequency count instead of the data score."""
    prompt = (
        f"In a test, 8 learners scored 15 out of 20, which was the highest count of any mark.\n"
        f"A learner states: \"*The mode is 8.*\"\n\n"
        f"What error did the learner make?\n"
        f"State: **the learner gave the frequency instead of the actual score (15)**"
    )

    return {
        "subskill": "48_error_analysis_confusing_frequency_with_data_value_in_mode",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "the learner gave the frequency instead of the actual score (15)",
        "sample_answer": "the learner gave the frequency instead of the actual score (15)",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Explain that 8 is the frequency (how many learners), while the mode is the score itself (15)", "marks": 1},
        ],
        "hints": [
            "The mode is the actual data value, not the count of times it occurs.",
            "The count is 8, but the mode is 15.",
            "Answer: **the learner gave the frequency instead of the actual score (15)**.",
        ],
        "misconception_tags": ["mode_vs_frequency_confusion"],
    }


def arch_49_error_analysis_dividing_by_wrong_n_in_mean_frequency_table(rng: random.Random) -> Dict[str, Any]:
    """Diagnose dividing by number of table rows instead of total frequency."""
    prompt = (
        f"A frequency table has 5 rows representing test scores and a total frequency of $\\sum f = 30$ learners.\n"
        f"When calculating the mean, a learner divides $\\sum (f \\cdot x)$ by 5 instead of 30.\n\n"
        f"What error did the learner make?\n"
        f"State: **the learner divided by the number of categories instead of the total frequency**"
    )

    return {
        "subskill": "49_error_analysis_dividing_by_wrong_n_in_mean_frequency_table",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": "the learner divided by the number of categories instead of the total frequency",
        "sample_answer": "the learner divided by the number of categories instead of the total frequency",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": "Explain that the mean requires dividing by the sample size n = sum(f), not the number of rows/categories", "marks": 1},
        ],
        "hints": [
            "The total number of observations is the sum of frequencies ($\\sum f = 30$).",
            "Dividing by 5 divides by the number of categories, which is invalid.",
            "Answer: **the learner divided by the number of categories instead of the total frequency**.",
        ],
        "misconception_tags": ["frequency_table_sample_size_confusion"],
    }


def arch_50_compound_multi_stage_statistical_investigation_synthesis(rng: random.Random) -> Dict[str, Any]:
    """Compound synthesis: Given 5 ordered numbers, calculate mean, median, and range."""
    # Choose 5 numbers: e.g. 10, 12, 15, 18, 25
    base = rng.randint(10, 20)
    d1, d2, d3, d4 = 2, 5, 8, 15
    data = [base, base + d1, base + d2, base + d3, base + d4]
    med = data[2]
    r_val = data[4] - data[0]
    total = sum(data)
    mean_val = total / 5.0
    mean_str = f"{mean_val:.1f}".rstrip("0").rstrip(".")

    val_str = ", ".join(str(x) for x in data)

    prompt = (
        f"A learner conducts a statistical investigation on 5 observations:\n"
        f"**{val_str}**\n\n"
        f"1. Calculate the **range** ($R = \\text{{Max}} - \\text{{Min}}$).\n"
        f"2. Identify the **median** ($M$).\n"
        f"3. Calculate the **mean** ($\\bar{{x}}$).\n\n"
        f"Calculate the **sum of the range and the median** ($R + M$)."
    )

    ans = r_val + med

    return {
        "subskill": "50_compound_multi_stage_statistical_investigation_synthesis",
        "question_text": prompt,
        "prompt": prompt,
        "diagram_spec": None,
        "correct_answer": str(ans),
        "sample_answer": f"{ans} (Range = {r_val}, Median = {med}, Mean = {mean_str})",
        "tolerance": 0.0,
        "marking_schema": [
            {"step": f"Calculate range: {data[4]} - {data[0]} = {r_val}", "marks": 1},
            {"step": f"Identify median: {med}", "marks": 1},
            {"step": f"Calculate sum: {r_val} + {med} = {ans}", "marks": 1},
        ],
        "hints": [
            f"Range $= \\text{{Maximum}} - \\text{{Minimum}} = {data[4]} - {data[0]} = {r_val}$.",
            f"Median is the 3rd number: ${med}$.",
            f"Sum $= {r_val} + {med} = {ans}$.",
        ],
        "misconception_tags": ["compound_statistical_synthesis_error"],
    }
