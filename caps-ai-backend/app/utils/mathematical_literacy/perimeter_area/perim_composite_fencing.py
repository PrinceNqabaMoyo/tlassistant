"""Cluster 2: Composite Perimeters & Practical Boundary Applications (Subskills 10 to 18)."""
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

# --------------------------------------------------------------------------- #
# Subskill 10: L-Shaped Floor Perimeter
# --------------------------------------------------------------------------- #
def _gen_perim_l_shaped_floor_perimeter(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_l_shaped_floor_perimeter"
    name = r.choice(SA_NAMES)
    total_l = r.choice([10, 12, 14, 15, 16])
    total_w = r.choice([8, 9, 10, 12])
    cut_l = r.choice([3, 4, 5])
    cut_w = r.choice([2, 3, 4])
    # For an L-shape, the outer perimeter equals 2*(total_l + total_w)
    perimeter = 2 * (total_l + total_w)
    correct_ans = f"{perimeter} m"

    prompt = (
        f"{name} is measuring the perimeter of an L-shaped room.\n"
        f"The maximum length is {total_l} m and the maximum width is {total_w} m.\n"
        f"The cut-out indentation has dimensions {cut_l} m by {cut_w} m.\n\n"
        f"Calculate the total perimeter around the outer boundary of this L-shaped room."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"For any orthogonal L-shaped polygon, the sum of the horizontal edges equals $2 \\times \\text{{total length}}$, "
        f"and the sum of the vertical edges equals $2 \\times \\text{{total width}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Perimeter}} = 2 \\times (\\text{{length}} + \\text{{width}})$$\n"
        f"$$\\text{{Perimeter}} = 2 \\times ({total_l} + {total_w}) = 2 \\times {total_l + total_w}$$ ✓ [1 Mark: Method – recognizing opposing parallel edge conservation]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Perimeter}} = {perimeter}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – accurate perimeter calculation]"
    )

    d1 = f"{perimeter - cut_l - cut_w} m"
    d2 = f"{perimeter + cut_l + cut_w} m"
    d3 = f"{total_l * total_w} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Notice that the inner cutout sides equal the missing outer length and width.",
        tier_2=f"The total perimeter of this orthogonal L-shape is 2 × ({total_l} + {total_w}).",
        tier_3=f"2 × {total_l + total_w} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 11: U-Shaped Courtyard Perimeter
# --------------------------------------------------------------------------- #
def _gen_perim_u_shaped_courtyard_perimeter(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_u_shaped_courtyard_perimeter"
    name = r.choice(SA_NAMES)
    outer_l = r.choice([16, 18, 20, 22])
    outer_w = r.choice([10, 12, 14])
    indent_l = r.choice([6, 8])
    indent_w = r.choice([4, 5, 6])
    # Outer rectangle perimeter + 2 * indent_w
    perimeter = 2 * outer_l + 2 * outer_w + 2 * indent_w
    correct_ans = f"{perimeter} m"

    prompt = (
        f"{name} is installing edging around a U-shaped paved courtyard.\n"
        f"The overall outer length is {outer_l} m and outer width is {outer_w} m.\n"
        f"The courtyard has a central rectangular garden cutout measuring {indent_l} m long by {indent_w} m deep that opens to one side.\n\n"
        f"Calculate the total perimeter of the paved courtyard boundary."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The U-shaped boundary includes all outer edges plus the two internal sidewalls of the courtyard indentation.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Outer perimeter base}} = 2({outer_l} + {outer_w}) = {2 * (outer_l + outer_w)}\\text{{ m}}$$\n"
        f"$$\\text{{Additional indentation sides}} = 2 \\times {indent_w} = {2 * indent_w}\\text{{ m}}$$\n"
        f"$$\\text{{Total Perimeter}} = {2 * (outer_l + outer_w)} + {2 * indent_w}$$ ✓ [1 Mark: Method – adding outer perimeter and internal indent edges]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Perimeter}} = {perimeter}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – correct final sum]"
    )

    d1 = f"{2 * (outer_l + outer_w)} m"
    d2 = f"{perimeter - indent_w} m"
    d3 = f"{perimeter + 4} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Account for all outer sides plus the inward-facing sidewalls of the cutout.",
        tier_2=f"Sum 2 × ({outer_l} + {outer_w}) + 2 × {indent_w}.",
        tier_3=f"Total perimeter = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 12: Rectangle with Semicircular End
# --------------------------------------------------------------------------- #
def _gen_perim_rectangle_with_semicircular_end(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_rectangle_with_semicircular_end"
    name = r.choice(SA_NAMES)
    length = r.choice([10, 12, 14, 15, 18])
    width = r.choice([6, 8, 10])  # width is diameter
    radius = width / 2
    pi_val = 3.142
    semicircle_arc = round(pi_val * radius, 2)
    # Boundary: 2 lengths + 1 width + 1 semicircle arc (internal shared line NOT counted!)
    perimeter = round(2 * length + width + semicircle_arc, 2)
    correct_ans = f"{_fmt(perimeter)} m"

    prompt = (
        f"{name} is installing a perimeter garden wall around a patio shaped as a rectangle with a semicircular bay extension at one end.\n"
        f"The straight rectangular part is {length} m long and {width} m wide. The semicircular bay is attached across the {width} m end.\n"
        f"(Note: The internal boundary between the rectangle and the bay does NOT have a wall).\n\n"
        f"Calculate the total perimeter of the outer wall. (Use $\\pi = 3,142$ and round to 2 decimal places).\n\n"
        f"**Formula**: $\\text{{Perimeter}} = 2l + w + (\\pi \\times r)$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The outer wall consists of three straight edges (2 lengths of {length} m, 1 width of {width} m) "
        f"and the curved semicircular arc ($\\pi \\times r$, where $r = \\frac{{{width}}}{{2}} = {radius}\\text{{ m}}$). The interior shared line is excluded.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Curved arc}} = \\pi \\times r = 3,142 \\times {radius} = {_fmt(semicircle_arc)}\\text{{ m}}$$\n"
        f"$$\\text{{Straight edges}} = (2 \\times {length}) + {width} = {2 * length + width}\\text{{ m}}$$\n"
        f"$$\\text{{Total Perimeter}} = {2 * length + width} + {_fmt(semicircle_arc)}$$ ✓ [1 Mark: Method – summing 3 straight sides and curved arc]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Perimeter}} = {_fmt(perimeter)}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – correct sum with units]"
    )

    d1 = f"{_fmt(round(2 * length + 2 * width + semicircle_arc, 2))} m"  # included interior width
    d2 = f"{_fmt(round(2 * length + 2 * width, 2))} m"
    d3 = f"{_fmt(round(perimeter - 3, 2))} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Exclude the internal divider line from the perimeter.",
        tier_2=f"Add 2 × {length} + {width} + (3,142 × {radius}).",
        tier_3=f"Total perimeter = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 13: Running Track Perimeter (Two Semicircles)
# --------------------------------------------------------------------------- #
def _gen_perim_running_track_two_semicircles(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_running_track_two_semicircles"
    name = r.choice(SA_NAMES)
    straight = r.choice([80, 84, 90, 100])
    diameter = r.choice([40, 50, 60, 64])
    pi_val = 3.142
    circ = round(pi_val * diameter, 2)
    total_lap = round(2 * straight + circ, 2)
    correct_ans = f"{_fmt(total_lap)} m"

    prompt = (
        f"{name} is marking out an athletics running track at a high school.\n"
        f"The track consists of two straight sections, each {straight} m long, and two semicircular ends with diameter {diameter} m.\n\n"
        f"Calculate the total perimeter of one complete lap around the inside edge of the track.\n"
        f"(Use $\\pi = 3,142$, round to 2 decimal places).\n\n"
        f"**Formula**: $\\text{{Perimeter}} = (2 \\times \\text{{straight}}) + (\\pi \\times d)$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Two semicircles of the same diameter combine to make one full circle of circumference $C = \\pi \\times d$.\n"
        f"Adding the two straights gives the total lap distance.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Two straights}} = 2 \\times {straight} = {2 * straight}\\text{{ m}}$$\n"
        f"$$\\text{{Two semicircular ends}} = \\pi \\times d = 3,142 \\times {diameter} = {_fmt(circ)}\\text{{ m}}$$\n"
        f"$$\\text{{Total lap}} = {2 * straight} + {_fmt(circ)}$$ ✓ [1 Mark: Method – summing two straights and full circumference]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total lap}} = {_fmt(total_lap)}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – correct evaluation with units]"
    )

    d1 = f"{_fmt(round(straight + circ, 2))} m"
    d2 = f"{_fmt(round(2 * straight + 2 * circ, 2))} m"
    d3 = f"{_fmt(round(total_lap + 10, 2))} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The two semicircular ends together equal one complete circle.",
        tier_2=f"Calculate (2 × {straight}) + (3,142 × {diameter}).",
        tier_3=f"Total distance = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 14: Garden Fencing Deducting Gate
# --------------------------------------------------------------------------- #
def _gen_perim_garden_fencing_deducting_gate(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_garden_fencing_deducting_gate"
    name = r.choice(SA_NAMES)
    length = r.choice([15, 18, 20, 24, 25, 30])
    width = r.choice([10, 12, 14, 15, 16])
    gate_w = r.choice([1.0, 1.2, 1.5, 2.0])
    full_p = 2 * (length + width)
    fence_len = round(full_p - gate_w, 2)
    correct_ans = f"{_fmt(fence_len)} m"

    prompt = (
        f"{name} is fencing a rectangular vegetable garden measuring {length} m long by {width} m wide.\n"
        f"A gate of width {_fmt(gate_w)} m will be installed on one side, where no fencing is required.\n\n"
        f"Calculate the total length of fencing wire mesh needed."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The total garden perimeter is $2(l + w)$. Subtract the gate opening where no fence is erected.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total Perimeter}} = 2 \\times ({length} + {width}) = {full_p}\\text{{ m}}$$\n"
        f"$$\\text{{Fencing required}} = {full_p} - {_fmt(gate_w)}$$ ✓ [1 Mark: Method – calculating perimeter and deducting gate opening]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Fencing required}} = {_fmt(fence_len)}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – accurate subtraction with units]"
    )

    d1 = f"{full_p} m"  # forgot to deduct gate
    d2 = f"{_fmt(round(full_p + gate_w, 2))} m"
    d3 = f"{length * width} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the full perimeter of the rectangle first.",
        tier_2=f"Deduct the gate width {_fmt(gate_w)} m from {full_p} m.",
        tier_3=f"Fencing = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 15: Multiple Strands Barbed Wire
# --------------------------------------------------------------------------- #
def _gen_perim_fencing_multiple_strands_barbed_wire(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_fencing_multiple_strands_barbed_wire"
    name = r.choice(SA_NAMES)
    length = r.choice([40, 50, 60, 80, 100])
    width = r.choice([25, 30, 40, 50])
    strands = r.choice([3, 4, 5, 6])
    perimeter = 2 * (length + width)
    total_wire = perimeter * strands
    correct_ans = f"{_fmt(total_wire)} m"

    prompt = (
        f"{name} is fencing a rectangular livestock paddock measuring {length} m by {width} m.\n"
        f"The fence will have {strands} horizontal strands of barbed wire running completely around the boundary.\n\n"
        f"Calculate the total length of barbed wire required."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Each strand circles the entire paddock perimeter. The total wire needed is the single-strand perimeter multiplied by the number of strands.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Perimeter}} = 2 \\times ({length} + {width}) = {perimeter}\\text{{ m}}$$\n"
        f"$$\\text{{Total wire}} = {perimeter} \\times {strands}$$ ✓ [1 Mark: Method – multiplying perimeter by number of strands]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total wire}} = {_fmt(total_wire)}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – accurate product with units]"
    )

    d1 = f"{perimeter} m"  # single strand
    d2 = f"{_fmt(total_wire + perimeter)} m"
    d3 = f"{_fmt(length * width)} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the perimeter for 1 strand: 2(l + w).",
        tier_2=f"Multiply the perimeter ({perimeter} m) by {strands} strands.",
        tier_3=f"{perimeter} × {strands} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 16: Fence Posts Interval Spacing
# --------------------------------------------------------------------------- #
def _gen_perim_fencing_posts_interval_spacing(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_fencing_posts_interval_spacing"
    name = r.choice(SA_NAMES)
    length = r.choice([20, 25, 30, 40])
    width = r.choice([10, 15, 20])
    spacing = r.choice([2, 5])  # ensures integer divisions
    perimeter = 2 * (length + width)
    posts = perimeter // spacing
    correct_ans = f"{posts} posts"

    prompt = (
        f"{name} is erecting a perimeter fence around the rectangular plot shown in the diagram ({length} m by {width} m).\n"
        f"Posts are installed at equal {spacing} m intervals on the closed boundary loop.\n\n"
        f"Calculate the total number of fence posts required."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"For any closed boundary loop, the number of posts equals the total perimeter divided by the spacing interval between posts.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Perimeter}} = 2 \\times ({length} + {width}) = {perimeter}\\text{{ m}}$$\n"
        f"$$\\text{{Number of posts}} = \\frac{{{perimeter}}}{{{spacing}}}$$ ✓ [1 Mark: Method – dividing total perimeter by spacing interval]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Number of posts}} = {posts}\\text{{ posts}}$$ ✓ [1 Mark: Accuracy – correct integer count of posts]"
    )

    d1 = f"{posts + 1} posts"  # open line off-by-one trap
    d2 = f"{posts - 1} posts"
    d3 = f"{perimeter} posts"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "length": length,
        "width": width,
        "shape": "rectangle",
        "title": f"Rectangular Fencing Plot ({length} m × {width} m, Spacing {spacing} m)",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="For a closed perimeter loop, Number of posts = Perimeter ÷ Spacing.",
        tier_2=f"Calculate {perimeter} m ÷ {spacing} m.",
        tier_3=f"{perimeter} ÷ {spacing} = {correct_ans}.",
        r=r,
        diagram_spec=d_spec,
    )

