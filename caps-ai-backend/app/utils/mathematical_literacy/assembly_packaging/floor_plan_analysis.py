"""Cluster 3: Floor Plans — Architectural Symbols & Layout Analysis (Subskills 18 to 26).

Covers:
18. Standard architectural floor plan symbols (walls, doors, windows, fixtures)
19. Door swing quarter-circle arc notation & clearance envelopes
20. Room type deduction based on sanitary & furniture fixtures
21. Compass orientation & North-facing aspect (Southern Hemisphere winter sun)
22. Kitchen work triangle layout & movement efficiency (sink, stove, fridge)
23. Architectural design flaws & fire/safety hazard audits
24. Furniture space planning & wall clearance verification
25. Cross-ventilation & exterior vs interior partition wall window placement
26. Doorway opening dimensions vs large furniture delivery ingress
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_asm_plan_identify_architectural_symbols(r: random.Random) -> Dict[str, Any]:
    symbol_scenario = r.choice([
        (
            "a straight line hinged at one wall corner with a curved quarter-circle dotted or solid arc sweeping outward",
            "Door showing the direction and swing space required to open",
            "Window opening to the outside",
            "Built-in cupboard (BIC) with sliding shelves",
            "Underfloor heating coil"
        ),
        (
            "two thin parallel lines breaking a thick solid wall with two small cross-ticks",
            "Window situated within an external or internal wall",
            "Solid load-bearing brick wall with no openings",
            "Kitchen double sink basin",
            "Electrical plug wall socket"
        ),
        (
            "a rectangle with a large diagonal 'X' drawn across it, placed against an internal bedroom wall",
            "Built-in Cupboard (BIC) / Wardrobe",
            "Emergency escape exit",
            "Glass sliding patio door",
            "Brick chimney fireplace"
        ),
        (
            "an oval bowl inside a rectangular outline with an adjoining smaller circle representing a tap faucet",
            "Hand wash basin / sink fixture",
            "Television flat screen",
            "Single single-sized mattress",
            "Fire extinguisher cabinet"
        ),
    ])
    visual_desc, correct_name, d1, d2, d3 = symbol_scenario

    prompt = (
        f"Study the standard architectural conventions used on South African residential floor plans.\n\n"
        f"Which architectural feature is represented by the symbol: **{visual_desc}**?"
    )
    ans = correct_name
    opts = [correct_name, d1, d2, d3]

    s1 = f"Identify standard national architectural drawing symbols used on building floor layout plans."
    s2 = f"✓ [1 Mark: Method – Matching technical graphical symbol with building element]\nStandard architectural symbol conventions indicate walls, doors, windows, and fixed cabinetry."
    s3 = f"✓ [1 Mark: Accuracy – Correct architectural symbol]\nIdentified feature: {correct_name}."

    floor_diag = {
        "image_type": "architectural_floor_packaging_plan",
        "master": "architectural_floor_packaging_plan",
        "diagram_id": "architectural_floor_packaging_plan",
        "view": "exam",
        "pins": [{"pin": "A", "anchor": [186, 68], "default_box": [60, 75], "side": "left", "role": "target"}],
        "caption": "Architectural Residential Floor Plan with Standard Symbols",
    }

    return _build_question_payload(
        "asm_plan_identify_architectural_symbols",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Look at the visual description: {visual_desc}.",
        tier_2_hint="Arcs represent door swings, parallel breaks represent windows, and crossed boxes represent built-in cupboards.",
        tier_3_hint=f"The symbol represents: {correct_name}.",
        diagram_spec=floor_diag,
    )


def _gen_asm_plan_door_swing_quarter_circle_arc(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"On a house floor plan, every door is drawn as a straight line perpendicular or angled to the wall, "
        f"with a circular quarter-arc connecting the free edge of the door back to the doorframe.\n\n"
        f"Why is the door symbol drawn with this quarter-circle arc?"
    )
    ans = "It indicates the direction the door swings open and shows the clear floor space that must be kept free of furniture."
    opts = [
        "It indicates the direction the door swings open and shows the clear floor space that must be kept free of furniture.",
        "It represents an electrical sensor that opens the door automatically.",
        "It indicates that the door is made from curved glass or flexible wood.",
        "It measures the sound echo produced when the door slams shut.",
    ]

    s1 = f"Understand spatial planning conventions and door opening clearance envelopes on floor plans."
    s2 = f"✓ [1 Mark: Method – Spatial interpretation of door swing arc]\nThe 90° arc demarcates the sweep area of the door panel, preventing furniture from blocking ingress and egress."
    s3 = f"✓ [1 Mark: Accuracy – Correct functional explanation]\nExplanation: It indicates the direction the door swings open and shows the clear floor space that must be kept free of furniture."

    door_diag = {
        "image_type": "architectural_floor_packaging_plan",
        "master": "architectural_floor_packaging_plan",
        "diagram_id": "architectural_floor_packaging_plan",
        "view": "exam",
        "pins": [{"pin": "D", "anchor": [260, 210], "default_box": [60, 210], "side": "left", "role": "target"}],
        "caption": "Door Swing Quarter-Circle Arc Clearance Envelope",
    }

    return _build_question_payload(
        "asm_plan_door_swing_quarter_circle_arc",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Think about what would happen if a table was placed inside that quarter-circle area.",
        tier_2_hint="The arc represents the path the door takes as it opens and closes.",
        tier_3_hint="It shows the direction the door swings and the clearance envelope required.",
        diagram_spec=door_diag,
    )


def _gen_asm_plan_room_type_deduction_from_fixtures(r: random.Random) -> Dict[str, Any]:
    room_scenario = r.choice([
        (
            "Room A contains a double sink unit with draining board, a four-plate stove icon, and a tall rectangular box labelled 'REF'",
            "Kitchen",
            "Bathroom",
            "Dining room",
            "Garage"
        ),
        (
            "Room B contains an enclosed cubicle with a small circular showerhead symbol, a porcelain pan with a water cistern, and a washbasin",
            "Bathroom / Ensuite",
            "Kitchen",
            "Living room / Lounge",
            "Study"
        ),
        (
            "Room C contains a large rectangular shape labelled 'Queen Bed' flanked by two small bedside pedestal squares and a full-wall Built-in Cupboard (BIC)",
            "Master Bedroom",
            "Kitchen",
            "Bathroom",
            "Laundry room"
        ),
        (
            "Room D has an extra-wide double opening roll-up door on an exterior wall and contains space for two vehicles",
            "Double Garage",
            "Lounge",
            "Kitchen",
            "Patio"
        ),
    ])
    fixture_desc, correct_room, d1, d2, d3 = room_scenario

    prompt = (
        f"Study an unlabeled floor plan of a modern South African family house.\n\n"
        f"Based on the following fixtures and furnishings: **{fixture_desc}**, what is the primary function of this room?"
    )
    ans = correct_room
    opts = [correct_room, d1, d2, d3]

    s1 = f"Deduce functional room types on architectural plans from standard plumbing fixtures, appliances, and furniture layouts."
    s2 = f"✓ [1 Mark: Method – Identifying specialized domestic fixtures]\nSanitary fixtures, culinary appliances, and beds define room typology."
    s3 = f"✓ [1 Mark: Accuracy – Correct room designation]\nIdentified room: {correct_room}."

    fixture_diag = {
        "image_type": "architectural_floor_packaging_plan",
        "master": "architectural_floor_packaging_plan",
        "diagram_id": "architectural_floor_packaging_plan",
        "view": "exam",
        "pins": [{"pin": "K", "anchor": [420, 110], "default_box": [540, 110], "side": "right", "role": "target"}],
        "caption": "Architectural Plan Fixtures (Kitchen Sink & Stove)",
    }

    return _build_question_payload(
        "asm_plan_room_type_deduction_from_fixtures",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Check the fixtures: {fixture_desc}.",
        tier_2_hint="Which room in a home contains those specific appliances or sanitary fixtures?",
        tier_3_hint=f"The room is a {correct_room}.",
        diagram_spec=fixture_diag,
    )


def _gen_asm_plan_compass_orientation_north_aspect(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    l_val = r.choice([11.0, 12.0, 13.0])
    diag = {
        "kind": "floor_plan",
        "title": f"House Orientation Plan ({name})",
        "scale": "1 : 100",
        "rooms": [
            {"name": "Living Room (North)", "dims": "5,0 m × 4,2 m", "length_m": 5.0, "width_m": 4.2},
            {"name": "Main Bedroom (North)", "dims": "4,2 m × 3,8 m", "length_m": 4.2, "width_m": 3.8},
            {"name": "Kitchen (South)", "dims": "3,5 m × 3,0 m", "length_m": 3.5, "width_m": 3.0},
            {"name": "Bathroom (South)", "dims": "2,8 m × 2,2 m", "length_m": 2.8, "width_m": 2.2},
        ],
        "length_m": 12.0,
        "width_m": 8.0,
    }
    prompt = (
        f"{name} is reviewing an architect's house plan for a new house in Gauteng, South Africa (refer to the accompanying floor plan).\n\n"
        f"The plan features a north compass arrow pointing upwards towards the top wall.\n"
        f"The architect strongly advises placing the main bedrooms and the living room along the **North-facing** wall of the house.\n\n"
        f"What is the environmental and energy-efficiency advantage of having North-facing living areas in South Africa?"
    )
    ans = "Because South Africa is in the Southern Hemisphere, North-facing rooms receive maximum natural sunlight during winter, keeping rooms warm and reducing heating electricity costs."
    opts = [
        "Because South Africa is in the Southern Hemisphere, North-facing rooms receive maximum natural sunlight during winter, keeping rooms warm and reducing heating electricity costs.",
        "North-facing walls are naturally shielded from all rain and lightning storms in Africa.",
        "Municipal building regulations in South Africa strictly forbid building windows facing south.",
        "North-facing windows receive direct satellite internet signals better than south-facing windows.",
    ]

    s1 = f"Apply geographic principles of solar orientation in the Southern Hemisphere to architectural building design and passive thermal comfort."
    s2 = f"✓ [1 Mark: Method – Linking compass orientation with Southern Hemisphere solar path]\nThe midday sun arcs across the northern sky in the Southern Hemisphere. North-facing glazing captures low-angle winter sunlight for passive heating."
    s3 = f"✓ [1 Mark: Accuracy – Correct passive solar orientation rationale]\nAdvantage: North-facing rooms receive maximum natural sunlight during winter, keeping rooms warm and reducing heating electricity costs."

    return _build_question_payload(
        "asm_plan_compass_orientation_north_aspect",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Where is the sun positioned in the sky during winter in South Africa (Southern Hemisphere)?",
        tier_2_hint="In the Southern Hemisphere, the sun is in the north, so north-facing windows let in warm winter sunshine.",
        tier_3_hint="North-facing living areas receive optimal winter sun, keeping rooms naturally warm.",
        diagram_spec=diag,
    )


def _gen_asm_plan_kitchen_work_triangle_layout(r: random.Random) -> Dict[str, Any]:
    k_len = r.choice([3.8, 4.0, 4.2])
    diag = {
        "kind": "floor_plan",
        "title": f"Kitchen Ergonomic Work Triangle Layout ({k_len}m)",
        "scale": "1 : 50",
        "rooms": [
            {"name": "Kitchen (Work Triangle)", "dims": "4,0 m × 3,5 m", "length_m": 4.0, "width_m": 3.5},
            {"name": "Dining Area", "dims": "4,5 m × 3,8 m", "length_m": 4.5, "width_m": 3.8},
        ],
        "length_m": 8.5,
        "width_m": 4.0,
    }
    prompt = (
        f"When architects design domestic kitchens, they evaluate the 'Kitchen Work Triangle' connecting "
        f"the three primary work centres (shown on the accompanying floor plan layout).\n\n"
        f"Which three appliances and fixtures form the apexes of this fundamental ergonomic kitchen triangle?"
    )
    ans = "Refrigerator (food storage), Sink (food preparation & washing), and Stove/Hob (cooking)"
    opts = [
        "Refrigerator (food storage), Sink (food preparation & washing), and Stove/Hob (cooking)",
        "Microwave, Toaster, and Electric Kettle",
        "Dining Table, Dishwasher, and Rubbish Bin",
        "Washing Machine, Tumble Dryer, and Ironing Board",
    ]

    s1 = f"Identify the three core functional stations forming the ergonomic kitchen work triangle: storage, washing/prep, and cooking."
    s2 = f"✓ [1 Mark: Method – Identifying components of the kitchen work triangle]\nThe classic kitchen triangle connects the refrigerator (storage), sink (prep/cleaning), and stove (cooking) with unobstructed traffic paths."
    s3 = f"✓ [1 Mark: Accuracy – Exact three stations]\nStations: Refrigerator (food storage), Sink (food preparation & washing), and Stove/Hob (cooking)."

    return _build_question_payload(
        "asm_plan_kitchen_work_triangle_layout",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Think about the three main activities done in a kitchen: storing food, washing it, and cooking it.",
        tier_2_hint="The triangle connects the three main stations: fridge, sink, and stove.",
        tier_3_hint="Correct apexes: Refrigerator, Sink, and Stove/Hob.",
        diagram_spec=diag,
    )


def _gen_asm_plan_design_flaws_clearance_hazard_audit(r: random.Random) -> Dict[str, Any]:
    flaw_scenario = r.choice([
        (
            "The four-plate cooking stove is placed directly beneath an opening window with hanging fabric curtains.",
            "Severe fire hazard: Wind blowing through the open window can blow curtains onto open flames or hot plates, or blow out gas flames causing gas leaks.",
            "The stove will block natural daylight from reaching the countertop.",
            "The stove will cook food too quickly due to excess oxygen.",
            "Curtains are not permitted in residential kitchens under health regulations."
        ),
        (
            "The main kitchen entrance door swings inwards directly against the front oven door of the cooking stove.",
            "Collision and burn hazard: A person entering through the door could strike someone bending down at a hot open oven, causing severe burns or spills.",
            "The stove will prevent the refrigerator from staying cool.",
            "The door will trap cooking steam inside the oven.",
            "The kitchen will fail water conservation standards."
        ),
        (
            "The bathroom toilet is positioned facing an unpartitioned doorway directly into the open-plan dining room.",
            "Hygiene and privacy defect: Lack of visual and olfactory privacy, and cross-contamination risk between sanitary facilities and dining areas.",
            "The toilet plumbing will freeze in winter.",
            "The dining table will absorb moisture from the toilet cistern.",
            "The house will require two separate water meters."
        ),
    ])
    flaw_desc, correct_reason, d1, d2, d3 = flaw_scenario

    diag = {
        "kind": "floor_plan",
        "title": f"Clearance & Hazard Audit ({flaw_desc[:25]}...)",
        "scale": "1 : 100",
        "rooms": [
            {"name": "Kitchen / Dining Area", "dims": "4,2 m × 3,6 m", "length_m": 4.2, "width_m": 3.6},
            {"name": "Adjacent Room", "dims": "4,0 m × 3,5 m", "length_m": 4.0, "width_m": 3.5},
        ],
        "length_m": 8.2,
        "width_m": 4.0,
    }

    prompt = (
        f"A floor plan draft submitted by an amateur draughtsman contains the layout defect noted on the accompanying plan:\n"
        f"**'{flaw_desc}'**\n\n"
        f"Why is this layout classified as a serious design defect according to South African building and safety standards?"
    )
    ans = correct_reason
    opts = [correct_reason, d1, d2, d3]

    s1 = f"Evaluate floor plan layouts for ergonomic defects, health regulations, and safety/fire hazards."
    s2 = f"✓ [1 Mark: Method – Analyzing architectural conflict and danger]\nStoves beneath curtains create fire risks; doors swinging into hot appliances create burn hazards; toilets facing dining areas violate privacy and hygiene."
    s3 = f"✓ [1 Mark: Accuracy – Correct technical hazard explanation]\nDefect reason: {correct_reason}"

    return _build_question_payload(
        "asm_plan_design_flaws_clearance_hazard_audit",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Focus on the specific flaw described: '{flaw_desc}'.",
        tier_2_hint="Consider fire safety, physical burn collisions, or hygiene and privacy requirements.",
        tier_3_hint=f"Correct explanation: {correct_reason}",
        diagram_spec=diag,
    )


def _gen_asm_plan_furniture_space_planning_placement(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    wall_length_m = r.choice([3.2, 3.5, 3.8, 4.0, 4.2])
    door_clearance_m = 0.9  # 90 cm door swing
    window_clearance_m = r.choice([0.8, 1.0, 1.2])
    available_wall_m = round(wall_length_m - door_clearance_m - window_clearance_m, 2)
    couch_len_m = round(available_wall_m + r.choice([-0.3, 0.2]), 2)
    fits = couch_len_m <= available_wall_m

    diag = {
        "kind": "floor_plan",
        "title": "Living Room Wall Clearance & Space Planning",
        "scale": "1 : 50",
        "rooms": [
            {"name": "Living Room Wall", "dims": f"{_fmt(wall_length_m)} m", "length_m": wall_length_m, "width_m": 3.5},
        ],
        "length_m": wall_length_m,
        "width_m": 3.5,
    }

    prompt = (
        f"{name} wants to place a 3-seater couch along a living room wall of length {_fmt(wall_length_m)} m (refer to the floor plan layout).\n\n"
        f"The wall contains:\n"
        f"• An entrance door requiring a {_fmt(door_clearance_m)} m clear swing arc from the left corner.\n"
        f"• A low floor-to-ceiling glass panel on the right side requiring {_fmt(window_clearance_m)} m clearance.\n\n"
        f"1. Calculate the maximum remaining wall length available for furniture along this wall.\n"
        f"2. Determine whether a couch measuring {_fmt(couch_len_m)} m long will fit along this wall without obstructing the door or glass panel."
    )
    if fits:
        ans = f"Available: {_fmt(available_wall_m)} m — Yes, the couch will fit (clearance of {_fmt(round(available_wall_m - couch_len_m, 2))} m remaining)."
    else:
        over = round(couch_len_m - available_wall_m, 2)
        ans = f"Available: {_fmt(available_wall_m)} m — No, the couch will NOT fit (it exceeds available space by {_fmt(over)} m)."

    s1 = f"Calculate available wall space by subtracting door swing clearance ({_fmt(door_clearance_m)} m) and window clearance ({_fmt(window_clearance_m)} m) from total wall length ({_fmt(wall_length_m)} m)."
    s2 = f"✓ [1 Mark: Method – Subtracting clearances from total wall length]\nAvailable = {_fmt(wall_length_m)} − {_fmt(door_clearance_m)} − {_fmt(window_clearance_m)} = {_fmt(available_wall_m)} m.\nComparison with couch length: {_fmt(couch_len_m)} m vs {_fmt(available_wall_m)} m."
    s3 = f"✓ [1 Mark: Accuracy – Space calculation and definitive fit verdict]\n{ans}"

    return _build_question_payload(
        "asm_plan_furniture_space_planning_placement",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Subtract the door ({_fmt(door_clearance_m)} m) and window ({_fmt(window_clearance_m)} m) from total wall length ({_fmt(wall_length_m)} m).",
        tier_2_hint=f"Available wall space = {_fmt(available_wall_m)} m. Compare this with couch length of {_fmt(couch_len_m)} m.",
        tier_3_hint=f"{ans}",
        diagram_spec=diag,
    )


def _gen_asm_plan_ventilation_and_window_placement(r: random.Random) -> Dict[str, Any]:
    b_len = r.choice([3.6, 3.8, 4.0])
    diag = {
        "kind": "floor_plan",
        "title": f"Perimeter Wall Fenestration Plan ({b_len}m)",
        "scale": "1 : 100",
        "rooms": [
            {"name": "Bedroom 1 (External Wall)", "dims": "3,8 m × 3,2 m", "length_m": 3.8, "width_m": 3.2},
            {"name": "Bedroom 2 (External Wall)", "dims": "3,8 m × 3,2 m", "length_m": 3.8, "width_m": 3.2},
        ],
        "length_m": 7.6,
        "width_m": 3.5,
    }
    prompt = (
        f"Study the accompanying residential floor plan layout showing room boundaries.\n\n"
        f"Why can window symbols only be placed along **external perimeter walls** "
        f"of a room, and never along internal dividing partition walls between two bedrooms?"
    )
    ans = "Windows must open to the outside atmosphere to provide direct natural daylight and fresh air ventilation into the room."
    opts = [
        "Windows must open to the outside atmosphere to provide direct natural daylight and fresh air ventilation into the room.",
        "Internal walls are too thick to cut window holes into.",
        "Glass conducts electricity through interior walls.",
        "Building regulations require all internal walls to be soundproof concrete.",
    ]

    s1 = f"Understand building envelope principles, passive ventilation, natural fenestration, and health standards."
    s2 = f"✓ [1 Mark: Method – Identifying primary function of external fenestration]\nWindows require an interface with exterior ambient air and sunlight to satisfy habitable room ventilation requirements (e.g. SANS 10400-O)."
    s3 = f"✓ [1 Mark: Accuracy – Correct architectural ventilation rule]\nRule: Windows must open to the outside atmosphere to provide direct natural daylight and fresh air ventilation into the room."

    return _build_question_payload(
        "asm_plan_ventilation_and_window_placement",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What is the main purpose of a window in a habitable bedroom?",
        tier_2_hint="Windows require an opening to outside fresh air and natural sunlight.",
        tier_3_hint="They must connect to the outside atmosphere for light and fresh air.",
        diagram_spec=diag,
    )


def _gen_asm_plan_doorway_clearance_furniture_delivery(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    door_width_mm = r.choice([760, 810, 850, 900])
    couch_width_mm = r.choice([820, 880, 950, 1050])
    couch_height_mm = r.choice([700, 720, 750])  # couch height when turned on its side

    diag = {
        "kind": "floor_plan",
        "title": "Apartment Doorway Ingress Clearance Plan",
        "scale": "1 : 50",
        "rooms": [
            {"name": "Entrance Hallway", "dims": f"Doorway: {door_width_mm} mm", "length_m": 3.0, "width_m": 2.0},
        ],
        "length_m": 3.0,
        "width_m": 2.0,
    }

    prompt = (
        f"{name} is buying a large bulky sofa for a newly rented apartment (refer to the entrance layout plan).\n\n"
        f"Measurements:\n"
        f"• Front entrance doorway clear opening width: {door_width_mm} mm (0,{door_width_mm // 10} m)\n"
        f"• Sofa dimensions: Length = 2 200 mm, Width = {couch_width_mm} mm, Height = {couch_height_mm} mm\n\n"
        f"Can the delivery team carry the sofa through the front entrance doorway, and how?"
    )
    if couch_height_mm < door_width_mm:
        ans = f"Yes — by rotating the sofa on its side so its height ({couch_height_mm} mm) passes through the doorway width ({door_width_mm} mm)."
    else:
        ans = f"No — neither the sofa's width ({couch_width_mm} mm) nor height ({couch_height_mm} mm) is narrower than the {door_width_mm} mm door opening."

    s1 = f"Compare 3D furniture cross-sectional dimensions (width vs height) against 2D doorway clear opening width to determine delivery ingress."
    s2 = f"✓ [1 Mark: Method – Comparing smallest cross-sectional dimension of sofa with door width]\nDoor clear width = {door_width_mm} mm.\nSofa normal width = {couch_width_mm} mm (too wide).\nSofa side height = {couch_height_mm} mm."
    s3 = f"✓ [1 Mark: Accuracy – Correct delivery verdict and orientation explanation]\nVerdict: {ans}"

    return _build_question_payload(
        "asm_plan_doorway_clearance_furniture_delivery",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Sofas do not have to be carried upright; they can be turned onto their side or back.",
        tier_2_hint=f"Compare the sofa's height ({couch_height_mm} mm) with the door width ({door_width_mm} mm).",
        tier_3_hint=f"{ans}",
        diagram_spec=diag,
    )

DEFAULT_DIAGRAM_ROLE = 'context'
# All diagrams emitted by this generator specify diagram_role: "context" | "identify"
