"""Subskills 47 to 52: Advanced Clinical Dispensing, IV Drip Flow Rates & Healthcare Budgeting.
Covers IV infusion rates in drops per minute (gtt/min), infusion durations, powdered suspension reconstitution,
WHO oral rehydration solution (ORS) ratios, nutritional energy macronutrient calculations (kJ & kcal),
and complete outpatient pediatric prescription cost quotations.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: Intravenous (IV) drip flow rate in drops per minute (gtt/min)."""
    # Drip rate (gtt/min) = [Volume (mL) * Drop Factor (gtt/mL)] / Time (minutes)
    vol_ml = r.choice([500, 1000])
    hours = r.choice([4, 6, 8, 10])
    mins = hours * 60
    drop_factor = 20  # standard macrodrip: 20 drops/mL

    total_drops = vol_ml * drop_factor
    rate_gtt_min = round(total_drops / mins)

    prompt = (
        f"A hospital nurse sets up an intravenous (IV) infusion of Normal Saline:\n"
        f"• Total Volume = {_fmt(vol_ml)} mL to be infused over {hours} hours\n"
        f"• Administration set drop factor = 20 drops per mL (20 gtt/mL)\n\n"
        f"Formula: Drip Flow Rate (drops/min) = [Volume (mL) × Drop Factor (gtt/mL)] ÷ Time (in minutes)\n"
        f"Calculate the drip flow rate in drops per minute (rounded to the nearest whole drop)."
    )

    correct_ans = f"{rate_gtt_min} drops/min"
    explanation = (
        f"1. Time in minutes = {hours} hours × 60 = {mins} minutes.\n"
        f"2. Total drops = {_fmt(vol_ml)} mL × 20 gtt/mL = {_fmt(total_drops)} drops.\n"
        f"3. Flow rate = {_fmt(total_drops)} drops ÷ {mins} min = {total_drops / mins:.2f} ≈ {correct_ans}."
    )
    t1 = "Convert infusion hours to minutes (hours × 60). Multiply volume by 20, then divide by minutes."
    t2 = f"({vol_ml} × 20) ÷ ({hours} × 60) = {total_drops} ÷ {mins}."
    t3 = f"Drip rate = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_47",
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


def gen_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: IV infusion duration: calculating total hours to infuse a saline bag at a set rate."""
    bag_ml = 1000.0
    rate_ml_hr = r.choice([100.0, 125.0, 200.0])

    infusion_hours = round(bag_ml / rate_ml_hr, 1)

    prompt = (
        f"A patient in a medical ward is connected to an infusion pump delivering {_fmt(bag_ml)} mL of Ringers Lactate.\n"
        f"The pump is programmed at a constant rate of {_fmt(rate_ml_hr)} mL per hour.\n\n"
        f"Formula: Infusion Duration (hours) = Total Volume (mL) ÷ Hourly Rate (mL/h)\n"
        f"Calculate the total time (in hours) needed to complete the infusion."
    )

    correct_ans = f"{_fmt(infusion_hours, 1)} hours"
    explanation = (
        f"1. Time = Total Volume ÷ Rate = {_fmt(bag_ml)} mL ÷ {_fmt(rate_ml_hr)} mL/h = {correct_ans}."
    )
    t1 = "Divide the total bag volume by the programmed hourly flow rate."
    t2 = f"{bag_ml} ÷ {rate_ml_hr} = {infusion_hours}."
    t3 = f"Infusion duration = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_48",
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


def gen_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Reconstituting powdered antibiotic: adding sterile water and calculating concentration."""
    total_powder_mg = 2500  # 2 500 mg active antibiotic in dry powder
    water_added_ml = 100    # reconstituted to 100 mL mark

    conc_per_ml = total_powder_mg / water_added_ml  # 25 mg/mL
    conc_per_5ml = conc_per_ml * 5                  # 125 mg / 5 mL

    prompt = (
        f"A pharmacist reconstitutes a bottle of dry antibiotic powder containing 2 500 mg of active drug.\n"
        f"Sterile water is added up to the 100 mL line on the bottle to make a suspension.\n\n"
        f"1. Calculate the concentration of the suspension in milligrams per millilitre (mg/mL).\n"
        f"2. Calculate the equivalent dosage contained in a standard 5 mL medicine spoon."
    )

    correct_ans = f"{_fmt(conc_per_ml)} mg/mL ({_fmt(conc_per_5ml)} mg in 5 mL)"
    explanation = (
        f"1. Concentration per mL = 2 500 mg ÷ 100 mL = {_fmt(conc_per_ml)} mg/mL.\n"
        f"2. Amount in 5 mL = {_fmt(conc_per_ml)} mg/mL × 5 mL = {_fmt(conc_per_5ml)} mg in 5 mL."
    )
    t1 = "Divide total powder mg by 100 mL to get mg/mL, then multiply by 5 for a 5 mL spoon."
    t2 = f"2 500 ÷ 100 = {conc_per_ml} mg/mL. Multiply by 5 = {conc_per_5ml} mg."
    t3 = f"Concentration: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(conc_per_ml * 2)} mg/mL ({_fmt(conc_per_5ml * 2)} mg in 5 mL)",
        f"{_fmt(conc_per_ml)} mg/mL ({_fmt(conc_per_5ml / 2)} mg in 5 mL)",
        f"{_fmt(conc_per_ml / 10)} mg/mL ({_fmt(conc_per_5ml / 10)} mg in 5 mL)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_49",
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


def gen_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: Oral Rehydration Salts (ORS) home recipe mixing ratios."""
    # Standard WHO/DoH home recipe for 1 Litre boiled water:
    # 6 level teaspoons sugar + 1/2 level teaspoon salt in 1 Litre water
    num_litres = r.choice([2, 3, 4, 5])
    sugar_spoons = num_litres * 6
    salt_spoons = round(num_litres * 0.5, 1)

    prompt = (
        f"The South African Department of Health standard home-made Oral Rehydration Solution (ORS) "
        f"for treating dehydration requires the following ratio per 1 Litre of clean boiled water:\n"
        f"• 6 level teaspoons of sugar\n"
        f"• 1/2 (0,5) level teaspoon of salt\n\n"
        f"A community health worker prepares {num_litres} Litres of ORS solution for an outreach clinic.\n"
        f"Calculate the total number of teaspoons of sugar and salt required."
    )

    correct_ans = f"{sugar_spoons} teaspoons sugar, {_fmt(salt_spoons, 1)} teaspoons salt"
    explanation = (
        f"1. Sugar = {num_litres} Litres × 6 teaspoons/L = {sugar_spoons} teaspoons sugar.\n"
        f"2. Salt = {num_litres} Litres × 0,5 teaspoons/L = {_fmt(salt_spoons, 1)} teaspoons salt."
    )
    t1 = f"Multiply the 1-Litre quantities (6 sugar, 0,5 salt) by {num_litres}."
    t2 = f"Sugar = {num_litres} × 6 = {sugar_spoons}. Salt = {num_litres} × 0,5 = {salt_spoons}."
    t3 = f"Recipe quantities: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{sugar_spoons} teaspoons sugar, {num_litres} teaspoons salt",
        f"{sugar_spoons - 6} teaspoons sugar, {_fmt(salt_spoons, 1)} teaspoons salt",
        f"{sugar_spoons * 2} teaspoons sugar, {_fmt(salt_spoons * 2, 1)} teaspoons salt",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_50",
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


def gen_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: Nutritional calorie counting: energy in kJ and kcal from macronutrients."""
    # Macronutrient energy values:
    # Carbohydrates: 4 kcal/g (17 kJ/g)
    # Protein: 4 kcal/g (17 kJ/g)
    # Fat: 9 kcal/g (38 kJ/g)
    carb_g = r.choice([35, 45, 50])
    prot_g = r.choice([15, 20, 25])
    fat_g = r.choice([8, 12, 15])

    total_kcal = carb_g * 4 + prot_g * 4 + fat_g * 9
    total_kj = carb_g * 17 + prot_g * 17 + fat_g * 38

    prompt = (
        f"A meal nutritional label states the following macronutrient composition:\n"
        f"• Carbohydrates: {carb_g} g (provides 4 kcal per gram)\n"
        f"• Protein: {prot_g} g (provides 4 kcal per gram)\n"
        f"• Fat: {fat_g} g (provides 9 kcal per gram)\n\n"
        f"Given that 1 kcal = 4,184 kilojoules (kJ) [or 17 kJ/g carb, 17 kJ/g prot, 38 kJ/g fat]:\n"
        f"1. Calculate the total energy of the meal in calories (kcal).\n"
        f"2. Calculate the total energy in kilojoules (kJ) using standard factors (17 kJ/g carb & prot; 38 kJ/g fat)."
    )

    correct_ans = f"{_fmt(total_kcal)} kcal ({_fmt(total_kj)} kJ)"
    explanation = (
        f"1. Calories: ({carb_g} × 4) + ({prot_g} × 4) + ({fat_g} × 9) = "
        f"{carb_g * 4} + {prot_g * 4} + {fat_g * 9} = {_fmt(total_kcal)} kcal.\n"
        f"2. Kilojoules: ({carb_g} × 17) + ({prot_g} × 17) + ({fat_g} × 38) = "
        f"{carb_g * 17} + {prot_g * 17} + {fat_g * 38} = {_fmt(total_kj)} kJ."
    )
    t1 = "Multiply carbs and protein by 4, fat by 9, and add for kcal. Use 17 and 38 for kJ."
    t2 = f"kcal = {carb_g*4} + {prot_g*4} + {fat_g*9} = {total_kcal}. kJ = {carb_g*17} + {prot_g*17} + {fat_g*38} = {total_kj}."
    t3 = f"Energy = {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(total_kcal * 2)} kcal ({_fmt(total_kj * 2)} kJ)",
        f"{_fmt(total_kcal)} kcal ({_fmt(int(total_kcal * 4.184))} kJ)",
        f"{_fmt((carb_g + prot_g + fat_g) * 4)} kcal ({_fmt(total_kj)} kJ)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_51",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )


def gen_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Full pediatric outpatient clinic quotation: consultation + antibiotic + syrup + vitamins."""
    consultation = r.choice([350.0, 400.0, 450.0])
    antibiotic_susp = r.choice([120.0, 145.0, 160.0])
    paracetamol_syrup = 68.00
    multivitamin_drops = 85.00

    subtotal = consultation + antibiotic_susp + paracetamol_syrup + multivitamin_drops
    # 15% VAT on medicines / consultation
    vat = round(subtotal * 0.15, 2)
    total_bill = round(subtotal + vat, 2)

    prompt = (
        f"A parent visits a private pediatric clinic and receives an itemised invoice:\n"
        f"• General medical consultation: {_fmt_curr(consultation)}\n"
        f"• Amoxicillin 250 mg/5 mL suspension: {_fmt_curr(antibiotic_susp)}\n"
        f"• Paracetamol infant syrup: {_fmt_curr(paracetamol_syrup)}\n"
        f"• Pediatric multivitamin drops: {_fmt_curr(multivitamin_drops)}\n\n"
        f"1. Calculate the subtotal before VAT.\n"
        f"2. Calculate 15% VAT on the subtotal.\n"
        f"3. Calculate the final total payable."
    )

    correct_ans = f"Subtotal: {_fmt_curr(subtotal)} + VAT: {_fmt_curr(vat)} -> Total: {_fmt_curr(total_bill)}"
    explanation = (
        f"1. Subtotal = {_fmt_curr(consultation)} + {_fmt_curr(antibiotic_susp)} + "
        f"{_fmt_curr(paracetamol_syrup)} + {_fmt_curr(multivitamin_drops)} = {_fmt_curr(subtotal)}.\n"
        f"2. 15% VAT = {_fmt_curr(subtotal)} × 0,15 = {_fmt_curr(vat)}.\n"
        f"3. Total payable = {_fmt_curr(subtotal)} + {_fmt_curr(vat)} = {_fmt_curr(total_bill)}."
    )
    t1 = "Sum all 4 line items to find the subtotal, calculate 15% VAT, and add to get the total."
    t2 = f"Subtotal = {_fmt_curr(subtotal)}. VAT = {_fmt_curr(vat)}. Total = {_fmt_curr(total_bill)}."
    t3 = f"Invoice total: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Subtotal: {_fmt_curr(subtotal)} + VAT: R 0,00 -> Total: {_fmt_curr(subtotal)}",
        f"Subtotal: {_fmt_curr(subtotal)} + VAT: {_fmt_curr(vat * 1.5)} -> Total: {_fmt_curr(total_bill + 50)}",
        f"Subtotal: {_fmt_curr(subtotal - 68)} + VAT: {_fmt_curr((subtotal - 68) * 0.15)} -> Total: {_fmt_curr((subtotal - 68) * 1.15)}",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_52",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )
