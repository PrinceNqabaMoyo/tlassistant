"""Subskills 28 to 36: Volume, Capacity, Liquid Conversions & Flow Rates for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Subskill 28: Volume of a rectangular shipping container in m³."""
    # Standard 20ft container dimensions approx: 6.0m x 2.4m x 2.6m
    l = round(r.choice([6.0, 12.0]), 1)  # 20ft or 40ft
    w = round(r.choice([2.4, 2.5]), 1)
    h = round(r.choice([2.6, 2.9]), 1)  # standard or high cube

    prompt = (
        f"A freight logistics company loads cargo into a standard rectangular ISO intermodal shipping container.\n"
        f"The internal dimensions of the container are:\n"
        f"- Length ($l$) = **{_fmt(l)} m**\n"
        f"- Width ($w$) = **{_fmt(w)} m**\n"
        f"- Height ($h$) = **{_fmt(h)} m**\n\n"
        f"Calculate the **internal cubic volume (capacity)** of the shipping container in **cubic metres (m³)**.\n"
        f"*(Formula: $\\text{{Volume}} = l \\times w \\times h$. Round to 2 decimal places)*"
    )

    vol = round(l * w * h, 2)
    correct_ans = f"{_fmt(vol)} m³"

    # Distractor: Surface area
    sa = round(2 * (l * w + l * h + w * h), 2)
    dist_sa = f"{_fmt(sa)} m³"

    custom_opts = [
        correct_ans,
        dist_sa,
        f"{_fmt(round(vol / 2, 2))} m³",
        f"{_fmt(round(vol + 12.4, 2))} m³",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State the formula for volume of a rectangular prism [1 mark]:\n"
        f"Volume = length × width × height.\n\n"
        f"Step 2: Substitute dimensions [1 mark]:\n"
        f"Volume = {_fmt(l)} m × {_fmt(w)} m × {_fmt(h)} m.\n\n"
        f"Step 3: Calculate volume with units [1 mark]:\n"
        f"Volume = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_28",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the three perpendicular dimensions: length × width × height.",
        tier_2=f"Volume = {l} × {w} × {h}.",
        tier_3=f"Volume = {correct_ans}.",
        r=r,
    )


def generate_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Subskill 29: Capacity of a rectangular swimming pool in litres (1 m³ = 1 000 L)."""
    length = r.randint(8, 12)  # m
    width = r.randint(4, 6)    # m
    avg_depth = round(r.choice([1.4, 1.5, 1.6, 1.8]), 1)  # m

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is building a rectangular swimming pool with uniform average depth.\n"
        f"The pool is **{length} m** long, **{width} m** wide, and has an average water depth of **{_fmt(avg_depth)} m**.\n\n"
        f"Calculate the **volume** of the pool in cubic metres (m³) and its **water capacity in litres (ℓ)**.\n"
        f"*(Note: $1\\text{{ m}}^3 = 1\\ 000\\text{{ litres}}$)*"
    )

    vol_m3 = round(length * width * avg_depth, 2)
    capacity_litres = int(round(vol_m3 * 1000))

    correct_ans = f"{_fmt(vol_m3)} m³ ({_fmt(capacity_litres)} ℓ)"

    # Distractor: 1 m3 = 100 L
    dist_100 = f"{_fmt(vol_m3)} m³ ({_fmt(int(vol_m3 * 100))} ℓ)"
    # Distractor: Surface area
    dist_sa = f"{_fmt(round(length * width, 2))} m³ ({_fmt(int(length * width * 1000))} ℓ)"

    custom_opts = [
        correct_ans,
        dist_100,
        dist_sa,
        f"{_fmt(vol_m3 + 10)} m³ ({_fmt(capacity_litres + 10000)} ℓ)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate volume in cubic metres [1 mark]:\n"
        f"Volume = length × width × depth = {length} m × {width} m × {_fmt(avg_depth)} m = {_fmt(vol_m3)} m³.\n\n"
        f"Step 2: Convert cubic metres to litres using 1 m³ = 1 000 ℓ [1 mark]:\n"
        f"Capacity = {_fmt(vol_m3)} × 1 000 = {_fmt(capacity_litres)} ℓ.\n\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_29",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Volume = l × w × d. Then multiply by 1 000 to convert m³ to litres.",
        tier_2=f"Volume = {length} × {width} × {avg_depth} = {vol_m3} m³. Multiply by 1 000.",
        tier_3=f"Capacity = {correct_ans}.",
        r=r,
    )


def generate_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Subskill 30: Swimming pool water volume filled to freeboard level (below rim)."""
    l = 10.0  # m
    w = 5.0   # m
    wall_height = 1.8  # m
    freeboard_cm = r.choice([15, 20, 25])  # cm below rim
    freeboard_m = freeboard_cm / 100.0

    prompt = (
        f"A rectangular municipal swimming pool has walls that are **{_fmt(l)} m** long, **{_fmt(w)} m** wide, and **{_fmt(wall_height)} m** deep.\n"
        f"For safety and wave overflow protection, the pool is filled with water up to **{freeboard_cm} cm** below the top coping edge.\n\n"
        f"Calculate the **actual volume of water** inside the pool in **litres**.\n"
        f"*(Note: $1\\text{{ m}}^3 = 1\\ 000\\text{{ litres}}$)*"
    )

    water_depth = round(wall_height - freeboard_m, 2)
    water_vol_m3 = round(l * w * water_depth, 2)
    water_litres = int(round(water_vol_m3 * 1000))

    correct_ans = f"{_fmt(water_litres)} ℓ"

    # Distractor filled to the brim
    full_litres = int(round(l * w * wall_height * 1000))
    dist_full = f"{_fmt(full_litres)} ℓ"

    custom_opts = [
        correct_ans,
        dist_full,
        f"{_fmt(int(water_litres * 0.8))} ℓ",
        f"{_fmt(water_litres + 5000)} ℓ",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the actual depth of water by subtracting freeboard [1 mark]:\n"
        f"Water Depth = {_fmt(wall_height)} m - {_fmt(freeboard_m)} m = {_fmt(water_depth)} m.\n\n"
        f"Step 2: Calculate water volume in m³ [1 mark]:\n"
        f"Volume = {_fmt(l)} m × {_fmt(w)} m × {_fmt(water_depth)} m = {_fmt(water_vol_m3)} m³.\n\n"
        f"Step 3: Convert to litres (× 1 000) [1 mark]:\n"
        f"Capacity = {_fmt(water_vol_m3)} × 1 000 = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_30",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the freeboard distance (in metres) from wall height to find water depth, then multiply by length and width.",
        tier_2=f"Water depth = {wall_height} - {freeboard_m} = {water_depth} m. Volume = {l} × {w} × {water_depth} × 1 000.",
        tier_3=f"Water capacity = {correct_ans}.",
        r=r,
    )


def generate_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Subskill 31: Volume of a closed cylindrical JoJo water tank in m³ and litres."""
    radius_m = round(r.choice([0.9, 1.0, 1.1, 1.25]), 2)
    height_m = round(r.choice([2.0, 2.2, 2.5, 2.8]), 2)
    pi_val = 3.142

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} installs a vertical cylindrical JoJo rainwater harvesting tank on a concrete plinth.\n"
        f"The tank has an internal radius of **{_fmt(radius_m)} m** and an internal height of **{_fmt(height_m)} m**.\n\n"
        f"Calculate the **storage capacity** of the JoJo tank in **litres**.\n"
        f"*(Use $\\pi = 3,142$ and $\\text{{Volume}} = \\pi r^2 h$. Recall: $1\\text{{ m}}^3 = 1\\ 000\\text{{ litres}}$. Round to the nearest whole litre)*"
    )

    vol_m3 = pi_val * (radius_m ** 2) * height_m
    litres = int(round(vol_m3 * 1000))

    correct_ans = f"{_fmt(litres)} ℓ"

    # Distractor forgot square on radius: pi * r * h * 1000
    dist_no_sq = int(round(pi_val * radius_m * height_m * 1000))
    # Distractor 2*pi*r*h (curved surface area)
    dist_curved = int(round(2 * pi_val * radius_m * height_m * 1000))

    custom_opts = [
        correct_ans,
        f"{_fmt(dist_no_sq)} ℓ",
        f"{_fmt(dist_curved)} ℓ",
        f"{_fmt(litres + 500)} ℓ",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: State the formula for the volume of a cylinder [1 mark]:\n"
        f"Volume = $\\pi \\times r^2 \\times h$.\n\n"
        f"Step 2: Substitute radius and height to find volume in m³ [1 mark]:\n"
        f"Volume = 3,142 × ({_fmt(radius_m)})² × {_fmt(height_m)} = 3,142 × {_fmt(round(radius_m**2, 4))} × {_fmt(height_m)} = {_fmt(vol_m3, 3)} m³.\n\n"
        f"Step 3: Convert to litres by multiplying by 1 000 [1 mark]:\n"
        f"Capacity = {_fmt(vol_m3, 3)} × 1 000 = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_31",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Volume of a cylinder = π × r² × h. Multiply by 1 000 to get litres.",
        tier_2=f"Volume = 3,142 × ({radius_m})² × {height_m} m³. Multiply by 1 000.",
        tier_3=f"Capacity = {correct_ans}.",
        r=r,
    )


def generate_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Subskill 32: Volume of a cylindrical beverage can in millilitres (1 cm³ = 1 mL)."""
    radius_cm = round(r.choice([3.0, 3.2, 3.3]), 1)
    height_cm = round(r.choice([11.0, 11.5, 12.0]), 1)
    pi_val = 3.142

    prompt = (
        f"A soft drink manufacturer packages carbonated juice in cylindrical aluminium cans.\n"
        f"Each can has an internal radius of **{_fmt(radius_cm)} cm** and an internal height of **{_fmt(height_cm)} cm**.\n\n"
        f"Calculate the **liquid volume** of the beverage can in **millilitres (mℓ)**.\n"
        f"*(Use $\\pi = 3,142$, $\\text{{Volume}} = \\pi r^2 h$, and note that $1\\text{{ cm}}^3 = 1\\text{{ m\\ell}}$. Round to the nearest whole mℓ)*"
    )

    vol_cm3 = pi_val * (radius_cm ** 2) * height_cm
    ml_val = int(round(vol_cm3))

    correct_ans = f"{_fmt(ml_val)} mℓ"

    custom_opts = [
        correct_ans,
        f"{_fmt(int(round(vol_cm3 / 10.0)))} mℓ",
        f"{_fmt(int(round(2 * pi_val * radius_cm * height_cm)))} mℓ",
        f"{_fmt(ml_val + 35)} mℓ",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the volume of the cylinder in cm³ [1 mark]:\n"
        f"Volume = $\\pi \\times r^2 \\times h$ = 3,142 × ({_fmt(radius_cm)})² × {_fmt(height_cm)} = {_fmt(vol_cm3, 2)} cm³.\n\n"
        f"Step 2: Apply the liquid conversion ratio ($1\\text{{ cm}}^3 = 1\\text{{ m\\ell}}$) [1 mark]:\n"
        f"{_fmt(vol_cm3, 2)} cm³ = {_fmt(vol_cm3, 2)} mℓ.\n\n"
        f"Step 3: Stated answer rounded to the nearest integer [1 mark]:\n"
        f"Liquid Volume = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_32",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Volume = π × r² × h in cm³. Since 1 cm³ = 1 mℓ, the numerical answer is identical.",
        tier_2=f"Volume = 3,142 × ({radius_cm})² × {height_cm}.",
        tier_3=f"Liquid Volume = {correct_ans}.",
        r=r,
    )


