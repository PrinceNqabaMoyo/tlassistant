"""Grade 7 Mathematics - Functions and Relationships 3: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 3/02. Functions and relationships 3.md
Focus: Real-world graphs (distance-time, cost, temperature, conversion), narrative stories, axis scaling, speed-time, and journey autopsies.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from .functions_3_archetypes_01_25 import _svg_graph_line


# 26. Distance time graph constant speed segment
def arch_26_distance_time_graph_constant_speed_segment(rng: random.Random) -> Dict[str, Any]:
    spd = rng.choice([50, 60, 70, 80])
    hrs = 3
    dist = spd * hrs
    svg = _svg_graph_line("Distance vs Time", x_range=(0, 4), y_range=(0, dist + 40), line_pts=[(0, 0), (hrs, dist)])
    ans = f"{spd} km/h"
    prompt = (
        f"The distance-time graph represents a car journey:\n\n"
        f"Calculate the constant speed of the car in km/h."
    )
    sol = (
        "**Step 1:** In a distance-time graph, speed is represented by the gradient:\n"
        "$$\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}}$$\n\n"
        f"**Step 2:** From the graph, at \\(t = {hrs}\\text{{ h}}\\), distance = \\({dist}\\text{{ km}}\\):\n"
        f"$$\\text{{Speed}} = \\frac{{{dist}\\text{{ km}}}}{{{hrs}\\text{{ h}}}} = \\mathbf{{{spd}\\text{{ km/h}}}}$$"
    )
    return {
        "id": f"g7_fn3_26_{rng.randint(100000, 999999)}",
        "subskill": "26_distance_time_graph_constant_speed_segment",
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
        "learning_objective_id": "math_g7_fn3_26",
        "hints": {"tier_1": f"Divide total distance ({dist} km) by total time ({hrs} hours).", "tier_2": f"{dist} / {hrs} = {spd}.", "tier_3": ans},
        "misconception_tags": ["speed_formula_inversion"]
    }


# 27. Distance time graph stationary horizontal segment
def arch_27_distance_time_graph_stationary_horizontal_segment(rng: random.Random) -> Dict[str, Any]:
    d_rest = rng.choice([80, 100, 120])
    svg = _svg_graph_line("Journey with Rest Stop", x_range=(0, 6), y_range=(0, d_rest + 50), line_pts=[(0, 0), (2, d_rest), (4, d_rest), (6, d_rest + 50)])
    ans = "2 hours (stationary / resting)"
    prompt = (
        f"A cyclist's journey is plotted:\n\n"
        f"What is the cyclist doing between \\(t = 2\\) hours and \\(t = 4\\) hours, and how long does this last?"
    )
    sol = (
        f"**Step 1:** Between \\(t = 2\\) and \\(t = 4\\), the line is flat and horizontal (distance remains constant at {d_rest} km).\n\n"
        "**Step 2:** This means the cyclist has stopped moving (stationary/resting).\n\n"
        "**Step 3:** Duration: $$4 - 2 = \\mathbf{2\\text{ hours}}$$"
    )
    return {
        "id": f"g7_fn3_27_{rng.randint(100000, 999999)}",
        "subskill": "27_distance_time_graph_stationary_horizontal_segment",
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
        "learning_objective_id": "math_g7_fn3_27",
        "hints": {"tier_1": "What does a flat distance-time graph indicate?", "tier_2": "Distance is not changing: stopped for 2 hours.", "tier_3": ans},
        "misconception_tags": ["confusing_horizontal_distance_line_with_moving_at_constant_speed"]
    }


# 28. Distance time graph calculating speed
def arch_28_distance_time_graph_calculating_speed(rng: random.Random) -> Dict[str, Any]:
    # Segment from t=1 (d=30) to t=3 (d=110): speed = (110 - 30)/2 = 80/2 = 40 km/h
    ans = "40 km/h"
    prompt = (
        "On a distance-time graph, a runner travels from distance 30 km at \\(t = 1\\text{ h}\\) "
        "to distance 110 km at \\(t = 3\\text{ h}\\).\n\n"
        "Calculate the runner's speed during this interval."
    )
    sol = (
        "**Step 1:** Change in distance: $$110 - 30 = 80\\text{ km}$$\n\n"
        "**Step 2:** Change in time: $$3 - 1 = 2\\text{ hours}$$\n\n"
        "**Step 3:** Speed:\n"
        "$$\\text{Speed} = \\frac{80\\text{ km}}{2\\text{ h}} = \\mathbf{40\\text{ km/h}}$$"
    )
    return {
        "id": f"g7_fn3_28_{rng.randint(100000, 999999)}",
        "subskill": "28_distance_time_graph_calculating_speed",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_28",
        "hints": {"tier_1": "Divide change in distance (80) by change in time (2).", "tier_2": "80 / 2 = 40.", "tier_3": ans},
        "misconception_tags": ["dividing_final_distance_by_final_time_directly"]
    }


# 29. Distance time graph returning to start
def arch_29_distance_time_graph_returning_to_start(rng: random.Random) -> Dict[str, Any]:
    d_max = rng.choice([50, 60, 70, 80])
    svg = _svg_graph_line("Out-and-Back Journey", x_range=(0, 5), y_range=(0, d_max + 10), line_pts=[(0, 0), (2, d_max), (4, 0)])
    ans = "Returning home / back to the starting point"
    prompt = (
        f"A delivery van's round trip is plotted:\n\n"
        f"What does the downward-sloping section between \\(t = 2\\) and \\(t = 4\\) represent?"
    )
    sol = (
        f"**Step 1:** The vertical axis measures distance from the starting depot.\n\n"
        f"**Step 2:** From \\(t = 2\\) to \\(t = 4\\), the distance decreases from {d_max} km to 0 km.\n\n"
        f"**Conclusion:** The van is traveling **back towards the starting point (returning home)**."
    )
    return {
        "id": f"g7_fn3_29_{rng.randint(100000, 999999)}",
        "subskill": "29_distance_time_graph_returning_to_start",
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
        "learning_objective_id": "math_g7_fn3_29",
        "hints": {"tier_1": "Distance from start is decreasing back to 0.", "tier_2": "Returning to start.", "tier_3": ans},
        "misconception_tags": ["interpreting_downward_distance_as_going_downhill"]
    }


# 30. Distance time graph comparing two travellers
def arch_30_distance_time_graph_comparing_two_travellers(rng: random.Random) -> Dict[str, Any]:
    # Runner A covers 10 km in 1 h (speed 10 km/h). Runner B covers 10 km in 2 h (speed 5 km/h).
    ans = "Runner A"
    prompt = (
        "Runner A and Runner B run a 10 km race.\n"
        "- Runner A finishes in 1 hour.\n"
        "- Runner B finishes in 2 hours.\n\n"
        "Which runner has the steeper line on a distance-time graph, and who was faster?"
    )
    sol = (
        "**Step 1: Calculate speeds (gradients):**\n"
        "- Speed A = $$\\frac{10\\text{ km}}{1\\text{ h}} = 10\\text{ km/h}$$\n"
        "- Speed B = $$\\frac{10\\text{ km}}{2\\text{ h}} = 5\\text{ km/h}$$\n\n"
        "**Step 2: Conclusion:**\n"
        "**Runner A** was faster and therefore has the steeper slope on the distance-time graph."
    )
    return {
        "id": f"g7_fn3_30_{rng.randint(100000, 999999)}",
        "subskill": "30_distance_time_graph_comparing_two_travellers",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_30",
        "hints": {"tier_1": "Higher speed produces a steeper graph.", "tier_2": "Runner A (10 km/h vs 5 km/h).", "tier_3": ans},
        "misconception_tags": ["confusing_time_taken_with_steepness"]
    }


# 31. Cost graph fixed charge plus variable rate
def arch_31_cost_graph_fixed_charge_plus_variable_rate(rng: random.Random) -> Dict[str, Any]:
    # Electrician charges R150 call-out fee + R100/h. Graph starts at (0, 150). For 3h -> 150 + 300 = 450
    ans = "R450"
    prompt = (
        "An electrician's billing graph starts at \\((0; 150)\\) on the vertical axis (a call-out fee of R150) "
        "and rises by R100 for every hour worked.\n\n"
        "1. Write the formula for total cost \\(C\\) in terms of hours \\(h\\).\n"
        "2. Calculate the total charge for 3 hours of work."
    )
    sol = (
        "**Step 1: Formula:**\n"
        "$$C = 100h + 150$$\n\n"
        "**Step 2: Calculation for \\(h = 3\\):**\n"
        "$$C = 100(3) + 150 = 300 + 150 = \\mathbf{R450}$$\n\n"
        "**Summary:** 1. \\(C = 100h + 150\\); 2. R450"
    )
    return {
        "id": f"g7_fn3_31_{rng.randint(100000, 999999)}",
        "subskill": "31_cost_graph_fixed_charge_plus_variable_rate",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_31",
        "hints": {"tier_1": "Call-out fee is R150, plus 3 * 100.", "tier_2": "150 + 300 = 450.", "tier_3": ans},
        "misconception_tags": ["omitting_fixed_call_out_fee"]
    }


# 32. Cost graph break even comparison two tariffs
def arch_32_cost_graph_break_even_comparison_two_tariffs(rng: random.Random) -> Dict[str, Any]:
    # Option A: C = 30n. Option B: C = 100 + 10n. Break-even: 30n = 100 + 10n -> 20n = 100 -> n = 5
    ans = "5 lessons"
    prompt = (
        "A gym offers two membership options:\n"
        "- **Tariff A:** R30 per lesson with no registration fee (\\(C = 30n\\))\n"
        "- **Tariff B:** R100 registration fee plus R10 per lesson (\\(C = 100 + 10n\\))\n\n"
        "For how many lessons \\(n\\) is the cost identical for both options (the break-even point)?"
    )
    sol = (
        "**Step 1:** Set the two cost equations equal:\n"
        "$$30n = 100 + 10n$$\n\n"
        "**Step 2:** Subtract \\(10n\\) from both sides:\n"
        "$$20n = 100$$\n\n"
        "**Step 3:** Divide by 20:\n"
        "$$n = \\frac{100}{20} = \\mathbf{5\\text{ lessons}}$$\n\n"
        "*(At 5 lessons, both tariffs cost R150)*."
    )
    return {
        "id": f"g7_fn3_32_{rng.randint(100000, 999999)}",
        "subskill": "32_cost_graph_break_even_comparison_two_tariffs",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn3_32",
        "hints": {"tier_1": "Solve 30n = 100 + 10n.", "tier_2": "20n = 100.", "tier_3": ans},
        "misconception_tags": ["break_even_algebra_slip"]
    }


# 33. Water level graph filling constant rate
def arch_33_water_level_graph_filling_constant_rate(rng: random.Random) -> Dict[str, Any]:
    # Tank starts with 50 L, tap adds 20 L/min. Volume at t = 10 mins -> 50 + 200 = 250 L
    ans = "250 litres"
    prompt = (
        "A rainwater tank already contains 50 litres of water. A tap fills it at a constant rate of 20 litres per minute.\n\n"
        "Calculate the volume of water in the tank after 10 minutes."
    )
    sol = (
        "**Step 1:** Formula: \\(V = 50 + 20t\\)\n\n"
        "**Step 2:** For \\(t = 10\\text{ minutes}\\):\n"
        "$$V = 50 + 20(10) = 50 + 200 = \\mathbf{250\\text{ litres}}$$"
    )
    return {
        "id": f"g7_fn3_33_{rng.randint(100000, 999999)}",
        "subskill": "33_water_level_graph_filling_constant_rate",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_33",
        "hints": {"tier_1": "Add 50 to 20 * 10.", "tier_2": "50 + 200 = 250.", "tier_3": ans},
        "misconception_tags": ["rate_addition_slip"]
    }


# 34. Water level graph emptying leaking tank
def arch_34_water_level_graph_emptying_leaking_tank(rng: random.Random) -> Dict[str, Any]:
    # Tank has 300 L, leaks 15 L per hour: V = 300 - 15t. When is it empty? 300 / 15 = 20 h
    ans = "20 hours"
    prompt = (
        "A water tank holds 300 litres of water and leaks at a constant rate of 15 litres per hour.\n\n"
        "How many hours will it take for the tank to be completely empty?"
    )
    sol = (
        "**Step 1:** Set volume \\(V = 0\\) in the emptying formula \\(V = 300 - 15t\\):\n"
        "$$0 = 300 - 15t$$\n\n"
        "**Step 2:** Solve for \\(t\\):\n"
        "$$15t = 300 \\implies t = \\frac{300}{15} = \\mathbf{20\\text{ hours}}$$"
    )
    return {
        "id": f"g7_fn3_34_{rng.randint(100000, 999999)}",
        "subskill": "34_water_level_graph_emptying_leaking_tank",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_34",
        "hints": {"tier_1": "Divide total volume (300) by leak rate (15).", "tier_2": "300 / 15 = 20.", "tier_3": ans},
        "misconception_tags": ["multiplying_instead_of_dividing_for_empty_time"]
    }


# 35. Temperature graph daily fluctuation cycle
def arch_35_temperature_graph_daily_fluctuation_cycle(rng: random.Random) -> Dict[str, Any]:
    # Min temp 8°C at 04:00, max temp 26°C at 14:00. Range = 18°C
    ans = "18 °C"
    prompt = (
        "A temperature graph over a 24-hour day records a minimum temperature of \\(8^\\circ\\text{C}\\) at 04:00 "
        "and a maximum of \\(26^\\circ\\text{C}\\) at 14:00.\n\n"
        "Calculate the temperature range for the day."
    )
    sol = (
        "**Step 1:** Recall the range formula:\n"
        "$$\\text{Range} = \\text{Maximum} - \\text{Minimum}$$\n\n"
        "**Step 2:** Substitute values:\n"
        "$$\\text{Range} = 26^\\circ\\text{C} - 8^\\circ\\text{C} = \\mathbf{18^\\circ\\text{C}}$$"
    )
    return {
        "id": f"g7_fn3_35_{rng.randint(100000, 999999)}",
        "subskill": "35_temperature_graph_daily_fluctuation_cycle",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn3_35",
        "hints": {"tier_1": "Subtract minimum (8) from maximum (26).", "tier_2": "26 - 8 = 18.", "tier_3": ans},
        "misconception_tags": ["temperature_range_calculation_error"]
    }


# 36. Conversion graph currency rand to dollar
def arch_36_conversion_graph_currency_rand_to_dollar(rng: random.Random) -> Dict[str, Any]:
    # Exchange rate: $1 = R18. Convert $25 to Rand -> 25 * 18 = R450
    ans = "R450"
    prompt = (
        "On a currency conversion line passing through the origin, \\$10 corresponds to R180.\n\n"
        "Calculate the value in South African Rand of \\$25."
    )
    sol = (
        "**Step 1:** Find exchange rate per dollar:\n"
        "$$\\frac{\\text{R180}}{\\$10} = \\text{R18 per dollar}$$\n\n"
        "**Step 2:** Convert \\$25:\n"
        "$$25 \\times \\text{R18} = \\mathbf{R450}$$"
    )
    return {
        "id": f"g7_fn3_36_{rng.randint(100000, 999999)}",
        "subskill": "36_conversion_graph_currency_rand_to_dollar",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_36",
        "hints": {"tier_1": "Find rate per dollar: 180 / 10 = 18.", "tier_2": "25 * 18 = 450.", "tier_3": ans},
        "misconception_tags": ["currency_exchange_division_error"]
    }


# 37. Conversion graph measurement miles to kilometres
def arch_37_conversion_graph_measurement_miles_to_kilometres(rng: random.Random) -> Dict[str, Any]:
    # 5 miles approx 8 km. 25 miles -> 5 * 8 = 40 km
    ans = "40 km"
    prompt = (
        "A conversion graph shows that 5 miles is approximately equal to 8 kilometres.\n\n"
        "Use this ratio to estimate the equivalent distance in kilometres for 25 miles."
    )
    sol = (
        "**Step 1:** Scale factor from 5 miles to 25 miles:\n"
        "$$\\frac{25}{5} = 5$$\n\n"
        "**Step 2:** Multiply kilometres by 5:\n"
        "$$8\\text{ km} \\times 5 = \\mathbf{40\\text{ km}}$$"
    )
    return {
        "id": f"g7_fn3_37_{rng.randint(100000, 999999)}",
        "subskill": "37_conversion_graph_measurement_miles_to_kilometres",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_37",
        "hints": {"tier_1": "25 is 5 times 5 miles.", "tier_2": "8 * 5 = 40 km.", "tier_3": ans},
        "misconception_tags": ["scaling_ratio_multiplication_error"]
    }


# 38. Graph interpreting steepness as speed
def arch_38_graph_interpreting_steepness_as_speed(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "On a distance-time graph, Section A has a steep upward line while Section B has a gentle, less steep upward line.\n\n"
        "During which section was the vehicle moving faster? Explain why."
    )
    sol = (
        "**Step 1:** In a distance-time graph, gradient (steepness) represents speed (\\(\\frac{\\text{distance}}{\\text{time}}\\)).\n\n"
        "**Conclusion:** The vehicle was moving faster during **Section A** because a steeper line indicates "
        "covering more distance in a given amount of time."
    )
    ans = "Section A"
    return {
        "id": f"g7_fn3_38_{rng.randint(100000, 999999)}",
        "subskill": "38_graph_interpreting_steepness_as_speed",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_38",
        "hints": {"tier_1": "Steeper slope = higher speed.", "tier_2": "Section A is steeper.", "tier_3": ans},
        "misconception_tags": ["steepness_speed_inverse_misunderstanding"]
    }


# 39. Graph identifying maximum and minimum turning points
def arch_39_graph_identifying_maximum_and_minimum_turning_points(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A roller-coaster trajectory graph reaches a highest crest at \\((4; 35)\\) and a lowest trough at \\((9; 3)\\).\n\n"
        "1. State the coordinates of the **maximum point**.\n"
        "2. State the coordinates of the **minimum point**."
    )
    sol = (
        "**Step 1:** Maximum point is the highest peak: **(4; 35)** (height 35 m at 4 seconds).\n\n"
        "**Step 2:** Minimum point is the lowest trough: **(9; 3)** (height 3 m at 9 seconds).\n\n"
        "**Summary:** 1. (4; 35); 2. (9; 3)"
    )
    ans = "1. (4; 35); 2. (9; 3)"
    return {
        "id": f"g7_fn3_39_{rng.randint(100000, 999999)}",
        "subskill": "39_graph_identifying_maximum_and_minimum_turning_points",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_39",
        "hints": {"tier_1": "Max is highest point, min is lowest.", "tier_2": "1. (4; 35); 2. (9; 3).", "tier_3": ans},
        "misconception_tags": ["swapping_maximum_and_minimum"]
    }


# 40. Graph interpreting average speed whole journey
def arch_40_graph_interpreting_average_speed_whole_journey(rng: random.Random) -> Dict[str, Any]:
    # Total distance 240 km in 4 hours total (including a 1-hour stop)
    ans = "60 km/h"
    prompt = (
        "A family drives a total distance of 240 km. The trip took 4 hours in total, which included a 1-hour lunch break.\n\n"
        "Calculate the **average speed** for the entire 4-hour journey."
    )
    sol = (
        "**Step 1:** Formula for average speed for a whole journey:\n"
        "$$\\text{Average Speed} = \\frac{\\text{Total Distance}}{\\text{Total Time Taken}}$$\n\n"
        "**Step 2:** Substitute total values:\n"
        "$$\\text{Average Speed} = \\frac{240\\text{ km}}{4\\text{ h}} = \\mathbf{60\\text{ km/h}}$$"
    )
    return {
        "id": f"g7_fn3_40_{rng.randint(100000, 999999)}",
        "subskill": "40_graph_interpreting_average_speed_whole_journey",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_40",
        "hints": {"tier_1": "Divide total distance by total time.", "tier_2": "240 / 4 = 60.", "tier_3": ans},
        "misconception_tags": ["subtracting_rest_stops_from_total_journey_time"]
    }


# 41. Graph from verbal journey story
def arch_41_graph_from_verbal_journey_story(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A learner walks to school, stops at a shop to buy bread, and then continues running to school because they are late.\n\n"
        "Describe the three consecutive line segments on a distance-from-home vs time graph."
    )
    sol = (
        "**Three Segments:**\n"
        "1. **Walking to shop:** A straight line sloping upward at a moderate gradient.\n"
        "2. **Stopped at shop:** A flat, horizontal line segment (distance remains constant as time passes).\n"
        "3. **Running to school:** A steeper straight line sloping upward (higher speed to school)."
    )
    ans = "1. Moderate slope; 2. Horizontal line; 3. Steeper slope"
    return {
        "id": f"g7_fn3_41_{rng.randint(100000, 999999)}",
        "subskill": "41_graph_from_verbal_journey_story",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_fn3_41",
        "hints": {"tier_1": "Walk = moderate slope, stop = flat, run = steep slope.", "tier_2": "Describe the 3 gradients.", "tier_3": ans},
        "misconception_tags": ["story_to_graph_translation_gap"]
    }


# 42. Verbal story from given graph
def arch_42_verbal_story_from_given_graph(rng: random.Random) -> Dict[str, Any]:
    d_dest = rng.choice([6, 8, 10, 12])
    svg = _svg_graph_line("Journey Profile", x_range=(0, 6), y_range=(0, d_dest + 2), line_pts=[(0, 0), (2, d_dest), (4, d_dest), (6, 0)])
    ans = "Travels away, stops for 2 hours, then returns home"
    prompt = (
        f"Examine the plotted profile of distance from home over time:\n\n"
        f"Write a short, three-sentence story describing what happens during this trip."
    )
    sol = (
        "**Story:**\n"
        f"1. The traveller journeys {d_dest} km away from home over the first 2 hours.\n"
        "2. They remain stopped at their destination for 2 hours (from hour 2 to hour 4).\n"
        "3. They travel back home, arriving at the starting point at hour 6."
    )
    return {
        "id": f"g7_fn3_42_{rng.randint(100000, 999999)}",
        "subskill": "42_verbal_story_from_given_graph",
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
        "learning_objective_id": "math_g7_fn3_42",
        "hints": {"tier_1": "Describe going away, stopping, and returning.", "tier_2": "Travels away, stops, returns.", "tier_3": ans},
        "misconception_tags": ["graph_to_narrative_misinterpretation"]
    }


# 43. Graph interpreting horizontal axis units and scale
def arch_43_graph_interpreting_horizontal_axis_units_and_scale(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "On a graph's horizontal axis, there are 5 grid squares between 0 and 10 hours.\n\n"
        "What duration does each single grid square represent?"
    )
    sol = (
        "**Step 1:** Calculate scale per grid division:\n"
        "$$\\text{Scale} = \\frac{10\\text{ hours}}{5\\text{ squares}} = \\mathbf{2\\text{ hours per square}}$$"
    )
    ans = "2 hours"
    return {
        "id": f"g7_fn3_43_{rng.randint(100000, 999999)}",
        "subskill": "43_graph_interpreting_horizontal_axis_units_and_scale",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_fn3_43",
        "hints": {"tier_1": "Divide 10 by 5.", "tier_2": "10 / 5 = 2.", "tier_3": ans},
        "misconception_tags": ["grid_scale_division_error"]
    }


# 44. Graph interpreting vertical axis units and scale
def arch_44_graph_interpreting_vertical_axis_units_and_scale(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "On the vertical \\(y\\)-axis, 4 grid blocks represent R200.\n\n"
        "How much money does a height of 7 grid blocks represent?"
    )
    sol = (
        "**Step 1:** Find value per block:\n"
        "$$\\frac{\\text{R200}}{4} = \\text{R50 per block}$$\n\n"
        "**Step 2:** Multiply by 7 blocks:\n"
        "$$7 \\times \\text{R50} = \\mathbf{R350}$$"
    )
    ans = "R350"
    return {
        "id": f"g7_fn3_44_{rng.randint(100000, 999999)}",
        "subskill": "44_graph_interpreting_vertical_axis_units_and_scale",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_44",
        "hints": {"tier_1": "Each block is R50.", "tier_2": "7 * 50 = R350.", "tier_3": ans},
        "misconception_tags": ["axis_scaling_multiplication_slip"]
    }


# 45. Graph detecting misleading scale distortion
def arch_45_graph_detecting_misleading_scale_distortion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "A company publishes a graph of profits where the vertical axis starts at R950 000 instead of 0.\n\n"
        "A small profit rise from R960 000 to R980 000 appears visually as a huge, massive bar.\n\n"
        "Explain why starting a vertical axis away from zero without a broken axis symbol is misleading."
    )
    sol = (
        "**Step 1:** Truncating or omitting zero on the vertical axis exaggerates small percentage differences, "
        "making minor changes appear dramatically larger than they actually are.\n\n"
        "**Step 2:** A rise from R960k to R980k is only about a 2% change, but visually appears like a 300% surge.\n\n"
        "**Conclusion:** It distorts visual proportions and misleads the reader."
    )
    ans = "It exaggerates small differences and distorts proportions"
    return {
        "id": f"g7_fn3_45_{rng.randint(100000, 999999)}",
        "subskill": "45_graph_detecting_misleading_scale_distortion",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_45",
        "hints": {"tier_1": "Think about why bar heights look different when not starting at 0.", "tier_2": "It exaggerates small differences.", "tier_3": ans},
        "misconception_tags": ["unaware_of_graphical_scale_bias"]
    }


# 46. Graph quadratic parabola symmetry observation
def arch_46_graph_quadratic_parabola_symmetry_observation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The parabola \\(y = x^2\\) passes through points \\((-2; 4)\\), \\((-1; 1)\\), \\((0; 0)\\), \\((1; 1)\\), \\((2; 4)\\).\n\n"
        "1. What is the line of symmetry for this curve?\n"
        "2. What is the lowest point (vertex) of the parabola?"
    )
    sol = (
        "**Step 1:** The points on the left (negative \\(x\\)) mirror the points on the right (positive \\(x\\)) "
        "across the vertical **\\(y\\)-axis (equation \\(x = 0\\))**.\n\n"
        "**Step 2:** The lowest turning point (vertex) is at the origin: **(0; 0)**.\n\n"
        "**Summary:** 1. The y-axis (x = 0); 2. (0; 0)"
    )
    ans = "1. The y-axis (x = 0); 2. (0; 0)"
    return {
        "id": f"g7_fn3_46_{rng.randint(100000, 999999)}",
        "subskill": "46_graph_quadratic_parabola_symmetry_observation",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_46",
        "hints": {"tier_1": "Mirror line is the vertical axis x = 0.", "tier_2": "Vertex is (0; 0).", "tier_3": ans},
        "misconception_tags": ["parabola_axis_of_symmetry_confusion"]
    }


# 47. Graph identifying domain and range concept
def arch_47_graph_identifying_domain_and_range_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In function terminology:\n\n"
        "1. What term refers to the set of all possible **input values** (horizontal \\(x\\))?\n"
        "2. What term refers to the set of all corresponding **output values** (vertical \\(y\\))?"
    )
    sol = (
        "**Definitions:**\n"
        "1. The set of all permissible input values (\\(x\\)) is called the **Domain**.\n"
        "2. The set of all resulting output values (\\(y\\)) is called the **Range**.\n\n"
        "**Summary:** 1. Domain; 2. Range"
    )
    ans = "1. Domain; 2. Range"
    return {
        "id": f"g7_fn3_47_{rng.randint(100000, 999999)}",
        "subskill": "47_graph_identifying_domain_and_range_concept",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_47",
        "hints": {"tier_1": "Inputs = Domain, Outputs = Range.", "tier_2": "1. Domain; 2. Range.", "tier_3": ans},
        "misconception_tags": ["swapping_domain_and_range"]
    }


# 48. Graph step function parking fees
def arch_48_graph_step_function_parking_fees(rng: random.Random) -> Dict[str, Any]:
    # 0 to 1 h = R10; 1 to 2 h = R20; 2 to 3 h = R30. For 2,5 h -> R30
    ans = "R30"
    prompt = (
        "A shopping mall parking garage charges in 1-hour brackets (a step function):\n"
        "- \\(0\\) to \\(1\\) hour: R10\n"
        "- More than \\(1\\) up to \\(2\\) hours: R20\n"
        "- More than \\(2\\) up to \\(3\\) hours: R30\n\n"
        "How much will a customer pay for parking for 2 hours and 25 minutes?"
    )
    sol = (
        "**Step 1:** Convert 2 hours and 25 minutes to decimal hours: \\(2,42\\text{ hours}\\).\n\n"
        "**Step 2:** Locate which tier \\(2,42\\) falls into:\n"
        "It exceeds 2 hours and is less than 3 hours, so it falls in the **R30 bracket**.\n\n"
        "**Total fee:** **R30**"
    )
    return {
        "id": f"g7_fn3_48_{rng.randint(100000, 999999)}",
        "subskill": "48_graph_step_function_parking_fees",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_48",
        "hints": {"tier_1": "Since time is between 2 and 3 hours, use the 2-to-3 hour bracket.", "tier_2": "Cost is R30.", "tier_3": ans},
        "misconception_tags": ["rounding_down_step_function_rate"]
    }


# 49. Graph speed time interpreting acceleration
def arch_49_graph_speed_time_interpreting_acceleration(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "On a **speed-time graph** (speed on vertical axis, time on horizontal):\n\n"
        "1. What does an upward sloping line mean?\n"
        "2. What does a flat horizontal line mean?"
    )
    sol = (
        "**Interpretations on Speed-Time Graph:**\n"
        "1. **Upward sloping line:** The speed is increasing over time (the object is **accelerating**).\n"
        "2. **Horizontal line:** The speed remains constant (moving at a **steady/constant speed**).\n\n"
        "*(Caution: In a distance-time graph, a horizontal line means stationary, but in a speed-time graph it means constant speed!)*"
    )
    ans = "1. Accelerating (speed increasing); 2. Moving at constant speed"
    return {
        "id": f"g7_fn3_49_{rng.randint(100000, 999999)}",
        "subskill": "49_graph_speed_time_interpreting_acceleration",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_fn3_49",
        "hints": {"tier_1": "Vertical axis is speed, not distance.", "tier_2": "1. Speeding up; 2. Constant speed.", "tier_3": ans},
        "misconception_tags": ["confusing_speed_time_with_distance_time"]
    }


# 50. Graph comprehensive journey autopsy
def arch_50_graph_comprehensive_journey_autopsy(rng: random.Random) -> Dict[str, Any]:
    # A complete journey autopsy:
    # 0 to 2 h: moves 120 km (speed 60 km/h)
    # 2 to 3 h: rests 1 h (speed 0)
    # 3 to 5 h: travels 160 km to reach 280 km (speed 80 km/h)
    # Total distance 280 km, total time 5 h -> avg speed = 56 km/h
    ans = "1. 60 km/h; 2. 1 hour; 3. 56 km/h"
    prompt = (
        "A truck journey distance-time profile has three sections:\n"
        "- **Section 1:** From \\(t = 0\\) to \\(t = 2\\text{ h}\\), travels from 0 to 120 km.\n"
        "- **Section 2:** From \\(t = 2\\) to \\(t = 3\\text{ h}\\), remains at 120 km.\n"
        "- **Section 3:** From \\(t = 3\\) to \\(t = 5\\text{ h}\\), travels from 120 to 280 km.\n\n"
        "Perform a complete three-part autopsy:\n"
        "1. Calculate the speed during Section 1.\n"
        "2. How long did the truck stop in Section 2?\n"
        "3. Calculate the overall average speed for the entire 5-hour journey."
    )
    sol = (
        "**Part 1: Section 1 speed:**\n"
        "$$\\text{Speed}_1 = \\frac{120\\text{ km}}{2\\text{ h}} = \\mathbf{60\\text{ km/h}}$$\n\n"
        "**Part 2: Stop duration:**\n"
        "$$\\text{Duration} = 3 - 2 = \\mathbf{1\\text{ hour}}$$\n\n"
        "**Part 3: Overall average speed:**\n"
        "$$\\text{Total distance} = 280\\text{ km}, \\quad \\text{Total time} = 5\\text{ hours}$$\n"
        "$$\\text{Average Speed} = \\frac{280}{5} = \\mathbf{56\\text{ km/h}}$$\n\n"
        "**Summary:** 1. \\(60\\text{ km/h}\\); 2. \\(1\\text{ hour}\\); 3. \\(56\\text{ km/h}\\)"
    )
    return {
        "id": f"g7_fn3_50_{rng.randint(100000, 999999)}",
        "subskill": "50_graph_comprehensive_journey_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "learning_objective_id": "math_g7_fn3_50",
        "hints": {"tier_1": "1: 120/2; 2: 3-2; 3: 280/5.", "tier_2": "60 km/h, 1 h, 56 km/h.", "tier_3": ans},
        "misconception_tags": ["comprehensive_graph_autopsy_slip"]
    }
