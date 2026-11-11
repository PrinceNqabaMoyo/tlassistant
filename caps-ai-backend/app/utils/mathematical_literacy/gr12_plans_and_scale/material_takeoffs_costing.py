"""Subskills 47-52: Material Takeoffs & Construction Costing for Grade 12 Plans & Scale."""
from __future__ import annotations

import math
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
    """Subskill 47: Brick quantity takeoff from scaled wall perimeter and height."""
    # Standard South African construction estimating factor:
    # Double-brick wall (220 mm) = 110 standard clay bricks per m² of wall area
    wall_perimeter_m = r.choice([24.0, 28.0, 32.0, 36.0])
    wall_height_m = 2.6
    gross_wall_area_m2 = wall_perimeter_m * wall_height_m

    # Openings deduction: 2 doors (2.0 m² each = 4.0 m²) + 4 windows (1.5 m² each = 6.0 m²) = 10.0 m²
    openings_area_m2 = 10.0
    net_wall_area_m2 = gross_wall_area_m2 - openings_area_m2

    bricks_per_m2 = 110
    total_bricks = int(math.ceil(net_wall_area_m2 * bricks_per_m2))

    prompt = (
        f"A builder estimates the number of standard clay face bricks required for a new cottage.\n"
        f"The exterior perimeter of the 220 mm double-brick walls is {_fmt(wall_perimeter_m, 1)} m, "
        f"and the wall height is {_fmt(wall_height_m, 1)} m from foundation to wall plate.\n"
        f"Total door and window openings deducted from the walls measure {_fmt(openings_area_m2, 1)} m².\n"
        f"Standard South African building estimating guidelines specify 110 bricks per square metre of 220 mm double wall.\n\n"
        f"Calculate the TOTAL number of bricks required (rounded to the nearest whole brick)."
    )

    correct_ans = f"{_fmt(total_bricks, 0)} bricks"
    custom_opts = [
        correct_ans,
        f"{_fmt(int(gross_wall_area_m2 * bricks_per_m2), 0)} bricks",
        f"{_fmt(int(total_bricks * 1.2), 0)} bricks",
        f"{_fmt(int(total_bricks / 2), 0)} bricks",
    ]

    t1 = f"Calculate gross wall area: {_fmt(wall_perimeter_m, 1)} m × {_fmt(wall_height_m, 1)} m = {_fmt(gross_wall_area_m2, 1)} m²."
    t2 = f"Deduct openings: {_fmt(gross_wall_area_m2, 1)} - {_fmt(openings_area_m2, 1)} = {_fmt(net_wall_area_m2, 1)} m²."
    t3 = f"Multiply net wall area by 110 bricks/m²: {_fmt(net_wall_area_m2, 1)} × 110 = {total_bricks} bricks."

    explanation = [
        f"Step 1: Gross wall area = {_fmt(wall_perimeter_m, 1)} m × {_fmt(wall_height_m, 1)} m = {_fmt(gross_wall_area_m2, 1)} m² [1 Mark: Method].",
        f"Step 2: Net wall area after openings = {_fmt(gross_wall_area_m2, 1)} m² - {_fmt(openings_area_m2, 1)} m² = {_fmt(net_wall_area_m2, 1)} m² [1 Mark: Method].",
        f"Step 3: Total bricks = {_fmt(net_wall_area_m2, 1)} m² × 110 bricks/m² = {total_bricks} bricks [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_47",
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


def gen_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Skirting board timber length calculation deducting door openings."""
    room_l_m = r.choice([4.2, 4.8, 5.2, 6.0])
    room_w_m = r.choice([3.2, 3.6, 4.0])
    gross_perim_m = 2 * (room_l_m + room_w_m)

    # 1 external door (0.9 m) + 1 built-in cupboard sliding opening (1.8 m)
    door_opening_m = 0.9
    cupboard_opening_m = 1.8
    total_deduction_m = door_opening_m + cupboard_opening_m
    net_skirting_m = gross_perim_m - total_deduction_m

    prompt = (
        f"Refer to the bedroom layout shown in the diagram. "
        f"A carpenter is installing hardwood skirting boards along the bottom of the walls in a bedroom "
        f"measuring {_fmt(room_l_m, 1)} m long by {_fmt(room_w_m, 1)} m wide, deducting the entrance door opening of {_fmt(door_opening_m, 1)} m "
        f"and built-in wardrobe opening of {_fmt(cupboard_opening_m, 1)} m.\n\n"
        f"Calculate the TOTAL net linear metres of skirting board timber needed."
    )
    d_spec_48 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Bedroom Skirting Layout ({_fmt(room_l_m, 1)} m × {_fmt(room_w_m, 1)} m)",
        "rooms": [{"name": "Bedroom", "length": room_l_m, "width": room_w_m}],
        "openings": [{"name": "Door", "width": door_opening_m}, {"name": "Wardrobe", "width": cupboard_opening_m}],
    }

    correct_ans = f"{_fmt(net_skirting_m, 2)} m"
    custom_opts = [
        correct_ans,
        f"{_fmt(gross_perim_m, 2)} m",
        f"{_fmt(net_skirting_m + 1.0, 2)} m",
        f"{_fmt(room_l_m + room_w_m, 2)} m",
    ]

    t1 = f"Calculate the room perimeter: 2 × ({_fmt(room_l_m, 1)} + {_fmt(room_w_m, 1)}) = {_fmt(gross_perim_m, 2)} m."
    t2 = f"Calculate total doorway deductions: {_fmt(door_opening_m, 1)} m + {_fmt(cupboard_opening_m, 1)} m = {_fmt(total_deduction_m, 2)} m."
    t3 = f"Net skirting = {_fmt(gross_perim_m, 2)} - {_fmt(total_deduction_m, 2)} = {_fmt(net_skirting_m, 2)} m."

    explanation = [
        f"Step 1: Calculate gross room perimeter = 2 × ({_fmt(room_l_m, 1)} + {_fmt(room_w_m, 1)}) = {_fmt(gross_perim_m, 2)} m [1 Mark: Method].",
        f"Step 2: Total openings deduction = {_fmt(door_opening_m, 1)} m + {_fmt(cupboard_opening_m, 1)} m = {_fmt(total_deduction_m, 2)} m [1 Mark: Method].",
        f"Step 3: Net skirting timber required = {_fmt(gross_perim_m, 2)} m - {_fmt(total_deduction_m, 2)} m = {_fmt(net_skirting_m, 2)} m [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_48",
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
    """Subskill 49: Ceiling board sheet takeoff (1 200 mm x 2 400 mm sheets) with 10% wastage."""
    total_ceiling_area_m2 = r.choice([45.0, 52.0, 60.0, 75.0])
    # Standard Rhinoboard gypsum ceiling board in SA: 1 200 mm x 2 400 mm = 2.88 m²
    sheet_area_m2 = 1.2 * 2.4  # 2.88 m²

    wastage_pct = 10
    total_area_with_waste = total_ceiling_area_m2 * (1.0 + (wastage_pct / 100.0))
    exact_sheets = total_area_with_waste / sheet_area_m2
    sheets_to_buy = math.ceil(exact_sheets)

    prompt = (
        f"A contractor needs to install plasterboard ceilings across all rooms of a cottage with a total "
        f"ceiling area of {_fmt(total_ceiling_area_m2, 1)} m².\n"
        f"Standard gypsum ceiling boards measure 1 200 mm × 2 400 mm (Area = 2,88 m² per board).\n"
        f"To account for offcut wastage and diagonal trims, an extra 10% must be added to the ceiling area.\n"
        f"(Ceiling boards must be purchased as complete whole sheets).\n\n"
        f"Calculate the MINIMUM number of ceiling board sheets that must be ordered."
    )

    correct_ans = f"{sheets_to_buy} sheets"
    custom_opts = [
        correct_ans,
        f"{math.ceil(total_ceiling_area_m2 / sheet_area_m2)} sheets",
        f"{sheets_to_buy + 3} sheets",
        f"{sheets_to_buy - 2} sheets",
    ]

    t1 = f"Calculate the required area including 10% wastage: {_fmt(total_ceiling_area_m2, 1)} m² × 1,10 = {_fmt(total_area_with_waste, 2)} m²."
    t2 = f"Divide the gross area by 2,88 m² (the area of one sheet)."
    t3 = f"Sheets = {_fmt(total_area_with_waste, 2)} ÷ 2,88 = {exact_sheets:.2f} → Round UP to {sheets_to_buy} full sheets."

    explanation = [
        f"Step 1: Total area including 10% wastage = {_fmt(total_ceiling_area_m2, 1)} m² × 1,10 = {_fmt(total_area_with_waste, 2)} m² [1 Mark: Method].",
        f"Step 2: Number of boards required = {_fmt(total_area_with_waste, 2)} ÷ 2,88 m² = {exact_sheets:.2f} [1 Mark: Method].",
        f"Step 3: Round UP to the next whole sheet: Order {sheets_to_buy} sheets [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_49",
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
    """Subskill 50: Ceramic floor tile quantity with 10% cutting wastage allowance."""
    floor_area_m2 = r.choice([32.0, 38.0, 44.0, 50.0])
    # Box of tiles covers 1.44 m² (e.g. 4 tiles of 600 mm x 600 mm)
    box_coverage_m2 = 1.44
    price_per_box = 189.50

    wastage_pct = 10
    total_tile_area = floor_area_m2 * (1.0 + (wastage_pct / 100.0))
    boxes_exact = total_tile_area / box_coverage_m2
    boxes_to_buy = math.ceil(boxes_exact)
    total_tile_cost = boxes_to_buy * price_per_box

    prompt = (
        f"A homeowner tiles a living area with a net floor area of {_fmt(floor_area_m2, 1)} m².\n"
        f"Ceramic porcelain tiles are sold in full cardboard boxes covering 1,44 m² per box at R 189,50 per box.\n"
        f"The tiler advises adding 10% extra area to allow for cutting against perimeter walls and broken tiles.\n\n"
        f"Calculate the total number of boxes to buy and the TOTAL cost of the tiles."
    )

    correct_ans = f"{boxes_to_buy} boxes ({_fmt_zar(total_tile_cost)})"
    custom_opts = [
        correct_ans,
        f"{math.ceil(floor_area_m2 / box_coverage_m2)} boxes ({_fmt_zar(math.ceil(floor_area_m2 / box_coverage_m2) * price_per_box)})",
        f"{boxes_to_buy + 2} boxes ({_fmt_zar((boxes_to_buy + 2) * price_per_box)})",
        f"{boxes_to_buy - 2} boxes ({_fmt_zar((boxes_to_buy - 2) * price_per_box)})",
    ]

    t1 = f"Add 10% wastage: {_fmt(floor_area_m2, 1)} m² × 1,10 = {_fmt(total_tile_area, 2)} m²."
    t2 = f"Divide by box coverage (1,44 m²) and round UP to the next whole box."
    t3 = f"Boxes = {_fmt(total_tile_area, 2)} ÷ 1,44 = {boxes_exact:.2f} → {boxes_to_buy} boxes. Total cost = {boxes_to_buy} × R 189,50 = {_fmt_zar(total_tile_cost)}."

    explanation = [
        f"Step 1: Calculate tile area with 10% wastage: {_fmt(floor_area_m2, 1)} m² × 1,10 = {_fmt(total_tile_area, 2)} m² [1 Mark: Method].",
        f"Step 2: Number of boxes needed: {_fmt(total_tile_area, 2)} ÷ 1,44 = {boxes_exact:.2f} → Round UP to {boxes_to_buy} full boxes [1 Mark: Method].",
        f"Step 3: Total tile purchase cost: {boxes_to_buy} × R 189,50 = {_fmt_zar(total_tile_cost)} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_50",
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
    """Subskill 51: Interior wall plastering and paint takeoff in m²."""
    net_wall_area_m2 = r.choice([64.0, 72.0, 80.0, 96.0])
    # 2 coats of PVA paint required
    # Paint spread rate: 8.0 m² per litre per coat
    spread_rate = 8.0
    paint_litres_needed = (net_wall_area_m2 * 2.0) / spread_rate
    # Sold in 5-litre drums
    drum_size_l = 5
    drums_to_buy = math.ceil(paint_litres_needed / drum_size_l)
    price_per_drum = 425.0
    total_paint_cost = drums_to_buy * price_per_drum

    prompt = (
        f"A painter prepares an estimate to apply TWO coats of acrylic PVA wall paint over {_fmt(net_wall_area_m2, 1)} m² "
        f"of newly plastered internal walls.\n"
        f"The paint has a manufacturer coverage spread rate of 8,0 m² per litre per coat.\n"
        f"The paint is sold in 5-litre drums at R 425,00 per drum.\n\n"
        f"Calculate the minimum number of 5-litre drums to purchase and the TOTAL cost of the paint."
    )

    correct_ans = f"{drums_to_buy} drums ({_fmt_zar(total_paint_cost)})"
    custom_opts = [
        correct_ans,
        f"{math.ceil((net_wall_area_m2 / spread_rate) / drum_size_l)} drums ({_fmt_zar(math.ceil((net_wall_area_m2 / spread_rate) / drum_size_l) * price_per_drum)})",
        f"{drums_to_buy + 2} drums ({_fmt_zar((drums_to_buy + 2) * price_per_drum)})",
        f"{drums_to_buy - 1} drums ({_fmt_zar((drums_to_buy - 1) * price_per_drum)})",
    ]

    t1 = f"Total paint coverage required for 2 coats: {_fmt(net_wall_area_m2, 1)} m² × 2 = {_fmt(net_wall_area_m2 * 2, 1)} m²."
    t2 = f"Total litres needed = {_fmt(net_wall_area_m2 * 2, 1)} ÷ 8,0 = {_fmt(paint_litres_needed, 1)} litres."
    t3 = f"Drums = {_fmt(paint_litres_needed, 1)} ÷ 5 = {paint_litres_needed / 5:.2f} → {drums_to_buy} drums. Total = {drums_to_buy} × R 425,00 = {_fmt_zar(total_paint_cost)}."

    explanation = [
        f"Step 1: Total painted area for 2 coats: {_fmt(net_wall_area_m2, 1)} m² × 2 = {_fmt(net_wall_area_m2 * 2, 1)} m² [1 Mark: Method].",
        f"Step 2: Total litres required = {_fmt(net_wall_area_m2 * 2, 1)} ÷ 8,0 = {_fmt(paint_litres_needed, 1)} L [1 Mark: Method].",
        f"Step 3: Number of 5 L drums: {_fmt(paint_litres_needed, 1)} ÷ 5 = {paint_litres_needed / 5:.2f} → Round UP to {drums_to_buy} drums ({_fmt_zar(total_paint_cost)}) [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_51",
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


def gen_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Comprehensive bill of quantities (BOQ) cost estimate with builder's markup and VAT."""
    name = r.choice(SA_NAMES)
    brickwork_subtotal = r.choice([48000.0, 54000.0, 62000.0])
    roofing_subtotal = r.choice([32000.0, 36000.0, 40000.0])
    plumbing_subtotal = r.choice([18000.0, 22000.0, 25000.0])
    electrical_subtotal = r.choice([14000.0, 16000.0, 18000.0])

    prime_cost = brickwork_subtotal + roofing_subtotal + plumbing_subtotal + electrical_subtotal
    # Builder's profit markup: 15%
    markup_pct = 15
    markup_amount = prime_cost * (markup_pct / 100.0)
    subtotal_with_markup = prime_cost + markup_amount

    # VAT: 15%
    vat_pct = 15
    vat_amount = subtotal_with_markup * (vat_pct / 100.0)
    grand_total_boq = subtotal_with_markup + vat_amount

    prompt = (
        f"{name} prepares a formal Bill of Quantities (BOQ) summary for a cottage building contract:\n"
        f"  - Masonry and foundations: {_fmt_zar(brickwork_subtotal)}\n"
        f"  - Timber trusses and roof sheeting: {_fmt_zar(roofing_subtotal)}\n"
        f"  - Plumbing and drainage installation: {_fmt_zar(plumbing_subtotal)}\n"
        f"  - Electrical reticulation: {_fmt_zar(electrical_subtotal)}\n"
        f"  - Builder's preliminary and profit markup: {markup_pct}% on prime costs\n"
        f"  - Value Added Tax (VAT): {vat_pct}% on the contract subtotal\n\n"
        f"Calculate the FINAL contract price payable by the client (inclusive of VAT)."
    )

    correct_ans = _fmt_zar(grand_total_boq)
    custom_opts = [
        correct_ans,
        _fmt_zar(subtotal_with_markup),
        _fmt_zar(prime_cost * 1.30),  # simple additive mistake
        _fmt_zar(grand_total_boq + 15000.0),
    ]

    t1 = f"Calculate prime cost: {_fmt_zar(brickwork_subtotal)} + {_fmt_zar(roofing_subtotal)} + {_fmt_zar(plumbing_subtotal)} + {_fmt_zar(electrical_subtotal)} = {_fmt_zar(prime_cost)}."
    t2 = f"Add {markup_pct}% builder's markup: {_fmt_zar(prime_cost)} × 1,15 = {_fmt_zar(subtotal_with_markup)}."
    t3 = f"Add {vat_pct}% VAT: {_fmt_zar(subtotal_with_markup)} × 1,15 = {_fmt_zar(grand_total_boq)}."

    explanation = [
        f"Step 1: Calculate total prime costs: {_fmt_zar(brickwork_subtotal)} + {_fmt_zar(roofing_subtotal)} + {_fmt_zar(plumbing_subtotal)} + {_fmt_zar(electrical_subtotal)} = {_fmt_zar(prime_cost)} [1 Mark: Method].",
        f"Step 2: Add {markup_pct}% markup: {_fmt_zar(prime_cost)} × 1,15 = {_fmt_zar(subtotal_with_markup)} [1 Mark: Method].",
        f"Step 3: Add {vat_pct}% VAT: {_fmt_zar(subtotal_with_markup)} × 1,15 = {_fmt_zar(grand_total_boq)} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_plans_subskill_52",
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
