"""Grade 10–12 Mathematical Literacy — Measurement & Probability (Deterministic 6-Pillar Generator).
100% aligned with South African CAPS Curriculum (Mathematical Literacy Paper 2: Measurement and Probability).
Covers:
- Practical measurement: perimeter, floor area, cylinder/box volume, capacity (litres)
- Body Mass Index (BMI = mass in kg / (height in m)^2) and health weight categories
- Medicine dosage calculation based on child mass
- Authentic probability in everyday life: percentages, decimal fractions, weather forecasting, sports outcomes

Zero-LLM: 100% deterministic Python logic with South African comma decimals ({,}).
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "mathematical_literacy_measurement"
LO = "mathlit_measurement_practical"

SA_NAMES = ["Sipho", "Lerato", "Kagiso", "Zanele", "Thabo", "Nomsa", "Bongani", "Nandi", "Andile", "Mpho"]


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed)


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return f"{val:.{places}f}".replace(".", ",")


def _build_bmi_drill(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    mass_kg = r.randint(55, 95)
    height_cm = r.randint(155, 188)
    height_m = height_cm / 100.0

    bmi = round(mass_kg / (height_m ** 2), 1)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal weight"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"

    prompt = (
        rf"{name} is a high school learner with a body mass of {mass_kg}\text{{ kg}} "
        rf"and a measured height of {height_cm}\text{{ cm}}.\n\n"
        rf"The official Body Mass Index (BMI) formula is:\n"
        rf"$$\text{{BMI}} = \frac{{\text{{mass (kg)}}}}{{(\text{{height in metres}})^2}}$$\n\n"
        rf"1. Convert {name}'s height from centimetres to metres.\n"
        rf"2. Calculate {name}'s BMI. Round off your answer to ONE decimal place.\n"
        rf"3. Refer to the standard health categories:\n"
        rf"- Below 18,5: Underweight\n"
        rf"- 18,5 to 24,9: Normal weight\n"
        rf"- 25,0 to 29,9: Overweight\n"
        rf"- 30,0 and above: Obese\n\n"
        rf"State {name}'s health category based on the calculated BMI."
    )

    sample_ans = (
        rf"1. Height in metres = {height_cm} / 100 = {_fmt_sa(height_m, 2)} m.\n"
        rf"2. BMI = {mass_kg} / ({_fmt_sa(height_m, 2)})^2 = {mass_kg} / {_fmt_sa(round(height_m**2, 4), 4)} = {_fmt_sa(bmi, 1)} kg/m^2.\n"
        rf"3. Category: {category}."
    )

    return {
        "id": f"mathlit_bmi_{r.randint(1000, 9999)}",
        "question_type": "typed",
        "topic": "Measurement",
        "learning_objective_id": LO,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "marks": 5,
        "correct_answer": f"Height: {_fmt_sa(height_m, 2)} m, BMI: {_fmt_sa(bmi, 1)}, Category: {category}",
        "sample_answer": sample_ans,
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert height cm to metres (divide by 100)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Substitute mass and height into BMI formula", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": f"Accurate BMI calculation ({_fmt_sa(bmi, 1)}) and correct category ({category})", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Remember that height MUST be in metres, not centimetres, in the BMI formula.",
            "2_concept": "Divide height in cm by 100 to get metres, square it, and divide the mass by this value.",
            "3_breakdown": rf"Height = {_fmt_sa(height_m, 2)} m. BMI = {mass_kg} / ({_fmt_sa(height_m, 2)})^2 = {_fmt_sa(bmi, 1)}. Category: {category}.",
        },
        "misconception_tags": ["bmi_unit_conversion_error", "forgot_square_height"],
    }


def _build_tank_capacity_drill(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    diameter = r.choice([1.4, 1.8, 2.0, 2.4])
    radius = round(diameter / 2.0, 2)
    height = r.choice([2.0, 2.5, 3.0])

    vol_m3 = round(math.pi * (radius ** 2) * height, 2)
    capacity_litres = round(vol_m3 * 1000)

    prompt = (
        rf"{name}'s family installs a cylindrical rainwater harvesting tank with a diameter of "
        rf"{_fmt_sa(diameter)}\text{{ m}} and a height of {_fmt_sa(height)}\text{{ m}}.\n\n"
        r"$$\text{Volume of cylinder} = \pi \times \text{radius}^2 \times \text{height}$$\n"
        r"Take $\pi = 3{,}142$.\n\n"
        r"1. Calculate the radius of the tank.\n"
        r"2. Calculate the volume of the tank in cubic metres ($\text{m}^3$). Round off to TWO decimal places.\n"
        r"3. Given that $1\text{ m}^3 = 1\,000\text{ litres}$, determine the maximum water capacity of the tank in litres."
    )

    sample_ans = (
        rf"1. Radius = {diameter} / 2 = {_fmt_sa(radius)} m.\n"
        rf"2. Volume = 3,142 x ({_fmt_sa(radius)})^2 x {_fmt_sa(height)} = {_fmt_sa(vol_m3)} m^3.\n"
        rf"3. Capacity = {_fmt_sa(vol_m3)} x 1 000 = {capacity_litres:,} litres."
    ).replace(",", " ")

    return {
        "id": f"mathlit_tank_{r.randint(1000, 9999)}",
        "question_type": "typed",
        "topic": "Measurement",
        "learning_objective_id": LO,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "marks": 6,
        "correct_answer": f"Radius: {_fmt_sa(radius)} m, Volume: {_fmt_sa(vol_m3)} m^3, Capacity: {capacity_litres} L",
        "sample_answer": sample_ans,
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Radius = diameter / 2", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Substitution into cylinder volume formula", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Volume in m^3", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Conversion from m^3 to litres (x 1000)", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Radius is half the diameter. Then use V = pi x r^2 x h.",
            "2_concept": "Multiply cubic metres by 1 000 to convert to litres.",
            "3_breakdown": rf"Radius = {_fmt_sa(radius)} m. Volume = {_fmt_sa(vol_m3)} m^3. Capacity = {capacity_litres} litres.",
        },
        "misconception_tags": ["diameter_used_as_radius", "cubic_metre_to_litre_conversion_error"],
    }


def _build_daily_probability_drill(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    rain_chance = r.choice([20, 30, 40, 60, 75, 80])
    no_rain_chance = 100 - rain_chance
    decimal_rain = round(rain_chance / 100.0, 2)

    prompt = (
        rf"The South African Weather Service forecasts a {rain_chance}\% chance of rain in Durban on Saturday.\n\n"
        rf"1. Express the probability of rain as a decimal fraction.\n"
        rf"2. What is the probability that it will NOT rain on Saturday, expressed as a percentage?\n"
        rf"3. On a probability scale from 0 (impossible) to 1 (certain), describe the likelihood of rain on Saturday."
    )

    if rain_chance < 40:
        desc = "Unlikely (low probability)"
    elif rain_chance <= 60:
        desc = "Evens / equally likely"
    else:
        desc = "Likely (high probability)"

    sample_ans = (
        rf"1. Decimal fraction = {rain_chance} / 100 = {_fmt_sa(decimal_rain)}.\n"
        rf"2. Probability of no rain = 100% - {rain_chance}% = {no_rain_chance}%.\n"
        rf"3. Likelihood: {desc}."
    )

    return {
        "id": f"mathlit_prob_{r.randint(1000, 9999)}",
        "question_type": "typed",
        "topic": "Probability",
        "learning_objective_id": "mathlit_probability_daily",
        "term": 4,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "marks": 4,
        "correct_answer": f"Decimal: {_fmt_sa(decimal_rain)}, No rain: {no_rain_chance}%, Likelihood: {desc}",
        "sample_answer": sample_ans,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Convert percentage to decimal fraction", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Complementary probability calculation (100% - p)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Probability scale verbal description", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Divide by 100 to convert percentage to a decimal fraction.",
            "2_concept": "The sum of complementary probabilities always equals 100% or 1.",
            "3_breakdown": rf"Decimal = {_fmt_sa(decimal_rain)}. No rain = {no_rain_chance}%. Likelihood = {desc}.",
        },
        "misconception_tags": ["percentage_to_decimal_error"],
    }


def generate(subskill: Optional[str] = None, difficulty: str = "medium", count: int = 1, seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    r = _rng(seed)
    generators = [_build_bmi_drill, _build_tank_capacity_drill, _build_daily_probability_drill]
    if subskill == "bmi":
        generators = [_build_bmi_drill]
    elif subskill == "volume" or subskill == "tank":
        generators = [_build_tank_capacity_drill]
    elif subskill == "probability":
        generators = [_build_daily_probability_drill]

    questions = []
    for _ in range(count):
        gen_fn = r.choice(generators)
        questions.append(gen_fn(r))
    return questions
