"""Grade 11 Mathematics — Statistics: Summaries, Ogive Curves & Dispersion (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (Paper 2, Question 1 / 2: 15–20 marks):
- Five-number summary (Min, Q1, Median, Q3, Max) and Interquartile Range (IQR = Q3 - Q1).
- Formal 1,5 x IQR outlier test (x < Q1 - 1,5 IQR or x > Q3 + 1,5 IQR).
- Box-and-whisker plot skewness analysis (skewed right / skewed left / symmetrical).
- Cumulative frequency distribution tables and Ogive curves (reading estimated median and quartiles).
- Mean (x̄), variance (σ²), and standard deviation (σ) with one standard deviation interval (x̄ - σ ; x̄ + σ).
Supports full 10-mark compound exam questions and atomic 3-mark elementary sub-drills for adaptive scaffolding.
Zero-LLM: 100% deterministic Python & SymPy calculations with South African comma decimals ({,}).
"""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple
import sympy as sp

from app.utils.grade11_mathematics._math_common import (
    make_id,
    make_math_question,
    nonzero,
    num,
    rng,
    solution_graph,
    step,
    to_latex,
)

TOPIC = "grade11_math_statistics"
LO = "math11_statistics_summary_ogive"


# --------------------------------------------------------------------------- #
# Helper: Compute Five-Number Summary & Fences
# --------------------------------------------------------------------------- #
def _compute_summary(data: List[int]) -> Dict[str, Any]:
    s = sorted(data)
    n = len(s)
    min_v = s[0]
    max_v = s[-1]

    # CAPS method for odd N:
    mid = n // 2
    if n % 2 == 1:
        med_v = s[mid]
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

    lower_fence = q1_v - 1.5 * iqr_v
    upper_fence = q3_v + 1.5 * iqr_v

    outliers = [x for x in s if x < lower_fence or x > upper_fence]

    d_left = med_v - q1_v
    d_right = q3_v - med_v
    if d_right > d_left:
        skewness = "skewed to the right (positively skewed)"
        skew_reason = rf"Q_3 - \text{{Median}} = {num(d_right, 1)} > \text{{Median}} - Q_1 = {num(d_left, 1)}"
    elif d_left > d_right:
        skewness = "skewed to the left (negatively skewed)"
        skew_reason = rf"\text{{Median}} - Q_1 = {num(d_left, 1)} > Q_3 - \text{{Median}} = {num(d_right, 1)}"
    else:
        skewness = "symmetrical"
        skew_reason = rf"Q_3 - \text{{Median}} = \text{{Median}} - Q_1 = {num(d_left, 1)}"

    return {
        "sorted_data": s,
        "n": n,
        "min": min_v,
        "q1": q1_v,
        "median": med_v,
        "q3": q3_v,
        "max": max_v,
        "iqr": iqr_v,
        "lower_fence": lower_fence,
        "upper_fence": upper_fence,
        "outliers": outliers,
        "skewness": skewness,
        "skew_reason": skew_reason,
        "d_left": d_left,
        "d_right": d_right,
    }


