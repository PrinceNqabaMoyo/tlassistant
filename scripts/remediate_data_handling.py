"""Remediate Data Handling (Grade 10)."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DH_BASE = os.path.join(ROOT, "caps-ai-backend", "app", "utils", "mathematical_literacy", "data_handling")

def remediate_bar_graphs():
    p = os.path.join(DH_BASE, "bar_graphs_histograms.py")
    c = open(p, encoding="utf-8").read()

    # 1. _gen_data_graph_compound_double_bar_comparison
    old_fn = re.search(r'def _gen_data_graph_compound_double_bar_comparison\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_graph_compound_double_bar_comparison(r: random.Random) -> Dict[str, Any]:
    years = ["2023", "2024"]
    sports = ["Soccer", "Netball", "Athletics"]
    val_23 = r.randint(45, 65)
    val_24 = val_23 + r.randint(12, 28)
    diff = val_24 - val_23

    prompt = (
        f"Study the accompanying double bar graph comparing learner participation in school sports between 2023 and 2024:\\n\\n"
        f"For Soccer:\\n"
        f"• 2023 bar height: {val_23} participants\\n"
        f"• 2024 bar height: {val_24} participants\\n\\n"
        f"1. In which year was participation higher?\\n"
        f"2. By how many participants did soccer enrollment increase between 2023 and 2024?"
    )
    ans = f"2024 — increased by {diff} participants"

    s1 = f"Compare the paired bar heights for 2023 ({val_23}) and 2024 ({val_24}), then subtract to find the increase ({val_24} − {val_23} = {diff})."
    s2 = f"✓ [1 Mark: Method – Double bar height comparison and subtraction]\\nIncrease = {val_24} − {val_23} = {diff}."
    s3 = f"✓ [1 Mark: Accuracy – Year of higher participation and numeric increase]\\n{ans}."

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)

    # 2. _gen_data_graph_stacked_component_bar_breakdown
    old_fn = re.search(r'def _gen_data_graph_stacked_component_bar_breakdown\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_graph_stacked_component_bar_breakdown(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    fixed_charge = 150
    energy_charge = r.choice([350, 420, 500, 580])
    vat_charge = round((fixed_charge + energy_charge) * 0.15, 2)
    total_bill = fixed_charge + energy_charge + vat_charge

    prompt = (
        f"Refer to the segmented stacked bar graph below illustrating {name}'s municipal electricity bill.\\n\\n"
        f"The single vertical bar has a total height of {_fmt(total_bill)} Rands, broken into 3 stacked segments:\\n"
        f"• Bottom segment (Fixed Service Charge): R {fixed_charge},00\\n"
        f"• Middle segment (Electricity Energy Consumption): R {energy_charge},00\\n"
        f"• Top segment (15% VAT): R {_fmt(vat_charge)}\\n\\n"
        f"What percentage of the total municipal electricity bill is accounted for by the electricity "
        f"energy consumption charge alone? (Round to 1 decimal place)."
    )
    pct = round((energy_charge / total_bill) * 100, 1)
    ans = f"{_fmt(pct)}%"

    s1 = f"Divide the middle energy consumption segment value (R {energy_charge},00) by the total stacked bar height (R {_fmt(total_bill)}) and multiply by 100."
    s2 = f"✓ [1 Mark: Method – Component value divided by total stacked height]\\nPercentage = (R {energy_charge} ÷ R {_fmt(total_bill)}) × 100%."
    s3 = f"✓ [1 Mark: Accuracy – Calculated percentage to 1 decimal place]\\nEnergy share = {_fmt(pct)}%."

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)

    # 3. _gen_data_graph_histogram_continuous_class_intervals
    old_fn = re.search(r'def _gen_data_graph_histogram_continuous_class_intervals\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_graph_histogram_continuous_class_intervals(r: random.Random) -> Dict[str, Any]:
    bin_labels = ["0 to <10", "10 to <20", "20 to <30", "30 to <40"]
    bin_heights = [r.randint(5, 12), r.randint(15, 25), r.randint(28, 42), r.randint(10, 18)]
    target_idx = r.randint(0, 3)
    target_bin = bin_labels[target_idx]
    target_f = bin_heights[target_idx]
    total_learners = sum(bin_heights)

    prompt = (
        f"Study the accompanying histogram representing the travel time (in minutes) taken by {total_learners} learners to walk to school.\\n\\n"
        f"Class interval boundaries and heights:\\n"
        f"• 0 to <10 min: height = {bin_heights[0]} learners\\n"
        f"• 10 to <20 min: height = {bin_heights[1]} learners\\n"
        f"• 20 to <30 min: height = {bin_heights[2]} learners\\n"
        f"• 30 to <40 min: height = {bin_heights[3]} learners\\n\\n"
        f"1. How many learners take between **{target_bin} minutes** to walk to school?\\n"
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
    s2 = f"✓ [1 Mark: Method – Reading histogram bar and continuous interval rationale]\\nHeight for interval [{target_bin}] = {target_f} learners. Continuous data requires touching bars."
    s3 = f"✓ [1 Mark: Accuracy – Correct count and continuous justification]\\n{ans}"

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)

    # 4. _gen_data_graph_bar_vs_histogram_fundamental_differences
    old_fn = re.search(r'def _gen_data_graph_bar_vs_histogram_fundamental_differences\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_graph_bar_vs_histogram_fundamental_differences(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A Grade 10 Mathematical Literacy teacher displays the comparison chart below contrasting a **Bar Graph** with a **Histogram**.\\n\\n"
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
    s2 = f"✓ [1 Mark: Method – Identifying discrete vs continuous conventions]\\nDiscrete categories require spaces between bars to show distinct separate entities. Continuous intervals require touching bars to show a seamless continuum."
    s3 = f"✓ [1 Mark: Accuracy – Correct graphical distinction]\\nDistinction: {ans}"

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)

    # 5. _gen_data_graph_line_graph_time_series_trend
    old_fn = re.search(r'def _gen_data_graph_line_graph_time_series_trend\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_graph_line_graph_time_series_trend(r: random.Random) -> Dict[str, Any]:
    town = r.choice(["Polokwane", "Bloemfontein", "Kimberley", "Mbombela"])
    temps = [28, 30, 31, 26, 21, 18, 17, 20, 24, 27, 29, 30] # Jan to Dec
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    min_temp = min(temps)
    min_month = months[temps.index(min_temp)]
    max_temp = max(temps)
    max_month = months[temps.index(max_temp)]

    prompt = (
        f"Refer to the monthly temperature line graph below for {town} over a 12-month calendar year:\\n\\n"
        f"• Summer peaks: Jan (28 °C), Feb (30 °C), Mar (31 °C)\\n"
        f"• Autumn decline: Apr (26 °C), May (21 °C)\\n"
        f"• Winter troughs: Jun (18 °C), Jul (17 °C), Aug (20 °C)\\n"
        f"• Spring recovery: Sep (24 °C), Oct (27 °C), Nov (29 °C), Dec (30 °C)\\n\\n"
        f"1. In which month was the lowest average temperature recorded, and what was the value?\\n"
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
    s2 = f"✓ [1 Mark: Method – Reading trough coordinate and trend trajectory]\\nTrough = {min_month} ({min_temp} °C). Trend reflects Southern Hemisphere seasonal cycle."
    s3 = f"✓ [1 Mark: Accuracy – Month, minimum temperature, and seasonal description]\\n{ans}"

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)

    # 6. _gen_data_graph_broken_axis_misleading_scale_audit
    old_fn = re.search(r'def _gen_data_graph_broken_axis_misleading_scale_audit\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_graph_broken_axis_misleading_scale_audit(r: random.Random) -> Dict[str, Any]:
    diff_cents = r.choice([10, 15, 20])
    p_a = 24.10
    p_b = round(p_a + diff_cents / 100.0, 2)
    prompt = (
        f"Refer to the petrol price bar graph below from a newspaper advertisement comparing two service stations:\\n"
        f"• Garage A: R {_fmt(p_a)} per litre\\n"
        f"• Garage B: R {_fmt(p_b)} per litre (difference of only {diff_cents} cents)\\n\\n"
        f"However, the vertical y-axis does NOT start at zero (0). Instead, the y-axis starts at **R 24,00**.\\n"
        f"As a visual result, the bar for Garage B appears disproportionately taller than the bar for Garage A!\\n\\n"
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
    s2 = f"✓ [1 Mark: Method – Identifying broken/truncated axis visual distortion]\\nStarting the scale at R 24,00 distorts true proportion."
    s3 = f"✓ [1 Mark: Accuracy – Correct statistical critique]\\nCritique: {ans}"

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)

    # 7. _gen_data_graph_frequency_polygon_midpoint_plotting
    old_fn = re.search(r'def _gen_data_graph_frequency_polygon_midpoint_plotting\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_graph_frequency_polygon_midpoint_plotting(r: random.Random) -> Dict[str, Any]:
    interval_start = r.choice([10, 20, 30, 40])
    interval_end = interval_start + 10
    midpoint = (interval_start + interval_end) / 2
    f_val = r.randint(12, 28)

    prompt = (
        f"When drawing a **Frequency Polygon** for grouped continuous data (refer to the frequency polygon below), "
        f"each data point plotted on the graph is placed at the **class interval midpoint** along the horizontal x-axis, "
        f"at a height equal to the class frequency on the vertical y-axis.\\n\\n"
        f"For the class interval **{interval_start} to {interval_end}** with a frequency of **{f_val}**:\\n"
        f"1. Calculate the class midpoint.\\n"
        f"2. State the exact coordinate (x; y) where this point must be plotted."
    )
    ans = f"Midpoint = {_fmt(midpoint)}; Coordinate = ({_fmt(midpoint)}; {f_val})"

    s1 = f"Calculate the midpoint of the interval by averaging the lower and upper class limits: ({interval_start} + {interval_end}) ÷ 2 = {_fmt(midpoint)}. Pair with frequency {f_val} as (x; y)."
    s2 = f"✓ [1 Mark: Method – Midpoint formula setup and coordinate pairing]\\nMidpoint = ({interval_start} + {interval_end}) ÷ 2 = {_fmt(midpoint)}.\\nCoordinate = (Midpoint; Frequency) = ({_fmt(midpoint)}; {f_val})."
    s3 = f"✓ [1 Mark: Accuracy – Midpoint and (x; y) coordinate]\\n{ans}."

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)

    # 8. _gen_data_graph_percentage_increase_between_bars
    old_fn = re.search(r'def _gen_data_graph_percentage_increase_between_bars\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_graph_percentage_increase_between_bars(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    v1 = r.choice([200, 250, 400, 500])
    v2 = v1 + r.choice([50, 75, 100, 150])
    diff = v2 - v1
    pct_increase = round((diff / v1) * 100, 1)

    prompt = (
        f"Refer to the municipal health department bar graph below showing childhood immunizations administered:\\n"
        f"• May: {v1} children\\n"
        f"• June: {v2} children\\n\\n"
        f"Formula: Percentage Increase = [(New Value − Old Value) ÷ Old Value] × 100%\\n\\n"
        f"Calculate the percentage increase in immunizations from May to June (rounded to 1 decimal place)."
    )
    ans = f"{_fmt(pct_increase)}%"

    s1 = f"Subtract old value ({v1}) from new value ({v2}) to find absolute increase ({diff}), divide by original value ({v1}), and multiply by 100."
    s2 = f"✓ [1 Mark: Method – Percentage change formula substitution]\\nPercentage Increase = [({v2} − {v1}) ÷ {v1}] × 100% = ({diff} ÷ {v1}) × 100%."
    s3 = f"✓ [1 Mark: Accuracy – Final percentage increase]\\nIncrease = {_fmt(pct_increase)}%."

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)
    open(p, "w", encoding="utf-8").write(c)
    print("remediated bar_graphs_histograms.py")

def remediate_pie_charts():
    p = os.path.join(DH_BASE, "pie_charts_interpretation.py")
    c = open(p, encoding="utf-8").read()

    # 1. _gen_data_pie_total_dataset_from_sector_value
    old_fn = re.search(r'def _gen_data_pie_total_dataset_from_sector_value\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_pie_total_dataset_from_sector_value(r: random.Random) -> Dict[str, Any]:
    pct = r.choice([20, 25, 40, 50])
    sector_value = r.choice([150, 240, 350, 500, 600])
    grand_total = round((sector_value / pct) * 100)

    prompt = (
        f"Refer to the refuse collection pie chart below. The slice representing "
        f"'Households with weekly municipal curbside collection' accounts for **{pct}%** of the chart, "
        f"which corresponds to exactly **{sector_value} households**.\\n\\n"
        f"Calculate the **total number of households** surveyed in the entire municipality."
    )
    ans = f"{grand_total} households"

    s1 = f"Use reverse percentage calculation: Total = Sector Value ÷ (Percentage ÷ 100) = {sector_value} ÷ ({pct} ÷ 100) = {sector_value} ÷ {_fmt(pct / 100)}."
    s2 = f"✓ [1 Mark: Method – Reverse percentage setup]\\nTotal = ({sector_value} ÷ {pct}) × 100."
    s3 = f"✓ [1 Mark: Accuracy – Total population count]\\nTotal = {grand_total} households."

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)

    # 2. _gen_data_misleading_pie_chart_3d_perspective
    old_fn = re.search(r'def _gen_data_misleading_pie_chart_3d_perspective\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_misleading_pie_chart_3d_perspective(r: random.Random) -> Dict[str, Any]:
    share_x = r.choice([30, 35, 38])
    share_y = r.choice([42, 45, 48])
    share_z = 100 - share_x - share_y

    prompt = (
        f"Refer to the 3D perspective pie chart below displaying market share between competing brands:\\n"
        f"• Brand X (foreground/front slice): {share_x}% of the market\\n"
        f"• Brand Y (background/rear slice): {share_y}% of the market\\n\\n"
        f"Because the pie chart is tilted horizontally at a sharp 3D perspective angle towards the viewer, "
        f"the {share_x}% slice in front appears visually larger on the page than the {share_y}% slice in the back!\\n\\n"
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
    s2 = f"✓ [1 Mark: Method – Identifying perspective distortion in data graphics]\\nPerspective foreshortening enlarges front angles and compresses rear angles, misleading the reader."
    s3 = f"✓ [1 Mark: Accuracy – Correct statistical critique]\\nCritique: {ans}"

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)

    # 3. _gen_data_stats_sa_census_demographics_interpretation
    old_fn = re.search(r'def _gen_data_stats_sa_census_demographics_interpretation\(.*?\n\n', c, re.S).group(0)
    new_fn = '''def _gen_data_stats_sa_census_demographics_interpretation(r: random.Random) -> Dict[str, Any]:
    prov = r.choice(SA_PROVINCES)
    piped_water_pct = r.choice([72.4, 78.5, 84.2, 89.6])
    borehole_pct = r.choice([8.5, 11.2, 14.0])
    rain_tank_pct = r.choice([4.2, 6.5, 7.8])
    other_pct = round(100.0 - piped_water_pct - borehole_pct - rain_tank_pct, 1)

    prompt = (
        f"Refer to the Stats SA census demographics bar chart below for household drinking water in {prov}:\\n\\n"
        f"• Piped tap water: {_fmt(piped_water_pct)}%\\n"
        f"• Communal borehole: {_fmt(borehole_pct)}%\\n"
        f"• Rainwater harvesting tank: {_fmt(rain_tank_pct)}%\\n"
        f"• Other: {_fmt(other_pct)}%\\n\\n"
        f"1. What is the most prevalent (modal) water source in {prov}?\\n"
        f"2. If {prov} has a total of 1 500 000 households, calculate the exact number of households "
        f"relying primarily on **rainwater harvesting tanks**."
    )
    rain_households = round((rain_tank_pct / 100.0) * 1_500_000)
    ans = f"Modal source = Piped tap water ({_fmt(piped_water_pct)}%); Rainwater households = {_fmt(rain_households)}"

    s1 = f"Identify the highest percentage ({_fmt(piped_water_pct)}% = Piped tap water). Calculate rainwater households: ({_fmt(rain_tank_pct)} ÷ 100) × 1 500 000."
    s2 = f"✓ [1 Mark: Method – Identifying mode and percentage calculation]\\nModal = Piped tap water ({_fmt(piped_water_pct)}%).\\nRainwater = ({_fmt(rain_tank_pct)} ÷ 100) × 1 500 000."
    s3 = f"✓ [1 Mark: Accuracy – Modal category and household calculation]\\n{ans}."

    diagram_spec = {
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

'''
    c = c.replace(old_fn, new_fn)
    open(p, "w", encoding="utf-8").write(c)
    print("remediated pie_charts_interpretation.py")

remediate_bar_graphs()
remediate_pie_charts()
