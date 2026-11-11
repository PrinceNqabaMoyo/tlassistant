"""Subskills 37 to 44: Topographical Maps, Contour Lines, Gradients & Profiles for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Contour line interval determination from index contours."""
    contour_1 = r.choice([1000, 1200, 1400, 1500, 1600])
    num_intervals = r.choice([4, 5])
    interval = r.choice([20, 25, 50])
    contour_2 = contour_1 + (num_intervals * interval)

    prompt = (
        f"A standard South African 1 : 50 000 topographical map extract displays brown contour lines indicating elevation above sea level.\n\n"
        f"Two adjacent thick index contour lines are marked as **{_fmt(contour_1)} m** and **{_fmt(contour_2)} m**.\n"
        f"There are **{num_intervals} equal intervals** (contour spaces) between these two index contours.\n\n"
        f"Calculate the **contour interval** (the vertical height difference between two consecutive contour lines) on this map."
    )

    diff = contour_2 - contour_1
    calc_interval = diff / num_intervals
    correct_ans = f"{_fmt(int(calc_interval))} m"

    custom_opts = [
        f"{_fmt(int(calc_interval))} m",
        f"{_fmt(int(calc_interval * 2))} m",
        f"{_fmt(int(calc_interval / 2))} m",
        f"{_fmt(int(diff))} m",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the vertical difference between the index contours [1 mark]:\n"
        f"Difference = {_fmt(contour_2)} m - {_fmt(contour_1)} m = {_fmt(diff)} m.\n\n"
        f"Step 2: Divide by the number of contour intervals [1 mark]:\n"
        f"Contour Interval = {_fmt(diff)} m ÷ {num_intervals} = {correct_ans}.\n\n"
        f"Step 3: Stated answer with unit [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Topographic Contour Map (Interval {interval} m)",
        "elevation": contour_2,
        "dimensions": f"{contour_1}m to {contour_2}m",
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="subskill_37",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the difference in height between the two index contours, then divide by the number of intervals.",
        tier_2=f"Difference = {contour_2} - {contour_1} = {diff} m. Divide this by {num_intervals}.",
        tier_3=f"Contour interval = {diff} ÷ {num_intervals} = {correct_ans}.",
        r=r,
    )


def generate_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: Spot height and trigonometrical station altitude lookup & interpretation."""
    trig_beacon_num = r.randint(120, 380)
    altitude = round(r.uniform(1320.0, 1890.0), 1)
    base_spot_height = round(altitude - r.uniform(110.0, 340.0), 1)

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is studying a 1 : 50 000 topographical map of the Drakensberg foothills.\n\n"
        f"On the map, a trigonometrical station is marked as **Δ {trig_beacon_num}** with an elevation of **{_fmt(altitude)} m**.\n"
        f"Nearby at the bottom of the valley, a spot height is marked as **• {_fmt(base_spot_height)}**.\n\n"
        f"Calculate the vertical height difference between the trigonometrical station and the valley spot height."
    )

    height_diff = round(altitude - base_spot_height, 1)
    correct_ans = f"{_fmt(height_diff)} m"

    custom_opts = [
        f"{_fmt(height_diff)} m",
        f"{_fmt(round(height_diff + 50.0, 1))} m",
        f"{_fmt(round(altitude + base_spot_height, 1))} m",
        f"{_fmt(round(height_diff / 2, 1))} m",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify the altitude of trigonometrical station Δ {trig_beacon_num} = {_fmt(altitude)} m [1 mark].\n"
        f"Step 2: Identify the spot height in the valley = {_fmt(base_spot_height)} m [1 mark].\n"
        f"Step 3: Subtract to determine the vertical difference [1 mark]:\n"
        f"Vertical Difference = {_fmt(altitude)} m - {_fmt(base_spot_height)} m = {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Trig Beacon {trig_beacon_num} ({altitude} m)",
        "elevation": altitude,
        "features": [f"Trig Beacon {trig_beacon_num}", f"Base Spot Height {base_spot_height}"],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="subskill_38",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the lower spot height altitude from the trigonometrical station altitude.",
        tier_2=f"Difference = {altitude} m - {base_spot_height} m.",
        tier_3=f"Vertical difference = {correct_ans}.",
        r=r,
    )


def generate_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Steep vs gentle slope identification based on contour spacing."""
    feature = r.choice(["koppie", "ridge", "escarpment", "hill"])
    side_steep = r.choice(["North-facing slope", "South-facing slope", "East-facing slope", "West-facing slope"])
    side_gentle = r.choice([s for s in ["North-facing slope", "South-facing slope", "East-facing slope", "West-facing slope"] if s != side_steep])

    ask_steep = r.choice([True, False])
    target = side_steep if ask_steep else side_gentle

    prompt = (
        f"A topographical map depicts an isolated {feature}.\n"
        f"- On the **{side_steep}**, the contour lines are packed very close together.\n"
        f"- On the **{side_gentle}**, the contour lines are widely spaced apart.\n\n"
        f"Which slope has the **{'STEEPEST' if ask_steep else 'GENTLEST'}** incline, and why?"
    )

    if ask_steep:
        correct_ans = f"{side_steep}, because closely spaced contour lines represent a rapid increase in elevation over a short horizontal distance."
        opt_b = f"{side_gentle}, because widely spaced contour lines mean the elevation changes very fast."
        opt_c = f"{side_steep}, because closely spaced contour lines indicate completely flat terrain."
        opt_d = f"{side_gentle}, because widely spaced contours always indicate a steep cliff face."
    else:
        correct_ans = f"{side_gentle}, because widely spaced contour lines represent a gradual increase in elevation over a large horizontal distance."
        opt_b = f"{side_steep}, because closely spaced contour lines mean the land is flat and gentle."
        opt_c = f"{side_gentle}, because contours far apart indicate an almost vertical cliff."
        opt_d = f"{side_steep}, because contour lines close together represent a gradual gentle slope."

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Understand contour line spacing rules on maps [1 mark]:\n"
        f"- Close contour lines = steep gradient (high elevation change over small distance).\n"
        f"- Wide contour lines = gentle gradient (low elevation change over large distance).\n"
        f"Step 2: Apply to the question [1 mark]: The {'steepest' if ask_steep else 'gentlest'} slope is the {target}.\n"
        f"Step 3: Stated reasoning [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Topographic Feature: {feature.title()} Slopes",
        "features": [side_steep, side_gentle],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="subskill_39",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Contour lines close together indicate steep terrain, while contour lines far apart indicate gentle, flatter terrain.",
        tier_2=f"Closely spaced contours = steep. Widely spaced contours = gentle. Check which slope matches {'steep' if ask_steep else 'gentle'}.",
        tier_3=f"Correct answer is: {correct_ans}.",
        r=r,
    )


