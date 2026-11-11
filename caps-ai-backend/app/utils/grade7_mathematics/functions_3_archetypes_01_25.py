"""Grade 7 Mathematics - Functions and Relationships 3: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/02. Functions and relationships 3.md
Focus: Cartesian coordinates, ordered pairs, rate of change (gradient), intercepts, linear vs non-linear, and line equations.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _svg_graph_line(
    title: str = "",
    x_range: tuple = (0, 6),
    y_range: tuple = (0, 12),
    line_pts: Optional[List[tuple]] = None,
    highlight_pts: Optional[List[tuple]] = None,
    width: int = 320,
    height: int = 240,
) -> str:
    """Renders a clean static 2D Cartesian coordinate grid with axes, gridlines, and optional plotted line/points."""
    # margins: left=40, right=20, top=25, bottom=35
    w_plot = width - 60
    h_plot = height - 60
    
    x_min, x_max = x_range
    y_min, y_max = y_range
    
    def to_screen(x: float, y: float) -> tuple:
        sx = 40 + ((x - x_min) / (x_max - x_min)) * w_plot
        sy = (height - 35) - ((y - y_min) / (y_max - y_min)) * h_plot
        return sx, sy

    elements = []
    # Title
    if title:
        elements.append(f'<text x="{width/2}" y="18" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>')
    
    # Grid lines
    for gx in range(int(x_min), int(x_max) + 1):
        sx, _ = to_screen(gx, 0)
        elements.append(f'<line x1="{sx}" y1="25" x2="{sx}" y2="{height-35}" stroke="#e2e8f0" stroke-width="1"/>')
        elements.append(f'<text x="{sx}" y="{height-20}" font-family="sans-serif" font-size="10" fill="#64748b" text-anchor="middle">{gx}</text>')
        
    for gy in range(int(y_min), int(y_max) + 1, max(1, (y_max - y_min) // 5)):
        _, sy = to_screen(0, gy)
        elements.append(f'<line x1="40" y1="{sy}" x2="{width-20}" y2="{sy}" stroke="#e2e8f0" stroke-width="1"/>')
        elements.append(f'<text x="32" y="{sy+3}" font-family="sans-serif" font-size="10" fill="#64748b" text-anchor="end">{gy}</text>')
        
    # Axes
    ox, oy = to_screen(0, 0)
    elements.append(f'<line x1="40" y1="{oy}" x2="{width-15}" y2="{oy}" stroke="#1e293b" stroke-width="2"/>') # x-axis
    elements.append(f'<polygon points="{width-15},{oy-3} {width-8},{oy} {width-15},{oy+3}" fill="#1e293b"/>')
    elements.append(f'<line x1="{ox}" y1="{height-35}" x2="{ox}" y2="20" stroke="#1e293b" stroke-width="2"/>') # y-axis
    elements.append(f'<polygon points="{ox-3},20 {ox},13 {ox+3},20" fill="#1e293b"/>')
    
    # Axis labels
    elements.append(f'<text x="{width-10}" y="{oy+16}" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">x</text>')
    elements.append(f'<text x="{ox-10}" y="16" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">y</text>')

    # Plotted line
    if line_pts and len(line_pts) >= 2:
        pts_str = " ".join(f"{to_screen(x, y)[0]:.1f},{to_screen(x, y)[1]:.1f}" for x, y in line_pts)
        elements.append(f'<polyline points="{pts_str}" fill="none" stroke="#2563eb" stroke-width="2.5"/>')
        
    # Plotted dots
    if highlight_pts:
        for px, py in highlight_pts:
            sx, sy = to_screen(px, py)
            elements.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="4" fill="#dc2626" stroke="#ffffff" stroke-width="1.5"/>')
            
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="auto" style="background-color:#ffffff; max-width:{width}px;">'
        f'{"".join(elements)}'
        f'</svg>'
    )


# 01. Cartesian ordered pairs from linear rule
def arch_01_cartesian_ordered_pairs_from_linear_rule(rng: random.Random) -> Dict[str, Any]:
    # y = 2x + 1 for x in 0, 1, 2, 3 -> (0, 1), (1, 3), (2, 5), (3, 7)
    ans = "(0; 1), (1; 3), (2; 5), (3; 7)"
    prompt = (
        "Consider the function rule \\(y = 2x + 1\\).\n\n"
        "Write the coordinates as ordered pairs \\((x; y)\\) for input values \\(x = 0, 1, 2, 3\\)."
    )
    sol = (
        "**Step 1:** Calculate each output value \\(y\\):\n"
        "- For \\(x = 0\\): \\(y = 2(0) + 1 = 1 \\implies (0; 1)\\)\n"
        "- For \\(x = 1\\): \\(y = 2(1) + 1 = 3 \\implies (1; 3)\\)\n"
        "- For \\(x = 2\\): \\(y = 2(2) + 1 = 5 \\implies (2; 5)\\)\n"
        "- For \\(x = 3\\): \\(y = 2(3) + 1 = 7 \\implies (3; 7)\\)\n\n"
        "**Ordered Pairs:** **(0; 1), (1; 3), (2; 5), (3; 7)**"
    )
    return {
        "id": f"g7_fn3_01_{rng.randint(100000, 999999)}",
        "subskill": "01_cartesian_ordered_pairs_from_linear_rule",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_01",
        "hints": {"tier_1": "Calculate y for each x, then format as (x; y).", "tier_2": "Outputs are 1, 3, 5, 7.", "tier_3": ans},
        "misconception_tags": ["swapping_x_and_y_in_ordered_pair"]
    }


# 02. Cartesian identifying x and y coordinates
def arch_02_cartesian_identifying_x_and_y_coordinates(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the Cartesian coordinate pair \\(P(4; 9)\\):\n\n"
        "1. Which number represents the \\(x\\)-coordinate (horizontal displacement)?\n"
        "2. Which number represents the \\(y\\)-coordinate (vertical displacement)?"
    )
    sol = (
        "**Step 1:** Coordinates are universally written in the standard form \\((x; y)\\).\n\n"
        "**Summary:** 1. \\(x = 4\\); 2. \\(y = 9\\)"
    )
    ans = "1. 4; 2. 9"
    return {
        "id": f"g7_fn3_02_{rng.randint(100000, 999999)}",
        "subskill": "02_cartesian_identifying_x_and_y_coordinates",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn3_02",
        "hints": {"tier_1": "First number is x, second is y.", "tier_2": "x = 4, y = 9.", "tier_3": ans},
        "misconception_tags": ["coordinate_order_confusion"]
    }


# 03. Cartesian plotting points first quadrant
def arch_03_cartesian_plotting_points_first_quadrant(rng: random.Random) -> Dict[str, Any]:
    px = rng.choice([2, 3, 4, 5])
    py = rng.choice([3, 4, 5, 6, 7])
    svg = _svg_graph_line(f"Point A({px}; {py}) Plotted", x_range=(0, 6), y_range=(0, 8), highlight_pts=[(px, py)])
    ans = f"({px}; {py})"
    prompt = (
        f"Read the coordinates of the highlighted red point A from the coordinate plane:"
    )
    sol = (
        f"**Step 1:** Move along the horizontal \\(x\\)-axis to find {px}.\n\n"
        f"**Step 2:** Move vertically up to read the value on the \\(y\\)-axis: {py}.\n\n"
        f"**Coordinates:** **({px}; {py})**"
    )
    return {
        "id": f"g7_fn3_03_{rng.randint(100000, 999999)}",
        "subskill": "03_cartesian_plotting_points_first_quadrant",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn3_03",
        "hints": {"tier_1": "Read along the horizontal axis first, then vertical.", "tier_2": f"x = {px}, y = {py}.", "tier_3": ans},
        "misconception_tags": ["reading_y_before_x"]
    }


# 04. Cartesian points with negative coordinates
def arch_04_cartesian_points_with_negative_coordinates(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A point has coordinates \\(Q(-3; 5)\\).\n\n"
        "Describe where point \\(Q\\) is located relative to the origin \\((0; 0)\\):\n"
        "How many units to the left/right, and how many units up/down?"
    )
    sol = (
        "**Step 1:** The \\(x\\)-coordinate is \\(-3\\), which indicates **3 units to the left** of the origin.\n\n"
        "**Step 2:** The \\(y\\)-coordinate is \\(+5\\), which indicates **5 units upwards** from the origin.\n\n"
        "**Summary:** 3 units left, 5 units up (Quadrant II)."
    )
    ans = "3 units left and 5 units up"
    return {
        "id": f"g7_fn3_04_{rng.randint(100000, 999999)}",
        "subskill": "04_cartesian_points_with_negative_coordinates",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_04",
        "hints": {"tier_1": "Negative x means left, positive y means up.", "tier_2": "3 left, 5 up.", "tier_3": ans},
        "misconception_tags": ["quadrant_direction_sign_error"]
    }


# 05. Cartesian points on axes intercepts
def arch_05_cartesian_points_on_axes_intercepts(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "1. Where does the point \\((0; 7)\\) lie on the Cartesian plane?\n"
        "2. Where does the point \\((5; 0)\\) lie?"
    )
    sol = (
        "**Step 1:** At \\((0; 7)\\), \\(x = 0\\), so the point lies on the **\\(y\\)-axis** (at \\(y = 7\\)).\n\n"
        "**Step 2:** At \\((5; 0)\\), \\(y = 0\\), so the point lies on the **\\(x\\)-axis** (at \\(x = 5\\)).\n\n"
        "**Summary:** 1. On the y-axis; 2. On the x-axis"
    )
    ans = "1. y-axis; 2. x-axis"
    return {
        "id": f"g7_fn3_05_{rng.randint(100000, 999999)}",
        "subskill": "05_cartesian_points_on_axes_intercepts",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_05",
        "hints": {"tier_1": "If x=0 it is on the y-axis; if y=0 it is on the x-axis.", "tier_2": "1. y-axis; 2. x-axis.", "tier_3": ans},
        "misconception_tags": ["axis_intercept_identification_confusion"]
    }


# 06. Rate of change gradient from two points
def arch_06_rate_of_change_gradient_from_two_points(rng: random.Random) -> Dict[str, Any]:
    # (1, 4) and (3, 10) -> (10 - 4)/(3 - 1) = 6/2 = 3
    ans = "3"
    prompt = (
        "A line passes through the points \\(A(1; 4)\\) and \\(B(3; 10)\\).\n\n"
        "Calculate the constant rate of change (gradient) between these two points:\n"
        "\\[ \\text{Rate of Change} = \\frac{\\text{Change in } y}{\\text{Change in } x} \\]"
    )
    sol = (
        "**Step 1:** Change in \\(y\\): $$10 - 4 = 6$$\n\n"
        "**Step 2:** Change in \\(x\\): $$3 - 1 = 2$$\n\n"
        "**Step 3:** Calculate rate of change:\n"
        "$$\\text{Rate} = \\frac{6}{2} = \\mathbf{3}$$"
    )
    return {
        "id": f"g7_fn3_06_{rng.randint(100000, 999999)}",
        "subskill": "06_rate_of_change_gradient_from_two_points",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_06",
        "hints": {"tier_1": "Divide (10 - 4) by (3 - 1).", "tier_2": "6 / 2 = 3.", "tier_3": ans},
        "misconception_tags": ["inverting_gradient_formula_delta_x_over_delta_y"]
    }


# 07. Rate of change gradient from table
def arch_07_rate_of_change_gradient_from_table(rng: random.Random) -> Dict[str, Any]:
    # Table: x: 2, 4, 6 -> y: 7, 13, 19. dy = 6, dx = 2 -> rate = 3
    ans = "3"
    table_md = (
        "| \\(x\\) | 2 | 4 | 6 |\n"
        "| :--- | :---: | :---: | :---: |\n"
        "| \\(y\\) | 7 | 13 | 19 |\n"
    )
    prompt = (
        f"Notice that the \\(x\\)-values in this table increase by 2:\n\n{table_md}\n"
        f"Calculate the rate of change per unit of \\(x\\) (\\(\\frac{{\\Delta y}}{{\\Delta x}}\\))."
    )
    sol = (
        "**Step 1:** Find change in \\(y\\): $$13 - 7 = 6$$\n\n"
        "**Step 2:** Find change in \\(x\\): $$4 - 2 = 2$$\n\n"
        "**Step 3:** Divide to find rate per unit:\n"
        "$$\\frac{\\Delta y}{\\Delta x} = \\frac{6}{2} = \\mathbf{3}$$"
    )
    return {
        "id": f"g7_fn3_07_{rng.randint(100000, 999999)}",
        "subskill": "07_rate_of_change_gradient_from_table",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_07",
        "hints": {"tier_1": "Divide change in y (6) by change in x (2).", "tier_2": "6 / 2 = 3.", "tier_3": ans},
        "misconception_tags": ["forgetting_to_divide_by_step_size_in_x"]
    }


# 08. Rate of change positive steepness comparison
def arch_08_rate_of_change_positive_steepness_comparison(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Line 1 has equation \\(y = 5x + 1\\) and Line 2 has equation \\(y = 2x + 10\\).\n\n"
        "Which line has a steeper upward slope on a Cartesian graph? Explain your reasoning."
    )
    sol = (
        "**Step 1:** In the linear form \\(y = mx + c\\), the multiplier \\(m\\) represents steepness (gradient).\n\n"
        "**Step 2:** Compare \\(m\\)-values:\n"
        "- Line 1: \\(m = 5\\)\n"
        "- Line 2: \\(m = 2\\)\n\n"
        "**Conclusion:** **Line 1** is steeper because its rate of change (5) is greater than 2."
    )
    ans = "Line 1"
    return {
        "id": f"g7_fn3_08_{rng.randint(100000, 999999)}",
        "subskill": "08_rate_of_change_positive_steepness_comparison",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_08",
        "hints": {"tier_1": "Look at the coefficient of x.", "tier_2": "5 is greater than 2.", "tier_3": ans},
        "misconception_tags": ["confusing_y_intercept_with_steepness"]
    }


# 09. Rate of change negative downward slope
def arch_09_rate_of_change_negative_downward_slope(rng: random.Random) -> Dict[str, Any]:
    # (0, 10) and (2, 4) -> (4 - 10)/(2 - 0) = -6/2 = -3
    ans = "-3"
    prompt = (
        "A line slants downwards from left to right, passing through \\((0; 10)\\) and \\((2; 4)\\).\n\n"
        "Calculate the gradient of this downward sloping line."
    )
    sol = (
        "**Step 1:** Change in \\(y\\): $$4 - 10 = -6$$\n\n"
        "**Step 2:** Change in \\(x\\): $$2 - 0 = 2$$\n\n"
        "**Step 3:** Gradient:\n"
        "$$m = \\frac{-6}{2} = \\mathbf{-3}$$"
    )
    return {
        "id": f"g7_fn3_09_{rng.randint(100000, 999999)}",
        "subskill": "09_rate_of_change_negative_downward_slope",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_09",
        "hints": {"tier_1": "Subtract in the same order: (4 - 10) / (2 - 0).", "tier_2": "-6 / 2 = -3.", "tier_3": ans},
        "misconception_tags": ["dropping_negative_sign_in_negative_slope"]
    }


# 10. Rate of change horizontal line zero gradient
def arch_10_rate_of_change_horizontal_line_zero_gradient(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A straight line on a graph has the equation \\(y = 4\\) for all values of \\(x\\).\n\n"
        "1. What is the gradient (rate of change) of this horizontal line?\n"
        "2. Does the output value change as \\(x\\) increases?"
    )
    sol = (
        "**Step 1:** The line is completely flat and horizontal.\n"
        "$$\\Delta y = 0 \\implies m = \\frac{0}{\\Delta x} = \\mathbf{0}$$\n\n"
        "**Step 2:** No, the output value is constant at 4.\n\n"
        "**Summary:** 1. 0; 2. No"
    )
    ans = "1. 0; 2. No"
    return {
        "id": f"g7_fn3_10_{rng.randint(100000, 999999)}",
        "subskill": "10_rate_of_change_horizontal_line_zero_gradient",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_10",
        "hints": {"tier_1": "A horizontal line has zero vertical rise.", "tier_2": "Gradient is 0.", "tier_3": ans},
        "misconception_tags": ["confusing_zero_gradient_with_undefined"]
    }


# 11. Graph line equation matching given graph
def arch_11_graph_line_equation_matching_given_graph(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3])
    c = rng.randint(1, 4)
    y_end = m * 5 + c
    svg = _svg_graph_line("Graph of a Linear Function", x_range=(0, 5), y_range=(0, y_end + 2), line_pts=[(0, c), (5, y_end)])
    ans = f"y = {m}x + {c}"
    prompt = (
        f"Examine the linear graph:\n\n"
        f"Determine the equation of this straight line in the form \\(y = mx + c\\)."
    )
    sol = (
        f"**Step 1: Identify \\(y\\)-intercept \\(c\\):**\n"
        f"The line crosses the \\(y\\)-axis at \\((0; {c})\\), so \\(c = {c}\\).\n\n"
        f"**Step 2: Calculate gradient \\(m\\):**\n"
        f"Between \\((0; {c})\\) and \\((5; {y_end})\\):\n"
        f"$$m = \\frac{{{y_end} - {c}}}{{5 - 0}} = \\frac{{{y_end - c}}}{{5}} = {m}$$\n\n"
        f"**Equation:** **\\(y = {m}x + {c}\\)**"
    )
    return {
        "id": f"g7_fn3_11_{rng.randint(100000, 999999)}",
        "subskill": "11_graph_line_equation_matching_given_graph",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn3_11",
        "hints": {"tier_1": f"Find where the line crosses y-axis (c = {c}).", "tier_2": f"Gradient is rise / run = {y_end - c} / 5 = {m}.", "tier_3": ans},
        "misconception_tags": ["swapping_m_and_c_in_line_equation"]
    }


# 12. Graph identifying y intercept from graph
def arch_12_graph_identifying_y_intercept_from_graph(rng: random.Random) -> Dict[str, Any]:
    c = rng.randint(2, 7)
    svg = _svg_graph_line("Linear Graph", x_range=(0, 6), y_range=(0, c + 7), line_pts=[(0, c), (6, c + 6)])
    ans = f"(0; {c})"
    prompt = (
        f"State the coordinates of the **\\(y\\)-intercept** for the plotted line:"
    )
    sol = (
        f"**Step 1:** The \\(y\\)-intercept is the point where the line crosses the vertical \\(y\\)-axis (where \\(x = 0\\)).\n\n"
        f"**Step 2:** Reading the graph at \\(x = 0\\), the line crosses at \\(y = {c}\\).\n\n"
        f"**Coordinates:** **({0}; {c})**"
    )
    return {
        "id": f"g7_fn3_12_{rng.randint(100000, 999999)}",
        "subskill": "12_graph_identifying_y_intercept_from_graph",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn3_12",
        "hints": {"tier_1": "Look at where the line hits the vertical axis.", "tier_2": f"Point is (0; {c}).", "tier_3": ans},
        "misconception_tags": ["reading_x_intercept_instead_of_y_intercept"]
    }


# 13. Graph identifying x intercept where y is zero
def arch_13_graph_identifying_x_intercept_where_y_is_zero(rng: random.Random) -> Dict[str, Any]:
    # Line y = 2x - 6. Crossing y=0 at 2x = 6 -> x = 3
    ans = "(3; 0)"
    prompt = (
        "A straight line has the algebraic rule \\(y = 2x - 6\\).\n\n"
        "Find the coordinates of the \\(x\\)-intercept (where \\(y = 0\\))."
    )
    sol = (
        "**Step 1:** Set \\(y = 0\\) in the equation:\n"
        "$$0 = 2x - 6$$\n\n"
        "**Step 2:** Solve for \\(x\\):\n"
        "$$2x = 6 \\implies x = 3$$\n\n"
        "**Coordinates:** **(3; 0)**"
    )
    return {
        "id": f"g7_fn3_13_{rng.randint(100000, 999999)}",
        "subskill": "13_graph_identifying_x_intercept_where_y_is_zero",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_13",
        "hints": {"tier_1": "Set y = 0 and solve 2x - 6 = 0.", "tier_2": "x = 3.", "tier_3": ans},
        "misconception_tags": ["setting_x_to_zero_for_x_intercept"]
    }


# 14. Graph linear vs curved non linear distinction
def arch_14_graph_linear_vs_curved_non_linear_distinction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner graphs two equations:\n"
        "- Graph A: \\(y = 3x - 1\\)\n"
        "- Graph B: \\(y = x^2\\)\n\n"
        "Which of these will produce a perfectly straight line graph and which will produce a curved line? Explain."
    )
    sol = (
        "**Step 1:** Graph A has \\(x\\) to the first power (degree 1) with a constant rate of change (3), "
        "so **Graph A is a straight line (linear)**.\n\n"
        "**Step 2:** Graph B has \\(x^2\\) (degree 2), meaning the rate of change increases with \\(x\\), "
        "so **Graph B produces a curve / parabola (non-linear)**."
    )
    ans = "Graph A is straight; Graph B is curved"
    return {
        "id": f"g7_fn3_14_{rng.randint(100000, 999999)}",
        "subskill": "14_graph_linear_vs_curved_non_linear_distinction",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_14",
        "hints": {"tier_1": "Degree 1 gives straight lines; powers like x² curve.", "tier_2": "A is straight, B is curved.", "tier_3": ans},
        "misconception_tags": ["assuming_all_functions_produce_straight_lines"]
    }


# 15. Graph discrete vs continuous data points
def arch_15_graph_discrete_vs_continuous_data_points(rng: random.Random) -> Dict[str, Any]:
    price = rng.choice([2, 3, 4])
    pts = [(i, i * price) for i in range(1, 5)]
    svg = _svg_graph_line(f"Discrete Dots (R{price} per item)", x_range=(0, 5), y_range=(0, 5 * price), highlight_pts=pts)
    prompt = (
        "Explain whether the plotted points should be joined with a continuous line or left as separate dots:\n\n"
        "1. A plot of the number of soccer balls sold and total cost in Rand.\n"
        "2. A plot of time elapsed and water temperature heating from 20°C to 100°C."
    )
    sol = (
        "**Step 1: Situation 1 (Soccer balls):**\n"
        "Soccer balls are discrete count items (you cannot buy 2,3 balls). Therefore, the points should be left as **separate dots (discrete)**.\n\n"
        "**Step 2: Situation 2 (Water temperature):**\n"
        "Temperature and time vary continuously through every real decimal value. Therefore, points must be joined with a **continuous solid line**."
    )
    ans = "1. Separate dots (discrete); 2. Continuous line"
    return {
        "id": f"g7_fn3_15_{rng.randint(100000, 999999)}",
        "subskill": "15_graph_discrete_vs_continuous_data_points",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_15",
        "hints": {"tier_1": "Can you have fractional soccer balls? Can time be continuous?", "tier_2": "1. Discrete dots; 2. Continuous line.", "tier_3": ans},
        "misconception_tags": ["joining_discrete_points_with_continuous_lines"]
    }


# 16. Graph table formula three way matching
def arch_16_graph_table_formula_three_way_matching(rng: random.Random) -> Dict[str, Any]:
    # Table: (1, 5), (2, 8), (3, 11). Rule: y = 3x + 2
    ans = "y = 3x + 2"
    prompt = (
        "A line passes through coordinates \\((1; 5)\\), \\((2; 8)\\), and \\((3; 11)\\).\n\n"
        "Which of the following formulae generated these coordinates?\n"
        "A) \\(y = 2x + 3\\)\n"
        "B) \\(y = 3x + 2\\)\n"
        "C) \\(y = 4x + 1\\)"
    )
    sol = (
        "**Step 1:** Calculate rate of change:\n"
        "$$m = 8 - 5 = 3$$\n\n"
        "**Step 2:** Test formula B (\\(y = 3x + 2\\)):\n"
        "- \\(x = 1 \\implies 3(1) + 2 = 5\\) (matches)\n"
        "- \\(x = 2 \\implies 3(2) + 2 = 8\\) (matches)\n"
        "- \\(x = 3 \\implies 3(3) + 2 = 11\\) (matches)\n\n"
        "**Correct Choice:** **B (y = 3x + 2)**"
    )
    return {
        "id": f"g7_fn3_16_{rng.randint(100000, 999999)}",
        "subskill": "16_graph_table_formula_three_way_matching",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_16",
        "hints": {"tier_1": "Check which formula produces 5 for x=1 and 8 for x=2.", "tier_2": "3(1) + 2 = 5.", "tier_3": ans},
        "misconception_tags": ["formula_verification_slip"]
    }


# 17. Graph determining if point lies on line
def arch_17_graph_determining_if_point_lies_on_line(rng: random.Random) -> Dict[str, Any]:
    # Line y = 4x - 1. Does point (5, 19) lie on it? 4(5) - 1 = 19 -> Yes!
    ans = "Yes, because 4(5) - 1 = 19"
    prompt = (
        "Does the point \\((5; 19)\\) lie on the straight line with equation \\(y = 4x - 1\\)?\n\n"
        "Show substitution into the equation to justify your answer."
    )
    sol = (
        "**Step 1:** Substitute \\(x = 5\\) into the right-hand side:\n"
        "$$\\text{RHS} = 4(5) - 1 = 20 - 1 = 19$$\n\n"
        "**Step 2:** Compare with given \\(y\\)-coordinate:\n"
        "$$\\text{LHS} = 19$$\n"
        "Since \\(\\text{LHS} = \\text{RHS}\\), the point **does lie on the line**."
    )
    return {
        "id": f"g7_fn3_17_{rng.randint(100000, 999999)}",
        "subskill": "17_graph_determining_if_point_lies_on_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_17",
        "hints": {"tier_1": "Evaluate 4(5) - 1.", "tier_2": "4(5) - 1 = 19.", "tier_3": ans},
        "misconception_tags": ["algebraic_point_verification_misconception"]
    }


# 18. Graph finding missing coordinate on line
def arch_18_graph_finding_missing_coordinate_on_line(rng: random.Random) -> Dict[str, Any]:
    # Line y = 3x + 5. Point (k, 26) -> 3k + 5 = 26 -> 3k = 21 -> k = 7
    ans = "7"
    prompt = (
        "A point \\((k; 26)\\) lies on the line \\(y = 3x + 5\\).\n\n"
        "Calculate the missing \\(x\\)-coordinate, \\(k\\)."
    )
    sol = (
        "**Step 1:** Substitute the coordinates into the line equation:\n"
        "$$26 = 3k + 5$$\n\n"
        "**Step 2:** Subtract 5:\n"
        "$$3k = 26 - 5 = 21$$\n\n"
        "**Step 3:** Divide by 3:\n"
        "$$k = \\frac{21}{3} = \\mathbf{7}$$"
    )
    return {
        "id": f"g7_fn3_18_{rng.randint(100000, 999999)}",
        "subskill": "18_graph_finding_missing_coordinate_on_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_18",
        "hints": {"tier_1": "Solve 3k + 5 = 26.", "tier_2": "3k = 21.", "tier_3": ans},
        "misconception_tags": ["reverse_coordinate_solution_slip"]
    }


# 19. Graph parallel lines equal rate of change
def arch_19_graph_parallel_lines_equal_rate_of_change(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Two lines have equations:\n"
        "- Line A: \\(y = 4x + 3\\)\n"
        "- Line B: \\(y = 4x - 7\\)\n\n"
        "Explain why these two lines will never intersect (are parallel) on a Cartesian plane."
    )
    sol = (
        "**Step 1:** Compare their gradients (rate of change):\n"
        "Both lines have gradient \\(m = 4\\).\n\n"
        "**Step 2:** Compare their \\(y\\)-intercepts:\n"
        "Line A has \\(c = 3\\) and Line B has \\(c = -7\\) (different intercepts).\n\n"
        "**Conclusion:**\n"
        "Lines with the exact same gradient have identical steepness and therefore remain a constant distance apart, "
        "making them **parallel**."
    )
    ans = "They have the same gradient (m = 4)"
    return {
        "id": f"g7_fn3_19_{rng.randint(100000, 999999)}",
        "subskill": "19_graph_parallel_lines_equal_rate_of_change",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_19",
        "hints": {"tier_1": "What geometric property makes lines parallel?", "tier_2": "Equal gradients / rate of change.", "tier_3": ans},
        "misconception_tags": ["parallel_lines_gradient_property_misunderstanding"]
    }


# 20. Graph intersecting lines point of intersection
def arch_20_graph_intersecting_lines_point_of_intersection(rng: random.Random) -> Dict[str, Any]:
    # Line 1: y = x + 3. Line 2: y = 2x. Intersection at x+3 = 2x -> x = 3, y = 6 -> (3, 6)
    ans = "(3; 6)"
    prompt = (
        "Find the point of intersection \\((x; y)\\) for the two lines:\n"
        "- Line 1: \\(y = x + 3\\)\n"
        "- Line 2: \\(y = 2x\\)"
    )
    sol = (
        "**Step 1:** Set equations equal to each other:\n"
        "$$2x = x + 3$$\n\n"
        "**Step 2:** Solve for \\(x\\):\n"
        "$$2x - x = 3 \\implies x = 3$$\n\n"
        "**Step 3:** Find \\(y\\) using Line 2:\n"
        "$$y = 2(3) = 6$$\n\n"
        "**Intersection Point:** **(3; 6)**"
    )
    return {
        "id": f"g7_fn3_20_{rng.randint(100000, 999999)}",
        "subskill": "20_graph_intersecting_lines_point_of_intersection",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_20",
        "hints": {"tier_1": "Set x + 3 = 2x.", "tier_2": "x = 3, then y = 2(3) = 6.", "tier_3": ans},
        "misconception_tags": ["simultaneous_intersection_slip"]
    }


# 21. Graph direct proportion line through origin
def arch_21_graph_direct_proportion_line_through_origin(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "State two visual conditions that must be met for a graph to represent a **directly proportional relationship**."
    )
    sol = (
        "**Conditions for Direct Proportion Graph:**\n"
        "1. The graph must be a **straight line** (constant gradient).\n"
        "2. The line must pass through the **origin** \\((0; 0)\\)."
    )
    ans = "1. Straight line; 2. Passes through origin (0; 0)"
    return {
        "id": f"g7_fn3_21_{rng.randint(100000, 999999)}",
        "subskill": "21_graph_direct_proportion_line_through_origin",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_21",
        "hints": {"tier_1": "What shape is it, and what special point does it pass through?", "tier_2": "Straight line through (0; 0).", "tier_3": ans},
        "misconception_tags": ["omitting_origin_requirement_for_direct_proportion"]
    }


# 22. Graph reading value at given x
def arch_22_graph_reading_value_at_given_x(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3])
    x_q = rng.choice([2, 3, 4])
    y_q = m * x_q
    svg = _svg_graph_line(f"Graph of y = {m}x", x_range=(0, 5), y_range=(0, 5 * m), line_pts=[(0, 0), (5, 5 * m)], highlight_pts=[(x_q, y_q)])
    ans = str(y_q)
    prompt = (
        f"Use the plotted graph of \\(y = {m}x\\) to determine the output value when \\(x = {x_q}\\):"
    )
    sol = (
        f"**Step 1:** Locate \\(x = {x_q}\\) on the horizontal axis.\n\n"
        f"**Step 2:** Follow vertically up to meet the line.\n\n"
        f"**Step 3:** Read the corresponding horizontal value on the \\(y\\)-axis: **{y_q}**."
    )
    return {
        "id": f"g7_fn3_22_{rng.randint(100000, 999999)}",
        "subskill": "22_graph_reading_value_at_given_x",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn3_22",
        "hints": {"tier_1": f"Find {x_q} on the x-axis, then look across to the y-axis.", "tier_2": f"y = {y_q}.", "tier_3": ans},
        "misconception_tags": ["graphical_reading_alignment_error"]
    }


# 23. Graph reading value at given y
def arch_23_graph_reading_value_at_given_y(rng: random.Random) -> Dict[str, Any]:
    m = rng.choice([2, 3])
    x_q = rng.choice([2, 3, 4])
    y_q = m * x_q
    svg = _svg_graph_line("Reading Input from Graph", x_range=(0, 5), y_range=(0, 5 * m), line_pts=[(0, 0), (5, 5 * m)], highlight_pts=[(x_q, y_q)])
    ans = str(x_q)
    prompt = (
        f"Using the plotted line, find the input \\(x\\) that produces an output of \\(y = {y_q}\\):"
    )
    sol = (
        f"**Step 1:** Locate \\(y = {y_q}\\) on the vertical axis.\n\n"
        f"**Step 2:** Move horizontally across to the line.\n\n"
        f"**Step 3:** Move down to the \\(x\\)-axis to read the input: **{x_q}**."
    )
    return {
        "id": f"g7_fn3_23_{rng.randint(100000, 999999)}",
        "subskill": "23_graph_reading_value_at_given_y",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn3_23",
        "hints": {"tier_1": f"Start from y = {y_q} on the vertical axis.", "tier_2": f"Move down to x = {x_q}.", "tier_3": ans},
        "misconception_tags": ["reading_wrong_axis_first"]
    }


# 24. Graph extrapolating trend line
def arch_24_graph_extrapolating_trend_line(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain what it means to **extrapolate** a trend line on a graph.\n\n"
        "Give one reason why extrapolation beyond the tested data range must be done with caution."
    )
    sol = (
        "**Step 1: Definition of Extrapolation:**\n"
        "Extrapolation is extending the line/trend beyond the known observed data points to estimate future or unseen values.\n\n"
        "**Step 2: Caution:**\n"
        "We cannot be certain that the same pattern or linear relationship continues indefinitely in the real world "
        "(e.g., physical limits, saturation, or changing conditions)."
    )
    ans = "Extending the trend beyond known data points"
    return {
        "id": f"g7_fn3_24_{rng.randint(100000, 999999)}",
        "subskill": "24_graph_extrapolating_trend_line",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_24",
        "hints": {"tier_1": "Extra means outside or beyond.", "tier_2": "Estimating values outside the known data range.", "tier_3": ans},
        "misconception_tags": ["confusing_extrapolation_with_interpolation"]
    }


# 25. Graph interpolating between plotted points
def arch_25_graph_interpolating_between_plotted_points(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain the meaning of **interpolation** on a Cartesian graph.\n\n"
        "How is it different from extrapolation?"
    )
    sol = (
        "**Step 1: Definition of Interpolation:**\n"
        "Interpolation is estimating a value **between** two known, recorded data points inside the plotted range.\n\n"
        "**Step 2: Difference:**\n"
        "- **Interpolation:** Inside the known range (generally reliable).\n"
        "- **Extrapolation:** Outside the known range (less reliable)."
    )
    ans = "Estimating values between known recorded points"
    return {
        "id": f"g7_fn3_25_{rng.randint(100000, 999999)}",
        "subskill": "25_graph_interpolating_between_plotted_points",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_25",
        "hints": {"tier_1": "Inter means within or between.", "tier_2": "Estimating inside known data.", "tier_3": ans},
        "misconception_tags": ["interpolation_terminology_confusion"]
    }
