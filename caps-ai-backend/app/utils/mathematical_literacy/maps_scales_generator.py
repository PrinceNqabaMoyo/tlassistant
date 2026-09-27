"""Grade 10–12 Mathematical Literacy — Maps, Plans & Scale Conversions (Deterministic 6-Pillar Generator).
Covers 1:50 000 topographic map scales, distance conversion (cm to km), travel time, fuel costs,
and architectural floor plan dimensioning (Paper 2, Term 2).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


SA_TOWNS = [
    ("Polokwane", "Mokopane", 58),
    ("Mbombela", "White River", 20),
    ("Pietermaritzburg", "Howick", 24),
    ("Bloemfontein", "Brandfort", 54),
    ("George", "Knysna", 62),
    ("Kimberley", "Barkly West", 35),
    ("Mahikeng", "Mmabatho", 12),
]


# --------------------------------------------------------------------------- #
# Sub-Drill: Scale Ratio Direct Conversion (cm to km)
# --------------------------------------------------------------------------- #
def _build_scale_ratio_drill(r: random.Random) -> Dict[str, Any]:
    scale_type = r.choice([
        ("1:50 000 topographic map", 50000, 0.5),    # 1 cm = 0.5 km
        ("1:10 000 orthophoto map", 10000, 0.1),     # 1 cm = 0.1 km
        ("1:250 000 regional map", 250000, 2.5),    # 1 cm = 2.5 km
    ])
    map_desc, scale_denom, km_per_cm = scale_type

    cm_measured = r.choice([3.2, 4.5, 6.0, 7.8, 8.4, 11.2, 14.0])
    actual_km = round(cm_measured * km_per_cm, 2)

    prompt = (
        f"A learner measures a straight-line distance of **{_fmt_sa(cm_measured)}\\text{{ cm}}** on a "
        f"**{map_desc}**.\n\n"
        f"1. Explain what the scale ratio $1 : {scale_denom:,}$ means in words.\n"
        f"2. Calculate the actual ground distance in **kilometres (km)**."
    ).replace(",", " ")

    ans_latex = (
        rf"1\text{{ cm on map}} = {scale_denom:,}\text{{ cm on ground}}, \quad "
        rf"\text{{Distance}} = {_fmt_sa(cm_measured)}\text{{ cm}} \times {_fmt_sa(km_per_cm)}\text{{ km/cm}} = {_fmt_sa(actual_km)}\text{{ km}}"
    ).replace(",", " ")

    sample_answer = (
        f"1. Scale Meaning:\n"
        f"   One unit of measurement on the map represents {scale_denom:,} of the same units on the ground.\n"
        f"   (e.g. $1\\text{{ cm on map}} = {scale_denom:,}\\text{{ cm on the ground}}$).\n\n"
        f"2. Distance in Kilometres:\n"
        f"   $\\text{{Ground Distance}} = {_fmt_sa(cm_measured)}\\text{{ cm}} \\times {scale_denom:,} = {int(cm_measured * scale_denom):,}\\text{{ cm}}$\n"
        f"   Convert $\\text{{cm}} \\to \\text{{m}}$: $\\div 100$\n"
        f"   Convert $\\text{{m}} \\to \\text{{km}}$: $\\div 1\\,000$\n"
        f"   $$\\text{{Distance}} = \\frac{{{int(cm_measured * scale_denom):,}}}{{100\\,000}} = {_fmt_sa(actual_km)}\\text{{ km}}$$"
    ).replace(",", " ")

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": f"Correct meaning of ratio scale 1:{scale_denom}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Multiply measured cm by scale factor {scale_denom}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate conversion to km: {_fmt_sa(actual_km)} km", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "confused_cm_to_km_factor", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Multiply the measured length in cm by the scale denominator.",
        "tier_2": "Convert cm to km: divide by 100 000 (100 cm in a m, 1 000 m in a km).",
        "tier_3": f"Actual Distance = {_fmt_sa(cm_measured)} x {scale_denom:,} / 100 000 = {_fmt_sa(actual_km)} km.".replace(",", " "),
    }

    return {
        "id": f"mathlit_scale_{r.randint(100000, 999999)}",
        "question_id": f"mathlit_scale_{r.randint(100000, 999999)}",
        "topic": "mathematical_literacy_maps_scales",
        "subskill": "scale_ratio_conversion_elementary",
        "learning_objective_id": "mathlit_scale_ratio",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["confused_cm_to_km_conversion_factor", "inverted_scale_ratio"],
        "keywords": ["map scale", "topographic map", "ratio scale", "kilometres", "distance conversion"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 3,
        "mode": "elementary_scale_ratio_conversion",
        "difficulty": "easy",
        "marks": 3,
    }


# --------------------------------------------------------------------------- #
# Sub-Drill: Travel Time Calculation
# --------------------------------------------------------------------------- #
def _build_travel_time_drill(r: random.Random) -> Dict[str, Any]:
    town1, town2, _ = r.choice(SA_TOWNS)
    distance_km = r.choice([45, 60, 75, 90, 110, 135, 150, 180])
    speed_kmh = r.choice([60, 80, 90, 100, 120])

    total_hours = distance_km / speed_kmh
    hrs = int(total_hours)
    mins = int(round((total_hours - hrs) * 60))

    time_str = f"{hrs} hour{'s' if hrs != 1 else ''} and {mins} minute{'s' if mins != 1 else ''}"

    prompt = (
        f"A delivery vehicle travels between **{town1}** and **{town2}**, covering a road distance "
        f"of **{distance_km}\\text{{ km}}** at a constant average speed of **{speed_kmh}\\text{{ km/h}}**.\n\n"
        f"1. Write down the formula relating distance, speed, and time.\n"
        f"2. Calculate the travel time in hours and minutes."
    )

    ans_latex = rf"\text{{Time}} = \frac{{{distance_km}\text{{ km}}}}{{{speed_kmh}\text{{ km/h}}}} = {hrs}\text{{ h }} {mins}\text{{ min}}"

    sample_answer = (
        f"1. Formula: $\\text{{Time}} = \\frac{{\\text{{Distance}}}}{{\\text{{Speed}}}}$\n\n"
        f"2. Calculation:\n"
        f"   $$\\text{{Time}} = \\frac{{{distance_km}\\text{{ km}}}}{{{speed_kmh}\\text{{ km/h}}}} = {_fmt_sa(total_hours, 2)}\\text{{ hours}}$$\n"
        f"   Convert decimal hours to minutes: $0{_fmt_sa(total_hours - hrs, 2)[1:]} \\times 60 = {mins}\\text{{ minutes}}$\n"
        f"   Total Travel Time: **{time_str}**"
    )

    marking_schema = {
        "total_marks": 3,
        "marking_points": [
            {"id": "mp1", "desc": "Formula: Time = Distance / Speed", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Substitution: {distance_km} / {speed_kmh} = {total_hours:.2f} hours", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Convert decimal to minutes: {time_str}", "marks": 1, "editable": True},
        ],
        "deductions": [{"rule": "treated_decimal_as_minutes", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "Formula: Time = Distance / Speed.",
        "tier_2": "Do NOT write decimal hours directly as minutes (e.g. 1,5 hours is NOT 1 hour 5 minutes; it is 1 hour 30 minutes).",
        "tier_3": f"Time = {distance_km} / {speed_kmh} = {hrs} h {mins} min.",
    }

    return {
        "id": f"mathlit_time_{r.randint(100000, 999999)}",
        "question_id": f"mathlit_time_{r.randint(100000, 999999)}",
        "topic": "mathematical_literacy_maps_scales",
        "subskill": "travel_time_elementary",
        "learning_objective_id": "mathlit_travel_time",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": ["treated_decimal_as_minutes", "inverted_speed_distance_formula"],
        "keywords": ["travel time", "average speed", "hours and minutes", "decimal conversion"],
        "term": 2,
        "caps_weight_percent": 20,
        "suggested_duration_mins": 3,
        "mode": "elementary_travel_time_calc",
        "difficulty": "medium",
        "marks": 3,
    }


# --------------------------------------------------------------------------- #
# Compound: Topographic Map Scale, Travel Time & Fuel Cost (8 Marks Exam Standard)
# --------------------------------------------------------------------------- #
def _build_compound_maps_scales(r: random.Random) -> Dict[str, Any]:
    town1, town2, _ = r.choice(SA_TOWNS)
    # Measured distance on 1:50 000 map (1 cm = 0.5 km)
    measured_cm = r.choice([7.2, 8.4, 9.6, 10.8, 12.0, 14.4])
    ground_km = round(measured_cm * 0.5, 2)

    avg_speed = r.choice([60, 80, 90, 100])
    total_hours = ground_km / avg_speed
    hrs = int(total_hours)
    mins = int(round((total_hours - hrs) * 60))

    # Fuel consumption: L / 100km
    litres_per_100km = r.choice([6.5, 7.2, 8.0, 8.5])
    fuel_price_per_l = r.choice([22.50, 23.80, 24.20, 25.10])
    fuel_used = round((ground_km / 100) * litres_per_100km, 2)
    fuel_cost = round(fuel_used * fuel_price_per_l, 2)

    prompt = (
        f"A tourist consults an official **1 : 50 000 South African Topographic Map** to plan a road trip "
        f"from **{town1}** to **{town2}**.\n\n"
        f"Using a ruler, the straight-line distance measured on the map is **{_fmt_sa(measured_cm)}\\text{{ cm}}**.\n\n"
        f"1. State the ground distance in kilometres that is represented by $1\\text{{ cm}}$ on a $1 : 50\\ 000$ map.\n"
        f"2. Calculate the actual ground distance between {town1} and {town2} in kilometres (km).\n"
        f"3. If the tourist drives at an average speed of **{avg_speed}\\text{{ km/h}}**, calculate the estimated travel time in **hours and minutes**.\n"
        f"4. The tourist's car has an average fuel consumption of **{_fmt_sa(litres_per_100km)}\\text{{ litres per 100 km}}**. "
        f"If petrol costs **R{_fmt_sa(fuel_price_per_l)} per litre**, calculate the total fuel cost for the trip."
    )

    sample_answer = (
        f"1. Scale factor:\n"
        f"   $$1\\text{{ cm on map}} = 50\\ 000\\text{{ cm on ground}} = \\frac{{50\\ 000}}{{100\\ 000}} = 0{{,}}5\\text{{ km}}$$\n\n"
        f"2. Actual Ground Distance:\n"
        f"   $$\\text{{Distance}} = {_fmt_sa(measured_cm)}\\text{{ cm}} \\times 0{{,}}5\\text{{ km/cm}} = {_fmt_sa(ground_km)}\\text{{ km}}$$\n\n"
        f"3. Travel Time ($t = d/v$):\n"
        f"   $$t = \\frac{{{_fmt_sa(ground_km)}\\text{{ km}}}}{{{avg_speed}\\text{{ km/h}}}} = {_fmt_sa(total_hours, 2)}\\text{{ hours}}$$\n"
        f"   Decimal to minutes: $0{_fmt_sa(total_hours - hrs, 2)[1:]} \\times 60 = {mins}\\text{{ minutes}}$\n"
        f"   Time = **{hrs} hour{'s' if hrs != 1 else ''} and {mins} minute{'s' if mins != 1 else ''}**\n\n"
        f"4. Fuel Cost:\n"
        f"   $$\\text{{Litres consumed}} = \\frac{{{_fmt_sa(ground_km)}}}{{100}} \\times {_fmt_sa(litres_per_100km)} = {_fmt_sa(fuel_used)}\\text{{ litres}}$$\n"
        f"   $$\\text{{Cost}} = {_fmt_sa(fuel_used)}\\text{{ L}} \\times \\text{{R}}{_fmt_sa(fuel_price_per_l)} = \\text{{R}}{_fmt_sa(fuel_cost)}$$"
    )

    ans_latex = (
        rf"\text{{Distance}} = {_fmt_sa(ground_km)}\text{{ km}}, \quad "
        rf"\text{{Time}} = {hrs}\text{{ h }} {mins}\text{{ min}}, \quad "
        rf"\text{{Fuel Cost}} = \text{{R}}{_fmt_sa(fuel_cost)}"
    )

    marking_schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Identify 1 cm = 0.5 km on 1:50 000 map", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate ground distance: {measured_cm} x 0.5 = {_fmt_sa(ground_km)} km", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Calculate travel time in hours and minutes", "marks": 2, "editable": True},
            {"id": "mp4", "desc": f"Calculate fuel consumption in litres: {_fmt_sa(fuel_used)} L", "marks": 1, "editable": True},
            {"id": "mp5", "desc": f"Calculate total fuel cost: R{_fmt_sa(fuel_cost)}", "marks": 2, "editable": True},
        ],
        "deductions": [{"rule": "treated_decimal_hours_as_minutes", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy",
    }

    hints = {
        "tier_1": "On a 1:50 000 map, 1 cm represents 0,5 km (50 000 cm / 100 000).",
        "tier_2": "Calculate distance = cm x 0,5. Travel time = distance / speed. Fuel used = (distance / 100) x consumption. Cost = litres x price.",
        "tier_3": f"Distance = {_fmt_sa(ground_km)} km. Time = {hrs} h {mins} min. Fuel cost = R{_fmt_sa(fuel_cost)}.",
    }

    return {
        "id": f"mathlit_map_comp_{r.randint(100000, 999999)}",
        "question_id": f"mathlit_map_comp_{r.randint(100000, 999999)}",
        "topic": "mathematical_literacy_maps_scales",
        "subskill": "maps_scales_compound",
        "learning_objective_id": "mathlit_maps_scales_compound",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_latex": ans_latex,
        "sample_answer": sample_answer,
        "marking_schema": marking_schema,
        "hints": hints,
        "misconception_tags": [
            "confused_cm_to_km_conversion_factor",
            "treated_decimal_as_minutes",
            "forgot_to_divide_fuel_by_100",
        ],
        "keywords": ["topographic map", "1:50000", "scale", "ground distance", "travel time", "fuel consumption"],
        "term": 2,
        "caps_weight_percent": 35,
        "suggested_duration_mins": 12,
        "mode": "compound",
        "difficulty": "hard",
        "marks": 8,
    }


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_maps_scales,
    "elementary_scale_ratio_conversion": _build_scale_ratio_drill,
    "elementary_travel_time_calc": _build_travel_time_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 10-12 Mathematical Literacy Maps & Scales questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_maps_scales)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
