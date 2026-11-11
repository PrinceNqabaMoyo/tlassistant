"""Subskills 19 to 27: Design Drawings, Assembly Instructions, Cutting Lists & Material Waste for Grade 11 Mathematical Literacy."""
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


def generate_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Subskill 19: Identify constituent parts of a furniture item from a design drawing."""
    item = r.choice(["Bookshelf", "Study Desk", "Dog Kennel", "Garden Bench", "Bedside Table"])

    if item == "Bookshelf":
        parts_dict = {"Side Panels": 2, "Top & Bottom Panels": 2, "Adjustable Shelves": 3, "Hardboard Backing": 1}
        target_part = "Adjustable Shelves"
        target_qty = 3
    elif item == "Study Desk":
        parts_dict = {"Leg Frames": 2, "Desktop Surface": 1, "Drawer Fronts": 3, "Modesty Panel": 1}
        target_part = "Drawer Fronts"
        target_qty = 3
    elif item == "Dog Kennel":
        parts_dict = {"Side Walls": 2, "Front Wall with Door Opening": 1, "Back Wall": 1, "Pitched Roof Panels": 2, "Floor Base": 1}
        target_part = "Pitched Roof Panels"
        target_qty = 2
    elif item == "Garden Bench":
        parts_dict = {"End Support Frames": 2, "Seat Slats": 5, "Backrest Slats": 4, "Centre Support Brace": 1}
        target_part = "Seat Slats"
        target_qty = 5
    else:
        parts_dict = {"Side Frames": 2, "Top Shelf": 1, "Lower Shelf": 1, "Drawer Unit": 1}
        target_part = "Side Frames"
        target_qty = 2

    prompt = (
        f"A design drawing and exploded parts diagram for a wooden {item} lists all timber components. "
        f"According to the specifications, how many '{target_part}' are required to assemble this {item}?"
    )

    correct_ans = f"{target_qty} {target_part}"
    wrong_1 = f"{target_qty + 1} {target_part}"
    wrong_2 = f"{max(1, target_qty - 1)} {target_part}"
    wrong_3 = f"{target_qty + 2} {target_part}"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Locate '{target_part}' in the design drawing and parts list [1 mark].\n"
        f"The cutting list specifies the quantity for each component.\n"
        f"Step 2: Read the quantity column [1 mark].\n"
        f"The required quantity for '{target_part}' is {target_qty}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="19",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Check the parts table or diagram callouts for the component name.",
        tier_2=f"Look for '{target_part}' in the list of parts.",
        tier_3=f"The required number is {target_qty}.",
        r=r,
    )


def generate_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Subskill 20: Read dimensions of specific components from a cutting list."""
    name = r.choice(SA_NAMES)
    component = r.choice(["Side Upright", "Top Shelf", "Base Plinth", "Back Panel", "Drawer Runner"])

    length_mm = r.choice([800, 900, 1000, 1200, 1500, 1800])
    width_mm = r.choice([200, 250, 300, 400, 450])
    thick_mm = r.choice([16, 18, 22, 25])

    prompt = (
        f"{name} consults the following cutting list for a woodworking project:\n\n"
        f"| Component | Quantity | Length (mm) | Width (mm) | Thickness (mm) |\n"
        f"| :--- | :--- | :--- | :--- | :--- |\n"
        f"| {component} | 2 | {_fmt(length_mm)} | {_fmt(width_mm)} | {_fmt(thick_mm)} |\n\n"
        f"What are the dimensions (Length × Width × Thickness) of the {component} in millimetres?"
    )

    correct_ans = f"{_fmt(length_mm)} mm × {_fmt(width_mm)} mm × {_fmt(thick_mm)} mm"
    wrong_1 = f"{_fmt(width_mm)} mm × {_fmt(length_mm)} mm × {_fmt(thick_mm)} mm"
    wrong_2 = f"{_fmt(length_mm)} mm × {_fmt(thick_mm)} mm × {_fmt(width_mm)} mm"
    wrong_3 = f"{_fmt(length_mm + 100)} mm × {_fmt(width_mm)} mm × {_fmt(thick_mm)} mm"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Read columns from the table [1 mark].\n"
        f"Length = {_fmt(length_mm)} mm, Width = {_fmt(width_mm)} mm, Thickness = {_fmt(thick_mm)} mm.\n"
        f"Step 2: Combine in standard dimension format (L × W × T) [1 mark].\n"
        f"Dimensions = {_fmt(length_mm)} mm × {_fmt(width_mm)} mm × {_fmt(thick_mm)} mm.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="20",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Read the row for the specified component in the cutting table.",
        tier_2=f"Match Length ({_fmt(length_mm)} mm), Width ({_fmt(width_mm)} mm), and Thickness ({_fmt(thick_mm)} mm).",
        tier_3=f"Correct format: {correct_ans}.",
        r=r,
    )


