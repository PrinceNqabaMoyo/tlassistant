"""Subskills 33 to 40: Earthworks, Bulk Materials, and Environmental Fluid Volumes.
Covers gravel/crushed stone volume, bulk bags & costing, topsoil planter beds,
compost bag conversions, trench excavations, rainwater harvesting collection,
dam storage capacity in megalitres (ML), and reservoir evaporation loss.
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


def gen_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Subskill 33: Volume of gravel/crushed stone required for a driveway."""
    name = r.choice(SA_NAMES)
    length = r.choice([12.0, 15.0, 18.0, 20.0])
    width = r.choice([2.5, 3.0, 3.5])
    depth_mm = r.choice([80, 100, 120, 150])
    depth_m = depth_mm / 1000.0

    vol_m3 = round(length * width * depth_m, 2)

    prompt = (
        f"{name} is laying a crushed stone gravel layer on a driveway measuring "
        f"{_fmt(length)} m long and {_fmt(width)} m wide. The gravel must be spread to a "
        f"uniform depth of {depth_mm} mm.\n\n"
        f"Using the formula: Volume = Length × Width × Depth,\n"
        f"calculate the volume of crushed stone needed in cubic metres (m³)."
    )

    correct_ans = f"{_fmt(vol_m3)} m³"
    explanation = (
        f"1. Convert depth to metres: {depth_mm} mm ÷ 1 000 = {_fmt(depth_m, 3)} m.\n"
        f"2. Volume = {_fmt(length)} m × {_fmt(width)} m × {_fmt(depth_m, 3)} m = {correct_ans}."
    )
    t1 = "Convert the depth from millimetres to metres (divide by 1 000) first."
    t2 = f"Calculation: {length} × {width} × {depth_m}."
    t3 = f"Volume of gravel = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_33",
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


def gen_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Subskill 34: Number of bulk gravel bags (rounded up) and total purchase cost."""
    name = r.choice(SA_NAMES)
    vol_required = r.choice([3.2, 4.4, 5.1, 6.7])
    bag_size_m3 = 0.5  # standard 0.5 m³ builder bulk bag
    bags_needed = math.ceil(vol_required / bag_size_m3)
    bag_price = r.choice([420.0, 480.0, 520.0, 550.0])
    total_cost = bags_needed * bag_price

    prompt = (
        f"{name} needs {_fmt(vol_required)} m³ of river sand for building works. "
        f"The local building merchant supplies river sand in 0,5 m³ bulk bags at "
        f"{_fmt_curr(bag_price)} per bag.\n\n"
        f"Determine the number of bulk bags {name} must purchase (rounded up to whole bags) "
        f"and the total cost."
    )

    correct_ans = f"{bags_needed} bags ({_fmt_curr(total_cost)})"
    explanation = (
        f"1. Number of bags = {_fmt(vol_required)} m³ ÷ 0,5 m³ = {_fmt(vol_required / bag_size_m3, 2)}.\n"
        f"2. Round up to whole bags: {bags_needed} bags.\n"
        f"3. Total cost = {bags_needed} × {_fmt_curr(bag_price)} = {_fmt_curr(total_cost)}."
    )
    t1 = "Divide total volume needed by 0,5 and round up to the next whole number."
    t2 = f"Number of bags = {bags_needed}. Multiply by {_fmt_curr(bag_price)}."
    t3 = f"Purchase: {correct_ans}."

    # Custom options
    cand_under = f"{bags_needed - 1} bags ({_fmt_curr((bags_needed - 1) * bag_price)})"
    cand_over = f"{bags_needed + 1} bags ({_fmt_curr((bags_needed + 1) * bag_price)})"
    cand_exact_unrounded = f"{bags_needed} bags ({_fmt_curr((vol_required / bag_size_m3) * bag_price)})"
    custom_opts = [correct_ans, cand_under, cand_over, cand_exact_unrounded]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_34",
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


def gen_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Subskill 35: Topsoil volume for raised garden planter beds."""
    num_beds = r.choice([3, 4, 5])
    length = r.choice([2.5, 3.0, 3.6])
    width = r.choice([1.0, 1.2, 1.5])
    depth = r.choice([0.35, 0.40, 0.45])

    vol_one = length * width * depth
    total_vol = round(vol_one * num_beds, 2)

    d_spec_35 = {
        "diagram_role": "context",
        "kind": "mensuration_3d",
        "shape": "rectangular_planter",
        "title": f"Planter Box ({_fmt(length)} m x {_fmt(width)} m x {_fmt(depth)} m)",
        "dimensions": {"length": length, "width": width, "depth": depth},
    }

    prompt = (
        f"Refer to the raised planter box diagram ({_fmt(length)} m long, {_fmt(width)} m wide, and {_fmt(depth)} m deep).\n"
        f"A community school garden is constructing {num_beds} identical raised vegetable planter boxes.\n\n"
        f"Using the formula: Volume of one box = Length × Width × Depth,\n"
        f"calculate the total volume of topsoil needed to fill all {num_beds} boxes (in m³)."
    )

    correct_ans = f"{_fmt(total_vol)} m³"
    explanation = (
        f"1. Volume of one box = {_fmt(length)} m × {_fmt(width)} m × {_fmt(depth)} m = {_fmt(vol_one, 3)} m³.\n"
        f"2. Total volume for {num_beds} boxes = {num_beds} × {_fmt(vol_one, 3)} m³ = {correct_ans}."
    )
    t1 = "Calculate the volume of a single rectangular planter box, then multiply by the number of boxes."
    t2 = f"Single box: {length} × {width} × {depth} = {_fmt(vol_one, 3)} m³. Multiply by {num_beds}."
    t3 = f"Total volume = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_35",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_35,
    )


def gen_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Subskill 36: Number of 30 dm³ bags of compost needed to cover garden area."""
    name = r.choice(SA_NAMES)
    area_m2 = r.choice([15.0, 20.0, 25.0, 30.0])
    depth_mm = r.choice([20, 25, 30, 40])
    depth_m = depth_mm / 1000.0

    vol_m3 = area_m2 * depth_m
    # 1 m³ = 1 000 dm³
    vol_dm3 = vol_m3 * 1000.0
    bag_size_dm3 = 30.0
    bags_needed = math.ceil(vol_dm3 / bag_size_dm3)

    prompt = (
        f"{name} wants to enrich a flower bed of area {_fmt(area_m2)} m² by spreading compost "
        f"to a thickness of {depth_mm} mm.\n"
        f"Compost is sold at the nursery in 30 dm³ bags.\n\n"
        f"Given that 1 m³ = 1 000 dm³:\n"
        f"1. Calculate the required volume of compost in cubic metres (m³).\n"
        f"2. Convert the volume to dm³ and determine the minimum number of bags {name} must buy."
    )

    correct_ans = f"{bags_needed} bags"
    explanation = (
        f"1. Volume in m³ = Area × Depth = {_fmt(area_m2)} m² × {_fmt(depth_m, 3)} m = {_fmt(vol_m3, 3)} m³.\n"
        f"2. Volume in dm³ = {_fmt(vol_m3, 3)} × 1 000 = {_fmt(vol_dm3, 1)} dm³.\n"
        f"3. Bags required = {_fmt(vol_dm3, 1)} ÷ 30 dm³ = {_fmt(vol_dm3 / bag_size_dm3, 2)} bags.\n"
        f"4. Round up to whole bags: {correct_ans}."
    )
    t1 = "Find volume in m³ (Area × depth in metres), multiply by 1 000 to get dm³, then divide by 30."
    t2 = f"Volume = {_fmt(vol_dm3, 1)} dm³. Bags = {_fmt(vol_dm3 / bag_size_dm3, 2)} -> round up."
    t3 = f"Number of bags = {correct_ans}."

    # Custom options
    cand_down = f"{max(1, bags_needed - 3)} bags"
    cand_up = f"{bags_needed + 4} bags"
    cand_10x = f"{bags_needed * 2} bags"
    cand_half = f"{max(1, math.ceil(bags_needed / 2))} bags"
    custom_opts = [correct_ans, cand_down, cand_up, cand_10x, cand_half]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_36",
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


def gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Trench excavation volume for underground electrical cables/pipes."""
    length = r.choice([45.0, 60.0, 80.0, 100.0])
    width_mm = r.choice([400, 500, 600])
    depth_mm = r.choice([800, 900, 1000, 1200])

    width_m = width_mm / 1000.0
    depth_m = depth_mm / 1000.0
    vol_m3 = round(length * width_m * depth_m, 2)

    prompt = (
        f"A contractor is digging a utility trench for an underground water main.\n"
        f"• Length: {_fmt(length)} m\n"
        f"• Width: {width_mm} mm\n"
        f"• Depth: {depth_mm} mm\n\n"
        f"Using the formula: Volume = Length × Width × Depth,\n"
        f"calculate the total volume of earth excavated in cubic metres (m³)."
    )

    correct_ans = f"{_fmt(vol_m3)} m³"
    explanation = (
        f"1. Convert millimetres to metres:\n"
        f"   • Width = {width_mm} mm ÷ 1 000 = {_fmt(width_m, 2)} m\n"
        f"   • Depth = {depth_mm} mm ÷ 1 000 = {_fmt(depth_m, 2)} m\n"
        f"2. Volume = {_fmt(length)} m × {_fmt(width_m, 2)} m × {_fmt(depth_m, 2)} m = {correct_ans}."
    )
    t1 = "Convert both the trench width and depth from millimetres to metres before multiplying."
    t2 = f"Calculation: {length} × {width_m} × {depth_m}."
    t3 = f"Excavation volume = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_37",
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


def gen_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: Rainwater harvesting collection potential."""
    name = r.choice(SA_NAMES)
    roof_area = r.choice([120.0, 150.0, 180.0, 220.0])
    rainfall_mm = r.choice([45.0, 60.0, 80.0, 110.0])
    efficiency = r.choice([0.85, 0.90])

    # 1 mm of rain on 1 m² = 1 Litre of water
    # Potential Litres = Area × rainfall_mm × efficiency
    harvested_litres = round(roof_area * rainfall_mm * efficiency, 1)

    prompt = (
        f"{name} has installed a rainwater harvesting system connected to a roof with a "
        f"catchment area of {_fmt(roof_area)} m².\n"
        f"During a storm in the Highveld, {rainfall_mm} mm of rain fell.\n"
        f"The gutter collection efficiency is {_fmt(efficiency * 100, 0)}% (due to first-flush "
        f"diversion and minor losses).\n\n"
        f"Formula: Harvested Litres = Roof Area (m²) × Rainfall (mm) × Efficiency\n"
        f"Calculate the total volume of water harvested in Litres (L)."
    )

    correct_ans = f"{_fmt(harvested_litres, 1)} L"
    explanation = (
        f"1. 1 mm rain on 1 m² yields 1 Litre.\n"
        f"2. Harvested Litres = {_fmt(roof_area)} m² × {rainfall_mm} mm × {_fmt(efficiency, 2)} = {correct_ans}."
    )
    t1 = "Multiply roof area by rainfall depth, then multiply by the collection efficiency percentage."
    t2 = f"Calculation: {roof_area} × {rainfall_mm} × {efficiency}."
    t3 = f"Harvested volume = {correct_ans}."

    # Custom options
    no_eff = f"{_fmt(roof_area * rainfall_mm, 1)} L"
    wrong_100x = f"{_fmt(roof_area * rainfall_mm * efficiency / 100.0, 1)} L"
    custom_opts = [correct_ans, no_eff, wrong_100x]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_38",
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


def gen_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Municipal dam storage capacity in megalitres (ML)."""
    dam_name = r.choice(["Vaaldam", "Theewaterskloof Dam", "Gariep Dam", "Midmar Dam", "Roodeplaat Dam"])
    capacity_ml = r.choice([2500.0, 4800.0, 7200.0, 11000.0])
    pct_full = r.choice([62.5, 68.0, 74.5, 81.0])

    water_present_ml = round(capacity_ml * (pct_full / 100.0), 1)
    water_present_kl = round(water_present_ml * 1000.0, 1)

    prompt = (
        f"A hydrological report for {dam_name} indicates that its full capacity is "
        f"{_fmt(capacity_ml, 1)} Megalitres (ML). The dam level is currently at {_fmt(pct_full, 1)}%.\n\n"
        f"Given that 1 Megalitre (ML) = 1 000 kilolitres (kL) = 1 000 000 Litres:\n"
        f"1. Calculate the current volume of water in the dam in Megalitres (ML).\n"
        f"2. State this volume in kilolitres (kL)."
    )

    correct_ans = f"{_fmt(water_present_ml, 1)} ML ({_fmt(water_present_kl, 1)} kL)"
    explanation = (
        f"1. Water volume in ML = {_fmt(capacity_ml, 1)} ML × {_fmt(pct_full, 1)}% = {water_present_ml} ML.\n"
        f"2. Convert to kL: {water_present_ml} ML × 1 000 kL/ML = {_fmt(water_present_kl, 1)} kL."
    )
    t1 = "Calculate percentage of the full capacity in ML, then multiply by 1 000 to get kL."
    t2 = f"{capacity_ml} × {pct_full}% = {_fmt(water_present_ml, 1)} ML. Multiply by 1 000 for kL."
    t3 = f"Current water storage = {correct_ans}."

    # Custom options
    opt_deficit_ml = round(capacity_ml * (1 - pct_full / 100.0), 1)
    opt_deficit = f"{_fmt(opt_deficit_ml, 1)} ML ({_fmt(opt_deficit_ml * 1000, 1)} kL)"
    opt_no_kL_conv = f"{_fmt(water_present_ml, 1)} ML ({_fmt(water_present_ml, 1)} kL)"
    opt_100x = f"{_fmt(water_present_ml * 10, 1)} ML ({_fmt(water_present_kl * 10, 1)} kL)"
    custom_opts = [correct_ans, opt_deficit, opt_no_kL_conv, opt_100x]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_39",
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


def gen_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: Evaporation loss from an open rectangular farm dam."""
    length = r.choice([40.0, 50.0, 60.0])
    width = r.choice([20.0, 25.0, 30.0])
    evap_mm = r.choice([180, 220, 250, 280])  # mm over summer month
    evap_m = evap_mm / 1000.0

    surface_area = length * width
    evap_vol_m3 = round(surface_area * evap_m, 2)
    evap_litres = int(evap_vol_m3 * 1000)

    d_spec_40 = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "shape": "rectangular_dam",
        "title": f"Irrigation Dam ({_fmt(length)} m x {_fmt(width)} m)",
        "dimensions": {"length": length, "width": width},
    }

    prompt = (
        f"Refer to the open irrigation dam diagram on a Limpopo citrus farm ({_fmt(length)} m long by {_fmt(width)} m wide).\n"
        f"During January, the monthly net evaporation loss is recorded as {evap_mm} mm.\n\n"
        f"1. Calculate the surface area of the dam in square metres (m²).\n"
        f"2. Calculate the volume of water lost to evaporation in cubic metres (m³).\n"
        f"3. State the volume lost in Litres (L)."
    )

    correct_ans = f"{_fmt(evap_vol_m3)} m³ ({_fmt(evap_litres)} L)"
    explanation = (
        f"1. Surface Area = {_fmt(length)} m × {_fmt(width)} m = {_fmt(surface_area)} m².\n"
        f"2. Evaporation depth in metres = {evap_mm} mm ÷ 1 000 = {_fmt(evap_m, 3)} m.\n"
        f"3. Volume lost = {_fmt(surface_area)} m² × {_fmt(evap_m, 3)} m = {_fmt(evap_vol_m3)} m³.\n"
        f"4. Volume in Litres = {_fmt(evap_vol_m3)} × 1 000 = {_fmt(evap_litres)} L."
    )
    t1 = "Surface area = Length × Width. Convert evaporation depth from mm to m, then multiply Area × depth."
    t2 = f"Area = {_fmt(surface_area)} m². Depth = {_fmt(evap_m, 3)} m. Volume = {_fmt(evap_vol_m3)} m³."
    t3 = f"Evaporation loss = {correct_ans}."

    # Custom options
    opt_no_mm_conv = f"{_fmt(surface_area * evap_mm)} m³ ({_fmt(surface_area * evap_mm * 1000)} L)"
    opt_half = f"{_fmt(evap_vol_m3 / 2)} m³ ({_fmt(int(evap_litres / 2))} L)"
    opt_double = f"{_fmt(evap_vol_m3 * 2)} m³ ({_fmt(int(evap_litres * 2))} L)"
    custom_opts = [correct_ans, opt_no_mm_conv, opt_half, opt_double]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_meas_subskill_40",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_40,
    )
