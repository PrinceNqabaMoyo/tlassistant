"""Subskills 09 to 16: Child & Adolescent BMI-for-Age Growth Charts & Percentiles.
Covers BMI calculations for children, looking up percentiles on CDC/Road to Health curves,
classifying weight status (Underweight, Healthy, At Risk, Overweight),
contrasting adult cut-offs with age-dependent percentile trajectories,
and analyzing longitudinal growth curve tracking and percentile channel crossing.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_09(r: random.Random) -> Dict[str, Any]:
    """Subskill 09: Calculating child BMI and reading BMI-for-age percentile for girls."""
    name = r.choice(["Amy", "Nontando", "Lerato", "Zanele"])
    age = r.choice([9, 10, 12, 14])
    # Approximate percentiles for girls around age 9-14
    # Age 9: 14.0 (25th), 16.0 (50th), 18.2 (85th), 19.8 (90th-95th)
    # Age 12: 15.5 (25th), 18.0 (50th), 21.0 (85th), 23.5 (95th)
    cases = {
        9: (33.0, 1.29, 19.83, "90th percentile"),
        10: (32.0, 1.38, 16.80, "60th percentile"),
        12: (46.0, 1.52, 19.91, "70th percentile"),
        14: (50.0, 1.58, 20.03, "55th percentile"),
    }
    w, h, b, perc = cases[age]

    d_spec_09 = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"Girls BMI-for-Age Growth Curves ({name}, Age {age})",
        "x_label": "Age (years)",
        "y_label": "BMI (kg/m²)",
        "series": [
            {"name": "50th Percentile", "points": [[9, 16.0], [10, 16.6], [12, 18.0], [14, 19.5]]},
            {"name": f"{name}'s BMI", "points": [[age, b]]},
        ],
    }

    table_data = {
        "headers": ["Age (Years)", "5th Percentile", "50th Percentile (Median)", "85th Percentile", "95th Percentile"],
        "rows": [
            ["9 years", "13,5 kg/m²", "16,0 kg/m²", "18,2 kg/m²", "21,0 kg/m²"],
            ["10 years", "14,0 kg/m²", "16,6 kg/m²", "19,0 kg/m²", "22,0 kg/m²"],
            ["12 years", "15,0 kg/m²", "18,0 kg/m²", "21,0 kg/m²", "24,5 kg/m²"],
            ["14 years", "16,0 kg/m²", "19,5 kg/m²", "22,8 kg/m²", "26,0 kg/m²"],
        ]
    }

    prompt = (
        f"{name} is a {age}-year-old girl. She weighs {_fmt(w)} kg and is {_fmt(h)} m tall.\n\n"
        f"1. Calculate {name}'s BMI in kg/m² (Formula: BMI = Weight ÷ [Height]²).\n"
        f"2. Refer to the Girls BMI-for-Age Percentile Table below.\n"
        f"Estimate {name}'s approximate percentile position on the growth chart."
    )

    correct_ans = f"BMI = {_fmt(b, 2)} kg/m² (approx. {perc})"
    explanation = (
        f"1. BMI = {_fmt(w)} ÷ ({_fmt(h)})² = {_fmt(w)} ÷ {_fmt(h**2, 4)} = {_fmt(b, 2)} kg/m².\n"
        f"2. For a {age}-year-old girl, {_fmt(b, 2)} kg/m² places her at {perc}."
    )
    t1 = "Calculate Weight ÷ Height², then find the corresponding percentile column for her age."
    t2 = f"{w} ÷ ({h})² = {_fmt(b, 2)} kg/m². Compare with table row for {age} years."
    t3 = f"Growth position: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"BMI = {_fmt(b, 2)} kg/m² (approx. 25th percentile)",
        f"BMI = {_fmt(round(w / h, 2))} kg/m² (approx. {perc})",
        f"BMI = {_fmt(b, 2)} kg/m² (approx. 98th percentile)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_09",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="medium",
        diagram_spec=d_spec_09,
    )


def gen_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: Calculating child BMI and reading BMI-for-age percentile for boys."""
    name = r.choice(["Sipho", "Kagiso", "Lwazi", "Johan"])
    age = r.choice([11, 13, 15, 16])

    cases = {
        11: (38.0, 1.45, 18.07, "65th percentile"),
        13: (45.0, 1.56, 18.49, "50th percentile (Median)"),
        15: (58.0, 1.70, 20.07, "55th percentile"),
        16: (55.45, 1.78, 17.50, "10th percentile"),
    }
    w, h, b, perc = cases[age]

    d_spec_09 = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"Girls BMI-for-Age Growth Curves ({name}, Age {age})",
        "x_label": "Age (years)",
        "y_label": "BMI (kg/m²)",
        "series": [
            {"name": "50th Percentile", "points": [[9, 16.0], [10, 16.6], [12, 18.0], [14, 19.5]]},
            {"name": f"{name}'s BMI", "points": [[age, b]]},
        ],
    }

    table_data = {
        "headers": ["Age (Years)", "5th Percentile", "50th Percentile (Median)", "85th Percentile", "95th Percentile"],
        "rows": [
            ["11 years", "14,5 kg/m²", "17,2 kg/m²", "20,5 kg/m²", "23,5 kg/m²"],
            ["13 years", "15,5 kg/m²", "18,5 kg/m²", "22,0 kg/m²", "25,5 kg/m²"],
            ["15 years", "16,8 kg/m²", "19,8 kg/m²", "23,5 kg/m²", "27,0 kg/m²"],
            ["16 years", "17,2 kg/m²", "20,5 kg/m²", "24,2 kg/m²", "27,8 kg/m²"],
        ]
    }

    prompt = (
        f"{name} is a {age}-year-old boy. He weighs {_fmt(w, 2)} kg and stands {_fmt(h, 2)} m tall.\n\n"
        f"1. Calculate {name}'s BMI in kg/m² (Formula: BMI = Weight ÷ [Height]²).\n"
        f"2. Refer to the Boys BMI-for-Age Percentile Table below.\n"
        f"Determine {name}'s approximate percentile position on the growth chart."
    )

    correct_ans = f"BMI = {_fmt(b, 2)} kg/m² (approx. {perc})"
    explanation = (
        f"1. BMI = {_fmt(w, 2)} ÷ ({_fmt(h, 2)})² = {_fmt(w, 2)} ÷ {_fmt(h**2, 4)} = {_fmt(b, 2)} kg/m².\n"
        f"2. In the {age}-year row, {_fmt(b, 2)} kg/m² aligns with {perc}."
    )
    t1 = "Calculate Weight ÷ Height², then look up the value in the table row for his age."
    t2 = f"{w} ÷ ({h})² = {_fmt(b, 2)} kg/m². Compare with {age}-year-old benchmarks."
    t3 = f"Position: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"BMI = {_fmt(b, 2)} kg/m² (approx. 90th percentile)",
        f"BMI = {_fmt(round(w / h, 2))} kg/m² (approx. {perc})",
        f"BMI = {_fmt(b, 2)} kg/m² (approx. 5th percentile)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_10",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="medium",
        diagram_spec=d_spec_09,
    )


