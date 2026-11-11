"""Subskills 17 to 24: Stature-for-Age, Weight-for-Age Percentiles & Anthropometric Assessment.
Covers stature and weight growth charts for boys and girls, statistical percentile interpretations,
the 50th percentile median benchmark, detecting chronic stunting (< 5th percentile height),
and identifying acute wasting (< 5th percentile weight with preserved stature).
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Subskill 17: Reading Stature (Height)-for-age percentile for boys."""
    age = r.choice([12, 14, 16])
    # Benchmarks for boys height:
    # Age 12: 137 cm (5th), 149 cm (50th), 160 cm (95th)
    # Age 14: 150 cm (5th), 164 cm (50th), 176 cm (95th)
    # Age 16: 162 cm (5th), 173 cm (50th), 178 cm (75th), 185 cm (95th)
    cases = {
        12: (149.0, "50th percentile (Median)"),
        14: (170.0, "75th percentile"),
        16: (178.0, "75th percentile"),
    }
    height_cm, perc = cases[age]

    d_spec_17 = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"Boys Stature-for-Age Growth Curves (Age {age})",
        "x_label": "Age (years)",
        "y_label": "Height (cm)",
        "series": [
            {"name": "50th Percentile", "points": [[12, 149.0], [14, 164.0], [16, 173.0]]},
            {"name": "Recorded Height", "points": [[age, height_cm]]},
        ],
    }

    table_data = {
        "headers": ["Age (Years)", "5th Percentile", "25th Percentile", "50th Percentile (Median)", "75th Percentile", "95th Percentile"],
        "rows": [
            ["12 years", "137 cm", "143 cm", "149 cm", "154 cm", "160 cm"],
            ["14 years", "150 cm", "157 cm", "164 cm", "170 cm", "176 cm"],
            ["16 years", "162 cm", "168 cm", "173 cm", "178 cm", "185 cm"],
        ]
    }

    prompt = (
        f"A 16-year-old boy named Thabo is measured at the clinic. His height is recorded as {height_cm} cm.\n\n"
        f"Refer to the Stature-for-Age Table for Boys below.\n"
        f"Determine Thabo's height percentile on the growth chart."
    ) if age == 16 else (
        f"A {age}-year-old boy is measured at {height_cm} cm.\n\n"
        f"Refer to the Stature-for-Age Table for Boys below.\n"
        f"Determine his height percentile on the growth chart."
    )

    correct_ans = perc
    explanation = (
        f"1. Locate row '{age} years' in the Stature-for-Age Table.\n"
        f"2. {height_cm} cm aligns exactly with the {perc} column."
    )
    t1 = "Find the row for the child's age, then match the measured height in centimetres."
    t2 = f"{height_cm} cm in the {age}-year row corresponds to {perc}."
    t3 = f"Percentile = {correct_ans}."

    all_percs = ["5th Percentile", "25th Percentile", "50th Percentile (Median)", "75th Percentile", "95th Percentile"]
    custom_opts = [correct_ans] + [p for p in all_percs if p != correct_ans][:3]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_17",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="easy",
        diagram_spec=d_spec_17,
    )


def gen_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Subskill 18: Reading Stature (Height)-for-age percentile for girls."""
    age = r.choice([11, 13, 15])
    cases = {
        11: (144.0, "50th percentile (Median)"),
        13: (162.0, "75th percentile"),
        15: (162.0, "50th percentile (Median)"),
    }
    height_cm, perc = cases[age]

    d_spec_17 = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"Boys Stature-for-Age Growth Curves (Age {age})",
        "x_label": "Age (years)",
        "y_label": "Height (cm)",
        "series": [
            {"name": "50th Percentile", "points": [[12, 149.0], [14, 164.0], [16, 173.0]]},
            {"name": "Recorded Height", "points": [[age, height_cm]]},
        ],
    }

    table_data = {
        "headers": ["Age (Years)", "5th Percentile", "25th Percentile", "50th Percentile (Median)", "75th Percentile", "95th Percentile"],
        "rows": [
            ["11 years", "133 cm", "139 cm", "144 cm", "150 cm", "156 cm"],
            ["13 years", "145 cm", "151 cm", "156 cm", "162 cm", "168 cm"],
            ["15 years", "151 cm", "157 cm", "162 cm", "167 cm", "172 cm"],
        ]
    }

    prompt = (
        f"A {age}-year-old girl named Nandi is measured at the school health desk. Her height is {height_cm} cm.\n\n"
        f"Refer to the Stature-for-Age Table for Girls below.\n"
        f"Identify Nandi's height percentile position."
    )

    correct_ans = perc
    explanation = (
        f"1. Locate row '{age} years' in the Stature-for-Age Table for Girls.\n"
        f"2. Her height of {height_cm} cm corresponds to the {perc} column."
    )
    t1 = "Read across the row matching the girl's age to locate her height."
    t2 = f"{height_cm} cm matches {perc} for age {age}."
    t3 = f"Position = {correct_ans}."

    all_percs = ["5th Percentile", "25th Percentile", "50th Percentile (Median)", "75th Percentile", "95th Percentile"]
    custom_opts = [correct_ans] + [p for p in all_percs if p != correct_ans][:3]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_18",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="easy",
    )


def gen_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Subskill 19: Reading Weight-for-age percentile for boys."""
    age = 16
    weight_kg = 55.45

    table_data = {
        "headers": ["Age (Years)", "5th Percentile", "10th Percentile", "25th Percentile", "50th Percentile (Median)", "75th Percentile"],
        "rows": [
            ["16 years", "48,5 kg", "52,0 kg", "57,5 kg", "64,0 kg", "72,0 kg"],
        ]
    }

    prompt = (
        f"A 16-year-old boy has a body weight of {_fmt(weight_kg, 2)} kg.\n\n"
        f"Refer to the Weight-for-Age Table for 16-Year-Old Boys below.\n"
        f"Between which two percentile curves does the boy's weight fall?"
    )

    correct_ans = "Between the 10th and 25th percentile"
    explanation = (
        f"1. 52,0 kg (10th percentile) < {_fmt(weight_kg, 2)} kg < 57,5 kg (25th percentile).\n"
        f"2. Therefore, his weight lies {correct_ans}."
    )
    t1 = "Compare 55,45 kg with the numbers in the table row for 16-year-olds."
    t2 = "55,45 kg is between 52,0 kg (10th) and 57,5 kg (25th)."
    t3 = f"Bracket = {correct_ans}."

    custom_opts = [
        correct_ans,
        "Between the 25th and 50th percentile",
        "Between the 5th and 10th percentile",
        "Above the 75th percentile",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_19",
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
    )


def gen_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Subskill 20: Reading Weight-for-age percentile for girls."""
    age = 12
    weight_kg = 46.0

    table_data = {
        "headers": ["Age (Years)", "5th Percentile", "25th Percentile", "50th Percentile (Median)", "75th Percentile", "95th Percentile"],
        "rows": [
            ["12 years", "28,5 kg", "36,0 kg", "42,5 kg", "50,0 kg", "63,0 kg"],
        ]
    }

    prompt = (
        f"Nontando is 12 years old and weighs {_fmt(weight_kg)} kg.\n\n"
        f"Refer to the Weight-for-Age Table for 12-Year-Old Girls below.\n"
        f"Between which two percentile curves does Nontando's weight fall?"
    )

    correct_ans = "Between the 50th and 75th percentile"
    explanation = (
        f"1. 42,5 kg (50th percentile) < {_fmt(weight_kg)} kg < 50,0 kg (75th percentile).\n"
        f"2. Nontando's weight lies {correct_ans}."
    )
    t1 = "Look at the numbers for 50th and 75th percentiles in the 12-year row."
    t2 = "46 kg is between 42,5 kg and 50,0 kg."
    t3 = f"Position = {correct_ans}."

    custom_opts = [
        correct_ans,
        "Between the 25th and 50th percentile",
        "Between the 75th and 95th percentile",
        "Below the 5th percentile",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_20",
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
    )


def gen_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Statistical percentile interpretation: explaining what '75th percentile' means."""
    prompt = (
        f"A doctor tells a mother that her 14-year-old son's height is on the 75th percentile.\n\n"
        f"Which of the following statements provides the scientifically accurate interpretation of this percentile value?"
    )

    correct_ans = "He is taller than 75% of boys his own age (and shorter than 25%)"
    explanation = (
        f"1. A percentile indicates the percentage of a reference population that scores below that value.\n"
        f"2. Being on the 75th percentile for height means that 75% of peer boys are shorter, and only 25% are taller."
    )
    t1 = "Recall the definition of a percentile: the percentage of individuals below a given mark."
    t2 = "75th percentile means taller than 75% of peers."
    t3 = f"Meaning: {correct_ans}."

    custom_opts = [
        correct_ans,
        "He has reached 75% of his adult final height",
        "He is 75 cm taller than the average boy in his class",
        "He scored 75% on his medical growth examination",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_21",
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


def gen_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Subskill 22: Median benchmark: explaining the significance of the 50th percentile curve."""
    prompt = (
        f"On all South African Road to Health and WHO growth charts, the central bold curve is "
        f"marked as the '50th percentile'.\n\n"
        f"What statistical measure of central tendency does the 50th percentile represent?"
    )

    correct_ans = "The Median (the exact middle value where 50% are above and 50% are below)"
    explanation = (
        f"1. The 50th percentile divides any ranked population exactly in half.\n"
        f"2. In statistics, the middle value is the Median."
    )
    t1 = "The 50th percentile splits data exactly into two equal halves."
    t2 = "The middle value is the median."
    t3 = f"Statistical concept: {correct_ans}."

    custom_opts = [
        correct_ans,
        "The Mode (the most frequently observed measurement)",
        "The Range (the difference between the tallest and shortest child)",
        "The Maximum possible healthy height",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_22",
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


def gen_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Subskill 23: Identifying stunted growth (height below 3rd/5th percentile)."""
    prompt = (
        f"A public health clinic in rural Eastern Cape assesses an 8-year-old child whose height "
        f"consistently tracks below the 3rd percentile for his age, despite balanced proportions.\n\n"
        f"In nutritional and pediatric terminology, chronic linear growth failure resulting in a "
        f"height far below normal age expectations is called:"
    )

    correct_ans = "Stunting (chronic undernutrition or long-term growth retardation)"
    explanation = (
        f"1. Height-for-age below the 3rd or 5th percentile is the clinical definition of stunting.\n"
        f"2. Stunting reflects long-term, chronic nutritional deficiency or recurrent childhood illness."
    )
    t1 = "Recall the medical term for chronic low height-for-age."
    t2 = "Low height-for-age over time is called stunting."
    t3 = f"Condition: {correct_ans}."

    custom_opts = [
        correct_ans,
        "Wasting (acute rapid weight loss)",
        "Obesity (excessive body fat)",
        "Normal pubertal growth spurt",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_23",
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


def gen_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Subskill 24: Identifying acute wasting (weight below 3rd/5th percentile with normal height)."""
    prompt = (
        f"A 5-year-old child who recently suffered from severe gastrointestinal illness has normal "
        f"height (50th percentile), but his weight has dropped sharply below the 3rd percentile.\n\n"
        f"In pediatric anthropometry, acute severe weight loss resulting in a low weight-for-height "
        f"is specifically identified as:"
    )

    correct_ans = "Wasting (acute malnutrition or rapid severe weight loss)"
    explanation = (
        f"1. When weight falls below the 3rd percentile while height remains normal, the child has lost muscle and fat mass.\n"
        f"2. This condition of acute nutritional deficit is termed wasting."
    )
    t1 = "Acute weight drop while height remains normal is called wasting."
    t2 = "Wasting reflects acute severe weight deficit."
    t3 = f"Term: {correct_ans}."

    custom_opts = [
        correct_ans,
        "Stunting (long-term deficit in linear height)",
        "Overweight",
        "Normal metabolic plateau",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_24",
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
