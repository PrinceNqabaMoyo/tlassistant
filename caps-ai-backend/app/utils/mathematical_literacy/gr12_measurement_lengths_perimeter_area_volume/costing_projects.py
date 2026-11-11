"""Subskills 47 to 52: Multi-step Measurement Project Costing, Quotations & Optimization.
Covers swimming pool renovation, paving and kerbing project, interior room decorating,
smallholder irrigation water budget, warehouse floor storage density,
and concrete slab casting quotation.
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


def gen_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: Complete swimming pool renovation: interior plaster area + mosaic waterline border."""
    name = r.choice(SA_NAMES)
    length = r.choice([8.0, 9.0, 10.0])
    width = r.choice([4.0, 4.5, 5.0])
    depth = r.choice([1.5, 1.6, 1.8])

    # Floor area + 4 walls
    floor_area = length * width
    wall_area = 2 * (length * depth) + 2 * (width * depth)
    interior_sa = round(floor_area + wall_area, 2)

    # Perimeter waterline border
    perimeter = round(2 * (length + width), 2)
    border_cost_per_m = r.choice([120.0, 150.0, 180.0])
    total_border_cost = round(perimeter * border_cost_per_m, 2)

    prompt = (
        f"{name} is renovating a rectangular swimming pool with interior dimensions:\n"
        f"• Length = {_fmt(length)} m, Width = {_fmt(width)} m, Uniform Depth = {_fmt(depth)} m.\n\n"
        f"The renovation requires:\n"
        f"1. Applying epoxy coating to the interior surfaces (floor and 4 walls).\n"
        f"   Formula: Interior Area = (Length × Width) + 2(Length × Depth) + 2(Width × Depth).\n"
        f"2. Installing a decorative ceramic mosaic waterline border strip around the top perimeter.\n"
        f"   The mosaic strip costs {_fmt_curr(border_cost_per_m)} per linear metre.\n\n"
        f"Calculate the total interior surface area to be coated (in m²) and the cost of the waterline mosaic strip."
    )

    correct_ans = f"{_fmt(interior_sa)} m² ({_fmt_curr(total_border_cost)})"
    explanation = (
        f"1. Floor area = {_fmt(length)} × {_fmt(width)} = {_fmt(floor_area)} m².\n"
        f"2. Long walls area = 2 × ({_fmt(length)} × {_fmt(depth)}) = {_fmt(2 * length * depth)} m².\n"
        f"3. Short walls area = 2 × ({_fmt(width)} × {_fmt(depth)}) = {_fmt(2 * width * depth)} m².\n"
        f"4. Total interior surface area = {_fmt(interior_sa)} m².\n"
        f"5. Perimeter = 2 × ({_fmt(length)} + {_fmt(width)}) = {_fmt(perimeter)} m.\n"
        f"6. Waterline border cost = {_fmt(perimeter)} m × {_fmt_curr(border_cost_per_m)} = {_fmt_curr(total_border_cost)}."
    )
    t1 = "Calculate interior surface area (floor + 4 walls) and perimeter around the pool."
    t2 = f"Interior area = {_fmt(interior_sa)} m². Perimeter = {_fmt(perimeter)} m. Cost = {_fmt(perimeter)} × {_fmt_curr(border_cost_per_m)}."
    t3 = f"Renovation spec: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(floor_area + 2 * wall_area)} m² ({_fmt_curr(total_border_cost)})",
        f"{_fmt(interior_sa)} m² ({_fmt_curr(total_border_cost * 1.15)})",
        f"{_fmt(interior_sa - floor_area)} m² ({_fmt_curr(total_border_cost)})",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_47",
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


def gen_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Complete paving project: bricks with 10% wastage + bedding sand volume + kerb edging."""
    name = r.choice(SA_NAMES)
    length = r.choice([10.0, 12.0, 15.0])
    width = r.choice([3.0, 4.0, 5.0])
    area = length * width  # m²

    # Bricks per m² = 50
    raw_bricks = area * 50
    total_bricks = int(math.ceil(raw_bricks * 1.10))  # 10% cutting waste

    # Bedding sand 25 mm thick
    sand_vol_m3 = round(area * 0.025, 2)

    # Perimeter edging along both long sides (width sides open to road/house)
    edging_m = round(2 * length, 1)

    prompt = (
        f"{name} is paving a driveway of {_fmt(length)} m long by {_fmt(width)} m wide.\n"
        f"• Paving area = Length × Width.\n"
        f"• Interlocking paving bricks required: 50 bricks per m², plus 10% extra for cutting and breakage.\n"
        f"• Bedding river sand layer thickness: 25 mm (0,025 m).\n"
        f"• Concrete kerb edging is installed along both lengths of the driveway.\n\n"
        f"1. How many paving bricks must be ordered (including 10% waste)?\n"
        f"2. What volume of bedding sand is needed in m³?\n"
        f"3. What is the total length of kerb edging required?"
    )

    correct_ans = f"{total_bricks} bricks, {_fmt(sand_vol_m3)} m³ sand, {_fmt(edging_m)} m kerbing"
    explanation = (
        f"1. Paving area = {_fmt(length)} × {_fmt(width)} = {_fmt(area)} m².\n"
        f"2. Bricks needed = {_fmt(area)} × 50 = {int(raw_bricks)}. With 10% waste: {int(raw_bricks)} × 1,10 = {total_bricks} bricks.\n"
        f"3. Bedding sand volume = {_fmt(area)} m² × 0,025 m = {_fmt(sand_vol_m3)} m³.\n"
        f"4. Kerb edging (both long sides) = 2 × {_fmt(length)} = {_fmt(edging_m)} m."
    )
    t1 = "Multiply area by 50 and add 10%. Multiply area by 0,025 for sand. Multiply length by 2 for kerbing."
    t2 = f"Area = {_fmt(area)} m². Bricks = {total_bricks}. Sand = {_fmt(sand_vol_m3)} m³. Kerbing = {_fmt(edging_m)} m."
    t3 = f"Requirements: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{int(raw_bricks)} bricks, {_fmt(sand_vol_m3)} m³ sand, {_fmt(edging_m)} m kerbing",
        f"{total_bricks} bricks, {_fmt(sand_vol_m3 * 10)} m³ sand, {_fmt(edging_m * 2)} m kerbing",
        f"{total_bricks + 200} bricks, {_fmt(sand_vol_m3)} m³ sand, {_fmt(edging_m)} m kerbing",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_48",
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


def gen_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Complete room decorating project: ceiling + net walls (minus door/window) + skirting."""
    length = r.choice([5.0, 6.0])
    width = r.choice([4.0, 4.5])
    height = 2.8

    # Ceiling area
    ceiling_area = length * width

    # Gross wall area
    gross_walls = 2 * (length * height) + 2 * (width * height)
    # Deductions: 1 door (2.0 m × 0.8 m = 1.6 m²) + 1 window (1.5 m × 1.2 m = 1.8 m²)
    door_window_area = 1.6 + 1.8  # 3.4 m²
    net_walls = round(gross_walls - door_window_area, 2)

    # Skirting boards perimeter = 2(length + width) - 0.8 m door opening
    skirting_m = round(2 * (length + width) - 0.8, 1)

    d_spec_49 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Living Room Floor Plan ({_fmt(length)} m x {_fmt(width)} m)",
        "rooms": [{"name": "Living Room", "length_m": length, "width_m": width, "height_m": height}],
    }

    prompt = (
        f"Refer to the living room floor plan measuring Length = {_fmt(length)} m, Width = {_fmt(width)} m, Height = {_fmt(height)} m.\n"
        f"The room has one door (2,0 m × 0,8 m) and one window (1,5 m × 1,2 m).\n\n"
        f"1. Ceiling area = Length × Width.\n"
        f"2. Net wall painting area = Gross wall area − Door and window area.\n"
        f"3. Skirting boards perimeter = Room perimeter − Door opening (0,8 m).\n\n"
        f"Calculate the net wall painting area (in m²) and the skirting board length required (in m)."
    )

    correct_ans = f"Net walls: {_fmt(net_walls)} m², Skirting: {_fmt(skirting_m)} m"
    explanation = (
        f"1. Gross walls = 2({_fmt(length)} × {height}) + 2({_fmt(width)} × {height}) = {_fmt(gross_walls)} m².\n"
        f"2. Door = 2,0 × 0,8 = 1,60 m². Window = 1,5 × 1,2 = 1,80 m². Total deductions = 3,40 m².\n"
        f"3. Net walls = {_fmt(gross_walls)} − 3,40 = {_fmt(net_walls)} m².\n"
        f"4. Perimeter = 2({_fmt(length)} + {_fmt(width)}) = {_fmt(2 * (length + width))} m.\n"
        f"5. Skirting length = {_fmt(2 * (length + width))} − 0,8 m = {_fmt(skirting_m)} m."
    )
    t1 = "Calculate total 4-wall area, subtract door and window area. For skirting, find perimeter and subtract door width."
    t2 = f"Net walls = {_fmt(gross_walls)} - 3,40 = {_fmt(net_walls)} m². Skirting = {_fmt(2 * (length + width))} - 0,8 = {_fmt(skirting_m)} m."
    t3 = f"Results: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Net walls: {_fmt(gross_walls)} m², Skirting: {_fmt(skirting_m + 0.8)} m",
        f"Net walls: {_fmt(net_walls - 3.4)} m², Skirting: {_fmt(skirting_m)} m",
        f"Net walls: {_fmt(net_walls)} m², Skirting: {_fmt(skirting_m - 2.0)} m",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_49",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_49,
    )