def generate_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: V-shaped river contour flow direction."""
    river_name = r.choice(["Blyde River", "Mooi River", "Buffels River", "Molopo River", "Crocodile River"])
    flow_dir = r.choice(["South to North", "North to South", "West to East", "East to West"])
    
    if flow_dir == "South to North":
        v_points = "South"
        high_side = "South"
        low_side = "North"
    elif flow_dir == "North to South":
        v_points = "North"
        high_side = "North"
        low_side = "South"
    elif flow_dir == "West to East":
        v_points = "West"
        high_side = "West"
        low_side = "East"
    else:
        v_points = "East"
        high_side = "East"
        low_side = "West"

    prompt = (
        f"On a 1 : 50 000 topographical map, the **{river_name}** cuts through a valley.\n"
        f"Where the brown contour lines cross the river, they bend into distinct **'V'-shapes**.\n"
        f"The apex (point) of the 'V' points towards the **{v_points}**.\n\n"
        f"In which general direction is the river flowing, and what is the geographical rule for river contours?"
    )

    correct_ans = f"Towards the {flow_dir.split(' to ')[1]} (from {high_side} to {low_side}), because the 'V' points upstream to higher ground, meaning water flows downstream."
    opt_b = f"Towards the {v_points}, because rivers always flow in the direction the 'V' points."
    opt_c = f"Towards the {v_points}, because contour lines point downstream towards sea level."
    opt_d = f"Towards the {high_side}, because water flows uphill towards the apex of the 'V'."

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Apply the contour 'V' rule for river valleys [1 mark]:\n"
        f"Contour lines form a 'V' pointing upstream (towards higher ground / the river source).\n"
        f"Step 2: Determine flow direction [1 mark]:\n"
        f"Since the 'V' points {v_points} (upstream), the river flows downstream towards the {low_side} (from {high_side} to {low_side}).\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_40",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="In river valleys, contour lines form 'V's that point UPSTREAM (towards higher elevation). Water flows DOWNSTREAM.",
        tier_2=f"The 'V' points towards {v_points} (upstream). Therefore, water flows in the opposite direction towards {low_side}.",
        tier_3=f"The river flows towards the {low_side} ({flow_dir}).",
        r=r,
    )


def generate_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Gradient calculation as a ratio 1 : n (Rise / Run)."""
    # Rise (vertical height) and Run (horizontal distance)
    rise_m = r.choice([50, 80, 100, 120, 150, 200])
    ratio_n = r.choice([10, 15, 20, 25, 40, 50])
    run_m = rise_m * ratio_n
    run_km = run_m / 1000

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is planning a mountain hike shown on a 1 : 50 000 map.\n"
        f"- The starting point is at an altitude of **1 200 m**.\n"
        f"- The summit is at an altitude of **{_fmt(1200 + rise_m)} m**.\n"
        f"- The horizontal map ground distance between the start and summit is **{_fmt(run_km)} km** ({_fmt(run_m)} m).\n\n"
        f"Calculate the **average gradient** of the hiking trail, expressed in the standard ratio format **1 : n**.\n"
        f"*(Formula: $\\text{{Gradient}} = \\frac{{\\text{{Vertical Height (Rise)}}}}{{\\text{{Horizontal Distance (Run)}}}}$)*"
    )

    correct_ans = f"1 : {ratio_n}"

    custom_opts = [
        f"1 : {ratio_n}",
        f"1 : {ratio_n * 2}",
        f"1 : {max(2, int(ratio_n / 2))}",
        f"1 : {ratio_n + 10}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the vertical rise [1 mark]:\n"
        f"Rise = {_fmt(1200 + rise_m)} m - 1 200 m = {_fmt(rise_m)} m.\n\n"
        f"Step 2: Express both rise and run in the same units (metres) [1 mark]:\n"
        f"Run = {_fmt(run_km)} km = {_fmt(run_m)} m.\n\n"
        f"Step 3: Calculate gradient ratio 1 : n [1 mark]:\n"
        f"Gradient = Rise ÷ Run = {_fmt(rise_m)} ÷ {_fmt(run_m)} = 1 ÷ ({_fmt(run_m)} ÷ {_fmt(rise_m)}) = 1 : {ratio_n}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Gradient Slope Profile (Rise {rise_m} m, Run {run_m} m)",
        "height_m": rise_m,
        "width_m": run_m,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="subskill_41",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Make sure rise and run are in the same units (metres). Then divide the run by the rise: n = Run ÷ Rise.",
        tier_2=f"Rise = {rise_m} m. Run = {run_m} m. n = {run_m} ÷ {rise_m}.",
        tier_3=f"Gradient = 1 : {ratio_n}.",
        r=r,
    )


