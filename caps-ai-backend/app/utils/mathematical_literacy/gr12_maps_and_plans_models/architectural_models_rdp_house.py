"""Subskills 09-16: Architectural Models (RDP House & Community Structures) for Grade 12 Maps & Plans (Models)."""
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


def gen_subskill_09(r: random.Random) -> Dict[str, Any]:
    """Subskill 09: RDP house standard floor plan: scaled exterior wall dimensions."""
    scale = 50
    real_l_m = r.choice([6.8, 7.2, 7.5, 8.0])
    real_w_m = r.choice([5.0, 5.4, 5.8, 6.0])

    model_l_cm = (real_l_m * 100.0) / scale
    model_w_cm = (real_w_m * 100.0) / scale

    prompt = (
        f"Refer to the RDP house floor plan shown in the diagram (scale ratio 1 : {scale}). "
        f"The external dimensions of the house foundation slab are {_fmt(real_l_m, 1)} m long by {_fmt(real_w_m, 1)} m wide.\n\n"
        f"Calculate the exterior length and width of the model cardboard base, in centimetres."
    )
    d_spec_09 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"RDP House Model Base (Scale 1 : {scale})",
        "rooms": [{"name": "RDP House", "length": real_l_m, "width": real_w_m}],
    }

    correct_ans = f"{_fmt(model_l_cm, 1)} cm × {_fmt(model_w_cm, 1)} cm"
    custom_opts = [
        correct_ans,
        f"{_fmt(model_l_cm * 2, 1)} cm × {_fmt(model_w_cm * 2, 1)} cm",
        f"{_fmt(model_l_cm / 2, 1)} cm × {_fmt(model_w_cm / 2, 1)} cm",
        f"{_fmt(real_l_m * 10, 1)} cm × {_fmt(real_w_m * 10, 1)} cm",
    ]

    t1 = "Convert the actual metres to centimetres by multiplying by 100."
    t2 = f"Divide each dimension in centimetres by the scale factor of {scale}."
    t3 = f"Length = ({_fmt(real_l_m, 1)} × 100) ÷ {scale} = {_fmt(model_l_cm, 1)} cm. Width = ({_fmt(real_w_m, 1)} × 100) ÷ {scale} = {_fmt(model_w_cm, 1)} cm."

    explanation = [
        f"Step 1: Real dimensions in cm: Length = {_fmt(real_l_m * 100, 0)} cm, Width = {_fmt(real_w_m * 100, 0)} cm [1 Mark: Method].",
        f"Step 2: Divide by scale factor {scale}: Length = {_fmt(real_l_m * 100, 0)} ÷ {scale}; Width = {_fmt(real_w_m * 100, 0)} ÷ {scale} [1 Mark: Method].",
        f"Step 3: Model base dimensions = {_fmt(model_l_cm, 1)} cm × {_fmt(model_w_cm, 1)} cm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_09",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_09,
    )


def gen_subskill_10(r: random.Random) -> Dict[str, Any]:
    """Subskill 10: RDP house interior partition wall offset measurements."""
    scale = r.choice([25, 50])
    wall_offset_m = r.choice([2.5, 3.0, 3.2, 3.5])
    model_offset_cm = (wall_offset_m * 100.0) / scale

    prompt = (
        f"On a 1 : {scale} architectural model of a two-bedroom house, an interior partition wall dividing "
        f"the living room from the master bedroom must be placed exactly {_fmt(wall_offset_m, 1)} m from the front exterior wall.\n\n"
        f"At what distance from the front wall of the model must the balsa wood partition strip be glued, in centimetres?"
    )

    correct_ans = f"{_fmt(model_offset_cm, 1)} cm"
    custom_opts = [
        correct_ans,
        f"{_fmt(model_offset_cm * 2, 1)} cm",
        f"{_fmt(model_offset_cm / 2, 1)} cm",
        f"{_fmt(wall_offset_m * 10, 1)} cm",
    ]

    t1 = "Convert the real offset distance from metres to centimetres."
    t2 = f"Divide the centimetres by the scale factor of {scale}."
    t3 = f"Offset in cm = ({_fmt(wall_offset_m, 1)} × 100) ÷ {scale} = {_fmt(model_offset_cm, 1)} cm."

    explanation = [
        f"Step 1: Convert real offset distance to cm: {_fmt(wall_offset_m, 1)} m × 100 = {_fmt(wall_offset_m * 100, 0)} cm [1 Mark: Method].",
        f"Step 2: Divide by scale factor {scale}: {_fmt(wall_offset_m * 100, 0)} cm ÷ {scale} [1 Mark: Method].",
        f"Step 3: Distance on model = {_fmt(model_offset_cm, 1)} cm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_10",
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


def gen_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Subskill 11: Scaled window and door cut-out dimensions for model walls."""
    scale = r.choice([20, 25, 50])
    # Standard external door in SA: 813 mm wide x 2 032 mm high
    door_w_mm = 813.0
    door_h_mm = 2032.0

    model_w_mm = door_w_mm / scale
    model_h_mm = door_h_mm / scale

    prompt = (
        f"Refer to the entrance doorway detail shown in the diagram (scale ratio 1 : {scale}). "
        f"A standard external entrance door has a width of 813 mm and a height of 2 032 mm.\n\n"
        f"If a learner is cutting out the front doorway on a cardboard wall at a scale of 1 : {scale}, "
        f"what should be the cut-out dimensions in millimetres (rounded to one decimal place)?"
    )
    d_spec_11 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Doorway Opening Cutout (Scale 1 : {scale})",
        "side": "Front",
        "elevation": "Front Elevation",
        "width_m": door_w_mm / 1000.0,
        "height_m": door_h_mm / 1000.0,
        "door_w_mm": door_w_mm,
        "door_h_mm": door_h_mm,
        "model_w_mm": model_w_mm,
        "model_h_mm": model_h_mm,
    }

    correct_ans = f"{_fmt(model_w_mm, 1)} mm × {_fmt(model_h_mm, 1)} mm"
    custom_opts = [
        correct_ans,
        f"{_fmt(model_w_mm * 1.5, 1)} mm × {_fmt(model_h_mm * 1.5, 1)} mm",
        f"{_fmt(model_w_mm * 0.75, 1)} mm × {_fmt(model_h_mm * 0.75, 1)} mm",
        f"{_fmt(model_w_mm * 2.0, 1)} mm × {_fmt(model_h_mm * 2.0, 1)} mm",
        f"{_fmt(model_w_mm * 0.5, 1)} mm × {_fmt(model_h_mm * 0.5, 1)} mm",
    ]

    t1 = "Both the real door width and height are already given in millimetres."
    t2 = f"Divide both real dimensions by the scale factor {scale}."
    t3 = f"Model door width = 813 ÷ {scale} = {_fmt(model_w_mm, 1)} mm. Model door height = 2 032 ÷ {scale} = {_fmt(model_h_mm, 1)} mm."

    explanation = [
        f"Step 1: Identify standard door dimensions: Width = 813 mm, Height = 2 032 mm [1 Mark: Method].",
        f"Step 2: Scale both dimensions by dividing by {scale}: Width = 813 ÷ {scale} = {_fmt(model_w_mm, 1)} mm; Height = 2 032 ÷ {scale} = {_fmt(model_h_mm, 1)} mm [1 Mark: Method].",
        f"Step 3: Scaled cut-out dimensions = {_fmt(model_w_mm, 1)} mm × {_fmt(model_h_mm, 1)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_11",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_11,
    )


def gen_subskill_12(r: random.Random) -> Dict[str, Any]:
    """Subskill 12: Gabled roof rafter pitch calculation at scale using Pythagoras."""
    scale = r.choice([25, 50])
    building_width_m = r.choice([5.0, 6.0, 7.0])
    half_span_m = building_width_m / 2.0
    roof_rise_m = r.choice([1.0, 1.2, 1.5])

    # Real rafter length via Pythagoras: sqrt(half_span^2 + rise^2)
    rafter_real_m = math.sqrt((half_span_m ** 2) + (roof_rise_m ** 2))
    rafter_model_cm = (rafter_real_m * 100.0) / scale

    prompt = (
        f"A symmetrical pitched gable roof has a total building span (width) of {_fmt(building_width_m, 1)} m. "
        f"The vertical roof rise from wall plate to the apex ridge is {_fmt(roof_rise_m, 1)} m.\n"
        f"An architectural model of the roof is built at a scale of 1 : {scale}.\n\n"
        f"Using the Theorem of Pythagoras (Rafter² = Half-Span² + Rise²), calculate the inclined length of the model rafter, in centimetres (rounded to 1 decimal place)."
    )

    correct_ans = f"{_fmt(rafter_model_cm, 1)} cm"
    custom_opts = [
        correct_ans,
        f"{_fmt((half_span_m * 100.0) / scale, 1)} cm",
        f"{_fmt((roof_rise_m * 100.0) / scale, 1)} cm",
        f"{_fmt(rafter_model_cm * 2, 1)} cm",
    ]

    t1 = f"Calculate the half-span: {_fmt(building_width_m, 1)} m ÷ 2 = {_fmt(half_span_m, 2)} m."
    t2 = f"Apply Pythagoras: Rafter = √(({_fmt(half_span_m, 2)})² + ({_fmt(roof_rise_m, 1)})²)."
    t3 = f"Real rafter = {_fmt(rafter_real_m, 3)} m = {_fmt(rafter_real_m * 100, 1)} cm. Model rafter = {_fmt(rafter_real_m * 100, 1)} ÷ {scale} = {_fmt(rafter_model_cm, 1)} cm."

    explanation = [
        f"Step 1: Calculate half-span = {_fmt(building_width_m, 1)} m ÷ 2 = {_fmt(half_span_m, 2)} m [1 Mark: Method].",
        f"Step 2: Real rafter length = √(({_fmt(half_span_m, 2)})² + ({_fmt(roof_rise_m, 1)})²) = √({_fmt(half_span_m**2, 2)} + {_fmt(roof_rise_m**2, 2)}) = {_fmt(rafter_real_m, 3)} m [1 Mark: Method].",
        f"Step 3: Convert to cm and scale: ({_fmt(rafter_real_m, 3)} × 100) ÷ {scale} = {_fmt(rafter_model_cm, 1)} cm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_12",
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


def gen_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: South vs North elevation wall height comparison in model."""
    name = r.choice(SA_NAMES)
    wall_height_m = r.choice([2.6, 2.7, 2.8, 3.0])
    scale = r.choice([25, 50, 100])
    scaled_h_cm = (wall_height_m * 100.0) / scale

    prompt = (
        f"Refer to the cottage elevation model shown in the diagram (scale ratio 1 : {scale}). "
        f"{name} is building a 1 : {scale} model of a cottage on a flat, level foundation slab. "
        f"The South elevation shows a vertical wall height of {_fmt(wall_height_m, 2)} m.\n\n"
        f"What should be the vertical wall height of the North elevation model wall, and why?"
    )
    d_spec_13 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Cottage Elevation Model (Scale 1 : {scale})",
        "side": "North/South",
        "elevation": "Wall Height Elevation",
        "height_m": wall_height_m,
        "wall_height_m": wall_height_m,
        "scaled_height_cm": scaled_h_cm,
    }

    correct_ans = f"{_fmt(scaled_h_cm, 2)} cm, because on a level foundation the exterior perimeter walls are identical in height"
    custom_opts = [
        correct_ans,
        f"{_fmt(scaled_h_cm * 1.5, 2)} cm, because the North elevation receives more sunlight and requires higher walls",
        f"{_fmt(scaled_h_cm * 0.8, 2)} cm, because North elevations are traditionally sloped downwards",
        f"{_fmt(scaled_h_cm, 2)} cm, but only if the roof has no eaves or gutters",
    ]

    t1 = "Consider whether the building is situated on level ground."
    t2 = f"On a level slab, opposite exterior walls that support a symmetrical roof share the same wall height ({_fmt(wall_height_m, 2)} m)."
    t3 = f"Calculate the scaled height: ({_fmt(wall_height_m, 2)} × 100) ÷ {scale} = {_fmt(scaled_h_cm, 2)} cm."

    explanation = [
        f"Step 1: Identify that the building sits on a level foundation slab, so opposing exterior walls have identical vertical heights [1 Mark: Method].",
        f"Step 2: Scale the wall height: ({_fmt(wall_height_m, 2)} × 100) ÷ {scale} = {_fmt(scaled_h_cm, 2)} cm [1 Mark: Method].",
        f"Step 3: State the model height: {_fmt(scaled_h_cm, 2)} cm with the architectural justification [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_13",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_13,
    )


def gen_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Subskill 14: Verifying doorway clearance for wheelchair/furniture access at scale."""
    scale = 50
    # SANS 10400-S standard wheelchair clearance: minimum 800 mm clear width
    clearance_real_mm = 800.0
    model_req_mm = clearance_real_mm / scale

    # Test cases: either 17 mm (850 mm real -> PASS) or 14 mm (700 mm real -> FAIL)
    pass_case = r.choice([True, False])
    if pass_case:
        model_measured_mm = 17.0
        real_measured_mm = model_measured_mm * scale  # 850 mm
        status = f"Yes, the doorway provides {real_measured_mm:.0f} mm clear opening (≥ 800 mm SANS requirement)"
    else:
        model_measured_mm = 14.0
        real_measured_mm = model_measured_mm * scale  # 700 mm
        status = f"No, the doorway provides only {real_measured_mm:.0f} mm clear opening (< 800 mm SANS requirement)"

    prompt = (
        f"According to the South African National Building Regulations (SANS 10400-S), an accessible doorway "
        f"must have a MINIMUM clear width of 800 mm to accommodate wheelchair users.\n"
        f"On a 1 : {scale} scale model of a community health center, a learner cuts a doorway with an opening width of {_fmt(model_measured_mm, 1)} mm.\n\n"
        f"Does this model doorway satisfy the national accessibility requirement in real life? Provide mathematical proof."
    )

    correct_ans = status
    custom_opts = [
        correct_ans,
        f"Yes, any model opening greater than 10 mm automatically satisfies SANS regulations",
        f"No, SANS regulations require all interior doors to be exactly 1 200 mm wide",
        f"Yes, because 800 mm divided by 50 equals 16 mm, which is equal to {_fmt(model_measured_mm, 1)} mm",
    ]

    t1 = f"Calculate the actual width represented by {_fmt(model_measured_mm, 1)} mm by multiplying by {scale}."
    t2 = f"Actual width = {_fmt(model_measured_mm, 1)} mm × {scale} = {real_measured_mm:.0f} mm."
    t3 = f"Compare {real_measured_mm:.0f} mm to the required 800 mm minimum."

    explanation = [
        f"Step 1: Minimum required real width = 800 mm (or 800 ÷ {scale} = 16,0 mm on model) [1 Mark: Method].",
        f"Step 2: Actual real doorway width = {_fmt(model_measured_mm, 1)} mm × {scale} = {real_measured_mm:.0f} mm [1 Mark: Method].",
        f"Step 3: {status} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_14",
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


def gen_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Subskill 15: Minimum ceiling height verification from model elevation (SANS 10400)."""
    scale = 50
    # SANS 10400 requires 2.4 m (2 400 mm) for habitable rooms
    min_real_m = 2.4
    min_model_cm = (min_real_m * 100.0) / scale  # 4.8 cm

    measured_cm = r.choice([4.2, 4.6, 5.0, 5.2])
    real_h_m = (measured_cm * scale) / 100.0

    compliant = real_h_m >= min_real_m
    verdict = (
        f"Compliant: actual ceiling height is {_fmt(real_h_m, 2)} m, which meets the 2,4 m SANS 10400 requirement"
        if compliant
        else f"Non-compliant: actual ceiling height is {_fmt(real_h_m, 2)} m, which is below the 2,4 m SANS 10400 requirement"
    )

    prompt = (
        f"Under South African Building Regulations (SANS 10400-A), the minimum permissible ceiling height "
        f"for any habitable bedroom or living room is 2,4 m.\n"
        f"On a 1 : {scale} elevation model of a proposed granny flat, the vertical distance from floor to ceiling "
        f"measures {_fmt(measured_cm, 1)} cm.\n\n"
        f"Is this design compliant with national regulations? Show your calculation."
    )

    correct_ans = verdict
    custom_opts = [
        correct_ans,
        f"Compliant: all ceiling heights above 2,0 m satisfy municipal building bylaws",
        f"Non-compliant: regulations require a minimum ceiling height of 3,5 m for all South African homes",
        f"Compliant: {_fmt(measured_cm, 1)} cm on a model automatically converts to 3,0 m",
    ]

    t1 = f"Multiply the measured model height ({_fmt(measured_cm, 1)} cm) by {scale} to find the actual height in cm."
    t2 = "Divide the actual height in cm by 100 to get metres."
    t3 = f"Actual height = ({_fmt(measured_cm, 1)} × {scale}) ÷ 100 = {_fmt(real_h_m, 2)} m. Compare to 2,4 m."

    explanation = [
        f"Step 1: Calculate actual ceiling height: {_fmt(measured_cm, 1)} cm × {scale} = {_fmt(measured_cm * scale, 0)} cm = {_fmt(real_h_m, 2)} m [1 Mark: Method].",
        f"Step 2: Compare with SANS 10400 minimum standard of 2,4 m [1 Mark: Method].",
        f"Step 3: {verdict} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_15",
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


def gen_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Subskill 16: Multi-room floor plan circulation corridor width check."""
    scale = r.choice([25, 50])
    # Minimum domestic passage/corridor width in SA: 900 mm (0.9 m)
    min_real_mm = 900.0
    corridor_real_mm = r.choice([800.0, 900.0, 1000.0, 1200.0])
    model_corridor_mm = corridor_real_mm / scale

    prompt = (
        f"A floor plan model built at a scale of 1 : {scale} includes a central circulation hallway between classrooms.\n"
        f"The physical width of the hallway on the model measures {_fmt(model_corridor_mm, 1)} mm.\n\n"
        f"Calculate the actual width of this hallway in real life (in millimetres), and state whether it meets "
        f"the standard minimum passage width of 900 mm."
    )

    meets_str = "meets" if corridor_real_mm >= min_real_mm else "does not meet"
    correct_ans = f"{corridor_real_mm:.0f} mm ({meets_str} the 900 mm minimum)"
    custom_opts = [
        correct_ans,
        f"{corridor_real_mm * 1.5:.0f} mm (meets the 900 mm minimum)",
        f"{corridor_real_mm * 0.75:.0f} mm (does not meet the 900 mm minimum)",
        f"{model_corridor_mm * 10:.0f} mm (does not meet the 900 mm minimum)",
    ]

    t1 = f"Multiply the model hallway measurement ({_fmt(model_corridor_mm, 1)} mm) by the scale factor {scale}."
    t2 = f"Actual width = {_fmt(model_corridor_mm, 1)} mm × {scale} = {corridor_real_mm:.0f} mm."
    t3 = f"Compare {corridor_real_mm:.0f} mm to 900 mm."

    explanation = [
        f"Step 1: Calculate actual hallway width: {_fmt(model_corridor_mm, 1)} mm × {scale} = {corridor_real_mm:.0f} mm [1 Mark: Method].",
        f"Step 2: Compare against standard minimum passage requirement of 900 mm [1 Mark: Method].",
        f"Step 3: Actual width = {corridor_real_mm:.0f} mm ({meets_str} the 900 mm minimum) [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_16",
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
