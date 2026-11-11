"""Subskills 37 to 44: Material Costing, Estimation & Packaging Optimization for Grade 11 Mathematical Literacy."""
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


def generate_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Wall paint quantity calculation with spread rate (m²/L) and 2 coats."""
    wall_area = r.choice([70, 80, 95, 110, 120])  # m2
    spread_rate = r.choice([8, 10, 12])  # m2 per litre
    num_coats = 2

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is planning to paint the exterior walls of a cottage with a total paintable surface area of **{wall_area} m²**.\n"
        f"The paint instructions specify:\n"
        f"- Spreading rate: **{spread_rate} m² per litre** per coat.\n"
        f"- Number of coats required: **{num_coats} coats**.\n\n"
        f"Calculate the **total volume of paint in litres** needed to complete the job.\n"
        f"*(Formula: $\\text{{Paint in Litres}} = \\frac{{\\text{{Surface Area}} \\times \\text{{Number of Coats}}}}{{\\text{{Spread Rate}}}}$)*"
    )

    total_area_to_coat = wall_area * num_coats
    litres_float = total_area_to_coat / spread_rate
    litres = round(litres_float, 1)

    correct_ans = f"{_fmt(litres)} ℓ"

    # Distractor 1: Only 1 coat
    dist_1_coat = f"{_fmt(round(wall_area / spread_rate, 1))} ℓ"
    # Distractor 2: Multiplied by spread rate
    dist_mult = f"{_fmt(wall_area * spread_rate)} ℓ"

    custom_opts = [
        correct_ans,
        dist_1_coat,
        dist_mult,
        f"{_fmt(round(litres + 4.0, 1))} ℓ",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate total coated area for {num_coats} coats [1 mark]:\n"
        f"Coated Area = {wall_area} m² × {num_coats} = {total_area_to_coat} m².\n\n"
        f"Step 2: Divide by the spread rate [1 mark]:\n"
        f"Paint Required = {total_area_to_coat} m² ÷ {spread_rate} m²/ℓ = {_fmt(litres_float, 2)} ℓ.\n\n"
        f"Step 3: Stated answer with units [1 mark]:\n"
        f"Paint Needed = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_37",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the wall area by 2 for the two coats, then divide by the spread rate.",
        tier_2=f"Total area = {wall_area} × 2 = {total_area_to_coat} m². Litres = {total_area_to_coat} ÷ {spread_rate}.",
        tier_3=f"Paint needed = {correct_ans}.",
        r=r,
    )


def generate_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: Paint purchasing optimization (comparing 1 L, 5 L, 20 L tins)."""
    needed_litres = r.choice([26, 27, 28])
    
    # Prices:
    # 20 L: R 1 350
    # 5 L: R 380
    # 1 L: R 95
    p20 = 1350.0
    p5 = 380.0
    p1 = 95.0

    prompt = (
        f"A homeowner needs exactly **{needed_litres} litres** of acrylic paint for a boundary wall.\n"
        f"The paint is sold in three container sizes at Builders Warehouse:\n\n"
        f"| Tin Size | Price |\n"
        f"| :--- | :--- |\n"
        f"| 1 Litre tin | {_fmt_curr(p1)} |\n"
        f"| 5 Litre tin | {_fmt_curr(p5)} |\n"
        f"| 20 Litre tin | {_fmt_curr(p20)} |\n\n"
        f"Determine the **most cost-effective combination of tins** to buy at least {needed_litres} litres, and calculate the **total cost**."
    )

    # Option 1: 1x 20L + 2x 5L = 30L -> R 1 350 + 2*380 = R 2 110.00
    # Option 2: 1x 20L + 1x 5L + 1x 1L = 26L -> R 1 350 + 380 + 95 = R 1 825.00 (if 26L)
    # Option 3: 1x 20L + 1x 5L + 2x 1L = 27L -> R 1 350 + 380 + 190 = R 1 920.00 (if 27L)
    # Option 4: 1x 20L + 1x 5L + 3x 1L = 28L -> R 1 350 + 380 + 285 = R 2 015.00 (if 28L)
    
    rem_litres = needed_litres - 20
    if rem_litres <= 5:
        opt_tins = "One 20 ℓ tin + One 5 ℓ tin"
        cost = p20 + p5  # 25 L (wait, if needed_litres is 26, 25L is not enough! Need at least needed_litres)
    
    # To cover at least needed_litres:
    # 26 L: 1x20L + 1x5L + 1x1L = R 1 825.00
    # 27 L: 1x20L + 1x5L + 2x1L = R 1 920.00
    # 28 L: 1x20L + 1x5L + 3x1L = R 2 015.00  (vs 1x20L + 2x5L = R 2 110.00)
    
    num_1l = needed_litres - 25
    cost_with_1l = p20 + p5 + (num_1l * p1)
    cost_two_5l = p20 + (2 * p5)  # R 2 110.00
    
    if cost_with_1l < cost_two_5l:
        combo_desc = f"1 × 20 ℓ tin, 1 × 5 ℓ tin, and {num_1l} × 1 ℓ tin{'s' if num_1l > 1 else ''}"
        min_cost = cost_with_1l
    else:
        combo_desc = f"1 × 20 ℓ tin and 2 × 5 ℓ tins"
        min_cost = cost_two_5l

    correct_ans = f"{combo_desc} for {_fmt_curr(min_cost)}"

    custom_opts = [
        correct_ans,
        f"6 × 5 ℓ tins for {_fmt_curr(6 * p5)}",
        f"28 × 1 ℓ tins for {_fmt_curr(needed_litres * p1)}",
        f"2 × 20 ℓ tins for {_fmt_curr(2 * p20)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Test combinations that provide at least {needed_litres} ℓ [1 mark]:\n"
        f"- Combination A (1×20ℓ + 1×5ℓ + {num_1l}×1ℓ): {_fmt_curr(p20)} + {_fmt_curr(p5)} + {_fmt_curr(num_1l * p1)} = {_fmt_curr(cost_with_1l)}.\n"
        f"- Combination B (1×20ℓ + 2×5ℓ = 30ℓ): {_fmt_curr(p20)} + {_fmt_curr(2 * p5)} = {_fmt_curr(cost_two_5l)}.\n"
        f"- Combination C (All 5ℓ tins): {math.ceil(needed_litres/5)} × {_fmt_curr(p5)} = {_fmt_curr(math.ceil(needed_litres/5) * p5)}.\n\n"
        f"Step 2: Compare costs [1 mark]:\n"
        f"Combination A is cheapest at {_fmt_curr(min_cost)}.\n\n"
        f"Step 3: Stated conclusion [1 mark]:\n"
        f"{correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_38",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the cost of different tin combinations that provide at least the required volume and pick the lowest price.",
        tier_2=f"1×20ℓ + 1×5ℓ + {num_1l}×1ℓ = R {cost_with_1l:.2f}. Compare with other options.",
        tier_3=f"Optimal choice: {correct_ans}.",
        r=r,
    )


