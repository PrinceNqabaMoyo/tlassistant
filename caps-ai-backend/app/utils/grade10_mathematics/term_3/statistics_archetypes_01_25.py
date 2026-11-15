"""Grade 10 Mathematics — Term 3: Statistics Archetypes 01 to 25.
100% aligned with South African CAPS Curriculum (Grade 10 Mathematics: Statistics).
Covers:
- Qualitative vs Quantitative, Discrete vs Continuous data classification
- Measures of central tendency for ungrouped data: Mean, Median, Mode
- Missing data value from known mean or median
- Effects of arithmetic transformations (+c, *k) on central tendency
- Ungrouped frequency tables (mean, median, mode)
- Measures of dispersion: Range, Quartiles (Q1, Q3), IQR, Semi-IQR, Percentiles
- Five-number summary from raw data
- Grouped data: Class midpoints, modal class, median interval, estimated mean
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

TOPIC = "Statistics"
TOPIC_ID = "grade10_math_statistics"
LO = "math10_statistics_measures"


def _fmt_dec(val: float | int, places: int = 2) -> str:
    """Format number with South African comma decimal."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _fmt_katex(val: float | int, places: int = 2) -> str:
    """Format number for KaTeX with {,} separator."""
    dec = _fmt_dec(val, places)
    return dec.replace(",", "{,}")


# -----------------------------------------------------------------------------
# 01. Qualitative vs Quantitative classification
# -----------------------------------------------------------------------------
def arch_01_qualitative_vs_quantitative_classification(rng: random.Random) -> Dict[str, Any]:
    items_pool = [
        ("The number of learners in a Grade 10 class", "Quantitative", "It is numerical and represents a countable count."),
        ("The colours of cell phone covers owned by students", "Qualitative", "It represents descriptive categories, not numerical values."),
        ("The daily high temperature recorded in Durban", "Quantitative", "It is a numerical measurement."),
        ("Learners' favourite genre of music", "Qualitative", "It is categorical/descriptive and cannot be measured with numbers."),
        ("The height of athletes in the 100m sprint team", "Quantitative", "It represents measurable numerical values."),
        ("The names of primary languages spoken at home", "Qualitative", "It describes categories of languages, not numbers."),
        ("The shoe sizes of rugby players", "Quantitative", "Shoe sizes are numerical values."),
        ("The brands of sneakers worn by learners", "Qualitative", "Brand names are descriptive categories."),
    ]
    chosen = rng.sample(items_pool, 3)

    prompt = (
        "Classify each of the following types of data as either **Qualitative** or **Quantitative**, "
        "and provide a brief mathematical reason for each classification:\n\n"
        + "\n".join(f"{i+1}. {item[0]}" for i, item in enumerate(chosen))
    )

    worked = "\n\n".join(
        f"**{i+1}. {item[0]}:**\n- **Classification:** {item[1]}\n- **Reason:** {item[2]}"
        for i, item in enumerate(chosen)
    )
    ans = "; ".join(f"{i+1}: {item[1]}" for i, item in enumerate(chosen))

    return {
        "id": f"g10_stat_01_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "01_qualitative_vs_quantitative_classification",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": f"mp_{i+1}", "desc": f"Correct classification of {item[0][:30]}...", "marks": 1, "editable": True}
                for i, item in enumerate(chosen)
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Quantitative data consists of numbers obtained by counting or measuring.",
            "2_concept": "Qualitative data describes qualities or categories (words/labels), while quantitative data represents numerical counts or measurements.",
            "3_breakdown": f"Classifications: {ans}.",
        },
        "misconception_tags": ["data_classification_confusion"],
    }


# -----------------------------------------------------------------------------
# 02. Discrete vs Continuous identification
# -----------------------------------------------------------------------------
def arch_02_discrete_vs_continuous_identification(rng: random.Random) -> Dict[str, Any]:
    pool = [
        ("The number of text messages a teenager sends in a day", "Discrete", "Counts can only take integer values (you cannot send 4,3 messages)."),
        ("The time taken to run 400 metres in physical education", "Continuous", "Time can take any real value on a continuous scale."),
        ("The volume of petrol poured into a vehicle tank", "Continuous", "Liquid volume can be measured to any fraction of a litre."),
        ("The number of cars parked in the school parking lot", "Discrete", "Cars are counted in whole numbers."),
        ("The mass of school bags weighed to the nearest gram", "Continuous", "Mass is a measurable physical quantity with infinite possible values."),
        ("The number of goals scored by a soccer team during a tournament", "Discrete", "Goals are counted in integer units."),
    ]
    chosen = rng.sample(pool, 3)

    prompt = (
        "State whether each of the following quantitative variables is **Discrete** or **Continuous**, "
        "and justify your answer in each case:\n\n"
        + "\n".join(f"{i+1}. {c[0]}" for i, c in enumerate(chosen))
    )

    worked = "\n\n".join(
        f"**{i+1}. {c[0]}:**\n- **Type:** {c[1]}\n- **Reason:** {c[2]}"
        for i, c in enumerate(chosen)
    )
    ans = "; ".join(f"{i+1}: {c[1]}" for i, c in enumerate(chosen))

    return {
        "id": f"g10_stat_02_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "02_discrete_vs_continuous_identification",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": f"mp_{i+1}", "desc": f"Correct identification of {c[0][:30]}...", "marks": 1, "editable": True}
                for i, c in enumerate(chosen)
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Ask yourself: Is this quantity counted in whole units or measured on a continuous scale?",
            "2_concept": "Discrete variables take separate values (usually integers). Continuous variables can take any value within a range.",
            "3_breakdown": f"Answers: {ans}.",
        },
        "misconception_tags": ["discrete_vs_continuous_error"],
    }


# -----------------------------------------------------------------------------
# 03. Categorical to frequency table
# -----------------------------------------------------------------------------
def arch_03_categorical_to_frequency_table(rng: random.Random) -> Dict[str, Any]:
    categories = ["Bus", "Taxi", "Walk", "Car", "Bicycle"]
    counts = [rng.randint(3, 8) for _ in range(4)]
    chosen_cats = categories[:4]
    raw_list: List[str] = []
    for cat, cnt in zip(chosen_cats, counts):
        raw_list.extend([cat] * cnt)
    rng.shuffle(raw_list)

    total_n = len(raw_list)
    raw_display = ", ".join(raw_list)

    prompt = (
        f"A group of {total_n} Grade 10 learners were asked about their primary method of travel to school. "
        f"The responses recorded were:\n\n"
        f"{raw_display}\n\n"
        f"1. Summarise the responses in a frequency table with columns for **Mode of Transport** and **Frequency** ($f$).\n"
        f"2. State the total number of learners surveyed.\n"
        f"3. Identify the mode (most common transport method)."
    )

    modal_idx = counts.index(max(counts))
    modal_cat = chosen_cats[modal_idx]

    table_rows = "\n".join(f"| {cat} | {cnt} |" for cat, cnt in zip(chosen_cats, counts))
    worked = (
        "**1. Frequency Table:**\n\n"
        "| Mode of Transport | Frequency ($f$) |\n"
        "| :--- | :--- |\n"
        f"{table_rows}\n"
        f"| **Total** | **{total_n}** |\n\n"
        f"**2. Total learners surveyed:** $n = {total_n}$\n\n"
        f"**3. Mode:** {modal_cat} (with a frequency of {counts[modal_idx]})."
    )

    ans = f"Total={total_n}, Mode={modal_cat}"

    return {
        "id": f"g10_stat_03_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "03_categorical_to_frequency_table",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Accurate tallies for all categories in frequency table", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Correct total count n = {total_n}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct identification of mode ({modal_cat})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Count how many times each transport method appears in the list.",
            "2_concept": "The frequency is the number of times a particular category occurs. The mode is the category with the highest frequency.",
            "3_breakdown": f"Counts: {', '.join(f'{c}: {k}' for c, k in zip(chosen_cats, counts))}. Total = {total_n}. Mode = {modal_cat}.",
        },
        "misconception_tags": ["frequency_tally_counting_error"],
    }