# --------------------------------------------------------------------------- #
# Subskill 17: Skirting Boards Deducting Doorways
# --------------------------------------------------------------------------- #
def _gen_perim_skirting_boards_deducting_doorways(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_skirting_boards_deducting_doorways"
    name = r.choice(SA_NAMES)
    length = r.choice([5, 6, 7, 8])
    width = r.choice([4, 5, 6])
    doorways = r.choice([1, 2])
    door_w = 0.9  # standard SA door 900 mm = 0.9 m
    full_p = 2 * (length + width)
    skirting = round(full_p - (doorways * door_w), 2)
    correct_ans = f"{_fmt(skirting)} m"

    prompt = (
        f"{name} is installing skirting boards around the base of the walls in a rectangular bedroom.\n"
        f"The room is {length} m long and {width} m wide.\n"
        f"There {'is 1 door opening' if doorways == 1 else 'are 2 door openings'}, each 0,9 m wide, where no skirting board is installed.\n\n"
        f"Calculate the total length of skirting board required."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Skirting boards run along the perimeter of the room at floor level, but are omitted across door openings.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Room Perimeter}} = 2 \\times ({length} + {width}) = {full_p}\\text{{ m}}$$\n"
        f"$$\\text{{Door deductions}} = {doorways} \\times 0,9\\text{{ m}} = {_fmt(doorways * door_w)}\\text{{ m}}$$\n"
        f"$$\\text{{Skirting length}} = {full_p} - {_fmt(doorways * door_w)}$$ ✓ [1 Mark: Method – subtracting doorway openings from room perimeter]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Skirting length}} = {_fmt(skirting)}\\text{{ m}}$$ ✓ [1 Mark: Accuracy – accurate subtraction with units]"
    )

    d1 = f"{full_p} m"
    d2 = f"{_fmt(round(full_p - 0.9, 2))} m" if doorways == 2 else f"{_fmt(round(full_p - 1.8, 2))} m"
    d3 = f"{length * width} m"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate room perimeter 2(l + w).",
        tier_2=f"Deduct {_fmt(doorways * door_w)} m for the door opening(s).",
        tier_3=f"Skirting = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 18: Picture Frame Border Perimeter
# --------------------------------------------------------------------------- #
def _gen_perim_picture_frame_border_perimeter(r: random.Random) -> Dict[str, Any]:
    sub_id = "perim_picture_frame_border_perimeter"
    name = r.choice(SA_NAMES)
    pic_l = r.choice([40, 50, 60, 70])  # cm
    pic_w = r.choice([30, 40, 50])
    border = r.choice([5, 8, 10])  # cm on each side
    outer_l = pic_l + 2 * border
    outer_w = pic_w + 2 * border
    outer_p = 2 * (outer_l + outer_w)
    correct_ans = f"{outer_p} cm"

    prompt = (
        f"{name} is framing a photograph that is {pic_l} cm long and {pic_w} cm wide.\n"
        f"A wooden frame of uniform width {border} cm surrounds the photograph on all four sides.\n\n"
        f"Calculate the outer perimeter of the wooden frame."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A border adds to both the top and bottom (width), and to both the left and right (length).\n"
        f"Outer length = $\\text{{photo length}} + 2 \\times \\text{{border}}$;\n"
        f"Outer width = $\\text{{photo width}} + 2 \\times \\text{{border}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Outer length}} = {pic_l} + 2({border}) = {outer_l}\\text{{ cm}}$$\n"
        f"$$\\text{{Outer width}} = {pic_w} + 2({border}) = {outer_w}\\text{{ cm}}$$\n"
        f"$$\\text{{Outer perimeter}} = 2 \\times ({outer_l} + {outer_w}) = 2 \\times {outer_l + outer_w}$$ ✓ [1 Mark: Method – adding border to both ends and applying perimeter formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Outer perimeter}} = {outer_p}\\text{{ cm}}$$ ✓ [1 Mark: Accuracy – accurate perimeter with units]"
    )

    d1 = f"{2 * (pic_l + pic_w)} cm"  # inner perimeter
    d2 = f"{outer_p - 2 * border} cm"  # only added border once
    d3 = f"{outer_p + 20} cm"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "length": outer_l,
        "width": outer_w,
        "shape": "concentric_rectangles",
        "title": f"Picture Frame ({outer_l} cm × {outer_w} cm with {border} cm Border)",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember the frame adds border width to BOTH sides: Length + 2(border).",
        tier_2=f"Outer length = {outer_l} cm, outer width = {outer_w} cm.",
        tier_3=f"Perimeter = 2 × ({outer_l} + {outer_w}) = {correct_ans}.",
        r=r,
        diagram_spec=d_spec,
    )
