"""Cluster 5: Surface Materials, Tiling, Paving & Turf (Subskills 37 to 44)."""
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

# --------------------------------------------------------------------------- #
# Subskill 37: Number of Floor Tiles Needed
# --------------------------------------------------------------------------- #
def _gen_area_tiling_floor_tile_count(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_tiling_floor_tile_count"
    name = r.choice(SA_NAMES)
    room_l = r.choice([4, 5, 6])
    room_w = r.choice([3, 4, 5])
    room_area = room_l * room_w
    # tile dimensions in cm: e.g. 50cm x 50cm = 0.25 m², 40cm x 40cm = 0.16 m²
    tile_cm = r.choice([50, 40, 25])
    tile_m = tile_cm / 100.0
    tile_area = round(tile_m * tile_m, 4)
    tiles_needed = math.ceil(room_area / tile_area)
    correct_ans = f"{tiles_needed} tiles"

    prompt = (
        f"{name} is tiling a rectangular bathroom floor measuring {room_l} m by {room_w} m.\n"
        f"Each square ceramic tile measures {tile_cm} cm by {tile_cm} cm.\n\n"
        f"Calculate the theoretical minimum number of tiles needed to cover the bathroom floor (ignoring cutting wastage)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Convert the tile dimensions from cm to metres first: {tile_cm} cm = {_fmt(tile_m)} m.\n"
        f"Then divide the total floor area by the area of one individual tile.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Room Area}} = {room_l} \\times {room_w} = {room_area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Tile Area}} = {_fmt(tile_m)} \\times {_fmt(tile_m)} = {_fmt(tile_area, 4)}\\text{{ m}}^2$$\n"
        f"$$\\text{{Number of tiles}} = \\frac{{{room_area}}}{{{_fmt(tile_area, 4)}}}$$ ✓ [1 Mark: Method – dividing room area by single tile area in consistent units]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Number of tiles}} = {tiles_needed}\\text{{ tiles}}$$ ✓ [1 Mark: Accuracy – accurate quotient]"
    )

    d1 = f"{room_area} tiles"  # assumed 1 m² per tile
    d2 = f"{tiles_needed + 20} tiles"
    d3 = f"{math.ceil(room_area / tile_m)} tiles"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Convert tile measurements from cm to metres first: divide by 100.",
        tier_2=f"Room area = {room_area} m², Tile area = {_fmt(tile_area, 4)} m².",
        tier_3=f"Number of tiles = {room_area} ÷ {_fmt(tile_area, 4)} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 38: Tile Boxes with 10% Wastage
# --------------------------------------------------------------------------- #
def _gen_area_tiling_boxes_with_wastage(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_tiling_boxes_with_wastage"
    name = r.choice(SA_NAMES)
    room_l = r.choice([5, 6, 7, 8])
    room_w = r.choice([4, 5, 6])
    room_area = room_l * room_w
    wastage_factor = 1.10
    total_area_with_waste = round(room_area * wastage_factor, 2)
    box_coverage = r.choice([1.44, 1.62, 1.92, 2.0])  # typical SA tile box coverage in m²
    boxes = math.ceil(total_area_with_waste / box_coverage)
    correct_ans = f"{boxes} boxes"

    prompt = (
        f"{name} is buying floor tiles for a kitchen with an area of {room_area} m².\n"
        f"An extra 10% must be added to allow for cutting and breakages.\n"
        f"Tiles are sold in whole boxes, where each box covers {_fmt(box_coverage)} m².\n\n"
        f"Calculate the minimum number of boxes of tiles that {name} must purchase."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Add 10% wastage to the room area: $\\text{{Area}} \\times 1,10$. Then divide by the box coverage and round UP to the next whole box, "
        f"because hardware stores do not sell partial boxes.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Area with 10\\% wastage}} = {room_area} \\times 1,10 = {_fmt(total_area_with_waste)}\\text{{ m}}^2$$\n"
        f"$$\\text{{Number of boxes}} = \\frac{{{_fmt(total_area_with_waste)}}}{{{_fmt(box_coverage)}}} = {_fmt(total_area_with_waste / box_coverage, 2)}$$ ✓ [1 Mark: Method – adding 10% and dividing by box coverage]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"Round up to the nearest whole box: **{boxes} boxes** ✓ [1 Mark: Accuracy – correct upward rounding to whole boxes]"
    )

    d1 = f"{math.floor(total_area_with_waste / box_coverage)} boxes"  # rounded down
    d2 = f"{math.ceil(room_area / box_coverage)} boxes"  # forgot 10% wastage
    d3 = f"{boxes + 3} boxes"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add 10% to the area: multiply by 1,10.",
        tier_2=f"Divide {_fmt(total_area_with_waste)} m² by {_fmt(box_coverage)} m² per box.",
        tier_3=f"Always round UP to the next whole box: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 39: Total Cost of Tiling Project
# --------------------------------------------------------------------------- #
def _gen_area_tiling_total_cost_calculation(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_tiling_total_cost_calculation"
    name = r.choice(SA_NAMES)
    boxes = r.choice([15, 18, 20, 24, 28, 30])
    price_per_box = r.choice([189.90, 219.50, 249.00, 275.00, 299.90])
    adhesive_bags = math.ceil(boxes / 5)  # 1 bag per 5 boxes
    adhesive_price = 85.00
    tile_total = boxes * price_per_box
    adhesive_total = adhesive_bags * adhesive_price
    project_total = tile_total + adhesive_total
    correct_ans = _fmt_curr(project_total)

    prompt = (
        f"{name} is buying materials for a home tiling project.\n"
        f"  • {boxes} boxes of floor tiles at {_fmt_curr(price_per_box)} per box\n"
        f"  • {adhesive_bags} bags of tile adhesive at {_fmt_curr(adhesive_price)} per bag\n\n"
        f"Calculate the total cost of the tiling materials."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate the total cost of the tile boxes and adhesive bags separately, then sum them together.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Tile boxes cost}} = {boxes} \\times {_fmt_curr(price_per_box)} = {_fmt_curr(tile_total)}$$\n"
        f"$$\\text{{Adhesive cost}} = {adhesive_bags} \\times {_fmt_curr(adhesive_price)} = {_fmt_curr(adhesive_total)}$$\n"
        f"$$\\text{{Total Cost}} = {_fmt_curr(tile_total)} + {_fmt_curr(adhesive_total)}$$ ✓ [1 Mark: Method – multiplying unit prices and summing]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Cost}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate Rand sum with 2 decimal places]"
    )

    d1 = _fmt_curr(tile_total)  # forgot adhesive
    d2 = _fmt_curr(project_total + 100)
    d3 = _fmt_curr(project_total * 0.9)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the quantities by their unit prices and add the results.",
        tier_2=f"Tiles = {_fmt_curr(tile_total)}, Adhesive = {_fmt_curr(adhesive_total)}.",
        tier_3=f"Total cost = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 40: Cobblestone Pavers Count
# --------------------------------------------------------------------------- #
def _gen_area_paving_cobblestones_count(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_paving_cobblestones_count"
    name = r.choice(SA_NAMES)
    patio_l = r.choice([6, 8, 10, 12])
    patio_w = r.choice([4, 5, 6])
    patio_area = patio_l * patio_w
    # standard cobblestone: 10 cm x 10 cm = 0.01 m² -> 100 pavers per m²
    # or 20 cm x 10 cm = 0.02 m² -> 50 pavers per m²
    paver_choice = r.choice([
        (10, 10, 100, "10 cm × 10 cm"),
        (20, 10, 50, "20 cm × 10 cm"),
        (20, 20, 25, "20 cm × 20 cm"),
    ])
    pl, pw, per_m2, desc = paver_choice
    pavers_needed = patio_area * per_m2
    correct_ans = f"{_fmt(pavers_needed)} pavers"

    prompt = (
        f"{name} is paving a driveway measuring {patio_l} m by {patio_w} m with cobblestones.\n"
        f"Each cobblestone has dimensions {desc}.\n"
        f"There are {per_m2} cobblestones per square metre (m²).\n\n"
        f"Calculate the total number of cobblestones required to pave the driveway."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First calculate the area of the driveway ($l \\times w$). Then multiply the area by the number of pavers required per square metre.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Driveway Area}} = {patio_l} \\times {patio_w} = {patio_area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Total pavers}} = {patio_area} \\times {per_m2}$$ ✓ [1 Mark: Method – multiplying driveway area by pavers per m²]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total pavers}} = {_fmt(pavers_needed)}\\text{{ pavers}}$$ ✓ [1 Mark: Accuracy – accurate product]"
    )

    d1 = f"{_fmt(patio_area)} pavers"
    d2 = f"{_fmt(pavers_needed // 2)} pavers"
    d3 = f"{_fmt(pavers_needed + per_m2 * 2)} pavers"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Driveway Area = length × width.",
        tier_2=f"Multiply driveway area ({patio_area} m²) by {per_m2} pavers/m².",
        tier_3=f"Total pavers = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 41: Paving Batches & Cost