# -----------------------------------------------------------------------------
# 04. Mean ungrouped small dataset
# -----------------------------------------------------------------------------
def arch_04_mean_ungrouped_small_dataset(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([6, 7, 8])
    target_mean = rng.randint(12, 28)
    # Generate numbers that average to target_mean
    diffs = [rng.randint(-8, 8) for _ in range(n - 1)]
    last_diff = -sum(diffs)
    if abs(last_diff) > 12:
        diffs[0] += last_diff // 2
        last_diff -= last_diff // 2
    data = [target_mean + d for d in diffs] + [target_mean + last_diff]
    rng.shuffle(data)

    data_str = ", ".join(str(x) for x in data)
    sum_x = sum(data)
    mean_val = sum_x / n
    mean_str = _fmt_katex(mean_val)

    prompt = (
        f"A group of {n} learners wrote a 30-mark class test. Their scores were:\n\n"
        f"$$\\{{{data_str}\\}}$$\n\n"
        f"Calculate the mean (average) score of the learners. Show all working using the formula "
        f"$\\bar{{x}} = \\frac{{\\sum x}}{{n}}$."
    )

    worked = (
        f"**Step 1: Calculate the sum of the data values:**\n"
        f"$$\\sum x = {' + '.join(str(x) for x in data)} = {sum_x}$$\n\n"
        f"**Step 2: Divide by the number of values ($n = {n}$):**\n"
        f"$$\\bar{{x}} = \\frac{{\\sum x}}{{n}} = \\frac{{{sum_x}}}{{{n}}} = {mean_str}$$"
    )

    return {
        "id": f"g10_stat_04_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"{_fmt_dec(mean_val)}",
        "answer_latex": rf"\bar{{x}} = {mean_str}",
        "worked_solution": worked,
        "marks": 2,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "04_mean_ungrouped_small_dataset",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct sum of values (sum = {sum_x})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct quotient / mean ({_fmt_dec(mean_val)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Add up all the test scores and divide by the number of scores.",
            "2_concept": "The mean is given by sum(x) / n.",
            "3_breakdown": f"Sum = {sum_x}, n = {n}. Mean = {sum_x}/{n} = {_fmt_dec(mean_val)}.",
        },
        "misconception_tags": ["mean_formula_denominator_error"],
    }


# -----------------------------------------------------------------------------
# 05. Median ungrouped odd n
# -----------------------------------------------------------------------------
def arch_05_median_ungrouped_odd_n(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([7, 9, 11])
    data = [rng.randint(10, 50) for _ in range(n)]
    sorted_data = sorted(data)
    mid_pos = (n + 1) // 2
    median_val = sorted_data[mid_pos - 1]

    data_str = ", ".join(str(x) for x in data)
    sorted_str = ", ".join(str(x) for x in sorted_data)

    prompt = (
        f"Consider the following set of {n} numbers:\n\n"
        f"$$\\{{{data_str}\\}}$$\n\n"
        f"1. Arrange the data in ascending order.\n"
        f"2. Determine the position of the median using the position formula $\\frac{{n + 1}}{{2}}$.\n"
        f"3. State the value of the median."
    )

    worked = (
        f"**1. Ordered data:** [{sorted_str}]\n\n"
        f"**2. Position of median:**\n"
        f"$$\\text{{Position}} = \\frac{{n + 1}}{{2}} = \\frac{{{n} + 1}}{{2}} = {mid_pos}\\text{{th value}}$$\n\n"
        f"**3. Value of median:**\n"
        f"The {mid_pos}th value in the ordered list is **{median_val}**."
    )

    return {
        "id": f"g10_stat_05_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(median_val),
        "answer_latex": rf"\text{{Median}} = {median_val}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "05_median_ungrouped_odd_n",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct ascending sort of data", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct position formula (position = {mid_pos})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct median value ({median_val})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Always sort the numbers in order from smallest to largest first.",
            "2_concept": "For an odd number of data items, the median is the single middle value located at position (n + 1)/2.",
            "3_breakdown": f"Ordered: [{sorted_str}]. The {mid_pos}th value is {median_val}.",
        },
        "misconception_tags": ["unsorted_median_error", "median_position_confusion"],
    }


# -----------------------------------------------------------------------------
# 06. Median ungrouped even n
# -----------------------------------------------------------------------------
def arch_06_median_ungrouped_even_n(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([8, 10, 12])
    data = [rng.randint(15, 60) for _ in range(n)]
    sorted_data = sorted(data)
    idx1 = (n // 2) - 1
    idx2 = n // 2
    v1 = sorted_data[idx1]
    v2 = sorted_data[idx2]
    med = (v1 + v2) / 2.0
    med_str = _fmt_katex(med)

    data_str = ", ".join(str(x) for x in data)
    sorted_str = ", ".join(str(x) for x in sorted_data)

    prompt = (
        f"Consider the following set of {n} exam marks:\n\n"
        f"$$\\{{{data_str}\\}}$$\n\n"
        f"1. Arrange the data in ascending order.\n"
        f"2. Identify the two middle values.\n"
        f"3. Calculate the median of the dataset."
    )

    worked = (
        f"**1. Ordered data:** [{sorted_str}]\n\n"
        f"**2. Middle values:**\n"
        f"Since $n = {n}$ is even, the median lies between the {n//2}th value ({v1}) and the {n//2 + 1}th value ({v2}).\n\n"
        f"**3. Median calculation:**\n"
        f"$$\\text{{Median}} = \\frac{{{v1} + {v2}}}{{2}} = \\frac{{{v1 + v2}}}{{2}} = {med_str}$$"
    )

    return {
        "id": f"g10_stat_06_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_dec(med),
        "answer_latex": rf"\text{{Median}} = {med_str}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "06_median_ungrouped_even_n",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct ascending sort of data", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Identification of two middle values ({v1} and {v2})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct median quotient ({_fmt_dec(med)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "When n is even, there is no single middle number; you must average the two central numbers.",
            "2_concept": "Sort in order, take the middle two values at indices n/2 and n/2 + 1, and compute their mean.",
            "3_breakdown": f"Middle values are {v1} and {v2}. Median = ({v1} + {v2})/2 = {_fmt_dec(med)}.",
        },
        "misconception_tags": ["even_n_median_average_omission"],
    }


# -----------------------------------------------------------------------------
# 07. Mode ungrouped unimodal bimodal
# -----------------------------------------------------------------------------
def arch_07_mode_ungrouped_unimodal_bimodal(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice(["unimodal", "bimodal", "no_mode"])
    base = [rng.randint(20, 45) for _ in range(5)]
    base = list(set(base))
    while len(base) < 5:
        base.append(rng.randint(20, 45))
        base = list(set(base))

    if scenario == "unimodal":
        m_val = base[0]
        data = base + [m_val, m_val]  # m_val appears 3 times
        ans_str = str(m_val)
        expl = f"**Mode:** {m_val} (it appears 3 times, which is more than any other value)."
    elif scenario == "bimodal":
        m1 = base[0]
        m2 = base[1]
        data = base + [m1, m2]  # m1 and m2 each appear twice, others once
        ans_str = f"{min(m1, m2)} and {max(m1, m2)}"
        expl = f"**Bimodal:** {min(m1, m2)} and {max(m1, m2)} (both appear with the highest frequency of 2)."
    else:
        data = base[:5]  # all distinct
        ans_str = "no mode"
        expl = "Each value appears exactly once, so there is **no mode**."

    rng.shuffle(data)
    data_str = ", ".join(str(x) for x in data)

    prompt = (
        f"Consider the following data set:\n\n"
        f"$$\\{{{data_str}\\}}$$\n\n"
        f"Determine the mode of the data set. State whether the data is unimodal, bimodal, or has no mode, "
        f"and explain your reasoning."
    )

    worked = f"**Analysis of frequencies:**\n{expl}"

    return {
        "id": f"g10_stat_07_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans_str,
        "answer_latex": ans_str,
        "worked_solution": worked,
        "marks": 2,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "07_mode_ungrouped_unimodal_bimodal",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 2,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct mode identification ({ans_str})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Valid mathematical reason based on frequency", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Count the frequency of each distinct number in the list.",
            "2_concept": "The mode is the number that appears most frequently. A dataset can have one mode, two modes (bimodal), or no mode.",
            "3_breakdown": expl,
        },
        "misconception_tags": ["mode_zero_vs_no_mode_confusion"],
    }


# -----------------------------------------------------------------------------
# 08. Mean median mode comparison single dataset
# -----------------------------------------------------------------------------
def arch_08_mean_median_mode_comparison_single_dataset(rng: random.Random) -> Dict[str, Any]:
    n = 7
    mode_val = rng.randint(15, 25)
    other = [mode_val + rng.choice([-6, -4, -2, 2, 4, 6]) for _ in range(4)]
    data = [mode_val, mode_val, mode_val] + other
    sorted_d = sorted(data)
    mean_val = sum(sorted_d) / n
    median_val = sorted_d[3]

    data_str = ", ".join(str(x) for x in data)
    sorted_str = ", ".join(str(x) for x in sorted_d)
    mean_str = _fmt_katex(mean_val)

    prompt = (
        f"A learner recorded the following {n} scores in a mathematics quiz:\n\n"
        f"$$\\{{{data_str}\\}}$$\n\n"
        f"1. Arrange the data in ascending order.\n"
        f"2. Calculate the mean (average), rounded to two decimal places if necessary.\n"
        f"3. Determine the median.\n"
        f"4. State the mode."
    )

    worked = (
        f"**1. Ordered data:** [{sorted_str}]\n\n"
        f"**2. Mean:**\n"
        f"$$\\bar{{x}} = \\frac{{{sum(sorted_d)}}}{{{n}}} = {mean_str}$$\n\n"
        f"**3. Median:** The 4th value in the ordered list is **{median_val}**.\n\n"
        f"**4. Mode:** The value appearing most frequently is **{mode_val}** (appears 3 times)."
    )

    ans = f"Mean={_fmt_dec(mean_val)}, Median={median_val}, Mode={mode_val}"

    return {
        "id": f"g10_stat_08_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 5,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "08_mean_median_mode_comparison_single_dataset",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Data arranged in ascending order", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Mean calculation (mean = {_fmt_dec(mean_val)})", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": f"Median identification ({median_val})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Mode identification ({mode_val})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Order the values first, then calculate sum/n, locate the middle value, and find the most frequent value.",
            "2_concept": "Mean is sum/n; Median is the middle number when sorted; Mode is the most frequent value.",
            "3_breakdown": f"Mean = {_fmt_dec(mean_val)}, Median = {median_val}, Mode = {mode_val}.",
        },
        "misconception_tags": ["central_tendency_measure_confusion"],
    }


# -----------------------------------------------------------------------------
# 09. Missing value from known mean
# -----------------------------------------------------------------------------
def arch_09_missing_value_from_known_mean(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7])
    mean_val = rng.randint(20, 40)
    total_needed = mean_val * n
    # pick n-1 numbers
    known_values = [mean_val + rng.randint(-12, 12) for _ in range(n - 1)]
    missing_val = total_needed - sum(known_values)
    while missing_val <= 0 or missing_val > 100:
        known_values = [mean_val + rng.randint(-12, 12) for _ in range(n - 1)]
        missing_val = total_needed - sum(known_values)

    data_display = known_values + ["x"]
    rng.shuffle(data_display)
    data_str = ", ".join(str(v) for v in data_display)
    sum_known = sum(known_values)

    prompt = (
        f"A set of {n} numbers has a mean of {mean_val}. The numbers are:\n\n"
        f"$$\\{{{data_str}\\}}$$\n\n"
        f"Set up an equation using the definition of the mean and solve for the unknown value $x$."
    )

    worked = (
        f"**Step 1: Write the mean equation:**\n"
        f"$$\\frac{{\\sum x}}{{n}} = \\text{{Mean}}$$\n"
        f"$$\\frac{{{sum_known} + x}}{{{n}}} = {mean_val}$$\n\n"
        f"**Step 2: Multiply both sides by {n}:**\n"
        f"$${sum_known} + x = {mean_val} \\times {n} = {total_needed}$$\n\n"
        f"**Step 3: Solve for $x$:**\n"
        f"$$x = {total_needed} - {sum_known} = {missing_val}$$"
    )

    return {
        "id": f"g10_stat_09_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(missing_val),
        "answer_latex": rf"x = {missing_val}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "09_missing_value_from_known_mean",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct equation setup: ({sum_known} + x)/{n} = {mean_val}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Total sum calculation: {total_needed}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct solution x = {missing_val}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "The total sum of all n numbers must equal n multiplied by the mean.",
            "2_concept": "Total = Mean * n. Then subtract the known numbers to find x.",
            "3_breakdown": f"Total = {n} * {mean_val} = {total_needed}. Known sum = {sum_known}. x = {total_needed} - {sum_known} = {missing_val}.",
        },
        "misconception_tags": ["missing_mean_algebraic_setup_error"],
    }


# -----------------------------------------------------------------------------
# 10. Missing value from known median
# -----------------------------------------------------------------------------
def arch_10_missing_value_from_known_median(rng: random.Random) -> Dict[str, Any]:
    # 5 numbers in ascending order: a, b, x, d, e where x is the median
    a = rng.randint(10, 20)
    b = a + rng.randint(2, 5)
    med = b + rng.randint(3, 6)
    d = med + rng.randint(2, 6)
    e = d + rng.randint(3, 8)

    prompt = (
        f"Five numbers are written in ascending order:\n\n"
        f"$${a}, \\quad {b}, \\quad x, \\quad {d}, \\quad {e}$$\n\n"
        f"1. If the median of these five numbers is {med}, determine the value of $x$.\n"
        f"2. If another number $y = {e + 5}$ is added to this dataset, state the two middle values and "
        f"calculate the new median."
    )

    new_med = (med + d) / 2.0
    new_med_str = _fmt_katex(new_med)

    worked = (
        f"**1. Value of $x$:**\n"
        f"Since the five numbers are in ascending order, the median is the 3rd value: $x = {med}$.\n\n"
        f"**2. New dataset with $y = {e + 5}$ added:**\n"
        f"Ordered data: [{a}, {b}, {med}, {d}, {e}, {e + 5}]\n"
        f"The two middle values are the 3rd ({med}) and 4th ({d}) values.\n"
        f"$$\\text{{New Median}} = \\frac{{{med} + {d}}}{{2}} = \\frac{{{med + d}}}{{2}} = {new_med_str}$$"
    )

    ans = f"x={med}, New Median={_fmt_dec(new_med)}"

    return {
        "id": f"g10_stat_10_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "10_missing_value_from_known_median",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct value of x = {med}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Identification of new middle values ({med} and {d})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct new median ({_fmt_dec(new_med)})", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "In an ordered list of 5 numbers, the 3rd number is the median.",
            "2_concept": "Adding one number increases n to 6 (even), so the new median is the mean of the 3rd and 4th numbers.",
            "3_breakdown": f"x = {med}. Middle values for 6 numbers are {med} and {d}. New median = ({med} + {d})/2 = {_fmt_dec(new_med)}.",
        },
        "misconception_tags": ["median_position_index_shift"],
    }


# -----------------------------------------------------------------------------
# 11. Effect of adding constant on central tendency
# -----------------------------------------------------------------------------
def arch_11_effect_of_adding_constant_on_central_tendency(rng: random.Random) -> Dict[str, Any]:
    old_mean = rng.randint(45, 65)
    old_med = old_mean + rng.choice([-3, -2, 2, 3])
    old_mode = old_med + rng.choice([-2, 2])
    c = rng.randint(3, 8)

    prompt = (
        f"A teacher calculates the statistics for a Grade 10 mathematics test:\n\n"
        f"- $\\text{{Mean}} = {old_mean}$\n"
        f"- $\\text{{Median}} = {old_med}$\n"
        f"- $\\text{{Mode}} = {old_mode}$\n\n"
        f"Due to an adjustment, the teacher decides to add {c} marks to every learner's score.\n\n"
        f"1. State the new mean.\n"
        f"2. State the new median.\n"
        f"3. State the new mode.\n"
        f"4. State what happens to the range of the scores."
    )

    new_mean = old_mean + c
    new_med = old_med + c
    new_mode = old_mode + c

    worked = (
        f"**1. New Mean:**\n"
        f"Adding a constant $c = {c}$ increases the mean by $c$:\n"
        f"$$\\text{{New Mean}} = {old_mean} + {c} = {new_mean}$$\n\n"
        f"**2. New Median:**\n"
        f"$$\\text{{New Median}} = {old_med} + {c} = {new_med}$$\n\n"
        f"**3. New Mode:**\n"
        f"$$\\text{{New Mode}} = {old_mode} + {c} = {new_mode}$$\n\n"
        f"**4. Effect on Range:**\n"
        f"The range remains **unchanged**, because both the maximum and minimum increase by {c}:\n"
        f"$$(\\text{{Max}} + {c}) - (\\text{{Min}} + {c}) = \\text{{Max}} - \\text{{Min}}$$"
    )

    ans = f"Mean={new_mean}, Median={new_med}, Mode={new_mode}, Range unchanged"

    return {
        "id": f"g10_stat_11_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "11_effect_of_adding_constant_on_central_tendency",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct new mean ({new_mean})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct new median ({new_med})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct new mode ({new_mode})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Statement that range is unchanged with reason", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Adding a constant shifts every score up by that amount.",
            "2_concept": "Measures of central tendency increase by c, while measures of spread (like range and IQR) remain unchanged.",
            "3_breakdown": f"New Mean = {new_mean}, New Median = {new_med}, New Mode = {new_mode}, Range is unchanged.",
        },
        "misconception_tags": ["constant_addition_range_confusion"],
    }


