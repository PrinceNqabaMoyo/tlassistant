"""Cluster 1: Assembly Diagrams & Component Hardware (Subskills 1 to 9).

Covers:
1. Parts list & hardware inventory calculations
2. Assembly step sequence & logical ordering
3. Tool identification & correct usage (Allen key, screwdrivers, spanners)
4. Fastener quantities & pilot hole alignment
5. Directional arrows & pictorial symbols
6. Warning symbols & safety precautions (anti-tip brackets, two-person lifts)
7. Electronic device disassembly/assembly (SIM card, battery orientation)
8. Cabinet hinge & drawer runner mounting orientation
9. Modular shelving unit tier spacing & height calculations
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_asm_diag_parts_list_hardware_inventory(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    item_type = r.choice(["bookcase", "TV cabinet", "study desk", "wardrobe"])
    panels = r.randint(4, 8)
    dowels_per_panel = r.choice([2, 4, 6])
    total_dowels = panels * dowels_per_panel
    cams = r.choice([8, 12, 16, 20])
    screws = r.choice([16, 24, 32, 40])
    pack_dowels = total_dowels + r.choice([2, 4])  # includes spares

    diag = {
        "kind": "inline_svg",
        "title": f"Parts List & Hardware Inventory ({item_type.title()})",
        "svg": (
            f'<svg viewBox="0 0 400 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="400" height="160" fill="#f8fafc" stroke="#cbd5e1" rx="8"/>'
            f'<text x="20" y="30" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Parts List &amp; Hardware Count</text>'
            f'<rect x="20" y="45" width="360" height="95" fill="#ffffff" stroke="#e2e8f0" rx="4"/>'
            f'<text x="35" y="70" font-family="sans-serif" font-size="12" fill="#334155">Structural Panels: {panels} panels</text>'
            f'<text x="35" y="90" font-family="sans-serif" font-size="12" fill="#334155">Dowels per panel required: {dowels_per_panel} dowels</text>'
            f'<text x="35" y="110" font-family="sans-serif" font-size="12" fill="#334155">Dowels supplied in pack: {pack_dowels} units</text>'
            f'<text x="35" y="130" font-family="sans-serif" font-size="12" fill="#64748b">Cam locks: {cams} | Connecting screws: {screws}</text>'
            f'</svg>'
        ),
    }

    prompt = (
        f"{name} buys a flat-pack {item_type} from a furniture retailer. "
        f"Refer to the accompanying parts list and assembly diagram.\n\n"
        f"Each structural panel requires exactly {dowels_per_panel} wooden dowels to join the frame. "
        f"How many spare wooden dowels will {name} have left over after assembling all {panels} panels?"
    )
    spare = pack_dowels - total_dowels
    ans = f"{spare} spare dowels"

    s1 = f"Identify total dowels required by multiplying {panels} panels by {dowels_per_panel} dowels per panel, then subtract from supplied total."
    s2 = f"✓ [1 Mark: Method – Calculating required dowels and subtracting from pack]\nRequired = {panels} × {dowels_per_panel} = {total_dowels} dowels.\nSpare = {pack_dowels} − {total_dowels}."
    s3 = f"✓ [1 Mark: Accuracy – Spare dowels remaining]\nLeft over = {spare} spare dowels."

    return _build_question_payload(
        "asm_diag_parts_list_hardware_inventory",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Calculate the total number of dowels used for the {panels} panels.",
        tier_2_hint=f"Total required = {panels} × {dowels_per_panel} = {total_dowels}. Subtract this from {pack_dowels}.",
        tier_3_hint=f"{pack_dowels} − {total_dowels} = {spare} spare dowels.",
        diagram_spec=diag,
    )


def _gen_asm_diag_step_sequence_order_determination(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    diag = {
        "kind": "inline_svg",
        "title": f"Assembly Steps Sequence Diagram ({name})",
        "svg": (
            '<svg viewBox="0 0 420 140" width="100%" height="140" xmlns="http://www.w3.org/2000/svg">'
            '<rect width="420" height="140" fill="#f8fafc" stroke="#cbd5e1" rx="8"/>'
            '<rect x="20" y="20" width="80" height="100" fill="#ffffff" stroke="#94a3b8" rx="6"/>'
            '<text x="60" y="45" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">Step P</text>'
            '<text x="60" y="75" font-family="sans-serif" font-size="10" text-anchor="middle" fill="#64748b">Ridge Cap</text>'
            '<rect x="120" y="20" width="80" height="100" fill="#ffffff" stroke="#94a3b8" rx="6"/>'
            '<text x="160" y="45" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">Step Q</text>'
            '<text x="160" y="75" font-family="sans-serif" font-size="10" text-anchor="middle" fill="#64748b">Outer Frame</text>'
            '<rect x="220" y="20" width="80" height="100" fill="#ffffff" stroke="#94a3b8" rx="6"/>'
            '<text x="260" y="45" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">Step R</text>'
            '<text x="260" y="75" font-family="sans-serif" font-size="10" text-anchor="middle" fill="#64748b">Roof Panels</text>'
            '<rect x="320" y="20" width="80" height="100" fill="#ffffff" stroke="#94a3b8" rx="6"/>'
            '<text x="360" y="45" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">Step S</text>'
            '<text x="360" y="75" font-family="sans-serif" font-size="10" text-anchor="middle" fill="#64748b">Floor Panel</text>'
            '</svg>'
        ),
    }
    prompt = (
        f"{name} is assembling a wooden dog kennel according to the manufacturer's 4-step assembly diagram shown.\n\n"
        f"The four steps are illustrated in random order:\n"
        f"P: Fasten ridge cap and level feet.\n"
        f"Q: Align front, side, and back panels to form outer frame.\n"
        f"R: Fasten sloping roof panels onto walls.\n"
        f"S: Slide floor panel into position onto internal base ledge.\n\n"
        f"Which of the following represents the correct, logical chronological sequence of assembly?"
    )
    ans = "Q → S → R → P"
    opts = ["Q → S → R → P", "S → Q → P → R", "Q → R → S → P", "R → Q → S → P"]

    s1 = f"A kennel must have its outer wall frame erected first (Q), then the floor inserted before the roof seals the structure (S), then the roof panels secured (R), and finally the ridge cap and leveling feet (P)."
    s2 = f"✓ [1 Mark: Method – Logical sequential deduction from foundation to roof]\n1st: Frame assembly (Q)\n2nd: Floor insertion (S)\n3rd: Roof attachment (R)\n4th: Ridge cap finishing & leveling (P)."
    s3 = f"✓ [1 Mark: Accuracy – Correct step sequence]\nSequence: Q → S → R → P."

    return _build_question_payload(
        "asm_diag_step_sequence_order_determination",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Think about why you cannot put the floor in after the roof is screwed on.",
        tier_2_hint="Walls must be built (Q) before the floor drops in (S), followed by the main roof (R) and ridge cap (P).",
        tier_3_hint="The correct sequence is Q → S → R → P.",
        diagram_spec=diag,
    )


def _gen_asm_diag_tool_selection_and_usage(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    fastener = r.choice([
        ("hex-head socket screw (recessed six-sided bolt)", "Allen key (hex wrench)", "Phillips screwdriver", "Flathead screwdriver", "Rubber mallet"),
        ("cross-shaped recess screw (+ symbol head)", "Phillips screwdriver", "Flathead screwdriver", "Allen key (hex wrench)", "Adjustable spanner"),
        ("single straight slot screw head", "Flathead screwdriver", "Phillips screwdriver", "Allen key (hex wrench)", "Pliers"),
        ("hexagonal outer bolt nut (6 flat exterior sides)", "Spanner (or socket wrench)", "Phillips screwdriver", "Flathead screwdriver", "Allen key"),
    ])
    f_desc, correct_tool, d1, d2, d3 = fastener

    prompt = (
        f"{name} is opening a flat-pack furniture carton. The assembly instructions specify that fastener 'Part G' "
        f"is a {f_desc}.\n\n"
        f"Which tool is strictly designed and required to tighten this specific fastener correctly without stripping the head?"
    )
    ans = correct_tool
    opts = [correct_tool, d1, d2, d3]

    s1 = f"Match the fastener drive type with the corresponding mechanical hand tool."
    s2 = f"✓ [1 Mark: Method – Identifying the mating tool profile for {f_desc}]\nThe drive shape requires a mating profile that locks securely."
    s3 = f"✓ [1 Mark: Accuracy – Exact tool identification]\nRequired tool: {correct_tool}."

    return _build_question_payload(
        "asm_diag_tool_selection_and_usage",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Examine the shape of the screw/bolt head described: {f_desc}.",
        tier_2_hint=f"Each fastener type requires a matching tool profile to avoid stripping.",
        tier_3_hint=f"The correct tool is {correct_tool}.",
    )


def _gen_asm_diag_furniture_screw_pilot_hole_alignment(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    drawers = r.choice([3, 4, 5, 6])
    screws_per_runner = r.choice([2, 3, 4])
    runners_per_drawer = 2  # left and right side
    handle_screws = 2
    total_screws = drawers * (runners_per_drawer * screws_per_runner + handle_screws)

    diag = {
        "kind": "inline_svg",
        "title": "Drawer Hardware Pilot Alignment Diagram",
        "svg": (
            f'<svg viewBox="0 0 380 150" width="100%" height="150" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="380" height="150" fill="#f8fafc" stroke="#cbd5e1" rx="8"/>'
            f'<text x="20" y="28" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">Chest of Drawers: {drawers} Drawer Units</text>'
            f'<rect x="30" y="45" width="320" height="85" fill="#ffffff" stroke="#94a3b8" rx="4"/>'
            f'<text x="45" y="75" font-family="sans-serif" font-size="12" fill="#1e293b">Runners per drawer: 2 (left &amp; right)</text>'
            f'<text x="45" y="95" font-family="sans-serif" font-size="12" fill="#1e293b">Screws per runner: {screws_per_runner} screws</text>'
            f'<text x="45" y="115" font-family="sans-serif" font-size="12" fill="#1e293b">Handle screws: {handle_screws} screws</text>'
            f'</svg>'
        ),
    }

    prompt = (
        f"{name} is assembling a chest of drawers with {drawers} identical pull-out drawer boxes. "
        f"Refer to the accompanying hardware alignment diagram.\n\n"
        f"• Each drawer requires 2 metal roller runners (one left, one right).\n"
        f"• Each metal runner is secured to the drawer body using {screws_per_runner} screws.\n"
        f"• Each drawer has 1 handle secured by {handle_screws} screws from the inside.\n\n"
        f"Calculate the total number of screws required to assemble all {drawers} drawers completely."
    )
    per_drawer = runners_per_drawer * screws_per_runner + handle_screws
    ans = f"{total_screws} screws"

    s1 = f"Calculate the number of screws required for one drawer (runners + handle), then multiply by {drawers} drawers."
    s2 = f"✓ [1 Mark: Method – Screws per drawer and total multiplication]\nScrews per drawer = (2 runners × {screws_per_runner}) + {handle_screws} handle screws = {per_drawer} screws.\nTotal = {drawers} × {per_drawer}."
    s3 = f"✓ [1 Mark: Accuracy – Total screws]\nTotal screws required = {total_screws} screws."

    return _build_question_payload(
        "asm_diag_furniture_screw_pilot_hole_alignment",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint="Find how many screws are needed for just one drawer first.",
        tier_2_hint=f"1 drawer needs (2 × {screws_per_runner}) + {handle_screws} = {per_drawer} screws. Multiply by {drawers}.",
        tier_3_hint=f"{drawers} × {per_drawer} = {total_screws} screws.",
        diagram_spec=diag,
    )


def _gen_asm_diag_directional_arrows_action_interpretation(r: random.Random) -> Dict[str, Any]:
    arrow_scenario = r.choice([
        (
            "a curved circular arrow looping clockwise around a cam lock fitting",
            "Turn the cam lock clockwise (usually 90° to 180°) using a screwdriver to lock the connecting bolt firmly in place.",
            "Loosen and completely remove the cam lock from the panel hole.",
            "Hammer the cam lock down into the wooden panel until flush.",
            "Rotate the entire furniture panel 360° on the floor."
        ),
        (
            "a straight bold arrow pointing downwards with a small click icon next to it",
            "Press or push the shelf downward firmly until the plastic locking pins snap or click into the side holes.",
            "Pull the shelf upward to detach it from the side walls.",
            "Screw the shelf directly into the wall using an electric drill.",
            "Slide the shelf outwards horizontally to extend it."
        ),
        (
            "two parallel opposing arrows pointing towards each other across a seam",
            "Push the two wooden panels tightly together to close the joint without leaving a gap.",
            "Pull the two panels apart to insert additional glue.",
            "Measure the distance between the two panels with a ruler.",
            "Cut along the line between the two panels using a handsaw."
        ),
    ])
    arrow_desc, correct_meaning, d1, d2, d3 = arrow_scenario

    prompt = (
        f"In a flat-pack wardrobe assembly manual, Step 3 displays {arrow_desc}.\n\n"
        f"What action does this specific symbol instruct the builder to perform?"
    )
    ans = correct_meaning
    opts = [correct_meaning, d1, d2, d3]

    s1 = f"Interpret standardized pictorial technical drawing symbols used in flat-pack assembly manuals."
    s2 = f"✓ [1 Mark: Method – Identifying action represented by symbol]\nThe visual symbol represents the physical action required on the hardware component."
    s3 = f"✓ [1 Mark: Accuracy – Correct symbol interpretation]\nInstruction: {correct_meaning}"

    return _build_question_payload(
        "asm_diag_directional_arrows_action_interpretation",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Read the visual description: {arrow_desc}.",
        tier_2_hint="Standard assembly diagrams use curved arrows for rotational turning/locking and straight arrows for pressing/sliding.",
        tier_3_hint=f"The correct instruction is: {correct_meaning}",
    )


def _gen_asm_diag_warning_symbols_safety_precautions(r: random.Random) -> Dict[str, Any]:
    scenario = r.choice([
        (
            "an illustration of an electric power drill with a prominent red diagonal cross (X) over it",
            "Do not use an electric screwdriver or power drill, as high torque can strip the pre-drilled pilot holes or crack the particle board.",
            "The furniture requires electricity to function.",
            "The product must be assembled in complete darkness.",
            "Only an electrician is licensed to assemble this furniture."
        ),
        (
            "an illustration of a tall bookcase tipping forward onto a child, with an anchor strap attached to the wall",
            "The furniture must be anchored to the wall with the safety strap to prevent accidental tip-over and severe injury.",
            "The bookcase must be laid flat on the floor at all times.",
            "Children under 5 years old are prohibited from entering the room.",
            "The bookcase can only be moved while fully loaded with heavy books."
        ),
        (
            "an illustration of two human figures lifting a panel together",
            "This component or assembly step requires a minimum of two persons to lift safely to avoid injury or damage.",
            "The furniture is designed to seat two persons simultaneously.",
            "The product can only be purchased by two registered customers.",
            "Both persons must use matching screwdrivers at the same time."
        ),
    ])
    icon_desc, correct_meaning, d1, d2, d3 = scenario

    prompt = (
        f"On page 1 of an imported flat-pack tall bookcase manual, a safety warning icon depicts {icon_desc}.\n\n"
        f"What is the primary safety reason for including this warning?"
    )
    ans = correct_meaning
    opts = [correct_meaning, d1, d2, d3]

    s1 = f"Understand safety icons, health precautions, and structural failure prevention in furniture assembly."
    s2 = f"✓ [1 Mark: Method – Identifying technical rationale behind safety warning]\nManufacturers provide safety notices to prevent structural failure or physical injury."
    s3 = f"✓ [1 Mark: Accuracy – Correct explanation]\nSafety meaning: {correct_meaning}"

    return _build_question_payload(
        "asm_diag_warning_symbols_safety_precautions",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Consider what physical risk the manufacturer is trying to prevent.",
        tier_2_hint="Think about product safety, torque damage to manufactured wood, or balance/weight risks.",
        tier_3_hint=f"The correct reason is: {correct_meaning}",
    )


def _gen_asm_diag_cell_phone_sim_battery_installation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    diag = {
        "kind": "inline_svg",
        "title": f"Mobile Phone Component Installation Diagram ({name})",
        "svg": (
            '<svg viewBox="0 0 340 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">'
            '<rect width="340" height="180" fill="#f8fafc" stroke="#cbd5e1" rx="8"/>'
            '<text x="20" y="25" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">SIM &amp; Battery Alignment Diagram</text>'
            '<rect x="40" y="40" width="110" height="120" rx="6" fill="#e2e8f0" stroke="#64748b"/>'
            '<text x="95" y="105" text-anchor="middle" font-size="12" font-weight="bold" fill="#334155">Battery Bay</text>'
            '<rect x="180" y="55" width="80" height="95" rx="4" fill="#fef08a" stroke="#ca8a04"/>'
            '<polygon points="240,55 260,75 260,150 180,150 180,55" fill="#fef9c3" stroke="#ca8a04"/>'
            '<text x="220" y="105" text-anchor="middle" font-size="11" font-weight="bold" fill="#854d0e">SIM Card</text>'
            '<text x="220" y="125" text-anchor="middle" font-size="9" fill="#a16207">Gold Contacts</text>'
            '</svg>'
        ),
    }
    prompt = (
        f"{name} purchases a new feature mobile phone that requires manual installation of the SIM card and removable battery. "
        f"Refer to the accompanying component orientation diagram.\n\n"
        f"Why must the SIM card be installed with the metallic gold contacts facing downwards into the socket?"
    )
    ans = "To ensure physical electrical contact between the SIM chip and the phone's internal circuit board terminals."
    opts = [
        "To ensure physical electrical contact between the SIM chip and the phone's internal circuit board terminals.",
        "To protect the gold plate from overheating when the screen illuminates.",
        "To make sure the phone antenna can pick up FM radio frequencies.",
        "To prevent the battery from touching the phone case.",
    ]

    s1 = f"Electrical devices require conductive terminals to make physical contact for circuit completion and data communication."
    s2 = f"✓ [1 Mark: Method – Understanding electrical contact requirements in mobile hardware]\nThe SIM card contains microscopic integrated circuits connected to the exterior gold pads. These must touch the spring pins in the chassis."
    s3 = f"✓ [1 Mark: Accuracy – Correct technical reason]\nReason: To ensure physical electrical contact between the SIM chip and the phone's internal circuit board terminals."

    return _build_question_payload(
        "asm_diag_cell_phone_sim_battery_installation",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What purpose do the gold plates on a SIM card serve?",
        tier_2_hint="Gold is a conductor that carries electrical signals between the chip and phone board.",
        tier_3_hint="Physical contact with the phone's internal pins is necessary to read subscriber data.",
        diagram_spec=diag,
    )


def _gen_asm_diag_flatpack_wardrobe_hinge_and_runner_mounting(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} is mounting the metal slide runners for 3 drawers inside a flat-pack wardrobe carcass.\n\n"
        f"The instruction manual shows a close-up diagram of the cabinet runner rail. The rail has a small plastic wheel (roller) at one end.\n\n"
        f"In which direction should the runner rail with the roller wheel be oriented when screwed to the inside side-panel of the wardrobe?"
    )
    ans = "The roller wheel must face towards the front opening of the wardrobe at the bottom of the rail."
    opts = [
        "The roller wheel must face towards the front opening of the wardrobe at the bottom of the rail.",
        "The roller wheel must face towards the solid backboard of the wardrobe.",
        "The roller wheel must point vertically towards the ceiling.",
        "The roller wheel must face the exterior outside wall of the wardrobe.",
    ]

    s1 = f"Mechanical drawer runners rely on the cabinet roller situated at the front opening to support the mating drawer track rolling in and out."
    s2 = f"✓ [1 Mark: Method – Kinematic orientation of drawer slide mechanism]\nThe cabinet track wheel stays stationary at the front aperture while the drawer box roller rides along the rail towards the back."
    s3 = f"✓ [1 Mark: Accuracy – Correct orientation]\nCorrect orientation: The roller wheel must face towards the front opening of the wardrobe at the bottom of the rail."

    return _build_question_payload(
        "asm_diag_flatpack_wardrobe_hinge_and_runner_mounting",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Think about how a drawer slides out of the cabinet towards you.",
        tier_2_hint="The stationary cabinet wheel must be at the front opening where the drawer enters.",
        tier_3_hint="The roller wheel must face towards the front opening of the wardrobe.",
    )


def _gen_asm_diag_modular_shelving_unit_tier_spacing(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_inner_height_cm = r.choice([160, 180, 200, 210])
    shelf_count = r.choice([3, 4, 5])  # internal shelves creating (shelf_count + 1) compartments
    shelf_thickness_cm = r.choice([1.5, 2.0, 2.5])
    compartments = shelf_count + 1

    total_shelf_thickness = shelf_count * shelf_thickness_cm
    available_space = total_inner_height_cm - total_shelf_thickness
    spacing_cm = round(available_space / compartments, 1)

    prompt = (
        f"{name} is assembling a tall bookcase with an internal vertical frame height of {total_inner_height_cm} cm.\n\n"
        f"The unit includes {shelf_count} adjustable internal shelves. Each shelf is {_fmt(shelf_thickness_cm)} cm thick.\n"
        f"If {name} positions all {shelf_count} shelves so that the {compartments} open shelf compartments have "
        f"equal vertical clearance height, calculate the height of each compartment (in cm)."
    )
    ans = f"{_fmt(spacing_cm)} cm"

    s1 = f"Deduct total thickness of all {shelf_count} shelves from internal frame height ({total_inner_height_cm} cm), then divide by {compartments} equal compartments."
    s2 = f"✓ [1 Mark: Method – Deducting shelf thickness and dividing by compartment count]\nTotal shelf thickness = {shelf_count} × {_fmt(shelf_thickness_cm)} cm = {_fmt(total_shelf_thickness)} cm.\nAvailable opening space = {total_inner_height_cm} cm − {_fmt(total_shelf_thickness)} cm = {_fmt(available_space)} cm.\nCompartment height = {_fmt(available_space)} ÷ {compartments}."
    s3 = f"✓ [1 Mark: Accuracy – Height of each compartment]\nHeight = {_fmt(spacing_cm)} cm."

    return _build_question_payload(
        "asm_diag_modular_shelving_unit_tier_spacing",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"How many open compartments do {shelf_count} shelves create? ({shelf_count} + 1 = {compartments}).",
        tier_2_hint=f"Subtract total shelf thickness ({shelf_count} × {_fmt(shelf_thickness_cm)} = {_fmt(total_shelf_thickness)} cm) from {total_inner_height_cm} cm.",
        tier_3_hint=f"{_fmt(available_space)} ÷ {compartments} = {_fmt(spacing_cm)} cm.",
    )

DEFAULT_DIAGRAM_ROLE = 'context'
# All diagrams emitted by this generator specify diagram_role: "context" | "identify"