# --------------------------------------------------------------------------- #
# Sub-drill 1: elementary_five_number_summary (3 marks)
# --------------------------------------------------------------------------- #
def _build_five_number_summary_drill(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding drill: Calculate five-number summary and IQR from raw data."""
    # Choose 11 distinct or near-distinct values in [30, 95]
    base_vals = sorted(r.sample(range(32, 92), 11))
    summary = _compute_summary(base_vals)

    data_str = ", ".join(str(x) for x in base_vals)
    min_v = summary["min"]
    q1_v = int(summary["q1"])
    med_v = int(summary["median"])
    q3_v = int(summary["q3"])
    max_v = summary["max"]
    iqr_v = int(summary["iqr"])

    prompt = (
        f"The following ordered data set represents the scores (out of 100) obtained by 11 learners in a Mathematics test:\n\n"
        f"$${data_str}$$\n\n"
        f"1. Determine the five-number summary for this data set. (2)\n"
        f"2. Calculate the Interquartile Range (IQR). (1)"
    )

    steps = [
        step(
            from_latex=rf"\text{{Data: }} {data_str}",
            to_latex_str=(
                rf"\text{{Min}} = {min_v}, \; Q_1 = {q1_v}, \; \text{{Median}} = {med_v}, \; "
                rf"Q_3 = {q3_v}, \; \text{{Max}} = {max_v}"
            ),
            op="locate position of minimum, quartiles, median, and maximum in ordered set",
            rule="five-number summary definition",
        ),
        step(
            from_latex=rf"\text{{IQR}} = Q_3 - Q_1 = {q3_v} - {q1_v}",
            to_latex_str=rf"\text{{IQR}} = {iqr_v}",
            op="evaluate difference between upper and lower quartiles",
            rule="interquartile range formula",
        ),
    ]

    canonical = solution_graph(
        goal="determine five-number summary and calculate IQR",
        steps=steps,
        final_latex=(
            rf"\text{{Min}} = {min_v}, \; Q_1 = {q1_v}, \; \text{{Med}} = {med_v}, \; "
            rf"Q_3 = {q3_v}, \; \text{{Max}} = {max_v}; \quad \text{{IQR}} = {iqr_v}"
        ),
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct median: {med_v}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Correct Q1 = {q1_v}, Q3 = {q3_v}, Min = {min_v}, Max = {max_v}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"Correct IQR = Q3 - Q1 = {iqr_v}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "arithmetic_error", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "The data is already arranged in ascending order. The median is the 6th value.",
        "concept": "For 11 values, Median is at position (11+1)/2 = 6. Q1 is the median of the lower 5 values (position 3), and Q3 is the median of the upper 5 values (position 9).",
        "breakdown": f"1. Min = {min_v}, Max = {max_v}.\n2. Median = {med_v}.\n3. $Q_1 = {q1_v}$ and $Q_3 = {q3_v}$.\n4. $\\text{{IQR}} = {q3_v} - {q1_v} = {iqr_v}$.",
    }

    diag = {
        "kind": "box_and_whisker",
        "min": min_v,
        "q1": q1_v,
        "median": med_v,
        "q3": q3_v,
        "max": max_v,
        "iqr": iqr_v,
    }

    return make_math_question(
        prefix="stat_5num",
        topic=TOPIC,
        subskill="elementary_five_number_summary",
        learning_objective_id=f"{LO}_five_number_summary",
        prompt=prompt,
        prompt_latex=data_str,
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        diagram_spec=diag,
        misconception_tags=["incorrect_quartile_position", "subtracted_median_instead_of_q1_for_iqr"],
        keywords=["five-number summary", "interquartile range", "quartiles", "median", "statistics"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_five_number_summary",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Sub-drill 2: elementary_iqr_outlier (3 marks)
# --------------------------------------------------------------------------- #
def _build_iqr_outlier_drill(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding drill: Test whether a given value is an outlier using 1,5 x IQR rule."""
    q1 = r.randint(35, 48)
    iqr = r.randint(14, 24)
    q3 = q1 + iqr

    has_outlier = r.choice([True, False])
    fence_choice = r.choice(["lower", "upper"])

    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    if fence_choice == "upper":
        if has_outlier:
            test_val = int(upper_fence + r.randint(2, 8))
            is_outlier = True
        else:
            test_val = int(upper_fence - r.randint(2, 6))
            is_outlier = False
        limit_desc = rf"\text{{Upper limit: }} Q_3 + 1{{,}}5 \times \text{{IQR}} = {q3} + 1{{,}}5({iqr}) = {num(upper_fence, 1)}"
        comp_str = rf"{test_val} > {num(upper_fence, 1)}" if is_outlier else rf"{test_val} \le {num(upper_fence, 1)}"
    else:
        if has_outlier:
            test_val = int(lower_fence - r.randint(2, 6))
            is_outlier = True
        else:
            test_val = int(lower_fence + r.randint(2, 6))
            is_outlier = False
        limit_desc = rf"\text{{Lower limit: }} Q_1 - 1{{,}}5 \times \text{{IQR}} = {q1} - 1{{,}}5({iqr}) = {num(lower_fence, 1)}"
        comp_str = rf"{test_val} < {num(lower_fence, 1)}" if is_outlier else rf"{test_val} \ge {num(lower_fence, 1)}"

    concl_str = "AN OUTLIER" if is_outlier else "NOT AN OUTLIER"

    prompt = (
        f"A data set has a lower quartile $Q_1 = {q1}$ and an upper quartile $Q_3 = {q3}$.\n\n"
        f"1. Calculate the Interquartile Range (IQR). (1)\n"
        f"2. Use the $1{{,}}5 \\times \\text{{IQR}}$ rule to show whether a data value of {test_val} is an outlier. (2)"
    )

    steps = [
        step(
            from_latex=rf"\text{{IQR}} = Q_3 - Q_1 = {q3} - {q1}",
            to_latex_str=rf"\text{{IQR}} = {iqr}",
            op="calculate IQR",
            rule="interquartile range formula",
        ),
        step(
            from_latex=limit_desc,
            to_latex_str=rf"{comp_str} \implies \text{{{test_val} is {concl_str}}}",
            op="compute outlier boundary and compare with test value",
            rule="1.5 x IQR outlier rule",
        ),
    ]

    canonical = solution_graph(
        goal="calculate IQR and determine if value is an outlier",
        steps=steps,
        final_latex=rf"\text{{IQR}} = {iqr}; \quad {test_val} \text{{ is {concl_str}}}",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct IQR = {iqr}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Correct fence calculation: {limit_desc}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"Comparison and conclusion: {test_val} is {concl_str}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "used_semi_iqr_instead_of_1.5_iqr", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": r"Calculate $\text{IQR} = Q_3 - Q_1$ first, then determine the outlier boundary using $Q \pm 1{,}5 \times \text{IQR}$.",
        "concept": r"A value $x$ is an outlier if $x < Q_1 - 1{,}5\text{IQR}$ or $x > Q_3 + 1{,}5\text{IQR}$.",
        "breakdown": f"1. $\\text{{IQR}} = {q3} - {q1} = {iqr}$.\n2. ${limit_desc}$.\n3. Since ${comp_str}$, the value {test_val} is {concl_str}.",
    }

    return make_math_question(
        prefix="stat_outlier",
        topic=TOPIC,
        subskill="elementary_iqr_outlier",
        learning_objective_id=f"{LO}_outlier_detection",
        prompt=prompt,
        prompt_latex=r"Q_1 - 1{,}5\text{IQR} \quad \text{or} \quad Q_3 + 1{,}5\text{IQR}",
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        misconception_tags=["used_semi_iqr_instead_of_1.5_iqr", "confused_lower_and_upper_fence"],
        keywords=["outlier", "IQR", "interquartile range", "1.5 IQR rule", "statistics"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_iqr_outlier",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Sub-drill 3: elementary_skewness_analysis (3 marks)
# --------------------------------------------------------------------------- #
def _build_skewness_analysis_drill(r, difficulty: str) -> Dict[str, Any]:
    """Scaffolding drill: Analyze box-and-whisker plot skewness with formal justification."""
    skew_type = r.choice(["right", "left", "symmetrical"])

    med = r.randint(45, 60)
    if skew_type == "right":
        d_left = r.randint(6, 10)
        d_right = d_left + r.randint(5, 10)  # Q3 further from Med
        concl_str = "SKEWED TO THE RIGHT (POSITIVELY SKEWED)"
        reason_math = rf"Q_3 - \text{{Median}} = {d_right} > \text{{Median}} - Q_1 = {d_left}"
    elif skew_type == "left":
        d_right = r.randint(6, 10)
        d_left = d_right + r.randint(5, 10)  # Q1 further from Med
        concl_str = "SKEWED TO THE LEFT (NEGATIVELY SKEWED)"
        reason_math = rf"\text{{Median}} - Q_1 = {d_left} > Q_3 - \text{{Median}} = {d_right}"
    else:
        d_left = r.randint(8, 12)
        d_right = d_left
        concl_str = "SYMMETRICAL"
        reason_math = rf"Q_3 - \text{{Median}} = \text{{Median}} - Q_1 = {d_left}"

    q1 = med - d_left
    q3 = med + d_right
    min_v = q1 - r.randint(10, 16)
    max_v = q3 + r.randint(10, 16)

    prompt = (
        f"A box-and-whisker plot has the following summary values:\n\n"
        f"$$\\text{{Min}} = {min_v}, \\quad Q_1 = {q1}, \\quad \\text{{Median}} = {med}, \\quad "
        f"Q_3 = {q3}, \\quad \\text{{Max}} = {max_v}$$\n\n"
        f"1. Calculate the distance between $Q_1$ and the Median, and between the Median and $Q_3$. (1)\n"
        f"2. Comment on the skewness (distribution) of the data. Fully justify your answer. (2)"
    )

    steps = [
        step(
            from_latex=rf"\text{{Median}} - Q_1 = {med} - {q1} = {d_left}, \quad Q_3 - \text{{Median}} = {q3} - {med} = {d_right}",
            to_latex_str=rf"\text{{Distances: }} {d_left} \text{{ and }} {d_right}",
            op="calculate distances between median and lower/upper quartiles",
            rule="box-and-whisker quartile dispersion analysis",
        ),
        step(
            from_latex=reason_math,
            to_latex_str=rf"\text{{Conclusion: The data is }} \textbf{{{concl_str}}}",
            op="compare quartile intervals and deduce skewness",
            rule="skewness criteria from five-number summary",
        ),
    ]

    canonical = solution_graph(
        goal="determine skewness of distribution from box-and-whisker summary",
        steps=steps,
        final_latex=rf"\text{{{concl_str}}} \quad ({reason_math})",
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": rf"Correct calculation of distances: Med - Q1 = {d_left} and Q3 - Med = {d_right}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"Correct identification of skewness: {concl_str}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"Valid mathematical justification: {reason_math}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "stated_skewness_without_justification", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": r"Compare $(Q_3 - \text{Median})$ with $(\text{Median} - Q_1)$.",
        "concept": "If the upper box $(Q_3 - \\text{Median})$ is wider than the lower box $(\\text{Median} - Q_1)$, data is skewed right. If the lower box is wider, data is skewed left. If equal, it is symmetrical.",
        "breakdown": f"1. $\\text{{Median}} - Q_1 = {med} - {q1} = {d_left}$.\n2. $Q_3 - \\text{{Median}} = {q3} - {med} = {d_right}$.\n3. ${reason_math} \\implies \\textbf{{{concl_str}}}$.",
    }

    diag = {
        "kind": "box_and_whisker",
        "min": min_v,
        "q1": q1,
        "median": med,
        "q3": q3,
        "max": max_v,
        "skewness": concl_str,
    }

    return make_math_question(
        prefix="stat_skew",
        topic=TOPIC,
        subskill="elementary_skewness_analysis",
        learning_objective_id=f"{LO}_skewness_analysis",
        prompt=prompt,
        prompt_latex=rf"\text{{Min}} = {min_v}, \; Q_1 = {q1}, \; \text{{Med}} = {med}, \; Q_3 = {q3}, \; \text{{Max}} = {max_v}",
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        diagram_spec=diag,
        misconception_tags=["inverted_skewness_rule", "compared_whiskers_incorrectly"],
        keywords=["skewness", "box-and-whisker", "positively skewed", "negatively skewed", "symmetry"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=4,
        mode="elementary_skewness_analysis",
        difficulty=difficulty,
    )


# --------------------------------------------------------------------------- #
# Compound Exam Ceiling: mode="compound" (10 marks)
# --------------------------------------------------------------------------- #
def _build_compound_statistics_exam(r, difficulty: str) -> Dict[str, Any]:
    """10-Mark NSC Paper 2 Comprehensive Statistics Examination Question:
    Part 1 (3 marks): Five-number summary and Interquartile Range (IQR).
    Part 2 (2 marks): Outlier test using 1,5 x IQR rule on minimum or maximum.
    Part 3 (2 marks): Box-and-whisker skewness analysis with mathematical justification.
    Part 4 (3 marks): Ogive cumulative frequency curve reading & One standard deviation interval.
    """
    # ------------------ Part 1, 2, 3: Ungrouped Data (N = 15) ----------------- #
    # Construct 15 sorted test scores
    # Ensure controlled skewness and an outlier at the top or bottom
    skew_choice = r.choice(["right", "left"])
    if skew_choice == "right":
        # Clustered lower values, stretched upper values
        s_vals = [28, 32, 35, 38, 40, 42, 44, 46, 50, 54, 58, 64, 70, 78, 96]
    else:
        # Stretched lower values, clustered upper values
        s_vals = [12, 30, 36, 42, 46, 50, 54, 56, 58, 60, 62, 64, 66, 70, 74]

    summary = _compute_summary(s_vals)
    min_v = summary["min"]
    q1_v = int(summary["q1"])
    med_v = int(summary["median"])
    q3_v = int(summary["q3"])
    max_v = summary["max"]
    iqr_v = int(summary["iqr"])
    lower_fence = summary["lower_fence"]
    upper_fence = summary["upper_fence"]
    outliers = summary["outliers"]

    has_outlier = len(outliers) > 0
    if has_outlier:
        outlier_val = outliers[0]
        outlier_concl = (
            rf"{outlier_val} \text{{ is an outlier because }} "
            rf"{outlier_val} {'<' if outlier_val < lower_fence else '>'} "
            rf"{num(lower_fence if outlier_val < lower_fence else upper_fence, 1)}"
        )
    else:
        outlier_concl = rf"\text{{There are no outliers since all values lie within }}[{num(lower_fence, 1)}; {num(upper_fence, 1)}]"

    data_list_str = ", ".join(str(x) for x in s_vals)

    # ------------------ Part 4: Grouped Ogive & Standard Deviation ------------- #
    # 50 learners' test marks grouped in intervals of 10
    # Clean integer mean and standard deviation
    intervals = ["20 \\le x < 30", "30 \\le x < 40", "40 \\le x < 50", "50 \\le x < 60", "60 \\le x < 70"]
    freqs = [4, 8, 18, 14, 6]
    cum_freqs = [4, 12, 30, 44, 50]
    total_grouped = 50

    # Midpoints: 25, 35, 45, 55, 65
    # Sum f*x = 4*25 + 8*35 + 18*45 + 14*55 + 6*65 = 100 + 280 + 810 + 770 + 390 = 2350
    # Mean = 2350 / 50 = 47
    mean_val = 47.0
    # Sum f*(x - mean)^2 = 4*(484) + 8*(144) + 18*(4) + 14*(64) + 6*(324) = 6000
    # Variance = 6000 / 50 = 120
    # Std dev = sqrt(120) = 10.95
    sd_val = round(math.sqrt(120.0), 2)
    sd_str = num(sd_val, 2)
    mean_str = num(mean_val, 1)

    sd_lower = round(mean_val - sd_val, 2)
    sd_upper = round(mean_val + sd_val, 2)
    sd_interval_str = rf"({num(sd_lower, 2)}; {num(sd_upper, 2)})"

    # From cumulative frequency ogive:
    # Median is read at cum_freq = 50 / 2 = 25.
    # At cf = 25, lies in interval 40 - 50:
    # Linear interpolation: 40 + (25 - 12) / 18 * 10 = 40 + 130 / 18 ≈ 47.2
    est_med_ogive = 47.2

    # Number of learners within 1 std dev (36.05 to 57.95):
    # From table: approx 34 learners (68% of 50)
    percent_within_sd = 68.0

    prompt_table = (
        r"\begin{array}{|c|c|c|}"
        r"\hline"
        r"\textbf{Class Interval} & \textbf{Frequency } (f) & \textbf{Cumulative Frequency} \\ \hline"
        rf"20 \le x < 30 & 4 & 4 \\ \hline"
        rf"30 \le x < 40 & 8 & 12 \\ \hline"
        rf"40 \le x < 50 & 18 & 30 \\ \hline"
        rf"50 \le x < 60 & 14 & 44 \\ \hline"
        rf"60 \le x < 70 & 6 & 50 \\ \hline"
        r"\end{array}"
    )

    prompt = (
        f"QUESTION 3 (10 MARKS)\n\n"
        f"3.1 The following ordered data set shows the final exam marks (out of 100) of 15 Grade 11 learners:\n\n"
        f"$${data_list_str}$$\n\n"
        f"    (a) Write down the five-number summary for this data set and calculate the Interquartile Range (IQR). (3)\n"
        f"    (b) Show whether any score in this data set is an OUTLIER using the $1{{,}}5 \\times \\text{{IQR}}$ rule. (2)\n"
        f"    (c) Comment on the skewness (distribution) of the data set. Provide a clear mathematical reason. (2)\n\n"
        f"3.2 The cumulative frequency distribution below records the results of a larger sample of 50 learners:\n\n"
        f"$${prompt_table}$$\n\n"
        f"    (a) Use the cumulative frequency table to estimate the median score from the ogive curve (at cumulative frequency $= 25$). (1)\n"
        f"    (b) The estimated mean of this grouped data is $\\bar{{x}} = {mean_str}$ and the standard deviation is $\\sigma = {sd_str}$. "
        f"Determine the interval representing ONE standard deviation of the mean, and state what percentage of learners "
        f"expectedly fall within this interval for a normal distribution. (2)"
    )

    steps = [
        # 3.1 (a)
        step(
            from_latex=rf"\text{{Data: }} {data_list_str}",
            to_latex_str=(
                rf"\text{{Min}} = {min_v}, \; Q_1 = {q1_v}, \; \text{{Median}} = {med_v}, \; "
                rf"Q_3 = {q3_v}, \; \text{{Max}} = {max_v}; \quad \text{{IQR}} = {q3_v} - {q1_v} = {iqr_v}"
            ),
            op="determine five-number summary values and compute IQR",
            rule="five-number summary and IQR definition",
        ),
        # 3.1 (b)
        step(
            from_latex=rf"\text{{Fences: }} Q_1 - 1{{,}}5({iqr_v}) = {num(lower_fence, 1)}, \quad Q_3 + 1{{,}}5({iqr_v}) = {num(upper_fence, 1)}",
            to_latex_str=outlier_concl,
            op="evaluate outlier boundaries and compare with extreme data values",
            rule="1.5 x IQR outlier rule",
        ),
        # 3.1 (c)
        step(
            from_latex=rf"Q_3 - \text{{Median}} = {q3_v - med_v}, \quad \text{{Median}} - Q_1 = {med_v - q1_v}",
            to_latex_str=rf"\text{{Data is }} \textbf{{{summary['skewness']}}} \quad ({summary['skew_reason']})",
            op="compare distance between median and quartiles to deduce skewness",
            rule="distribution skewness criterion",
        ),
        # 3.2 (a) & (b)
        step(
            from_latex=rf"\text{{Ogive Median at cf}} = 25 \implies \text{{Estimated Median}} \approx {num(est_med_ogive, 1)}",
            to_latex_str=(
                rf"(\bar{{x}} - \sigma; \; \bar{{x}} + \sigma) = {sd_interval_str}; \quad "
                rf"\text{{Percentage within }} 1\sigma \approx {num(percent_within_sd, 0)}\%"
            ),
            op="read median from cumulative frequency and compute standard deviation interval",
            rule="dispersion interval and normal distribution property",
        ),
    ]

    canonical = solution_graph(
        goal="complete 10-mark Grade 11 statistics examination question",
        steps=steps,
        final_latex=(
            rf"3.1(a) \; \text{{Min}} = {min_v}, \; Q_1 = {q1_v}, \; \text{{Med}} = {med_v}, \; Q_3 = {q3_v}, \; \text{{Max}} = {max_v}, \; \text{{IQR}} = {iqr_v}; \quad "
            rf"3.1(b) \; {outlier_concl}; \quad "
            rf"3.1(c) \; \text{{{summary['skewness']}}}; \quad "
            rf"3.2(a) \; \approx {num(est_med_ogive, 1)}; \quad "
            rf"3.2(b) \; {sd_interval_str} \text{{ with }} {num(percent_within_sd, 0)}\%"
        ),
    )

    marking_schema = {
        "total_marks": 10,
        "marking_points": [
            # 3.1 (a) - 3 marks
            {"id": "mp1", "desc": rf"3.1(a) Correct Median = {med_v}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": rf"3.1(a) Correct Q1 = {q1_v} and Q3 = {q3_v}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": rf"3.1(a) Correct IQR = {iqr_v}", "marks": 1, "editable": True},
            # 3.1 (b) - 2 marks
            {"id": "mp4", "desc": rf"3.1(b) Correct lower fence ({num(lower_fence, 1)}) or upper fence ({num(upper_fence, 1)})", "marks": 1, "editable": True},
            {"id": "mp5", "desc": rf"3.1(b) Correct outlier identification and conclusion", "marks": 1, "editable": True},
            # 3.1 (c) - 2 marks
            {"id": "mp6", "desc": rf"3.1(c) Correct skewness statement: {summary['skewness']}", "marks": 1, "editable": True},
            {"id": "mp7", "desc": rf"3.1(c) Valid mathematical justification: {summary['skew_reason']}", "marks": 1, "editable": True},
            # 3.2 (a) - 1 mark
            {"id": "mp8", "desc": rf"3.2(a) Reading estimated median from ogive at cf = 25 (approx 46 - 48)", "marks": 1, "editable": True},
            # 3.2 (b) - 2 marks
            {"id": "mp9", "desc": rf"3.2(b) Correct interval: {sd_interval_str}", "marks": 1, "editable": True},
            {"id": "mp10", "desc": rf"3.2(b) Correct percentage within one standard deviation: approx 68%", "marks": 1, "editable": True},
        ],
        "deductions": [
            {"rule": "inverted_skewness", "penalty": -1},
            {"rule": "stated_outlier_without_proof", "penalty": -1},
        ],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "nudge": "Break down each question part: 3.1 uses the five-number summary and IQR formulas, while 3.2 involves reading from the cumulative frequency table/ogive and calculating the standard deviation interval.",
        "concept": (
            "Key CAPS Statistics principles:\n"
            "• Outlier rule: $x < Q_1 - 1{,}5\\text{IQR}$ or $x > Q_3 + 1{,}5\\text{IQR}$\n"
            "• Skewness: compare $(Q_3 - \\text{Median})$ with $(\\text{Median} - Q_1)$\n"
            "• Ogive median: locate cumulative frequency $N/2 = 25$ on the vertical axis and read across to the curve\n"
            "• One standard deviation interval: $(\\bar{x} - \\sigma; \\bar{x} + \\sigma)$ contains approx 68% of data for normal distributions."
        ),
        "breakdown": (
            f"3.1(a) Median = {med_v}, $Q_1 = {q1_v}$, $Q_3 = {q3_v}$, $\\text{{IQR}} = {iqr_v}$.\n"
            f"3.1(b) Lower fence = ${num(lower_fence, 1)}$, Upper fence = ${num(upper_fence, 1)}$. {outlier_concl}.\n"
            f"3.1(c) ${summary['skew_reason']} \\implies \\text{{{summary['skewness']}}}$.\n"
            f"3.2(a) At cf = 25, median $\\approx {num(est_med_ogive, 1)}$.\n"
            f"3.2(b) Interval: $({mean_str} - {sd_str}; {mean_str} + {sd_str}) = {sd_interval_str}$, containing $\\approx 68\\%$ of data."
        ),
    }

    diag = {
        "kind": "statistics_box_and_ogive",
        "box_and_whisker": {
            "min": min_v,
            "q1": q1_v,
            "median": med_v,
            "q3": q3_v,
            "max": max_v,
            "iqr": iqr_v,
            "outliers": outliers,
            "skewness": summary["skewness"],
        },
        "ogive_curve": {
            "intervals": intervals,
            "frequencies": freqs,
            "cumulative_frequencies": cum_freqs,
            "points": [[20, 0], [30, 4], [40, 12], [50, 30], [60, 44], [70, 50]],
            "median_lookup": {"cf": 25, "estimated_mark": est_med_ogive},
        },
    }

    return make_math_question(
        prefix="stat_exam_compound",
        topic=TOPIC,
        subskill="statistics_summary_ogive_compound",
        learning_objective_id=f"{LO}_compound_exam",
        prompt=prompt,
        prompt_latex=r"\text{Five-number summary, Ogive and } \sigma",
        answer_latex=canonical["final_latex"],
        answer_sympy=canonical["final_latex"],
        sample_answer=canonical["final_latex"],
        canonical_solution=canonical,
        marking_schema=marking_schema,
        hints=hints,
        diagram_spec=diag,
        misconception_tags=[
            "inverted_skewness_rule",
            "used_semi_iqr_instead_of_1.5_iqr",
            "read_ogive_horizontal_instead_of_vertical",
            "confused_standard_deviation_with_variance",
        ],
        keywords=["five-number summary", "ogive", "outlier test", "standard deviation", "skewness", "NSC Paper 2"],
        term=4,
        caps_weight_percent=15,
        suggested_duration_mins=15,
        mode="compound",
        difficulty="hard",
    )


# --------------------------------------------------------------------------- #
# Public Dispatcher & API
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_statistics_exam,
    "elementary_five_number_summary": _build_five_number_summary_drill,
    "elementary_iqr_outlier": _build_iqr_outlier_drill,
    "elementary_skewness_analysis": _build_skewness_analysis_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 11 Statistics questions meeting the 6-pillar contract."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_statistics_exam)

    questions = []
    for i in range(max(1, count)):
        r = rng(base_seed * 1000 + i)
        q = builder(r, difficulty)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
