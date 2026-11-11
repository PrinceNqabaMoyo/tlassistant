"""Cluster 6: Painting, Agriculture & Commercial Area Applications (Subskills 45 to 52)."""
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
# Subskill 45: Wall Painting Gross Area Minus Openings
# --------------------------------------------------------------------------- #
def _gen_area_wall_painting_perimeter_height(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_wall_painting_perimeter_height"
    name = r.choice(SA_NAMES)
    length = r.choice([5, 6, 7])
    width = r.choice([4, 5])
    height = 2.8  # m
    wall_perim = 2 * (length + width)
    gross_area = round(wall_perim * height, 2)
    # Deductions: 1 door (1.8 m²) + 2 windows (each 1.5 m² = 3.0 m²) = 4.8 m²
    openings = 4.8
    net_area = round(gross_area - openings, 2)
    correct_ans = f"{_fmt(net_area)} m²"

    prompt = (
        f"{name} is preparing to paint the four internal walls of a rectangular lounge.\n"
        f"The room is {length} m long, {width} m wide, and the ceiling height is {_fmt(height)} m.\n"
        f"The room contains one door and two windows with a combined total area of {_fmt(openings)} m² that will not be painted.\n\n"
        f"Calculate the net wall surface area to be painted.\n\n"
        f"**Formula**: $\\text{{Gross Wall Area}} = 2(l + w) \\times h$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The gross wall area is the perimeter of the room multiplied by the ceiling height. Subtract the door and window openings.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Room Perimeter}} = 2 \\times ({length} + {width}) = {wall_perim}\\text{{ m}}$$\n"
        f"$$\\text{{Gross wall area}} = {wall_perim} \\times {_fmt(height)} = {_fmt(gross_area)}\\text{{ m}}^2$$\n"
        f"$$\\text{{Net wall area}} = {_fmt(gross_area)} - {_fmt(openings)}$$ ✓ [1 Mark: Method – finding wall area from perimeter × height and deducting openings]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Net wall area}} = {_fmt(net_area)}\\text{{ m}}^2$$ ✓ [1 Mark: Accuracy – accurate net area to 2 d.p.]"
    )

    d1 = f"{_fmt(gross_area)} m²"  # forgot to deduct openings
    d2 = f"{_fmt(round(length * width * height, 2))} m²"  # volume error
    d3 = f"{_fmt(round(net_area + 3, 2))} m²"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "length": length,
        "width": width,
        "height": height,
        "shape": "room_walls",
        "title": f"Lounge Wall Dimensions ({length} m × {width} m × {_fmt(height)} m)",
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Gross wall area = 2(l + w) × h.",
        tier_2=f"Perimeter = {wall_perim} m, gross area = {_fmt(gross_area)} m². Deduct {_fmt(openings)} m².",
        tier_3=f"Net wall area = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 46: Paint Litres for Two Coats
# --------------------------------------------------------------------------- #
def _gen_area_wall_painting_two_coats_spread_rate(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_wall_painting_two_coats_spread_rate"
    name = r.choice(SA_NAMES)
    wall_area = r.choice([48, 54, 60, 72, 80, 96])  # m²
    spread_rate = r.choice([8, 10])  # m² per litre
    coats = 2
    total_coverage = wall_area * coats
    litres_needed = round(total_coverage / spread_rate, 1)
    correct_ans = f"{_fmt(litres_needed)} litres"

    prompt = (
        f"{name} needs to apply {coats} coats of paint to walls with a total surface area of {wall_area} m².\n"
        f"The paint has a manufacturer spread rate of {spread_rate} m² per litre.\n\n"
        f"Calculate the total volume of paint required in litres."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Because {coats} coats are applied, the total area to be painted is doubled ($A \\times 2$).\n"
        f"Then divide by the spread rate to determine the required litres.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total coverage for {coats} coats}} = {wall_area} \\times {coats} = {total_coverage}\\text{{ m}}^2$$\n"
        f"$$\\text{{Litres of paint}} = \\frac{{{total_coverage}}}{{{spread_rate}}}$$ ✓ [1 Mark: Method – multiplying area by coats and dividing by spread rate]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Litres of paint}} = {_fmt(litres_needed)}\\text{{ litres}}$$ ✓ [1 Mark: Accuracy – accurate quotient]"
    )

    d1 = f"{_fmt(round(wall_area / spread_rate, 1))} litres"  # only 1 coat
    d2 = f"{_fmt(round(litres_needed * 1.5, 1))} litres"
    d3 = f"{_fmt(round(litres_needed + 4, 1))} litres"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="For 2 coats, multiply the wall area by 2 first.",
        tier_2=f"Total coverage = {wall_area} × 2 = {total_coverage} m². Divide by {spread_rate} m²/L.",
        tier_3=f"Litres needed = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 47: Paint Tins Size and Cost
# --------------------------------------------------------------------------- #
def _gen_area_wall_painting_tin_size_and_cost(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_wall_painting_tin_size_and_cost"
    name = r.choice(SA_NAMES)
    litres_needed = r.choice([11.5, 13.0, 16.5, 18.0, 22.5])
    tin_size = 5  # 5-litre tins
    price_per_tin = r.choice([389.00, 429.00, 459.00, 499.00])
    tins = math.ceil(litres_needed / tin_size)
    total_cost = tins * price_per_tin
    correct_ans = _fmt_curr(total_cost)

    prompt = (
        f"{name} calculates that a house painting job requires {_fmt(litres_needed)} litres of PVA paint.\n"
        f"The hardware store sells the paint in {tin_size}-litre tins at {_fmt_curr(price_per_tin)} per tin.\n\n"
        f"Calculate the total cost to purchase the paint (rounding up to whole tins)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Hardware stores only sell whole tins. Divide the required litres by the tin size and round UP to the next integer, "
        f"then multiply by the price per tin.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Tins needed}} = \\frac{{{_fmt(litres_needed)}}}{{{tin_size}}} = {_fmt(litres_needed / tin_size, 2)} \\implies {tins}\\text{{ tins}}$$\n"
        f"$$\\text{{Total Cost}} = {tins} \\times {_fmt_curr(price_per_tin)}$$ ✓ [1 Mark: Method – rounding up to whole 5L tins and multiplying by price]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Cost}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    d1 = _fmt_curr((litres_needed / tin_size) * price_per_tin)  # fractional tin price
    d2 = _fmt_curr((tins - 1) * price_per_tin)  # rounded down
    d3 = _fmt_curr(total_cost + price_per_tin)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine the number of 5L tins needed by rounding up.",
        tier_2=f"{_fmt(litres_needed)} ÷ {tin_size} = {_fmt(litres_needed / tin_size, 2)} → {tins} tins.",
        tier_3=f"Total cost = {tins} × {_fmt_curr(price_per_tin)} = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 48: Compost Bags Application Rate
# --------------------------------------------------------------------------- #
def _gen_area_garden_compost_application_rate(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_garden_compost_application_rate"
    name = r.choice(SA_NAMES)
    bed_l = r.choice([6, 8, 10, 12])
    bed_w = r.choice([3, 4, 5])
    bed_area = bed_l * bed_w
    coverage_per_bag = 2  # 1 bag per 2 m² (authentic CAPS textbook standard)
    bags = math.ceil(bed_area / coverage_per_bag)
    correct_ans = f"{bags} bags"

    prompt = (
        f"{name} is preparing a vegetable patch measuring {bed_l} m by {bed_w} m.\n"
        f"Organic compost must be applied at a rate of 1 bag per {coverage_per_bag} m² of soil.\n\n"
        f"Calculate the number of bags of compost required to cover the vegetable patch."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate the area of the vegetable patch ($l \\times w$), then divide by the coverage rate per bag.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Patch Area}} = {bed_l} \\times {bed_w} = {bed_area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Bags of compost}} = \\frac{{{bed_area}}}{{{coverage_per_bag}}}$$ ✓ [1 Mark: Method – dividing bed area by application rate]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Bags of compost}} = {bags}\\text{{ bags}}$$ ✓ [1 Mark: Accuracy – accurate integer count]"
    )

    d1 = f"{bed_area} bags"  # 1 bag per m²
    d2 = f"{bed_area * coverage_per_bag} bags"  # multiplied instead of dividing
    d3 = f"{bags + 4} bags"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate area of patch = length × width.",
        tier_2=f"Divide {bed_area} m² by {coverage_per_bag} m² per bag.",
        tier_3=f"Bags needed = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 49: Seedling Planting Density
# --------------------------------------------------------------------------- #
def _gen_area_seedling_planting_density(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_seedling_planting_density"
    name = r.choice(SA_NAMES)
    bed_l = r.choice([5, 6, 8, 10])
    bed_w = r.choice([2, 3, 4])
    crop = r.choice(["lettuce", "cabbage", "spinach", "carrot"])
    density = r.choice([16, 20, 25])  # seedlings per m²
    bed_area = bed_l * bed_w
    seedlings = bed_area * density
    correct_ans = f"{_fmt(seedlings)} seedlings"

    prompt = (
        f"{name} is planting {crop} seedlings in a raised garden bed measuring {bed_l} m by {bed_w} m.\n"
        f"The recommended agricultural planting density for {crop} is {density} seedlings per square metre (m²).\n\n"
        f"Calculate the total number of {crop} seedlings that can be planted in the bed."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First find the surface area of the bed ($l \\times w$). Then multiply the area by the planting density per m².\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Bed Area}} = {bed_l} \\times {bed_w} = {bed_area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Total seedlings}} = {bed_area} \\times {density}$$ ✓ [1 Mark: Method – multiplying bed area by density per m²]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total seedlings}} = {_fmt(seedlings)}\\text{{ seedlings}}$$ ✓ [1 Mark: Accuracy – accurate product]"
    )

    d1 = f"{_fmt(bed_area)} seedlings"
    d2 = f"{_fmt(seedlings // 2)} seedlings"
    d3 = f"{_fmt(seedlings + density * 2)} seedlings"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "length": bed_l,
        "width": bed_w,
        "shape": "garden_bed",
        "title": f"Raised Garden Bed ({bed_l} m × {bed_w} m)",
    }
    return _build_question_payload(
        diagram_spec=d_spec,
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find bed area = length × width.",
        tier_2=f"Multiply bed area ({bed_area} m²) by {density} seedlings/m².",
        tier_3=f"Total seedlings = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 50: Fertilizer Application Budget
# --------------------------------------------------------------------------- #
def _gen_area_fertilizer_application_budget(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_fertilizer_application_budget"
    name = r.choice(SA_NAMES)
    field_l = r.choice([20, 25, 30, 40])
    field_w = r.choice([15, 20, 25])
    field_area = field_l * field_w
    rate_g = 50  # 50 grams per m²
    total_kg = (field_area * rate_g) / 1000.0  # convert grams to kg
    price_per_kg = 24.50
    total_cost = total_kg * price_per_kg
    correct_ans = _fmt_curr(total_cost)

    prompt = (
        f"{name} is fertilizing a rectangular crop field measuring {field_l} m by {field_w} m.\n"
        f"  • Fertilizer application rate: {rate_g} g per square metre\n"
        f"  • Fertilizer cost: {_fmt_curr(price_per_kg)} per kg\n\n"
        f"Calculate the total cost of fertilizer required for this field. (Recall: 1 kg = 1 000 g)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First calculate field area ($l \\times w$). Find total grams by multiplying area by {rate_g} g/m², "
        f"then convert grams to kilograms by dividing by 1 000. Finally multiply by the price per kg.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Field Area}} = {field_l} \\times {field_w} = {field_area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Total mass in kg}} = \\frac{{{field_area} \\times {rate_g}}}{{1\\ 000}} = \\frac{{{field_area * rate_g}}}{{1\\ 000}} = {_fmt(total_kg)}\\text{{ kg}}$$\n"
        f"$$\\text{{Total Cost}} = {_fmt(total_kg)} \\times {_fmt_curr(price_per_kg)}$$ ✓ [1 Mark: Method – calculating area, converting g to kg, and multiplying by unit price]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Total Cost}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    d1 = _fmt_curr(total_cost * 10)  # forgot to divide by 1000 (divided by 100)
    d2 = _fmt_curr(field_area * price_per_kg)
    d3 = _fmt_curr(total_cost * 0.8)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Field area = l × w. Multiply by 50 g/m² and divide by 1 000 to get kg.",
        tier_2=f"Area = {field_area} m² → {_fmt(total_kg)} kg. Multiply by {_fmt_curr(price_per_kg)}/kg.",
        tier_3=f"Total cost = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 51: Commercial Property Rental
# --------------------------------------------------------------------------- #
def _gen_area_commercial_property_rental(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_commercial_property_rental"
    name = r.choice(SA_NAMES)
    shop_l = r.choice([12, 14, 15, 18, 20])
    shop_w = r.choice([8, 10, 12])
    area = shop_l * shop_w
    rate_per_m2 = r.choice([125.00, 140.00, 165.00, 185.00, 210.00])
    monthly_rent = area * rate_per_m2
    correct_ans = _fmt_curr(monthly_rent)

    prompt = (
        f"{name} is leasing retail shop space in a shopping mall measuring {shop_l} m by {shop_w} m.\n"
        f"The commercial landlord charges a basic monthly rental of {_fmt_curr(rate_per_m2)} per square metre (m²).\n\n"
        f"Calculate the total basic monthly rental for this shop space."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Commercial property rental is based on the floor area multiplied by the tariff per m²: $\\text{{Rent}} = \\text{{Area}} \\times \\text{{Rate per m}}^2$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Shop Area}} = {shop_l} \\times {shop_w} = {area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Monthly Rental}} = {area} \\times {_fmt_curr(rate_per_m2)}$$ ✓ [1 Mark: Method – multiplying shop floor area by monthly rate per m²]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Monthly Rental}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate currency total]"
    )

    d1 = _fmt_curr(area * (rate_per_m2 - 20))
    d2 = _fmt_curr(monthly_rent * 1.15)  # with VAT
    d3 = _fmt_curr(monthly_rent * 0.9)
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Shop area = length × width.",
        tier_2=f"Area = {area} m². Multiply by {_fmt_curr(rate_per_m2)} per m².",
        tier_3=f"Monthly rent = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 52: Municipal Property Rates Assessment
# --------------------------------------------------------------------------- #
def _gen_area_municipal_property_rates_assessment(r: random.Random) -> Dict[str, Any]:
    sub_id = "area_municipal_property_rates_assessment"
    name = r.choice(SA_NAMES)
    prop_l = r.choice([30, 40, 50])
    prop_w = r.choice([20, 25, 30])
    area = prop_l * prop_w
    valuation_per_m2 = r.choice([800.00, 1000.00, 1200.00, 1500.00])
    total_valuation = area * valuation_per_m2
    # Municipal rates tariff: e.g. 0.0085 Rands per Rand valuation (0.85 cents in the Rand)
    rate_factor = 0.008  # 0.8%
    annual_rates = round(total_valuation * rate_factor, 2)
    monthly_rates = round(annual_rates / 12, 2)
    correct_ans = _fmt_curr(monthly_rates)

    prompt = (
        f"{name} owns a residential erf measuring {prop_l} m by {prop_w} m.\n"
        f"The municipal property valuation is {_fmt_curr(valuation_per_m2)} per m² of land area.\n"
        f"The municipality assesses property rates at an annual rate of 0,8% (factor of 0,008) of the total property valuation.\n\n"
        f"Calculate the monthly municipal property rates payable for this property."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First find the total property land area ($l \\times w$). Then determine the total valuation by multiplying area by the valuation per m².\n"
        f"Calculate annual property rates by applying 0,008, and divide by 12 months to get the monthly charge.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Property Area}} = {prop_l} \\times {prop_w} = {area}\\text{{ m}}^2$$\n"
        f"$$\\text{{Total Valuation}} = {area} \\times {_fmt_curr(valuation_per_m2)} = {_fmt_curr(total_valuation)}$$\n"
        f"$$\\text{{Annual Rates}} = {_fmt_curr(total_valuation)} \\times 0,008 = {_fmt_curr(annual_rates)}$$\n"
        f"$$\\text{{Monthly Rates}} = \\frac{{{_fmt_curr(annual_rates)}}}{{12}}$$ ✓ [1 Mark: Method – finding valuation, annual rates, and dividing by 12]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Monthly Rates}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate monthly currency value]"
    )

    d1 = _fmt_curr(annual_rates)  # forgot to divide by 12
    d2 = _fmt_curr(round(monthly_rates * 1.2, 2))
    d3 = _fmt_curr(round(monthly_rates * 0.8, 2))
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find total property valuation = area × value/m².",
        tier_2=f"Annual rates = Total valuation × 0,008. Divide by 12 for monthly rates.",
        tier_3=f"Monthly rates = {correct_ans}.",
        r=r,
    )
