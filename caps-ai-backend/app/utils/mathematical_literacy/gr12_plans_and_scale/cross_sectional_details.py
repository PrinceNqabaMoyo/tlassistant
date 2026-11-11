"""Subskills 41-46: Cross-Sectional Technical Details for Grade 12 Plans & Scale."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def gen_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Foundation trench depth, footing width, and concrete slab thickness."""
    scale = 20
    # Standard foundation detail:
    # Footing width = 600 mm, footing depth = 250 mm, floor slab thickness = 100 mm, trench depth = 800 mm
    footing_w_mm = 600.0
    slab_thickness_mm = 100.0
    trench_depth_mm = r.choice([600.0, 750.0, 800.0, 900.0])

    plan_footing_w_cm = (footing_w_mm / scale) / 10.0  # in cm
    plan_trench_d_cm = (trench_depth_mm / scale) / 10.0

    prompt = (
        f"Refer to the foundation cross-section detail drawing shown in the diagram (scale ratio 1 : {scale}). "
        f"The concrete footing strip width measures {_fmt(plan_footing_w_cm, 1)} cm on paper, "
        f"and the depth of the foundation trench below ground level measures {_fmt(plan_trench_d_cm, 1)} cm on paper.\n\n"
        f"Calculate the ACTUAL full-size construction dimensions of the footing width and trench depth in millimetres (mm)."
    )
    d_spec_41 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Foundation Cross-Section (Scale 1 : {scale})",
        "side": "Section",
        "elevation": "Foundation Cross-Section",
        "label": "Foundation Trench",
        "height_m": 0.6,
        "scale_ratio": f"1 : {scale}",
        "footing_cm": plan_footing_w_cm,
        "trench_cm": plan_trench_d_cm,
    }

    correct_ans = f"Footing: {_fmt(footing_w_mm, 0)} mm; Trench: {_fmt(trench_depth_mm, 0)} mm"
    custom_opts = [
        correct_ans,
        f"Footing: {_fmt(footing_w_mm * 2, 0)} mm; Trench: {_fmt(trench_depth_mm * 2, 0)} mm",
        f"Footing: {_fmt(footing_w_mm / 2, 0)} mm; Trench: {_fmt(trench_depth_mm / 2, 0)} mm",
        f"Footing: {_fmt(plan_footing_w_cm * 10, 0)} mm; Trench: {_fmt(plan_trench_d_cm * 10, 0)} mm",
    ]

    t1 = f"Convert the plan cm measurements to mm (multiply by 10)."
    t2 = f"Multiply by the scale denominator ({scale})."
    t3 = f"Footing = ({_fmt(plan_footing_w_cm, 1)} × 10) × {scale} = {_fmt(footing_w_mm, 0)} mm. Trench = ({_fmt(plan_trench_d_cm, 1)} × 10) × {scale} = {_fmt(trench_depth_mm, 0)} mm."

    explanation = [
        f"Step 1: Convert plan cm to mm: Footing = {_fmt(plan_footing_w_cm * 10, 0)} mm; Trench = {_fmt(plan_trench_d_cm * 10, 0)} mm [1 Mark: Method].",
        f"Step 2: Multiply by scale factor {scale}: Footing = {_fmt(plan_footing_w_cm * 10, 0)} × {scale} = {_fmt(footing_w_mm, 0)} mm; Trench = {_fmt(plan_trench_d_cm * 10, 0)} × {scale} = {_fmt(trench_depth_mm, 0)} mm [1 Mark: Method].",
        f"Step 3: State full-size dimensions: Footing: {_fmt(footing_w_mm, 0)} mm; Trench: {_fmt(trench_depth_mm, 0)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_41",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_41,
    )


def gen_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Subskill 42: Damp Proof Course (DPC) and Damp Proof Membrane (DPM) location and purpose."""
    prompt = (
        "In a detailed foundation section drawing, a thick black zigzag line labeled 'DPC' is inserted "
        "horizontally within a masonry mortar joint directly level with the top of the concrete floor slab.\n\n"
        "What does the acronym 'DPC' stand for, and what is its essential building function?"
    )

    correct_ans = "Damp Proof Course: an impervious polyethylene plastic strip that blocks moisture from rising up through brickwork porous mortar via capillary action (rising damp)"
    custom_opts = [
        correct_ans,
        "Direct Power Conduit: an electrical channel that delivers municipal power to under-floor sockets",
        "Drainage Pressure Controller: an automated pneumatic valve that controls greywater discharge",
        "Diagonal Pre-cast Concrete: a structural lintel placed to reinforce internal door thresholds",
    ]

    t1 = "Consider what happens when porous bricks rest on moist soil."
    t2 = "DPC prevents ground water from being wicked upwards into internal walls."
    t3 = "DPC stands for Damp Proof Course, and it prevents rising damp."

    explanation = [
        f"Step 1: Identify the standard building terminology: DPC = Damp Proof Course [1 Mark: Method].",
        f"Step 2: Explain capillary action and ground moisture transmission in masonry [1 Mark: Method].",
        f"Step 3: Conclude that its primary function is preventing rising damp into living spaces [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_42",
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


def gen_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Subskill 43: Wall construction layers: double-brick vs single skin with plaster."""
    wall_types = [
        {"type": "Double-brick solid wall (one-brick wall)", "thickness": "220 mm (two leaves of 105 mm bricks with a 10 mm mortar collar joint)"},
        {"type": "Half-brick single skin wall (internal non-loadbearing partition)", "thickness": "110 mm (single stretcher leaf of 105 mm brick plus plaster)"},
        {"type": "Cavity wall (coastal weatherproofing)", "thickness": "270 mm (two 105 mm brick leaves separated by a 50 mm continuous air cavity with wall ties)"},
    ]
    target = r.choice(wall_types)

    prompt = (
        f"An architectural specification specifies an exterior wall construction described as:\n"
        f"'{target['type']}'.\n\n"
        f"What is the standard nominal construction thickness of this wall assembly in millimetres?"
    )

    correct_ans = target["thickness"]
    custom_opts = [
        correct_ans,
        "500 mm (cast in-situ solid basalt boulder masonry)",
        "50 mm (single gypsum drywall plasterboard panel)",
        "150 mm (pre-stressed reinforced concrete pavement slab)",
    ]

    t1 = "Recall South African standard clay brick dimensions: 222 mm long × 106 mm wide × 73 mm high."
    t2 = "A single stretcher leaf is roughly 110 mm thick, while a double wall is 220 mm thick."
    t3 = f"The nominal thickness is {target['thickness']}."

    explanation = [
        f"Step 1: Review standard South African imperial/metric clay brick dimensions [1 Mark: Method].",
        f"Step 2: Account for leaf arrangement, mortar joints, and air cavities [1 Mark: Method].",
        f"Step 3: State nominal wall thickness: {target['thickness']} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_43",
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


def gen_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Ceiling truss pitch, collar tie, and brandering spacing."""
    # Brandering: timber strips nailed perpendicular to the underside of trusses
    # Standard spacing for gypsum plasterboard (Rhinoboard): 450 mm centres
    room_length_m = r.choice([3.6, 4.0, 4.5, 5.4])
    room_length_mm = room_length_m * 1000.0
    spacing_mm = 450.0
    battens_count = int(room_length_mm // spacing_mm) + 1

    prompt = (
        f"To install a gypsum board ceiling in a room {_fmt(room_length_m, 1)} m long, a carpenter nails timber brandering "
        f"battens (38 mm × 38 mm) across the underside of the roof trusses at 450 mm centre-to-centre spacing.\n\n"
        f"Calculate the minimum number of brandering batten rows needed across the {_fmt(room_length_m, 1)} m length of the ceiling.\n"
        f"(Formula: Rows = [Room Length ÷ 450 mm] + 1; discard any fraction and add 1 for the starting batten)."
    )

    correct_ans = f"{battens_count} rows"
    custom_opts = [
        correct_ans,
        f"{battens_count - 1} rows",
        f"{battens_count + 1} rows",
        f"{battens_count + 2} rows",
        f"{battens_count - 2} rows",
    ]

    t1 = f"Convert {_fmt(room_length_m, 1)} m to millimetres: {_fmt(room_length_mm, 0)} mm."
    t2 = f"Divide by 450 mm and add 1 for the end batten: ({_fmt(room_length_mm, 0)} ÷ 450) + 1."
    t3 = f"{_fmt(room_length_mm, 0)} ÷ 450 = {room_length_mm / 450:.2f} → {int(room_length_mm // spacing_mm)} spaces + 1 = {battens_count} rows."

    explanation = [
        f"Step 1: Convert room length to mm: {_fmt(room_length_m, 1)} m × 1 000 = {_fmt(room_length_mm, 0)} mm [1 Mark: Method].",
        f"Step 2: Number of intervals = {_fmt(room_length_mm, 0)} ÷ 450 = {room_length_mm / 450:.2f} [1 Mark: Method].",
        f"Step 3: Total brandering rows = {int(room_length_mm // spacing_mm)} + 1 = {battens_count} rows [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_44",
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


def gen_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Subskill 45: Natural ground level (NGL) vs finished floor level (FFL) step-up height."""
    # SANS 10400 requirement: FFL must be at least 150 mm above NGL to prevent flood water ingress
    min_step_mm = 150
    step_options = [100, 150, 180, 220]
    actual_step_mm = r.choice(step_options)

    compliant = actual_step_mm >= min_step_mm
    status = (
        f"Compliant: FFL step of {actual_step_mm} mm meets the mandatory 150 mm SANS minimum above ground level"
        if compliant
        else f"Non-compliant: FFL step of {actual_step_mm} mm is below the 150 mm SANS minimum, creating flood ingress risk"
    )

    prompt = (
        f"Refer to the foundation cross-sectional detail shown in the diagram. "
        f"Under South African National Building Regulations (SANS 10400 Part J), the Finished Floor Level (FFL) "
        f"of any habitable dwelling must be elevated by a MINIMUM of 150 mm above the surrounding Natural Ground Level (NGL).\n"
        f"On the technical cross-section, the top of a finished concrete slab is drawn {actual_step_mm} mm above the ground.\n\n"
        f"Does this floor elevation comply with national building regulations?"
    )
    d_spec_45 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"FFL vs NGL Step-Up Detail ({actual_step_mm} mm)",
        "side": "Section",
        "elevation": "FFL vs NGL Step-Up Detail",
        "label": "FFL Step-Up",
        "height_m": actual_step_mm / 1000.0,
        "step_mm": actual_step_mm,
        "min_sans_mm": min_step_mm,
    }

    correct_ans = status
    custom_opts = [
        correct_ans,
        "Compliant: finished floors may be set completely flush with ground level if turf is planted",
        "Non-compliant: national regulations require all domestic floors to be raised by exactly 1 000 mm",
        "Compliant: only coastal properties within 500 m of the sea are subject to floor height standards",
    ]

    t1 = f"Compare the design step height ({actual_step_mm} mm) against the SANS minimum requirement (150 mm)."
    t2 = "The floor must be at least 150 mm higher than ground level to stop rainwater pouring inside."
    t3 = f"{status}."

    explanation = [
        f"Step 1: Identify mandatory SANS 10400 minimum clearance: FFL ≥ NGL + 150 mm [1 Mark: Method].",
        f"Step 2: Compare design step ({actual_step_mm} mm) to 150 mm [1 Mark: Method].",
        f"Step 3: State compliance and environmental rationale: {status} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_45",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_45,
    )


def gen_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Subskill 46: Rainwater gutter fall gradient and downpipe positioning."""
    # SANS 10400 gutter fall: minimum 1:500 (2 mm fall per 1 m of gutter length) towards downpipe
    gutter_length_m = r.choice([6.0, 8.0, 10.0, 12.0])
    fall_per_m_mm = 2.0  # 1:500 gradient
    total_fall_mm = gutter_length_m * fall_per_m_mm

    prompt = (
        f"To ensure rainwater drains effectively into downpipes without overflowing or silting, "
        f"seamless aluminium gutters are sloped along the fascia board at a minimum gradient of 1 : 500 (2 mm fall per metre).\n\n"
        f"Calculate the TOTAL vertical fall (in millimetres) required for a straight gutter run of {_fmt(gutter_length_m, 1)} m."
    )

    correct_ans = f"{_fmt(total_fall_mm, 0)} mm"
    custom_opts = [
        correct_ans,
        f"{_fmt(total_fall_mm * 2, 0)} mm",
        f"{_fmt(total_fall_mm / 2, 0)} mm",
        f"{_fmt(gutter_length_m, 0)} mm",
    ]

    t1 = f"Multiply the length of the gutter ({_fmt(gutter_length_m, 1)} m) by 2 mm per metre."
    t2 = f"{_fmt(gutter_length_m, 1)} m × 2 mm/m."
    t3 = f"Total fall = {_fmt(gutter_length_m, 1)} × 2 = {_fmt(total_fall_mm, 0)} mm."

    explanation = [
        f"Step 1: State unit fall rate for 1 : 500 gradient = 1 000 mm ÷ 500 = 2 mm vertical drop per linear metre [1 Mark: Method].",
        f"Step 2: Multiply by total gutter run: {_fmt(gutter_length_m, 1)} m × 2 mm/m [1 Mark: Method].",
        f"Step 3: Total required gutter fall = {_fmt(total_fall_mm, 0)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_46",
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
