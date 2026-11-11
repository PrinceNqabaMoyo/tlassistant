"""Subskills 25 to 32: Basal Metabolic Rate (BMR), Daily Caloric Deficits & Ideal Body Weight.
Covers BMR calculations for women and men, age-dependent metabolic decline,
Total Daily Energy Expenditure (TDEE) activity multipliers, caloric deficits for weight loss,
J.D. Robinson ideal weight formulas, and anatomical/racial limitations of ideal weight models.
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


def gen_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Subskill 25: Calculating BMR for a woman using the standard textbook formula."""
    name = r.choice(["Nomvula", "Fatima", "Lerato", "Amy"])
    age = r.choice([17, 24, 32, 45])
    weight_kg = r.choice([46.0, 58.0, 65.0, 72.0])
    height_cm = r.choice([143, 155, 162, 168])

    # Textbook formula from LB p. 183:
    # BMR (calories) = 10 * weight(kg) + 6.25 * height(cm) - 5 * age(years) - 161
    bmr = round(10 * weight_kg + 6.25 * height_cm - 5 * age - 161, 2)

    prompt = (
        f"{name} is a {age}-year-old woman weighing {_fmt(weight_kg)} kg and measuring {height_cm} cm tall.\n\n"
        f"The formula for a woman's Basal Metabolic Rate (BMR in calories) is:\n"
        f"BMR = 10 × Weight (in kg) + 6,25 × Height (in cm) − 5 × Age (in years) − 161\n\n"
        f"Calculate {name}'s daily BMR in calories."
    )

    correct_ans = f"{_fmt(bmr, 2)} calories"
    explanation = (
        f"1. Weight component = 10 × {_fmt(weight_kg)} = {_fmt(10 * weight_kg)}.\n"
        f"2. Height component = 6,25 × {height_cm} = {_fmt(6.25 * height_cm, 2)}.\n"
        f"3. Age component = 5 × {age} = {5 * age}.\n"
        f"4. BMR = {_fmt(10 * weight_kg)} + {_fmt(6.25 * height_cm, 2)} − {5 * age} − 161 = {correct_ans}."
    )
    t1 = "Substitute weight in kg, height in cm, and age into the equation."
    t2 = f"(10 × {weight_kg}) + (6,25 × {height_cm}) − (5 × {age}) − 161."
    t3 = f"BMR = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_25",
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