def gen_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Subskill 11: Child weight status classification: Underweight (< 5th percentile)."""
    name = r.choice(SA_NAMES)
    percentile = r.choice([2, 3, 4])

    prompt = (
        f"A clinic sister plots {name}'s BMI on the Road to Health growth chart and observes that "
        f"{name}'s point lies on the {percentile}rd/th percentile curve.\n\n"
        f"According to standard pediatric guidelines:\n"
        f"• Less than 5th percentile = Underweight\n"
        f"• 5th to < 85th percentile = Healthy weight\n"
        f"• 85th to < 95th percentile = At risk of overweight\n"
        f"• 95th percentile and above = Overweight\n\n"
        f"Classify {name}'s weight status."
    )

    correct_ans = "Underweight (< 5th percentile)"
    explanation = (
        f"1. {name}'s position is at the {percentile}th percentile.\n"
        f"2. Any position below the 5th percentile is classified as Underweight."
    )
    t1 = "Check which category corresponds to a percentile lower than 5."
    t2 = f"{percentile}th percentile is less than the 5th percentile cutoff."
    t3 = f"Classification = {correct_ans}."

    custom_opts = [
        correct_ans,
        "Healthy weight (5th to < 85th percentile)",
        "At risk of overweight (85th to < 95th percentile)",
        "Overweight (≥ 95th percentile)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_11",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Subskill 12: Child weight status classification: Healthy weight (5th to < 85th percentile)."""
    name = r.choice(SA_NAMES)
    percentile = r.choice([25, 40, 50, 70, 75])

    prompt = (
        f"A school nurse checks {name}'s health card and finds that his BMI-for-age is located on "
        f"the {percentile}th percentile curve.\n\n"
        f"Refer to the weight status criteria:\n"
        f"• Underweight: < 5th percentile\n"
        f"• Healthy weight: ≥ 5th and < 85th percentile\n"
        f"• At risk of overweight: ≥ 85th and < 95th percentile\n"
        f"• Overweight: ≥ 95th percentile\n\n"
        f"What is {name}'s weight status classification?"
    )

    correct_ans = "Healthy weight (≥ 5th and < 85th percentile)"
    explanation = (
        f"1. {name}'s percentile is {percentile}th.\n"
        f"2. Since 5 ≤ {percentile} < 85, {name} falls within the healthy weight bracket."
    )
    t1 = "Check where the given percentile lies relative to 5 and 85."
    t2 = f"{percentile} is between 5 and 85."
    t3 = f"Weight status = {correct_ans}."

    custom_opts = [
        correct_ans,
        "Underweight (< 5th percentile)",
        "At risk of overweight (≥ 85th and < 95th percentile)",
        "Overweight (≥ 95th percentile)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_12",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Child weight status classification: At risk of overweight (85th to < 95th percentile)."""
    name = r.choice(SA_NAMES)
    percentile = r.choice([86, 88, 90, 92])

    d_spec_13 = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"Pediatric BMI-for-Age Growth Curves ({name}, {percentile}th Percentile)",
        "categories": ["5th", "50th", "85th", f"{name} ({percentile}th)", "95th"],
        "values": [14.0, 16.5, 18.5, 19.2, 20.5],
        "series": [
            {"name": "BMI Thresholds", "values": [14.0, 16.5, 18.5, 19.2, 20.5]}
        ],
    }

    prompt = (
        f"Refer to the pediatric BMI-for-age growth chart shown in the diagram.\n"
        f"During an annual routine school health screening, {name}'s BMI is plotted at the "
        f"{percentile}th percentile.\n\n"
        f"Categorize {name}'s weight status using standard pediatric percentile classifications."
    )

    correct_ans = "At risk of overweight (≥ 85th and < 95th percentile)"
    explanation = (
        f"1. {name}'s BMI is at the {percentile}th percentile.\n"
        f"2. Values between the 85th and 95th percentiles are classified as 'At risk of overweight'."
    )
    t1 = "Check the classification for percentiles between 85 and 95."
    t2 = f"{percentile} falls between 85 and 95."
    t3 = f"Classification = {correct_ans}."

    custom_opts = [
        correct_ans,
        "Healthy weight (≥ 5th and < 85th percentile)",
        "Overweight (≥ 95th percentile)",
        "Underweight (< 5th percentile)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_13",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_13,
    )


def gen_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Subskill 14: Child weight status classification: Overweight (>= 95th percentile)."""
    name = r.choice(SA_NAMES)
    percentile = r.choice([95, 96, 98])

    prompt = (
        f"A pediatric endocrinologist reviews a child's Road to Health card and observes that {name}'s "
        f"BMI-for-age curve has tracked along the {percentile}th percentile.\n\n"
        f"Classify {name}'s weight status according to standard growth chart benchmarks."
    )

    correct_ans = "Overweight (≥ 95th percentile)"
    explanation = (
        f"1. {name} is at or above the 95th percentile ({percentile}th).\n"
        f"2. A percentile position ≥ 95th on pediatric growth charts is classified as Overweight."
    )
    t1 = "Identify the category corresponding to percentiles at or above 95."
    t2 = f"{percentile} ≥ 95 indicates Overweight."
    t3 = f"Classification = {correct_ans}."

    custom_opts = [
        correct_ans,
        "At risk of overweight (≥ 85th and < 95th percentile)",
        "Healthy weight (≥ 5th and < 85th percentile)",
        "Underweight (< 5th percentile)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_14",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Subskill 15: Age vs BMI comparison: Why identical BMI values have different health classifications."""
    prompt = (
        f"Two girls both have an identical BMI of 19,8 kg/m²:\n"
        f"• Amy is 9 years old: on the girls' growth chart, 19,8 kg/m² lies on the 90th percentile.\n"
        f"• Nontando is 12 years old: on the girls' growth chart, 19,8 kg/m² lies below the 75th percentile.\n\n"
        f"Explain why two children with the exact same numerical BMI have different weight status classifications."
    )

    correct_ans = "Children are constantly growing and developing, so BMI norms change significantly with age"
    explanation = (
        f"1. In adults, height is constant, so fixed numerical BMI cutoffs (18,5 to 24,9) apply.\n"
        f"2. In growing children, body composition and height change dynamically every year.\n"
        f"3. A BMI of 19,8 kg/m² is high for a 9-year-old (90th percentile = at risk of overweight), "
        f"but normal for a 12-year-old (below 75th percentile = healthy weight)."
    )
    t1 = "Think about growth: children change in height and body fat ratio as they get older."
    t2 = "A single numerical BMI cannot be evaluated without comparing it to peers of the exact same age and gender."
    t3 = f"Core reason: {correct_ans}."

    custom_opts = [
        correct_ans,
        "The formula for calculating BMI is completely different for 9-year-olds than for 12-year-olds",
        "Amy's height was measured incorrectly in metres instead of centimetres",
        "Both girls must have the exact same weight status because their calculated numbers are equal",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_15",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Subskill 16: Percentile curve tracking: evaluating longitudinal growth stability vs sudden upward crossing."""
    prompt = (
        f"A clinic sister monitors a boy's BMI over 3 years:\n"
        f"• At age 7: 50th percentile\n"
        f"• At age 8: 52nd percentile\n"
        f"• At age 9: 92nd percentile\n\n"
        f"How should the clinic sister interpret this child's growth trajectory from age 8 to 9?"
    )

    correct_ans = "A rapid upward crossing of percentile channels indicates abnormal weight gain requiring intervention"
    explanation = (
        f"1. A healthy child normally tracks steadily along their established percentile channel (e.g. around the 50th percentile).\n"
        f"2. Jumping abruptly from the 52nd percentile to the 92nd percentile in one year indicates sudden rapid weight gain.\n"
        f"3. This puts the child 'At risk of overweight' and warrants dietary and clinical evaluation."
    )
    t1 = "Normal growth follows the same percentile curve; crossing multiple channels upward indicates rapid weight gain."
    t2 = "Jumping from 52nd to 92nd percentile is abnormal."
    t3 = f"Clinical assessment: {correct_ans}."

    custom_opts = [
        correct_ans,
        "The child's growth is completely normal because he is getting older",
        "The child is severely malnourished and underweight because his percentile number changed",
        "The percentile increase proves that the child had a sudden growth spurt in height",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_16",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )
