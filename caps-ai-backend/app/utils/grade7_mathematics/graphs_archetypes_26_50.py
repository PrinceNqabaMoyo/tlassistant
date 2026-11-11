"""Grade 7 Mathematics - Graphs: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 1/04. Graphs.md
"""
import random
import math
from typing import Dict, Any, List


def _svg_graph(
    x_label: str,
    y_label: str,
    path_d: str,
    points: List[tuple] = None,
    x_ticks: List[tuple] = None,
    y_ticks: List[tuple] = None,
    width: int = 440,
    height: int = 260,
    extra_svg: str = ""
) -> str:
    origin_x, origin_y = 60, 200
    w_plot, h_plot = 340, 160
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px;">',
        f'<defs><marker id="ar2" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">'
        f'<path d="M0,0 L0,6 L6,3 z" fill="#1e293b"/></marker></defs>',
        f'<line x1="{origin_x}" y1="{origin_y - h_plot}" x2="{origin_x + w_plot}" y2="{origin_y - h_plot}" stroke="#e2e8f0" stroke-width="1"/>',
        f'<line x1="{origin_x}" y1="{origin_y - h_plot//2}" x2="{origin_x + w_plot}" y2="{origin_y - h_plot//2}" stroke="#e2e8f0" stroke-width="1"/>',
        f'<line x1="{origin_x}" y1="{origin_y}" x2="{origin_x + w_plot + 15}" y2="{origin_y}" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar2)"/>',
        f'<line x1="{origin_x}" y1="{origin_y}" x2="{origin_x}" y2="{origin_y - h_plot - 15}" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar2)"/>',
        f'<text x="{origin_x + w_plot//2}" y="{origin_y + 40}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">{x_label}</text>',
        f'<text x="20" y="{origin_y - h_plot//2}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" transform="rotate(-90 20 {origin_y - h_plot//2})" text-anchor="middle">{y_label}</text>',
    ]
    
    if x_ticks:
        for x_val, label in x_ticks:
            svg_parts.append(f'<line x1="{x_val}" y1="{origin_y}" x2="{x_val}" y2="{origin_y + 5}" stroke="#1e293b" stroke-width="1.5"/>')
            svg_parts.append(f'<text x="{x_val}" y="{origin_y + 18}" font-family="sans-serif" font-size="10" fill="#475569" text-anchor="middle">{label}</text>')

    if y_ticks:
        for y_val, label in y_ticks:
            svg_parts.append(f'<line x1="{origin_x - 5}" y1="{y_val}" x2="{origin_x}" y2="{y_val}" stroke="#1e293b" stroke-width="1.5"/>')
            svg_parts.append(f'<text x="{origin_x - 10}" y="{y_val + 4}" font-family="sans-serif" font-size="10" fill="#475569" text-anchor="end">{label}</text>')

    if path_d:
        svg_parts.append(f'<path d="{path_d}" fill="none" stroke="#2563eb" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')

    if points:
        for px, py in points:
            svg_parts.append(f'<circle cx="{px}" cy="{py}" r="4" fill="#dc2626"/>')

    if extra_svg:
        svg_parts.append(extra_svg)

    svg_parts.append('</svg>')
    return "".join(svg_parts)


# 26. Temperature graph daily fluctuation max min
def arch_26_temperature_graph_daily_fluctuation_max_min(rng: random.Random) -> Dict[str, Any]:
    t_min = rng.choice([10, 12, 14])
    t_max = rng.choice([26, 28, 30])
    diff = t_max - t_min
    prompt = (
        f"A weather station recorded a city's temperatures throughout a 24-hour period. "
        f"The minimum temperature recorded was {t_min}°C at 05:00 and the maximum was {t_max}°C at 14:00.\n\n"
        f"1. What is the temperature range (difference between maximum and minimum) for the day?\n"
        f"2. Between 05:00 and 14:00, was the temperature increasing or decreasing?"
    )
    sol = (
        f"**Step 1:** $\\text{{Temperature Range}} = \\text{{Maximum}} - \\text{{Minimum}} = {t_max}^\\circ\\text{{C}} - {t_min}^\\circ\\text{{C}} = {diff}^\\circ\\text{{C}}$.\n\n"
        f"**Step 2:** From 05:00 ({t_min}°C) to 14:00 ({t_max}°C), the temperature was **increasing**."
    )
    ans = f"1. {diff}°C; 2. Increasing"
    return {
        "id": f"g7_graph_26_{rng.randint(100000, 999999)}",
        "subskill": "26_temperature_graph_daily_fluctuation_max_min",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_26",
        "hints": {
            "tier_1": f"Subtract {t_min} from {t_max}.",
            "tier_2": "The temperature rose from 05:00 to 14:00.",
            "tier_3": ans
        },
        "misconception_tags": ["temperature_range_calculation_error"]
    }


