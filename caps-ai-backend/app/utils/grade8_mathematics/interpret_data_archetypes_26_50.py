"""
Grade 8 Mathematics - Interpret, Analyse and Report on Data Archetypes (26 to 50).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/01. Interpret analyse and report on data.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from app.utils.grade8_mathematics.svg_diagrams import (
    draw_bar_chart_svg,
    draw_histogram_svg,
    draw_pie_chart_svg,
    draw_real_world_line_graph_svg,
)


def _fmt_sa(val: float, places: int = 1) -> str:
    s = f"{val:.{places}f}".rstrip("0").rstrip(".") if places > 1 else f"{val:.{places}f}"
    if s == "-0":
        s = "0"
    return s.replace(".", ",")


def arch_26_misleading_graph_truncated_vertical_axis(rng: random.Random) -> Dict[str, Any]:
    seed = rng.randint(1, 1000000)
    cats = ["Product A", "Product B"]
    base = rng.randint(92, 98)
    diff = rng.randint(2, 5)
    vals = [float(base), float(base + diff)]
    svg = draw_bar_chart_svg(
        categories=cats,
        values=vals,
        title="Customer Satisfaction Rating (%)",
        y_label="Satisfaction (%)",
        width=420,
        height=240,
        seed=seed,
    )

    return {
        "title": "Critiquing Misleading Graphs: Truncated Vertical Axis",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "26_misleading_graph_truncated_vertical_axis",
        "difficulty": "medium",
        "question_text": (
            "An advertising company displays satisfaction ratings for two competing products:\n\n"
            f"- {cats[0]}: **{vals[0]:.0f}%**\n"
            f"- {cats[1]}: **{vals[1]:.0f}%**\n\n"
            "If the visual display begins its vertical scale at 90% instead of 0%, "
            "explain why the display is visually misleading to consumers."
        ),
        "correct_answer": "Starting the vertical scale at 90% instead of 0 exaggerates the visual difference, making Product B look multiple times taller even though the difference is only a few percentage points.",
        "marking_schema": [
            "Mention baseline not starting at 0 / truncated vertical scale [1 mark]",
            "Explain that small difference appears exaggerated / disproportionate [1 mark]",
        ],
        "hints": [
            "Check where the vertical axis starts.",
            "When the vertical axis does not start at 0, bars are not proportional to their actual values.",
            "The small difference is exaggerated visually.",
        ],
        "misconception_tags": ["truncated_axis_misinterpretation"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_27_misleading_pictograph_area_volume_distortion(rng: random.Random) -> Dict[str, Any]:
    ratio = rng.choice([2, 3])
    area_mult = ratio ** 2
    return {
        "title": "Critiquing Misleading Displays: Dimensional Scaling Distortion",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "27_misleading_pictograph_area_volume_distortion",
        "difficulty": "medium",
        "question_text": (
            f"A company's sales doubled (increased by a factor of {ratio}) over a 5-year period. "
            f"In a marketing presentation, the graphic designer doubled both the **width** and the **height** "
            "of a money-bag symbol to represent the new sales figure.\n\n"
            f"By what factor did the **surface area** of the symbol actually increase? "
            "Explain why this creates a misleading visual impression."
        ),
        "correct_answer": f"The area increases by a factor of {area_mult} ({ratio} x {ratio} = {area_mult}). This misleads the viewer because the eye perceives the area, making the increase look {area_mult} times larger instead of only {ratio} times larger.",
        "marking_schema": [
            f"Area increases by factor of {area_mult} [1 mark]",
            f"Viewer perceives 2D area, exaggerating growth [1 mark]",
        ],
        "hints": [
            f"Area = width x height. If both are multiplied by {ratio}, area is multiplied by {ratio} squared.",
            f"Calculate {ratio}^2 = {area_mult}.",
            "The eye judges visual area, so doubling dimensions quadruples the area.",
        ],
        "misconception_tags": ["pictograph_scaling_dimension_error"],
        "diagram_spec": None,
    }


def arch_28_misleading_graph_irregular_time_intervals(rng: random.Random) -> Dict[str, Any]:
    years = [2018, 2019, 2020, 2025]
    return {
        "title": "Critiquing Misleading Graphs: Irregular Time Intervals",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "28_misleading_graph_irregular_time_intervals",
        "difficulty": "medium",
        "question_text": (
            "A town records municipal water consumption across four recorded years: "
            f"**{years[0]}**, **{years[1]}**, **{years[2]}**, and **{years[3]}**.\n\n"
            "If a line chart plots these four points at equal horizontal distances along the time axis, "
            "explain why this representation misrepresents the actual rate of change."
        ),
        "correct_answer": f"The gap between 2020 and 2025 is 5 years, whereas the earlier gaps are only 1 year. Plotting them with equal spacing compresses the 5-year gap and makes a gradual 5-year change appear 5 times steeper than it actually was.",
        "marking_schema": [
            "Identify uneven time gap (1 year vs 5 years) [1 mark]",
            "Explain that slope/rate of change is falsely steepened or compressed [1 mark]",
        ],
        "hints": [
            "Look at the differences between consecutive years: 1 year, 1 year, then 5 years.",
            "Equal horizontal spacing assumes equal time intervals.",
            "The 5-year jump is compressed into a 1-year width.",
        ],
        "misconception_tags": ["irregular_scale_misinterpretation"],
        "diagram_spec": None,
    }


def arch_29_interpreting_line_graph_trend(rng: random.Random) -> Dict[str, Any]:
    seed = rng.randint(1, 1000000)
    m1 = rng.randint(30, 45)
    m2 = m1 + rng.randint(15, 25)
    m3 = m2 + rng.randint(10, 20)
    m4 = m3 - rng.randint(20, 30)
    pts = [
        (1.0, float(m1), "Jan"),
        (2.0, float(m2), "Feb"),
        (3.0, float(m3), "Mar"),
        (4.0, float(m4), "Apr"),
    ]
    svg = draw_real_world_line_graph_svg(
        waypoints=pts,
        x_label="Month (1=Jan, 2=Feb, 3=Mar, 4=Apr)",
        y_label="Dam Level (%)",
        max_x=5.0,
        max_y=100.0,
        title="Municipal Dam Capacity (%)",
        width=420,
        height=260,
        seed=seed,
    )

    diff = m3 - m1
    return {
        "title": "Interpreting Trends in a Line Graph",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "29_interpreting_line_graph_trend",
        "difficulty": "easy",
        "question_text": (
            "A municipal dam records the following capacity percentages over four consecutive months:\n\n"
            f"- January: **{m1}%**\n"
            f"- February: **{m2}%**\n"
            f"- March: **{m3}%**\n"
            f"- April: **{m4}%**\n\n"
            "1. Describe the overall trend in dam capacity from January to March.\n"
            f"2. Calculate the total percentage point increase from January to March."
        ),
        "correct_answer": f"1. The capacity increased steadily. 2. {diff} percentage points ({m3} - {m1} = {diff}%).",
        "marking_schema": [
            "Trend identified as increasing [1 mark]",
            f"Calculated difference: {m3} - {m1} = {diff}% [1 mark]",
        ],
        "hints": [
            "Compare the values from January to March: do they rise or fall?",
            f"Subtract the January level ({m1}%) from the March level ({m3}%).",
            f"Difference = {m3} - {m1} = {diff}%.",
        ],
        "misconception_tags": ["trend_direction_confusion"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_30_predicting_future_value_by_linear_extrapolation(rng: random.Random) -> Dict[str, Any]:
    base_year = rng.randint(2020, 2022)
    start_val = rng.randint(320, 480)
    rate = rng.randint(15, 35)

    y1, v1 = base_year, start_val
    y2, v2 = base_year + 1, start_val + rate
    y3, v3 = base_year + 2, start_val + 2 * rate
    target_year = base_year + 3
    expected_v = start_val + 3 * rate

    return {
        "title": "Predicting Future Values via Linear Extrapolation",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "30_predicting_future_value_by_linear_extrapolation",
        "difficulty": "medium",
        "question_text": (
            "A secondary school tracks its Grade 8 learner enrolment over three consecutive years:\n\n"
            f"| Year | Grade 8 Enrolment |\n"
            f"| :--- | :--- |\n"
            f"| {y1} | {v1} |\n"
            f"| {y2} | {v2} |\n"
            f"| {y3} | {v3} |\n\n"
            f"Assuming the enrolment continues to increase at this constant rate, "
            f"predict the expected Grade 8 enrolment for **{target_year}**."
        ),
        "correct_answer": str(expected_v),
        "marking_schema": [
            f"Find common annual difference: {rate} learners/year [1 mark]",
            f"Add rate to {y3} figure: {v3} + {rate} = {expected_v} [1 mark]",
        ],
        "hints": [
            f"Find the constant annual increase: {v2} - {v1} = {rate}.",
            f"Add {rate} to the {y3} enrolment ({v3}).",
            f"{v3} + {rate} = {expected_v}.",
        ],
        "misconception_tags": ["linear_extrapolation_step_error"],
        "diagram_spec": None,
    }


def arch_31_interpolating_value_from_data_table(rng: random.Random) -> Dict[str, Any]:
    d1 = 10
    d2 = 20
    d3 = 30
    t1 = rng.randint(26, 30)
    drop = rng.randint(3, 5)
    t2 = t1 - drop
    t3 = t2 - drop
    target_d = 15
    interp_t = t1 - (drop / 2.0)

    return {
        "title": "Interpolating Values from an Empirical Data Table",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "31_interpolating_value_from_data_table",
        "difficulty": "medium",
        "question_text": (
            "Marine researchers record water temperature at varying depths in a coastal bay:\n\n"
            f"| Depth (m) | Water Temperature (°C) |\n"
            f"| :--- | :--- |\n"
            f"| {d1} | {t1} |\n"
            f"| {d2} | {t2} |\n"
            f"| {d3} | {t3} |\n\n"
            f"Estimate the water temperature at a depth of **{target_d} m**, "
            "assuming a constant linear change between 10 m and 20 m."
        ),
        "correct_answer": f"{_fmt_sa(interp_t, 1)} °C",
        "marking_schema": [
            f"Identify midpoint depth between {d1} m and {d2} m [1 mark]",
            f"Calculate midpoint temperature: ({t1} + {t2}) / 2 = {_fmt_sa(interp_t, 1)} °C [1 mark]",
        ],
        "hints": [
            f"Notice that {target_d} m is halfway between {d1} m and {d2} m.",
            f"Calculate the average of {t1} and {t2}.",
            f"({t1} + {t2}) / 2 = {_fmt_sa(interp_t, 1)}.",
        ],
        "misconception_tags": ["interpolation_midpoint_error"],
        "diagram_spec": None,
    }


def arch_32_two_way_contingency_table_gender_by_grade(rng: random.Random) -> Dict[str, Any]:
    b8 = rng.randint(65, 85)
    g8 = rng.randint(65, 85)
    b9 = rng.randint(60, 80)
    g9 = rng.randint(60, 80)
    tot8 = b8 + g8
    tot9 = b9 + g9
    tot_boys = b8 + b9
    tot_girls = g8 + g9
    grand_tot = tot8 + tot9

    return {
        "title": "Analysing a Two-Way Contingency Table",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "32_two_way_contingency_table_gender_by_grade",
        "difficulty": "medium",
        "question_text": (
            "The following contingency table records learner enrolments in Grade 8 and Grade 9:\n\n"
            f"| Grade | Boys | Girls | Total |\n"
            f"| :--- | :--- | :--- | :--- |\n"
            f"| Grade 8 | {b8} | {g8} | {tot8} |\n"
            f"| Grade 9 | {b9} | {g9} | {tot9} |\n"
            f"| **Total** | **{tot_boys}** | **{tot_girls}** | **{grand_tot}** |\n\n"
            "1. What is the total number of girls across both grades?\n"
            "2. What fraction of Grade 8 learners are boys? (Write in simplest fractional form)."
        ),
        "correct_answer": f"1. {tot_girls} girls. 2. {b8}/{tot8}.",
        "marking_schema": [
            f"Correct column sum for girls: {tot_girls} [1 mark]",
            f"Fraction of Grade 8 boys: {b8}/{tot8} [1 mark]",
        ],
        "hints": [
            f"For girls, add {g8} + {g9} = {tot_girls}.",
            f"For Grade 8 boys, divide Grade 8 boys ({b8}) by total Grade 8 learners ({tot8}).",
            f"Fraction = {b8}/{tot8}.",
        ],
        "misconception_tags": ["contingency_row_column_confusion"],
        "diagram_spec": None,
    }


def arch_33_calculating_percentage_proportion_from_subgroup(rng: random.Random) -> Dict[str, Any]:
    boys = rng.randint(18, 30)
    girls = rng.randint(20, 32)
    tot = boys + girls
    pct_girls = (girls / tot) * 100

    return {
        "title": "Calculating Percentage Proportion from Subgroups",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "33_calculating_percentage_proportion_from_subgroup",
        "difficulty": "easy",
        "question_text": (
            f"A school robotics society consists of **{boys} boys** and **{girls} girls**.\n\n"
            "Calculate the percentage of members in the society who are girls. "
            "Round your final answer to one decimal place."
        ),
        "correct_answer": f"{_fmt_sa(pct_girls, 1)}%",
        "marking_schema": [
            f"Total members: {boys} + {girls} = {tot} [1 mark]",
            f"Percentage: ({girls}/{tot}) x 100 = {_fmt_sa(pct_girls, 1)}% [1 mark]",
        ],
        "hints": [
            f"First find total members: {boys} + {girls} = {tot}.",
            f"Divide the number of girls ({girls}) by {tot} and multiply by 100.",
            f"({girls}/{tot}) x 100 = {_fmt_sa(pct_girls, 1)}%.",
        ],
        "misconception_tags": ["percentage_denominator_error"],
        "diagram_spec": None,
    }


def arch_34_identifying_modal_class_interval_from_histogram(rng: random.Random) -> Dict[str, Any]:
    intervals = ["0–9", "10–19", "20–29", "30–39", "40–49"]
    freqs = [rng.randint(4, 9), rng.randint(12, 18), rng.randint(24, 32), rng.randint(14, 20), rng.randint(5, 10)]
    max_idx = freqs.index(max(freqs))
    modal_int = intervals[max_idx]

    seed = rng.randint(1, 1000000)
    svg = draw_histogram_svg(
        intervals=intervals,
        frequencies=[float(f) for f in freqs],
        title="Distribution of Test Scores",
        x_label="Score Interval",
        y_label="Number of Learners",
        width=420,
        height=240,
        seed=seed,
    )

    rows = "\n".join(f"| {intervals[i]} | {freqs[i]} |" for i in range(len(intervals)))

    return {
        "title": "Identifying Modal Class Interval",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "34_identifying_modal_class_interval_from_histogram",
        "difficulty": "easy",
        "question_text": (
            "A mathematics test distribution for 80 learners is grouped into class intervals:\n\n"
            f"| Score Interval | Frequency |\n"
            f"| :--- | :--- |\n"
            f"{rows}\n\n"
            "Identify the **modal class interval** and state its frequency."
        ),
        "correct_answer": f"Modal interval: {modal_int} (frequency = {freqs[max_idx]}).",
        "marking_schema": [
            f"Identify highest frequency interval: {modal_int} [1 mark]",
            f"State frequency: {freqs[max_idx]} [1 mark]",
        ],
        "hints": [
            "The modal interval is the interval with the highest frequency.",
            f"Find the largest number in the frequency column: {freqs[max_idx]}.",
            f"The matching interval is {modal_int}.",
        ],
        "misconception_tags": ["modal_class_interval_confusion"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_35_estimating_mean_from_grouped_frequency_table(rng: random.Random) -> Dict[str, Any]:
    mids = [5, 15, 25]
    freqs = [rng.randint(4, 8), rng.randint(10, 16), rng.randint(4, 8)]
    fx = [mids[i] * freqs[i] for i in range(3)]
    sum_f = sum(freqs)
    sum_fx = sum(fx)
    est_mean = sum_fx / sum_f

    return {
        "title": "Estimating Mean from Grouped Frequency Distribution",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "35_estimating_mean_from_grouped_frequency_table",
        "difficulty": "hard",
        "question_text": (
            "A group of learners recorded time spent reading per day:\n\n"
            f"| Time Interval (mins) | Midpoint ($m$) | Frequency ($f$) | Product ($f \\times m$) |\n"
            f"| :--- | :--- | :--- | :--- |\n"
            f"| 0–10 | {mids[0]} | {freqs[0]} | {fx[0]} |\n"
            f"| 10–20 | {mids[1]} | {freqs[1]} | {fx[1]} |\n"
            f"| 20–30 | {mids[2]} | {freqs[2]} | {fx[2]} |\n\n"
            f"Calculate the **estimated mean** reading time. Round your answer to one decimal place."
        ),
        "correct_answer": f"{_fmt_sa(est_mean, 1)} minutes",
        "marking_schema": [
            f"Sum of frequencies: {sum_f} and sum of products: {sum_fx} [1 mark]",
            f"Mean calculation: {sum_fx} / {sum_f} = {_fmt_sa(est_mean, 1)} mins [1 mark]",
        ],
        "hints": [
            f"Sum the total frequencies: {freqs[0]} + {freqs[1]} + {freqs[2]} = {sum_f}.",
            f"Sum the products ($f \\times m$): {fx[0]} + {fx[1]} + {fx[2]} = {sum_fx}.",
            f"Estimated mean = {sum_fx} / {sum_f} = {_fmt_sa(est_mean, 1)}.",
        ],
        "misconception_tags": ["grouped_mean_midpoint_calculation_error"],
        "diagram_spec": None,
    }


def arch_36_distinguishing_correlation_from_causation(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Distinguishing Correlation from Causation",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "36_distinguishing_correlation_from_causation",
        "difficulty": "medium",
        "question_text": (
            "A Durban beachfront study finds a very strong positive correlation between "
            "**ice cream sales** and the **number of drowning incidents** in summer.\n\n"
            "Does buying ice cream cause drowning? "
            "Explain the true underlying factor (lurking/confounding variable) responsible for this association."
        ),
        "correct_answer": "No, correlation does not imply causation. The confounding variable is hot summer weather: higher temperatures lead both to more people buying ice cream and more people swimming in the ocean, which increases the opportunity for drowning.",
        "marking_schema": [
            "State clearly that correlation does not mean causation [1 mark]",
            "Identify hot weather/summer as the confounding factor affecting both [1 mark]",
        ],
        "hints": [
            "Ask yourself: would eating ice cream physically cause a swimmer to drown?",
            "What common environmental factor happens in summer that increases both ice cream sales and swimming?",
            "Hot sunny weather causes both events independently.",
        ],
        "misconception_tags": ["correlation_equals_causation_fallacy"],
        "diagram_spec": None,
    }


def arch_37_impact_of_sample_size_on_reliability(rng: random.Random) -> Dict[str, Any]:
    s1 = 10
    s2 = 500
    return {
        "title": "Evaluating Impact of Sample Size on Reliability",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "37_impact_of_sample_size_on_reliability",
        "difficulty": "medium",
        "question_text": (
            f"To determine the favourite sports of learners at a school of 1 200 pupils, "
            f"Researcher A surveys **{s1} learners**, while Researcher B surveys **{s2} learners** "
            "selected at random.\n\n"
            "State which survey will yield more reliable findings and explain why in terms of sampling variability."
        ),
        "correct_answer": f"Researcher B's survey is more reliable. A larger random sample ({s2} vs {s1}) is much more representative of the 1 200 population and reduces sampling variability and margin of error.",
        "marking_schema": [
            f"Select Researcher B ({s2} learners) [1 mark]",
            "Explain that larger sample reduces error and better represents population [1 mark]",
        ],
        "hints": [
            f"10 learners represents less than 1% of the school.",
            f"500 learners provides a much larger cross-section.",
            "Larger sample sizes reduce chance variation and yield more reliable statistics.",
        ],
        "misconception_tags": ["sample_size_reliability_gap"],
        "diagram_spec": None,
    }


def arch_38_interpreting_pie_chart_sector_budget(rng: random.Random) -> Dict[str, Any]:
    seed = rng.randint(1, 1000000)
    p_sal = 50
    p_infra = 25
    p_books = 15
    p_nutr = 10
    slices = [
        ("Salaries", float(p_sal)),
        ("Infrastructure", float(p_infra)),
        ("Learning Materials", float(p_books)),
        ("School Nutrition", float(p_nutr)),
    ]
    svg = draw_pie_chart_svg(
        slices=slices,
        title="Provincial Education Budget Allocation",
        width=340,
        height=240,
        seed=seed,
    )

    tot_million = rng.choice([200, 300, 400, 500])
    target_pct = p_infra
    amt = (target_pct / 100) * tot_million

    return {
        "title": "Interpreting Sector Allocation from a Pie Chart",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "38_interpreting_pie_chart_sector_budget",
        "difficulty": "medium",
        "question_text": (
            f"A provincial department of education allocates an annual budget of **R{tot_million} million**:\n\n"
            f"- Educator Salaries: **{p_sal}%**\n"
            f"- School Infrastructure: **{p_infra}%**\n"
            f"- Learning Materials: **{p_books}%**\n"
            f"- School Nutrition: **{p_nutr}%**\n\n"
            f"Calculate the actual amount allocated to **School Infrastructure** in millions of Rands."
        ),
        "correct_answer": f"R{amt:.0f} million",
        "marking_schema": [
            f"Calculate {target_pct}% of R{tot_million} million: ({target_pct}/100) x {tot_million} [1 mark]",
            f"Correct amount: R{amt:.0f} million [1 mark]",
        ],
        "hints": [
            f"Infrastructure receives {p_infra}% of the total.",
            f"Calculate {p_infra}% of {tot_million}.",
            f"0,{p_infra} x {tot_million} = {amt:.0f}.",
        ],
        "misconception_tags": ["percentage_to_absolute_quantity_error"],
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    }


def arch_39_choosing_median_for_household_income(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Evaluating Summary Measures for Skewed Income Data",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "39_choosing_median_for_household_income",
        "difficulty": "medium",
        "question_text": (
            "A town surveyed monthly household incomes for 100 families. "
            "Ninety-five families earn between R12 000 and R25 000 per month, "
            "while 5 corporate executives earn over R1 500 000 per month.\n\n"
            "State whether the **mean** or the **median** is the more appropriate summary measure "
            "for typical household income in this town, and provide a clear justification."
        ),
        "correct_answer": "The median. The mean is strongly inflated and distorted by the extreme high incomes of the 5 executives, whereas the median is resistant to extreme outliers and accurately reflects the typical family's income.",
        "marking_schema": [
            "Select median [1 mark]",
            "Explain that extreme outliers distort the mean while the median remains representative [1 mark]",
        ],
        "hints": [
            "Look at the extreme difference between R25 000 and R1 500 000.",
            "Adding a few very large numbers raises the mean significantly.",
            "The median is not affected by extreme values.",
        ],
        "misconception_tags": ["mean_skewness_vulnerability"],
        "diagram_spec": None,
    }


def arch_40_writing_summary_statement_from_data_table(rng: random.Random) -> Dict[str, Any]:
    t1_pass = rng.randint(62, 70)
    t2_pass = t1_pass + rng.randint(8, 15)
    diff = t2_pass - t1_pass
    return {
        "title": "Synthesising Findings into a Summary Report",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "40_writing_summary_statement_from_data_table",
        "difficulty": "medium",
        "question_text": (
            "A secondary school introduces after-school tutoring in Term 2. "
            "The percentage of learners achieving a passing mark in Mathematics was:\n\n"
            f"- Term 1 (before tutoring): **{t1_pass}%**\n"
            f"- Term 2 (after tutoring): **{t2_pass}%**\n\n"
            "Formulate a concise summary statement for the school governing body describing "
            "the observed change in pass rate and its educational implication."
        ),
        "correct_answer": f"The Mathematics pass rate improved by {diff} percentage points from {t1_pass}% to {t2_pass}% following the tutoring intervention, indicating that the after-school support program was positively associated with learner performance.",
        "marking_schema": [
            f"State pass rate increase of {diff} percentage points ({t1_pass}% to {t2_pass}%) [1 mark]",
            "Conclude that tutoring intervention was effective/positive [1 mark]",
        ],
        "hints": [
            f"Calculate the difference: {t2_pass} - {t1_pass} = {diff}%.",
            "State whether performance improved or declined.",
            "Link the improvement to the tutoring program.",
        ],
        "misconception_tags": ["data_synthesis_reporting_gap"],
        "diagram_spec": None,
    }


def arch_41_identifying_confounding_variable(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Identifying Confounding Variables in Observational Studies",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "41_identifying_confounding_variable",
        "difficulty": "medium",
        "question_text": (
            "A primary school study finds a high positive correlation between "
            "**learners' shoe sizes** and their **reading comprehension scores**.\n\n"
            "Does having bigger feet improve reading ability? "
            "Identify the confounding variable (hidden factor) that explains this correlation."
        ),
        "correct_answer": "No. The confounding variable is age (or grade level). Older children have larger shoe sizes and have also had more years of schooling, giving them better reading comprehension.",
        "marking_schema": [
            "Answer 'No' [1 mark]",
            "Identify age / maturity / grade level as the confounding variable [1 mark]",
        ],
        "hints": [
            "Think about who has larger feet: a Grade 1 child or a Grade 7 child?",
            "Who has had more reading instruction?",
            "Age explains both larger feet and better reading skills.",
        ],
        "misconception_tags": ["confounding_variable_blindness"],
        "diagram_spec": None,
    }


def arch_42_comparing_two_groups_spread_and_consistency(rng: random.Random) -> Dict[str, Any]:
    mean_score = 65
    r_a = rng.randint(8, 14)
    r_b = rng.randint(25, 38)
    return {
        "title": "Comparing Consistency Between Two Groups Using Range",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "42_comparing_two_groups_spread_and_consistency",
        "difficulty": "medium",
        "question_text": (
            "Two cricket batsmen, Player A and Player B, both have an average (mean) score of "
            f"**{mean_score} runs** across 10 matches.\n\n"
            f"- Player A's scores have a **range of {r_a} runs**.\n"
            f"- Player B's scores have a **range of {r_b} runs**.\n\n"
            "Which player is more consistent in their batting performances? Justify your answer using the data."
        ),
        "correct_answer": f"Player A is more consistent. A smaller range ({r_a} vs {r_b}) indicates that scores are clustered more closely around the mean with less variability.",
        "marking_schema": [
            "Select Player A [1 mark]",
            f"Justify that smaller range ({r_a}) indicates less spread / higher consistency [1 mark]",
        ],
        "hints": [
            "Consistency means scoring close to the same number in every match.",
            "A smaller range means less spread or variation.",
            f"Player A's range ({r_a}) is smaller than Player B's range ({r_b}).",
        ],
        "misconception_tags": ["range_spread_interpretation_error"],
        "diagram_spec": None,
    }


def arch_43_percentage_increase_vs_percentage_point_difference(rng: random.Random) -> Dict[str, Any]:
    p1 = 50
    p2 = 75
    pp_diff = p2 - p1
    rel_inc = ((p2 - p1) / p1) * 100

    return {
        "title": "Distinguishing Percentage Points from Relative Percentage Increase",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "43_percentage_increase_vs_percentage_point_difference",
        "difficulty": "hard",
        "question_text": (
            f"A school's sports participation rate increased from **{p1}%** in 2023 to **{p2}%** in 2024.\n\n"
            "1. Calculate the increase in **percentage points**.\n"
            "2. Calculate the **relative percentage increase** based on the 2023 baseline value."
        ),
        "correct_answer": f"1. {pp_diff} percentage points ({p2} - {p1} = {pp_diff}). 2. {rel_inc:.0f}% increase (({pp_diff}/{p1}) x 100 = {rel_inc:.0f}%).",
        "marking_schema": [
            f"Percentage point difference: {p2} - {p1} = {pp_diff} percentage points [1 mark]",
            f"Relative increase: ({pp_diff}/{p1}) x 100 = {rel_inc:.0f}% [1 mark]",
        ],
        "hints": [
            f"Percentage point change is simple subtraction: {p2} - {p1} = {pp_diff}.",
            f"Relative percentage increase divides the change by the original value: ({pp_diff} / {p1}) x 100.",
            f"({pp_diff} / {p1}) x 100 = {rel_inc:.0f}%.",
        ],
        "misconception_tags": ["percentage_points_vs_percent_confusion"],
        "diagram_spec": None,
    }


def arch_44_evaluating_leading_question_bias(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Evaluating Question Wording and Leading Questions",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "44_evaluating_leading_question_bias",
        "difficulty": "medium",
        "question_text": (
            "A survey question reads:\n\n"
            "> *'Don't you agree that homework causes unnecessary stress for Grade 8 learners?'*\n\n"
            "1. Explain why this question is considered a **leading (biased) question**.\n"
            "2. Rephrase the question so that it is neutral and unbiased."
        ),
        "correct_answer": "1. It prompts the respondent to agree with the researcher's opinion that homework causes stress. 2. A neutral alternative: 'To what extent do you feel homework affects your stress levels? (Not at all / Slightly / Moderately / Strongly)'.",
        "marking_schema": [
            "Explain that the wording nudges/leads respondents toward agreement [1 mark]",
            "Provide balanced, neutral alternative question [1 mark]",
        ],
        "hints": [
            "The phrase 'Don't you agree...' suggests the desired answer.",
            "An unbiased question does not state an opinion.",
            "Provide neutral options without emotional words.",
        ],
        "misconception_tags": ["leading_question_bias_blindness"],
        "diagram_spec": None,
    }


def arch_45_evaluating_sampling_exclusion_bias(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Evaluating Undercoverage and Exclusion Bias",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "45_evaluating_sampling_exclusion_bias",
        "difficulty": "medium",
        "question_text": (
            "A municipality conducts an **online internet survey** via social media to find out "
            "how satisfied residents are with drinking water delivery in rural villages.\n\n"
            "Identify the major source of bias in this survey methodology and name the group of residents "
            "who are systematically excluded from participating."
        ),
        "correct_answer": "Exclusion (undercoverage) bias. Rural residents without internet access, smartphones, or computers are excluded, yet they are the ones most likely to experience severe water service disruptions.",
        "marking_schema": [
            "Identify exclusion / undercoverage / digital divide bias [1 mark]",
            "Identify residents without internet / smartphones as the excluded group [1 mark]",
        ],
        "hints": [
            "Can every rural household access high-speed internet and social media?",
            "Who lacks digital connectivity?",
            "People without internet are excluded from the sample.",
        ],
        "misconception_tags": ["sampling_undercoverage_bias"],
        "diagram_spec": None,
    }


def arch_46_interpreting_double_bar_chart_comparison(rng: random.Random) -> Dict[str, Any]:
    seasons = ["Summer", "Autumn", "Winter", "Spring"]
    rf_ct = [25, 45, 110, 40]
    rf_db = [120, 80, 30, 95]
    diffs = [abs(rf_ct[i] - rf_db[i]) for i in range(4)]
    max_d = max(diffs)
    max_season = seasons[diffs.index(max_d)]

    return {
        "title": "Interpreting Comparative Seasonal Rainfall Data",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "46_interpreting_double_bar_chart_comparison",
        "difficulty": "medium",
        "question_text": (
            "Average seasonal rainfall (mm) for Cape Town and Durban is recorded below:\n\n"
            f"| Season | Cape Town (mm) | Durban (mm) |\n"
            f"| :--- | :--- | :--- |\n"
            f"| Summer | {rf_ct[0]} | {rf_db[0]} |\n"
            f"| Autumn | {rf_ct[1]} | {rf_db[1]} |\n"
            f"| Winter | {rf_ct[2]} | {rf_db[2]} |\n"
            f"| Spring | {rf_ct[3]} | {rf_db[3]} |\n\n"
            f"1. Which season shows the **greatest difference** in rainfall between the two cities?\n"
            f"2. Calculate that maximum difference in mm."
        ),
        "correct_answer": f"1. {max_season}. 2. {max_d} mm.",
        "marking_schema": [
            f"Identify season: {max_season} [1 mark]",
            f"Calculate difference: {max_d} mm [1 mark]",
        ],
        "hints": [
            f"Calculate the difference for each season: Summer={diffs[0]} mm, Autumn={diffs[1]} mm, Winter={diffs[2]} mm, Spring={diffs[3]} mm.",
            f"Identify the largest difference: {max_d} mm.",
            f"The season with {max_d} mm is {max_season}.",
        ],
        "misconception_tags": ["comparative_data_difference_error"],
        "diagram_spec": None,
    }


def arch_47_interpreting_broken_line_temperature_graph(rng: random.Random) -> Dict[str, Any]:
    times = ["06:00", "09:00", "12:00", "15:00", "18:00"]
    temps = [12, 18, 26, 28, 20]
    t_max = max(temps)
    time_max = times[temps.index(t_max)]

    rate_06_12 = (temps[2] - temps[0]) / 6.0

    return {
        "title": "Analysing Diurnal Temperature Changes",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "47_interpreting_broken_line_temperature_graph",
        "difficulty": "medium",
        "question_text": (
            "Hourly temperature readings taken in Bloemfontein on an autumn day:\n\n"
            f"| Time | Temperature (°C) |\n"
            f"| :--- | :--- |\n"
            f"| {times[0]} | {temps[0]} |\n"
            f"| {times[1]} | {temps[1]} |\n"
            f"| {times[2]} | {temps[2]} |\n"
            f"| {times[3]} | {temps[3]} |\n"
            f"| {times[4]} | {temps[4]} |\n\n"
            f"1. State the time at which the **maximum temperature** was recorded.\n"
            f"2. Calculate the average rate of temperature increase between 06:00 and 12:00 in °C per hour."
        ),
        "correct_answer": f"1. {time_max} ({t_max} °C). 2. {_fmt_sa(rate_06_12, 2)} °C/hour.",
        "marking_schema": [
            f"Identify maximum time: {time_max} [1 mark]",
            f"Rate of change: ({temps[2]} - {temps[0]}) / 6 = {_fmt_sa(rate_06_12, 2)} °C/hour [1 mark]",
        ],
        "hints": [
            f"Find the highest temperature: {t_max} °C at {time_max}.",
            f"Between 06:00 and 12:00, 6 hours elapsed.",
            f"Change in temperature = {temps[2]} - {temps[0]} = {temps[2] - temps[0]} °C. Divide by 6 hours.",
        ],
        "misconception_tags": ["rate_of_change_time_interval_error"],
        "diagram_spec": None,
    }


def arch_48_calculating_median_from_stem_and_leaf_table(rng: random.Random) -> Dict[str, Any]:
    tens = [10, 20, 30]
    vals = [
        12, 14, 15, 17, 19,
        21, 23, 24, 26, 28,
        30, 32, 35, 37, 39,
    ]
    median_val = vals[7]

    return {
        "title": "Determining Median from Stem-and-Leaf Representation",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "48_calculating_median_from_stem_and_leaf_table",
        "difficulty": "medium",
        "question_text": (
            "An ordered stem-and-leaf display shows test marks for 15 learners:\n\n"
            "```\n"
            "Stem | Leaf\n"
            "   1 | 2  4  5  7  9\n"
            "   2 | 1  3  4  6  8\n"
            "   3 | 0  2  5  7  9\n"
            "```\n"
            "Key: `1 | 2` = 12 marks.\n\n"
            "Find the **median mark** for this group of 15 learners."
        ),
        "correct_answer": str(median_val),
        "marking_schema": [
            "Identify 8th position: (15 + 1) / 2 = 8th value [1 mark]",
            f"Read 8th value from display: {median_val} [1 mark]",
        ],
        "hints": [
            "There are 15 scores in total.",
            "The median position is (15 + 1) / 2 = 8th score.",
            f"Count 8 leaves from the smallest: the 8th leaf is 4 in stem 2, giving {median_val}.",
        ],
        "misconception_tags": ["stem_and_leaf_median_position_error"],
        "diagram_spec": None,
    }


def arch_49_calculating_combined_mean_of_two_classes(rng: random.Random) -> Dict[str, Any]:
    n1 = 20
    m1 = rng.choice([55, 60, 65])
    n2 = 30
    m2 = rng.choice([70, 75, 80])

    tot1 = n1 * m1
    tot2 = n2 * m2
    grand_tot = tot1 + tot2
    grand_n = n1 + n2
    comb_mean = grand_tot / grand_n

    return {
        "title": "Calculating Weighted Mean of Combined Classes",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "49_calculating_combined_mean_of_two_classes",
        "difficulty": "hard",
        "question_text": (
            f"Class 8A has **{n1} learners** with a mean test mark of **{m1}%**.\n"
            f"Class 8B has **{n2} learners** with a mean test mark of **{m2}%**.\n\n"
            "Calculate the **combined mean mark** for all 50 learners across both classes."
        ),
        "correct_answer": f"{_fmt_sa(comb_mean, 1)}%",
        "marking_schema": [
            f"Calculate total marks: ({n1} x {m1}) + ({n2} x {m2}) = {tot1} + {tot2} = {grand_tot} [1 mark]",
            f"Divide by 50: {grand_tot} / 50 = {_fmt_sa(comb_mean, 1)}% [1 mark]",
        ],
        "hints": [
            f"Find total marks for Class 8A: {n1} x {m1} = {tot1}.",
            f"Find total marks for Class 8B: {n2} x {m2} = {tot2}.",
            f"Add totals ({tot1} + {tot2} = {grand_tot}) and divide by total learners ({grand_n}).",
        ],
        "misconception_tags": ["unweighted_average_fallacy"],
        "diagram_spec": None,
    }


def arch_50_synthesizing_data_for_policy_recommendation(rng: random.Random) -> Dict[str, Any]:
    before_wait = rng.randint(55, 75)
    after_wait = before_wait - rng.randint(20, 35)
    diff = before_wait - after_wait
    pct_reduction = (diff / before_wait) * 100

    return {
        "title": "Synthesising Data for Policy Recommendations",
        "topic": "Interpret analyse and report on data",
        "grade": 8,
        "term": 1,
        "subskill": "50_synthesizing_data_for_policy_recommendation",
        "difficulty": "medium",
        "question_text": (
            "A public health clinic records average patient waiting times before and after "
            "implementing an electronic booking system:\n\n"
            f"- Average wait time before system: **{before_wait} minutes**\n"
            f"- Average wait time after system: **{after_wait} minutes**\n\n"
            "1. Calculate the reduction in average wait time in minutes.\n"
            "2. State whether the clinic committee should recommend keeping the system, justified by the data."
        ),
        "correct_answer": f"1. {diff} minutes reduction. 2. Yes, the committee should recommend keeping the system because patient wait times dropped significantly by {diff} minutes ({_fmt_sa(pct_reduction, 1)}% reduction).",
        "marking_schema": [
            f"Calculate reduction: {before_wait} - {after_wait} = {diff} minutes [1 mark]",
            "Recommend keeping system with data justification [1 mark]",
        ],
        "hints": [
            f"Subtract the after wait time from the before wait time: {before_wait} - {after_wait}.",
            f"Difference = {diff} minutes.",
            "Since wait time decreased substantially, the system was effective.",
        ],
        "misconception_tags": ["data_informed_policy_gap"],
        "diagram_spec": None,
    }


BUILDERS_26_50 = [
    arch_26_misleading_graph_truncated_vertical_axis,
    arch_27_misleading_pictograph_area_volume_distortion,
    arch_28_misleading_graph_irregular_time_intervals,
    arch_29_interpreting_line_graph_trend,
    arch_30_predicting_future_value_by_linear_extrapolation,
    arch_31_interpolating_value_from_data_table,
    arch_32_two_way_contingency_table_gender_by_grade,
    arch_33_calculating_percentage_proportion_from_subgroup,
    arch_34_identifying_modal_class_interval_from_histogram,
    arch_35_estimating_mean_from_grouped_frequency_table,
    arch_36_distinguishing_correlation_from_causation,
    arch_37_impact_of_sample_size_on_reliability,
    arch_38_interpreting_pie_chart_sector_budget,
    arch_39_choosing_median_for_household_income,
    arch_40_writing_summary_statement_from_data_table,
    arch_41_identifying_confounding_variable,
    arch_42_comparing_two_groups_spread_and_consistency,
    arch_43_percentage_increase_vs_percentage_point_difference,
    arch_44_evaluating_leading_question_bias,
    arch_45_evaluating_sampling_exclusion_bias,
    arch_46_interpreting_double_bar_chart_comparison,
    arch_47_interpreting_broken_line_temperature_graph,
    arch_48_calculating_median_from_stem_and_leaf_table,
    arch_49_calculating_combined_mean_of_two_classes,
    arch_50_synthesizing_data_for_policy_recommendation,
]
