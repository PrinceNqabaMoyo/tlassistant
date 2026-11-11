"""Grade 9 Mathematics — Collect, Organise & Summarise Data Generator (Deterministic 6-Pillar Contract).

Curriculum Alignment:
- Grade 9 Term 4: Collect, organise and summarise data
- South African National Curriculum Standards (Senior Phase Mathematics)
- Measures of central tendency: Mean, Median, Mode for ungrouped and grouped data
- Measures of dispersion: Range (Maximum - Minimum)
- Outlier detection and effect on mean vs median
- Grouped frequency tables with class intervals (modal class, median class, estimated mean)

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with formula, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng

TOPIC = "grade9_math_data_summarise"
LO = "math9_data_summarise"


def generate_grade9_data_summarise_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "ungrouped_mean_median_mode_range",
        "outlier_impact_analysis",
        "grouped_frequency_table_intervals",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_datasum_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "ungrouped_mean_median_mode_range":
        # Generate n numbers (e.g. 7, 8, or 9 values) with clean integer mean and a distinct mode
        n = r.choice([7, 9])
        target_mean = r.randint(15, 30)
        mode_val = target_mean + r.randint(-4, 4)
        
        # Build dataset around mean with mode repeated 2 or 3 times
        data = [mode_val, mode_val]
        while len(data) < n - 1:
            val = target_mean + r.randint(-10, 10)
            if val != mode_val and val > 0:
                data.append(val)
        
        # Adjust last value so sum is exact multiple of n
        current_sum = sum(data)
        needed_last = target_mean * n - current_sum
        if needed_last <= 0 or needed_last == mode_val:
            # Shift a value
            data[0] = target_mean
            data[1] = target_mean
            mode_val = target_mean
            current_sum = sum(data)
            needed_last = target_mean * n - current_sum
        data.append(needed_last)
        
        # Shuffle for presentation
        raw_data = list(data)
        r.shuffle(raw_data)
        
        sorted_data = sorted(raw_data)
        data_sum = sum(sorted_data)
        mean_val = data_sum // n
        median_val = sorted_data[n // 2]
        min_val = sorted_data[0]
        max_val = sorted_data[-1]
        range_val = max_val - min_val

        data_str = ", ".join(str(x) for x in raw_data)
        sorted_str = ", ".join(str(x) for x in sorted_data)

        question_text = (
            f"The following marks out of $50$ were obtained by a sample of Grade 9 learners in a Mathematics test:\n\n"
            f"$$\\text{{Data: }} [{data_str}]$$\n\n"
            f"1. Arrange the data in ascending order.\n"
            f"2. Calculate the mean mark ($\\bar{{x}}$).\n"
            f"3. Determine the median mark.\n"
            f"4. State the mode.\n"
            f"5. Calculate the range of the marks."
        )

        steps = [
            {"id": "S1", "statement": f"Ascending order: $[{sorted_str}]$", "reason": "sort data values", "deps": []},
            {"id": "S2", "statement": f"Mean $\\bar{{x}} = \\frac{{\\sum x}}{{n}} = \\frac{{{data_sum}}}{{{n}}} = {mean_val}$", "reason": "mean formula", "deps": ["S1"]},
            {"id": "S3", "statement": f"Median = middle value (position $\\frac{{{n}+1}}{{2}} = {n//2 + 1}$) = ${median_val}$", "reason": "median position", "deps": ["S1"]},
            {"id": "S4", "statement": f"Mode = most frequent value = ${mode_val}$", "reason": "mode frequency", "deps": ["S1"]},
            {"id": "S5", "statement": f"Range = $\\text{{Maximum}} - \\text{{Minimum}} = {max_val} - {min_val} = {range_val}$", "reason": "range formula", "deps": ["S1"]},
        ]

        hints = [
            "Always sort the raw data in ascending order from smallest to largest first.",
            f"Formulas:\n- Mean = Total sum ÷ Number of items ({data_sum} ÷ {n})\n- Median = Middle value in sorted list\n- Mode = Most repeated number\n- Range = Highest value minus Lowest value.",
            f"Sorted: {sorted_str}. Mean = {mean_val}, Median = {median_val}, Mode = {mode_val}, Range = {range_val}.",
        ]

        error_tax = [
            {
                "id": "err_median_unsorted",
                "tag": "misconception_median_without_sorting",
                "condition": f"Selected middle item of unsorted raw data: {raw_data[n//2]}",
                "feedback": "You MUST order the data in ascending order before finding the median. Finding the middle of an unsorted list is incorrect.",
            },
            {
                "id": "err_range_as_interval",
                "tag": "misconception_range_as_interval",
                "condition": f"Wrote range as '{min_val} - {max_val}' instead of difference {range_val}",
                "feedback": "Range is a single number representing spread: Range = Max - Min. Subtract the minimum from the maximum.",
            },
        ]

        sample_answer = (
            f"1. Ascending order: $[{sorted_str}]$\n"
            f"2. $\\bar{{x}} = \\frac{{{data_sum}}}{{{n}}} = {mean_val}$\n"
            f"3. Median $= {median_val}$\n"
            f"4. Mode $= {mode_val}$\n"
            f"5. Range $= {max_val} - {min_val} = {range_val}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "statistics_box_and_ogive",
            "caption": f"Ungrouped sample dataset (n = {n})",
            "five_num": [min_val, sorted_data[n // 4], median_val, sorted_data[3 * n // 4], max_val],
        }

        correct_ans = f"Mean = {mean_val}, Median = {median_val}, Mode = {mode_val}, Range = {range_val}"
        subskill_id = "ungrouped_mean_median_mode_range"
        reason_code = "measures of central tendency and spread"
        marks = 5

    elif archetype == "outlier_impact_analysis":
        # Dataset with a severe outlier (e.g. 5, 6, 7, 8, 9, 10, 80)
        base_vals = [r.randint(12, 18) for _ in range(6)]
        outlier = r.randint(65, 85)
        raw_with_outlier = sorted(base_vals + [outlier])
        
        n_all = len(raw_with_outlier)
        sum_all = sum(raw_with_outlier)
        mean_all = round(sum_all / n_all, 1)
        median_all = raw_with_outlier[n_all // 2]
        
        # Without outlier
        sum_no = sum(base_vals)
        mean_no = round(sum_no / len(base_vals), 1)
        median_no = sorted(base_vals)[len(base_vals) // 2]

        data_str = ", ".join(str(x) for x in raw_with_outlier)

        question_text = (
            f"A learner recorded the time (in minutes) taken by 7 students to complete a homework task:\n\n"
            f"$$\\text{{Times: }} [{data_str}]$$\n\n"
            f"1. Identify the outlier in this dataset.\n"
            f"2. Calculate the mean and median of the complete dataset (including the outlier).\n"
            f"3. Explain which measure of central tendency (mean or median) best represents the typical time taken by the students, giving a reason."
        )

        steps = [
            {"id": "S1", "statement": f"Outlier = ${outlier}$ minutes", "reason": "value significantly greater than all other values", "deps": []},
            {"id": "S2", "statement": f"Mean with outlier: $\\frac{{{sum_all}}}{{{n_all}}} = {mean_all}$ mins; Median = ${median_all}$ mins", "reason": "statistical calculation", "deps": ["S1"]},
            {"id": "S3", "statement": f"Best measure: Median (${median_all}$ mins), because the mean is distorted by the extreme outlier ${outlier}$", "reason": "outlier sensitivity principle", "deps": ["S2"]},
        ]

        hints = [
            f"An outlier is an extreme value that lies far outside the rest of the observations (here, {outlier}).",
            f"Calculate the mean: {sum_all} ÷ 7 = {mean_all}. The median is the middle number: {median_all}.",
            "The mean is heavily pulled upwards by extreme values, whereas the median is resistant to outliers. Thus, the median provides a much fairer picture of the typical score.",
        ]

        error_tax = [
            {
                "id": "err_chose_mean",
                "tag": "misconception_mean_superiority",
                "condition": "Claimed the mean is best despite the outlier",
                "feedback": "The mean is distorted by the outlier (it makes the average look much higher than what 6 out of 7 students actually scored). The median is the better representative measure.",
            },
        ]

        sample_answer = (
            f"1. Outlier: ${outlier}$\\text{{ minutes}}\n"
            f"2. Mean with outlier: $\\bar{{x}} = \\frac{{{sum_all}}}{{7}} = {mean_all}$\\text{{ mins}}\n"
            f"   Median with outlier: ${median_all}$\\text{{ mins}}\n"
            f"3. The **median** best represents the typical time because the mean is heavily skewed upwards by the single extreme outlier (${outlier}$). Six of the seven students took between {min(base_vals)} and {max(base_vals)} minutes, which is close to the median ({median_all})."
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "statistics_box_and_ogive",
            "caption": f"Distribution with outlier at {outlier}",
            "five_num": [min(raw_with_outlier), raw_with_outlier[1], median_all, raw_with_outlier[-2], outlier],
        }

        correct_ans = f"Outlier = {outlier}; Best = Median ({median_all})"
        subskill_id = "outlier_impact_analysis"
        reason_code = "outlier effect on mean vs median"
        marks = 4

    else:
        # grouped_frequency_table_intervals: Grouped frequency distribution
        # Intervals: 0 <= x < 10, 10 <= x < 20, 20 <= x < 30, 30 <= x < 40
        f1 = r.randint(3, 8)
        f2 = r.randint(8, 16)
        f3 = r.randint(12, 22)  # modal class
        f4 = r.randint(4, 9)
        total_f = f1 + f2 + f3 + f4
        
        intervals = [
            ("0 \\le x < 10", 5, f1),
            ("10 \\le x < 20", 15, f2),
            ("20 \\le x < 30", 25, f3),
            ("30 \\le x < 40", 35, f4),
        ]
        
        # Estimated mean: sum(midpoint * freq) / total_freq
        sum_fx = sum(mid * freq for _, mid, freq in intervals)
        est_mean = round(sum_fx / total_f, 1)

        question_text = (
            f"The table below shows the distribution of scores in an assessment of $N = {total_f}$ learners:\n\n"
            f"| Class Interval | Midpoint ($m$) | Frequency ($f$) |\n"
            f"| :--- | :---: | :---: |\n"
            f"| $0 \\le x < 10$ | $5$ | ${f1}$ |\n"
            f"| $10 \\le x < 20$ | $15$ | ${f2}$ |\n"
            f"| $20 \\le x < 30$ | $25$ | ${f3}$ |\n"
            f"| $30 \\le x < 40$ | $35$ | ${f4}$ |\n\n"
            f"1. Identify the **modal class interval**.\n"
            f"2. In which class interval does the **median** lie?\n"
            f"3. Calculate the **estimated mean** ($\\bar{{x}}$) using class midpoints."
        )

        steps = [
            {"id": "S1", "statement": f"Modal class interval: $20 \\le x < 30$ (highest frequency = ${f3}$)", "reason": "modal class definition", "deps": []},
            {"id": "S2", "statement": f"Median position: $\\frac{{{total_f}}}{{2}} = {total_f/2}$. Cumulative frequencies: {f1}, {f1+f2}, {f1+f2+f3}. Median lies in $20 \\le x < 30$.", "reason": "median class interval", "deps": ["S1"]},
            {"id": "S3", "statement": f"Estimated mean: $\\bar{{x}} = \\frac{{\\sum (m \\times f)}}{{N}} = \\frac{{{sum_fx}}}{{{total_f}}} = {est_mean}$", "reason": "grouped mean formula", "deps": ["S2"]},
        ]

        hints = [
            f"The modal class is the interval with the greatest frequency (here, {f3} is the highest frequency).",
            f"To find the median interval, find the position $N/2 = {total_f}/2 = {total_f/2}$. Add the frequencies consecutively to see which interval contains the {total_f/2}th learner.",
            f"Estimated mean = $\\frac{{(5 \\times {f1}) + (15 \\times {f2}) + (25 \\times {f3}) + (35 \\times {f4})}}{{{total_f}}} = \\frac{{{sum_fx}}}{{{total_f}}} = {est_mean}$.",
        ]

        error_tax = [
            {
                "id": "err_divided_by_num_classes",
                "tag": "misconception_grouped_mean_denominator",
                "condition": f"Divided sum_fx by 4 classes instead of total frequency N = {total_f}",
                "feedback": f"When calculating the mean of grouped data, divide by the total number of learners (N = {total_f}), NOT the number of rows/classes.",
            },
        ]

        sample_answer = (
            f"1. Modal class: $20 \\le x < 30$ (highest frequency = ${f3}$)\n"
            f"2. Median position $= \\frac{{{total_f}}}{{2}} = {total_f/2}$.\n"
            f"   Cumulative frequencies: {f1}, {f1+f2}, {f1+f2+f3}. Therefore, the median lies in interval $20 \\le x < 30$.\n"
            f"3. $\\bar{{x}} = \\frac{{\\sum (m \\times f)}}{{N}} = \\frac{{{5}({f1}) + {15}({f2}) + {25}({f3}) + {35}({f4})}}{{{total_f}}} = \\frac{{{sum_fx}}}{{{total_f}}} = {est_mean}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "statistics_box_and_ogive",
            "caption": f"Grouped frequency distribution (Total N = {total_f})",
        }

        correct_ans = f"Modal: 20 <= x < 30; Median: 20 <= x < 30; Mean: {est_mean}"
        subskill_id = "grouped_frequency_table_intervals"
        reason_code = "grouped frequency analysis"
        marks = 4

    q = {
        "id": qid,
        "subject": "Mathematics",
        "grade": 9,
        "topic": TOPIC,
        "subskill": subskill_id,
        "learning_objective_id": LO,
        "mode": mode,
        "difficulty": difficulty,
        "question_type": "free_response",
        "answer_mode": "free_response",
        "prompt": question_text,
        "question": question_text,
        "prompt_latex": question_text,
        "answer_latex": correct_ans,
        "correct_answer": correct_ans,
        "sample_answer": sample_answer,
        "worked_solution": sample_answer,
        "canonical_solution": sample_answer,
        "marking_schema": [
            {"criterion": f"Correct statistical definitions and method [{reason_code}]", "marks": 1},
            {"criterion": f"Accurate calculation and values {correct_ans}", "marks": marks - 1},
        ],
        "marks": marks,
        "hints": hints,
        "hint_sections": {
            "concept": hints[0],
            "rules": hints[1],
            "step_by_step": hints[2],
        },
        "misconception_tags": [m["tag"] for m in error_tax],
        "diagnostic_tags": [f"diag_{subskill_id}"],
        "keywords": ["data handling", "mean", "median", "mode", "range", "outlier", "grouped data", "frequency table"],
        "term": 4,
        "caps_weight_percent": 10.0,
        "suggested_duration_mins": 6,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Calculate summary statistics for dataset",
            "steps": steps,
        },
        "metadata": {
            "diagram_spec": diagram_spec,
            "answer_value": correct_ans,
            "reason_code": reason_code,
        },
    }
    return q


def generate(seed: Optional[int] = None, count: int = 1, **kwargs: Any) -> Dict[str, Any]:
    r = rng(seed)
    questions = []
    for _ in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        questions.append(generate_grade9_data_summarise_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
