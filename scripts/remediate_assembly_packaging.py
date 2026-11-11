"""Remediation for scaled_plans_costs.py (Grade 10)."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "caps-ai-backend", "app", "utils", "mathematical_literacy", "assembly_packaging")

def remediate_scaled_plans_costs():
    p = os.path.join(BASE, "scaled_plans_costs.py")
    code = open(p, encoding="utf-8").read()

    # 27. asm_plan_scale_number_ratio_room_dimension
    old_p27 = '''def _gen_asm_plan_scale_number_ratio_room_dimension(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    room = r.choice(["main bedroom", "classroom", "lounge", "dining room"])
    scale_val = r.choice([50, 100])
    plan_cm = r.choice([8.0, 9.5, 11.0, 12.0, 13.5, 14.0])
    real_cm = plan_cm * scale_val
    real_m = real_cm / 100.0

    prompt = (
        f"{name} measures the length of the {room} on an architectural floor plan using a ruler. "
        f"The measurement on the drawing is {_fmt(plan_cm)} cm.\\n\\n"
        f"The plan is drawn to a scale of 1 : {scale_val}.\\n\\n"
        f"Calculate the actual (real-life) length of the {room} in metres (m)."
    )'''
    new_p27 = '''def _gen_asm_plan_scale_number_ratio_room_dimension(r: random.Random) -> Dict[str, Any]:
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
        f"{name} measures the length of the {room} on the accompanying architectural floor plan using a ruler.\\n\\n"
        f"The measurement on the drawing is {_fmt(plan_cm)} cm.\\n"
        f"The plan is drawn to a scale of 1 : {scale_val}.\\n\\n"
        f"Calculate the actual (real-life) length of the {room} in metres (m)."
    )'''
    code = code.replace(old_p27, new_p27)
    code = code.replace(
        'tier_3_hint=f"{_fmt(real_cm)} ÷ 100 = {_fmt(real_m)} m.",\n    )',
        'tier_3_hint=f"{_fmt(real_cm)} ÷ 100 = {_fmt(real_m)} m.",\n        diagram_spec=diag,\n    )'
    )

    # 28. asm_plan_scale_inverse_real_to_drawing_length
    old_p28 = '''def _gen_asm_plan_scale_inverse_real_to_drawing_length(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    scale_val = r.choice([50, 100])
    real_m = r.choice([4.5, 5.0, 6.0, 7.5, 8.0, 9.0])
    real_cm = real_m * 100.0
    drawing_cm = real_cm / scale_val

    prompt = (
        f"An architectural draughtsman is drafting a floor plan to a scale of 1 : {scale_val}.\\n\\n"
        f"A real-world rectangular classroom has an actual length of {_fmt(real_m)} m.\\n\\n"
        f"Determine the length (in cm) that the draughtsman must draw on the paper to represent this classroom."
    )'''
    new_p28 = '''def _gen_asm_plan_scale_inverse_real_to_drawing_length(r: random.Random) -> Dict[str, Any]:
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
        f"An architectural draughtsman is drafting a floor plan to a scale of 1 : {scale_val} (see accompanying layout).\\n\\n"
        f"A real-world rectangular classroom has an actual length of {_fmt(real_m)} m.\\n\\n"
        f"Determine the length (in cm) that the draughtsman must draw on the paper to represent this classroom."
    )'''
    code = code.replace(old_p28, new_p28)
    code = code.replace(
        'tier_3_hint=f"{_fmt(real_cm)} ÷ {scale_val} = {_fmt(drawing_cm)} cm.",\n    )',
        'tier_3_hint=f"{_fmt(real_cm)} ÷ {scale_val} = {_fmt(drawing_cm)} cm.",\n        diagram_spec=diag,\n    )'
    )

    # 29. asm_plan_bar_scale_measurement_conversion
    old_p29 = '''def _gen_asm_plan_bar_scale_measurement_conversion(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    bar_cm = r.choice([2.0, 2.5, 3.0])  # length of bar segment on paper
    bar_m = r.choice([1.0, 2.0, 5.0])    # real distance represented by bar segment
    measured_cm = round(bar_cm * r.choice([3, 4, 5, 6]), 1)
    real_m = round((measured_cm / bar_cm) * bar_m, 2)

    prompt = (
        f"A house extension floor plan includes a graphic bar scale.\\n"
        f"On the printed paper, a {_fmt(bar_cm)} cm segment on the bar scale represents an actual distance of {_fmt(bar_m)} m.\\n\\n"
        f"{name} measures the width of the new open-plan patio on the plan and finds it measures {_fmt(measured_cm)} cm.\\n\\n"
        f"Using the bar scale ratio, calculate the actual real-life width of the patio (in metres)."
    )'''
    new_p29 = '''def _gen_asm_plan_bar_scale_measurement_conversion(r: random.Random) -> Dict[str, Any]:
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
        f"A house extension floor plan includes the accompanying graphic bar scale.\\n"
        f"On the printed paper, a {_fmt(bar_cm)} cm segment on the bar scale represents an actual distance of {_fmt(bar_m)} m.\\n\\n"
        f"{name} measures the width of the new open-plan patio on the plan and finds it measures {_fmt(measured_cm)} cm.\\n\\n"
        f"Using the bar scale, calculate the actual real-life width of the patio (in metres)."
    )'''
    code = code.replace(old_p29, new_p29)
    code = code.replace(
        'tier_3_hint=f"Actual width = {_fmt(real_m)} m.",\n    )',
        'tier_3_hint=f"Actual width = {_fmt(real_m)} m.",\n        diagram_spec=diag,\n    )'
    )

    # 30. asm_plan_total_floor_area_calculation
    old_p30 = '''def _gen_asm_plan_total_floor_area_calculation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    length_m = r.choice([4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
    width_m = r.choice([3.0, 3.5, 4.0, 4.2, 4.5])
    area = round(length_m * width_m, 2)

    prompt = (
        f"{name} is calculating the floor dimensions for a rectangular master bedroom.\\n"
        f"The room has an actual length of {_fmt(length_m)} m and a width of {_fmt(width_m)} m.\\n\\n"
        f"Formula: Area = Length × Width\\n\\n"
        f"Calculate the total floor surface area of the room in square metres (m²)."
    )'''
    new_p30 = '''def _gen_asm_plan_total_floor_area_calculation(r: random.Random) -> Dict[str, Any]:
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
        f"{name} is calculating the floor dimensions for a rectangular master bedroom (refer to the accompanying floor plan).\\n"
        f"The room has an actual length of {_fmt(length_m)} m and a width of {_fmt(width_m)} m.\\n\\n"
        f"Formula: Area = Length × Width\\n\\n"
        f"Calculate the total floor surface area of the room in square metres (m²)."
    )'''
    code = code.replace(old_p30, new_p30)
    code = code.replace(
        'tier_3_hint=f"{_fmt(length_m)} × {_fmt(width_m)} = {_fmt(area)} m².",\n    )',
        'tier_3_hint=f"{_fmt(length_m)} × {_fmt(width_m)} = {_fmt(area)} m².",\n        diagram_spec=diag,\n    )'
    )

    # 31. asm_plan_floor_tiling_box_estimate_and_wastage
    old_p31 = '''def _gen_asm_plan_floor_tiling_box_estimate_and_wastage(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    area_m2 = r.choice([18.0, 22.5, 25.0, 28.0, 32.0, 36.5])
    box_coverage_m2 = r.choice([2.0, 2.5, 3.0, 4.0])
    # 10% wastage
    total_area_with_wastage = round(area_m2 * 1.10, 2)
    raw_boxes = total_area_with_wastage / box_coverage_m2
    boxes_needed = math.ceil(raw_boxes)

    prompt = (
        f"{name} plans to tile a kitchen floor with an area of {_fmt(area_m2)} m².\\n\\n"
        f"Tiling guidelines:\\n"
        f"• Add 10% extra area to allow for cutting, trimming, and tile breakage wastage.\\n"
        f"• Ceramic floor tiles are sold only in full boxes, with each box covering exactly {_fmt(box_coverage_m2)} m².\\n\\n"
        f"Calculate the minimum number of full boxes of tiles that {name} must purchase."
    )'''
    new_p31 = '''def _gen_asm_plan_floor_tiling_box_estimate_and_wastage(r: random.Random) -> Dict[str, Any]:
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
        f"{name} plans to tile a kitchen floor with an area of {_fmt(area_m2)} m² (refer to the accompanying floor plan).\\n\\n"
        f"Tiling guidelines:\\n"
        f"• Add 10% extra area to allow for cutting, trimming, and tile breakage wastage.\\n"
        f"• Ceramic floor tiles are sold only in full boxes, with each box covering exactly {_fmt(box_coverage_m2)} m².\\n\\n"
        f"Calculate the minimum number of full boxes of tiles that {name} must purchase."
    )'''
    code = code.replace(old_p31, new_p31)
    code = code.replace(
        'tier_3_hint=f"Always round UP for tile boxes: {boxes_needed} boxes.",\n    )',
        'tier_3_hint=f"Always round UP for tile boxes: {boxes_needed} boxes.",\n        diagram_spec=diag,\n    )'
    )

    # 32. asm_plan_floor_tiling_total_cost
    old_p32 = '''def _gen_asm_plan_floor_tiling_total_cost(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    boxes = r.choice([7, 8, 9, 11, 12, 14])
    price_per_box = r.choice([145.0, 160.0, 185.0, 199.95, 220.0, 245.50])
    total_cost = round(boxes * price_per_box, 2)

    prompt = (
        f"{name} is buying tiles to renovate a dining room floor.\\n"
        f"After accounting for room area and cutting wastage, {name} requires {boxes} boxes of porcelain floor tiles.\\n"
        f"Each box costs {_fmt_curr(price_per_box)} (VAT inclusive).\\n\\n"
        f"Calculate the total cost of the tiles for this renovation project."
    )'''
    new_p32 = '''def _gen_asm_plan_floor_tiling_total_cost(r: random.Random) -> Dict[str, Any]:
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
        f"{name} is buying tiles to renovate a dining room floor (see floor layout).\\n"
        f"After accounting for room area and cutting wastage, {name} requires {boxes} boxes of porcelain floor tiles.\\n"
        f"Each box costs {_fmt_curr(price_per_box)} (VAT inclusive).\\n\\n"
        f"Calculate the total cost of the tiles for this renovation project."
    )'''
    code = code.replace(old_p32, new_p32)
    code = code.replace(
        'tier_3_hint=f"Total cost = {_fmt_curr(total_cost)}.",\n    )',
        'tier_3_hint=f"Total cost = {_fmt_curr(total_cost)}.",\n        diagram_spec=diag,\n    )'
    )

    # 33. asm_plan_skirting_board_perimeter_deducting_doors
    old_p33 = '''def _gen_asm_plan_skirting_board_perimeter_deducting_doors(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    length_m = r.choice([4.8, 5.2, 5.5, 6.0])
    width_m = r.choice([3.2, 3.6, 4.0, 4.5])
    doors = r.choice([1, 2])
    door_width_m = 0.85
    total_door_width = round(doors * door_width_m, 2)
    room_perimeter = round(2 * (length_m + width_m), 2)
    skirting_len = round(room_perimeter - total_door_width, 2)

    prompt = (
        f"{name} is installing timber skirting boards around the base of the walls of a bedroom.\\n\\n"
        f"Room details:\\n"
        f"• Room dimensions: Length = {_fmt(length_m)} m, Width = {_fmt(width_m)} m\\n"
        f"• The bedroom has {doors} doorway(s), each {_fmt(door_width_m)} m wide\\n\\n"
        f"Skirting boards are NOT installed across doorway openings.\\n\\n"
        f"Calculate the total linear metres of skirting board required for the bedroom."
    )'''
    new_p33 = '''def _gen_asm_plan_skirting_board_perimeter_deducting_doors(r: random.Random) -> Dict[str, Any]:
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
        f"{name} is installing timber skirting boards around the base of the walls of a bedroom (refer to the floor plan).\\n\\n"
        f"Room details:\\n"
        f"• Room dimensions: Length = {_fmt(length_m)} m, Width = {_fmt(width_m)} m\\n"
        f"• The bedroom has {doors} doorway(s), each {_fmt(door_width_m)} m wide\\n\\n"
        f"Skirting boards are NOT installed across doorway openings.\\n\\n"
        f"Calculate the total linear metres of skirting board required for the bedroom."
    )'''
    code = code.replace(old_p33, new_p33)
    code = code.replace(
        'tier_3_hint=f"{_fmt(room_perimeter)} − {_fmt(total_door_width)} = {_fmt(skirting_len)} m.",\n    )',
        'tier_3_hint=f"{_fmt(room_perimeter)} − {_fmt(total_door_width)} = {_fmt(skirting_len)} m.",\n        diagram_spec=diag,\n    )'
    )

    # 34. asm_plan_wall_painting_surface_area_deducting_openings
    old_p34 = '''def _gen_asm_plan_wall_painting_surface_area_deducting_openings(r: random.Random) -> Dict[str, Any]:
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

    prompt = (
        f"{name} wants to paint the four interior walls of a bedroom.\\n\\n"
        f"Dimensions & Openings:\\n"
        f"• Room dimensions: Length = {_fmt(length_m)} m, Width = {_fmt(width_m)} m, Height = {_fmt(height_m)} m\\n"
        f"• 1 door with a surface area of {_fmt(door_area_m2)} m²\\n"
        f"• {windows} window(s), each with a surface area of {_fmt(win_area_per_win)} m²\\n\\n"
        f"Formula: Total Wall Area = 2 × (Length + Width) × Height\\n\\n"
        f"Calculate the net wall surface area (in m²) that must be painted after deducting the door and window openings."
    )'''
    new_p34 = '''def _gen_asm_plan_wall_painting_surface_area_deducting_openings(r: random.Random) -> Dict[str, Any]:
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
        f"{name} wants to paint the four interior walls of a bedroom (refer to the floor plan layout).\\n\\n"
        f"Dimensions & Openings:\\n"
        f"• Room dimensions: Length = {_fmt(length_m)} m, Width = {_fmt(width_m)} m, Height = {_fmt(height_m)} m\\n"
        f"• 1 door with a surface area of {_fmt(door_area_m2)} m²\\n"
        f"• {windows} window(s), each with a surface area of {_fmt(win_area_per_win)} m²\\n\\n"
        f"Formula: Total Wall Area = 2 × (Length + Width) × Height\\n\\n"
        f"Calculate the net wall surface area (in m²) that must be painted after deducting the door and window openings."
    )'''
    code = code.replace(old_p34, new_p34)
    code = code.replace(
        'tier_3_hint=f"{_fmt(gross_wall_area)} − {_fmt(total_openings)} = {_fmt(net_paint_area)} m².",\n    )',
        'tier_3_hint=f"{_fmt(gross_wall_area)} − {_fmt(total_openings)} = {_fmt(net_paint_area)} m².",\n        diagram_spec=diag,\n    )'
    )

    # 35. asm_plan_rental_cost_per_square_metre
    old_p35 = '''def _gen_asm_plan_rental_cost_per_square_metre(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    length_m = r.choice([6.0, 7.0, 7.5, 8.0])
    width_m = r.choice([5.0, 5.5, 6.0])
    flat_area_m2 = round(length_m * width_m, 2)
    rate_per_m2 = r.choice([85.0, 90.0, 95.0, 105.0, 110.0, 120.0])
    monthly_rent = round(flat_area_m2 * rate_per_m2, 2)

    prompt = (
        f"{name} is considering renting an open-plan studio flat.\\n\\n"
        f"According to the scaled floor plan, the flat is rectangular with dimensions:\\n"
        f"• Length = {_fmt(length_m)} m\\n"
        f"• Width = {_fmt(width_m)} m\\n\\n"
        f"The landlord charges rent at a fixed rate of {_fmt_curr(rate_per_m2)} per square metre (m²) per month.\\n\\n"
        f"Calculate {name}'s total monthly rent in Rands."
    )'''
    new_p35 = '''def _gen_asm_plan_rental_cost_per_square_metre(r: random.Random) -> Dict[str, Any]:
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
        f"{name} is considering renting an open-plan studio flat.\\n\\n"
        f"According to the accompanying scaled floor plan, the flat is rectangular with dimensions:\\n"
        f"• Length = {_fmt(length_m)} m\\n"
        f"• Width = {_fmt(width_m)} m\\n\\n"
        f"The landlord charges rent at a fixed rate of {_fmt_curr(rate_per_m2)} per square metre (m²) per month.\\n\\n"
        f"Calculate {name}'s total monthly rent in Rands."
    )'''
    code = code.replace(old_p35, new_p35)
    code = code.replace(
        'tier_3_hint=f"{_fmt(flat_area_m2)} × {_fmt(rate_per_m2)} = {_fmt_curr(monthly_rent)}.",\n    )',
        'tier_3_hint=f"{_fmt(flat_area_m2)} × {_fmt(rate_per_m2)} = {_fmt_curr(monthly_rent)}.",\n        diagram_spec=diag,\n    )'
    )

    with open(p, "w", encoding="utf-8") as f:
        f.write(code)
    print("remediated scaled_plans_costs.py")

remediate_scaled_plans_costs()
