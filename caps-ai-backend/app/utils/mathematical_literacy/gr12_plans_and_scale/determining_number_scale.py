"""Subskills 01-08: Determining Number Scales & Conversions for Grade 12 Plans & Scale."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_BUILDING_EXAMPLES,
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def gen_subskill_01(r: random.Random) -> Dict[str, Any]:
    """Subskill 01: Determining scale 1:x from measured plan length (cm) and real length (m)."""
    # Authentic textbook example: e.g. 5.0 cm on plan represents 2.0 m or 2.5 m in real life
    measured_cm = r.choice([4.0, 5.0, 6.0, 8.0])
    real_m = r.choice([2.0, 2.5, 3.0, 4.0])
    real_cm = real_m * 100.0
    scale_denom = int(round(real_cm / measured_cm))

    prompt = (
        f"Refer to the cottage plan measurement shown in the diagram. "
        f"The external wall measures {_fmt(measured_cm, 1)} cm on paper, "
        f"while the actual real-life length on site is {_fmt(real_m, 1)} m.\n\n"
        f"Calculate the scale of the plan in the standard ratio format 1 : x."
    )
    d_spec_01 = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "title": f"Cottage Wall Plan Measurement ({_fmt(measured_cm, 1)} cm)",
        "shape": "rectangle",
        "width": measured_cm * 10,
        "height": 20,
        "labels": {"width": f"{_fmt(measured_cm, 1)} cm", "real": f"Actual {_fmt(real_m, 1)} m"},
    }

    correct_ans = f"1 : {scale_denom}"
    custom_opts = [
        correct_ans,
        f"1 : {scale_denom * 2}",
        f"1 : {scale_denom // 2 if scale_denom > 20 else scale_denom + 25}",
        f"1 : {scale_denom + 15}",
        f"1 : {scale_denom - 15 if scale_denom > 30 else scale_denom + 35}",
    ]

    t1 = "Convert the real-life measurement from metres to centimetres (multiply by 100)."
    t2 = f"Divide the real-life centimetres by the plan measurement in centimetres: ({_fmt(real_m, 1)} × 100) ÷ {_fmt(measured_cm, 1)}."
    t3 = f"Real cm = {_fmt(real_cm, 0)} cm. Denominator x = {_fmt(real_cm, 0)} ÷ {_fmt(measured_cm, 1)} = {scale_denom}. Scale = 1 : {scale_denom}."

    explanation = [
        f"Step 1: Convert real distance to cm: {_fmt(real_m, 1)} m × 100 = {_fmt(real_cm, 0)} cm [1 Mark: Method].",
        f"Step 2: Express ratio and simplify: Plan : Real = {_fmt(measured_cm, 1)} cm : {_fmt(real_cm, 0)} cm → Divide both sides by {_fmt(measured_cm, 1)} [1 Mark: Method].",
        f"Step 3: {_fmt(real_cm, 0)} ÷ {_fmt(measured_cm, 1)} = {scale_denom} → Scale = 1 : {scale_denom} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_01",
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
    """Subskill 02: Determining scale 1:x from roof height measurement on elevation view."""
    # Via Afrika textbook example (LB page 256): 2.9 cm measured for 3.53 m -> 353 / 2.9 = 121.7 -> approx 1:120
    measured_cm = 2.9
    real_m = 3.53
    real_cm = real_m * 100.0  # 353 cm
    exact_ratio = real_cm / measured_cm  # 121.72
    rounded_scale = 120

    measured_cm = r.choice([2.5, 2.9, 3.2, 3.5])
    real_m = r.choice([3.20, 3.53, 3.80, 4.20])
    real_cm = real_m * 100.0
    exact_ratio = real_cm / measured_cm
    rounded_scale = 100 if exact_ratio < 110 else (120 if exact_ratio < 135 else 150)

    prompt = (
        f"Refer to the South elevation plan shown in the diagram. The vertical height of the roof from eaves to ridge "
        f"measures exactly {_fmt(measured_cm, 1)} cm with a ruler on the drawing, "
        f"while the actual construction dimension is {_fmt(real_m, 2)} m.\n\n"
        f"Calculate the exact ratio scale (rounded to one decimal place), and state the nearest standard architectural scale."
    )
    d_spec_02 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"South Elevation Roof Ridge (Measured {_fmt(measured_cm, 1)} cm)",
        "side": "South",
        "elevation": "South Elevation",
        "height_m": real_m,
        "roof": "pitched",
        "roof_type": "pitched",
        "measured_height_cm": measured_cm,
        "real_height_m": real_m,
    }

    correct_ans = f"1 : {_fmt(exact_ratio, 1)} (≈ 1 : {rounded_scale})"
    custom_opts = [
        correct_ans,
        f"1 : 100 (≈ 1 : 100)",
        f"1 : 150 (≈ 1 : 150)",
        f"1 : {_fmt(exact_ratio * 0.8, 1)} (≈ 1 : 100)",
    ]

    t1 = f"Convert the real measurement to cm: {_fmt(real_m, 2)} m × 100 = {_fmt(real_cm, 0)} cm."
    t2 = f"Divide real cm by plan cm: {_fmt(real_cm, 0)} ÷ {_fmt(measured_cm, 1)}."
    t3 = f"Scale = {_fmt(real_cm, 0)} ÷ {_fmt(measured_cm, 1)} = {_fmt(exact_ratio, 1)}, which rounds to standard 1 : {rounded_scale}."

    explanation = [
        f"Step 1: Convert real height to cm: {_fmt(real_m, 2)} m × 100 = {_fmt(real_cm, 0)} cm [1 Mark: Method].",
        f"Step 2: Divide real cm by measured plan cm: {_fmt(real_cm, 0)} ÷ {_fmt(measured_cm, 1)} = {_fmt(exact_ratio, 1)} [1 Mark: Method].",
        f"Step 3: State the exact and standard architectural scale: 1 : {_fmt(exact_ratio, 1)} (≈ 1 : {rounded_scale}) [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_02",
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
    """Subskill 03: Rounding calculated scale factor to nearest standard architectural scale."""
    calculated_denom = r.choice([48.6, 51.4, 98.2, 102.8, 196.4, 204.2])
    # Nearest standard: 50, 100, or 200
    if calculated_denom < 75:
        std_scale = 50
    elif calculated_denom < 150:
        std_scale = 100
    else:
        std_scale = 200

    prompt = (
        f"Refer to the drawing scale comparison diagram shown. Due to paper shrinkage and ruler measuring tolerances, "
        f"a learner calculates a scale ratio of 1 : {_fmt(calculated_denom, 1)} for an architectural plan.\n\n"
        f"To which standard commercial architectural drawing scale should this calculation be rounded, "
        f"and what accounts for the minor discrepancy?"
    )
    d_spec_03 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Drawing Scale Comparison (Calculated 1 : {_fmt(calculated_denom, 1)})",
        "ratio_str": f"1 : {std_scale}",
        "segments": [{"length_cm": 2.0, "real_val": std_scale * 2 / 100, "unit": "m"}],
    }

    correct_ans = f"1 : {std_scale}, with the difference caused by paper printing tolerances and manual ruler limits"
    custom_opts = [
        correct_ans,
        f"1 : {std_scale * 2}, because drawing scales always double in size when printed",
        f"1 : 10, because all South African domestic plans must use 1 : 10",
        f"1 : {int(calculated_denom)}, because scales must never be rounded under any circumstances",
    ]

    t1 = "Commercial plans are drawn to standard round intervals such as 1:20, 1:50, 1:100, 1:200, or 1:500."
    t2 = f"Determine which standard scale ({std_scale}) is nearest to {_fmt(calculated_denom, 1)}."
    t3 = f"{_fmt(calculated_denom, 1)} is closest to {std_scale}. The discrepancy is due to printing tolerances and manual ruler measurement."

    explanation = [
        f"Step 1: Identify standard commercial drawing scales (1:20, 1:50, 1:100, 1:200) [1 Mark: Method].",
        f"Step 2: Compare calculated ratio 1 : {_fmt(calculated_denom, 1)} against standard scales [1 Mark: Method].",
        f"Step 3: Round to 1 : {std_scale} and provide the physical explanation [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_03",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_03,
    )


def gen_subskill_04(r: random.Random) -> Dict[str, Any]:
    """Subskill 04: Calculating ground distance from plan measurement and 1:50 scale."""
    scale = 50
    plan_cm = r.choice([5.4, 6.8, 7.5, 9.2, 11.6])
    real_cm = plan_cm * scale
    real_m = real_cm / 100.0

    prompt = (
        f"Refer to the residential floor plan shown in the diagram (scale ratio 1 : {scale}). "
        f"The bedroom window measures {_fmt(plan_cm, 1)} cm on paper.\n\n"
        f"Calculate the ACTUAL real-life length of the window in metres (m)."
    )
    d_spec_04 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Bedroom Window Plan Detail (Scale 1 : {scale})",
        "rooms": [{"name": "Bedroom", "width": plan_cm * 2, "length": plan_cm * 2}],
        "annotations": [{"text": f"Window: {_fmt(plan_cm, 1)} cm"}],
    }

    correct_ans = f"{_fmt(real_m, 2)} m"
    custom_opts = [
        correct_ans,
        f"{_fmt(real_cm, 1)} m",
        f"{_fmt(real_m / 10.0, 2)} m",
        f"{_fmt(plan_cm / scale, 2)} m",
    ]

    t1 = f"Multiply the plan measurement ({_fmt(plan_cm, 1)} cm) by the scale denominator ({scale})."
    t2 = "Convert the resulting actual length from centimetres to metres by dividing by 100."
    t3 = f"Real cm = {_fmt(plan_cm, 1)} × {scale} = {_fmt(real_cm, 1)} cm. Real metres = {_fmt(real_cm, 1)} ÷ 100 = {_fmt(real_m, 2)} m."

    explanation = [
        f"Step 1: Multiply by scale factor: {_fmt(plan_cm, 1)} cm × {scale} = {_fmt(real_cm, 1)} cm [1 Mark: Method].",
        f"Step 2: Convert cm to metres: {_fmt(real_cm, 1)} cm ÷ 100 [1 Mark: Method].",
        f"Step 3: Actual window length = {_fmt(real_m, 2)} m [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_04",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_04,
    )


def gen_subskill_05(r: random.Random) -> Dict[str, Any]:
    """Subskill 05: Calculating ground distance from plan measurement and 1:100 scale."""
    scale = 100
    plan_cm = r.choice([7.2, 8.5, 9.6, 12.0, 14.4])
    real_cm = plan_cm * scale
    real_m = real_cm / 100.0  # At 1:100, 1 cm on plan is 1 m in real life!

    prompt = (
        f"Refer to the municipal building plan shown in the diagram (scale ratio 1 : {scale}). "
        f"The front veranda measures {_fmt(plan_cm, 1)} cm on paper.\n\n"
        f"Calculate the actual ground length of the veranda in metres (m)."
    )
    d_spec_05 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Veranda Plan Detail (Scale 1 : {scale})",
        "rooms": [{"name": "Veranda", "width": plan_cm * 2, "length": 15}],
        "annotations": [{"text": f"Veranda: {_fmt(plan_cm, 1)} cm"}],
    }

    correct_ans = f"{_fmt(real_m, 2)} m"
    custom_opts = [
        correct_ans,
        f"{_fmt(real_m * 10, 2)} m",
        f"{_fmt(real_m / 2, 2)} m",
        f"{_fmt(plan_cm * 10, 1)} m",
    ]

    t1 = f"At a scale of 1 : 100, 1 cm on the drawing represents exactly 100 cm (or 1 metre) in real life."
    t2 = f"Therefore, {_fmt(plan_cm, 1)} cm on the plan equals {_fmt(plan_cm, 1)} metres in real life."
    t3 = f"Actual distance = {_fmt(plan_cm, 1)} cm × 100 = {_fmt(real_cm, 0)} cm = {_fmt(real_m, 2)} m."

    explanation = [
        f"Step 1: State relationship: At 1 : 100, 1 cm represents 100 cm = 1 m [1 Mark: Method].",
        f"Step 2: Multiply: {_fmt(plan_cm, 1)} × 1 m = {_fmt(real_m, 2)} m [1 Mark: Method].",
        f"Step 3: Actual ground length = {_fmt(real_m, 2)} m [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_05",
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
    """Subskill 06: Calculating ground distance from plan measurement and 1:200 site plan scale."""
    scale = 200
    plan_cm = r.choice([8.0, 11.5, 14.5, 17.0, 22.5])
    real_cm = plan_cm * scale
    real_m = real_cm / 100.0

    prompt = (
        f"Refer to the municipal erf site plan shown in the diagram (scale ratio 1 : {scale}). "
        f"The distance between the rear boundary wall and the back of the house measures {_fmt(plan_cm, 1)} cm on paper.\n\n"
        f"Calculate the actual ground distance in metres (m)."
    )
    d_spec_06 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Erf Site Plan (Scale 1 : {scale})",
        "dimensions": {"width_m": 80, "length_m": 120},
        "rooms": [{"name": "Stand Boundary", "width": 80, "length": 120}],
        "boundary": {"width": 80, "length": 120},
        "annotations": [{"text": f"Rear distance: {_fmt(plan_cm, 1)} cm"}],
    }

    correct_ans = f"{_fmt(real_m, 2)} m"
    custom_opts = [
        correct_ans,
        f"{_fmt(real_m / 2, 2)} m",
        f"{_fmt(real_m * 2, 2)} m",
        f"{_fmt(real_cm, 1)} m",
    ]

    t1 = f"Multiply the plan distance ({_fmt(plan_cm, 1)} cm) by {scale}."
    t2 = "Divide the result by 100 to convert to metres."
    t3 = f"Real cm = {_fmt(plan_cm, 1)} × {scale} = {_fmt(real_cm, 0)} cm. In metres = {_fmt(real_cm, 0)} ÷ 100 = {_fmt(real_m, 2)} m."

    explanation = [
        f"Step 1: Multiply by scale: {_fmt(plan_cm, 1)} cm × {scale} = {_fmt(real_cm, 0)} cm [1 Mark: Method].",
        f"Step 2: Convert cm to metres: {_fmt(real_cm, 0)} cm ÷ 100 [1 Mark: Method].",
        f"Step 3: Actual ground distance = {_fmt(real_m, 2)} m [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_06",
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
    """Subskill 07: Plan measurement in mm for a given ground distance at 1:50."""
    scale = 50
    real_m = r.choice([2.4, 3.2, 4.2, 5.0, 6.4])
    real_mm = real_m * 1000.0
    plan_mm = real_mm / scale

    prompt = (
        f"Refer to the kitchen layout plan shown in the diagram (scale ratio 1 : {scale}). "
        f"A row of kitchen floor cupboards has an actual ground length of {_fmt(real_m, 2)} m.\n\n"
        f"What should be the length of this cupboard unit on the drawing, in millimetres (mm)?"
    )
    d_spec_07 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Kitchen Cupboard Layout (Scale 1 : {scale})",
        "rooms": [{"name": "Kitchen", "width": 40, "length": 50}],
        "annotations": [{"text": f"Cupboard Ground: {_fmt(real_m, 2)} m"}],
    }

    correct_ans = f"{_fmt(plan_mm, 1)} mm"
    custom_opts = [
        correct_ans,
        f"{_fmt(plan_mm / 10.0, 1)} mm",
        f"{_fmt(plan_mm * 2, 1)} mm",
        f"{_fmt(real_m * 10, 1)} mm",
    ]

    t1 = "Convert the real ground length from metres to millimetres by multiplying by 1 000."
    t2 = f"Divide the millimetres by the scale factor of {scale}."
    t3 = f"Real mm = {_fmt(real_m, 2)} × 1 000 = {_fmt(real_mm, 0)} mm. Drawing mm = {_fmt(real_mm, 0)} ÷ {scale} = {_fmt(plan_mm, 1)} mm."

    explanation = [
        f"Step 1: Convert real length to mm: {_fmt(real_m, 2)} m × 1 000 = {_fmt(real_mm, 0)} mm [1 Mark: Method].",
        f"Step 2: Divide by scale factor {scale}: {_fmt(real_mm, 0)} mm ÷ {scale} [1 Mark: Method].",
        f"Step 3: Drawing length = {_fmt(plan_mm, 1)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_07",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_07,
    )


def gen_subskill_08(r: random.Random) -> Dict[str, Any]:
    """Subskill 08: Comparing precision limits of ruler measurement on small vs large scale plans."""
    var_plan_b = r.choice([200, 500, 1000])
    ground_mm_b = var_plan_b
    ground_cm_b = ground_mm_b // 10

    prompt = (
        f"Refer to the scale precision diagram shown. When taking manual measurements with a ruler graduated in 1 mm increments:\n"
        f"  - On Plan A (Scale ratio 1 : 50), a 1 mm measurement error corresponds to 50 mm (5 cm) on the ground.\n"
        f"  - On Plan B (Scale ratio 1 : {var_plan_b}), a 1 mm measurement error corresponds to {ground_mm_b} mm ({ground_cm_b} cm) on the ground.\n\n"
        f"What practical deduction must a builder make when extracting construction dimensions from small-scale plans?"
    )
    d_spec_08 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Scale Precision: Plan A (1 : 50) vs Plan B (1 : {var_plan_b})",
        "ratio_str": f"1 : 50 vs 1 : {var_plan_b}",
        "segments": [{"length_cm": 1.0, "real_val": 0.5, "unit": "m"}, {"length_cm": 1.0, "real_val": var_plan_b / 100, "unit": "m"}],
    }

    correct_ans = "Small-scale plans (1 : 500) magnify measurement error by a factor of 10; dimensions should always be taken from written figured dimensions rather than scaling with a ruler"
    custom_opts = [
        correct_ans,
        "Ruler measurements on 1 : 500 plans are 10 times more accurate than on 1 : 50 plans",
        "Builders are legally prohibited from reading any plans with scales smaller than 1 : 20",
        "Paper thickness automatically corrects measurement errors on small-scale drawings",
    ]

    t1 = "Consider how a 1 mm ruler error is magnified by the scale factor."
    t2 = "At 1:500, a 1 mm reading error equals 500 mm (half a metre!) in reality."
    t3 = "The standard architectural rule is: Never scale from a small-scale drawing; always verify written figured dimensions."

    explanation = [
        f"Step 1: Calculate real ground error: 1 mm × 50 = 50 mm (Plan A); 1 mm × 500 = 500 mm (Plan B) [1 Mark: Method].",
        f"Step 2: Compare magnification: Plan B has 10 times greater error vulnerability [1 Mark: Method].",
        f"Step 3: Conclude that figured written dimensions must be used instead of ruler scaling [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_08",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_08,
    )
