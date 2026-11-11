"""Grade 7 Mathematics - Graphs: Archetypes 01 to 25.
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
    height: int = 260
) -> str:
    """Generates a clean Cartesian graph SVG on white background with dark geometry."""
    origin_x, origin_y = 60, 200
    w_plot, h_plot = 340, 160
    
    # Axis lines
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px;">',
        f'<defs><marker id="ar" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">'
        f'<path d="M0,0 L0,6 L6,3 z" fill="#1e293b"/></marker></defs>',
        # Grid lines (light)
        f'<line x1="{origin_x}" y1="{origin_y - h_plot}" x2="{origin_x + w_plot}" y2="{origin_y - h_plot}" stroke="#e2e8f0" stroke-width="1"/>',
        f'<line x1="{origin_x}" y1="{origin_y - h_plot//2}" x2="{origin_x + w_plot}" y2="{origin_y - h_plot//2}" stroke="#e2e8f0" stroke-width="1"/>',
        # Axes
        f'<line x1="{origin_x}" y1="{origin_y}" x2="{origin_x + w_plot + 15}" y2="{origin_y}" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar)"/>',
        f'<line x1="{origin_x}" y1="{origin_y}" x2="{origin_x}" y2="{origin_y - h_plot - 15}" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar)"/>',
        # Axis Labels
        f'<text x="{origin_x + w_plot//2}" y="{origin_y + 40}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">{x_label}</text>',
        f'<text x="20" y="{origin_y - h_plot//2}" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" transform="rotate(-90 20 {origin_y - h_plot//2})" text-anchor="middle">{y_label}</text>',
    ]
    
    # Custom X Ticks
    if x_ticks:
        for x_val, label in x_ticks:
            svg_parts.append(f'<line x1="{x_val}" y1="{origin_y}" x2="{x_val}" y2="{origin_y + 5}" stroke="#1e293b" stroke-width="1.5"/>')
            svg_parts.append(f'<text x="{x_val}" y="{origin_y + 18}" font-family="sans-serif" font-size="10" fill="#475569" text-anchor="middle">{label}</text>')

    # Custom Y Ticks
    if y_ticks:
        for y_val, label in y_ticks:
            svg_parts.append(f'<line x1="{origin_x - 5}" y1="{y_val}" x2="{origin_x}" y2="{y_val}" stroke="#1e293b" stroke-width="1.5"/>')
            svg_parts.append(f'<text x="{origin_x - 10}" y="{y_val + 4}" font-family="sans-serif" font-size="10" fill="#475569" text-anchor="end">{label}</text>')

    # Plot path
    if path_d:
        svg_parts.append(f'<path d="{path_d}" fill="none" stroke="#2563eb" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')

    # Points
    if points:
        for px, py in points:
            svg_parts.append(f'<circle cx="{px}" cy="{py}" r="4" fill="#dc2626"/>')

    svg_parts.append('</svg>')
    return "".join(svg_parts)


# 01. Story graph identify increasing interval
def arch_01_story_graph_identify_increasing_interval(rng: random.Random) -> Dict[str, Any]:
    max_d = rng.choice([40, 50, 60, 80])
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Water Depth (cm)",
        path_d="M 60 200 L 160 80 L 260 80 L 360 180",
        x_ticks=[(60, "0"), (160, "4"), (260, "8"), (360, "12")],
        y_ticks=[(200, "0"), (140, f"{max_d//2}"), (80, f"{max_d}")]
    )
    prompt = (
        f"The graph illustrates the water depth (up to {max_d} cm) in a garden pond over a 12-hour recording period.\n\n"
        "1. Identify the time interval (in hours) during which the water depth was increasing.\n"
        "2. What visual feature of the graph line indicates that the value is increasing?"
    )
    sol = (
        "**Step 1:** The line slopes upwards from left to right from time $0$ to time $4$ hours.\n\n"
        "**Step 2:** An upward slope (positive gradient) from left to right indicates an **increasing** quantity."
    )
    ans = "1. From 0 to 4 hours; 2. The line slopes upward from left to right."
    return {
        "id": f"g7_graph_01_{rng.randint(100000, 999999)}",
        "subskill": "01_story_graph_identify_increasing_interval",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Look for Upward Slope", "body": f"Between t = 0 and t = 4, the curve rises from 0 to {max_d} cm."},
                {"title": "State Interval", "body": "Increasing interval is 0 to 4 hours."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_01",
        "hints": {
            "tier_1": "Find where the line rises from left to right.",
            "tier_2": "Look at the x-axis numbers directly below the rising section.",
            "tier_3": ans
        },
        "misconception_tags": ["read_y_axis_instead_of_x_interval"]
    }


# 02. Story graph identify decreasing interval
def arch_02_story_graph_identify_decreasing_interval(rng: random.Random) -> Dict[str, Any]:
    max_d = rng.choice([40, 50, 60, 80])
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Water Depth (cm)",
        path_d="M 60 200 L 160 80 L 260 80 L 360 180",
        x_ticks=[(60, "0"), (160, "4"), (260, "8"), (360, "12")],
        y_ticks=[(200, "0"), (140, f"{max_d//2}"), (80, f"{max_d}")]
    )
    prompt = (
        f"Refer to the garden pond depth graph (peak depth {max_d} cm) above.\n\n"
        "1. Identify the time interval (in hours) during which the water depth was decreasing.\n"
        "2. Describe what was happening to the water level during this interval."
    )
    sol = (
        "**Step 1:** The line slopes downwards from left to right between $8$ hours and $12$ hours.\n\n"
        f"**Step 2:** The water level is falling / draining from ${max_d}\\text{{ cm}}$ down to $10\\text{{ cm}}$."
    )
    ans = "1. From 8 to 12 hours; 2. The water level is falling / decreasing."
    return {
        "id": f"g7_graph_02_{rng.randint(100000, 999999)}",
        "subskill": "02_story_graph_identify_decreasing_interval",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Downward Slope", "body": "From t = 8 to t = 12, the line goes downwards."},
                {"title": "Physical Meaning", "body": "Decreasing means water is draining out."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_02",
        "hints": {
            "tier_1": "Where does the line slope downwards?",
            "tier_2": "Look between 8 and 12 hours.",
            "tier_3": ans
        },
        "misconception_tags": ["confused_decreasing_with_stationary"]
    }


# 03. Story graph identify constant interval
def arch_03_story_graph_identify_constant_interval(rng: random.Random) -> Dict[str, Any]:
    max_d = rng.choice([40, 50, 60, 80])
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Water Depth (cm)",
        path_d="M 60 200 L 160 80 L 260 80 L 360 180",
        x_ticks=[(60, "0"), (160, "4"), (260, "8"), (360, "12")],
        y_ticks=[(200, "0"), (140, f"{max_d//2}"), (80, f"{max_d}")]
    )
    prompt = (
        f"Refer to the garden pond depth graph (level {max_d} cm) above.\n\n"
        "1. Identify the time interval during which the water level remained constant.\n"
        "2. What visual feature shows that a quantity is constant on a time graph?"
    )
    sol = (
        "**Step 1:** The line is completely horizontal between $4$ hours and $8$ hours.\n\n"
        "**Step 2:** A **flat horizontal line** indicates that the dependent variable is unchanging (constant)."
    )
    ans = "1. From 4 to 8 hours; 2. A horizontal (flat) line."
    return {
        "id": f"g7_graph_03_{rng.randint(100000, 999999)}",
        "subskill": "03_story_graph_identify_constant_interval",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Locate Flat Section", "body": "The flat plateau extends from t = 4 to t = 8."},
                {"title": "Concept", "body": "Zero change = horizontal line."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_03",
        "hints": {
            "tier_1": "Find the horizontal portion of the graph.",
            "tier_2": "Look at the x-axis under the flat line (4 to 8 hours).",
            "tier_3": ans
        },
        "misconception_tags": ["assumed_flat_line_means_zero_value"]
    }


# 04. Story graph identify maximum turning point
def arch_04_story_graph_identify_maximum_turning_point(rng: random.Random) -> Dict[str, Any]:
    max_val = rng.choice([28, 30, 32, 35])
    max_time = rng.choice([14, 15])
    svg = _svg_graph(
        x_label="Time of Day (hours)",
        y_label="Temperature (°C)",
        path_d="M 60 170 Q 200 40 360 160",
        points=[(210, 45)],
        x_ticks=[(60, "06:00"), (210, f"{max_time}:00"), (360, "20:00")],
        y_ticks=[(170, "15"), (110, "25"), (45, f"{max_val}")]
    )
    prompt = (
        f"The graph records daily temperature changes from 06:00 to 20:00.\n\n"
        f"1. What was the maximum temperature recorded during the day?\n"
        f"2. At what time did this maximum temperature occur?"
    )
    sol = (
        f"**Step 1:** The highest peak of the curve reaches ${max_val}^\\circ\\text{{C}}$.\n\n"
        f"**Step 2:** Reading down to the horizontal axis from the highest point gives **{max_time}:00**."
    )
    ans = f"1. {max_val}°C; 2. At {max_time}:00"
    return {
        "id": f"g7_graph_04_{rng.randint(100000, 999999)}",
        "subskill": "04_story_graph_identify_maximum_turning_point",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Locate Peak", "body": f"The red dot marks the highest point at {max_val}°C."},
                {"title": "Read Time", "body": f"Project down to the time axis: {max_time}:00."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_04",
        "hints": {
            "tier_1": "Find the highest point (crest) on the curve.",
            "tier_2": f"Look at the y-axis for temperature ({max_val}°C) and x-axis for time ({max_time}:00).",
            "tier_3": ans
        },
        "misconception_tags": ["swapped_input_output_coordinates"]
    }


# 05. Story graph identify minimum turning point
def arch_05_story_graph_identify_minimum_turning_point(rng: random.Random) -> Dict[str, Any]:
    min_val = rng.choice([2, 4, 6, 8, 9])
    svg = _svg_graph(
        x_label="Time of Night (hours)",
        y_label="Temperature (°C)",
        path_d="M 60 70 Q 200 180 360 80",
        points=[(210, 180)],
        x_ticks=[(60, "20:00"), (210, "04:00"), (360, "08:00")],
        y_ticks=[(70, "20"), (125, "12"), (180, f"{min_val}")]
    )
    prompt = (
        "The graph illustrates night-time ambient temperature fluctuations.\n\n"
        "1. What was the minimum (lowest) temperature reached?\n"
        "2. At what time was the temperature at its minimum?"
    )
    sol = (
        f"**Step 1:** The lowest trough on the graph reaches **{min_val}°C** on the vertical axis.\n\n"
        f"**Step 2:** Reading vertically down to the x-axis gives **04:00**."
    )
    ans = f"1. {min_val}°C; 2. At 04:00"
    return {
        "id": f"g7_graph_05_{rng.randint(100000, 999999)}",
        "subskill": "05_story_graph_identify_minimum_turning_point",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Locate Lowest Point", "body": f"The trough dips to {min_val}°C."},
                {"title": "Read Time", "body": "The time corresponding to this minimum is 04:00."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_05",
        "hints": {
            "tier_1": "Find the lowest point (valley) on the curve.",
            "tier_2": f"Y-value is {min_val}°C, X-value is 04:00.",
            "tier_3": ans
        },
        "misconception_tags": ["confused_maximum_with_minimum"]
    }


# 06. Discrete vs continuous concept classification
def arch_06_discrete_vs_continuous_concept_classification(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In Mathematics, data and graphs are classified as either **discrete** or **continuous**.\n\n"
        "1. Define what makes data discrete versus continuous.\n"
        "2. Classify each of the following scenarios as discrete or continuous:\n"
        "   (a) The number of learners attending school each day.\n"
        "   (b) The height of a growing maize plant measured over 8 weeks.\n"
        "   (c) The number of goals scored in soccer matches."
    )
    sol = (
        "**Step 1:**\n"
        "- **Discrete data** consists of separate, distinct values (counted in whole numbers; cannot take fractions/in-between values).\n"
        "- **Continuous data** can take any value within a given range (measured on a continuous scale like time, height, mass).\n\n"
        "**Step 2:**\n"
        "(a) Number of learners $\\rightarrow$ **Discrete** (you count whole people).\n"
        "(b) Height of maize plant $\\rightarrow$ **Continuous** (plant grows continuously through fractional measurements).\n"
        "(c) Goals scored $\\rightarrow$ **Discrete** (goals are whole numbers)."
    )
    ans = "1. Discrete data is counted in separate whole units; Continuous data is measured continuously along a scale; 2. (a) Discrete, (b) Continuous, (c) Discrete"
    return {
        "id": f"g7_graph_06_{rng.randint(100000, 999999)}",
        "subskill": "06_discrete_vs_continuous_concept_classification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g7_graphs_06",
        "hints": {
            "tier_1": "Can you have half a learner or 2.5 goals? If not, it is discrete.",
            "tier_2": "Things counted are discrete; things measured (height, time) are continuous.",
            "tier_3": ans
        },
        "misconception_tags": ["confused_discrete_and_continuous"]
    }


# 07. Discrete graph interpretation points only
def arch_07_discrete_graph_interpretation_points_only(rng: random.Random) -> Dict[str, Any]:
    p = rng.choice([70, 80, 90, 100, 110])
    svg = _svg_graph(
        x_label="Number of T-shirts",
        y_label="Total Cost (Rands)",
        path_d="",
        points=[(100, 170), (160, 140), (220, 110), (280, 80), (340, 50)],
        x_ticks=[(100, "1"), (160, "2"), (220, "3"), (280, "4"), (340, "5")],
        y_ticks=[(170, f"{p}"), (140, f"{2*p}"), (110, f"{3*p}"), (80, f"{4*p}"), (50, f"{5*p}")]
    )
    prompt = (
        "The graph plots the cost of buying school T-shirts against the number of T-shirts bought.\n\n"
        "1. Why are the data points plotted as separate dots rather than connected by a solid continuous line?\n"
        "2. What is the cost of buying 3 T-shirts according to the graph?"
    )
    sol = (
        "**Step 1:** The number of T-shirts is **discrete data** (you can only buy whole shirts, not fractions like 1.5 shirts). "
        "Connecting the dots with a line would falsely imply that fractional quantities of shirts exist.\n\n"
        f"**Step 2:** Looking at input $3$ on the x-axis, the corresponding y-value is **R{3*p}**."
    )
    ans = f"1. T-shirts are discrete items (cannot buy fractions of a shirt); 2. R{3*p}"
    return {
        "id": f"g7_graph_07_{rng.randint(100000, 999999)}",
        "subskill": "07_discrete_graph_interpretation_points_only",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Look at Dots", "body": "Notice that dots are isolated without connecting lines."},
                {"title": "Discrete Nature", "body": "You cannot purchase 1.5 or 2.7 shirts."},
                {"title": "Read 3 shirts", "body": f"At x = 3, y = R{3*p}."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_07",
        "hints": {
            "tier_1": "Can a shop sell 2.5 shirts?",
            "tier_2": "Points are not joined because the data is discrete.",
            "tier_3": ans
        },
        "misconception_tags": ["inappropriate_line_joining_discrete_points"]
    }


# 08. Continuous graph interpretation unbroken line
def arch_08_continuous_graph_interpretation_unbroken_line(rng: random.Random) -> Dict[str, Any]:
    step_d = rng.choice([4, 5, 6, 8])
    svg = _svg_graph(
        x_label="Time (minutes)",
        y_label="Distance (km)",
        path_d="M 60 200 L 360 60",
        x_ticks=[(60, "0"), (160, "10"), (260, "20"), (360, "30")],
        y_ticks=[(200, "0"), (153, f"{step_d}"), (106, f"{2*step_d}"), (60, f"{3*step_d}")]
    )
    prompt = (
        "A cyclist rides steadily along a cycle track. Distance against time is drawn with a solid unbroken line.\n\n"
        "1. Explain why distance and time can be joined with a continuous solid line.\n"
        "2. Can you read values at fractional minutes (e.g. 15.5 minutes) from this graph? Explain."
    )
    sol = (
        "**Step 1:** Both distance and time are **continuous quantities** that flow smoothly and can take any intermediate fractional or decimal value.\n\n"
        "**Step 2:** **Yes**, because the line is continuous, every real point along the line represents a valid instant in time and corresponding distance."
    )
    ans = "1. Distance and time are continuous variables; 2. Yes, because continuous graphs allow values at any intermediate fractional point."
    return {
        "id": f"g7_graph_08_{rng.randint(100000, 999999)}",
        "subskill": "08_continuous_graph_interpretation_unbroken_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Continuous Flow", "body": "Time moves continuously without gaps."},
                {"title": "Intermediate Values", "body": "Any point on the solid line has a measurable meaning."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_08",
        "hints": {
            "tier_1": "Does time jump in whole steps or flow smoothly?",
            "tier_2": "Continuous lines represent variables that can take any fractional value.",
            "tier_3": ans
        },
        "misconception_tags": ["continuous_variables_intermediate_meaning"]
    }


# 09. Independent vs dependent variable identification
def arch_09_independent_vs_dependent_variable_identification(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice([
        ("amount of electricity consumed (kWh)", "cost of electricity bill (Rands)"),
        ("number of hours studied", "examination test mark (%)"),
        ("time water is heated (minutes)", "temperature of water (°C)")
    ])
    v1, v2 = context
    prompt = (
        f"A scientific investigation explores the relationship between {v1} and {v2}.\n\n"
        f"1. Which variable is the **independent variable**, and which axis is it typically plotted on?\n"
        f"2. Which variable is the **dependent variable**, and which axis is it typically plotted on?"
    )
    sol = (
        f"**Step 1:** The **independent variable** (the input or cause) is **{v1}**, plotted on the **horizontal axis (x-axis)**.\n\n"
        f"**Step 2:** The **dependent variable** (the output or outcome that depends on the other) is **{v2}**, plotted on the **vertical axis (y-axis)**."
    )
    ans = f"1. Independent: {v1} (horizontal/x-axis); 2. Dependent: {v2} (vertical/y-axis)"
    return {
        "id": f"g7_graph_09_{rng.randint(100000, 999999)}",
        "subskill": "09_independent_vs_dependent_variable_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_09",
        "hints": {
            "tier_1": "Which variable depends on the other?",
            "tier_2": "Independent goes on horizontal axis; Dependent goes on vertical axis.",
            "tier_3": ans
        },
        "misconception_tags": ["swapped_independent_dependent_axes"]
    }


# 10. Axis labels and scales reading
def arch_10_axis_labels_and_scales_reading(rng: random.Random) -> Dict[str, Any]:
    step_y = rng.choice([5, 10, 20, 50])
    y4 = 4 * step_y
    svg = _svg_graph(
        x_label="Time (days)",
        y_label="Mass (kg)",
        path_d="M 60 200 L 360 80",
        x_ticks=[(60, "0"), (135, "1"), (210, "2"), (285, "3"), (360, "4")],
        y_ticks=[(200, "0"), (170, f"{step_y}"), (140, f"{2*step_y}"), (110, f"{3*step_y}"), (80, f"{y4}")]
    )
    prompt = (
        "Inspect the axes of the graph shown above.\n\n"
        "1. What is the scale (unit value per major grid mark) on the horizontal axis?\n"
        "2. What is the scale (unit value per major grid mark) on the vertical axis?"
    )
    sol = (
        f"**Step 1:** On the horizontal axis, each tick mark represents **1 day**.\n\n"
        f"**Step 2:** On the vertical axis, the ticks advance from 0 to {step_y}, {2*step_y}, {3*step_y}, etc., "
        f"so each tick mark represents **{step_y} kg**."
    )
    ans = f"1. 1 day per tick mark; 2. {step_y} kg per tick mark"
    return {
        "id": f"g7_graph_10_{rng.randint(100000, 999999)}",
        "subskill": "10_axis_labels_and_scales_reading",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Check X Ticks", "body": "0 to 1 to 2 -> step is 1 day."},
                {"title": "Check Y Ticks", "body": f"0 to {step_y} to {2*step_y} -> step is {step_y} kg."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_10",
        "hints": {
            "tier_1": "Find the difference between consecutive numbers on each axis.",
            "tier_2": f"X goes up by 1; Y goes up by {step_y}.",
            "tier_3": ans
        },
        "misconception_tags": ["scale_reading_arithmetic_error"]
    }


# 11. Rate of change constant linear identification
def arch_11_rate_of_change_constant_linear_identification(rng: random.Random) -> Dict[str, Any]:
    sp = rng.choice([15, 20, 25, 30])
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Distance (km)",
        path_d="M 60 200 L 360 80",
        x_ticks=[(60, "0"), (160, "2"), (260, "4"), (360, "6")],
        y_ticks=[(200, "0"), (160, f"{2*sp}"), (120, f"{4*sp}"), (80, f"{6*sp}")]
    )
    prompt = (
        f"The graph of a car's journey is a perfectly straight line from (0, 0) through (2, {2*sp}), (4, {4*sp}), and (6, {6*sp}).\n\n"
        "1. What can you say about the car's rate of change (speed)? Is it constant, increasing, or decreasing?\n"
        "2. Calculate the exact rate of change in km/h."
    )
    sol = (
        "**Step 1:** A straight line graph indicates a **constant rate of change**.\n\n"
        f"**Step 2:** Rate of change = $\\frac{{\\text{{change in distance}}}}{{\\text{{change in time}}}} = \\frac{{{2*sp}\\text{{ km}}}}{{2\\text{{ h}}}} = {sp}\\text{{ km/h}}$."
    )
    ans = f"1. Constant rate of change; 2. {sp} km/h"
    return {
        "id": f"g7_graph_11_{rng.randint(100000, 999999)}",
        "subskill": "11_rate_of_change_constant_linear_identification",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Straight Line", "body": "A straight line always represents a constant rate of change."},
                {"title": "Calculate Speed", "body": f"{2*sp} km / 2 h = {sp} km/h."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_11",
        "hints": {
            "tier_1": "Straight lines have constant slopes.",
            "tier_2": f"Divide {2*sp} by 2.",
            "tier_3": ans
        },
        "misconception_tags": ["variable_speed_belief_on_straight_line"]
    }


# 12. Rate of change increasing faster and faster
def arch_12_rate_of_change_increasing_faster_and_faster(rng: random.Random) -> Dict[str, Any]:
    max_pop = rng.choice([3000, 4000, 5000, 6000])
    svg = _svg_graph(
        x_label="Time (days)",
        y_label="Bacteria Population",
        path_d="M 60 190 Q 220 180 360 40",
        x_ticks=[(60, "0"), (160, "2"), (260, "4"), (360, "6")],
        y_ticks=[(200, "0"), (150, "500"), (100, "1500"), (40, f"{max_pop}")]
    )
    prompt = (
        "The graph illustrates the growth of a bacterial colony over 6 days. The curve becomes noticeably steeper as time progresses.\n\n"
        "1. How is the rate of change behaving? (Choose: constant, increasing, or decreasing)\n"
        "2. Explain in words what 'increasing rate of change' means in this context."
    )
    sol = (
        "**Step 1:** The rate of change is **increasing** (growing faster and faster).\n\n"
        "**Step 2:** It means the population is adding more bacteria each subsequent day than it did on the previous day."
    )
    ans = "1. Increasing; 2. The population grows faster and faster with each passing day (steeper slope)."
    return {
        "id": f"g7_graph_12_{rng.randint(100000, 999999)}",
        "subskill": "12_rate_of_change_increasing_faster_and_faster",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Observe Curvature", "body": "The curve starts shallow and bends upwards steeply."},
                {"title": "Meaning", "body": "Rate of change is increasing over time."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_12",
        "hints": {
            "tier_1": "Does the curve get steeper or flatter?",
            "tier_2": "Steeper slope means increasing rate of change.",
            "tier_3": ans
        },
        "misconception_tags": ["confused_increasing_value_with_constant_rate"]
    }


# 13. Rate of change decreasing slower and slower
def arch_13_rate_of_change_decreasing_slower_and_slower(rng: random.Random) -> Dict[str, Any]:
    max_h = rng.choice([85, 90, 95, 100])
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Water Height (cm)",
        path_d="M 60 200 Q 140 70 360 60",
        x_ticks=[(60, "0"), (160, "2"), (260, "4"), (360, "6")],
        y_ticks=[(200, "0"), (130, "50"), (80, "75"), (60, f"{max_h}")]
    )
    prompt = (
        "A wide container is filled with water. The graph rises very quickly at first and then flattens out gradually.\n\n"
        "1. Is the rate of change of water height constant, increasing, or decreasing?\n"
        "2. What visual clue shows that the rate of change is slowing down?"
    )
    sol = (
        "**Step 1:** The rate of change is **decreasing** (growing slower and slower).\n\n"
        "**Step 2:** The curve becomes **gentler (flatter)** as time advances."
    )
    ans = "1. Decreasing; 2. The curve gets flatter / less steep over time."
    return {
        "id": f"g7_graph_13_{rng.randint(100000, 999999)}",
        "subskill": "13_rate_of_change_decreasing_slower_and_slower",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Look at Gradient", "body": "The slope is steep initially, then levels off."},
                {"title": "Rate Interpretation", "body": "Decreasing rate of change."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_13",
        "hints": {
            "tier_1": "Does the line become steeper or flatter?",
            "tier_2": "Flatter slope means decreasing rate of change.",
            "tier_3": ans
        },
        "misconception_tags": ["flattening_curve_misinterpretation"]
    }


# 14. Steepness comparison fast vs slow change
def arch_14_steepness_comparison_fast_vs_slow_change(rng: random.Random) -> Dict[str, Any]:
    sp_a = rng.choice([50, 60, 70, 80])
    d_a = 2 * sp_a
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Distance (km)",
        path_d="M 60 200 L 210 60 L 360 90",
        points=[(210, 60)],
        x_ticks=[(60, "0"), (210, "2"), (360, "5")],
        y_ticks=[(200, "0"), (130, f"{sp_a}"), (60, f"{d_a}")]
    )
    prompt = (
        "A runner's journey is split into two sections: Section A (from 0 to 2 hours) and Section B (from 2 to 5 hours).\n\n"
        "1. In which section was the runner traveling at a greater speed (steeper slope)?\n"
        "2. Calculate the speed in km/h for Section A."
    )
    sol = (
        "**Step 1:** Section A is much steeper than Section B, meaning speed was **greater in Section A**.\n\n"
        f"**Step 2:** In Section A, the runner covered ${d_a}\\text{{ km}}$ in $2\\text{{ hours}}$, so:\n"
        f"$$\\text{{Speed}} = \\frac{{{d_a}\\text{{ km}}}}{{2\\text{{ h}}}} = {sp_a}\\text{{ km/h}}$$"
    )
    ans = f"1. Section A; 2. {sp_a} km/h"
    return {
        "id": f"g7_graph_14_{rng.randint(100000, 999999)}",
        "subskill": "14_steepness_comparison_fast_vs_slow_change",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Compare Slopes", "body": "Section A rises sharply compared to Section B."},
                {"title": "Calculate Speed A", "body": f"{d_a} km / 2 h = {sp_a} km/h."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_14",
        "hints": {
            "tier_1": "Steeper slope = faster speed.",
            "tier_2": "Divide distance by time for Section A.",
            "tier_3": ans
        },
        "misconception_tags": ["longer_time_interval_confused_with_faster_speed"]
    }


# 15. Reading output value from given input
def arch_15_reading_output_value_from_given_input(rng: random.Random) -> Dict[str, Any]:
    rate = rng.choice([25, 30, 40, 50])
    inp = rng.choice([2, 3, 4])
    out = inp * rate
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Distance (km)",
        path_d=f"M 60 200 L 360 {200 - 5 * rate // 2}",
        points=[(60 + inp * 60, 200 - inp * rate // 2)],
        x_ticks=[(60, "0"), (120, "1"), (180, "2"), (240, "3"), (300, "4"), (360, "5")],
        y_ticks=[(200, "0"), (150, f"{rate}"), (100, f"{2*rate}"), (50, f"{3*rate}")]
    )
    prompt = (
        f"A cyclist travels according to the distance-time graph shown.\n\n"
        f"Use the graph to find the distance covered after exactly **{inp} hours** of cycling."
    )
    sol = (
        f"**Step 1:** Locate {inp} on the horizontal time axis.\n\n"
        f"**Step 2:** Trace vertically upwards to meet the line, then horizontally across to read the vertical distance axis.\n\n"
        f"**Conclusion:** The distance covered is **{out} km**."
    )
    ans = f"{out} km"
    return {
        "id": f"g7_graph_15_{rng.randint(100000, 999999)}",
        "subskill": "15_reading_output_value_from_given_input",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Locate Input", "body": f"Find x = {inp} on the horizontal axis."},
                {"title": "Project to Line", "body": "Move up to the line."},
                {"title": "Read Output", "body": f"Read y = {out} km."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_15",
        "hints": {
            "tier_1": f"Find {inp} on the x-axis and look at the line above it.",
            "tier_2": "Look directly left to the y-axis.",
            "tier_3": ans
        },
        "misconception_tags": ["grid_interpolation_error"]
    }


# 16. Reading input value from given output
def arch_16_reading_input_value_from_given_output(rng: random.Random) -> Dict[str, Any]:
    rate = rng.choice([20, 30, 40])
    inp = rng.choice([2, 3, 4])
    out = inp * rate
    prompt = (
        f"A vehicle travels at a steady speed of {rate} km/h, represented by the linear equation $d = {rate}t$, "
        f"where $d$ is distance in km and $t$ is time in hours.\n\n"
        f"Find the time required to travel a distance of **{out} km**."
    )
    sol = (
        f"**Step 1:** Substitute $d = {out}$ into the formula:\n"
        f"$${out} = {rate}t$$\n\n"
        f"**Step 2:** Solve for $t$:\n"
        f"$$t = \\frac{{{out}}}{{{rate}}} = {inp}\\text{{ hours}}$$"
    )
    ans = f"{inp} hours"
    return {
        "id": f"g7_graph_16_{rng.randint(100000, 999999)}",
        "subskill": "16_reading_input_value_from_given_output",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_16",
        "hints": {
            "tier_1": f"Divide distance ({out}) by speed ({rate}).",
            "tier_2": f"t = {out} / {rate}.",
            "tier_3": ans
        },
        "misconception_tags": ["multiplied_instead_of_divided_for_time"]
    }


# 17. Distance-time graph stationary period
def arch_17_distance_time_graph_stationary_period(rng: random.Random) -> Dict[str, Any]:
    d_stop = rng.choice([40, 50, 60, 75])
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Distance from Home (km)",
        path_d="M 60 200 L 160 100 L 260 100 L 360 40",
        x_ticks=[(60, "0"), (160, "2"), (260, "3.5"), (360, "5")],
        y_ticks=[(200, "0"), (100, f"{d_stop}"), (40, f"{d_stop + 40}")]
    )
    prompt = (
        "The graph illustrates a family's road trip away from home.\n\n"
        "1. Identify the time period during which the family stopped and was stationary.\n"
        "2. How long did this stop last in hours and minutes?"
    )
    sol = (
        "**Step 1:** The horizontal line segment represents a stationary period where distance is unchanged: from **2 hours to 3.5 hours**.\n\n"
        "**Step 2:** Duration: $3.5 - 2 = 1.5\\text{ hours}$ (or **1 hour and 30 minutes**)."
    )
    ans = "1. From 2 hours to 3.5 hours; 2. 1 hour and 30 minutes (1.5 hours)"
    return {
        "id": f"g7_graph_17_{rng.randint(100000, 999999)}",
        "subskill": "17_distance_time_graph_stationary_period",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Flat Section", "body": f"Distance remains {d_stop} km between 2 and 3.5 hours."},
                {"title": "Duration", "body": "3.5 - 2 = 1.5 hours = 1 hour 30 min."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_17",
        "hints": {
            "tier_1": "Stationary means the distance does not increase (horizontal line).",
            "tier_2": "Subtract: 3.5 - 2 = 1.5 hours.",
            "tier_3": ans
        },
        "misconception_tags": ["decimal_hours_conversion_error"]
    }


# 18. Distance-time graph total distance traveled
def arch_18_distance_time_graph_total_distance_traveled(rng: random.Random) -> Dict[str, Any]:
    d1 = rng.choice([40, 50, 60])
    d2 = rng.choice([30, 40, 50])
    total = d1 + d2
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Distance from Start (km)",
        path_d="M 60 200 L 210 110 L 360 40",
        x_ticks=[(60, "0"), (210, "2"), (360, "4")],
        y_ticks=[(200, "0"), (110, f"{d1}"), (40, f"{total}")]
    )
    prompt = (
        f"A hiker walked from a base camp to Checkpoint 1 ({d1} km away) in 2 hours, and then continued "
        f"to Checkpoint 2 ({total} km from base) over the next 2 hours.\n\n"
        f"1. What is the total distance the hiker traveled from the base camp?\n"
        f"2. What was the average speed across the entire 4-hour hike?"
    )
    avg_speed = total / 4
    sol = (
        f"**Step 1:** The final y-value on the graph represents the total distance: **{total} km**.\n\n"
        f"**Step 2:** Average speed = $\\frac{{\\text{{Total Distance}}}}{{\\text{{Total Time}}}} = \\frac{{{total}\\text{{ km}}}}{{4\\text{{ h}}}} = {avg_speed}\\text{{ km/h}}$."
    )
    ans = f"1. {total} km; 2. {avg_speed} km/h"
    return {
        "id": f"g7_graph_18_{rng.randint(100000, 999999)}",
        "subskill": "18_distance_time_graph_total_distance_traveled",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Read Max Distance", "body": f"The total distance reached is {total} km."},
                {"title": "Average Speed", "body": f"{total} km / 4 h = {avg_speed} km/h."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_18",
        "hints": {
            "tier_1": "Read the top-most y-value for total distance.",
            "tier_2": f"Divide {total} by 4 for average speed.",
            "tier_3": ans
        },
        "misconception_tags": ["average_speed_calculation_error"]
    }


# 19. Distance-time graph calculating speed from slope
def arch_19_distance_time_graph_calculating_speed_from_slope(rng: random.Random) -> Dict[str, Any]:
    speed = rng.choice([60, 70, 80, 90])
    dist = speed * 2
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Distance (km)",
        path_d="M 60 200 L 360 60",
        x_ticks=[(60, "0"), (210, "2"), (360, "4")],
        y_ticks=[(200, "0"), (130, f"{speed}"), (60, f"{dist}")]
    )
    prompt = (
        f"A truck travels a distance of {dist} km in 4 hours at a constant rate.\n\n"
        f"1. What feature of a distance-time graph represents speed?\n"
        f"2. Calculate the speed of the truck in km/h."
    )
    sol = (
        f"**Step 1:** The **slope (gradient)** of a distance-time graph represents speed.\n\n"
        f"**Step 2:** $\\text{{Speed}} = \\frac{{\\text{{Distance}}}}{{\\text{{Time}}}} = \\frac{{{dist}\\text{{ km}}}}{{4\\text{{ h}}}} = {speed}\\text{{ km/h}}$."
    )
    ans = f"1. The slope (or gradient); 2. {speed} km/h"
    return {
        "id": f"g7_graph_19_{rng.randint(100000, 999999)}",
        "subskill": "19_distance_time_graph_calculating_speed_from_slope",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Slope = Speed", "body": "On distance-time graphs, slope is speed."},
                {"title": "Calculate", "body": f"{dist} / 4 = {speed} km/h."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_19",
        "hints": {
            "tier_1": "Speed = Distance divided by Time.",
            "tier_2": f"Divide {dist} by 4.",
            "tier_3": ans
        },
        "misconception_tags": ["gradient_speed_relationship_error"]
    }


# 20. Distance-time graph fastest leg comparison
def arch_20_distance_time_graph_fastest_leg_comparison(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A courier drives three distinct legs of a delivery route:\n"
        "- Leg 1: 50 km covered in 1 hour\n"
        "- Leg 2: 90 km covered in 1.5 hours\n"
        "- Leg 3: 40 km covered in 1 hour\n\n"
        "1. Calculate the speed for each leg.\n"
        "2. Identify which leg was the fastest (had the steepest slope on a distance-time graph)."
    )
    s1 = 50
    s2 = 90 / 1.5 # 60
    s3 = 40
    sol = (
        f"**Step 1:** Calculate speeds:\n"
        f"- Leg 1: $\\frac{{50}}{{1}} = 50\\text{{ km/h}}$\n"
        f"- Leg 2: $\\frac{{90}}{{1.5}} = 60\\text{{ km/h}}$\n"
        f"- Leg 3: $\\frac{{40}}{{1}} = 40\\text{{ km/h}}$\n\n"
        f"**Step 2:** **Leg 2** was the fastest ({s2} km/h)."
    )
    ans = f"1. Leg 1: 50 km/h, Leg 2: 60 km/h, Leg 3: 40 km/h; 2. Leg 2 was the fastest."
    return {
        "id": f"g7_graph_20_{rng.randint(100000, 999999)}",
        "subskill": "20_distance_time_graph_fastest_leg_comparison",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_graphs_20",
        "hints": {
            "tier_1": "Calculate speed = distance / time for each leg.",
            "tier_2": "Compare the 3 speed values.",
            "tier_3": ans
        },
        "misconception_tags": ["longest_distance_assumed_fastest"]
    }


# 21. Distance-time graph return journey
def arch_21_distance_time_graph_return_journey(rng: random.Random) -> Dict[str, Any]:
    peak_d = rng.choice([60, 80, 100, 120])
    svg = _svg_graph(
        x_label="Time (hours)",
        y_label="Distance from Home (km)",
        path_d="M 60 200 L 210 60 L 360 200",
        points=[(210, 60)],
        x_ticks=[(60, "0"), (210, "2"), (360, "4")],
        y_ticks=[(200, "0"), (130, f"{peak_d//2}"), (60, f"{peak_d}")]
    )
    prompt = (
        "The graph illustrates a cyclist leaving home, reaching a destination, and immediately returning home.\n\n"
        "1. What was the maximum distance the cyclist was from home?\n"
        "2. What does the downward-sloping line from hour 2 to hour 4 represent?"
    )
    sol = (
        f"**Step 1:** The peak of the graph is at **{peak_d} km**.\n\n"
        "**Step 2:** The downward slope shows that distance from home is decreasing, meaning the cyclist is **traveling back towards home**."
    )
    ans = f"1. {peak_d} km; 2. Returning back home (distance from home is decreasing)."
    return {
        "id": f"g7_graph_21_{rng.randint(100000, 999999)}",
        "subskill": "21_distance_time_graph_return_journey",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Maximum Distance", "body": f"Peak distance is {peak_d} km at t = 2 hours."},
                {"title": "Return Leg", "body": "Returning to y = 0 means returning home."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_21",
        "hints": {
            "tier_1": "What is the highest point reached?",
            "tier_2": "Distance going down to 0 means arriving back where you started.",
            "tier_3": ans
        },
        "misconception_tags": ["downward_slope_confused_with_reversing_direction"]
    }


# 22. Water tank filling constant flow cylinder
def arch_22_water_tank_filling_constant_flow_cylinder(rng: random.Random) -> Dict[str, Any]:
    rate = rng.choice([4, 5, 6, 8])
    svg = _svg_graph(
        x_label="Time (minutes)",
        y_label="Water Height (cm)",
        path_d="M 60 200 L 360 60",
        x_ticks=[(60, "0"), (210, "5"), (360, "10")],
        y_ticks=[(200, "0"), (130, f"{5*rate}"), (60, f"{10*rate}")]
    )
    prompt = (
        f"A cylindrical tank with straight vertical sides is filled with water at a constant rate of {rate} litres per minute.\n\n"
        "1. Describe the shape of the graph of water height versus time (straight line or curve).\n"
        "2. Explain why the water height rises at a constant rate."
    )
    sol = (
        "**Step 1:** The graph will be a **straight line**.\n\n"
        "**Step 2:** Because the cylinder has a constant cross-sectional area (the sides are straight and vertical) "
        "and water enters at a constant rate, every litre of water adds the exact same height increase."
    )
    ans = "1. A straight line; 2. The cross-sectional width is constant, so each unit of water adds equal height."
    return {
        "id": f"g7_graph_22_{rng.randint(100000, 999999)}",
        "subskill": "22_water_tank_filling_constant_flow_cylinder",
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
        "learning_objective_id": "math_g7_graphs_22",
        "hints": {
            "tier_1": "Does a cylinder get wider or stay the same width?",
            "tier_2": "Constant width + constant inflow = straight line.",
            "tier_3": ans
        },
        "misconception_tags": ["cylindrical_filling_curve_misconception"]
    }


# 23. Water tank filling cone or funnel
def arch_23_water_tank_filling_cone_or_funnel(rng: random.Random) -> Dict[str, Any]:
    max_h = rng.choice([30, 40, 50, 60])
    svg = _svg_graph(
        x_label="Time (seconds)",
        y_label="Water Height (cm)",
        path_d="M 60 200 Q 140 70 360 60",
        x_ticks=[(60, "0"), (210, "10"), (360, "20")],
        y_ticks=[(200, "0"), (60, f"{max_h}")]
    )
    prompt = (
        f"A funnel-shaped vase (height {max_h} cm, narrow at the bottom and wide at the top) is filled with water at a constant flow rate.\n\n"
        "1. Does the water level rise faster at the beginning or at the end?\n"
        "2. Describe the shape of the graph of water height versus time."
    )
    sol = (
        "**Step 1:** The water level rises **faster at the beginning** (when the container is narrow) and **slower at the end** (when it is wide).\n\n"
        "**Step 2:** The graph will be a **curve that starts steep and gradually flattens out**."
    )
    ans = "1. Faster at the beginning; 2. A curve that starts steep and becomes flatter."
    return {
        "id": f"g7_graph_23_{rng.randint(100000, 999999)}",
        "subskill": "23_water_tank_filling_cone_or_funnel",
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
        "learning_objective_id": "math_g7_graphs_23",
        "hints": {
            "tier_1": "A narrow container fills up faster in height than a wide one.",
            "tier_2": "Starts steep, then becomes flatter as the width increases.",
            "tier_3": ans
        },
        "misconception_tags": ["cone_filling_linearity_assumption"]
    }


# 24. Water tank filling stepped cylinder bottle
def arch_24_water_tank_filling_stepped_cylinder_bottle(rng: random.Random) -> Dict[str, Any]:
    t_end = rng.choice([14, 15, 16, 18])
    neck_dur = t_end - 10
    svg = _svg_graph(
        x_label="Time (seconds)",
        y_label="Water Height (cm)",
        path_d="M 60 200 L 210 130 L 360 40",
        points=[(210, 130)],
        x_ticks=[(60, "0"), (210, "10"), (360, f"{t_end}")],
        y_ticks=[(200, "0"), (130, "10"), (40, "30")]
    )
    prompt = (
        "A bottle consists of a wide lower cylinder (10 cm high) and a narrow upper neck (20 cm high). "
        "Water is poured in at a constant rate.\n\n"
        f"1. Why is the second section of the graph (from t = 10s to t = {t_end}s) steeper than the first section?\n"
        "2. How long did it take to fill the narrow neck?"
    )
    sol = (
        "**Step 1:** The narrow neck has a smaller diameter, so water height rises **much faster** (steeper slope).\n\n"
        f"**Step 2:** Filling the neck took ${t_end}\\text{{ s}} - 10\\text{{ s}} = {neck_dur}\\text{{ seconds}}$."
    )
    ans = f"1. The neck is narrower so height rises faster; 2. {neck_dur} seconds"
    return {
        "id": f"g7_graph_24_{rng.randint(100000, 999999)}",
        "subskill": "24_water_tank_filling_stepped_cylinder_bottle",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Section 1", "body": "Wide base fills slowly (gentle slope)."},
                {"title": "Section 2", "body": "Narrow neck fills fast (steep slope)."},
                {"title": "Duration", "body": f"{t_end} - 10 = {neck_dur} seconds."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_24",
        "hints": {
            "tier_1": "Narrow tubes fill faster.",
            "tier_2": f"Subtract: {t_end} - 10 = {neck_dur} seconds.",
            "tier_3": ans
        },
        "misconception_tags": ["stepped_container_misinterpretation"]
    }


# 25. Water tank emptying graph interpretation
def arch_25_water_tank_emptying_graph_interpretation(rng: random.Random) -> Dict[str, Any]:
    vol = rng.choice([500, 600, 800, 1000])
    time_min = rng.choice([20, 25, 40, 50])
    rate = vol // time_min
    svg = _svg_graph(
        x_label="Time (minutes)",
        y_label="Volume in Tank (litres)",
        path_d="M 60 60 L 360 200",
        x_ticks=[(60, "0"), (210, f"{time_min//2}"), (360, f"{time_min}")],
        y_ticks=[(200, "0"), (130, f"{vol//2}"), (60, f"{vol}")]
    )
    prompt = (
        f"A storage tank contains {vol} litres of water. A drainage valve is opened at t = 0.\n\n"
        f"1. How long does it take for the tank to empty completely?\n"
        f"2. Calculate the rate at which water is draining from the tank in litres per minute."
    )
    sol = (
        f"**Step 1:** The volume reaches 0 litres at **{time_min} minutes**.\n\n"
        f"**Step 2:** Rate of drainage = $\\frac{{{vol}\\text{{ litres}}}}{{{time_min}\\text{{ min}}}} = {rate}\\text{{ litres/min}}$."
    )
    ans = f"1. {time_min} minutes; 2. {rate} litres/min"
    return {
        "id": f"g7_graph_25_{rng.randint(100000, 999999)}",
        "subskill": "25_water_tank_emptying_graph_interpretation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"diagram_type": "inline_svg", "svg": svg},
        "diagram_and_steps": {
            "diagram": {"diagram_type": "inline_svg", "svg": svg},
            "steps": [
                {"title": "Empty Point", "body": f"The line hits y = 0 at t = {time_min} min."},
                {"title": "Drainage Rate", "body": f"{vol} / {time_min} = {rate} L/min."}
            ]
        },
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_graphs_25",
        "hints": {
            "tier_1": "Find where volume reaches zero on the x-axis.",
            "tier_2": f"Divide total volume ({vol}) by total time ({time_min}).",
            "tier_3": ans
        },
        "misconception_tags": ["negative_slope_drainage_rate_confusion"]
    }

DEFAULT_DIAGRAM_META = {'diagram_role': 'context'}
