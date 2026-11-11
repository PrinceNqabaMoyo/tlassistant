"""Subskills 33 to 40: Pediatric Weight-Based Medicine Dosages & Liquid Suspensions.
Covers single-dose mg/kg calculations, multi-interval daily regimens, concentration-to-volume dispensing
(120 mg/5 mL and 250 mg/5 mL suspensions), toxic ceiling safety checks, pediatric oral syringe calibrations,
doses per bottle, and full antibiotic course bottle quantification.
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


def gen_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Subskill 33: Pediatric dose calculation from mg/kg prescription (e.g. Paracetamol 15 mg/kg)."""
    child_weight = r.choice([8.0, 10.0, 12.0, 14.5, 18.0, 22.0])
    dose_per_kg = 15.0  # standard paracetamol 15 mg/kg

    total_dose_mg = round(child_weight * dose_per_kg, 1)

    prompt = (
        f"A clinic doctor prescribes Paracetamol syrup for a feverish toddler weighing {_fmt(child_weight)} kg.\n"
        f"The recommended single dosage is 15 mg per kilogram of body mass (15 mg/kg).\n\n"
        f"Formula: Single Dose (mg) = Child Weight (kg) × Recommended Dose (mg/kg)\n"
        f"Calculate the correct single dose of Paracetamol in milligrams (mg)."
    )

    correct_ans = f"{_fmt(total_dose_mg, 1)} mg"
    explanation = (
        f"1. Formula: Dose = Weight × Rate.\n"
        f"2. Calculation = {_fmt(child_weight)} kg × 15 mg/kg = {correct_ans}."
    )
    t1 = "Multiply the child's weight in kilograms by 15 mg."
    t2 = f"{child_weight} × 15 = {total_dose_mg}."
    t3 = f"Single dose = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_33",
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


def gen_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Subskill 34: Daily dose divided into equal intervals (e.g. 40 mg/kg/day divided into 3 doses)."""
    child_weight = r.choice([12.0, 15.0, 18.0, 24.0])
    daily_rate_per_kg = 40.0  # mg/kg/day (e.g. Amoxicillin)
    num_doses = 3  # every 8 hours

    total_daily_mg = child_weight * daily_rate_per_kg
    dose_per_admin_mg = round(total_daily_mg / num_doses, 1)

    prompt = (
        f"A pediatric patient weighing {_fmt(child_weight)} kg is prescribed an antibiotic.\n"
        f"• Daily dosage rate = 40 mg per kg per day (40 mg/kg/day)\n"
        f"• The daily total must be divided into 3 equal doses (administered every 8 hours)\n\n"
        f"1. Calculate the total daily antibiotic requirement in milligrams (mg).\n"
        f"2. Calculate the amount of antibiotic to be administered in each individual dose."
    )

    correct_ans = f"Daily: {_fmt(total_daily_mg)} mg (Dose: {_fmt(dose_per_admin_mg, 1)} mg every 8 h)"
    explanation = (
        f"1. Total daily dose = {_fmt(child_weight)} kg × 40 mg/kg = {_fmt(total_daily_mg)} mg.\n"
        f"2. Individual dose = {_fmt(total_daily_mg)} mg ÷ 3 = {_fmt(dose_per_admin_mg, 1)} mg."
    )
    t1 = "Multiply weight by 40 for the daily total, then divide by 3 for each dose."
    t2 = f"Total = {_fmt(total_daily_mg)} mg. Each dose = {_fmt(total_daily_mg)} ÷ 3 = {_fmt(dose_per_admin_mg, 1)} mg."
    t3 = f"Dosage regimen: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Daily: {_fmt(total_daily_mg)} mg (Dose: {_fmt(total_daily_mg)} mg every 8 h)",
        f"Daily: {_fmt(total_daily_mg / 3)} mg (Dose: {_fmt(dose_per_admin_mg, 1)} mg every 8 h)",
        f"Daily: {_fmt(total_daily_mg * 2)} mg (Dose: {_fmt(dose_per_admin_mg * 2, 1)} mg every 8 h)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_34",
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


def gen_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Subskill 35: Liquid suspension dose volume calculation (Concentration: 120 mg / 5 mL)."""
    # Standard Paracetamol infant syrup: 120 mg per 5 mL -> 24 mg per mL
    prescribed_mg = r.choice([60, 120, 180, 240])
    # volume_mL = (prescribed_mg / 120) * 5
    volume_ml = round((prescribed_mg / 120.0) * 5.0, 1)

    prompt = (
        f"A clinic nurse needs to administer a {_fmt(prescribed_mg)} mg dose of analgesic syrup to an infant.\n"
        f"The medicine bottle label states a concentration of: 120 mg per 5 mL.\n\n"
        f"Formula: Volume to Administer (mL) = [Prescribed Dose (mg) ÷ Concentration (mg)] × 5 mL\n"
        f"Calculate the volume of liquid medicine (in mL) to measure out for the infant."
    )

    correct_ans = f"{_fmt(volume_ml, 1)} mL"
    explanation = (
        f"1. Ratio: 120 mg is contained in 5 mL (24 mg per 1 mL).\n"
        f"2. Volume = ({_fmt(prescribed_mg)} ÷ 120) × 5 mL = {correct_ans}."
    )
    t1 = "Divide the prescribed milligrams by 120, then multiply by 5 mL."
    t2 = f"Calculation: ({prescribed_mg} ÷ 120) × 5 = {volume_ml}."
    t3 = f"Volume = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_35",
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