def gen_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: Smallholder farm irrigation: dam volume capacity + daily requirement + days of supply."""
    dam_vol_m3 = r.choice([450.0, 600.0, 800.0])
    dam_litres = int(dam_vol_m3 * 1000)

    daily_usage_litres = r.choice([15000, 20000, 25000])
    days_supply = dam_litres // daily_usage_litres

    prompt = (
        f"A smallholder farmer in Mpumalanga relies on a rainwater earth dam with a holding "
        f"capacity of {_fmt(dam_vol_m3)} m³.\n"
        f"During dry season irrigation, the vegetable crop consumes {daily_usage_litres:,} Litres "
        f"of water per day.\n\n"
        f"Given that 1 m³ = 1 000 Litres:\n"
        f"1. Convert the dam holding capacity to Litres.\n"
        f"2. Calculate the number of full days of irrigation supply available from a full dam "
        f"(assuming no rainfall)."
    )

    correct_ans = f"{dam_litres:,} L ({days_supply} days)".replace(",", " ")
    explanation = (
        f"1. Dam capacity in Litres = {_fmt(dam_vol_m3)} m³ × 1 000 = {dam_litres:,} L.\n"
        f"2. Days of supply = {dam_litres:,} L ÷ {daily_usage_litres:,} L/day = {days_supply} full days."
    ).replace(",", " ")
    t1 = "Convert m³ to Litres by multiplying by 1 000, then divide by the daily water usage."
    t2 = f"{dam_vol_m3} × 1 000 = {dam_litres:,} L. Divide by {daily_usage_litres:,}.".replace(",", " ")
    t3 = f"Irrigation budget: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{dam_litres:,} L ({days_supply - 5} days)".replace(",", " "),
        f"{dam_litres:,} L ({days_supply + 5} days)".replace(",", " "),
        f"{int(dam_vol_m3):,} L ({int(dam_vol_m3 // daily_usage_litres)} days)".replace(",", " "),
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_50",
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


def gen_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: Warehouse inventory pallet racking: floor area occupied + aisle clearance + storage density."""
    wh_l, wh_w = 40.0, 25.0
    total_floor = wh_l * wh_w  # 1 000 m²

    num_pallets_floor = r.choice([320, 360, 400])
    pallet_footprint_m2 = 1.2 * 1.0  # 1.2 m² per standard pallet

    total_pallet_area = num_pallets_floor * pallet_footprint_m2
    density_pct = round((total_pallet_area / total_floor) * 100.0, 1)
    aisle_area = round(total_floor - total_pallet_area, 1)

    prompt = (
        f"A distribution warehouse in Midrand has a floor space measuring {_fmt(wh_l)} m by {_fmt(wh_w)} m.\n"
        f"• Total floor area = {_fmt(total_floor)} m².\n"
        f"• The floor accommodates {num_pallets_floor} pallet bays.\n"
        f"• Each pallet bay has a footprint of 1,2 m × 1,0 m = {_fmt(pallet_footprint_m2)} m².\n\n"
        f"1. Calculate the total floor area directly occupied by pallet bays.\n"
        f"2. Calculate the remaining floor area reserved for forklift aisles and staging.\n"
        f"3. Calculate the pallet floor storage density percentage: (Pallet Area ÷ Total Floor Area) × 100%."
    )

    correct_ans = f"Pallets: {_fmt(total_pallet_area)} m², Aisles: {_fmt(aisle_area)} m² ({_fmt(density_pct, 1)}%)"
    explanation = (
        f"1. Pallet area = {num_pallets_floor} × {_fmt(pallet_footprint_m2)} m² = {_fmt(total_pallet_area)} m².\n"
        f"2. Aisle and staging area = {_fmt(total_floor)} m² − {_fmt(total_pallet_area)} m² = {_fmt(aisle_area)} m².\n"
        f"3. Storage density = ({_fmt(total_pallet_area)} ÷ {_fmt(total_floor)}) × 100% = {_fmt(density_pct, 1)}%."
    )
    t1 = "Multiply number of pallets by 1,2 m² to get pallet area. Subtract from total warehouse floor for aisles."
    t2 = f"Pallet area = {_fmt(total_pallet_area)} m². Aisle area = {_fmt(aisle_area)} m². Density = {_fmt(density_pct, 1)}%."
    t3 = f"Warehouse space breakdown: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Pallets: {_fmt(total_pallet_area)} m², Aisles: {_fmt(aisle_area)} m² ({_fmt(100.0 - density_pct, 1)}%)",
        f"Pallets: {_fmt(total_pallet_area * 1.1)} m², Aisles: {_fmt(aisle_area * 0.9)} m² ({_fmt(density_pct + 5, 1)}%)",
        f"Pallets: {_fmt(total_pallet_area * 0.8)} m², Aisles: {_fmt(aisle_area * 1.2)} m² ({_fmt(density_pct - 10, 1)}%)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_51",
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


def gen_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Concrete slab casting quotation: volume + ready-mix cost + timber shuttering perimeter."""
    name = r.choice(SA_NAMES)
    length = r.choice([12.0, 14.0, 16.0])
    width = r.choice([6.0, 7.0, 8.0])
    thickness_mm = r.choice([120, 150, 180])
    thickness_m = thickness_mm / 1000.0

    vol_m3 = round(length * width * thickness_m, 2)
    concrete_rate = r.choice([1250.0, 1350.0, 1450.0])  # R per m³
    concrete_cost = round(vol_m3 * concrete_rate, 2)

    # Perimeter of wooden formwork / shuttering boards
    perimeter = round(2 * (length + width), 1)

    prompt = (
        f"{name} is casting a reinforced concrete foundation slab for an outbuilding:\n"
        f"• Dimensions: Length = {_fmt(length)} m, Width = {_fmt(width)} m, Thickness = {thickness_mm} mm.\n"
        f"• Ready-mix concrete price: {_fmt_curr(concrete_rate)} per m³ (incl. VAT).\n"
        f"• Perimeter wooden formwork (shuttering) is placed around the entire outer edge.\n\n"
        f"1. Convert thickness to metres and calculate the concrete volume in m³.\n"
        f"2. Calculate the ready-mix concrete cost.\n"
        f"3. State the total length of wooden shuttering boards needed to frame the slab perimeter."
    )

    correct_ans = f"{_fmt(vol_m3)} m³ concrete ({_fmt_curr(concrete_cost)}), {_fmt(perimeter)} m shuttering"
    explanation = (
        f"1. Thickness in metres = {thickness_mm} mm ÷ 1 000 = {_fmt(thickness_m, 3)} m.\n"
        f"2. Volume = {_fmt(length)} m × {_fmt(width)} m × {_fmt(thickness_m, 3)} m = {_fmt(vol_m3)} m³.\n"
        f"3. Concrete cost = {_fmt(vol_m3)} m³ × {_fmt_curr(concrete_rate)} = {_fmt_curr(concrete_cost)}.\n"
        f"4. Perimeter shuttering = 2 × ({_fmt(length)} + {_fmt(width)}) = {_fmt(perimeter)} m."
    )
    t1 = "Convert thickness from mm to m, multiply L × W × thickness for volume, multiply volume by rate, and find perimeter."
    t2 = f"Volume = {_fmt(vol_m3)} m³. Cost = {_fmt_curr(concrete_cost)}. Perimeter = {_fmt(perimeter)} m."
    t3 = f"Quotation: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(vol_m3)} m³ concrete ({_fmt_curr(concrete_cost * 1.15)}), {_fmt(perimeter)} m shuttering",
        f"{_fmt(vol_m3 * 10)} m³ concrete ({_fmt_curr(concrete_cost * 10)}), {_fmt(perimeter)} m shuttering",
        f"{_fmt(vol_m3)} m³ concrete ({_fmt_curr(concrete_cost)}), {_fmt(perimeter * 2)} m shuttering",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_52",
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
