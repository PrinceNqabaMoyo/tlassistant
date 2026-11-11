"""Subskills 25-32: Architectural Floor Plans, Symbols & SANS Compliance for Grade 12 Plans & Scale."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def gen_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Subskill 25: Decoding standard architectural door symbols."""
    door_symbols = [
        {"symbol": "A straight line hinged at a wall opening with a 90° dashed or solid circular arc", "type": "Single hinged inward-swinging door"},
        {"symbol": "Two opposing straight lines with symmetrical quarter-circle swing arcs meeting in the center", "type": "Double hinged French doors"},
        {"symbol": "A solid line parallel to the wall disappearing into a hollow pocket inside the wall cavity", "type": "Cavity sliding pocket door"},
        {"symbol": "A zig-zag accordion-style folding line across a wide opening", "type": "Multi-leaf bi-fold stacking door"},
    ]
    target = r.choice(door_symbols)

    prompt = (
        f"On a standard architectural floor plan drawn to SANS specifications, a doorway is represented by:\n"
        f"'{target['symbol']}'.\n\n"
        f"What type of door does this symbol indicate, and what does the curved arc signify?"
    )

    correct_ans = f"{target['type']} (the arc indicates the swing path and space clearance required to open the door)"
    custom_opts = [
        correct_ans,
        f"{target['type']} (the arc represents an overhead arched brick lintel)",
        "A permanent load-bearing reinforced concrete shear wall with no doorway opening",
        "A roll-up steel security shutter installed for commercial retail stores",
    ]

    t1 = "Look at the components of the symbol: straight door leaf and curved trajectory."
    t2 = "The circular arc illustrates the path taken by the door edge as it swings open."
    t3 = f"The symbol represents a {target['type']} with the arc showing the required floor clearance."

    explanation = [
        f"Step 1: Identify the graphic convention: door leaf line + circular trajectory [1 Mark: Method].",
        f"Step 2: Match to standard architectural door taxonomy [1 Mark: Method].",
        f"Step 3: State door type and explain that the arc represents swing clearance [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_25",
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


def gen_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Subskill 26: Decoding window symbols, sill lines, and curtain wall notation."""
    prompt = (
        "On a 2D floor plan, a window opening in a 220 mm exterior brick wall is depicted by:\n"
        "  - A break in the thick wall lines\n"
        "  - Three or four thin parallel lines running through the gap\n"
        "  - A thin line extending slightly outward beyond the exterior wall face\n\n"
        "What do the thin central lines and the outer projecting line represent?"
    )

    correct_ans = "The central thin lines represent the glass window pane(s) and frame; the outer projecting line represents the exterior sloping window sill for rainwater runoff"
    custom_opts = [
        correct_ans,
        "The central lines represent steel security burglar bars; the outer line represents a flower box",
        "The central lines represent curtain tracks; the outer line represents an outdoor solar patio umbrella",
        "The central lines represent electrical wiring conduit; the outer line represents an emergency fire exit ladder",
    ]

    t1 = "Consider how walls, glass, and sills are drafted in architectural cross-sections."
    t2 = "Thick lines represent cut brickwork; thin parallel lines represent glazed panes; the external projection is the window sill."
    t3 = "The central lines are the glass pane and frame; the projecting line is the exterior weather sill."

    explanation = [
        f"Step 1: Identify standard drafting conventions for masonry openings [1 Mark: Method].",
        f"Step 2: Recognize thin parallel lines as glazed window sashes [1 Mark: Method].",
        f"Step 3: State the exact functions of the glass frame and external weathering sill [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_26",
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


def gen_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Subskill 27: Decoding sanitary fittings on bathroom and kitchen plans."""
    fittings = [
        {"icon": "An oval nested inside a rectangle with a small circle at one end", "item": "Built-in enamel bathtub (circle indicates the waste drain outlet)"},
        {"icon": "A circle or elongated bowl attached to a rectangular tank against the wall", "item": "Water closet (toilet) with rear cistern"},
        {"icon": "A square with diagonal cross-lines meeting at a central circle", "item": "Walk-in shower cubicle (cross lines indicate sloped floor screed to central drain)"},
        {"icon": "A rounded basin with two small circles and a central overflow hole", "item": "Wash hand basin with hot/cold tap outlets"},
    ]
    target = r.choice(fittings)

    prompt = (
        f"In an architectural floor plan for a residential bathroom, a sanitary fixture is depicted as:\n"
        f"'{target['icon']}'.\n\n"
        f"Identify this plumbing fixture and explain its specific detailing."
    )

    correct_ans = target["item"]
    custom_opts = [
        correct_ans,
        "Under-floor central heating boiler unit",
        "Domestic automated washing machine and tumble dryer unit",
        "Built-in linen cupboard shelving unit",
    ]

    t1 = "Read the visual description of the fixture geometry."
    t2 = "Match the geometric shapes to standard bathroom plumbing fixtures."
    t3 = f"The fixture is a {target['item']}."

    explanation = [
        f"Step 1: Examine the geometry of the plumbing symbol [1 Mark: Method].",
        f"Step 2: Correlate features (cistern, drain, tap holes, sloped floor) to standard sanitary fittings [1 Mark: Method].",
        f"Step 3: State the fixture identity: {target['item']} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_27",
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


def gen_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Subskill 28: Wall thickness deduction: internal room dimensions from external plan dimensions."""
    # Standard external brick wall in SA: 220 mm (double brick)
    # External length = 5 000 mm, external width = 4 000 mm
    ext_l_mm = r.choice([4800, 5000, 5400, 6000])
    ext_w_mm = r.choice([3600, 4000, 4200])
    wall_thickness_mm = 220

    # Internal dimensions = external - 2 * wall_thickness
    int_l_mm = ext_l_mm - (2 * wall_thickness_mm)
    int_w_mm = ext_w_mm - (2 * wall_thickness_mm)
    int_l_m = int_l_mm / 1000.0
    int_w_m = int_w_mm / 1000.0

    prompt = (
        f"An architectural floor plan shows a single-room outbuilding with EXTERNAL wall dimensions of "
        f"{ext_l_mm} mm long by {ext_w_mm} mm wide.\n"
        f"All exterior walls are constructed from standard double-brick masonry with a finished wall thickness of 220 mm.\n\n"
        f"Calculate the INTERNAL living dimensions of the room (Length × Width) in metres (m)."
    )

    correct_ans = f"{_fmt(int_l_m, 2)} m × {_fmt(int_w_m, 2)} m"
    custom_opts = [
        correct_ans,
        f"{_fmt((ext_l_mm - wall_thickness_mm) / 1000.0, 2)} m × {_fmt((ext_w_mm - wall_thickness_mm) / 1000.0, 2)} m",
        f"{_fmt(ext_l_mm / 1000.0, 2)} m × {_fmt(ext_w_mm / 1000.0, 2)} m",
        f"{_fmt((int_l_mm - 200) / 1000.0, 2)} m × {_fmt((int_w_mm - 200) / 1000.0, 2)} m",
    ]

    t1 = "Remember that walls exist on BOTH sides of the room (2 walls along length, 2 walls along width)."
    t2 = f"Total wall deduction = 2 × 220 mm = 440 mm for each axis."
    t3 = f"Internal length = {ext_l_mm} - 440 = {int_l_mm} mm = {_fmt(int_l_m, 2)} m. Internal width = {ext_w_mm} - 440 = {int_w_mm} mm = {_fmt(int_w_m, 2)} m."

    explanation = [
        f"Step 1: Calculate total wall deduction per dimension: 2 × 220 mm = 440 mm [1 Mark: Method].",
        f"Step 2: Internal length = {ext_l_mm} mm - 440 mm = {int_l_mm} mm = {_fmt(int_l_m, 2)} m [1 Mark: Method].",
        f"Step 3: Internal width = {ext_w_mm} mm - 440 mm = {int_w_mm} mm = {_fmt(int_w_m, 2)} m → {_fmt(int_l_m, 2)} m × {_fmt(int_w_m, 2)} m [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_28",
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


def gen_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Subskill 29: Calculating net internal room floor area excluding internal partition walls."""
    # L-shaped room or two rooms: Bedroom 1 (3.5 m x 3.2 m) + Bedroom 2 (3.0 m x 2.8 m)
    l1 = r.choice([3.2, 3.5, 4.0])
    w1 = r.choice([3.0, 3.2, 3.5])
    l2 = r.choice([2.8, 3.0, 3.2])
    w2 = r.choice([2.4, 2.6, 2.8])

    area1 = l1 * w1
    area2 = l2 * w2
    total_net_area = area1 + area2

    prompt = (
        f"Refer to the two-bedroom floor plan shown in the diagram. Bedroom 1 has dimensions of {_fmt(l1, 1)} m by {_fmt(w1, 1)} m, "
        f"and Bedroom 2 has dimensions of {_fmt(l2, 1)} m by {_fmt(w2, 1)} m.\n\n"
        f"Calculate the TOTAL net usable floor area of the two bedrooms combined, in square metres (m²)."
    )
    d_spec_29 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Two-Bedroom Floor Plan ({_fmt(l1, 1)} m × {_fmt(w1, 1)} m)",
        "rooms": [{"name": "Bedroom 1", "length": l1, "width": w1}, {"name": "Bedroom 2", "length": l2, "width": w2}],
    }

    correct_ans = f"{_fmt(total_net_area, 2)} m²"
    custom_opts = [
        correct_ans,
        f"{_fmt(area1, 2)} m²",
        f"{_fmt(total_net_area * 1.2, 2)} m²",
        f"{_fmt((l1 + l2) * (w1 + w2), 2)} m²",
    ]

    t1 = f"Calculate the area of Bedroom 1: {_fmt(l1, 1)} m × {_fmt(w1, 1)} m."
    t2 = f"Calculate the area of Bedroom 2: {_fmt(l2, 1)} m × {_fmt(w2, 1)} m."
    t3 = f"Total area = {_fmt(area1, 2)} m² + {_fmt(area2, 2)} m² = {_fmt(total_net_area, 2)} m²."

    explanation = [
        f"Step 1: Bedroom 1 area = {_fmt(l1, 1)} × {_fmt(w1, 1)} = {_fmt(area1, 2)} m² [1 Mark: Method].",
        f"Step 2: Bedroom 2 area = {_fmt(l2, 1)} × {_fmt(w2, 1)} = {_fmt(area2, 2)} m² [1 Mark: Method].",
        f"Step 3: Combined net floor area = {_fmt(area1, 2)} + {_fmt(area2, 2)} = {_fmt(total_net_area, 2)} m² [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_29",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_29,
    )


def gen_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Subskill 30: Measuring window glazing area to check natural lighting compliance (SANS 10400-XA: min 10%)."""
    # SANS 10400-O & XA: Total window glass area must be at least 10% of floor area
    floor_l_m = r.choice([4.0, 4.5, 5.0])
    floor_w_m = r.choice([3.0, 3.5, 4.0])
    floor_area_m2 = floor_l_m * floor_w_m
    min_glazing_req_m2 = floor_area_m2 * 0.10  # 10%

    window_w_m = r.choice([1.2, 1.5, 1.8])
    window_h_m = r.choice([1.0, 1.2])
    actual_glazing_m2 = window_w_m * window_h_m

    compliant = actual_glazing_m2 >= min_glazing_req_m2
    status = (
        f"Compliant: actual glazing area is {_fmt(actual_glazing_m2, 2)} m² (≥ {_fmt(min_glazing_req_m2, 2)} m² required 10% minimum)"
        if compliant
        else f"Non-compliant: actual glazing area is {_fmt(actual_glazing_m2, 2)} m² (< {_fmt(min_glazing_req_m2, 2)} m² required 10% minimum)"
    )

    prompt = (
        f"According to South African National Building Regulations (SANS 10400 Part O), any habitable room "
        f"must have natural window lighting with a total glazed area equal to AT LEAST 10% of the room's floor area.\n"
        f"A bedroom has internal floor dimensions of {_fmt(floor_l_m, 1)} m long by {_fmt(floor_w_m, 1)} m wide.\n"
        f"The bedroom window has glazed dimensions of {_fmt(window_w_m, 1)} m wide by {_fmt(window_h_m, 1)} m high.\n\n"
        f"Does this window meet the mandatory 10% SANS natural lighting requirement? Show your calculations."
    )

    correct_ans = status
    custom_opts = [
        correct_ans,
        f"Compliant: all bedroom windows over 1,0 m² automatically comply with building regulations",
        f"Non-compliant: regulations require at least 25% of the floor area in glass",
        f"Compliant: {_fmt(actual_glazing_m2, 2)} m² is equal to 50% of the room's floor area",
    ]

    t1 = f"Calculate room floor area: {_fmt(floor_l_m, 1)} × {_fmt(floor_w_m, 1)} = {_fmt(floor_area_m2, 2)} m²."
    t2 = f"Calculate the 10% minimum requirement: {_fmt(floor_area_m2, 2)} × 0,10 = {_fmt(min_glazing_req_m2, 2)} m²."
    t3 = f"Calculate actual window area: {_fmt(window_w_m, 1)} × {_fmt(window_h_m, 1)} = {_fmt(actual_glazing_m2, 2)} m². Compare to {_fmt(min_glazing_req_m2, 2)} m²."

    explanation = [
        f"Step 1: Calculate room floor area = {_fmt(floor_l_m, 1)} × {_fmt(floor_w_m, 1)} = {_fmt(floor_area_m2, 2)} m² [1 Mark: Method].",
        f"Step 2: Minimum 10% glazing required = {_fmt(floor_area_m2, 2)} m² × 0,10 = {_fmt(min_glazing_req_m2, 2)} m² [1 Mark: Method].",
        f"Step 3: Actual window area = {_fmt(window_w_m, 1)} × {_fmt(window_h_m, 1)} = {_fmt(actual_glazing_m2, 2)} m² → {status} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_30",
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


def gen_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Subskill 31: Measuring openable window area to check natural ventilation compliance (SANS 10400: min 5%)."""
    # SANS 10400: Openable window area must be at least 5% of floor area
    floor_area_m2 = r.choice([12.0, 15.0, 18.0, 20.0])
    min_vent_m2 = floor_area_m2 * 0.05  # 5%

    openable_w_m = r.choice([0.6, 0.8, 0.9])
    openable_h_m = r.choice([0.8, 1.0, 1.2])
    actual_vent_m2 = openable_w_m * openable_h_m

    compliant = actual_vent_m2 >= min_vent_m2
    status = (
        f"Compliant: openable sash area is {_fmt(actual_vent_m2, 2)} m² (≥ {_fmt(min_vent_m2, 2)} m² required 5% minimum)"
        if compliant
        else f"Non-compliant: openable sash area is {_fmt(actual_vent_m2, 2)} m² (< {_fmt(min_vent_m2, 2)} m² required 5% minimum)"
    )

    prompt = (
        f"Under SANS 10400 (Part O), habitable rooms must provide openable window sashes for natural ventilation "
        f"equal to AT LEAST 5% of the room's total floor area.\n"
        f"A lounge has a total floor area of {_fmt(floor_area_m2, 1)} m².\n"
        f"Its window has an openable opening sash measuring {_fmt(openable_w_m, 1)} m wide by {_fmt(openable_h_m, 1)} m high.\n\n"
        f"Determine whether this openable sash satisfies the mandatory 5% ventilation requirement."
    )

    correct_ans = status
    custom_opts = [
        correct_ans,
        f"Compliant: all domestic windows in South Africa automatically provide 10% ventilation",
        f"Non-compliant: regulations require 50% of the room's floor area to be openable to the sky",
        f"Compliant: {_fmt(actual_vent_m2, 2)} m² is equal to 15% of the floor area",
    ]

    t1 = f"Calculate the 5% requirement: {_fmt(floor_area_m2, 1)} m² × 0,05 = {_fmt(min_vent_m2, 2)} m²."
    t2 = f"Calculate actual openable sash area: {_fmt(openable_w_m, 1)} × {_fmt(openable_h_m, 1)} = {_fmt(actual_vent_m2, 2)} m²."
    t3 = f"Compare {_fmt(actual_vent_m2, 2)} m² to {_fmt(min_vent_m2, 2)} m²."

    explanation = [
        f"Step 1: Calculate minimum 5% ventilation requirement = {_fmt(floor_area_m2, 1)} m² × 0,05 = {_fmt(min_vent_m2, 2)} m² [1 Mark: Method].",
        f"Step 2: Actual openable sash area = {_fmt(openable_w_m, 1)} × {_fmt(openable_h_m, 1)} = {_fmt(actual_vent_m2, 2)} m² [1 Mark: Method].",
        f"Step 3: Compare and state compliance: {status} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_31",
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


def gen_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Subskill 32: Circulation flow and door swing conflict analysis in tight spaces."""
    prompt = (
        "In a compact 1,8 m × 1,5 m bathroom floor plan, an architect places a standard 813 mm hinged entrance door "
        "that swings INWARD directly against the toilet bowl, leaving only 120 mm clearance.\n\n"
        "What architectural and safety issue does this cause, and what is the standard recommended solution?"
    )

    correct_ans = "The inward swing creates a dangerous entrapment hazard if an occupant collapses inside; the door should either swing OUTWARD or be replaced with a sliding pocket door"
    custom_opts = [
        correct_ans,
        "It increases municipal water tariffs by restricting sewer pipe ventilation",
        "It causes the toilet porcelain to crack due to atmospheric air pressure changes",
        "It violates South African electrical zoning because doors cannot face sanitary fittings",
    ]

    t1 = "Consider emergency access in small bathrooms."
    t2 = "If someone falls behind an inward-swinging door, rescuers cannot push the door open."
    t3 = "The standard design remedy is to reverse the door swing outward or use a sliding door."

    explanation = [
        f"Step 1: Identify ergonomic and safety hazards in compact spaces [1 Mark: Method].",
        f"Step 2: Recognize entrapment risk during medical emergencies [1 Mark: Method].",
        f"Step 3: State the recommended architectural solution (outward swing or sliding door) [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_32",
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
