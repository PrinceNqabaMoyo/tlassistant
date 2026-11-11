"""Cluster 4: Scaled Floor Plans & Cost Calculations (Subskills 27 to 35).

Covers:
27. Scale ratio conversion from plan drawing measurement to real-life dimensions (1:50, 1:100)
28. Inverse scale conversion: real-life room dimensions to drawing lengths on paper
29. Graphical bar scale interpretation and real-world distance derivation
30. Total floor area calculations for rectangular rooms (Area = L × W)
31. Floor tiling box estimation with rounding up and cutting wastage margins
32. Total material cost calculation for floor coverings and tiles
33. Skirting board linear perimeter calculation deducting doorway openings
34. Wall surface area calculation for painting deducting doors and windows
35. Residential apartment rental calculation based on floor area rate (R/m²)
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _build_question_payload,
)


def _gen_asm_plan_scale_number_ratio_room_dimension(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    room = r.choice(["main bedroom", "classroom", "lounge", "dining room"])
    scale_val = r.choice([50, 100])
    plan_cm = r.choice([8.0, 9.5, 11.0, 12.0, 13.5, 14.0])
    real_cm = plan_cm * scale_val
    real_m = real_cm / 100.0

    diag = {
        "kind": "floor_plan",
        "title": f"Architectural Floor Plan (Scale 1 : {scale_val})",
        "scale": f"1 : {scale_val}",
        "rooms": [
            {"name": room.title(), "dims": f"{_fmt(plan_cm)} cm on drawing", "length_m": real_m, "width_m": round(real_m * 0.7, 1)},
        ],
        "length_m": real_m,
        "width_m": round(real_m * 0.7, 1),
    }

    prompt = (
        f"{name} measures the length of the {room} on the accompanying architectural floor plan using a ruler.\n\n"
        f"Drawing ruler reading: {_fmt(plan_cm)} cm.\n"
        f"Blueprint scale ratio: 1 : {scale_val}.\n\n"
        f"Calculate the actual (real-life) length of the {room} in metres (m)."
    )
    ans = f"{_fmt(real_m)} m"

    s1 = f"Multiply the plan measurement ({_fmt(plan_cm)} cm) by the scale factor ({scale_val}) to get real-life centimetres, then divide by 100 to convert to metres."
    s2 = f"✓ [1 Mark: Method – Scaling and unit conversion to metres]\nReal distance (cm) = {_fmt(plan_cm)} cm × {scale_val} = {_fmt(real_cm)} cm.\nReal distance (m) = {_fmt(real_cm)} cm ÷ 100."
    s3 = f"✓ [1 Mark: Accuracy – Real-life dimension in metres]\nActual length = {_fmt(real_m)} m."

    return _build_question_payload(
        "asm_plan_scale_number_ratio_room_dimension",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Scale 1 : {scale_val} means 1 cm on paper equals {scale_val} cm in real life.",
        tier_2_hint=f"Real cm = {_fmt(plan_cm)} × {scale_val} = {_fmt(real_cm)} cm. Convert to metres by dividing by 100.",
        tier_3_hint=f"{_fmt(real_cm)} ÷ 100 = {_fmt(real_m)} m.",
        diagram_spec=diag,
    )

    diag = {
        "kind": "floor_plan",
        "title": f"Architectural Floor Plan (Scale 1 : {scale_val})",
        "scale": f"1 : {scale_val}",
        "rooms": [
            {"name": room.title(), "dims": f"{_fmt(plan_cm)} cm on drawing", "length_m": real_m, "width_m": round(real_m * 0.7, 1)},
        ],
        "length_m": real_m,
        "width_m": round(real_m * 0.7, 1),
    }

    prompt = (
        f"{name} measures the length of the {room} on the accompanying architectural floor plan using a ruler.\n\n"
        f"The measurement on the drawing is {_fmt(plan_cm)} cm.\n"
        f"The plan blueprint scale ratio is 1 : {scale_val}.\n\n"
        f"Calculate the actual (real-life) length of the {room} in metres (m)."
    )
    ans = f"{_fmt(real_m)} m"

    s1 = f"Multiply the plan measurement ({_fmt(plan_cm)} cm) by the scale factor ({scale_val}) to get real-life centimetres, then divide by 100 to convert to metres."
    s2 = f"✓ [1 Mark: Method – Scaling and unit conversion to metres]\nReal distance (cm) = {_fmt(plan_cm)} cm × {scale_val} = {_fmt(real_cm)} cm.\nReal distance (m) = {_fmt(real_cm)} cm ÷ 100."
    s3 = f"✓ [1 Mark: Accuracy – Real-life dimension in metres]\nActual length = {_fmt(real_m)} m."

    return _build_question_payload(
        "asm_plan_scale_number_ratio_room_dimension",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Scale 1 : {scale_val} means 1 cm on paper equals {scale_val} cm in real life.",
        tier_2_hint=f"Real cm = {_fmt(plan_cm)} × {scale_val} = {_fmt(real_cm)} cm. Convert to metres by dividing by 100.",
        tier_3_hint=f"{_fmt(real_cm)} ÷ 100 = {_fmt(real_m)} m.",
        diagram_spec=diag,
    )


def _gen_asm_plan_scale_inverse_real_to_drawing_length(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    scale_val = r.choice([50, 100])
    real_m = r.choice([4.5, 5.0, 6.0, 7.5, 8.0, 9.0])
    real_cm = real_m * 100.0
    drawing_cm = real_cm / scale_val

    diag = {
        "kind": "floor_plan",
        "title": f"Draughting Plan (Scale 1 : {scale_val})",
        "scale": f"1 : {scale_val}",
        "rooms": [
            {"name": "Classroom", "dims": f"Real: {_fmt(real_m)} m", "length_m": real_m, "width_m": round(real_m * 0.6, 1)},
        ],
        "length_m": real_m,
        "width_m": round(real_m * 0.6, 1),
    }

    prompt = (
        f"An architectural draughtsman is drafting a floor plan to a scale of 1 : {scale_val} (see accompanying layout).\n\n"
        f"A real-world rectangular classroom has an actual length of {_fmt(real_m)} m.\n\n"
        f"Determine the length (in cm) that the draughtsman must draw on the paper to represent this classroom."
    )
    ans = f"{_fmt(drawing_cm)} cm"

    s1 = f"Convert real-life dimension from metres to centimetres (multiply by 100), then divide by scale factor ({scale_val}) to find drawing length on paper."
    s2 = f"✓ [1 Mark: Method – Converting metres to cm and dividing by scale ratio]\nReal length = {_fmt(real_m)} m × 100 = {_fmt(real_cm)} cm.\nDrawing length = {_fmt(real_cm)} cm ÷ {scale_val}."
    s3 = f"✓ [1 Mark: Accuracy – Drawing length in cm]\nDrawing length = {_fmt(drawing_cm)} cm."

    return _build_question_payload(
        "asm_plan_scale_inverse_real_to_drawing_length",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Convert {_fmt(real_m)} m into cm first: {_fmt(real_m)} × 100 = {_fmt(real_cm)} cm.",
        tier_2_hint=f"Divide the real-life centimetres by the scale factor of {scale_val}.",
        tier_3_hint=f"{_fmt(real_cm)} ÷ {scale_val} = {_fmt(drawing_cm)} cm.",
        diagram_spec=diag,
    )


def _gen_asm_plan_bar_scale_measurement_conversion(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    bar_cm = r.choice([2.0, 2.5, 3.0])  # length of bar segment on paper
    bar_m = r.choice([1.0, 2.0, 5.0])    # real distance represented by bar segment
    measured_cm = round(bar_cm * r.choice([3, 4, 5, 6]), 1)
    real_m = round((measured_cm / bar_cm) * bar_m, 2)

    diag = {
        "kind": "bar_scale",
        "title": "House Extension Graphic Bar Scale",
        "segment_value_m": bar_m,
        "scale": f"{_fmt(bar_cm)} cm = {_fmt(bar_m)} m",
        "segments": 4,
        "total_km": bar_m * 4,
    }

    prompt = (
        f"A house extension floor plan includes the accompanying graphic bar scale.\n"
        f"On the printed paper, a {_fmt(bar_cm)} cm segment on the bar scale represents an actual distance of {_fmt(bar_m)} m.\n\n"
        f"{name} measures the width of the new open-plan patio on the plan and finds it measures {_fmt(measured_cm)} cm.\n\n"
        f"Using the bar scale, calculate the actual real-life width of the patio (in metres)."
    )
    ans = f"{_fmt(real_m)} m"

    s1 = f"Set up a direct proportion using the bar scale: {_fmt(bar_cm)} cm on paper = {_fmt(bar_m)} m in reality."
    s2 = f"✓ [1 Mark: Method – Setting up bar scale ratio and cross-multiplying]\nRatio: 1 cm on plan = {_fmt(bar_m)} m ÷ {_fmt(bar_cm)} cm = {_fmt(round(bar_m / bar_cm, 3))} m/cm.\nActual width = {_fmt(measured_cm)} cm × ({_fmt(bar_m)} ÷ {_fmt(bar_cm)})."
    s3 = f"✓ [1 Mark: Accuracy – Real-life distance in metres]\nActual width = {_fmt(real_m)} m."

    return _build_question_payload(
        "asm_plan_bar_scale_measurement_conversion",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"How many {_fmt(bar_cm)} cm segments fit into {_fmt(measured_cm)} cm?",
        tier_2_hint=f"Segments = {_fmt(measured_cm)} ÷ {_fmt(bar_cm)}. Multiply this by {_fmt(bar_m)} m.",
        tier_3_hint=f"Actual width = {_fmt(real_m)} m.",
        diagram_spec=diag,
    )


def _gen_asm_plan_total_floor_area_calculation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    length_m = r.choice([4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
    width_m = r.choice([3.0, 3.5, 4.0, 4.2, 4.5])
    area = round(length_m * width_m, 2)

    diag = {
        "kind": "floor_plan",
        "title": "Master Bedroom Dimensions Plan",
        "scale": "1 : 50",
        "rooms": [
            {"name": "Master Bedroom", "dims": f"{_fmt(length_m)} m × {_fmt(width_m)} m", "length_m": length_m, "width_m": width_m},
        ],
        "length_m": length_m,
        "width_m": width_m,
    }

    prompt = (
        f"{name} is calculating the floor dimensions for a rectangular master bedroom (refer to the accompanying floor plan).\n"
        f"The room has an actual length of {_fmt(length_m)} m and a width of {_fmt(width_m)} m.\n\n"
        f"Formula: Area = Length × Width\n\n"
        f"Calculate the total floor surface area of the room in square metres (m²)."
    )
    ans = f"{_fmt(area)} m²"

    s1 = f"Multiply length ({_fmt(length_m)} m) by width ({_fmt(width_m)} m) to compute 2D rectangular surface area."
    s2 = f"✓ [1 Mark: Method – Area formula setup]\nArea = {_fmt(length_m)} m × {_fmt(width_m)} m."
    s3 = f"✓ [1 Mark: Accuracy – Total floor area]\nArea = {_fmt(area)} m²."

    return _build_question_payload(
        "asm_plan_total_floor_area_calculation",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Area of a rectangle = length × width.",
        tier_2_hint=f"Multiply {_fmt(length_m)} by {_fmt(width_m)}.",
        tier_3_hint=f"{_fmt(length_m)} × {_fmt(width_m)} = {_fmt(area)} m².",
        diagram_spec=diag,
    )


def _gen_asm_plan_floor_tiling_box_estimate_and_wastage(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    area_m2 = r.choice([18.0, 22.5, 25.0, 28.0, 32.0, 36.5])
    box_coverage_m2 = r.choice([2.0, 2.5, 3.0, 4.0])
    total_area_with_wastage = round(area_m2 * 1.10, 2)
    raw_boxes = total_area_with_wastage / box_coverage_m2
    boxes_needed = math.ceil(raw_boxes)

    diag = {
        "kind": "floor_plan",
        "title": "Kitchen Tiling Layout Plan",
        "scale": "1 : 50",
        "rooms": [
            {"name": "Kitchen Floor", "dims": f"Area: {_fmt(area_m2)} m²", "length_m": 6.0, "width_m": round(area_m2 / 6.0, 1)},
        ],
        "length_m": 6.0,
        "width_m": round(area_m2 / 6.0, 1),
    }

    prompt = (
        f"{name} plans to tile a kitchen floor with an area of {_fmt(area_m2)} m² (refer to the accompanying floor plan).\n\n"
        f"Tiling guidelines:\n"
        f"• Add 10% extra area to allow for cutting, trimming, and tile breakage wastage.\n"
        f"• Ceramic floor tiles are sold only in full boxes, with each box covering exactly {_fmt(box_coverage_m2)} m².\n\n"
        f"Calculate the minimum number of full boxes of tiles that {name} must purchase."
    )
    ans = f"{boxes_needed} boxes"

    s1 = f"Add 10% wastage to the room area ({_fmt(area_m2)} m² × 1,10 = {_fmt(total_area_with_wastage)} m²), divide by box coverage ({_fmt(box_coverage_m2)} m²), and round up to the next whole box."
    s2 = f"✓ [1 Mark: Method – Adding 10% wastage and dividing by box coverage]\nTotal area needed = {_fmt(area_m2)} × 1,10 = {_fmt(total_area_with_wastage)} m².\nRaw boxes = {_fmt(total_area_with_wastage)} ÷ {_fmt(box_coverage_m2)} = {_fmt(round(raw_boxes, 2))} boxes."
    s3 = f"✓ [1 Mark: Accuracy – Rounding up to whole integer boxes]\nMust purchase = {boxes_needed} boxes (cannot purchase fraction of a box)."

    return _build_question_payload(
        "asm_plan_floor_tiling_box_estimate_and_wastage",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find 10% extra area: {_fmt(area_m2)} × 1,10 = {_fmt(total_area_with_wastage)} m².",
        tier_2_hint=f"Divide by box coverage: {_fmt(total_area_with_wastage)} ÷ {_fmt(box_coverage_m2)} = {_fmt(round(raw_boxes, 2))}.",
        tier_3_hint=f"Always round UP for tile boxes: {boxes_needed} boxes.",
        diagram_spec=diag,
    )


def _gen_asm_plan_floor_tiling_total_cost(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    boxes = r.choice([7, 8, 9, 11, 12, 14])
    price_per_box = r.choice([145.0, 160.0, 185.0, 199.95, 220.0, 245.50])
    total_cost = round(boxes * price_per_box, 2)

    diag = {
        "kind": "floor_plan",
        "title": "Dining Room Tiling Renovation Plan",
        "scale": "1 : 50",
        "rooms": [
            {"name": "Dining Room", "dims": f"{boxes} boxes required", "length_m": 5.0, "width_m": 4.0},
        ],
        "length_m": 5.0,
        "width_m": 4.0,
    }

    prompt = (
        f"{name} is buying tiles to renovate a dining room floor (see floor layout).\n"
        f"After accounting for room area and cutting wastage, {name} requires {boxes} boxes of porcelain floor tiles.\n"
        f"Each box costs {_fmt_curr(price_per_box)} (VAT inclusive).\n\n"
        f"Calculate the total cost of the tiles for this renovation project."
    )
    ans = _fmt_curr(total_cost)

    s1 = f"Multiply the required number of boxes ({boxes}) by the unit price per box ({_fmt_curr(price_per_box)})."
    s2 = f"✓ [1 Mark: Method – Multiplying box count by box unit price]\nTotal Cost = {boxes} × {_fmt_curr(price_per_box)}."
    s3 = f"✓ [1 Mark: Accuracy – Final Rand cost to 2 decimal places]\nTotal Cost = {_fmt_curr(total_cost)}."

    return _build_question_payload(
        "asm_plan_floor_tiling_total_cost",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Multiply {boxes} boxes by {_fmt_curr(price_per_box)}.",
        tier_2_hint=f"{boxes} × {_fmt(price_per_box)}.",
        tier_3_hint=f"Total cost = {_fmt_curr(total_cost)}.",
        diagram_spec=diag,
    )


def _gen_asm_plan_skirting_board_perimeter_deducting_doors(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    length_m = r.choice([4.8, 5.2, 5.5, 6.0])
    width_m = r.choice([3.2, 3.6, 4.0, 4.5])
    doors = r.choice([1, 2])
    door_width_m = 0.85
    total_door_width = round(doors * door_width_m, 2)
    room_perimeter = round(2 * (length_m + width_m), 2)
    skirting_len = round(room_perimeter - total_door_width, 2)

    diag = {
        "kind": "floor_plan",
        "title": "Bedroom Skirting Board Layout Plan",
        "scale": "1 : 50",
        "rooms": [
            {"name": "Bedroom", "dims": f"{_fmt(length_m)} m × {_fmt(width_m)} m", "length_m": length_m, "width_m": width_m},
        ],
        "length_m": length_m,
        "width_m": width_m,
    }

    prompt = (
        f"{name} is installing timber skirting boards around the base of the walls of a bedroom (refer to the floor plan).\n\n"
        f"Room details:\n"
        f"• Room dimensions: Length = {_fmt(length_m)} m, Width = {_fmt(width_m)} m\n"
        f"• The bedroom has {doors} doorway(s), each {_fmt(door_width_m)} m wide\n\n"
        f"Skirting boards are NOT installed across doorway openings.\n\n"
        f"Calculate the total linear metres of skirting board required for the bedroom."
    )
    ans = f"{_fmt(skirting_len)} m"

    s1 = f"Calculate the full room perimeter (2 × (Length + Width)), then subtract the total width of all doorway openings ({doors} × {_fmt(door_width_m)} m)."
    s2 = f"✓ [1 Mark: Method – Calculating perimeter and subtracting door openings]\nGross perimeter = 2 × ({_fmt(length_m)} + {_fmt(width_m)}) = {_fmt(room_perimeter)} m.\nDoorway deductions = {doors} × {_fmt(door_width_m)} m = {_fmt(total_door_width)} m.\nNet skirting = {_fmt(room_perimeter)} − {_fmt(total_door_width)}."
    s3 = f"✓ [1 Mark: Accuracy – Total linear metres of skirting board]\nRequired skirting = {_fmt(skirting_len)} m."

    return _build_question_payload(
        "asm_plan_skirting_board_perimeter_deducting_doors",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the perimeter of the room first: 2 × ({_fmt(length_m)} + {_fmt(width_m)}) = {_fmt(room_perimeter)} m.",
        tier_2_hint=f"Subtract the doorway opening width ({doors} × {_fmt(door_width_m)} = {_fmt(total_door_width)} m).",
        tier_3_hint=f"{_fmt(room_perimeter)} − {_fmt(total_door_width)} = {_fmt(skirting_len)} m.",
        diagram_spec=diag,
    )


def _gen_asm_plan_wall_painting_surface_area_deducting_openings(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    length_m = r.choice([4.0, 5.0, 5.5])
    width_m = r.choice([3.0, 3.5, 4.0])
    height_m = 2.7  # standard ceiling height
    door_area_m2 = 1.8  # 0.9 m × 2.0 m
    windows = r.choice([1, 2])
    win_area_per_win = 1.2
    total_openings = round(door_area_m2 + (windows * win_area_per_win), 2)
    gross_wall_area = round(2 * (length_m + width_m) * height_m, 2)
    net_paint_area = round(gross_wall_area - total_openings, 2)

    diag = {
        "kind": "floor_plan",
        "title": "Bedroom Wall Dimensions & Openings Plan",
        "scale": "1 : 50",
        "rooms": [
            {"name": "Bedroom", "dims": f"{_fmt(length_m)} m × {_fmt(width_m)} m (H={height_m}m)", "length_m": length_m, "width_m": width_m},
        ],
        "length_m": length_m,
        "width_m": width_m,
    }

    prompt = (
        f"{name} wants to paint the four interior walls of a bedroom (refer to the floor plan layout).\n\n"
        f"Dimensions & Openings:\n"
        f"• Room dimensions: Length = {_fmt(length_m)} m, Width = {_fmt(width_m)} m, Height = {_fmt(height_m)} m\n"
        f"• 1 door with a surface area of {_fmt(door_area_m2)} m²\n"
        f"• {windows} window(s), each with a surface area of {_fmt(win_area_per_win)} m²\n\n"
        f"Formula: Total Wall Area = 2 × (Length + Width) × Height\n\n"
        f"Calculate the net wall surface area (in m²) that must be painted after deducting the door and window openings."
    )
    ans = f"{_fmt(net_paint_area)} m²"

    s1 = f"Calculate the gross area of the four vertical walls (Perimeter × Height), then subtract the combined surface area of the door and windows."
    s2 = f"✓ [1 Mark: Method – Gross wall area calculation and openings deduction]\nGross wall area = 2 × ({_fmt(length_m)} + {_fmt(width_m)}) × {_fmt(height_m)} = {_fmt(gross_wall_area)} m².\nTotal openings = {_fmt(door_area_m2)} + ({windows} × {_fmt(win_area_per_win)}) = {_fmt(total_openings)} m².\nNet area = {_fmt(gross_wall_area)} − {_fmt(total_openings)}."
    s3 = f"✓ [1 Mark: Accuracy – Net painted area in m²]\nNet paint area = {_fmt(net_paint_area)} m²."

    return _build_question_payload(
        "asm_plan_wall_painting_surface_area_deducting_openings",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find total wall area: 2 × ({_fmt(length_m)} + {_fmt(width_m)}) × {_fmt(height_m)} = {_fmt(gross_wall_area)} m².",
        tier_2_hint=f"Total openings to subtract = {_fmt(door_area_m2)} + ({windows} × {_fmt(win_area_per_win)}) = {_fmt(total_openings)} m².",
        tier_3_hint=f"{_fmt(gross_wall_area)} − {_fmt(total_openings)} = {_fmt(net_paint_area)} m².",
        diagram_spec=diag,
    )


def _gen_asm_plan_rental_cost_per_square_metre(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    length_m = r.choice([6.0, 7.0, 7.5, 8.0])
    width_m = r.choice([5.0, 5.5, 6.0])
    flat_area_m2 = round(length_m * width_m, 2)
    rate_per_m2 = r.choice([85.0, 90.0, 95.0, 105.0, 110.0, 120.0])
    monthly_rent = round(flat_area_m2 * rate_per_m2, 2)

    diag = {
        "kind": "floor_plan",
        "title": "Studio Flat Rental Dimensions Plan",
        "scale": "1 : 100",
        "rooms": [
            {"name": "Studio Living/Bed", "dims": f"{_fmt(length_m)} m × {_fmt(width_m)} m", "length_m": length_m, "width_m": width_m},
        ],
        "length_m": length_m,
        "width_m": width_m,
    }

    prompt = (
        f"{name} is considering renting an open-plan studio flat.\n\n"
        f"According to the accompanying scaled floor plan, the flat is rectangular with dimensions:\n"
        f"• Length = {_fmt(length_m)} m\n"
        f"• Width = {_fmt(width_m)} m\n\n"
        f"The landlord charges rent at a fixed rate of {_fmt_curr(rate_per_m2)} per square metre (m²) per month.\n\n"
        f"Calculate {name}'s total monthly rent in Rands."
    )
    ans = _fmt_curr(monthly_rent)

    s1 = f"Calculate the total floor area of the flat (Length × Width = {_fmt(length_m)} × {_fmt(width_m)} = {_fmt(flat_area_m2)} m²), then multiply by the rental rate per m² ({_fmt_curr(rate_per_m2)})."
    s2 = f"✓ [1 Mark: Method – Area calculation and rate multiplication]\nArea = {_fmt(length_m)} m × {_fmt(width_m)} m = {_fmt(flat_area_m2)} m².\nMonthly Rent = {_fmt(flat_area_m2)} m² × {_fmt_curr(rate_per_m2)}/m²."
    s3 = f"✓ [1 Mark: Accuracy – Final monthly rent in Rands]\nMonthly Rent = {_fmt_curr(monthly_rent)}."

    return _build_question_payload(
        "asm_plan_rental_cost_per_square_metre",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the total area of the flat: {_fmt(length_m)} × {_fmt(width_m)} = {_fmt(flat_area_m2)} m².",
        tier_2_hint=f"Multiply the area by {_fmt_curr(rate_per_m2)}.",
        tier_3_hint=f"{_fmt(flat_area_m2)} × {_fmt(rate_per_m2)} = {_fmt_curr(monthly_rent)}.",
        diagram_spec=diag,
    )

DEFAULT_DIAGRAM_ROLE = 'context'
# All diagrams emitted by this generator specify diagram_role: "context" | "identify"
