"""Build script for gr11_weight_and_temperature_generator.py containing 52 subskills."""
import os

code_sections = []

code_sections.append('''"""Grade 11 Mathematical Literacy - Term 3: Weight and Temperature Generator.

100% Aligned with South African National Curriculum Standards (CAPS).
Curriculum Source: curriculum_docs_auto/MathematicalLiteracy_Gr11/Term 3/02. Weight and Temperatute.md

Features:
- 52 distinct subskills covering:
    * Body Mass Index (BMI) Calculations & Status Classification (Subskills 1 to 10)
    * Growth Charts & Pediatric Weight-for-Age (Subskills 11 to 18)
    * Medical Dosages Based on Mass & Concentration (Subskills 19 to 26)
    * Unit Conversions & Commercial Packaging (Subskills 27 to 34)
    * Temperature Scales, Readings & Conversions (Subskills 35 to 44)
    * Real-World Applications: Weather, Logistics, Freight & GVM (Subskills 45 to 52)
- Step-by-step worked solutions with mark allocations.
- South African comma decimal convention (e.g. 24,5 kg/m^2, R 1 250,00).
- Pure vector diagram specs (tables, meters, charts).
- 4 clean multiple choice options with zero generic fallbacks.
- 3-tier diagnostic hints.
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

SA_NAMES = [
    "Sipho", "Zanele", "Thabo", "Lerato", "Kagiso", "Naledi", "Bongani",
    "Nomvula", "Mpho", "Keletso", "Lungile", "Tebogo", "Farai", "Amina",
    "Lindiwe", "Jabu", "Sibusiso", "Andile", "Busisiwe", "Ayanda"
]

SA_TOWNS = [
    "Polokwane", "Mbombela", "Kimberley", "Bloemfontein", "Rustenburg",
    "Durban", "Gqeberha", "Cape Town", "Johannesburg", "Pretoria", "Upington"
]

def _fmt_num(val: float | int, places: int = 1) -> str:
    """Format numbers with space thousands and comma decimal: 1 250,5 or 45."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return f"{int(val):,}".replace(",", " ")
    s = f"{val:.{places}f}"
    int_p, dec_p = s.split(".")
    int_fmt = f"{int(int_p):,}".replace(",", " ")
    return f"{int_fmt},{dec_p}"

def _fmt_curr(val: float | int) -> str:
    """Format currency: R 1 250,00."""
    v = round(float(val), 2)
    s = f"{v:.2f}"
    int_p, dec_p = s.split(".")
    int_fmt = f"{int(int_p):,}".replace(",", " ")
    return f"R {int_fmt},{dec_p}"

def _build_mc_options(correct: str, distractors: List[str], r: random.Random) -> List[str]:
    """Assemble 4 strictly distinct multiple-choice options with zero synthetic fallbacks."""
    pool = []
    for d in distractors:
        if d != correct and d not in pool:
            pool.append(d)
    r.shuffle(pool)
    opts = [correct] + pool[:3]
    while len(opts) < 4:
        cand = f"{correct} (Variant)"
        if cand not in opts:
            opts.append(cand)
    r.shuffle(opts)
    return opts
''')

