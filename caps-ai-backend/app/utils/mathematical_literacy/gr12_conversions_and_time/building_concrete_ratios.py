"""Subskills 17 to 24: Building materials, concrete mixes, wheelbarrow-to-bucket conversions, and mortar takeoff."""
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


def generate_17_concrete_bags_per_cubic_metre(r: random.Random) -> Dict[str, Any]:
    """Calculate the number of 50 kg cement bags needed for a concrete floor slab given volume."""
    vol_m3 = round(r.uniform(2.5, 4.5), 1)  # e.g. 3.0 m3
    rate_bags = 7.7  # 7.7 bags per m3 for medium strength concrete
    exact_bags = vol_m3 * rate_bags
    whole_bags = math.ceil(exact_bags)

    correct_ans = f"Exact = {_fmt(exact_bags, 1)} bags; Purchase {whole_bags} whole bags of cement"

    custom_options = [
        correct_ans,
        f"Exact = {_fmt(exact_bags, 1)} bags; Purchase {math.floor(exact_bags)} whole bags of cement",
        f"Exact = {_fmt(vol_m3 * 10, 0)} bags; Purchase {int(vol_m3 * 10)} whole bags of cement",
        f"Exact = {_fmt(exact_bags / 2, 1)} bags; Purchase {math.ceil(exact_bags / 2)} whole bags of cement",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A builder is pouring a medium-strength concrete floor slab for an outside storeroom with a total volume of {_fmt(vol_m3, 1)} m³.\n"
        f"The cement manufacturer's specification states that 7,7 bags of cement are required for every 1 m³ of concrete.\n\n"
        f"1. Calculate the exact number of bags of cement required.\n"
        f"2. State how many whole 50 kg bags must be purchased from the hardware store."
    )
    explanation = (
        f"Step 1: Multiply slab volume by the cement requirement: {_fmt(vol_m3, 1)} m³ × 7,7 bags/m³ [M].\n"
        f"Step 2: Exact bags = {_fmt(exact_bags, 1)} bags [M].\n"
        f"Step 3: Round UP to the next whole bag to ensure adequate strength: {whole_bags} bags [A]."
    )
    return _build_question_payload(
        subskill_id="17_concrete_bags_per_cubic_metre",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the volume in m³ by 7,7 bags per m³. Round UP to whole bags.",
        tier_2=f"{vol_m3} × 7,7 = {_fmt(exact_bags, 1)} bags.",
        tier_3=f"Purchase {whole_bags} whole bags.",
        r=r,
    )


def generate_18_wheelbarrows_of_stone_and_sand(r: random.Random) -> Dict[str, Any]:
    """Calculate the number of wheelbarrows of crushed stone required for a wall foundation."""
    vol_m3 = round(r.uniform(2.0, 3.2), 1)  # e.g. 2.7 m3
    cement_rate = 5.8  # 5.8 bags per m3 for low strength concrete
    stone_per_bag = 1.75  # 1.75 wheelbarrows of stone per bag of cement

    total_cement_bags = vol_m3 * cement_rate  # e.g. 2.7 * 5.8 = 15.66 bags
    wheelbarrows_stone = total_cement_bags * stone_per_bag  # e.g. 15.66 * 1.75 = 27.405
    round_wheelbarrows = round(wheelbarrows_stone)

    correct_ans = f"Exact = {_fmt(wheelbarrows_stone, 3)} wheelbarrows ≈ {round_wheelbarrows} full wheelbarrows of stone"

    custom_options = [
        correct_ans,
        f"Exact = {_fmt(wheelbarrows_stone * 2, 2)} wheelbarrows ≈ {round_wheelbarrows * 2} wheelbarrows",
        f"Exact = {_fmt(total_cement_bags, 2)} wheelbarrows ≈ {round(total_cement_bags)} wheelbarrows",
        f"Exact = {_fmt(wheelbarrows_stone / 1.75, 2)} wheelbarrows ≈ {round(wheelbarrows_stone / 1.75)} wheelbarrows",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A trench foundation for a brick wall requires {_fmt(vol_m3, 1)} m³ of low-strength concrete.\n"
        f"• 5,8 bags of cement are required to make 1 m³ of this concrete mixture\n"
        f"• 1,75 wheelbarrows of crushed stone are mixed for every 1 bag of cement used\n\n"
        f"Calculate the total number of full wheelbarrows of stone required for the foundation, "
        f"rounded to the nearest full wheelbarrow."
    )
    explanation = (
        f"Step 1: Calculate total bags of cement: {_fmt(vol_m3, 1)} m³ × 5,8 bags/m³ = {_fmt(total_cement_bags, 2)} bags [M].\n"
        f"Step 2: Multiply by stone ratio: {_fmt(total_cement_bags, 2)} × 1,75 = {_fmt(wheelbarrows_stone, 3)} wheelbarrows [M].\n"
        f"Step 3: Round to the nearest whole wheelbarrow: {round_wheelbarrows} full wheelbarrows [A]."
    )
    return _build_question_payload(
        subskill_id="18_wheelbarrows_of_stone_and_sand",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="First find total cement bags (volume × 5,8), then multiply by 1,75 wheelbarrows per bag.",
        tier_2=f"Bags = {vol_m3} × 5,8 = {_fmt(total_cement_bags, 2)}. Stone = {_fmt(total_cement_bags, 2)} × 1,75 = {_fmt(wheelbarrows_stone, 3)}.",
        tier_3=f"Approximately {round_wheelbarrows} full wheelbarrows.",
        r=r,
    )


def generate_19_wheelbarrow_litres_to_cubic_metres(r: random.Random) -> Dict[str, Any]:
    """Convert stone volume from wheelbarrows to litres and cubic metres (m3)."""
    wheelbarrows = r.choice([24, 27, 30, 32, 35])
    litres_per_barrow = 65.0  # 65 litres per standard builder's wheelbarrow
    total_litres = wheelbarrows * litres_per_barrow  # e.g. 27 * 65 = 1 755 litres
    vol_kl = total_litres / 1000.0  # 1.755 kl
    vol_m3 = round(vol_kl, 1)  # 1.8 m3

    correct_ans = f"{_fmt(total_litres, 0)} ℓ = {_fmt(vol_kl, 3)} kl ≈ {_fmt(vol_m3, 1)} m³ of stone to purchase"

    custom_options = [
        correct_ans,
        f"{_fmt(total_litres, 0)} ℓ = {_fmt(vol_kl * 10, 1)} m³ of stone to purchase",
        f"{_fmt(wheelbarrows * 100, 0)} ℓ = {_fmt(wheelbarrows / 10, 1)} m³ of stone to purchase",
        f"{_fmt(total_litres, 0)} ℓ = {_fmt(vol_kl / 10, 2)} m³ of stone to purchase",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A building site requires {wheelbarrows} full wheelbarrows of crushed stone for a foundation.\n"
        f"• A standard builder's wheelbarrow has a capacity of 65 litres\n"
        f"• Conversion standards: 1 000 ℓ = 1 kl = 1 m³\n\n"
        f"1. Calculate the total volume of stone in litres (ℓ).\n"
        f"2. Convert this to cubic metres (m³) rounded to 1 decimal place to determine how much bulk stone to order."
    )
    explanation = (
        f"Step 1: Total litres = {wheelbarrows} wheelbarrows × 65 ℓ = {_fmt(total_litres, 0)} ℓ [M].\n"
        f"Step 2: Convert to kilolitres / cubic metres: {_fmt(total_litres, 0)} ÷ 1 000 = {_fmt(vol_kl, 3)} m³ [M].\n"
        f"Step 3: Round off to 1 decimal place: {_fmt(vol_m3, 1)} m³ [A]."
    )
    return _build_question_payload(
        subskill_id="19_wheelbarrow_litres_to_cubic_metres",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply wheelbarrows by 65 litres, then divide by 1 000 to convert to m³.",
        tier_2=f"{wheelbarrows} × 65 = {_fmt(total_litres, 0)} ℓ. Divide by 1 000 = {_fmt(vol_kl, 3)} m³.",
        tier_3=f"Order approximately {_fmt(vol_m3, 1)} m³.",
        r=r,
    )


def generate_20_total_cement_bags_floor_and_walls(r: random.Random) -> Dict[str, Any]:
    """Calculate combined cement bags for floor and wall foundation and round up at the end."""
    floor_vol = round(r.uniform(2.8, 3.5), 1)  # 3.0 m3
    wall_vol = round(r.uniform(2.4, 3.0), 1)   # 2.7 m3

    floor_rate = 7.7  # 7.7 bags/m3
    wall_rate = 5.8   # 5.8 bags/m3

    floor_bags = floor_vol * floor_rate  # 23.1
    wall_bags = wall_vol * wall_rate     # 15.66
    total_exact = floor_bags + wall_bags # 38.76
    total_whole = math.ceil(total_exact) # 39

    correct_ans = f"Floor = {_fmt(floor_bags, 1)} bags; Wall = {_fmt(wall_bags, 2)} bags; Total = {_fmt(total_exact, 2)} bags ≈ {total_whole} bags"

    custom_options = [
        correct_ans,
        f"Floor = {_fmt(floor_bags, 1)} bags; Wall = {_fmt(wall_bags, 2)} bags; Total = {math.floor(total_exact)} bags",
        f"Floor = {math.ceil(floor_bags)} bags; Wall = {math.ceil(wall_bags)} bags; Total = {math.ceil(floor_bags) + math.ceil(wall_bags) + 2} bags",
        f"Floor = {_fmt(floor_bags / 2, 1)} bags; Wall = {_fmt(wall_bags / 2, 2)} bags; Total = {total_whole // 2} bags",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A builder is ordering materials for an outbuilding project:\n"
        f"• Floor slab volume: {_fmt(floor_vol, 1)} m³ (requires 7,7 bags of cement per m³)\n"
        f"• Wall foundation volume: {_fmt(wall_vol, 1)} m³ (requires 5,8 bags of cement per m³)\n\n"
        f"Calculate the total number of whole 50 kg bags of cement that must be ordered to complete both the floor and wall foundations."
    )
    explanation = (
        f"Step 1: Cement for floor = {_fmt(floor_vol, 1)} × 7,7 = {_fmt(floor_bags, 1)} bags [M].\n"
        f"Step 2: Cement for walls = {_fmt(wall_vol, 1)} × 5,8 = {_fmt(wall_bags, 2)} bags [M].\n"
        f"Step 3: Total = {_fmt(floor_bags, 1)} + {_fmt(wall_bags, 2)} = {_fmt(total_exact, 2)} bags → Round UP to {total_whole} whole bags [A]."
    )
    return _build_question_payload(
        subskill_id="20_total_cement_bags_floor_and_walls",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the cement bags for each section, add them together, and round UP only at the end.",
        tier_2=f"Floor: {floor_vol} × 7,7 = {_fmt(floor_bags, 1)}. Wall: {wall_vol} × 5,8 = {_fmt(wall_bags, 2)}. Total: {_fmt(total_exact, 2)}.",
        tier_3=f"Purchase {total_whole} bags.",
        r=r,
    )


def generate_21_converting_wheelbarrows_to_bucket_ratio(r: random.Random) -> Dict[str, Any]:
    """Convert concrete wheelbarrow proportions to a simplified bucket volume ratio."""
    bag_vol_litres = 33.2
    wheelbarrow_vol_litres = 65.0
    barrows_sand = 1.75
    barrows_stone = 1.75

    sand_litres = barrows_sand * wheelbarrow_vol_litres  # 113.75 ℓ
    stone_litres = barrows_stone * wheelbarrow_vol_litres  # 113.75 ℓ

    # Ratio: 33.2 : 113.75 : 113.75
    ratio_sand = round(sand_litres / bag_vol_litres, 1)  # 3.4
    ratio_stone = round(stone_litres / bag_vol_litres, 1)  # 3.4

    correct_ans = f"1 bucket cement : {_fmt(ratio_sand, 1)} buckets sand : {_fmt(ratio_stone, 1)} buckets stone"

    custom_options = [
        correct_ans,
        f"1 bucket cement : 1,75 buckets sand : 1,75 buckets stone",
        f"1 bucket cement : 2,0 buckets sand : 3,0 buckets stone",
        f"1 bucket cement : 5,0 buckets sand : 5,0 buckets stone",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A concrete mixture recipe gives quantities using builder's wheelbarrows:\n"
        f"• 1 bag of cement = 33,2 litres\n"
        f"• 1 builder's wheelbarrow = 65 litres\n"
        f"• Concrete specification: 1 bag cement : 1,75 wheelbarrows sand : 1,75 wheelbarrows stone\n\n"
        f"For a small repair job using a standard bucket, convert this mix into a simplified bucket ratio: "
        f"**1 bucket cement : … buckets sand : … buckets stone**."
    )
    explanation = (
        f"Step 1: Calculate volume of sand and stone in litres: 1,75 × 65 ℓ = {_fmt(sand_litres, 2)} ℓ [M].\n"
        f"Step 2: Express ratio in litres: {_fmt(bag_vol_litres, 1)} ℓ cement : {_fmt(sand_litres, 2)} ℓ sand : {_fmt(stone_litres, 2)} ℓ stone [M].\n"
        f"Step 3: Divide all terms by {_fmt(bag_vol_litres, 1)}: 1 : {_fmt(ratio_sand, 1)} : {_fmt(ratio_stone, 1)} [A]."
    )
    return _build_question_payload(
        subskill_id="21_converting_wheelbarrows_to_bucket_ratio",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Convert wheelbarrows to litres (1,75 × 65), then divide each part by 33,2 litres.",
        tier_2=f"Sand/Stone litres = 1,75 × 65 = 113,75 ℓ. Divide by 33,2 = {_fmt(ratio_sand, 1)}.",
        tier_3=f"Ratio = 1 : {_fmt(ratio_sand, 1)} : {_fmt(ratio_stone, 1)}.",
        r=r,
    )


def generate_22_brick_mortar_mix_volume(r: random.Random) -> Dict[str, Any]:
    """Calculate mortar volume and cement bags required for laying standard stock bricks."""
    num_bricks = r.choice([1500, 2000, 2500, 3000])
    rate_m3_per_1000 = 0.30  # 0.3 m3 mortar per 1 000 bricks
    mortar_vol_m3 = (num_bricks / 1000.0) * rate_m3_per_1000  # e.g. 2.0 * 0.3 = 0.6 m3
    cement_bags_per_m3_mortar = 8.0  # 8 bags per m3 of building mortar
    bags_needed = math.ceil(mortar_vol_m3 * cement_bags_per_m3_mortar)

    correct_ans = f"Mortar = {_fmt(mortar_vol_m3, 2)} m³; Cement Required = {bags_needed} bags (50 kg each)"

    custom_options = [
        correct_ans,
        f"Mortar = {_fmt(mortar_vol_m3 * 10, 1)} m³; Cement Required = {bags_needed * 10} bags",
        f"Mortar = {_fmt(mortar_vol_m3, 2)} m³; Cement Required = {math.floor(mortar_vol_m3 * cement_bags_per_m3_mortar)} bags",
        f"Mortar = {_fmt(mortar_vol_m3 / 2, 2)} m³; Cement Required = {bags_needed // 2} bags",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A bricklayer is constructing a boundary wall requiring {_fmt(num_bricks, 0)} standard building bricks.\n"
        f"• Average mortar requirement: 0,30 m³ of mortar per 1 000 bricks\n"
        f"• 8 bags of cement are needed per 1 m³ of bricklaying mortar\n\n"
        f"1. Calculate the total volume of mortar required in cubic metres (m³).\n"
        f"2. How many whole 50 kg bags of cement must be purchased to mix this mortar?"
    )
    explanation = (
        f"Step 1: Calculate mortar volume: ({_fmt(num_bricks, 0)} ÷ 1 000) × 0,30 m³ = {_fmt(mortar_vol_m3, 2)} m³ [M].\n"
        f"Step 2: Calculate cement bags: {_fmt(mortar_vol_m3, 2)} m³ × 8 bags/m³ = {mortar_vol_m3 * 8:.2f} bags [M].\n"
        f"Step 3: Round UP to ensure enough cement: {bags_needed} bags [A]."
    )
    return _build_question_payload(
        subskill_id="22_brick_mortar_mix_volume",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find mortar volume (bricks ÷ 1 000 × 0,30), then multiply by 8 bags per m³.",
        tier_2=f"Mortar = ({num_bricks} ÷ 1 000) × 0,30 = {_fmt(mortar_vol_m3, 2)} m³. Bags = {_fmt(mortar_vol_m3, 2)} × 8.",
        tier_3=f"Purchase {bags_needed} bags.",
        r=r,
    )


