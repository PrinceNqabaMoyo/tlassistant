"""Subskills 10 to 18: Elevation Plans, Cardinal Directions & Solar Orientation for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: Identify North Elevation vs South Elevation based on floor plan layout."""
    name = r.choice(SA_NAMES)
    north_rooms = r.choice(["Living Room and Master Bedroom", "Lounge and Dining Area", "Veranda and Kitchen"])

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "elevation_compass",
        "title": "House Orientation & Elevation Compass",
        "compass": {"north": "Up", "south": "Down", "east": "Right", "west": "Left"},
        "north_facing_wall": north_rooms,
    }

    prompt = (
        f"A floor plan has a compass rose indicating that the top edge of the page points North. "
        f"The {north_rooms} are positioned along the top external wall of the house.\n"
        f"Which elevation plan represents the view looking at this top external wall?"
    )

    correct_ans = "North Elevation"
    custom_opts = [
        "North Elevation",
        "South Elevation",
        "East Elevation",
        "West Elevation",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand architectural elevation naming conventions [1 mark].\n"
        f"An elevation plan is named after the compass direction that the wall faces.\n"
        f"Step 2: Relate wall orientation to compass direction [1 mark].\n"
        f"Because the top wall faces North, it is designated as the North Elevation.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="10",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Elevation plans are named according to the compass direction that the wall faces.",
        tier_2="The wall facing North is the North Elevation.",
        tier_3="Correct elevation: North Elevation.",
        r=r,
        diagram_spec=diagram_spec,
    )


def generate_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Subskill 11: Identify East vs West Elevation based on window/door positions."""
    name = r.choice(SA_NAMES)
    compass_cardinal = r.choice(["East", "West"])
    opposite = "West" if compass_cardinal == "East" else "East"
    features = "a double garage door and a side kitchen door" if compass_cardinal == "East" else "two high bathroom windows and a sliding patio door"

    prompt = (
        f"On a house plan where North points directly upward, the side wall facing {compass_cardinal} "
        f"contains {features}.\n"
        f"What is the official architectural name of the drawing showing this specific side view of the house?"
    )

    correct_ans = f"{compass_cardinal} Elevation"
    custom_opts = [
        f"{compass_cardinal} Elevation",
        f"{opposite} Elevation",
        "North Elevation",
        "South Elevation",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Determine wall direction [1 mark].\n"
        f"The wall is on the {compass_cardinal} side of the house and faces {compass_cardinal}.\n"
        f"Step 2: Apply elevation terminology [1 mark].\n"
        f"A view showing the wall that faces {compass_cardinal} is called the {compass_cardinal} Elevation.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"House Elevation ({compass_cardinal})",
        "side": compass_cardinal,
        "features": [features],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="11",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The elevation is named after the cardinal direction the wall faces.",
        tier_2=f"The wall facing {compass_cardinal} is the {compass_cardinal} Elevation.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Subskill 12: Observer viewpoint facing direction relative to elevation name."""
    elevation_name = r.choice(["North", "South", "East", "West"])
    opposite_map = {"North": "South", "South": "North", "East": "West", "West": "East"}
    observer_facing = opposite_map[elevation_name]

    prompt = (
        f"A builder stands outside in the garden and looks directly at the {elevation_name} Elevation of a house.\n"
        f"In which compass direction is the builder physically facing while looking at this wall?"
    )

    correct_ans = observer_facing
    custom_opts = ["North", "South", "East", "West"]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Recall the definition of the {elevation_name} Elevation [1 mark].\n"
        f"The {elevation_name} Elevation is the side of the house that faces {elevation_name}.\n"
        f"Step 2: Determine observer's line of sight [1 mark].\n"
        f"If the wall faces {elevation_name}, a person standing outside looking towards that wall must look in the opposite direction.\n"
        f"Step 3: Opposite direction [1 mark]: The opposite of {elevation_name} is {observer_facing} ({correct_ans})."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "elevation_compass",
        "title": f"Observer Viewpoint Facing {observer_facing}",
        "target_dir": observer_facing,
        "compass": True,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="12",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The wall faces outward. To look at it from outside, you must face towards the house, which is opposite to the wall's facing direction.",
        tier_2=f"The {elevation_name} wall faces {elevation_name}. Looking at it means facing {observer_facing}.",
        tier_3=f"The observer is facing {observer_facing}.",
        r=r,
    )


def generate_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Passive solar heating principles for South African home design."""
    name = r.choice(SA_NAMES)

    prompt = (
        f"In South Africa (located in the Southern Hemisphere), architects strongly recommend that the main living "
        f"areas and large windows of a house should be placed along the North Elevation.\n"
        f"What is the mathematical and environmental reason for this design principle?"
    )

    correct_ans = (
        "In the Southern Hemisphere, the sun is positioned in the northern sky, maximizing natural winter warmth and sunlight"
    )
    wrong_1 = "The South African prevailing winds blow from the North, which prevents dust from entering the house"
    wrong_2 = "The sun rises in the North and sets in the South throughout the year in South Africa"
    wrong_3 = "North-facing walls receive zero sunlight, which keeps the house completely dark and cold"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Geographic orientation in Southern Hemisphere [1 mark].\n"
        f"South Africa lies south of the Equator, meaning the midday sun is always in the northern half of the sky.\n"
        f"Step 2: Solar trajectory in winter vs summer [1 mark].\n"
        f"In winter, the sun travels at a lower angle from the North, allowing sunlight to penetrate deep into north-facing rooms.\n"
        f"Step 3: Conclusion [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "elevation_compass",
        "title": f"Passive Solar Orientation (North Wall - Design #{r.randint(10, 99)})",
        "target_dir": "North",
        "compass": True,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="13",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Consider the path of the sun in the Southern Hemisphere.",
        tier_2="In South Africa, the sun passes through the northern sky at noon, giving the most solar energy to north-facing walls.",
        tier_3=f"Correct reason: {correct_ans}.",
        r=r,
    )


def generate_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Subskill 14: Determine wall and roof ridge height from elevation plan with scale 1:100."""
    name = r.choice(SA_NAMES)
    wall_h_cm = r.choice([2.6, 2.8, 3.0, 3.2])
    roof_rise_cm = r.choice([1.2, 1.4, 1.5, 1.8])
    total_h_cm = round(wall_h_cm + roof_rise_cm, 2)

    real_wall_m = wall_h_cm  # on 1:100, 1 cm = 1 m
    real_ridge_m = total_h_cm

    prompt = (
        f"On a South Elevation plan rendered at a scale ratio of 1:100, the vertical height from ground level to the ceiling "
        f"eaves measures {_fmt(wall_h_cm)} cm, and the additional rise from the eaves to the apex of the roof ridge "
        f"measures {_fmt(roof_rise_cm)} cm.\n"
        f"Calculate the actual total height of the house from the ground to the roof ridge apex in metres."
    )

    correct_ans = f"{_fmt(real_ridge_m)} m"
    wrong_1 = f"{_fmt(real_wall_m)} m"
    wrong_2 = f"{_fmt(roof_rise_cm)} m"
    wrong_3 = f"{_fmt(real_ridge_m * 10)} m"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate total drawing height [1 mark].\n"
        f"Total drawing height = Wall height + Roof rise = {_fmt(wall_h_cm)} cm + {_fmt(roof_rise_cm)} cm = {_fmt(total_h_cm)} cm.\n"
        f"Step 2: Apply scale 1:100 [1 mark].\n"
        f"Scale 1:100 means 1 cm on paper = 100 cm = 1 m in real life.\n"
        f"Step 3: Stated real height [1 mark]: {_fmt(total_h_cm)} cm × 1 m/cm = {_fmt(real_ridge_m)} m ({correct_ans})."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Wall & Roof Ridge Elevation ({real_wall_m} m)",
        "height_m": real_wall_m,
        "roof": {"rise_m": roof_rise_cm},
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="14",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the drawing height of the wall and roof, then apply the 1:100 scale (1 cm = 1 m).",
        tier_2=f"Total plan height = {_fmt(wall_h_cm)} + {_fmt(roof_rise_cm)} = {_fmt(total_h_cm)} cm.",
        tier_3=f"At 1:100 scale, {_fmt(total_h_cm)} cm = {_fmt(real_ridge_m)} m.",
        r=r,
    )


