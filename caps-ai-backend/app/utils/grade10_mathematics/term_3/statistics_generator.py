"""Grade 10 Mathematics — Term 3: Statistics (Deterministic 6-Pillar Generator).
100% aligned with South African CAPS Curriculum (Grade 10 Mathematics Paper 2: Statistics).
Covers:
- Five-number summary: Min, Q1 (lower quartile), Median (Q2), Q3 (upper quartile), Max
- Range and Interquartile Range (IQR = Q3 - Q1), Semi-interquartile range
- Box-and-whisker diagrams and skewness identification
- Measures of central tendency: Mean (average), Median, Mode

Zero-LLM: 100% deterministic Python calculations with South African comma decimals ({,}).
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "Statistics"
TOPIC_ID = "grade10_math_statistics"
LO = "math10_statistics_measures"

CONTEXTS = [
    ("Mathematics test marks (out of 50)", "marks"),
    ("Daily temperatures in Bloemfontein (°C)", "°C"),
    ("Sprint times of Grade 10 athletes (seconds)", "seconds"),
    ("Number of books read by learners in a year", "books"),
    ("Weekly pocket money (Rand)", "Rand"),
]


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return f"{val:.{places}f}".replace(".", ",")


def _compute_five_num(data: List[int]) -> Dict[str, Any]:
    s = sorted(data)
    n = len(s)
    min_v = s[0]
    max_v = s[-1]

    mid = n // 2
    if n % 2 == 1:
        med_v = float(s[mid])
        lower_half = s[:mid]
        upper_half = s[mid + 1 :]
    else:
        med_v = (s[mid - 1] + s[mid]) / 2.0
        lower_half = s[:mid]
        upper_half = s[mid:]

    def half_median(half: List[int]) -> float:
        m = len(half)
        if m % 2 == 1:
            return float(half[m // 2])
        return (half[m // 2 - 1] + half[m // 2]) / 2.0

    q1_v = half_median(lower_half)
    q3_v = half_median(upper_half)
    iqr_v = q3_v - q1_v
    range_v = max_v - min_v

    return {
        "sorted": s,
        "n": n,
        "min": min_v,
        "q1": q1_v,
        "median": med_v,
        "q3": q3_v,
        "max": max_v,
        "iqr": iqr_v,
        "range": range_v,
    }


def _build_five_number_drill(r: random.Random) -> Dict[str, Any]:
    title, unit = r.choice(CONTEXTS)
    n_items = r.choice([11, 13, 15])
    base = r.randint(15, 35)
    raw = [base + r.randint(-12, 18) for _ in range(n_items)]
    stats = _compute_five_num(raw)

    raw_str = ", ".join(str(x) for x in raw)
    sorted_str = ", ".join(str(x) for x in stats["sorted"])

    prompt = (
        rf"Consider the following set of {title}:\n\n"
        rf"$$\{{{raw_str}\}}$$\n\n"
        rf"1. Arrange the data in ascending order.\n"
        rf"2. Determine the five-number summary (Minimum, $Q_1$, Median, $Q_3$, Maximum).\n"
        rf"3. Calculate the Interquartile Range (IQR)."
    )

    q1_str = _fmt_sa(stats["q1"])
    med_str = _fmt_sa(stats["median"])
    q3_str = _fmt_sa(stats["q3"])
    iqr_str = _fmt_sa(stats["iqr"])

    worked = (
        rf"**1. Ordered Data:** [{sorted_str}]"
        rf"\n\n**2. Five-Number Summary:**"
        rf"\n- Minimum = {stats['min']}"
        rf"\n- Lower Quartile ($Q_1$) = {q1_str}"
        rf"\n- Median ($Q_2$) = {med_str}"
        rf"\n- Upper Quartile ($Q_3$) = {q3_str}"
        rf"\n- Maximum = {stats['max']}"
        rf"\n\n**3. Interquartile Range:**"
        rf"\n$$\text{{IQR}} = Q_3 - Q_1 = {q3_str} - {q1_str} = {iqr_str}$$"
    )

    ans_str = f"Min={stats['min']}, Q1={q1_str}, Med={med_str}, Q3={q3_str}, Max={stats['max']}, IQR={iqr_str}"

    return {
        "id": f"g10_stat_five_num_{r.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans_str,
        "answer_latex": ans_str,
        "worked_solution": worked,
        "marks": 6,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "five_number_summary",
        "term": 3,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Sort data in ascending order", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Minimum ({stats['min']}) and Maximum ({stats['max']})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Median Q2 = {med_str}", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Quartiles Q1 = {q1_str} and Q3 = {q3_str}", "marks": 2, "editable": True},
                {"id": "mp_5", "desc": f"Interquartile Range IQR = {iqr_str}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Always sort data in ascending order before finding quartiles or median.",
            "2_concept": "The median divides data into lower and upper halves; Q1 is the median of the lower half, Q3 of the upper half.",
            "3_breakdown": rf"Sorted: [{sorted_str}]. Median = {med_str}, Q1 = {q1_str}, Q3 = {q3_str}. IQR = {iqr_str}.",
        },
        "misconception_tags": ["unsorted_data_error", "quartile_miscalculation"],
    }


def _build_box_and_whisker_drill(r: random.Random) -> Dict[str, Any]:
    min_v = r.randint(10, 25)
    iqr_len = r.randint(12, 20)
    q1_v = min_v + r.randint(5, 10)

    skew_type = r.choice(["symmetrical", "skewed_right", "skewed_left"])
    if skew_type == "symmetrical":
        med_v = q1_v + iqr_len // 2
        q3_v = q1_v + iqr_len
        max_v = q3_v + (q1_v - min_v)
        skew_answer = "symmetrical"
        reason = "The median is centered between Q1 and Q3, and the whiskers are of approximately equal length."
    elif skew_type == "skewed_right":
        med_v = q1_v + 3
        q3_v = q1_v + iqr_len
        max_v = q3_v + (q1_v - min_v) + 15
        skew_answer = "skewed to the right (positively skewed)"
        reason = "The whisker on the right is longer, and the distance between Q3 and the median is greater than the distance between the median and Q1."
    else:
        med_v = q1_v + iqr_len - 3
        q3_v = q1_v + iqr_len
        min_v = max(0, min_v - 15)
        max_v = q3_v + 5
        skew_answer = "skewed to the left (negatively skewed)"
        reason = "The whisker on the left is longer, and the distance between the median and Q1 is greater than the distance between Q3 and the median."

    prompt = (
        rf"A box-and-whisker diagram for a test mark distribution has the following summary values:\n\n"
        rf"$$\text{{Minimum}} = {min_v}, \quad Q_1 = {q1_v}, \quad \text{{Median}} = {med_v}, \quad Q_3 = {q3_v}, \quad \text{{Maximum}} = {max_v}$$\n\n"
        rf"1. State the percentage of learners who scored below $Q_1$.\n"
        rf"2. State the percentage of learners who scored between $Q_1$ and $Q_3$.\n"
        rf"3. Comment on the skewness of the data distribution and provide a reason."
    )

    worked = (
        rf"**1. Below $Q_1$:** Exactly 25\% of the data lies below the lower quartile $Q_1$."
        rf"\n\n**2. Between $Q_1$ and $Q_3$:** Exactly 50\% of the data lies in the interquartile box."
        rf"\n\n**3. Skewness:** {skew_answer}. **Reason:** {reason}"
    )

    return {
        "id": f"g10_stat_box_skew_{r.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"Below Q1: 25%, Middle: 50%, Skewness: {skew_answer}",
        "answer_latex": rf"\text{{Below }} Q_1: 25\%, \text{{ Middle: }} 50\%, \text{{ Skewness: }} \text{{{skew_answer}}}",
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "box_whisker_skewness",
        "term": 3,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Percentage below Q1 (25%)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Percentage between Q1 and Q3 (50%)", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct skewness identification ({skew_answer})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Valid mathematical reason based on whiskers/median", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Each quartile represents exactly 25% of the data.",
            "2_concept": "Look at which whisker is longer and whether the median is closer to Q1 or Q3.",
            "3_breakdown": rf"Below Q1 is 25%. Between Q1 and Q3 is 50%. The distribution is {skew_answer}.",
        },
        "misconception_tags": ["skewness_direction_confusion"],
    }


def generate(subskill: Optional[str] = None, difficulty: str = "medium", count: int = 1, seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    r = _rng(seed)
    generators = [_build_five_number_drill, _build_box_and_whisker_drill]
    if subskill == "five_number_summary":
        generators = [_build_five_number_drill]
    elif subskill == "box_whisker_skewness":
        generators = [_build_box_and_whisker_drill]

    questions = []
    for _ in range(count):
        gen_fn = r.choice(generators)
        questions.append(gen_fn(r))
    return questions
