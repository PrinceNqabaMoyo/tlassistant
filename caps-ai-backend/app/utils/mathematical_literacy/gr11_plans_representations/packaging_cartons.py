"""Subskills 45 to 52: Packaging Arrangements, Space Utilization & Pallet Loading for Grade 11 Mathematical Literacy."""
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
    """Subskill 45: 1D packing along length, width, and height of a shipping carton."""
    name = r.choice(SA_NAMES)
    item_l, item_w, item_h = 15, 10, 8  # small soap boxes in cm
    carton_l, carton_w, carton_h = 60, 40, 32  # master carton in cm

    n_l = carton_l // item_l
    n_w = carton_w // item_w
    n_h = carton_h // item_h

    prompt = (
        f"A cosmetics distributor packs soap boxes measuring {_fmt(item_l)} cm (length), {_fmt(item_w)} cm (width), "
        f"and {_fmt(item_h)} cm (height) into a shipping carton with internal dimensions of {_fmt(carton_l)} cm (length), "
        f"{_fmt(carton_w)} cm (width), and {_fmt(carton_h)} cm (height).\n"
        f"Without rotating individual boxes, how many soap boxes fit along the length, width, and height of the carton?"
    )

    correct_ans = f"{n_l} along length, {n_w} along width, and {n_h} along height"
    wrong_1 = f"{n_l + 1} along length, {n_w} along width, and {n_h} along height"
    wrong_2 = f"{n_w} along length, {n_l} along width, and {n_h + 1} along height"
    wrong_3 = f"{n_l} along length, {n_w - 1} along width, and {n_h} along height"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Divide carton dimensions by soap box dimensions (integer division) [1 mark].\n"
        f"Along Length = {_fmt(carton_l)} cm ÷ {_fmt(item_l)} cm = {n_l} boxes.\n"
        f"Along Width = {_fmt(carton_w)} cm ÷ {_fmt(item_w)} cm = {n_w} boxes.\n"
        f"Along Height = {_fmt(carton_h)} cm ÷ {_fmt(item_h)} cm = {n_h} boxes.\n"
        f"Step 2: Note that fractional remainders are discarded (only whole boxes fit) [1 mark].\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="45",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide each carton dimension by the corresponding item dimension using whole numbers only.",
        tier_2=f"Length: {carton_l} ÷ {item_l} = {n_l}; Width: {carton_w} ÷ {item_w} = {n_w}; Height: {carton_h} ÷ {item_h} = {n_h}.",
        tier_3=f"Result: {correct_ans}.",
        r=r,
    )