# -----------------------------------------------------------------------------
# 12. Effect of multiplying by constant on central tendency
# -----------------------------------------------------------------------------
def arch_12_effect_of_multiplying_by_constant_on_central_tendency(rng: random.Random) -> Dict[str, Any]:
    old_mean = rng.randint(25, 40)
    old_range = rng.randint(15, 30)
    k = rng.choice([2, 3])

    prompt = (
        f"A data set has a mean of {old_mean} and a range of {old_range}.\n\n"
        f"Every value in the data set is multiplied by {k}.\n\n"
        f"1. Determine the new mean of the data set.\n"
        f"2. Determine the new range of the data set.\n"
        f"3. Explain why the range changes when multiplying, but does not change when adding a constant."
    )

    new_mean = old_mean * k
    new_range = old_range * k

    worked = (
        f"**1. New Mean:**\n"
        f"$$\\text{{New Mean}} = k \\times \\bar{{x}} = {k} \\times {old_mean} = {new_mean}$$\n\n"
        f"**2. New Range:**\n"
        f"$$\\text{{New Range}} = k \\times \\text{{Range}} = {k} \\times {old_range} = {new_range}$$\n\n"
        f"**3. Explanation:**\n"
        f"Multiplication stretches the entire distribution: the distance between the maximum and minimum "
        f"is scaled by a factor of {k}, whereas addition merely translates the distribution along the number line."
    )

    ans = f"New Mean={new_mean}, New Range={new_range}"

    return {
        "id": f"g10_stat_12_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "12_effect_of_multiplying_by_constant_on_central_tendency",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct new mean ({new_mean})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct new range ({new_range})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Valid mathematical reasoning for scaling vs translation", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Multiplying each number by k multiplies both central tendency and spread by k.",
            "2_concept": "New Mean = k * Mean; New Range = k * Range.",
            "3_breakdown": f"New Mean = {new_mean}, New Range = {new_range}.",
        },
        "misconception_tags": ["multiplication_spread_scaling_error"],
    }


# -----------------------------------------------------------------------------
# 13. Frequency table mean ungrouped
# -----------------------------------------------------------------------------
def arch_13_frequency_table_mean_ungrouped(rng: random.Random) -> Dict[str, Any]:
    scores = [1, 2, 3, 4, 5]
    freqs = [rng.randint(2, 6) for _ in scores]
    fx = [s * f for s, f in zip(scores, freqs)]
    total_f = sum(freqs)
    total_fx = sum(fx)
    mean_val = total_fx / total_f
    mean_str = _fmt_katex(mean_val)

    rows = "\n".join(f"| {s} | {f} |" for s, f in zip(scores, freqs))

    prompt = (
        "The following frequency table records the number of goals scored per match by a school soccer team:\n\n"
        "| Goals ($x$) | Matches ($f$) |\n"
        "| :--- | :--- |\n"
        f"{rows}\n\n"
        "1. Complete an $f \\times x$ column.\n"
        "2. Calculate $\\sum f$ and $\\sum (f \\times x)$.\n"
        "3. Calculate the mean number of goals scored per match, rounded to two decimal places."
    )

    worked_rows = "\n".join(f"| {s} | {f} | {p} |" for s, f, p in zip(scores, freqs, fx))
    worked = (
        "**1. Completed calculation table:**\n\n"
        "| Goals ($x$) | Matches ($f$) | $f \\times x$ |\n"
        "| :--- | :--- | :--- |\n"
        f"{worked_rows}\n"
        f"| **Total** | **{total_f}** | **{total_fx}** |\n\n"
        f"**2. Totals:**\n"
        f"- $\\sum f = {total_f}$\n"
        f"- $\\sum (f \\times x) = {total_fx}$\n\n"
        f"**3. Mean:**\n"
        f"$$\\bar{{x}} = \\frac{{\\sum (f \\times x)}}{{\\sum f}} = \\frac{{{total_fx}}}{{{total_f}}} = {mean_str}$$"
    )

    return {
        "id": f"g10_stat_13_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_dec(mean_val),
        "answer_latex": rf"\bar{{x}} = {mean_str}",
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "13_frequency_table_mean_ungrouped",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct f * x column entries", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct sum of f ({total_f})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct sum of fx ({total_fx})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Correct mean quotient ({_fmt_dec(mean_val)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Multiply each score by its frequency to get f * x, then add them all together.",
            "2_concept": "The mean of a frequency table is sum(f * x) / sum(f).",
            "3_breakdown": f"sum(f) = {total_f}, sum(fx) = {total_fx}. Mean = {total_fx}/{total_f} = {_fmt_dec(mean_val)}.",
        },
        "misconception_tags": ["frequency_table_mean_divided_by_categories"],
    }


# -----------------------------------------------------------------------------
# 14. Frequency table median and mode ungrouped
# -----------------------------------------------------------------------------
def arch_14_frequency_table_median_and_mode_ungrouped(rng: random.Random) -> Dict[str, Any]:
    values = [2, 3, 4, 5, 6]
    freqs = [rng.randint(2, 5) for _ in values]
    # Ensure a unique mode
    mode_idx = rng.randint(0, len(values) - 1)
    freqs[mode_idx] = max(freqs) + rng.randint(2, 4)

    total_n = sum(freqs)
    # cumulative frequencies
    cum_f: List[int] = []
    running = 0
    for f in freqs:
        running += f
        cum_f.append(running)

    # find median value
    mid_pos = (total_n + 1) / 2.0
    med_val = None
    for v, cf in zip(values, cum_f):
        if cf >= mid_pos:
            med_val = v
            break

    mode_val = values[mode_idx]

    rows = "\n".join(f"| {v} | {f} |" for v, f in zip(values, freqs))

    prompt = (
        "The following frequency table shows the number of siblings reported by learners in a class:\n\n"
        "| Number of Siblings ($x$) | Number of Learners ($f$) |\n"
        "| :--- | :--- |\n"
        f"{rows}\n\n"
        "1. State the mode.\n"
        "2. Add a cumulative frequency column to locate the median position $\\frac{{n + 1}}{{2}}$.\n"
        "3. Determine the median number of siblings."
    )

    worked_rows = "\n".join(f"| {v} | {f} | {cf} |" for v, f, cf in zip(values, freqs, cum_f))
    worked = (
        f"**1. Mode:** {mode_val} (highest frequency of {freqs[mode_idx]}).\n\n"
        "**2. Cumulative Frequency Table:**\n\n"
        "| Number of Siblings ($x$) | Frequency ($f$) | Cumulative Frequency |\n"
        "| :--- | :--- | :--- |\n"
        f"{worked_rows}\n\n"
        f"Total learners: $n = {total_n}$.\n"
        f"Median position: $\\frac{{{total_n} + 1}}{{2}} = {_fmt_dec(mid_pos)}$th position.\n\n"
        f"**3. Median:** The {_fmt_dec(mid_pos)}th learner falls in the row where $x = {med_val}$ "
        f"(since cumulative frequency reaches {cum_f[values.index(med_val)]} $\\ge {_fmt_dec(mid_pos)}$). "
        f"Therefore, **Median = {med_val}**."
    )

    ans = f"Mode={mode_val}, Median={med_val}"

    return {
        "id": f"g10_stat_14_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "14_frequency_table_median_and_mode_ungrouped",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct mode identification ({mode_val})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate cumulative frequency column", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Median position calculation ({_fmt_dec(mid_pos)})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Correct median value ({med_val})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "The mode is the value with the largest frequency. The median is found using cumulative frequencies.",
            "2_concept": "Use cumulative frequencies to locate which data value contains position (n + 1)/2.",
            "3_breakdown": f"Mode = {mode_val}, Position = {_fmt_dec(mid_pos)}, Median = {med_val}.",
        },
        "misconception_tags": ["frequency_table_median_row_confusion"],
    }


# -----------------------------------------------------------------------------
# 15. Range calculation ungrouped
# -----------------------------------------------------------------------------
def arch_15_range_calculation_ungrouped(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([8, 9, 10])
    min_v = rng.randint(10, 25)
    max_v = min_v + rng.randint(25, 55)
    middle = [rng.randint(min_v + 1, max_v - 1) for _ in range(n - 2)]
    data = [min_v, max_v] + middle
    rng.shuffle(data)
    data_str = ", ".join(str(x) for x in data)
    r_val = max_v - min_v

    prompt = (
        f"Consider the following set of data values:\n\n"
        f"$$\\{{{data_str}\\}}$$\n\n"
        f"1. Identify the maximum and minimum values in the dataset.\n"
        f"2. Calculate the range of the dataset.\n"
        f"3. Explain what the range tells us about the spread of the data."
    )

    worked = (
        f"**1. Extremes:**\n"
        f"- Maximum = {max_v}\n"
        f"- Minimum = {min_v}\n\n"
        f"**2. Range calculation:**\n"
        f"$$\\text{{Range}} = \\text{{Maximum}} - \\text{{Minimum}} = {max_v} - {min_v} = {r_val}$$\n\n"
        f"**3. Interpretation:**\n"
        f"The range measures the total spread between the smallest and largest values in the distribution."
    )

    ans = f"Min={min_v}, Max={max_v}, Range={r_val}"

    return {
        "id": f"g10_stat_15_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(r_val),
        "answer_latex": rf"\text{{Range}} = {r_val}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "15_range_calculation_ungrouped",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct identification of Min ({min_v}) and Max ({max_v})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct range calculation ({r_val})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Valid interpretation of spread", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Range = Maximum - Minimum.",
            "2_concept": "Find the highest and lowest scores, then subtract the lowest from the highest.",
            "3_breakdown": f"Max = {max_v}, Min = {min_v}. Range = {max_v} - {min_v} = {r_val}.",
        },
        "misconception_tags": ["range_order_subtraction_error"],
    }


# -----------------------------------------------------------------------------
# 16. Lower quartile Q1 ungrouped
# -----------------------------------------------------------------------------
def arch_16_lower_quartile_q1_ungrouped(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([11, 13, 15])
    data = [rng.randint(12, 60) for _ in range(n)]
    sorted_d = sorted(data)
    mid = n // 2
    lower_half = sorted_d[:mid]
    m_low = len(lower_half)
    if m_low % 2 == 1:
        q1 = float(lower_half[m_low // 2])
    else:
        q1 = (lower_half[m_low // 2 - 1] + lower_half[m_low // 2]) / 2.0

    q1_str = _fmt_katex(q1)
    data_str = ", ".join(str(x) for x in data)
    sorted_str = ", ".join(str(x) for x in sorted_d)
    lower_str = ", ".join(str(x) for x in lower_half)

    prompt = (
        f"A coach recorded the training times (in seconds) of {n} athletes:\n\n"
        f"$$\\{{{data_str}\\}}$$\n\n"
        f"1. Arrange the data in ascending order.\n"
        f"2. Identify the median ($Q_2$) to separate the lower half of the data.\n"
        f"3. Calculate the lower quartile ($Q_1$)."
    )

    med = sorted_d[mid]
    worked = (
        f"**1. Ordered data:** [{sorted_str}]\n\n"
        f"**2. Median ($Q_2$):**\n"
        f"The middle value is at position {mid + 1}, which is $Q_2 = {med}$.\n"
        f"Lower half of data (below median): [{lower_str}]\n\n"
        f"**3. Lower Quartile ($Q_1$):**\n"
        f"$Q_1$ is the median of the lower half:\n"
        f"$$Q_1 = {q1_str}$$"
    )

    return {
        "id": f"g10_stat_16_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_dec(q1),
        "answer_latex": rf"Q_1 = {q1_str}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "16_lower_quartile_q1_ungrouped",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Data sorted in ascending order", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Median identification ({med})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct lower quartile Q1 ({_fmt_dec(q1)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Sort the data and find the median. Q1 is the median of the lower half of data.",
            "2_concept": "Lower quartile Q1 cuts off the lowest 25% of the data.",
            "3_breakdown": f"Ordered: [{sorted_str}]. Lower half: [{lower_str}]. Q1 = {_fmt_dec(q1)}.",
        },
        "misconception_tags": ["quartile_includes_median_error"],
    }


# -----------------------------------------------------------------------------
# 17. Upper quartile Q3 ungrouped
# -----------------------------------------------------------------------------
def arch_17_upper_quartile_q3_ungrouped(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([11, 13, 15])
    data = [rng.randint(20, 80) for _ in range(n)]
    sorted_d = sorted(data)
    mid = n // 2
    upper_half = sorted_d[mid + 1 :]
    m_up = len(upper_half)
    if m_up % 2 == 1:
        q3 = float(upper_half[m_up // 2])
    else:
        q3 = (upper_half[m_up // 2 - 1] + upper_half[m_up // 2]) / 2.0

    q3_str = _fmt_katex(q3)
    data_str = ", ".join(str(x) for x in data)
    sorted_str = ", ".join(str(x) for x in sorted_d)
    upper_str = ", ".join(str(x) for x in upper_half)

    prompt = (
        f"Consider the following set of {n} test scores:\n\n"
        f"$$\\{{{data_str}\\}}$$\n\n"
        f"1. Arrange the scores in ascending order.\n"
        f"2. Identify the median to separate the upper half of the data.\n"
        f"3. Calculate the upper quartile ($Q_3$)."
    )

    med = sorted_d[mid]
    worked = (
        f"**1. Ordered data:** [{sorted_str}]\n\n"
        f"**2. Median ($Q_2$):** $Q_2 = {med}$.\n"
        f"Upper half of data (above median): [{upper_str}]\n\n"
        f"**3. Upper Quartile ($Q_3$):**\n"
        f"$Q_3$ is the median of the upper half:\n"
        f"$$Q_3 = {q3_str}$$"
    )

    return {
        "id": f"g10_stat_17_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_dec(q3),
        "answer_latex": rf"Q_3 = {q3_str}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "17_upper_quartile_q3_ungrouped",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Data sorted in ascending order", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Median identification ({med})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct upper quartile Q3 ({_fmt_dec(q3)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Sort the data and find the median. Q3 is the median of the upper half of data.",
            "2_concept": "Upper quartile Q3 cuts off the lowest 75% (or top 25%) of the data.",
            "3_breakdown": f"Ordered: [{sorted_str}]. Upper half: [{upper_str}]. Q3 = {_fmt_dec(q3)}.",
        },
        "misconception_tags": ["upper_quartile_index_error"],
    }


# -----------------------------------------------------------------------------
# 18. Interquartile range IQR calculation
# -----------------------------------------------------------------------------
def arch_18_interquartile_range_iqr_calculation(rng: random.Random) -> Dict[str, Any]:
    q1 = rng.randint(20, 45)
    iqr = rng.randint(12, 26)
    q3 = q1 + iqr

    prompt = (
        f"A statistical analysis of the monthly rainfall figures for a town over several years yields:\n\n"
        f"- Lower quartile ($Q_1$) = {q1} mm\n"
        f"- Upper quartile ($Q_3$) = {q3} mm\n\n"
        f"1. State the formula for the Interquartile Range (IQR).\n"
        f"2. Calculate the IQR for the rainfall figures.\n"
        f"3. Explain what percentage of the rainfall observations lies within the IQR."
    )

    worked = (
        f"**1. Formula:**\n"
        f"$$\\text{{IQR}} = Q_3 - Q_1$$\n\n"
        f"**2. Calculation:**\n"
        f"$$\\text{{IQR}} = {q3} - {q1} = {iqr}\\text{{ mm}}$$\n\n"
        f"**3. Interpretation:**\n"
        f"Exactly **50%** of the observations lie between $Q_1$ and $Q_3$ (the middle 50% of the distribution)."
    )

    ans = f"IQR={iqr}, Middle 50%"

    return {
        "id": f"g10_stat_18_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(iqr),
        "answer_latex": rf"\text{{IQR}} = {iqr}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "18_interquartile_range_iqr_calculation",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of formula IQR = Q3 - Q1", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct calculation IQR = {iqr}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Statement that IQR contains 50% of the data", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Subtract Q1 from Q3 to get the interquartile range.",
            "2_concept": "IQR = Q3 - Q1, which represents the spread of the middle 50% of the data.",
            "3_breakdown": f"IQR = {q3} - {q1} = {iqr}.",
        },
        "misconception_tags": ["iqr_formula_subtraction_order"],
    }


# -----------------------------------------------------------------------------
# 19. Semi-interquartile range calculation
# -----------------------------------------------------------------------------
def arch_19_semi_interquartile_range_calculation(rng: random.Random) -> Dict[str, Any]:
    q1 = rng.randint(30, 50)
    diff = rng.choice([14, 16, 18, 20, 22])
    q3 = q1 + diff
    semi_iqr = diff / 2.0
    semi_str = _fmt_katex(semi_iqr)

    prompt = (
        f"A data set has a lower quartile of $Q_1 = {q1}$ and an upper quartile of $Q_3 = {q3}$.\n\n"
        f"1. Calculate the Interquartile Range (IQR).\n"
        f"2. Calculate the semi-interquartile range."
    )

    worked = (
        f"**1. Interquartile Range (IQR):**\n"
        f"$$\\text{{IQR}} = Q_3 - Q_1 = {q3} - {q1} = {diff}$$\n\n"
        f"**2. Semi-interquartile range:**\n"
        f"$$\\text{{Semi-IQR}} = \\frac{{\\text{{IQR}}}}{{2}} = \\frac{{{diff}}}{{2}} = {semi_str}$$"
    )

    return {
        "id": f"g10_stat_19_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_dec(semi_iqr),
        "answer_latex": rf"\text{{Semi-IQR}} = {semi_str}",
        "worked_solution": worked,
        "marks": 2,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "19_semi_interquartile_range_calculation",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 2,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct IQR = {diff}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct semi-IQR = {_fmt_dec(semi_iqr)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "The semi-interquartile range is half of the interquartile range.",
            "2_concept": "Semi-IQR = (Q3 - Q1) / 2.",
            "3_breakdown": f"IQR = {q3} - {q1} = {diff}. Semi-IQR = {diff} / 2 = {_fmt_dec(semi_iqr)}.",
        },
        "misconception_tags": ["semi_iqr_half_factor_omission"],
    }


# -----------------------------------------------------------------------------
# 20. Five-number summary from raw data
# -----------------------------------------------------------------------------
def arch_20_five_number_summary_from_raw_data(rng: random.Random) -> Dict[str, Any]:
    n = 11
    raw = [rng.randint(15, 65) for _ in range(n)]
    sorted_d = sorted(raw)
    min_v = sorted_d[0]
    max_v = sorted_d[-1]
    med = sorted_d[5]
    q1 = sorted_d[2]
    q3 = sorted_d[8]
    iqr = q3 - q1

    raw_str = ", ".join(str(x) for x in raw)
    sorted_str = ", ".join(str(x) for x in sorted_d)

    prompt = (
        f"Consider the following set of {n} marks obtained by Grade 10 learners:\n\n"
        f"$$\\{{{raw_str}\\}}$$\n\n"
        f"1. Arrange the data in ascending order.\n"
        f"2. Determine the five-number summary: Minimum, Lower Quartile ($Q_1$), Median ($Q_2$), Upper Quartile ($Q_3$), Maximum.\n"
        f"3. Calculate the Interquartile Range (IQR)."
    )

    worked = (
        f"**1. Ordered data:** [{sorted_str}]\n\n"
        f"**2. Five-Number Summary:**\n"
        f"- Minimum = {min_v}\n"
        f"- Lower Quartile ($Q_1$) = {q1}\n"
        f"- Median ($Q_2$) = {med}\n"
        f"- Upper Quartile ($Q_3$) = {q3}\n"
        f"- Maximum = {max_v}\n\n"
        f"**3. Interquartile Range:**\n"
        f"$$\\text{{IQR}} = Q_3 - Q_1 = {q3} - {q1} = {iqr}$$"
    )

    ans = f"Min={min_v}, Q1={q1}, Med={med}, Q3={q3}, Max={max_v}, IQR={iqr}"

    return {
        "id": f"g10_stat_20_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 6,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "20_five_number_summary_from_raw_data",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Data arranged in ascending order", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Minimum ({min_v}) and Maximum ({max_v})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Median Q2 = {med}", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Quartiles Q1 = {q1} and Q3 = {q3}", "marks": 2, "editable": True},
                {"id": "mp_5", "desc": f"IQR = {iqr}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Sort the data in ascending order to find min, max, median, and quartiles.",
            "2_concept": "Five-number summary consists of Min, Q1, Median, Q3, Max.",
            "3_breakdown": f"Sorted: [{sorted_str}]. Min={min_v}, Q1={q1}, Med={med}, Q3={q3}, Max={max_v}, IQR={iqr}.",
        },
        "misconception_tags": ["five_number_summary_ordering_error"],
    }


# -----------------------------------------------------------------------------
# 21. Percentiles calculation simple
# -----------------------------------------------------------------------------
def arch_21_percentiles_calculation_simple(rng: random.Random) -> Dict[str, Any]:
    n = 20
    data = sorted([rng.randint(25, 95) for _ in range(n)])
    pct = rng.choice([10, 20, 80, 90])
    pos = int(round((pct / 100.0) * (n + 1)))
    pos = max(1, min(n, pos))
    val = data[pos - 1]

    data_str = ", ".join(str(x) for x in data)

    prompt = (
        f"A list of test percentages for {n} learners is arranged in ascending order:\n\n"
        f"$$\\{{{data_str}\\}}$$\n\n"
        f"1. Use the position formula $\\text{{Position}} = \\frac{{p}}{{100}} \\times (n + 1)$ to determine the "
        f"position of the {pct}th percentile ($P_{{{pct}}}$).\n"
        f"2. State the value corresponding to the {pct}th percentile."
    )

    worked = (
        f"**1. Position formula:**\n"
        f"$$\\text{{Position}} = \\frac{{{pct}}}{{100}} \\times ({n} + 1) = \\frac{{{pct}}}{{100}} \\times 21 = {pos}\\text{{th value}}$$\n\n"
        f"**2. Value:**\n"
        f"The {pos}th value in the ordered list is **{val}**.\n"
        f"Therefore, $P_{{{pct}}} = {val}$."
    )

    return {
        "id": f"g10_stat_21_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(val),
        "answer_latex": rf"P_{{{pct}}} = {val}",
        "worked_solution": worked,
        "marks": 2,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "21_percentiles_calculation_simple",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct position calculation (position = {pos})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct percentile value ({val})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Calculate position = (p/100) * (n + 1) and read that term from the list.",
            "2_concept": "The p-th percentile is the value below which p percent of the observations fall.",
            "3_breakdown": f"Position = ({pct}/100) * 21 = {pos}. The {pos}th value is {val}.",
        },
        "misconception_tags": ["percentile_position_vs_value_confusion"],
    }


# -----------------------------------------------------------------------------
# 22. Grouped data class midpoints
# -----------------------------------------------------------------------------
def arch_22_grouped_data_class_midpoints(rng: random.Random) -> Dict[str, Any]:
    step = rng.choice([10, 20])
    start = rng.choice([0, 10, 20])
    intervals = [(start + i * step, start + (i + 1) * step) for i in range(4)]
    midpoints = [(low + high) / 2.0 for low, high in intervals]

    prompt = (
        "Consider the following grouped data intervals:\n\n"
        + "\n".join(f"{i+1}. ${low} \\le x < {high}$" for i, (low, high) in enumerate(intervals))
        + "\n\n"
        "1. State the formula used to calculate the class midpoint (class mark).\n"
        "2. Calculate the midpoint for each of the four intervals."
    )

    worked = (
        "**1. Formula:**\n"
        "$$\\text{Midpoint} = \\frac{\\text{Lower boundary} + \\text{Upper boundary}}{2}$$\n\n"
        "**2. Midpoints:**\n"
        + "\n".join(
            f"- Interval ${low} \\le x < {high}$: $\\frac{{{low} + {high}}}{{2}} = {_fmt_katex(m)}$"
            for (low, high), m in zip(intervals, midpoints)
        )
    )

    ans = ", ".join(_fmt_dec(m) for m in midpoints)

    return {
        "id": f"g10_stat_22_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "22_grouped_data_class_midpoints",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct class midpoint formula", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct midpoints for all intervals ({ans})", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Add the lower and upper limits of each interval and divide by 2.",
            "2_concept": "Class midpoint = (Lower + Upper) / 2.",
            "3_breakdown": f"Midpoints: {ans}.",
        },
        "misconception_tags": ["class_midpoint_calculation_error"],
    }


# -----------------------------------------------------------------------------
# 23. Grouped data modal class
# -----------------------------------------------------------------------------
def arch_23_grouped_data_modal_class(rng: random.Random) -> Dict[str, Any]:
    intervals = [(10, 20), (20, 30), (30, 40), (40, 50), (50, 60)]
    freqs = [rng.randint(3, 8) for _ in intervals]
    # pick one modal class with highest frequency
    modal_idx = rng.randint(1, 3)
    freqs[modal_idx] = max(freqs) + rng.randint(4, 7)

    rows = "\n".join(f"| ${low} \\le x < {high}$ | {f} |" for (low, high), f in zip(intervals, freqs))
    modal_int = intervals[modal_idx]

    prompt = (
        "The following frequency table records the ages of visitors to a community library:\n\n"
        "| Age Interval ($x$) | Frequency ($f$) |\n"
        "| :--- | :--- |\n"
        f"{rows}\n\n"
        "1. Identify the modal class interval.\n"
        "2. Explain your choice using the definition of modal class."
    )

    worked = (
        f"**1. Modal Class:** ${modal_int[0]} \\le x < {modal_int[1]}$\n\n"
        f"**2. Explanation:**\n"
        f"The modal class is the interval with the highest frequency. "
        f"Here, the interval ${modal_int[0]} \\le x < {modal_int[1]}$ has the highest frequency of {freqs[modal_idx]}."
    )

    ans = f"{modal_int[0]} <= x < {modal_int[1]}"

    return {
        "id": f"g10_stat_23_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": rf"{modal_int[0]} \le x < {modal_int[1]}",
        "worked_solution": worked,
        "marks": 2,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "23_grouped_data_modal_class",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 2,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct modal interval ({ans})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Reason based on highest frequency ({freqs[modal_idx]})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Look down the frequency column for the largest number.",
            "2_concept": "The modal class is the class interval with the greatest frequency.",
            "3_breakdown": f"Largest frequency is {freqs[modal_idx]} in interval {modal_int[0]} <= x < {modal_int[1]}.",
        },
        "misconception_tags": ["modal_class_frequency_vs_interval_confusion"],
    }


# -----------------------------------------------------------------------------
# 24. Grouped data median class interval
# -----------------------------------------------------------------------------
def arch_24_grouped_data_median_class_interval(rng: random.Random) -> Dict[str, Any]:
    intervals = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50)]
    freqs = [rng.randint(4, 9) for _ in intervals]
    total_n = sum(freqs)

    cum_f: List[int] = []
    running = 0
    for f in freqs:
        running += f
        cum_f.append(running)

    half_n = total_n / 2.0
    med_int = None
    for (low, high), cf in zip(intervals, cum_f):
        if cf >= half_n:
            med_int = (low, high)
            break

    rows = "\n".join(f"| ${low} \\le x < {high}$ | {f} |" for (low, high), f in zip(intervals, freqs))

    prompt = (
        "The following frequency table shows the marks of learners in a test:\n\n"
        "| Mark Interval | Frequency ($f$) |\n"
        "| :--- | :--- |\n"
        f"{rows}\n\n"
        f"1. Calculate the total number of learners ($n$).\n"
        f"2. Add a cumulative frequency column to find the interval containing the median mark ($n / 2$ position).\n"
        f"3. State the median class interval."
    )

    worked_rows = "\n".join(f"| ${low} \\le x < {high}$ | {f} | {cf} |" for (low, high), f, cf in zip(intervals, freqs, cum_f))
    worked = (
        f"**1. Total learners:** $n = {total_n}$\n\n"
        "**2. Cumulative Frequency Table:**\n\n"
        "| Mark Interval | Frequency ($f$) | Cumulative Frequency |\n"
        "| :--- | :--- | :--- |\n"
        f"{worked_rows}\n\n"
        f"Median position: $\\frac{{n}}{{2}} = \\frac{{{total_n}}}{{2}} = {_fmt_dec(half_n)}$th position.\n\n"
        f"**3. Median Class Interval:**\n"
        f"The {_fmt_dec(half_n)}th learner falls in the interval **${med_int[0]} \\le x < {med_int[1]}$**."
    )

    ans = f"{med_int[0]} <= x < {med_int[1]}"

    return {
        "id": f"g10_stat_24_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": rf"{med_int[0]} \le x < {med_int[1]}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "24_grouped_data_median_class_interval",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct total count n = {total_n}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Accurate cumulative frequency calculation", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct median class interval ({ans})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Find half of the total frequency (n/2), then use cumulative frequencies to see which interval contains that count.",
            "2_concept": "The median class is the first interval where the cumulative frequency is greater than or equal to n/2.",
            "3_breakdown": f"Total n = {total_n}, half = {_fmt_dec(half_n)}. Interval is {ans}.",
        },
        "misconception_tags": ["median_interval_cumulative_misalignment"],
    }


# -----------------------------------------------------------------------------
# 25. Grouped data estimated mean
# -----------------------------------------------------------------------------
def arch_25_grouped_data_estimated_mean(rng: random.Random) -> Dict[str, Any]:
    intervals = [(0, 10), (10, 20), (20, 30), (30, 40)]
    freqs = [rng.randint(3, 8) for _ in intervals]
    midpoints = [(low + high) / 2.0 for low, high in intervals]
    fm = [f * m for f, m in zip(freqs, midpoints)]

    sum_f = sum(freqs)
    sum_fm = sum(fm)
    est_mean = sum_fm / sum_f
    est_mean_str = _fmt_katex(est_mean)

    rows = "\n".join(f"| ${low} \\le x < {high}$ | {f} |" for (low, high), f in zip(intervals, freqs))

    prompt = (
        "The table below shows the time (in minutes) taken by learners to travel to school:\n\n"
        "| Time Interval | Frequency ($f$) |\n"
        "| :--- | :--- |\n"
        f"{rows}\n\n"
        "1. Complete columns for the class midpoints ($m$) and $f \\times m$.\n"
        "2. Calculate $\\sum f$ and $\\sum (f \\times m)$.\n"
        "3. Calculate the estimated mean travel time, rounded to two decimal places."
    )

    worked_rows = "\n".join(
        f"| ${low} \\le x < {high}$ | {f} | {_fmt_katex(m)} | {_fmt_katex(p)} |"
        for (low, high), f, m, p in zip(intervals, freqs, midpoints, fm)
    )
    worked = (
        "**1. Calculation Table:**\n\n"
        "| Time Interval | Frequency ($f$) | Midpoint ($m$) | $f \\times m$ |\n"
        "| :--- | :--- | :--- | :--- |\n"
        f"{worked_rows}\n"
        f"| **Total** | **{sum_f}** | — | **{_fmt_katex(sum_fm)}** |\n\n"
        f"**2. Totals:**\n"
        f"- $\\sum f = {sum_f}$\n"
        f"- $\\sum (f \\times m) = {_fmt_katex(sum_fm)}$\n\n"
        f"**3. Estimated Mean:**\n"
        f"$$\\bar{{x}} \\approx \\frac{{\\sum (f \\times m)}}{{\\sum f}} = \\frac{{{_fmt_katex(sum_fm)}}}{{{sum_f}}} = {est_mean_str}$$"
    )

    return {
        "id": f"g10_stat_25_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_dec(est_mean),
        "answer_latex": rf"\bar{{x}} \approx {est_mean_str}",
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "25_grouped_data_estimated_mean",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct midpoints (m) column", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Correct f * m products column", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct sum of f ({sum_f}) and sum of fm ({_fmt_dec(sum_fm)})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Correct estimated mean ({_fmt_dec(est_mean)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Find the midpoint of each interval, multiply by frequency, and divide the total by sum of frequencies.",
            "2_concept": "Estimated mean = sum(f * m) / sum(f).",
            "3_breakdown": f"sum(f) = {sum_f}, sum(fm) = {_fmt_dec(sum_fm)}. Estimated mean = {_fmt_dec(est_mean)}.",
        },
        "misconception_tags": ["estimated_mean_boundary_instead_of_midpoint"],
    }
