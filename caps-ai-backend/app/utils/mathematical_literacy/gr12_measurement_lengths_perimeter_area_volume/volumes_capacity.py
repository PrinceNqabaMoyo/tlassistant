"""Subskills 25 to 32: 3D Volume, Liquid Capacity & Fill-Time Mechanics.
Covers rectangular reservoirs, m³ to L/kL conversions, JoJo cylindrical tanks,
flow-rate fill duration, liquid drawdown height, trapezoidal waste skips, and stepped concrete slabs.
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    PI,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Subskill 25: Volume of a rectangular water reservoir."""
    l = r.choice([4.0, 5.0, 6.0])
    w = r.choice([2.5, 3.0, 3.5])
    h = r.choice([1.5, 2.0, 2.2])
    volume_m3 = round(l * w * h, 2)

    prompt = (
        f"A farm irrigation reservoir is built as a rectangular prism with inside dimensions:\n"
        f"• Length: {_fmt(l)} m\n"
        f"• Width: {_fmt(w)} m\n"
        f"• Depth (height): {_fmt(h)} m\n\n"
        f"Using the formula: Volume = Length × Width × Height,\n"
        f"calculate the volume of the reservoir in cubic metres (m³)."
    )

    correct_ans = f"{_fmt(volume_m3)} m³"
    explanation = (
        f"1. Formula: Volume = l × w × h.\n"
        f"2. Substitution: Volume = {_fmt(l)} m × {_fmt(w)} m × {_fmt(h)} m = {correct_ans}."
    )
    t1 = "Multiply length by width by height."
    t2 = f"Calculation: {l} × {w} × {h}."
    t3 = f"Volume = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_25",
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


def gen_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Subskill 26: Converting cubic metres (m³) to Litres and kilolitres (kL)."""
    vol_m3 = r.choice([12.5, 18.0, 24.5, 32.0])
    litres = int(vol_m3 * 1000)
    kl = vol_m3  # 1 m³ = 1 kL

    prompt = (
        f"A municipal water storage tank has a measured volume of {_fmt(vol_m3)} m³.\n\n"
        f"Knowing that 1 m³ = 1 000 Litres = 1 kilolitre (kL),\n"
        f"calculate the capacity of the tank in Litres (L)."
    )

    correct_ans = f"{_fmt(litres)} L"
    explanation = (
        f"1. Conversion rule: 1 m³ = 1 000 L.\n"
        f"2. Capacity in Litres = {_fmt(vol_m3)} m³ × 1 000 L/m³ = {correct_ans}."
    )
    t1 = "Multiply the volume in cubic metres by 1 000."
    t2 = f"Calculation: {vol_m3} × 1 000."
    t3 = f"Capacity = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_26",
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


def gen_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Subskill 27: Volume of a cylindrical water tank / JoJo tank."""
    diameter = r.choice([1.8, 2.0, 2.4])
    radius = diameter / 2.0
    height = r.choice([2.0, 2.5, 3.0])

    vol_m3 = round(PI * (radius ** 2) * height, 3)

    prompt = (
        f"A cylindrical rainwater JoJo tank has an internal diameter of {_fmt(diameter)} m "
        f"(radius = {_fmt(radius)} m) and a vertical height of {_fmt(height)} m.\n\n"
        f"Using the formula: Volume = π × (radius)² × height (where π = 3,142),\n"
        f"calculate the volume of the tank in cubic metres (m³) rounded to 3 decimal places."
    )

    correct_ans = f"{_fmt(vol_m3, 3)} m³"
    explanation = (
        f"1. Radius = Diameter ÷ 2 = {_fmt(diameter)} m ÷ 2 = {_fmt(radius)} m.\n"
        f"2. Formula: Volume = π × r² × h = 3,142 × ({_fmt(radius)})² × {_fmt(height)}\n"
        f"   = 3,142 × {radius**2:.4f} × {height} = {correct_ans}."
    )
    t1 = f"Square the radius ({radius}² = {radius**2:.4f}), then multiply by π (3,142) and height ({height})."
    t2 = f"Calculation: 3,142 × {radius**2:.4f} × {height}."
    t3 = f"Volume = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_27",
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


def gen_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Subskill 28: Capacity in litres of a cylindrical tank from dimensions."""
    diameter = 1.6
    radius = 0.8
    height = 2.5
    vol_m3 = PI * (radius ** 2) * height  # 3.142 * 0.64 * 2.5 = 5.0272 m³
    capacity_litres = int(round(vol_m3 * 1000))  # 5 027 L

    prompt = (
        f"A standard domestic water tank has an internal diameter of 1,6 m (radius = 0,8 m) "
        f"and a height of 2,5 m.\n\n"
        f"Using the formula: Volume = π × r² × h (where π = 3,142),\n"
        f"calculate the total liquid holding capacity of the tank in Litres (1 m³ = 1 000 L, rounded to the nearest whole Litre)."
    )

    correct_ans = f"{_fmt(capacity_litres)} L"
    explanation = (
        f"1. Volume in m³ = 3,142 × (0,8 m)² × 2,5 m = 3,142 × 0,64 × 2,5 = {vol_m3:.4f} m³.\n"
        f"2. Convert to Litres: {vol_m3:.4f} m³ × 1 000 L/m³ = {capacity_litres} L."
    )
    t1 = "Calculate volume in m³: 3,142 × (0,8)² × 2,5."
    t2 = "Multiply the cubic metres result by 1 000 to convert to Litres."
    t3 = f"Capacity = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_28",
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
    """Subskill 29: Fill-time duration for a water tank at a given flow rate."""
    tank_litres = r.choice([2500, 5000, 10000])
    flow_rate_l_per_min = 25  # 25 litres per minute

    time_mins = tank_litres // flow_rate_l_per_min
    hours = time_mins // 60
    rem_mins = time_mins % 60

    if rem_mins == 0:
        correct_ans = f"{hours} hours"
    else:
        correct_ans = f"{hours} hours {rem_mins} minutes"

    prompt = (
        f"An empty water tank with a capacity of {_fmt(tank_litres)} Litres is being filled from a borehole pump.\n"
        f"The pump discharges water at a constant flow rate of 25 Litres per minute.\n\n"
        f"Calculate the total time required to fill the tank completely (in hours and minutes)."
    )

    explanation = (
        f"1. Total minutes = Volume ÷ Flow rate = {_fmt(tank_litres)} L ÷ 25 L/min = {time_mins} minutes.\n"
        f"2. Convert to hours: {time_mins} ÷ 60 = {hours} full hours and {rem_mins} minutes.\n"
        f"3. Result = {correct_ans}."
    )
    t1 = f"Divide total capacity ({_fmt(tank_litres)} L) by the flow rate (25 L/min) to get total minutes."
    t2 = f"Divide {time_mins} minutes by 60 to find hours and remaining minutes."
    t3 = f"Time = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_29",
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
    """Subskill 30: Depth / liquid height drawdown in a cylindrical water tank."""
    # Cylinder radius = 1,0 m (area = pi * r^2 = 3.142 m^2)
    # Consumed 2 500 Litres = 2,5 m^3
    # Drop in height = Volume / Area = 2,5 / 3,142 = 0,796 m = 0,80 m
    radius = 1.0
    litres_drawn = 2500
    vol_drawn_m3 = litres_drawn / 1000.0  # 2.5 m^3
    base_area = PI * (radius ** 2)        # 3.142 m^2
    height_drop_m = round(vol_drawn_m3 / base_area, 2)

    prompt = (
        f"A cylindrical community water tank with an internal radius of 1,0 m supplies water to a clinic.\n"
        f"During a single day, the clinic consumed 2 500 Litres (2,5 m³) of water from the tank.\n\n"
        f"Using the formula: Height = Volume ÷ (π × r²) (where π = 3,142),\n"
        f"calculate the drop in water level (height drawdown) inside the tank in metres (rounded to 2 decimal places)."
    )

    correct_ans = f"{_fmt(height_drop_m)} m"
    explanation = (
        f"1. Base area of tank = 3,142 × (1,0 m)² = 3,142 m².\n"
        f"2. Height drop = Volume drawn ÷ Base area\n"
        f"   = 2,5 m³ ÷ 3,142 m² = {height_drop_m:.2f} m."
    )
    t1 = "Calculate the circular cross-sectional base area: 3,142 × (1,0)² = 3,142 m²."
    t2 = f"Divide the consumed volume (2,5 m³) by the base area (3,142 m²)."
    t3 = f"Height drop = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_30",
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


def gen_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Subskill 31: Volume of a trapezoidal waste skip prism."""
    # Front face trapezium: top = 2.9m, bottom = 1.5m, height = 0.7m
    # Width (length of prism) = 1.8m
    top_a = 2.9
    bottom_b = 1.5
    h_trap = 0.7
    length_prism = 1.8

    trap_area = 0.5 * (top_a + bottom_b) * h_trap  # 0.5 * 4.4 * 0.7 = 1.54 m²
    skip_volume = round(trap_area * length_prism, 2)  # 1.54 * 1.8 = 2.77 m³

    prompt = (
        f"A commercial waste disposal skip has a side cross-section shaped like a trapezium with dimensions:\n"
        f"• Top edge: {_fmt(top_a)} m\n"
        f"• Bottom base: {_fmt(bottom_b)} m\n"
        f"• Vertical height: {_fmt(h_trap)} m\n"
        f"The skip has a uniform width (length of the prism) of {_fmt(length_prism)} m.\n\n"
        f"Using the formula: Volume = Area of Trapezium × Length = [½ × (a + b) × h] × Length,\n"
        f"calculate the total holding volume of the waste skip in cubic metres (m³) rounded to 2 decimal places."
    )

    correct_ans = f"{_fmt(skip_volume)} m³"
    explanation = (
        f"1. Area of trapezoidal side = 0,5 × ({_fmt(top_a)} + {_fmt(bottom_b)}) × {_fmt(h_trap)}\n"
        f"   = 0,5 × {top_a + bottom_b:.2f} × {_fmt(h_trap)} = {trap_area:.2f} m².\n"
        f"2. Volume of prism = Area × Length = {trap_area:.2f} m² × {_fmt(length_prism)} m = {correct_ans}."
    )
    t1 = f"Calculate the trapezium area: 0,5 × ({top_a} + {bottom_b}) × {h_trap} = {trap_area:.2f} m²."
    t2 = f"Multiply the cross-sectional area by the prism length ({length_prism} m)."
    t3 = f"Volume = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_31",
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