# 27. Temperature graph rate of cooling heating
def arch_27_temperature_graph_rate_of_cooling_heating(rng: random.Random) -> Dict[str, Any]:
    t_start = rng.choice([84, 90, 96])
    t_end = 30
    duration_hrs = 3
    rate = (t_start - t_end) // duration_hrs
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Temperature (°C)",
        path_d="M 60 60 L 360 170",
        x_ticks=[(60, "0"), (360, f"{duration_hrs}")],
        y_ticks=[(170, f"{t_end}"), (60, f"{t_start}")]
    )
    prompt = (
        f"A pot of hot soup at {t_start}°C cools down steadily to {t_end}°C over {duration_hrs} hours.\n\n"
        f"1. What is the average rate of cooling in °C per hour?\n"
        f"2. What is the sign of the gradient on this cooling temperature graph?"
    )
    sol = (
        f"**Step 1:** $\\text{{Rate of Cooling}} = \\frac{{{t_start} - {t_end}}}{{{duration_hrs}}} = \\frac{{{t_start - t_end}}}{{{duration_hrs}}} = {rate}^\\circ\\text{{C/hour}}$.\n\n"
        f"**Step 2:** Because temperature decreases over time, the gradient is **negative** (downward slope)."
    )
    ans = f"1. {rate}°C/hour; 2. Negative"
    return {
        "id": f"g7_graph_27_{rng.randint(100000, 999999)}",
        "subskill": "27_temperature_graph_rate_of_cooling_heating",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_27",
        "hints": {
            "tier_1": f"Subtract: {t_start} - {t_end} = {t_start - t_end}, then divide by {duration_hrs}.",
            "tier_2": "Downward sloping lines have negative gradients.",
            "tier_3": ans
        },
        "misconception_tags": ["negative_gradient_sign_confusion"]
    }


