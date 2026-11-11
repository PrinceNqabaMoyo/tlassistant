"""Subskills 28 to 36: Scaled Drawing Calculations, Scale Selection & Rescaling for Grade 11 Mathematical Literacy."""
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


def generate_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Subskill 28: Convert actual real-world dimension (in metres) to drawing length on 1:50 scale (in cm)."""
    name = r.choice(SA_NAMES)
    real_m = r.choice([2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.5])
    # On 1:50: drawing_cm = real_m * 100 / 50 = real_m * 2
    drawing_cm = round(real_m * 2.0, 2)

    prompt = (
        f"{name} is drawing an architectural floor plan to a scale of 1:50. "
        f"A bedroom wall has an actual real-world length of {_fmt(real_m)} m.\n"
        f"What length (in centimetres) should {name} draw this wall on the paper?"
    )

    correct_ans = f"{_fmt(drawing_cm)} cm"
    wrong_1 = f"{_fmt(drawing_cm * 10)} cm"
    wrong_2 = f"{_fmt(drawing_cm * 0.5)} cm"
    wrong_3 = f"{_fmt(real_m)} cm"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Convert real dimension to centimetres [1 mark].\n"
        f"Real length = {_fmt(real_m)} m × 100 cm/m = {_fmt(real_m * 100)} cm.\n"
        f"Step 2: Divide by the scale denominator (50) [1 mark].\n"
        f"Drawing length = {_fmt(real_m * 100)} cm ÷ 50 = {_fmt(drawing_cm)} cm.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="28",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Drawing Length = Real Length ÷ Scale Factor.",
        tier_2=f"Convert {_fmt(real_m)} m to {_fmt(real_m * 100)} cm, then divide by 50.",
        tier_3=f"{_fmt(real_m * 100)} cm ÷ 50 = {_fmt(drawing_cm)} cm.",
        r=r,
    )


def generate_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Subskill 29: Convert actual real-world length to drawing length on 1:100 scale."""
    name = r.choice(SA_NAMES)
    real_m = r.choice([4.2, 5.6, 6.8, 7.5, 8.4, 9.6, 12.0, 15.0])
    # On 1:100: drawing_cm = real_m * 100 / 100 = real_m cm
    drawing_cm = round(real_m, 2)

    prompt = (
        f"A site plan for a school library is rendered at a scale ratio of 1:100. "
        f"The main exterior boundary wall is {_fmt(real_m)} m long in reality.\n"
        f"Calculate the length of the line representing this wall on the 1:100 drawing in centimetres."
    )

    correct_ans = f"{_fmt(drawing_cm)} cm"
    wrong_1 = f"{_fmt(drawing_cm * 10)} cm"
    wrong_2 = f"{_fmt(drawing_cm * 0.1)} cm"
    wrong_3 = f"{_fmt(drawing_cm * 2)} cm"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand scale 1:100 [1 mark].\n"
        f"1 cm on the plan represents 100 cm (which is exactly 1 m) in reality.\n"
        f"Step 2: Convert directly from metres to centimetres [1 mark].\n"
        f"Drawing length = {_fmt(real_m)} m × 1 cm/m = {_fmt(drawing_cm)} cm.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Site Plan Bar Scale (1:100, Wall {_fmt(real_m)} m)",
        "scale": "1 : 100",
        "segment_value_m": 1.0,
        "total_km": real_m / 1000,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="29",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="On a 1:100 scale, each 1 metre in reality corresponds to exactly 1 centimetre on paper.",
        tier_2=f"A real distance of {_fmt(real_m)} m is represented by {_fmt(drawing_cm)} cm.",
        tier_3=f"The drawing length is {_fmt(drawing_cm)} cm.",
        r=r,
    )


def generate_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Subskill 30: Convert actual real-world length to drawing length on 1:200 scale."""
    name = r.choice(SA_NAMES)
    real_m = r.choice([10.0, 14.0, 16.0, 20.0, 24.0, 28.0, 32.0, 40.0])
    # On 1:200: drawing_cm = real_m * 100 / 200 = real_m * 0.5
    drawing_cm = round(real_m * 0.5, 2)

    prompt = (
        f"An overall property site layout is rendered at a scale ratio of 1:200. "
        f"The street boundary fence has an actual length of {_fmt(real_m)} m.\n"
        f"Calculate the length (in centimetres) that represents this fence on the 1:200 scale layout."
    )

    correct_ans = f"{_fmt(drawing_cm)} cm"
    wrong_1 = f"{_fmt(drawing_cm * 2)} cm"
    wrong_2 = f"{_fmt(drawing_cm * 10)} cm"
    wrong_3 = f"{_fmt(real_m)} cm"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Convert real length to centimetres [1 mark].\n"
        f"Real length = {_fmt(real_m)} m × 100 cm/m = {_fmt(real_m * 100)} cm.\n"
        f"Step 2: Divide by scale factor 200 [1 mark].\n"
        f"Drawing length = {_fmt(real_m * 100)} cm ÷ 200 = {_fmt(drawing_cm)} cm.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Site Layout Bar Scale (1:200, Fence {_fmt(real_m)} m)",
        "scale": "1 : 200",
        "segment_value_m": 2.0,
        "total_km": real_m / 1000,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="30",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="On a 1:200 scale, divide the real distance in cm by 200.",
        tier_2=f"{_fmt(real_m)} m = {_fmt(real_m * 100)} cm. Divide by 200 to get the drawing length.",
        tier_3=f"{_fmt(real_m * 100)} cm ÷ 200 = {_fmt(drawing_cm)} cm.",
        r=r,
    )


def generate_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Subskill 31: Measure line on a plan using a graphic bar scale."""
    name = r.choice(SA_NAMES)
    bar_seg_cm = r.choice([2.0, 2.5, 3.0])  # length of one bar segment in cm
    bar_seg_m = r.choice([5.0, 10.0])       # real distance represented by one segment

    measured_line_cm = r.choice([4.0, 5.0, 6.0, 7.5, 8.0])
    # segments = measured_line_cm / bar_seg_cm
    # real_dist = segments * bar_seg_m
    real_dist = round((measured_line_cm / bar_seg_cm) * bar_seg_m, 2)

    diagram_spec = {
        "diagram_role": "context",
        "diagram_type": "bar_scale",
        "title": "Graphic Bar Scale",
        "segment_length_cm": bar_seg_cm,
        "segment_value_m": bar_seg_m,
        "measured_line_cm": measured_line_cm,
    }

    prompt = (
        f"A floor plan features a graphic bar scale where a {_fmt(bar_seg_cm)} cm bar segment represents "
        f"{_fmt(bar_seg_m)} metres in reality. "
        f"{name} measures the length of a driveway on the plan and finds it is {_fmt(measured_line_cm)} cm long.\n"
        f"Using the bar scale, calculate the actual real-world length of the driveway in metres."
    )

    correct_ans = f"{_fmt(real_dist)} m"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Determine the scale ratio per centimetre [1 mark].\n"
        f"1 cm on the plan represents {_fmt(bar_seg_m)} m ÷ {_fmt(bar_seg_cm)} cm = {_fmt(bar_seg_m / bar_seg_cm, 2)} m in reality.\n"
        f"Step 2: Multiply by the measured drawing length [1 mark].\n"
        f"Real distance = {_fmt(measured_line_cm)} cm × ({_fmt(bar_seg_m)} m ÷ {_fmt(bar_seg_cm)} cm) = {_fmt(real_dist)} m.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="31",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine how many real metres each centimetre on the bar represents, then multiply by the measured length.",
        tier_2=f"Scale factor = {_fmt(bar_seg_m)} m ÷ {_fmt(bar_seg_cm)} cm. Multiply this by {_fmt(measured_line_cm)} cm.",
        tier_3=f"Driveway length = {_fmt(real_dist)} m.",
        r=r,
        diagram_spec=diagram_spec,
    )


def generate_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Subskill 32: Select the most suitable scale to fit a building on standard paper (A4 / A3)."""
    name = r.choice(SA_NAMES)
    paper = r.choice(["A4 (usable printable area: 260 mm × 180 mm)", "A3 (usable printable area: 380 mm × 260 mm)"])
    usable_l_mm = 260 if "A4" in paper else 380
    usable_w_mm = 180 if "A4" in paper else 260

    # Building dimensions in metres
    bld_l_m = r.choice([15.0, 18.0, 20.0, 24.0])
    bld_w_m = r.choice([8.0, 10.0, 12.0])

    # Check scales: 1:50, 1:100, 1:200, 1:500
    # On 1:50: length = bld_l_m * 1000 / 50 = bld_l_m * 20 mm
    # On 1:100: length = bld_l_m * 10 mm
    # On 1:200: length = bld_l_m * 5 mm
    if "A4" in paper:
        # If building is 18m: on 1:50 = 360mm (exceeds 260mm). On 1:100 = 180mm <= 260mm, width 10m = 100mm <= 180mm.
        # So 1:100 is best (fits with good detail, whereas 1:50 is too big and 1:500 is unnecessarily tiny).
        best_scale = "1:100"
        reason = f"At 1:50 the building would measure {_fmt(bld_l_m * 20)} mm (too large for {_fmt(usable_l_mm)} mm printable space), whereas 1:100 fits comfortably at {_fmt(bld_l_m * 10)} mm × {_fmt(bld_w_m * 10)} mm"
    else:
        best_scale = "1:50" if bld_l_m <= 18.0 else "1:100"
        reason = f"It provides the maximum detail while fitting within the {_fmt(usable_l_mm)} mm × {_fmt(usable_w_mm)} mm printable boundary"

    prompt = (
        f"{name} needs to print a floor plan for a building measuring {_fmt(bld_l_m)} m by {_fmt(bld_w_m)} m "
        f"on {paper} with suitable margins.\n"
        f"Which standard architectural scale is the most appropriate choice to maximize detail while fitting completely on the page?"
    )

    correct_ans = f"{best_scale}"
    custom_opts = ["1:20", "1:50", "1:100", "1:500"]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate drawing dimensions at different candidate scales [1 mark].\n"
        f"At 1:50: Length = {_fmt(bld_l_m)} m ÷ 50 = {_fmt(bld_l_m * 20)} mm.\n"
        f"At 1:100: Length = {_fmt(bld_l_m)} m ÷ 100 = {_fmt(bld_l_m * 10)} mm; Width = {_fmt(bld_w_m * 10)} mm.\n"
        f"Step 2: Compare with printable paper bounds ({_fmt(usable_l_mm)} mm × {_fmt(usable_w_mm)} mm) [1 mark].\n"
        f"{reason}.\n"
        f"Step 3: Stated scale [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="32",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Test candidate scales to find the largest scale that does not exceed the page dimensions.",
        tier_2=f"Convert {_fmt(bld_l_m)} m to mm and divide by 50, 100, etc., to see which fits within {_fmt(usable_l_mm)} mm.",
        tier_3=f"The most appropriate scale is {best_scale}.",
        r=r,
    )


def generate_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Subskill 33: Convert number scale (1 : n) to verbal / sentence scale."""
    ratio = r.choice([50, 100, 200, 250, 500])
    # 1 cm represents ratio cm
    if ratio < 100:
        verbal_desc = f"1 cm on the plan represents {_fmt(ratio)} cm in reality"
    else:
        metres = ratio / 100
        verbal_desc = f"1 cm on the plan represents {_fmt(metres)} m in reality"

    prompt = (
        f"A floor plan indicates a number scale of 1 : {_fmt(ratio)}.\n"
        f"Which statement correctly translates this number scale into a verbal (sentence) scale?"
    )

    correct_ans = verbal_desc
    distractors = [
        f"1 cm on the plan represents {_fmt(ratio * 10)} m in reality",
        f"1 metre on the plan represents {_fmt(ratio)} cm in reality",
        f"1 cm on the plan represents {_fmt(ratio * 2)} cm in reality",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Understand number scale ratio 1 : {_fmt(ratio)} [1 mark].\n"
        f"1 unit on paper represents {_fmt(ratio)} of the exact same units in real life.\n"
        f"Step 2: Express in standard metric units [1 mark].\n"
        f"1 cm on paper represents {_fmt(ratio)} cm in reality ({_fmt(ratio / 100)} m).\n"
        f"Step 3: Stated sentence scale [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Number Scale (1 : {ratio})",
        "scale": f"1 : {ratio}",
        "segment_value_m": ratio / 100 if ratio >= 100 else 1.0,
        "total_km": 1.0,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="33",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="In a number scale 1 : n, both numbers use the exact same unit.",
        tier_2=f"1 cm on paper represents {_fmt(ratio)} cm in real life (divide by 100 to get metres).",
        tier_3=f"Verbal scale: {verbal_desc}.",
        r=r,
    )


def generate_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Subskill 34: Scaled area relationship: area scale factor is 1 : n²."""
    scale_n = r.choice([50, 100, 200])
    area_factor = scale_n ** 2

    drawing_area_cm2 = r.choice([12.0, 15.0, 20.0, 24.0, 30.0])
    # Real area in cm² = drawing_area_cm2 * area_factor
    # Real area in m² = drawing_area_cm2 * area_factor / 10000
    real_area_m2 = round(drawing_area_cm2 * (scale_n / 100) ** 2, 2)

    prompt = (
        f"Refer to the scaled room drawing shown in the diagram with scale ratio 1 : {_fmt(scale_n)}, "
        f"where the room measures {_fmt(drawing_area_cm2)} cm² on paper.\n"
        f"Calculate the actual real-world floor area of this room in square metres (m²)."
    )

    correct_ans = f"{_fmt(real_area_m2)} m²"
    wrong_1 = f"{_fmt(drawing_area_cm2 * scale_n / 100)} m²"  # forgot to square scale
    wrong_2 = f"{_fmt(real_area_m2 * 10)} m²"
    wrong_3 = f"{_fmt(real_area_m2 * 0.1)} m²"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand the area scale factor [1 mark].\n"
        f"When linear dimensions are scaled by 1 : {scale_n}, areas are scaled by (1 : {scale_n})² = 1 : {scale_n}² = 1 : {_fmt(area_factor)}.\n"
        f"Step 2: Multiply drawing area by {scale_n}² [1 mark].\n"
        f"Real area in cm² = {_fmt(drawing_area_cm2)} cm² × {_fmt(area_factor)} = {_fmt(drawing_area_cm2 * area_factor)} cm².\n"
        f"Step 3: Convert cm² to m² (divide by 10 000) [1 mark].\n"
        f"Real area in m² = {_fmt(drawing_area_cm2 * area_factor)} ÷ 10 000 = {_fmt(real_area_m2)} m² ({correct_ans})."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "title": f"Scaled Room Plan (1:{scale_n}, Area {drawing_area_cm2} cm² - Opt {r.randint(1, 9)})",
        "length": scale_n / 10,
        "width": scale_n / 10,
        "shape": "scaled_room",
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="34",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember that area scaling uses the square of the linear scale factor: (scale factor)².",
        tier_2=f"Multiply drawing area by ({scale_n})² = {_fmt(area_factor)}, then divide by 10 000 to convert from cm² to m².",
        tier_3=f"Real area = {_fmt(real_area_m2)} m².",
        r=r,
    )


def generate_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Subskill 35: Measurement error propagation from scale drawing."""
    name = r.choice(SA_NAMES)
    scale = r.choice([50, 100, 200])
    error_mm = r.choice([1.5, 2.0, 3.0])

    real_error_mm = error_mm * scale
    real_error_m = round(real_error_mm / 1000, 2)

    prompt = (
        f"{name} measures a wall on an architectural drawing with a scale of 1 : {_fmt(scale)}. "
        f"Due to an imperfect ruler alignment, {name}'s measurement is off by {_fmt(error_mm)} mm on the paper.\n"
        f"What is the resulting error in the calculated real-world length of the wall in metres?"
    )

    correct_ans = f"{_fmt(real_error_m)} m (or {_fmt(int(real_error_mm))} mm)"
    wrong_1 = f"{_fmt(error_mm)} m"
    wrong_2 = f"{_fmt(real_error_m * 10)} m"
    wrong_3 = f"{_fmt(real_error_m * 0.1)} m"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Multiply drawing error by the scale factor [1 mark].\n"
        f"Real error in mm = {_fmt(error_mm)} mm × {_fmt(scale)} = {_fmt(real_error_mm)} mm.\n"
        f"Step 2: Convert to metres (divide by 1 000) [1 mark].\n"
        f"Real error in metres = {_fmt(real_error_mm)} ÷ 1 000 = {_fmt(real_error_m)} m.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="35",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the paper measurement error by the scale factor.",
        tier_2=f"{_fmt(error_mm)} mm × {_fmt(scale)} = {_fmt(real_error_mm)} mm.",
        tier_3=f"Divide by 1 000 to get {_fmt(real_error_m)} m.",
        r=r,
    )


def generate_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Subskill 36: Rescaling impact on Number Scale vs Graphic Bar Scale."""
    prompt = (
        f"An architectural floor plan with both a number scale (1:100) and a graphic bar scale "
        f"is photocopied and enlarged from A4 paper to A3 paper (a 141% enlargement).\n"
        f"Which statement correctly describes how this enlargement affects both scales?"
    )

    correct_ans = (
        "The bar scale enlarges in exact proportion with the drawing and remains 100% accurate, whereas the printed ratio '1:100' becomes invalid"
    )
    wrong_1 = "Both the bar scale and the number scale remain completely accurate without any change"
    wrong_2 = "The number scale remains 100% accurate, but the bar scale becomes invalid and misleading"
    wrong_3 = "Both scales become completely invalid and neither can ever be used again"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Analyze how graphic bar scale behaves during enlargement [1 mark].\n"
        f"Because the bar scale is part of the graphic image, it stretches by the exact same 141% factor as the building walls, keeping the relationship intact.\n"
        f"Step 2: Analyze how static number scale text behaves [1 mark].\n"
        f"The printed text '1:100' does not automatically update its numbers, so 1 cm on the new enlarged sheet no longer represents 100 cm in reality.\n"
        f"Step 3: Conclude comparative validity [1 mark]: {correct_ans}."
    )

    d_spec = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"A4 to A3 Rescaling Graphic Bar Scale (Factor {r.choice([141, 150, 200])}%)",
        "scale": "1 : 100",
        "segment_value_m": 1.0,
        "total_km": 0.05,
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id="36",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Consider what happens to printed image bars vs static text numbers when enlarged.",
        tier_2="A graphic bar scale grows with the drawing, so its segments maintain the exact proportional scale.",
        tier_3=f"Correct conclusion: {correct_ans}.",
        r=r,
    )