def gen_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Subskill 26: Calculating BMR for a man using the standard BMR formula."""
    name = r.choice(["Sipho", "Johan", "Thabo", "Pieter"])
    age = r.choice([20, 28, 35, 48])
    weight_kg = r.choice([68.0, 75.0, 84.0, 92.0])
    height_cm = r.choice([168, 175, 180, 185])

    # Men: BMR = 10 * weight(kg) + 6.25 * height(cm) - 5 * age + 5
    bmr = round(10 * weight_kg + 6.25 * height_cm - 5 * age + 5, 2)

    prompt = (
        f"{name} is a {age}-year-old man weighing {_fmt(weight_kg)} kg and standing {height_cm} cm tall.\n\n"
        f"The formula for a man's Basal Metabolic Rate (BMR in calories) is:\n"
        f"BMR = 10 × Weight (in kg) + 6,25 × Height (in cm) − 5 × Age (in years) + 5\n\n"
        f"Calculate {name}'s daily BMR in calories."
    )

    correct_ans = f"{_fmt(bmr, 2)} calories"
    explanation = (
        f"1. Weight component = 10 × {_fmt(weight_kg)} = {_fmt(10 * weight_kg)}.\n"
        f"2. Height component = 6,25 × {height_cm} = {_fmt(6.25 * height_cm, 2)}.\n"
        f"3. Age component = 5 × {age} = {5 * age}.\n"
        f"4. BMR = {_fmt(10 * weight_kg)} + {_fmt(6.25 * height_cm, 2)} − {5 * age} + 5 = {correct_ans}."
    )
    t1 = "Substitute weight, height, and age into the male BMR equation."
    t2 = f"(10 × {weight_kg}) + (6,25 × {height_cm}) − (5 × {age}) + 5."
    t3 = f"BMR = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_26",
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


def gen_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Subskill 27: Explaining the effect of aging on BMR."""
    prompt = (
        f"Consider the BMR formula: BMR = 10(Weight) + 6,25(Height) − 5(Age) − 161.\n"
        f"If a woman maintains her exact same weight and height as she ages from 20 to 50 years old,\n"
        f"will she require MORE calories or FEWER calories to maintain her basal metabolism, and why?"
    )

    correct_ans = "Fewer calories, because the '5 × Age' subtraction term increases as age increases"
    explanation = (
        f"1. The formula contains the term '− 5 × Age'.\n"
        f"2. As age increases from 20 to 50, '5 × Age' increases from 100 to 250 calories subtracted.\n"
        f"3. Therefore, the resulting BMR decreases, meaning fewer calories are required to maintain vital functions."
    )
    t1 = "Look at the sign in front of the age term: it is negative (− 5 × Age)."
    t2 = "Larger age means subtracting more calories, resulting in a lower BMR."
    t3 = f"Conclusion: {correct_ans}."

    custom_opts = [
        correct_ans,
        "More calories, because older adults require higher energy to digest food",
        "The exact same calories, because height and weight did not change",
        "Double the calories, because the body loses efficiency with time",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_27",
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


def gen_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Subskill 28: Total Daily Energy Expenditure (TDEE): BMR x physical activity multiplier."""
    name = r.choice(SA_NAMES)
    bmr = r.choice([1450, 1600, 1750, 1900])
    activity_levels = [
        ("Sedentary (desk job, little exercise)", 1.2),
        ("Lightly active (light exercise 1-3 days/week)", 1.375),
        ("Moderately active (moderate sports 3-5 days/week)", 1.55),
        ("Very active (hard sports 6-7 days/week)", 1.725),
    ]
    activity_desc, multiplier = r.choice(activity_levels)
    tdee = round(bmr * multiplier, 1)

    prompt = (
        f"{name}'s calculated Basal Metabolic Rate is {bmr} calories per day.\n"
        f"His physical lifestyle is classified as: {activity_desc}, which has an activity multiplier of {_fmt(multiplier, 3)}.\n\n"
        f"Formula: Total Daily Energy Expenditure (TDEE) = BMR × Activity Multiplier\n"
        f"Calculate {name}'s total daily caloric expenditure."
    )

    correct_ans = f"{_fmt(tdee, 1)} calories"
    explanation = (
        f"1. TDEE = BMR × Multiplier = {bmr} × {_fmt(multiplier, 3)} = {correct_ans}."
    )
    t1 = "Multiply the BMR by the given activity multiplier."
    t2 = f"{bmr} × {multiplier} = {tdee}."
    t3 = f"TDEE = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_28",
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


def gen_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Subskill 29: Daily caloric deficit calculation to lose 0.5 kg of body fat per week."""
    # 1 kg body fat = approx 7 700 kcal (or 0.5 kg = approx 3 500 kcal)
    # Daily deficit = 3 500 kcal / 7 days = 500 kcal/day
    tdee = r.choice([2200, 2400, 2600, 2800])
    daily_deficit = 500  # kcal to lose 0.5 kg/week
    daily_target_calories = tdee - daily_deficit

    prompt = (
        f"A nutritionist explains that burning 0,5 kg of stored body fat requires a cumulative "
        f"caloric deficit of 3 500 calories over a 7-day week.\n"
        f"A client's daily maintenance expenditure (TDEE) is {_fmt(tdee)} calories per day.\n\n"
        f"1. Calculate the required daily caloric deficit (3 500 calories ÷ 7 days).\n"
        f"2. Determine the maximum daily caloric intake the client should consume to lose 0,5 kg per week."
    )

    correct_ans = f"Deficit: {daily_deficit} cal/day -> Daily Intake: {_fmt(daily_target_calories)} calories"
    explanation = (
        f"1. Daily deficit = 3 500 calories ÷ 7 days = {daily_deficit} calories per day.\n"
        f"2. Daily caloric intake = Maintenance ({_fmt(tdee)}) − Deficit ({daily_deficit}) = {_fmt(daily_target_calories)} calories."
    )
    t1 = "Divide 3 500 by 7 to get the daily deficit, then subtract from TDEE."
    t2 = f"3 500 ÷ 7 = 500 cal. Daily intake = {tdee} - 500 = {daily_target_calories}."
    t3 = f"Caloric target: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Deficit: {daily_deficit} cal/day -> Daily Intake: {_fmt(tdee + daily_deficit)} calories",
        f"Deficit: 700 cal/day -> Daily Intake: {_fmt(tdee - 700)} calories",
        f"Deficit: 250 cal/day -> Daily Intake: {_fmt(tdee - 250)} calories",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_29",
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


def gen_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Subskill 30: Ideal body weight using the J.D. Robinson formula for women."""
    name = r.choice(SA_NAMES)
    height_cm = r.choice([155, 160, 165, 170, 175])

    # Formula for women: Ideal Weight = 49 kg + 0.7 kg * (Height in cm - 150)
    ideal_kg = round(49.0 + 0.7 * (height_cm - 150), 2)

    prompt = (
        f"The J.D. Robinson formula calculates a woman's ideal body weight based on height:\n"
        f"Ideal Weight (kg) = 49 kg + 0,7 kg × [Height (in cm) − 150]\n\n"
        f"Calculate the ideal body weight for a woman named {name} who is {height_cm} cm tall (to 2 decimal places)."
    )

    correct_ans = f"{_fmt(ideal_kg, 2)} kg"
    explanation = (
        f"1. Subtract 150 from height: {height_cm} − 150 = {height_cm - 150} cm.\n"
        f"2. Multiply by 0,7: 0,7 × {height_cm - 150} = {_fmt(0.7 * (height_cm - 150), 2)} kg.\n"
        f"3. Add 49 kg: 49 + {_fmt(0.7 * (height_cm - 150), 2)} = {correct_ans}."
    )
    t1 = "Subtract 150 from height in cm, multiply the difference by 0,7, then add 49."
    t2 = f"49 + 0,7 × ({height_cm} - 150) = 49 + {round(0.7 * (height_cm - 150), 2)}."
    t3 = f"Ideal weight = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_30",
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


def gen_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Subskill 31: Ideal body weight using the J.D. Robinson formula for men."""
    name = r.choice(SA_NAMES)
    height_cm = r.choice([165, 172, 178, 185])

    # Formula for men: Ideal Weight = 52 kg + 0.9 kg * (Height in cm - 150)
    ideal_kg = round(52.0 + 0.9 * (height_cm - 150), 2)

    prompt = (
        f"The J.D. Robinson formula for a man's ideal body weight is:\n"
        f"Ideal Weight (kg) = 52 kg + 0,9 kg × [Height (in cm) − 150]\n\n"
        f"Calculate the ideal body weight for an adult man who is {height_cm} cm tall (to 2 decimal places)."
    )

    correct_ans = f"{_fmt(ideal_kg, 2)} kg"
    explanation = (
        f"1. Height difference: {height_cm} − 150 = {height_cm - 150} cm.\n"
        f"2. Multiply by 0,9: 0,9 × {height_cm - 150} = {_fmt(0.9 * (height_cm - 150), 2)} kg.\n"
        f"3. Add 52 kg: 52 + {_fmt(0.9 * (height_cm - 150), 2)} = {correct_ans}."
    )
    t1 = "Subtract 150 from height in cm, multiply by 0,9, then add 52."
    t2 = f"52 + 0,9 × ({height_cm} - 150) = 52 + {round(0.9 * (height_cm - 150), 2)}."
    t3 = f"Ideal weight = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_bmi_subskill_31",
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


def gen_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Subskill 32: Analyzing biological factors that limit ideal weight formulas."""
    prompt = (
        f"Mathematical formulas like Robinson's Ideal Body Weight predict an exact single number "
        f"of kilograms for any given height.\n\n"
        f"Which TWO anatomical and biological factors cause such formulas to be medically inaccurate for many individuals?"
    )

    correct_ans = "Differences in skeletal bone frame size (small vs large-boned) and muscular development"
    explanation = (
        f"1. Ideal weight formulas assume an average skeletal frame and body composition.\n"
        f"2. Individuals with large, broad skeletal bone structures naturally carry more weight healthily.\n"
        f"3. Furthermore, individuals with high muscle mass (such as manual workers or athletes) will naturally weigh more than the formula predicts without being unhealthy."
    )
    t1 = "Consider what makes people physically distinct: bone structure and muscle ratio."
    t2 = "Frame size and muscle mass are not accounted for in simple height formulas."
    t3 = f"Key factors: {correct_ans}."

    custom_opts = [
        correct_ans,
        "The person's shoe size and blood pressure level",
        "Whether the person eats white bread or brown bread",
        "The altitude of the city where the person resides",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_bmi_subskill_32",
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
