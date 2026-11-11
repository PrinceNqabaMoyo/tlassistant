"""Cluster 4: Composite Areas & Cutouts (Subskills 28 to 36)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)

# --------------------------------------------------------------------------- #
# Subskill 28: L-Shaped Composite Area
# --------------------------------------------------------------------------- #
def _gen_area_composite_l_shape_split_rectangles(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_composite_l_shape_split_rectangles"
    name = r.choice(SA_NAMES)
    l1 = r.choice([6, 8, 10])
    w1 = r.choice([4, 5, 6])
    l2 = r.choice([4, 5, 6])
    w2 = r.choice([3, 4])
    a1 = l1 * w1
    a2 = l2 * w2
    total_area = a1 + a2
    correct_ans = f"{total_area} m²"

    prompt = (
        f"{name} is calculating the floor area of an L-shaped open-plan lounge and dining area.\n"
        f"The layout is divided into two non-overlapping rectangular sections:\n"
        f"  • Section A (Lounge): {l1} m long by {w1} m wide\n"
        f"  • Section B (Dining): {l2} m long by {w2} m wide\n\n"
        f"Calculate the total combined floor area of the L-shaped room."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"An L-shaped polygon can be split into two simpler rectangles. The total area is the sum of both individual areas: $A = A_1 + A_2$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Area of Section A}} = {l1} \\times {w1} = {a1}\\text{{ m}}^2$$\n"
        f"$$\\text{{Area of Section B}} = {l2} \\times {w2} = {a2}\\text{{ m}}^2$$\n"
        f"$$\\text{{Total Area}} = {a1} + {a2}$$ ✓ [1 Mark: Method – splitting into two rectangles and summing]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Area}} = {total_area}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate total area with units]"
    )

    d1 = f"{2 * (l1 + w1 + l2 + w2)} m²"
    d2 = f"{total_area - w2} m²"
    d3 = f"{total_area + l1} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "length": l1 + l2,
        "width": max(w1, w2),
        "shape": "l_shape",
        "title": f"L-Shaped Room Layout ({l1} m × {w1} m and {l2} m × {w2} m)",
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the area of each rectangle separately: l × w.",
        tier_2=f"Section A = {a1} m², Section B = {a2} m².",
        tier_3=f"Total area = {a1} + {a2} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 29: T-Shaped Composite Area
# --------------------------------------------------------------------------- #
def _gen_area_composite_t_shape_layout(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_composite_t_shape_layout"
    name = r.choice(SA_NAMES)
    top_l = r.choice([12, 14, 16])
    top_w = r.choice([3, 4])
    stem_l = r.choice([6, 8, 10])
    stem_w = r.choice([4, 5])
    a_top = top_l * top_w
    a_stem = stem_l * stem_w
    total_area = a_top + a_stem
    correct_ans = f"{total_area} m²"

    prompt = (
        f"{name} is tiling a T-shaped hallway consisting of a top horizontal corridor and a vertical stem corridor.\n"
        f"  • Top Corridor: {top_l} m long by {top_w} m wide\n"
        f"  • Stem Corridor: {stem_l} m long by {stem_w} m wide\n\n"
        f"Calculate the total area of the T-shaped hallway in m²."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Decompose the T-shape into its two distinct rectangular components (top crossbar and vertical stem).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Area of Top Corridor}} = {top_l} \\times {top_w} = {a_top}\\text{{ m}}^2$$\n"
        f"$$\\text{{Area of Stem Corridor}} = {stem_l} \\times {stem_w} = {a_stem}\\text{{ m}}^2$$\n"
        f"$$\\text{{Total Area}} = {a_top} + {a_stem}$$ ✓ [1 Mark: Method – calculating both rectangular areas and adding]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Area}} = {total_area}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate sum]"
    )

    d1 = f"{top_l * stem_l} m²"
    d2 = f"{total_area - 10} m²"
    d3 = f"{total_area + top_w} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the area of the top corridor and stem corridor separately.",
        tier_2=f"Top = {top_l} × {top_w} = {a_top} m². Stem = {stem_l} × {stem_w} = {a_stem} m².",
        tier_3=f"Total area = {a_top} + {a_stem} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 30: Rectangle Plus Semicircle Patio
# --------------------------------------------------------------------------- #
def _gen_area_rectangle_plus_semicircle_patio(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_rectangle_plus_semicircle_patio"
    name = r.choice(SA_NAMES)
    rect_l = r.choice([8, 10, 12])
    rect_w = r.choice([6, 8])  # diameter of semicircle
    radius = rect_w / 2
    pi_val = 3.142
    rect_area = rect_l * rect_w
    semi_area = round(0.5 * pi_val * (radius ** 2), 2)
    total_area = round(rect_area + semi_area, 2)
    correct_ans = f"{_fmt(total_area)} m²"

    prompt = (
        f"{name} is planning to pave a rectangular entertainment area with an attached semicircular patio at one end.\n"
        f"The rectangular section is {rect_l} m long by {rect_w} m wide. The semicircular patio attaches across the {rect_w} m side.\n\n"
        f"Calculate the total surface area to be paved. (Use $\\pi = 3,142$, round to 2 decimal places).\n\n"
        f"**Formulas**: $\\text{{Area of rectangle}} = l \\times w$ and $\\text{{Area of semicircle}} = \\frac{{1}}{{2}} \\pi r^2$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The combined area is the area of the rectangle plus the area of the attached semicircle.\n"
        f"Radius of semicircle = $\\frac{{{rect_w}}}{{2}} = {_fmt(radius)}\\text{{ m}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Area of rectangle}} = {rect_l} \\times {rect_w} = {rect_area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Area of semicircle}} = 0,5 \\times 3,142 \\times ({_fmt(radius)})^2 = {_fmt(semi_area)}\\text{{ m}}^2$$\n"
        f"$$\\text{{Total Area}} = {rect_area} + {_fmt(semi_area)}$$ ✓ [1 Mark: Method – adding rectangle area and semicircle area]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Area}} = {_fmt(total_area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate combined area]"
    )

    d1 = f"{_fmt(round(rect_area + 2 * semi_area, 2))} m²"  # added full circle
    d2 = f"{rect_area} m²"  # forgot patio
    d3 = f"{_fmt(round(total_area + 4, 2))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the area of the rectangle and the area of the semicircle.",
        tier_2=f"Rectangle = {rect_area} m², Semicircle = 0,5 × 3,142 × ({_fmt(radius)})² = {_fmt(semi_area)} m².",
        tier_3=f"Total area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 31: Rectangle Plus Triangular Gable Wall
# --------------------------------------------------------------------------- #
def _gen_area_rectangle_plus_triangle_gable(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_rectangle_plus_triangle_gable"
    name = r.choice(SA_NAMES)
    width = r.choice([6, 8, 10, 12])  # building base
    wall_h = r.choice([3, 4])  # rectangular wall height
    roof_h = r.choice([2, 3])  # triangular peak height
    rect_a = width * wall_h
    tri_a = round(0.5 * width * roof_h, 1)
    total_area = round(rect_a + tri_a, 1)
    correct_ans = f"{_fmt(total_area)} m²"

    prompt = (
        f"{name} is calculating the exterior wall area of the gable end of a house to buy plaster.\n"
        f"The wall consists of a rectangular base measuring {width} m wide by {wall_h} m high, "
        f"topped by a triangular gable with the same base width of {width} m and a peak height of {roof_h} m.\n\n"
        f"Calculate the total area of the gable wall in m²."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Total area is the sum of the rectangular wall base ($l \\times w$) and the triangular gable roof section ($\\frac{{1}}{{2}} b \\times h$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Rectangular area}} = {width} \\times {wall_h} = {rect_a}\\text{{ m}}^2$$\n"
        f"$$\\text{{Triangular gable area}} = 0,5 \\times {width} \\times {roof_h} = {_fmt(tri_a)}\\text{{ m}}^2$$\n"
        f"$$\\text{{Total Area}} = {rect_a} + {_fmt(tri_a)}$$ ✓ [1 Mark: Method – summing rectangular and triangular portions]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Area}} = {_fmt(total_area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate sum with units]"
    )

    d1 = f"{_fmt(rect_a + width * roof_h)} m²"  # forgot 1/2 for triangle
    d2 = f"{rect_a} m²"
    d3 = f"{_fmt(total_area + 5)} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Split into a rectangle at the bottom and a triangle at the top.",
        tier_2=f"Rectangle = {rect_a} m², Triangle = 0,5 × {width} × {roof_h} = {_fmt(tri_a)} m².",
        tier_3=f"Total area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 32: Lawn Minus Swimming Pool Cutout
# --------------------------------------------------------------------------- #
def _gen_area_cutout_lawn_minus_swimming_pool(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_cutout_lawn_minus_swimming_pool"
    name = r.choice(SA_NAMES)
    yard_l = r.choice([20, 24, 25, 30])
    yard_w = r.choice([15, 18, 20])
    pool_l = r.choice([8, 10])
    pool_w = r.choice([4, 5])
    yard_area = yard_l * yard_w
    pool_area = pool_l * pool_w
    lawn_area = yard_area - pool_area
    correct_ans = f"{lawn_area} m²"

    prompt = (
        f"{name}'s back garden measures {yard_l} m long by {yard_w} m wide.\n"
        f"A rectangular swimming pool measuring {pool_l} m by {pool_w} m is situated in the centre of the garden.\n"
        f"The rest of the garden is planted with lawn.\n\n"
        f"Calculate the area of the lawn."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"When an object is inside another shape, subtract the inner cutout area from the total enclosing area: $A_{{lawn}} = A_{{total}} - A_{{pool}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total garden area}} = {yard_l} \\times {yard_w} = {yard_area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Pool area}} = {pool_l} \\times {pool_w} = {pool_area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Lawn area}} = {yard_area} - {pool_area}$$ ✓ [1 Mark: Method – subtracting cutout area from total area]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Lawn area}} = {lawn_area}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate subtraction with units]"
    )

    d1 = f"{yard_area + pool_area} m²"  # added instead of subtracted
    d2 = f"{yard_area} m²"
    d3 = f"{lawn_area - 20} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the pool area from the total garden area.",
        tier_2=f"Total = {yard_area} m², Pool = {pool_area} m².",
        tier_3=f"Lawn = {yard_area} - {pool_area} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 33: Patio Minus Circular Pond Cutout
# --------------------------------------------------------------------------- #
def _gen_area_cutout_patio_minus_circular_pond(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_cutout_patio_minus_circular_pond"
    name = r.choice(SA_NAMES)
    patio_l = r.choice([10, 12, 14, 15])
    patio_w = r.choice([8, 10])
    pond_radius = r.choice([2, 3])
    pi_val = 3.142
    patio_area = patio_l * patio_w
    pond_area = round(pi_val * (pond_radius ** 2), 2)
    paved_area = round(patio_area - pond_area, 2)
    correct_ans = f"{_fmt(paved_area)} m²"

    prompt = (
        f"{name} is paving a rectangular patio measuring {patio_l} m by {patio_w} m.\n"
        f"In the middle of the patio is a circular fish pond with a radius of {pond_radius} m, which will not be paved.\n\n"
        f"Calculate the actual area to be paved. (Use $\\pi = 3,142$ and round to 2 decimal places)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The paved area is the rectangular patio area minus the circular pond area: $A_{{paved}} = (l \\times w) - (\\pi r^2)$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Patio area}} = {patio_l} \\times {patio_w} = {patio_area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Pond area}} = 3,142 \\times {pond_radius}^2 = 3,142 \\times {pond_radius * pond_radius} = {_fmt(pond_area)}\\text{{ m}}^2$$\n"
        f"$$\\text{{Paved area}} = {patio_area} - {_fmt(pond_area)}$$ ✓ [1 Mark: Method – subtracting circle area from rectangle area]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Paved area}} = {_fmt(paved_area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate subtraction to 2 d.p.]"
    )

    d1 = f"{patio_area} m²"
    d2 = f"{_fmt(round(patio_area + pond_area, 2))} m²"
    d3 = f"{_fmt(round(paved_area - 5, 2))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the circular pond area from the rectangular patio area.",
        tier_2=f"Patio = {patio_area} m², Pond = 3,142 × {pond_radius}² = {_fmt(pond_area)} m².",
        tier_3=f"Paved area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 34: Room Wall Area Minus Doors and Windows
# --------------------------------------------------------------------------- #
def _gen_area_cutout_wall_minus_doors_and_windows(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_cutout_wall_minus_doors_and_windows"
    name = r.choice(SA_NAMES)
    length = r.choice([5, 6, 7])
    height = 2.8  # standard ceiling height
    door_w, door_h = 0.9, 2.0  # door = 1.8 m²
    win_w, win_h = 1.5, 1.2    # window = 1.8 m²
    door_area = round(door_w * door_h, 2)
    win_area = round(win_w * win_h, 2)
    wall_gross = round(length * height, 2)
    wall_net = round(wall_gross - door_area - win_area, 2)
    correct_ans = f"{_fmt(wall_net)} m²"

    prompt = (
        f"{name} is tiling one feature wall in a dining room.\n"
        f"The wall is {length} m long and {_fmt(height)} m high.\n"
        f"The wall contains:\n"
        f"  • 1 door opening measuring {_fmt(door_w)} m by {_fmt(door_h)} m\n"
        f"  • 1 window opening measuring {_fmt(win_w)} m by {_fmt(win_h)} m\n\n"
        f"Calculate the net wall surface area that requires tiling (excluding door and window openings)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate the gross area of the wall ($l \\times h$) and subtract the cutouts for the door and window.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Gross wall area}} = {length} \\times {_fmt(height)} = {_fmt(wall_gross)}\\text{{ m}}^2$$\n"
        f"$$\\text{{Door area}} = {_fmt(door_w)} \\times {_fmt(door_h)} = {_fmt(door_area)}\\text{{ m}}^2$$\n"
        f"$$\\text{{Window area}} = {_fmt(win_w)} \\times {_fmt(win_h)} = {_fmt(win_area)}\\text{{ m}}^2$$\n"
        f"$$\\text{{Net wall area}} = {_fmt(wall_gross)} - {_fmt(door_area)} - {_fmt(win_area)}$$ ✓ [1 Mark: Method – subtracting openings from gross wall area]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net wall area}} = {_fmt(wall_net)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate subtraction to 2 d.p.]"
    )

    d1 = f"{_fmt(wall_gross)} m²"  # forgot to deduct
    d2 = f"{_fmt(round(wall_gross - door_area, 2))} m²"  # only deducted door
    d3 = f"{_fmt(round(wall_net + 2, 2))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "length": length,
        "height": height,
        "shape": "wall_with_openings",
        "title": f"Feature Wall Cutout ({length} m × {_fmt(height)} m)",
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate gross wall area, then subtract door area and window area.",
        tier_2=f"Gross = {_fmt(wall_gross)} m², Door = {_fmt(door_area)} m², Window = {_fmt(win_area)} m².",
        tier_3=f"Net area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 35: Circular Ring / Washer / Annulus
# --------------------------------------------------------------------------- #
def _gen_area_cutout_washer_ring_annulus(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_cutout_washer_ring_annulus"
    name = r.choice(SA_NAMES)
    outer_r = r.choice([5, 6, 7, 8, 10])
    inner_r = r.choice([2, 3, 4])
    pi_val = 3.142
    outer_a = pi_val * (outer_r ** 2)
    inner_a = pi_val * (inner_r ** 2)
    ring_area = round(outer_a - inner_a, 2)
    correct_ans = f"{_fmt(ring_area)} m²"

    prompt = (
        f"{name} is installing a paved circular pathway around a circular grass lawn.\n"
        f"The inner radius of the pathway (the edge of the grass lawn) is $r = {inner_r}$ m.\n"
        f"The outer radius of the pathway is $R = {outer_r}$ m.\n\n"
        f"Calculate the area of the circular paved pathway. (Use $\\pi = 3,142$ and round to 2 decimal places).\n\n"
        f"**Formula**: $\\text{{Area of ring}} = \\pi \\times (R^2 - r^2)$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The ring (annulus) area is the difference between the outer circular area and the inner circular area: $A = \\pi R^2 - \\pi r^2$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$R^2 - r^2 = {outer_r}^2 - {inner_r}^2 = {outer_r * outer_r} - {inner_r * inner_r} = {outer_r * outer_r - inner_r * inner_r}$$\n"
        f"$$\\text{{Area}} = 3,142 \\times ({outer_r * outer_r - inner_r * inner_r})$$ ✓ [1 Mark: Method – applying annulus area formula]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Area}} = {_fmt(ring_area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate product to 2 d.p.]"
    )

    d1 = f"{_fmt(round(outer_a, 2))} m²"
    d2 = f"{_fmt(round(pi_val * ((outer_r - inner_r) ** 2), 2))} m²"  # classic error π(R-r)²
    d3 = f"{_fmt(round(ring_area + 10, 2))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the inner circle area from the outer circle area: π(R² - r²).",
        tier_2=f"R² - r² = {outer_r}² - {inner_r}² = {outer_r * outer_r - inner_r * inner_r}. Multiply by 3,142.",
        tier_3=f"Ring area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 36: Percentage of Property Occupied
# --------------------------------------------------------------------------- #
def _gen_area_percentage_of_property_occupied(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_percentage_of_property_occupied"
    name = r.choice(SA_NAMES)
    prop_l = r.choice([25, 30, 40, 50])
    prop_w = r.choice([20, 25, 30])
    total_prop = prop_l * prop_w
    bldg_area = r.choice([150, 180, 200, 240, 300])
    pct = round((bldg_area / total_prop) * 100, 1)
    correct_ans = f"{_fmt(pct)}%"

    prompt = (
        f"{name}'s suburban property measures {prop_l} m by {prop_w} m.\n"
        f"The main house and outbuildings occupy a combined footprint area of {bldg_area} m².\n\n"
        f"Calculate the percentage of the total property area occupied by the buildings.\n"
        f"Round your answer to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First find the total property area ($l \\times w$). Then calculate what fraction the buildings represent and multiply by 100%.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total Property Area}} = {prop_l} \\times {prop_w} = {total_prop}\\text{{ m}}^2$$\n"
        f"$$\\text{{Percentage occupied}} = \\frac{{{bldg_area}}}{{{total_prop}}} \\times 100\\%$$ ✓ [1 Mark: Method – dividing building area by total property area and multiplying by 100]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Percentage occupied}} = {_fmt(pct)}\\%$$ ✓ [1 Mark: Accuracy – accurate percentage rounded to 1 d.p.]"
    )

    d1 = f"{_fmt(round(pct * 1.5, 1))}%"
    d2 = f"{_fmt(round(100 - pct, 1))}%"  # unoccupied percentage
    d3 = f"{_fmt(round(pct / 2, 1))}%"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find total property area: length × width.",
        tier_2=f"Calculate ({bldg_area} ÷ {total_prop}) × 100.",
        tier_3=f"Percentage = {correct_ans}.",
        r=r,
    )