def generate_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Subskill 42: Intervisibility between two points on a topographic profile."""
    height_a = r.choice([1400, 1450, 1500])
    height_b = r.choice([1420, 1460, 1510])
    has_obstacle = r.choice([True, False])

    if has_obstacle:
        obstacle_name = "Koppie Ridge"
        obstacle_height = max(height_a, height_b) + r.choice([80, 120, 150])
    else:
        obstacle_name = "Valley Floor"
        obstacle_height = min(height_a, height_b) - r.choice([60, 100])

    prompt = (
        f"Two fire lookout towers are marked on a topographical map:\n"
        f"- **Tower A** sits at an elevation of **{_fmt(height_a)} m**.\n"
        f"- **Tower B** sits at an elevation of **{_fmt(height_b)} m**.\n"
        f"Directly in a straight line between Tower A and Tower B lies **{obstacle_name}**, with an elevation of **{_fmt(obstacle_height)} m**.\n\n"
        f"Is there **intervisibility** between Tower A and Tower B (can an observer at Tower A see Tower B directly)?"
    )

    if has_obstacle:
        correct_ans = f"No, because {obstacle_name} ({_fmt(obstacle_height)} m) is higher than both towers, obstructing the direct line of sight."
        opt_b = f"Yes, because both towers are above sea level."
        opt_c = f"Yes, because Tower B is higher than Tower A."
        opt_d = f"No, because Tower A and Tower B have identical heights."
    else:
        correct_ans = f"Yes, because the intervening {obstacle_name} ({_fmt(obstacle_height)} m) is lower than both towers, so there is an unobstructed line of sight."
        opt_b = f"No, because you can never see across a valley floor."
        opt_c = f"No, because the distance between towers is too great for any map."
        opt_d = f"Yes, but only if Tower A is moved to the valley floor."

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Compare the elevations of Tower A ({_fmt(height_a)} m) and Tower B ({_fmt(height_b)} m) [1 mark].\n"
        f"Step 2: Check the elevation of the landform directly between them ({obstacle_name} = {_fmt(obstacle_height)} m) [1 mark].\n"
        f"Step 3: Determine intervisibility [1 mark]:\n"
        f"{'Since ' + obstacle_name + ' is higher than both towers, it blocks line of sight (NO intervisibility).' if has_obstacle else 'Since ' + obstacle_name + ' is lower than both towers, line of sight is clear (YES, intervisible).'}"
    )

    return _build_question_payload(
        subskill_id="subskill_42",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Check if the landform between the two points is higher than the line of sight connecting them.",
        tier_2=f"Towers are at {height_a} m and {height_b} m. Intervening landform is at {obstacle_height} m.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Subskill 43: Hiking trail elevation gain and loss across waypoints."""
    p1 = r.choice([800, 900, 1000])
    gain_1 = r.randint(250, 450)
    p2 = p1 + gain_1
    loss_1 = r.randint(100, 200)
    p3 = p2 - loss_1
    gain_2 = r.randint(300, 500)
    p4 = p3 + gain_2

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is hiking an amphitheatre trail in the Drakensberg. The elevation profile logs 4 major waypoints:\n"
        f"- **Start (Waypoint 1)**: {_fmt(p1)} m\n"
        f"- **Viewpoint (Waypoint 2)**: {_fmt(p2)} m\n"
        f"- **River Crossing (Waypoint 3)**: {_fmt(p3)} m\n"
        f"- **Summit Hut (Waypoint 4)**: {_fmt(p4)} m\n\n"
        f"Calculate the **total cumulative vertical ascent (elevation gain)** completed by {name} along this hike."
    )

    total_ascent = gain_1 + gain_2
    correct_ans = f"{_fmt(total_ascent)} m"

    custom_opts = [
        f"{_fmt(total_ascent)} m",
        f"{_fmt(p4 - p1)} m",  # Net gain
        f"{_fmt(total_ascent + loss_1)} m",
        f"{_fmt(gain_1)} m",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate ascent for each climbing segment [1 mark]:\n"
        f"- Waypoint 1 to 2: {_fmt(p2)} m - {_fmt(p1)} m = {_fmt(gain_1)} m ascent.\n"
        f"- Waypoint 2 to 3: descent of {_fmt(loss_1)} m (not counted towards ascent).\n"
        f"- Waypoint 3 to 4: {_fmt(p4)} m - {_fmt(p3)} m = {_fmt(gain_2)} m ascent.\n\n"
        f"Step 2: Sum the uphill ascents [1 mark]:\n"
        f"Total Ascent = {_fmt(gain_1)} m + {_fmt(gain_2)} m = {_fmt(total_ascent)} m.\n\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"Hiking Trail Elevation Profile ({p1}m - {p4}m)",
        "categories": ["P1", "P2", "P3", "P4"],
        "values": [p1, p2, p3, p4],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="subskill_43",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Cumulative elevation gain sums only the uphill climbs, ignoring downhill descents.",
        tier_2=f"Ascent 1 = {p2} - {p1} = {gain_1} m. Ascent 2 = {p4} - {p3} = {gain_2} m. Add them.",
        tier_3=f"Total ascent = {gain_1} + {gain_2} = {correct_ans}.",
        r=r,
    )