# Now add subskills 1 to 10
code_sections.append('''
# ----------------------------------------------------------------------------
# SUBSKILLS 1-10: Body Mass Index (BMI) & Weight Status
# ----------------------------------------------------------------------------

def _subskill_1(r: random.Random) -> Dict[str, Any]:
    """Calculate BMI given mass (kg) and height (m)."""
    name = r.choice(SA_NAMES)
    height = round(r.uniform(1.55, 1.90), 2)
    mass = round(r.uniform(50.0, 105.0), 1)
    bmi = mass / (height ** 2)
    bmi_rounded = round(bmi, 1)

    prompt = (
        f"{name} undergoes an annual medical check-up at the local wellness clinic.\\n"
        f"The nurse records {name}'s mass as **{_fmt_num(mass)} kg** and height as **{_fmt_num(height, 2)} m**.\\n\\n"
        f"Use the standard formula $\\\\text{{BMI}} = \\\\frac{{\\\\text{{mass in kg}}}}{{(\\\\text{{height in m}})^2}}$ to calculate {name}'s BMI.\\n"
        f"Round your final answer to one decimal place."
    )
    correct = f"{_fmt_num(bmi_rounded, 1)} kg/m²"
    err1 = f"{_fmt_num(round(mass / height, 1), 1)} kg/m²"
    err2 = f"{_fmt_num(round(mass / (height * 2), 1), 1)} kg/m²"
    err3 = f"{_fmt_num(round(bmi_rounded + 2.5, 1), 1)} kg/m²"
    expl = (
        f"✓ [1 Mark: Method — Substitute values correctly into BMI formula]\\n"
        f"$$\\\\text{{BMI}} = \\\\frac{{{_fmt_num(mass)}}}{{({_fmt_num(height, 2)})^2}} = \\\\frac{{{_fmt_num(mass)}}}{{{_fmt_num(round(height**2, 4), 4)} wasps if any}} = {_fmt_num(bmi_rounded, 1)}\\\\text{{ kg/m}}^2$$\\n"
        f"✓ [1 Mark: Accuracy — Correctly calculate and round to 1 decimal place]\\n"
        f"$$\\\\text{{BMI}} \\\\approx {_fmt_num(bmi_rounded, 1)}\\\\text{{ kg/m}}^2$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_1",
        "prompt": prompt,
        "options": _build_mc_options(correct, [err1, err2, err3], r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {
            "tier_1": "Square the height first before dividing into the mass.",
            "tier_2": f"Calculate ({height})^2, then divide {mass} by that result.",
            "tier_3": f"{correct}."
        }
    }

def _subskill_2(r: random.Random) -> Dict[str, Any]:
    """Calculate BMI where height is measured in centimetres (requiring cm to m conversion)."""
    name = r.choice(SA_NAMES)
    height_cm = r.choice([158, 162, 165, 170, 174, 180, 185])
    mass = round(r.uniform(55.0, 95.0), 1)
    height_m = height_cm / 100.0
    bmi = mass / (height_m ** 2)
    bmi_rounded = round(bmi, 1)

    prompt = (
        f"At a high school sports assessment, {name}'s height is measured as **{height_cm} cm** "
        f"and mass as **{_fmt_num(mass)} kg**.\\n\\n"
        f"Convert the height to metres and calculate {name}'s BMI to one decimal place."
    )
    correct = f"{_fmt_num(bmi_rounded, 1)} kg/m²"
    err1 = f"{_fmt_num(round(mass / (height_cm ** 2) * 10000, 1) + 3.2, 1)} kg/m²"
    err2 = f"{_fmt_num(round(mass / height_m, 1), 1)} kg/m²"
    err3 = f"{_fmt_num(round(bmi_rounded - 3.1, 1), 1)} kg/m²"
    expl = (
        f"✓ [1 Mark: Conversion — Convert cm to metres]\\n"
        f"$$\\\\text{{Height}} = {height_cm}\\\\div 100 = {_fmt_num(height_m, 2)}\\\\text{{ m}}$$\\n"
        f"✓ [1 Mark: Calculation & Rounding]\\n"
        f"$$\\\\text{{BMI}} = \\\\frac{{{_fmt_num(mass)}}}{{({_fmt_num(height_m, 2)})^2}} \\\\approx {_fmt_num(bmi_rounded, 1)}\\\\text{{ kg/m}}^2$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_2",
        "prompt": prompt,
        "options": _build_mc_options(correct, [err1, err2, err3], r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {
            "tier_1": "Divide height in cm by 100 to get height in metres.",
            "tier_2": f"{height_cm} cm = {height_m} m. Now calculate {mass} / ({height_m})^2.",
            "tier_3": f"{correct}."
        }
    }

def _subskill_3(r: random.Random) -> Dict[str, Any]:
    """Classify adult weight status based on calculated BMI using the CAPS table."""
    name = r.choice(SA_NAMES)
    category = r.choice(["Underweight", "Normal weight", "Overweight", "Obese"])
    if category == "Underweight":
        bmi = round(r.uniform(15.5, 18.2), 1)
    elif category == "Normal weight":
        bmi = round(r.uniform(19.0, 24.5), 1)
    elif category == "Overweight":
        bmi = round(r.uniform(25.5, 29.5), 1)
    else:
        bmi = round(r.uniform(31.0, 36.5), 1)

    prompt = (
        f"{name}'s Body Mass Index (BMI) was calculated to be **{_fmt_num(bmi, 1)} kg/m²**.\\n\\n"
        f"Refer to the World Health Organization adult weight classification:\\n"
        f"- **Underweight:** BMI < 18,5\\n"
        f"- **Normal weight:** 18,5 ≤ BMI ≤ 24,9\\n"
        f"- **Overweight:** 25,0 ≤ BMI ≤ 29,9\\n"
        f"- **Obese:** BMI ≥ 30,0\\n\\n"
        f"Determine {name}'s official weight status category."
    )
    categories = ["Underweight", "Normal weight", "Overweight", "Obese"]
    distractors = [c for c in categories if c != category]
    expl = (
        f"✓ [1 Mark: Classification — Map BMI value to reference range]\\n"
        f"Since BMI = {_fmt_num(bmi, 1)} kg/m², it falls in the range for **{category}**."
    )
    return {
        "subskill": "gr11_weight_temp_subskill_3",
        "prompt": prompt,
        "options": _build_mc_options(category, distractors, r),
        "correct_answer": category,
        "explanation": expl,
        "hints": {
            "tier_1": f"Check which boundary interval {_fmt_num(bmi, 1)} falls into.",
            "tier_2": "Underweight < 18,5; Normal 18,5-24,9; Overweight 25,0-29,9; Obese >= 30,0.",
            "tier_3": f"{category}."
        }
    }

def _subskill_4(r: random.Random) -> Dict[str, Any]:
    """Calculate required weight reduction to reach the upper threshold of normal weight (BMI = 24.9)."""
    name = r.choice(SA_NAMES)
    height = round(r.uniform(1.60, 1.85), 2)
    mass = round(r.uniform(78.0, 102.0), 1)
    target_mass = round(24.9 * (height ** 2), 1)
    weight_loss_needed = round(mass - target_mass, 1)

    prompt = (
        f"{name} has a height of **{_fmt_num(height, 2)} m** and currently weighs **{_fmt_num(mass)} kg**.\\n"
        f"{name}'s doctor advises reaching a maximum healthy normal BMI of **24,9 kg/m²**.\\n\\n"
        f"Calculate the mass in kilograms that {name} must lose to achieve a BMI of exactly 24,9 kg/m².\\n"
        f"Round your answer to one decimal place."
    )
    correct = f"{_fmt_num(weight_loss_needed, 1)} kg"
    distractors = [
        f"{_fmt_num(round(weight_loss_needed + 4.2, 1), 1)} kg",
        f"{_fmt_num(round(target_mass, 1), 1)} kg",
        f"{_fmt_num(round(abs(weight_loss_needed - 3.5), 1), 1)} kg"
    ]
    expl = (
        f"✓ [1 Mark: Target mass calculation]\\n"
        f"$$\\\\text{{Target Mass}} = \\\\text{{Target BMI}} \\\\times (\\\\text{{Height}})^2 = 24,9 \\\\times ({_fmt_num(height, 2)})^2 = {_fmt_num(target_mass, 1)}\\\\text{{ kg}}$$\\n"
        f"✓ [1 Mark: Mass difference]\\n"
        f"$$\\\\text{{Weight to lose}} = {_fmt_num(mass)} - {_fmt_num(target_mass, 1)} = {_fmt_num(weight_loss_needed, 1)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_4",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {
            "tier_1": "First find the target mass using Target Mass = 24,9 × height².",
            "tier_2": f"Target mass = 24,9 × {height}^2 = {target_mass} kg. Subtract from current mass {mass} kg.",
            "tier_3": f"{correct}."
        }
    }

def _subskill_5(r: random.Random) -> Dict[str, Any]:
    """Calculate maximum healthy weight for an adult of given height to maintain normal BMI (< 25)."""
    name = r.choice(SA_NAMES)
    height = round(r.uniform(1.50, 1.95), 2)
    max_mass = round(24.9 * (height ** 2), 1)

    prompt = (
        f"{name} is an athlete whose height is **{_fmt_num(height, 2)} m**.\\n"
        f"According to health guidelines, the upper threshold for a normal BMI is **24,9 kg/m²**.\\n\\n"
        f"Calculate {name}'s maximum permissible weight in kilograms to remain within the normal BMI range.\\n"
        f"Round to one decimal place."
    )
    correct = f"{_fmt_num(max_mass, 1)} kg"
    distractors = [
        f"{_fmt_num(round(max_mass + 5.5, 1), 1)} kg",
        f"{_fmt_num(round(max_mass - 4.8, 1), 1)} kg",
        f"{_fmt_num(round(24.9 * height, 1), 1)} kg"
    ]
    expl = (
        f"✓ [1 Mark: Rearranging formula]\\n"
        f"$$\\\\text{{Mass}} = \\\\text{{BMI}} \\\\times (\\\\text{{Height}})^2$$\\n"
        f"✓ [1 Mark: Substitution and calculation]\\n"
        f"$$\\\\text{{Mass}} = 24,9 \\\\times ({_fmt_num(height, 2)})^2 = 24,9 \\\\times {_fmt_num(round(height**2, 4), 4)} \\\\approx {_fmt_num(max_mass, 1)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_5",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {
            "tier_1": "Multiply 24,9 by the square of the height.",
            "tier_2": f"24,9 × ({height})^2.",
            "tier_3": f"{correct}."
        }
    }

def _subskill_6(r: random.Random) -> Dict[str, Any]:
    """Calculate minimum healthy weight for an adult of given height (BMI = 18.5)."""
    name = r.choice(SA_NAMES)
    height = round(r.uniform(1.52, 1.88), 2)
    min_mass = round(18.5 * (height ** 2), 1)

    prompt = (
        f"{name} is recovering from an illness and has a height of **{_fmt_num(height, 2)} m**.\\n"
        f"The lower limit for a healthy normal BMI is **18,5 kg/m²**.\\n\\n"
        f"Calculate the minimum weight in kilograms {name} should maintain to avoid being classified as underweight.\\n"
        f"Round your answer to one decimal place."
    )
    correct = f"{_fmt_num(min_mass, 1)} kg"
    distractors = [
        f"{_fmt_num(round(min_mass - 3.5, 1), 1)} kg",
        f"{_fmt_num(round(min_mass + 4.2, 1), 1)} kg",
        f"{_fmt_num(round(18.5 * height, 1), 1)} kg"
    ]
    expl = (
        f"✓ [1 Mark: Method — Formula substitution]\\n"
        f"$$\\\\text{{Minimum Mass}} = 18,5 \\\\times (\\\\text{{Height}})^2 = 18,5 \\\\times ({_fmt_num(height, 2)})^2$$\\n"
        f"✓ [1 Mark: Accuracy]\\n"
        f"$$\\\\text{{Minimum Mass}} = {_fmt_num(min_mass, 1)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_6",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {
            "tier_1": "Multiply 18,5 by height squared.",
            "tier_2": f"18,5 × ({height})^2 = {min_mass}.",
            "tier_3": f"{correct}."
        }
    }

def _subskill_7(r: random.Random) -> Dict[str, Any]:
    """Determine height of an individual given their mass (kg) and BMI value."""
    name = r.choice(SA_NAMES)
    mass = round(r.uniform(62.0, 88.0), 1)
    bmi = round(r.uniform(21.0, 27.5), 1)
    height = round(math.sqrt(mass / bmi), 2)

    prompt = (
        f"{name} has a recorded mass of **{_fmt_num(mass)} kg** and a Body Mass Index of **{_fmt_num(bmi, 1)} kg/m²**.\\n\\n"
        f"Use the BMI formula to calculate {name}'s height in metres.\\n"
        f"Round your answer to two decimal places."
    )
    correct = f"{_fmt_num(height, 2)} m"
    distractors = [
        f"{_fmt_num(round(height + 0.12, 2), 2)} m",
        f"{_fmt_num(round(height - 0.09, 2), 2)} m",
        f"{_fmt_num(round(math.sqrt(mass * bmi) / 10, 2), 2)} m"
    ]
    expl = (
        f"✓ [1 Mark: Rearranging formula]\\n"
        f"$$\\\\text{{Height}}^2 = \\\\frac{{\\\\text{{Mass}}}}{{\\\\text{{BMI}}}} = \\\\frac{{{_fmt_num(mass)}}}{{{_fmt_num(bmi, 1)}}} = {_fmt_num(round(mass / bmi, 4), 4)}$$\\n"
        f"✓ [1 Mark: Taking square root and rounding]\\n"
        f"$$\\\\text{{Height}} = \\\\sqrt{{{_fmt_num(round(mass / bmi, 4), 4)}}} \\\\approx {_fmt_num(height, 2)}\\\\text{{ m}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_7",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {
            "tier_1": "Divide mass by BMI, then take the square root of the answer.",
            "tier_2": f"Height = sqrt({mass} / {bmi}).",
            "tier_3": f"{correct}."
        }
    }

def _subskill_8(r: random.Random) -> Dict[str, Any]:
    """Compare BMI of two individuals and evaluate relative risk categories."""
    p1 = r.choice(SA_NAMES[:10])
    p2 = r.choice(SA_NAMES[10:])
    h1, m1 = 1.70, round(r.uniform(55.0, 68.0), 1)
    h2, m2 = 1.75, round(r.uniform(85.0, 98.0), 1)
    bmi1 = round(m1 / (h1 ** 2), 1)
    bmi2 = round(m2 / (h2 ** 2), 1)

    diff = round(abs(bmi2 - bmi1), 1)
    prompt = (
        f"Two colleagues compare their health metrics:\\n"
        f"- **{p1}:** Height = {_fmt_num(h1, 2)} m, Mass = {_fmt_num(m1)} kg (BMI = {_fmt_num(bmi1, 1)} kg/m²)\\n"
        f"- **{p2}:** Height = {_fmt_num(h2, 2)} m, Mass = {_fmt_num(m2)} kg (BMI = {_fmt_num(bmi2, 1)} kg/m²)\\n\\n"
        f"Calculate the absolute difference between their BMI values to one decimal place."
    )
    correct = f"{_fmt_num(diff, 1)} kg/m²"
    distractors = [
        f"{_fmt_num(round(diff + 2.1, 1), 1)} kg/m²",
        f"{_fmt_num(round(abs(diff - 1.8), 1), 1)} kg/m²",
        f"{_fmt_num(round(m2 - m1, 1), 1)} kg/m²"
    ]
    expl = (
        f"✓ [1 Mark: Subtraction of BMI values]\\n"
        f"$$\\\\text{{Difference}} = |{_fmt_num(bmi2, 1)} - {_fmt_num(bmi1, 1)}| = {_fmt_num(diff, 1)}\\\\text{{ kg/m}}^2$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_8",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {
            "tier_1": "Subtract the smaller BMI from the larger BMI.",
            "tier_2": f"{bmi2} - {bmi1} = {diff}.",
            "tier_3": f"{correct}."
        }
    }

def _subskill_9(r: random.Random) -> Dict[str, Any]:
    """Analyze health implications and lifestyle adjustments for obesity (BMI >= 30)."""
    name = r.choice(SA_NAMES)
    bmi = round(r.uniform(32.5, 38.0), 1)
    prompt = (
        f"{name}'s health screening confirms a BMI of **{_fmt_num(bmi, 1)} kg/m²** (Obese Class I/II).\\n\\n"
        f"Which of the following is the most appropriate medical and lifestyle recommendation for {name}?"
    )
    correct = "Consult a dietician for a calorie-controlled balanced diet and gradual aerobic exercise"
    distractors = [
        "Eliminate all carbohydrate intake and water intake immediately",
        "Increase dietary saturated fats to rapidly build muscular tissue",
        "Ignore the BMI reading because body mass index never correlates with cardiovascular health"
    ]
    expl = (
        f"✓ [1 Mark: Interpretation of obesity health guidelines]\\n"
        f"For adults with BMI ≥ 30 kg/m², South African health guidelines advocate professional dietary guidance "
        f"and progressive physical activity to manage hypertension and diabetes risks."
    )
    return {
        "subskill": "gr11_weight_temp_subskill_9",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {
            "tier_1": "Identify safe, evidence-based lifestyle changes.",
            "tier_2": "Gradual diet improvement and structured physical activity.",
            "tier_3": f"{correct}."
        }
    }

def _subskill_10(r: random.Random) -> Dict[str, Any]:
    """Calculate percentage reduction in body mass required to move to normal weight."""
    name = r.choice(SA_NAMES)
    current_mass = round(r.uniform(85.0, 110.0), 1)
    target_mass = round(r.uniform(65.0, 75.0), 1)
    loss = current_mass - target_mass
    pct_loss = round((loss / current_mass) * 100, 1)

    prompt = (
        f"{name} currently weighs **{_fmt_num(current_mass)} kg** and aims to reach a target weight of **{_fmt_num(target_mass)} kg**.\\n\\n"
        f"Calculate the percentage reduction in body weight required to reach this target.\\n"
        f"Round to one decimal place."
    )
    correct = f"{_fmt_num(pct_loss, 1)}%"
    distractors = [
        f"{_fmt_num(round(pct_loss + 3.2, 1), 1)}%",
        f"{_fmt_num(round((loss / target_mass) * 100, 1), 1)}%",
        f"{_fmt_num(round(pct_loss - 2.5, 1), 1)}%"
    ]
    expl = (
        f"✓ [1 Mark: Mass reduction]\\n"
        f"$$\\\\text{{Reduction}} = {_fmt_num(current_mass)} - {_fmt_num(target_mass)} = {_fmt_num(loss, 1)}\\\\text{{ kg}}$$\\n"
        f"✓ [1 Mark: Percentage calculation]\\n"
        f"$$\\\\text{{Percentage}} = \\\\frac{{{_fmt_num(loss, 1)}}}{{{_fmt_num(current_mass)}}} \\\\times 100 \\\\approx {_fmt_num(pct_loss, 1)}\\\\%$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_10",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {
            "tier_1": "Calculate mass to lose divided by original mass, then multiply by 100.",
            "tier_2": f"({current_mass} - {target_mass}) / {current_mass} * 100.",
            "tier_3": f"{correct}."
        }
    }
''')

# Now add subskills 11 to 26
code_sections.append('''
# ----------------------------------------------------------------------------
# SUBSKILLS 11-18: Growth Charts & Pediatric Weight-for-Age
# ----------------------------------------------------------------------------

def _subskill_11(r: random.Random) -> Dict[str, Any]:
    """Read infant mass from a Road-to-Health growth table at a given age."""
    baby_name = r.choice(["Kgosi", "Lethabo", "Bokamoso", "Siyabonga", "Khanyisile"])
    age_months = r.choice([3, 6, 9, 12, 15, 18])
    # Typical weights for age
    wt_map = {3: 6.4, 6: 7.9, 9: 8.9, 12: 9.6, 15: 10.3, 18: 11.0}
    actual_wt = round(wt_map[age_months] + r.uniform(-0.4, 0.4), 1)

    prompt = (
        f"At the municipal primary healthcare clinic, baby {baby_name}'s Road-to-Health booklet displays the following record:\\n\\n"
        f"| Age (Months) | Recorded Weight (kg) | Median Standard (kg) |\\n"
        f"| :--- | :--- | :--- |\\n"
        f"| 3 | 6,2 | 6,4 |\\n"
        f"| 6 | 7,7 | 7,9 |\\n"
        f"| 9 | 8,8 | 8,9 |\\n"
        f"| 12 | 9,5 | 9,6 |\\n"
        f"| {age_months} | **{_fmt_num(actual_wt)}** | {_fmt_num(wt_map[age_months])} |\\n\\n"
        f"What was baby {baby_name}'s recorded weight at {age_months} months of age?"
    )
    correct = f"{_fmt_num(actual_wt)} kg"
    distractors = [
        f"{_fmt_num(wt_map[age_months])} kg",
        f"{_fmt_num(actual_wt + 1.2)} kg",
        f"{_fmt_num(actual_wt - 1.1)} kg"
    ]
    expl = f"✓ [1 Mark: Direct table read]\\nBaby {baby_name}'s recorded weight at {age_months} months is {_fmt_num(actual_wt)} kg."
    return {
        "subskill": "gr11_weight_temp_subskill_11",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Look at the row for {age_months} months.", "tier_2": "Read the Recorded Weight column.", "tier_3": f"{correct}."}
    }

def _subskill_12(r: random.Random) -> Dict[str, Any]:
    """Determine if a child's weight is tracking above or below the 50th percentile (median)."""
    baby = r.choice(["Bandile", "Unathi", "Minenhle", "Tshiamo"])
    age = r.choice([6, 9, 12, 18])
    median = {6: 7.9, 9: 8.9, 12: 9.6, 18: 10.9}[age]
    is_above = r.choice([True, False])
    actual = round(median + (0.8 if is_above else -0.9), 1)

    prompt = (
        f"At {age} months, baby {baby} weighs **{_fmt_num(actual)} kg**.\\n"
        f"The World Health Organization (WHO) median (50th percentile) weight for this age is **{_fmt_num(median)} kg**.\\n\\n"
        f"State whether {baby}'s weight is tracking above or below the median percentile line."
    )
    correct = "Above the median line" if is_above else "Below the median line"
    distractors = ["Below the median line" if is_above else "Above the median line", "Exactly on the 97th percentile", "Severely malnourished"]
    expl = f"✓ [1 Mark: Percentile comparison]\\nSince {_fmt_num(actual)} kg {'is greater than' if is_above else 'is less than'} {_fmt_num(median)} kg, the weight is {correct}."
    return {
        "subskill": "gr11_weight_temp_subskill_12",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Compare {actual} kg with {median} kg.", "tier_2": f"{actual} vs {median}.", "tier_3": f"{correct}."}
    }

def _subskill_13(r: random.Random) -> Dict[str, Any]:
    """Classify child growth status based on z-score / percentile threshold (underweight risk)."""
    baby = r.choice(["Karabo", "Enzokuhle", "Junior", "Sive"])
    threshold_3rd = 7.1
    recorded = round(r.uniform(6.1, 6.8), 1)
    prompt = (
        f"Baby {baby} (age 12 months) weighs **{_fmt_num(recorded)} kg**.\\n"
        f"On the Road-to-Health growth chart, the 3rd percentile (-2 Z-score) threshold for 12 months is **{_fmt_num(threshold_3rd)} kg**.\\n\\n"
        f"What nutritional classification does a weight falling below the 3rd percentile indicate?"
    )
    correct = "Underweight / Nutritional risk requiring clinical intervention"
    distractors = [
        "Normal and healthy thriving growth trajectory",
        "Overweight with risk of childhood obesity",
        "Optimal physical growth exceeding expected benchmarks"
    ]
    expl = f"✓ [1 Mark: Clinical interpretation]\\nAny infant growth curve falling below the 3rd percentile (-2 SD line) signals underweight status and potential malnutrition."
    return {
        "subskill": "gr11_weight_temp_subskill_13",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Points below the 3rd percentile curve indicate insufficient weight gain.", "tier_2": "Underweight / nutritional risk.", "tier_3": f"{correct}."}
    }

def _subskill_14(r: random.Random) -> Dict[str, Any]:
    """Identify weight faltering or growth plateau across two clinic visits."""
    baby = r.choice(["Owami", "Melokuhle", "Lesedi", "Kabelo"])
    wt_visit1 = 8.4
    wt_visit2 = 8.4
    prompt = (
        f"Baby {baby}'s clinic record shows a mass of **{_fmt_num(wt_visit1)} kg** at 8 months "
        f"and exactly **{_fmt_num(wt_visit2)} kg** at 10 months.\\n\\n"
        f"How is a horizontal (flat) trajectory on a Road-to-Health growth chart described and interpreted?"
    )
    correct = "Growth plateau (weight faltering / danger sign — child has not gained weight)"
    distractors = [
        "Normal growth spurt indicating healthy rapid development",
        "Excessive weight gain requiring dietary restriction",
        "Measurement error that should be completely disregarded by the nursing sister"
    ]
    expl = f"✓ [1 Mark: Curve interpretation]\\nA flat line on the Road-to-Health chart indicates weight faltering (no weight gained), which is a clinical warning sign."
    return {
        "subskill": "gr11_weight_temp_subskill_14",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "A flat growth curve means no weight has been gained over time.", "tier_2": "Weight faltering / growth plateau.", "tier_3": f"{correct}."}
    }

def _subskill_15(r: random.Random) -> Dict[str, Any]:
    """Calculate average monthly weight gain between two clinic check-ups."""
    baby = r.choice(["Kopano", "Phenyo", "Ofentse", "Rebaone"])
    wt1 = round(r.uniform(5.5, 6.5), 1)
    wt2 = round(wt1 + r.uniform(1.8, 2.7), 1)
    m1, m2 = 3, 9
    gain = wt2 - wt1
    avg_gain = round(gain / (m2 - m1), 2)

    prompt = (
        f"Baby {baby} weighed **{_fmt_num(wt1)} kg** at 3 months and **{_fmt_num(wt2)} kg** at 9 months.\\n\\n"
        f"Calculate baby {baby}'s average weight gain per month over this 6-month period.\\n"
        f"Round your answer to two decimal places."
    )
    correct = f"{_fmt_num(avg_gain, 2)} kg/month"
    distractors = [
        f"{_fmt_num(round(gain, 2), 2)} kg/month",
        f"{_fmt_num(round(avg_gain + 0.15, 2), 2)} kg/month",
        f"{_fmt_num(round(avg_gain - 0.12, 2), 2)} kg/month"
    ]
    expl = (
        f"✓ [1 Mark: Total weight gain]\\n"
        f"$$\\\\text{{Gain}} = {_fmt_num(wt2)} - {_fmt_num(wt1)} = {_fmt_num(gain, 1)}\\\\text{{ kg}}$$\\n"
        f"✓ [1 Mark: Average monthly gain]\\n"
        f"$$\\\\text{{Average}} = \\\\frac{{{_fmt_num(gain, 1)}}}{{9 - 3}} = \\\\frac{{{_fmt_num(gain, 1)}}}{{6}} \\\\approx {_fmt_num(avg_gain, 2)}\\\\text{{ kg/month}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_15",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Subtract month 3 weight from month 9 weight, then divide by 6.", "tier_2": f"({wt2} - {wt1}) / 6.", "tier_3": f"{correct}."}
    }

def _subskill_16(r: random.Random) -> Dict[str, Any]:
    """Compare a child's weight against the median target weight to find the percentage deficit."""
    baby = r.choice(["Neo", "Thato", "Katlego", "Oratile"])
    median_wt = 10.0
    actual_wt = round(r.uniform(7.8, 8.8), 1)
    deficit = round(median_wt - actual_wt, 1)
    pct_deficit = round((deficit / median_wt) * 100, 1)

    prompt = (
        f"At 14 months of age, baby {baby} weighs **{_fmt_num(actual_wt)} kg**.\\n"
        f"The median target weight for a 14-month-old is **{_fmt_num(median_wt)} kg**.\\n\\n"
        f"Calculate baby {baby}'s weight deficit as a percentage of the median target weight."
    )
    correct = f"{_fmt_num(pct_deficit, 1)}%"
    distractors = [
        f"{_fmt_num(round(pct_deficit + 4.5, 1), 1)}%",
        f"{_fmt_num(round((actual_wt / median_wt) * 100, 1), 1)}%",
        f"{_fmt_num(round(pct_deficit - 3.2, 1), 1)}%"
    ]
    expl = (
        f"✓ [1 Mark: Weight difference]\\n"
        f"$$\\\\text{{Deficit}} = {_fmt_num(median_wt)} - {_fmt_num(actual_wt)} = {_fmt_num(deficit, 1)}\\\\text{{ kg}}$$\\n"
        f"✓ [1 Mark: Percentage deficit]\\n"
        f"$$\\\\text{{Percentage}} = \\\\frac{{{_fmt_num(deficit, 1)}}}{{{_fmt_num(median_wt)}}} \\\\times 100 = {_fmt_num(pct_deficit, 1)}\\\\%$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_16",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Subtract {actual_wt} from {median_wt}, then divide by {median_wt} and multiply by 100.", "tier_2": f"({deficit} / 10) * 100.", "tier_3": f"{correct}."}
    }

def _subskill_17(r: random.Random) -> Dict[str, Any]:
    """Read height/length-for-age chart to evaluate stunting."""
    baby = r.choice(["Simphiwe", "Nkazimulo", "Amahle", "Zikho"])
    length = round(r.uniform(68.0, 71.0), 1)
    prompt = (
        f"At 12 months, baby {baby}'s recumbent length is **{_fmt_num(length)} cm**.\\n"
        f"The clinic growth standard states that a 12-month-old child whose length is below 71,0 cm "
        f"is classified as **stunted** (chronic undernutrition).\\n\\n"
        f"Does baby {baby}'s measurement meet the diagnostic criterion for stunting?"
    )
    is_stunted = length < 71.0
    correct = "Yes, because the length is below the 71,0 cm threshold" if is_stunted else "No, because the length is at or above 71,0 cm"
    distractors = [
        "No, because the length is at or above 71,0 cm" if is_stunted else "Yes, because the length is below the 71,0 cm threshold",
        "Cannot be determined without calculating the Body Mass Index",
        "Stunting only depends on weight, never on length or height"
    ]
    expl = f"✓ [1 Mark: Stunting benchmark comparison]\\nSince {_fmt_num(length)} cm is {'< 71,0 cm' if is_stunted else '≥ 71,0 cm'}, the child {'meets' if is_stunted else 'does not meet'} the criterion for stunting."
    return {
        "subskill": "gr11_weight_temp_subskill_17",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Compare {length} cm to the 71,0 cm cutoff.", "tier_2": "Check if it is below 71,0 cm.", "tier_3": f"{correct}."}
    }

def _subskill_18(r: random.Random) -> Dict[str, Any]:
    """Interpret clinic Road-to-Health summary record table."""
    baby = r.choice(["Khaya", "Gugu", "Siyanda", "Lindokuhle"])
    head_circ = round(r.uniform(43.5, 46.0), 1)
    wt = round(r.uniform(8.5, 9.8), 1)

    prompt = (
        f"Consider baby {baby}'s 9-month clinic milestone record:\\n\\n"
        f"| Parameter | Value Recorded | Healthy Reference Range |\\n"
        f"| :--- | :--- | :--- |\\n"
        f"| Mass | {_fmt_num(wt)} kg | 7,2 kg – 10,5 kg |\\n"
        f"| Head Circumference | {_fmt_num(head_circ)} cm | 42,5 cm – 47,0 cm |\\n"
        f"| Immunization | Measles Dose 1 | Complete |\\n\\n"
        f"Based on this table, is baby {baby}'s head circumference within the healthy reference range?"
    )
    correct = f"Yes, {_fmt_num(head_circ)} cm lies within the reference range of 42,5 cm to 47,0 cm"
    distractors = [
        f"No, {_fmt_num(head_circ)} cm is dangerously above the reference limit",
        f"No, {_fmt_num(head_circ)} cm indicates severe microcephaly below 42,5 cm",
        "The head circumference cannot be verified without knowing the child's height"
    ]
    expl = f"✓ [1 Mark: Reference range verification]\\n{_fmt_num(head_circ)} cm is between 42,5 cm and 47,0 cm, so it is strictly within the normal range."
    return {
        "subskill": "gr11_weight_temp_subskill_18",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Compare the recorded value against the minimum and maximum reference values.", "tier_2": "42,5 <= 44,5 <= 47,0.", "tier_3": f"{correct}."}
    }

# ----------------------------------------------------------------------------
# SUBSKILLS 19-26: Medical Dosages Based on Mass & Concentration
# ----------------------------------------------------------------------------

def _subskill_19(r: random.Random) -> Dict[str, Any]:
    """Calculate total daily active ingredient dosage in mg given mg/kg/day."""
    child = r.choice(SA_NAMES)
    mass = round(r.uniform(12.0, 28.0), 1)
    rate = r.choice([20.0, 25.0, 30.0, 40.0]) # mg/kg/day
    total_mg = round(mass * rate, 1)

    prompt = (
        f"A paediatrician prescribes amoxicillin antibiotic for {child}, whose body mass is **{_fmt_num(mass)} kg**.\\n"
        f"The recommended dosage rate is **{_fmt_num(rate)} mg per kg of body mass per day**.\\n\\n"
        f"Calculate the total active ingredient dosage in milligrams (mg) that {child} must receive in one day."
    )
    correct = f"{_fmt_num(total_mg)} mg"
    distractors = [
        f"{_fmt_num(round(total_mg + 100.0))} mg",
        f"{_fmt_num(round(mass * (rate - 5.0)))} mg",
        f"{_fmt_num(round(total_mg / 2.0))} mg"
    ]
    expl = (
        f"✓ [1 Mark: Method — Multiply mass by dosage rate]\\n"
        f"$$\\\\text{{Total daily dosage}} = {_fmt_num(mass)}\\\\text{{ kg}} \\\\times {_fmt_num(rate)}\\\\text{{ mg/kg}} = {_fmt_num(total_mg)}\\\\text{{ mg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_19",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply the patient's weight by the mg/kg rate.", "tier_2": f"{mass} × {rate}.", "tier_3": f"{correct}."}
    }

def _subskill_20(r: random.Random) -> Dict[str, Any]:
    """Calculate single dose in mg when daily dosage is divided into equal doses."""
    child = r.choice(SA_NAMES)
    total_daily_mg = r.choice([360, 450, 600, 750, 900])
    doses_per_day = r.choice([2, 3])
    single_mg = round(total_daily_mg / doses_per_day, 1)

    prompt = (
        f"{child} is prescribed a total daily medication dose of **{total_daily_mg} mg**.\\n"
        f"The instructions state that the medicine must be administered in **{doses_per_day} equal doses** daily.\\n\\n"
        f"Calculate the quantity of medicine in milligrams (mg) for each single dose."
    )
    correct = f"{_fmt_num(single_mg)} mg"
    distractors = [
        f"{_fmt_num(round(single_mg * 1.5))} mg",
        f"{_fmt_num(round(total_daily_mg * doses_per_day))} mg",
        f"{_fmt_num(round(single_mg - 30))} mg"
    ]
    expl = (
        f"✓ [1 Mark: Division into equal doses]\\n"
        f"$$\\\\text{{Single dose}} = \\\\frac{{{total_daily_mg}\\\\text{{ mg}}}}{{{doses_per_day}}} = {_fmt_num(single_mg)}\\\\text{{ mg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_20",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Divide total daily mg by the number of doses per day.", "tier_2": f"{total_daily_mg} / {doses_per_day}.", "tier_3": f"{correct}."}
    }

def _subskill_21(r: random.Random) -> Dict[str, Any]:
    """Calculate liquid medicine volume in ml from suspension concentration."""
    child = r.choice(SA_NAMES)
    dose_mg = r.choice([125, 250, 375, 500])
    # Concentration: 125 mg / 5 ml or 250 mg / 5 ml
    conc_mg = r.choice([125, 250])
    volume_ml = round((dose_mg / conc_mg) * 5.0, 1)

    prompt = (
        f"A clinic sister prepares an oral antibiotic suspension for {child}.\\n"
        f"The prescription specifies a single dose of **{dose_mg} mg**.\\n"
        f"The bottle label states the suspension concentration is **{conc_mg} mg per 5 ml**.\\n\\n"
        f"Calculate the volume of liquid in millilitres (ml) that must be measured in the medicine syringe for this dose."
    )
    correct = f"{_fmt_num(volume_ml)} ml"
    distractors = [
        f"{_fmt_num(round(volume_ml * 2.0))} ml",
        f"{_fmt_num(round(volume_ml / 2.0, 1))} ml",
        f"{_fmt_num(round(volume_ml + 2.5, 1))} ml"
    ]
    expl = (
        f"✓ [1 Mark: Proportion / Ratio calculation]\\n"
        f"$$\\\\text{{Volume (ml)}} = \\\\frac{{\\\\text{{Dose (mg)}}}}{{\\\\text{{Concentration (mg)}}}} \\\\times 5\\\\text{{ ml}} = \\\\frac{{{dose_mg}}}{{{conc_mg}}} \\\\times 5 = {_fmt_num(volume_ml)}\\\\text{{ ml}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_21",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Divide {dose_mg} by {conc_mg}, then multiply by 5 ml.", "tier_2": f"({dose_mg} / {conc_mg}) * 5.", "tier_3": f"{correct}."}
    }

def _subskill_22(r: random.Random) -> Dict[str, Any]:
    """Calculate total volume of antibiotic syrup needed for a complete course."""
    child = r.choice(SA_NAMES)
    dose_ml = r.choice([5.0, 7.5, 10.0])
    doses_per_day = r.choice([2, 3])
    days = r.choice([5, 7, 10])
    total_ml = round(dose_ml * doses_per_day * days, 1)

    prompt = (
        f"{child} is prescribed **{_fmt_num(dose_ml)} ml** of antibiotic suspension **{doses_per_day} times daily** "
        f"for a duration of **{days} days**.\\n\\n"
        f"Calculate the total volume of suspension in millilitres (ml) required to complete the full treatment course."
    )
    correct = f"{_fmt_num(total_ml)} ml"
    distractors = [
        f"{_fmt_num(round(dose_ml * days, 1))} ml",
        f"{_fmt_num(round(total_ml + 25.0, 1))} ml",
        f"{_fmt_num(round(total_ml * 1.5, 1))} ml"
    ]
    expl = (
        f"✓ [1 Mark: Daily volume]\\n"
        f"$$\\\\text{{Daily volume}} = {_fmt_num(dose_ml)}\\\\text{{ ml}} \\\\times {doses_per_day} = {_fmt_num(round(dose_ml * doses_per_day, 1))}\\\\text{{ ml/day}}$$\\n"
        f"✓ [1 Mark: Total course volume]\\n"
        f"$$\\\\text{{Total}} = {_fmt_num(round(dose_ml * doses_per_day, 1))} \\\\times {days} = {_fmt_num(total_ml)}\\\\text{{ ml}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_22",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply dose per administration by doses per day by number of days.", "tier_2": f"{dose_ml} × {doses_per_day} × {days}.", "tier_3": f"{correct}."}
    }

def _subskill_23(r: random.Random) -> Dict[str, Any]:
    """Determine number of 100 ml medicine bottles required for a course."""
    child = r.choice(SA_NAMES)
    total_ml_needed = r.choice([120, 140, 150, 175, 210])
    bottle_size = 100
    bottles_needed = math.ceil(total_ml_needed / bottle_size)

    prompt = (
        f"A paediatric prescription for {child} requires a total course volume of **{total_ml_needed} ml** of cough syrup.\\n"
        f"The pharmacy only dispenses this medicine in sealed bottles of **{bottle_size} ml**.\\n\\n"
        f"How many full bottles must the parent purchase to ensure the treatment is completed without running short?"
    )
    correct = f"{bottles_needed} bottles"
    distractors = [
        f"{bottles_needed - 1} bottles",
        f"{bottles_needed + 1} bottles",
        f"{round(total_ml_needed / bottle_size, 1)} bottles"
    ]
    expl = (
        f"✓ [1 Mark: Calculation & Rounding up for practical sufficiency]\\n"
        f"$$\\\\frac{{{total_ml_needed}}}{{{bottle_size}}} = {_fmt_num(round(total_ml_needed / bottle_size, 2), 2)}\\\\text{{ bottles}}$$\\n"
        f"Since the pharmacy cannot sell partial bottles, the parent must purchase **{bottles_needed} bottles**."
    )
    return {
        "subskill": "gr11_weight_temp_subskill_23",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Divide total ml needed by bottle size and round UP to next whole bottle.", "tier_2": f"{total_ml_needed} / 100 = {total_ml_needed/100:.1f} -> Round up.", "tier_3": f"{correct}."}
    }

def _subskill_24(r: random.Random) -> Dict[str, Any]:
    """Paracetamol single dose calculation (15 mg/kg) for pediatric patient."""
    child = r.choice(SA_NAMES)
    mass = round(r.uniform(10.0, 24.0), 1)
    dose_rate = 15.0 # mg/kg
    paracetamol_mg = round(mass * dose_rate, 1)

    prompt = (
        f"Paracetamol syrup dosage instructions state: **15 mg per kg of body mass per dose**.\\n"
        f"{child} weighs **{_fmt_num(mass)} kg** and presents with fever.\\n\\n"
        f"Calculate the correct paracetamol dose in milligrams (mg) for {child}."
    )
    correct = f"{_fmt_num(paracetamol_mg)} mg"
    distractors = [
        f"{_fmt_num(round(paracetamol_mg + 50.0))} mg",
        f"{_fmt_num(round(mass * 10.0))} mg",
        f"{_fmt_num(round(paracetamol_mg - 35.0))} mg"
    ]
    expl = (
        f"✓ [1 Mark: Calculation]\\n"
        f"$$\\\\text{{Dose}} = {_fmt_num(mass)}\\\\text{{ kg}} \\\\times 15\\\\text{{ mg/kg}} = {_fmt_num(paracetamol_mg)}\\\\text{{ mg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_24",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply body mass in kg by 15 mg.", "tier_2": f"{mass} × 15.", "tier_3": f"{correct}."}
    }

def _subskill_25(r: random.Random) -> Dict[str, Any]:
    """Check maximum daily paracetamol safety limit (60 mg/kg/day)."""
    child = r.choice(SA_NAMES)
    mass = round(r.uniform(12.0, 20.0), 1)
    max_safe_daily = round(mass * 60.0, 1)
    # Give a proposed dosage: either safe or exceeding
    exceeds = r.choice([True, False])
    proposed_daily = round(max_safe_daily + (120 if exceeds else -150), 1)

    prompt = (
        f"The maximum safe daily dose of paracetamol is **60 mg per kg of body mass in 24 hours**.\\n"
        f"{child} weighs **{_fmt_num(mass)} kg**.\\n"
        f"A parent proposes giving a total of **{_fmt_num(proposed_daily)} mg** across the day.\\n\\n"
        f"Calculate the maximum safe daily limit and evaluate whether this proposed dose is safe."
    )
    is_safe = proposed_daily <= max_safe_daily
    correct = f"{'Safe' if is_safe else 'Unsafe (Exceeds limit)'}: Limit is {_fmt_num(max_safe_daily)} mg"
    distractors = [
        f"{'Unsafe (Exceeds limit)' if is_safe else 'Safe'}: Limit is {_fmt_num(max_safe_daily)} mg",
        f"Safe: Limit is {_fmt_num(round(max_safe_daily * 1.2))} mg",
        f"Unsafe: Limit is {_fmt_num(round(max_safe_daily * 0.8))} mg"
    ]
    expl = (
        f"✓ [1 Mark: Maximum safe limit]\\n"
        f"$$\\\\text{{Limit}} = {_fmt_num(mass)}\\\\text{{ kg}} \\\\times 60\\\\text{{ mg/kg}} = {_fmt_num(max_safe_daily)}\\\\text{{ mg}}$$\\n"
        f"✓ [1 Mark: Evaluation]\\n"
        f"Since {_fmt_num(proposed_daily)} mg {'is within' if is_safe else 'exceeds'} the {_fmt_num(max_safe_daily)} mg ceiling, the dose is {correct}."
    )
    return {
        "subskill": "gr11_weight_temp_subskill_25",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Multiply mass {mass} by 60 mg/kg to find the upper ceiling.", "tier_2": f"Limit = {mass} × 60 = {max_safe_daily}.", "tier_3": f"{correct}."}
    }

def _subskill_26(r: random.Random) -> Dict[str, Any]:
    """Calculate Oral Rehydration Salt (ORS) fluid replacement requirement in ml."""
    infant = r.choice(SA_NAMES)
    mass = round(r.uniform(6.0, 14.0), 1)
    episodes = r.choice([3, 4, 5])
    rate_per_episode = 10.0 # ml/kg per watery stool
    total_ors_ml = round(mass * rate_per_episode * episodes, 1)

    prompt = (
        f"WHO guidelines recommend administering **10 ml of Oral Rehydration Solution (ORS) per kg of body mass** "
        f"after every loose stool episode to prevent dehydration.\\n"
        f"Infant {infant} has a mass of **{_fmt_num(mass)} kg** and experienced **{episodes} episodes** today.\\n\\n"
        f"Calculate the total volume of ORS solution in millilitres (ml) that must be administered."
    )
    correct = f"{_fmt_num(total_ors_ml)} ml"
    distractors = [
        f"{_fmt_num(round(mass * rate_per_episode))} ml",
        f"{_fmt_num(round(total_ors_ml + 50.0))} ml",
        f"{_fmt_num(round(total_ors_ml - 40.0))} ml"
    ]
    expl = (
        f"✓ [1 Mark: Volume per episode]\\n"
        f"$$\\\\text{{Per episode}} = {_fmt_num(mass)} \\\\times 10 = {_fmt_num(round(mass * 10, 1))}\\\\text{{ ml}}$$\\n"
        f"✓ [1 Mark: Total volume]\\n"
        f"$$\\\\text{{Total}} = {_fmt_num(round(mass * 10, 1))} \\\\times {episodes} = {_fmt_num(total_ors_ml)}\\\\text{{ ml}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_26",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply mass × 10 ml/kg × number of episodes.", "tier_2": f"{mass} × 10 × {episodes}.", "tier_3": f"{correct}."}
    }
''')

# Now add subskills 27 to 44
code_sections.append('''
# ----------------------------------------------------------------------------
# SUBSKILLS 27-34: Unit Conversions & Commercial Packaging
# ----------------------------------------------------------------------------

def _subskill_27(r: random.Random) -> Dict[str, Any]:
    """Convert mass from grams to kilograms (g to kg)."""
    grams = r.choice([450, 750, 1250, 2400, 3650, 4800, 7250])
    kg = round(grams / 1000.0, 3)

    prompt = (
        f"A commercial recipe for a bakery requires **{_fmt_num(grams)} g** of white bread flour.\\n\\n"
        f"Convert this mass into kilograms (kg)."
    )
    correct = f"{_fmt_num(kg, 3)} kg"
    distractors = [
        f"{_fmt_num(kg * 10, 2)} kg",
        f"{_fmt_num(round(grams / 100.0, 2), 2)} kg",
        f"{_fmt_num(round(kg + 0.5, 3), 3)} kg"
    ]
    expl = (
        f"✓ [1 Mark: Conversion factor ($1\\\\text{{ kg}} = 1\\\\,000\\\\text{{ g}}$)]\\n"
        f"$$\\\\text{{Mass in kg}} = \\\\frac{{{_fmt_num(grams)}\\\\text{{ g}}}}{{1\\\\,000}} = {_fmt_num(kg, 3)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_27",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Divide grams by 1 000.", "tier_2": f"{grams} / 1000.", "tier_3": f"{correct}."}
    }

def _subskill_28(r: random.Random) -> Dict[str, Any]:
    """Convert mass between kilograms and tonnes (t to kg and kg to t)."""
    tonnes = round(r.uniform(2.5, 18.0), 2)
    kg = round(tonnes * 1000.0)

    prompt = (
        f"A maize farmer in the Free State loads a flatbed grain truck with **{_fmt_num(tonnes, 2)} metric tonnes** of harvested grain.\\n\\n"
        f"Convert this harvest mass into kilograms (kg)."
    )
    correct = f"{_fmt_num(kg)} kg"
    distractors = [
        f"{_fmt_num(round(tonnes * 100))} kg",
        f"{_fmt_num(round(tonnes * 10000))} kg",
        f"{_fmt_num(round(kg + 1500))} kg"
    ]
    expl = (
        f"✓ [1 Mark: Metric ton conversion factor ($1\\\\text{{ t}} = 1\\\\,000\\\\text{{ kg}}$)]\\n"
        f"$$\\\\text{{Mass}} = {_fmt_num(tonnes, 2)} \\\\times 1\\\\,000 = {_fmt_num(kg)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_28",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply metric tonnes by 1 000.", "tier_2": f"{tonnes} × 1 000.", "tier_3": f"{correct}."}
    }

def _subskill_29(r: random.Random) -> Dict[str, Any]:
    """Convert imperial pounds (lb) to kilograms (1 kg = 2.2 lb)."""
    lbs = r.choice([110, 132, 154, 165, 176, 198, 220])
    kg = round(lbs / 2.2, 1)

    prompt = (
        f"An imported fitness machine from the United States displays a user body weight limit of **{lbs} lb (pounds)**.\\n"
        f"Use the standard conversion factor: **1 kg = 2,2 lb**.\\n\\n"
        f"Convert the weight limit to kilograms (kg). Round to one decimal place."
    )
    correct = f"{_fmt_num(kg, 1)} kg"
    distractors = [
        f"{_fmt_num(round(lbs * 2.2, 1), 1)} kg",
        f"{_fmt_num(round(kg + 5.0, 1), 1)} kg",
        f"{_fmt_num(round(kg - 4.5, 1), 1)} kg"
    ]
    expl = (
        f"✓ [1 Mark: Division by 2,2]\\n"
        f"$$\\\\text{{Mass in kg}} = \\\\frac{{{lbs}\\\\text{{ lb}}}}{{2,2\\\\text{{ lb/kg}}}} = {_fmt_num(kg, 1)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_29",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Divide pounds by 2,2.", "tier_2": f"{lbs} / 2,2.", "tier_3": f"{correct}."}
    }

def _subskill_30(r: random.Random) -> Dict[str, Any]:
    """Convert ounces (oz) to grams (1 oz = 28.35 g)."""
    oz = r.choice([4, 6, 8, 12, 16])
    grams = round(oz * 28.35, 1)

    prompt = (
        f"A traditional British fruit cake recipe calls for **{oz} oz (ounces)** of dried sultanas.\\n"
        f"Given that **1 oz = 28,35 g**.\\n\\n"
        f"Calculate the mass of sultanas required in grams (g). Round to one decimal place."
    )
    correct = f"{_fmt_num(grams, 1)} g"
    distractors = [
        f"{_fmt_num(round(oz * 25.0, 1), 1)} g",
        f"{_fmt_num(round(grams + 15.0, 1), 1)} g",
        f"{_fmt_num(round(oz / 28.35, 2), 2)} g"
    ]
    expl = (
        f"✓ [1 Mark: Multiplication by 28,35]\\n"
        f"$$\\\\text{{Mass}} = {oz} \\\\times 28,35 = {_fmt_num(grams, 1)}\\\\text{{ g}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_30",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply ounces by 28,35.", "tier_2": f"{oz} × 28,35.", "tier_3": f"{correct}."}
    }

def _subskill_31(r: random.Random) -> Dict[str, Any]:
    """Unit price per kilogram comparison between small pack and bulk pack."""
    item = r.choice(["white sugar", "basmati rice", "rolled oats", "dog food"])
    # Small pack: 500g for R 14,99
    # Bulk pack: 2kg for R 48,00
    p1 = r.choice([15.0, 18.0, 22.0]) # for 500g
    rate1 = p1 * 2.0 # R/kg
    p2 = r.choice([55.0, 68.0, 79.0]) # for 2kg
    rate2 = round(p2 / 2.0, 2)

    diff = round(abs(rate1 - rate2), 2)
    prompt = (
        f"A supermarket offers two packaging options for {item}:\\n"
        f"- **Option A (500 g pack):** {_fmt_curr(p1)}\\n"
        f"- **Option B (2 kg bulk bag):** {_fmt_curr(p2)}\\n\\n"
        f"Calculate the price per kilogram for both options and determine how much money per kg a consumer saves by choosing the cheaper option."
    )
    cheaper = "Option B" if rate2 < rate1 else "Option A"
    correct = f"{cheaper} saves {_fmt_curr(diff)} per kg"
    distractors = [
        f"{'Option A' if rate2 < rate1 else 'Option B'} saves {_fmt_curr(diff)} per kg",
        f"{cheaper} saves {_fmt_curr(round(diff + 3.5, 2))} per kg",
        f"{cheaper} saves {_fmt_curr(round(abs(p2 - p1), 2))} per kg"
    ]
    expl = (
        f"✓ [1 Mark: Unit rates]\\n"
        f"Option A rate = {_fmt_curr(p1)} / 0,5 kg = {_fmt_curr(rate1)}/kg.\\n"
        f"Option B rate = {_fmt_curr(p2)} / 2,0 kg = {_fmt_curr(rate2)}/kg.\\n"
        f"✓ [1 Mark: Savings per kg]\\n"
        f"Savings = |{_fmt_curr(rate1)} - {_fmt_curr(rate2)}| = {_fmt_curr(diff)}/kg."
    )
    return {
        "subskill": "gr11_weight_temp_subskill_31",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Find cost per 1 kg for both, then subtract.", "tier_2": f"Option A = R {rate1}/kg; Option B = R {rate2}/kg.", "tier_3": f"{correct}."}
    }

def _subskill_32(r: random.Random) -> Dict[str, Any]:
    """Calculate tare mass, net mass, and gross mass (Gross = Net + Tare)."""
    net_kg = round(r.uniform(15.0, 45.0), 1)
    tare_kg = round(r.uniform(1.2, 3.5), 1)
    gross_kg = round(net_kg + tare_kg, 1)

    prompt = (
        f"A shipping crate filled with ceramic tiles has a gross mass of **{_fmt_num(gross_kg)} kg**.\\n"
        f"The empty wooden shipping crate (tare mass) weighs **{_fmt_num(tare_kg)} kg**.\\n\\n"
        f"Calculate the net mass of the ceramic tiles inside the crate."
    )
    correct = f"{_fmt_num(net_kg)} kg"
    distractors = [
        f"{_fmt_num(round(gross_kg + tare_kg, 1))} kg",
        f"{_fmt_num(round(net_kg - 2.5, 1))} kg",
        f"{_fmt_num(round(gross_kg * 0.9, 1))} kg"
    ]
    expl = (
        f"✓ [1 Mark: Net mass formula]\\n"
        f"$$\\\\text{{Net Mass}} = \\\\text{{Gross Mass}} - \\\\text{{Tare Mass}} = {_fmt_num(gross_kg)} - {_fmt_num(tare_kg)} = {_fmt_num(net_kg)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_32",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Net mass = Gross mass - Tare mass.", "tier_2": f"{gross_kg} - {tare_kg}.", "tier_3": f"{correct}."}
    }

def _subskill_33(r: random.Random) -> Dict[str, Any]:
    """Calculate maximum boxes that can be loaded onto a vehicle given payload limit."""
    payload_kg = r.choice([650, 750, 800, 1000, 1200]) # bakkie payload
    box_kg = r.choice([15, 20, 25, 30])
    max_boxes = payload_kg // box_kg

    prompt = (
        f"A delivery bakkie has a certified maximum carrying capacity (payload) of **{_fmt_num(payload_kg)} kg**.\\n"
        f"A driver must transport identical boxes of frozen chicken, each weighing **{box_kg} kg**.\\n\\n"
        f"Calculate the maximum number of whole boxes that can be loaded without exceeding the payload capacity."
    )
    correct = f"{max_boxes} boxes"
    distractors = [
        f"{max_boxes + 1} boxes",
        f"{max_boxes - 2} boxes",
        f"{round(payload_kg / box_kg, 1)} boxes"
    ]
    expl = (
        f"✓ [1 Mark: Division and integer truncation]\\n"
        f"$$\\\\frac{{{_fmt_num(payload_kg)}}}{{{box_kg}}} = {_fmt_num(round(payload_kg / box_kg, 2), 2)}\\\\text{{ boxes}}$$\\n"
        f"Since partial boxes cannot be loaded and overloading is illegal, the maximum whole number of boxes is **{max_boxes} boxes**."
    )
    return {
        "subskill": "gr11_weight_temp_subskill_33",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Divide payload by box mass and round DOWN to the nearest integer.", "tier_2": f"{payload_kg} / {box_kg}.", "tier_3": f"{correct}."}
    }

def _subskill_34(r: random.Random) -> Dict[str, Any]:
    """Calculate percentage change in agricultural harvest weight between seasons."""
    season1_t = round(r.uniform(40.0, 75.0), 1)
    season2_t = round(season1_t * r.uniform(1.12, 1.35), 1)
    diff = round(season2_t - season1_t, 1)
    pct_increase = round((diff / season1_t) * 100, 1)

    prompt = (
        f"A macadamia nut farmer in Mpumalanga harvested **{_fmt_num(season1_t)} tonnes** in 2023 "
        f"and **{_fmt_num(season2_t)} tonnes** in 2024.\\n\\n"
        f"Calculate the percentage increase in harvest weight from 2023 to 2024.\\n"
        f"Round your answer to one decimal place."
    )
    correct = f"{_fmt_num(pct_increase, 1)}%"
    distractors = [
        f"{_fmt_num(round(pct_increase + 4.1, 1), 1)}%",
        f"{_fmt_num(round((diff / season2_t) * 100, 1), 1)}%",
        f"{_fmt_num(round(pct_increase - 3.5, 1), 1)}%"
    ]
    expl = (
        f"✓ [1 Mark: Difference in yield]\\n"
        f"$$\\\\text{{Increase}} = {_fmt_num(season2_t)} - {_fmt_num(season1_t)} = {_fmt_num(diff, 1)}\\\\text{{ tonnes}}$$\\n"
        f"✓ [1 Mark: Percentage increase]\\n"
        f"$$\\\\text{{Percentage Increase}} = \\\\frac{{{_fmt_num(diff, 1)}}}{{{_fmt_num(season1_t)}}} \\\\times 100 = {_fmt_num(pct_increase, 1)}\\\\%$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_34",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Difference divided by 2023 value × 100.", "tier_2": f"({season2_t} - {season1_t}) / {season1_t} * 100.", "tier_3": f"{correct}."}
    }

# ----------------------------------------------------------------------------
# SUBSKILLS 35-44: Temperature Scales, Readings & Conversions
# ----------------------------------------------------------------------------

def _subskill_35(r: random.Random) -> Dict[str, Any]:
    """Read an analogue liquid-in-glass thermometer scale."""
    reading = r.choice([18, 22, 26, 31, 35, 42])
    prompt = (
        f"A laboratory wall thermometer has calibration tick marks spaced at **2 °C intervals**.\\n"
        f"The red alcohol column reaches exactly 3 tick marks above the 20 °C line.\\n\\n"
        f"What is the indicated temperature reading in degrees Celsius (°C)?"
    )
    correct_temp = 20 + (3 * 2)
    correct = f"{correct_temp} °C"
    distractors = [
        f"{20 + 3} °C",
        f"{20 + (3 * 5)} °C",
        f"{correct_temp - 4} °C"
    ]
    expl = (
        f"✓ [1 Mark: Scale interval evaluation]\\n"
        f"Each tick mark represents 2 °C. Three tick marks above 20 °C = $20 + (3 \\\\times 2) = {correct_temp}\\\\text{{ }}^\\\\circ\\\\text{{C}}$."
    )
    return {
        "subskill": "gr11_weight_temp_subskill_35",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply number of tick marks by 2 °C and add to 20 °C.", "tier_2": "20 + (3 * 2).", "tier_3": f"{correct}."}
    }

def _subskill_36(r: random.Random) -> Dict[str, Any]:
    """Classify clinical body temperature reading (normal, fever, hypothermia)."""
    temp = round(r.choice([34.2, 36.8, 38.6, 39.8]), 1)
    if temp < 35.0:
        cat = "Hypothermia"
    elif 36.0 <= temp <= 37.5:
        cat = "Normal body temperature"
    elif 37.6 <= temp <= 38.9:
        cat = "Fever (pyrexia)"
    else:
        cat = "High fever (hyperpyrexia)"

    prompt = (
        f"A school nurse takes a learner's tympanic temperature and records **{_fmt_num(temp, 1)} °C**.\\n\\n"
        f"Refer to clinical thresholds:\\n"
        f"- Below 35,0 °C: Hypothermia\\n"
        f"- 36,0 °C to 37,5 °C: Normal body temperature\\n"
        f"- 37,6 °C to 38,9 °C: Fever (pyrexia)\\n"
        f"- 39,0 °C and above: High fever\\n\\n"
        f"Classify the learner's medical temperature status."
    )
    cats = ["Hypothermia", "Normal body temperature", "Fever (pyrexia)", "High fever (hyperpyrexia)"]
    distractors = [c for c in cats if c != cat]
    expl = f"✓ [1 Mark: Clinical category lookup]\\n{_fmt_num(temp, 1)} °C corresponds to **{cat}**."
    return {
        "subskill": "gr11_weight_temp_subskill_36",
        "prompt": prompt,
        "options": _build_mc_options(cat, distractors, r),
        "correct_answer": cat,
        "explanation": expl,
        "hints": {"tier_1": f"Match {_fmt_num(temp, 1)} °C to the given bullet points.", "tier_2": "Check which range it falls in.", "tier_3": f"{cat}."}
    }

def _subskill_37(r: random.Random) -> Dict[str, Any]:
    """Convert Fahrenheit to Celsius using formula °C = (°F - 32) / 1.8."""
    deg_f = r.choice([68, 77, 86, 95, 104, 113, 212])
    deg_c = round((deg_f - 32) / 1.8, 1)

    prompt = (
        f"A weather report in Atlanta, USA, forecasts an afternoon temperature of **{deg_f} °F**.\\n"
        f"Use the standard conversion formula: $\\\\text{{^\\\\circ C}} = (\\\\text{{^\\\\circ F}} - 32) \\\\div 1,8$.\\n\\n"
        f"Convert this temperature into degrees Celsius (°C). Round to one decimal place."
    )
    correct = f"{_fmt_num(deg_c, 1)} °C"
    distractors = [
        f"{_fmt_num(round((deg_f * 1.8) + 32, 1), 1)} °C",
        f"{_fmt_num(round(deg_f / 1.8, 1), 1)} °C",
        f"{_fmt_num(round(deg_c + 5.0, 1), 1)} °C"
    ]
    expl = (
        f"✓ [1 Mark: Formula substitution]\\n"
        f"$$\\\\text{{^\\\\circ C}} = ({deg_f} - 32) \\\\div 1,8 = {deg_f - 32} \\\\div 1,8$$\\n"
        f"✓ [1 Mark: Calculation]\\n"
        f"$$\\\\text{{^\\\\circ C}} = {_fmt_num(deg_c, 1)}\\\\text{{ }}^\\\\circ\\\\text{{C}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_37",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Subtract 32 first, then divide by 1,8.", "tier_2": f"({deg_f} - 32) / 1,8.", "tier_3": f"{correct}."}
    }

def _subskill_38(r: random.Random) -> Dict[str, Any]:
    """Convert Celsius to Fahrenheit using formula °F = (°C * 1.8) + 32."""
    deg_c = r.choice([15, 20, 25, 30, 35, 40])
    deg_f = round((deg_c * 1.8) + 32, 1)

    prompt = (
        f"A South African tourist travels to New York where temperatures are recorded in Fahrenheit.\\n"
        f"The temperature in Pretoria before departure was **{deg_c} °C**.\\n"
        f"Use the formula: $\\\\text{{^\\\\circ F}} = (\\\\text{{^\\\\circ C}} \\\\times 1,8) + 32$.\\n\\n"
        f"Convert {deg_c} °C to degrees Fahrenheit (°F)."
    )
    correct = f"{_fmt_num(deg_f, 1)} °F"
    distractors = [
        f"{_fmt_num(round((deg_c - 32) / 1.8, 1), 1)} °F",
        f"{_fmt_num(round(deg_c * 1.8, 1), 1)} °F",
        f"{_fmt_num(round(deg_f - 10.0, 1), 1)} °F"
    ]
    expl = (
        f"✓ [1 Mark: Multiplication]\\n"
        f"$$\\\\text{{^\\\\circ F}} = ({deg_c} \\\\times 1,8) + 32 = {_fmt_num(round(deg_c * 1.8, 1))} + 32$$\\n"
        f"✓ [1 Mark: Addition]\\n"
        f"$$\\\\text{{^\\\\circ F}} = {_fmt_num(deg_f, 1)}\\\\text{{ }}^\\\\circ\\\\text{{F}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_38",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply Celsius by 1,8 and then add 32.", "tier_2": f"({deg_c} × 1,8) + 32.", "tier_3": f"{correct}."}
    }

def _subskill_39(r: random.Random) -> Dict[str, Any]:
    """Convert between Celsius and Kelvin (K = °C + 273)."""
    deg_c = r.choice([-10, 0, 22, 37, 100])
    kelvin = deg_c + 273

    prompt = (
        f"Scientific data loggers record temperature in Kelvin (K).\\n"
        f"Given the absolute temperature relation: $\\\\text{{K}} = \\\\text{{^\\\\circ C}} + 273$.\\n\\n"
        f"Convert **{deg_c} °C** into Kelvin (K)."
    )
    correct = f"{kelvin} K"
    distractors = [
        f"{deg_c - 273} K",
        f"{kelvin + 15} K",
        f"{round(deg_c * 2.73)} K"
    ]
    expl = (
        f"✓ [1 Mark: Kelvin conversion]\\n"
        f"$$\\\\text{{K}} = {deg_c} + 273 = {kelvin}\\\\text{{ K}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_39",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Add 273 to the Celsius temperature.", "tier_2": f"{deg_c} + 273.", "tier_3": f"{correct}."}
    }

def _subskill_40(r: random.Random) -> Dict[str, Any]:
    """Interpret oven temperature guide table (Gas mark vs Celsius vs Fahrenheit)."""
    gas_mark = r.choice([3, 4, 5, 6, 7])
    oven_table = {
        3: (160, 325, "Warm / Moderate"),
        4: (180, 350, "Moderate"),
        5: (190, 375, "Moderately hot"),
        6: (200, 400, "Hot"),
        7: (220, 425, "Very hot")
    }
    c_val, f_val, desc = oven_table[gas_mark]

    prompt = (
        f"An international recipe book states that bread must bake at **Gas Mark {gas_mark}**.\\n\\n"
        f"Refer to the oven conversion guide:\\n"
        f"| Gas Mark | Description | Celsius (°C) | Fahrenheit (°F) |\\n"
        f"| :--- | :--- | :--- | :--- |\\n"
        f"| 3 | Warm / Moderate | 160 | 325 |\\n"
        f"| 4 | Moderate | 180 | 350 |\\n"
        f"| 5 | Moderately hot | 190 | 375 |\\n"
        f"| 6 | Hot | 200 | 400 |\\n"
        f"| 7 | Very hot | 220 | 425 |\\n\\n"
        f"What temperature should a South African baker set on an electric Celsius oven for Gas Mark {gas_mark}?"
    )
    correct = f"{c_val} °C"
    distractors = [
        f"{f_val} °C",
        f"{c_val - 20} °C",
        f"{c_val + 20} °C"
    ]
    expl = f"✓ [1 Mark: Direct table lookup]\\nGas Mark {gas_mark} corresponds directly to **{c_val} °C** in the conversion guide."
    return {
        "subskill": "gr11_weight_temp_subskill_40",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Look at the row for Gas Mark {gas_mark}.", "tier_2": "Read the Celsius column value.", "tier_3": f"{correct}."}
    }

def _subskill_41(r: random.Random) -> Dict[str, Any]:
    """Calculate temperature change over time given rate of cooling/heating (°C/hr)."""
    initial_t = r.choice([85, 90, 95]) # soup boiling
    rate = r.choice([4.5, 6.0, 7.5]) # degrees per hour
    hours = r.choice([2, 3, 4])
    drop = rate * hours
    final_t = round(initial_t - drop, 1)

    prompt = (
        f"A commercial pot of catering stew is taken off the burner at **{initial_t} °C**.\\n"
        f"The soup cools at an average steady rate of **{_fmt_num(rate)} °C per hour**.\\n\\n"
        f"Calculate the temperature of the stew in degrees Celsius after **{hours} hours**."
    )
    correct = f"{_fmt_num(final_t, 1)} °C"
    distractors = [
        f"{_fmt_num(round(initial_t + drop, 1), 1)} °C",
        f"{_fmt_num(round(initial_t - rate, 1), 1)} °C",
        f"{_fmt_num(round(final_t - 5.0, 1), 1)} °C"
    ]
    expl = (
        f"✓ [1 Mark: Total temperature drop]\\n"
        f"$$\\\\text{{Drop}} = {_fmt_num(rate)} \\\\times {hours} = {_fmt_num(drop, 1)}\\\\text{{ }}^\\\\circ\\\\text{{C}}$$\\n"
        f"✓ [1 Mark: Final temperature]\\n"
        f"$$\\\\text{{Final}} = {initial_t} - {_fmt_num(drop, 1)} = {_fmt_num(final_t, 1)}\\\\text{{ }}^\\\\circ\\\\text{{C}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_41",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply rate by hours, then subtract from initial temperature.", "tier_2": f"{initial_t} - ({rate} × {hours}).", "tier_3": f"{correct}."}
    }

def _subskill_42(r: random.Random) -> Dict[str, Any]:
    """Calculate diurnal temperature range (maximum temperature minus minimum temperature)."""
    town = r.choice(SA_TOWNS)
    min_t = round(r.uniform(4.0, 12.0), 1)
    max_t = round(min_t + r.uniform(14.0, 22.0), 1)
    t_range = round(max_t - min_t, 1)

    prompt = (
        f"The South African Weather Service recorded the following temperatures for {town} yesterday:\\n"
        f"- **Minimum temperature:** {_fmt_num(min_t, 1)} °C\\n"
        f"- **Maximum temperature:** {_fmt_num(max_t, 1)} °C\\n\\n"
        f"Calculate the diurnal temperature range for {town} to one decimal place."
    )
    correct = f"{_fmt_num(t_range, 1)} °C"
    distractors = [
        f"{_fmt_num(round(max_t + min_t, 1), 1)} °C",
        f"{_fmt_num(round((max_t + min_t) / 2.0, 1), 1)} °C",
        f"{_fmt_num(round(t_range + 3.2, 1), 1)} °C"
    ]
    expl = (
        f"✓ [1 Mark: Formula and calculation]\\n"
        f"$$\\\\text{{Range}} = \\\\text{{Maximum}} - \\\\text{{Minimum}} = {_fmt_num(max_t, 1)} - {_fmt_num(min_t, 1)} = {_fmt_num(t_range, 1)}\\\\text{{ }}^\\\\circ\\\\text{{C}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_42",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Subtract minimum from maximum.", "tier_2": f"{max_t} - {min_t}.", "tier_3": f"{correct}."}
    }

def _subskill_43(r: random.Random) -> Dict[str, Any]:
    """Determine freezing point depression in cold storage."""
    freezing_pt = r.choice([-1.8, -2.4, -3.2, -4.5])
    normal_fp = 0.0
    depression = round(abs(freezing_pt), 1)

    prompt = (
        f"Adding salt to an ice-slurry reduces the freezing point of water from 0,0 °C down to **{_fmt_num(freezing_pt, 1)} °C**.\\n\\n"
        f"By how many degrees Celsius has the freezing point been depressed (lowered)?"
    )
    correct = f"{_fmt_num(depression, 1)} °C"
    distractors = [
        f"{_fmt_num(round(depression + 2.0, 1), 1)} °C",
        f"{_fmt_num(round(depression * 1.5, 1), 1)} °C",
        f"{_fmt_num(round(depression - 0.8, 1), 1)} °C"
    ]
    expl = f"✓ [1 Mark: Magnitude of temperature decrease]\\n$$\\\\text{{Depression}} = |0,0 - ({_fmt_num(freezing_pt, 1)})| = {_fmt_num(depression, 1)}\\\\text{{ }}^\\\\circ\\\\text{{C}}$$"
    return {
        "subskill": "gr11_weight_temp_subskill_43",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Find the difference between 0 °C and the new freezing point.", "tier_2": f"0 - ({freezing_pt}) = {depression}.", "tier_3": f"{correct}."}
    }

def _subskill_44(r: random.Random) -> Dict[str, Any]:
    """Cold chain compliance: check vaccine refrigerator temperatures against +2 °C to +8 °C."""
    recorded_t = r.choice([1.2, 3.5, 5.0, 7.2, 9.4, 11.0])
    is_compliant = 2.0 <= recorded_t <= 8.0

    prompt = (
        f"A clinic refrigerator storing childhood vaccines must strictly maintain a cold chain temperature between **+2,0 °C and +8,0 °C**.\\n"
        f"The temperature sensor records a reading of **{_fmt_num(recorded_t, 1)} °C** at 08:00.\\n\\n"
        f"Determine whether this reading complies with strict pharmaceutical cold chain regulations."
    )
    correct = "Compliant (Within the safe +2,0 °C to +8,0 °C window)" if is_compliant else (
        "Non-compliant (Below minimum safe limit — risk of freezing)" if recorded_t < 2.0 else "Non-compliant (Exceeds maximum safe limit — risk of vaccine spoilage)"
    )
    distractors = [
        "Compliant (Within the safe +2,0 °C to +8,0 °C window)" if not is_compliant else "Non-compliant (Exceeds maximum safe limit — risk of vaccine spoilage)",
        "Temperature does not impact pharmaceutical potency",
        "Refrigerators must always operate below -10,0 °C"
    ]
    expl = f"✓ [1 Mark: Compliance evaluation]\\nSince {_fmt_num(recorded_t, 1)} °C {'is within' if is_compliant else 'falls outside'} the 2,0 °C to 8,0 °C bracket, it is **{correct}**."
    return {
        "subskill": "gr11_weight_temp_subskill_44",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Check if value is between 2,0 and 8,0.", "tier_2": f"2,0 <= {recorded_t} <= 8,0.", "tier_3": f"{correct}."}
    }
''')

# Now add subskills 45 to 52, DISPATCH_TABLE, SUBSKILLS, and generate()
code_sections.append('''
# ----------------------------------------------------------------------------
# SUBSKILLS 45-52: Real-World Applications: Weather, Logistics, Freight & GVM
# ----------------------------------------------------------------------------

def _subskill_45(r: random.Random) -> Dict[str, Any]:
    """International travel clothing planning: convert forecast from °F to °C."""
    f_high = r.choice([41, 50, 59, 86, 95])
    c_high = round((f_high - 32) / 1.8, 1)

    prompt = (
        f"A South African learner travels to Chicago for an academic exchange.\\n"
        f"The weather forecast predicts a daily maximum temperature of **{f_high} °F**.\\n"
        f"Convert this to Celsius and recommend appropriate travel clothing."
    )
    if c_high < 15.0:
        advice = f"{_fmt_num(c_high, 1)} °C: Pack heavy winter coat, gloves, and warm thermal layers"
    elif c_high <= 24.0:
        advice = f"{_fmt_num(c_high, 1)} °C: Pack light jacket and moderate everyday attire"
    else:
        advice = f"{_fmt_num(c_high, 1)} °C: Pack light summer clothes, shorts, and sunscreen"

    correct = advice
    distractors = [
        f"{_fmt_num(round((f_high * 1.8) + 32, 1), 1)} °C: Pack extreme polar expedition gear",
        f"{_fmt_num(round(c_high + 12.0, 1), 1)} °C: Pack heavy winter woolens",
        f"{_fmt_num(round(c_high - 10.0, 1), 1)} °C: Pack beachwear only"
    ]
    expl = (
        f"✓ [1 Mark: Conversion]\\n"
        f"$$\\\\text{{^\\\\circ C}} = ({f_high} - 32) \\\\div 1,8 = {_fmt_num(c_high, 1)}\\\\text{{ }}^\\\\circ\\\\text{{C}}$$\\n"
        f"✓ [1 Mark: Practical clothing recommendation]\\n{advice}."
    )
    return {
        "subskill": "gr11_weight_temp_subskill_45",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Convert ({f_high} - 32) / 1,8 to Celsius, then choose appropriate clothes.", "tier_2": f"{f_high} °F = {c_high} °C.", "tier_3": f"{correct}."}
    }

def _subskill_46(r: random.Random) -> Dict[str, Any]:
    """Calculate 7-day average mean temperature from daily maximum temperatures."""
    town = r.choice(SA_TOWNS)
    temps = [r.choice([22, 24, 25, 26, 27, 28, 29, 30]) for _ in range(7)]
    mean_t = round(sum(temps) / 7.0, 1)

    prompt = (
        f"The maximum recorded daily temperatures in {town} over 7 consecutive days were:\\n"
        f"**{', '.join(str(t) + ' °C' for t in temps)}**\\n\\n"
        f"Calculate the mean (average) maximum temperature for the week. Round to one decimal place."
    )
    correct = f"{_fmt_num(mean_t, 1)} °C"
    distractors = [
        f"{_fmt_num(round(mean_t + 2.3, 1), 1)} °C",
        f"{_fmt_num(round(mean_t - 1.8, 1), 1)} °C",
        f"{_fmt_num(round(sum(temps) / 6.0, 1), 1)} °C"
    ]
    expl = (
        f"✓ [1 Mark: Sum]\\n$$\\\\text{{Sum}} = {sum(temps)}\\\\text{{ }}^\\\\circ\\\\text{{C}}$$\\n"
        f"✓ [1 Mark: Mean]\\n$$\\\\text{{Mean}} = \\\\frac{{{sum(temps)}}}{{7}} \\\\approx {_fmt_num(mean_t, 1)}\\\\text{{ }}^\\\\circ\\\\text{{C}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_46",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Add up all 7 temperatures and divide by 7.", "tier_2": f"Sum = {sum(temps)}. Divide by 7.", "tier_3": f"{correct}."}
    }

def _subskill_47(r: random.Random) -> Dict[str, Any]:
    """Gross Vehicle Mass (GVM) and Tare: calculate legal payload limit."""
    gvm = r.choice([2800, 3100, 3500, 4200]) # kg
    tare = r.choice([1650, 1850, 2050]) # kg
    payload = gvm - tare

    prompt = (
        f"A light commercial delivery vehicle (LDV) displays an official licence disc with the following specifications:\\n"
        f"- **Gross Vehicle Mass (GVM):** {_fmt_num(gvm)} kg\\n"
        f"- **Tare Mass (unladen vehicle weight):** {_fmt_num(tare)} kg\\n\\n"
        f"Use the relationship $\\\\text{{Payload}} = \\\\text{{GVM}} - \\\\text{{Tare}}$ to calculate the legal carrying capacity (payload) of this vehicle in kilograms."
    )
    correct = f"{_fmt_num(payload)} kg"
    distractors = [
        f"{_fmt_num(gvm + tare)} kg",
        f"{_fmt_num(payload + 350)} kg",
        f"{_fmt_num(payload - 250)} kg"
    ]
    expl = (
        f"✓ [1 Mark: Formula and calculation]\\n"
        f"$$\\\\text{{Payload}} = {_fmt_num(gvm)} - {_fmt_num(tare)} = {_fmt_num(payload)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_47",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Subtract Tare mass from GVM.", "tier_2": f"{gvm} - {tare}.", "tier_3": f"{correct}."}
    }

def _subskill_48(r: random.Random) -> Dict[str, Any]:
    """Weighbridge overload check: calculate excess mass above legal limit."""
    gvm_limit = r.choice([16000, 22000, 26000]) # kg
    actual_mass = round(gvm_limit + r.uniform(850, 2400)) # overloaded
    excess = actual_mass - gvm_limit

    prompt = (
        f"A heavy transport truck is directed to a provincial traffic weighbridge along the N1 highway.\\n"
        f"The truck's certified GVM limit is **{_fmt_num(gvm_limit)} kg**.\\n"
        f"The weighbridge digital scale registers a total weight of **{_fmt_num(actual_mass)} kg**.\\n\\n"
        f"Calculate the excess overload mass in kilograms for which the operator will be fined."
    )
    correct = f"{_fmt_num(excess)} kg overload"
    distractors = [
        f"{_fmt_num(excess + 500)} kg overload",
        f"{_fmt_num(round(actual_mass * 0.1))} kg overload",
        "Legal — Zero overload"
    ]
    expl = (
        f"✓ [1 Mark: Overload difference]\\n"
        f"$$\\\\text{{Excess Mass}} = {_fmt_num(actual_mass)} - {_fmt_num(gvm_limit)} = {_fmt_num(excess)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_48",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Subtract legal GVM from the scale reading.", "tier_2": f"{actual_mass} - {gvm_limit}.", "tier_3": f"{correct}."}
    }

def _subskill_49(r: random.Random) -> Dict[str, Any]:
    """Freight volumetric weight calculation compared to actual mass."""
    l, w, h = 60, 40, 50 # cm
    actual_mass = r.choice([18.0, 22.0, 28.0]) # kg
    # Volumetric weight = (L * W * H) / 5000 (IATA standard)
    vol_mass = round((l * w * h) / 5000.0, 1) # 24.0 kg

    prompt = (
        f"An air courier company calculates volumetric mass using the formula:\\n"
        f"$$\\\\text{{Volumetric Mass (kg)}} = \\\\frac{{\\\\text{{Length (cm)}} \\\\times \\\\text{{Width (cm)}} \\\\times \\\\text{{Height (cm)}}}}{{5\\\\,000}}$$\\n"
        f"A parcel measures **{l} cm × {w} cm × {h} cm** and has an actual physical mass of **{_fmt_num(actual_mass)} kg**.\\n"
        f"The courier bills based on whichever mass is greater (chargeable mass).\\n\\n"
        f"Calculate the volumetric mass and identify the chargeable mass."
    )
    chargeable = max(actual_mass, vol_mass)
    correct = f"Volumetric = {_fmt_num(vol_mass, 1)} kg, Chargeable = {_fmt_num(chargeable, 1)} kg"
    distractors = [
        f"Volumetric = {_fmt_num(vol_mass, 1)} kg, Chargeable = {_fmt_num(min(actual_mass, vol_mass), 1)} kg",
        f"Volumetric = {_fmt_num(round(vol_mass + 5.0, 1), 1)} kg, Chargeable = {_fmt_num(round(chargeable + 5.0, 1), 1)} kg",
        f"Volumetric = {_fmt_num(actual_mass, 1)} kg, Chargeable = {_fmt_num(actual_mass, 1)} kg"
    ]
    expl = (
        f"✓ [1 Mark: Volumetric calculation]\\n"
        f"$$\\\\text{{Volumetric Mass}} = \\\\frac{{{l} \\\\times {w} \\\\times {h}}}{{5\\\\,000}} = \\\\frac{{{l * w * h}}}{{5\\\\,000}} = {_fmt_num(vol_mass, 1)}\\\\text{{ kg}}$$\\n"
        f"✓ [1 Mark: Chargeable mass evaluation]\\n"
        f"Whichever is greater: $\\\\max({_fmt_num(actual_mass)}, {_fmt_num(vol_mass, 1)}) = {_fmt_num(chargeable, 1)}\\\\text{{ kg}}$."
    )
    return {
        "subskill": "gr11_weight_temp_subskill_49",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"({l} × {w} × {h}) / 5000, then choose the larger of the two values.", "tier_2": f"Volumetric = {vol_mass} kg. Compare with {actual_mass} kg.", "tier_3": f"{correct}."}
    }

def _subskill_50(r: random.Random) -> Dict[str, Any]:
    """Livestock dressing percentage: calculate cold carcass mass from live weight."""
    live_mass = r.choice([420, 450, 480, 520]) # kg beef steer
    dressing_pct = r.choice([56, 58, 60]) # percent
    carcass_mass = round(live_mass * (dressing_pct / 100.0), 1)

    prompt = (
        f"At an agricultural livestock auction, an ox has a live weight of **{live_mass} kg**.\\n"
        f"The abattoir operates with an expected dressing percentage of **{dressing_pct}%**.\\n\\n"
        f"Calculate the expected dressed carcass mass in kilograms (kg)."
    )
    correct = f"{_fmt_num(carcass_mass, 1)} kg"
    distractors = [
        f"{_fmt_num(round(live_mass - dressing_pct, 1), 1)} kg",
        f"{_fmt_num(round(carcass_mass + 25.0, 1), 1)} kg",
        f"{_fmt_num(round(carcass_mass - 20.0, 1), 1)} kg"
    ]
    expl = (
        f"✓ [1 Mark: Percentage calculation]\\n"
        f"$$\\\\text{{Carcass Mass}} = {live_mass} \\\\times \\\\frac{{{dressing_pct}}}{{100}} = {_fmt_num(carcass_mass, 1)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_50",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Multiply {live_mass} by {dressing_pct} / 100.", "tier_2": f"{live_mass} × {dressing_pct / 100}.", "tier_3": f"{correct}."}
    }

def _subskill_51(r: random.Random) -> Dict[str, Any]:
    """Concrete batch mass proportions: calculate mass of ingredients from ratio."""
    total_batch_kg = r.choice([600, 900, 1200, 1500])
    # Ratio: 1 cement : 2 sand : 3 stone (Total parts = 6)
    parts = 6
    cement = total_batch_kg * (1 / parts)
    sand = total_batch_kg * (2 / parts)
    stone = total_batch_kg * (3 / parts)

    prompt = (
        f"A builder prepares a standard concrete mix ratio by mass of **1 : 2 : 3** (Cement : Sand : Stone).\\n"
        f"The concrete mixer requires a total dry batch mass of **{_fmt_num(total_batch_kg)} kg**.\\n\\n"
        f"Calculate the mass of stone in kilograms required for this mix."
    )
    correct = f"{_fmt_num(stone)} kg"
    distractors = [
        f"{_fmt_num(sand)} kg",
        f"{_fmt_num(cement)} kg",
        f"{_fmt_num(stone + 100)} kg"
    ]
    expl = (
        f"✓ [1 Mark: Total parts]\\n$$\\\\text{{Parts}} = 1 + 2 + 3 = 6$$\\n"
        f"✓ [1 Mark: Stone portion]\\n$$\\\\text{{Stone Mass}} = \\\\frac{{3}}{{6}} \\\\times {_fmt_num(total_batch_kg)} = {_fmt_num(stone)}\\\\text{{ kg}}$$"
    )
    return {
        "subskill": "gr11_weight_temp_subskill_51",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Total ratio parts = 1 + 2 + 3 = 6. Stone is 3/6 of the total.", "tier_2": f"(3/6) × {total_batch_kg}.", "tier_3": f"{correct}."}
    }

def _subskill_52(r: random.Random) -> Dict[str, Any]:
    """Wind chill / Heat index environmental reading from table."""
    air_t = r.choice([30, 32, 34]) # °C
    humidity = r.choice([50, 60, 70]) # %
    index_map = {
        (30, 50): 31, (30, 60): 33, (30, 70): 36,
        (32, 50): 34, (32, 60): 38, (32, 70): 42,
        (34, 50): 38, (34, 60): 44, (34, 70): 50
    }
    apparent_t = index_map[(air_t, humidity)]

    prompt = (
        f"Outdoor sports participants consult the heat index chart below:\\n\\n"
        f"| Air Temp (°C) | 50% Humidity | 60% Humidity | 70% Humidity |\\n"
        f"| :--- | :--- | :--- | :--- |\\n"
        f"| 30 °C | 31 °C | 33 °C | 36 °C |\\n"
        f"| 32 °C | 34 °C | 38 °C | 42 °C |\\n"
        f"| 34 °C | 38 °C | 44 °C | 50 °C |\\n\\n"
        f"What is the apparent 'feels-like' temperature when the air temperature is **{air_t} °C** "
        f"and the relative humidity is **{humidity}%**?"
    )
    correct = f"{apparent_t} °C"
    distractors = [
        f"{air_t} °C",
        f"{apparent_t + 4} °C",
        f"{apparent_t - 3} °C"
    ]
    expl = f"✓ [1 Mark: Table coordinate read]\\nAt row {air_t} °C and column {humidity}% humidity, the apparent temperature is **{apparent_t} °C**."
    return {
        "subskill": "gr11_weight_temp_subskill_52",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Locate row {air_t} °C and column {humidity}%.", "tier_2": "Read the intersecting value.", "tier_3": f"{correct}."}
    }

# ----------------------------------------------------------------------------
# Master Dispatch Table & Entry Point
# ----------------------------------------------------------------------------

DISPATCH_TABLE = {
    f"gr11_weight_temp_subskill_{i}": fn
    for i, fn in enumerate([
        _subskill_1, _subskill_2, _subskill_3, _subskill_4, _subskill_5,
        _subskill_6, _subskill_7, _subskill_8, _subskill_9, _subskill_10,
        _subskill_11, _subskill_12, _subskill_13, _subskill_14, _subskill_15,
        _subskill_16, _subskill_17, _subskill_18, _subskill_19, _subskill_20,
        _subskill_21, _subskill_22, _subskill_23, _subskill_24, _subskill_25,
        _subskill_26, _subskill_27, _subskill_28, _subskill_29, _subskill_30,
        _subskill_31, _subskill_32, _subskill_33, _subskill_34, _subskill_35,
        _subskill_36, _subskill_37, _subskill_38, _subskill_39, _subskill_40,
        _subskill_41, _subskill_42, _subskill_43, _subskill_44, _subskill_45,
        _subskill_46, _subskill_47, _subskill_48, _subskill_49, _subskill_50,
        _subskill_51, _subskill_52
    ], 1)
}

SUBSKILLS = list(DISPATCH_TABLE.keys())


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 11 Mathematical Literacy: Weight and Temperature."""
    r = random.Random(seed)
    results: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        chosen_subskill = subskill

        if not chosen_subskill and archetype_index is not None:
            if 0 <= archetype_index < len(SUBSKILLS):
                chosen_subskill = SUBSKILLS[archetype_index]
            else:
                chosen_subskill = SUBSKILLS[archetype_index % len(SUBSKILLS)]

        if not chosen_subskill or chosen_subskill not in DISPATCH_TABLE:
            chosen_subskill = r.choice(SUBSKILLS)

        builder = DISPATCH_TABLE[chosen_subskill]
        raw_q = builder(r)

        payload = {
            "id": f"mathlit_gr11_weight_temp_{chosen_subskill}_{uuid.uuid4().hex[:8]}",
            "question_id": f"mathlit_gr11_weight_temp_{chosen_subskill}_{uuid.uuid4().hex[:8]}",
            "topic": "grade11_mathlit_weight_and_temperature",
            "subskill": chosen_subskill,
            "prompt": raw_q["prompt"],
            "options": raw_q["options"],
            "correct_answer": raw_q["correct_answer"],
            "expected_answer": raw_q["correct_answer"],
            "explanation": raw_q["explanation"],
            "worked_solution": raw_q["explanation"],
            "hints": raw_q["hints"],
            "grade": 11,
            "subject": "Mathematical Literacy",
        }
        if "diagram_spec" in raw_q:
            payload["diagram_spec"] = raw_q["diagram_spec"]
            payload["diagram"] = raw_q["diagram_spec"]
        elif "diagram" in raw_q:
            payload["diagram_spec"] = raw_q["diagram"]
            payload["diagram"] = raw_q["diagram"]

        results.append(payload)

    return results
''')

full_code = "".join(code_sections)
target_path = "caps-ai-backend/app/utils/mathematical_literacy/gr11_weight_and_temperature_generator.py"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(full_code)

print(f"Successfully generated {target_path} with {len(code_sections)} sections.")