def generate_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Calculate total linear length of timber planks (in metres) needed for a frame."""
    name = r.choice(SA_NAMES)
    project = r.choice(["garden workbench", "raised garden bed", "picnic bench frame", "storage rack"])

    # Planks: 4 legs of L1, 4 side rails of L2, 4 cross braces of L3
    h_mm = r.choice([750, 800, 850, 900])
    l_mm = r.choice([1200, 1400, 1500, 1800])
    w_mm = r.choice([600, 700, 800])

    # 4 legs + 4 rails of length l + 4 rails of length w
    total_mm = 4 * h_mm + 4 * l_mm + 4 * w_mm
    total_m = round(total_mm / 1000, 2)

    prompt = (
        f"{name} is building the frame for a {project}. The frame requires the following timber pieces:\n"
        f"• 4 vertical legs, each {_fmt(h_mm)} mm long\n"
        f"• 4 horizontal side rails, each {_fmt(l_mm)} mm long\n"
        f"• 4 horizontal end rails, each {_fmt(w_mm)} mm long\n"
        f"Calculate the total linear length of timber (in metres) needed to cut all 12 frame pieces."
    )

    correct_ans = f"{_fmt(total_m)} m"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Calculate total length in millimetres [1 mark].\n"
        f"Legs = 4 × {_fmt(h_mm)} mm = {_fmt(4 * h_mm)} mm.\n"
        f"Side rails = 4 × {_fmt(l_mm)} mm = {_fmt(4 * l_mm)} mm.\n"
        f"End rails = 4 × {_fmt(w_mm)} mm = {_fmt(4 * w_mm)} mm.\n"
        f"Total mm = {_fmt(4 * h_mm)} + {_fmt(4 * l_mm)} + {_fmt(4 * w_mm)} = {_fmt(total_mm)} mm.\n"
        f"Step 2: Convert to metres (divide by 1 000) [1 mark].\n"
        f"Total length in metres = {_fmt(total_mm)} ÷ 1 000 = {_fmt(total_m)} m.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="21",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the quantity of each piece by its length, sum the totals in mm, then divide by 1 000 to convert to metres.",
        tier_2=f"Total mm = (4 × {_fmt(h_mm)}) + (4 × {_fmt(l_mm)}) + (4 × {_fmt(w_mm)}) = {_fmt(total_mm)} mm.",
        tier_3=f"Divide by 1 000 to get {_fmt(total_m)} m.",
        r=r,
    )


def generate_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Subskill 22: Calculate total sheet area (in m²) needed for cabinet panels."""
    name = r.choice(SA_NAMES)
    num_shelves = r.choice([3, 4, 5])
    panel_l_cm = r.choice([80, 90, 100, 120])
    panel_w_cm = r.choice([30, 35, 40])

    area_single_m2 = round((panel_l_cm / 100) * (panel_w_cm / 100), 4)
    total_area_m2 = round(num_shelves * area_single_m2, 2)

    prompt = (
        f"{name} is making {num_shelves} identical shelves for a pantry cupboard. "
        f"Each shelf measures {_fmt(panel_l_cm)} cm long by {_fmt(panel_w_cm)} cm wide.\n"
        f"Calculate the total surface area of timber sheeting (in m²) required for all {num_shelves} shelves."
    )

    correct_ans = f"{_fmt(total_area_m2)} m²"
    wrong_1 = f"{_fmt(total_area_m2 * 10)} m²"
    wrong_2 = f"{_fmt(area_single_m2)} m²"
    wrong_3 = f"{_fmt(total_area_m2 * 0.1)} m²"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Convert dimensions to metres [1 mark].\n"
        f"Length = {_fmt(panel_l_cm)} cm = {_fmt(panel_l_cm / 100)} m; Width = {_fmt(panel_w_cm)} cm = {_fmt(panel_w_cm / 100)} m.\n"
        f"Step 2: Calculate area of one shelf [1 mark].\n"
        f"Area per shelf = {_fmt(panel_l_cm / 100)} m × {_fmt(panel_w_cm / 100)} m = {_fmt(area_single_m2)} m².\n"
        f"Step 3: Multiply by {num_shelves} shelves [1 mark].\n"
        f"Total area = {num_shelves} × {_fmt(area_single_m2)} m² = {_fmt(total_area_m2)} m² ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="22",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Convert measurements to metres first, multiply length by width, then multiply by the number of shelves.",
        tier_2=f"One shelf is {_fmt(panel_l_cm / 100)} m × {_fmt(panel_w_cm / 100)} m = {_fmt(area_single_m2)} m².",
        tier_3=f"Total area for {num_shelves} shelves = {_fmt(total_area_m2)} m².",
        r=r,
    )


