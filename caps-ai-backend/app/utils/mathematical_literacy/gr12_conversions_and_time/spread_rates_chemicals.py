"""Subskills 09 to 16: Area spread rates, paint volume packaging, agricultural chemicals, and dosing."""
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
    _fmt_frac,
    _fmt_pct,
)


def generate_09_paint_spread_rate_single_coat(r: random.Random) -> Dict[str, Any]:
    """Calculate the liquid volume of paint required for a single coat given surface area and spread rate."""
    area_m2 = r.choice([44, 55, 66, 77, 88, 110])
    spread_rate = 11.0  # 11 m2 per litre
    litres_needed = round(area_m2 / spread_rate, 2)

    correct_ans = f"Volume = {area_m2} m² ÷ 11 m²/ℓ = {_fmt(litres_needed, 1)} ℓ"

    custom_options = [
        correct_ans,
        f"Volume = {area_m2} m² × 11 = {_fmt(area_m2 * 11, 0)} ℓ",
        f"Volume = {area_m2} m² ÷ 5 = {_fmt(area_m2 / 5, 1)} ℓ",
        f"Volume = {_fmt(litres_needed * 2, 1)} ℓ",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A homeowner is painting the interior walls of a lounge with a total surface area of {area_m2} m².\n"
        f"The paint manufacturer specifies a spread rate of 11 m² per litre (1 ℓ covers 11 m²).\n\n"
        f"Calculate the volume of paint in litres (ℓ) required to apply a single coat of paint."
    )
    explanation = (
        f"Step 1: Identify formula: Volume (ℓ) = Total Area (m²) ÷ Spread Rate (m²/ℓ) [M].\n"
        f"Step 2: Substitute values: {area_m2} ÷ 11 [M].\n"
        f"Step 3: Volume = {_fmt(litres_needed, 1)} ℓ [A]."
    )
    return _build_question_payload(
        subskill_id="09_paint_spread_rate_single_coat",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the total area to be painted by the spread rate per litre.",
        tier_2=f"Volume = {area_m2} ÷ 11.",
        tier_3=f"Volume = {_fmt(litres_needed, 1)} ℓ.",
        r=r,
    )


def generate_10_multi_coat_paint_tin_packaging(r: random.Random) -> Dict[str, Any]:
    """Calculate total litres for two coats of paint and determine the number of 5-litre tins to buy."""
    floor_area = r.choice([28, 30, 32, 35, 40])
    spread_rate = 11.0  # 1 litre covers 11 m2
    coats = 2
    total_area_to_cover = floor_area * coats  # e.g. 30 * 2 = 60 m2
    litres_exact = total_area_to_cover / spread_rate  # e.g. 60 / 11 = 5.45 litres

    # In commercial retail, tins come in 5 litres
    tins_5l = math.ceil(litres_exact / 5.0)

    d_spec_10 = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "shape": "garage_floor",
        "title": f"Concrete Garage Floor ({floor_area} m²)",
        "area_m2": floor_area,
    }

    correct_ans = f"Total Area = {total_area_to_cover} m²; Litres = {_fmt(litres_exact, 2)} ℓ; Purchase {tins_5l} × 5 ℓ tins"

    custom_options = [
        correct_ans,
        f"Total Area = {floor_area} m²; Litres = {_fmt(floor_area / spread_rate, 2)} ℓ; Purchase 1 × 5 ℓ tin",
        f"Total Area = {total_area_to_cover} m²; Litres = {_fmt(total_area_to_cover, 0)} ℓ; Purchase {math.ceil(total_area_to_cover / 5)} × 5 ℓ tins",
        f"Total Area = {total_area_to_cover} m²; Litres = {_fmt(litres_exact, 2)} ℓ; Purchase {tins_5l + 1} × 5 ℓ tins",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A concrete garage floor with an area of {floor_area} m² is to be painted with 2 coats of heavy-duty epoxy floor paint.\n"
        f"• Spread rate of floor paint: 1 ℓ covers 11 m²\n"
        f"• Floor paint is sold only in 5-litre tins\n\n"
        f"1. Calculate the total area to be covered for {coats} coats.\n"
        f"2. Calculate the exact volume of paint required in litres (ℓ).\n"
        f"3. State how many whole 5-litre tins must be purchased."
    )
    explanation = (
        f"Step 1: Total area to paint = {floor_area} m² × {coats} coats = {total_area_to_cover} m² [M].\n"
        f"Step 2: Exact volume = {total_area_to_cover} m² ÷ 11 m²/ℓ = {_fmt(litres_exact, 2)} ℓ [M].\n"
        f"Step 3: Since paint is sold in 5 ℓ tins, divide {_fmt(litres_exact, 2)} by 5 and round UP to ensure full coverage: {tins_5l} tins [A]."
    )
    return _build_question_payload(
        subskill_id="10_multi_coat_paint_tin_packaging",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the floor area by 2 for two coats. Divide by 11 to get litres, then round up to whole 5-litre tins.",
        tier_2=f"Total area = {floor_area} × 2 = {total_area_to_cover} m². Litres = {total_area_to_cover} ÷ 11 = {_fmt(litres_exact, 2)} ℓ.",
        tier_3=f"Purchase {tins_5l} × 5 ℓ tins.",
        r=r,
        diagram_spec=d_spec_10,
    )


def generate_11_costing_paint_tins_total(r: random.Random) -> Dict[str, Any]:
    """Calculate the total cost of purchasing required paint tins."""
    tin_price = r.choice([429.0, 449.0, 489.0, 529.0])
    num_tins = r.choice([2, 3, 4, 5])
    total_cost = tin_price * num_tins

    correct_ans = f"Total Cost = {num_tins} tins × {_fmt_curr(tin_price)} = {_fmt_curr(total_cost)}"

    custom_options = [
        correct_ans,
        f"Total Cost = {_fmt_curr(tin_price)} (single tin)",
        f"Total Cost = {_fmt_curr(total_cost * 1.15)} (incl VAT twice)",
        f"Total Cost = {_fmt_curr(total_cost - tin_price)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A painting contractor determines that {num_tins} tins (5 litres each) of specialized exterior wall paint "
        f"are required to complete a commercial building facade.\n"
        f"The hardware store sells each 5-litre tin for {_fmt_curr(tin_price)} (VAT inclusive).\n\n"
        f"Calculate the total cost to purchase the required paint."
    )
    explanation = (
        f"Step 1: Identify unit price and quantity: {num_tins} tins at {_fmt_curr(tin_price)} per tin [M].\n"
        f"Step 2: Multiply: {num_tins} × {_fmt_curr(tin_price)} [M].\n"
        f"Step 3: Total Cost = {_fmt_curr(total_cost)} [A]."
    )
    return _build_question_payload(
        subskill_id="11_costing_paint_tins_total",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the number of tins required by the price per tin.",
        tier_2=f"{num_tins} × {_fmt_curr(tin_price)}.",
        tier_3=f"Total Cost = {_fmt_curr(total_cost)}.",
        r=r,
    )


def generate_12_agricultural_pesticide_ratio_coverage(r: random.Random) -> Dict[str, Any]:
    """Calculate the volume of agricultural pesticide concentrate required using rates and proportion."""
    plot_l = r.choice([20, 25, 30])
    plot_w = r.choice([12, 15, 20])
    plot_area = plot_l * plot_w  # e.g. 20 * 12 = 240 m2

    rate_ml = 60.0  # 60 ml per 100 m2
    total_ml = (plot_area / 100.0) * rate_ml  # e.g. 2.4 * 60 = 144 ml

    correct_ans = f"Plot Area = {plot_area} m²; Pesticide Required = {_fmt(total_ml, 1)} ml"

    custom_options = [
        correct_ans,
        f"Plot Area = {plot_area} m²; Pesticide Required = {_fmt(rate_ml, 1)} ml",
        f"Plot Area = {plot_area} m²; Pesticide Required = {_fmt(total_ml / 10, 2)} ml",
        f"Plot Area = {plot_area} m²; Pesticide Required = {_fmt(total_ml * 10, 0)} ml",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A commercial citrus farmer needs to apply a weed pesticide across an orchard plot measuring {plot_l} m by {plot_w} m.\n"
        f"The manufacturer's label states:\n"
        f"• Mix 60 ml of pesticide concentrate for every 100 m² of land area\n\n"
        f"1. Calculate the surface area of the plot in square metres (m²).\n"
        f"2. Calculate the exact volume of pesticide concentrate in millilitres (ml) required to treat the plot."
    )
    explanation = (
        f"Step 1: Calculate plot area: A = {plot_l} m × {plot_w} m = {plot_area} m² [M].\n"
        f"Step 2: Set up proportion: 60 ml : 100 m² = x ml : {plot_area} m² [M].\n"
        f"Step 3: x = (60 ÷ 100) × {plot_area} = {_fmt(total_ml, 1)} ml [A]."
    )
    return _build_question_payload(
        subskill_id="12_agricultural_pesticide_ratio_coverage",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="First find the area (length × width). Then divide by 100 and multiply by 60 ml.",
        tier_2=f"Area = {plot_l} × {plot_w} = {plot_area} m². Pesticide = ({plot_area} ÷ 100) × 60.",
        tier_3=f"Pesticide Required = {_fmt(total_ml, 1)} ml.",
        r=r,
    )


