"""Subskills 41-46: Pallet Stacking & Shipping Container Loading for Grade 12 Maps & Plans (Models)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def gen_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Number of cartons on a single pallet layer (1 200 mm x 1 000 mm ISO pallet)."""
    # Standard South African pallet: 1 200 mm x 1 000 mm
    pallet_l = 1200
    pallet_w = 1000

    # Carton sizes:
    # 1. 400 x 300 mm -> (1200//400)*(1000//300) = 3 * 3 = 9 OR (1200//300)*(1000//400) = 4 * 2 = 8
    # 2. 600 x 400 mm -> (1200//600)*(1000//400) = 2 * 2 = 4 OR (1200//400)*(1000//600) = 3 * 1 = 3 -> 5 interlocking!
    # Let's test a clean rectangular grid:
    carton_l = r.choice([400, 300])
    carton_w = r.choice([250, 200])

    fit_1 = (pallet_l // carton_l) * (pallet_w // carton_w)
    fit_2 = (pallet_l // carton_w) * (pallet_w // carton_l)
    max_cartons = max(fit_1, fit_2)

    prompt = (
        f"A distribution warehouse in Durban packs identical product cartons onto standard South African wooden pallets "
        f"measuring 1 200 mm long by 1 000 mm wide.\n"
        f"Each carton measures {carton_l} mm long by {carton_w} mm wide.\n"
        f"The cartons must not overhang the edges of the pallet.\n\n"
        f"By comparing both grid orientations, calculate the MAXIMUM number of cartons that can fit on a SINGLE layer."
    )

    correct_ans = f"{max_cartons} cartons per layer"
    custom_opts = [
        correct_ans,
        f"{min(fit_1, fit_2)} cartons per layer" if min(fit_1, fit_2) != max_cartons else f"{max_cartons - 2} cartons per layer",
        f"{max_cartons + 2} cartons per layer",
        f"{max_cartons - 3} cartons per layer",
        f"{max_cartons + 4} cartons per layer",
    ]

    t1 = "Calculate how many cartons fit along length and width for Orientation 1."
    t2 = "Calculate how many cartons fit along length and width for Orientation 2 (rotated 90°)."
    t3 = f"Orientation 1: ({pallet_l} ÷ {carton_l} = {pallet_l // carton_l}) × ({pallet_w} ÷ {carton_w} = {pallet_w // carton_w}) = {fit_1}. Orientation 2: ({pallet_l} ÷ {carton_w} = {pallet_l // carton_w}) × ({pallet_w} ÷ {carton_l} = {pallet_w // carton_l}) = {fit_2}. Maximum = {max_cartons}."

    explanation = [
        f"Step 1: Orientation 1: Length fit = {pallet_l} ÷ {carton_l} = {pallet_l // carton_l}; Width fit = {pallet_w} ÷ {carton_w} = {pallet_w // carton_w}; Total = {pallet_l // carton_l} × {pallet_w // carton_w} = {fit_1} [1 Mark: Method].",
        f"Step 2: Orientation 2: Length fit = {pallet_l} ÷ {carton_w} = {pallet_l // carton_w}; Width fit = {pallet_w} ÷ {carton_l} = {pallet_w // carton_l}; Total = {pallet_l // carton_w} × {pallet_w // carton_l} = {fit_2} [1 Mark: Method].",
        f"Step 3: Comparing both yields a maximum of {max_cartons} cartons per layer [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_41",
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


def gen_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Subskill 42: Interlocking pallet stacking layer count to maximum height limit."""
    pallet_base_h_mm = 150  # Pallet wooden base height = 150 mm
    max_total_h_mm = 1800  # Warehouse maximum safe stack height = 1 800 mm
    carton_h_mm = r.choice([200, 250, 300])

    available_h_mm = max_total_h_mm - pallet_base_h_mm
    layers_count = available_h_mm // carton_h_mm
    total_stack_h = pallet_base_h_mm + (layers_count * carton_h_mm)

    prompt = (
        f"A logistics safety standard sets the maximum total height for a stacked pallet at 1 800 mm (including the wooden pallet base).\n"
        f"The wooden pallet base is 150 mm high.\n"
        f"If the cartons stacked on the pallet each have a height of {carton_h_mm} mm, "
        f"what is the MAXIMUM number of full layers that can be stacked safely?"
    )

    correct_ans = f"{layers_count} layers (Total height: {_fmt(total_stack_h, 0)} mm)"
    custom_opts = [
        correct_ans,
        f"{layers_count + 1} layers (Total height: {_fmt(total_stack_h + carton_h_mm, 0)} mm)",
        f"{layers_count + 2} layers (Total height: {_fmt(total_stack_h + (2 * carton_h_mm), 0)} mm)",
        f"{layers_count - 1} layers (Total height: {_fmt(total_stack_h - carton_h_mm, 0)} mm)",
        f"{layers_count - 2} layers (Total height: {_fmt(total_stack_h - (2 * carton_h_mm), 0)} mm)",
    ]

    t1 = f"Subtract the pallet base height (150 mm) from the maximum allowed height (1 800 mm)."
    t2 = f"Divide the remaining height ({available_h_mm} mm) by the height of one carton ({carton_h_mm} mm)."
    t3 = f"Available height = 1 800 - 150 = {available_h_mm} mm. Layers = {available_h_mm} ÷ {carton_h_mm} = {available_h_mm / carton_h_mm:.2f} → {layers_count} full layers."

    explanation = [
        f"Step 1: Calculate available height for cartons: 1 800 mm - 150 mm = {available_h_mm} mm [1 Mark: Method].",
        f"Step 2: Divide available height by carton height: {available_h_mm} ÷ {carton_h_mm} = {available_h_mm / carton_h_mm:.2f} [1 Mark: Method].",
        f"Step 3: Discard the remainder: Maximum safe stack = {layers_count} layers ({_fmt(total_stack_h, 0)} mm total height) [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_42",
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


def gen_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Subskill 43: Pallet total gross mass and forklift load limit check."""
    cartons_per_layer = r.choice([6, 8, 10])
    layers = r.choice([4, 5, 6])
    total_cartons = cartons_per_layer * layers
    mass_per_carton_kg = r.choice([18.5, 22.0, 25.0])
    pallet_base_kg = 25.0

    carton_mass_total = total_cartons * mass_per_carton_kg
    total_pallet_mass_kg = carton_mass_total + pallet_base_kg

    forklift_limit_kg = 1000.0
    safe = total_pallet_mass_kg <= forklift_limit_kg
    status = (
        f"{_fmt(total_pallet_mass_kg, 1)} kg (Safe: below 1 000 kg forklift limit)"
        if safe
        else f"{_fmt(total_pallet_mass_kg, 1)} kg (Unsafe: exceeds 1 000 kg forklift limit)"
    )

    prompt = (
        f"A pallet is stacked with {layers} layers of cartons, with {cartons_per_layer} cartons per layer.\n"
        f"Each carton has a gross mass of {_fmt(mass_per_carton_kg, 1)} kg.\n"
        f"The empty wooden pallet base has a tare mass of 25,0 kg.\n"
        f"The warehouse forklift has a strict safe working load limit of 1 000 kg.\n\n"
        f"Calculate the total gross mass of the loaded pallet and determine whether it is safe for the forklift to lift."
    )

    correct_ans = status
    custom_opts = [
        correct_ans,
        f"{_fmt(carton_mass_total, 1)} kg (Safe: excludes pallet base)",
        f"{_fmt(total_pallet_mass_kg * 1.2, 1)} kg (Unsafe: exceeds limit)",
        f"{_fmt(total_pallet_mass_kg - 50.0, 1)} kg (Safe: below 1 000 kg forklift limit)",
    ]

    t1 = f"Calculate total number of cartons: {layers} layers × {cartons_per_layer} = {total_cartons} cartons."
    t2 = f"Calculate total carton mass: {total_cartons} × {_fmt(mass_per_carton_kg, 1)} kg = {_fmt(carton_mass_total, 1)} kg."
    t3 = f"Add the 25,0 kg pallet base: {_fmt(carton_mass_total, 1)} + 25 = {_fmt(total_pallet_mass_kg, 1)} kg. Compare to 1 000 kg."

    explanation = [
        f"Step 1: Total cartons = {layers} × {cartons_per_layer} = {total_cartons} cartons [1 Mark: Method].",
        f"Step 2: Total carton mass = {total_cartons} × {_fmt(mass_per_carton_kg, 1)} kg = {_fmt(carton_mass_total, 1)} kg [1 Mark: Method].",
        f"Step 3: Total pallet mass = {_fmt(carton_mass_total, 1)} + 25,0 = {_fmt(total_pallet_mass_kg, 1)} kg → {status} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_43",
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


def gen_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Loading pallets into a 6 m (20 ft) shipping container."""
    # Standard 20 ft GP shipping container internal dimensions:
    # Length = 5 898 mm (~5.9 m), Width = 2 352 mm (~2.35 m)
    # Standard SA/ISO pallet: 1 200 mm x 1 000 mm
    # Along width (2 352 mm): 2 pallets of 1 000 mm fit side-by-side with 1 200 mm facing the length:
    # 2 rows of 1 000 mm = 2 000 mm (fits within 2 352 mm).
    # Along length (5 898 mm): 5 898 // 1 200 = 4 pallets (4 * 1 200 = 4 800 mm). Or with mixed orientation:
    # Standard 20ft container holds 10 standard pallets (or 11 Euro pallets 1200x800).
    container_l_mm = 5898
    container_w_mm = 2352

    prompt = (
        f"A freight forwarding company in Cape Town is packing standard South African wooden pallets (1 200 mm × 1 000 mm) "
        f"into a standard 6-metre (20 ft) general purpose shipping container.\n"
        f"The internal dimensions of the container are:\n"
        f"  - Length = 5 898 mm\n"
        f"  - Width = 2 352 mm\n"
        f"Pallets cannot be stacked on top of one another (single floor tier only).\n\n"
        f"What is the standard maximum number of 1 200 mm × 1 000 mm pallets that can be arranged on the container floor?"
    )

    correct_ans = "10 standard pallets (2 rows of 5 pallets placed side-by-side)"
    custom_opts = [
        correct_ans,
        "14 standard pallets (2 rows of 7 pallets)",
        "8 standard pallets (2 rows of 4 pallets)",
        "12 standard pallets (3 rows of 4 pallets)",
    ]

    t1 = "Consider the width of the container: 2 352 mm. Two 1 000 mm pallet widths equal 2 000 mm, fitting side-by-side."
    t2 = "Along the length (5 898 mm), 1 200 mm pallets can be arranged end-to-end: 4 or 5 depending on pinwheel/interlocking."
    t3 = "The industry standard packing layout for 1 200 mm × 1 000 mm pallets in a 20 ft container is 10 pallets."

    explanation = [
        f"Step 1: Check container internal width: 2 352 mm accommodates 2 pallets of 1 000 mm side-by-side (2 000 mm < 2 352 mm) [1 Mark: Method].",
        f"Step 2: Check length arrangement: Interlocking / pinwheel loading accommodates 10 full pallets within 5 898 mm [1 Mark: Method].",
        f"Step 3: Conclude: 10 standard pallets on the floor tier [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_44",
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


def gen_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Subskill 45: Loading pallets into a 12 m (40 ft) shipping container."""
    prompt = (
        "A manufacturing plant is exporting goods using a standard 12-metre (40 ft) shipping container "
        "with an internal length of 12 032 mm and internal width of 2 352 mm.\n"
        "The goods are secured on standard pallets (1 200 mm × 1 000 mm) in a single floor tier.\n\n"
        "What is the standard maximum capacity of 1 200 mm × 1 000 mm pallets that fit on the floor of a 40 ft container?"
    )

    correct_ans = "20 to 21 standard pallets"
    custom_opts = [
        correct_ans,
        "28 to 30 standard pallets",
        "15 to 16 standard pallets",
        "10 to 11 standard pallets",
    ]

    t1 = "A 40 ft container is roughly double the length of a 20 ft container (12 m vs 6 m)."
    t2 = "Since a 20 ft container accommodates 10 standard pallets, a 40 ft container accommodates approximately 2 × 10 = 20 to 21 pallets."
    t3 = "The standard capacity is 20 to 21 standard 1 200 mm × 1 000 mm pallets."

    explanation = [
        f"Step 1: Internal length = 12 032 mm, internal width = 2 352 mm [1 Mark: Method].",
        f"Step 2: 2 rows of 1 000 mm width fit across the 2 352 mm beam [1 Mark: Method].",
        f"Step 3: Length fit = 12 032 ÷ 1 200 = 10 pairs = 20 pallets (or 21 with pinwheel layout) [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_45",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )


def gen_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Subskill 46: Palletized container space utilization efficiency (%)."""
    # 20 ft container internal volume = 33.2 m³
    container_vol_m3 = 33.2
    # 10 pallets loaded. Each palletized cargo unit volume:
    pallet_w_m = 1.0
    pallet_l_m = 1.2
    pallet_h_m = r.choice([1.4, 1.5, 1.6, 1.7])
    single_pallet_vol_m3 = pallet_w_m * pallet_l_m * pallet_h_m
    total_cargo_vol_m3 = 10 * single_pallet_vol_m3

    efficiency_pct = (total_cargo_vol_m3 / container_vol_m3) * 100.0

    prompt = (
        f"A 6-metre shipping container has a total internal volume of {_fmt(container_vol_m3, 1)} m³.\n"
        f"Ten identical loaded pallets are placed inside. Each loaded pallet occupies a bounding cuboid of "
        f"1,2 m long by 1,0 m wide by {_fmt(pallet_h_m, 2)} m high.\n\n"
        f"Calculate the volumetric space utilization efficiency percentage of the container.\n"
        f"(Formula: Efficiency % = [Total Cargo Volume ÷ Container Volume] × 100)."
    )

    correct_ans = f"{_fmt(efficiency_pct, 1)}%"
    custom_opts = [
        correct_ans,
        f"{_fmt(efficiency_pct * 0.8, 1)}%",
        f"{_fmt(efficiency_pct * 1.15, 1)}%",
        f"{_fmt(total_cargo_vol_m3, 1)}%",
    ]

    t1 = f"Calculate the volume of one loaded pallet: 1,2 m × 1,0 m × {_fmt(pallet_h_m, 2)} m."
    t2 = f"Multiply by 10 to get total cargo volume, then divide by {_fmt(container_vol_m3, 1)} m³."
    t3 = f"Single pallet = {_fmt(single_pallet_vol_m3, 3)} m³. Total = {_fmt(total_cargo_vol_m3, 2)} m³. Efficiency = ({_fmt(total_cargo_vol_m3, 2)} ÷ {_fmt(container_vol_m3, 1)}) × 100 = {_fmt(efficiency_pct, 1)}%."

    explanation = [
        f"Step 1: Calculate single pallet volume = 1,2 × 1,0 × {_fmt(pallet_h_m, 2)} = {_fmt(single_pallet_vol_m3, 3)} m³ [1 Mark: Method].",
        f"Step 2: Total cargo volume = 10 × {_fmt(single_pallet_vol_m3, 3)} m³ = {_fmt(total_cargo_vol_m3, 2)} m³ [1 Mark: Method].",
        f"Step 3: Space efficiency = ({_fmt(total_cargo_vol_m3, 2)} ÷ {_fmt(container_vol_m3, 1)}) × 100 = {_fmt(efficiency_pct, 1)}% [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_46",
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