def generate_23_plastering_sand_cement_ratio(r: random.Random) -> Dict[str, Any]:
    """Calculate plaster sand and cement quantities using a 1 : 4 volumetric plaster mix."""
    wall_area = r.choice([40, 50, 60, 80])
    thickness_mm = 15.0  # 15 mm plaster layer
    thickness_m = thickness_mm / 1000.0  # 0.015 m
    vol_plaster = wall_area * thickness_m  # e.g. 60 * 0.015 = 0.9 m3

    # Plaster mix 1 : 4 (1 part cement : 4 parts plaster sand)
    # Total parts = 5
    cement_vol_m3 = vol_plaster * (1 / 5.0)  # 0.18 m3
    sand_vol_m3 = vol_plaster * (4 / 5.0)    # 0.72 m3
    # 1 bag cement = 0.0332 m3
    bags_cement = math.ceil(cement_vol_m3 / 0.0332)

    correct_ans = f"Plaster Volume = {_fmt(vol_plaster, 3)} m³; Sand = {_fmt(sand_vol_m3, 2)} m³; Cement = {bags_cement} bags"

    custom_options = [
        correct_ans,
        f"Plaster Volume = {_fmt(vol_plaster * 10, 2)} m³; Sand = {_fmt(sand_vol_m3 * 10, 1)} m³; Cement = {bags_cement * 10} bags",
        f"Plaster Volume = {_fmt(vol_plaster, 3)} m³; Sand = {_fmt(vol_plaster / 2, 2)} m³; Cement = {bags_cement // 2} bags",
        f"Plaster Volume = {_fmt(vol_plaster, 3)} m³; Sand = {_fmt(sand_vol_m3, 2)} m³; Cement = 1 bag",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A contractor must plaster {wall_area} m² of interior brick wall with a uniform thickness of {thickness_mm} mm (0,015 m).\n"
        f"• The plaster is mixed in a ratio of 1 part cement to 4 parts plaster sand (1 : 4 by volume)\n"
        f"• 1 bag of cement has a volume of 0,0332 m³ (33,2 litres)\n\n"
        f"Calculate:\n"
        f"1. The total volume of wet plaster required in m³\n"
        f"2. The volume of plaster sand required in m³\n"
        f"3. The number of whole 50 kg bags of cement to purchase"
    )
    explanation = (
        f"Step 1: Plaster volume = {wall_area} m² × 0,015 m = {_fmt(vol_plaster, 3)} m³ [M].\n"
        f"Step 2: Sand required = {_fmt(vol_plaster, 3)} × (4/5) = {_fmt(sand_vol_m3, 2)} m³ [M].\n"
        f"Step 3: Cement volume = {_fmt(vol_plaster, 3)} × (1/5) = {_fmt(cement_vol_m3, 3)} m³ → {_fmt(cement_vol_m3, 3)} ÷ 0,0332 = {cement_vol_m3 / 0.0332:.1f} → Round UP to {bags_cement} bags [A]."
    )
    return _build_question_payload(
        subskill_id="23_plastering_sand_cement_ratio",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply area by 0,015 m to get total volume. In a 1:4 mix, sand is 4/5 and cement is 1/5 of the total.",
        tier_2=f"Plaster = {wall_area} × 0,015 = {_fmt(vol_plaster, 3)} m³. Sand = 4/5 × {vol_plaster}. Cement = 1/5 × {vol_plaster}.",
        tier_3=f"Sand = {_fmt(sand_vol_m3, 2)} m³; Cement = {bags_cement} bags.",
        r=r,
    )


def generate_24_costing_foundation_concrete_materials(r: random.Random) -> Dict[str, Any]:
    """Calculate the total material invoice cost for a concrete foundation batch."""
    cement_bags = r.choice([35, 40, 45])
    sand_m3 = 2.5
    stone_m3 = 2.5

    price_cement_bag = 118.0
    price_sand_per_m3 = 340.0
    price_stone_per_m3 = 380.0
    delivery_fee = 450.0

    cost_cement = cement_bags * price_cement_bag
    cost_sand = sand_m3 * price_sand_per_m3
    cost_stone = stone_m3 * price_stone_per_m3
    subtotal = cost_cement + cost_sand + cost_stone + delivery_fee
    vat = subtotal * 0.15
    total_invoice = subtotal + vat

    correct_ans = f"Subtotal = {_fmt_curr(subtotal)}; VAT (15%) = {_fmt_curr(vat)}; Total Invoice = {_fmt_curr(total_invoice)}"

    custom_options = [
        correct_ans,
        f"Subtotal = {_fmt_curr(subtotal)}; VAT (15%) = R 0,00; Total Invoice = {_fmt_curr(subtotal)}",
        f"Subtotal = {_fmt_curr(subtotal - delivery_fee)}; VAT (15%) = {_fmt_curr(vat)}; Total Invoice = {_fmt_curr(total_invoice - delivery_fee)}",
        f"Subtotal = {_fmt_curr(subtotal * 1.15)}; VAT (15%) = {_fmt_curr(vat * 1.15)}; Total Invoice = {_fmt_curr(total_invoice * 1.15)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A builder receives an itemized materials quotation for pouring a house foundation:\n"
        f"• {cement_bags} bags of cement @ {_fmt_curr(price_cement_bag)} per bag\n"
        f"• {_fmt(sand_m3, 1)} m³ of river sand @ {_fmt_curr(price_sand_per_m3)} per m³\n"
        f"• {_fmt(stone_m3, 1)} m³ of crushed stone @ {_fmt_curr(price_stone_per_m3)} per m³\n"
        f"• Flat site delivery fee: {_fmt_curr(delivery_fee)}\n\n"
        f"Calculate the subtotal, 15% VAT, and the final total invoice payable."
    )
    explanation = (
        f"Step 1: Calculate material costs:\n"
        f"Cement = {cement_bags} × {_fmt_curr(price_cement_bag)} = {_fmt_curr(cost_cement)}\n"
        f"Sand = {_fmt(sand_m3, 1)} × {_fmt_curr(price_sand_per_m3)} = {_fmt_curr(cost_sand)}\n"
        f"Stone = {_fmt(stone_m3, 1)} × {_fmt_curr(price_stone_per_m3)} = {_fmt_curr(cost_stone)} [M].\n"
        f"Step 2: Subtotal = {_fmt_curr(cost_cement)} + {_fmt_curr(cost_sand)} + {_fmt_curr(cost_stone)} + {_fmt_curr(delivery_fee)} = {_fmt_curr(subtotal)} [M].\n"
        f"Step 3: VAT = 15% × {_fmt_curr(subtotal)} = {_fmt_curr(vat)}; Total = {_fmt_curr(total_invoice)} [A]."
    )
    return _build_question_payload(
        subskill_id="24_costing_foundation_concrete_materials",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply each material quantity by its unit price, add delivery, then add 15% VAT.",
        tier_2=f"Subtotal = {_fmt_curr(cost_cement)} + {_fmt_curr(cost_sand)} + {_fmt_curr(cost_stone)} + {_fmt_curr(delivery_fee)} = {_fmt_curr(subtotal)}.",
        tier_3=f"Total Invoice = {_fmt_curr(total_invoice)}.",
        r=r,
    )
