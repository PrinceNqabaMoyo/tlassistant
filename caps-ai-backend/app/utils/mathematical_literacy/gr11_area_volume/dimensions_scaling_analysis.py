"""Subskills 45 to 52: Dimensions Scaling, Proportions & Critical Reasoning for Grade 11 Mathematical Literacy."""
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


def generate_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Subskill 45: Effect on perimeter and area when doubling the length of a rectangular garden."""
    l = r.randint(6, 10)
    w = r.randint(4, 6)

    prompt = (
        f"A rectangular garden initially measures **{l} m** long by **{w} m** wide.\n"
        f"The owner decides to **double the length** (to {2 * l} m) while keeping the width unchanged at {w} m.\n\n"
        f"What is the mathematical effect of this single-dimension doubling on the garden's **perimeter** and **area**?"
    )

    old_p = 2 * (l + w)
    new_p = 2 * (2 * l + w)
    old_a = l * w
    new_a = (2 * l) * w

    correct_ans = f"The area exactly doubles (from {old_a} m² to {new_a} m²), while the perimeter increases from {old_p} m to {new_p} m (does NOT double)."
    opt_b = f"Both the area and the perimeter double exactly."
    opt_c = f"The perimeter doubles, but the area quadruples."
    opt_d = f"Neither the area nor the perimeter changes."

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Calculate initial perimeter and area [1 mark]:\n"
        f"P1 = 2({l} + {w}) = {old_p} m. A1 = {l} × {w} = {old_a} m².\n\n"
        f"Step 2: Calculate new perimeter and area after doubling length [1 mark]:\n"
        f"P2 = 2({2 * l} + {w}) = {new_p} m. A2 = {2 * l} × {w} = {new_a} m².\n\n"
        f"Step 3: Compare results [1 mark]:\n"
        f"A2 ÷ A1 = {new_a} ÷ {old_a} = 2 (area doubles). Perimeter increases by {2*l} m but does not double."
    )

    return _build_question_payload(
        subskill_id="subskill_45",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate initial perimeter and area, then calculate the new values with length doubled.",
        tier_2=f"Old: P = {old_p} m, A = {old_a} m². New: P = {new_p} m, A = {new_a} m².",
        tier_3=f"Conclusion: {correct_ans}.",
        r=r,
    )


def generate_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Subskill 46: Effect on area when both length and width are doubled (4x increase)."""
    l = r.randint(4, 8)
    w = r.randint(3, 5)

    prompt = (
        f"A rectangular lawn has dimensions **{l} m × {w} m**.\n"
        f"If the landscaper **doubles both the length AND the width** (to {2 * l} m × {2 * w} m), "
        f"by what factor does the total lawn area increase?"
    )

    old_area = l * w
    new_area = (2 * l) * (2 * w)
    factor = 4

    correct_ans = f"Increases by a factor of 4 (quadruples from {old_area} m² to {new_area} m²)"

    opt_b = f"Increases by a factor of 2 (doubles from {old_area} m² to {2 * old_area} m²)"
    opt_c = f"Increases by a factor of 8 (from {old_area} m² to {8 * old_area} m²)"
    opt_d = f"Increases by a factor of 16"

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Calculate original area [1 mark]:\n"
        f"Original Area = {l} m × {w} m = {old_area} m².\n\n"
        f"Step 2: Calculate new area with both dimensions doubled [1 mark]:\n"
        f"New Area = ({2*l} m) × ({2*w} m) = (2 × 2) × ({l} × {w}) = 4 × {old_area} = {new_area} m².\n\n"
        f"Step 3: Stated ratio [1 mark]:\n"
        f"Area factor = {new_area} ÷ {old_area} = 4 (Area increases by 2² = 4 times)."
    )

    return _build_question_payload(
        subskill_id="subskill_46",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="When all 2D dimensions are scaled by factor k, area increases by k² = 2² = 4.",
        tier_2=f"Old area = {old_area}. New area = {2*l} × {2*w} = {new_area}. Factor = {new_area} ÷ {old_area}.",
        tier_3=f"Factor is 4 (quadrupled): {correct_ans}.",
        r=r,
    )


def generate_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: Effect on volume of a rectangular prism when all dimensions are doubled (8x increase)."""
    l, w, h = 3, 2, 2

    prompt = (
        f"A small water reservoir has dimensions length = **3 m**, width = **2 m**, depth = **2 m**.\n"
        f"If the municipality constructs a larger reservoir where **all three linear dimensions are doubled** "
        f"(length = 6 m, width = 4 m, depth = 4 m), by what factor does the water storage capacity increase?"
    )

    old_vol = l * w * h  # 12 m3
    new_vol = (2 * l) * (2 * w) * (2 * h)  # 6 * 4 * 4 = 96 m3
    factor = 8

    correct_ans = f"Increases by a factor of 8 (from {old_vol} m³ to {new_vol} m³)"

    opt_b = f"Increases by a factor of 2 (doubles to {2 * old_vol} m³)"
    opt_c = f"Increases by a factor of 4 (quadruples to {4 * old_vol} m³)"
    opt_d = f"Increases by a factor of 6 (to {6 * old_vol} m³)"

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Calculate original volume [1 mark]:\n"
        f"V1 = 3 m × 2 m × 2 m = {old_vol} m³.\n\n"
        f"Step 2: Calculate new volume with all 3 dimensions doubled [1 mark]:\n"
        f"V2 = 6 m × 4 m × 4 m = {new_vol} m³.\n\n"
        f"Step 3: Calculate factor of increase [1 mark]:\n"
        f"Factor = {new_vol} ÷ {old_vol} = 8 (Because 2 × 2 × 2 = 2³ = 8).\n"
        f"Conclusion: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_47",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="When all three dimensions of a 3D solid double, the volume increases by 2³ = 8 times.",
        tier_2=f"Old = 3 × 2 × 2 = {old_vol} m³. New = 6 × 4 × 4 = {new_vol} m³. Ratio = {new_vol} ÷ {old_vol}.",
        tier_3=f"Factor is 8: {correct_ans}.",
        r=r,
    )


def generate_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Effect on cylinder volume when doubling radius vs doubling height."""
    r_val = 1.0  # m
    h_val = 2.0  # m

    prompt = (
        f"An engineer evaluates two modifications to a cylindrical storage tank ($V = \\pi r^2 h$):\n"
        f"- **Tank A**: Double the radius ($2r$) while keeping height ($h$) constant.\n"
        f"- **Tank B**: Double the height ($2h$) while keeping radius ($r$) constant.\n\n"
        f"Which modification produces the **GREATEST increase in volume**, and why?"
    )

    correct_ans = (
        f"Tank A, because radius is squared in the volume formula: doubling radius multiplies volume by 2² = 4, "
        f"whereas doubling height only multiplies volume by 2."
    )
    opt_b = f"Tank B, because height directly controls the gravitational pressure head."
    opt_c = f"Both modifications produce identical volumes because multiplication is commutative."
    opt_d = f"Neither modification increases volume."

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Test doubling radius in formula [1 mark]:\n"
        f"V_new = $\\pi \\times (2r)^2 \\times h = \\pi \\times 4r^2 \\times h = 4 \\times (\\pi r^2 h)$ (Volume quadruples, 4×).\n\n"
        f"Step 2: Test doubling height in formula [1 mark]:\n"
        f"V_new = $\\pi \\times r^2 \\times (2h) = 2 \\times (\\pi r^2 h)$ (Volume doubles, 2×).\n\n"
        f"Step 3: Stated conclusion [1 mark]:\n"
        f"{correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_48",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Radius is squared in the formula V = πr²h. Scaling radius by 2 gives 2² = 4 times the volume.",
        tier_2="Tank A volume factor = 4. Tank B volume factor = 2.",
        tier_3=f"Correct answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Surface area to volume ratio (SA/V) comparison of two water tanks for heat loss."""
    # Tank 1: Small cube 1m x 1m x 1m -> SA = 6 m2, V = 1 m3 -> SA/V = 6
    # Tank 2: Large cube 2m x 2m x 2m -> SA = 24 m2, V = 8 m3 -> SA/V = 3
    
    prompt = (
        f"In solar water heating, tanks lose heat through their exterior surface area.\n"
        f"A thermal engineer calculates the **Surface Area to Volume ratio (SA/V)** for two cubical hot water storage tanks:\n"
        f"- **Tank 1 (Small)**: side = **1 m** (Volume = 1 m³; Surface Area = 6 m²).\n"
        f"- **Tank 2 (Large)**: side = **2 m** (Volume = 8 m³; Surface Area = 24 m²).\n\n"
        f"Calculate the **SA/V ratio** for both tanks, and identify which tank loses heat **more slowly per unit volume**."
    )

    ratio_1 = 6.0 / 1.0  # 6.0
    ratio_2 = 24.0 / 8.0 # 3.0

    correct_ans = f"Tank 1 ratio = 6 : 1; Tank 2 ratio = 3 : 1; Tank 2 retains heat better (lower SA/V ratio)"
    opt_b = f"Tank 1 ratio = 3 : 1; Tank 2 ratio = 6 : 1; Tank 1 retains heat better"
    opt_c = f"Both tanks have identical ratio of 4 : 1"
    opt_d = f"Tank 1 ratio = 1 : 6; Tank 2 ratio = 1 : 3; Tank 1 retains heat better"

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Calculate SA/V ratio for Tank 1 [1 mark]:\n"
        f"Tank 1: 6 m² ÷ 1 m³ = 6 m⁻¹ (ratio 6 : 1).\n\n"
        f"Step 2: Calculate SA/V ratio for Tank 2 [1 mark]:\n"
        f"Tank 2: 24 m² ÷ 8 m³ = 3 m⁻¹ (ratio 3 : 1).\n\n"
        f"Step 3: Thermal interpretation [1 mark]:\n"
        f"A smaller SA/V ratio means less exposed surface area per unit of stored volume, so Tank 2 cools down much more slowly."
    )

    return _build_question_payload(
        subskill_id="subskill_49",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide surface area by volume for each tank. Lower ratio = better heat retention.",
        tier_2="Tank 1 = 6 ÷ 1 = 6. Tank 2 = 24 ÷ 8 = 3.",
        tier_3=f"Result: {correct_ans}.",
        r=r,
    )


def generate_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: Cost efficiency comparison: price per litre between different packaged liquid containers."""
    p_500ml = 12.50
    p_2l = 32.00
    p_5l = 65.00

    prompt = (
        f"A shopper compares three different packaging sizes of swimming pool algaecide at Makro:\n\n"
        f"| Package Size | Bottle Volume | Retail Price |\n"
        f"| :--- | :--- | :--- |\n"
        f"| Bottle A | 500 mℓ (0,5 ℓ) | {_fmt_curr(p_500ml)} |\n"
        f"| Bottle B | 2 Litres | {_fmt_curr(p_2l)} |\n"
        f"| Bottle C | 5 Litres | {_fmt_curr(p_5l)} |\n\n"
        f"Calculate the **unit price per litre** for each container size, and determine which bottle provides the **best value for money**."
    )

    rate_a = p_500ml / 0.5   # R 25.00 / L
    rate_b = p_2l / 2.0      # R 16.00 / L
    rate_c = p_5l / 5.0      # R 13.00 / L

    correct_ans = f"A: {_fmt_curr(rate_a)}/ℓ, B: {_fmt_curr(rate_b)}/ℓ, C: {_fmt_curr(rate_c)}/ℓ; Bottle C is best value"

    custom_opts = [
        correct_ans,
        f"A: {_fmt_curr(rate_a)}/ℓ, B: {_fmt_curr(rate_b)}/ℓ, C: {_fmt_curr(rate_c)}/ℓ; Bottle A is best value",
        f"A: {_fmt_curr(p_500ml)}/ℓ, B: {_fmt_curr(p_2l)}/ℓ, C: {_fmt_curr(p_5l)}/ℓ; Bottle A is best value",
        f"All bottles have the exact same unit price per litre",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate unit price per litre for each bottle [1 mark]:\n"
        f"- Bottle A: {_fmt_curr(p_500ml)} ÷ 0,5 ℓ = {_fmt_curr(rate_a)}/ℓ.\n"
        f"- Bottle B: {_fmt_curr(p_2l)} ÷ 2 ℓ = {_fmt_curr(rate_b)}/ℓ.\n"
        f"- Bottle C: {_fmt_curr(p_5l)} ÷ 5 ℓ = {_fmt_curr(rate_c)}/ℓ.\n\n"
        f"Step 2: Compare rates [1 mark]:\n"
        f"Bottle C has the lowest unit cost per litre at {_fmt_curr(rate_c)}/ℓ.\n\n"
        f"Step 3: Stated answer [1 mark]:\n"
        f"{correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_50",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide price by litres to find rate per litre for each bottle.",
        tier_2=f"A = {p_500ml} ÷ 0,5 = R {rate_a:.2f}. B = {p_2l} ÷ 2 = R {rate_b:.2f}. C = {p_5l} ÷ 5 = R {rate_c:.2f}.",
        tier_3=f"Conclusion: {correct_ans}.",
        r=r,
    )


def generate_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: Irregular composite building excavation soil volume with bulking factor."""
    l = r.randint(8, 12)  # m
    w = r.randint(5, 8)   # m
    depth = round(r.choice([1.2, 1.5, 1.8]), 1)  # m
    bulking_pct = 20  # 20% soil expansion upon excavation (bulking factor = 1.20)
    truck_capacity_m3 = 6  # 6 m3 tipper truck

    prompt = (
        f"An earthmoving team excavates a foundation trench measuring **{l} m** long, **{w} m** wide, and **{_fmt(depth)} m** deep.\n"
        f"When solid in-situ earth is dug up, it loosens and expands by **20%** in volume (bulking factor = 1,20).\n"
        f"The loose soil must be carted away using tipper trucks with a capacity of **{truck_capacity_m3} m³** each.\n\n"
        f"Calculate the **loose soil volume** in m³ and the **minimum number of full truck loads** required."
    )

    in_situ_vol = round(l * w * depth, 2)
    loose_vol = round(in_situ_vol * 1.20, 2)
    truck_loads = int(math.ceil(loose_vol / truck_capacity_m3))

    correct_ans = f"{_fmt(loose_vol)} m³ ({truck_loads} truck loads)"

    # Distractor: without bulking factor
    no_bulk_loads = int(math.ceil(in_situ_vol / truck_capacity_m3))
    dist_no_bulk = f"{_fmt(in_situ_vol)} m³ ({no_bulk_loads} truck loads)"

    custom_opts = [
        correct_ans,
        dist_no_bulk,
        f"{_fmt(loose_vol)} m³ ({truck_loads + 5} truck loads)",
        f"{_fmt(round(loose_vol * 2, 2))} m³ ({truck_loads * 2} truck loads)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the solid in-situ trench volume [1 mark]:\n"
        f"In-situ Volume = {l} m × {w} m × {_fmt(depth)} m = {_fmt(in_situ_vol)} m³.\n\n"
        f"Step 2: Apply 20% bulking expansion factor [1 mark]:\n"
        f"Loose Volume = {_fmt(in_situ_vol)} m³ × 1,20 = {_fmt(loose_vol)} m³.\n\n"
        f"Step 3: Divide by tipper truck capacity and round up to whole loads [1 mark]:\n"
        f"Truck loads = {_fmt(loose_vol)} m³ ÷ {truck_capacity_m3} m³ = {loose_vol / truck_capacity_m3:.2f} -> {truck_loads} loads.\n"
        f"Conclusion: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_51",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate trench volume (l × w × d), multiply by 1,20 for soil bulking, then divide by truck capacity and round up.",
        tier_2=f"In-situ = {in_situ_vol} m³. Loose = {in_situ_vol} × 1,20 = {loose_vol} m³. Truck loads = {loose_vol} ÷ {truck_capacity_m3}.",
        tier_3=f"Result: {correct_ans}.",
        r=r,
    )


def generate_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Comprehensive home renovation project budgeting."""
    # Combining Paint, Tiles, Skirting, and Labour
    room_l, room_w = 6, 4
    room_h = 2.8
    
    # 1. Floor tiles: Area = 24 m2 + 10% waste = 26.4 m2 -> 19 boxes @ R 180 = R 3 420.00
    net_floor = room_l * room_w
    boxes = int(math.ceil(net_floor * 1.10 / 1.44))
    cost_tiles = boxes * 180.0
    
    # 2. Skirting: 2(6+4) - 0.9m door = 19.1m @ R 45/m = R 859.50
    skirting_m = 2 * (room_l + room_w) - 0.9
    cost_skirting = round(skirting_m * 45.0, 2)
    
    # 3. Wall paint: Wall area = 2(6+4)*2.8 = 56 m2 minus door (1.9m2) = 54.1 m2.
    # 2 coats @ 10 m2/L = 10.82 L -> 1x 20L tin @ R 1 350.00
    cost_paint = 1350.0
    
    # 4. Contractor labour: 3 days @ R 650/day = R 1 950.00
    cost_labour = 3 * 650.0

    total_budget = cost_tiles + cost_skirting + cost_paint + cost_labour

    prompt = (
        f"A homeowner prepares a budget estimate to renovate a rectangular home office ({room_l} m × {room_w} m with {room_h} m ceiling):\n\n"
        f"| Item | Quantity & Rate | Subtotal |\n"
        f"| :--- | :--- | :--- |\n"
        f"| Floor Tiles | {boxes} boxes @ R 180,00/box | {_fmt_curr(cost_tiles)} |\n"
        f"| Skirting Boards | {_fmt(skirting_m)} m @ R 45,00/m | {_fmt_curr(cost_skirting)} |\n"
        f"| Wall Paint | 1 × 20 ℓ tin acrylic paint | {_fmt_curr(cost_paint)} |\n"
        f"| Renovation Labour | 3 days @ R 650,00/day | {_fmt_curr(cost_labour)} |\n\n"
        f"Calculate the **grand total renovation project budget** including all materials and contractor labour."
    )

    correct_ans = _fmt_curr(total_budget)

    custom_opts = [
        correct_ans,
        _fmt_curr(total_budget - cost_labour),  # Forgot labour
        _fmt_curr(total_budget - cost_paint),   # Forgot paint
        _fmt_curr(total_budget + 850.0),
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate material subtotals [1 mark]:\n"
        f"- Tiles: {_fmt_curr(cost_tiles)}.\n"
        f"- Skirting: {_fmt_curr(cost_skirting)}.\n"
        f"- Paint: {_fmt_curr(cost_paint)}.\n"
        f"Total Materials = {_fmt_curr(cost_tiles + cost_skirting + cost_paint)}.\n\n"
        f"Step 2: Add contractor labour cost [1 mark]:\n"
        f"Labour = 3 days × R 650,00 = {_fmt_curr(cost_labour)}.\n\n"
        f"Step 3: Sum grand total project budget [1 mark]:\n"
        f"Grand Total = {_fmt_curr(cost_tiles + cost_skirting + cost_paint)} + {_fmt_curr(cost_labour)} = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_52",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add up the four itemized budget categories: tiles + skirting + paint + labour.",
        tier_2=f"Materials = R {cost_tiles + cost_skirting + cost_paint:.2f}. Labour = R {cost_labour:.2f}.",
        tier_3=f"Grand Total Budget = {correct_ans}.",
        r=r,
    )
