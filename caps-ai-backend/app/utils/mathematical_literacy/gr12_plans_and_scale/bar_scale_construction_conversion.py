"""Subskills 09-16: Bar Scale Construction & Conversion for Grade 12 Plans & Scale."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def gen_subskill_09(r: random.Random) -> Dict[str, Any]:
    """Subskill 09: Converting number scale 1:50 to a bar scale with 1 m segments."""
    # Scale 1:50 means 1 cm on plan represents 50 cm (0.5 m) in reality.
    # To represent 1.0 m: 100 cm / 50 = 2.0 cm on the bar scale!
    scale = 50
    segment_real_m = 1.0
    bar_segment_cm = (segment_real_m * 100.0) / scale

    scale = r.choice([40, 50, 60])
    bar_segment_cm = (segment_real_m * 100.0) / scale
    prompt = (
        f"Refer to the graphic bar scale shown in the diagram for an architectural plan (scale ratio 1 : {scale}). "
        f"The bar scale has major divisions representing {_fmt(segment_real_m, 1)} m ground intervals.\n\n"
        f"What distance (in centimetres) must separate each {_fmt(segment_real_m, 1)} m division on the ruler bar scale?"
    )
    d_spec_09 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Graphic Bar Scale (Scale 1 : {scale})",
        "ratio_str": f"1 : {scale}",
        "segments": [{"length_cm": bar_segment_cm, "real_val": segment_real_m, "unit": "m"}],
    }

    correct_ans = f"{_fmt(bar_segment_cm, 1)} cm per division"
    custom_opts = [
        correct_ans,
        f"{_fmt(bar_segment_cm * 2, 1)} cm per division",
        f"{_fmt(bar_segment_cm / 2, 1)} cm per division",
        f"1,0 cm per division",
    ]

    t1 = f"Convert {_fmt(segment_real_m, 1)} m to centimetres (multiply by 100)."
    t2 = f"Divide the centimetres by the scale factor of {scale}."
    t3 = f"Real cm = {_fmt(segment_real_m * 100, 0)} cm. Bar segment = {_fmt(segment_real_m * 100, 0)} ÷ {scale} = {_fmt(bar_segment_cm, 1)} cm."

    explanation = [
        f"Step 1: Convert ground interval to cm: {_fmt(segment_real_m, 1)} m = 100 cm [1 Mark: Method].",
        f"Step 2: Divide by scale factor {scale}: 100 cm ÷ {scale} = {_fmt(bar_segment_cm, 1)} cm [1 Mark: Method].",
        f"Step 3: Distance per division on the bar scale = {_fmt(bar_segment_cm, 1)} cm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_09",
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
    """Subskill 10: Converting number scale 1:100 to a bar scale with 2 m segments."""
    scale = 100
    segment_real_m = 2.0
    bar_segment_cm = (segment_real_m * 100.0) / scale

    scale = r.choice([80, 100, 120])
    bar_segment_cm = (segment_real_m * 100.0) / scale
    prompt = (
        f"Refer to the graphic bar scale shown in the diagram for an architectural floor plan (number scale 1 : {scale}). "
        f"The bar scale is marked in {_fmt(segment_real_m, 0)} m increments.\n\n"
        f"What length (in centimetres) should represent each {_fmt(segment_real_m, 0)} m interval on the drawing?"
    )
    d_spec_10 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Floor Plan Bar Scale (Scale 1 : {scale})",
        "ratio_str": f"1 : {scale}",
        "segments": [{"length_cm": bar_segment_cm, "real_val": segment_real_m, "unit": "m"}],
    }

    correct_ans = f"{_fmt(bar_segment_cm, 1)} cm"
    custom_opts = [
        correct_ans,
        f"{_fmt(bar_segment_cm * 2, 1)} cm",
        f"{_fmt(bar_segment_cm / 2, 1)} cm",
        f"5,0 cm",
    ]

    t1 = f"Convert {_fmt(segment_real_m, 0)} m to centimetres (200 cm)."
    t2 = f"Divide by the scale denominator ({scale})."
    t3 = f"200 cm ÷ 100 = {_fmt(bar_segment_cm, 1)} cm."

    explanation = [
        f"Step 1: Convert ground interval to cm: {_fmt(segment_real_m, 0)} m = 200 cm [1 Mark: Method].",
        f"Step 2: Divide by scale factor {scale}: 200 cm ÷ 100 = {_fmt(bar_segment_cm, 1)} cm [1 Mark: Method].",
        f"Step 3: Length per interval = {_fmt(bar_segment_cm, 1)} cm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_10",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_10,
    )


def gen_subskill_11(r: random.Random) -> Dict[str, Any]:
    """Subskill 11: Converting number scale 1:500 to a bar scale with 10 m increments."""
    # Via Afrika textbook question 1.1 (LB page 260)
    scale = 500
    segment_real_m = 10.0
    bar_segment_cm = (segment_real_m * 100.0) / scale

    scale = r.choice([400, 500, 600])
    bar_segment_cm = (segment_real_m * 100.0) / scale
    prompt = (
        f"Refer to the site development bar scale shown in the diagram (scale ratio 1 : {scale}). "
        f"The bar scale goes up in {_fmt(segment_real_m, 0)} m increments.\n\n"
        f"Calculate the physical length (in centimetres) of each {_fmt(segment_real_m, 0)} m division on the bar scale."
    )
    d_spec_11 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Site Plan Bar Scale (Scale 1 : {scale})",
        "ratio_str": f"1 : {scale}",
        "segments": [{"length_cm": bar_segment_cm, "real_val": segment_real_m, "unit": "m"}],
    }

    correct_ans = f"{_fmt(bar_segment_cm, 1)} cm"
    custom_opts = [
        correct_ans,
        f"{_fmt(bar_segment_cm * 2, 1)} cm",
        f"{_fmt(bar_segment_cm / 2, 1)} cm",
        f"5,0 cm",
    ]

    t1 = f"Convert {_fmt(segment_real_m, 0)} m to centimetres: {_fmt(segment_real_m, 0)} × 100 = 1 000 cm."
    t2 = f"Divide by the scale denominator ({scale}): 1 000 ÷ 500."
    t3 = f"1 000 cm ÷ 500 = {_fmt(bar_segment_cm, 1)} cm."

    explanation = [
        f"Step 1: A scale of 1 : {scale} means 1 cm represents {scale} cm = 5 m in real life [1 Mark: Method].",
        f"Step 2: To represent {_fmt(segment_real_m, 0)} m, calculate: 1 000 cm ÷ 500 = {_fmt(bar_segment_cm, 1)} cm [1 Mark: Method].",
        f"Step 3: Each {_fmt(segment_real_m, 0)} m increment must measure {_fmt(bar_segment_cm, 1)} cm on the plan [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_11",
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
    """Subskill 12: Converting number scale 1:10 000 to a bar scale with 200 m increments."""
    # Via Afrika textbook question 1.2 (LB page 260)
    scale = 10000
    segment_real_m = 200.0
    bar_segment_cm = (segment_real_m * 100.0) / scale

    scale = r.choice([5000, 10000, 20000])
    bar_segment_cm = (segment_real_m * 100.0) / scale
    prompt = (
        f"Refer to the regional layout plan and bar scale shown in the diagram (scale ratio 1 : {scale}). "
        f"The bar scale goes up in {_fmt(segment_real_m, 0)} m increments.\n\n"
        f"Calculate the measurement (in centimetres) between each {_fmt(segment_real_m, 0)} m mark on the bar scale."
    )
    d_spec_12 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Regional Layout Bar Scale (Scale 1 : {scale})",
        "ratio_str": f"1 : {scale}",
        "segments": [{"length_cm": bar_segment_cm, "real_val": segment_real_m, "unit": "m"}],
    }

    correct_ans = f"{_fmt(bar_segment_cm, 1)} cm"
    custom_opts = [
        correct_ans,
        f"{_fmt(bar_segment_cm * 2, 1)} cm",
        f"{_fmt(bar_segment_cm / 2, 1)} cm",
        f"1,0 cm",
    ]

    t1 = "A scale of 1 : 10 000 means 1 cm on the map represents 10 000 cm (100 m) in real life."
    t2 = "To represent 200 m, find how many times 100 m goes into 200 m."
    t3 = f"200 m = 20 000 cm. In cm on drawing = 20 000 ÷ 10 000 = {_fmt(bar_segment_cm, 1)} cm."

    explanation = [
        f"Step 1: Convert ground interval to cm: 200 m × 100 = 20 000 cm [1 Mark: Method].",
        f"Step 2: Divide by scale factor 10 000: 20 000 cm ÷ 10 000 = {_fmt(bar_segment_cm, 1)} cm [1 Mark: Method].",
        f"Step 3: Distance per 200 m division on the bar scale = {_fmt(bar_segment_cm, 1)} cm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_12",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_12,
    )


def gen_subskill_13(r: random.Random) -> Dict[str, Any]:
    """Subskill 13: Measuring distance on a plan using a graphic bar scale directly."""
    # A bar scale has divisions where 2 cm represents 5 m.
    # A measured corridor length is 6.8 cm.
    # Real length = (6.8 / 2) * 5 = 3.4 * 5 = 17.0 m
    bar_cm_per_unit = 2.0
    bar_unit_m = 5.0
    measured_len_cm = r.choice([4.0, 6.0, 6.8, 8.4, 10.0])
    real_distance_m = (measured_len_cm / bar_cm_per_unit) * bar_unit_m

    prompt = (
        f"Refer to the factory floor plan and bar scale shown in the diagram, where each 2 cm segment represents 5 m on the ground. "
        f"The internal factory driveway measures {_fmt(measured_len_cm, 1)} cm on paper.\n\n"
        f"Using the bar scale directly, calculate the actual ground distance in metres."
    )
    d_spec_13 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Factory Floor Plan Bar Scale (Driveway {_fmt(measured_len_cm, 1)} cm)",
        "ratio_str": "1 : 250",
        "segments": [{"length_cm": 2.0, "real_val": 5.0, "unit": "m"}],
        "measured_cm": measured_len_cm,
    }

    correct_ans = f"{_fmt(real_distance_m, 1)} m"
    custom_opts = [
        correct_ans,
        f"{_fmt(real_distance_m * 2, 1)} m",
        f"{_fmt(real_distance_m / 2, 1)} m",
        f"{_fmt(measured_len_cm * bar_unit_m, 1)} m",
    ]

    t1 = f"Determine the scale factor from the bar scale: 2 cm represents 5 m, which means 1 cm represents 2,5 m."
    t2 = f"Multiply the measured {_fmt(measured_len_cm, 1)} cm by 2,5 m/cm."
    t3 = f"Real distance = ({_fmt(measured_len_cm, 1)} ÷ 2) × 5 = {_fmt(real_distance_m, 1)} m."

    explanation = [
        f"Step 1: Determine the bar scale unit rate: 5 m ÷ 2 cm = 2,5 m per cm [1 Mark: Method].",
        f"Step 2: Multiply measured distance by the unit rate: {_fmt(measured_len_cm, 1)} cm × 2,5 m/cm [1 Mark: Method].",
        f"Step 3: Actual ground distance = {_fmt(real_distance_m, 1)} m [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_13",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_13,
    )


def gen_subskill_14(r: random.Random) -> Dict[str, Any]:
    """Subskill 14: Explaining TWO key advantages of a bar scale over a number scale."""
    v_scale = r.choice([50, 100, 200])
    prompt = (
        f"Refer to the scale representation diagram shown (Scale ratio 1 : {v_scale}). "
        f"State TWO significant practical advantages of a graphic bar scale relative to a number scale."
    )
    d_spec_14 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Bar Scale vs Number Scale Comparison (1 : {v_scale})",
        "ratio_str": f"1 : {v_scale}",
        "segments": [{"length_cm": 2.0, "real_val": v_scale * 2 / 100, "unit": "m"}],
    }

    correct_ans = "1. Remains accurate when the document is resized or photocopied; 2. Enables quick direct estimation of distance using a piece of paper without calculations"
    custom_opts = [
        correct_ans,
        "1. It is legally required under the Companies Act; 2. It occupies zero space on the margin of the plan",
        "1. It converts automatically between imperial and metric units; 2. It prevents copyright infringement",
        "1. It displays three-dimensional elevation data; 2. It eliminates the need to measure with a ruler",
    ]

    t1 = "Consider what happens to printed lines when a document is enlarged or shrunk."
    t2 = "A bar scale resizes in exact proportion with the drawing, preserving true proportions."
    t3 = "The two advantages are: photocopying resilience and simple direct estimation without math calculations."

    explanation = [
        f"Step 1: Identify resizing resilience: the graphic bar changes size in exact proportion to the drawing when photocopied [1 Mark: Method].",
        f"Step 2: Identify usability: distances can be estimated directly by eye or paper edge without conversion arithmetic [1 Mark: Method].",
        f"Step 3: State both advantages clearly [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_14",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_14,
    )


def gen_subskill_15(r: random.Random) -> Dict[str, Any]:
    """Subskill 15: Impact of photocopy enlargement (A4 to A3, 141%) on number scale vs bar scale."""
    pct = r.choice([141, 150, 200])
    prompt = (
        f"Refer to the architectural drawing scale diagram shown. An architectural floor plan with number scale 1 : 100 "
        f"on an A4 sheet is enlarged by {pct}% onto a larger sheet via a photocopier.\n\n"
        f"What is the effect of this enlargement on:\n"
        f"1. The original printed number scale (1 : 100)?\n"
        f"2. The printed graphic bar scale?"
    )
    d_spec_15 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Photocopy Enlargement ({pct}%)",
        "ratio_str": f"1 : 100 enlarged by {pct}%",
        "segments": [{"length_cm": 2.0 * pct / 100, "real_val": 2.0, "unit": "m"}],
    }

    correct_ans = "The number scale becomes completely invalid (1 cm no longer equals 1 m); the bar scale expands by 141% and remains 100% accurate"
    custom_opts = [
        correct_ans,
        "Both scales become completely invalid and the drawing cannot be used",
        "The number scale remains 100% valid; the bar scale becomes invalid",
        "Both scales remain valid because standard photocopying preserves numerical ratios",
    ]

    t1 = "Remember that the printed text '1 : 100' does not physically change its words, but the lines on paper have expanded."
    t2 = "The bar scale lines grow by 141%, exactly matching the 141% growth of the building walls."
    t3 = "The number scale becomes invalid, while the bar scale remains completely accurate."

    explanation = [
        f"Step 1: The printed text '1 : 100' remains fixed, but lines are 1,41 times longer, making the ratio false [1 Mark: Method].",
        f"Step 2: The graphic bar scale physically expands by 141% alongside the floor plan lines [1 Mark: Method].",
        f"Step 3: Conclude that number scale is invalid while bar scale remains 100% accurate [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_15",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_15,
    )


def gen_subskill_16(r: random.Random) -> Dict[str, Any]:
    """Subskill 16: Recalibrating an altered number scale from a photocopied bar scale."""
    # A bar scale labeled "10 m" originally measured 2.0 cm (1:500).
    # After enlargement, the "10 m" bar scale segment now measures 2.8 cm!
    # What is the new number scale?
    # 2.8 cm = 10 m = 1 000 cm -> 1 000 / 2.8 = 357.14 -> 1 : 357
    measured_bar_cm = r.choice([2.5, 2.8, 3.2, 3.5])
    bar_label_m = r.choice([5.0, 10.0])
    bar_label_cm = bar_label_m * 100.0
    new_denom = int(round(bar_label_cm / measured_bar_cm))

    prompt = (
        f"Refer to the enlarged photocopy bar scale shown in the diagram. On the photocopied page, "
        f"the bar scale marked '{_fmt(bar_label_m, 0)} m' measures exactly {_fmt(measured_bar_cm, 1)} cm with a metric ruler.\n\n"
        f"Recalibrate the plan by calculating the NEW number scale in the form 1 : x (rounded to the nearest whole integer)."
    )
    d_spec_16 = {
        "diagram_role": "context",
        "kind": "bar_scale",
        "title": f"Recalibrated Bar Scale (Ruler: {_fmt(measured_bar_cm, 1)} cm)",
        "ratio_str": f"1 : {new_denom}",
        "segments": [{"length_cm": measured_bar_cm, "real_val": bar_label_m, "unit": "m"}],
    }

    correct_ans = f"1 : {new_denom}"
    custom_opts = [
        correct_ans,
        f"1 : {new_denom * 2}",
        f"1 : {new_denom // 2}",
        f"1 : {int(bar_label_m * 10)}",
    ]

    t1 = f"Convert the bar scale label ({_fmt(bar_label_m, 0)} m) to centimetres: {_fmt(bar_label_cm, 0)} cm."
    t2 = f"Divide the ground distance in centimetres by the measured ruler distance in centimetres: {_fmt(bar_label_cm, 0)} ÷ {_fmt(measured_bar_cm, 1)}."
    t3 = f"New denominator = {_fmt(bar_label_cm, 0)} ÷ {_fmt(measured_bar_cm, 1)} = {new_denom}. New scale is 1 : {new_denom}."

    explanation = [
        f"Step 1: Ground distance in cm = {_fmt(bar_label_m, 0)} m × 100 = {_fmt(bar_label_cm, 0)} cm [1 Mark: Method].",
        f"Step 2: Divide by ruler measurement: {_fmt(bar_label_cm, 0)} cm ÷ {_fmt(measured_bar_cm, 1)} cm [1 Mark: Method].",
        f"Step 3: New scale denominator = {new_denom} → Scale = 1 : {new_denom} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_16",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_16,
    )