def generate_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Impact of steep gradient on hiking time or vehicle fuel consumption."""
    flat_rate = r.choice([4.0, 5.0])  # km/h on flat
    dist_km = r.choice([12.0, 15.0, 18.0])
    steep_slowdown_pct = r.choice([20, 25, 30])  # % speed reduction on steep terrain

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name}'s hiking group walks at an average speed of **{_fmt(flat_rate)} km/h** on flat terrain.\n"
        f"They are hiking a mountainous route of **{_fmt(dist_km)} km** where steep gradients reduce their average walking speed by **{steep_slowdown_pct}%**.\n\n"
        f"Calculate the estimated time (in hours and minutes) the group will take to complete the hiking route."
    )

    reduced_speed = flat_rate * (1 - steep_slowdown_pct / 100)
    time_hours_float = dist_km / reduced_speed
    hours = int(time_hours_float)
    minutes = int(round((time_hours_float - hours) * 60))
    if minutes == 60:
        hours += 1
        minutes = 0

    correct_ans = f"{hours} hours {minutes} minutes"

    # Distractor using flat speed
    flat_time = dist_km / flat_rate
    f_h = int(flat_time)
    f_m = int(round((flat_time - f_h) * 60))
    flat_ans = f"{f_h} hours {f_m} minutes"

    custom_opts = [
        correct_ans,
        flat_ans,
        f"{hours + 1} hours {minutes} minutes",
        f"{max(1, hours - 1)} hours {minutes} minutes",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the reduced walking speed on steep gradient [1 mark]:\n"
        f"Speed = {_fmt(flat_rate)} km/h × (1 - {steep_slowdown_pct}%) = {_fmt(flat_rate)} × {1 - steep_slowdown_pct/100:.2f} = {_fmt(reduced_speed)} km/h.\n\n"
        f"Step 2: Calculate travel time in hours [1 mark]:\n"
        f"Time = Distance ÷ Speed = {_fmt(dist_km)} km ÷ {_fmt(reduced_speed)} km/h = {_fmt(time_hours_float)} hours.\n\n"
        f"Step 3: Convert to hours and minutes [1 mark]:\n"
        f"{hours} hours + ({_fmt(time_hours_float - hours, 4)} × 60 min) = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_44",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="First find the reduced speed after subtracting the percentage slowdown, then use Time = Distance ÷ Speed.",
        tier_2=f"Reduced speed = {flat_rate} × (1 - {steep_slowdown_pct/100}) = {reduced_speed:.2f} km/h. Time = {dist_km} ÷ {reduced_speed:.2f}.",
        tier_3=f"Time = {time_hours_float:.2f} hours = {correct_ans}.",
        r=r,
    )
