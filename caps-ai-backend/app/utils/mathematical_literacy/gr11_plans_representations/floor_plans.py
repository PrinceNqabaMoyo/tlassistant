"""Subskills 1 to 9: Floor Plans, Symbols, Dimensions, Area & Clearances for Grade 11 Mathematical Literacy."""
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


def generate_subskill_1(r: random.Random) -> Dict[str, Any]:
    """Subskill 1: Audit and count architectural symbols (doors, windows, rooms) from floor plan."""
    name = r.choice(SA_NAMES)
    num_bed = r.choice([2, 3, 4])
    num_bath = r.choice([1, 2])
    num_ext_doors = r.choice([2, 3])
    num_windows = num_bed * 2 + num_bath + 3  # kitchen/lounge windows

    rooms_list = [f"Bedroom {i+1}" for i in range(num_bed)] + [f"Bathroom {i+1}" for i in range(num_bath)] + ["Kitchen", "Lounge"]
    total_rooms = len(rooms_list)

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "floor_plan",
        "title": f"Floor Plan of {name}'s House",
        "rooms": rooms_list,
        "features": {
            "bedrooms": num_bed,
            "bathrooms": num_bath,
            "exterior_doors": num_ext_doors,
            "windows": num_windows,
        },
        "scale": "1:100",
    }

    feature_to_ask = r.choice([
        ("exterior doors", num_ext_doors, "exterior door symbols (openings in external perimeter walls with swing arcs)"),
        ("windows", num_windows, "standard window symbols (parallel lines within external walls)"),
        ("bedrooms", num_bed, "designated bedroom spaces"),
        ("total distinct rooms (including kitchen and lounge)", total_rooms, "enclosed functional room spaces"),
    ])
    feat_name, feat_count, feat_desc = feature_to_ask

    prompt = (
        f"Refer to the accompanying floor plan for {name}'s new house.\n"
        f"The plan features {num_bed} bedrooms, {num_bath} bathroom(s), an open-plan kitchen, and a lounge.\n"
        f"How many {feat_name} are indicated on this floor plan?"
    )

    correct_ans = f"{feat_count} {feat_name}"
    custom_opts = [
        f"{feat_count} {feat_name}",
        f"{feat_count + 1} {feat_name}",
        f"{max(1, feat_count - 1)} {feat_name}",
        f"{feat_count + 2} {feat_name}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify the standard architectural symbol [1 mark].\n"
        f"Locate all {feat_desc} shown on the floor plan.\n"
        f"Step 2: Count the occurrences systematically [1 mark].\n"
        f"Systematic count yields exactly {feat_count} {feat_name}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="1",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Identify the architectural symbols on the floor plan and count them carefully.",
        tier_2=f"Scan the plan for {feat_desc}.",
        tier_3=f"There are exactly {feat_count} {feat_name}.",
        r=r,
        diagram_spec=diagram_spec,
    )


def generate_subskill_2(r: random.Random) -> Dict[str, Any]:
    """Subskill 2: Calculate actual room dimensions from 1:100 scale floor plan."""
    name = r.choice(SA_NAMES)
    room = r.choice(["Master Bedroom", "Lounge", "Kitchen", "Dining Room", "Guest Bedroom"])

    # Plan measurements in cm
    plan_l_cm = r.choice([4.0, 4.5, 5.0, 5.2, 5.5, 6.0, 6.5])
    plan_w_cm = r.choice([3.0, 3.2, 3.5, 3.8, 4.0, 4.2])

    real_l_m = round(plan_l_cm * 100 / 100, 2)  # cm * 100 = cm, / 100 = m
    real_w_m = round(plan_w_cm * 100 / 100, 2)

    prompt = (
        f"Refer to the 1:100 scale house floor plan shown in the diagram. The {room} measures "
        f"{_fmt(plan_l_cm)} cm in length and {_fmt(plan_w_cm)} cm in width.\n"
        f"Calculate the actual real-world length and width of the room in metres (m)."
    )

    correct_ans = f"{_fmt(real_l_m)} m by {_fmt(real_w_m)} m"
    wrong_1 = f"{_fmt(real_l_m * 10)} m by {_fmt(real_w_m * 10)} m"
    wrong_2 = f"{_fmt(real_l_m * 0.1)} m by {_fmt(real_w_m * 0.1)} m"
    wrong_3 = f"{_fmt(real_l_m + 1)} m by {_fmt(real_w_m + 1)} m"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand the scale ratio [1 mark].\n"
        f"Scale 1:100 means 1 cm on the plan represents 100 cm (which is 1 metre) in reality.\n"
        f"Step 2: Multiply plan measurements by 100 cm and convert to metres [1 mark].\n"
        f"Length = {_fmt(plan_l_cm)} cm × 100 = {_fmt(plan_l_cm * 100)} cm = {_fmt(real_l_m)} m.\n"
        f"Width = {_fmt(plan_w_cm)} cm × 100 = {_fmt(plan_w_cm * 100)} cm = {_fmt(real_w_m)} m.\n"
        f"Step 3: Stated dimensions [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"House Floor Plan (Scale 1:100) - {room}",
        "length_m": real_l_m,
        "width_m": real_w_m,
        "rooms": [{"name": room, "length_m": real_l_m, "width_m": real_w_m}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="2",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Scale 1:100 means 1 cm on paper equals 100 cm (1 m) in real life.",
        tier_2=f"Multiply {_fmt(plan_l_cm)} cm by 100 to get real length in cm, then divide by 100 to get metres.",
        tier_3=f"Real length is {_fmt(real_l_m)} m and real width is {_fmt(real_w_m)} m.",
        r=r,
    )