def generate_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Floor tiling calculation with tile dimensions, box packaging, and waste factor."""
    floor_l = r.randint(6, 9)  # m
    floor_w = r.randint(4, 6)  # m
    waste_pct = 10  # 10% waste for cutting and breakage
    box_coverage = 1.44  # m2 per box of tiles (standard 600x600 or 300x300 boxes)

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is tiling the floor of a rectangular dining room measuring **{floor_l} m** long by **{floor_w} m** wide.\n"
        f"Tiles are packed in boxes that cover **{_fmt(box_coverage)} m²** per box.\n"
        f"An extra **10%** must be added to the room's floor area to account for tile cutting and breakage.\n\n"
        f"Calculate the **total area of tiles needed** (including waste) and the **minimum number of full boxes** to purchase.\n"
        f"*(Boxes cannot be bought as fractions)*"
    )

    net_area = floor_l * floor_w
    gross_area = round(net_area * 1.10, 2)
    boxes = int(math.ceil(gross_area / box_coverage))

    correct_ans = f"{_fmt(gross_area)} m² ({boxes} boxes)"

    # Distractor: Forgot 10% waste
    no_waste_boxes = int(math.ceil(net_area / box_coverage))
    dist_no_waste = f"{_fmt(net_area)} m² ({no_waste_boxes} boxes)"

    custom_opts = [
        correct_ans,
        dist_no_waste,
        f"{_fmt(gross_area)} m² ({boxes + 5} boxes)",
        f"{_fmt(gross_area * 2)} m² ({boxes * 2} boxes)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate net floor area [1 mark]:\n"
        f"Net Area = {floor_l} m × {floor_w} m = {net_area} m².\n\n"
        f"Step 2: Add 10% cutting waste [1 mark]:\n"
        f"Gross Area = {net_area} m² × 1,10 = {_fmt(gross_area)} m².\n\n"
        f"Step 3: Divide by box coverage and round up to the next whole box [1 mark]:\n"
        f"Boxes = {_fmt(gross_area)} ÷ {_fmt(box_coverage)} = {gross_area / box_coverage:.2f} -> {boxes} boxes.\n"
        f"Stated answer: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_39",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find net area (l × w), multiply by 1,10 for 10% waste, divide by 1,44 m² per box, and round UP.",
        tier_2=f"Net = {floor_l} × {floor_w} = {net_area} m². Gross = {gross_area} m². Boxes = {gross_area} ÷ 1,44 = {boxes}.",
        tier_3=f"Result: {correct_ans}.",
        r=r,
    )


def generate_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: Total cost of floor tiling including tile boxes, adhesive bags, and grout."""
    num_boxes = r.randint(22, 38)
    tile_price_per_box = r.choice([165.0, 185.0, 210.0])
    
    # 1 bag of tile adhesive per 4 boxes
    adhesive_bags = int(math.ceil(num_boxes / 4.0))
    adhesive_price = 85.0
    
    # Grout: 2 bags
    grout_bags = 2
    grout_price = 45.0

    prompt = (
        f"A homeowner purchases materials to tile a floor requiring **{num_boxes} boxes of ceramic tiles**.\n"
        f"The material price list at the tile warehouse is:\n"
        f"- Floor tiles: **{_fmt_curr(tile_price_per_box)} per box**\n"
        f"- Tile adhesive: **{_fmt_curr(adhesive_price)} per 20 kg bag** (1 bag is needed for every 4 boxes of tiles)\n"
        f"- Tile grout: **{_fmt_curr(grout_price)} per 5 kg bag** (a total of 2 bags are required)\n\n"
        f"Calculate the **total cost of all materials** needed for the tiling project."
    )

    cost_tiles = num_boxes * tile_price_per_box
    cost_adhesive = adhesive_bags * adhesive_price
    cost_grout = grout_bags * grout_price
    total_material_cost = cost_tiles + cost_adhesive + cost_grout

    correct_ans = _fmt_curr(total_material_cost)

    # Distractor: forgot adhesive
    dist_no_adh = cost_tiles + cost_grout

    custom_opts = [
        correct_ans,
        _fmt_curr(dist_no_adh),
        _fmt_curr(cost_tiles),
        _fmt_curr(total_material_cost + 450.0),
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate tile cost [1 mark]:\n"
        f"Tiles = {num_boxes} boxes × {_fmt_curr(tile_price_per_box)} = {_fmt_curr(cost_tiles)}.\n\n"
        f"Step 2: Determine adhesive and grout quantities and costs [1 mark]:\n"
        f"Adhesive Bags = {num_boxes} ÷ 4 = {num_boxes / 4:.1f} -> {adhesive_bags} bags.\n"
        f"Adhesive Cost = {adhesive_bags} × {_fmt_curr(adhesive_price)} = {_fmt_curr(cost_adhesive)}.\n"
        f"Grout Cost = {grout_bags} × {_fmt_curr(grout_price)} = {_fmt_curr(cost_grout)}.\n\n"
        f"Step 3: Sum total costs [1 mark]:\n"
        f"Total Cost = {_fmt_curr(cost_tiles)} + {_fmt_curr(cost_adhesive)} + {_fmt_curr(cost_grout)} = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_40",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate cost of tiles, then adhesive (round up bags to nearest integer), then grout, and sum.",
        tier_2=f"Tiles = R {cost_tiles:.2f}. Adhesive = {adhesive_bags} × R {adhesive_price} = R {cost_adhesive:.2f}. Grout = 2 × R {grout_price} = R {cost_grout:.2f}.",
        tier_3=f"Total Cost = {correct_ans}.",
        r=r,
    )


def generate_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Concrete slab volume and ready-mix delivery cost."""
    slab_l = r.randint(6, 10)  # m
    slab_w = r.randint(4, 7)   # m
    thickness_mm = r.choice([100, 120, 150])  # mm
    thickness_m = thickness_mm / 1000.0
    concrete_price_m3 = r.choice([1250.0, 1380.0, 1450.0])  # R per m3 ready-mix

    prompt = (
        f"A building contractor is pouring a rectangular concrete garage floor slab.\n"
        f"The slab measures **{slab_l} m** long, **{slab_w} m** wide, and **{thickness_mm} mm** thick.\n"
        f"Ready-mix concrete costs **{_fmt_curr(concrete_price_m3)} per cubic metre (m³)**.\n\n"
        f"Calculate the **volume of concrete needed** in m³ and the **total cost** of the concrete.\n"
        f"*(Round volume to 2 decimal places)*"
    )

    vol_m3 = round(slab_l * slab_w * thickness_m, 2)
    total_cost = round(vol_m3 * concrete_price_m3, 2)

    correct_ans = f"Volume: {_fmt(vol_m3)} m³; Cost: {_fmt_curr(total_cost)}"

    # Distractor: Forgot to convert mm to m
    dist_mm = f"Volume: {_fmt(round(slab_l * slab_w * thickness_mm, 2))} m³; Cost: {_fmt_curr(round(slab_l * slab_w * thickness_mm * concrete_price_m3, 2))}"

    custom_opts = [
        correct_ans,
        dist_mm,
        f"Volume: {_fmt(vol_m3)} m³; Cost: {_fmt_curr(total_cost * 1.5)}",
        f"Volume: {_fmt(round(vol_m3 + 2.0, 2))} m³; Cost: {_fmt_curr(round((vol_m3 + 2.0) * concrete_price_m3, 2))}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Convert slab thickness from mm to metres [1 mark]:\n"
        f"Thickness = {thickness_mm} mm ÷ 1 000 = {_fmt(thickness_m)} m.\n\n"
        f"Step 2: Calculate concrete volume in m³ [1 mark]:\n"
        f"Volume = {slab_l} m × {slab_w} m × {_fmt(thickness_m)} m = {_fmt(vol_m3)} m³.\n\n"
        f"Step 3: Multiply volume by ready-mix rate [1 mark]:\n"
        f"Total Cost = {_fmt(vol_m3)} m³ × {_fmt_curr(concrete_price_m3)}/m³ = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_41",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Convert mm thickness to metres by dividing by 1 000, multiply l × w × thickness, then multiply by price per m³.",
        tier_2=f"Thickness = {thickness_m} m. Volume = {slab_l} × {slab_w} × {thickness_m} = {vol_m3} m³. Multiply by R {concrete_price_m3:.2f}.",
        tier_3=f"Result: {correct_ans}.",
        r=r,
    )


def generate_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Subskill 42: Paving a rectangular driveway with brick pavers."""
    drive_l = r.randint(10, 16)  # m
    drive_w = r.choice([3.0, 3.5, 4.0])  # m
    # Standard bevel brick paver: 200 mm x 100 mm = 0.02 m2 -> 50 pavers per m2
    pavers_per_m2 = 50
    paver_price_each = 3.80  # R 3.80 each
    waste_pct = 5

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is paving a rectangular driveway measuring **{drive_l} m** long by **{_fmt(drive_w)} m** wide.\n"
        f"Standard clay pavers are used at a density of **50 pavers per square metre (m²)**.\n"
        f"A **5% wastage allowance** is added for edge cutting and chipping.\n"
        f"Each paver costs **{_fmt_curr(paver_price_each)}**.\n\n"
        f"Calculate the **total number of pavers needed** (rounded up to the nearest hundred) and the **total cost**."
    )

    drive_area = round(drive_l * drive_w, 2)
    exact_pavers = drive_area * pavers_per_m2
    gross_pavers = exact_pavers * 1.05
    # Round up to nearest hundred
    ordered_pavers = int(math.ceil(gross_pavers / 100.0) * 100)
    total_cost = ordered_pavers * paver_price_each

    correct_ans = f"{_fmt(ordered_pavers)} pavers ({_fmt_curr(total_cost)})"

    # Distractor: without 5% waste
    no_waste_pavers = int(math.ceil(exact_pavers / 100.0) * 100)
    dist_no_waste = f"{_fmt(no_waste_pavers)} pavers ({_fmt_curr(no_waste_pavers * paver_price_each)})"

    custom_opts = [
        correct_ans,
        dist_no_waste,
        f"{_fmt(ordered_pavers + 500)} pavers ({_fmt_curr((ordered_pavers + 500) * paver_price_each)})",
        f"{_fmt(int(exact_pavers))} pavers ({_fmt_curr(exact_pavers * paver_price_each)})",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate driveway area [1 mark]:\n"
        f"Area = {drive_l} m × {_fmt(drive_w)} m = {_fmt(drive_area)} m².\n\n"
        f"Step 2: Calculate pavers with 5% waste [1 mark]:\n"
        f"Exact = {_fmt(drive_area)} m² × 50 pavers/m² = {_fmt(int(exact_pavers))} pavers.\n"
        f"With 5% waste = {_fmt(int(exact_pavers))} × 1,05 = {_fmt(gross_pavers, 1)} -> rounded up to nearest 100 = {_fmt(ordered_pavers)} pavers.\n\n"
        f"Step 3: Calculate total cost [1 mark]:\n"
        f"Total Cost = {_fmt(ordered_pavers)} × {_fmt_curr(paver_price_each)} = {_fmt_curr(total_cost)}.\n"
        f"Conclusion: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_42",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Area = l × w. Multiply by 50 for pavers, add 5% waste, round up to nearest 100, then multiply by paver price.",
        tier_2=f"Area = {drive_area} m². Exact = {exact_pavers} pavers. With waste = {gross_pavers:.1f} -> {ordered_pavers} pavers.",
        tier_3=f"Total = {correct_ans}.",
        r=r,
    )


