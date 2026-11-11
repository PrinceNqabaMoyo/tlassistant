"""Subskills 01 to 08: Adult Body Mass Index (BMI) Mechanics, WHO Cut-Offs & Reverse Targets.
Covers basic BMI calculations, metric unit conversions (cm to m), WHO adult weight status classifications,
imperial conversions (pounds to kg, inches to cm), reverse BMI threshold solving,
target weight-loss and weight-gain regimens, and physiological limitations of BMI in athletes.
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


def gen_subskill_01(r: random.Random) -> Dict[str, Any]:
    """Subskill 01: Adult BMI calculation from weight (kg) and height (m)."""
    name = r.choice(SA_NAMES)
    weight_kg = r.choice([58.0, 64.0, 72.0, 81.0, 88.0])
    height_m = r.choice([1.62, 1.68, 1.74, 1.80])

    bmi = round(weight_kg / (height_m ** 2), 2)

    prompt = (
        f"{name} is an adult measuring {_fmt(height_m)} m tall and weighing {_fmt(weight_kg)} kg.\n\n"
        f"Formula: BMI = Weight (kg) ÷ [Height (m)]²\n"
        f"Calculate {name}'s Body Mass Index (BMI) in kg/m² (to 2 decimal places)."
    )

    correct_ans = f"{_fmt(bmi, 2)} kg/m²"
    explanation = (
        f"1. Formula: BMI = {_fmt(weight_kg)} ÷ ({_fmt(height_m)})².\n"
        f"2. Height squared = ({_fmt(height_m)})² = {_fmt(height_m ** 2, 4)} m².\n"
        f"3. BMI = {_fmt(weight_kg)} ÷ {_fmt(height_m ** 2, 4)} = {correct_ans}."
    )
    t1 = "Square the height first, then divide weight by that number."
    t2 = f"{weight_kg} ÷ ({height_m} × {height_m}) = {weight_kg} ÷ {round(height_m**2, 4)}."
    t3 = f"BMI = {correct_ans}."

    # Misconceptions: forgetting to square height (weight / height)
    wrong_unsquared = round(weight_kg / height_m, 2)
    custom_opts = [
        correct_ans,
        f"{_fmt(wrong_unsquared, 2)} kg/m²",
        f"{_fmt(bmi + 3.5, 2)} kg/m²",
        f"{_fmt(bmi - 3.5, 2)} kg/m²",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_01",
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


def gen_subskill_02(r: random.Random) -> Dict[str, Any]:
    """Subskill 02: Adult BMI calculation requiring cm to m height conversion."""
    name = r.choice(SA_NAMES)
    weight_kg = r.choice([55.0, 68.0, 75.0, 84.0])
    height_cm = r.choice([155, 164, 172, 178])
    height_m = height_cm / 100.0

    bmi = round(weight_kg / (height_m ** 2), 2)

    prompt = (
        f"{name} has a recorded body weight of {_fmt(weight_kg)} kg and a height of {height_cm} cm.\n\n"
        f"Given that 1 m = 100 cm and BMI = Weight (kg) ÷ [Height (m)]²:\n"
        f"1. Convert {name}'s height to metres (m).\n"
        f"2. Calculate {name}'s BMI in kg/m² (to 2 decimal places)."
    )

    correct_ans = f"{_fmt(height_m, 2)} m -> {_fmt(bmi, 2)} kg/m²"
    explanation = (
        f"1. Height in metres = {height_cm} cm ÷ 100 = {_fmt(height_m, 2)} m.\n"
        f"2. Height squared = ({_fmt(height_m, 2)})² = {_fmt(height_m ** 2, 4)} m².\n"
        f"3. BMI = {_fmt(weight_kg)} ÷ {_fmt(height_m ** 2, 4)} = {_fmt(bmi, 2)} kg/m²."
    )
    t1 = "Divide the height in cm by 100 to convert to metres, then calculate Weight ÷ (Height in m)²."
    t2 = f"Height = {_fmt(height_m, 2)} m. BMI = {weight_kg} ÷ ({height_m})²."
    t3 = f"Result: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(height_m, 2)} m -> {_fmt(weight_kg / height_m, 2)} kg/m²",
        f"{_fmt(height_m, 2)} m -> {_fmt(bmi + 4.2, 2)} kg/m²",
        f"{_fmt(height_m, 2)} m -> {_fmt(bmi * 10, 2)} kg/m²",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_02",
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


def gen_subskill_03(r: random.Random) -> Dict[str, Any]:
    """Subskill 03: Adult WHO BMI classification: Underweight, Normal, Overweight, Obese."""
    cases = [
        (48.0, 1.70, 16.61, "Underweight (< 18,5)"),
        (65.0, 1.70, 22.49, "Normal / Healthy (18,5 - 24,9)"),
        (82.0, 1.70, 28.37, "Overweight (25,0 - 29,9)"),
        (98.0, 1.70, 33.91, "Obese (≥ 30,0)"),
    ]
    w, h, b, status = r.choice(cases)

    table_data = {
        "headers": ["BMI Range", "WHO Weight Status Classification"],
        "rows": [
            ["Less than 18,5", "Underweight"],
            ["18,5 to 24,9", "Normal / Healthy Weight"],
            ["25,0 to 29,9", "Overweight"],
            ["30,0 and upwards", "Obese"],
        ]
    }

    prompt = (
        f"An adult patient weighs {_fmt(w)} kg and is {_fmt(h)} m tall.\n"
        f"His calculated BMI is {_fmt(b, 2)} kg/m².\n\n"
        f"Refer to the World Health Organization (WHO) Adult BMI Table below.\n"
        f"Classify the patient's weight status according to this standard."
    )

    correct_ans = status
    explanation = (
        f"1. Calculated BMI = {_fmt(b, 2)} kg/m².\n"
        f"2. In the table, this value falls into the category: {correct_ans}."
    )
    t1 = "Find the row where the BMI value fits between the upper and lower limits."
    t2 = f"BMI {_fmt(b, 2)} matches {status}."
    t3 = f"Weight status = {correct_ans}."

    all_statuses = [
        "Underweight (< 18,5)",
        "Normal / Healthy (18,5 - 24,9)",
        "Overweight (25,0 - 29,9)",
        "Obese (≥ 30,0)"
    ]
    custom_opts = [correct_ans] + [s for s in all_statuses if s != correct_ans]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_03",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        table_data=table_data,
        difficulty="easy",
    )


def gen_subskill_04(r: random.Random) -> Dict[str, Any]:
    """Subskill 04: Imperial units BMI conversion: Weight in pounds (lb) and height in inches."""
    pounds = r.choice([122, 140, 165, 185])
    inches = r.choice([66, 68, 70, 72])

    # Convert lb to kg: lb / 2.2
    kg = round(pounds / 2.2, 2)
    # Convert inches to cm: inches * 2.54; cm to m: / 100
    m = round((inches * 2.54) / 100.0, 3)
    bmi = round(kg / (m ** 2), 2)

    prompt = (
        f"A medical assessment form lists a patient's measurements in imperial units:\n"
        f"• Weight: {pounds} lb\n"
        f"• Height: {inches} inches\n\n"
        f"Conversions: 1 kg = 2,2 lb; 1 inch = 2,54 cm; 100 cm = 1 m.\n"
        f"1. Convert the weight to kilograms (kg).\n"
        f"2. Convert the height to metres (m).\n"
        f"3. Calculate the patient's BMI in kg/m² (to 2 decimal places)."
    )

    correct_ans = f"{_fmt(kg, 2)} kg, {_fmt(m, 3)} m -> {_fmt(bmi, 2)} kg/m²"
    explanation = (
        f"1. Weight in kg = {pounds} lb ÷ 2,2 = {_fmt(kg, 2)} kg.\n"
        f"2. Height in cm = {inches} × 2,54 = {_fmt(inches * 2.54, 2)} cm = {_fmt(m, 3)} m.\n"
        f"3. BMI = {_fmt(kg, 2)} ÷ ({_fmt(m, 3)})² = {correct_ans}."
    )
    t1 = "Divide pounds by 2,2 for kg, multiply inches by 2,54 and divide by 100 for metres, then calculate BMI."
    t2 = f"Weight = {kg} kg. Height = {m} m. BMI = {kg} ÷ ({m})²."
    t3 = f"Results: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"{_fmt(kg, 2)} kg, {_fmt(m, 3)} m -> {_fmt(round(kg / m, 2))} kg/m²",
        f"{_fmt(pounds * 2.2, 2)} kg, {_fmt(m, 3)} m -> {_fmt(round((pounds * 2.2) / (m**2), 2))} kg/m²",
        f"{_fmt(kg, 2)} kg, {_fmt(m, 3)} m -> {_fmt(bmi + 5.0, 2)} kg/m²",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_04",
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


def gen_subskill_05(r: random.Random) -> Dict[str, Any]:
    """Subskill 05: Reverse BMI: Finding weight threshold for obesity (BMI = 30) for a given height."""
    height_m = r.choice([1.65, 1.72, 1.78, 1.82])
    target_bmi = 30.0  # Obesity threshold

    # Weight = BMI * (height^2)
    h_sq = height_m ** 2
    weight_threshold = round(target_bmi * h_sq, 1)

    prompt = (
        f"According to WHO standards, an adult is classified as obese if their BMI is 30,0 kg/m² or higher.\n"
        f"A man stands {_fmt(height_m)} m tall.\n\n"
        f"Formula: Minimum Obese Weight (kg) = 30 × [Height (m)]²\n"
        f"Calculate the minimum body weight (in kg) at which this man would be considered obese (to 1 decimal place)."
    )

    correct_ans = f"{_fmt(weight_threshold, 1)} kg"
    explanation = (
        f"1. Formula: Weight = BMI × (Height)².\n"
        f"2. Substitution: Weight = 30 × ({_fmt(height_m)})² = 30 × {_fmt(h_sq, 4)} = {correct_ans}."
    )
    t1 = "Square the height in metres, then multiply by the threshold BMI of 30."
    t2 = f"Calculation: 30 × ({height_m} × {height_m}) = 30 × {round(h_sq, 4)}."
    t3 = f"Weight threshold = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_05",
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


def gen_subskill_06(r: random.Random) -> Dict[str, Any]:
    """Subskill 06: Target weight loss: calculating kg needed to move from overweight (BMI = 28) to normal (BMI = 24)."""
    name = r.choice(SA_NAMES)
    height_m = r.choice([1.65, 1.70, 1.75, 1.80])
    h_sq = height_m ** 2

    current_bmi = 28.5
    target_bmi = 24.0

    current_weight = round(current_bmi * h_sq, 1)
    target_weight = round(target_bmi * h_sq, 1)
    loss_needed = round(current_weight - target_weight, 1)

    prompt = (
        f"{name} is {_fmt(height_m)} m tall and currently weighs {_fmt(current_weight, 1)} kg (BMI = {_fmt(current_bmi, 1)} kg/m², overweight).\n"
        f"Her dietitian sets a goal for her to reach a healthy normal BMI of {_fmt(target_bmi, 1)} kg/m².\n\n"
        f"1. Calculate the target weight corresponding to a BMI of {_fmt(target_bmi, 1)} kg/m².\n"
        f"2. Determine the total weight loss (in kg) {name} must achieve."
    )

    correct_ans = f"Target: {_fmt(target_weight, 1)} kg (Loss: {_fmt(loss_needed, 1)} kg)"
    explanation = (
        f"1. Target Weight = Target BMI × (Height)² = {_fmt(target_bmi, 1)} × {_fmt(h_sq, 4)} = {_fmt(target_weight, 1)} kg.\n"
        f"2. Weight Loss Required = {_fmt(current_weight, 1)} kg − {_fmt(target_weight, 1)} kg = {loss_needed} kg."
    )
    t1 = "Multiply target BMI by height squared to find target weight, then subtract target weight from current weight."
    t2 = f"Target = {target_bmi} × {round(h_sq, 4)} = {_fmt(target_weight, 1)} kg. Loss = {_fmt(loss_needed, 1)} kg."
    t3 = f"Weight goal: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Target: {_fmt(target_weight, 1)} kg (Loss: {_fmt(loss_needed + 5, 1)} kg)",
        f"Target: {_fmt(target_weight - 5, 1)} kg (Loss: {_fmt(loss_needed, 1)} kg)",
        f"Target: {_fmt(target_weight, 1)} kg (Loss: {_fmt(current_bmi - target_bmi, 1)} kg)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_06",
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


def gen_subskill_07(r: random.Random) -> Dict[str, Any]:
    """Subskill 07: Weight gain target: calculating kg needed to move from underweight (< 18.5) to healthy (20.0)."""
    name = r.choice(SA_NAMES)
    height_m = r.choice([1.70, 1.75, 1.80])
    h_sq = height_m ** 2

    current_bmi = 16.5  # severely underweight
    target_bmi = 20.0   # solid normal weight

    current_weight = round(current_bmi * h_sq, 1)
    target_weight = round(target_bmi * h_sq, 1)
    gain_needed = round(target_weight - current_weight, 1)

    prompt = (
        f"A patient recovering from illness weighs {_fmt(current_weight, 1)} kg and stands {_fmt(height_m)} m tall "
        f"(BMI = {_fmt(current_bmi, 1)} kg/m², underweight).\n"
        f"His physician advises him to gain weight to reach a healthy baseline BMI of {_fmt(target_bmi, 1)} kg/m².\n\n"
        f"Calculate the patient's target healthy weight (in kg) and the weight gain required (in kg)."
    )

    correct_ans = f"Target: {_fmt(target_weight, 1)} kg (Gain: +{_fmt(gain_needed, 1)} kg)"
    explanation = (
        f"1. Target Weight = {_fmt(target_bmi, 1)} × ({_fmt(height_m)})² = {_fmt(target_bmi, 1)} × {_fmt(h_sq, 4)} = {_fmt(target_weight, 1)} kg.\n"
        f"2. Weight Gain = {_fmt(target_weight, 1)} kg − {_fmt(current_weight, 1)} kg = +{_fmt(gain_needed, 1)} kg."
    )
    t1 = "Calculate target weight (BMI × height²), then subtract current weight from target weight."
    t2 = f"Target = {target_bmi} × {round(h_sq, 4)} = {_fmt(target_weight, 1)} kg. Gain = +{_fmt(gain_needed, 1)} kg."
    t3 = f"Gain plan: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Target: {_fmt(target_weight, 1)} kg (Gain: +{_fmt(gain_needed + 4, 1)} kg)",
        f"Target: {_fmt(target_weight - 3, 1)} kg (Gain: +{_fmt(gain_needed - 3, 1)} kg)",
        f"Target: {_fmt(target_weight, 1)} kg (Gain: +{_fmt(target_bmi - current_bmi, 1)} kg)",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_07",
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


def gen_subskill_08(r: random.Random) -> Dict[str, Any]:
    """Subskill 08: Limitations of BMI in muscular athletes and elderly populations."""
    prompt = (
        f"A professional South African rugby prop forward weighs 112 kg and is 1,84 m tall.\n"
        f"His calculated BMI is 33,08 kg/m², which classifies him as 'Obese' according to WHO tables.\n"
        f"However, medical testing shows that his body fat percentage is only 12% (extremely lean and athletic).\n\n"
        f"What is the primary scientific reason why the standard BMI formula misclassifies this athlete?"
    )

    correct_ans = "BMI cannot distinguish between heavy dense muscle mass and adipose fatty tissue"
    explanation = (
        f"1. The standard BMI formula only uses total body weight and height.\n"
        f"2. Muscle tissue is much denser and heavier than fat tissue.\n"
        f"3. Highly trained athletes have high muscle mass, giving them high body weight and high BMI without excess body fat."
    )
    t1 = "Consider what BMI measures: it only looks at total weight, not body composition."
    t2 = "Muscle weighs more than fat, but BMI cannot differentiate between muscle and fat."
    t3 = f"Primary limitation: {correct_ans}."

    custom_opts = [
        correct_ans,
        "The athlete's height was measured incorrectly in centimetres instead of metres",
        "BMI only applies to female patients and is invalid for all males",
        "The rugby player should be classified as underweight because he exercises daily",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_08",
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