def generate_subskill_3(r: random.Random) -> Dict[str, Any]:
    """Subskill 3: Calculate actual room dimensions from 1:50 scale floor plan."""
    name = r.choice(SA_NAMES)
    room = r.choice(["En-suite Bathroom", "Study Room", "Scullery", "Walk-in Closet", "Balcony"])

    # Plan measurements in mm or cm on 1:50 scale
    # On 1:50, 1 cm = 50 cm = 0.5 m, or 1 mm = 50 mm = 0.05 m
    plan_l_mm = r.choice([48, 56, 64, 70, 80, 90, 100])
    plan_w_mm = r.choice([36, 40, 44, 50, 60])

    real_l_m = round(plan_l_mm * 50 / 1000, 2)
    real_w_m = round(plan_w_mm * 50 / 1000, 2)

    prompt = (
        f"A detailed architectural drawing of a {room} uses a scale of 1:50. "
        f"On the drawing, the length is {_fmt(plan_l_mm)} mm and the width is {_fmt(plan_w_mm)} mm.\n"
        f"Calculate the actual real-world length and width of the {room} in metres."
    )

    correct_ans = f"{_fmt(real_l_m)} m by {_fmt(real_w_m)} m"
    wrong_1 = f"{_fmt(real_l_m * 2)} m by {_fmt(real_w_m * 2)} m"
    wrong_2 = f"{_fmt(real_l_m * 0.5)} m by {_fmt(real_w_m * 0.5)} m"
    wrong_3 = f"{_fmt(real_l_m * 10)} m by {_fmt(real_w_m * 10)} m"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand scale 1:50 [1 mark].\n"
        f"1 mm on the plan represents 50 mm in reality (50 mm = 0,05 m).\n"
        f"Step 2: Multiply by 50 and convert mm to metres [1 mark].\n"
        f"Length = {_fmt(plan_l_mm)} mm × 50 = {_fmt(plan_l_mm * 50)} mm ÷ 1 000 = {_fmt(real_l_m)} m.\n"
        f"Width = {_fmt(plan_w_mm)} mm × 50 = {_fmt(plan_w_mm * 50)} mm ÷ 1 000 = {_fmt(real_w_m)} m.\n"
        f"Step 3: Stated dimensions [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Architectural Drawing (Scale 1:50) - {room}",
        "length_m": real_l_m,
        "width_m": real_w_m,
        "rooms": [{"name": room, "length_m": real_l_m, "width_m": real_w_m}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="3",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Scale 1:50 means 1 unit on paper equals 50 units in real life.",
        tier_2=f"Multiply plan dimensions by 50 to get mm, then divide by 1 000 to convert to metres.",
        tier_3=f"Actual dimensions: {_fmt(real_l_m)} m by {_fmt(real_w_m)} m.",
        r=r,
    )


def generate_subskill_4(r: random.Random) -> Dict[str, Any]:
    """Subskill 4: Calculate actual floor area of a rectangular room in m² from scale plan."""
    name = r.choice(SA_NAMES)
    room = r.choice(["Conference Room", "Classroom", "Kitchen", "Living Room", "Workshop"])

    real_l = r.choice([5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0])
    real_w = r.choice([3.5, 4.0, 4.5, 5.0, 5.5])
    area = round(real_l * real_w, 2)

    prompt = (
        f"{name} is measuring a rectangular {room} on a floor plan. The real-world length of the room is "
        f"{_fmt(real_l)} m and the width is {_fmt(real_w)} m.\n"
        f"Calculate the total floor area of the {room} in square metres (m²)."
    )

    correct_ans = f"{_fmt(area)} m²"
    wrong_1 = f"{_fmt(2 * (real_l + real_w))} m²"  # perimeter mistake
    wrong_2 = f"{_fmt(area * 1.5)} m²"
    wrong_3 = f"{_fmt(area * 0.8)} m²"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify area formula [1 mark].\n"
        f"\\text{{Area}} = \\text{{Length}} \\times \\text{{Width}}.\n"
        f"Step 2: Substitute values [1 mark].\n"
        f"\\text{{Area}} = {_fmt(real_l)} \\text{{ m}} \\times {_fmt(real_w)} \\text{{ m}} = {_fmt(area)} \\text{{ m}}^2.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="4",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Area of a rectangle = Length × Width.",
        tier_2=f"Multiply {_fmt(real_l)} m by {_fmt(real_w)} m.",
        tier_3=f"The floor area is {_fmt(area)} m².",
        r=r,
    )


def generate_subskill_5(r: random.Random) -> Dict[str, Any]:
    """Subskill 5: Calculate perimeter of a room for skirting board installation, subtracting door opening."""
    name = r.choice(SA_NAMES)
    room = r.choice(["Bedroom", "Study", "Dining Room", "Office"])

    real_l = r.choice([4.2, 4.5, 4.8, 5.0, 5.4, 6.0])
    real_w = r.choice([3.2, 3.5, 3.6, 4.0, 4.2])
    door_width = r.choice([0.8, 0.85, 0.9, 1.0])

    full_perim = round(2 * (real_l + real_w), 2)
    skirting_needed = round(full_perim - door_width, 2)

    prompt = (
        f"{name} is installing timber skirting boards around the base of the walls in a rectangular {room} "
        f"measuring {_fmt(real_l)} m by {_fmt(real_w)} m. "
        f"There is one entrance door that is {_fmt(door_width)} m wide where no skirting board is needed.\n"
        f"Calculate the total length of skirting board (in metres) required for the room."
    )

    correct_ans = f"{_fmt(skirting_needed)} m"
    wrong_1 = f"{_fmt(full_perim)} m"  # forgot to subtract door
    wrong_2 = f"{_fmt(full_perim + door_width)} m"
    wrong_3 = f"{_fmt(skirting_needed - 1.0)} m"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate total perimeter of the room [1 mark].\n"
        f"Perimeter = 2 × (Length + Width) = 2 × ({_fmt(real_l)} + {_fmt(real_w)}) = 2 × {_fmt(real_l + real_w)} = {_fmt(full_perim)} m.\n"
        f"Step 2: Subtract the door opening [1 mark].\n"
        f"Skirting required = Total Perimeter - Door Width = {_fmt(full_perim)} m - {_fmt(door_width)} m = {_fmt(skirting_needed)} m.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="5",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the full room perimeter 2(L + W), then subtract the width of the doorway.",
        tier_2=f"Perimeter is 2 × ({_fmt(real_l)} + {_fmt(real_w)}) = {_fmt(full_perim)} m. Subtract {_fmt(door_width)} m for the door.",
        tier_3=f"Skirting board length = {_fmt(skirting_needed)} m.",
        r=r,
    )


def generate_subskill_6(r: random.Random) -> Dict[str, Any]:
    """Subskill 6: Calculate floor tiles needed including 10% cutting wastage."""
    name = r.choice(SA_NAMES)
    room = r.choice(["Kitchen", "Bathroom", "Veranda", "Foyer"])

    room_l = r.choice([3.0, 3.5, 4.0, 4.5, 5.0])
    room_w = r.choice([2.5, 3.0, 3.5, 4.0])
    floor_area = round(room_l * room_w, 2)

    # Tile size in cm
    tile_size_cm = r.choice([40, 50, 60])
    tile_area_m2 = round((tile_size_cm / 100) ** 2, 4)

    raw_tiles = floor_area / tile_area_m2
    # Add 10% for cutting and breakage, rounded up to next whole tile
    tiles_with_waste = math.ceil(raw_tiles * 1.10)

    prompt = (
        f"{name} plans to tile the floor of a rectangular {room} measuring {_fmt(room_l)} m by {_fmt(room_w)} m. "
        f"The ceramic tiles chosen are square, measuring {_fmt(tile_size_cm)} cm by {_fmt(tile_size_cm)} cm.\n"
        f"Tiling guidelines recommend purchasing an additional 10% of tiles to allow for cutting and breakage. "
        f"Calculate the minimum number of whole tiles {name} must buy."
    )

    correct_ans = f"{_fmt(tiles_with_waste)} tiles"
    wrong_1 = f"{math.ceil(raw_tiles)} tiles"  # forgot 10% waste
    wrong_2 = f"{math.ceil(raw_tiles * 1.25)} tiles"
    wrong_3 = f"{math.floor(raw_tiles * 0.9)} tiles"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate floor area and single tile area in m² [1 mark].\n"
        f"Floor Area = {_fmt(room_l)} m × {_fmt(room_w)} m = {_fmt(floor_area)} m².\n"
        f"Tile Area = ({_fmt(tile_size_cm / 100)} m)² = {_fmt(tile_area_m2)} m².\n"
        f"Step 2: Calculate basic tile count [1 mark].\n"
        f"Basic tiles = {_fmt(floor_area)} ÷ {_fmt(tile_area_m2)} = {_fmt(raw_tiles, 1)} tiles.\n"
        f"Step 3: Add 10% wastage and round up to whole tile [1 mark].\n"
        f"Total with 10% = {_fmt(raw_tiles, 1)} × 1,10 = {_fmt(raw_tiles * 1.10, 2)} → rounded up = {_fmt(tiles_with_waste)} tiles ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="6",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate room area and tile area in the same units (m²), divide them, then add 10% and round up.",
        tier_2=f"Room area = {_fmt(floor_area)} m². Single tile area = {_fmt(tile_area_m2)} m². Base tiles = {_fmt(raw_tiles, 1)}.",
        tier_3=f"Multiply by 1,10 to add 10% wastage: {_fmt(raw_tiles * 1.10, 1)} → {tiles_with_waste} tiles.",
        r=r,
    )


def generate_subskill_7(r: random.Random) -> Dict[str, Any]:
    """Subskill 7: Door swing arc interpretation and furniture clearance."""
    name = r.choice(SA_NAMES)
    room = r.choice(["Bedroom 1", "Guest Room", "Study Room", "Bathroom"])

    swing_direction = r.choice(["inward into the room", "outward into the hallway"])
    hinge_side = r.choice(["left side", "right side"])
    door_width_cm = r.choice([80, 85, 90])

    prompt = (
        f"On an architectural floor plan, the entrance door to {room} is indicated by a straight line "
        f"representing the open door leaf and a curved quarter-circle arc. "
        f"The door leaf is attached to the {hinge_side} of the door frame and the arc curves {swing_direction}. "
        f"The door width is {_fmt(door_width_cm)} cm.\n"
        f"What is the practical meaning of this door swing representation for room layout planning?"
    )

    correct_ans = (
        f"The door swings {swing_direction}, requiring an unobstructed circular clearance radius of at least {_fmt(door_width_cm)} cm"
    )
    wrong_1 = f"The door slides horizontally into a wall cavity of {_fmt(door_width_cm)} cm"
    wrong_2 = f"The door swings {'outward into the hallway' if 'inward' in swing_direction else 'inward into the room'} and requires zero clearance"
    wrong_3 = f"The door is a revolving door with radius {_fmt(door_width_cm * 2)} cm"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand door swing conventions on floor plans [1 mark].\n"
        f"The straight line represents the door leaf and the curved arc shows the pathway swept out when opening.\n"
        f"Step 2: Relate to spatial clearances [1 mark].\n"
        f"Because the door opens {swing_direction}, no furniture or fixtures can be placed within the {_fmt(door_width_cm)} cm swing arc.\n"
        f"Step 3: Stated deduction [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="7",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The quarter-circle arc shows the space swept out by the door when it opens.",
        tier_2=f"The door swings {swing_direction}, so that {_fmt(door_width_cm)} cm radius must be kept completely clear of furniture.",
        tier_3=f"Correct conclusion: {correct_ans}.",
        r=r,
    )


