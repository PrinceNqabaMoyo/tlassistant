"""Subskills 37 to 44: 2D Nets, Folding, Opposite Faces & 3D Packaging Models for Grade 11 Mathematical Literacy."""
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


def generate_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Identify 3D geometric solid from its unfolded 2D net."""
    solid_info = r.choice([
        ("Rectangular Prism (Carton Box)", "6 rectangular faces arranged in a cruciform or t-shape where opposite pairs have equal dimensions"),
        ("Cylinder", "one central rectangular body panel and two identical circular discs attached at opposite edges"),
        ("Triangular Prism", "two identical triangular end faces and three rectangular connecting side faces"),
        ("Square-based Pyramid", "one central square base with four identical triangular faces attached to its four edges"),
    ])
    solid_name, net_desc = solid_info

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "2d_net",
        "title": f"2D Net of a {solid_name}",
        "description": net_desc,
        "solid": solid_name,
    }

    prompt = (
        f"A packaging company uses a 2D cardboard cutout (net) consisting of {net_desc}.\n"
        f"When this net is folded along all crease lines, which 3-dimensional geometric solid is formed?"
    )

    correct_ans = solid_name
    all_solids = [
        "Rectangular Prism (Carton Box)",
        "Cylinder",
        "Triangular Prism",
        "Square-based Pyramid",
        "Cone",
        "Hexagonal Prism",
    ]
    distractors = [s for s in all_solids if s != solid_name][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Inspect the 2D net components [1 mark].\n"
        f"The net comprises {net_desc}.\n"
        f"Step 2: Trace folding into 3D space [1 mark].\n"
        f"Folding the faces along their connecting seams forms a {solid_name}.\n"
        f"Step 3: Stated solid [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="37",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Count the number and shapes of faces in the net to determine which 3D solid they create.",
        tier_2=f"The description ({net_desc}) matches a {solid_name}.",
        tier_3=f"Answer: {solid_name}.",
        r=r,
        diagram_spec=diagram_spec,
    )


def generate_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: Identify opposite faces on a 2D net of a cube or rectangular carton."""
    # Standard t-net or cross net with faces A, B, C, D, E, F
    # In a standard row: A - B - C - D, with E above B and F below B
    # Opposite pairs in A-B-C-D with E, F:
    # A is opposite C; B is opposite D; E is opposite F.
    pairs = [
        ("A", "C", "they are separated by one intervening face (B) along the horizontal strip"),
        ("B", "D", "they are separated by one intervening face (C) along the horizontal strip"),
        ("E", "F", "they are on opposite wings attached to face B, folding upward and downward respectively"),
    ]
    face_1, face_2, reason = r.choice(pairs)

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "cube_net",
        "title": "Unfolded Cube Net with Lettered Faces",
        "layout": {
            "row_2": ["E"],
            "row_3": ["A", "B", "C", "D"],
            "row_4": ["F"],
        },
        "highlight_face": face_1,
    }

    prompt = (
        f"Refer to the standard 2D cube net shown below:\n\n"
        f"```\n"
        f"      [ E ]\n"
        f"[ A ][ B ][ C ][ D ]\n"
        f"      [ F ]\n"
        f"```\n\n"
        f"When this net is folded to form a closed cube, which face will be directly opposite Face {face_1}?"
    )

    correct_ans = f"Face {face_2}"
    distractors = [f"Face {f}" for f in ["A", "B", "C", "D", "E", "F"] if f not in (face_1, face_2)][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Apply opposite-face folding rule for nets [1 mark].\n"
        f"Along any straight strip of squares, opposite faces are always separated by exactly one intervening face.\n"
        f"Step 2: Trace Face {face_1} [1 mark].\n"
        f"{reason}.\n"
        f"Step 3: Stated opposite face [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="38",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="In a strip of squares on a cube net, faces separated by one square fold up to become opposite faces.",
        tier_2=f"Find the face separated from {face_1} by one square or on the opposite wing.",
        tier_3=f"Face {face_1} is directly opposite Face {face_2}.",
        r=r,
        diagram_spec=diagram_spec,
    )