def generate_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Subskill 23: Determine logical assembly sequence from numbered assembly diagrams."""
    furniture = r.choice(["flat-pack study desk", "wardrobe cabinet", "bedside table", "bookshelf"])

    prompt = (
        f"When assembling a {furniture} using manufacturer step-by-step instructions, which sequence of assembly "
        f"steps is structurally correct and safe?"
    )

    correct_ans = "Insert wooden dowels and fix side panels to base first, attach top panel, then screw on the back stabilizing board"
    wrong_1 = "Nail the back stabilizing board into thin air first before attaching any side panels or base"
    wrong_2 = "Insert all drawers and shelves into the room before assembling the outer carcass frame"
    wrong_3 = "Attach the top panel to the side panels, leave out the base, and hang the drawers from the top"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand structural carcass assembly principles [1 mark].\n"
        f"Rigidity requires building the primary lower frame (base and sides) before securing the top.\n"
        f"Step 2: Identify squaring and stabilization [1 mark].\n"
        f"The backboard provides lateral shear strength and must be secured once the outer rectangular box is assembled.\n"
        f"Step 3: Stated sequence [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="23",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Think about how a box is built: build the bottom and sides first, then the top, and square it with the back.",
        tier_2="Base and side panels must be joined before the top panel can be installed.",
        tier_3=f"Correct sequence: {correct_ans}.",
        r=r,
    )


def generate_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Subskill 24: Identify hardware fasteners from technical symbols and bill of materials."""
    fastener = r.choice([
        ("Cam Lock Nut & Connecting Bolt", "a two-piece concealed fastener where a round rotating metal cam tightens over a threaded pin", "rigid hidden 90° panel joinery"),
        ("Wooden Fluted Dowel", "a small cylindrical grooved wooden pin inserted into pre-drilled holes with glue", "aligning and reinforcing butt joints"),
        ("L-Shaped Corner Bracket", "a 90° bent metal angle plate secured with screws into internal corners", "reinforcing corner joints against racking"),
        ("Euro Screw / Confirmat Screw", "a heavy-duty thick-threaded screw designed specifically for particle board", "directly fastening carcass panels together"),
    ])
    f_name, f_desc, f_use = fastener

    prompt = (
        f"A hardware pack for a flat-pack kitchen cupboard includes {f_desc}. "
        f"What is the standard name of this hardware fastener, and what is its primary function?"
    )

    correct_ans = f"{f_name} (used for {f_use})"
    distractors = [
        f"{other[0]} (used for {other[2]})"
        for other in [
            ("Cam Lock Nut & Connecting Bolt", "", "rigid hidden 90° panel joinery"),
            ("Wooden Fluted Dowel", "", "aligning and reinforcing butt joints"),
            ("L-Shaped Corner Bracket", "", "reinforcing corner joints against racking"),
            ("Euro Screw / Confirmat Screw", "", "directly fastening carcass panels together"),
        ]
        if other[0] != f_name
    ][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Match physical description to hardware component [1 mark].\n"
        f"{f_desc} describes a {f_name}.\n"
        f"Step 2: Identify mechanical function [1 mark].\n"
        f"Its primary role is {f_use}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="24",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Identify the hardware item by its shape and mechanical function.",
        tier_2=f"The description corresponds to: {f_name}.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Subskill 25: Calculate total material cost from a bill of quantities and unit rates."""
    name = r.choice(SA_NAMES)

    timber_qty = r.choice([6, 8, 10, 12])
    timber_rate = r.choice([85.0, 95.0, 110.0, 125.0])
    timber_total = timber_qty * timber_rate

    screw_boxes = r.choice([2, 3])
    screw_rate = 65.0
    screw_total = screw_boxes * screw_rate

    varnish_tins = 2
    varnish_rate = 145.0
    varnish_total = varnish_tins * varnish_rate

    grand_total = round(timber_total + screw_total + varnish_total, 2)

    prompt = (
        f"{name} prepares a Bill of Quantities to build custom patio furniture:\n"
        f"• Timber Planks: {timber_qty} lengths at {_fmt_curr(timber_rate)} each\n"
        f"• Screws: {screw_boxes} boxes at {_fmt_curr(screw_rate)} per box\n"
        f"• Varnish: {varnish_tins} tins at {_fmt_curr(varnish_rate)} per tin\n"
        f"Calculate the grand total cost of materials in Rands."
    )

    correct_ans = _fmt_curr(grand_total)
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Calculate subtotal for each item [1 mark].\n"
        f"Timber = {timber_qty} × {_fmt_curr(timber_rate)} = {_fmt_curr(timber_total)}.\n"
        f"Screws = {screw_boxes} × {_fmt_curr(screw_rate)} = {_fmt_curr(screw_total)}.\n"
        f"Varnish = {varnish_tins} × {_fmt_curr(varnish_rate)} = {_fmt_curr(varnish_total)}.\n"
        f"Step 2: Add all subtotals together [1 mark].\n"
        f"Grand Total = {_fmt_curr(timber_total)} + {_fmt_curr(screw_total)} + {_fmt_curr(varnish_total)} = {_fmt_curr(grand_total)}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="25",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply quantity by unit rate for each material item, then add the results.",
        tier_2=f"Timber = {_fmt_curr(timber_total)}, Screws = {_fmt_curr(screw_total)}, Varnish = {_fmt_curr(varnish_total)}.",
        tier_3=f"Grand total = {_fmt_curr(grand_total)}.",
        r=r,
    )


