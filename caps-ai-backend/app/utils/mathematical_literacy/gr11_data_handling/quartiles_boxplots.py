"""Subskills 28 to 36: Quartiles, Five-Number Summary, Box-and-Whisker Plots & Percentiles for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Subskill 28: Lower Quartile (Q1 / 25th percentile) calculation from ordered data."""
    # Data with n=11 for clean integer positions: Q1 is at position 3, Median at 6, Q3 at 9
    vals = sorted([r.randint(20, 90) for _ in range(11)])
    q1 = vals[2]  # 3rd item

    prompt = (
        f"A set of 11 learner test marks arranged in ascending order is given as:\n"
        f"**{', '.join(str(v) for v in vals)}**\n"
        f"Determine the Lower Quartile (Q₁) for this data set."
    )

    correct_ans = f"{q1}"
    wrong_1 = f"{vals[1]}"
    wrong_2 = f"{vals[5]}"  # median
    wrong_3 = f"{vals[8]}"  # Q3
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify the median position [1 mark].\n"
        f"For n = 11, the median Q₂ is at position (11 + 1) ÷ 2 = 6th value ({vals[5]}).\n"
        f"Step 2: Find the lower quartile (median of the lower half) [1 mark].\n"
        f"The lower half consists of the first 5 values: {', '.join(str(v) for v in vals[:5])}.\n"
        f"The median of these 5 values is the 3rd value: {q1}.\n"
        f"Step 3: Stated Q₁ [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="28",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The lower quartile Q₁ is the median of the lower half of the data.",
        tier_2=f"The lower half is the first 5 numbers: {vals[:5]}. The middle of these is {q1}.",
        tier_3=f"Q₁ = {q1}.",
        r=r,
    )


def generate_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Subskill 29: Upper Quartile (Q3 / 75th percentile) calculation from ordered data."""
    vals = sorted([r.randint(25, 95) for _ in range(11)])
    q3 = vals[8]  # 9th item

    prompt = (
        f"A set of 11 employee weekly overtime hours arranged in ascending order is:\n"
        f"**{', '.join(str(v) for v in vals)}**\n"
        f"Determine the Upper Quartile (Q₃) for this data set."
    )

    correct_ans = f"{q3}"
    wrong_1 = f"{vals[7]}"
    wrong_2 = f"{vals[5]}"  # median
    wrong_3 = f"{vals[2]}"  # Q1
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify median position [1 mark].\n"
        f"Median Q₂ is the 6th value ({vals[5]}).\n"
        f"Step 2: Find upper quartile (median of the upper half) [1 mark].\n"
        f"The upper half consists of the last 5 values: {', '.join(str(v) for v in vals[6:])}.\n"
        f"The median of these 5 values is the middle value ({q3}).\n"
        f"Step 3: Stated Q₃ [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="29",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The upper quartile Q₃ is the median of the upper half of the ordered data.",
        tier_2=f"Look at the upper 5 values: {vals[6:]}. The middle value is {q3}.",
        tier_3=f"Q₃ = {q3}.",
        r=r,
    )


def generate_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Subskill 30: Five-number summary compilation: Min, Q1, Q2, Q3, Max."""
    name = r.choice(SA_NAMES)
    vals = sorted([r.randint(10, 90) for _ in range(11)])
    min_v = vals[0]
    q1_v = vals[2]
    med_v = vals[5]
    q3_v = vals[8]
    max_v = vals[10]

    prompt = (
        f"{name} records test percentages for 11 learners:\n"
        f"**{', '.join(str(v) for v in vals)}**\n"
        f"Which of the following correctly represents the complete Five-Number Summary (Min; Q₁; Median; Q₃; Max) for this data?"
    )

    correct_ans = f"Min = {min_v}; Q₁ = {q1_v}; Median = {med_v}; Q₃ = {q3_v}; Max = {max_v}"
    wrong_1 = f"Min = {min_v}; Q₁ = {vals[1]}; Median = {med_v}; Q₃ = {vals[7]}; Max = {max_v}"
    wrong_2 = f"Min = {min_v}; Q₁ = {q1_v}; Median = {round(sum(vals)/11, 1)}; Q₃ = {q3_v}; Max = {max_v}"
    wrong_3 = f"Min = {min_v}; Q₁ = {vals[3]}; Median = {med_v}; Q₃ = {vals[9]}; Max = {max_v}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify Minimum and Maximum [1 mark].\n"
        f"Min = {min_v}, Max = {max_v}.\n"
        f"Step 2: Find Q₁, Q₂, Q₃ [1 mark].\n"
        f"Median Q₂ (6th value) = {med_v}; Lower Quartile Q₁ (3rd value) = {q1_v}; Upper Quartile Q₃ (9th value) = {q3_v}.\n"
        f"Step 3: Stated five-number summary [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="30",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The Five-Number Summary consists of: Minimum, Lower Quartile (Q₁), Median (Q₂), Upper Quartile (Q₃), and Maximum.",
        tier_2=f"Min = {min_v}, Q₁ = {q1_v}, Med = {med_v}, Q₃ = {q3_v}, Max = {max_v}.",
        tier_3=f"Summary: {correct_ans}.",
        r=r,
    )


