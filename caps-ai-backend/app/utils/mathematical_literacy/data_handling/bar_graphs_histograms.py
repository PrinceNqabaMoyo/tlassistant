"""Cluster 5: Bar Graphs, Histograms & Graphical Displays (Subskills 35 to 43).

Covers:
35. Single vertical bar graph reading and value extraction from y-axis
36. Compound (double / comparative) bar graph reading and difference analysis
37. Stacked (component) bar graph decomposition into segmented values
38. Continuous histogram reading across touching class interval bins
39. Fundamental graphical distinctions: Bar graphs (gaps) vs Histograms (touching bars)
40. Time-series line graph trend interpretation and rate of change
41. Misleading graphical representation audit: truncated/broken y-axes
42. Frequency polygon construction and class midpoint coordinates
43. Percentage increase or decrease calculation between comparative bars
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_data_graph_single_vertical_bar_reading(r: random.Random) -> Dict[str, Any]:
    categories = ["Term 1", "Term 2", "Term 3", "Term 4"]
    values = [r.randint(120, 180), r.randint(150, 220), r.randint(180, 260), r.randint(210, 300)]
    idx = r.randint(0, 3)
    target_cat = categories[idx]
    target_val = values[idx]

    table_desc = " | ".join([f"{c}: {v} units" for c, v in zip(categories, values)])

    prompt = (
        f"A vertical bar graph displays quarterly textbook deliveries to high schools in a municipal district.\n\n"
        f"The height of each vertical bar plotted along the vertical y-axis (scale in units of 10) indicates:\n"
        f"• {table_desc}\n\n"
        f"Read the bar graph to determine the exact number of textbook units delivered in **{target_cat}**."
    )
    ans = f"{target_val} units"

    s1 = f"Locate the category '{target_cat}' along the horizontal x-axis and project vertically to read the height against the vertical y-axis ({target_val} units)."
    s2 = f"✓ [1 Mark: Method – Reading vertical bar height against y-axis scale]\nBar height for {target_cat} = {target_val} units."
    s3 = f"✓ [1 Mark: Accuracy – Value read from graph]\nDeliveries = {target_val} units."

    bar_diag = {
        "kind": "bar_graph",
        "categories": categories,
        "values": values,
        "x_label": "School Terms",
        "y_label": "Textbook Units",
        "caption": "Quarterly Textbook Deliveries",
    }

    return _build_question_payload(
        "data_graph_single_vertical_bar_reading",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find '{target_cat}' on the horizontal axis.",
        tier_2_hint=f"Read the corresponding height on the vertical axis: {target_val}.",
        tier_3_hint=f"Deliveries = {target_val} units.",
        diagram_spec=bar_diag,
    )


def _gen_data_graph_compound_double_bar_comparison(r: random.Random) -> Dict[str, Any]:
    years = ["2023", "2024"]
    sports = ["Soccer", "Netball", "Athletics"]
    val_23 = r.randint(45, 65)
    val_24 = val_23 + r.randint(12, 28)
    diff = val_24 - val_23

    prompt = (
        f"Study the accompanying double bar graph comparing learner participation in school sports between 2023 and 2024:\n\n"
        f"For Soccer:\n"
        f"• 2023 bar height: {val_23} participants\n"
        f"• 2024 bar height: {val_24} participants\n\n"
        f"1. In which year was participation higher?\n"
        f"2. By how many participants did soccer enrollment increase between 2023 and 2024?"
    )
    ans = f"2024 — increased by {diff} participants"

    s1 = f"Compare the paired bar heights for 2023 ({val_23}) and 2024 ({val_24}), then subtract to find the increase ({val_24} − {val_23} = {diff})."
    s2 = f"✓ [1 Mark: Method – Double bar height comparison and subtraction]\nIncrease = {val_24} − {val_23} = {diff}."
    s3 = f"✓ [1 Mark: Accuracy – Year of higher participation and numeric increase]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "double_bar_graph",
        "title": "Sports Participation Double Bar Graph",
        "categories": sports,
        "series": [
            {"name": "2023", "values": [val_23, r.randint(30, 48), r.randint(25, 42)]},
            {"name": "2024", "values": [val_24, r.randint(40, 60), r.randint(30, 50)]},
        ],
        "x_label": "Sports Code",
        "y_label": "Participants",
    }

    return _build_question_payload(
        "data_graph_compound_double_bar_comparison",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Compare the two bar heights: {val_24} (2024) vs {val_23} (2023).",
        tier_2_hint=f"Subtract the earlier year from the later year: {val_24} − {val_23} = {diff}.",
        tier_3_hint=f"{ans}.",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"A double bar graph compares learner participation in school sports between 2023 and 2024:\n\n"
        f"For Soccer:\n"
        f"• 2023 bar height: {val_23} participants\n"
        f"• 2024 bar height: {val_24} participants\n\n"
        f"1. In which year was participation higher?\n"
        f"2. By how many participants did soccer enrollment increase between 2023 and 2024?"
    )
    ans = f"2024 — increased by {diff} participants"

    s1 = f"Compare the paired bar heights for 2023 ({val_23}) and 2024 ({val_24}), then subtract to find the increase ({val_24} − {val_23} = {diff})."
    s2 = f"✓ [1 Mark: Method – Double bar height comparison and subtraction]\nIncrease = {val_24} − {val_23} = {diff}."
    s3 = f"✓ [1 Mark: Accuracy – Year of higher participation and numeric increase]\n{ans}."

    return _build_question_payload(
        "data_graph_compound_double_bar_comparison",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Compare the two bar heights: {val_24} (2024) vs {val_23} (2023).",
        tier_2_hint=f"Subtract the earlier year from the later year: {val_24} − {val_23} = {diff}.",
        tier_3_hint=f"{ans}.",
    )


def _gen_data_graph_stacked_component_bar_breakdown(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    fixed_charge = 150
    energy_charge = r.choice([350, 420, 500, 580])
    vat_charge = round((fixed_charge + energy_charge) * 0.15, 2)
    total_bill = fixed_charge + energy_charge + vat_charge

    prompt = (
        f"Refer to the segmented stacked bar graph below illustrating {name}'s municipal electricity bill.\n\n"
        f"The single vertical bar has a total height of {_fmt(total_bill)} Rands, broken into 3 stacked segments:\n"
        f"• Bottom segment (Fixed Service Charge): R {fixed_charge},00\n"
        f"• Middle segment (Electricity Energy Consumption): R {energy_charge},00\n"
        f"• Top segment (15% VAT): R {_fmt(vat_charge)}\n\n"
        f"What percentage of the total municipal electricity bill is accounted for by the electricity "
        f"energy consumption charge alone? (Round to 1 decimal place)."
    )
    pct = round((energy_charge / total_bill) * 100, 1)
    ans = f"{_fmt(pct)}%"

    s1 = f"Divide the middle energy consumption segment value (R {energy_charge},00) by the total stacked bar height (R {_fmt(total_bill)}) and multiply by 100."
    s2 = f"✓ [1 Mark: Method – Component value divided by total stacked height]\nPercentage = (R {energy_charge} ÷ R {_fmt(total_bill)}) × 100%."
    s3 = f"✓ [1 Mark: Accuracy – Calculated percentage to 1 decimal place]\nEnergy share = {_fmt(pct)}%."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Electricity Bill Component Breakdown ({name})",
        "categories": ["Fixed Service", "Energy Usage", "15% VAT"],
        "values": [fixed_charge, energy_charge, vat_charge],
        "x_label": "Bill Item",
        "y_label": "Amount (Rands)",
    }

    return _build_question_payload(
        "data_graph_stacked_component_bar_breakdown",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide the energy segment (R {energy_charge}) by total height (R {_fmt(total_bill)}).",
        tier_2_hint=f"({energy_charge} ÷ {_fmt(total_bill)}) × 100 = {_fmt(pct)}%.",
        tier_3_hint=f"Percentage = {_fmt(pct)}%.",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name}'s municipal electricity bill is displayed as a segmented stacked (component) bar graph.\n\n"
        f"The single vertical bar has a total height of {_fmt(total_bill)} Rands, broken into 3 stacked segments:\n"
        f"• Bottom segment (Fixed Service Charge): R {fixed_charge},00\n"
        f"• Middle segment (Electricity Energy Consumption): R {energy_charge},00\n"
        f"• Top segment (15% VAT): R {_fmt(vat_charge)}\n\n"
        f"What percentage of the total municipal electricity bill is accounted for by the electricity "
        f"energy consumption charge alone? (Round to 1 decimal place)."
    )
    pct = round((energy_charge / total_bill) * 100, 1)
    ans = f"{_fmt(pct)}%"

    s1 = f"Divide the middle energy consumption segment value (R {energy_charge},00) by the total stacked bar height (R {_fmt(total_bill)}) and multiply by 100."
    s2 = f"✓ [1 Mark: Method – Component value divided by total stacked height]\nPercentage = (R {energy_charge} ÷ R {_fmt(total_bill)}) × 100%."
    s3 = f"✓ [1 Mark: Accuracy – Calculated percentage to 1 decimal place]\nEnergy share = {_fmt(pct)}%."

    return _build_question_payload(
        "data_graph_stacked_component_bar_breakdown",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide the energy segment (R {energy_charge}) by total height (R {_fmt(total_bill)}).",
        tier_2_hint=f"({energy_charge} ÷ {_fmt(total_bill)}) × 100 = {_fmt(pct)}%.",
        tier_3_hint=f"Percentage = {_fmt(pct)}%.",
    )


def _gen_data_graph_histogram_continuous_class_intervals(r: random.Random) -> Dict[str, Any]:
    bin_labels = ["0 to <10", "10 to <20", "20 to <30", "30 to <40"]
    bin_heights = [r.randint(5, 12), r.randint(15, 25), r.randint(28, 42), r.randint(10, 18)]
    target_idx = r.randint(0, 3)
    target_bin = bin_labels[target_idx]
    target_f = bin_heights[target_idx]
    total_learners = sum(bin_heights)

    prompt = (
        f"Study the accompanying histogram representing the travel time (in minutes) taken by {total_learners} learners to walk to school.\n\n"
        f"Class interval boundaries and heights:\n"
        f"• 0 to <10 min: height = {bin_heights[0]} learners\n"
        f"• 10 to <20 min: height = {bin_heights[1]} learners\n"
        f"• 20 to <30 min: height = {bin_heights[2]} learners\n"
        f"• 30 to <40 min: height = {bin_heights[3]} learners\n\n"
        f"1. How many learners take between **{target_bin} minutes** to walk to school?\n"
        f"2. Why are there no gaps between the bars of this histogram?"
    )
    ans = f"{target_f} learners — There are no gaps because time is a continuous numerical variable measured in continuous intervals."
    opts = [
        f"{target_f} learners — There are no gaps because time is a continuous numerical variable measured in continuous intervals.",
        f"{target_f} learners — Gaps were omitted to save printer ink.",
        f"{target_f + 5} learners — Histograms always start from 10.",
        f"{target_f} learners — The bars represent discrete qualitative categories.",
    ]

    s1 = f"Read the frequency height of the specified continuous class interval ({target_f}). Explain that histograms have no gaps because they depict continuous data along a continuous number line."
    s2 = f"✓ [1 Mark: Method – Reading histogram bar and continuous interval rationale]\nHeight for interval [{target_bin}] = {target_f} learners. Continuous data requires touching bars."
    s3 = f"✓ [1 Mark: Accuracy – Correct count and continuous justification]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "histogram",
        "title": f"Travel Time Distribution ({total_learners} Learners)",
        "categories": bin_labels,
        "values": bin_heights,
        "x_label": "Walking Time (minutes)",
        "y_label": "Number of Learners",
    }

    return _build_question_payload(
        "data_graph_histogram_continuous_class_intervals",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Find the bar labelled '{target_bin}' to get the number of learners.",
        tier_2_hint="Histograms have touching bars because the variable (time) is continuous with no gaps between intervals.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"A histogram represents the travel time (in minutes) taken by {total_learners} learners to walk to school.\n\n"
        f"The touching rectangular bars have the following class interval boundaries and heights:\n"
        f"• 0 to <10 min: height = {bin_heights[0]} learners\n"
        f"• 10 to <20 min: height = {bin_heights[1]} learners\n"
        f"• 20 to <30 min: height = {bin_heights[2]} learners\n"
        f"• 30 to <40 min: height = {bin_heights[3]} learners\n\n"
        f"1. How many learners take between **{target_bin} minutes** to walk to school?\n"
        f"2. Why are there no gaps between the bars of this histogram?"
    )
    ans = f"{target_f} learners — There are no gaps because time is a continuous numerical variable measured in continuous intervals."
    opts = [
        f"{target_f} learners — There are no gaps because time is a continuous numerical variable measured in continuous intervals.",
        f"{target_f} learners — Gaps were omitted to save printer ink.",
        f"{target_f + 5} learners — Histograms always start from 10.",
        f"{target_f} learners — The bars represent discrete qualitative categories.",
    ]

    s1 = f"Read the frequency height of the specified continuous class interval ({target_f}). Explain that histograms have no gaps because they depict continuous data along a continuous number line."
    s2 = f"✓ [1 Mark: Method – Reading histogram bar and continuous interval rationale]\nHeight for interval [{target_bin}] = {target_f} learners. Continuous data requires touching bars."
    s3 = f"✓ [1 Mark: Accuracy – Correct count and continuous justification]\n{ans}"

    return _build_question_payload(
        "data_graph_histogram_continuous_class_intervals",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Find the bar labelled '{target_bin}' to get the number of learners.",
        tier_2_hint="Histograms have touching bars because the variable (time) is continuous with no gaps between intervals.",
        tier_3_hint=f"{ans}",
    )


def _gen_data_graph_bar_vs_histogram_fundamental_differences(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A Grade 10 Mathematical Literacy teacher displays the comparison chart below contrasting a **Bar Graph** with a **Histogram**.\n\n"
        f"Which statement correctly describes the fundamental mathematical differences between these two graphs?"
    )
    ans = "A Bar Graph displays discrete/categorical data with spaces (gaps) between bars; a Histogram displays continuous numerical data in intervals with bars touching (no spaces)."
    opts = [
        "A Bar Graph displays discrete/categorical data with spaces (gaps) between bars; a Histogram displays continuous numerical data in intervals with bars touching (no spaces).",
        "A Bar Graph is drawn horizontally, while a Histogram can only be drawn vertically.",
        "A Bar Graph requires a compass and protractor, while a Histogram uses a ruler.",
        "A Bar Graph displays percentages, while a Histogram displays currency in Rands.",
    ]

    s1 = f"Distinguish between bar graphs (spaces between discrete categories) and histograms (touching bars representing continuous quantitative bins)."
    s2 = f"✓ [1 Mark: Method – Identifying discrete vs continuous conventions]\nDiscrete categories require spaces between bars to show distinct separate entities. Continuous intervals require touching bars to show a seamless continuum."
    s3 = f"✓ [1 Mark: Accuracy – Correct graphical distinction]\nDistinction: {ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": "Bar Graph vs Histogram Comparison",
        "categories": ["Cat A (Gap)", "Cat B (Gap)", "Cat C (Gap)"],
        "values": [r.randint(15, 25), r.randint(20, 30), r.randint(10, 20)],
        "x_label": "Discrete Categories",
        "y_label": "Frequency",
    }

    return _build_question_payload(
        "data_graph_bar_vs_histogram_fundamental_differences",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Do bar graphs have gaps between the bars? Yes. Do histograms have gaps? No.",
        tier_2_hint="Bar graphs are for discrete/categorical data; histograms are for continuous numerical data.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Distinguish between bar graphs (spaces between discrete categories) and histograms (touching bars representing continuous quantitative bins)."
    s2 = f"✓ [1 Mark: Method – Identifying discrete vs continuous conventions]\nDiscrete categories require spaces between bars to show distinct separate entities. Continuous intervals require touching bars to show a seamless continuum."
    s3 = f"✓ [1 Mark: Accuracy – Correct graphical distinction]\nDistinction: {ans}"

    return _build_question_payload(
        "data_graph_bar_vs_histogram_fundamental_differences",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Do bar graphs have gaps between the bars? Yes. Do histograms have gaps? No.",
        tier_2_hint="Bar graphs are for discrete/categorical data; histograms are for continuous numerical data.",
        tier_3_hint=f"{ans}",
    )


def _gen_data_graph_line_graph_time_series_trend(r: random.Random) -> Dict[str, Any]:
    town = r.choice(["Polokwane", "Bloemfontein", "Kimberley", "Mbombela"])
    temps = [28, 30, 31, 26, 21, 18, 17, 20, 24, 27, 29, 30] # Jan to Dec
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    min_temp = min(temps)
    min_month = months[temps.index(min_temp)]
    max_temp = max(temps)
    max_month = months[temps.index(max_temp)]

    prompt = (
        f"Refer to the monthly temperature line graph below for {town} over a 12-month calendar year:\n\n"
        f"• Summer peaks: Jan (28 °C), Feb (30 °C), Mar (31 °C)\n"
        f"• Autumn decline: Apr (26 °C), May (21 °C)\n"
        f"• Winter troughs: Jun (18 °C), Jul (17 °C), Aug (20 °C)\n"
        f"• Spring recovery: Sep (24 °C), Oct (27 °C), Nov (29 °C), Dec (30 °C)\n\n"
        f"1. In which month was the lowest average temperature recorded, and what was the value?\n"
        f"2. Describe the overall seasonal temperature trend shown by the line graph across the year."
    )
    ans = f"Lowest in {min_month} ({min_temp} °C) — Temperatures decrease steadily from March to July (winter trough) before rising steadily towards December (summer peak)."
    opts = [
        f"Lowest in {min_month} ({min_temp} °C) — Temperatures decrease steadily from March to July (winter trough) before rising steadily towards December (summer peak).",
        f"Lowest in {max_month} ({max_temp} °C) — Temperatures remain identical in every month.",
        f"Lowest in April (26 °C) — Temperatures peak during mid-winter.",
        "The line graph shows no seasonal pattern whatsoever.",
    ]

    s1 = f"Identify the minimum turning point on a time-series line graph ({min_month} at {min_temp} °C) and describe continuous seasonal cyclical variation."
    s2 = f"✓ [1 Mark: Method – Reading trough coordinate and trend trajectory]\nTrough = {min_month} ({min_temp} °C). Trend reflects Southern Hemisphere seasonal cycle."
    s3 = f"✓ [1 Mark: Accuracy – Month, minimum temperature, and seasonal description]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"Monthly Temperatures ({town})",
        "categories": months,
        "values": temps,
        "x_label": "Month",
        "y_label": "Temperature (°C)",
    }

    return _build_question_payload(
        "data_graph_line_graph_time_series_trend",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Find the lowest point on the graph: which month is it, and what is the temperature?",
        tier_2_hint=f"The lowest point is in {min_month} at {min_temp} °C.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"A line graph tracks the average monthly maximum temperature in {town} over a 12-month calendar year:\n\n"
        f"• Summer peaks: Jan (28 °C), Feb (30 °C), Mar (31 °C)\n"
        f"• Autumn decline: Apr (26 °C), May (21 °C)\n"
        f"• Winter troughs: Jun (18 °C), Jul (17 °C), Aug (20 °C)\n"
        f"• Spring recovery: Sep (24 °C), Oct (27 °C), Nov (29 °C), Dec (30 °C)\n\n"
        f"1. In which month was the lowest average temperature recorded, and what was the value?\n"
        f"2. Describe the overall seasonal temperature trend shown by the line graph across the year."
    )
    ans = f"Lowest in {min_month} ({min_temp} °C) — Temperatures decrease steadily from March to July (winter trough) before rising steadily towards December (summer peak)."
    opts = [
        f"Lowest in {min_month} ({min_temp} °C) — Temperatures decrease steadily from March to July (winter trough) before rising steadily towards December (summer peak).",
        f"Lowest in {max_month} ({max_temp} °C) — Temperatures remain identical in every month.",
        f"Lowest in April (26 °C) — Temperatures peak during mid-winter.",
        "The line graph shows no seasonal pattern whatsoever.",
    ]

    s1 = f"Identify the minimum turning point on a time-series line graph ({min_month} at {min_temp} °C) and describe continuous seasonal cyclical variation."
    s2 = f"✓ [1 Mark: Method – Reading trough coordinate and trend trajectory]\nTrough = {min_month} ({min_temp} °C). Trend reflects Southern Hemisphere seasonal cycle."
    s3 = f"✓ [1 Mark: Accuracy – Month, minimum temperature, and seasonal description]\n{ans}"

    return _build_question_payload(
        "data_graph_line_graph_time_series_trend",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Find the lowest point on the graph: which month is it, and what is the temperature?",
        tier_2_hint=f"The lowest point is in {min_month} at {min_temp} °C.",
        tier_3_hint=f"{ans}",
    )


def _gen_data_graph_broken_axis_misleading_scale_audit(r: random.Random) -> Dict[str, Any]:
    diff_cents = r.choice([10, 15, 20])
    p_a = 24.10
    p_b = round(p_a + diff_cents / 100.0, 2)
    prompt = (
        f"Refer to the petrol price bar graph below from a newspaper advertisement comparing two service stations:\n"
        f"• Garage A: R {_fmt(p_a)} per litre\n"
        f"• Garage B: R {_fmt(p_b)} per litre (difference of only {diff_cents} cents)\n\n"
        f"However, the vertical y-axis does NOT start at zero (0). Instead, the y-axis starts at **R 24,00**.\n"
        f"As a visual result, the bar for Garage B appears disproportionately taller than the bar for Garage A!\n\n"
        f"Why is this graph classified as **misleading and statistically manipulative**?"
    )
    ans = f"Truncating the vertical axis (not starting at zero) distorts the visual proportions, exaggerating a tiny {diff_cents}-cent price difference to make it look massive."
    opts = [
        f"Truncating the vertical axis (not starting at zero) distorts the visual proportions, exaggerating a tiny {diff_cents}-cent price difference to make it look massive.",
        "The graph is perfectly fair because R 24,00 is a round number.",
        "Service stations are not legally allowed to use bar graphs.",
        "The vertical axis should always be labelled in litres rather than Rands.",
    ]

    s1 = f"Critique distorted visual statistics: truncated axes that do not originate at zero artificially amplify minor variance into dramatic visual disparities."
    s2 = f"✓ [1 Mark: Method – Identifying broken/truncated axis visual distortion]\nStarting the scale at R 24,00 distorts true proportion."
    s3 = f"✓ [1 Mark: Accuracy – Correct statistical critique]\nCritique: {ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Petrol Price Comparison ({diff_cents}c Gap)",
        "categories": ["Garage A", "Garage B"],
        "values": [p_a, p_b],
        "x_label": "Service Station",
        "y_label": "Price (R/L)",
    }

    return _build_question_payload(
        "data_graph_broken_axis_misleading_scale_audit",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Does a {diff_cents}-cent difference justify one bar looking much taller than another?",
        tier_2_hint="Not starting the axis at zero distorts visual comparison and exaggerates differences.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Critique distorted visual statistics: truncated axes that do not originate at zero artificially amplify minor variance into dramatic visual disparities."
    s2 = f"✓ [1 Mark: Method – Identifying broken/truncated axis visual distortion]\nStarting the scale at R 24,00 means a bar representing 10 cents above baseline is 1 unit tall, while 20 cents is 2 units tall (double height for a 0,4% true difference)."
    s3 = f"✓ [1 Mark: Accuracy – Correct statistical critique]\nCritique: {ans}"

    return _build_question_payload(
        "data_graph_broken_axis_misleading_scale_audit",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Does a 10-cent difference justify one bar looking twice as tall as another?",
        tier_2_hint="Not starting the axis at zero distorts visual comparison and exaggerates differences.",
        tier_3_hint=f"{ans}",
    )


def _gen_data_graph_frequency_polygon_midpoint_plotting(r: random.Random) -> Dict[str, Any]:
    interval_start = r.choice([10, 20, 30, 40])
    interval_end = interval_start + 10
    midpoint = (interval_start + interval_end) / 2
    f_val = r.randint(12, 28)

    prompt = (
        f"When drawing a **Frequency Polygon** for grouped continuous data (refer to the frequency polygon below), "
        f"each data point plotted on the graph is placed at the **class interval midpoint** along the horizontal x-axis, "
        f"at a height equal to the class frequency on the vertical y-axis.\n\n"
        f"For the class interval **{interval_start} to {interval_end}** with a frequency of **{f_val}**:\n"
        f"1. Calculate the class midpoint.\n"
        f"2. State the exact coordinate (x; y) where this point must be plotted."
    )
    ans = f"Midpoint = {_fmt(midpoint)}; Coordinate = ({_fmt(midpoint)}; {f_val})"

    s1 = f"Calculate the midpoint of the interval by averaging the lower and upper class limits: ({interval_start} + {interval_end}) ÷ 2 = {_fmt(midpoint)}. Pair with frequency {f_val} as (x; y)."
    s2 = f"✓ [1 Mark: Method – Midpoint formula setup and coordinate pairing]\nMidpoint = ({interval_start} + {interval_end}) ÷ 2 = {_fmt(midpoint)}.\nCoordinate = (Midpoint; Frequency) = ({_fmt(midpoint)}; {f_val})."
    s3 = f"✓ [1 Mark: Accuracy – Midpoint and (x; y) coordinate]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "frequency_polygon",
        "title": f"Frequency Polygon Midpoint ({interval_start}-{interval_end})",
        "categories": [str(interval_start), str(midpoint), str(interval_end)],
        "values": [0, f_val, 0],
        "x_label": "Class Interval",
        "y_label": "Frequency",
    }

    return _build_question_payload(
        "data_graph_frequency_polygon_midpoint_plotting",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the middle of {interval_start} and {interval_end}: ({interval_start} + {interval_end}) ÷ 2.",
        tier_2_hint=f"Midpoint = {_fmt(midpoint)}. Combine with frequency {f_val} as an (x; y) pair.",
        tier_3_hint=f"{ans}.",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"When drawing a **Frequency Polygon** for grouped continuous data, each data point plotted on the "
        f"graph is placed at the **class interval midpoint** along the horizontal x-axis, at a height "
        f"equal to the class frequency on the vertical y-axis.\n\n"
        f"For the class interval **{interval_start} to {interval_end}** with a frequency of **{f_val}**:\n"
        f"1. Calculate the class midpoint.\n"
        f"2. State the exact coordinate (x; y) where this point must be plotted."
    )
    ans = f"Midpoint = {_fmt(midpoint)}; Coordinate = ({_fmt(midpoint)}; {f_val})"

    s1 = f"Calculate the midpoint of the interval by averaging the lower and upper class limits: ({interval_start} + {interval_end}) ÷ 2 = {_fmt(midpoint)}. Pair with frequency {f_val} as (x; y)."
    s2 = f"✓ [1 Mark: Method – Midpoint formula setup and coordinate pairing]\nMidpoint = ({interval_start} + {interval_end}) ÷ 2 = {_fmt(midpoint)}.\nCoordinate = (Midpoint; Frequency) = ({_fmt(midpoint)}; {f_val})."
    s3 = f"✓ [1 Mark: Accuracy – Midpoint and (x; y) coordinate]\n{ans}."

    return _build_question_payload(
        "data_graph_frequency_polygon_midpoint_plotting",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the middle of {interval_start} and {interval_end}: ({interval_start} + {interval_end}) ÷ 2.",
        tier_2_hint=f"Midpoint = {_fmt(midpoint)}. Combine with frequency {f_val} as an (x; y) pair.",
        tier_3_hint=f"{ans}.",
    )


def _gen_data_graph_percentage_increase_between_bars(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    v1 = r.choice([200, 250, 400, 500])
    v2 = v1 + r.choice([50, 75, 100, 150])
    diff = v2 - v1
    pct_increase = round((diff / v1) * 100, 1)

    prompt = (
        f"Refer to the municipal health department bar graph below showing childhood immunizations administered:\n"
        f"• May: {v1} children\n"
        f"• June: {v2} children\n\n"
        f"Formula: Percentage Increase = [(New Value − Old Value) ÷ Old Value] × 100%\n\n"
        f"Calculate the percentage increase in immunizations from May to June (rounded to 1 decimal place)."
    )
    ans = f"{_fmt(pct_increase)}%"

    s1 = f"Subtract old value ({v1}) from new value ({v2}) to find absolute increase ({diff}), divide by original value ({v1}), and multiply by 100."
    s2 = f"✓ [1 Mark: Method – Percentage change formula substitution]\nPercentage Increase = [({v2} − {v1}) ÷ {v1}] × 100% = ({diff} ÷ {v1}) × 100%."
    s3 = f"✓ [1 Mark: Accuracy – Final percentage increase]\nIncrease = {_fmt(pct_increase)}%."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Monthly Immunization Increase ({name})",
        "categories": ["May", "June"],
        "values": [v1, v2],
        "x_label": "Month",
        "y_label": "Immunizations",
    }

    return _build_question_payload(
        "data_graph_percentage_increase_between_bars",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the difference between June ({v2}) and May ({v1}): {v2} − {v1} = {diff}.",
        tier_2_hint=f"Divide the increase ({diff}) by the original May value ({v1}) and multiply by 100.",
        tier_3_hint=f"Percentage Increase = {_fmt(pct_increase)}%.",
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"A municipal health department bar graph shows the number of childhood immunizations administered:\n"
        f"• May: {v1} children\n"
        f"• June: {v2} children\n\n"
        f"Formula: Percentage Increase = [(New Value − Old Value) ÷ Old Value] × 100%\n\n"
        f"Calculate the percentage increase in immunizations from May to June (rounded to 1 decimal place)."
    )
    ans = f"{_fmt(pct_increase)}%"

    s1 = f"Subtract old value ({v1}) from new value ({v2}) to find absolute increase ({diff}), divide by original value ({v1}), and multiply by 100."
    s2 = f"✓ [1 Mark: Method – Percentage change formula substitution]\nPercentage Increase = [({v2} − {v1}) ÷ {v1}] × 100% = ({diff} ÷ {v1}) × 100%."
    s3 = f"✓ [1 Mark: Accuracy – Final percentage increase]\nIncrease = {_fmt(pct_increase)}%."

    return _build_question_payload(
        "data_graph_percentage_increase_between_bars",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the difference between June ({v2}) and May ({v1}): {v2} − {v1} = {diff}.",
        tier_2_hint=f"Divide the increase ({diff}) by the original May value ({v1}) and multiply by 100.",
        tier_3_hint=f"Percentage Increase = {_fmt(pct_increase)}%.",
    )