def gen_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Subskill 36: Liquid suspension dose volume calculation (Concentration: 250 mg / 5 mL)."""
    # Standard Amoxicillin suspension: 250 mg per 5 mL -> 50 mg per mL
    prescribed_mg = r.choice([125, 250, 375, 500])
    volume_ml = round((prescribed_mg / 250.0) * 5.0, 1)

    prompt = (
        f"A doctor prescribes {_fmt(prescribed_mg)} mg of antibiotic suspension for a child with a chest infection.\n"
        f"The pharmacy dispenses a suspension labelled: 250 mg in 5 mL.\n\n"
        f"Formula: Volume (mL) = [Dose (mg) ÷ 250 mg] × 5 mL\n"
        f"Calculate the volume of suspension to be given per dose in millilitres (mL)."
    )

    correct_ans = f"{_fmt(volume_ml, 1)} mL"
    explanation = (
        f"1. Concentration = 250 mg per 5 mL = 50 mg/mL.\n"
        f"2. Volume = {_fmt(prescribed_mg)} mg ÷ 50 mg/mL = {correct_ans}."
    )
    t1 = "Divide the prescribed dose by 250, then multiply by 5 mL."
    t2 = f"({prescribed_mg} ÷ 250) × 5 = {volume_ml}."
    t3 = f"Volume = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_36",
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


def gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Maximum safe daily dose check: verifying whether prescribed dose exceeds toxic ceiling."""
    weight_kg = r.choice([15.0, 20.0, 25.0])
    max_safe_rate = 60.0  # max 60 mg/kg/day for paracetamol
    max_safe_daily_mg = weight_kg * max_safe_rate

    # Prescribed regimen: e.g. 250 mg every 6 hours = 4 doses * 250 mg = 1000 mg
    dose_mg = r.choice([250, 300, 350])
    prescribed_daily_mg = dose_mg * 4

    is_safe = prescribed_daily_mg <= max_safe_daily_mg
    safe_label = "SAFE (does not exceed ceiling)" if is_safe else "UNSAFE (exceeds maximum threshold)"

    prompt = (
        f"A pediatric safety protocol states that the maximum safe daily dose of Paracetamol "
        f"must NEVER exceed 60 mg per kg of body mass in 24 hours.\n"
        f"A child weighs {_fmt(weight_kg)} kg and is prescribed {_fmt(dose_mg)} mg every 6 hours (4 doses per day).\n\n"
        f"1. Calculate the child's maximum safe daily dose limit in milligrams (mg).\n"
        f"2. Calculate the total prescribed daily dosage ({_fmt(dose_mg)} mg × 4).\n"
        f"3. Determine whether the prescribed dosage is medically safe."
    )

    correct_ans = f"Max Limit: {_fmt(max_safe_daily_mg)} mg; Prescribed: {_fmt(prescribed_daily_mg)} mg ({safe_label})"
    explanation = (
        f"1. Maximum safe limit = {_fmt(weight_kg)} kg × 60 mg/kg = {_fmt(max_safe_daily_mg)} mg.\n"
        f"2. Prescribed daily dose = {_fmt(dose_mg)} mg × 4 = {_fmt(prescribed_daily_mg)} mg.\n"
        f"3. Verdict: {prescribed_daily_mg} mg vs {max_safe_daily_mg} mg limit -> {safe_label}."
    )
    t1 = "Multiply child weight by 60 for the limit. Multiply single dose by 4 for the prescribed total, then compare."
    t2 = f"Limit = {weight_kg} × 60 = {_fmt(max_safe_daily_mg)} mg. Prescribed = {dose_mg} × 4 = {_fmt(prescribed_daily_mg)} mg."
    t3 = f"Safety assessment: {correct_ans}."

    opposite_label = "UNSAFE (exceeds maximum threshold)" if is_safe else "SAFE (does not exceed ceiling)"
    custom_opts = [
        correct_ans,
        f"Max Limit: {_fmt(max_safe_daily_mg)} mg; Prescribed: {_fmt(prescribed_daily_mg)} mg ({opposite_label})",
        f"Max Limit: {_fmt(max_safe_daily_mg * 1.5)} mg; Prescribed: {_fmt(prescribed_daily_mg)} mg (SAFE (does not exceed ceiling))",
        f"Max Limit: {_fmt(max_safe_daily_mg)} mg; Prescribed: {_fmt(dose_mg)} mg (SAFE (does not exceed ceiling))",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_37",
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


def gen_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Subskill 38: Medicine measuring spoon/syringe selection: measuring 2.5 mL, 5.0 mL, or 7.5 mL accurately."""
    prescribed_vol = r.choice([2.5, 5.0, 7.5])

    prompt = (
        f"A mother needs to give her child exactly {_fmt(prescribed_vol, 1)} mL of medicine syrup.\n"
        f"The pharmacy supplied a standard 5 mL medicine measure spoon with a 2,5 mL half-mark,\n"
        f"as well as household kitchen spoons (a teaspoon = 5 mL, tablespoon = 15 mL).\n\n"
        f"How should the mother measure out exactly {_fmt(prescribed_vol, 1)} mL of medicine accurately?"
    )

    if prescribed_vol == 2.5:
        correct_ans = "Use the medical measuring spoon filled exactly to the 2,5 mL half-measure line"
    elif prescribed_vol == 5.0:
        correct_ans = "Use one full level 5 mL medical measuring spoon"
    else:
        correct_ans = "Use one full 5 mL medical spoon plus one 2,5 mL half-measure spoon (5 + 2,5 = 7,5 mL)"

    explanation = (
        f"1. Medical spoons and oral syringes provide calibrated volumetric accuracy.\n"
        f"2. Ordinary kitchen silverware spoons vary widely in shape and volume and should never be used for medicine.\n"
        f"3. Exactly {_fmt(prescribed_vol, 1)} mL is achieved by: {correct_ans}."
    )
    t1 = "Always choose the calibrated medical spoon over uncalibrated kitchen spoons."
    t2 = f"To get {_fmt(prescribed_vol, 1)} mL, use calibrated medical measures."
    t3 = f"Accurate method: {correct_ans}."

    custom_opts = [
        correct_ans,
        "Estimate the volume using a soup spoon from the kitchen cutlery drawer",
        "Fill a 15 mL tablespoon halfway by eye",
        "Pour medicine into a regular drinking glass and guess the level",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_38",
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


def gen_subskill_39(r: random.Random) -> Dict[str, Any]:
    """Subskill 39: Number of doses per medicine bottle (Volume_bottle / Volume_dose)."""
    bottle_vol_ml = r.choice([100, 150, 200])
    dose_vol_ml = r.choice([5.0, 7.5, 10.0])

    num_doses = int(bottle_vol_ml // dose_vol_ml)

    prompt = (
        f"A bottle of cough mixture contains {bottle_vol_ml} mL of syrup.\n"
        f"The patient is instructed to take {_fmt(dose_vol_ml, 1)} mL per dose.\n\n"
        f"Calculate the total number of full doses contained in one bottle."
    )

    correct_ans = f"{num_doses} doses"
    explanation = (
        f"1. Number of doses = Total volume ÷ Dose volume = {bottle_vol_ml} mL ÷ {_fmt(dose_vol_ml, 1)} mL = {correct_ans}."
    )
    t1 = "Divide the total bottle volume in mL by the volume per dose."
    t2 = f"{bottle_vol_ml} ÷ {dose_vol_ml} = {num_doses}."
    t3 = f"Total doses = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_39",
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


def gen_subskill_40(r: random.Random) -> Dict[str, Any]:
    """Subskill 40: Number of full medicine bottles needed for a completed 7-day antibiotic course."""
    days = 7
    doses_per_day = 3
    dose_ml = 5.0  # 5 mL per dose
    bottle_ml = 100.0  # 100 mL bottle

    total_doses = days * doses_per_day  # 21 doses
    total_ml_needed = total_doses * dose_ml  # 105 mL
    bottles_needed = math.ceil(total_ml_needed / bottle_ml)  # 2 bottles

    prompt = (
        f"A child must complete a full {days}-day course of antibiotic suspension:\n"
        f"• Dose = {_fmt(dose_ml, 1)} mL taken {doses_per_day} times daily\n"
        f"• The pharmacy dispenses the suspension in {_fmt(bottle_ml)} mL bottles\n\n"
        f"1. Calculate the total volume of suspension required to complete the {days}-day course.\n"
        f"2. Determine the minimum number of full bottles the pharmacy must dispense."
    )

    correct_ans = f"{_fmt(total_ml_needed)} mL required ({bottles_needed} bottles)"
    explanation = (
        f"1. Total doses = {days} days × {doses_per_day} doses/day = {total_doses} doses.\n"
        f"2. Total volume needed = {total_doses} × {_fmt(dose_ml, 1)} mL = {_fmt(total_ml_needed)} mL.\n"
        f"3. Bottles needed = {_fmt(total_ml_needed)} mL ÷ {_fmt(bottle_ml)} mL/bottle = {total_ml_needed / bottle_ml:.2f}.\n"
        f"4. Since medicine is sold in whole bottles, round up: {bottles_needed} bottles."
    )
    t1 = "Calculate total mL (Days × Doses per day × mL per dose), divide by bottle size, and round up."
    t2 = f"Total = {days} × {doses_per_day} × {dose_ml} = {total_ml_needed} mL. Bottles = {bottles_needed}."
    t3 = f"Prescription requirement: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(total_ml_needed)} mL required (1 bottle)",
        f"{_fmt(total_ml_needed)} mL required (3 bottles)",
        f"{_fmt(days * dose_ml)} mL required (1 bottle)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_40",
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