def generate_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Subskill 43: Packaging small rectangular boxes into a master shipping carton without crushing."""
    # Small box: 10 cm x 8 cm x 5 cm
    b_l, b_w, b_h = 10, 8, 5
    # Carton: 50 cm x 40 cm x 30 cm
    c_l, c_w, c_h = 50, 40, 30

    prompt = (
        f"A pharmaceutical distributor packs rectangular medicine cartons into a large master shipping box.\n"
        f"- **Medicine box**: length = **{b_l} cm**, width = **{b_w} cm**, height = **{b_h} cm**.\n"
        f"- **Master shipping carton**: length = **{c_l} cm**, width = **{c_w} cm**, height = **{c_h} cm**.\n\n"
        f"Assuming all small boxes must be placed upright in the same orientation, calculate the **maximum number of medicine boxes** "
        f"that can fit inside one master shipping carton."
    )

    fit_l = c_l // b_l
    fit_w = c_w // b_w
    fit_h = c_h // b_h
    total_fit = fit_l * fit_w * fit_h

    correct_ans = f"{total_fit} boxes ({fit_l} along length × {fit_w} along width × {fit_h} vertical layers)"

    # Distractor based on theoretical volume division
    carton_vol = c_l * c_w * c_h
    box_vol = b_l * b_w * b_h
    vol_div = carton_vol // box_vol
    dist_vol = f"{vol_div} boxes (based on volume calculation)"

    custom_opts = [
        correct_ans,
        dist_vol,
        f"{total_fit - 50} boxes",
        f"{total_fit + 60} boxes",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate how many boxes fit along each dimension [1 mark]:\n"
        f"- Along length: {c_l} cm ÷ {b_l} cm = {fit_l} boxes.\n"
        f"- Along width: {c_w} cm ÷ {b_w} cm = {fit_w} boxes.\n"
        f"- Along height: {c_h} cm ÷ {b_h} cm = {fit_h} layers.\n\n"
        f"Step 2: Multiply the integer capacities [1 mark]:\n"
        f"Total capacity = {fit_l} × {fit_w} × {fit_h} = {total_fit} boxes.\n\n"
        f"Step 3: Stated answer [1 mark]:\n"
        f"{correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_43",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Never just divide volumes! Divide each carton dimension by the corresponding box dimension, then multiply the three integers.",
        tier_2=f"Length fit = {c_l} ÷ {b_l} = {fit_l}. Width fit = {c_w} ÷ {b_w} = {fit_w}. Height fit = {c_h} ÷ {b_h} = {fit_h}.",
        tier_3=f"Total = {fit_l} × {fit_w} × {fit_h} = {correct_ans}.",
        r=r,
    )


def generate_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Packaging cylindrical food cans into a rectangular transport crate."""
    can_diameter = 8  # cm
    can_height = 12    # cm
    
    crate_l = 48  # cm
    crate_w = 32  # cm
    crate_h = 24  # cm (2 layers of 12 cm)

    prompt = (
        f"A food manufacturer packs cylindrical canned peaches into a rectangular transport crate:\n"
        f"- **Peach can**: diameter = **{can_diameter} cm**, height = **{can_height} cm**.\n"
        f"- **Transport crate**: length = **{crate_l} cm**, width = **{crate_w} cm**, height = **{crate_h} cm**.\n\n"
        f"Calculate the **maximum number of cylindrical cans** that can be packed in a grid pattern into one crate."
    )

    cans_l = crate_l // can_diameter  # 48 // 8 = 6
    cans_w = crate_w // can_diameter  # 32 // 8 = 4
    cans_per_layer = cans_l * cans_w   # 24
    num_layers = crate_h // can_height # 24 // 12 = 2
    total_cans = cans_per_layer * num_layers  # 48 cans

    correct_ans = f"{total_cans} cans ({cans_per_layer} cans per layer × {num_layers} layers)"

    custom_opts = [
        correct_ans,
        f"{cans_per_layer} cans (1 single layer)",
        f"{total_cans + 12} cans",
        f"{total_cans * 2} cans",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the grid layout per layer using can diameter [1 mark]:\n"
        f"- Cans along length: {crate_l} cm ÷ {can_diameter} cm = {cans_l} cans.\n"
        f"- Cans along width: {crate_w} cm ÷ {can_diameter} cm = {cans_w} cans.\n"
        f"Cans per layer = {cans_l} × {cans_w} = {cans_per_layer} cans.\n\n"
        f"Step 2: Calculate the number of vertical layers [1 mark]:\n"
        f"Layers = {crate_h} cm ÷ {can_height} cm = {num_layers} layers.\n\n"
        f"Step 3: Multiply layer capacity by number of layers [1 mark]:\n"
        f"Total Cans = {cans_per_layer} × {num_layers} = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_44",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Use diameter to find grid size: (crate length ÷ diameter) × (crate width ÷ diameter) × (crate height ÷ can height).",
        tier_2=f"Length = {cans_l}, Width = {cans_w}, Layers = {num_layers}.",
        tier_3=f"Total = {cans_l} × {cans_w} × {num_layers} = {correct_ans}.",
        r=r,
    )
