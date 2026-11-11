"""Cluster 6: Pie Charts & Advanced Data Interpretation (Subskills 44 to 52).

Covers:
44. Pie chart sector angle calculation from percentage (Angle = % ÷ 100 × 360°)
45. Percentage calculation from measured sector angle (Percentage = Angle ÷ 360° × 100%)
46. Category frequency derivation from sector angle and grand total sample size
47. Total sample size reconstruction from a single sector value and percentage share
48. Scatter plot correlation identification (positive, negative, zero correlation)
49. Line of best fit (trendline) estimation and linear interpolation
50. Misleading 3D perspective distortion in pie charts (spatial visual bias)
51. Stats SA census demographic tables interpretation (municipal services)
52. Selection of optimal summary statistic (Mean vs Median vs Mode) for skewed contexts
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    SA_PROVINCES,
    _fmt,
    _fmt_curr,
    _build_question_payload,
)


def _gen_data_pie_sector_angle_from_percentage(r: random.Random) -> Dict[str, Any]:
    pct = r.choice([15, 20, 25, 30, 35, 40, 45, 60])
    angle = round((pct / 100.0) * 360.0, 1)

    prompt = (
        f"A municipal survey shows that **{pct}%** of households in a ward use prepaid electricity meters.\n\n"
        f"A learner is constructing a pie chart to represent this data graphically.\n\n"
        f"Formula: Sector Angle = (Percentage ÷ 100) × 360°\n\n"
        f"Calculate the size of the sector angle (in degrees) that must be drawn with a protractor "
        f"to represent the {pct}% prepaid electricity share."
    )
    ans = f"{_fmt(angle)}°"

    s1 = f"Multiply the percentage ({pct}%) converted to a decimal by 360° (the total degrees in a complete circle): ({pct} ÷ 100) × 360°."
    s2 = f"✓ [1 Mark: Method – Angle calculation setup]\nSector Angle = ({pct} ÷ 100) × 360° = {_fmt(pct / 100)} × 360°."
    s3 = f"✓ [1 Mark: Accuracy – Sector angle in degrees]\nAngle = {_fmt(angle)}°."

    pie_diag = {
        "kind": "pie_chart",
        "slices": [
            {"label": f"Prepaid ({pct}%)", "value": pct, "color": "#1d4ed8"},
            {"label": f"Other ({100 - pct}%)", "value": 100 - pct, "color": "#94a3b8"},
        ],
        "caption": "Household Electricity Meter Survey",
    }

    return _build_question_payload(
        "data_pie_sector_angle_from_percentage",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {pct} by 100 and multiply by 360°.",
        tier_2_hint=f"({pct} ÷ 100) × 360° = {_fmt(angle)}°.",
        tier_3_hint=f"Sector angle = {_fmt(angle)}°.",
        diagram_spec=pie_diag,
    )


def _gen_data_pie_percentage_from_sector_degrees(r: random.Random) -> Dict[str, Any]:
    angle = r.choice([54, 72, 90, 108, 126, 144, 180])
    pct = round((angle / 360.0) * 100.0, 1)

    prompt = (
        f"A pie chart in a national education report depicts the distribution of high school matric candidates.\n\n"
        f"A learner measures the sector angle representing candidates who wrote Mathematical Literacy "
        f"using a protractor and finds it measures exactly **{angle}°**.\n\n"
        f"Formula: Percentage (%) = (Sector Angle ÷ 360°) × 100%\n\n"
        f"Calculate the percentage of matric candidates represented by this {angle}° slice."
    )
    ans = f"{_fmt(pct)}%"

    s1 = f"Divide the measured sector angle ({angle}°) by the full circle angle (360°) and multiply by 100%."
    s2 = f"✓ [1 Mark: Method – Sector percentage formula substitution]\nPercentage = ({angle}° ÷ 360°) × 100%."
    s3 = f"✓ [1 Mark: Accuracy – Calculated percentage]\nPercentage = {_fmt(pct)}%."

    return _build_question_payload(
        "data_pie_percentage_from_sector_degrees",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {angle}° by 360° and multiply by 100.",
        tier_2_hint=f"({angle} ÷ 360) × 100 = {_fmt(pct)}%.",
        tier_3_hint=f"Percentage = {_fmt(pct)}%.",
    )


def _gen_data_pie_frequency_from_sector_angle(r: random.Random) -> Dict[str, Any]:
    total_learners = r.choice([360, 720, 1080, 1200, 1800])
    angle = r.choice([45, 60, 90, 120, 150])
    count = round((angle / 360.0) * total_learners)

    prompt = (
        f"A pie chart represents the favourite school sports chosen by a total population of **{total_learners} learners**.\n\n"
        f"The sector representing Netball has a central angle of **{angle}°**.\n\n"
        f"Formula: Frequency = (Sector Angle ÷ 360°) × Total Population\n\n"
        f"Calculate how many individual learners chose Netball as their favourite sport."
    )
    ans = f"{count} learners"

    s1 = f"Multiply the proportion of the circle ({angle}° ÷ 360°) by the total learner population ({total_learners})."
    s2 = f"✓ [1 Mark: Method – Sector frequency formula setup]\nFrequency = ({angle}° ÷ 360°) × {total_learners}."
    s3 = f"✓ [1 Mark: Accuracy – Final learner count]\nLearners = {count} learners."

    return _build_question_payload(
        "data_pie_frequency_from_sector_angle",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {angle}° by 360°, then multiply by {total_learners}.",
        tier_2_hint=f"({angle} ÷ 360) × {total_learners} = {count}.",
        tier_3_hint=f"Frequency = {count} learners.",
    )


def _gen_data_pie_total_dataset_from_sector_value(r: random.Random) -> Dict[str, Any]:
    pct = r.choice([20, 25, 40, 50])
    sector_value = r.choice([150, 240, 350, 500, 600])
    grand_total = round((sector_value / pct) * 100)

    prompt = (
        f"Refer to the refuse collection pie chart below. The slice representing "
        f"'Households with weekly municipal curbside collection' accounts for **{pct}%** of the chart, "
        f"which corresponds to exactly **{sector_value} households**.\n\n"
        f"Calculate the **total number of households** surveyed in the entire municipality."
    )
    ans = f"{grand_total} households"

    s1 = f"Use reverse percentage calculation: Total = Sector Value ÷ (Percentage ÷ 100) = {sector_value} ÷ ({pct} ÷ 100) = {sector_value} ÷ {_fmt(pct / 100)}."
    s2 = f"✓ [1 Mark: Method – Reverse percentage setup]\nTotal = ({sector_value} ÷ {pct}) × 100."
    s3 = f"✓ [1 Mark: Accuracy – Total population count]\nTotal = {grand_total} households."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "pie_chart",
        "title": f"Refuse Collection ({grand_total} Households)",
        "slices": [
            {"label": "Curbside", "value": sector_value, "color": "#2563eb"},
            {"label": "Other", "value": grand_total - sector_value, "color": "#94a3b8"},
        ],
    }

    return _build_question_payload(
        "data_pie_total_dataset_from_sector_value",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"If {pct}% equals {sector_value}, find 1% by dividing {sector_value} by {pct}.",
        tier_2_hint=f"Multiply by 100 to get 100%: ({sector_value} ÷ {pct}) × 100.",
        tier_3_hint=f"Total = {grand_total} households.",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"In a pie chart displaying municipal household refuse collection methods, the slice representing "
        f"'Households with weekly municipal curbside collection' accounts for **{pct}%** of the chart, "
        f"which corresponds to exactly **{sector_value} households**.\n\n"
        f"Calculate the **total number of households** surveyed in the entire municipality."
    )
    ans = f"{grand_total} households"

    s1 = f"Use reverse percentage calculation: Total = Sector Value ÷ (Percentage ÷ 100) = {sector_value} ÷ ({pct} ÷ 100) = {sector_value} ÷ {_fmt(pct / 100)}."
    s2 = f"✓ [1 Mark: Method – Reverse percentage setup]\nTotal = ({sector_value} ÷ {pct}) × 100."
    s3 = f"✓ [1 Mark: Accuracy – Total population count]\nTotal = {grand_total} households."

    return _build_question_payload(
        "data_pie_total_dataset_from_sector_value",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"If {pct}% equals {sector_value}, find 1% by dividing {sector_value} by {pct}.",
        tier_2_hint=f"Multiply by 100 to get 100%: ({sector_value} ÷ {pct}) × 100.",
        tier_3_hint=f"Total = {grand_total} households.",
    )


def _gen_data_scatter_correlation_pattern_interpretation(r: random.Random) -> Dict[str, Any]:
    scenario = r.choice([
        (
            "Hours spent studying Mathematical Literacy weekly vs Examination final marks (%)",
            "Strong Positive Correlation",
            "As the number of study hours increases, the examination marks generally increase."
        ),
        (
            "Age of a second-hand passenger car (in years) vs Market resale value (in Rands)",
            "Strong Negative Correlation",
            "As the age of the vehicle increases, its market resale value decreases."
        ),
        (
            "Learner's shoe size vs Mathematical Literacy test percentage mark",
            "No Correlation (Zero Correlation)",
            "There is no statistical or causal relationship between physical shoe size and mathematical performance."
        ),
    ])
    ctx, correct_corr, explanation = scenario

    prompt = (
        f"A researcher plots a **Scatter Plot** investigating the statistical relationship between:\n"
        f"**'{ctx}'**\n\n"
        f"Identify the expected type of correlation (Positive, Negative, or No Correlation) and provide the logical reasoning."
    )
    ans = f"{correct_corr} — {explanation}"
    opts = [
        f"{correct_corr} — {explanation}",
        "Inverse parabolic correlation with zero trendline.",
        "Constant horizontal correlation.",
        "Undetermined categorical correlation.",
    ]

    s1 = f"Identify the direction of association: Positive (both variables increase together), Negative (one increases as other decreases), or Zero (scattered dots with no trend)."
    s2 = f"✓ [1 Mark: Method – Identifying direction of bivariate association]\n{explanation}"
    s3 = f"✓ [1 Mark: Accuracy – Correlation classification]\n{ans}"

    return _build_question_payload(
        "data_scatter_correlation_pattern_interpretation",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Do the two variables increase together, or does one go down as the other goes up?",
        tier_2_hint=f"Consider the real-world connection in '{ctx}'.",
        tier_3_hint=f"{ans}",
    )


def _gen_data_scatter_line_of_best_fit_estimation(r: random.Random) -> Dict[str, Any]:
    m = r.choice([8.0, 10.0, 12.0])  # mark increase per hour studied
    c = 30.0  # base mark with 0 hours
    hours = r.choice([3.0, 4.0, 5.0, 6.0])
    predicted_mark = round(m * hours + c)

    prompt = (
        f"A scatter plot comparing hours studied per week (x) and test marks (y) has a drawn **Line of Best Fit** (trendline).\n\n"
        f"According to the trendline equation:\n"
        f"Predicted Mark (%) = ({_fmt(m)} × Hours Studied) + {_fmt(c)}\n\n"
        f"Using this line of best fit, estimate the test mark of a learner who studies for **{_fmt(hours)} hours** per week."
    )
    ans = f"{predicted_mark}%"

    s1 = f"Substitute x = {_fmt(hours)} hours into the linear trendline formula: y = ({_fmt(m)} × {_fmt(hours)}) + {_fmt(c)}."
    s2 = f"✓ [1 Mark: Method – Trendline formula substitution]\nMark = ({_fmt(m)} × {_fmt(hours)}) + {_fmt(c)} = {_fmt(m * hours)} + {_fmt(c)}."
    s3 = f"✓ [1 Mark: Accuracy – Predicted percentage mark]\nPredicted Mark = {predicted_mark}%."

    return _build_question_payload(
        "data_scatter_line_of_best_fit_estimation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Multiply {_fmt(m)} by {_fmt(hours)}, then add {_fmt(c)}.",
        tier_2_hint=f"({_fmt(m)} × {_fmt(hours)}) + {_fmt(c)} = {_fmt(m * hours + c)}.",
        tier_3_hint=f"Predicted mark = {predicted_mark}%.",
    )


def _gen_data_misleading_pie_chart_3d_perspective(r: random.Random) -> Dict[str, Any]:
    share_x = r.choice([30, 35, 38])
    share_y = r.choice([42, 45, 48])
    share_z = 100 - share_x - share_y

    prompt = (
        f"Refer to the 3D perspective pie chart below displaying market share between competing brands:\n"
        f"• Brand X (foreground/front slice): {share_x}% of the market\n"
        f"• Brand Y (background/rear slice): {share_y}% of the market\n\n"
        f"Because the pie chart is tilted horizontally at a sharp 3D perspective angle towards the viewer, "
        f"the {share_x}% slice in front appears visually larger on the page than the {share_y}% slice in the back!\n\n"
        f"Why do statisticians and curriculum guidelines advise against using 3D perspective pie charts?"
    )
    ans = "The 3D tilt distorts visual perspective, making slices placed in the foreground appear deceptively larger than equal or larger slices placed in the background."
    opts = [
        "The 3D tilt distorts visual perspective, making slices placed in the foreground appear deceptively larger than equal or larger slices placed in the background.",
        "3D charts consume too much computer battery power to display.",
        "Circles cannot exist in three dimensions under South African law.",
        "The angles inside a 3D circle only add up to 180 degrees.",
    ]

    s1 = f"Understand visual statistical distortion: three-dimensional perspective tilting violates the fundamental data visualization rule that graphical area must be directly proportional to numerical frequency."
    s2 = f"✓ [1 Mark: Method – Identifying perspective distortion in data graphics]\nPerspective foreshortening enlarges front angles and compresses rear angles, misleading the reader."
    s3 = f"✓ [1 Mark: Accuracy – Correct statistical critique]\nCritique: {ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "pie_chart",
        "title": f"Market Share 3D Perspective ({share_x}% vs {share_y}%)",
        "slices": [
            {"label": "Brand X (Front)", "value": share_x, "color": "#ef4444"},
            {"label": "Brand Y (Rear)", "value": share_y, "color": "#3b82f6"},
            {"label": "Brand Z", "value": share_z, "color": "#94a3b8"},
        ],
    }

    return _build_question_payload(
        "data_misleading_pie_chart_3d_perspective",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="How does the 3D angle affect the way slices look to your eye?",
        tier_2_hint="The front slice looks bigger because of 3D perspective, even though its percentage is smaller.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Understand visual statistical distortion: three-dimensional perspective tilting violates the fundamental data visualization rule that graphical area must be directly proportional to numerical frequency."
    s2 = f"✓ [1 Mark: Method – Identifying perspective distortion in data graphics]\nPerspective foreshortening enlarges front angles and compresses rear angles, misleading the reader."
    s3 = f"✓ [1 Mark: Accuracy – Correct statistical critique]\nCritique: {ans}"

    return _build_question_payload(
        "data_misleading_pie_chart_3d_perspective",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="How does the 3D angle affect the way slices look to your eye?",
        tier_2_hint="The front slice looks bigger because of 3D perspective, even though its percentage is smaller.",
        tier_3_hint=f"{ans}",
    )


def _gen_data_stats_sa_census_demographics_interpretation(r: random.Random) -> Dict[str, Any]:
    prov = r.choice(SA_PROVINCES)
    piped_water_pct = r.choice([72.4, 78.5, 84.2, 89.6])
    borehole_pct = r.choice([8.5, 11.2, 14.0])
    rain_tank_pct = r.choice([4.2, 6.5, 7.8])
    other_pct = round(100.0 - piped_water_pct - borehole_pct - rain_tank_pct, 1)

    prompt = (
        f"Refer to the Stats SA census demographics bar chart below for household drinking water in {prov}:\n\n"
        f"• Piped tap water: {_fmt(piped_water_pct)}%\n"
        f"• Communal borehole: {_fmt(borehole_pct)}%\n"
        f"• Rainwater harvesting tank: {_fmt(rain_tank_pct)}%\n"
        f"• Other: {_fmt(other_pct)}%\n\n"
        f"1. What is the most prevalent (modal) water source in {prov}?\n"
        f"2. If {prov} has a total of 1 500 000 households, calculate the exact number of households "
        f"relying primarily on **rainwater harvesting tanks**."
    )
    rain_households = round((rain_tank_pct / 100.0) * 1_500_000)
    ans = f"Modal source = Piped tap water ({_fmt(piped_water_pct)}%); Rainwater households = {_fmt(rain_households)}"

    s1 = f"Identify the highest percentage ({_fmt(piped_water_pct)}% = Piped tap water). Calculate rainwater households: ({_fmt(rain_tank_pct)} ÷ 100) × 1 500 000."
    s2 = f"✓ [1 Mark: Method – Identifying mode and percentage calculation]\nModal = Piped tap water ({_fmt(piped_water_pct)}%).\nRainwater = ({_fmt(rain_tank_pct)} ÷ 100) × 1 500 000."
    s3 = f"✓ [1 Mark: Accuracy – Modal category and household calculation]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Stats SA Water Sources ({prov})",
        "categories": ["Piped", "Borehole", "Rain Tank", "Other"],
        "values": [piped_water_pct, borehole_pct, rain_tank_pct, other_pct],
        "x_label": "Water Source",
        "y_label": "Percentage (%)",
    }

    return _build_question_payload(
        "data_stats_sa_census_demographics_interpretation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Which category has the highest bar/percentage? Piped tap water ({_fmt(piped_water_pct)}%).",
        tier_2_hint=f"Find {_fmt(rain_tank_pct)}% of 1 500 000: ({_fmt(rain_tank_pct)} ÷ 100) × 1 500 000.",
        tier_3_hint=f"{ans}.",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"Statistics South Africa (Stats SA) published the following census data regarding primary drinking water "
        f"sources for households in {prov}:\n\n"
        f"| Water Source | Percentage of Households (%) |\n"
        f"| :--- | :---: |\n"
        f"| Piped tap water inside dwelling or yard | {_fmt(piped_water_pct)}% |\n"
        f"| Communal borehole / groundwater pump | {_fmt(borehole_pct)}% |\n"
        f"| Rainwater harvesting tank | {_fmt(rain_tank_pct)}% |\n"
        f"| Other (spring, river, tanker truck) | {_fmt(other_pct)}% |\n"
        f"| **Total** | **100,0%** |\n\n"
        f"1. What is the most prevalent (modal) water source in {prov}?\n"
        f"2. If {prov} has a total of 1 500 000 households, calculate the exact number of households "
        f"relying primarily on **rainwater harvesting tanks**."
    )
    tanks_count = round((rain_tank_pct / 100.0) * 1_500_000)
    ans = f"Modal source: Piped tap water ({_fmt(piped_water_pct)}%); Rainwater households = {_fmt(tanks_count)}"

    s1 = f"Identify modal category with highest percentage (Piped tap water). Calculate number of households: ({rain_tank_pct} ÷ 100) × 1 500 000 = {tanks_count}."
    s2 = f"✓ [1 Mark: Method – Identifying modal category and calculating percentage of total]\nModal: Piped tap water ({_fmt(piped_water_pct)}%).\nHouseholds = ({_fmt(rain_tank_pct)} ÷ 100) × 1 500 000 = {tanks_count}."
    s3 = f"✓ [1 Mark: Accuracy – Modal category and calculated household count]\n{ans}."

    return _build_question_payload(
        "data_stats_sa_census_demographics_interpretation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the largest percentage in the table for the modal source.",
        tier_2_hint=f"Multiply {_fmt(rain_tank_pct)}% by 1 500 000 households.",
        tier_3_hint=f"{ans}.",
    )


def _gen_data_summary_statistics_measure_selection(r: random.Random) -> Dict[str, Any]:
    context_type = r.choice([
        (
            "A shoe store manager wants to know which shoe size to order most stock of from the factory",
            "Mode",
            "Shoe sizes are discrete categories where the store must stock the most frequently requested size; the mean shoe size (e.g. 7,42) cannot be manufactured."
        ),
        (
            "An economist analyzes household wealth in a country with extreme income inequality and a few billionaires",
            "Median",
            "The median is resistant to extreme high outliers (billionaires) and represents the true midpoint where 50% of the population lies below and 50% above."
        ),
        (
            "A swimming coach wants to calculate the total team race time by summing individual 100 m split times",
            "Mean",
            "The mean directly relates to the mathematical total sum (Total = Mean × n), which is needed to project aggregate team time."
        ),
    ])
    scenario_desc, correct_measure, rationale = context_type

    prompt = (
        f"Statistical Decision Making Scenario:\n"
        f"**'{scenario_desc}'**\n\n"
        f"Which measure of central tendency (**Mean, Median, or Mode**) is the most appropriate and useful to use in this situation, and why?"
    )
    ans = f"{correct_measure} — {rationale}"
    opts = [
        f"{correct_measure} — {rationale}",
        "Range — Spread is always superior to averages.",
        "Lower Quartile — Only the bottom 25% should be considered.",
        "Standard Deviation — It replaces all measures of central tendency.",
    ]

    s1 = f"Select the optimal summary statistic based on data scale (nominal, ordinal, interval/ratio) and statistical distribution (symmetric vs skewed)."
    s2 = f"✓ [1 Mark: Method – Matching context requirements with statistical properties]\n{rationale}"
    s3 = f"✓ [1 Mark: Accuracy – Selection of {correct_measure} and justification]\n{ans}"

    return _build_question_payload(
        "data_summary_statistics_measure_selection",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Consider what the manager/analyst is trying to achieve with the number.",
        tier_2_hint=f"Read the specific context carefully: '{scenario_desc}'.",
        tier_3_hint=f"{ans}",
    )
