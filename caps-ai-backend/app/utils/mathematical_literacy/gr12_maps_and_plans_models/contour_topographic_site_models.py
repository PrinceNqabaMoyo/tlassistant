"""Subskills 47-52: Topographic Site Models, Contours & Civil Layouts for Grade 12 Maps & Plans (Models)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_zar,
)


def gen_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: Stepped contour model layer thickness from vertical scale and foam sheet gauge."""
    contour_interval_m = r.choice([2.0, 5.0, 10.0])
    vert_scale = r.choice([200, 500, 1000])

    interval_mm = contour_interval_m * 1000.0
    layer_thickness_mm = interval_mm / vert_scale

    d_spec_47 = {
        "diagram_role": "context",
        "kind": "elevation_view",
        "title": f"Contour Profile (Interval: {_fmt(contour_interval_m, 1)} m)",
        "side": "Cross-Section",
        "elevation": "Topographic Contour Profile",
        "height_m": contour_interval_m,
        "layers": [{"thickness_mm": layer_thickness_mm, "scale": f"1:{vert_scale}"}],
    }

    prompt = (
        f"A geography and civil engineering team is building a stepped topographic model of a mountain pass.\n"
        f"The topographical contour map has a vertical contour interval of {_fmt(contour_interval_m, 1)} m.\n"
        f"The model's vertical scale is set at 1 : {vert_scale}.\n\n"
        f"What thickness of foam board (in millimetres) must be used for each contour layer so that the vertical elevation is accurately represented?"
    )

    correct_ans = f"{_fmt(layer_thickness_mm, 1)} mm"
    custom_opts = [
        correct_ans,
        f"{_fmt(layer_thickness_mm * 10, 1)} mm",
        f"{_fmt(layer_thickness_mm / 2, 1)} mm",
        f"{_fmt(contour_interval_m, 1)} mm",
    ]

    t1 = "Convert the contour interval from metres to millimetres by multiplying by 1 000."
    t2 = f"Divide the contour interval in millimetres by the vertical scale denominator ({vert_scale})."
    t3 = f"Interval in mm = {_fmt(contour_interval_m, 1)} × 1 000 = {_fmt(interval_mm, 0)} mm. Layer thickness = {_fmt(interval_mm, 0)} ÷ {vert_scale} = {_fmt(layer_thickness_mm, 1)} mm."

    explanation = [
        f"Step 1: Convert contour interval to mm: {_fmt(contour_interval_m, 1)} m × 1 000 = {_fmt(interval_mm, 0)} mm [1 Mark: Method].",
        f"Step 2: Apply vertical scale 1 : {vert_scale}: {_fmt(interval_mm, 0)} mm ÷ {vert_scale} [1 Mark: Method].",
        f"Step 3: Required foam board sheet thickness = {_fmt(layer_thickness_mm, 1)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_47",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_47,
    )


def gen_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Identifying hill peaks vs valleys from contour lines on stepped contour models."""
    base_elev = r.choice([1000, 1200, 1400])
    interval = r.choice([10, 20, 25])
    c1 = base_elev
    c2 = base_elev + interval
    c3 = base_elev + (2 * interval)

    d_spec_48 = {
        "diagram_role": "context",
        "kind": "grid_map",
        "title": f"Topographic Contour Rings ({c1} m, {c2} m, {c3} m)",
        "contours": [c1, c2, c3],
        "landmarks": [{"name": "Peak", "elev": c3}],
        "cells": [{"row": 1, "col": 1, "label": f"{c3} m"}],
    }

    prompt = (
        f"Refer to the stepped topographical scale model shown in the diagram.\n"
        f"A student notices a series of closed concentric contour rings labeled from outer to inner:\n"
        f"Outer ring = {c1} m, Middle ring = {c2} m, Innermost ring = {c3} m.\n\n"
        f"Does this stepped model represent a hill peak or a valley/depression, and what would indicate the opposite?"
    )

    correct_ans = "Hill peak (elevations increase towards the innermost ring); a valley would have elevations decreasing towards the center."
    custom_opts = [
        correct_ans,
        "Valley (elevations increase towards the innermost ring); a hill peak would decrease towards the center.",
        "Plateau (elevations remain constant); contour lines are always concentric on flat terrain.",
        "Cliff edge (concentric lines represent vertical drops regardless of elevation values).",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    explanation = (
        f"1. Contour values: Outer = {c1} m, Middle = {c2} m, Inner = {c3} m.\n"
        f"2. Because the elevation values increase towards the innermost ring ({c1} m -> {c3} m), it represents a hill peak.\n"
        f"3. In a valley or depression, contour values decrease towards the center."
    )
    t1 = "Observe the trend in elevation from the outer ring to the innermost ring."
    t2 = f"{c1} m < {c2} m < {c3} m shows rising elevation towards the center."
    t3 = "Rising elevation towards the inner closed ring indicates a hill peak."

    return _build_question_payload(
        "gr12_models_subskill_48",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_48,
    )


def gen_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Calculating slope gradient (Rise/Run) on scale site model."""
    rise_m = r.choice([15.0, 20.0, 25.0, 30.0])
    run_m = r.choice([100.0, 150.0, 200.0, 250.0])

    # Gradient = Rise / Run -> in form 1 : x where x = run / rise
    x_val = run_m / rise_m
    pct_gradient = (rise_m / run_m) * 100.0

    prompt = (
        f"On a civil engineering site model, a proposed access road climbs an embankment with a vertical rise "
        f"of {_fmt(rise_m, 1)} m over a horizontal ground distance (run) of {_fmt(run_m, 1)} m.\n\n"
        f"Calculate the gradient of the road slope expressed in the standard ratio format 1 : x, "
        f"and state the slope percentage."
    )

    correct_ans = f"1 : {_fmt(x_val, 1)} ({_fmt(pct_gradient, 1)}%)"
    custom_opts = [
        correct_ans,
        f"1 : {_fmt(x_val * 2, 1)} ({_fmt(pct_gradient / 2, 1)}%)",
        f"1 : {_fmt(rise_m, 1)} ({_fmt(rise_m, 1)}%)",
        f"1 : {_fmt(x_val / 2, 1)} ({_fmt(pct_gradient * 2, 1)}%)",
    ]

    t1 = "Gradient = Vertical Rise ÷ Horizontal Run."
    t2 = f"To express as 1 : x, divide the run by the rise: {_fmt(run_m, 1)} ÷ {_fmt(rise_m, 1)}."
    t3 = f"x = {_fmt(run_m, 1)} ÷ {_fmt(rise_m, 1)} = {_fmt(x_val, 1)}. Gradient ratio is 1 : {_fmt(x_val, 1)}. Percentage = ({_fmt(rise_m, 1)} ÷ {_fmt(run_m, 1)}) × 100 = {_fmt(pct_gradient, 1)}%."

    explanation = [
        f"Step 1: State gradient formula: Gradient = Vertical Rise ÷ Horizontal Run = {_fmt(rise_m, 1)} ÷ {_fmt(run_m, 1)} [1 Mark: Method].",
        f"Step 2: Calculate denominator x: {_fmt(run_m, 1)} ÷ {_fmt(rise_m, 1)} = {_fmt(x_val, 1)} [1 Mark: Method].",
        f"Step 3: State gradient ratio and percentage: 1 : {_fmt(x_val, 1)} ({_fmt(pct_gradient, 1)}%) [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_49",
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


def gen_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: Cut-and-fill excavation balance on terraced model."""
    cut_vol_m3 = r.choice([450.0, 600.0, 750.0, 900.0])
    # Bulking factor of excavated soil: 1.15 (15% expansion upon digging)
    bulking_factor = 1.15
    fill_required_m3 = r.choice([400.0, 500.0, 650.0])

    available_fill_m3 = cut_vol_m3 * bulking_factor
    net_surplus_m3 = available_fill_m3 - fill_required_m3

    d_spec_50 = {
        "diagram_role": "context",
        "kind": "bar_graph",
        "title": f"Cut-and-Fill Excavation Volume ({_fmt(cut_vol_m3, 0)} m³)",
        "series": [{"name": "Cut", "value": cut_vol_m3}, {"name": "Fill", "value": fill_required_m3}],
        "categories": ["Excavated", "Required Fill"],
    }

    prompt = (
        f"In civil earthworks modeling for a leveled building terrace, {_fmt(cut_vol_m3, 0)} m³ of compacted earth "
        f"is excavated ('cut') from the higher slope.\n"
        f"Due to aeration, loose excavated soil expands by 15% (bulking factor = 1,15).\n"
        f"The lower section of the site requires {_fmt(fill_required_m3, 0)} m³ of soil ('fill') to build up the terrace.\n\n"
        f"Calculate the net surplus loose soil that must be removed from the site in cubic metres (m³)."
    )

    correct_ans = f"{_fmt(net_surplus_m3, 1)} m³"
    custom_opts = [
        correct_ans,
        f"{_fmt(cut_vol_m3 - fill_required_m3, 1)} m³",
        f"{_fmt(net_surplus_m3 * 1.5, 1)} m³",
        f"{_fmt(available_fill_m3, 1)} m³",
    ]

    t1 = f"Calculate the loose soil volume: {_fmt(cut_vol_m3, 0)} m³ × 1,15."
    t2 = f"Subtract the required fill volume ({_fmt(fill_required_m3, 0)} m³) from the available loose soil volume."
    t3 = f"Available loose soil = {_fmt(cut_vol_m3, 0)} × 1,15 = {_fmt(available_fill_m3, 1)} m³. Surplus = {_fmt(available_fill_m3, 1)} - {_fmt(fill_required_m3, 0)} = {_fmt(net_surplus_m3, 1)} m³."

    explanation = [
        f"Step 1: Calculate expanded loose volume: {_fmt(cut_vol_m3, 0)} m³ × 1,15 = {_fmt(available_fill_m3, 1)} m³ [1 Mark: Method].",
        f"Step 2: Subtract required fill: {_fmt(available_fill_m3, 1)} m³ - {_fmt(fill_required_m3, 0)} m³ [1 Mark: Method].",
        f"Step 3: Net surplus soil to cart away = {_fmt(net_surplus_m3, 1)} m³ [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_50",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_50,
    )


def gen_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: Scaled parking lot bay layouts (5,0 m x 2,5 m at 1:x) and turning aisles."""
    scale = r.choice([100, 200, 250])
    bay_l_m = 5.0
    bay_w_m = 2.5
    aisle_w_m = 6.0

    model_bay_l_mm = (bay_l_m * 1000.0) / scale
    model_bay_w_mm = (bay_w_m * 1000.0) / scale
    model_aisle_mm = (aisle_w_m * 1000.0) / scale

    d_spec_51 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Parking Bay Layout (Scale 1 : {scale})",
        "rooms": [{"name": "Parking Bay", "length_m": 5.0, "width_m": 2.5}],
        "dimensions": {"model_bay_l_mm": model_bay_l_mm, "model_bay_w_mm": model_bay_w_mm, "scale": scale},
    }

    prompt = (
        f"Refer to the parking bay layout shown in the diagram (scale ratio 1 : {scale}).\n"
        f"A town planner designs a parking layout for a shopping mall on a site model with standard perpendicular parking dimensions of:\n"
        f"  - Bay length = 5,0 m\n"
        f"  - Bay width = 2,5 m\n"
        f"  - Central two-way driving aisle width = 6,0 m\n\n"
        f"Calculate the dimensions (in millimetres) of a single parking bay and the driving aisle on the scale model."
    )

    correct_ans = f"Bay: {_fmt(model_bay_l_mm, 1)} mm × {_fmt(model_bay_w_mm, 1)} mm; Aisle: {_fmt(model_aisle_mm, 1)} mm"
    custom_opts = [
        correct_ans,
        f"Bay: {_fmt(model_bay_l_mm * 2, 1)} mm × {_fmt(model_bay_w_mm * 2, 1)} mm; Aisle: {_fmt(model_aisle_mm * 2, 1)} mm",
        f"Bay: {_fmt(model_bay_l_mm / 2, 1)} mm × {_fmt(model_bay_w_mm / 2, 1)} mm; Aisle: {_fmt(model_aisle_mm / 2, 1)} mm",
        f"Bay: {_fmt(model_bay_l_mm * 1.5, 1)} mm × {_fmt(model_bay_w_mm * 1.5, 1)} mm; Aisle: {_fmt(model_aisle_mm * 1.5, 1)} mm",
    ]

    t1 = "Convert all real metres to millimetres by multiplying by 1 000."
    t2 = f"Divide each measurement in millimetres by {scale}."
    t3 = f"Bay length = (5,0 × 1 000) ÷ {scale} = {_fmt(model_bay_l_mm, 1)} mm. Bay width = (2,5 × 1 000) ÷ {scale} = {_fmt(model_bay_w_mm, 1)} mm. Aisle = (6,0 × 1 000) ÷ {scale} = {_fmt(model_aisle_mm, 1)} mm."

    explanation = [
        f"Step 1: Convert dimensions to mm: Bay = 5 000 mm × 2 500 mm; Aisle = 6 000 mm [1 Mark: Method].",
        f"Step 2: Scale down by dividing by {scale}: Bay L = 5 000 ÷ {scale} = {_fmt(model_bay_l_mm, 1)} mm; Bay W = 2 500 ÷ {scale} = {_fmt(model_bay_w_mm, 1)} mm [1 Mark: Method].",
        f"Step 3: Aisle width = 6 000 ÷ {scale} = {_fmt(model_aisle_mm, 1)} mm [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_51",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_51,
    )


def gen_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Comprehensive civil engineering site model project quotation."""
    name = r.choice(SA_NAMES)
    baseboard_fee = 350.0
    contour_cutting_fee = 720.0
    acrylic_casework = 480.0
    landscaping_materials = 250.0
    labour_hours = r.choice([12, 15, 18, 20])
    labour_rate = 85.0
    labour_total = labour_hours * labour_rate

    subtotal = baseboard_fee + contour_cutting_fee + acrylic_casework + landscaping_materials + labour_total
    vat_rate = 0.15
    vat_amount = subtotal * vat_rate
    grand_total_quote = subtotal + vat_amount

    prompt = (
        f"{name} operates an architectural model-making studio in Pretoria and prepares a formal quotation "
        f"for an institutional tender to build a topographical campus master model:\n"
        f"  - Marine plywood baseboard (1 200 mm × 900 mm): {_fmt_zar(baseboard_fee)}\n"
        f"  - Laser contour slicing & assembly: {_fmt_zar(contour_cutting_fee)}\n"
        f"  - Transparent acrylic display dust-cover: {_fmt_zar(acrylic_casework)}\n"
        f"  - Architectural miniature trees & groundcover: {_fmt_zar(landscaping_materials)}\n"
        f"  - Skilled technician labour: {labour_hours} hours at {_fmt_zar(labour_rate)} per hour\n"
        f"  - Value Added Tax (VAT): 15% on all goods and services\n\n"
        f"Calculate the TOTAL quotation amount payable (inclusive of VAT)."
    )

    correct_ans = _fmt_zar(grand_total_quote)
    custom_opts = [
        correct_ans,
        _fmt_zar(subtotal),
        _fmt_zar(grand_total_quote - vat_amount / 2),
        _fmt_zar(grand_total_quote + 500.0),
    ]

    t1 = f"First calculate labour cost: {labour_hours} hours × R 85,00/hr = {_fmt_zar(labour_total)}."
    t2 = "Sum all items to find the subtotal excluding VAT."
    t3 = f"Subtotal = {_fmt_zar(subtotal)}. Add 15% VAT: {_fmt_zar(subtotal)} × 1,15 = {_fmt_zar(grand_total_quote)}."

    explanation = [
        f"Step 1: Calculate labour charge: {labour_hours} × R 85,00 = {_fmt_zar(labour_total)} [1 Mark: Method].",
        f"Step 2: Calculate subtotal before VAT: {_fmt_zar(baseboard_fee)} + {_fmt_zar(contour_cutting_fee)} + {_fmt_zar(acrylic_casework)} + {_fmt_zar(landscaping_materials)} + {_fmt_zar(labour_total)} = {_fmt_zar(subtotal)} [1 Mark: Method].",
        f"Step 3: Add 15% VAT: {_fmt_zar(subtotal)} × 1,15 = {_fmt_zar(grand_total_quote)} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_52",
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