def gen_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Subskill 32: Volume of a composite concrete foundation slab with stepped thickness."""
    # Main slab: 10m x 6m x 0.15m (thickness)
    # Edge beam: perimeter beam 0.3m extra depth x 0.4m width x 32m length
    slab_l, slab_w, slab_thick = 10.0, 6.0, 0.15
    slab_vol = slab_l * slab_w * slab_thick  # 9.0 m³

    beam_l = 32.0  # 2*(10+6)
    beam_w = 0.4
    beam_extra_depth = 0.25
    beam_vol = beam_l * beam_w * beam_extra_depth  # 3.2 m³

    total_concrete_vol = round(slab_vol + beam_vol, 2)

    prompt = (
        f"A building foundation comprises two integrated concrete sections:\n"
        f"• A surface slab measuring 10,0 m by 6,0 m with a thickness of 0,15 m (Volume = 9,00 m³)\n"
        f"• An under-slab perimeter beam trench measuring 32,0 m in length, 0,4 m wide, and 0,25 m deep\n\n"
        f"Calculate the total volume of ready-mix concrete required to cast both sections in cubic metres (m³)."
    )

    correct_ans = f"{_fmt(total_concrete_vol)} m³"
    explanation = (
        f"1. Volume of slab = 10,0 m × 6,0 m × 0,15 m = {_fmt(slab_vol)} m³.\n"
        f"2. Volume of perimeter beam = 32,0 m × 0,4 m × 0,25 m = {_fmt(beam_vol)} m³.\n"
        f"3. Total concrete volume = {_fmt(slab_vol)} m³ + {_fmt(beam_vol)} m³ = {correct_ans}."
    )
    t1 = "Calculate the volume of the perimeter trench: 32,0 × 0,4 × 0,25."
    t2 = f"Add the beam volume ({_fmt(beam_vol)} m³) to the slab volume (9,00 m³)."
    t3 = f"Total volume = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_32",
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
