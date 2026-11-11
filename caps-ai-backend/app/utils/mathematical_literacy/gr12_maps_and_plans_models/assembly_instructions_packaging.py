"""Subskills 33-40: Assembly Instructions & Packaging Models for Grade 12 Maps & Plans (Models)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def gen_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Subskill 33: Identifying component sequence from exploded assembly diagram."""
    prompt = (
        "In a flat-pack furniture assembly instruction manual, a three-shelf bookcase is constructed "
        "from a base panel, two side panels, a top panel, two adjustable shelves, and a hardboard backing.\n\n"
        "According to standard mechanical assembly principles, what is the CORRECT logical order of assembly?"
    )

    correct_ans = "1. Connect side panels to base panel; 2. Attach top panel; 3. Nail on backing board to square the frame; 4. Insert shelf pins and shelves"
    custom_opts = [
        correct_ans,
        "1. Nail on backing board; 2. Insert shelves; 3. Attach side panels; 4. Attach base panel",
        "1. Insert shelf pins; 2. Attach top panel; 3. Attach base panel; 4. Attach side panels",
        "1. Glue shelves to top panel; 2. Attach backing board; 3. Attach side panels; 4. Attach base",
    ]

    t1 = "Consider structural stability: you cannot nail a backing board before the perimeter frame exists."
    t2 = "The perimeter frame (base, sides, top) must be built first, followed by the backing to hold it rigid and square."
    t3 = "The correct sequence is: base and sides, then top panel, then square with backing board, and finally movable internal shelves."

    explanation = [
        f"Step 1: Identify structural sequence: rigid outer perimeter frame must be erected first [1 Mark: Method].",
        f"Step 2: Backing board must be affixed to provide diagonal shear stability and square the frame [1 Mark: Method].",
        f"Step 3: Internal adjustable components are inserted last [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_33",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Subskill 34: Bolt, dowel, and cam-lock fastener inventory verification."""
    # Bookcase assembly hardware
    cam_locks_per_joint = 2
    joints_count = 4  # top-left, top-right, bottom-left, bottom-right
    cam_locks_required = cam_locks_per_joint * joints_count  # 8
    dowels_per_joint = 2
    dowels_required = dowels_per_joint * joints_count  # 8
    shelf_pins_per_shelf = 4
    shelves_count = r.choice([2, 3, 4])
    shelf_pins_required = shelf_pins_per_shelf * shelves_count

    total_fasteners = cam_locks_required + dowels_required + shelf_pins_required

    prompt = (
        f"A learner unpacks a flat-pack storage unit with {shelves_count} adjustable internal shelves.\n"
        f"The assembly instructions specify the following hardware requirements:\n"
        f"  - 8 cam-lock studs and 8 matching cam bolts for the frame corners\n"
        f"  - 8 wooden fluted dowels for frame alignment\n"
        f"  - 4 metal shelf support pins per adjustable shelf\n\n"
        f"Calculate the TOTAL number of fasteners (cam studs, bolts, dowels, and shelf pins) required to complete the assembly."
    )

    # 8 studs + 8 bolts = 16 cam components, + 8 dowels = 24, + (4 * shelves_count) pins
    total_count = 16 + 8 + shelf_pins_required
    correct_ans = f"{total_count} hardware pieces"
    custom_opts = [
        correct_ans,
        f"{total_count - 4} hardware pieces",
        f"{total_count + 8} hardware pieces",
        f"{8 + 8 + shelf_pins_required} hardware pieces",
    ]

    t1 = f"Remember that cam locks consist of both the stud (8) and the cam bolt (8), totaling 16 pieces."
    t2 = f"Add 8 wooden dowels: 16 + 8 = 24. Then add {shelves_count} shelves × 4 pins = {shelf_pins_required} pins."
    t3 = f"Total = 16 + 8 + {shelf_pins_required} = {total_count} hardware pieces."

    explanation = [
        f"Step 1: Frame cam fittings = 8 studs + 8 cam bolts = 16 pieces [1 Mark: Method].",
        f"Step 2: Add dowels (8) and shelf pins ({shelves_count} × 4 = {shelf_pins_required}) [1 Mark: Method].",
        f"Step 3: Total hardware count = 16 + 8 + {shelf_pins_required} = {total_count} hardware pieces [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_34",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Subskill 35: Left-hand vs right-hand panel symmetry identification."""
    prompt = (
        "During the assembly of a two-door kitchen under-counter cupboard, a builder must distinguish "
        "between the Left Side Panel (A) and the Right Side Panel (B).\n"
        "Both panels have identical outer rectangular dimensions.\n\n"
        "How can the assembler positively identify the interior facing side and whether the panel belongs on the left or right?"
    )

    correct_ans = "The pre-drilled hinge cups and shelf pin holes are located strictly on the interior face; the finished melamine edge must face the front"
    custom_opts = [
        correct_ans,
        "The left panel is always 5 mm thicker than the right panel to balance drawer weight",
        "The manufacturer prints a large red serial barcode on the outside visible surface of panel A",
        "Both panels are completely interchangeable with holes on both exterior sides",
    ]

    t1 = "Consider where hardware (hinges, shelf pins) must be mounted on cabinetry."
    t2 = "Hardware must be on the interior face, and the finished edge banding faces the forward opening."
    t3 = "The correct distinguishing feature is that pre-drilled holes are on the interior face with the finished edge facing the front."

    explanation = [
        f"Step 1: Understand cabinet construction standards: shelf pin and hinge drillings face inward [1 Mark: Method].",
        f"Step 2: Raw chipboard edges face the wall/rear, while finished edged veneer faces the front [1 Mark: Method].",
        f"Step 3: State the exact orientation rule [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_35",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Subskill 36: Flat-pack carton internal volume and minimum box dimensions."""
    # Stack of furniture panels:
    # 2 side panels: 1 800 mm x 400 mm x 16 mm each
    # 1 top panel: 800 mm x 400 mm x 16 mm
    # 1 bottom panel: 800 mm x 400 mm x 16 mm
    # 3 shelves: 768 mm x 380 mm x 16 mm each
    # Total 7 panels stacked. Total thickness = 7 * 16 mm = 112 mm
    # Max length = 1 800 mm, max width = 400 mm
    box_l_mm = 1820  # +20 mm clearance
    box_w_mm = 420   # +20 mm clearance
    box_h_mm = 130   # +18 mm clearance for packaging foam

    # Volume in m³ = (box_l * box_w * box_h) / 10^9
    vol_m3 = (box_l_mm * box_w_mm * box_h_mm) / 1e9

    prompt = (
        f"A furniture factory manufactures flat-pack desks. A disassembled desk is packed into a corrugated carton "
        f"with internal dimensions of {box_l_mm} mm long by {box_w_mm} mm wide by {box_h_mm} mm high.\n\n"
        f"Calculate the internal volume of the packaging carton in cubic metres (m³).\n"
        f"(Hint: 1 m³ = 1 000 000 000 mm³; round your answer to four decimal places)."
    )

    correct_ans = f"{_fmt(vol_m3, 4)} m³"
    custom_opts = [
        correct_ans,
        f"{_fmt(vol_m3 * 10, 4)} m³",
        f"{_fmt(vol_m3 / 10, 4)} m³",
        f"{_fmt((box_l_mm * box_w_mm * box_h_mm) / 1e6, 2)} m³",
    ]

    t1 = "Multiply length × width × height in millimetres to get volume in mm³."
    t2 = "Divide the volume in mm³ by 1 000 000 000 (10⁹) to convert to cubic metres."
    t3 = f"Volume in mm³ = {box_l_mm} × {box_w_mm} × {box_h_mm} = {box_l_mm * box_w_mm * box_h_mm} mm³. In m³ = {box_l_mm * box_w_mm * box_h_mm} ÷ 10⁹ = {_fmt(vol_m3, 4)} m³."

    explanation = [
        f"Step 1: Calculate volume in mm³: V = L × W × H = {box_l_mm} × {box_w_mm} × {box_h_mm} = {_fmt(box_l_mm * box_w_mm * box_h_mm, 0)} mm³ [1 Mark: Method].",
        f"Step 2: Conversion factor: 1 m³ = (1 000 mm)³ = 1 000 000 000 mm³ [1 Mark: Method].",
        f"Step 3: Internal volume = {_fmt(box_l_mm * box_w_mm * box_h_mm, 0)} ÷ 10⁹ = {_fmt(vol_m3, 4)} m³ [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_36",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Corrugated box wall thickness deduction for net inside capacity."""
    wall_thickness_mm = r.choice([6.0, 7.5, 8.0])
    ext_l_mm = r.choice([800, 900, 1000])
    ext_w_mm = r.choice([500, 600])
    ext_h_mm = r.choice([150, 200])

    # Net inside = external - 2 * wall_thickness for each dimension
    net_l_mm = ext_l_mm - (2 * wall_thickness_mm)
    net_w_mm = ext_w_mm - (2 * wall_thickness_mm)
    net_h_mm = ext_h_mm - (2 * wall_thickness_mm)

    d_spec_37 = {
        "diagram_role": "context",
        "kind": "packaging_cartons",
        "title": f"Corrugated Box: {ext_l_mm} x {ext_w_mm} x {ext_h_mm} mm",
        "box": {"length": ext_l_mm, "width": ext_w_mm, "height": ext_h_mm, "wall_thickness": wall_thickness_mm},
        "container": {"length": ext_l_mm, "width": ext_w_mm, "height": ext_h_mm},
        "dims": {"length": ext_l_mm, "width": ext_w_mm, "height": ext_h_mm},
        "carton_l": ext_l_mm,
        "box_l": ext_l_mm,
    }

    prompt = (
        f"A heavy-duty double-wall corrugated shipping box has EXTERNAL dimensions of:\n"
        f"  - Length = {ext_l_mm} mm\n"
        f"  - Width = {ext_w_mm} mm\n"
        f"  - Height = {ext_h_mm} mm\n"
        f"The corrugated cardboard wall has a thickness of {_fmt(wall_thickness_mm, 1)} mm on every side.\n\n"
        f"Calculate the NET INTERNAL length, width, and height available for packing product panels."
    )

    correct_ans = f"{_fmt(net_l_mm, 1)} mm × {_fmt(net_w_mm, 1)} mm × {_fmt(net_h_mm, 1)} mm"
    custom_opts = [
        correct_ans,
        f"{_fmt(ext_l_mm - wall_thickness_mm, 1)} mm × {_fmt(ext_w_mm - wall_thickness_mm, 1)} mm × {_fmt(ext_h_mm - wall_thickness_mm, 1)} mm",
        f"{_fmt(net_l_mm - 10, 1)} mm × {_fmt(net_w_mm - 10, 1)} mm × {_fmt(net_h_mm - 10, 1)} mm",
        f"{ext_l_mm} mm × {ext_w_mm} mm × {ext_h_mm} mm",
    ]

    t1 = f"Deduct TWO wall thicknesses (2 × {_fmt(wall_thickness_mm, 1)} mm = {_fmt(2 * wall_thickness_mm, 1)} mm) from each external dimension."
    t2 = f"Internal length = {ext_l_mm} - {_fmt(2 * wall_thickness_mm, 1)} mm."
    t3 = f"Length = {ext_l_mm} - {_fmt(2 * wall_thickness_mm, 1)} = {_fmt(net_l_mm, 1)} mm; Width = {ext_w_mm} - {_fmt(2 * wall_thickness_mm, 1)} = {_fmt(net_w_mm, 1)} mm; Height = {ext_h_mm} - {_fmt(2 * wall_thickness_mm, 1)} = {_fmt(net_h_mm, 1)} mm."

    explanation = [
        f"Step 1: Total wall deduction per axis = 2 × {_fmt(wall_thickness_mm, 1)} mm = {_fmt(2 * wall_thickness_mm, 1)} mm [1 Mark: Method].",
        f"Step 2: Net length = {ext_l_mm} - {_fmt(2 * wall_thickness_mm, 1)} = {_fmt(net_l_mm, 1)} mm; Net width = {ext_w_mm} - {_fmt(2 * wall_thickness_mm, 1)} = {_fmt(net_w_mm, 1)} mm [1 Mark: Method].",
        f"Step 3: Net height = {ext_h_mm} - {_fmt(2 * wall_thickness_mm, 1)} = {_fmt(net_h_mm, 1)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_37",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_37,
    )


def gen_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: Carton gross mass calculation (Net product mass + Packaging tare mass)."""
    product_mass_kg = r.choice([24.5, 28.0, 32.4, 38.6])
    box_tare_kg = 2.4
    styrofoam_tare_kg = 0.8
    hardware_tare_kg = 0.6
    total_tare_kg = box_tare_kg + styrofoam_tare_kg + hardware_tare_kg
    gross_mass_kg = product_mass_kg + total_tare_kg

    prompt = (
        f"A courier company bills freight according to gross package weight.\n"
        f"A flat-pack wardrobe has a net timber panel mass of {_fmt(product_mass_kg, 1)} kg.\n"
        f"The packaging materials include:\n"
        f"  - Outer corrugated cardboard carton: {_fmt(box_tare_kg, 1)} kg\n"
        f"  - Expanded polystyrene edge protectors: {_fmt(styrofoam_tare_kg, 1)} kg\n"
        f"  - Hardware blister pack and instruction booklet: {_fmt(hardware_tare_kg, 1)} kg\n\n"
        f"Calculate the TOTAL gross shipping mass of the carton in kilograms."
    )

    correct_ans = f"{_fmt(gross_mass_kg, 1)} kg"
    custom_opts = [
        correct_ans,
        f"{_fmt(product_mass_kg, 1)} kg",
        f"{_fmt(product_mass_kg + box_tare_kg, 1)} kg",
        f"{_fmt(gross_mass_kg * 1.2, 1)} kg",
    ]

    t1 = "Gross mass = Net product mass + All packaging tare masses."
    t2 = f"Sum the tare masses: {_fmt(box_tare_kg, 1)} + {_fmt(styrofoam_tare_kg, 1)} + {_fmt(hardware_tare_kg, 1)} = {_fmt(total_tare_kg, 1)} kg."
    t3 = f"Gross mass = {_fmt(product_mass_kg, 1)} + {_fmt(total_tare_kg, 1)} = {_fmt(gross_mass_kg, 1)} kg."

    explanation = [
        f"Step 1: Calculate total packaging tare mass: {_fmt(box_tare_kg, 1)} + {_fmt(styrofoam_tare_kg, 1)} + {_fmt(hardware_tare_kg, 1)} = {_fmt(total_tare_kg, 1)} kg [1 Mark: Method].",
        f"Step 2: Add net product mass to tare mass: Gross = {_fmt(product_mass_kg, 1)} kg + {_fmt(total_tare_kg, 1)} kg [1 Mark: Method].",
        f"Step 3: Total gross shipping mass = {_fmt(gross_mass_kg, 1)} kg [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_38",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Orientation comparison for optimal flat-pack arrangement."""
    prompt = (
        "When packing heavy flat furniture panels into a corrugated cardboard carton, packaging engineers "
        "must choose between laying panels flat vs standing them on edge during pallet transport.\n\n"
        "Why is it mechanically preferred to pack and ship flat-pack panels lying completely flat?"
    )

    correct_ans = "It distributes heavy weight uniformly across the broad surface, preventing bowing, edge crushing, and corner cracking"
    custom_opts = [
        correct_ans,
        "It reduces the actual mass of the wood panels by lowering atmospheric friction",
        "It eliminates the need for glue or fasteners during the assembly stage",
        "It allows moisture to evaporate faster through the edges of the box",
    ]

    t1 = "Think about pressure: Pressure = Force ÷ Area."
    t2 = "A broad flat surface distributes load evenly and prevents concentrated edge shear."
    t3 = "The correct engineering justification is uniform weight distribution preventing bowing, warping, and edge breakage."

    explanation = [
        f"Step 1: Evaluate mechanical forces acting on stacked timber boards [1 Mark: Method].",
        f"Step 2: Compare contact surface area (flat face vs thin edge) [1 Mark: Method].",
        f"Step 3: Conclude that flat orientation distributes load uniformly and prevents transit damage [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_39",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: Flat-pack instruction symbol decoding."""
    symbols = [
        {"icon": "Two people lifting a carton together", "meaning": "Team lift required (box exceeds 25 kg safe single-person handling limit)"},
        {"icon": "An electric power drill with a red diagonal strike-through bar", "meaning": "Do not use a power drill or impact driver; hand-tighten only to avoid stripping screw threads"},
        {"icon": "A mallet/hammer tapping a wooden block gently against a panel", "meaning": "Use a wooden block to protect veneer when tapping dowels or joints into place"},
        {"icon": "A rug or blanket placed beneath the furniture unit during assembly", "meaning": "Assemble unit on a soft rug or carpet to prevent scratching the face veneer"},
    ]
    item = r.choice(symbols)

    prompt = (
        f"On page 1 of a flat-pack furniture instruction manual, a safety icon shows: '{item['icon']}'.\n\n"
        f"What is the correct technical interpretation of this symbol?"
    )

    correct_ans = item["meaning"]
    custom_opts = [
        correct_ans,
        "This product is strictly for commercial industrial factory use",
        "The manufacturer provides a 10-year warranty if returned unopened",
        "Assembly must be completed within 15 minutes of unsealing the carton",
    ]

    t1 = "Read the literal visual elements in the symbol description."
    t2 = "Consider consumer product safety and assembly precautions."
    t3 = f"The correct meaning is: {item['meaning']}."

    explanation = [
        f"Step 1: Identify the graphic elements described in the symbol [1 Mark: Method].",
        f"Step 2: Match the visual prompt to standard consumer product safety protocols [1 Mark: Method].",
        f"Step 3: State the correct meaning: {item['meaning']} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_40",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )
