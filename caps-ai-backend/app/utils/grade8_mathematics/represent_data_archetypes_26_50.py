"""
Grade 8 Mathematics - Represent Data Archetypes (26 to 50).
100% CAPS-aligned deterministic question generators.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 1/03. Represent data.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

from .svg_diagrams import draw_pie_chart_svg, draw_real_world_line_graph_svg


def arch_26_histogram_percentage_of_learners_in_interval(rng: random.Random) -> Dict[str, Any]:
    total = rng.choice([40, 50, 100])
    freq = rng.choice([10, 15, 20, 25])
    pct = int((freq / total) * 100)

    return {
        "title": "Histogram Percentage Calculation",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "26_histogram_percentage_of_learners_in_interval",
        "difficulty": "medium",
        "question_text": (
            f"A histogram displays data for a total sample of **{total} learners**.\n\n"
            f"The bar for the class interval **50 - 59** has a frequency of **{freq}**.\n\n"
            "What percentage of the sample falls into this interval?"
        ),
        "correct_answer": f"{pct}%",
        "marking_schema": [
            f"Calculate percentage: ({freq}/{total}) * 100% = {pct}% (1 mark)",
        ],
        "hints": [
            f"Divide frequency by total: $\\frac{{{freq}}}{{{total}}}$.",
            f"Multiply by 100%: $\\frac{{{freq}}}{{{total}}} \\times 100\\% = {pct}\\%$.",
            f"Percentage = {pct}%.",
        ],
        "misconception_tags": ["percentage_calculation_division_error"],
        "diagram_spec": None,
    }


def arch_27_histogram_determining_class_width_from_axis(rng: random.Random) -> Dict[str, Any]:
    w = rng.choice([5, 10, 15])
    low = rng.choice([20, 30, 40])
    high = low + w

    return {
        "title": "Determining Class Width from Histogram Axis",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "27_histogram_determining_class_width_from_axis",
        "difficulty": "easy",
        "question_text": (
            f"On the horizontal axis of a continuous histogram, a bar spans from **{low}** to **{high}**.\n\n"
            "What is the **class width** of this interval?"
        ),
        "correct_answer": str(w),
        "marking_schema": [
            f"Class width = {high} - {low} = {w} (1 mark)",
        ],
        "hints": [
            "For continuous boundary intervals, class width = upper boundary - lower boundary.",
            f"$\\text{{Class width}} = {high} - {low} = {w}$.",
            f"Class width = {w}.",
        ],
        "misconception_tags": ["class_width_boundary_subtraction_slip"],
        "diagram_spec": None,
    }


def arch_28_histogram_vs_bar_graph_distinction(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Distinguishing Between Bar Graphs and Histograms",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "28_histogram_vs_bar_graph_distinction",
        "difficulty": "medium",
        "question_text": (
            "State the **fundamental difference** in the type of data displayed by a **bar graph** compared to a **histogram**."
        ),
        "correct_answer": "A bar graph represents discrete or categorical data (with spaces between bars), whereas a histogram represents continuous numerical data grouped into intervals (bars touch without spaces).",
        "marking_schema": [
            "State bar graphs = discrete/categorical data with spaces; histograms = continuous grouped data touching without spaces: 2 marks",
        ],
        "hints": [
            "Bar graphs display discrete categories (like transport modes or favorite colors).",
            "Histograms display continuous numerical measurements grouped into intervals (like height, mass, or time).",
            "In bar graphs, bars have spaces; in histograms, bars touch.",
        ],
        "misconception_tags": ["bar_graph_histogram_data_type_confusion"],
        "diagram_spec": None,
    }


def arch_29_histogram_identifying_least_frequent_interval(rng: random.Random) -> Dict[str, Any]:
    intervals = ["20 - 29", "30 - 39", "40 - 49", "50 - 59"]
    freqs = [14, 25, 4, 18]
    least_int = "40 - 49"

    return {
        "title": "Identifying Least Frequent Interval in Histogram",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "29_histogram_identifying_least_frequent_interval",
        "difficulty": "easy",
        "question_text": (
            "A histogram has class intervals with frequencies: "
            "**20-29 (14)**, **30-39 (25)**, **40-49 (4)**, and **50-59 (18)**.\n\n"
            "Which class interval has the **lowest frequency**?"
        ),
        "correct_answer": least_int,
        "marking_schema": [
            f"Identify interval with lowest frequency: {least_int} (frequency 4) (1 mark)",
        ],
        "hints": [
            "Look for the interval with the smallest frequency.",
            "The minimum frequency is 4.",
            f"Least frequent interval: {least_int}.",
        ],
        "misconception_tags": ["lowest_frequency_interval_identification_error"],
        "diagram_spec": None,
    }


def arch_30_histogram_estimating_median_interval(rng: random.Random) -> Dict[str, Any]:
    # Intervals: 10-19 (5), 20-29 (12), 30-39 (8) => Total = 25
    # Middle value is 13th
    # 1-5 in 10-19; 6-17 in 20-29 => 13th is in 20-29
    return {
        "title": "Locating the Median Class Interval",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "30_histogram_estimating_median_interval",
        "difficulty": "hard",
        "question_text": (
            "A grouped frequency distribution of 25 learners shows:\n\n"
            "- **10 - 19**: 5 learners\n"
            "- **20 - 29**: 12 learners\n"
            "- **30 - 39**: 8 learners\n\n"
            "In which class interval does the **median** score lie?"
        ),
        "correct_answer": "20 - 29",
        "marking_schema": [
            "Find position (25+1)/2 = 13th learner => interval 20 - 29: 2 marks",
        ],
        "hints": [
            "With $N = 25$ learners, the median is the 13th ordered value.",
            "The first interval contains learners 1 to 5.",
            "The second interval contains learners 6 to 17, which includes the 13th learner.",
            "The median lies in interval 20 - 29.",
        ],
        "misconception_tags": ["median_interval_cumulative_ranking_error"],
        "diagram_spec": None,
    }


def arch_31_pie_chart_calculating_sector_angle_from_fraction(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        (1, 4, 90),
        (1, 3, 120),
        (1, 6, 60),
        (1, 8, 45),
        (3, 8, 135),
        (3, 4, 270),
        (1, 5, 72),
        (2, 5, 144),
    ]
    num, den, angle = rng.choice(pairs)

    return {
        "title": "Calculating Sector Angle from Fraction",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "31_pie_chart_calculating_sector_angle_from_fraction",
        "difficulty": "medium",
        "question_text": (
            f"A category in a survey represents $\\frac{{{num}}}{{{den}}}$ of the total responses.\n\n"
            "Calculate the size of the **sector angle** (in degrees) needed to represent this category in a circular sector."
        ),
        "correct_answer": f"{angle}°",
        "marking_schema": [
            f"Multiply fraction by 360 degrees: ({num}/{den}) * 360 = {angle}° (1 mark)",
        ],
        "hints": [
            "A complete circle in a pie chart contains $360^\\circ$.",
            f"Multiply the fraction by $360^\\circ$: $\\frac{{{num}}}{{{den}}} \\times 360^\\circ$.",
            f"Sector angle = {angle}°.",
        ],
        "misconception_tags": ["pie_chart_angle_total_degrees_confusion"],
        "diagram_spec": None,
    }


def arch_32_pie_chart_calculating_sector_angle_from_percentage(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([10, 15, 20, 25, 30, 40, 50])
    angle = int((pct / 100) * 360)

    return {
        "title": "Calculating Sector Angle from Percentage",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "32_pie_chart_calculating_sector_angle_from_percentage",
        "difficulty": "medium",
        "question_text": (
            f"In a school survey, **{pct}%** of learners travel to school by bus.\n\n"
            "Calculate the **sector angle** needed to represent bus travelers on a pie chart."
        ),
        "correct_answer": f"{angle}°",
        "marking_schema": [
            f"Calculate angle: ({pct}/100) * 360 = {angle}° (1 mark)",
        ],
        "hints": [
            f"Formula: $\\text{{Angle}} = \\frac{{\\text{{Percentage}}}}{{100}} \\times 360^\\circ$.",
            f"$\\frac{{{pct}}}{{100}} \\times 360^\\circ = {angle}^\\circ$.",
            f"Angle = {angle}°.",
        ],
        "misconception_tags": ["percentage_to_angle_scaling_slip"],
        "diagram_spec": None,
    }


def arch_33_pie_chart_calculating_frequency_from_sector_angle(rng: random.Random) -> Dict[str, Any]:
    total = rng.choice([120, 180, 240, 360])
    angle = rng.choice([60, 90, 120, 150])
    freq = int((angle / 360) * total)

    return {
        "title": "Calculating Frequency from Sector Angle",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "33_pie_chart_calculating_frequency_from_sector_angle",
        "difficulty": "medium",
        "question_text": (
            f"On a pie chart representing **{total} learners**, the sector for Cricket has an angle of **{angle}°**.\n\n"
            "How many learners chose Cricket?"
        ),
        "correct_answer": str(freq),
        "marking_schema": [
            f"Frequency = ({angle}/360) * {total} = {freq} learners (2 marks)",
        ],
        "hints": [
            f"Find what fraction of the circle {angle}° represents: $\\frac{{{angle}}}{{360}}$.",
            f"Multiply by total learners: $\\frac{{{angle}}}{{360}} \\times {total} = {freq}$.",
            f"Number of learners = {freq}.",
        ],
        "misconception_tags": ["angle_to_frequency_inversion_error"],
        "diagram_spec": None,
    }


def arch_34_pie_chart_calculating_frequency_from_percentage(rng: random.Random) -> Dict[str, Any]:
    total = rng.choice([200, 300, 400, 500])
    pct = rng.choice([15, 25, 35, 45])
    freq = int((pct / 100) * total)

    return {
        "title": "Calculating Frequency from Percentage on Pie Chart",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "34_pie_chart_calculating_frequency_from_percentage",
        "difficulty": "easy",
        "question_text": (
            f"A pie chart represents **{total} survey respondents**. The sector for Brand A is **{pct}%**.\n\n"
            "How many respondents chose Brand A?"
        ),
        "correct_answer": str(freq),
        "marking_schema": [
            f"Calculate frequency: ({pct}/100) * {total} = {freq} (1 mark)",
        ],
        "hints": [
            f"Calculate {pct}% of {total}.",
            f"$\\frac{{{pct}}}{{100}} \\times {total} = {freq}$.",
            f"Answer: {freq}.",
        ],
        "misconception_tags": ["percentage_of_total_multiplication_slip"],
        "diagram_spec": None,
    }


def arch_35_pie_chart_reading_proportions_from_svg_diagram(rng: random.Random) -> Dict[str, Any]:
    slices = [
        ("Soccer", 50.0),
        ("Rugby", 25.0),
        ("Netball", 15.0),
        ("Cricket", 10.0),
    ]

    seed_val = rng.randint(1, 1000000)
    svg = draw_pie_chart_svg(
        slices=slices,
        title="Sports Preferences Distribution",
        seed=seed_val,
    )

    return {
        "title": "Reading Proportions from Pie Chart",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "35_pie_chart_reading_proportions_from_svg_diagram",
        "difficulty": "easy",
        "question_text": (
            "Refer to the pie chart below.\n\n"
            "Which sport represents exactly **half (50%)** of all responses?"
        ),
        "correct_answer": "Soccer",
        "marking_schema": [
            "Identify Soccer with 50% sector: 1 mark",
        ],
        "hints": [
            "Half of the circle forms a semicircle with an angle of $180^\\circ$.",
            "The legend and sector indicate that Soccer is 50%.",
            "Sport: Soccer.",
        ],
        "misconception_tags": ["pie_chart_legend_matching_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_36_pie_chart_sum_of_angles_in_full_circle(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Total Angle Sum in a Pie Chart",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "36_pie_chart_sum_of_angles_in_full_circle",
        "difficulty": "easy",
        "question_text": (
            "What is the **sum of all sector angles** at the center of any complete pie chart?"
        ),
        "correct_answer": "360°",
        "marking_schema": [
            "State 360 degrees: 1 mark",
        ],
        "hints": [
            "A full circular revolution consists of 360 degrees.",
            "All sectors in a pie chart must combine to fill the entire circle.",
            "Sum = 360°.",
        ],
        "misconception_tags": ["angle_sum_full_revolution_confusion"],
        "diagram_spec": None,
    }


def arch_37_pie_chart_half_circle_and_quarter_circle_angles(rng: random.Random) -> Dict[str, Any]:
    fraction_choice = rng.choice(["one quarter (1/4)", "one half (1/2)", "three quarters (3/4)"])
    if "quarter (1/4)" in fraction_choice:
        ans = "90°"
    elif "half" in fraction_choice:
        ans = "180°"
    else:
        ans = "270°"

    return {
        "title": "Standard Sector Angles (Quarters and Halves)",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "37_pie_chart_half_circle_and_quarter_circle_angles",
        "difficulty": "easy",
        "question_text": (
            f"What is the sector angle (in degrees) that represents **{fraction_choice}** of a pie chart?"
        ),
        "correct_answer": ans,
        "marking_schema": [
            f"State sector angle for {fraction_choice}: {ans} (1 mark)",
        ],
        "hints": [
            "Multiply the fraction by 360°.",
            f"Sector angle = {ans}.",
        ],
        "misconception_tags": ["fraction_of_circle_angle_slip"],
        "diagram_spec": None,
    }


def arch_38_pie_chart_calculating_missing_sector_angle(rng: random.Random) -> Dict[str, Any]:
    a1 = rng.choice([90, 100, 120])
    a2 = rng.choice([60, 70, 80])
    a3 = rng.choice([50, 60, 70])
    missing = 360 - (a1 + a2 + a3)

    return {
        "title": "Finding Missing Sector Angle in Pie Chart",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "38_pie_chart_calculating_missing_sector_angle",
        "difficulty": "medium",
        "question_text": (
            f"A pie chart is divided into four sectors. Three of the sector angles measure **{a1}°**, **{a2}°**, and **{a3}°**.\n\n"
            "Calculate the size of the fourth sector angle."
        ),
        "correct_answer": f"{missing}°",
        "marking_schema": [
            f"Subtract from 360: 360 - ({a1} + {a2} + {a3}) = {missing}° (1 mark)",
        ],
        "hints": [
            "All angles in a pie chart sum to 360°.",
            f"$\\text{{Missing angle}} = 360^\\circ - ({a1}^\\circ + {a2}^\\circ + {a3}^\\circ)$.",
            f"Answer: {missing}°.",
        ],
        "misconception_tags": ["circle_angle_subtraction_slip"],
        "diagram_spec": None,
    }


def arch_39_pie_chart_calculating_missing_sector_percentage(rng: random.Random) -> Dict[str, Any]:
    p1 = rng.choice([30, 40, 45])
    p2 = rng.choice([20, 25])
    p3 = rng.choice([15, 20])
    missing = 100 - (p1 + p2 + p3)

    return {
        "title": "Finding Missing Sector Percentage in Pie Chart",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "39_pie_chart_calculating_missing_sector_percentage",
        "difficulty": "easy",
        "question_text": (
            f"A pie chart represents four categories. Three categories have percentages of **{p1}%**, **{p2}%**, and **{p3}%**.\n\n"
            "Calculate the percentage for the fourth category."
        ),
        "correct_answer": f"{missing}%",
        "marking_schema": [
            f"Subtract from 100%: 100 - ({p1} + {p2} + {p3}) = {missing}% (1 mark)",
        ],
        "hints": [
            "The sum of all percentages in a pie chart must equal 100%.",
            f"$\\text{{Missing percentage}} = 100\\% - ({p1}\\% + {p2}\\% + {p3}\\%)$.",
            f"Result = {missing}%.",
        ],
        "misconception_tags": ["percentage_sum_100_subtraction_error"],
        "diagram_spec": None,
    }


def arch_40_pie_chart_converting_fraction_of_day_to_sector_angle(rng: random.Random) -> Dict[str, Any]:
    hours = rng.choice([6, 8, 9, 12])
    angle = int((hours / 24) * 360)

    return {
        "title": "Converting Daily Hours to Pie Chart Sector Angle",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "40_pie_chart_converting_fraction_of_day_to_sector_angle",
        "difficulty": "medium",
        "question_text": (
            f"A teenager spends **{hours} hours** of a 24-hour day sleeping.\n\n"
            "Calculate the sector angle in degrees to show sleep on a daily routine pie chart."
        ),
        "correct_answer": f"{angle}°",
        "marking_schema": [
            f"Angle = ({hours}/24) * 360 = {angle}° (2 marks)",
        ],
        "hints": [
            f"Fraction of the day = $\\frac{{{hours}}}{{24}}$.",
            f"Multiply by $360^\\circ$: $\\frac{{{hours}}}{{24}} \\times 360^\\circ = {angle}^\\circ$.",
            f"Sector angle = {angle}°.",
        ],
        "misconception_tags": ["daily_hours_fraction_scaling_slip"],
        "diagram_spec": None,
    }


def arch_41_broken_line_graph_reading_temperature_over_time(rng: random.Random) -> Dict[str, Any]:
    waypoints = [
        (0.0, 15.0, "06:00"),
        (2.0, 20.0, "08:00"),
        (4.0, 26.0, "10:00"),
        (6.0, 30.0, "12:00"),
    ]
    t_reading = "26 °C at 10:00"

    seed_val = rng.randint(1, 1000000)
    svg = draw_real_world_line_graph_svg(
        waypoints=waypoints,
        x_label="Time of Day",
        y_label="Temperature (°C)",
        max_x=6.0,
        max_y=35.0,
        title="Daily Temperature Trend",
        seed=seed_val,
    )

    return {
        "title": "Reading Temperature from Broken-Line Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "41_broken_line_graph_reading_temperature_over_time",
        "difficulty": "easy",
        "question_text": (
            "Refer to the broken-line graph below tracking daily temperature.\n\n"
            "What was the recorded temperature at **10:00** (hour 4)?"
        ),
        "correct_answer": "26 °C",
        "marking_schema": [
            "Read vertical temperature at 10:00: 26 °C (1 mark)",
        ],
        "hints": [
            "Locate 10:00 (x = 4) on the horizontal time axis.",
            "Trace vertically to the data point and across to the temperature axis.",
            "Temperature = 26 °C.",
        ],
        "misconception_tags": ["broken_line_axis_lookup_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


def arch_42_broken_line_graph_identifying_steepest_rise_or_fall(rng: random.Random) -> Dict[str, Any]:
    # Stage 1: 0 to 2 hrs -> rise of 5 (2.5/hr)
    # Stage 2: 2 to 4 hrs -> rise of 12 (6.0/hr - steepest!)
    # Stage 3: 4 to 6 hrs -> rise of 4 (2.0/hr)
    return {
        "title": "Identifying Steepest Rise on Line Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "42_broken_line_graph_identifying_steepest_rise_or_fall",
        "difficulty": "medium",
        "question_text": (
            "On a temperature trend graph, the temperature rises:\n"
            "- From 06:00 to 08:00 by **5°C** (over 2 hours)\n"
            "- From 08:00 to 10:00 by **12°C** (over 2 hours)\n"
            "- From 10:00 to 12:00 by **4°C** (over 2 hours)\n\n"
            "During which two-hour interval was the rate of temperature increase the **steepest**?"
        ),
        "correct_answer": "08:00 to 10:00",
        "marking_schema": [
            "Identify 08:00 to 10:00 (rate of 6 °C/hr): 1 mark",
        ],
        "hints": [
            "Steepest rate means the greatest rise per hour.",
            "08:00 to 10:00 had a rise of 12°C in 2 hours (6°C per hour), which is the greatest.",
            "Interval: 08:00 to 10:00.",
        ],
        "misconception_tags": ["steepest_slope_rate_misidentification"],
        "diagram_spec": None,
    }


def arch_43_broken_line_graph_calculating_overall_change(rng: random.Random) -> Dict[str, Any]:
    t_start = 14
    t_end = 32
    diff = t_end - t_start

    return {
        "title": "Calculating Overall Change on Line Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "43_broken_line_graph_calculating_overall_change",
        "difficulty": "easy",
        "question_text": (
            f"A weather station recorded an initial temperature of **{t_start}°C** at dawn and a peak temperature of **{t_end}°C** in the afternoon.\n\n"
            "Calculate the overall change (increase) in temperature."
        ),
        "correct_answer": f"{diff} °C",
        "marking_schema": [
            f"Overall change = {t_end} - {t_start} = {diff} °C (1 mark)",
        ],
        "hints": [
            f"$\\text{{Change}} = \\text{{Final value}} - \\text{{Initial value}} = {t_end} - {t_start}$.",
            f"Change = {diff} °C.",
        ],
        "misconception_tags": ["overall_change_subtraction_slip"],
        "diagram_spec": None,
    }


def arch_44_broken_line_graph_why_dots_are_connected_by_lines(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Why Dots Are Connected by Line Segments",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "44_broken_line_graph_why_dots_are_connected_by_lines",
        "difficulty": "easy",
        "question_text": (
            "Explain why points are connected by straight-line segments in a **broken-line graph**."
        ),
        "correct_answer": "Connecting segments help visualize the direction, trend, and continuous pattern of change over time.",
        "marking_schema": [
            "Explain that lines show trends and patterns of change over continuous time: 1 mark",
        ],
        "hints": [
            "Broken-line graphs track continuous variables over time.",
            "Connecting lines make it easy to see when a quantity is rising, falling, or remaining steady.",
            "Lines emphasize the trend and progression over time.",
        ],
        "misconception_tags": ["broken_line_trend_concept_gap"],
        "diagram_spec": None,
    }


def arch_45_comparing_two_series_on_broken_line_graph(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Comparing Two Comparative Lines on Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "45_comparing_two_series_on_broken_line_graph",
        "difficulty": "medium",
        "question_text": (
            "A graph plots the mass of Cow A and Cow B from January to June:\n"
            "- In March, Cow A weighed **280 kg** and Cow B weighed **260 kg**.\n"
            "- In April, both cows weighed **295 kg**.\n"
            "- In May, Cow A weighed **310 kg** and Cow B weighed **330 kg**.\n\n"
            "In which month did Cow B first **overtake** Cow A in mass?"
        ),
        "correct_answer": "May",
        "marking_schema": [
            "Identify May where Cow B (330 kg) > Cow A (310 kg): 1 mark",
        ],
        "hints": [
            "Compare the two masses month by month.",
            "In April they were tied at 295 kg.",
            "In May, Cow B reached 330 kg while Cow A was 310 kg.",
            "Month: May.",
        ],
        "misconception_tags": ["comparative_line_overtake_month_confusion"],
        "diagram_spec": None,
    }


def arch_46_graph_suitability_when_to_use_pie_chart(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Graph Suitability: When to Use a Pie Chart",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "46_graph_suitability_when_to_use_pie_chart",
        "difficulty": "easy",
        "question_text": (
            "Why is a circular pie chart considered the preferred visual display for showing how a monthly household budget is divided among expenses?"
        ),
        "correct_answer": "Because a pie chart visually displays how a single whole (100%) is divided into fractional parts or proportions.",
        "marking_schema": [
            "Explain that pie charts show parts/proportions of a whole (100%): 1 mark",
        ],
        "hints": [
            "A budget is a single whole sum of money (100%).",
            "Each expense represents a fraction or percentage of that total.",
            "Pie charts are specifically designed to show proportions of a whole.",
        ],
        "misconception_tags": ["graph_format_selection_error"],
        "diagram_spec": None,
    }


def arch_47_graph_suitability_when_to_use_broken_line_graph(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Graph Suitability: When to Use a Broken-Line Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "47_graph_suitability_when_to_use_broken_line_graph",
        "difficulty": "easy",
        "question_text": (
            "Which type of graph (**pie chart**, **bar graph**, or **broken-line graph**) is most suitable for tracking "
            "changes in daily maximum temperature over the course of a month? Give a reason."
        ),
        "correct_answer": "Broken-line graph, because it clearly illustrates continuous change and trends over time.",
        "marking_schema": [
            "Identify broken-line graph with trend over time justification: 1 mark",
        ],
        "hints": [
            "Temperature changes continuously over time.",
            "Line graphs are ideal for showing how a continuous variable increases, decreases, or fluctuates across time intervals.",
            "Answer: Broken-line graph.",
        ],
        "misconception_tags": ["graph_format_selection_error"],
        "diagram_spec": None,
    }


def arch_48_graph_suitability_when_to_use_bar_graph(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Graph Suitability: When to Use a Bar Graph",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "48_graph_suitability_when_to_use_bar_graph",
        "difficulty": "easy",
        "question_text": (
            "Why is a **bar graph** suitable for displaying the number of learners who participate in different sports clubs?"
        ),
        "correct_answer": "Because sports clubs are separate, discrete categories, allowing bar heights to be easily compared with spaces between them.",
        "marking_schema": [
            "Explain that bar graphs are best for comparing discrete categories: 1 mark",
        ],
        "hints": [
            "Sports clubs (soccer, netball, chess) are separate non-numerical categories.",
            "Bars allow easy visual comparison of individual category frequencies.",
            "Answer: Bar graph compares discrete categories.",
        ],
        "misconception_tags": ["graph_format_selection_error"],
        "diagram_spec": None,
    }


def arch_49_graph_suitability_when_to_use_histogram(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Graph Suitability: When to Use a Histogram",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "49_graph_suitability_when_to_use_histogram",
        "difficulty": "medium",
        "question_text": (
            "Why is a **histogram** chosen instead of a bar graph to display the distribution of heights (in cm) of 100 Grade 8 learners?"
        ),
        "correct_answer": "Because height is a continuous measurement grouped into numerical intervals, requiring touching bars to represent an unbroken scale.",
        "marking_schema": [
            "Explain that height is continuous data grouped into numerical class intervals: 1 mark",
        ],
        "hints": [
            "Height can take any decimal value; it is continuous measurement data.",
            "Data is grouped into continuous intervals (e.g. 140-149 cm, 150-159 cm).",
            "Histograms represent continuous grouped numerical data.",
        ],
        "misconception_tags": ["histogram_suitability_justification_error"],
        "diagram_spec": None,
    }


def arch_50_misleading_graphs_identifying_truncated_vertical_axis(rng: random.Random) -> Dict[str, Any]:
    return {
        "title": "Identifying Misleading Graphs (Truncated Axis)",
        "topic": "Represent data",
        "grade": 8,
        "term": 1,
        "subskill": "50_misleading_graphs_identifying_truncated_vertical_axis",
        "difficulty": "hard",
        "question_text": (
            "In an advertisement, a bar graph showing company sales starts its vertical axis at **R90 000** instead of **0**.\n\n"
            "Explain how this truncated vertical axis can mislead viewers."
        ),
        "correct_answer": "It exaggerates small differences between bars, making a slight increase appear dramatically larger than it actually is.",
        "marking_schema": [
            "Explain that starting above zero exaggerates differences and creates a false visual impression: 2 marks",
        ],
        "hints": [
            "When the vertical axis does not start at 0, bar heights are not proportional to their actual numerical values.",
            "A small percentage difference looks massive because the bottom 90 000 is cut off.",
            "It exaggerates minor differences.",
        ],
        "misconception_tags": ["misleading_graph_truncated_axis_unawareness"],
        "diagram_spec": None,
    }


BUILDERS_26_50 = [
    arch_26_histogram_percentage_of_learners_in_interval,
    arch_27_histogram_determining_class_width_from_axis,
    arch_28_histogram_vs_bar_graph_distinction,
    arch_29_histogram_identifying_least_frequent_interval,
    arch_30_histogram_estimating_median_interval,
    arch_31_pie_chart_calculating_sector_angle_from_fraction,
    arch_32_pie_chart_calculating_sector_angle_from_percentage,
    arch_33_pie_chart_calculating_frequency_from_sector_angle,
    arch_34_pie_chart_calculating_frequency_from_percentage,
    arch_35_pie_chart_reading_proportions_from_svg_diagram,
    arch_36_pie_chart_sum_of_angles_in_full_circle,
    arch_37_pie_chart_half_circle_and_quarter_circle_angles,
    arch_38_pie_chart_calculating_missing_sector_angle,
    arch_39_pie_chart_calculating_missing_sector_percentage,
    arch_40_pie_chart_converting_fraction_of_day_to_sector_angle,
    arch_41_broken_line_graph_reading_temperature_over_time,
    arch_42_broken_line_graph_identifying_steepest_rise_or_fall,
    arch_43_broken_line_graph_calculating_overall_change,
    arch_44_broken_line_graph_why_dots_are_connected_by_lines,
    arch_45_comparing_two_series_on_broken_line_graph,
    arch_46_graph_suitability_when_to_use_pie_chart,
    arch_47_graph_suitability_when_to_use_broken_line_graph,
    arch_48_graph_suitability_when_to_use_bar_graph,
    arch_49_graph_suitability_when_to_use_histogram,
    arch_50_misleading_graphs_identifying_truncated_vertical_axis,
]