def generate_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Subskill 46: Orientation comparison: test two orientations to maximize packing count."""
    name = r.choice(SA_NAMES)
    item_l = r.choice([20, 25])
    item_w = r.choice([12, 15])
    item_h = 10

    carton_l, carton_w, carton_h = 60, 50, 40

    # Orientation A: item_l along carton_l, item_w along carton_w, item_h along carton_h
    cnt_a = (carton_l // item_l) * (carton_w // item_w) * (carton_h // item_h)
    # Orientation B: item_w along carton_l, item_l along carton_w, item_h along carton_h
    cnt_b = (carton_l // item_w) * (carton_w // item_l) * (carton_h // item_h)

    best_cnt = max(cnt_a, cnt_b)
    best_opt = "Orientation A" if cnt_a >= cnt_b else "Orientation B"
    diff = abs(cnt_a - cnt_b)

    prompt = (
        f"{name} is testing two packaging orientations for small boxes ({_fmt(item_l)} cm × {_fmt(item_w)} cm × {_fmt(item_h)} cm) "
        f"inside a master carton measuring {_fmt(carton_l)} cm × {_fmt(carton_w)} cm × {_fmt(carton_h)} cm:\n"
        f"• Orientation A: Length along length ({item_l} cm along {carton_l} cm), width along width ({item_w} cm along {carton_w} cm).\n"
        f"• Orientation B: Width along length ({item_w} cm along {carton_l} cm), length along width ({item_l} cm along {carton_w} cm).\n"
        f"In both cases, box height ({item_h} cm) aligns with carton height ({carton_h} cm).\n"
        f"Which orientation packs more boxes, and what is the maximum number of boxes packed?"
    )

    correct_ans = f"{best_opt} packs more with {_fmt(best_cnt)} boxes"
    other_opt = "Orientation B" if best_opt == "Orientation A" else "Orientation A"
    wrong_1 = f"{other_opt} packs more with {_fmt(min(cnt_a, cnt_b))} boxes"
    wrong_2 = f"Both orientations pack the exact same number ({_fmt(best_cnt + 5)} boxes)"
    wrong_3 = f"{best_opt} packs more with {_fmt(best_cnt + 8)} boxes"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate count for Orientation A [1 mark].\n"
        f"A: ({carton_l} ÷ {item_l}) × ({carton_w} ÷ {item_w}) × ({carton_h} ÷ {item_h}) = "
        f"{carton_l // item_l} × {carton_w // item_w} × {carton_h // item_h} = {cnt_a} boxes.\n"
        f"Step 2: Calculate count for Orientation B [1 mark].\n"
        f"B: ({carton_l} ÷ {item_w}) × ({carton_w} ÷ {item_l}) × ({carton_h} ÷ {item_h}) = "
        f"{carton_l // item_w} × {carton_w // item_l} × {carton_h // item_h} = {cnt_b} boxes.\n"
        f"Step 3: Compare results [1 mark].\n"
        f"{best_opt} packs {best_cnt} boxes (higher by {diff} boxes) ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="46",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the number of boxes in each direction for both orientations, then multiply and compare.",
        tier_2=f"Orientation A gives {cnt_a} boxes; Orientation B gives {cnt_b} boxes.",
        tier_3=f"{best_opt} packs more ({best_cnt} boxes).",
        r=r,
    )


def generate_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: Total number of unit items packed in a master carton."""
    name = r.choice(SA_NAMES)
    item = r.choice(["tea boxes", "tinned fish cartons", "medicine bottles", "energy bars"])

    n_l = r.choice([4, 5, 6])
    n_w = r.choice([3, 4, 5])
    n_h = r.choice([2, 3, 4])
    total_packed = n_l * n_w * n_h

    prompt = (
        f"A shipping carton is packed with {item} arranged neatly in layers. "
        f"There are {n_l} boxes along the length, {n_w} boxes along the width, "
        f"and {n_h} complete layers stacked vertically.\n"
        f"How many total unit boxes are packed inside this shipping carton?"
    )

    correct_ans = f"{_fmt(total_packed)} boxes"
    wrong_1 = f"{_fmt(n_l + n_w + n_h)} boxes"
    wrong_2 = f"{_fmt(total_packed + n_l)} boxes"
    wrong_3 = f"{_fmt(total_packed - n_w)} boxes"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Understand 3D packing arrangement [1 mark].\n"
        f"Number per layer = Length count × Width count = {n_l} × {n_w} = {n_l * n_w} boxes.\n"
        f"Step 2: Multiply by number of vertical layers [1 mark].\n"
        f"Total boxes = (Length × Width) × Height = {n_l * n_w} × {n_h} = {_fmt(total_packed)} boxes.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="47",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Total items = (items along length) × (items along width) × (items along height).",
        tier_2=f"Multiply {n_l} × {n_w} × {n_h}.",
        tier_3=f"Total = {_fmt(total_packed)} boxes.",
        r=r,
    )


def generate_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Unused (wasted) volume in a master carton after optimal packing."""
    name = r.choice(SA_NAMES)
    carton_l, carton_w, carton_h = 50, 40, 30
    carton_vol = carton_l * carton_w * carton_h  # 60 000 cm³

    item_l, item_w, item_h = 12, 10, 8
    item_vol = item_l * item_w * item_h  # 960 cm³

    n_l = carton_l // item_l  # 4
    n_w = carton_w // item_w  # 4
    n_h = carton_h // item_h  # 3
    total_items = n_l * n_w * n_h  # 48 items
    packed_vol = total_items * item_vol  # 48 * 960 = 46 080 cm³

    wasted_vol = carton_vol - packed_vol

    prompt = (
        f"A master carton has internal dimensions of {_fmt(carton_l)} cm × {_fmt(carton_w)} cm × {_fmt(carton_h)} cm "
        f"(total internal volume = {_fmt(carton_vol)} cm³). "
        f"It is packed with the maximum possible number of identical smaller boxes measuring "
        f"{_fmt(item_l)} cm × {_fmt(item_w)} cm × {_fmt(item_h)} cm (volume = {_fmt(item_vol)} cm³ each). "
        f"Altogether, {total_items} boxes fit inside.\n"
        f"Calculate the unused (empty / wasted) volume remaining inside the carton in cm³."
    )

    correct_ans = f"{_fmt(wasted_vol)} cm³"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Calculate total volume occupied by packed boxes [1 mark].\n"
        f"Packed volume = {total_items} boxes × {_fmt(item_vol)} cm³/box = {_fmt(packed_vol)} cm³.\n"
        f"Step 2: Subtract packed volume from total carton volume [1 mark].\n"
        f"Unused volume = Carton Volume - Packed Volume = {_fmt(carton_vol)} cm³ - {_fmt(packed_vol)} cm³ = {_fmt(wasted_vol)} cm³.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="48",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Unused Volume = Total Carton Volume - Total Volume of Packed Items.",
        tier_2=f"Carton volume = {_fmt(carton_vol)} cm³. Packed items = {total_items} × {_fmt(item_vol)} = {_fmt(packed_vol)} cm³.",
        tier_3=f"Difference = {_fmt(wasted_vol)} cm³.",
        r=r,
    )


def generate_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Packaging efficiency / space utilization percentage."""
    name = r.choice(SA_NAMES)
    carton_vol = r.choice([48000, 60000, 72000, 80000])
    eff_percent = r.choice([75.0, 76.8, 80.0, 82.5, 85.0])
    packed_vol = round(carton_vol * (eff_percent / 100), 1)

    prompt = (
        f"A shipping container carton has an internal volume of {_fmt(carton_vol)} cm³. "
        f"When fully packed with {name}'s retail packages, the total volume of all packed goods is "
        f"{_fmt(packed_vol)} cm³.\n"
        f"Calculate the space utilization (packaging efficiency) percentage of the carton (round to one decimal place)."
    )

    correct_ans = f"{_fmt(eff_percent, 1)}%"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: State the efficiency formula [1 mark].\n"
        f"\\text{{Efficiency}} = \\left( \\frac{{\\text{{Packed Volume}}}}{{\\text{{Total Carton Volume}}}} \\right) \\times 100\\%.\n"
        f"Step 2: Substitute values [1 mark].\n"
        f"\\text{{Efficiency}} = \\left( \\frac{{{_fmt(packed_vol)}}}{{{_fmt(carton_vol)}}} \\right) \\times 100\\% = {_fmt(eff_percent, 1)}\\%.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="49",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Space Utilization % = (Packed Volume ÷ Total Carton Volume) × 100%.",
        tier_2=f"Divide {_fmt(packed_vol)} by {_fmt(carton_vol)} and multiply by 100.",
        tier_3=f"Efficiency = {_fmt(eff_percent, 1)}%.",
        r=r,
    )


def generate_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: Packing cylindrical cans into rectangular shipping cartons."""
    name = r.choice(SA_NAMES)
    can_diam = r.choice([7, 8, 10])  # can diameter in cm
    can_h = r.choice([11, 12, 14])    # can height in cm

    carton_l = r.choice([40, 48, 56])
    carton_w = r.choice([24, 32, 40])
    carton_h = r.choice([24, 28, 30])

    n_l = carton_l // can_diam
    n_w = carton_w // can_diam
    n_h = carton_h // can_h
    total_cans = n_l * n_w * n_h

    prompt = (
        f"A food manufacturer packs cylindrical soup cans with a diameter of {_fmt(can_diam)} cm and a height of "
        f"{_fmt(can_h)} cm upright into a cardboard carton with internal dimensions of {_fmt(carton_l)} cm (length), "
        f"{_fmt(carton_w)} cm (width), and {_fmt(carton_h)} cm (height).\n"
        f"How many whole soup cans can be packed upright into one carton?"
    )

    correct_ans = f"{_fmt(total_cans)} cans"
    wrong_1 = f"{_fmt(total_cans + n_l)} cans"
    wrong_2 = f"{_fmt(total_cans - n_w)} cans"
    wrong_3 = f"{_fmt(n_l * n_w)} cans"  # only one layer
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate cans along base dimensions using can diameter [1 mark].\n"
        f"Cans along Length = {_fmt(carton_l)} ÷ {_fmt(can_diam)} = {n_l} cans.\n"
        f"Cans along Width = {_fmt(carton_w)} ÷ {_fmt(can_diam)} = {n_w} cans.\n"
        f"Cans per layer = {n_l} × {n_w} = {n_l * n_w} cans.\n"
        f"Step 2: Calculate vertical layers using can height [1 mark].\n"
        f"Layers = {_fmt(carton_h)} ÷ {_fmt(can_h)} = {n_h} layers.\n"
        f"Step 3: Calculate total cans [1 mark].\n"
        f"Total Cans = {n_l * n_w} × {n_h} = {_fmt(total_cans)} cans ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="50",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Each can occupies a square footprint of (diameter × diameter) on the base.",
        tier_2=f"Length: {carton_l} ÷ {can_diam} = {n_l}; Width: {carton_w} ÷ {can_diam} = {n_w}; Layers: {carton_h} ÷ {can_h} = {n_h}.",
        tier_3=f"Total cans = {n_l} × {n_w} × {n_h} = {_fmt(total_cans)} cans.",
        r=r,
    )


def generate_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: Packing master cartons onto a standard South African shipping pallet."""
    name = r.choice(SA_NAMES)
    pallet_l = 1200  # mm
    pallet_w = 1000  # mm
    max_height_mm = 1600  # max stack height above pallet

    carton_l_mm = r.choice([400, 300])
    carton_w_mm = r.choice([300, 250, 200])
    carton_h_mm = r.choice([200, 250])

    n_l = pallet_l // carton_l_mm
    n_w = pallet_w // carton_w_mm
    per_layer = n_l * n_w

    layers = max_height_mm // carton_h_mm
    total_pallet_cartons = per_layer * layers

    prompt = (
        f"A logistics warehouse stacks master cartons measuring {_fmt(carton_l_mm)} mm × {_fmt(carton_w_mm)} mm "
        f"× {_fmt(carton_h_mm)} mm onto a standard South African wooden pallet measuring {_fmt(pallet_l)} mm by "
        f"{_fmt(pallet_w)} mm. "
        f"Safety rules state that the cartons may not overhang the pallet edges, and the maximum allowable stack "
        f"height above the pallet is {_fmt(max_height_mm / 1000, 1)} m ({_fmt(max_height_mm)} mm).\n"
        f"What is the maximum number of cartons that can be stacked onto one pallet?"
    )

    correct_ans = f"{_fmt(total_pallet_cartons)} cartons"
    wrong_1 = f"{_fmt(per_layer * (layers + 1))} cartons"
    wrong_2 = f"{_fmt(total_pallet_cartons - per_layer)} cartons"
    wrong_3 = f"{_fmt(per_layer)} cartons"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate cartons per layer [1 mark].\n"
        f"Along length: {pallet_l} ÷ {carton_l_mm} = {n_l} cartons.\n"
        f"Along width: {pallet_w} ÷ {carton_w_mm} = {n_w} cartons.\n"
        f"Cartons per layer = {n_l} × {n_w} = {per_layer} cartons.\n"
        f"Step 2: Calculate maximum number of vertical layers [1 mark].\n"
        f"Layers = {max_height_mm} ÷ {carton_h_mm} = {layers} layers.\n"
        f"Step 3: Calculate total cartons on pallet [1 mark].\n"
        f"Total cartons = {per_layer} cartons/layer × {layers} layers = {_fmt(total_pallet_cartons)} cartons ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="51",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Determine how many cartons fit in one layer on the 1 200 mm × 1 000 mm base, then multiply by the number of vertical layers.",
        tier_2=f"Cartons per layer = ({pallet_l} ÷ {carton_l_mm}) × ({pallet_w} ÷ {carton_w_mm}) = {n_l} × {n_w} = {per_layer}. Layers = {max_height_mm} ÷ {carton_h_mm} = {layers}.",
        tier_3=f"Total = {per_layer} × {layers} = {_fmt(total_pallet_cartons)} cartons.",
        r=r,
    )


def generate_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Total shipping mass and volume calculation for a fully packed pallet."""
    name = r.choice(SA_NAMES)
    num_cartons = r.choice([40, 48, 60, 72])
    mass_per_carton_kg = r.choice([12.5, 14.0, 15.0, 16.5, 18.0])
    pallet_tare_kg = 25.0  # empty pallet mass

    cartons_mass = num_cartons * mass_per_carton_kg
    total_gross_mass = round(cartons_mass + pallet_tare_kg, 1)

    prompt = (
        f"{name} prepares a fully loaded pallet carrying {_fmt(num_cartons)} cartons for road freight delivery. "
        f"Each carton has a gross mass of {_fmt(mass_per_carton_kg)} kg. "
        f"The empty wooden pallet itself has a tare mass of {_fmt(pallet_tare_kg)} kg.\n"
        f"Calculate the total gross shipping mass of the loaded pallet in kilograms (kg)."
    )

    correct_ans = f"{_fmt(total_gross_mass)} kg"
    wrong_1 = f"{_fmt(cartons_mass)} kg"  # forgot pallet tare
    wrong_2 = f"{_fmt(total_gross_mass + 50.0)} kg"
    wrong_3 = f"{_fmt(total_gross_mass * 1.5)} kg"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate total mass of all cartons [1 mark].\n"
        f"Cartons mass = {_fmt(num_cartons)} × {_fmt(mass_per_carton_kg)} kg = {_fmt(cartons_mass)} kg.\n"
        f"Step 2: Add tare mass of the wooden pallet [1 mark].\n"
        f"Gross mass = Cartons mass + Pallet tare = {_fmt(cartons_mass)} kg + {_fmt(pallet_tare_kg)} kg = {_fmt(total_gross_mass)} kg.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="52",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the number of cartons by the mass of each carton, then add the tare mass of the wooden pallet.",
        tier_2=f"Cartons = {_fmt(num_cartons)} × {_fmt(mass_per_carton_kg)} = {_fmt(cartons_mass)} kg. Add {_fmt(pallet_tare_kg)} kg for the pallet.",
        tier_3=f"Total gross mass = {_fmt(total_gross_mass)} kg.",
        r=r,
    )