def generate_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Determine edge matching when folding a net into a 3D box."""
    name = r.choice(SA_NAMES)

    prompt = (
        f"When folding an open-top rectangular cardboard box from a flat 2D net with a central base and four upright flaps, "
        f"the side edge of the North flap must join with which edge to form a rigid 90° corner?"
    )

    correct_ans = "The adjacent top edge of the East or West flap"
    wrong_1 = "The bottom edge of the South flap"
    wrong_2 = "The center line of the base panel"
    wrong_3 = "The exterior diagonal corner of the opposite wall"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Visualize corner formation in a 3D net [1 mark].\n"
        f"Each of the 4 vertical corners of the box is formed where two perpendicular side flaps meet.\n"
        f"Step 2: Identify meeting edges [1 mark].\n"
        f"The side edge of the North flap meets the adjacent side edge of the perpendicular East (or West) flap.\n"
        f"Step 3: Conclusion [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="39",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="When side flaps fold up at 90°, their adjacent vertical edges come together to form corners.",
        tier_2="The edge of the North flap meets the edge of the adjacent East/West flap.",
        tier_3=f"Correct join: {correct_ans}.",
        r=r,
    )


def generate_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: Calculate total cardboard area for a box net including glue flaps."""
    name = r.choice(SA_NAMES)
    box_l = r.choice([20, 25, 30, 35])
    box_w = r.choice([15, 20, 25])
    box_h = r.choice([10, 12, 15])

    # Surface area of 6 faces: 2*(L*W + L*H + W*H) in cm²
    sa_faces = 2 * (box_l * box_w + box_l * box_h + box_w * box_h)
    flap_percentage = r.choice([5, 8, 10])
    total_cardboard = round(sa_faces * (1 + flap_percentage / 100), 1)

    prompt = (
        f"A factory manufactures cereal boxes measuring {_fmt(box_l)} cm long, {_fmt(box_w)} cm wide, "
        f"and {_fmt(box_h)} cm high. "
        f"The 2D die-cut net requires an additional {flap_percentage}% of cardboard area for glue tabs and sealing flaps.\n"
        f"Calculate the total area of cardboard (in cm²) required to produce one cereal box net."
    )

    correct_ans = f"{_fmt(total_cardboard)} cm²"
    wrong_1 = f"{_fmt(sa_faces)} cm²"  # forgot flaps
    wrong_2 = f"{_fmt(sa_faces * (1 + flap_percentage / 10))} cm²"
    wrong_3 = f"{_fmt(total_cardboard * 0.5)} cm²"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate surface area of the 6 faces [1 mark].\n"
        f"SA = 2 × (L × W + L × H + W × H) = 2 × ({box_l * box_w} + {box_l * box_h} + {box_w * box_h}) = {_fmt(sa_faces)} cm².\n"
        f"Step 2: Add {flap_percentage}% for glue tabs and flaps [1 mark].\n"
        f"Total Area = {_fmt(sa_faces)} × (1 + {flap_percentage / 100}) = {_fmt(sa_faces)} × {1 + flap_percentage / 100} = {_fmt(total_cardboard)} cm².\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="40",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the surface area of the 6 faces 2(LW + LH + WH) then add the flap percentage.",
        tier_2=f"Net face area = {_fmt(sa_faces)} cm². Add {flap_percentage}%: multiply by {1 + flap_percentage / 100}.",
        tier_3=f"Total cardboard required = {_fmt(total_cardboard)} cm².",
        r=r,
    )