def generate_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Subskill 15: Calculate net wall surface area (gross area minus windows and doors)."""
    name = r.choice(SA_NAMES)
    wall_l = r.choice([8.0, 9.0, 10.0, 11.0, 12.0])
    wall_h = r.choice([2.7, 2.8, 3.0])
    gross_area = round(wall_l * wall_h, 2)

    # Windows and doors
    door_area = round(0.9 * 2.1, 2)  # 1.89 m²
    num_windows = r.choice([2, 3])
    win_w = 1.5
    win_h = 1.2
    single_win_area = round(win_w * win_h, 2)  # 1.80 m²
    total_win_area = round(num_windows * single_win_area, 2)

    openings_area = round(door_area + total_win_area, 2)
    net_area = round(gross_area - openings_area, 2)

    prompt = (
        f"{name} is calculating the net wall area of the North Elevation to be plastered. "
        f"The rectangular exterior wall has a length of {_fmt(wall_l)} m and a height of {_fmt(wall_h)} m. "
        f"The wall contains one exterior door measuring 0,90 m by 2,10 m, and {num_windows} identical windows "
        f"each measuring 1,50 m wide by 1,20 m high.\n"
        f"Calculate the net wall surface area in square metres (m²) after subtracting all door and window openings."
    )

    correct_ans = f"{_fmt(net_area)} m²"
    wrong_1 = f"{_fmt(gross_area)} m²"  # forgot openings
    wrong_2 = f"{_fmt(gross_area - door_area)} m²"
    wrong_3 = f"{_fmt(net_area + 4.5)} m²"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate gross wall area [1 mark].\n"
        f"Gross Area = Length × Height = {_fmt(wall_l)} m × {_fmt(wall_h)} m = {_fmt(gross_area)} m².\n"
        f"Step 2: Calculate total area of openings [1 mark].\n"
        f"Door area = 0,90 m × 2,10 m = {_fmt(door_area)} m².\n"
        f"Windows area = {num_windows} × (1,50 m × 1,20 m) = {num_windows} × {_fmt(single_win_area)} m² = {_fmt(total_win_area)} m².\n"
        f"Total openings = {_fmt(door_area)} + {_fmt(total_win_area)} = {_fmt(openings_area)} m².\n"
        f"Step 3: Subtract openings from gross area [1 mark].\n"
        f"Net Area = {_fmt(gross_area)} - {_fmt(openings_area)} = {_fmt(net_area)} m² ({correct_ans})."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Net Wall Surface Area ({wall_l} m × {wall_h} m)",
        "width_m": wall_l,
        "height_m": wall_h,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="15",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Net Wall Area = Gross Wall Area - (Total Window Area + Total Door Area).",
        tier_2=f"Gross area = {_fmt(gross_area)} m². Openings = {_fmt(door_area)} + {_fmt(total_win_area)} = {_fmt(openings_area)} m².",
        tier_3=f"Net area = {_fmt(gross_area)} - {_fmt(openings_area)} = {_fmt(net_area)} m².",
        r=r,
    )


def generate_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Subskill 16: Exterior paint coverage calculation and tin procurement."""
    name = r.choice(SA_NAMES)
    net_area = r.choice([48.0, 56.0, 64.0, 72.0, 80.0, 96.0])
    coverage_rate = r.choice([8.0, 9.0, 10.0])  # m² per litre for one coat
    num_coats = 2

    total_paint_area = net_area * num_coats
    litres_needed = total_paint_area / coverage_rate
    tins_5l = math.ceil(litres_needed / 5.0)

    prompt = (
        f"{name} needs to apply {num_coats} coats of exterior acrylic paint to a wall with a net surface area of "
        f"{_fmt(net_area)} m². "
        f"The manufacturer specifies a coverage rate of {_fmt(coverage_rate)} m² per litre per coat. "
        f"The paint is sold strictly in 5-litre tins.\n"
        f"Calculate the minimum number of 5-litre tins {name} must buy to complete the two coats."
    )

    correct_ans = f"{tins_5l} tins (5 L each)"
    wrong_1 = f"{math.ceil(litres_needed / 5.0) + 1} tins (5 L each)"
    wrong_2 = f"{math.ceil(net_area / coverage_rate / 5.0)} tins (5 L each)"  # only 1 coat
    wrong_3 = f"{tins_5l + 3} tins (5 L each)"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate total area to be painted for {num_coats} coats [1 mark].\n"
        f"Total area = {_fmt(net_area)} m² × {num_coats} = {_fmt(total_paint_area)} m².\n"
        f"Step 2: Calculate total litres required [1 mark].\n"
        f"Litres = Total Area ÷ Coverage Rate = {_fmt(total_paint_area)} ÷ {_fmt(coverage_rate)} = {_fmt(litres_needed, 1)} L.\n"
        f"Step 3: Determine number of 5 L tins (round up) [1 mark].\n"
        f"Tins = {_fmt(litres_needed, 1)} ÷ 5 = {_fmt(litres_needed / 5.0, 2)} → rounded up to whole tin = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="16",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply net area by 2 coats, divide by coverage rate to find litres, then divide by 5 and round up.",
        tier_2=f"Total area for 2 coats = {_fmt(total_paint_area)} m². Litres = {_fmt(total_paint_area)} ÷ {_fmt(coverage_rate)} = {_fmt(litres_needed, 1)} L.",
        tier_3=f"{_fmt(litres_needed, 1)} L ÷ 5 L/tin = {_fmt(litres_needed / 5.0, 1)} → buy {tins_5l} tins.",
        r=r,
    )


