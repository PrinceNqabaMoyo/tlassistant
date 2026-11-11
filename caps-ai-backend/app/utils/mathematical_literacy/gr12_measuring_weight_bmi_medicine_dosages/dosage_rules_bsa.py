"""Subskills 41 to 46: Classical Pediatric Dosage Rules & Body Surface Area (BSA) Formulation.
Covers Clark's Rule (kg and lb variants), Young's Rule (age in years), Fried's Rule (infant months),
Body Surface Area (BSA in m²) chemotherapy/specialist dosing,
and clinical analysis of weight-based vs age-based pharmacological safety.
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


def gen_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Subskill 41: Clark's Rule: child dose from adult dose using weight in kilograms."""
    # Clark's rule (kg): Child dose = (Weight in kg / 68 kg) * Adult dose
    adult_dose_mg = r.choice([250, 500, 750, 1000])
    child_weight_kg = r.choice([17.0, 20.4, 27.2, 34.0])

    child_dose = round((child_weight_kg / 68.0) * adult_dose_mg, 1)

    prompt = (
        f"Clark's Rule calculates a child's medicine dosage based on body mass in kilograms:\n"
        f"Child Dose (mg) = [Child Weight (in kg) ÷ 68 kg] × Adult Dose (mg)\n\n"
        f"An adult dose of antibiotic is {adult_dose_mg} mg.\n"
        f"Calculate the appropriate child dose for a {_fmt(child_weight_kg)} kg child in milligrams (mg)."
    )

    correct_ans = f"{_fmt(child_dose, 1)} mg"
    explanation = (
        f"1. Fraction = {_fmt(child_weight_kg)} ÷ 68 = {child_weight_kg / 68.0:.4f}.\n"
        f"2. Child dose = {child_weight_kg / 68.0:.4f} × {adult_dose_mg} mg = {correct_ans}."
    )
    t1 = "Divide the child's weight in kg by 68, then multiply by the adult dose."
    t2 = f"({child_weight_kg} ÷ 68) × {adult_dose_mg} = {child_dose}."
    t3 = f"Child dose = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_41",
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
    """Subskill 42: Clark's Rule: child dose from adult dose using weight in pounds (lb)."""
    # Clark's rule (lb): Child dose = (Weight in lb / 150) * Adult dose
    adult_dose_mg = r.choice([200, 300, 400, 500])
    child_weight_lb = r.choice([30, 45, 60, 75])

    child_dose = round((child_weight_lb / 150.0) * adult_dose_mg, 1)

    prompt = (
        f"The imperial version of Clark's Rule uses body weight in pounds (lb):\n"
        f"Child Dose (mg) = [Weight (in lb) ÷ 150] × Adult Dose (mg)\n\n"
        f"If the standard adult dose is {adult_dose_mg} mg,\n"
        f"calculate the child dose for a child weighing {child_weight_lb} lb."
    )

    correct_ans = f"{_fmt(child_dose, 1)} mg"
    explanation = (
        f"1. Fraction = {child_weight_lb} ÷ 150 = {child_weight_lb / 150.0:.3f}.\n"
        f"2. Child dose = ({child_weight_lb} ÷ 150) × {adult_dose_mg} = {correct_ans}."
    )
    t1 = "Divide weight in pounds by 150, then multiply by the adult dose."
    t2 = f"({child_weight_lb} ÷ 150) × {adult_dose_mg} = {child_dose}."
    t3 = f"Child dose = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_42",
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
    """Subskill 43: Young's Rule: child dose based on age in years."""
    # Young's rule: Child dose = [Age / (Age + 12)] * Adult dose
    adult_dose_mg = r.choice([300, 400, 500, 600])
    child_age = r.choice([3, 4, 6, 8])

    fraction = child_age / (child_age + 12.0)
    child_dose = round(fraction * adult_dose_mg, 1)

    prompt = (
        f"Young's Rule calculates a child's dose for patients aged 1 to 12 years:\n"
        f"Child Dose (mg) = [Age (years) ÷ (Age (years) + 12)] × Adult Dose (mg)\n\n"
        f"An adult is prescribed {adult_dose_mg} mg of medication.\n"
        f"Calculate the dose for a {child_age}-year-old child in milligrams (mg)."
    )

    correct_ans = f"{_fmt(child_dose, 1)} mg"
    explanation = (
        f"1. Denominator = {child_age} + 12 = {child_age + 12}.\n"
        f"2. Fraction = {child_age} ÷ {child_age + 12} = {fraction:.4f}.\n"
        f"3. Child dose = {fraction:.4f} × {adult_dose_mg} mg = {correct_ans}."
    )
    t1 = "Add 12 to the child's age, divide the age by that total, and multiply by the adult dose."
    t2 = f"[{child_age} ÷ ({child_age} + 12)] × {adult_dose_mg}."
    t3 = f"Child dose = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_43",
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
    """Subskill 44: Fried's Rule: infant dose based on age in months."""
    # Fried's rule: Infant dose = (Age in months / 150) * Adult dose
    adult_dose_mg = r.choice([250, 300, 450, 600])
    infant_months = r.choice([5, 6, 8, 10])

    infant_dose = round((infant_months / 150.0) * adult_dose_mg, 1)

    prompt = (
        f"Fried's Rule is used to calculate medicine dosage for infants under 1 year of age:\n"
        f"Infant Dose (mg) = [Age (in months) ÷ 150] × Adult Dose (mg)\n\n"
        f"The adult dose of a decongestant is {adult_dose_mg} mg.\n"
        f"Calculate the safe infant dose for a {infant_months}-month-old baby in milligrams (mg)."
    )

    correct_ans = f"{_fmt(infant_dose, 1)} mg"
    explanation = (
        f"1. Fraction = {infant_months} ÷ 150 = {infant_months / 150.0:.4f}.\n"
        f"2. Infant dose = ({infant_months} ÷ 150) × {adult_dose_mg} = {correct_ans}."
    )
    t1 = "Divide the baby's age in months by 150, then multiply by the adult dose."
    t2 = f"({infant_months} ÷ 150) × {adult_dose_mg} = {infant_dose}."
    t3 = f"Infant dose = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_44",
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
    """Subskill 45: Body Surface Area (BSA) dosage calculation."""
    bsa_m2 = r.choice([0.65, 0.85, 1.15, 1.45])  # m²
    prescribed_rate_per_m2 = r.choice([150.0, 200.0, 250.0])  # mg/m²

    total_dose_mg = round(bsa_m2 * prescribed_rate_per_m2, 1)

    prompt = (
        f"In oncology and specialized pediatric medicine, drugs are dosed according to Body Surface Area (BSA):\n"
        f"Dosage (mg) = Patient BSA (in m²) × Prescribed Rate (mg/m²)\n\n"
        f"A young patient has a calculated BSA of {_fmt(bsa_m2, 2)} m² and is prescribed {_fmt(prescribed_rate_per_m2)} mg/m².\n"
        f"Calculate the total dose to administer in milligrams (mg)."
    )

    correct_ans = f"{_fmt(total_dose_mg, 1)} mg"
    explanation = (
        f"1. Dose = BSA × Rate = {_fmt(bsa_m2, 2)} m² × {_fmt(prescribed_rate_per_m2)} mg/m² = {correct_ans}."
    )
    t1 = "Multiply the patient's BSA in m² by the prescribed rate per m²."
    t2 = f"{bsa_m2} × {prescribed_rate_per_m2} = {total_dose_mg}."
    t3 = f"BSA dose = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_45",
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
    """Subskill 46: Comparing Young's Rule vs Clark's Rule: why weight-based dosing is medically superior."""
    prompt = (
        f"Modern pharmacologists and pediatricians strongly prefer weight-based dosing (such as Clark's Rule "
        f"or mg/kg) over age-based formulas (such as Young's Rule).\n\n"
        f"What is the critical clinical danger of calculating a child's medicine dosage using age alone?"
    )

    correct_ans = "Children of the exact same age vary widely in body weight, risking toxic overdose or ineffective underdose"
    explanation = (
        f"1. Children of the same age can have drastically different body masses (e.g. an 8-year-old child could weigh 18 kg or 35 kg).\n"
        f"2. Using age alone would give both children the exact same dose, which would overdose the lighter child or underdose the heavier child.\n"
        f"3. Weight-based dosing directly reflects metabolic clearance and circulating blood volume."
    )
    t1 = "Consider how children of the same age vary in weight."
    t2 = "Age does not account for differences in body mass, leading to dosing errors."
    t3 = f"Clinical rationale: {correct_ans}."

    custom_opts = [
        correct_ans,
        "Age-based formulas can only be calculated using Roman numerals",
        "Weight-based formulas require expensive electronic hospital equipment",
        "Young's Rule was outlawed because it was invented before 1900",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_46",
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
