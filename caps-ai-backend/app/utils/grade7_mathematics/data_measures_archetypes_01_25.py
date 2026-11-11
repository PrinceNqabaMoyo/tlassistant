"""Grade 7 Mathematics - Interpret, Analyse and Report on Data: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 4/01. Interpret analyse and report on data.md
Focus: Measures of central tendency (mean, median, mode), measures of spread (range), extreme values (outliers), population vs sample, frequency tables, and bar graph interpretations with clean SVGs.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_bar_graph(labels: List[str], values: List[int], title: str, y_label: str = "Learners") -> str:
    """Renders a clean static 2D SVG vertical bar graph."""
    w, h = 340, 220
    max_v = max(values) if values else 10
    scale_y = 130 / max_v if max_v > 0 else 1

    bars = []
    n = len(labels)
    bar_w = min(36, int(220 / (n * 1.5)))
    gap = int(220 / n)

    for i, (lab, val) in enumerate(zip(labels, values)):
        bx = 55 + i * gap
        bh = int(val * scale_y)
        by = 170 - bh
        bars.append(f'<rect x="{bx}" y="{by}" width="{bar_w}" height="{bh}" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5"/>')
        bars.append(f'<text x="{bx + bar_w // 2}" y="{by - 4}" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e3a8a">{val}</text>')
        bars.append(f'<text x="{bx + bar_w // 2}" y="185" text-anchor="middle" font-size="10" fill="#475569">{lab}</text>')

    # Axis lines
    axes = [
        '<line x1="45" y1="30" x2="45" y2="170" stroke="#64748b" stroke-width="1.5"/>',
        '<line x1="45" y1="170" x2="310" y2="170" stroke="#64748b" stroke-width="1.5"/>',
        f'<text x="170" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">{title}</text>',
        f'<text x="15" y="100" text-anchor="middle" font-size="10" fill="#64748b" transform="rotate(-90 15 100)">{y_label}</text>'
    ]

    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'{"".join(axes)}{"".join(bars)}'
        f'</svg>'
    )


# 01. Calculate mean integer dataset
def arch_01_calculate_mean_integer_dataset(rng: random.Random) -> Dict[str, Any]:
    n = rng.choice([5, 6, 7])
    target_mean = rng.randint(14, 25)
    base_vals = [target_mean + rng.randint(-5, 5) for _ in range(n - 1)]
    rem = (target_mean * n) - sum(base_vals)
    vals = base_vals + [rem]
    rng.shuffle(vals)
    vals_str = ", ".join(str(x) for x in vals)
    total_sum = sum(vals)
    ans = f"{target_mean}"
    prompt = (
        f"A learner recorded the daily mathematics quiz scores of a study group:\n\n"
        f"$$\\{{ {vals_str} \\}}$$\n\n"
        f"Calculate the **arithmetic mean** score for this dataset."
    )
    sol = (
        f"**Step 1: Formula for Mean:**\n"
        f"$$\\text{{Mean}} = \\frac{{\\text{{Sum of all scores}}}}{{\\text{{Number of scores (n)}}}}$$\n\n"
        f"**Step 2: Calculate sum:**\n"
        f"$$\\text{{Sum}} = {' + '.join(str(x) for x in vals)} = {total_sum}$$\n\n"
        f"**Step 3: Divide by count $n = {n}$:**\n"
        f"$$\\text{{Mean}} = \\frac{{{total_sum}}}{{{n}}} = {target_mean}$$"
    )
    return {
        "id": f"g7_dm_01_{rng.randint(100000, 999999)}",
        "subskill": "01_calculate_mean_integer_dataset",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{target_mean}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_01",
        "hints": {
            "tier_1": f"Add all {n} numbers together and divide by {n}.",
            "tier_2": f"Sum = {total_sum}. Divide by {n}.",
            "tier_3": f"Mean = {target_mean}."
        },
        "misconception_tags": ["dividing_by_wrong_count"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates sum = {total_sum}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Divides by {n} to get mean = {target_mean}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 02. Calculate mean formula and definition
def arch_02_calculate_mean_formula_and_definition(rng: random.Random) -> Dict[str, Any]:
    ans = "Mean = (Sum of all data values) / (Total number of data values); it represents the balance point / average"
    prompt = (
        "In statistics, state the formula for the **arithmetic mean** and explain what the mean represents "
        "in terms of the distribution of a dataset."
    )
    sol = (
        "**Definition & Formula:**\n"
        "The arithmetic mean (average) is calculated by adding all the values in a dataset and dividing the total by the number of values:\n"
        "$$\\text{Mean} = \\frac{\\text{Sum of all values}}{\\text{Total number of values}} = \\frac{\\sum x}{n}$$\n\n"
        "**Statistical Interpretation:**\n"
        "The mean represents the 'balance point' of the data. If all data items were shared out equally among all participants, "
        "each would receive the mean value."
    )
    return {
        "id": f"g7_dm_02_{rng.randint(100000, 999999)}",
        "subskill": "02_calculate_mean_formula_and_definition",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Sum of values divided by count of values; represents the equal share or balance point",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_02",
        "hints": {
            "tier_1": "Think about how you find your average term mark.",
            "tier_2": "Add everything up and divide by how many items there are.",
            "tier_3": "Formula: Sum / Count. It represents the equal share or balance point."
        },
        "misconception_tags": ["confusing_mean_with_median"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States formula: Sum of values / total count", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains balance point / equal sharing concept", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 03. Calculate mean with decimal result
def arch_03_calculate_mean_with_decimal_result(rng: random.Random) -> Dict[str, Any]:
    n = 4
    vals = [rng.randint(11, 23) for _ in range(n)]
    total_sum = sum(vals)
    mean_val = round(total_sum / n, 2)
    mean_str = str(mean_val).replace(".", "{,}")
    vals_str = ", ".join(str(x) for x in vals)
    ans = f"{mean_str}"
    prompt = (
        f"Four friends ran a $100\\text{{ m}}$ sprint and recorded their times in seconds:\n\n"
        f"$$\\{{ {vals_str} \\}}$$\n\n"
        f"Calculate the mean sprint time. Give your answer with a South African decimal comma to one or two decimal places."
    )
    sol = (
        f"**Step 1: Calculate total time:**\n"
        f"$$\\text{{Sum}} = {' + '.join(str(x) for x in vals)} = {total_sum}$$\n\n"
        f"**Step 2: Divide by $n = {n}$:**\n"
        f"$$\\text{{Mean}} = \\frac{{{total_sum}}}{{{n}}} = {mean_str}\\text{{ seconds}}$$"
    )
    return {
        "id": f"g7_dm_03_{rng.randint(100000, 999999)}",
        "subskill": "03_calculate_mean_with_decimal_result",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{mean_str} seconds",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_03",
        "hints": {
            "tier_1": f"Sum = {total_sum}.",
            "tier_2": f"Divide {total_sum} by {n}.",
            "tier_3": f"Mean is {mean_str}."
        },
        "misconception_tags": ["decimal_division_rounding_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates sum = {total_sum}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates mean = {mean_str}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 04. Calculate mean find missing value
def arch_04_calculate_mean_find_missing_value(rng: random.Random) -> Dict[str, Any]:
    n = 5
    known_count = 4
    target_mean = rng.randint(60, 80)
    total_needed = target_mean * n
    known_vals = [target_mean + rng.randint(-12, 12) for _ in range(known_count)]
    missing_val = total_needed - sum(known_vals)
    known_str = ", ".join(f"{x}\\%" for x in known_vals)
    ans = f"{missing_val}%"
    prompt = (
        f"Thabo wrote $5$ class tests. His first $4$ test marks were:\n\n"
        f"$$\\{{ {known_str} \\}}$$\n\n"
        f"If Thabo wants to achieve an overall mean mark of **{target_mean}\\%** across all $5$ tests, "
        f"what mark must he obtain on his fifth test?"
    )
    sum_known = sum(known_vals)
    sol = (
        f"**Step 1: Calculate total marks required for 5 tests:**\n"
        f"$$\\text{{Total Required}} = \\text{{Mean}} \\times n = {target_mean} \\times 5 = {total_needed}$$\n\n"
        f"**Step 2: Sum the first 4 known marks:**\n"
        f"$$\\text{{Current Total}} = {' + '.join(str(x) for x in known_vals)} = {sum_known}$$\n\n"
        f"**Step 3: Subtract to find the required fifth mark:**\n"
        f"$$\\text{{Fifth Mark}} = {total_needed} - {sum_known} = {missing_val}\\%$$"
    )
    return {
        "id": f"g7_dm_04_{rng.randint(100000, 999999)}",
        "subskill": "04_calculate_mean_find_missing_value",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{missing_val}%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_04",
        "hints": {
            "tier_1": f"To get an average of {target_mean} across 5 tests, what is the grand total needed?",
            "tier_2": f"Grand total = 5 × {target_mean} = {total_needed}. Sum of 4 tests = {sum_known}.",
            "tier_3": f"Required mark = {total_needed} - {sum_known} = {missing_val}%."
        },
        "misconception_tags": ["subtracting_from_mean_instead_of_total_sum"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates total required sum = {total_needed}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates current sum = {sum_known}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Finds missing test mark = {missing_val}%", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


# 05. Calculate mean word problem temperatures
def arch_05_calculate_mean_word_problem_temperatures(rng: random.Random) -> Dict[str, Any]:
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    temps = [rng.randint(18, 30) for _ in days]
    total_temp = sum(temps)
    mean_temp = round(total_temp / len(days), 1)
    mean_str = str(mean_temp).replace(".", "{,}")
    pairs_str = ", ".join(f"{d}: {t}^\\circ\\text{{C}}" for d, t in zip(days, temps))
    ans = f"{mean_str} °C"
    prompt = (
        f"The maximum temperatures in Polokwane were recorded from Monday to Friday:\n\n"
        f"$$\\{{ {pairs_str} \\}}$$\n\n"
        f"Calculate the mean maximum temperature for this 5-day school week."
    )
    sol = (
        f"**Step 1: Calculate total sum of temperatures:**\n"
        f"$$\\text{{Sum}} = {' + '.join(str(x) for x in temps)} = {total_temp}^\\circ\\text{{C}}$$\n\n"
        f"**Step 2: Divide by the number of days ($n = 5$):**\n"
        f"$$\\text{{Mean Temperature}} = \\frac{{{total_temp}}}{{5}} = {mean_str}^\\circ\\text{{C}}$$"
    )
    return {
        "id": f"g7_dm_05_{rng.randint(100000, 999999)}",
        "subskill": "05_calculate_mean_word_problem_temperatures",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{mean_str} °C",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_05",
        "hints": {
            "tier_1": f"Add the 5 temperatures together: {total_temp}.",
            "tier_2": f"Divide {total_temp} by 5.",
            "tier_3": f"Mean is {mean_str} °C."
        },
        "misconception_tags": ["omitting_units_in_temperature_mean"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates sum = {total_temp}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates mean = {mean_str} °C", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 06. Calculate median odd count dataset
def arch_06_calculate_median_odd_count_dataset(rng: random.Random) -> Dict[str, Any]:
    n = 7
    raw_vals = [rng.randint(10, 40) for _ in range(n)]
    sorted_vals = sorted(raw_vals)
    median_val = sorted_vals[n // 2]
    raw_str = ", ".join(str(x) for x in raw_vals)
    sorted_str = ", ".join(str(x) for x in sorted_vals)
    ans = f"{median_val}"
    prompt = (
        f"Consider the following set of raw marks:\n\n"
        f"$$\\{{ {raw_str} \\}}$$\n\n"
        f"1. Arrange the data in ascending order.\n"
        f"2. Determine the **median** mark."
    )
    sol = (
        f"**Step 1: Arrange data in ascending order:**\n"
        f"$$\\{{ {sorted_str} \\}}$$\n\n"
        f"**Step 2: Identify the middle value:**\n"
        f"Since $n = {n}$ is an odd number, the median is the value at position $\\frac{{{n} + 1}}{{2}} = 4$:\n"
        f"$$\\text{{Median}} = {median_val}$$"
    )
    return {
        "id": f"g7_dm_06_{rng.randint(100000, 999999)}",
        "subskill": "06_calculate_median_odd_count_dataset",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Sorted: {sorted_str}; Median = {median_val}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_06",
        "hints": {
            "tier_1": "You must sort the numbers from smallest to largest first!",
            "tier_2": f"Sorted list: {sorted_str}. Look at the 4th number.",
            "tier_3": f"Median is {median_val}."
        },
        "misconception_tags": ["finding_median_without_sorting"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Arranges in ascending order: {sorted_str}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Identifies middle value = {median_val}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 07. Calculate median even count dataset
def arch_07_calculate_median_even_count_dataset(rng: random.Random) -> Dict[str, Any]:
    n = 6
    raw_vals = [rng.randint(10, 50) for _ in range(n)]
    sorted_vals = sorted(raw_vals)
    m1, m2 = sorted_vals[2], sorted_vals[3]
    med_val = (m1 + m2) / 2
    med_str = str(med_val).replace(".0", "").replace(".", "{,}")
    raw_str = ", ".join(str(x) for x in raw_vals)
    sorted_str = ", ".join(str(x) for x in sorted_vals)
    ans = f"{med_str}"
    prompt = (
        f"Six runners recorded their race completion times in minutes:\n\n"
        f"$$\\{{ {raw_str} \\}}$$\n\n"
        f"1. Arrange the times in ascending order.\n"
        f"2. Explain how to find the median when the number of values $n$ is even.\n"
        f"3. Calculate the median time."
    )
    sol = (
        f"**Step 1: Order the data ascending:**\n"
        f"$$\\{{ {sorted_str} \\}}$$\n\n"
        f"**Step 2: Rule for even $n$:**\n"
        f"When $n = {n}$ is even, there is no single middle number. "
        f"We find the two middle numbers (at positions $3$ and $4$) and calculate their average (mean).\n\n"
        f"**Step 3: Calculate median:**\n"
        f"The two middle numbers are ${m1}$ and ${m2}$:\n"
        f"$$\\text{{Median}} = \\frac{{{m1} + {m2}}}{{2}} = \\frac{{{m1 + m2}}}{{2}} = {med_str}\\text{{ minutes}}$$"
    )
    return {
        "id": f"g7_dm_07_{rng.randint(100000, 999999)}",
        "subskill": "07_calculate_median_even_count_dataset",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Ordered: {sorted_str}; average of {m1} and {m2} is {med_str}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_07",
        "hints": {
            "tier_1": "Order the 6 numbers. The two in the middle are at positions 3 and 4.",
            "tier_2": f"Middle numbers are {m1} and {m2}. Add them and divide by 2.",
            "tier_3": f"Median = ({m1} + {m2}) / 2 = {med_str}."
        },
        "misconception_tags": ["picking_only_one_middle_number_for_even_n"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Orders data ascending: {sorted_str}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Identifies two middle numbers {m1} and {m2}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculates average = {med_str}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 08. Calculate median unordered list sorting
def arch_08_calculate_median_unordered_list_sorting(rng: random.Random) -> Dict[str, Any]:
    vals = [28, 14, 35, 12, 19, 22, 31]
    sorted_vals = sorted(vals)
    median_val = sorted_vals[len(vals) // 2]
    ans = f"{median_val}"
    prompt = (
        f"Find the median of the following set of numbers:\n\n"
        f"$$28;\\; 14;\\; 35;\\; 12;\\; 19;\\; 22;\\; 31$$\n\n"
        f"Show your ordered list clearly."
    )
    sorted_str = "; ".join(str(x) for x in sorted_vals)
    sol = (
        f"**Step 1: Arrange in ascending order:**\n"
        f"$${sorted_str}$$\n\n"
        f"**Step 2: Find the middle value ($4$th position out of $7$):**\n"
        f"$$\\text{{Median}} = {median_val}$$"
    )
    return {
        "id": f"g7_dm_08_{rng.randint(100000, 999999)}",
        "subskill": "08_calculate_median_unordered_list_sorting",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Ordered: {sorted_str}; Median = {median_val}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_08",
        "hints": {
            "tier_1": "Smallest is 12, largest is 35.",
            "tier_2": f"Sorted order: {sorted_str}.",
            "tier_3": f"Median is {median_val}."
        },
        "misconception_tags": ["picking_middle_without_sorting"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Writes correctly ordered list", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Selects median = {median_val}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 09. Calculate median test scores word problem
def arch_09_calculate_median_test_scores_word_problem(rng: random.Random) -> Dict[str, Any]:
    scores = [rng.randint(45, 95) for _ in range(5)]
    sorted_scores = sorted(scores)
    med = sorted_scores[2]
    scores_str = ", ".join(f"{s}\\%" for s in scores)
    ans = f"{med}%"
    prompt = (
        f"Five learners wrote an EMS diagnostic test and obtained the following percentage scores:\n\n"
        f"$$\\{{ {scores_str} \\}}$$\n\n"
        f"Determine the **median score** for this group."
    )
    sorted_str = ", ".join(f"{s}\\%" for s in sorted_scores)
    sol = (
        f"**Step 1: Order scores from lowest to highest:**\n"
        f"$$\\{{ {sorted_str} \\}}$$\n\n"
        f"**Step 2: Locate the middle score:**\n"
        f"The 3rd score out of 5 is ${med}\\%$.\n\n"
        f"$$\\therefore \\text{{Median}} = {med}\\%$$"
    )
    return {
        "id": f"g7_dm_09_{rng.randint(100000, 999999)}",
        "subskill": "09_calculate_median_test_scores_word_problem",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{med}%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_09",
        "hints": {
            "tier_1": "Sort the 5 percentages from smallest to largest.",
            "tier_2": f"Sorted: {sorted_str}.",
            "tier_3": f"Median is {med}%."
        },
        "misconception_tags": ["finding_median_without_sorting"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Orders scores ascending", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Identifies median = {med}%", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 10. Calculate mode single most frequent
def arch_10_calculate_mode_single_most_frequent(rng: random.Random) -> Dict[str, Any]:
    mode_val = rng.randint(12, 25)
    other_vals = [mode_val + rng.choice([-4, -3, -2, 2, 3, 4]) for _ in range(4)]
    dataset = [mode_val, mode_val, mode_val] + other_vals
    rng.shuffle(dataset)
    dataset_str = ", ".join(str(x) for x in dataset)
    ans = f"{mode_val}"
    prompt = (
        f"Consider the following set of data values:\n\n"
        f"$$\\{{ {dataset_str} \\}}$$\n\n"
        f"1. Define what the **mode** of a dataset is.\n"
        f"2. State the mode of this dataset and its frequency."
    )
    sol = (
        f"**1. Definition of Mode:**\n"
        f"The mode is the data value that appears most frequently in a dataset.\n\n"
        f"**2. Mode Identification:**\n"
        f"In this dataset, the number **{mode_val}** appears $3$ times, which is more frequent than any other value.\n\n"
        f"$$\\therefore \\text{{Mode}} = {mode_val} \\text{{ (frequency = 3)}}$$"
    )
    return {
        "id": f"g7_dm_10_{rng.randint(100000, 999999)}",
        "subskill": "10_calculate_mode_single_most_frequent",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Mode = {mode_val} (appears 3 times)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_10",
        "hints": {
            "tier_1": "Which number appears more times than any other number?",
            "tier_2": f"Count the frequency of each value. {mode_val} occurs 3 times.",
            "tier_3": f"Mode = {mode_val}."
        },
        "misconception_tags": ["confusing_mode_with_frequency_count"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Defines mode as most frequent value", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Identifies mode = {mode_val}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 11. Calculate mode bimodal dataset
def arch_11_calculate_mode_bimodal_dataset(rng: random.Random) -> Dict[str, Any]:
    m1 = rng.randint(10, 20)
    m2 = rng.randint(25, 35)
    others = [rng.randint(36, 45), rng.randint(46, 55)]
    dataset = [m1, m1, m2, m2] + others
    rng.shuffle(dataset)
    dataset_str = ", ".join(str(x) for x in dataset)
    ans = f"{min(m1, m2)} and {max(m1, m2)} (Bimodal)"
    prompt = (
        f"A survey recorded the shoe sizes of a sports squad:\n\n"
        f"$$\\{{ {dataset_str} \\}}$$\n\n"
        f"1. How many modes does this dataset have, and what are their values?\n"
        f"2. What statistical term is used to describe a dataset with two modes?"
    )
    sol = (
        f"**1. Modes:**\n"
        f"Both **{m1}** and **{m2}** appear $2$ times each, which is the highest frequency in the dataset.\n"
        f"Therefore, the modes are **{min(m1, m2)}** and **{max(m1, m2)}**.\n\n"
        f"**2. Statistical Term:**\n"
        f"A dataset with two modes is called **bimodal**."
    )
    return {
        "id": f"g7_dm_11_{rng.randint(100000, 999999)}",
        "subskill": "11_calculate_mode_bimodal_dataset",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Modes: {min(m1, m2)} and {max(m1, m2)}; term: Bimodal",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_11",
        "hints": {
            "tier_1": "Can a dataset have more than one mode if two numbers tie for highest frequency?",
            "tier_2": f"Yes. Both {m1} and {m2} appear twice.",
            "tier_3": f"Modes are {min(m1, m2)} and {max(m1, m2)}; it is bimodal."
        },
        "misconception_tags": ["assuming_only_one_mode_exists"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Identifies both modes {min(m1, m2)} and {max(m1, m2)}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Uses the term bimodal", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 12. Calculate mode no mode dataset
def arch_12_calculate_mode_no_mode_dataset(rng: random.Random) -> Dict[str, Any]:
    dataset = [14, 18, 22, 27, 31, 39]
    dataset_str = ", ".join(str(x) for x in dataset)
    ans = "No mode (all values appear with equal frequency of 1)"
    prompt = (
        f"Determine the mode of the following dataset:\n\n"
        f"$$\\{{ {dataset_str} \\}}$$\n\n"
        f"If no mode exists, explain why."
    )
    sol = (
        "**Analysis:**\n"
        "Each value in the dataset appears exactly once.\n"
        "No single number appears more frequently than any other.\n\n"
        "$$\\therefore \\text{There is no mode}$$"
    )
    return {
        "id": f"g7_dm_12_{rng.randint(100000, 999999)}",
        "subskill": "12_calculate_mode_no_mode_dataset",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "No mode, because each value appears only once",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_12",
        "hints": {
            "tier_1": "Does any number repeat?",
            "tier_2": "Every number occurs once. None has a higher frequency.",
            "tier_3": "There is no mode."
        },
        "misconception_tags": ["stating_zero_as_mode_when_none_exists"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States No mode", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains all values have equal frequency", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 13. Calculate mode categorical survey data
def arch_13_calculate_mode_categorical_survey_data(rng: random.Random) -> Dict[str, Any]:
    categories = ["Soccer", "Netball", "Rugby", "Cricket"]
    counts = [18, 12, 14, 8]
    ans = "Soccer (frequency = 18)"
    prompt = (
        "In a survey of favorite sports among Grade 7 learners, the results were:\n\n"
        "- Soccer: $18$\n"
        "- Netball: $12$\n"
        "- Rugby: $14$\n"
        "- Cricket: $8$\n\n"
        "1. Can we calculate a mean for this categorical data? Explain.\n"
        "2. What is the modal sport (mode) of this survey?"
    )
    sol = (
        "**1. Mean for Categorical Data:**\n"
        "No, we cannot calculate a numerical mean because the data categories are qualitative words (sports names), not numbers that can be added together.\n\n"
        "**2. Modal Sport:**\n"
        "The category with the highest frequency ($18$ votes) is **Soccer**.\n\n"
        "$$\\therefore \\text{Mode} = \\text{Soccer}$$"
    )
    return {
        "id": f"g7_dm_13_{rng.randint(100000, 999999)}",
        "subskill": "13_calculate_mode_categorical_survey_data",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "No mean for words; Modal sport is Soccer (18 votes)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_13",
        "hints": {
            "tier_1": "You cannot add 'Soccer' and 'Rugby'. But you can see which has the most votes.",
            "tier_2": "Soccer has 18 votes, which is the highest count.",
            "tier_3": "Cannot calculate mean for words. Mode is Soccer."
        },
        "misconception_tags": ["attempting_mean_on_categorical_labels"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Explains mean cannot be calculated for categorical data", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identifies Soccer as modal sport", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 14. Calculate range spread of data
def arch_14_calculate_range_spread_of_data(rng: random.Random) -> Dict[str, Any]:
    min_v = rng.randint(12, 18)
    max_v = rng.randint(45, 68)
    others = [rng.randint(min_v + 2, max_v - 2) for _ in range(4)]
    vals = [min_v, max_v] + others
    rng.shuffle(vals)
    vals_str = ", ".join(str(x) for x in vals)
    r = max_v - min_v
    ans = f"{r}"
    prompt = (
        f"Consider the dataset:\n\n"
        f"$$\\{{ {vals_str} \\}}$$\n\n"
        f"1. State the formula for the **range** of a dataset.\n"
        f"2. Calculate the range of this dataset."
    )
    sol = (
        f"**1. Formula for Range:**\n"
        f"$$\\text{{Range}} = \\text{{Highest value}} - \\text{{Lowest value}}$$\n\n"
        f"**2. Calculation:**\n"
        f"- Highest value: ${max_v}$\n"
        f"- Lowest value: ${min_v}$\n\n"
        f"$$\\text{{Range}} = {max_v} - {min_v} = {r}$$"
    )
    return {
        "id": f"g7_dm_14_{rng.randint(100000, 999999)}",
        "subskill": "14_calculate_range_spread_of_data",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Range = {max_v} - {min_v} = {r}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_14",
        "hints": {
            "tier_1": "Find the biggest number and subtract the smallest number.",
            "tier_2": f"Highest = {max_v}, Lowest = {min_v}.",
            "tier_3": f"Range = {max_v} - {min_v} = {r}."
        },
        "misconception_tags": ["adding_instead_of_subtracting_for_range"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States formula Range = Maximum - Minimum", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates range = {r}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 15. Calculate range temperature extremes
def arch_15_calculate_range_temperature_extremes(rng: random.Random) -> Dict[str, Any]:
    min_temp = rng.randint(4, 11)
    max_temp = rng.randint(24, 34)
    r = max_temp - min_temp
    ans = f"{r} °C"
    prompt = (
        f"In Sutherland, the minimum overnight temperature dropped to ${min_temp}^\\circ\\text{{C}}$, "
        f"while the daytime maximum reached ${max_temp}^\\circ\\text{{C}}$.\n\n"
        f"Calculate the **temperature range** for Sutherland on that day."
    )
    sol = (
        f"**Step 1: Formula:**\n"
        f"$$\\text{{Range}} = \\text{{Maximum Temperature}} - \\text{{Minimum Temperature}}$$\n\n"
        f"**Step 2: Calculate:**\n"
        f"$$\\text{{Range}} = {max_temp}^\\circ\\text{{C}} - {min_temp}^\\circ\\text{{C}} = {r}^\\circ\\text{{C}}$$"
    )
    return {
        "id": f"g7_dm_15_{rng.randint(100000, 999999)}",
        "subskill": "15_calculate_range_temperature_extremes",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{r} °C",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_15",
        "hints": {
            "tier_1": f"Subtract {min_temp} from {max_temp}.",
            "tier_2": f"{max_temp} - {min_temp} = {r}.",
            "tier_3": f"Range is {r} °C."
        },
        "misconception_tags": ["omitting_units_in_range"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Subtracts minimum from maximum", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"States range = {r} °C", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 16. Data extremes outliers identification
def arch_16_data_extremes_outliers_identification(rng: random.Random) -> Dict[str, Any]:
    normal_vals = [rng.randint(15, 22) for _ in range(5)]
    outlier = rng.choice([75, 82, 90])
    dataset = normal_vals + [outlier]
    rng.shuffle(dataset)
    data_str = ", ".join(str(x) for x in dataset)
    ans = f"Outlier: {outlier}; it lies far away from the rest of the clustered data"
    prompt = (
        f"Consider the following set of learner test completion times in minutes:\n\n"
        f"$$\\{{ {data_str} \\}}$$\n\n"
        f"1. Define what an **outlier** (extreme value) is in statistics.\n"
        f"2. Identify the outlier in this dataset and justify your choice."
    )
    sol = (
        f"**1. Definition of Outlier:**\n"
        f"An outlier is a data value that is significantly higher or lower than almost all the other values in a dataset.\n\n"
        f"**2. Identification & Justification:**\n"
        f"- The value **{outlier}** is the outlier.\n"
        f"- **Justification:** While all other completion times cluster tightly between $15$ and $22$ minutes, "
        f"${outlier}$ is more than triple the values of the rest of the group."
    )
    return {
        "id": f"g7_dm_16_{rng.randint(100000, 999999)}",
        "subskill": "16_data_extremes_outliers_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{outlier}; significantly higher than the clustered values",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_16",
        "hints": {
            "tier_1": "Look for a number that looks out of place compared to all the others.",
            "tier_2": f"Most numbers are near 20, but {outlier} is huge.",
            "tier_3": f"Outlier is {outlier}."
        },
        "misconception_tags": ["ignoring_outliers_in_distribution"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Defines outlier as value significantly different from the rest", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Identifies {outlier} as the outlier", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 17. Data extremes outliers effect on mean
def arch_17_data_extremes_outliers_effect_on_mean(rng: random.Random) -> Dict[str, Any]:
    vals = [10, 12, 14, 16]
    mean_without = sum(vals) / len(vals)  # 13.0
    outlier = 70
    vals_with = vals + [outlier]
    mean_with = sum(vals_with) / len(vals_with)  # 122 / 5 = 24.4
    ans = "The extreme outlier dramatically increases the mean, giving a distorted impression"
    prompt = (
        "A group of 4 workers earn daily wages of R100, R120, R140, and R160 (mean = R130).\n"
        "A company director earning R700 per day is added to this group.\n\n"
        "1. Calculate the new mean wage for all 5 individuals.\n"
        "2. Explain how this extreme outlier affects the mean and why the mean is misleading in this case."
    )
    sol = (
        "**1. New Mean Calculation:**\n"
        "$$\\text{Total} = 100 + 120 + 140 + 160 + 700 = \\text{R}1\\,220$$\n"
        "$$\\text{New Mean} = \\frac{1\\,220}{5} = \\text{R}244$$\n\n"
        "**2. Impact of Outlier:**\n"
        "The extreme outlier (R700) pulls the mean up from R130 to R244. "
        "The new mean of R244 is misleading because 4 out of the 5 individuals (80%) earn far less than R244."
    )
    return {
        "id": f"g7_dm_17_{rng.randint(100000, 999999)}",
        "subskill": "17_data_extremes_outliers_effect_on_mean",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "New mean is R244; outlier pulls mean up so it no longer represents typical workers",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_17",
        "hints": {
            "tier_1": "Add all 5 wages and divide by 5.",
            "tier_2": "1220 / 5 = 244.",
            "tier_3": "The outlier pulls the mean up to R244, making it unrepresentative."
        },
        "misconception_tags": ["assuming_mean_is_always_representative"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates new mean = R244", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains outlier pulls the mean upwards", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Explains why mean is misleading for typical workers", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 18. Outlier impact mean vs median comparison
def arch_18_outlier_impact_mean_vs_median_comparison(rng: random.Random) -> Dict[str, Any]:
    ans = "Median is resistant/robust to outliers; Mean is heavily affected by outliers"
    prompt = (
        "When a dataset contains one or more extreme outliers:\n\n"
        "1. Which measure of central tendency is more reliable to represent the 'typical' value: the **mean** or the **median**?\n"
        "2. Explain why one measure is preferred over the other in the presence of outliers."
    )
    sol = (
        "**1. Preferred Measure:**\n"
        "The **median** is preferred.\n\n"
        "**2. Explanation:**\n"
        "- The **mean** incorporates the numerical value of every single data point, so an extreme value pulls the mean heavily toward itself.\n"
        "- The **median** depends only on the positional rank of ordered values. Extreme values at the ends do not change the middle position, "
        "making the median **resistant (robust)** to outliers."
    )
    return {
        "id": f"g7_dm_18_{rng.randint(100000, 999999)}",
        "subskill": "18_outlier_impact_mean_vs_median_comparison",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Median is preferred because it is not affected by extreme values, unlike the mean",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_18",
        "hints": {
            "tier_1": "Does changing the highest number to a million change the middle number?",
            "tier_2": "The middle number stays the middle number, but the average shoots through the roof.",
            "tier_3": "Median is more reliable because it resists outliers."
        },
        "misconception_tags": ["preferring_mean_when_outliers_present"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Selects median as preferred measure", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains median depends on position and resists outliers", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 19. Population vs sample definitions
def arch_19_population_vs_sample_definitions(rng: random.Random) -> Dict[str, Any]:
    ans = "Population: entire group of interest; Sample: smaller subgroup chosen from the population to represent it"
    prompt = (
        "In statistical investigations and data reporting:\n\n"
        "1. Define the term **population**.\n"
        "2. Define the term **sample**.\n"
        "3. Explain why researchers study a sample rather than the entire population."
    )
    sol = (
        "**1. Population:**\n"
        "The entire group of individuals, objects, or events that researchers want to investigate.\n\n"
        "**2. Sample:**\n"
        "A smaller subgroup selected from the population that is used to collect data and represent the whole group.\n\n"
        "**3. Why Use a Sample?**\n"
        "It is usually too costly, time-consuming, or practically impossible to survey every single member of an entire population."
    )
    return {
        "id": f"g7_dm_19_{rng.randint(100000, 999999)}",
        "subskill": "19_population_vs_sample_definitions",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Population is the entire group; sample is a selected subset; samples save time and cost",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_19",
        "hints": {
            "tier_1": "Population is everyone. Sample is a small group chosen from everyone.",
            "tier_2": "Can you test every grain of rice in a sack to see if it's cooked?",
            "tier_3": "Population = entire group; Sample = representative subgroup."
        },
        "misconception_tags": ["confusing_sample_with_population"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Defines population as entire group", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Defines sample as subset representing population", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Explains sample saves time/cost/practicality", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 20. Population vs sample representative size
def arch_20_population_vs_sample_representative_size(rng: random.Random) -> Dict[str, Any]:
    pop = 26000
    sample = 2500
    pct = round((sample / pop) * 100, 1)
    pct_str = str(pct).replace(".", "{,}")
    ans = f"1. Population = {pop}; Sample = {sample}; 2. {pct_str}%"
    prompt = (
        f"In a national survey on school infrastructure in South Africa, $2\\,500$ schools were selected "
        f"and inspected out of all $26\\,000$ schools across the country.\n\n"
        f"1. State the population size and the sample size.\n"
        f"2. Calculate the percentage of the total school population that the sample represents (round to 1 decimal place)."
    )
    sol = (
        f"**1. Sizes:**\n"
        f"- **Population:** $26\\,000$ schools (all schools in South Africa).\n"
        f"- **Sample:** $2\\,500$ schools (the group actually surveyed).\n\n"
        f"**2. Percentage Calculation:**\n"
        f"$$\\text{{Percentage}} = \\frac{{\\text{{Sample Size}}}}{{\\text{{Population Size}}}} \\times 100\\%$$\n"
        f"$$\\text{{Percentage}} = \\frac{{2\\,500}}{{26\\,000}} \\times 100\\% = \\frac{{250}}{{26}}\\% \\approx {pct_str}\\%$$"
    )
    return {
        "id": f"g7_dm_20_{rng.randint(100000, 999999)}",
        "subskill": "20_population_vs_sample_representative_size",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Population: 26 000, Sample: 2 500, Percentage: {pct_str}%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_20",
        "hints": {
            "tier_1": "Population is the big number (26 000); sample is the surveyed group (2 500).",
            "tier_2": "Divide 2 500 by 26 000 and multiply by 100.",
            "tier_3": f"{pct_str}%."
        },
        "misconception_tags": ["dividing_population_by_sample_for_percentage"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "States population = 26 000 and sample = 2 500", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Sets up ratio 2500 / 26000 * 100%", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculates percentage = {pct_str}%", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 21. Frequency table percentage calculation
def arch_21_frequency_table_percentage_calculation(rng: random.Random) -> Dict[str, Any]:
    total_learners = 200
    category = "Walk"
    count = rng.choice([50, 60, 70, 80])
    pct = int((count / total_learners) * 100)
    ans = f"{pct}%"
    prompt = (
        f"In a travel-to-school survey of {total_learners} Grade 7 learners, "
        f"{count} learners stated that they walk to school.\n\n"
        f"Calculate the percentage of learners in the survey who walk to school."
    )
    sol = (
        f"**Step 1: Formula for Percentage:**\n"
        f"$$\\text{{Percentage}} = \\frac{{\\text{{Frequency}}}}{{\\text{{Total Count}}}} \\times 100\\%$$\n\n"
        f"**Step 2: Substitute values:**\n"
        f"$$\\text{{Percentage}} = \\frac{{{count}}}{{{total_learners}}} \\times 100\\% = \\frac{{{count}}}{{2}}\\% = {pct}\\%$$"
    )
    return {
        "id": f"g7_dm_21_{rng.randint(100000, 999999)}",
        "subskill": "21_frequency_table_percentage_calculation",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{pct}%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_21",
        "hints": {
            "tier_1": f"Write the fraction {count} / {total_learners}.",
            "tier_2": f"Multiply by 100 to get percentage.",
            "tier_3": f"{pct}%."
        },
        "misconception_tags": ["percentage_conversion_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Sets up fraction {count}/{total_learners}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates {pct}%", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 22. Frequency table finding total and frequencies
def arch_22_frequency_table_finding_total_and_frequencies(rng: random.Random) -> Dict[str, Any]:
    counts = [12, 18, 15, 5]
    total = sum(counts)
    ans = f"{total}"
    prompt = (
        "A frequency table records transport methods used by Grade 7 learners:\n\n"
        "- Bus: $12$\n"
        "- Taxi: $18$\n"
        "- Bicycle: $15$\n"
        "- Car: $5$\n\n"
        "What is the total number of learners surveyed in this sample?"
    )
    sol = (
        f"**Sum of frequencies:**\n"
        f"$$\\text{{Total}} = 12 + 18 + 15 + 5 = {total}\\text{{ learners}}$$"
    )
    return {
        "id": f"g7_dm_22_{rng.randint(100000, 999999)}",
        "subskill": "22_frequency_table_finding_total_and_frequencies",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{total} learners",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_dm_22",
        "hints": {
            "tier_1": "Add all the frequencies together.",
            "tier_2": "12 + 18 + 15 + 5.",
            "tier_3": f"Total is {total}."
        },
        "misconception_tags": ["arithmetic_addition_error"],
        "marking_schema": {
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates total = {total}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 23. Bar graph interpretation single bars SVG
def arch_23_bar_graph_interpretation_single_bars_svg(rng: random.Random) -> Dict[str, Any]:
    labs = ["A", "B", "C", "D"]
    b_val = rng.choice([36, 38, 42, 45])
    vals = [rng.randint(18, 25), b_val, rng.randint(12, 17), rng.randint(26, 32)]
    svg = _svg_bar_graph(labs, vals, "Grade 7 Test Grade Distribution")
    ans = f"Grade B ({b_val} learners)"
    prompt = (
        "Inspect the bar graph diagram below showing the test grade distribution of a Grade 7 cohort:\n\n"
        "1. Which grade category was achieved by the highest number of learners?\n"
        "2. How many learners achieved this modal grade?"
    )
    sol = (
        "**Analysis of the Bar Graph:**\n"
        "1. Looking at the vertical heights of the bars, **Grade B** has the tallest bar.\n"
        f"2. The height of the bar for Grade B is **{b_val}** learners."
    )
    return {
        "id": f"g7_dm_23_{rng.randint(100000, 999999)}",
        "subskill": "23_bar_graph_interpretation_single_bars_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Grade B with {b_val} learners",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_23",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Find the tallest bar in the graph.",
            "tier_2": f"The bar for B reaches {b_val}.",
            "tier_3": f"Grade B ({b_val} learners)."
        },
        "misconception_tags": ["reading_wrong_bar_height"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies Grade B as highest", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Reads frequency = {b_val}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 24. Bar graph read highest lowest frequencies
def arch_24_bar_graph_read_highest_lowest_frequencies(rng: random.Random) -> Dict[str, Any]:
    labs = ["Red", "Blue", "Green", "Yellow"]
    hi_v = rng.choice([40, 42, 45, 48])
    lo_v = rng.choice([8, 9, 11, 12])
    vals = [rng.randint(15, 22), hi_v, rng.randint(25, 32), lo_v]
    svg = _svg_bar_graph(labs, vals, "Favorite House Colors", "Votes")
    diff = hi_v - lo_v
    ans = f"Highest: Blue ({hi_v}); Lowest: Yellow ({lo_v}); Difference = {diff}"
    prompt = (
        "Refer to the bar graph diagram showing learner votes for house colors:\n\n"
        "1. State the color with the highest number of votes and its count.\n"
        "2. State the color with the fewest votes and its count.\n"
        "3. Find the difference in votes between the most popular and least popular colors."
    )
    sol = (
        "**Analysis of the Bar Graph:**\n"
        f"- Most popular: **Blue** with ${hi_v}$ votes.\n"
        f"- Least popular: **Yellow** with ${lo_v}$ votes.\n"
        f"- Difference: ${hi_v} - {lo_v} = {diff}$ votes."
    )
    return {
        "id": f"g7_dm_24_{rng.randint(100000, 999999)}",
        "subskill": "24_bar_graph_read_highest_lowest_frequencies",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Blue: {hi_v}, Yellow: {lo_v}, Difference = {diff}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_dm_24",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": f"Find the tallest bar (Blue = {hi_v}) and shortest bar (Yellow = {lo_v}).",
            "tier_2": f"Subtract: {hi_v} - {lo_v} = {diff}.",
            "tier_3": f"{ans}"
        },
        "misconception_tags": ["subtraction_error_in_range_from_graph"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": f"Identifies Blue ({hi_v})", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Identifies Yellow ({lo_v})", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculates difference = {diff}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 25. Double bar graph compare two groups SVG
def arch_25_double_bar_graph_compare_two_groups_svg(rng: random.Random) -> Dict[str, Any]:
    ans = "Grade 7: Boys = 45, Girls = 55 (Total = 100); Girls exceed boys by 10"
    prompt = (
        "A double bar graph compares the enrollment of Boys and Girls across Grade 7:\n\n"
        "- Grade 7 Boys: $45$\n"
        "- Grade 7 Girls: $55$\n\n"
        "1. What is the total enrollment of Grade 7 learners?\n"
        "2. Which gender has a higher enrollment, and by how many learners?"
    )
    sol = (
        "**1. Total Enrollment:**\n"
        "$$\\text{Total} = 45 + 55 = 100\\text{ learners}$$\n\n"
        "**2. Comparison:**\n"
        "**Girls** have a higher enrollment ($55 > 45$).\n"
        "$$\\text{Difference} = 55 - 45 = 10\\text{ learners}$$\n"
        "There are $10$ more girls than boys enrolled."
    )
    return {
        "id": f"g7_dm_25_{rng.randint(100000, 999999)}",
        "subskill": "25_double_bar_graph_compare_two_groups_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Total = 100; Girls have 10 more than boys",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_dm_25",
        "hints": {
            "tier_1": "Add 45 and 55 for total. Subtract 45 from 55 for difference.",
            "tier_2": "Total = 100. Difference = 10.",
            "tier_3": "Total = 100; 10 more girls than boys."
        },
        "misconception_tags": ["reading_wrong_category_in_double_bar"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates total = 100", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identifies Girls exceed Boys by 10", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }
