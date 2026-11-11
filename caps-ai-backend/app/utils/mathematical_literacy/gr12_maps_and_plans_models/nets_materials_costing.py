"""Subskills 17-24: Nets, Materials & Fabrication Costing for Grade 12 Maps & Plans (Models)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_zar,
)


def gen_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Subskill 17: Prism net layout surface area for cardboard model."""
    # Rectangular prism model (building walls): length, width, height in cm
    model_l_cm = r.choice([15.0, 18.0, 20.0, 24.0])
    model_w_cm = r.choice([10.0, 12.0, 14.0])
    model_h_cm = r.choice([5.0, 6.0, 7.0])

    # 4 walls surface area: 2*(l*h) + 2*(w*h)
    wall_area_cm2 = 2 * (model_l_cm * model_h_cm) + 2 * (model_w_cm * model_h_cm)

    d_spec_17 = {
        "diagram_role": "context",
        "kind": "rectangular_prism_net",
        "length": model_l_cm,
        "width": model_w_cm,
        "height": model_h_cm,
        "title": f"Net Dimensions: {_fmt(model_l_cm, 1)} cm x {_fmt(model_w_cm, 1)} cm x {_fmt(model_h_cm, 1)} cm",
    }

    prompt = (
        f"A learner is drafting a flat cardboard net to construct the four exterior walls of a rectangular "
        f"building model. The model dimensions are: Length = {_fmt(model_l_cm, 1)} cm, Width = {_fmt(model_w_cm, 1)} cm, "
        f"and Height = {_fmt(model_h_cm, 1)} cm.\n\n"
        f"Calculate the TOTAL surface area of the four vertical walls on the net, in square centimetres (cm²)."
    )

    correct_ans = f"{_fmt(wall_area_cm2, 1)} cm²"
    custom_opts = [
        correct_ans,
        f"{_fmt(wall_area_cm2 + 2 * (model_l_cm * model_w_cm), 1)} cm²",
        f"{_fmt(wall_area_cm2 / 2, 1)} cm²",
        f"{_fmt((model_l_cm + model_w_cm) * model_h_cm, 1)} cm²",
    ]

    t1 = "The four walls consist of two pairs of opposing rectangular sides."
    t2 = f"Wall area = 2 × (Length × Height) + 2 × (Width × Height)."
    t3 = f"Area = 2 × ({_fmt(model_l_cm, 1)} × {_fmt(model_h_cm, 1)}) + 2 × ({_fmt(model_w_cm, 1)} × {_fmt(model_h_cm, 1)}) = 2 × {_fmt(model_l_cm * model_h_cm, 1)} + 2 × {_fmt(model_w_cm * model_h_cm, 1)} = {_fmt(wall_area_cm2, 1)} cm²."

    explanation = [
        f"Step 1: Identify wall formula: Area = 2(L × H) + 2(W × H) [1 Mark: Method].",
        f"Step 2: Substitute: 2({_fmt(model_l_cm, 1)} × {_fmt(model_h_cm, 1)}) + 2({_fmt(model_w_cm, 1)} × {_fmt(model_h_cm, 1)}) = {_fmt(2 * model_l_cm * model_h_cm, 1)} + {_fmt(2 * model_w_cm * model_h_cm, 1)} [1 Mark: Method].",
        f"Step 3: Total net area for 4 walls = {_fmt(wall_area_cm2, 1)} cm² [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_17",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_17,
    )


def gen_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Subskill 18: Gluing tabs and joint allowance percentage calculation (+10% to +15%)."""
    base_area_cm2 = r.choice([350.0, 420.0, 500.0, 640.0])
    allowance_pct = r.choice([10, 12, 15])
    extra_cm2 = base_area_cm2 * (allowance_pct / 100.0)
    total_area_cm2 = base_area_cm2 + extra_cm2

    prompt = (
        f"A paper craft model has a net surface area of {_fmt(base_area_cm2, 1)} cm² for its visible panels. "
        f"To allow for gluing tabs, overlap seams, and fold margins, the student must add {allowance_pct}% "
        f"to the total card area before purchasing material.\n\n"
        f"Calculate the TOTAL cardboard sheet area required, in square centimetres (cm²)."
    )

    correct_ans = f"{_fmt(total_area_cm2, 1)} cm²"
    custom_opts = [
        correct_ans,
        f"{_fmt(extra_cm2, 1)} cm²",
        f"{_fmt(base_area_cm2 * 2, 1)} cm²",
        f"{_fmt(base_area_cm2 + allowance_pct, 1)} cm²",
    ]

    t1 = f"Calculate {allowance_pct}% of {_fmt(base_area_cm2, 1)} cm²."
    t2 = "Add this tab allowance to the original net surface area."
    t3 = f"Allowance = {_fmt(base_area_cm2, 1)} × {allowance_pct / 100} = {_fmt(extra_cm2, 1)} cm². Total = {_fmt(base_area_cm2, 1)} + {_fmt(extra_cm2, 1)} = {_fmt(total_area_cm2, 1)} cm²."

    explanation = [
        f"Step 1: Calculate tab margin: {_fmt(base_area_cm2, 1)} cm² × {allowance_pct}% = {_fmt(extra_cm2, 1)} cm² [1 Mark: Method].",
        f"Step 2: Add to net surface area: {_fmt(base_area_cm2, 1)} cm² + {_fmt(extra_cm2, 1)} cm² [1 Mark: Method].",
        f"Step 3: Total cardboard required = {_fmt(total_area_cm2, 1)} cm² [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_18",
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


def gen_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Subskill 19: Balsa wood/cardboard sheet optimization (nesting rectangular panels)."""
    # Standard poster foam board in SA: 1 000 mm x 700 mm
    board_l_mm = 1000
    board_w_mm = 700

    panel_l_mm = r.choice([250, 300, 350])
    panel_w_mm = r.choice([150, 200])

    # Option A: align length with length: (1000 // panel_l) * (700 // panel_w)
    fit_a = (board_l_mm // panel_l_mm) * (board_w_mm // panel_w_mm)
    # Option B: align length with width: (1000 // panel_w) * (700 // panel_l)
    fit_b = (board_l_mm // panel_w_mm) * (board_w_mm // panel_l_mm)
    max_fit = max(fit_a, fit_b)

    prompt = (
        f"A student has a standard foam board sheet measuring 1 000 mm × 700 mm.\n"
        f"She needs to cut out rectangular wall panels measuring {panel_l_mm} mm × {panel_w_mm} mm.\n\n"
        f"By comparing both orientations, what is the MAXIMUM number of complete panels that can be cut from this single foam board?"
    )

    correct_ans = f"{max_fit} panels"
    custom_opts = [
        correct_ans,
        f"{min(fit_a, fit_b)} panels" if min(fit_a, fit_b) != max_fit else f"{max_fit - 1} panels",
        f"{max_fit + 2} panels",
        f"{max_fit - 2} panels" if max_fit > 2 else f"{max_fit + 4} panels",
        f"{max_fit + 3} panels",
    ]

    t1 = "Calculate how many panels fit along the length and width for Orientation A."
    t2 = "Calculate how many panels fit along the length and width for Orientation B (rotated 90 degrees)."
    t3 = f"Orientation A: (1 000 ÷ {panel_l_mm} = {board_l_mm // panel_l_mm}) × (700 ÷ {panel_w_mm} = {board_w_mm // panel_w_mm}) = {fit_a}. Orientation B: (1 000 ÷ {panel_w_mm} = {board_l_mm // panel_w_mm}) × (700 ÷ {panel_l_mm} = {board_w_mm // panel_l_mm}) = {fit_b}. Maximum = {max_fit}."

    explanation = [
        f"Step 1: Orientation A: along length = 1 000 ÷ {panel_l_mm} = {board_l_mm // panel_l_mm}; along width = 700 ÷ {panel_w_mm} = {board_w_mm // panel_w_mm}; Total = {board_l_mm // panel_l_mm} × {board_w_mm // panel_w_mm} = {fit_a} panels [1 Mark: Method].",
        f"Step 2: Orientation B: along length = 1 000 ÷ {panel_w_mm} = {board_l_mm // panel_w_mm}; along width = 700 ÷ {panel_l_mm} = {board_w_mm // panel_l_mm}; Total = {board_l_mm // panel_w_mm} × {board_w_mm // panel_l_mm} = {fit_b} panels [1 Mark: Method].",
        f"Step 3: Comparing both yields a maximum of {max_fit} complete panels [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_19",
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


def gen_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Subskill 20: Costing architectural modeling materials."""
    name = r.choice(SA_NAMES)
    sheets_needed = r.choice([3, 4, 5, 6])
    sheet_price = 85.0
    knife_price = 45.0
    glue_price = 38.0
    ruler_price = 28.0

    materials_subtotal = (sheets_needed * sheet_price) + knife_price + glue_price + ruler_price

    prompt = (
        f"{name} is buying supplies at an art and stationary store to build a scale model.\n"
        f"The price list is as follows:\n"
        f"  - 5 mm White Foam Core Board: R 85,00 per sheet\n"
        f"  - Precision Craft Knife: R 45,00\n"
        f"  - Quick-drying PVA Wood Glue (250 ml): R 38,00\n"
        f"  - Steel Cutting Ruler (500 mm): R 28,00\n\n"
        f"If {name} requires {sheets_needed} sheets of foam board and one of each of the other tools, "
        f"calculate the TOTAL expenditure (inclusive of VAT)."
    )

    correct_ans = _fmt_zar(materials_subtotal)
    custom_opts = [
        correct_ans,
        _fmt_zar(materials_subtotal - sheet_price),
        _fmt_zar(materials_subtotal + 100.0),
        _fmt_zar(sheets_needed * sheet_price),
    ]

    t1 = f"Multiply the number of foam sheets ({sheets_needed}) by the unit price of R 85,00."
    t2 = "Add the fixed costs of the craft knife (R 45,00), glue (R 38,00), and steel ruler (R 28,00)."
    t3 = f"Foam board = {sheets_needed} × R 85,00 = {_fmt_zar(sheets_needed * sheet_price)}. Total = {_fmt_zar(sheets_needed * sheet_price)} + R 45,00 + R 38,00 + R 28,00 = {_fmt_zar(materials_subtotal)}."

    explanation = [
        f"Step 1: Cost of foam sheets: {sheets_needed} × R 85,00 = {_fmt_zar(sheets_needed * sheet_price)} [1 Mark: Method].",
        f"Step 2: Add tools: {_fmt_zar(sheets_needed * sheet_price)} + R 45,00 + R 38,00 + R 28,00 [1 Mark: Method].",
        f"Step 3: Total material expenditure = {_fmt_zar(materials_subtotal)} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_20",
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


def gen_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Model paint surface area and spray canister budgeting."""
    # Model surface area in m²: e.g. 1.8 m²
    total_area_m2 = r.choice([1.2, 1.6, 2.0, 2.5, 3.2])
    can_coverage_m2 = 0.8
    # 2 coats of paint required
    paint_needed_m2 = total_area_m2 * 2.0
    cans_exact = paint_needed_m2 / can_coverage_m2
    cans_to_buy = math.ceil(cans_exact)
    price_per_can = 72.50
    total_paint_cost = cans_to_buy * price_per_can

    prompt = (
        f"A completed architectural model has a total paintable surface area of {_fmt(total_area_m2, 2)} m².\n"
        f"The specifications require TWO coats of acrylic spray paint.\n"
        f"Each spray paint canister covers 0,8 m² per coat and costs R 72,50.\n"
        f"(Note: spray cans cannot be bought in fractions; full cans must be purchased).\n\n"
        f"Calculate the minimum number of spray cans to buy and the TOTAL cost of the paint."
    )

    correct_ans = f"{cans_to_buy} cans ({_fmt_zar(total_paint_cost)})"
    custom_opts = [
        correct_ans,
        f"{math.ceil(total_area_m2 / can_coverage_m2)} cans ({_fmt_zar(math.ceil(total_area_m2 / can_coverage_m2) * price_per_can)})",
        f"{cans_to_buy + 1} cans ({_fmt_zar((cans_to_buy + 1) * price_per_can)})",
        f"{cans_to_buy - 1} cans ({_fmt_zar((cans_to_buy - 1) * price_per_can)})",
    ]

    t1 = f"Multiply the surface area ({_fmt(total_area_m2, 2)} m²) by 2 for the two coats."
    t2 = f"Divide total paint area ({_fmt(paint_needed_m2, 2)} m²) by 0,8 m² and round UP to the next whole number."
    t3 = f"Cans = {_fmt(paint_needed_m2, 2)} ÷ 0,8 = {_fmt(cans_exact, 2)} → {cans_to_buy} cans. Total cost = {cans_to_buy} × R 72,50 = {_fmt_zar(total_paint_cost)}."

    explanation = [
        f"Step 1: Total painted area for 2 coats: {_fmt(total_area_m2, 2)} m² × 2 = {_fmt(paint_needed_m2, 2)} m² [1 Mark: Method].",
        f"Step 2: Number of spray cans needed: {_fmt(paint_needed_m2, 2)} ÷ 0,8 = {_fmt(cans_exact, 2)} → Round UP to {cans_to_buy} full cans [1 Mark: Method].",
        f"Step 3: Total paint cost: {cans_to_buy} × R 72,50 = {_fmt_zar(total_paint_cost)} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_21",
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


def gen_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Subskill 22: Laser cutting time and fabrication cost calculation."""
    cut_length_m = r.choice([14.5, 18.0, 22.5, 30.0])
    rate_per_metre = 4.50
    setup_fee = 60.0
    total_cut_cost = setup_fee + (cut_length_m * rate_per_metre)

    prompt = (
        f"An architectural workshop charges a fixed machine setup fee of R 60,00 plus R 4,50 per linear metre "
        f"of cutting path to laser-cut intricate balsa wood components from digital CAD files.\n"
        f"The total cut line path length for a roof truss model is {_fmt(cut_length_m, 1)} m.\n\n"
        f"Calculate the TOTAL cost for laser cutting this model."
    )

    correct_ans = _fmt_zar(total_cut_cost)
    custom_opts = [
        correct_ans,
        _fmt_zar(cut_length_m * rate_per_metre),
        _fmt_zar(total_cut_cost + 50.0),
        _fmt_zar(setup_fee + cut_length_m),
    ]

    t1 = f"Multiply the cutting path length ({_fmt(cut_length_m, 1)} m) by R 4,50/m."
    t2 = "Add the fixed machine setup fee of R 60,00."
    t3 = f"Linear cutting charge = {_fmt(cut_length_m, 1)} × R 4,50 = {_fmt_zar(cut_length_m * rate_per_metre)}. Total = R 60,00 + {_fmt_zar(cut_length_m * rate_per_metre)} = {_fmt_zar(total_cut_cost)}."

    explanation = [
        f"Step 1: Calculate cutting length charge: {_fmt(cut_length_m, 1)} m × R 4,50/m = {_fmt_zar(cut_length_m * rate_per_metre)} [1 Mark: Method].",
        f"Step 2: Add fixed setup fee: R 60,00 + {_fmt_zar(cut_length_m * rate_per_metre)} [1 Mark: Method].",
        f"Step 3: Total laser cutting cost = {_fmt_zar(total_cut_cost)} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_22",
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


def gen_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Subskill 23: Scaled 3D printing filament mass calculation (Volume x Density)."""
    # 3D printed model volume in cm³
    model_vol_cm3 = r.choice([45.0, 60.0, 80.0, 120.0])
    # Density of standard PLA plastic: 1.24 g/cm³
    pla_density = 1.24
    filament_mass_g = model_vol_cm3 * pla_density
    cost_per_kg = 320.0
    cost_filament = (filament_mass_g / 1000.0) * cost_per_kg

    d_spec_23 = {
        "diagram_role": "context",
        "kind": "mensuration_3d",
        "shape": "spiral_staircase_model",
        "volume_cm3": model_vol_cm3,
        "title": f"3D Printed Model (Volume: {_fmt(model_vol_cm3, 1)} cm³)",
    }

    prompt = (
        f"A student 3D-prints a scale model of an intricate spiral staircase with a solid filament volume "
        f"of {_fmt(model_vol_cm3, 1)} cm³.\n"
        f"Standard Polylactic Acid (PLA) 3D printing filament has a density of 1,24 g/cm³ and costs R 320,00 per 1 kg spool.\n\n"
        f"Calculate:\n"
        f"1. The mass of the printed model in grams.\n"
        f"2. The raw material cost of the filament used."
    )

    correct_ans = f"{_fmt(filament_mass_g, 1)} g ({_fmt_zar(cost_filament)})"
    custom_opts = [
        correct_ans,
        f"{_fmt(model_vol_cm3, 1)} g ({_fmt_zar((model_vol_cm3 / 1000.0) * cost_per_kg)})",
        f"{_fmt(filament_mass_g * 1.5, 1)} g ({_fmt_zar(cost_filament * 1.5)})",
        f"{_fmt(filament_mass_g / 2, 1)} g ({_fmt_zar(cost_filament / 2)})",
    ]

    t1 = f"Calculate mass: Volume ({_fmt(model_vol_cm3, 1)} cm³) × Density (1,24 g/cm³)."
    t2 = "Divide the mass in grams by 1 000 to convert to kilograms, then multiply by R 320,00."
    t3 = f"Mass = {_fmt(model_vol_cm3, 1)} × 1,24 = {_fmt(filament_mass_g, 1)} g. In kg = {_fmt(filament_mass_g / 1000, 3)} kg. Cost = {_fmt(filament_mass_g / 1000, 3)} × R 320,00 = {_fmt_zar(cost_filament)}."

    explanation = [
        f"Step 1: Calculate mass = Volume × Density = {_fmt(model_vol_cm3, 1)} cm³ × 1,24 g/cm³ = {_fmt(filament_mass_g, 1)} g [1 Mark: Method].",
        f"Step 2: Convert mass to kg: {_fmt(filament_mass_g, 1)} g ÷ 1 000 = {_fmt(filament_mass_g / 1000, 4)} kg [1 Mark: Method].",
        f"Step 3: Filament cost = {_fmt(filament_mass_g / 1000, 4)} kg × R 320,00 = {_fmt_zar(cost_filament)} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_23",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_23,
    )


def gen_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Subskill 24: Total model production budget with contingency allowance (+10%)."""
    materials_cost = r.choice([380.0, 450.0, 520.0, 600.0])
    laser_cut_cost = r.choice([120.0, 150.0, 180.0])
    baseboard_cost = r.choice([95.0, 110.0, 130.0])

    subtotal = materials_cost + laser_cut_cost + baseboard_cost
    contingency_pct = 10
    contingency = subtotal * (contingency_pct / 100.0)
    grand_total = subtotal + contingency

    prompt = (
        f"A learner compiles a cost estimate to build an architectural display model for a school science expo:\n"
        f"  - Cardboard & modeling materials: {_fmt_zar(materials_cost)}\n"
        f"  - Laser cutting service: {_fmt_zar(laser_cut_cost)}\n"
        f"  - Timber display baseboard: {_fmt_zar(baseboard_cost)}\n"
        f"  - Contingency allowance for unexpected wastage: {contingency_pct}% of the subtotal\n\n"
        f"Calculate the FINAL budgeted project cost."
    )

    correct_ans = _fmt_zar(grand_total)
    custom_opts = [
        correct_ans,
        _fmt_zar(subtotal),
        _fmt_zar(grand_total + 100.0),
        _fmt_zar(subtotal + (contingency * 2)),
    ]

    t1 = f"Sum the three cost items to determine the subtotal: {_fmt_zar(materials_cost)} + {_fmt_zar(laser_cut_cost)} + {_fmt_zar(baseboard_cost)}."
    t2 = f"Calculate {contingency_pct}% of the subtotal for contingency."
    t3 = f"Subtotal = {_fmt_zar(subtotal)}. Contingency = {_fmt_zar(subtotal)} × 10% = {_fmt_zar(contingency)}. Grand Total = {_fmt_zar(subtotal)} + {_fmt_zar(contingency)} = {_fmt_zar(grand_total)}."

    explanation = [
        f"Step 1: Calculate subtotal: {_fmt_zar(materials_cost)} + {_fmt_zar(laser_cut_cost)} + {_fmt_zar(baseboard_cost)} = {_fmt_zar(subtotal)} [1 Mark: Method].",
        f"Step 2: Calculate {contingency_pct}% contingency: {_fmt_zar(subtotal)} × 0,10 = {_fmt_zar(contingency)} [1 Mark: Method].",
        f"Step 3: Total budgeted cost = {_fmt_zar(subtotal)} + {_fmt_zar(contingency)} = {_fmt_zar(grand_total)} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_24",
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