def generate_subskill_8(r: random.Random) -> Dict[str, Any]:
    """Subskill 8: Calculate total internal floor area of entire multi-room structure."""
    name = r.choice(SA_NAMES)

    bed1_area = r.choice([16.0, 18.0, 20.0])
    bed2_area = r.choice([12.0, 14.0, 15.0])
    bath_area = r.choice([6.0, 7.5, 8.0])
    living_kitchen_area = r.choice([28.0, 32.0, 35.0, 40.0])
    passage_area = r.choice([4.5, 5.0, 6.0])

    total_internal = round(bed1_area + bed2_area + bath_area + living_kitchen_area + passage_area, 2)

    prompt = (
        f"{name}'s house plan comprises the following internal room areas:\n"
        f"• Master Bedroom: {_fmt(bed1_area)} m²\n"
        f"• Bedroom 2: {_fmt(bed2_area)} m²\n"
        f"• Bathroom: {_fmt(bath_area)} m²\n"
        f"• Open-plan Living & Kitchen: {_fmt(living_kitchen_area)} m²\n"
        f"• Hallway / Passage: {_fmt(passage_area)} m²\n"
        f"Calculate the total internal usable floor area of the house in square metres."
    )

    correct_ans = f"{_fmt(total_internal)} m²"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Sum all individual room areas [1 mark].\n"
        f"Total Area = {_fmt(bed1_area)} + {_fmt(bed2_area)} + {_fmt(bath_area)} + {_fmt(living_kitchen_area)} + {_fmt(passage_area)} [1 mark].\n"
        f"Step 2: Perform addition [1 mark].\n"
        f"Total Area = {_fmt(total_internal)} m².\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="8",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add up the internal floor areas of all rooms and corridors.",
        tier_2=f"Sum: {_fmt(bed1_area)} + {_fmt(bed2_area)} + {_fmt(bath_area)} + {_fmt(living_kitchen_area)} + {_fmt(passage_area)}.",
        tier_3=f"The total internal floor area is {_fmt(total_internal)} m².",
        r=r,
    )


def generate_subskill_9(r: random.Random) -> Dict[str, Any]:
    """Subskill 9: Spatial furniture fit & clearance along a designated wall."""
    name = r.choice(SA_NAMES)
    wall_length_m = r.choice([3.6, 4.0, 4.2, 4.5, 4.8])
    wardrobe_width_m = r.choice([1.2, 1.5, 1.8])
    bed_width_m = r.choice([1.5, 1.6, 1.8])  # queen or king bed
    min_clearance_m = 0.6  # 60 cm walkway on each side

    total_furniture = wardrobe_width_m + bed_width_m
    remaining_space = round(wall_length_m - total_furniture, 2)
    fits = remaining_space >= 0.6

    prompt = (
        f"{name} wants to arrange furniture along a bedroom wall that is {_fmt(wall_length_m)} m long. "
        f"{name} wants to place a wardrobe of width {_fmt(wardrobe_width_m)} m and a bed of width "
        f"{_fmt(bed_width_m)} m side-by-side along this wall. "
        f"Building guidelines require at least 0,60 m (60 cm) of remaining clearance space for walking.\n"
        f"Will both items fit along this wall while meeting the required clearance, and what is the remaining space?"
    )

    if fits:
        correct_ans = f"Yes, they fit with {_fmt(remaining_space)} m of clearance remaining"
        wrong_1 = f"No, they exceed the wall length by {_fmt(abs(remaining_space))} m"
        wrong_2 = f"Yes, they fit with {_fmt(remaining_space + 0.5)} m of clearance remaining"
        wrong_3 = f"No, they leave only {_fmt(remaining_space * 0.5)} m of clearance"
    else:
        correct_ans = f"No, remaining space is only {_fmt(remaining_space)} m (less than 0,60 m required)"
        wrong_1 = f"Yes, they fit with {_fmt(remaining_space)} m of clearance remaining"
        wrong_2 = f"No, they exceed the wall length by {_fmt(abs(wall_length_m - total_furniture + 1.0))} m"
        wrong_3 = f"Yes, because total furniture width is exactly {_fmt(total_furniture)} m"

    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate combined furniture width [1 mark].\n"
        f"Combined width = Wardrobe + Bed = {_fmt(wardrobe_width_m)} m + {_fmt(bed_width_m)} m = {_fmt(total_furniture)} m.\n"
        f"Step 2: Calculate remaining wall space [1 mark].\n"
        f"Remaining space = Wall Length - Combined Width = {_fmt(wall_length_m)} m - {_fmt(total_furniture)} m = {_fmt(remaining_space)} m.\n"
        f"Step 3: Compare with required clearance [1 mark].\n"
        f"Required clearance = 0,60 m. Since {_fmt(remaining_space)} m is {'≥ 0,60 m' if fits else '< 0,60 m'}, the conclusion is: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="9",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the widths of both pieces of furniture and subtract from the wall length.",
        tier_2=f"Total furniture = {_fmt(wardrobe_width_m)} + {_fmt(bed_width_m)} = {_fmt(total_furniture)} m. Wall length = {_fmt(wall_length_m)} m.",
        tier_3=f"Remaining space is {_fmt(remaining_space)} m. Compare this to the 0,60 m required clearance.",
        r=r,
    )