def generate_13_lawn_fertilizer_application_rate(r: random.Random) -> Dict[str, Any]:
    """Calculate granular lawn fertilizer requirement in kg and bags given application rate."""
    lawn_area = r.choice([350, 400, 500, 600])
    rate_g_per_m2 = 35.0  # 35 grams per m2
    total_grams = lawn_area * rate_g_per_m2
    total_kg = total_grams / 1000.0  # e.g. 500 * 35 = 17 500 g = 17.5 kg
    bag_size_kg = 5.0
    bags_needed = math.ceil(total_kg / bag_size_kg)

    correct_ans = f"Mass = {_fmt(total_kg, 1)} kg; Purchase {bags_needed} × 5 kg bags of fertilizer"

    custom_options = [
        correct_ans,
        f"Mass = {_fmt(total_grams, 0)} kg; Purchase {math.ceil(total_grams / 5)} bags",
        f"Mass = {_fmt(total_kg, 1)} kg; Purchase {math.floor(total_kg / bag_size_kg)} × 5 kg bags",
        f"Mass = {_fmt(total_kg / 10, 2)} kg; Purchase 1 × 5 kg bag",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} is treating a school sports lawn with an area of {lawn_area} m² using 4:1:1 granular lawn fertilizer.\n"
        f"• The recommended application rate is 35 g per m²\n"
        f"• Fertilizer is sold in 5 kg bags at the garden depot\n\n"
        f"1. Calculate the total mass of fertilizer required in grams (g) and kilograms (kg).\n"
        f"2. How many whole 5 kg bags must {name} purchase?"
    )
    explanation = (
        f"Step 1: Total grams = {lawn_area} m² × 35 g/m² = {_fmt(total_grams, 0)} g [M].\n"
        f"Step 2: Convert to kg: {_fmt(total_grams, 0)} ÷ 1 000 = {_fmt(total_kg, 1)} kg [M].\n"
        f"Step 3: Bags needed = {_fmt(total_kg, 1)} ÷ 5 kg = {total_kg / 5:.1f} → Round UP to {bags_needed} bags [A]."
    )
    return _build_question_payload(
        subskill_id="13_lawn_fertilizer_application_rate",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply area by 35 g to get total grams, divide by 1 000 for kg, then round up for 5 kg bags.",
        tier_2=f"{lawn_area} × 35 = {total_grams} g = {total_kg} kg. {total_kg} ÷ 5 = {total_kg / 5}.",
        tier_3=f"Purchase {bags_needed} × 5 kg bags.",
        r=r,
    )


def generate_14_tile_adhesive_spread_rate(r: random.Random) -> Dict[str, Any]:
    """Calculate the number of tile adhesive bags required based on floor area and coverage rate."""
    room_l = r.choice([5.0, 6.0, 7.0])
    room_w = r.choice([4.0, 4.5, 5.0])
    room_area = room_l * room_w  # e.g. 6.0 * 4.5 = 27 m2
    coverage_per_bag = 3.5  # 1 bag (20 kg) covers 3.5 m2
    bags_exact = room_area / coverage_per_bag
    bags_to_buy = math.ceil(bags_exact)

    correct_ans = f"Area = {_fmt(room_area, 1)} m²; Exact = {_fmt(bags_exact, 2)} bags; Purchase {bags_to_buy} bags (20 kg each)"

    custom_options = [
        correct_ans,
        f"Area = {_fmt(room_area, 1)} m²; Exact = {_fmt(bags_exact, 2)} bags; Purchase {math.floor(bags_exact)} bags",
        f"Area = {_fmt(room_area * 10, 0)} m²; Purchase {bags_to_buy * 2} bags",
        f"Area = {_fmt(room_area, 1)} m²; Purchase {bags_to_buy + 3} bags",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A tiler is laying porcelain tiles in an office reception measuring {_fmt(room_l, 1)} m by {_fmt(room_w, 1)} m.\n"
        f"• One 20 kg bag of tile adhesive covers an average of 3,5 m² of floor\n\n"
        f"1. Calculate the total floor area of the reception.\n"
        f"2. How many whole 20 kg bags of adhesive must the contractor buy to complete the job?"
    )
    explanation = (
        f"Step 1: Floor area = {_fmt(room_l, 1)} m × {_fmt(room_w, 1)} m = {_fmt(room_area, 1)} m² [M].\n"
        f"Step 2: Number of bags = {_fmt(room_area, 1)} ÷ 3,5 = {_fmt(bags_exact, 2)} bags [M].\n"
        f"Step 3: Round UP to ensure enough adhesive: {bags_to_buy} bags [A]."
    )
    return _build_question_payload(
        subskill_id="14_tile_adhesive_spread_rate",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply length by width to get floor area, then divide by 3,5 m² per bag and round UP.",
        tier_2=f"Area = {room_area} m². Bags = {room_area} ÷ 3,5 = {_fmt(bags_exact, 2)}.",
        tier_3=f"Purchase {bags_to_buy} bags.",
        r=r,
    )


