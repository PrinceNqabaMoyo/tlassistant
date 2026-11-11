"""Subskills 17-24: Elevation Plans & Multi-View Projections for Grade 12 Plans & Scale."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def gen_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Subskill 17: Identifying North, South, East, West elevation views from floor plan orientation."""
    directions = [
        {"dir": "North Elevation", "face": "facing towards True North (viewed looking South)"},
        {"dir": "South Elevation", "face": "facing towards True South (viewed looking North)"},
        {"dir": "East Elevation", "face": "facing towards the sunrise direction (viewed looking West)"},
        {"dir": "West Elevation", "face": "facing towards the sunset direction (viewed looking East)"},
    ]
    target = r.choice(directions)

    prompt = (
        f"Refer to the building plan orientation and compass rose shown in the diagram. "
        f"Which architectural elevation corresponds to the exterior wall {target['face']}?"
    )
    b_deg = 0 if "North" in target["dir"] else (180 if "South" in target["dir"] else (90 if "East" in target["dir"] else 270))
    d_spec_17 = {
        "diagram_role": "context",
        "kind": "compass_rose",
        "title": f"Plan Orientation ({target['dir']})",
        "bearing_deg": b_deg,
        "target_dir": target["dir"],
    }

    correct_ans = target["dir"]
    custom_opts = [
        correct_ans,
        [d["dir"] for d in directions if d["dir"] != target["dir"]][0],
        [d["dir"] for d in directions if d["dir"] != target["dir"]][1],
        [d["dir"] for d in directions if d["dir"] != target["dir"]][2],
    ]

    t1 = "Consider the 4 cardinal directions relative to the compass arrow."
    t2 = "The elevation is named after the external face of the building that looks toward that direction."
    t3 = f"The exterior wall {target['face']} is the {target['dir']}."

    explanation = [
        f"Step 1: Identify the compass orientation marked on the plan [1 Mark: Method].",
        f"Step 2: Relate the building facade direction to the cardinal compass points [1 Mark: Method].",
        f"Step 3: Conclude that the wall is designated as the {target['dir']} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_17",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_17,
    )


def gen_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Subskill 18: Identifying Front, Rear, Left, and Right elevation views of a building."""
    views = [
        {"view": "Front Elevation", "desc": "shows the primary street entrance doorway and main veranda"},
        {"view": "Rear (Back) Elevation", "desc": "shows the private back garden, kitchen exit door, and courtyard"},
        {"view": "Left Side Elevation", "desc": "shows the building exterior viewed from the observer's left side when facing the front entrance"},
        {"view": "Right Side Elevation", "desc": "shows the building exterior viewed from the observer's right side when facing the front entrance"},
    ]
    item = r.choice(views)

    prompt = (
        f"Refer to the orthogonal elevation drawings shown in the diagram. "
        f"Which elevation view {item['desc']}?"
    )
    d_spec_18 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Orthogonal Facade ({item['view']})",
        "view_name": item["view"],
        "features": [item["desc"]],
    }

    correct_ans = item["view"]
    custom_opts = [
        correct_ans,
        [v["view"] for v in views if v["view"] != item["view"]][0],
        [v["view"] for v in views if v["view"] != item["view"]][1],
        [v["view"] for v in views if v["view"] != item["view"]][2],
    ]

    t1 = "Read the architectural description of the facade."
    t2 = "Identify whether the features describe the street frontage, rear garden, or side flank."
    t3 = f"The correct view is the {item['view']}."

    explanation = [
        f"Step 1: Analyze the prominent features listed (entrance, kitchen, side views) [1 Mark: Method].",
        f"Step 2: Orient observer perspective relative to the front entrance [1 Mark: Method].",
        f"Step 3: Conclude that this corresponds to the {item['view']} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_18",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_18,
    )


def gen_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Subskill 19: Determining shared measurements between Front view and Left side view."""
    # Via Afrika textbook question 3.3.1 (LB page 260)
    prompt = (
        "A builder is given a completed Left Side Elevation of a timber Wendy house and needs to construct "
        "the Front Elevation drawing.\n\n"
        "Which of the following sets lists FOUR vertical measurements that will be IDENTICAL in both "
        "the Front view and the Left side view?"
    )

    correct_ans = "1. Height to the roof ridge apex; 2. Height to the wall plate / eaves; 3. Height of window top; 4. Height of window sill above floor"
    custom_opts = [
        correct_ans,
        "1. Overall building width; 2. Width of entrance door; 3. Length of side wall; 4. Width of window panes",
        "1. Property stand boundary width; 2. Depth of foundation trench; 3. Roof pitch angle; 4. Diameter of gutter",
        "1. Distance to street curb; 2. Area of kitchen floor; 3. Height of chimney flue; 4. Brandering spacing",
    ]

    t1 = "Vertical heights above the level ground remain constant around the perimeter of the building."
    t2 = "Horizontal widths differ between front and side, but vertical wall and opening levels are shared."
    t3 = "The shared measurements are vertical heights: roof apex, wall eaves, window top, and window sill."

    explanation = [
        f"Step 1: Recognize that on a flat site, all vertical levels remain consistent across all four elevation views [1 Mark: Method].",
        f"Step 2: Eliminate horizontal dimensions (widths, lengths) which change between front and side [1 Mark: Method].",
        f"Step 3: State the 4 shared vertical heights [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_19",
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


def gen_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Subskill 20: Deducing missing Front view dimensions from Side elevation and Floor plan."""
    # Via Afrika textbook question 3.3.2 (LB page 260)
    # Wendy house: front width = 3.6 m. Scale 1:40 (or 1:50) -> 360 cm / 40 = 9.0 cm on drawing!
    scale = r.choice([40, 50])
    real_front_width_m = r.choice([3.2, 3.6, 4.0, 4.5])
    real_front_cm = real_front_width_m * 100.0
    plan_width_cm = real_front_cm / scale

    prompt = (
        f"Refer to the Wendy house floor plan and elevation views shown in the diagram (scale ratio 1 : {scale}). "
        f"The front of the structure is {_fmt(real_front_width_m, 1)} m wide on the floor plan.\n\n"
        f"Calculate the width of the Wendy house as it should be drawn on the Front view elevation, in centimetres."
    )
    d_spec_20 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Wendy House Elevation (Front Width {_fmt(real_front_width_m, 1)} m)",
        "side": "Front",
        "elevation": "Wendy House Front Elevation",
        "width_m": real_front_width_m,
        "height_m": 2.4,
        "scale_ratio": f"1 : {scale}",
        "front_width_m": real_front_width_m,
        "plan_width_cm": plan_width_cm,
    }

    correct_ans = f"{_fmt(plan_width_cm, 1)} cm"
    custom_opts = [
        correct_ans,
        f"{_fmt(plan_width_cm * 2, 1)} cm",
        f"{_fmt(plan_width_cm / 2, 1)} cm",
        f"{_fmt(real_front_width_m * 10, 1)} cm",
    ]

    t1 = f"Convert the real front width from metres to centimetres: {_fmt(real_front_width_m, 1)} m × 100 = {_fmt(real_front_cm, 0)} cm."
    t2 = f"Divide the centimetres by the scale factor of {scale}."
    t3 = f"Width on drawing = {_fmt(real_front_cm, 0)} ÷ {scale} = {_fmt(plan_width_cm, 1)} cm."

    explanation = [
        f"Step 1: Convert ground width to cm: {_fmt(real_front_width_m, 1)} m × 100 = {_fmt(real_front_cm, 0)} cm [1 Mark: Method].",
        f"Step 2: Apply scale 1 : {scale}: {_fmt(real_front_cm, 0)} cm ÷ {scale} [1 Mark: Method].",
        f"Step 3: Drawing width on Front elevation = {_fmt(plan_width_cm, 1)} cm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_20",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_20,
    )


def gen_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Roof overhang (eaves) dimension from elevation view."""
    scale = 50
    overhang_real_mm = r.choice([300.0, 450.0, 600.0])
    model_overhang_mm = overhang_real_mm / scale

    prompt = (
        f"Refer to the sectional elevation shown in the diagram (scale ratio 1 : {scale}), where a pitched roof creates eaves. "
        f"The specification stipulates a standard roof overhang of {_fmt(overhang_real_mm, 0)} mm beyond the exterior brick face.\n\n"
        f"What distance (in millimetres) should represent this roof overhang on the 1 : {scale} drawing?"
    )
    d_spec_21 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Sectional Roof Eaves (Overhang {_fmt(overhang_real_mm, 0)} mm)",
        "side": "Eaves",
        "elevation": "Roof Eaves Detail",
        "roof": "pitched",
        "height_m": 0.5,
        "dimensions": {"overhang_mm": overhang_real_mm},
        "scale_ratio": f"1 : {scale}",
        "overhang_mm": overhang_real_mm,
    }

    correct_ans = f"{_fmt(model_overhang_mm, 1)} mm"
    custom_opts = [
        correct_ans,
        f"{_fmt(model_overhang_mm * 2, 1)} mm",
        f"{_fmt(model_overhang_mm / 2, 1)} mm",
        f"{_fmt(overhang_real_mm / 10, 1)} mm",
    ]

    t1 = "Both the real measurement and answer are in millimetres."
    t2 = f"Divide the real overhang ({_fmt(overhang_real_mm, 0)} mm) by the scale denominator ({scale})."
    t3 = f"Drawing measurement = {_fmt(overhang_real_mm, 0)} ÷ {scale} = {_fmt(model_overhang_mm, 1)} mm."

    explanation = [
        f"Step 1: Identify real overhang = {_fmt(overhang_real_mm, 0)} mm [1 Mark: Method].",
        f"Step 2: Divide by scale factor {scale}: {_fmt(overhang_real_mm, 0)} ÷ {scale} [1 Mark: Method].",
        f"Step 3: Overhang on drawing = {_fmt(model_overhang_mm, 1)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_21",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_21,
    )


def gen_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Subskill 22: Window sill height above finished floor level (AFFL) from elevation."""
    scale = 50
    sill_height_real_mm = r.choice([900.0, 1050.0, 1200.0, 1500.0])
    plan_sill_mm = sill_height_real_mm / scale

    prompt = (
        f"Refer to the residential elevation plan shown in the diagram (scale ratio 1 : {scale}). "
        f"The window sill height above finished floor level (AFFL) measures {_fmt(plan_sill_mm, 1)} mm on the paper.\n\n"
        f"Calculate the actual construction height of the window sill above the floor in millimetres (mm)."
    )
    d_spec_22 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Window Sill Height Plan (Scale 1 : {scale})",
        "side": "Front",
        "elevation": "Window Sill Elevation",
        "height_m": sill_height_real_mm / 1000.0,
        "dimensions": {"sill_height_mm": sill_height_real_mm},
        "scale_ratio": f"1 : {scale}",
        "plan_sill_mm": plan_sill_mm,
        "real_sill_mm": sill_height_real_mm,
    }

    correct_ans = f"{_fmt(sill_height_real_mm, 0)} mm"
    custom_opts = [
        correct_ans,
        f"{_fmt(sill_height_real_mm * 1.5, 0)} mm",
        f"{_fmt(sill_height_real_mm * 0.75, 0)} mm",
        f"{_fmt(plan_sill_mm * 10, 0)} mm",
    ]

    t1 = f"Multiply the plan measurement ({_fmt(plan_sill_mm, 1)} mm) by the scale factor {scale}."
    t2 = f"Actual height = {_fmt(plan_sill_mm, 1)} mm × {scale}."
    t3 = f"Actual height = {_fmt(plan_sill_mm, 1)} × {scale} = {_fmt(sill_height_real_mm, 0)} mm."

    explanation = [
        f"Step 1: Multiply drawing measurement by scale: {_fmt(plan_sill_mm, 1)} mm × {scale} [1 Mark: Method].",
        f"Step 2: Carry out multiplication: {_fmt(plan_sill_mm, 1)} × {scale} = {_fmt(sill_height_real_mm, 0)} mm [1 Mark: Method].",
        f"Step 3: Actual window sill height = {_fmt(sill_height_real_mm, 0)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_22",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_22,
    )


def gen_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Subskill 23: Top-of-door to ceiling clearance measurement on elevation."""
    ceiling_h_mm = r.choice([2400, 2600, 2700])
    door_h_mm = 2032  # Standard door height
    lintel_clearance_mm = ceiling_h_mm - door_h_mm

    prompt = (
        f"A room has a finished ceiling height of {ceiling_h_mm} mm.\n"
        f"The standard internal timber door frame has a height of 2 032 mm above the floor.\n\n"
        f"Calculate the vertical wall clearance between the top of the door frame and the ceiling line (in millimetres)."
    )

    correct_ans = f"{lintel_clearance_mm} mm"
    custom_opts = [
        correct_ans,
        f"{lintel_clearance_mm + 100} mm",
        f"{lintel_clearance_mm - 100} mm",
        f"{ceiling_h_mm // 2} mm",
    ]

    t1 = "Subtract the door frame height from the ceiling height."
    t2 = f"{ceiling_h_mm} mm - 2 032 mm."
    t3 = f"Clearance = {ceiling_h_mm} - 2 032 = {lintel_clearance_mm} mm."

    explanation = [
        f"Step 1: Identify ceiling level ({ceiling_h_mm} mm) and door frame height (2 032 mm) [1 Mark: Method].",
        f"Step 2: Subtract: {ceiling_h_mm} mm - 2 032 mm [1 Mark: Method].",
        f"Step 3: Vertical clearance above door = {lintel_clearance_mm} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_23",
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


def gen_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Subskill 24: Verifying building height limit against municipal zoning bylaws."""
    scale = 100
    max_bylaw_h_m = 8.5
    # Measured height from natural ground level to roof apex on plan in cm
    measured_apex_cm = r.choice([7.2, 7.8, 8.2, 8.8, 9.2])
    actual_apex_m = (measured_apex_cm * scale) / 100.0

    compliant = actual_apex_m <= max_bylaw_h_m
    status = (
        f"Compliant: actual apex height is {_fmt(actual_apex_m, 2)} m (≤ 8,50 m municipal limit)"
        if compliant
        else f"Non-compliant: actual apex height is {_fmt(actual_apex_m, 2)} m (> 8,50 m municipal limit)"
    )

    prompt = (
        f"Municipal town planning bylaws specify that no single-dwelling residential roof apex "
        f"may exceed 8,50 m measured vertically above Natural Ground Level (NGL).\n"
        f"On a 1 : {scale} elevation drawing, the total vertical height from NGL to the roof ridge apex "
        f"measures {_fmt(measured_apex_cm, 1)} cm.\n\n"
        f"Determine whether this design complies with municipal height restrictions. Show your calculation."
    )

    correct_ans = status
    custom_opts = [
        correct_ans,
        f"Compliant: all residential structures with roof pitch under 30° are automatically exempt from height restrictions",
        f"Non-compliant: municipal bylaws restrict all residential buildings to a maximum of 4,50 m",
        f"Compliant: {_fmt(measured_apex_cm, 1)} cm on a plan always represents exactly 8,00 m in real life",
    ]

    t1 = f"Calculate the actual height: {_fmt(measured_apex_cm, 1)} cm × {scale} = {_fmt(measured_apex_cm * scale, 0)} cm = {_fmt(actual_apex_m, 2)} m."
    t2 = f"Compare {_fmt(actual_apex_m, 2)} m to the 8,50 m municipal limit."
    t3 = f"{status}."

    explanation = [
        f"Step 1: Calculate actual building apex height: {_fmt(measured_apex_cm, 1)} cm × {scale} = {_fmt(measured_apex_cm * scale, 0)} cm = {_fmt(actual_apex_m, 2)} m [1 Mark: Method].",
        f"Step 2: Compare against bylaw limit of 8,50 m [1 Mark: Method].",
        f"Step 3: {status} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_24",
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