def generate_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Subskill 33: Volume of a triangular prism water trough in litres."""
    tri_base_m = round(r.choice([0.6, 0.8, 1.0]), 1)
    tri_depth_m = round(r.choice([0.4, 0.5, 0.6]), 1)
    trough_length_m = round(r.choice([2.5, 3.0, 4.0]), 1)

    prompt = (
        f"A dairy farmer constructs a V-shaped livestock drinking trough shaped as a triangular prism.\n"
        f"The triangular cross-section has a top base width of **{_fmt(tri_base_m)} m** and a vertical depth of **{_fmt(tri_depth_m)} m**.\n"
        f"The total length of the trough is **{_fmt(trough_length_m)} m**.\n\n"
        f"Calculate the **maximum water capacity** of the trough in **litres**.\n"
        f"*(Formula: $\\text{{Volume}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} \\times \\text{{length}}$. Note: $1\\text{{ m}}^3 = 1\\ 000\\text{{ litres}}$)*"
    )

    vol_m3 = round(0.5 * tri_base_m * tri_depth_m * trough_length_m, 3)
    litres = int(round(vol_m3 * 1000))

    correct_ans = f"{_fmt(litres)} ℓ"

    # Distractor forgot 1/2
    dist_no_half = int(round(tri_base_m * tri_depth_m * trough_length_m * 1000))

    custom_opts = [
        correct_ans,
        f"{_fmt(dist_no_half)} ℓ",
        f"{_fmt(int(litres / 2))} ℓ",
        f"{_fmt(litres + 150)} ℓ",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the area of the triangular cross-section [1 mark]:\n"
        f"Triangular Area = 1/2 × base × depth = 0,5 × {_fmt(tri_base_m)} m × {_fmt(tri_depth_m)} m = {_fmt(0.5 * tri_base_m * tri_depth_m)} m².\n\n"
        f"Step 2: Multiply by the length of the trough [1 mark]:\n"
        f"Volume = {_fmt(0.5 * tri_base_m * tri_depth_m)} m² × {_fmt(trough_length_m)} m = {_fmt(vol_m3)} m³.\n\n"
        f"Step 3: Convert cubic metres to litres (× 1 000) [1 mark]:\n"
        f"Capacity = {_fmt(vol_m3)} × 1 000 = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_33",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Volume of triangular prism = 0,5 × base × height × length. Multiply by 1 000 for litres.",
        tier_2=f"Volume = 0,5 × {tri_base_m} × {tri_depth_m} × {trough_length_m} = {vol_m3} m³.",
        tier_3=f"Capacity = {correct_ans}.",
        r=r,
    )


def generate_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Subskill 34: Time required to fill a swimming pool at a constant flow rate."""
    pool_litres = r.choice([36000, 45000, 54000, 60000])
    flow_rate_l_min = r.choice([25, 30, 40])  # litres per minute

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is filling an empty newly-marbelited swimming pool holding **{_fmt(pool_litres)} litres** of water.\n"
        f"Water flows from a garden borehole hose at a constant rate of **{flow_rate_l_min} litres per minute**.\n\n"
        f"Calculate the **total time in hours** required to completely fill the swimming pool.\n"
        f"*(Formula: $\\text{{Time in hours}} = \\frac{{\\text{{Total Volume in Litres}}}}{{\\text{{Flow Rate (litres/min)}} \\times 60}}$)*"
    )

    total_mins = pool_litres / flow_rate_l_min
    total_hours = round(total_mins / 60.0, 1)

    correct_ans = f"{_fmt(total_hours)} hours"

    # Distractor: Forgot to divide by 60
    dist_mins = f"{_fmt(int(total_mins))} hours"

    custom_opts = [
        correct_ans,
        dist_mins,
        f"{_fmt(round(total_hours / 2, 1))} hours",
        f"{_fmt(round(total_hours + 5.0, 1))} hours",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate the flow rate in litres per hour [1 mark]:\n"
        f"Hourly Flow Rate = {flow_rate_l_min} ℓ/min × 60 min/h = {_fmt(flow_rate_l_min * 60)} ℓ/h.\n\n"
        f"Step 2: Divide total pool volume by hourly flow rate [1 mark]:\n"
        f"Time = {_fmt(pool_litres)} ℓ ÷ {_fmt(flow_rate_l_min * 60)} ℓ/h.\n\n"
        f"Step 3: Stated answer in hours [1 mark]:\n"
        f"Time Required = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_34",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="First convert flow rate from L/min to L/hour by multiplying by 60, then divide total volume by hourly rate.",
        tier_2=f"Hourly rate = {flow_rate_l_min} × 60 = {flow_rate_l_min * 60} ℓ/h. Time = {pool_litres} ÷ {flow_rate_l_min * 60}.",
        tier_3=f"Time = {correct_ans}.",
        r=r,
    )