def generate_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Identify invalid net that cannot fold into a closed cube."""
    prompt = (
        f"Which of the following flat arrangements of 6 identical squares CANNOT be folded into a closed cube?"
    )

    correct_ans = "A 2 × 3 solid grid of 6 squares (two rows of 3 squares touching along their long edges)"
    wrong_1 = "A 'T-shaped' net with 4 squares in a vertical column and 2 arms extending left and right from row 2"
    wrong_2 = "A 'Cruciform' (cross) net with 4 squares in a horizontal row and one square above and below the second square"
    wrong_3 = "A 'Step-like' (zigzag) net of 6 squares with 3 pairs of offset adjacent squares"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Recall valid cube net rules [1 mark].\n"
        f"A cube has 11 distinct valid nets. A net cannot contain any 2 × 2 block of 4 squares.\n"
        f"Step 2: Analyze the 2 × 3 grid [1 mark].\n"
        f"A 2 × 3 grid contains multiple 2 × 2 squares; when folded, adjacent faces fold directly onto each other, overlapping and leaving openings.\n"
        f"Step 3: Conclusion [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="41",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="A valid cube net can never contain a solid 2 × 2 block of four squares.",
        tier_2="A 2 × 3 grid contains 2 × 2 blocks which cause faces to overlap when folded.",
        tier_3=f"The invalid net is: {correct_ans}.",
        r=r,
    )


def generate_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Subskill 42: Cylinder net rectangular body dimensions calculation."""
    name = r.choice(SA_NAMES)
    cyl_h = r.choice([10, 12, 14, 15, 18, 20])
    cyl_radius = r.choice([3.5, 4.0, 5.0, 7.0])
    pi_val = 3.1416

    # Circumference = 2 * pi * r
    circ = round(2 * pi_val * cyl_radius, 2)

    prompt = (
        f"{name} is creating the 2D cardboard net for a cylindrical tin of height {_fmt(cyl_h)} cm "
        f"and base radius {_fmt(cyl_radius)} cm (use π ≈ 3,1416).\n"
        f"The net consists of two circular end discs and a rectangular curved body panel. "
        f"What are the dimensions (length and width) of the rectangular body panel?"
    )

    correct_ans = f"{_fmt(circ)} cm by {_fmt(cyl_h)} cm"
    wrong_1 = f"{_fmt(round(pi_val * cyl_radius, 2))} cm by {_fmt(cyl_h)} cm"
    wrong_2 = f"{_fmt(cyl_radius * 2)} cm by {_fmt(cyl_h)} cm"
    wrong_3 = f"{_fmt(circ * 2)} cm by {_fmt(cyl_h)} cm"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand cylinder net geometry [1 mark].\n"
        f"The width of the rectangle equals the height of the cylinder ({_fmt(cyl_h)} cm).\n"
        f"The length of the rectangle wraps completely around the circular base, so it equals the circumference.\n"
        f"Step 2: Calculate circumference [1 mark].\n"
        f"Length = 2 × π × r = 2 × 3,1416 × {_fmt(cyl_radius)} cm = {_fmt(circ)} cm.\n"
        f"Step 3: Stated dimensions [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "cylinder_net",
        "title": f"Cylinder 2D Net (Radius {_fmt(cyl_radius)} cm, Height {_fmt(cyl_h)} cm)",
        "radius": cyl_radius,
        "height": cyl_h,
        "length": circ,
        "width": cyl_h,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="42",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The length of the rectangle must equal the circumference of the circular base: 2πr.",
        tier_2=f"Calculate 2 × 3,1416 × {_fmt(cyl_radius)} cm = {_fmt(circ)} cm. The width equals the cylinder height ({_fmt(cyl_h)} cm).",
        tier_3=f"Dimensions: {_fmt(circ)} cm by {_fmt(cyl_h)} cm.",
        r=r,
    )


