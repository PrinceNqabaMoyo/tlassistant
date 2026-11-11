"""Subskills 41 to 46: Packaging, 3D Stacking, and Volumetric Packing Efficiency.
Covers 1D floor/axis division for boxes, package orientation comparisons,
cylindrical can packing grids, unused airspace volume, percentage packing efficiency,
and pallet loading in standard shipping containers.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    PI,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Maximum rectangular boxes packed inside a shipping carton (1D integer division)."""
    # Box dimensions in cm
    item_l = r.choice([10, 12, 15])
    item_w = r.choice([8, 10])
    item_h = r.choice([5, 6])

    # Carton dimensions in cm
    carton_l = item_l * r.randint(3, 5) + r.randint(1, 4)
    carton_w = item_w * r.randint(2, 4) + r.randint(1, 3)
    carton_h = item_h * r.randint(3, 5) + r.randint(1, 2)

    fit_l = carton_l // item_l
    fit_w = carton_w // item_w
    fit_h = carton_h // item_h
    total_boxes = fit_l * fit_w * fit_h

    prompt = (
        f"A factory packs tea boxes into master corrugated cardboard cartons.\n"
        f"• Master carton internal dimensions: {carton_l} cm long × {carton_w} cm wide × {carton_h} cm high.\n"
        f"• Tea box dimensions: {item_l} cm long × {item_w} cm wide × {item_h} cm high.\n\n"
        f"Tea boxes must be placed upright without turning.\n"
        f"Calculate the maximum number of tea boxes that can fit inside one master carton."
    )

    correct_ans = f"{total_boxes} boxes"
    explanation = (
        f"1. Along length: {carton_l} cm ÷ {item_l} cm = {carton_l / item_l:.2f} -> {fit_l} boxes.\n"
        f"2. Along width: {carton_w} cm ÷ {item_w} cm = {carton_w / item_w:.2f} -> {fit_w} boxes.\n"
        f"3. Along height: {carton_h} cm ÷ {item_h} cm = {carton_h / item_h:.2f} -> {fit_h} boxes.\n"
        f"4. Total boxes = {fit_l} × {fit_w} × {fit_h} = {correct_ans}."
    )
    t1 = "Calculate how many boxes fit along each dimension (length, width, height) using integer division."
    t2 = f"Fit: {fit_l} along length, {fit_w} along width, {fit_h} along height. Multiply them together."
    t3 = f"Total = {correct_ans}."

    # Misconception: dividing total volumes
    vol_div = int((carton_l * carton_w * carton_h) / (item_l * item_w * item_h))
    custom_opts = [
        correct_ans,
        f"{vol_div} boxes",
        f"{(fit_l + 1) * fit_w * fit_h} boxes",
        f"{fit_l * fit_w * (fit_h - 1)} boxes",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_41",
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


def gen_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Subskill 42: Orienting packages: comparing horizontal vs vertical packing arrangements."""
    # Box dimensions (L=20, W=10, H=5)
    item_l, item_w, item_h = 20, 10, 5
    carton_l, carton_w, carton_h = 60, 40, 30

    # Orientation A: box length along carton length, width along width, height along height
    fit_a = (carton_l // item_l) * (carton_w // item_w) * (carton_h // item_h)

    # Orientation B: box length along carton width, width along length, height along height
    fit_b = (carton_l // item_w) * (carton_w // item_l) * (carton_h // item_h)

    best_count = max(fit_a, fit_b)
    best_orient = "Orientation A" if fit_a >= fit_b else "Orientation B"

    prompt = (
        f"A distributor packages rectangular soap cartons into a dispatch crate measuring "
        f"{carton_l} cm × {carton_w} cm × {carton_h} cm.\n"
        f"Each soap carton measures {item_l} cm × {item_w} cm × {item_h} cm.\n\n"
        f"• Orientation A: Length along length ({carton_l} ÷ {item_l}), width along width ({carton_w} ÷ {item_w}), "
        f"height along height ({carton_h} ÷ {item_h}).\n"
        f"• Orientation B: Length along width ({carton_w} ÷ {item_l}), width along length ({carton_l} ÷ {item_w}), "
        f"height along height ({carton_h} ÷ {item_h}).\n\n"
        f"Determine the maximum number of soap cartons that fit and which orientation yields this number."
    )

    correct_ans = f"{best_count} cartons ({best_orient})"
    explanation = (
        f"1. Orientation A: ({carton_l} ÷ {item_l}) × ({carton_w} ÷ {item_w}) × ({carton_h} ÷ {item_h}) "
        f"= {carton_l // item_l} × {carton_w // item_w} × {carton_h // item_h} = {fit_a} cartons.\n"
        f"2. Orientation B: ({carton_l} ÷ {item_w}) × ({carton_w} ÷ {item_l}) × ({carton_h} ÷ {item_h}) "
        f"= {carton_l // item_w} × {carton_w // item_l} × {carton_h // item_h} = {fit_b} cartons.\n"
        f"3. Maximum capacity = {correct_ans}."
    )
    t1 = "Calculate the total cartons for both Orientation A and Orientation B and choose the larger."
    t2 = f"Orientation A: {fit_a} cartons. Orientation B: {fit_b} cartons."
    t3 = f"Optimal packing: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{min(fit_a, fit_b)} cartons (Orientation A)" if fit_a < fit_b else f"{min(fit_a, fit_b)} cartons (Orientation B)",
        f"{best_count - 12} cartons (Orientation A)",
        f"{best_count + 12} cartons (Orientation B)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_42",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )


def gen_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Subskill 43: Packing cylindrical cans inside a rectangular cardboard carton."""
    can_diam = r.choice([7.5, 8.0, 10.0])  # cm
    can_h = r.choice([11.0, 12.0, 14.0])    # cm

    num_l = r.choice([4, 6])
    num_w = r.choice([3, 4])
    num_h = r.choice([1, 2])

    carton_l = round(can_diam * num_l + 1.0, 1)
    carton_w = round(can_diam * num_w + 1.0, 1)
    carton_h = round(can_h * num_h + 1.0, 1)

    fit_l = int(carton_l // can_diam)
    fit_w = int(carton_w // can_diam)
    fit_h = int(carton_h // can_h)
    total_cans = fit_l * fit_w * fit_h

    prompt = (
        f"A food cannery packs canned baked beans into cardboard cartons.\n"
        f"• Cylindrical can: Diameter = {_fmt(can_diam)} cm, Height = {_fmt(can_h)} cm.\n"
        f"• Carton interior: Length = {_fmt(carton_l)} cm, Width = {_fmt(carton_w)} cm, Height = {_fmt(carton_h)} cm.\n\n"
        f"Given that cylindrical cans occupy a square grid footprint equal to their diameter ({_fmt(can_diam)} cm × {_fmt(can_diam)} cm),\n"
        f"calculate the maximum number of cans that can be packed into one carton."
    )

    correct_ans = f"{total_cans} cans"
    explanation = (
        f"1. Along length: {_fmt(carton_l)} cm ÷ {_fmt(can_diam)} cm = {carton_l / can_diam:.2f} -> {fit_l} cans.\n"
        f"2. Along width: {_fmt(carton_w)} cm ÷ {_fmt(can_diam)} cm = {carton_w / can_diam:.2f} -> {fit_w} cans.\n"
        f"3. Along height: {_fmt(carton_h)} cm ÷ {_fmt(can_h)} cm = {carton_h / can_h:.2f} -> {fit_h} layer(s).\n"
        f"4. Total cans = {fit_l} × {fit_w} × {fit_h} = {correct_ans}."
    )
    t1 = "Divide carton length and width by the can diameter, and carton height by the can height."
    t2 = f"Calculation: {fit_l} × {fit_w} × {fit_h} = {total_cans}."
    t3 = f"Maximum cans packed = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{fit_l * fit_w * (fit_h + 1)} cans",
        f"{(fit_l - 1) * fit_w * fit_h} cans",
        f"{int((carton_l * carton_w * carton_h) / (PI * ((can_diam / 2)**2) * can_h))} cans",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_43",
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


def gen_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Volume of unused / wasted air space inside a packed shipping box."""
    # Box dimensions
    item_l, item_w, item_h = 10.0, 10.0, 10.0  # 1 000 cm³
    carton_l, carton_w, carton_h = 45.0, 35.0, 25.0

    fit_l = int(carton_l // item_l)  # 4
    fit_w = int(carton_w // item_w)  # 3
    fit_h = int(carton_h // item_h)  # 2
    total_items = fit_l * fit_w * fit_h  # 24

    vol_carton = carton_l * carton_w * carton_h  # 39 375 cm³
    vol_items = total_items * (item_l * item_w * item_h)  # 24 000 cm³
    wasted_vol = round(vol_carton - vol_items, 1)

    prompt = (
        f"A shipping box with internal dimensions {_fmt(carton_l)} cm × {_fmt(carton_w)} cm × {_fmt(carton_h)} cm "
        f"is packed with cubes measuring {_fmt(item_l)} cm on each side.\n"
        f"• Number of cubes packed = {total_items}\n\n"
        f"1. Calculate the total volume of the shipping box in cm³.\n"
        f"2. Calculate the combined volume of the {total_items} packed cubes in cm³.\n"
        f"3. Calculate the volume of unused (wasted) air space inside the box."
    )

    correct_ans = f"{_fmt(wasted_vol)} cm³"
    explanation = (
        f"1. Carton volume = {_fmt(carton_l)} × {_fmt(carton_w)} × {_fmt(carton_h)} = {_fmt(vol_carton)} cm³.\n"
        f"2. Volume of {total_items} cubes = {total_items} × ({_fmt(item_l)} × {_fmt(item_w)} × {_fmt(item_h)}) = {_fmt(vol_items)} cm³.\n"
        f"3. Wasted space = {_fmt(vol_carton)} cm³ − {_fmt(vol_items)} cm³ = {correct_ans}."
    )
    t1 = "Subtract the total volume of all packed cubes from the total volume of the carton."
    t2 = f"Carton volume: {_fmt(vol_carton)} cm³. Cubes: {_fmt(vol_items)} cm³. Wasted: {_fmt(vol_carton)} - {_fmt(vol_items)}."
    t3 = f"Wasted space = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(vol_carton)} cm³",
        f"{_fmt(vol_items)} cm³",
        f"{_fmt(wasted_vol + 2500)} cm³",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_44",
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
    """Subskill 45: Volumetric packing efficiency percentage."""
    can_diam = 8.0
    can_radius = can_diam / 2.0
    can_h = 10.0
    vol_can = PI * (can_radius ** 2) * can_h  # 3.142 * 16 * 10 = 502.72 cm³

    carton_l = 32.0  # fits 4 cans
    carton_w = 24.0  # fits 3 cans
    carton_h = 10.0  # fits 1 layer
    num_cans = 4 * 3 * 1  # 12 cans

    vol_carton = carton_l * carton_w * carton_h  # 7 680 cm³
    vol_all_cans = num_cans * vol_can  # 6 032.64 cm³
    efficiency_pct = round((vol_all_cans / vol_carton) * 100.0, 1)

    prompt = (
        f"A carton measuring {_fmt(carton_l)} cm × {_fmt(carton_w)} cm × {_fmt(carton_h)} cm contains "
        f"{num_cans} cylindrical cans (arranged in a 4 × 3 grid, 1 layer deep).\n"
        f"• Each can has a diameter of {_fmt(can_diam)} cm and height of {_fmt(can_h)} cm.\n"
        f"• Use the formula: Volume of a cylinder = π × r² × h, where π = {PI}.\n\n"
        f"Formula: Packing Efficiency (%) = (Total Volume of Cans ÷ Total Volume of Carton) × 100%\n"
        f"Calculate the volumetric packing efficiency percentage of the carton (to 1 decimal place)."
    )

    correct_ans = f"{_fmt(efficiency_pct, 1)}%"
    explanation = (
        f"1. Volume of one can = {PI} × ({can_radius})² × {can_h} = {_fmt(vol_can, 2)} cm³.\n"
        f"2. Volume of {num_cans} cans = {num_cans} × {_fmt(vol_can, 2)} = {_fmt(vol_all_cans, 2)} cm³.\n"
        f"3. Carton volume = {_fmt(carton_l)} × {_fmt(carton_w)} × {_fmt(carton_h)} = {_fmt(vol_carton)} cm³.\n"
        f"4. Efficiency = ({_fmt(vol_all_cans, 2)} ÷ {_fmt(vol_carton)}) × 100% = {correct_ans}."
    )
    t1 = "Find total volume of all cans, divide by carton volume, and multiply by 100%."
    t2 = f"Cans volume = {_fmt(vol_all_cans, 2)} cm³. Carton = {_fmt(vol_carton)} cm³."
    t3 = f"Packing efficiency = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(100.0 - efficiency_pct, 1)}%",
        f"{_fmt(efficiency_pct - 10.0, 1)}%",
        f"{_fmt(efficiency_pct + 10.0, 1)}%",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_45",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )


def gen_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Subskill 46: Loading standard wooden pallets into a commercial 6-metre shipping container."""
    cont_l_mm = 5898
    cont_w_mm = 2352
    pallet_l_mm = 1200
    pallet_w_mm = 1000
    pallet_h_mm = 1100
    cont_h_mm = 2390

    tier_options = r.choice([1, 2])
    fit_lengthwise = cont_l_mm // pallet_l_mm  # 4
    fit_widthwise = cont_w_mm // pallet_w_mm   # 2
    standard_floor_fit = fit_lengthwise * fit_widthwise  # 8
    fit_height = cont_h_mm // pallet_h_mm if tier_options == 2 else 1  # 2 tiers or 1 tier
    total_pallets = standard_floor_fit * fit_height

    d_spec_46 = {
        "diagram_role": "context",
        "kind": "packaging_packing",
        "title": f"Shipping Container Pallet Stacking ({total_pallets} Pallets in {fit_height} Tiers)",
        "container": {"length": cont_l_mm, "width": cont_w_mm, "height": cont_h_mm},
        "box": {"length": pallet_l_mm, "width": pallet_w_mm, "height": pallet_h_mm},
        "dims": {"cont_l": cont_l_mm, "cont_w": cont_w_mm, "pallet_l": pallet_l_mm, "pallet_w": pallet_w_mm, "tiers": fit_height},
        "carton_l": pallet_l_mm,
        "box_l": cont_l_mm,
    }

    prompt = (
        f"Refer to the container packaging layout shown in the diagram.\n"
        f"A freight logistics company loads standard wooden pallets (1 200 mm × 1 000 mm × 1 100 mm) "
        f"into a 6-metre container (5 898 mm × 2 352 mm × 2 390 mm) in {fit_height} tier(s).\n\n"
        f"1. How many pallets fit on the container floor in one layer?\n"
        f"2. What is the total number of pallets that can be transported in {fit_height} tier(s)?"
    )

    correct_ans = f"{total_pallets} pallets ({standard_floor_fit} on floor × {fit_height} tier{'s' if fit_height > 1 else ''})"
    explanation = (
        f"1. Floor length fit: 5 898 mm ÷ 1 200 mm = {cont_l_mm / pallet_l_mm:.2f} -> {fit_lengthwise} pallets.\n"
        f"2. Floor width fit: 2 352 mm ÷ 1 000 mm = {cont_w_mm / pallet_w_mm:.2f} -> {fit_widthwise} rows.\n"
        f"3. Floor layer capacity = {fit_lengthwise} × {fit_widthwise} = {standard_floor_fit} pallets.\n"
        f"4. Total pallets in {fit_height} tier(s) = {standard_floor_fit} × {fit_height} = {correct_ans}."
    )
    t1 = "Divide container length and width by pallet dimensions to determine floor fit."
    t2 = f"Floor: {fit_lengthwise} × {fit_widthwise} = {standard_floor_fit} pallets."
    t3 = f"Total = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{standard_floor_fit} pallets ({standard_floor_fit} on floor × 1 tier)",
        f"{standard_floor_fit * 3} pallets ({standard_floor_fit} on floor × 3 tiers)",
        f"{total_pallets + 4} pallets (10 on floor)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_46",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_46,
    )