def generate_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Subskill 35: Rainwater harvesting collection potential from roof catchment area."""
    # Catchment Volume = Roof Area (m2) * Rainfall (mm) * runoff coefficient (e.g. 0.85)
    # 1 mm of rain on 1 m2 = 1 litre of water!
    roof_length = r.randint(12, 18)
    roof_width = r.randint(8, 12)
    roof_area = roof_length * roof_width
    rainfall_mm = r.choice([35, 50, 65, 80])  # mm in a summer month
    runoff_efficiency = 0.85  # 85% collection after gutter splashing and evaporation

    name = r.choice(SA_NAMES)

    prompt = (
        f"During a summer storm in Gauteng, a residential home with a pitched corrugated roof collects rainwater.\n"
        f"The roof has an effective horizontal catchment area of **{roof_area} m²** ({roof_length} m × {roof_width} m).\n"
        f"The weather service records **{rainfall_mm} mm** of rainfall.\n"
        f"Due to roof absorption and gutter overflow, the system has a collection efficiency of **85%** (runoff coefficient = 0,85).\n\n"
        f"Calculate the **volume of water in litres** harvested into the storage tanks.\n"
        f"*(Note: $1\\text{{ mm}}$ of rain falling on $1\\text{{ m}}^2$ yields exactly $1\\text{{ litre}}$ of water. Formula: $\\text{{Harvested Litres}} = \\text{{Area (m}}^2\\text{{)}} \\times \\text{{Rainfall (mm)}} \\times 0,85$)*"
    )

    gross_litres = roof_area * rainfall_mm
    net_litres = int(round(gross_litres * runoff_efficiency))

    correct_ans = f"{_fmt(net_litres)} ℓ"

    custom_opts = [
        correct_ans,
        f"{_fmt(gross_litres)} ℓ",  # 100% efficiency
        f"{_fmt(int(net_litres / 2))} ℓ",
        f"{_fmt(net_litres + 1200)} ℓ",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate gross potential rainwater volume [1 mark]:\n"
        f"Gross Volume = {roof_area} m² × {rainfall_mm} mm × 1 ℓ/(m²·mm) = {_fmt(gross_litres)} ℓ.\n\n"
        f"Step 2: Multiply by collection efficiency factor (85% = 0,85) [1 mark]:\n"
        f"Harvested Litres = {_fmt(gross_litres)} ℓ × 0,85.\n\n"
        f"Step 3: Stated answer [1 mark]:\n"
        f"Harvested Litres = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_35",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="1 mm on 1 m² = 1 litre. Multiply roof area by rainfall in mm, then multiply by 0,85.",
        tier_2=f"Gross = {roof_area} × {rainfall_mm} = {gross_litres} ℓ. Multiply by 0,85.",
        tier_3=f"Harvested Volume = {correct_ans}.",
        r=r,
    )


def generate_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Subskill 36: Municipal water step tariff bill calculation for a residential pool fill."""
    fill_volume_kl = r.choice([40, 50, 60])  # kilolitres (kL = m3)
    
    # Standard 3-block municipal tariff:
    # 0 - 6 kL: Free / R0.00
    # 7 - 25 kL (19 kL): R 18.50 per kL
    # > 25 kL: R 34.00 per kL

    prompt = (
        f"A homeowner fills their swimming pool with **{fill_volume_kl} kℓ** (40 000 – 60 000 litres) of municipal tap water.\n"
        f"The local municipality charges stepped water consumption tariffs (excluding VAT) as follows:\n\n"
        f"| Step Block | Consumption Range | Tariff per kℓ |\n"
        f"| :--- | :--- | :--- |\n"
        f"| Block 1 | 0 to 6 kℓ | Free (R 0,00) |\n"
        f"| Block 2 | 7 to 25 kℓ (next 19 kℓ) | R 18,50 |\n"
        f"| Block 3 | Above 25 kℓ | R 34,00 |\n\n"
        f"Assuming the household had zero prior water consumption in this billing cycle, calculate the **total water bill** for the {fill_volume_kl} kℓ pool fill."
    )

    cost_block1 = 0.0
    cost_block2 = 19 * 18.50  # R 351.50
    excess_kl = fill_volume_kl - 25
    cost_block3 = excess_kl * 34.00
    total_bill = cost_block1 + cost_block2 + cost_block3

    correct_ans = _fmt_curr(total_bill)

    # Distractor 1: Flat rate at highest block
    dist_flat = fill_volume_kl * 34.00
    # Distractor 2: Flat rate at Block 2
    dist_flat2 = fill_volume_kl * 18.50

    custom_opts = [
        correct_ans,
        _fmt_curr(dist_flat),
        _fmt_curr(dist_flat2),
        _fmt_curr(total_bill + 150.0),
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate Block 1 and Block 2 charges [1 mark]:\n"
        f"- Block 1 (0 to 6 kℓ): 6 kℓ × R 0,00 = R 0,00.\n"
        f"- Block 2 (7 to 25 kℓ = 19 kℓ): 19 kℓ × R 18,50 = {_fmt_curr(cost_block2)}.\n\n"
        f"Step 2: Calculate Block 3 charges for the excess consumption [1 mark]:\n"
        f"Excess in Block 3 = {fill_volume_kl} kℓ - 25 kℓ = {excess_kl} kℓ.\n"
        f"Block 3 cost = {excess_kl} kℓ × R 34,00 = {_fmt_curr(cost_block3)}.\n\n"
        f"Step 3: Sum the step charges [1 mark]:\n"
        f"Total Bill = {_fmt_curr(cost_block2)} + {_fmt_curr(cost_block3)} = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_36",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Break the volume across the 3 step tiers: 6 kL free, next 19 kL at R 18,50, remaining at R 34,00.",
        tier_2=f"Block 2 = 19 × R 18,50 = R {cost_block2:.2f}. Block 3 = ({fill_volume_kl} - 25) × R 34,00 = {excess_kl} × R 34,00 = R {cost_block3:.2f}.",
        tier_3=f"Total Water Bill = {correct_ans}.",
        r=r,
    )