def generate_15_roof_sealant_waterproofing_volume(r: random.Random) -> Dict[str, Any]:
    """Calculate the liquid volume and number of 20-litre drums of roof waterproofing membrane needed."""
    roof_area = r.choice([80, 100, 120, 150])
    spread_rate = 1.5  # 1.5 litres per m2 (for 2 coats)
    total_litres = roof_area * spread_rate  # e.g. 100 * 1.5 = 150 litres
    drum_size = 20.0  # 20 litre drum
    drums_to_buy = math.ceil(total_litres / drum_size)

    correct_ans = f"Volume = {_fmt(total_litres, 0)} ℓ; Purchase {drums_to_buy} × 20 ℓ drums"

    custom_options = [
        correct_ans,
        f"Volume = {_fmt(roof_area / spread_rate, 1)} ℓ; Purchase {math.ceil((roof_area / spread_rate) / 20)} drums",
        f"Volume = {_fmt(total_litres, 0)} ℓ; Purchase {math.floor(total_litres / drum_size)} drums",
        f"Volume = {_fmt(total_litres * 2, 0)} ℓ; Purchase {drums_to_buy * 2} drums",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A building maintenance team is applying liquid rubber waterproofing to a flat concrete roof section of {roof_area} m².\n"
        f"• The technical datasheet specifies a total spread rate of 1,5 litres per m² (for 2 coats)\n"
        f"• The liquid membrane is packaged in 20-litre drums\n\n"
        f"Calculate the total volume of waterproofing liquid required in litres (ℓ) and state the number of 20 ℓ drums to purchase."
    )
    explanation = (
        f"Step 1: Total volume = {roof_area} m² × 1,5 ℓ/m² = {_fmt(total_litres, 0)} ℓ [M].\n"
        f"Step 2: Number of drums = {_fmt(total_litres, 0)} ÷ 20 = {total_litres / drum_size:.2f} drums [M].\n"
        f"Step 3: Round UP to the next whole container: {drums_to_buy} drums [A]."
    )
    return _build_question_payload(
        subskill_id="15_roof_sealant_waterproofing_volume",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the roof area by the spread rate (1,5 ℓ/m²), then divide by 20 litres per drum.",
        tier_2=f"{roof_area} × 1,5 = {total_litres} ℓ. {total_litres} ÷ 20 = {total_litres / drum_size}.",
        tier_3=f"Volume = {_fmt(total_litres, 0)} ℓ; Purchase {drums_to_buy} × 20 ℓ drums.",
        r=r,
    )


def generate_16_pool_chlorination_chemical_dosing(r: random.Random) -> Dict[str, Any]:
    """Calculate the chemical mass required for swimming pool shock treatment based on pool capacity."""
    pool_litres = r.choice([30000, 40000, 50000, 60000])
    rate_g_per_10kl = 150.0  # 150 g per 10 000 litres
    dose_g = (pool_litres / 10000.0) * rate_g_per_10kl
    dose_kg = dose_g / 1000.0

    correct_ans = f"Dose = {_fmt(dose_g, 0)} g = {_fmt(dose_kg, 2)} kg"

    custom_options = [
        correct_ans,
        f"Dose = {_fmt(dose_g * 10, 0)} g = {_fmt(dose_kg * 10, 1)} kg",
        f"Dose = {_fmt(dose_g / 10, 1)} g = {_fmt(dose_kg / 10, 3)} kg",
        f"Dose = {_fmt(rate_g_per_10kl, 0)} g = 0,15 kg",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A municipal swimming pool contains {_fmt(pool_litres, 0)} litres of water.\n"
        f"To treat an algae outbreak, the pool manager applies granular shock chlorine.\n"
        f"• Recommended dosage: 150 g of granular chlorine for every 10 000 litres of pool water\n\n"
        f"Calculate the total mass of granular chlorine required in grams (g) and kilograms (kg)."
    )
    explanation = (
        f"Step 1: Determine the number of 10 000-litre units: {_fmt(pool_litres, 0)} ÷ 10 000 = {pool_litres / 10000:.1f} units [M].\n"
        f"Step 2: Multiply by dosage rate: {pool_litres / 10000:.1f} × 150 g = {_fmt(dose_g, 0)} g [M].\n"
        f"Step 3: Convert to kilograms: {_fmt(dose_g, 0)} ÷ 1 000 = {_fmt(dose_kg, 2)} kg [A]."
    )
    return _build_question_payload(
        subskill_id="16_pool_chlorination_chemical_dosing",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide pool litres by 10 000, multiply by 150 g, then divide by 1 000 to convert to kg.",
        tier_2=f"({pool_litres} ÷ 10 000) × 150 = {dose_g} g = {_fmt(dose_kg, 2)} kg.",
        tier_3=f"Dose = {_fmt(dose_g, 0)} g ({_fmt(dose_kg, 2)} kg).",
        r=r,
    )