def generate_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Subskill 17: Match elevation openings to corresponding rooms on floor plan."""
    name = r.choice(SA_NAMES)
    direction = r.choice(["East", "West", "North", "South"])
    room = r.choice(["Master Bedroom", "Kitchen", "Lounge", "Family Bathroom"])

    prompt = (
        f"On the {direction} Elevation drawing of a house, Window W2 is located 1,5 metres from the left-hand corner. "
        f"Examining the floor plan on the same {direction} side, which room corresponds to the location of Window W2?"
    )

    correct_ans = room
    distractors = [r_name for r_name in ["Master Bedroom", "Kitchen", "Lounge", "Family Bathroom", "Garage", "Scullery"] if r_name != room][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Locate the {direction} wall on the floor plan [1 mark].\n"
        f"Identify the corresponding exterior wall that faces {direction}.\n"
        f"Step 2: Measure offset from the left corner on the floor plan [1 mark].\n"
        f"At 1,5 m from the corner, Window W2 opens into the {room}.\n"
        f"Step 3: Stated room [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Elevation Openings ({direction} Elevation - {room})",
        "side": direction,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="17",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Cross-reference the position of the window on the elevation view with the floor plan layout.",
        tier_2=f"Look at the {direction} wall on the floor plan 1,5 m from the reference corner.",
        tier_3=f"The window belongs to the {room}.",
        r=r,
    )


def generate_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Subskill 18: Roof pitch / slope ratio calculation from elevation view."""
    name = r.choice(SA_NAMES)
    rise_m = r.choice([1.0, 1.2, 1.5, 1.8, 2.0])
    run_m = r.choice([3.0, 3.6, 4.0, 4.5, 5.0])

    pitch_ratio = round(rise_m / run_m, 2)
    angle_deg = round(math.degrees(math.atan(rise_m / run_m)), 1)

    prompt = (
        f"On an architectural side elevation drawing, a pitched roof rises vertically by {_fmt(rise_m)} m (the rise) "
        f"over a horizontal distance of {_fmt(run_m)} m from the eaves to the ridge (the run).\n"
        f"Calculate the roof slope (pitch) as a simplified fraction or ratio (Rise : Run)."
    )

    # Simplified ratio
    gcd_val = math.gcd(int(rise_m * 10), int(run_m * 10))
    num = int(rise_m * 10) // gcd_val
    den = int(run_m * 10) // gcd_val
    correct_ans = f"{num} : {den} (or gradient of {_fmt(pitch_ratio)})"
    wrong_1 = f"{den} : {num} (or gradient of {_fmt(round(den / num, 2))})"
    wrong_2 = f"1 : {_fmt(int(den * 1.5))}"
    wrong_3 = f"2 : {den + 1}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State the formula for slope / pitch [1 mark].\n"
        f"Slope = Rise ÷ Run = {_fmt(rise_m)} m ÷ {_fmt(run_m)} m.\n"
        f"Step 2: Express as simplified ratio [1 mark].\n"
        f"{_fmt(rise_m)} : {_fmt(run_m)} = {num} : {den}.\n"
        f"Step 3: Stated ratio and gradient [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="18",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Roof slope / pitch = Vertical Rise ÷ Horizontal Run.",
        tier_2=f"Divide vertical rise {_fmt(rise_m)} m by horizontal run {_fmt(run_m)} m.",
        tier_3=f"The simplified ratio is {num} : {den}.",
        r=r,
    )