def generate_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Subskill 31: Interquartile Range (IQR = Q3 - Q1) calculation."""
    q1 = r.choice([35, 40, 45, 50])
    iqr_val = r.choice([15, 20, 25, 30])
    q3 = q1 + iqr_val

    prompt = (
        f"In a statistical study of daily electricity consumption (kWh), the Lower Quartile is "
        f"Q₁ = {_fmt(q1)} kWh and the Upper Quartile is Q₃ = {_fmt(q3)} kWh.\n"
        f"Calculate the Interquartile Range (IQR) of this data set."
    )

    correct_ans = f"{_fmt(iqr_val)} kWh"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: State the IQR formula [1 mark].\n"
        f"\\text{{IQR}} = Q_3 - Q_1.\n"
        f"Step 2: Substitute values [1 mark].\n"
        f"\\text{{IQR}} = {_fmt(q3)} - {_fmt(q1)} = {_fmt(iqr_val)} kWh.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="31",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Interquartile Range IQR = Q₃ - Q₁.",
        tier_2=f"Subtract Q₁ ({q1}) from Q₃ ({q3}).",
        tier_3=f"IQR = {q3} - {q1} = {iqr_val} kWh.",
        r=r,
    )


def generate_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Subskill 32: Semi-interquartile range calculation: (Q3 - Q1) / 2."""
    q1 = r.choice([24, 30, 36, 42])
    iqr = r.choice([16, 20, 24, 28])
    q3 = q1 + iqr
    semi_iqr = round(iqr / 2, 1)

    prompt = (
        f"A data set of petrol prices at various fuel stations has an Upper Quartile of Q₃ = R {_fmt(q3 / 2, 2)} "
        f"and a Lower Quartile of Q₁ = R {_fmt(q1 / 2, 2)} (giving an IQR of R {_fmt(iqr / 2, 2)}).\n"
        f"Calculate the semi-interquartile range for this data set."
    )

    semi_curr = round(iqr / 4, 2)
    correct_ans = _fmt_curr(semi_curr)
    wrong_1 = _fmt_curr(semi_curr * 2)  # full IQR
    wrong_2 = _fmt_curr(semi_curr * 4)
    wrong_3 = _fmt_curr(semi_curr * 0.5)
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State the semi-interquartile range formula [1 mark].\n"
        f"\\text{{Semi-IQR}} = \\frac{{Q_3 - Q_1}}{{2}} = \\frac{{\\text{{IQR}}}}{{2}}.\n"
        f"Step 2: Divide IQR by 2 [1 mark].\n"
        f"Semi-IQR = {_fmt_curr(iqr / 2)} ÷ 2 = {_fmt_curr(semi_curr)}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="32",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Semi-interquartile range is simply half of the Interquartile Range: IQR ÷ 2.",
        tier_2=f"Divide {_fmt_curr(iqr / 2)} by 2.",
        tier_3=f"Result: {_fmt_curr(semi_curr)}.",
        r=r,
    )


