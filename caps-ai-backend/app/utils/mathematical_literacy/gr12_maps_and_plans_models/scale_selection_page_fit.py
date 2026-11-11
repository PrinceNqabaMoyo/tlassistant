"""Subskills 01-08: Scale Selection & Page Fit for Grade 12 Maps and Plans (Models)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    PAGE_SIZES_MM,
    SA_BUILDING_PROJECTS,
    SA_NAMES,
    STANDARD_MODEL_SCALES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def gen_subskill_01(r: random.Random) -> Dict[str, Any]:
    """Subskill 01: Comparing model scales to identify the largest scale with reason."""
    scales = r.sample([10, 20, 25, 50, 80, 100, 200, 500], 3)
    scales.sort()
    smallest_denom = scales[0]
    largest_scale_str = f"1 : {smallest_denom}"

    prompt = (
        f"Refer to the model scale comparison shown in the diagram. "
        f"A learner is deciding on an architectural scale to build a physical 3D model, "
        f"considering three candidate scales: 1 : {scales[0]}, 1 : {scales[1]}, and 1 : {scales[2]}.\n\n"
        f"Which of these scales represents the LARGEST scale, and what is the mathematical reason?"
    )
    d_spec_01 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Model Scale Comparison (1 : {scales[0]}, 1 : {scales[1]}, 1 : {scales[2]})",
        "ratio_str": largest_scale_str,
        "segments": [{"length_cm": 2.0, "real_val": smallest_denom * 2 / 100, "unit": "m"}],
    }

    correct_ans = f"1 : {smallest_denom}, because the scale factor has the smallest denominator, producing the largest model"
    custom_opts = [
        correct_ans,
        f"1 : {scales[2]}, because {scales[2]} is the largest number and represents the greatest reduction",
        f"1 : {scales[1]}, because it offers an average middle reduction factor",
        f"1 : {smallest_denom}, because it requires fewer calculations than larger numbers",
    ]

    t1 = "Recall that in ratio scales 1 : x, a smaller denominator x means the representation is closer to actual size."
    t2 = f"Compare the fractions: 1/{scales[0]} is greater than 1/{scales[2]}."
    t3 = f"The largest fraction is 1/{smallest_denom}, meaning 1 cm on the model represents only {smallest_denom} cm in reality, producing the largest physical model."

    explanation = [
        f"Step 1: Express scales as unit fractions: 1/{scales[0]}, 1/{scales[1]}, and 1/{scales[2]} [1 Mark: Method].",
        f"Step 2: 1/{smallest_denom} has the smallest denominator, so it is the largest fractional value [1 Mark: Method].",
        f"Step 3: Therefore, 1 : {smallest_denom} is the largest scale, producing the largest and most detailed model [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_01",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_01,
    )


def gen_subskill_02(r: random.Random) -> Dict[str, Any]:
    """Subskill 02: Best scale selection to fit a building floor plan onto an A4 page."""
    name = r.choice(SA_NAMES)
    project = r.choice(SA_BUILDING_PROJECTS)
    real_l_m = project["real_length_m"]
    real_w_m = project["real_width_m"]

    # Candidate scales: 1:20, 1:50, 1:100
    candidate_scales = [20, 50, 100]
    # Check A4 page: length 29.7 cm, width 21.0 cm
    # At 1:20 -> real_l_m * 100 / 20. If real_l_m=7.5m -> 750/20 = 37.5 cm (too big for 29.7)
    # At 1:50 -> 750/50 = 15 cm, 540/50 = 10.8 cm (fits nicely!)
    # At 1:100 -> 7.5 cm x 5.4 cm (fits, but 1:50 is larger and shows more detail)
    valid_scale = None
    for s in candidate_scales:
        ml = (real_l_m * 100.0) / s
        mw = (real_w_m * 100.0) / s
        if ml <= 28.0 and mw <= 19.5:  # with margin
            valid_scale = s
            break
    if not valid_scale:
        valid_scale = 100

    ml_cm = (real_l_m * 100.0) / valid_scale
    mw_cm = (real_w_m * 100.0) / valid_scale

    prompt = (
        f"Refer to the A4 page layout shown in the diagram. "
        f"{name} wants to draw a 2D floor plan for a {project['type']} to fit comfortably on an A4 page "
        f"(29,7 cm long and 21,0 cm wide in landscape orientation). "
        f"The building measures {_fmt(real_l_m, 1)} m long by {_fmt(real_w_m, 1)} m wide.\\n\\n"
        f"Which of the following scales is the MOST APPROPRIATE scale to show maximum detail while fitting on the A4 page?\\n"
        f"Scales to evaluate: 1 : 20, 1 : 50, or 1 : 100."
    )
    d_spec_02 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"A4 Page Fit ({project['type']}: {_fmt(real_l_m, 1)} m × {_fmt(real_w_m, 1)} m)",
        "rooms": [{"name": project["type"], "length": real_l_m, "width": real_w_m}],
    }

    correct_ans = f"1 : {valid_scale} (Plan size: {_fmt(ml_cm, 1)} cm × {_fmt(mw_cm, 1)} cm)"
    alt_scales = [s for s in [10, 20, 50, 100, 200] if s != valid_scale][:4]
    custom_opts = [correct_ans] + [
        f"1 : {s} (Plan size: {_fmt((real_l_m * 100) / s, 1)} cm × {_fmt((real_w_m * 100) / s, 1)} cm)"
        for s in alt_scales
    ]

    t1 = "Convert real dimensions from metres to centimetres (multiply by 100)."
    t2 = "Divide real dimensions in cm by each scale factor to find the drawing dimensions."
    t3 = f"1 : 20 produces a plan that exceeds the 29,7 cm page length. 1 : {valid_scale} fits ({_fmt(ml_cm, 1)} cm ≤ 29,7 cm) while maximizing detail."

    explanation = [
        f"Step 1: Convert real dimensions to cm: Length = {_fmt(real_l_m * 100, 0)} cm, Width = {_fmt(real_w_m * 100, 0)} cm [1 Mark: Method].",
        f"Step 2: Test 1 : {valid_scale}: Length on plan = {_fmt(real_l_m * 100, 0)} ÷ {valid_scale} = {_fmt(ml_cm, 1)} cm; Width = {_fmt(real_w_m * 100, 0)} ÷ {valid_scale} = {_fmt(mw_cm, 1)} cm [1 Mark: Method].",
        f"Step 3: Both dimensions fit within the 29,7 cm × 21,0 cm page with sufficient margin for maximum detail [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_02",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_02,
    )


def gen_subskill_03(r: random.Random) -> Dict[str, Any]:
    """Subskill 03: Best scale selection to fit a large structure onto an A3 poster board."""
    name = r.choice(SA_NAMES)
    length_m = r.choice([16.0, 18.0, 20.0, 24.0])
    width_m = r.choice([10.0, 12.0, 14.0])

    # A3 size: 42.0 cm x 29.7 cm
    # Test 1:50: length = length_m * 100 / 50 = length_m * 2. E.g. 18m -> 36 cm (fits in 42cm). Width = 12m * 2 = 24 cm (fits in 29.7 cm).
    # Test 1:25: length = length_m * 4 = 72 cm (way too big).
    # Test 1:100: length = 18 cm, width = 12 cm (fits, but 1:50 is much more detailed).
    chosen_scale = 50 if (length_m * 2.0 <= 40.0 and width_m * 2.0 <= 28.0) else 100
    plan_l = (length_m * 100.0) / chosen_scale
    plan_w = (width_m * 100.0) / chosen_scale

    prompt = (
        f"Refer to the A3 display board layout shown in the diagram. "
        f"{name} is preparing an exhibition model for a community sports hall measuring {_fmt(length_m, 1)} m long "
        f"by {_fmt(width_m, 1)} m wide on an A3 poster board (42,0 cm × 29,7 cm).\\n\\n"
        f"Which scale is the MOST APPROPRIATE to maximize the physical model size while leaving at least a 1 cm margin around all edges?"
    )
    d_spec_03 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"A3 Display Board Fit ({_fmt(length_m, 1)} m × {_fmt(width_m, 1)} m)",
        "rooms": [{"name": "Community Sports Hall", "length": length_m, "width": width_m}],
    }

    correct_ans = f"1 : {chosen_scale} (Model footprint: {_fmt(plan_l, 1)} cm × {_fmt(plan_w, 1)} cm)"
    custom_opts = [
        correct_ans,
        f"1 : 25 (Model footprint: {_fmt((length_m * 100) / 25, 1)} cm × {_fmt((width_m * 100) / 25, 1)} cm)",
        f"1 : 200 (Model footprint: {_fmt((length_m * 100) / 200, 1)} cm × {_fmt((width_m * 100) / 200, 1)} cm)",
        f"1 : 10 (Model footprint: {_fmt((length_m * 100) / 10, 1)} cm × {_fmt((width_m * 100) / 10, 1)} cm)",
    ]

    t1 = "Convert the sports hall dimensions from metres to centimetres."
    t2 = "Divide the real dimensions in cm by each candidate scale."
    t3 = f"At 1 : {chosen_scale}, length is {_fmt(plan_l, 1)} cm and width is {_fmt(plan_w, 1)} cm, which fits within the 42,0 cm × 29,7 cm board."

    explanation = [
        f"Step 1: Real dimensions in cm: Length = {_fmt(length_m * 100, 0)} cm, Width = {_fmt(width_m * 100, 0)} cm [1 Mark: Method].",
        f"Step 2: Scale 1 : {chosen_scale}: Model length = {_fmt(length_m * 100, 0)} ÷ {chosen_scale} = {_fmt(plan_l, 1)} cm; Model width = {_fmt(width_m * 100, 0)} ÷ {chosen_scale} = {_fmt(plan_w, 1)} cm [1 Mark: Method].",
        f"Step 3: Footprint {_fmt(plan_l, 1)} cm × {_fmt(plan_w, 1)} cm fits within A3 board (42,0 cm × 29,7 cm) with ample margins [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_03",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_03,
    )


def gen_subskill_04(r: random.Random) -> Dict[str, Any]:
    """Subskill 04: Minimum baseboard dimensions with perimeter lawn/pavement border."""
    name = r.choice(SA_NAMES)
    scale = r.choice([50, 100])
    real_l = r.choice([8.0, 10.0, 12.0, 15.0])
    real_w = r.choice([6.0, 7.5, 8.0])
    border_cm = r.choice([3.0, 4.0, 5.0])

    model_l_cm = (real_l * 100.0) / scale
    model_w_cm = (real_w * 100.0) / scale

    # Baseboard needs border on both sides (left + right, front + back)
    board_l_cm = model_l_cm + (2 * border_cm)
    board_w_cm = model_w_cm + (2 * border_cm)

    prompt = (
        f"{name} is constructing a 3D architectural model of a clinic building at a scale of 1 : {scale}.\n"
        f"The real building measures {_fmt(real_l, 1)} m in length and {_fmt(real_w, 1)} m in width.\n"
        f"To display surrounding landscaping, the wooden baseboard must extend {_fmt(border_cm, 1)} cm beyond the building on ALL four sides.\n\n"
        f"What are the MINIMUM length and width dimensions required for the display baseboard?"
    )

    correct_ans = f"{_fmt(board_l_cm, 1)} cm × {_fmt(board_w_cm, 1)} cm"
    custom_opts = [
        correct_ans,
        f"{_fmt(model_l_cm + border_cm, 1)} cm × {_fmt(model_w_cm + border_cm, 1)} cm",
        f"{_fmt(model_l_cm, 1)} cm × {_fmt(model_w_cm, 1)} cm",
        f"{_fmt(board_l_cm * 1.2, 1)} cm × {_fmt(board_w_cm * 1.2, 1)} cm",
    ]

    t1 = "First find the model's footprint by dividing real dimensions (in cm) by the scale denominator."
    t2 = f"Remember that the border extends on BOTH opposite sides, so add 2 × {_fmt(border_cm, 1)} cm = {_fmt(2 * border_cm, 1)} cm to both length and width."
    t3 = f"Model length = {_fmt(model_l_cm, 1)} cm. Baseboard length = {_fmt(model_l_cm, 1)} + {_fmt(2 * border_cm, 1)} = {_fmt(board_l_cm, 1)} cm. Model width = {_fmt(model_w_cm, 1)} cm. Baseboard width = {_fmt(model_w_cm, 1)} + {_fmt(2 * border_cm, 1)} = {_fmt(board_w_cm, 1)} cm."

    explanation = [
        f"Step 1: Calculate model building footprint: Length = ({_fmt(real_l, 1)} × 100) ÷ {scale} = {_fmt(model_l_cm, 1)} cm; Width = ({_fmt(real_w, 1)} × 100) ÷ {scale} = {_fmt(model_w_cm, 1)} cm [1 Mark: Method].",
        f"Step 2: Add border margin on both sides: Length margin = 2 × {_fmt(border_cm, 1)} cm = {_fmt(2 * border_cm, 1)} cm; Width margin = 2 × {_fmt(border_cm, 1)} cm = {_fmt(2 * border_cm, 1)} cm [1 Mark: Method].",
        f"Step 3: Total baseboard dimensions = {_fmt(board_l_cm, 1)} cm × {_fmt(board_w_cm, 1)} cm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_04",
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


def gen_subskill_05(r: random.Random) -> Dict[str, Any]:
    """Subskill 05: Calculating model height from elevation plan wall and roof apex."""
    scale = r.choice([25, 50, 100])
    wall_h_m = r.choice([2.6, 2.8, 3.0, 3.2])
    roof_h_m = r.choice([1.2, 1.4, 1.5, 1.8])
    total_real_h_m = wall_h_m + roof_h_m

    model_h_cm = (total_real_h_m * 100.0) / scale

    prompt = (
        f"Refer to the elevation plan shown in the diagram (scale ratio 1 : {scale}). "
        f"A residential building has a vertical wall height of {_fmt(wall_h_m, 2)} m "
        f"and a pitched roof with an apex height of {_fmt(roof_h_m, 2)} m above the wall (total height {_fmt(total_real_h_m, 2)} m).\\n\\n"
        f"If an architectural model is built at a scale of 1 : {scale}, what will be the TOTAL height of the model from base to roof apex, in centimetres?"
    )
    d_spec_05 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Cottage Model Height ({_fmt(total_real_h_m, 2)} m at Scale 1 : {scale})",
        "side": "Front",
        "elevation": "Front Elevation",
        "height_m": total_real_h_m,
        "roof": "pitched",
        "wall_height_m": wall_h_m,
        "roof_height_m": roof_h_m,
        "total_height_m": total_real_h_m,
    }

    correct_ans = f"{_fmt(model_h_cm, 2)} cm"
    custom_opts = [
        correct_ans,
        f"{_fmt((wall_h_m * 100.0) / scale, 2)} cm",
        f"{_fmt((total_real_h_m * 100.0) / (scale * 2), 2)} cm",
        f"{_fmt(model_h_cm * 10, 2)} cm",
    ]

    t1 = "Add the wall height and roof apex height together to find the total real-life vertical height."
    t2 = "Convert the total real height to centimetres, then divide by the scale denominator."
    t3 = f"Total real height = {_fmt(wall_h_m, 2)} m + {_fmt(roof_h_m, 2)} m = {_fmt(total_real_h_m, 2)} m = {_fmt(total_real_h_m * 100, 0)} cm. Model height = {_fmt(total_real_h_m * 100, 0)} ÷ {scale} = {_fmt(model_h_cm, 2)} cm."

    explanation = [
        f"Step 1: Total real vertical height = {_fmt(wall_h_m, 2)} m + {_fmt(roof_h_m, 2)} m = {_fmt(total_real_h_m, 2)} m = {_fmt(total_real_h_m * 100, 0)} cm [1 Mark: Method].",
        f"Step 2: Apply scale 1 : {scale}: Height on model = {_fmt(total_real_h_m * 100, 0)} ÷ {scale} [1 Mark: Method].",
        f"Step 3: Total model height = {_fmt(model_h_cm, 2)} cm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_05",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_05,
    )


def gen_subskill_06(r: random.Random) -> Dict[str, Any]:
    """Subskill 06: Checking whether chosen scale reveals sufficient detail vs unmanageable size."""
    scales = [
        {"scale": "1 : 500", "size": "too small to discern window frames, doors, or internal partition walls"},
        {"scale": "1 : 5", "size": "too huge and unwieldy to build or transport on a standard desk"},
        {"scale": "1 : 1 000", "size": "reduces an entire house to less than 1 cm, making 3D modeling impossible"},
    ]
    item = r.choice(scales)

    prompt = (
        f"Refer to the scale feasibility comparison diagram shown. "
        f"An architectural student suggests building a 3D model of a 7 m × 5 m RDP house using a scale of {item['scale']}.\\n\\n"
        f"Why is this scale unsuitable for demonstrating interior room layouts and window placements?"
    )
    v_denom = int(item["scale"].replace(" ", "").split(":")[-1].strip())
    d_spec_06 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Scale Detail vs Feasibility ({item['scale']})",
        "ratio_str": item["scale"],
        "segments": [{"length_cm": 2.0, "real_val": v_denom * 2 / 100, "unit": "m"}],
    }

    correct_ans = f"It is {item['size']}"
    custom_opts = [
        correct_ans,
        "It is illegal under South African National Building Regulations",
        "It produces negative dimensions during trigonometric conversions",
        "It violates the metric standard because ratio scales cannot be used for residential buildings",
    ]

    t1 = "Consider the physical size of 7 metres reduced by this scale."
    t2 = "A scale of 1 : 500 would make a 7 m house only 1,4 cm long, whereas 1 : 5 would make it 1,4 metres long."
    t3 = f"The correct critique is that it is {item['size']}."

    explanation = [
        f"Step 1: Calculate the model size resulting from {item['scale']} [1 Mark: Method].",
        f"Step 2: Evaluate physical feasibility against typical architectural modeling requirements [1 Mark: Method].",
        f"Step 3: Conclude that the scale is unsuitable because it is {item['size']} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_06",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_06,
    )


def gen_subskill_07(r: random.Random) -> Dict[str, Any]:
    """Subskill 07: Converting real dimensions to model dimensions in mm and cm."""
    scale = r.choice([20, 25, 50])
    real_m = r.choice([2.5, 3.2, 4.0, 5.6, 6.4])
    real_mm = real_m * 1000.0
    model_mm = real_mm / scale
    model_cm = model_mm / 10.0

    prompt = (
        f"A carpenter is building a scale model of a roof truss at a scale of 1 : {scale}.\n"
        f"The real wooden tie-beam has a length of {_fmt(real_m, 2)} m.\n\n"
        f"Calculate the length of the model tie-beam in millimetres (mm)."
    )

    correct_ans = f"{_fmt(model_mm, 1)} mm"
    custom_opts = [
        correct_ans,
        f"{_fmt(model_cm, 1)} mm",
        f"{_fmt(model_mm * 10, 1)} mm",
        f"{_fmt(model_mm / 2.0, 1)} mm",
    ]

    t1 = "Convert the real length from metres to millimetres by multiplying by 1 000."
    t2 = f"Divide the real millimetres by the scale denominator ({scale})."
    t3 = f"Real length = {_fmt(real_m, 2)} m × 1 000 = {_fmt(real_mm, 0)} mm. Model length = {_fmt(real_mm, 0)} ÷ {scale} = {_fmt(model_mm, 1)} mm."

    explanation = [
        f"Step 1: Convert real length to mm: {_fmt(real_m, 2)} m × 1 000 = {_fmt(real_mm, 0)} mm [1 Mark: Method].",
        f"Step 2: Divide by scale factor {scale}: {_fmt(real_mm, 0)} mm ÷ {scale} [1 Mark: Method].",
        f"Step 3: Length on model = {_fmt(model_mm, 1)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_07",
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


def gen_subskill_08(r: random.Random) -> Dict[str, Any]:
    """Subskill 08: Reverse conversion: measuring model dimension with ruler to find real ground size."""
    scale = r.choice([20, 50, 100])
    measured_cm = r.choice([4.2, 5.5, 6.8, 8.4, 9.6])
    real_cm = measured_cm * scale
    real_m = real_cm / 100.0

    prompt = (
        f"On a completed architectural scale model built to a scale of 1 : {scale}, a learner measures the width "
        f"of a model veranda using a plastic ruler and finds it is exactly {_fmt(measured_cm, 1)} cm.\n\n"
        f"What is the ACTUAL real-life width of the veranda in metres (m)?"
    )

    correct_ans = f"{_fmt(real_m, 2)} m"
    custom_opts = [
        correct_ans,
        f"{_fmt(real_cm, 1)} m",
        f"{_fmt(real_m / 10.0, 2)} m",
        f"{_fmt(measured_cm / scale, 2)} m",
    ]

    t1 = f"Multiply the measured model length in cm by the scale denominator ({scale})."
    t2 = "Convert the resulting actual length from centimetres to metres by dividing by 100."
    t3 = f"Actual cm = {_fmt(measured_cm, 1)} cm × {scale} = {_fmt(real_cm, 1)} cm. In metres = {_fmt(real_cm, 1)} ÷ 100 = {_fmt(real_m, 2)} m."

    explanation = [
        f"Step 1: Multiply model measurement by scale factor: {_fmt(measured_cm, 1)} cm × {scale} = {_fmt(real_cm, 1)} cm [1 Mark: Method].",
        f"Step 2: Convert cm to metres: {_fmt(real_cm, 1)} cm ÷ 100 [1 Mark: Method].",
        f"Step 3: Actual real-life width = {_fmt(real_m, 2)} m [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_08",
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