# --------------------------------------------------------------------------- #
def _gen_area_paving_batches_and_cost(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_paving_batches_and_cost"
    name = r.choice(SA_NAMES)
    pavers_needed = r.choice([1650, 2100, 2400, 2850, 3200])
    batch_size = 500  # standard pallet / batch
    price_per_batch = r.choice([1250.00, 1450.00, 1600.00, 1850.00])
    batches = math.ceil(pavers_needed / batch_size)
    total_cost = batches * price_per_batch
    correct_ans = _fmt_curr(total_cost)

    prompt = (
        f"{name} requires {pavers_needed} cobblestone pavers for a patio project.\n"
        f"The brick supplier sells cobblestones only in full pallets (batches) of {batch_size} pavers.\n"
        f"Each pallet costs {_fmt_curr(price_per_batch)}.\n\n"
        f"Calculate the total cost to purchase the required pallets of cobblestones."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Divide the total pavers required by the batch size and round UP to the nearest whole pallet, "
        f"then multiply by the pallet price.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Pallets needed}} = \\frac{{{pavers_needed}}}{{{batch_size}}} = {_fmt(pavers_needed / batch_size, 2)} \\implies {batches}\\text{{ pallets}}$$\n"
        f"$$\\text{{Total Cost}} = {batches} \\times {_fmt_curr(price_per_batch)}$$ ✓ [1 Mark: Method – rounding up to whole pallets and multiplying by price]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Cost}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    d1 = _fmt_curr((pavers_needed / batch_size) * price_per_batch)  # exact fractional cost
    d2 = _fmt_curr((batches - 1) * price_per_batch)  # rounded down
    d3 = _fmt_curr(total_cost + price_per_batch)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine how many pallets are needed by rounding up.",
        tier_2=f"{pavers_needed} ÷ {batch_size} = {_fmt(pavers_needed / batch_size, 2)} → {batches} pallets.",
        tier_3=f"Total cost = {batches} × {_fmt_curr(price_per_batch)} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 42: Instant Turf Grass Rolls
# --------------------------------------------------------------------------- #
def _gen_area_turf_grass_rolls_and_wastage(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_turf_grass_rolls_and_wastage"
    name = r.choice(SA_NAMES)
    lawn_l = r.choice([10, 12, 14, 15, 18])
    lawn_w = r.choice([6, 8, 10])
    lawn_area = lawn_l * lawn_w
    # each turf roll is 1m x 0.5m = 0.5 m² (standard Kikuyu / Buffalo roll in SA)
    roll_area = 0.5
    raw_rolls = lawn_area / roll_area  # 2 rolls per m²
    total_rolls = math.ceil(raw_rolls * 1.05)  # 5% cutting wastage
    correct_ans = f"{total_rolls} rolls"

    prompt = (
        f"{name} is laying instant lawn turf rolls in a backyard measuring {lawn_l} m by {lawn_w} m.\n"
        f"Each roll of instant turf measures 1 m long by 0,5 m wide (area = 0,5 m²).\n"
        f"An extra 5% must be added to the total number of rolls to allow for trimming and cutting.\n\n"
        f"Calculate the total number of rolls of instant lawn needed (rounded up to the next whole roll)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First calculate the lawn area ($l \\times w$). Since each roll covers 0,5 m², each square metre needs 2 rolls.\n"
        f"Then add 5% for cutting wastage and round up.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Lawn Area}} = {lawn_l} \\times {lawn_w} = {lawn_area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Base rolls}} = \\frac{{{lawn_area}}}{{0,5}} = {int(raw_rolls)}\\text{{ rolls}}$$\n"
        f"$$\\text{{With 5\\% wastage}} = {int(raw_rolls)} \\times 1,05 = {_fmt(raw_rolls * 1.05, 1)}$$ ✓ [1 Mark: Method – calculating rolls and applying 5% wastage]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"Round up to next whole roll: **{total_rolls} rolls** ✓ [1 Mark: Accuracy – accurate upward rounding]"
    )

    d1 = f"{int(raw_rolls)} rolls"  # forgot wastage
    d2 = f"{math.floor(raw_rolls * 1.05)} rolls"
    d3 = f"{total_rolls + 10} rolls"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the lawn area, then divide by 0,5 m² per roll.",
        tier_2=f"Lawn area = {lawn_area} m² → {int(raw_rolls)} rolls. Multiply by 1,05 for 5% waste.",
        tier_3=f"Round up to whole rolls: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 43: Carpet Roll and Underlay Budget
# --------------------------------------------------------------------------- #
def _gen_area_carpet_roll_and_underlay_budget(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_carpet_roll_and_underlay_budget"
    name = r.choice(SA_NAMES)
    room_l = r.choice([5, 6, 7])
    room_w = r.choice([4, 5])
    area = room_l * room_w
    carpet_rate = r.choice([165.00, 195.00, 220.00, 250.00])
    underlay_rate = 45.00
    combined_rate = carpet_rate + underlay_rate
    total_cost = area * combined_rate
    correct_ans = _fmt_curr(total_cost)

    prompt = (
        f"{name} is installing wall-to-wall carpeting in a bedroom measuring {room_l} m by {room_w} m.\n"
        f"The carpet costs {_fmt_curr(carpet_rate)} per m² and the rubber underlay costs {_fmt_curr(underlay_rate)} per m².\n\n"
        f"Calculate the total cost for carpeting and underlay for this room."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Find the room area ($l \\times w$) and multiply by the combined cost per square metre of carpet plus underlay.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Room Area}} = {room_l} \\times {room_w} = {area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Combined rate}} = {_fmt_curr(carpet_rate)} + {_fmt_curr(underlay_rate)} = {_fmt_curr(combined_rate)}\\text{{ / m}}^2$$\n"
        f"$$\\text{{Total Cost}} = {area} \\times {_fmt_curr(combined_rate)}$$ ✓ [1 Mark: Method – multiplying room area by combined rate per m²]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Cost}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    d1 = _fmt_curr(area * carpet_rate)  # forgot underlay
    d2 = _fmt_curr(total_cost * 1.1)
    d3 = _fmt_curr(total_cost - 200)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply room area by the combined rate (carpet + underlay).",
        tier_2=f"Area = {area} m², combined rate = {_fmt_curr(combined_rate)}/m².",
        tier_3=f"Total cost = {area} × {_fmt_curr(combined_rate)} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 44: Swimming Pool Cover with Overlap Border
# --------------------------------------------------------------------------- #
def _gen_area_swimming_pool_cover_with_overlap(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_swimming_pool_cover_with_overlap"
    name = r.choice(SA_NAMES)
    pool_l = r.choice([8, 10, 12])
    pool_w = r.choice([4, 5, 6])
    overlap = 0.5  # 0.5 m overlap on all sides
    cover_l = pool_l + 2 * overlap
    cover_w = pool_w + 2 * overlap
    cover_area = round(cover_l * cover_w, 2)
    correct_ans = f"{_fmt(cover_area)} m²"

    prompt = (
        f"{name} is purchasing a thermal safety cover for a rectangular swimming pool measuring {pool_l} m by {pool_w} m.\n"
        f"To anchor the cover securely, it must overlap the pool edges by 0,5 m on all four sides.\n\n"
        f"Calculate the total area of the pool cover needed."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"An overlap of 0,5 m on all sides adds to both ends of the length and both ends of the width.\n"
        f"Cover length = $\\text{{pool length}} + 2(0,5\\text{{ m}}) = {pool_l} + 1 = {cover_l}\\text{{ m}}$.\n"
        f"Cover width = $\\text{{pool width}} + 2(0,5\\text{{ m}}) = {pool_w} + 1 = {cover_w}\\text{{ m}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Cover Length}} = {pool_l} + (2 \\times 0,5) = {cover_l}\\text{{ m}}$$\n"
        f"$$\\text{{Cover Width}} = {pool_w} + (2 \\times 0,5) = {cover_w}\\text{{ m}}$$\n"
        f"$$\\text{{Cover Area}} = {cover_l} \\times {cover_w}$$ ✓ [1 Mark: Method – adding overlap to both sides and multiplying]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Cover Area}} = {_fmt(cover_area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate product with units]"
    )

    d1 = f"{pool_l * pool_w} m²"  # exact pool area
    d2 = f"{(pool_l + overlap) * (pool_w + overlap)} m²"  # only added overlap once
    d3 = f"{_fmt(round(cover_area + 4, 2))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add 2 × 0,5 m = 1 m to both the length and width.",
        tier_2=f"Cover length = {cover_l} m, cover width = {cover_w} m.",
        tier_3=f"Cover area = {cover_l} × {cover_w} = {correct_ans}.",
        r=r,
    )