def generate_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Subskill 33: Read quartiles and median directly from a Box-and-Whisker plot with diagram_spec."""
    name = r.choice(SA_NAMES)
    min_v = r.choice([20, 25])
    q1_v = r.choice([35, 40])
    med_v = r.choice([55, 60])
    q3_v = r.choice([75, 80])
    max_v = r.choice([90, 95])

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "box_and_whisker",
        "title": f"Distribution of Mathematics Test Marks for {name}'s Class",
        "summary": {
            "min": min_v,
            "q1": q1_v,
            "median": med_v,
            "q3": q3_v,
            "max": max_v,
        },
        "unit": "%",
    }

    prompt = (
        f"Refer to the accompanying Box-and-Whisker plot showing learner test performance.\n"
        f"What is the Median mark and the Interquartile Range (IQR) represented by this plot?"
    )

    iqr = q3_v - q1_v
    correct_ans = f"Median = {med_v}%; IQR = {iqr}%"
    wrong_1 = f"Median = {med_v}%; IQR = {max_v - min_v}%"  # full range
    wrong_2 = f"Median = {q1_v}%; IQR = {iqr}%"
    wrong_3 = f"Median = {q3_v}%; IQR = {iqr}%"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Read the median from the vertical line inside the box [1 mark].\n"
        f"The line inside the central box is located at {med_v}%.\n"
        f"Step 2: Calculate IQR from the box edges [1 mark].\n"
        f"Q₁ (left box edge) = {q1_v}%; Q₃ (right box edge) = {q3_v}%.\n"
        f"IQR = Q₃ - Q₁ = {q3_v}% - {q1_v}% = {iqr}%.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="33",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Median is the line inside the box; IQR is the length of the box (Q₃ - Q₁).",
        tier_2=f"Median line = {med_v}%. Box runs from Q₁ = {q1_v}% to Q₃ = {q3_v}%.",
        tier_3=f"Median = {med_v}%, IQR = {iqr}%.",
        r=r,
        diagram_spec=diagram_spec,
    )


def generate_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Subskill 34: Identify distribution skewness from box-and-whisker plot."""
    skew_type = r.choice(["Positively Skewed (Skewed to the Right)", "Negatively Skewed (Skewed to the Left)", "Symmetrical"])

    if skew_type == "Positively Skewed (Skewed to the Right)":
        box_desc = "The right whisker is substantially longer than the left whisker, and the median line is closer to Q1"
    elif skew_type == "Negatively Skewed (Skewed to the Left)":
        box_desc = "The left whisker is substantially longer than the right whisker, and the median line is closer to Q3"
    else:
        box_desc = "The whiskers are of equal length and the median line sits centrally inside the box"

    prompt = (
        f"In a box-and-whisker plot of monthly salaries, {box_desc.lower()}.\n"
        f"How is the shape of this salary distribution classified?"
    )

    correct_ans = skew_type
    custom_opts = [
        "Positively Skewed (Skewed to the Right)",
        "Negatively Skewed (Skewed to the Left)",
        "Symmetrical",
        "Bimodal Uniform",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Analyze the whisker lengths and median position [1 mark].\n"
        f"{box_desc}.\n"
        f"Step 2: Connect to distribution tail [1 mark].\n"
        f"The side with the longer whisker represents the stretched tail of the distribution.\n"
        f"Step 3: Conclude shape [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="34",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Data is skewed in the direction of the longer tail (whisker).",
        tier_2=f"A longer right whisker means skewed to the right (positive); a longer left whisker means skewed to the left (negative).",
        tier_3=f"Classification: {skew_type}.",
        r=r,
    )


def generate_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Subskill 35: Compare two data sets using side-by-side box-and-whisker plots."""
    # School A: Median 65%, IQR 15% (more consistent, higher median)
    # School B: Median 52%, IQR 30% (more spread out, lower median)
    prompt = (
        f"Two parallel box-and-whisker plots compare the matric Mathematics trial exam results of School A and School B:\n"
        f"• School A: Median = 65%, IQR = 15%, Range = 35%\n"
        f"• School B: Median = 52%, IQR = 30%, Range = 60%\n"
        f"Which statement correctly compares the performance and consistency of the two schools?"
    )

    correct_ans = (
        "School A performed better overall (higher median of 65%) and was more consistent (smaller IQR of 15%) than School B"
    )
    wrong_1 = "School B performed better overall because it had a much wider range of scores"
    wrong_2 = "Both schools had identical performance because their student populations were the same"
    wrong_3 = "School B was more consistent because its IQR was twice as large as School A"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Compare measures of central performance [1 mark].\n"
        f"School A median (65%) > School B median (52%), indicating higher overall marks.\n"
        f"Step 2: Compare measures of dispersion / consistency [1 mark].\n"
        f"A smaller IQR indicates less variation (greater consistency). School A's IQR (15%) is lower than School B's (30%).\n"
        f"Step 3: Conclude comparative evaluation [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="35",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Higher median indicates better performance; smaller IQR indicates greater consistency.",
        tier_2="School A has a higher median (65% vs 52%) and a smaller IQR (15% vs 30%).",
        tier_3=f"Conclusion: {correct_ans}.",
        r=r,
    )


def generate_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Subskill 36: Interpret percentiles on Road to Health growth charts."""
    name = r.choice(SA_NAMES)
    age_months = r.choice([6, 12, 18, 24])

    prompt = (
        f"On a South African Department of Health 'Road to Health' child growth chart, a 12-month-old infant's "
        f"weight plots exactly on the 50th percentile curve.\n"
        f"What is the clinical and statistical interpretation of this finding?"
    )

    correct_ans = (
        "The infant's weight is at the exact median: 50% of healthy infants of the same age weigh less and 50% weigh more"
    )
    wrong_1 = "The infant is severely malnourished and weighs half of what a normal baby should weigh"
    wrong_2 = "The infant weighs more than 95% of all babies in South Africa"
    wrong_3 = "The infant has only a 50% chance of reaching adulthood"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand statistical percentiles [1 mark].\n"
        f"The p-th percentile is the value below which p percent of the observations fall.\n"
        f"Step 2: Relate 50th percentile to the median [1 mark].\n"
        f"The 50th percentile is the exact median of the reference population.\n"
        f"Step 3: Stated clinical meaning [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="36",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The 50th percentile is the median value.",
        tier_2="Being on the 50th percentile means 50% of healthy babies weigh less and 50% weigh more.",
        tier_3=f"Interpretation: {correct_ans}.",
        r=r,
    )