def generate_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Subskill 43: Open-top box made by cutting identical corner squares from a sheet."""
    name = r.choice(SA_NAMES)
    sheet_l = r.choice([30, 40, 50])
    sheet_w = r.choice([20, 25, 30])
    corner_cut = r.choice([3, 4, 5])

    base_l = sheet_l - 2 * corner_cut
    base_w = sheet_w - 2 * corner_cut
    base_area = base_l * base_w

    prompt = (
        f"{name} makes an open-top organizing tray from a flat rectangular sheet of cardboard measuring "
        f"{_fmt(sheet_l)} cm by {_fmt(sheet_w)} cm by cutting out a square of {_fmt(corner_cut)} cm by "
        f"{_fmt(corner_cut)} cm from each of the four corners, then folding up the sides.\n"
        f"Calculate the dimensions (length and width) and area of the resulting base of the tray."
    )

    correct_ans = f"{_fmt(base_l)} cm by {_fmt(base_w)} cm (Base Area = {_fmt(base_area)} cm²)"
    wrong_1 = f"{_fmt(sheet_l - corner_cut)} cm by {_fmt(sheet_w - corner_cut)} cm (Base Area = {(sheet_l - corner_cut) * (sheet_w - corner_cut)} cm²)"
    wrong_2 = f"{_fmt(base_l)} cm by {_fmt(base_w)} cm (Base Area = {_fmt(base_area * 10)} cm²)"
    wrong_3 = f"{_fmt(base_l - 2)} cm by {_fmt(base_w - 2)} cm (Base Area = {(base_l - 2) * (base_w - 2)} cm²)"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Subtract corner cutouts from both ends of length and width [1 mark].\n"
        f"Base Length = {_fmt(sheet_l)} - (2 × {_fmt(corner_cut)}) = {_fmt(sheet_l)} - {_fmt(2 * corner_cut)} = {_fmt(base_l)} cm.\n"
        f"Base Width = {_fmt(sheet_w)} - (2 × {_fmt(corner_cut)}) = {_fmt(sheet_w)} - {_fmt(2 * corner_cut)} = {_fmt(base_w)} cm.\n"
        f"Step 2: Calculate base area [1 mark].\n"
        f"Base Area = {_fmt(base_l)} cm × {_fmt(base_w)} cm = {_fmt(base_area)} cm².\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="43",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Because a corner is cut from both sides, subtract 2 × cut size from each dimension.",
        tier_2=f"Length = {_fmt(sheet_l)} - 2({corner_cut}) = {_fmt(base_l)} cm; Width = {_fmt(sheet_w)} - 2({corner_cut}) = {_fmt(base_w)} cm.",
        tier_3=f"Base area = {_fmt(base_l)} × {_fmt(base_w)} = {_fmt(base_area)} cm².",
        r=r,
    )


def generate_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Volume of folded container from dimensions of its net."""
    name = r.choice(SA_NAMES)
    l_cm = r.choice([15, 20, 25, 30])
    w_cm = r.choice([10, 12, 15])
    h_cm = r.choice([8, 10, 12])

    vol_cm3 = l_cm * w_cm * h_cm
    vol_litres = round(vol_cm3 / 1000, 2)

    prompt = (
        f"A gift box folded from a 2D net has internal base dimensions of {_fmt(l_cm)} cm length, "
        f"{_fmt(w_cm)} cm width, and a folded height of {_fmt(h_cm)} cm.\n"
        f"Calculate the internal volume (capacity) of this container in litres (1 litre = 1 000 cm³)."
    )

    correct_ans = f"{_fmt(vol_litres)} litres"
    wrong_1 = f"{_fmt(vol_litres * 10)} litres"
    wrong_2 = f"{_fmt(vol_litres * 0.1)} litres"
    wrong_3 = f"{_fmt(vol_cm3)} litres"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate volume in cm³ [1 mark].\n"
        f"Volume = Length × Width × Height = {_fmt(l_cm)} cm × {_fmt(w_cm)} cm × {_fmt(h_cm)} cm = {_fmt(vol_cm3)} cm³.\n"
        f"Step 2: Convert cm³ to litres (divide by 1 000) [1 mark].\n"
        f"Volume in litres = {_fmt(vol_cm3)} ÷ 1 000 = {_fmt(vol_litres)} litres.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="44",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Volume = L × W × H. Divide cm³ by 1 000 to convert to litres.",
        tier_2=f"{_fmt(l_cm)} × {_fmt(w_cm)} × {_fmt(h_cm)} = {_fmt(vol_cm3)} cm³.",
        tier_3=f"{_fmt(vol_cm3)} ÷ 1 000 = {_fmt(vol_litres)} litres.",
        r=r,
    )
