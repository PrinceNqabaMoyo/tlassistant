"""Cluster 5: 3D Packaging Arrangements & Orientation Optimization (Subskills 36 to 44).

Covers:
36. Single-layer 2D rectangular box grid packaging (integer division rows & columns)
37. Multi-layer 3D box stacking in master shipping cartons (L × W × H integer bounds)
38. Orientation comparison: upright vs sideways packing to maximize capacity
39. Cylindrical cans packaging in rectangular cartons using diameter grid spacing
40. Area/volume division fallacy explanation (why simple division overestimates capacity)
41. Wasted/void volume calculation and percentage empty space in packaging
42. Maximum mass payload limit vs volume capacity (safe stacking limits)
43. Master shipping cartons required for customer order delivery (rounding up)
44. Total packaging budget: cartons, goods, and courier weight shipping charges
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _build_question_payload,
)


def _gen_asm_pack_single_layer_box_grid_length_width(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L = r.choice([40, 45, 50, 60])
    carton_W = r.choice([25, 30, 35, 40])
    box_l = r.choice([6, 8, 10])
    box_w = r.choice([4, 5, 6])

    fit_L = carton_L // box_l
    fit_W = carton_W // box_w
    total_boxes = fit_L * fit_W

    diag = {
        "kind": "packaging_packing",
        "title": "Carton Base Grid Packaging Layout",
        "carton_l": carton_L,
        "carton_w": carton_W,
        "box_l": box_l,
        "box_w": box_w,
        "boxes_l": fit_L,
        "boxes_w": fit_W,
        "total_boxes": total_boxes,
    }

    prompt = (
        f"{name} works in a biscuit dispatch warehouse and must pack small rectangular biscuit boxes into "
        f"the base of a large shipping carton (single layer deep), as shown in the accompanying layout.\n\n"
        f"Dimensions:\n"
        f"• Large shipping carton base: Length = {carton_L} cm, Width = {carton_W} cm\n"
        f"• Small biscuit box base: Length = {box_l} cm, Width = {box_w} cm\n\n"
        f"The small boxes are aligned along the carton axis in uniform rows.\n\n"
        f"1. How many boxes fit along the length of the carton?\n"
        f"2. How many boxes fit along the width of the carton?\n"
        f"3. Calculate the total number of small boxes that can fit in this single layer."
    )
    ans = f"{fit_L} along length × {fit_W} along width = {total_boxes} boxes"

    s1 = f"Divide carton length by box length ({carton_L} ÷ {box_l}) and round DOWN to nearest integer; divide carton width by box width ({carton_W} ÷ {box_w}) and round DOWN; then multiply."
    s2 = f"✓ [1 Mark: Method – Integer division along both axes and product]\nLength fit = {carton_L} ÷ {box_l} = {_fmt(carton_L / box_l)} → {fit_L} boxes.\nWidth fit = {carton_W} ÷ {box_w} = {_fmt(carton_W / box_w)} → {fit_W} boxes.\nTotal = {fit_L} × {fit_W}."
    s3 = f"✓ [1 Mark: Accuracy – Total packed boxes]\nTotal single layer = {total_boxes} boxes."

    return _build_question_payload(
        "asm_pack_single_layer_box_grid_length_width",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {carton_L} by {box_l} (discard decimals), and divide {carton_W} by {box_w} (discard decimals).",
        tier_2_hint=f"{carton_L} ÷ {box_l} = {fit_L}; {carton_W} ÷ {box_w} = {fit_W}.",
        tier_3_hint=f"{fit_L} × {fit_W} = {total_boxes} boxes.",
        diagram_spec=diag,
    )


def _gen_asm_pack_multi_layer_3d_box_stacking(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L = r.choice([400, 480, 500, 600])
    carton_W = r.choice([280, 300, 320, 360])
    carton_H = r.choice([200, 240, 250, 300])

    box_l = r.choice([80, 100, 120])
    box_w = r.choice([50, 60, 80])
    box_h = r.choice([40, 50, 60, 80])

    n_L = carton_L // box_l
    n_W = carton_W // box_w
    n_H = carton_H // box_h
    total_3d = n_L * n_W * n_H

    diag = {
        "kind": "packaging_cartons",
        "title": "3D Multi-Layer Box Stacking Arrangement",
        "carton_l": carton_L,
        "carton_w": carton_W,
        "carton_h": carton_H,
        "box_l": box_l,
        "box_w": box_w,
        "box_h": box_h,
        "dims": f"{carton_L}×{carton_W}×{carton_H}",
    }

    prompt = (
        f"{name} is packing identical tea boxes into a large rectangular corrugated shipping carton (see accompanying 3D packing diagram).\n\n"
        f"Dimensions of large carton: Length = {carton_L} mm, Width = {carton_W} mm, Height = {carton_H} mm\n"
        f"Dimensions of tea box: Length = {box_l} mm, Width = {box_w} mm, Height = {box_h} mm\n\n"
        f"All tea boxes are packed upright in the same orientation.\n\n"
        f"Calculate the maximum number of tea boxes that can be packed into the shipping carton in three dimensions."
    )
    ans = f"{total_3d} tea boxes"

    s1 = f"Calculate the number of boxes along each 3D dimension: length ({carton_L} ÷ {box_l} = {n_L}), width ({carton_W} ÷ {box_w} = {n_W}), height ({carton_H} ÷ {box_h} = {n_H}), then multiply the three counts."
    s2 = f"✓ [1 Mark: Method – 3D integer division and volume multiplication]\nLength-wise = {carton_L} mm ÷ {box_l} mm = {n_L} boxes.\nWidth-wise = {carton_W} mm ÷ {box_w} mm = {n_W} boxes.\nHeight layers = {carton_H} mm ÷ {box_h} mm = {n_H} layers.\nTotal = {n_L} × {n_W} × {n_H}."
    s3 = f"✓ [1 Mark: Accuracy – Total 3D packed boxes]\nTotal packed = {total_3d} tea boxes."

    return _build_question_payload(
        "asm_pack_multi_layer_3d_box_stacking",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the number of boxes along the length ({carton_L} ÷ {box_l}), width ({carton_W} ÷ {box_w}), and height ({carton_H} ÷ {box_h}).",
        tier_2_hint=f"Counts are: {n_L} in length, {n_W} in width, {n_H} in height. Multiply all three.",
        tier_3_hint=f"{n_L} × {n_W} × {n_H} = {total_3d} tea boxes.",
        diagram_spec=diag,
    )


def _gen_asm_pack_orientation_comparison_lengthwise_vs_widthwise(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L = r.choice([60, 72, 80])
    carton_W = r.choice([40, 48, 50])
    carton_H = r.choice([30, 36, 40])

    item_l = r.choice([15, 16, 20])
    item_w = r.choice([10, 12, 15])
    item_h = r.choice([8, 10, 12])

    a_L = carton_L // item_l
    a_W = carton_W // item_w
    a_H = carton_H // item_h
    total_A = a_L * a_W * a_H

    b_L = carton_L // item_w
    b_W = carton_W // item_l
    b_H = carton_H // item_h
    total_B = b_L * b_W * b_H

    diag = {
        "kind": "packaging_packing",
        "title": "Carton Packing Orientation Comparison",
        "carton_l": carton_L,
        "carton_w": carton_W,
        "box_l": item_l,
        "box_w": item_w,
        "boxes_l": a_L,
        "boxes_w": a_W,
        "total_boxes": total_A,
    }

    prompt = (
        f"{name} is testing two different packing orientations for packing gift boxes into a master carton.\n\n"
        f"Master carton dimensions: Length = {carton_L} cm, Width = {carton_W} cm, Height = {carton_H} cm\n"
        f"Gift box dimensions: Length = {item_l} cm, Width = {item_w} cm, Height = {item_h} cm\n\n"
        f"• Orientation 1: Gift box length ({item_l} cm) parallel to carton length ({carton_L} cm)\n"
        f"• Orientation 2: Gift box width ({item_w} cm) parallel to carton length ({carton_L} cm)\n"
        f"(In both orientations, the height remains {item_h} cm).\n\n"
        f"Determine which orientation packs more gift boxes and by how many boxes."
    )
    diff = abs(total_A - total_B)
    ans = f"Orientation 1 holds {total_A} boxes (Orientation 2 holds {total_B} boxes) — Orientation 1 is better by {diff} boxes."

    s1 = f"Calculate total pack capacity for both orientations using integer division in all 3 axes, then compare the totals."
    s2 = f"✓ [1 Mark: Method – Calculating both 3D orientations]\nOrientation 1: ({carton_L}÷{item_l}) × ({carton_W}÷{item_w}) × ({carton_H}÷{item_h}) = {a_L} × {a_W} × {a_H} = {total_A} boxes.\nOrientation 2: ({carton_L}÷{item_w}) × ({carton_W}÷{item_l}) × ({carton_H}÷{item_h}) = {b_L} × {b_W} × {b_H} = {total_B} boxes."
    s3 = f"✓ [1 Mark: Accuracy – Orientation comparison and difference]\n{ans}"

    return _build_question_payload(
        "asm_pack_orientation_comparison_lengthwise_vs_widthwise",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Calculate Orientation 1: {a_L} × {a_W} × {a_H} = {total_A} boxes.",
        tier_2_hint=f"Calculate Orientation 2: {b_L} × {b_W} × {b_H} = {total_B} boxes.",
        tier_3_hint=f"{ans}",
        diagram_spec=diag,
    )


def _gen_asm_pack_cylindrical_cans_in_rectangular_carton(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L_mm = r.choice([400, 500, 600])
    carton_W_mm = r.choice([300, 350, 400])
    carton_H_mm = r.choice([240, 250, 360])

    can_d_mm = r.choice([75, 80, 100])
    can_h_mm = r.choice([110, 120])

    n_L = carton_L_mm // can_d_mm
    n_W = carton_W_mm // can_d_mm
    n_layers = carton_H_mm // can_h_mm
    total_cans = n_L * n_W * n_layers

    prompt = (
        f"{name} packs round cylindrical coffee cans into a rectangular shipping box.\n\n"
        f"Dimensions:\n"
        f"• Shipping box: Length = {carton_L_mm} mm, Width = {carton_W_mm} mm, Height = {carton_H_mm} mm\n"
        f"• Coffee can: Diameter = {can_d_mm} mm, Height = {can_h_mm} mm\n\n"
        f"Note: Each round can occupies a square footprint on the base with side equal to its diameter ({can_d_mm} mm).\n\n"
        f"Calculate the maximum number of coffee cans that can fit into this box."
    )
    ans = f"{total_cans} cans"

    s1 = f"Treat each cylindrical can't footprint as a square of side equal to its diameter ({can_d_mm} mm). Find integer quotient in length, width, and height layers."
    s2 = f"✓ [1 Mark: Method – Using can diameter for length and width bounds and height for layers]\nLength = {carton_L_mm} ÷ {can_d_mm} = {n_L} cans.\nWidth = {carton_W_mm} ÷ {can_d_mm} = {n_W} cans.\nLayers = {carton_H_mm} ÷ {can_h_mm} = {n_layers} layers.\nTotal = {n_L} × {n_W} × {n_layers}."
    s3 = f"✓ [1 Mark: Accuracy – Total packed cylindrical cans]\nTotal capacity = {total_cans} cans."

    return _build_question_payload(
        "asm_pack_cylindrical_cans_in_rectangular_carton",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Use the diameter ({can_d_mm} mm) for length and width divisions.",
        tier_2_hint=f"{carton_L_mm} ÷ {can_d_mm} = {n_L}; {carton_W_mm} ÷ {can_d_mm} = {n_W}; {carton_H_mm} ÷ {can_h_mm} = {n_layers}.",
        tier_3_hint=f"{n_L} × {n_W} × {n_layers} = {total_cans} cans.",
    )


def _gen_asm_pack_area_division_fallacy_explanation(r: random.Random) -> Dict[str, Any]:
    b_side = r.choice([4, 5])
    c_len = 45 if b_side == 5 else 48
    diag = {
        "kind": "packaging_packing",
        "title": f"Discrete Grid vs Continuous Area ({b_side}cm box)",
        "carton_l": c_len,
        "carton_w": 16,
        "box_l": b_side,
        "box_w": b_side,
        "boxes_l": c_len // b_side,
        "boxes_w": 16 // b_side,
        "total_boxes": (c_len // b_side) * (16 // b_side),
    }

    prompt = (
        f"A learner attempts to calculate how many small square boxes (each 5 cm × 5 cm = 25 cm²) will fit "
        f"into a larger carton base measuring 45 cm long and 16 cm wide (see accompanying layout, Total Base Area = 720 cm²).\n\n"
        f"The learner calculates:\n"
        f"720 cm² ÷ 25 cm² = 28,8 boxes → rounds down to 28 boxes.\n\n"
        f"However, when physically packing the boxes:\n"
        f"• Length fit = 45 cm ÷ 5 cm = 9 boxes\n"
        f"• Width fit = 16 cm ÷ 5 cm = 3,2 → 3 boxes\n"
        f"• Actual total = 9 × 3 = 27 boxes.\n\n"
        f"Why did the learner's area division calculation give an incorrect answer of 28 boxes?"
    )
    ans = "Simple area division ignores rigid shapes; a 1 cm strip along the width (45 cm × 1 cm = 45 cm²) is left empty because 5 cm boxes cannot be cut or distorted to fit into the remaining gap."
    opts = [
        "Simple area division ignores rigid shapes; a 1 cm strip along the width (45 cm × 1 cm = 45 cm²) is left empty because 5 cm boxes cannot be cut or distorted to fit into the remaining gap.",
        "The learner forgot to include 15% Value Added Tax in the area.",
        "Cardboard shrinks by 5% when exposed to dry atmospheric air.",
        "Round biscuit boxes become hexagonal when packed closely together.",
    ]

    s1 = f"Understand geometric packing constraints: rigid solid bodies cannot flow into fractional perimeter leftover spaces."
    s2 = f"✓ [1 Mark: Method – Identifying geometric constraint vs continuous area fallacy]\nArea division assumes liquid or malleable matter that fills every corner. Rigid boxes require discrete integer rows and columns."
    s3 = f"✓ [1 Mark: Accuracy – Correct mathematical explanation]\nExplanation: Simple area division ignores rigid shapes; a 1 cm strip along the width (45 cm × 1 cm = 45 cm²) is left empty because 5 cm boxes cannot be cut or distorted to fit into the remaining gap."

    return _build_question_payload(
        "asm_pack_area_division_fallacy_explanation",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Can you cut the biscuit boxes into pieces to fill leftover narrow strips?",
        tier_2_hint="Rigid boxes can only fit in full integer units along length and width.",
        tier_3_hint="Area division ignores rigid boundaries and empty leftover strip spaces.",
        diagram_spec=diag,
    )


def _gen_asm_pack_wasted_volume_void_space_percentage(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    item_l = r.choice([8, 10, 12])
    item_w = r.choice([8, 10])
    item_h = r.choice([8, 10])
    item_vol = item_l * item_w * item_h

    fit_L = r.choice([3, 4, 5])
    fit_W = r.choice([2, 3, 4])
    fit_H = r.choice([2, 3])
    n_packed = fit_L * fit_W * fit_H

    carton_L = fit_L * item_l + r.choice([3, 5])
    carton_W = fit_W * item_w + r.choice([2, 4])
    carton_H = fit_H * item_h + r.choice([2, 3])
    carton_vol = carton_L * carton_W * carton_H
    used_vol = n_packed * item_vol
    void_vol = carton_vol - used_vol
    void_pct = round((void_vol / carton_vol) * 100, 1)

    diag = {
        "kind": "packaging_cartons",
        "title": "Carton 3D Void Space Layout",
        "carton_l": carton_L,
        "carton_w": carton_W,
        "carton_h": carton_H,
        "box_l": item_l,
        "box_w": item_w,
        "box_h": item_h,
        "dims": f"{carton_L}×{carton_W}×{carton_H}",
    }

    prompt = (
        f"{name} packs {n_packed} rectangular items into a shipping box.\n\n"
        f"Measurements:\n"
        f"• Shipping box external volume: {_fmt(carton_vol)} cm³ (45 cm × 32 cm × 22 cm)\n"
        f"• Each packed item has a volume of {_fmt(item_vol)} cm³\n"
        f"• Exactly {n_packed} items fit inside the box\n\n"
        f"1. Calculate the total used volume occupied by the {n_packed} items.\n"
        f"2. Calculate the wasted (empty void) space inside the box in cm³.\n"
        f"3. Calculate the percentage of void space inside the shipping box (rounded to 1 decimal place)."
    )
    ans = f"Void volume = {_fmt(void_vol)} cm³ ({_fmt(void_pct)}% empty space)"

    s1 = f"Multiply packed items by item volume ({n_packed} × {_fmt(item_vol)} = {_fmt(used_vol)} cm³), subtract from carton volume ({_fmt(carton_vol)} − {_fmt(used_vol)} = {_fmt(void_vol)} cm³), then find percentage of total carton volume."
    s2 = f"✓ [1 Mark: Method – Calculating used volume, void volume, and percentage]\nUsed volume = {n_packed} × {_fmt(item_vol)} cm³ = {_fmt(used_vol)} cm³.\nVoid volume = {_fmt(carton_vol)} cm³ − {_fmt(used_vol)} cm³ = {_fmt(void_vol)} cm³.\nVoid % = ({_fmt(void_vol)} ÷ {_fmt(carton_vol)}) × 100."
    s3 = f"✓ [1 Mark: Accuracy – Final void volume and percentage]\nVoid space = {_fmt(void_vol)} cm³ ({_fmt(void_pct)}% empty space)."

    return _build_question_payload(
        "asm_pack_wasted_volume_void_space_percentage",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find total item volume: {n_packed} × {_fmt(item_vol)} = {_fmt(used_vol)} cm³.",
        tier_2_hint=f"Subtract from carton volume: {_fmt(carton_vol)} − {_fmt(used_vol)} = {_fmt(void_vol)} cm³.",
        tier_3_hint=f"Percentage = ({_fmt(void_vol)} ÷ {_fmt(carton_vol)}) × 100 = {_fmt(void_pct)}%.",
        diagram_spec=diag,
    )


def _gen_asm_pack_mass_limit_vs_volume_capacity(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    max_mass_kg = r.choice([10.0, 12.0, 15.0, 20.0])
    max_mass_g = int(max_mass_kg * 1000)
    item_mass_g = r.choice([250, 300, 400, 500])
    mass_capacity = max_mass_g // item_mass_g
    volume_capacity = mass_capacity + r.choice([4, 6, 8, 10])

    prompt = (
        f"{name} is packing tins of paint into a cardboard master carton.\n\n"
        f"Packaging Constraints:\n"
        f"• The physical size of the carton allows a maximum volume capacity of {volume_capacity} tins.\n"
        f"• However, the manufacturer specifies that the carton has a maximum safe carrying mass of {_fmt(max_mass_kg)} kg.\n"
        f"• Each tin of paint has a gross mass of {item_mass_g} g.\n\n"
        f"Calculate the maximum number of tins of paint {name} can pack into one carton without exceeding the safe mass limit."
    )
    ans = f"{mass_capacity} tins"

    s1 = f"Convert maximum mass from kg to grams ({_fmt(max_mass_kg)} kg × 1 000 = {max_mass_g} g), divide by individual tin mass ({item_mass_g} g), and round down to the nearest whole integer."
    s2 = f"✓ [1 Mark: Method – Converting kg to grams and integer division by item mass]\nMax mass (g) = {_fmt(max_mass_kg)} × 1 000 = {max_mass_g} g.\nTins allowed by mass = {max_mass_g} g ÷ {item_mass_g} g = {_fmt(round(max_mass_g / item_mass_g, 2))} → {mass_capacity} tins."
    s3 = f"✓ [1 Mark: Accuracy – Safe packing count limited by mass]\nMaximum packed = {mass_capacity} tins."

    return _build_question_payload(
        "asm_pack_mass_limit_vs_volume_capacity",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Convert {_fmt(max_mass_kg)} kg to grams: {_fmt(max_mass_kg)} × 1 000 = {max_mass_g} g.",
        tier_2_hint=f"Divide {max_mass_g} g by {item_mass_g} g = {_fmt(round(max_mass_g / item_mass_g, 2))}.",
        tier_3_hint=f"Round DOWN to nearest whole integer: {mass_capacity} tins.",
    )


def _gen_asm_pack_shipping_carton_count_for_order(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_order_units = r.choice([450, 520, 600, 750, 1000])
    units_per_carton = r.choice([24, 30, 36, 48])
    cartons_needed = math.ceil(total_order_units / units_per_carton)

    prompt = (
        f"{name}'s manufacturing business must dispatch an order of {total_order_units} units of canned peaches to a supermarket.\n\n"
        f"Each corrugated master shipping carton can hold exactly {units_per_carton} cans.\n\n"
        f"How many shipping cartons does {name} need to pack the entire order completely?"
    )
    ans = f"{cartons_needed} cartons"

    s1 = f"Divide total order units ({total_order_units}) by carton capacity ({units_per_carton}) and round UP to ensure no items are left behind."
    s2 = f"✓ [1 Mark: Method – Dividing total units by units per carton and rounding up]\nRaw cartons = {total_order_units} ÷ {units_per_carton} = {_fmt(round(total_order_units / units_per_carton, 2))} cartons."
    s3 = f"✓ [1 Mark: Accuracy – Rounding up to whole integer cartons]\nTotal shipping cartons = {cartons_needed} cartons."

    return _build_question_payload(
        "asm_pack_shipping_carton_count_for_order",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Divide {total_order_units} by {units_per_carton}.",
        tier_2_hint=f"{total_order_units} ÷ {units_per_carton} = {_fmt(round(total_order_units / units_per_carton, 2))}.",
        tier_3_hint=f"Always round UP so all cans are packed: {cartons_needed} cartons.",
    )


def _gen_asm_pack_carton_and_postage_total_budget(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    chocolates = r.choice([20, 25, 30])
    price_per_choc = r.choice([12.50, 14.00, 15.50])
    carton_cost = r.choice([12.00, 15.00, 18.50])
    weight_kg = round(chocolates * 0.10 + 0.3, 1)  # 100g per choc + 300g box
    courier_rate_per_kg = r.choice([35.00, 40.00, 45.00])

    choc_total = chocolates * price_per_choc
    shipping_total = weight_kg * courier_rate_per_kg
    total_budget = choc_total + carton_cost + shipping_total

    prompt = (
        f"{name} is sending a care package of {chocolates} specialty chocolates to a family member in another province.\n\n"
        f"Cost Breakdown:\n"
        f"• {chocolates} chocolates at {_fmt_curr(price_per_choc)} each\n"
        f"• 1 reinforced postal shipping box at {_fmt_curr(carton_cost)}\n"
        f"• Courier freight charge at {_fmt_curr(courier_rate_per_kg)} per kg for a parcel weighing {_fmt(weight_kg)} kg\n\n"
        f"Calculate the total cost (in Rands) of sending this gift package."
    )
    ans = _fmt_curr(total_budget)

    s1 = f"Calculate cost of chocolates ({chocolates} × {_fmt_curr(price_per_choc)}), courier charge ({_fmt(weight_kg)} kg × {_fmt_curr(courier_rate_per_kg)}), and add the carton box cost ({_fmt_curr(carton_cost)})."
    s2 = f"✓ [1 Mark: Method – Summing merchandise, box, and freight costs]\nChocolates = {chocolates} × {_fmt_curr(price_per_choc)} = {_fmt_curr(choc_total)}.\nBox = {_fmt_curr(carton_cost)}.\nCourier = {_fmt(weight_kg)} × {_fmt_curr(courier_rate_per_kg)} = {_fmt_curr(shipping_total)}.\nTotal = {_fmt_curr(choc_total)} + {_fmt_curr(carton_cost)} + {_fmt_curr(shipping_total)}."
    s3 = f"✓ [1 Mark: Accuracy – Total parcel budget]\nTotal Cost = {_fmt_curr(total_budget)}."

    return _build_question_payload(
        "asm_pack_carton_and_postage_total_budget",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Calculate each component: chocolates ({_fmt_curr(choc_total)}), box ({_fmt_curr(carton_cost)}), and courier ({_fmt_curr(shipping_total)}).",
        tier_2_hint=f"Add {_fmt_curr(choc_total)} + {_fmt_curr(carton_cost)} + {_fmt_curr(shipping_total)}.",
        tier_3_hint=f"Total = {_fmt_curr(total_budget)}.",
    )

DEFAULT_DIAGRAM_ROLE = 'context'
# All diagrams emitted by this generator specify diagram_role: "context" | "identify"