def generate_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Subskill 26: Cutting layout optimization from standard board (1 220 mm x 2 440 mm)."""
    name = r.choice(SA_NAMES)
    board_l = 2440
    board_w = 1220

    # Panel dimensions: choose clean divisions
    # e.g. 600 mm x 400 mm
    panel_l = r.choice([600, 800])
    panel_w = r.choice([400, 500])

    # Orientation 1: panel_l along board_l, panel_w along board_w
    n1_along_l = board_l // panel_l
    n1_along_w = board_w // panel_w
    total_opt1 = n1_along_l * n1_along_w

    # Orientation 2: panel_w along board_l, panel_l along board_w
    n2_along_l = board_l // panel_w
    n2_along_w = board_w // panel_l
    total_opt2 = n2_along_l * n2_along_w

    max_panels = max(total_opt1, total_opt2)

    prompt = (
        f"{name} needs to cut identical rectangular panels measuring {_fmt(panel_l)} mm by {_fmt(panel_w)} mm "
        f"from a standard sheet of plywood measuring {_fmt(board_l)} mm by {_fmt(board_w)} mm. "
        f"Assuming all panels are cut in the same orientation with negligible saw blade kerf (cutting width), "
        f"what is the maximum number of whole panels {name} can cut from one sheet?"
    )

    correct_ans = f"{max_panels} panels"
    wrong_1 = f"{min(total_opt1, total_opt2)} panels"
    wrong_2 = f"{max_panels + 2} panels"
    wrong_3 = f"{max(1, max_panels - 3)} panels"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Test Orientation 1 (Lengthwise) [1 mark].\n"
        f"Along length: {board_l} ÷ {panel_l} = {n1_along_l} panels.\n"
        f"Along width: {board_w} ÷ {panel_w} = {n1_along_w} panels.\n"
        f"Total Orientation 1 = {n1_along_l} × {n1_along_w} = {total_opt1} panels.\n"
        f"Step 2: Test Orientation 2 (Rotated 90°) [1 mark].\n"
        f"Along length: {board_l} ÷ {panel_w} = {n2_along_l} panels.\n"
        f"Along width: {board_w} ÷ {panel_l} = {n2_along_w} panels.\n"
        f"Total Orientation 2 = {n2_along_l} × {n2_along_w} = {total_opt2} panels.\n"
        f"Step 3: Select maximum [1 mark]: Maximum = {max_panels} panels ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="26",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Test both orientations: divide board dimensions by panel dimensions and multiply the whole numbers.",
        tier_2=f"Orientation 1 yields {total_opt1} panels ({n1_along_l} × {n1_along_w}); Orientation 2 yields {total_opt2} panels ({n2_along_l} × {n2_along_w}).",
        tier_3=f"The maximum whole panels cut is {max_panels}.",
        r=r,
    )


def generate_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Subskill 27: Percentage material wastage calculation during sheet fabrication."""
    name = r.choice(SA_NAMES)
    board_area = round(1.22 * 2.44, 4)  # 2.9768 m²

    num_panels = r.choice([8, 10, 12])
    panel_area_single = r.choice([0.18, 0.20, 0.22])
    useful_area = round(num_panels * panel_area_single, 4)

    wasted_area = round(board_area - useful_area, 4)
    waste_percent = round((wasted_area / board_area) * 100, 1)

    prompt = (
        f"{name} cuts {num_panels} panels from a standard board with a total surface area of {_fmt(board_area, 2)} m². "
        f"Each cut panel has a surface area of {_fmt(panel_area_single, 2)} m², giving a total useful panel area of "
        f"{_fmt(useful_area, 2)} m².\n"
        f"Calculate the percentage of timber board wasted as off-cuts (round to one decimal place)."
    )

    correct_ans = f"{_fmt(waste_percent, 1)}%"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Calculate wasted area [1 mark].\n"
        f"Wasted area = Total Area - Useful Area = {_fmt(board_area, 2)} m² - {_fmt(useful_area, 2)} m² = {_fmt(wasted_area, 2)} m².\n"
        f"Step 2: Express as percentage of total board area [1 mark].\n"
        f"Percentage waste = (Wasted Area ÷ Total Area) × 100% = ({_fmt(wasted_area, 2)} ÷ {_fmt(board_area, 2)}) × 100%.\n"
        f"Step 3: Stated percentage [1 mark]: {_fmt(waste_percent, 1)}% ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="27",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Percentage waste = (Wasted Area ÷ Total Area) × 100%.",
        tier_2=f"Subtract useful area ({_fmt(useful_area, 2)} m²) from total area ({_fmt(board_area, 2)} m²) to get waste of {_fmt(wasted_area, 2)} m².",
        tier_3=f"({_fmt(wasted_area, 2)} ÷ {_fmt(board_area, 2)}) × 100% = {_fmt(waste_percent, 1)}%.",
        r=r,
    )