# 28. Comparing two runners same axes who won
def arch_28_comparing_two_runners_same_axes_who_won(rng: random.Random) -> Dict[str, Any]:
    t_a = rng.choice([20, 25])
    t_b = t_a + 5
    extra = (
        f'<line x1="60" y1="200" x2="260" y2="60" stroke="#2563eb" stroke-width="3"/>'
        f'<line x1="60" y1="200" x2="360" y2="60" stroke="#dc2626" stroke-width="3" stroke-dasharray="4,4"/>'
        f'<text x="270" y="65" font-family="sans-serif" font-size="12" font-weight="bold" fill="#2563eb">Runner A</text>'
        f'<text x="370" y="65" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">Runner B</text>'
    )
    svg = _svg_graph(
        x_label="Time (minutes)",
        y_label="Distance (km)",
        path_d="",
        x_ticks=[(60, "0"), (260, f"{t_a}"), (360, f"{t_b}")],
        y_ticks=[(200, "0"), (60, "5")],
        extra_svg=extra
    )
    prompt = (
        f"Two athletes compete in a 5 km race. Runner A (blue solid line) finishes in {t_a} minutes. "
        f"Runner B (red dashed line) finishes in {t_b} minutes.\n\n"
        f"1. Which runner won the race?\n"
        f"2. How does the graph visually indicate which runner had the greater speed?"
    )
    sol = (
        f"**Step 1:** **Runner A** won because Runner A reached the 5 km mark in less time ({t_a} min vs {t_b} min).\n\n"
        f"**Step 2:** Runner A's line has a **steeper slope (gradient)**, which signifies a higher speed."
    )
    ans = "1. Runner A; 2. Runner A's line is steeper (greater gradient)."
    return {
        "id": f"g7_graph_28_{rng.randint(100000, 999999)}",
        "subskill": "28_comparing_two_runners_same_axes_who_won",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Check Finish Times", "body": f"Runner A took {t_a} min, Runner B took {t_b} min."},
                {"title": "Winner", "body": "Runner A finished in less time."},
                {"title": "Steepness", "body": "Runner A's steeper line indicates higher speed."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_28",
        "hints": {
            "tier_1": "Who reached 5 km first (at a lower time value)?",
            "tier_2": "Steeper slope = faster runner.",
            "tier_3": ans
        },
        "misconception_tags": ["higher_time_confused_with_winning"]
    }


# 29. Comparing two runners point of overtaking
def arch_29_comparing_two_runners_point_of_overtaking(rng: random.Random) -> Dict[str, Any]:
    inter_time = rng.choice([15, 20])
    inter_dist = rng.choice([3, 4])
    extra = (
        f'<line x1="60" y1="170" x2="360" y2="80" stroke="#dc2626" stroke-width="2.5"/>' # Slow head start
        f'<line x1="60" y1="200" x2="360" y2="50" stroke="#2563eb" stroke-width="2.5"/>' # Fast catch up
        f'<circle cx="210" cy="125" r="5" fill="#059669"/>'
        f'<text x="220" y="120" font-family="sans-serif" font-size="12" font-weight="bold" fill="#059669">Intersection</text>'
    )
    svg = _svg_graph(
        x_label="Time (minutes)",
        y_label="Distance (km)",
        path_d="",
        x_ticks=[(60, "0"), (210, f"{inter_time}"), (360, "30")],
        y_ticks=[(200, "0"), (125, f"{inter_dist}"), (50, "6")],
        extra_svg=extra
    )
    prompt = (
        "Two runners A and B run along the same trail. Their distance graphs cross at the green dot shown.\n\n"
        "1. What is the physical significance of the intersection point of the two graphs?\n"
        "2. At what time and distance does the overtaking occur?"
    )
    sol = (
        f"**Step 1:** The intersection point is where both runners are at the **exact same position at the exact same time** (Runner A overtakes Runner B).\n\n"
        f"**Step 2:** Reading coordinates: at **{inter_time} minutes** and **{inter_dist} km**."
    )
    ans = f"1. Both runners are at the same position at the same time (overtaking); 2. At {inter_time} minutes, {inter_dist} km."
    return {
        "id": f"g7_graph_29_{rng.randint(100000, 999999)}",
        "subskill": "29_comparing_two_runners_point_of_overtaking",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Intersection Point", "body": "Where lines cross, coordinates (x, y) are identical."},
                {"title": "Read Values", "body": f"Time = {inter_time} min, Distance = {inter_dist} km."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_29",
        "hints": {
            "tier_1": "Crossing lines mean equal distance and time.",
            "tier_2": f"Read x = {inter_time} min and y = {inter_dist} km.",
            "tier_3": ans
        },
        "misconception_tags": ["intersection_point_interpretation_error"]
    }


# 30. Comparing two runners head start delay
def arch_30_comparing_two_runners_head_start_delay(rng: random.Random) -> Dict[str, Any]:
    head_start_m = rng.choice([5, 10, 15])
    prompt = (
        f"In a handicap race, Runner 1 starts at t = 0 from the start line. "
        f"Runner 2 starts {head_start_m} minutes later from the same start line.\n\n"
        f"1. On a distance-time graph, at what coordinate (time, distance) does Runner 2's line begin on the time axis?\n"
        f"2. Explain why Runner 2's line does not pass through the origin (0, 0)."
    )
    sol = (
        f"**Step 1:** Runner 2 begins at coordinate **({head_start_m}, 0)** on the horizontal time axis.\n\n"
        f"**Step 2:** Because Runner 2 did not begin running until {head_start_m} minutes had elapsed, distance was zero for $t < {head_start_m}$."
    )
    ans = f"1. ({head_start_m}, 0); 2. Runner 2 delayed start by {head_start_m} minutes, so distance begins increasing only after {head_start_m} min."
    return {
        "id": f"g7_graph_30_{rng.randint(100000, 999999)}",
        "subskill": "30_comparing_two_runners_head_start_delay",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_30",
        "hints": {
            "tier_1": "At the start of Runner 2's run, what is time? What is distance?",
            "tier_2": f"Time is {head_start_m}, distance is 0.",
            "tier_3": ans
        },
        "misconception_tags": ["head_start_axis_placement_error"]
    }


# 31. Savings accumulation linear graph
def arch_31_savings_accumulation_linear_graph(rng: random.Random) -> Dict[str, Any]:
    initial = rng.choice([50, 100])
    weekly = rng.choice([20, 30, 40])
    weeks = 5
    total = initial + weeks * weekly
    prompt = (
        f"Lindiwe has R{initial} in her piggy bank. She saves an additional R{weekly} each week.\n\n"
        f"1. Write down a linear formula for total savings $S$ in terms of number of weeks $w$.\n"
        f"2. What is the vertical intercept (starting value on the vertical axis)?\n"
        f"3. Calculate her total savings after {weeks} weeks."
    )
    sol = (
        f"**Step 1:** Formula: $$S = {weekly}w + {initial}$$\n\n"
        f"**Step 2:** Vertical intercept is **R{initial}** (savings when $w = 0$).\n\n"
        f"**Step 3:** After {weeks} weeks: $$S = {weekly}({weeks}) + {initial} = {weekly * weeks} + {initial} = \\text{{R}}{total}$$."
    )
    ans = f"1. S = {weekly}w + {initial}; 2. R{initial}; 3. R{total}"
    return {
        "id": f"g7_graph_31_{rng.randint(100000, 999999)}",
        "subskill": "31_savings_accumulation_linear_graph",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_graphs_31",
        "hints": {
            "tier_1": f"Multiply {weekly} by number of weeks and add {initial}.",
            "tier_2": f"{weekly} * {weeks} + {initial}.",
            "tier_3": ans
        },
        "misconception_tags": ["omitted_initial_savings_intercept"]
    }


# 32. Cellphone plan cost vs minutes graph
def arch_32_cellphone_plan_cost_vs_minutes_graph(rng: random.Random) -> Dict[str, Any]:
    fixed_fee = rng.choice([50, 75, 100, 120])
    cost_per_min = 2
    total = fixed_fee + 60 * cost_per_min
    svg = _svg_graph(
        x_label="Call Minutes",
        y_label="Monthly Cost (R)",
        path_d="M 60 150 L 360 60",
        x_ticks=[(60, "0"), (360, "60")],
        y_ticks=[(200, "0"), (150, f"{fixed_fee}"), (60, f"{total}")]
    )
    prompt = (
        f"A prepaid cellphone contract charges a fixed monthly line rental of R{fixed_fee} plus R{cost_per_min} per minute of calls.\n\n"
        f"1. On a graph of Monthly Cost versus Call Minutes, does the graph start at (0, 0) or (0, {fixed_fee})?\n"
        f"2. What is the gradient (slope) of this cost graph?\n"
        f"3. Calculate the bill for 60 call minutes."
    )
    sol = (
        f"**Step 1:** The graph starts at **(0, {fixed_fee})** because the customer pays the fixed R{fixed_fee} fee even with 0 minutes called.\n\n"
        f"**Step 2:** The gradient is **{cost_per_min}** (representing the rate of R{cost_per_min} per minute).\n\n"
        f"**Step 3:** Total cost = ${fixed_fee} + 60 \\times {cost_per_min} = {fixed_fee} + 120 = \\text{{R}}{total}$."
    )
    ans = f"1. (0, {fixed_fee}); 2. 2 (or R2/min); 3. R{total}"
    return {
        "id": f"g7_graph_32_{rng.randint(100000, 999999)}",
        "subskill": "32_cellphone_plan_cost_vs_minutes_graph",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_graphs_32",
        "hints": {
            "tier_1": "Fixed cost is the y-intercept.",
            "tier_2": f"Bill = {fixed_fee} + 60 * 2.",
            "tier_3": ans
        },
        "misconception_tags": ["forgot_fixed_rental_fee"]
    }


# 33. Plant growth over weeks table to graph
def arch_33_plant_growth_over_weeks_table_to_graph(rng: random.Random) -> Dict[str, Any]:
    # Week 1: 3, Week 2: 6, Week 3: 9, Week 4: 12
    prompt = (
        "A bean seedling is measured every week:\n"
        "Week 1: 3 cm\n"
        "Week 2: 6 cm\n"
        "Week 3: 9 cm\n"
        "Week 4: 12 cm\n\n"
        "1. Is the growth rate constant? Support your answer with calculations.\n"
        "2. Predict the height of the seedling at Week 6 if this trend continues."
    )
    sol = (
        "**Step 1:** Yes, growth rate is **constant**:\n"
        "- Week 1 to 2: $6 - 3 = 3\\text{ cm}$\n"
        "- Week 2 to 3: $9 - 6 = 3\\text{ cm}$\n"
        "- Week 3 to 4: $12 - 9 = 3\\text{ cm}$\n"
        "The constant difference is $3\\text{ cm/week}$.\n\n"
        "**Step 2:** At Week 6: $6 \\times 3\\text{ cm} = \\mathbf{18\\text{ cm}}$."
    )
    ans = "1. Yes, constant rate of 3 cm per week; 2. 18 cm"
    return {
        "id": f"g7_graph_33_{rng.randint(100000, 999999)}",
        "subskill": "33_plant_growth_over_weeks_table_to_graph",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_33",
        "hints": {
            "tier_1": "Find the difference between each week.",
            "tier_2": "Add 3 cm for Week 5 (15 cm) and Week 6 (18 cm).",
            "tier_3": ans
        },
        "misconception_tags": ["non_constant_growth_prediction_error"]
    }


# 34. Speed time graph acceleration and braking
def arch_34_speed_time_graph_acceleration_and_braking(rng: random.Random) -> Dict[str, Any]:
    v_c = rng.choice([16, 20, 24, 30])
    svg = _svg_graph(
        x_label="Time (seconds)",
        y_label="Speed (m/s)",
        path_d="M 60 200 L 160 80 L 280 80 L 360 200",
        x_ticks=[(60, "0"), (160, "10"), (280, "30"), (360, "40")],
        y_ticks=[(200, "0"), (140, f"{v_c//2}"), (80, f"{v_c}")]
    )
    prompt = (
        "The speed-time graph illustrates a train accelerating from rest, cruising, and braking to a stop.\n\n"
        "1. Identify the time interval during which the train was accelerating (speed increasing).\n"
        "2. Identify the time interval during which the train was braking (speed decreasing).\n"
        "3. What was the cruising speed of the train in m/s?"
    )
    sol = (
        f"**Step 1:** Accelerating: from **0 to 10 seconds** (speed increases from 0 to {v_c} m/s).\n\n"
        f"**Step 2:** Braking: from **30 to 40 seconds** (speed decreases from {v_c} m/s to 0).\n\n"
        f"**Step 3:** Cruising speed = **{v_c} m/s**."
    )
    ans = f"1. 0 to 10 s; 2. 30 to 40 s; 3. {v_c} m/s"
    return {
        "id": f"g7_graph_34_{rng.randint(100000, 999999)}",
        "subskill": "34_speed_time_graph_acceleration_and_braking",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Acceleration", "body": f"Speed rises from 0 to {v_c} m/s in first 10 s."},
                {"title": "Cruise", "body": f"Constant speed {v_c} m/s from 10 to 30 s."},
                {"title": "Braking", "body": "Speed drops to 0 from 30 to 40 s."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_graphs_34",
        "hints": {
            "tier_1": "Look at rising slope for acceleration and falling slope for braking.",
            "tier_2": f"Cruising speed is the flat top value ({v_c} m/s).",
            "tier_3": ans
        },
        "misconception_tags": ["speed_time_graph_confused_with_distance_time"]
    }


# 35. Speed time graph constant speed cruise
def arch_35_speed_time_graph_constant_speed_cruise(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "On a speed-time graph, a horizontal straight line at y = 60 km/h is observed between t = 1 hour and t = 3 hours.\n\n"
        "1. Does this horizontal line mean the vehicle is stopped (stationary) or moving at a constant speed?\n"
        "2. Explain the crucial difference between a horizontal line on a distance-time graph vs a speed-time graph."
    )
    sol = (
        "**Step 1:** It means the vehicle is **moving at a constant speed of 60 km/h** (it is NOT stationary!).\n\n"
        "**Step 2:**\n"
        "- On a **distance-time graph**, a horizontal line means distance is not changing $\\rightarrow$ the vehicle is **stationary**.\n"
        "- On a **speed-time graph**, a horizontal line means speed is not changing $\\rightarrow$ the vehicle is **moving at a constant speed**."
    )
    ans = "1. Moving at a constant speed of 60 km/h; 2. Distance-time horizontal = stationary; Speed-time horizontal = moving at constant speed."
    return {
        "id": f"g7_graph_35_{rng.randint(100000, 999999)}",
        "subskill": "35_speed_time_graph_constant_speed_cruise",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_35",
        "hints": {
            "tier_1": "Look at what is on the vertical axis: is it Distance or Speed?",
            "tier_2": "Speed = 60 means moving at 60 km/h, not standing still.",
            "tier_3": ans
        },
        "misconception_tags": ["assumed_horizontal_speed_means_stopped"]
    }


# 36. Matching story to correct graph option
def arch_36_matching_story_to_correct_graph_option(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Read this story: 'Sipho walked at a steady pace to the library, stayed there studying for 1 hour, "
        "and then jogged back home at twice his walking speed.'\n\n"
        "Which of the following graphical descriptions accurately matches Sipho's distance-from-home graph?\n"
        "A) A curved line upwards, a dip to zero, then a horizontal line.\n"
        "B) A straight upward sloping line, a horizontal flat line, and then a steeper straight downward sloping line to zero.\n"
        "C) A straight horizontal line, an upward sloping line, and a downward line of equal steepness."
    )
    sol = (
        "**Step 1:** Walking steadily $\\rightarrow$ straight upward line with moderate slope.\n"
        "**Step 2:** Staying at library for 1 hour $\\rightarrow$ flat horizontal line.\n"
        "**Step 3:** Jogging home at twice speed $\\rightarrow$ steeper straight downward line back to 0 distance.\n\n"
        "**Conclusion:** **Option B** is the correct description."
    )
    ans = "Option B"
    return {
        "id": f"g7_graph_36_{rng.randint(100000, 999999)}",
        "subskill": "36_matching_story_to_correct_graph_option",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_36",
        "hints": {
            "tier_1": "Look for upward line -> flat line -> steeper downward line.",
            "tier_2": "Jogging is faster than walking, so return leg is steeper.",
            "tier_3": "Option B."
        },
        "misconception_tags": ["story_graph_matching_error"]
    }


# 37. Drawing inferences from flattening curve
def arch_37_drawing_inferences_from_flattening_curve(rng: random.Random) -> Dict[str, Any]:
    max_h = rng.choice([180, 200, 220, 240])
    svg = _svg_graph(
        x_label="Time (weeks)",
        y_label="Sunflower Height (cm)",
        path_d="M 60 190 Q 180 60 280 60 L 360 60",
        x_ticks=[(60, "0"), (280, "12"), (360, "16")],
        y_ticks=[(200, "0"), (60, f"{max_h}")]
    )
    prompt = (
        f"The line graph above illustrates the height of a sunflower (reaching {max_h} cm) over 16 weeks. The height increases rapidly during weeks 2 to 10, "
        "and then the curve completely levels off horizontally from week 12 to 16.\n\n"
        "What biological inference can you draw from the horizontal leveling off of the graph?"
    )
    sol = (
        "**Answer:** The sunflower has reached its maximum mature height and has stopped growing taller."
    )
    ans = "The sunflower has reached full maturity and has stopped growing."
    return {
        "id": f"g7_graph_37_{rng.randint(100000, 999999)}",
        "subskill": "37_drawing_inferences_from_flattening_curve",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_37",
        "hints": {
            "tier_1": "If height stops increasing, what does that mean for a plant?",
            "tier_2": "Growth has ended / full maturity reached.",
            "tier_3": ans
        },
        "misconception_tags": ["plant_growth_plateau_confusion"]
    }


# 38. Identifying intercepts starting value
def arch_38_identifying_intercepts_starting_value(rng: random.Random) -> Dict[str, Any]:
    init_val = rng.choice([15, 20, 25, 30])
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Temperature (°C)",
        path_d="M 60 140 L 360 50",
        points=[(60, 140)],
        x_ticks=[(60, "0"), (160, "2"), (260, "4"), (360, "6")],
        y_ticks=[(200, "0"), (140, f"{init_val}"), (50, "40")]
    )
    prompt = (
        f"A scientific experiment starts recording at t = 0.\n\n"
        f"1. What is the mathematical term for the point where a graph crosses the vertical axis?\n"
        f"2. What was the initial starting temperature at t = 0?"
    )
    sol = (
        f"**Step 1:** The point where a graph cuts the vertical axis is the **y-intercept** (or vertical intercept).\n\n"
        f"**Step 2:** At $t = 0$, the temperature is **{init_val}°C**."
    )
    ans = f"1. y-intercept (or vertical intercept); 2. {init_val}°C"
    return {
        "id": f"g7_graph_38_{rng.randint(100000, 999999)}",
        "subskill": "38_identifying_intercepts_starting_value",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Vertical Axis", "body": "Where x = 0, y is the vertical intercept."},
                {"title": "Read Value", "body": f"The starting value is {init_val}°C."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_38",
        "hints": {
            "tier_1": "Look at where the line touches the vertical y-axis.",
            "tier_2": f"The value is {init_val}°C.",
            "tier_3": ans
        },
        "misconception_tags": ["confused_x_and_y_intercepts"]
    }


# 39. Identifying intercepts finishing value
def arch_39_identifying_intercepts_finishing_value(rng: random.Random) -> Dict[str, Any]:
    duration = rng.choice([40, 50, 60, 70])
    svg = _svg_graph(
        x_label="Distance Driven (10s of km)",
        y_label="Fuel Remaining (L)",
        path_d="M 60 60 L 360 200",
        points=[(360, 200)],
        x_ticks=[(60, "0"), (360, f"{duration}")],
        y_ticks=[(200, "0"), (60, "60")]
    )
    prompt = (
        f"A vehicle's fuel tank drains until the fuel level reaches zero after exactly {duration} units of driving.\n\n"
        f"1. What is the mathematical term for the point where a graph crosses the horizontal axis?\n"
        f"2. What is the coordinate of this point if fuel remaining is on the y-axis and distance is on the x-axis?"
    )
    sol = (
        f"**Step 1:** The point where a graph cuts the horizontal axis is called the **x-intercept** (or horizontal intercept).\n\n"
        f"**Step 2:** The coordinate is **({duration}, 0)**."
    )
    ans = f"1. x-intercept (or horizontal intercept); 2. ({duration}, 0)"
    return {
        "id": f"g7_graph_39_{rng.randint(100000, 999999)}",
        "subskill": "39_identifying_intercepts_finishing_value",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_39",
        "hints": {
            "tier_1": "Crossing the horizontal axis is the x-intercept.",
            "tier_2": f"Coordinates are always (x, y): ({duration}, 0).",
            "tier_3": ans
        },
        "misconception_tags": ["swapped_intercept_coordinates"]
    }


# 40. Travel graph lunch break duration
def arch_40_travel_graph_lunch_break_duration(rng: random.Random) -> Dict[str, Any]:
    t1 = rng.choice(["12:00", "12:30"])
    t2 = "13:30"
    dur_min = 90 if t1 == "12:00" else 60
    prompt = (
        f"On a school excursion travel graph, the bus stops at a rest area from {t1} to {t2}.\n\n"
        f"1. How long was the lunch break in minutes?\n"
        f"2. What was the bus's speed during the lunch break?"
    )
    sol = (
        f"**Step 1:** From {t1} to {t2} is **{dur_min} minutes**.\n\n"
        f"**Step 2:** The speed was **0 km/h** because the bus was parked."
    )
    ans = f"1. {dur_min} minutes; 2. 0 km/h"
    return {
        "id": f"g7_graph_40_{rng.randint(100000, 999999)}",
        "subskill": "40_travel_graph_lunch_break_duration",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_40",
        "hints": {
            "tier_1": f"Calculate the time difference between {t1} and {t2}.",
            "tier_2": "When parked, speed is 0.",
            "tier_3": ans
        },
        "misconception_tags": ["time_subtraction_error_clock"]
    }


# 41. Linear vs nonlinear graph identification
def arch_41_linear_vs_nonlinear_graph_identification(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "1. What is the fundamental visual difference between a **linear** graph and a **non-linear** graph?\n"
        "2. Does a linear graph represent a constant rate of change or a changing rate of change?"
    )
    sol = (
        "**Step 1:** A **linear graph** is a straight line, while a **non-linear graph** is curved or bent.\n\n"
        "**Step 2:** A linear graph represents a **constant rate of change**."
    )
    ans = "1. Linear is a straight line, non-linear is curved; 2. Constant rate of change"
    return {
        "id": f"g7_graph_41_{rng.randint(100000, 999999)}",
        "subskill": "41_linear_vs_nonlinear_graph_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_41",
        "hints": {
            "tier_1": "Linear comes from the word 'line'.",
            "tier_2": "Straight line = linear = constant rate.",
            "tier_3": ans
        },
        "misconception_tags": ["linear_definition_confusion"]
    }


# 42. Interpreting negative slope in practical context
def arch_42_interpreting_negative_slope_in_practical_context(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A car's petrol tank level decreases as distance driven increases.\n\n"
        "1. What type of slope (positive, negative, or zero) does this relationship have on a graph?\n"
        "2. Explain what a negative slope indicates in everyday terms."
    )
    sol = (
        "**Step 1:** The relationship has a **negative slope**.\n\n"
        "**Step 2:** A negative slope indicates that as one quantity increases (distance driven), the other quantity **decreases** (petrol remaining)."
    )
    ans = "1. Negative slope; 2. As the independent variable increases, the dependent variable decreases."
    return {
        "id": f"g7_graph_42_{rng.randint(100000, 999999)}",
        "subskill": "42_interpreting_negative_slope_in_practical_context",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_42",
        "hints": {
            "tier_1": "Does petrol go up or down when driving?",
            "tier_2": "Going down from left to right is negative slope.",
            "tier_3": ans
        },
        "misconception_tags": ["negative_slope_practical_inversion"]
    }


# 43. Spot the error misreading axes scale
def arch_43_spot_the_error_misreading_axes_scale(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "On a distance-time graph, the vertical axis has tick marks at intervals of 20 km (0, 20, 40, 60, 80). "
        "A point is plotted exactly halfway between the 40 and 60 tick marks. "
        "A learner writes down that the distance is 45 km.\n\n"
        "1. What error did the learner make?\n"
        "2. What is the correct distance value at this point?"
    )
    sol = (
        "**Step 1:** The learner incorrectly assumed each tick interval represented 10 km instead of 20 km (halfway between 40 and 60 is not 45).\n\n"
        "**Step 2:** Halfway between 40 and 60 is: $$\\frac{40 + 60}{2} = \\mathbf{50\\text{ km}}$$"
    )
    ans = "1. The learner miscalculated the midpoint of a 20-unit interval; 2. 50 km"
    return {
        "id": f"g7_graph_43_{rng.randint(100000, 999999)}",
        "subskill": "43_spot_the_error_misreading_axes_scale",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_43",
        "hints": {
            "tier_1": "What number is exactly halfway between 40 and 60?",
            "tier_2": "(40 + 60) / 2 = 50.",
            "tier_3": ans
        },
        "misconception_tags": ["scale_midpoint_misreading"]
    }


# 44. Spot the error confusing steepness with height
def arch_44_spot_the_error_confusing_steepness_with_height(rng: random.Random) -> Dict[str, Any]:
    d_max = rng.choice([80, 100, 120, 150])
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Distance (km)",
        path_d="M 60 200 L 180 60 L 320 60",
        points=[(250, 60)],
        x_ticks=[(60, "0"), (180, "2"), (320, "4")],
        y_ticks=[(200, "0"), (60, f"{d_max}")],
        extra_svg='<text x="250" y="50" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">B</text>'
    )
    prompt = (
        f"A learner looks at the distance-time graph (peak {d_max} km) and says: 'At point B, the graph is at its highest position on the page, "
        "so the car must be traveling at its fastest speed at point B.'\n\n"
        "Explain why this statement is a misconception in interpreting distance-time graphs."
    )
    sol = (
        "**Answer:** Being at the highest position indicates the **maximum distance covered**, not the maximum speed. "
        "Speed is determined by the **steepness (gradient)** of the line, not by its height on the page. "
        "A line can be very high up on the graph while being completely flat (meaning speed is 0 km/h)."
    )
    ans = "Height shows total distance, while speed is determined by the steepness (gradient) of the graph."
    return {
        "id": f"g7_graph_44_{rng.randint(100000, 999999)}",
        "subskill": "44_spot_the_error_confusing_steepness_with_height",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_44",
        "hints": {
            "tier_1": "Does height show distance or speed?",
            "tier_2": "Height shows distance; steepness shows speed.",
            "tier_3": ans
        },
        "misconception_tags": ["height_confused_with_slope_misconception"]
    }


# 45. Spot the error connecting discrete dots
def arch_45_spot_the_error_connecting_discrete_dots(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner plots the number of loaves of bread baked versus the number of whole bags of flour used. "
        "The learner connects the discrete dots with a solid continuous line.\n\n"
        "Explain why connecting the dots is mathematically incorrect for this scenario."
    )
    sol = (
        "**Answer:** The data is **discrete**. Whole bags of flour and whole loaves of bread are counted in integer units. "
        "Drawing a continuous line falsely implies that fractional values (e.g. 2.37 bags of flour producing 4.81 loaves) exist."
    )
    ans = "The data is discrete (counted in whole units), so points should not be connected by a continuous line."
    return {
        "id": f"g7_graph_45_{rng.randint(100000, 999999)}",
        "subskill": "45_spot_the_error_connecting_discrete_dots",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_45",
        "hints": {
            "tier_1": "Can you have fractional bags of flour?",
            "tier_2": "Discrete data must remain as separate dots.",
            "tier_3": ans
        },
        "misconception_tags": ["continuous_line_on_discrete_data"]
    }


# 46. Practical context hiking elevation profile
def arch_46_practical_context_hiking_elevation_profile(rng: random.Random) -> Dict[str, Any]:
    elev_start = 1200
    elev_peak = rng.choice([1800, 2000, 2200, 2400])
    gain = elev_peak - elev_start
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Elevation (m)",
        path_d="M 60 160 L 260 60 L 360 160",
        x_ticks=[(60, "0"), (260, "4"), (360, "6")],
        y_ticks=[(160, f"{elev_start}"), (60, f"{elev_peak}")]
    )
    prompt = (
        f"A mountain trail elevation profile starts at {elev_start} m above sea level and reaches a summit at {elev_peak} m.\n\n"
        f"1. What is the total elevation gained during the ascent?\n"
        f"2. If the descent back to {elev_start} m takes half as much time as the climb, "
        f"which section has the steeper slope on an elevation-time graph?"
    )
    sol = (
        f"**Step 1:** $\\text{{Elevation gain}} = {elev_peak} - {elev_start} = {gain}\\text{{ metres}}$.\n\n"
        f"**Step 2:** The descent covers the same elevation in half the time, so the **descent has the steeper slope**."
    )
    ans = f"1. {gain} metres; 2. The descent"
    return {
        "id": f"g7_graph_46_{rng.randint(100000, 999999)}",
        "subskill": "46_practical_context_hiking_elevation_profile",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_46",
        "hints": {
            "tier_1": f"Subtract {elev_start} from {elev_peak}.",
            "tier_2": "Faster change over shorter time = steeper slope.",
            "tier_3": ans
        },
        "misconception_tags": ["elevation_profile_rate_error"]
    }


# 47. Practical context battery percentage discharge
def arch_47_practical_context_battery_percentage_discharge(rng: random.Random) -> Dict[str, Any]:
    hours = rng.choice([8, 10, 12])
    rate = 100 // hours
    rem = 100 - (rate * hours)
    prompt = (
        f"A smartphone battery drops from 100% to 0% over {hours} hours of continuous video streaming at a constant rate.\n\n"
        f"1. What is the discharge rate in percent per hour?\n"
        f"2. What is the battery percentage remaining after 3 hours of streaming?"
    )
    rem_3 = 100 - 3 * (100 / hours)
    sol = (
        f"**Step 1:** $\\text{{Discharge rate}} = \\frac{{100\\%}}{{{hours}\\text{{ h}}}} = {100/hours:.1f}\\%\\text{{/hour}}$.\n\n"
        f"**Step 2:** After 3 hours: $$100\\% - (3 \\times {100/hours:.1f}\\%) = {rem_3:.1f}\\%$$."
    )
    ans = f"1. {100/hours:.1f}%/hour; 2. {rem_3:.1f}%"
    return {
        "id": f"g7_graph_47_{rng.randint(100000, 999999)}",
        "subskill": "47_practical_context_battery_percentage_discharge",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_47",
        "hints": {
            "tier_1": f"Divide 100 by {hours}.",
            "tier_2": "Subtract 3 hours of battery use from 100%.",
            "tier_3": ans
        },
        "misconception_tags": ["percentage_rate_subtraction_error"]
    }


# 48. Practical context baking oven preheating
def arch_48_practical_context_baking_oven_preheating(rng: random.Random) -> Dict[str, Any]:
    room_t = 20
    target_t = rng.choice([170, 180, 200, 220])
    time_min = 10
    rate = (target_t - room_t) // time_min
    svg = _svg_graph(
        x_label="Time (minutes)",
        y_label="Oven Temp (°C)",
        path_d="M 60 180 L 160 60 L 360 60",
        x_ticks=[(60, "0"), (160, "10"), (360, "40")],
        y_ticks=[(180, f"{room_t}"), (60, f"{target_t}")]
    )
    prompt = (
        f"An electric oven is preheated from room temperature ({room_t}°C) to baking temperature ({target_t}°C) in {time_min} minutes.\n\n"
        f"1. Calculate the rate of temperature increase in °C per minute.\n"
        f"2. If it maintains {target_t}°C for 30 minutes of baking, describe the graph during that baking period."
    )
    sol = (
        f"**Step 1:** $\\text{{Rate of heating}} = \\frac{{{target_t} - {room_t}}}{{{time_min}}} = \\frac{{{target_t - room_t}}}{{{time_min}}} = {rate}^\\circ\\text{{C/min}}$.\n\n"
        f"**Step 2:** During baking, the graph is a **horizontal straight line at {target_t}°C**."
    )
    ans = f"1. {rate}°C/min; 2. A horizontal line at {target_t}°C"
    return {
        "id": f"g7_graph_48_{rng.randint(100000, 999999)}",
        "subskill": "48_practical_context_baking_oven_preheating",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_48",
        "hints": {
            "tier_1": f"Subtract: {target_t} - {room_t} = {target_t - room_t}, then divide by {time_min}.",
            "tier_2": "Constant temperature produces a horizontal line.",
            "tier_3": ans
        },
        "misconception_tags": ["preheating_rate_calculation_error"]
    }


# 49. Practical context rainfall accumulation storm
def arch_49_practical_context_rainfall_accumulation_storm(rng: random.Random) -> Dict[str, Any]:
    rain_total = rng.choice([30, 45, 60])
    dur = 3
    rate = rain_total // dur
    prompt = (
        f"A rain gauge records accumulated rainfall during a {dur}-hour thunderstorm. "
        f"Total rainfall reached {rain_total} mm.\n\n"
        f"1. What is the average rainfall intensity in mm per hour?\n"
        f"2. Explain why an accumulated rainfall graph can never have a negative slope."
    )
    sol = (
        f"**Step 1:** $\\text{{Intensity}} = \\frac{{{rain_total}\\text{{ mm}}}}{{{dur}\\text{{ h}}}} = {rate}\\text{{ mm/hour}}$.\n\n"
        f"**Step 2:** Accumulated rainfall only accumulates or stays constant; it **cannot un-rain or decrease**, "
        f"so the slope can only be positive or zero."
    )
    ans = f"1. {rate} mm/hour; 2. Accumulated rainfall can never decrease (cannot un-rain)."
    return {
        "id": f"g7_graph_49_{rng.randint(100000, 999999)}",
        "subskill": "49_practical_context_rainfall_accumulation_storm",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_49",
        "hints": {
            "tier_1": f"Divide {rain_total} by {dur}.",
            "tier_2": "Cumulative totals can only go up or stay flat.",
            "tier_3": ans
        },
        "misconception_tags": ["cumulative_quantity_negative_slope_misconception"]
    }


# 50. Comprehensive multi stage journey autopsy
def arch_50_comprehensive_multi_stage_journey_autopsy(rng: random.Random) -> Dict[str, Any]:
    d1 = rng.choice([30, 40, 50])
    d2 = 2 * d1
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Distance from School (km)",
        path_d="M 60 200 L 140 100 L 220 100 L 300 40 L 360 200",
        points=[(140, 100), (220, 100), (300, 40), (360, 200)],
        x_ticks=[(60, "0"), (140, "1"), (220, "2"), (300, "3"), (360, "4")],
        y_ticks=[(200, "0"), (100, f"{d1}"), (40, f"{d2}")]
    )
    prompt = (
        "The graph illustrates a school bus journey from School:\n"
        f"- Stage 1 (0 to 1 h): travels {d1} km\n"
        "- Stage 2 (1 to 2 h): rest stop\n"
        f"- Stage 3 (2 to 3 h): travels from {d1} km to {d2} km\n"
        f"- Stage 4 (3 to 4 h): returns directly back to School ({d2} km to 0 km in 1 hour)\n\n"
        "1. In which stage did the bus travel at its fastest speed?\n"
        "2. What was the fastest speed in km/h?\n"
        "3. What was the total distance covered by the bus over the entire 4 hours?"
    )
    sol = (
        "**Step 1 & 2:** Speed for each stage:\n"
        f"- Stage 1: ${d1}\\text{{ km}} / 1\\text{{ h}} = {d1}\\text{{ km/h}}$\n"
        "- Stage 2: $0\\text{ km/h}$ (stationary)\n"
        f"- Stage 3: ${d1}\\text{{ km}} / 1\\text{{ h}} = {d1}\\text{{ km/h}}$\n"
        f"- Stage 4: ${d2}\\text{{ km}} / 1\\text{{ h}} = \\mathbf{{{d2}\\text{{ km/h}}}}$\n"
        f"The fastest stage was **Stage 4** at **{d2} km/h**.\n\n"
        f"**Step 3:** Total distance = ${d2}\\text{{ km (outbound)}} + {d2}\\text{{ km (return)}} = \\mathbf{{{2*d2}\\text{{ km}}}}$."
    )
    ans = f"1. Stage 4; 2. {d2} km/h; 3. {2*d2} km"
    return {
        "id": f"g7_graph_50_{rng.randint(100000, 999999)}",
        "subskill": "50_comprehensive_multi_stage_journey_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Calculate Stage Speeds", "body": f"Stage 1: {d1} km/h, Stage 2: 0, Stage 3: {d1} km/h, Stage 4: {d2} km/h."},
                {"title": "Fastest Leg", "body": f"Stage 4 has the steepest gradient: {d2} km/h."},
                {"title": "Total Distance", "body": f"{d2} km out + {d2} km back = {2*d2} km."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_graphs_50",
        "hints": {
            "tier_1": "Which section has the steepest slope?",
            "tier_2": f"Stage 4 covers {d2} km in 1 hour.",
            "tier_3": ans
        },
        "misconception_tags": ["total_distance_confused_with_displacement"]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
